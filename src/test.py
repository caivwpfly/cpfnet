from selenium import webdriver
from selenium.webdriver import ChromeOptions
'''
brower = webdriver.Chrome(r'/home/cai/chromedriver_linux64/chromedriver')
option.add_experimental_option('excludeSwitches', ['enable-automation'])

#option = ChromeOptions()
brower.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
#option.add_argument("--disable-blink-features")
#option.add_argument("--disable-blink-features=AutomationControlled")
#brower = webdriver.Chrome(options=option)

brower.get("file:///home/cai/code/js.html")
'''

with open('test.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('Hello, world!\n')
    f.write('Hello, world!\n')
