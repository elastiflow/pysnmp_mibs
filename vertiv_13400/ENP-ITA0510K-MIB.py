# SNMP MIB module (ENP-ITA0510K-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_13400/ENP-ITA0510K-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:06:02 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ita0510kMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("informational", 0),
          ("warning", 1),
          ("critical", 2))
    )



class StatusChange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 0),
          ("deactivated", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Enp_ObjectIdentity = ObjectIdentity
enp = _Enp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2)
)
_Ident_ObjectIdentity = ObjectIdentity
ident = _Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 1)
)
_IdentManufacturer_Type = DisplayString
_IdentManufacturer_Object = MibScalar
identManufacturer = _IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 1, 1),
    _IdentManufacturer_Type()
)
identManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identManufacturer.setStatus("current")
_IdentModel_Type = DisplayString
_IdentModel_Object = MibScalar
identModel = _IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 1, 2),
    _IdentModel_Type()
)
identModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identModel.setStatus("current")
_IdentIndex_Type = Integer32
_IdentIndex_Object = MibScalar
identIndex = _IdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 1, 3),
    _IdentIndex_Type()
)
identIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIndex.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 1)
)
_SystemStatus_Type = Status
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 1, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 2)
)
_InputPhaseVoltageA_Type = Integer32
_InputPhaseVoltageA_Object = MibScalar
inputPhaseVoltageA = _InputPhaseVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 2, 1),
    _InputPhaseVoltageA_Type()
)
inputPhaseVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseVoltageA.setStatus("current")
_InputPhaseVoltageB_Type = Integer32
_InputPhaseVoltageB_Object = MibScalar
inputPhaseVoltageB = _InputPhaseVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 2, 2),
    _InputPhaseVoltageB_Type()
)
inputPhaseVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseVoltageB.setStatus("current")
_InputPhaseVoltageC_Type = Integer32
_InputPhaseVoltageC_Object = MibScalar
inputPhaseVoltageC = _InputPhaseVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 2, 3),
    _InputPhaseVoltageC_Type()
)
inputPhaseVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseVoltageC.setStatus("current")
_InputFrequency_Type = Integer32
_InputFrequency_Object = MibScalar
inputFrequency = _InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 2, 4),
    _InputFrequency_Type()
)
inputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputFrequency.setStatus("current")
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 3)
)
_OutputVoltage_Type = Integer32
_OutputVoltage_Object = MibScalar
outputVoltage = _OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 3, 1),
    _OutputVoltage_Type()
)
outputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltage.setStatus("current")
_OutputCurrent_Type = Integer32
_OutputCurrent_Object = MibScalar
outputCurrent = _OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 3, 2),
    _OutputCurrent_Type()
)
outputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrent.setStatus("current")
_OutputFrequency_Type = Integer32
_OutputFrequency_Object = MibScalar
outputFrequency = _OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 3, 3),
    _OutputFrequency_Type()
)
outputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputFrequency.setStatus("current")
_OutputActivePower_Type = Integer32
_OutputActivePower_Object = MibScalar
outputActivePower = _OutputActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 3, 4),
    _OutputActivePower_Type()
)
outputActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputActivePower.setStatus("current")
_OutputApparentPower_Type = Integer32
_OutputApparentPower_Object = MibScalar
outputApparentPower = _OutputApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 3, 5),
    _OutputApparentPower_Type()
)
outputApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputApparentPower.setStatus("current")
_OutputLoad_Type = Integer32
_OutputLoad_Object = MibScalar
outputLoad = _OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 3, 6),
    _OutputLoad_Type()
)
outputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputLoad.setStatus("current")
_Bypass_ObjectIdentity = ObjectIdentity
bypass = _Bypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 4)
)
_BypassVoltage_Type = Integer32
_BypassVoltage_Object = MibScalar
bypassVoltage = _BypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 4, 1),
    _BypassVoltage_Type()
)
bypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassVoltage.setStatus("current")
_BypassCurrent_Type = Integer32
_BypassCurrent_Object = MibScalar
bypassCurrent = _BypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 4, 2),
    _BypassCurrent_Type()
)
bypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassCurrent.setStatus("current")
_BypassFrequency_Type = Integer32
_BypassFrequency_Object = MibScalar
bypassFrequency = _BypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 4, 3),
    _BypassFrequency_Type()
)
bypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassFrequency.setStatus("current")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 5)
)
_BatteryVoltage_Type = Integer32
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 5, 1),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")
_BatteryRemainsTime_Type = Integer32
_BatteryRemainsTime_Object = MibScalar
batteryRemainsTime = _BatteryRemainsTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 5, 2),
    _BatteryRemainsTime_Type()
)
batteryRemainsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRemainsTime.setStatus("current")
_Parallel_ObjectIdentity = ObjectIdentity
parallel = _Parallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 6)
)
_LocalIDNumber_Type = Integer32
_LocalIDNumber_Object = MibScalar
localIDNumber = _LocalIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 6, 1),
    _LocalIDNumber_Type()
)
localIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localIDNumber.setStatus("current")
_ParallelSystemOutputVoltage_Type = Integer32
_ParallelSystemOutputVoltage_Object = MibScalar
parallelSystemOutputVoltage = _ParallelSystemOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 6, 2),
    _ParallelSystemOutputVoltage_Type()
)
parallelSystemOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelSystemOutputVoltage.setStatus("current")
_ParallelSystemOutputCurrent_Type = Integer32
_ParallelSystemOutputCurrent_Object = MibScalar
parallelSystemOutputCurrent = _ParallelSystemOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 6, 3),
    _ParallelSystemOutputCurrent_Type()
)
parallelSystemOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelSystemOutputCurrent.setStatus("current")
_ParallelSystemOutputFrequency_Type = Integer32
_ParallelSystemOutputFrequency_Object = MibScalar
parallelSystemOutputFrequency = _ParallelSystemOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 6, 4),
    _ParallelSystemOutputFrequency_Type()
)
parallelSystemOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelSystemOutputFrequency.setStatus("current")
_ParallelSystemActivePower_Type = Integer32
_ParallelSystemActivePower_Object = MibScalar
parallelSystemActivePower = _ParallelSystemActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 6, 5),
    _ParallelSystemActivePower_Type()
)
parallelSystemActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelSystemActivePower.setStatus("current")
_ParallelSystemApparentPower_Type = Integer32
_ParallelSystemApparentPower_Object = MibScalar
parallelSystemApparentPower = _ParallelSystemApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 6, 6),
    _ParallelSystemApparentPower_Type()
)
parallelSystemApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelSystemApparentPower.setStatus("current")
_ParallelSystemLoad_Type = Integer32
_ParallelSystemLoad_Object = MibScalar
parallelSystemLoad = _ParallelSystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 6, 7),
    _ParallelSystemLoad_Type()
)
parallelSystemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelSystemLoad.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 7)
)


