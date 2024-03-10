import requests
from bs4 import BeautifulSoup
import pandas as pd

max_page=45

dates=[]
links=[]

#Iterating thru links
for i in range(0,max_page):
    url=f"https://www.cbsl.gov.lk/en/statistics/economic-indicators/price-report?page={i}"
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    main_html=soup.find('div',class_='wrapper',id="main-wrapper")
    tables=main_html.find("div",class_="view-content")
    pdfs=tables.find_all("div",class_="field-content")
    for i in range(0,len(pdfs),2):
        dates.append(pdfs[i].text)
        links.append(pdfs[i].find("a").get("href"))
        
price_data=pd.DataFrame({"Dates":dates,"Links":links})
        
price_data.to_csv("Data Links.csv",index=False)