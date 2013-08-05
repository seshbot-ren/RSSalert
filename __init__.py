'''
Created on August 4, 2013
@summary: This script follows the RSS feed of a given CBOX and alerts user if there's a new message. This code originated from
Whats_Calculus' comment in this Reddit thread: http://www.reddit.com/r/raspberry_pi/comments/19pr93/using_my_raspberry_pi_to_monitor_an_rss_feed/
@author: Ren
'''

import win32api
import feedparser
import time
import requests

def main():
    cbox = raw_input("Please type your CBox's RSS Feed URL: ")
    r = requests.head(cbox)
    c = feedparser.parse(cbox)
    message = c.entries[0].description
    answer = True
    while answer:
        if r.status_code == 304: 
            time.sleep(30)
        elif r.status_code == 200:   
            r1 = requests.get(cbox)
            d = feedparser.parse(r1.content)
            newMessage = d.entries[0].description
            if message != newMessage:
                answer = win32api.MessageBox(0, newMessage, 'CBox Alert!', 0x0000100)
                message = newMessage  
        else:
            print "Error: Unexpected response code."
            time.sleep(30)
main()