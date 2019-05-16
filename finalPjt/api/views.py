from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from bs4 import BeautifulSoup
import os
import datetime
from django.http import JsonResponse
# Create your views here.

@api_view(['GET'])
def cgv(request, type_id, gender, age):

    url = 'http://www.cgv.co.kr/movies/?lt=1&ot={}'.format(type_id)
    response = requests.get(url).text
    movies = {'data':[]}
    doc = BeautifulSoup(response, 'html.parser')
    doc = doc.select_one('#contents > div.wrap-movie-chart > div.sect-movie-chart')
    docs = doc.findAll('ol')
    for i in range(len(docs)):
        doc = docs[i]
        for content in doc.findAll('li'):
            image = content.find('div',{'class':'box-image'})
            result = content.find('div',{'class':'box-contents'})
            if result:
                movies['data'].append({'title':result.select_one('strong').text, 'image':image.select_one('img')['src'], 'percent': result.select_one('span').text, 'url': 'http://www.cgv.co.kr'+result.select_one('a')['href'] })
    
    for movie in movies['data']:
        response = requests.get(movie['url']).text
        doc = BeautifulSoup(response, 'html.parser')
        reservation_link = doc.select_one('#select_main > div.sect-base-movie > div.box-contents > span.like > a')['href']
        temp = doc.text
        age_i = [temp.index('10대'),temp.index('20대'), temp.index('30대'), temp.index('40대'), temp.index('50대')]
        ages = []
        for age_val in age_i:
            i = 6
            while(temp[age_val+i]!=']'):
                i+=1
            ages.append(temp[age_val+6:age_val+i])
        gender_i = [temp.index('"남 '), temp.index('"여 ')]
        genders = []
        for gender_val in gender_i:
            i = 3
            while(temp[gender_val+i]!='"'):
                i+=1
            genders.append(temp[gender_val+3:gender_val+i-1])
        movie['gender']=genders
        movie['age']=ages
        
    gender-=1
    age-=1
    
    temp_gender = []
    temp_age = []
    for obj in movies['data']:
        temp_gender.append(obj['gender'][gender])
        temp_age.append(obj['age'][age])
    
    age_sorted = sorted(temp_age, reverse=True)[:3]
    gender_sorted = sorted(temp_gender, reverse=True)[:3]
    response = {'data':{'gender_rank':[], 'age_rank':[]}}
    for i in range(3):
        age_now = temp_age.index(age_sorted[i])
        gender_now = temp_gender.index(gender_sorted[i])
        response['data']['age_rank'].append(movies['data'][age_now])
        response['data']['gender_rank'].append(movies['data'][gender_now])
    
    return JsonResponse(response)

@api_view(['GET'])
def naver(request, type_id):
    x = datetime.datetime.now()
    year = str(x.year)
    if x.month<10:
        month='0'+str(x.month)
    else:
        month=str(x.month)
    if x.day-1<0:
        day = '30'
        if x.month-1<0:
            year = str(x.year-1)
            month=str(12)
        else:
            month = str(x.month-1)
    elif x.day-1<10:
        day = '0'+str(x.day-1)
    else:
        day=str(x.day-1)
    cur_date = year+month+day
    if type_id<=3:
        type_id-=1
    elif type_id>=9:
        type_id+=1
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date={}&tg={}'.format(cur_date, str(type_id))
    response = requests.get(url).text
    movies = {'data':[]}
    doc = BeautifulSoup(response, 'html.parser')
    temp = doc.select_one('#old_content > table > tbody')
    
    temp = temp.findAll('tr')
    # print(len(temp))
    
    if len(temp)<=11:
        temp = temp[1:-1]
    else:
        temp = temp[1:11]

    i=1
    for movie in temp:
        movies['data'].append({'title': movie.find('a').text, 'url': 'https://movie.naver.com'+movie.select_one('a')['href'], 'image_url': movie.select_one('img')['src'], 'rank':i, 'naver_point': movie.find('td',{'class':'point'}).text})
        i+=1
    
    # print(movies)
    return Response(movies)

@api_view(['GET'])
def current(request):
    url = 'https://movie.daum.net/premovie/released'
    response = requests.get(url).text
    movies = []
    doc = BeautifulSoup(response, 'html.parser')

    temp = doc.find('div',{'id':'mArticle'})
    movies = temp.findAll('strong',{'class':'tit_join'})
    percents = temp.findAll('dd')
    images = temp.findAll('img')
    percents = [percents[i] for i in range(len(percents)) if i%2]
    
    response = {'data':[]}
    i = 0
    for movie in movies:
        percent = percents[i].text
        percent = percent.split()[1]
        image = images[i]
        response['data'].append({'title':movie.text, 'url':'https://movie.daum.net'+movie.select_one('a')['href'], 'rank':i+1, 'image': image['src'], 'reservation_percent': percent})
        i+=1

    return Response(response)