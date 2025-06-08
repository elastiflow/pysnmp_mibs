# SNMP MIB module (CISCO-FIREPOWER-AP-NFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-NFS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:14 2025
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
 CfprApNfsClientConfigState,
 CfprApNfsDefAdminState,
 CfprApNfsMntAdminState,
 CfprApNfsMntOperState,
 CfprApNfsMountDefFsmCurrentFsm,
 CfprApNfsMountDefFsmStageName,
 CfprApNfsMountDefFsmTaskItem,
 CfprApNfsMountInstFsmCurrentFsm,
 CfprApNfsMountInstFsmStageName,
 CfprApNfsMountInstFsmTaskItem,
 CfprApNfsPurpose,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApNfsClientConfigState",
    "CfprApNfsDefAdminState",
    "CfprApNfsMntAdminState",
    "CfprApNfsMntOperState",
    "CfprApNfsMountDefFsmCurrentFsm",
    "CfprApNfsMountDefFsmStageName",
    "CfprApNfsMountDefFsmTaskItem",
    "CfprApNfsMountInstFsmCurrentFsm",
    "CfprApNfsMountInstFsmStageName",
    "CfprApNfsMountInstFsmTaskItem",
    "CfprApNfsPurpose",
    "CfprApPolicyPolicyOwner")

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

cfprApNfsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApNfsEpTable_Object = MibTable
cfprApNfsEpTable = _CfprApNfsEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 1)
)
if mibBuilder.loadTexts:
    cfprApNfsEpTable.setStatus("current")
_CfprApNfsEpEntry_Object = MibTableRow
cfprApNfsEpEntry = _CfprApNfsEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 1, 1)
)
cfprApNfsEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsEpEntry.setStatus("current")
_CfprApNfsEpInstanceId_Type = CfprApManagedObjectId
_CfprApNfsEpInstanceId_Object = MibTableColumn
cfprApNfsEpInstanceId = _CfprApNfsEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 1, 1, 1),
    _CfprApNfsEpInstanceId_Type()
)
cfprApNfsEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsEpInstanceId.setStatus("current")
_CfprApNfsEpDn_Type = CfprApManagedObjectDn
_CfprApNfsEpDn_Object = MibTableColumn
cfprApNfsEpDn = _CfprApNfsEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 1, 1, 2),
    _CfprApNfsEpDn_Type()
)
cfprApNfsEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsEpDn.setStatus("current")
_CfprApNfsEpRn_Type = SnmpAdminString
_CfprApNfsEpRn_Object = MibTableColumn
cfprApNfsEpRn = _CfprApNfsEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 1, 1, 3),
    _CfprApNfsEpRn_Type()
)
cfprApNfsEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsEpRn.setStatus("current")
_CfprApNfsMountDefTable_Object = MibTable
cfprApNfsMountDefTable = _CfprApNfsMountDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2)
)
if mibBuilder.loadTexts:
    cfprApNfsMountDefTable.setStatus("current")
