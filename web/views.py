from django.shortcuts import render
import MySQLdb
from web import models
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def insert_data(request):
    url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=1&s=1&click=0"
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    goods_info = soup.select(".gl-item")
    for info in goods_info:
        t = info.select(".p-name.p-name-type-2 a")[0].text.strip()
        p = info.select(".p-price")[0].text.strip()
        models.phone.objects.create(title=t,price=p)
    driver.close()
    return render(request,'data_list.html')

def insert_movie(request):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2864.400'}
    for i in range(0,10):
        link='https://movie.douban.com/top250?start='+str(i*25)
        r=requests.get(link,headers=headers)
        soup=BeautifulSoup(r.text,"lxml")
        movie_list=soup.find_all('div',class_='hd')
        for eachone in movie_list:
            m=eachone.a.span.text.strip()
            models.movie.objects.create(title=m)
    return render(request,'movie_list.html')    

def show(request):
    phone_list=models.phone.objects.all()
    return render(request,'data_list.html',{"p_data":phone_list})

def showmovie(request):
    movies_list=models.movie.objects.all()
    return render(request,'movie_list.html',{"m_data":movies_list})

def index(request):
    return render(request,'index.html')