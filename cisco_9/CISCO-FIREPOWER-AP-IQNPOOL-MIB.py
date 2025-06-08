# SNMP MIB module (CISCO-FIREPOWER-AP-IQNPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-IQNPOOL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:53 2025
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

(CfprApIqnpoolBlockFrom,
 CfprApIqnpoolBlockTo,
 CfprApIqnpoolPoolAssignmentOrder,
 CfprApIqnpoolTransportBlockFrom,
 CfprApIqnpoolTransportBlockTo,
 CfprApPolicyPolicyOwner,
 CfprApPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApIqnpoolBlockFrom",
    "CfprApIqnpoolBlockTo",
    "CfprApIqnpoolPoolAssignmentOrder",
    "CfprApIqnpoolTransportBlockFrom",
    "CfprApIqnpoolTransportBlockTo",
    "CfprApPolicyPolicyOwner",
    "CfprApPoolElementOwner")

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

cfprApIqnpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApIqnpoolAddrTable_Object = MibTable
cfprApIqnpoolAddrTable = _CfprApIqnpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1)
)
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrTable.setStatus("current")
_CfprApIqnpoolAddrEntry_Object = MibTableRow
cfprApIqnpoolAddrEntry = _CfprApIqnpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1)
)
cfprApIqnpoolAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IQNPOOL-MIB", "cfprApIqnpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrEntry.setStatus("current")
_CfprApIqnpoolAddrInstanceId_Type = CfprApManagedObjectId
_CfprApIqnpoolAddrInstanceId_Object = MibTableColumn
cfprApIqnpoolAddrInstanceId = _CfprApIqnpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 1),
    _CfprApIqnpoolAddrInstanceId_Type()
)
cfprApIqnpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrInstanceId.setStatus("current")
_CfprApIqnpoolAddrDn_Type = CfprApManagedObjectDn
_CfprApIqnpoolAddrDn_Object = MibTableColumn
cfprApIqnpoolAddrDn = _CfprApIqnpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 2),
    _CfprApIqnpoolAddrDn_Type()
)
cfprApIqnpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrDn.setStatus("current")
_CfprApIqnpoolAddrRn_Type = SnmpAdminString
_CfprApIqnpoolAddrRn_Object = MibTableColumn
cfprApIqnpoolAddrRn = _CfprApIqnpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 3),
    _CfprApIqnpoolAddrRn_Type()
)
cfprApIqnpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrRn.setStatus("current")
_CfprApIqnpoolAddrAssigned_Type = TruthValue
_CfprApIqnpoolAddrAssigned_Object = MibTableColumn
cfprApIqnpoolAddrAssigned = _CfprApIqnpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 4),
    _CfprApIqnpoolAddrAssigned_Type()
)
cfprApIqnpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrAssigned.setStatus("current")
_CfprApIqnpoolAddrAssignedToDn_Type = SnmpAdminString
_CfprApIqnpoolAddrAssignedToDn_Object = MibTableColumn
cfprApIqnpoolAddrAssignedToDn = _CfprApIqnpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 5),
    _CfprApIqnpoolAddrAssignedToDn_Type()
)
cfprApIqnpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrAssignedToDn.setStatus("current")
_CfprApIqnpoolAddrGlobalAssignedCnt_Type = Gauge32
_CfprApIqnpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cfprApIqnpoolAddrGlobalAssignedCnt = _CfprApIqnpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 6),
    _CfprApIqnpoolAddrGlobalAssignedCnt_Type()
)
cfprApIqnpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrGlobalAssignedCnt.setStatus("current")
_CfprApIqnpoolAddrGlobalDefinedCnt_Type = Gauge32
_CfprApIqnpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cfprApIqnpoolAddrGlobalDefinedCnt = _CfprApIqnpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 7),
    _CfprApIqnpoolAddrGlobalDefinedCnt_Type()
)
cfprApIqnpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrGlobalDefinedCnt.setStatus("current")
_CfprApIqnpoolAddrName_Type = SnmpAdminString
_CfprApIqnpoolAddrName_Object = MibTableColumn
cfprApIqnpoolAddrName = _CfprApIqnpoolAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 8),
    _CfprApIqnpoolAddrName_Type()
)
cfprApIqnpoolAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrName.setStatus("current")
_CfprApIqnpoolAddrOwner_Type = CfprApPoolElementOwner
_CfprApIqnpoolAddrOwner_Object = MibTableColumn
cfprApIqnpoolAddrOwner = _CfprApIqnpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 1, 1, 9),
    _CfprApIqnpoolAddrOwner_Type()
)
cfprApIqnpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolAddrOwner.setStatus("current")
_CfprApIqnpoolBlockTable_Object = MibTable
cfprApIqnpoolBlockTable = _CfprApIqnpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 2)
)
if mibBuilder.loadTexts:
    cfprApIqnpoolBlockTable.setStatus("current")