class _CtrlBatterySelfTestStart_Type(Integer32):
    """Custom type ctrlBatterySelfTestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlBatterySelfTestStart_Type.__name__ = "Integer32"
_CtrlBatterySelfTestStart_Object = MibScalar
ctrlBatterySelfTestStart = _CtrlBatterySelfTestStart_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 7, 1),
    _CtrlBatterySelfTestStart_Type()
)
ctrlBatterySelfTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlBatterySelfTestStart.setStatus("current")


class _CtrlBatteryMaintenanceTestStart_Type(Integer32):
    """Custom type ctrlBatteryMaintenanceTestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlBatteryMaintenanceTestStart_Type.__name__ = "Integer32"
_CtrlBatteryMaintenanceTestStart_Object = MibScalar
ctrlBatteryMaintenanceTestStart = _CtrlBatteryMaintenanceTestStart_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 7, 2),
    _CtrlBatteryMaintenanceTestStart_Type()
)
ctrlBatteryMaintenanceTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlBatteryMaintenanceTestStart.setStatus("current")


class _CtrlBatteryTestEnd_Type(Integer32):
    """Custom type ctrlBatteryTestEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlBatteryTestEnd_Type.__name__ = "Integer32"
_CtrlBatteryTestEnd_Object = MibScalar
ctrlBatteryTestEnd = _CtrlBatteryTestEnd_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 7, 3),
    _CtrlBatteryTestEnd_Type()
)
ctrlBatteryTestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlBatteryTestEnd.setStatus("current")


class _CtrlTurnOn_Type(Integer32):
    """Custom type ctrlTurnOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOn_Type.__name__ = "Integer32"
_CtrlTurnOn_Object = MibScalar
ctrlTurnOn = _CtrlTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 7, 4),
    _CtrlTurnOn_Type()
)
ctrlTurnOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOn.setStatus("current")


class _CtrlTurnOff_Type(Integer32):
    """Custom type ctrlTurnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOff_Type.__name__ = "Integer32"
_CtrlTurnOff_Object = MibScalar
ctrlTurnOff = _CtrlTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 7, 5),
    _CtrlTurnOff_Type()
)
ctrlTurnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOff.setStatus("current")


class _CtrlTurnOffOutput_Type(Integer32):
    """Custom type ctrlTurnOffOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOffOutput_Type.__name__ = "Integer32"
_CtrlTurnOffOutput_Object = MibScalar
ctrlTurnOffOutput = _CtrlTurnOffOutput_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 7, 6),
    _CtrlTurnOffOutput_Type()
)
ctrlTurnOffOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOffOutput.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 8)
)


class _ConfBatterySelfTestPeriod_Type(Integer32):
    """Custom type confBatterySelfTestPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("by-3-months", 1),
          ("by-6-months", 2),
          ("by-9-months", 3),
          ("by-12-months", 4))
    )


_ConfBatterySelfTestPeriod_Type.__name__ = "Integer32"
_ConfBatterySelfTestPeriod_Object = MibScalar
confBatterySelfTestPeriod = _ConfBatterySelfTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 8, 1),
    _ConfBatterySelfTestPeriod_Type()
)
confBatterySelfTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confBatterySelfTestPeriod.setStatus("current")


class _ConfECOMode_Type(Integer32):
    """Custom type confECOMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfECOMode_Type.__name__ = "Integer32"
