from selenium import webdriver

rows_selector = ".table_dates > tbody > tr"

def main():
	options = webdriver.ChromeOptions()
	#options.add_argument('headless')
	options.add_argument('--no-sandbox')
	driver = webdriver.Chrome(options=options)
	driver.get("https://www.pashbar.co.il/show.php?id=378")
	get_and_save(driver)


def get_and_save(driver):
	rows = len(driver.find_elements_by_css_selector(rows_selector)) - 1 # we dont need the first row
	with open("old_row_count.txt", 'w') as file:
		file.write(str(rows))

if __name__ == "__main__": 
	main()