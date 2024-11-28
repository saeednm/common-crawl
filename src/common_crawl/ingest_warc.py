from warcio.archiveiterator import ArchiveIterator
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import validators

warc_file_directory = "commoncrawl_segments"
txt_file_directory = "links_txt"

def extract_external_links(warc_file):
    external_links = {}  # Store links in a dictionary 

    # Open the WARC file
    with open(warc_file, 'rb') as stream:
        for record in ArchiveIterator(stream):
            if record.rec_type == 'response':  # Look for HTTP response records
                url = record.rec_headers.get_header('WARC-Target-URI')
                content_type = record.http_headers.get_header('Content-Type')

                # Process HTML content only
                if content_type and 'text/html' in content_type:
                    payload = record.content_stream().read()
                    try:
                        soup = BeautifulSoup(payload, 'html.parser')

                        # Extract all anchor tags with href
                        for link in soup.find_all('a', href=True):
                            href = link['href'].strip()
                            parsed_href = urlparse(href)

                            # Check if the link is external
                            if parsed_href.scheme in ('http', 'https') and urlparse(url).netloc != parsed_href.netloc:
                                if url not in external_links:
                                    external_links[url] = []
                                external_links[url].append(href)
                    except:
                        pass

    return external_links




# Save the external links to a file
def save_links_to_file(links, filename):
    file_complete_name = os.path.join(txt_file_directory, filename)
    os.makedirs(os.path.dirname(file_complete_name), exist_ok=True)
    with open(file_complete_name, "w") as file:
        for page, external_links in links.items():
            for link in external_links:
                if validators.url(link, private=False): # filter malformatted urls
                    file.write(f"{link}\n")  # Write one link per line


def extract_and_save_external_links():
    with os.scandir(warc_file_directory) as iter:
        for entry in iter:
            if entry.name.endswith(".warc.gz") and entry.is_file():
                print(entry.name, entry.path)
                links = extract_external_links( entry.path)
                save_links_to_file(links, entry.name + ".txt")

    print("done!")

