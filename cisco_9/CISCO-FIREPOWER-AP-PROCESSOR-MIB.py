# SNMP MIB module (CISCO-FIREPOWER-AP-PROCESSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-PROCESSOR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:27 2025
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
 CfprApMemoryVisibility,
 CfprApProcessorEnvStatsHistThresholded,
 CfprApProcessorEnvStatsThresholded,
 CfprApProcessorErrorStatsThresholded,
 CfprApProcessorQualArch,
 CfprApProcessorRuntimeHistThresholded,
 CfprApProcessorRuntimeThresholded,
 CfprApProcessorUnitArch) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApEquipmentOperability",
    "CfprApEquipmentPowerState",
    "CfprApEquipmentPresence",
    "CfprApEquipmentSensorThresholdStatus",
    "CfprApMemoryVisibility",
    "CfprApProcessorEnvStatsHistThresholded",
    "CfprApProcessorEnvStatsThresholded",
    "CfprApProcessorErrorStatsThresholded",
    "CfprApProcessorQualArch",
    "CfprApProcessorRuntimeHistThresholded",
    "CfprApProcessorRuntimeThresholded",
    "CfprApProcessorUnitArch")

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

cfprApProcessorObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApProcessorCoreTable_Object = MibTable
cfprApProcessorCoreTable = _CfprApProcessorCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 1)
)
if mibBuilder.loadTexts:
    cfprApProcessorCoreTable.setStatus("current")
