import pyautogui
import os
import subprocess
def action(str):
        try:
            words = str.split()
            print(str)
            if "wycisz" in words[0]:
                os.popen("xdotool key XF86AudioMute")
                print('silence')
            elif "podgłośnij" in words[0]:
                os.popen("pactl set-sink-volume 0 +{}db".format(int(words[1])))
            elif "ścisz" in words[0]:
                os.popen("pactl set-sink-volume 0 -{}db".format(int(words[1])))
            elif "volume_reset" in words[0]:
                os.popen("pactl set-sink-volume 0 0db")
            elif "page_up" in words[0]:
                pyautogui.press('pageup')
            elif "page_down" in words[0]:
                pyautogui.press('pagedown')
            elif "start" in words[0]:
                if "web" in words[1]:
                    subprocess.Popen('chromium', stdout=subprocess.PIPE)
                elif "terminal" in words[1]:
                    subprocess.Popen('konsole', stdout=subprocess.PIPE)
                elif "music" in words[1]:
                    subprocess.Popen('konsole', stdout=subprocess.PIPE)
                elif "files" in words[1]:
                    if "home" in words[2]:
                        subprocess.Popen('dolphin ~', stdout=subprocess.PIPE)
                    else:
                        subprocess.Popen('dolphin {}.format()', stdout=subprocess.PIPE)
                elif "efx" in words[1]:
                    subprocess.Popen('pulseeffects', stdout=subprocess.PIPE)
            elif "stop" in words[0]:
                if "web" in words[1]:
                    os.popen("killall chromium")
                elif "terminal" in words[1]:
                    os.popen('killall konsole', stdout=subprocess.PIPE)
            elif "ctrl+a" in words[0]:
                pyautogui.hotkey('ctrl', 'a')
            elif "back" in words[0]:
                pyautogui.hotkey('ctrl', 'z')
            elif "print" in words[0]:
                pyautogui.hotkey('ctrl', 'p')

        except:
            print("repeat")