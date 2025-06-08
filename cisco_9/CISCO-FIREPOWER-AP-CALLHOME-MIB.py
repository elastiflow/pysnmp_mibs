# SNMP MIB module (CISCO-FIREPOWER-AP-CALLHOME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-CALLHOME-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:13 2025
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

(CfprApCallhomeAdminState,
 CfprApCallhomeAlertGroup,
 CfprApCallhomeAlertGroups,
 CfprApCallhomeAlertLevel,
 CfprApCallhomeAlertMessageSubtype,
 CfprApCallhomeAlertMessageType,
 CfprApCallhomeAlertThrottlingAdminState,
 CfprApCallhomeAnonymousReportingAdminState,
 CfprApCallhomeCallhomeProtocol,
 CfprApCallhomeEpConfigState,
 CfprApCallhomeEpFsmCurrentFsm,
 CfprApCallhomeEpFsmStageName,
 CfprApCallhomeEpFsmTaskItem,
 CfprApCallhomeFormat,
 CfprApCallhomeHttpProxyEnable,
 CfprApCallhomeLevel,
 CfprApCallhomePolicyAdminState,
 CfprApCallhomeReportingType,
 CfprApCallhomeUrgency,
 CfprApConditionCallHomeCause,
 CfprApConditionRemoteInvRslt,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApCallhomeAdminState",
    "CfprApCallhomeAlertGroup",
    "CfprApCallhomeAlertGroups",
    "CfprApCallhomeAlertLevel",
    "CfprApCallhomeAlertMessageSubtype",
    "CfprApCallhomeAlertMessageType",
    "CfprApCallhomeAlertThrottlingAdminState",
    "CfprApCallhomeAnonymousReportingAdminState",
    "CfprApCallhomeCallhomeProtocol",
    "CfprApCallhomeEpConfigState",
    "CfprApCallhomeEpFsmCurrentFsm",
    "CfprApCallhomeEpFsmStageName",
    "CfprApCallhomeEpFsmTaskItem",
    "CfprApCallhomeFormat",
    "CfprApCallhomeHttpProxyEnable",
    "CfprApCallhomeLevel",
    "CfprApCallhomePolicyAdminState",
    "CfprApCallhomeReportingType",
    "CfprApCallhomeUrgency",
    "CfprApConditionCallHomeCause",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
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

cfprApCallhomeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApCallhomeAnonymousReportingTable_Object = MibTable
cfprApCallhomeAnonymousReportingTable = _CfprApCallhomeAnonymousReportingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingTable.setStatus("current")
_CfprApCallhomeAnonymousReportingEntry_Object = MibTableRow
cfprApCallhomeAnonymousReportingEntry = _CfprApCallhomeAnonymousReportingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1, 1)
)
cfprApCallhomeAnonymousReportingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeAnonymousReportingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingEntry.setStatus("current")
_CfprApCallhomeAnonymousReportingInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeAnonymousReportingInstanceId_Object = MibTableColumn
cfprApCallhomeAnonymousReportingInstanceId = _CfprApCallhomeAnonymousReportingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1, 1, 1),
    _CfprApCallhomeAnonymousReportingInstanceId_Type()
)
cfprApCallhomeAnonymousReportingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingInstanceId.setStatus("current")
_CfprApCallhomeAnonymousReportingDn_Type = CfprApManagedObjectDn
_CfprApCallhomeAnonymousReportingDn_Object = MibTableColumn
cfprApCallhomeAnonymousReportingDn = _CfprApCallhomeAnonymousReportingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1, 1, 2),
    _CfprApCallhomeAnonymousReportingDn_Type()
)
cfprApCallhomeAnonymousReportingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingDn.setStatus("current")
_CfprApCallhomeAnonymousReportingRn_Type = SnmpAdminString
_CfprApCallhomeAnonymousReportingRn_Object = MibTableColumn
cfprApCallhomeAnonymousReportingRn = _CfprApCallhomeAnonymousReportingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1, 1, 3),
    _CfprApCallhomeAnonymousReportingRn_Type()
)
cfprApCallhomeAnonymousReportingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingRn.setStatus("current")
_CfprApCallhomeAnonymousReportingAdminState_Type = CfprApCallhomeAnonymousReportingAdminState
_CfprApCallhomeAnonymousReportingAdminState_Object = MibTableColumn
cfprApCallhomeAnonymousReportingAdminState = _CfprApCallhomeAnonymousReportingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1, 1, 4),
    _CfprApCallhomeAnonymousReportingAdminState_Type()
)
cfprApCallhomeAnonymousReportingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingAdminState.setStatus("current")
_CfprApCallhomeAnonymousReportingCount_Type = Gauge32
_CfprApCallhomeAnonymousReportingCount_Object = MibTableColumn
cfprApCallhomeAnonymousReportingCount = _CfprApCallhomeAnonymousReportingCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1, 1, 5),
    _CfprApCallhomeAnonymousReportingCount_Type()
)
cfprApCallhomeAnonymousReportingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingCount.setStatus("current")
_CfprApCallhomeAnonymousReportingSleepInterval_Type = Gauge32
_CfprApCallhomeAnonymousReportingSleepInterval_Object = MibTableColumn
cfprApCallhomeAnonymousReportingSleepInterval = _CfprApCallhomeAnonymousReportingSleepInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1, 1, 6),
    _CfprApCallhomeAnonymousReportingSleepInterval_Type()
)
cfprApCallhomeAnonymousReportingSleepInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingSleepInterval.setStatus("current")
_CfprApCallhomeAnonymousReportingUserAcknowledged_Type = TruthValue
_CfprApCallhomeAnonymousReportingUserAcknowledged_Object = MibTableColumn
cfprApCallhomeAnonymousReportingUserAcknowledged = _CfprApCallhomeAnonymousReportingUserAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 1, 1, 7),
    _CfprApCallhomeAnonymousReportingUserAcknowledged_Type()
)
cfprApCallhomeAnonymousReportingUserAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeAnonymousReportingUserAcknowledged.setStatus("current")
_CfprApCallhomeDestTable_Object = MibTable
cfprApCallhomeDestTable = _CfprApCallhomeDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cfprApCallhomeDestTable.setStatus("current")
_CfprApCallhomeDestEntry_Object = MibTableRow
cfprApCallhomeDestEntry = _CfprApCallhomeDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 2, 1)
)
cfprApCallhomeDestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeDestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeDestEntry.setStatus("current")
_CfprApCallhomeDestInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeDestInstanceId_Object = MibTableColumn
cfprApCallhomeDestInstanceId = _CfprApCallhomeDestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 2, 1, 1),
    _CfprApCallhomeDestInstanceId_Type()
)
cfprApCallhomeDestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeDestInstanceId.setStatus("current")
_CfprApCallhomeDestDn_Type = CfprApManagedObjectDn
_CfprApCallhomeDestDn_Object = MibTableColumn
cfprApCallhomeDestDn = _CfprApCallhomeDestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 2, 1, 2),
    _CfprApCallhomeDestDn_Type()
)
cfprApCallhomeDestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeDestDn.setStatus("current")
_CfprApCallhomeDestRn_Type = SnmpAdminString
_CfprApCallhomeDestRn_Object = MibTableColumn
cfprApCallhomeDestRn = _CfprApCallhomeDestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 2, 1, 3),
    _CfprApCallhomeDestRn_Type()
)
cfprApCallhomeDestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeDestRn.setStatus("current")
_CfprApCallhomeDestAddress_Type = SnmpAdminString
_CfprApCallhomeDestAddress_Object = MibTableColumn
cfprApCallhomeDestAddress = _CfprApCallhomeDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 2, 1, 4),
    _CfprApCallhomeDestAddress_Type()
)
cfprApCallhomeDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeDestAddress.setStatus("current")
_CfprApCallhomeDestName_Type = SnmpAdminString
_CfprApCallhomeDestName_Object = MibTableColumn
cfprApCallhomeDestName = _CfprApCallhomeDestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 2, 1, 5),
    _CfprApCallhomeDestName_Type()
)
cfprApCallhomeDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeDestName.setStatus("current")
_CfprApCallhomeDestProtocol_Type = CfprApCallhomeCallhomeProtocol
_CfprApCallhomeDestProtocol_Object = MibTableColumn
cfprApCallhomeDestProtocol = _CfprApCallhomeDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 2, 1, 6),
    _CfprApCallhomeDestProtocol_Type()
)
cfprApCallhomeDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeDestProtocol.setStatus("current")
_CfprApCallhomeEpTable_Object = MibTable
cfprApCallhomeEpTable = _CfprApCallhomeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cfprApCallhomeEpTable.setStatus("current")
_CfprApCallhomeEpEntry_Object = MibTableRow
cfprApCallhomeEpEntry = _CfprApCallhomeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1)
)
cfprApCallhomeEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeEpEntry.setStatus("current")
_CfprApCallhomeEpInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeEpInstanceId_Object = MibTableColumn
cfprApCallhomeEpInstanceId = _CfprApCallhomeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 1),
    _CfprApCallhomeEpInstanceId_Type()
)
cfprApCallhomeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeEpInstanceId.setStatus("current")
_CfprApCallhomeEpDn_Type = CfprApManagedObjectDn
_CfprApCallhomeEpDn_Object = MibTableColumn
cfprApCallhomeEpDn = _CfprApCallhomeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 2),
    _CfprApCallhomeEpDn_Type()
)
cfprApCallhomeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpDn.setStatus("current")
_CfprApCallhomeEpRn_Type = SnmpAdminString
_CfprApCallhomeEpRn_Object = MibTableColumn
cfprApCallhomeEpRn = _CfprApCallhomeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 3),
    _CfprApCallhomeEpRn_Type()
)
cfprApCallhomeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpRn.setStatus("current")
_CfprApCallhomeEpAdminState_Type = CfprApCallhomeAdminState
_CfprApCallhomeEpAdminState_Object = MibTableColumn
cfprApCallhomeEpAdminState = _CfprApCallhomeEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 4),
    _CfprApCallhomeEpAdminState_Type()
)
cfprApCallhomeEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpAdminState.setStatus("current")
_CfprApCallhomeEpAlertThrottlingAdminState_Type = CfprApCallhomeAlertThrottlingAdminState
_CfprApCallhomeEpAlertThrottlingAdminState_Object = MibTableColumn
cfprApCallhomeEpAlertThrottlingAdminState = _CfprApCallhomeEpAlertThrottlingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 5),
    _CfprApCallhomeEpAlertThrottlingAdminState_Type()
)
cfprApCallhomeEpAlertThrottlingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpAlertThrottlingAdminState.setStatus("current")
_CfprApCallhomeEpConfigState_Type = CfprApCallhomeEpConfigState
_CfprApCallhomeEpConfigState_Object = MibTableColumn
cfprApCallhomeEpConfigState = _CfprApCallhomeEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 6),
    _CfprApCallhomeEpConfigState_Type()
)
cfprApCallhomeEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpConfigState.setStatus("current")
_CfprApCallhomeEpDescr_Type = SnmpAdminString
_CfprApCallhomeEpDescr_Object = MibTableColumn
cfprApCallhomeEpDescr = _CfprApCallhomeEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 7),
    _CfprApCallhomeEpDescr_Type()
)
cfprApCallhomeEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpDescr.setStatus("current")
_CfprApCallhomeEpFsmDescr_Type = SnmpAdminString
_CfprApCallhomeEpFsmDescr_Object = MibTableColumn
cfprApCallhomeEpFsmDescr = _CfprApCallhomeEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 8),
    _CfprApCallhomeEpFsmDescr_Type()
)
cfprApCallhomeEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmDescr.setStatus("current")
_CfprApCallhomeEpFsmPrev_Type = SnmpAdminString
_CfprApCallhomeEpFsmPrev_Object = MibTableColumn
cfprApCallhomeEpFsmPrev = _CfprApCallhomeEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 9),
    _CfprApCallhomeEpFsmPrev_Type()
)
cfprApCallhomeEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmPrev.setStatus("current")
_CfprApCallhomeEpFsmProgr_Type = Gauge32
_CfprApCallhomeEpFsmProgr_Object = MibTableColumn
cfprApCallhomeEpFsmProgr = _CfprApCallhomeEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 10),
    _CfprApCallhomeEpFsmProgr_Type()
)
cfprApCallhomeEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmProgr.setStatus("current")
_CfprApCallhomeEpFsmRmtInvErrCode_Type = Gauge32
_CfprApCallhomeEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApCallhomeEpFsmRmtInvErrCode = _CfprApCallhomeEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 11),
    _CfprApCallhomeEpFsmRmtInvErrCode_Type()
)
cfprApCallhomeEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmRmtInvErrCode.setStatus("current")
_CfprApCallhomeEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApCallhomeEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApCallhomeEpFsmRmtInvErrDescr = _CfprApCallhomeEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 12),
    _CfprApCallhomeEpFsmRmtInvErrDescr_Type()
)
cfprApCallhomeEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmRmtInvErrDescr.setStatus("current")
_CfprApCallhomeEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCallhomeEpFsmRmtInvRslt_Object = MibTableColumn
cfprApCallhomeEpFsmRmtInvRslt = _CfprApCallhomeEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 13),
    _CfprApCallhomeEpFsmRmtInvRslt_Type()
)
cfprApCallhomeEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmRmtInvRslt.setStatus("current")
_CfprApCallhomeEpFsmStageDescr_Type = SnmpAdminString
_CfprApCallhomeEpFsmStageDescr_Object = MibTableColumn
cfprApCallhomeEpFsmStageDescr = _CfprApCallhomeEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 14),
    _CfprApCallhomeEpFsmStageDescr_Type()
)
cfprApCallhomeEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageDescr.setStatus("current")
_CfprApCallhomeEpFsmStamp_Type = DateAndTime
_CfprApCallhomeEpFsmStamp_Object = MibTableColumn
cfprApCallhomeEpFsmStamp = _CfprApCallhomeEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 15),
    _CfprApCallhomeEpFsmStamp_Type()
)
cfprApCallhomeEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStamp.setStatus("current")
_CfprApCallhomeEpFsmStatus_Type = SnmpAdminString
_CfprApCallhomeEpFsmStatus_Object = MibTableColumn
cfprApCallhomeEpFsmStatus = _CfprApCallhomeEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 16),
    _CfprApCallhomeEpFsmStatus_Type()
)
cfprApCallhomeEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStatus.setStatus("current")
_CfprApCallhomeEpFsmTry_Type = Gauge32
_CfprApCallhomeEpFsmTry_Object = MibTableColumn
cfprApCallhomeEpFsmTry = _CfprApCallhomeEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 17),
    _CfprApCallhomeEpFsmTry_Type()
)
cfprApCallhomeEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTry.setStatus("current")
_CfprApCallhomeEpIntId_Type = SnmpAdminString
_CfprApCallhomeEpIntId_Object = MibTableColumn
cfprApCallhomeEpIntId = _CfprApCallhomeEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 18),
    _CfprApCallhomeEpIntId_Type()
)
cfprApCallhomeEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpIntId.setStatus("current")
_CfprApCallhomeEpName_Type = SnmpAdminString
_CfprApCallhomeEpName_Object = MibTableColumn
cfprApCallhomeEpName = _CfprApCallhomeEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 19),
    _CfprApCallhomeEpName_Type()
)
cfprApCallhomeEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpName.setStatus("current")
_CfprApCallhomeEpPolicyLevel_Type = Gauge32
_CfprApCallhomeEpPolicyLevel_Object = MibTableColumn
cfprApCallhomeEpPolicyLevel = _CfprApCallhomeEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 20),
    _CfprApCallhomeEpPolicyLevel_Type()
)
cfprApCallhomeEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpPolicyLevel.setStatus("current")
_CfprApCallhomeEpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCallhomeEpPolicyOwner_Object = MibTableColumn
cfprApCallhomeEpPolicyOwner = _CfprApCallhomeEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 3, 1, 21),
    _CfprApCallhomeEpPolicyOwner_Type()
)
cfprApCallhomeEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpPolicyOwner.setStatus("current")
_CfprApCallhomeEpFsmTable_Object = MibTable
cfprApCallhomeEpFsmTable = _CfprApCallhomeEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTable.setStatus("current")
_CfprApCallhomeEpFsmEntry_Object = MibTableRow
cfprApCallhomeEpFsmEntry = _CfprApCallhomeEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1)
)
cfprApCallhomeEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmEntry.setStatus("current")
_CfprApCallhomeEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeEpFsmInstanceId_Object = MibTableColumn
cfprApCallhomeEpFsmInstanceId = _CfprApCallhomeEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 1),
    _CfprApCallhomeEpFsmInstanceId_Type()
)
cfprApCallhomeEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmInstanceId.setStatus("current")
_CfprApCallhomeEpFsmDn_Type = CfprApManagedObjectDn
_CfprApCallhomeEpFsmDn_Object = MibTableColumn
cfprApCallhomeEpFsmDn = _CfprApCallhomeEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 2),
    _CfprApCallhomeEpFsmDn_Type()
)
cfprApCallhomeEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmDn.setStatus("current")
_CfprApCallhomeEpFsmRn_Type = SnmpAdminString
_CfprApCallhomeEpFsmRn_Object = MibTableColumn
cfprApCallhomeEpFsmRn = _CfprApCallhomeEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 3),
    _CfprApCallhomeEpFsmRn_Type()
)
cfprApCallhomeEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmRn.setStatus("current")
_CfprApCallhomeEpFsmCompletionTime_Type = DateAndTime
_CfprApCallhomeEpFsmCompletionTime_Object = MibTableColumn
cfprApCallhomeEpFsmCompletionTime = _CfprApCallhomeEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 4),
    _CfprApCallhomeEpFsmCompletionTime_Type()
)
cfprApCallhomeEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmCompletionTime.setStatus("current")
_CfprApCallhomeEpFsmCurrentFsm_Type = CfprApCallhomeEpFsmCurrentFsm
_CfprApCallhomeEpFsmCurrentFsm_Object = MibTableColumn
cfprApCallhomeEpFsmCurrentFsm = _CfprApCallhomeEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 5),
    _CfprApCallhomeEpFsmCurrentFsm_Type()
)
cfprApCallhomeEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmCurrentFsm.setStatus("current")
_CfprApCallhomeEpFsmDescrData_Type = SnmpAdminString
_CfprApCallhomeEpFsmDescrData_Object = MibTableColumn
cfprApCallhomeEpFsmDescrData = _CfprApCallhomeEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 6),
    _CfprApCallhomeEpFsmDescrData_Type()
)
cfprApCallhomeEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmDescrData.setStatus("current")
_CfprApCallhomeEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApCallhomeEpFsmFsmStatus_Object = MibTableColumn
cfprApCallhomeEpFsmFsmStatus = _CfprApCallhomeEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 7),
    _CfprApCallhomeEpFsmFsmStatus_Type()
)
cfprApCallhomeEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmFsmStatus.setStatus("current")
_CfprApCallhomeEpFsmProgress_Type = Gauge32
_CfprApCallhomeEpFsmProgress_Object = MibTableColumn
cfprApCallhomeEpFsmProgress = _CfprApCallhomeEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 8),
    _CfprApCallhomeEpFsmProgress_Type()
)
cfprApCallhomeEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmProgress.setStatus("current")
_CfprApCallhomeEpFsmRmtErrCode_Type = Gauge32
_CfprApCallhomeEpFsmRmtErrCode_Object = MibTableColumn
cfprApCallhomeEpFsmRmtErrCode = _CfprApCallhomeEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 9),
    _CfprApCallhomeEpFsmRmtErrCode_Type()
)
cfprApCallhomeEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmRmtErrCode.setStatus("current")
_CfprApCallhomeEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApCallhomeEpFsmRmtErrDescr_Object = MibTableColumn
cfprApCallhomeEpFsmRmtErrDescr = _CfprApCallhomeEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 10),
    _CfprApCallhomeEpFsmRmtErrDescr_Type()
)
cfprApCallhomeEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmRmtErrDescr.setStatus("current")
_CfprApCallhomeEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCallhomeEpFsmRmtRslt_Object = MibTableColumn
cfprApCallhomeEpFsmRmtRslt = _CfprApCallhomeEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 4, 1, 11),
    _CfprApCallhomeEpFsmRmtRslt_Type()
)
cfprApCallhomeEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmRmtRslt.setStatus("current")
_CfprApCallhomeEpFsmStageTable_Object = MibTable
cfprApCallhomeEpFsmStageTable = _CfprApCallhomeEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageTable.setStatus("current")
_CfprApCallhomeEpFsmStageEntry_Object = MibTableRow
cfprApCallhomeEpFsmStageEntry = _CfprApCallhomeEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1)
)
cfprApCallhomeEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageEntry.setStatus("current")
_CfprApCallhomeEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeEpFsmStageInstanceId_Object = MibTableColumn
cfprApCallhomeEpFsmStageInstanceId = _CfprApCallhomeEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 1),
    _CfprApCallhomeEpFsmStageInstanceId_Type()
)
cfprApCallhomeEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageInstanceId.setStatus("current")
_CfprApCallhomeEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApCallhomeEpFsmStageDn_Object = MibTableColumn
cfprApCallhomeEpFsmStageDn = _CfprApCallhomeEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 2),
    _CfprApCallhomeEpFsmStageDn_Type()
)
cfprApCallhomeEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageDn.setStatus("current")
_CfprApCallhomeEpFsmStageRn_Type = SnmpAdminString
_CfprApCallhomeEpFsmStageRn_Object = MibTableColumn
cfprApCallhomeEpFsmStageRn = _CfprApCallhomeEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 3),
    _CfprApCallhomeEpFsmStageRn_Type()
)
cfprApCallhomeEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageRn.setStatus("current")
_CfprApCallhomeEpFsmStageDescrData_Type = SnmpAdminString
_CfprApCallhomeEpFsmStageDescrData_Object = MibTableColumn
cfprApCallhomeEpFsmStageDescrData = _CfprApCallhomeEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 4),
    _CfprApCallhomeEpFsmStageDescrData_Type()
)
cfprApCallhomeEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageDescrData.setStatus("current")
_CfprApCallhomeEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApCallhomeEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApCallhomeEpFsmStageLastUpdateTime = _CfprApCallhomeEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 5),
    _CfprApCallhomeEpFsmStageLastUpdateTime_Type()
)
cfprApCallhomeEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageLastUpdateTime.setStatus("current")
_CfprApCallhomeEpFsmStageName_Type = CfprApCallhomeEpFsmStageName
_CfprApCallhomeEpFsmStageName_Object = MibTableColumn
cfprApCallhomeEpFsmStageName = _CfprApCallhomeEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 6),
    _CfprApCallhomeEpFsmStageName_Type()
)
cfprApCallhomeEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageName.setStatus("current")
_CfprApCallhomeEpFsmStageOrder_Type = Gauge32
_CfprApCallhomeEpFsmStageOrder_Object = MibTableColumn
cfprApCallhomeEpFsmStageOrder = _CfprApCallhomeEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 7),
    _CfprApCallhomeEpFsmStageOrder_Type()
)
cfprApCallhomeEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageOrder.setStatus("current")
_CfprApCallhomeEpFsmStageRetry_Type = Gauge32
_CfprApCallhomeEpFsmStageRetry_Object = MibTableColumn
cfprApCallhomeEpFsmStageRetry = _CfprApCallhomeEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 8),
    _CfprApCallhomeEpFsmStageRetry_Type()
)
cfprApCallhomeEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageRetry.setStatus("current")
_CfprApCallhomeEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApCallhomeEpFsmStageStageStatus_Object = MibTableColumn
cfprApCallhomeEpFsmStageStageStatus = _CfprApCallhomeEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 5, 1, 9),
    _CfprApCallhomeEpFsmStageStageStatus_Type()
)
cfprApCallhomeEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmStageStageStatus.setStatus("current")
_CfprApCallhomeEpFsmTaskTable_Object = MibTable
cfprApCallhomeEpFsmTaskTable = _CfprApCallhomeEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskTable.setStatus("current")
_CfprApCallhomeEpFsmTaskEntry_Object = MibTableRow
cfprApCallhomeEpFsmTaskEntry = _CfprApCallhomeEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6, 1)
)
cfprApCallhomeEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskEntry.setStatus("current")
_CfprApCallhomeEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeEpFsmTaskInstanceId_Object = MibTableColumn
cfprApCallhomeEpFsmTaskInstanceId = _CfprApCallhomeEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6, 1, 1),
    _CfprApCallhomeEpFsmTaskInstanceId_Type()
)
cfprApCallhomeEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskInstanceId.setStatus("current")
_CfprApCallhomeEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApCallhomeEpFsmTaskDn_Object = MibTableColumn
cfprApCallhomeEpFsmTaskDn = _CfprApCallhomeEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6, 1, 2),
    _CfprApCallhomeEpFsmTaskDn_Type()
)
cfprApCallhomeEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskDn.setStatus("current")
_CfprApCallhomeEpFsmTaskRn_Type = SnmpAdminString
_CfprApCallhomeEpFsmTaskRn_Object = MibTableColumn
cfprApCallhomeEpFsmTaskRn = _CfprApCallhomeEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6, 1, 3),
    _CfprApCallhomeEpFsmTaskRn_Type()
)
cfprApCallhomeEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskRn.setStatus("current")
_CfprApCallhomeEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApCallhomeEpFsmTaskCompletion_Object = MibTableColumn
cfprApCallhomeEpFsmTaskCompletion = _CfprApCallhomeEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6, 1, 4),
    _CfprApCallhomeEpFsmTaskCompletion_Type()
)
cfprApCallhomeEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskCompletion.setStatus("current")
_CfprApCallhomeEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApCallhomeEpFsmTaskFlags_Object = MibTableColumn
cfprApCallhomeEpFsmTaskFlags = _CfprApCallhomeEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6, 1, 5),
    _CfprApCallhomeEpFsmTaskFlags_Type()
)
cfprApCallhomeEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskFlags.setStatus("current")
_CfprApCallhomeEpFsmTaskItem_Type = CfprApCallhomeEpFsmTaskItem
_CfprApCallhomeEpFsmTaskItem_Object = MibTableColumn
cfprApCallhomeEpFsmTaskItem = _CfprApCallhomeEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6, 1, 6),
    _CfprApCallhomeEpFsmTaskItem_Type()
)
cfprApCallhomeEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskItem.setStatus("current")
_CfprApCallhomeEpFsmTaskSeqId_Type = Gauge32
_CfprApCallhomeEpFsmTaskSeqId_Object = MibTableColumn
cfprApCallhomeEpFsmTaskSeqId = _CfprApCallhomeEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 6, 1, 7),
    _CfprApCallhomeEpFsmTaskSeqId_Type()
)
cfprApCallhomeEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeEpFsmTaskSeqId.setStatus("current")
_CfprApCallhomeHttpProxyTable_Object = MibTable
cfprApCallhomeHttpProxyTable = _CfprApCallhomeHttpProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 7)
)
if mibBuilder.loadTexts:
    cfprApCallhomeHttpProxyTable.setStatus("current")
