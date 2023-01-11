import HOSAS
import scmap


#Left MFD
@HOSAS.LeftMFD.button(HOSAS.MFD_1)
def onJoystickBtn_ESPToggle(event, vjoy):
    vjoy[1].button(scmap.ESPToggle).is_pressed = event.is_pressed

@HOSAS.LeftMFD.button(HOSAS.MFD_2)
def onJoystickBtn_Decouple(event, vjoy):
    vjoy[1].button(scmap.Decouple).is_pressed = event.is_pressed

@HOSAS.LeftMFD.button(HOSAS.MFD_3)
def onJoystickBtn_gsafe(event, vjoy):
    vjoy[1].button(scmap.gsafe).is_pressed = event.is_pressed

@HOSAS.LeftMFD.button(HOSAS.MFD_11)
def onJoystickBtn_ActiveScan(event, vjoy):
    vjoy[1].button(scmap.ActiveScan).is_pressed = event.is_pressed

@HOSAS.LeftMFD.button(HOSAS.MFD_12)
def onJoystickBtn_RadarPing(event, vjoy):
    vjoy[1].button(scmap.RadarPing).is_pressed = event.is_pressed

@HOSAS.LeftMFD.button(HOSAS.MFD_13)
def onJoystickBtn_AnglePlus(event, vjoy):
    vjoy[1].button(scmap.AnglePlus).is_pressed = event.is_pressed

@HOSAS.LeftMFD.button(HOSAS.MFD_14)
def onJoystickBtn_AngleMinus(event, vjoy):
    vjoy[1].button(scmap.AngleMinus).is_pressed = event.is_pressed

@HOSAS.LeftMFD.button(HOSAS.MFD_15)
def onJoystickBtn_ScanMode(event, vjoy):
    vjoy[1].button(scmap.ScanMode).is_pressed = event.is_pressed


#Right MFD
@HOSAS.RightMFD.button(HOSAS.MFD_1)
def onJoystickBtn_Vtol(event, vjoy):
    vjoy[1].button(scmap.Vtol).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_2)
def onJoystickBtn_DockMode(event, vjoy):
    vjoy[1].button(scmap.DockMode).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_3)
def onJoystickBtn_AutoDock(event, vjoy):
    vjoy[1].button(scmap.AutoDock).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_4)
def onJoystickBtn_AutoLand(event, vjoy):
    vjoy[1].button(scmap.AutoLand).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_5)
def onJoystickBtn_LandingGear(event, vjoy):
    vjoy[1].button(scmap.LandingGear).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_11)
def onJoystickBtn_InternalLocks(event, vjoy):
    vjoy[1].button(scmap.InternalLocks).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_12)
def onJoystickBtn_CloseDoors(event, vjoy):
    vjoy[1].button(scmap.CloseDoors).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_13)
def onJoystickBtn_OpenDoors(event, vjoy):
    vjoy[1].button(scmap.OpenDoors).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_14)
def onJoystickBtn_UnlockDoors(event, vjoy):
    vjoy[1].button(scmap.UnlockDoors).is_pressed = event.is_pressed

@HOSAS.RightMFD.button(HOSAS.MFD_15)
def onJoystickBtn_LockDoors(event, vjoy):
    vjoy[1].button(scmap.LockDoors).is_pressed = event.is_pressed
 