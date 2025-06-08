# SNMP MIB module (CISCO-FIREPOWER-PROCESSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-PROCESSOR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:12 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprEquipmentOperability,
 CfprEquipmentPowerState,
 CfprEquipmentPresence,
 CfprEquipmentSensorThresholdStatus,
 CfprMemoryVisibility,
 CfprProcessorEnvStatsHistThresholded,
 CfprProcessorEnvStatsThresholded,
 CfprProcessorErrorStatsThresholded,
 CfprProcessorQualArch,
 CfprProcessorRuntimeHistThresholded,
 CfprProcessorRuntimeThresholded,
 CfprProcessorUnitArch) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprEquipmentOperability",
    "CfprEquipmentPowerState",
    "CfprEquipmentPresence",
    "CfprEquipmentSensorThresholdStatus",
    "CfprMemoryVisibility",
    "CfprProcessorEnvStatsHistThresholded",
    "CfprProcessorEnvStatsThresholded",
    "CfprProcessorErrorStatsThresholded",
    "CfprProcessorQualArch",
    "CfprProcessorRuntimeHistThresholded",
    "CfprProcessorRuntimeThresholded",
    "CfprProcessorUnitArch")

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

cfprProcessorObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprProcessorCoreTable_Object = MibTable
cfprProcessorCoreTable = _CfprProcessorCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 1)
)
if mibBuilder.loadTexts:
    cfprProcessorCoreTable.setStatus("current")
