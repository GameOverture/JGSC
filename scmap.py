"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                         Joystick Gremlin Star Citizen
              (Complete Star Citizen 3.7 Joystick Gremlin Plugin)
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
from gremlin.macro import *
from vjoy.vjoy import AxisName

# Specify vJoy IDs
VJOY_1 = 1
VJOY_2 = 2
VJOY_3 = 3

# Keyboard only inputs in Star Citizen
KB_CameraModifier = Key("F4", 0x3e, False, win32con.VK_F4)

                        ############################
######################### Flight - Cockpit         ###########################
                        ############################
Eject = (1, VJOY_1)
ExitSeat = (2, VJOY_1)
SelfDestruct = (3, VJOY_1)
#EmergencyExitSeat = double tap of ExitSeat
IncreaseCoolerRate = (4, VJOY_1)
DecreaseCoolerRate = (5, VJOY_1)
FlightSystemsReady = (6, VJOY_1)
#ToggleOpenCloseDoors
OpenAllDoors = (7, VJOY_1)
CloseAllDoors = (8, VJOY_1)
#ToggleLockUnlockDoors
LockAllDoors = (9, VJOY_1)
UnlockAllDoors = (10, VJOY_1)
                        ############################
######################### Flight - View            ###########################
                        ############################
#Look... = handled by mouse
#CycleCameraView = handled by mouse
#CycleCameraOrbitMode = handled by mouse
#ZoomIn = handled by mouse
#ZoomOut = handled by mouse
#FreeLookToggle = handled by mouse
AXIS_DynamicZoomInAndOut = (AxisName.SL0, VJOY_2)
#DynamicZoomIn = (, VJOY_1)
#DynamicZoomOut = (, VJOY_1)
LookBehind = (11, VJOY_1)
                        ############################
######################### Flight - Movement        ###########################
                        ############################
AXIS_Pitch = (AxisName.RX, VJOY_1)
AXIS_Yaw = (AxisName.RY, VJOY_1)
AXIS_Roll = (AxisName.RZ, VJOY_1)
#SwapYawRollToggle = handled with script logic
MatchTargetVelocity = (12, VJOY_1)
Spacebrake = (13, VJOY_1)
AXIS_SpeedLimiterRel = (AxisName.SL0, VJOY_1)
AXIS_SpeedLimiterAbs = (AxisName.SL1, VJOY_1)
AXIS_AccelerationLimiterAbs = (AxisName.SL1, VJOY_2)
DecoupledModeToggle = (14, VJOY_1)
AXIS_StrafeUpDown = (AxisName.Y, VJOY_1)
AXIS_StrafeLeftRight = (AxisName.X, VJOY_1)
AXIS_ThrottleForwardBack = (AxisName.Z, VJOY_1)
#SpeedLimiterToggle = not needed with script logic
GForceSafetyToggle = (15, VJOY_1)
ESPToggle = (16, VJOY_1)
#CruiseControlToggle = not needed with script logic
Afterburner = (17, VJOY_1)
LandingSystemToggle = (18, VJOY_1)
ToggleVTOL = (19, VJOY_1)
Autoland = (20, VJOY_1)
QuantumTravelSystemToggle = (21, VJOY_1)
QuantumDrive = (22, VJOY_1)
                        ############################
######################### Flight - Targeting       ###########################
                        ############################
AXIS_AimLeftRight = (AxisName.RY, VJOY_2)
AXIS_AimUpDown = (AxisName.RX, VJOY_2)
ResetAim = (23, VJOY_1)
LookAhead = (24, VJOY_1)
ReticleFocus = (26, VJOY_1)
CycleAllTargets = (27, VJOY_1)
CycleAllTargetsBack = (28, VJOY_1)
CycleFriendlyTargets = (29, VJOY_1)
CycleFriendlyTargetsBack = (30, VJOY_1)
PinFocusedTarget = (31, VJOY_1)
CyclePinnedTargets = (32, VJOY_1)
#CyclePinnedTargetsBack = (, VJOY_1)
CycleHostileTargets = (33, VJOY_1)
CycleHostileTargetsBack = (34, VJOY_1)
TargetNearestHostile = (35, VJOY_1)
CycleSubTarget = (36, VJOY_1)
CycleSubTargetBack = (37, VJOY_1)
ResetSubTarget = (38, VJOY_1)
ReticleModeToggle = (39, VJOY_1)

TargetFocus = (40, VJOY_1)

#ScanningRadarPing = (, VJOY_1)
ScanningModeToggle = (41, VJOY_1)
ActivateScanning = (42, VJOY_1)
ScanningIncreaseRadarAngle = (43, VJOY_1)
ScanningDecreaseRadarAngle = (44, VJOY_1)
                        ############################
######################### Flight - Target Hailing  ###########################
                        ############################
HailTarget = (45, VJOY_1)
                        ############################
######################### Flight - Mining          ###########################
                        ############################
