from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from bs4 import BeautifulSoup
# Create your views here.

@api_view(['GET'])
def cgv(request, type_id, gender, age):
    url = 'http://www.cgv.co.kr/movies/?lt=1&ot={}'.format(type_id)
    response = requests.get(url).text
    movies = {"data":[]}
    
    doc = BeautifulSoup(response, 'html.parser')
    doc = doc.select_one('#contents > div.wrap-movie-chart > div.sect-movie-chart')
    docs = doc.findAll('ol')
    #contents > div.wrap-movie-chart > div.sect-movie-chart > ol:nth-child(3) > li:nth-child(1) > div.box-contents
    #contents > div.wrap-movie-chart > div.sect-movie-chart > ol:nth-child(2) > li:nth-child(1) > div.box-contents
    #contents > div.wrap-movie-chart > div.sect-movie-chart > ol:nth-child(2) > li:nth-child(2) > div.box-contents
    #movie_more_container > li:nth-child(1) > div.box-image
    #movie_more_container > li:nth-child(2) > div.box-contents
    for i in range(len(docs)):
        doc = docs[i]
        for content in doc.findAll('li'):
            image = content.find('div',{'class':'box-image'})
            result = content.find('div',{'class':'box-contents'})
            if result:
                movies['data'].append({'title':result.select_one('strong').text, 'image':image.select_one('img')['src'], 'percent': result.select_one('span').text, 'url': 'http://www.cgv.co.kr'+result.select_one('a')['href'] })
    doc = BeautifulSoup(response, 'html.parser')
    doc = doc.select_one('#movie_more_container')
    print(doc)
    docs = doc.findAll('li')
    for doc in docs:
        image = content.find('div',{'class':'box-image'})
        result = content.find('div',{'class':'box-contents'})
        if result:
            movies['data'].append({'title':result.select_one('strong').text, 'image':image.select_one('img')['src'], 'percent': result.select_one('span').text, 'url': 'http://www.cgv.co.kr'+result.select_one('a')['href'] })

    print(movies)
    

@api_view(['GET'])
def naver(request, type_id):
    pass