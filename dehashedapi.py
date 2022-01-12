//Testing a fork :)

import argparse
import requests
import json

dhusername = "EMAIL"
dhapikey = "APIKEY"
headers = {
    'Accept': 'application/json',
}

parser = argparse.ArgumentParser(description="Interact with Dehashed.com's API. Dehashed API help docs https://dehashed.com/docs")
parser.add_argument('-d', '--domain', help='Domain to search for.')
parser.add_argument('-id', help='ID to search for')
parser.add_argument('-e','--email',help='Email to search for.')
parser.add_argument('-ip', '--ipaddr',help='IP address to search for.')
parser.add_argument('-u','--username',help='Username to search for.')
parser.add_argument('-p','--passwd',help='Password to search for.')
parser.add_argument('-hp','--hashedpasswd',help='Hash to search.')
parser.add_argument('-ht','--hashtype',help='The hash type to search for.')
parser.add_argument('-n','--name',help='A name to search for.')
parser.add_argument('-v','--vin',help='A vin number to search for.')
parser.add_argument('-a','--address',help='An address to search for')
parser.add_argument('-ph','--phone',help='A phone number to search for.')
parser.add_argument('-db', '--database', help='The database name to search for.')
parser.add_argument('-s', '--size', help='Max number of results to return. 1 - 30000. Defualt = 100')
parser.add_argument('-pg', '--page', help='Which page to pull from. Dependent on -s argument.')
parser.add_argument('-o', '--output', help='Output the output to a file.')

args = parser.parse_args()
endpoint = "https://api.dehashed.com/search?query="
params = ["domain", "id", "email", "username", "ip_address", "password", "hashed_pasword",
          "hash_type", "name", "vin", "phone", "address", "database_name", "size", "page"]

is_param_added = False
for k, v in args.__dict__.items():
    if v:
        if is_param_added:
            endpoint += "&{0}:{1}".format(k, v)
        else:
            endpoint += "{0}:{1}".format(k, v)
            is_param_added = True

if args.output:
    print("The request sent is: " + endpoint)
    response = requests.get(endpoint, headers=headers, auth=(dhusername, dhapikey))
    print(response.status_code)
    with open(args.output, 'w') as fout:
        json.dump(response.json(), fout, ensure_ascii=False, indent=4)
    print("JSON data saved to %s." % args.output)
else:
    print("The request sent is: " + endpoint)
    response = requests.get(endpoint, headers=headers, auth=(dhusername, dhapikey))
    print(response.status_code)
    print(response.json())

