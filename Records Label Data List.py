from bs4 import BeautifulSoup
import requests, os
good_links = list()
for i in range(2,50):

    page_number = i
    url = 'https://labelsbase.net/?g=Techno&page={}'.format(page_number)
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    all_labels_list = soup.find_all('a',{"class":"label-card-logo-link"})
    
    for tmp in all_labels_list:
        link_to_sinlge_label = tmp.get('href')
        print(link_to_sinlge_label)
        ##get email
        res = requests.get(link_to_sinlge_label)
        soup = BeautifulSoup(res.content, "html.parser")
        
        for obj in soup.find_all('a'):
            found_link = obj.get('href')
            print(found_link)
            if '@' in found_link:
                try:
                    found_link = found_link.split(':')[1]
                except:
                    continue
                if '?' not in found_link:
                    good_links.append(found_link)
        
print(good_links)

import pandas as pd
df = pd.DataFrame(good_links)
df = df.drop_duplicates()
df.to_csv (r'C:\Users\omerr\OneDrive\שולחן העבודה\New folder (2)\Labelist.csv', index = 0)

print('done!')