_CfprApIqnpoolBlockEntry_Object = MibTableRow
cfprApIqnpoolBlockEntry = _CfprApIqnpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 2, 1)
)
cfprApIqnpoolBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IQNPOOL-MIB", "cfprApIqnpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIqnpoolBlockEntry.setStatus("current")
_CfprApIqnpoolBlockInstanceId_Type = CfprApManagedObjectId
_CfprApIqnpoolBlockInstanceId_Object = MibTableColumn
cfprApIqnpoolBlockInstanceId = _CfprApIqnpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 2, 1, 1),
    _CfprApIqnpoolBlockInstanceId_Type()
)
cfprApIqnpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIqnpoolBlockInstanceId.setStatus("current")
_CfprApIqnpoolBlockDn_Type = CfprApManagedObjectDn
_CfprApIqnpoolBlockDn_Object = MibTableColumn
cfprApIqnpoolBlockDn = _CfprApIqnpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 2, 1, 2),
    _CfprApIqnpoolBlockDn_Type()
)
cfprApIqnpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolBlockDn.setStatus("current")
_CfprApIqnpoolBlockRn_Type = SnmpAdminString
_CfprApIqnpoolBlockRn_Object = MibTableColumn
cfprApIqnpoolBlockRn = _CfprApIqnpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 2, 1, 3),
    _CfprApIqnpoolBlockRn_Type()
)
cfprApIqnpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolBlockRn.setStatus("current")
_CfprApIqnpoolBlockFrom_Type = CfprApIqnpoolBlockFrom
_CfprApIqnpoolBlockFrom_Object = MibTableColumn
cfprApIqnpoolBlockFrom = _CfprApIqnpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 2, 1, 4),
    _CfprApIqnpoolBlockFrom_Type()
)
cfprApIqnpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolBlockFrom.setStatus("current")
_CfprApIqnpoolBlockSuffix_Type = SnmpAdminString
_CfprApIqnpoolBlockSuffix_Object = MibTableColumn
cfprApIqnpoolBlockSuffix = _CfprApIqnpoolBlockSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 2, 1, 5),
    _CfprApIqnpoolBlockSuffix_Type()
)
cfprApIqnpoolBlockSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolBlockSuffix.setStatus("current")
_CfprApIqnpoolBlockTo_Type = CfprApIqnpoolBlockTo
_CfprApIqnpoolBlockTo_Object = MibTableColumn
cfprApIqnpoolBlockTo = _CfprApIqnpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 2, 1, 6),
    _CfprApIqnpoolBlockTo_Type()
)
cfprApIqnpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolBlockTo.setStatus("current")
_CfprApIqnpoolFormatTable_Object = MibTable
cfprApIqnpoolFormatTable = _CfprApIqnpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 3)
)
if mibBuilder.loadTexts:
    cfprApIqnpoolFormatTable.setStatus("current")
