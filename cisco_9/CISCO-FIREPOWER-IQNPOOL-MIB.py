# SNMP MIB module (CISCO-FIREPOWER-IQNPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-IQNPOOL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:11 2025
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

(CfprIqnpoolBlockFrom,
 CfprIqnpoolBlockTo,
 CfprIqnpoolPoolAssignmentOrder,
 CfprIqnpoolTransportBlockFrom,
 CfprIqnpoolTransportBlockTo,
 CfprPolicyPolicyOwner,
 CfprPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprIqnpoolBlockFrom",
    "CfprIqnpoolBlockTo",
    "CfprIqnpoolPoolAssignmentOrder",
    "CfprIqnpoolTransportBlockFrom",
    "CfprIqnpoolTransportBlockTo",
    "CfprPolicyPolicyOwner",
    "CfprPoolElementOwner")

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

cfprIqnpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprIqnpoolAddrTable_Object = MibTable
cfprIqnpoolAddrTable = _CfprIqnpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1)
)
if mibBuilder.loadTexts:
    cfprIqnpoolAddrTable.setStatus("current")
_CfprIqnpoolAddrEntry_Object = MibTableRow
cfprIqnpoolAddrEntry = _CfprIqnpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1)
)
cfprIqnpoolAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IQNPOOL-MIB", "cfprIqnpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIqnpoolAddrEntry.setStatus("current")
_CfprIqnpoolAddrInstanceId_Type = CfprManagedObjectId
_CfprIqnpoolAddrInstanceId_Object = MibTableColumn
cfprIqnpoolAddrInstanceId = _CfprIqnpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 1),
    _CfprIqnpoolAddrInstanceId_Type()
)
cfprIqnpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrInstanceId.setStatus("current")
_CfprIqnpoolAddrDn_Type = CfprManagedObjectDn
_CfprIqnpoolAddrDn_Object = MibTableColumn
cfprIqnpoolAddrDn = _CfprIqnpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 2),
    _CfprIqnpoolAddrDn_Type()
)
cfprIqnpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrDn.setStatus("current")
_CfprIqnpoolAddrRn_Type = SnmpAdminString
_CfprIqnpoolAddrRn_Object = MibTableColumn
cfprIqnpoolAddrRn = _CfprIqnpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 3),
    _CfprIqnpoolAddrRn_Type()
)
cfprIqnpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrRn.setStatus("current")
_CfprIqnpoolAddrAssigned_Type = TruthValue
_CfprIqnpoolAddrAssigned_Object = MibTableColumn
cfprIqnpoolAddrAssigned = _CfprIqnpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 4),
    _CfprIqnpoolAddrAssigned_Type()
)
cfprIqnpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrAssigned.setStatus("current")
_CfprIqnpoolAddrAssignedToDn_Type = SnmpAdminString
_CfprIqnpoolAddrAssignedToDn_Object = MibTableColumn
cfprIqnpoolAddrAssignedToDn = _CfprIqnpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 5),
    _CfprIqnpoolAddrAssignedToDn_Type()
)
cfprIqnpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrAssignedToDn.setStatus("current")
_CfprIqnpoolAddrGlobalAssignedCnt_Type = Gauge32
_CfprIqnpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cfprIqnpoolAddrGlobalAssignedCnt = _CfprIqnpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 6),
    _CfprIqnpoolAddrGlobalAssignedCnt_Type()
)
cfprIqnpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrGlobalAssignedCnt.setStatus("current")
_CfprIqnpoolAddrGlobalDefinedCnt_Type = Gauge32
_CfprIqnpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cfprIqnpoolAddrGlobalDefinedCnt = _CfprIqnpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 7),
    _CfprIqnpoolAddrGlobalDefinedCnt_Type()
)
cfprIqnpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrGlobalDefinedCnt.setStatus("current")
_CfprIqnpoolAddrName_Type = SnmpAdminString
_CfprIqnpoolAddrName_Object = MibTableColumn
cfprIqnpoolAddrName = _CfprIqnpoolAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 8),
    _CfprIqnpoolAddrName_Type()
)
cfprIqnpoolAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrName.setStatus("current")
_CfprIqnpoolAddrOwner_Type = CfprPoolElementOwner
_CfprIqnpoolAddrOwner_Object = MibTableColumn
cfprIqnpoolAddrOwner = _CfprIqnpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 1, 1, 9),
    _CfprIqnpoolAddrOwner_Type()
)
cfprIqnpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolAddrOwner.setStatus("current")
_CfprIqnpoolBlockTable_Object = MibTable
cfprIqnpoolBlockTable = _CfprIqnpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 2)
)
if mibBuilder.loadTexts:
    cfprIqnpoolBlockTable.setStatus("current")
