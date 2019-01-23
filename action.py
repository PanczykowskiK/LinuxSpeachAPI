import pyautogui
import os
import subprocess
from notify import Notification
import get_active_window
def action(str):
        try:

            Notification("LinuxSpeachAPI", str)
            words = str.split()
            active_window = get_active_window.get_active_window_title().decode('utf-8')
            print(active_window)
            if "audio_play" in words[0]:
                os.popen("xdotool key XF86AudioPlay")
            elif "audio_next" in words[0]:
                os.popen("xdotool key XF86AudioNext")
            elif "audio_prev" in words[0]:
                os.popen("xdotool key XF86AudioPrev")

            elif "start_app" in words[0]:
                if len(words) > 1:
                    if "web" in words[1]:
                        os.popen("chromium")
                    elif "text" in words[1]:
                        os.popen("/opt/visual-studio-code/code")
                    elif "music" in words[1]:
                        os.popen("amarok")
                    elif "files" in words[1]:
                        if len(words)>2:
                            if "docs" in words[2]:
                                os.popen("dolphin ~/OneDrive")
                            elif "music" in words[2]:
                                os.popen("dolphin ~/Music")
                            elif "music" in words[2]:
                                os.popen("dolphin ~/Desktop")
                        else:
                            os.popen("dolphin")

            elif "close_app" in words[0]:
                if len(words) == 1:
                    if not ( "Konsole" in active_window or "LinuxSpeachAPI" in active_window):
                        os.popen("xdotool getactivewindow windowclose")
                else:
                    if "web" in words[1]:
                        os.popen("killall chromium")
                        os.popen("killall chromium")
                        os.popen("killall chromium")
                    elif "text" in words[1]:
                        os.popen("killall /opt/visual-studio-code/code")
                        os.popen("killall /opt/visual-studio-code/code")
                        os.popen("killall /opt/visual-studio-code/code")
                    elif "music" in words[1]:
                        os.popen("killall amarok")
                    elif "files" in words[1]:
                        os.popen("killall dolphin")
            elif "back" in words[0]:
                pyautogui.hotkey('ctrl', 'z')
            elif "nextt" in words[0]:
                pyautogui.hotkey('ctrl', 'shift', 'z')
            elif "mark_all" in words[0]:
                pyautogui.hotkey('ctrl', 'a')
            elif "cut" in words[0]:
                pyautogui.hotkey('ctrl', 'x')
            elif "copy" in words[0]:
                pyautogui.hotkey('ctrl', 'c')
            elif "paste" in words[0]:
                pyautogui.hotkey('ctrl', 'v')
            elif "enter" in words[0]:
                pyautogui.press('enter')
            elif "cancel" in words[0]:
                pyautogui.press('escape')
            elif "delete" in words[0]:
                pyautogui.press('del')
            elif "page_down" in words[0]:
                pyautogui.hotkey('pagedown')
            elif "page_up" in words[0]:
                pyautogui.hotkey('pageup')
            elif "end" in words[0]:
                pyautogui.hotkey('end')
            elif "home" in words[0]:
                pyautogui.hotkey('home')
            elif "volume_up" in words[0]:
                if len(words) > 1:
                    os.popen("pactl set-sink-volume 0 +{}dB".format(words[1]))
            elif "volume_down" in words[0]:
                if len(words) > 1:
                    os.popen("pactl set-sink-volume 0 -{}dB".format(words[1]))
            elif "mute" in words[0]:
                    os.popen("pactl set-sink-mute 0 toggle")
            elif "audio_reset" in words[0]:
                    os.popen("pactl set-sink-volume 0 0dB")
            elif "left" in words[0]:
                pyautogui.hotkey('left')
            elif "right" in words[0]:
                pyautogui.hotkey('right')
            elif "up" in words[0]:
                pyautogui.hotkey('up')
            elif "down" in words[0]:
                pyautogui.hotkey('down')
            elif "print_screen" in words[0]:
                os.popen('spectacle')
            elif "print" in words[0]:
                pyautogui.hotkey('ctrl', 'p')
            elif "change_desktop" in words[0]:
                pyautogui.hotkey('ctrl', 'alt', 'pageup')
            elif "Niezapisane*" in active_window:
                if "save_file" in words[0]:
                    pyautogui.hotkey('ctrl', 's')
            elif "Visual Studio Code" in active_window:
                if "new_file" in words[0]:
                    pyautogui.hotkey('ctrl', 'n')
                elif "save_file" in words[0]:
                    pyautogui.hotkey('ctrl', 's')
                elif "save_as_new_file" in words[0]:
                    pyautogui.hotkey('ctrl', 'shift', 's')
                elif "close_file" in words[0]:
                    pyautogui.hotkey('ctrl', 'w')
                elif "search" in words[0]:
                    pyautogui.hotkey('ctrl', 'f')
                elif "cart_close" in words[0]:
                    pyautogui.hotkey('ctrl', 'w')
            elif "Chromium" in active_window:
                if "cart_new" in words[0]:
                    pyautogui.hotkey('ctrl', 't')
                elif "cart_close" in words[0]:
                    pyautogui.hotkey('ctrl', 'w')
                elif "site_prev" in words[0]:
                    pyautogui.hotkey('alt', 'left')
                elif "site_next" in words[0]:
                    print("action")
                    pyautogui.hotkey('alt', 'right')
                elif "web_search" in words[0]:
                    pyautogui.hotkey('ctrl', 'k')
                elif "cart_restore" in words[0]:
                    pyautogui.hotkey('ctrl', 'shift',  't')
                elif "refresh" in words[0]:
                    pyautogui.hotkey('ctrl', "f5")
                elif "home_website" in words[0]:
                    pyautogui.hotkey('alt', "home")
                elif "cart_go" in words[0]:
                    if len(words) > 1:
                        if 'last_one' in words[1]:
                            pyautogui.hotkey('ctrl', '9')
                        else:
                            pyautogui.hotkey('ctrl', '{}'.format(words[1]))

        except:
            print("repeat")