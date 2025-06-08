# SNMP MIB module (CISCO-FIREPOWER-PROC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-PROC-MIB.mib
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

(CfprProcStatAdminState,) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprProcStatAdminState")

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

cfprProcObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprProcDoerTable_Object = MibTable
cfprProcDoerTable = _CfprProcDoerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 1)
)
if mibBuilder.loadTexts:
    cfprProcDoerTable.setStatus("current")
_CfprProcDoerEntry_Object = MibTableRow
cfprProcDoerEntry = _CfprProcDoerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 1, 1)
)
cfprProcDoerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROC-MIB", "cfprProcDoerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcDoerEntry.setStatus("current")
_CfprProcDoerInstanceId_Type = CfprManagedObjectId
_CfprProcDoerInstanceId_Object = MibTableColumn
cfprProcDoerInstanceId = _CfprProcDoerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 1, 1, 1),
    _CfprProcDoerInstanceId_Type()
)
cfprProcDoerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcDoerInstanceId.setStatus("current")
_CfprProcDoerDn_Type = CfprManagedObjectDn
_CfprProcDoerDn_Object = MibTableColumn
cfprProcDoerDn = _CfprProcDoerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 1, 1, 2),
    _CfprProcDoerDn_Type()
)
cfprProcDoerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcDoerDn.setStatus("current")
_CfprProcDoerRn_Type = SnmpAdminString
_CfprProcDoerRn_Object = MibTableColumn
cfprProcDoerRn = _CfprProcDoerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 1, 1, 3),
    _CfprProcDoerRn_Type()
)
cfprProcDoerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcDoerRn.setStatus("current")
_CfprProcDoerId_Type = Gauge32
_CfprProcDoerId_Object = MibTableColumn
cfprProcDoerId = _CfprProcDoerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 1, 1, 4),
    _CfprProcDoerId_Type()
)
cfprProcDoerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcDoerId.setStatus("current")
_CfprProcDoerName_Type = SnmpAdminString
_CfprProcDoerName_Object = MibTableColumn
cfprProcDoerName = _CfprProcDoerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 1, 1, 5),
    _CfprProcDoerName_Type()
)
cfprProcDoerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcDoerName.setStatus("current")
_CfprProcManagerTable_Object = MibTable
cfprProcManagerTable = _CfprProcManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 2)
)
if mibBuilder.loadTexts:
    cfprProcManagerTable.setStatus("current")
_CfprProcManagerEntry_Object = MibTableRow
cfprProcManagerEntry = _CfprProcManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 2, 1)
)
cfprProcManagerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROC-MIB", "cfprProcManagerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcManagerEntry.setStatus("current")
_CfprProcManagerInstanceId_Type = CfprManagedObjectId
_CfprProcManagerInstanceId_Object = MibTableColumn
cfprProcManagerInstanceId = _CfprProcManagerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 2, 1, 1),
    _CfprProcManagerInstanceId_Type()
)
cfprProcManagerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcManagerInstanceId.setStatus("current")
_CfprProcManagerDn_Type = CfprManagedObjectDn
_CfprProcManagerDn_Object = MibTableColumn
cfprProcManagerDn = _CfprProcManagerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 2, 1, 2),
    _CfprProcManagerDn_Type()
)
cfprProcManagerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcManagerDn.setStatus("current")
_CfprProcManagerRn_Type = SnmpAdminString
_CfprProcManagerRn_Object = MibTableColumn
cfprProcManagerRn = _CfprProcManagerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 2, 1, 3),
    _CfprProcManagerRn_Type()
)
cfprProcManagerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcManagerRn.setStatus("current")
_CfprProcPrtTable_Object = MibTable
cfprProcPrtTable = _CfprProcPrtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 3)
)
if mibBuilder.loadTexts:
    cfprProcPrtTable.setStatus("current")
