# LinuxSpeachAPI
How it works:
on start is created input stream with buffer size of 8 or 16 bits and if rms of this samples is greater than
level (voice is on the air), first stream is paused and another InputStream is starting with buffer size of equal to freqency sampling. 
Recording stops if audio rms of last sample is lower than provided level and first InputStream resume listening for voice.
If record is longer than 5s, recognition is provided by Dictation and result is typewrited in actiove input field,
else sarmata is going to recognize the seqence of words and run the action funtion with argument of most probably sequqnce of words.

For now the program is able to:
-

- change volume, mute (by pulsectl)

- typewrite the words into field (dictation)

- run and stop chromium, terminal, amarok,

- wstepnie nawigowac po przegladarce


W planach:
-

- pelne nawigowanie po przegladarce www

- pelne sterowanie multimediami jak z poziomu KDE plasma

- sterowanie podstawowymi funkcjami systemu

Możliwości
-

- pełna emulacja naciśnięć klawiszy

- sterowanie systemem poprzez konsole i pakiety pythona

- 