from bs4 import BeautifulSoup
from tqdm import tqdm
import os




class Html2Txt():
    def __init__(self, html_file_path, txt_file_path):
        self.html_file_path = html_file_path
        self.txt_file_path = txt_file_path

    def get_html_content(self):
        with open(self.html_file_path, 'r', encoding='ISO-8859-1') as html_file:
            html_content = html_file.read()
            # 使用BeautifulSoup解析HTML文档
            soup = BeautifulSoup(html_content, 'lxml')
            # 判断是否有table标签
            if len(soup.body.findAll('table')) > 2:
                return soup.body.findAll('table')[2].text
            else:
                return soup.body.text

    def write_txt_file(self):
        with open(self.txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(self.get_html_content())


if __name__ == '__main__':
    # file_origin_path = '../sec_typical_letter_file/'
    file_origin_path = '../sec_single_letter_file/'
    for file in tqdm(os.listdir(file_origin_path)):
        if file.endswith('.htm'):
            # 设置file的路径
            html_file_path = os.path.join(file_origin_path, file)
            text_file_path = os.path.join(file_origin_path, file.replace('.htm', '.txt'))
            # 创建Html2Txt类的实例对象
            if not os.path.exists(text_file_path):
                file = Html2Txt(html_file_path, text_file_path)
                # 写入txt文件
                try:
                    file.write_txt_file()
                except:
                    print(f'Error: {html_file_path}')
                    break