import pandas as pd
from tqdm import tqdm
import nltk
import os


def get_text_file_length(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sentence = f.read()
    except Exception as e:
        print(e)
        print(f'Error: {file_path}')
        return -1
    return len(nltk.word_tokenize(sentence))


typical_letter_file_path = '../sec_typical_letter_file/'
single_letter_file_path = '../sec_single_letter_file/'
single_letter_file_list = [i for i in os.listdir(single_letter_file_path) if i.endswith('.txt')]
typical_letter_file_list = [i for i in os.listdir(typical_letter_file_path) if i.endswith('.txt')]
# get df
single_letter_file_df = pd.DataFrame(single_letter_file_list, columns=['single_letter_file_list'])
typical_letter_file_df = pd.DataFrame(typical_letter_file_list, columns=['typical_letter_file_list'])
# get file path
single_letter_file_df['file_path'] = single_letter_file_df['single_letter_file_list'].apply(lambda x: single_letter_file_path + x)
typical_letter_file_df['file_path'] = typical_letter_file_df['typical_letter_file_list'].apply(lambda x: typical_letter_file_path + x)
# get file length
tqdm.pandas()
single_letter_file_df['content_length'] = single_letter_file_df['file_path'].progress_apply(get_text_file_length)
tqdm.pandas()
typical_letter_file_df['content_length'] = typical_letter_file_df['file_path'].progress_apply(get_text_file_length)
# drop file path and save
single_letter_file_df.drop('file_path', axis=1).to_csv('./single_letter_file_length_list.csv', index=False)
typical_letter_file_df.drop('file_path', axis=1).to_csv('./typical_letter_file_length_list.csv', index=False)