_CfprProcessorCoreEntry_Object = MibTableRow
cfprProcessorCoreEntry = _CfprProcessorCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 1, 1)
)
cfprProcessorCoreEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorCoreInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorCoreEntry.setStatus("current")
_CfprProcessorCoreInstanceId_Type = CfprManagedObjectId
_CfprProcessorCoreInstanceId_Object = MibTableColumn
cfprProcessorCoreInstanceId = _CfprProcessorCoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 1, 1, 1),
    _CfprProcessorCoreInstanceId_Type()
)
cfprProcessorCoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorCoreInstanceId.setStatus("current")
_CfprProcessorCoreDn_Type = CfprManagedObjectDn
_CfprProcessorCoreDn_Object = MibTableColumn
cfprProcessorCoreDn = _CfprProcessorCoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 1, 1, 2),
    _CfprProcessorCoreDn_Type()
)
cfprProcessorCoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorCoreDn.setStatus("current")
_CfprProcessorCoreRn_Type = SnmpAdminString
_CfprProcessorCoreRn_Object = MibTableColumn
cfprProcessorCoreRn = _CfprProcessorCoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 1, 1, 3),
    _CfprProcessorCoreRn_Type()
)
cfprProcessorCoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorCoreRn.setStatus("current")
_CfprProcessorCoreId_Type = Gauge32
_CfprProcessorCoreId_Object = MibTableColumn
cfprProcessorCoreId = _CfprProcessorCoreId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 1, 1, 4),
    _CfprProcessorCoreId_Type()
)
cfprProcessorCoreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorCoreId.setStatus("current")
_CfprProcessorEnvStatsTable_Object = MibTable
cfprProcessorEnvStatsTable = _CfprProcessorEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2)
)
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsTable.setStatus("current")
_CfprProcessorEnvStatsEntry_Object = MibTableRow
cfprProcessorEnvStatsEntry = _CfprProcessorEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1)
)
cfprProcessorEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsEntry.setStatus("current")
_CfprProcessorEnvStatsInstanceId_Type = CfprManagedObjectId
_CfprProcessorEnvStatsInstanceId_Object = MibTableColumn
cfprProcessorEnvStatsInstanceId = _CfprProcessorEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 1),
    _CfprProcessorEnvStatsInstanceId_Type()
)
cfprProcessorEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsInstanceId.setStatus("current")
_CfprProcessorEnvStatsDn_Type = CfprManagedObjectDn
_CfprProcessorEnvStatsDn_Object = MibTableColumn
cfprProcessorEnvStatsDn = _CfprProcessorEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 2),
    _CfprProcessorEnvStatsDn_Type()
)
cfprProcessorEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsDn.setStatus("current")
_CfprProcessorEnvStatsRn_Type = SnmpAdminString
_CfprProcessorEnvStatsRn_Object = MibTableColumn
cfprProcessorEnvStatsRn = _CfprProcessorEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 3),
    _CfprProcessorEnvStatsRn_Type()
)
cfprProcessorEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsRn.setStatus("current")
_CfprProcessorEnvStatsInputCurrent_Type = Integer32
_CfprProcessorEnvStatsInputCurrent_Object = MibTableColumn
cfprProcessorEnvStatsInputCurrent = _CfprProcessorEnvStatsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 4),
    _CfprProcessorEnvStatsInputCurrent_Type()
)
cfprProcessorEnvStatsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsInputCurrent.setStatus("current")
_CfprProcessorEnvStatsInputCurrentAvg_Type = Integer32
_CfprProcessorEnvStatsInputCurrentAvg_Object = MibTableColumn
cfprProcessorEnvStatsInputCurrentAvg = _CfprProcessorEnvStatsInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 5),
    _CfprProcessorEnvStatsInputCurrentAvg_Type()
)
cfprProcessorEnvStatsInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsInputCurrentAvg.setStatus("current")
_CfprProcessorEnvStatsInputCurrentMax_Type = Integer32
_CfprProcessorEnvStatsInputCurrentMax_Object = MibTableColumn
cfprProcessorEnvStatsInputCurrentMax = _CfprProcessorEnvStatsInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 6),
    _CfprProcessorEnvStatsInputCurrentMax_Type()
)
cfprProcessorEnvStatsInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsInputCurrentMax.setStatus("current")
_CfprProcessorEnvStatsInputCurrentMin_Type = Integer32
_CfprProcessorEnvStatsInputCurrentMin_Object = MibTableColumn
cfprProcessorEnvStatsInputCurrentMin = _CfprProcessorEnvStatsInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 7),
    _CfprProcessorEnvStatsInputCurrentMin_Type()
)
cfprProcessorEnvStatsInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsInputCurrentMin.setStatus("current")
_CfprProcessorEnvStatsIntervals_Type = Gauge32
_CfprProcessorEnvStatsIntervals_Object = MibTableColumn
cfprProcessorEnvStatsIntervals = _CfprProcessorEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 8),
    _CfprProcessorEnvStatsIntervals_Type()
)
cfprProcessorEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsIntervals.setStatus("current")
_CfprProcessorEnvStatsSuspect_Type = TruthValue
_CfprProcessorEnvStatsSuspect_Object = MibTableColumn
cfprProcessorEnvStatsSuspect = _CfprProcessorEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 9),
    _CfprProcessorEnvStatsSuspect_Type()
)
cfprProcessorEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsSuspect.setStatus("current")
_CfprProcessorEnvStatsTemperature_Type = Integer32
_CfprProcessorEnvStatsTemperature_Object = MibTableColumn
cfprProcessorEnvStatsTemperature = _CfprProcessorEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 10),
    _CfprProcessorEnvStatsTemperature_Type()
)
cfprProcessorEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsTemperature.setStatus("current")
_CfprProcessorEnvStatsTemperatureAvg_Type = Integer32
_CfprProcessorEnvStatsTemperatureAvg_Object = MibTableColumn
cfprProcessorEnvStatsTemperatureAvg = _CfprProcessorEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 11),
    _CfprProcessorEnvStatsTemperatureAvg_Type()
)
cfprProcessorEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsTemperatureAvg.setStatus("current")
_CfprProcessorEnvStatsTemperatureMax_Type = Integer32
_CfprProcessorEnvStatsTemperatureMax_Object = MibTableColumn
cfprProcessorEnvStatsTemperatureMax = _CfprProcessorEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 12),
    _CfprProcessorEnvStatsTemperatureMax_Type()
)
cfprProcessorEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsTemperatureMax.setStatus("current")
_CfprProcessorEnvStatsTemperatureMin_Type = Integer32
_CfprProcessorEnvStatsTemperatureMin_Object = MibTableColumn
cfprProcessorEnvStatsTemperatureMin = _CfprProcessorEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 13),
    _CfprProcessorEnvStatsTemperatureMin_Type()
)
cfprProcessorEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsTemperatureMin.setStatus("current")
_CfprProcessorEnvStatsThresholded_Type = CfprProcessorEnvStatsThresholded
_CfprProcessorEnvStatsThresholded_Object = MibTableColumn
cfprProcessorEnvStatsThresholded = _CfprProcessorEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 14),
    _CfprProcessorEnvStatsThresholded_Type()
)
cfprProcessorEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsThresholded.setStatus("current")
_CfprProcessorEnvStatsTimeCollected_Type = DateAndTime
_CfprProcessorEnvStatsTimeCollected_Object = MibTableColumn
cfprProcessorEnvStatsTimeCollected = _CfprProcessorEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 15),
    _CfprProcessorEnvStatsTimeCollected_Type()
)
cfprProcessorEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsTimeCollected.setStatus("current")
_CfprProcessorEnvStatsUpdate_Type = Gauge32
_CfprProcessorEnvStatsUpdate_Object = MibTableColumn
cfprProcessorEnvStatsUpdate = _CfprProcessorEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 2, 1, 16),
    _CfprProcessorEnvStatsUpdate_Type()
)
cfprProcessorEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsUpdate.setStatus("current")
_CfprProcessorEnvStatsHistTable_Object = MibTable
cfprProcessorEnvStatsHistTable = _CfprProcessorEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3)
)
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistTable.setStatus("current")
_CfprProcessorEnvStatsHistEntry_Object = MibTableRow
cfprProcessorEnvStatsHistEntry = _CfprProcessorEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1)
)
cfprProcessorEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistEntry.setStatus("current")
_CfprProcessorEnvStatsHistInstanceId_Type = CfprManagedObjectId
_CfprProcessorEnvStatsHistInstanceId_Object = MibTableColumn
cfprProcessorEnvStatsHistInstanceId = _CfprProcessorEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 1),
    _CfprProcessorEnvStatsHistInstanceId_Type()
)
cfprProcessorEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistInstanceId.setStatus("current")
_CfprProcessorEnvStatsHistDn_Type = CfprManagedObjectDn
_CfprProcessorEnvStatsHistDn_Object = MibTableColumn
cfprProcessorEnvStatsHistDn = _CfprProcessorEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 2),
    _CfprProcessorEnvStatsHistDn_Type()
)
cfprProcessorEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistDn.setStatus("current")
_CfprProcessorEnvStatsHistRn_Type = SnmpAdminString
_CfprProcessorEnvStatsHistRn_Object = MibTableColumn
cfprProcessorEnvStatsHistRn = _CfprProcessorEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 3),
    _CfprProcessorEnvStatsHistRn_Type()
)
cfprProcessorEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistRn.setStatus("current")
_CfprProcessorEnvStatsHistId_Type = Unsigned64
_CfprProcessorEnvStatsHistId_Object = MibTableColumn
cfprProcessorEnvStatsHistId = _CfprProcessorEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 4),
    _CfprProcessorEnvStatsHistId_Type()
)
cfprProcessorEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistId.setStatus("current")
_CfprProcessorEnvStatsHistInputCurrent_Type = Integer32
_CfprProcessorEnvStatsHistInputCurrent_Object = MibTableColumn
cfprProcessorEnvStatsHistInputCurrent = _CfprProcessorEnvStatsHistInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 5),
    _CfprProcessorEnvStatsHistInputCurrent_Type()
)
cfprProcessorEnvStatsHistInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistInputCurrent.setStatus("current")
_CfprProcessorEnvStatsHistInputCurrentAvg_Type = Integer32
_CfprProcessorEnvStatsHistInputCurrentAvg_Object = MibTableColumn
cfprProcessorEnvStatsHistInputCurrentAvg = _CfprProcessorEnvStatsHistInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 6),
    _CfprProcessorEnvStatsHistInputCurrentAvg_Type()
)
cfprProcessorEnvStatsHistInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistInputCurrentAvg.setStatus("current")
_CfprProcessorEnvStatsHistInputCurrentMax_Type = Integer32
_CfprProcessorEnvStatsHistInputCurrentMax_Object = MibTableColumn
cfprProcessorEnvStatsHistInputCurrentMax = _CfprProcessorEnvStatsHistInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 7),
    _CfprProcessorEnvStatsHistInputCurrentMax_Type()
)
cfprProcessorEnvStatsHistInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistInputCurrentMax.setStatus("current")
_CfprProcessorEnvStatsHistInputCurrentMin_Type = Integer32
_CfprProcessorEnvStatsHistInputCurrentMin_Object = MibTableColumn
cfprProcessorEnvStatsHistInputCurrentMin = _CfprProcessorEnvStatsHistInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 8),
    _CfprProcessorEnvStatsHistInputCurrentMin_Type()
)
cfprProcessorEnvStatsHistInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistInputCurrentMin.setStatus("current")
_CfprProcessorEnvStatsHistMostRecent_Type = TruthValue
_CfprProcessorEnvStatsHistMostRecent_Object = MibTableColumn
cfprProcessorEnvStatsHistMostRecent = _CfprProcessorEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 9),
    _CfprProcessorEnvStatsHistMostRecent_Type()
)
cfprProcessorEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistMostRecent.setStatus("current")
_CfprProcessorEnvStatsHistSuspect_Type = TruthValue
_CfprProcessorEnvStatsHistSuspect_Object = MibTableColumn
cfprProcessorEnvStatsHistSuspect = _CfprProcessorEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 10),
    _CfprProcessorEnvStatsHistSuspect_Type()
)
cfprProcessorEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistSuspect.setStatus("current")
_CfprProcessorEnvStatsHistTemperature_Type = Integer32
_CfprProcessorEnvStatsHistTemperature_Object = MibTableColumn
cfprProcessorEnvStatsHistTemperature = _CfprProcessorEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 11),
    _CfprProcessorEnvStatsHistTemperature_Type()
)
cfprProcessorEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistTemperature.setStatus("current")
_CfprProcessorEnvStatsHistTemperatureAvg_Type = Integer32
_CfprProcessorEnvStatsHistTemperatureAvg_Object = MibTableColumn
cfprProcessorEnvStatsHistTemperatureAvg = _CfprProcessorEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 12),
    _CfprProcessorEnvStatsHistTemperatureAvg_Type()
)
cfprProcessorEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistTemperatureAvg.setStatus("current")
_CfprProcessorEnvStatsHistTemperatureMax_Type = Integer32
_CfprProcessorEnvStatsHistTemperatureMax_Object = MibTableColumn
cfprProcessorEnvStatsHistTemperatureMax = _CfprProcessorEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 13),
    _CfprProcessorEnvStatsHistTemperatureMax_Type()
)
cfprProcessorEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistTemperatureMax.setStatus("current")
_CfprProcessorEnvStatsHistTemperatureMin_Type = Integer32
_CfprProcessorEnvStatsHistTemperatureMin_Object = MibTableColumn
cfprProcessorEnvStatsHistTemperatureMin = _CfprProcessorEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 14),
    _CfprProcessorEnvStatsHistTemperatureMin_Type()
)
cfprProcessorEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistTemperatureMin.setStatus("current")
_CfprProcessorEnvStatsHistThresholded_Type = CfprProcessorEnvStatsHistThresholded
_CfprProcessorEnvStatsHistThresholded_Object = MibTableColumn
cfprProcessorEnvStatsHistThresholded = _CfprProcessorEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 15),
    _CfprProcessorEnvStatsHistThresholded_Type()
)
cfprProcessorEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistThresholded.setStatus("current")
_CfprProcessorEnvStatsHistTimeCollected_Type = DateAndTime
_CfprProcessorEnvStatsHistTimeCollected_Object = MibTableColumn
cfprProcessorEnvStatsHistTimeCollected = _CfprProcessorEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 3, 1, 16),
    _CfprProcessorEnvStatsHistTimeCollected_Type()
)
cfprProcessorEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorEnvStatsHistTimeCollected.setStatus("current")
_CfprProcessorErrorStatsTable_Object = MibTable
cfprProcessorErrorStatsTable = _CfprProcessorErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4)
)
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsTable.setStatus("current")
_CfprProcessorErrorStatsEntry_Object = MibTableRow
cfprProcessorErrorStatsEntry = _CfprProcessorErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1)
)
cfprProcessorErrorStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorErrorStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsEntry.setStatus("current")
_CfprProcessorErrorStatsInstanceId_Type = CfprManagedObjectId
_CfprProcessorErrorStatsInstanceId_Object = MibTableColumn
cfprProcessorErrorStatsInstanceId = _CfprProcessorErrorStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 1),
    _CfprProcessorErrorStatsInstanceId_Type()
)
cfprProcessorErrorStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsInstanceId.setStatus("current")
_CfprProcessorErrorStatsDn_Type = CfprManagedObjectDn
_CfprProcessorErrorStatsDn_Object = MibTableColumn
cfprProcessorErrorStatsDn = _CfprProcessorErrorStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 2),
    _CfprProcessorErrorStatsDn_Type()
)
cfprProcessorErrorStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsDn.setStatus("current")
_CfprProcessorErrorStatsRn_Type = SnmpAdminString
_CfprProcessorErrorStatsRn_Object = MibTableColumn
cfprProcessorErrorStatsRn = _CfprProcessorErrorStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 3),
    _CfprProcessorErrorStatsRn_Type()
)
cfprProcessorErrorStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsRn.setStatus("current")
_CfprProcessorErrorStatsIntervals_Type = Gauge32
_CfprProcessorErrorStatsIntervals_Object = MibTableColumn
cfprProcessorErrorStatsIntervals = _CfprProcessorErrorStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 4),
    _CfprProcessorErrorStatsIntervals_Type()
)
cfprProcessorErrorStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsIntervals.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors_Type = Counter32
_CfprProcessorErrorStatsMirroringInterSockErrors_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors = _CfprProcessorErrorStatsMirroringInterSockErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 5),
    _CfprProcessorErrorStatsMirroringInterSockErrors_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors15Min_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors15Min_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors15Min = _CfprProcessorErrorStatsMirroringInterSockErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 6),
    _CfprProcessorErrorStatsMirroringInterSockErrors15Min_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors15Min.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors15MinH_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors15MinH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors15MinH = _CfprProcessorErrorStatsMirroringInterSockErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 7),
    _CfprProcessorErrorStatsMirroringInterSockErrors15MinH_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors15MinH.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors1Day_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors1Day_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors1Day = _CfprProcessorErrorStatsMirroringInterSockErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 8),
    _CfprProcessorErrorStatsMirroringInterSockErrors1Day_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors1Day.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors1DayH_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors1DayH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors1DayH = _CfprProcessorErrorStatsMirroringInterSockErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 9),
    _CfprProcessorErrorStatsMirroringInterSockErrors1DayH_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors1DayH.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors1Hour_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors1Hour_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors1Hour = _CfprProcessorErrorStatsMirroringInterSockErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 10),
    _CfprProcessorErrorStatsMirroringInterSockErrors1Hour_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors1Hour.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors1HourH_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors1HourH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors1HourH = _CfprProcessorErrorStatsMirroringInterSockErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 11),
    _CfprProcessorErrorStatsMirroringInterSockErrors1HourH_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors1HourH.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors1Week_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors1Week_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors1Week = _CfprProcessorErrorStatsMirroringInterSockErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 12),
    _CfprProcessorErrorStatsMirroringInterSockErrors1Week_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors1Week.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors1WeekH_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors1WeekH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors1WeekH = _CfprProcessorErrorStatsMirroringInterSockErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 13),
    _CfprProcessorErrorStatsMirroringInterSockErrors1WeekH_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors1WeekH.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors2Weeks_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors2Weeks_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors2Weeks = _CfprProcessorErrorStatsMirroringInterSockErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 14),
    _CfprProcessorErrorStatsMirroringInterSockErrors2Weeks_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors2Weeks.setStatus("current")
