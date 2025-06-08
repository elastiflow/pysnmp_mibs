# SNMP MIB module (CISCO-FIREPOWER-AP-PROC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-PROC-MIB.mib
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

(CfprApProcStatAdminState,) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApProcStatAdminState")

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

cfprApProcObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApProcDoerTable_Object = MibTable
cfprApProcDoerTable = _CfprApProcDoerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 1)
)
if mibBuilder.loadTexts:
    cfprApProcDoerTable.setStatus("current")
_CfprApProcDoerEntry_Object = MibTableRow
cfprApProcDoerEntry = _CfprApProcDoerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 1, 1)
)
cfprApProcDoerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROC-MIB", "cfprApProcDoerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcDoerEntry.setStatus("current")
_CfprApProcDoerInstanceId_Type = CfprApManagedObjectId
_CfprApProcDoerInstanceId_Object = MibTableColumn
cfprApProcDoerInstanceId = _CfprApProcDoerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 1, 1, 1),
    _CfprApProcDoerInstanceId_Type()
)
cfprApProcDoerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcDoerInstanceId.setStatus("current")
_CfprApProcDoerDn_Type = CfprApManagedObjectDn
_CfprApProcDoerDn_Object = MibTableColumn
cfprApProcDoerDn = _CfprApProcDoerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 1, 1, 2),
    _CfprApProcDoerDn_Type()
)
cfprApProcDoerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcDoerDn.setStatus("current")
_CfprApProcDoerRn_Type = SnmpAdminString
_CfprApProcDoerRn_Object = MibTableColumn
cfprApProcDoerRn = _CfprApProcDoerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 1, 1, 3),
    _CfprApProcDoerRn_Type()
)
cfprApProcDoerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcDoerRn.setStatus("current")
_CfprApProcDoerId_Type = Gauge32
_CfprApProcDoerId_Object = MibTableColumn
cfprApProcDoerId = _CfprApProcDoerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 1, 1, 4),
    _CfprApProcDoerId_Type()
)
cfprApProcDoerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcDoerId.setStatus("current")
_CfprApProcDoerName_Type = SnmpAdminString
_CfprApProcDoerName_Object = MibTableColumn
cfprApProcDoerName = _CfprApProcDoerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 1, 1, 5),
    _CfprApProcDoerName_Type()
)
cfprApProcDoerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcDoerName.setStatus("current")
_CfprApProcManagerTable_Object = MibTable
cfprApProcManagerTable = _CfprApProcManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 2)
)
if mibBuilder.loadTexts:
    cfprApProcManagerTable.setStatus("current")
_CfprApProcManagerEntry_Object = MibTableRow
cfprApProcManagerEntry = _CfprApProcManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 2, 1)
)
cfprApProcManagerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROC-MIB", "cfprApProcManagerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcManagerEntry.setStatus("current")
_CfprApProcManagerInstanceId_Type = CfprApManagedObjectId
_CfprApProcManagerInstanceId_Object = MibTableColumn
cfprApProcManagerInstanceId = _CfprApProcManagerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 2, 1, 1),
    _CfprApProcManagerInstanceId_Type()
)
cfprApProcManagerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcManagerInstanceId.setStatus("current")
_CfprApProcManagerDn_Type = CfprApManagedObjectDn
_CfprApProcManagerDn_Object = MibTableColumn
cfprApProcManagerDn = _CfprApProcManagerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 2, 1, 2),
    _CfprApProcManagerDn_Type()
)
cfprApProcManagerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcManagerDn.setStatus("current")
_CfprApProcManagerRn_Type = SnmpAdminString
_CfprApProcManagerRn_Object = MibTableColumn
cfprApProcManagerRn = _CfprApProcManagerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 2, 1, 3),
    _CfprApProcManagerRn_Type()
)
cfprApProcManagerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcManagerRn.setStatus("current")
_CfprApProcPrtTable_Object = MibTable
cfprApProcPrtTable = _CfprApProcPrtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 3)
)
if mibBuilder.loadTexts:
    cfprApProcPrtTable.setStatus("current")
