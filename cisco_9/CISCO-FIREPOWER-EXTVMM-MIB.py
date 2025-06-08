# SNMP MIB module (CISCO-FIREPOWER-EXTVMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-EXTVMM-MIB.mib
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

(CfprCommFilePathProtocol,
 CfprConditionRemoteInvRslt,
 CfprExtvmmEpFsmCurrentFsm,
 CfprExtvmmEpFsmStageName,
 CfprExtvmmEpFsmTaskItem,
 CfprExtvmmFabricNetworkType,
 CfprExtvmmKeyStoreFsmCurrentFsm,
 CfprExtvmmKeyStoreFsmStageName,
 CfprExtvmmKeyStoreFsmTaskItem,
 CfprExtvmmMasterExtKeyFsmCurrentFsm,
 CfprExtvmmMasterExtKeyFsmStageName,
 CfprExtvmmMasterExtKeyFsmTaskItem,
 CfprExtvmmNetworkSetConfigQualifier,
 CfprExtvmmNetworkSetsFsmCurrentFsm,
 CfprExtvmmNetworkSetsFsmStageName,
 CfprExtvmmNetworkSetsFsmTaskItem,
 CfprExtvmmProviderFsmCurrentFsm,
 CfprExtvmmProviderFsmStageName,
 CfprExtvmmProviderFsmTaskItem,
 CfprExtvmmProviderVendorType,
 CfprExtvmmRefOperState,
 CfprExtvmmSwitchDelTaskFsmCurrentFsm,
 CfprExtvmmSwitchDelTaskFsmStageName,
 CfprExtvmmSwitchDelTaskFsmTaskItem,
 CfprExtvmmVcVersion,
 CfprExtvmmVnicType,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprCommFilePathProtocol",
    "CfprConditionRemoteInvRslt",
    "CfprExtvmmEpFsmCurrentFsm",
    "CfprExtvmmEpFsmStageName",
    "CfprExtvmmEpFsmTaskItem",
    "CfprExtvmmFabricNetworkType",
    "CfprExtvmmKeyStoreFsmCurrentFsm",
    "CfprExtvmmKeyStoreFsmStageName",
    "CfprExtvmmKeyStoreFsmTaskItem",
    "CfprExtvmmMasterExtKeyFsmCurrentFsm",
    "CfprExtvmmMasterExtKeyFsmStageName",
    "CfprExtvmmMasterExtKeyFsmTaskItem",
    "CfprExtvmmNetworkSetConfigQualifier",
    "CfprExtvmmNetworkSetsFsmCurrentFsm",
    "CfprExtvmmNetworkSetsFsmStageName",
    "CfprExtvmmNetworkSetsFsmTaskItem",
    "CfprExtvmmProviderFsmCurrentFsm",
    "CfprExtvmmProviderFsmStageName",
    "CfprExtvmmProviderFsmTaskItem",
    "CfprExtvmmProviderVendorType",
    "CfprExtvmmRefOperState",
    "CfprExtvmmSwitchDelTaskFsmCurrentFsm",
    "CfprExtvmmSwitchDelTaskFsmStageName",
    "CfprExtvmmSwitchDelTaskFsmTaskItem",
    "CfprExtvmmVcVersion",
    "CfprExtvmmVnicType",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
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

cfprExtvmmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprExtvmmEpTable_Object = MibTable
cfprExtvmmEpTable = _CfprExtvmmEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1)
)
if mibBuilder.loadTexts:
    cfprExtvmmEpTable.setStatus("current")
