# SNMP MIB module (CISCO-FIREPOWER-IDENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-IDENT-MIB.mib
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

(CfprConditionRemoteInvRslt,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprIdentConsType,
 CfprIdentIdDefinedInIdm,
 CfprIdentIdentReqIntent,
 CfprIdentIdentRequestFsmCurrentFsm,
 CfprIdentIdentRequestFsmStageName,
 CfprIdentIdentRequestFsmTaskItem,
 CfprIdentIdentType,
 CfprIdentMetaSystemFsmCurrentFsm,
 CfprIdentMetaSystemFsmStageName,
 CfprIdentMetaSystemFsmTaskItem,
 CfprIdentRetStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprIdentConsType",
    "CfprIdentIdDefinedInIdm",
    "CfprIdentIdentReqIntent",
    "CfprIdentIdentRequestFsmCurrentFsm",
    "CfprIdentIdentRequestFsmStageName",
    "CfprIdentIdentRequestFsmTaskItem",
    "CfprIdentIdentType",
    "CfprIdentMetaSystemFsmCurrentFsm",
    "CfprIdentMetaSystemFsmStageName",
    "CfprIdentMetaSystemFsmTaskItem",
    "CfprIdentRetStatus")

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

cfprIdentObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprIdentIdentCtxTable_Object = MibTable
cfprIdentIdentCtxTable = _CfprIdentIdentCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1)
)
if mibBuilder.loadTexts:
    cfprIdentIdentCtxTable.setStatus("current")
_CfprIdentIdentCtxEntry_Object = MibTableRow
cfprIdentIdentCtxEntry = _CfprIdentIdentCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1)
)
cfprIdentIdentCtxEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentIdentCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentIdentCtxEntry.setStatus("current")
_CfprIdentIdentCtxInstanceId_Type = CfprManagedObjectId
_CfprIdentIdentCtxInstanceId_Object = MibTableColumn
cfprIdentIdentCtxInstanceId = _CfprIdentIdentCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 1),
    _CfprIdentIdentCtxInstanceId_Type()
)
cfprIdentIdentCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxInstanceId.setStatus("current")
_CfprIdentIdentCtxDn_Type = CfprManagedObjectDn
_CfprIdentIdentCtxDn_Object = MibTableColumn
cfprIdentIdentCtxDn = _CfprIdentIdentCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 2),
    _CfprIdentIdentCtxDn_Type()
)
cfprIdentIdentCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxDn.setStatus("current")
_CfprIdentIdentCtxRn_Type = SnmpAdminString
_CfprIdentIdentCtxRn_Object = MibTableColumn
cfprIdentIdentCtxRn = _CfprIdentIdentCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 3),
    _CfprIdentIdentCtxRn_Type()
)
cfprIdentIdentCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxRn.setStatus("current")
_CfprIdentIdentCtxAssigned_Type = SnmpAdminString
_CfprIdentIdentCtxAssigned_Object = MibTableColumn
cfprIdentIdentCtxAssigned = _CfprIdentIdentCtxAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 4),
    _CfprIdentIdentCtxAssigned_Type()
)
cfprIdentIdentCtxAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxAssigned.setStatus("current")
_CfprIdentIdentCtxConsDn_Type = SnmpAdminString
_CfprIdentIdentCtxConsDn_Object = MibTableColumn
cfprIdentIdentCtxConsDn = _CfprIdentIdentCtxConsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 5),
    _CfprIdentIdentCtxConsDn_Type()
)
cfprIdentIdentCtxConsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxConsDn.setStatus("current")
_CfprIdentIdentCtxConsType_Type = CfprIdentConsType
_CfprIdentIdentCtxConsType_Object = MibTableColumn
cfprIdentIdentCtxConsType = _CfprIdentIdentCtxConsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 6),
    _CfprIdentIdentCtxConsType_Type()
)
cfprIdentIdentCtxConsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxConsType.setStatus("current")
_CfprIdentIdentCtxDefinedInIdm_Type = CfprIdentIdDefinedInIdm
_CfprIdentIdentCtxDefinedInIdm_Object = MibTableColumn
cfprIdentIdentCtxDefinedInIdm = _CfprIdentIdentCtxDefinedInIdm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 7),
    _CfprIdentIdentCtxDefinedInIdm_Type()
)
cfprIdentIdentCtxDefinedInIdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxDefinedInIdm.setStatus("current")
_CfprIdentIdentCtxGlobalAssignedCnt_Type = Gauge32
_CfprIdentIdentCtxGlobalAssignedCnt_Object = MibTableColumn
cfprIdentIdentCtxGlobalAssignedCnt = _CfprIdentIdentCtxGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 8),
    _CfprIdentIdentCtxGlobalAssignedCnt_Type()
)
cfprIdentIdentCtxGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxGlobalAssignedCnt.setStatus("current")
_CfprIdentIdentCtxGlobalDefinedCnt_Type = Gauge32
_CfprIdentIdentCtxGlobalDefinedCnt_Object = MibTableColumn
cfprIdentIdentCtxGlobalDefinedCnt = _CfprIdentIdentCtxGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 9),
    _CfprIdentIdentCtxGlobalDefinedCnt_Type()
)
cfprIdentIdentCtxGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxGlobalDefinedCnt.setStatus("current")
_CfprIdentIdentCtxIdentPoolName_Type = SnmpAdminString
_CfprIdentIdentCtxIdentPoolName_Object = MibTableColumn
cfprIdentIdentCtxIdentPoolName = _CfprIdentIdentCtxIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 10),
    _CfprIdentIdentCtxIdentPoolName_Type()
)
cfprIdentIdentCtxIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxIdentPoolName.setStatus("current")
_CfprIdentIdentCtxIdentType_Type = CfprIdentIdentType
_CfprIdentIdentCtxIdentType_Object = MibTableColumn
cfprIdentIdentCtxIdentType = _CfprIdentIdentCtxIdentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 11),
    _CfprIdentIdentCtxIdentType_Type()
)
cfprIdentIdentCtxIdentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxIdentType.setStatus("current")
_CfprIdentIdentCtxIntent_Type = CfprIdentIdentReqIntent
_CfprIdentIdentCtxIntent_Object = MibTableColumn
cfprIdentIdentCtxIntent = _CfprIdentIdentCtxIntent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 12),
    _CfprIdentIdentCtxIntent_Type()
)
cfprIdentIdentCtxIntent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxIntent.setStatus("current")
_CfprIdentIdentCtxIsAssignedLocally_Type = TruthValue
_CfprIdentIdentCtxIsAssignedLocally_Object = MibTableColumn
cfprIdentIdentCtxIsAssignedLocally = _CfprIdentIdentCtxIsAssignedLocally_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 13),
    _CfprIdentIdentCtxIsAssignedLocally_Type()
)
cfprIdentIdentCtxIsAssignedLocally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxIsAssignedLocally.setStatus("current")
_CfprIdentIdentCtxPoolDn_Type = SnmpAdminString
_CfprIdentIdentCtxPoolDn_Object = MibTableColumn
cfprIdentIdentCtxPoolDn = _CfprIdentIdentCtxPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 14),
    _CfprIdentIdentCtxPoolDn_Type()
)
cfprIdentIdentCtxPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxPoolDn.setStatus("current")
_CfprIdentIdentCtxPoolOrgDn_Type = SnmpAdminString
_CfprIdentIdentCtxPoolOrgDn_Object = MibTableColumn
cfprIdentIdentCtxPoolOrgDn = _CfprIdentIdentCtxPoolOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 15),
    _CfprIdentIdentCtxPoolOrgDn_Type()
)
cfprIdentIdentCtxPoolOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxPoolOrgDn.setStatus("current")
_CfprIdentIdentCtxPooledId_Type = Gauge32
_CfprIdentIdentCtxPooledId_Object = MibTableColumn
cfprIdentIdentCtxPooledId = _CfprIdentIdentCtxPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 16),
    _CfprIdentIdentCtxPooledId_Type()
)
cfprIdentIdentCtxPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxPooledId.setStatus("current")
_CfprIdentIdentCtxRetStatus_Type = CfprIdentRetStatus
_CfprIdentIdentCtxRetStatus_Object = MibTableColumn
cfprIdentIdentCtxRetStatus = _CfprIdentIdentCtxRetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 17),
    _CfprIdentIdentCtxRetStatus_Type()
)
cfprIdentIdentCtxRetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxRetStatus.setStatus("current")
_CfprIdentIdentCtxSeqNum_Type = Gauge32
_CfprIdentIdentCtxSeqNum_Object = MibTableColumn
cfprIdentIdentCtxSeqNum = _CfprIdentIdentCtxSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 18),
    _CfprIdentIdentCtxSeqNum_Type()
)
cfprIdentIdentCtxSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxSeqNum.setStatus("current")
_CfprIdentIdentCtxSupplId1_Type = SnmpAdminString
_CfprIdentIdentCtxSupplId1_Object = MibTableColumn
cfprIdentIdentCtxSupplId1 = _CfprIdentIdentCtxSupplId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 19),
    _CfprIdentIdentCtxSupplId1_Type()
)
cfprIdentIdentCtxSupplId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxSupplId1.setStatus("current")
_CfprIdentIdentCtxSupplId2_Type = SnmpAdminString
_CfprIdentIdentCtxSupplId2_Object = MibTableColumn
cfprIdentIdentCtxSupplId2 = _CfprIdentIdentCtxSupplId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 20),
    _CfprIdentIdentCtxSupplId2_Type()
)
cfprIdentIdentCtxSupplId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxSupplId2.setStatus("current")
_CfprIdentIdentCtxSupplId3_Type = SnmpAdminString
_CfprIdentIdentCtxSupplId3_Object = MibTableColumn
cfprIdentIdentCtxSupplId3 = _CfprIdentIdentCtxSupplId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 21),
    _CfprIdentIdentCtxSupplId3_Type()
)
cfprIdentIdentCtxSupplId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxSupplId3.setStatus("current")
_CfprIdentIdentCtxSupplId4_Type = SnmpAdminString
_CfprIdentIdentCtxSupplId4_Object = MibTableColumn
cfprIdentIdentCtxSupplId4 = _CfprIdentIdentCtxSupplId4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 1, 1, 22),
    _CfprIdentIdentCtxSupplId4_Type()
)
cfprIdentIdentCtxSupplId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentCtxSupplId4.setStatus("current")
_CfprIdentIdentRequestTable_Object = MibTable
cfprIdentIdentRequestTable = _CfprIdentIdentRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2)
)
if mibBuilder.loadTexts:
    cfprIdentIdentRequestTable.setStatus("current")
