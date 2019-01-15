import pyautogui
import os


def action(str):
    try:
        if "wycisz" in str:
            pyautogui.hotkey("ctrl", "alt", "s")
            print('silence')
        elif "podgłośnij" in str:
            if "o" in str:
                if "jeden" in str:
                    i = 1
                elif "dwa" in str:
                    i = 2
                elif "trzy" in str:
                    i = 3
                elif "cztery" in str:
                    i = 4
                elif "pięć" in str:
                    i = 5
                elif "sześć" in str:
                    i = 6
                elif "siedem" in str:
                    i = 7
                elif "osiem" in str:
                    i = 8
                elif "dziewięć" in str:
                    i = 9
                elif "dziesięć" in str:
                    i = 10
                for j in xrange(i):
                    pyautogui.hotkey("ctrl", "alt", "+")
                    print('podglasniamy')
            else:
                pyautogui.hotkey("ctrl", "alt", "+")
                print('podglasniamy')
        elif "ścisz" in str:
            if "o" in str:
                if "jeden" in str:
                    i = 1
                elif "dwa" in str:
                    i = 2
                elif "trzy" in str:
                    i = 3
                elif "cztery" in str:
                    i = 4
                elif "pięć" in str:
                    i = 5
                elif "sześć" in str:
                    i = 6
                elif "siedem" in str:
                    i = 7
                elif "osiem" in str:
                    i = 8
                elif "dziewięć" in str:
                    i = 9
                elif "dziesięć" in str:
                    i = 10
                for j in xrange(i):
                    pyautogui.hotkey("ctrl", "alt", "-")
                    print('sciszamy')
            else:
                pyautogui.hotkey("ctrl", "alt", "-")
                print('sciszamy')
        elif "blank" in str:
            pyautogui.hotkey("ctrl", "alt", "b")
            print('wyłączamy ekran')
        elif "wyłącz kopmuter" in str:
            pyautogui.hotkey("ctrl", "alt", "k")
            print ("shutdown")
        elif "uruchom terminal" in str:
            pyautogui.hotkey("ctrl", "alt", "t")
            print ("terminal opened")
        elif "uruchom notatnik" in str:
            pyautogui.hotkey("ctrl", "alt", "t")
            os.system("cd Desktop")
            os.system("vi textfile.txt")
            pyautogui.hotkey("enter")
            pyautogui.hotkey("i")
            print ("Vi notepad opened")
        elif "zamknij notatnik" in str:
            pyautogui.hotkey("enter")
            pyautogui.hotkey(":")
            pyautogui.hotkey("w")
            pyautogui.hotkey("enter")
        elif "zamknij terminal" in str:
            pyautogui.hotkey("ctrl", "alt", "w")
            print ("terminal closed")
        elif "otwórz odtwarzacz muzyki" in str:
            print("Music player opened")
        elif "zamknij odtwarzacz muzyki" in str:
            print("Music player closed")
        elif "wstrzymaj muzykę" in str:
            print("Music stopped")
        elif "wznów muzykę" in str:
            print("Music resumed")

    except:
        print("repeat")
