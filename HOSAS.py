import imp
from pydoc import importfile
import gremlin
from gremlin.spline import CubicSpline
from gremlin.spline import CubicBezierSpline
from vjoy.vjoy import AxisName
import math
import scmap



##############################################################################
#Define vJoy Axis'and assign variable names 

#Define VJoy 1 Axis
StrafeLeftRight = 1                    # X-Axis USED
StrafeUpDown = 2                       # Y-Axis USED
StrafeForwardBack = 3                  # Z-Axis USED
Pitch = 4                              # X-Axis Rot USED
Yaw = 5                                # Y-Axis Rot USED
Roll = 6                               # Z-Axis Rot USED
ThumbStickLeftRight = 7                # Slider 1
ThumbStickUpDown = 8                   # Slider 2

#Define VJoy 2 Axis (variables to be renamed)
ThrottleAxisRight = 1                  # X-Axis
ThrottleAxisLeft = 2                   # Y-Axis
ThrottleIncrement = 3                  # Z-Axis
TempAxis1 = 4                          # X-Axis Rot
TempAxis2 = 5                          # Y-Axis Rot
Roll2 = 6                              # Z-Axis Rot
ThrottleAbs2 = 7                       # Slider 1
ThrusterPower2 = 8                     # Slider 2

##############################################################################

###########################
#  PHYSICAL DEVICE MAPPINGS #
###########################

# The following variables are initialized to the physical axes and buttons on
# the HOTAS. The included scripts' logic utilize these values to know what
# inputs to "listen" for to do particular actions and maneuvers.

##############################################################################


LeftStick = gremlin.input_devices.JoystickDecorator(
    "LEFT VPC Stick WarBRD",
    "{338B04D0-F7DB-11EC-8002-444553540000}",
    "Default"
)

RightStick = gremlin.input_devices.JoystickDecorator(
    "RIGHT VPC Stick WarBRD",
    "{338B04D0-F7DB-11EC-8003-444553540000}",
    "Default"
)

Pedals = gremlin.input_devices.JoystickDecorator(
    "Saitek Pro Flight Combat Rudder Pedals",
    "{D88335C0-F7BD-11EC-8001-444553540000}",
    "Default"
)

Throttle = gremlin.input_devices.JoystickDecorator(
    "Throttle - HOTAS Warthog",
    "{F5ACEB40-F7BE-11EC-8001-444553540000}",
    "Default"
)

LeftMFD = gremlin.input_devices.JoystickDecorator (
    "MFD - Left",
    "{683754D0-0925-11ED-8001-444553540000}",
    "Default"
)

RightMFD = gremlin.input_devices.JoystickDecorator (
    "MFD - Right",
    "{683754D0-0925-11ED-8002-444553540000}",
    "Default"
)

default_curve = CubicSpline(
        [(-1.0, -1.0), (0.0, 0.0), (1.0, 1.0)]
)

control_curve = CubicSpline(
    [(-1.0, -1.0), (-0.5, -0.25), ( 0.0,  0.0), ( 0.5,  0.25), ( 1.0,  1.0)
])

reverse_curve = CubicBezierSpline(
     [(-1.0, 1.0), (-0.8, 0.8), (-0.512, 0.004), (0, 0), (0.512, 0.004), (0.8, 0.8), (1.0, -1.0),
])

precision_curve = CubicSpline(
        [(-1.0, -0.5), (0.0, 0.0), (1.0, 0.5)]
)

#Pedals Stick Axis
''''
@Pedals.axis(1)
def pitch(event, vjoy):
    vjoy[2].axis(TempAxis1).value = default_curve(event.value)

@Pedals.axis(2)
def yaw(event, vjoy):
    vjoy[2].axis(TempAxis2).value = default_curve(event.value)

@Pedals.axis(6)
def yaw(event, vjoy):
    vjoy[1].axis(Roll).value = control_curve(event.value)
'''


##############################################################################
#Link physical buttons to appropriate Variable name for use in other scripts

###########################
#  Left Stick - Virpil Constellation Delta #
###########################

#Left Stick Axis
#Axis 1 = Left/right

@LeftStick.axis(1)
def pitch(event, vjoy):
    vjoy[1].axis(StrafeLeftRight).value = control_curve(event.value)

#Axis 2 = forward/back
@LeftStick.axis(2)
def yaw(event, vjoy):
    vjoy[1].axis(StrafeForwardBack).value = reverse_curve(event.value)

#Axis 3 = Strafe Up/Down (twist)
@LeftStick.axis(3)
def verticalStrafe(event, vjoy):
    vjoy[1].axis(StrafeUpDown).value = reverse_curve(event.value)

