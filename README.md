# Tele-Webscraper [Work in Progress]

The aim is to automate the manual check of students' attendance at night done by Residential Assistants in Raffles Insitution Boarding (RIB).

Every night students are supposed to scan their fingerprint around 10pm - 10.30pm. Once they have scanned, it will be recorded in the RIB website.

## What am I solving?

1. The current RIB website is REALLY slow.
2. Human error:
    - Students may forget to scan their fingerprint
    - Residential Assistant on duty that night may forget to check the attendance

## How it works

1. The scraper will scrape the attendance from the RIB website and store it in a temporary database at regular time (~5 minutes). Then we can call these data using telegram bot without much lag.


2. Shifting the whole responsibility to the community. The attendance checking duty will be shifted to a public telegram channel where every students and teachers can see live updates of who has and has not scanned their fingerprint in the channel every night. 