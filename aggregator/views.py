from django.shortcuts import render, redirect
from .models import Article
import requests

def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key={secret_key}&countries=us&categories=general')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    category = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
        category.append(i['category'])
    shortenedDesc = []
    for desc in description:
        words = desc.split()
        shortenedDesc.append(" ".join(words[:70]))
    news = zip(title, shortenedDesc, image, url, category)
    return render(request, 'aggregator/index.html', {'news': news})

def home(request):
    return redirect("index.html")

def health(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=3c7d4824e90ecc3cc72bab6b965ba3dd&countries=us&categories=health')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    shortenedDesc = []
    for desc in description:
        words = desc.split()
        shortenedDesc.append(" ".join(words[:70]))
    news = zip(title, shortenedDesc, image, url)
    return render(request, 'aggregator/health.html', {'news': news})

def business(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key={secret_key}&countries=us&categories=business')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    shortenedDesc = []
    for desc in description:
        words = desc.split()
        shortenedDesc.append(" ".join(words[:70]))
    news = zip(title, shortenedDesc, image, url)
    return render(request, 'aggregator/business.html', {'news': news})

def sports(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key={secret_key}&countries=us&categories=sports')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    shortenedDesc = []
    for desc in description:
        words = desc.split()
        shortenedDesc.append(" ".join(words[:70]))
    news = zip(title, shortenedDesc, image, url)
    return render(request, 'aggregator/sports.html', {'news': news})

def entertainment(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key={secret_key}&countries=us&categories=entertainment')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    shortenedDesc = []
    for desc in description:
        words = desc.split()
        shortenedDesc.append(" ".join(words[:70]))
    news = zip(title, shortenedDesc, image, url)
    return render(request, 'aggregator/entertainment.html', {'news': news})

def science(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key={secret_key}&countries=us&categories=science')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    shortenedDesc = []
    for desc in description:
        words = desc.split()
        shortenedDesc.append(" ".join(words[:70]))
    news = zip(title, shortenedDesc, image, url)
    return render(request, 'aggregator/science.html', {'news': news})

def technology(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key={secret_key}&countries=us&categories=technology')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    shortenedDesc = []
    for desc in description:
        words = desc.split()
        shortenedDesc.append(" ".join(words[:70]))
    news = zip(title, shortenedDesc, image, url)
    return render(request, 'aggregator/technology.html', {'news': news})
