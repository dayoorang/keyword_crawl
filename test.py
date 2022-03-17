from keyword_search import KeywordSearchGoogle

# keyword = '블로그'
# url = f'https://www.google.com/complete/search?q={keyword}'


# data = {'q': keyword,
# 'cp': str(len(keyword)),
# 'client': 'gws-wiz',
# 'xssi': 't',
# 'hl': 'ko',
# 'authuser': '0',
# 'psi': 'wG4xYoHqGs_pwQOGtLdw.1647406785738',
# 'dpr': '1'}


# params = urlencode(data)

# headers = {
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
#         }

# response = requests.get(f'https://www.google.com/complete/search?{params}', headers=headers)
# print(response.status_code)

# results = response.text

# p1 = re.compile(r'''(<b>|\\|\d|\[|\]|,|{|}|[a-zA-Z]+|-|:|'|\)|/|_)''')
# results1 = p1.sub('',results)
# p2 = re.compile(r'</>')
# results2 = p2.sub('',results1)
# print(results2)
# p3 = re.compile(r'""')
# results3 = p3.sub(',',results2)
# print(results3)
# p4 = re.compile(r',,|"|\n')
# results4 = p4.sub('',results3).strip()
# print(results4)
# print(results4.split(','))


if __name__ == "__main__":
    keyword = '블로그'
    url = f'https://www.google.com/complete/search?q={keyword}'
    keyword_search_google = KeywordSearchGoogle(url, keyword)

    keyword_search_google.requests_start()
    keyword_search_google.collect_keyword()
    print(keyword_search_google.keyword_list)