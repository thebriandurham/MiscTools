# imports
import sys
import requests

urls_file = sys.argv[1]
urls_list = [line.rstrip('\n') for line in open(urls_file)]

for url in urls_list:
    r = requests.options(url)
    if r.status_code == 200:
        try:
            print('Allowed methods for %s: %s' % (url,r.headers['allow']))
        except KeyError as e:
            print('OPTIONS method allowed for %s, but response header had unexpected keys.\n:Response headers:%s\nResponse Text:%s' % (url,r.headers,r.text))
    else:
        print('OPTIONS method not allowed for %s' % (url))