_CfprApProcPrtEntry_Object = MibTableRow
cfprApProcPrtEntry = _CfprApProcPrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 3, 1)
)
cfprApProcPrtEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROC-MIB", "cfprApProcPrtInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcPrtEntry.setStatus("current")
_CfprApProcPrtInstanceId_Type = CfprApManagedObjectId
_CfprApProcPrtInstanceId_Object = MibTableColumn
cfprApProcPrtInstanceId = _CfprApProcPrtInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 3, 1, 1),
    _CfprApProcPrtInstanceId_Type()
)
cfprApProcPrtInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcPrtInstanceId.setStatus("current")
_CfprApProcPrtDn_Type = CfprApManagedObjectDn
_CfprApProcPrtDn_Object = MibTableColumn
cfprApProcPrtDn = _CfprApProcPrtDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 3, 1, 2),
    _CfprApProcPrtDn_Type()
)
cfprApProcPrtDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtDn.setStatus("current")
_CfprApProcPrtRn_Type = SnmpAdminString
_CfprApProcPrtRn_Object = MibTableColumn
cfprApProcPrtRn = _CfprApProcPrtRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 3, 1, 3),
    _CfprApProcPrtRn_Type()
)
cfprApProcPrtRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtRn.setStatus("current")
_CfprApProcPrtId_Type = Gauge32
_CfprApProcPrtId_Object = MibTableColumn
cfprApProcPrtId = _CfprApProcPrtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 3, 1, 4),
    _CfprApProcPrtId_Type()
)
cfprApProcPrtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtId.setStatus("current")
_CfprApProcPrtName_Type = SnmpAdminString
_CfprApProcPrtName_Object = MibTableColumn
cfprApProcPrtName = _CfprApProcPrtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 3, 1, 5),
    _CfprApProcPrtName_Type()
)
cfprApProcPrtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtName.setStatus("current")
_CfprApProcPrtCountsTable_Object = MibTable
cfprApProcPrtCountsTable = _CfprApProcPrtCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4)
)
if mibBuilder.loadTexts:
    cfprApProcPrtCountsTable.setStatus("current")
