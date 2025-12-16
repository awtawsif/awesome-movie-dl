# Awesome Movie Downloader

This is a command-line tool that allows you to search for and download movies from `dl.freedrivemovie.org`.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- `pip` for installing packages

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/awtawsif/awesome-movie-dl.git
    cd awesome-movie-dl
    ```

2.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the tool, run the following command:

```bash
python main.py
```

You will be prompted to enter a search term. The tool will then scrape the website for download links related to your search and display them in a table.

To exit the script, type `/exit` or `/quit` at the prompt.

## How It Works

The script takes a search term, formats it for the URL, and then scrapes the corresponding page on `dl.freedrivemovie.org`. It uses `BeautifulSoup` to parse the HTML and extract the movie titles and their associated download links. The results are then displayed in a clean, formatted table using the `rich` library.

## Dependencies

-   [requests](https://pypi.org/project/requests/): For making HTTP requests to the website.
-   [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/): For parsing HTML and extracting data.
-   [rich](https://pypi.org/project/rich/): For creating rich, formatted output in the terminal.

## Disclaimer

This tool is for educational purposes only. Please respect the copyrights of the content you are accessing. The developers of this tool are not responsible for any misuse.
