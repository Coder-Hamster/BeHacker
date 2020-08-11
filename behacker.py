import lib.component as component
import lib.nobody as nobody
import lib.command as command
import json
import os

#变量PATH
PATH = os.getcwd()

#用户语言处理
choose_file = open("F:/coding/Python/porject/project/BeHacker" + "/assets/texts.json","r",encoding="UTF-8")
choose = json.loads(choose_file.read())
LANG = choose["lang"]
choose_file.close()
lang_file = open("F:/coding/Python/porject/project/BeHacker" + "/assets/texts/" + LANG + ".json","r",encoding="UTF-8")
lang = json.loads(lang_file.read())
lang_file.close()

#Plugins加载
print(lang["plugin_load"])
nobody.wait(1)
plugin_command = []
for root,dirs,files in os.walk("F:/coding/Python/porject/project/BeHacker" + "/plugins"):
    for dir_name in dirs:
        if dir_name == "":
            nobody.wait(1)
        else:
            print("-----" + dir_name)
            nobody.wait(0.5)
            try:
                plugin_command.append(__import__("F:/coding/Python/porject/project/BeHacker" + "/plugins/" + dir_name + "/command.py"))
            except:
                print(lang["no_command_file"])
                nobody.wait(1)
os.system("CLS")
        
        

#欢迎语
if (nobody.check_times("F:/coding/Python/porject/project/BeHacker" + "/assets/config.json")):
    print("===========================================")
    nobody.wait(0.1)
    print(lang["first_time_welcome"])
    nobody.wait(0.1)
    print("===========================================")
    nobody.wait(0.1)
    print(lang["help"])
    nobody.wait(0.1)
    print("===========================================")
    nobody.wait(0.1)
else:
    print("===========================================")
    nobody.wait(0.1)
    print(lang["welcome"])
    nobody.wait(0.1)
    print("===========================================")
    nobody.wait(0.1)

#指令处理及调度
while(True):
    command_input = input("Command->")
    for com in plugin_command:
        try:
            com.do_command(command_input)
        except:
            pass
    command.do_command(command_input)



