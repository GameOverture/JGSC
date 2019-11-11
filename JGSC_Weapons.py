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

pvFireWeaponGroup1 = PhysicalInputVariable("Fire Weapon Group 1",
                    "Fire weapon group 1 button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvFireWeaponGroup2 = PhysicalInputVariable("Fire Weapon Group 2",
                    "Fire weapon group 2 button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])
                    
pvCycleWeaponAmmo = PhysicalInputVariable("Cycle Weapon Ammo",
                    "Cycle weapon ammo button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvCycleWeaponAmmoBack = PhysicalInputVariable("Cycle Weapon Ammo Back",
                    "Cycle weapon ammo back button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvCycleGimbleModes = PhysicalInputVariable("Cycle Gimble Modes",
                    "Cycle gimble modes between auto, gimble, and fixed",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvAcquireMissileLock = PhysicalInputVariable("Acquire Missile Lock",
                    "Acquire missile lock button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvLaunchMissile = PhysicalInputVariable("Launch Missile",
                    "Launch missile button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvReticleModeToggle = PhysicalInputVariable("Toggle Reticle Mode",
                    "Button to toggle the reticle mode",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvLookAhead = PhysicalInputVariable("Look Ahead",
                    "",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvTargetFocus = PhysicalInputVariable("Target Focus",
                    "",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

fireWeaponGroup1Decorator = pvFireWeaponGroup1.create_decorator(mode.value)
@fireWeaponGroup1Decorator.button(pvFireWeaponGroup1.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.FireWeaponGroup1[1]].button(scmap.FireWeaponGroup1[0]).is_pressed = event.is_pressed

fireWeaponGroup2Decorator = pvFireWeaponGroup2.create_decorator(mode.value)
@fireWeaponGroup2Decorator.button(pvFireWeaponGroup2.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.FireWeaponGroup2[1]].button(scmap.FireWeaponGroup2[0]).is_pressed = event.is_pressed

cycleWeaponAmmoDecorator = pvCycleWeaponAmmo.create_decorator(mode.value)
@cycleWeaponAmmoDecorator.button(pvCycleWeaponAmmo.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.CycleWeaponAmmo[1]].button(scmap.CycleWeaponAmmo[0]).is_pressed = event.is_pressed

cycleWeaponAmmoBackDecorator = pvCycleWeaponAmmoBack.create_decorator(mode.value)
@cycleWeaponAmmoBackDecorator.button(pvCycleWeaponAmmoBack.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.CycleWeaponAmmoBack[1]].button(scmap.CycleWeaponAmmoBack[0]).is_pressed = event.is_pressed

cycleGimbleModesDecorator = pvCycleGimbleModes.create_decorator(mode.value)
@cycleGimbleModesDecorator.button(pvCycleGimbleModes.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.CycleGimbleModes[1]].button(scmap.CycleGimbleModes[0]).is_pressed = event.is_pressed

acquireMissileLockDecorator = pvAcquireMissileLock.create_decorator(mode.value)
@acquireMissileLockDecorator.button(pvAcquireMissileLock.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.AcquireMissileLock[1]].button(scmap.AcquireMissileLock[0]).is_pressed = event.is_pressed

launchMissileDecorator = pvLaunchMissile.create_decorator(mode.value)
@launchMissileDecorator.button(pvLaunchMissile.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.LaunchMissile[1]].button(scmap.LaunchMissile[0]).is_pressed = event.is_pressed

reticleModeToggleDecorator = pvReticleModeToggle.create_decorator(mode.value)
@reticleModeToggleDecorator.button(pvReticleModeToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ReticleModeToggle[1]].button(scmap.ReticleModeToggle[0]).is_pressed = event.is_pressed

lookAheadDecorator = pvLookAhead.create_decorator(mode.value)
@lookAheadDecorator.button(pvLookAhead.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.LookAhead[1]].button(scmap.LookAhead[0]).is_pressed = event.is_pressed

targetFocusDecorator = pvTargetFocus.create_decorator(mode.value)
@targetFocusDecorator.button(pvTargetFocus.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.TargetFocus[1]].button(scmap.TargetFocus[0]).is_pressed = event.is_pressed