_CfprIqnpoolBlockEntry_Object = MibTableRow
cfprIqnpoolBlockEntry = _CfprIqnpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 2, 1)
)
cfprIqnpoolBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IQNPOOL-MIB", "cfprIqnpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIqnpoolBlockEntry.setStatus("current")
_CfprIqnpoolBlockInstanceId_Type = CfprManagedObjectId
_CfprIqnpoolBlockInstanceId_Object = MibTableColumn
cfprIqnpoolBlockInstanceId = _CfprIqnpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 2, 1, 1),
    _CfprIqnpoolBlockInstanceId_Type()
)
cfprIqnpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIqnpoolBlockInstanceId.setStatus("current")
_CfprIqnpoolBlockDn_Type = CfprManagedObjectDn
_CfprIqnpoolBlockDn_Object = MibTableColumn
cfprIqnpoolBlockDn = _CfprIqnpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 2, 1, 2),
    _CfprIqnpoolBlockDn_Type()
)
cfprIqnpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolBlockDn.setStatus("current")
_CfprIqnpoolBlockRn_Type = SnmpAdminString
_CfprIqnpoolBlockRn_Object = MibTableColumn
cfprIqnpoolBlockRn = _CfprIqnpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 2, 1, 3),
    _CfprIqnpoolBlockRn_Type()
)
cfprIqnpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolBlockRn.setStatus("current")
_CfprIqnpoolBlockFrom_Type = CfprIqnpoolBlockFrom
_CfprIqnpoolBlockFrom_Object = MibTableColumn
cfprIqnpoolBlockFrom = _CfprIqnpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 2, 1, 4),
    _CfprIqnpoolBlockFrom_Type()
)
cfprIqnpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolBlockFrom.setStatus("current")
_CfprIqnpoolBlockSuffix_Type = SnmpAdminString
_CfprIqnpoolBlockSuffix_Object = MibTableColumn
cfprIqnpoolBlockSuffix = _CfprIqnpoolBlockSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 2, 1, 5),
    _CfprIqnpoolBlockSuffix_Type()
)
cfprIqnpoolBlockSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolBlockSuffix.setStatus("current")
_CfprIqnpoolBlockTo_Type = CfprIqnpoolBlockTo
_CfprIqnpoolBlockTo_Object = MibTableColumn
cfprIqnpoolBlockTo = _CfprIqnpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 2, 1, 6),
    _CfprIqnpoolBlockTo_Type()
)
cfprIqnpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolBlockTo.setStatus("current")
_CfprIqnpoolFormatTable_Object = MibTable
cfprIqnpoolFormatTable = _CfprIqnpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 3)
)
if mibBuilder.loadTexts:
    cfprIqnpoolFormatTable.setStatus("current")
