# SNMP MIB module (NQMSFIBER-VARIABLES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exfo_6718/NQMSFIBER-VARIABLES-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:54:13 2025
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

(exfoModules,) = mibBuilder.importSymbols(
    "EXFO-SMI-REG",
    "exfoModules")

(nqmsFiber,) = mibBuilder.importSymbols(
    "NQMSFIBER-MIB",
    "nqmsFiber")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

nqmsFiberVariablesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NqmsFiberTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("break", 0),
          ("degradation", 1),
          ("manualcleared", 2),
          ("systemcleared", 3))
    )



# MIB Managed Objects in the order of their OIDs

_VariableList_ObjectIdentity = ObjectIdentity
variableList = _VariableList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1)
)
if mibBuilder.loadTexts:
    variableList.setStatus("current")
_MeasurementType_ObjectIdentity = ObjectIdentity
measurementType = _MeasurementType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    measurementType.setStatus("current")
_MessageIdentifier_Type = Unsigned32
_MessageIdentifier_Object = MibScalar
messageIdentifier = _MessageIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 1),
    _MessageIdentifier_Type()
)
messageIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    messageIdentifier.setStatus("current")
_FaultIdentifier_Type = Unsigned32
_FaultIdentifier_Object = MibScalar
faultIdentifier = _FaultIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 2),
    _FaultIdentifier_Type()
)
faultIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultIdentifier.setStatus("current")
_FaultDescription_Type = OctetString
_FaultDescription_Object = MibScalar
faultDescription = _FaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 3),
    _FaultDescription_Type()
)
faultDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultDescription.setStatus("current")
_FaultType_Type = NqmsFiberTC
_FaultType_Object = MibScalar
faultType = _FaultType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 4),
    _FaultType_Type()
)
faultType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultType.setStatus("current")
_Level_Type = Integer32
_Level_Object = MibScalar
level = _Level_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 5),
    _Level_Type()
)
level.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    level.setStatus("current")
if mibBuilder.loadTexts:
    level.setUnits("dB")
_RtuName_Type = OctetString
_RtuName_Object = MibScalar
rtuName = _RtuName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 6),
    _RtuName_Type()
)
rtuName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtuName.setStatus("current")
_RtuOpticalSwitchPort_Type = Unsigned32
_RtuOpticalSwitchPort_Object = MibScalar
rtuOpticalSwitchPort = _RtuOpticalSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 7),
    _RtuOpticalSwitchPort_Type()
)
rtuOpticalSwitchPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtuOpticalSwitchPort.setStatus("current")
_FaultDistanceEstimated_Type = Unsigned32
_FaultDistanceEstimated_Object = MibScalar
faultDistanceEstimated = _FaultDistanceEstimated_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 8),
    _FaultDistanceEstimated_Type()
)
faultDistanceEstimated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultDistanceEstimated.setStatus("current")
if mibBuilder.loadTexts:
    faultDistanceEstimated.setUnits("meter")
_FaultDistanceMin_Type = Unsigned32
_FaultDistanceMin_Object = MibScalar
faultDistanceMin = _FaultDistanceMin_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 9),
    _FaultDistanceMin_Type()
)
faultDistanceMin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultDistanceMin.setStatus("current")
if mibBuilder.loadTexts:
    faultDistanceMin.setUnits("meter")
_FaultDistanceMax_Type = Unsigned32
_FaultDistanceMax_Object = MibScalar
faultDistanceMax = _FaultDistanceMax_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 10),
    _FaultDistanceMax_Type()
)
faultDistanceMax.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultDistanceMax.setStatus("current")
if mibBuilder.loadTexts:
    faultDistanceMax.setUnits("meter")
