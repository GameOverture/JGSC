"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                         Joystick Gremlin Star Citizen
              (Complete Star Citizen 3.7 Joystick Gremlin Plugin)
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import scmap
from gremlin.user_plugin import *

mode = ModeVariable("Mode", "The mode to use for this mapping")


pvEject = PhysicalInputVariable("Eject",
                                  "Eject Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvExitSeat = PhysicalInputVariable("Exit Seat",
                                  "Exit Seat Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvSelfDestruct = PhysicalInputVariable("Self Destruct",
                                  "Self Destruct Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvIncreaseCoolerRate = PhysicalInputVariable("Increase Cooler Rate",
                                  "Increase Cooler Rate Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvDecreaseCoolerRate = PhysicalInputVariable("Decrease Cooler Rate",
                                  "Decrease Cooler Rate Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvFlightSystemsReady = PhysicalInputVariable("Flight Systems Ready",
                                  "Flight Systems Ready Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvOpenAllDoors = PhysicalInputVariable("Open All Doors",
                                  "Open All Doors Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvCloseAllDoors = PhysicalInputVariable("Close All Doors",
                                  "Close All Doors Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvLockAllDoors = PhysicalInputVariable("Lock All Doors",
                                  "Lock All Doors Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvUnlockAllDoors = PhysicalInputVariable("Unlock All Doors",
                                  "Unlock All Doors Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvLookBehind = PhysicalInputVariable("Look Behind",
                                  "Look Behind Button",
                                  [gremlin.common.InputType.JoystickButton])

pvMap = PhysicalInputVariable("Map",
                                  "MobiGlass Map Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvHeadlightsToggle = PhysicalInputVariable("Headlights Toggle",
                                  "Headlights Toggle Button",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])
                                  
