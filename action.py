import pyautogui

def action(str):
    try:
        if "wycisz" in str:
            pyautogui.hotkey("ctrl", "alt", "s")
            print('silence')
        elif "podgłośnij" in str:
            pyautogui.hotkey("ctrl", "alt", "+")
            print('podglasniamy')
        elif "ścisz" in str:
            pyautogui.hotkey("ctrl", "alt", "-")
            print('sciszamy')
        elif "blank" in str:
            pyautogui.hotkey("ctrl", "alt", "b")
            print('wyłączamy ekran')
    except:
        print("repeat")