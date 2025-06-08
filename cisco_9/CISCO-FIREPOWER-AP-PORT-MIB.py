# SNMP MIB module (CISCO-FIREPOWER-AP-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-PORT-MIB.mib
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

(CfprApConditionRemoteInvRslt,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApLicenseState,
 CfprApNetworkConnectionType,
 CfprApNetworkLocale,
 CfprApNetworkPortRole,
 CfprApNetworkPortType,
 CfprApNetworkSwitchId,
 CfprApNetworkTransport,
 CfprApPortGroupType,
 CfprApPortPIoFsmCurrentFsm,
 CfprApPortPIoFsmStageName,
 CfprApPortPIoFsmTaskItem,
 CfprApPortSubGroupConfigState,
 CfprApPortSubGroupSlotId,
 CfprApPortTrust) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApLicenseState",
    "CfprApNetworkConnectionType",
    "CfprApNetworkLocale",
    "CfprApNetworkPortRole",
    "CfprApNetworkPortType",
    "CfprApNetworkSwitchId",
    "CfprApNetworkTransport",
    "CfprApPortGroupType",
    "CfprApPortPIoFsmCurrentFsm",
    "CfprApPortPIoFsmStageName",
    "CfprApPortPIoFsmTaskItem",
    "CfprApPortSubGroupConfigState",
    "CfprApPortSubGroupSlotId",
    "CfprApPortTrust")

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

cfprApPortObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApPortDomainEpTable_Object = MibTable
cfprApPortDomainEpTable = _CfprApPortDomainEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1)
)
if mibBuilder.loadTexts:
    cfprApPortDomainEpTable.setStatus("current")
_CfprApPortDomainEpEntry_Object = MibTableRow
cfprApPortDomainEpEntry = _CfprApPortDomainEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1)
)
cfprApPortDomainEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PORT-MIB", "cfprApPortDomainEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPortDomainEpEntry.setStatus("current")
_CfprApPortDomainEpInstanceId_Type = CfprApManagedObjectId
_CfprApPortDomainEpInstanceId_Object = MibTableColumn
cfprApPortDomainEpInstanceId = _CfprApPortDomainEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 1),
    _CfprApPortDomainEpInstanceId_Type()
)
cfprApPortDomainEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPortDomainEpInstanceId.setStatus("current")
_CfprApPortDomainEpDn_Type = CfprApManagedObjectDn
_CfprApPortDomainEpDn_Object = MibTableColumn
cfprApPortDomainEpDn = _CfprApPortDomainEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 2),
    _CfprApPortDomainEpDn_Type()
)
cfprApPortDomainEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpDn.setStatus("current")
_CfprApPortDomainEpRn_Type = SnmpAdminString
_CfprApPortDomainEpRn_Object = MibTableColumn
cfprApPortDomainEpRn = _CfprApPortDomainEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 3),
    _CfprApPortDomainEpRn_Type()
)
cfprApPortDomainEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpRn.setStatus("current")
_CfprApPortDomainEpEpDn_Type = SnmpAdminString
_CfprApPortDomainEpEpDn_Object = MibTableColumn
cfprApPortDomainEpEpDn = _CfprApPortDomainEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 4),
    _CfprApPortDomainEpEpDn_Type()
)
cfprApPortDomainEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpEpDn.setStatus("current")
_CfprApPortDomainEpIfRole_Type = CfprApNetworkPortRole
_CfprApPortDomainEpIfRole_Object = MibTableColumn
cfprApPortDomainEpIfRole = _CfprApPortDomainEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 5),
    _CfprApPortDomainEpIfRole_Type()
)
cfprApPortDomainEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpIfRole.setStatus("current")
_CfprApPortDomainEpIfType_Type = CfprApNetworkPortType
_CfprApPortDomainEpIfType_Object = MibTableColumn
cfprApPortDomainEpIfType = _CfprApPortDomainEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 6),
    _CfprApPortDomainEpIfType_Type()
)
cfprApPortDomainEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpIfType.setStatus("current")
_CfprApPortDomainEpLocale_Type = CfprApNetworkLocale
_CfprApPortDomainEpLocale_Object = MibTableColumn
cfprApPortDomainEpLocale = _CfprApPortDomainEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 7),
    _CfprApPortDomainEpLocale_Type()
)
cfprApPortDomainEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpLocale.setStatus("current")
_CfprApPortDomainEpName_Type = SnmpAdminString
_CfprApPortDomainEpName_Object = MibTableColumn
cfprApPortDomainEpName = _CfprApPortDomainEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 8),
    _CfprApPortDomainEpName_Type()
)
cfprApPortDomainEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpName.setStatus("current")
_CfprApPortDomainEpPeerDn_Type = SnmpAdminString
_CfprApPortDomainEpPeerDn_Object = MibTableColumn
cfprApPortDomainEpPeerDn = _CfprApPortDomainEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 9),
    _CfprApPortDomainEpPeerDn_Type()
)
cfprApPortDomainEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpPeerDn.setStatus("current")
_CfprApPortDomainEpTransport_Type = CfprApNetworkTransport
_CfprApPortDomainEpTransport_Object = MibTableColumn
cfprApPortDomainEpTransport = _CfprApPortDomainEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 10),
    _CfprApPortDomainEpTransport_Type()
)
cfprApPortDomainEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpTransport.setStatus("current")
_CfprApPortDomainEpType_Type = CfprApNetworkConnectionType
_CfprApPortDomainEpType_Object = MibTableColumn
cfprApPortDomainEpType = _CfprApPortDomainEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 1, 1, 11),
    _CfprApPortDomainEpType_Type()
)
cfprApPortDomainEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortDomainEpType.setStatus("current")
_CfprApPortGroupTable_Object = MibTable
cfprApPortGroupTable = _CfprApPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2)
)
if mibBuilder.loadTexts:
    cfprApPortGroupTable.setStatus("current")
