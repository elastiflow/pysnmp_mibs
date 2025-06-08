# SNMP MIB module (CISCO-FIREPOWER-AP-IDENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-IDENT-MIB.mib
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

(CfprApConditionRemoteInvRslt,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApIdentConsType,
 CfprApIdentIdDefinedInIdm,
 CfprApIdentIdentReqIntent,
 CfprApIdentIdentRequestFsmCurrentFsm,
 CfprApIdentIdentRequestFsmStageName,
 CfprApIdentIdentRequestFsmTaskItem,
 CfprApIdentIdentType,
 CfprApIdentMetaSystemFsmCurrentFsm,
 CfprApIdentMetaSystemFsmStageName,
 CfprApIdentMetaSystemFsmTaskItem,
 CfprApIdentRetStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApIdentConsType",
    "CfprApIdentIdDefinedInIdm",
    "CfprApIdentIdentReqIntent",
    "CfprApIdentIdentRequestFsmCurrentFsm",
    "CfprApIdentIdentRequestFsmStageName",
    "CfprApIdentIdentRequestFsmTaskItem",
    "CfprApIdentIdentType",
    "CfprApIdentMetaSystemFsmCurrentFsm",
    "CfprApIdentMetaSystemFsmStageName",
    "CfprApIdentMetaSystemFsmTaskItem",
    "CfprApIdentRetStatus")

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

cfprApIdentObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApIdentIdentCtxTable_Object = MibTable
cfprApIdentIdentCtxTable = _CfprApIdentIdentCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1)
)
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxTable.setStatus("current")
_CfprApIdentIdentCtxEntry_Object = MibTableRow
cfprApIdentIdentCtxEntry = _CfprApIdentIdentCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1)
)
cfprApIdentIdentCtxEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentIdentCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxEntry.setStatus("current")
_CfprApIdentIdentCtxInstanceId_Type = CfprApManagedObjectId
_CfprApIdentIdentCtxInstanceId_Object = MibTableColumn
cfprApIdentIdentCtxInstanceId = _CfprApIdentIdentCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 1),
    _CfprApIdentIdentCtxInstanceId_Type()
)
cfprApIdentIdentCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxInstanceId.setStatus("current")
_CfprApIdentIdentCtxDn_Type = CfprApManagedObjectDn
_CfprApIdentIdentCtxDn_Object = MibTableColumn
cfprApIdentIdentCtxDn = _CfprApIdentIdentCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 2),
    _CfprApIdentIdentCtxDn_Type()
)
cfprApIdentIdentCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxDn.setStatus("current")
_CfprApIdentIdentCtxRn_Type = SnmpAdminString
_CfprApIdentIdentCtxRn_Object = MibTableColumn
cfprApIdentIdentCtxRn = _CfprApIdentIdentCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 3),
    _CfprApIdentIdentCtxRn_Type()
)
cfprApIdentIdentCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxRn.setStatus("current")
_CfprApIdentIdentCtxAssigned_Type = SnmpAdminString
_CfprApIdentIdentCtxAssigned_Object = MibTableColumn
cfprApIdentIdentCtxAssigned = _CfprApIdentIdentCtxAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 4),
    _CfprApIdentIdentCtxAssigned_Type()
)
cfprApIdentIdentCtxAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxAssigned.setStatus("current")
_CfprApIdentIdentCtxConsDn_Type = SnmpAdminString
_CfprApIdentIdentCtxConsDn_Object = MibTableColumn
cfprApIdentIdentCtxConsDn = _CfprApIdentIdentCtxConsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 5),
    _CfprApIdentIdentCtxConsDn_Type()
)
cfprApIdentIdentCtxConsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxConsDn.setStatus("current")
_CfprApIdentIdentCtxConsType_Type = CfprApIdentConsType
_CfprApIdentIdentCtxConsType_Object = MibTableColumn
cfprApIdentIdentCtxConsType = _CfprApIdentIdentCtxConsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 6),
    _CfprApIdentIdentCtxConsType_Type()
)
cfprApIdentIdentCtxConsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxConsType.setStatus("current")
_CfprApIdentIdentCtxDefinedInIdm_Type = CfprApIdentIdDefinedInIdm
_CfprApIdentIdentCtxDefinedInIdm_Object = MibTableColumn
cfprApIdentIdentCtxDefinedInIdm = _CfprApIdentIdentCtxDefinedInIdm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 7),
    _CfprApIdentIdentCtxDefinedInIdm_Type()
)
cfprApIdentIdentCtxDefinedInIdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxDefinedInIdm.setStatus("current")
_CfprApIdentIdentCtxGlobalAssignedCnt_Type = Gauge32
_CfprApIdentIdentCtxGlobalAssignedCnt_Object = MibTableColumn
cfprApIdentIdentCtxGlobalAssignedCnt = _CfprApIdentIdentCtxGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 8),
    _CfprApIdentIdentCtxGlobalAssignedCnt_Type()
)
cfprApIdentIdentCtxGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxGlobalAssignedCnt.setStatus("current")
_CfprApIdentIdentCtxGlobalDefinedCnt_Type = Gauge32
_CfprApIdentIdentCtxGlobalDefinedCnt_Object = MibTableColumn
cfprApIdentIdentCtxGlobalDefinedCnt = _CfprApIdentIdentCtxGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 9),
    _CfprApIdentIdentCtxGlobalDefinedCnt_Type()
)
cfprApIdentIdentCtxGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxGlobalDefinedCnt.setStatus("current")
_CfprApIdentIdentCtxIdentPoolName_Type = SnmpAdminString
_CfprApIdentIdentCtxIdentPoolName_Object = MibTableColumn
cfprApIdentIdentCtxIdentPoolName = _CfprApIdentIdentCtxIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 10),
    _CfprApIdentIdentCtxIdentPoolName_Type()
)
cfprApIdentIdentCtxIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxIdentPoolName.setStatus("current")
_CfprApIdentIdentCtxIdentType_Type = CfprApIdentIdentType
_CfprApIdentIdentCtxIdentType_Object = MibTableColumn
cfprApIdentIdentCtxIdentType = _CfprApIdentIdentCtxIdentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 11),
    _CfprApIdentIdentCtxIdentType_Type()
)
cfprApIdentIdentCtxIdentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxIdentType.setStatus("current")
_CfprApIdentIdentCtxIntent_Type = CfprApIdentIdentReqIntent
_CfprApIdentIdentCtxIntent_Object = MibTableColumn
cfprApIdentIdentCtxIntent = _CfprApIdentIdentCtxIntent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 12),
    _CfprApIdentIdentCtxIntent_Type()
)
cfprApIdentIdentCtxIntent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxIntent.setStatus("current")
_CfprApIdentIdentCtxIsAssignedLocally_Type = TruthValue
_CfprApIdentIdentCtxIsAssignedLocally_Object = MibTableColumn
cfprApIdentIdentCtxIsAssignedLocally = _CfprApIdentIdentCtxIsAssignedLocally_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 13),
    _CfprApIdentIdentCtxIsAssignedLocally_Type()
)
cfprApIdentIdentCtxIsAssignedLocally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxIsAssignedLocally.setStatus("current")
_CfprApIdentIdentCtxPoolDn_Type = SnmpAdminString
_CfprApIdentIdentCtxPoolDn_Object = MibTableColumn
cfprApIdentIdentCtxPoolDn = _CfprApIdentIdentCtxPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 14),
    _CfprApIdentIdentCtxPoolDn_Type()
)
cfprApIdentIdentCtxPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxPoolDn.setStatus("current")
_CfprApIdentIdentCtxPoolOrgDn_Type = SnmpAdminString
_CfprApIdentIdentCtxPoolOrgDn_Object = MibTableColumn
cfprApIdentIdentCtxPoolOrgDn = _CfprApIdentIdentCtxPoolOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 15),
    _CfprApIdentIdentCtxPoolOrgDn_Type()
)
cfprApIdentIdentCtxPoolOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxPoolOrgDn.setStatus("current")
_CfprApIdentIdentCtxPooledId_Type = Gauge32
_CfprApIdentIdentCtxPooledId_Object = MibTableColumn
cfprApIdentIdentCtxPooledId = _CfprApIdentIdentCtxPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 16),
    _CfprApIdentIdentCtxPooledId_Type()
)
cfprApIdentIdentCtxPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxPooledId.setStatus("current")
_CfprApIdentIdentCtxRetStatus_Type = CfprApIdentRetStatus
_CfprApIdentIdentCtxRetStatus_Object = MibTableColumn
cfprApIdentIdentCtxRetStatus = _CfprApIdentIdentCtxRetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 17),
    _CfprApIdentIdentCtxRetStatus_Type()
)
cfprApIdentIdentCtxRetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxRetStatus.setStatus("current")
_CfprApIdentIdentCtxSeqNum_Type = Gauge32
_CfprApIdentIdentCtxSeqNum_Object = MibTableColumn
cfprApIdentIdentCtxSeqNum = _CfprApIdentIdentCtxSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 18),
    _CfprApIdentIdentCtxSeqNum_Type()
)
cfprApIdentIdentCtxSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxSeqNum.setStatus("current")
_CfprApIdentIdentCtxSupplId1_Type = SnmpAdminString
_CfprApIdentIdentCtxSupplId1_Object = MibTableColumn
cfprApIdentIdentCtxSupplId1 = _CfprApIdentIdentCtxSupplId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 19),
    _CfprApIdentIdentCtxSupplId1_Type()
)
cfprApIdentIdentCtxSupplId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxSupplId1.setStatus("current")
_CfprApIdentIdentCtxSupplId2_Type = SnmpAdminString
_CfprApIdentIdentCtxSupplId2_Object = MibTableColumn
cfprApIdentIdentCtxSupplId2 = _CfprApIdentIdentCtxSupplId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 20),
    _CfprApIdentIdentCtxSupplId2_Type()
)
cfprApIdentIdentCtxSupplId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxSupplId2.setStatus("current")
_CfprApIdentIdentCtxSupplId3_Type = SnmpAdminString
_CfprApIdentIdentCtxSupplId3_Object = MibTableColumn
cfprApIdentIdentCtxSupplId3 = _CfprApIdentIdentCtxSupplId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 21),
    _CfprApIdentIdentCtxSupplId3_Type()
)
cfprApIdentIdentCtxSupplId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxSupplId3.setStatus("current")
_CfprApIdentIdentCtxSupplId4_Type = SnmpAdminString
_CfprApIdentIdentCtxSupplId4_Object = MibTableColumn
cfprApIdentIdentCtxSupplId4 = _CfprApIdentIdentCtxSupplId4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 1, 1, 22),
    _CfprApIdentIdentCtxSupplId4_Type()
)
cfprApIdentIdentCtxSupplId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentCtxSupplId4.setStatus("current")
_CfprApIdentIdentRequestTable_Object = MibTable
cfprApIdentIdentRequestTable = _CfprApIdentIdentRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2)
)
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestTable.setStatus("current")
_CfprApIdentIdentRequestEntry_Object = MibTableRow
cfprApIdentIdentRequestEntry = _CfprApIdentIdentRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1)
)
cfprApIdentIdentRequestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentIdentRequestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestEntry.setStatus("current")
_CfprApIdentIdentRequestInstanceId_Type = CfprApManagedObjectId
_CfprApIdentIdentRequestInstanceId_Object = MibTableColumn
cfprApIdentIdentRequestInstanceId = _CfprApIdentIdentRequestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 1),
    _CfprApIdentIdentRequestInstanceId_Type()
)
cfprApIdentIdentRequestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestInstanceId.setStatus("current")
_CfprApIdentIdentRequestDn_Type = CfprApManagedObjectDn
_CfprApIdentIdentRequestDn_Object = MibTableColumn
cfprApIdentIdentRequestDn = _CfprApIdentIdentRequestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 2),
    _CfprApIdentIdentRequestDn_Type()
)
cfprApIdentIdentRequestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestDn.setStatus("current")
_CfprApIdentIdentRequestRn_Type = SnmpAdminString
_CfprApIdentIdentRequestRn_Object = MibTableColumn
cfprApIdentIdentRequestRn = _CfprApIdentIdentRequestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 3),
    _CfprApIdentIdentRequestRn_Type()
)
cfprApIdentIdentRequestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestRn.setStatus("current")
_CfprApIdentIdentRequestEpDn_Type = SnmpAdminString
_CfprApIdentIdentRequestEpDn_Object = MibTableColumn
cfprApIdentIdentRequestEpDn = _CfprApIdentIdentRequestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 4),
    _CfprApIdentIdentRequestEpDn_Type()
)
cfprApIdentIdentRequestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestEpDn.setStatus("current")
_CfprApIdentIdentRequestFsmDescr_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmDescr_Object = MibTableColumn
cfprApIdentIdentRequestFsmDescr = _CfprApIdentIdentRequestFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 5),
    _CfprApIdentIdentRequestFsmDescr_Type()
)
cfprApIdentIdentRequestFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmDescr.setStatus("current")
_CfprApIdentIdentRequestFsmPrev_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmPrev_Object = MibTableColumn
cfprApIdentIdentRequestFsmPrev = _CfprApIdentIdentRequestFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 6),
    _CfprApIdentIdentRequestFsmPrev_Type()
)
cfprApIdentIdentRequestFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmPrev.setStatus("current")
_CfprApIdentIdentRequestFsmProgr_Type = Gauge32
_CfprApIdentIdentRequestFsmProgr_Object = MibTableColumn
cfprApIdentIdentRequestFsmProgr = _CfprApIdentIdentRequestFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 7),
    _CfprApIdentIdentRequestFsmProgr_Type()
)
cfprApIdentIdentRequestFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmProgr.setStatus("current")
_CfprApIdentIdentRequestFsmRmtInvErrCode_Type = Gauge32
_CfprApIdentIdentRequestFsmRmtInvErrCode_Object = MibTableColumn
cfprApIdentIdentRequestFsmRmtInvErrCode = _CfprApIdentIdentRequestFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 8),
    _CfprApIdentIdentRequestFsmRmtInvErrCode_Type()
)
cfprApIdentIdentRequestFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmRmtInvErrCode.setStatus("current")
_CfprApIdentIdentRequestFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmRmtInvErrDescr_Object = MibTableColumn
cfprApIdentIdentRequestFsmRmtInvErrDescr = _CfprApIdentIdentRequestFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 9),
    _CfprApIdentIdentRequestFsmRmtInvErrDescr_Type()
)
cfprApIdentIdentRequestFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmRmtInvErrDescr.setStatus("current")
_CfprApIdentIdentRequestFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApIdentIdentRequestFsmRmtInvRslt_Object = MibTableColumn
cfprApIdentIdentRequestFsmRmtInvRslt = _CfprApIdentIdentRequestFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 10),
    _CfprApIdentIdentRequestFsmRmtInvRslt_Type()
)
cfprApIdentIdentRequestFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmRmtInvRslt.setStatus("current")
_CfprApIdentIdentRequestFsmStageDescr_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmStageDescr_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageDescr = _CfprApIdentIdentRequestFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 11),
    _CfprApIdentIdentRequestFsmStageDescr_Type()
)
cfprApIdentIdentRequestFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageDescr.setStatus("current")
_CfprApIdentIdentRequestFsmStamp_Type = DateAndTime
_CfprApIdentIdentRequestFsmStamp_Object = MibTableColumn
cfprApIdentIdentRequestFsmStamp = _CfprApIdentIdentRequestFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 12),
    _CfprApIdentIdentRequestFsmStamp_Type()
)
cfprApIdentIdentRequestFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStamp.setStatus("current")
_CfprApIdentIdentRequestFsmStatus_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmStatus_Object = MibTableColumn
cfprApIdentIdentRequestFsmStatus = _CfprApIdentIdentRequestFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 13),
    _CfprApIdentIdentRequestFsmStatus_Type()
)
cfprApIdentIdentRequestFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStatus.setStatus("current")
_CfprApIdentIdentRequestFsmTry_Type = Gauge32
_CfprApIdentIdentRequestFsmTry_Object = MibTableColumn
cfprApIdentIdentRequestFsmTry = _CfprApIdentIdentRequestFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 14),
    _CfprApIdentIdentRequestFsmTry_Type()
)
cfprApIdentIdentRequestFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTry.setStatus("current")
_CfprApIdentIdentRequestId_Type = Gauge32
_CfprApIdentIdentRequestId_Object = MibTableColumn
cfprApIdentIdentRequestId = _CfprApIdentIdentRequestId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 15),
    _CfprApIdentIdentRequestId_Type()
)
cfprApIdentIdentRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestId.setStatus("current")
_CfprApIdentIdentRequestRequestSize_Type = Gauge32
_CfprApIdentIdentRequestRequestSize_Object = MibTableColumn
cfprApIdentIdentRequestRequestSize = _CfprApIdentIdentRequestRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 16),
    _CfprApIdentIdentRequestRequestSize_Type()
)
cfprApIdentIdentRequestRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestRequestSize.setStatus("current")
_CfprApIdentIdentRequestSeqNum_Type = Gauge32
_CfprApIdentIdentRequestSeqNum_Object = MibTableColumn
cfprApIdentIdentRequestSeqNum = _CfprApIdentIdentRequestSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 2, 1, 17),
    _CfprApIdentIdentRequestSeqNum_Type()
)
cfprApIdentIdentRequestSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestSeqNum.setStatus("current")
_CfprApIdentIdentRequestFsmTable_Object = MibTable
cfprApIdentIdentRequestFsmTable = _CfprApIdentIdentRequestFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3)
)
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTable.setStatus("current")
_CfprApIdentIdentRequestFsmEntry_Object = MibTableRow
cfprApIdentIdentRequestFsmEntry = _CfprApIdentIdentRequestFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1)
)
cfprApIdentIdentRequestFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentIdentRequestFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmEntry.setStatus("current")
_CfprApIdentIdentRequestFsmInstanceId_Type = CfprApManagedObjectId
_CfprApIdentIdentRequestFsmInstanceId_Object = MibTableColumn
cfprApIdentIdentRequestFsmInstanceId = _CfprApIdentIdentRequestFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 1),
    _CfprApIdentIdentRequestFsmInstanceId_Type()
)
cfprApIdentIdentRequestFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmInstanceId.setStatus("current")
_CfprApIdentIdentRequestFsmDn_Type = CfprApManagedObjectDn
_CfprApIdentIdentRequestFsmDn_Object = MibTableColumn
cfprApIdentIdentRequestFsmDn = _CfprApIdentIdentRequestFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 2),
    _CfprApIdentIdentRequestFsmDn_Type()
)
cfprApIdentIdentRequestFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmDn.setStatus("current")
_CfprApIdentIdentRequestFsmRn_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmRn_Object = MibTableColumn
cfprApIdentIdentRequestFsmRn = _CfprApIdentIdentRequestFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 3),
    _CfprApIdentIdentRequestFsmRn_Type()
)
cfprApIdentIdentRequestFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmRn.setStatus("current")
_CfprApIdentIdentRequestFsmCompletionTime_Type = DateAndTime
_CfprApIdentIdentRequestFsmCompletionTime_Object = MibTableColumn
cfprApIdentIdentRequestFsmCompletionTime = _CfprApIdentIdentRequestFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 4),
    _CfprApIdentIdentRequestFsmCompletionTime_Type()
)
cfprApIdentIdentRequestFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmCompletionTime.setStatus("current")
_CfprApIdentIdentRequestFsmCurrentFsm_Type = CfprApIdentIdentRequestFsmCurrentFsm
_CfprApIdentIdentRequestFsmCurrentFsm_Object = MibTableColumn
cfprApIdentIdentRequestFsmCurrentFsm = _CfprApIdentIdentRequestFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 5),
    _CfprApIdentIdentRequestFsmCurrentFsm_Type()
)
cfprApIdentIdentRequestFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmCurrentFsm.setStatus("current")
_CfprApIdentIdentRequestFsmDescrData_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmDescrData_Object = MibTableColumn
cfprApIdentIdentRequestFsmDescrData = _CfprApIdentIdentRequestFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 6),
    _CfprApIdentIdentRequestFsmDescrData_Type()
)
cfprApIdentIdentRequestFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmDescrData.setStatus("current")
_CfprApIdentIdentRequestFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApIdentIdentRequestFsmFsmStatus_Object = MibTableColumn
cfprApIdentIdentRequestFsmFsmStatus = _CfprApIdentIdentRequestFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 7),
    _CfprApIdentIdentRequestFsmFsmStatus_Type()
)
cfprApIdentIdentRequestFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmFsmStatus.setStatus("current")
_CfprApIdentIdentRequestFsmProgress_Type = Gauge32
_CfprApIdentIdentRequestFsmProgress_Object = MibTableColumn
cfprApIdentIdentRequestFsmProgress = _CfprApIdentIdentRequestFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 8),
    _CfprApIdentIdentRequestFsmProgress_Type()
)
cfprApIdentIdentRequestFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmProgress.setStatus("current")
_CfprApIdentIdentRequestFsmRmtErrCode_Type = Gauge32
_CfprApIdentIdentRequestFsmRmtErrCode_Object = MibTableColumn
cfprApIdentIdentRequestFsmRmtErrCode = _CfprApIdentIdentRequestFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 9),
    _CfprApIdentIdentRequestFsmRmtErrCode_Type()
)
cfprApIdentIdentRequestFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmRmtErrCode.setStatus("current")
_CfprApIdentIdentRequestFsmRmtErrDescr_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmRmtErrDescr_Object = MibTableColumn
cfprApIdentIdentRequestFsmRmtErrDescr = _CfprApIdentIdentRequestFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 10),
    _CfprApIdentIdentRequestFsmRmtErrDescr_Type()
)
cfprApIdentIdentRequestFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmRmtErrDescr.setStatus("current")
_CfprApIdentIdentRequestFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApIdentIdentRequestFsmRmtRslt_Object = MibTableColumn
cfprApIdentIdentRequestFsmRmtRslt = _CfprApIdentIdentRequestFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 3, 1, 11),
    _CfprApIdentIdentRequestFsmRmtRslt_Type()
)
cfprApIdentIdentRequestFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmRmtRslt.setStatus("current")
_CfprApIdentIdentRequestFsmStageTable_Object = MibTable
cfprApIdentIdentRequestFsmStageTable = _CfprApIdentIdentRequestFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4)
)
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageTable.setStatus("current")
_CfprApIdentIdentRequestFsmStageEntry_Object = MibTableRow
cfprApIdentIdentRequestFsmStageEntry = _CfprApIdentIdentRequestFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1)
)
cfprApIdentIdentRequestFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentIdentRequestFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageEntry.setStatus("current")
_CfprApIdentIdentRequestFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApIdentIdentRequestFsmStageInstanceId_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageInstanceId = _CfprApIdentIdentRequestFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 1),
    _CfprApIdentIdentRequestFsmStageInstanceId_Type()
)
cfprApIdentIdentRequestFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageInstanceId.setStatus("current")
_CfprApIdentIdentRequestFsmStageDn_Type = CfprApManagedObjectDn
_CfprApIdentIdentRequestFsmStageDn_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageDn = _CfprApIdentIdentRequestFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 2),
    _CfprApIdentIdentRequestFsmStageDn_Type()
)
cfprApIdentIdentRequestFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageDn.setStatus("current")
_CfprApIdentIdentRequestFsmStageRn_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmStageRn_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageRn = _CfprApIdentIdentRequestFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 3),
    _CfprApIdentIdentRequestFsmStageRn_Type()
)
cfprApIdentIdentRequestFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageRn.setStatus("current")
_CfprApIdentIdentRequestFsmStageDescrData_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmStageDescrData_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageDescrData = _CfprApIdentIdentRequestFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 4),
    _CfprApIdentIdentRequestFsmStageDescrData_Type()
)
cfprApIdentIdentRequestFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageDescrData.setStatus("current")
_CfprApIdentIdentRequestFsmStageLastUpdateTime_Type = DateAndTime
_CfprApIdentIdentRequestFsmStageLastUpdateTime_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageLastUpdateTime = _CfprApIdentIdentRequestFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 5),
    _CfprApIdentIdentRequestFsmStageLastUpdateTime_Type()
)
cfprApIdentIdentRequestFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageLastUpdateTime.setStatus("current")
_CfprApIdentIdentRequestFsmStageName_Type = CfprApIdentIdentRequestFsmStageName
_CfprApIdentIdentRequestFsmStageName_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageName = _CfprApIdentIdentRequestFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 6),
    _CfprApIdentIdentRequestFsmStageName_Type()
)
cfprApIdentIdentRequestFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageName.setStatus("current")
_CfprApIdentIdentRequestFsmStageOrder_Type = Gauge32
_CfprApIdentIdentRequestFsmStageOrder_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageOrder = _CfprApIdentIdentRequestFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 7),
    _CfprApIdentIdentRequestFsmStageOrder_Type()
)
cfprApIdentIdentRequestFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageOrder.setStatus("current")
_CfprApIdentIdentRequestFsmStageRetry_Type = Gauge32
_CfprApIdentIdentRequestFsmStageRetry_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageRetry = _CfprApIdentIdentRequestFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 8),
    _CfprApIdentIdentRequestFsmStageRetry_Type()
)
cfprApIdentIdentRequestFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageRetry.setStatus("current")
_CfprApIdentIdentRequestFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApIdentIdentRequestFsmStageStageStatus_Object = MibTableColumn
cfprApIdentIdentRequestFsmStageStageStatus = _CfprApIdentIdentRequestFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 4, 1, 9),
    _CfprApIdentIdentRequestFsmStageStageStatus_Type()
)
cfprApIdentIdentRequestFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmStageStageStatus.setStatus("current")
_CfprApIdentIdentRequestFsmTaskTable_Object = MibTable
cfprApIdentIdentRequestFsmTaskTable = _CfprApIdentIdentRequestFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5)
)
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskTable.setStatus("current")
_CfprApIdentIdentRequestFsmTaskEntry_Object = MibTableRow
cfprApIdentIdentRequestFsmTaskEntry = _CfprApIdentIdentRequestFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5, 1)
)
cfprApIdentIdentRequestFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentIdentRequestFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskEntry.setStatus("current")
_CfprApIdentIdentRequestFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApIdentIdentRequestFsmTaskInstanceId_Object = MibTableColumn
cfprApIdentIdentRequestFsmTaskInstanceId = _CfprApIdentIdentRequestFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5, 1, 1),
    _CfprApIdentIdentRequestFsmTaskInstanceId_Type()
)
cfprApIdentIdentRequestFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskInstanceId.setStatus("current")
_CfprApIdentIdentRequestFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApIdentIdentRequestFsmTaskDn_Object = MibTableColumn
cfprApIdentIdentRequestFsmTaskDn = _CfprApIdentIdentRequestFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5, 1, 2),
    _CfprApIdentIdentRequestFsmTaskDn_Type()
)
cfprApIdentIdentRequestFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskDn.setStatus("current")
_CfprApIdentIdentRequestFsmTaskRn_Type = SnmpAdminString
_CfprApIdentIdentRequestFsmTaskRn_Object = MibTableColumn
cfprApIdentIdentRequestFsmTaskRn = _CfprApIdentIdentRequestFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5, 1, 3),
    _CfprApIdentIdentRequestFsmTaskRn_Type()
)
cfprApIdentIdentRequestFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskRn.setStatus("current")
_CfprApIdentIdentRequestFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApIdentIdentRequestFsmTaskCompletion_Object = MibTableColumn
cfprApIdentIdentRequestFsmTaskCompletion = _CfprApIdentIdentRequestFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5, 1, 4),
    _CfprApIdentIdentRequestFsmTaskCompletion_Type()
)
cfprApIdentIdentRequestFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskCompletion.setStatus("current")
_CfprApIdentIdentRequestFsmTaskFlags_Type = CfprApFsmFlags
_CfprApIdentIdentRequestFsmTaskFlags_Object = MibTableColumn
cfprApIdentIdentRequestFsmTaskFlags = _CfprApIdentIdentRequestFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5, 1, 5),
    _CfprApIdentIdentRequestFsmTaskFlags_Type()
)
cfprApIdentIdentRequestFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskFlags.setStatus("current")
_CfprApIdentIdentRequestFsmTaskItem_Type = CfprApIdentIdentRequestFsmTaskItem
_CfprApIdentIdentRequestFsmTaskItem_Object = MibTableColumn
cfprApIdentIdentRequestFsmTaskItem = _CfprApIdentIdentRequestFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5, 1, 6),
    _CfprApIdentIdentRequestFsmTaskItem_Type()
)
cfprApIdentIdentRequestFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskItem.setStatus("current")
_CfprApIdentIdentRequestFsmTaskSeqId_Type = Gauge32
_CfprApIdentIdentRequestFsmTaskSeqId_Object = MibTableColumn
cfprApIdentIdentRequestFsmTaskSeqId = _CfprApIdentIdentRequestFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 5, 1, 7),
    _CfprApIdentIdentRequestFsmTaskSeqId_Type()
)
cfprApIdentIdentRequestFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentIdentRequestFsmTaskSeqId.setStatus("current")
_CfprApIdentMetaSystemTable_Object = MibTable
cfprApIdentMetaSystemTable = _CfprApIdentMetaSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6)
)
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemTable.setStatus("current")
_CfprApIdentMetaSystemEntry_Object = MibTableRow
cfprApIdentMetaSystemEntry = _CfprApIdentMetaSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1)
)
cfprApIdentMetaSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentMetaSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemEntry.setStatus("current")
_CfprApIdentMetaSystemInstanceId_Type = CfprApManagedObjectId
_CfprApIdentMetaSystemInstanceId_Object = MibTableColumn
cfprApIdentMetaSystemInstanceId = _CfprApIdentMetaSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 1),
    _CfprApIdentMetaSystemInstanceId_Type()
)
cfprApIdentMetaSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemInstanceId.setStatus("current")
_CfprApIdentMetaSystemDn_Type = CfprApManagedObjectDn
_CfprApIdentMetaSystemDn_Object = MibTableColumn
cfprApIdentMetaSystemDn = _CfprApIdentMetaSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 2),
    _CfprApIdentMetaSystemDn_Type()
)
cfprApIdentMetaSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemDn.setStatus("current")
_CfprApIdentMetaSystemRn_Type = SnmpAdminString
_CfprApIdentMetaSystemRn_Object = MibTableColumn
cfprApIdentMetaSystemRn = _CfprApIdentMetaSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 3),
    _CfprApIdentMetaSystemRn_Type()
)
cfprApIdentMetaSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemRn.setStatus("current")
_CfprApIdentMetaSystemFsmDescr_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmDescr_Object = MibTableColumn
cfprApIdentMetaSystemFsmDescr = _CfprApIdentMetaSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 4),
    _CfprApIdentMetaSystemFsmDescr_Type()
)
cfprApIdentMetaSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmDescr.setStatus("current")
_CfprApIdentMetaSystemFsmPrev_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmPrev_Object = MibTableColumn
cfprApIdentMetaSystemFsmPrev = _CfprApIdentMetaSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 5),
    _CfprApIdentMetaSystemFsmPrev_Type()
)
cfprApIdentMetaSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmPrev.setStatus("current")
_CfprApIdentMetaSystemFsmProgr_Type = Gauge32
_CfprApIdentMetaSystemFsmProgr_Object = MibTableColumn
cfprApIdentMetaSystemFsmProgr = _CfprApIdentMetaSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 6),
    _CfprApIdentMetaSystemFsmProgr_Type()
)
cfprApIdentMetaSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmProgr.setStatus("current")
_CfprApIdentMetaSystemFsmRmtInvErrCode_Type = Gauge32
_CfprApIdentMetaSystemFsmRmtInvErrCode_Object = MibTableColumn
cfprApIdentMetaSystemFsmRmtInvErrCode = _CfprApIdentMetaSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 7),
    _CfprApIdentMetaSystemFsmRmtInvErrCode_Type()
)
cfprApIdentMetaSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmRmtInvErrCode.setStatus("current")
_CfprApIdentMetaSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmRmtInvErrDescr_Object = MibTableColumn
cfprApIdentMetaSystemFsmRmtInvErrDescr = _CfprApIdentMetaSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 8),
    _CfprApIdentMetaSystemFsmRmtInvErrDescr_Type()
)
cfprApIdentMetaSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmRmtInvErrDescr.setStatus("current")
_CfprApIdentMetaSystemFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApIdentMetaSystemFsmRmtInvRslt_Object = MibTableColumn
cfprApIdentMetaSystemFsmRmtInvRslt = _CfprApIdentMetaSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 9),
    _CfprApIdentMetaSystemFsmRmtInvRslt_Type()
)
cfprApIdentMetaSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmRmtInvRslt.setStatus("current")
_CfprApIdentMetaSystemFsmStageDescr_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmStageDescr_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageDescr = _CfprApIdentMetaSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 10),
    _CfprApIdentMetaSystemFsmStageDescr_Type()
)
cfprApIdentMetaSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageDescr.setStatus("current")
_CfprApIdentMetaSystemFsmStamp_Type = DateAndTime
_CfprApIdentMetaSystemFsmStamp_Object = MibTableColumn
cfprApIdentMetaSystemFsmStamp = _CfprApIdentMetaSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 11),
    _CfprApIdentMetaSystemFsmStamp_Type()
)
cfprApIdentMetaSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStamp.setStatus("current")
_CfprApIdentMetaSystemFsmStatus_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmStatus_Object = MibTableColumn
cfprApIdentMetaSystemFsmStatus = _CfprApIdentMetaSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 12),
    _CfprApIdentMetaSystemFsmStatus_Type()
)
cfprApIdentMetaSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStatus.setStatus("current")
_CfprApIdentMetaSystemFsmTry_Type = Gauge32
_CfprApIdentMetaSystemFsmTry_Object = MibTableColumn
cfprApIdentMetaSystemFsmTry = _CfprApIdentMetaSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 13),
    _CfprApIdentMetaSystemFsmTry_Type()
)
cfprApIdentMetaSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTry.setStatus("current")
_CfprApIdentMetaSystemGeneration_Type = Gauge32
_CfprApIdentMetaSystemGeneration_Object = MibTableColumn
cfprApIdentMetaSystemGeneration = _CfprApIdentMetaSystemGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 14),
    _CfprApIdentMetaSystemGeneration_Type()
)
cfprApIdentMetaSystemGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemGeneration.setStatus("current")
_CfprApIdentMetaSystemNextReqId_Type = Gauge32
_CfprApIdentMetaSystemNextReqId_Object = MibTableColumn
cfprApIdentMetaSystemNextReqId = _CfprApIdentMetaSystemNextReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 15),
    _CfprApIdentMetaSystemNextReqId_Type()
)
cfprApIdentMetaSystemNextReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemNextReqId.setStatus("current")
_CfprApIdentMetaSystemSysid_Type = Gauge32
_CfprApIdentMetaSystemSysid_Object = MibTableColumn
cfprApIdentMetaSystemSysid = _CfprApIdentMetaSystemSysid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 16),
    _CfprApIdentMetaSystemSysid_Type()
)
cfprApIdentMetaSystemSysid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemSysid.setStatus("current")
_CfprApIdentMetaSystemUcscGeneration_Type = Gauge32
_CfprApIdentMetaSystemUcscGeneration_Object = MibTableColumn
cfprApIdentMetaSystemUcscGeneration = _CfprApIdentMetaSystemUcscGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 6, 1, 17),
    _CfprApIdentMetaSystemUcscGeneration_Type()
)
cfprApIdentMetaSystemUcscGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemUcscGeneration.setStatus("current")
_CfprApIdentMetaSystemFsmTable_Object = MibTable
cfprApIdentMetaSystemFsmTable = _CfprApIdentMetaSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7)
)
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTable.setStatus("current")
_CfprApIdentMetaSystemFsmEntry_Object = MibTableRow
cfprApIdentMetaSystemFsmEntry = _CfprApIdentMetaSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1)
)
cfprApIdentMetaSystemFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentMetaSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmEntry.setStatus("current")
_CfprApIdentMetaSystemFsmInstanceId_Type = CfprApManagedObjectId
_CfprApIdentMetaSystemFsmInstanceId_Object = MibTableColumn
cfprApIdentMetaSystemFsmInstanceId = _CfprApIdentMetaSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 1),
    _CfprApIdentMetaSystemFsmInstanceId_Type()
)
cfprApIdentMetaSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmInstanceId.setStatus("current")
_CfprApIdentMetaSystemFsmDn_Type = CfprApManagedObjectDn
_CfprApIdentMetaSystemFsmDn_Object = MibTableColumn
cfprApIdentMetaSystemFsmDn = _CfprApIdentMetaSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 2),
    _CfprApIdentMetaSystemFsmDn_Type()
)
cfprApIdentMetaSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmDn.setStatus("current")
_CfprApIdentMetaSystemFsmRn_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmRn_Object = MibTableColumn
cfprApIdentMetaSystemFsmRn = _CfprApIdentMetaSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 3),
    _CfprApIdentMetaSystemFsmRn_Type()
)
cfprApIdentMetaSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmRn.setStatus("current")
_CfprApIdentMetaSystemFsmCompletionTime_Type = DateAndTime
_CfprApIdentMetaSystemFsmCompletionTime_Object = MibTableColumn
cfprApIdentMetaSystemFsmCompletionTime = _CfprApIdentMetaSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 4),
    _CfprApIdentMetaSystemFsmCompletionTime_Type()
)
cfprApIdentMetaSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmCompletionTime.setStatus("current")
_CfprApIdentMetaSystemFsmCurrentFsm_Type = CfprApIdentMetaSystemFsmCurrentFsm
_CfprApIdentMetaSystemFsmCurrentFsm_Object = MibTableColumn
cfprApIdentMetaSystemFsmCurrentFsm = _CfprApIdentMetaSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 5),
    _CfprApIdentMetaSystemFsmCurrentFsm_Type()
)
cfprApIdentMetaSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmCurrentFsm.setStatus("current")
_CfprApIdentMetaSystemFsmDescrData_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmDescrData_Object = MibTableColumn
cfprApIdentMetaSystemFsmDescrData = _CfprApIdentMetaSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 6),
    _CfprApIdentMetaSystemFsmDescrData_Type()
)
cfprApIdentMetaSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmDescrData.setStatus("current")
_CfprApIdentMetaSystemFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApIdentMetaSystemFsmFsmStatus_Object = MibTableColumn
cfprApIdentMetaSystemFsmFsmStatus = _CfprApIdentMetaSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 7),
    _CfprApIdentMetaSystemFsmFsmStatus_Type()
)
cfprApIdentMetaSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmFsmStatus.setStatus("current")
_CfprApIdentMetaSystemFsmProgress_Type = Gauge32
_CfprApIdentMetaSystemFsmProgress_Object = MibTableColumn
cfprApIdentMetaSystemFsmProgress = _CfprApIdentMetaSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 8),
    _CfprApIdentMetaSystemFsmProgress_Type()
)
cfprApIdentMetaSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmProgress.setStatus("current")
_CfprApIdentMetaSystemFsmRmtErrCode_Type = Gauge32
_CfprApIdentMetaSystemFsmRmtErrCode_Object = MibTableColumn
cfprApIdentMetaSystemFsmRmtErrCode = _CfprApIdentMetaSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 9),
    _CfprApIdentMetaSystemFsmRmtErrCode_Type()
)
cfprApIdentMetaSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmRmtErrCode.setStatus("current")
_CfprApIdentMetaSystemFsmRmtErrDescr_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmRmtErrDescr_Object = MibTableColumn
cfprApIdentMetaSystemFsmRmtErrDescr = _CfprApIdentMetaSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 10),
    _CfprApIdentMetaSystemFsmRmtErrDescr_Type()
)
cfprApIdentMetaSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmRmtErrDescr.setStatus("current")
_CfprApIdentMetaSystemFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApIdentMetaSystemFsmRmtRslt_Object = MibTableColumn
cfprApIdentMetaSystemFsmRmtRslt = _CfprApIdentMetaSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 7, 1, 11),
    _CfprApIdentMetaSystemFsmRmtRslt_Type()
)
cfprApIdentMetaSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmRmtRslt.setStatus("current")
_CfprApIdentMetaSystemFsmStageTable_Object = MibTable
cfprApIdentMetaSystemFsmStageTable = _CfprApIdentMetaSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8)
)
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageTable.setStatus("current")
_CfprApIdentMetaSystemFsmStageEntry_Object = MibTableRow
cfprApIdentMetaSystemFsmStageEntry = _CfprApIdentMetaSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1)
)
cfprApIdentMetaSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentMetaSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageEntry.setStatus("current")
_CfprApIdentMetaSystemFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApIdentMetaSystemFsmStageInstanceId_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageInstanceId = _CfprApIdentMetaSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 1),
    _CfprApIdentMetaSystemFsmStageInstanceId_Type()
)
cfprApIdentMetaSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageInstanceId.setStatus("current")
_CfprApIdentMetaSystemFsmStageDn_Type = CfprApManagedObjectDn
_CfprApIdentMetaSystemFsmStageDn_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageDn = _CfprApIdentMetaSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 2),
    _CfprApIdentMetaSystemFsmStageDn_Type()
)
cfprApIdentMetaSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageDn.setStatus("current")
_CfprApIdentMetaSystemFsmStageRn_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmStageRn_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageRn = _CfprApIdentMetaSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 3),
    _CfprApIdentMetaSystemFsmStageRn_Type()
)
cfprApIdentMetaSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageRn.setStatus("current")
_CfprApIdentMetaSystemFsmStageDescrData_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmStageDescrData_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageDescrData = _CfprApIdentMetaSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 4),
    _CfprApIdentMetaSystemFsmStageDescrData_Type()
)
cfprApIdentMetaSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageDescrData.setStatus("current")
_CfprApIdentMetaSystemFsmStageLastUpdateTime_Type = DateAndTime
_CfprApIdentMetaSystemFsmStageLastUpdateTime_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageLastUpdateTime = _CfprApIdentMetaSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 5),
    _CfprApIdentMetaSystemFsmStageLastUpdateTime_Type()
)
cfprApIdentMetaSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageLastUpdateTime.setStatus("current")
_CfprApIdentMetaSystemFsmStageName_Type = CfprApIdentMetaSystemFsmStageName
_CfprApIdentMetaSystemFsmStageName_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageName = _CfprApIdentMetaSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 6),
    _CfprApIdentMetaSystemFsmStageName_Type()
)
cfprApIdentMetaSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageName.setStatus("current")
_CfprApIdentMetaSystemFsmStageOrder_Type = Gauge32
_CfprApIdentMetaSystemFsmStageOrder_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageOrder = _CfprApIdentMetaSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 7),
    _CfprApIdentMetaSystemFsmStageOrder_Type()
)
cfprApIdentMetaSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageOrder.setStatus("current")
_CfprApIdentMetaSystemFsmStageRetry_Type = Gauge32
_CfprApIdentMetaSystemFsmStageRetry_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageRetry = _CfprApIdentMetaSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 8),
    _CfprApIdentMetaSystemFsmStageRetry_Type()
)
cfprApIdentMetaSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageRetry.setStatus("current")
_CfprApIdentMetaSystemFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApIdentMetaSystemFsmStageStageStatus_Object = MibTableColumn
cfprApIdentMetaSystemFsmStageStageStatus = _CfprApIdentMetaSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 8, 1, 9),
    _CfprApIdentMetaSystemFsmStageStageStatus_Type()
)
cfprApIdentMetaSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmStageStageStatus.setStatus("current")
_CfprApIdentMetaSystemFsmTaskTable_Object = MibTable
cfprApIdentMetaSystemFsmTaskTable = _CfprApIdentMetaSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9)
)
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskTable.setStatus("current")
_CfprApIdentMetaSystemFsmTaskEntry_Object = MibTableRow
cfprApIdentMetaSystemFsmTaskEntry = _CfprApIdentMetaSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9, 1)
)
cfprApIdentMetaSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentMetaSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskEntry.setStatus("current")
_CfprApIdentMetaSystemFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApIdentMetaSystemFsmTaskInstanceId_Object = MibTableColumn
cfprApIdentMetaSystemFsmTaskInstanceId = _CfprApIdentMetaSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9, 1, 1),
    _CfprApIdentMetaSystemFsmTaskInstanceId_Type()
)
cfprApIdentMetaSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskInstanceId.setStatus("current")
_CfprApIdentMetaSystemFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApIdentMetaSystemFsmTaskDn_Object = MibTableColumn
cfprApIdentMetaSystemFsmTaskDn = _CfprApIdentMetaSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9, 1, 2),
    _CfprApIdentMetaSystemFsmTaskDn_Type()
)
cfprApIdentMetaSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskDn.setStatus("current")
_CfprApIdentMetaSystemFsmTaskRn_Type = SnmpAdminString
_CfprApIdentMetaSystemFsmTaskRn_Object = MibTableColumn
cfprApIdentMetaSystemFsmTaskRn = _CfprApIdentMetaSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9, 1, 3),
    _CfprApIdentMetaSystemFsmTaskRn_Type()
)
cfprApIdentMetaSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskRn.setStatus("current")
_CfprApIdentMetaSystemFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApIdentMetaSystemFsmTaskCompletion_Object = MibTableColumn
cfprApIdentMetaSystemFsmTaskCompletion = _CfprApIdentMetaSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9, 1, 4),
    _CfprApIdentMetaSystemFsmTaskCompletion_Type()
)
cfprApIdentMetaSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskCompletion.setStatus("current")
_CfprApIdentMetaSystemFsmTaskFlags_Type = CfprApFsmFlags
_CfprApIdentMetaSystemFsmTaskFlags_Object = MibTableColumn
cfprApIdentMetaSystemFsmTaskFlags = _CfprApIdentMetaSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9, 1, 5),
    _CfprApIdentMetaSystemFsmTaskFlags_Type()
)
cfprApIdentMetaSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskFlags.setStatus("current")
_CfprApIdentMetaSystemFsmTaskItem_Type = CfprApIdentMetaSystemFsmTaskItem
_CfprApIdentMetaSystemFsmTaskItem_Object = MibTableColumn
cfprApIdentMetaSystemFsmTaskItem = _CfprApIdentMetaSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9, 1, 6),
    _CfprApIdentMetaSystemFsmTaskItem_Type()
)
cfprApIdentMetaSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskItem.setStatus("current")
_CfprApIdentMetaSystemFsmTaskSeqId_Type = Gauge32
_CfprApIdentMetaSystemFsmTaskSeqId_Object = MibTableColumn
cfprApIdentMetaSystemFsmTaskSeqId = _CfprApIdentMetaSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 9, 1, 7),
    _CfprApIdentMetaSystemFsmTaskSeqId_Type()
)
cfprApIdentMetaSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaSystemFsmTaskSeqId.setStatus("current")
_CfprApIdentMetaVerseTable_Object = MibTable
cfprApIdentMetaVerseTable = _CfprApIdentMetaVerseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 10)
)
if mibBuilder.loadTexts:
    cfprApIdentMetaVerseTable.setStatus("current")