_CfprExtvmmEpEntry_Object = MibTableRow
cfprExtvmmEpEntry = _CfprExtvmmEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1)
)
cfprExtvmmEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmEpEntry.setStatus("current")
_CfprExtvmmEpInstanceId_Type = CfprManagedObjectId
_CfprExtvmmEpInstanceId_Object = MibTableColumn
cfprExtvmmEpInstanceId = _CfprExtvmmEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 1),
    _CfprExtvmmEpInstanceId_Type()
)
cfprExtvmmEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmEpInstanceId.setStatus("current")
_CfprExtvmmEpDn_Type = CfprManagedObjectDn
_CfprExtvmmEpDn_Object = MibTableColumn
cfprExtvmmEpDn = _CfprExtvmmEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 2),
    _CfprExtvmmEpDn_Type()
)
cfprExtvmmEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpDn.setStatus("current")
_CfprExtvmmEpRn_Type = SnmpAdminString
_CfprExtvmmEpRn_Object = MibTableColumn
cfprExtvmmEpRn = _CfprExtvmmEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 3),
    _CfprExtvmmEpRn_Type()
)
cfprExtvmmEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpRn.setStatus("current")
_CfprExtvmmEpFsmDescr_Type = SnmpAdminString
_CfprExtvmmEpFsmDescr_Object = MibTableColumn
cfprExtvmmEpFsmDescr = _CfprExtvmmEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 4),
    _CfprExtvmmEpFsmDescr_Type()
)
cfprExtvmmEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmDescr.setStatus("current")
_CfprExtvmmEpFsmPrev_Type = SnmpAdminString
_CfprExtvmmEpFsmPrev_Object = MibTableColumn
cfprExtvmmEpFsmPrev = _CfprExtvmmEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 5),
    _CfprExtvmmEpFsmPrev_Type()
)
cfprExtvmmEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmPrev.setStatus("current")
_CfprExtvmmEpFsmProgr_Type = Gauge32
_CfprExtvmmEpFsmProgr_Object = MibTableColumn
cfprExtvmmEpFsmProgr = _CfprExtvmmEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 6),
    _CfprExtvmmEpFsmProgr_Type()
)
cfprExtvmmEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmProgr.setStatus("current")
_CfprExtvmmEpFsmRmtInvErrCode_Type = Gauge32
_CfprExtvmmEpFsmRmtInvErrCode_Object = MibTableColumn
cfprExtvmmEpFsmRmtInvErrCode = _CfprExtvmmEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 7),
    _CfprExtvmmEpFsmRmtInvErrCode_Type()
)
cfprExtvmmEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmRmtInvErrCode.setStatus("current")
_CfprExtvmmEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtvmmEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtvmmEpFsmRmtInvErrDescr = _CfprExtvmmEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 8),
    _CfprExtvmmEpFsmRmtInvErrDescr_Type()
)
cfprExtvmmEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmRmtInvErrDescr.setStatus("current")
_CfprExtvmmEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmEpFsmRmtInvRslt_Object = MibTableColumn
cfprExtvmmEpFsmRmtInvRslt = _CfprExtvmmEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 9),
    _CfprExtvmmEpFsmRmtInvRslt_Type()
)
cfprExtvmmEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmRmtInvRslt.setStatus("current")
_CfprExtvmmEpFsmStageDescr_Type = SnmpAdminString
_CfprExtvmmEpFsmStageDescr_Object = MibTableColumn
cfprExtvmmEpFsmStageDescr = _CfprExtvmmEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 10),
    _CfprExtvmmEpFsmStageDescr_Type()
)
cfprExtvmmEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageDescr.setStatus("current")
_CfprExtvmmEpFsmStamp_Type = DateAndTime
_CfprExtvmmEpFsmStamp_Object = MibTableColumn
cfprExtvmmEpFsmStamp = _CfprExtvmmEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 11),
    _CfprExtvmmEpFsmStamp_Type()
)
cfprExtvmmEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStamp.setStatus("current")
_CfprExtvmmEpFsmStatus_Type = SnmpAdminString
_CfprExtvmmEpFsmStatus_Object = MibTableColumn
cfprExtvmmEpFsmStatus = _CfprExtvmmEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 12),
    _CfprExtvmmEpFsmStatus_Type()
)
cfprExtvmmEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStatus.setStatus("current")
_CfprExtvmmEpFsmTry_Type = Gauge32
_CfprExtvmmEpFsmTry_Object = MibTableColumn
cfprExtvmmEpFsmTry = _CfprExtvmmEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 13),
    _CfprExtvmmEpFsmTry_Type()
)
cfprExtvmmEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTry.setStatus("current")
_CfprExtvmmEpGenNum_Type = Gauge32
_CfprExtvmmEpGenNum_Object = MibTableColumn
cfprExtvmmEpGenNum = _CfprExtvmmEpGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 1, 1, 14),
    _CfprExtvmmEpGenNum_Type()
)
cfprExtvmmEpGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpGenNum.setStatus("current")
_CfprExtvmmEpFsmTable_Object = MibTable
cfprExtvmmEpFsmTable = _CfprExtvmmEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2)
)
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTable.setStatus("current")
_CfprExtvmmEpFsmEntry_Object = MibTableRow
cfprExtvmmEpFsmEntry = _CfprExtvmmEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1)
)
cfprExtvmmEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmEntry.setStatus("current")
_CfprExtvmmEpFsmInstanceId_Type = CfprManagedObjectId
_CfprExtvmmEpFsmInstanceId_Object = MibTableColumn
cfprExtvmmEpFsmInstanceId = _CfprExtvmmEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 1),
    _CfprExtvmmEpFsmInstanceId_Type()
)
cfprExtvmmEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmInstanceId.setStatus("current")
_CfprExtvmmEpFsmDn_Type = CfprManagedObjectDn
_CfprExtvmmEpFsmDn_Object = MibTableColumn
cfprExtvmmEpFsmDn = _CfprExtvmmEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 2),
    _CfprExtvmmEpFsmDn_Type()
)
cfprExtvmmEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmDn.setStatus("current")
_CfprExtvmmEpFsmRn_Type = SnmpAdminString
_CfprExtvmmEpFsmRn_Object = MibTableColumn
cfprExtvmmEpFsmRn = _CfprExtvmmEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 3),
    _CfprExtvmmEpFsmRn_Type()
)
cfprExtvmmEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmRn.setStatus("current")
_CfprExtvmmEpFsmCompletionTime_Type = DateAndTime
_CfprExtvmmEpFsmCompletionTime_Object = MibTableColumn
cfprExtvmmEpFsmCompletionTime = _CfprExtvmmEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 4),
    _CfprExtvmmEpFsmCompletionTime_Type()
)
cfprExtvmmEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmCompletionTime.setStatus("current")
_CfprExtvmmEpFsmCurrentFsm_Type = CfprExtvmmEpFsmCurrentFsm
_CfprExtvmmEpFsmCurrentFsm_Object = MibTableColumn
cfprExtvmmEpFsmCurrentFsm = _CfprExtvmmEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 5),
    _CfprExtvmmEpFsmCurrentFsm_Type()
)
cfprExtvmmEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmCurrentFsm.setStatus("current")
_CfprExtvmmEpFsmDescrData_Type = SnmpAdminString
_CfprExtvmmEpFsmDescrData_Object = MibTableColumn
cfprExtvmmEpFsmDescrData = _CfprExtvmmEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 6),
    _CfprExtvmmEpFsmDescrData_Type()
)
cfprExtvmmEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmDescrData.setStatus("current")
_CfprExtvmmEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmEpFsmFsmStatus_Object = MibTableColumn
cfprExtvmmEpFsmFsmStatus = _CfprExtvmmEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 7),
    _CfprExtvmmEpFsmFsmStatus_Type()
)
cfprExtvmmEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmFsmStatus.setStatus("current")
_CfprExtvmmEpFsmProgress_Type = Gauge32
_CfprExtvmmEpFsmProgress_Object = MibTableColumn
cfprExtvmmEpFsmProgress = _CfprExtvmmEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 8),
    _CfprExtvmmEpFsmProgress_Type()
)
cfprExtvmmEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmProgress.setStatus("current")
_CfprExtvmmEpFsmRmtErrCode_Type = Gauge32
_CfprExtvmmEpFsmRmtErrCode_Object = MibTableColumn
cfprExtvmmEpFsmRmtErrCode = _CfprExtvmmEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 9),
    _CfprExtvmmEpFsmRmtErrCode_Type()
)
cfprExtvmmEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmRmtErrCode.setStatus("current")
_CfprExtvmmEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtvmmEpFsmRmtErrDescr_Object = MibTableColumn
cfprExtvmmEpFsmRmtErrDescr = _CfprExtvmmEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 10),
    _CfprExtvmmEpFsmRmtErrDescr_Type()
)
cfprExtvmmEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmRmtErrDescr.setStatus("current")
_CfprExtvmmEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmEpFsmRmtRslt_Object = MibTableColumn
cfprExtvmmEpFsmRmtRslt = _CfprExtvmmEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 2, 1, 11),
    _CfprExtvmmEpFsmRmtRslt_Type()
)
cfprExtvmmEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmRmtRslt.setStatus("current")
_CfprExtvmmEpFsmStageTable_Object = MibTable
cfprExtvmmEpFsmStageTable = _CfprExtvmmEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3)
)
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageTable.setStatus("current")
_CfprExtvmmEpFsmStageEntry_Object = MibTableRow
cfprExtvmmEpFsmStageEntry = _CfprExtvmmEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1)
)
cfprExtvmmEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageEntry.setStatus("current")
_CfprExtvmmEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtvmmEpFsmStageInstanceId_Object = MibTableColumn
cfprExtvmmEpFsmStageInstanceId = _CfprExtvmmEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 1),
    _CfprExtvmmEpFsmStageInstanceId_Type()
)
cfprExtvmmEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageInstanceId.setStatus("current")
_CfprExtvmmEpFsmStageDn_Type = CfprManagedObjectDn
_CfprExtvmmEpFsmStageDn_Object = MibTableColumn
cfprExtvmmEpFsmStageDn = _CfprExtvmmEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 2),
    _CfprExtvmmEpFsmStageDn_Type()
)
cfprExtvmmEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageDn.setStatus("current")
_CfprExtvmmEpFsmStageRn_Type = SnmpAdminString
_CfprExtvmmEpFsmStageRn_Object = MibTableColumn
cfprExtvmmEpFsmStageRn = _CfprExtvmmEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 3),
    _CfprExtvmmEpFsmStageRn_Type()
)
cfprExtvmmEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageRn.setStatus("current")
_CfprExtvmmEpFsmStageDescrData_Type = SnmpAdminString
_CfprExtvmmEpFsmStageDescrData_Object = MibTableColumn
cfprExtvmmEpFsmStageDescrData = _CfprExtvmmEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 4),
    _CfprExtvmmEpFsmStageDescrData_Type()
)
cfprExtvmmEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageDescrData.setStatus("current")
_CfprExtvmmEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtvmmEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtvmmEpFsmStageLastUpdateTime = _CfprExtvmmEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 5),
    _CfprExtvmmEpFsmStageLastUpdateTime_Type()
)
cfprExtvmmEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageLastUpdateTime.setStatus("current")
_CfprExtvmmEpFsmStageName_Type = CfprExtvmmEpFsmStageName
_CfprExtvmmEpFsmStageName_Object = MibTableColumn
cfprExtvmmEpFsmStageName = _CfprExtvmmEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 6),
    _CfprExtvmmEpFsmStageName_Type()
)
cfprExtvmmEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageName.setStatus("current")
_CfprExtvmmEpFsmStageOrder_Type = Gauge32
_CfprExtvmmEpFsmStageOrder_Object = MibTableColumn
cfprExtvmmEpFsmStageOrder = _CfprExtvmmEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 7),
    _CfprExtvmmEpFsmStageOrder_Type()
)
cfprExtvmmEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageOrder.setStatus("current")
_CfprExtvmmEpFsmStageRetry_Type = Gauge32
_CfprExtvmmEpFsmStageRetry_Object = MibTableColumn
cfprExtvmmEpFsmStageRetry = _CfprExtvmmEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 8),
    _CfprExtvmmEpFsmStageRetry_Type()
)
cfprExtvmmEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageRetry.setStatus("current")
_CfprExtvmmEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmEpFsmStageStageStatus_Object = MibTableColumn
cfprExtvmmEpFsmStageStageStatus = _CfprExtvmmEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 3, 1, 9),
    _CfprExtvmmEpFsmStageStageStatus_Type()
)
cfprExtvmmEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmStageStageStatus.setStatus("current")
_CfprExtvmmEpFsmTaskTable_Object = MibTable
cfprExtvmmEpFsmTaskTable = _CfprExtvmmEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4)
)
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskTable.setStatus("current")
_CfprExtvmmEpFsmTaskEntry_Object = MibTableRow
cfprExtvmmEpFsmTaskEntry = _CfprExtvmmEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4, 1)
)
cfprExtvmmEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskEntry.setStatus("current")
_CfprExtvmmEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtvmmEpFsmTaskInstanceId_Object = MibTableColumn
cfprExtvmmEpFsmTaskInstanceId = _CfprExtvmmEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4, 1, 1),
    _CfprExtvmmEpFsmTaskInstanceId_Type()
)
cfprExtvmmEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskInstanceId.setStatus("current")
_CfprExtvmmEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtvmmEpFsmTaskDn_Object = MibTableColumn
cfprExtvmmEpFsmTaskDn = _CfprExtvmmEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4, 1, 2),
    _CfprExtvmmEpFsmTaskDn_Type()
)
cfprExtvmmEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskDn.setStatus("current")
_CfprExtvmmEpFsmTaskRn_Type = SnmpAdminString
_CfprExtvmmEpFsmTaskRn_Object = MibTableColumn
cfprExtvmmEpFsmTaskRn = _CfprExtvmmEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4, 1, 3),
    _CfprExtvmmEpFsmTaskRn_Type()
)
cfprExtvmmEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskRn.setStatus("current")
_CfprExtvmmEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtvmmEpFsmTaskCompletion_Object = MibTableColumn
cfprExtvmmEpFsmTaskCompletion = _CfprExtvmmEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4, 1, 4),
    _CfprExtvmmEpFsmTaskCompletion_Type()
)
cfprExtvmmEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskCompletion.setStatus("current")
_CfprExtvmmEpFsmTaskFlags_Type = CfprFsmFlags
_CfprExtvmmEpFsmTaskFlags_Object = MibTableColumn
cfprExtvmmEpFsmTaskFlags = _CfprExtvmmEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4, 1, 5),
    _CfprExtvmmEpFsmTaskFlags_Type()
)
cfprExtvmmEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskFlags.setStatus("current")
_CfprExtvmmEpFsmTaskItem_Type = CfprExtvmmEpFsmTaskItem
_CfprExtvmmEpFsmTaskItem_Object = MibTableColumn
cfprExtvmmEpFsmTaskItem = _CfprExtvmmEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4, 1, 6),
    _CfprExtvmmEpFsmTaskItem_Type()
)
cfprExtvmmEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskItem.setStatus("current")
_CfprExtvmmEpFsmTaskSeqId_Type = Gauge32
_CfprExtvmmEpFsmTaskSeqId_Object = MibTableColumn
cfprExtvmmEpFsmTaskSeqId = _CfprExtvmmEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 4, 1, 7),
    _CfprExtvmmEpFsmTaskSeqId_Type()
)
cfprExtvmmEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmEpFsmTaskSeqId.setStatus("current")
_CfprExtvmmFNDReferenceTable_Object = MibTable
cfprExtvmmFNDReferenceTable = _CfprExtvmmFNDReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5)
)
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceTable.setStatus("current")
_CfprExtvmmFNDReferenceEntry_Object = MibTableRow
cfprExtvmmFNDReferenceEntry = _CfprExtvmmFNDReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1)
)
cfprExtvmmFNDReferenceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmFNDReferenceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceEntry.setStatus("current")
_CfprExtvmmFNDReferenceInstanceId_Type = CfprManagedObjectId
_CfprExtvmmFNDReferenceInstanceId_Object = MibTableColumn
cfprExtvmmFNDReferenceInstanceId = _CfprExtvmmFNDReferenceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 1),
    _CfprExtvmmFNDReferenceInstanceId_Type()
)
cfprExtvmmFNDReferenceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceInstanceId.setStatus("current")
_CfprExtvmmFNDReferenceDn_Type = CfprManagedObjectDn
_CfprExtvmmFNDReferenceDn_Object = MibTableColumn
cfprExtvmmFNDReferenceDn = _CfprExtvmmFNDReferenceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 2),
    _CfprExtvmmFNDReferenceDn_Type()
)
cfprExtvmmFNDReferenceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceDn.setStatus("current")
_CfprExtvmmFNDReferenceRn_Type = SnmpAdminString
_CfprExtvmmFNDReferenceRn_Object = MibTableColumn
cfprExtvmmFNDReferenceRn = _CfprExtvmmFNDReferenceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 3),
    _CfprExtvmmFNDReferenceRn_Type()
)
cfprExtvmmFNDReferenceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceRn.setStatus("current")
_CfprExtvmmFNDReferenceDescr_Type = SnmpAdminString
_CfprExtvmmFNDReferenceDescr_Object = MibTableColumn
cfprExtvmmFNDReferenceDescr = _CfprExtvmmFNDReferenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 4),
    _CfprExtvmmFNDReferenceDescr_Type()
)
cfprExtvmmFNDReferenceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceDescr.setStatus("current")
_CfprExtvmmFNDReferenceFnDefName_Type = SnmpAdminString
_CfprExtvmmFNDReferenceFnDefName_Object = MibTableColumn
cfprExtvmmFNDReferenceFnDefName = _CfprExtvmmFNDReferenceFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 5),
    _CfprExtvmmFNDReferenceFnDefName_Type()
)
cfprExtvmmFNDReferenceFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceFnDefName.setStatus("current")
_CfprExtvmmFNDReferenceIntId_Type = SnmpAdminString
_CfprExtvmmFNDReferenceIntId_Object = MibTableColumn
cfprExtvmmFNDReferenceIntId = _CfprExtvmmFNDReferenceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 6),
    _CfprExtvmmFNDReferenceIntId_Type()
)
cfprExtvmmFNDReferenceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceIntId.setStatus("current")
_CfprExtvmmFNDReferenceName_Type = SnmpAdminString
_CfprExtvmmFNDReferenceName_Object = MibTableColumn
cfprExtvmmFNDReferenceName = _CfprExtvmmFNDReferenceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 7),
    _CfprExtvmmFNDReferenceName_Type()
)
cfprExtvmmFNDReferenceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceName.setStatus("current")
_CfprExtvmmFNDReferenceOperFnDefName_Type = SnmpAdminString
_CfprExtvmmFNDReferenceOperFnDefName_Object = MibTableColumn
cfprExtvmmFNDReferenceOperFnDefName = _CfprExtvmmFNDReferenceOperFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 8),
    _CfprExtvmmFNDReferenceOperFnDefName_Type()
)
cfprExtvmmFNDReferenceOperFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferenceOperFnDefName.setStatus("current")
_CfprExtvmmFNDReferencePolicyLevel_Type = Gauge32
_CfprExtvmmFNDReferencePolicyLevel_Object = MibTableColumn
cfprExtvmmFNDReferencePolicyLevel = _CfprExtvmmFNDReferencePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 9),
    _CfprExtvmmFNDReferencePolicyLevel_Type()
)
cfprExtvmmFNDReferencePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferencePolicyLevel.setStatus("current")
_CfprExtvmmFNDReferencePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmFNDReferencePolicyOwner_Object = MibTableColumn
cfprExtvmmFNDReferencePolicyOwner = _CfprExtvmmFNDReferencePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 5, 1, 10),
    _CfprExtvmmFNDReferencePolicyOwner_Type()
)
cfprExtvmmFNDReferencePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFNDReferencePolicyOwner.setStatus("current")
_CfprExtvmmFabricNetworkTable_Object = MibTable
cfprExtvmmFabricNetworkTable = _CfprExtvmmFabricNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6)
)
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkTable.setStatus("current")
_CfprExtvmmFabricNetworkEntry_Object = MibTableRow
cfprExtvmmFabricNetworkEntry = _CfprExtvmmFabricNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1)
)
cfprExtvmmFabricNetworkEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmFabricNetworkInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkEntry.setStatus("current")
_CfprExtvmmFabricNetworkInstanceId_Type = CfprManagedObjectId
_CfprExtvmmFabricNetworkInstanceId_Object = MibTableColumn
cfprExtvmmFabricNetworkInstanceId = _CfprExtvmmFabricNetworkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 1),
    _CfprExtvmmFabricNetworkInstanceId_Type()
)
cfprExtvmmFabricNetworkInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkInstanceId.setStatus("current")
_CfprExtvmmFabricNetworkDn_Type = CfprManagedObjectDn
_CfprExtvmmFabricNetworkDn_Object = MibTableColumn
cfprExtvmmFabricNetworkDn = _CfprExtvmmFabricNetworkDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 2),
    _CfprExtvmmFabricNetworkDn_Type()
)
cfprExtvmmFabricNetworkDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDn.setStatus("current")
_CfprExtvmmFabricNetworkRn_Type = SnmpAdminString
_CfprExtvmmFabricNetworkRn_Object = MibTableColumn
cfprExtvmmFabricNetworkRn = _CfprExtvmmFabricNetworkRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 3),
    _CfprExtvmmFabricNetworkRn_Type()
)
cfprExtvmmFabricNetworkRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkRn.setStatus("current")
_CfprExtvmmFabricNetworkDescr_Type = SnmpAdminString
_CfprExtvmmFabricNetworkDescr_Object = MibTableColumn
cfprExtvmmFabricNetworkDescr = _CfprExtvmmFabricNetworkDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 4),
    _CfprExtvmmFabricNetworkDescr_Type()
)
cfprExtvmmFabricNetworkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDescr.setStatus("current")
_CfprExtvmmFabricNetworkGuid_Type = SnmpAdminString
_CfprExtvmmFabricNetworkGuid_Object = MibTableColumn
cfprExtvmmFabricNetworkGuid = _CfprExtvmmFabricNetworkGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 5),
    _CfprExtvmmFabricNetworkGuid_Type()
)
cfprExtvmmFabricNetworkGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkGuid.setStatus("current")
_CfprExtvmmFabricNetworkIntId_Type = SnmpAdminString
_CfprExtvmmFabricNetworkIntId_Object = MibTableColumn
cfprExtvmmFabricNetworkIntId = _CfprExtvmmFabricNetworkIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 6),
    _CfprExtvmmFabricNetworkIntId_Type()
)
cfprExtvmmFabricNetworkIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkIntId.setStatus("current")
_CfprExtvmmFabricNetworkName_Type = SnmpAdminString
_CfprExtvmmFabricNetworkName_Object = MibTableColumn
cfprExtvmmFabricNetworkName = _CfprExtvmmFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 7),
    _CfprExtvmmFabricNetworkName_Type()
)
cfprExtvmmFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkName.setStatus("current")
_CfprExtvmmFabricNetworkNetworkType_Type = CfprExtvmmFabricNetworkType
_CfprExtvmmFabricNetworkNetworkType_Object = MibTableColumn
cfprExtvmmFabricNetworkNetworkType = _CfprExtvmmFabricNetworkNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 8),
    _CfprExtvmmFabricNetworkNetworkType_Type()
)
cfprExtvmmFabricNetworkNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkNetworkType.setStatus("current")
_CfprExtvmmFabricNetworkPolicyLevel_Type = Gauge32
_CfprExtvmmFabricNetworkPolicyLevel_Object = MibTableColumn
cfprExtvmmFabricNetworkPolicyLevel = _CfprExtvmmFabricNetworkPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 9),
    _CfprExtvmmFabricNetworkPolicyLevel_Type()
)
cfprExtvmmFabricNetworkPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkPolicyLevel.setStatus("current")
_CfprExtvmmFabricNetworkPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmFabricNetworkPolicyOwner_Object = MibTableColumn
cfprExtvmmFabricNetworkPolicyOwner = _CfprExtvmmFabricNetworkPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 10),
    _CfprExtvmmFabricNetworkPolicyOwner_Type()
)
cfprExtvmmFabricNetworkPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkPolicyOwner.setStatus("current")
_CfprExtvmmFabricNetworkRefOperState_Type = CfprExtvmmRefOperState
_CfprExtvmmFabricNetworkRefOperState_Object = MibTableColumn
cfprExtvmmFabricNetworkRefOperState = _CfprExtvmmFabricNetworkRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 6, 1, 11),
    _CfprExtvmmFabricNetworkRefOperState_Type()
)
cfprExtvmmFabricNetworkRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkRefOperState.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionTable_Object = MibTable
cfprExtvmmFabricNetworkDefinitionTable = _CfprExtvmmFabricNetworkDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7)
)
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionTable.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionEntry_Object = MibTableRow
cfprExtvmmFabricNetworkDefinitionEntry = _CfprExtvmmFabricNetworkDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1)
)
cfprExtvmmFabricNetworkDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmFabricNetworkDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionEntry.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionInstanceId_Type = CfprManagedObjectId
_CfprExtvmmFabricNetworkDefinitionInstanceId_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionInstanceId = _CfprExtvmmFabricNetworkDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 1),
    _CfprExtvmmFabricNetworkDefinitionInstanceId_Type()
)
cfprExtvmmFabricNetworkDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionInstanceId.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionDn_Type = CfprManagedObjectDn
_CfprExtvmmFabricNetworkDefinitionDn_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionDn = _CfprExtvmmFabricNetworkDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 2),
    _CfprExtvmmFabricNetworkDefinitionDn_Type()
)
cfprExtvmmFabricNetworkDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionDn.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionRn_Type = SnmpAdminString
_CfprExtvmmFabricNetworkDefinitionRn_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionRn = _CfprExtvmmFabricNetworkDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 3),
    _CfprExtvmmFabricNetworkDefinitionRn_Type()
)
cfprExtvmmFabricNetworkDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionRn.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionAllowedVnicType_Type = CfprExtvmmVnicType
_CfprExtvmmFabricNetworkDefinitionAllowedVnicType_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionAllowedVnicType = _CfprExtvmmFabricNetworkDefinitionAllowedVnicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 4),
    _CfprExtvmmFabricNetworkDefinitionAllowedVnicType_Type()
)
cfprExtvmmFabricNetworkDefinitionAllowedVnicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionAllowedVnicType.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionDescr_Type = SnmpAdminString
_CfprExtvmmFabricNetworkDefinitionDescr_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionDescr = _CfprExtvmmFabricNetworkDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 5),
    _CfprExtvmmFabricNetworkDefinitionDescr_Type()
)
cfprExtvmmFabricNetworkDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionDescr.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionGuid_Type = SnmpAdminString
_CfprExtvmmFabricNetworkDefinitionGuid_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionGuid = _CfprExtvmmFabricNetworkDefinitionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 6),
    _CfprExtvmmFabricNetworkDefinitionGuid_Type()
)
cfprExtvmmFabricNetworkDefinitionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionGuid.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionIntId_Type = SnmpAdminString
_CfprExtvmmFabricNetworkDefinitionIntId_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionIntId = _CfprExtvmmFabricNetworkDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 7),
    _CfprExtvmmFabricNetworkDefinitionIntId_Type()
)
cfprExtvmmFabricNetworkDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionIntId.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionName_Type = SnmpAdminString
_CfprExtvmmFabricNetworkDefinitionName_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionName = _CfprExtvmmFabricNetworkDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 8),
    _CfprExtvmmFabricNetworkDefinitionName_Type()
)
cfprExtvmmFabricNetworkDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionName.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionPolicyLevel_Type = Gauge32
_CfprExtvmmFabricNetworkDefinitionPolicyLevel_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionPolicyLevel = _CfprExtvmmFabricNetworkDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 9),
    _CfprExtvmmFabricNetworkDefinitionPolicyLevel_Type()
)
cfprExtvmmFabricNetworkDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionPolicyLevel.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmFabricNetworkDefinitionPolicyOwner_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionPolicyOwner = _CfprExtvmmFabricNetworkDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 10),
    _CfprExtvmmFabricNetworkDefinitionPolicyOwner_Type()
)
cfprExtvmmFabricNetworkDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionPolicyOwner.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionPrimaryVlanId_Type = Gauge32
_CfprExtvmmFabricNetworkDefinitionPrimaryVlanId_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionPrimaryVlanId = _CfprExtvmmFabricNetworkDefinitionPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 11),
    _CfprExtvmmFabricNetworkDefinitionPrimaryVlanId_Type()
)
cfprExtvmmFabricNetworkDefinitionPrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionPrimaryVlanId.setStatus("current")
_CfprExtvmmFabricNetworkDefinitionRefOperState_Type = CfprExtvmmRefOperState
_CfprExtvmmFabricNetworkDefinitionRefOperState_Object = MibTableColumn
cfprExtvmmFabricNetworkDefinitionRefOperState = _CfprExtvmmFabricNetworkDefinitionRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 7, 1, 12),
    _CfprExtvmmFabricNetworkDefinitionRefOperState_Type()
)
cfprExtvmmFabricNetworkDefinitionRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmFabricNetworkDefinitionRefOperState.setStatus("current")
_CfprExtvmmKeyInstTable_Object = MibTable
cfprExtvmmKeyInstTable = _CfprExtvmmKeyInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 8)
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyInstTable.setStatus("current")
_CfprExtvmmKeyInstEntry_Object = MibTableRow
cfprExtvmmKeyInstEntry = _CfprExtvmmKeyInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 8, 1)
)
cfprExtvmmKeyInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmKeyInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyInstEntry.setStatus("current")
_CfprExtvmmKeyInstInstanceId_Type = CfprManagedObjectId
_CfprExtvmmKeyInstInstanceId_Object = MibTableColumn
cfprExtvmmKeyInstInstanceId = _CfprExtvmmKeyInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 8, 1, 1),
    _CfprExtvmmKeyInstInstanceId_Type()
)
cfprExtvmmKeyInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmKeyInstInstanceId.setStatus("current")
_CfprExtvmmKeyInstDn_Type = CfprManagedObjectDn
_CfprExtvmmKeyInstDn_Object = MibTableColumn
cfprExtvmmKeyInstDn = _CfprExtvmmKeyInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 8, 1, 2),
    _CfprExtvmmKeyInstDn_Type()
)
cfprExtvmmKeyInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyInstDn.setStatus("current")
_CfprExtvmmKeyInstRn_Type = SnmpAdminString
_CfprExtvmmKeyInstRn_Object = MibTableColumn
cfprExtvmmKeyInstRn = _CfprExtvmmKeyInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 8, 1, 3),
    _CfprExtvmmKeyInstRn_Type()
)
cfprExtvmmKeyInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyInstRn.setStatus("current")
_CfprExtvmmKeyInstInst_Type = Gauge32
_CfprExtvmmKeyInstInst_Object = MibTableColumn
cfprExtvmmKeyInstInst = _CfprExtvmmKeyInstInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 8, 1, 4),
    _CfprExtvmmKeyInstInst_Type()
)
cfprExtvmmKeyInstInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyInstInst.setStatus("current")
_CfprExtvmmKeyInstKey_Type = SnmpAdminString
_CfprExtvmmKeyInstKey_Object = MibTableColumn
cfprExtvmmKeyInstKey = _CfprExtvmmKeyInstKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 8, 1, 5),
    _CfprExtvmmKeyInstKey_Type()
)
cfprExtvmmKeyInstKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyInstKey.setStatus("current")
_CfprExtvmmKeyRingTable_Object = MibTable
cfprExtvmmKeyRingTable = _CfprExtvmmKeyRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9)
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingTable.setStatus("current")
_CfprExtvmmKeyRingEntry_Object = MibTableRow
cfprExtvmmKeyRingEntry = _CfprExtvmmKeyRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9, 1)
)
cfprExtvmmKeyRingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmKeyRingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingEntry.setStatus("current")
_CfprExtvmmKeyRingInstanceId_Type = CfprManagedObjectId
_CfprExtvmmKeyRingInstanceId_Object = MibTableColumn
cfprExtvmmKeyRingInstanceId = _CfprExtvmmKeyRingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9, 1, 1),
    _CfprExtvmmKeyRingInstanceId_Type()
)
cfprExtvmmKeyRingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingInstanceId.setStatus("current")
_CfprExtvmmKeyRingDn_Type = CfprManagedObjectDn
_CfprExtvmmKeyRingDn_Object = MibTableColumn
cfprExtvmmKeyRingDn = _CfprExtvmmKeyRingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9, 1, 2),
    _CfprExtvmmKeyRingDn_Type()
)
cfprExtvmmKeyRingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingDn.setStatus("current")
_CfprExtvmmKeyRingRn_Type = SnmpAdminString
_CfprExtvmmKeyRingRn_Object = MibTableColumn
cfprExtvmmKeyRingRn = _CfprExtvmmKeyRingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9, 1, 3),
    _CfprExtvmmKeyRingRn_Type()
)
cfprExtvmmKeyRingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingRn.setStatus("current")
_CfprExtvmmKeyRingCertFile_Type = SnmpAdminString
_CfprExtvmmKeyRingCertFile_Object = MibTableColumn
cfprExtvmmKeyRingCertFile = _CfprExtvmmKeyRingCertFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9, 1, 4),
    _CfprExtvmmKeyRingCertFile_Type()
)
cfprExtvmmKeyRingCertFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingCertFile.setStatus("current")
_CfprExtvmmKeyRingLocation_Type = CfprCommFilePathProtocol
_CfprExtvmmKeyRingLocation_Object = MibTableColumn
cfprExtvmmKeyRingLocation = _CfprExtvmmKeyRingLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9, 1, 5),
    _CfprExtvmmKeyRingLocation_Type()
)
cfprExtvmmKeyRingLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingLocation.setStatus("current")
_CfprExtvmmKeyRingName_Type = SnmpAdminString
_CfprExtvmmKeyRingName_Object = MibTableColumn
cfprExtvmmKeyRingName = _CfprExtvmmKeyRingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9, 1, 6),
    _CfprExtvmmKeyRingName_Type()
)
cfprExtvmmKeyRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingName.setStatus("current")
_CfprExtvmmKeyRingPath_Type = SnmpAdminString
_CfprExtvmmKeyRingPath_Object = MibTableColumn
cfprExtvmmKeyRingPath = _CfprExtvmmKeyRingPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 9, 1, 7),
    _CfprExtvmmKeyRingPath_Type()
)
cfprExtvmmKeyRingPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyRingPath.setStatus("current")
_CfprExtvmmKeyStoreTable_Object = MibTable
cfprExtvmmKeyStoreTable = _CfprExtvmmKeyStoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10)
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreTable.setStatus("current")
_CfprExtvmmKeyStoreEntry_Object = MibTableRow
cfprExtvmmKeyStoreEntry = _CfprExtvmmKeyStoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1)
)
cfprExtvmmKeyStoreEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmKeyStoreInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreEntry.setStatus("current")
_CfprExtvmmKeyStoreInstanceId_Type = CfprManagedObjectId
_CfprExtvmmKeyStoreInstanceId_Object = MibTableColumn
cfprExtvmmKeyStoreInstanceId = _CfprExtvmmKeyStoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 1),
    _CfprExtvmmKeyStoreInstanceId_Type()
)
cfprExtvmmKeyStoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreInstanceId.setStatus("current")
_CfprExtvmmKeyStoreDn_Type = CfprManagedObjectDn
_CfprExtvmmKeyStoreDn_Object = MibTableColumn
cfprExtvmmKeyStoreDn = _CfprExtvmmKeyStoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 2),
    _CfprExtvmmKeyStoreDn_Type()
)
cfprExtvmmKeyStoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreDn.setStatus("current")
_CfprExtvmmKeyStoreRn_Type = SnmpAdminString
_CfprExtvmmKeyStoreRn_Object = MibTableColumn
cfprExtvmmKeyStoreRn = _CfprExtvmmKeyStoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 3),
    _CfprExtvmmKeyStoreRn_Type()
)
cfprExtvmmKeyStoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreRn.setStatus("current")
_CfprExtvmmKeyStoreFsmDescr_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmDescr_Object = MibTableColumn
cfprExtvmmKeyStoreFsmDescr = _CfprExtvmmKeyStoreFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 4),
    _CfprExtvmmKeyStoreFsmDescr_Type()
)
cfprExtvmmKeyStoreFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmDescr.setStatus("current")
_CfprExtvmmKeyStoreFsmPrev_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmPrev_Object = MibTableColumn
cfprExtvmmKeyStoreFsmPrev = _CfprExtvmmKeyStoreFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 5),
    _CfprExtvmmKeyStoreFsmPrev_Type()
)
cfprExtvmmKeyStoreFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmPrev.setStatus("current")
_CfprExtvmmKeyStoreFsmProgr_Type = Gauge32
_CfprExtvmmKeyStoreFsmProgr_Object = MibTableColumn
cfprExtvmmKeyStoreFsmProgr = _CfprExtvmmKeyStoreFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 6),
    _CfprExtvmmKeyStoreFsmProgr_Type()
)
cfprExtvmmKeyStoreFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmProgr.setStatus("current")
_CfprExtvmmKeyStoreFsmRmtInvErrCode_Type = Gauge32
_CfprExtvmmKeyStoreFsmRmtInvErrCode_Object = MibTableColumn
cfprExtvmmKeyStoreFsmRmtInvErrCode = _CfprExtvmmKeyStoreFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 7),
    _CfprExtvmmKeyStoreFsmRmtInvErrCode_Type()
)
cfprExtvmmKeyStoreFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmRmtInvErrCode.setStatus("current")
_CfprExtvmmKeyStoreFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtvmmKeyStoreFsmRmtInvErrDescr = _CfprExtvmmKeyStoreFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 8),
    _CfprExtvmmKeyStoreFsmRmtInvErrDescr_Type()
)
cfprExtvmmKeyStoreFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmRmtInvErrDescr.setStatus("current")
_CfprExtvmmKeyStoreFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmKeyStoreFsmRmtInvRslt_Object = MibTableColumn
cfprExtvmmKeyStoreFsmRmtInvRslt = _CfprExtvmmKeyStoreFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 9),
    _CfprExtvmmKeyStoreFsmRmtInvRslt_Type()
)
cfprExtvmmKeyStoreFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmRmtInvRslt.setStatus("current")
_CfprExtvmmKeyStoreFsmStageDescr_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmStageDescr_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageDescr = _CfprExtvmmKeyStoreFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 10),
    _CfprExtvmmKeyStoreFsmStageDescr_Type()
)
cfprExtvmmKeyStoreFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageDescr.setStatus("current")
_CfprExtvmmKeyStoreFsmStamp_Type = DateAndTime
_CfprExtvmmKeyStoreFsmStamp_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStamp = _CfprExtvmmKeyStoreFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 11),
    _CfprExtvmmKeyStoreFsmStamp_Type()
)
cfprExtvmmKeyStoreFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStamp.setStatus("current")
_CfprExtvmmKeyStoreFsmStatus_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmStatus_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStatus = _CfprExtvmmKeyStoreFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 12),
    _CfprExtvmmKeyStoreFsmStatus_Type()
)
cfprExtvmmKeyStoreFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStatus.setStatus("current")
_CfprExtvmmKeyStoreFsmTry_Type = Gauge32
_CfprExtvmmKeyStoreFsmTry_Object = MibTableColumn
cfprExtvmmKeyStoreFsmTry = _CfprExtvmmKeyStoreFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 10, 1, 13),
    _CfprExtvmmKeyStoreFsmTry_Type()
)
cfprExtvmmKeyStoreFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTry.setStatus("current")
_CfprExtvmmKeyStoreFsmTable_Object = MibTable
cfprExtvmmKeyStoreFsmTable = _CfprExtvmmKeyStoreFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11)
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTable.setStatus("current")
_CfprExtvmmKeyStoreFsmEntry_Object = MibTableRow
cfprExtvmmKeyStoreFsmEntry = _CfprExtvmmKeyStoreFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1)
)
cfprExtvmmKeyStoreFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmKeyStoreFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmEntry.setStatus("current")
_CfprExtvmmKeyStoreFsmInstanceId_Type = CfprManagedObjectId
_CfprExtvmmKeyStoreFsmInstanceId_Object = MibTableColumn
cfprExtvmmKeyStoreFsmInstanceId = _CfprExtvmmKeyStoreFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 1),
    _CfprExtvmmKeyStoreFsmInstanceId_Type()
)
cfprExtvmmKeyStoreFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmInstanceId.setStatus("current")
_CfprExtvmmKeyStoreFsmDn_Type = CfprManagedObjectDn
_CfprExtvmmKeyStoreFsmDn_Object = MibTableColumn
cfprExtvmmKeyStoreFsmDn = _CfprExtvmmKeyStoreFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 2),
    _CfprExtvmmKeyStoreFsmDn_Type()
)
cfprExtvmmKeyStoreFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmDn.setStatus("current")
_CfprExtvmmKeyStoreFsmRn_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmRn_Object = MibTableColumn
cfprExtvmmKeyStoreFsmRn = _CfprExtvmmKeyStoreFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 3),
    _CfprExtvmmKeyStoreFsmRn_Type()
)
cfprExtvmmKeyStoreFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmRn.setStatus("current")
_CfprExtvmmKeyStoreFsmCompletionTime_Type = DateAndTime
_CfprExtvmmKeyStoreFsmCompletionTime_Object = MibTableColumn
cfprExtvmmKeyStoreFsmCompletionTime = _CfprExtvmmKeyStoreFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 4),
    _CfprExtvmmKeyStoreFsmCompletionTime_Type()
)
cfprExtvmmKeyStoreFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmCompletionTime.setStatus("current")
_CfprExtvmmKeyStoreFsmCurrentFsm_Type = CfprExtvmmKeyStoreFsmCurrentFsm
_CfprExtvmmKeyStoreFsmCurrentFsm_Object = MibTableColumn
cfprExtvmmKeyStoreFsmCurrentFsm = _CfprExtvmmKeyStoreFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 5),
    _CfprExtvmmKeyStoreFsmCurrentFsm_Type()
)
cfprExtvmmKeyStoreFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmCurrentFsm.setStatus("current")
_CfprExtvmmKeyStoreFsmDescrData_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmDescrData_Object = MibTableColumn
cfprExtvmmKeyStoreFsmDescrData = _CfprExtvmmKeyStoreFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 6),
    _CfprExtvmmKeyStoreFsmDescrData_Type()
)
cfprExtvmmKeyStoreFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmDescrData.setStatus("current")
_CfprExtvmmKeyStoreFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmKeyStoreFsmFsmStatus_Object = MibTableColumn
cfprExtvmmKeyStoreFsmFsmStatus = _CfprExtvmmKeyStoreFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 7),
    _CfprExtvmmKeyStoreFsmFsmStatus_Type()
)
cfprExtvmmKeyStoreFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmFsmStatus.setStatus("current")
_CfprExtvmmKeyStoreFsmProgress_Type = Gauge32
_CfprExtvmmKeyStoreFsmProgress_Object = MibTableColumn
cfprExtvmmKeyStoreFsmProgress = _CfprExtvmmKeyStoreFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 8),
    _CfprExtvmmKeyStoreFsmProgress_Type()
)
cfprExtvmmKeyStoreFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmProgress.setStatus("current")
_CfprExtvmmKeyStoreFsmRmtErrCode_Type = Gauge32
_CfprExtvmmKeyStoreFsmRmtErrCode_Object = MibTableColumn
cfprExtvmmKeyStoreFsmRmtErrCode = _CfprExtvmmKeyStoreFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 9),
    _CfprExtvmmKeyStoreFsmRmtErrCode_Type()
)
cfprExtvmmKeyStoreFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmRmtErrCode.setStatus("current")
_CfprExtvmmKeyStoreFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmRmtErrDescr_Object = MibTableColumn
cfprExtvmmKeyStoreFsmRmtErrDescr = _CfprExtvmmKeyStoreFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 10),
    _CfprExtvmmKeyStoreFsmRmtErrDescr_Type()
)
cfprExtvmmKeyStoreFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmRmtErrDescr.setStatus("current")
_CfprExtvmmKeyStoreFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmKeyStoreFsmRmtRslt_Object = MibTableColumn
cfprExtvmmKeyStoreFsmRmtRslt = _CfprExtvmmKeyStoreFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 11, 1, 11),
    _CfprExtvmmKeyStoreFsmRmtRslt_Type()
)
cfprExtvmmKeyStoreFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmRmtRslt.setStatus("current")
_CfprExtvmmKeyStoreFsmStageTable_Object = MibTable
cfprExtvmmKeyStoreFsmStageTable = _CfprExtvmmKeyStoreFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12)
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageTable.setStatus("current")
_CfprExtvmmKeyStoreFsmStageEntry_Object = MibTableRow
cfprExtvmmKeyStoreFsmStageEntry = _CfprExtvmmKeyStoreFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1)
)
cfprExtvmmKeyStoreFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmKeyStoreFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageEntry.setStatus("current")
_CfprExtvmmKeyStoreFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtvmmKeyStoreFsmStageInstanceId_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageInstanceId = _CfprExtvmmKeyStoreFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 1),
    _CfprExtvmmKeyStoreFsmStageInstanceId_Type()
)
cfprExtvmmKeyStoreFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageInstanceId.setStatus("current")
_CfprExtvmmKeyStoreFsmStageDn_Type = CfprManagedObjectDn
_CfprExtvmmKeyStoreFsmStageDn_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageDn = _CfprExtvmmKeyStoreFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 2),
    _CfprExtvmmKeyStoreFsmStageDn_Type()
)
cfprExtvmmKeyStoreFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageDn.setStatus("current")
_CfprExtvmmKeyStoreFsmStageRn_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmStageRn_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageRn = _CfprExtvmmKeyStoreFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 3),
    _CfprExtvmmKeyStoreFsmStageRn_Type()
)
cfprExtvmmKeyStoreFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageRn.setStatus("current")
_CfprExtvmmKeyStoreFsmStageDescrData_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmStageDescrData_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageDescrData = _CfprExtvmmKeyStoreFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 4),
    _CfprExtvmmKeyStoreFsmStageDescrData_Type()
)
cfprExtvmmKeyStoreFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageDescrData.setStatus("current")
_CfprExtvmmKeyStoreFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtvmmKeyStoreFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageLastUpdateTime = _CfprExtvmmKeyStoreFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 5),
    _CfprExtvmmKeyStoreFsmStageLastUpdateTime_Type()
)
cfprExtvmmKeyStoreFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageLastUpdateTime.setStatus("current")
_CfprExtvmmKeyStoreFsmStageName_Type = CfprExtvmmKeyStoreFsmStageName
_CfprExtvmmKeyStoreFsmStageName_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageName = _CfprExtvmmKeyStoreFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 6),
    _CfprExtvmmKeyStoreFsmStageName_Type()
)
cfprExtvmmKeyStoreFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageName.setStatus("current")
_CfprExtvmmKeyStoreFsmStageOrder_Type = Gauge32
_CfprExtvmmKeyStoreFsmStageOrder_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageOrder = _CfprExtvmmKeyStoreFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 7),
    _CfprExtvmmKeyStoreFsmStageOrder_Type()
)
cfprExtvmmKeyStoreFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageOrder.setStatus("current")
_CfprExtvmmKeyStoreFsmStageRetry_Type = Gauge32
_CfprExtvmmKeyStoreFsmStageRetry_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageRetry = _CfprExtvmmKeyStoreFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 8),
    _CfprExtvmmKeyStoreFsmStageRetry_Type()
)
cfprExtvmmKeyStoreFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageRetry.setStatus("current")
_CfprExtvmmKeyStoreFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmKeyStoreFsmStageStageStatus_Object = MibTableColumn
cfprExtvmmKeyStoreFsmStageStageStatus = _CfprExtvmmKeyStoreFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 12, 1, 9),
    _CfprExtvmmKeyStoreFsmStageStageStatus_Type()
)
cfprExtvmmKeyStoreFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmStageStageStatus.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskTable_Object = MibTable
cfprExtvmmKeyStoreFsmTaskTable = _CfprExtvmmKeyStoreFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13)
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskTable.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskEntry_Object = MibTableRow
cfprExtvmmKeyStoreFsmTaskEntry = _CfprExtvmmKeyStoreFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13, 1)
)
cfprExtvmmKeyStoreFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmKeyStoreFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskEntry.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtvmmKeyStoreFsmTaskInstanceId_Object = MibTableColumn
cfprExtvmmKeyStoreFsmTaskInstanceId = _CfprExtvmmKeyStoreFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13, 1, 1),
    _CfprExtvmmKeyStoreFsmTaskInstanceId_Type()
)
cfprExtvmmKeyStoreFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskInstanceId.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtvmmKeyStoreFsmTaskDn_Object = MibTableColumn
cfprExtvmmKeyStoreFsmTaskDn = _CfprExtvmmKeyStoreFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13, 1, 2),
    _CfprExtvmmKeyStoreFsmTaskDn_Type()
)
cfprExtvmmKeyStoreFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskDn.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskRn_Type = SnmpAdminString
_CfprExtvmmKeyStoreFsmTaskRn_Object = MibTableColumn
cfprExtvmmKeyStoreFsmTaskRn = _CfprExtvmmKeyStoreFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13, 1, 3),
    _CfprExtvmmKeyStoreFsmTaskRn_Type()
)
cfprExtvmmKeyStoreFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskRn.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtvmmKeyStoreFsmTaskCompletion_Object = MibTableColumn
cfprExtvmmKeyStoreFsmTaskCompletion = _CfprExtvmmKeyStoreFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13, 1, 4),
    _CfprExtvmmKeyStoreFsmTaskCompletion_Type()
)
cfprExtvmmKeyStoreFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskCompletion.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskFlags_Type = CfprFsmFlags
_CfprExtvmmKeyStoreFsmTaskFlags_Object = MibTableColumn
cfprExtvmmKeyStoreFsmTaskFlags = _CfprExtvmmKeyStoreFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13, 1, 5),
    _CfprExtvmmKeyStoreFsmTaskFlags_Type()
)
cfprExtvmmKeyStoreFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskFlags.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskItem_Type = CfprExtvmmKeyStoreFsmTaskItem
_CfprExtvmmKeyStoreFsmTaskItem_Object = MibTableColumn
cfprExtvmmKeyStoreFsmTaskItem = _CfprExtvmmKeyStoreFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13, 1, 6),
    _CfprExtvmmKeyStoreFsmTaskItem_Type()
)
cfprExtvmmKeyStoreFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskItem.setStatus("current")
_CfprExtvmmKeyStoreFsmTaskSeqId_Type = Gauge32
_CfprExtvmmKeyStoreFsmTaskSeqId_Object = MibTableColumn
cfprExtvmmKeyStoreFsmTaskSeqId = _CfprExtvmmKeyStoreFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 13, 1, 7),
    _CfprExtvmmKeyStoreFsmTaskSeqId_Type()
)
cfprExtvmmKeyStoreFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmKeyStoreFsmTaskSeqId.setStatus("current")
_CfprExtvmmMasterExtKeyTable_Object = MibTable
cfprExtvmmMasterExtKeyTable = _CfprExtvmmMasterExtKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14)
)
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyTable.setStatus("current")
_CfprExtvmmMasterExtKeyEntry_Object = MibTableRow
cfprExtvmmMasterExtKeyEntry = _CfprExtvmmMasterExtKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1)
)
cfprExtvmmMasterExtKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmMasterExtKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyEntry.setStatus("current")
_CfprExtvmmMasterExtKeyInstanceId_Type = CfprManagedObjectId
_CfprExtvmmMasterExtKeyInstanceId_Object = MibTableColumn
cfprExtvmmMasterExtKeyInstanceId = _CfprExtvmmMasterExtKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 1),
    _CfprExtvmmMasterExtKeyInstanceId_Type()
)
cfprExtvmmMasterExtKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyInstanceId.setStatus("current")
_CfprExtvmmMasterExtKeyDn_Type = CfprManagedObjectDn
_CfprExtvmmMasterExtKeyDn_Object = MibTableColumn
cfprExtvmmMasterExtKeyDn = _CfprExtvmmMasterExtKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 2),
    _CfprExtvmmMasterExtKeyDn_Type()
)
cfprExtvmmMasterExtKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyDn.setStatus("current")
_CfprExtvmmMasterExtKeyRn_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyRn_Object = MibTableColumn
cfprExtvmmMasterExtKeyRn = _CfprExtvmmMasterExtKeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 3),
    _CfprExtvmmMasterExtKeyRn_Type()
)
cfprExtvmmMasterExtKeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyRn.setStatus("current")
_CfprExtvmmMasterExtKeyFsmDescr_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmDescr_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmDescr = _CfprExtvmmMasterExtKeyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 4),
    _CfprExtvmmMasterExtKeyFsmDescr_Type()
)
cfprExtvmmMasterExtKeyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmDescr.setStatus("current")
_CfprExtvmmMasterExtKeyFsmPrev_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmPrev_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmPrev = _CfprExtvmmMasterExtKeyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 5),
    _CfprExtvmmMasterExtKeyFsmPrev_Type()
)
cfprExtvmmMasterExtKeyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmPrev.setStatus("current")
_CfprExtvmmMasterExtKeyFsmProgr_Type = Gauge32
_CfprExtvmmMasterExtKeyFsmProgr_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmProgr = _CfprExtvmmMasterExtKeyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 6),
    _CfprExtvmmMasterExtKeyFsmProgr_Type()
)
cfprExtvmmMasterExtKeyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmProgr.setStatus("current")
_CfprExtvmmMasterExtKeyFsmRmtInvErrCode_Type = Gauge32
_CfprExtvmmMasterExtKeyFsmRmtInvErrCode_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmRmtInvErrCode = _CfprExtvmmMasterExtKeyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 7),
    _CfprExtvmmMasterExtKeyFsmRmtInvErrCode_Type()
)
cfprExtvmmMasterExtKeyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmRmtInvErrCode.setStatus("current")
_CfprExtvmmMasterExtKeyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmRmtInvErrDescr = _CfprExtvmmMasterExtKeyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 8),
    _CfprExtvmmMasterExtKeyFsmRmtInvErrDescr_Type()
)
cfprExtvmmMasterExtKeyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmRmtInvErrDescr.setStatus("current")
_CfprExtvmmMasterExtKeyFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmMasterExtKeyFsmRmtInvRslt_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmRmtInvRslt = _CfprExtvmmMasterExtKeyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 9),
    _CfprExtvmmMasterExtKeyFsmRmtInvRslt_Type()
)
cfprExtvmmMasterExtKeyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmRmtInvRslt.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageDescr_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmStageDescr_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageDescr = _CfprExtvmmMasterExtKeyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 10),
    _CfprExtvmmMasterExtKeyFsmStageDescr_Type()
)
cfprExtvmmMasterExtKeyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageDescr.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStamp_Type = DateAndTime
_CfprExtvmmMasterExtKeyFsmStamp_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStamp = _CfprExtvmmMasterExtKeyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 11),
    _CfprExtvmmMasterExtKeyFsmStamp_Type()
)
cfprExtvmmMasterExtKeyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStamp.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStatus_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmStatus_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStatus = _CfprExtvmmMasterExtKeyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 12),
    _CfprExtvmmMasterExtKeyFsmStatus_Type()
)
cfprExtvmmMasterExtKeyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStatus.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTry_Type = Gauge32
_CfprExtvmmMasterExtKeyFsmTry_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmTry = _CfprExtvmmMasterExtKeyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 13),
    _CfprExtvmmMasterExtKeyFsmTry_Type()
)
cfprExtvmmMasterExtKeyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTry.setStatus("current")
_CfprExtvmmMasterExtKeyKey_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyKey_Object = MibTableColumn
cfprExtvmmMasterExtKeyKey = _CfprExtvmmMasterExtKeyKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 14, 1, 14),
    _CfprExtvmmMasterExtKeyKey_Type()
)
cfprExtvmmMasterExtKeyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyKey.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTable_Object = MibTable
cfprExtvmmMasterExtKeyFsmTable = _CfprExtvmmMasterExtKeyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15)
)
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTable.setStatus("current")
_CfprExtvmmMasterExtKeyFsmEntry_Object = MibTableRow
cfprExtvmmMasterExtKeyFsmEntry = _CfprExtvmmMasterExtKeyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1)
)
cfprExtvmmMasterExtKeyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmMasterExtKeyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmEntry.setStatus("current")
_CfprExtvmmMasterExtKeyFsmInstanceId_Type = CfprManagedObjectId
_CfprExtvmmMasterExtKeyFsmInstanceId_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmInstanceId = _CfprExtvmmMasterExtKeyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 1),
    _CfprExtvmmMasterExtKeyFsmInstanceId_Type()
)
cfprExtvmmMasterExtKeyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmInstanceId.setStatus("current")
_CfprExtvmmMasterExtKeyFsmDn_Type = CfprManagedObjectDn
_CfprExtvmmMasterExtKeyFsmDn_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmDn = _CfprExtvmmMasterExtKeyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 2),
    _CfprExtvmmMasterExtKeyFsmDn_Type()
)
cfprExtvmmMasterExtKeyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmDn.setStatus("current")
_CfprExtvmmMasterExtKeyFsmRn_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmRn_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmRn = _CfprExtvmmMasterExtKeyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 3),
    _CfprExtvmmMasterExtKeyFsmRn_Type()
)
cfprExtvmmMasterExtKeyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmRn.setStatus("current")
_CfprExtvmmMasterExtKeyFsmCompletionTime_Type = DateAndTime
_CfprExtvmmMasterExtKeyFsmCompletionTime_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmCompletionTime = _CfprExtvmmMasterExtKeyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 4),
    _CfprExtvmmMasterExtKeyFsmCompletionTime_Type()
)
cfprExtvmmMasterExtKeyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmCompletionTime.setStatus("current")
_CfprExtvmmMasterExtKeyFsmCurrentFsm_Type = CfprExtvmmMasterExtKeyFsmCurrentFsm
_CfprExtvmmMasterExtKeyFsmCurrentFsm_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmCurrentFsm = _CfprExtvmmMasterExtKeyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 5),
    _CfprExtvmmMasterExtKeyFsmCurrentFsm_Type()
)
cfprExtvmmMasterExtKeyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmCurrentFsm.setStatus("current")
_CfprExtvmmMasterExtKeyFsmDescrData_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmDescrData_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmDescrData = _CfprExtvmmMasterExtKeyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 6),
    _CfprExtvmmMasterExtKeyFsmDescrData_Type()
)
cfprExtvmmMasterExtKeyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmDescrData.setStatus("current")
_CfprExtvmmMasterExtKeyFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmMasterExtKeyFsmFsmStatus_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmFsmStatus = _CfprExtvmmMasterExtKeyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 7),
    _CfprExtvmmMasterExtKeyFsmFsmStatus_Type()
)
cfprExtvmmMasterExtKeyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmFsmStatus.setStatus("current")
_CfprExtvmmMasterExtKeyFsmProgress_Type = Gauge32
_CfprExtvmmMasterExtKeyFsmProgress_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmProgress = _CfprExtvmmMasterExtKeyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 8),
    _CfprExtvmmMasterExtKeyFsmProgress_Type()
)
cfprExtvmmMasterExtKeyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmProgress.setStatus("current")
_CfprExtvmmMasterExtKeyFsmRmtErrCode_Type = Gauge32
_CfprExtvmmMasterExtKeyFsmRmtErrCode_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmRmtErrCode = _CfprExtvmmMasterExtKeyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 9),
    _CfprExtvmmMasterExtKeyFsmRmtErrCode_Type()
)
cfprExtvmmMasterExtKeyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmRmtErrCode.setStatus("current")
_CfprExtvmmMasterExtKeyFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmRmtErrDescr_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmRmtErrDescr = _CfprExtvmmMasterExtKeyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 10),
    _CfprExtvmmMasterExtKeyFsmRmtErrDescr_Type()
)
cfprExtvmmMasterExtKeyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmRmtErrDescr.setStatus("current")
_CfprExtvmmMasterExtKeyFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmMasterExtKeyFsmRmtRslt_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmRmtRslt = _CfprExtvmmMasterExtKeyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 15, 1, 11),
    _CfprExtvmmMasterExtKeyFsmRmtRslt_Type()
)
cfprExtvmmMasterExtKeyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmRmtRslt.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageTable_Object = MibTable
cfprExtvmmMasterExtKeyFsmStageTable = _CfprExtvmmMasterExtKeyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16)
)
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageTable.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageEntry_Object = MibTableRow
cfprExtvmmMasterExtKeyFsmStageEntry = _CfprExtvmmMasterExtKeyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1)
)
cfprExtvmmMasterExtKeyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmMasterExtKeyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageEntry.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtvmmMasterExtKeyFsmStageInstanceId_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageInstanceId = _CfprExtvmmMasterExtKeyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 1),
    _CfprExtvmmMasterExtKeyFsmStageInstanceId_Type()
)
cfprExtvmmMasterExtKeyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageInstanceId.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageDn_Type = CfprManagedObjectDn
_CfprExtvmmMasterExtKeyFsmStageDn_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageDn = _CfprExtvmmMasterExtKeyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 2),
    _CfprExtvmmMasterExtKeyFsmStageDn_Type()
)
cfprExtvmmMasterExtKeyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageDn.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageRn_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmStageRn_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageRn = _CfprExtvmmMasterExtKeyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 3),
    _CfprExtvmmMasterExtKeyFsmStageRn_Type()
)
cfprExtvmmMasterExtKeyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageRn.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageDescrData_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmStageDescrData_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageDescrData = _CfprExtvmmMasterExtKeyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 4),
    _CfprExtvmmMasterExtKeyFsmStageDescrData_Type()
)
cfprExtvmmMasterExtKeyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageDescrData.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtvmmMasterExtKeyFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageLastUpdateTime = _CfprExtvmmMasterExtKeyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 5),
    _CfprExtvmmMasterExtKeyFsmStageLastUpdateTime_Type()
)
cfprExtvmmMasterExtKeyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageLastUpdateTime.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageName_Type = CfprExtvmmMasterExtKeyFsmStageName
_CfprExtvmmMasterExtKeyFsmStageName_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageName = _CfprExtvmmMasterExtKeyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 6),
    _CfprExtvmmMasterExtKeyFsmStageName_Type()
)
cfprExtvmmMasterExtKeyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageName.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageOrder_Type = Gauge32
_CfprExtvmmMasterExtKeyFsmStageOrder_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageOrder = _CfprExtvmmMasterExtKeyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 7),
    _CfprExtvmmMasterExtKeyFsmStageOrder_Type()
)
cfprExtvmmMasterExtKeyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageOrder.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageRetry_Type = Gauge32
_CfprExtvmmMasterExtKeyFsmStageRetry_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageRetry = _CfprExtvmmMasterExtKeyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 8),
    _CfprExtvmmMasterExtKeyFsmStageRetry_Type()
)
cfprExtvmmMasterExtKeyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageRetry.setStatus("current")
_CfprExtvmmMasterExtKeyFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmMasterExtKeyFsmStageStageStatus_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmStageStageStatus = _CfprExtvmmMasterExtKeyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 16, 1, 9),
    _CfprExtvmmMasterExtKeyFsmStageStageStatus_Type()
)
cfprExtvmmMasterExtKeyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmStageStageStatus.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskTable_Object = MibTable
cfprExtvmmMasterExtKeyFsmTaskTable = _CfprExtvmmMasterExtKeyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17)
)
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskTable.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskEntry_Object = MibTableRow
cfprExtvmmMasterExtKeyFsmTaskEntry = _CfprExtvmmMasterExtKeyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17, 1)
)
cfprExtvmmMasterExtKeyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmMasterExtKeyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskEntry.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtvmmMasterExtKeyFsmTaskInstanceId_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmTaskInstanceId = _CfprExtvmmMasterExtKeyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17, 1, 1),
    _CfprExtvmmMasterExtKeyFsmTaskInstanceId_Type()
)
cfprExtvmmMasterExtKeyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskInstanceId.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtvmmMasterExtKeyFsmTaskDn_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmTaskDn = _CfprExtvmmMasterExtKeyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17, 1, 2),
    _CfprExtvmmMasterExtKeyFsmTaskDn_Type()
)
cfprExtvmmMasterExtKeyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskDn.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskRn_Type = SnmpAdminString
_CfprExtvmmMasterExtKeyFsmTaskRn_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmTaskRn = _CfprExtvmmMasterExtKeyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17, 1, 3),
    _CfprExtvmmMasterExtKeyFsmTaskRn_Type()
)
cfprExtvmmMasterExtKeyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskRn.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtvmmMasterExtKeyFsmTaskCompletion_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmTaskCompletion = _CfprExtvmmMasterExtKeyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17, 1, 4),
    _CfprExtvmmMasterExtKeyFsmTaskCompletion_Type()
)
cfprExtvmmMasterExtKeyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskCompletion.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskFlags_Type = CfprFsmFlags
_CfprExtvmmMasterExtKeyFsmTaskFlags_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmTaskFlags = _CfprExtvmmMasterExtKeyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17, 1, 5),
    _CfprExtvmmMasterExtKeyFsmTaskFlags_Type()
)
cfprExtvmmMasterExtKeyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskFlags.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskItem_Type = CfprExtvmmMasterExtKeyFsmTaskItem
_CfprExtvmmMasterExtKeyFsmTaskItem_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmTaskItem = _CfprExtvmmMasterExtKeyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17, 1, 6),
    _CfprExtvmmMasterExtKeyFsmTaskItem_Type()
)
cfprExtvmmMasterExtKeyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskItem.setStatus("current")
_CfprExtvmmMasterExtKeyFsmTaskSeqId_Type = Gauge32
_CfprExtvmmMasterExtKeyFsmTaskSeqId_Object = MibTableColumn
cfprExtvmmMasterExtKeyFsmTaskSeqId = _CfprExtvmmMasterExtKeyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 17, 1, 7),
    _CfprExtvmmMasterExtKeyFsmTaskSeqId_Type()
)
cfprExtvmmMasterExtKeyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmMasterExtKeyFsmTaskSeqId.setStatus("current")
_CfprExtvmmNetworkSetsTable_Object = MibTable
cfprExtvmmNetworkSetsTable = _CfprExtvmmNetworkSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18)
)
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsTable.setStatus("current")
_CfprExtvmmNetworkSetsEntry_Object = MibTableRow
cfprExtvmmNetworkSetsEntry = _CfprExtvmmNetworkSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1)
)
cfprExtvmmNetworkSetsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmNetworkSetsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsEntry.setStatus("current")
_CfprExtvmmNetworkSetsInstanceId_Type = CfprManagedObjectId
_CfprExtvmmNetworkSetsInstanceId_Object = MibTableColumn
cfprExtvmmNetworkSetsInstanceId = _CfprExtvmmNetworkSetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 1),
    _CfprExtvmmNetworkSetsInstanceId_Type()
)
cfprExtvmmNetworkSetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsInstanceId.setStatus("current")
_CfprExtvmmNetworkSetsDn_Type = CfprManagedObjectDn
_CfprExtvmmNetworkSetsDn_Object = MibTableColumn
cfprExtvmmNetworkSetsDn = _CfprExtvmmNetworkSetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 2),
    _CfprExtvmmNetworkSetsDn_Type()
)
cfprExtvmmNetworkSetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsDn.setStatus("current")
_CfprExtvmmNetworkSetsRn_Type = SnmpAdminString
_CfprExtvmmNetworkSetsRn_Object = MibTableColumn
cfprExtvmmNetworkSetsRn = _CfprExtvmmNetworkSetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 3),
    _CfprExtvmmNetworkSetsRn_Type()
)
cfprExtvmmNetworkSetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsRn.setStatus("current")
_CfprExtvmmNetworkSetsFltAggr_Type = Unsigned64
_CfprExtvmmNetworkSetsFltAggr_Object = MibTableColumn
cfprExtvmmNetworkSetsFltAggr = _CfprExtvmmNetworkSetsFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 4),
    _CfprExtvmmNetworkSetsFltAggr_Type()
)
cfprExtvmmNetworkSetsFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFltAggr.setStatus("current")
_CfprExtvmmNetworkSetsFsmDescr_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmDescr_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmDescr = _CfprExtvmmNetworkSetsFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 5),
    _CfprExtvmmNetworkSetsFsmDescr_Type()
)
cfprExtvmmNetworkSetsFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmDescr.setStatus("current")
_CfprExtvmmNetworkSetsFsmPrev_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmPrev_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmPrev = _CfprExtvmmNetworkSetsFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 6),
    _CfprExtvmmNetworkSetsFsmPrev_Type()
)
cfprExtvmmNetworkSetsFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmPrev.setStatus("current")
_CfprExtvmmNetworkSetsFsmProgr_Type = Gauge32
_CfprExtvmmNetworkSetsFsmProgr_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmProgr = _CfprExtvmmNetworkSetsFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 7),
    _CfprExtvmmNetworkSetsFsmProgr_Type()
)
cfprExtvmmNetworkSetsFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmProgr.setStatus("current")
_CfprExtvmmNetworkSetsFsmRmtInvErrCode_Type = Gauge32
_CfprExtvmmNetworkSetsFsmRmtInvErrCode_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmRmtInvErrCode = _CfprExtvmmNetworkSetsFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 8),
    _CfprExtvmmNetworkSetsFsmRmtInvErrCode_Type()
)
cfprExtvmmNetworkSetsFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmRmtInvErrCode.setStatus("current")
_CfprExtvmmNetworkSetsFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmRmtInvErrDescr = _CfprExtvmmNetworkSetsFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 9),
    _CfprExtvmmNetworkSetsFsmRmtInvErrDescr_Type()
)
cfprExtvmmNetworkSetsFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmRmtInvErrDescr.setStatus("current")
_CfprExtvmmNetworkSetsFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmNetworkSetsFsmRmtInvRslt_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmRmtInvRslt = _CfprExtvmmNetworkSetsFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 10),
    _CfprExtvmmNetworkSetsFsmRmtInvRslt_Type()
)
cfprExtvmmNetworkSetsFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmRmtInvRslt.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageDescr_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmStageDescr_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageDescr = _CfprExtvmmNetworkSetsFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 11),
    _CfprExtvmmNetworkSetsFsmStageDescr_Type()
)
cfprExtvmmNetworkSetsFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageDescr.setStatus("current")
_CfprExtvmmNetworkSetsFsmStamp_Type = DateAndTime
_CfprExtvmmNetworkSetsFsmStamp_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStamp = _CfprExtvmmNetworkSetsFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 12),
    _CfprExtvmmNetworkSetsFsmStamp_Type()
)
cfprExtvmmNetworkSetsFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStamp.setStatus("current")
_CfprExtvmmNetworkSetsFsmStatus_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmStatus_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStatus = _CfprExtvmmNetworkSetsFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 13),
    _CfprExtvmmNetworkSetsFsmStatus_Type()
)
cfprExtvmmNetworkSetsFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStatus.setStatus("current")
_CfprExtvmmNetworkSetsFsmTry_Type = Gauge32
_CfprExtvmmNetworkSetsFsmTry_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmTry = _CfprExtvmmNetworkSetsFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 14),
    _CfprExtvmmNetworkSetsFsmTry_Type()
)
cfprExtvmmNetworkSetsFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTry.setStatus("current")
_CfprExtvmmNetworkSetsGenNum_Type = Gauge32
_CfprExtvmmNetworkSetsGenNum_Object = MibTableColumn
cfprExtvmmNetworkSetsGenNum = _CfprExtvmmNetworkSetsGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 18, 1, 15),
    _CfprExtvmmNetworkSetsGenNum_Type()
)
cfprExtvmmNetworkSetsGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsGenNum.setStatus("current")
_CfprExtvmmNetworkSetsFsmTable_Object = MibTable
cfprExtvmmNetworkSetsFsmTable = _CfprExtvmmNetworkSetsFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19)
)
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTable.setStatus("current")
_CfprExtvmmNetworkSetsFsmEntry_Object = MibTableRow
cfprExtvmmNetworkSetsFsmEntry = _CfprExtvmmNetworkSetsFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1)
)
cfprExtvmmNetworkSetsFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmNetworkSetsFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmEntry.setStatus("current")
_CfprExtvmmNetworkSetsFsmInstanceId_Type = CfprManagedObjectId
_CfprExtvmmNetworkSetsFsmInstanceId_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmInstanceId = _CfprExtvmmNetworkSetsFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 1),
    _CfprExtvmmNetworkSetsFsmInstanceId_Type()
)
cfprExtvmmNetworkSetsFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmInstanceId.setStatus("current")
_CfprExtvmmNetworkSetsFsmDn_Type = CfprManagedObjectDn
_CfprExtvmmNetworkSetsFsmDn_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmDn = _CfprExtvmmNetworkSetsFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 2),
    _CfprExtvmmNetworkSetsFsmDn_Type()
)
cfprExtvmmNetworkSetsFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmDn.setStatus("current")
_CfprExtvmmNetworkSetsFsmRn_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmRn_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmRn = _CfprExtvmmNetworkSetsFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 3),
    _CfprExtvmmNetworkSetsFsmRn_Type()
)
cfprExtvmmNetworkSetsFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmRn.setStatus("current")
_CfprExtvmmNetworkSetsFsmCompletionTime_Type = DateAndTime
_CfprExtvmmNetworkSetsFsmCompletionTime_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmCompletionTime = _CfprExtvmmNetworkSetsFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 4),
    _CfprExtvmmNetworkSetsFsmCompletionTime_Type()
)
cfprExtvmmNetworkSetsFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmCompletionTime.setStatus("current")
_CfprExtvmmNetworkSetsFsmCurrentFsm_Type = CfprExtvmmNetworkSetsFsmCurrentFsm
_CfprExtvmmNetworkSetsFsmCurrentFsm_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmCurrentFsm = _CfprExtvmmNetworkSetsFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 5),
    _CfprExtvmmNetworkSetsFsmCurrentFsm_Type()
)
cfprExtvmmNetworkSetsFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmCurrentFsm.setStatus("current")
_CfprExtvmmNetworkSetsFsmDescrData_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmDescrData_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmDescrData = _CfprExtvmmNetworkSetsFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 6),
    _CfprExtvmmNetworkSetsFsmDescrData_Type()
)
cfprExtvmmNetworkSetsFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmDescrData.setStatus("current")
_CfprExtvmmNetworkSetsFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmNetworkSetsFsmFsmStatus_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmFsmStatus = _CfprExtvmmNetworkSetsFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 7),
    _CfprExtvmmNetworkSetsFsmFsmStatus_Type()
)
cfprExtvmmNetworkSetsFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmFsmStatus.setStatus("current")
_CfprExtvmmNetworkSetsFsmProgress_Type = Gauge32
_CfprExtvmmNetworkSetsFsmProgress_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmProgress = _CfprExtvmmNetworkSetsFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 8),
    _CfprExtvmmNetworkSetsFsmProgress_Type()
)
cfprExtvmmNetworkSetsFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmProgress.setStatus("current")
_CfprExtvmmNetworkSetsFsmRmtErrCode_Type = Gauge32
_CfprExtvmmNetworkSetsFsmRmtErrCode_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmRmtErrCode = _CfprExtvmmNetworkSetsFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 9),
    _CfprExtvmmNetworkSetsFsmRmtErrCode_Type()
)
cfprExtvmmNetworkSetsFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmRmtErrCode.setStatus("current")
_CfprExtvmmNetworkSetsFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmRmtErrDescr_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmRmtErrDescr = _CfprExtvmmNetworkSetsFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 10),
    _CfprExtvmmNetworkSetsFsmRmtErrDescr_Type()
)
cfprExtvmmNetworkSetsFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmRmtErrDescr.setStatus("current")
_CfprExtvmmNetworkSetsFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmNetworkSetsFsmRmtRslt_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmRmtRslt = _CfprExtvmmNetworkSetsFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 19, 1, 11),
    _CfprExtvmmNetworkSetsFsmRmtRslt_Type()
)
cfprExtvmmNetworkSetsFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmRmtRslt.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageTable_Object = MibTable
cfprExtvmmNetworkSetsFsmStageTable = _CfprExtvmmNetworkSetsFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20)
)
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageTable.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageEntry_Object = MibTableRow
cfprExtvmmNetworkSetsFsmStageEntry = _CfprExtvmmNetworkSetsFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1)
)
cfprExtvmmNetworkSetsFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmNetworkSetsFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageEntry.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtvmmNetworkSetsFsmStageInstanceId_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageInstanceId = _CfprExtvmmNetworkSetsFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 1),
    _CfprExtvmmNetworkSetsFsmStageInstanceId_Type()
)
cfprExtvmmNetworkSetsFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageInstanceId.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageDn_Type = CfprManagedObjectDn
_CfprExtvmmNetworkSetsFsmStageDn_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageDn = _CfprExtvmmNetworkSetsFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 2),
    _CfprExtvmmNetworkSetsFsmStageDn_Type()
)
cfprExtvmmNetworkSetsFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageDn.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageRn_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmStageRn_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageRn = _CfprExtvmmNetworkSetsFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 3),
    _CfprExtvmmNetworkSetsFsmStageRn_Type()
)
cfprExtvmmNetworkSetsFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageRn.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageDescrData_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmStageDescrData_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageDescrData = _CfprExtvmmNetworkSetsFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 4),
    _CfprExtvmmNetworkSetsFsmStageDescrData_Type()
)
cfprExtvmmNetworkSetsFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageDescrData.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtvmmNetworkSetsFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageLastUpdateTime = _CfprExtvmmNetworkSetsFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 5),
    _CfprExtvmmNetworkSetsFsmStageLastUpdateTime_Type()
)
cfprExtvmmNetworkSetsFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageLastUpdateTime.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageName_Type = CfprExtvmmNetworkSetsFsmStageName
_CfprExtvmmNetworkSetsFsmStageName_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageName = _CfprExtvmmNetworkSetsFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 6),
    _CfprExtvmmNetworkSetsFsmStageName_Type()
)
cfprExtvmmNetworkSetsFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageName.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageOrder_Type = Gauge32
_CfprExtvmmNetworkSetsFsmStageOrder_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageOrder = _CfprExtvmmNetworkSetsFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 7),
    _CfprExtvmmNetworkSetsFsmStageOrder_Type()
)
cfprExtvmmNetworkSetsFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageOrder.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageRetry_Type = Gauge32
_CfprExtvmmNetworkSetsFsmStageRetry_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageRetry = _CfprExtvmmNetworkSetsFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 8),
    _CfprExtvmmNetworkSetsFsmStageRetry_Type()
)
cfprExtvmmNetworkSetsFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageRetry.setStatus("current")
_CfprExtvmmNetworkSetsFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmNetworkSetsFsmStageStageStatus_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmStageStageStatus = _CfprExtvmmNetworkSetsFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 20, 1, 9),
    _CfprExtvmmNetworkSetsFsmStageStageStatus_Type()
)
cfprExtvmmNetworkSetsFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmStageStageStatus.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskTable_Object = MibTable
cfprExtvmmNetworkSetsFsmTaskTable = _CfprExtvmmNetworkSetsFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21)
)
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskTable.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskEntry_Object = MibTableRow
cfprExtvmmNetworkSetsFsmTaskEntry = _CfprExtvmmNetworkSetsFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21, 1)
)
cfprExtvmmNetworkSetsFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmNetworkSetsFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskEntry.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtvmmNetworkSetsFsmTaskInstanceId_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmTaskInstanceId = _CfprExtvmmNetworkSetsFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21, 1, 1),
    _CfprExtvmmNetworkSetsFsmTaskInstanceId_Type()
)
cfprExtvmmNetworkSetsFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskInstanceId.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtvmmNetworkSetsFsmTaskDn_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmTaskDn = _CfprExtvmmNetworkSetsFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21, 1, 2),
    _CfprExtvmmNetworkSetsFsmTaskDn_Type()
)
cfprExtvmmNetworkSetsFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskDn.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskRn_Type = SnmpAdminString
_CfprExtvmmNetworkSetsFsmTaskRn_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmTaskRn = _CfprExtvmmNetworkSetsFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21, 1, 3),
    _CfprExtvmmNetworkSetsFsmTaskRn_Type()
)
cfprExtvmmNetworkSetsFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskRn.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtvmmNetworkSetsFsmTaskCompletion_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmTaskCompletion = _CfprExtvmmNetworkSetsFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21, 1, 4),
    _CfprExtvmmNetworkSetsFsmTaskCompletion_Type()
)
cfprExtvmmNetworkSetsFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskCompletion.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskFlags_Type = CfprFsmFlags
_CfprExtvmmNetworkSetsFsmTaskFlags_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmTaskFlags = _CfprExtvmmNetworkSetsFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21, 1, 5),
    _CfprExtvmmNetworkSetsFsmTaskFlags_Type()
)
cfprExtvmmNetworkSetsFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskFlags.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskItem_Type = CfprExtvmmNetworkSetsFsmTaskItem
_CfprExtvmmNetworkSetsFsmTaskItem_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmTaskItem = _CfprExtvmmNetworkSetsFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21, 1, 6),
    _CfprExtvmmNetworkSetsFsmTaskItem_Type()
)
cfprExtvmmNetworkSetsFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskItem.setStatus("current")
_CfprExtvmmNetworkSetsFsmTaskSeqId_Type = Gauge32
_CfprExtvmmNetworkSetsFsmTaskSeqId_Object = MibTableColumn
cfprExtvmmNetworkSetsFsmTaskSeqId = _CfprExtvmmNetworkSetsFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 21, 1, 7),
    _CfprExtvmmNetworkSetsFsmTaskSeqId_Type()
)
cfprExtvmmNetworkSetsFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmNetworkSetsFsmTaskSeqId.setStatus("current")
_CfprExtvmmProviderTable_Object = MibTable
cfprExtvmmProviderTable = _CfprExtvmmProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22)
)
if mibBuilder.loadTexts:
    cfprExtvmmProviderTable.setStatus("current")