_CfprIqnpoolFormatEntry_Object = MibTableRow
cfprIqnpoolFormatEntry = _CfprIqnpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 3, 1)
)
cfprIqnpoolFormatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IQNPOOL-MIB", "cfprIqnpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIqnpoolFormatEntry.setStatus("current")
_CfprIqnpoolFormatInstanceId_Type = CfprManagedObjectId
_CfprIqnpoolFormatInstanceId_Object = MibTableColumn
cfprIqnpoolFormatInstanceId = _CfprIqnpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 3, 1, 1),
    _CfprIqnpoolFormatInstanceId_Type()
)
cfprIqnpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIqnpoolFormatInstanceId.setStatus("current")
_CfprIqnpoolFormatDn_Type = CfprManagedObjectDn
_CfprIqnpoolFormatDn_Object = MibTableColumn
cfprIqnpoolFormatDn = _CfprIqnpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 3, 1, 2),
    _CfprIqnpoolFormatDn_Type()
)
cfprIqnpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolFormatDn.setStatus("current")
_CfprIqnpoolFormatRn_Type = SnmpAdminString
_CfprIqnpoolFormatRn_Object = MibTableColumn
cfprIqnpoolFormatRn = _CfprIqnpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 3, 1, 3),
    _CfprIqnpoolFormatRn_Type()
)
cfprIqnpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolFormatRn.setStatus("current")
_CfprIqnpoolFormatFormat_Type = SnmpAdminString
_CfprIqnpoolFormatFormat_Object = MibTableColumn
cfprIqnpoolFormatFormat = _CfprIqnpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 3, 1, 4),
    _CfprIqnpoolFormatFormat_Type()
)
cfprIqnpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolFormatFormat.setStatus("current")
_CfprIqnpoolPoolTable_Object = MibTable
cfprIqnpoolPoolTable = _CfprIqnpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4)
)
if mibBuilder.loadTexts:
    cfprIqnpoolPoolTable.setStatus("current")
