"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                         Joystick Gremlin Star Citizen
              (Complete Star Citizen 3.7 Joystick Gremlin Plugin)
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import scmap
from container_plugins.tempo import *
from action_plugins.remap import *
from gremlin.user_plugin import *

mode = ModeVariable("Mode", "The mode to use for this mapping")

pvLaunchCountermeasure = PhysicalInputVariable("Launch Countermeasure",
                    "Launch countermeasure button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvCycleCountermeasureAmmo = PhysicalInputVariable("Cycle Countermeasure Ammo",
                    "Cycle countermeasure ammo button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])
                    
pvCycleCountermeasureAmmoBack = PhysicalInputVariable("Cycle Countermeasure Back",
                    "Cycle countermeasure ammo back button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvShieldModifierKey = PhysicalInputVariable("[MODE] Shield Modifer Button",
                    "When pressed/held, Raise Shields Front/Back becomes Top/Bottom",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvShieldRaiseLevelFront = PhysicalInputVariable("Raise Shields: Front (or Top)",
                    "Raise front shields, or top shields if modifer key is pressed",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvShieldRaiseLevelBack = PhysicalInputVariable("Raise Shields: Back (or Bottom)",
                    "Raise back shields, or bottom shields if modifer key is pressed",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvShieldRaiseLevelLeft = PhysicalInputVariable("Raise Shields: Left",
                    "Raise left shields button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvShieldRaiseLevelRight = PhysicalInputVariable("Raise Shields: Right",
                    "Raise right shields button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

#pvShieldRaiseLevelTop = PhysicalInputVariable("Raise Shields: Top",
#                    "Raise top shields button",
#                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

#pvShieldRaiseLevelBottom = PhysicalInputVariable("Raise Shields: Bottom",
#                    "Raise bottom shields button",
#                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvShieldResetLevels = PhysicalInputVariable("Reset Shield Levels",
                    "Reset all shield levels button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

launchCountermeasureDecorator = pvLaunchCountermeasure.create_decorator(mode.value)
@launchCountermeasureDecorator.button(pvLaunchCountermeasure.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.LaunchCountermeasure[1]].button(scmap.LaunchCountermeasure[0]).is_pressed = event.is_pressed

cycleCountermeasureAmmoDecorator = pvCycleCountermeasureAmmo.create_decorator(mode.value)
@cycleCountermeasureAmmoDecorator.button(pvCycleCountermeasureAmmo.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.CycleCountermeasureAmmo[1]].button(scmap.CycleCountermeasureAmmo[0]).is_pressed = event.is_pressed

cycleCountermeasureAmmoBackDecorator = pvCycleCountermeasureAmmoBack.create_decorator(mode.value)
@cycleCountermeasureAmmoBackDecorator.button(pvCycleCountermeasureAmmoBack.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.CycleCountermeasureAmmoBack[1]].button(scmap.CycleCountermeasureAmmoBack[0]).is_pressed = event.is_pressed

shieldModifierKeyDecorator = pvShieldModifierKey.create_decorator(mode.value)
@shieldModifierKeyDecorator.button(pvShieldModifierKey.input_id)
def onBtn(event, vjoy, joy):
    if event.is_pressed:
        vjoy[scmap.ShieldRaiseLevelFront[1]].button(scmap.ShieldRaiseLevelFront[0]).is_pressed = False
        vjoy[scmap.ShieldRaiseLevelBack[1]].button(scmap.ShieldRaiseLevelBack[0]).is_pressed = False
        vjoy[scmap.ShieldRaiseLevelTop[1]].button(scmap.ShieldRaiseLevelTop[0]).is_pressed = joy[pvShieldRaiseLevelFront.device_guid].button(pvShieldRaiseLevelFront.input_id).is_pressed
        vjoy[scmap.ShieldRaiseLevelBottom[1]].button(scmap.ShieldRaiseLevelBottom[0]).is_pressed = joy[pvShieldRaiseLevelBack.device_guid].button(pvShieldRaiseLevelBack.input_id).is_pressed
    else:
        vjoy[scmap.ShieldRaiseLevelFront[1]].button(scmap.ShieldRaiseLevelFront[0]).is_pressed = joy[pvShieldRaiseLevelFront.device_guid].button(pvShieldRaiseLevelFront.input_id).is_pressed
        vjoy[scmap.ShieldRaiseLevelBack[1]].button(scmap.ShieldRaiseLevelBack[0]).is_pressed = joy[pvShieldRaiseLevelBack.device_guid].button(pvShieldRaiseLevelBack.input_id).is_pressed
        vjoy[scmap.ShieldRaiseLevelTop[1]].button(scmap.ShieldRaiseLevelTop[0]).is_pressed = False
        vjoy[scmap.ShieldRaiseLevelBottom[1]].button(scmap.ShieldRaiseLevelBottom[0]).is_pressed = False

shieldRaiseLevelFrontDecorator = pvShieldRaiseLevelFront.create_decorator(mode.value)
@shieldRaiseLevelFrontDecorator.button(pvShieldRaiseLevelFront.input_id)
def onBtn(event, vjoy, joy):
    if joy[pvShieldModifierKey.device_guid].button(pvShieldModifierKey.input_id).is_pressed:
        vjoy[scmap.ShieldRaiseLevelTop[1]].button(scmap.ShieldRaiseLevelTop[0]).is_pressed = event.is_pressed
    else:
        vjoy[scmap.ShieldRaiseLevelFront[1]].button(scmap.ShieldRaiseLevelFront[0]).is_pressed = event.is_pressed

shieldRaiseLevelBackDecorator = pvShieldRaiseLevelBack.create_decorator(mode.value)
@shieldRaiseLevelBackDecorator.button(pvShieldRaiseLevelBack.input_id)
def onBtn(event, vjoy, joy):
    if joy[pvShieldModifierKey.device_guid].button(pvShieldModifierKey.input_id).is_pressed:
        vjoy[scmap.ShieldRaiseLevelBottom[1]].button(scmap.ShieldRaiseLevelBottom[0]).is_pressed = event.is_pressed
    else:
        vjoy[scmap.ShieldRaiseLevelBack[1]].button(scmap.ShieldRaiseLevelBack[0]).is_pressed = event.is_pressed

shieldRaiseLevelLeftDecorator = pvShieldRaiseLevelLeft.create_decorator(mode.value)
@shieldRaiseLevelLeftDecorator.button(pvShieldRaiseLevelLeft.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ShieldRaiseLevelLeft[1]].button(scmap.ShieldRaiseLevelLeft[0]).is_pressed = event.is_pressed

shieldRaiseLevelRightDecorator = pvShieldRaiseLevelRight.create_decorator(mode.value)
@shieldRaiseLevelRightDecorator.button(pvShieldRaiseLevelRight.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ShieldRaiseLevelRight[1]].button(scmap.ShieldRaiseLevelRight[0]).is_pressed = event.is_pressed

#shieldRaiseLevelTopDecorator = pvShieldRaiseLevelTop.create_decorator(mode.value)
#@shieldRaiseLevelTopDecorator.button(pvShieldRaiseLevelTop.input_id)
#def onBtn(event, vjoy):
#    vjoy[scmap.ShieldRaiseLevelTop[1]].button(scmap.ShieldRaiseLevelTop[0]).is_pressed = event.is_pressed

#shieldRaiseLevelBottomDecorator = pvShieldRaiseLevelBottom.create_decorator(mode.value)
#@shieldRaiseLevelBottomDecorator.button(pvShieldRaiseLevelBottom.input_id)
#def onBtn(event, vjoy):
#    vjoy[scmap.ShieldRaiseLevelBottom[1]].button(scmap.ShieldRaiseLevelBottom[0]).is_pressed = event.is_pressed

shieldResetLevelsDecorator = pvShieldResetLevels.create_decorator(mode.value)
@shieldResetLevelsDecorator.button(pvShieldResetLevels.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ShieldResetLevels[1]].button(scmap.ShieldResetLevels[0]).is_pressed = event.is_pressed