_ConfECOMode_Object = MibScalar
confECOMode = _ConfECOMode_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 8, 2),
    _ConfECOMode_Type()
)
confECOMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confECOMode.setStatus("current")


class _ConfEodAutoStart_Type(Integer32):
    """Custom type confEodAutoStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("disabled", 1))
    )


_ConfEodAutoStart_Type.__name__ = "Integer32"
_ConfEodAutoStart_Object = MibScalar
confEodAutoStart = _ConfEodAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 8, 3),
    _ConfEodAutoStart_Type()
)
confEodAutoStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confEodAutoStart.setStatus("current")
_ConfAddress_Type = Integer32
_ConfAddress_Object = MibScalar
confAddress = _ConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 2, 8, 4),
    _ConfAddress_Type()
)
confAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confAddress.setStatus("current")
_AlarmTrapTable_Object = MibTable
alarmTrapTable = _AlarmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 3)
)
if mibBuilder.loadTexts:
    alarmTrapTable.setStatus("current")
_AlarmTrapEntry_Object = MibTableRow
alarmTrapEntry = _AlarmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 3, 1)
)
alarmTrapEntry.setIndexNames(
    (0, "ENP-ITA0510K-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmTrapEntry.setStatus("current")
_AlarmIndex_Type = Counter32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 3, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmTime_Type = DisplayString
_AlarmTime_Object = MibTableColumn
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 3, 1, 2),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_AlarmStatusChange_Type = StatusChange
_AlarmStatusChange_Object = MibTableColumn
alarmStatusChange = _AlarmStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 3, 1, 3),
    _AlarmStatusChange_Type()
)
alarmStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusChange.setStatus("current")
_AlarmSeverity_Type = Status
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 3, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmDescription_Type = DisplayString
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 3, 1, 5),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_AlarmId_Type = Integer32
_AlarmId_Object = MibTableColumn
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 16, 3, 1, 6),
    _AlarmId_Type()
)
alarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENP-ITA0510K-MIB",
    **{"Status": Status,
       "StatusChange": StatusChange,
       "enp": enp,
       "products": products,
       "ita0510kMIB": ita0510kMIB,
       "ident": ident,
       "identManufacturer": identManufacturer,
       "identModel": identModel,
       "identIndex": identIndex,
       "system": system,
       "status": status,
       "systemStatus": systemStatus,
       "input": input,
       "inputPhaseVoltageA": inputPhaseVoltageA,
       "inputPhaseVoltageB": inputPhaseVoltageB,
       "inputPhaseVoltageC": inputPhaseVoltageC,
       "inputFrequency": inputFrequency,
       "output": output,
       "outputVoltage": outputVoltage,
       "outputCurrent": outputCurrent,
       "outputFrequency": outputFrequency,
       "outputActivePower": outputActivePower,
       "outputApparentPower": outputApparentPower,
       "outputLoad": outputLoad,
       "bypass": bypass,
       "bypassVoltage": bypassVoltage,
       "bypassCurrent": bypassCurrent,
       "bypassFrequency": bypassFrequency,
       "battery": battery,
       "batteryVoltage": batteryVoltage,
       "batteryRemainsTime": batteryRemainsTime,
       "parallel": parallel,
       "localIDNumber": localIDNumber,
       "parallelSystemOutputVoltage": parallelSystemOutputVoltage,
       "parallelSystemOutputCurrent": parallelSystemOutputCurrent,
       "parallelSystemOutputFrequency": parallelSystemOutputFrequency,
       "parallelSystemActivePower": parallelSystemActivePower,
       "parallelSystemApparentPower": parallelSystemApparentPower,
       "parallelSystemLoad": parallelSystemLoad,
       "control": control,
       "ctrlBatterySelfTestStart": ctrlBatterySelfTestStart,
       "ctrlBatteryMaintenanceTestStart": ctrlBatteryMaintenanceTestStart,
       "ctrlBatteryTestEnd": ctrlBatteryTestEnd,
       "ctrlTurnOn": ctrlTurnOn,
       "ctrlTurnOff": ctrlTurnOff,
       "ctrlTurnOffOutput": ctrlTurnOffOutput,
       "config": config,
       "confBatterySelfTestPeriod": confBatterySelfTestPeriod,
       "confECOMode": confECOMode,
       "confEodAutoStart": confEodAutoStart,
       "confAddress": confAddress,
       "alarmTrapTable": alarmTrapTable,
       "alarmTrapEntry": alarmTrapEntry,
       "alarmIndex": alarmIndex,
       "alarmTime": alarmTime,
       "alarmStatusChange": alarmStatusChange,
       "alarmSeverity": alarmSeverity,
       "alarmDescription": alarmDescription,
       "alarmId": alarmId}
)
