"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                         Joystick Gremlin Star Citizen
              (Complete Star Citizen 3.5 Joystick Gremlin Plugin)
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import scmap
from container_plugins.tempo import *
from action_plugins.remap import *
from gremlin.user_plugin import *

mode = ModeVariable("Mode", "The mode to use for this mapping")

pvLeftAnalogX = PhysicalInputVariable("Left Analog X",
                    "Left analog stick X",
                    [gremlin.common.InputType.JoystickAxis])

pvLeftAnalogY = PhysicalInputVariable("Left Analog Y",
                    "Left analog stick Y",
                    [gremlin.common.InputType.JoystickAxis])
                    
pvRightAnalogX = PhysicalInputVariable("Right Analog X",
                    "Left analog stick X",
                    [gremlin.common.InputType.JoystickAxis])

pvRightAnalogY = PhysicalInputVariable("Right Analog Y",
                    "Left analog stick Y",
                    [gremlin.common.InputType.JoystickAxis])

pvTriggers = PhysicalInputVariable("Triggers",
                    "Trigger axis",
                    [gremlin.common.InputType.JoystickAxis])

pvModifier = PhysicalInputVariable("Modifier Button",
                    "Modifier button for alternate actions",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

#pvJump = PhysicalInputVariable("Jump",
#                    "Jump button",
#                    [gremlin.common.InputType.JoystickButton,
#                     gremlin.common.InputType.JoystickHat])

pvCrouch = PhysicalInputVariable("Crouch",
                    "Crouch button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvProne = PhysicalInputVariable("Prone",
                    "Prone button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

#pvSprint = PhysicalInputVariable("Sprint",
#                    "Sprint button",
#                    [gremlin.common.InputType.JoystickButton,
#                     gremlin.common.InputType.JoystickHat])

pvSelectGadget = PhysicalInputVariable("Select Gadget (or Contract Item)",
                    "Select gadget button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvReload = PhysicalInputVariable("Reload",
                    "Reload button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvDropItem = PhysicalInputVariable("Drop Item",
                    "Drop item button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvFlashlightToggle = PhysicalInputVariable("Flashlight Toggle",
                    "Flashlight toggle button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvThirdPersonViewToggle = PhysicalInputVariable("Third Person View Toggle",
                    "Third person view toggle button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvThirdPersonFreeViewToggle = PhysicalInputVariable("Third Person Free View Toggle",
                    "Third person free view toggle button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvSelfieCam = PhysicalInputVariable("Selfie Cam",
                    "Selfie cam button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvMobiGlas = PhysicalInputVariable("MobiGlas (or Map)",
                    "Third person free view toggle button",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

pvCommLinkAppToggle = PhysicalInputVariable("CommLink App (or Toggle Chat)",
                    "Brings up Comm Link App in MobiGlass or alternately toggles chat window",
                    [gremlin.common.InputType.JoystickButton,
                     gremlin.common.InputType.JoystickHat])

leftAnalogXDecorator = pvLeftAnalogX.create_decorator(mode.value)
@leftAnalogXDecorator.axis(pvLeftAnalogX.input_id)
def onAxis(event, vjoy):
    vjoy[scmap.AXIS_MoveLeftRight[1]].axis(scmap.AXIS_MoveLeftRight[0]).value = event.value

leftAnalogYDecorator = pvLeftAnalogY.create_decorator(mode.value)
@leftAnalogYDecorator.axis(pvLeftAnalogY.input_id)
def onAxis(event, vjoy):
    vjoy[scmap.AXIS_MoveForwardBackward[1]].axis(scmap.AXIS_MoveForwardBackward[0]).value = event.value

triggersDecorator = pvTriggers.create_decorator(mode.value)
@triggersDecorator.axis(pvTriggers.input_id)
def onAxis(event, vjoy):
    pass

modifierDecorator = pvModifier.create_decorator(mode.value)
@modifierDecorator.button(pvModifier.input_id)
def onBtn(event, vjoy):
    gremlin.util.log("modifer pressed")
    vjoy[scmap.Crouch[1]].button(scmap.Crouch[0]).is_pressed = event.is_pressed

crouchDecorator = pvCrouch.create_decorator(mode.value)
@crouchDecorator.button(pvCrouch.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.Crouch[1]].button(scmap.Crouch[0]).is_pressed = event.is_pressed

proneDecorator = pvProne.create_decorator(mode.value)
@proneDecorator.button(pvProne.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.Prone[1]].button(scmap.Prone[0]).is_pressed = event.is_pressed

selectGadgetDecorator = pvSelectGadget.create_decorator(mode.value)
@selectGadgetDecorator.button(pvSelectGadget.input_id)
def onBtn(event, vjoy, joy):
    if joy[pvModifier.device_guid].button(pvModifier.input_id).is_pressed:
        vjoy[scmap.SelectContractItem[1]].button(scmap.SelectContractItem[0]).is_pressed = event.is_pressed
    else:
        vjoy[scmap.SelectGadget[1]].button(scmap.SelectGadget[0]).is_pressed = event.is_pressed

reloadDecorator = pvReload.create_decorator(mode.value)
@reloadDecorator.button(pvReload.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.Reload[1]].button(scmap.Reload[0]).is_pressed = event.is_pressed

dropItemDecorator = pvDropItem.create_decorator(mode.value)
@dropItemDecorator.button(pvDropItem.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.SelfDestruct[1]].button(scmap.SelfDestruct[0]).is_pressed = event.is_pressed

flashlightToggleDecorator = pvFlashlightToggle.create_decorator(mode.value)
@flashlightToggleDecorator.button(pvFlashlightToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.FlashlightToggle[1]].button(scmap.FlashlightToggle[0]).is_pressed = event.is_pressed

thirdPersonViewToggleDecorator = pvThirdPersonViewToggle.create_decorator(mode.value)
@thirdPersonViewToggleDecorator.button(pvThirdPersonViewToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ThirdPersonViewToggle[1]].button(scmap.ThirdPersonViewToggle[0]).is_pressed = event.is_pressed

thirdPersonFreeViewToggleDecorator = pvThirdPersonFreeViewToggle.create_decorator(mode.value)
@thirdPersonFreeViewToggleDecorator.button(pvThirdPersonFreeViewToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ThirdPersonFreeViewToggle[1]].button(scmap.ThirdPersonFreeViewToggle[0]).is_pressed = event.is_pressed

mobiGlasDecorator = pvMobiGlas.create_decorator(mode.value)
@mobiGlasDecorator.button(pvMobiGlas.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.MobiGlas[1]].button(scmap.MobiGlas[0]).is_pressed = event.is_pressed
