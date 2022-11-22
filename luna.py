from dic_api import get_json,save_word,get_mp3,review

while 1:
    word = input("\nPlease input the word you're looking up:(Press 'N' to exit.)\n").strip()
    if word == 'n'or word == 'N':
        break
    # Retrieving json
    
    res_json = get_json(word) 