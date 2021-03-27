import os, json, pyautogui, time, playsound
#for things that always have to be running
#from automation bot import reminder_setup

def reminder():
    with open(os.getcwd() + "\\reminders.json") as file:
         data = json.load(file)
    time.sleep(data["reminder"][1])
    playsound.playsound("C:\\Users\\mikas\\Downloads\\bababooey-sound-effect.mp3")
    pyautogui.alert(text=data["reminder"][0], title='REMINDER', button='OK')
    

reminder()