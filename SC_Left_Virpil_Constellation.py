import HOSAS
import scmap
import gremlin

#Trigger groups

L_TriggerFirstStage = 1
L_TriggerSecondStage = 2

@HOSAS.LeftStick.button(HOSAS.FlatTrigger)
def onJoystickBtn_CruiseControl(event, vjoy):
    vjoy[1].button(scmap.CruiseControl).is_pressed = event.is_pressed


#Scroll Wheel

@HOSAS.LeftStick.button(HOSAS.LeftFourWayDown)
def onJoystickBtn_SpeedLimitDown(event, vjoy):
    vjoy[1].button(scmap.FlatTrigger).is_pressed = event.is_pressed

#Scroll Wheel
@HOSAS.LeftStick.button(HOSAS.ScrollUp)
def onJoystickBtn_SpeedLimitUp(event, vjoy):
    vjoy[1].button(scmap.SpeedLimitUp).is_pressed = event.is_pressed

@HOSAS.LeftStick.button(HOSAS.ScrollDown)
def onJoystickBtn_SpeedLimitDown(event, vjoy):
    vjoy[1].button(scmap.SpeedLimitDown).is_pressed = event.is_pressed



#Thumb Stick
ThumbStickPress = 7

#4Way - Right
RightFourWayUp = 8
RightFourWayLeft = 11
RightFourWayRight = 9
RightFourWayDown = 10
RightFourWayPress = 12

#4Way - Left

@HOSAS.LeftStick.button(HOSAS.LeftFourWayUp)
def onJoystickBtn_SpeedLimitUp(event, vjoy):
    vjoy[1].button(scmap.SpeedLimitUp).is_pressed = event.is_pressed

@HOSAS.LeftStick.button(HOSAS.LeftFourWayDown)
def onJoystickBtn_SpeedLimitDown(event, vjoy):
    vjoy[1].button(scmap.SpeedLimitDown).is_pressed = event.is_pressed



LeftFourWayLeft = 16
LeftFourWayRight = 14
LeftFourWayPress = 17

#4Way - Top
TopFourWayUp = 18
TopFourWayLeft = 21
TopFourWayRight = 19
TopFourWayDown = 20
TopFourWayPress = 22

