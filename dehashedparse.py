import argparse
import json

# add arguments
parser = argparse.ArgumentParser(description='Sift through dehashed json and output email, password, or both.')
parser.add_argument('-e', '--email', help='Output just emails.', action='store_true')
parser.add_argument('-p', '--passwd', help='Output just passwords.', action='store_true')
parser.add_argument('-c', '--creds', help='Output both as email:password', action='store_true')
parser.add_argument('-o', '--output', help='Output the output to a file.')
parser.add_argument(help='JSON file to parse.', dest='filename', type=argparse.FileType('r'))

args = parser.parse_args()
if args.email:
    #do email things
    with args.filename as json_file:
        data = json.load(json_file)
        elist = []
        for entry in data['entries']:
            emails = entry['email']
            if args.output:
                with open(args.output, 'a') as output_file:
                    if emails.lower() not in elist:
                        elist.append(emails.lower())
                        output_file.write(emails.lower() + "\n")
                    else:
                        continue
            else:
                if emails.lower() not in elist:
                    elist.append(emails.lower())
                    print(emails.lower())
                else:
                    continue

elif args.passwd:
    #do password things
    with args.filename as json_file:
        data = json.load(json_file)
        plist = []
        for entry in data['entries']:
            passwords = entry['password']
            if passwords == "":
                continue
            else:
                if args.output:
                    with open(args.output, 'a') as output_file:
                        if passwords not in plist:
                            plist.append(passwords)
                            output_file.write(passwords + "\n")
                        else:
                            continue
                else:
                    if passwords not in plist:
                        plist.append(passwords)
                        print(passwords)
                    else:
                        continue
            
elif args.creds:
    #do creds things
    with args.filename as json_file:
        data = json.load(json_file)
        clist = []
        for entry in data['entries']:
            emails = entry['email']
            passwords = entry['password']
            if passwords == "":
                continue
            else:
                creds = emails.lower() + ":" + passwords
                if args.output:
                    with open(args.output, 'a') as output_file:
                        if creds not in clist:
                            clist.append(creds)
                            output_file.write(creds + "\n")
                        else:
                            continue
                else:
                    if creds not in clist:
                        clist.append(creds)
                        print(creds)
                    else:
                        continue
        
else:
    args.print_help()