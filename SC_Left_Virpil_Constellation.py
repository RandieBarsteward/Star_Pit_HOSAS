import HOSAS
import scmap
import SC_Right_Warthog

#Trigger groups

L_TriggerFirstStage = 1
L_TriggerSecondStage = 2
FlatTrigger = 3

#Scroll Wheel
@HOSAS.LeftStick.button(HOSAS.ScrollUp)
def onJoystickBtn_SpeedLimitUp(event, vjoy):
    vjoy[1].button(scmap.SpeedLimitUp).is_pressed = event.is_pressed

@HOSAS.LeftStick.button(HOSAS.ScrollDown)
def onJoystickBtn_SpeedLimitDown(event, vjoy):
    vjoy[1].button(scmap.SpeedLimitDown).is_pressed = event.is_pressed

@HOSAS.LeftStick.button(HOSAS.ScrollPress)
def onJoystickBtn_MatchTargetSpeed(event, vjoy):
    vjoy[1].button(scmap.MatchTargetSpeed).is_pressed = event.is_pressed

#Thumb Stick
ThumbStickPress = 7

#4Way - Right
RightFourWayUp = 8
RightFourWayLeft = 11
RightFourWayRight = 9
RightFourWayDown = 10
RightFourWayPress = 12

#4Way - Left
LeftFourWayUp = 13
LeftFourWayLeft = 16
LeftFourWayRight = 14
LeftFourWayDown = 15
LeftFourWayPress = 17

#4Way - Top
TopFourWayUp = 18
TopFourWayLeft = 21
TopFourWayRight = 19
TopFourWayDown = 20
TopFourWayPress = 22