_CfprIqnpoolPoolEntry_Object = MibTableRow
cfprIqnpoolPoolEntry = _CfprIqnpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1)
)
cfprIqnpoolPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IQNPOOL-MIB", "cfprIqnpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIqnpoolPoolEntry.setStatus("current")
_CfprIqnpoolPoolInstanceId_Type = CfprManagedObjectId
_CfprIqnpoolPoolInstanceId_Object = MibTableColumn
cfprIqnpoolPoolInstanceId = _CfprIqnpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 1),
    _CfprIqnpoolPoolInstanceId_Type()
)
cfprIqnpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolInstanceId.setStatus("current")
_CfprIqnpoolPoolDn_Type = CfprManagedObjectDn
_CfprIqnpoolPoolDn_Object = MibTableColumn
cfprIqnpoolPoolDn = _CfprIqnpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 2),
    _CfprIqnpoolPoolDn_Type()
)
cfprIqnpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolDn.setStatus("current")
_CfprIqnpoolPoolRn_Type = SnmpAdminString
_CfprIqnpoolPoolRn_Object = MibTableColumn
cfprIqnpoolPoolRn = _CfprIqnpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 3),
    _CfprIqnpoolPoolRn_Type()
)
cfprIqnpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolRn.setStatus("current")
_CfprIqnpoolPoolAssigned_Type = Gauge32
_CfprIqnpoolPoolAssigned_Object = MibTableColumn
cfprIqnpoolPoolAssigned = _CfprIqnpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 4),
    _CfprIqnpoolPoolAssigned_Type()
)
cfprIqnpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolAssigned.setStatus("current")
_CfprIqnpoolPoolAssignmentOrder_Type = CfprIqnpoolPoolAssignmentOrder
_CfprIqnpoolPoolAssignmentOrder_Object = MibTableColumn
cfprIqnpoolPoolAssignmentOrder = _CfprIqnpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 5),
    _CfprIqnpoolPoolAssignmentOrder_Type()
)
cfprIqnpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolAssignmentOrder.setStatus("current")
_CfprIqnpoolPoolDescr_Type = SnmpAdminString
_CfprIqnpoolPoolDescr_Object = MibTableColumn
cfprIqnpoolPoolDescr = _CfprIqnpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 6),
    _CfprIqnpoolPoolDescr_Type()
)
cfprIqnpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolDescr.setStatus("current")
_CfprIqnpoolPoolIntId_Type = SnmpAdminString
_CfprIqnpoolPoolIntId_Object = MibTableColumn
cfprIqnpoolPoolIntId = _CfprIqnpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 7),
    _CfprIqnpoolPoolIntId_Type()
)
cfprIqnpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolIntId.setStatus("current")
_CfprIqnpoolPoolName_Type = SnmpAdminString
_CfprIqnpoolPoolName_Object = MibTableColumn
cfprIqnpoolPoolName = _CfprIqnpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 8),
    _CfprIqnpoolPoolName_Type()
)
cfprIqnpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolName.setStatus("current")
_CfprIqnpoolPoolPolicyLevel_Type = Gauge32
_CfprIqnpoolPoolPolicyLevel_Object = MibTableColumn
cfprIqnpoolPoolPolicyLevel = _CfprIqnpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 9),
    _CfprIqnpoolPoolPolicyLevel_Type()
)
cfprIqnpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolPolicyLevel.setStatus("current")
_CfprIqnpoolPoolPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprIqnpoolPoolPolicyOwner_Object = MibTableColumn
cfprIqnpoolPoolPolicyOwner = _CfprIqnpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 10),
    _CfprIqnpoolPoolPolicyOwner_Type()
)
cfprIqnpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolPolicyOwner.setStatus("current")
_CfprIqnpoolPoolPrefix_Type = SnmpAdminString
_CfprIqnpoolPoolPrefix_Object = MibTableColumn
cfprIqnpoolPoolPrefix = _CfprIqnpoolPoolPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 11),
    _CfprIqnpoolPoolPrefix_Type()
)
cfprIqnpoolPoolPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolPrefix.setStatus("current")
_CfprIqnpoolPoolSize_Type = Gauge32
_CfprIqnpoolPoolSize_Object = MibTableColumn
cfprIqnpoolPoolSize = _CfprIqnpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 4, 1, 12),
    _CfprIqnpoolPoolSize_Type()
)
cfprIqnpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolSize.setStatus("current")
_CfprIqnpoolPoolableTable_Object = MibTable
cfprIqnpoolPoolableTable = _CfprIqnpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 5)
)
if mibBuilder.loadTexts:
    cfprIqnpoolPoolableTable.setStatus("current")
_CfprIqnpoolPoolableEntry_Object = MibTableRow
cfprIqnpoolPoolableEntry = _CfprIqnpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 5, 1)
)
cfprIqnpoolPoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IQNPOOL-MIB", "cfprIqnpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIqnpoolPoolableEntry.setStatus("current")
_CfprIqnpoolPoolableInstanceId_Type = CfprManagedObjectId
_CfprIqnpoolPoolableInstanceId_Object = MibTableColumn
cfprIqnpoolPoolableInstanceId = _CfprIqnpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 5, 1, 1),
    _CfprIqnpoolPoolableInstanceId_Type()
)
cfprIqnpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolableInstanceId.setStatus("current")
_CfprIqnpoolPoolableDn_Type = CfprManagedObjectDn
_CfprIqnpoolPoolableDn_Object = MibTableColumn
cfprIqnpoolPoolableDn = _CfprIqnpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 5, 1, 2),
    _CfprIqnpoolPoolableDn_Type()
)
cfprIqnpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolableDn.setStatus("current")
_CfprIqnpoolPoolableRn_Type = SnmpAdminString
_CfprIqnpoolPoolableRn_Object = MibTableColumn
cfprIqnpoolPoolableRn = _CfprIqnpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 5, 1, 3),
    _CfprIqnpoolPoolableRn_Type()
)
cfprIqnpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolableRn.setStatus("current")
_CfprIqnpoolPoolableId_Type = Unsigned64
_CfprIqnpoolPoolableId_Object = MibTableColumn
cfprIqnpoolPoolableId = _CfprIqnpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 5, 1, 4),
    _CfprIqnpoolPoolableId_Type()
)
cfprIqnpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolableId.setStatus("current")
_CfprIqnpoolPoolablePoolDn_Type = SnmpAdminString
_CfprIqnpoolPoolablePoolDn_Object = MibTableColumn
cfprIqnpoolPoolablePoolDn = _CfprIqnpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 5, 1, 5),
    _CfprIqnpoolPoolablePoolDn_Type()
)
cfprIqnpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPoolablePoolDn.setStatus("current")
_CfprIqnpoolPooledTable_Object = MibTable
cfprIqnpoolPooledTable = _CfprIqnpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6)
)
if mibBuilder.loadTexts:
    cfprIqnpoolPooledTable.setStatus("current")