_CfprApProcessorCoreEntry_Object = MibTableRow
cfprApProcessorCoreEntry = _CfprApProcessorCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 1, 1)
)
cfprApProcessorCoreEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorCoreInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorCoreEntry.setStatus("current")
_CfprApProcessorCoreInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorCoreInstanceId_Object = MibTableColumn
cfprApProcessorCoreInstanceId = _CfprApProcessorCoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 1, 1, 1),
    _CfprApProcessorCoreInstanceId_Type()
)
cfprApProcessorCoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorCoreInstanceId.setStatus("current")
_CfprApProcessorCoreDn_Type = CfprApManagedObjectDn
_CfprApProcessorCoreDn_Object = MibTableColumn
cfprApProcessorCoreDn = _CfprApProcessorCoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 1, 1, 2),
    _CfprApProcessorCoreDn_Type()
)
cfprApProcessorCoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorCoreDn.setStatus("current")
_CfprApProcessorCoreRn_Type = SnmpAdminString
_CfprApProcessorCoreRn_Object = MibTableColumn
cfprApProcessorCoreRn = _CfprApProcessorCoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 1, 1, 3),
    _CfprApProcessorCoreRn_Type()
)
cfprApProcessorCoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorCoreRn.setStatus("current")
_CfprApProcessorCoreId_Type = Gauge32
_CfprApProcessorCoreId_Object = MibTableColumn
cfprApProcessorCoreId = _CfprApProcessorCoreId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 1, 1, 4),
    _CfprApProcessorCoreId_Type()
)
cfprApProcessorCoreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorCoreId.setStatus("current")
_CfprApProcessorEnvStatsTable_Object = MibTable
cfprApProcessorEnvStatsTable = _CfprApProcessorEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2)
)
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsTable.setStatus("current")
_CfprApProcessorEnvStatsEntry_Object = MibTableRow
cfprApProcessorEnvStatsEntry = _CfprApProcessorEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1)
)
cfprApProcessorEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsEntry.setStatus("current")
_CfprApProcessorEnvStatsInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorEnvStatsInstanceId_Object = MibTableColumn
cfprApProcessorEnvStatsInstanceId = _CfprApProcessorEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 1),
    _CfprApProcessorEnvStatsInstanceId_Type()
)
cfprApProcessorEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsInstanceId.setStatus("current")
_CfprApProcessorEnvStatsDn_Type = CfprApManagedObjectDn
_CfprApProcessorEnvStatsDn_Object = MibTableColumn
cfprApProcessorEnvStatsDn = _CfprApProcessorEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 2),
    _CfprApProcessorEnvStatsDn_Type()
)
cfprApProcessorEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsDn.setStatus("current")
_CfprApProcessorEnvStatsRn_Type = SnmpAdminString
_CfprApProcessorEnvStatsRn_Object = MibTableColumn
cfprApProcessorEnvStatsRn = _CfprApProcessorEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 3),
    _CfprApProcessorEnvStatsRn_Type()
)
cfprApProcessorEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsRn.setStatus("current")
_CfprApProcessorEnvStatsIntervals_Type = Gauge32
_CfprApProcessorEnvStatsIntervals_Object = MibTableColumn
cfprApProcessorEnvStatsIntervals = _CfprApProcessorEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 8),
    _CfprApProcessorEnvStatsIntervals_Type()
)
cfprApProcessorEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsIntervals.setStatus("current")
_CfprApProcessorEnvStatsSuspect_Type = TruthValue
_CfprApProcessorEnvStatsSuspect_Object = MibTableColumn
cfprApProcessorEnvStatsSuspect = _CfprApProcessorEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 9),
    _CfprApProcessorEnvStatsSuspect_Type()
)
cfprApProcessorEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsSuspect.setStatus("current")
_CfprApProcessorEnvStatsTemperature_Type = Integer32
_CfprApProcessorEnvStatsTemperature_Object = MibTableColumn
cfprApProcessorEnvStatsTemperature = _CfprApProcessorEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 10),
    _CfprApProcessorEnvStatsTemperature_Type()
)
cfprApProcessorEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsTemperature.setStatus("current")
_CfprApProcessorEnvStatsTemperatureAvg_Type = Integer32
_CfprApProcessorEnvStatsTemperatureAvg_Object = MibTableColumn
cfprApProcessorEnvStatsTemperatureAvg = _CfprApProcessorEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 11),
    _CfprApProcessorEnvStatsTemperatureAvg_Type()
)
cfprApProcessorEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsTemperatureAvg.setStatus("current")
_CfprApProcessorEnvStatsTemperatureMax_Type = Integer32
_CfprApProcessorEnvStatsTemperatureMax_Object = MibTableColumn
cfprApProcessorEnvStatsTemperatureMax = _CfprApProcessorEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 12),
    _CfprApProcessorEnvStatsTemperatureMax_Type()
)
cfprApProcessorEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsTemperatureMax.setStatus("current")
_CfprApProcessorEnvStatsTemperatureMin_Type = Integer32
_CfprApProcessorEnvStatsTemperatureMin_Object = MibTableColumn
cfprApProcessorEnvStatsTemperatureMin = _CfprApProcessorEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 13),
    _CfprApProcessorEnvStatsTemperatureMin_Type()
)
cfprApProcessorEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsTemperatureMin.setStatus("current")
_CfprApProcessorEnvStatsThresholded_Type = CfprApProcessorEnvStatsThresholded
_CfprApProcessorEnvStatsThresholded_Object = MibTableColumn
cfprApProcessorEnvStatsThresholded = _CfprApProcessorEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 14),
    _CfprApProcessorEnvStatsThresholded_Type()
)
cfprApProcessorEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsThresholded.setStatus("current")
_CfprApProcessorEnvStatsTimeCollected_Type = DateAndTime
_CfprApProcessorEnvStatsTimeCollected_Object = MibTableColumn
cfprApProcessorEnvStatsTimeCollected = _CfprApProcessorEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 15),
    _CfprApProcessorEnvStatsTimeCollected_Type()
)
cfprApProcessorEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsTimeCollected.setStatus("current")
_CfprApProcessorEnvStatsUpdate_Type = Gauge32
_CfprApProcessorEnvStatsUpdate_Object = MibTableColumn
cfprApProcessorEnvStatsUpdate = _CfprApProcessorEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 2, 1, 16),
    _CfprApProcessorEnvStatsUpdate_Type()
)
cfprApProcessorEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsUpdate.setStatus("current")
_CfprApProcessorEnvStatsHistTable_Object = MibTable
cfprApProcessorEnvStatsHistTable = _CfprApProcessorEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3)
)
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistTable.setStatus("current")
_CfprApProcessorEnvStatsHistEntry_Object = MibTableRow
cfprApProcessorEnvStatsHistEntry = _CfprApProcessorEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1)
)
cfprApProcessorEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistEntry.setStatus("current")
_CfprApProcessorEnvStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorEnvStatsHistInstanceId_Object = MibTableColumn
cfprApProcessorEnvStatsHistInstanceId = _CfprApProcessorEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 1),
    _CfprApProcessorEnvStatsHistInstanceId_Type()
)
cfprApProcessorEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistInstanceId.setStatus("current")
_CfprApProcessorEnvStatsHistDn_Type = CfprApManagedObjectDn
_CfprApProcessorEnvStatsHistDn_Object = MibTableColumn
cfprApProcessorEnvStatsHistDn = _CfprApProcessorEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 2),
    _CfprApProcessorEnvStatsHistDn_Type()
)
cfprApProcessorEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistDn.setStatus("current")
_CfprApProcessorEnvStatsHistRn_Type = SnmpAdminString
_CfprApProcessorEnvStatsHistRn_Object = MibTableColumn
cfprApProcessorEnvStatsHistRn = _CfprApProcessorEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 3),
    _CfprApProcessorEnvStatsHistRn_Type()
)
cfprApProcessorEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistRn.setStatus("current")
_CfprApProcessorEnvStatsHistId_Type = Unsigned64
_CfprApProcessorEnvStatsHistId_Object = MibTableColumn
cfprApProcessorEnvStatsHistId = _CfprApProcessorEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 4),
    _CfprApProcessorEnvStatsHistId_Type()
)
cfprApProcessorEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistId.setStatus("current")
_CfprApProcessorEnvStatsHistMostRecent_Type = TruthValue
_CfprApProcessorEnvStatsHistMostRecent_Object = MibTableColumn
cfprApProcessorEnvStatsHistMostRecent = _CfprApProcessorEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 9),
    _CfprApProcessorEnvStatsHistMostRecent_Type()
)
cfprApProcessorEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistMostRecent.setStatus("current")
_CfprApProcessorEnvStatsHistSuspect_Type = TruthValue
_CfprApProcessorEnvStatsHistSuspect_Object = MibTableColumn
cfprApProcessorEnvStatsHistSuspect = _CfprApProcessorEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 10),
    _CfprApProcessorEnvStatsHistSuspect_Type()
)
cfprApProcessorEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistSuspect.setStatus("current")
_CfprApProcessorEnvStatsHistTemperature_Type = Integer32
_CfprApProcessorEnvStatsHistTemperature_Object = MibTableColumn
cfprApProcessorEnvStatsHistTemperature = _CfprApProcessorEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 11),
    _CfprApProcessorEnvStatsHistTemperature_Type()
)
cfprApProcessorEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistTemperature.setStatus("current")
_CfprApProcessorEnvStatsHistTemperatureAvg_Type = Integer32
_CfprApProcessorEnvStatsHistTemperatureAvg_Object = MibTableColumn
cfprApProcessorEnvStatsHistTemperatureAvg = _CfprApProcessorEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 12),
    _CfprApProcessorEnvStatsHistTemperatureAvg_Type()
)
cfprApProcessorEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistTemperatureAvg.setStatus("current")
_CfprApProcessorEnvStatsHistTemperatureMax_Type = Integer32
_CfprApProcessorEnvStatsHistTemperatureMax_Object = MibTableColumn
cfprApProcessorEnvStatsHistTemperatureMax = _CfprApProcessorEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 13),
    _CfprApProcessorEnvStatsHistTemperatureMax_Type()
)
cfprApProcessorEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistTemperatureMax.setStatus("current")
_CfprApProcessorEnvStatsHistTemperatureMin_Type = Integer32
_CfprApProcessorEnvStatsHistTemperatureMin_Object = MibTableColumn
cfprApProcessorEnvStatsHistTemperatureMin = _CfprApProcessorEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 14),
    _CfprApProcessorEnvStatsHistTemperatureMin_Type()
)
cfprApProcessorEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistTemperatureMin.setStatus("current")
_CfprApProcessorEnvStatsHistThresholded_Type = CfprApProcessorEnvStatsHistThresholded
_CfprApProcessorEnvStatsHistThresholded_Object = MibTableColumn
cfprApProcessorEnvStatsHistThresholded = _CfprApProcessorEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 15),
    _CfprApProcessorEnvStatsHistThresholded_Type()
)
cfprApProcessorEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistThresholded.setStatus("current")
_CfprApProcessorEnvStatsHistTimeCollected_Type = DateAndTime
_CfprApProcessorEnvStatsHistTimeCollected_Object = MibTableColumn
cfprApProcessorEnvStatsHistTimeCollected = _CfprApProcessorEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 3, 1, 16),
    _CfprApProcessorEnvStatsHistTimeCollected_Type()
)
cfprApProcessorEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorEnvStatsHistTimeCollected.setStatus("current")
_CfprApProcessorErrorStatsTable_Object = MibTable
cfprApProcessorErrorStatsTable = _CfprApProcessorErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4)
)
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsTable.setStatus("current")
_CfprApProcessorErrorStatsEntry_Object = MibTableRow
cfprApProcessorErrorStatsEntry = _CfprApProcessorErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1)
)
cfprApProcessorErrorStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorErrorStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsEntry.setStatus("current")
_CfprApProcessorErrorStatsInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorErrorStatsInstanceId_Object = MibTableColumn
cfprApProcessorErrorStatsInstanceId = _CfprApProcessorErrorStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 1),
    _CfprApProcessorErrorStatsInstanceId_Type()
)
cfprApProcessorErrorStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsInstanceId.setStatus("current")
_CfprApProcessorErrorStatsDn_Type = CfprApManagedObjectDn
_CfprApProcessorErrorStatsDn_Object = MibTableColumn
cfprApProcessorErrorStatsDn = _CfprApProcessorErrorStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 2),
    _CfprApProcessorErrorStatsDn_Type()
)
cfprApProcessorErrorStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsDn.setStatus("current")
_CfprApProcessorErrorStatsRn_Type = SnmpAdminString
_CfprApProcessorErrorStatsRn_Object = MibTableColumn
cfprApProcessorErrorStatsRn = _CfprApProcessorErrorStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 3),
    _CfprApProcessorErrorStatsRn_Type()
)
cfprApProcessorErrorStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsRn.setStatus("current")
_CfprApProcessorErrorStatsIntervals_Type = Gauge32
_CfprApProcessorErrorStatsIntervals_Object = MibTableColumn
cfprApProcessorErrorStatsIntervals = _CfprApProcessorErrorStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 4),
    _CfprApProcessorErrorStatsIntervals_Type()
)
cfprApProcessorErrorStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsIntervals.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors_Type = Counter32
_CfprApProcessorErrorStatsMirroringInterSockErrors_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors = _CfprApProcessorErrorStatsMirroringInterSockErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 5),
    _CfprApProcessorErrorStatsMirroringInterSockErrors_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors15Min_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors15Min_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors15Min = _CfprApProcessorErrorStatsMirroringInterSockErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 6),
    _CfprApProcessorErrorStatsMirroringInterSockErrors15Min_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors15Min.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors15MinH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors15MinH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors15MinH = _CfprApProcessorErrorStatsMirroringInterSockErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 7),
    _CfprApProcessorErrorStatsMirroringInterSockErrors15MinH_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors15MinH.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors1Day_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors1Day_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors1Day = _CfprApProcessorErrorStatsMirroringInterSockErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 8),
    _CfprApProcessorErrorStatsMirroringInterSockErrors1Day_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors1Day.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors1DayH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors1DayH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors1DayH = _CfprApProcessorErrorStatsMirroringInterSockErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 9),
    _CfprApProcessorErrorStatsMirroringInterSockErrors1DayH_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors1DayH.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors1Hour_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors1Hour_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors1Hour = _CfprApProcessorErrorStatsMirroringInterSockErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 10),
    _CfprApProcessorErrorStatsMirroringInterSockErrors1Hour_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors1Hour.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors1HourH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors1HourH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors1HourH = _CfprApProcessorErrorStatsMirroringInterSockErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 11),
    _CfprApProcessorErrorStatsMirroringInterSockErrors1HourH_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors1HourH.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors1Week_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors1Week_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors1Week = _CfprApProcessorErrorStatsMirroringInterSockErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 12),
    _CfprApProcessorErrorStatsMirroringInterSockErrors1Week_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors1Week.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors1WeekH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors1WeekH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors1WeekH = _CfprApProcessorErrorStatsMirroringInterSockErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 13),
    _CfprApProcessorErrorStatsMirroringInterSockErrors1WeekH_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors1WeekH.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors2Weeks_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors2Weeks_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors2Weeks = _CfprApProcessorErrorStatsMirroringInterSockErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 14),
    _CfprApProcessorErrorStatsMirroringInterSockErrors2Weeks_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors2Weeks.setStatus("current")
_CfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH = _CfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 15),
    _CfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH_Type()
)
cfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors_Type = Counter32
_CfprApProcessorErrorStatsMirroringIntraSockErrors_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors = _CfprApProcessorErrorStatsMirroringIntraSockErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 16),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors15Min_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors15Min_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors15Min = _CfprApProcessorErrorStatsMirroringIntraSockErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 17),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors15Min_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors15Min.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors15MinH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors15MinH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors15MinH = _CfprApProcessorErrorStatsMirroringIntraSockErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 18),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors15MinH_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors15MinH.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors1Day_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors1Day_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors1Day = _CfprApProcessorErrorStatsMirroringIntraSockErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 19),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors1Day_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors1Day.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors1DayH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors1DayH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors1DayH = _CfprApProcessorErrorStatsMirroringIntraSockErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 20),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors1DayH_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors1DayH.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors1Hour_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors1Hour_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors1Hour = _CfprApProcessorErrorStatsMirroringIntraSockErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 21),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors1Hour_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors1Hour.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors1HourH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors1HourH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors1HourH = _CfprApProcessorErrorStatsMirroringIntraSockErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 22),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors1HourH_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors1HourH.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors1Week_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors1Week_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors1Week = _CfprApProcessorErrorStatsMirroringIntraSockErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 23),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors1Week_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors1Week.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH = _CfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 24),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks = _CfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 25),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks.setStatus("current")
_CfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Type = Gauge32
_CfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Object = MibTableColumn
cfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH = _CfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 26),
    _CfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Type()
)
cfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors_Type = Counter32
_CfprApProcessorErrorStatsSmiLinkCorrErrors_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors = _CfprApProcessorErrorStatsSmiLinkCorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 27),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors15Min_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors15Min_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors15Min = _CfprApProcessorErrorStatsSmiLinkCorrErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 28),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors15Min_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors15Min.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors15MinH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors15MinH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors15MinH = _CfprApProcessorErrorStatsSmiLinkCorrErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 29),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors15MinH_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors15MinH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors1Day_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors1Day_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors1Day = _CfprApProcessorErrorStatsSmiLinkCorrErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 30),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors1Day_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors1Day.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors1DayH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors1DayH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors1DayH = _CfprApProcessorErrorStatsSmiLinkCorrErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 31),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors1DayH_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors1DayH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors1Hour_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors1Hour_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors1Hour = _CfprApProcessorErrorStatsSmiLinkCorrErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 32),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors1Hour_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors1Hour.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors1HourH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors1HourH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors1HourH = _CfprApProcessorErrorStatsSmiLinkCorrErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 33),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors1HourH_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors1HourH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors1Week_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors1Week_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors1Week = _CfprApProcessorErrorStatsSmiLinkCorrErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 34),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors1Week_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors1Week.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH = _CfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 35),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks = _CfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 36),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH = _CfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 37),
    _CfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Type()
)
cfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors_Type = Counter32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors = _CfprApProcessorErrorStatsSmiLinkUncorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 38),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors15Min_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors15Min_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors15Min = _CfprApProcessorErrorStatsSmiLinkUncorrErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 39),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors15Min_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors15Min.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH = _CfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 40),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1Day_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1Day_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors1Day = _CfprApProcessorErrorStatsSmiLinkUncorrErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 41),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors1Day_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors1Day.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH = _CfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 42),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour = _CfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 43),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH = _CfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 44),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1Week_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1Week_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors1Week = _CfprApProcessorErrorStatsSmiLinkUncorrErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 45),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors1Week_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors1Week.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH = _CfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 46),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks = _CfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 47),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks.setStatus("current")
_CfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Type = Gauge32
_CfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Object = MibTableColumn
cfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH = _CfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 48),
    _CfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Type()
)
cfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors_Type = Counter32
_CfprApProcessorErrorStatsSparingErrors_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors = _CfprApProcessorErrorStatsSparingErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 49),
    _CfprApProcessorErrorStatsSparingErrors_Type()
)
cfprApProcessorErrorStatsSparingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors15Min_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors15Min_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors15Min = _CfprApProcessorErrorStatsSparingErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 50),
    _CfprApProcessorErrorStatsSparingErrors15Min_Type()
)
cfprApProcessorErrorStatsSparingErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors15Min.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors15MinH_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors15MinH_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors15MinH = _CfprApProcessorErrorStatsSparingErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 51),
    _CfprApProcessorErrorStatsSparingErrors15MinH_Type()
)
cfprApProcessorErrorStatsSparingErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors15MinH.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors1Day_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors1Day_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors1Day = _CfprApProcessorErrorStatsSparingErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 52),
    _CfprApProcessorErrorStatsSparingErrors1Day_Type()
)
cfprApProcessorErrorStatsSparingErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors1Day.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors1DayH_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors1DayH_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors1DayH = _CfprApProcessorErrorStatsSparingErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 53),
    _CfprApProcessorErrorStatsSparingErrors1DayH_Type()
)
cfprApProcessorErrorStatsSparingErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors1DayH.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors1Hour_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors1Hour_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors1Hour = _CfprApProcessorErrorStatsSparingErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 54),
    _CfprApProcessorErrorStatsSparingErrors1Hour_Type()
)
cfprApProcessorErrorStatsSparingErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors1Hour.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors1HourH_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors1HourH_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors1HourH = _CfprApProcessorErrorStatsSparingErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 55),
    _CfprApProcessorErrorStatsSparingErrors1HourH_Type()
)
cfprApProcessorErrorStatsSparingErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors1HourH.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors1Week_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors1Week_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors1Week = _CfprApProcessorErrorStatsSparingErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 56),
    _CfprApProcessorErrorStatsSparingErrors1Week_Type()
)
cfprApProcessorErrorStatsSparingErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors1Week.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors1WeekH_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors1WeekH_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors1WeekH = _CfprApProcessorErrorStatsSparingErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 57),
    _CfprApProcessorErrorStatsSparingErrors1WeekH_Type()
)
cfprApProcessorErrorStatsSparingErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors1WeekH.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors2Weeks_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors2Weeks_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors2Weeks = _CfprApProcessorErrorStatsSparingErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 58),
    _CfprApProcessorErrorStatsSparingErrors2Weeks_Type()
)
cfprApProcessorErrorStatsSparingErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors2Weeks.setStatus("current")
_CfprApProcessorErrorStatsSparingErrors2WeeksH_Type = Gauge32
_CfprApProcessorErrorStatsSparingErrors2WeeksH_Object = MibTableColumn
cfprApProcessorErrorStatsSparingErrors2WeeksH = _CfprApProcessorErrorStatsSparingErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 59),
    _CfprApProcessorErrorStatsSparingErrors2WeeksH_Type()
)
cfprApProcessorErrorStatsSparingErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSparingErrors2WeeksH.setStatus("current")
_CfprApProcessorErrorStatsSuspect_Type = TruthValue
_CfprApProcessorErrorStatsSuspect_Object = MibTableColumn
cfprApProcessorErrorStatsSuspect = _CfprApProcessorErrorStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 60),
    _CfprApProcessorErrorStatsSuspect_Type()
)
cfprApProcessorErrorStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsSuspect.setStatus("current")
_CfprApProcessorErrorStatsThresholded_Type = CfprApProcessorErrorStatsThresholded
_CfprApProcessorErrorStatsThresholded_Object = MibTableColumn
cfprApProcessorErrorStatsThresholded = _CfprApProcessorErrorStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 61),
    _CfprApProcessorErrorStatsThresholded_Type()
)
cfprApProcessorErrorStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsThresholded.setStatus("current")
_CfprApProcessorErrorStatsTimeCollected_Type = DateAndTime
_CfprApProcessorErrorStatsTimeCollected_Object = MibTableColumn
cfprApProcessorErrorStatsTimeCollected = _CfprApProcessorErrorStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 62),
    _CfprApProcessorErrorStatsTimeCollected_Type()
)
cfprApProcessorErrorStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsTimeCollected.setStatus("current")
_CfprApProcessorErrorStatsUpdate_Type = Gauge32
_CfprApProcessorErrorStatsUpdate_Object = MibTableColumn
cfprApProcessorErrorStatsUpdate = _CfprApProcessorErrorStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 4, 1, 63),
    _CfprApProcessorErrorStatsUpdate_Type()
)
cfprApProcessorErrorStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorErrorStatsUpdate.setStatus("current")
_CfprApProcessorQualTable_Object = MibTable
cfprApProcessorQualTable = _CfprApProcessorQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5)
)
if mibBuilder.loadTexts:
    cfprApProcessorQualTable.setStatus("current")
