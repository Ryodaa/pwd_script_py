import requests
from hashlib import sha1
import sys

password = sys.argv[1].encode('utf-8')
prefix_pw = sha1(password).hexdigest()[:5]
suffix_pw = sha1(password).hexdigest()[5:]

url = 'https://api.pwnedpasswords.com/range/' + prefix_pw
res = requests.get(url)

content_str = str(res.content)

content_list = content_str.split('\\n')

pwnage_hits = 0

for sha1_hash in content_list:
    if suffix_pw.upper() in sha1_hash:
        pwnage_hits += 1
        print('You\'ve been pwned! Change your password!')
        break

if pwnage_hits == 0:
    print('Your password is safe')