#Axis 4 = Thumb Joy Left Right
@LeftStick.axis(4)
def walkLeftRight(event, vjoy):
    vjoy[1].axis(ThumbStickLeftRight).value = control_curve(event.value)

#Axis 5 = Thumb Joy Up Down
@LeftStick.axis(5)
def walkForwardBack(event, vjoy):
    vjoy[1].axis(ThumbStickUpDown).value = control_curve(event.value)
                      
ThumbStickUpDown = 8 

#Trigger groups
L_TriggerFirstStage = 1
L_TriggerSecondStage = 2
FlatTrigger = 3 #used

#Scroll Wheel
ScrollUp = 5
ScrollDown = 4
ScrollPress = 6

#Thumb Stick
ThumbStickPress = 7

#4Way - Right
RightFourWayUp = 8
RightFourWayLeft = 11
RightFourWayRight = 9
RightFourWayDown = 10
RightFourWayPress = 12

#4Way - Left
LeftFourWayUp = 13 #used
LeftFourWayLeft = 16
LeftFourWayRight = 14
LeftFourWayDown = 15 #used
LeftFourWayPress = 17

#4Way - Top
TopFourWayUp = 18
TopFourWayLeft = 21
TopFourWayRight = 19
TopFourWayDown = 20
TopFourWayPress = 22



@LeftStick.button(FlatTrigger)
def onJoystickBtn_CruiseControl(event, vjoy):
    vjoy[1].button(scmap.CruiseControl).is_pressed = event.is_pressed

#4Way - Left
@LeftStick.button(LeftFourWayUp)
def onJoystickBtn_SpeedLimitUp(event, vjoy):
    vjoy[1].button(scmap.SpeedLimitUp).is_pressed = event.is_pressed

@LeftStick.button(LeftFourWayDown)
def onJoystickBtn_SpeedLimitDown(event, vjoy):
    vjoy[1].button(scmap.SpeedLimitDown).is_pressed = event.is_pressed


###########################
#  Right Stick - Warthog Stick
###########################
#Trigger groups
TriggerFirstStage = 1
TriggerSecondStage = 6


#Right Stick Axis
@RightStick.axis(1)
def pitch(event, vjoy):
    vjoy[1].axis(Pitch).value = default_curve(event.value)

@RightStick.axis(2)
def yaw(event, vjoy):
    vjoy[1].axis(Yaw).value = default_curve(event.value)

# Red Missile Button
RedButton = 2

#Pinky Button
PinkyButton = 3

#Pinky Handle
PinkyHandle = 4

#Index Button
IndexButton = 5

#Right Joystick HAT
@RightStick.hat(1)
def onJoystickHat(event, vjoy, joy):
    vjoy[1].hat(1).direction = (event.value)

#Left 4 Way
Left4wayUp = 7
Left4wayRight = 8
Left4wayDown = 9
Left4wayLeft = 10

#Right 4 Way
Right4wayUp = 11
Right4wayRight = 12
Right4wayDown = 13
Right4wayLeft = 14

#Thumb Toggle
ThumbUp = 15
ThumbRight = 16
ThumbDown = 17
ThumbLeft = 18
ThumbPress = 19

#Trigger groups
@RightStick.button(TriggerFirstStage)
def onJoystickBtn_FireWeaponGroup1(event, vjoy):
    vjoy[1].button(scmap.FireWeaponGroup1).is_pressed = event.is_pressed

@RightStick.button(TriggerSecondStage)
def onJoystickBtn_FireWeaponGroup2(event, vjoy):
    vjoy[1].button(scmap.FireWeaponGroup2).is_pressed = event.is_pressed


# Red Missile Button
@RightStick.button(RedButton)
def onJoystickBtn_Missiles(event, vjoy):
    vjoy[1].button(scmap.LockFireMissiles).is_pressed = event.is_pressed

    
#Pinky Button - Intend CounterMeasure Macro?
@RightStick.button(PinkyButton)
def onJoystickBtn_HeadTrackCentre(event, vjoy):
    vjoy[1].button(scmap.HeadTrackCentre).is_pressed = event.is_pressed

#Pinky Handle
@RightStick.button(PinkyHandle)
def onJoystickBtn_CounterMeasures(event, vjoy):
    vjoy[1].button(scmap.CounterMeasures).is_pressed = event.is_pressed

#Index Button
@RightStick.button(IndexButton)
def onJoystickBtn_PinSelectedTarget(event, vjoy):
    vjoy[1].button(scmap.PinSelectedTarget).is_pressed = event.is_pressed

#Left 4 Way
@RightStick.button(Left4wayUp)
def onJoystickBtn_PinLock1(event, vjoy):
    vjoy[1].button(scmap.PinLock1).is_pressed = event.is_pressed

