"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                         Joystick Gremlin Star Citizen
              (Complete Star Citizen 3.7 Joystick Gremlin Plugin)
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import scmap
import threading
from gremlin.user_plugin import *
from gremlin.macro import *

mode = ModeVariable("Mode", "The mode to use for this mapping")

pvAimLeftRight = PhysicalInputVariable("Aim Thumbstick Left/Right",
                    "Aims left and right along an axis",
                    [gremlin.common.InputType.JoystickAxis])

pvAimUpDown = PhysicalInputVariable("Aim Thumbstick Up/Down",
                    "Aims up and down along an axis",
                    [gremlin.common.InputType.JoystickAxis])

pvResetAim = PhysicalInputVariable("Reset Aim",
                    "Reset gimble reticle button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvCycleAll = PhysicalInputVariable("Cycle All (back)",
                    "Cycle all targets. Hold to cycle backward",
                    [gremlin.common.InputType.JoystickButton])#, gremlin.common.InputType.JoystickHat])

pvCycleNext = PhysicalInputVariable("Cycle Next Enemy (Friendly)",
                    "Cycle next enemy target. Hold to cycle next friendly",
                    [gremlin.common.InputType.JoystickButton])#, gremlin.common.InputType.JoystickHat])

pvCyclePrev = PhysicalInputVariable("Cycle Previous Enemy (Friendly)",
                    "Cycle previous enemy target. Hold to cycle previous friendly",
                    [gremlin.common.InputType.JoystickButton])#, gremlin.common.InputType.JoystickHat])

pvReticleFocus = PhysicalInputVariable("Reticle Focus (Pin Selected)",
                    "Target object under reticle. Hold to pin currently selected target",
                    [gremlin.common.InputType.JoystickButton])#, gremlin.common.InputType.JoystickHat])

pvTargetNearest = PhysicalInputVariable("Target Nearest Hostile (Cycle Pinned)",
                    "Target nearest hostile. Hold to cycle next pinned target",
                    [gremlin.common.InputType.JoystickButton])#, gremlin.common.InputType.JoystickHat])

pvSubTargetModifierKey = PhysicalInputVariable("Subtarget Modifer Key/Switch",
                    "When pressed/held, it cycles/resets subtarget instead of cycle/resets target",
                    [gremlin.common.InputType.JoystickButton])#, gremlin.common.InputType.JoystickHat])

pvDynamicZoomInOut = PhysicalInputVariable("Dynamic Zoom Axis",
                    "Zooms in and out cockpit view along an axis",
                    [gremlin.common.InputType.JoystickAxis])

pvScanningModeToggle = PhysicalInputVariable("Scanning Mode Toggle",
                    "Toggle scanning mode",
                    [gremlin.common.InputType.JoystickButton])

pvActivateScanning = PhysicalInputVariable("Activate Scanning",
                    "Activate scanning or something",
                    [gremlin.common.InputType.JoystickButton])

pvScanningIncreaseRadarAngle = PhysicalInputVariable("Increase Scanning Radar Angle",
                    "Increase Radar Angle for scans",
                    [gremlin.common.InputType.JoystickButton])

pvScanningDecreaseRadarAngle = PhysicalInputVariable("Decrease Scanning Radar Angle",
                    "Decrease Radar Angle for scans",
                    [gremlin.common.InputType.JoystickButton])

class JGSCTempo:
    def __init__(self, scmap_short, scmap_long):
        self.delay = 0.5
        self.start_time = 0
        self.timer = None
        
        shortActionPress = VJoyAction(scmap_short[1], gremlin.common.InputType.JoystickButton, scmap_short[0], True)
        shortActionRelease = VJoyAction(scmap_short[1], gremlin.common.InputType.JoystickButton, scmap_short[0], False)
        self.vBtnPressMacroShort = Macro()
        self.vBtnPressMacroShort.add_action(shortActionPress)
        self.vBtnPressMacroShort.pause(0.1)
        self.vBtnPressMacroShort.add_action(shortActionRelease)
        
        longActionPress = VJoyAction(scmap_long[1], gremlin.common.InputType.JoystickButton, scmap_long[0], True)
        longActionRelease = VJoyAction(scmap_long[1], gremlin.common.InputType.JoystickButton, scmap_long[0], False)
        self.vBtnPressMacroLong = Macro()
        self.vBtnPressMacroLong.add_action(longActionPress)
        self.vBtnPressMacroLong.pause(0.1)
        self.vBtnPressMacroLong.add_action(longActionRelease)
    
    def process_event(self, event):
        if event.is_pressed:
            self.start_time = time.time()
            self.timer = threading.Timer(self.delay, self._long_press)
            self.timer.start()
        else:
            if (self.start_time + self.delay) > time.time():
                # Short press
                self.timer.cancel()
                MacroManager().queue_macro(self.vBtnPressMacroShort)
    
    def _long_press(self):
        MacroManager().queue_macro(self.vBtnPressMacroLong)
        self.timer.cancel()
        self.timer = None

aimLeftRightDecorator = pvAimLeftRight.create_decorator(mode.value)
@aimLeftRightDecorator.axis(pvAimLeftRight.input_id)
def onAxis(event, vjoy):
    vjoy[scmap.AXIS_AimLeftRight[1]].axis(scmap.AXIS_AimLeftRight[0]).value = event.value