_CfprProcessorErrorStatsMirroringInterSockErrors2WeeksH_Type = Gauge32
_CfprProcessorErrorStatsMirroringInterSockErrors2WeeksH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringInterSockErrors2WeeksH = _CfprProcessorErrorStatsMirroringInterSockErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 15),
    _CfprProcessorErrorStatsMirroringInterSockErrors2WeeksH_Type()
)
cfprProcessorErrorStatsMirroringInterSockErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringInterSockErrors2WeeksH.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors_Type = Counter32
_CfprProcessorErrorStatsMirroringIntraSockErrors_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors = _CfprProcessorErrorStatsMirroringIntraSockErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 16),
    _CfprProcessorErrorStatsMirroringIntraSockErrors_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors15Min_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors15Min_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors15Min = _CfprProcessorErrorStatsMirroringIntraSockErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 17),
    _CfprProcessorErrorStatsMirroringIntraSockErrors15Min_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors15Min.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors15MinH_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors15MinH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors15MinH = _CfprProcessorErrorStatsMirroringIntraSockErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 18),
    _CfprProcessorErrorStatsMirroringIntraSockErrors15MinH_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors15MinH.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors1Day_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors1Day_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors1Day = _CfprProcessorErrorStatsMirroringIntraSockErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 19),
    _CfprProcessorErrorStatsMirroringIntraSockErrors1Day_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors1Day.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors1DayH_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors1DayH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors1DayH = _CfprProcessorErrorStatsMirroringIntraSockErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 20),
    _CfprProcessorErrorStatsMirroringIntraSockErrors1DayH_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors1DayH.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors1Hour_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors1Hour_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors1Hour = _CfprProcessorErrorStatsMirroringIntraSockErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 21),
    _CfprProcessorErrorStatsMirroringIntraSockErrors1Hour_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors1Hour.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors1HourH_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors1HourH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors1HourH = _CfprProcessorErrorStatsMirroringIntraSockErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 22),
    _CfprProcessorErrorStatsMirroringIntraSockErrors1HourH_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors1HourH.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors1Week_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors1Week_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors1Week = _CfprProcessorErrorStatsMirroringIntraSockErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 23),
    _CfprProcessorErrorStatsMirroringIntraSockErrors1Week_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors1Week.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors1WeekH_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors1WeekH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors1WeekH = _CfprProcessorErrorStatsMirroringIntraSockErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 24),
    _CfprProcessorErrorStatsMirroringIntraSockErrors1WeekH_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors1WeekH.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors2Weeks_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors2Weeks_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors2Weeks = _CfprProcessorErrorStatsMirroringIntraSockErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 25),
    _CfprProcessorErrorStatsMirroringIntraSockErrors2Weeks_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors2Weeks.setStatus("current")
_CfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Type = Gauge32
_CfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Object = MibTableColumn
cfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH = _CfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 26),
    _CfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Type()
)
cfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors_Type = Counter32
_CfprProcessorErrorStatsSmiLinkCorrErrors_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors = _CfprProcessorErrorStatsSmiLinkCorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 27),
    _CfprProcessorErrorStatsSmiLinkCorrErrors_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors15Min_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors15Min_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors15Min = _CfprProcessorErrorStatsSmiLinkCorrErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 28),
    _CfprProcessorErrorStatsSmiLinkCorrErrors15Min_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors15Min.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors15MinH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors15MinH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors15MinH = _CfprProcessorErrorStatsSmiLinkCorrErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 29),
    _CfprProcessorErrorStatsSmiLinkCorrErrors15MinH_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors15MinH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors1Day_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors1Day_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors1Day = _CfprProcessorErrorStatsSmiLinkCorrErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 30),
    _CfprProcessorErrorStatsSmiLinkCorrErrors1Day_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors1Day.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors1DayH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors1DayH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors1DayH = _CfprProcessorErrorStatsSmiLinkCorrErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 31),
    _CfprProcessorErrorStatsSmiLinkCorrErrors1DayH_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors1DayH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors1Hour_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors1Hour_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors1Hour = _CfprProcessorErrorStatsSmiLinkCorrErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 32),
    _CfprProcessorErrorStatsSmiLinkCorrErrors1Hour_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors1Hour.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors1HourH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors1HourH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors1HourH = _CfprProcessorErrorStatsSmiLinkCorrErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 33),
    _CfprProcessorErrorStatsSmiLinkCorrErrors1HourH_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors1HourH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors1Week_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors1Week_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors1Week = _CfprProcessorErrorStatsSmiLinkCorrErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 34),
    _CfprProcessorErrorStatsSmiLinkCorrErrors1Week_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors1Week.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors1WeekH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors1WeekH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors1WeekH = _CfprProcessorErrorStatsSmiLinkCorrErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 35),
    _CfprProcessorErrorStatsSmiLinkCorrErrors1WeekH_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors1WeekH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors2Weeks_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors2Weeks_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors2Weeks = _CfprProcessorErrorStatsSmiLinkCorrErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 36),
    _CfprProcessorErrorStatsSmiLinkCorrErrors2Weeks_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors2Weeks.setStatus("current")
_CfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH = _CfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 37),
    _CfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Type()
)
cfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors_Type = Counter32
_CfprProcessorErrorStatsSmiLinkUncorrErrors_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors = _CfprProcessorErrorStatsSmiLinkUncorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 38),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors15Min_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors15Min_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors15Min = _CfprProcessorErrorStatsSmiLinkUncorrErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 39),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors15Min_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors15Min.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors15MinH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors15MinH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors15MinH = _CfprProcessorErrorStatsSmiLinkUncorrErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 40),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors15MinH_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors15MinH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors1Day_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors1Day_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors1Day = _CfprProcessorErrorStatsSmiLinkUncorrErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 41),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors1Day_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors1Day.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors1DayH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors1DayH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors1DayH = _CfprProcessorErrorStatsSmiLinkUncorrErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 42),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors1DayH_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors1DayH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors1Hour_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors1Hour_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors1Hour = _CfprProcessorErrorStatsSmiLinkUncorrErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 43),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors1Hour_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors1Hour.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors1HourH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors1HourH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors1HourH = _CfprProcessorErrorStatsSmiLinkUncorrErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 44),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors1HourH_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors1HourH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors1Week_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors1Week_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors1Week = _CfprProcessorErrorStatsSmiLinkUncorrErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 45),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors1Week_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors1Week.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH = _CfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 46),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks = _CfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 47),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks.setStatus("current")
_CfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Type = Gauge32
_CfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Object = MibTableColumn
cfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH = _CfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 48),
    _CfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Type()
)
cfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH.setStatus("current")
_CfprProcessorErrorStatsSparingErrors_Type = Counter32
_CfprProcessorErrorStatsSparingErrors_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors = _CfprProcessorErrorStatsSparingErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 49),
    _CfprProcessorErrorStatsSparingErrors_Type()
)
cfprProcessorErrorStatsSparingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors.setStatus("current")
_CfprProcessorErrorStatsSparingErrors15Min_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors15Min_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors15Min = _CfprProcessorErrorStatsSparingErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 50),
    _CfprProcessorErrorStatsSparingErrors15Min_Type()
)
cfprProcessorErrorStatsSparingErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors15Min.setStatus("current")
_CfprProcessorErrorStatsSparingErrors15MinH_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors15MinH_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors15MinH = _CfprProcessorErrorStatsSparingErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 51),
    _CfprProcessorErrorStatsSparingErrors15MinH_Type()
)
cfprProcessorErrorStatsSparingErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors15MinH.setStatus("current")
_CfprProcessorErrorStatsSparingErrors1Day_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors1Day_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors1Day = _CfprProcessorErrorStatsSparingErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 52),
    _CfprProcessorErrorStatsSparingErrors1Day_Type()
)
cfprProcessorErrorStatsSparingErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors1Day.setStatus("current")
_CfprProcessorErrorStatsSparingErrors1DayH_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors1DayH_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors1DayH = _CfprProcessorErrorStatsSparingErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 53),
    _CfprProcessorErrorStatsSparingErrors1DayH_Type()
)
cfprProcessorErrorStatsSparingErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors1DayH.setStatus("current")
_CfprProcessorErrorStatsSparingErrors1Hour_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors1Hour_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors1Hour = _CfprProcessorErrorStatsSparingErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 54),
    _CfprProcessorErrorStatsSparingErrors1Hour_Type()
)
cfprProcessorErrorStatsSparingErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors1Hour.setStatus("current")
_CfprProcessorErrorStatsSparingErrors1HourH_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors1HourH_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors1HourH = _CfprProcessorErrorStatsSparingErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 55),
    _CfprProcessorErrorStatsSparingErrors1HourH_Type()
)
cfprProcessorErrorStatsSparingErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors1HourH.setStatus("current")
_CfprProcessorErrorStatsSparingErrors1Week_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors1Week_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors1Week = _CfprProcessorErrorStatsSparingErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 56),
    _CfprProcessorErrorStatsSparingErrors1Week_Type()
)
cfprProcessorErrorStatsSparingErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors1Week.setStatus("current")
_CfprProcessorErrorStatsSparingErrors1WeekH_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors1WeekH_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors1WeekH = _CfprProcessorErrorStatsSparingErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 57),
    _CfprProcessorErrorStatsSparingErrors1WeekH_Type()
)
cfprProcessorErrorStatsSparingErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors1WeekH.setStatus("current")
_CfprProcessorErrorStatsSparingErrors2Weeks_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors2Weeks_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors2Weeks = _CfprProcessorErrorStatsSparingErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 58),
    _CfprProcessorErrorStatsSparingErrors2Weeks_Type()
)
cfprProcessorErrorStatsSparingErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors2Weeks.setStatus("current")
_CfprProcessorErrorStatsSparingErrors2WeeksH_Type = Gauge32
_CfprProcessorErrorStatsSparingErrors2WeeksH_Object = MibTableColumn
cfprProcessorErrorStatsSparingErrors2WeeksH = _CfprProcessorErrorStatsSparingErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 59),
    _CfprProcessorErrorStatsSparingErrors2WeeksH_Type()
)
cfprProcessorErrorStatsSparingErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSparingErrors2WeeksH.setStatus("current")
_CfprProcessorErrorStatsSuspect_Type = TruthValue
_CfprProcessorErrorStatsSuspect_Object = MibTableColumn
cfprProcessorErrorStatsSuspect = _CfprProcessorErrorStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 60),
    _CfprProcessorErrorStatsSuspect_Type()
)
cfprProcessorErrorStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsSuspect.setStatus("current")
_CfprProcessorErrorStatsThresholded_Type = CfprProcessorErrorStatsThresholded
_CfprProcessorErrorStatsThresholded_Object = MibTableColumn
cfprProcessorErrorStatsThresholded = _CfprProcessorErrorStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 61),
    _CfprProcessorErrorStatsThresholded_Type()
)
cfprProcessorErrorStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsThresholded.setStatus("current")
_CfprProcessorErrorStatsTimeCollected_Type = DateAndTime
_CfprProcessorErrorStatsTimeCollected_Object = MibTableColumn
cfprProcessorErrorStatsTimeCollected = _CfprProcessorErrorStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 62),
    _CfprProcessorErrorStatsTimeCollected_Type()
)
cfprProcessorErrorStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsTimeCollected.setStatus("current")
_CfprProcessorErrorStatsUpdate_Type = Gauge32
_CfprProcessorErrorStatsUpdate_Object = MibTableColumn
cfprProcessorErrorStatsUpdate = _CfprProcessorErrorStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 4, 1, 63),
    _CfprProcessorErrorStatsUpdate_Type()
)
cfprProcessorErrorStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorErrorStatsUpdate.setStatus("current")
_CfprProcessorQualTable_Object = MibTable
cfprProcessorQualTable = _CfprProcessorQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5)
)
if mibBuilder.loadTexts:
    cfprProcessorQualTable.setStatus("current")
