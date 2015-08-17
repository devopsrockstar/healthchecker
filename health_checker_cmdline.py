#!/usr/bin/python
import requests
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="specify the csv file name")
args = parser.parse_args()

def url_scan( url, string ):
    #from csv file, requests urls and checks whether strings are present.
    r = requests.get(url, timeout=2)
    c = r.text
    hc = string
    if hc in c:
        print ("SUCCESS:\t\"{}\" was found at {}".format(string,url))
    else:
        print ("FAILURE:\t\"{}\" was NOT found at {}".format(string,url))

with open(args.filename) as csvfile:
    #opens csv file and iterates url and strings with url_scan function.
    reader = csv.DictReader(csvfile)
    for row in reader:
        url_scan(row['hostname'],row['string'])