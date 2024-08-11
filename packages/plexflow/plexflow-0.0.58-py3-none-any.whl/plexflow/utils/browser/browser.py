import logging
import subprocess
import os
import time
from seleniumbase import SB

def get(url: str, screenshot_path: str = None):
    # Start Xvfb
    with subprocess.Popen(['Xvfb', ':99', '-screen', '0', '1920x1080x24']) as xvfb_process:
        logging.info("Xvfb started")
        time.sleep(5)
        os.environ['DISPLAY'] = ':99'

        try:
            logging.info("Running test task")
            with SB(uc=True, test=False, headed=True) as sb:
                logging.info("Opening URL")
                sb.uc_open_with_reconnect(url, reconnect_time=2)
                sb.uc_gui_handle_cf()
                cookies = sb.get_cookies()
                logging.info(cookies)
                time.sleep(10)
                if screenshot_path:                
                    logging.info("Taking screenshot")
                    sb.save_screenshot(screenshot_path)

                # Get HTML content
                html = sb.get_page_source()
                return html
        finally:
            logging.info("Cleaning up")
            # Terminate Xvfb
            xvfb_process.terminate()
            xvfb_process.wait()
            logging.info("Xvfb terminated")