_CfprApProcessorQualEntry_Object = MibTableRow
cfprApProcessorQualEntry = _CfprApProcessorQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1)
)
cfprApProcessorQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorQualEntry.setStatus("current")
_CfprApProcessorQualInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorQualInstanceId_Object = MibTableColumn
cfprApProcessorQualInstanceId = _CfprApProcessorQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 1),
    _CfprApProcessorQualInstanceId_Type()
)
cfprApProcessorQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorQualInstanceId.setStatus("current")
_CfprApProcessorQualDn_Type = CfprApManagedObjectDn
_CfprApProcessorQualDn_Object = MibTableColumn
cfprApProcessorQualDn = _CfprApProcessorQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 2),
    _CfprApProcessorQualDn_Type()
)
cfprApProcessorQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualDn.setStatus("current")
_CfprApProcessorQualRn_Type = SnmpAdminString
_CfprApProcessorQualRn_Object = MibTableColumn
cfprApProcessorQualRn = _CfprApProcessorQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 3),
    _CfprApProcessorQualRn_Type()
)
cfprApProcessorQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualRn.setStatus("current")
_CfprApProcessorQualArch_Type = CfprApProcessorQualArch
_CfprApProcessorQualArch_Object = MibTableColumn
cfprApProcessorQualArch = _CfprApProcessorQualArch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 4),
    _CfprApProcessorQualArch_Type()
)
cfprApProcessorQualArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualArch.setStatus("current")
_CfprApProcessorQualMaxCores_Type = Gauge32
_CfprApProcessorQualMaxCores_Object = MibTableColumn
cfprApProcessorQualMaxCores = _CfprApProcessorQualMaxCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 5),
    _CfprApProcessorQualMaxCores_Type()
)
cfprApProcessorQualMaxCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualMaxCores.setStatus("current")
_CfprApProcessorQualMaxProcs_Type = Gauge32
_CfprApProcessorQualMaxProcs_Object = MibTableColumn
cfprApProcessorQualMaxProcs = _CfprApProcessorQualMaxProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 6),
    _CfprApProcessorQualMaxProcs_Type()
)
cfprApProcessorQualMaxProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualMaxProcs.setStatus("current")
_CfprApProcessorQualMaxThreads_Type = Gauge32
_CfprApProcessorQualMaxThreads_Object = MibTableColumn
cfprApProcessorQualMaxThreads = _CfprApProcessorQualMaxThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 7),
    _CfprApProcessorQualMaxThreads_Type()
)
cfprApProcessorQualMaxThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualMaxThreads.setStatus("current")
_CfprApProcessorQualMinCores_Type = Gauge32
_CfprApProcessorQualMinCores_Object = MibTableColumn
cfprApProcessorQualMinCores = _CfprApProcessorQualMinCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 8),
    _CfprApProcessorQualMinCores_Type()
)
cfprApProcessorQualMinCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualMinCores.setStatus("current")
_CfprApProcessorQualMinProcs_Type = Gauge32
_CfprApProcessorQualMinProcs_Object = MibTableColumn
cfprApProcessorQualMinProcs = _CfprApProcessorQualMinProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 9),
    _CfprApProcessorQualMinProcs_Type()
)
cfprApProcessorQualMinProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualMinProcs.setStatus("current")
_CfprApProcessorQualMinThreads_Type = Gauge32
_CfprApProcessorQualMinThreads_Object = MibTableColumn
cfprApProcessorQualMinThreads = _CfprApProcessorQualMinThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 10),
    _CfprApProcessorQualMinThreads_Type()
)
cfprApProcessorQualMinThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualMinThreads.setStatus("current")
_CfprApProcessorQualModel_Type = SnmpAdminString
_CfprApProcessorQualModel_Object = MibTableColumn
cfprApProcessorQualModel = _CfprApProcessorQualModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 11),
    _CfprApProcessorQualModel_Type()
)
cfprApProcessorQualModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualModel.setStatus("current")
_CfprApProcessorQualSpeed_Type = Integer32
_CfprApProcessorQualSpeed_Object = MibTableColumn
cfprApProcessorQualSpeed = _CfprApProcessorQualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 12),
    _CfprApProcessorQualSpeed_Type()
)
cfprApProcessorQualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualSpeed.setStatus("current")
_CfprApProcessorQualStepping_Type = Gauge32
_CfprApProcessorQualStepping_Object = MibTableColumn
cfprApProcessorQualStepping = _CfprApProcessorQualStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 5, 1, 13),
    _CfprApProcessorQualStepping_Type()
)
cfprApProcessorQualStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorQualStepping.setStatus("current")
_CfprApProcessorRuntimeTable_Object = MibTable
cfprApProcessorRuntimeTable = _CfprApProcessorRuntimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6)
)
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeTable.setStatus("current")
_CfprApProcessorRuntimeEntry_Object = MibTableRow
cfprApProcessorRuntimeEntry = _CfprApProcessorRuntimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1)
)
cfprApProcessorRuntimeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorRuntimeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeEntry.setStatus("current")
_CfprApProcessorRuntimeInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorRuntimeInstanceId_Object = MibTableColumn
cfprApProcessorRuntimeInstanceId = _CfprApProcessorRuntimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 1),
    _CfprApProcessorRuntimeInstanceId_Type()
)
cfprApProcessorRuntimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeInstanceId.setStatus("current")
_CfprApProcessorRuntimeDn_Type = CfprApManagedObjectDn
_CfprApProcessorRuntimeDn_Object = MibTableColumn
cfprApProcessorRuntimeDn = _CfprApProcessorRuntimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 2),
    _CfprApProcessorRuntimeDn_Type()
)
cfprApProcessorRuntimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeDn.setStatus("current")
_CfprApProcessorRuntimeRn_Type = SnmpAdminString
_CfprApProcessorRuntimeRn_Object = MibTableColumn
cfprApProcessorRuntimeRn = _CfprApProcessorRuntimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 3),
    _CfprApProcessorRuntimeRn_Type()
)
cfprApProcessorRuntimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeRn.setStatus("current")
_CfprApProcessorRuntimeIntervals_Type = Gauge32
_CfprApProcessorRuntimeIntervals_Object = MibTableColumn
cfprApProcessorRuntimeIntervals = _CfprApProcessorRuntimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 4),
    _CfprApProcessorRuntimeIntervals_Type()
)
cfprApProcessorRuntimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeIntervals.setStatus("current")
_CfprApProcessorRuntimeLoad_Type = Integer32
_CfprApProcessorRuntimeLoad_Object = MibTableColumn
cfprApProcessorRuntimeLoad = _CfprApProcessorRuntimeLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 5),
    _CfprApProcessorRuntimeLoad_Type()
)
cfprApProcessorRuntimeLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeLoad.setStatus("current")
_CfprApProcessorRuntimeLoadAvg_Type = Integer32
_CfprApProcessorRuntimeLoadAvg_Object = MibTableColumn
cfprApProcessorRuntimeLoadAvg = _CfprApProcessorRuntimeLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 6),
    _CfprApProcessorRuntimeLoadAvg_Type()
)
cfprApProcessorRuntimeLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeLoadAvg.setStatus("current")
_CfprApProcessorRuntimeLoadMax_Type = Integer32
_CfprApProcessorRuntimeLoadMax_Object = MibTableColumn
cfprApProcessorRuntimeLoadMax = _CfprApProcessorRuntimeLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 7),
    _CfprApProcessorRuntimeLoadMax_Type()
)
cfprApProcessorRuntimeLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeLoadMax.setStatus("current")
_CfprApProcessorRuntimeLoadMin_Type = Integer32
_CfprApProcessorRuntimeLoadMin_Object = MibTableColumn
cfprApProcessorRuntimeLoadMin = _CfprApProcessorRuntimeLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 8),
    _CfprApProcessorRuntimeLoadMin_Type()
)
cfprApProcessorRuntimeLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeLoadMin.setStatus("current")
_CfprApProcessorRuntimeSuspect_Type = TruthValue
_CfprApProcessorRuntimeSuspect_Object = MibTableColumn
cfprApProcessorRuntimeSuspect = _CfprApProcessorRuntimeSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 9),
    _CfprApProcessorRuntimeSuspect_Type()
)
cfprApProcessorRuntimeSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeSuspect.setStatus("current")
_CfprApProcessorRuntimeThresholded_Type = CfprApProcessorRuntimeThresholded
_CfprApProcessorRuntimeThresholded_Object = MibTableColumn
cfprApProcessorRuntimeThresholded = _CfprApProcessorRuntimeThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 10),
    _CfprApProcessorRuntimeThresholded_Type()
)
cfprApProcessorRuntimeThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeThresholded.setStatus("current")
_CfprApProcessorRuntimeTimeCollected_Type = DateAndTime
_CfprApProcessorRuntimeTimeCollected_Object = MibTableColumn
cfprApProcessorRuntimeTimeCollected = _CfprApProcessorRuntimeTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 11),
    _CfprApProcessorRuntimeTimeCollected_Type()
)
cfprApProcessorRuntimeTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeTimeCollected.setStatus("current")
_CfprApProcessorRuntimeUpdate_Type = Gauge32
_CfprApProcessorRuntimeUpdate_Object = MibTableColumn
cfprApProcessorRuntimeUpdate = _CfprApProcessorRuntimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 12),
    _CfprApProcessorRuntimeUpdate_Type()
)
cfprApProcessorRuntimeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeUpdate.setStatus("current")
_CfprApProcessorRuntimeUptime_Type = TimeIntervalSec
_CfprApProcessorRuntimeUptime_Object = MibTableColumn
cfprApProcessorRuntimeUptime = _CfprApProcessorRuntimeUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 6, 1, 13),
    _CfprApProcessorRuntimeUptime_Type()
)
cfprApProcessorRuntimeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeUptime.setStatus("current")
_CfprApProcessorRuntimeHistTable_Object = MibTable
cfprApProcessorRuntimeHistTable = _CfprApProcessorRuntimeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7)
)
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistTable.setStatus("current")
_CfprApProcessorRuntimeHistEntry_Object = MibTableRow
cfprApProcessorRuntimeHistEntry = _CfprApProcessorRuntimeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1)
)
cfprApProcessorRuntimeHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorRuntimeHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistEntry.setStatus("current")
_CfprApProcessorRuntimeHistInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorRuntimeHistInstanceId_Object = MibTableColumn
cfprApProcessorRuntimeHistInstanceId = _CfprApProcessorRuntimeHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 1),
    _CfprApProcessorRuntimeHistInstanceId_Type()
)
cfprApProcessorRuntimeHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistInstanceId.setStatus("current")
_CfprApProcessorRuntimeHistDn_Type = CfprApManagedObjectDn
_CfprApProcessorRuntimeHistDn_Object = MibTableColumn
cfprApProcessorRuntimeHistDn = _CfprApProcessorRuntimeHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 2),
    _CfprApProcessorRuntimeHistDn_Type()
)
cfprApProcessorRuntimeHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistDn.setStatus("current")
_CfprApProcessorRuntimeHistRn_Type = SnmpAdminString
_CfprApProcessorRuntimeHistRn_Object = MibTableColumn
cfprApProcessorRuntimeHistRn = _CfprApProcessorRuntimeHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 3),
    _CfprApProcessorRuntimeHistRn_Type()
)
cfprApProcessorRuntimeHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistRn.setStatus("current")
_CfprApProcessorRuntimeHistId_Type = Unsigned64
_CfprApProcessorRuntimeHistId_Object = MibTableColumn
cfprApProcessorRuntimeHistId = _CfprApProcessorRuntimeHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 4),
    _CfprApProcessorRuntimeHistId_Type()
)
cfprApProcessorRuntimeHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistId.setStatus("current")
_CfprApProcessorRuntimeHistLoad_Type = Integer32
_CfprApProcessorRuntimeHistLoad_Object = MibTableColumn
cfprApProcessorRuntimeHistLoad = _CfprApProcessorRuntimeHistLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 5),
    _CfprApProcessorRuntimeHistLoad_Type()
)
cfprApProcessorRuntimeHistLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistLoad.setStatus("current")
_CfprApProcessorRuntimeHistLoadAvg_Type = Integer32
_CfprApProcessorRuntimeHistLoadAvg_Object = MibTableColumn
cfprApProcessorRuntimeHistLoadAvg = _CfprApProcessorRuntimeHistLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 6),
    _CfprApProcessorRuntimeHistLoadAvg_Type()
)
cfprApProcessorRuntimeHistLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistLoadAvg.setStatus("current")
_CfprApProcessorRuntimeHistLoadMax_Type = Integer32
_CfprApProcessorRuntimeHistLoadMax_Object = MibTableColumn
cfprApProcessorRuntimeHistLoadMax = _CfprApProcessorRuntimeHistLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 7),
    _CfprApProcessorRuntimeHistLoadMax_Type()
)
cfprApProcessorRuntimeHistLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistLoadMax.setStatus("current")
_CfprApProcessorRuntimeHistLoadMin_Type = Integer32
_CfprApProcessorRuntimeHistLoadMin_Object = MibTableColumn
cfprApProcessorRuntimeHistLoadMin = _CfprApProcessorRuntimeHistLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 8),
    _CfprApProcessorRuntimeHistLoadMin_Type()
)
cfprApProcessorRuntimeHistLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistLoadMin.setStatus("current")
_CfprApProcessorRuntimeHistMostRecent_Type = TruthValue
_CfprApProcessorRuntimeHistMostRecent_Object = MibTableColumn
cfprApProcessorRuntimeHistMostRecent = _CfprApProcessorRuntimeHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 9),
    _CfprApProcessorRuntimeHistMostRecent_Type()
)
cfprApProcessorRuntimeHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistMostRecent.setStatus("current")
_CfprApProcessorRuntimeHistSuspect_Type = TruthValue
_CfprApProcessorRuntimeHistSuspect_Object = MibTableColumn
cfprApProcessorRuntimeHistSuspect = _CfprApProcessorRuntimeHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 10),
    _CfprApProcessorRuntimeHistSuspect_Type()
)
cfprApProcessorRuntimeHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistSuspect.setStatus("current")
_CfprApProcessorRuntimeHistThresholded_Type = CfprApProcessorRuntimeHistThresholded
_CfprApProcessorRuntimeHistThresholded_Object = MibTableColumn
cfprApProcessorRuntimeHistThresholded = _CfprApProcessorRuntimeHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 11),
    _CfprApProcessorRuntimeHistThresholded_Type()
)
cfprApProcessorRuntimeHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistThresholded.setStatus("current")
_CfprApProcessorRuntimeHistTimeCollected_Type = DateAndTime
_CfprApProcessorRuntimeHistTimeCollected_Object = MibTableColumn
cfprApProcessorRuntimeHistTimeCollected = _CfprApProcessorRuntimeHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 7, 1, 12),
    _CfprApProcessorRuntimeHistTimeCollected_Type()
)
cfprApProcessorRuntimeHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorRuntimeHistTimeCollected.setStatus("current")
_CfprApProcessorThreadTable_Object = MibTable
cfprApProcessorThreadTable = _CfprApProcessorThreadTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 8)
)
if mibBuilder.loadTexts:
    cfprApProcessorThreadTable.setStatus("current")
