# SNMP MIB module (CISCO-FIREPOWER-AP-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-MEMORY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:13 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApEquipmentOperability,
 CfprApEquipmentPowerState,
 CfprApEquipmentPresence,
 CfprApEquipmentSensorThresholdStatus,
 CfprApMemoryAdminState,
 CfprApMemoryArrayEnvStatsHistThresholded,
 CfprApMemoryArrayEnvStatsThresholded,
 CfprApMemoryArrayId,
 CfprApMemoryBufferUnitEnvStatsHistThresholded,
 CfprApMemoryBufferUnitEnvStatsThresholded,
 CfprApMemoryBufferUnitId,
 CfprApMemoryErrorCorrection,
 CfprApMemoryErrorStatsThresholded,
 CfprApMemoryFormFactor,
 CfprApMemoryIssues,
 CfprApMemoryRuntimeHistThresholded,
 CfprApMemoryRuntimeThresholded,
 CfprApMemoryRuntimeType,
 CfprApMemoryType,
 CfprApMemoryUnitEnvStatsHistThresholded,
 CfprApMemoryUnitEnvStatsThresholded,
 CfprApMemoryUnitId,
 CfprApMemoryUnitOperability,
 CfprApMemoryVisibility) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApEquipmentOperability",
    "CfprApEquipmentPowerState",
    "CfprApEquipmentPresence",
    "CfprApEquipmentSensorThresholdStatus",
    "CfprApMemoryAdminState",
    "CfprApMemoryArrayEnvStatsHistThresholded",
    "CfprApMemoryArrayEnvStatsThresholded",
    "CfprApMemoryArrayId",
    "CfprApMemoryBufferUnitEnvStatsHistThresholded",
    "CfprApMemoryBufferUnitEnvStatsThresholded",
    "CfprApMemoryBufferUnitId",
    "CfprApMemoryErrorCorrection",
    "CfprApMemoryErrorStatsThresholded",
    "CfprApMemoryFormFactor",
    "CfprApMemoryIssues",
    "CfprApMemoryRuntimeHistThresholded",
    "CfprApMemoryRuntimeThresholded",
    "CfprApMemoryRuntimeType",
    "CfprApMemoryType",
    "CfprApMemoryUnitEnvStatsHistThresholded",
    "CfprApMemoryUnitEnvStatsThresholded",
    "CfprApMemoryUnitId",
    "CfprApMemoryUnitOperability",
    "CfprApMemoryVisibility")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprApMemoryObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApMemoryArrayTable_Object = MibTable
cfprApMemoryArrayTable = _CfprApMemoryArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1)
)
if mibBuilder.loadTexts:
    cfprApMemoryArrayTable.setStatus("current")
