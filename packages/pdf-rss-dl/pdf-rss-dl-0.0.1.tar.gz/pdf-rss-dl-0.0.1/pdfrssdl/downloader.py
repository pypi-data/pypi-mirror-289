import os
import feedparser
from datetime import datetime
from fpdf import FPDF
import hashlib

# Define file paths
RSS_FEEDS_FILE = "rss_feeds.txt"
PDF_DOWNLOAD_DIR = "downloaded_pdfs"
DOWNLOADED_ENTRIES_FILE = "downloaded.dat"


def sanitize_filename(filename, max_length=100):
    """Sanitize and truncate the filename to avoid issues with long paths or invalid characters."""
    # Remove any unwanted characters
    filename = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()

    # Truncate the filename if it's too long
    if len(filename) > max_length:
        # Create a hash of the full title to ensure uniqueness
        hash_suffix = hashlib.md5(filename.encode('utf-8')).hexdigest()[:8]
        filename = filename[:max_length-9] + '_' + hash_suffix
    
    return filename

def load_downloaded_entries():
    """Load the set of downloaded entry IDs from the file"""
    if not os.path.exists(DOWNLOADED_ENTRIES_FILE):
        return set()
    with open(DOWNLOADED_ENTRIES_FILE, 'r') as file:
        return set(line.strip() for line in file.readlines())

def save_downloaded_entry(entry_id):
    """Save an entry ID to the downloaded entries file"""
    with open(DOWNLOADED_ENTRIES_FILE, 'a') as file:
        file.write(f"{entry_id}\n")

from datetime import datetime

def parse_published_date(date_string):
    """Try multiple datetime formats to parse the published date."""
    date_formats = [
        '%a, %d %b %Y %H:%M:%S %Z',   # Format like: Fri, 09 Aug 2024 16:34:41 GMT
        '%a, %d %b %Y %H:%M:%S %z',    # Format like: Sat, 10 Aug 2024 01:23:37 +0200
        '%Y-%m-%dT%H:%M:%S%z',         # ISO 8601 format (rare in RSS, but sometimes used)
        '%a, %d %b %Y %H:%M:%S',       # Without timezone (Sat, 10 Aug 2024 01:23:37)
        '%d %b %Y %H:%M:%S %Z',        # Without weekday (10 Aug 2024 01:23:37 GMT)
        '%d %b %Y %H:%M:%S %z'         # Without weekday, with timezone (10 Aug 2024 01:23:37 +0200)
    ]

    for fmt in date_formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue

    raise ValueError(f"Date format not recognized: {date_string}")

def export_entry_to_pdf(entry, feed_title):
    """Export the RSS entry to a PDF file"""
    # Ensure base download directory exists
    os.makedirs(PDF_DOWNLOAD_DIR, exist_ok=True)

    # Parse the published date using the correct format
    published_date = parse_published_date(entry.published)
    
    # Create sub-directory based on Feed Title and year
    feed_dir = os.path.join(
        PDF_DOWNLOAD_DIR,
        sanitize_filename(feed_title),
        published_date.strftime('%Y')
    )
    os.makedirs(feed_dir, exist_ok=True)

    # Construct and sanitize PDF filename
    pdf_filename = os.path.join(
        feed_dir,
        f"{published_date.strftime('%Y-%m-%d')} - {sanitize_filename(entry.title)}.pdf"
    )

    # Create a PDF document
    pdf = FPDF()
    pdf.add_page()

    # Set font with support for UTF-8 characters
    pdf.set_font("Arial", size=12)
    
    # Function to add UTF-8 text
    def add_utf8_text(pdf, text):
        pdf.multi_cell(0, 10, text.encode('latin-1', 'replace').decode('latin-1'))

    # Add title and other information to the PDF
    add_utf8_text(pdf, f"Title: {entry.title}")
    add_utf8_text(pdf, f"Link: {entry.link}")
    add_utf8_text(pdf, f"Published: {entry.published}")
    add_utf8_text(pdf, f"Description: {entry.description}")

    # Save the PDF
    pdf.output(pdf_filename)
    print(f"Exported: {entry.title} to {pdf_filename}")
    save_downloaded_entry(entry.id)

# Remaining part of your script remains unchanged




def fetch_entries_for_feed(feed_url, downloaded_entries):
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        entry_id = entry.id
        entry_title = entry.title

        # Check if the entry is already downloaded
        if entry_id in downloaded_entries:
            print(f"Skipping already exported entry: {entry_title}")
            continue

        # Print entry information
        print(f"Found entry: {entry_title} published on {entry.published} from feed {feed.feed.title}")

        # Export the entry to PDF
        export_entry_to_pdf(entry, feed.feed.title)

def load_feed_urls():
    with open(RSS_FEEDS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def fetch_entries():
    downloaded_entries = load_downloaded_entries()
    feed_urls = load_feed_urls()
    for feed_url in feed_urls:
        print(f"Fetching entries for feed: {feed_url}")
        fetch_entries_for_feed(feed_url, downloaded_entries)

def main():
    fetch_entries()

if __name__ == "__main__":
    main()
