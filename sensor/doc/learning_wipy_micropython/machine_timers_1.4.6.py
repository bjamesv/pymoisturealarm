from machine import Timer, Pin, HeartBeat

#disable heartbeat
#per - https://micropython.org/resources/docs/en/latest/wipy/library/machine.html
HeartBeat().disable()

#turn LED on
# (says v1.6, led works/HB is incorrect?) https://micropython.org/resources/docs/en/latest/wipy/wipy/tutorial/repl.html#linux
led = Pin('GP25', mode=Pin.OUT)
led(1)

#simple function to blink lamp
blink = lambda f:led.toggle()

#Much of 1.4.6 doc is just bad/does not match actual v1.4.6 WiPy firmware
#https://github.com/micropython/micropython/blob/v1.4.6/docs/pyboard/tutorial/timer.rst
#initialize a timer
tim = Timer(4) #1-14 exist; 3 is for internal use; avoid 5+6 (used for servo control or ADC/DAC)
tim.init(mode=Timer.PERIODIC)

#configure a timer 'channel'
tim_a = tim.channel( tim.A, freq=5) #less than 5per sec did not work

#add something useful to the running channel
tim_a.irq(handler=blink) #blinks strangely rapidly

#disable the timer 'channel'
tim_a = None #still blinking
#tim.deinit() #stopped, terminal froze.
tim.channel( tim.A, freq=5) #stopped blinking

#reinitialize, for a slower blink
tim.init(mode=Timer.PERIODIC, width=32)
tim_a = tim.channel( tim.A, freq=4) #does not work

#seems to re-enable the timer channel & useful event?
tim_a = tim.channel( tim.A, freq=5)
tim_a.irq(handler=blink) #starts blinking

tim.channel( tim.A, freq=5)#stops blinking
tim_a = tim.channel( tim.A, freq=8)#does not blink
tim_a.irq(handler=blink) #starts blinking, faster now

tim_a = tim.channel( tim.A, freq=5)#stops blinking
tim_a.irq(handler=blink) #starts blinking, now at the slow blink

#TODO: figure out how events <5Hz work!
#tim_ab = tim.channel( tim.A|tim.B, freq=4) does not seem to work, even with width=32?
