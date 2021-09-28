from selenium import webdriver

def get_chromeBrowser():
    """
    return chrome driver with options
    """
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
    browser.set_window_size(1280,800)

    return browser