_CfprApProcessorThreadEntry_Object = MibTableRow
cfprApProcessorThreadEntry = _CfprApProcessorThreadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 8, 1)
)
cfprApProcessorThreadEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorThreadInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorThreadEntry.setStatus("current")
_CfprApProcessorThreadInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorThreadInstanceId_Object = MibTableColumn
cfprApProcessorThreadInstanceId = _CfprApProcessorThreadInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 8, 1, 1),
    _CfprApProcessorThreadInstanceId_Type()
)
cfprApProcessorThreadInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorThreadInstanceId.setStatus("current")
_CfprApProcessorThreadDn_Type = CfprApManagedObjectDn
_CfprApProcessorThreadDn_Object = MibTableColumn
cfprApProcessorThreadDn = _CfprApProcessorThreadDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 8, 1, 2),
    _CfprApProcessorThreadDn_Type()
)
cfprApProcessorThreadDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorThreadDn.setStatus("current")
_CfprApProcessorThreadRn_Type = SnmpAdminString
_CfprApProcessorThreadRn_Object = MibTableColumn
cfprApProcessorThreadRn = _CfprApProcessorThreadRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 8, 1, 3),
    _CfprApProcessorThreadRn_Type()
)
cfprApProcessorThreadRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorThreadRn.setStatus("current")
_CfprApProcessorThreadId_Type = Gauge32
_CfprApProcessorThreadId_Object = MibTableColumn
cfprApProcessorThreadId = _CfprApProcessorThreadId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 8, 1, 4),
    _CfprApProcessorThreadId_Type()
)
cfprApProcessorThreadId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorThreadId.setStatus("current")
_CfprApProcessorUnitTable_Object = MibTable
cfprApProcessorUnitTable = _CfprApProcessorUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9)
)
if mibBuilder.loadTexts:
    cfprApProcessorUnitTable.setStatus("current")
