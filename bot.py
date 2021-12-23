import pyautogui
import time

mensaje = input("Que mensaje quieres spamear:\n ")
numveces = int(input("Quantas veces?:\n "))
delay = int(input("Con quanto delay?\n "))

isLoaded = input("\n\nPulsa [Enter] quando tengas el programa abierto")

print("\nTienes 10 segundos antes de que empieze")
time.sleep(10)
for i in range(0,numveces):
    if mensaje != "":
        pyautogui.typewrite(mensaje)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")
    time.sleep(delay/1000)

print("\n ya esta ;)")
