from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# dr = webdriver.Chrome()
# dr.get("http://bs.ifengstar.com/ifengSearch")
# dr.maximize_window()
# dr.implicitly_wait(22)
# dr.find_element_by_id("username").send_keys("haoke")
# dr.find_element_by_id("password").send_keys("123456")
# sleep(1)
# dr.find_element_by_id("button").click()
# sleep(1)
# menu = dr.find_element_by_xpath("/html/body/nav/div/div/div[2]/ul/li[3]/a")
# cd = dr.find_element_by_xpath("/html/body/nav/div/div/div[2]/ul/li[3]/dl/dd[2]/a")
# action = ActionChains(dr)
# print("111111")
# sleep(1)
# action.move_to_element(menu).perform()
# sleep(1)
# action.click(cd).perform()
# print("222222")
# sleep(1)
# action.perform()
# print("33333")


# import math
# def is_sqrt(n):
	# return math.sqrt(n) % 1 == 0
# print(list(filter(is_sqrt,range(1,101))))

# new_list = list(map(lambda x:x**2,range(1,11)))
# print(new_list)


for x in range(1,4):
	print("点添加按钮")
	xpath = "//*[@id='layui-layer-iframe%s']"%x
	print(xpath)
















































