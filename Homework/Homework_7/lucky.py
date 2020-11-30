'''
Homework 7, Exercise 3
Kyle Bush
11/23/2020
Here’s what the program should do:
1. Read the command line arguments as the search term that you’ll use in Google.
2. Fetch the search results page with the requests module, then open the results to
inspect.
3. Find the links to each search result. Then call webbrowser.open() to open the
top three hits in new browser tabs.
'''
import sys, webbrowser, requests

def main():
    

    searchTerms = '+'.join(sys.argv[1:])
    url = 'https://www.google.com/search?q=' + searchTerms
    webbrowser.open(url, new = 2)

    requests.get(url)

if __name__ == '__main__':
    main()