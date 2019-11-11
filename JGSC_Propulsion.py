"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                         Joystick Gremlin Star Citizen
              (Complete Star Citizen 3.7 Joystick Gremlin Plugin)
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import scmap
from gremlin.user_plugin import *

g_isStrafeUpDown = 0     # a value of 0, 1, or -1
g_isStrafeLeftRight = 0  # a value of 0, 1, or -1

mode = ModeVariable("Mode", "The mode to use for this mapping")

pvMODE_0 = PhysicalInputVariable("[MODE 0] Ship Off",
                    "Turns ship off and enables ground vehicle controls for rudders",
                    [gremlin.common.InputType.JoystickButton])

pvPitch = PhysicalInputVariable("Stick Up/Down",
                    "Default Pitch Axis",
                    [gremlin.common.InputType.JoystickAxis])

pvYaw = PhysicalInputVariable("Stick Left/Right",
                    "Default Yaw Axis",
                    [gremlin.common.InputType.JoystickAxis])

pvThrottleForwardBack = PhysicalInputVariable("Throttle",
                    "Throttle Axis",
                    [gremlin.common.InputType.JoystickAxis])

pvToeBrakeLeft = PhysicalInputVariable("Left Toe Brake",
                    "Left Toe Brake Axis",
                    [gremlin.common.InputType.JoystickAxis])

pvToeBrakeRight = PhysicalInputVariable("Right Toe Brake",
                    "Right Toe Brake Axis",
                    [gremlin.common.InputType.JoystickAxis])

pvRudder = PhysicalInputVariable("Rudder",
                    "Rudder pedal's main axis",
                    [gremlin.common.InputType.JoystickAxis])
                    
bInvertRudder = BoolVariable("Invert Rudder Axis",
                    "Inverts the rudder pedal's main axis",
                    True)

pvSWITCH_SwapYawRoll = PhysicalInputVariable("[SWITCH] Swap Yaw/Roll",
                    "When enabled, this switch will swap the stick and rudders' yaw and roll axis",
                    [gremlin.common.InputType.JoystickButton])

pvSWITCH_PrecisionMode = PhysicalInputVariable("[SWITCH] Precision Mode",
                    "When enabled, The center detent is stop, forward and backward goes that way respectively",
                    #"When enabled, The center detent would be SCM speed, and the back, and forward half would interpolate between stopped, and max respectively",
                    [gremlin.common.InputType.JoystickButton])

pvPrecisionSlider = PhysicalInputVariable("Acceleration Limiter Axis",
                    "How much axis sensitivity when using thrusters",
                    [gremlin.common.InputType.JoystickAxis])

