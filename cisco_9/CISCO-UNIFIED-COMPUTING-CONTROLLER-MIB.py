# SNMP MIB module (CISCO-UNIFIED-COMPUTING-CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UNIFIED-COMPUTING-CONTROLLER-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 08:58:45 2025
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

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

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

cucsControllerObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsControllerHaControllerTable_Object = MibTable
cucsControllerHaControllerTable = _CucsControllerHaControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 5)
)
if mibBuilder.loadTexts:
    cucsControllerHaControllerTable.setStatus("current")
_CucsControllerHaControllerEntry_Object = MibTableRow
cucsControllerHaControllerEntry = _CucsControllerHaControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 5, 1)
)
cucsControllerHaControllerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CONTROLLER-MIB", "cucsControllerHaControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsControllerHaControllerEntry.setStatus("current")
_CucsControllerHaControllerInstanceId_Type = CucsManagedObjectId
_CucsControllerHaControllerInstanceId_Object = MibTableColumn
cucsControllerHaControllerInstanceId = _CucsControllerHaControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 5, 1, 1),
    _CucsControllerHaControllerInstanceId_Type()
)
cucsControllerHaControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsControllerHaControllerInstanceId.setStatus("current")
_CucsControllerHaControllerDn_Type = CucsManagedObjectDn
_CucsControllerHaControllerDn_Object = MibTableColumn
cucsControllerHaControllerDn = _CucsControllerHaControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 5, 1, 2),
    _CucsControllerHaControllerDn_Type()
)
cucsControllerHaControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerHaControllerDn.setStatus("current")
_CucsControllerHaControllerRn_Type = SnmpAdminString
_CucsControllerHaControllerRn_Object = MibTableColumn
cucsControllerHaControllerRn = _CucsControllerHaControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 5, 1, 3),
    _CucsControllerHaControllerRn_Type()
)
cucsControllerHaControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerHaControllerRn.setStatus("current")
_CucsControllerHaControllerTrigElectionFlag_Type = TruthValue
_CucsControllerHaControllerTrigElectionFlag_Object = MibTableColumn
cucsControllerHaControllerTrigElectionFlag = _CucsControllerHaControllerTrigElectionFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 5, 1, 4),
    _CucsControllerHaControllerTrigElectionFlag_Type()
)
cucsControllerHaControllerTrigElectionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerHaControllerTrigElectionFlag.setStatus("current")
_CucsControllerOperationalVersionHolderTable_Object = MibTable
cucsControllerOperationalVersionHolderTable = _CucsControllerOperationalVersionHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 6)
)
if mibBuilder.loadTexts:
    cucsControllerOperationalVersionHolderTable.setStatus("current")
_CucsControllerOperationalVersionHolderEntry_Object = MibTableRow
cucsControllerOperationalVersionHolderEntry = _CucsControllerOperationalVersionHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 6, 1)
)
cucsControllerOperationalVersionHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CONTROLLER-MIB", "cucsControllerOperationalVersionHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsControllerOperationalVersionHolderEntry.setStatus("current")
_CucsControllerOperationalVersionHolderInstanceId_Type = CucsManagedObjectId
_CucsControllerOperationalVersionHolderInstanceId_Object = MibTableColumn
cucsControllerOperationalVersionHolderInstanceId = _CucsControllerOperationalVersionHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 6, 1, 1),
    _CucsControllerOperationalVersionHolderInstanceId_Type()
)
cucsControllerOperationalVersionHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsControllerOperationalVersionHolderInstanceId.setStatus("current")
_CucsControllerOperationalVersionHolderDn_Type = CucsManagedObjectDn
_CucsControllerOperationalVersionHolderDn_Object = MibTableColumn
cucsControllerOperationalVersionHolderDn = _CucsControllerOperationalVersionHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 6, 1, 2),
    _CucsControllerOperationalVersionHolderDn_Type()
)
cucsControllerOperationalVersionHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerOperationalVersionHolderDn.setStatus("current")
_CucsControllerOperationalVersionHolderRn_Type = SnmpAdminString
_CucsControllerOperationalVersionHolderRn_Object = MibTableColumn
cucsControllerOperationalVersionHolderRn = _CucsControllerOperationalVersionHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 6, 1, 3),
    _CucsControllerOperationalVersionHolderRn_Type()
)
cucsControllerOperationalVersionHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerOperationalVersionHolderRn.setStatus("current")
_CucsControllerOperationalVersionHolderSerial_Type = SnmpAdminString
_CucsControllerOperationalVersionHolderSerial_Object = MibTableColumn
cucsControllerOperationalVersionHolderSerial = _CucsControllerOperationalVersionHolderSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 6, 1, 4),
    _CucsControllerOperationalVersionHolderSerial_Type()
)
cucsControllerOperationalVersionHolderSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerOperationalVersionHolderSerial.setStatus("current")
_CucsControllerPreferedVersionHolderTable_Object = MibTable
cucsControllerPreferedVersionHolderTable = _CucsControllerPreferedVersionHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 7)
)
if mibBuilder.loadTexts:
    cucsControllerPreferedVersionHolderTable.setStatus("current")
