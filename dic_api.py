import json
import urllib.request, urllib.parse, urllib.error
import ssl
import textwrap
import requests


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# format text in a certain width
def text_format(value):
    wrapper = textwrap.TextWrapper(width=90)
    str= wrapper.fill(text=value)
    print(str)

def get_json(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    # urllib open handle
    try:
        uh = urllib.request.urlopen(url, context=ctx)
    except Exception as e:
        return print(e)
    # read html in a format of UTF-8
    data = uh.read() 
    # Parsing UTF-8 in HTML into Objects in JavaScript (decode)
    info = json.loads(data)  
 

    #Print Phonetic:
    try:
        phonetic = info[0]['phonetic']
    except:
        phonetic = "No phonetic avaliable. :("
    print(phonetic)

    syn_ls = []
    ant_ls = []

    meanings = info[0]['meanings']
    for _ in meanings:
        # print definitions 
        print("[{0}]".format(_['partOfSpeech'])) 
            
        # colloect syns and ants 
        for d in _["definitions"]:
            syn_ls.append(d["synonyms"])
            ant_ls.append(d["antonyms"])
            print("{0}. {1}".format(_["definitions"].index(d)+1,d["definition"]))

    # print out syns and ants
    if d["synonyms"]:
        print("\nsynonyms:",*d["synonyms"])
    if d["antonyms"]:
        print("\nantonyms:",*d["antonyms"])

    print("\nRetrieving audio:",get_mp3(info))
    save_word(info)
    return info

def get_mp3(info):  
    if info[0]["phonetics"]:
        str=json.dumps(info[0]["phonetics"][0]["audio"])
        if len(str)>2:
            return str[1:-1] 
        else: return "No phonetic audio avaliable. :("
    else: 
        return "No phonetic audio avaliable. :("


# write json into a file
def save_word(info):
    cmd=input("\nDo you want to save this entry? (Yes: press any key, No: press 'N')\n")
    if cmd != 'N' and cmd != 'n':
        with open("history/{}.json".format(info[0]['word']), "w") as write_file:
            json.dump(info[0], write_file, indent=4)

        mp3 = get_mp3(info)
        try:
            doc = requests.get(mp3)
            with open('audio/{}.mp3'.format(info[0]['word']), 'wb') as f:
                f.write(doc.content)
        except Exception as e:
            print(e)
        print("\nword saved!")    

# read json from a file
def review(word):
     with open("history/{0}.json".format(word), "r") as read_file:
        #Serialize utf8-formatted str to a JSON-formatted str
        json.dumps(json.load(read_file), indent=4)

