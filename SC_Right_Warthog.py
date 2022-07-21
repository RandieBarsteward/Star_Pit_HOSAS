import HOSAS
import scmap
import SC_Left_Virpil_Constellation


#Trigger groups
@HOSAS.RightStick.button(HOSAS.TriggerFirstStage)
def onJoystickBtn_FireWeaponGroup1(event, vjoy):
    vjoy[1].button(scmap.FireWeaponGroup1).is_pressed = event.is_pressed

@HOSAS.RightStick.button(HOSAS.TriggerSecondStage)
def onJoystickBtn_FireWeaponGroup2(event, vjoy):
    vjoy[1].button(scmap.FireWeaponGroup2).is_pressed = event.is_pressed

# Red Missile Button
@HOSAS.RightStick.button(HOSAS.RedButton)
def onJoystickBtn_Missiles(event, vjoy):
    vjoy[1].button(scmap.LockFireMissiles).is_pressed = event.is_pressed

    
#Pinky Button - Intend CounterMeasure Macro?
@HOSAS.RightStick.button(HOSAS.PinkyButton)
def onJoystickBtn_SecondCM(event, vjoy):
    vjoy[1].button(scmap.CounterMeasures).is_pressed = event.is_pressed

#Pinky Handle
@HOSAS.RightStick.button(HOSAS.PinkyHandle)
def onJoystickBtn_CounterMeasures(event, vjoy):
    vjoy[1].button(scmap.CounterMeasures).is_pressed = event.is_pressed

#Index Button
@HOSAS.RightStick.button(HOSAS.IndexButton)
def onJoystickBtn_PinSelectedTarget(event, vjoy):
    vjoy[1].button(scmap.PinSelectedTarget).is_pressed = event.is_pressed

#Left 4 Way
@HOSAS.RightStick.button(HOSAS.Left4wayUp)
def onJoystickBtn_PinLock1(event, vjoy):
    vjoy[1].button(scmap.PinLock1).is_pressed = event.is_pressed

@HOSAS.RightStick.button(HOSAS.Left4wayRight)
def onJoystickBtn_PinLock2(event, vjoy):
    vjoy[1].button(scmap.PinLock2).is_pressed = event.is_pressed

@HOSAS.RightStick.button(HOSAS.Left4wayDown)
def onJoystickBtn_PinLock3(event, vjoy):
    vjoy[1].button(scmap.PinLock3).is_pressed = event.is_pressed

@HOSAS.RightStick.button(HOSAS.Left4wayLeft)
def onJoystickBtn_RemoveAllPins(event, vjoy):
    vjoy[1].button(scmap.RemoveAllPins).is_pressed = event.is_pressed

#Right 4 Way
@HOSAS.RightStick.button(HOSAS.Right4wayUp)
def onJoystickBtn_TgtReticle(event, vjoy):
    vjoy[1].button(scmap.TgtReticle).is_pressed = event.is_pressed

@HOSAS.RightStick.button(HOSAS.Right4wayRight)
def onJoystickBtn_TgtCycleHostile(event, vjoy):
    vjoy[1].button(scmap.TgtCycleHostile).is_pressed = event.is_pressed

@HOSAS.RightStick.button(HOSAS.Right4wayDown)
def onJoystickBtn_TgtNearestHostile(event, vjoy):
    vjoy[1].button(scmap.TgtNearestHostile).is_pressed = event.is_pressed

@HOSAS.RightStick.button(HOSAS.Right4wayLeft)
def onJoystickBtn_TgtCycleHostileBck(event, vjoy):
    vjoy[1].button(scmap.TgtCycleHostileBck).is_pressed = event.is_pressed

#Thumb Toggle
ThumbUp = 15
ThumbRight = 16
ThumbDown = 17
ThumbLeft = 18
ThumbPress = 19