_RemoteSwitchNumber_Type = Unsigned32
_RemoteSwitchNumber_Object = MibScalar
remoteSwitchNumber = _RemoteSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 11),
    _RemoteSwitchNumber_Type()
)
remoteSwitchNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    remoteSwitchNumber.setStatus("current")
_RemoteSwitchPort_Type = Unsigned32
_RemoteSwitchPort_Object = MibScalar
remoteSwitchPort = _RemoteSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 12),
    _RemoteSwitchPort_Type()
)
remoteSwitchPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    remoteSwitchPort.setStatus("current")
_FaultDistanceToRS_Type = Unsigned32
_FaultDistanceToRS_Object = MibScalar
faultDistanceToRS = _FaultDistanceToRS_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 13),
    _FaultDistanceToRS_Type()
)
faultDistanceToRS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultDistanceToRS.setStatus("current")
if mibBuilder.loadTexts:
    faultDistanceToRS.setUnits("meter")
_OpticalRouteNumber_Type = Unsigned32
_OpticalRouteNumber_Object = MibScalar
opticalRouteNumber = _OpticalRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 14),
    _OpticalRouteNumber_Type()
)
opticalRouteNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    opticalRouteNumber.setStatus("current")
_OpticalRouteGISReference_Type = Unsigned32
_OpticalRouteGISReference_Object = MibScalar
opticalRouteGISReference = _OpticalRouteGISReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 15),
    _OpticalRouteGISReference_Type()
)
opticalRouteGISReference.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    opticalRouteGISReference.setStatus("current")
_DefaultIORValue_Type = OctetString
_DefaultIORValue_Object = MibScalar
defaultIORValue = _DefaultIORValue_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 16),
    _DefaultIORValue_Type()
)
defaultIORValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    defaultIORValue.setStatus("current")
if mibBuilder.loadTexts:
    defaultIORValue.setUnits("IOR metrics")
_DefaultHelixFactorValue_Type = OctetString
_DefaultHelixFactorValue_Object = MibScalar
defaultHelixFactorValue = _DefaultHelixFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 1, 17),
    _DefaultHelixFactorValue_Type()
)
defaultHelixFactorValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    defaultHelixFactorValue.setStatus("current")
if mibBuilder.loadTexts:
    defaultHelixFactorValue.setUnits("percent")
_SystemType_ObjectIdentity = ObjectIdentity
systemType = _SystemType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    systemType.setStatus("current")
_FreeDiskSpaceSystem_Type = OctetString
_FreeDiskSpaceSystem_Object = MibScalar
freeDiskSpaceSystem = _FreeDiskSpaceSystem_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 2, 1),
    _FreeDiskSpaceSystem_Type()
)
freeDiskSpaceSystem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    freeDiskSpaceSystem.setStatus("current")
if mibBuilder.loadTexts:
    freeDiskSpaceSystem.setUnits("kByte")
_SystemUptime_Type = TimeInterval
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 2, 2),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_NqmsFiberFaultType_ObjectIdentity = ObjectIdentity
nqmsFiberFaultType = _NqmsFiberFaultType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    nqmsFiberFaultType.setStatus("current")
_AlertTime_Type = OctetString
_AlertTime_Object = MibScalar
alertTime = _AlertTime_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 1),
    _AlertTime_Type()
)
alertTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertTime.setStatus("current")
_AlertType_Type = OctetString
_AlertType_Object = MibScalar
alertType = _AlertType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 2),
    _AlertType_Type()
)
alertType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertType.setStatus("current")
_AlertProvider_Type = OctetString
_AlertProvider_Object = MibScalar
alertProvider = _AlertProvider_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 3),
    _AlertProvider_Type()
)
alertProvider.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertProvider.setStatus("current")
_AlertRecipient_Type = OctetString
_AlertRecipient_Object = MibScalar
alertRecipient = _AlertRecipient_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 4),
    _AlertRecipient_Type()
)
alertRecipient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertRecipient.setStatus("current")
_AlertDeliveryAddress_Type = OctetString
_AlertDeliveryAddress_Object = MibScalar
alertDeliveryAddress = _AlertDeliveryAddress_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 5),
    _AlertDeliveryAddress_Type()
)
alertDeliveryAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertDeliveryAddress.setStatus("current")
_AlarmId_Type = Unsigned32
_AlarmId_Object = MibScalar
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 6),
    _AlarmId_Type()
)
alarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")
_AlarmType_Type = OctetString
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 7),
    _AlarmType_Type()
)
alarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_AlarmTime_Type = OctetString
_AlarmTime_Object = MibScalar
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 8),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_AlarmSeverity_Type = OctetString
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 9),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
if mibBuilder.loadTexts:
    alarmSeverity.setUnits("meter")
