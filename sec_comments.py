import pandas as pd
from tqdm import tqdm
import requests
import time
import random
import os


def save_from_url(url, headers):
    destination = url.split('/')[-1]
    save_path = f'../sec_comments_file/{destination}'
    # 判断文件是否存在
    if os.path.exists(save_path):
        return 0
    else:
        response = requests.get(url=url, headers=headers, stream=False)
        # 判断是否下载成功
        if response.status_code == 200:
            with open(save_path, 'wb') as pdf_file:
                pdf_file.write(response.content)
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
        "Cookie": '''_gid=GA1.2.311884299.1701777511; bm_mi=2B5F381419AE01F4E5D35952C9C556C9~YAAQ0ONIFywGePKLAQAA4RvUPxbdB9MXHKjoU1gytyURQsXdbg5aiXlToXti43tDdNxhlZUYhCUsVKY3JY9l5GVOG3KKjoGS6WUQevghhhDPC9VmYfjT+NgWWsLnwCgXlySXOFxVkYDn9t0BjCI93ScL2n0leilAMO1w3Ff6dZ0Wuw2PC/9gQPkKKfb7uX6zJ2Y9007kYzzNetpkVZNb5Fs5dD8B8c8cB9gLkzpdkGgtXujAQyKC6SlKMR/fgQPODsSVW72T7xPtPZCZDeS9/bR8LPclrQQgKOGtNPap4wmbXgrz72GILmSB2ydGpIgQnz6WErBbH7O9TyO7yw==~1; ak_bmsc=6F31ED8303C2A9308C913655612C6333~000000000000000000000000000000~YAAQDVLIF1O95ziMAQAApSrUPxbSIZPUIn4+26fGCHuW055KcF2iT4AvkiLMioTLJuZBtMZTyApYnqBwsJboJHh2DPna4Kq62ADefdo31v0G0M5NG3kDUzr19Q72U1Y8gQwTIcv+WWL9aSkKF8Vxt0sOdYj0Ubwy5kOJ+3a/dPWUBRvWg4KuYz0NdpnggC5fNL5B4AWIkOAVMerXw2jEG2CiGcBEJeQwqJ6Pxg48fhp5Kn9aaWDMkrEnpwzAu0zeUvxYwljR4uT+QGD3gPhcBOq6LibpZeHtlnzadwVtZ1gpGvPSQRs2qkM2PQ99owYAb/yj4626EDjOOXWw1zOzf1LP+WL7EHFSzxxXRhG4Tljv34nP3KvRrgv/+pq/JiDilOu18egaI+SFp+Eu/fLWLBjm1rLrZuvT48XwrZst4sGars7/Q0tR8xsl4LE54EwR2i2AvoMRfLA/+xLAlxzzrW33i2Mj0h4B8JwmPRAW6KS2snHZAh66vbQy9aTfjbzyo6AzMWdG4EhdgYfv8GxubDYcpvWMKS5wl5DAJSJfPZdo5DU=; bm_sv=987A02CB4037D3F5677A66AEE88288C5~YAAQLEV7aFjGw8+LAQAApFX8PxZlxULayW8sAWARj4txU1dZQhbgmfhaJqfvglZ6xIegva0Ku6ZLQ0MDQEa35/aH+UXe7DqA4qSk2wJ6pe4UVGjE2qF6/MfQRnSHCcuoL7zV8eyTA5SO5Y+C6m9onaRoBiYwvsKZ/DfmY5YE/DhbYR81/xEkysO/jAnyxX2ES1AEWxASQLZTpaWssxs1hoxtfB0Qx6MvvM6lQavA1+C11SZKYasumjo+0l4pfA==~1; _ga_300V1CHKH1=GS1.1.1701877915.3.1.1701880553.0.0.0; _ga=GA1.2.692162108.1701777511; _4c_=%7B%22_4c_s_%22%3A%22lVJNj5swEP0rK59DYoPxR25VKlU9bKtW2%2FYYAR6ClTQg4w3dRvnvnQkJ2d1uD%2BUC8%2BbN8Pyej2xoYM%2BWQnNhDNdCCq1mbAtPPVseWfCOXge2ZHVRV6bOeCIkzxNpeZqUZWYSo0uoKmtza2s2Y7%2FOu2yeZ7kQJtOnGau6y44jq1oHuEvYuTBzntQ9TsTfiEjD8bMLrXus4jo%2BdUQboLzr3RYbDg6%2BgvXgXWxoPs%2FUDW3Ab5qIsFGS0C4QZZ7mWAx%2B79phGjSpuoHTnBaElqEdeqDZVRPan3AnhEW4RSPYj%2FMEqQ1QQwhnGla9jyS0h2q%2BaQ8XAM0bsWTEvntC3d3D6ivin54hX1af7y9QRx6T4l1bFTtairHM2Id3628f32OlbCpUKriZU1Raa7QX%2B49hh80mxq5fLhbDMMwvWhbYhD0t7YIjYVBF3%2B5HYVg%2FBL%2FZQLiH2LSYMdaF88QoduQhEQM46P2GZDiyCattbLsJPl3TFlYpm2eWa0wzoiAMgtNzGs91Dj%2B%2FsXOdKsut%2BZs9ZpCQd7D%2Fv1GSPN7UZ7qn22ikFEbQbfRdvBDPd15zo6zl8iU3takk7nWlY2%2F2HdRXhoEik7VWieBgEqllmlitsoSXCoyWjleiYK%2FOkWVvGBaGmzyrpDLE1NPvJ4S8Da9O8i%2Fq6fQH%22%7D'''
    }

    # load data
    df = pd.read_csv('../comment_info_all.csv')
    # iterate over rows
    with tqdm(total=df.shape[0]) as pbar:
        for index, row in df.iterrows():
            if not pd.isna(df.loc[0, 'pdf_url']):
                url = df.loc[0, 'pdf_url']
                while True:
                    try:
                        save_from_url(url, custom_headers)
                        break
                    except Exception as e:
                        print(e)
                        time.sleep(random.random() * 100 + 100)
                        continue
            pbar.update(1)
            time.sleep(random.random() * 5 + 5)