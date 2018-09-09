import time
import pyap
import usaddress
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# simple function for parsing addresses using pyap
def parseAddress(text):
    addresses = pyap.parse(text, country='US')
    return addresses

# a much better parsing addresses function using usaddress
def parseAddressV2(text):
    lastSeenLabel = ''

    parsedList = usaddress.parse(text)

    # time to create a list of the addresses present.
    addressList = []
    tempAddress = ''

    labelTypes = ['AddressNumber', 'StreetNamePreDirectional',
                    'StreetName', 'StreetNamePostType',
                    'ZipCode', 'PlaceName']

    for pair in parsedList:
        if pair[1] in labelTypes:
            tempAddress += (re.sub('[!@#(),\n$]', '', pair[0]) + " ")
            
        elif (lastSeenLabel == 'StreetNamePostType' 
                and pair[1] == 'OccupancyIdentifier'):
            tempAddress += (re.sub('[!@#(),\n$]', '', pair[0]) + " ")

        elif tempAddress != '':
            addressList.append(tempAddress.strip())
            tempAddress = ''

        lastSeenLabel = pair[1]

    return addressList




browser = webdriver.Chrome()
base_url = u'https://twitter.com/'
handle = u'NoMadTruckLA'
url = base_url + handle

browser.get(url)
time.sleep(2)

body = browser.find_element_by_tag_name('body')

tweets = browser.find_elements_by_class_name('tweet-text')


count = 1
for tweet in tweets:
    
    if count > 10:
        count+=1
        continue
    
    tweetAddresses = parseAddressV2(tweet.text)
    print("Tweet " + str(count) + " Text:")
    print(tweet.text)
    print()

    print("Address parsing list: ")
    print(tweetAddresses)
    print('\n\n\n\n')

    count+=1


browser.close()