_AlarmState_Type = OctetString
_AlarmState_Object = MibScalar
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 10),
    _AlarmState_Type()
)
alarmState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmState.setStatus("current")
_AlarmEvent_Type = OctetString
_AlarmEvent_Object = MibScalar
alarmEvent = _AlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 11),
    _AlarmEvent_Type()
)
alarmEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmEvent.setStatus("current")
_AlarmEventTime_Type = OctetString
_AlarmEventTime_Object = MibScalar
alarmEventTime = _AlarmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 12),
    _AlarmEventTime_Type()
)
alarmEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmEventTime.setStatus("current")
_FaultStatus_Type = OctetString
_FaultStatus_Object = MibScalar
faultStatus = _FaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 13),
    _FaultStatus_Type()
)
faultStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultStatus.setStatus("current")
_FaultConfirmations_Type = Integer32
_FaultConfirmations_Object = MibScalar
faultConfirmations = _FaultConfirmations_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 14),
    _FaultConfirmations_Type()
)
faultConfirmations.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultConfirmations.setStatus("current")
_FaultPositionKM_Type = OctetString
_FaultPositionKM_Object = MibScalar
faultPositionKM = _FaultPositionKM_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 15),
    _FaultPositionKM_Type()
)
faultPositionKM.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultPositionKM.setStatus("current")
if mibBuilder.loadTexts:
    faultPositionKM.setUnits("KM")
_FaultMaximumPositionKm_Type = OctetString
_FaultMaximumPositionKm_Object = MibScalar
faultMaximumPositionKm = _FaultMaximumPositionKm_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 16),
    _FaultMaximumPositionKm_Type()
)
faultMaximumPositionKm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultMaximumPositionKm.setStatus("current")
if mibBuilder.loadTexts:
    faultMaximumPositionKm.setUnits("KM")
_FaultMinimumPositionKM_Type = OctetString
_FaultMinimumPositionKM_Object = MibScalar
faultMinimumPositionKM = _FaultMinimumPositionKM_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 17),
    _FaultMinimumPositionKM_Type()
)
faultMinimumPositionKM.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultMinimumPositionKM.setStatus("current")
if mibBuilder.loadTexts:
    faultMinimumPositionKM.setUnits("KM")
_FaultLoss_Type = OctetString
_FaultLoss_Object = MibScalar
faultLoss = _FaultLoss_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 18),
    _FaultLoss_Type()
)
faultLoss.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultLoss.setStatus("current")
_FaultThresholdType_Type = OctetString
_FaultThresholdType_Object = MibScalar
faultThresholdType = _FaultThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 19),
    _FaultThresholdType_Type()
)
faultThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultThresholdType.setStatus("current")
_FaultThresholdValueDB_Type = OctetString
_FaultThresholdValueDB_Object = MibScalar
faultThresholdValueDB = _FaultThresholdValueDB_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 20),
    _FaultThresholdValueDB_Type()
)
faultThresholdValueDB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultThresholdValueDB.setStatus("current")
if mibBuilder.loadTexts:
    faultThresholdValueDB.setUnits("dB")
