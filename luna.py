#from dic_api import get_json,save_word,get_mp3,review
from webster_api import webster
import os

ls = []

# update
def update():
    ls.clear()
    entries = os.listdir('/Users/lunayang/Documents/datas/LunaFlashy/history')
    for _ in entries:
        ls.append(_[:-5])
    ls.sort()

# delete
def delete():  
    while 1:
        print("Deletion".center(80,'-'))
        word = input("Please enter the words you want to delete(Press 'N' to exit.):").strip()
        if word != 'n' and word != 'N':
            try:
                os.remove('/Users/lunayang/Documents/datas/LunaFlashy/history/'+word+'.json')
                os.remove('/Users/lunayang/Documents/datas/LunaFlashy/audio/'+word+'.mp3')
                print("Delete succeed!".center(80,'*'))
                update()
                print("Total {0} Items.".format(len(ls)-1))
            except:
                print("Delete failed! Word '{0}' is not found.".format(word).center(80,'*'))
        else:
            main()

# insert
def inquiry():
    while 1:
        print("Inquiry".center(80,'-'))
        word = input("\nPlease input the word you're looking up:(Press 'N' to exit.)\n").strip()
        if word == 'n'or word == 'N':
            main()
        # Retrieving json
        obj = webster(word)
        p_obj = obj.get_json2()    

def main():
    while 1:
        update()
        print('Welcome back!'.center(80,'-'))
        cmd = input("Total {0} items. \nDo you want to show them? (Press 'N' to exit.)".format(len(ls)-1))
        if cmd !="n" and cmd !='N':
            print("Review".center(80,'-'))
            print("\n".join(ls[1:]))
        print("Menu".center(80,'-'))
        cmd = input("\n 1.inquiry\n 2.delete\n 0:exit\n Please input command[0-2]:")
        if cmd == '1': inquiry()
        elif cmd == '2': delete()
        elif cmd == '0': break
        else : print("Try again.".center(80,'*'))

main()