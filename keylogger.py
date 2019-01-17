import os
import pyxhook
"""first version from  https://www.geeksforgeeks.org/design-a-keylogger-in-python/ but not used anymore since we have audio_detector"""

cancel_key = ord(
	os.environ.get(
		'pylogger_cancel',
		'`'
	)[0]
)


def OnKeyPress(event):
		print(event.Key)


new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
new_hook.HookKeyboard()
try:
	new_hook.start()
except KeyboardInterrupt:
	pass
except Exception as ex:
	pyxhook.print_err(ex)
