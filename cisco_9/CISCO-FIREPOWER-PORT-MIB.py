# SNMP MIB module (CISCO-FIREPOWER-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-PORT-MIB.mib
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
 CfprLicenseState,
 CfprNetworkConnectionType,
 CfprNetworkLocale,
 CfprNetworkPortRole,
 CfprNetworkPortType,
 CfprNetworkSwitchId,
 CfprNetworkTransport,
 CfprPortGroupType,
 CfprPortPIoFsmCurrentFsm,
 CfprPortPIoFsmStageName,
 CfprPortPIoFsmTaskItem,
 CfprPortSubGroupConfigState,
 CfprPortSubGroupSlotId,
 CfprPortTrust) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprLicenseState",
    "CfprNetworkConnectionType",
    "CfprNetworkLocale",
    "CfprNetworkPortRole",
    "CfprNetworkPortType",
    "CfprNetworkSwitchId",
    "CfprNetworkTransport",
    "CfprPortGroupType",
    "CfprPortPIoFsmCurrentFsm",
    "CfprPortPIoFsmStageName",
    "CfprPortPIoFsmTaskItem",
    "CfprPortSubGroupConfigState",
    "CfprPortSubGroupSlotId",
    "CfprPortTrust")

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

cfprPortObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprPortDomainEpTable_Object = MibTable
cfprPortDomainEpTable = _CfprPortDomainEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1)
)
if mibBuilder.loadTexts:
    cfprPortDomainEpTable.setStatus("current")
_CfprPortDomainEpEntry_Object = MibTableRow
cfprPortDomainEpEntry = _CfprPortDomainEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1)
)
cfprPortDomainEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PORT-MIB", "cfprPortDomainEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPortDomainEpEntry.setStatus("current")
_CfprPortDomainEpInstanceId_Type = CfprManagedObjectId
_CfprPortDomainEpInstanceId_Object = MibTableColumn
cfprPortDomainEpInstanceId = _CfprPortDomainEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 1),
    _CfprPortDomainEpInstanceId_Type()
)
cfprPortDomainEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPortDomainEpInstanceId.setStatus("current")
_CfprPortDomainEpDn_Type = CfprManagedObjectDn
_CfprPortDomainEpDn_Object = MibTableColumn
cfprPortDomainEpDn = _CfprPortDomainEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 2),
    _CfprPortDomainEpDn_Type()
)
cfprPortDomainEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpDn.setStatus("current")
_CfprPortDomainEpRn_Type = SnmpAdminString
_CfprPortDomainEpRn_Object = MibTableColumn
cfprPortDomainEpRn = _CfprPortDomainEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 3),
    _CfprPortDomainEpRn_Type()
)
cfprPortDomainEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpRn.setStatus("current")
_CfprPortDomainEpEpDn_Type = SnmpAdminString
_CfprPortDomainEpEpDn_Object = MibTableColumn
cfprPortDomainEpEpDn = _CfprPortDomainEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 4),
    _CfprPortDomainEpEpDn_Type()
)
cfprPortDomainEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpEpDn.setStatus("current")
_CfprPortDomainEpIfRole_Type = CfprNetworkPortRole
_CfprPortDomainEpIfRole_Object = MibTableColumn
cfprPortDomainEpIfRole = _CfprPortDomainEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 5),
    _CfprPortDomainEpIfRole_Type()
)
cfprPortDomainEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpIfRole.setStatus("current")
_CfprPortDomainEpIfType_Type = CfprNetworkPortType
_CfprPortDomainEpIfType_Object = MibTableColumn
cfprPortDomainEpIfType = _CfprPortDomainEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 6),
    _CfprPortDomainEpIfType_Type()
)
cfprPortDomainEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpIfType.setStatus("current")
_CfprPortDomainEpLocale_Type = CfprNetworkLocale
_CfprPortDomainEpLocale_Object = MibTableColumn
cfprPortDomainEpLocale = _CfprPortDomainEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 7),
    _CfprPortDomainEpLocale_Type()
)
cfprPortDomainEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpLocale.setStatus("current")
_CfprPortDomainEpName_Type = SnmpAdminString
_CfprPortDomainEpName_Object = MibTableColumn
cfprPortDomainEpName = _CfprPortDomainEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 8),
    _CfprPortDomainEpName_Type()
)
cfprPortDomainEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpName.setStatus("current")
_CfprPortDomainEpPeerDn_Type = SnmpAdminString
_CfprPortDomainEpPeerDn_Object = MibTableColumn
cfprPortDomainEpPeerDn = _CfprPortDomainEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 9),
    _CfprPortDomainEpPeerDn_Type()
)
cfprPortDomainEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpPeerDn.setStatus("current")
_CfprPortDomainEpTransport_Type = CfprNetworkTransport
_CfprPortDomainEpTransport_Object = MibTableColumn
cfprPortDomainEpTransport = _CfprPortDomainEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 10),
    _CfprPortDomainEpTransport_Type()
)
cfprPortDomainEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpTransport.setStatus("current")
_CfprPortDomainEpType_Type = CfprNetworkConnectionType
_CfprPortDomainEpType_Object = MibTableColumn
cfprPortDomainEpType = _CfprPortDomainEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 1, 1, 11),
    _CfprPortDomainEpType_Type()
)
cfprPortDomainEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortDomainEpType.setStatus("current")
_CfprPortGroupTable_Object = MibTable
cfprPortGroupTable = _CfprPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2)
)
if mibBuilder.loadTexts:
    cfprPortGroupTable.setStatus("current")