_FaultAppliedThresholdDB_Type = OctetString
_FaultAppliedThresholdDB_Object = MibScalar
faultAppliedThresholdDB = _FaultAppliedThresholdDB_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 21),
    _FaultAppliedThresholdDB_Type()
)
faultAppliedThresholdDB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultAppliedThresholdDB.setStatus("current")
if mibBuilder.loadTexts:
    faultAppliedThresholdDB.setUnits("dB")
_FaultEventTime_Type = OctetString
_FaultEventTime_Object = MibScalar
faultEventTime = _FaultEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 22),
    _FaultEventTime_Type()
)
faultEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faultEventTime.setStatus("current")
_RtuSiteName_Type = OctetString
_RtuSiteName_Object = MibScalar
rtuSiteName = _RtuSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 23),
    _RtuSiteName_Type()
)
rtuSiteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtuSiteName.setStatus("current")
_OtdrSerialNumber_Type = OctetString
_OtdrSerialNumber_Object = MibScalar
otdrSerialNumber = _OtdrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 24),
    _OtdrSerialNumber_Type()
)
otdrSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    otdrSerialNumber.setStatus("current")
_OthSerialNumber_Type = OctetString
_OthSerialNumber_Object = MibScalar
othSerialNumber = _OthSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 25),
    _OthSerialNumber_Type()
)
othSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    othSerialNumber.setStatus("current")
_OtauPort_Type = Unsigned32
_OtauPort_Object = MibScalar
otauPort = _OtauPort_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 26),
    _OtauPort_Type()
)
otauPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    otauPort.setStatus("current")
_RotauPort_Type = Unsigned32
_RotauPort_Object = MibScalar
rotauPort = _RotauPort_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 27),
    _RotauPort_Type()
)
rotauPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rotauPort.setStatus("current")
_OpticalRouteName_Type = OctetString
_OpticalRouteName_Object = MibScalar
opticalRouteName = _OpticalRouteName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 28),
    _OpticalRouteName_Type()
)
opticalRouteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    opticalRouteName.setStatus("current")
_CableTemplateName_Type = OctetString
_CableTemplateName_Object = MibScalar
cableTemplateName = _CableTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 29),
    _CableTemplateName_Type()
)
cableTemplateName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cableTemplateName.setStatus("current")
_OspRouteId_Type = Integer32
_OspRouteId_Object = MibScalar
ospRouteId = _OspRouteId_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 30),
    _OspRouteId_Type()
)
ospRouteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospRouteId.setStatus("current")
_ExternalNMSrouteref1_Type = OctetString
_ExternalNMSrouteref1_Object = MibScalar
externalNMSrouteref1 = _ExternalNMSrouteref1_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 31),
    _ExternalNMSrouteref1_Type()
)
externalNMSrouteref1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalNMSrouteref1.setStatus("current")
_ExternalNMSrouteref2_Type = OctetString
_ExternalNMSrouteref2_Object = MibScalar
externalNMSrouteref2 = _ExternalNMSrouteref2_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 32),
    _ExternalNMSrouteref2_Type()
)
externalNMSrouteref2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalNMSrouteref2.setStatus("current")
_FiberCode_Type = OctetString
_FiberCode_Object = MibScalar
fiberCode = _FiberCode_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 33),
    _FiberCode_Type()
)
fiberCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fiberCode.setStatus("current")
_TestSetupName_Type = OctetString
_TestSetupName_Object = MibScalar
testSetupName = _TestSetupName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 34),
    _TestSetupName_Type()
)
testSetupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    testSetupName.setStatus("current")
_TestSetupType_Type = OctetString
_TestSetupType_Object = MibScalar
testSetupType = _TestSetupType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 35),
    _TestSetupType_Type()
)
testSetupType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    testSetupType.setStatus("current")
_TestSetupWavelength_Type = Integer32
_TestSetupWavelength_Object = MibScalar
testSetupWavelength = _TestSetupWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 36),
    _TestSetupWavelength_Type()
)
testSetupWavelength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    testSetupWavelength.setStatus("current")
if mibBuilder.loadTexts:
    testSetupWavelength.setUnits("nm")
