# SNMP MIB module (ENP-HipulseU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_13400/ENP-HipulseU-MIB.mib
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

hipulseuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14)
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
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 1)
)
_IdentManufacturer_Type = DisplayString
_IdentManufacturer_Object = MibScalar
identManufacturer = _IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 1, 1),
    _IdentManufacturer_Type()
)
identManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identManufacturer.setStatus("current")
_IdentModel_Type = DisplayString
_IdentModel_Object = MibScalar
identModel = _IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 1, 2),
    _IdentModel_Type()
)
identModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identModel.setStatus("current")
_IdentIndex_Type = Integer32
_IdentIndex_Object = MibScalar
identIndex = _IdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 1, 3),
    _IdentIndex_Type()
)
identIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIndex.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 1)
)
_SystemStatus_Type = Status
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 1, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")
_RoomTemperature_Type = Integer32
_RoomTemperature_Object = MibScalar
roomTemperature = _RoomTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 1, 2),
    _RoomTemperature_Type()
)
roomTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roomTemperature.setStatus("current")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 2)
)
_InputLineVoltageA_Type = Integer32
_InputLineVoltageA_Object = MibScalar
inputLineVoltageA = _InputLineVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 2, 1),
    _InputLineVoltageA_Type()
)
inputLineVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputLineVoltageA.setStatus("current")
_InputLineVoltageB_Type = Integer32
_InputLineVoltageB_Object = MibScalar
inputLineVoltageB = _InputLineVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 2, 2),
    _InputLineVoltageB_Type()
)
inputLineVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputLineVoltageB.setStatus("current")
_InputLineVoltageC_Type = Integer32
_InputLineVoltageC_Object = MibScalar
inputLineVoltageC = _InputLineVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 2, 3),
    _InputLineVoltageC_Type()
)
inputLineVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputLineVoltageC.setStatus("current")
_InputCurrentA_Type = Integer32
_InputCurrentA_Object = MibScalar
inputCurrentA = _InputCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 2, 4),
    _InputCurrentA_Type()
)
inputCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentA.setStatus("current")
_InputCurrentB_Type = Integer32
_InputCurrentB_Object = MibScalar
inputCurrentB = _InputCurrentB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 2, 5),
    _InputCurrentB_Type()
)
inputCurrentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentB.setStatus("current")
_InputCurrentC_Type = Integer32
_InputCurrentC_Object = MibScalar
inputCurrentC = _InputCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 2, 6),
    _InputCurrentC_Type()
)
inputCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentC.setStatus("current")
_InputFrequency_Type = Integer32
_InputFrequency_Object = MibScalar
inputFrequency = _InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 2, 7),
    _InputFrequency_Type()
)
inputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputFrequency.setStatus("current")
_Bypass_ObjectIdentity = ObjectIdentity
bypass = _Bypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 3)
)
_BypassPhaseVoltageA_Type = Integer32
_BypassPhaseVoltageA_Object = MibScalar
bypassPhaseVoltageA = _BypassPhaseVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 3, 1),
    _BypassPhaseVoltageA_Type()
)
bypassPhaseVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassPhaseVoltageA.setStatus("current")
_BypassPhaseVoltageB_Type = Integer32
_BypassPhaseVoltageB_Object = MibScalar
bypassPhaseVoltageB = _BypassPhaseVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 3, 2),
    _BypassPhaseVoltageB_Type()
)
bypassPhaseVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassPhaseVoltageB.setStatus("current")
_BypassPhaseVoltageC_Type = Integer32
_BypassPhaseVoltageC_Object = MibScalar
bypassPhaseVoltageC = _BypassPhaseVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 3, 3),
    _BypassPhaseVoltageC_Type()
)
bypassPhaseVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassPhaseVoltageC.setStatus("current")
_BypassFrequency_Type = Integer32
_BypassFrequency_Object = MibScalar
bypassFrequency = _BypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 3, 4),
    _BypassFrequency_Type()
)
bypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassFrequency.setStatus("current")
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4)
)
_OutputPhaseVoltageA_Type = Integer32
_OutputPhaseVoltageA_Object = MibScalar
outputPhaseVoltageA = _OutputPhaseVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 1),
    _OutputPhaseVoltageA_Type()
)
outputPhaseVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPhaseVoltageA.setStatus("current")
_OutputPhaseVoltageB_Type = Integer32
_OutputPhaseVoltageB_Object = MibScalar
outputPhaseVoltageB = _OutputPhaseVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 2),
    _OutputPhaseVoltageB_Type()
)
outputPhaseVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPhaseVoltageB.setStatus("current")
_OutputPhaseVoltageC_Type = Integer32
_OutputPhaseVoltageC_Object = MibScalar
outputPhaseVoltageC = _OutputPhaseVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 3),
    _OutputPhaseVoltageC_Type()
)
outputPhaseVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPhaseVoltageC.setStatus("current")
_OutputCurrentA_Type = Integer32
_OutputCurrentA_Object = MibScalar
outputCurrentA = _OutputCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 4),
    _OutputCurrentA_Type()
)
outputCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentA.setStatus("current")
_OutputCurrentB_Type = Integer32
_OutputCurrentB_Object = MibScalar
outputCurrentB = _OutputCurrentB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 5),
    _OutputCurrentB_Type()
)
outputCurrentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentB.setStatus("current")
_OutputCurrentC_Type = Integer32
_OutputCurrentC_Object = MibScalar
outputCurrentC = _OutputCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 6),
    _OutputCurrentC_Type()
)
outputCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentC.setStatus("current")
_OutputFrequency_Type = Integer32
_OutputFrequency_Object = MibScalar
outputFrequency = _OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 7),
    _OutputFrequency_Type()
)
outputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputFrequency.setStatus("current")
_OutputPowerFactorA_Type = Integer32
_OutputPowerFactorA_Object = MibScalar
outputPowerFactorA = _OutputPowerFactorA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 8),
    _OutputPowerFactorA_Type()
)
outputPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPowerFactorA.setStatus("current")
_OutputPowerFactorB_Type = Integer32
_OutputPowerFactorB_Object = MibScalar
outputPowerFactorB = _OutputPowerFactorB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 9),
    _OutputPowerFactorB_Type()
)
outputPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPowerFactorB.setStatus("current")
_OutputPowerFactorC_Type = Integer32
_OutputPowerFactorC_Object = MibScalar
outputPowerFactorC = _OutputPowerFactorC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 10),
    _OutputPowerFactorC_Type()
)
outputPowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPowerFactorC.setStatus("current")
_OutputActivePowerA_Type = Integer32
_OutputActivePowerA_Object = MibScalar
outputActivePowerA = _OutputActivePowerA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 11),
    _OutputActivePowerA_Type()
)
outputActivePowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputActivePowerA.setStatus("current")
_OutputActivePowerB_Type = Integer32
_OutputActivePowerB_Object = MibScalar
outputActivePowerB = _OutputActivePowerB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 12),
    _OutputActivePowerB_Type()
)
outputActivePowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputActivePowerB.setStatus("current")
_OutputActivePowerC_Type = Integer32
_OutputActivePowerC_Object = MibScalar
outputActivePowerC = _OutputActivePowerC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 13),
    _OutputActivePowerC_Type()
)
outputActivePowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputActivePowerC.setStatus("current")
_OutputApparentPowerA_Type = Integer32
_OutputApparentPowerA_Object = MibScalar
outputApparentPowerA = _OutputApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 14),
    _OutputApparentPowerA_Type()
)
outputApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputApparentPowerA.setStatus("current")
_OutputApparentPowerB_Type = Integer32
_OutputApparentPowerB_Object = MibScalar
outputApparentPowerB = _OutputApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 15),
    _OutputApparentPowerB_Type()
)
outputApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputApparentPowerB.setStatus("current")
_OutputApparentPowerC_Type = Integer32
_OutputApparentPowerC_Object = MibScalar
outputApparentPowerC = _OutputApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 16),
    _OutputApparentPowerC_Type()
)
outputApparentPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputApparentPowerC.setStatus("current")
_OutputReactivePowerA_Type = Integer32
_OutputReactivePowerA_Object = MibScalar
outputReactivePowerA = _OutputReactivePowerA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 17),
    _OutputReactivePowerA_Type()
)
outputReactivePowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputReactivePowerA.setStatus("current")
_OutputReactivePowerB_Type = Integer32
_OutputReactivePowerB_Object = MibScalar
outputReactivePowerB = _OutputReactivePowerB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 18),
    _OutputReactivePowerB_Type()
)
outputReactivePowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputReactivePowerB.setStatus("current")
_OutputReactivePowerC_Type = Integer32
_OutputReactivePowerC_Object = MibScalar
outputReactivePowerC = _OutputReactivePowerC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 19),
    _OutputReactivePowerC_Type()
)
outputReactivePowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputReactivePowerC.setStatus("current")
_OutputLoadA_Type = Integer32
_OutputLoadA_Object = MibScalar
outputLoadA = _OutputLoadA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 20),
    _OutputLoadA_Type()
)
outputLoadA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputLoadA.setStatus("current")
_OutputLoadB_Type = Integer32
_OutputLoadB_Object = MibScalar
outputLoadB = _OutputLoadB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 21),
    _OutputLoadB_Type()
)
outputLoadB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputLoadB.setStatus("current")
_OutputLoadC_Type = Integer32
_OutputLoadC_Object = MibScalar
outputLoadC = _OutputLoadC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 22),
    _OutputLoadC_Type()
)
outputLoadC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputLoadC.setStatus("current")
_OutputCrestFactorA_Type = Integer32
_OutputCrestFactorA_Object = MibScalar
outputCrestFactorA = _OutputCrestFactorA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 23),
    _OutputCrestFactorA_Type()
)
outputCrestFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCrestFactorA.setStatus("current")
_OutputCrestFactorB_Type = Integer32
_OutputCrestFactorB_Object = MibScalar
outputCrestFactorB = _OutputCrestFactorB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 24),
    _OutputCrestFactorB_Type()
)
outputCrestFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCrestFactorB.setStatus("current")
_OutputCrestFactorC_Type = Integer32
_OutputCrestFactorC_Object = MibScalar
outputCrestFactorC = _OutputCrestFactorC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 4, 25),
    _OutputCrestFactorC_Type()
)
outputCrestFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCrestFactorC.setStatus("current")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 5)
)
_BatteryVoltage_Type = Integer32
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 5, 1),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")
_BatteryCurrent_Type = Integer32
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 5, 2),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("current")
_BatteryRemainsTime_Type = Integer32
_BatteryRemainsTime_Object = MibScalar
batteryRemainsTime = _BatteryRemainsTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 5, 3),
    _BatteryRemainsTime_Type()
)
batteryRemainsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRemainsTime.setStatus("current")
_BatteryTemperature_Type = Integer32
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 5, 4),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("current")
_Parallel_ObjectIdentity = ObjectIdentity
parallel = _Parallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6)
)
_ParallelCapability_Type = Integer32
_ParallelCapability_Object = MibScalar
parallelCapability = _ParallelCapability_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 1),
    _ParallelCapability_Type()
)
parallelCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelCapability.setStatus("current")
_ParallelID_Type = Integer32
_ParallelID_Object = MibScalar
parallelID = _ParallelID_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 2),
    _ParallelID_Type()
)
parallelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelID.setStatus("current")
_ParallelActivePowerA_Type = Integer32
_ParallelActivePowerA_Object = MibScalar
parallelActivePowerA = _ParallelActivePowerA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 3),
    _ParallelActivePowerA_Type()
)
parallelActivePowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelActivePowerA.setStatus("current")
_ParallelActivePowerB_Type = Integer32
_ParallelActivePowerB_Object = MibScalar
parallelActivePowerB = _ParallelActivePowerB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 4),
    _ParallelActivePowerB_Type()
)
parallelActivePowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelActivePowerB.setStatus("current")
_ParallelActivePowerC_Type = Integer32
_ParallelActivePowerC_Object = MibScalar
parallelActivePowerC = _ParallelActivePowerC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 5),
    _ParallelActivePowerC_Type()
)
parallelActivePowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelActivePowerC.setStatus("current")
_ParallelApparentPowerA_Type = Integer32
_ParallelApparentPowerA_Object = MibScalar
parallelApparentPowerA = _ParallelApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 6),
    _ParallelApparentPowerA_Type()
)
parallelApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelApparentPowerA.setStatus("current")
_ParallelApparentPowerB_Type = Integer32
_ParallelApparentPowerB_Object = MibScalar
parallelApparentPowerB = _ParallelApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 7),
    _ParallelApparentPowerB_Type()
)
parallelApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelApparentPowerB.setStatus("current")
_ParallelApparentPowerC_Type = Integer32
_ParallelApparentPowerC_Object = MibScalar
parallelApparentPowerC = _ParallelApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 8),
    _ParallelApparentPowerC_Type()
)
parallelApparentPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelApparentPowerC.setStatus("current")
_ParallelReactivePowerA_Type = Integer32
_ParallelReactivePowerA_Object = MibScalar
parallelReactivePowerA = _ParallelReactivePowerA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 9),
    _ParallelReactivePowerA_Type()
)
parallelReactivePowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelReactivePowerA.setStatus("current")
_ParallelReactivePowerB_Type = Integer32
_ParallelReactivePowerB_Object = MibScalar
parallelReactivePowerB = _ParallelReactivePowerB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 10),
    _ParallelReactivePowerB_Type()
)
parallelReactivePowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelReactivePowerB.setStatus("current")
_ParallelReactivePowerC_Type = Integer32
_ParallelReactivePowerC_Object = MibScalar
parallelReactivePowerC = _ParallelReactivePowerC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 2, 6, 11),
    _ParallelReactivePowerC_Type()
)
parallelReactivePowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelReactivePowerC.setStatus("current")
_AlarmTrapTable_Object = MibTable
alarmTrapTable = _AlarmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 3)
)
if mibBuilder.loadTexts:
    alarmTrapTable.setStatus("current")