_CfprApProcPrtCountsEntry_Object = MibTableRow
cfprApProcPrtCountsEntry = _CfprApProcPrtCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1)
)
cfprApProcPrtCountsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROC-MIB", "cfprApProcPrtCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcPrtCountsEntry.setStatus("current")
_CfprApProcPrtCountsInstanceId_Type = CfprApManagedObjectId
_CfprApProcPrtCountsInstanceId_Object = MibTableColumn
cfprApProcPrtCountsInstanceId = _CfprApProcPrtCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1, 1),
    _CfprApProcPrtCountsInstanceId_Type()
)
cfprApProcPrtCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcPrtCountsInstanceId.setStatus("current")
_CfprApProcPrtCountsDn_Type = CfprApManagedObjectDn
_CfprApProcPrtCountsDn_Object = MibTableColumn
cfprApProcPrtCountsDn = _CfprApProcPrtCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1, 2),
    _CfprApProcPrtCountsDn_Type()
)
cfprApProcPrtCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtCountsDn.setStatus("current")
_CfprApProcPrtCountsRn_Type = SnmpAdminString
_CfprApProcPrtCountsRn_Object = MibTableColumn
cfprApProcPrtCountsRn = _CfprApProcPrtCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1, 3),
    _CfprApProcPrtCountsRn_Type()
)
cfprApProcPrtCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtCountsRn.setStatus("current")
_CfprApProcPrtCountsCachenospc_Type = Gauge32
_CfprApProcPrtCountsCachenospc_Object = MibTableColumn
cfprApProcPrtCountsCachenospc = _CfprApProcPrtCountsCachenospc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1, 4),
    _CfprApProcPrtCountsCachenospc_Type()
)
cfprApProcPrtCountsCachenospc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtCountsCachenospc.setStatus("current")
_CfprApProcPrtCountsDbtxs_Type = Gauge32
_CfprApProcPrtCountsDbtxs_Object = MibTableColumn
cfprApProcPrtCountsDbtxs = _CfprApProcPrtCountsDbtxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1, 5),
    _CfprApProcPrtCountsDbtxs_Type()
)
cfprApProcPrtCountsDbtxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtCountsDbtxs.setStatus("current")
_CfprApProcPrtCountsLargetxs_Type = Gauge32
_CfprApProcPrtCountsLargetxs_Object = MibTableColumn
cfprApProcPrtCountsLargetxs = _CfprApProcPrtCountsLargetxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1, 6),
    _CfprApProcPrtCountsLargetxs_Type()
)
cfprApProcPrtCountsLargetxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtCountsLargetxs.setStatus("current")
_CfprApProcPrtCountsPersistTime_Type = Unsigned64
_CfprApProcPrtCountsPersistTime_Object = MibTableColumn
cfprApProcPrtCountsPersistTime = _CfprApProcPrtCountsPersistTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1, 7),
    _CfprApProcPrtCountsPersistTime_Type()
)
cfprApProcPrtCountsPersistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtCountsPersistTime.setStatus("current")
_CfprApProcPrtCountsTotal_Type = Gauge32
_CfprApProcPrtCountsTotal_Object = MibTableColumn
cfprApProcPrtCountsTotal = _CfprApProcPrtCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 4, 1, 8),
    _CfprApProcPrtCountsTotal_Type()
)
cfprApProcPrtCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcPrtCountsTotal.setStatus("current")
_CfprApProcStimulusCountsTable_Object = MibTable
cfprApProcStimulusCountsTable = _CfprApProcStimulusCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5)
)
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsTable.setStatus("current")
_CfprApProcStimulusCountsEntry_Object = MibTableRow
cfprApProcStimulusCountsEntry = _CfprApProcStimulusCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1)
)
cfprApProcStimulusCountsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROC-MIB", "cfprApProcStimulusCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsEntry.setStatus("current")
_CfprApProcStimulusCountsInstanceId_Type = CfprApManagedObjectId
_CfprApProcStimulusCountsInstanceId_Object = MibTableColumn
cfprApProcStimulusCountsInstanceId = _CfprApProcStimulusCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 1),
    _CfprApProcStimulusCountsInstanceId_Type()
)
cfprApProcStimulusCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsInstanceId.setStatus("current")
_CfprApProcStimulusCountsDn_Type = CfprApManagedObjectDn
_CfprApProcStimulusCountsDn_Object = MibTableColumn
cfprApProcStimulusCountsDn = _CfprApProcStimulusCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 2),
    _CfprApProcStimulusCountsDn_Type()
)
cfprApProcStimulusCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsDn.setStatus("current")
_CfprApProcStimulusCountsRn_Type = SnmpAdminString
_CfprApProcStimulusCountsRn_Object = MibTableColumn
cfprApProcStimulusCountsRn = _CfprApProcStimulusCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 3),
    _CfprApProcStimulusCountsRn_Type()
)
cfprApProcStimulusCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsRn.setStatus("current")
_CfprApProcStimulusCountsAdminState_Type = CfprApProcStatAdminState
_CfprApProcStimulusCountsAdminState_Object = MibTableColumn
cfprApProcStimulusCountsAdminState = _CfprApProcStimulusCountsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 4),
    _CfprApProcStimulusCountsAdminState_Type()
)
cfprApProcStimulusCountsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsAdminState.setStatus("current")
_CfprApProcStimulusCountsBulked_Type = Gauge32
_CfprApProcStimulusCountsBulked_Object = MibTableColumn
cfprApProcStimulusCountsBulked = _CfprApProcStimulusCountsBulked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 5),
    _CfprApProcStimulusCountsBulked_Type()
)
cfprApProcStimulusCountsBulked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsBulked.setStatus("current")
_CfprApProcStimulusCountsFailed_Type = Gauge32
_CfprApProcStimulusCountsFailed_Object = MibTableColumn
cfprApProcStimulusCountsFailed = _CfprApProcStimulusCountsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 6),
    _CfprApProcStimulusCountsFailed_Type()
)
cfprApProcStimulusCountsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsFailed.setStatus("current")
_CfprApProcStimulusCountsRetried_Type = Gauge32
_CfprApProcStimulusCountsRetried_Object = MibTableColumn
cfprApProcStimulusCountsRetried = _CfprApProcStimulusCountsRetried_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 7),
    _CfprApProcStimulusCountsRetried_Type()
)
cfprApProcStimulusCountsRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsRetried.setStatus("current")
_CfprApProcStimulusCountsSingleton_Type = Gauge32
_CfprApProcStimulusCountsSingleton_Object = MibTableColumn
cfprApProcStimulusCountsSingleton = _CfprApProcStimulusCountsSingleton_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 8),
    _CfprApProcStimulusCountsSingleton_Type()
)
cfprApProcStimulusCountsSingleton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsSingleton.setStatus("current")
_CfprApProcStimulusCountsSuccessfull_Type = Gauge32
_CfprApProcStimulusCountsSuccessfull_Object = MibTableColumn
cfprApProcStimulusCountsSuccessfull = _CfprApProcStimulusCountsSuccessfull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 9),
    _CfprApProcStimulusCountsSuccessfull_Type()
)
cfprApProcStimulusCountsSuccessfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsSuccessfull.setStatus("current")
_CfprApProcStimulusCountsTotal_Type = Gauge32
_CfprApProcStimulusCountsTotal_Object = MibTableColumn
cfprApProcStimulusCountsTotal = _CfprApProcStimulusCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 5, 1, 10),
    _CfprApProcStimulusCountsTotal_Type()
)
cfprApProcStimulusCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcStimulusCountsTotal.setStatus("current")
_CfprApProcSvcTable_Object = MibTable
cfprApProcSvcTable = _CfprApProcSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 6)
)
if mibBuilder.loadTexts:
    cfprApProcSvcTable.setStatus("current")