_CfprIqnpoolPooledEntry_Object = MibTableRow
cfprIqnpoolPooledEntry = _CfprIqnpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1)
)
cfprIqnpoolPooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IQNPOOL-MIB", "cfprIqnpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIqnpoolPooledEntry.setStatus("current")
_CfprIqnpoolPooledInstanceId_Type = CfprManagedObjectId
_CfprIqnpoolPooledInstanceId_Object = MibTableColumn
cfprIqnpoolPooledInstanceId = _CfprIqnpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1, 1),
    _CfprIqnpoolPooledInstanceId_Type()
)
cfprIqnpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIqnpoolPooledInstanceId.setStatus("current")
_CfprIqnpoolPooledDn_Type = CfprManagedObjectDn
_CfprIqnpoolPooledDn_Object = MibTableColumn
cfprIqnpoolPooledDn = _CfprIqnpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1, 2),
    _CfprIqnpoolPooledDn_Type()
)
cfprIqnpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPooledDn.setStatus("current")
_CfprIqnpoolPooledRn_Type = SnmpAdminString
_CfprIqnpoolPooledRn_Object = MibTableColumn
cfprIqnpoolPooledRn = _CfprIqnpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1, 3),
    _CfprIqnpoolPooledRn_Type()
)
cfprIqnpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPooledRn.setStatus("current")
_CfprIqnpoolPooledAssigned_Type = TruthValue
_CfprIqnpoolPooledAssigned_Object = MibTableColumn
cfprIqnpoolPooledAssigned = _CfprIqnpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1, 4),
    _CfprIqnpoolPooledAssigned_Type()
)
cfprIqnpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPooledAssigned.setStatus("current")
_CfprIqnpoolPooledAssignedToDn_Type = SnmpAdminString
_CfprIqnpoolPooledAssignedToDn_Object = MibTableColumn
cfprIqnpoolPooledAssignedToDn = _CfprIqnpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1, 5),
    _CfprIqnpoolPooledAssignedToDn_Type()
)
cfprIqnpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPooledAssignedToDn.setStatus("current")
_CfprIqnpoolPooledName_Type = SnmpAdminString
_CfprIqnpoolPooledName_Object = MibTableColumn
cfprIqnpoolPooledName = _CfprIqnpoolPooledName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1, 6),
    _CfprIqnpoolPooledName_Type()
)
cfprIqnpoolPooledName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPooledName.setStatus("current")
_CfprIqnpoolPooledPoolableDn_Type = SnmpAdminString
_CfprIqnpoolPooledPoolableDn_Object = MibTableColumn
cfprIqnpoolPooledPoolableDn = _CfprIqnpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1, 7),
    _CfprIqnpoolPooledPoolableDn_Type()
)
cfprIqnpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPooledPoolableDn.setStatus("current")
_CfprIqnpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CfprIqnpoolPooledPrevAssignedToDn_Object = MibTableColumn
cfprIqnpoolPooledPrevAssignedToDn = _CfprIqnpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 6, 1, 8),
    _CfprIqnpoolPooledPrevAssignedToDn_Type()
)
cfprIqnpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolPooledPrevAssignedToDn.setStatus("current")
_CfprIqnpoolTransportBlockTable_Object = MibTable
cfprIqnpoolTransportBlockTable = _CfprIqnpoolTransportBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 7)
)
if mibBuilder.loadTexts:
    cfprIqnpoolTransportBlockTable.setStatus("current")
