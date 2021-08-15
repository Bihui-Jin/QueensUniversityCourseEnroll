from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import pause


pause.until(datetime.datetime(2021,8,11,7,45,0)) # set time before 15 mins of your enrollment begin time

solus = 'https://my.queensu.ca/sidebar/20'
netId = '' #Your NetId here
pwd = '' #Your password here
term = ['2021 Fall', '2022 Winter']
driver = webdriver.Chrome(executable_path="/home/user/Documents/chromedriver_linux64/chromedriver")


def exp_do(driver):
	driver.refresh()
	wait = WebDriverWait(driver,20)
	wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Enroll']"))).click()
	
	if len(driver.find_elements_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK')) > 0:
		driver.find_element_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK').click()
	flag = True
	while flag:
		for i in range(1,4):
			element = driver.find_element_by_xpath(f"//tr[@id='trSSR_DUMMY_RECV1$0_row{i}']")
			termName = element.find_element_by_tag_name('span').text
			if termName in term:
				element.find_element_by_tag_name('input').click()
				wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='DERIVED_SSS_SCT_SSR_PB_GO']"))).click()

				##Proceed to Step 2 of 3
				wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@title='Enroll in Classes']"))).click()

				##Confirm classes
				wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='DERIVED_REGFRM1_SSR_PB_SUBMIT']"))).click()
				term.remove(termName)
				driver.refresh()
				wait.until(EC.element_to_be_clickable((By.ID, 'selectedtab')))
				driver.find_element_by_id('selectedtab').find_element_by_tag_name('a').click()

				if len(driver.find_elements_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK')) > 0:
					driver.find_element_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK').click()##change term
				else:
					wait.until(EC.element_to_be_clickable((By.ID, 'selectedtab')))
					driver.find_element_by_id('selectedtab').find_element_by_tag_name('a').click()
					if len(driver.find_elements_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK')) > 0:
						driver.find_element_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK').click()##change term

				wait.until(EC.element_to_be_clickable((By.ID, 'SSR_DUMMY_RECV1$scroll$0')))

			if len(term) == 0:
				flag = False

try:

	driver.get(solus)
	wait = WebDriverWait(driver,20)
	wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]'))).send_keys(netId)
	wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))).send_keys(pwd)

	driver.find_element(By.XPATH, '//button[@class="form-element form-button"]').click()

	wait.until(EC.element_to_be_clickable((By.ID, "ptifrmtgtframe")))

	driver.get(driver.find_element_by_id("ptifrmtgtframe").get_attribute("src"))

	##Enroll function on the top-left bar
	wait.until(EC.element_to_be_clickable((By.ID, "DERIVED_SSS_SCR_SSS_LINK_ANCHOR3"))).click()
	wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='DERIVED_SSS_SCT_SSR_PB_GO']")))

	while len(term) != 0:
		for i in range(1,4):
			element = driver.find_element_by_xpath(f"//tr[@id='trSSR_DUMMY_RECV1$0_row{i}']")
			termName = element.find_element_by_tag_name('span').text
			if termName in term:
				element.find_element_by_tag_name('input').click()
				wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='DERIVED_SSS_SCT_SSR_PB_GO']"))).click()

				pause.until(datetime.datetime(2021,8,11,8,0,0)) # set time at your enrollment begin time

				##Proceed to Step 2 of 3
				wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@title='Enroll in Classes']"))).click()
				##Confirm classes
				wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='DERIVED_REGFRM1_SSR_PB_SUBMIT']"))).click()
				term.remove(termName)

				driver.refresh()
				wait.until(EC.element_to_be_clickable((By.ID, 'selectedtab')))
				driver.find_element_by_id('selectedtab').find_element_by_tag_name('a').click()

				if len(driver.find_elements_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK')) > 0:
					driver.find_element_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK').click()##change term
				else:
					wait.until(EC.element_to_be_clickable((By.ID, 'selectedtab')))
					driver.find_element_by_id('selectedtab').find_element_by_tag_name('a').click()
					if len(driver.find_elements_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK')) > 0:
						driver.find_element_by_id('DERIVED_SSS_SCT_SSS_TERM_LINK').click()##change term

				wait.until(EC.element_to_be_clickable((By.ID, 'SSR_DUMMY_RECV1$scroll$0')))

			
except (TimeoutException, Exception) as exp:
	exp_do(driver)
	