_CfprApPortGroupEntry_Object = MibTableRow
cfprApPortGroupEntry = _CfprApPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2, 1)
)
cfprApPortGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PORT-MIB", "cfprApPortGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPortGroupEntry.setStatus("current")
_CfprApPortGroupInstanceId_Type = CfprApManagedObjectId
_CfprApPortGroupInstanceId_Object = MibTableColumn
cfprApPortGroupInstanceId = _CfprApPortGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2, 1, 1),
    _CfprApPortGroupInstanceId_Type()
)
cfprApPortGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPortGroupInstanceId.setStatus("current")
_CfprApPortGroupDn_Type = CfprApManagedObjectDn
_CfprApPortGroupDn_Object = MibTableColumn
cfprApPortGroupDn = _CfprApPortGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2, 1, 2),
    _CfprApPortGroupDn_Type()
)
cfprApPortGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortGroupDn.setStatus("current")
_CfprApPortGroupRn_Type = SnmpAdminString
_CfprApPortGroupRn_Object = MibTableColumn
cfprApPortGroupRn = _CfprApPortGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2, 1, 3),
    _CfprApPortGroupRn_Type()
)
cfprApPortGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortGroupRn.setStatus("current")
_CfprApPortGroupLocale_Type = CfprApNetworkLocale
_CfprApPortGroupLocale_Object = MibTableColumn
cfprApPortGroupLocale = _CfprApPortGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2, 1, 4),
    _CfprApPortGroupLocale_Type()
)
cfprApPortGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortGroupLocale.setStatus("current")
_CfprApPortGroupName_Type = SnmpAdminString
_CfprApPortGroupName_Object = MibTableColumn
cfprApPortGroupName = _CfprApPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2, 1, 5),
    _CfprApPortGroupName_Type()
)
cfprApPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortGroupName.setStatus("current")
_CfprApPortGroupTransport_Type = CfprApNetworkTransport
_CfprApPortGroupTransport_Object = MibTableColumn
cfprApPortGroupTransport = _CfprApPortGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2, 1, 6),
    _CfprApPortGroupTransport_Type()
)
cfprApPortGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortGroupTransport.setStatus("current")
_CfprApPortGroupType_Type = CfprApPortGroupType
_CfprApPortGroupType_Object = MibTableColumn
cfprApPortGroupType = _CfprApPortGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 2, 1, 7),
    _CfprApPortGroupType_Type()
)
cfprApPortGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortGroupType.setStatus("current")
_CfprApPortPIoFsmTable_Object = MibTable
cfprApPortPIoFsmTable = _CfprApPortPIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3)
)
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTable.setStatus("current")
_CfprApPortPIoFsmEntry_Object = MibTableRow
cfprApPortPIoFsmEntry = _CfprApPortPIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1)
)
cfprApPortPIoFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PORT-MIB", "cfprApPortPIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPortPIoFsmEntry.setStatus("current")
_CfprApPortPIoFsmInstanceId_Type = CfprApManagedObjectId
_CfprApPortPIoFsmInstanceId_Object = MibTableColumn
cfprApPortPIoFsmInstanceId = _CfprApPortPIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 1),
    _CfprApPortPIoFsmInstanceId_Type()
)
cfprApPortPIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmInstanceId.setStatus("current")
_CfprApPortPIoFsmDn_Type = CfprApManagedObjectDn
_CfprApPortPIoFsmDn_Object = MibTableColumn
cfprApPortPIoFsmDn = _CfprApPortPIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 2),
    _CfprApPortPIoFsmDn_Type()
)
cfprApPortPIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmDn.setStatus("current")
_CfprApPortPIoFsmRn_Type = SnmpAdminString
_CfprApPortPIoFsmRn_Object = MibTableColumn
cfprApPortPIoFsmRn = _CfprApPortPIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 3),
    _CfprApPortPIoFsmRn_Type()
)
cfprApPortPIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmRn.setStatus("current")
_CfprApPortPIoFsmCompletionTime_Type = DateAndTime
_CfprApPortPIoFsmCompletionTime_Object = MibTableColumn
cfprApPortPIoFsmCompletionTime = _CfprApPortPIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 4),
    _CfprApPortPIoFsmCompletionTime_Type()
)
cfprApPortPIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmCompletionTime.setStatus("current")
_CfprApPortPIoFsmCurrentFsm_Type = CfprApPortPIoFsmCurrentFsm
_CfprApPortPIoFsmCurrentFsm_Object = MibTableColumn
cfprApPortPIoFsmCurrentFsm = _CfprApPortPIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 5),
    _CfprApPortPIoFsmCurrentFsm_Type()
)
cfprApPortPIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmCurrentFsm.setStatus("current")
_CfprApPortPIoFsmDescr_Type = SnmpAdminString
_CfprApPortPIoFsmDescr_Object = MibTableColumn
cfprApPortPIoFsmDescr = _CfprApPortPIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 6),
    _CfprApPortPIoFsmDescr_Type()
)
cfprApPortPIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmDescr.setStatus("current")
_CfprApPortPIoFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApPortPIoFsmFsmStatus_Object = MibTableColumn
cfprApPortPIoFsmFsmStatus = _CfprApPortPIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 7),
    _CfprApPortPIoFsmFsmStatus_Type()
)
cfprApPortPIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmFsmStatus.setStatus("current")
_CfprApPortPIoFsmProgress_Type = Gauge32
_CfprApPortPIoFsmProgress_Object = MibTableColumn
cfprApPortPIoFsmProgress = _CfprApPortPIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 8),
    _CfprApPortPIoFsmProgress_Type()
)
cfprApPortPIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmProgress.setStatus("current")
_CfprApPortPIoFsmRmtErrCode_Type = Gauge32
_CfprApPortPIoFsmRmtErrCode_Object = MibTableColumn
cfprApPortPIoFsmRmtErrCode = _CfprApPortPIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 9),
    _CfprApPortPIoFsmRmtErrCode_Type()
)
cfprApPortPIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmRmtErrCode.setStatus("current")
_CfprApPortPIoFsmRmtErrDescr_Type = SnmpAdminString
_CfprApPortPIoFsmRmtErrDescr_Object = MibTableColumn
cfprApPortPIoFsmRmtErrDescr = _CfprApPortPIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 10),
    _CfprApPortPIoFsmRmtErrDescr_Type()
)
cfprApPortPIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmRmtErrDescr.setStatus("current")
_CfprApPortPIoFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPortPIoFsmRmtRslt_Object = MibTableColumn
cfprApPortPIoFsmRmtRslt = _CfprApPortPIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 3, 1, 11),
    _CfprApPortPIoFsmRmtRslt_Type()
)
cfprApPortPIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmRmtRslt.setStatus("current")
_CfprApPortPIoFsmStageTable_Object = MibTable
cfprApPortPIoFsmStageTable = _CfprApPortPIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4)
)
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageTable.setStatus("current")
_CfprApPortPIoFsmStageEntry_Object = MibTableRow
cfprApPortPIoFsmStageEntry = _CfprApPortPIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1)
)
cfprApPortPIoFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PORT-MIB", "cfprApPortPIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageEntry.setStatus("current")
_CfprApPortPIoFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApPortPIoFsmStageInstanceId_Object = MibTableColumn
cfprApPortPIoFsmStageInstanceId = _CfprApPortPIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 1),
    _CfprApPortPIoFsmStageInstanceId_Type()
)
cfprApPortPIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageInstanceId.setStatus("current")
_CfprApPortPIoFsmStageDn_Type = CfprApManagedObjectDn
_CfprApPortPIoFsmStageDn_Object = MibTableColumn
cfprApPortPIoFsmStageDn = _CfprApPortPIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 2),
    _CfprApPortPIoFsmStageDn_Type()
)
cfprApPortPIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageDn.setStatus("current")
_CfprApPortPIoFsmStageRn_Type = SnmpAdminString
_CfprApPortPIoFsmStageRn_Object = MibTableColumn
cfprApPortPIoFsmStageRn = _CfprApPortPIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 3),
    _CfprApPortPIoFsmStageRn_Type()
)
cfprApPortPIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageRn.setStatus("current")
_CfprApPortPIoFsmStageDescr_Type = SnmpAdminString
_CfprApPortPIoFsmStageDescr_Object = MibTableColumn
cfprApPortPIoFsmStageDescr = _CfprApPortPIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 4),
    _CfprApPortPIoFsmStageDescr_Type()
)
cfprApPortPIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageDescr.setStatus("current")
_CfprApPortPIoFsmStageLastUpdateTime_Type = DateAndTime
_CfprApPortPIoFsmStageLastUpdateTime_Object = MibTableColumn
cfprApPortPIoFsmStageLastUpdateTime = _CfprApPortPIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 5),
    _CfprApPortPIoFsmStageLastUpdateTime_Type()
)
cfprApPortPIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageLastUpdateTime.setStatus("current")
_CfprApPortPIoFsmStageName_Type = CfprApPortPIoFsmStageName
_CfprApPortPIoFsmStageName_Object = MibTableColumn
cfprApPortPIoFsmStageName = _CfprApPortPIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 6),
    _CfprApPortPIoFsmStageName_Type()
)
cfprApPortPIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageName.setStatus("current")
_CfprApPortPIoFsmStageOrder_Type = Gauge32
_CfprApPortPIoFsmStageOrder_Object = MibTableColumn
cfprApPortPIoFsmStageOrder = _CfprApPortPIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 7),
    _CfprApPortPIoFsmStageOrder_Type()
)
cfprApPortPIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageOrder.setStatus("current")
_CfprApPortPIoFsmStageRetry_Type = Gauge32
_CfprApPortPIoFsmStageRetry_Object = MibTableColumn
cfprApPortPIoFsmStageRetry = _CfprApPortPIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 8),
    _CfprApPortPIoFsmStageRetry_Type()
)
cfprApPortPIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageRetry.setStatus("current")
_CfprApPortPIoFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApPortPIoFsmStageStageStatus_Object = MibTableColumn
cfprApPortPIoFsmStageStageStatus = _CfprApPortPIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 4, 1, 9),
    _CfprApPortPIoFsmStageStageStatus_Type()
)
cfprApPortPIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmStageStageStatus.setStatus("current")
_CfprApPortPIoFsmTaskTable_Object = MibTable
cfprApPortPIoFsmTaskTable = _CfprApPortPIoFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5)
)
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskTable.setStatus("current")
_CfprApPortPIoFsmTaskEntry_Object = MibTableRow
cfprApPortPIoFsmTaskEntry = _CfprApPortPIoFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5, 1)
)
cfprApPortPIoFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PORT-MIB", "cfprApPortPIoFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskEntry.setStatus("current")
_CfprApPortPIoFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApPortPIoFsmTaskInstanceId_Object = MibTableColumn
cfprApPortPIoFsmTaskInstanceId = _CfprApPortPIoFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5, 1, 1),
    _CfprApPortPIoFsmTaskInstanceId_Type()
)
cfprApPortPIoFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskInstanceId.setStatus("current")
_CfprApPortPIoFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApPortPIoFsmTaskDn_Object = MibTableColumn
cfprApPortPIoFsmTaskDn = _CfprApPortPIoFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5, 1, 2),
    _CfprApPortPIoFsmTaskDn_Type()
)
cfprApPortPIoFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskDn.setStatus("current")
_CfprApPortPIoFsmTaskRn_Type = SnmpAdminString
_CfprApPortPIoFsmTaskRn_Object = MibTableColumn
cfprApPortPIoFsmTaskRn = _CfprApPortPIoFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5, 1, 3),
    _CfprApPortPIoFsmTaskRn_Type()
)
cfprApPortPIoFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskRn.setStatus("current")
_CfprApPortPIoFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApPortPIoFsmTaskCompletion_Object = MibTableColumn
cfprApPortPIoFsmTaskCompletion = _CfprApPortPIoFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5, 1, 4),
    _CfprApPortPIoFsmTaskCompletion_Type()
)
cfprApPortPIoFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskCompletion.setStatus("current")
_CfprApPortPIoFsmTaskFlags_Type = CfprApFsmFlags
_CfprApPortPIoFsmTaskFlags_Object = MibTableColumn
cfprApPortPIoFsmTaskFlags = _CfprApPortPIoFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5, 1, 5),
    _CfprApPortPIoFsmTaskFlags_Type()
)
cfprApPortPIoFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskFlags.setStatus("current")
_CfprApPortPIoFsmTaskItem_Type = CfprApPortPIoFsmTaskItem
_CfprApPortPIoFsmTaskItem_Object = MibTableColumn
cfprApPortPIoFsmTaskItem = _CfprApPortPIoFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5, 1, 6),
    _CfprApPortPIoFsmTaskItem_Type()
)
cfprApPortPIoFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskItem.setStatus("current")
_CfprApPortPIoFsmTaskSeqId_Type = Gauge32
_CfprApPortPIoFsmTaskSeqId_Object = MibTableColumn
cfprApPortPIoFsmTaskSeqId = _CfprApPortPIoFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 5, 1, 7),
    _CfprApPortPIoFsmTaskSeqId_Type()
)
cfprApPortPIoFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortPIoFsmTaskSeqId.setStatus("current")
_CfprApPortSubGroupTable_Object = MibTable
cfprApPortSubGroupTable = _CfprApPortSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6)
)
if mibBuilder.loadTexts:
    cfprApPortSubGroupTable.setStatus("current")
