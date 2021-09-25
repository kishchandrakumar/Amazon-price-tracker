'''
A script to notify when an item on amazon is available, 
or if available, track its price and store historic prices.
'''
import requests
import csv
from bs4 import BeautifulSoup
from datetime import date


# User-Agent key contains information about the browser
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'} #Identifies the type of browser and version
url = "https://www.amazon.co.uk/Adidas-Gymnastics-Black-Footwear-White/dp/B079L56FNM/ref=sxin_18_ac_d_rm?ac_md=3-3-YWRpZGFzIHNob2Vz-ac_d_rm_rm_rm&cv_ct_cx=shoes&dchild=1&keywords=shoes&pd_rd_i=B079L56FNM&pd_rd_r=d014aeac-758e-4b5a-a184-609e5d291bd8&pd_rd_w=Lb5KS&pd_rd_wg=df4N1&pf_rd_p=73573abc-9548-43f0-87cb-a185286cee4c&pf_rd_r=AVF547YARHQKJ743J16A&psc=1&qid=1632321242&sr=1-4-fe323411-17bb-433b-b2f8-c44f2e1370d4"

r = requests.get(url, headers = headers)
# Response will be HTML so needs parsing using beautiful soup
print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')

#Find unique elements in the soup using HTML tag as 'id', and assign to individual variables
title  = soup.find(id='productTitle').get_text(strip=True)
rrp    = soup.find("span", {'class':"priceBlockStrikePriceString"}).get_text(strip=True)
current_price  = soup.find(id='priceblock_ourprice').get_text(strip=True)

# Remove '£' sign and convert to float
rrp = float(rrp[1:])
current_price = float(current_price[1:])
perc_saving = (rrp-current_price)/rrp
date = str(date.today())

#Creates CSV with correct headers if one doesn't exist:
try:   #If CSV file doesn't yet exist, create one with headers:
    with open('price-drop.csv', 'r') as f:
        pass
except:
    with open('price-drop.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Date','Product','RRP','Current Price','Percentage Saving','Link'])
finally:
    with open('price-drop.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        data   = [date, title, rrp, current_price, perc_saving,url]
        writer.writerow(data)

#TODO: email notification if perc_saving > 0.1


item1 = {
		 "adidas mens defiant generation tennis shoe" : 
		 "https://www.amazon.co.uk/adidas-Defiant-Generation-Racquetball-Black/dp/B08N5N1B7B/ref=sr_1_14?dchild=1&keywords=adidas%2Btennis%2Bcourt%2Bshoes%2Bred%2Bblack&qid=1632320961&qsid=257-4680912-6359131&sr=8-14&sres=B07ZGV63TG%2CB07KX769FJ%2CB08N5F15HZ%2CB0919RVT78%2CB08BX4KKV3%2CB08N5CN2C8%2CB07S62Z35L%2CB07ZQG7WR7%2CB082W4L2JY%2CB07KFQJ7CH%2CB07SCDJSRN%2CB07S8428FL%2CB07FM9KB5D%2CB08N5LPVN1%2CB07S963B86%2CB0784W8M7V%2CB07D98RJY6%2CB07SC149KY%2CB074HFR9YV%2CB0721TM38H&srpt=SHOES&th=1&psc=1"
		 }

item2 = {"adidas Men's Vs Pace Gymnastics Shoes":
		 "https://www.amazon.co.uk/Adidas-Gymnastics-Black-Footwear-White/dp/B079L56FNM/ref=sxin_18_ac_d_rm?ac_md=3-3-YWRpZGFzIHNob2Vz-ac_d_rm_rm_rm&cv_ct_cx=shoes&dchild=1&keywords=shoes&pd_rd_i=B079L56FNM&pd_rd_r=d014aeac-758e-4b5a-a184-609e5d291bd8&pd_rd_w=Lb5KS&pd_rd_wg=df4N1&pf_rd_p=73573abc-9548-43f0-87cb-a185286cee4c&pf_rd_r=AVF547YARHQKJ743J16A&psc=1&qid=1632321242&sr=1-4-fe323411-17bb-433b-b2f8-c44f2e1370d4"}

all_items = [item1, item2] #list of dictionaries

for item in all_items:
	pass