_CfprApMemoryArrayEntry_Object = MibTableRow
cfprApMemoryArrayEntry = _CfprApMemoryArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1)
)
cfprApMemoryArrayEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryArrayInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryArrayEntry.setStatus("current")
_CfprApMemoryArrayInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryArrayInstanceId_Object = MibTableColumn
cfprApMemoryArrayInstanceId = _CfprApMemoryArrayInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 1),
    _CfprApMemoryArrayInstanceId_Type()
)
cfprApMemoryArrayInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryArrayInstanceId.setStatus("current")
_CfprApMemoryArrayDn_Type = CfprApManagedObjectDn
_CfprApMemoryArrayDn_Object = MibTableColumn
cfprApMemoryArrayDn = _CfprApMemoryArrayDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 2),
    _CfprApMemoryArrayDn_Type()
)
cfprApMemoryArrayDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayDn.setStatus("current")
_CfprApMemoryArrayRn_Type = SnmpAdminString
_CfprApMemoryArrayRn_Object = MibTableColumn
cfprApMemoryArrayRn = _CfprApMemoryArrayRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 3),
    _CfprApMemoryArrayRn_Type()
)
cfprApMemoryArrayRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayRn.setStatus("current")
_CfprApMemoryArrayCpuId_Type = Gauge32
_CfprApMemoryArrayCpuId_Object = MibTableColumn
cfprApMemoryArrayCpuId = _CfprApMemoryArrayCpuId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 4),
    _CfprApMemoryArrayCpuId_Type()
)
cfprApMemoryArrayCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayCpuId.setStatus("current")
_CfprApMemoryArrayCurrCapacity_Type = Gauge32
_CfprApMemoryArrayCurrCapacity_Object = MibTableColumn
cfprApMemoryArrayCurrCapacity = _CfprApMemoryArrayCurrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 5),
    _CfprApMemoryArrayCurrCapacity_Type()
)
cfprApMemoryArrayCurrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayCurrCapacity.setStatus("current")
_CfprApMemoryArrayErrorCorrection_Type = CfprApMemoryErrorCorrection
_CfprApMemoryArrayErrorCorrection_Object = MibTableColumn
cfprApMemoryArrayErrorCorrection = _CfprApMemoryArrayErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 6),
    _CfprApMemoryArrayErrorCorrection_Type()
)
cfprApMemoryArrayErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayErrorCorrection.setStatus("current")
_CfprApMemoryArrayId_Type = CfprApMemoryArrayId
_CfprApMemoryArrayId_Object = MibTableColumn
cfprApMemoryArrayId = _CfprApMemoryArrayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 7),
    _CfprApMemoryArrayId_Type()
)
cfprApMemoryArrayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayId.setStatus("current")
_CfprApMemoryArrayLocationDn_Type = SnmpAdminString
_CfprApMemoryArrayLocationDn_Object = MibTableColumn
cfprApMemoryArrayLocationDn = _CfprApMemoryArrayLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 8),
    _CfprApMemoryArrayLocationDn_Type()
)
cfprApMemoryArrayLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayLocationDn.setStatus("current")
_CfprApMemoryArrayMaxCapacity_Type = Gauge32
_CfprApMemoryArrayMaxCapacity_Object = MibTableColumn
cfprApMemoryArrayMaxCapacity = _CfprApMemoryArrayMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 9),
    _CfprApMemoryArrayMaxCapacity_Type()
)
cfprApMemoryArrayMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayMaxCapacity.setStatus("current")
_CfprApMemoryArrayMaxDevices_Type = Gauge32
_CfprApMemoryArrayMaxDevices_Object = MibTableColumn
cfprApMemoryArrayMaxDevices = _CfprApMemoryArrayMaxDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 10),
    _CfprApMemoryArrayMaxDevices_Type()
)
cfprApMemoryArrayMaxDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayMaxDevices.setStatus("current")
_CfprApMemoryArrayModel_Type = SnmpAdminString
_CfprApMemoryArrayModel_Object = MibTableColumn
cfprApMemoryArrayModel = _CfprApMemoryArrayModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 11),
    _CfprApMemoryArrayModel_Type()
)
cfprApMemoryArrayModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayModel.setStatus("current")
_CfprApMemoryArrayOperQualifierReason_Type = SnmpAdminString
_CfprApMemoryArrayOperQualifierReason_Object = MibTableColumn
cfprApMemoryArrayOperQualifierReason = _CfprApMemoryArrayOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 12),
    _CfprApMemoryArrayOperQualifierReason_Type()
)
cfprApMemoryArrayOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayOperQualifierReason.setStatus("current")
_CfprApMemoryArrayOperState_Type = CfprApEquipmentOperability
_CfprApMemoryArrayOperState_Object = MibTableColumn
cfprApMemoryArrayOperState = _CfprApMemoryArrayOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 13),
    _CfprApMemoryArrayOperState_Type()
)
cfprApMemoryArrayOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayOperState.setStatus("current")
_CfprApMemoryArrayOperability_Type = CfprApEquipmentOperability
_CfprApMemoryArrayOperability_Object = MibTableColumn
cfprApMemoryArrayOperability = _CfprApMemoryArrayOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 14),
    _CfprApMemoryArrayOperability_Type()
)
cfprApMemoryArrayOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayOperability.setStatus("current")
_CfprApMemoryArrayPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryArrayPerf_Object = MibTableColumn
cfprApMemoryArrayPerf = _CfprApMemoryArrayPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 15),
    _CfprApMemoryArrayPerf_Type()
)
cfprApMemoryArrayPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayPerf.setStatus("current")
_CfprApMemoryArrayPopulated_Type = Gauge32
_CfprApMemoryArrayPopulated_Object = MibTableColumn
cfprApMemoryArrayPopulated = _CfprApMemoryArrayPopulated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 16),
    _CfprApMemoryArrayPopulated_Type()
)
cfprApMemoryArrayPopulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayPopulated.setStatus("current")
_CfprApMemoryArrayPower_Type = CfprApEquipmentPowerState
_CfprApMemoryArrayPower_Object = MibTableColumn
cfprApMemoryArrayPower = _CfprApMemoryArrayPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 17),
    _CfprApMemoryArrayPower_Type()
)
cfprApMemoryArrayPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayPower.setStatus("current")
_CfprApMemoryArrayPresence_Type = CfprApEquipmentPresence
_CfprApMemoryArrayPresence_Object = MibTableColumn
cfprApMemoryArrayPresence = _CfprApMemoryArrayPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 18),
    _CfprApMemoryArrayPresence_Type()
)
cfprApMemoryArrayPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayPresence.setStatus("current")
_CfprApMemoryArrayRevision_Type = SnmpAdminString
_CfprApMemoryArrayRevision_Object = MibTableColumn
cfprApMemoryArrayRevision = _CfprApMemoryArrayRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 19),
    _CfprApMemoryArrayRevision_Type()
)
cfprApMemoryArrayRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayRevision.setStatus("current")
_CfprApMemoryArraySerial_Type = SnmpAdminString
_CfprApMemoryArraySerial_Object = MibTableColumn
cfprApMemoryArraySerial = _CfprApMemoryArraySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 20),
    _CfprApMemoryArraySerial_Type()
)
cfprApMemoryArraySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArraySerial.setStatus("current")
_CfprApMemoryArrayThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryArrayThermal_Object = MibTableColumn
cfprApMemoryArrayThermal = _CfprApMemoryArrayThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 21),
    _CfprApMemoryArrayThermal_Type()
)
cfprApMemoryArrayThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayThermal.setStatus("current")
_CfprApMemoryArrayVendor_Type = SnmpAdminString
_CfprApMemoryArrayVendor_Object = MibTableColumn
cfprApMemoryArrayVendor = _CfprApMemoryArrayVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 22),
    _CfprApMemoryArrayVendor_Type()
)
cfprApMemoryArrayVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayVendor.setStatus("current")
_CfprApMemoryArrayVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryArrayVoltage_Object = MibTableColumn
cfprApMemoryArrayVoltage = _CfprApMemoryArrayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 1, 1, 23),
    _CfprApMemoryArrayVoltage_Type()
)
cfprApMemoryArrayVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayVoltage.setStatus("current")
_CfprApMemoryArrayEnvStatsTable_Object = MibTable
cfprApMemoryArrayEnvStatsTable = _CfprApMemoryArrayEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2)
)
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsTable.setStatus("current")
_CfprApMemoryArrayEnvStatsEntry_Object = MibTableRow
cfprApMemoryArrayEnvStatsEntry = _CfprApMemoryArrayEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1)
)
cfprApMemoryArrayEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryArrayEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsEntry.setStatus("current")
_CfprApMemoryArrayEnvStatsInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryArrayEnvStatsInstanceId_Object = MibTableColumn
cfprApMemoryArrayEnvStatsInstanceId = _CfprApMemoryArrayEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 1),
    _CfprApMemoryArrayEnvStatsInstanceId_Type()
)
cfprApMemoryArrayEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsInstanceId.setStatus("current")
_CfprApMemoryArrayEnvStatsDn_Type = CfprApManagedObjectDn
_CfprApMemoryArrayEnvStatsDn_Object = MibTableColumn
cfprApMemoryArrayEnvStatsDn = _CfprApMemoryArrayEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 2),
    _CfprApMemoryArrayEnvStatsDn_Type()
)
cfprApMemoryArrayEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsDn.setStatus("current")
_CfprApMemoryArrayEnvStatsRn_Type = SnmpAdminString
_CfprApMemoryArrayEnvStatsRn_Object = MibTableColumn
cfprApMemoryArrayEnvStatsRn = _CfprApMemoryArrayEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 3),
    _CfprApMemoryArrayEnvStatsRn_Type()
)
cfprApMemoryArrayEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsRn.setStatus("current")
_CfprApMemoryArrayEnvStatsInputCurrent_Type = Integer32
_CfprApMemoryArrayEnvStatsInputCurrent_Object = MibTableColumn
cfprApMemoryArrayEnvStatsInputCurrent = _CfprApMemoryArrayEnvStatsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 4),
    _CfprApMemoryArrayEnvStatsInputCurrent_Type()
)
cfprApMemoryArrayEnvStatsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsInputCurrent.setStatus("current")
_CfprApMemoryArrayEnvStatsInputCurrentAvg_Type = Integer32
_CfprApMemoryArrayEnvStatsInputCurrentAvg_Object = MibTableColumn
cfprApMemoryArrayEnvStatsInputCurrentAvg = _CfprApMemoryArrayEnvStatsInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 5),
    _CfprApMemoryArrayEnvStatsInputCurrentAvg_Type()
)
cfprApMemoryArrayEnvStatsInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsInputCurrentAvg.setStatus("current")
_CfprApMemoryArrayEnvStatsInputCurrentMax_Type = Integer32
_CfprApMemoryArrayEnvStatsInputCurrentMax_Object = MibTableColumn
cfprApMemoryArrayEnvStatsInputCurrentMax = _CfprApMemoryArrayEnvStatsInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 6),
    _CfprApMemoryArrayEnvStatsInputCurrentMax_Type()
)
cfprApMemoryArrayEnvStatsInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsInputCurrentMax.setStatus("current")
_CfprApMemoryArrayEnvStatsInputCurrentMin_Type = Integer32
_CfprApMemoryArrayEnvStatsInputCurrentMin_Object = MibTableColumn
cfprApMemoryArrayEnvStatsInputCurrentMin = _CfprApMemoryArrayEnvStatsInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 7),
    _CfprApMemoryArrayEnvStatsInputCurrentMin_Type()
)
cfprApMemoryArrayEnvStatsInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsInputCurrentMin.setStatus("current")
_CfprApMemoryArrayEnvStatsIntervals_Type = Gauge32
_CfprApMemoryArrayEnvStatsIntervals_Object = MibTableColumn
cfprApMemoryArrayEnvStatsIntervals = _CfprApMemoryArrayEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 8),
    _CfprApMemoryArrayEnvStatsIntervals_Type()
)
cfprApMemoryArrayEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsIntervals.setStatus("current")
_CfprApMemoryArrayEnvStatsSuspect_Type = TruthValue
_CfprApMemoryArrayEnvStatsSuspect_Object = MibTableColumn
cfprApMemoryArrayEnvStatsSuspect = _CfprApMemoryArrayEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 9),
    _CfprApMemoryArrayEnvStatsSuspect_Type()
)
cfprApMemoryArrayEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsSuspect.setStatus("current")
_CfprApMemoryArrayEnvStatsThresholded_Type = CfprApMemoryArrayEnvStatsThresholded
_CfprApMemoryArrayEnvStatsThresholded_Object = MibTableColumn
cfprApMemoryArrayEnvStatsThresholded = _CfprApMemoryArrayEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 10),
    _CfprApMemoryArrayEnvStatsThresholded_Type()
)
cfprApMemoryArrayEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsThresholded.setStatus("current")
_CfprApMemoryArrayEnvStatsTimeCollected_Type = DateAndTime
_CfprApMemoryArrayEnvStatsTimeCollected_Object = MibTableColumn
cfprApMemoryArrayEnvStatsTimeCollected = _CfprApMemoryArrayEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 11),
    _CfprApMemoryArrayEnvStatsTimeCollected_Type()
)
cfprApMemoryArrayEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsTimeCollected.setStatus("current")
_CfprApMemoryArrayEnvStatsUpdate_Type = Gauge32
_CfprApMemoryArrayEnvStatsUpdate_Object = MibTableColumn
cfprApMemoryArrayEnvStatsUpdate = _CfprApMemoryArrayEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 2, 1, 12),
    _CfprApMemoryArrayEnvStatsUpdate_Type()
)
cfprApMemoryArrayEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsUpdate.setStatus("current")
_CfprApMemoryArrayEnvStatsHistTable_Object = MibTable
cfprApMemoryArrayEnvStatsHistTable = _CfprApMemoryArrayEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3)
)
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistTable.setStatus("current")
_CfprApMemoryArrayEnvStatsHistEntry_Object = MibTableRow
cfprApMemoryArrayEnvStatsHistEntry = _CfprApMemoryArrayEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1)
)
cfprApMemoryArrayEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryArrayEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistEntry.setStatus("current")
_CfprApMemoryArrayEnvStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryArrayEnvStatsHistInstanceId_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistInstanceId = _CfprApMemoryArrayEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 1),
    _CfprApMemoryArrayEnvStatsHistInstanceId_Type()
)
cfprApMemoryArrayEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistInstanceId.setStatus("current")
_CfprApMemoryArrayEnvStatsHistDn_Type = CfprApManagedObjectDn
_CfprApMemoryArrayEnvStatsHistDn_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistDn = _CfprApMemoryArrayEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 2),
    _CfprApMemoryArrayEnvStatsHistDn_Type()
)
cfprApMemoryArrayEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistDn.setStatus("current")
_CfprApMemoryArrayEnvStatsHistRn_Type = SnmpAdminString
_CfprApMemoryArrayEnvStatsHistRn_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistRn = _CfprApMemoryArrayEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 3),
    _CfprApMemoryArrayEnvStatsHistRn_Type()
)
cfprApMemoryArrayEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistRn.setStatus("current")
_CfprApMemoryArrayEnvStatsHistId_Type = Unsigned64
_CfprApMemoryArrayEnvStatsHistId_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistId = _CfprApMemoryArrayEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 4),
    _CfprApMemoryArrayEnvStatsHistId_Type()
)
cfprApMemoryArrayEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistId.setStatus("current")
_CfprApMemoryArrayEnvStatsHistInputCurrent_Type = Integer32
_CfprApMemoryArrayEnvStatsHistInputCurrent_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistInputCurrent = _CfprApMemoryArrayEnvStatsHistInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 5),
    _CfprApMemoryArrayEnvStatsHistInputCurrent_Type()
)
cfprApMemoryArrayEnvStatsHistInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistInputCurrent.setStatus("current")
_CfprApMemoryArrayEnvStatsHistInputCurrentAvg_Type = Integer32
_CfprApMemoryArrayEnvStatsHistInputCurrentAvg_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistInputCurrentAvg = _CfprApMemoryArrayEnvStatsHistInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 6),
    _CfprApMemoryArrayEnvStatsHistInputCurrentAvg_Type()
)
cfprApMemoryArrayEnvStatsHistInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistInputCurrentAvg.setStatus("current")
_CfprApMemoryArrayEnvStatsHistInputCurrentMax_Type = Integer32
_CfprApMemoryArrayEnvStatsHistInputCurrentMax_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistInputCurrentMax = _CfprApMemoryArrayEnvStatsHistInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 7),
    _CfprApMemoryArrayEnvStatsHistInputCurrentMax_Type()
)
cfprApMemoryArrayEnvStatsHistInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistInputCurrentMax.setStatus("current")
_CfprApMemoryArrayEnvStatsHistInputCurrentMin_Type = Integer32
_CfprApMemoryArrayEnvStatsHistInputCurrentMin_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistInputCurrentMin = _CfprApMemoryArrayEnvStatsHistInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 8),
    _CfprApMemoryArrayEnvStatsHistInputCurrentMin_Type()
)
cfprApMemoryArrayEnvStatsHistInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistInputCurrentMin.setStatus("current")
_CfprApMemoryArrayEnvStatsHistMostRecent_Type = TruthValue
_CfprApMemoryArrayEnvStatsHistMostRecent_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistMostRecent = _CfprApMemoryArrayEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 9),
    _CfprApMemoryArrayEnvStatsHistMostRecent_Type()
)
cfprApMemoryArrayEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistMostRecent.setStatus("current")
_CfprApMemoryArrayEnvStatsHistSuspect_Type = TruthValue
_CfprApMemoryArrayEnvStatsHistSuspect_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistSuspect = _CfprApMemoryArrayEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 10),
    _CfprApMemoryArrayEnvStatsHistSuspect_Type()
)
cfprApMemoryArrayEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistSuspect.setStatus("current")
_CfprApMemoryArrayEnvStatsHistThresholded_Type = CfprApMemoryArrayEnvStatsHistThresholded
_CfprApMemoryArrayEnvStatsHistThresholded_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistThresholded = _CfprApMemoryArrayEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 11),
    _CfprApMemoryArrayEnvStatsHistThresholded_Type()
)
cfprApMemoryArrayEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistThresholded.setStatus("current")
_CfprApMemoryArrayEnvStatsHistTimeCollected_Type = DateAndTime
_CfprApMemoryArrayEnvStatsHistTimeCollected_Object = MibTableColumn
cfprApMemoryArrayEnvStatsHistTimeCollected = _CfprApMemoryArrayEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 3, 1, 12),
    _CfprApMemoryArrayEnvStatsHistTimeCollected_Type()
)
cfprApMemoryArrayEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryArrayEnvStatsHistTimeCollected.setStatus("current")
_CfprApMemoryBufferUnitTable_Object = MibTable
cfprApMemoryBufferUnitTable = _CfprApMemoryBufferUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4)
)
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitTable.setStatus("current")
_CfprApMemoryBufferUnitEntry_Object = MibTableRow
cfprApMemoryBufferUnitEntry = _CfprApMemoryBufferUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1)
)
cfprApMemoryBufferUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryBufferUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEntry.setStatus("current")
_CfprApMemoryBufferUnitInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryBufferUnitInstanceId_Object = MibTableColumn
cfprApMemoryBufferUnitInstanceId = _CfprApMemoryBufferUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 1),
    _CfprApMemoryBufferUnitInstanceId_Type()
)
cfprApMemoryBufferUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitInstanceId.setStatus("current")
_CfprApMemoryBufferUnitDn_Type = CfprApManagedObjectDn
_CfprApMemoryBufferUnitDn_Object = MibTableColumn
cfprApMemoryBufferUnitDn = _CfprApMemoryBufferUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 2),
    _CfprApMemoryBufferUnitDn_Type()
)
cfprApMemoryBufferUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitDn.setStatus("current")
_CfprApMemoryBufferUnitRn_Type = SnmpAdminString
_CfprApMemoryBufferUnitRn_Object = MibTableColumn
cfprApMemoryBufferUnitRn = _CfprApMemoryBufferUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 3),
    _CfprApMemoryBufferUnitRn_Type()
)
cfprApMemoryBufferUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitRn.setStatus("current")
_CfprApMemoryBufferUnitId_Type = CfprApMemoryBufferUnitId
_CfprApMemoryBufferUnitId_Object = MibTableColumn
cfprApMemoryBufferUnitId = _CfprApMemoryBufferUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 4),
    _CfprApMemoryBufferUnitId_Type()
)
cfprApMemoryBufferUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitId.setStatus("current")
_CfprApMemoryBufferUnitLocationDn_Type = SnmpAdminString
_CfprApMemoryBufferUnitLocationDn_Object = MibTableColumn
cfprApMemoryBufferUnitLocationDn = _CfprApMemoryBufferUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 5),
    _CfprApMemoryBufferUnitLocationDn_Type()
)
cfprApMemoryBufferUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitLocationDn.setStatus("current")
_CfprApMemoryBufferUnitModel_Type = SnmpAdminString
_CfprApMemoryBufferUnitModel_Object = MibTableColumn
cfprApMemoryBufferUnitModel = _CfprApMemoryBufferUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 6),
    _CfprApMemoryBufferUnitModel_Type()
)
cfprApMemoryBufferUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitModel.setStatus("current")
_CfprApMemoryBufferUnitOperQualifierReason_Type = SnmpAdminString
_CfprApMemoryBufferUnitOperQualifierReason_Object = MibTableColumn
cfprApMemoryBufferUnitOperQualifierReason = _CfprApMemoryBufferUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 7),
    _CfprApMemoryBufferUnitOperQualifierReason_Type()
)
cfprApMemoryBufferUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitOperQualifierReason.setStatus("current")
_CfprApMemoryBufferUnitOperState_Type = CfprApEquipmentOperability
_CfprApMemoryBufferUnitOperState_Object = MibTableColumn
cfprApMemoryBufferUnitOperState = _CfprApMemoryBufferUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 8),
    _CfprApMemoryBufferUnitOperState_Type()
)
cfprApMemoryBufferUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitOperState.setStatus("current")
_CfprApMemoryBufferUnitOperability_Type = CfprApEquipmentOperability
_CfprApMemoryBufferUnitOperability_Object = MibTableColumn
cfprApMemoryBufferUnitOperability = _CfprApMemoryBufferUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 9),
    _CfprApMemoryBufferUnitOperability_Type()
)
cfprApMemoryBufferUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitOperability.setStatus("current")
_CfprApMemoryBufferUnitPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryBufferUnitPerf_Object = MibTableColumn
cfprApMemoryBufferUnitPerf = _CfprApMemoryBufferUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 10),
    _CfprApMemoryBufferUnitPerf_Type()
)
cfprApMemoryBufferUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitPerf.setStatus("current")
_CfprApMemoryBufferUnitPower_Type = CfprApEquipmentPowerState
_CfprApMemoryBufferUnitPower_Object = MibTableColumn
cfprApMemoryBufferUnitPower = _CfprApMemoryBufferUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 11),
    _CfprApMemoryBufferUnitPower_Type()
)
cfprApMemoryBufferUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitPower.setStatus("current")
_CfprApMemoryBufferUnitPresence_Type = CfprApEquipmentPresence
_CfprApMemoryBufferUnitPresence_Object = MibTableColumn
cfprApMemoryBufferUnitPresence = _CfprApMemoryBufferUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 12),
    _CfprApMemoryBufferUnitPresence_Type()
)
cfprApMemoryBufferUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitPresence.setStatus("current")
_CfprApMemoryBufferUnitRevision_Type = SnmpAdminString
_CfprApMemoryBufferUnitRevision_Object = MibTableColumn
cfprApMemoryBufferUnitRevision = _CfprApMemoryBufferUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 13),
    _CfprApMemoryBufferUnitRevision_Type()
)
cfprApMemoryBufferUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitRevision.setStatus("current")
_CfprApMemoryBufferUnitSerial_Type = SnmpAdminString
_CfprApMemoryBufferUnitSerial_Object = MibTableColumn
cfprApMemoryBufferUnitSerial = _CfprApMemoryBufferUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 14),
    _CfprApMemoryBufferUnitSerial_Type()
)
cfprApMemoryBufferUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitSerial.setStatus("current")
_CfprApMemoryBufferUnitThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryBufferUnitThermal_Object = MibTableColumn
cfprApMemoryBufferUnitThermal = _CfprApMemoryBufferUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 15),
    _CfprApMemoryBufferUnitThermal_Type()
)
cfprApMemoryBufferUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitThermal.setStatus("current")
_CfprApMemoryBufferUnitVendor_Type = SnmpAdminString
_CfprApMemoryBufferUnitVendor_Object = MibTableColumn
cfprApMemoryBufferUnitVendor = _CfprApMemoryBufferUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 16),
    _CfprApMemoryBufferUnitVendor_Type()
)
cfprApMemoryBufferUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitVendor.setStatus("current")
_CfprApMemoryBufferUnitVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryBufferUnitVoltage_Object = MibTableColumn
cfprApMemoryBufferUnitVoltage = _CfprApMemoryBufferUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 4, 1, 17),
    _CfprApMemoryBufferUnitVoltage_Type()
)
cfprApMemoryBufferUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitVoltage.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsTable_Object = MibTable
cfprApMemoryBufferUnitEnvStatsTable = _CfprApMemoryBufferUnitEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5)
)
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsTable.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsEntry_Object = MibTableRow
cfprApMemoryBufferUnitEnvStatsEntry = _CfprApMemoryBufferUnitEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1)
)
cfprApMemoryBufferUnitEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryBufferUnitEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsEntry.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryBufferUnitEnvStatsInstanceId_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsInstanceId = _CfprApMemoryBufferUnitEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 1),
    _CfprApMemoryBufferUnitEnvStatsInstanceId_Type()
)
cfprApMemoryBufferUnitEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsInstanceId.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsDn_Type = CfprApManagedObjectDn
_CfprApMemoryBufferUnitEnvStatsDn_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsDn = _CfprApMemoryBufferUnitEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 2),
    _CfprApMemoryBufferUnitEnvStatsDn_Type()
)
cfprApMemoryBufferUnitEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsDn.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsRn_Type = SnmpAdminString
_CfprApMemoryBufferUnitEnvStatsRn_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsRn = _CfprApMemoryBufferUnitEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 3),
    _CfprApMemoryBufferUnitEnvStatsRn_Type()
)
cfprApMemoryBufferUnitEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsRn.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsIntervals_Type = Gauge32
_CfprApMemoryBufferUnitEnvStatsIntervals_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsIntervals = _CfprApMemoryBufferUnitEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 4),
    _CfprApMemoryBufferUnitEnvStatsIntervals_Type()
)
cfprApMemoryBufferUnitEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsIntervals.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsSuspect_Type = TruthValue
_CfprApMemoryBufferUnitEnvStatsSuspect_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsSuspect = _CfprApMemoryBufferUnitEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 5),
    _CfprApMemoryBufferUnitEnvStatsSuspect_Type()
)
cfprApMemoryBufferUnitEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsSuspect.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsTemperature_Type = Integer32
_CfprApMemoryBufferUnitEnvStatsTemperature_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsTemperature = _CfprApMemoryBufferUnitEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 6),
    _CfprApMemoryBufferUnitEnvStatsTemperature_Type()
)
cfprApMemoryBufferUnitEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsTemperature.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsTemperatureAvg_Type = Integer32
_CfprApMemoryBufferUnitEnvStatsTemperatureAvg_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsTemperatureAvg = _CfprApMemoryBufferUnitEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 7),
    _CfprApMemoryBufferUnitEnvStatsTemperatureAvg_Type()
)
cfprApMemoryBufferUnitEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsTemperatureAvg.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsTemperatureMax_Type = Integer32
_CfprApMemoryBufferUnitEnvStatsTemperatureMax_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsTemperatureMax = _CfprApMemoryBufferUnitEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 8),
    _CfprApMemoryBufferUnitEnvStatsTemperatureMax_Type()
)
cfprApMemoryBufferUnitEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsTemperatureMax.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsTemperatureMin_Type = Integer32
_CfprApMemoryBufferUnitEnvStatsTemperatureMin_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsTemperatureMin = _CfprApMemoryBufferUnitEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 9),
    _CfprApMemoryBufferUnitEnvStatsTemperatureMin_Type()
)
cfprApMemoryBufferUnitEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsTemperatureMin.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsThresholded_Type = CfprApMemoryBufferUnitEnvStatsThresholded
_CfprApMemoryBufferUnitEnvStatsThresholded_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsThresholded = _CfprApMemoryBufferUnitEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 10),
    _CfprApMemoryBufferUnitEnvStatsThresholded_Type()
)
cfprApMemoryBufferUnitEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsThresholded.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsTimeCollected_Type = DateAndTime
_CfprApMemoryBufferUnitEnvStatsTimeCollected_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsTimeCollected = _CfprApMemoryBufferUnitEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 11),
    _CfprApMemoryBufferUnitEnvStatsTimeCollected_Type()
)
cfprApMemoryBufferUnitEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsTimeCollected.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsUpdate_Type = Gauge32
_CfprApMemoryBufferUnitEnvStatsUpdate_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsUpdate = _CfprApMemoryBufferUnitEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 5, 1, 12),
    _CfprApMemoryBufferUnitEnvStatsUpdate_Type()
)
cfprApMemoryBufferUnitEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsUpdate.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistTable_Object = MibTable
cfprApMemoryBufferUnitEnvStatsHistTable = _CfprApMemoryBufferUnitEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6)
)
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistTable.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistEntry_Object = MibTableRow
cfprApMemoryBufferUnitEnvStatsHistEntry = _CfprApMemoryBufferUnitEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1)
)
cfprApMemoryBufferUnitEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryBufferUnitEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistEntry.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryBufferUnitEnvStatsHistInstanceId_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistInstanceId = _CfprApMemoryBufferUnitEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 1),
    _CfprApMemoryBufferUnitEnvStatsHistInstanceId_Type()
)
cfprApMemoryBufferUnitEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistInstanceId.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistDn_Type = CfprApManagedObjectDn
_CfprApMemoryBufferUnitEnvStatsHistDn_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistDn = _CfprApMemoryBufferUnitEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 2),
    _CfprApMemoryBufferUnitEnvStatsHistDn_Type()
)
cfprApMemoryBufferUnitEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistDn.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistRn_Type = SnmpAdminString
_CfprApMemoryBufferUnitEnvStatsHistRn_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistRn = _CfprApMemoryBufferUnitEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 3),
    _CfprApMemoryBufferUnitEnvStatsHistRn_Type()
)
cfprApMemoryBufferUnitEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistRn.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistId_Type = Unsigned64
_CfprApMemoryBufferUnitEnvStatsHistId_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistId = _CfprApMemoryBufferUnitEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 4),
    _CfprApMemoryBufferUnitEnvStatsHistId_Type()
)
cfprApMemoryBufferUnitEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistId.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistMostRecent_Type = TruthValue
_CfprApMemoryBufferUnitEnvStatsHistMostRecent_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistMostRecent = _CfprApMemoryBufferUnitEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 5),
    _CfprApMemoryBufferUnitEnvStatsHistMostRecent_Type()
)
cfprApMemoryBufferUnitEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistMostRecent.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistSuspect_Type = TruthValue
_CfprApMemoryBufferUnitEnvStatsHistSuspect_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistSuspect = _CfprApMemoryBufferUnitEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 6),
    _CfprApMemoryBufferUnitEnvStatsHistSuspect_Type()
)
cfprApMemoryBufferUnitEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistSuspect.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistTemperature_Type = Integer32
_CfprApMemoryBufferUnitEnvStatsHistTemperature_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistTemperature = _CfprApMemoryBufferUnitEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 7),
    _CfprApMemoryBufferUnitEnvStatsHistTemperature_Type()
)
cfprApMemoryBufferUnitEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistTemperature.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistTemperatureAvg_Type = Integer32
_CfprApMemoryBufferUnitEnvStatsHistTemperatureAvg_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistTemperatureAvg = _CfprApMemoryBufferUnitEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 8),
    _CfprApMemoryBufferUnitEnvStatsHistTemperatureAvg_Type()
)
cfprApMemoryBufferUnitEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistTemperatureAvg.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistTemperatureMax_Type = Integer32
_CfprApMemoryBufferUnitEnvStatsHistTemperatureMax_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistTemperatureMax = _CfprApMemoryBufferUnitEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 9),
    _CfprApMemoryBufferUnitEnvStatsHistTemperatureMax_Type()
)
cfprApMemoryBufferUnitEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistTemperatureMax.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistTemperatureMin_Type = Integer32
_CfprApMemoryBufferUnitEnvStatsHistTemperatureMin_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistTemperatureMin = _CfprApMemoryBufferUnitEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 10),
    _CfprApMemoryBufferUnitEnvStatsHistTemperatureMin_Type()
)
cfprApMemoryBufferUnitEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistTemperatureMin.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistThresholded_Type = CfprApMemoryBufferUnitEnvStatsHistThresholded
_CfprApMemoryBufferUnitEnvStatsHistThresholded_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistThresholded = _CfprApMemoryBufferUnitEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 11),
    _CfprApMemoryBufferUnitEnvStatsHistThresholded_Type()
)
cfprApMemoryBufferUnitEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistThresholded.setStatus("current")
_CfprApMemoryBufferUnitEnvStatsHistTimeCollected_Type = DateAndTime
_CfprApMemoryBufferUnitEnvStatsHistTimeCollected_Object = MibTableColumn
cfprApMemoryBufferUnitEnvStatsHistTimeCollected = _CfprApMemoryBufferUnitEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 6, 1, 12),
    _CfprApMemoryBufferUnitEnvStatsHistTimeCollected_Type()
)
cfprApMemoryBufferUnitEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryBufferUnitEnvStatsHistTimeCollected.setStatus("current")
_CfprApMemoryErrorStatsTable_Object = MibTable
cfprApMemoryErrorStatsTable = _CfprApMemoryErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7)
)
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsTable.setStatus("current")
_CfprApMemoryErrorStatsEntry_Object = MibTableRow
cfprApMemoryErrorStatsEntry = _CfprApMemoryErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1)
)
cfprApMemoryErrorStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryErrorStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEntry.setStatus("current")
_CfprApMemoryErrorStatsInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryErrorStatsInstanceId_Object = MibTableColumn
cfprApMemoryErrorStatsInstanceId = _CfprApMemoryErrorStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 1),
    _CfprApMemoryErrorStatsInstanceId_Type()
)
cfprApMemoryErrorStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsInstanceId.setStatus("current")
_CfprApMemoryErrorStatsDn_Type = CfprApManagedObjectDn
_CfprApMemoryErrorStatsDn_Object = MibTableColumn
cfprApMemoryErrorStatsDn = _CfprApMemoryErrorStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 2),
    _CfprApMemoryErrorStatsDn_Type()
)
cfprApMemoryErrorStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsDn.setStatus("current")
_CfprApMemoryErrorStatsRn_Type = SnmpAdminString
_CfprApMemoryErrorStatsRn_Object = MibTableColumn
cfprApMemoryErrorStatsRn = _CfprApMemoryErrorStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 3),
    _CfprApMemoryErrorStatsRn_Type()
)
cfprApMemoryErrorStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsRn.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors_Type = Counter32
_CfprApMemoryErrorStatsAddressParityErrors_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors = _CfprApMemoryErrorStatsAddressParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 4),
    _CfprApMemoryErrorStatsAddressParityErrors_Type()
)
cfprApMemoryErrorStatsAddressParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors15Min_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors15Min_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors15Min = _CfprApMemoryErrorStatsAddressParityErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 5),
    _CfprApMemoryErrorStatsAddressParityErrors15Min_Type()
)
cfprApMemoryErrorStatsAddressParityErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors15Min.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors15MinH_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors15MinH_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors15MinH = _CfprApMemoryErrorStatsAddressParityErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 6),
    _CfprApMemoryErrorStatsAddressParityErrors15MinH_Type()
)
cfprApMemoryErrorStatsAddressParityErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors15MinH.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors1Day_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors1Day_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors1Day = _CfprApMemoryErrorStatsAddressParityErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 7),
    _CfprApMemoryErrorStatsAddressParityErrors1Day_Type()
)
cfprApMemoryErrorStatsAddressParityErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors1Day.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors1DayH_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors1DayH_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors1DayH = _CfprApMemoryErrorStatsAddressParityErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 8),
    _CfprApMemoryErrorStatsAddressParityErrors1DayH_Type()
)
cfprApMemoryErrorStatsAddressParityErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors1DayH.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors1Hour_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors1Hour_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors1Hour = _CfprApMemoryErrorStatsAddressParityErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 9),
    _CfprApMemoryErrorStatsAddressParityErrors1Hour_Type()
)
cfprApMemoryErrorStatsAddressParityErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors1Hour.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors1HourH_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors1HourH_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors1HourH = _CfprApMemoryErrorStatsAddressParityErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 10),
    _CfprApMemoryErrorStatsAddressParityErrors1HourH_Type()
)
cfprApMemoryErrorStatsAddressParityErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors1HourH.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors1Week_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors1Week_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors1Week = _CfprApMemoryErrorStatsAddressParityErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 11),
    _CfprApMemoryErrorStatsAddressParityErrors1Week_Type()
)
cfprApMemoryErrorStatsAddressParityErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors1Week.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors1WeekH_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors1WeekH_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors1WeekH = _CfprApMemoryErrorStatsAddressParityErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 12),
    _CfprApMemoryErrorStatsAddressParityErrors1WeekH_Type()
)
cfprApMemoryErrorStatsAddressParityErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors1WeekH.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors2Weeks_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors2Weeks_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors2Weeks = _CfprApMemoryErrorStatsAddressParityErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 13),
    _CfprApMemoryErrorStatsAddressParityErrors2Weeks_Type()
)
cfprApMemoryErrorStatsAddressParityErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors2Weeks.setStatus("current")
_CfprApMemoryErrorStatsAddressParityErrors2WeeksH_Type = Gauge32
_CfprApMemoryErrorStatsAddressParityErrors2WeeksH_Object = MibTableColumn
cfprApMemoryErrorStatsAddressParityErrors2WeeksH = _CfprApMemoryErrorStatsAddressParityErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 14),
    _CfprApMemoryErrorStatsAddressParityErrors2WeeksH_Type()
)
cfprApMemoryErrorStatsAddressParityErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsAddressParityErrors2WeeksH.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors_Type = Counter32
_CfprApMemoryErrorStatsEccMultibitErrors_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors = _CfprApMemoryErrorStatsEccMultibitErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 15),
    _CfprApMemoryErrorStatsEccMultibitErrors_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors15Min_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors15Min_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors15Min = _CfprApMemoryErrorStatsEccMultibitErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 16),
    _CfprApMemoryErrorStatsEccMultibitErrors15Min_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors15Min.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors15MinH_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors15MinH_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors15MinH = _CfprApMemoryErrorStatsEccMultibitErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 17),
    _CfprApMemoryErrorStatsEccMultibitErrors15MinH_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors15MinH.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors1Day_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors1Day_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors1Day = _CfprApMemoryErrorStatsEccMultibitErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 18),
    _CfprApMemoryErrorStatsEccMultibitErrors1Day_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors1Day.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors1DayH_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors1DayH_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors1DayH = _CfprApMemoryErrorStatsEccMultibitErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 19),
    _CfprApMemoryErrorStatsEccMultibitErrors1DayH_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors1DayH.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors1Hour_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors1Hour_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors1Hour = _CfprApMemoryErrorStatsEccMultibitErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 20),
    _CfprApMemoryErrorStatsEccMultibitErrors1Hour_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors1Hour.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors1HourH_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors1HourH_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors1HourH = _CfprApMemoryErrorStatsEccMultibitErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 21),
    _CfprApMemoryErrorStatsEccMultibitErrors1HourH_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors1HourH.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors1Week_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors1Week_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors1Week = _CfprApMemoryErrorStatsEccMultibitErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 22),
    _CfprApMemoryErrorStatsEccMultibitErrors1Week_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors1Week.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors1WeekH_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors1WeekH_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors1WeekH = _CfprApMemoryErrorStatsEccMultibitErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 23),
    _CfprApMemoryErrorStatsEccMultibitErrors1WeekH_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors1WeekH.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors2Weeks_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors2Weeks_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors2Weeks = _CfprApMemoryErrorStatsEccMultibitErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 24),
    _CfprApMemoryErrorStatsEccMultibitErrors2Weeks_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors2Weeks.setStatus("current")
