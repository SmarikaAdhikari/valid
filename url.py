import re
def is_url_valid(url):
    reg_url=re.compile('^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')
    return reg_url.match(url)
url=input("enter the url:")
if is_url_valid(url):
    print("url is valid")
else:
    print("url is invalid")
