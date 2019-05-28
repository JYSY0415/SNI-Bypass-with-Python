from OpenSSL import SSL
import sys, os, select, socket
from selenium import webdriver
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import re
import time

#export PATH=$PATH:/root/Desktop/python_ssl

def fwrite(buf, f):
	while(True):
		f.write(buf+" ")
		buf=sock.recv(4096)		
		if "</html>" in buf:
			f.close()		
			break
#----------------------------------------------------------------------------------#
url = "www.xvideos.com"
port = 443
driver=webdriver.Firefox()
driver.implicitly_wait(3)
ctx=SSL.Context(SSL.SSLv23_METHOD)
sock=SSL.Connection(ctx,socket.socket(socket.AF_INET, socket.SOCK_STREAM))
sock.connect((url,port))

k=sock.send("""GET /video48130111/asian_girl_teasing_his_bulge HTTP/1.1
Host: www.xvideos.com


""".replace("\n","\r\n"))

f = open(url+".html","w")
#------------------------------------------------------------------------------------#
while(True):
	try:						
		buf=sock.recv(4096)
		print(buf)
		page = BeautifulSoup(buf, "html.parser")	
		for link in page.findAll():
			if 'a href' in link.attrs:
				print(link.attrs['a href'])

		if "<!doctype html>" in buf:
			fwrite(buf, f)
			break
	except SSL.SysCallError:
		break
#-----------------------------------------------------------------------------------#
driver.get("file:///root/Desktop/python_ssl/"+url+".html")
	
