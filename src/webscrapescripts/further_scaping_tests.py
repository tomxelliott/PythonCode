from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

# (We need to use page.content rather than page.text
# because html.fromstring implicitly expects bytes as input.)

# this will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')


# this will create a list of prices:
prices = tree.xpath('//span[@class="item-price"]/text()')


print 'Buyers: ', buyers
print 'Prices: ', prices
