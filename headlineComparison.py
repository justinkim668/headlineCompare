from bs4 import BeautifulSoup
import requests

urlUS = requests.get('http://www.huffingtonpost.com/entry/donald-trump-doesnt-like-twitter_us_587f29f8e4b01cdc64c87fb4')
urlAU = requests.get('http://www.huffingtonpost.com.au/2017/01/18/donald-trump-now-says-he-doesnt-like-tweeting/?utm_hp_ref=au-homepage')

soupUS = BeautifulSoup(urlUS.text, 'lxml')
soupAU = BeautifulSoup(urlAU.text, 'lxml')

headlineUS = soupUS.find_all('div', attrs={'class': 'headline'})
headlineAU = soupAU.find_all('div' , attrs={'class': 'headline'})


for headlineUS in headlineUS:
   list1 = list[headlineUS.get_text()]

for headlineAU in headlineAU:
   list2 = list[headlineAU.get_text()]

str1 = str(list1)
str2 = str(list2)

if str1 == str2:
   print "THE HEADLINES ARE IDENTICAL"
else:
   print "THE HEADLINES ARE NOT IDENTICAL"

articletextUS = soupUS.find_all('div', attrs={'class': 'content-list-component text'})
articletextAU = soupAU.find_all('div' , attrs={'class': 'content-list-component text'})


for textUS in articletextUS:
   list3 = list[textUS.get_text()]

for textAU in articletextAU:
   list4 = list[textAU.get_text()]

str3 = str(list3)
str4 = str(list4)

if str3 == str4:
   print "THE TEXT OF THE ARTICLES ARE IDENTICAL"
else:
   print "THE TEXT OF THE ARTICLES ARE NOT IDENTICAL"