_CfprApMemoryErrorStatsEccMultibitErrors2WeeksH_Type = Gauge32
_CfprApMemoryErrorStatsEccMultibitErrors2WeeksH_Object = MibTableColumn
cfprApMemoryErrorStatsEccMultibitErrors2WeeksH = _CfprApMemoryErrorStatsEccMultibitErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 25),
    _CfprApMemoryErrorStatsEccMultibitErrors2WeeksH_Type()
)
cfprApMemoryErrorStatsEccMultibitErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccMultibitErrors2WeeksH.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors_Type = Counter32
_CfprApMemoryErrorStatsEccSinglebitErrors_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors = _CfprApMemoryErrorStatsEccSinglebitErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 26),
    _CfprApMemoryErrorStatsEccSinglebitErrors_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors15Min_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors15Min_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors15Min = _CfprApMemoryErrorStatsEccSinglebitErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 27),
    _CfprApMemoryErrorStatsEccSinglebitErrors15Min_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors15Min.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors15MinH_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors15MinH_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors15MinH = _CfprApMemoryErrorStatsEccSinglebitErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 28),
    _CfprApMemoryErrorStatsEccSinglebitErrors15MinH_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors15MinH.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors1Day_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors1Day_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors1Day = _CfprApMemoryErrorStatsEccSinglebitErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 29),
    _CfprApMemoryErrorStatsEccSinglebitErrors1Day_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors1Day.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors1DayH_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors1DayH_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors1DayH = _CfprApMemoryErrorStatsEccSinglebitErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 30),
    _CfprApMemoryErrorStatsEccSinglebitErrors1DayH_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors1DayH.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors1Hour_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors1Hour_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors1Hour = _CfprApMemoryErrorStatsEccSinglebitErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 31),
    _CfprApMemoryErrorStatsEccSinglebitErrors1Hour_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors1Hour.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors1HourH_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors1HourH_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors1HourH = _CfprApMemoryErrorStatsEccSinglebitErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 32),
    _CfprApMemoryErrorStatsEccSinglebitErrors1HourH_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors1HourH.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors1Week_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors1Week_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors1Week = _CfprApMemoryErrorStatsEccSinglebitErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 33),
    _CfprApMemoryErrorStatsEccSinglebitErrors1Week_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors1Week.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors1WeekH_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors1WeekH_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors1WeekH = _CfprApMemoryErrorStatsEccSinglebitErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 34),
    _CfprApMemoryErrorStatsEccSinglebitErrors1WeekH_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors1WeekH.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors2Weeks_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors2Weeks_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors2Weeks = _CfprApMemoryErrorStatsEccSinglebitErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 35),
    _CfprApMemoryErrorStatsEccSinglebitErrors2Weeks_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors2Weeks.setStatus("current")
