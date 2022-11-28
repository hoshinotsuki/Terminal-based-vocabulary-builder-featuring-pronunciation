import json
import urllib.request, urllib.parse, urllib.error
import ssl
import textwrap
import requests
import hidden
import re
import os


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class webster:
    def __init__(self,word) -> None: 
        self.word = word.split() 

    def get_json2(self):
        word = self.word
        url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"+word+"?key="+hidden.key
        #print(url)

        # urllib open handle
        try:
            uh = urllib.request.urlopen(url, context=ctx)
        except Exception as e:
            return print(e)
        # read html in a format of UTF-8
        data = uh.read() 
        # Parsing UTF-8 in HTML into Objects in JavaScript (decode)
        p_obj = json.loads(data)
        
        # Smart spell
        try:
            meta = p_obj[0]['meta']
        except:
            print("Do you mean...\n"+" / ".join(p_obj),end="?\n")
            return

        # Pronouciation 
        phonetic = p_obj[0]['hwi']['prs'][0]['mw']  
        sound = p_obj[0]['hwi']['prs'][0]['sound']['audio'] 
        if re.findall('\d',word):
            self.mp3= "https://media.merriam-webster.com/audio/prons/en/us/mp3/number/"+sound+".mp3"
        else:
            self.mp3= "https://media.merriam-webster.com/audio/prons/en/us/mp3/"+word[0]+"/"+sound+".mp3"
        print("["+phonetic+"]",self.mp3)

        # Syns (RegEx)
        try:
            syns_str = p_obj[0]['syns'][0]['pt'][0][1]
            syns = set(re.findall(r'\{sc\}(.*?)\{',syns_str))
            print("[synonyms]\n"+" / ".join(syns))
        except:
            pass

        # Definitions 
        for meta in p_obj: 
            if meta['shortdef']:
                try:
                    print('['+meta['fl']+']') 
                except:
                    print('[verb]')
                defi = meta['shortdef']
                try:
                    for _ in range(len(defi)):
                        print(str(_+1)+'.',defi[_])
                except Exception as e:
                    print(e)

        self.save_word(p_obj)
        return p_obj

    # write json into a file
    def save_word(self, info):
        cmd=input("\nDo you want to save this entry? (Yes: press any key, No: press 'N')\n")
        if cmd != 'N' and cmd != 'n':
            with open("/Users/lunayang/Documents/datas/LunaFlashy/history/{}.json".format(self.word), "w") as write_file:
                json.dump(info[0], write_file, indent=4)
            doc = requests.get(self.mp3)
            with open('/Users/lunayang/Documents/datas/LunaFlashy/audio/{}.mp3'.format(self.word), 'wb') as f:
                f.write(doc.content)
            print("word saved!".center(80,'*'))  

    # synchronize
    def auto(self,info):
        with open("/Users/lunayang/Documents/datas/LunaFlashy/history/{}.json".format(self.word), "w") as write_file:
            json.dump(info[0], write_file, indent=4)
        doc = requests.get(self.mp3)
        with open('/Users/lunayang/Documents/datas/LunaFlashy/audio/{}.mp3'.format(self.word), 'wb') as f:
            f.write(doc.content)
        print("\nword saved!")  
    