_CfprIdentIdentRequestEntry_Object = MibTableRow
cfprIdentIdentRequestEntry = _CfprIdentIdentRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1)
)
cfprIdentIdentRequestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentIdentRequestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentIdentRequestEntry.setStatus("current")
_CfprIdentIdentRequestInstanceId_Type = CfprManagedObjectId
_CfprIdentIdentRequestInstanceId_Object = MibTableColumn
cfprIdentIdentRequestInstanceId = _CfprIdentIdentRequestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 1),
    _CfprIdentIdentRequestInstanceId_Type()
)
cfprIdentIdentRequestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestInstanceId.setStatus("current")
_CfprIdentIdentRequestDn_Type = CfprManagedObjectDn
_CfprIdentIdentRequestDn_Object = MibTableColumn
cfprIdentIdentRequestDn = _CfprIdentIdentRequestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 2),
    _CfprIdentIdentRequestDn_Type()
)
cfprIdentIdentRequestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestDn.setStatus("current")
_CfprIdentIdentRequestRn_Type = SnmpAdminString
_CfprIdentIdentRequestRn_Object = MibTableColumn
cfprIdentIdentRequestRn = _CfprIdentIdentRequestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 3),
    _CfprIdentIdentRequestRn_Type()
)
cfprIdentIdentRequestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestRn.setStatus("current")
_CfprIdentIdentRequestEpDn_Type = SnmpAdminString
_CfprIdentIdentRequestEpDn_Object = MibTableColumn
cfprIdentIdentRequestEpDn = _CfprIdentIdentRequestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 4),
    _CfprIdentIdentRequestEpDn_Type()
)
cfprIdentIdentRequestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestEpDn.setStatus("current")
_CfprIdentIdentRequestFsmDescr_Type = SnmpAdminString
_CfprIdentIdentRequestFsmDescr_Object = MibTableColumn
cfprIdentIdentRequestFsmDescr = _CfprIdentIdentRequestFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 5),
    _CfprIdentIdentRequestFsmDescr_Type()
)
cfprIdentIdentRequestFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmDescr.setStatus("current")
_CfprIdentIdentRequestFsmPrev_Type = SnmpAdminString
_CfprIdentIdentRequestFsmPrev_Object = MibTableColumn
cfprIdentIdentRequestFsmPrev = _CfprIdentIdentRequestFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 6),
    _CfprIdentIdentRequestFsmPrev_Type()
)
cfprIdentIdentRequestFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmPrev.setStatus("current")
_CfprIdentIdentRequestFsmProgr_Type = Gauge32
_CfprIdentIdentRequestFsmProgr_Object = MibTableColumn
cfprIdentIdentRequestFsmProgr = _CfprIdentIdentRequestFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 7),
    _CfprIdentIdentRequestFsmProgr_Type()
)
cfprIdentIdentRequestFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmProgr.setStatus("current")
_CfprIdentIdentRequestFsmRmtInvErrCode_Type = Gauge32
_CfprIdentIdentRequestFsmRmtInvErrCode_Object = MibTableColumn
cfprIdentIdentRequestFsmRmtInvErrCode = _CfprIdentIdentRequestFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 8),
    _CfprIdentIdentRequestFsmRmtInvErrCode_Type()
)
cfprIdentIdentRequestFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmRmtInvErrCode.setStatus("current")
_CfprIdentIdentRequestFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprIdentIdentRequestFsmRmtInvErrDescr_Object = MibTableColumn
cfprIdentIdentRequestFsmRmtInvErrDescr = _CfprIdentIdentRequestFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 9),
    _CfprIdentIdentRequestFsmRmtInvErrDescr_Type()
)
cfprIdentIdentRequestFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmRmtInvErrDescr.setStatus("current")
_CfprIdentIdentRequestFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprIdentIdentRequestFsmRmtInvRslt_Object = MibTableColumn
cfprIdentIdentRequestFsmRmtInvRslt = _CfprIdentIdentRequestFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 10),
    _CfprIdentIdentRequestFsmRmtInvRslt_Type()
)
cfprIdentIdentRequestFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmRmtInvRslt.setStatus("current")
_CfprIdentIdentRequestFsmStageDescr_Type = SnmpAdminString
_CfprIdentIdentRequestFsmStageDescr_Object = MibTableColumn
cfprIdentIdentRequestFsmStageDescr = _CfprIdentIdentRequestFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 11),
    _CfprIdentIdentRequestFsmStageDescr_Type()
)
cfprIdentIdentRequestFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageDescr.setStatus("current")
_CfprIdentIdentRequestFsmStamp_Type = DateAndTime
_CfprIdentIdentRequestFsmStamp_Object = MibTableColumn
cfprIdentIdentRequestFsmStamp = _CfprIdentIdentRequestFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 12),
    _CfprIdentIdentRequestFsmStamp_Type()
)
cfprIdentIdentRequestFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStamp.setStatus("current")
_CfprIdentIdentRequestFsmStatus_Type = SnmpAdminString
_CfprIdentIdentRequestFsmStatus_Object = MibTableColumn
cfprIdentIdentRequestFsmStatus = _CfprIdentIdentRequestFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 13),
    _CfprIdentIdentRequestFsmStatus_Type()
)
cfprIdentIdentRequestFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStatus.setStatus("current")
_CfprIdentIdentRequestFsmTry_Type = Gauge32
_CfprIdentIdentRequestFsmTry_Object = MibTableColumn
cfprIdentIdentRequestFsmTry = _CfprIdentIdentRequestFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 14),
    _CfprIdentIdentRequestFsmTry_Type()
)
cfprIdentIdentRequestFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTry.setStatus("current")
_CfprIdentIdentRequestId_Type = Gauge32
_CfprIdentIdentRequestId_Object = MibTableColumn
cfprIdentIdentRequestId = _CfprIdentIdentRequestId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 15),
    _CfprIdentIdentRequestId_Type()
)
cfprIdentIdentRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestId.setStatus("current")
_CfprIdentIdentRequestRequestSize_Type = Gauge32
_CfprIdentIdentRequestRequestSize_Object = MibTableColumn
cfprIdentIdentRequestRequestSize = _CfprIdentIdentRequestRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 16),
    _CfprIdentIdentRequestRequestSize_Type()
)
cfprIdentIdentRequestRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestRequestSize.setStatus("current")
_CfprIdentIdentRequestSeqNum_Type = Gauge32
_CfprIdentIdentRequestSeqNum_Object = MibTableColumn
cfprIdentIdentRequestSeqNum = _CfprIdentIdentRequestSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 2, 1, 17),
    _CfprIdentIdentRequestSeqNum_Type()
)
cfprIdentIdentRequestSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestSeqNum.setStatus("current")
_CfprIdentIdentRequestFsmTable_Object = MibTable
cfprIdentIdentRequestFsmTable = _CfprIdentIdentRequestFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3)
)
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTable.setStatus("current")
_CfprIdentIdentRequestFsmEntry_Object = MibTableRow
cfprIdentIdentRequestFsmEntry = _CfprIdentIdentRequestFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1)
)
cfprIdentIdentRequestFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentIdentRequestFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmEntry.setStatus("current")
_CfprIdentIdentRequestFsmInstanceId_Type = CfprManagedObjectId
_CfprIdentIdentRequestFsmInstanceId_Object = MibTableColumn
cfprIdentIdentRequestFsmInstanceId = _CfprIdentIdentRequestFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 1),
    _CfprIdentIdentRequestFsmInstanceId_Type()
)
cfprIdentIdentRequestFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmInstanceId.setStatus("current")
_CfprIdentIdentRequestFsmDn_Type = CfprManagedObjectDn
_CfprIdentIdentRequestFsmDn_Object = MibTableColumn
cfprIdentIdentRequestFsmDn = _CfprIdentIdentRequestFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 2),
    _CfprIdentIdentRequestFsmDn_Type()
)
cfprIdentIdentRequestFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmDn.setStatus("current")
_CfprIdentIdentRequestFsmRn_Type = SnmpAdminString
_CfprIdentIdentRequestFsmRn_Object = MibTableColumn
cfprIdentIdentRequestFsmRn = _CfprIdentIdentRequestFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 3),
    _CfprIdentIdentRequestFsmRn_Type()
)
cfprIdentIdentRequestFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmRn.setStatus("current")
_CfprIdentIdentRequestFsmCompletionTime_Type = DateAndTime
_CfprIdentIdentRequestFsmCompletionTime_Object = MibTableColumn
cfprIdentIdentRequestFsmCompletionTime = _CfprIdentIdentRequestFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 4),
    _CfprIdentIdentRequestFsmCompletionTime_Type()
)
cfprIdentIdentRequestFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmCompletionTime.setStatus("current")
_CfprIdentIdentRequestFsmCurrentFsm_Type = CfprIdentIdentRequestFsmCurrentFsm
_CfprIdentIdentRequestFsmCurrentFsm_Object = MibTableColumn
cfprIdentIdentRequestFsmCurrentFsm = _CfprIdentIdentRequestFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 5),
    _CfprIdentIdentRequestFsmCurrentFsm_Type()
)
cfprIdentIdentRequestFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmCurrentFsm.setStatus("current")
_CfprIdentIdentRequestFsmDescrData_Type = SnmpAdminString
_CfprIdentIdentRequestFsmDescrData_Object = MibTableColumn
cfprIdentIdentRequestFsmDescrData = _CfprIdentIdentRequestFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 6),
    _CfprIdentIdentRequestFsmDescrData_Type()
)
cfprIdentIdentRequestFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmDescrData.setStatus("current")
_CfprIdentIdentRequestFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprIdentIdentRequestFsmFsmStatus_Object = MibTableColumn
cfprIdentIdentRequestFsmFsmStatus = _CfprIdentIdentRequestFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 7),
    _CfprIdentIdentRequestFsmFsmStatus_Type()
)
cfprIdentIdentRequestFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmFsmStatus.setStatus("current")
_CfprIdentIdentRequestFsmProgress_Type = Gauge32
_CfprIdentIdentRequestFsmProgress_Object = MibTableColumn
cfprIdentIdentRequestFsmProgress = _CfprIdentIdentRequestFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 8),
    _CfprIdentIdentRequestFsmProgress_Type()
)
cfprIdentIdentRequestFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmProgress.setStatus("current")
_CfprIdentIdentRequestFsmRmtErrCode_Type = Gauge32
_CfprIdentIdentRequestFsmRmtErrCode_Object = MibTableColumn
cfprIdentIdentRequestFsmRmtErrCode = _CfprIdentIdentRequestFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 9),
    _CfprIdentIdentRequestFsmRmtErrCode_Type()
)
cfprIdentIdentRequestFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmRmtErrCode.setStatus("current")
_CfprIdentIdentRequestFsmRmtErrDescr_Type = SnmpAdminString
_CfprIdentIdentRequestFsmRmtErrDescr_Object = MibTableColumn
cfprIdentIdentRequestFsmRmtErrDescr = _CfprIdentIdentRequestFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 10),
    _CfprIdentIdentRequestFsmRmtErrDescr_Type()
)
cfprIdentIdentRequestFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmRmtErrDescr.setStatus("current")
_CfprIdentIdentRequestFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprIdentIdentRequestFsmRmtRslt_Object = MibTableColumn
cfprIdentIdentRequestFsmRmtRslt = _CfprIdentIdentRequestFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 3, 1, 11),
    _CfprIdentIdentRequestFsmRmtRslt_Type()
)
cfprIdentIdentRequestFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmRmtRslt.setStatus("current")
_CfprIdentIdentRequestFsmStageTable_Object = MibTable
cfprIdentIdentRequestFsmStageTable = _CfprIdentIdentRequestFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4)
)
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageTable.setStatus("current")
_CfprIdentIdentRequestFsmStageEntry_Object = MibTableRow
cfprIdentIdentRequestFsmStageEntry = _CfprIdentIdentRequestFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1)
)
cfprIdentIdentRequestFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentIdentRequestFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageEntry.setStatus("current")
_CfprIdentIdentRequestFsmStageInstanceId_Type = CfprManagedObjectId
_CfprIdentIdentRequestFsmStageInstanceId_Object = MibTableColumn
cfprIdentIdentRequestFsmStageInstanceId = _CfprIdentIdentRequestFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 1),
    _CfprIdentIdentRequestFsmStageInstanceId_Type()
)
cfprIdentIdentRequestFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageInstanceId.setStatus("current")
_CfprIdentIdentRequestFsmStageDn_Type = CfprManagedObjectDn
_CfprIdentIdentRequestFsmStageDn_Object = MibTableColumn
cfprIdentIdentRequestFsmStageDn = _CfprIdentIdentRequestFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 2),
    _CfprIdentIdentRequestFsmStageDn_Type()
)
cfprIdentIdentRequestFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageDn.setStatus("current")
_CfprIdentIdentRequestFsmStageRn_Type = SnmpAdminString
_CfprIdentIdentRequestFsmStageRn_Object = MibTableColumn
cfprIdentIdentRequestFsmStageRn = _CfprIdentIdentRequestFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 3),
    _CfprIdentIdentRequestFsmStageRn_Type()
)
cfprIdentIdentRequestFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageRn.setStatus("current")
_CfprIdentIdentRequestFsmStageDescrData_Type = SnmpAdminString
_CfprIdentIdentRequestFsmStageDescrData_Object = MibTableColumn
cfprIdentIdentRequestFsmStageDescrData = _CfprIdentIdentRequestFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 4),
    _CfprIdentIdentRequestFsmStageDescrData_Type()
)
cfprIdentIdentRequestFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageDescrData.setStatus("current")
_CfprIdentIdentRequestFsmStageLastUpdateTime_Type = DateAndTime
_CfprIdentIdentRequestFsmStageLastUpdateTime_Object = MibTableColumn
cfprIdentIdentRequestFsmStageLastUpdateTime = _CfprIdentIdentRequestFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 5),
    _CfprIdentIdentRequestFsmStageLastUpdateTime_Type()
)
cfprIdentIdentRequestFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageLastUpdateTime.setStatus("current")
_CfprIdentIdentRequestFsmStageName_Type = CfprIdentIdentRequestFsmStageName
_CfprIdentIdentRequestFsmStageName_Object = MibTableColumn
cfprIdentIdentRequestFsmStageName = _CfprIdentIdentRequestFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 6),
    _CfprIdentIdentRequestFsmStageName_Type()
)
cfprIdentIdentRequestFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageName.setStatus("current")
_CfprIdentIdentRequestFsmStageOrder_Type = Gauge32
_CfprIdentIdentRequestFsmStageOrder_Object = MibTableColumn
cfprIdentIdentRequestFsmStageOrder = _CfprIdentIdentRequestFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 7),
    _CfprIdentIdentRequestFsmStageOrder_Type()
)
cfprIdentIdentRequestFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageOrder.setStatus("current")
_CfprIdentIdentRequestFsmStageRetry_Type = Gauge32
_CfprIdentIdentRequestFsmStageRetry_Object = MibTableColumn
cfprIdentIdentRequestFsmStageRetry = _CfprIdentIdentRequestFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 8),
    _CfprIdentIdentRequestFsmStageRetry_Type()
)
cfprIdentIdentRequestFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageRetry.setStatus("current")
_CfprIdentIdentRequestFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprIdentIdentRequestFsmStageStageStatus_Object = MibTableColumn
cfprIdentIdentRequestFsmStageStageStatus = _CfprIdentIdentRequestFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 4, 1, 9),
    _CfprIdentIdentRequestFsmStageStageStatus_Type()
)
cfprIdentIdentRequestFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmStageStageStatus.setStatus("current")
_CfprIdentIdentRequestFsmTaskTable_Object = MibTable
cfprIdentIdentRequestFsmTaskTable = _CfprIdentIdentRequestFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5)
)
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskTable.setStatus("current")
_CfprIdentIdentRequestFsmTaskEntry_Object = MibTableRow
cfprIdentIdentRequestFsmTaskEntry = _CfprIdentIdentRequestFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5, 1)
)
cfprIdentIdentRequestFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentIdentRequestFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskEntry.setStatus("current")
_CfprIdentIdentRequestFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprIdentIdentRequestFsmTaskInstanceId_Object = MibTableColumn
cfprIdentIdentRequestFsmTaskInstanceId = _CfprIdentIdentRequestFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5, 1, 1),
    _CfprIdentIdentRequestFsmTaskInstanceId_Type()
)
cfprIdentIdentRequestFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskInstanceId.setStatus("current")
_CfprIdentIdentRequestFsmTaskDn_Type = CfprManagedObjectDn
_CfprIdentIdentRequestFsmTaskDn_Object = MibTableColumn
cfprIdentIdentRequestFsmTaskDn = _CfprIdentIdentRequestFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5, 1, 2),
    _CfprIdentIdentRequestFsmTaskDn_Type()
)
cfprIdentIdentRequestFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskDn.setStatus("current")
_CfprIdentIdentRequestFsmTaskRn_Type = SnmpAdminString
_CfprIdentIdentRequestFsmTaskRn_Object = MibTableColumn
cfprIdentIdentRequestFsmTaskRn = _CfprIdentIdentRequestFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5, 1, 3),
    _CfprIdentIdentRequestFsmTaskRn_Type()
)
cfprIdentIdentRequestFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskRn.setStatus("current")
_CfprIdentIdentRequestFsmTaskCompletion_Type = CfprFsmCompletion
_CfprIdentIdentRequestFsmTaskCompletion_Object = MibTableColumn
cfprIdentIdentRequestFsmTaskCompletion = _CfprIdentIdentRequestFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5, 1, 4),
    _CfprIdentIdentRequestFsmTaskCompletion_Type()
)
cfprIdentIdentRequestFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskCompletion.setStatus("current")
_CfprIdentIdentRequestFsmTaskFlags_Type = CfprFsmFlags
_CfprIdentIdentRequestFsmTaskFlags_Object = MibTableColumn
cfprIdentIdentRequestFsmTaskFlags = _CfprIdentIdentRequestFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5, 1, 5),
    _CfprIdentIdentRequestFsmTaskFlags_Type()
)
cfprIdentIdentRequestFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskFlags.setStatus("current")
_CfprIdentIdentRequestFsmTaskItem_Type = CfprIdentIdentRequestFsmTaskItem
_CfprIdentIdentRequestFsmTaskItem_Object = MibTableColumn
cfprIdentIdentRequestFsmTaskItem = _CfprIdentIdentRequestFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5, 1, 6),
    _CfprIdentIdentRequestFsmTaskItem_Type()
)
cfprIdentIdentRequestFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskItem.setStatus("current")
_CfprIdentIdentRequestFsmTaskSeqId_Type = Gauge32
_CfprIdentIdentRequestFsmTaskSeqId_Object = MibTableColumn
cfprIdentIdentRequestFsmTaskSeqId = _CfprIdentIdentRequestFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 5, 1, 7),
    _CfprIdentIdentRequestFsmTaskSeqId_Type()
)
cfprIdentIdentRequestFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentIdentRequestFsmTaskSeqId.setStatus("current")
_CfprIdentMetaSystemTable_Object = MibTable
cfprIdentMetaSystemTable = _CfprIdentMetaSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6)
)
if mibBuilder.loadTexts:
    cfprIdentMetaSystemTable.setStatus("current")
