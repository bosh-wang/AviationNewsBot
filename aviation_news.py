import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl_news():

    stories = []
    urls = []

    for i in range(36, 1, -1):
        url = f'https://flyfttw.com/category/all/page/{i}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all(class_="entry-title ast-blog-single-element")

        for j in range(len(paragraphs)-1, -1, -1):
            story_name = paragraphs[j].text
            a = paragraphs[j].find_all('a')
            url = a[0].get('href')
            stories.append(story_name)
            urls.append(url)


    url = 'https://flyfttw.com/category/all/'
    
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all(class_="entry-title ast-blog-single-element")

    for i in range(len(paragraphs)-1, -1, -1):
        story_name = paragraphs[i].text
        a = paragraphs[i].find_all('a')
        url = a[0].get('href')
        stories.append(story_name)
        urls.append(url)

    # data = {'story' : stories,
    #         'url' : urls,
    #         'read' : False}
    # df = pd.DataFrame(data)
    # df.to_csv('all_news.csv', index=False)

    return stories, urls

def next_news():
    df = pd.read_csv('all_news.csv')
    for i in range(len(df)):
        if not df['read'][i]:
            df['read'][i] = True
            df.to_csv('all_news.csv', index=False)
            break
    return df['story'][i], df['url'][i]
    
def latest_news():
    
    url = 'https://flyfttw.com/category/all/'
    
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all(class_="entry-title ast-blog-single-element")

    return paragraphs[0].text, paragraphs[0].find_all('a')[0].get('href')