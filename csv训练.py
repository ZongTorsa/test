import requests
import csv
from lxml import html
import re 

url = 'https://www.themoviedb.org'
url_top = 'https://www.themoviedb.org/movie/top-rated'
#获得电影名、年份、上映时间、类型、时长、语言、导演、作者、主演、Slogan、简介。
def movie_info(movie_path):
    movie_data = {}
    response = requests.get(movie_path, timeout=15)
    tree = html.fromstring(response.text)
    print(f'正在爬取{movie_path}信息...')
    movie_name = tree.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/h2/a/text()') 
    movie_year = tree.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/h2/span/text()')
    movie_year = re.search(r'\d+', movie_year[0])
    movie_time = tree.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[2]/text()')
    movie_time[0] = movie_time[0].strip()
    movie_type = tree.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[3]/a/text()')
    movie_runtime = tree.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[4]/text()')
    movie_runtime[0] = movie_runtime[0].strip()
    movie_language = tree.xpath('/html/body/div[1]/main/section/div[3]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    movie_director = tree.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    movie_author = tree.xpath('//*[@id="cast_scroller"]/ol/li[1]/p[1]/a/text()')
    movie_slogan = tree.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/h3[@class="tagline"]/text()')
    movie_overview = tree.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/div/p/text()')

    movie_data['电影名'] = movie_name[0] if movie_name else '暂无数据'
    movie_data['年份'] = movie_year[0] if movie_year else '暂无数据'
    movie_data['上映时间'] = movie_time[0] if movie_time else '暂无数据'
    movie_data['类型'] = movie_type if movie_type else '暂无数据'
    movie_data['时长'] = movie_runtime[0] if movie_runtime else '暂无数据'
    movie_data['语言'] = movie_language[0] if movie_language else '暂无数据'
    movie_data['导演'] = movie_director[0] if movie_director else '暂无数据'
    movie_data['主演'] = movie_author[0] if movie_author else '暂无数据'
    movie_data['slogan'] = movie_slogan[0] if movie_slogan else '暂无数据'
    movie_data['简介'] = movie_overview[0] if movie_overview else '暂无数据'
    return movie_data
def movie():
    movie_list = []
    response = requests.get(url_top,timeout=10)
    tree = html.fromstring(response.text)
    movie_url = tree.xpath('/html/body/div[1]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div/div/div[2]/div/a/@href')
    for x in movie_url:
        movie_top = url+x
        movie_list.append(movie_info(movie_top))
    return  movie_list

def csv_self(movie_list):
    with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['电影名', '年份', '上映时间', '类型', '时长', '语言', '导演', '主演', 'slogan', '简介'])
        for movie in movie_list:
            writer.writerow(movie.values())



movie_list = movie()
csv_self(movie_list)