_CfprApPortSubGroupEntry_Object = MibTableRow
cfprApPortSubGroupEntry = _CfprApPortSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1)
)
cfprApPortSubGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PORT-MIB", "cfprApPortSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPortSubGroupEntry.setStatus("current")
_CfprApPortSubGroupInstanceId_Type = CfprApManagedObjectId
_CfprApPortSubGroupInstanceId_Object = MibTableColumn
cfprApPortSubGroupInstanceId = _CfprApPortSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 1),
    _CfprApPortSubGroupInstanceId_Type()
)
cfprApPortSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPortSubGroupInstanceId.setStatus("current")
_CfprApPortSubGroupDn_Type = CfprApManagedObjectDn
_CfprApPortSubGroupDn_Object = MibTableColumn
cfprApPortSubGroupDn = _CfprApPortSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 2),
    _CfprApPortSubGroupDn_Type()
)
cfprApPortSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupDn.setStatus("current")
_CfprApPortSubGroupRn_Type = SnmpAdminString
_CfprApPortSubGroupRn_Object = MibTableColumn
cfprApPortSubGroupRn = _CfprApPortSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 3),
    _CfprApPortSubGroupRn_Type()
)
cfprApPortSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupRn.setStatus("current")
_CfprApPortSubGroupAggrPortId_Type = Gauge32
_CfprApPortSubGroupAggrPortId_Object = MibTableColumn
cfprApPortSubGroupAggrPortId = _CfprApPortSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 4),
    _CfprApPortSubGroupAggrPortId_Type()
)
cfprApPortSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupAggrPortId.setStatus("current")
_CfprApPortSubGroupConfigState_Type = CfprApPortSubGroupConfigState
_CfprApPortSubGroupConfigState_Object = MibTableColumn
cfprApPortSubGroupConfigState = _CfprApPortSubGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 5),
    _CfprApPortSubGroupConfigState_Type()
)
cfprApPortSubGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupConfigState.setStatus("current")
_CfprApPortSubGroupLicGP_Type = Unsigned64
_CfprApPortSubGroupLicGP_Object = MibTableColumn
cfprApPortSubGroupLicGP = _CfprApPortSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 6),
    _CfprApPortSubGroupLicGP_Type()
)
cfprApPortSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupLicGP.setStatus("current")
_CfprApPortSubGroupLicState_Type = CfprApLicenseState
_CfprApPortSubGroupLicState_Object = MibTableColumn
cfprApPortSubGroupLicState = _CfprApPortSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 7),
    _CfprApPortSubGroupLicState_Type()
)
cfprApPortSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupLicState.setStatus("current")
_CfprApPortSubGroupLocale_Type = CfprApNetworkLocale
_CfprApPortSubGroupLocale_Object = MibTableColumn
cfprApPortSubGroupLocale = _CfprApPortSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 8),
    _CfprApPortSubGroupLocale_Type()
)
cfprApPortSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupLocale.setStatus("current")
_CfprApPortSubGroupName_Type = SnmpAdminString
_CfprApPortSubGroupName_Object = MibTableColumn
cfprApPortSubGroupName = _CfprApPortSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 9),
    _CfprApPortSubGroupName_Type()
)
cfprApPortSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupName.setStatus("current")
_CfprApPortSubGroupSlotId_Type = CfprApPortSubGroupSlotId
_CfprApPortSubGroupSlotId_Object = MibTableColumn
cfprApPortSubGroupSlotId = _CfprApPortSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 10),
    _CfprApPortSubGroupSlotId_Type()
)
cfprApPortSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupSlotId.setStatus("current")
_CfprApPortSubGroupSwitchId_Type = CfprApNetworkSwitchId
_CfprApPortSubGroupSwitchId_Object = MibTableColumn
cfprApPortSubGroupSwitchId = _CfprApPortSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 11),
    _CfprApPortSubGroupSwitchId_Type()
)
cfprApPortSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupSwitchId.setStatus("current")
_CfprApPortSubGroupTransport_Type = CfprApNetworkTransport
_CfprApPortSubGroupTransport_Object = MibTableColumn
cfprApPortSubGroupTransport = _CfprApPortSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 12),
    _CfprApPortSubGroupTransport_Type()
)
cfprApPortSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupTransport.setStatus("current")
_CfprApPortSubGroupType_Type = CfprApNetworkConnectionType
_CfprApPortSubGroupType_Object = MibTableColumn
cfprApPortSubGroupType = _CfprApPortSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 6, 1, 13),
    _CfprApPortSubGroupType_Type()
)
cfprApPortSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortSubGroupType.setStatus("current")
_CfprApPortTrustModeTable_Object = MibTable
cfprApPortTrustModeTable = _CfprApPortTrustModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 7)
)
if mibBuilder.loadTexts:
    cfprApPortTrustModeTable.setStatus("current")
