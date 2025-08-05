import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

# Initialize the rich console
console = Console()

def extract_links(html):
    """
    Extracts titles and associated download links from the HTML content.
    """
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', class_='entry-content')
    if not content_div:
        return []

    sections = []
    current_title = None

    for element in content_div.children:
        if element.name == 'p' and element.strong:
            current_title = element.strong.get_text(strip=True)
            sections.append({
                'title': current_title,
                'links': []
            })
        elif element.name == 'div' and 'wp-block-buttons' in element.get('class', []):
            if sections:
                for link in element.find_all('a', class_='wp-block-button__link'):
                    link_text = link.get_text(strip=True)
                    link_url = link.get('href')
                    if link_url:
                        sections[-1]['links'].append({
                            'text': link_text,
                            'url': link_url
                        })
    return sections

def main():
    """
    Prompts the user for a search term, scrapes the website, and prints
    the extracted links using the rich library for improved formatting.
    """
    console.print(Panel("[bold green]Welcome to the Link Scraper![/bold green]"))
    keyword = console.input("[bold cyan]Search: [/bold cyan]")
    real_keyword = keyword.lower().replace(" ", "-")
    url = f"https://dl.freedrivemovie.org/{real_keyword}"

    try:
        console.print(f"Fetching links for [yellow]'{keyword}'[/yellow] from [link={url}]{url}[/link]...")
        response = requests.get(url, allow_redirects=True, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        content = response.content

        extracted_data = extract_links(content)

        if extracted_data:
            console.print("\n[bold green]-- Found Links --[/bold green]")
            for section in extracted_data:
                console.print(Panel(Text(section['title'], justify="center", style="bold magenta")))
                
                # Create a table for each section's links
                if section['links']:
                    table = Table(title="", title_style="bold blue")
                    table.add_column("Quality", style="cyan", no_wrap=True)
                    table.add_column("URL", style="green")

                    for link in section['links']:
                        table.add_row(link['text'], link['url'])
                    
                    console.print(table)
                else:
                    console.print("[yellow]No links found for this section.[/yellow]")
        else:
            console.print(f"[bold red]No relevant sections or links found for '{keyword}'.[/bold red]")

    except requests.exceptions.HTTPError as errh:
        console.print(f"[bold red]HTTP Error:[/bold red] {errh}")
    except requests.exceptions.RequestException as err:
        console.print(f"[bold red]An error occurred:[/bold red] {err}")

if __name__ == "__main__":
    main()
