import time
from selenium import webdriver

def get_chromeBrowser():
    """ Return chrome driver with options """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('useAutomationExtension', False)
    # 第一步，使用chrome开发者模式
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 第二步，禁用启用Blink运行时的功能
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Other parameters
    options.add_argument("--disable-gpu-driver-bug-workarounds") # Disable workarounds for various GPU driver bugs.
    # options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片, 提升速度
    # 第三步，Selenium执行cdp命令
    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => false
                    })
                """
    })
    browser.set_window_size(1280,1200)

    return browser

# 切换到最新打开选项卡
def switchToNewTab(chromeBrowser):
    """ 切换到当前最新打开的窗口 """
    if chromeBrowser.current_window_handle != chromeBrowser.window_handles[len(chromeBrowser.window_handles)-1]:
        chromeBrowser.switch_to.window(chromeBrowser.window_handles[-1])

def closeOtherTabs(chromeBrowser, firstHandle):
    """ Loop through until find the handle """
    for window_handle in chromeBrowser.window_handles:
        if window_handle != firstHandle:
            chromeBrowser.switch_to.window(window_handle)
            chromeBrowser.close()
            time.sleep(1)
    
    chromeBrowser.switch_to.window(firstHandle)
    time.sleep(1)

def closeLastTab(chromeBrowser):
    chromeBrowser.switch_to.window(chromeBrowser.window_handles[-1])
    chromeBrowser.close()
    chromeBrowser.switch_to.window(chromeBrowser.window_handles[-1])
    time.sleep(1)