_CfprApIdentMetaVerseEntry_Object = MibTableRow
cfprApIdentMetaVerseEntry = _CfprApIdentMetaVerseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 10, 1)
)
cfprApIdentMetaVerseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentMetaVerseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentMetaVerseEntry.setStatus("current")
_CfprApIdentMetaVerseInstanceId_Type = CfprApManagedObjectId
_CfprApIdentMetaVerseInstanceId_Object = MibTableColumn
cfprApIdentMetaVerseInstanceId = _CfprApIdentMetaVerseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 10, 1, 1),
    _CfprApIdentMetaVerseInstanceId_Type()
)
cfprApIdentMetaVerseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentMetaVerseInstanceId.setStatus("current")
_CfprApIdentMetaVerseDn_Type = CfprApManagedObjectDn
_CfprApIdentMetaVerseDn_Object = MibTableColumn
cfprApIdentMetaVerseDn = _CfprApIdentMetaVerseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 10, 1, 2),
    _CfprApIdentMetaVerseDn_Type()
)
cfprApIdentMetaVerseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaVerseDn.setStatus("current")
_CfprApIdentMetaVerseRn_Type = SnmpAdminString
_CfprApIdentMetaVerseRn_Object = MibTableColumn
cfprApIdentMetaVerseRn = _CfprApIdentMetaVerseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 10, 1, 3),
    _CfprApIdentMetaVerseRn_Type()
)
cfprApIdentMetaVerseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentMetaVerseRn.setStatus("current")
_CfprApIdentRequestEpTable_Object = MibTable
cfprApIdentRequestEpTable = _CfprApIdentRequestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 11)
)
if mibBuilder.loadTexts:
    cfprApIdentRequestEpTable.setStatus("current")