_CfprApProcessorUnitEntry_Object = MibTableRow
cfprApProcessorUnitEntry = _CfprApProcessorUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1)
)
cfprApProcessorUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorUnitEntry.setStatus("current")
_CfprApProcessorUnitInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorUnitInstanceId_Object = MibTableColumn
cfprApProcessorUnitInstanceId = _CfprApProcessorUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 1),
    _CfprApProcessorUnitInstanceId_Type()
)
cfprApProcessorUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorUnitInstanceId.setStatus("current")
_CfprApProcessorUnitDn_Type = CfprApManagedObjectDn
_CfprApProcessorUnitDn_Object = MibTableColumn
cfprApProcessorUnitDn = _CfprApProcessorUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 2),
    _CfprApProcessorUnitDn_Type()
)
cfprApProcessorUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitDn.setStatus("current")
_CfprApProcessorUnitRn_Type = SnmpAdminString
_CfprApProcessorUnitRn_Object = MibTableColumn
cfprApProcessorUnitRn = _CfprApProcessorUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 3),
    _CfprApProcessorUnitRn_Type()
)
cfprApProcessorUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitRn.setStatus("current")
_CfprApProcessorUnitArch_Type = CfprApProcessorUnitArch
_CfprApProcessorUnitArch_Object = MibTableColumn
cfprApProcessorUnitArch = _CfprApProcessorUnitArch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 4),
    _CfprApProcessorUnitArch_Type()
)
cfprApProcessorUnitArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitArch.setStatus("current")
_CfprApProcessorUnitCores_Type = Gauge32
_CfprApProcessorUnitCores_Object = MibTableColumn
cfprApProcessorUnitCores = _CfprApProcessorUnitCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 5),
    _CfprApProcessorUnitCores_Type()
)
cfprApProcessorUnitCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitCores.setStatus("current")
_CfprApProcessorUnitCoresEnabled_Type = Gauge32
_CfprApProcessorUnitCoresEnabled_Object = MibTableColumn
cfprApProcessorUnitCoresEnabled = _CfprApProcessorUnitCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 6),
    _CfprApProcessorUnitCoresEnabled_Type()
)
cfprApProcessorUnitCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitCoresEnabled.setStatus("current")
_CfprApProcessorUnitId_Type = Gauge32
_CfprApProcessorUnitId_Object = MibTableColumn
cfprApProcessorUnitId = _CfprApProcessorUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 7),
    _CfprApProcessorUnitId_Type()
)
cfprApProcessorUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitId.setStatus("current")
_CfprApProcessorUnitLocationDn_Type = SnmpAdminString
_CfprApProcessorUnitLocationDn_Object = MibTableColumn
cfprApProcessorUnitLocationDn = _CfprApProcessorUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 8),
    _CfprApProcessorUnitLocationDn_Type()
)
cfprApProcessorUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitLocationDn.setStatus("current")
_CfprApProcessorUnitModel_Type = SnmpAdminString
_CfprApProcessorUnitModel_Object = MibTableColumn
cfprApProcessorUnitModel = _CfprApProcessorUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 9),
    _CfprApProcessorUnitModel_Type()
)
cfprApProcessorUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitModel.setStatus("current")
_CfprApProcessorUnitOperQualifierReason_Type = SnmpAdminString
_CfprApProcessorUnitOperQualifierReason_Object = MibTableColumn
cfprApProcessorUnitOperQualifierReason = _CfprApProcessorUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 10),
    _CfprApProcessorUnitOperQualifierReason_Type()
)
cfprApProcessorUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitOperQualifierReason.setStatus("current")
_CfprApProcessorUnitOperState_Type = CfprApEquipmentOperability
_CfprApProcessorUnitOperState_Object = MibTableColumn
cfprApProcessorUnitOperState = _CfprApProcessorUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 11),
    _CfprApProcessorUnitOperState_Type()
)
cfprApProcessorUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitOperState.setStatus("current")
_CfprApProcessorUnitOperability_Type = CfprApEquipmentOperability
_CfprApProcessorUnitOperability_Object = MibTableColumn
cfprApProcessorUnitOperability = _CfprApProcessorUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 12),
    _CfprApProcessorUnitOperability_Type()
)
cfprApProcessorUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitOperability.setStatus("current")
_CfprApProcessorUnitPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApProcessorUnitPerf_Object = MibTableColumn
cfprApProcessorUnitPerf = _CfprApProcessorUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 13),
    _CfprApProcessorUnitPerf_Type()
)
cfprApProcessorUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitPerf.setStatus("current")
_CfprApProcessorUnitPower_Type = CfprApEquipmentPowerState
_CfprApProcessorUnitPower_Object = MibTableColumn
cfprApProcessorUnitPower = _CfprApProcessorUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 14),
    _CfprApProcessorUnitPower_Type()
)
cfprApProcessorUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitPower.setStatus("current")
_CfprApProcessorUnitPresence_Type = CfprApEquipmentPresence
_CfprApProcessorUnitPresence_Object = MibTableColumn
cfprApProcessorUnitPresence = _CfprApProcessorUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 15),
    _CfprApProcessorUnitPresence_Type()
)
cfprApProcessorUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitPresence.setStatus("current")
_CfprApProcessorUnitRevision_Type = SnmpAdminString
_CfprApProcessorUnitRevision_Object = MibTableColumn
cfprApProcessorUnitRevision = _CfprApProcessorUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 16),
    _CfprApProcessorUnitRevision_Type()
)
cfprApProcessorUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitRevision.setStatus("current")
_CfprApProcessorUnitSerial_Type = SnmpAdminString
_CfprApProcessorUnitSerial_Object = MibTableColumn
cfprApProcessorUnitSerial = _CfprApProcessorUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 17),
    _CfprApProcessorUnitSerial_Type()
)
cfprApProcessorUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitSerial.setStatus("current")
_CfprApProcessorUnitSocketDesignation_Type = SnmpAdminString
_CfprApProcessorUnitSocketDesignation_Object = MibTableColumn
cfprApProcessorUnitSocketDesignation = _CfprApProcessorUnitSocketDesignation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 18),
    _CfprApProcessorUnitSocketDesignation_Type()
)
cfprApProcessorUnitSocketDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitSocketDesignation.setStatus("current")
_CfprApProcessorUnitSpeed_Type = Integer32
_CfprApProcessorUnitSpeed_Object = MibTableColumn
cfprApProcessorUnitSpeed = _CfprApProcessorUnitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 19),
    _CfprApProcessorUnitSpeed_Type()
)
cfprApProcessorUnitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitSpeed.setStatus("current")
_CfprApProcessorUnitStepping_Type = Gauge32
_CfprApProcessorUnitStepping_Object = MibTableColumn
cfprApProcessorUnitStepping = _CfprApProcessorUnitStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 20),
    _CfprApProcessorUnitStepping_Type()
)
cfprApProcessorUnitStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitStepping.setStatus("current")
_CfprApProcessorUnitThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApProcessorUnitThermal_Object = MibTableColumn
cfprApProcessorUnitThermal = _CfprApProcessorUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 21),
    _CfprApProcessorUnitThermal_Type()
)
cfprApProcessorUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitThermal.setStatus("current")
_CfprApProcessorUnitThreads_Type = Gauge32
_CfprApProcessorUnitThreads_Object = MibTableColumn
cfprApProcessorUnitThreads = _CfprApProcessorUnitThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 22),
    _CfprApProcessorUnitThreads_Type()
)
cfprApProcessorUnitThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitThreads.setStatus("current")
_CfprApProcessorUnitVendor_Type = SnmpAdminString
_CfprApProcessorUnitVendor_Object = MibTableColumn
cfprApProcessorUnitVendor = _CfprApProcessorUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 23),
    _CfprApProcessorUnitVendor_Type()
)
cfprApProcessorUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitVendor.setStatus("current")
_CfprApProcessorUnitVisibility_Type = CfprApMemoryVisibility
_CfprApProcessorUnitVisibility_Object = MibTableColumn
cfprApProcessorUnitVisibility = _CfprApProcessorUnitVisibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 24),
    _CfprApProcessorUnitVisibility_Type()
)
cfprApProcessorUnitVisibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitVisibility.setStatus("current")
_CfprApProcessorUnitVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApProcessorUnitVoltage_Object = MibTableColumn
cfprApProcessorUnitVoltage = _CfprApProcessorUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 9, 1, 25),
    _CfprApProcessorUnitVoltage_Type()
)
cfprApProcessorUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitVoltage.setStatus("current")
_CfprApProcessorUnitAssocCtxTable_Object = MibTable
cfprApProcessorUnitAssocCtxTable = _CfprApProcessorUnitAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 10)
)
if mibBuilder.loadTexts:
    cfprApProcessorUnitAssocCtxTable.setStatus("current")