MiningModeToggle = (46, VJOY_1)
#FireMiningLaserToggle = (47, VJOY_1)
#SwitchMiningLaserToggle = (48, VJOY_1)
#IncreaseMiningLaserPower = (49, VJOY_1)
#DecreaseMiningLaserPower = (50, VJOY_1)
AXIS_IncreaseDecreaseMiningLaserPower = (AxisName.SL1, VJOY_2)
                        ############################
######################### Flight - Weapons         ###########################
                        ############################
FireWeaponGroup1 = (1, VJOY_2)
FireWeaponGroup2 = (2, VJOY_2)
CycleWeaponAmmo = (3, VJOY_2)
CycleWeaponAmmoBack = (4, VJOY_2)
CycleGimbleModes = (5, VJOY_2)
TurretGyroStabilizationToggle = (6, VJOY_2)
AcquireMissileLock = (7, VJOY_2)
LaunchMissile = (8, VJOY_2)
                        ############################
######################### Flight - Defensive       ###########################
                        ############################
LaunchCountermeasure = (9, VJOY_2)
CycleCountermeasureAmmo = (10, VJOY_2)
CycleCountermeasureAmmoBack = (11, VJOY_2)
ShieldRaiseLevelFront = (12, VJOY_2)
ShieldRaiseLevelBack = (13, VJOY_2)
ShieldRaiseLevelLeft = (14, VJOY_2)
ShieldRaiseLevelRight = (15, VJOY_2)
ShieldRaiseLevelTop = (16, VJOY_2)
ShieldRaiseLevelBottom = (17, VJOY_2)
ShieldResetLevels = (18, VJOY_2)
                        ############################
######################### Flight - Power           ###########################
                        ############################
PowerPreset1Increase = (19, VJOY_2)
PowerPreset2Increase = (20, VJOY_2)
PowerPreset3Increase = (21, VJOY_2)
ResetPowerDistribution = (22, VJOY_2)
IncreasePower = (23, VJOY_2)
DecreasePower = (24, VJOY_2)
IncreasePowerMax = (25, VJOY_2)
DecreasePowerMin = (26, VJOY_2)
PowerPreset1Toggle = (27, VJOY_2)
PowerPreset2Toggle = (28, VJOY_2)
PowerPreset3Toggle = (29, VJOY_2)
PowerToggle = (30, VJOY_2)
                        ############################
######################### Flight - Radar           ###########################
                        ############################
PIBSToggle = (31, VJOY_2)
RadarCycleRange = (32, VJOY_2)
                        ############################
######################### Flight - HUD             ###########################
                        ############################
Scoreboard = (33, VJOY_2)
Map = (34, VJOY_2)
                        ############################
######################### Flight - Lights          ###########################
                        ############################
HeadlightsToggle = (35, VJOY_2)
                        ############################
######################### On Foot - All            ###########################
                        ############################
#AXIS_MoveLeftRight = (AxisName.X, VJOY_3)
#AXIS_MoveForwardBackward = (AxisName.Z, VJOY_3)
#Jump = (1, VJOY_3)
#Crouch = (2, VJOY_3)
#Prone = (3, VJOY_3)
#Sprint = (4, VJOY_3)
##LeanLeft = <rudderPedals>
##LeanRight = <rudderPedals>
##PrimaryAttack = <mouse>
##MeleeAttack = <mouse>
##ThrowItem = <mouse>
##AimDownSight = <mouse>
##ZoomOutADS = <mouse>
##ZoomInADS = <mouse>
##ZoomInOutADS = <mouse>
##SelectSidearm = <mouse>
##SelectPrimaryWeapon = <mouse>
##SelectSecondaryWeapon = <mouse>
#SelectGadget = (5, VJOY_3)
#SelectContractItem = (6, VJOY_3)
##NextWeapon = <mouse>
##PreviousWeapon = <mouse>
#Reload = (7, VJOY_3)
##HolsterWeapon = <mouse>
#DropItem = (8, VJOY_3)
##InspectItem = <mouse>
##HoldBreathADS = Sprint
##ChangeFireMode = <mouse>
##DefaultMovementSpeedIncrease
##DefaultMovementSpeedDecrease
#FlashlightToggle = (9, VJOY_3)
##Heal = <mouse>
##RefillOxygen = <mouse> (with modifier button)
#ThirdPersonViewToggle = (10, VJOY_3)
#ThirdPersonFreeViewToggle = (11, VJOY_3)
#MobiGlas = (12, VJOY_3)
##ScoreboardPortModificationInteract = <mouse>
#OnFootMap = (13, VJOY_3)
##ForceRespawn
##RollLeftWhileProne = <rudderPedals>
##RollRightWhileProne = <rudderPedals>
                        ############################
######################### E.V.A. - All             ###########################
                        ############################