_CfprApIqnpoolFormatEntry_Object = MibTableRow
cfprApIqnpoolFormatEntry = _CfprApIqnpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 3, 1)
)
cfprApIqnpoolFormatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IQNPOOL-MIB", "cfprApIqnpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIqnpoolFormatEntry.setStatus("current")
_CfprApIqnpoolFormatInstanceId_Type = CfprApManagedObjectId
_CfprApIqnpoolFormatInstanceId_Object = MibTableColumn
cfprApIqnpoolFormatInstanceId = _CfprApIqnpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 3, 1, 1),
    _CfprApIqnpoolFormatInstanceId_Type()
)
cfprApIqnpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIqnpoolFormatInstanceId.setStatus("current")
_CfprApIqnpoolFormatDn_Type = CfprApManagedObjectDn
_CfprApIqnpoolFormatDn_Object = MibTableColumn
cfprApIqnpoolFormatDn = _CfprApIqnpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 3, 1, 2),
    _CfprApIqnpoolFormatDn_Type()
)
cfprApIqnpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolFormatDn.setStatus("current")
_CfprApIqnpoolFormatRn_Type = SnmpAdminString
_CfprApIqnpoolFormatRn_Object = MibTableColumn
cfprApIqnpoolFormatRn = _CfprApIqnpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 3, 1, 3),
    _CfprApIqnpoolFormatRn_Type()
)
cfprApIqnpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolFormatRn.setStatus("current")
_CfprApIqnpoolFormatFormat_Type = SnmpAdminString
_CfprApIqnpoolFormatFormat_Object = MibTableColumn
cfprApIqnpoolFormatFormat = _CfprApIqnpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 3, 1, 4),
    _CfprApIqnpoolFormatFormat_Type()
)
cfprApIqnpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolFormatFormat.setStatus("current")
_CfprApIqnpoolPoolTable_Object = MibTable
cfprApIqnpoolPoolTable = _CfprApIqnpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4)
)
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolTable.setStatus("current")
_CfprApIqnpoolPoolEntry_Object = MibTableRow
cfprApIqnpoolPoolEntry = _CfprApIqnpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1)
)
cfprApIqnpoolPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IQNPOOL-MIB", "cfprApIqnpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolEntry.setStatus("current")
_CfprApIqnpoolPoolInstanceId_Type = CfprApManagedObjectId
_CfprApIqnpoolPoolInstanceId_Object = MibTableColumn
cfprApIqnpoolPoolInstanceId = _CfprApIqnpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 1),
    _CfprApIqnpoolPoolInstanceId_Type()
)
cfprApIqnpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolInstanceId.setStatus("current")
_CfprApIqnpoolPoolDn_Type = CfprApManagedObjectDn
_CfprApIqnpoolPoolDn_Object = MibTableColumn
cfprApIqnpoolPoolDn = _CfprApIqnpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 2),
    _CfprApIqnpoolPoolDn_Type()
)
cfprApIqnpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolDn.setStatus("current")
_CfprApIqnpoolPoolRn_Type = SnmpAdminString
_CfprApIqnpoolPoolRn_Object = MibTableColumn
cfprApIqnpoolPoolRn = _CfprApIqnpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 3),
    _CfprApIqnpoolPoolRn_Type()
)
cfprApIqnpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolRn.setStatus("current")
_CfprApIqnpoolPoolAssigned_Type = Gauge32
_CfprApIqnpoolPoolAssigned_Object = MibTableColumn
cfprApIqnpoolPoolAssigned = _CfprApIqnpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 4),
    _CfprApIqnpoolPoolAssigned_Type()
)
cfprApIqnpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolAssigned.setStatus("current")
_CfprApIqnpoolPoolAssignmentOrder_Type = CfprApIqnpoolPoolAssignmentOrder
_CfprApIqnpoolPoolAssignmentOrder_Object = MibTableColumn
cfprApIqnpoolPoolAssignmentOrder = _CfprApIqnpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 5),
    _CfprApIqnpoolPoolAssignmentOrder_Type()
)
cfprApIqnpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolAssignmentOrder.setStatus("current")
_CfprApIqnpoolPoolDescr_Type = SnmpAdminString
_CfprApIqnpoolPoolDescr_Object = MibTableColumn
cfprApIqnpoolPoolDescr = _CfprApIqnpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 6),
    _CfprApIqnpoolPoolDescr_Type()
)
cfprApIqnpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolDescr.setStatus("current")
_CfprApIqnpoolPoolIntId_Type = SnmpAdminString
_CfprApIqnpoolPoolIntId_Object = MibTableColumn
cfprApIqnpoolPoolIntId = _CfprApIqnpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 7),
    _CfprApIqnpoolPoolIntId_Type()
)
cfprApIqnpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolIntId.setStatus("current")
_CfprApIqnpoolPoolName_Type = SnmpAdminString
_CfprApIqnpoolPoolName_Object = MibTableColumn
cfprApIqnpoolPoolName = _CfprApIqnpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 8),
    _CfprApIqnpoolPoolName_Type()
)
cfprApIqnpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolName.setStatus("current")
_CfprApIqnpoolPoolPolicyLevel_Type = Gauge32
_CfprApIqnpoolPoolPolicyLevel_Object = MibTableColumn
cfprApIqnpoolPoolPolicyLevel = _CfprApIqnpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 9),
    _CfprApIqnpoolPoolPolicyLevel_Type()
)
cfprApIqnpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolPolicyLevel.setStatus("current")
_CfprApIqnpoolPoolPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApIqnpoolPoolPolicyOwner_Object = MibTableColumn
cfprApIqnpoolPoolPolicyOwner = _CfprApIqnpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 10),
    _CfprApIqnpoolPoolPolicyOwner_Type()
)
cfprApIqnpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolPolicyOwner.setStatus("current")
_CfprApIqnpoolPoolPrefix_Type = SnmpAdminString
_CfprApIqnpoolPoolPrefix_Object = MibTableColumn
cfprApIqnpoolPoolPrefix = _CfprApIqnpoolPoolPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 11),
    _CfprApIqnpoolPoolPrefix_Type()
)
cfprApIqnpoolPoolPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolPrefix.setStatus("current")
_CfprApIqnpoolPoolSize_Type = Gauge32
_CfprApIqnpoolPoolSize_Object = MibTableColumn
cfprApIqnpoolPoolSize = _CfprApIqnpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 4, 1, 12),
    _CfprApIqnpoolPoolSize_Type()
)
cfprApIqnpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolSize.setStatus("current")
_CfprApIqnpoolPoolableTable_Object = MibTable
cfprApIqnpoolPoolableTable = _CfprApIqnpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 5)
)
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolableTable.setStatus("current")
_CfprApIqnpoolPoolableEntry_Object = MibTableRow
cfprApIqnpoolPoolableEntry = _CfprApIqnpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 5, 1)
)
cfprApIqnpoolPoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IQNPOOL-MIB", "cfprApIqnpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolableEntry.setStatus("current")
_CfprApIqnpoolPoolableInstanceId_Type = CfprApManagedObjectId
_CfprApIqnpoolPoolableInstanceId_Object = MibTableColumn
cfprApIqnpoolPoolableInstanceId = _CfprApIqnpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 5, 1, 1),
    _CfprApIqnpoolPoolableInstanceId_Type()
)
cfprApIqnpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolableInstanceId.setStatus("current")
_CfprApIqnpoolPoolableDn_Type = CfprApManagedObjectDn
_CfprApIqnpoolPoolableDn_Object = MibTableColumn
cfprApIqnpoolPoolableDn = _CfprApIqnpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 5, 1, 2),
    _CfprApIqnpoolPoolableDn_Type()
)
cfprApIqnpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolableDn.setStatus("current")
_CfprApIqnpoolPoolableRn_Type = SnmpAdminString
_CfprApIqnpoolPoolableRn_Object = MibTableColumn
cfprApIqnpoolPoolableRn = _CfprApIqnpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 5, 1, 3),
    _CfprApIqnpoolPoolableRn_Type()
)
cfprApIqnpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolableRn.setStatus("current")
_CfprApIqnpoolPoolableId_Type = Unsigned64
_CfprApIqnpoolPoolableId_Object = MibTableColumn
cfprApIqnpoolPoolableId = _CfprApIqnpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 5, 1, 4),
    _CfprApIqnpoolPoolableId_Type()
)
cfprApIqnpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolableId.setStatus("current")
_CfprApIqnpoolPoolablePoolDn_Type = SnmpAdminString
_CfprApIqnpoolPoolablePoolDn_Object = MibTableColumn
cfprApIqnpoolPoolablePoolDn = _CfprApIqnpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 5, 1, 5),
    _CfprApIqnpoolPoolablePoolDn_Type()
)
cfprApIqnpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPoolablePoolDn.setStatus("current")
_CfprApIqnpoolPooledTable_Object = MibTable
cfprApIqnpoolPooledTable = _CfprApIqnpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6)
)
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledTable.setStatus("current")
_CfprApIqnpoolPooledEntry_Object = MibTableRow
cfprApIqnpoolPooledEntry = _CfprApIqnpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1)
)
cfprApIqnpoolPooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IQNPOOL-MIB", "cfprApIqnpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledEntry.setStatus("current")
_CfprApIqnpoolPooledInstanceId_Type = CfprApManagedObjectId
_CfprApIqnpoolPooledInstanceId_Object = MibTableColumn
cfprApIqnpoolPooledInstanceId = _CfprApIqnpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1, 1),
    _CfprApIqnpoolPooledInstanceId_Type()
)
cfprApIqnpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledInstanceId.setStatus("current")
_CfprApIqnpoolPooledDn_Type = CfprApManagedObjectDn
_CfprApIqnpoolPooledDn_Object = MibTableColumn
cfprApIqnpoolPooledDn = _CfprApIqnpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1, 2),
    _CfprApIqnpoolPooledDn_Type()
)
cfprApIqnpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledDn.setStatus("current")
_CfprApIqnpoolPooledRn_Type = SnmpAdminString
_CfprApIqnpoolPooledRn_Object = MibTableColumn
cfprApIqnpoolPooledRn = _CfprApIqnpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1, 3),
    _CfprApIqnpoolPooledRn_Type()
)
cfprApIqnpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledRn.setStatus("current")
_CfprApIqnpoolPooledAssigned_Type = TruthValue
_CfprApIqnpoolPooledAssigned_Object = MibTableColumn
cfprApIqnpoolPooledAssigned = _CfprApIqnpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1, 4),
    _CfprApIqnpoolPooledAssigned_Type()
)
cfprApIqnpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledAssigned.setStatus("current")
_CfprApIqnpoolPooledAssignedToDn_Type = SnmpAdminString
_CfprApIqnpoolPooledAssignedToDn_Object = MibTableColumn
cfprApIqnpoolPooledAssignedToDn = _CfprApIqnpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1, 5),
    _CfprApIqnpoolPooledAssignedToDn_Type()
)
cfprApIqnpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledAssignedToDn.setStatus("current")
_CfprApIqnpoolPooledName_Type = SnmpAdminString
_CfprApIqnpoolPooledName_Object = MibTableColumn
cfprApIqnpoolPooledName = _CfprApIqnpoolPooledName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1, 6),
    _CfprApIqnpoolPooledName_Type()
)
cfprApIqnpoolPooledName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledName.setStatus("current")
_CfprApIqnpoolPooledPoolableDn_Type = SnmpAdminString
_CfprApIqnpoolPooledPoolableDn_Object = MibTableColumn
cfprApIqnpoolPooledPoolableDn = _CfprApIqnpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1, 7),
    _CfprApIqnpoolPooledPoolableDn_Type()
)
cfprApIqnpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledPoolableDn.setStatus("current")
_CfprApIqnpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CfprApIqnpoolPooledPrevAssignedToDn_Object = MibTableColumn
cfprApIqnpoolPooledPrevAssignedToDn = _CfprApIqnpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 6, 1, 8),
    _CfprApIqnpoolPooledPrevAssignedToDn_Type()
)
cfprApIqnpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolPooledPrevAssignedToDn.setStatus("current")
_CfprApIqnpoolTransportBlockTable_Object = MibTable
cfprApIqnpoolTransportBlockTable = _CfprApIqnpoolTransportBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 7)
)
if mibBuilder.loadTexts:
    cfprApIqnpoolTransportBlockTable.setStatus("current")
