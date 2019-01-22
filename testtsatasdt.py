import pulsectl
pulse = pulsectl.Pulse('my_client')

pulse.volume_set_all_chans(vol = 100)