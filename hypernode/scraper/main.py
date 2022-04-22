import os
from logging import getLogger
from typing import List
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from hypernode.common.logging import configure_logging
from hypernode.scraper.input import parse_args

logger = getLogger(__name__)


scraped_urls = []


def scrape(url: str) -> List[str]:
    try:
        logger.info(f"Fetching {url}")
        response = requests.get(url)
    except Exception:
        logger.warning(f"Failed to fetch {url}")
        return []
    result = [url]
    url_parts = urlparse(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all(name="a")
    for link in links:
        if link.has_attr("href"):
            link_url = link["href"]
            if link_url.startswith("/"):
                link_url = f"{url_parts.scheme}://{url_parts.hostname}{link_url}"
            elif link_url.startswith("http://") or link_url.startswith("https://"):
                link_url = link_url
            else:
                continue
            link_url = link_url.split("#")[0].rstrip("/")
            if "?" not in link_url:
                link_url = link_url + "/"
            link_url_parts = urlparse(link_url)
            if (
                link_url_parts.hostname != url_parts.hostname
                or not link_url_parts.path.startswith("/en/")
            ):
                continue
            if link_url not in scraped_urls:
                scraped_urls.append(link_url)
                result.extend(scrape(link_url))

    return result


def main(args: List[str]) -> int:
    verbose = parse_args(args)
    configure_logging(verbose, logger)
    result = sorted(scrape("https://support.hypernode.com/en/"))
    with open("documentation_urls.txt", "w", encoding="utf-8") as f:
        for link in result:
            f.write(f"{link}\n")
    return os.EX_OK