_CfprProcessorQualEntry_Object = MibTableRow
cfprProcessorQualEntry = _CfprProcessorQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1)
)
cfprProcessorQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorQualEntry.setStatus("current")
_CfprProcessorQualInstanceId_Type = CfprManagedObjectId
_CfprProcessorQualInstanceId_Object = MibTableColumn
cfprProcessorQualInstanceId = _CfprProcessorQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 1),
    _CfprProcessorQualInstanceId_Type()
)
cfprProcessorQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorQualInstanceId.setStatus("current")
_CfprProcessorQualDn_Type = CfprManagedObjectDn
_CfprProcessorQualDn_Object = MibTableColumn
cfprProcessorQualDn = _CfprProcessorQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 2),
    _CfprProcessorQualDn_Type()
)
cfprProcessorQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualDn.setStatus("current")
_CfprProcessorQualRn_Type = SnmpAdminString
_CfprProcessorQualRn_Object = MibTableColumn
cfprProcessorQualRn = _CfprProcessorQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 3),
    _CfprProcessorQualRn_Type()
)
cfprProcessorQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualRn.setStatus("current")
_CfprProcessorQualArch_Type = CfprProcessorQualArch
_CfprProcessorQualArch_Object = MibTableColumn
cfprProcessorQualArch = _CfprProcessorQualArch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 4),
    _CfprProcessorQualArch_Type()
)
cfprProcessorQualArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualArch.setStatus("current")
_CfprProcessorQualMaxCores_Type = Gauge32
_CfprProcessorQualMaxCores_Object = MibTableColumn
cfprProcessorQualMaxCores = _CfprProcessorQualMaxCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 5),
    _CfprProcessorQualMaxCores_Type()
)
cfprProcessorQualMaxCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualMaxCores.setStatus("current")
_CfprProcessorQualMaxProcs_Type = Gauge32
_CfprProcessorQualMaxProcs_Object = MibTableColumn
cfprProcessorQualMaxProcs = _CfprProcessorQualMaxProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 6),
    _CfprProcessorQualMaxProcs_Type()
)
cfprProcessorQualMaxProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualMaxProcs.setStatus("current")
_CfprProcessorQualMaxThreads_Type = Gauge32
_CfprProcessorQualMaxThreads_Object = MibTableColumn
cfprProcessorQualMaxThreads = _CfprProcessorQualMaxThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 7),
    _CfprProcessorQualMaxThreads_Type()
)
cfprProcessorQualMaxThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualMaxThreads.setStatus("current")
_CfprProcessorQualMinCores_Type = Gauge32
_CfprProcessorQualMinCores_Object = MibTableColumn
cfprProcessorQualMinCores = _CfprProcessorQualMinCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 8),
    _CfprProcessorQualMinCores_Type()
)
cfprProcessorQualMinCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualMinCores.setStatus("current")
_CfprProcessorQualMinProcs_Type = Gauge32
_CfprProcessorQualMinProcs_Object = MibTableColumn
cfprProcessorQualMinProcs = _CfprProcessorQualMinProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 9),
    _CfprProcessorQualMinProcs_Type()
)
cfprProcessorQualMinProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualMinProcs.setStatus("current")
_CfprProcessorQualMinThreads_Type = Gauge32
_CfprProcessorQualMinThreads_Object = MibTableColumn
cfprProcessorQualMinThreads = _CfprProcessorQualMinThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 10),
    _CfprProcessorQualMinThreads_Type()
)
cfprProcessorQualMinThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualMinThreads.setStatus("current")
_CfprProcessorQualModel_Type = SnmpAdminString
_CfprProcessorQualModel_Object = MibTableColumn
cfprProcessorQualModel = _CfprProcessorQualModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 11),
    _CfprProcessorQualModel_Type()
)
cfprProcessorQualModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualModel.setStatus("current")
_CfprProcessorQualSpeed_Type = Integer32
_CfprProcessorQualSpeed_Object = MibTableColumn
cfprProcessorQualSpeed = _CfprProcessorQualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 12),
    _CfprProcessorQualSpeed_Type()
)
cfprProcessorQualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualSpeed.setStatus("current")
_CfprProcessorQualStepping_Type = Gauge32
_CfprProcessorQualStepping_Object = MibTableColumn
cfprProcessorQualStepping = _CfprProcessorQualStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 5, 1, 13),
    _CfprProcessorQualStepping_Type()
)
cfprProcessorQualStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorQualStepping.setStatus("current")
_CfprProcessorRuntimeTable_Object = MibTable
cfprProcessorRuntimeTable = _CfprProcessorRuntimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6)
)
if mibBuilder.loadTexts:
    cfprProcessorRuntimeTable.setStatus("current")