_CfprApMemoryErrorStatsEccSinglebitErrors2WeeksH_Type = Gauge32
_CfprApMemoryErrorStatsEccSinglebitErrors2WeeksH_Object = MibTableColumn
cfprApMemoryErrorStatsEccSinglebitErrors2WeeksH = _CfprApMemoryErrorStatsEccSinglebitErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 36),
    _CfprApMemoryErrorStatsEccSinglebitErrors2WeeksH_Type()
)
cfprApMemoryErrorStatsEccSinglebitErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsEccSinglebitErrors2WeeksH.setStatus("current")
_CfprApMemoryErrorStatsIntervals_Type = Gauge32
_CfprApMemoryErrorStatsIntervals_Object = MibTableColumn
cfprApMemoryErrorStatsIntervals = _CfprApMemoryErrorStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 37),
    _CfprApMemoryErrorStatsIntervals_Type()
)
cfprApMemoryErrorStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsIntervals.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors_Type = Counter32
_CfprApMemoryErrorStatsMismatchErrors_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors = _CfprApMemoryErrorStatsMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 38),
    _CfprApMemoryErrorStatsMismatchErrors_Type()
)
cfprApMemoryErrorStatsMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors15Min_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors15Min_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors15Min = _CfprApMemoryErrorStatsMismatchErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 39),
    _CfprApMemoryErrorStatsMismatchErrors15Min_Type()
)
cfprApMemoryErrorStatsMismatchErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors15Min.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors15MinH_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors15MinH_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors15MinH = _CfprApMemoryErrorStatsMismatchErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 40),
    _CfprApMemoryErrorStatsMismatchErrors15MinH_Type()
)
cfprApMemoryErrorStatsMismatchErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors15MinH.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors1Day_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors1Day_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors1Day = _CfprApMemoryErrorStatsMismatchErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 41),
    _CfprApMemoryErrorStatsMismatchErrors1Day_Type()
)
cfprApMemoryErrorStatsMismatchErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors1Day.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors1DayH_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors1DayH_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors1DayH = _CfprApMemoryErrorStatsMismatchErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 42),
    _CfprApMemoryErrorStatsMismatchErrors1DayH_Type()
)
cfprApMemoryErrorStatsMismatchErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors1DayH.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors1Hour_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors1Hour_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors1Hour = _CfprApMemoryErrorStatsMismatchErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 43),
    _CfprApMemoryErrorStatsMismatchErrors1Hour_Type()
)
cfprApMemoryErrorStatsMismatchErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors1Hour.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors1HourH_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors1HourH_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors1HourH = _CfprApMemoryErrorStatsMismatchErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 44),
    _CfprApMemoryErrorStatsMismatchErrors1HourH_Type()
)
cfprApMemoryErrorStatsMismatchErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors1HourH.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors1Week_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors1Week_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors1Week = _CfprApMemoryErrorStatsMismatchErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 45),
    _CfprApMemoryErrorStatsMismatchErrors1Week_Type()
)
cfprApMemoryErrorStatsMismatchErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors1Week.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors1WeekH_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors1WeekH_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors1WeekH = _CfprApMemoryErrorStatsMismatchErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 46),
    _CfprApMemoryErrorStatsMismatchErrors1WeekH_Type()
)
cfprApMemoryErrorStatsMismatchErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors1WeekH.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors2Weeks_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors2Weeks_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors2Weeks = _CfprApMemoryErrorStatsMismatchErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 47),
    _CfprApMemoryErrorStatsMismatchErrors2Weeks_Type()
)
cfprApMemoryErrorStatsMismatchErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors2Weeks.setStatus("current")
_CfprApMemoryErrorStatsMismatchErrors2WeeksH_Type = Gauge32
_CfprApMemoryErrorStatsMismatchErrors2WeeksH_Object = MibTableColumn
cfprApMemoryErrorStatsMismatchErrors2WeeksH = _CfprApMemoryErrorStatsMismatchErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 48),
    _CfprApMemoryErrorStatsMismatchErrors2WeeksH_Type()
)
cfprApMemoryErrorStatsMismatchErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsMismatchErrors2WeeksH.setStatus("current")
_CfprApMemoryErrorStatsSuspect_Type = TruthValue
_CfprApMemoryErrorStatsSuspect_Object = MibTableColumn
cfprApMemoryErrorStatsSuspect = _CfprApMemoryErrorStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 49),
    _CfprApMemoryErrorStatsSuspect_Type()
)
cfprApMemoryErrorStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsSuspect.setStatus("current")
_CfprApMemoryErrorStatsThresholded_Type = CfprApMemoryErrorStatsThresholded
_CfprApMemoryErrorStatsThresholded_Object = MibTableColumn
cfprApMemoryErrorStatsThresholded = _CfprApMemoryErrorStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 50),
    _CfprApMemoryErrorStatsThresholded_Type()
)
cfprApMemoryErrorStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsThresholded.setStatus("current")
_CfprApMemoryErrorStatsTimeCollected_Type = DateAndTime
_CfprApMemoryErrorStatsTimeCollected_Object = MibTableColumn
cfprApMemoryErrorStatsTimeCollected = _CfprApMemoryErrorStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 51),
    _CfprApMemoryErrorStatsTimeCollected_Type()
)
cfprApMemoryErrorStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsTimeCollected.setStatus("current")
_CfprApMemoryErrorStatsUpdate_Type = Gauge32
_CfprApMemoryErrorStatsUpdate_Object = MibTableColumn
cfprApMemoryErrorStatsUpdate = _CfprApMemoryErrorStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 7, 1, 52),
    _CfprApMemoryErrorStatsUpdate_Type()
)
cfprApMemoryErrorStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryErrorStatsUpdate.setStatus("current")
_CfprApMemoryQualTable_Object = MibTable
cfprApMemoryQualTable = _CfprApMemoryQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8)
)
if mibBuilder.loadTexts:
    cfprApMemoryQualTable.setStatus("current")