_CfprIdentMetaSystemEntry_Object = MibTableRow
cfprIdentMetaSystemEntry = _CfprIdentMetaSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1)
)
cfprIdentMetaSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentMetaSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentMetaSystemEntry.setStatus("current")
_CfprIdentMetaSystemInstanceId_Type = CfprManagedObjectId
_CfprIdentMetaSystemInstanceId_Object = MibTableColumn
cfprIdentMetaSystemInstanceId = _CfprIdentMetaSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 1),
    _CfprIdentMetaSystemInstanceId_Type()
)
cfprIdentMetaSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemInstanceId.setStatus("current")
_CfprIdentMetaSystemDn_Type = CfprManagedObjectDn
_CfprIdentMetaSystemDn_Object = MibTableColumn
cfprIdentMetaSystemDn = _CfprIdentMetaSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 2),
    _CfprIdentMetaSystemDn_Type()
)
cfprIdentMetaSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemDn.setStatus("current")
_CfprIdentMetaSystemRn_Type = SnmpAdminString
_CfprIdentMetaSystemRn_Object = MibTableColumn
cfprIdentMetaSystemRn = _CfprIdentMetaSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 3),
    _CfprIdentMetaSystemRn_Type()
)
cfprIdentMetaSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemRn.setStatus("current")
_CfprIdentMetaSystemFsmDescr_Type = SnmpAdminString
_CfprIdentMetaSystemFsmDescr_Object = MibTableColumn
cfprIdentMetaSystemFsmDescr = _CfprIdentMetaSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 4),
    _CfprIdentMetaSystemFsmDescr_Type()
)
cfprIdentMetaSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmDescr.setStatus("current")
_CfprIdentMetaSystemFsmPrev_Type = SnmpAdminString
_CfprIdentMetaSystemFsmPrev_Object = MibTableColumn
cfprIdentMetaSystemFsmPrev = _CfprIdentMetaSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 5),
    _CfprIdentMetaSystemFsmPrev_Type()
)
cfprIdentMetaSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmPrev.setStatus("current")
_CfprIdentMetaSystemFsmProgr_Type = Gauge32
_CfprIdentMetaSystemFsmProgr_Object = MibTableColumn
cfprIdentMetaSystemFsmProgr = _CfprIdentMetaSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 6),
    _CfprIdentMetaSystemFsmProgr_Type()
)
cfprIdentMetaSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmProgr.setStatus("current")
_CfprIdentMetaSystemFsmRmtInvErrCode_Type = Gauge32
_CfprIdentMetaSystemFsmRmtInvErrCode_Object = MibTableColumn
cfprIdentMetaSystemFsmRmtInvErrCode = _CfprIdentMetaSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 7),
    _CfprIdentMetaSystemFsmRmtInvErrCode_Type()
)
cfprIdentMetaSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmRmtInvErrCode.setStatus("current")
_CfprIdentMetaSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprIdentMetaSystemFsmRmtInvErrDescr_Object = MibTableColumn
cfprIdentMetaSystemFsmRmtInvErrDescr = _CfprIdentMetaSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 8),
    _CfprIdentMetaSystemFsmRmtInvErrDescr_Type()
)
cfprIdentMetaSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmRmtInvErrDescr.setStatus("current")
_CfprIdentMetaSystemFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprIdentMetaSystemFsmRmtInvRslt_Object = MibTableColumn
cfprIdentMetaSystemFsmRmtInvRslt = _CfprIdentMetaSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 9),
    _CfprIdentMetaSystemFsmRmtInvRslt_Type()
)
cfprIdentMetaSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmRmtInvRslt.setStatus("current")
_CfprIdentMetaSystemFsmStageDescr_Type = SnmpAdminString
_CfprIdentMetaSystemFsmStageDescr_Object = MibTableColumn
cfprIdentMetaSystemFsmStageDescr = _CfprIdentMetaSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 10),
    _CfprIdentMetaSystemFsmStageDescr_Type()
)
cfprIdentMetaSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageDescr.setStatus("current")
_CfprIdentMetaSystemFsmStamp_Type = DateAndTime
_CfprIdentMetaSystemFsmStamp_Object = MibTableColumn
cfprIdentMetaSystemFsmStamp = _CfprIdentMetaSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 11),
    _CfprIdentMetaSystemFsmStamp_Type()
)
cfprIdentMetaSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStamp.setStatus("current")
_CfprIdentMetaSystemFsmStatus_Type = SnmpAdminString
_CfprIdentMetaSystemFsmStatus_Object = MibTableColumn
cfprIdentMetaSystemFsmStatus = _CfprIdentMetaSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 12),
    _CfprIdentMetaSystemFsmStatus_Type()
)
cfprIdentMetaSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStatus.setStatus("current")
_CfprIdentMetaSystemFsmTry_Type = Gauge32
_CfprIdentMetaSystemFsmTry_Object = MibTableColumn
cfprIdentMetaSystemFsmTry = _CfprIdentMetaSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 13),
    _CfprIdentMetaSystemFsmTry_Type()
)
cfprIdentMetaSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTry.setStatus("current")
_CfprIdentMetaSystemGeneration_Type = Gauge32
_CfprIdentMetaSystemGeneration_Object = MibTableColumn
cfprIdentMetaSystemGeneration = _CfprIdentMetaSystemGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 14),
    _CfprIdentMetaSystemGeneration_Type()
)
cfprIdentMetaSystemGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemGeneration.setStatus("current")
_CfprIdentMetaSystemNextReqId_Type = Gauge32
_CfprIdentMetaSystemNextReqId_Object = MibTableColumn
cfprIdentMetaSystemNextReqId = _CfprIdentMetaSystemNextReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 15),
    _CfprIdentMetaSystemNextReqId_Type()
)
cfprIdentMetaSystemNextReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemNextReqId.setStatus("current")
_CfprIdentMetaSystemSysid_Type = Gauge32
_CfprIdentMetaSystemSysid_Object = MibTableColumn
cfprIdentMetaSystemSysid = _CfprIdentMetaSystemSysid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 16),
    _CfprIdentMetaSystemSysid_Type()
)
cfprIdentMetaSystemSysid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemSysid.setStatus("current")
_CfprIdentMetaSystemFprcGeneration_Type = Gauge32
_CfprIdentMetaSystemFprcGeneration_Object = MibTableColumn
cfprIdentMetaSystemFprcGeneration = _CfprIdentMetaSystemFprcGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 6, 1, 17),
    _CfprIdentMetaSystemFprcGeneration_Type()
)
cfprIdentMetaSystemFprcGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFprcGeneration.setStatus("current")
_CfprIdentMetaSystemFsmTable_Object = MibTable
cfprIdentMetaSystemFsmTable = _CfprIdentMetaSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7)
)
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTable.setStatus("current")
_CfprIdentMetaSystemFsmEntry_Object = MibTableRow
cfprIdentMetaSystemFsmEntry = _CfprIdentMetaSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1)
)
cfprIdentMetaSystemFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentMetaSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmEntry.setStatus("current")
_CfprIdentMetaSystemFsmInstanceId_Type = CfprManagedObjectId
_CfprIdentMetaSystemFsmInstanceId_Object = MibTableColumn
cfprIdentMetaSystemFsmInstanceId = _CfprIdentMetaSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 1),
    _CfprIdentMetaSystemFsmInstanceId_Type()
)
cfprIdentMetaSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmInstanceId.setStatus("current")
_CfprIdentMetaSystemFsmDn_Type = CfprManagedObjectDn
_CfprIdentMetaSystemFsmDn_Object = MibTableColumn
cfprIdentMetaSystemFsmDn = _CfprIdentMetaSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 2),
    _CfprIdentMetaSystemFsmDn_Type()
)
cfprIdentMetaSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmDn.setStatus("current")
_CfprIdentMetaSystemFsmRn_Type = SnmpAdminString
_CfprIdentMetaSystemFsmRn_Object = MibTableColumn
cfprIdentMetaSystemFsmRn = _CfprIdentMetaSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 3),
    _CfprIdentMetaSystemFsmRn_Type()
)
cfprIdentMetaSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmRn.setStatus("current")
_CfprIdentMetaSystemFsmCompletionTime_Type = DateAndTime
_CfprIdentMetaSystemFsmCompletionTime_Object = MibTableColumn
cfprIdentMetaSystemFsmCompletionTime = _CfprIdentMetaSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 4),
    _CfprIdentMetaSystemFsmCompletionTime_Type()
)
cfprIdentMetaSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmCompletionTime.setStatus("current")
_CfprIdentMetaSystemFsmCurrentFsm_Type = CfprIdentMetaSystemFsmCurrentFsm
_CfprIdentMetaSystemFsmCurrentFsm_Object = MibTableColumn
cfprIdentMetaSystemFsmCurrentFsm = _CfprIdentMetaSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 5),
    _CfprIdentMetaSystemFsmCurrentFsm_Type()
)
cfprIdentMetaSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmCurrentFsm.setStatus("current")
_CfprIdentMetaSystemFsmDescrData_Type = SnmpAdminString
_CfprIdentMetaSystemFsmDescrData_Object = MibTableColumn
cfprIdentMetaSystemFsmDescrData = _CfprIdentMetaSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 6),
    _CfprIdentMetaSystemFsmDescrData_Type()
)
cfprIdentMetaSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmDescrData.setStatus("current")
_CfprIdentMetaSystemFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprIdentMetaSystemFsmFsmStatus_Object = MibTableColumn
cfprIdentMetaSystemFsmFsmStatus = _CfprIdentMetaSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 7),
    _CfprIdentMetaSystemFsmFsmStatus_Type()
)
cfprIdentMetaSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmFsmStatus.setStatus("current")
_CfprIdentMetaSystemFsmProgress_Type = Gauge32
_CfprIdentMetaSystemFsmProgress_Object = MibTableColumn
cfprIdentMetaSystemFsmProgress = _CfprIdentMetaSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 8),
    _CfprIdentMetaSystemFsmProgress_Type()
)
cfprIdentMetaSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmProgress.setStatus("current")
_CfprIdentMetaSystemFsmRmtErrCode_Type = Gauge32
_CfprIdentMetaSystemFsmRmtErrCode_Object = MibTableColumn
cfprIdentMetaSystemFsmRmtErrCode = _CfprIdentMetaSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 9),
    _CfprIdentMetaSystemFsmRmtErrCode_Type()
)
cfprIdentMetaSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmRmtErrCode.setStatus("current")
_CfprIdentMetaSystemFsmRmtErrDescr_Type = SnmpAdminString
_CfprIdentMetaSystemFsmRmtErrDescr_Object = MibTableColumn
cfprIdentMetaSystemFsmRmtErrDescr = _CfprIdentMetaSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 10),
    _CfprIdentMetaSystemFsmRmtErrDescr_Type()
)
cfprIdentMetaSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmRmtErrDescr.setStatus("current")
_CfprIdentMetaSystemFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprIdentMetaSystemFsmRmtRslt_Object = MibTableColumn
cfprIdentMetaSystemFsmRmtRslt = _CfprIdentMetaSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 7, 1, 11),
    _CfprIdentMetaSystemFsmRmtRslt_Type()
)
cfprIdentMetaSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmRmtRslt.setStatus("current")
_CfprIdentMetaSystemFsmStageTable_Object = MibTable
cfprIdentMetaSystemFsmStageTable = _CfprIdentMetaSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8)
)
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageTable.setStatus("current")
_CfprIdentMetaSystemFsmStageEntry_Object = MibTableRow
cfprIdentMetaSystemFsmStageEntry = _CfprIdentMetaSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1)
)
cfprIdentMetaSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentMetaSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageEntry.setStatus("current")
_CfprIdentMetaSystemFsmStageInstanceId_Type = CfprManagedObjectId
_CfprIdentMetaSystemFsmStageInstanceId_Object = MibTableColumn
cfprIdentMetaSystemFsmStageInstanceId = _CfprIdentMetaSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 1),
    _CfprIdentMetaSystemFsmStageInstanceId_Type()
)
cfprIdentMetaSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageInstanceId.setStatus("current")
_CfprIdentMetaSystemFsmStageDn_Type = CfprManagedObjectDn
_CfprIdentMetaSystemFsmStageDn_Object = MibTableColumn
cfprIdentMetaSystemFsmStageDn = _CfprIdentMetaSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 2),
    _CfprIdentMetaSystemFsmStageDn_Type()
)
cfprIdentMetaSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageDn.setStatus("current")
_CfprIdentMetaSystemFsmStageRn_Type = SnmpAdminString
_CfprIdentMetaSystemFsmStageRn_Object = MibTableColumn
cfprIdentMetaSystemFsmStageRn = _CfprIdentMetaSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 3),
    _CfprIdentMetaSystemFsmStageRn_Type()
)
cfprIdentMetaSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageRn.setStatus("current")
_CfprIdentMetaSystemFsmStageDescrData_Type = SnmpAdminString
_CfprIdentMetaSystemFsmStageDescrData_Object = MibTableColumn
cfprIdentMetaSystemFsmStageDescrData = _CfprIdentMetaSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 4),
    _CfprIdentMetaSystemFsmStageDescrData_Type()
)
cfprIdentMetaSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageDescrData.setStatus("current")
_CfprIdentMetaSystemFsmStageLastUpdateTime_Type = DateAndTime
_CfprIdentMetaSystemFsmStageLastUpdateTime_Object = MibTableColumn
cfprIdentMetaSystemFsmStageLastUpdateTime = _CfprIdentMetaSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 5),
    _CfprIdentMetaSystemFsmStageLastUpdateTime_Type()
)
cfprIdentMetaSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageLastUpdateTime.setStatus("current")
_CfprIdentMetaSystemFsmStageName_Type = CfprIdentMetaSystemFsmStageName
_CfprIdentMetaSystemFsmStageName_Object = MibTableColumn
cfprIdentMetaSystemFsmStageName = _CfprIdentMetaSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 6),
    _CfprIdentMetaSystemFsmStageName_Type()
)
cfprIdentMetaSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageName.setStatus("current")
_CfprIdentMetaSystemFsmStageOrder_Type = Gauge32
_CfprIdentMetaSystemFsmStageOrder_Object = MibTableColumn
cfprIdentMetaSystemFsmStageOrder = _CfprIdentMetaSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 7),
    _CfprIdentMetaSystemFsmStageOrder_Type()
)
cfprIdentMetaSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageOrder.setStatus("current")
_CfprIdentMetaSystemFsmStageRetry_Type = Gauge32
_CfprIdentMetaSystemFsmStageRetry_Object = MibTableColumn
cfprIdentMetaSystemFsmStageRetry = _CfprIdentMetaSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 8),
    _CfprIdentMetaSystemFsmStageRetry_Type()
)
cfprIdentMetaSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageRetry.setStatus("current")
_CfprIdentMetaSystemFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprIdentMetaSystemFsmStageStageStatus_Object = MibTableColumn
cfprIdentMetaSystemFsmStageStageStatus = _CfprIdentMetaSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 8, 1, 9),
    _CfprIdentMetaSystemFsmStageStageStatus_Type()
)
cfprIdentMetaSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmStageStageStatus.setStatus("current")
_CfprIdentMetaSystemFsmTaskTable_Object = MibTable
cfprIdentMetaSystemFsmTaskTable = _CfprIdentMetaSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9)
)
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskTable.setStatus("current")
_CfprIdentMetaSystemFsmTaskEntry_Object = MibTableRow
cfprIdentMetaSystemFsmTaskEntry = _CfprIdentMetaSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9, 1)
)
cfprIdentMetaSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentMetaSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskEntry.setStatus("current")
_CfprIdentMetaSystemFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprIdentMetaSystemFsmTaskInstanceId_Object = MibTableColumn
cfprIdentMetaSystemFsmTaskInstanceId = _CfprIdentMetaSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9, 1, 1),
    _CfprIdentMetaSystemFsmTaskInstanceId_Type()
)
cfprIdentMetaSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskInstanceId.setStatus("current")
_CfprIdentMetaSystemFsmTaskDn_Type = CfprManagedObjectDn
_CfprIdentMetaSystemFsmTaskDn_Object = MibTableColumn
cfprIdentMetaSystemFsmTaskDn = _CfprIdentMetaSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9, 1, 2),
    _CfprIdentMetaSystemFsmTaskDn_Type()
)
cfprIdentMetaSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskDn.setStatus("current")
_CfprIdentMetaSystemFsmTaskRn_Type = SnmpAdminString
_CfprIdentMetaSystemFsmTaskRn_Object = MibTableColumn
cfprIdentMetaSystemFsmTaskRn = _CfprIdentMetaSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9, 1, 3),
    _CfprIdentMetaSystemFsmTaskRn_Type()
)
cfprIdentMetaSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskRn.setStatus("current")
_CfprIdentMetaSystemFsmTaskCompletion_Type = CfprFsmCompletion
_CfprIdentMetaSystemFsmTaskCompletion_Object = MibTableColumn
cfprIdentMetaSystemFsmTaskCompletion = _CfprIdentMetaSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9, 1, 4),
    _CfprIdentMetaSystemFsmTaskCompletion_Type()
)
cfprIdentMetaSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskCompletion.setStatus("current")
_CfprIdentMetaSystemFsmTaskFlags_Type = CfprFsmFlags
_CfprIdentMetaSystemFsmTaskFlags_Object = MibTableColumn
cfprIdentMetaSystemFsmTaskFlags = _CfprIdentMetaSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9, 1, 5),
    _CfprIdentMetaSystemFsmTaskFlags_Type()
)
cfprIdentMetaSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskFlags.setStatus("current")
_CfprIdentMetaSystemFsmTaskItem_Type = CfprIdentMetaSystemFsmTaskItem
_CfprIdentMetaSystemFsmTaskItem_Object = MibTableColumn
cfprIdentMetaSystemFsmTaskItem = _CfprIdentMetaSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9, 1, 6),
    _CfprIdentMetaSystemFsmTaskItem_Type()
)
cfprIdentMetaSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskItem.setStatus("current")
_CfprIdentMetaSystemFsmTaskSeqId_Type = Gauge32
_CfprIdentMetaSystemFsmTaskSeqId_Object = MibTableColumn
cfprIdentMetaSystemFsmTaskSeqId = _CfprIdentMetaSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 9, 1, 7),
    _CfprIdentMetaSystemFsmTaskSeqId_Type()
)
cfprIdentMetaSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaSystemFsmTaskSeqId.setStatus("current")
_CfprIdentMetaVerseTable_Object = MibTable
cfprIdentMetaVerseTable = _CfprIdentMetaVerseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 10)
)
if mibBuilder.loadTexts:
    cfprIdentMetaVerseTable.setStatus("current")
