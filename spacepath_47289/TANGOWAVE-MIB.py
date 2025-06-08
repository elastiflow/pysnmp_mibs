# SNMP MIB module (TANGOWAVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/spacepath_47289/TANGOWAVE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:01:22 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

tango = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47289)
)
if mibBuilder.loadTexts:
    tango.setRevisions(
        ("1997-04-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wave_ObjectIdentity = ObjectIdentity
wave = _Wave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1)
)
_Data_ObjectIdentity = ObjectIdentity
data = _Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1)
)
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1)
)
_HelloString_Type = DisplayString
_HelloString_Object = MibScalar
helloString = _HelloString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 1),
    _HelloString_Type()
)
helloString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    helloString.setStatus("current")
_ModelString_Type = DisplayString
_ModelString_Object = MibScalar
modelString = _ModelString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 2),
    _ModelString_Type()
)
modelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelString.setStatus("current")
_SerialString_Type = DisplayString
_SerialString_Object = MibScalar
serialString = _SerialString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 3),
    _SerialString_Type()
)
serialString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialString.setStatus("current")
_ControlState_Type = Integer32
_ControlState_Object = MibScalar
controlState = _ControlState_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 4),
    _ControlState_Type()
)
controlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlState.setStatus("current")
_ControlStateString_Type = DisplayString
_ControlStateString_Object = MibScalar
controlStateString = _ControlStateString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 5),
    _ControlStateString_Type()
)
controlStateString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlStateString.setStatus("current")
_LocalControl_Type = Integer32
_LocalControl_Object = MibScalar
localControl = _LocalControl_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 6),
    _LocalControl_Type()
)
localControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localControl.setStatus("current")
_FrontPanelDisplay_Type = Integer32
_FrontPanelDisplay_Object = MibScalar
frontPanelDisplay = _FrontPanelDisplay_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 7),
    _FrontPanelDisplay_Type()
)
frontPanelDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontPanelDisplay.setStatus("current")
_FrontPanelButtons_Type = Integer32
_FrontPanelButtons_Object = MibScalar
frontPanelButtons = _FrontPanelButtons_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 8),
    _FrontPanelButtons_Type()
)
frontPanelButtons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontPanelButtons.setStatus("current")
_CustomerRS485Term_Type = Integer32
_CustomerRS485Term_Object = MibScalar
customerRS485Term = _CustomerRS485Term_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 9),
    _CustomerRS485Term_Type()
)
customerRS485Term.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customerRS485Term.setStatus("current")
_SaveConfiguration_Type = Integer32
_SaveConfiguration_Object = MibScalar
saveConfiguration = _SaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 1, 10),
    _SaveConfiguration_Type()
)
saveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveConfiguration.setStatus("current")
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2)
)
_CmHwVersion_Type = Integer32
_CmHwVersion_Object = MibScalar
cmHwVersion = _CmHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2, 1),
    _CmHwVersion_Type()
)
cmHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHwVersion.setStatus("current")
_FmHwVersion_Type = Integer32
_FmHwVersion_Object = MibScalar
fmHwVersion = _FmHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2, 2),
    _FmHwVersion_Type()
)
fmHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHwVersion.setStatus("current")
_RfmHwVersion_Type = Integer32
_RfmHwVersion_Object = MibScalar
rfmHwVersion = _RfmHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2, 3),
    _RfmHwVersion_Type()
)
rfmHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfmHwVersion.setStatus("current")
_CmFwVersionString_Type = DisplayString
_CmFwVersionString_Object = MibScalar
cmFwVersionString = _CmFwVersionString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2, 4),
    _CmFwVersionString_Type()
)
cmFwVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFwVersionString.setStatus("current")
_FmFwVersionString_Type = DisplayString
_FmFwVersionString_Object = MibScalar
fmFwVersionString = _FmFwVersionString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2, 5),
    _FmFwVersionString_Type()
)
fmFwVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFwVersionString.setStatus("current")
_RfmFwVersionString_Type = DisplayString
_RfmFwVersionString_Object = MibScalar
rfmFwVersionString = _RfmFwVersionString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2, 6),
    _RfmFwVersionString_Type()
)
rfmFwVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfmFwVersionString.setStatus("current")
_FmBlVersionString_Type = DisplayString
_FmBlVersionString_Object = MibScalar
fmBlVersionString = _FmBlVersionString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2, 7),
    _FmBlVersionString_Type()
)
fmBlVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmBlVersionString.setStatus("current")
_RfmBlVersionString_Type = DisplayString
_RfmBlVersionString_Object = MibScalar
rfmBlVersionString = _RfmBlVersionString_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 2, 8),
    _RfmBlVersionString_Type()
)
rfmBlVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfmBlVersionString.setStatus("current")
_Twt_ObjectIdentity = ObjectIdentity
twt = _Twt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 3)
)
_TwtHeaterVoltageEf_Type = Integer32
_TwtHeaterVoltageEf_Object = MibScalar
twtHeaterVoltageEf = _TwtHeaterVoltageEf_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 3, 1),
    _TwtHeaterVoltageEf_Type()
)
twtHeaterVoltageEf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twtHeaterVoltageEf.setStatus("current")
_TwtHeaterCurrentIf_Type = Integer32
_TwtHeaterCurrentIf_Object = MibScalar
twtHeaterCurrentIf = _TwtHeaterCurrentIf_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 3, 2),
    _TwtHeaterCurrentIf_Type()
)
twtHeaterCurrentIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twtHeaterCurrentIf.setStatus("current")
_TwtHelixVoltageEw_Type = Integer32
_TwtHelixVoltageEw_Object = MibScalar
twtHelixVoltageEw = _TwtHelixVoltageEw_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 3, 3),
    _TwtHelixVoltageEw_Type()
)
twtHelixVoltageEw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twtHelixVoltageEw.setStatus("current")
_TwtHelixCurrentIw_Type = Integer32
_TwtHelixCurrentIw_Object = MibScalar
twtHelixCurrentIw = _TwtHelixCurrentIw_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 3, 4),
    _TwtHelixCurrentIw_Type()
)
twtHelixCurrentIw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twtHelixCurrentIw.setStatus("current")
_TwtAnodePos_Type = Integer32
_TwtAnodePos_Object = MibScalar
twtAnodePos = _TwtAnodePos_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 3, 5),
    _TwtAnodePos_Type()
)
twtAnodePos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twtAnodePos.setStatus("current")
_TwtAnodeNeg_Type = Integer32
_TwtAnodeNeg_Object = MibScalar
twtAnodeNeg = _TwtAnodeNeg_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 3, 6),
    _TwtAnodeNeg_Type()
)
twtAnodeNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twtAnodeNeg.setStatus("current")
_TwtTemperature_Type = Integer32
_TwtTemperature_Object = MibScalar
twtTemperature = _TwtTemperature_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 3, 7),
    _TwtTemperature_Type()
)
twtTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twtTemperature.setStatus("current")
_Cooling_ObjectIdentity = ObjectIdentity
cooling = _Cooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 4)
)
_CoolingFan1Speed_Type = Integer32
_CoolingFan1Speed_Object = MibScalar
coolingFan1Speed = _CoolingFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 4, 1),
    _CoolingFan1Speed_Type()
)
coolingFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFan1Speed.setStatus("current")
_CoolingFan2Speed_Type = Integer32
_CoolingFan2Speed_Object = MibScalar
coolingFan2Speed = _CoolingFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 4, 2),
    _CoolingFan2Speed_Type()
)
coolingFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFan2Speed.setStatus("current")
_CoolingFanVoltage_Type = Integer32
_CoolingFanVoltage_Object = MibScalar
coolingFanVoltage = _CoolingFanVoltage_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 4, 3),
    _CoolingFanVoltage_Type()
)
coolingFanVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanVoltage.setStatus("current")
_Rf_ObjectIdentity = ObjectIdentity
rf = _Rf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5)
)
_RfForwardPower_Type = Integer32
_RfForwardPower_Object = MibScalar
rfForwardPower = _RfForwardPower_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 1),
    _RfForwardPower_Type()
)
rfForwardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfForwardPower.setStatus("current")
_RfForwardPowerMinAlarm_Type = Integer32
_RfForwardPowerMinAlarm_Object = MibScalar
rfForwardPowerMinAlarm = _RfForwardPowerMinAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 2),
    _RfForwardPowerMinAlarm_Type()
)
rfForwardPowerMinAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfForwardPowerMinAlarm.setStatus("current")
_RfForwardPowerMinFault_Type = Integer32
_RfForwardPowerMinFault_Object = MibScalar
rfForwardPowerMinFault = _RfForwardPowerMinFault_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 3),
    _RfForwardPowerMinFault_Type()
)
rfForwardPowerMinFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfForwardPowerMinFault.setStatus("current")
_RfForwardPowerMaxAlarm_Type = Integer32
_RfForwardPowerMaxAlarm_Object = MibScalar
rfForwardPowerMaxAlarm = _RfForwardPowerMaxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 4),
    _RfForwardPowerMaxAlarm_Type()
)
rfForwardPowerMaxAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfForwardPowerMaxAlarm.setStatus("current")
_RfForwardPowerMaxFault_Type = Integer32
_RfForwardPowerMaxFault_Object = MibScalar
rfForwardPowerMaxFault = _RfForwardPowerMaxFault_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 5),
    _RfForwardPowerMaxFault_Type()
)
rfForwardPowerMaxFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfForwardPowerMaxFault.setStatus("current")
_RfReversePowerA_Type = Integer32
_RfReversePowerA_Object = MibScalar
rfReversePowerA = _RfReversePowerA_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 6),
    _RfReversePowerA_Type()
)
rfReversePowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfReversePowerA.setStatus("current")
_RfReversePowerB_Type = Integer32
_RfReversePowerB_Object = MibScalar
rfReversePowerB = _RfReversePowerB_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 7),
    _RfReversePowerB_Type()
)
rfReversePowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfReversePowerB.setStatus("current")
_RfAttenuator_Type = Integer32
_RfAttenuator_Object = MibScalar
rfAttenuator = _RfAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 8),
    _RfAttenuator_Type()
)
rfAttenuator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAttenuator.setStatus("current")
_RfAdjustGain_Type = Integer32
_RfAdjustGain_Object = MibScalar
rfAdjustGain = _RfAdjustGain_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 9),
    _RfAdjustGain_Type()
)
rfAdjustGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfAdjustGain.setStatus("current")
_RfForwardPowerOffset_Type = Integer32
_RfForwardPowerOffset_Object = MibScalar
rfForwardPowerOffset = _RfForwardPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 10),
    _RfForwardPowerOffset_Type()
)
rfForwardPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfForwardPowerOffset.setStatus("current")
_BeaconReceiverEnable_Type = Integer32
_BeaconReceiverEnable_Object = MibScalar
beaconReceiverEnable = _BeaconReceiverEnable_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 11),
    _BeaconReceiverEnable_Type()
)
beaconReceiverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconReceiverEnable.setStatus("current")
_BeaconReceiverVolt_Type = Integer32
_BeaconReceiverVolt_Object = MibScalar
beaconReceiverVolt = _BeaconReceiverVolt_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 12),
    _BeaconReceiverVolt_Type()
)
beaconReceiverVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconReceiverVolt.setStatus("current")
_BeaconReceiverVoltDelta_Type = Integer32
_BeaconReceiverVoltDelta_Object = MibScalar
beaconReceiverVoltDelta = _BeaconReceiverVoltDelta_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 13),
    _BeaconReceiverVoltDelta_Type()
)
beaconReceiverVoltDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconReceiverVoltDelta.setStatus("current")
_BeaconReceiverGain_Type = Integer32
_BeaconReceiverGain_Object = MibScalar
beaconReceiverGain = _BeaconReceiverGain_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 14),
    _BeaconReceiverGain_Type()
)
beaconReceiverGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconReceiverGain.setStatus("current")
_BeaconReceiverGradient_Type = Integer32
_BeaconReceiverGradient_Object = MibScalar
beaconReceiverGradient = _BeaconReceiverGradient_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 15),
    _BeaconReceiverGradient_Type()
)
beaconReceiverGradient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconReceiverGradient.setStatus("current")
_BucStatus_Type = DisplayString
_BucStatus_Object = MibScalar
bucStatus = _BucStatus_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 16),
    _BucStatus_Type()
)
bucStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bucStatus.setStatus("current")
_BucAttenuation_Type = Integer32
_BucAttenuation_Object = MibScalar
bucAttenuation = _BucAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 17),
    _BucAttenuation_Type()
)
bucAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bucAttenuation.setStatus("current")
_BucAdjustGain_Type = Integer32
_BucAdjustGain_Object = MibScalar
bucAdjustGain = _BucAdjustGain_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 5, 18),
    _BucAdjustGain_Type()
)
bucAdjustGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bucAdjustGain.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 6)
)
_Trapmsg1_Type = DisplayString
_Trapmsg1_Object = MibScalar
trapmsg1 = _Trapmsg1_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 6, 1),
    _Trapmsg1_Type()
)
trapmsg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapmsg1.setStatus("current")
_TrapFaultMsg_Type = DisplayString
_TrapFaultMsg_Object = MibScalar
trapFaultMsg = _TrapFaultMsg_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 6, 2),
    _TrapFaultMsg_Type()
)
trapFaultMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFaultMsg.setStatus("current")
_Red_ObjectIdentity = ObjectIdentity
red = _Red_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7)
)
_RedUnit_Type = DisplayString
_RedUnit_Object = MibScalar
redUnit = _RedUnit_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7, 1),
    _RedUnit_Type()
)
redUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redUnit.setStatus("current")
_RedControl_Type = DisplayString
_RedControl_Object = MibScalar
redControl = _RedControl_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7, 2),
    _RedControl_Type()
)
redControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redControl.setStatus("current")
_RedMode_Type = DisplayString
_RedMode_Object = MibScalar
redMode = _RedMode_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7, 3),
    _RedMode_Type()
)
redMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redMode.setStatus("current")
_RedSubMode_Type = DisplayString
_RedSubMode_Object = MibScalar
redSubMode = _RedSubMode_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7, 4),
    _RedSubMode_Type()
)
redSubMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redSubMode.setStatus("current")
_RedRS485Id_Type = DisplayString
_RedRS485Id_Object = MibScalar
redRS485Id = _RedRS485Id_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7, 5),
    _RedRS485Id_Type()
)
redRS485Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redRS485Id.setStatus("current")
_RedRS485Term_Type = Integer32
_RedRS485Term_Object = MibScalar
redRS485Term = _RedRS485Term_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7, 6),
    _RedRS485Term_Type()
)
redRS485Term.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redRS485Term.setStatus("current")
_RedRS485Enable_Type = Integer32
_RedRS485Enable_Object = MibScalar
redRS485Enable = _RedRS485Enable_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7, 7),
    _RedRS485Enable_Type()
)
redRS485Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redRS485Enable.setStatus("current")
_RedForceFault_Type = Integer32
_RedForceFault_Object = MibScalar
redForceFault = _RedForceFault_Object(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 7, 8),
    _RedForceFault_Type()
)
redForceFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redForceFault.setStatus("current")
_SnmpMIBConformance_ObjectIdentity = ObjectIdentity
snmpMIBConformance = _SnmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 2)
)
_SnmpMIBCompliances_ObjectIdentity = ObjectIdentity
snmpMIBCompliances = _SnmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 2, 1)
)
_SnmpMIBGroups_ObjectIdentity = ObjectIdentity
snmpMIBGroups = _SnmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47289, 2, 2)
)