_CfprApIqnpoolTransportBlockEntry_Object = MibTableRow
cfprApIqnpoolTransportBlockEntry = _CfprApIqnpoolTransportBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 7, 1)
)
cfprApIqnpoolTransportBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IQNPOOL-MIB", "cfprApIqnpoolTransportBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIqnpoolTransportBlockEntry.setStatus("current")
_CfprApIqnpoolTransportBlockInstanceId_Type = CfprApManagedObjectId
_CfprApIqnpoolTransportBlockInstanceId_Object = MibTableColumn
cfprApIqnpoolTransportBlockInstanceId = _CfprApIqnpoolTransportBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 7, 1, 1),
    _CfprApIqnpoolTransportBlockInstanceId_Type()
)
cfprApIqnpoolTransportBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIqnpoolTransportBlockInstanceId.setStatus("current")
_CfprApIqnpoolTransportBlockDn_Type = CfprApManagedObjectDn
_CfprApIqnpoolTransportBlockDn_Object = MibTableColumn
cfprApIqnpoolTransportBlockDn = _CfprApIqnpoolTransportBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 7, 1, 2),
    _CfprApIqnpoolTransportBlockDn_Type()
)
cfprApIqnpoolTransportBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolTransportBlockDn.setStatus("current")
_CfprApIqnpoolTransportBlockRn_Type = SnmpAdminString
_CfprApIqnpoolTransportBlockRn_Object = MibTableColumn
cfprApIqnpoolTransportBlockRn = _CfprApIqnpoolTransportBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 7, 1, 3),
    _CfprApIqnpoolTransportBlockRn_Type()
)
cfprApIqnpoolTransportBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolTransportBlockRn.setStatus("current")
_CfprApIqnpoolTransportBlockFrom_Type = CfprApIqnpoolTransportBlockFrom
_CfprApIqnpoolTransportBlockFrom_Object = MibTableColumn
cfprApIqnpoolTransportBlockFrom = _CfprApIqnpoolTransportBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 7, 1, 4),
    _CfprApIqnpoolTransportBlockFrom_Type()
)
cfprApIqnpoolTransportBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolTransportBlockFrom.setStatus("current")
_CfprApIqnpoolTransportBlockSuffix_Type = SnmpAdminString
_CfprApIqnpoolTransportBlockSuffix_Object = MibTableColumn
cfprApIqnpoolTransportBlockSuffix = _CfprApIqnpoolTransportBlockSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 7, 1, 5),
    _CfprApIqnpoolTransportBlockSuffix_Type()
)
cfprApIqnpoolTransportBlockSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolTransportBlockSuffix.setStatus("current")
_CfprApIqnpoolTransportBlockTo_Type = CfprApIqnpoolTransportBlockTo
_CfprApIqnpoolTransportBlockTo_Object = MibTableColumn
cfprApIqnpoolTransportBlockTo = _CfprApIqnpoolTransportBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 7, 1, 6),
    _CfprApIqnpoolTransportBlockTo_Type()
)
cfprApIqnpoolTransportBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolTransportBlockTo.setStatus("current")
_CfprApIqnpoolUniverseTable_Object = MibTable
cfprApIqnpoolUniverseTable = _CfprApIqnpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 8)
)
if mibBuilder.loadTexts:
    cfprApIqnpoolUniverseTable.setStatus("current")