_CfprProcPrtEntry_Object = MibTableRow
cfprProcPrtEntry = _CfprProcPrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 3, 1)
)
cfprProcPrtEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROC-MIB", "cfprProcPrtInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcPrtEntry.setStatus("current")
_CfprProcPrtInstanceId_Type = CfprManagedObjectId
_CfprProcPrtInstanceId_Object = MibTableColumn
cfprProcPrtInstanceId = _CfprProcPrtInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 3, 1, 1),
    _CfprProcPrtInstanceId_Type()
)
cfprProcPrtInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcPrtInstanceId.setStatus("current")
_CfprProcPrtDn_Type = CfprManagedObjectDn
_CfprProcPrtDn_Object = MibTableColumn
cfprProcPrtDn = _CfprProcPrtDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 3, 1, 2),
    _CfprProcPrtDn_Type()
)
cfprProcPrtDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtDn.setStatus("current")
_CfprProcPrtRn_Type = SnmpAdminString
_CfprProcPrtRn_Object = MibTableColumn
cfprProcPrtRn = _CfprProcPrtRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 3, 1, 3),
    _CfprProcPrtRn_Type()
)
cfprProcPrtRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtRn.setStatus("current")
_CfprProcPrtId_Type = Gauge32
_CfprProcPrtId_Object = MibTableColumn
cfprProcPrtId = _CfprProcPrtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 3, 1, 4),
    _CfprProcPrtId_Type()
)
cfprProcPrtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtId.setStatus("current")
_CfprProcPrtName_Type = SnmpAdminString
_CfprProcPrtName_Object = MibTableColumn
cfprProcPrtName = _CfprProcPrtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 3, 1, 5),
    _CfprProcPrtName_Type()
)
cfprProcPrtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtName.setStatus("current")
_CfprProcPrtCountsTable_Object = MibTable
cfprProcPrtCountsTable = _CfprProcPrtCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4)
)
if mibBuilder.loadTexts:
    cfprProcPrtCountsTable.setStatus("current")
_CfprProcPrtCountsEntry_Object = MibTableRow
cfprProcPrtCountsEntry = _CfprProcPrtCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1)
)
cfprProcPrtCountsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROC-MIB", "cfprProcPrtCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcPrtCountsEntry.setStatus("current")
_CfprProcPrtCountsInstanceId_Type = CfprManagedObjectId
_CfprProcPrtCountsInstanceId_Object = MibTableColumn
cfprProcPrtCountsInstanceId = _CfprProcPrtCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1, 1),
    _CfprProcPrtCountsInstanceId_Type()
)
cfprProcPrtCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcPrtCountsInstanceId.setStatus("current")
_CfprProcPrtCountsDn_Type = CfprManagedObjectDn
_CfprProcPrtCountsDn_Object = MibTableColumn
cfprProcPrtCountsDn = _CfprProcPrtCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1, 2),
    _CfprProcPrtCountsDn_Type()
)
cfprProcPrtCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtCountsDn.setStatus("current")
_CfprProcPrtCountsRn_Type = SnmpAdminString
_CfprProcPrtCountsRn_Object = MibTableColumn
cfprProcPrtCountsRn = _CfprProcPrtCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1, 3),
    _CfprProcPrtCountsRn_Type()
)
cfprProcPrtCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtCountsRn.setStatus("current")
_CfprProcPrtCountsCachenospc_Type = Gauge32
_CfprProcPrtCountsCachenospc_Object = MibTableColumn
cfprProcPrtCountsCachenospc = _CfprProcPrtCountsCachenospc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1, 4),
    _CfprProcPrtCountsCachenospc_Type()
)
cfprProcPrtCountsCachenospc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtCountsCachenospc.setStatus("current")
_CfprProcPrtCountsDbtxs_Type = Gauge32
_CfprProcPrtCountsDbtxs_Object = MibTableColumn
cfprProcPrtCountsDbtxs = _CfprProcPrtCountsDbtxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1, 5),
    _CfprProcPrtCountsDbtxs_Type()
)
cfprProcPrtCountsDbtxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtCountsDbtxs.setStatus("current")
_CfprProcPrtCountsLargetxs_Type = Gauge32
_CfprProcPrtCountsLargetxs_Object = MibTableColumn
cfprProcPrtCountsLargetxs = _CfprProcPrtCountsLargetxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1, 6),
    _CfprProcPrtCountsLargetxs_Type()
)
cfprProcPrtCountsLargetxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtCountsLargetxs.setStatus("current")
_CfprProcPrtCountsPersistTime_Type = Unsigned64
_CfprProcPrtCountsPersistTime_Object = MibTableColumn
cfprProcPrtCountsPersistTime = _CfprProcPrtCountsPersistTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1, 7),
    _CfprProcPrtCountsPersistTime_Type()
)
cfprProcPrtCountsPersistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtCountsPersistTime.setStatus("current")
_CfprProcPrtCountsTotal_Type = Gauge32
_CfprProcPrtCountsTotal_Object = MibTableColumn
cfprProcPrtCountsTotal = _CfprProcPrtCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 4, 1, 8),
    _CfprProcPrtCountsTotal_Type()
)
cfprProcPrtCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcPrtCountsTotal.setStatus("current")
_CfprProcStimulusCountsTable_Object = MibTable
cfprProcStimulusCountsTable = _CfprProcStimulusCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5)
)
if mibBuilder.loadTexts:
    cfprProcStimulusCountsTable.setStatus("current")
