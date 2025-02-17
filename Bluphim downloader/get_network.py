from time import sleep
from seleniumwire import webdriver


driver = webdriver.Chrome()
driver.get('https://bluphim.net/xem-phim/solo-leveling-3927/')
sleep(10)
for request in driver.requests:
    if request.response:
        if 'https://cdn.xyncdn.tech/' in request.url:
            print(request.url)
            print(request.headers)      
        