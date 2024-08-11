from bs4 import BeautifulSoup
import dateparser
from plexflow.utils.strings.filesize import parse_size


def extract_torrent_results(html):
    """
    Extracts torrent results from HTML content, resilient to changes in HTML structure.

    Args:
        html: The HTML content as a string.

    Returns:
        A list of dictionaries, each representing a torrent result with keys:
            - 'download_name': The name of the torrent.
            - 'magnet_link': The magnet link for the torrent.
            - 'age': The age of the torrent.
            - 'torrent_type': The type of the torrent (e.g., Movie, Game, etc.).
            - 'files': The number of files in the torrent.
            - 'size': The size of the torrent.
            - 'seeders': The number of seeders for the torrent.
            - 'leechers': The number of leechers for the torrent.
    """

    soup = BeautifulSoup(html, 'html.parser')
    torrent_results = []

    # Find all 'a' tags with 'magnet' in the href attribute
    magnet_links = soup.find_all('a', href=lambda href: 'magnet' in href)

    # Iterate over each magnet link
    for magnet_link in magnet_links:
        torrent_result = {'magnet_link': magnet_link['href']}

        # Find the parent 'tr' (table row) of the magnet link
        parent_row = magnet_link.find_parent('tr')
        if parent_row:
            cols = parent_row.find_all('td')

            # Extract data from columns based on their position 
            # (assuming consistent layout within the table row)
            if len(cols) >= 8:
                torrent_result['name'] = cols[1].find('a').text.strip()
                # get link of name
                link = cols[1].find('a')['href']
                # make it a full link
                torrent_result['link'] = f"https://torrentquest.com{link}"
                age = cols[2].text.strip()
                torrent_result['age'] = age
                if isinstance(age, str):
                    age_str = f"{age} ago"
                    date = dateparser.parse(age_str)
                    torrent_result['date'] = date
                else:
                    torrent_result['date'] = None
                torrent_result['type'] = cols[3].text.strip().lower()
                torrent_result['files'] = cols[4].text.strip()
                size_human = cols[5].text.strip()
                torrent_result['size'] = size_human

                if isinstance(size_human, str):
                    sizes = parse_size(size_human)
                    if sizes:
                        torrent_result['size_bytes'] = sizes[0]
                    else:
                        torrent_result['size_bytes'] = None
                
                torrent_result['seeds'] = cols[6].text.strip()
                torrent_result['peers'] = cols[7].text.strip()

        torrent_results.append(torrent_result)

    return torrent_results