_CfprApNfsMountDefEntry_Object = MibTableRow
cfprApNfsMountDefEntry = _CfprApNfsMountDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1)
)
cfprApNfsMountDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsMountDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsMountDefEntry.setStatus("current")
_CfprApNfsMountDefInstanceId_Type = CfprApManagedObjectId
_CfprApNfsMountDefInstanceId_Object = MibTableColumn
cfprApNfsMountDefInstanceId = _CfprApNfsMountDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 1),
    _CfprApNfsMountDefInstanceId_Type()
)
cfprApNfsMountDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsMountDefInstanceId.setStatus("current")
_CfprApNfsMountDefDn_Type = CfprApManagedObjectDn
_CfprApNfsMountDefDn_Object = MibTableColumn
cfprApNfsMountDefDn = _CfprApNfsMountDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 2),
    _CfprApNfsMountDefDn_Type()
)
cfprApNfsMountDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefDn.setStatus("current")
_CfprApNfsMountDefRn_Type = SnmpAdminString
_CfprApNfsMountDefRn_Object = MibTableColumn
cfprApNfsMountDefRn = _CfprApNfsMountDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 3),
    _CfprApNfsMountDefRn_Type()
)
cfprApNfsMountDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefRn.setStatus("current")
_CfprApNfsMountDefAdminState_Type = CfprApNfsDefAdminState
_CfprApNfsMountDefAdminState_Object = MibTableColumn
cfprApNfsMountDefAdminState = _CfprApNfsMountDefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 4),
    _CfprApNfsMountDefAdminState_Type()
)
cfprApNfsMountDefAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefAdminState.setStatus("current")
_CfprApNfsMountDefDescr_Type = SnmpAdminString
_CfprApNfsMountDefDescr_Object = MibTableColumn
cfprApNfsMountDefDescr = _CfprApNfsMountDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 5),
    _CfprApNfsMountDefDescr_Type()
)
cfprApNfsMountDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefDescr.setStatus("current")
_CfprApNfsMountDefFltAggr_Type = Unsigned64
_CfprApNfsMountDefFltAggr_Object = MibTableColumn
cfprApNfsMountDefFltAggr = _CfprApNfsMountDefFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 6),
    _CfprApNfsMountDefFltAggr_Type()
)
cfprApNfsMountDefFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFltAggr.setStatus("current")
_CfprApNfsMountDefFsmDescr_Type = SnmpAdminString
_CfprApNfsMountDefFsmDescr_Object = MibTableColumn
cfprApNfsMountDefFsmDescr = _CfprApNfsMountDefFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 7),
    _CfprApNfsMountDefFsmDescr_Type()
)
cfprApNfsMountDefFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmDescr.setStatus("current")
_CfprApNfsMountDefFsmPrev_Type = SnmpAdminString
_CfprApNfsMountDefFsmPrev_Object = MibTableColumn
cfprApNfsMountDefFsmPrev = _CfprApNfsMountDefFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 8),
    _CfprApNfsMountDefFsmPrev_Type()
)
cfprApNfsMountDefFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmPrev.setStatus("current")
_CfprApNfsMountDefFsmProgr_Type = Gauge32
_CfprApNfsMountDefFsmProgr_Object = MibTableColumn
cfprApNfsMountDefFsmProgr = _CfprApNfsMountDefFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 9),
    _CfprApNfsMountDefFsmProgr_Type()
)
cfprApNfsMountDefFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmProgr.setStatus("current")
_CfprApNfsMountDefFsmRmtInvErrCode_Type = Gauge32
_CfprApNfsMountDefFsmRmtInvErrCode_Object = MibTableColumn
cfprApNfsMountDefFsmRmtInvErrCode = _CfprApNfsMountDefFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 10),
    _CfprApNfsMountDefFsmRmtInvErrCode_Type()
)
cfprApNfsMountDefFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmRmtInvErrCode.setStatus("current")
_CfprApNfsMountDefFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApNfsMountDefFsmRmtInvErrDescr_Object = MibTableColumn
cfprApNfsMountDefFsmRmtInvErrDescr = _CfprApNfsMountDefFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 11),
    _CfprApNfsMountDefFsmRmtInvErrDescr_Type()
)
cfprApNfsMountDefFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmRmtInvErrDescr.setStatus("current")
_CfprApNfsMountDefFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApNfsMountDefFsmRmtInvRslt_Object = MibTableColumn
cfprApNfsMountDefFsmRmtInvRslt = _CfprApNfsMountDefFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 12),
    _CfprApNfsMountDefFsmRmtInvRslt_Type()
)
cfprApNfsMountDefFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmRmtInvRslt.setStatus("current")
_CfprApNfsMountDefFsmStageDescr_Type = SnmpAdminString
_CfprApNfsMountDefFsmStageDescr_Object = MibTableColumn
cfprApNfsMountDefFsmStageDescr = _CfprApNfsMountDefFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 13),
    _CfprApNfsMountDefFsmStageDescr_Type()
)
cfprApNfsMountDefFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageDescr.setStatus("current")
_CfprApNfsMountDefFsmStamp_Type = DateAndTime
_CfprApNfsMountDefFsmStamp_Object = MibTableColumn
cfprApNfsMountDefFsmStamp = _CfprApNfsMountDefFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 14),
    _CfprApNfsMountDefFsmStamp_Type()
)
cfprApNfsMountDefFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStamp.setStatus("current")
_CfprApNfsMountDefFsmStatus_Type = SnmpAdminString
_CfprApNfsMountDefFsmStatus_Object = MibTableColumn
cfprApNfsMountDefFsmStatus = _CfprApNfsMountDefFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 15),
    _CfprApNfsMountDefFsmStatus_Type()
)
cfprApNfsMountDefFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStatus.setStatus("current")
_CfprApNfsMountDefFsmTry_Type = Gauge32
_CfprApNfsMountDefFsmTry_Object = MibTableColumn
cfprApNfsMountDefFsmTry = _CfprApNfsMountDefFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 16),
    _CfprApNfsMountDefFsmTry_Type()
)
cfprApNfsMountDefFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTry.setStatus("current")
_CfprApNfsMountDefIntId_Type = SnmpAdminString
_CfprApNfsMountDefIntId_Object = MibTableColumn
cfprApNfsMountDefIntId = _CfprApNfsMountDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 17),
    _CfprApNfsMountDefIntId_Type()
)
cfprApNfsMountDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefIntId.setStatus("current")
_CfprApNfsMountDefLocalDir_Type = SnmpAdminString
_CfprApNfsMountDefLocalDir_Object = MibTableColumn
cfprApNfsMountDefLocalDir = _CfprApNfsMountDefLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 18),
    _CfprApNfsMountDefLocalDir_Type()
)
cfprApNfsMountDefLocalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefLocalDir.setStatus("current")
_CfprApNfsMountDefName_Type = SnmpAdminString
_CfprApNfsMountDefName_Object = MibTableColumn
cfprApNfsMountDefName = _CfprApNfsMountDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 19),
    _CfprApNfsMountDefName_Type()
)
cfprApNfsMountDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefName.setStatus("current")
_CfprApNfsMountDefPolicyLevel_Type = Gauge32
_CfprApNfsMountDefPolicyLevel_Object = MibTableColumn
cfprApNfsMountDefPolicyLevel = _CfprApNfsMountDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 20),
    _CfprApNfsMountDefPolicyLevel_Type()
)
cfprApNfsMountDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefPolicyLevel.setStatus("current")
_CfprApNfsMountDefPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApNfsMountDefPolicyOwner_Object = MibTableColumn
cfprApNfsMountDefPolicyOwner = _CfprApNfsMountDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 21),
    _CfprApNfsMountDefPolicyOwner_Type()
)
cfprApNfsMountDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefPolicyOwner.setStatus("current")
_CfprApNfsMountDefPurpose_Type = CfprApNfsPurpose
_CfprApNfsMountDefPurpose_Object = MibTableColumn
cfprApNfsMountDefPurpose = _CfprApNfsMountDefPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 22),
    _CfprApNfsMountDefPurpose_Type()
)
cfprApNfsMountDefPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefPurpose.setStatus("current")
_CfprApNfsMountDefRemoteDir_Type = SnmpAdminString
_CfprApNfsMountDefRemoteDir_Object = MibTableColumn
cfprApNfsMountDefRemoteDir = _CfprApNfsMountDefRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 23),
    _CfprApNfsMountDefRemoteDir_Type()
)
cfprApNfsMountDefRemoteDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefRemoteDir.setStatus("current")
_CfprApNfsMountDefServer_Type = SnmpAdminString
_CfprApNfsMountDefServer_Object = MibTableColumn
cfprApNfsMountDefServer = _CfprApNfsMountDefServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 2, 1, 24),
    _CfprApNfsMountDefServer_Type()
)
cfprApNfsMountDefServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefServer.setStatus("current")
_CfprApNfsMountDefFsmTable_Object = MibTable
cfprApNfsMountDefFsmTable = _CfprApNfsMountDefFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3)
)
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTable.setStatus("current")
_CfprApNfsMountDefFsmEntry_Object = MibTableRow
cfprApNfsMountDefFsmEntry = _CfprApNfsMountDefFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1)
)
cfprApNfsMountDefFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsMountDefFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmEntry.setStatus("current")
_CfprApNfsMountDefFsmInstanceId_Type = CfprApManagedObjectId
_CfprApNfsMountDefFsmInstanceId_Object = MibTableColumn
cfprApNfsMountDefFsmInstanceId = _CfprApNfsMountDefFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 1),
    _CfprApNfsMountDefFsmInstanceId_Type()
)
cfprApNfsMountDefFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmInstanceId.setStatus("current")
_CfprApNfsMountDefFsmDn_Type = CfprApManagedObjectDn
_CfprApNfsMountDefFsmDn_Object = MibTableColumn
cfprApNfsMountDefFsmDn = _CfprApNfsMountDefFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 2),
    _CfprApNfsMountDefFsmDn_Type()
)
cfprApNfsMountDefFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmDn.setStatus("current")
_CfprApNfsMountDefFsmRn_Type = SnmpAdminString
_CfprApNfsMountDefFsmRn_Object = MibTableColumn
cfprApNfsMountDefFsmRn = _CfprApNfsMountDefFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 3),
    _CfprApNfsMountDefFsmRn_Type()
)
cfprApNfsMountDefFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmRn.setStatus("current")
_CfprApNfsMountDefFsmCompletionTime_Type = DateAndTime
_CfprApNfsMountDefFsmCompletionTime_Object = MibTableColumn
cfprApNfsMountDefFsmCompletionTime = _CfprApNfsMountDefFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 4),
    _CfprApNfsMountDefFsmCompletionTime_Type()
)
cfprApNfsMountDefFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmCompletionTime.setStatus("current")
_CfprApNfsMountDefFsmCurrentFsm_Type = CfprApNfsMountDefFsmCurrentFsm
_CfprApNfsMountDefFsmCurrentFsm_Object = MibTableColumn
cfprApNfsMountDefFsmCurrentFsm = _CfprApNfsMountDefFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 5),
    _CfprApNfsMountDefFsmCurrentFsm_Type()
)
cfprApNfsMountDefFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmCurrentFsm.setStatus("current")
_CfprApNfsMountDefFsmDescrData_Type = SnmpAdminString
_CfprApNfsMountDefFsmDescrData_Object = MibTableColumn
cfprApNfsMountDefFsmDescrData = _CfprApNfsMountDefFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 6),
    _CfprApNfsMountDefFsmDescrData_Type()
)
cfprApNfsMountDefFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmDescrData.setStatus("current")
_CfprApNfsMountDefFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApNfsMountDefFsmFsmStatus_Object = MibTableColumn
cfprApNfsMountDefFsmFsmStatus = _CfprApNfsMountDefFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 7),
    _CfprApNfsMountDefFsmFsmStatus_Type()
)
cfprApNfsMountDefFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmFsmStatus.setStatus("current")
_CfprApNfsMountDefFsmProgress_Type = Gauge32
_CfprApNfsMountDefFsmProgress_Object = MibTableColumn
cfprApNfsMountDefFsmProgress = _CfprApNfsMountDefFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 8),
    _CfprApNfsMountDefFsmProgress_Type()
)
cfprApNfsMountDefFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmProgress.setStatus("current")
_CfprApNfsMountDefFsmRmtErrCode_Type = Gauge32
_CfprApNfsMountDefFsmRmtErrCode_Object = MibTableColumn
cfprApNfsMountDefFsmRmtErrCode = _CfprApNfsMountDefFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 9),
    _CfprApNfsMountDefFsmRmtErrCode_Type()
)
cfprApNfsMountDefFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmRmtErrCode.setStatus("current")
_CfprApNfsMountDefFsmRmtErrDescr_Type = SnmpAdminString
_CfprApNfsMountDefFsmRmtErrDescr_Object = MibTableColumn
cfprApNfsMountDefFsmRmtErrDescr = _CfprApNfsMountDefFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 10),
    _CfprApNfsMountDefFsmRmtErrDescr_Type()
)
cfprApNfsMountDefFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmRmtErrDescr.setStatus("current")
_CfprApNfsMountDefFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApNfsMountDefFsmRmtRslt_Object = MibTableColumn
cfprApNfsMountDefFsmRmtRslt = _CfprApNfsMountDefFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 3, 1, 11),
    _CfprApNfsMountDefFsmRmtRslt_Type()
)
cfprApNfsMountDefFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmRmtRslt.setStatus("current")
_CfprApNfsMountDefFsmStageTable_Object = MibTable
cfprApNfsMountDefFsmStageTable = _CfprApNfsMountDefFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4)
)
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageTable.setStatus("current")
_CfprApNfsMountDefFsmStageEntry_Object = MibTableRow
cfprApNfsMountDefFsmStageEntry = _CfprApNfsMountDefFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1)
)
cfprApNfsMountDefFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsMountDefFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageEntry.setStatus("current")
_CfprApNfsMountDefFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApNfsMountDefFsmStageInstanceId_Object = MibTableColumn
cfprApNfsMountDefFsmStageInstanceId = _CfprApNfsMountDefFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 1),
    _CfprApNfsMountDefFsmStageInstanceId_Type()
)
cfprApNfsMountDefFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageInstanceId.setStatus("current")
_CfprApNfsMountDefFsmStageDn_Type = CfprApManagedObjectDn
_CfprApNfsMountDefFsmStageDn_Object = MibTableColumn
cfprApNfsMountDefFsmStageDn = _CfprApNfsMountDefFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 2),
    _CfprApNfsMountDefFsmStageDn_Type()
)
cfprApNfsMountDefFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageDn.setStatus("current")
_CfprApNfsMountDefFsmStageRn_Type = SnmpAdminString
_CfprApNfsMountDefFsmStageRn_Object = MibTableColumn
cfprApNfsMountDefFsmStageRn = _CfprApNfsMountDefFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 3),
    _CfprApNfsMountDefFsmStageRn_Type()
)
cfprApNfsMountDefFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageRn.setStatus("current")
_CfprApNfsMountDefFsmStageDescrData_Type = SnmpAdminString
_CfprApNfsMountDefFsmStageDescrData_Object = MibTableColumn
cfprApNfsMountDefFsmStageDescrData = _CfprApNfsMountDefFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 4),
    _CfprApNfsMountDefFsmStageDescrData_Type()
)
cfprApNfsMountDefFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageDescrData.setStatus("current")
_CfprApNfsMountDefFsmStageLastUpdateTime_Type = DateAndTime
_CfprApNfsMountDefFsmStageLastUpdateTime_Object = MibTableColumn
cfprApNfsMountDefFsmStageLastUpdateTime = _CfprApNfsMountDefFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 5),
    _CfprApNfsMountDefFsmStageLastUpdateTime_Type()
)
cfprApNfsMountDefFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageLastUpdateTime.setStatus("current")
_CfprApNfsMountDefFsmStageName_Type = CfprApNfsMountDefFsmStageName
_CfprApNfsMountDefFsmStageName_Object = MibTableColumn
cfprApNfsMountDefFsmStageName = _CfprApNfsMountDefFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 6),
    _CfprApNfsMountDefFsmStageName_Type()
)
cfprApNfsMountDefFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageName.setStatus("current")
_CfprApNfsMountDefFsmStageOrder_Type = Gauge32
_CfprApNfsMountDefFsmStageOrder_Object = MibTableColumn
cfprApNfsMountDefFsmStageOrder = _CfprApNfsMountDefFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 7),
    _CfprApNfsMountDefFsmStageOrder_Type()
)
cfprApNfsMountDefFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageOrder.setStatus("current")
_CfprApNfsMountDefFsmStageRetry_Type = Gauge32
_CfprApNfsMountDefFsmStageRetry_Object = MibTableColumn
cfprApNfsMountDefFsmStageRetry = _CfprApNfsMountDefFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 8),
    _CfprApNfsMountDefFsmStageRetry_Type()
)
cfprApNfsMountDefFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageRetry.setStatus("current")
_CfprApNfsMountDefFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApNfsMountDefFsmStageStageStatus_Object = MibTableColumn
cfprApNfsMountDefFsmStageStageStatus = _CfprApNfsMountDefFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 4, 1, 9),
    _CfprApNfsMountDefFsmStageStageStatus_Type()
)
cfprApNfsMountDefFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmStageStageStatus.setStatus("current")
_CfprApNfsMountDefFsmTaskTable_Object = MibTable
cfprApNfsMountDefFsmTaskTable = _CfprApNfsMountDefFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5)
)
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskTable.setStatus("current")
_CfprApNfsMountDefFsmTaskEntry_Object = MibTableRow
cfprApNfsMountDefFsmTaskEntry = _CfprApNfsMountDefFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5, 1)
)
cfprApNfsMountDefFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsMountDefFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskEntry.setStatus("current")
_CfprApNfsMountDefFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApNfsMountDefFsmTaskInstanceId_Object = MibTableColumn
cfprApNfsMountDefFsmTaskInstanceId = _CfprApNfsMountDefFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5, 1, 1),
    _CfprApNfsMountDefFsmTaskInstanceId_Type()
)
cfprApNfsMountDefFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskInstanceId.setStatus("current")
_CfprApNfsMountDefFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApNfsMountDefFsmTaskDn_Object = MibTableColumn
cfprApNfsMountDefFsmTaskDn = _CfprApNfsMountDefFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5, 1, 2),
    _CfprApNfsMountDefFsmTaskDn_Type()
)
cfprApNfsMountDefFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskDn.setStatus("current")
_CfprApNfsMountDefFsmTaskRn_Type = SnmpAdminString
_CfprApNfsMountDefFsmTaskRn_Object = MibTableColumn
cfprApNfsMountDefFsmTaskRn = _CfprApNfsMountDefFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5, 1, 3),
    _CfprApNfsMountDefFsmTaskRn_Type()
)
cfprApNfsMountDefFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskRn.setStatus("current")
_CfprApNfsMountDefFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApNfsMountDefFsmTaskCompletion_Object = MibTableColumn
cfprApNfsMountDefFsmTaskCompletion = _CfprApNfsMountDefFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5, 1, 4),
    _CfprApNfsMountDefFsmTaskCompletion_Type()
)
cfprApNfsMountDefFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskCompletion.setStatus("current")
_CfprApNfsMountDefFsmTaskFlags_Type = CfprApFsmFlags
_CfprApNfsMountDefFsmTaskFlags_Object = MibTableColumn
cfprApNfsMountDefFsmTaskFlags = _CfprApNfsMountDefFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5, 1, 5),
    _CfprApNfsMountDefFsmTaskFlags_Type()
)
cfprApNfsMountDefFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskFlags.setStatus("current")
_CfprApNfsMountDefFsmTaskItem_Type = CfprApNfsMountDefFsmTaskItem
_CfprApNfsMountDefFsmTaskItem_Object = MibTableColumn
cfprApNfsMountDefFsmTaskItem = _CfprApNfsMountDefFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5, 1, 6),
    _CfprApNfsMountDefFsmTaskItem_Type()
)
cfprApNfsMountDefFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskItem.setStatus("current")
_CfprApNfsMountDefFsmTaskSeqId_Type = Gauge32
_CfprApNfsMountDefFsmTaskSeqId_Object = MibTableColumn
cfprApNfsMountDefFsmTaskSeqId = _CfprApNfsMountDefFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 5, 1, 7),
    _CfprApNfsMountDefFsmTaskSeqId_Type()
)
cfprApNfsMountDefFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountDefFsmTaskSeqId.setStatus("current")
_CfprApNfsMountInstTable_Object = MibTable
cfprApNfsMountInstTable = _CfprApNfsMountInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6)
)
if mibBuilder.loadTexts:
    cfprApNfsMountInstTable.setStatus("current")
