from keyword_search import KeywordSearchGoogle
from keyword_list import keyword_list
import pandas as pd
import time 

keyword = '공매도'
url = f'https://www.google.com/complete/search?q={keyword}'
add_keyword = False


def select_keyword_list(add_keyword, keyword_list):
    if add_keyword == False:
        keyword_list = keyword_list(keyword)
        keyword_list.insert(0, keyword)
        keyword_list = keyword_list
    else :
        df = pd.read_csv(f"./keyword_list({keyword}_google).csv").iterrows()
        
        keyword_list_2 = []
        for _, row in df:
            keyword_list_2.extend(keyword_list(row[0]))

        keyword_list = set(keyword_list_2) # 중복 제거

    return keyword_list

keyword_list = select_keyword_list(add_keyword, keyword_list)


if __name__ == "__main__":

    keyword_search_google = KeywordSearchGoogle(url, keyword)

    for key_elem in keyword_list:
        keyword_search_google.requests_start(key_elem)
        time.sleep(1)
        keyword_search_google.collect_keyword()

    keyword_search_google.save_csv()

print('최종 리스트 :\n',keyword_search_google.keyword_list)