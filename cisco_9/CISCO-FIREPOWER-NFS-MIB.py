# SNMP MIB module (CISCO-FIREPOWER-NFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-NFS-MIB.mib
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

(CfprConditionRemoteInvRslt,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprNfsClientConfigState,
 CfprNfsDefAdminState,
 CfprNfsMntAdminState,
 CfprNfsMntOperState,
 CfprNfsMountDefFsmCurrentFsm,
 CfprNfsMountDefFsmStageName,
 CfprNfsMountDefFsmTaskItem,
 CfprNfsMountInstFsmCurrentFsm,
 CfprNfsMountInstFsmStageName,
 CfprNfsMountInstFsmTaskItem,
 CfprNfsPurpose,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprNfsClientConfigState",
    "CfprNfsDefAdminState",
    "CfprNfsMntAdminState",
    "CfprNfsMntOperState",
    "CfprNfsMountDefFsmCurrentFsm",
    "CfprNfsMountDefFsmStageName",
    "CfprNfsMountDefFsmTaskItem",
    "CfprNfsMountInstFsmCurrentFsm",
    "CfprNfsMountInstFsmStageName",
    "CfprNfsMountInstFsmTaskItem",
    "CfprNfsPurpose",
    "CfprPolicyPolicyOwner")

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

cfprNfsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprNfsEpTable_Object = MibTable
cfprNfsEpTable = _CfprNfsEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 1)
)
if mibBuilder.loadTexts:
    cfprNfsEpTable.setStatus("current")
_CfprNfsEpEntry_Object = MibTableRow
cfprNfsEpEntry = _CfprNfsEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 1, 1)
)
cfprNfsEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsEpEntry.setStatus("current")
_CfprNfsEpInstanceId_Type = CfprManagedObjectId
_CfprNfsEpInstanceId_Object = MibTableColumn
cfprNfsEpInstanceId = _CfprNfsEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 1, 1, 1),
    _CfprNfsEpInstanceId_Type()
)
cfprNfsEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsEpInstanceId.setStatus("current")
_CfprNfsEpDn_Type = CfprManagedObjectDn
_CfprNfsEpDn_Object = MibTableColumn
cfprNfsEpDn = _CfprNfsEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 1, 1, 2),
    _CfprNfsEpDn_Type()
)
cfprNfsEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsEpDn.setStatus("current")
_CfprNfsEpRn_Type = SnmpAdminString
_CfprNfsEpRn_Object = MibTableColumn
cfprNfsEpRn = _CfprNfsEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 1, 1, 3),
    _CfprNfsEpRn_Type()
)
cfprNfsEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsEpRn.setStatus("current")
_CfprNfsMountDefTable_Object = MibTable
cfprNfsMountDefTable = _CfprNfsMountDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2)
)
if mibBuilder.loadTexts:
    cfprNfsMountDefTable.setStatus("current")