_NearestSite_Type = OctetString
_NearestSite_Object = MibScalar
nearestSite = _NearestSite_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 37),
    _NearestSite_Type()
)
nearestSite.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nearestSite.setStatus("current")
_DistanceFromNearestSiteKM_Type = OctetString
_DistanceFromNearestSiteKM_Object = MibScalar
distanceFromNearestSiteKM = _DistanceFromNearestSiteKM_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 38),
    _DistanceFromNearestSiteKM_Type()
)
distanceFromNearestSiteKM.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    distanceFromNearestSiteKM.setStatus("current")
if mibBuilder.loadTexts:
    distanceFromNearestSiteKM.setUnits("KM")
_AffectedClient_Type = OctetString
_AffectedClient_Object = MibScalar
affectedClient = _AffectedClient_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 39),
    _AffectedClient_Type()
)
affectedClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    affectedClient.setStatus("current")
_Assignee_Type = OctetString
_Assignee_Object = MibScalar
assignee = _Assignee_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 40),
    _Assignee_Type()
)
assignee.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    assignee.setStatus("current")
_TroubleTicketDescription_Type = OctetString
_TroubleTicketDescription_Object = MibScalar
troubleTicketDescription = _TroubleTicketDescription_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 3, 41),
    _TroubleTicketDescription_Type()
)
troubleTicketDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    troubleTicketDescription.setStatus("current")
_NqmsFiberRtuStatusType_ObjectIdentity = ObjectIdentity
nqmsFiberRtuStatusType = _NqmsFiberRtuStatusType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    nqmsFiberRtuStatusType.setStatus("current")
_SourceDataSet_Type = OctetString
_SourceDataSet_Object = MibScalar
sourceDataSet = _SourceDataSet_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 1),
    _SourceDataSet_Type()
)
sourceDataSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sourceDataSet.setStatus("current")
_PrimaryAlarmSource_Type = OctetString
_PrimaryAlarmSource_Object = MibScalar
primaryAlarmSource = _PrimaryAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 2),
    _PrimaryAlarmSource_Type()
)
primaryAlarmSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    primaryAlarmSource.setStatus("current")
_AlarmStatus_Type = OctetString
_AlarmStatus_Object = MibScalar
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 3),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("current")
_SecondaryAlarmSource_Type = OctetString
_SecondaryAlarmSource_Object = MibScalar
secondaryAlarmSource = _SecondaryAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 4),
    _SecondaryAlarmSource_Type()
)
secondaryAlarmSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    secondaryAlarmSource.setStatus("current")
_AlarmDetails_Type = OctetString
_AlarmDetails_Object = MibScalar
alarmDetails = _AlarmDetails_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5),
    _AlarmDetails_Type()
)
alarmDetails.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmDetails.setStatus("current")
_AvailableMemory_Type = OctetString
_AvailableMemory_Object = MibScalar
availableMemory = _AvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 1),
    _AvailableMemory_Type()
)
availableMemory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    availableMemory.setStatus("current")
if mibBuilder.loadTexts:
    availableMemory.setUnits("MB")
_Uptime_Type = TimeInterval
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 2),
    _Uptime_Type()
)
uptime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    uptime.setStatus("current")
if mibBuilder.loadTexts:
    uptime.setUnits("secs")
_Status_Type = OctetString
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 3),
    _Status_Type()
)
status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    status.setStatus("current")
_ProcessorLoad_Type = OctetString
_ProcessorLoad_Object = MibScalar
processorLoad = _ProcessorLoad_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 4),
    _ProcessorLoad_Type()
)
processorLoad.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    processorLoad.setStatus("current")
if mibBuilder.loadTexts:
    processorLoad.setUnits("%")