_CfprApNfsMountInstEntry_Object = MibTableRow
cfprApNfsMountInstEntry = _CfprApNfsMountInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1)
)
cfprApNfsMountInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsMountInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsMountInstEntry.setStatus("current")
_CfprApNfsMountInstInstanceId_Type = CfprApManagedObjectId
_CfprApNfsMountInstInstanceId_Object = MibTableColumn
cfprApNfsMountInstInstanceId = _CfprApNfsMountInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 1),
    _CfprApNfsMountInstInstanceId_Type()
)
cfprApNfsMountInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsMountInstInstanceId.setStatus("current")
_CfprApNfsMountInstDn_Type = CfprApManagedObjectDn
_CfprApNfsMountInstDn_Object = MibTableColumn
cfprApNfsMountInstDn = _CfprApNfsMountInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 2),
    _CfprApNfsMountInstDn_Type()
)
cfprApNfsMountInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstDn.setStatus("current")
_CfprApNfsMountInstRn_Type = SnmpAdminString
_CfprApNfsMountInstRn_Object = MibTableColumn
cfprApNfsMountInstRn = _CfprApNfsMountInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 3),
    _CfprApNfsMountInstRn_Type()
)
cfprApNfsMountInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstRn.setStatus("current")
_CfprApNfsMountInstAdminState_Type = CfprApNfsMntAdminState
_CfprApNfsMountInstAdminState_Object = MibTableColumn
cfprApNfsMountInstAdminState = _CfprApNfsMountInstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 4),
    _CfprApNfsMountInstAdminState_Type()
)
cfprApNfsMountInstAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstAdminState.setStatus("current")
_CfprApNfsMountInstClientConfigState_Type = CfprApNfsClientConfigState
_CfprApNfsMountInstClientConfigState_Object = MibTableColumn
cfprApNfsMountInstClientConfigState = _CfprApNfsMountInstClientConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 5),
    _CfprApNfsMountInstClientConfigState_Type()
)
cfprApNfsMountInstClientConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstClientConfigState.setStatus("current")
_CfprApNfsMountInstDefDn_Type = SnmpAdminString
_CfprApNfsMountInstDefDn_Object = MibTableColumn
cfprApNfsMountInstDefDn = _CfprApNfsMountInstDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 6),
    _CfprApNfsMountInstDefDn_Type()
)
cfprApNfsMountInstDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstDefDn.setStatus("current")
_CfprApNfsMountInstFsmDescr_Type = SnmpAdminString
_CfprApNfsMountInstFsmDescr_Object = MibTableColumn
cfprApNfsMountInstFsmDescr = _CfprApNfsMountInstFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 7),
    _CfprApNfsMountInstFsmDescr_Type()
)
cfprApNfsMountInstFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmDescr.setStatus("current")
_CfprApNfsMountInstFsmPrev_Type = SnmpAdminString
_CfprApNfsMountInstFsmPrev_Object = MibTableColumn
cfprApNfsMountInstFsmPrev = _CfprApNfsMountInstFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 8),
    _CfprApNfsMountInstFsmPrev_Type()
)
cfprApNfsMountInstFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmPrev.setStatus("current")
_CfprApNfsMountInstFsmProgr_Type = Gauge32
_CfprApNfsMountInstFsmProgr_Object = MibTableColumn
cfprApNfsMountInstFsmProgr = _CfprApNfsMountInstFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 9),
    _CfprApNfsMountInstFsmProgr_Type()
)
cfprApNfsMountInstFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmProgr.setStatus("current")
_CfprApNfsMountInstFsmRmtInvErrCode_Type = Gauge32
_CfprApNfsMountInstFsmRmtInvErrCode_Object = MibTableColumn
cfprApNfsMountInstFsmRmtInvErrCode = _CfprApNfsMountInstFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 10),
    _CfprApNfsMountInstFsmRmtInvErrCode_Type()
)
cfprApNfsMountInstFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmRmtInvErrCode.setStatus("current")
_CfprApNfsMountInstFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApNfsMountInstFsmRmtInvErrDescr_Object = MibTableColumn
cfprApNfsMountInstFsmRmtInvErrDescr = _CfprApNfsMountInstFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 11),
    _CfprApNfsMountInstFsmRmtInvErrDescr_Type()
)
cfprApNfsMountInstFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmRmtInvErrDescr.setStatus("current")
_CfprApNfsMountInstFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApNfsMountInstFsmRmtInvRslt_Object = MibTableColumn
cfprApNfsMountInstFsmRmtInvRslt = _CfprApNfsMountInstFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 12),
    _CfprApNfsMountInstFsmRmtInvRslt_Type()
)
cfprApNfsMountInstFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmRmtInvRslt.setStatus("current")
_CfprApNfsMountInstFsmStageDescr_Type = SnmpAdminString
_CfprApNfsMountInstFsmStageDescr_Object = MibTableColumn
cfprApNfsMountInstFsmStageDescr = _CfprApNfsMountInstFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 13),
    _CfprApNfsMountInstFsmStageDescr_Type()
)
cfprApNfsMountInstFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageDescr.setStatus("current")
_CfprApNfsMountInstFsmStamp_Type = DateAndTime
_CfprApNfsMountInstFsmStamp_Object = MibTableColumn
cfprApNfsMountInstFsmStamp = _CfprApNfsMountInstFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 14),
    _CfprApNfsMountInstFsmStamp_Type()
)
cfprApNfsMountInstFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStamp.setStatus("current")
_CfprApNfsMountInstFsmStatus_Type = SnmpAdminString
_CfprApNfsMountInstFsmStatus_Object = MibTableColumn
cfprApNfsMountInstFsmStatus = _CfprApNfsMountInstFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 15),
    _CfprApNfsMountInstFsmStatus_Type()
)
cfprApNfsMountInstFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStatus.setStatus("current")
_CfprApNfsMountInstFsmTry_Type = Gauge32
_CfprApNfsMountInstFsmTry_Object = MibTableColumn
cfprApNfsMountInstFsmTry = _CfprApNfsMountInstFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 16),
    _CfprApNfsMountInstFsmTry_Type()
)
cfprApNfsMountInstFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTry.setStatus("current")
_CfprApNfsMountInstLocalDir_Type = SnmpAdminString
_CfprApNfsMountInstLocalDir_Object = MibTableColumn
cfprApNfsMountInstLocalDir = _CfprApNfsMountInstLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 17),
    _CfprApNfsMountInstLocalDir_Type()
)
cfprApNfsMountInstLocalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstLocalDir.setStatus("current")
_CfprApNfsMountInstName_Type = SnmpAdminString
_CfprApNfsMountInstName_Object = MibTableColumn
cfprApNfsMountInstName = _CfprApNfsMountInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 18),
    _CfprApNfsMountInstName_Type()
)
cfprApNfsMountInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstName.setStatus("current")
_CfprApNfsMountInstOperState_Type = CfprApNfsMntOperState
_CfprApNfsMountInstOperState_Object = MibTableColumn
cfprApNfsMountInstOperState = _CfprApNfsMountInstOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 19),
    _CfprApNfsMountInstOperState_Type()
)
cfprApNfsMountInstOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstOperState.setStatus("current")
_CfprApNfsMountInstPurpose_Type = CfprApNfsPurpose
_CfprApNfsMountInstPurpose_Object = MibTableColumn
cfprApNfsMountInstPurpose = _CfprApNfsMountInstPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 20),
    _CfprApNfsMountInstPurpose_Type()
)
cfprApNfsMountInstPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstPurpose.setStatus("current")
_CfprApNfsMountInstRemoteDir_Type = SnmpAdminString
_CfprApNfsMountInstRemoteDir_Object = MibTableColumn
cfprApNfsMountInstRemoteDir = _CfprApNfsMountInstRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 21),
    _CfprApNfsMountInstRemoteDir_Type()
)
cfprApNfsMountInstRemoteDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstRemoteDir.setStatus("current")
_CfprApNfsMountInstServer_Type = SnmpAdminString
_CfprApNfsMountInstServer_Object = MibTableColumn
cfprApNfsMountInstServer = _CfprApNfsMountInstServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 6, 1, 22),
    _CfprApNfsMountInstServer_Type()
)
cfprApNfsMountInstServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstServer.setStatus("current")
_CfprApNfsMountInstFsmTable_Object = MibTable
cfprApNfsMountInstFsmTable = _CfprApNfsMountInstFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7)
)
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTable.setStatus("current")
_CfprApNfsMountInstFsmEntry_Object = MibTableRow
cfprApNfsMountInstFsmEntry = _CfprApNfsMountInstFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1)
)
cfprApNfsMountInstFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsMountInstFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmEntry.setStatus("current")
_CfprApNfsMountInstFsmInstanceId_Type = CfprApManagedObjectId
_CfprApNfsMountInstFsmInstanceId_Object = MibTableColumn
cfprApNfsMountInstFsmInstanceId = _CfprApNfsMountInstFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 1),
    _CfprApNfsMountInstFsmInstanceId_Type()
)
cfprApNfsMountInstFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmInstanceId.setStatus("current")
_CfprApNfsMountInstFsmDn_Type = CfprApManagedObjectDn
_CfprApNfsMountInstFsmDn_Object = MibTableColumn
cfprApNfsMountInstFsmDn = _CfprApNfsMountInstFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 2),
    _CfprApNfsMountInstFsmDn_Type()
)
cfprApNfsMountInstFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmDn.setStatus("current")
_CfprApNfsMountInstFsmRn_Type = SnmpAdminString
_CfprApNfsMountInstFsmRn_Object = MibTableColumn
cfprApNfsMountInstFsmRn = _CfprApNfsMountInstFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 3),
    _CfprApNfsMountInstFsmRn_Type()
)
cfprApNfsMountInstFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmRn.setStatus("current")
_CfprApNfsMountInstFsmCompletionTime_Type = DateAndTime
_CfprApNfsMountInstFsmCompletionTime_Object = MibTableColumn
cfprApNfsMountInstFsmCompletionTime = _CfprApNfsMountInstFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 4),
    _CfprApNfsMountInstFsmCompletionTime_Type()
)
cfprApNfsMountInstFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmCompletionTime.setStatus("current")
_CfprApNfsMountInstFsmCurrentFsm_Type = CfprApNfsMountInstFsmCurrentFsm
_CfprApNfsMountInstFsmCurrentFsm_Object = MibTableColumn
cfprApNfsMountInstFsmCurrentFsm = _CfprApNfsMountInstFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 5),
    _CfprApNfsMountInstFsmCurrentFsm_Type()
)
cfprApNfsMountInstFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmCurrentFsm.setStatus("current")
_CfprApNfsMountInstFsmDescrData_Type = SnmpAdminString
_CfprApNfsMountInstFsmDescrData_Object = MibTableColumn
cfprApNfsMountInstFsmDescrData = _CfprApNfsMountInstFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 6),
    _CfprApNfsMountInstFsmDescrData_Type()
)
cfprApNfsMountInstFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmDescrData.setStatus("current")
_CfprApNfsMountInstFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApNfsMountInstFsmFsmStatus_Object = MibTableColumn
cfprApNfsMountInstFsmFsmStatus = _CfprApNfsMountInstFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 7),
    _CfprApNfsMountInstFsmFsmStatus_Type()
)
cfprApNfsMountInstFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmFsmStatus.setStatus("current")
_CfprApNfsMountInstFsmProgress_Type = Gauge32
_CfprApNfsMountInstFsmProgress_Object = MibTableColumn
cfprApNfsMountInstFsmProgress = _CfprApNfsMountInstFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 8),
    _CfprApNfsMountInstFsmProgress_Type()
)
cfprApNfsMountInstFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmProgress.setStatus("current")
_CfprApNfsMountInstFsmRmtErrCode_Type = Gauge32
_CfprApNfsMountInstFsmRmtErrCode_Object = MibTableColumn
cfprApNfsMountInstFsmRmtErrCode = _CfprApNfsMountInstFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 9),
    _CfprApNfsMountInstFsmRmtErrCode_Type()
)
cfprApNfsMountInstFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmRmtErrCode.setStatus("current")
_CfprApNfsMountInstFsmRmtErrDescr_Type = SnmpAdminString
_CfprApNfsMountInstFsmRmtErrDescr_Object = MibTableColumn
cfprApNfsMountInstFsmRmtErrDescr = _CfprApNfsMountInstFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 10),
    _CfprApNfsMountInstFsmRmtErrDescr_Type()
)
cfprApNfsMountInstFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmRmtErrDescr.setStatus("current")
_CfprApNfsMountInstFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApNfsMountInstFsmRmtRslt_Object = MibTableColumn
cfprApNfsMountInstFsmRmtRslt = _CfprApNfsMountInstFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 7, 1, 11),
    _CfprApNfsMountInstFsmRmtRslt_Type()
)
cfprApNfsMountInstFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmRmtRslt.setStatus("current")
_CfprApNfsMountInstFsmStageTable_Object = MibTable
cfprApNfsMountInstFsmStageTable = _CfprApNfsMountInstFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8)
)
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageTable.setStatus("current")
_CfprApNfsMountInstFsmStageEntry_Object = MibTableRow
cfprApNfsMountInstFsmStageEntry = _CfprApNfsMountInstFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1)
)
cfprApNfsMountInstFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsMountInstFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageEntry.setStatus("current")
_CfprApNfsMountInstFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApNfsMountInstFsmStageInstanceId_Object = MibTableColumn
cfprApNfsMountInstFsmStageInstanceId = _CfprApNfsMountInstFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 1),
    _CfprApNfsMountInstFsmStageInstanceId_Type()
)
cfprApNfsMountInstFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageInstanceId.setStatus("current")
_CfprApNfsMountInstFsmStageDn_Type = CfprApManagedObjectDn
_CfprApNfsMountInstFsmStageDn_Object = MibTableColumn
cfprApNfsMountInstFsmStageDn = _CfprApNfsMountInstFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 2),
    _CfprApNfsMountInstFsmStageDn_Type()
)
cfprApNfsMountInstFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageDn.setStatus("current")
_CfprApNfsMountInstFsmStageRn_Type = SnmpAdminString
_CfprApNfsMountInstFsmStageRn_Object = MibTableColumn
cfprApNfsMountInstFsmStageRn = _CfprApNfsMountInstFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 3),
    _CfprApNfsMountInstFsmStageRn_Type()
)
cfprApNfsMountInstFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageRn.setStatus("current")
_CfprApNfsMountInstFsmStageDescrData_Type = SnmpAdminString
_CfprApNfsMountInstFsmStageDescrData_Object = MibTableColumn
cfprApNfsMountInstFsmStageDescrData = _CfprApNfsMountInstFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 4),
    _CfprApNfsMountInstFsmStageDescrData_Type()
)
cfprApNfsMountInstFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageDescrData.setStatus("current")
_CfprApNfsMountInstFsmStageLastUpdateTime_Type = DateAndTime
_CfprApNfsMountInstFsmStageLastUpdateTime_Object = MibTableColumn
cfprApNfsMountInstFsmStageLastUpdateTime = _CfprApNfsMountInstFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 5),
    _CfprApNfsMountInstFsmStageLastUpdateTime_Type()
)
cfprApNfsMountInstFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageLastUpdateTime.setStatus("current")
_CfprApNfsMountInstFsmStageName_Type = CfprApNfsMountInstFsmStageName
_CfprApNfsMountInstFsmStageName_Object = MibTableColumn
cfprApNfsMountInstFsmStageName = _CfprApNfsMountInstFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 6),
    _CfprApNfsMountInstFsmStageName_Type()
)
cfprApNfsMountInstFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageName.setStatus("current")
_CfprApNfsMountInstFsmStageOrder_Type = Gauge32
_CfprApNfsMountInstFsmStageOrder_Object = MibTableColumn
cfprApNfsMountInstFsmStageOrder = _CfprApNfsMountInstFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 7),
    _CfprApNfsMountInstFsmStageOrder_Type()
)
cfprApNfsMountInstFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageOrder.setStatus("current")
_CfprApNfsMountInstFsmStageRetry_Type = Gauge32
_CfprApNfsMountInstFsmStageRetry_Object = MibTableColumn
cfprApNfsMountInstFsmStageRetry = _CfprApNfsMountInstFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 8),
    _CfprApNfsMountInstFsmStageRetry_Type()
)
cfprApNfsMountInstFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageRetry.setStatus("current")
_CfprApNfsMountInstFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApNfsMountInstFsmStageStageStatus_Object = MibTableColumn
cfprApNfsMountInstFsmStageStageStatus = _CfprApNfsMountInstFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 8, 1, 9),
    _CfprApNfsMountInstFsmStageStageStatus_Type()
)
cfprApNfsMountInstFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmStageStageStatus.setStatus("current")
_CfprApNfsMountInstFsmTaskTable_Object = MibTable
cfprApNfsMountInstFsmTaskTable = _CfprApNfsMountInstFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9)
)
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskTable.setStatus("current")
_CfprApNfsMountInstFsmTaskEntry_Object = MibTableRow
cfprApNfsMountInstFsmTaskEntry = _CfprApNfsMountInstFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9, 1)
)
cfprApNfsMountInstFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NFS-MIB", "cfprApNfsMountInstFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskEntry.setStatus("current")
_CfprApNfsMountInstFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApNfsMountInstFsmTaskInstanceId_Object = MibTableColumn
cfprApNfsMountInstFsmTaskInstanceId = _CfprApNfsMountInstFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9, 1, 1),
    _CfprApNfsMountInstFsmTaskInstanceId_Type()
)
cfprApNfsMountInstFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskInstanceId.setStatus("current")
_CfprApNfsMountInstFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApNfsMountInstFsmTaskDn_Object = MibTableColumn
cfprApNfsMountInstFsmTaskDn = _CfprApNfsMountInstFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9, 1, 2),
    _CfprApNfsMountInstFsmTaskDn_Type()
)
cfprApNfsMountInstFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskDn.setStatus("current")
_CfprApNfsMountInstFsmTaskRn_Type = SnmpAdminString
_CfprApNfsMountInstFsmTaskRn_Object = MibTableColumn
cfprApNfsMountInstFsmTaskRn = _CfprApNfsMountInstFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9, 1, 3),
    _CfprApNfsMountInstFsmTaskRn_Type()
)
cfprApNfsMountInstFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskRn.setStatus("current")
_CfprApNfsMountInstFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApNfsMountInstFsmTaskCompletion_Object = MibTableColumn
cfprApNfsMountInstFsmTaskCompletion = _CfprApNfsMountInstFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9, 1, 4),
    _CfprApNfsMountInstFsmTaskCompletion_Type()
)
cfprApNfsMountInstFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskCompletion.setStatus("current")
_CfprApNfsMountInstFsmTaskFlags_Type = CfprApFsmFlags
_CfprApNfsMountInstFsmTaskFlags_Object = MibTableColumn
cfprApNfsMountInstFsmTaskFlags = _CfprApNfsMountInstFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9, 1, 5),
    _CfprApNfsMountInstFsmTaskFlags_Type()
)
cfprApNfsMountInstFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskFlags.setStatus("current")
_CfprApNfsMountInstFsmTaskItem_Type = CfprApNfsMountInstFsmTaskItem
_CfprApNfsMountInstFsmTaskItem_Object = MibTableColumn
cfprApNfsMountInstFsmTaskItem = _CfprApNfsMountInstFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9, 1, 6),
    _CfprApNfsMountInstFsmTaskItem_Type()
)
cfprApNfsMountInstFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskItem.setStatus("current")
_CfprApNfsMountInstFsmTaskSeqId_Type = Gauge32
_CfprApNfsMountInstFsmTaskSeqId_Object = MibTableColumn
cfprApNfsMountInstFsmTaskSeqId = _CfprApNfsMountInstFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 53, 9, 1, 7),
    _CfprApNfsMountInstFsmTaskSeqId_Type()
)
cfprApNfsMountInstFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNfsMountInstFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-NFS-MIB",
    **{"cfprApNfsObjects": cfprApNfsObjects,
       "cfprApNfsEpTable": cfprApNfsEpTable,
       "cfprApNfsEpEntry": cfprApNfsEpEntry,
       "cfprApNfsEpInstanceId": cfprApNfsEpInstanceId,
       "cfprApNfsEpDn": cfprApNfsEpDn,
       "cfprApNfsEpRn": cfprApNfsEpRn,
       "cfprApNfsMountDefTable": cfprApNfsMountDefTable,
       "cfprApNfsMountDefEntry": cfprApNfsMountDefEntry,
       "cfprApNfsMountDefInstanceId": cfprApNfsMountDefInstanceId,
       "cfprApNfsMountDefDn": cfprApNfsMountDefDn,
       "cfprApNfsMountDefRn": cfprApNfsMountDefRn,
       "cfprApNfsMountDefAdminState": cfprApNfsMountDefAdminState,
       "cfprApNfsMountDefDescr": cfprApNfsMountDefDescr,
       "cfprApNfsMountDefFltAggr": cfprApNfsMountDefFltAggr,
       "cfprApNfsMountDefFsmDescr": cfprApNfsMountDefFsmDescr,
       "cfprApNfsMountDefFsmPrev": cfprApNfsMountDefFsmPrev,
       "cfprApNfsMountDefFsmProgr": cfprApNfsMountDefFsmProgr,
       "cfprApNfsMountDefFsmRmtInvErrCode": cfprApNfsMountDefFsmRmtInvErrCode,
       "cfprApNfsMountDefFsmRmtInvErrDescr": cfprApNfsMountDefFsmRmtInvErrDescr,
       "cfprApNfsMountDefFsmRmtInvRslt": cfprApNfsMountDefFsmRmtInvRslt,
       "cfprApNfsMountDefFsmStageDescr": cfprApNfsMountDefFsmStageDescr,
       "cfprApNfsMountDefFsmStamp": cfprApNfsMountDefFsmStamp,
       "cfprApNfsMountDefFsmStatus": cfprApNfsMountDefFsmStatus,
       "cfprApNfsMountDefFsmTry": cfprApNfsMountDefFsmTry,
       "cfprApNfsMountDefIntId": cfprApNfsMountDefIntId,
       "cfprApNfsMountDefLocalDir": cfprApNfsMountDefLocalDir,
       "cfprApNfsMountDefName": cfprApNfsMountDefName,
       "cfprApNfsMountDefPolicyLevel": cfprApNfsMountDefPolicyLevel,
       "cfprApNfsMountDefPolicyOwner": cfprApNfsMountDefPolicyOwner,
       "cfprApNfsMountDefPurpose": cfprApNfsMountDefPurpose,
       "cfprApNfsMountDefRemoteDir": cfprApNfsMountDefRemoteDir,
       "cfprApNfsMountDefServer": cfprApNfsMountDefServer,
       "cfprApNfsMountDefFsmTable": cfprApNfsMountDefFsmTable,
       "cfprApNfsMountDefFsmEntry": cfprApNfsMountDefFsmEntry,
       "cfprApNfsMountDefFsmInstanceId": cfprApNfsMountDefFsmInstanceId,
       "cfprApNfsMountDefFsmDn": cfprApNfsMountDefFsmDn,
       "cfprApNfsMountDefFsmRn": cfprApNfsMountDefFsmRn,
       "cfprApNfsMountDefFsmCompletionTime": cfprApNfsMountDefFsmCompletionTime,
       "cfprApNfsMountDefFsmCurrentFsm": cfprApNfsMountDefFsmCurrentFsm,
       "cfprApNfsMountDefFsmDescrData": cfprApNfsMountDefFsmDescrData,
       "cfprApNfsMountDefFsmFsmStatus": cfprApNfsMountDefFsmFsmStatus,
       "cfprApNfsMountDefFsmProgress": cfprApNfsMountDefFsmProgress,
       "cfprApNfsMountDefFsmRmtErrCode": cfprApNfsMountDefFsmRmtErrCode,
       "cfprApNfsMountDefFsmRmtErrDescr": cfprApNfsMountDefFsmRmtErrDescr,
       "cfprApNfsMountDefFsmRmtRslt": cfprApNfsMountDefFsmRmtRslt,
       "cfprApNfsMountDefFsmStageTable": cfprApNfsMountDefFsmStageTable,
       "cfprApNfsMountDefFsmStageEntry": cfprApNfsMountDefFsmStageEntry,
       "cfprApNfsMountDefFsmStageInstanceId": cfprApNfsMountDefFsmStageInstanceId,
       "cfprApNfsMountDefFsmStageDn": cfprApNfsMountDefFsmStageDn,
       "cfprApNfsMountDefFsmStageRn": cfprApNfsMountDefFsmStageRn,
       "cfprApNfsMountDefFsmStageDescrData": cfprApNfsMountDefFsmStageDescrData,
       "cfprApNfsMountDefFsmStageLastUpdateTime": cfprApNfsMountDefFsmStageLastUpdateTime,
       "cfprApNfsMountDefFsmStageName": cfprApNfsMountDefFsmStageName,
       "cfprApNfsMountDefFsmStageOrder": cfprApNfsMountDefFsmStageOrder,
       "cfprApNfsMountDefFsmStageRetry": cfprApNfsMountDefFsmStageRetry,
       "cfprApNfsMountDefFsmStageStageStatus": cfprApNfsMountDefFsmStageStageStatus,
       "cfprApNfsMountDefFsmTaskTable": cfprApNfsMountDefFsmTaskTable,
       "cfprApNfsMountDefFsmTaskEntry": cfprApNfsMountDefFsmTaskEntry,
       "cfprApNfsMountDefFsmTaskInstanceId": cfprApNfsMountDefFsmTaskInstanceId,
       "cfprApNfsMountDefFsmTaskDn": cfprApNfsMountDefFsmTaskDn,
       "cfprApNfsMountDefFsmTaskRn": cfprApNfsMountDefFsmTaskRn,
       "cfprApNfsMountDefFsmTaskCompletion": cfprApNfsMountDefFsmTaskCompletion,
       "cfprApNfsMountDefFsmTaskFlags": cfprApNfsMountDefFsmTaskFlags,
       "cfprApNfsMountDefFsmTaskItem": cfprApNfsMountDefFsmTaskItem,
       "cfprApNfsMountDefFsmTaskSeqId": cfprApNfsMountDefFsmTaskSeqId,
       "cfprApNfsMountInstTable": cfprApNfsMountInstTable,
       "cfprApNfsMountInstEntry": cfprApNfsMountInstEntry,
       "cfprApNfsMountInstInstanceId": cfprApNfsMountInstInstanceId,
       "cfprApNfsMountInstDn": cfprApNfsMountInstDn,
       "cfprApNfsMountInstRn": cfprApNfsMountInstRn,
       "cfprApNfsMountInstAdminState": cfprApNfsMountInstAdminState,
       "cfprApNfsMountInstClientConfigState": cfprApNfsMountInstClientConfigState,
       "cfprApNfsMountInstDefDn": cfprApNfsMountInstDefDn,
       "cfprApNfsMountInstFsmDescr": cfprApNfsMountInstFsmDescr,
       "cfprApNfsMountInstFsmPrev": cfprApNfsMountInstFsmPrev,
       "cfprApNfsMountInstFsmProgr": cfprApNfsMountInstFsmProgr,
       "cfprApNfsMountInstFsmRmtInvErrCode": cfprApNfsMountInstFsmRmtInvErrCode,
       "cfprApNfsMountInstFsmRmtInvErrDescr": cfprApNfsMountInstFsmRmtInvErrDescr,
       "cfprApNfsMountInstFsmRmtInvRslt": cfprApNfsMountInstFsmRmtInvRslt,
       "cfprApNfsMountInstFsmStageDescr": cfprApNfsMountInstFsmStageDescr,
       "cfprApNfsMountInstFsmStamp": cfprApNfsMountInstFsmStamp,
       "cfprApNfsMountInstFsmStatus": cfprApNfsMountInstFsmStatus,
       "cfprApNfsMountInstFsmTry": cfprApNfsMountInstFsmTry,
       "cfprApNfsMountInstLocalDir": cfprApNfsMountInstLocalDir,
       "cfprApNfsMountInstName": cfprApNfsMountInstName,
       "cfprApNfsMountInstOperState": cfprApNfsMountInstOperState,
       "cfprApNfsMountInstPurpose": cfprApNfsMountInstPurpose,
       "cfprApNfsMountInstRemoteDir": cfprApNfsMountInstRemoteDir,
       "cfprApNfsMountInstServer": cfprApNfsMountInstServer,
       "cfprApNfsMountInstFsmTable": cfprApNfsMountInstFsmTable,
       "cfprApNfsMountInstFsmEntry": cfprApNfsMountInstFsmEntry,
       "cfprApNfsMountInstFsmInstanceId": cfprApNfsMountInstFsmInstanceId,
       "cfprApNfsMountInstFsmDn": cfprApNfsMountInstFsmDn,
       "cfprApNfsMountInstFsmRn": cfprApNfsMountInstFsmRn,
       "cfprApNfsMountInstFsmCompletionTime": cfprApNfsMountInstFsmCompletionTime,
       "cfprApNfsMountInstFsmCurrentFsm": cfprApNfsMountInstFsmCurrentFsm,
       "cfprApNfsMountInstFsmDescrData": cfprApNfsMountInstFsmDescrData,
       "cfprApNfsMountInstFsmFsmStatus": cfprApNfsMountInstFsmFsmStatus,
       "cfprApNfsMountInstFsmProgress": cfprApNfsMountInstFsmProgress,
       "cfprApNfsMountInstFsmRmtErrCode": cfprApNfsMountInstFsmRmtErrCode,
       "cfprApNfsMountInstFsmRmtErrDescr": cfprApNfsMountInstFsmRmtErrDescr,
       "cfprApNfsMountInstFsmRmtRslt": cfprApNfsMountInstFsmRmtRslt,
       "cfprApNfsMountInstFsmStageTable": cfprApNfsMountInstFsmStageTable,
       "cfprApNfsMountInstFsmStageEntry": cfprApNfsMountInstFsmStageEntry,
       "cfprApNfsMountInstFsmStageInstanceId": cfprApNfsMountInstFsmStageInstanceId,
       "cfprApNfsMountInstFsmStageDn": cfprApNfsMountInstFsmStageDn,
       "cfprApNfsMountInstFsmStageRn": cfprApNfsMountInstFsmStageRn,
       "cfprApNfsMountInstFsmStageDescrData": cfprApNfsMountInstFsmStageDescrData,
       "cfprApNfsMountInstFsmStageLastUpdateTime": cfprApNfsMountInstFsmStageLastUpdateTime,
       "cfprApNfsMountInstFsmStageName": cfprApNfsMountInstFsmStageName,
       "cfprApNfsMountInstFsmStageOrder": cfprApNfsMountInstFsmStageOrder,
       "cfprApNfsMountInstFsmStageRetry": cfprApNfsMountInstFsmStageRetry,
       "cfprApNfsMountInstFsmStageStageStatus": cfprApNfsMountInstFsmStageStageStatus,
       "cfprApNfsMountInstFsmTaskTable": cfprApNfsMountInstFsmTaskTable,
       "cfprApNfsMountInstFsmTaskEntry": cfprApNfsMountInstFsmTaskEntry,
       "cfprApNfsMountInstFsmTaskInstanceId": cfprApNfsMountInstFsmTaskInstanceId,
       "cfprApNfsMountInstFsmTaskDn": cfprApNfsMountInstFsmTaskDn,
       "cfprApNfsMountInstFsmTaskRn": cfprApNfsMountInstFsmTaskRn,
       "cfprApNfsMountInstFsmTaskCompletion": cfprApNfsMountInstFsmTaskCompletion,
       "cfprApNfsMountInstFsmTaskFlags": cfprApNfsMountInstFsmTaskFlags,
       "cfprApNfsMountInstFsmTaskItem": cfprApNfsMountInstFsmTaskItem,
       "cfprApNfsMountInstFsmTaskSeqId": cfprApNfsMountInstFsmTaskSeqId}
)
