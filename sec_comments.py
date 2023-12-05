# %%
import urllib.request
from pathlib import Path
import requests
import pandas as pd
import io


def save_pdf_from_url(url):
    destination = url.split('/')[-1]
    file = Path(f'../sec_comments_file/{destination}')
    response = requests.get(url)
    file.write_bytes(response.content)
    # 保存地址
    # destination = url.split('/')[-1]
    # print(destination)
    # print(url)
    # # 访问url
    # response = requests.get(url)
    # # bytes_io = io.BytesIO(response.content)  # 转换为字节流
    # # 写入文件
    # with open(f'../sec_comments_file/{destination}', 'wb') as output_file:
    #     output_file.write_bytes(response.content)


def save_html_from_url(url):
    # 保存地址
    destination = url.split('/')[-1]
    # 访问url
    response = requests.get(url)
    # 写入文件
    with open(f'../sec_comments_file/{destination}', 'wb+', encoding='utf-8') as output_file:
        output_file.write(response.text)


# %%
comments_url_df = pd.read_csv('../comment_info_all.csv')
comments_url_df.loc[2, 'pdf_url']

# %%
# headers = {
#     
# }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    ,'Content-Type': 'application/json', 'Content-Length': '311', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
url = 'https://www.sec.gov/comments/s7-01-23/s70123-291639-710162.pdf'
response = requests.get(url, headers=headers)
# %%
response = requests.get('https://httpbin.org/get')
print(response.headers)
# %%
response
# %%