@RightStick.button(Left4wayRight)
def onJoystickBtn_PinLock2(event, vjoy):
    vjoy[1].button(scmap.PinLock2).is_pressed = event.is_pressed

@RightStick.button(Left4wayDown)
def onJoystickBtn_PinLock3(event, vjoy):
    vjoy[1].button(scmap.PinLock3).is_pressed = event.is_pressed

@RightStick.button(Left4wayLeft)
def onJoystickBtn_RemoveAllPins(event, vjoy):
    vjoy[1].button(scmap.RemoveAllPins).is_pressed = event.is_pressed

#Right 4 Way
@RightStick.button(Right4wayUp)
def onJoystickBtn_TgtReticle(event, vjoy):
    vjoy[1].button(scmap.TgtReticle).is_pressed = event.is_pressed

@RightStick.button(Right4wayRight)
def onJoystickBtn_TgtCycleHostile(event, vjoy):
    vjoy[1].button(scmap.TgtCycleHostile).is_pressed = event.is_pressed

@RightStick.button(Right4wayDown)
def onJoystickBtn_TgtNearestHostile(event, vjoy):
    vjoy[1].button(scmap.TgtNearestHostile).is_pressed = event.is_pressed

@RightStick.button(Right4wayLeft)
def onJoystickBtn_TgtCycleHostileBck(event, vjoy):
    vjoy[1].button(scmap.TgtCycleHostileBck).is_pressed = event.is_pressed


###########################
#  Warthog Throttle
############################

# Throttle Main Axis

@Throttle.axis(3)
def ThrottleRight(event, vjoy):
    vjoy[2].axis(ThrottleAxisRight).value = default_curve(event.value)

@Throttle.axis(6)
def ThrottleLeft(event, vjoy):
    vjoy[2].axis(ThrottleAxisLeft).value = default_curve(event.value)

@Throttle.axis(7)
def ThrottleIncrementLever(event, vjoy):
    vjoy[2].axis(ThrottleIncrement).value = default_curve(event.value)

# Throttle Handle Buttons

############################
# Throttle Grip
############################

#Main grip face
NippleButton = 1

ThrottleRedButton = 15

#Throttle Hat
@Throttle.hat(1)
def onJoystickHat(event, vjoy, joy):
    vjoy[1].hat(2).direction = (event.value)

#Throttle Pinky Switch
PinkySwitchForward = 13
PinkySwitchBack = 14

#Main grip right side
#Throttle right side hat
SideHatForward = 4
SideHatBack = 6
SideHatLeft = 3
SideHatRight = 5
SideHatPress = 2

#Side 2 way
Side2WayForward = 7
Side2WayBack = 8

#Side 3 way
Side3WayForward = 9
Side3WayBack = 10

#Red 2 Way Temp
RedTempForward = 11
RedTempBack = 12

############################
# Throttle Main Panel
############################

EngineLeft = 16
EngineRight = 17

ToggleLeft = 18
ToggleLeftTemp = 31

ToggleRight = 19
ToggleRightTemp = 32

FuelScoop = 20

EmergencyStop = 21

############################
# Throttle Lower Panel
############################

RedAlertToggle = 24

OverrideToggle = 25

EngageButton = 26

ControlToggleCruise = 27
ControlToggleFlight = 28


############################
# MFD - Clockwise - Both MFDs have the same construction and button layout
############################

MFD_1 = 1
MFD_2 = 2
MFD_3 = 3
MFD_4 = 4
MFD_5 = 5

MFD_6 = 6
MFD_7 = 7
MFD_8 = 8
MFD_9 = 9
MFD_10 = 10

MFD_11 = 11
MFD_12 = 12
MFD_13 = 13
MFD_14 = 14
MFD_15 = 15

MFD_16 = 16
MFD_17 = 17
MFD_18 = 18
MFD_19 = 19
MFD_20 = 20

#Top right
SYM_Up = 21
SYM_Down = 22

#Bottom right
CON_Up = 23
CON_Down = 24

#Bottom left
BRT_Up = 25
BRT_Down = 26

#Top left
GAIN_Up = 27
GAIN_Down = 28

'''
############################
# MFD Left - Clockwise
############################

Left_MFD_1 = 1
Left_MFD_2 = 2
Left_MFD_3 = 3
Left_MFD_4 = 4
Left_MFD_5 = 5

Left_MFD_6 = 6
Left_MFD_7 = 7
Left_MFD_8 = 8
Left_MFD_9 = 9
Left_MFD_10 = 10

Left_MFD_11 = 11
Left_MFD_12 = 12
Left_MFD_13 = 13
Left_MFD_14 = 14
Left_MFD_15 = 15

Left_MFD_16 = 16
Left_MFD_17 = 17
Left_MFD_18 = 18
Left_MFD_19 = 19
Left_MFD_20 = 20

#Top right
Left_SYM_Up = 21
Left_SYM_Down = 22

#Bottom right
Left_CON_Up = 23
Left_CON_Down = 24

#Bottom left
Left_BRT_Up = 25
Left_BRT_Down = 26

#Top left
Left_GAIN_Up = 27
Left_GAIN_Down = 28
'''
#Left MFD
LeftMFD.button(MFD_1)
def onJoystickBtn_ESPToggle(event, vjoy):
    vjoy[1].button(scmap.ESPToggle).is_pressed = event.is_pressed