_CfprIqnpoolTransportBlockEntry_Object = MibTableRow
cfprIqnpoolTransportBlockEntry = _CfprIqnpoolTransportBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 7, 1)
)
cfprIqnpoolTransportBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IQNPOOL-MIB", "cfprIqnpoolTransportBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIqnpoolTransportBlockEntry.setStatus("current")
_CfprIqnpoolTransportBlockInstanceId_Type = CfprManagedObjectId
_CfprIqnpoolTransportBlockInstanceId_Object = MibTableColumn
cfprIqnpoolTransportBlockInstanceId = _CfprIqnpoolTransportBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 7, 1, 1),
    _CfprIqnpoolTransportBlockInstanceId_Type()
)
cfprIqnpoolTransportBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIqnpoolTransportBlockInstanceId.setStatus("current")
_CfprIqnpoolTransportBlockDn_Type = CfprManagedObjectDn
_CfprIqnpoolTransportBlockDn_Object = MibTableColumn
cfprIqnpoolTransportBlockDn = _CfprIqnpoolTransportBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 7, 1, 2),
    _CfprIqnpoolTransportBlockDn_Type()
)
cfprIqnpoolTransportBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolTransportBlockDn.setStatus("current")
_CfprIqnpoolTransportBlockRn_Type = SnmpAdminString
_CfprIqnpoolTransportBlockRn_Object = MibTableColumn
cfprIqnpoolTransportBlockRn = _CfprIqnpoolTransportBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 7, 1, 3),
    _CfprIqnpoolTransportBlockRn_Type()
)
cfprIqnpoolTransportBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolTransportBlockRn.setStatus("current")
_CfprIqnpoolTransportBlockFrom_Type = CfprIqnpoolTransportBlockFrom
_CfprIqnpoolTransportBlockFrom_Object = MibTableColumn
cfprIqnpoolTransportBlockFrom = _CfprIqnpoolTransportBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 7, 1, 4),
    _CfprIqnpoolTransportBlockFrom_Type()
)
cfprIqnpoolTransportBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolTransportBlockFrom.setStatus("current")
_CfprIqnpoolTransportBlockSuffix_Type = SnmpAdminString
_CfprIqnpoolTransportBlockSuffix_Object = MibTableColumn
cfprIqnpoolTransportBlockSuffix = _CfprIqnpoolTransportBlockSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 7, 1, 5),
    _CfprIqnpoolTransportBlockSuffix_Type()
)
cfprIqnpoolTransportBlockSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolTransportBlockSuffix.setStatus("current")
_CfprIqnpoolTransportBlockTo_Type = CfprIqnpoolTransportBlockTo
_CfprIqnpoolTransportBlockTo_Object = MibTableColumn
cfprIqnpoolTransportBlockTo = _CfprIqnpoolTransportBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 7, 1, 6),
    _CfprIqnpoolTransportBlockTo_Type()
)
cfprIqnpoolTransportBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolTransportBlockTo.setStatus("current")
_CfprIqnpoolUniverseTable_Object = MibTable
cfprIqnpoolUniverseTable = _CfprIqnpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 8)
)
if mibBuilder.loadTexts:
    cfprIqnpoolUniverseTable.setStatus("current")
