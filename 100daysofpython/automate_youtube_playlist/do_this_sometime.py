"""Uses firefox browser driver"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.youtube import Youtube

url = "https://www.youtube.com/playlist?list=PLZ2c3JLxOIdVv-nVa0jnnI0tDUezvnCHK"
url2 = 'https://www.youtube.com/playlist?list=PLZ2c3JLxOIdXCzy-g2SOwW8Tk304LdbX5'
video_title_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string'
video_duration_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[24]/div[2]/div[1]/div[1]/span[3]'
number_of_videos_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-playlist-sidebar-renderer/div/ytd-playlist-sidebar-primary-info-renderer/div[1]/yt-formatted-string[1]/span[1]'

with Youtube(url2, headless=False) as yt:
    WebDriverWait(yt, 5).until(EC.presence_of_element_located(
        (By.XPATH, number_of_videos_xpath)))

    number_of_videos = yt.find_element_by_xpath(number_of_videos_xpath)
    nov = int(number_of_videos.text)

    print(f"Found {nov} videos.", '\n')

    yt.find_element_by_xpath('//*[@id="img"]').click()

    while nov != 0:
        # Wait until 5 seconds to get the video_title else video_title returns an empty string,
        # returns TimeOutExceptions if failed
        WebDriverWait(yt, 15).until(
            EC.presence_of_element_located((By.XPATH, video_title_xpath)))

        # Wait until 5 seconds to get the duration,
        # returns TimeOutExceptions if failed
        WebDriverWait(yt, 15).until(
            EC.presence_of_element_located((By.XPATH, video_duration_xpath)))

        video_title = yt.find_element_by_xpath(video_title_xpath)
        video_duration = yt.find_element_by_xpath(video_duration_xpath)
        video_duration_minute = str(video_duration.text).replace(':', '.')

        print(f"Playing : {video_title.text}")
        print(video_duration_minute.split('.'))
        if int(video_duration_minute.split('.')[0]) > 0:
            print('If block')
            print(f"{float(video_duration_minute)*60} seconds", '\n')
            time.sleep(float(video_duration_minute)*60)
            # time.sleep(2)
        else:
            print('else block')
            print(f"{video_duration_minute.split('.')[1]} seconds")
            time.sleep(int(video_duration_minute.split('.')[1]))
            # time.sleep(2)

        nov -= 1