_EmsName_Type = OctetString
_EmsName_Object = MibScalar
emsName = _EmsName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 5),
    _EmsName_Type()
)
emsName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    emsName.setStatus("current")
_HostName_Type = OctetString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 6),
    _HostName_Type()
)
hostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_RaidStatus_Type = OctetString
_RaidStatus_Object = MibScalar
raidStatus = _RaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 7),
    _RaidStatus_Type()
)
raidStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    raidStatus.setStatus("current")
_LastSynchronizationStatus_Type = OctetString
_LastSynchronizationStatus_Object = MibScalar
lastSynchronizationStatus = _LastSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 8),
    _LastSynchronizationStatus_Type()
)
lastSynchronizationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lastSynchronizationStatus.setStatus("current")
_HardwareKey_Type = OctetString
_HardwareKey_Object = MibScalar
hardwareKey = _HardwareKey_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 9),
    _HardwareKey_Type()
)
hardwareKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hardwareKey.setStatus("current")
_RtuStatus_Type = OctetString
_RtuStatus_Object = MibScalar
rtuStatus = _RtuStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 10),
    _RtuStatus_Type()
)
rtuStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtuStatus.setStatus("current")
_UpsStatus_Type = OctetString
_UpsStatus_Object = MibScalar
upsStatus = _UpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 11),
    _UpsStatus_Type()
)
upsStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    upsStatus.setStatus("current")
_ErrorLogCount_Type = Integer32
_ErrorLogCount_Object = MibScalar
errorLogCount = _ErrorLogCount_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 12),
    _ErrorLogCount_Type()
)
errorLogCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorLogCount.setStatus("current")
_WarningLogCount_Type = Integer32
_WarningLogCount_Object = MibScalar
warningLogCount = _WarningLogCount_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 13),
    _WarningLogCount_Type()
)
warningLogCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    warningLogCount.setStatus("current")
_MessageCategory_Type = OctetString
_MessageCategory_Object = MibScalar
messageCategory = _MessageCategory_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 14),
    _MessageCategory_Type()
)
messageCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    messageCategory.setStatus("current")
_MessageData_Type = OctetString
_MessageData_Object = MibScalar
messageData = _MessageData_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 15),
    _MessageData_Type()
)
messageData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    messageData.setStatus("current")
_FreeDiskSpaceDatabase_Type = OctetString
_FreeDiskSpaceDatabase_Object = MibScalar
freeDiskSpaceDatabase = _FreeDiskSpaceDatabase_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 16),
    _FreeDiskSpaceDatabase_Type()
)
freeDiskSpaceDatabase.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    freeDiskSpaceDatabase.setStatus("current")
if mibBuilder.loadTexts:
    freeDiskSpaceDatabase.setUnits("dB")
_FreeDiskSpaceBackup_Type = OctetString
_FreeDiskSpaceBackup_Object = MibScalar
freeDiskSpaceBackup = _FreeDiskSpaceBackup_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 4, 5, 17),
    _FreeDiskSpaceBackup_Type()
)
freeDiskSpaceBackup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    freeDiskSpaceBackup.setStatus("current")
if mibBuilder.loadTexts:
    freeDiskSpaceBackup.setUnits("dB")
