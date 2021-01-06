"""Uses firefox browser driver"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.youtube import Youtube
from utils.xpaths import *

url = 'https://www.youtube.com/playlist?list=PLZ2c3JLxOIdXCzy-g2SOwW8Tk304LdbX5'
with Youtube(url) as yt:
    yt.find_element_by_xpath('//*[@id="img"]').click()
    # Wait until 15 seconds,
    # returns TimeOutExceptions if failed
    loop_btn = WebDriverWait(yt, 15).until(
        EC.presence_of_element_located((By.XPATH, loop_xpath)))
    loop_btn.click()
    print("LOOPING FOR AN HOUR.")
    # video_title = yt.find_element_by_xpath(video_title_xpath)
    time.sleep(60*60)