_CfprApIdentRequestEpEntry_Object = MibTableRow
cfprApIdentRequestEpEntry = _CfprApIdentRequestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 11, 1)
)
cfprApIdentRequestEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentRequestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentRequestEpEntry.setStatus("current")
_CfprApIdentRequestEpInstanceId_Type = CfprApManagedObjectId
_CfprApIdentRequestEpInstanceId_Object = MibTableColumn
cfprApIdentRequestEpInstanceId = _CfprApIdentRequestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 11, 1, 1),
    _CfprApIdentRequestEpInstanceId_Type()
)
cfprApIdentRequestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentRequestEpInstanceId.setStatus("current")
_CfprApIdentRequestEpDn_Type = CfprApManagedObjectDn
_CfprApIdentRequestEpDn_Object = MibTableColumn
cfprApIdentRequestEpDn = _CfprApIdentRequestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 11, 1, 2),
    _CfprApIdentRequestEpDn_Type()
)
cfprApIdentRequestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentRequestEpDn.setStatus("current")
_CfprApIdentRequestEpRn_Type = SnmpAdminString
_CfprApIdentRequestEpRn_Object = MibTableColumn
cfprApIdentRequestEpRn = _CfprApIdentRequestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 11, 1, 3),
    _CfprApIdentRequestEpRn_Type()
)
cfprApIdentRequestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentRequestEpRn.setStatus("current")
_CfprApIdentRequestEpReqDn_Type = SnmpAdminString
_CfprApIdentRequestEpReqDn_Object = MibTableColumn
cfprApIdentRequestEpReqDn = _CfprApIdentRequestEpReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 11, 1, 4),
    _CfprApIdentRequestEpReqDn_Type()
)
cfprApIdentRequestEpReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentRequestEpReqDn.setStatus("current")
_CfprApIdentRequestEpReqId_Type = Gauge32
_CfprApIdentRequestEpReqId_Object = MibTableColumn
cfprApIdentRequestEpReqId = _CfprApIdentRequestEpReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 11, 1, 5),
    _CfprApIdentRequestEpReqId_Type()
)
cfprApIdentRequestEpReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentRequestEpReqId.setStatus("current")
_CfprApIdentSysInfoTable_Object = MibTable
cfprApIdentSysInfoTable = _CfprApIdentSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12)
)
if mibBuilder.loadTexts:
    cfprApIdentSysInfoTable.setStatus("current")