_CfprApMemoryQualEntry_Object = MibTableRow
cfprApMemoryQualEntry = _CfprApMemoryQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1)
)
cfprApMemoryQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryQualEntry.setStatus("current")
_CfprApMemoryQualInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryQualInstanceId_Object = MibTableColumn
cfprApMemoryQualInstanceId = _CfprApMemoryQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 1),
    _CfprApMemoryQualInstanceId_Type()
)
cfprApMemoryQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryQualInstanceId.setStatus("current")
_CfprApMemoryQualDn_Type = CfprApManagedObjectDn
_CfprApMemoryQualDn_Object = MibTableColumn
cfprApMemoryQualDn = _CfprApMemoryQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 2),
    _CfprApMemoryQualDn_Type()
)
cfprApMemoryQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualDn.setStatus("current")
_CfprApMemoryQualRn_Type = SnmpAdminString
_CfprApMemoryQualRn_Object = MibTableColumn
cfprApMemoryQualRn = _CfprApMemoryQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 3),
    _CfprApMemoryQualRn_Type()
)
cfprApMemoryQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualRn.setStatus("current")
_CfprApMemoryQualClock_Type = Gauge32
_CfprApMemoryQualClock_Object = MibTableColumn
cfprApMemoryQualClock = _CfprApMemoryQualClock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 4),
    _CfprApMemoryQualClock_Type()
)
cfprApMemoryQualClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualClock.setStatus("current")
_CfprApMemoryQualLatency_Type = Integer32
_CfprApMemoryQualLatency_Object = MibTableColumn
cfprApMemoryQualLatency = _CfprApMemoryQualLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 5),
    _CfprApMemoryQualLatency_Type()
)
cfprApMemoryQualLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualLatency.setStatus("current")
_CfprApMemoryQualMaxCap_Type = Gauge32
_CfprApMemoryQualMaxCap_Object = MibTableColumn
cfprApMemoryQualMaxCap = _CfprApMemoryQualMaxCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 6),
    _CfprApMemoryQualMaxCap_Type()
)
cfprApMemoryQualMaxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualMaxCap.setStatus("current")
_CfprApMemoryQualMinCap_Type = Gauge32
_CfprApMemoryQualMinCap_Object = MibTableColumn
cfprApMemoryQualMinCap = _CfprApMemoryQualMinCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 7),
    _CfprApMemoryQualMinCap_Type()
)
cfprApMemoryQualMinCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualMinCap.setStatus("current")
_CfprApMemoryQualSpeed_Type = Gauge32
_CfprApMemoryQualSpeed_Object = MibTableColumn
cfprApMemoryQualSpeed = _CfprApMemoryQualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 8),
    _CfprApMemoryQualSpeed_Type()
)
cfprApMemoryQualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualSpeed.setStatus("current")
_CfprApMemoryQualUnits_Type = Gauge32
_CfprApMemoryQualUnits_Object = MibTableColumn
cfprApMemoryQualUnits = _CfprApMemoryQualUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 9),
    _CfprApMemoryQualUnits_Type()
)
cfprApMemoryQualUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualUnits.setStatus("current")
_CfprApMemoryQualWidth_Type = Gauge32
_CfprApMemoryQualWidth_Object = MibTableColumn
cfprApMemoryQualWidth = _CfprApMemoryQualWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 8, 1, 10),
    _CfprApMemoryQualWidth_Type()
)
cfprApMemoryQualWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryQualWidth.setStatus("current")
_CfprApMemoryRuntimeTable_Object = MibTable
cfprApMemoryRuntimeTable = _CfprApMemoryRuntimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9)
)
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeTable.setStatus("current")
_CfprApMemoryRuntimeEntry_Object = MibTableRow
cfprApMemoryRuntimeEntry = _CfprApMemoryRuntimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1)
)
cfprApMemoryRuntimeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryRuntimeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeEntry.setStatus("current")
_CfprApMemoryRuntimeInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryRuntimeInstanceId_Object = MibTableColumn
cfprApMemoryRuntimeInstanceId = _CfprApMemoryRuntimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 1),
    _CfprApMemoryRuntimeInstanceId_Type()
)
cfprApMemoryRuntimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeInstanceId.setStatus("current")
_CfprApMemoryRuntimeDn_Type = CfprApManagedObjectDn
_CfprApMemoryRuntimeDn_Object = MibTableColumn
cfprApMemoryRuntimeDn = _CfprApMemoryRuntimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 2),
    _CfprApMemoryRuntimeDn_Type()
)
cfprApMemoryRuntimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeDn.setStatus("current")
_CfprApMemoryRuntimeRn_Type = SnmpAdminString
_CfprApMemoryRuntimeRn_Object = MibTableColumn
cfprApMemoryRuntimeRn = _CfprApMemoryRuntimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 3),
    _CfprApMemoryRuntimeRn_Type()
)
cfprApMemoryRuntimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeRn.setStatus("current")
_CfprApMemoryRuntimeAvailable_Type = Gauge32
_CfprApMemoryRuntimeAvailable_Object = MibTableColumn
cfprApMemoryRuntimeAvailable = _CfprApMemoryRuntimeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 4),
    _CfprApMemoryRuntimeAvailable_Type()
)
cfprApMemoryRuntimeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeAvailable.setStatus("current")
_CfprApMemoryRuntimeAvailableAvg_Type = Gauge32
_CfprApMemoryRuntimeAvailableAvg_Object = MibTableColumn
cfprApMemoryRuntimeAvailableAvg = _CfprApMemoryRuntimeAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 5),
    _CfprApMemoryRuntimeAvailableAvg_Type()
)
cfprApMemoryRuntimeAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeAvailableAvg.setStatus("current")
_CfprApMemoryRuntimeAvailableMax_Type = Gauge32
_CfprApMemoryRuntimeAvailableMax_Object = MibTableColumn
cfprApMemoryRuntimeAvailableMax = _CfprApMemoryRuntimeAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 6),
    _CfprApMemoryRuntimeAvailableMax_Type()
)
cfprApMemoryRuntimeAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeAvailableMax.setStatus("current")
_CfprApMemoryRuntimeAvailableMin_Type = Gauge32
_CfprApMemoryRuntimeAvailableMin_Object = MibTableColumn
cfprApMemoryRuntimeAvailableMin = _CfprApMemoryRuntimeAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 7),
    _CfprApMemoryRuntimeAvailableMin_Type()
)
cfprApMemoryRuntimeAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeAvailableMin.setStatus("current")
_CfprApMemoryRuntimeCached_Type = Gauge32
_CfprApMemoryRuntimeCached_Object = MibTableColumn
cfprApMemoryRuntimeCached = _CfprApMemoryRuntimeCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 8),
    _CfprApMemoryRuntimeCached_Type()
)
cfprApMemoryRuntimeCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeCached.setStatus("current")
_CfprApMemoryRuntimeCachedAvg_Type = Gauge32
_CfprApMemoryRuntimeCachedAvg_Object = MibTableColumn
cfprApMemoryRuntimeCachedAvg = _CfprApMemoryRuntimeCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 9),
    _CfprApMemoryRuntimeCachedAvg_Type()
)
cfprApMemoryRuntimeCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeCachedAvg.setStatus("current")
_CfprApMemoryRuntimeCachedMax_Type = Gauge32
_CfprApMemoryRuntimeCachedMax_Object = MibTableColumn
cfprApMemoryRuntimeCachedMax = _CfprApMemoryRuntimeCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 10),
    _CfprApMemoryRuntimeCachedMax_Type()
)
cfprApMemoryRuntimeCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeCachedMax.setStatus("current")
_CfprApMemoryRuntimeCachedMin_Type = Gauge32
_CfprApMemoryRuntimeCachedMin_Object = MibTableColumn
cfprApMemoryRuntimeCachedMin = _CfprApMemoryRuntimeCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 11),
    _CfprApMemoryRuntimeCachedMin_Type()
)
cfprApMemoryRuntimeCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeCachedMin.setStatus("current")
_CfprApMemoryRuntimeIntervals_Type = Gauge32
_CfprApMemoryRuntimeIntervals_Object = MibTableColumn
cfprApMemoryRuntimeIntervals = _CfprApMemoryRuntimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 12),
    _CfprApMemoryRuntimeIntervals_Type()
)
cfprApMemoryRuntimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeIntervals.setStatus("current")
_CfprApMemoryRuntimeSuspect_Type = TruthValue
_CfprApMemoryRuntimeSuspect_Object = MibTableColumn
cfprApMemoryRuntimeSuspect = _CfprApMemoryRuntimeSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 13),
    _CfprApMemoryRuntimeSuspect_Type()
)
cfprApMemoryRuntimeSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeSuspect.setStatus("current")
_CfprApMemoryRuntimeThresholded_Type = CfprApMemoryRuntimeThresholded
_CfprApMemoryRuntimeThresholded_Object = MibTableColumn
cfprApMemoryRuntimeThresholded = _CfprApMemoryRuntimeThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 14),
    _CfprApMemoryRuntimeThresholded_Type()
)
cfprApMemoryRuntimeThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeThresholded.setStatus("current")
_CfprApMemoryRuntimeTimeCollected_Type = DateAndTime
_CfprApMemoryRuntimeTimeCollected_Object = MibTableColumn
cfprApMemoryRuntimeTimeCollected = _CfprApMemoryRuntimeTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 15),
    _CfprApMemoryRuntimeTimeCollected_Type()
)
cfprApMemoryRuntimeTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeTimeCollected.setStatus("current")
_CfprApMemoryRuntimeTotal_Type = Gauge32
_CfprApMemoryRuntimeTotal_Object = MibTableColumn
cfprApMemoryRuntimeTotal = _CfprApMemoryRuntimeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 16),
    _CfprApMemoryRuntimeTotal_Type()
)
cfprApMemoryRuntimeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeTotal.setStatus("current")
_CfprApMemoryRuntimeTotalAvg_Type = Gauge32
_CfprApMemoryRuntimeTotalAvg_Object = MibTableColumn
cfprApMemoryRuntimeTotalAvg = _CfprApMemoryRuntimeTotalAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 17),
    _CfprApMemoryRuntimeTotalAvg_Type()
)
cfprApMemoryRuntimeTotalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeTotalAvg.setStatus("current")
_CfprApMemoryRuntimeTotalMax_Type = Gauge32
_CfprApMemoryRuntimeTotalMax_Object = MibTableColumn
cfprApMemoryRuntimeTotalMax = _CfprApMemoryRuntimeTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 18),
    _CfprApMemoryRuntimeTotalMax_Type()
)
cfprApMemoryRuntimeTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeTotalMax.setStatus("current")
_CfprApMemoryRuntimeTotalMin_Type = Gauge32
_CfprApMemoryRuntimeTotalMin_Object = MibTableColumn
cfprApMemoryRuntimeTotalMin = _CfprApMemoryRuntimeTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 19),
    _CfprApMemoryRuntimeTotalMin_Type()
)
cfprApMemoryRuntimeTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeTotalMin.setStatus("current")
_CfprApMemoryRuntimeType_Type = CfprApMemoryRuntimeType
_CfprApMemoryRuntimeType_Object = MibTableColumn
cfprApMemoryRuntimeType = _CfprApMemoryRuntimeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 20),
    _CfprApMemoryRuntimeType_Type()
)
cfprApMemoryRuntimeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeType.setStatus("current")
_CfprApMemoryRuntimeUpdate_Type = Gauge32
_CfprApMemoryRuntimeUpdate_Object = MibTableColumn
cfprApMemoryRuntimeUpdate = _CfprApMemoryRuntimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 9, 1, 21),
    _CfprApMemoryRuntimeUpdate_Type()
)
cfprApMemoryRuntimeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeUpdate.setStatus("current")
_CfprApMemoryRuntimeHistTable_Object = MibTable
cfprApMemoryRuntimeHistTable = _CfprApMemoryRuntimeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10)
)
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistTable.setStatus("current")
_CfprApMemoryRuntimeHistEntry_Object = MibTableRow
cfprApMemoryRuntimeHistEntry = _CfprApMemoryRuntimeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1)
)
cfprApMemoryRuntimeHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryRuntimeHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistEntry.setStatus("current")
_CfprApMemoryRuntimeHistInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryRuntimeHistInstanceId_Object = MibTableColumn
cfprApMemoryRuntimeHistInstanceId = _CfprApMemoryRuntimeHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 1),
    _CfprApMemoryRuntimeHistInstanceId_Type()
)
cfprApMemoryRuntimeHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistInstanceId.setStatus("current")
_CfprApMemoryRuntimeHistDn_Type = CfprApManagedObjectDn
_CfprApMemoryRuntimeHistDn_Object = MibTableColumn
cfprApMemoryRuntimeHistDn = _CfprApMemoryRuntimeHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 2),
    _CfprApMemoryRuntimeHistDn_Type()
)
cfprApMemoryRuntimeHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistDn.setStatus("current")
_CfprApMemoryRuntimeHistRn_Type = SnmpAdminString
_CfprApMemoryRuntimeHistRn_Object = MibTableColumn
cfprApMemoryRuntimeHistRn = _CfprApMemoryRuntimeHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 3),
    _CfprApMemoryRuntimeHistRn_Type()
)
cfprApMemoryRuntimeHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistRn.setStatus("current")
_CfprApMemoryRuntimeHistAvailable_Type = Gauge32
_CfprApMemoryRuntimeHistAvailable_Object = MibTableColumn
cfprApMemoryRuntimeHistAvailable = _CfprApMemoryRuntimeHistAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 4),
    _CfprApMemoryRuntimeHistAvailable_Type()
)
cfprApMemoryRuntimeHistAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistAvailable.setStatus("current")
_CfprApMemoryRuntimeHistAvailableAvg_Type = Gauge32
_CfprApMemoryRuntimeHistAvailableAvg_Object = MibTableColumn
cfprApMemoryRuntimeHistAvailableAvg = _CfprApMemoryRuntimeHistAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 5),
    _CfprApMemoryRuntimeHistAvailableAvg_Type()
)
cfprApMemoryRuntimeHistAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistAvailableAvg.setStatus("current")
_CfprApMemoryRuntimeHistAvailableMax_Type = Gauge32
_CfprApMemoryRuntimeHistAvailableMax_Object = MibTableColumn
cfprApMemoryRuntimeHistAvailableMax = _CfprApMemoryRuntimeHistAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 6),
    _CfprApMemoryRuntimeHistAvailableMax_Type()
)
cfprApMemoryRuntimeHistAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistAvailableMax.setStatus("current")
_CfprApMemoryRuntimeHistAvailableMin_Type = Gauge32
_CfprApMemoryRuntimeHistAvailableMin_Object = MibTableColumn
cfprApMemoryRuntimeHistAvailableMin = _CfprApMemoryRuntimeHistAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 7),
    _CfprApMemoryRuntimeHistAvailableMin_Type()
)
cfprApMemoryRuntimeHistAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistAvailableMin.setStatus("current")
_CfprApMemoryRuntimeHistCached_Type = Gauge32
_CfprApMemoryRuntimeHistCached_Object = MibTableColumn
cfprApMemoryRuntimeHistCached = _CfprApMemoryRuntimeHistCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 8),
    _CfprApMemoryRuntimeHistCached_Type()
)
cfprApMemoryRuntimeHistCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistCached.setStatus("current")
_CfprApMemoryRuntimeHistCachedAvg_Type = Gauge32
_CfprApMemoryRuntimeHistCachedAvg_Object = MibTableColumn
cfprApMemoryRuntimeHistCachedAvg = _CfprApMemoryRuntimeHistCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 9),
    _CfprApMemoryRuntimeHistCachedAvg_Type()
)
cfprApMemoryRuntimeHistCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistCachedAvg.setStatus("current")
_CfprApMemoryRuntimeHistCachedMax_Type = Gauge32
_CfprApMemoryRuntimeHistCachedMax_Object = MibTableColumn
cfprApMemoryRuntimeHistCachedMax = _CfprApMemoryRuntimeHistCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 10),
    _CfprApMemoryRuntimeHistCachedMax_Type()
)
cfprApMemoryRuntimeHistCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistCachedMax.setStatus("current")
_CfprApMemoryRuntimeHistCachedMin_Type = Gauge32
_CfprApMemoryRuntimeHistCachedMin_Object = MibTableColumn
cfprApMemoryRuntimeHistCachedMin = _CfprApMemoryRuntimeHistCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 11),
    _CfprApMemoryRuntimeHistCachedMin_Type()
)
cfprApMemoryRuntimeHistCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistCachedMin.setStatus("current")
_CfprApMemoryRuntimeHistId_Type = Unsigned64
_CfprApMemoryRuntimeHistId_Object = MibTableColumn
cfprApMemoryRuntimeHistId = _CfprApMemoryRuntimeHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 12),
    _CfprApMemoryRuntimeHistId_Type()
)
cfprApMemoryRuntimeHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistId.setStatus("current")
_CfprApMemoryRuntimeHistMostRecent_Type = TruthValue
_CfprApMemoryRuntimeHistMostRecent_Object = MibTableColumn
cfprApMemoryRuntimeHistMostRecent = _CfprApMemoryRuntimeHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 13),
    _CfprApMemoryRuntimeHistMostRecent_Type()
)
cfprApMemoryRuntimeHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistMostRecent.setStatus("current")
_CfprApMemoryRuntimeHistSuspect_Type = TruthValue
_CfprApMemoryRuntimeHistSuspect_Object = MibTableColumn
cfprApMemoryRuntimeHistSuspect = _CfprApMemoryRuntimeHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 14),
    _CfprApMemoryRuntimeHistSuspect_Type()
)
cfprApMemoryRuntimeHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistSuspect.setStatus("current")
_CfprApMemoryRuntimeHistThresholded_Type = CfprApMemoryRuntimeHistThresholded
_CfprApMemoryRuntimeHistThresholded_Object = MibTableColumn
cfprApMemoryRuntimeHistThresholded = _CfprApMemoryRuntimeHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 15),
    _CfprApMemoryRuntimeHistThresholded_Type()
)
cfprApMemoryRuntimeHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistThresholded.setStatus("current")
_CfprApMemoryRuntimeHistTimeCollected_Type = DateAndTime
_CfprApMemoryRuntimeHistTimeCollected_Object = MibTableColumn
cfprApMemoryRuntimeHistTimeCollected = _CfprApMemoryRuntimeHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 16),
    _CfprApMemoryRuntimeHistTimeCollected_Type()
)
cfprApMemoryRuntimeHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistTimeCollected.setStatus("current")
_CfprApMemoryRuntimeHistTotal_Type = Gauge32
_CfprApMemoryRuntimeHistTotal_Object = MibTableColumn
cfprApMemoryRuntimeHistTotal = _CfprApMemoryRuntimeHistTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 17),
    _CfprApMemoryRuntimeHistTotal_Type()
)
cfprApMemoryRuntimeHistTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistTotal.setStatus("current")
_CfprApMemoryRuntimeHistTotalAvg_Type = Gauge32
_CfprApMemoryRuntimeHistTotalAvg_Object = MibTableColumn
cfprApMemoryRuntimeHistTotalAvg = _CfprApMemoryRuntimeHistTotalAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 18),
    _CfprApMemoryRuntimeHistTotalAvg_Type()
)
cfprApMemoryRuntimeHistTotalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistTotalAvg.setStatus("current")
_CfprApMemoryRuntimeHistTotalMax_Type = Gauge32
_CfprApMemoryRuntimeHistTotalMax_Object = MibTableColumn
cfprApMemoryRuntimeHistTotalMax = _CfprApMemoryRuntimeHistTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 19),
    _CfprApMemoryRuntimeHistTotalMax_Type()
)
cfprApMemoryRuntimeHistTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistTotalMax.setStatus("current")
_CfprApMemoryRuntimeHistTotalMin_Type = Gauge32
_CfprApMemoryRuntimeHistTotalMin_Object = MibTableColumn
cfprApMemoryRuntimeHistTotalMin = _CfprApMemoryRuntimeHistTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 10, 1, 20),
    _CfprApMemoryRuntimeHistTotalMin_Type()
)
cfprApMemoryRuntimeHistTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryRuntimeHistTotalMin.setStatus("current")
_CfprApMemoryUnitTable_Object = MibTable
cfprApMemoryUnitTable = _CfprApMemoryUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11)
)
if mibBuilder.loadTexts:
    cfprApMemoryUnitTable.setStatus("current")