LeftMFD.button(MFD_2)
def onJoystickBtn_Decouple(event, vjoy):
    vjoy[1].button(scmap.Decouple).is_pressed = event.is_pressed

LeftMFD.button(MFD_3)
def onJoystickBtn_gsafe(event, vjoy):
    vjoy[1].button(scmap.gsafe).is_pressed = event.is_pressed

LeftMFD.button(MFD_11)
def onJoystickBtn_ActiveScan(event, vjoy):
    vjoy[1].button(scmap.ActiveScan).is_pressed = event.is_pressed

LeftMFD.button(MFD_12)
def onJoystickBtn_RadarPing(event, vjoy):
    vjoy[1].button(scmap.RadarPing).is_pressed = event.is_pressed

LeftMFD.button(MFD_13)
def onJoystickBtn_AnglePlus(event, vjoy):
    vjoy[1].button(scmap.AnglePlus).is_pressed = event.is_pressed

LeftMFD.button(MFD_14)
def onJoystickBtn_AngleMinus(event, vjoy):
    vjoy[1].button(scmap.AngleMinus).is_pressed = event.is_pressed

LeftMFD.button(MFD_15)
def onJoystickBtn_ScanMode(event, vjoy):
    vjoy[1].button(scmap.ScanMode).is_pressed = event.is_pressed



############################
# MFD Right
############################
'''
Right_MFD_1 = 1
Right_MFD_2 = 2
Right_MFD_3 = 3
Right_MFD_4 = 4
Right_MFD_5 = 5

Right_MFD_6 = 6
Right_MFD_7 = 7
Right_MFD_8 = 8
Right_MFD_9 = 9
Right_MFD_10 = 10

Right_MFD_11 = 11
Right_MFD_12 = 12
Right_MFD_13 = 13
Right_MFD_14 = 14
Right_MFD_15 = 15

Right_MFD_16 = 16
Right_MFD_17 = 17
Right_MFD_18 = 18
Right_MFD_19 = 19
Right_MFD_20 = 20

#Top right
Left_SYM_Up = 21
Left_SYM_Down = 22

#Bottom right
Left_CON_Up = 23
Left_CON_Down = 24

#Bottom left
Left_BRT_Up = 25
Left_BRT_Down = 26

#Top left
Left_GAIN_Up = 27
Left_GAIN_Down = 28
'''
#Right MFD
RightMFD.button(MFD_1)
def onJoystickBtn_Vtol(event, vjoy):
    vjoy[1].button(scmap.Vtol).is_pressed = event.is_pressed

RightMFD.button(MFD_2)
def onJoystickBtn_DockMode(event, vjoy):
    vjoy[1].button(scmap.DockMode).is_pressed = event.is_pressed

RightMFD.button(MFD_3)
def onJoystickBtn_AutoDock(event, vjoy):
    vjoy[1].button(scmap.AutoDock).is_pressed = event.is_pressed

RightMFD.button(MFD_4)
def onJoystickBtn_AutoLand(event, vjoy):
    vjoy[1].button(scmap.AutoLand).is_pressed = event.is_pressed

RightMFD.button(MFD_5)
def onJoystickBtn_LandingGear(event, vjoy):
    vjoy[1].button(scmap.LandingGear).is_pressed = event.is_pressed

RightMFD.button(MFD_11)
def onJoystickBtn_InternalLocks(event, vjoy):
    vjoy[1].button(scmap.InternalLocks).is_pressed = event.is_pressed

RightMFD.button(MFD_12)
def onJoystickBtn_CloseDoors(event, vjoy):
    vjoy[1].button(scmap.CloseDoors).is_pressed = event.is_pressed

RightMFD.button(MFD_13)
def onJoystickBtn_OpenDoors(event, vjoy):
    vjoy[1].button(scmap.OpenDoors).is_pressed = event.is_pressed

RightMFD.button(MFD_14)
def onJoystickBtn_UnlockDoors(event, vjoy):
    vjoy[1].button(scmap.UnlockDoors).is_pressed = event.is_pressed

RightMFD.button(MFD_15)
def onJoystickBtn_LockDoors(event, vjoy):
    vjoy[1].button(scmap.LockDoors).is_pressed = event.is_pressed

