import pandas as pd
from tqdm import tqdm
import requests
import time
import random
import os


requests.adapters.DEFAULT_RETRIES = 5


class NotFoundList():
    def __init__(self):
        self.not_found_list = []
        self.not_found_list_path = './not_found_list.csv'

    def read_not_found_list(self):
        if os.path.exists(self.not_found_list_path):
            self.not_found_list = pd.read_csv(self.not_found_list_path, header=None)[0].tolist()
        else:
            self.not_found_list = []

    def write_not_found_list(self):
        not_found_list_df = pd.DataFrame(self.not_found_list)
        not_found_list_df.to_csv(self.not_found_list_path, index=False, header=False)

    def add_not_found_list(self, url):
        self.not_found_list.append(url)

    def remove_not_found_list(self, url):
        self.not_found_list.remove(url)

    def is_in_not_found_list(self, url):
        if url in self.not_found_list:
            return True
        else:
            return False


def save_from_url(url, headers):
    destination = url.split('/')[-1]
    # 设置保存路径
    save_path = f'../sec_typical_letter_file/{destination}'
    # 判断文件是否存在
    if os.path.exists(save_path):
        return 0
    else:
        response = requests.get(url=url, headers=headers, stream=True)
        # 判断是否下载成功
        if response.status_code == 200:
            with open(save_path, 'wb') as pdf_file:
                for chunk in response.iter_content(chunk_size=1024):
                    pdf_file.write(chunk)
            return 0
        else:
            raise Exception(f'Error: {response.status_code} - {url}')
        

if __name__ == '__main__':

    custom_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "close",
        "Cookie": '''_gid=GA1.2.1518350710.1702034236; _ga=GA1.2.692162108.1701777511; _gat_UA-30394047-1=1; _gat_GSA_ENOR0=1; _gat_GSA_ENOR1=1; ak_bmsc=BC7C9AC86BA92DAF37DAFE2A304C7243~000000000000000000000000000000~YAAQLEV7aL/55s+LAQAAcXIDShbD3YhdSisRJbCNn50ofiANZb3mN1XHs8/TFTgTEUHVvcPuh8ILudS+1Ay3BbnBx+2b8Mm1oJ3aoM5M+jurT6Kh+9mucRNONBrhZkluMwOYnpeWdpVtX382XGzmxFM6GWqXQ7gWOROZbgR1FI6DJYuNsw1nuS1FoQKI7CImJB4uEALp5PlE8FVFX1ItyexuR7iW5RRhnqzo8i3jgqSA2/xKzRaagsIJ0XJzmuH4nd9p0aUdlerrfGdmWP4LspRfyc8YGFTrBOxwdutktgTVjnEDCnthF9BSjyd217N51V5BYGPiNjeHd67oMcNc3HpPfJc3WiA5jjlFBOdDkaYQiCi3ce0iVXRUHrpgA4XBi2VMJRHGgGVupTi9V5C8r7ZJG6I81vyfLmp0L8EpDRWep1QH45wKya6nttTfkwzLhCKT1lg6j8fmU0WavK0woDoXaFKUgpQXlBnBGN8BiwYGN2VsRylZ2w==; bm_mi=213708BF62525B1329253BA26E0CC937~YAAQLEV7aMD55s+LAQAAcXIDShbV267DHGgNfUlaYfsssJJS0Pekd8HEstJt2UcFasDQ/Mz6Ge7eZl5OzdNp03Mexq+M/nsuF1O6yNCCsi7+8WoNPpz57ECpKh6Xeq39KLKijLZiY1i/ChyYInoLlhbBv73rxxECpJrq7Wp8I1iZSxqxl6tneGo3rVlwL7zjE8tvGmvtbDragQtnfWfLPTfkyt49nH1QYcq2Sj84s+bATNB/yTEn1F/WkN0PEmFjxaWk/OoyyHFXC45Babak0qGNjFrLFlXXaFJMZQv+eD0ex3Lh+iedNd0S3zv2TA+9RTY7ysVnJSzMv/HPNA==~1; _4c_=%7B%22_4c_s_%22%3A%22dZJLT8MwDID%2FyuTzWsVp2iS7oSEhDoBAPI4TbdI1GqxTWlbG1P%2BOs3UPEPRS%2BfNnx3Wzha6yS5igZJwJpRimMhnDwm4amGzBOxNea5hA%2BVoWqkxYhIKlkdCMR3meqEjJ3BaF1qnWJYzhc9dLp2mSIqpE9mMwy0MPb41t3Hx57ikhUGHw3KodRMqgkkxlWjPx0%2BWai%2BAeWhr4M%2B%2B7UyudiUxJnml5VI%2BE1JX%2Fder%2FarEa1C0UtbF0POoYVcyisqE52i8iQjEITWvzUbSzdrMKWmfzUWMWlDB27Qo765xpq1CfJtmJVtbNK1oCqEwEGkYDjHlKQeeWpu7OCrk60WOhxNAu93XX2FA8rXz9bkeImnBN%2FxRedhVhXG9L6%2F1Oo6hxbZi0sUU8r9cDoHuwZ9GePbtAzehx%2BkD89ozcT%2B9uBnR1MXu6vqQg0xwzjkzFYbVSSroS0B82y5GuCBlS0%2BbaN5jQR7Pw9H3%2FDQ%3D%3D%22%7D; _ga_300V1CHKH1=GS1.1.1702048791.6.0.1702048802.0.0.0; bm_sv=D40F1923D3B5D41C85AD2EFE43DC8EDB~YAAQhZHdWJgxBjaMAQAAvRsEShb9e/L74GDgbKDD7c6HQgYpP1ZZ66GJAd8to5Ha85VP/gFyy7KHYj+wY9byC7zZdcYtpeC2v/KhLd8U6u/3XIzTmxn1oRM0Ro/BUO2Yh0R22FTALVt81grR65YKXJVK8Gz598wRyfW16opuYgf8bHJInUbiuxogPdp3mxfk+4JsZ4gLxPrhh74vRNmeTC8W5kBxdU5zuEYo+k6Gr9hS2j5O3OCDEiZrL11Q~1'''
    }

    # load data
    df = pd.read_csv('../type_letter_urls_final.csv', header=None)
    # load not found list
    not_found_list = NotFoundList()
    not_found_list.read_not_found_list()
    # iterate over rows
    with tqdm(total=df.shape[0]) as pbar:
        for index, row in df.iterrows():
            not_found_count = 0
            url = df.loc[index, 3]
            # url = df.loc[index, 'pdf_url']
            # 判断是否在not found list中
            if not pd.isna(url) and not not_found_list.is_in_not_found_list(url):
                while True:
                    try:
                        res = save_from_url(url, custom_headers)
                        break
                    except Exception as e:
                        print(e)
                        not_found_count += 1
                        if not_found_count > 2:
                            not_found_list.add_not_found_list(url)
                            not_found_list.write_not_found_list()
                            break
                        time.sleep(random.random() * 100 + 100)
                        continue
                if res:
                    time.sleep(random.random() * 2 + 1)
            pbar.update(1)
            