_CfprApIqnpoolUniverseEntry_Object = MibTableRow
cfprApIqnpoolUniverseEntry = _CfprApIqnpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 8, 1)
)
cfprApIqnpoolUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IQNPOOL-MIB", "cfprApIqnpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIqnpoolUniverseEntry.setStatus("current")
_CfprApIqnpoolUniverseInstanceId_Type = CfprApManagedObjectId
_CfprApIqnpoolUniverseInstanceId_Object = MibTableColumn
cfprApIqnpoolUniverseInstanceId = _CfprApIqnpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 8, 1, 1),
    _CfprApIqnpoolUniverseInstanceId_Type()
)
cfprApIqnpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIqnpoolUniverseInstanceId.setStatus("current")
_CfprApIqnpoolUniverseDn_Type = CfprApManagedObjectDn
_CfprApIqnpoolUniverseDn_Object = MibTableColumn
cfprApIqnpoolUniverseDn = _CfprApIqnpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 8, 1, 2),
    _CfprApIqnpoolUniverseDn_Type()
)
cfprApIqnpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolUniverseDn.setStatus("current")
_CfprApIqnpoolUniverseRn_Type = SnmpAdminString
_CfprApIqnpoolUniverseRn_Object = MibTableColumn
cfprApIqnpoolUniverseRn = _CfprApIqnpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 42, 8, 1, 3),
    _CfprApIqnpoolUniverseRn_Type()
)
cfprApIqnpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIqnpoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-IQNPOOL-MIB",
    **{"cfprApIqnpoolObjects": cfprApIqnpoolObjects,
       "cfprApIqnpoolAddrTable": cfprApIqnpoolAddrTable,
       "cfprApIqnpoolAddrEntry": cfprApIqnpoolAddrEntry,
       "cfprApIqnpoolAddrInstanceId": cfprApIqnpoolAddrInstanceId,
       "cfprApIqnpoolAddrDn": cfprApIqnpoolAddrDn,
       "cfprApIqnpoolAddrRn": cfprApIqnpoolAddrRn,
       "cfprApIqnpoolAddrAssigned": cfprApIqnpoolAddrAssigned,
       "cfprApIqnpoolAddrAssignedToDn": cfprApIqnpoolAddrAssignedToDn,
       "cfprApIqnpoolAddrGlobalAssignedCnt": cfprApIqnpoolAddrGlobalAssignedCnt,
       "cfprApIqnpoolAddrGlobalDefinedCnt": cfprApIqnpoolAddrGlobalDefinedCnt,
       "cfprApIqnpoolAddrName": cfprApIqnpoolAddrName,
       "cfprApIqnpoolAddrOwner": cfprApIqnpoolAddrOwner,
       "cfprApIqnpoolBlockTable": cfprApIqnpoolBlockTable,
       "cfprApIqnpoolBlockEntry": cfprApIqnpoolBlockEntry,
       "cfprApIqnpoolBlockInstanceId": cfprApIqnpoolBlockInstanceId,
       "cfprApIqnpoolBlockDn": cfprApIqnpoolBlockDn,
       "cfprApIqnpoolBlockRn": cfprApIqnpoolBlockRn,
       "cfprApIqnpoolBlockFrom": cfprApIqnpoolBlockFrom,
       "cfprApIqnpoolBlockSuffix": cfprApIqnpoolBlockSuffix,
       "cfprApIqnpoolBlockTo": cfprApIqnpoolBlockTo,
       "cfprApIqnpoolFormatTable": cfprApIqnpoolFormatTable,
       "cfprApIqnpoolFormatEntry": cfprApIqnpoolFormatEntry,
       "cfprApIqnpoolFormatInstanceId": cfprApIqnpoolFormatInstanceId,
       "cfprApIqnpoolFormatDn": cfprApIqnpoolFormatDn,
       "cfprApIqnpoolFormatRn": cfprApIqnpoolFormatRn,
       "cfprApIqnpoolFormatFormat": cfprApIqnpoolFormatFormat,
       "cfprApIqnpoolPoolTable": cfprApIqnpoolPoolTable,
       "cfprApIqnpoolPoolEntry": cfprApIqnpoolPoolEntry,
       "cfprApIqnpoolPoolInstanceId": cfprApIqnpoolPoolInstanceId,
       "cfprApIqnpoolPoolDn": cfprApIqnpoolPoolDn,
       "cfprApIqnpoolPoolRn": cfprApIqnpoolPoolRn,
       "cfprApIqnpoolPoolAssigned": cfprApIqnpoolPoolAssigned,
       "cfprApIqnpoolPoolAssignmentOrder": cfprApIqnpoolPoolAssignmentOrder,
       "cfprApIqnpoolPoolDescr": cfprApIqnpoolPoolDescr,
       "cfprApIqnpoolPoolIntId": cfprApIqnpoolPoolIntId,
       "cfprApIqnpoolPoolName": cfprApIqnpoolPoolName,
       "cfprApIqnpoolPoolPolicyLevel": cfprApIqnpoolPoolPolicyLevel,
       "cfprApIqnpoolPoolPolicyOwner": cfprApIqnpoolPoolPolicyOwner,
       "cfprApIqnpoolPoolPrefix": cfprApIqnpoolPoolPrefix,
       "cfprApIqnpoolPoolSize": cfprApIqnpoolPoolSize,
       "cfprApIqnpoolPoolableTable": cfprApIqnpoolPoolableTable,
       "cfprApIqnpoolPoolableEntry": cfprApIqnpoolPoolableEntry,
       "cfprApIqnpoolPoolableInstanceId": cfprApIqnpoolPoolableInstanceId,
       "cfprApIqnpoolPoolableDn": cfprApIqnpoolPoolableDn,
       "cfprApIqnpoolPoolableRn": cfprApIqnpoolPoolableRn,
       "cfprApIqnpoolPoolableId": cfprApIqnpoolPoolableId,
       "cfprApIqnpoolPoolablePoolDn": cfprApIqnpoolPoolablePoolDn,
       "cfprApIqnpoolPooledTable": cfprApIqnpoolPooledTable,
       "cfprApIqnpoolPooledEntry": cfprApIqnpoolPooledEntry,
       "cfprApIqnpoolPooledInstanceId": cfprApIqnpoolPooledInstanceId,
       "cfprApIqnpoolPooledDn": cfprApIqnpoolPooledDn,
       "cfprApIqnpoolPooledRn": cfprApIqnpoolPooledRn,
       "cfprApIqnpoolPooledAssigned": cfprApIqnpoolPooledAssigned,
       "cfprApIqnpoolPooledAssignedToDn": cfprApIqnpoolPooledAssignedToDn,
       "cfprApIqnpoolPooledName": cfprApIqnpoolPooledName,
       "cfprApIqnpoolPooledPoolableDn": cfprApIqnpoolPooledPoolableDn,
       "cfprApIqnpoolPooledPrevAssignedToDn": cfprApIqnpoolPooledPrevAssignedToDn,
       "cfprApIqnpoolTransportBlockTable": cfprApIqnpoolTransportBlockTable,
       "cfprApIqnpoolTransportBlockEntry": cfprApIqnpoolTransportBlockEntry,
       "cfprApIqnpoolTransportBlockInstanceId": cfprApIqnpoolTransportBlockInstanceId,
       "cfprApIqnpoolTransportBlockDn": cfprApIqnpoolTransportBlockDn,
       "cfprApIqnpoolTransportBlockRn": cfprApIqnpoolTransportBlockRn,
       "cfprApIqnpoolTransportBlockFrom": cfprApIqnpoolTransportBlockFrom,
       "cfprApIqnpoolTransportBlockSuffix": cfprApIqnpoolTransportBlockSuffix,
       "cfprApIqnpoolTransportBlockTo": cfprApIqnpoolTransportBlockTo,
       "cfprApIqnpoolUniverseTable": cfprApIqnpoolUniverseTable,
       "cfprApIqnpoolUniverseEntry": cfprApIqnpoolUniverseEntry,
       "cfprApIqnpoolUniverseInstanceId": cfprApIqnpoolUniverseInstanceId,
       "cfprApIqnpoolUniverseDn": cfprApIqnpoolUniverseDn,
       "cfprApIqnpoolUniverseRn": cfprApIqnpoolUniverseRn}
)
