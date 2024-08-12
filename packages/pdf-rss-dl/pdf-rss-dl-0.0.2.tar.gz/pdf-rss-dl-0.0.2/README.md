# PDF RSS Downloader

This Python script downloads and exports RSS feed entries into PDF files. It checks if the entries have already been exported by referencing a `downloaded.dat` file to avoid duplicates. The script handles multiple date formats and ensures that the generated filenames are compatible with the filesystem.

## Features

- **RSS Feed Parsing:** Parses RSS feeds from a list of URLs.
- **PDF Export:** Converts RSS entries (including title, link, publication date, and description) into PDF files.
- **Duplicate Check:** Keeps track of downloaded entries using `downloaded.dat` to prevent duplicate downloads.
- **Filename Sanitization:** Ensures filenames are safe and do not exceed OS limits by truncating and sanitizing them.
- **Multiple Date Formats:** Supports parsing of multiple date formats commonly found in RSS feeds.
- **UTF-8 Character Handling:** Handles special characters in RSS entries to avoid encoding issues.

## Requirements

- Python 3.7 or higher
- [fpdf](https://pypi.org/project/fpdf/) library

You can install the required dependencies using pip:

```bash
pip install fpdf feedparser
```

## Usage
1. Clone the repository:
```
git clone https://github.com/thisisawesome1994/pdf-rss-downloader.git
cd pdf-rss-downloader
```
2. Prepare the RSS Feeds:
   
    -  Create a rss_feeds.txt file in the root directory of the project.
    -  Add the RSS feed URLs, one per line. Example:
```
https://example.com/rss
https://anotherexample.com/feed
```
3. Run the Script:
```
python app.py
```
4. Output:
  
  -  PDFs will be saved in the downloaded_pdfs directory, organized by feed title and year of publication.
5. Check Duplicates:
  -  The script logs downloaded entries in downloaded.dat to avoid processing the same entry multiple times.

## Customization
  -  Filename Length:
    -  The sanitize_filename function truncates filenames to a default of 100 characters. You can modify this value in the script if needed.
  -  Adding New Date Formats:
    -  You can add more date formats to the parse_published_date function if your RSS feed uses a format not covered by the script.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!
