import pyautogui
import time

mensaje = input("Que mensaje quieres spamear (si quieres spamear un menaje que tienes copiado simplemente no pongas nada):\n ")
numveces = int(input("Quantas veces?:\n "))
delay = int(input("Con quanto delay?\n "))

isLoaded = input("\n\nPulsa [Enter] para que epiece la cuenta regresiva de 10 segundos")
times = 11
while True:
    times -= 1
    if times == -1:
        for i in range(0,numveces):
            if mensaje != "":
                pyautogui.typewrite(mensaje)
                pyautogui.press("enter")
            else:
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press("enter")
            time.sleep(delay/1000)

        print("\n Empieza la magia ;)")
        break
    else:
        print(times)
        time.sleep(1)