aimUpDownDecorator = pvAimUpDown.create_decorator(mode.value)
@aimUpDownDecorator.axis(pvAimUpDown.input_id)
def onAxis(event, vjoy):
    vjoy[scmap.AXIS_AimUpDown[1]].axis(scmap.AXIS_AimUpDown[0]).value = event.value

resetAimDecorator = pvResetAim.create_decorator(mode.value)
@resetAimDecorator.button(pvResetAim.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ResetAim[1]].button(scmap.ResetAim[0]).is_pressed = event.is_pressed

cycleAllTempo = JGSCTempo(scmap.CycleAllTargets, scmap.CycleAllTargetsBack)
cycleAllDecorator = pvCycleAll.create_decorator(mode.value)
@cycleAllDecorator.button(pvCycleAll.input_id)
def onBtn(event):
    cycleAllTempo.process_event(event)

cycleNextTempo = JGSCTempo(scmap.CycleHostileTargets, scmap.CycleFriendlyTargets)
cycleNextDecorator = pvCycleNext.create_decorator(mode.value)
@cycleNextDecorator.button(pvCycleNext.input_id)
def onBtn(event, vjoy, joy):
    if joy[pvSubTargetModifierKey.device_guid].button(pvSubTargetModifierKey.input_id).is_pressed:
        vjoy[scmap.CycleSubTarget[1]].button(scmap.CycleSubTarget[0]).is_pressed = event.is_pressed
    else:
        cycleNextTempo.process_event(event)

cyclePrevTempo = JGSCTempo(scmap.CycleHostileTargetsBack, scmap.CycleFriendlyTargetsBack)
cyclePrevDecorator = pvCyclePrev.create_decorator(mode.value)
@cyclePrevDecorator.button(pvCyclePrev.input_id)
def onBtn(event, vjoy, joy):
    if joy[pvSubTargetModifierKey.device_guid].button(pvSubTargetModifierKey.input_id).is_pressed:
        vjoy[scmap.CycleSubTargetBack[1]].button(scmap.CycleSubTargetBack[0]).is_pressed = event.is_pressed
    else:
        cyclePrevTempo.process_event(event)

reticleFocusTempo = JGSCTempo(scmap.ReticleFocus, scmap.PinFocusedTarget)
reticleFocusDecorator = pvReticleFocus.create_decorator(mode.value)
@reticleFocusDecorator.button(pvReticleFocus.input_id)
def onBtn(event, vjoy, joy):
    if joy[pvSubTargetModifierKey.device_guid].button(pvSubTargetModifierKey.input_id).is_pressed:
        vjoy[scmap.ResetSubTarget[1]].button(scmap.ResetSubTarget[0]).is_pressed = event.is_pressed
    else:
        reticleFocusTempo.process_event(event)

targetNearestTempo = JGSCTempo(scmap.TargetNearestHostile, scmap.CyclePinnedTargets)
targetNearestDecorator = pvTargetNearest.create_decorator(mode.value)
@targetNearestDecorator.button(pvTargetNearest.input_id)
def onBtn(event):
    targetNearestTempo.process_event(event)

subTargetModifierKeyDecorator = pvSubTargetModifierKey.create_decorator(mode.value)
@subTargetModifierKeyDecorator.button(pvSubTargetModifierKey.input_id)
def onBtn(event, vjoy):
    if not event.is_pressed:
        vjoy[scmap.CycleSubTarget[1]].button(scmap.CycleSubTarget[0]).is_pressed = False
        vjoy[scmap.CycleSubTargetBack[1]].button(scmap.CycleSubTargetBack[0]).is_pressed = False
        vjoy[scmap.ResetSubTarget[1]].button(scmap.ResetSubTarget[0]).is_pressed = False

dynamicZoomInOutDecorator = pvDynamicZoomInOut.create_decorator(mode.value)
@dynamicZoomInOutDecorator.axis(pvDynamicZoomInOut.input_id)
def onAxis(event, vjoy):
    vjoy[scmap.AXIS_DynamicZoomInAndOut[1]].axis(scmap.AXIS_DynamicZoomInAndOut[0]).value = event.value

scanningModeToggleDecorator = pvScanningModeToggle.create_decorator(mode.value)
@scanningModeToggleDecorator.button(pvScanningModeToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ScanningModeToggle[1]].button(scmap.ScanningModeToggle[0]).is_pressed = event.is_pressed

activateScanningDecorator = pvActivateScanning.create_decorator(mode.value)
@activateScanningDecorator.button(pvActivateScanning.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ActivateScanning[1]].button(scmap.ActivateScanning[0]).is_pressed = event.is_pressed

scanningIncreaseRadarAngleDecorator = pvScanningIncreaseRadarAngle.create_decorator(mode.value)
@scanningIncreaseRadarAngleDecorator.button(pvScanningIncreaseRadarAngle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ScanningIncreaseRadarAngle[1]].button(scmap.ScanningIncreaseRadarAngle[0]).is_pressed = event.is_pressed

scanningDecreaseRadarAngleDecorator = pvScanningDecreaseRadarAngle.create_decorator(mode.value)
@scanningDecreaseRadarAngleDecorator.button(pvScanningDecreaseRadarAngle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.ScanningDecreaseRadarAngle[1]].button(scmap.ScanningDecreaseRadarAngle[0]).is_pressed = event.is_pressed
