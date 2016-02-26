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
tim.deinit()
#tim.init(mode=Timer.PERIODIC, width=32)#terminal froze.
tim = Timer(4,mode=Timer.PERIODIC, width=32)
tim_ab = tim.channel( Timer.A | Timer.B, freq=4) #does not work
tim_ab.irq(handler=blink) #does not start blinking

seconds = 2 * 1000 * 1000
tim_ab = tim.channel( Timer.A | Timer.B, period=seconds)
tim_ab.irq(handler=blink) #does not start blinking

tim.deinit()
tim = Timer(1, mode=Timer.PERIODIC, width=32)
tim_ab = tim.channel( Timer.A | Timer.B, period=seconds) #works! perhaps issue is with Timer 4?
tim_ab.irq(handler=blink)

seconds = 13 * 1000 * 1000
tim_ab = tim.channel( Timer.A | Timer.B, period=seconds) #rate slowed to every 13 seconds