#EVA_ViewLeftRight = (AxisName.RY, VJOY_3)
#EVA_ViewUpDown = (AxisName.RZ, VJOY_3)
##EVA_PitchUpDown = <mouse>
##EVA_YawLeftRight = <mouse>
#EVA_RollLeftRight = (AxisName.RZ, VJOY_2)
##EVA_StrafeUpDown
##EVA_StrafeLeftRight
##EVA_Brake = Prone
##EVA_Boost = Sprint
##EVA_FreeLookToggle
                        ############################
######################### Ground Vehicle - General ###########################
                        ############################
##GV_ExitSeat = prone
##GV_Horn
##GV_CycleCameraView
#GV_ZoomIn3rdPersonView = (13, VJOY_3)
#GV_ZoomOut3rdPersonView = (14, VJOY_3)
##GV_LookLeftRight = <mouse>
##GV_LookUpDown = <mouse>
#GV_LookBehind = (15, VJOY_3)
##GV_FireWeaponGroup1
##GV_FireWeaponGroup2
##GV_FlightSystemsReady
##GV_OpenAllDoors
##GV_CloseAllDoors
##GV_LockAllDoors
##GV_UnlockAllDoors
##GV_Map
                        ############################
######################### Ground Vehicle - Movement###########################
                        ############################
AXIS_DriveForwardBackward = (AxisName.Z, VJOY_2)
##AXIS_TurnLeftRight = (AxisName.X, VJOY_2)
##GV_RollLeft
##GV_RollRight
##GV_Brake
##GV_PrimaryFire
##GV_SecondaryFire
##GV_DynamicZoomInOut
                        ############################
######################### Ground Vehicle - Gunner  ###########################
                        ############################
#GV_PrimaryFire
#GV_SecondaryFire
                        ############################
######################### Electronic Access - Spec.###########################
                        ############################
#SPEC_CameraTargetNext
#SPEC_CameraTargetPrev
#SPEC_CameraLockTarget
#SPEC_CameraZoomInOut
#SPEC_CameraZoomIn
#SPEC_CameraZoomOut
#SPEC_CameraRotateYaw
#SPEC_CameraRotatePitch
#SPEC_CameraHUDToggle
#SPEC_CameraModeNext
#SPEC_CameraModePrev
                        ############################
######################### Social - General         ###########################
                        ############################
#SOCIAL_Respawn
#SOCIAL_FOIPPushToTalk = Key("F4", 0x3e, False, win32con.VK_F4)
#SOCIAL_FOIPHeadTrackingToggle = Key("F4", 0x3e, False, win32con.VK_F4)
#SOCIAL_FOIPSelfieCam = Key("F4", 0x3e, False, win32con.VK_F4)
#SOCIAL_FOIPRecalibrate = Key("F4", 0x3e, False, win32con.VK_F4)
#SOCIAL_CommLinkAppToggle = Key("F4", 0x3e, False, win32con.VK_F4)
#SOCIAL_ChatWindowToggle = Key("F4", 0x3e, False, win32con.VK_F4)
#SOCIAL_ChatWindowFocus = Key("", 0x3e, False, win32con.VK_F4)
                        ############################
######################### Social - Invites         ###########################
                        ############################
#SOCIAL_AcceptInvite = Key("F4", 0x3e, False, win32con.VK_F4)
#SOCIAL_RejectInvite = Key("F4", 0x3e, False, win32con.VK_F4)
#SOCIAL_IgnoreInvite = Key("F4", 0x3e, False, win32con.VK_F4)
                        ############################
######################### Social - Emotes         ###########################
                        ############################
                        
                        ############################
######################### Interaction - All        ###########################
                        ############################
#InteractionMode
#ActivateInnerThought
#Focus
#DecreaseThrowPower
#InteractionModeZoomIn
#InteractionModeZoomOut
#MFDLeft
#MFDRight
#MFDUp
#MFDDown
#PersonalInnerThought
                        ############################
######################### Camera - Adv Controls    ###########################
                        ############################
#AdvancedCameraControlsModifier = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView1 = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView2 = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView3 = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView4 = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView5 = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView6 = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView7 = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView8 = Key("F4", 0x3e, False, win32con.VK_F4)
#SaveView9 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView1 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView2 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView3 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView4 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView5 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView6 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView7 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView8 = Key("F4", 0x3e, False, win32con.VK_F4)
#LoadView9 = Key("F4", 0x3e, False, win32con.VK_F4)
#ClearSavedView = Key("F4", 0x3e, False, win32con.VK_F4)
#XOffsetPositive = Key("F4", 0x3e, False, win32con.VK_F4)
#XOffsetNegative = Key("F4", 0x3e, False, win32con.VK_F4)
#YOffsetPositive = Key("F4", 0x3e, False, win32con.VK_F4)
#YOffsetNegative = Key("F4", 0x3e, False, win32con.VK_F4)
#ZOffsetPositive = Key("F4", 0x3e, False, win32con.VK_F4)
#ZOffsetNegative = Key("F4", 0x3e, False, win32con.VK_F4)
#IncreaseFoV
#DecreaseFoV
#IncreaseDoF
#DecreaseDoF
#ResetCurrentView
