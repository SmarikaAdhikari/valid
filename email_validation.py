import re
def validate(email):
    regex = re.compile('^[a-z0-9]+[@]\w+[.]\w{2,3}$')
                            #email regex in regex online python
    return regex.match(email)



email = input("enter the email")
if validate(email):
    print("validation email:")
else:
    print("invalidation occurs")
#pythex.org for regex practise
#gitlab copilot
"""
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email):

    if(re.search(regex,email)):
        print("Valid Email")
    else:
        print("Invalid Email")
if __name__ == '__main__' :

    email = "sma.adh@gmail.com"
    check(email)
    """