_CfprNfsMountDefEntry_Object = MibTableRow
cfprNfsMountDefEntry = _CfprNfsMountDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1)
)
cfprNfsMountDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsMountDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsMountDefEntry.setStatus("current")
_CfprNfsMountDefInstanceId_Type = CfprManagedObjectId
_CfprNfsMountDefInstanceId_Object = MibTableColumn
cfprNfsMountDefInstanceId = _CfprNfsMountDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 1),
    _CfprNfsMountDefInstanceId_Type()
)
cfprNfsMountDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsMountDefInstanceId.setStatus("current")
_CfprNfsMountDefDn_Type = CfprManagedObjectDn
_CfprNfsMountDefDn_Object = MibTableColumn
cfprNfsMountDefDn = _CfprNfsMountDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 2),
    _CfprNfsMountDefDn_Type()
)
cfprNfsMountDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefDn.setStatus("current")
_CfprNfsMountDefRn_Type = SnmpAdminString
_CfprNfsMountDefRn_Object = MibTableColumn
cfprNfsMountDefRn = _CfprNfsMountDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 3),
    _CfprNfsMountDefRn_Type()
)
cfprNfsMountDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefRn.setStatus("current")
_CfprNfsMountDefAdminState_Type = CfprNfsDefAdminState
_CfprNfsMountDefAdminState_Object = MibTableColumn
cfprNfsMountDefAdminState = _CfprNfsMountDefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 4),
    _CfprNfsMountDefAdminState_Type()
)
cfprNfsMountDefAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefAdminState.setStatus("current")
_CfprNfsMountDefDescr_Type = SnmpAdminString
_CfprNfsMountDefDescr_Object = MibTableColumn
cfprNfsMountDefDescr = _CfprNfsMountDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 5),
    _CfprNfsMountDefDescr_Type()
)
cfprNfsMountDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefDescr.setStatus("current")
_CfprNfsMountDefFltAggr_Type = Unsigned64
_CfprNfsMountDefFltAggr_Object = MibTableColumn
cfprNfsMountDefFltAggr = _CfprNfsMountDefFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 6),
    _CfprNfsMountDefFltAggr_Type()
)
cfprNfsMountDefFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFltAggr.setStatus("current")
_CfprNfsMountDefFsmDescr_Type = SnmpAdminString
_CfprNfsMountDefFsmDescr_Object = MibTableColumn
cfprNfsMountDefFsmDescr = _CfprNfsMountDefFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 7),
    _CfprNfsMountDefFsmDescr_Type()
)
cfprNfsMountDefFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmDescr.setStatus("current")
_CfprNfsMountDefFsmPrev_Type = SnmpAdminString
_CfprNfsMountDefFsmPrev_Object = MibTableColumn
cfprNfsMountDefFsmPrev = _CfprNfsMountDefFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 8),
    _CfprNfsMountDefFsmPrev_Type()
)
cfprNfsMountDefFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmPrev.setStatus("current")
_CfprNfsMountDefFsmProgr_Type = Gauge32
_CfprNfsMountDefFsmProgr_Object = MibTableColumn
cfprNfsMountDefFsmProgr = _CfprNfsMountDefFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 9),
    _CfprNfsMountDefFsmProgr_Type()
)
cfprNfsMountDefFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmProgr.setStatus("current")
_CfprNfsMountDefFsmRmtInvErrCode_Type = Gauge32
_CfprNfsMountDefFsmRmtInvErrCode_Object = MibTableColumn
cfprNfsMountDefFsmRmtInvErrCode = _CfprNfsMountDefFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 10),
    _CfprNfsMountDefFsmRmtInvErrCode_Type()
)
cfprNfsMountDefFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmRmtInvErrCode.setStatus("current")
_CfprNfsMountDefFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprNfsMountDefFsmRmtInvErrDescr_Object = MibTableColumn
cfprNfsMountDefFsmRmtInvErrDescr = _CfprNfsMountDefFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 11),
    _CfprNfsMountDefFsmRmtInvErrDescr_Type()
)
cfprNfsMountDefFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmRmtInvErrDescr.setStatus("current")
_CfprNfsMountDefFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprNfsMountDefFsmRmtInvRslt_Object = MibTableColumn
cfprNfsMountDefFsmRmtInvRslt = _CfprNfsMountDefFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 12),
    _CfprNfsMountDefFsmRmtInvRslt_Type()
)
cfprNfsMountDefFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmRmtInvRslt.setStatus("current")
_CfprNfsMountDefFsmStageDescr_Type = SnmpAdminString
_CfprNfsMountDefFsmStageDescr_Object = MibTableColumn
cfprNfsMountDefFsmStageDescr = _CfprNfsMountDefFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 13),
    _CfprNfsMountDefFsmStageDescr_Type()
)
cfprNfsMountDefFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageDescr.setStatus("current")
_CfprNfsMountDefFsmStamp_Type = DateAndTime
_CfprNfsMountDefFsmStamp_Object = MibTableColumn
cfprNfsMountDefFsmStamp = _CfprNfsMountDefFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 14),
    _CfprNfsMountDefFsmStamp_Type()
)
cfprNfsMountDefFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStamp.setStatus("current")
_CfprNfsMountDefFsmStatus_Type = SnmpAdminString
_CfprNfsMountDefFsmStatus_Object = MibTableColumn
cfprNfsMountDefFsmStatus = _CfprNfsMountDefFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 15),
    _CfprNfsMountDefFsmStatus_Type()
)
cfprNfsMountDefFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStatus.setStatus("current")
_CfprNfsMountDefFsmTry_Type = Gauge32
_CfprNfsMountDefFsmTry_Object = MibTableColumn
cfprNfsMountDefFsmTry = _CfprNfsMountDefFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 16),
    _CfprNfsMountDefFsmTry_Type()
)
cfprNfsMountDefFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTry.setStatus("current")
_CfprNfsMountDefIntId_Type = SnmpAdminString
_CfprNfsMountDefIntId_Object = MibTableColumn
cfprNfsMountDefIntId = _CfprNfsMountDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 17),
    _CfprNfsMountDefIntId_Type()
)
cfprNfsMountDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefIntId.setStatus("current")
_CfprNfsMountDefLocalDir_Type = SnmpAdminString
_CfprNfsMountDefLocalDir_Object = MibTableColumn
cfprNfsMountDefLocalDir = _CfprNfsMountDefLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 18),
    _CfprNfsMountDefLocalDir_Type()
)
cfprNfsMountDefLocalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefLocalDir.setStatus("current")
_CfprNfsMountDefName_Type = SnmpAdminString
_CfprNfsMountDefName_Object = MibTableColumn
cfprNfsMountDefName = _CfprNfsMountDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 19),
    _CfprNfsMountDefName_Type()
)
cfprNfsMountDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefName.setStatus("current")
_CfprNfsMountDefPolicyLevel_Type = Gauge32
_CfprNfsMountDefPolicyLevel_Object = MibTableColumn
cfprNfsMountDefPolicyLevel = _CfprNfsMountDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 20),
    _CfprNfsMountDefPolicyLevel_Type()
)
cfprNfsMountDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefPolicyLevel.setStatus("current")
_CfprNfsMountDefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprNfsMountDefPolicyOwner_Object = MibTableColumn
cfprNfsMountDefPolicyOwner = _CfprNfsMountDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 21),
    _CfprNfsMountDefPolicyOwner_Type()
)
cfprNfsMountDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefPolicyOwner.setStatus("current")
_CfprNfsMountDefPurpose_Type = CfprNfsPurpose
_CfprNfsMountDefPurpose_Object = MibTableColumn
cfprNfsMountDefPurpose = _CfprNfsMountDefPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 22),
    _CfprNfsMountDefPurpose_Type()
)
cfprNfsMountDefPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefPurpose.setStatus("current")
_CfprNfsMountDefRemoteDir_Type = SnmpAdminString
_CfprNfsMountDefRemoteDir_Object = MibTableColumn
cfprNfsMountDefRemoteDir = _CfprNfsMountDefRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 23),
    _CfprNfsMountDefRemoteDir_Type()
)
cfprNfsMountDefRemoteDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefRemoteDir.setStatus("current")
_CfprNfsMountDefServer_Type = SnmpAdminString
_CfprNfsMountDefServer_Object = MibTableColumn
cfprNfsMountDefServer = _CfprNfsMountDefServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 2, 1, 24),
    _CfprNfsMountDefServer_Type()
)
cfprNfsMountDefServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefServer.setStatus("current")
_CfprNfsMountDefFsmTable_Object = MibTable
cfprNfsMountDefFsmTable = _CfprNfsMountDefFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3)
)
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTable.setStatus("current")
_CfprNfsMountDefFsmEntry_Object = MibTableRow
cfprNfsMountDefFsmEntry = _CfprNfsMountDefFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1)
)
cfprNfsMountDefFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsMountDefFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmEntry.setStatus("current")
_CfprNfsMountDefFsmInstanceId_Type = CfprManagedObjectId
_CfprNfsMountDefFsmInstanceId_Object = MibTableColumn
cfprNfsMountDefFsmInstanceId = _CfprNfsMountDefFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 1),
    _CfprNfsMountDefFsmInstanceId_Type()
)
cfprNfsMountDefFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmInstanceId.setStatus("current")
_CfprNfsMountDefFsmDn_Type = CfprManagedObjectDn
_CfprNfsMountDefFsmDn_Object = MibTableColumn
cfprNfsMountDefFsmDn = _CfprNfsMountDefFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 2),
    _CfprNfsMountDefFsmDn_Type()
)
cfprNfsMountDefFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmDn.setStatus("current")
_CfprNfsMountDefFsmRn_Type = SnmpAdminString
_CfprNfsMountDefFsmRn_Object = MibTableColumn
cfprNfsMountDefFsmRn = _CfprNfsMountDefFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 3),
    _CfprNfsMountDefFsmRn_Type()
)
cfprNfsMountDefFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmRn.setStatus("current")
_CfprNfsMountDefFsmCompletionTime_Type = DateAndTime
_CfprNfsMountDefFsmCompletionTime_Object = MibTableColumn
cfprNfsMountDefFsmCompletionTime = _CfprNfsMountDefFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 4),
    _CfprNfsMountDefFsmCompletionTime_Type()
)
cfprNfsMountDefFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmCompletionTime.setStatus("current")
_CfprNfsMountDefFsmCurrentFsm_Type = CfprNfsMountDefFsmCurrentFsm
_CfprNfsMountDefFsmCurrentFsm_Object = MibTableColumn
cfprNfsMountDefFsmCurrentFsm = _CfprNfsMountDefFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 5),
    _CfprNfsMountDefFsmCurrentFsm_Type()
)
cfprNfsMountDefFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmCurrentFsm.setStatus("current")
_CfprNfsMountDefFsmDescrData_Type = SnmpAdminString
_CfprNfsMountDefFsmDescrData_Object = MibTableColumn
cfprNfsMountDefFsmDescrData = _CfprNfsMountDefFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 6),
    _CfprNfsMountDefFsmDescrData_Type()
)
cfprNfsMountDefFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmDescrData.setStatus("current")
_CfprNfsMountDefFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprNfsMountDefFsmFsmStatus_Object = MibTableColumn
cfprNfsMountDefFsmFsmStatus = _CfprNfsMountDefFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 7),
    _CfprNfsMountDefFsmFsmStatus_Type()
)
cfprNfsMountDefFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmFsmStatus.setStatus("current")
_CfprNfsMountDefFsmProgress_Type = Gauge32
_CfprNfsMountDefFsmProgress_Object = MibTableColumn
cfprNfsMountDefFsmProgress = _CfprNfsMountDefFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 8),
    _CfprNfsMountDefFsmProgress_Type()
)
cfprNfsMountDefFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmProgress.setStatus("current")
_CfprNfsMountDefFsmRmtErrCode_Type = Gauge32
_CfprNfsMountDefFsmRmtErrCode_Object = MibTableColumn
cfprNfsMountDefFsmRmtErrCode = _CfprNfsMountDefFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 9),
    _CfprNfsMountDefFsmRmtErrCode_Type()
)
cfprNfsMountDefFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmRmtErrCode.setStatus("current")
_CfprNfsMountDefFsmRmtErrDescr_Type = SnmpAdminString
_CfprNfsMountDefFsmRmtErrDescr_Object = MibTableColumn
cfprNfsMountDefFsmRmtErrDescr = _CfprNfsMountDefFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 10),
    _CfprNfsMountDefFsmRmtErrDescr_Type()
)
cfprNfsMountDefFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmRmtErrDescr.setStatus("current")
_CfprNfsMountDefFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprNfsMountDefFsmRmtRslt_Object = MibTableColumn
cfprNfsMountDefFsmRmtRslt = _CfprNfsMountDefFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 3, 1, 11),
    _CfprNfsMountDefFsmRmtRslt_Type()
)
cfprNfsMountDefFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmRmtRslt.setStatus("current")
_CfprNfsMountDefFsmStageTable_Object = MibTable
cfprNfsMountDefFsmStageTable = _CfprNfsMountDefFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4)
)
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageTable.setStatus("current")
_CfprNfsMountDefFsmStageEntry_Object = MibTableRow
cfprNfsMountDefFsmStageEntry = _CfprNfsMountDefFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1)
)
cfprNfsMountDefFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsMountDefFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageEntry.setStatus("current")
_CfprNfsMountDefFsmStageInstanceId_Type = CfprManagedObjectId
_CfprNfsMountDefFsmStageInstanceId_Object = MibTableColumn
cfprNfsMountDefFsmStageInstanceId = _CfprNfsMountDefFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 1),
    _CfprNfsMountDefFsmStageInstanceId_Type()
)
cfprNfsMountDefFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageInstanceId.setStatus("current")
_CfprNfsMountDefFsmStageDn_Type = CfprManagedObjectDn
_CfprNfsMountDefFsmStageDn_Object = MibTableColumn
cfprNfsMountDefFsmStageDn = _CfprNfsMountDefFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 2),
    _CfprNfsMountDefFsmStageDn_Type()
)
cfprNfsMountDefFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageDn.setStatus("current")
_CfprNfsMountDefFsmStageRn_Type = SnmpAdminString
_CfprNfsMountDefFsmStageRn_Object = MibTableColumn
cfprNfsMountDefFsmStageRn = _CfprNfsMountDefFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 3),
    _CfprNfsMountDefFsmStageRn_Type()
)
cfprNfsMountDefFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageRn.setStatus("current")
_CfprNfsMountDefFsmStageDescrData_Type = SnmpAdminString
_CfprNfsMountDefFsmStageDescrData_Object = MibTableColumn
cfprNfsMountDefFsmStageDescrData = _CfprNfsMountDefFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 4),
    _CfprNfsMountDefFsmStageDescrData_Type()
)
cfprNfsMountDefFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageDescrData.setStatus("current")
_CfprNfsMountDefFsmStageLastUpdateTime_Type = DateAndTime
_CfprNfsMountDefFsmStageLastUpdateTime_Object = MibTableColumn
cfprNfsMountDefFsmStageLastUpdateTime = _CfprNfsMountDefFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 5),
    _CfprNfsMountDefFsmStageLastUpdateTime_Type()
)
cfprNfsMountDefFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageLastUpdateTime.setStatus("current")
_CfprNfsMountDefFsmStageName_Type = CfprNfsMountDefFsmStageName
_CfprNfsMountDefFsmStageName_Object = MibTableColumn
cfprNfsMountDefFsmStageName = _CfprNfsMountDefFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 6),
    _CfprNfsMountDefFsmStageName_Type()
)
cfprNfsMountDefFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageName.setStatus("current")
_CfprNfsMountDefFsmStageOrder_Type = Gauge32
_CfprNfsMountDefFsmStageOrder_Object = MibTableColumn
cfprNfsMountDefFsmStageOrder = _CfprNfsMountDefFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 7),
    _CfprNfsMountDefFsmStageOrder_Type()
)
cfprNfsMountDefFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageOrder.setStatus("current")
_CfprNfsMountDefFsmStageRetry_Type = Gauge32
_CfprNfsMountDefFsmStageRetry_Object = MibTableColumn
cfprNfsMountDefFsmStageRetry = _CfprNfsMountDefFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 8),
    _CfprNfsMountDefFsmStageRetry_Type()
)
cfprNfsMountDefFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageRetry.setStatus("current")
_CfprNfsMountDefFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprNfsMountDefFsmStageStageStatus_Object = MibTableColumn
cfprNfsMountDefFsmStageStageStatus = _CfprNfsMountDefFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 4, 1, 9),
    _CfprNfsMountDefFsmStageStageStatus_Type()
)
cfprNfsMountDefFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmStageStageStatus.setStatus("current")
_CfprNfsMountDefFsmTaskTable_Object = MibTable
cfprNfsMountDefFsmTaskTable = _CfprNfsMountDefFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5)
)
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskTable.setStatus("current")
_CfprNfsMountDefFsmTaskEntry_Object = MibTableRow
cfprNfsMountDefFsmTaskEntry = _CfprNfsMountDefFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5, 1)
)
cfprNfsMountDefFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsMountDefFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskEntry.setStatus("current")
_CfprNfsMountDefFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprNfsMountDefFsmTaskInstanceId_Object = MibTableColumn
cfprNfsMountDefFsmTaskInstanceId = _CfprNfsMountDefFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5, 1, 1),
    _CfprNfsMountDefFsmTaskInstanceId_Type()
)
cfprNfsMountDefFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskInstanceId.setStatus("current")
_CfprNfsMountDefFsmTaskDn_Type = CfprManagedObjectDn
_CfprNfsMountDefFsmTaskDn_Object = MibTableColumn
cfprNfsMountDefFsmTaskDn = _CfprNfsMountDefFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5, 1, 2),
    _CfprNfsMountDefFsmTaskDn_Type()
)
cfprNfsMountDefFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskDn.setStatus("current")
_CfprNfsMountDefFsmTaskRn_Type = SnmpAdminString
_CfprNfsMountDefFsmTaskRn_Object = MibTableColumn
cfprNfsMountDefFsmTaskRn = _CfprNfsMountDefFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5, 1, 3),
    _CfprNfsMountDefFsmTaskRn_Type()
)
cfprNfsMountDefFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskRn.setStatus("current")
_CfprNfsMountDefFsmTaskCompletion_Type = CfprFsmCompletion
_CfprNfsMountDefFsmTaskCompletion_Object = MibTableColumn
cfprNfsMountDefFsmTaskCompletion = _CfprNfsMountDefFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5, 1, 4),
    _CfprNfsMountDefFsmTaskCompletion_Type()
)
cfprNfsMountDefFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskCompletion.setStatus("current")
_CfprNfsMountDefFsmTaskFlags_Type = CfprFsmFlags
_CfprNfsMountDefFsmTaskFlags_Object = MibTableColumn
cfprNfsMountDefFsmTaskFlags = _CfprNfsMountDefFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5, 1, 5),
    _CfprNfsMountDefFsmTaskFlags_Type()
)
cfprNfsMountDefFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskFlags.setStatus("current")
_CfprNfsMountDefFsmTaskItem_Type = CfprNfsMountDefFsmTaskItem
_CfprNfsMountDefFsmTaskItem_Object = MibTableColumn
cfprNfsMountDefFsmTaskItem = _CfprNfsMountDefFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5, 1, 6),
    _CfprNfsMountDefFsmTaskItem_Type()
)
cfprNfsMountDefFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskItem.setStatus("current")
_CfprNfsMountDefFsmTaskSeqId_Type = Gauge32
_CfprNfsMountDefFsmTaskSeqId_Object = MibTableColumn
cfprNfsMountDefFsmTaskSeqId = _CfprNfsMountDefFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 5, 1, 7),
    _CfprNfsMountDefFsmTaskSeqId_Type()
)
cfprNfsMountDefFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountDefFsmTaskSeqId.setStatus("current")
_CfprNfsMountInstTable_Object = MibTable
cfprNfsMountInstTable = _CfprNfsMountInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6)
)
if mibBuilder.loadTexts:
    cfprNfsMountInstTable.setStatus("current")
