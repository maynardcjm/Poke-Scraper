import requests
import argparse


def banner():
    print("""


              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \n
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         \"\"\"\"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\n
   -" /`.         _,'     | _  _  _.|
    ""--'---"\"\"\"\"'        `' '! |! /
                            `" " -' mh


    """)

banner()

# Initialize parser
parser = argparse.ArgumentParser()

# Command-line Argument
parser.add_argument("-u", "--username", help = "Username to authenticate to web page with")

parser.add_argument("-p", "--password", help = "Password to authenticate to web page with")


# Read arguments from command line
args = parser.parse_args()

# Assign Cmdline args to variables
username = args.username
password = args.password

# Displays Arguments Back to User
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

# Note you may need to make multiple requests with different query parameters for limit to see more results
# Play around with searching and looking at the different variables in the url query. 
# Example: search.php?limit=100&n=charizard
# Happy Hacking :)

print(query_req.status_code)
# print(query_req.content) # Since this returns json data it's easiest to user the json function
# print(query_req.json())

# Example Using JSON Object
#print(query_req.json()[0]['name'])
#print(query_req.json()[0]['text'])


# Get the data for the first card object returned by the request
# Note: datastructure is a list of dictionaries

first_card = query_req.json()[0]
# Print All Details for First Card
for k in first_card:
    print(k,':',first_card[k])
