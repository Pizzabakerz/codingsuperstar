import xml.etree.ElementTree as ET

# read the xml
root = ET.parse('xml_data/sample.xml').getroot()

# find all the child
data = root.findall('bar/type')


for type_tag in root.findall('bar/type'):
    value = type_tag.get('foobar')
    print(value)

print("---------")
# rss
# Python code to illustrate parsing of XML files
# importing the required modules
import xml.etree.ElementTree as ET


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []
    i = 0
    j = 0
    # iterate news items
    for item in root.findall('./channel/item'):
        i += 1
        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:
            j += 1
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

                # append news dictionary to news items list
        newsitems.append(news)

        # return news items list
    print(i)
    print(j)
    return newsitems



# parse xml file from rss
newsitems = parseXML('xml_data/rssfeed.xml')
print(newsitems)

title = []
description=[]
link=[]
guid=[]
pubDate=[]
media=[]


for i in newsitems:
    title.append(i['title'])
    description.append(i['description'])
    link.append(i['link'])
    guid.append(i['guid'])
    pubDate.append('pubData')
    media.append('media')





import pandas as pd

data = pd.DataFrame({
    'title':title,
    'description':description,
    'link':link,
    'guid':guid,
    'pubDate':pubDate,
    'media':media
})

data.to_csv('xmlparse.csv',index=False)
print(data)

print(len(newsitems))