_CfprExtvmmProviderEntry_Object = MibTableRow
cfprExtvmmProviderEntry = _CfprExtvmmProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1)
)
cfprExtvmmProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmProviderEntry.setStatus("current")
_CfprExtvmmProviderInstanceId_Type = CfprManagedObjectId
_CfprExtvmmProviderInstanceId_Object = MibTableColumn
cfprExtvmmProviderInstanceId = _CfprExtvmmProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 1),
    _CfprExtvmmProviderInstanceId_Type()
)
cfprExtvmmProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmProviderInstanceId.setStatus("current")
_CfprExtvmmProviderDn_Type = CfprManagedObjectDn
_CfprExtvmmProviderDn_Object = MibTableColumn
cfprExtvmmProviderDn = _CfprExtvmmProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 2),
    _CfprExtvmmProviderDn_Type()
)
cfprExtvmmProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderDn.setStatus("current")
_CfprExtvmmProviderRn_Type = SnmpAdminString
_CfprExtvmmProviderRn_Object = MibTableColumn
cfprExtvmmProviderRn = _CfprExtvmmProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 3),
    _CfprExtvmmProviderRn_Type()
)
cfprExtvmmProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderRn.setStatus("current")
_CfprExtvmmProviderCert_Type = SnmpAdminString
_CfprExtvmmProviderCert_Object = MibTableColumn
cfprExtvmmProviderCert = _CfprExtvmmProviderCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 4),
    _CfprExtvmmProviderCert_Type()
)
cfprExtvmmProviderCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderCert.setStatus("current")
_CfprExtvmmProviderDescr_Type = SnmpAdminString
_CfprExtvmmProviderDescr_Object = MibTableColumn
cfprExtvmmProviderDescr = _CfprExtvmmProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 5),
    _CfprExtvmmProviderDescr_Type()
)
cfprExtvmmProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderDescr.setStatus("current")
_CfprExtvmmProviderFsmDescr_Type = SnmpAdminString
_CfprExtvmmProviderFsmDescr_Object = MibTableColumn
cfprExtvmmProviderFsmDescr = _CfprExtvmmProviderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 6),
    _CfprExtvmmProviderFsmDescr_Type()
)
cfprExtvmmProviderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmDescr.setStatus("current")
_CfprExtvmmProviderFsmPrev_Type = SnmpAdminString
_CfprExtvmmProviderFsmPrev_Object = MibTableColumn
cfprExtvmmProviderFsmPrev = _CfprExtvmmProviderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 7),
    _CfprExtvmmProviderFsmPrev_Type()
)
cfprExtvmmProviderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmPrev.setStatus("current")
_CfprExtvmmProviderFsmProgr_Type = Gauge32
_CfprExtvmmProviderFsmProgr_Object = MibTableColumn
cfprExtvmmProviderFsmProgr = _CfprExtvmmProviderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 8),
    _CfprExtvmmProviderFsmProgr_Type()
)
cfprExtvmmProviderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmProgr.setStatus("current")
_CfprExtvmmProviderFsmRmtInvErrCode_Type = Gauge32
_CfprExtvmmProviderFsmRmtInvErrCode_Object = MibTableColumn
cfprExtvmmProviderFsmRmtInvErrCode = _CfprExtvmmProviderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 9),
    _CfprExtvmmProviderFsmRmtInvErrCode_Type()
)
cfprExtvmmProviderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmRmtInvErrCode.setStatus("current")
_CfprExtvmmProviderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtvmmProviderFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtvmmProviderFsmRmtInvErrDescr = _CfprExtvmmProviderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 10),
    _CfprExtvmmProviderFsmRmtInvErrDescr_Type()
)
cfprExtvmmProviderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmRmtInvErrDescr.setStatus("current")
_CfprExtvmmProviderFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmProviderFsmRmtInvRslt_Object = MibTableColumn
cfprExtvmmProviderFsmRmtInvRslt = _CfprExtvmmProviderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 11),
    _CfprExtvmmProviderFsmRmtInvRslt_Type()
)
cfprExtvmmProviderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmRmtInvRslt.setStatus("current")
_CfprExtvmmProviderFsmStageDescr_Type = SnmpAdminString
_CfprExtvmmProviderFsmStageDescr_Object = MibTableColumn
cfprExtvmmProviderFsmStageDescr = _CfprExtvmmProviderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 12),
    _CfprExtvmmProviderFsmStageDescr_Type()
)
cfprExtvmmProviderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageDescr.setStatus("current")
_CfprExtvmmProviderFsmStamp_Type = DateAndTime
_CfprExtvmmProviderFsmStamp_Object = MibTableColumn
cfprExtvmmProviderFsmStamp = _CfprExtvmmProviderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 13),
    _CfprExtvmmProviderFsmStamp_Type()
)
cfprExtvmmProviderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStamp.setStatus("current")
_CfprExtvmmProviderFsmStatus_Type = SnmpAdminString
_CfprExtvmmProviderFsmStatus_Object = MibTableColumn
cfprExtvmmProviderFsmStatus = _CfprExtvmmProviderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 14),
    _CfprExtvmmProviderFsmStatus_Type()
)
cfprExtvmmProviderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStatus.setStatus("current")
_CfprExtvmmProviderFsmTry_Type = Gauge32
_CfprExtvmmProviderFsmTry_Object = MibTableColumn
cfprExtvmmProviderFsmTry = _CfprExtvmmProviderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 15),
    _CfprExtvmmProviderFsmTry_Type()
)
cfprExtvmmProviderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTry.setStatus("current")
_CfprExtvmmProviderHost_Type = SnmpAdminString
_CfprExtvmmProviderHost_Object = MibTableColumn
cfprExtvmmProviderHost = _CfprExtvmmProviderHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 16),
    _CfprExtvmmProviderHost_Type()
)
cfprExtvmmProviderHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderHost.setStatus("current")
_CfprExtvmmProviderIntId_Type = SnmpAdminString
_CfprExtvmmProviderIntId_Object = MibTableColumn
cfprExtvmmProviderIntId = _CfprExtvmmProviderIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 17),
    _CfprExtvmmProviderIntId_Type()
)
cfprExtvmmProviderIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderIntId.setStatus("current")
_CfprExtvmmProviderKey_Type = SnmpAdminString
_CfprExtvmmProviderKey_Object = MibTableColumn
cfprExtvmmProviderKey = _CfprExtvmmProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 18),
    _CfprExtvmmProviderKey_Type()
)
cfprExtvmmProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderKey.setStatus("current")
_CfprExtvmmProviderName_Type = SnmpAdminString
_CfprExtvmmProviderName_Object = MibTableColumn
cfprExtvmmProviderName = _CfprExtvmmProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 19),
    _CfprExtvmmProviderName_Type()
)
cfprExtvmmProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderName.setStatus("current")
_CfprExtvmmProviderPolicyLevel_Type = Gauge32
_CfprExtvmmProviderPolicyLevel_Object = MibTableColumn
cfprExtvmmProviderPolicyLevel = _CfprExtvmmProviderPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 20),
    _CfprExtvmmProviderPolicyLevel_Type()
)
cfprExtvmmProviderPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderPolicyLevel.setStatus("current")
_CfprExtvmmProviderPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmProviderPolicyOwner_Object = MibTableColumn
cfprExtvmmProviderPolicyOwner = _CfprExtvmmProviderPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 21),
    _CfprExtvmmProviderPolicyOwner_Type()
)
cfprExtvmmProviderPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderPolicyOwner.setStatus("current")
_CfprExtvmmProviderPortValue_Type = Gauge32
_CfprExtvmmProviderPortValue_Object = MibTableColumn
cfprExtvmmProviderPortValue = _CfprExtvmmProviderPortValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 22),
    _CfprExtvmmProviderPortValue_Type()
)
cfprExtvmmProviderPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderPortValue.setStatus("current")
_CfprExtvmmProviderUuid_Type = SnmpAdminString
_CfprExtvmmProviderUuid_Object = MibTableColumn
cfprExtvmmProviderUuid = _CfprExtvmmProviderUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 23),
    _CfprExtvmmProviderUuid_Type()
)
cfprExtvmmProviderUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderUuid.setStatus("current")
_CfprExtvmmProviderVendorType_Type = CfprExtvmmProviderVendorType
_CfprExtvmmProviderVendorType_Object = MibTableColumn
cfprExtvmmProviderVendorType = _CfprExtvmmProviderVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 24),
    _CfprExtvmmProviderVendorType_Type()
)
cfprExtvmmProviderVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderVendorType.setStatus("current")
_CfprExtvmmProviderVer_Type = CfprExtvmmVcVersion
_CfprExtvmmProviderVer_Object = MibTableColumn
cfprExtvmmProviderVer = _CfprExtvmmProviderVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 25),
    _CfprExtvmmProviderVer_Type()
)
cfprExtvmmProviderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderVer.setStatus("current")
_CfprExtvmmProviderVerRaw_Type = SnmpAdminString
_CfprExtvmmProviderVerRaw_Object = MibTableColumn
cfprExtvmmProviderVerRaw = _CfprExtvmmProviderVerRaw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 22, 1, 26),
    _CfprExtvmmProviderVerRaw_Type()
)
cfprExtvmmProviderVerRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderVerRaw.setStatus("current")
_CfprExtvmmProviderFsmTable_Object = MibTable
cfprExtvmmProviderFsmTable = _CfprExtvmmProviderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23)
)
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTable.setStatus("current")
_CfprExtvmmProviderFsmEntry_Object = MibTableRow
cfprExtvmmProviderFsmEntry = _CfprExtvmmProviderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1)
)
cfprExtvmmProviderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmProviderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmEntry.setStatus("current")
_CfprExtvmmProviderFsmInstanceId_Type = CfprManagedObjectId
_CfprExtvmmProviderFsmInstanceId_Object = MibTableColumn
cfprExtvmmProviderFsmInstanceId = _CfprExtvmmProviderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 1),
    _CfprExtvmmProviderFsmInstanceId_Type()
)
cfprExtvmmProviderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmInstanceId.setStatus("current")
_CfprExtvmmProviderFsmDn_Type = CfprManagedObjectDn
_CfprExtvmmProviderFsmDn_Object = MibTableColumn
cfprExtvmmProviderFsmDn = _CfprExtvmmProviderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 2),
    _CfprExtvmmProviderFsmDn_Type()
)
cfprExtvmmProviderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmDn.setStatus("current")
_CfprExtvmmProviderFsmRn_Type = SnmpAdminString
_CfprExtvmmProviderFsmRn_Object = MibTableColumn
cfprExtvmmProviderFsmRn = _CfprExtvmmProviderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 3),
    _CfprExtvmmProviderFsmRn_Type()
)
cfprExtvmmProviderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmRn.setStatus("current")
_CfprExtvmmProviderFsmCompletionTime_Type = DateAndTime
_CfprExtvmmProviderFsmCompletionTime_Object = MibTableColumn
cfprExtvmmProviderFsmCompletionTime = _CfprExtvmmProviderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 4),
    _CfprExtvmmProviderFsmCompletionTime_Type()
)
cfprExtvmmProviderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmCompletionTime.setStatus("current")
_CfprExtvmmProviderFsmCurrentFsm_Type = CfprExtvmmProviderFsmCurrentFsm
_CfprExtvmmProviderFsmCurrentFsm_Object = MibTableColumn
cfprExtvmmProviderFsmCurrentFsm = _CfprExtvmmProviderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 5),
    _CfprExtvmmProviderFsmCurrentFsm_Type()
)
cfprExtvmmProviderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmCurrentFsm.setStatus("current")
_CfprExtvmmProviderFsmDescrData_Type = SnmpAdminString
_CfprExtvmmProviderFsmDescrData_Object = MibTableColumn
cfprExtvmmProviderFsmDescrData = _CfprExtvmmProviderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 6),
    _CfprExtvmmProviderFsmDescrData_Type()
)
cfprExtvmmProviderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmDescrData.setStatus("current")
_CfprExtvmmProviderFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmProviderFsmFsmStatus_Object = MibTableColumn
cfprExtvmmProviderFsmFsmStatus = _CfprExtvmmProviderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 7),
    _CfprExtvmmProviderFsmFsmStatus_Type()
)
cfprExtvmmProviderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmFsmStatus.setStatus("current")
_CfprExtvmmProviderFsmProgress_Type = Gauge32
_CfprExtvmmProviderFsmProgress_Object = MibTableColumn
cfprExtvmmProviderFsmProgress = _CfprExtvmmProviderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 8),
    _CfprExtvmmProviderFsmProgress_Type()
)
cfprExtvmmProviderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmProgress.setStatus("current")
_CfprExtvmmProviderFsmRmtErrCode_Type = Gauge32
_CfprExtvmmProviderFsmRmtErrCode_Object = MibTableColumn
cfprExtvmmProviderFsmRmtErrCode = _CfprExtvmmProviderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 9),
    _CfprExtvmmProviderFsmRmtErrCode_Type()
)
cfprExtvmmProviderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmRmtErrCode.setStatus("current")
_CfprExtvmmProviderFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtvmmProviderFsmRmtErrDescr_Object = MibTableColumn
cfprExtvmmProviderFsmRmtErrDescr = _CfprExtvmmProviderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 10),
    _CfprExtvmmProviderFsmRmtErrDescr_Type()
)
cfprExtvmmProviderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmRmtErrDescr.setStatus("current")
_CfprExtvmmProviderFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmProviderFsmRmtRslt_Object = MibTableColumn
cfprExtvmmProviderFsmRmtRslt = _CfprExtvmmProviderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 23, 1, 11),
    _CfprExtvmmProviderFsmRmtRslt_Type()
)
cfprExtvmmProviderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmRmtRslt.setStatus("current")
_CfprExtvmmProviderFsmStageTable_Object = MibTable
cfprExtvmmProviderFsmStageTable = _CfprExtvmmProviderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24)
)
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageTable.setStatus("current")
_CfprExtvmmProviderFsmStageEntry_Object = MibTableRow
cfprExtvmmProviderFsmStageEntry = _CfprExtvmmProviderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1)
)
cfprExtvmmProviderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmProviderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageEntry.setStatus("current")
_CfprExtvmmProviderFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtvmmProviderFsmStageInstanceId_Object = MibTableColumn
cfprExtvmmProviderFsmStageInstanceId = _CfprExtvmmProviderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 1),
    _CfprExtvmmProviderFsmStageInstanceId_Type()
)
cfprExtvmmProviderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageInstanceId.setStatus("current")
_CfprExtvmmProviderFsmStageDn_Type = CfprManagedObjectDn
_CfprExtvmmProviderFsmStageDn_Object = MibTableColumn
cfprExtvmmProviderFsmStageDn = _CfprExtvmmProviderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 2),
    _CfprExtvmmProviderFsmStageDn_Type()
)
cfprExtvmmProviderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageDn.setStatus("current")
_CfprExtvmmProviderFsmStageRn_Type = SnmpAdminString
_CfprExtvmmProviderFsmStageRn_Object = MibTableColumn
cfprExtvmmProviderFsmStageRn = _CfprExtvmmProviderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 3),
    _CfprExtvmmProviderFsmStageRn_Type()
)
cfprExtvmmProviderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageRn.setStatus("current")
_CfprExtvmmProviderFsmStageDescrData_Type = SnmpAdminString
_CfprExtvmmProviderFsmStageDescrData_Object = MibTableColumn
cfprExtvmmProviderFsmStageDescrData = _CfprExtvmmProviderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 4),
    _CfprExtvmmProviderFsmStageDescrData_Type()
)
cfprExtvmmProviderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageDescrData.setStatus("current")
_CfprExtvmmProviderFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtvmmProviderFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtvmmProviderFsmStageLastUpdateTime = _CfprExtvmmProviderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 5),
    _CfprExtvmmProviderFsmStageLastUpdateTime_Type()
)
cfprExtvmmProviderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageLastUpdateTime.setStatus("current")
_CfprExtvmmProviderFsmStageName_Type = CfprExtvmmProviderFsmStageName
_CfprExtvmmProviderFsmStageName_Object = MibTableColumn
cfprExtvmmProviderFsmStageName = _CfprExtvmmProviderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 6),
    _CfprExtvmmProviderFsmStageName_Type()
)
cfprExtvmmProviderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageName.setStatus("current")
_CfprExtvmmProviderFsmStageOrder_Type = Gauge32
_CfprExtvmmProviderFsmStageOrder_Object = MibTableColumn
cfprExtvmmProviderFsmStageOrder = _CfprExtvmmProviderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 7),
    _CfprExtvmmProviderFsmStageOrder_Type()
)
cfprExtvmmProviderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageOrder.setStatus("current")
_CfprExtvmmProviderFsmStageRetry_Type = Gauge32
_CfprExtvmmProviderFsmStageRetry_Object = MibTableColumn
cfprExtvmmProviderFsmStageRetry = _CfprExtvmmProviderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 8),
    _CfprExtvmmProviderFsmStageRetry_Type()
)
cfprExtvmmProviderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageRetry.setStatus("current")
_CfprExtvmmProviderFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmProviderFsmStageStageStatus_Object = MibTableColumn
cfprExtvmmProviderFsmStageStageStatus = _CfprExtvmmProviderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 24, 1, 9),
    _CfprExtvmmProviderFsmStageStageStatus_Type()
)
cfprExtvmmProviderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmStageStageStatus.setStatus("current")
_CfprExtvmmProviderFsmTaskTable_Object = MibTable
cfprExtvmmProviderFsmTaskTable = _CfprExtvmmProviderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25)
)
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskTable.setStatus("current")
_CfprExtvmmProviderFsmTaskEntry_Object = MibTableRow
cfprExtvmmProviderFsmTaskEntry = _CfprExtvmmProviderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25, 1)
)
cfprExtvmmProviderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmProviderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskEntry.setStatus("current")
_CfprExtvmmProviderFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtvmmProviderFsmTaskInstanceId_Object = MibTableColumn
cfprExtvmmProviderFsmTaskInstanceId = _CfprExtvmmProviderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25, 1, 1),
    _CfprExtvmmProviderFsmTaskInstanceId_Type()
)
cfprExtvmmProviderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskInstanceId.setStatus("current")
_CfprExtvmmProviderFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtvmmProviderFsmTaskDn_Object = MibTableColumn
cfprExtvmmProviderFsmTaskDn = _CfprExtvmmProviderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25, 1, 2),
    _CfprExtvmmProviderFsmTaskDn_Type()
)
cfprExtvmmProviderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskDn.setStatus("current")
_CfprExtvmmProviderFsmTaskRn_Type = SnmpAdminString
_CfprExtvmmProviderFsmTaskRn_Object = MibTableColumn
cfprExtvmmProviderFsmTaskRn = _CfprExtvmmProviderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25, 1, 3),
    _CfprExtvmmProviderFsmTaskRn_Type()
)
cfprExtvmmProviderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskRn.setStatus("current")
_CfprExtvmmProviderFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtvmmProviderFsmTaskCompletion_Object = MibTableColumn
cfprExtvmmProviderFsmTaskCompletion = _CfprExtvmmProviderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25, 1, 4),
    _CfprExtvmmProviderFsmTaskCompletion_Type()
)
cfprExtvmmProviderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskCompletion.setStatus("current")
_CfprExtvmmProviderFsmTaskFlags_Type = CfprFsmFlags
_CfprExtvmmProviderFsmTaskFlags_Object = MibTableColumn
cfprExtvmmProviderFsmTaskFlags = _CfprExtvmmProviderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25, 1, 5),
    _CfprExtvmmProviderFsmTaskFlags_Type()
)
cfprExtvmmProviderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskFlags.setStatus("current")
_CfprExtvmmProviderFsmTaskItem_Type = CfprExtvmmProviderFsmTaskItem
_CfprExtvmmProviderFsmTaskItem_Object = MibTableColumn
cfprExtvmmProviderFsmTaskItem = _CfprExtvmmProviderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25, 1, 6),
    _CfprExtvmmProviderFsmTaskItem_Type()
)
cfprExtvmmProviderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskItem.setStatus("current")
_CfprExtvmmProviderFsmTaskSeqId_Type = Gauge32
_CfprExtvmmProviderFsmTaskSeqId_Object = MibTableColumn
cfprExtvmmProviderFsmTaskSeqId = _CfprExtvmmProviderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 25, 1, 7),
    _CfprExtvmmProviderFsmTaskSeqId_Type()
)
cfprExtvmmProviderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmProviderFsmTaskSeqId.setStatus("current")
_CfprExtvmmSwitchDelTaskTable_Object = MibTable
cfprExtvmmSwitchDelTaskTable = _CfprExtvmmSwitchDelTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26)
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskTable.setStatus("current")
_CfprExtvmmSwitchDelTaskEntry_Object = MibTableRow
cfprExtvmmSwitchDelTaskEntry = _CfprExtvmmSwitchDelTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1)
)
cfprExtvmmSwitchDelTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmSwitchDelTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskEntry.setStatus("current")
_CfprExtvmmSwitchDelTaskInstanceId_Type = CfprManagedObjectId
_CfprExtvmmSwitchDelTaskInstanceId_Object = MibTableColumn
cfprExtvmmSwitchDelTaskInstanceId = _CfprExtvmmSwitchDelTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 1),
    _CfprExtvmmSwitchDelTaskInstanceId_Type()
)
cfprExtvmmSwitchDelTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskInstanceId.setStatus("current")
_CfprExtvmmSwitchDelTaskDn_Type = CfprManagedObjectDn
_CfprExtvmmSwitchDelTaskDn_Object = MibTableColumn
cfprExtvmmSwitchDelTaskDn = _CfprExtvmmSwitchDelTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 2),
    _CfprExtvmmSwitchDelTaskDn_Type()
)
cfprExtvmmSwitchDelTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskDn.setStatus("current")
_CfprExtvmmSwitchDelTaskRn_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskRn_Object = MibTableColumn
cfprExtvmmSwitchDelTaskRn = _CfprExtvmmSwitchDelTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 3),
    _CfprExtvmmSwitchDelTaskRn_Type()
)
cfprExtvmmSwitchDelTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskRn.setStatus("current")
_CfprExtvmmSwitchDelTaskCertFile_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskCertFile_Object = MibTableColumn
cfprExtvmmSwitchDelTaskCertFile = _CfprExtvmmSwitchDelTaskCertFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 4),
    _CfprExtvmmSwitchDelTaskCertFile_Type()
)
cfprExtvmmSwitchDelTaskCertFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskCertFile.setStatus("current")
_CfprExtvmmSwitchDelTaskDcName_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskDcName_Object = MibTableColumn
cfprExtvmmSwitchDelTaskDcName = _CfprExtvmmSwitchDelTaskDcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 5),
    _CfprExtvmmSwitchDelTaskDcName_Type()
)
cfprExtvmmSwitchDelTaskDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskDcName.setStatus("current")
_CfprExtvmmSwitchDelTaskDcOrg_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskDcOrg_Object = MibTableColumn
cfprExtvmmSwitchDelTaskDcOrg = _CfprExtvmmSwitchDelTaskDcOrg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 6),
    _CfprExtvmmSwitchDelTaskDcOrg_Type()
)
cfprExtvmmSwitchDelTaskDcOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskDcOrg.setStatus("current")
_CfprExtvmmSwitchDelTaskDescr_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskDescr_Object = MibTableColumn
cfprExtvmmSwitchDelTaskDescr = _CfprExtvmmSwitchDelTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 7),
    _CfprExtvmmSwitchDelTaskDescr_Type()
)
cfprExtvmmSwitchDelTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskDescr.setStatus("current")
_CfprExtvmmSwitchDelTaskExtKey_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskExtKey_Object = MibTableColumn
cfprExtvmmSwitchDelTaskExtKey = _CfprExtvmmSwitchDelTaskExtKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 8),
    _CfprExtvmmSwitchDelTaskExtKey_Type()
)
cfprExtvmmSwitchDelTaskExtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskExtKey.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmDescr_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmDescr_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmDescr = _CfprExtvmmSwitchDelTaskFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 9),
    _CfprExtvmmSwitchDelTaskFsmDescr_Type()
)
cfprExtvmmSwitchDelTaskFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmDescr.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmPrev_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmPrev_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmPrev = _CfprExtvmmSwitchDelTaskFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 10),
    _CfprExtvmmSwitchDelTaskFsmPrev_Type()
)
cfprExtvmmSwitchDelTaskFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmPrev.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmProgr_Type = Gauge32
_CfprExtvmmSwitchDelTaskFsmProgr_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmProgr = _CfprExtvmmSwitchDelTaskFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 11),
    _CfprExtvmmSwitchDelTaskFsmProgr_Type()
)
cfprExtvmmSwitchDelTaskFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmProgr.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmRmtInvErrCode_Type = Gauge32
_CfprExtvmmSwitchDelTaskFsmRmtInvErrCode_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmRmtInvErrCode = _CfprExtvmmSwitchDelTaskFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 12),
    _CfprExtvmmSwitchDelTaskFsmRmtInvErrCode_Type()
)
cfprExtvmmSwitchDelTaskFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmRmtInvErrCode.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmRmtInvErrDescr = _CfprExtvmmSwitchDelTaskFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 13),
    _CfprExtvmmSwitchDelTaskFsmRmtInvErrDescr_Type()
)
cfprExtvmmSwitchDelTaskFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmRmtInvErrDescr.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmSwitchDelTaskFsmRmtInvRslt_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmRmtInvRslt = _CfprExtvmmSwitchDelTaskFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 14),
    _CfprExtvmmSwitchDelTaskFsmRmtInvRslt_Type()
)
cfprExtvmmSwitchDelTaskFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmRmtInvRslt.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageDescr_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmStageDescr_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageDescr = _CfprExtvmmSwitchDelTaskFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 15),
    _CfprExtvmmSwitchDelTaskFsmStageDescr_Type()
)
cfprExtvmmSwitchDelTaskFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageDescr.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStamp_Type = DateAndTime
_CfprExtvmmSwitchDelTaskFsmStamp_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStamp = _CfprExtvmmSwitchDelTaskFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 16),
    _CfprExtvmmSwitchDelTaskFsmStamp_Type()
)
cfprExtvmmSwitchDelTaskFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStamp.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStatus_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmStatus_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStatus = _CfprExtvmmSwitchDelTaskFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 17),
    _CfprExtvmmSwitchDelTaskFsmStatus_Type()
)
cfprExtvmmSwitchDelTaskFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStatus.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTry_Type = Gauge32
_CfprExtvmmSwitchDelTaskFsmTry_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmTry = _CfprExtvmmSwitchDelTaskFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 18),
    _CfprExtvmmSwitchDelTaskFsmTry_Type()
)
cfprExtvmmSwitchDelTaskFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTry.setStatus("current")
_CfprExtvmmSwitchDelTaskHost_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskHost_Object = MibTableColumn
cfprExtvmmSwitchDelTaskHost = _CfprExtvmmSwitchDelTaskHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 19),
    _CfprExtvmmSwitchDelTaskHost_Type()
)
cfprExtvmmSwitchDelTaskHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskHost.setStatus("current")
_CfprExtvmmSwitchDelTaskIntId_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskIntId_Object = MibTableColumn
cfprExtvmmSwitchDelTaskIntId = _CfprExtvmmSwitchDelTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 20),
    _CfprExtvmmSwitchDelTaskIntId_Type()
)
cfprExtvmmSwitchDelTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskIntId.setStatus("current")
_CfprExtvmmSwitchDelTaskKeyInst_Type = Gauge32
_CfprExtvmmSwitchDelTaskKeyInst_Object = MibTableColumn
cfprExtvmmSwitchDelTaskKeyInst = _CfprExtvmmSwitchDelTaskKeyInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 21),
    _CfprExtvmmSwitchDelTaskKeyInst_Type()
)
cfprExtvmmSwitchDelTaskKeyInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskKeyInst.setStatus("current")
_CfprExtvmmSwitchDelTaskName_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskName_Object = MibTableColumn
cfprExtvmmSwitchDelTaskName = _CfprExtvmmSwitchDelTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 22),
    _CfprExtvmmSwitchDelTaskName_Type()
)
cfprExtvmmSwitchDelTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskName.setStatus("current")
_CfprExtvmmSwitchDelTaskOrgPath_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskOrgPath_Object = MibTableColumn
cfprExtvmmSwitchDelTaskOrgPath = _CfprExtvmmSwitchDelTaskOrgPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 23),
    _CfprExtvmmSwitchDelTaskOrgPath_Type()
)
cfprExtvmmSwitchDelTaskOrgPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskOrgPath.setStatus("current")
_CfprExtvmmSwitchDelTaskPolicyLevel_Type = Gauge32
_CfprExtvmmSwitchDelTaskPolicyLevel_Object = MibTableColumn
cfprExtvmmSwitchDelTaskPolicyLevel = _CfprExtvmmSwitchDelTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 24),
    _CfprExtvmmSwitchDelTaskPolicyLevel_Type()
)
cfprExtvmmSwitchDelTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskPolicyLevel.setStatus("current")
_CfprExtvmmSwitchDelTaskPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmSwitchDelTaskPolicyOwner_Object = MibTableColumn
cfprExtvmmSwitchDelTaskPolicyOwner = _CfprExtvmmSwitchDelTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 25),
    _CfprExtvmmSwitchDelTaskPolicyOwner_Type()
)
cfprExtvmmSwitchDelTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskPolicyOwner.setStatus("current")
_CfprExtvmmSwitchDelTaskPortValue_Type = Gauge32
_CfprExtvmmSwitchDelTaskPortValue_Object = MibTableColumn
cfprExtvmmSwitchDelTaskPortValue = _CfprExtvmmSwitchDelTaskPortValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 26),
    _CfprExtvmmSwitchDelTaskPortValue_Type()
)
cfprExtvmmSwitchDelTaskPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskPortValue.setStatus("current")
_CfprExtvmmSwitchDelTaskProvIntId_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskProvIntId_Object = MibTableColumn
cfprExtvmmSwitchDelTaskProvIntId = _CfprExtvmmSwitchDelTaskProvIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 27),
    _CfprExtvmmSwitchDelTaskProvIntId_Type()
)
cfprExtvmmSwitchDelTaskProvIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskProvIntId.setStatus("current")
_CfprExtvmmSwitchDelTaskProvider_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskProvider_Object = MibTableColumn
cfprExtvmmSwitchDelTaskProvider = _CfprExtvmmSwitchDelTaskProvider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 28),
    _CfprExtvmmSwitchDelTaskProvider_Type()
)
cfprExtvmmSwitchDelTaskProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskProvider.setStatus("current")
_CfprExtvmmSwitchDelTaskSwIntId_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskSwIntId_Object = MibTableColumn
cfprExtvmmSwitchDelTaskSwIntId = _CfprExtvmmSwitchDelTaskSwIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 29),
    _CfprExtvmmSwitchDelTaskSwIntId_Type()
)
cfprExtvmmSwitchDelTaskSwIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskSwIntId.setStatus("current")
_CfprExtvmmSwitchDelTaskSwName_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskSwName_Object = MibTableColumn
cfprExtvmmSwitchDelTaskSwName = _CfprExtvmmSwitchDelTaskSwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 26, 1, 30),
    _CfprExtvmmSwitchDelTaskSwName_Type()
)
cfprExtvmmSwitchDelTaskSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskSwName.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTable_Object = MibTable
cfprExtvmmSwitchDelTaskFsmTable = _CfprExtvmmSwitchDelTaskFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27)
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTable.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmEntry_Object = MibTableRow
cfprExtvmmSwitchDelTaskFsmEntry = _CfprExtvmmSwitchDelTaskFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1)
)
cfprExtvmmSwitchDelTaskFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmSwitchDelTaskFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmEntry.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmInstanceId_Type = CfprManagedObjectId
_CfprExtvmmSwitchDelTaskFsmInstanceId_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmInstanceId = _CfprExtvmmSwitchDelTaskFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 1),
    _CfprExtvmmSwitchDelTaskFsmInstanceId_Type()
)
cfprExtvmmSwitchDelTaskFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmInstanceId.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmDn_Type = CfprManagedObjectDn
_CfprExtvmmSwitchDelTaskFsmDn_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmDn = _CfprExtvmmSwitchDelTaskFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 2),
    _CfprExtvmmSwitchDelTaskFsmDn_Type()
)
cfprExtvmmSwitchDelTaskFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmDn.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmRn_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmRn_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmRn = _CfprExtvmmSwitchDelTaskFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 3),
    _CfprExtvmmSwitchDelTaskFsmRn_Type()
)
cfprExtvmmSwitchDelTaskFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmRn.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmCompletionTime_Type = DateAndTime
_CfprExtvmmSwitchDelTaskFsmCompletionTime_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmCompletionTime = _CfprExtvmmSwitchDelTaskFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 4),
    _CfprExtvmmSwitchDelTaskFsmCompletionTime_Type()
)
cfprExtvmmSwitchDelTaskFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmCompletionTime.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmCurrentFsm_Type = CfprExtvmmSwitchDelTaskFsmCurrentFsm
_CfprExtvmmSwitchDelTaskFsmCurrentFsm_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmCurrentFsm = _CfprExtvmmSwitchDelTaskFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 5),
    _CfprExtvmmSwitchDelTaskFsmCurrentFsm_Type()
)
cfprExtvmmSwitchDelTaskFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmCurrentFsm.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmDescrData_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmDescrData_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmDescrData = _CfprExtvmmSwitchDelTaskFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 6),
    _CfprExtvmmSwitchDelTaskFsmDescrData_Type()
)
cfprExtvmmSwitchDelTaskFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmDescrData.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmSwitchDelTaskFsmFsmStatus_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmFsmStatus = _CfprExtvmmSwitchDelTaskFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 7),
    _CfprExtvmmSwitchDelTaskFsmFsmStatus_Type()
)
cfprExtvmmSwitchDelTaskFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmFsmStatus.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmProgress_Type = Gauge32
_CfprExtvmmSwitchDelTaskFsmProgress_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmProgress = _CfprExtvmmSwitchDelTaskFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 8),
    _CfprExtvmmSwitchDelTaskFsmProgress_Type()
)
cfprExtvmmSwitchDelTaskFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmProgress.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmRmtErrCode_Type = Gauge32
_CfprExtvmmSwitchDelTaskFsmRmtErrCode_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmRmtErrCode = _CfprExtvmmSwitchDelTaskFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 9),
    _CfprExtvmmSwitchDelTaskFsmRmtErrCode_Type()
)
cfprExtvmmSwitchDelTaskFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmRmtErrCode.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmRmtErrDescr_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmRmtErrDescr = _CfprExtvmmSwitchDelTaskFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 10),
    _CfprExtvmmSwitchDelTaskFsmRmtErrDescr_Type()
)
cfprExtvmmSwitchDelTaskFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmRmtErrDescr.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtvmmSwitchDelTaskFsmRmtRslt_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmRmtRslt = _CfprExtvmmSwitchDelTaskFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 27, 1, 11),
    _CfprExtvmmSwitchDelTaskFsmRmtRslt_Type()
)
cfprExtvmmSwitchDelTaskFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmRmtRslt.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageTable_Object = MibTable
cfprExtvmmSwitchDelTaskFsmStageTable = _CfprExtvmmSwitchDelTaskFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28)
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageTable.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageEntry_Object = MibTableRow
cfprExtvmmSwitchDelTaskFsmStageEntry = _CfprExtvmmSwitchDelTaskFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1)
)
cfprExtvmmSwitchDelTaskFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmSwitchDelTaskFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageEntry.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtvmmSwitchDelTaskFsmStageInstanceId_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageInstanceId = _CfprExtvmmSwitchDelTaskFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 1),
    _CfprExtvmmSwitchDelTaskFsmStageInstanceId_Type()
)
cfprExtvmmSwitchDelTaskFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageInstanceId.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageDn_Type = CfprManagedObjectDn
_CfprExtvmmSwitchDelTaskFsmStageDn_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageDn = _CfprExtvmmSwitchDelTaskFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 2),
    _CfprExtvmmSwitchDelTaskFsmStageDn_Type()
)
cfprExtvmmSwitchDelTaskFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageDn.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageRn_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmStageRn_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageRn = _CfprExtvmmSwitchDelTaskFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 3),
    _CfprExtvmmSwitchDelTaskFsmStageRn_Type()
)
cfprExtvmmSwitchDelTaskFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageRn.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageDescrData_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmStageDescrData_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageDescrData = _CfprExtvmmSwitchDelTaskFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 4),
    _CfprExtvmmSwitchDelTaskFsmStageDescrData_Type()
)
cfprExtvmmSwitchDelTaskFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageDescrData.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtvmmSwitchDelTaskFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageLastUpdateTime = _CfprExtvmmSwitchDelTaskFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 5),
    _CfprExtvmmSwitchDelTaskFsmStageLastUpdateTime_Type()
)
cfprExtvmmSwitchDelTaskFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageLastUpdateTime.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageName_Type = CfprExtvmmSwitchDelTaskFsmStageName
_CfprExtvmmSwitchDelTaskFsmStageName_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageName = _CfprExtvmmSwitchDelTaskFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 6),
    _CfprExtvmmSwitchDelTaskFsmStageName_Type()
)
cfprExtvmmSwitchDelTaskFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageName.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageOrder_Type = Gauge32
_CfprExtvmmSwitchDelTaskFsmStageOrder_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageOrder = _CfprExtvmmSwitchDelTaskFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 7),
    _CfprExtvmmSwitchDelTaskFsmStageOrder_Type()
)
cfprExtvmmSwitchDelTaskFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageOrder.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageRetry_Type = Gauge32
_CfprExtvmmSwitchDelTaskFsmStageRetry_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageRetry = _CfprExtvmmSwitchDelTaskFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 8),
    _CfprExtvmmSwitchDelTaskFsmStageRetry_Type()
)
cfprExtvmmSwitchDelTaskFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageRetry.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtvmmSwitchDelTaskFsmStageStageStatus_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmStageStageStatus = _CfprExtvmmSwitchDelTaskFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 28, 1, 9),
    _CfprExtvmmSwitchDelTaskFsmStageStageStatus_Type()
)
cfprExtvmmSwitchDelTaskFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmStageStageStatus.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskTable_Object = MibTable
cfprExtvmmSwitchDelTaskFsmTaskTable = _CfprExtvmmSwitchDelTaskFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29)
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskTable.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskEntry_Object = MibTableRow
cfprExtvmmSwitchDelTaskFsmTaskEntry = _CfprExtvmmSwitchDelTaskFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29, 1)
)
cfprExtvmmSwitchDelTaskFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmSwitchDelTaskFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskEntry.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtvmmSwitchDelTaskFsmTaskInstanceId_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmTaskInstanceId = _CfprExtvmmSwitchDelTaskFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29, 1, 1),
    _CfprExtvmmSwitchDelTaskFsmTaskInstanceId_Type()
)
cfprExtvmmSwitchDelTaskFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskInstanceId.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtvmmSwitchDelTaskFsmTaskDn_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmTaskDn = _CfprExtvmmSwitchDelTaskFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29, 1, 2),
    _CfprExtvmmSwitchDelTaskFsmTaskDn_Type()
)
cfprExtvmmSwitchDelTaskFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskDn.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskRn_Type = SnmpAdminString
_CfprExtvmmSwitchDelTaskFsmTaskRn_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmTaskRn = _CfprExtvmmSwitchDelTaskFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29, 1, 3),
    _CfprExtvmmSwitchDelTaskFsmTaskRn_Type()
)
cfprExtvmmSwitchDelTaskFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskRn.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtvmmSwitchDelTaskFsmTaskCompletion_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmTaskCompletion = _CfprExtvmmSwitchDelTaskFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29, 1, 4),
    _CfprExtvmmSwitchDelTaskFsmTaskCompletion_Type()
)
cfprExtvmmSwitchDelTaskFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskCompletion.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskFlags_Type = CfprFsmFlags
_CfprExtvmmSwitchDelTaskFsmTaskFlags_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmTaskFlags = _CfprExtvmmSwitchDelTaskFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29, 1, 5),
    _CfprExtvmmSwitchDelTaskFsmTaskFlags_Type()
)
cfprExtvmmSwitchDelTaskFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskFlags.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskItem_Type = CfprExtvmmSwitchDelTaskFsmTaskItem
_CfprExtvmmSwitchDelTaskFsmTaskItem_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmTaskItem = _CfprExtvmmSwitchDelTaskFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29, 1, 6),
    _CfprExtvmmSwitchDelTaskFsmTaskItem_Type()
)
cfprExtvmmSwitchDelTaskFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskItem.setStatus("current")
_CfprExtvmmSwitchDelTaskFsmTaskSeqId_Type = Gauge32
_CfprExtvmmSwitchDelTaskFsmTaskSeqId_Object = MibTableColumn
cfprExtvmmSwitchDelTaskFsmTaskSeqId = _CfprExtvmmSwitchDelTaskFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 29, 1, 7),
    _CfprExtvmmSwitchDelTaskFsmTaskSeqId_Type()
)
cfprExtvmmSwitchDelTaskFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchDelTaskFsmTaskSeqId.setStatus("current")
_CfprExtvmmSwitchSetTable_Object = MibTable
cfprExtvmmSwitchSetTable = _CfprExtvmmSwitchSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 30)
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchSetTable.setStatus("current")
_CfprExtvmmSwitchSetEntry_Object = MibTableRow
cfprExtvmmSwitchSetEntry = _CfprExtvmmSwitchSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 30, 1)
)
cfprExtvmmSwitchSetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmSwitchSetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmSwitchSetEntry.setStatus("current")
_CfprExtvmmSwitchSetInstanceId_Type = CfprManagedObjectId
_CfprExtvmmSwitchSetInstanceId_Object = MibTableColumn
cfprExtvmmSwitchSetInstanceId = _CfprExtvmmSwitchSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 30, 1, 1),
    _CfprExtvmmSwitchSetInstanceId_Type()
)
cfprExtvmmSwitchSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchSetInstanceId.setStatus("current")
_CfprExtvmmSwitchSetDn_Type = CfprManagedObjectDn
_CfprExtvmmSwitchSetDn_Object = MibTableColumn
cfprExtvmmSwitchSetDn = _CfprExtvmmSwitchSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 30, 1, 2),
    _CfprExtvmmSwitchSetDn_Type()
)
cfprExtvmmSwitchSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchSetDn.setStatus("current")
_CfprExtvmmSwitchSetRn_Type = SnmpAdminString
_CfprExtvmmSwitchSetRn_Object = MibTableColumn
cfprExtvmmSwitchSetRn = _CfprExtvmmSwitchSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 30, 1, 3),
    _CfprExtvmmSwitchSetRn_Type()
)
cfprExtvmmSwitchSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmSwitchSetRn.setStatus("current")
_CfprExtvmmUpLinkPPTable_Object = MibTable
cfprExtvmmUpLinkPPTable = _CfprExtvmmUpLinkPPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31)
)
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPTable.setStatus("current")
_CfprExtvmmUpLinkPPEntry_Object = MibTableRow
cfprExtvmmUpLinkPPEntry = _CfprExtvmmUpLinkPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1)
)
cfprExtvmmUpLinkPPEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmUpLinkPPInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPEntry.setStatus("current")
_CfprExtvmmUpLinkPPInstanceId_Type = CfprManagedObjectId
_CfprExtvmmUpLinkPPInstanceId_Object = MibTableColumn
cfprExtvmmUpLinkPPInstanceId = _CfprExtvmmUpLinkPPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 1),
    _CfprExtvmmUpLinkPPInstanceId_Type()
)
cfprExtvmmUpLinkPPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPInstanceId.setStatus("current")
_CfprExtvmmUpLinkPPDn_Type = CfprManagedObjectDn
_CfprExtvmmUpLinkPPDn_Object = MibTableColumn
cfprExtvmmUpLinkPPDn = _CfprExtvmmUpLinkPPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 2),
    _CfprExtvmmUpLinkPPDn_Type()
)
cfprExtvmmUpLinkPPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPDn.setStatus("current")
_CfprExtvmmUpLinkPPRn_Type = SnmpAdminString
_CfprExtvmmUpLinkPPRn_Object = MibTableColumn
cfprExtvmmUpLinkPPRn = _CfprExtvmmUpLinkPPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 3),
    _CfprExtvmmUpLinkPPRn_Type()
)
cfprExtvmmUpLinkPPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPRn.setStatus("current")
_CfprExtvmmUpLinkPPDescr_Type = SnmpAdminString
_CfprExtvmmUpLinkPPDescr_Object = MibTableColumn
cfprExtvmmUpLinkPPDescr = _CfprExtvmmUpLinkPPDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 4),
    _CfprExtvmmUpLinkPPDescr_Type()
)
cfprExtvmmUpLinkPPDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPDescr.setStatus("current")
_CfprExtvmmUpLinkPPFltAggr_Type = Unsigned64
_CfprExtvmmUpLinkPPFltAggr_Object = MibTableColumn
cfprExtvmmUpLinkPPFltAggr = _CfprExtvmmUpLinkPPFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 5),
    _CfprExtvmmUpLinkPPFltAggr_Type()
)
cfprExtvmmUpLinkPPFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPFltAggr.setStatus("current")
_CfprExtvmmUpLinkPPGuid_Type = SnmpAdminString
_CfprExtvmmUpLinkPPGuid_Object = MibTableColumn
cfprExtvmmUpLinkPPGuid = _CfprExtvmmUpLinkPPGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 6),
    _CfprExtvmmUpLinkPPGuid_Type()
)
cfprExtvmmUpLinkPPGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPGuid.setStatus("current")
_CfprExtvmmUpLinkPPIntId_Type = SnmpAdminString
_CfprExtvmmUpLinkPPIntId_Object = MibTableColumn
cfprExtvmmUpLinkPPIntId = _CfprExtvmmUpLinkPPIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 7),
    _CfprExtvmmUpLinkPPIntId_Type()
)
cfprExtvmmUpLinkPPIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPIntId.setStatus("current")
_CfprExtvmmUpLinkPPName_Type = SnmpAdminString
_CfprExtvmmUpLinkPPName_Object = MibTableColumn
cfprExtvmmUpLinkPPName = _CfprExtvmmUpLinkPPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 8),
    _CfprExtvmmUpLinkPPName_Type()
)
cfprExtvmmUpLinkPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPName.setStatus("current")
_CfprExtvmmUpLinkPPPolicyLevel_Type = Gauge32
_CfprExtvmmUpLinkPPPolicyLevel_Object = MibTableColumn
cfprExtvmmUpLinkPPPolicyLevel = _CfprExtvmmUpLinkPPPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 9),
    _CfprExtvmmUpLinkPPPolicyLevel_Type()
)
cfprExtvmmUpLinkPPPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPPolicyLevel.setStatus("current")
_CfprExtvmmUpLinkPPPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmUpLinkPPPolicyOwner_Object = MibTableColumn
cfprExtvmmUpLinkPPPolicyOwner = _CfprExtvmmUpLinkPPPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 10),
    _CfprExtvmmUpLinkPPPolicyOwner_Type()
)
cfprExtvmmUpLinkPPPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPPolicyOwner.setStatus("current")
_CfprExtvmmUpLinkPPRefOperState_Type = CfprExtvmmRefOperState
_CfprExtvmmUpLinkPPRefOperState_Object = MibTableColumn
cfprExtvmmUpLinkPPRefOperState = _CfprExtvmmUpLinkPPRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 31, 1, 11),
    _CfprExtvmmUpLinkPPRefOperState_Type()
)
cfprExtvmmUpLinkPPRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmUpLinkPPRefOperState.setStatus("current")
_CfprExtvmmVMNDRefTable_Object = MibTable
cfprExtvmmVMNDRefTable = _CfprExtvmmVMNDRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32)
)
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefTable.setStatus("current")
_CfprExtvmmVMNDRefEntry_Object = MibTableRow
cfprExtvmmVMNDRefEntry = _CfprExtvmmVMNDRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1)
)
cfprExtvmmVMNDRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmVMNDRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefEntry.setStatus("current")
_CfprExtvmmVMNDRefInstanceId_Type = CfprManagedObjectId
_CfprExtvmmVMNDRefInstanceId_Object = MibTableColumn
cfprExtvmmVMNDRefInstanceId = _CfprExtvmmVMNDRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 1),
    _CfprExtvmmVMNDRefInstanceId_Type()
)
cfprExtvmmVMNDRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefInstanceId.setStatus("current")
_CfprExtvmmVMNDRefDn_Type = CfprManagedObjectDn
_CfprExtvmmVMNDRefDn_Object = MibTableColumn
cfprExtvmmVMNDRefDn = _CfprExtvmmVMNDRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 2),
    _CfprExtvmmVMNDRefDn_Type()
)
cfprExtvmmVMNDRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefDn.setStatus("current")
_CfprExtvmmVMNDRefRn_Type = SnmpAdminString
_CfprExtvmmVMNDRefRn_Object = MibTableColumn
cfprExtvmmVMNDRefRn = _CfprExtvmmVMNDRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 3),
    _CfprExtvmmVMNDRefRn_Type()
)
cfprExtvmmVMNDRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefRn.setStatus("current")
_CfprExtvmmVMNDRefConfigQualifier_Type = CfprExtvmmNetworkSetConfigQualifier
_CfprExtvmmVMNDRefConfigQualifier_Object = MibTableColumn
cfprExtvmmVMNDRefConfigQualifier = _CfprExtvmmVMNDRefConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 4),
    _CfprExtvmmVMNDRefConfigQualifier_Type()
)
cfprExtvmmVMNDRefConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefConfigQualifier.setStatus("current")
_CfprExtvmmVMNDRefDescr_Type = SnmpAdminString
_CfprExtvmmVMNDRefDescr_Object = MibTableColumn
cfprExtvmmVMNDRefDescr = _CfprExtvmmVMNDRefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 5),
    _CfprExtvmmVMNDRefDescr_Type()
)
cfprExtvmmVMNDRefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefDescr.setStatus("current")
_CfprExtvmmVMNDRefFnDefName_Type = SnmpAdminString
_CfprExtvmmVMNDRefFnDefName_Object = MibTableColumn
cfprExtvmmVMNDRefFnDefName = _CfprExtvmmVMNDRefFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 6),
    _CfprExtvmmVMNDRefFnDefName_Type()
)
cfprExtvmmVMNDRefFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefFnDefName.setStatus("current")
_CfprExtvmmVMNDRefFnName_Type = SnmpAdminString
_CfprExtvmmVMNDRefFnName_Object = MibTableColumn
cfprExtvmmVMNDRefFnName = _CfprExtvmmVMNDRefFnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 7),
    _CfprExtvmmVMNDRefFnName_Type()
)
cfprExtvmmVMNDRefFnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefFnName.setStatus("current")
_CfprExtvmmVMNDRefIntId_Type = SnmpAdminString
_CfprExtvmmVMNDRefIntId_Object = MibTableColumn
cfprExtvmmVMNDRefIntId = _CfprExtvmmVMNDRefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 8),
    _CfprExtvmmVMNDRefIntId_Type()
)
cfprExtvmmVMNDRefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefIntId.setStatus("current")
_CfprExtvmmVMNDRefName_Type = SnmpAdminString
_CfprExtvmmVMNDRefName_Object = MibTableColumn
cfprExtvmmVMNDRefName = _CfprExtvmmVMNDRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 9),
    _CfprExtvmmVMNDRefName_Type()
)
cfprExtvmmVMNDRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefName.setStatus("current")
_CfprExtvmmVMNDRefOperVmNetworkDefName_Type = SnmpAdminString
_CfprExtvmmVMNDRefOperVmNetworkDefName_Object = MibTableColumn
cfprExtvmmVMNDRefOperVmNetworkDefName = _CfprExtvmmVMNDRefOperVmNetworkDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 10),
    _CfprExtvmmVMNDRefOperVmNetworkDefName_Type()
)
cfprExtvmmVMNDRefOperVmNetworkDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefOperVmNetworkDefName.setStatus("current")
_CfprExtvmmVMNDRefPolicyLevel_Type = Gauge32
_CfprExtvmmVMNDRefPolicyLevel_Object = MibTableColumn
cfprExtvmmVMNDRefPolicyLevel = _CfprExtvmmVMNDRefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 11),
    _CfprExtvmmVMNDRefPolicyLevel_Type()
)
cfprExtvmmVMNDRefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefPolicyLevel.setStatus("current")
_CfprExtvmmVMNDRefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmVMNDRefPolicyOwner_Object = MibTableColumn
cfprExtvmmVMNDRefPolicyOwner = _CfprExtvmmVMNDRefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 12),
    _CfprExtvmmVMNDRefPolicyOwner_Type()
)
cfprExtvmmVMNDRefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefPolicyOwner.setStatus("current")
_CfprExtvmmVMNDRefVmNetworkDefName_Type = SnmpAdminString
_CfprExtvmmVMNDRefVmNetworkDefName_Object = MibTableColumn
cfprExtvmmVMNDRefVmNetworkDefName = _CfprExtvmmVMNDRefVmNetworkDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 32, 1, 13),
    _CfprExtvmmVMNDRefVmNetworkDefName_Type()
)
cfprExtvmmVMNDRefVmNetworkDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNDRefVmNetworkDefName.setStatus("current")
_CfprExtvmmVMNetworkTable_Object = MibTable
cfprExtvmmVMNetworkTable = _CfprExtvmmVMNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33)
)
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkTable.setStatus("current")
_CfprExtvmmVMNetworkEntry_Object = MibTableRow
cfprExtvmmVMNetworkEntry = _CfprExtvmmVMNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1)
)
cfprExtvmmVMNetworkEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmVMNetworkInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkEntry.setStatus("current")
_CfprExtvmmVMNetworkInstanceId_Type = CfprManagedObjectId
_CfprExtvmmVMNetworkInstanceId_Object = MibTableColumn
cfprExtvmmVMNetworkInstanceId = _CfprExtvmmVMNetworkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 1),
    _CfprExtvmmVMNetworkInstanceId_Type()
)
cfprExtvmmVMNetworkInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkInstanceId.setStatus("current")
_CfprExtvmmVMNetworkDn_Type = CfprManagedObjectDn
_CfprExtvmmVMNetworkDn_Object = MibTableColumn
cfprExtvmmVMNetworkDn = _CfprExtvmmVMNetworkDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 2),
    _CfprExtvmmVMNetworkDn_Type()
)
cfprExtvmmVMNetworkDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDn.setStatus("current")
_CfprExtvmmVMNetworkRn_Type = SnmpAdminString
_CfprExtvmmVMNetworkRn_Object = MibTableColumn
cfprExtvmmVMNetworkRn = _CfprExtvmmVMNetworkRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 3),
    _CfprExtvmmVMNetworkRn_Type()
)
cfprExtvmmVMNetworkRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkRn.setStatus("current")
_CfprExtvmmVMNetworkDescr_Type = SnmpAdminString
_CfprExtvmmVMNetworkDescr_Object = MibTableColumn
cfprExtvmmVMNetworkDescr = _CfprExtvmmVMNetworkDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 4),
    _CfprExtvmmVMNetworkDescr_Type()
)
cfprExtvmmVMNetworkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDescr.setStatus("current")
_CfprExtvmmVMNetworkFabricNetworkName_Type = SnmpAdminString
_CfprExtvmmVMNetworkFabricNetworkName_Object = MibTableColumn
cfprExtvmmVMNetworkFabricNetworkName = _CfprExtvmmVMNetworkFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 5),
    _CfprExtvmmVMNetworkFabricNetworkName_Type()
)
cfprExtvmmVMNetworkFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkFabricNetworkName.setStatus("current")
_CfprExtvmmVMNetworkFltAggr_Type = Unsigned64
_CfprExtvmmVMNetworkFltAggr_Object = MibTableColumn
cfprExtvmmVMNetworkFltAggr = _CfprExtvmmVMNetworkFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 6),
    _CfprExtvmmVMNetworkFltAggr_Type()
)
cfprExtvmmVMNetworkFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkFltAggr.setStatus("current")
_CfprExtvmmVMNetworkGuid_Type = SnmpAdminString
_CfprExtvmmVMNetworkGuid_Object = MibTableColumn
cfprExtvmmVMNetworkGuid = _CfprExtvmmVMNetworkGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 7),
    _CfprExtvmmVMNetworkGuid_Type()
)
cfprExtvmmVMNetworkGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkGuid.setStatus("current")
_CfprExtvmmVMNetworkIntId_Type = SnmpAdminString
_CfprExtvmmVMNetworkIntId_Object = MibTableColumn
cfprExtvmmVMNetworkIntId = _CfprExtvmmVMNetworkIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 8),
    _CfprExtvmmVMNetworkIntId_Type()
)
cfprExtvmmVMNetworkIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkIntId.setStatus("current")
_CfprExtvmmVMNetworkName_Type = SnmpAdminString
_CfprExtvmmVMNetworkName_Object = MibTableColumn
cfprExtvmmVMNetworkName = _CfprExtvmmVMNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 9),
    _CfprExtvmmVMNetworkName_Type()
)
cfprExtvmmVMNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkName.setStatus("current")
_CfprExtvmmVMNetworkOperFabricNetworkName_Type = SnmpAdminString
_CfprExtvmmVMNetworkOperFabricNetworkName_Object = MibTableColumn
cfprExtvmmVMNetworkOperFabricNetworkName = _CfprExtvmmVMNetworkOperFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 10),
    _CfprExtvmmVMNetworkOperFabricNetworkName_Type()
)
cfprExtvmmVMNetworkOperFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkOperFabricNetworkName.setStatus("current")
_CfprExtvmmVMNetworkPolicyLevel_Type = Gauge32
_CfprExtvmmVMNetworkPolicyLevel_Object = MibTableColumn
cfprExtvmmVMNetworkPolicyLevel = _CfprExtvmmVMNetworkPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 11),
    _CfprExtvmmVMNetworkPolicyLevel_Type()
)
cfprExtvmmVMNetworkPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkPolicyLevel.setStatus("current")
_CfprExtvmmVMNetworkPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmVMNetworkPolicyOwner_Object = MibTableColumn
cfprExtvmmVMNetworkPolicyOwner = _CfprExtvmmVMNetworkPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 33, 1, 12),
    _CfprExtvmmVMNetworkPolicyOwner_Type()
)
cfprExtvmmVMNetworkPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkPolicyOwner.setStatus("current")
_CfprExtvmmVMNetworkDefinitionTable_Object = MibTable
cfprExtvmmVMNetworkDefinitionTable = _CfprExtvmmVMNetworkDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34)
)
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionTable.setStatus("current")
_CfprExtvmmVMNetworkDefinitionEntry_Object = MibTableRow
cfprExtvmmVMNetworkDefinitionEntry = _CfprExtvmmVMNetworkDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1)
)
cfprExtvmmVMNetworkDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmVMNetworkDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionEntry.setStatus("current")
_CfprExtvmmVMNetworkDefinitionInstanceId_Type = CfprManagedObjectId
_CfprExtvmmVMNetworkDefinitionInstanceId_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionInstanceId = _CfprExtvmmVMNetworkDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 1),
    _CfprExtvmmVMNetworkDefinitionInstanceId_Type()
)
cfprExtvmmVMNetworkDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionInstanceId.setStatus("current")
_CfprExtvmmVMNetworkDefinitionDn_Type = CfprManagedObjectDn
_CfprExtvmmVMNetworkDefinitionDn_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionDn = _CfprExtvmmVMNetworkDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 2),
    _CfprExtvmmVMNetworkDefinitionDn_Type()
)
cfprExtvmmVMNetworkDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionDn.setStatus("current")
_CfprExtvmmVMNetworkDefinitionRn_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionRn_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionRn = _CfprExtvmmVMNetworkDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 3),
    _CfprExtvmmVMNetworkDefinitionRn_Type()
)
cfprExtvmmVMNetworkDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionRn.setStatus("current")
_CfprExtvmmVMNetworkDefinitionDescr_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionDescr_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionDescr = _CfprExtvmmVMNetworkDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 4),
    _CfprExtvmmVMNetworkDefinitionDescr_Type()
)
cfprExtvmmVMNetworkDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionDescr.setStatus("current")
_CfprExtvmmVMNetworkDefinitionExtIpPoolName_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionExtIpPoolName_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionExtIpPoolName = _CfprExtvmmVMNetworkDefinitionExtIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 5),
    _CfprExtvmmVMNetworkDefinitionExtIpPoolName_Type()
)
cfprExtvmmVMNetworkDefinitionExtIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionExtIpPoolName.setStatus("current")
_CfprExtvmmVMNetworkDefinitionGuid_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionGuid_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionGuid = _CfprExtvmmVMNetworkDefinitionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 6),
    _CfprExtvmmVMNetworkDefinitionGuid_Type()
)
cfprExtvmmVMNetworkDefinitionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionGuid.setStatus("current")
_CfprExtvmmVMNetworkDefinitionIntId_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionIntId_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionIntId = _CfprExtvmmVMNetworkDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 7),
    _CfprExtvmmVMNetworkDefinitionIntId_Type()
)
cfprExtvmmVMNetworkDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionIntId.setStatus("current")
_CfprExtvmmVMNetworkDefinitionIpPoolGuid_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionIpPoolGuid_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionIpPoolGuid = _CfprExtvmmVMNetworkDefinitionIpPoolGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 8),
    _CfprExtvmmVMNetworkDefinitionIpPoolGuid_Type()
)
cfprExtvmmVMNetworkDefinitionIpPoolGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionIpPoolGuid.setStatus("current")
_CfprExtvmmVMNetworkDefinitionMaxPorts_Type = Gauge32
_CfprExtvmmVMNetworkDefinitionMaxPorts_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionMaxPorts = _CfprExtvmmVMNetworkDefinitionMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 9),
    _CfprExtvmmVMNetworkDefinitionMaxPorts_Type()
)
cfprExtvmmVMNetworkDefinitionMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionMaxPorts.setStatus("current")
_CfprExtvmmVMNetworkDefinitionName_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionName_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionName = _CfprExtvmmVMNetworkDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 10),
    _CfprExtvmmVMNetworkDefinitionName_Type()
)
cfprExtvmmVMNetworkDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionName.setStatus("current")
_CfprExtvmmVMNetworkDefinitionOperExtIpPoolName_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionOperExtIpPoolName_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionOperExtIpPoolName = _CfprExtvmmVMNetworkDefinitionOperExtIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 11),
    _CfprExtvmmVMNetworkDefinitionOperExtIpPoolName_Type()
)
cfprExtvmmVMNetworkDefinitionOperExtIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionOperExtIpPoolName.setStatus("current")
_CfprExtvmmVMNetworkDefinitionPolicyLevel_Type = Gauge32
_CfprExtvmmVMNetworkDefinitionPolicyLevel_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionPolicyLevel = _CfprExtvmmVMNetworkDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 12),
    _CfprExtvmmVMNetworkDefinitionPolicyLevel_Type()
)
cfprExtvmmVMNetworkDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionPolicyLevel.setStatus("current")
_CfprExtvmmVMNetworkDefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtvmmVMNetworkDefinitionPolicyOwner_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionPolicyOwner = _CfprExtvmmVMNetworkDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 13),
    _CfprExtvmmVMNetworkDefinitionPolicyOwner_Type()
)
cfprExtvmmVMNetworkDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionPolicyOwner.setStatus("current")
_CfprExtvmmVMNetworkDefinitionPrimaryVlanId_Type = Gauge32
_CfprExtvmmVMNetworkDefinitionPrimaryVlanId_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionPrimaryVlanId = _CfprExtvmmVMNetworkDefinitionPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 14),
    _CfprExtvmmVMNetworkDefinitionPrimaryVlanId_Type()
)
cfprExtvmmVMNetworkDefinitionPrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionPrimaryVlanId.setStatus("current")
_CfprExtvmmVMNetworkDefinitionRefOperState_Type = CfprExtvmmRefOperState
_CfprExtvmmVMNetworkDefinitionRefOperState_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionRefOperState = _CfprExtvmmVMNetworkDefinitionRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 15),
    _CfprExtvmmVMNetworkDefinitionRefOperState_Type()
)
cfprExtvmmVMNetworkDefinitionRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionRefOperState.setStatus("current")
_CfprExtvmmVMNetworkDefinitionVlanName_Type = SnmpAdminString
_CfprExtvmmVMNetworkDefinitionVlanName_Object = MibTableColumn
cfprExtvmmVMNetworkDefinitionVlanName = _CfprExtvmmVMNetworkDefinitionVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 34, 1, 16),
    _CfprExtvmmVMNetworkDefinitionVlanName_Type()
)
cfprExtvmmVMNetworkDefinitionVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkDefinitionVlanName.setStatus("current")
_CfprExtvmmVMNetworkSetsTable_Object = MibTable
cfprExtvmmVMNetworkSetsTable = _CfprExtvmmVMNetworkSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 35)
)
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkSetsTable.setStatus("current")
_CfprExtvmmVMNetworkSetsEntry_Object = MibTableRow
cfprExtvmmVMNetworkSetsEntry = _CfprExtvmmVMNetworkSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 35, 1)
)
cfprExtvmmVMNetworkSetsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTVMM-MIB", "cfprExtvmmVMNetworkSetsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkSetsEntry.setStatus("current")
_CfprExtvmmVMNetworkSetsInstanceId_Type = CfprManagedObjectId
_CfprExtvmmVMNetworkSetsInstanceId_Object = MibTableColumn
cfprExtvmmVMNetworkSetsInstanceId = _CfprExtvmmVMNetworkSetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 35, 1, 1),
    _CfprExtvmmVMNetworkSetsInstanceId_Type()
)
cfprExtvmmVMNetworkSetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkSetsInstanceId.setStatus("current")
_CfprExtvmmVMNetworkSetsDn_Type = CfprManagedObjectDn
_CfprExtvmmVMNetworkSetsDn_Object = MibTableColumn
cfprExtvmmVMNetworkSetsDn = _CfprExtvmmVMNetworkSetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 35, 1, 2),
    _CfprExtvmmVMNetworkSetsDn_Type()
)
cfprExtvmmVMNetworkSetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkSetsDn.setStatus("current")
_CfprExtvmmVMNetworkSetsRn_Type = SnmpAdminString
_CfprExtvmmVMNetworkSetsRn_Object = MibTableColumn
cfprExtvmmVMNetworkSetsRn = _CfprExtvmmVMNetworkSetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 35, 1, 3),
    _CfprExtvmmVMNetworkSetsRn_Type()
)
cfprExtvmmVMNetworkSetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkSetsRn.setStatus("current")
_CfprExtvmmVMNetworkSetsFltAggr_Type = Unsigned64
_CfprExtvmmVMNetworkSetsFltAggr_Object = MibTableColumn
cfprExtvmmVMNetworkSetsFltAggr = _CfprExtvmmVMNetworkSetsFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 35, 1, 4),
    _CfprExtvmmVMNetworkSetsFltAggr_Type()
)
cfprExtvmmVMNetworkSetsFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkSetsFltAggr.setStatus("current")
_CfprExtvmmVMNetworkSetsGenNum_Type = Gauge32
_CfprExtvmmVMNetworkSetsGenNum_Object = MibTableColumn
cfprExtvmmVMNetworkSetsGenNum = _CfprExtvmmVMNetworkSetsGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 25, 35, 1, 5),
    _CfprExtvmmVMNetworkSetsGenNum_Type()
)
cfprExtvmmVMNetworkSetsGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtvmmVMNetworkSetsGenNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-EXTVMM-MIB",
    **{"cfprExtvmmObjects": cfprExtvmmObjects,
       "cfprExtvmmEpTable": cfprExtvmmEpTable,
       "cfprExtvmmEpEntry": cfprExtvmmEpEntry,
       "cfprExtvmmEpInstanceId": cfprExtvmmEpInstanceId,
       "cfprExtvmmEpDn": cfprExtvmmEpDn,
       "cfprExtvmmEpRn": cfprExtvmmEpRn,
       "cfprExtvmmEpFsmDescr": cfprExtvmmEpFsmDescr,
       "cfprExtvmmEpFsmPrev": cfprExtvmmEpFsmPrev,
       "cfprExtvmmEpFsmProgr": cfprExtvmmEpFsmProgr,
       "cfprExtvmmEpFsmRmtInvErrCode": cfprExtvmmEpFsmRmtInvErrCode,
       "cfprExtvmmEpFsmRmtInvErrDescr": cfprExtvmmEpFsmRmtInvErrDescr,
       "cfprExtvmmEpFsmRmtInvRslt": cfprExtvmmEpFsmRmtInvRslt,
       "cfprExtvmmEpFsmStageDescr": cfprExtvmmEpFsmStageDescr,
       "cfprExtvmmEpFsmStamp": cfprExtvmmEpFsmStamp,
       "cfprExtvmmEpFsmStatus": cfprExtvmmEpFsmStatus,
       "cfprExtvmmEpFsmTry": cfprExtvmmEpFsmTry,
       "cfprExtvmmEpGenNum": cfprExtvmmEpGenNum,
       "cfprExtvmmEpFsmTable": cfprExtvmmEpFsmTable,
       "cfprExtvmmEpFsmEntry": cfprExtvmmEpFsmEntry,
       "cfprExtvmmEpFsmInstanceId": cfprExtvmmEpFsmInstanceId,
       "cfprExtvmmEpFsmDn": cfprExtvmmEpFsmDn,
       "cfprExtvmmEpFsmRn": cfprExtvmmEpFsmRn,
       "cfprExtvmmEpFsmCompletionTime": cfprExtvmmEpFsmCompletionTime,
       "cfprExtvmmEpFsmCurrentFsm": cfprExtvmmEpFsmCurrentFsm,
       "cfprExtvmmEpFsmDescrData": cfprExtvmmEpFsmDescrData,
       "cfprExtvmmEpFsmFsmStatus": cfprExtvmmEpFsmFsmStatus,
       "cfprExtvmmEpFsmProgress": cfprExtvmmEpFsmProgress,
       "cfprExtvmmEpFsmRmtErrCode": cfprExtvmmEpFsmRmtErrCode,
       "cfprExtvmmEpFsmRmtErrDescr": cfprExtvmmEpFsmRmtErrDescr,
       "cfprExtvmmEpFsmRmtRslt": cfprExtvmmEpFsmRmtRslt,
       "cfprExtvmmEpFsmStageTable": cfprExtvmmEpFsmStageTable,
       "cfprExtvmmEpFsmStageEntry": cfprExtvmmEpFsmStageEntry,
       "cfprExtvmmEpFsmStageInstanceId": cfprExtvmmEpFsmStageInstanceId,
       "cfprExtvmmEpFsmStageDn": cfprExtvmmEpFsmStageDn,
       "cfprExtvmmEpFsmStageRn": cfprExtvmmEpFsmStageRn,
       "cfprExtvmmEpFsmStageDescrData": cfprExtvmmEpFsmStageDescrData,
       "cfprExtvmmEpFsmStageLastUpdateTime": cfprExtvmmEpFsmStageLastUpdateTime,
       "cfprExtvmmEpFsmStageName": cfprExtvmmEpFsmStageName,
       "cfprExtvmmEpFsmStageOrder": cfprExtvmmEpFsmStageOrder,
       "cfprExtvmmEpFsmStageRetry": cfprExtvmmEpFsmStageRetry,
       "cfprExtvmmEpFsmStageStageStatus": cfprExtvmmEpFsmStageStageStatus,
       "cfprExtvmmEpFsmTaskTable": cfprExtvmmEpFsmTaskTable,
       "cfprExtvmmEpFsmTaskEntry": cfprExtvmmEpFsmTaskEntry,
       "cfprExtvmmEpFsmTaskInstanceId": cfprExtvmmEpFsmTaskInstanceId,
       "cfprExtvmmEpFsmTaskDn": cfprExtvmmEpFsmTaskDn,
       "cfprExtvmmEpFsmTaskRn": cfprExtvmmEpFsmTaskRn,
       "cfprExtvmmEpFsmTaskCompletion": cfprExtvmmEpFsmTaskCompletion,
       "cfprExtvmmEpFsmTaskFlags": cfprExtvmmEpFsmTaskFlags,
       "cfprExtvmmEpFsmTaskItem": cfprExtvmmEpFsmTaskItem,
       "cfprExtvmmEpFsmTaskSeqId": cfprExtvmmEpFsmTaskSeqId,
       "cfprExtvmmFNDReferenceTable": cfprExtvmmFNDReferenceTable,
       "cfprExtvmmFNDReferenceEntry": cfprExtvmmFNDReferenceEntry,
       "cfprExtvmmFNDReferenceInstanceId": cfprExtvmmFNDReferenceInstanceId,
       "cfprExtvmmFNDReferenceDn": cfprExtvmmFNDReferenceDn,
       "cfprExtvmmFNDReferenceRn": cfprExtvmmFNDReferenceRn,
       "cfprExtvmmFNDReferenceDescr": cfprExtvmmFNDReferenceDescr,
       "cfprExtvmmFNDReferenceFnDefName": cfprExtvmmFNDReferenceFnDefName,
       "cfprExtvmmFNDReferenceIntId": cfprExtvmmFNDReferenceIntId,
       "cfprExtvmmFNDReferenceName": cfprExtvmmFNDReferenceName,
       "cfprExtvmmFNDReferenceOperFnDefName": cfprExtvmmFNDReferenceOperFnDefName,
       "cfprExtvmmFNDReferencePolicyLevel": cfprExtvmmFNDReferencePolicyLevel,
       "cfprExtvmmFNDReferencePolicyOwner": cfprExtvmmFNDReferencePolicyOwner,
       "cfprExtvmmFabricNetworkTable": cfprExtvmmFabricNetworkTable,
       "cfprExtvmmFabricNetworkEntry": cfprExtvmmFabricNetworkEntry,
       "cfprExtvmmFabricNetworkInstanceId": cfprExtvmmFabricNetworkInstanceId,
       "cfprExtvmmFabricNetworkDn": cfprExtvmmFabricNetworkDn,
       "cfprExtvmmFabricNetworkRn": cfprExtvmmFabricNetworkRn,
       "cfprExtvmmFabricNetworkDescr": cfprExtvmmFabricNetworkDescr,
       "cfprExtvmmFabricNetworkGuid": cfprExtvmmFabricNetworkGuid,
       "cfprExtvmmFabricNetworkIntId": cfprExtvmmFabricNetworkIntId,
       "cfprExtvmmFabricNetworkName": cfprExtvmmFabricNetworkName,
       "cfprExtvmmFabricNetworkNetworkType": cfprExtvmmFabricNetworkNetworkType,
       "cfprExtvmmFabricNetworkPolicyLevel": cfprExtvmmFabricNetworkPolicyLevel,
       "cfprExtvmmFabricNetworkPolicyOwner": cfprExtvmmFabricNetworkPolicyOwner,
       "cfprExtvmmFabricNetworkRefOperState": cfprExtvmmFabricNetworkRefOperState,
       "cfprExtvmmFabricNetworkDefinitionTable": cfprExtvmmFabricNetworkDefinitionTable,
       "cfprExtvmmFabricNetworkDefinitionEntry": cfprExtvmmFabricNetworkDefinitionEntry,
       "cfprExtvmmFabricNetworkDefinitionInstanceId": cfprExtvmmFabricNetworkDefinitionInstanceId,
       "cfprExtvmmFabricNetworkDefinitionDn": cfprExtvmmFabricNetworkDefinitionDn,
       "cfprExtvmmFabricNetworkDefinitionRn": cfprExtvmmFabricNetworkDefinitionRn,
       "cfprExtvmmFabricNetworkDefinitionAllowedVnicType": cfprExtvmmFabricNetworkDefinitionAllowedVnicType,
       "cfprExtvmmFabricNetworkDefinitionDescr": cfprExtvmmFabricNetworkDefinitionDescr,
       "cfprExtvmmFabricNetworkDefinitionGuid": cfprExtvmmFabricNetworkDefinitionGuid,
       "cfprExtvmmFabricNetworkDefinitionIntId": cfprExtvmmFabricNetworkDefinitionIntId,
       "cfprExtvmmFabricNetworkDefinitionName": cfprExtvmmFabricNetworkDefinitionName,
       "cfprExtvmmFabricNetworkDefinitionPolicyLevel": cfprExtvmmFabricNetworkDefinitionPolicyLevel,
       "cfprExtvmmFabricNetworkDefinitionPolicyOwner": cfprExtvmmFabricNetworkDefinitionPolicyOwner,
       "cfprExtvmmFabricNetworkDefinitionPrimaryVlanId": cfprExtvmmFabricNetworkDefinitionPrimaryVlanId,
       "cfprExtvmmFabricNetworkDefinitionRefOperState": cfprExtvmmFabricNetworkDefinitionRefOperState,
       "cfprExtvmmKeyInstTable": cfprExtvmmKeyInstTable,
       "cfprExtvmmKeyInstEntry": cfprExtvmmKeyInstEntry,
       "cfprExtvmmKeyInstInstanceId": cfprExtvmmKeyInstInstanceId,
       "cfprExtvmmKeyInstDn": cfprExtvmmKeyInstDn,
       "cfprExtvmmKeyInstRn": cfprExtvmmKeyInstRn,
       "cfprExtvmmKeyInstInst": cfprExtvmmKeyInstInst,
       "cfprExtvmmKeyInstKey": cfprExtvmmKeyInstKey,
       "cfprExtvmmKeyRingTable": cfprExtvmmKeyRingTable,
       "cfprExtvmmKeyRingEntry": cfprExtvmmKeyRingEntry,
       "cfprExtvmmKeyRingInstanceId": cfprExtvmmKeyRingInstanceId,
       "cfprExtvmmKeyRingDn": cfprExtvmmKeyRingDn,
       "cfprExtvmmKeyRingRn": cfprExtvmmKeyRingRn,
       "cfprExtvmmKeyRingCertFile": cfprExtvmmKeyRingCertFile,
       "cfprExtvmmKeyRingLocation": cfprExtvmmKeyRingLocation,
       "cfprExtvmmKeyRingName": cfprExtvmmKeyRingName,
       "cfprExtvmmKeyRingPath": cfprExtvmmKeyRingPath,
       "cfprExtvmmKeyStoreTable": cfprExtvmmKeyStoreTable,
       "cfprExtvmmKeyStoreEntry": cfprExtvmmKeyStoreEntry,
       "cfprExtvmmKeyStoreInstanceId": cfprExtvmmKeyStoreInstanceId,
       "cfprExtvmmKeyStoreDn": cfprExtvmmKeyStoreDn,
       "cfprExtvmmKeyStoreRn": cfprExtvmmKeyStoreRn,
       "cfprExtvmmKeyStoreFsmDescr": cfprExtvmmKeyStoreFsmDescr,
       "cfprExtvmmKeyStoreFsmPrev": cfprExtvmmKeyStoreFsmPrev,
       "cfprExtvmmKeyStoreFsmProgr": cfprExtvmmKeyStoreFsmProgr,
       "cfprExtvmmKeyStoreFsmRmtInvErrCode": cfprExtvmmKeyStoreFsmRmtInvErrCode,
       "cfprExtvmmKeyStoreFsmRmtInvErrDescr": cfprExtvmmKeyStoreFsmRmtInvErrDescr,
       "cfprExtvmmKeyStoreFsmRmtInvRslt": cfprExtvmmKeyStoreFsmRmtInvRslt,
       "cfprExtvmmKeyStoreFsmStageDescr": cfprExtvmmKeyStoreFsmStageDescr,
       "cfprExtvmmKeyStoreFsmStamp": cfprExtvmmKeyStoreFsmStamp,
       "cfprExtvmmKeyStoreFsmStatus": cfprExtvmmKeyStoreFsmStatus,
       "cfprExtvmmKeyStoreFsmTry": cfprExtvmmKeyStoreFsmTry,
       "cfprExtvmmKeyStoreFsmTable": cfprExtvmmKeyStoreFsmTable,
       "cfprExtvmmKeyStoreFsmEntry": cfprExtvmmKeyStoreFsmEntry,
       "cfprExtvmmKeyStoreFsmInstanceId": cfprExtvmmKeyStoreFsmInstanceId,
       "cfprExtvmmKeyStoreFsmDn": cfprExtvmmKeyStoreFsmDn,
       "cfprExtvmmKeyStoreFsmRn": cfprExtvmmKeyStoreFsmRn,
       "cfprExtvmmKeyStoreFsmCompletionTime": cfprExtvmmKeyStoreFsmCompletionTime,
       "cfprExtvmmKeyStoreFsmCurrentFsm": cfprExtvmmKeyStoreFsmCurrentFsm,
       "cfprExtvmmKeyStoreFsmDescrData": cfprExtvmmKeyStoreFsmDescrData,
       "cfprExtvmmKeyStoreFsmFsmStatus": cfprExtvmmKeyStoreFsmFsmStatus,
       "cfprExtvmmKeyStoreFsmProgress": cfprExtvmmKeyStoreFsmProgress,
       "cfprExtvmmKeyStoreFsmRmtErrCode": cfprExtvmmKeyStoreFsmRmtErrCode,
       "cfprExtvmmKeyStoreFsmRmtErrDescr": cfprExtvmmKeyStoreFsmRmtErrDescr,
       "cfprExtvmmKeyStoreFsmRmtRslt": cfprExtvmmKeyStoreFsmRmtRslt,
       "cfprExtvmmKeyStoreFsmStageTable": cfprExtvmmKeyStoreFsmStageTable,
       "cfprExtvmmKeyStoreFsmStageEntry": cfprExtvmmKeyStoreFsmStageEntry,
       "cfprExtvmmKeyStoreFsmStageInstanceId": cfprExtvmmKeyStoreFsmStageInstanceId,
       "cfprExtvmmKeyStoreFsmStageDn": cfprExtvmmKeyStoreFsmStageDn,
       "cfprExtvmmKeyStoreFsmStageRn": cfprExtvmmKeyStoreFsmStageRn,
       "cfprExtvmmKeyStoreFsmStageDescrData": cfprExtvmmKeyStoreFsmStageDescrData,
       "cfprExtvmmKeyStoreFsmStageLastUpdateTime": cfprExtvmmKeyStoreFsmStageLastUpdateTime,
       "cfprExtvmmKeyStoreFsmStageName": cfprExtvmmKeyStoreFsmStageName,
       "cfprExtvmmKeyStoreFsmStageOrder": cfprExtvmmKeyStoreFsmStageOrder,
       "cfprExtvmmKeyStoreFsmStageRetry": cfprExtvmmKeyStoreFsmStageRetry,
       "cfprExtvmmKeyStoreFsmStageStageStatus": cfprExtvmmKeyStoreFsmStageStageStatus,
       "cfprExtvmmKeyStoreFsmTaskTable": cfprExtvmmKeyStoreFsmTaskTable,
       "cfprExtvmmKeyStoreFsmTaskEntry": cfprExtvmmKeyStoreFsmTaskEntry,
       "cfprExtvmmKeyStoreFsmTaskInstanceId": cfprExtvmmKeyStoreFsmTaskInstanceId,
       "cfprExtvmmKeyStoreFsmTaskDn": cfprExtvmmKeyStoreFsmTaskDn,
       "cfprExtvmmKeyStoreFsmTaskRn": cfprExtvmmKeyStoreFsmTaskRn,
       "cfprExtvmmKeyStoreFsmTaskCompletion": cfprExtvmmKeyStoreFsmTaskCompletion,
       "cfprExtvmmKeyStoreFsmTaskFlags": cfprExtvmmKeyStoreFsmTaskFlags,
       "cfprExtvmmKeyStoreFsmTaskItem": cfprExtvmmKeyStoreFsmTaskItem,
       "cfprExtvmmKeyStoreFsmTaskSeqId": cfprExtvmmKeyStoreFsmTaskSeqId,
       "cfprExtvmmMasterExtKeyTable": cfprExtvmmMasterExtKeyTable,
       "cfprExtvmmMasterExtKeyEntry": cfprExtvmmMasterExtKeyEntry,
       "cfprExtvmmMasterExtKeyInstanceId": cfprExtvmmMasterExtKeyInstanceId,
       "cfprExtvmmMasterExtKeyDn": cfprExtvmmMasterExtKeyDn,
       "cfprExtvmmMasterExtKeyRn": cfprExtvmmMasterExtKeyRn,
       "cfprExtvmmMasterExtKeyFsmDescr": cfprExtvmmMasterExtKeyFsmDescr,
       "cfprExtvmmMasterExtKeyFsmPrev": cfprExtvmmMasterExtKeyFsmPrev,
       "cfprExtvmmMasterExtKeyFsmProgr": cfprExtvmmMasterExtKeyFsmProgr,
       "cfprExtvmmMasterExtKeyFsmRmtInvErrCode": cfprExtvmmMasterExtKeyFsmRmtInvErrCode,
       "cfprExtvmmMasterExtKeyFsmRmtInvErrDescr": cfprExtvmmMasterExtKeyFsmRmtInvErrDescr,
       "cfprExtvmmMasterExtKeyFsmRmtInvRslt": cfprExtvmmMasterExtKeyFsmRmtInvRslt,
       "cfprExtvmmMasterExtKeyFsmStageDescr": cfprExtvmmMasterExtKeyFsmStageDescr,
       "cfprExtvmmMasterExtKeyFsmStamp": cfprExtvmmMasterExtKeyFsmStamp,
       "cfprExtvmmMasterExtKeyFsmStatus": cfprExtvmmMasterExtKeyFsmStatus,
       "cfprExtvmmMasterExtKeyFsmTry": cfprExtvmmMasterExtKeyFsmTry,
       "cfprExtvmmMasterExtKeyKey": cfprExtvmmMasterExtKeyKey,
       "cfprExtvmmMasterExtKeyFsmTable": cfprExtvmmMasterExtKeyFsmTable,
       "cfprExtvmmMasterExtKeyFsmEntry": cfprExtvmmMasterExtKeyFsmEntry,
       "cfprExtvmmMasterExtKeyFsmInstanceId": cfprExtvmmMasterExtKeyFsmInstanceId,
       "cfprExtvmmMasterExtKeyFsmDn": cfprExtvmmMasterExtKeyFsmDn,
       "cfprExtvmmMasterExtKeyFsmRn": cfprExtvmmMasterExtKeyFsmRn,
       "cfprExtvmmMasterExtKeyFsmCompletionTime": cfprExtvmmMasterExtKeyFsmCompletionTime,
       "cfprExtvmmMasterExtKeyFsmCurrentFsm": cfprExtvmmMasterExtKeyFsmCurrentFsm,
       "cfprExtvmmMasterExtKeyFsmDescrData": cfprExtvmmMasterExtKeyFsmDescrData,
       "cfprExtvmmMasterExtKeyFsmFsmStatus": cfprExtvmmMasterExtKeyFsmFsmStatus,
       "cfprExtvmmMasterExtKeyFsmProgress": cfprExtvmmMasterExtKeyFsmProgress,
       "cfprExtvmmMasterExtKeyFsmRmtErrCode": cfprExtvmmMasterExtKeyFsmRmtErrCode,
       "cfprExtvmmMasterExtKeyFsmRmtErrDescr": cfprExtvmmMasterExtKeyFsmRmtErrDescr,
       "cfprExtvmmMasterExtKeyFsmRmtRslt": cfprExtvmmMasterExtKeyFsmRmtRslt,
       "cfprExtvmmMasterExtKeyFsmStageTable": cfprExtvmmMasterExtKeyFsmStageTable,
       "cfprExtvmmMasterExtKeyFsmStageEntry": cfprExtvmmMasterExtKeyFsmStageEntry,
       "cfprExtvmmMasterExtKeyFsmStageInstanceId": cfprExtvmmMasterExtKeyFsmStageInstanceId,
       "cfprExtvmmMasterExtKeyFsmStageDn": cfprExtvmmMasterExtKeyFsmStageDn,
       "cfprExtvmmMasterExtKeyFsmStageRn": cfprExtvmmMasterExtKeyFsmStageRn,
       "cfprExtvmmMasterExtKeyFsmStageDescrData": cfprExtvmmMasterExtKeyFsmStageDescrData,
       "cfprExtvmmMasterExtKeyFsmStageLastUpdateTime": cfprExtvmmMasterExtKeyFsmStageLastUpdateTime,
       "cfprExtvmmMasterExtKeyFsmStageName": cfprExtvmmMasterExtKeyFsmStageName,
       "cfprExtvmmMasterExtKeyFsmStageOrder": cfprExtvmmMasterExtKeyFsmStageOrder,
       "cfprExtvmmMasterExtKeyFsmStageRetry": cfprExtvmmMasterExtKeyFsmStageRetry,
       "cfprExtvmmMasterExtKeyFsmStageStageStatus": cfprExtvmmMasterExtKeyFsmStageStageStatus,
       "cfprExtvmmMasterExtKeyFsmTaskTable": cfprExtvmmMasterExtKeyFsmTaskTable,
       "cfprExtvmmMasterExtKeyFsmTaskEntry": cfprExtvmmMasterExtKeyFsmTaskEntry,
       "cfprExtvmmMasterExtKeyFsmTaskInstanceId": cfprExtvmmMasterExtKeyFsmTaskInstanceId,
       "cfprExtvmmMasterExtKeyFsmTaskDn": cfprExtvmmMasterExtKeyFsmTaskDn,
       "cfprExtvmmMasterExtKeyFsmTaskRn": cfprExtvmmMasterExtKeyFsmTaskRn,
       "cfprExtvmmMasterExtKeyFsmTaskCompletion": cfprExtvmmMasterExtKeyFsmTaskCompletion,
       "cfprExtvmmMasterExtKeyFsmTaskFlags": cfprExtvmmMasterExtKeyFsmTaskFlags,
       "cfprExtvmmMasterExtKeyFsmTaskItem": cfprExtvmmMasterExtKeyFsmTaskItem,
       "cfprExtvmmMasterExtKeyFsmTaskSeqId": cfprExtvmmMasterExtKeyFsmTaskSeqId,
       "cfprExtvmmNetworkSetsTable": cfprExtvmmNetworkSetsTable,
       "cfprExtvmmNetworkSetsEntry": cfprExtvmmNetworkSetsEntry,
       "cfprExtvmmNetworkSetsInstanceId": cfprExtvmmNetworkSetsInstanceId,
       "cfprExtvmmNetworkSetsDn": cfprExtvmmNetworkSetsDn,
       "cfprExtvmmNetworkSetsRn": cfprExtvmmNetworkSetsRn,
       "cfprExtvmmNetworkSetsFltAggr": cfprExtvmmNetworkSetsFltAggr,
       "cfprExtvmmNetworkSetsFsmDescr": cfprExtvmmNetworkSetsFsmDescr,
       "cfprExtvmmNetworkSetsFsmPrev": cfprExtvmmNetworkSetsFsmPrev,
       "cfprExtvmmNetworkSetsFsmProgr": cfprExtvmmNetworkSetsFsmProgr,
       "cfprExtvmmNetworkSetsFsmRmtInvErrCode": cfprExtvmmNetworkSetsFsmRmtInvErrCode,
       "cfprExtvmmNetworkSetsFsmRmtInvErrDescr": cfprExtvmmNetworkSetsFsmRmtInvErrDescr,
       "cfprExtvmmNetworkSetsFsmRmtInvRslt": cfprExtvmmNetworkSetsFsmRmtInvRslt,
       "cfprExtvmmNetworkSetsFsmStageDescr": cfprExtvmmNetworkSetsFsmStageDescr,
       "cfprExtvmmNetworkSetsFsmStamp": cfprExtvmmNetworkSetsFsmStamp,
       "cfprExtvmmNetworkSetsFsmStatus": cfprExtvmmNetworkSetsFsmStatus,
       "cfprExtvmmNetworkSetsFsmTry": cfprExtvmmNetworkSetsFsmTry,
       "cfprExtvmmNetworkSetsGenNum": cfprExtvmmNetworkSetsGenNum,
       "cfprExtvmmNetworkSetsFsmTable": cfprExtvmmNetworkSetsFsmTable,
       "cfprExtvmmNetworkSetsFsmEntry": cfprExtvmmNetworkSetsFsmEntry,
       "cfprExtvmmNetworkSetsFsmInstanceId": cfprExtvmmNetworkSetsFsmInstanceId,
       "cfprExtvmmNetworkSetsFsmDn": cfprExtvmmNetworkSetsFsmDn,
       "cfprExtvmmNetworkSetsFsmRn": cfprExtvmmNetworkSetsFsmRn,
       "cfprExtvmmNetworkSetsFsmCompletionTime": cfprExtvmmNetworkSetsFsmCompletionTime,
       "cfprExtvmmNetworkSetsFsmCurrentFsm": cfprExtvmmNetworkSetsFsmCurrentFsm,
       "cfprExtvmmNetworkSetsFsmDescrData": cfprExtvmmNetworkSetsFsmDescrData,
       "cfprExtvmmNetworkSetsFsmFsmStatus": cfprExtvmmNetworkSetsFsmFsmStatus,
       "cfprExtvmmNetworkSetsFsmProgress": cfprExtvmmNetworkSetsFsmProgress,
       "cfprExtvmmNetworkSetsFsmRmtErrCode": cfprExtvmmNetworkSetsFsmRmtErrCode,
       "cfprExtvmmNetworkSetsFsmRmtErrDescr": cfprExtvmmNetworkSetsFsmRmtErrDescr,
       "cfprExtvmmNetworkSetsFsmRmtRslt": cfprExtvmmNetworkSetsFsmRmtRslt,
       "cfprExtvmmNetworkSetsFsmStageTable": cfprExtvmmNetworkSetsFsmStageTable,
       "cfprExtvmmNetworkSetsFsmStageEntry": cfprExtvmmNetworkSetsFsmStageEntry,
       "cfprExtvmmNetworkSetsFsmStageInstanceId": cfprExtvmmNetworkSetsFsmStageInstanceId,
       "cfprExtvmmNetworkSetsFsmStageDn": cfprExtvmmNetworkSetsFsmStageDn,
       "cfprExtvmmNetworkSetsFsmStageRn": cfprExtvmmNetworkSetsFsmStageRn,
       "cfprExtvmmNetworkSetsFsmStageDescrData": cfprExtvmmNetworkSetsFsmStageDescrData,
       "cfprExtvmmNetworkSetsFsmStageLastUpdateTime": cfprExtvmmNetworkSetsFsmStageLastUpdateTime,
       "cfprExtvmmNetworkSetsFsmStageName": cfprExtvmmNetworkSetsFsmStageName,
       "cfprExtvmmNetworkSetsFsmStageOrder": cfprExtvmmNetworkSetsFsmStageOrder,
       "cfprExtvmmNetworkSetsFsmStageRetry": cfprExtvmmNetworkSetsFsmStageRetry,
       "cfprExtvmmNetworkSetsFsmStageStageStatus": cfprExtvmmNetworkSetsFsmStageStageStatus,
       "cfprExtvmmNetworkSetsFsmTaskTable": cfprExtvmmNetworkSetsFsmTaskTable,
       "cfprExtvmmNetworkSetsFsmTaskEntry": cfprExtvmmNetworkSetsFsmTaskEntry,
       "cfprExtvmmNetworkSetsFsmTaskInstanceId": cfprExtvmmNetworkSetsFsmTaskInstanceId,
       "cfprExtvmmNetworkSetsFsmTaskDn": cfprExtvmmNetworkSetsFsmTaskDn,
       "cfprExtvmmNetworkSetsFsmTaskRn": cfprExtvmmNetworkSetsFsmTaskRn,
       "cfprExtvmmNetworkSetsFsmTaskCompletion": cfprExtvmmNetworkSetsFsmTaskCompletion,
       "cfprExtvmmNetworkSetsFsmTaskFlags": cfprExtvmmNetworkSetsFsmTaskFlags,
       "cfprExtvmmNetworkSetsFsmTaskItem": cfprExtvmmNetworkSetsFsmTaskItem,
       "cfprExtvmmNetworkSetsFsmTaskSeqId": cfprExtvmmNetworkSetsFsmTaskSeqId,
       "cfprExtvmmProviderTable": cfprExtvmmProviderTable,
       "cfprExtvmmProviderEntry": cfprExtvmmProviderEntry,
       "cfprExtvmmProviderInstanceId": cfprExtvmmProviderInstanceId,
       "cfprExtvmmProviderDn": cfprExtvmmProviderDn,
       "cfprExtvmmProviderRn": cfprExtvmmProviderRn,
       "cfprExtvmmProviderCert": cfprExtvmmProviderCert,
       "cfprExtvmmProviderDescr": cfprExtvmmProviderDescr,
       "cfprExtvmmProviderFsmDescr": cfprExtvmmProviderFsmDescr,
       "cfprExtvmmProviderFsmPrev": cfprExtvmmProviderFsmPrev,
       "cfprExtvmmProviderFsmProgr": cfprExtvmmProviderFsmProgr,
       "cfprExtvmmProviderFsmRmtInvErrCode": cfprExtvmmProviderFsmRmtInvErrCode,
       "cfprExtvmmProviderFsmRmtInvErrDescr": cfprExtvmmProviderFsmRmtInvErrDescr,
       "cfprExtvmmProviderFsmRmtInvRslt": cfprExtvmmProviderFsmRmtInvRslt,
       "cfprExtvmmProviderFsmStageDescr": cfprExtvmmProviderFsmStageDescr,
       "cfprExtvmmProviderFsmStamp": cfprExtvmmProviderFsmStamp,
       "cfprExtvmmProviderFsmStatus": cfprExtvmmProviderFsmStatus,
       "cfprExtvmmProviderFsmTry": cfprExtvmmProviderFsmTry,
       "cfprExtvmmProviderHost": cfprExtvmmProviderHost,
       "cfprExtvmmProviderIntId": cfprExtvmmProviderIntId,
       "cfprExtvmmProviderKey": cfprExtvmmProviderKey,
       "cfprExtvmmProviderName": cfprExtvmmProviderName,
       "cfprExtvmmProviderPolicyLevel": cfprExtvmmProviderPolicyLevel,
       "cfprExtvmmProviderPolicyOwner": cfprExtvmmProviderPolicyOwner,
       "cfprExtvmmProviderPortValue": cfprExtvmmProviderPortValue,
       "cfprExtvmmProviderUuid": cfprExtvmmProviderUuid,
       "cfprExtvmmProviderVendorType": cfprExtvmmProviderVendorType,
       "cfprExtvmmProviderVer": cfprExtvmmProviderVer,
       "cfprExtvmmProviderVerRaw": cfprExtvmmProviderVerRaw,
       "cfprExtvmmProviderFsmTable": cfprExtvmmProviderFsmTable,
       "cfprExtvmmProviderFsmEntry": cfprExtvmmProviderFsmEntry,
       "cfprExtvmmProviderFsmInstanceId": cfprExtvmmProviderFsmInstanceId,
       "cfprExtvmmProviderFsmDn": cfprExtvmmProviderFsmDn,
       "cfprExtvmmProviderFsmRn": cfprExtvmmProviderFsmRn,
       "cfprExtvmmProviderFsmCompletionTime": cfprExtvmmProviderFsmCompletionTime,
       "cfprExtvmmProviderFsmCurrentFsm": cfprExtvmmProviderFsmCurrentFsm,
       "cfprExtvmmProviderFsmDescrData": cfprExtvmmProviderFsmDescrData,
       "cfprExtvmmProviderFsmFsmStatus": cfprExtvmmProviderFsmFsmStatus,
       "cfprExtvmmProviderFsmProgress": cfprExtvmmProviderFsmProgress,
       "cfprExtvmmProviderFsmRmtErrCode": cfprExtvmmProviderFsmRmtErrCode,
       "cfprExtvmmProviderFsmRmtErrDescr": cfprExtvmmProviderFsmRmtErrDescr,
       "cfprExtvmmProviderFsmRmtRslt": cfprExtvmmProviderFsmRmtRslt,
       "cfprExtvmmProviderFsmStageTable": cfprExtvmmProviderFsmStageTable,
       "cfprExtvmmProviderFsmStageEntry": cfprExtvmmProviderFsmStageEntry,
       "cfprExtvmmProviderFsmStageInstanceId": cfprExtvmmProviderFsmStageInstanceId,
       "cfprExtvmmProviderFsmStageDn": cfprExtvmmProviderFsmStageDn,
       "cfprExtvmmProviderFsmStageRn": cfprExtvmmProviderFsmStageRn,
       "cfprExtvmmProviderFsmStageDescrData": cfprExtvmmProviderFsmStageDescrData,
       "cfprExtvmmProviderFsmStageLastUpdateTime": cfprExtvmmProviderFsmStageLastUpdateTime,
       "cfprExtvmmProviderFsmStageName": cfprExtvmmProviderFsmStageName,
       "cfprExtvmmProviderFsmStageOrder": cfprExtvmmProviderFsmStageOrder,
       "cfprExtvmmProviderFsmStageRetry": cfprExtvmmProviderFsmStageRetry,
       "cfprExtvmmProviderFsmStageStageStatus": cfprExtvmmProviderFsmStageStageStatus,
       "cfprExtvmmProviderFsmTaskTable": cfprExtvmmProviderFsmTaskTable,
       "cfprExtvmmProviderFsmTaskEntry": cfprExtvmmProviderFsmTaskEntry,
       "cfprExtvmmProviderFsmTaskInstanceId": cfprExtvmmProviderFsmTaskInstanceId,
       "cfprExtvmmProviderFsmTaskDn": cfprExtvmmProviderFsmTaskDn,
       "cfprExtvmmProviderFsmTaskRn": cfprExtvmmProviderFsmTaskRn,
       "cfprExtvmmProviderFsmTaskCompletion": cfprExtvmmProviderFsmTaskCompletion,
       "cfprExtvmmProviderFsmTaskFlags": cfprExtvmmProviderFsmTaskFlags,
       "cfprExtvmmProviderFsmTaskItem": cfprExtvmmProviderFsmTaskItem,
       "cfprExtvmmProviderFsmTaskSeqId": cfprExtvmmProviderFsmTaskSeqId,
       "cfprExtvmmSwitchDelTaskTable": cfprExtvmmSwitchDelTaskTable,
       "cfprExtvmmSwitchDelTaskEntry": cfprExtvmmSwitchDelTaskEntry,
       "cfprExtvmmSwitchDelTaskInstanceId": cfprExtvmmSwitchDelTaskInstanceId,
       "cfprExtvmmSwitchDelTaskDn": cfprExtvmmSwitchDelTaskDn,
       "cfprExtvmmSwitchDelTaskRn": cfprExtvmmSwitchDelTaskRn,
       "cfprExtvmmSwitchDelTaskCertFile": cfprExtvmmSwitchDelTaskCertFile,
       "cfprExtvmmSwitchDelTaskDcName": cfprExtvmmSwitchDelTaskDcName,
       "cfprExtvmmSwitchDelTaskDcOrg": cfprExtvmmSwitchDelTaskDcOrg,
       "cfprExtvmmSwitchDelTaskDescr": cfprExtvmmSwitchDelTaskDescr,
       "cfprExtvmmSwitchDelTaskExtKey": cfprExtvmmSwitchDelTaskExtKey,
       "cfprExtvmmSwitchDelTaskFsmDescr": cfprExtvmmSwitchDelTaskFsmDescr,
       "cfprExtvmmSwitchDelTaskFsmPrev": cfprExtvmmSwitchDelTaskFsmPrev,
       "cfprExtvmmSwitchDelTaskFsmProgr": cfprExtvmmSwitchDelTaskFsmProgr,
       "cfprExtvmmSwitchDelTaskFsmRmtInvErrCode": cfprExtvmmSwitchDelTaskFsmRmtInvErrCode,
       "cfprExtvmmSwitchDelTaskFsmRmtInvErrDescr": cfprExtvmmSwitchDelTaskFsmRmtInvErrDescr,
       "cfprExtvmmSwitchDelTaskFsmRmtInvRslt": cfprExtvmmSwitchDelTaskFsmRmtInvRslt,
       "cfprExtvmmSwitchDelTaskFsmStageDescr": cfprExtvmmSwitchDelTaskFsmStageDescr,
       "cfprExtvmmSwitchDelTaskFsmStamp": cfprExtvmmSwitchDelTaskFsmStamp,
       "cfprExtvmmSwitchDelTaskFsmStatus": cfprExtvmmSwitchDelTaskFsmStatus,
       "cfprExtvmmSwitchDelTaskFsmTry": cfprExtvmmSwitchDelTaskFsmTry,
       "cfprExtvmmSwitchDelTaskHost": cfprExtvmmSwitchDelTaskHost,
       "cfprExtvmmSwitchDelTaskIntId": cfprExtvmmSwitchDelTaskIntId,
       "cfprExtvmmSwitchDelTaskKeyInst": cfprExtvmmSwitchDelTaskKeyInst,
       "cfprExtvmmSwitchDelTaskName": cfprExtvmmSwitchDelTaskName,
       "cfprExtvmmSwitchDelTaskOrgPath": cfprExtvmmSwitchDelTaskOrgPath,
       "cfprExtvmmSwitchDelTaskPolicyLevel": cfprExtvmmSwitchDelTaskPolicyLevel,
       "cfprExtvmmSwitchDelTaskPolicyOwner": cfprExtvmmSwitchDelTaskPolicyOwner,
       "cfprExtvmmSwitchDelTaskPortValue": cfprExtvmmSwitchDelTaskPortValue,
       "cfprExtvmmSwitchDelTaskProvIntId": cfprExtvmmSwitchDelTaskProvIntId,
       "cfprExtvmmSwitchDelTaskProvider": cfprExtvmmSwitchDelTaskProvider,
       "cfprExtvmmSwitchDelTaskSwIntId": cfprExtvmmSwitchDelTaskSwIntId,
       "cfprExtvmmSwitchDelTaskSwName": cfprExtvmmSwitchDelTaskSwName,
       "cfprExtvmmSwitchDelTaskFsmTable": cfprExtvmmSwitchDelTaskFsmTable,
       "cfprExtvmmSwitchDelTaskFsmEntry": cfprExtvmmSwitchDelTaskFsmEntry,
       "cfprExtvmmSwitchDelTaskFsmInstanceId": cfprExtvmmSwitchDelTaskFsmInstanceId,
       "cfprExtvmmSwitchDelTaskFsmDn": cfprExtvmmSwitchDelTaskFsmDn,
       "cfprExtvmmSwitchDelTaskFsmRn": cfprExtvmmSwitchDelTaskFsmRn,
       "cfprExtvmmSwitchDelTaskFsmCompletionTime": cfprExtvmmSwitchDelTaskFsmCompletionTime,
       "cfprExtvmmSwitchDelTaskFsmCurrentFsm": cfprExtvmmSwitchDelTaskFsmCurrentFsm,
       "cfprExtvmmSwitchDelTaskFsmDescrData": cfprExtvmmSwitchDelTaskFsmDescrData,
       "cfprExtvmmSwitchDelTaskFsmFsmStatus": cfprExtvmmSwitchDelTaskFsmFsmStatus,
       "cfprExtvmmSwitchDelTaskFsmProgress": cfprExtvmmSwitchDelTaskFsmProgress,
       "cfprExtvmmSwitchDelTaskFsmRmtErrCode": cfprExtvmmSwitchDelTaskFsmRmtErrCode,
       "cfprExtvmmSwitchDelTaskFsmRmtErrDescr": cfprExtvmmSwitchDelTaskFsmRmtErrDescr,
       "cfprExtvmmSwitchDelTaskFsmRmtRslt": cfprExtvmmSwitchDelTaskFsmRmtRslt,
       "cfprExtvmmSwitchDelTaskFsmStageTable": cfprExtvmmSwitchDelTaskFsmStageTable,
       "cfprExtvmmSwitchDelTaskFsmStageEntry": cfprExtvmmSwitchDelTaskFsmStageEntry,
       "cfprExtvmmSwitchDelTaskFsmStageInstanceId": cfprExtvmmSwitchDelTaskFsmStageInstanceId,
       "cfprExtvmmSwitchDelTaskFsmStageDn": cfprExtvmmSwitchDelTaskFsmStageDn,
       "cfprExtvmmSwitchDelTaskFsmStageRn": cfprExtvmmSwitchDelTaskFsmStageRn,
       "cfprExtvmmSwitchDelTaskFsmStageDescrData": cfprExtvmmSwitchDelTaskFsmStageDescrData,
       "cfprExtvmmSwitchDelTaskFsmStageLastUpdateTime": cfprExtvmmSwitchDelTaskFsmStageLastUpdateTime,
       "cfprExtvmmSwitchDelTaskFsmStageName": cfprExtvmmSwitchDelTaskFsmStageName,
       "cfprExtvmmSwitchDelTaskFsmStageOrder": cfprExtvmmSwitchDelTaskFsmStageOrder,
       "cfprExtvmmSwitchDelTaskFsmStageRetry": cfprExtvmmSwitchDelTaskFsmStageRetry,
       "cfprExtvmmSwitchDelTaskFsmStageStageStatus": cfprExtvmmSwitchDelTaskFsmStageStageStatus,
       "cfprExtvmmSwitchDelTaskFsmTaskTable": cfprExtvmmSwitchDelTaskFsmTaskTable,
       "cfprExtvmmSwitchDelTaskFsmTaskEntry": cfprExtvmmSwitchDelTaskFsmTaskEntry,
       "cfprExtvmmSwitchDelTaskFsmTaskInstanceId": cfprExtvmmSwitchDelTaskFsmTaskInstanceId,
       "cfprExtvmmSwitchDelTaskFsmTaskDn": cfprExtvmmSwitchDelTaskFsmTaskDn,
       "cfprExtvmmSwitchDelTaskFsmTaskRn": cfprExtvmmSwitchDelTaskFsmTaskRn,
       "cfprExtvmmSwitchDelTaskFsmTaskCompletion": cfprExtvmmSwitchDelTaskFsmTaskCompletion,
       "cfprExtvmmSwitchDelTaskFsmTaskFlags": cfprExtvmmSwitchDelTaskFsmTaskFlags,
       "cfprExtvmmSwitchDelTaskFsmTaskItem": cfprExtvmmSwitchDelTaskFsmTaskItem,
       "cfprExtvmmSwitchDelTaskFsmTaskSeqId": cfprExtvmmSwitchDelTaskFsmTaskSeqId,
       "cfprExtvmmSwitchSetTable": cfprExtvmmSwitchSetTable,
       "cfprExtvmmSwitchSetEntry": cfprExtvmmSwitchSetEntry,
       "cfprExtvmmSwitchSetInstanceId": cfprExtvmmSwitchSetInstanceId,
       "cfprExtvmmSwitchSetDn": cfprExtvmmSwitchSetDn,
       "cfprExtvmmSwitchSetRn": cfprExtvmmSwitchSetRn,
       "cfprExtvmmUpLinkPPTable": cfprExtvmmUpLinkPPTable,
       "cfprExtvmmUpLinkPPEntry": cfprExtvmmUpLinkPPEntry,
       "cfprExtvmmUpLinkPPInstanceId": cfprExtvmmUpLinkPPInstanceId,
       "cfprExtvmmUpLinkPPDn": cfprExtvmmUpLinkPPDn,
       "cfprExtvmmUpLinkPPRn": cfprExtvmmUpLinkPPRn,
       "cfprExtvmmUpLinkPPDescr": cfprExtvmmUpLinkPPDescr,
       "cfprExtvmmUpLinkPPFltAggr": cfprExtvmmUpLinkPPFltAggr,
       "cfprExtvmmUpLinkPPGuid": cfprExtvmmUpLinkPPGuid,
       "cfprExtvmmUpLinkPPIntId": cfprExtvmmUpLinkPPIntId,
       "cfprExtvmmUpLinkPPName": cfprExtvmmUpLinkPPName,
       "cfprExtvmmUpLinkPPPolicyLevel": cfprExtvmmUpLinkPPPolicyLevel,
       "cfprExtvmmUpLinkPPPolicyOwner": cfprExtvmmUpLinkPPPolicyOwner,
       "cfprExtvmmUpLinkPPRefOperState": cfprExtvmmUpLinkPPRefOperState,
       "cfprExtvmmVMNDRefTable": cfprExtvmmVMNDRefTable,
       "cfprExtvmmVMNDRefEntry": cfprExtvmmVMNDRefEntry,
       "cfprExtvmmVMNDRefInstanceId": cfprExtvmmVMNDRefInstanceId,
       "cfprExtvmmVMNDRefDn": cfprExtvmmVMNDRefDn,
       "cfprExtvmmVMNDRefRn": cfprExtvmmVMNDRefRn,
       "cfprExtvmmVMNDRefConfigQualifier": cfprExtvmmVMNDRefConfigQualifier,
       "cfprExtvmmVMNDRefDescr": cfprExtvmmVMNDRefDescr,
       "cfprExtvmmVMNDRefFnDefName": cfprExtvmmVMNDRefFnDefName,
       "cfprExtvmmVMNDRefFnName": cfprExtvmmVMNDRefFnName,
       "cfprExtvmmVMNDRefIntId": cfprExtvmmVMNDRefIntId,
       "cfprExtvmmVMNDRefName": cfprExtvmmVMNDRefName,
       "cfprExtvmmVMNDRefOperVmNetworkDefName": cfprExtvmmVMNDRefOperVmNetworkDefName,
       "cfprExtvmmVMNDRefPolicyLevel": cfprExtvmmVMNDRefPolicyLevel,
       "cfprExtvmmVMNDRefPolicyOwner": cfprExtvmmVMNDRefPolicyOwner,
       "cfprExtvmmVMNDRefVmNetworkDefName": cfprExtvmmVMNDRefVmNetworkDefName,
       "cfprExtvmmVMNetworkTable": cfprExtvmmVMNetworkTable,
       "cfprExtvmmVMNetworkEntry": cfprExtvmmVMNetworkEntry,
       "cfprExtvmmVMNetworkInstanceId": cfprExtvmmVMNetworkInstanceId,
       "cfprExtvmmVMNetworkDn": cfprExtvmmVMNetworkDn,
       "cfprExtvmmVMNetworkRn": cfprExtvmmVMNetworkRn,
       "cfprExtvmmVMNetworkDescr": cfprExtvmmVMNetworkDescr,
       "cfprExtvmmVMNetworkFabricNetworkName": cfprExtvmmVMNetworkFabricNetworkName,
       "cfprExtvmmVMNetworkFltAggr": cfprExtvmmVMNetworkFltAggr,
       "cfprExtvmmVMNetworkGuid": cfprExtvmmVMNetworkGuid,
       "cfprExtvmmVMNetworkIntId": cfprExtvmmVMNetworkIntId,
       "cfprExtvmmVMNetworkName": cfprExtvmmVMNetworkName,
       "cfprExtvmmVMNetworkOperFabricNetworkName": cfprExtvmmVMNetworkOperFabricNetworkName,
       "cfprExtvmmVMNetworkPolicyLevel": cfprExtvmmVMNetworkPolicyLevel,
       "cfprExtvmmVMNetworkPolicyOwner": cfprExtvmmVMNetworkPolicyOwner,
       "cfprExtvmmVMNetworkDefinitionTable": cfprExtvmmVMNetworkDefinitionTable,
       "cfprExtvmmVMNetworkDefinitionEntry": cfprExtvmmVMNetworkDefinitionEntry,
       "cfprExtvmmVMNetworkDefinitionInstanceId": cfprExtvmmVMNetworkDefinitionInstanceId,
       "cfprExtvmmVMNetworkDefinitionDn": cfprExtvmmVMNetworkDefinitionDn,
       "cfprExtvmmVMNetworkDefinitionRn": cfprExtvmmVMNetworkDefinitionRn,
       "cfprExtvmmVMNetworkDefinitionDescr": cfprExtvmmVMNetworkDefinitionDescr,
       "cfprExtvmmVMNetworkDefinitionExtIpPoolName": cfprExtvmmVMNetworkDefinitionExtIpPoolName,
       "cfprExtvmmVMNetworkDefinitionGuid": cfprExtvmmVMNetworkDefinitionGuid,
       "cfprExtvmmVMNetworkDefinitionIntId": cfprExtvmmVMNetworkDefinitionIntId,
       "cfprExtvmmVMNetworkDefinitionIpPoolGuid": cfprExtvmmVMNetworkDefinitionIpPoolGuid,
       "cfprExtvmmVMNetworkDefinitionMaxPorts": cfprExtvmmVMNetworkDefinitionMaxPorts,
       "cfprExtvmmVMNetworkDefinitionName": cfprExtvmmVMNetworkDefinitionName,
       "cfprExtvmmVMNetworkDefinitionOperExtIpPoolName": cfprExtvmmVMNetworkDefinitionOperExtIpPoolName,
       "cfprExtvmmVMNetworkDefinitionPolicyLevel": cfprExtvmmVMNetworkDefinitionPolicyLevel,
       "cfprExtvmmVMNetworkDefinitionPolicyOwner": cfprExtvmmVMNetworkDefinitionPolicyOwner,
       "cfprExtvmmVMNetworkDefinitionPrimaryVlanId": cfprExtvmmVMNetworkDefinitionPrimaryVlanId,
       "cfprExtvmmVMNetworkDefinitionRefOperState": cfprExtvmmVMNetworkDefinitionRefOperState,
       "cfprExtvmmVMNetworkDefinitionVlanName": cfprExtvmmVMNetworkDefinitionVlanName,
       "cfprExtvmmVMNetworkSetsTable": cfprExtvmmVMNetworkSetsTable,
       "cfprExtvmmVMNetworkSetsEntry": cfprExtvmmVMNetworkSetsEntry,
       "cfprExtvmmVMNetworkSetsInstanceId": cfprExtvmmVMNetworkSetsInstanceId,
       "cfprExtvmmVMNetworkSetsDn": cfprExtvmmVMNetworkSetsDn,
       "cfprExtvmmVMNetworkSetsRn": cfprExtvmmVMNetworkSetsRn,
       "cfprExtvmmVMNetworkSetsFltAggr": cfprExtvmmVMNetworkSetsFltAggr,
       "cfprExtvmmVMNetworkSetsGenNum": cfprExtvmmVMNetworkSetsGenNum}
)
