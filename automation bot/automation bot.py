import webbrowser as wb #needs instalation
import json, os, base64, random, requests, time


def main():
    print("Welcome to MikaShell ")
    w_for_cmd = ['exit', 'help', 'QWS', 'FTI', 'coinflip', 'suntzu', 'wifi info', 'converter', 'b64', 'make reminder']
    acc_cmd = [do_exit, do_help, quickwebsitesearcher, files_to_img, coinflip, ran_sun_tzu, wifi_status, currencyconverter, base64_converter, reminder_setup]
    index = 0
    while True:
        command = input("# ")
        if command not in w_for_cmd:
            print("Command doesn't exist.")
            continue
        elif command == 'exit':
            break
        for i in w_for_cmd:
            if i == command:
                acc_cmd[index]()
                index= 0
                break
            else:
                index +=1
                continue


#        for word, cmd in enumerate(w_for_cmd):
#            if word == command:
#                acc_cmd[cmd]()
       
            
#Helper commands
def writeToJSONFile(fileName, data):
    file_source = os.getcwd() + "\\" + fileName
    with open(file_source, 'w') as fp:
        json.dump(data, fp)

def checkforfile(file):
    if os.path.isfile(file):
        pass
    else:
        print("file not available")

def converterFtoC(amount):
    calculations = (int(amount) - 32) * 5/9
    return round(calculations, 1)

def converterCtoF(amount):
    calculations = (int(amount)*9/5) + 32
    return round(calculations, 1)


#automation commands
def do_exit():
    #break
    pass
def reminder_setup():
    reminder = {}
    reminder_subject = input("What shall I remind you about?\n")
    reminder_time = float(input("In how many minutes?\n"))
    reminder.setdefault('reminder', []).append(reminder_subject)
    reminder.setdefault('reminder', []).append(reminder_time*60)
    writeToJSONFile("reminders.json", reminder)
    print(f"Done! I'll remind you to {reminder_subject} in {reminder_time} minutes")  
    os.system('cmd /c "Put path for automation bot then running.pyw file"')  
def do_help():
    print("Since commands aren't complete, the help command isn't available.")
def quickwebsitesearcher():
     '''Easy access to different websites'''
     sites = {}
     site = input("What website do you want to go to?\n")
     with open(os.getcwd() + "\\sites.json") as file:
         l = json.load(file)
     try:
         wb.open(l[site])
     except KeyError:
         nosite = input("Site doesn't exist, would you like to add it to your list of websites?(Y/N)\n")
         if nosite == "Y":
             key_name = input("What's the website called?\n")
             link = input("What's the link to " + key_name + "?\n")
             sites[key_name] = link
             writeToJSONFile("sites.json", sites)
             print("Website is saved! taking you to", key_name + "...")
             wb.open(link)
         if nosite == "N":
             print("Alright..but maybe this'll help")
             wb.open("https://www.google.com/")
def files_to_img():
    '''Hiding files into an image'''
    print("Before we start, please save all the files you want in an image to a folder than zipt it up for this to work (will work on automating this part)")
    zip_or_rar = input("You also need a file compressor, do you use .zip or .rar (if you have no file compressor put .zip)?\n")
    image = input("Please give the directory to the image you want to put the file to (without extention)\n")
    checkforfile(image)
    file = input("Please give the directory to your folder/file you want to hide (without extention)\n")
    checkforfile(file)
    if zip_or_rar == ".zip" or ".ZIP" or "zip":
        os.system(f'cmd /c "copy /b {image}.jpg + {file}.zip hidden_file.jpg > NULL"')
        print(f"{file} has been moved to {image}.")
    elif zip_or_rar == ".rar" or ".RAR" or "rar":
        os.system(f'cmd /c "copy /b {image}.jpg + {file}.rar hidden_file.jpg > NULL"')
        print(f"{file} has been moved to {image}.")
def coinflip():
    print("The coin landed on", random.choice(["Heads", "Tails"]))
def currencyconverter():
    '''Converting Currencies'''
    exchange_rate = requests.get("https://v6.exchangerate-api.com/v6/b7bb36fc565afa521322632f/latest/USD").json()
    from_or_to = input("Would you like to convert from or to dollars? (F/T) {sorry it's the only one we have available for now)\n")
    if from_or_to == "F": 
        how_much_f = input("How much would you like to convert from dollars\n")
        curr_f = input("What's the currency you would like to convert with (e.g EUR)\n")
        final_f = float(how_much_f)*float(exchange_rate["conversion_rates"][curr_f])
        print(final_f)
    elif from_or_to == "T":
        how_much_t = input("How much would you like to convert to dollars\n")
        curr_t = input("What's the currency you would like to convert with (e.g EUR)\n")
        final_t = float(how_much_t)/float(exchange_rate["conversion_rates"][curr_t])
        print(final_t)
