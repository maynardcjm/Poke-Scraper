import requests
import argparse

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-u", "--username", help = "Username to authenticate to web page with")

parser.add_argument("-p", "--password", help = "Password to authenticate to web page with")


# Read arguments from command line
args = parser.parse_args()

# Displays Arguments Back to User
username = args.username
password = args.password

print('Username:', username)
print('Password:', password)

url = "https://pokemoncard.io"

# Authentication Payload
auth = {'username':username, 'password':password, 'rememberme':'false'}

# Send Authentication Request
logon_req = requests.post(url+'/api/users/authenticate.php', data=auth)

# Print Server  Response
print('\nRequest Repsone:',logon_req.status_code)
print(logon_req.content)


# Grab Session Cookies for Subsequent Requests
cookies={'Cookie':logon_req.headers['Set-Cookie']}


# API Query Request for Card Data 
query_req = requests.get(url+'/api/search.php?limit=100&sort=name', headers=cookies)

print(query_req.status_code)
print(query_req.content)