_CfprIdentMetaVerseEntry_Object = MibTableRow
cfprIdentMetaVerseEntry = _CfprIdentMetaVerseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 10, 1)
)
cfprIdentMetaVerseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentMetaVerseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentMetaVerseEntry.setStatus("current")
_CfprIdentMetaVerseInstanceId_Type = CfprManagedObjectId
_CfprIdentMetaVerseInstanceId_Object = MibTableColumn
cfprIdentMetaVerseInstanceId = _CfprIdentMetaVerseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 10, 1, 1),
    _CfprIdentMetaVerseInstanceId_Type()
)
cfprIdentMetaVerseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentMetaVerseInstanceId.setStatus("current")
_CfprIdentMetaVerseDn_Type = CfprManagedObjectDn
_CfprIdentMetaVerseDn_Object = MibTableColumn
cfprIdentMetaVerseDn = _CfprIdentMetaVerseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 10, 1, 2),
    _CfprIdentMetaVerseDn_Type()
)
cfprIdentMetaVerseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaVerseDn.setStatus("current")
_CfprIdentMetaVerseRn_Type = SnmpAdminString
_CfprIdentMetaVerseRn_Object = MibTableColumn
cfprIdentMetaVerseRn = _CfprIdentMetaVerseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 10, 1, 3),
    _CfprIdentMetaVerseRn_Type()
)
cfprIdentMetaVerseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentMetaVerseRn.setStatus("current")
_CfprIdentRequestEpTable_Object = MibTable
cfprIdentRequestEpTable = _CfprIdentRequestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 11)
)
if mibBuilder.loadTexts:
    cfprIdentRequestEpTable.setStatus("current")