_CfprPortGroupEntry_Object = MibTableRow
cfprPortGroupEntry = _CfprPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2, 1)
)
cfprPortGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PORT-MIB", "cfprPortGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPortGroupEntry.setStatus("current")
_CfprPortGroupInstanceId_Type = CfprManagedObjectId
_CfprPortGroupInstanceId_Object = MibTableColumn
cfprPortGroupInstanceId = _CfprPortGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2, 1, 1),
    _CfprPortGroupInstanceId_Type()
)
cfprPortGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPortGroupInstanceId.setStatus("current")
_CfprPortGroupDn_Type = CfprManagedObjectDn
_CfprPortGroupDn_Object = MibTableColumn
cfprPortGroupDn = _CfprPortGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2, 1, 2),
    _CfprPortGroupDn_Type()
)
cfprPortGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortGroupDn.setStatus("current")
_CfprPortGroupRn_Type = SnmpAdminString
_CfprPortGroupRn_Object = MibTableColumn
cfprPortGroupRn = _CfprPortGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2, 1, 3),
    _CfprPortGroupRn_Type()
)
cfprPortGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortGroupRn.setStatus("current")
_CfprPortGroupLocale_Type = CfprNetworkLocale
_CfprPortGroupLocale_Object = MibTableColumn
cfprPortGroupLocale = _CfprPortGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2, 1, 4),
    _CfprPortGroupLocale_Type()
)
cfprPortGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortGroupLocale.setStatus("current")
_CfprPortGroupName_Type = SnmpAdminString
_CfprPortGroupName_Object = MibTableColumn
cfprPortGroupName = _CfprPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2, 1, 5),
    _CfprPortGroupName_Type()
)
cfprPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortGroupName.setStatus("current")
_CfprPortGroupTransport_Type = CfprNetworkTransport
_CfprPortGroupTransport_Object = MibTableColumn
cfprPortGroupTransport = _CfprPortGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2, 1, 6),
    _CfprPortGroupTransport_Type()
)
cfprPortGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortGroupTransport.setStatus("current")
_CfprPortGroupType_Type = CfprPortGroupType
_CfprPortGroupType_Object = MibTableColumn
cfprPortGroupType = _CfprPortGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 2, 1, 7),
    _CfprPortGroupType_Type()
)
cfprPortGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortGroupType.setStatus("current")
_CfprPortPIoFsmTable_Object = MibTable
cfprPortPIoFsmTable = _CfprPortPIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3)
)
if mibBuilder.loadTexts:
    cfprPortPIoFsmTable.setStatus("current")
