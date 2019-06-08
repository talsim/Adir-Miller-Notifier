from selenium import webdriver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config
import smtplib

rows_selector = ".table_dates > tbody > tr"
FROM = config["sender"]
TO = config["recipients"]
password = config["password"]
body = config["body"]
subject = config["subject"]

def main():
	driver = webdriver.Chrome()
	driver.get("https://www.pashbar.co.il/show.php?id=378")
	log_to_file("##STARTED RUNNING##\n")
	check(driver)

def check(driver):
	curr_row_count = len(driver.find_elements_by_css_selector(rows_selector)) - 1 # we dont want the first row
	log_to_file("checking if current count is bigger than before:\n")
	if (curr_row_count > get_from_file()):
		log_to_file("sending mail...\n")
		send_mail()
		save_to_file(curr_row_count)
		log_to_file("leaving\n")
	else: # curr_row_count == get_from_file()
		log_to_file("No changes yet\n")

def save_to_file(curr_row_count):
	log_to_file("saving to file..\n")
	with open("old_row_count.txt", 'w') as file:
		file.write(str(curr_row_count))
	log_to_file("saving complete!\n")


def get_from_file():
	log_to_file("getting from file...\n")
	with open("old_row_count.txt", 'r') as file:
		data = file.read()
	return int(data)


def send_mail():
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo();
		server.starttls()
		server.login(FROM, password)
		msg = MIMEMultipart()
		msg['From'], msg['To'], msg['Subject'] = FROM, ', '.join(TO), subject
		msg.attach(MIMEText(body, 'plain'))
		server.sendmail(FROM, TO, msg.as_string())
		server.close();
		log_to_file("Successfully sended the email!\n")

	except smtplib.SMTPException:
		log_to_file("Error: unable to send mail\n")

def log_to_file(log):
	with open("log.txt", 'a') as logFile:
		logFile.write(log);

if __name__ == "__main__": 
	main()