_CfprApCallhomeHttpProxyEntry_Object = MibTableRow
cfprApCallhomeHttpProxyEntry = _CfprApCallhomeHttpProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 7, 1)
)
cfprApCallhomeHttpProxyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeHttpProxyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeHttpProxyEntry.setStatus("current")
_CfprApCallhomeHttpProxyInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeHttpProxyInstanceId_Object = MibTableColumn
cfprApCallhomeHttpProxyInstanceId = _CfprApCallhomeHttpProxyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 7, 1, 1),
    _CfprApCallhomeHttpProxyInstanceId_Type()
)
cfprApCallhomeHttpProxyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeHttpProxyInstanceId.setStatus("current")
_CfprApCallhomeHttpProxyDn_Type = CfprApManagedObjectDn
_CfprApCallhomeHttpProxyDn_Object = MibTableColumn
cfprApCallhomeHttpProxyDn = _CfprApCallhomeHttpProxyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 7, 1, 2),
    _CfprApCallhomeHttpProxyDn_Type()
)
cfprApCallhomeHttpProxyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeHttpProxyDn.setStatus("current")
_CfprApCallhomeHttpProxyRn_Type = SnmpAdminString
_CfprApCallhomeHttpProxyRn_Object = MibTableColumn
cfprApCallhomeHttpProxyRn = _CfprApCallhomeHttpProxyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 7, 1, 3),
    _CfprApCallhomeHttpProxyRn_Type()
)
cfprApCallhomeHttpProxyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeHttpProxyRn.setStatus("current")
_CfprApCallhomeHttpProxyProxyServerEnable_Type = CfprApCallhomeHttpProxyEnable
_CfprApCallhomeHttpProxyProxyServerEnable_Object = MibTableColumn
cfprApCallhomeHttpProxyProxyServerEnable = _CfprApCallhomeHttpProxyProxyServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 7, 1, 4),
    _CfprApCallhomeHttpProxyProxyServerEnable_Type()
)
cfprApCallhomeHttpProxyProxyServerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeHttpProxyProxyServerEnable.setStatus("current")
_CfprApCallhomeHttpProxyProxyServerPort_Type = Gauge32
_CfprApCallhomeHttpProxyProxyServerPort_Object = MibTableColumn
cfprApCallhomeHttpProxyProxyServerPort = _CfprApCallhomeHttpProxyProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 7, 1, 5),
    _CfprApCallhomeHttpProxyProxyServerPort_Type()
)
cfprApCallhomeHttpProxyProxyServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeHttpProxyProxyServerPort.setStatus("current")
_CfprApCallhomeHttpProxyProxyServerUrl_Type = SnmpAdminString
_CfprApCallhomeHttpProxyProxyServerUrl_Object = MibTableColumn
cfprApCallhomeHttpProxyProxyServerUrl = _CfprApCallhomeHttpProxyProxyServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 7, 1, 6),
    _CfprApCallhomeHttpProxyProxyServerUrl_Type()
)
cfprApCallhomeHttpProxyProxyServerUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeHttpProxyProxyServerUrl.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryTable_Object = MibTable
cfprApCallhomePeriodicSystemInventoryTable = _CfprApCallhomePeriodicSystemInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8)
)
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryTable.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryEntry_Object = MibTableRow
cfprApCallhomePeriodicSystemInventoryEntry = _CfprApCallhomePeriodicSystemInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1)
)
cfprApCallhomePeriodicSystemInventoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomePeriodicSystemInventoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryEntry.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomePeriodicSystemInventoryInstanceId_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryInstanceId = _CfprApCallhomePeriodicSystemInventoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 1),
    _CfprApCallhomePeriodicSystemInventoryInstanceId_Type()
)
cfprApCallhomePeriodicSystemInventoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryInstanceId.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryDn_Type = CfprApManagedObjectDn
_CfprApCallhomePeriodicSystemInventoryDn_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryDn = _CfprApCallhomePeriodicSystemInventoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 2),
    _CfprApCallhomePeriodicSystemInventoryDn_Type()
)
cfprApCallhomePeriodicSystemInventoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryDn.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryRn_Type = SnmpAdminString
_CfprApCallhomePeriodicSystemInventoryRn_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryRn = _CfprApCallhomePeriodicSystemInventoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 3),
    _CfprApCallhomePeriodicSystemInventoryRn_Type()
)
cfprApCallhomePeriodicSystemInventoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryRn.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryAdminState_Type = CfprApCallhomeAdminState
_CfprApCallhomePeriodicSystemInventoryAdminState_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryAdminState = _CfprApCallhomePeriodicSystemInventoryAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 4),
    _CfprApCallhomePeriodicSystemInventoryAdminState_Type()
)
cfprApCallhomePeriodicSystemInventoryAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryAdminState.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryIntervalDays_Type = Gauge32
_CfprApCallhomePeriodicSystemInventoryIntervalDays_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryIntervalDays = _CfprApCallhomePeriodicSystemInventoryIntervalDays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 5),
    _CfprApCallhomePeriodicSystemInventoryIntervalDays_Type()
)
cfprApCallhomePeriodicSystemInventoryIntervalDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryIntervalDays.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryLastDeadline_Type = DateAndTime
_CfprApCallhomePeriodicSystemInventoryLastDeadline_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryLastDeadline = _CfprApCallhomePeriodicSystemInventoryLastDeadline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 6),
    _CfprApCallhomePeriodicSystemInventoryLastDeadline_Type()
)
cfprApCallhomePeriodicSystemInventoryLastDeadline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryLastDeadline.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryMaximumRetryCount_Type = Gauge32
_CfprApCallhomePeriodicSystemInventoryMaximumRetryCount_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryMaximumRetryCount = _CfprApCallhomePeriodicSystemInventoryMaximumRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 7),
    _CfprApCallhomePeriodicSystemInventoryMaximumRetryCount_Type()
)
cfprApCallhomePeriodicSystemInventoryMaximumRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryMaximumRetryCount.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Type = Gauge32
_CfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds = _CfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 8),
    _CfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Type()
)
cfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryNextDeadline_Type = DateAndTime
_CfprApCallhomePeriodicSystemInventoryNextDeadline_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryNextDeadline = _CfprApCallhomePeriodicSystemInventoryNextDeadline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 9),
    _CfprApCallhomePeriodicSystemInventoryNextDeadline_Type()
)
cfprApCallhomePeriodicSystemInventoryNextDeadline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryNextDeadline.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryPollIntervalSeconds_Type = Gauge32
_CfprApCallhomePeriodicSystemInventoryPollIntervalSeconds_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryPollIntervalSeconds = _CfprApCallhomePeriodicSystemInventoryPollIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 10),
    _CfprApCallhomePeriodicSystemInventoryPollIntervalSeconds_Type()
)
cfprApCallhomePeriodicSystemInventoryPollIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryPollIntervalSeconds.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryRetryCount_Type = Gauge32
_CfprApCallhomePeriodicSystemInventoryRetryCount_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryRetryCount = _CfprApCallhomePeriodicSystemInventoryRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 11),
    _CfprApCallhomePeriodicSystemInventoryRetryCount_Type()
)
cfprApCallhomePeriodicSystemInventoryRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryRetryCount.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryRetryDelayMinutes_Type = Gauge32
_CfprApCallhomePeriodicSystemInventoryRetryDelayMinutes_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryRetryDelayMinutes = _CfprApCallhomePeriodicSystemInventoryRetryDelayMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 12),
    _CfprApCallhomePeriodicSystemInventoryRetryDelayMinutes_Type()
)
cfprApCallhomePeriodicSystemInventoryRetryDelayMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryRetryDelayMinutes.setStatus("current")
_CfprApCallhomePeriodicSystemInventorySendNow_Type = TruthValue
_CfprApCallhomePeriodicSystemInventorySendNow_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventorySendNow = _CfprApCallhomePeriodicSystemInventorySendNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 13),
    _CfprApCallhomePeriodicSystemInventorySendNow_Type()
)
cfprApCallhomePeriodicSystemInventorySendNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventorySendNow.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryTimeOfDayHour_Type = Gauge32
_CfprApCallhomePeriodicSystemInventoryTimeOfDayHour_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryTimeOfDayHour = _CfprApCallhomePeriodicSystemInventoryTimeOfDayHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 14),
    _CfprApCallhomePeriodicSystemInventoryTimeOfDayHour_Type()
)
cfprApCallhomePeriodicSystemInventoryTimeOfDayHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryTimeOfDayHour.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryTimeOfDayMinute_Type = Gauge32
_CfprApCallhomePeriodicSystemInventoryTimeOfDayMinute_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryTimeOfDayMinute = _CfprApCallhomePeriodicSystemInventoryTimeOfDayMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 15),
    _CfprApCallhomePeriodicSystemInventoryTimeOfDayMinute_Type()
)
cfprApCallhomePeriodicSystemInventoryTimeOfDayMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryTimeOfDayMinute.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt_Type = DateAndTime
_CfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt = _CfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 16),
    _CfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt_Type()
)
cfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt.setStatus("current")
_CfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess_Type = DateAndTime
_CfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess_Object = MibTableColumn
cfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess = _CfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 8, 1, 17),
    _CfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess_Type()
)
cfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess.setStatus("current")
_CfprApCallhomePolicyTable_Object = MibTable
cfprApCallhomePolicyTable = _CfprApCallhomePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9)
)
if mibBuilder.loadTexts:
    cfprApCallhomePolicyTable.setStatus("current")