_CfprIdentRequestEpEntry_Object = MibTableRow
cfprIdentRequestEpEntry = _CfprIdentRequestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 11, 1)
)
cfprIdentRequestEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentRequestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentRequestEpEntry.setStatus("current")
_CfprIdentRequestEpInstanceId_Type = CfprManagedObjectId
_CfprIdentRequestEpInstanceId_Object = MibTableColumn
cfprIdentRequestEpInstanceId = _CfprIdentRequestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 11, 1, 1),
    _CfprIdentRequestEpInstanceId_Type()
)
cfprIdentRequestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentRequestEpInstanceId.setStatus("current")
_CfprIdentRequestEpDn_Type = CfprManagedObjectDn
_CfprIdentRequestEpDn_Object = MibTableColumn
cfprIdentRequestEpDn = _CfprIdentRequestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 11, 1, 2),
    _CfprIdentRequestEpDn_Type()
)
cfprIdentRequestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentRequestEpDn.setStatus("current")
_CfprIdentRequestEpRn_Type = SnmpAdminString
_CfprIdentRequestEpRn_Object = MibTableColumn
cfprIdentRequestEpRn = _CfprIdentRequestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 11, 1, 3),
    _CfprIdentRequestEpRn_Type()
)
cfprIdentRequestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentRequestEpRn.setStatus("current")
_CfprIdentRequestEpReqDn_Type = SnmpAdminString
_CfprIdentRequestEpReqDn_Object = MibTableColumn
cfprIdentRequestEpReqDn = _CfprIdentRequestEpReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 11, 1, 4),
    _CfprIdentRequestEpReqDn_Type()
)
cfprIdentRequestEpReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentRequestEpReqDn.setStatus("current")
_CfprIdentRequestEpReqId_Type = Gauge32
_CfprIdentRequestEpReqId_Object = MibTableColumn
cfprIdentRequestEpReqId = _CfprIdentRequestEpReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 11, 1, 5),
    _CfprIdentRequestEpReqId_Type()
)
cfprIdentRequestEpReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentRequestEpReqId.setStatus("current")
_CfprIdentSysInfoTable_Object = MibTable
cfprIdentSysInfoTable = _CfprIdentSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12)
)
if mibBuilder.loadTexts:
    cfprIdentSysInfoTable.setStatus("current")
