from urllib.request import urlopen
from bs4 import BeautifulSoup
import linecache
url="http://127.0.0.1:5500/data.html"
html=urlopen(url).read()
soup=BeautifulSoup(html,features="html.parser")

for script in soup(["script","style"]):
    script.extract()  
    
    text = soup.get_text()
    
    lines = (line.strip() for line in text.splitlines())
    
    chunks= (phrase.strip() for line in lines for phrase in line.split(" "))
    
    text= '\n'.join(chunk for chunk in chunks if chunk)
    print(text)