_AlarmTrapEntry_Object = MibTableRow
alarmTrapEntry = _AlarmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 3, 1)
)
alarmTrapEntry.setIndexNames(
    (0, "ENP-HipulseU-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmTrapEntry.setStatus("current")
_AlarmIndex_Type = Counter32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 3, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmTime_Type = DisplayString
_AlarmTime_Object = MibTableColumn
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 3, 1, 2),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_AlarmStatusChange_Type = StatusChange
_AlarmStatusChange_Object = MibTableColumn
alarmStatusChange = _AlarmStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 3, 1, 3),
    _AlarmStatusChange_Type()
)
alarmStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusChange.setStatus("current")
_AlarmSeverity_Type = Status
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 3, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmDescription_Type = DisplayString
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 3, 1, 5),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_AlarmId_Type = Integer32
_AlarmId_Object = MibTableColumn
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 14, 3, 1, 6),
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
    "ENP-HipulseU-MIB",
    **{"Status": Status,
       "StatusChange": StatusChange,
       "enp": enp,
       "products": products,
       "hipulseuMIB": hipulseuMIB,
       "ident": ident,
       "identManufacturer": identManufacturer,
       "identModel": identModel,
       "identIndex": identIndex,
       "system": system,
       "status": status,
       "systemStatus": systemStatus,
       "roomTemperature": roomTemperature,
       "input": input,
       "inputLineVoltageA": inputLineVoltageA,
       "inputLineVoltageB": inputLineVoltageB,
       "inputLineVoltageC": inputLineVoltageC,
       "inputCurrentA": inputCurrentA,
       "inputCurrentB": inputCurrentB,
       "inputCurrentC": inputCurrentC,
       "inputFrequency": inputFrequency,
       "bypass": bypass,
       "bypassPhaseVoltageA": bypassPhaseVoltageA,
       "bypassPhaseVoltageB": bypassPhaseVoltageB,
       "bypassPhaseVoltageC": bypassPhaseVoltageC,
       "bypassFrequency": bypassFrequency,
       "output": output,
       "outputPhaseVoltageA": outputPhaseVoltageA,
       "outputPhaseVoltageB": outputPhaseVoltageB,
       "outputPhaseVoltageC": outputPhaseVoltageC,
       "outputCurrentA": outputCurrentA,
       "outputCurrentB": outputCurrentB,
       "outputCurrentC": outputCurrentC,
       "outputFrequency": outputFrequency,
       "outputPowerFactorA": outputPowerFactorA,
       "outputPowerFactorB": outputPowerFactorB,
       "outputPowerFactorC": outputPowerFactorC,
       "outputActivePowerA": outputActivePowerA,
       "outputActivePowerB": outputActivePowerB,
       "outputActivePowerC": outputActivePowerC,
       "outputApparentPowerA": outputApparentPowerA,
       "outputApparentPowerB": outputApparentPowerB,
       "outputApparentPowerC": outputApparentPowerC,
       "outputReactivePowerA": outputReactivePowerA,
       "outputReactivePowerB": outputReactivePowerB,
       "outputReactivePowerC": outputReactivePowerC,
       "outputLoadA": outputLoadA,
       "outputLoadB": outputLoadB,
       "outputLoadC": outputLoadC,
       "outputCrestFactorA": outputCrestFactorA,
       "outputCrestFactorB": outputCrestFactorB,
       "outputCrestFactorC": outputCrestFactorC,
       "battery": battery,
       "batteryVoltage": batteryVoltage,
       "batteryCurrent": batteryCurrent,
       "batteryRemainsTime": batteryRemainsTime,
       "batteryTemperature": batteryTemperature,
       "parallel": parallel,
       "parallelCapability": parallelCapability,
       "parallelID": parallelID,
       "parallelActivePowerA": parallelActivePowerA,
       "parallelActivePowerB": parallelActivePowerB,
       "parallelActivePowerC": parallelActivePowerC,
       "parallelApparentPowerA": parallelApparentPowerA,
       "parallelApparentPowerB": parallelApparentPowerB,
       "parallelApparentPowerC": parallelApparentPowerC,
       "parallelReactivePowerA": parallelReactivePowerA,
       "parallelReactivePowerB": parallelReactivePowerB,
       "parallelReactivePowerC": parallelReactivePowerC,
       "alarmTrapTable": alarmTrapTable,
       "alarmTrapEntry": alarmTrapEntry,
       "alarmIndex": alarmIndex,
       "alarmTime": alarmTime,
       "alarmStatusChange": alarmStatusChange,
       "alarmSeverity": alarmSeverity,
       "alarmDescription": alarmDescription,
       "alarmId": alarmId}
)
