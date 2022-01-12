import sys, getopt, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from celery import Celery

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--headless")
opt.add_experimental_option("prefs",{
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1
})


app = Celery(
   'tasks',
   broker = 'redis://localhost:6379/0',
   backend = 'redis://localhost:6379/1',
)

@app.task
def jit(x,y):
    driver = webdriver.Chrome(options=opt, executable_path="chromedriver")
    url = f"https://ggg.e04e04.ga/{x}?jwt={y}"
    driver.get(url)
    time.sleep(10)
    driver.close()

def jit_test():
    driver = webdriver.Chrome(options=opt, executable_path="chromedriver")
    driver.get(url)
    time.sleep(10)
    driver.close()

if __name__ == '__main__':
    jit_test()