_CfprApIdentSysInfoEntry_Object = MibTableRow
cfprApIdentSysInfoEntry = _CfprApIdentSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1)
)
cfprApIdentSysInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IDENT-MIB", "cfprApIdentSysInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIdentSysInfoEntry.setStatus("current")
_CfprApIdentSysInfoInstanceId_Type = CfprApManagedObjectId
_CfprApIdentSysInfoInstanceId_Object = MibTableColumn
cfprApIdentSysInfoInstanceId = _CfprApIdentSysInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1, 1),
    _CfprApIdentSysInfoInstanceId_Type()
)
cfprApIdentSysInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIdentSysInfoInstanceId.setStatus("current")
_CfprApIdentSysInfoDn_Type = CfprApManagedObjectDn
_CfprApIdentSysInfoDn_Object = MibTableColumn
cfprApIdentSysInfoDn = _CfprApIdentSysInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1, 2),
    _CfprApIdentSysInfoDn_Type()
)
cfprApIdentSysInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentSysInfoDn.setStatus("current")
_CfprApIdentSysInfoRn_Type = SnmpAdminString
_CfprApIdentSysInfoRn_Object = MibTableColumn
cfprApIdentSysInfoRn = _CfprApIdentSysInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1, 3),
    _CfprApIdentSysInfoRn_Type()
)
cfprApIdentSysInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentSysInfoRn.setStatus("current")
_CfprApIdentSysInfoGeneration_Type = Gauge32
_CfprApIdentSysInfoGeneration_Object = MibTableColumn
cfprApIdentSysInfoGeneration = _CfprApIdentSysInfoGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1, 4),
    _CfprApIdentSysInfoGeneration_Type()
)
cfprApIdentSysInfoGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentSysInfoGeneration.setStatus("current")
_CfprApIdentSysInfoIsFirstSync_Type = TruthValue
_CfprApIdentSysInfoIsFirstSync_Object = MibTableColumn
cfprApIdentSysInfoIsFirstSync = _CfprApIdentSysInfoIsFirstSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1, 5),
    _CfprApIdentSysInfoIsFirstSync_Type()
)
cfprApIdentSysInfoIsFirstSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentSysInfoIsFirstSync.setStatus("current")
_CfprApIdentSysInfoIsSync_Type = TruthValue
_CfprApIdentSysInfoIsSync_Object = MibTableColumn
cfprApIdentSysInfoIsSync = _CfprApIdentSysInfoIsSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1, 6),
    _CfprApIdentSysInfoIsSync_Type()
)
cfprApIdentSysInfoIsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentSysInfoIsSync.setStatus("current")
_CfprApIdentSysInfoIsSyncAllowed_Type = TruthValue
_CfprApIdentSysInfoIsSyncAllowed_Object = MibTableColumn
cfprApIdentSysInfoIsSyncAllowed = _CfprApIdentSysInfoIsSyncAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1, 7),
    _CfprApIdentSysInfoIsSyncAllowed_Type()
)
cfprApIdentSysInfoIsSyncAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentSysInfoIsSyncAllowed.setStatus("current")
_CfprApIdentSysInfoUcscGeneration_Type = Gauge32
_CfprApIdentSysInfoUcscGeneration_Object = MibTableColumn
cfprApIdentSysInfoUcscGeneration = _CfprApIdentSysInfoUcscGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 36, 12, 1, 8),
    _CfprApIdentSysInfoUcscGeneration_Type()
)
cfprApIdentSysInfoUcscGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIdentSysInfoUcscGeneration.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-IDENT-MIB",
    **{"cfprApIdentObjects": cfprApIdentObjects,
       "cfprApIdentIdentCtxTable": cfprApIdentIdentCtxTable,
       "cfprApIdentIdentCtxEntry": cfprApIdentIdentCtxEntry,
       "cfprApIdentIdentCtxInstanceId": cfprApIdentIdentCtxInstanceId,
       "cfprApIdentIdentCtxDn": cfprApIdentIdentCtxDn,
       "cfprApIdentIdentCtxRn": cfprApIdentIdentCtxRn,
       "cfprApIdentIdentCtxAssigned": cfprApIdentIdentCtxAssigned,
       "cfprApIdentIdentCtxConsDn": cfprApIdentIdentCtxConsDn,
       "cfprApIdentIdentCtxConsType": cfprApIdentIdentCtxConsType,
       "cfprApIdentIdentCtxDefinedInIdm": cfprApIdentIdentCtxDefinedInIdm,
       "cfprApIdentIdentCtxGlobalAssignedCnt": cfprApIdentIdentCtxGlobalAssignedCnt,
       "cfprApIdentIdentCtxGlobalDefinedCnt": cfprApIdentIdentCtxGlobalDefinedCnt,
       "cfprApIdentIdentCtxIdentPoolName": cfprApIdentIdentCtxIdentPoolName,
       "cfprApIdentIdentCtxIdentType": cfprApIdentIdentCtxIdentType,
       "cfprApIdentIdentCtxIntent": cfprApIdentIdentCtxIntent,
       "cfprApIdentIdentCtxIsAssignedLocally": cfprApIdentIdentCtxIsAssignedLocally,
       "cfprApIdentIdentCtxPoolDn": cfprApIdentIdentCtxPoolDn,
       "cfprApIdentIdentCtxPoolOrgDn": cfprApIdentIdentCtxPoolOrgDn,
       "cfprApIdentIdentCtxPooledId": cfprApIdentIdentCtxPooledId,
       "cfprApIdentIdentCtxRetStatus": cfprApIdentIdentCtxRetStatus,
       "cfprApIdentIdentCtxSeqNum": cfprApIdentIdentCtxSeqNum,
       "cfprApIdentIdentCtxSupplId1": cfprApIdentIdentCtxSupplId1,
       "cfprApIdentIdentCtxSupplId2": cfprApIdentIdentCtxSupplId2,
       "cfprApIdentIdentCtxSupplId3": cfprApIdentIdentCtxSupplId3,
       "cfprApIdentIdentCtxSupplId4": cfprApIdentIdentCtxSupplId4,
       "cfprApIdentIdentRequestTable": cfprApIdentIdentRequestTable,
       "cfprApIdentIdentRequestEntry": cfprApIdentIdentRequestEntry,
       "cfprApIdentIdentRequestInstanceId": cfprApIdentIdentRequestInstanceId,
       "cfprApIdentIdentRequestDn": cfprApIdentIdentRequestDn,
       "cfprApIdentIdentRequestRn": cfprApIdentIdentRequestRn,
       "cfprApIdentIdentRequestEpDn": cfprApIdentIdentRequestEpDn,
       "cfprApIdentIdentRequestFsmDescr": cfprApIdentIdentRequestFsmDescr,
       "cfprApIdentIdentRequestFsmPrev": cfprApIdentIdentRequestFsmPrev,
       "cfprApIdentIdentRequestFsmProgr": cfprApIdentIdentRequestFsmProgr,
       "cfprApIdentIdentRequestFsmRmtInvErrCode": cfprApIdentIdentRequestFsmRmtInvErrCode,
       "cfprApIdentIdentRequestFsmRmtInvErrDescr": cfprApIdentIdentRequestFsmRmtInvErrDescr,
       "cfprApIdentIdentRequestFsmRmtInvRslt": cfprApIdentIdentRequestFsmRmtInvRslt,
       "cfprApIdentIdentRequestFsmStageDescr": cfprApIdentIdentRequestFsmStageDescr,
       "cfprApIdentIdentRequestFsmStamp": cfprApIdentIdentRequestFsmStamp,
       "cfprApIdentIdentRequestFsmStatus": cfprApIdentIdentRequestFsmStatus,
       "cfprApIdentIdentRequestFsmTry": cfprApIdentIdentRequestFsmTry,
       "cfprApIdentIdentRequestId": cfprApIdentIdentRequestId,
       "cfprApIdentIdentRequestRequestSize": cfprApIdentIdentRequestRequestSize,
       "cfprApIdentIdentRequestSeqNum": cfprApIdentIdentRequestSeqNum,
       "cfprApIdentIdentRequestFsmTable": cfprApIdentIdentRequestFsmTable,
       "cfprApIdentIdentRequestFsmEntry": cfprApIdentIdentRequestFsmEntry,
       "cfprApIdentIdentRequestFsmInstanceId": cfprApIdentIdentRequestFsmInstanceId,
       "cfprApIdentIdentRequestFsmDn": cfprApIdentIdentRequestFsmDn,
       "cfprApIdentIdentRequestFsmRn": cfprApIdentIdentRequestFsmRn,
       "cfprApIdentIdentRequestFsmCompletionTime": cfprApIdentIdentRequestFsmCompletionTime,
       "cfprApIdentIdentRequestFsmCurrentFsm": cfprApIdentIdentRequestFsmCurrentFsm,
       "cfprApIdentIdentRequestFsmDescrData": cfprApIdentIdentRequestFsmDescrData,
       "cfprApIdentIdentRequestFsmFsmStatus": cfprApIdentIdentRequestFsmFsmStatus,
       "cfprApIdentIdentRequestFsmProgress": cfprApIdentIdentRequestFsmProgress,
       "cfprApIdentIdentRequestFsmRmtErrCode": cfprApIdentIdentRequestFsmRmtErrCode,
       "cfprApIdentIdentRequestFsmRmtErrDescr": cfprApIdentIdentRequestFsmRmtErrDescr,
       "cfprApIdentIdentRequestFsmRmtRslt": cfprApIdentIdentRequestFsmRmtRslt,
       "cfprApIdentIdentRequestFsmStageTable": cfprApIdentIdentRequestFsmStageTable,
       "cfprApIdentIdentRequestFsmStageEntry": cfprApIdentIdentRequestFsmStageEntry,
       "cfprApIdentIdentRequestFsmStageInstanceId": cfprApIdentIdentRequestFsmStageInstanceId,
       "cfprApIdentIdentRequestFsmStageDn": cfprApIdentIdentRequestFsmStageDn,
       "cfprApIdentIdentRequestFsmStageRn": cfprApIdentIdentRequestFsmStageRn,
       "cfprApIdentIdentRequestFsmStageDescrData": cfprApIdentIdentRequestFsmStageDescrData,
       "cfprApIdentIdentRequestFsmStageLastUpdateTime": cfprApIdentIdentRequestFsmStageLastUpdateTime,
       "cfprApIdentIdentRequestFsmStageName": cfprApIdentIdentRequestFsmStageName,
       "cfprApIdentIdentRequestFsmStageOrder": cfprApIdentIdentRequestFsmStageOrder,
       "cfprApIdentIdentRequestFsmStageRetry": cfprApIdentIdentRequestFsmStageRetry,
       "cfprApIdentIdentRequestFsmStageStageStatus": cfprApIdentIdentRequestFsmStageStageStatus,
       "cfprApIdentIdentRequestFsmTaskTable": cfprApIdentIdentRequestFsmTaskTable,
       "cfprApIdentIdentRequestFsmTaskEntry": cfprApIdentIdentRequestFsmTaskEntry,
       "cfprApIdentIdentRequestFsmTaskInstanceId": cfprApIdentIdentRequestFsmTaskInstanceId,
       "cfprApIdentIdentRequestFsmTaskDn": cfprApIdentIdentRequestFsmTaskDn,
       "cfprApIdentIdentRequestFsmTaskRn": cfprApIdentIdentRequestFsmTaskRn,
       "cfprApIdentIdentRequestFsmTaskCompletion": cfprApIdentIdentRequestFsmTaskCompletion,
       "cfprApIdentIdentRequestFsmTaskFlags": cfprApIdentIdentRequestFsmTaskFlags,
       "cfprApIdentIdentRequestFsmTaskItem": cfprApIdentIdentRequestFsmTaskItem,
       "cfprApIdentIdentRequestFsmTaskSeqId": cfprApIdentIdentRequestFsmTaskSeqId,
       "cfprApIdentMetaSystemTable": cfprApIdentMetaSystemTable,
       "cfprApIdentMetaSystemEntry": cfprApIdentMetaSystemEntry,
       "cfprApIdentMetaSystemInstanceId": cfprApIdentMetaSystemInstanceId,
       "cfprApIdentMetaSystemDn": cfprApIdentMetaSystemDn,
       "cfprApIdentMetaSystemRn": cfprApIdentMetaSystemRn,
       "cfprApIdentMetaSystemFsmDescr": cfprApIdentMetaSystemFsmDescr,
       "cfprApIdentMetaSystemFsmPrev": cfprApIdentMetaSystemFsmPrev,
       "cfprApIdentMetaSystemFsmProgr": cfprApIdentMetaSystemFsmProgr,
       "cfprApIdentMetaSystemFsmRmtInvErrCode": cfprApIdentMetaSystemFsmRmtInvErrCode,
       "cfprApIdentMetaSystemFsmRmtInvErrDescr": cfprApIdentMetaSystemFsmRmtInvErrDescr,
       "cfprApIdentMetaSystemFsmRmtInvRslt": cfprApIdentMetaSystemFsmRmtInvRslt,
       "cfprApIdentMetaSystemFsmStageDescr": cfprApIdentMetaSystemFsmStageDescr,
       "cfprApIdentMetaSystemFsmStamp": cfprApIdentMetaSystemFsmStamp,
       "cfprApIdentMetaSystemFsmStatus": cfprApIdentMetaSystemFsmStatus,
       "cfprApIdentMetaSystemFsmTry": cfprApIdentMetaSystemFsmTry,
       "cfprApIdentMetaSystemGeneration": cfprApIdentMetaSystemGeneration,
       "cfprApIdentMetaSystemNextReqId": cfprApIdentMetaSystemNextReqId,
       "cfprApIdentMetaSystemSysid": cfprApIdentMetaSystemSysid,
       "cfprApIdentMetaSystemUcscGeneration": cfprApIdentMetaSystemUcscGeneration,
       "cfprApIdentMetaSystemFsmTable": cfprApIdentMetaSystemFsmTable,
       "cfprApIdentMetaSystemFsmEntry": cfprApIdentMetaSystemFsmEntry,
       "cfprApIdentMetaSystemFsmInstanceId": cfprApIdentMetaSystemFsmInstanceId,
       "cfprApIdentMetaSystemFsmDn": cfprApIdentMetaSystemFsmDn,
       "cfprApIdentMetaSystemFsmRn": cfprApIdentMetaSystemFsmRn,
       "cfprApIdentMetaSystemFsmCompletionTime": cfprApIdentMetaSystemFsmCompletionTime,
       "cfprApIdentMetaSystemFsmCurrentFsm": cfprApIdentMetaSystemFsmCurrentFsm,
       "cfprApIdentMetaSystemFsmDescrData": cfprApIdentMetaSystemFsmDescrData,
       "cfprApIdentMetaSystemFsmFsmStatus": cfprApIdentMetaSystemFsmFsmStatus,
       "cfprApIdentMetaSystemFsmProgress": cfprApIdentMetaSystemFsmProgress,
       "cfprApIdentMetaSystemFsmRmtErrCode": cfprApIdentMetaSystemFsmRmtErrCode,
       "cfprApIdentMetaSystemFsmRmtErrDescr": cfprApIdentMetaSystemFsmRmtErrDescr,
       "cfprApIdentMetaSystemFsmRmtRslt": cfprApIdentMetaSystemFsmRmtRslt,
       "cfprApIdentMetaSystemFsmStageTable": cfprApIdentMetaSystemFsmStageTable,
       "cfprApIdentMetaSystemFsmStageEntry": cfprApIdentMetaSystemFsmStageEntry,
       "cfprApIdentMetaSystemFsmStageInstanceId": cfprApIdentMetaSystemFsmStageInstanceId,
       "cfprApIdentMetaSystemFsmStageDn": cfprApIdentMetaSystemFsmStageDn,
       "cfprApIdentMetaSystemFsmStageRn": cfprApIdentMetaSystemFsmStageRn,
       "cfprApIdentMetaSystemFsmStageDescrData": cfprApIdentMetaSystemFsmStageDescrData,
       "cfprApIdentMetaSystemFsmStageLastUpdateTime": cfprApIdentMetaSystemFsmStageLastUpdateTime,
       "cfprApIdentMetaSystemFsmStageName": cfprApIdentMetaSystemFsmStageName,
       "cfprApIdentMetaSystemFsmStageOrder": cfprApIdentMetaSystemFsmStageOrder,
       "cfprApIdentMetaSystemFsmStageRetry": cfprApIdentMetaSystemFsmStageRetry,
       "cfprApIdentMetaSystemFsmStageStageStatus": cfprApIdentMetaSystemFsmStageStageStatus,
       "cfprApIdentMetaSystemFsmTaskTable": cfprApIdentMetaSystemFsmTaskTable,
       "cfprApIdentMetaSystemFsmTaskEntry": cfprApIdentMetaSystemFsmTaskEntry,
       "cfprApIdentMetaSystemFsmTaskInstanceId": cfprApIdentMetaSystemFsmTaskInstanceId,
       "cfprApIdentMetaSystemFsmTaskDn": cfprApIdentMetaSystemFsmTaskDn,
       "cfprApIdentMetaSystemFsmTaskRn": cfprApIdentMetaSystemFsmTaskRn,
       "cfprApIdentMetaSystemFsmTaskCompletion": cfprApIdentMetaSystemFsmTaskCompletion,
       "cfprApIdentMetaSystemFsmTaskFlags": cfprApIdentMetaSystemFsmTaskFlags,
       "cfprApIdentMetaSystemFsmTaskItem": cfprApIdentMetaSystemFsmTaskItem,
       "cfprApIdentMetaSystemFsmTaskSeqId": cfprApIdentMetaSystemFsmTaskSeqId,
       "cfprApIdentMetaVerseTable": cfprApIdentMetaVerseTable,
       "cfprApIdentMetaVerseEntry": cfprApIdentMetaVerseEntry,
       "cfprApIdentMetaVerseInstanceId": cfprApIdentMetaVerseInstanceId,
       "cfprApIdentMetaVerseDn": cfprApIdentMetaVerseDn,
       "cfprApIdentMetaVerseRn": cfprApIdentMetaVerseRn,
       "cfprApIdentRequestEpTable": cfprApIdentRequestEpTable,
       "cfprApIdentRequestEpEntry": cfprApIdentRequestEpEntry,
       "cfprApIdentRequestEpInstanceId": cfprApIdentRequestEpInstanceId,
       "cfprApIdentRequestEpDn": cfprApIdentRequestEpDn,
       "cfprApIdentRequestEpRn": cfprApIdentRequestEpRn,
       "cfprApIdentRequestEpReqDn": cfprApIdentRequestEpReqDn,
       "cfprApIdentRequestEpReqId": cfprApIdentRequestEpReqId,
       "cfprApIdentSysInfoTable": cfprApIdentSysInfoTable,
       "cfprApIdentSysInfoEntry": cfprApIdentSysInfoEntry,
       "cfprApIdentSysInfoInstanceId": cfprApIdentSysInfoInstanceId,
       "cfprApIdentSysInfoDn": cfprApIdentSysInfoDn,
       "cfprApIdentSysInfoRn": cfprApIdentSysInfoRn,
       "cfprApIdentSysInfoGeneration": cfprApIdentSysInfoGeneration,
       "cfprApIdentSysInfoIsFirstSync": cfprApIdentSysInfoIsFirstSync,
       "cfprApIdentSysInfoIsSync": cfprApIdentSysInfoIsSync,
       "cfprApIdentSysInfoIsSyncAllowed": cfprApIdentSysInfoIsSyncAllowed,
       "cfprApIdentSysInfoUcscGeneration": cfprApIdentSysInfoUcscGeneration}
)
