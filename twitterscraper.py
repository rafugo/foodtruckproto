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

# takes out all the times
def removeTimes(text):
    times = parseTime(text)

    for time in times:
        # this is the only substitution i could find that would not get picked
        # up as a street name lmao
        text = re.sub(time, 'this must be ignored trust me', text)

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

# function that attempts to pair addresses with their corresponding times
# returns None if there's not an equal amount of addresses and times
def pairAddressTimes(text, addresses, times):
    # if there's the same amount of addresses and times, then we are most likely
    # correct in just pairing them up
    if (len(addresses) == len(times)):
        return list(zip(addresses, times))

    # given that our time parser is more trustworthy, if there's one time and 
    # multiple places, we can assume that time is for all the places
    elif len(times) == 1: 

        # NOTE: this is risky and may be taken out if too risky
        return [(address, times[0]) for address in addresses]

    # otherwise this cannot be trusted
    else:
        return None


browser = webdriver.Chrome()
base_url = u'https://twitter.com/'
handle = u'KogiBBQ'
# handle = u'grlldcheesetruk'
# handle = u'NoMadTruckLA'
# handle = u'JogasakiBurrito'
# handle = u'LobstaTruck'

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

    # parse the tweet
    tweetText = tweet.text
    times = parseTime(tweetText)
    tweetText = removeTimes(tweetText)
    tweetAddresses = parseAddressV2(tweetText)

    print("Tweet " + str(count) + " Text:")
    print(tweetText)
    print()

    print("Address parsing list: ")
    print(tweetAddresses)
    print()

    print("Time parsing list: ")
    print(times)
    print()

    print("Tweet Date: ")
    print(tweetDate)
    print()

    print("Food Truck Locations: ")
    print(pairAddressTimes(tweet.text, tweetAddresses, times))

    print('\n\n\n\n')

    count+=1


browser.close()