_CfprProcessorRuntimeEntry_Object = MibTableRow
cfprProcessorRuntimeEntry = _CfprProcessorRuntimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1)
)
cfprProcessorRuntimeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorRuntimeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorRuntimeEntry.setStatus("current")
_CfprProcessorRuntimeInstanceId_Type = CfprManagedObjectId
_CfprProcessorRuntimeInstanceId_Object = MibTableColumn
cfprProcessorRuntimeInstanceId = _CfprProcessorRuntimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 1),
    _CfprProcessorRuntimeInstanceId_Type()
)
cfprProcessorRuntimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeInstanceId.setStatus("current")
_CfprProcessorRuntimeDn_Type = CfprManagedObjectDn
_CfprProcessorRuntimeDn_Object = MibTableColumn
cfprProcessorRuntimeDn = _CfprProcessorRuntimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 2),
    _CfprProcessorRuntimeDn_Type()
)
cfprProcessorRuntimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeDn.setStatus("current")
_CfprProcessorRuntimeRn_Type = SnmpAdminString
_CfprProcessorRuntimeRn_Object = MibTableColumn
cfprProcessorRuntimeRn = _CfprProcessorRuntimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 3),
    _CfprProcessorRuntimeRn_Type()
)
cfprProcessorRuntimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeRn.setStatus("current")
_CfprProcessorRuntimeIntervals_Type = Gauge32
_CfprProcessorRuntimeIntervals_Object = MibTableColumn
cfprProcessorRuntimeIntervals = _CfprProcessorRuntimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 4),
    _CfprProcessorRuntimeIntervals_Type()
)
cfprProcessorRuntimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeIntervals.setStatus("current")
_CfprProcessorRuntimeLoad_Type = Integer32
_CfprProcessorRuntimeLoad_Object = MibTableColumn
cfprProcessorRuntimeLoad = _CfprProcessorRuntimeLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 5),
    _CfprProcessorRuntimeLoad_Type()
)
cfprProcessorRuntimeLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeLoad.setStatus("current")
_CfprProcessorRuntimeLoadAvg_Type = Integer32
_CfprProcessorRuntimeLoadAvg_Object = MibTableColumn
cfprProcessorRuntimeLoadAvg = _CfprProcessorRuntimeLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 6),
    _CfprProcessorRuntimeLoadAvg_Type()
)
cfprProcessorRuntimeLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeLoadAvg.setStatus("current")
_CfprProcessorRuntimeLoadMax_Type = Integer32
_CfprProcessorRuntimeLoadMax_Object = MibTableColumn
cfprProcessorRuntimeLoadMax = _CfprProcessorRuntimeLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 7),
    _CfprProcessorRuntimeLoadMax_Type()
)
cfprProcessorRuntimeLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeLoadMax.setStatus("current")
_CfprProcessorRuntimeLoadMin_Type = Integer32
_CfprProcessorRuntimeLoadMin_Object = MibTableColumn
cfprProcessorRuntimeLoadMin = _CfprProcessorRuntimeLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 8),
    _CfprProcessorRuntimeLoadMin_Type()
)
cfprProcessorRuntimeLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeLoadMin.setStatus("current")
_CfprProcessorRuntimeSuspect_Type = TruthValue
_CfprProcessorRuntimeSuspect_Object = MibTableColumn
cfprProcessorRuntimeSuspect = _CfprProcessorRuntimeSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 9),
    _CfprProcessorRuntimeSuspect_Type()
)
cfprProcessorRuntimeSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeSuspect.setStatus("current")
_CfprProcessorRuntimeThresholded_Type = CfprProcessorRuntimeThresholded
_CfprProcessorRuntimeThresholded_Object = MibTableColumn
cfprProcessorRuntimeThresholded = _CfprProcessorRuntimeThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 10),
    _CfprProcessorRuntimeThresholded_Type()
)
cfprProcessorRuntimeThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeThresholded.setStatus("current")
_CfprProcessorRuntimeTimeCollected_Type = DateAndTime
_CfprProcessorRuntimeTimeCollected_Object = MibTableColumn
cfprProcessorRuntimeTimeCollected = _CfprProcessorRuntimeTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 11),
    _CfprProcessorRuntimeTimeCollected_Type()
)
cfprProcessorRuntimeTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeTimeCollected.setStatus("current")
_CfprProcessorRuntimeUpdate_Type = Gauge32
_CfprProcessorRuntimeUpdate_Object = MibTableColumn
cfprProcessorRuntimeUpdate = _CfprProcessorRuntimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 12),
    _CfprProcessorRuntimeUpdate_Type()
)
cfprProcessorRuntimeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeUpdate.setStatus("current")
_CfprProcessorRuntimeUptime_Type = TimeIntervalSec
_CfprProcessorRuntimeUptime_Object = MibTableColumn
cfprProcessorRuntimeUptime = _CfprProcessorRuntimeUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 6, 1, 13),
    _CfprProcessorRuntimeUptime_Type()
)
cfprProcessorRuntimeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeUptime.setStatus("current")
_CfprProcessorRuntimeHistTable_Object = MibTable
cfprProcessorRuntimeHistTable = _CfprProcessorRuntimeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7)
)
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistTable.setStatus("current")
_CfprProcessorRuntimeHistEntry_Object = MibTableRow
cfprProcessorRuntimeHistEntry = _CfprProcessorRuntimeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1)
)
cfprProcessorRuntimeHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorRuntimeHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistEntry.setStatus("current")
_CfprProcessorRuntimeHistInstanceId_Type = CfprManagedObjectId
_CfprProcessorRuntimeHistInstanceId_Object = MibTableColumn
cfprProcessorRuntimeHistInstanceId = _CfprProcessorRuntimeHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 1),
    _CfprProcessorRuntimeHistInstanceId_Type()
)
cfprProcessorRuntimeHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistInstanceId.setStatus("current")
_CfprProcessorRuntimeHistDn_Type = CfprManagedObjectDn
_CfprProcessorRuntimeHistDn_Object = MibTableColumn
cfprProcessorRuntimeHistDn = _CfprProcessorRuntimeHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 2),
    _CfprProcessorRuntimeHistDn_Type()
)
cfprProcessorRuntimeHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistDn.setStatus("current")
_CfprProcessorRuntimeHistRn_Type = SnmpAdminString
_CfprProcessorRuntimeHistRn_Object = MibTableColumn
cfprProcessorRuntimeHistRn = _CfprProcessorRuntimeHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 3),
    _CfprProcessorRuntimeHistRn_Type()
)
cfprProcessorRuntimeHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistRn.setStatus("current")
_CfprProcessorRuntimeHistId_Type = Unsigned64
_CfprProcessorRuntimeHistId_Object = MibTableColumn
cfprProcessorRuntimeHistId = _CfprProcessorRuntimeHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 4),
    _CfprProcessorRuntimeHistId_Type()
)
cfprProcessorRuntimeHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistId.setStatus("current")
_CfprProcessorRuntimeHistLoad_Type = Integer32
_CfprProcessorRuntimeHistLoad_Object = MibTableColumn
cfprProcessorRuntimeHistLoad = _CfprProcessorRuntimeHistLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 5),
    _CfprProcessorRuntimeHistLoad_Type()
)
cfprProcessorRuntimeHistLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistLoad.setStatus("current")
_CfprProcessorRuntimeHistLoadAvg_Type = Integer32
_CfprProcessorRuntimeHistLoadAvg_Object = MibTableColumn
cfprProcessorRuntimeHistLoadAvg = _CfprProcessorRuntimeHistLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 6),
    _CfprProcessorRuntimeHistLoadAvg_Type()
)
cfprProcessorRuntimeHistLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistLoadAvg.setStatus("current")
_CfprProcessorRuntimeHistLoadMax_Type = Integer32
_CfprProcessorRuntimeHistLoadMax_Object = MibTableColumn
cfprProcessorRuntimeHistLoadMax = _CfprProcessorRuntimeHistLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 7),
    _CfprProcessorRuntimeHistLoadMax_Type()
)
cfprProcessorRuntimeHistLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistLoadMax.setStatus("current")
_CfprProcessorRuntimeHistLoadMin_Type = Integer32
_CfprProcessorRuntimeHistLoadMin_Object = MibTableColumn
cfprProcessorRuntimeHistLoadMin = _CfprProcessorRuntimeHistLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 8),
    _CfprProcessorRuntimeHistLoadMin_Type()
)
cfprProcessorRuntimeHistLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistLoadMin.setStatus("current")
_CfprProcessorRuntimeHistMostRecent_Type = TruthValue
_CfprProcessorRuntimeHistMostRecent_Object = MibTableColumn
cfprProcessorRuntimeHistMostRecent = _CfprProcessorRuntimeHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 9),
    _CfprProcessorRuntimeHistMostRecent_Type()
)
cfprProcessorRuntimeHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistMostRecent.setStatus("current")
_CfprProcessorRuntimeHistSuspect_Type = TruthValue
_CfprProcessorRuntimeHistSuspect_Object = MibTableColumn
cfprProcessorRuntimeHistSuspect = _CfprProcessorRuntimeHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 10),
    _CfprProcessorRuntimeHistSuspect_Type()
)
cfprProcessorRuntimeHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistSuspect.setStatus("current")
_CfprProcessorRuntimeHistThresholded_Type = CfprProcessorRuntimeHistThresholded
_CfprProcessorRuntimeHistThresholded_Object = MibTableColumn
cfprProcessorRuntimeHistThresholded = _CfprProcessorRuntimeHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 11),
    _CfprProcessorRuntimeHistThresholded_Type()
)
cfprProcessorRuntimeHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistThresholded.setStatus("current")
_CfprProcessorRuntimeHistTimeCollected_Type = DateAndTime
_CfprProcessorRuntimeHistTimeCollected_Object = MibTableColumn
cfprProcessorRuntimeHistTimeCollected = _CfprProcessorRuntimeHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 7, 1, 12),
    _CfprProcessorRuntimeHistTimeCollected_Type()
)
cfprProcessorRuntimeHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorRuntimeHistTimeCollected.setStatus("current")
_CfprProcessorThreadTable_Object = MibTable
cfprProcessorThreadTable = _CfprProcessorThreadTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 8)
)
if mibBuilder.loadTexts:
    cfprProcessorThreadTable.setStatus("current")
_CfprProcessorThreadEntry_Object = MibTableRow
cfprProcessorThreadEntry = _CfprProcessorThreadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 8, 1)
)
cfprProcessorThreadEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorThreadInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorThreadEntry.setStatus("current")
_CfprProcessorThreadInstanceId_Type = CfprManagedObjectId
_CfprProcessorThreadInstanceId_Object = MibTableColumn
cfprProcessorThreadInstanceId = _CfprProcessorThreadInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 8, 1, 1),
    _CfprProcessorThreadInstanceId_Type()
)
cfprProcessorThreadInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorThreadInstanceId.setStatus("current")
_CfprProcessorThreadDn_Type = CfprManagedObjectDn
_CfprProcessorThreadDn_Object = MibTableColumn
cfprProcessorThreadDn = _CfprProcessorThreadDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 8, 1, 2),
    _CfprProcessorThreadDn_Type()
)
cfprProcessorThreadDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorThreadDn.setStatus("current")
_CfprProcessorThreadRn_Type = SnmpAdminString
_CfprProcessorThreadRn_Object = MibTableColumn
cfprProcessorThreadRn = _CfprProcessorThreadRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 8, 1, 3),
    _CfprProcessorThreadRn_Type()
)
cfprProcessorThreadRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorThreadRn.setStatus("current")
_CfprProcessorThreadId_Type = Gauge32
_CfprProcessorThreadId_Object = MibTableColumn
cfprProcessorThreadId = _CfprProcessorThreadId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 8, 1, 4),
    _CfprProcessorThreadId_Type()
)
cfprProcessorThreadId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorThreadId.setStatus("current")
_CfprProcessorUnitTable_Object = MibTable
cfprProcessorUnitTable = _CfprProcessorUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9)
)
if mibBuilder.loadTexts:
    cfprProcessorUnitTable.setStatus("current")