_CfprApProcessorUnitAssocCtxEntry_Object = MibTableRow
cfprApProcessorUnitAssocCtxEntry = _CfprApProcessorUnitAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 10, 1)
)
cfprApProcessorUnitAssocCtxEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROCESSOR-MIB", "cfprApProcessorUnitAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcessorUnitAssocCtxEntry.setStatus("current")
_CfprApProcessorUnitAssocCtxInstanceId_Type = CfprApManagedObjectId
_CfprApProcessorUnitAssocCtxInstanceId_Object = MibTableColumn
cfprApProcessorUnitAssocCtxInstanceId = _CfprApProcessorUnitAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 10, 1, 1),
    _CfprApProcessorUnitAssocCtxInstanceId_Type()
)
cfprApProcessorUnitAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcessorUnitAssocCtxInstanceId.setStatus("current")
_CfprApProcessorUnitAssocCtxDn_Type = CfprApManagedObjectDn
_CfprApProcessorUnitAssocCtxDn_Object = MibTableColumn
cfprApProcessorUnitAssocCtxDn = _CfprApProcessorUnitAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 10, 1, 2),
    _CfprApProcessorUnitAssocCtxDn_Type()
)
cfprApProcessorUnitAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitAssocCtxDn.setStatus("current")
_CfprApProcessorUnitAssocCtxRn_Type = SnmpAdminString
_CfprApProcessorUnitAssocCtxRn_Object = MibTableColumn
cfprApProcessorUnitAssocCtxRn = _CfprApProcessorUnitAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 10, 1, 3),
    _CfprApProcessorUnitAssocCtxRn_Type()
)
cfprApProcessorUnitAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitAssocCtxRn.setStatus("current")
_CfprApProcessorUnitAssocCtxFruCapDn_Type = SnmpAdminString
_CfprApProcessorUnitAssocCtxFruCapDn_Object = MibTableColumn
cfprApProcessorUnitAssocCtxFruCapDn = _CfprApProcessorUnitAssocCtxFruCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 10, 1, 4),
    _CfprApProcessorUnitAssocCtxFruCapDn_Type()
)
cfprApProcessorUnitAssocCtxFruCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitAssocCtxFruCapDn.setStatus("current")
_CfprApProcessorUnitAssocCtxStepping_Type = Gauge32
_CfprApProcessorUnitAssocCtxStepping_Object = MibTableColumn
cfprApProcessorUnitAssocCtxStepping = _CfprApProcessorUnitAssocCtxStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 66, 10, 1, 5),
    _CfprApProcessorUnitAssocCtxStepping_Type()
)
cfprApProcessorUnitAssocCtxStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcessorUnitAssocCtxStepping.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-PROCESSOR-MIB",
    **{"cfprApProcessorObjects": cfprApProcessorObjects,
       "cfprApProcessorCoreTable": cfprApProcessorCoreTable,
       "cfprApProcessorCoreEntry": cfprApProcessorCoreEntry,
       "cfprApProcessorCoreInstanceId": cfprApProcessorCoreInstanceId,
       "cfprApProcessorCoreDn": cfprApProcessorCoreDn,
       "cfprApProcessorCoreRn": cfprApProcessorCoreRn,
       "cfprApProcessorCoreId": cfprApProcessorCoreId,
       "cfprApProcessorEnvStatsTable": cfprApProcessorEnvStatsTable,
       "cfprApProcessorEnvStatsEntry": cfprApProcessorEnvStatsEntry,
       "cfprApProcessorEnvStatsInstanceId": cfprApProcessorEnvStatsInstanceId,
       "cfprApProcessorEnvStatsDn": cfprApProcessorEnvStatsDn,
       "cfprApProcessorEnvStatsRn": cfprApProcessorEnvStatsRn,
       "cfprApProcessorEnvStatsIntervals": cfprApProcessorEnvStatsIntervals,
       "cfprApProcessorEnvStatsSuspect": cfprApProcessorEnvStatsSuspect,
       "cfprApProcessorEnvStatsTemperature": cfprApProcessorEnvStatsTemperature,
       "cfprApProcessorEnvStatsTemperatureAvg": cfprApProcessorEnvStatsTemperatureAvg,
       "cfprApProcessorEnvStatsTemperatureMax": cfprApProcessorEnvStatsTemperatureMax,
       "cfprApProcessorEnvStatsTemperatureMin": cfprApProcessorEnvStatsTemperatureMin,
       "cfprApProcessorEnvStatsThresholded": cfprApProcessorEnvStatsThresholded,
       "cfprApProcessorEnvStatsTimeCollected": cfprApProcessorEnvStatsTimeCollected,
       "cfprApProcessorEnvStatsUpdate": cfprApProcessorEnvStatsUpdate,
       "cfprApProcessorEnvStatsHistTable": cfprApProcessorEnvStatsHistTable,
       "cfprApProcessorEnvStatsHistEntry": cfprApProcessorEnvStatsHistEntry,
       "cfprApProcessorEnvStatsHistInstanceId": cfprApProcessorEnvStatsHistInstanceId,
       "cfprApProcessorEnvStatsHistDn": cfprApProcessorEnvStatsHistDn,
       "cfprApProcessorEnvStatsHistRn": cfprApProcessorEnvStatsHistRn,
       "cfprApProcessorEnvStatsHistId": cfprApProcessorEnvStatsHistId,
       "cfprApProcessorEnvStatsHistMostRecent": cfprApProcessorEnvStatsHistMostRecent,
       "cfprApProcessorEnvStatsHistSuspect": cfprApProcessorEnvStatsHistSuspect,
       "cfprApProcessorEnvStatsHistTemperature": cfprApProcessorEnvStatsHistTemperature,
       "cfprApProcessorEnvStatsHistTemperatureAvg": cfprApProcessorEnvStatsHistTemperatureAvg,
       "cfprApProcessorEnvStatsHistTemperatureMax": cfprApProcessorEnvStatsHistTemperatureMax,
       "cfprApProcessorEnvStatsHistTemperatureMin": cfprApProcessorEnvStatsHistTemperatureMin,
       "cfprApProcessorEnvStatsHistThresholded": cfprApProcessorEnvStatsHistThresholded,
       "cfprApProcessorEnvStatsHistTimeCollected": cfprApProcessorEnvStatsHistTimeCollected,
       "cfprApProcessorErrorStatsTable": cfprApProcessorErrorStatsTable,
       "cfprApProcessorErrorStatsEntry": cfprApProcessorErrorStatsEntry,
       "cfprApProcessorErrorStatsInstanceId": cfprApProcessorErrorStatsInstanceId,
       "cfprApProcessorErrorStatsDn": cfprApProcessorErrorStatsDn,
       "cfprApProcessorErrorStatsRn": cfprApProcessorErrorStatsRn,
       "cfprApProcessorErrorStatsIntervals": cfprApProcessorErrorStatsIntervals,
       "cfprApProcessorErrorStatsMirroringInterSockErrors": cfprApProcessorErrorStatsMirroringInterSockErrors,
       "cfprApProcessorErrorStatsMirroringInterSockErrors15Min": cfprApProcessorErrorStatsMirroringInterSockErrors15Min,
       "cfprApProcessorErrorStatsMirroringInterSockErrors15MinH": cfprApProcessorErrorStatsMirroringInterSockErrors15MinH,
       "cfprApProcessorErrorStatsMirroringInterSockErrors1Day": cfprApProcessorErrorStatsMirroringInterSockErrors1Day,
       "cfprApProcessorErrorStatsMirroringInterSockErrors1DayH": cfprApProcessorErrorStatsMirroringInterSockErrors1DayH,
       "cfprApProcessorErrorStatsMirroringInterSockErrors1Hour": cfprApProcessorErrorStatsMirroringInterSockErrors1Hour,
       "cfprApProcessorErrorStatsMirroringInterSockErrors1HourH": cfprApProcessorErrorStatsMirroringInterSockErrors1HourH,
       "cfprApProcessorErrorStatsMirroringInterSockErrors1Week": cfprApProcessorErrorStatsMirroringInterSockErrors1Week,
       "cfprApProcessorErrorStatsMirroringInterSockErrors1WeekH": cfprApProcessorErrorStatsMirroringInterSockErrors1WeekH,
       "cfprApProcessorErrorStatsMirroringInterSockErrors2Weeks": cfprApProcessorErrorStatsMirroringInterSockErrors2Weeks,
       "cfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH": cfprApProcessorErrorStatsMirroringInterSockErrors2WeeksH,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors": cfprApProcessorErrorStatsMirroringIntraSockErrors,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors15Min": cfprApProcessorErrorStatsMirroringIntraSockErrors15Min,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors15MinH": cfprApProcessorErrorStatsMirroringIntraSockErrors15MinH,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors1Day": cfprApProcessorErrorStatsMirroringIntraSockErrors1Day,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors1DayH": cfprApProcessorErrorStatsMirroringIntraSockErrors1DayH,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors1Hour": cfprApProcessorErrorStatsMirroringIntraSockErrors1Hour,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors1HourH": cfprApProcessorErrorStatsMirroringIntraSockErrors1HourH,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors1Week": cfprApProcessorErrorStatsMirroringIntraSockErrors1Week,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH": cfprApProcessorErrorStatsMirroringIntraSockErrors1WeekH,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks": cfprApProcessorErrorStatsMirroringIntraSockErrors2Weeks,
       "cfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH": cfprApProcessorErrorStatsMirroringIntraSockErrors2WeeksH,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors": cfprApProcessorErrorStatsSmiLinkCorrErrors,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors15Min": cfprApProcessorErrorStatsSmiLinkCorrErrors15Min,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors15MinH": cfprApProcessorErrorStatsSmiLinkCorrErrors15MinH,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors1Day": cfprApProcessorErrorStatsSmiLinkCorrErrors1Day,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors1DayH": cfprApProcessorErrorStatsSmiLinkCorrErrors1DayH,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors1Hour": cfprApProcessorErrorStatsSmiLinkCorrErrors1Hour,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors1HourH": cfprApProcessorErrorStatsSmiLinkCorrErrors1HourH,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors1Week": cfprApProcessorErrorStatsSmiLinkCorrErrors1Week,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH": cfprApProcessorErrorStatsSmiLinkCorrErrors1WeekH,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks": cfprApProcessorErrorStatsSmiLinkCorrErrors2Weeks,
       "cfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH": cfprApProcessorErrorStatsSmiLinkCorrErrors2WeeksH,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors": cfprApProcessorErrorStatsSmiLinkUncorrErrors,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors15Min": cfprApProcessorErrorStatsSmiLinkUncorrErrors15Min,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH": cfprApProcessorErrorStatsSmiLinkUncorrErrors15MinH,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors1Day": cfprApProcessorErrorStatsSmiLinkUncorrErrors1Day,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH": cfprApProcessorErrorStatsSmiLinkUncorrErrors1DayH,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour": cfprApProcessorErrorStatsSmiLinkUncorrErrors1Hour,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH": cfprApProcessorErrorStatsSmiLinkUncorrErrors1HourH,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors1Week": cfprApProcessorErrorStatsSmiLinkUncorrErrors1Week,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH": cfprApProcessorErrorStatsSmiLinkUncorrErrors1WeekH,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks": cfprApProcessorErrorStatsSmiLinkUncorrErrors2Weeks,
       "cfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH": cfprApProcessorErrorStatsSmiLinkUncorrErrors2WeeksH,
       "cfprApProcessorErrorStatsSparingErrors": cfprApProcessorErrorStatsSparingErrors,
       "cfprApProcessorErrorStatsSparingErrors15Min": cfprApProcessorErrorStatsSparingErrors15Min,
       "cfprApProcessorErrorStatsSparingErrors15MinH": cfprApProcessorErrorStatsSparingErrors15MinH,
       "cfprApProcessorErrorStatsSparingErrors1Day": cfprApProcessorErrorStatsSparingErrors1Day,
       "cfprApProcessorErrorStatsSparingErrors1DayH": cfprApProcessorErrorStatsSparingErrors1DayH,
       "cfprApProcessorErrorStatsSparingErrors1Hour": cfprApProcessorErrorStatsSparingErrors1Hour,
       "cfprApProcessorErrorStatsSparingErrors1HourH": cfprApProcessorErrorStatsSparingErrors1HourH,
       "cfprApProcessorErrorStatsSparingErrors1Week": cfprApProcessorErrorStatsSparingErrors1Week,
       "cfprApProcessorErrorStatsSparingErrors1WeekH": cfprApProcessorErrorStatsSparingErrors1WeekH,
       "cfprApProcessorErrorStatsSparingErrors2Weeks": cfprApProcessorErrorStatsSparingErrors2Weeks,
       "cfprApProcessorErrorStatsSparingErrors2WeeksH": cfprApProcessorErrorStatsSparingErrors2WeeksH,
       "cfprApProcessorErrorStatsSuspect": cfprApProcessorErrorStatsSuspect,
       "cfprApProcessorErrorStatsThresholded": cfprApProcessorErrorStatsThresholded,
       "cfprApProcessorErrorStatsTimeCollected": cfprApProcessorErrorStatsTimeCollected,
       "cfprApProcessorErrorStatsUpdate": cfprApProcessorErrorStatsUpdate,
       "cfprApProcessorQualTable": cfprApProcessorQualTable,
       "cfprApProcessorQualEntry": cfprApProcessorQualEntry,
       "cfprApProcessorQualInstanceId": cfprApProcessorQualInstanceId,
       "cfprApProcessorQualDn": cfprApProcessorQualDn,
       "cfprApProcessorQualRn": cfprApProcessorQualRn,
       "cfprApProcessorQualArch": cfprApProcessorQualArch,
       "cfprApProcessorQualMaxCores": cfprApProcessorQualMaxCores,
       "cfprApProcessorQualMaxProcs": cfprApProcessorQualMaxProcs,
       "cfprApProcessorQualMaxThreads": cfprApProcessorQualMaxThreads,
       "cfprApProcessorQualMinCores": cfprApProcessorQualMinCores,
       "cfprApProcessorQualMinProcs": cfprApProcessorQualMinProcs,
       "cfprApProcessorQualMinThreads": cfprApProcessorQualMinThreads,
       "cfprApProcessorQualModel": cfprApProcessorQualModel,
       "cfprApProcessorQualSpeed": cfprApProcessorQualSpeed,
       "cfprApProcessorQualStepping": cfprApProcessorQualStepping,
       "cfprApProcessorRuntimeTable": cfprApProcessorRuntimeTable,
       "cfprApProcessorRuntimeEntry": cfprApProcessorRuntimeEntry,
       "cfprApProcessorRuntimeInstanceId": cfprApProcessorRuntimeInstanceId,
       "cfprApProcessorRuntimeDn": cfprApProcessorRuntimeDn,
       "cfprApProcessorRuntimeRn": cfprApProcessorRuntimeRn,
       "cfprApProcessorRuntimeIntervals": cfprApProcessorRuntimeIntervals,
       "cfprApProcessorRuntimeLoad": cfprApProcessorRuntimeLoad,
       "cfprApProcessorRuntimeLoadAvg": cfprApProcessorRuntimeLoadAvg,
       "cfprApProcessorRuntimeLoadMax": cfprApProcessorRuntimeLoadMax,
       "cfprApProcessorRuntimeLoadMin": cfprApProcessorRuntimeLoadMin,
       "cfprApProcessorRuntimeSuspect": cfprApProcessorRuntimeSuspect,
       "cfprApProcessorRuntimeThresholded": cfprApProcessorRuntimeThresholded,
       "cfprApProcessorRuntimeTimeCollected": cfprApProcessorRuntimeTimeCollected,
       "cfprApProcessorRuntimeUpdate": cfprApProcessorRuntimeUpdate,
       "cfprApProcessorRuntimeUptime": cfprApProcessorRuntimeUptime,
       "cfprApProcessorRuntimeHistTable": cfprApProcessorRuntimeHistTable,
       "cfprApProcessorRuntimeHistEntry": cfprApProcessorRuntimeHistEntry,
       "cfprApProcessorRuntimeHistInstanceId": cfprApProcessorRuntimeHistInstanceId,
       "cfprApProcessorRuntimeHistDn": cfprApProcessorRuntimeHistDn,
       "cfprApProcessorRuntimeHistRn": cfprApProcessorRuntimeHistRn,
       "cfprApProcessorRuntimeHistId": cfprApProcessorRuntimeHistId,
       "cfprApProcessorRuntimeHistLoad": cfprApProcessorRuntimeHistLoad,
       "cfprApProcessorRuntimeHistLoadAvg": cfprApProcessorRuntimeHistLoadAvg,
       "cfprApProcessorRuntimeHistLoadMax": cfprApProcessorRuntimeHistLoadMax,
       "cfprApProcessorRuntimeHistLoadMin": cfprApProcessorRuntimeHistLoadMin,
       "cfprApProcessorRuntimeHistMostRecent": cfprApProcessorRuntimeHistMostRecent,
       "cfprApProcessorRuntimeHistSuspect": cfprApProcessorRuntimeHistSuspect,
       "cfprApProcessorRuntimeHistThresholded": cfprApProcessorRuntimeHistThresholded,
       "cfprApProcessorRuntimeHistTimeCollected": cfprApProcessorRuntimeHistTimeCollected,
       "cfprApProcessorThreadTable": cfprApProcessorThreadTable,
       "cfprApProcessorThreadEntry": cfprApProcessorThreadEntry,
       "cfprApProcessorThreadInstanceId": cfprApProcessorThreadInstanceId,
       "cfprApProcessorThreadDn": cfprApProcessorThreadDn,
       "cfprApProcessorThreadRn": cfprApProcessorThreadRn,
       "cfprApProcessorThreadId": cfprApProcessorThreadId,
       "cfprApProcessorUnitTable": cfprApProcessorUnitTable,
       "cfprApProcessorUnitEntry": cfprApProcessorUnitEntry,
       "cfprApProcessorUnitInstanceId": cfprApProcessorUnitInstanceId,
       "cfprApProcessorUnitDn": cfprApProcessorUnitDn,
       "cfprApProcessorUnitRn": cfprApProcessorUnitRn,
       "cfprApProcessorUnitArch": cfprApProcessorUnitArch,
       "cfprApProcessorUnitCores": cfprApProcessorUnitCores,
       "cfprApProcessorUnitCoresEnabled": cfprApProcessorUnitCoresEnabled,
       "cfprApProcessorUnitId": cfprApProcessorUnitId,
       "cfprApProcessorUnitLocationDn": cfprApProcessorUnitLocationDn,
       "cfprApProcessorUnitModel": cfprApProcessorUnitModel,
       "cfprApProcessorUnitOperQualifierReason": cfprApProcessorUnitOperQualifierReason,
       "cfprApProcessorUnitOperState": cfprApProcessorUnitOperState,
       "cfprApProcessorUnitOperability": cfprApProcessorUnitOperability,
       "cfprApProcessorUnitPerf": cfprApProcessorUnitPerf,
       "cfprApProcessorUnitPower": cfprApProcessorUnitPower,
       "cfprApProcessorUnitPresence": cfprApProcessorUnitPresence,
       "cfprApProcessorUnitRevision": cfprApProcessorUnitRevision,
       "cfprApProcessorUnitSerial": cfprApProcessorUnitSerial,
       "cfprApProcessorUnitSocketDesignation": cfprApProcessorUnitSocketDesignation,
       "cfprApProcessorUnitSpeed": cfprApProcessorUnitSpeed,
       "cfprApProcessorUnitStepping": cfprApProcessorUnitStepping,
       "cfprApProcessorUnitThermal": cfprApProcessorUnitThermal,
       "cfprApProcessorUnitThreads": cfprApProcessorUnitThreads,
       "cfprApProcessorUnitVendor": cfprApProcessorUnitVendor,
       "cfprApProcessorUnitVisibility": cfprApProcessorUnitVisibility,
       "cfprApProcessorUnitVoltage": cfprApProcessorUnitVoltage,
       "cfprApProcessorUnitAssocCtxTable": cfprApProcessorUnitAssocCtxTable,
       "cfprApProcessorUnitAssocCtxEntry": cfprApProcessorUnitAssocCtxEntry,
       "cfprApProcessorUnitAssocCtxInstanceId": cfprApProcessorUnitAssocCtxInstanceId,
       "cfprApProcessorUnitAssocCtxDn": cfprApProcessorUnitAssocCtxDn,
       "cfprApProcessorUnitAssocCtxRn": cfprApProcessorUnitAssocCtxRn,
       "cfprApProcessorUnitAssocCtxFruCapDn": cfprApProcessorUnitAssocCtxFruCapDn,
       "cfprApProcessorUnitAssocCtxStepping": cfprApProcessorUnitAssocCtxStepping}
)