pvCockpitModifierKey = PhysicalInputVariable("Cockpit Modifer Key/Switch",
                                  "When pressed/held, it does the alternate action of a few buttons",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvLandingSystemToggle = PhysicalInputVariable("Landing Gear (or Spool Quantum)",
                                  "Toggles landing gear, or spools the quantum drive if modifer key is pressed",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvAutoland = PhysicalInputVariable("Autoland (or Start Quantum)",
                                  "Autoland, or starts quantum drive if modifer key is pressed",
                                  [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvGForceSafetyToggle = PhysicalInputVariable("GForce Safety Toggle",
                                  "GForce Safety Toggle button",
                                  [gremlin.common.InputType.JoystickButton])

pvESPToggle = PhysicalInputVariable("ESP Toggle",
                                  "Toggles Enhanced Stick Percision",
                                  [gremlin.common.InputType.JoystickButton])

pvToggleVTOL = PhysicalInputVariable("VTOL Toggle",
                                  "Toggle Vertical Take Off and Landing mode",
                                  [gremlin.common.InputType.JoystickButton])

pvHailTarget = PhysicalInputVariable("Hail Target",
                                  "Hail Hydra Target",
                                  [gremlin.common.InputType.JoystickButton])

ejectDecorator = pvEject.create_decorator(mode.value)
@ejectDecorator.button(pvEject.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.Eject[1]].button(scmap.Eject[0]).is_pressed = event.is_pressed

exitSeatDecorator = pvExitSeat.create_decorator(mode.value)
@exitSeatDecorator.button(pvExitSeat.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ExitSeat[1]].button(scmap.ExitSeat[0]).is_pressed = event.is_pressed

selfDestructDecorator = pvSelfDestruct.create_decorator(mode.value)
@selfDestructDecorator.button(pvSelfDestruct.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.SelfDestruct[1]].button(scmap.SelfDestruct[0]).is_pressed = event.is_pressed

increaseCoolerRateDecorator = pvIncreaseCoolerRate.create_decorator(mode.value)
@increaseCoolerRateDecorator.button(pvIncreaseCoolerRate.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.IncreaseCoolerRate[1]].button(scmap.IncreaseCoolerRate[0]).is_pressed = event.is_pressed

decreaseCoolerRateDecorator = pvDecreaseCoolerRate.create_decorator(mode.value)
@decreaseCoolerRateDecorator.button(pvDecreaseCoolerRate.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.DecreaseCoolerRate[1]].button(scmap.DecreaseCoolerRate[0]).is_pressed = event.is_pressed

flightSystemsReadyDecorator = pvFlightSystemsReady.create_decorator(mode.value)
@flightSystemsReadyDecorator.button(pvFlightSystemsReady.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.FlightSystemsReady[1]].button(scmap.FlightSystemsReady[0]).is_pressed = event.is_pressed

openAllDoorsDecorator = pvOpenAllDoors.create_decorator(mode.value)
@openAllDoorsDecorator.button(pvOpenAllDoors.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.OpenAllDoors[1]].button(scmap.OpenAllDoors[0]).is_pressed = event.is_pressed

closeAllDoorsDecorator = pvCloseAllDoors.create_decorator(mode.value)
@closeAllDoorsDecorator.button(pvCloseAllDoors.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.CloseAllDoors[1]].button(scmap.CloseAllDoors[0]).is_pressed = event.is_pressed

lockAllDoorsDecorator = pvLockAllDoors.create_decorator(mode.value)
@lockAllDoorsDecorator.button(pvLockAllDoors.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.LockAllDoors[1]].button(scmap.LockAllDoors[0]).is_pressed = event.is_pressed

unlockAllDoorsDecorator = pvUnlockAllDoors.create_decorator(mode.value)
@unlockAllDoorsDecorator.button(pvUnlockAllDoors.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.UnlockAllDoors[1]].button(scmap.UnlockAllDoors[0]).is_pressed = event.is_pressed

lookBehindDecorator = pvLookBehind.create_decorator(mode.value)
@lookBehindDecorator.button(pvLookBehind.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.LookBehind[1]].button(scmap.LookBehind[0]).is_pressed = event.is_pressed

mapDecorator = pvMap.create_decorator(mode.value)
@mapDecorator.button(pvMap.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.Map[1]].button(scmap.Map[0]).is_pressed = event.is_pressed

headlightsToggleDecorator = pvHeadlightsToggle.create_decorator(mode.value)
@headlightsToggleDecorator.button(pvHeadlightsToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.HeadlightsToggle[1]].button(scmap.HeadlightsToggle[0]).is_pressed = event.is_pressed

cockpitModifierKeyDecorator = pvCockpitModifierKey.create_decorator(mode.value)
@cockpitModifierKeyDecorator.button(pvCockpitModifierKey.input_id)
def onBtn(event, vjoy):
    if event.is_pressed:
        vjoy[scmap.LandingSystemToggle[1]].button(scmap.LandingSystemToggle[0]).is_pressed = False
        vjoy[scmap.Autoland[1]].button(scmap.Autoland[0]).is_pressed = event.is_pressed = False

landingSystemToggleDecorator = pvLandingSystemToggle.create_decorator(mode.value)
@landingSystemToggleDecorator.button(pvLandingSystemToggle.input_id)
def onBtn(event, vjoy, joy):
    if pvCockpitModifierKey.value is not None:
        if joy[pvCockpitModifierKey.device_guid].button(pvCockpitModifierKey.input_id).is_pressed:
            vjoy[scmap.QuantumTravelSystemToggle[1]].button(scmap.QuantumTravelSystemToggle[0]).is_pressed = event.is_pressed
        else:
            vjoy[scmap.LandingSystemToggle[1]].button(scmap.LandingSystemToggle[0]).is_pressed = event.is_pressed
    else:
        vjoy[scmap.LandingSystemToggle[1]].button(scmap.LandingSystemToggle[0]).is_pressed = event.is_pressed

autolandDecorator = pvAutoland.create_decorator(mode.value)
@autolandDecorator.button(pvAutoland.input_id)
def onBtn(event, vjoy, joy):
    if pvCockpitModifierKey.value is not None:
        if joy[pvCockpitModifierKey.device_guid].button(pvCockpitModifierKey.input_id).is_pressed:
            vjoy[scmap.QuantumDrive[1]].button(scmap.QuantumDrive[0]).is_pressed = event.is_pressed
        else:
            vjoy[scmap.Autoland[1]].button(scmap.Autoland[0]).is_pressed = event.is_pressed
    else:
        vjoy[scmap.Autoland[1]].button(scmap.Autoland[0]).is_pressed = event.is_pressed

gForceSafetyToggleDecorator = pvGForceSafetyToggle.create_decorator(mode.value)
@gForceSafetyToggleDecorator.button(pvGForceSafetyToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.GForceSafetyToggle[1]].button(scmap.GForceSafetyToggle[0]).is_pressed = event.is_pressed

espToggleDecorator = pvESPToggle.create_decorator(mode.value)
@espToggleDecorator.button(pvESPToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ESPToggle[1]].button(scmap.ESPToggle[0]).is_pressed = event.is_pressed

toggleVTOLDecorator = pvToggleVTOL.create_decorator(mode.value)
@toggleVTOLDecorator.button(pvToggleVTOL.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ToggleVTOL[1]].button(scmap.ToggleVTOL[0]).is_pressed = event.is_pressed

hailTargetDecorator = pvHailTarget.create_decorator(mode.value)
@hailTargetDecorator.button(pvHailTarget.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.HailTarget[1]].button(scmap.HailTarget[0]).is_pressed = event.is_pressed