_CfprNfsMountInstEntry_Object = MibTableRow
cfprNfsMountInstEntry = _CfprNfsMountInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1)
)
cfprNfsMountInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsMountInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsMountInstEntry.setStatus("current")
_CfprNfsMountInstInstanceId_Type = CfprManagedObjectId
_CfprNfsMountInstInstanceId_Object = MibTableColumn
cfprNfsMountInstInstanceId = _CfprNfsMountInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 1),
    _CfprNfsMountInstInstanceId_Type()
)
cfprNfsMountInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsMountInstInstanceId.setStatus("current")
_CfprNfsMountInstDn_Type = CfprManagedObjectDn
_CfprNfsMountInstDn_Object = MibTableColumn
cfprNfsMountInstDn = _CfprNfsMountInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 2),
    _CfprNfsMountInstDn_Type()
)
cfprNfsMountInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstDn.setStatus("current")
_CfprNfsMountInstRn_Type = SnmpAdminString
_CfprNfsMountInstRn_Object = MibTableColumn
cfprNfsMountInstRn = _CfprNfsMountInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 3),
    _CfprNfsMountInstRn_Type()
)
cfprNfsMountInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstRn.setStatus("current")
_CfprNfsMountInstAdminState_Type = CfprNfsMntAdminState
_CfprNfsMountInstAdminState_Object = MibTableColumn
cfprNfsMountInstAdminState = _CfprNfsMountInstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 4),
    _CfprNfsMountInstAdminState_Type()
)
cfprNfsMountInstAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstAdminState.setStatus("current")
_CfprNfsMountInstClientConfigState_Type = CfprNfsClientConfigState
_CfprNfsMountInstClientConfigState_Object = MibTableColumn
cfprNfsMountInstClientConfigState = _CfprNfsMountInstClientConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 5),
    _CfprNfsMountInstClientConfigState_Type()
)
cfprNfsMountInstClientConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstClientConfigState.setStatus("current")
_CfprNfsMountInstDefDn_Type = SnmpAdminString
_CfprNfsMountInstDefDn_Object = MibTableColumn
cfprNfsMountInstDefDn = _CfprNfsMountInstDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 6),
    _CfprNfsMountInstDefDn_Type()
)
cfprNfsMountInstDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstDefDn.setStatus("current")
_CfprNfsMountInstFsmDescr_Type = SnmpAdminString
_CfprNfsMountInstFsmDescr_Object = MibTableColumn
cfprNfsMountInstFsmDescr = _CfprNfsMountInstFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 7),
    _CfprNfsMountInstFsmDescr_Type()
)
cfprNfsMountInstFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmDescr.setStatus("current")
_CfprNfsMountInstFsmPrev_Type = SnmpAdminString
_CfprNfsMountInstFsmPrev_Object = MibTableColumn
cfprNfsMountInstFsmPrev = _CfprNfsMountInstFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 8),
    _CfprNfsMountInstFsmPrev_Type()
)
cfprNfsMountInstFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmPrev.setStatus("current")
_CfprNfsMountInstFsmProgr_Type = Gauge32
_CfprNfsMountInstFsmProgr_Object = MibTableColumn
cfprNfsMountInstFsmProgr = _CfprNfsMountInstFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 9),
    _CfprNfsMountInstFsmProgr_Type()
)
cfprNfsMountInstFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmProgr.setStatus("current")
_CfprNfsMountInstFsmRmtInvErrCode_Type = Gauge32
_CfprNfsMountInstFsmRmtInvErrCode_Object = MibTableColumn
cfprNfsMountInstFsmRmtInvErrCode = _CfprNfsMountInstFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 10),
    _CfprNfsMountInstFsmRmtInvErrCode_Type()
)
cfprNfsMountInstFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmRmtInvErrCode.setStatus("current")
_CfprNfsMountInstFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprNfsMountInstFsmRmtInvErrDescr_Object = MibTableColumn
cfprNfsMountInstFsmRmtInvErrDescr = _CfprNfsMountInstFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 11),
    _CfprNfsMountInstFsmRmtInvErrDescr_Type()
)
cfprNfsMountInstFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmRmtInvErrDescr.setStatus("current")
_CfprNfsMountInstFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprNfsMountInstFsmRmtInvRslt_Object = MibTableColumn
cfprNfsMountInstFsmRmtInvRslt = _CfprNfsMountInstFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 12),
    _CfprNfsMountInstFsmRmtInvRslt_Type()
)
cfprNfsMountInstFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmRmtInvRslt.setStatus("current")
_CfprNfsMountInstFsmStageDescr_Type = SnmpAdminString
_CfprNfsMountInstFsmStageDescr_Object = MibTableColumn
cfprNfsMountInstFsmStageDescr = _CfprNfsMountInstFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 13),
    _CfprNfsMountInstFsmStageDescr_Type()
)
cfprNfsMountInstFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageDescr.setStatus("current")
_CfprNfsMountInstFsmStamp_Type = DateAndTime
_CfprNfsMountInstFsmStamp_Object = MibTableColumn
cfprNfsMountInstFsmStamp = _CfprNfsMountInstFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 14),
    _CfprNfsMountInstFsmStamp_Type()
)
cfprNfsMountInstFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStamp.setStatus("current")
_CfprNfsMountInstFsmStatus_Type = SnmpAdminString
_CfprNfsMountInstFsmStatus_Object = MibTableColumn
cfprNfsMountInstFsmStatus = _CfprNfsMountInstFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 15),
    _CfprNfsMountInstFsmStatus_Type()
)
cfprNfsMountInstFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStatus.setStatus("current")
_CfprNfsMountInstFsmTry_Type = Gauge32
_CfprNfsMountInstFsmTry_Object = MibTableColumn
cfprNfsMountInstFsmTry = _CfprNfsMountInstFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 16),
    _CfprNfsMountInstFsmTry_Type()
)
cfprNfsMountInstFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTry.setStatus("current")
_CfprNfsMountInstLocalDir_Type = SnmpAdminString
_CfprNfsMountInstLocalDir_Object = MibTableColumn
cfprNfsMountInstLocalDir = _CfprNfsMountInstLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 17),
    _CfprNfsMountInstLocalDir_Type()
)
cfprNfsMountInstLocalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstLocalDir.setStatus("current")
_CfprNfsMountInstName_Type = SnmpAdminString
_CfprNfsMountInstName_Object = MibTableColumn
cfprNfsMountInstName = _CfprNfsMountInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 18),
    _CfprNfsMountInstName_Type()
)
cfprNfsMountInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstName.setStatus("current")
_CfprNfsMountInstOperState_Type = CfprNfsMntOperState
_CfprNfsMountInstOperState_Object = MibTableColumn
cfprNfsMountInstOperState = _CfprNfsMountInstOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 19),
    _CfprNfsMountInstOperState_Type()
)
cfprNfsMountInstOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstOperState.setStatus("current")
_CfprNfsMountInstPurpose_Type = CfprNfsPurpose
_CfprNfsMountInstPurpose_Object = MibTableColumn
cfprNfsMountInstPurpose = _CfprNfsMountInstPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 20),
    _CfprNfsMountInstPurpose_Type()
)
cfprNfsMountInstPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstPurpose.setStatus("current")
_CfprNfsMountInstRemoteDir_Type = SnmpAdminString
_CfprNfsMountInstRemoteDir_Object = MibTableColumn
cfprNfsMountInstRemoteDir = _CfprNfsMountInstRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 21),
    _CfprNfsMountInstRemoteDir_Type()
)
cfprNfsMountInstRemoteDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstRemoteDir.setStatus("current")
_CfprNfsMountInstServer_Type = SnmpAdminString
_CfprNfsMountInstServer_Object = MibTableColumn
cfprNfsMountInstServer = _CfprNfsMountInstServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 6, 1, 22),
    _CfprNfsMountInstServer_Type()
)
cfprNfsMountInstServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstServer.setStatus("current")
_CfprNfsMountInstFsmTable_Object = MibTable
cfprNfsMountInstFsmTable = _CfprNfsMountInstFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7)
)
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTable.setStatus("current")
_CfprNfsMountInstFsmEntry_Object = MibTableRow
cfprNfsMountInstFsmEntry = _CfprNfsMountInstFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1)
)
cfprNfsMountInstFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsMountInstFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmEntry.setStatus("current")
_CfprNfsMountInstFsmInstanceId_Type = CfprManagedObjectId
_CfprNfsMountInstFsmInstanceId_Object = MibTableColumn
cfprNfsMountInstFsmInstanceId = _CfprNfsMountInstFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 1),
    _CfprNfsMountInstFsmInstanceId_Type()
)
cfprNfsMountInstFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmInstanceId.setStatus("current")
_CfprNfsMountInstFsmDn_Type = CfprManagedObjectDn
_CfprNfsMountInstFsmDn_Object = MibTableColumn
cfprNfsMountInstFsmDn = _CfprNfsMountInstFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 2),
    _CfprNfsMountInstFsmDn_Type()
)
cfprNfsMountInstFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmDn.setStatus("current")
_CfprNfsMountInstFsmRn_Type = SnmpAdminString
_CfprNfsMountInstFsmRn_Object = MibTableColumn
cfprNfsMountInstFsmRn = _CfprNfsMountInstFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 3),
    _CfprNfsMountInstFsmRn_Type()
)
cfprNfsMountInstFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmRn.setStatus("current")
_CfprNfsMountInstFsmCompletionTime_Type = DateAndTime
_CfprNfsMountInstFsmCompletionTime_Object = MibTableColumn
cfprNfsMountInstFsmCompletionTime = _CfprNfsMountInstFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 4),
    _CfprNfsMountInstFsmCompletionTime_Type()
)
cfprNfsMountInstFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmCompletionTime.setStatus("current")
_CfprNfsMountInstFsmCurrentFsm_Type = CfprNfsMountInstFsmCurrentFsm
_CfprNfsMountInstFsmCurrentFsm_Object = MibTableColumn
cfprNfsMountInstFsmCurrentFsm = _CfprNfsMountInstFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 5),
    _CfprNfsMountInstFsmCurrentFsm_Type()
)
cfprNfsMountInstFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmCurrentFsm.setStatus("current")
_CfprNfsMountInstFsmDescrData_Type = SnmpAdminString
_CfprNfsMountInstFsmDescrData_Object = MibTableColumn
cfprNfsMountInstFsmDescrData = _CfprNfsMountInstFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 6),
    _CfprNfsMountInstFsmDescrData_Type()
)
cfprNfsMountInstFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmDescrData.setStatus("current")
_CfprNfsMountInstFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprNfsMountInstFsmFsmStatus_Object = MibTableColumn
cfprNfsMountInstFsmFsmStatus = _CfprNfsMountInstFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 7),
    _CfprNfsMountInstFsmFsmStatus_Type()
)
cfprNfsMountInstFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmFsmStatus.setStatus("current")
_CfprNfsMountInstFsmProgress_Type = Gauge32
_CfprNfsMountInstFsmProgress_Object = MibTableColumn
cfprNfsMountInstFsmProgress = _CfprNfsMountInstFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 8),
    _CfprNfsMountInstFsmProgress_Type()
)
cfprNfsMountInstFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmProgress.setStatus("current")
_CfprNfsMountInstFsmRmtErrCode_Type = Gauge32
_CfprNfsMountInstFsmRmtErrCode_Object = MibTableColumn
cfprNfsMountInstFsmRmtErrCode = _CfprNfsMountInstFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 9),
    _CfprNfsMountInstFsmRmtErrCode_Type()
)
cfprNfsMountInstFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmRmtErrCode.setStatus("current")
_CfprNfsMountInstFsmRmtErrDescr_Type = SnmpAdminString
_CfprNfsMountInstFsmRmtErrDescr_Object = MibTableColumn
cfprNfsMountInstFsmRmtErrDescr = _CfprNfsMountInstFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 10),
    _CfprNfsMountInstFsmRmtErrDescr_Type()
)
cfprNfsMountInstFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmRmtErrDescr.setStatus("current")
_CfprNfsMountInstFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprNfsMountInstFsmRmtRslt_Object = MibTableColumn
cfprNfsMountInstFsmRmtRslt = _CfprNfsMountInstFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 7, 1, 11),
    _CfprNfsMountInstFsmRmtRslt_Type()
)
cfprNfsMountInstFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmRmtRslt.setStatus("current")
_CfprNfsMountInstFsmStageTable_Object = MibTable
cfprNfsMountInstFsmStageTable = _CfprNfsMountInstFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8)
)
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageTable.setStatus("current")
_CfprNfsMountInstFsmStageEntry_Object = MibTableRow
cfprNfsMountInstFsmStageEntry = _CfprNfsMountInstFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1)
)
cfprNfsMountInstFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsMountInstFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageEntry.setStatus("current")
_CfprNfsMountInstFsmStageInstanceId_Type = CfprManagedObjectId
_CfprNfsMountInstFsmStageInstanceId_Object = MibTableColumn
cfprNfsMountInstFsmStageInstanceId = _CfprNfsMountInstFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 1),
    _CfprNfsMountInstFsmStageInstanceId_Type()
)
cfprNfsMountInstFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageInstanceId.setStatus("current")
_CfprNfsMountInstFsmStageDn_Type = CfprManagedObjectDn
_CfprNfsMountInstFsmStageDn_Object = MibTableColumn
cfprNfsMountInstFsmStageDn = _CfprNfsMountInstFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 2),
    _CfprNfsMountInstFsmStageDn_Type()
)
cfprNfsMountInstFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageDn.setStatus("current")
_CfprNfsMountInstFsmStageRn_Type = SnmpAdminString
_CfprNfsMountInstFsmStageRn_Object = MibTableColumn
cfprNfsMountInstFsmStageRn = _CfprNfsMountInstFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 3),
    _CfprNfsMountInstFsmStageRn_Type()
)
cfprNfsMountInstFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageRn.setStatus("current")
_CfprNfsMountInstFsmStageDescrData_Type = SnmpAdminString
_CfprNfsMountInstFsmStageDescrData_Object = MibTableColumn
cfprNfsMountInstFsmStageDescrData = _CfprNfsMountInstFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 4),
    _CfprNfsMountInstFsmStageDescrData_Type()
)
cfprNfsMountInstFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageDescrData.setStatus("current")
_CfprNfsMountInstFsmStageLastUpdateTime_Type = DateAndTime
_CfprNfsMountInstFsmStageLastUpdateTime_Object = MibTableColumn
cfprNfsMountInstFsmStageLastUpdateTime = _CfprNfsMountInstFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 5),
    _CfprNfsMountInstFsmStageLastUpdateTime_Type()
)
cfprNfsMountInstFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageLastUpdateTime.setStatus("current")
_CfprNfsMountInstFsmStageName_Type = CfprNfsMountInstFsmStageName
_CfprNfsMountInstFsmStageName_Object = MibTableColumn
cfprNfsMountInstFsmStageName = _CfprNfsMountInstFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 6),
    _CfprNfsMountInstFsmStageName_Type()
)
cfprNfsMountInstFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageName.setStatus("current")
_CfprNfsMountInstFsmStageOrder_Type = Gauge32
_CfprNfsMountInstFsmStageOrder_Object = MibTableColumn
cfprNfsMountInstFsmStageOrder = _CfprNfsMountInstFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 7),
    _CfprNfsMountInstFsmStageOrder_Type()
)
cfprNfsMountInstFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageOrder.setStatus("current")
_CfprNfsMountInstFsmStageRetry_Type = Gauge32
_CfprNfsMountInstFsmStageRetry_Object = MibTableColumn
cfprNfsMountInstFsmStageRetry = _CfprNfsMountInstFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 8),
    _CfprNfsMountInstFsmStageRetry_Type()
)
cfprNfsMountInstFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageRetry.setStatus("current")
_CfprNfsMountInstFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprNfsMountInstFsmStageStageStatus_Object = MibTableColumn
cfprNfsMountInstFsmStageStageStatus = _CfprNfsMountInstFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 8, 1, 9),
    _CfprNfsMountInstFsmStageStageStatus_Type()
)
cfprNfsMountInstFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmStageStageStatus.setStatus("current")
_CfprNfsMountInstFsmTaskTable_Object = MibTable
cfprNfsMountInstFsmTaskTable = _CfprNfsMountInstFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9)
)
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskTable.setStatus("current")
_CfprNfsMountInstFsmTaskEntry_Object = MibTableRow
cfprNfsMountInstFsmTaskEntry = _CfprNfsMountInstFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9, 1)
)
cfprNfsMountInstFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NFS-MIB", "cfprNfsMountInstFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskEntry.setStatus("current")
_CfprNfsMountInstFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprNfsMountInstFsmTaskInstanceId_Object = MibTableColumn
cfprNfsMountInstFsmTaskInstanceId = _CfprNfsMountInstFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9, 1, 1),
    _CfprNfsMountInstFsmTaskInstanceId_Type()
)
cfprNfsMountInstFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskInstanceId.setStatus("current")
_CfprNfsMountInstFsmTaskDn_Type = CfprManagedObjectDn
_CfprNfsMountInstFsmTaskDn_Object = MibTableColumn
cfprNfsMountInstFsmTaskDn = _CfprNfsMountInstFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9, 1, 2),
    _CfprNfsMountInstFsmTaskDn_Type()
)
cfprNfsMountInstFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskDn.setStatus("current")
_CfprNfsMountInstFsmTaskRn_Type = SnmpAdminString
_CfprNfsMountInstFsmTaskRn_Object = MibTableColumn
cfprNfsMountInstFsmTaskRn = _CfprNfsMountInstFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9, 1, 3),
    _CfprNfsMountInstFsmTaskRn_Type()
)
cfprNfsMountInstFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskRn.setStatus("current")
_CfprNfsMountInstFsmTaskCompletion_Type = CfprFsmCompletion
_CfprNfsMountInstFsmTaskCompletion_Object = MibTableColumn
cfprNfsMountInstFsmTaskCompletion = _CfprNfsMountInstFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9, 1, 4),
    _CfprNfsMountInstFsmTaskCompletion_Type()
)
cfprNfsMountInstFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskCompletion.setStatus("current")
_CfprNfsMountInstFsmTaskFlags_Type = CfprFsmFlags
_CfprNfsMountInstFsmTaskFlags_Object = MibTableColumn
cfprNfsMountInstFsmTaskFlags = _CfprNfsMountInstFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9, 1, 5),
    _CfprNfsMountInstFsmTaskFlags_Type()
)
cfprNfsMountInstFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskFlags.setStatus("current")
_CfprNfsMountInstFsmTaskItem_Type = CfprNfsMountInstFsmTaskItem
_CfprNfsMountInstFsmTaskItem_Object = MibTableColumn
cfprNfsMountInstFsmTaskItem = _CfprNfsMountInstFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9, 1, 6),
    _CfprNfsMountInstFsmTaskItem_Type()
)
cfprNfsMountInstFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskItem.setStatus("current")
_CfprNfsMountInstFsmTaskSeqId_Type = Gauge32
_CfprNfsMountInstFsmTaskSeqId_Object = MibTableColumn
cfprNfsMountInstFsmTaskSeqId = _CfprNfsMountInstFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 53, 9, 1, 7),
    _CfprNfsMountInstFsmTaskSeqId_Type()
)
cfprNfsMountInstFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNfsMountInstFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-NFS-MIB",
    **{"cfprNfsObjects": cfprNfsObjects,
       "cfprNfsEpTable": cfprNfsEpTable,
       "cfprNfsEpEntry": cfprNfsEpEntry,
       "cfprNfsEpInstanceId": cfprNfsEpInstanceId,
       "cfprNfsEpDn": cfprNfsEpDn,
       "cfprNfsEpRn": cfprNfsEpRn,
       "cfprNfsMountDefTable": cfprNfsMountDefTable,
       "cfprNfsMountDefEntry": cfprNfsMountDefEntry,
       "cfprNfsMountDefInstanceId": cfprNfsMountDefInstanceId,
       "cfprNfsMountDefDn": cfprNfsMountDefDn,
       "cfprNfsMountDefRn": cfprNfsMountDefRn,
       "cfprNfsMountDefAdminState": cfprNfsMountDefAdminState,
       "cfprNfsMountDefDescr": cfprNfsMountDefDescr,
       "cfprNfsMountDefFltAggr": cfprNfsMountDefFltAggr,
       "cfprNfsMountDefFsmDescr": cfprNfsMountDefFsmDescr,
       "cfprNfsMountDefFsmPrev": cfprNfsMountDefFsmPrev,
       "cfprNfsMountDefFsmProgr": cfprNfsMountDefFsmProgr,
       "cfprNfsMountDefFsmRmtInvErrCode": cfprNfsMountDefFsmRmtInvErrCode,
       "cfprNfsMountDefFsmRmtInvErrDescr": cfprNfsMountDefFsmRmtInvErrDescr,
       "cfprNfsMountDefFsmRmtInvRslt": cfprNfsMountDefFsmRmtInvRslt,
       "cfprNfsMountDefFsmStageDescr": cfprNfsMountDefFsmStageDescr,
       "cfprNfsMountDefFsmStamp": cfprNfsMountDefFsmStamp,
       "cfprNfsMountDefFsmStatus": cfprNfsMountDefFsmStatus,
       "cfprNfsMountDefFsmTry": cfprNfsMountDefFsmTry,
       "cfprNfsMountDefIntId": cfprNfsMountDefIntId,
       "cfprNfsMountDefLocalDir": cfprNfsMountDefLocalDir,
       "cfprNfsMountDefName": cfprNfsMountDefName,
       "cfprNfsMountDefPolicyLevel": cfprNfsMountDefPolicyLevel,
       "cfprNfsMountDefPolicyOwner": cfprNfsMountDefPolicyOwner,
       "cfprNfsMountDefPurpose": cfprNfsMountDefPurpose,
       "cfprNfsMountDefRemoteDir": cfprNfsMountDefRemoteDir,
       "cfprNfsMountDefServer": cfprNfsMountDefServer,
       "cfprNfsMountDefFsmTable": cfprNfsMountDefFsmTable,
       "cfprNfsMountDefFsmEntry": cfprNfsMountDefFsmEntry,
       "cfprNfsMountDefFsmInstanceId": cfprNfsMountDefFsmInstanceId,
       "cfprNfsMountDefFsmDn": cfprNfsMountDefFsmDn,
       "cfprNfsMountDefFsmRn": cfprNfsMountDefFsmRn,
       "cfprNfsMountDefFsmCompletionTime": cfprNfsMountDefFsmCompletionTime,
       "cfprNfsMountDefFsmCurrentFsm": cfprNfsMountDefFsmCurrentFsm,
       "cfprNfsMountDefFsmDescrData": cfprNfsMountDefFsmDescrData,
       "cfprNfsMountDefFsmFsmStatus": cfprNfsMountDefFsmFsmStatus,
       "cfprNfsMountDefFsmProgress": cfprNfsMountDefFsmProgress,
       "cfprNfsMountDefFsmRmtErrCode": cfprNfsMountDefFsmRmtErrCode,
       "cfprNfsMountDefFsmRmtErrDescr": cfprNfsMountDefFsmRmtErrDescr,
       "cfprNfsMountDefFsmRmtRslt": cfprNfsMountDefFsmRmtRslt,
       "cfprNfsMountDefFsmStageTable": cfprNfsMountDefFsmStageTable,
       "cfprNfsMountDefFsmStageEntry": cfprNfsMountDefFsmStageEntry,
       "cfprNfsMountDefFsmStageInstanceId": cfprNfsMountDefFsmStageInstanceId,
       "cfprNfsMountDefFsmStageDn": cfprNfsMountDefFsmStageDn,
       "cfprNfsMountDefFsmStageRn": cfprNfsMountDefFsmStageRn,
       "cfprNfsMountDefFsmStageDescrData": cfprNfsMountDefFsmStageDescrData,
       "cfprNfsMountDefFsmStageLastUpdateTime": cfprNfsMountDefFsmStageLastUpdateTime,
       "cfprNfsMountDefFsmStageName": cfprNfsMountDefFsmStageName,
       "cfprNfsMountDefFsmStageOrder": cfprNfsMountDefFsmStageOrder,
       "cfprNfsMountDefFsmStageRetry": cfprNfsMountDefFsmStageRetry,
       "cfprNfsMountDefFsmStageStageStatus": cfprNfsMountDefFsmStageStageStatus,
       "cfprNfsMountDefFsmTaskTable": cfprNfsMountDefFsmTaskTable,
       "cfprNfsMountDefFsmTaskEntry": cfprNfsMountDefFsmTaskEntry,
       "cfprNfsMountDefFsmTaskInstanceId": cfprNfsMountDefFsmTaskInstanceId,
       "cfprNfsMountDefFsmTaskDn": cfprNfsMountDefFsmTaskDn,
       "cfprNfsMountDefFsmTaskRn": cfprNfsMountDefFsmTaskRn,
       "cfprNfsMountDefFsmTaskCompletion": cfprNfsMountDefFsmTaskCompletion,
       "cfprNfsMountDefFsmTaskFlags": cfprNfsMountDefFsmTaskFlags,
       "cfprNfsMountDefFsmTaskItem": cfprNfsMountDefFsmTaskItem,
       "cfprNfsMountDefFsmTaskSeqId": cfprNfsMountDefFsmTaskSeqId,
       "cfprNfsMountInstTable": cfprNfsMountInstTable,
       "cfprNfsMountInstEntry": cfprNfsMountInstEntry,
       "cfprNfsMountInstInstanceId": cfprNfsMountInstInstanceId,
       "cfprNfsMountInstDn": cfprNfsMountInstDn,
       "cfprNfsMountInstRn": cfprNfsMountInstRn,
       "cfprNfsMountInstAdminState": cfprNfsMountInstAdminState,
       "cfprNfsMountInstClientConfigState": cfprNfsMountInstClientConfigState,
       "cfprNfsMountInstDefDn": cfprNfsMountInstDefDn,
       "cfprNfsMountInstFsmDescr": cfprNfsMountInstFsmDescr,
       "cfprNfsMountInstFsmPrev": cfprNfsMountInstFsmPrev,
       "cfprNfsMountInstFsmProgr": cfprNfsMountInstFsmProgr,
       "cfprNfsMountInstFsmRmtInvErrCode": cfprNfsMountInstFsmRmtInvErrCode,
       "cfprNfsMountInstFsmRmtInvErrDescr": cfprNfsMountInstFsmRmtInvErrDescr,
       "cfprNfsMountInstFsmRmtInvRslt": cfprNfsMountInstFsmRmtInvRslt,
       "cfprNfsMountInstFsmStageDescr": cfprNfsMountInstFsmStageDescr,
       "cfprNfsMountInstFsmStamp": cfprNfsMountInstFsmStamp,
       "cfprNfsMountInstFsmStatus": cfprNfsMountInstFsmStatus,
       "cfprNfsMountInstFsmTry": cfprNfsMountInstFsmTry,
       "cfprNfsMountInstLocalDir": cfprNfsMountInstLocalDir,
       "cfprNfsMountInstName": cfprNfsMountInstName,
       "cfprNfsMountInstOperState": cfprNfsMountInstOperState,
       "cfprNfsMountInstPurpose": cfprNfsMountInstPurpose,
       "cfprNfsMountInstRemoteDir": cfprNfsMountInstRemoteDir,
       "cfprNfsMountInstServer": cfprNfsMountInstServer,
       "cfprNfsMountInstFsmTable": cfprNfsMountInstFsmTable,
       "cfprNfsMountInstFsmEntry": cfprNfsMountInstFsmEntry,
       "cfprNfsMountInstFsmInstanceId": cfprNfsMountInstFsmInstanceId,
       "cfprNfsMountInstFsmDn": cfprNfsMountInstFsmDn,
       "cfprNfsMountInstFsmRn": cfprNfsMountInstFsmRn,
       "cfprNfsMountInstFsmCompletionTime": cfprNfsMountInstFsmCompletionTime,
       "cfprNfsMountInstFsmCurrentFsm": cfprNfsMountInstFsmCurrentFsm,
       "cfprNfsMountInstFsmDescrData": cfprNfsMountInstFsmDescrData,
       "cfprNfsMountInstFsmFsmStatus": cfprNfsMountInstFsmFsmStatus,
       "cfprNfsMountInstFsmProgress": cfprNfsMountInstFsmProgress,
       "cfprNfsMountInstFsmRmtErrCode": cfprNfsMountInstFsmRmtErrCode,
       "cfprNfsMountInstFsmRmtErrDescr": cfprNfsMountInstFsmRmtErrDescr,
       "cfprNfsMountInstFsmRmtRslt": cfprNfsMountInstFsmRmtRslt,
       "cfprNfsMountInstFsmStageTable": cfprNfsMountInstFsmStageTable,
       "cfprNfsMountInstFsmStageEntry": cfprNfsMountInstFsmStageEntry,
       "cfprNfsMountInstFsmStageInstanceId": cfprNfsMountInstFsmStageInstanceId,
       "cfprNfsMountInstFsmStageDn": cfprNfsMountInstFsmStageDn,
       "cfprNfsMountInstFsmStageRn": cfprNfsMountInstFsmStageRn,
       "cfprNfsMountInstFsmStageDescrData": cfprNfsMountInstFsmStageDescrData,
       "cfprNfsMountInstFsmStageLastUpdateTime": cfprNfsMountInstFsmStageLastUpdateTime,
       "cfprNfsMountInstFsmStageName": cfprNfsMountInstFsmStageName,
       "cfprNfsMountInstFsmStageOrder": cfprNfsMountInstFsmStageOrder,
       "cfprNfsMountInstFsmStageRetry": cfprNfsMountInstFsmStageRetry,
       "cfprNfsMountInstFsmStageStageStatus": cfprNfsMountInstFsmStageStageStatus,
       "cfprNfsMountInstFsmTaskTable": cfprNfsMountInstFsmTaskTable,
       "cfprNfsMountInstFsmTaskEntry": cfprNfsMountInstFsmTaskEntry,
       "cfprNfsMountInstFsmTaskInstanceId": cfprNfsMountInstFsmTaskInstanceId,
       "cfprNfsMountInstFsmTaskDn": cfprNfsMountInstFsmTaskDn,
       "cfprNfsMountInstFsmTaskRn": cfprNfsMountInstFsmTaskRn,
       "cfprNfsMountInstFsmTaskCompletion": cfprNfsMountInstFsmTaskCompletion,
       "cfprNfsMountInstFsmTaskFlags": cfprNfsMountInstFsmTaskFlags,
       "cfprNfsMountInstFsmTaskItem": cfprNfsMountInstFsmTaskItem,
       "cfprNfsMountInstFsmTaskSeqId": cfprNfsMountInstFsmTaskSeqId}
)
