import time
from keyword_search import KeywordSearch
from keyword_list import keyword_list


keyword ='공매도'
url = "https://whereispost.com/keyword/" 


keyword_list = keyword_list(keyword)

print('keyword_list :',keyword_list)

if __name__ == "__main__":
    keyword_search = KeywordSearch(url, keyword)
    keyword_search.selenium_start()
    keyword_search.search_click(keyword)


    list_keywords = {keyword:[]}

   
    for key_elem in keyword_list:
        # print('keyword_list 2 :',keyword_list)
        # input()
        # input()
        # print(key_elem +' 클릭합니다.')
        keyword_search.search_click(key_elem)
        time.sleep(3)
        keyword_search.collect_keyword()

    keyword_search.save_csv()

    keyword_search.driver.quit()