_CfprApCallhomePolicyEntry_Object = MibTableRow
cfprApCallhomePolicyEntry = _CfprApCallhomePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9, 1)
)
cfprApCallhomePolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomePolicyEntry.setStatus("current")
_CfprApCallhomePolicyInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomePolicyInstanceId_Object = MibTableColumn
cfprApCallhomePolicyInstanceId = _CfprApCallhomePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9, 1, 1),
    _CfprApCallhomePolicyInstanceId_Type()
)
cfprApCallhomePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomePolicyInstanceId.setStatus("current")
_CfprApCallhomePolicyDn_Type = CfprApManagedObjectDn
_CfprApCallhomePolicyDn_Object = MibTableColumn
cfprApCallhomePolicyDn = _CfprApCallhomePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9, 1, 2),
    _CfprApCallhomePolicyDn_Type()
)
cfprApCallhomePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePolicyDn.setStatus("current")
_CfprApCallhomePolicyRn_Type = SnmpAdminString
_CfprApCallhomePolicyRn_Object = MibTableColumn
cfprApCallhomePolicyRn = _CfprApCallhomePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9, 1, 3),
    _CfprApCallhomePolicyRn_Type()
)
cfprApCallhomePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePolicyRn.setStatus("current")
_CfprApCallhomePolicyAdminState_Type = CfprApCallhomePolicyAdminState
_CfprApCallhomePolicyAdminState_Object = MibTableColumn
cfprApCallhomePolicyAdminState = _CfprApCallhomePolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9, 1, 4),
    _CfprApCallhomePolicyAdminState_Type()
)
cfprApCallhomePolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePolicyAdminState.setStatus("current")
_CfprApCallhomePolicyCause_Type = CfprApConditionCallHomeCause
_CfprApCallhomePolicyCause_Object = MibTableColumn
cfprApCallhomePolicyCause = _CfprApCallhomePolicyCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9, 1, 5),
    _CfprApCallhomePolicyCause_Type()
)
cfprApCallhomePolicyCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePolicyCause.setStatus("current")
_CfprApCallhomePolicyDescr_Type = SnmpAdminString
_CfprApCallhomePolicyDescr_Object = MibTableColumn
cfprApCallhomePolicyDescr = _CfprApCallhomePolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9, 1, 6),
    _CfprApCallhomePolicyDescr_Type()
)
cfprApCallhomePolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePolicyDescr.setStatus("current")
_CfprApCallhomePolicyName_Type = SnmpAdminString
_CfprApCallhomePolicyName_Object = MibTableColumn
cfprApCallhomePolicyName = _CfprApCallhomePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 9, 1, 7),
    _CfprApCallhomePolicyName_Type()
)
cfprApCallhomePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomePolicyName.setStatus("current")
_CfprApCallhomeProfileTable_Object = MibTable
cfprApCallhomeProfileTable = _CfprApCallhomeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10)
)
if mibBuilder.loadTexts:
    cfprApCallhomeProfileTable.setStatus("current")
