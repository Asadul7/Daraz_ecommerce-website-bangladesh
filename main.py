from selenium import webdriver
import gspread
from webdriver_manager.chrome import ChromeDriverManager

google = gspread.service_account(filename = "1.json")
data = google.open("my_data").sheet1

var = open("daraz.txt","r")
link = var.readlines()

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
for i in link:
    c_link = i.replace("\n","")
    driver.get(c_link)
    title = driver.find_element("xpath",'//div[@class="pdp-mod-product-badge-wrapper"]').text
    price = driver.find_element('xpath','//div[@class="pdp-product-price"]//span').text
    imag = driver.find_elements('xpath','//div[@class="next-slick-list"]//div')
    total_images = []

    for image_link in imag:
        images = image_link.find_element("xpath",'.//img').get_attribute('src')
        total_images.append(images)
    total = [title,price,str(total_images)]
    print(total)
    data.append_row(total)

driver.quit()
