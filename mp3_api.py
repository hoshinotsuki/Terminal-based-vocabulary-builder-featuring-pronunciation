import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_mp3(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    # urllib open handle
    uh = urllib.request.urlopen(url, context=ctx)
    # read html in a format of UTF-8
    data = uh.read() 
    # Parsing UTF-8 in HTML into Objects in JavaScript (decode)
    info = json.loads(data) 
    # Print JS
    str=json.dumps(info[0]["phonetics"][0]["audio"])

    # write json into a file
    with open("history:"+word+".json", "w") as write_file:
        json.dump(info[0], write_file, indent=4)
    return str[1:-1]
 

def review(word):
    # read json from a file
     with open("history:"+word+".json", "r") as read_file:
        json.dumps(json.load(read_file), indent=4)

word = input()
get_mp3(word)
review(word) 



