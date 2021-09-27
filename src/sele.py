from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



if __name__ == '__main__':
    driver = webdriver.Chrome(r'/home/cai/chromedriver_linux64/chromedriver')
    driver.set_window_position(x=50,y=60)
    driver.set_window_size(width=1366, height=700)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """
    })
    #driver.get("https://price.pcauto.com.cn/price/newpower/")
    driver.get("https://price.pcauto.com.cn/price/newpower/q-rl10000.html")
    #driver.get("file:///home/cai/code/js.html")
    
    time.sleep(1)
    #driver.get("https://getman.cn/")
    #element = driver.find_element_by_id("request")
    mapd = {}
    print(driver)

    con = driver.find_elements_by_css_selector("div.thlieBiao")
    print(con)

    for it in con:
        ref = it.find_element_by_css_selector("div.tit > a.sname")
        til = ref.get_attribute('textContent')
        ref = it.find_element_by_css_selector("dl.con-dl > dd.emphs")
        #ref = it.find_element_by_xpath("//dl[@class='con-dl']/dd[@class='emphs red']")
        price = ref.get_attribute('textContent')
        mapd[til] = price
        print(price)
    '''
    for count in range(0,3):
        driver.find_element_by_xpath("//div[@class='page']//a[@class='next']").click()
        time.sleep(1)
        con = driver.find_elements_by_css_selector("div.thlieBiao")
        for it in con:
            ref = it.find_element_by_css_selector("div.tit > a.sname")
            til = ref.get_attribute('textContent')
            ref = it.find_element_by_css_selector("dl.con-dl > dd.pri")
            #ref = it.find_element_by_xpath("//dl[@class='con-dl']/dd[@class='emphs red']")
            price = ref.get_attribute('textContent')
            mapd[til] = price
            #print(price)

    with open('test.txt', 'w') as f:
        loop = 0
        for it in mapd:
            loop += 1
            print(str(loop) + it + ":" + mapd[it])
            f.write(str(loop) + it + ":" + mapd[it] + '\n')
    #driver.close()


    
    for it in ref:
        text = it.get_attribute('outerHTML')
        print(text)
        mapd[text] = 'a'
    find_elements_by_tag_name
    #print(ref)
    #print(driver)
    #element = driver.find_elements_by_class_name("toast-header")
    #print(element)

    '''