_CfprIdentSysInfoEntry_Object = MibTableRow
cfprIdentSysInfoEntry = _CfprIdentSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1)
)
cfprIdentSysInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IDENT-MIB", "cfprIdentSysInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIdentSysInfoEntry.setStatus("current")
_CfprIdentSysInfoInstanceId_Type = CfprManagedObjectId
_CfprIdentSysInfoInstanceId_Object = MibTableColumn
cfprIdentSysInfoInstanceId = _CfprIdentSysInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1, 1),
    _CfprIdentSysInfoInstanceId_Type()
)
cfprIdentSysInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIdentSysInfoInstanceId.setStatus("current")
_CfprIdentSysInfoDn_Type = CfprManagedObjectDn
_CfprIdentSysInfoDn_Object = MibTableColumn
cfprIdentSysInfoDn = _CfprIdentSysInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1, 2),
    _CfprIdentSysInfoDn_Type()
)
cfprIdentSysInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentSysInfoDn.setStatus("current")
_CfprIdentSysInfoRn_Type = SnmpAdminString
_CfprIdentSysInfoRn_Object = MibTableColumn
cfprIdentSysInfoRn = _CfprIdentSysInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1, 3),
    _CfprIdentSysInfoRn_Type()
)
cfprIdentSysInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentSysInfoRn.setStatus("current")
_CfprIdentSysInfoGeneration_Type = Gauge32
_CfprIdentSysInfoGeneration_Object = MibTableColumn
cfprIdentSysInfoGeneration = _CfprIdentSysInfoGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1, 4),
    _CfprIdentSysInfoGeneration_Type()
)
cfprIdentSysInfoGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentSysInfoGeneration.setStatus("current")
_CfprIdentSysInfoIsFirstSync_Type = TruthValue
_CfprIdentSysInfoIsFirstSync_Object = MibTableColumn
cfprIdentSysInfoIsFirstSync = _CfprIdentSysInfoIsFirstSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1, 5),
    _CfprIdentSysInfoIsFirstSync_Type()
)
cfprIdentSysInfoIsFirstSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentSysInfoIsFirstSync.setStatus("current")
_CfprIdentSysInfoIsSync_Type = TruthValue
_CfprIdentSysInfoIsSync_Object = MibTableColumn
cfprIdentSysInfoIsSync = _CfprIdentSysInfoIsSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1, 6),
    _CfprIdentSysInfoIsSync_Type()
)
cfprIdentSysInfoIsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentSysInfoIsSync.setStatus("current")
_CfprIdentSysInfoIsSyncAllowed_Type = TruthValue
_CfprIdentSysInfoIsSyncAllowed_Object = MibTableColumn
cfprIdentSysInfoIsSyncAllowed = _CfprIdentSysInfoIsSyncAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1, 7),
    _CfprIdentSysInfoIsSyncAllowed_Type()
)
cfprIdentSysInfoIsSyncAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentSysInfoIsSyncAllowed.setStatus("current")
_CfprIdentSysInfoFprcGeneration_Type = Gauge32
_CfprIdentSysInfoFprcGeneration_Object = MibTableColumn
cfprIdentSysInfoFprcGeneration = _CfprIdentSysInfoFprcGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 36, 12, 1, 8),
    _CfprIdentSysInfoFprcGeneration_Type()
)
cfprIdentSysInfoFprcGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIdentSysInfoFprcGeneration.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-IDENT-MIB",
    **{"cfprIdentObjects": cfprIdentObjects,
       "cfprIdentIdentCtxTable": cfprIdentIdentCtxTable,
       "cfprIdentIdentCtxEntry": cfprIdentIdentCtxEntry,
       "cfprIdentIdentCtxInstanceId": cfprIdentIdentCtxInstanceId,
       "cfprIdentIdentCtxDn": cfprIdentIdentCtxDn,
       "cfprIdentIdentCtxRn": cfprIdentIdentCtxRn,
       "cfprIdentIdentCtxAssigned": cfprIdentIdentCtxAssigned,
       "cfprIdentIdentCtxConsDn": cfprIdentIdentCtxConsDn,
       "cfprIdentIdentCtxConsType": cfprIdentIdentCtxConsType,
       "cfprIdentIdentCtxDefinedInIdm": cfprIdentIdentCtxDefinedInIdm,
       "cfprIdentIdentCtxGlobalAssignedCnt": cfprIdentIdentCtxGlobalAssignedCnt,
       "cfprIdentIdentCtxGlobalDefinedCnt": cfprIdentIdentCtxGlobalDefinedCnt,
       "cfprIdentIdentCtxIdentPoolName": cfprIdentIdentCtxIdentPoolName,
       "cfprIdentIdentCtxIdentType": cfprIdentIdentCtxIdentType,
       "cfprIdentIdentCtxIntent": cfprIdentIdentCtxIntent,
       "cfprIdentIdentCtxIsAssignedLocally": cfprIdentIdentCtxIsAssignedLocally,
       "cfprIdentIdentCtxPoolDn": cfprIdentIdentCtxPoolDn,
       "cfprIdentIdentCtxPoolOrgDn": cfprIdentIdentCtxPoolOrgDn,
       "cfprIdentIdentCtxPooledId": cfprIdentIdentCtxPooledId,
       "cfprIdentIdentCtxRetStatus": cfprIdentIdentCtxRetStatus,
       "cfprIdentIdentCtxSeqNum": cfprIdentIdentCtxSeqNum,
       "cfprIdentIdentCtxSupplId1": cfprIdentIdentCtxSupplId1,
       "cfprIdentIdentCtxSupplId2": cfprIdentIdentCtxSupplId2,
       "cfprIdentIdentCtxSupplId3": cfprIdentIdentCtxSupplId3,
       "cfprIdentIdentCtxSupplId4": cfprIdentIdentCtxSupplId4,
       "cfprIdentIdentRequestTable": cfprIdentIdentRequestTable,
       "cfprIdentIdentRequestEntry": cfprIdentIdentRequestEntry,
       "cfprIdentIdentRequestInstanceId": cfprIdentIdentRequestInstanceId,
       "cfprIdentIdentRequestDn": cfprIdentIdentRequestDn,
       "cfprIdentIdentRequestRn": cfprIdentIdentRequestRn,
       "cfprIdentIdentRequestEpDn": cfprIdentIdentRequestEpDn,
       "cfprIdentIdentRequestFsmDescr": cfprIdentIdentRequestFsmDescr,
       "cfprIdentIdentRequestFsmPrev": cfprIdentIdentRequestFsmPrev,
       "cfprIdentIdentRequestFsmProgr": cfprIdentIdentRequestFsmProgr,
       "cfprIdentIdentRequestFsmRmtInvErrCode": cfprIdentIdentRequestFsmRmtInvErrCode,
       "cfprIdentIdentRequestFsmRmtInvErrDescr": cfprIdentIdentRequestFsmRmtInvErrDescr,
       "cfprIdentIdentRequestFsmRmtInvRslt": cfprIdentIdentRequestFsmRmtInvRslt,
       "cfprIdentIdentRequestFsmStageDescr": cfprIdentIdentRequestFsmStageDescr,
       "cfprIdentIdentRequestFsmStamp": cfprIdentIdentRequestFsmStamp,
       "cfprIdentIdentRequestFsmStatus": cfprIdentIdentRequestFsmStatus,
       "cfprIdentIdentRequestFsmTry": cfprIdentIdentRequestFsmTry,
       "cfprIdentIdentRequestId": cfprIdentIdentRequestId,
       "cfprIdentIdentRequestRequestSize": cfprIdentIdentRequestRequestSize,
       "cfprIdentIdentRequestSeqNum": cfprIdentIdentRequestSeqNum,
       "cfprIdentIdentRequestFsmTable": cfprIdentIdentRequestFsmTable,
       "cfprIdentIdentRequestFsmEntry": cfprIdentIdentRequestFsmEntry,
       "cfprIdentIdentRequestFsmInstanceId": cfprIdentIdentRequestFsmInstanceId,
       "cfprIdentIdentRequestFsmDn": cfprIdentIdentRequestFsmDn,
       "cfprIdentIdentRequestFsmRn": cfprIdentIdentRequestFsmRn,
       "cfprIdentIdentRequestFsmCompletionTime": cfprIdentIdentRequestFsmCompletionTime,
       "cfprIdentIdentRequestFsmCurrentFsm": cfprIdentIdentRequestFsmCurrentFsm,
       "cfprIdentIdentRequestFsmDescrData": cfprIdentIdentRequestFsmDescrData,
       "cfprIdentIdentRequestFsmFsmStatus": cfprIdentIdentRequestFsmFsmStatus,
       "cfprIdentIdentRequestFsmProgress": cfprIdentIdentRequestFsmProgress,
       "cfprIdentIdentRequestFsmRmtErrCode": cfprIdentIdentRequestFsmRmtErrCode,
       "cfprIdentIdentRequestFsmRmtErrDescr": cfprIdentIdentRequestFsmRmtErrDescr,
       "cfprIdentIdentRequestFsmRmtRslt": cfprIdentIdentRequestFsmRmtRslt,
       "cfprIdentIdentRequestFsmStageTable": cfprIdentIdentRequestFsmStageTable,
       "cfprIdentIdentRequestFsmStageEntry": cfprIdentIdentRequestFsmStageEntry,
       "cfprIdentIdentRequestFsmStageInstanceId": cfprIdentIdentRequestFsmStageInstanceId,
       "cfprIdentIdentRequestFsmStageDn": cfprIdentIdentRequestFsmStageDn,
       "cfprIdentIdentRequestFsmStageRn": cfprIdentIdentRequestFsmStageRn,
       "cfprIdentIdentRequestFsmStageDescrData": cfprIdentIdentRequestFsmStageDescrData,
       "cfprIdentIdentRequestFsmStageLastUpdateTime": cfprIdentIdentRequestFsmStageLastUpdateTime,
       "cfprIdentIdentRequestFsmStageName": cfprIdentIdentRequestFsmStageName,
       "cfprIdentIdentRequestFsmStageOrder": cfprIdentIdentRequestFsmStageOrder,
       "cfprIdentIdentRequestFsmStageRetry": cfprIdentIdentRequestFsmStageRetry,
       "cfprIdentIdentRequestFsmStageStageStatus": cfprIdentIdentRequestFsmStageStageStatus,
       "cfprIdentIdentRequestFsmTaskTable": cfprIdentIdentRequestFsmTaskTable,
       "cfprIdentIdentRequestFsmTaskEntry": cfprIdentIdentRequestFsmTaskEntry,
       "cfprIdentIdentRequestFsmTaskInstanceId": cfprIdentIdentRequestFsmTaskInstanceId,
       "cfprIdentIdentRequestFsmTaskDn": cfprIdentIdentRequestFsmTaskDn,
       "cfprIdentIdentRequestFsmTaskRn": cfprIdentIdentRequestFsmTaskRn,
       "cfprIdentIdentRequestFsmTaskCompletion": cfprIdentIdentRequestFsmTaskCompletion,
       "cfprIdentIdentRequestFsmTaskFlags": cfprIdentIdentRequestFsmTaskFlags,
       "cfprIdentIdentRequestFsmTaskItem": cfprIdentIdentRequestFsmTaskItem,
       "cfprIdentIdentRequestFsmTaskSeqId": cfprIdentIdentRequestFsmTaskSeqId,
       "cfprIdentMetaSystemTable": cfprIdentMetaSystemTable,
       "cfprIdentMetaSystemEntry": cfprIdentMetaSystemEntry,
       "cfprIdentMetaSystemInstanceId": cfprIdentMetaSystemInstanceId,
       "cfprIdentMetaSystemDn": cfprIdentMetaSystemDn,
       "cfprIdentMetaSystemRn": cfprIdentMetaSystemRn,
       "cfprIdentMetaSystemFsmDescr": cfprIdentMetaSystemFsmDescr,
       "cfprIdentMetaSystemFsmPrev": cfprIdentMetaSystemFsmPrev,
       "cfprIdentMetaSystemFsmProgr": cfprIdentMetaSystemFsmProgr,
       "cfprIdentMetaSystemFsmRmtInvErrCode": cfprIdentMetaSystemFsmRmtInvErrCode,
       "cfprIdentMetaSystemFsmRmtInvErrDescr": cfprIdentMetaSystemFsmRmtInvErrDescr,
       "cfprIdentMetaSystemFsmRmtInvRslt": cfprIdentMetaSystemFsmRmtInvRslt,
       "cfprIdentMetaSystemFsmStageDescr": cfprIdentMetaSystemFsmStageDescr,
       "cfprIdentMetaSystemFsmStamp": cfprIdentMetaSystemFsmStamp,
       "cfprIdentMetaSystemFsmStatus": cfprIdentMetaSystemFsmStatus,
       "cfprIdentMetaSystemFsmTry": cfprIdentMetaSystemFsmTry,
       "cfprIdentMetaSystemGeneration": cfprIdentMetaSystemGeneration,
       "cfprIdentMetaSystemNextReqId": cfprIdentMetaSystemNextReqId,
       "cfprIdentMetaSystemSysid": cfprIdentMetaSystemSysid,
       "cfprIdentMetaSystemFprcGeneration": cfprIdentMetaSystemFprcGeneration,
       "cfprIdentMetaSystemFsmTable": cfprIdentMetaSystemFsmTable,
       "cfprIdentMetaSystemFsmEntry": cfprIdentMetaSystemFsmEntry,
       "cfprIdentMetaSystemFsmInstanceId": cfprIdentMetaSystemFsmInstanceId,
       "cfprIdentMetaSystemFsmDn": cfprIdentMetaSystemFsmDn,
       "cfprIdentMetaSystemFsmRn": cfprIdentMetaSystemFsmRn,
       "cfprIdentMetaSystemFsmCompletionTime": cfprIdentMetaSystemFsmCompletionTime,
       "cfprIdentMetaSystemFsmCurrentFsm": cfprIdentMetaSystemFsmCurrentFsm,
       "cfprIdentMetaSystemFsmDescrData": cfprIdentMetaSystemFsmDescrData,
       "cfprIdentMetaSystemFsmFsmStatus": cfprIdentMetaSystemFsmFsmStatus,
       "cfprIdentMetaSystemFsmProgress": cfprIdentMetaSystemFsmProgress,
       "cfprIdentMetaSystemFsmRmtErrCode": cfprIdentMetaSystemFsmRmtErrCode,
       "cfprIdentMetaSystemFsmRmtErrDescr": cfprIdentMetaSystemFsmRmtErrDescr,
       "cfprIdentMetaSystemFsmRmtRslt": cfprIdentMetaSystemFsmRmtRslt,
       "cfprIdentMetaSystemFsmStageTable": cfprIdentMetaSystemFsmStageTable,
       "cfprIdentMetaSystemFsmStageEntry": cfprIdentMetaSystemFsmStageEntry,
       "cfprIdentMetaSystemFsmStageInstanceId": cfprIdentMetaSystemFsmStageInstanceId,
       "cfprIdentMetaSystemFsmStageDn": cfprIdentMetaSystemFsmStageDn,
       "cfprIdentMetaSystemFsmStageRn": cfprIdentMetaSystemFsmStageRn,
       "cfprIdentMetaSystemFsmStageDescrData": cfprIdentMetaSystemFsmStageDescrData,
       "cfprIdentMetaSystemFsmStageLastUpdateTime": cfprIdentMetaSystemFsmStageLastUpdateTime,
       "cfprIdentMetaSystemFsmStageName": cfprIdentMetaSystemFsmStageName,
       "cfprIdentMetaSystemFsmStageOrder": cfprIdentMetaSystemFsmStageOrder,
       "cfprIdentMetaSystemFsmStageRetry": cfprIdentMetaSystemFsmStageRetry,
       "cfprIdentMetaSystemFsmStageStageStatus": cfprIdentMetaSystemFsmStageStageStatus,
       "cfprIdentMetaSystemFsmTaskTable": cfprIdentMetaSystemFsmTaskTable,
       "cfprIdentMetaSystemFsmTaskEntry": cfprIdentMetaSystemFsmTaskEntry,
       "cfprIdentMetaSystemFsmTaskInstanceId": cfprIdentMetaSystemFsmTaskInstanceId,
       "cfprIdentMetaSystemFsmTaskDn": cfprIdentMetaSystemFsmTaskDn,
       "cfprIdentMetaSystemFsmTaskRn": cfprIdentMetaSystemFsmTaskRn,
       "cfprIdentMetaSystemFsmTaskCompletion": cfprIdentMetaSystemFsmTaskCompletion,
       "cfprIdentMetaSystemFsmTaskFlags": cfprIdentMetaSystemFsmTaskFlags,
       "cfprIdentMetaSystemFsmTaskItem": cfprIdentMetaSystemFsmTaskItem,
       "cfprIdentMetaSystemFsmTaskSeqId": cfprIdentMetaSystemFsmTaskSeqId,
       "cfprIdentMetaVerseTable": cfprIdentMetaVerseTable,
       "cfprIdentMetaVerseEntry": cfprIdentMetaVerseEntry,
       "cfprIdentMetaVerseInstanceId": cfprIdentMetaVerseInstanceId,
       "cfprIdentMetaVerseDn": cfprIdentMetaVerseDn,
       "cfprIdentMetaVerseRn": cfprIdentMetaVerseRn,
       "cfprIdentRequestEpTable": cfprIdentRequestEpTable,
       "cfprIdentRequestEpEntry": cfprIdentRequestEpEntry,
       "cfprIdentRequestEpInstanceId": cfprIdentRequestEpInstanceId,
       "cfprIdentRequestEpDn": cfprIdentRequestEpDn,
       "cfprIdentRequestEpRn": cfprIdentRequestEpRn,
       "cfprIdentRequestEpReqDn": cfprIdentRequestEpReqDn,
       "cfprIdentRequestEpReqId": cfprIdentRequestEpReqId,
       "cfprIdentSysInfoTable": cfprIdentSysInfoTable,
       "cfprIdentSysInfoEntry": cfprIdentSysInfoEntry,
       "cfprIdentSysInfoInstanceId": cfprIdentSysInfoInstanceId,
       "cfprIdentSysInfoDn": cfprIdentSysInfoDn,
       "cfprIdentSysInfoRn": cfprIdentSysInfoRn,
       "cfprIdentSysInfoGeneration": cfprIdentSysInfoGeneration,
       "cfprIdentSysInfoIsFirstSync": cfprIdentSysInfoIsFirstSync,
       "cfprIdentSysInfoIsSync": cfprIdentSysInfoIsSync,
       "cfprIdentSysInfoIsSyncAllowed": cfprIdentSysInfoIsSyncAllowed,
       "cfprIdentSysInfoFprcGeneration": cfprIdentSysInfoFprcGeneration}
)