_CfprProcStimulusCountsEntry_Object = MibTableRow
cfprProcStimulusCountsEntry = _CfprProcStimulusCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1)
)
cfprProcStimulusCountsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROC-MIB", "cfprProcStimulusCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcStimulusCountsEntry.setStatus("current")
_CfprProcStimulusCountsInstanceId_Type = CfprManagedObjectId
_CfprProcStimulusCountsInstanceId_Object = MibTableColumn
cfprProcStimulusCountsInstanceId = _CfprProcStimulusCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 1),
    _CfprProcStimulusCountsInstanceId_Type()
)
cfprProcStimulusCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsInstanceId.setStatus("current")
_CfprProcStimulusCountsDn_Type = CfprManagedObjectDn
_CfprProcStimulusCountsDn_Object = MibTableColumn
cfprProcStimulusCountsDn = _CfprProcStimulusCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 2),
    _CfprProcStimulusCountsDn_Type()
)
cfprProcStimulusCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsDn.setStatus("current")
_CfprProcStimulusCountsRn_Type = SnmpAdminString
_CfprProcStimulusCountsRn_Object = MibTableColumn
cfprProcStimulusCountsRn = _CfprProcStimulusCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 3),
    _CfprProcStimulusCountsRn_Type()
)
cfprProcStimulusCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsRn.setStatus("current")
_CfprProcStimulusCountsAdminState_Type = CfprProcStatAdminState
_CfprProcStimulusCountsAdminState_Object = MibTableColumn
cfprProcStimulusCountsAdminState = _CfprProcStimulusCountsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 4),
    _CfprProcStimulusCountsAdminState_Type()
)
cfprProcStimulusCountsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsAdminState.setStatus("current")
_CfprProcStimulusCountsBulked_Type = Gauge32
_CfprProcStimulusCountsBulked_Object = MibTableColumn
cfprProcStimulusCountsBulked = _CfprProcStimulusCountsBulked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 5),
    _CfprProcStimulusCountsBulked_Type()
)
cfprProcStimulusCountsBulked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsBulked.setStatus("current")
_CfprProcStimulusCountsFailed_Type = Gauge32
_CfprProcStimulusCountsFailed_Object = MibTableColumn
cfprProcStimulusCountsFailed = _CfprProcStimulusCountsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 6),
    _CfprProcStimulusCountsFailed_Type()
)
cfprProcStimulusCountsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsFailed.setStatus("current")
_CfprProcStimulusCountsRetried_Type = Gauge32
_CfprProcStimulusCountsRetried_Object = MibTableColumn
cfprProcStimulusCountsRetried = _CfprProcStimulusCountsRetried_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 7),
    _CfprProcStimulusCountsRetried_Type()
)
cfprProcStimulusCountsRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsRetried.setStatus("current")
_CfprProcStimulusCountsSingleton_Type = Gauge32
_CfprProcStimulusCountsSingleton_Object = MibTableColumn
cfprProcStimulusCountsSingleton = _CfprProcStimulusCountsSingleton_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 8),
    _CfprProcStimulusCountsSingleton_Type()
)
cfprProcStimulusCountsSingleton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsSingleton.setStatus("current")
_CfprProcStimulusCountsSuccessfull_Type = Gauge32
_CfprProcStimulusCountsSuccessfull_Object = MibTableColumn
cfprProcStimulusCountsSuccessfull = _CfprProcStimulusCountsSuccessfull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 9),
    _CfprProcStimulusCountsSuccessfull_Type()
)
cfprProcStimulusCountsSuccessfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsSuccessfull.setStatus("current")
_CfprProcStimulusCountsTotal_Type = Gauge32
_CfprProcStimulusCountsTotal_Object = MibTableColumn
cfprProcStimulusCountsTotal = _CfprProcStimulusCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 5, 1, 10),
    _CfprProcStimulusCountsTotal_Type()
)
cfprProcStimulusCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcStimulusCountsTotal.setStatus("current")
_CfprProcSvcTable_Object = MibTable
cfprProcSvcTable = _CfprProcSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 6)
)
if mibBuilder.loadTexts:
    cfprProcSvcTable.setStatus("current")