pvStrafeUp = PhysicalInputVariable("Strafe Up",
                    "Strafe Up Button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvStrafeDown = PhysicalInputVariable("Strafe Down",
                    "Strafe Down Button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvStrafeLeft = PhysicalInputVariable("Strafe Left",
                    "Strafe Left Button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvStrafeRight = PhysicalInputVariable("Strafe Right",
                    "Strafe Right Button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvDecoupledModeToggle = PhysicalInputVariable("Decoupled Mode Toggle",
                    "Decoupled mode toggle Button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

pvMatchTargetVelocity = PhysicalInputVariable("Match Target Velocity",
                    "Match target's velocity Button",
                    [gremlin.common.InputType.JoystickButton, gremlin.common.InputType.JoystickHat])

def setStrafe(vjoy, joy):
    global g_isStrafeUpDown
    global g_isStrafeLeftRight
    vjoy[scmap.AXIS_StrafeUpDown[1]].axis(scmap.AXIS_StrafeUpDown[0]).value = g_isStrafeUpDown;
    vjoy[scmap.AXIS_StrafeLeftRight[1]].axis(scmap.AXIS_StrafeLeftRight[0]).value = g_isStrafeLeftRight

def setThrottle(vjoy, joy):
    leftPedalAmt = joy[pvToeBrakeLeft.device_guid].axis(pvToeBrakeLeft.input_id).value
    leftPedalAmt = (leftPedalAmt * 0.5) + 0.5 # Normalize axis to 0..1
    rightPedalAmt = joy[pvToeBrakeRight.device_guid].axis(pvToeBrakeRight.input_id).value
    rightPedalAmt = (rightPedalAmt * 0.5) + 0.5 # Normalize axis to 0..1
    
    if joy[pvMODE_0.device_guid].button(pvMODE_0.input_id).is_pressed:
        ###################################################################################################
        # On gound vehicle gas/brake
        toeBrakeNormalized = 0 # a value from [-1.0 -> 1.0] that is calculated via both rudder toe brakes
        if leftPedalAmt > rightPedalAmt:
            toeBrakeNormalized = leftPedalAmt * -1
        else:
            toeBrakeNormalized = rightPedalAmt
        if abs(toeBrakeNormalized) < 0.1:
            toeBrakeNormalized = 0
        vjoy[scmap.AXIS_DriveForwardBackward[1]].axis(scmap.AXIS_DriveForwardBackward[0]).value = toeBrakeNormalized * -1
    else:
        scmPivot = 0.33
        deadZoneAmt = 0.1
        ###################################################################################################
        # Apply ship throttle
        throttleAmt = joy[pvThrottleForwardBack.device_guid].axis(pvThrottleForwardBack.input_id).value
        if joy[pvSWITCH_PrecisionMode.device_guid].button(pvSWITCH_PrecisionMode.input_id).is_pressed:
            ###################################################################################################
            # Precision Mode (Blue)
            if leftPedalAmt > 0.1:
                spdLimiterAbsValue = (-1.0 + scmPivot) + (scmPivot * -leftPedalAmt)
                vjoy[scmap.AXIS_SpeedLimiterRel[1]].axis(scmap.AXIS_SpeedLimiterRel[0]).value = 0
                vjoy[scmap.AXIS_SpeedLimiterAbs[1]].axis(scmap.AXIS_SpeedLimiterAbs[0]).value = spdLimiterAbsValue
            else:
                if rightPedalAmt < 0.1:
                    rightPedalAmt = 0
                vjoy[scmap.AXIS_SpeedLimiterRel[1]].axis(scmap.AXIS_SpeedLimiterRel[0]).value = rightPedalAmt
            if throttleAmt > -deadZoneAmt and throttleAmt < deadZoneAmt:
                throttleAmt = 0
            vjoy[scmap.AXIS_ThrottleForwardBack[1]].axis(scmap.AXIS_ThrottleForwardBack[0]).value = throttleAmt
        else:
            ###################################################################################################
            # Cruise Mode (Green)
            vjoy[scmap.Spacebrake[1]].button(scmap.Spacebrake[0]).is_pressed = (leftPedalAmt > 0.5)
            vjoy[scmap.Afterburner[1]].button(scmap.Afterburner[0]).is_pressed = (rightPedalAmt > 0.5)
            # Doing calculations in positive space [0..2]
            if throttleAmt < -deadZoneAmt:
                throttleAmt = 1.0 + throttleAmt # throttleAmt is now a value 0..1, but representing the negative half amount (acending values towards center detent)
                vjoy[scmap.AXIS_ThrottleForwardBack[1]].axis(scmap.AXIS_ThrottleForwardBack[0]).value = throttleAmt
                throttleAmt = scmPivot
            elif throttleAmt > deadZoneAmt:
                throttleAmt = scmPivot + ((2.0 - scmPivot) * throttleAmt)
                vjoy[scmap.AXIS_ThrottleForwardBack[1]].axis(scmap.AXIS_ThrottleForwardBack[0]).value = 1.0
            else:
                throttleAmt = scmPivot
                vjoy[scmap.AXIS_ThrottleForwardBack[1]].axis(scmap.AXIS_ThrottleForwardBack[0]).value = 1.0
            # Puts throttleAmt back into a [-1..1] range
            throttleAmt = throttleAmt - 1.0
            # Assign throttleAmt to speed limiter's absolute value, and set throttle to max to match it
            vjoy[scmap.AXIS_SpeedLimiterRel[1]].axis(scmap.AXIS_SpeedLimiterRel[0]).value = 0
            vjoy[scmap.AXIS_SpeedLimiterAbs[1]].axis(scmap.AXIS_SpeedLimiterAbs[0]).value = throttleAmt

pitchDecorator = pvPitch.create_decorator(mode.value)
@pitchDecorator.axis(pvPitch.input_id)
def onAxis(event, vjoy):
    vjoy[scmap.AXIS_Pitch[1]].axis(scmap.AXIS_Pitch[0]).value = event.value

yawDecorator = pvYaw.create_decorator(mode.value)
@yawDecorator.axis(pvYaw.input_id)
def onAxis(event, vjoy, joy):
    if joy[pvSWITCH_SwapYawRoll.device_guid].button(pvSWITCH_SwapYawRoll.input_id).is_pressed:
        vjoy[scmap.AXIS_Roll[1]].axis(scmap.AXIS_Roll[0]).value = event.value
    else:
        vjoy[scmap.AXIS_Yaw[1]].axis(scmap.AXIS_Yaw[0]).value = event.value

rudderDecorator = pvRudder.create_decorator(mode.value)
@rudderDecorator.axis(pvRudder.input_id)
def onAxis(event, vjoy, joy):
    if joy[pvSWITCH_SwapYawRoll.device_guid].button(pvSWITCH_SwapYawRoll.input_id).is_pressed:
        vjoy[scmap.AXIS_Yaw[1]].axis(scmap.AXIS_Yaw[0]).value = event.value * (-1 if bInvertRudder.value else 1)
    else:
        vjoy[scmap.AXIS_Roll[1]].axis(scmap.AXIS_Roll[0]).value = event.value * (-1 if bInvertRudder.value else 1)
    
    #vjoy[scmap.EVA_RollLeftRight[1]].axis(scmap.EVA_RollLeftRight[0]).value = event.value * (-1 if bInvertRudder.value else 1)

swapYawRollDecorator = pvSWITCH_SwapYawRoll.create_decorator(mode.value)
@swapYawRollDecorator.button(pvSWITCH_SwapYawRoll.input_id)
def onBtn(event, vjoy, joy):
    if event.is_pressed:
        vjoy[scmap.AXIS_Yaw[1]].axis(scmap.AXIS_Yaw[0]).value = joy[pvRudder.device_guid].axis(pvRudder.input_id).value * (-1 if bInvertRudder.value else 1)
        vjoy[scmap.AXIS_Roll[1]].axis(scmap.AXIS_Roll[0]).value = joy[pvYaw.device_guid].axis(pvYaw.input_id).value
    else:
        vjoy[scmap.AXIS_Yaw[1]].axis(scmap.AXIS_Yaw[0]).value = joy[pvYaw.device_guid].axis(pvYaw.input_id).value
        vjoy[scmap.AXIS_Roll[1]].axis(scmap.AXIS_Roll[0]).value = joy[pvRudder.device_guid].axis(pvRudder.input_id).value * (-1 if bInvertRudder.value else 1)

throttleDecorator = pvThrottleForwardBack.create_decorator(mode.value)
@throttleDecorator.axis(pvThrottleForwardBack.input_id)
def onAxis(event, vjoy, joy):
    setThrottle(vjoy, joy)

precisionModeDecorator = pvSWITCH_PrecisionMode.create_decorator(mode.value)
@precisionModeDecorator.button(pvSWITCH_PrecisionMode.input_id)
def onBtn(event, vjoy, joy):
    if event.is_pressed:
        vjoy[scmap.Spacebrake[1]].button(scmap.Spacebrake[0]).is_pressed = False
        vjoy[scmap.Afterburner[1]].button(scmap.Afterburner[0]).is_pressed = False
    setStrafe(vjoy, joy)
    setThrottle(vjoy, joy)

precisionSliderDecorator = pvPrecisionSlider.create_decorator(mode.value)
@precisionSliderDecorator.axis(pvPrecisionSlider.input_id)
def onAxis(event, vjoy):
    vjoy[scmap.AXIS_AccelerationLimiterAbs[1]].axis(scmap.AXIS_AccelerationLimiterAbs[0]).value = event.value

toeBrakeLeftDecorator = pvToeBrakeLeft.create_decorator(mode.value)
@toeBrakeLeftDecorator.axis(pvToeBrakeLeft.input_id)
def onAxis(event, vjoy, joy):
    setThrottle(vjoy, joy)

toeBrakeRightDecorator = pvToeBrakeRight.create_decorator(mode.value)
@toeBrakeRightDecorator.axis(pvToeBrakeRight.input_id)
def onAxis(event, vjoy, joy):
    setThrottle(vjoy, joy)

strafeUpDecorator = pvStrafeUp.create_decorator(mode.value)
@strafeUpDecorator.button(pvStrafeUp.input_id)
def onBtn(event, vjoy, joy):
    global g_isStrafeUpDown
    g_isStrafeUpDown = 1 if event.is_pressed else 0
    setStrafe(vjoy, joy)

strafeDownDecorator = pvStrafeDown.create_decorator(mode.value)
@strafeDownDecorator.button(pvStrafeDown.input_id)
def onBtn(event, vjoy, joy):
    global g_isStrafeUpDown
    g_isStrafeUpDown = -1 if event.is_pressed else 0
    setStrafe(vjoy, joy)

strafeLeftDecorator = pvStrafeLeft.create_decorator(mode.value)
@strafeLeftDecorator.button(pvStrafeLeft.input_id)
def onBtn(event, vjoy, joy):
    global g_isStrafeLeftRight
    g_isStrafeLeftRight = -1 if event.is_pressed else 0
    setStrafe(vjoy, joy)

strafeRightDecorator = pvStrafeRight.create_decorator(mode.value)
@strafeRightDecorator.button(pvStrafeRight.input_id)
def onBtn(event, vjoy, joy):
    global g_isStrafeLeftRight
    g_isStrafeLeftRight = 1 if event.is_pressed else 0
    setStrafe(vjoy, joy)

decoupledModeToggleDecorator = pvDecoupledModeToggle.create_decorator(mode.value)
@decoupledModeToggleDecorator.button(pvDecoupledModeToggle.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.DecoupledModeToggle[1]].button(scmap.DecoupledModeToggle[0]).is_pressed = event.is_pressed

matchTargetVelocityDecorator = pvMatchTargetVelocity.create_decorator(mode.value)
@matchTargetVelocityDecorator.button(pvMatchTargetVelocity.input_id)
def onBtn(event, vjoy):
    vjoy[scmap.MatchTargetVelocity[1]].button(scmap.MatchTargetVelocity[0]).is_pressed = event.is_pressed
