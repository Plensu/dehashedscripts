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
i = 0
if args.domain:
    if i < 1:
        endpoint = endpoint + "domain:" + args.domain
        i += 1
    else:
        endpoint = endpoint + "&domain:" + args.domain
        i += 1

if args.id:
    if i < 1:
        endpoint = endpoint + "id:" + args.id
        i += 1
    else:
        endpoint = endpoint + "&id:" + args.id
        i += 1

if args.email:
    if i < 1:
        endpoint = endpoint + "email:" + args.email
        i += 1
    else:
        endpoint = endpoint + "&email:" + args.email
        i += 1

if args.ipaddr:
    if i < 1:
        endpoint = endpoint + "ip_address:" + args.ipaddr
        i += 1
    else:
        endpoint = endpoint + "&ip_address:" + args.ipaddr
        i += 1

if args.username:
    if i < 1:
        endpoint = endpoint + "username:" + args.username
        i += 1
    else:
        endpoint = endpoint + "&username:" + args.username
        i += 1

if args.passwd:
    if i < 1:
        endpoint = endpoint + "password:" + args.passwd
        i += 1
    else:
        endpoint = endpoint + "&password:" + args.passwd
        i += 1

if args.hashedpasswd:
    if i < 1:
        endpoint = endpoint + "hashed_password:" + args.hashedpasswd
        i += 1
    else:
        endpoint = endpoint + "&hashed_password:" + args.hashedpasswd
        i += 1

if args.hashtype:
    if i < 1:
        endpoint = endpoint + "hash_type:" + args.hashtype
        i += 1
    else:
        endpoint = endpoint + "&hash_type:" + args.hashtype
        i += 1

if args.name:
    if i < 1:
        endpoint = endpoint + "name:" + args.name
        i += 1
    else:
        endpoint = endpoint + "&name:" + args.name
        i += 1

if args.vin:
    if i < 1:
        endpoint = endpoint + "vin:" + args.vin
        i += 1
    else:
        endpoint = endpoint + "&vin:" + args.vin
        i += 1

if args.address:
    if i < 1:
        endpoint = endpoint + "address:" + args.address
        i += 1
    else:
        endpoint = endpoint + "&address:" + args.address
        i += 1

if args.phone:
    if i < 1:
        endpoint = endpoint + "phone:" + args.phone
        i += 1
    else:
        endpoint = endpoint + "&phone:" + args.phone
        i += 1

if args.database:
    if i < 1:
        endpoint = endpoint + "database_name:" + args.database
        i += 1
    else:
        endpoint = endpoint + "&database_name:" + args.database
        i += 1

if args.size:
    if i < 1:
        endpoint = endpoint + "size:" + args.size
        i += 1
    else:
        endpoint = endpoint + "&size:" + args.size
        i += 1

if args.page:
    if i < 1:
        endpoint = endpoint + "page:" + args.page
        i += 1
    else:
        endpoint = endpoint + "&page:" + args.page
        i += 1
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
