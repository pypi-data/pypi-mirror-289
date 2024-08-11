from typing import Optional, Dict
import requests
import plexflow.utils.antibot.human_like_requests as human_like_requests
from urllib.parse import urljoin, urlencode, urlunparse, urlparse

class AntibotRestful:
    def __init__(self, base_url: str, use_xvfb: bool = False):
        self._base_url = base_url
        self._use_xvfb = use_xvfb

    def _construct_url(self, path: str, query_params: Optional[Dict[str, str]] = None) -> str:
        # Join the base URL and path
        url = urljoin(self._base_url, path)
        
        # Parse the URL and add query parameters
        url_parts = list(urlparse(url))
        if query_params:
            url_parts[4] = urlencode(query_params)
        return urlunparse(url_parts)

    def get(self, path: str, headers: Optional[Dict[str, str]] = None, query_params: Optional[Dict[str, str]] = None, **kwargs) -> human_like_requests.HumanLikeRequestCapture:
        # Construct the full URL
        url = self._construct_url(path, query_params)
        
        return human_like_requests.get(
            url=url,
            take_screenshot=True,
            use_xvfb=self._use_xvfb
        )