_CfprApPortTrustModeEntry_Object = MibTableRow
cfprApPortTrustModeEntry = _CfprApPortTrustModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 7, 1)
)
cfprApPortTrustModeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PORT-MIB", "cfprApPortTrustModeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPortTrustModeEntry.setStatus("current")
_CfprApPortTrustModeInstanceId_Type = CfprApManagedObjectId
_CfprApPortTrustModeInstanceId_Object = MibTableColumn
cfprApPortTrustModeInstanceId = _CfprApPortTrustModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 7, 1, 1),
    _CfprApPortTrustModeInstanceId_Type()
)
cfprApPortTrustModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPortTrustModeInstanceId.setStatus("current")
_CfprApPortTrustModeDn_Type = CfprApManagedObjectDn
_CfprApPortTrustModeDn_Object = MibTableColumn
cfprApPortTrustModeDn = _CfprApPortTrustModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 7, 1, 2),
    _CfprApPortTrustModeDn_Type()
)
cfprApPortTrustModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortTrustModeDn.setStatus("current")
_CfprApPortTrustModeRn_Type = SnmpAdminString
_CfprApPortTrustModeRn_Object = MibTableColumn
cfprApPortTrustModeRn = _CfprApPortTrustModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 7, 1, 3),
    _CfprApPortTrustModeRn_Type()
)
cfprApPortTrustModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortTrustModeRn.setStatus("current")
_CfprApPortTrustModeState_Type = CfprApPortTrust
_CfprApPortTrustModeState_Object = MibTableColumn
cfprApPortTrustModeState = _CfprApPortTrustModeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 63, 7, 1, 4),
    _CfprApPortTrustModeState_Type()
)
cfprApPortTrustModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPortTrustModeState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-PORT-MIB",
    **{"cfprApPortObjects": cfprApPortObjects,
       "cfprApPortDomainEpTable": cfprApPortDomainEpTable,
       "cfprApPortDomainEpEntry": cfprApPortDomainEpEntry,
       "cfprApPortDomainEpInstanceId": cfprApPortDomainEpInstanceId,
       "cfprApPortDomainEpDn": cfprApPortDomainEpDn,
       "cfprApPortDomainEpRn": cfprApPortDomainEpRn,
       "cfprApPortDomainEpEpDn": cfprApPortDomainEpEpDn,
       "cfprApPortDomainEpIfRole": cfprApPortDomainEpIfRole,
       "cfprApPortDomainEpIfType": cfprApPortDomainEpIfType,
       "cfprApPortDomainEpLocale": cfprApPortDomainEpLocale,
       "cfprApPortDomainEpName": cfprApPortDomainEpName,
       "cfprApPortDomainEpPeerDn": cfprApPortDomainEpPeerDn,
       "cfprApPortDomainEpTransport": cfprApPortDomainEpTransport,
       "cfprApPortDomainEpType": cfprApPortDomainEpType,
       "cfprApPortGroupTable": cfprApPortGroupTable,
       "cfprApPortGroupEntry": cfprApPortGroupEntry,
       "cfprApPortGroupInstanceId": cfprApPortGroupInstanceId,
       "cfprApPortGroupDn": cfprApPortGroupDn,
       "cfprApPortGroupRn": cfprApPortGroupRn,
       "cfprApPortGroupLocale": cfprApPortGroupLocale,
       "cfprApPortGroupName": cfprApPortGroupName,
       "cfprApPortGroupTransport": cfprApPortGroupTransport,
       "cfprApPortGroupType": cfprApPortGroupType,
       "cfprApPortPIoFsmTable": cfprApPortPIoFsmTable,
       "cfprApPortPIoFsmEntry": cfprApPortPIoFsmEntry,
       "cfprApPortPIoFsmInstanceId": cfprApPortPIoFsmInstanceId,
       "cfprApPortPIoFsmDn": cfprApPortPIoFsmDn,
       "cfprApPortPIoFsmRn": cfprApPortPIoFsmRn,
       "cfprApPortPIoFsmCompletionTime": cfprApPortPIoFsmCompletionTime,
       "cfprApPortPIoFsmCurrentFsm": cfprApPortPIoFsmCurrentFsm,
       "cfprApPortPIoFsmDescr": cfprApPortPIoFsmDescr,
       "cfprApPortPIoFsmFsmStatus": cfprApPortPIoFsmFsmStatus,
       "cfprApPortPIoFsmProgress": cfprApPortPIoFsmProgress,
       "cfprApPortPIoFsmRmtErrCode": cfprApPortPIoFsmRmtErrCode,
       "cfprApPortPIoFsmRmtErrDescr": cfprApPortPIoFsmRmtErrDescr,
       "cfprApPortPIoFsmRmtRslt": cfprApPortPIoFsmRmtRslt,
       "cfprApPortPIoFsmStageTable": cfprApPortPIoFsmStageTable,
       "cfprApPortPIoFsmStageEntry": cfprApPortPIoFsmStageEntry,
       "cfprApPortPIoFsmStageInstanceId": cfprApPortPIoFsmStageInstanceId,
       "cfprApPortPIoFsmStageDn": cfprApPortPIoFsmStageDn,
       "cfprApPortPIoFsmStageRn": cfprApPortPIoFsmStageRn,
       "cfprApPortPIoFsmStageDescr": cfprApPortPIoFsmStageDescr,
       "cfprApPortPIoFsmStageLastUpdateTime": cfprApPortPIoFsmStageLastUpdateTime,
       "cfprApPortPIoFsmStageName": cfprApPortPIoFsmStageName,
       "cfprApPortPIoFsmStageOrder": cfprApPortPIoFsmStageOrder,
       "cfprApPortPIoFsmStageRetry": cfprApPortPIoFsmStageRetry,
       "cfprApPortPIoFsmStageStageStatus": cfprApPortPIoFsmStageStageStatus,
       "cfprApPortPIoFsmTaskTable": cfprApPortPIoFsmTaskTable,
       "cfprApPortPIoFsmTaskEntry": cfprApPortPIoFsmTaskEntry,
       "cfprApPortPIoFsmTaskInstanceId": cfprApPortPIoFsmTaskInstanceId,
       "cfprApPortPIoFsmTaskDn": cfprApPortPIoFsmTaskDn,
       "cfprApPortPIoFsmTaskRn": cfprApPortPIoFsmTaskRn,
       "cfprApPortPIoFsmTaskCompletion": cfprApPortPIoFsmTaskCompletion,
       "cfprApPortPIoFsmTaskFlags": cfprApPortPIoFsmTaskFlags,
       "cfprApPortPIoFsmTaskItem": cfprApPortPIoFsmTaskItem,
       "cfprApPortPIoFsmTaskSeqId": cfprApPortPIoFsmTaskSeqId,
       "cfprApPortSubGroupTable": cfprApPortSubGroupTable,
       "cfprApPortSubGroupEntry": cfprApPortSubGroupEntry,
       "cfprApPortSubGroupInstanceId": cfprApPortSubGroupInstanceId,
       "cfprApPortSubGroupDn": cfprApPortSubGroupDn,
       "cfprApPortSubGroupRn": cfprApPortSubGroupRn,
       "cfprApPortSubGroupAggrPortId": cfprApPortSubGroupAggrPortId,
       "cfprApPortSubGroupConfigState": cfprApPortSubGroupConfigState,
       "cfprApPortSubGroupLicGP": cfprApPortSubGroupLicGP,
       "cfprApPortSubGroupLicState": cfprApPortSubGroupLicState,
       "cfprApPortSubGroupLocale": cfprApPortSubGroupLocale,
       "cfprApPortSubGroupName": cfprApPortSubGroupName,
       "cfprApPortSubGroupSlotId": cfprApPortSubGroupSlotId,
       "cfprApPortSubGroupSwitchId": cfprApPortSubGroupSwitchId,
       "cfprApPortSubGroupTransport": cfprApPortSubGroupTransport,
       "cfprApPortSubGroupType": cfprApPortSubGroupType,
       "cfprApPortTrustModeTable": cfprApPortTrustModeTable,
       "cfprApPortTrustModeEntry": cfprApPortTrustModeEntry,
       "cfprApPortTrustModeInstanceId": cfprApPortTrustModeInstanceId,
       "cfprApPortTrustModeDn": cfprApPortTrustModeDn,
       "cfprApPortTrustModeRn": cfprApPortTrustModeRn,
       "cfprApPortTrustModeState": cfprApPortTrustModeState}
)