_CfprApCallhomeProfileEntry_Object = MibTableRow
cfprApCallhomeProfileEntry = _CfprApCallhomeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1)
)
cfprApCallhomeProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeProfileEntry.setStatus("current")
_CfprApCallhomeProfileInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeProfileInstanceId_Object = MibTableColumn
cfprApCallhomeProfileInstanceId = _CfprApCallhomeProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 1),
    _CfprApCallhomeProfileInstanceId_Type()
)
cfprApCallhomeProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileInstanceId.setStatus("current")
_CfprApCallhomeProfileDn_Type = CfprApManagedObjectDn
_CfprApCallhomeProfileDn_Object = MibTableColumn
cfprApCallhomeProfileDn = _CfprApCallhomeProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 2),
    _CfprApCallhomeProfileDn_Type()
)
cfprApCallhomeProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileDn.setStatus("current")
_CfprApCallhomeProfileRn_Type = SnmpAdminString
_CfprApCallhomeProfileRn_Object = MibTableColumn
cfprApCallhomeProfileRn = _CfprApCallhomeProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 3),
    _CfprApCallhomeProfileRn_Type()
)
cfprApCallhomeProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileRn.setStatus("current")
_CfprApCallhomeProfileAlertGroups_Type = CfprApCallhomeAlertGroups
_CfprApCallhomeProfileAlertGroups_Object = MibTableColumn
cfprApCallhomeProfileAlertGroups = _CfprApCallhomeProfileAlertGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 4),
    _CfprApCallhomeProfileAlertGroups_Type()
)
cfprApCallhomeProfileAlertGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileAlertGroups.setStatus("current")
_CfprApCallhomeProfileDescr_Type = SnmpAdminString
_CfprApCallhomeProfileDescr_Object = MibTableColumn
cfprApCallhomeProfileDescr = _CfprApCallhomeProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 5),
    _CfprApCallhomeProfileDescr_Type()
)
cfprApCallhomeProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileDescr.setStatus("current")
_CfprApCallhomeProfileFormat_Type = CfprApCallhomeFormat
_CfprApCallhomeProfileFormat_Object = MibTableColumn
cfprApCallhomeProfileFormat = _CfprApCallhomeProfileFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 6),
    _CfprApCallhomeProfileFormat_Type()
)
cfprApCallhomeProfileFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileFormat.setStatus("current")
_CfprApCallhomeProfileLevel_Type = CfprApCallhomeLevel
_CfprApCallhomeProfileLevel_Object = MibTableColumn
cfprApCallhomeProfileLevel = _CfprApCallhomeProfileLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 7),
    _CfprApCallhomeProfileLevel_Type()
)
cfprApCallhomeProfileLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileLevel.setStatus("current")
_CfprApCallhomeProfileMaxSize_Type = Gauge32
_CfprApCallhomeProfileMaxSize_Object = MibTableColumn
cfprApCallhomeProfileMaxSize = _CfprApCallhomeProfileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 8),
    _CfprApCallhomeProfileMaxSize_Type()
)
cfprApCallhomeProfileMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileMaxSize.setStatus("current")
_CfprApCallhomeProfileName_Type = SnmpAdminString
_CfprApCallhomeProfileName_Object = MibTableColumn
cfprApCallhomeProfileName = _CfprApCallhomeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 9),
    _CfprApCallhomeProfileName_Type()
)
cfprApCallhomeProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileName.setStatus("current")
_CfprApCallhomeProfileReporting_Type = CfprApCallhomeReportingType
_CfprApCallhomeProfileReporting_Object = MibTableColumn
cfprApCallhomeProfileReporting = _CfprApCallhomeProfileReporting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 10, 1, 10),
    _CfprApCallhomeProfileReporting_Type()
)
cfprApCallhomeProfileReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeProfileReporting.setStatus("current")
_CfprApCallhomeSmtpTable_Object = MibTable
cfprApCallhomeSmtpTable = _CfprApCallhomeSmtpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 11)
)
if mibBuilder.loadTexts:
    cfprApCallhomeSmtpTable.setStatus("current")
