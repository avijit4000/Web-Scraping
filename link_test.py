from bs4 import BeautifulSoup as bs
import requests as re
# with open('nameofall.txt', 'a') as file:
#     file.write('\nmyname_ my name is avijit_biswas')

# print('avijit')
website='https://subslikescript.com/'
with open('nameofmovie.txt', 'w') as file:
    file.write('name_of_movie')
for i in range(1,10):
    page_link = f'{website}movies?page={i}'
    result = re.get(page_link)
    content = result.text
    soup = bs(content, 'lxml')
    box = soup.find('article', class_='main-article')
    tit_1 = box.find_all('li')
    for i in tit_1:
        with open('nameofmovie.txt', 'a') as file:
            print(i.text)
            file.write(f'\n{i.text}')