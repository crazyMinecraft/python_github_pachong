from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


protocol_names = ["Lido", "MakerDAO", "Curve", "AAVE", "Convex Finance", "Uniswap", "JustLend", "PancakeSwap", "Instadapp", "Compound Finance", "Coinbase Wrapped Staked ETH", "Frax Finance", "JustStables", "Balancer", "Rocket Pool", "Venus", "GMX", "Aura", "Sushi", "Liquity", "SUN", "Stargate", "Synthetix", "Arrakis Finance", "Yearn Finance", "dYdX", "Alpaca Finance", "Beefy", "Velodrome", "Morpho", "Euler", "Abracadabra", "Parallel DeFi Super App", "Tornado Cash"]

# 创建 WebDriver 对象
driver = webdriver.Chrome()
button_text = 'Lido'
for button_text in protocol_names:
    print(button_text)
    # 打开网页
    driver.get("https://defillama.com/")

    # 点击Lido按钮
    lido_button = driver.find_element(By.LINK_TEXT, button_text)
    lido_button.click()

    # 等待页面加载完成
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Website')))

    # 点击Website按钮
    website_button = driver.find_element(By.LINK_TEXT, 'Website')
    website_button.click()
    print(4)
    # 等待页面加载完成
    wait.until(EC.title_contains(button_text))
    print(3)
    # 等待页面加载完成

    # 获取页面中的所有链接
    links = driver.find_elements(By.XPATH, "//a[contains(@href,'https://github.com')]")

    # 遍历链接，找到包含"https://github.com"的链接并输出
    for link in links:
        href = link.get_attribute("href")
        if href is not None and "https://github.com" in href:
            print(href)