_CfprApCallhomeSmtpEntry_Object = MibTableRow
cfprApCallhomeSmtpEntry = _CfprApCallhomeSmtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 11, 1)
)
cfprApCallhomeSmtpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeSmtpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeSmtpEntry.setStatus("current")
_CfprApCallhomeSmtpInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeSmtpInstanceId_Object = MibTableColumn
cfprApCallhomeSmtpInstanceId = _CfprApCallhomeSmtpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 11, 1, 1),
    _CfprApCallhomeSmtpInstanceId_Type()
)
cfprApCallhomeSmtpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeSmtpInstanceId.setStatus("current")
_CfprApCallhomeSmtpDn_Type = CfprApManagedObjectDn
_CfprApCallhomeSmtpDn_Object = MibTableColumn
cfprApCallhomeSmtpDn = _CfprApCallhomeSmtpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 11, 1, 2),
    _CfprApCallhomeSmtpDn_Type()
)
cfprApCallhomeSmtpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSmtpDn.setStatus("current")
_CfprApCallhomeSmtpRn_Type = SnmpAdminString
_CfprApCallhomeSmtpRn_Object = MibTableColumn
cfprApCallhomeSmtpRn = _CfprApCallhomeSmtpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 11, 1, 3),
    _CfprApCallhomeSmtpRn_Type()
)
cfprApCallhomeSmtpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSmtpRn.setStatus("current")
_CfprApCallhomeSmtpHost_Type = SnmpAdminString
_CfprApCallhomeSmtpHost_Object = MibTableColumn
cfprApCallhomeSmtpHost = _CfprApCallhomeSmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 11, 1, 4),
    _CfprApCallhomeSmtpHost_Type()
)
cfprApCallhomeSmtpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSmtpHost.setStatus("current")
_CfprApCallhomeSmtpPort_Type = Gauge32
_CfprApCallhomeSmtpPort_Object = MibTableColumn
cfprApCallhomeSmtpPort = _CfprApCallhomeSmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 11, 1, 5),
    _CfprApCallhomeSmtpPort_Type()
)
cfprApCallhomeSmtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSmtpPort.setStatus("current")
_CfprApCallhomeSourceTable_Object = MibTable
cfprApCallhomeSourceTable = _CfprApCallhomeSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12)
)
if mibBuilder.loadTexts:
    cfprApCallhomeSourceTable.setStatus("current")
