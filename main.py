from fastapi import FastAPI
import datetime
from selenium.webdriver.common.by import By
from youtube.youtube import YouTube
from google_client.gspwrite import write

app = FastAPI()


@app.get('/scrap')
def write_sps():
    with YouTube(teardown=True) as bot:
        bot.land_first_page()
        rand = bot.find_elements(By.ID, "details")
        i = 0
        n = 0
        while n < 10:
            if rand[i].find_element(By.ID, "video-title").text.strip() != "":
                write([[str(datetime.datetime.now()), rand[i].find_element(By.ID, "video-title").text,
                        rand[i].find_element(By.ID, "channel-name").text]])
                n += 1
            i += 1
        return {"message": "Success"}
