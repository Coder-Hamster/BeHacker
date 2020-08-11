import os
import json
import lib.nobody as nobody

def do_command(com):
    cmd = eval(com)
    cmd()

def lang_list():
    lang_list_file = open("F:/coding/Python/porject/project/BeHacker/lib" + "/../assets/texts/list.json","r",encoding="UTF-8")
    lang_map = json.loads(lang_list_file.read())
    times = 0
    while(times < len(lang_map["texts"])):
        print(lang_map["texts"][times])
        times = times + 1
    lang_list_file.close()

def lang_change():
    lang_list_file = open("F:/coding/Python/porject/project/BeHacker/lib" + "/../assets/texts/list.json","r",encoding="UTF-8")
    lang_map = json.loads(lang_list_file.read())
    name_input = input("Name->")
    try:
        lang_name = lang_map[name_input]
        lang_choose_file = open("F:/coding/Python/porject/project/BeHacker/lib" + "/../assets/texts.json","r",encoding="UTF-8")
        lang_choose = {}
        lang_choose = json.loads(lang_choose_file.read())
        lang_choose_file.close()
        lang_choose["lang"] = lang_name
        lang_choose_file = open("F:/coding/Python/porject/project/BeHacker/lib" + "/../assets/texts.json","w",encoding="UTF-8")
        lang_choose_file.write(json.dumps(lang_choose))
        lang_choose_file.close()
        print("Done!Please restart game!")
    except:
        print("Error:Not such lang!")

def ping():
    ip = input("Ip->")
    ip_file = open("F:/coding/Python/porject/project/BeHacker/lib" + "/../assets/map/ip_list.json","r",encoding="UTF-8")
    ip_list = json.loads(ip_file.read())
    target_file_name = ip_list[ip]
    target_file = open("F:/coding/Python/porject/project/BeHacker/lib" + "/../assets/map/targets/" + target_file_name + ".json","r",encoding="UTF-8")
    target_info = json.loads(target_file.read())
    if target_info["can_ping"]:
        for num in range(0,3):
            print("Ping->From " + ip + "Date----163kb")
            nobody.wait(2)
        print("Ping->3/3 Done!")
    else:
        for num in range(0,3):
            print("Ping->From " + ip + "Date----Error")
            nobody.wait(3)
        print("Ping->0/3 Can not connect!")

def clear():
    os.system("CLS")