# Managed Objects groups

controlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 8)
)
controlGroup.setObjects(
      *(("TANGOWAVE-MIB", "helloString"),
        ("TANGOWAVE-MIB", "modelString"),
        ("TANGOWAVE-MIB", "serialString"),
        ("TANGOWAVE-MIB", "controlState"),
        ("TANGOWAVE-MIB", "controlStateString"),
        ("TANGOWAVE-MIB", "localControl"),
        ("TANGOWAVE-MIB", "frontPanelDisplay"),
        ("TANGOWAVE-MIB", "frontPanelButtons"),
        ("TANGOWAVE-MIB", "customerRS485Term"),
        ("TANGOWAVE-MIB", "saveConfiguration"))
)
if mibBuilder.loadTexts:
    controlGroup.setStatus("current")

versionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 9)
)
versionGroup.setObjects(
      *(("TANGOWAVE-MIB", "cmHwVersion"),
        ("TANGOWAVE-MIB", "fmHwVersion"),
        ("TANGOWAVE-MIB", "rfmHwVersion"),
        ("TANGOWAVE-MIB", "cmFwVersionString"),
        ("TANGOWAVE-MIB", "fmFwVersionString"),
        ("TANGOWAVE-MIB", "rfmFwVersionString"),
        ("TANGOWAVE-MIB", "fmBlVersionString"),
        ("TANGOWAVE-MIB", "rfmBlVersionString"))
)
if mibBuilder.loadTexts:
    versionGroup.setStatus("current")

twtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 10)
)
twtGroup.setObjects(
      *(("TANGOWAVE-MIB", "twtHeaterVoltageEf"),
        ("TANGOWAVE-MIB", "twtHeaterCurrentIf"),
        ("TANGOWAVE-MIB", "twtHelixVoltageEw"),
        ("TANGOWAVE-MIB", "twtHelixCurrentIw"),
        ("TANGOWAVE-MIB", "twtAnodePos"),
        ("TANGOWAVE-MIB", "twtAnodeNeg"),
        ("TANGOWAVE-MIB", "twtTemperature"))
)
if mibBuilder.loadTexts:
    twtGroup.setStatus("current")

coolingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 11)
)
coolingGroup.setObjects(
      *(("TANGOWAVE-MIB", "coolingFan1Speed"),
        ("TANGOWAVE-MIB", "coolingFan2Speed"),
        ("TANGOWAVE-MIB", "coolingFanVoltage"))
)
if mibBuilder.loadTexts:
    coolingGroup.setStatus("current")

rfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 12)
)
rfGroup.setObjects(
      *(("TANGOWAVE-MIB", "rfForwardPower"),
        ("TANGOWAVE-MIB", "rfForwardPowerMinAlarm"),
        ("TANGOWAVE-MIB", "rfForwardPowerMinFault"),
        ("TANGOWAVE-MIB", "rfForwardPowerMaxAlarm"),
        ("TANGOWAVE-MIB", "rfForwardPowerMaxFault"),
        ("TANGOWAVE-MIB", "rfReversePowerA"),
        ("TANGOWAVE-MIB", "rfReversePowerB"),
        ("TANGOWAVE-MIB", "rfAttenuator"),
        ("TANGOWAVE-MIB", "rfAdjustGain"),
        ("TANGOWAVE-MIB", "rfForwardPowerOffset"),
        ("TANGOWAVE-MIB", "beaconReceiverEnable"),
        ("TANGOWAVE-MIB", "beaconReceiverVolt"),
        ("TANGOWAVE-MIB", "beaconReceiverVoltDelta"),
        ("TANGOWAVE-MIB", "beaconReceiverGain"),
        ("TANGOWAVE-MIB", "beaconReceiverGradient"),
        ("TANGOWAVE-MIB", "bucStatus"),
        ("TANGOWAVE-MIB", "bucAttenuation"),
        ("TANGOWAVE-MIB", "bucAdjustGain"))
)
if mibBuilder.loadTexts:
    rfGroup.setStatus("current")

trapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 13)
)
trapsGroup.setObjects(
      *(("TANGOWAVE-MIB", "trapmsg1"),
        ("TANGOWAVE-MIB", "trapFaultMsg"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus("current")

redGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47289, 1, 1, 14)
)
redGroup.setObjects(
      *(("TANGOWAVE-MIB", "redUnit"),
        ("TANGOWAVE-MIB", "redControl"),
        ("TANGOWAVE-MIB", "redMode"),
        ("TANGOWAVE-MIB", "redSubMode"),
        ("TANGOWAVE-MIB", "redRS485Id"),
        ("TANGOWAVE-MIB", "redRS485Term"),
        ("TANGOWAVE-MIB", "redRS485Enable"),
        ("TANGOWAVE-MIB", "redForceFault"))
)
if mibBuilder.loadTexts:
    redGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TANGOWAVE-MIB",
    **{"tango": tango,
       "wave": wave,
       "data": data,
       "control": control,
       "helloString": helloString,
       "modelString": modelString,
       "serialString": serialString,
       "controlState": controlState,
       "controlStateString": controlStateString,
       "localControl": localControl,
       "frontPanelDisplay": frontPanelDisplay,
       "frontPanelButtons": frontPanelButtons,
       "customerRS485Term": customerRS485Term,
       "saveConfiguration": saveConfiguration,
       "version": version,
       "cmHwVersion": cmHwVersion,
       "fmHwVersion": fmHwVersion,
       "rfmHwVersion": rfmHwVersion,
       "cmFwVersionString": cmFwVersionString,
       "fmFwVersionString": fmFwVersionString,
       "rfmFwVersionString": rfmFwVersionString,
       "fmBlVersionString": fmBlVersionString,
       "rfmBlVersionString": rfmBlVersionString,
       "twt": twt,
       "twtHeaterVoltageEf": twtHeaterVoltageEf,
       "twtHeaterCurrentIf": twtHeaterCurrentIf,
       "twtHelixVoltageEw": twtHelixVoltageEw,
       "twtHelixCurrentIw": twtHelixCurrentIw,
       "twtAnodePos": twtAnodePos,
       "twtAnodeNeg": twtAnodeNeg,
       "twtTemperature": twtTemperature,
       "cooling": cooling,
       "coolingFan1Speed": coolingFan1Speed,
       "coolingFan2Speed": coolingFan2Speed,
       "coolingFanVoltage": coolingFanVoltage,
       "rf": rf,
       "rfForwardPower": rfForwardPower,
       "rfForwardPowerMinAlarm": rfForwardPowerMinAlarm,
       "rfForwardPowerMinFault": rfForwardPowerMinFault,
       "rfForwardPowerMaxAlarm": rfForwardPowerMaxAlarm,
       "rfForwardPowerMaxFault": rfForwardPowerMaxFault,
       "rfReversePowerA": rfReversePowerA,
       "rfReversePowerB": rfReversePowerB,
       "rfAttenuator": rfAttenuator,
       "rfAdjustGain": rfAdjustGain,
       "rfForwardPowerOffset": rfForwardPowerOffset,
       "beaconReceiverEnable": beaconReceiverEnable,
       "beaconReceiverVolt": beaconReceiverVolt,
       "beaconReceiverVoltDelta": beaconReceiverVoltDelta,
       "beaconReceiverGain": beaconReceiverGain,
       "beaconReceiverGradient": beaconReceiverGradient,
       "bucStatus": bucStatus,
       "bucAttenuation": bucAttenuation,
       "bucAdjustGain": bucAdjustGain,
       "traps": traps,
       "trapmsg1": trapmsg1,
       "trapFaultMsg": trapFaultMsg,
       "red": red,
       "redUnit": redUnit,
       "redControl": redControl,
       "redMode": redMode,
       "redSubMode": redSubMode,
       "redRS485Id": redRS485Id,
       "redRS485Term": redRS485Term,
       "redRS485Enable": redRS485Enable,
       "redForceFault": redForceFault,
       "controlGroup": controlGroup,
       "versionGroup": versionGroup,
       "twtGroup": twtGroup,
       "coolingGroup": coolingGroup,
       "rfGroup": rfGroup,
       "trapsGroup": trapsGroup,
       "redGroup": redGroup,
       "snmpMIBConformance": snmpMIBConformance,
       "snmpMIBCompliances": snmpMIBCompliances,
       "snmpMIBGroups": snmpMIBGroups}
)
