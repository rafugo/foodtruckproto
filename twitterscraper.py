import time
import usaddress
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# a much better parsing addresses function using usaddress
def parseAddressV2(text):
    lastSeenLabel = ''

    parsedList = usaddress.parse(text)

    # time to create a list of the addresses present.
    addressList = []
    tempAddress = ''

    labelTypes = ['AddressNumber', 'StreetNamePreDirectional',
                    'StreetName', 'StreetNamePostType',
                    'ZipCode', 'StateName', 'PlaceName', 
                    'IntersectionSeparator']

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

    if tempAddress != '':
        addressList.append(tempAddress)

    print(parsedList)
    return addressList

# replaces all potential StreetNamePostTypes with 
# recognizable ones for usaddress
def prepareText(text):
    text = re.sub('\WAve\W', ' Ave., ', text, re.I)

    return text

# ideally parses out times
def parseTime(text):
    # match for xx:xxAM/PM - x:xxAM/PM
    timeMatchObj = \
        re.findall(r'(\d{1,2}\s{0,}(:*)\s{0,}\d{0,2}\s{0,}([ap]*)(m*)\s{0,}-\s{0,}\d{1,2}\s{0,}(:*)\s{0,}\d{0,2}\s{0,}([ap]*)(m*))',
                    text, re.I)

    if (timeMatchObj == []):
        return []
    else:
        timeMatches = [i[0] for i in timeMatchObj]
        return timeMatches


browser = webdriver.Chrome()
base_url = u'https://twitter.com/'
# handle = u'KogiBBQ'
# handle = u'grlldcheesetruk'
# handle = u'NoMadTruckLA'
# handle = u'JogasakiBurrito'
handle = u'LobstaTruck'

url = base_url + handle

browser.get(url)
time.sleep(2)

body = browser.find_element_by_tag_name('body')

tweets = browser.find_elements_by_class_name('tweet-text')
dates = [element.get_attribute('title') \
    for element in browser.find_elements_by_xpath( \
        '//a[starts-with(@class,' + \
        ' "tweet-timestamp js-permalink js-nav js-tooltip")]')]


count = 1
for i in range(20): #len(tweets)
    tweet = tweets[i]
    tweetDate = dates[i]
    
    if count > 20:
        count+=1
        continue

    # preparedText = prepareText(tweet.text)
    # print(prepareText(tweet.text))

    # tweetAddresses = parseAddressV2(preparedText)
    tweetAddresses = parseAddressV2(tweet.text)
    print("Tweet " + str(count) + " Text:")
    print(tweet.text)
    print()

    print("Address parsing list: ")
    print(tweetAddresses)
    print()

    print("Time parsing list: ")
    print(parseTime(tweet.text))
    print()

    print("Tweet Date: ")
    print(tweetDate)


    print('\n\n\n\n')

    count+=1


browser.close()
