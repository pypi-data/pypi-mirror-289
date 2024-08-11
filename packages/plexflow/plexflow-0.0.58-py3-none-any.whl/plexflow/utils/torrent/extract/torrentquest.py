from bs4 import BeautifulSoup

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
                torrent_result['download_name'] = cols[1].find('a').text.strip()
                torrent_result['age'] = cols[2].text.strip()
                torrent_result['torrent_type'] = cols[3].text.strip()
                torrent_result['files'] = cols[4].text.strip()
                torrent_result['size'] = cols[5].text.strip()
                torrent_result['seeders'] = cols[6].text.strip()
                torrent_result['leechers'] = cols[7].text.strip()

        torrent_results.append(torrent_result)

    return torrent_results