def ran_sun_tzu():
    '''Random Sun Tzu quotes'''
    quotes = ['The general who wins the battle makes many calculations in his temple before the battle is fought. The general who loses makes but few calculations beforehand.- Sun Tzu', 'A leader leads by example not by force.- Sun Tzu', 'The control of a large force is the same principle as the control of a few men: it is merely a question of dividing up their numbers.- Sun Tzu', "The ultimate in disposing one's troops is to be without ascertainable shape. Then the most penetrating spies cannot pry in nor can the wise lay plans against you.- Sun Tzu", 'If words of command are not clear and distinct, if orders are not thoroughly understood, the general is to blame. But if his orders ARE clear, and the soldiers nevertheless disobey, then it is the fault of their officers.- Sun Tzu', 'Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.- Sun Tzu', 'All warfare is based on deception.- Sun Tzu', 'If fighting is sure to result in victory, then you must fight.- Sun Tzu', 'One defends when his strength is inadaquate, he attacks when it is abundant.- Sun Tzu', 'The quality of decision is like the well-timed swoop of a falcon which enables it to strike and destroy its victim.- Sun Tzu', 'When the enemy is at ease, be able to weary him; when well fed, to starve him; when at rest, to make him move. Appear at places to which he must hasten; move swiftly where he does not expect you.- Sun Tzu', 'If you know your enemy and you know your you need not fear the results of a hundred battles. If you know your but not the enemy for every victory gained you will also suffer a defeat. If you know neither the enemy nor your you will succumb in every battle.- Sun Tzu', 'The general who advances without coveting fame and retreats without fearing disgrace, whose only thought is to protect his country and do good service for his sovereign, is the jewel of the kingdom.- Sun Tzu', 'For to win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill.- Sun Tzu', 'What the ancients called a clever fighter is one who not only wins, but excels in winning with ease.- Sun Tzu', 'To a surrounded enemy, you must leave a way of escape.- Sun Tzu', 'To know your Enemy, you must become your Enemy.- Sun Tzu', "Thus, what is of supreme importance in war is to attack the enemy's strategy.- Sun Tzu", 'A leader leads by example, not force.- Sun Tzu', 'Too frequent rewards indicate that the general is at the end of his resources; too frequent punishments that he is in acute distress.- Sun Tzu', 'Pretend inferiority and encourage his arrogance.- Sun Tzu', 'All men can see these tactics whereby I conquer, but what none can see is the strategy out of which victory is evolved.- Sun Tzu', 'If we do not wish to fight, we can prevent the enemy from engaging us even though the lines of our encampment be merely traced out on the ground. All we need to do is to throw something odd and unaccountable in his way.- Sun Tzu', 'A military operation involves deception. Even though you are competent, appear to be incompetent. Though effective, appear to be ineffective.- Sun Tzu', 'Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.- Sun Tzu', 'The best victory is when the opponent surrenders of its own accord before there are any actual hostilities... It is best to win without fighting.- Sun Tzu', 'Opportunities multiply as they are seized.- Sun Tzu', "Speed is the essence of war. Take advantage of the enemy's unpreparedness; travel by unexpected routes and strike him where he has taken no precautions.- Sun Tzu", 'If your opponent is of choleric temperament, seek to irritate him.- Sun Tzu', 'Management of many is the same as management of few. It is a matter of organization.- Sun Tzu', 'The good fighters of old first put themselves beyond the possibility of defeat, and then waited for an opportunity of defeating the enemy.- Sun Tzu', 'Build your opponent a golden bridge to retreat across.- Sun Tzu', 'Swift as the wind. Quiet as the forest. Conquer like the fire. Steady as the mountain.- Sun Tzu', 'It is essential to seek out enemy agents who have come to conduct espionage against you and to bribe them to serve you. Give them instructions and care for them. Thus doubled agents are recruited and used.- Sun Tzu', 'Now the reason the enlightened prince and the wise general conquer the enemy whenever they move and their achievements surpass those of ordinary men is foreknowledge.- Sun Tzu', 'And therefore those skilled in war bring the enemy to the field of battle and are not brought there by him.- Sun Tzu', 'There is no instance of a nation benefitting from prolonged warfare.- Sun Tzu', 'When able to attack, we must seem unable; when using our forces, we must seem inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near.- Sun Tzu', 'When torrential water tosses boulders, it is because of its momentum. When the strike of a hawk breaks the body of its prey, it is because of timing.- Sun Tzu', 'Secret operations are essential in war; upon them the army relies to make its every move.- Sun Tzu', 'It is said that if you know your enemies and know your, you will not be imperilled in a hundred battles; if you do not know your enemies but do know your, you will win one and lose one; if you do not know your enemies nor your, you will be imperilled in every single battle.- Sun Tzu', 'He who knows when he can fight and when he cannot will be victorious.- Sun Tzu', "Subtle and insubstantial, the expert leaves no trace; divinely mysterious, he is inaudible. Thus he is master of his enemy's fate.- Sun Tzu", 'A skilled commander seeks victory from the situation and does not demand it of his subordinates.- Sun Tzu']
    print(random.choice(quotes))
def wifi_status():
    '''Information about wifi'''
    which_wifi = input("Which wifi are you currently connected to?")
    os.system(f'cmd /c "netsh wlan show profile {which_wifi} key = clear"')
def base64_converter():

    '''Converting base64'''
    e_or_d = input("Would you like to encode or decode a string in base64?(E/D)\n")
    if e_or_d == 'E':
        enc_e = input("Please paste what you would like to encode.\n")
        encodedBytes = base64.b64encode(enc_e.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        print(f"{enc_e} in base64 is {encodedStr}.")
    elif e_or_d == 'D':
        enc_d = input("Please paste the message that you would like to decode.\n")
        decodedBytes = base64.b64decode(enc_d.encode("utf-8"))
        decodedStr = str(decodedBytes, "utf-8")
        print(f"{enc_d} decoded is {decodedStr}.")



if __name__ == '__main__':
    try:
        main()
    except IndexError:
        print('\nThere was an error in indexing finding the appropriate command.')   
    except KeyboardInterrupt:
        print("\nSession ended.")