_CucsControllerPreferedVersionHolderEntry_Object = MibTableRow
cucsControllerPreferedVersionHolderEntry = _CucsControllerPreferedVersionHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 7, 1)
)
cucsControllerPreferedVersionHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CONTROLLER-MIB", "cucsControllerPreferedVersionHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsControllerPreferedVersionHolderEntry.setStatus("current")
_CucsControllerPreferedVersionHolderInstanceId_Type = CucsManagedObjectId
_CucsControllerPreferedVersionHolderInstanceId_Object = MibTableColumn
cucsControllerPreferedVersionHolderInstanceId = _CucsControllerPreferedVersionHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 7, 1, 1),
    _CucsControllerPreferedVersionHolderInstanceId_Type()
)
cucsControllerPreferedVersionHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsControllerPreferedVersionHolderInstanceId.setStatus("current")
_CucsControllerPreferedVersionHolderDn_Type = CucsManagedObjectDn
_CucsControllerPreferedVersionHolderDn_Object = MibTableColumn
cucsControllerPreferedVersionHolderDn = _CucsControllerPreferedVersionHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 7, 1, 2),
    _CucsControllerPreferedVersionHolderDn_Type()
)
cucsControllerPreferedVersionHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerPreferedVersionHolderDn.setStatus("current")
_CucsControllerPreferedVersionHolderRn_Type = SnmpAdminString
_CucsControllerPreferedVersionHolderRn_Object = MibTableColumn
cucsControllerPreferedVersionHolderRn = _CucsControllerPreferedVersionHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 7, 1, 3),
    _CucsControllerPreferedVersionHolderRn_Type()
)
cucsControllerPreferedVersionHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerPreferedVersionHolderRn.setStatus("current")
_CucsControllerPreferedVersionHolderInUse_Type = TruthValue
_CucsControllerPreferedVersionHolderInUse_Object = MibTableColumn
cucsControllerPreferedVersionHolderInUse = _CucsControllerPreferedVersionHolderInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 7, 1, 4),
    _CucsControllerPreferedVersionHolderInUse_Type()
)
cucsControllerPreferedVersionHolderInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerPreferedVersionHolderInUse.setStatus("current")
_CucsControllerPreferedVersionHolderSerial_Type = SnmpAdminString
_CucsControllerPreferedVersionHolderSerial_Object = MibTableColumn
cucsControllerPreferedVersionHolderSerial = _CucsControllerPreferedVersionHolderSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 7, 1, 5),
    _CucsControllerPreferedVersionHolderSerial_Type()
)
cucsControllerPreferedVersionHolderSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerPreferedVersionHolderSerial.setStatus("current")
_CucsControllerMgmtDbCheckPolTable_Object = MibTable
cucsControllerMgmtDbCheckPolTable = _CucsControllerMgmtDbCheckPolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8)
)
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolTable.setStatus("current")
_CucsControllerMgmtDbCheckPolEntry_Object = MibTableRow
cucsControllerMgmtDbCheckPolEntry = _CucsControllerMgmtDbCheckPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1)
)
cucsControllerMgmtDbCheckPolEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CONTROLLER-MIB", "cucsControllerMgmtDbCheckPolInstanceId"),
)
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolEntry.setStatus("current")
_CucsControllerMgmtDbCheckPolInstanceId_Type = CucsManagedObjectId
_CucsControllerMgmtDbCheckPolInstanceId_Object = MibTableColumn
cucsControllerMgmtDbCheckPolInstanceId = _CucsControllerMgmtDbCheckPolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 1),
    _CucsControllerMgmtDbCheckPolInstanceId_Type()
)
cucsControllerMgmtDbCheckPolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolInstanceId.setStatus("current")
_CucsControllerMgmtDbCheckPolDn_Type = CucsManagedObjectDn
_CucsControllerMgmtDbCheckPolDn_Object = MibTableColumn
cucsControllerMgmtDbCheckPolDn = _CucsControllerMgmtDbCheckPolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 2),
    _CucsControllerMgmtDbCheckPolDn_Type()
)
cucsControllerMgmtDbCheckPolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolDn.setStatus("current")
_CucsControllerMgmtDbCheckPolRn_Type = SnmpAdminString
_CucsControllerMgmtDbCheckPolRn_Object = MibTableColumn
cucsControllerMgmtDbCheckPolRn = _CucsControllerMgmtDbCheckPolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 3),
    _CucsControllerMgmtDbCheckPolRn_Type()
)
cucsControllerMgmtDbCheckPolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolRn.setStatus("current")
_CucsControllerMgmtDbCheckPolHealthCheckInterval_Type = Gauge32
_CucsControllerMgmtDbCheckPolHealthCheckInterval_Object = MibTableColumn
cucsControllerMgmtDbCheckPolHealthCheckInterval = _CucsControllerMgmtDbCheckPolHealthCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 4),
    _CucsControllerMgmtDbCheckPolHealthCheckInterval_Type()
)
cucsControllerMgmtDbCheckPolHealthCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolHealthCheckInterval.setStatus("current")
_CucsControllerMgmtDbCheckPolInternalBackupInterval_Type = Gauge32
_CucsControllerMgmtDbCheckPolInternalBackupInterval_Object = MibTableColumn
cucsControllerMgmtDbCheckPolInternalBackupInterval = _CucsControllerMgmtDbCheckPolInternalBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 5),
    _CucsControllerMgmtDbCheckPolInternalBackupInterval_Type()
)
cucsControllerMgmtDbCheckPolInternalBackupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolInternalBackupInterval.setStatus("current")
_CucsControllerMgmtDbCheckPolLastIntegrityCheckTime_Type = DateAndTime
_CucsControllerMgmtDbCheckPolLastIntegrityCheckTime_Object = MibTableColumn
cucsControllerMgmtDbCheckPolLastIntegrityCheckTime = _CucsControllerMgmtDbCheckPolLastIntegrityCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 6),
    _CucsControllerMgmtDbCheckPolLastIntegrityCheckTime_Type()
)
cucsControllerMgmtDbCheckPolLastIntegrityCheckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolLastIntegrityCheckTime.setStatus("current")
_CucsControllerMgmtDbCheckPolLastInternalBackupTime_Type = DateAndTime
_CucsControllerMgmtDbCheckPolLastInternalBackupTime_Object = MibTableColumn
cucsControllerMgmtDbCheckPolLastInternalBackupTime = _CucsControllerMgmtDbCheckPolLastInternalBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 7),
    _CucsControllerMgmtDbCheckPolLastInternalBackupTime_Type()
)
cucsControllerMgmtDbCheckPolLastInternalBackupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolLastInternalBackupTime.setStatus("current")
_CucsControllerMgmtDbCheckPolResetCorruptCount_Type = TruthValue
_CucsControllerMgmtDbCheckPolResetCorruptCount_Object = MibTableColumn
cucsControllerMgmtDbCheckPolResetCorruptCount = _CucsControllerMgmtDbCheckPolResetCorruptCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 8),
    _CucsControllerMgmtDbCheckPolResetCorruptCount_Type()
)
cucsControllerMgmtDbCheckPolResetCorruptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolResetCorruptCount.setStatus("current")
_CucsControllerMgmtDbCheckPolTriggerHealthCheck_Type = TruthValue
_CucsControllerMgmtDbCheckPolTriggerHealthCheck_Object = MibTableColumn
cucsControllerMgmtDbCheckPolTriggerHealthCheck = _CucsControllerMgmtDbCheckPolTriggerHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 83, 8, 1, 9),
    _CucsControllerMgmtDbCheckPolTriggerHealthCheck_Type()
)
cucsControllerMgmtDbCheckPolTriggerHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsControllerMgmtDbCheckPolTriggerHealthCheck.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-CONTROLLER-MIB",
    **{"cucsControllerObjects": cucsControllerObjects,
       "cucsControllerHaControllerTable": cucsControllerHaControllerTable,
       "cucsControllerHaControllerEntry": cucsControllerHaControllerEntry,
       "cucsControllerHaControllerInstanceId": cucsControllerHaControllerInstanceId,
       "cucsControllerHaControllerDn": cucsControllerHaControllerDn,
       "cucsControllerHaControllerRn": cucsControllerHaControllerRn,
       "cucsControllerHaControllerTrigElectionFlag": cucsControllerHaControllerTrigElectionFlag,
       "cucsControllerOperationalVersionHolderTable": cucsControllerOperationalVersionHolderTable,
       "cucsControllerOperationalVersionHolderEntry": cucsControllerOperationalVersionHolderEntry,
       "cucsControllerOperationalVersionHolderInstanceId": cucsControllerOperationalVersionHolderInstanceId,
       "cucsControllerOperationalVersionHolderDn": cucsControllerOperationalVersionHolderDn,
       "cucsControllerOperationalVersionHolderRn": cucsControllerOperationalVersionHolderRn,
       "cucsControllerOperationalVersionHolderSerial": cucsControllerOperationalVersionHolderSerial,
       "cucsControllerPreferedVersionHolderTable": cucsControllerPreferedVersionHolderTable,
       "cucsControllerPreferedVersionHolderEntry": cucsControllerPreferedVersionHolderEntry,
       "cucsControllerPreferedVersionHolderInstanceId": cucsControllerPreferedVersionHolderInstanceId,
       "cucsControllerPreferedVersionHolderDn": cucsControllerPreferedVersionHolderDn,
       "cucsControllerPreferedVersionHolderRn": cucsControllerPreferedVersionHolderRn,
       "cucsControllerPreferedVersionHolderInUse": cucsControllerPreferedVersionHolderInUse,
       "cucsControllerPreferedVersionHolderSerial": cucsControllerPreferedVersionHolderSerial,
       "cucsControllerMgmtDbCheckPolTable": cucsControllerMgmtDbCheckPolTable,
       "cucsControllerMgmtDbCheckPolEntry": cucsControllerMgmtDbCheckPolEntry,
       "cucsControllerMgmtDbCheckPolInstanceId": cucsControllerMgmtDbCheckPolInstanceId,
       "cucsControllerMgmtDbCheckPolDn": cucsControllerMgmtDbCheckPolDn,
       "cucsControllerMgmtDbCheckPolRn": cucsControllerMgmtDbCheckPolRn,
       "cucsControllerMgmtDbCheckPolHealthCheckInterval": cucsControllerMgmtDbCheckPolHealthCheckInterval,
       "cucsControllerMgmtDbCheckPolInternalBackupInterval": cucsControllerMgmtDbCheckPolInternalBackupInterval,
       "cucsControllerMgmtDbCheckPolLastIntegrityCheckTime": cucsControllerMgmtDbCheckPolLastIntegrityCheckTime,
       "cucsControllerMgmtDbCheckPolLastInternalBackupTime": cucsControllerMgmtDbCheckPolLastInternalBackupTime,
       "cucsControllerMgmtDbCheckPolResetCorruptCount": cucsControllerMgmtDbCheckPolResetCorruptCount,
       "cucsControllerMgmtDbCheckPolTriggerHealthCheck": cucsControllerMgmtDbCheckPolTriggerHealthCheck}
)
