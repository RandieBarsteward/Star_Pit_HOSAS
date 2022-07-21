import gremlin
from gremlin.spline import CubicSpline
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

#Define VJoy 1 Axis
StrafeLeftRight = 1                    # X-Axis USED
StrafeUpDown = 2                       # Y-Axis USED
StrafeForwardBack = 3                  # Z-Axis USED
Pitch = 4                              # X-Axis Rot USED
Yaw = 5                                # Y-Axis Rot USED
Roll = 6                               # Z-Axis Rot USED
TempAxis1 = 7                        # Slider 1
TempAxis2 = 8                      # Slider 2

#Define VJoy 2 Axis (variables to be renamed)
StrafeLeftRight2 = 1                    # X-Axis
StrafeUpDown2 = 2                       # Y-Axis
StrafeForwardBack2 = 3                  # Z-Axis
Pitch2 = 4                              # X-Axis Rot
Yaw2 = 5                                # Y-Axis Rot
Roll2 = 6                               # Z-Axis Rot
ThrottleAbs2 = 7                        # Slider 1
ThrusterPower2 = 8                      # Slider 2


#Left Stick Axis
#Axis 1 = Left/right
@LeftStick.axis(1)
def pitch(event, vjoy):
    vjoy[1].axis(StrafeLeftRight).value = control_curve(event.value)

#Axis 2 = forward/back
@LeftStick.axis(2)
def yaw(event, vjoy):
    vjoy[1].axis(StrafeForwardBack).value = control_curve(event.value)

#Axis 3 = Strafe Up/Down (twist)
@LeftStick.axis(3)
def yaw(event, vjoy):
    vjoy[1].axis(StrafeUpDown).value = control_curve(event.value)

#Right Stick Axis
@RightStick.axis(1)
def pitch(event, vjoy):
    vjoy[1].axis(Pitch).value = control_curve(event.value)

@RightStick.axis(2)
def yaw(event, vjoy):
    vjoy[1].axis(Yaw).value = control_curve(event.value)

#Pedals Stick Axis

@Pedals.axis(1)
def pitch(event, vjoy):
    vjoy[1].axis(TempAxis1).value = default_curve(event.value)

@Pedals.axis(2)
def yaw(event, vjoy):
    vjoy[1].axis(TempAxis2).value = default_curve(event.value)

@Pedals.axis(6)
def yaw(event, vjoy):
    vjoy[1].axis(Roll).value = default_curve(event.value)
##############################################################################