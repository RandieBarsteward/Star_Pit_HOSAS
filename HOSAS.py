import gremlin
#import scmap
#import SC_Left_Virpil_Constellation
#import SC_Right_Warthog
from gremlin.spline import CubicSpline
from gremlin.spline import CubicBezierSpline
from vjoy.vjoy import AxisName
import math



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

default_curve = CubicSpline(
        [(-1.0, -1.0), (0.0, 0.0), (1.0, 1.0)]
)

control_curve = CubicSpline(
    [(-1.0, -1.0), (-0.5, -0.25), ( 0.0,  0.0), ( 0.5,  0.25), ( 1.0,  1.0)
])

reverse_curve = CubicBezierSpline(
     [(-1.0, 1.0), (-0.8, 0.8), (-0.512, 0.004), (0, 0), (0.512, 0.004), (0.8, 0.8), (1.0, -1.0),
])

##############################################################################
#Define vJoy Axis'and assign variable names 

#Define VJoy 1 Axis
StrafeLeftRight = 1                    # X-Axis USED
StrafeUpDown = 2                       # Y-Axis USED
StrafeForwardBack = 3                  # Z-Axis USED
Pitch = 4                              # X-Axis Rot USED
Yaw = 5                                # Y-Axis Rot USED
Roll = 6                               # Z-Axis Rot USED
ThumbStickLeftRight = 7                          # Slider 1
ThumbStickUpDown = 8                          # Slider 2

#Define VJoy 2 Axis (variables to be renamed)
ThrottleAxisRight = 1                    # X-Axis
ThrottleAxisLeft = 2                    # Y-Axis
ThrottleIncrement = 3                  # Z-Axis
TempAxis1 = 4                              # X-Axis Rot
TempAxis2 = 5                                # Y-Axis Rot
Roll2 = 6                               # Z-Axis Rot
ThrottleAbs2 = 7                        # Slider 1
ThrusterPower2 = 8                      # Slider 2

##############################################################################

#Pedals Stick Axis

@Pedals.axis(1)
def pitch(event, vjoy):
    vjoy[2].axis(TempAxis1).value = default_curve(event.value)

@Pedals.axis(2)
def yaw(event, vjoy):
    vjoy[2].axis(TempAxis2).value = default_curve(event.value)

@Pedals.axis(6)
def yaw(event, vjoy):
    vjoy[1].axis(Roll).value = default_curve(event.value)



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
    vjoy[1].axis(StrafeUpDown).value = control_curve(event.value)

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
FlatTrigger = 3

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

###########################
#  Right Stick - Warthog Stick
###########################

#Right Stick Axis
@RightStick.axis(1)
def pitch(event, vjoy):
    vjoy[1].axis(Pitch).value = control_curve(event.value)

@RightStick.axis(2)
def yaw(event, vjoy):
    vjoy[1].axis(Yaw).value = control_curve(event.value)

#Trigger groups
TriggerFirstStage = 1
TriggerSecondStage = 6

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