_CfprProcessorUnitEntry_Object = MibTableRow
cfprProcessorUnitEntry = _CfprProcessorUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1)
)
cfprProcessorUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorUnitEntry.setStatus("current")
_CfprProcessorUnitInstanceId_Type = CfprManagedObjectId
_CfprProcessorUnitInstanceId_Object = MibTableColumn
cfprProcessorUnitInstanceId = _CfprProcessorUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 1),
    _CfprProcessorUnitInstanceId_Type()
)
cfprProcessorUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorUnitInstanceId.setStatus("current")
_CfprProcessorUnitDn_Type = CfprManagedObjectDn
_CfprProcessorUnitDn_Object = MibTableColumn
cfprProcessorUnitDn = _CfprProcessorUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 2),
    _CfprProcessorUnitDn_Type()
)
cfprProcessorUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitDn.setStatus("current")
_CfprProcessorUnitRn_Type = SnmpAdminString
_CfprProcessorUnitRn_Object = MibTableColumn
cfprProcessorUnitRn = _CfprProcessorUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 3),
    _CfprProcessorUnitRn_Type()
)
cfprProcessorUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitRn.setStatus("current")
_CfprProcessorUnitArch_Type = CfprProcessorUnitArch
_CfprProcessorUnitArch_Object = MibTableColumn
cfprProcessorUnitArch = _CfprProcessorUnitArch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 4),
    _CfprProcessorUnitArch_Type()
)
cfprProcessorUnitArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitArch.setStatus("current")
_CfprProcessorUnitCores_Type = Gauge32
_CfprProcessorUnitCores_Object = MibTableColumn
cfprProcessorUnitCores = _CfprProcessorUnitCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 5),
    _CfprProcessorUnitCores_Type()
)
cfprProcessorUnitCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitCores.setStatus("current")
_CfprProcessorUnitCoresEnabled_Type = Gauge32
_CfprProcessorUnitCoresEnabled_Object = MibTableColumn
cfprProcessorUnitCoresEnabled = _CfprProcessorUnitCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 6),
    _CfprProcessorUnitCoresEnabled_Type()
)
cfprProcessorUnitCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitCoresEnabled.setStatus("current")
_CfprProcessorUnitId_Type = Gauge32
_CfprProcessorUnitId_Object = MibTableColumn
cfprProcessorUnitId = _CfprProcessorUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 7),
    _CfprProcessorUnitId_Type()
)
cfprProcessorUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitId.setStatus("current")
_CfprProcessorUnitLocationDn_Type = SnmpAdminString
_CfprProcessorUnitLocationDn_Object = MibTableColumn
cfprProcessorUnitLocationDn = _CfprProcessorUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 8),
    _CfprProcessorUnitLocationDn_Type()
)
cfprProcessorUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitLocationDn.setStatus("current")
_CfprProcessorUnitModel_Type = SnmpAdminString
_CfprProcessorUnitModel_Object = MibTableColumn
cfprProcessorUnitModel = _CfprProcessorUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 9),
    _CfprProcessorUnitModel_Type()
)
cfprProcessorUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitModel.setStatus("current")
_CfprProcessorUnitOperQualifierReason_Type = SnmpAdminString
_CfprProcessorUnitOperQualifierReason_Object = MibTableColumn
cfprProcessorUnitOperQualifierReason = _CfprProcessorUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 10),
    _CfprProcessorUnitOperQualifierReason_Type()
)
cfprProcessorUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitOperQualifierReason.setStatus("current")
_CfprProcessorUnitOperState_Type = CfprEquipmentOperability
_CfprProcessorUnitOperState_Object = MibTableColumn
cfprProcessorUnitOperState = _CfprProcessorUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 11),
    _CfprProcessorUnitOperState_Type()
)
cfprProcessorUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitOperState.setStatus("current")
_CfprProcessorUnitOperability_Type = CfprEquipmentOperability
_CfprProcessorUnitOperability_Object = MibTableColumn
cfprProcessorUnitOperability = _CfprProcessorUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 12),
    _CfprProcessorUnitOperability_Type()
)
cfprProcessorUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitOperability.setStatus("current")
_CfprProcessorUnitPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprProcessorUnitPerf_Object = MibTableColumn
cfprProcessorUnitPerf = _CfprProcessorUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 13),
    _CfprProcessorUnitPerf_Type()
)
cfprProcessorUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitPerf.setStatus("current")
_CfprProcessorUnitPower_Type = CfprEquipmentPowerState
_CfprProcessorUnitPower_Object = MibTableColumn
cfprProcessorUnitPower = _CfprProcessorUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 14),
    _CfprProcessorUnitPower_Type()
)
cfprProcessorUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitPower.setStatus("current")
_CfprProcessorUnitPresence_Type = CfprEquipmentPresence
_CfprProcessorUnitPresence_Object = MibTableColumn
cfprProcessorUnitPresence = _CfprProcessorUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 15),
    _CfprProcessorUnitPresence_Type()
)
cfprProcessorUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitPresence.setStatus("current")
_CfprProcessorUnitRevision_Type = SnmpAdminString
_CfprProcessorUnitRevision_Object = MibTableColumn
cfprProcessorUnitRevision = _CfprProcessorUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 16),
    _CfprProcessorUnitRevision_Type()
)
cfprProcessorUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitRevision.setStatus("current")
_CfprProcessorUnitSerial_Type = SnmpAdminString
_CfprProcessorUnitSerial_Object = MibTableColumn
cfprProcessorUnitSerial = _CfprProcessorUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 17),
    _CfprProcessorUnitSerial_Type()
)
cfprProcessorUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitSerial.setStatus("current")
_CfprProcessorUnitSocketDesignation_Type = SnmpAdminString
_CfprProcessorUnitSocketDesignation_Object = MibTableColumn
cfprProcessorUnitSocketDesignation = _CfprProcessorUnitSocketDesignation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 18),
    _CfprProcessorUnitSocketDesignation_Type()
)
cfprProcessorUnitSocketDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitSocketDesignation.setStatus("current")
_CfprProcessorUnitSpeed_Type = Integer32
_CfprProcessorUnitSpeed_Object = MibTableColumn
cfprProcessorUnitSpeed = _CfprProcessorUnitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 19),
    _CfprProcessorUnitSpeed_Type()
)
cfprProcessorUnitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitSpeed.setStatus("current")
_CfprProcessorUnitStepping_Type = Gauge32
_CfprProcessorUnitStepping_Object = MibTableColumn
cfprProcessorUnitStepping = _CfprProcessorUnitStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 20),
    _CfprProcessorUnitStepping_Type()
)
cfprProcessorUnitStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitStepping.setStatus("current")
_CfprProcessorUnitThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprProcessorUnitThermal_Object = MibTableColumn
cfprProcessorUnitThermal = _CfprProcessorUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 21),
    _CfprProcessorUnitThermal_Type()
)
cfprProcessorUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitThermal.setStatus("current")
_CfprProcessorUnitThreads_Type = Gauge32
_CfprProcessorUnitThreads_Object = MibTableColumn
cfprProcessorUnitThreads = _CfprProcessorUnitThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 22),
    _CfprProcessorUnitThreads_Type()
)
cfprProcessorUnitThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitThreads.setStatus("current")
_CfprProcessorUnitVendor_Type = SnmpAdminString
_CfprProcessorUnitVendor_Object = MibTableColumn
cfprProcessorUnitVendor = _CfprProcessorUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 23),
    _CfprProcessorUnitVendor_Type()
)
cfprProcessorUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitVendor.setStatus("current")
_CfprProcessorUnitVisibility_Type = CfprMemoryVisibility
_CfprProcessorUnitVisibility_Object = MibTableColumn
cfprProcessorUnitVisibility = _CfprProcessorUnitVisibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 24),
    _CfprProcessorUnitVisibility_Type()
)
cfprProcessorUnitVisibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitVisibility.setStatus("current")
_CfprProcessorUnitVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprProcessorUnitVoltage_Object = MibTableColumn
cfprProcessorUnitVoltage = _CfprProcessorUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 9, 1, 25),
    _CfprProcessorUnitVoltage_Type()
)
cfprProcessorUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitVoltage.setStatus("current")
_CfprProcessorUnitAssocCtxTable_Object = MibTable
cfprProcessorUnitAssocCtxTable = _CfprProcessorUnitAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 10)
)
if mibBuilder.loadTexts:
    cfprProcessorUnitAssocCtxTable.setStatus("current")
