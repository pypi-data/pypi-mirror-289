from setuptools import setup, find_packages

setup(
    name='pdf-rss-dl',
    version='0.0.2',
    description='A tool to download and export RSS feed entries as PDFs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Joannes J.A. Wyckmans',
    author_email='johan.wyckmans@gmail.com',
    url='https://github.com/thisisawesome1994/pdf-rss-downloader',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fpdf',
        'feedparser',
    ],
    entry_points={
        'console_scripts': [
            'pdf-rss-dl=pdfrssdl.downloader:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