_CfprApProcSvcEntry_Object = MibTableRow
cfprApProcSvcEntry = _CfprApProcSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 6, 1)
)
cfprApProcSvcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROC-MIB", "cfprApProcSvcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcSvcEntry.setStatus("current")
_CfprApProcSvcInstanceId_Type = CfprApManagedObjectId
_CfprApProcSvcInstanceId_Object = MibTableColumn
cfprApProcSvcInstanceId = _CfprApProcSvcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 6, 1, 1),
    _CfprApProcSvcInstanceId_Type()
)
cfprApProcSvcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcSvcInstanceId.setStatus("current")
_CfprApProcSvcDn_Type = CfprApManagedObjectDn
_CfprApProcSvcDn_Object = MibTableColumn
cfprApProcSvcDn = _CfprApProcSvcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 6, 1, 2),
    _CfprApProcSvcDn_Type()
)
cfprApProcSvcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcSvcDn.setStatus("current")
_CfprApProcSvcRn_Type = SnmpAdminString
_CfprApProcSvcRn_Object = MibTableColumn
cfprApProcSvcRn = _CfprApProcSvcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 6, 1, 3),
    _CfprApProcSvcRn_Type()
)
cfprApProcSvcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcSvcRn.setStatus("current")
_CfprApProcSvcId_Type = Gauge32
_CfprApProcSvcId_Object = MibTableColumn
cfprApProcSvcId = _CfprApProcSvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 6, 1, 4),
    _CfprApProcSvcId_Type()
)
cfprApProcSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcSvcId.setStatus("current")
_CfprApProcSvcName_Type = SnmpAdminString
_CfprApProcSvcName_Object = MibTableColumn
cfprApProcSvcName = _CfprApProcSvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 6, 1, 5),
    _CfprApProcSvcName_Type()
)
cfprApProcSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcSvcName.setStatus("current")
_CfprApProcTxCountsTable_Object = MibTable
cfprApProcTxCountsTable = _CfprApProcTxCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7)
)
if mibBuilder.loadTexts:
    cfprApProcTxCountsTable.setStatus("current")