_CfprIqnpoolUniverseEntry_Object = MibTableRow
cfprIqnpoolUniverseEntry = _CfprIqnpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 8, 1)
)
cfprIqnpoolUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IQNPOOL-MIB", "cfprIqnpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIqnpoolUniverseEntry.setStatus("current")
_CfprIqnpoolUniverseInstanceId_Type = CfprManagedObjectId
_CfprIqnpoolUniverseInstanceId_Object = MibTableColumn
cfprIqnpoolUniverseInstanceId = _CfprIqnpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 8, 1, 1),
    _CfprIqnpoolUniverseInstanceId_Type()
)
cfprIqnpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIqnpoolUniverseInstanceId.setStatus("current")
_CfprIqnpoolUniverseDn_Type = CfprManagedObjectDn
_CfprIqnpoolUniverseDn_Object = MibTableColumn
cfprIqnpoolUniverseDn = _CfprIqnpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 8, 1, 2),
    _CfprIqnpoolUniverseDn_Type()
)
cfprIqnpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolUniverseDn.setStatus("current")
_CfprIqnpoolUniverseRn_Type = SnmpAdminString
_CfprIqnpoolUniverseRn_Object = MibTableColumn
cfprIqnpoolUniverseRn = _CfprIqnpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 42, 8, 1, 3),
    _CfprIqnpoolUniverseRn_Type()
)
cfprIqnpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIqnpoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-IQNPOOL-MIB",
    **{"cfprIqnpoolObjects": cfprIqnpoolObjects,
       "cfprIqnpoolAddrTable": cfprIqnpoolAddrTable,
       "cfprIqnpoolAddrEntry": cfprIqnpoolAddrEntry,
       "cfprIqnpoolAddrInstanceId": cfprIqnpoolAddrInstanceId,
       "cfprIqnpoolAddrDn": cfprIqnpoolAddrDn,
       "cfprIqnpoolAddrRn": cfprIqnpoolAddrRn,
       "cfprIqnpoolAddrAssigned": cfprIqnpoolAddrAssigned,
       "cfprIqnpoolAddrAssignedToDn": cfprIqnpoolAddrAssignedToDn,
       "cfprIqnpoolAddrGlobalAssignedCnt": cfprIqnpoolAddrGlobalAssignedCnt,
       "cfprIqnpoolAddrGlobalDefinedCnt": cfprIqnpoolAddrGlobalDefinedCnt,
       "cfprIqnpoolAddrName": cfprIqnpoolAddrName,
       "cfprIqnpoolAddrOwner": cfprIqnpoolAddrOwner,
       "cfprIqnpoolBlockTable": cfprIqnpoolBlockTable,
       "cfprIqnpoolBlockEntry": cfprIqnpoolBlockEntry,
       "cfprIqnpoolBlockInstanceId": cfprIqnpoolBlockInstanceId,
       "cfprIqnpoolBlockDn": cfprIqnpoolBlockDn,
       "cfprIqnpoolBlockRn": cfprIqnpoolBlockRn,
       "cfprIqnpoolBlockFrom": cfprIqnpoolBlockFrom,
       "cfprIqnpoolBlockSuffix": cfprIqnpoolBlockSuffix,
       "cfprIqnpoolBlockTo": cfprIqnpoolBlockTo,
       "cfprIqnpoolFormatTable": cfprIqnpoolFormatTable,
       "cfprIqnpoolFormatEntry": cfprIqnpoolFormatEntry,
       "cfprIqnpoolFormatInstanceId": cfprIqnpoolFormatInstanceId,
       "cfprIqnpoolFormatDn": cfprIqnpoolFormatDn,
       "cfprIqnpoolFormatRn": cfprIqnpoolFormatRn,
       "cfprIqnpoolFormatFormat": cfprIqnpoolFormatFormat,
       "cfprIqnpoolPoolTable": cfprIqnpoolPoolTable,
       "cfprIqnpoolPoolEntry": cfprIqnpoolPoolEntry,
       "cfprIqnpoolPoolInstanceId": cfprIqnpoolPoolInstanceId,
       "cfprIqnpoolPoolDn": cfprIqnpoolPoolDn,
       "cfprIqnpoolPoolRn": cfprIqnpoolPoolRn,
       "cfprIqnpoolPoolAssigned": cfprIqnpoolPoolAssigned,
       "cfprIqnpoolPoolAssignmentOrder": cfprIqnpoolPoolAssignmentOrder,
       "cfprIqnpoolPoolDescr": cfprIqnpoolPoolDescr,
       "cfprIqnpoolPoolIntId": cfprIqnpoolPoolIntId,
       "cfprIqnpoolPoolName": cfprIqnpoolPoolName,
       "cfprIqnpoolPoolPolicyLevel": cfprIqnpoolPoolPolicyLevel,
       "cfprIqnpoolPoolPolicyOwner": cfprIqnpoolPoolPolicyOwner,
       "cfprIqnpoolPoolPrefix": cfprIqnpoolPoolPrefix,
       "cfprIqnpoolPoolSize": cfprIqnpoolPoolSize,
       "cfprIqnpoolPoolableTable": cfprIqnpoolPoolableTable,
       "cfprIqnpoolPoolableEntry": cfprIqnpoolPoolableEntry,
       "cfprIqnpoolPoolableInstanceId": cfprIqnpoolPoolableInstanceId,
       "cfprIqnpoolPoolableDn": cfprIqnpoolPoolableDn,
       "cfprIqnpoolPoolableRn": cfprIqnpoolPoolableRn,
       "cfprIqnpoolPoolableId": cfprIqnpoolPoolableId,
       "cfprIqnpoolPoolablePoolDn": cfprIqnpoolPoolablePoolDn,
       "cfprIqnpoolPooledTable": cfprIqnpoolPooledTable,
       "cfprIqnpoolPooledEntry": cfprIqnpoolPooledEntry,
       "cfprIqnpoolPooledInstanceId": cfprIqnpoolPooledInstanceId,
       "cfprIqnpoolPooledDn": cfprIqnpoolPooledDn,
       "cfprIqnpoolPooledRn": cfprIqnpoolPooledRn,
       "cfprIqnpoolPooledAssigned": cfprIqnpoolPooledAssigned,
       "cfprIqnpoolPooledAssignedToDn": cfprIqnpoolPooledAssignedToDn,
       "cfprIqnpoolPooledName": cfprIqnpoolPooledName,
       "cfprIqnpoolPooledPoolableDn": cfprIqnpoolPooledPoolableDn,
       "cfprIqnpoolPooledPrevAssignedToDn": cfprIqnpoolPooledPrevAssignedToDn,
       "cfprIqnpoolTransportBlockTable": cfprIqnpoolTransportBlockTable,
       "cfprIqnpoolTransportBlockEntry": cfprIqnpoolTransportBlockEntry,
       "cfprIqnpoolTransportBlockInstanceId": cfprIqnpoolTransportBlockInstanceId,
       "cfprIqnpoolTransportBlockDn": cfprIqnpoolTransportBlockDn,
       "cfprIqnpoolTransportBlockRn": cfprIqnpoolTransportBlockRn,
       "cfprIqnpoolTransportBlockFrom": cfprIqnpoolTransportBlockFrom,
       "cfprIqnpoolTransportBlockSuffix": cfprIqnpoolTransportBlockSuffix,
       "cfprIqnpoolTransportBlockTo": cfprIqnpoolTransportBlockTo,
       "cfprIqnpoolUniverseTable": cfprIqnpoolUniverseTable,
       "cfprIqnpoolUniverseEntry": cfprIqnpoolUniverseEntry,
       "cfprIqnpoolUniverseInstanceId": cfprIqnpoolUniverseInstanceId,
       "cfprIqnpoolUniverseDn": cfprIqnpoolUniverseDn,
       "cfprIqnpoolUniverseRn": cfprIqnpoolUniverseRn}
)