_CfprProcessorUnitAssocCtxEntry_Object = MibTableRow
cfprProcessorUnitAssocCtxEntry = _CfprProcessorUnitAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 10, 1)
)
cfprProcessorUnitAssocCtxEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROCESSOR-MIB", "cfprProcessorUnitAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcessorUnitAssocCtxEntry.setStatus("current")
_CfprProcessorUnitAssocCtxInstanceId_Type = CfprManagedObjectId
_CfprProcessorUnitAssocCtxInstanceId_Object = MibTableColumn
cfprProcessorUnitAssocCtxInstanceId = _CfprProcessorUnitAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 10, 1, 1),
    _CfprProcessorUnitAssocCtxInstanceId_Type()
)
cfprProcessorUnitAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcessorUnitAssocCtxInstanceId.setStatus("current")
_CfprProcessorUnitAssocCtxDn_Type = CfprManagedObjectDn
_CfprProcessorUnitAssocCtxDn_Object = MibTableColumn
cfprProcessorUnitAssocCtxDn = _CfprProcessorUnitAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 10, 1, 2),
    _CfprProcessorUnitAssocCtxDn_Type()
)
cfprProcessorUnitAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitAssocCtxDn.setStatus("current")
_CfprProcessorUnitAssocCtxRn_Type = SnmpAdminString
_CfprProcessorUnitAssocCtxRn_Object = MibTableColumn
cfprProcessorUnitAssocCtxRn = _CfprProcessorUnitAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 10, 1, 3),
    _CfprProcessorUnitAssocCtxRn_Type()
)
cfprProcessorUnitAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitAssocCtxRn.setStatus("current")
_CfprProcessorUnitAssocCtxFruCapDn_Type = SnmpAdminString
_CfprProcessorUnitAssocCtxFruCapDn_Object = MibTableColumn
cfprProcessorUnitAssocCtxFruCapDn = _CfprProcessorUnitAssocCtxFruCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 10, 1, 4),
    _CfprProcessorUnitAssocCtxFruCapDn_Type()
)
cfprProcessorUnitAssocCtxFruCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitAssocCtxFruCapDn.setStatus("current")
_CfprProcessorUnitAssocCtxStepping_Type = Gauge32
_CfprProcessorUnitAssocCtxStepping_Object = MibTableColumn
cfprProcessorUnitAssocCtxStepping = _CfprProcessorUnitAssocCtxStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 66, 10, 1, 5),
    _CfprProcessorUnitAssocCtxStepping_Type()
)
cfprProcessorUnitAssocCtxStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcessorUnitAssocCtxStepping.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-PROCESSOR-MIB",
    **{"cfprProcessorObjects": cfprProcessorObjects,
       "cfprProcessorCoreTable": cfprProcessorCoreTable,
       "cfprProcessorCoreEntry": cfprProcessorCoreEntry,
       "cfprProcessorCoreInstanceId": cfprProcessorCoreInstanceId,
       "cfprProcessorCoreDn": cfprProcessorCoreDn,
       "cfprProcessorCoreRn": cfprProcessorCoreRn,
       "cfprProcessorCoreId": cfprProcessorCoreId,
       "cfprProcessorEnvStatsTable": cfprProcessorEnvStatsTable,
       "cfprProcessorEnvStatsEntry": cfprProcessorEnvStatsEntry,
       "cfprProcessorEnvStatsInstanceId": cfprProcessorEnvStatsInstanceId,
       "cfprProcessorEnvStatsDn": cfprProcessorEnvStatsDn,
       "cfprProcessorEnvStatsRn": cfprProcessorEnvStatsRn,
       "cfprProcessorEnvStatsInputCurrent": cfprProcessorEnvStatsInputCurrent,
       "cfprProcessorEnvStatsInputCurrentAvg": cfprProcessorEnvStatsInputCurrentAvg,
       "cfprProcessorEnvStatsInputCurrentMax": cfprProcessorEnvStatsInputCurrentMax,
       "cfprProcessorEnvStatsInputCurrentMin": cfprProcessorEnvStatsInputCurrentMin,
       "cfprProcessorEnvStatsIntervals": cfprProcessorEnvStatsIntervals,
       "cfprProcessorEnvStatsSuspect": cfprProcessorEnvStatsSuspect,
       "cfprProcessorEnvStatsTemperature": cfprProcessorEnvStatsTemperature,
       "cfprProcessorEnvStatsTemperatureAvg": cfprProcessorEnvStatsTemperatureAvg,
       "cfprProcessorEnvStatsTemperatureMax": cfprProcessorEnvStatsTemperatureMax,
       "cfprProcessorEnvStatsTemperatureMin": cfprProcessorEnvStatsTemperatureMin,
       "cfprProcessorEnvStatsThresholded": cfprProcessorEnvStatsThresholded,
       "cfprProcessorEnvStatsTimeCollected": cfprProcessorEnvStatsTimeCollected,
       "cfprProcessorEnvStatsUpdate": cfprProcessorEnvStatsUpdate,
       "cfprProcessorEnvStatsHistTable": cfprProcessorEnvStatsHistTable,
       "cfprProcessorEnvStatsHistEntry": cfprProcessorEnvStatsHistEntry,
       "cfprProcessorEnvStatsHistInstanceId": cfprProcessorEnvStatsHistInstanceId,
       "cfprProcessorEnvStatsHistDn": cfprProcessorEnvStatsHistDn,
       "cfprProcessorEnvStatsHistRn": cfprProcessorEnvStatsHistRn,
       "cfprProcessorEnvStatsHistId": cfprProcessorEnvStatsHistId,
       "cfprProcessorEnvStatsHistInputCurrent": cfprProcessorEnvStatsHistInputCurrent,
       "cfprProcessorEnvStatsHistInputCurrentAvg": cfprProcessorEnvStatsHistInputCurrentAvg,
       "cfprProcessorEnvStatsHistInputCurrentMax": cfprProcessorEnvStatsHistInputCurrentMax,
       "cfprProcessorEnvStatsHistInputCurrentMin": cfprProcessorEnvStatsHistInputCurrentMin,
       "cfprProcessorEnvStatsHistMostRecent": cfprProcessorEnvStatsHistMostRecent,
       "cfprProcessorEnvStatsHistSuspect": cfprProcessorEnvStatsHistSuspect,
       "cfprProcessorEnvStatsHistTemperature": cfprProcessorEnvStatsHistTemperature,
       "cfprProcessorEnvStatsHistTemperatureAvg": cfprProcessorEnvStatsHistTemperatureAvg,
       "cfprProcessorEnvStatsHistTemperatureMax": cfprProcessorEnvStatsHistTemperatureMax,
       "cfprProcessorEnvStatsHistTemperatureMin": cfprProcessorEnvStatsHistTemperatureMin,
       "cfprProcessorEnvStatsHistThresholded": cfprProcessorEnvStatsHistThresholded,
       "cfprProcessorEnvStatsHistTimeCollected": cfprProcessorEnvStatsHistTimeCollected,
       "cfprProcessorErrorStatsTable": cfprProcessorErrorStatsTable,
       "cfprProcessorErrorStatsEntry": cfprProcessorErrorStatsEntry,
       "cfprProcessorErrorStatsInstanceId": cfprProcessorErrorStatsInstanceId,
       "cfprProcessorErrorStatsDn": cfprProcessorErrorStatsDn,
       "cfprProcessorErrorStatsRn": cfprProcessorErrorStatsRn,
       "cfprProcessorErrorStatsIntervals": cfprProcessorErrorStatsIntervals,
       "cfprProcessorErrorStatsMirroringInterSockErrors": cfprProcessorErrorStatsMirroringInterSockErrors,
       "cfprProcessorErrorStatsMirroringInterSockErrors15Min": cfprProcessorErrorStatsMirroringInterSockErrors15Min,
       "cfprProcessorErrorStatsMirroringInterSockErrors15MinH": cfprProcessorErrorStatsMirroringInterSockErrors15MinH,
       "cfprProcessorErrorStatsMirroringInterSockErrors1Day": cfprProcessorErrorStatsMirroringInterSockErrors1Day,
       "cfprProcessorErrorStatsMirroringInterSockErrors1DayH": cfprProcessorErrorStatsMirroringInterSockErrors1DayH,
       "cfprProcessorErrorStatsMirroringInterSockErrors1Hour": cfprProcessorErrorStatsMirroringInterSockErrors1Hour,
       "cfprProcessorErrorStatsMirroringInterSockErrors1HourH": cfprProcessorErrorStatsMirroringInterSockErrors1HourH,
       "cfprProcessorErrorStatsMirroringInterSockErrors1Week": cfprProcessorErrorStatsMirroringInterSockErrors1Week,
       "cfprProcessorErrorStatsMirroringInterSockErrors1WeekH": cfprProcessorErrorStatsMirroringInterSockErrors1WeekH,
       "cfprProcessorErrorStatsMirroringInterSockErrors2Weeks": cfprProcessorErrorStatsMirroringInterSockErrors2Weeks,
       "cfprProcessorErrorStatsMirroringInterSockErrors2WeeksH": cfprProcessorErrorStatsMirroringInterSockErrors2WeeksH,
       "cfprProcessorErrorStatsMirroringIntraSockErrors": cfprProcessorErrorStatsMirroringIntraSockErrors,
       "cfprProcessorErrorStatsMirroringIntraSockErrors15Min": cfprProcessorErrorStatsMirroringIntraSockErrors15Min,
       "cfprProcessorErrorStatsMirroringIntraSockErrors15MinH": cfprProcessorErrorStatsMirroringIntraSockErrors15MinH,
       "cfprProcessorErrorStatsMirroringIntraSockErrors1Day": cfprProcessorErrorStatsMirroringIntraSockErrors1Day,
       "cfprProcessorErrorStatsMirroringIntraSockErrors1DayH": cfprProcessorErrorStatsMirroringIntraSockErrors1DayH,
       "cfprProcessorErrorStatsMirroringIntraSockErrors1Hour": cfprProcessorErrorStatsMirroringIntraSockErrors1Hour,
       "cfprProcessorErrorStatsMirroringIntraSockErrors1HourH": cfprProcessorErrorStatsMirroringIntraSockErrors1HourH,
       "cfprProcessorErrorStatsMirroringIntraSockErrors1Week": cfprProcessorErrorStatsMirroringIntraSockErrors1Week,
       "cfprProcessorErrorStatsMirroringIntraSockErrors1WeekH": cfprProcessorErrorStatsMirroringIntraSockErrors1WeekH,
       "cfprProcessorErrorStatsMirroringIntraSockErrors2Weeks": cfprProcessorErrorStatsMirroringIntraSockErrors2Weeks,
       "cfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH": cfprProcessorErrorStatsMirroringIntraSockErrors2WeeksH,
       "cfprProcessorErrorStatsSmiLinkCorrErrors": cfprProcessorErrorStatsSmiLinkCorrErrors,
       "cfprProcessorErrorStatsSmiLinkCorrErrors15Min": cfprProcessorErrorStatsSmiLinkCorrErrors15Min,
       "cfprProcessorErrorStatsSmiLinkCorrErrors15MinH": cfprProcessorErrorStatsSmiLinkCorrErrors15MinH,
       "cfprProcessorErrorStatsSmiLinkCorrErrors1Day": cfprProcessorErrorStatsSmiLinkCorrErrors1Day,
       "cfprProcessorErrorStatsSmiLinkCorrErrors1DayH": cfprProcessorErrorStatsSmiLinkCorrErrors1DayH,
       "cfprProcessorErrorStatsSmiLinkCorrErrors1Hour": cfprProcessorErrorStatsSmiLinkCorrErrors1Hour,
       "cfprProcessorErrorStatsSmiLinkCorrErrors1HourH": cfprProcessorErrorStatsSmiLinkCorrErrors1HourH,
       "cfprProcessorErrorStatsSmiLinkCorrErrors1Week": cfprProcessorErrorStatsSmiLinkCorrErrors1Week,
       "cfprProcessorErrorStatsSmiLinkCorrErrors1WeekH": cfprProcessorErrorStatsSmiLinkCorrErrors1WeekH,
       "cfprProcessorErrorStatsSmiLinkCorrErrors2Weeks": cfprProcessorErrorStatsSmiLinkCorrErrors2Weeks,
       "cfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH": cfprProcessorErrorStatsSmiLinkCorrErrors2WeeksH,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors": cfprProcessorErrorStatsSmiLinkUncorrErrors,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors15Min": cfprProcessorErrorStatsSmiLinkUncorrErrors15Min,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors15MinH": cfprProcessorErrorStatsSmiLinkUncorrErrors15MinH,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors1Day": cfprProcessorErrorStatsSmiLinkUncorrErrors1Day,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors1DayH": cfprProcessorErrorStatsSmiLinkUncorrErrors1DayH,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors1Hour": cfprProcessorErrorStatsSmiLinkUncorrErrors1Hour,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors1HourH": cfprProcessorErrorStatsSmiLinkUncorrErrors1HourH,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors1Week": cfprProcessorErrorStatsSmiLinkUncorrErrors1Week,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH": cfprProcessorErrorStatsSmiLinkUncorrErrors1WeekH,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks": cfprProcessorErrorStatsSmiLinkUncorrErrors2Weeks,
       "cfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH": cfprProcessorErrorStatsSmiLinkUncorrErrors2WeeksH,
       "cfprProcessorErrorStatsSparingErrors": cfprProcessorErrorStatsSparingErrors,
       "cfprProcessorErrorStatsSparingErrors15Min": cfprProcessorErrorStatsSparingErrors15Min,
       "cfprProcessorErrorStatsSparingErrors15MinH": cfprProcessorErrorStatsSparingErrors15MinH,
       "cfprProcessorErrorStatsSparingErrors1Day": cfprProcessorErrorStatsSparingErrors1Day,
       "cfprProcessorErrorStatsSparingErrors1DayH": cfprProcessorErrorStatsSparingErrors1DayH,
       "cfprProcessorErrorStatsSparingErrors1Hour": cfprProcessorErrorStatsSparingErrors1Hour,
       "cfprProcessorErrorStatsSparingErrors1HourH": cfprProcessorErrorStatsSparingErrors1HourH,
       "cfprProcessorErrorStatsSparingErrors1Week": cfprProcessorErrorStatsSparingErrors1Week,
       "cfprProcessorErrorStatsSparingErrors1WeekH": cfprProcessorErrorStatsSparingErrors1WeekH,
       "cfprProcessorErrorStatsSparingErrors2Weeks": cfprProcessorErrorStatsSparingErrors2Weeks,
       "cfprProcessorErrorStatsSparingErrors2WeeksH": cfprProcessorErrorStatsSparingErrors2WeeksH,
       "cfprProcessorErrorStatsSuspect": cfprProcessorErrorStatsSuspect,
       "cfprProcessorErrorStatsThresholded": cfprProcessorErrorStatsThresholded,
       "cfprProcessorErrorStatsTimeCollected": cfprProcessorErrorStatsTimeCollected,
       "cfprProcessorErrorStatsUpdate": cfprProcessorErrorStatsUpdate,
       "cfprProcessorQualTable": cfprProcessorQualTable,
       "cfprProcessorQualEntry": cfprProcessorQualEntry,
       "cfprProcessorQualInstanceId": cfprProcessorQualInstanceId,
       "cfprProcessorQualDn": cfprProcessorQualDn,
       "cfprProcessorQualRn": cfprProcessorQualRn,
       "cfprProcessorQualArch": cfprProcessorQualArch,
       "cfprProcessorQualMaxCores": cfprProcessorQualMaxCores,
       "cfprProcessorQualMaxProcs": cfprProcessorQualMaxProcs,
       "cfprProcessorQualMaxThreads": cfprProcessorQualMaxThreads,
       "cfprProcessorQualMinCores": cfprProcessorQualMinCores,
       "cfprProcessorQualMinProcs": cfprProcessorQualMinProcs,
       "cfprProcessorQualMinThreads": cfprProcessorQualMinThreads,
       "cfprProcessorQualModel": cfprProcessorQualModel,
       "cfprProcessorQualSpeed": cfprProcessorQualSpeed,
       "cfprProcessorQualStepping": cfprProcessorQualStepping,
       "cfprProcessorRuntimeTable": cfprProcessorRuntimeTable,
       "cfprProcessorRuntimeEntry": cfprProcessorRuntimeEntry,
       "cfprProcessorRuntimeInstanceId": cfprProcessorRuntimeInstanceId,
       "cfprProcessorRuntimeDn": cfprProcessorRuntimeDn,
       "cfprProcessorRuntimeRn": cfprProcessorRuntimeRn,
       "cfprProcessorRuntimeIntervals": cfprProcessorRuntimeIntervals,
       "cfprProcessorRuntimeLoad": cfprProcessorRuntimeLoad,
       "cfprProcessorRuntimeLoadAvg": cfprProcessorRuntimeLoadAvg,
       "cfprProcessorRuntimeLoadMax": cfprProcessorRuntimeLoadMax,
       "cfprProcessorRuntimeLoadMin": cfprProcessorRuntimeLoadMin,
       "cfprProcessorRuntimeSuspect": cfprProcessorRuntimeSuspect,
       "cfprProcessorRuntimeThresholded": cfprProcessorRuntimeThresholded,
       "cfprProcessorRuntimeTimeCollected": cfprProcessorRuntimeTimeCollected,
       "cfprProcessorRuntimeUpdate": cfprProcessorRuntimeUpdate,
       "cfprProcessorRuntimeUptime": cfprProcessorRuntimeUptime,
       "cfprProcessorRuntimeHistTable": cfprProcessorRuntimeHistTable,
       "cfprProcessorRuntimeHistEntry": cfprProcessorRuntimeHistEntry,
       "cfprProcessorRuntimeHistInstanceId": cfprProcessorRuntimeHistInstanceId,
       "cfprProcessorRuntimeHistDn": cfprProcessorRuntimeHistDn,
       "cfprProcessorRuntimeHistRn": cfprProcessorRuntimeHistRn,
       "cfprProcessorRuntimeHistId": cfprProcessorRuntimeHistId,
       "cfprProcessorRuntimeHistLoad": cfprProcessorRuntimeHistLoad,
       "cfprProcessorRuntimeHistLoadAvg": cfprProcessorRuntimeHistLoadAvg,
       "cfprProcessorRuntimeHistLoadMax": cfprProcessorRuntimeHistLoadMax,
       "cfprProcessorRuntimeHistLoadMin": cfprProcessorRuntimeHistLoadMin,
       "cfprProcessorRuntimeHistMostRecent": cfprProcessorRuntimeHistMostRecent,
       "cfprProcessorRuntimeHistSuspect": cfprProcessorRuntimeHistSuspect,
       "cfprProcessorRuntimeHistThresholded": cfprProcessorRuntimeHistThresholded,
       "cfprProcessorRuntimeHistTimeCollected": cfprProcessorRuntimeHistTimeCollected,
       "cfprProcessorThreadTable": cfprProcessorThreadTable,
       "cfprProcessorThreadEntry": cfprProcessorThreadEntry,
       "cfprProcessorThreadInstanceId": cfprProcessorThreadInstanceId,
       "cfprProcessorThreadDn": cfprProcessorThreadDn,
       "cfprProcessorThreadRn": cfprProcessorThreadRn,
       "cfprProcessorThreadId": cfprProcessorThreadId,
       "cfprProcessorUnitTable": cfprProcessorUnitTable,
       "cfprProcessorUnitEntry": cfprProcessorUnitEntry,
       "cfprProcessorUnitInstanceId": cfprProcessorUnitInstanceId,
       "cfprProcessorUnitDn": cfprProcessorUnitDn,
       "cfprProcessorUnitRn": cfprProcessorUnitRn,
       "cfprProcessorUnitArch": cfprProcessorUnitArch,
       "cfprProcessorUnitCores": cfprProcessorUnitCores,
       "cfprProcessorUnitCoresEnabled": cfprProcessorUnitCoresEnabled,
       "cfprProcessorUnitId": cfprProcessorUnitId,
       "cfprProcessorUnitLocationDn": cfprProcessorUnitLocationDn,
       "cfprProcessorUnitModel": cfprProcessorUnitModel,
       "cfprProcessorUnitOperQualifierReason": cfprProcessorUnitOperQualifierReason,
       "cfprProcessorUnitOperState": cfprProcessorUnitOperState,
       "cfprProcessorUnitOperability": cfprProcessorUnitOperability,
       "cfprProcessorUnitPerf": cfprProcessorUnitPerf,
       "cfprProcessorUnitPower": cfprProcessorUnitPower,
       "cfprProcessorUnitPresence": cfprProcessorUnitPresence,
       "cfprProcessorUnitRevision": cfprProcessorUnitRevision,
       "cfprProcessorUnitSerial": cfprProcessorUnitSerial,
       "cfprProcessorUnitSocketDesignation": cfprProcessorUnitSocketDesignation,
       "cfprProcessorUnitSpeed": cfprProcessorUnitSpeed,
       "cfprProcessorUnitStepping": cfprProcessorUnitStepping,
       "cfprProcessorUnitThermal": cfprProcessorUnitThermal,
       "cfprProcessorUnitThreads": cfprProcessorUnitThreads,
       "cfprProcessorUnitVendor": cfprProcessorUnitVendor,
       "cfprProcessorUnitVisibility": cfprProcessorUnitVisibility,
       "cfprProcessorUnitVoltage": cfprProcessorUnitVoltage,
       "cfprProcessorUnitAssocCtxTable": cfprProcessorUnitAssocCtxTable,
       "cfprProcessorUnitAssocCtxEntry": cfprProcessorUnitAssocCtxEntry,
       "cfprProcessorUnitAssocCtxInstanceId": cfprProcessorUnitAssocCtxInstanceId,
       "cfprProcessorUnitAssocCtxDn": cfprProcessorUnitAssocCtxDn,
       "cfprProcessorUnitAssocCtxRn": cfprProcessorUnitAssocCtxRn,
       "cfprProcessorUnitAssocCtxFruCapDn": cfprProcessorUnitAssocCtxFruCapDn,
       "cfprProcessorUnitAssocCtxStepping": cfprProcessorUnitAssocCtxStepping}
)
