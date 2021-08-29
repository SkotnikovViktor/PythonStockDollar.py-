import requests
from bs4 import BeautifulSoup
import time
import tkinter as tk
from tkinter import *

while True:
    time.sleep(5)
    link = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+apple+&sxsrf=ALeKk01yMwb7E8QCWuk32G2pR_hYUjwJXA%3A1629639293136&ei=fVIiYavFB4GQxc8P3sqvoAE&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+apple+&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQ-gEyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCCMQ6gIQJzoECCMQJzoNCAAQgAQQhwIQsQMQFDoICAAQgAQQsQM6DgguEIAEELEDEMcBEKMCOgUIABCABDoOCC4QgAQQsQMQxwEQ0QM6CQgjECcQRhCCAjoHCAAQsQMQQzoECAAQQzoLCAAQgAQQsQMQgwE6CggAEIAEEIcCEBRKBAhBGABQknBY-rQBYJ63AWgBcAJ4AYAB6QOIAd4ckgEJMC45LjYuMS4xmAEAoAEBsAEKwAEB&sclient=gws-wiz&ved=0ahUKEwjr97a538TyAhUBSPEDHV7lCxQQ4dUDCA4&uact=5"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    fuul_page = requests.get(link, headers= headers)


#respinse = requests.get(link).text
    soup = BeautifulSoup(fuul_page.content, 'html.parser')
#dolar = soup.find('span', class_ = 'DFlfde SwHCTb')
#box = dolar.find()
#print(dolar)
    convert =  soup.findAll("span", {"class":"IsqQVc NprOob XcVN5d wT3VGc",  "jsname":"vWLAgc"})
    #print('Акция Apple в долларах',convert[0].text)
    a = convert[0].text
    b = convert[0].text
    if a==b:
        print("Цена не изменилась по прежнему:",a)
    elif a!=b:
        print('Новая цена акции Apple',a)
