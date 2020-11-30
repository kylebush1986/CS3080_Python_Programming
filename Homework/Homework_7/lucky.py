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
import sys, webbrowser, requests, bs4

def main():
    # Get the search terms from the command line args and append them to the google search url.
    searchTerms = ''.join(sys.argv[1:])
    url = 'https://www.google.com/search?q=' + searchTerms

    # Setup user agent in the request header to mimic a browser request.
    userAgent = "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML,like Gecko) Chrome/20.0.1132.57 Safari/536.11"
    headers = {'User-Agent': userAgent}

    # Get response from request and check that we get an 'OK' response.
    response = requests.get(url, headers = headers)
    response.raise_for_status()

    # Open search results page.
    webbrowser.open(url)

    # Parse search results looking for all divs with class='g'. These divs contain the search results.
    searchResults = bs4.BeautifulSoup(response.text, 'html.parser')
    result_divs = searchResults.select('.g')

    # List that will hold all the links of the search results
    links = []

    # Loop through all the divs, find the links, and add them to the links list
    for result in result_divs:
        link = result.find('a', href = True)
        if link:
            links.append(link['href'])

    # Open up to the first 3 links in from the search in seperate tabs.
    # If the search returns less than 3 links it will open all of them.
    numLinks = min(3, len(links))
    for i in numLinks:
        webbrowser.open(links[i])


if __name__ == '__main__':
    main()