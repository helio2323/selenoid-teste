from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "113.0",
    "selenoid:options": {
        "enableVideo": False
    }
}

options = webdriver.ChromeOptions()
options.add_experimental_option("w3c", False)  # Evita a exceção

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options,
)
