import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL='https://www.amazon.in/FX505DT-Graphics-5-3550H-Windows-FX505DT-AL106T/dp/B07RTYFS9S/ref=sr_1_1?dchild=1&keywords=fx505dt&qid=1590455143&sr=8-1'

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'}

def check_price():


    page= requests.get(URL,headers=headers)

    soup= BeautifulSoup(page.content,'html.parser')

    title= soup.find(id="productTitle").get_text()
    price= soup.find(id="priceblock_ourprice").get_text()

    price=(price[2:8])
    converted_price=int((price.replace(',','')))

    if converted_price<58990:
        send_mail()
    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ayush8402@gmail.com','uqiygwdetyxokthi')

    subject='price fell down!'
    body= 'check amazon link now https://www.amazon.in/FX505DT-Graphics-5-3550H-Windows-FX505DT-AL106T/dp/B07RTYFS9S/ref=sr_1_1?dchild=1&keywords=fx505dt&qid=1590455143&sr=8-1'

    msg= f"Subject: {subject}\n\n {body}"

    server.sendmail('ayush8402@gmail.com','unnayansachan23@gmail.com',msg)

    print("email has been sent")

    server.quit()


while (True):
    check_price()
    time.sleep(86400)
