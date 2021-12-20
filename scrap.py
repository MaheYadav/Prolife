import  requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
nm = []
rs = []
page_num = input("Enter page number:")
for i in range (1,int(page_num)+1):
    url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=d544b0fb-85fe-4c16-a6e0-89042c7a5e28&page=5"
    req=requests.get(url)
    content=BeautifulSoup(req.content,'html.parser')
    name=content.find_all('div',{"class":"_4rR01T"})
    price=content.find_all('div',{"class":"_30jeq3 _1_WHN1"})
    print("lap in page:"+str(i))
    print(len(name))
    print(len(price))
    for n in name:
        nm.append(n.text)
    for p in price:
        rs.append(p.text)
a=pd.DataFrame({'name':nm,'price':rs})
a.to_csv('products.csv', index=False,header=True, encoding='utf-8')
print(a)

# a={'name':nm,'price':rs,'rating':rt}  Working
# df = pd.DataFrame.from_dict(a, orient='index')
# df.transpose()
# df.to_csv('products.csv', index=False,header=True, encoding='utf-8')1

# for i in lap_name:
#     print(i)
# for i in lap_price:
#       print(i)
# for i in lap_rating:
#     print(i)

# rt = []

# for r in rating:
#     rt.append(r.text)

# rating = content.find_all('div', {"class": "_3LWZlK"})

# print(len(rating))
