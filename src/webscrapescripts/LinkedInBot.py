import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def getPeopleLinks(page):
        links = []
        for link in page.find_all('a'):
                url = link.get('href')
                if url:
                        if 'profile/view?id=' in url:
                                links.append(url)
        return links

def getJobLinks(page):
        links = []
        for link in page.find_all('a'):
                url = link.get('href')
                if url:
                        if '/jobs' in url:
                                links.append(url)
        return links


def getID(url):
        pUrl = urlparse.urlparse(url)
        return urlparse.parse_qs(pUrl.query)['id'][0]

def ViewBot(browser):
        visited = {}
        p_list = []
        count = 0
        while True:
                # sleep to make sure everything loads.
                # add random to make us look human.
                time.sleep(random.uniform(3.5, 6.9))
                page = BeautifulSoup(browser.page_source)
                people = getPeopleLinks(page)
                if people:
                        for person in people:
                                ID = getID(person)
                                if ID not in visited:
                                    p_list.append(person)
                                    visited[ID] = 1
                                if p_list:  # If there are people to look at, the look at them.
                                    person = p_list.pop()
                                    browser.get(person)
                                    count += 1
                                else:  # otherwise find people via the jobs pages
                                    jobs = getJobLinks(page)
                                    if jobs:
                                        job = random.choice(jobs)
                                        root = 'http://www.linkedin.com'
                                        roots = 'http://www.linkedin.com'
                                        if root not in job or roots not in job:
                                            job = 'https://www.linkedin.com' + job
                                        browser.get(job)
                                    else:
                                        print "I'm lost Exiting"
                                        break
                                        # Output make option for this
                                print "[+] " + browser.title + " Visited! \n (" \
                                      + str(count) + "/" + str(len(p_list)) + ") Visited/Queue"

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="linkedin email")
    parser.add_argument("password", help="linkedin password")
    args = parser.parse_args()

    browser = webdriver.Firefox()
    browser.get("https://linkedin.com/uas/login")

    emailelement = browser.find_element_by_id("session_key-login")
    emailelement.send_keys(args.email)
    passelement = browser.find_element_by_id("session_password-login")
    passelement.send_keys(args.password)
    passelement.submit()

    os.system('clear')
    print "[+] Success! Logged In, Bot Starting!"
    ViewBot(browser)
    browser.close()


if __name__ == "__main__":
        Main()
