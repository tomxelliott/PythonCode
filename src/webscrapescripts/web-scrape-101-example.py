from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://www.djangoproject.com"


def get_category_links(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    page = soup.find("dl", “list-features”)
    category_links = [BASE_URL + dd.a["href"] for dd in page.findAll("dd")]
    return category_links



def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


soup_soup = make_soup(url) # where url is the url we're passing into the original function