_CfprProcSvcEntry_Object = MibTableRow
cfprProcSvcEntry = _CfprProcSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 6, 1)
)
cfprProcSvcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROC-MIB", "cfprProcSvcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcSvcEntry.setStatus("current")
_CfprProcSvcInstanceId_Type = CfprManagedObjectId
_CfprProcSvcInstanceId_Object = MibTableColumn
cfprProcSvcInstanceId = _CfprProcSvcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 6, 1, 1),
    _CfprProcSvcInstanceId_Type()
)
cfprProcSvcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcSvcInstanceId.setStatus("current")
_CfprProcSvcDn_Type = CfprManagedObjectDn
_CfprProcSvcDn_Object = MibTableColumn
cfprProcSvcDn = _CfprProcSvcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 6, 1, 2),
    _CfprProcSvcDn_Type()
)
cfprProcSvcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcSvcDn.setStatus("current")
_CfprProcSvcRn_Type = SnmpAdminString
_CfprProcSvcRn_Object = MibTableColumn
cfprProcSvcRn = _CfprProcSvcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 6, 1, 3),
    _CfprProcSvcRn_Type()
)
cfprProcSvcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcSvcRn.setStatus("current")
_CfprProcSvcId_Type = Gauge32
_CfprProcSvcId_Object = MibTableColumn
cfprProcSvcId = _CfprProcSvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 6, 1, 4),
    _CfprProcSvcId_Type()
)
cfprProcSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcSvcId.setStatus("current")
_CfprProcSvcName_Type = SnmpAdminString
_CfprProcSvcName_Object = MibTableColumn
cfprProcSvcName = _CfprProcSvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 6, 1, 5),
    _CfprProcSvcName_Type()
)
cfprProcSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcSvcName.setStatus("current")
_CfprProcTxCountsTable_Object = MibTable
cfprProcTxCountsTable = _CfprProcTxCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7)
)
if mibBuilder.loadTexts:
    cfprProcTxCountsTable.setStatus("current")