_CfprApCallhomeSourceEntry_Object = MibTableRow
cfprApCallhomeSourceEntry = _CfprApCallhomeSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1)
)
cfprApCallhomeSourceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeSourceEntry.setStatus("current")
_CfprApCallhomeSourceInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeSourceInstanceId_Object = MibTableColumn
cfprApCallhomeSourceInstanceId = _CfprApCallhomeSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 1),
    _CfprApCallhomeSourceInstanceId_Type()
)
cfprApCallhomeSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceInstanceId.setStatus("current")
_CfprApCallhomeSourceDn_Type = CfprApManagedObjectDn
_CfprApCallhomeSourceDn_Object = MibTableColumn
cfprApCallhomeSourceDn = _CfprApCallhomeSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 2),
    _CfprApCallhomeSourceDn_Type()
)
cfprApCallhomeSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceDn.setStatus("current")
_CfprApCallhomeSourceRn_Type = SnmpAdminString
_CfprApCallhomeSourceRn_Object = MibTableColumn
cfprApCallhomeSourceRn = _CfprApCallhomeSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 3),
    _CfprApCallhomeSourceRn_Type()
)
cfprApCallhomeSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceRn.setStatus("current")
_CfprApCallhomeSourceAddr_Type = SnmpAdminString
_CfprApCallhomeSourceAddr_Object = MibTableColumn
cfprApCallhomeSourceAddr = _CfprApCallhomeSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 4),
    _CfprApCallhomeSourceAddr_Type()
)
cfprApCallhomeSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceAddr.setStatus("current")
_CfprApCallhomeSourceContact_Type = SnmpAdminString
_CfprApCallhomeSourceContact_Object = MibTableColumn
cfprApCallhomeSourceContact = _CfprApCallhomeSourceContact_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 5),
    _CfprApCallhomeSourceContact_Type()
)
cfprApCallhomeSourceContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceContact.setStatus("current")
_CfprApCallhomeSourceContract_Type = SnmpAdminString
_CfprApCallhomeSourceContract_Object = MibTableColumn
cfprApCallhomeSourceContract = _CfprApCallhomeSourceContract_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 6),
    _CfprApCallhomeSourceContract_Type()
)
cfprApCallhomeSourceContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceContract.setStatus("current")
_CfprApCallhomeSourceCustomer_Type = SnmpAdminString
_CfprApCallhomeSourceCustomer_Object = MibTableColumn
cfprApCallhomeSourceCustomer = _CfprApCallhomeSourceCustomer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 7),
    _CfprApCallhomeSourceCustomer_Type()
)
cfprApCallhomeSourceCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceCustomer.setStatus("current")
_CfprApCallhomeSourceEmail_Type = SnmpAdminString
_CfprApCallhomeSourceEmail_Object = MibTableColumn
cfprApCallhomeSourceEmail = _CfprApCallhomeSourceEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 8),
    _CfprApCallhomeSourceEmail_Type()
)
cfprApCallhomeSourceEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceEmail.setStatus("current")
_CfprApCallhomeSourceFrom_Type = SnmpAdminString
_CfprApCallhomeSourceFrom_Object = MibTableColumn
cfprApCallhomeSourceFrom = _CfprApCallhomeSourceFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 9),
    _CfprApCallhomeSourceFrom_Type()
)
cfprApCallhomeSourceFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceFrom.setStatus("current")
_CfprApCallhomeSourcePhone_Type = SnmpAdminString
_CfprApCallhomeSourcePhone_Object = MibTableColumn
cfprApCallhomeSourcePhone = _CfprApCallhomeSourcePhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 10),
    _CfprApCallhomeSourcePhone_Type()
)
cfprApCallhomeSourcePhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourcePhone.setStatus("current")
_CfprApCallhomeSourceReplyTo_Type = SnmpAdminString
_CfprApCallhomeSourceReplyTo_Object = MibTableColumn
cfprApCallhomeSourceReplyTo = _CfprApCallhomeSourceReplyTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 11),
    _CfprApCallhomeSourceReplyTo_Type()
)
cfprApCallhomeSourceReplyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceReplyTo.setStatus("current")
_CfprApCallhomeSourceSite_Type = SnmpAdminString
_CfprApCallhomeSourceSite_Object = MibTableColumn
cfprApCallhomeSourceSite = _CfprApCallhomeSourceSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 12),
    _CfprApCallhomeSourceSite_Type()
)
cfprApCallhomeSourceSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceSite.setStatus("current")
_CfprApCallhomeSourceUrgency_Type = CfprApCallhomeUrgency
_CfprApCallhomeSourceUrgency_Object = MibTableColumn
cfprApCallhomeSourceUrgency = _CfprApCallhomeSourceUrgency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 12, 1, 13),
    _CfprApCallhomeSourceUrgency_Type()
)
cfprApCallhomeSourceUrgency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeSourceUrgency.setStatus("current")
_CfprApCallhomeTestAlertTable_Object = MibTable
cfprApCallhomeTestAlertTable = _CfprApCallhomeTestAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13)
)
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertTable.setStatus("current")
_CfprApCallhomeTestAlertEntry_Object = MibTableRow
cfprApCallhomeTestAlertEntry = _CfprApCallhomeTestAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1)
)
cfprApCallhomeTestAlertEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CALLHOME-MIB", "cfprApCallhomeTestAlertInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertEntry.setStatus("current")
_CfprApCallhomeTestAlertInstanceId_Type = CfprApManagedObjectId
_CfprApCallhomeTestAlertInstanceId_Object = MibTableColumn
cfprApCallhomeTestAlertInstanceId = _CfprApCallhomeTestAlertInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 1),
    _CfprApCallhomeTestAlertInstanceId_Type()
)
cfprApCallhomeTestAlertInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertInstanceId.setStatus("current")
_CfprApCallhomeTestAlertDn_Type = CfprApManagedObjectDn
_CfprApCallhomeTestAlertDn_Object = MibTableColumn
cfprApCallhomeTestAlertDn = _CfprApCallhomeTestAlertDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 2),
    _CfprApCallhomeTestAlertDn_Type()
)
cfprApCallhomeTestAlertDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertDn.setStatus("current")
_CfprApCallhomeTestAlertRn_Type = SnmpAdminString
_CfprApCallhomeTestAlertRn_Object = MibTableColumn
cfprApCallhomeTestAlertRn = _CfprApCallhomeTestAlertRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 3),
    _CfprApCallhomeTestAlertRn_Type()
)
cfprApCallhomeTestAlertRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertRn.setStatus("current")
_CfprApCallhomeTestAlertDescription_Type = SnmpAdminString
_CfprApCallhomeTestAlertDescription_Object = MibTableColumn
cfprApCallhomeTestAlertDescription = _CfprApCallhomeTestAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 4),
    _CfprApCallhomeTestAlertDescription_Type()
)
cfprApCallhomeTestAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertDescription.setStatus("current")
_CfprApCallhomeTestAlertGroup_Type = CfprApCallhomeAlertGroup
_CfprApCallhomeTestAlertGroup_Object = MibTableColumn
cfprApCallhomeTestAlertGroup = _CfprApCallhomeTestAlertGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 5),
    _CfprApCallhomeTestAlertGroup_Type()
)
cfprApCallhomeTestAlertGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertGroup.setStatus("current")
_CfprApCallhomeTestAlertLevel_Type = CfprApCallhomeAlertLevel
_CfprApCallhomeTestAlertLevel_Object = MibTableColumn
cfprApCallhomeTestAlertLevel = _CfprApCallhomeTestAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 6),
    _CfprApCallhomeTestAlertLevel_Type()
)
cfprApCallhomeTestAlertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertLevel.setStatus("current")
_CfprApCallhomeTestAlertMessageSubtype_Type = CfprApCallhomeAlertMessageSubtype
_CfprApCallhomeTestAlertMessageSubtype_Object = MibTableColumn
cfprApCallhomeTestAlertMessageSubtype = _CfprApCallhomeTestAlertMessageSubtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 7),
    _CfprApCallhomeTestAlertMessageSubtype_Type()
)
cfprApCallhomeTestAlertMessageSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertMessageSubtype.setStatus("current")
_CfprApCallhomeTestAlertMessageType_Type = CfprApCallhomeAlertMessageType
_CfprApCallhomeTestAlertMessageType_Object = MibTableColumn
cfprApCallhomeTestAlertMessageType = _CfprApCallhomeTestAlertMessageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 8),
    _CfprApCallhomeTestAlertMessageType_Type()
)
cfprApCallhomeTestAlertMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertMessageType.setStatus("current")
_CfprApCallhomeTestAlertSendNow_Type = TruthValue
_CfprApCallhomeTestAlertSendNow_Object = MibTableColumn
cfprApCallhomeTestAlertSendNow = _CfprApCallhomeTestAlertSendNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 7, 13, 1, 9),
    _CfprApCallhomeTestAlertSendNow_Type()
)
cfprApCallhomeTestAlertSendNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCallhomeTestAlertSendNow.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-CALLHOME-MIB",
    **{"cfprApCallhomeObjects": cfprApCallhomeObjects,
       "cfprApCallhomeAnonymousReportingTable": cfprApCallhomeAnonymousReportingTable,
       "cfprApCallhomeAnonymousReportingEntry": cfprApCallhomeAnonymousReportingEntry,
       "cfprApCallhomeAnonymousReportingInstanceId": cfprApCallhomeAnonymousReportingInstanceId,
       "cfprApCallhomeAnonymousReportingDn": cfprApCallhomeAnonymousReportingDn,
       "cfprApCallhomeAnonymousReportingRn": cfprApCallhomeAnonymousReportingRn,
       "cfprApCallhomeAnonymousReportingAdminState": cfprApCallhomeAnonymousReportingAdminState,
       "cfprApCallhomeAnonymousReportingCount": cfprApCallhomeAnonymousReportingCount,
       "cfprApCallhomeAnonymousReportingSleepInterval": cfprApCallhomeAnonymousReportingSleepInterval,
       "cfprApCallhomeAnonymousReportingUserAcknowledged": cfprApCallhomeAnonymousReportingUserAcknowledged,
       "cfprApCallhomeDestTable": cfprApCallhomeDestTable,
       "cfprApCallhomeDestEntry": cfprApCallhomeDestEntry,
       "cfprApCallhomeDestInstanceId": cfprApCallhomeDestInstanceId,
       "cfprApCallhomeDestDn": cfprApCallhomeDestDn,
       "cfprApCallhomeDestRn": cfprApCallhomeDestRn,
       "cfprApCallhomeDestAddress": cfprApCallhomeDestAddress,
       "cfprApCallhomeDestName": cfprApCallhomeDestName,
       "cfprApCallhomeDestProtocol": cfprApCallhomeDestProtocol,
       "cfprApCallhomeEpTable": cfprApCallhomeEpTable,
       "cfprApCallhomeEpEntry": cfprApCallhomeEpEntry,
       "cfprApCallhomeEpInstanceId": cfprApCallhomeEpInstanceId,
       "cfprApCallhomeEpDn": cfprApCallhomeEpDn,
       "cfprApCallhomeEpRn": cfprApCallhomeEpRn,
       "cfprApCallhomeEpAdminState": cfprApCallhomeEpAdminState,
       "cfprApCallhomeEpAlertThrottlingAdminState": cfprApCallhomeEpAlertThrottlingAdminState,
       "cfprApCallhomeEpConfigState": cfprApCallhomeEpConfigState,
       "cfprApCallhomeEpDescr": cfprApCallhomeEpDescr,
       "cfprApCallhomeEpFsmDescr": cfprApCallhomeEpFsmDescr,
       "cfprApCallhomeEpFsmPrev": cfprApCallhomeEpFsmPrev,
       "cfprApCallhomeEpFsmProgr": cfprApCallhomeEpFsmProgr,
       "cfprApCallhomeEpFsmRmtInvErrCode": cfprApCallhomeEpFsmRmtInvErrCode,
       "cfprApCallhomeEpFsmRmtInvErrDescr": cfprApCallhomeEpFsmRmtInvErrDescr,
       "cfprApCallhomeEpFsmRmtInvRslt": cfprApCallhomeEpFsmRmtInvRslt,
       "cfprApCallhomeEpFsmStageDescr": cfprApCallhomeEpFsmStageDescr,
       "cfprApCallhomeEpFsmStamp": cfprApCallhomeEpFsmStamp,
       "cfprApCallhomeEpFsmStatus": cfprApCallhomeEpFsmStatus,
       "cfprApCallhomeEpFsmTry": cfprApCallhomeEpFsmTry,
       "cfprApCallhomeEpIntId": cfprApCallhomeEpIntId,
       "cfprApCallhomeEpName": cfprApCallhomeEpName,
       "cfprApCallhomeEpPolicyLevel": cfprApCallhomeEpPolicyLevel,
       "cfprApCallhomeEpPolicyOwner": cfprApCallhomeEpPolicyOwner,
       "cfprApCallhomeEpFsmTable": cfprApCallhomeEpFsmTable,
       "cfprApCallhomeEpFsmEntry": cfprApCallhomeEpFsmEntry,
       "cfprApCallhomeEpFsmInstanceId": cfprApCallhomeEpFsmInstanceId,
       "cfprApCallhomeEpFsmDn": cfprApCallhomeEpFsmDn,
       "cfprApCallhomeEpFsmRn": cfprApCallhomeEpFsmRn,
       "cfprApCallhomeEpFsmCompletionTime": cfprApCallhomeEpFsmCompletionTime,
       "cfprApCallhomeEpFsmCurrentFsm": cfprApCallhomeEpFsmCurrentFsm,
       "cfprApCallhomeEpFsmDescrData": cfprApCallhomeEpFsmDescrData,
       "cfprApCallhomeEpFsmFsmStatus": cfprApCallhomeEpFsmFsmStatus,
       "cfprApCallhomeEpFsmProgress": cfprApCallhomeEpFsmProgress,
       "cfprApCallhomeEpFsmRmtErrCode": cfprApCallhomeEpFsmRmtErrCode,
       "cfprApCallhomeEpFsmRmtErrDescr": cfprApCallhomeEpFsmRmtErrDescr,
       "cfprApCallhomeEpFsmRmtRslt": cfprApCallhomeEpFsmRmtRslt,
       "cfprApCallhomeEpFsmStageTable": cfprApCallhomeEpFsmStageTable,
       "cfprApCallhomeEpFsmStageEntry": cfprApCallhomeEpFsmStageEntry,
       "cfprApCallhomeEpFsmStageInstanceId": cfprApCallhomeEpFsmStageInstanceId,
       "cfprApCallhomeEpFsmStageDn": cfprApCallhomeEpFsmStageDn,
       "cfprApCallhomeEpFsmStageRn": cfprApCallhomeEpFsmStageRn,
       "cfprApCallhomeEpFsmStageDescrData": cfprApCallhomeEpFsmStageDescrData,
       "cfprApCallhomeEpFsmStageLastUpdateTime": cfprApCallhomeEpFsmStageLastUpdateTime,
       "cfprApCallhomeEpFsmStageName": cfprApCallhomeEpFsmStageName,
       "cfprApCallhomeEpFsmStageOrder": cfprApCallhomeEpFsmStageOrder,
       "cfprApCallhomeEpFsmStageRetry": cfprApCallhomeEpFsmStageRetry,
       "cfprApCallhomeEpFsmStageStageStatus": cfprApCallhomeEpFsmStageStageStatus,
       "cfprApCallhomeEpFsmTaskTable": cfprApCallhomeEpFsmTaskTable,
       "cfprApCallhomeEpFsmTaskEntry": cfprApCallhomeEpFsmTaskEntry,
       "cfprApCallhomeEpFsmTaskInstanceId": cfprApCallhomeEpFsmTaskInstanceId,
       "cfprApCallhomeEpFsmTaskDn": cfprApCallhomeEpFsmTaskDn,
       "cfprApCallhomeEpFsmTaskRn": cfprApCallhomeEpFsmTaskRn,
       "cfprApCallhomeEpFsmTaskCompletion": cfprApCallhomeEpFsmTaskCompletion,
       "cfprApCallhomeEpFsmTaskFlags": cfprApCallhomeEpFsmTaskFlags,
       "cfprApCallhomeEpFsmTaskItem": cfprApCallhomeEpFsmTaskItem,
       "cfprApCallhomeEpFsmTaskSeqId": cfprApCallhomeEpFsmTaskSeqId,
       "cfprApCallhomeHttpProxyTable": cfprApCallhomeHttpProxyTable,
       "cfprApCallhomeHttpProxyEntry": cfprApCallhomeHttpProxyEntry,
       "cfprApCallhomeHttpProxyInstanceId": cfprApCallhomeHttpProxyInstanceId,
       "cfprApCallhomeHttpProxyDn": cfprApCallhomeHttpProxyDn,
       "cfprApCallhomeHttpProxyRn": cfprApCallhomeHttpProxyRn,
       "cfprApCallhomeHttpProxyProxyServerEnable": cfprApCallhomeHttpProxyProxyServerEnable,
       "cfprApCallhomeHttpProxyProxyServerPort": cfprApCallhomeHttpProxyProxyServerPort,
       "cfprApCallhomeHttpProxyProxyServerUrl": cfprApCallhomeHttpProxyProxyServerUrl,
       "cfprApCallhomePeriodicSystemInventoryTable": cfprApCallhomePeriodicSystemInventoryTable,
       "cfprApCallhomePeriodicSystemInventoryEntry": cfprApCallhomePeriodicSystemInventoryEntry,
       "cfprApCallhomePeriodicSystemInventoryInstanceId": cfprApCallhomePeriodicSystemInventoryInstanceId,
       "cfprApCallhomePeriodicSystemInventoryDn": cfprApCallhomePeriodicSystemInventoryDn,
       "cfprApCallhomePeriodicSystemInventoryRn": cfprApCallhomePeriodicSystemInventoryRn,
       "cfprApCallhomePeriodicSystemInventoryAdminState": cfprApCallhomePeriodicSystemInventoryAdminState,
       "cfprApCallhomePeriodicSystemInventoryIntervalDays": cfprApCallhomePeriodicSystemInventoryIntervalDays,
       "cfprApCallhomePeriodicSystemInventoryLastDeadline": cfprApCallhomePeriodicSystemInventoryLastDeadline,
       "cfprApCallhomePeriodicSystemInventoryMaximumRetryCount": cfprApCallhomePeriodicSystemInventoryMaximumRetryCount,
       "cfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds": cfprApCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds,
       "cfprApCallhomePeriodicSystemInventoryNextDeadline": cfprApCallhomePeriodicSystemInventoryNextDeadline,
       "cfprApCallhomePeriodicSystemInventoryPollIntervalSeconds": cfprApCallhomePeriodicSystemInventoryPollIntervalSeconds,
       "cfprApCallhomePeriodicSystemInventoryRetryCount": cfprApCallhomePeriodicSystemInventoryRetryCount,
       "cfprApCallhomePeriodicSystemInventoryRetryDelayMinutes": cfprApCallhomePeriodicSystemInventoryRetryDelayMinutes,
       "cfprApCallhomePeriodicSystemInventorySendNow": cfprApCallhomePeriodicSystemInventorySendNow,
       "cfprApCallhomePeriodicSystemInventoryTimeOfDayHour": cfprApCallhomePeriodicSystemInventoryTimeOfDayHour,
       "cfprApCallhomePeriodicSystemInventoryTimeOfDayMinute": cfprApCallhomePeriodicSystemInventoryTimeOfDayMinute,
       "cfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt": cfprApCallhomePeriodicSystemInventoryTimeOfLastAttempt,
       "cfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess": cfprApCallhomePeriodicSystemInventoryTimeOfLastSuccess,
       "cfprApCallhomePolicyTable": cfprApCallhomePolicyTable,
       "cfprApCallhomePolicyEntry": cfprApCallhomePolicyEntry,
       "cfprApCallhomePolicyInstanceId": cfprApCallhomePolicyInstanceId,
       "cfprApCallhomePolicyDn": cfprApCallhomePolicyDn,
       "cfprApCallhomePolicyRn": cfprApCallhomePolicyRn,
       "cfprApCallhomePolicyAdminState": cfprApCallhomePolicyAdminState,
       "cfprApCallhomePolicyCause": cfprApCallhomePolicyCause,
       "cfprApCallhomePolicyDescr": cfprApCallhomePolicyDescr,
       "cfprApCallhomePolicyName": cfprApCallhomePolicyName,
       "cfprApCallhomeProfileTable": cfprApCallhomeProfileTable,
       "cfprApCallhomeProfileEntry": cfprApCallhomeProfileEntry,
       "cfprApCallhomeProfileInstanceId": cfprApCallhomeProfileInstanceId,
       "cfprApCallhomeProfileDn": cfprApCallhomeProfileDn,
       "cfprApCallhomeProfileRn": cfprApCallhomeProfileRn,
       "cfprApCallhomeProfileAlertGroups": cfprApCallhomeProfileAlertGroups,
       "cfprApCallhomeProfileDescr": cfprApCallhomeProfileDescr,
       "cfprApCallhomeProfileFormat": cfprApCallhomeProfileFormat,
       "cfprApCallhomeProfileLevel": cfprApCallhomeProfileLevel,
       "cfprApCallhomeProfileMaxSize": cfprApCallhomeProfileMaxSize,
       "cfprApCallhomeProfileName": cfprApCallhomeProfileName,
       "cfprApCallhomeProfileReporting": cfprApCallhomeProfileReporting,
       "cfprApCallhomeSmtpTable": cfprApCallhomeSmtpTable,
       "cfprApCallhomeSmtpEntry": cfprApCallhomeSmtpEntry,
       "cfprApCallhomeSmtpInstanceId": cfprApCallhomeSmtpInstanceId,
       "cfprApCallhomeSmtpDn": cfprApCallhomeSmtpDn,
       "cfprApCallhomeSmtpRn": cfprApCallhomeSmtpRn,
       "cfprApCallhomeSmtpHost": cfprApCallhomeSmtpHost,
       "cfprApCallhomeSmtpPort": cfprApCallhomeSmtpPort,
       "cfprApCallhomeSourceTable": cfprApCallhomeSourceTable,
       "cfprApCallhomeSourceEntry": cfprApCallhomeSourceEntry,
       "cfprApCallhomeSourceInstanceId": cfprApCallhomeSourceInstanceId,
       "cfprApCallhomeSourceDn": cfprApCallhomeSourceDn,
       "cfprApCallhomeSourceRn": cfprApCallhomeSourceRn,
       "cfprApCallhomeSourceAddr": cfprApCallhomeSourceAddr,
       "cfprApCallhomeSourceContact": cfprApCallhomeSourceContact,
       "cfprApCallhomeSourceContract": cfprApCallhomeSourceContract,
       "cfprApCallhomeSourceCustomer": cfprApCallhomeSourceCustomer,
       "cfprApCallhomeSourceEmail": cfprApCallhomeSourceEmail,
       "cfprApCallhomeSourceFrom": cfprApCallhomeSourceFrom,
       "cfprApCallhomeSourcePhone": cfprApCallhomeSourcePhone,
       "cfprApCallhomeSourceReplyTo": cfprApCallhomeSourceReplyTo,
       "cfprApCallhomeSourceSite": cfprApCallhomeSourceSite,
       "cfprApCallhomeSourceUrgency": cfprApCallhomeSourceUrgency,
       "cfprApCallhomeTestAlertTable": cfprApCallhomeTestAlertTable,
       "cfprApCallhomeTestAlertEntry": cfprApCallhomeTestAlertEntry,
       "cfprApCallhomeTestAlertInstanceId": cfprApCallhomeTestAlertInstanceId,
       "cfprApCallhomeTestAlertDn": cfprApCallhomeTestAlertDn,
       "cfprApCallhomeTestAlertRn": cfprApCallhomeTestAlertRn,
       "cfprApCallhomeTestAlertDescription": cfprApCallhomeTestAlertDescription,
       "cfprApCallhomeTestAlertGroup": cfprApCallhomeTestAlertGroup,
       "cfprApCallhomeTestAlertLevel": cfprApCallhomeTestAlertLevel,
       "cfprApCallhomeTestAlertMessageSubtype": cfprApCallhomeTestAlertMessageSubtype,
       "cfprApCallhomeTestAlertMessageType": cfprApCallhomeTestAlertMessageType,
       "cfprApCallhomeTestAlertSendNow": cfprApCallhomeTestAlertSendNow}
)
