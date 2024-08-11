import logging
import subprocess
import os
import time
from seleniumbase import SB
from pydantic import BaseModel
from typing import Optional, List

class HumanLikeRequestCapture(BaseModel):
    url: str
    html: Optional[str] = None
    screenshot: Optional[bytes] = None
    use_xvfb: Optional[bool] = False
    cookies: Optional[List[dict]] = None    
    

def _execute_request(url: str, take_screenshot: bool = False):
    logging.info("Running test task")
    with SB(uc=True, maximize=True, test=False, headed=True, chromium_arg="--disable-search-engine-choice-screen") as sb:
        logging.info("Opening URL")
        sb.uc_open_with_reconnect(url, reconnect_time=2)
        sb.uc_gui_handle_cf()
        cookies = sb.get_cookies()
        logging.info(cookies)
        time.sleep(10)
        
        if take_screenshot:   
            logging.info("Taking screenshot")
            # make screenshot as bytes
            screenshot = sb.driver.get_screenshot_as_png()
        else:
            screenshot = None
    
        html = sb.get_page_source()
    
        return HumanLikeRequestCapture(url=url, html=html, screenshot=screenshot, cookies=cookies)
            

def get(url: str, take_screenshot: bool = False, use_xvfb: bool = False) -> HumanLikeRequestCapture:
    if not use_xvfb:
        response = _execute_request(url=url, take_screenshot=take_screenshot)
        response.use_xvfb = False
        return response

    # Start Xvfb
    with subprocess.Popen(['Xvfb', ':99', '-screen', '0', '1920x1080x24']) as xvfb_process:
        logging.info("Xvfb started")
        time.sleep(5)
        os.environ['DISPLAY'] = ':99'

        try:
            response = _execute_request(url=url, take_screenshot=take_screenshot)
            response.use_xvfb = True
            return response
        finally:
            xvfb_process.terminate()
            logging.info("Xvfb terminated")