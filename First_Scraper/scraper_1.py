from requests_html import HTMLSession as hs
from requests_html import AsyncHTMLSession as ahs

from selenium import webdriver




session = hs()
asession = ahs()
url = 'https://shopee.com.my/Women-Pleated-Mini-Skirt-Solid-Ruffle-Lingerie-mylitt-i.150145293.5396182168?sp_atk=8ff54979-3321-40d2-9e6e-60ac031c38e8&xptdk=8ff54979-3321-40d2-9e6e-60ac031c38e8'


def s_1():
    r = session.get(url)
    r.html.render(wait=0.5, scrolldown=True)
    links = (r.html.links)
    title = r.html.find('title')
    print(title[0].text) # list, therefore we need to use indexing

    list_of_links = []

    for link in links:
        list_of_links.append(link)

    # print(len(list_of_links))
    # print(list_of_links[1])

    price = r.html.xpath('//div[@class="flex items-center"]//div[@class="pmmxKx"]', first=True)
    print(price.text)


s_1()