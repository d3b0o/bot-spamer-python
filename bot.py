import pyautogui
import time

mensaje = input("Que mensaje quieres spamear:\n ")
numveces = int(input("Quantas veces?:\n "))
delay = int(input("Con quanto delay?\n "))

isLoaded = input("\n\nPulsa [Enter] para que epiece la cuenta regresiva de 10 segundos")
time = 0
while True:
    time += 1
    if time == 11:
        for i in range(0,numveces):
            if mensaje != "":
                pyautogui.typewrite(mensaje)
                pyautogui.press("enter")
            else:
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press("enter")
            time.sleep(delay/1000)

        print("\n ya esta ;)")
        break
       else:
        print(time)