_NqmsfiberStatusType_ObjectIdentity = ObjectIdentity
nqmsfiberStatusType = _NqmsfiberStatusType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    nqmsfiberStatusType.setStatus("current")
_NqmsFiberRtuLogType_ObjectIdentity = ObjectIdentity
nqmsFiberRtuLogType = _NqmsFiberRtuLogType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    nqmsFiberRtuLogType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NQMSFIBER-VARIABLES-MIB",
    **{"NqmsFiberTC": NqmsFiberTC,
       "nqmsFiberVariablesMib": nqmsFiberVariablesMib,
       "variableList": variableList,
       "measurementType": measurementType,
       "messageIdentifier": messageIdentifier,
       "faultIdentifier": faultIdentifier,
       "faultDescription": faultDescription,
       "faultType": faultType,
       "level": level,
       "rtuName": rtuName,
       "rtuOpticalSwitchPort": rtuOpticalSwitchPort,
       "faultDistanceEstimated": faultDistanceEstimated,
       "faultDistanceMin": faultDistanceMin,
       "faultDistanceMax": faultDistanceMax,
       "remoteSwitchNumber": remoteSwitchNumber,
       "remoteSwitchPort": remoteSwitchPort,
       "faultDistanceToRS": faultDistanceToRS,
       "opticalRouteNumber": opticalRouteNumber,
       "opticalRouteGISReference": opticalRouteGISReference,
       "defaultIORValue": defaultIORValue,
       "defaultHelixFactorValue": defaultHelixFactorValue,
       "systemType": systemType,
       "freeDiskSpaceSystem": freeDiskSpaceSystem,
       "systemUptime": systemUptime,
       "nqmsFiberFaultType": nqmsFiberFaultType,
       "alertTime": alertTime,
       "alertType": alertType,
       "alertProvider": alertProvider,
       "alertRecipient": alertRecipient,
       "alertDeliveryAddress": alertDeliveryAddress,
       "alarmId": alarmId,
       "alarmType": alarmType,
       "alarmTime": alarmTime,
       "alarmSeverity": alarmSeverity,
       "alarmState": alarmState,
       "alarmEvent": alarmEvent,
       "alarmEventTime": alarmEventTime,
       "faultStatus": faultStatus,
       "faultConfirmations": faultConfirmations,
       "faultPositionKM": faultPositionKM,
       "faultMaximumPositionKm": faultMaximumPositionKm,
       "faultMinimumPositionKM": faultMinimumPositionKM,
       "faultLoss": faultLoss,
       "faultThresholdType": faultThresholdType,
       "faultThresholdValueDB": faultThresholdValueDB,
       "faultAppliedThresholdDB": faultAppliedThresholdDB,
       "faultEventTime": faultEventTime,
       "rtuSiteName": rtuSiteName,
       "otdrSerialNumber": otdrSerialNumber,
       "othSerialNumber": othSerialNumber,
       "otauPort": otauPort,
       "rotauPort": rotauPort,
       "opticalRouteName": opticalRouteName,
       "cableTemplateName": cableTemplateName,
       "ospRouteId": ospRouteId,
       "externalNMSrouteref1": externalNMSrouteref1,
       "externalNMSrouteref2": externalNMSrouteref2,
       "fiberCode": fiberCode,
       "testSetupName": testSetupName,
       "testSetupType": testSetupType,
       "testSetupWavelength": testSetupWavelength,
       "nearestSite": nearestSite,
       "distanceFromNearestSiteKM": distanceFromNearestSiteKM,
       "affectedClient": affectedClient,
       "assignee": assignee,
       "troubleTicketDescription": troubleTicketDescription,
       "nqmsFiberRtuStatusType": nqmsFiberRtuStatusType,
       "sourceDataSet": sourceDataSet,
       "primaryAlarmSource": primaryAlarmSource,
       "alarmStatus": alarmStatus,
       "secondaryAlarmSource": secondaryAlarmSource,
       "alarmDetails": alarmDetails,
       "availableMemory": availableMemory,
       "uptime": uptime,
       "status": status,
       "processorLoad": processorLoad,
       "emsName": emsName,
       "hostName": hostName,
       "raidStatus": raidStatus,
       "lastSynchronizationStatus": lastSynchronizationStatus,
       "hardwareKey": hardwareKey,
       "rtuStatus": rtuStatus,
       "upsStatus": upsStatus,
       "errorLogCount": errorLogCount,
       "warningLogCount": warningLogCount,
       "messageCategory": messageCategory,
       "messageData": messageData,
       "freeDiskSpaceDatabase": freeDiskSpaceDatabase,
       "freeDiskSpaceBackup": freeDiskSpaceBackup,
       "nqmsfiberStatusType": nqmsfiberStatusType,
       "nqmsFiberRtuLogType": nqmsFiberRtuLogType}
)
