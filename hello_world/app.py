from tempfile import mkdtemp
import glob

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

print("chrome起動中")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-dev-tools')
chrome_options.add_argument('--no-zygote')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
chrome_options.add_argument(f"--data-path={mkdtemp()}")
chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--v=99')
chrome_options.add_argument('--single-process')
# chrome_options.add_argument('user-agent=' + ...)
# "/var/task/chrome/linux64/121.0.6167.85/chrome" のような場所にある実行ファイルを指定する。
chrome_options.binary_location = glob.glob("/var/task/chrome/linux64/*/chrome")[0]
service = ChromeService(glob.glob("/var/task/chromedriver/linux64/*/chromedriver")[0])
driver = webdriver.Chrome(service=service, options=chrome_options)
print("chrome起動完了")


def lambda_handler(event, context):
    driver.get("https://example.com/")
    body = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.TAG_NAME, "body"))
    return body.text