_CfprApProcTxCountsEntry_Object = MibTableRow
cfprApProcTxCountsEntry = _CfprApProcTxCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1)
)
cfprApProcTxCountsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PROC-MIB", "cfprApProcTxCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApProcTxCountsEntry.setStatus("current")
_CfprApProcTxCountsInstanceId_Type = CfprApManagedObjectId
_CfprApProcTxCountsInstanceId_Object = MibTableColumn
cfprApProcTxCountsInstanceId = _CfprApProcTxCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 1),
    _CfprApProcTxCountsInstanceId_Type()
)
cfprApProcTxCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApProcTxCountsInstanceId.setStatus("current")
_CfprApProcTxCountsDn_Type = CfprApManagedObjectDn
_CfprApProcTxCountsDn_Object = MibTableColumn
cfprApProcTxCountsDn = _CfprApProcTxCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 2),
    _CfprApProcTxCountsDn_Type()
)
cfprApProcTxCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsDn.setStatus("current")
_CfprApProcTxCountsRn_Type = SnmpAdminString
_CfprApProcTxCountsRn_Object = MibTableColumn
cfprApProcTxCountsRn = _CfprApProcTxCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 3),
    _CfprApProcTxCountsRn_Type()
)
cfprApProcTxCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsRn.setStatus("current")
_CfprApProcTxCountsAdminState_Type = CfprApProcStatAdminState
_CfprApProcTxCountsAdminState_Object = MibTableColumn
cfprApProcTxCountsAdminState = _CfprApProcTxCountsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 4),
    _CfprApProcTxCountsAdminState_Type()
)
cfprApProcTxCountsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsAdminState.setStatus("current")
_CfprApProcTxCountsBulked_Type = Gauge32
_CfprApProcTxCountsBulked_Object = MibTableColumn
cfprApProcTxCountsBulked = _CfprApProcTxCountsBulked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 5),
    _CfprApProcTxCountsBulked_Type()
)
cfprApProcTxCountsBulked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsBulked.setStatus("current")
_CfprApProcTxCountsFailed_Type = Gauge32
_CfprApProcTxCountsFailed_Object = MibTableColumn
cfprApProcTxCountsFailed = _CfprApProcTxCountsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 6),
    _CfprApProcTxCountsFailed_Type()
)
cfprApProcTxCountsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsFailed.setStatus("current")
_CfprApProcTxCountsRetried_Type = Gauge32
_CfprApProcTxCountsRetried_Object = MibTableColumn
cfprApProcTxCountsRetried = _CfprApProcTxCountsRetried_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 7),
    _CfprApProcTxCountsRetried_Type()
)
cfprApProcTxCountsRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsRetried.setStatus("current")
_CfprApProcTxCountsSingleton_Type = Gauge32
_CfprApProcTxCountsSingleton_Object = MibTableColumn
cfprApProcTxCountsSingleton = _CfprApProcTxCountsSingleton_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 8),
    _CfprApProcTxCountsSingleton_Type()
)
cfprApProcTxCountsSingleton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsSingleton.setStatus("current")
_CfprApProcTxCountsSuccessfull_Type = Gauge32
_CfprApProcTxCountsSuccessfull_Object = MibTableColumn
cfprApProcTxCountsSuccessfull = _CfprApProcTxCountsSuccessfull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 9),
    _CfprApProcTxCountsSuccessfull_Type()
)
cfprApProcTxCountsSuccessfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsSuccessfull.setStatus("current")
_CfprApProcTxCountsTotal_Type = Gauge32
_CfprApProcTxCountsTotal_Object = MibTableColumn
cfprApProcTxCountsTotal = _CfprApProcTxCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 65, 7, 1, 10),
    _CfprApProcTxCountsTotal_Type()
)
cfprApProcTxCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApProcTxCountsTotal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-PROC-MIB",
    **{"cfprApProcObjects": cfprApProcObjects,
       "cfprApProcDoerTable": cfprApProcDoerTable,
       "cfprApProcDoerEntry": cfprApProcDoerEntry,
       "cfprApProcDoerInstanceId": cfprApProcDoerInstanceId,
       "cfprApProcDoerDn": cfprApProcDoerDn,
       "cfprApProcDoerRn": cfprApProcDoerRn,
       "cfprApProcDoerId": cfprApProcDoerId,
       "cfprApProcDoerName": cfprApProcDoerName,
       "cfprApProcManagerTable": cfprApProcManagerTable,
       "cfprApProcManagerEntry": cfprApProcManagerEntry,
       "cfprApProcManagerInstanceId": cfprApProcManagerInstanceId,
       "cfprApProcManagerDn": cfprApProcManagerDn,
       "cfprApProcManagerRn": cfprApProcManagerRn,
       "cfprApProcPrtTable": cfprApProcPrtTable,
       "cfprApProcPrtEntry": cfprApProcPrtEntry,
       "cfprApProcPrtInstanceId": cfprApProcPrtInstanceId,
       "cfprApProcPrtDn": cfprApProcPrtDn,
       "cfprApProcPrtRn": cfprApProcPrtRn,
       "cfprApProcPrtId": cfprApProcPrtId,
       "cfprApProcPrtName": cfprApProcPrtName,
       "cfprApProcPrtCountsTable": cfprApProcPrtCountsTable,
       "cfprApProcPrtCountsEntry": cfprApProcPrtCountsEntry,
       "cfprApProcPrtCountsInstanceId": cfprApProcPrtCountsInstanceId,
       "cfprApProcPrtCountsDn": cfprApProcPrtCountsDn,
       "cfprApProcPrtCountsRn": cfprApProcPrtCountsRn,
       "cfprApProcPrtCountsCachenospc": cfprApProcPrtCountsCachenospc,
       "cfprApProcPrtCountsDbtxs": cfprApProcPrtCountsDbtxs,
       "cfprApProcPrtCountsLargetxs": cfprApProcPrtCountsLargetxs,
       "cfprApProcPrtCountsPersistTime": cfprApProcPrtCountsPersistTime,
       "cfprApProcPrtCountsTotal": cfprApProcPrtCountsTotal,
       "cfprApProcStimulusCountsTable": cfprApProcStimulusCountsTable,
       "cfprApProcStimulusCountsEntry": cfprApProcStimulusCountsEntry,
       "cfprApProcStimulusCountsInstanceId": cfprApProcStimulusCountsInstanceId,
       "cfprApProcStimulusCountsDn": cfprApProcStimulusCountsDn,
       "cfprApProcStimulusCountsRn": cfprApProcStimulusCountsRn,
       "cfprApProcStimulusCountsAdminState": cfprApProcStimulusCountsAdminState,
       "cfprApProcStimulusCountsBulked": cfprApProcStimulusCountsBulked,
       "cfprApProcStimulusCountsFailed": cfprApProcStimulusCountsFailed,
       "cfprApProcStimulusCountsRetried": cfprApProcStimulusCountsRetried,
       "cfprApProcStimulusCountsSingleton": cfprApProcStimulusCountsSingleton,
       "cfprApProcStimulusCountsSuccessfull": cfprApProcStimulusCountsSuccessfull,
       "cfprApProcStimulusCountsTotal": cfprApProcStimulusCountsTotal,
       "cfprApProcSvcTable": cfprApProcSvcTable,
       "cfprApProcSvcEntry": cfprApProcSvcEntry,
       "cfprApProcSvcInstanceId": cfprApProcSvcInstanceId,
       "cfprApProcSvcDn": cfprApProcSvcDn,
       "cfprApProcSvcRn": cfprApProcSvcRn,
       "cfprApProcSvcId": cfprApProcSvcId,
       "cfprApProcSvcName": cfprApProcSvcName,
       "cfprApProcTxCountsTable": cfprApProcTxCountsTable,
       "cfprApProcTxCountsEntry": cfprApProcTxCountsEntry,
       "cfprApProcTxCountsInstanceId": cfprApProcTxCountsInstanceId,
       "cfprApProcTxCountsDn": cfprApProcTxCountsDn,
       "cfprApProcTxCountsRn": cfprApProcTxCountsRn,
       "cfprApProcTxCountsAdminState": cfprApProcTxCountsAdminState,
       "cfprApProcTxCountsBulked": cfprApProcTxCountsBulked,
       "cfprApProcTxCountsFailed": cfprApProcTxCountsFailed,
       "cfprApProcTxCountsRetried": cfprApProcTxCountsRetried,
       "cfprApProcTxCountsSingleton": cfprApProcTxCountsSingleton,
       "cfprApProcTxCountsSuccessfull": cfprApProcTxCountsSuccessfull,
       "cfprApProcTxCountsTotal": cfprApProcTxCountsTotal}
)