_CfprPortPIoFsmEntry_Object = MibTableRow
cfprPortPIoFsmEntry = _CfprPortPIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1)
)
cfprPortPIoFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PORT-MIB", "cfprPortPIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPortPIoFsmEntry.setStatus("current")
_CfprPortPIoFsmInstanceId_Type = CfprManagedObjectId
_CfprPortPIoFsmInstanceId_Object = MibTableColumn
cfprPortPIoFsmInstanceId = _CfprPortPIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 1),
    _CfprPortPIoFsmInstanceId_Type()
)
cfprPortPIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPortPIoFsmInstanceId.setStatus("current")
_CfprPortPIoFsmDn_Type = CfprManagedObjectDn
_CfprPortPIoFsmDn_Object = MibTableColumn
cfprPortPIoFsmDn = _CfprPortPIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 2),
    _CfprPortPIoFsmDn_Type()
)
cfprPortPIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmDn.setStatus("current")
_CfprPortPIoFsmRn_Type = SnmpAdminString
_CfprPortPIoFsmRn_Object = MibTableColumn
cfprPortPIoFsmRn = _CfprPortPIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 3),
    _CfprPortPIoFsmRn_Type()
)
cfprPortPIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmRn.setStatus("current")
_CfprPortPIoFsmCompletionTime_Type = DateAndTime
_CfprPortPIoFsmCompletionTime_Object = MibTableColumn
cfprPortPIoFsmCompletionTime = _CfprPortPIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 4),
    _CfprPortPIoFsmCompletionTime_Type()
)
cfprPortPIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmCompletionTime.setStatus("current")
_CfprPortPIoFsmCurrentFsm_Type = CfprPortPIoFsmCurrentFsm
_CfprPortPIoFsmCurrentFsm_Object = MibTableColumn
cfprPortPIoFsmCurrentFsm = _CfprPortPIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 5),
    _CfprPortPIoFsmCurrentFsm_Type()
)
cfprPortPIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmCurrentFsm.setStatus("current")
_CfprPortPIoFsmDescr_Type = SnmpAdminString
_CfprPortPIoFsmDescr_Object = MibTableColumn
cfprPortPIoFsmDescr = _CfprPortPIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 6),
    _CfprPortPIoFsmDescr_Type()
)
cfprPortPIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmDescr.setStatus("current")
_CfprPortPIoFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprPortPIoFsmFsmStatus_Object = MibTableColumn
cfprPortPIoFsmFsmStatus = _CfprPortPIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 7),
    _CfprPortPIoFsmFsmStatus_Type()
)
cfprPortPIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmFsmStatus.setStatus("current")
_CfprPortPIoFsmProgress_Type = Gauge32
_CfprPortPIoFsmProgress_Object = MibTableColumn
cfprPortPIoFsmProgress = _CfprPortPIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 8),
    _CfprPortPIoFsmProgress_Type()
)
cfprPortPIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmProgress.setStatus("current")
_CfprPortPIoFsmRmtErrCode_Type = Gauge32
_CfprPortPIoFsmRmtErrCode_Object = MibTableColumn
cfprPortPIoFsmRmtErrCode = _CfprPortPIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 9),
    _CfprPortPIoFsmRmtErrCode_Type()
)
cfprPortPIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmRmtErrCode.setStatus("current")
_CfprPortPIoFsmRmtErrDescr_Type = SnmpAdminString
_CfprPortPIoFsmRmtErrDescr_Object = MibTableColumn
cfprPortPIoFsmRmtErrDescr = _CfprPortPIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 10),
    _CfprPortPIoFsmRmtErrDescr_Type()
)
cfprPortPIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmRmtErrDescr.setStatus("current")
_CfprPortPIoFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprPortPIoFsmRmtRslt_Object = MibTableColumn
cfprPortPIoFsmRmtRslt = _CfprPortPIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 3, 1, 11),
    _CfprPortPIoFsmRmtRslt_Type()
)
cfprPortPIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmRmtRslt.setStatus("current")
_CfprPortPIoFsmStageTable_Object = MibTable
cfprPortPIoFsmStageTable = _CfprPortPIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4)
)
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageTable.setStatus("current")
_CfprPortPIoFsmStageEntry_Object = MibTableRow
cfprPortPIoFsmStageEntry = _CfprPortPIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1)
)
cfprPortPIoFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PORT-MIB", "cfprPortPIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageEntry.setStatus("current")
_CfprPortPIoFsmStageInstanceId_Type = CfprManagedObjectId
_CfprPortPIoFsmStageInstanceId_Object = MibTableColumn
cfprPortPIoFsmStageInstanceId = _CfprPortPIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 1),
    _CfprPortPIoFsmStageInstanceId_Type()
)
cfprPortPIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageInstanceId.setStatus("current")
_CfprPortPIoFsmStageDn_Type = CfprManagedObjectDn
_CfprPortPIoFsmStageDn_Object = MibTableColumn
cfprPortPIoFsmStageDn = _CfprPortPIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 2),
    _CfprPortPIoFsmStageDn_Type()
)
cfprPortPIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageDn.setStatus("current")
_CfprPortPIoFsmStageRn_Type = SnmpAdminString
_CfprPortPIoFsmStageRn_Object = MibTableColumn
cfprPortPIoFsmStageRn = _CfprPortPIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 3),
    _CfprPortPIoFsmStageRn_Type()
)
cfprPortPIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageRn.setStatus("current")
_CfprPortPIoFsmStageDescr_Type = SnmpAdminString
_CfprPortPIoFsmStageDescr_Object = MibTableColumn
cfprPortPIoFsmStageDescr = _CfprPortPIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 4),
    _CfprPortPIoFsmStageDescr_Type()
)
cfprPortPIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageDescr.setStatus("current")
_CfprPortPIoFsmStageLastUpdateTime_Type = DateAndTime
_CfprPortPIoFsmStageLastUpdateTime_Object = MibTableColumn
cfprPortPIoFsmStageLastUpdateTime = _CfprPortPIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 5),
    _CfprPortPIoFsmStageLastUpdateTime_Type()
)
cfprPortPIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageLastUpdateTime.setStatus("current")
_CfprPortPIoFsmStageName_Type = CfprPortPIoFsmStageName
_CfprPortPIoFsmStageName_Object = MibTableColumn
cfprPortPIoFsmStageName = _CfprPortPIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 6),
    _CfprPortPIoFsmStageName_Type()
)
cfprPortPIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageName.setStatus("current")
_CfprPortPIoFsmStageOrder_Type = Gauge32
_CfprPortPIoFsmStageOrder_Object = MibTableColumn
cfprPortPIoFsmStageOrder = _CfprPortPIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 7),
    _CfprPortPIoFsmStageOrder_Type()
)
cfprPortPIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageOrder.setStatus("current")
_CfprPortPIoFsmStageRetry_Type = Gauge32
_CfprPortPIoFsmStageRetry_Object = MibTableColumn
cfprPortPIoFsmStageRetry = _CfprPortPIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 8),
    _CfprPortPIoFsmStageRetry_Type()
)
cfprPortPIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageRetry.setStatus("current")
_CfprPortPIoFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprPortPIoFsmStageStageStatus_Object = MibTableColumn
cfprPortPIoFsmStageStageStatus = _CfprPortPIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 4, 1, 9),
    _CfprPortPIoFsmStageStageStatus_Type()
)
cfprPortPIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmStageStageStatus.setStatus("current")
_CfprPortPIoFsmTaskTable_Object = MibTable
cfprPortPIoFsmTaskTable = _CfprPortPIoFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5)
)
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskTable.setStatus("current")
_CfprPortPIoFsmTaskEntry_Object = MibTableRow
cfprPortPIoFsmTaskEntry = _CfprPortPIoFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5, 1)
)
cfprPortPIoFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PORT-MIB", "cfprPortPIoFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskEntry.setStatus("current")
_CfprPortPIoFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprPortPIoFsmTaskInstanceId_Object = MibTableColumn
cfprPortPIoFsmTaskInstanceId = _CfprPortPIoFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5, 1, 1),
    _CfprPortPIoFsmTaskInstanceId_Type()
)
cfprPortPIoFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskInstanceId.setStatus("current")
_CfprPortPIoFsmTaskDn_Type = CfprManagedObjectDn
_CfprPortPIoFsmTaskDn_Object = MibTableColumn
cfprPortPIoFsmTaskDn = _CfprPortPIoFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5, 1, 2),
    _CfprPortPIoFsmTaskDn_Type()
)
cfprPortPIoFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskDn.setStatus("current")
_CfprPortPIoFsmTaskRn_Type = SnmpAdminString
_CfprPortPIoFsmTaskRn_Object = MibTableColumn
cfprPortPIoFsmTaskRn = _CfprPortPIoFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5, 1, 3),
    _CfprPortPIoFsmTaskRn_Type()
)
cfprPortPIoFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskRn.setStatus("current")
_CfprPortPIoFsmTaskCompletion_Type = CfprFsmCompletion
_CfprPortPIoFsmTaskCompletion_Object = MibTableColumn
cfprPortPIoFsmTaskCompletion = _CfprPortPIoFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5, 1, 4),
    _CfprPortPIoFsmTaskCompletion_Type()
)
cfprPortPIoFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskCompletion.setStatus("current")
_CfprPortPIoFsmTaskFlags_Type = CfprFsmFlags
_CfprPortPIoFsmTaskFlags_Object = MibTableColumn
cfprPortPIoFsmTaskFlags = _CfprPortPIoFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5, 1, 5),
    _CfprPortPIoFsmTaskFlags_Type()
)
cfprPortPIoFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskFlags.setStatus("current")
_CfprPortPIoFsmTaskItem_Type = CfprPortPIoFsmTaskItem
_CfprPortPIoFsmTaskItem_Object = MibTableColumn
cfprPortPIoFsmTaskItem = _CfprPortPIoFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5, 1, 6),
    _CfprPortPIoFsmTaskItem_Type()
)
cfprPortPIoFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskItem.setStatus("current")
_CfprPortPIoFsmTaskSeqId_Type = Gauge32
_CfprPortPIoFsmTaskSeqId_Object = MibTableColumn
cfprPortPIoFsmTaskSeqId = _CfprPortPIoFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 5, 1, 7),
    _CfprPortPIoFsmTaskSeqId_Type()
)
cfprPortPIoFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortPIoFsmTaskSeqId.setStatus("current")
_CfprPortSubGroupTable_Object = MibTable
cfprPortSubGroupTable = _CfprPortSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6)
)
if mibBuilder.loadTexts:
    cfprPortSubGroupTable.setStatus("current")
