import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

def get_chromeBrowser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('useAutomationExtension', False)
    # 第一步，使用chrome开发者模式
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 第二步，禁用启用Blink运行时的功能
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Other parameters
    options.add_argument("--disable-gpu-driver-bug-workarounds") # Disable workarounds for various GPU driver bugs.
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # 第三步，Selenium执行cdp命令
    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => false
                    })
                """
    })
    return browser


if __name__ == '__main__':
    url = 'https://cn.bing.com'
    browser = get_chromeBrowser()
    browser.get(url)
    search_window = browser.current_window_handle
    
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'search_icon')))

    input = browser.find_element_by_id('sb_form_q')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    time.sleep(1.2)
    
    # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # browser.execute_script('alert("To Bottom")')
    time.sleep(12)
    for window_handle in browser.window_handles:
        if window_handle != search_window:
            browser.switch_to.window(window_handle)
            browser.close()
            time.sleep(1)
    
    browser.switch_to.window(search_window)
    time.sleep(1)
    # browser.close()
    # browser.quit()