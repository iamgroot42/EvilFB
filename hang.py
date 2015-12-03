import webbrowser
import threading
# Optional import:
try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	import base64
except:
	print "Selenium not installed"

url="http://9gag.com/"

def chrome_hang():
	try:
		while True:
			webbrowser.open_new_tab(url)
	except:
		print "Should've hanged by now"

def firefox_hang():
	try:
		driver=webdriver.Firefox()
		while True:
			driver.get(url)
	except:
		print "Should've hanged by now"

try:
	thread1=threading.Thread(target=chrome_hang)
	thread2=threading.Thread(target=firefox_hang)
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
except:
  print "Error creating threads"