_CfprPortSubGroupEntry_Object = MibTableRow
cfprPortSubGroupEntry = _CfprPortSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1)
)
cfprPortSubGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PORT-MIB", "cfprPortSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPortSubGroupEntry.setStatus("current")
_CfprPortSubGroupInstanceId_Type = CfprManagedObjectId
_CfprPortSubGroupInstanceId_Object = MibTableColumn
cfprPortSubGroupInstanceId = _CfprPortSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 1),
    _CfprPortSubGroupInstanceId_Type()
)
cfprPortSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPortSubGroupInstanceId.setStatus("current")
_CfprPortSubGroupDn_Type = CfprManagedObjectDn
_CfprPortSubGroupDn_Object = MibTableColumn
cfprPortSubGroupDn = _CfprPortSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 2),
    _CfprPortSubGroupDn_Type()
)
cfprPortSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupDn.setStatus("current")
_CfprPortSubGroupRn_Type = SnmpAdminString
_CfprPortSubGroupRn_Object = MibTableColumn
cfprPortSubGroupRn = _CfprPortSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 3),
    _CfprPortSubGroupRn_Type()
)
cfprPortSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupRn.setStatus("current")
_CfprPortSubGroupAggrPortId_Type = Gauge32
_CfprPortSubGroupAggrPortId_Object = MibTableColumn
cfprPortSubGroupAggrPortId = _CfprPortSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 4),
    _CfprPortSubGroupAggrPortId_Type()
)
cfprPortSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupAggrPortId.setStatus("current")
_CfprPortSubGroupConfigState_Type = CfprPortSubGroupConfigState
_CfprPortSubGroupConfigState_Object = MibTableColumn
cfprPortSubGroupConfigState = _CfprPortSubGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 5),
    _CfprPortSubGroupConfigState_Type()
)
cfprPortSubGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupConfigState.setStatus("current")
_CfprPortSubGroupLicGP_Type = Unsigned64
_CfprPortSubGroupLicGP_Object = MibTableColumn
cfprPortSubGroupLicGP = _CfprPortSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 6),
    _CfprPortSubGroupLicGP_Type()
)
cfprPortSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupLicGP.setStatus("current")
_CfprPortSubGroupLicState_Type = CfprLicenseState
_CfprPortSubGroupLicState_Object = MibTableColumn
cfprPortSubGroupLicState = _CfprPortSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 7),
    _CfprPortSubGroupLicState_Type()
)
cfprPortSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupLicState.setStatus("current")
_CfprPortSubGroupLocale_Type = CfprNetworkLocale
_CfprPortSubGroupLocale_Object = MibTableColumn
cfprPortSubGroupLocale = _CfprPortSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 8),
    _CfprPortSubGroupLocale_Type()
)
cfprPortSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupLocale.setStatus("current")
_CfprPortSubGroupName_Type = SnmpAdminString
_CfprPortSubGroupName_Object = MibTableColumn
cfprPortSubGroupName = _CfprPortSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 9),
    _CfprPortSubGroupName_Type()
)
cfprPortSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupName.setStatus("current")
_CfprPortSubGroupSlotId_Type = CfprPortSubGroupSlotId
_CfprPortSubGroupSlotId_Object = MibTableColumn
cfprPortSubGroupSlotId = _CfprPortSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 10),
    _CfprPortSubGroupSlotId_Type()
)
cfprPortSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupSlotId.setStatus("current")
_CfprPortSubGroupSwitchId_Type = CfprNetworkSwitchId
_CfprPortSubGroupSwitchId_Object = MibTableColumn
cfprPortSubGroupSwitchId = _CfprPortSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 11),
    _CfprPortSubGroupSwitchId_Type()
)
cfprPortSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupSwitchId.setStatus("current")
_CfprPortSubGroupTransport_Type = CfprNetworkTransport
_CfprPortSubGroupTransport_Object = MibTableColumn
cfprPortSubGroupTransport = _CfprPortSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 12),
    _CfprPortSubGroupTransport_Type()
)
cfprPortSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupTransport.setStatus("current")
_CfprPortSubGroupType_Type = CfprNetworkConnectionType
_CfprPortSubGroupType_Object = MibTableColumn
cfprPortSubGroupType = _CfprPortSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 6, 1, 13),
    _CfprPortSubGroupType_Type()
)
cfprPortSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortSubGroupType.setStatus("current")
_CfprPortTrustModeTable_Object = MibTable
cfprPortTrustModeTable = _CfprPortTrustModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 7)
)
if mibBuilder.loadTexts:
    cfprPortTrustModeTable.setStatus("current")
