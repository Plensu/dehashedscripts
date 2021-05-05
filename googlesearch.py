import argparse
from bs4 import BeautifulSoup
import requests

parser = argparse.ArgumentParser(description="Automagical google dork search.")
parser.add_argument('-d', '--domain', help='Search for a domain using the site dork.')
parser.add_argument('-q', '--query', help='Run a custom query')
parser.add_argument('-t', '--tld', help='Change the TLD of google to something like .co or .co.in.', default='.com')
parser.add_argument('-l', '--lang', help='Change the language.', default='en')
parser.add_argument('-r', '--results', help='Change the number of results', default=100)
parser.add_argument('-s', '--start', help='First result to retrieve.', default=0)
parser.add_argument('-st', '--stop', help='Last result to retrieve.', default=None)
parser.add_argument('-p', '--pause', help='Time to wait between requests. Don\'t get banned y\'all', default=3.0)

args = parser.parse_args()
tld = args.tld
lang = args.lang
num = args.results
start = args.start
stop = args.stop
pause = args.pause
domain = args.domain
url = 'https://google.com/search?q='

response = requests.get(url + domain)

print(response)

soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get(href))




# def main():
#     if args.domain:
#         if args.query:
#             print('You can\'t use -d and -q. You gotta pick one fool!')
#             return
#         else:
#             for link in search('site:'+args.domain, tld=tld, num=num, start=start, stop=stop, pause=pause):
#                 print(link)
#     elif args.query and not args.domain:
#         for link in search(args.query, tld=tld, num=num, start=start, stop=stop, pause=pause):
#             print(link)
#     else:
#         print(parser.print_help)

# if __name__ == "__main__":
#     main()
