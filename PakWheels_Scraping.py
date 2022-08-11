from bs4 import BeautifulSoup
import requests
from csv import writer


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url = "https://www.pakwheels.com/used-cars/660cc-cars/190519"
page = requests.get(url, headers=headers)
##print(r.status_code)
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div',class_='well search-list clearfix ad-container page-')

with open('pak_wheels.csv','w',encoding='utf8',newline='') as f:
 thewriter = writer(f)
 header = ['Car_Model','Price','Location','Car_Info']
 thewriter.writerow(header)      
     

 for list in lists:

          carModel = list.find('a',class_='car-name ad-detail-path').text.replace('\n'," ")
          carPrice = list.find('div',class_='price-details generic-dark-grey').text.replace('\n'," ")
          carLocation = list.find('ul',class_='list-unstyled search-vehicle-info fs13').text.replace('\n'," ")
          carInfo = list.find('ul',class_='list-unstyled search-vehicle-info-2 fs13').text.replace('\n'," ")
          ##carImage = list.find('img',class_='pic')['src']
          Details = [carModel,carPrice,carLocation,carInfo]
          thewriter.writerow(Details)