_CfprPortTrustModeEntry_Object = MibTableRow
cfprPortTrustModeEntry = _CfprPortTrustModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 7, 1)
)
cfprPortTrustModeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PORT-MIB", "cfprPortTrustModeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPortTrustModeEntry.setStatus("current")
_CfprPortTrustModeInstanceId_Type = CfprManagedObjectId
_CfprPortTrustModeInstanceId_Object = MibTableColumn
cfprPortTrustModeInstanceId = _CfprPortTrustModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 7, 1, 1),
    _CfprPortTrustModeInstanceId_Type()
)
cfprPortTrustModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPortTrustModeInstanceId.setStatus("current")
_CfprPortTrustModeDn_Type = CfprManagedObjectDn
_CfprPortTrustModeDn_Object = MibTableColumn
cfprPortTrustModeDn = _CfprPortTrustModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 7, 1, 2),
    _CfprPortTrustModeDn_Type()
)
cfprPortTrustModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortTrustModeDn.setStatus("current")
_CfprPortTrustModeRn_Type = SnmpAdminString
_CfprPortTrustModeRn_Object = MibTableColumn
cfprPortTrustModeRn = _CfprPortTrustModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 7, 1, 3),
    _CfprPortTrustModeRn_Type()
)
cfprPortTrustModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortTrustModeRn.setStatus("current")
_CfprPortTrustModeState_Type = CfprPortTrust
_CfprPortTrustModeState_Object = MibTableColumn
cfprPortTrustModeState = _CfprPortTrustModeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 63, 7, 1, 4),
    _CfprPortTrustModeState_Type()
)
cfprPortTrustModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPortTrustModeState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-PORT-MIB",
    **{"cfprPortObjects": cfprPortObjects,
       "cfprPortDomainEpTable": cfprPortDomainEpTable,
       "cfprPortDomainEpEntry": cfprPortDomainEpEntry,
       "cfprPortDomainEpInstanceId": cfprPortDomainEpInstanceId,
       "cfprPortDomainEpDn": cfprPortDomainEpDn,
       "cfprPortDomainEpRn": cfprPortDomainEpRn,
       "cfprPortDomainEpEpDn": cfprPortDomainEpEpDn,
       "cfprPortDomainEpIfRole": cfprPortDomainEpIfRole,
       "cfprPortDomainEpIfType": cfprPortDomainEpIfType,
       "cfprPortDomainEpLocale": cfprPortDomainEpLocale,
       "cfprPortDomainEpName": cfprPortDomainEpName,
       "cfprPortDomainEpPeerDn": cfprPortDomainEpPeerDn,
       "cfprPortDomainEpTransport": cfprPortDomainEpTransport,
       "cfprPortDomainEpType": cfprPortDomainEpType,
       "cfprPortGroupTable": cfprPortGroupTable,
       "cfprPortGroupEntry": cfprPortGroupEntry,
       "cfprPortGroupInstanceId": cfprPortGroupInstanceId,
       "cfprPortGroupDn": cfprPortGroupDn,
       "cfprPortGroupRn": cfprPortGroupRn,
       "cfprPortGroupLocale": cfprPortGroupLocale,
       "cfprPortGroupName": cfprPortGroupName,
       "cfprPortGroupTransport": cfprPortGroupTransport,
       "cfprPortGroupType": cfprPortGroupType,
       "cfprPortPIoFsmTable": cfprPortPIoFsmTable,
       "cfprPortPIoFsmEntry": cfprPortPIoFsmEntry,
       "cfprPortPIoFsmInstanceId": cfprPortPIoFsmInstanceId,
       "cfprPortPIoFsmDn": cfprPortPIoFsmDn,
       "cfprPortPIoFsmRn": cfprPortPIoFsmRn,
       "cfprPortPIoFsmCompletionTime": cfprPortPIoFsmCompletionTime,
       "cfprPortPIoFsmCurrentFsm": cfprPortPIoFsmCurrentFsm,
       "cfprPortPIoFsmDescr": cfprPortPIoFsmDescr,
       "cfprPortPIoFsmFsmStatus": cfprPortPIoFsmFsmStatus,
       "cfprPortPIoFsmProgress": cfprPortPIoFsmProgress,
       "cfprPortPIoFsmRmtErrCode": cfprPortPIoFsmRmtErrCode,
       "cfprPortPIoFsmRmtErrDescr": cfprPortPIoFsmRmtErrDescr,
       "cfprPortPIoFsmRmtRslt": cfprPortPIoFsmRmtRslt,
       "cfprPortPIoFsmStageTable": cfprPortPIoFsmStageTable,
       "cfprPortPIoFsmStageEntry": cfprPortPIoFsmStageEntry,
       "cfprPortPIoFsmStageInstanceId": cfprPortPIoFsmStageInstanceId,
       "cfprPortPIoFsmStageDn": cfprPortPIoFsmStageDn,
       "cfprPortPIoFsmStageRn": cfprPortPIoFsmStageRn,
       "cfprPortPIoFsmStageDescr": cfprPortPIoFsmStageDescr,
       "cfprPortPIoFsmStageLastUpdateTime": cfprPortPIoFsmStageLastUpdateTime,
       "cfprPortPIoFsmStageName": cfprPortPIoFsmStageName,
       "cfprPortPIoFsmStageOrder": cfprPortPIoFsmStageOrder,
       "cfprPortPIoFsmStageRetry": cfprPortPIoFsmStageRetry,
       "cfprPortPIoFsmStageStageStatus": cfprPortPIoFsmStageStageStatus,
       "cfprPortPIoFsmTaskTable": cfprPortPIoFsmTaskTable,
       "cfprPortPIoFsmTaskEntry": cfprPortPIoFsmTaskEntry,
       "cfprPortPIoFsmTaskInstanceId": cfprPortPIoFsmTaskInstanceId,
       "cfprPortPIoFsmTaskDn": cfprPortPIoFsmTaskDn,
       "cfprPortPIoFsmTaskRn": cfprPortPIoFsmTaskRn,
       "cfprPortPIoFsmTaskCompletion": cfprPortPIoFsmTaskCompletion,
       "cfprPortPIoFsmTaskFlags": cfprPortPIoFsmTaskFlags,
       "cfprPortPIoFsmTaskItem": cfprPortPIoFsmTaskItem,
       "cfprPortPIoFsmTaskSeqId": cfprPortPIoFsmTaskSeqId,
       "cfprPortSubGroupTable": cfprPortSubGroupTable,
       "cfprPortSubGroupEntry": cfprPortSubGroupEntry,
       "cfprPortSubGroupInstanceId": cfprPortSubGroupInstanceId,
       "cfprPortSubGroupDn": cfprPortSubGroupDn,
       "cfprPortSubGroupRn": cfprPortSubGroupRn,
       "cfprPortSubGroupAggrPortId": cfprPortSubGroupAggrPortId,
       "cfprPortSubGroupConfigState": cfprPortSubGroupConfigState,
       "cfprPortSubGroupLicGP": cfprPortSubGroupLicGP,
       "cfprPortSubGroupLicState": cfprPortSubGroupLicState,
       "cfprPortSubGroupLocale": cfprPortSubGroupLocale,
       "cfprPortSubGroupName": cfprPortSubGroupName,
       "cfprPortSubGroupSlotId": cfprPortSubGroupSlotId,
       "cfprPortSubGroupSwitchId": cfprPortSubGroupSwitchId,
       "cfprPortSubGroupTransport": cfprPortSubGroupTransport,
       "cfprPortSubGroupType": cfprPortSubGroupType,
       "cfprPortTrustModeTable": cfprPortTrustModeTable,
       "cfprPortTrustModeEntry": cfprPortTrustModeEntry,
       "cfprPortTrustModeInstanceId": cfprPortTrustModeInstanceId,
       "cfprPortTrustModeDn": cfprPortTrustModeDn,
       "cfprPortTrustModeRn": cfprPortTrustModeRn,
       "cfprPortTrustModeState": cfprPortTrustModeState}
)
