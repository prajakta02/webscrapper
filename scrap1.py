from urllib.request import urlopen
from bs4 import BeautifulSoup 
  

r = urlopen("http://pythonscraping.com/pages/page1.html")  #pass the link from where u want to scrap the data
  

bobj=BeautifulSoup(r.read(),'html5lib')
f=open("first.txt",'a')
f.write(str(bobj))