_CfprApMemoryUnitEntry_Object = MibTableRow
cfprApMemoryUnitEntry = _CfprApMemoryUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1)
)
cfprApMemoryUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryUnitEntry.setStatus("current")
_CfprApMemoryUnitInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryUnitInstanceId_Object = MibTableColumn
cfprApMemoryUnitInstanceId = _CfprApMemoryUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 1),
    _CfprApMemoryUnitInstanceId_Type()
)
cfprApMemoryUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryUnitInstanceId.setStatus("current")
_CfprApMemoryUnitDn_Type = CfprApManagedObjectDn
_CfprApMemoryUnitDn_Object = MibTableColumn
cfprApMemoryUnitDn = _CfprApMemoryUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 2),
    _CfprApMemoryUnitDn_Type()
)
cfprApMemoryUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitDn.setStatus("current")
_CfprApMemoryUnitRn_Type = SnmpAdminString
_CfprApMemoryUnitRn_Object = MibTableColumn
cfprApMemoryUnitRn = _CfprApMemoryUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 3),
    _CfprApMemoryUnitRn_Type()
)
cfprApMemoryUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitRn.setStatus("current")
_CfprApMemoryUnitAdminState_Type = CfprApMemoryAdminState
_CfprApMemoryUnitAdminState_Object = MibTableColumn
cfprApMemoryUnitAdminState = _CfprApMemoryUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 4),
    _CfprApMemoryUnitAdminState_Type()
)
cfprApMemoryUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitAdminState.setStatus("current")
_CfprApMemoryUnitArray_Type = Gauge32
_CfprApMemoryUnitArray_Object = MibTableColumn
cfprApMemoryUnitArray = _CfprApMemoryUnitArray_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 5),
    _CfprApMemoryUnitArray_Type()
)
cfprApMemoryUnitArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitArray.setStatus("current")
_CfprApMemoryUnitBank_Type = Gauge32
_CfprApMemoryUnitBank_Object = MibTableColumn
cfprApMemoryUnitBank = _CfprApMemoryUnitBank_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 6),
    _CfprApMemoryUnitBank_Type()
)
cfprApMemoryUnitBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitBank.setStatus("current")
_CfprApMemoryUnitCapacity_Type = Gauge32
_CfprApMemoryUnitCapacity_Object = MibTableColumn
cfprApMemoryUnitCapacity = _CfprApMemoryUnitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 7),
    _CfprApMemoryUnitCapacity_Type()
)
cfprApMemoryUnitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitCapacity.setStatus("current")
_CfprApMemoryUnitClock_Type = Gauge32
_CfprApMemoryUnitClock_Object = MibTableColumn
cfprApMemoryUnitClock = _CfprApMemoryUnitClock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 8),
    _CfprApMemoryUnitClock_Type()
)
cfprApMemoryUnitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitClock.setStatus("current")
_CfprApMemoryUnitFormFactor_Type = CfprApMemoryFormFactor
_CfprApMemoryUnitFormFactor_Object = MibTableColumn
cfprApMemoryUnitFormFactor = _CfprApMemoryUnitFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 9),
    _CfprApMemoryUnitFormFactor_Type()
)
cfprApMemoryUnitFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitFormFactor.setStatus("current")
_CfprApMemoryUnitId_Type = CfprApMemoryUnitId
_CfprApMemoryUnitId_Object = MibTableColumn
cfprApMemoryUnitId = _CfprApMemoryUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 10),
    _CfprApMemoryUnitId_Type()
)
cfprApMemoryUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitId.setStatus("current")
_CfprApMemoryUnitLatency_Type = Integer32
_CfprApMemoryUnitLatency_Object = MibTableColumn
cfprApMemoryUnitLatency = _CfprApMemoryUnitLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 11),
    _CfprApMemoryUnitLatency_Type()
)
cfprApMemoryUnitLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitLatency.setStatus("current")
_CfprApMemoryUnitLocation_Type = SnmpAdminString
_CfprApMemoryUnitLocation_Object = MibTableColumn
cfprApMemoryUnitLocation = _CfprApMemoryUnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 12),
    _CfprApMemoryUnitLocation_Type()
)
cfprApMemoryUnitLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitLocation.setStatus("current")
_CfprApMemoryUnitLocationDn_Type = SnmpAdminString
_CfprApMemoryUnitLocationDn_Object = MibTableColumn
cfprApMemoryUnitLocationDn = _CfprApMemoryUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 13),
    _CfprApMemoryUnitLocationDn_Type()
)
cfprApMemoryUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitLocationDn.setStatus("current")
_CfprApMemoryUnitModel_Type = SnmpAdminString
_CfprApMemoryUnitModel_Object = MibTableColumn
cfprApMemoryUnitModel = _CfprApMemoryUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 14),
    _CfprApMemoryUnitModel_Type()
)
cfprApMemoryUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitModel.setStatus("current")
_CfprApMemoryUnitOperQualifier_Type = CfprApMemoryIssues
_CfprApMemoryUnitOperQualifier_Object = MibTableColumn
cfprApMemoryUnitOperQualifier = _CfprApMemoryUnitOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 15),
    _CfprApMemoryUnitOperQualifier_Type()
)
cfprApMemoryUnitOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitOperQualifier.setStatus("current")
_CfprApMemoryUnitOperQualifierReason_Type = SnmpAdminString
_CfprApMemoryUnitOperQualifierReason_Object = MibTableColumn
cfprApMemoryUnitOperQualifierReason = _CfprApMemoryUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 16),
    _CfprApMemoryUnitOperQualifierReason_Type()
)
cfprApMemoryUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitOperQualifierReason.setStatus("current")
_CfprApMemoryUnitOperState_Type = CfprApEquipmentOperability
_CfprApMemoryUnitOperState_Object = MibTableColumn
cfprApMemoryUnitOperState = _CfprApMemoryUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 17),
    _CfprApMemoryUnitOperState_Type()
)
cfprApMemoryUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitOperState.setStatus("current")
_CfprApMemoryUnitOperability_Type = CfprApMemoryUnitOperability
_CfprApMemoryUnitOperability_Object = MibTableColumn
cfprApMemoryUnitOperability = _CfprApMemoryUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 18),
    _CfprApMemoryUnitOperability_Type()
)
cfprApMemoryUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitOperability.setStatus("current")
_CfprApMemoryUnitPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryUnitPerf_Object = MibTableColumn
cfprApMemoryUnitPerf = _CfprApMemoryUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 19),
    _CfprApMemoryUnitPerf_Type()
)
cfprApMemoryUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitPerf.setStatus("current")
_CfprApMemoryUnitPower_Type = CfprApEquipmentPowerState
_CfprApMemoryUnitPower_Object = MibTableColumn
cfprApMemoryUnitPower = _CfprApMemoryUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 20),
    _CfprApMemoryUnitPower_Type()
)
cfprApMemoryUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitPower.setStatus("current")
_CfprApMemoryUnitPresence_Type = CfprApEquipmentPresence
_CfprApMemoryUnitPresence_Object = MibTableColumn
cfprApMemoryUnitPresence = _CfprApMemoryUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 21),
    _CfprApMemoryUnitPresence_Type()
)
cfprApMemoryUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitPresence.setStatus("current")
_CfprApMemoryUnitRevision_Type = SnmpAdminString
_CfprApMemoryUnitRevision_Object = MibTableColumn
cfprApMemoryUnitRevision = _CfprApMemoryUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 22),
    _CfprApMemoryUnitRevision_Type()
)
cfprApMemoryUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitRevision.setStatus("current")
_CfprApMemoryUnitSerial_Type = SnmpAdminString
_CfprApMemoryUnitSerial_Object = MibTableColumn
cfprApMemoryUnitSerial = _CfprApMemoryUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 23),
    _CfprApMemoryUnitSerial_Type()
)
cfprApMemoryUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitSerial.setStatus("current")
_CfprApMemoryUnitSet_Type = Gauge32
_CfprApMemoryUnitSet_Object = MibTableColumn
cfprApMemoryUnitSet = _CfprApMemoryUnitSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 24),
    _CfprApMemoryUnitSet_Type()
)
cfprApMemoryUnitSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitSet.setStatus("current")
_CfprApMemoryUnitSpeed_Type = Gauge32
_CfprApMemoryUnitSpeed_Object = MibTableColumn
cfprApMemoryUnitSpeed = _CfprApMemoryUnitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 25),
    _CfprApMemoryUnitSpeed_Type()
)
cfprApMemoryUnitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitSpeed.setStatus("current")
_CfprApMemoryUnitThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryUnitThermal_Object = MibTableColumn
cfprApMemoryUnitThermal = _CfprApMemoryUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 26),
    _CfprApMemoryUnitThermal_Type()
)
cfprApMemoryUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitThermal.setStatus("current")
_CfprApMemoryUnitType_Type = CfprApMemoryType
_CfprApMemoryUnitType_Object = MibTableColumn
cfprApMemoryUnitType = _CfprApMemoryUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 27),
    _CfprApMemoryUnitType_Type()
)
cfprApMemoryUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitType.setStatus("current")
_CfprApMemoryUnitVendor_Type = SnmpAdminString
_CfprApMemoryUnitVendor_Object = MibTableColumn
cfprApMemoryUnitVendor = _CfprApMemoryUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 28),
    _CfprApMemoryUnitVendor_Type()
)
cfprApMemoryUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitVendor.setStatus("current")
_CfprApMemoryUnitVisibility_Type = CfprApMemoryVisibility
_CfprApMemoryUnitVisibility_Object = MibTableColumn
cfprApMemoryUnitVisibility = _CfprApMemoryUnitVisibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 29),
    _CfprApMemoryUnitVisibility_Type()
)
cfprApMemoryUnitVisibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitVisibility.setStatus("current")
_CfprApMemoryUnitVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApMemoryUnitVoltage_Object = MibTableColumn
cfprApMemoryUnitVoltage = _CfprApMemoryUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 30),
    _CfprApMemoryUnitVoltage_Type()
)
cfprApMemoryUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitVoltage.setStatus("current")
_CfprApMemoryUnitWidth_Type = Gauge32
_CfprApMemoryUnitWidth_Object = MibTableColumn
cfprApMemoryUnitWidth = _CfprApMemoryUnitWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 11, 1, 31),
    _CfprApMemoryUnitWidth_Type()
)
cfprApMemoryUnitWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitWidth.setStatus("current")
_CfprApMemoryUnitEnvStatsTable_Object = MibTable
cfprApMemoryUnitEnvStatsTable = _CfprApMemoryUnitEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12)
)
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsTable.setStatus("current")
_CfprApMemoryUnitEnvStatsEntry_Object = MibTableRow
cfprApMemoryUnitEnvStatsEntry = _CfprApMemoryUnitEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1)
)
cfprApMemoryUnitEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryUnitEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsEntry.setStatus("current")
_CfprApMemoryUnitEnvStatsInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryUnitEnvStatsInstanceId_Object = MibTableColumn
cfprApMemoryUnitEnvStatsInstanceId = _CfprApMemoryUnitEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 1),
    _CfprApMemoryUnitEnvStatsInstanceId_Type()
)
cfprApMemoryUnitEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsInstanceId.setStatus("current")
_CfprApMemoryUnitEnvStatsDn_Type = CfprApManagedObjectDn
_CfprApMemoryUnitEnvStatsDn_Object = MibTableColumn
cfprApMemoryUnitEnvStatsDn = _CfprApMemoryUnitEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 2),
    _CfprApMemoryUnitEnvStatsDn_Type()
)
cfprApMemoryUnitEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsDn.setStatus("current")
_CfprApMemoryUnitEnvStatsRn_Type = SnmpAdminString
_CfprApMemoryUnitEnvStatsRn_Object = MibTableColumn
cfprApMemoryUnitEnvStatsRn = _CfprApMemoryUnitEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 3),
    _CfprApMemoryUnitEnvStatsRn_Type()
)
cfprApMemoryUnitEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsRn.setStatus("current")
_CfprApMemoryUnitEnvStatsIntervals_Type = Gauge32
_CfprApMemoryUnitEnvStatsIntervals_Object = MibTableColumn
cfprApMemoryUnitEnvStatsIntervals = _CfprApMemoryUnitEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 4),
    _CfprApMemoryUnitEnvStatsIntervals_Type()
)
cfprApMemoryUnitEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsIntervals.setStatus("current")
_CfprApMemoryUnitEnvStatsSuspect_Type = TruthValue
_CfprApMemoryUnitEnvStatsSuspect_Object = MibTableColumn
cfprApMemoryUnitEnvStatsSuspect = _CfprApMemoryUnitEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 5),
    _CfprApMemoryUnitEnvStatsSuspect_Type()
)
cfprApMemoryUnitEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsSuspect.setStatus("current")
_CfprApMemoryUnitEnvStatsTemperature_Type = Integer32
_CfprApMemoryUnitEnvStatsTemperature_Object = MibTableColumn
cfprApMemoryUnitEnvStatsTemperature = _CfprApMemoryUnitEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 6),
    _CfprApMemoryUnitEnvStatsTemperature_Type()
)
cfprApMemoryUnitEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsTemperature.setStatus("current")
_CfprApMemoryUnitEnvStatsTemperatureAvg_Type = Integer32
_CfprApMemoryUnitEnvStatsTemperatureAvg_Object = MibTableColumn
cfprApMemoryUnitEnvStatsTemperatureAvg = _CfprApMemoryUnitEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 7),
    _CfprApMemoryUnitEnvStatsTemperatureAvg_Type()
)
cfprApMemoryUnitEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsTemperatureAvg.setStatus("current")
_CfprApMemoryUnitEnvStatsTemperatureMax_Type = Integer32
_CfprApMemoryUnitEnvStatsTemperatureMax_Object = MibTableColumn
cfprApMemoryUnitEnvStatsTemperatureMax = _CfprApMemoryUnitEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 8),
    _CfprApMemoryUnitEnvStatsTemperatureMax_Type()
)
cfprApMemoryUnitEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsTemperatureMax.setStatus("current")
_CfprApMemoryUnitEnvStatsTemperatureMin_Type = Integer32
_CfprApMemoryUnitEnvStatsTemperatureMin_Object = MibTableColumn
cfprApMemoryUnitEnvStatsTemperatureMin = _CfprApMemoryUnitEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 9),
    _CfprApMemoryUnitEnvStatsTemperatureMin_Type()
)
cfprApMemoryUnitEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsTemperatureMin.setStatus("current")
_CfprApMemoryUnitEnvStatsThresholded_Type = CfprApMemoryUnitEnvStatsThresholded
_CfprApMemoryUnitEnvStatsThresholded_Object = MibTableColumn
cfprApMemoryUnitEnvStatsThresholded = _CfprApMemoryUnitEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 10),
    _CfprApMemoryUnitEnvStatsThresholded_Type()
)
cfprApMemoryUnitEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsThresholded.setStatus("current")
_CfprApMemoryUnitEnvStatsTimeCollected_Type = DateAndTime
_CfprApMemoryUnitEnvStatsTimeCollected_Object = MibTableColumn
cfprApMemoryUnitEnvStatsTimeCollected = _CfprApMemoryUnitEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 11),
    _CfprApMemoryUnitEnvStatsTimeCollected_Type()
)
cfprApMemoryUnitEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsTimeCollected.setStatus("current")
_CfprApMemoryUnitEnvStatsUpdate_Type = Gauge32
_CfprApMemoryUnitEnvStatsUpdate_Object = MibTableColumn
cfprApMemoryUnitEnvStatsUpdate = _CfprApMemoryUnitEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 12, 1, 12),
    _CfprApMemoryUnitEnvStatsUpdate_Type()
)
cfprApMemoryUnitEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsUpdate.setStatus("current")
_CfprApMemoryUnitEnvStatsHistTable_Object = MibTable
cfprApMemoryUnitEnvStatsHistTable = _CfprApMemoryUnitEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13)
)
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistTable.setStatus("current")
_CfprApMemoryUnitEnvStatsHistEntry_Object = MibTableRow
cfprApMemoryUnitEnvStatsHistEntry = _CfprApMemoryUnitEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1)
)
cfprApMemoryUnitEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MEMORY-MIB", "cfprApMemoryUnitEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistEntry.setStatus("current")
_CfprApMemoryUnitEnvStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApMemoryUnitEnvStatsHistInstanceId_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistInstanceId = _CfprApMemoryUnitEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 1),
    _CfprApMemoryUnitEnvStatsHistInstanceId_Type()
)
cfprApMemoryUnitEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistInstanceId.setStatus("current")
_CfprApMemoryUnitEnvStatsHistDn_Type = CfprApManagedObjectDn
_CfprApMemoryUnitEnvStatsHistDn_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistDn = _CfprApMemoryUnitEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 2),
    _CfprApMemoryUnitEnvStatsHistDn_Type()
)
cfprApMemoryUnitEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistDn.setStatus("current")
_CfprApMemoryUnitEnvStatsHistRn_Type = SnmpAdminString
_CfprApMemoryUnitEnvStatsHistRn_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistRn = _CfprApMemoryUnitEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 3),
    _CfprApMemoryUnitEnvStatsHistRn_Type()
)
cfprApMemoryUnitEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistRn.setStatus("current")
_CfprApMemoryUnitEnvStatsHistId_Type = Unsigned64
_CfprApMemoryUnitEnvStatsHistId_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistId = _CfprApMemoryUnitEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 4),
    _CfprApMemoryUnitEnvStatsHistId_Type()
)
cfprApMemoryUnitEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistId.setStatus("current")
_CfprApMemoryUnitEnvStatsHistMostRecent_Type = TruthValue
_CfprApMemoryUnitEnvStatsHistMostRecent_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistMostRecent = _CfprApMemoryUnitEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 5),
    _CfprApMemoryUnitEnvStatsHistMostRecent_Type()
)
cfprApMemoryUnitEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistMostRecent.setStatus("current")
_CfprApMemoryUnitEnvStatsHistSuspect_Type = TruthValue
_CfprApMemoryUnitEnvStatsHistSuspect_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistSuspect = _CfprApMemoryUnitEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 6),
    _CfprApMemoryUnitEnvStatsHistSuspect_Type()
)
cfprApMemoryUnitEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistSuspect.setStatus("current")
_CfprApMemoryUnitEnvStatsHistTemperature_Type = Integer32
_CfprApMemoryUnitEnvStatsHistTemperature_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistTemperature = _CfprApMemoryUnitEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 7),
    _CfprApMemoryUnitEnvStatsHistTemperature_Type()
)
cfprApMemoryUnitEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistTemperature.setStatus("current")
_CfprApMemoryUnitEnvStatsHistTemperatureAvg_Type = Integer32
_CfprApMemoryUnitEnvStatsHistTemperatureAvg_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistTemperatureAvg = _CfprApMemoryUnitEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 8),
    _CfprApMemoryUnitEnvStatsHistTemperatureAvg_Type()
)
cfprApMemoryUnitEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistTemperatureAvg.setStatus("current")
_CfprApMemoryUnitEnvStatsHistTemperatureMax_Type = Integer32
_CfprApMemoryUnitEnvStatsHistTemperatureMax_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistTemperatureMax = _CfprApMemoryUnitEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 9),
    _CfprApMemoryUnitEnvStatsHistTemperatureMax_Type()
)
cfprApMemoryUnitEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistTemperatureMax.setStatus("current")
_CfprApMemoryUnitEnvStatsHistTemperatureMin_Type = Integer32
_CfprApMemoryUnitEnvStatsHistTemperatureMin_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistTemperatureMin = _CfprApMemoryUnitEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 10),
    _CfprApMemoryUnitEnvStatsHistTemperatureMin_Type()
)
cfprApMemoryUnitEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistTemperatureMin.setStatus("current")
_CfprApMemoryUnitEnvStatsHistThresholded_Type = CfprApMemoryUnitEnvStatsHistThresholded
_CfprApMemoryUnitEnvStatsHistThresholded_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistThresholded = _CfprApMemoryUnitEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 11),
    _CfprApMemoryUnitEnvStatsHistThresholded_Type()
)
cfprApMemoryUnitEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistThresholded.setStatus("current")
_CfprApMemoryUnitEnvStatsHistTimeCollected_Type = DateAndTime
_CfprApMemoryUnitEnvStatsHistTimeCollected_Object = MibTableColumn
cfprApMemoryUnitEnvStatsHistTimeCollected = _CfprApMemoryUnitEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 50, 13, 1, 12),
    _CfprApMemoryUnitEnvStatsHistTimeCollected_Type()
)
cfprApMemoryUnitEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMemoryUnitEnvStatsHistTimeCollected.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-MEMORY-MIB",
    **{"cfprApMemoryObjects": cfprApMemoryObjects,
       "cfprApMemoryArrayTable": cfprApMemoryArrayTable,
       "cfprApMemoryArrayEntry": cfprApMemoryArrayEntry,
       "cfprApMemoryArrayInstanceId": cfprApMemoryArrayInstanceId,
       "cfprApMemoryArrayDn": cfprApMemoryArrayDn,
       "cfprApMemoryArrayRn": cfprApMemoryArrayRn,
       "cfprApMemoryArrayCpuId": cfprApMemoryArrayCpuId,
       "cfprApMemoryArrayCurrCapacity": cfprApMemoryArrayCurrCapacity,
       "cfprApMemoryArrayErrorCorrection": cfprApMemoryArrayErrorCorrection,
       "cfprApMemoryArrayId": cfprApMemoryArrayId,
       "cfprApMemoryArrayLocationDn": cfprApMemoryArrayLocationDn,
       "cfprApMemoryArrayMaxCapacity": cfprApMemoryArrayMaxCapacity,
       "cfprApMemoryArrayMaxDevices": cfprApMemoryArrayMaxDevices,
       "cfprApMemoryArrayModel": cfprApMemoryArrayModel,
       "cfprApMemoryArrayOperQualifierReason": cfprApMemoryArrayOperQualifierReason,
       "cfprApMemoryArrayOperState": cfprApMemoryArrayOperState,
       "cfprApMemoryArrayOperability": cfprApMemoryArrayOperability,
       "cfprApMemoryArrayPerf": cfprApMemoryArrayPerf,
       "cfprApMemoryArrayPopulated": cfprApMemoryArrayPopulated,
       "cfprApMemoryArrayPower": cfprApMemoryArrayPower,
       "cfprApMemoryArrayPresence": cfprApMemoryArrayPresence,
       "cfprApMemoryArrayRevision": cfprApMemoryArrayRevision,
       "cfprApMemoryArraySerial": cfprApMemoryArraySerial,
       "cfprApMemoryArrayThermal": cfprApMemoryArrayThermal,
       "cfprApMemoryArrayVendor": cfprApMemoryArrayVendor,
       "cfprApMemoryArrayVoltage": cfprApMemoryArrayVoltage,
       "cfprApMemoryArrayEnvStatsTable": cfprApMemoryArrayEnvStatsTable,
       "cfprApMemoryArrayEnvStatsEntry": cfprApMemoryArrayEnvStatsEntry,
       "cfprApMemoryArrayEnvStatsInstanceId": cfprApMemoryArrayEnvStatsInstanceId,
       "cfprApMemoryArrayEnvStatsDn": cfprApMemoryArrayEnvStatsDn,
       "cfprApMemoryArrayEnvStatsRn": cfprApMemoryArrayEnvStatsRn,
       "cfprApMemoryArrayEnvStatsInputCurrent": cfprApMemoryArrayEnvStatsInputCurrent,
       "cfprApMemoryArrayEnvStatsInputCurrentAvg": cfprApMemoryArrayEnvStatsInputCurrentAvg,
       "cfprApMemoryArrayEnvStatsInputCurrentMax": cfprApMemoryArrayEnvStatsInputCurrentMax,
       "cfprApMemoryArrayEnvStatsInputCurrentMin": cfprApMemoryArrayEnvStatsInputCurrentMin,
       "cfprApMemoryArrayEnvStatsIntervals": cfprApMemoryArrayEnvStatsIntervals,
       "cfprApMemoryArrayEnvStatsSuspect": cfprApMemoryArrayEnvStatsSuspect,
       "cfprApMemoryArrayEnvStatsThresholded": cfprApMemoryArrayEnvStatsThresholded,
       "cfprApMemoryArrayEnvStatsTimeCollected": cfprApMemoryArrayEnvStatsTimeCollected,
       "cfprApMemoryArrayEnvStatsUpdate": cfprApMemoryArrayEnvStatsUpdate,
       "cfprApMemoryArrayEnvStatsHistTable": cfprApMemoryArrayEnvStatsHistTable,
       "cfprApMemoryArrayEnvStatsHistEntry": cfprApMemoryArrayEnvStatsHistEntry,
       "cfprApMemoryArrayEnvStatsHistInstanceId": cfprApMemoryArrayEnvStatsHistInstanceId,
       "cfprApMemoryArrayEnvStatsHistDn": cfprApMemoryArrayEnvStatsHistDn,
       "cfprApMemoryArrayEnvStatsHistRn": cfprApMemoryArrayEnvStatsHistRn,
       "cfprApMemoryArrayEnvStatsHistId": cfprApMemoryArrayEnvStatsHistId,
       "cfprApMemoryArrayEnvStatsHistInputCurrent": cfprApMemoryArrayEnvStatsHistInputCurrent,
       "cfprApMemoryArrayEnvStatsHistInputCurrentAvg": cfprApMemoryArrayEnvStatsHistInputCurrentAvg,
       "cfprApMemoryArrayEnvStatsHistInputCurrentMax": cfprApMemoryArrayEnvStatsHistInputCurrentMax,
       "cfprApMemoryArrayEnvStatsHistInputCurrentMin": cfprApMemoryArrayEnvStatsHistInputCurrentMin,
       "cfprApMemoryArrayEnvStatsHistMostRecent": cfprApMemoryArrayEnvStatsHistMostRecent,
       "cfprApMemoryArrayEnvStatsHistSuspect": cfprApMemoryArrayEnvStatsHistSuspect,
       "cfprApMemoryArrayEnvStatsHistThresholded": cfprApMemoryArrayEnvStatsHistThresholded,
       "cfprApMemoryArrayEnvStatsHistTimeCollected": cfprApMemoryArrayEnvStatsHistTimeCollected,
       "cfprApMemoryBufferUnitTable": cfprApMemoryBufferUnitTable,
       "cfprApMemoryBufferUnitEntry": cfprApMemoryBufferUnitEntry,
       "cfprApMemoryBufferUnitInstanceId": cfprApMemoryBufferUnitInstanceId,
       "cfprApMemoryBufferUnitDn": cfprApMemoryBufferUnitDn,
       "cfprApMemoryBufferUnitRn": cfprApMemoryBufferUnitRn,
       "cfprApMemoryBufferUnitId": cfprApMemoryBufferUnitId,
       "cfprApMemoryBufferUnitLocationDn": cfprApMemoryBufferUnitLocationDn,
       "cfprApMemoryBufferUnitModel": cfprApMemoryBufferUnitModel,
       "cfprApMemoryBufferUnitOperQualifierReason": cfprApMemoryBufferUnitOperQualifierReason,
       "cfprApMemoryBufferUnitOperState": cfprApMemoryBufferUnitOperState,
       "cfprApMemoryBufferUnitOperability": cfprApMemoryBufferUnitOperability,
       "cfprApMemoryBufferUnitPerf": cfprApMemoryBufferUnitPerf,
       "cfprApMemoryBufferUnitPower": cfprApMemoryBufferUnitPower,
       "cfprApMemoryBufferUnitPresence": cfprApMemoryBufferUnitPresence,
       "cfprApMemoryBufferUnitRevision": cfprApMemoryBufferUnitRevision,
       "cfprApMemoryBufferUnitSerial": cfprApMemoryBufferUnitSerial,
       "cfprApMemoryBufferUnitThermal": cfprApMemoryBufferUnitThermal,
       "cfprApMemoryBufferUnitVendor": cfprApMemoryBufferUnitVendor,
       "cfprApMemoryBufferUnitVoltage": cfprApMemoryBufferUnitVoltage,
       "cfprApMemoryBufferUnitEnvStatsTable": cfprApMemoryBufferUnitEnvStatsTable,
       "cfprApMemoryBufferUnitEnvStatsEntry": cfprApMemoryBufferUnitEnvStatsEntry,
       "cfprApMemoryBufferUnitEnvStatsInstanceId": cfprApMemoryBufferUnitEnvStatsInstanceId,
       "cfprApMemoryBufferUnitEnvStatsDn": cfprApMemoryBufferUnitEnvStatsDn,
       "cfprApMemoryBufferUnitEnvStatsRn": cfprApMemoryBufferUnitEnvStatsRn,
       "cfprApMemoryBufferUnitEnvStatsIntervals": cfprApMemoryBufferUnitEnvStatsIntervals,
       "cfprApMemoryBufferUnitEnvStatsSuspect": cfprApMemoryBufferUnitEnvStatsSuspect,
       "cfprApMemoryBufferUnitEnvStatsTemperature": cfprApMemoryBufferUnitEnvStatsTemperature,
       "cfprApMemoryBufferUnitEnvStatsTemperatureAvg": cfprApMemoryBufferUnitEnvStatsTemperatureAvg,
       "cfprApMemoryBufferUnitEnvStatsTemperatureMax": cfprApMemoryBufferUnitEnvStatsTemperatureMax,
       "cfprApMemoryBufferUnitEnvStatsTemperatureMin": cfprApMemoryBufferUnitEnvStatsTemperatureMin,
       "cfprApMemoryBufferUnitEnvStatsThresholded": cfprApMemoryBufferUnitEnvStatsThresholded,
       "cfprApMemoryBufferUnitEnvStatsTimeCollected": cfprApMemoryBufferUnitEnvStatsTimeCollected,
       "cfprApMemoryBufferUnitEnvStatsUpdate": cfprApMemoryBufferUnitEnvStatsUpdate,
       "cfprApMemoryBufferUnitEnvStatsHistTable": cfprApMemoryBufferUnitEnvStatsHistTable,
       "cfprApMemoryBufferUnitEnvStatsHistEntry": cfprApMemoryBufferUnitEnvStatsHistEntry,
       "cfprApMemoryBufferUnitEnvStatsHistInstanceId": cfprApMemoryBufferUnitEnvStatsHistInstanceId,
       "cfprApMemoryBufferUnitEnvStatsHistDn": cfprApMemoryBufferUnitEnvStatsHistDn,
       "cfprApMemoryBufferUnitEnvStatsHistRn": cfprApMemoryBufferUnitEnvStatsHistRn,
       "cfprApMemoryBufferUnitEnvStatsHistId": cfprApMemoryBufferUnitEnvStatsHistId,
       "cfprApMemoryBufferUnitEnvStatsHistMostRecent": cfprApMemoryBufferUnitEnvStatsHistMostRecent,
       "cfprApMemoryBufferUnitEnvStatsHistSuspect": cfprApMemoryBufferUnitEnvStatsHistSuspect,
       "cfprApMemoryBufferUnitEnvStatsHistTemperature": cfprApMemoryBufferUnitEnvStatsHistTemperature,
       "cfprApMemoryBufferUnitEnvStatsHistTemperatureAvg": cfprApMemoryBufferUnitEnvStatsHistTemperatureAvg,
       "cfprApMemoryBufferUnitEnvStatsHistTemperatureMax": cfprApMemoryBufferUnitEnvStatsHistTemperatureMax,
       "cfprApMemoryBufferUnitEnvStatsHistTemperatureMin": cfprApMemoryBufferUnitEnvStatsHistTemperatureMin,
       "cfprApMemoryBufferUnitEnvStatsHistThresholded": cfprApMemoryBufferUnitEnvStatsHistThresholded,
       "cfprApMemoryBufferUnitEnvStatsHistTimeCollected": cfprApMemoryBufferUnitEnvStatsHistTimeCollected,
       "cfprApMemoryErrorStatsTable": cfprApMemoryErrorStatsTable,
       "cfprApMemoryErrorStatsEntry": cfprApMemoryErrorStatsEntry,
       "cfprApMemoryErrorStatsInstanceId": cfprApMemoryErrorStatsInstanceId,
       "cfprApMemoryErrorStatsDn": cfprApMemoryErrorStatsDn,
       "cfprApMemoryErrorStatsRn": cfprApMemoryErrorStatsRn,
       "cfprApMemoryErrorStatsAddressParityErrors": cfprApMemoryErrorStatsAddressParityErrors,
       "cfprApMemoryErrorStatsAddressParityErrors15Min": cfprApMemoryErrorStatsAddressParityErrors15Min,
       "cfprApMemoryErrorStatsAddressParityErrors15MinH": cfprApMemoryErrorStatsAddressParityErrors15MinH,
       "cfprApMemoryErrorStatsAddressParityErrors1Day": cfprApMemoryErrorStatsAddressParityErrors1Day,
       "cfprApMemoryErrorStatsAddressParityErrors1DayH": cfprApMemoryErrorStatsAddressParityErrors1DayH,
       "cfprApMemoryErrorStatsAddressParityErrors1Hour": cfprApMemoryErrorStatsAddressParityErrors1Hour,
       "cfprApMemoryErrorStatsAddressParityErrors1HourH": cfprApMemoryErrorStatsAddressParityErrors1HourH,
       "cfprApMemoryErrorStatsAddressParityErrors1Week": cfprApMemoryErrorStatsAddressParityErrors1Week,
       "cfprApMemoryErrorStatsAddressParityErrors1WeekH": cfprApMemoryErrorStatsAddressParityErrors1WeekH,
       "cfprApMemoryErrorStatsAddressParityErrors2Weeks": cfprApMemoryErrorStatsAddressParityErrors2Weeks,
       "cfprApMemoryErrorStatsAddressParityErrors2WeeksH": cfprApMemoryErrorStatsAddressParityErrors2WeeksH,
       "cfprApMemoryErrorStatsEccMultibitErrors": cfprApMemoryErrorStatsEccMultibitErrors,
       "cfprApMemoryErrorStatsEccMultibitErrors15Min": cfprApMemoryErrorStatsEccMultibitErrors15Min,
       "cfprApMemoryErrorStatsEccMultibitErrors15MinH": cfprApMemoryErrorStatsEccMultibitErrors15MinH,
       "cfprApMemoryErrorStatsEccMultibitErrors1Day": cfprApMemoryErrorStatsEccMultibitErrors1Day,
       "cfprApMemoryErrorStatsEccMultibitErrors1DayH": cfprApMemoryErrorStatsEccMultibitErrors1DayH,
       "cfprApMemoryErrorStatsEccMultibitErrors1Hour": cfprApMemoryErrorStatsEccMultibitErrors1Hour,
       "cfprApMemoryErrorStatsEccMultibitErrors1HourH": cfprApMemoryErrorStatsEccMultibitErrors1HourH,
       "cfprApMemoryErrorStatsEccMultibitErrors1Week": cfprApMemoryErrorStatsEccMultibitErrors1Week,
       "cfprApMemoryErrorStatsEccMultibitErrors1WeekH": cfprApMemoryErrorStatsEccMultibitErrors1WeekH,
       "cfprApMemoryErrorStatsEccMultibitErrors2Weeks": cfprApMemoryErrorStatsEccMultibitErrors2Weeks,
       "cfprApMemoryErrorStatsEccMultibitErrors2WeeksH": cfprApMemoryErrorStatsEccMultibitErrors2WeeksH,
       "cfprApMemoryErrorStatsEccSinglebitErrors": cfprApMemoryErrorStatsEccSinglebitErrors,
       "cfprApMemoryErrorStatsEccSinglebitErrors15Min": cfprApMemoryErrorStatsEccSinglebitErrors15Min,
       "cfprApMemoryErrorStatsEccSinglebitErrors15MinH": cfprApMemoryErrorStatsEccSinglebitErrors15MinH,
       "cfprApMemoryErrorStatsEccSinglebitErrors1Day": cfprApMemoryErrorStatsEccSinglebitErrors1Day,
       "cfprApMemoryErrorStatsEccSinglebitErrors1DayH": cfprApMemoryErrorStatsEccSinglebitErrors1DayH,
       "cfprApMemoryErrorStatsEccSinglebitErrors1Hour": cfprApMemoryErrorStatsEccSinglebitErrors1Hour,
       "cfprApMemoryErrorStatsEccSinglebitErrors1HourH": cfprApMemoryErrorStatsEccSinglebitErrors1HourH,
       "cfprApMemoryErrorStatsEccSinglebitErrors1Week": cfprApMemoryErrorStatsEccSinglebitErrors1Week,
       "cfprApMemoryErrorStatsEccSinglebitErrors1WeekH": cfprApMemoryErrorStatsEccSinglebitErrors1WeekH,
       "cfprApMemoryErrorStatsEccSinglebitErrors2Weeks": cfprApMemoryErrorStatsEccSinglebitErrors2Weeks,
       "cfprApMemoryErrorStatsEccSinglebitErrors2WeeksH": cfprApMemoryErrorStatsEccSinglebitErrors2WeeksH,
       "cfprApMemoryErrorStatsIntervals": cfprApMemoryErrorStatsIntervals,
       "cfprApMemoryErrorStatsMismatchErrors": cfprApMemoryErrorStatsMismatchErrors,
       "cfprApMemoryErrorStatsMismatchErrors15Min": cfprApMemoryErrorStatsMismatchErrors15Min,
       "cfprApMemoryErrorStatsMismatchErrors15MinH": cfprApMemoryErrorStatsMismatchErrors15MinH,
       "cfprApMemoryErrorStatsMismatchErrors1Day": cfprApMemoryErrorStatsMismatchErrors1Day,
       "cfprApMemoryErrorStatsMismatchErrors1DayH": cfprApMemoryErrorStatsMismatchErrors1DayH,
       "cfprApMemoryErrorStatsMismatchErrors1Hour": cfprApMemoryErrorStatsMismatchErrors1Hour,
       "cfprApMemoryErrorStatsMismatchErrors1HourH": cfprApMemoryErrorStatsMismatchErrors1HourH,
       "cfprApMemoryErrorStatsMismatchErrors1Week": cfprApMemoryErrorStatsMismatchErrors1Week,
       "cfprApMemoryErrorStatsMismatchErrors1WeekH": cfprApMemoryErrorStatsMismatchErrors1WeekH,
       "cfprApMemoryErrorStatsMismatchErrors2Weeks": cfprApMemoryErrorStatsMismatchErrors2Weeks,
       "cfprApMemoryErrorStatsMismatchErrors2WeeksH": cfprApMemoryErrorStatsMismatchErrors2WeeksH,
       "cfprApMemoryErrorStatsSuspect": cfprApMemoryErrorStatsSuspect,
       "cfprApMemoryErrorStatsThresholded": cfprApMemoryErrorStatsThresholded,
       "cfprApMemoryErrorStatsTimeCollected": cfprApMemoryErrorStatsTimeCollected,
       "cfprApMemoryErrorStatsUpdate": cfprApMemoryErrorStatsUpdate,
       "cfprApMemoryQualTable": cfprApMemoryQualTable,
       "cfprApMemoryQualEntry": cfprApMemoryQualEntry,
       "cfprApMemoryQualInstanceId": cfprApMemoryQualInstanceId,
       "cfprApMemoryQualDn": cfprApMemoryQualDn,
       "cfprApMemoryQualRn": cfprApMemoryQualRn,
       "cfprApMemoryQualClock": cfprApMemoryQualClock,
       "cfprApMemoryQualLatency": cfprApMemoryQualLatency,
       "cfprApMemoryQualMaxCap": cfprApMemoryQualMaxCap,
       "cfprApMemoryQualMinCap": cfprApMemoryQualMinCap,
       "cfprApMemoryQualSpeed": cfprApMemoryQualSpeed,
       "cfprApMemoryQualUnits": cfprApMemoryQualUnits,
       "cfprApMemoryQualWidth": cfprApMemoryQualWidth,
       "cfprApMemoryRuntimeTable": cfprApMemoryRuntimeTable,
       "cfprApMemoryRuntimeEntry": cfprApMemoryRuntimeEntry,
       "cfprApMemoryRuntimeInstanceId": cfprApMemoryRuntimeInstanceId,
       "cfprApMemoryRuntimeDn": cfprApMemoryRuntimeDn,
       "cfprApMemoryRuntimeRn": cfprApMemoryRuntimeRn,
       "cfprApMemoryRuntimeAvailable": cfprApMemoryRuntimeAvailable,
       "cfprApMemoryRuntimeAvailableAvg": cfprApMemoryRuntimeAvailableAvg,
       "cfprApMemoryRuntimeAvailableMax": cfprApMemoryRuntimeAvailableMax,
       "cfprApMemoryRuntimeAvailableMin": cfprApMemoryRuntimeAvailableMin,
       "cfprApMemoryRuntimeCached": cfprApMemoryRuntimeCached,
       "cfprApMemoryRuntimeCachedAvg": cfprApMemoryRuntimeCachedAvg,
       "cfprApMemoryRuntimeCachedMax": cfprApMemoryRuntimeCachedMax,
       "cfprApMemoryRuntimeCachedMin": cfprApMemoryRuntimeCachedMin,
       "cfprApMemoryRuntimeIntervals": cfprApMemoryRuntimeIntervals,
       "cfprApMemoryRuntimeSuspect": cfprApMemoryRuntimeSuspect,
       "cfprApMemoryRuntimeThresholded": cfprApMemoryRuntimeThresholded,
       "cfprApMemoryRuntimeTimeCollected": cfprApMemoryRuntimeTimeCollected,
       "cfprApMemoryRuntimeTotal": cfprApMemoryRuntimeTotal,
       "cfprApMemoryRuntimeTotalAvg": cfprApMemoryRuntimeTotalAvg,
       "cfprApMemoryRuntimeTotalMax": cfprApMemoryRuntimeTotalMax,
       "cfprApMemoryRuntimeTotalMin": cfprApMemoryRuntimeTotalMin,
       "cfprApMemoryRuntimeType": cfprApMemoryRuntimeType,
       "cfprApMemoryRuntimeUpdate": cfprApMemoryRuntimeUpdate,
       "cfprApMemoryRuntimeHistTable": cfprApMemoryRuntimeHistTable,
       "cfprApMemoryRuntimeHistEntry": cfprApMemoryRuntimeHistEntry,
       "cfprApMemoryRuntimeHistInstanceId": cfprApMemoryRuntimeHistInstanceId,
       "cfprApMemoryRuntimeHistDn": cfprApMemoryRuntimeHistDn,
       "cfprApMemoryRuntimeHistRn": cfprApMemoryRuntimeHistRn,
       "cfprApMemoryRuntimeHistAvailable": cfprApMemoryRuntimeHistAvailable,
       "cfprApMemoryRuntimeHistAvailableAvg": cfprApMemoryRuntimeHistAvailableAvg,
       "cfprApMemoryRuntimeHistAvailableMax": cfprApMemoryRuntimeHistAvailableMax,
       "cfprApMemoryRuntimeHistAvailableMin": cfprApMemoryRuntimeHistAvailableMin,
       "cfprApMemoryRuntimeHistCached": cfprApMemoryRuntimeHistCached,
       "cfprApMemoryRuntimeHistCachedAvg": cfprApMemoryRuntimeHistCachedAvg,
       "cfprApMemoryRuntimeHistCachedMax": cfprApMemoryRuntimeHistCachedMax,
       "cfprApMemoryRuntimeHistCachedMin": cfprApMemoryRuntimeHistCachedMin,
       "cfprApMemoryRuntimeHistId": cfprApMemoryRuntimeHistId,
       "cfprApMemoryRuntimeHistMostRecent": cfprApMemoryRuntimeHistMostRecent,
       "cfprApMemoryRuntimeHistSuspect": cfprApMemoryRuntimeHistSuspect,
       "cfprApMemoryRuntimeHistThresholded": cfprApMemoryRuntimeHistThresholded,
       "cfprApMemoryRuntimeHistTimeCollected": cfprApMemoryRuntimeHistTimeCollected,
       "cfprApMemoryRuntimeHistTotal": cfprApMemoryRuntimeHistTotal,
       "cfprApMemoryRuntimeHistTotalAvg": cfprApMemoryRuntimeHistTotalAvg,
       "cfprApMemoryRuntimeHistTotalMax": cfprApMemoryRuntimeHistTotalMax,
       "cfprApMemoryRuntimeHistTotalMin": cfprApMemoryRuntimeHistTotalMin,
       "cfprApMemoryUnitTable": cfprApMemoryUnitTable,
       "cfprApMemoryUnitEntry": cfprApMemoryUnitEntry,
       "cfprApMemoryUnitInstanceId": cfprApMemoryUnitInstanceId,
       "cfprApMemoryUnitDn": cfprApMemoryUnitDn,
       "cfprApMemoryUnitRn": cfprApMemoryUnitRn,
       "cfprApMemoryUnitAdminState": cfprApMemoryUnitAdminState,
       "cfprApMemoryUnitArray": cfprApMemoryUnitArray,
       "cfprApMemoryUnitBank": cfprApMemoryUnitBank,
       "cfprApMemoryUnitCapacity": cfprApMemoryUnitCapacity,
       "cfprApMemoryUnitClock": cfprApMemoryUnitClock,
       "cfprApMemoryUnitFormFactor": cfprApMemoryUnitFormFactor,
       "cfprApMemoryUnitId": cfprApMemoryUnitId,
       "cfprApMemoryUnitLatency": cfprApMemoryUnitLatency,
       "cfprApMemoryUnitLocation": cfprApMemoryUnitLocation,
       "cfprApMemoryUnitLocationDn": cfprApMemoryUnitLocationDn,
       "cfprApMemoryUnitModel": cfprApMemoryUnitModel,
       "cfprApMemoryUnitOperQualifier": cfprApMemoryUnitOperQualifier,
       "cfprApMemoryUnitOperQualifierReason": cfprApMemoryUnitOperQualifierReason,
       "cfprApMemoryUnitOperState": cfprApMemoryUnitOperState,
       "cfprApMemoryUnitOperability": cfprApMemoryUnitOperability,
       "cfprApMemoryUnitPerf": cfprApMemoryUnitPerf,
       "cfprApMemoryUnitPower": cfprApMemoryUnitPower,
       "cfprApMemoryUnitPresence": cfprApMemoryUnitPresence,
       "cfprApMemoryUnitRevision": cfprApMemoryUnitRevision,
       "cfprApMemoryUnitSerial": cfprApMemoryUnitSerial,
       "cfprApMemoryUnitSet": cfprApMemoryUnitSet,
       "cfprApMemoryUnitSpeed": cfprApMemoryUnitSpeed,
       "cfprApMemoryUnitThermal": cfprApMemoryUnitThermal,
       "cfprApMemoryUnitType": cfprApMemoryUnitType,
       "cfprApMemoryUnitVendor": cfprApMemoryUnitVendor,
       "cfprApMemoryUnitVisibility": cfprApMemoryUnitVisibility,
       "cfprApMemoryUnitVoltage": cfprApMemoryUnitVoltage,
       "cfprApMemoryUnitWidth": cfprApMemoryUnitWidth,
       "cfprApMemoryUnitEnvStatsTable": cfprApMemoryUnitEnvStatsTable,
       "cfprApMemoryUnitEnvStatsEntry": cfprApMemoryUnitEnvStatsEntry,
       "cfprApMemoryUnitEnvStatsInstanceId": cfprApMemoryUnitEnvStatsInstanceId,
       "cfprApMemoryUnitEnvStatsDn": cfprApMemoryUnitEnvStatsDn,
       "cfprApMemoryUnitEnvStatsRn": cfprApMemoryUnitEnvStatsRn,
       "cfprApMemoryUnitEnvStatsIntervals": cfprApMemoryUnitEnvStatsIntervals,
       "cfprApMemoryUnitEnvStatsSuspect": cfprApMemoryUnitEnvStatsSuspect,
       "cfprApMemoryUnitEnvStatsTemperature": cfprApMemoryUnitEnvStatsTemperature,
       "cfprApMemoryUnitEnvStatsTemperatureAvg": cfprApMemoryUnitEnvStatsTemperatureAvg,
       "cfprApMemoryUnitEnvStatsTemperatureMax": cfprApMemoryUnitEnvStatsTemperatureMax,
       "cfprApMemoryUnitEnvStatsTemperatureMin": cfprApMemoryUnitEnvStatsTemperatureMin,
       "cfprApMemoryUnitEnvStatsThresholded": cfprApMemoryUnitEnvStatsThresholded,
       "cfprApMemoryUnitEnvStatsTimeCollected": cfprApMemoryUnitEnvStatsTimeCollected,
       "cfprApMemoryUnitEnvStatsUpdate": cfprApMemoryUnitEnvStatsUpdate,
       "cfprApMemoryUnitEnvStatsHistTable": cfprApMemoryUnitEnvStatsHistTable,
       "cfprApMemoryUnitEnvStatsHistEntry": cfprApMemoryUnitEnvStatsHistEntry,
       "cfprApMemoryUnitEnvStatsHistInstanceId": cfprApMemoryUnitEnvStatsHistInstanceId,
       "cfprApMemoryUnitEnvStatsHistDn": cfprApMemoryUnitEnvStatsHistDn,
       "cfprApMemoryUnitEnvStatsHistRn": cfprApMemoryUnitEnvStatsHistRn,
       "cfprApMemoryUnitEnvStatsHistId": cfprApMemoryUnitEnvStatsHistId,
       "cfprApMemoryUnitEnvStatsHistMostRecent": cfprApMemoryUnitEnvStatsHistMostRecent,
       "cfprApMemoryUnitEnvStatsHistSuspect": cfprApMemoryUnitEnvStatsHistSuspect,
       "cfprApMemoryUnitEnvStatsHistTemperature": cfprApMemoryUnitEnvStatsHistTemperature,
       "cfprApMemoryUnitEnvStatsHistTemperatureAvg": cfprApMemoryUnitEnvStatsHistTemperatureAvg,
       "cfprApMemoryUnitEnvStatsHistTemperatureMax": cfprApMemoryUnitEnvStatsHistTemperatureMax,
       "cfprApMemoryUnitEnvStatsHistTemperatureMin": cfprApMemoryUnitEnvStatsHistTemperatureMin,
       "cfprApMemoryUnitEnvStatsHistThresholded": cfprApMemoryUnitEnvStatsHistThresholded,
       "cfprApMemoryUnitEnvStatsHistTimeCollected": cfprApMemoryUnitEnvStatsHistTimeCollected}
)
