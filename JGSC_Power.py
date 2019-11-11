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

pvPowerPreset1Increase = PhysicalInputVariable("Increase Weapon Power",
                    "Hold to increase power to weapons",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvPowerPreset2Increase = PhysicalInputVariable("Increase Shield Power",
                    "Hold to increase power to shields",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvPowerPreset3Increase = PhysicalInputVariable("Increase Engine Power",
                    "Hold to increase power to engines",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvResetPowerDistribution = PhysicalInputVariable("Reset Power Distribution",
                    "Balances power between weapons, shields, and engines",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvIncreasePower = PhysicalInputVariable("Increase Overall Power",
                    "Increase power draw from reactor, raising signature",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvDecreasePower = PhysicalInputVariable("Decrease Overall Power",
                    "Decrease power draw from reactor, lowering signature",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvIncreasePowerMax = PhysicalInputVariable("Use Maximum Power",
                    "Draws full power from reactor",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvDecreasePowerMin = PhysicalInputVariable("Use Minimum Power",
                    "Draws no power from reactor",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvPowerPreset1Toggle = PhysicalInputVariable("Toggle Weapons",
                    "Toggles weapons system ON and OFF",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvPowerPreset2Toggle = PhysicalInputVariable("Toggle Shields",
                    "Toggles shields system ON and OFF",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvPowerPreset3Toggle = PhysicalInputVariable("Toggle Engines",
                    "Toggles engines system ON and OFF",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvPowerToggle = PhysicalInputVariable("Toggle All Power",
                    "Toggles power to everything ON and OFF",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

powerPreset1IncreaseDecorator = pvPowerPreset1Increase.create_decorator(mode.value)
@powerPreset1IncreaseDecorator.button(pvPowerPreset1Increase.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.PowerPreset1Increase[1]].button(scmap.PowerPreset1Increase[0]).is_pressed = event.is_pressed

powerPreset2IncreaseDecorator = pvPowerPreset2Increase.create_decorator(mode.value)
@powerPreset2IncreaseDecorator.button(pvPowerPreset2Increase.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.PowerPreset2Increase[1]].button(scmap.PowerPreset2Increase[0]).is_pressed = event.is_pressed

powerPreset3IncreaseDecorator = pvPowerPreset3Increase.create_decorator(mode.value)
@powerPreset3IncreaseDecorator.button(pvPowerPreset3Increase.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.PowerPreset3Increase[1]].button(scmap.PowerPreset3Increase[0]).is_pressed = event.is_pressed

resetPowerDistributionDecorator = pvResetPowerDistribution.create_decorator(mode.value)
@resetPowerDistributionDecorator.button(pvResetPowerDistribution.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ResetPowerDistribution[1]].button(scmap.ResetPowerDistribution[0]).is_pressed = event.is_pressed

increasePowerDecorator = pvIncreasePower.create_decorator(mode.value)
@increasePowerDecorator.button(pvIncreasePower.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.IncreasePower[1]].button(scmap.IncreasePower[0]).is_pressed = event.is_pressed

decreasePowerDecorator = pvDecreasePower.create_decorator(mode.value)
@decreasePowerDecorator.button(pvDecreasePower.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.DecreasePower[1]].button(scmap.DecreasePower[0]).is_pressed = event.is_pressed

increasePowerMaxDecorator = pvIncreasePowerMax.create_decorator(mode.value)
@increasePowerMaxDecorator.button(pvIncreasePowerMax.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.IncreasePowerMax[1]].button(scmap.IncreasePowerMax[0]).is_pressed = event.is_pressed

decreasePowerMinDecorator = pvDecreasePowerMin.create_decorator(mode.value)
@decreasePowerMinDecorator.button(pvDecreasePowerMin.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.DecreasePowerMin[1]].button(scmap.DecreasePowerMin[0]).is_pressed = event.is_pressed

powerPreset1ToggleDecorator = pvPowerPreset1Toggle.create_decorator(mode.value)
@powerPreset1ToggleDecorator.button(pvPowerPreset1Toggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.PowerPreset1Toggle[1]].button(scmap.PowerPreset1Toggle[0]).is_pressed = event.is_pressed

powerPreset2ToggleDecorator = pvPowerPreset2Toggle.create_decorator(mode.value)
@powerPreset2ToggleDecorator.button(pvPowerPreset2Toggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.PowerPreset2Toggle[1]].button(scmap.PowerPreset2Toggle[0]).is_pressed = event.is_pressed

powerPreset3ToggleDecorator = pvPowerPreset3Toggle.create_decorator(mode.value)
@powerPreset3ToggleDecorator.button(pvPowerPreset3Toggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.PowerPreset3Toggle[1]].button(scmap.PowerPreset3Toggle[0]).is_pressed = event.is_pressed

powerToggleDecorator = pvPowerToggle.create_decorator(mode.value)
@powerToggleDecorator.button(pvPowerToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.PowerToggle[1]].button(scmap.PowerToggle[0]).is_pressed = event.is_pressed
