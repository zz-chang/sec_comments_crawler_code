from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import PyPDF2



class Pdf2Txt():
    def __init__(self, pdf_file_path, txt_file_path):
        self.pdf_file_path = pdf_file_path
        self.txt_file_path = txt_file_path

    def get_pdf_content(self):
        text = ''
        with open(self.pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # 获取PDF文件中的页面数
            num_pages = len(pdf_reader.pages)
            # 逐页提取文本
            for page_num in range(num_pages):
                # 获取每一页
                page = pdf_reader.pages[page_num]
                # 提取文本
                text += page.extract_text()
        return text

    def write_txt_file(self):
        with open(self.txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(self.get_pdf_content())


if __name__ == '__main__':
    # file_origin_path = '../sec_typical_letter_file/'
    file_origin_path = '../sec_single_letter_file/'
    file_list = [i for i in os.listdir(file_origin_path) if i.endswith('.pdf')]
    for file in tqdm(file_list):
        # 设置file的路径
        pdf_file_path = os.path.join(file_origin_path, file)
        text_file_path = os.path.join(file_origin_path, file.replace('.pdf', '.txt'))
        # 创建Pdf2Txt类的实例对象
        if not os.path.exists(text_file_path):
            file = Pdf2Txt(pdf_file_path, text_file_path)
            # 写入txt文件
            try:
                file.write_txt_file()
            except Exception as e:
                print(e)
                print(f'Error: {pdf_file_path}')
                continue