_CfprProcTxCountsEntry_Object = MibTableRow
cfprProcTxCountsEntry = _CfprProcTxCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1)
)
cfprProcTxCountsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PROC-MIB", "cfprProcTxCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprProcTxCountsEntry.setStatus("current")
_CfprProcTxCountsInstanceId_Type = CfprManagedObjectId
_CfprProcTxCountsInstanceId_Object = MibTableColumn
cfprProcTxCountsInstanceId = _CfprProcTxCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 1),
    _CfprProcTxCountsInstanceId_Type()
)
cfprProcTxCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprProcTxCountsInstanceId.setStatus("current")
_CfprProcTxCountsDn_Type = CfprManagedObjectDn
_CfprProcTxCountsDn_Object = MibTableColumn
cfprProcTxCountsDn = _CfprProcTxCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 2),
    _CfprProcTxCountsDn_Type()
)
cfprProcTxCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsDn.setStatus("current")
_CfprProcTxCountsRn_Type = SnmpAdminString
_CfprProcTxCountsRn_Object = MibTableColumn
cfprProcTxCountsRn = _CfprProcTxCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 3),
    _CfprProcTxCountsRn_Type()
)
cfprProcTxCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsRn.setStatus("current")
_CfprProcTxCountsAdminState_Type = CfprProcStatAdminState
_CfprProcTxCountsAdminState_Object = MibTableColumn
cfprProcTxCountsAdminState = _CfprProcTxCountsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 4),
    _CfprProcTxCountsAdminState_Type()
)
cfprProcTxCountsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsAdminState.setStatus("current")
_CfprProcTxCountsBulked_Type = Gauge32
_CfprProcTxCountsBulked_Object = MibTableColumn
cfprProcTxCountsBulked = _CfprProcTxCountsBulked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 5),
    _CfprProcTxCountsBulked_Type()
)
cfprProcTxCountsBulked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsBulked.setStatus("current")
_CfprProcTxCountsFailed_Type = Gauge32
_CfprProcTxCountsFailed_Object = MibTableColumn
cfprProcTxCountsFailed = _CfprProcTxCountsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 6),
    _CfprProcTxCountsFailed_Type()
)
cfprProcTxCountsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsFailed.setStatus("current")
_CfprProcTxCountsRetried_Type = Gauge32
_CfprProcTxCountsRetried_Object = MibTableColumn
cfprProcTxCountsRetried = _CfprProcTxCountsRetried_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 7),
    _CfprProcTxCountsRetried_Type()
)
cfprProcTxCountsRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsRetried.setStatus("current")
_CfprProcTxCountsSingleton_Type = Gauge32
_CfprProcTxCountsSingleton_Object = MibTableColumn
cfprProcTxCountsSingleton = _CfprProcTxCountsSingleton_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 8),
    _CfprProcTxCountsSingleton_Type()
)
cfprProcTxCountsSingleton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsSingleton.setStatus("current")
_CfprProcTxCountsSuccessfull_Type = Gauge32
_CfprProcTxCountsSuccessfull_Object = MibTableColumn
cfprProcTxCountsSuccessfull = _CfprProcTxCountsSuccessfull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 9),
    _CfprProcTxCountsSuccessfull_Type()
)
cfprProcTxCountsSuccessfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsSuccessfull.setStatus("current")
_CfprProcTxCountsTotal_Type = Gauge32
_CfprProcTxCountsTotal_Object = MibTableColumn
cfprProcTxCountsTotal = _CfprProcTxCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 65, 7, 1, 10),
    _CfprProcTxCountsTotal_Type()
)
cfprProcTxCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprProcTxCountsTotal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-PROC-MIB",
    **{"cfprProcObjects": cfprProcObjects,
       "cfprProcDoerTable": cfprProcDoerTable,
       "cfprProcDoerEntry": cfprProcDoerEntry,
       "cfprProcDoerInstanceId": cfprProcDoerInstanceId,
       "cfprProcDoerDn": cfprProcDoerDn,
       "cfprProcDoerRn": cfprProcDoerRn,
       "cfprProcDoerId": cfprProcDoerId,
       "cfprProcDoerName": cfprProcDoerName,
       "cfprProcManagerTable": cfprProcManagerTable,
       "cfprProcManagerEntry": cfprProcManagerEntry,
       "cfprProcManagerInstanceId": cfprProcManagerInstanceId,
       "cfprProcManagerDn": cfprProcManagerDn,
       "cfprProcManagerRn": cfprProcManagerRn,
       "cfprProcPrtTable": cfprProcPrtTable,
       "cfprProcPrtEntry": cfprProcPrtEntry,
       "cfprProcPrtInstanceId": cfprProcPrtInstanceId,
       "cfprProcPrtDn": cfprProcPrtDn,
       "cfprProcPrtRn": cfprProcPrtRn,
       "cfprProcPrtId": cfprProcPrtId,
       "cfprProcPrtName": cfprProcPrtName,
       "cfprProcPrtCountsTable": cfprProcPrtCountsTable,
       "cfprProcPrtCountsEntry": cfprProcPrtCountsEntry,
       "cfprProcPrtCountsInstanceId": cfprProcPrtCountsInstanceId,
       "cfprProcPrtCountsDn": cfprProcPrtCountsDn,
       "cfprProcPrtCountsRn": cfprProcPrtCountsRn,
       "cfprProcPrtCountsCachenospc": cfprProcPrtCountsCachenospc,
       "cfprProcPrtCountsDbtxs": cfprProcPrtCountsDbtxs,
       "cfprProcPrtCountsLargetxs": cfprProcPrtCountsLargetxs,
       "cfprProcPrtCountsPersistTime": cfprProcPrtCountsPersistTime,
       "cfprProcPrtCountsTotal": cfprProcPrtCountsTotal,
       "cfprProcStimulusCountsTable": cfprProcStimulusCountsTable,
       "cfprProcStimulusCountsEntry": cfprProcStimulusCountsEntry,
       "cfprProcStimulusCountsInstanceId": cfprProcStimulusCountsInstanceId,
       "cfprProcStimulusCountsDn": cfprProcStimulusCountsDn,
       "cfprProcStimulusCountsRn": cfprProcStimulusCountsRn,
       "cfprProcStimulusCountsAdminState": cfprProcStimulusCountsAdminState,
       "cfprProcStimulusCountsBulked": cfprProcStimulusCountsBulked,
       "cfprProcStimulusCountsFailed": cfprProcStimulusCountsFailed,
       "cfprProcStimulusCountsRetried": cfprProcStimulusCountsRetried,
       "cfprProcStimulusCountsSingleton": cfprProcStimulusCountsSingleton,
       "cfprProcStimulusCountsSuccessfull": cfprProcStimulusCountsSuccessfull,
       "cfprProcStimulusCountsTotal": cfprProcStimulusCountsTotal,
       "cfprProcSvcTable": cfprProcSvcTable,
       "cfprProcSvcEntry": cfprProcSvcEntry,
       "cfprProcSvcInstanceId": cfprProcSvcInstanceId,
       "cfprProcSvcDn": cfprProcSvcDn,
       "cfprProcSvcRn": cfprProcSvcRn,
       "cfprProcSvcId": cfprProcSvcId,
       "cfprProcSvcName": cfprProcSvcName,
       "cfprProcTxCountsTable": cfprProcTxCountsTable,
       "cfprProcTxCountsEntry": cfprProcTxCountsEntry,
       "cfprProcTxCountsInstanceId": cfprProcTxCountsInstanceId,
       "cfprProcTxCountsDn": cfprProcTxCountsDn,
       "cfprProcTxCountsRn": cfprProcTxCountsRn,
       "cfprProcTxCountsAdminState": cfprProcTxCountsAdminState,
       "cfprProcTxCountsBulked": cfprProcTxCountsBulked,
       "cfprProcTxCountsFailed": cfprProcTxCountsFailed,
       "cfprProcTxCountsRetried": cfprProcTxCountsRetried,
       "cfprProcTxCountsSingleton": cfprProcTxCountsSingleton,
       "cfprProcTxCountsSuccessfull": cfprProcTxCountsSuccessfull,
       "cfprProcTxCountsTotal": cfprProcTxCountsTotal}
)
