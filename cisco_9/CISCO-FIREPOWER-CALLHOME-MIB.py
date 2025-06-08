# SNMP MIB module (CISCO-FIREPOWER-CALLHOME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-CALLHOME-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:40 2025
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

(CfprCallhomeAdminState,
 CfprCallhomeAlertGroup,
 CfprCallhomeAlertGroups,
 CfprCallhomeAlertLevel,
 CfprCallhomeAlertMessageSubtype,
 CfprCallhomeAlertMessageType,
 CfprCallhomeAlertThrottlingAdminState,
 CfprCallhomeAnonymousReportingAdminState,
 CfprCallhomeCallhomeProtocol,
 CfprCallhomeEpConfigState,
 CfprCallhomeEpFsmCurrentFsm,
 CfprCallhomeEpFsmStageName,
 CfprCallhomeEpFsmTaskItem,
 CfprCallhomeFormat,
 CfprCallhomeHttpProxyEnable,
 CfprCallhomeLevel,
 CfprCallhomePolicyAdminState,
 CfprCallhomeReportingType,
 CfprCallhomeUrgency,
 CfprConditionCallHomeCause,
 CfprConditionRemoteInvRslt,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprCallhomeAdminState",
    "CfprCallhomeAlertGroup",
    "CfprCallhomeAlertGroups",
    "CfprCallhomeAlertLevel",
    "CfprCallhomeAlertMessageSubtype",
    "CfprCallhomeAlertMessageType",
    "CfprCallhomeAlertThrottlingAdminState",
    "CfprCallhomeAnonymousReportingAdminState",
    "CfprCallhomeCallhomeProtocol",
    "CfprCallhomeEpConfigState",
    "CfprCallhomeEpFsmCurrentFsm",
    "CfprCallhomeEpFsmStageName",
    "CfprCallhomeEpFsmTaskItem",
    "CfprCallhomeFormat",
    "CfprCallhomeHttpProxyEnable",
    "CfprCallhomeLevel",
    "CfprCallhomePolicyAdminState",
    "CfprCallhomeReportingType",
    "CfprCallhomeUrgency",
    "CfprConditionCallHomeCause",
    "CfprConditionRemoteInvRslt",
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

cfprCallhomeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprCallhomeAnonymousReportingTable_Object = MibTable
cfprCallhomeAnonymousReportingTable = _CfprCallhomeAnonymousReportingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingTable.setStatus("current")
_CfprCallhomeAnonymousReportingEntry_Object = MibTableRow
cfprCallhomeAnonymousReportingEntry = _CfprCallhomeAnonymousReportingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1, 1)
)
cfprCallhomeAnonymousReportingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeAnonymousReportingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingEntry.setStatus("current")
_CfprCallhomeAnonymousReportingInstanceId_Type = CfprManagedObjectId
_CfprCallhomeAnonymousReportingInstanceId_Object = MibTableColumn
cfprCallhomeAnonymousReportingInstanceId = _CfprCallhomeAnonymousReportingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1, 1, 1),
    _CfprCallhomeAnonymousReportingInstanceId_Type()
)
cfprCallhomeAnonymousReportingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingInstanceId.setStatus("current")
_CfprCallhomeAnonymousReportingDn_Type = CfprManagedObjectDn
_CfprCallhomeAnonymousReportingDn_Object = MibTableColumn
cfprCallhomeAnonymousReportingDn = _CfprCallhomeAnonymousReportingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1, 1, 2),
    _CfprCallhomeAnonymousReportingDn_Type()
)
cfprCallhomeAnonymousReportingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingDn.setStatus("current")
_CfprCallhomeAnonymousReportingRn_Type = SnmpAdminString
_CfprCallhomeAnonymousReportingRn_Object = MibTableColumn
cfprCallhomeAnonymousReportingRn = _CfprCallhomeAnonymousReportingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1, 1, 3),
    _CfprCallhomeAnonymousReportingRn_Type()
)
cfprCallhomeAnonymousReportingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingRn.setStatus("current")
_CfprCallhomeAnonymousReportingAdminState_Type = CfprCallhomeAnonymousReportingAdminState
_CfprCallhomeAnonymousReportingAdminState_Object = MibTableColumn
cfprCallhomeAnonymousReportingAdminState = _CfprCallhomeAnonymousReportingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1, 1, 4),
    _CfprCallhomeAnonymousReportingAdminState_Type()
)
cfprCallhomeAnonymousReportingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingAdminState.setStatus("current")
_CfprCallhomeAnonymousReportingCount_Type = Gauge32
_CfprCallhomeAnonymousReportingCount_Object = MibTableColumn
cfprCallhomeAnonymousReportingCount = _CfprCallhomeAnonymousReportingCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1, 1, 5),
    _CfprCallhomeAnonymousReportingCount_Type()
)
cfprCallhomeAnonymousReportingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingCount.setStatus("current")
_CfprCallhomeAnonymousReportingSleepInterval_Type = Gauge32
_CfprCallhomeAnonymousReportingSleepInterval_Object = MibTableColumn
cfprCallhomeAnonymousReportingSleepInterval = _CfprCallhomeAnonymousReportingSleepInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1, 1, 6),
    _CfprCallhomeAnonymousReportingSleepInterval_Type()
)
cfprCallhomeAnonymousReportingSleepInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingSleepInterval.setStatus("current")
_CfprCallhomeAnonymousReportingUserAcknowledged_Type = TruthValue
_CfprCallhomeAnonymousReportingUserAcknowledged_Object = MibTableColumn
cfprCallhomeAnonymousReportingUserAcknowledged = _CfprCallhomeAnonymousReportingUserAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 1, 1, 7),
    _CfprCallhomeAnonymousReportingUserAcknowledged_Type()
)
cfprCallhomeAnonymousReportingUserAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeAnonymousReportingUserAcknowledged.setStatus("current")
_CfprCallhomeDestTable_Object = MibTable
cfprCallhomeDestTable = _CfprCallhomeDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cfprCallhomeDestTable.setStatus("current")
_CfprCallhomeDestEntry_Object = MibTableRow
cfprCallhomeDestEntry = _CfprCallhomeDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 2, 1)
)
cfprCallhomeDestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeDestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeDestEntry.setStatus("current")
_CfprCallhomeDestInstanceId_Type = CfprManagedObjectId
_CfprCallhomeDestInstanceId_Object = MibTableColumn
cfprCallhomeDestInstanceId = _CfprCallhomeDestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 2, 1, 1),
    _CfprCallhomeDestInstanceId_Type()
)
cfprCallhomeDestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeDestInstanceId.setStatus("current")
_CfprCallhomeDestDn_Type = CfprManagedObjectDn
_CfprCallhomeDestDn_Object = MibTableColumn
cfprCallhomeDestDn = _CfprCallhomeDestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 2, 1, 2),
    _CfprCallhomeDestDn_Type()
)
cfprCallhomeDestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeDestDn.setStatus("current")
_CfprCallhomeDestRn_Type = SnmpAdminString
_CfprCallhomeDestRn_Object = MibTableColumn
cfprCallhomeDestRn = _CfprCallhomeDestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 2, 1, 3),
    _CfprCallhomeDestRn_Type()
)
cfprCallhomeDestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeDestRn.setStatus("current")
_CfprCallhomeDestAddress_Type = SnmpAdminString
_CfprCallhomeDestAddress_Object = MibTableColumn
cfprCallhomeDestAddress = _CfprCallhomeDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 2, 1, 4),
    _CfprCallhomeDestAddress_Type()
)
cfprCallhomeDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeDestAddress.setStatus("current")
_CfprCallhomeDestName_Type = SnmpAdminString
_CfprCallhomeDestName_Object = MibTableColumn
cfprCallhomeDestName = _CfprCallhomeDestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 2, 1, 5),
    _CfprCallhomeDestName_Type()
)
cfprCallhomeDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeDestName.setStatus("current")
_CfprCallhomeDestProtocol_Type = CfprCallhomeCallhomeProtocol
_CfprCallhomeDestProtocol_Object = MibTableColumn
cfprCallhomeDestProtocol = _CfprCallhomeDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 2, 1, 6),
    _CfprCallhomeDestProtocol_Type()
)
cfprCallhomeDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeDestProtocol.setStatus("current")
_CfprCallhomeEpTable_Object = MibTable
cfprCallhomeEpTable = _CfprCallhomeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cfprCallhomeEpTable.setStatus("current")
_CfprCallhomeEpEntry_Object = MibTableRow
cfprCallhomeEpEntry = _CfprCallhomeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1)
)
cfprCallhomeEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeEpEntry.setStatus("current")
_CfprCallhomeEpInstanceId_Type = CfprManagedObjectId
_CfprCallhomeEpInstanceId_Object = MibTableColumn
cfprCallhomeEpInstanceId = _CfprCallhomeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 1),
    _CfprCallhomeEpInstanceId_Type()
)
cfprCallhomeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeEpInstanceId.setStatus("current")
_CfprCallhomeEpDn_Type = CfprManagedObjectDn
_CfprCallhomeEpDn_Object = MibTableColumn
cfprCallhomeEpDn = _CfprCallhomeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 2),
    _CfprCallhomeEpDn_Type()
)
cfprCallhomeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpDn.setStatus("current")
_CfprCallhomeEpRn_Type = SnmpAdminString
_CfprCallhomeEpRn_Object = MibTableColumn
cfprCallhomeEpRn = _CfprCallhomeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 3),
    _CfprCallhomeEpRn_Type()
)
cfprCallhomeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpRn.setStatus("current")
_CfprCallhomeEpAdminState_Type = CfprCallhomeAdminState
_CfprCallhomeEpAdminState_Object = MibTableColumn
cfprCallhomeEpAdminState = _CfprCallhomeEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 4),
    _CfprCallhomeEpAdminState_Type()
)
cfprCallhomeEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpAdminState.setStatus("current")
_CfprCallhomeEpAlertThrottlingAdminState_Type = CfprCallhomeAlertThrottlingAdminState
_CfprCallhomeEpAlertThrottlingAdminState_Object = MibTableColumn
cfprCallhomeEpAlertThrottlingAdminState = _CfprCallhomeEpAlertThrottlingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 5),
    _CfprCallhomeEpAlertThrottlingAdminState_Type()
)
cfprCallhomeEpAlertThrottlingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpAlertThrottlingAdminState.setStatus("current")
_CfprCallhomeEpConfigState_Type = CfprCallhomeEpConfigState
_CfprCallhomeEpConfigState_Object = MibTableColumn
cfprCallhomeEpConfigState = _CfprCallhomeEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 6),
    _CfprCallhomeEpConfigState_Type()
)
cfprCallhomeEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpConfigState.setStatus("current")
_CfprCallhomeEpDescr_Type = SnmpAdminString
_CfprCallhomeEpDescr_Object = MibTableColumn
cfprCallhomeEpDescr = _CfprCallhomeEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 7),
    _CfprCallhomeEpDescr_Type()
)
cfprCallhomeEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpDescr.setStatus("current")
_CfprCallhomeEpFsmDescr_Type = SnmpAdminString
_CfprCallhomeEpFsmDescr_Object = MibTableColumn
cfprCallhomeEpFsmDescr = _CfprCallhomeEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 8),
    _CfprCallhomeEpFsmDescr_Type()
)
cfprCallhomeEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmDescr.setStatus("current")
_CfprCallhomeEpFsmPrev_Type = SnmpAdminString
_CfprCallhomeEpFsmPrev_Object = MibTableColumn
cfprCallhomeEpFsmPrev = _CfprCallhomeEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 9),
    _CfprCallhomeEpFsmPrev_Type()
)
cfprCallhomeEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmPrev.setStatus("current")
_CfprCallhomeEpFsmProgr_Type = Gauge32
_CfprCallhomeEpFsmProgr_Object = MibTableColumn
cfprCallhomeEpFsmProgr = _CfprCallhomeEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 10),
    _CfprCallhomeEpFsmProgr_Type()
)
cfprCallhomeEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmProgr.setStatus("current")
_CfprCallhomeEpFsmRmtInvErrCode_Type = Gauge32
_CfprCallhomeEpFsmRmtInvErrCode_Object = MibTableColumn
cfprCallhomeEpFsmRmtInvErrCode = _CfprCallhomeEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 11),
    _CfprCallhomeEpFsmRmtInvErrCode_Type()
)
cfprCallhomeEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmRmtInvErrCode.setStatus("current")
_CfprCallhomeEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprCallhomeEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprCallhomeEpFsmRmtInvErrDescr = _CfprCallhomeEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 12),
    _CfprCallhomeEpFsmRmtInvErrDescr_Type()
)
cfprCallhomeEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmRmtInvErrDescr.setStatus("current")
_CfprCallhomeEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprCallhomeEpFsmRmtInvRslt_Object = MibTableColumn
cfprCallhomeEpFsmRmtInvRslt = _CfprCallhomeEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 13),
    _CfprCallhomeEpFsmRmtInvRslt_Type()
)
cfprCallhomeEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmRmtInvRslt.setStatus("current")
_CfprCallhomeEpFsmStageDescr_Type = SnmpAdminString
_CfprCallhomeEpFsmStageDescr_Object = MibTableColumn
cfprCallhomeEpFsmStageDescr = _CfprCallhomeEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 14),
    _CfprCallhomeEpFsmStageDescr_Type()
)
cfprCallhomeEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageDescr.setStatus("current")
_CfprCallhomeEpFsmStamp_Type = DateAndTime
_CfprCallhomeEpFsmStamp_Object = MibTableColumn
cfprCallhomeEpFsmStamp = _CfprCallhomeEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 15),
    _CfprCallhomeEpFsmStamp_Type()
)
cfprCallhomeEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStamp.setStatus("current")
_CfprCallhomeEpFsmStatus_Type = SnmpAdminString
_CfprCallhomeEpFsmStatus_Object = MibTableColumn
cfprCallhomeEpFsmStatus = _CfprCallhomeEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 16),
    _CfprCallhomeEpFsmStatus_Type()
)
cfprCallhomeEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStatus.setStatus("current")
_CfprCallhomeEpFsmTry_Type = Gauge32
_CfprCallhomeEpFsmTry_Object = MibTableColumn
cfprCallhomeEpFsmTry = _CfprCallhomeEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 17),
    _CfprCallhomeEpFsmTry_Type()
)
cfprCallhomeEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTry.setStatus("current")
_CfprCallhomeEpIntId_Type = SnmpAdminString
_CfprCallhomeEpIntId_Object = MibTableColumn
cfprCallhomeEpIntId = _CfprCallhomeEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 18),
    _CfprCallhomeEpIntId_Type()
)
cfprCallhomeEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpIntId.setStatus("current")
_CfprCallhomeEpName_Type = SnmpAdminString
_CfprCallhomeEpName_Object = MibTableColumn
cfprCallhomeEpName = _CfprCallhomeEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 19),
    _CfprCallhomeEpName_Type()
)
cfprCallhomeEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpName.setStatus("current")
_CfprCallhomeEpPolicyLevel_Type = Gauge32
_CfprCallhomeEpPolicyLevel_Object = MibTableColumn
cfprCallhomeEpPolicyLevel = _CfprCallhomeEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 20),
    _CfprCallhomeEpPolicyLevel_Type()
)
cfprCallhomeEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpPolicyLevel.setStatus("current")
_CfprCallhomeEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCallhomeEpPolicyOwner_Object = MibTableColumn
cfprCallhomeEpPolicyOwner = _CfprCallhomeEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 3, 1, 21),
    _CfprCallhomeEpPolicyOwner_Type()
)
cfprCallhomeEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpPolicyOwner.setStatus("current")
_CfprCallhomeEpFsmTable_Object = MibTable
cfprCallhomeEpFsmTable = _CfprCallhomeEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTable.setStatus("current")
_CfprCallhomeEpFsmEntry_Object = MibTableRow
cfprCallhomeEpFsmEntry = _CfprCallhomeEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1)
)
cfprCallhomeEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmEntry.setStatus("current")
_CfprCallhomeEpFsmInstanceId_Type = CfprManagedObjectId
_CfprCallhomeEpFsmInstanceId_Object = MibTableColumn
cfprCallhomeEpFsmInstanceId = _CfprCallhomeEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 1),
    _CfprCallhomeEpFsmInstanceId_Type()
)
cfprCallhomeEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmInstanceId.setStatus("current")
_CfprCallhomeEpFsmDn_Type = CfprManagedObjectDn
_CfprCallhomeEpFsmDn_Object = MibTableColumn
cfprCallhomeEpFsmDn = _CfprCallhomeEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 2),
    _CfprCallhomeEpFsmDn_Type()
)
cfprCallhomeEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmDn.setStatus("current")
_CfprCallhomeEpFsmRn_Type = SnmpAdminString
_CfprCallhomeEpFsmRn_Object = MibTableColumn
cfprCallhomeEpFsmRn = _CfprCallhomeEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 3),
    _CfprCallhomeEpFsmRn_Type()
)
cfprCallhomeEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmRn.setStatus("current")
_CfprCallhomeEpFsmCompletionTime_Type = DateAndTime
_CfprCallhomeEpFsmCompletionTime_Object = MibTableColumn
cfprCallhomeEpFsmCompletionTime = _CfprCallhomeEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 4),
    _CfprCallhomeEpFsmCompletionTime_Type()
)
cfprCallhomeEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmCompletionTime.setStatus("current")
_CfprCallhomeEpFsmCurrentFsm_Type = CfprCallhomeEpFsmCurrentFsm
_CfprCallhomeEpFsmCurrentFsm_Object = MibTableColumn
cfprCallhomeEpFsmCurrentFsm = _CfprCallhomeEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 5),
    _CfprCallhomeEpFsmCurrentFsm_Type()
)
cfprCallhomeEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmCurrentFsm.setStatus("current")
_CfprCallhomeEpFsmDescrData_Type = SnmpAdminString
_CfprCallhomeEpFsmDescrData_Object = MibTableColumn
cfprCallhomeEpFsmDescrData = _CfprCallhomeEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 6),
    _CfprCallhomeEpFsmDescrData_Type()
)
cfprCallhomeEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmDescrData.setStatus("current")
_CfprCallhomeEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprCallhomeEpFsmFsmStatus_Object = MibTableColumn
cfprCallhomeEpFsmFsmStatus = _CfprCallhomeEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 7),
    _CfprCallhomeEpFsmFsmStatus_Type()
)
cfprCallhomeEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmFsmStatus.setStatus("current")
_CfprCallhomeEpFsmProgress_Type = Gauge32
_CfprCallhomeEpFsmProgress_Object = MibTableColumn
cfprCallhomeEpFsmProgress = _CfprCallhomeEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 8),
    _CfprCallhomeEpFsmProgress_Type()
)
cfprCallhomeEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmProgress.setStatus("current")
_CfprCallhomeEpFsmRmtErrCode_Type = Gauge32
_CfprCallhomeEpFsmRmtErrCode_Object = MibTableColumn
cfprCallhomeEpFsmRmtErrCode = _CfprCallhomeEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 9),
    _CfprCallhomeEpFsmRmtErrCode_Type()
)
cfprCallhomeEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmRmtErrCode.setStatus("current")
_CfprCallhomeEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprCallhomeEpFsmRmtErrDescr_Object = MibTableColumn
cfprCallhomeEpFsmRmtErrDescr = _CfprCallhomeEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 10),
    _CfprCallhomeEpFsmRmtErrDescr_Type()
)
cfprCallhomeEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmRmtErrDescr.setStatus("current")
_CfprCallhomeEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprCallhomeEpFsmRmtRslt_Object = MibTableColumn
cfprCallhomeEpFsmRmtRslt = _CfprCallhomeEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 4, 1, 11),
    _CfprCallhomeEpFsmRmtRslt_Type()
)
cfprCallhomeEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmRmtRslt.setStatus("current")
_CfprCallhomeEpFsmStageTable_Object = MibTable
cfprCallhomeEpFsmStageTable = _CfprCallhomeEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5)
)
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageTable.setStatus("current")
_CfprCallhomeEpFsmStageEntry_Object = MibTableRow
cfprCallhomeEpFsmStageEntry = _CfprCallhomeEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1)
)
cfprCallhomeEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageEntry.setStatus("current")
_CfprCallhomeEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprCallhomeEpFsmStageInstanceId_Object = MibTableColumn
cfprCallhomeEpFsmStageInstanceId = _CfprCallhomeEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 1),
    _CfprCallhomeEpFsmStageInstanceId_Type()
)
cfprCallhomeEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageInstanceId.setStatus("current")
_CfprCallhomeEpFsmStageDn_Type = CfprManagedObjectDn
_CfprCallhomeEpFsmStageDn_Object = MibTableColumn
cfprCallhomeEpFsmStageDn = _CfprCallhomeEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 2),
    _CfprCallhomeEpFsmStageDn_Type()
)
cfprCallhomeEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageDn.setStatus("current")
_CfprCallhomeEpFsmStageRn_Type = SnmpAdminString
_CfprCallhomeEpFsmStageRn_Object = MibTableColumn
cfprCallhomeEpFsmStageRn = _CfprCallhomeEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 3),
    _CfprCallhomeEpFsmStageRn_Type()
)
cfprCallhomeEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageRn.setStatus("current")
_CfprCallhomeEpFsmStageDescrData_Type = SnmpAdminString
_CfprCallhomeEpFsmStageDescrData_Object = MibTableColumn
cfprCallhomeEpFsmStageDescrData = _CfprCallhomeEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 4),
    _CfprCallhomeEpFsmStageDescrData_Type()
)
cfprCallhomeEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageDescrData.setStatus("current")
_CfprCallhomeEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprCallhomeEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprCallhomeEpFsmStageLastUpdateTime = _CfprCallhomeEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 5),
    _CfprCallhomeEpFsmStageLastUpdateTime_Type()
)
cfprCallhomeEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageLastUpdateTime.setStatus("current")
_CfprCallhomeEpFsmStageName_Type = CfprCallhomeEpFsmStageName
_CfprCallhomeEpFsmStageName_Object = MibTableColumn
cfprCallhomeEpFsmStageName = _CfprCallhomeEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 6),
    _CfprCallhomeEpFsmStageName_Type()
)
cfprCallhomeEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageName.setStatus("current")
_CfprCallhomeEpFsmStageOrder_Type = Gauge32
_CfprCallhomeEpFsmStageOrder_Object = MibTableColumn
cfprCallhomeEpFsmStageOrder = _CfprCallhomeEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 7),
    _CfprCallhomeEpFsmStageOrder_Type()
)
cfprCallhomeEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageOrder.setStatus("current")
_CfprCallhomeEpFsmStageRetry_Type = Gauge32
_CfprCallhomeEpFsmStageRetry_Object = MibTableColumn
cfprCallhomeEpFsmStageRetry = _CfprCallhomeEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 8),
    _CfprCallhomeEpFsmStageRetry_Type()
)
cfprCallhomeEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageRetry.setStatus("current")
_CfprCallhomeEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprCallhomeEpFsmStageStageStatus_Object = MibTableColumn
cfprCallhomeEpFsmStageStageStatus = _CfprCallhomeEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 5, 1, 9),
    _CfprCallhomeEpFsmStageStageStatus_Type()
)
cfprCallhomeEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmStageStageStatus.setStatus("current")
_CfprCallhomeEpFsmTaskTable_Object = MibTable
cfprCallhomeEpFsmTaskTable = _CfprCallhomeEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6)
)
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskTable.setStatus("current")
_CfprCallhomeEpFsmTaskEntry_Object = MibTableRow
cfprCallhomeEpFsmTaskEntry = _CfprCallhomeEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6, 1)
)
cfprCallhomeEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskEntry.setStatus("current")
_CfprCallhomeEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprCallhomeEpFsmTaskInstanceId_Object = MibTableColumn
cfprCallhomeEpFsmTaskInstanceId = _CfprCallhomeEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6, 1, 1),
    _CfprCallhomeEpFsmTaskInstanceId_Type()
)
cfprCallhomeEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskInstanceId.setStatus("current")
_CfprCallhomeEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprCallhomeEpFsmTaskDn_Object = MibTableColumn
cfprCallhomeEpFsmTaskDn = _CfprCallhomeEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6, 1, 2),
    _CfprCallhomeEpFsmTaskDn_Type()
)
cfprCallhomeEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskDn.setStatus("current")
_CfprCallhomeEpFsmTaskRn_Type = SnmpAdminString
_CfprCallhomeEpFsmTaskRn_Object = MibTableColumn
cfprCallhomeEpFsmTaskRn = _CfprCallhomeEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6, 1, 3),
    _CfprCallhomeEpFsmTaskRn_Type()
)
cfprCallhomeEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskRn.setStatus("current")
_CfprCallhomeEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprCallhomeEpFsmTaskCompletion_Object = MibTableColumn
cfprCallhomeEpFsmTaskCompletion = _CfprCallhomeEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6, 1, 4),
    _CfprCallhomeEpFsmTaskCompletion_Type()
)
cfprCallhomeEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskCompletion.setStatus("current")
_CfprCallhomeEpFsmTaskFlags_Type = CfprFsmFlags
_CfprCallhomeEpFsmTaskFlags_Object = MibTableColumn
cfprCallhomeEpFsmTaskFlags = _CfprCallhomeEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6, 1, 5),
    _CfprCallhomeEpFsmTaskFlags_Type()
)
cfprCallhomeEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskFlags.setStatus("current")
_CfprCallhomeEpFsmTaskItem_Type = CfprCallhomeEpFsmTaskItem
_CfprCallhomeEpFsmTaskItem_Object = MibTableColumn
cfprCallhomeEpFsmTaskItem = _CfprCallhomeEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6, 1, 6),
    _CfprCallhomeEpFsmTaskItem_Type()
)
cfprCallhomeEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskItem.setStatus("current")
_CfprCallhomeEpFsmTaskSeqId_Type = Gauge32
_CfprCallhomeEpFsmTaskSeqId_Object = MibTableColumn
cfprCallhomeEpFsmTaskSeqId = _CfprCallhomeEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 6, 1, 7),
    _CfprCallhomeEpFsmTaskSeqId_Type()
)
cfprCallhomeEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeEpFsmTaskSeqId.setStatus("current")
_CfprCallhomeHttpProxyTable_Object = MibTable
cfprCallhomeHttpProxyTable = _CfprCallhomeHttpProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 7)
)
if mibBuilder.loadTexts:
    cfprCallhomeHttpProxyTable.setStatus("current")
_CfprCallhomeHttpProxyEntry_Object = MibTableRow
cfprCallhomeHttpProxyEntry = _CfprCallhomeHttpProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 7, 1)
)
cfprCallhomeHttpProxyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeHttpProxyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeHttpProxyEntry.setStatus("current")
_CfprCallhomeHttpProxyInstanceId_Type = CfprManagedObjectId
_CfprCallhomeHttpProxyInstanceId_Object = MibTableColumn
cfprCallhomeHttpProxyInstanceId = _CfprCallhomeHttpProxyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 7, 1, 1),
    _CfprCallhomeHttpProxyInstanceId_Type()
)
cfprCallhomeHttpProxyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeHttpProxyInstanceId.setStatus("current")
_CfprCallhomeHttpProxyDn_Type = CfprManagedObjectDn
_CfprCallhomeHttpProxyDn_Object = MibTableColumn
cfprCallhomeHttpProxyDn = _CfprCallhomeHttpProxyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 7, 1, 2),
    _CfprCallhomeHttpProxyDn_Type()
)
cfprCallhomeHttpProxyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeHttpProxyDn.setStatus("current")
_CfprCallhomeHttpProxyRn_Type = SnmpAdminString
_CfprCallhomeHttpProxyRn_Object = MibTableColumn
cfprCallhomeHttpProxyRn = _CfprCallhomeHttpProxyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 7, 1, 3),
    _CfprCallhomeHttpProxyRn_Type()
)
cfprCallhomeHttpProxyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeHttpProxyRn.setStatus("current")
_CfprCallhomeHttpProxyProxyServerEnable_Type = CfprCallhomeHttpProxyEnable
_CfprCallhomeHttpProxyProxyServerEnable_Object = MibTableColumn
cfprCallhomeHttpProxyProxyServerEnable = _CfprCallhomeHttpProxyProxyServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 7, 1, 4),
    _CfprCallhomeHttpProxyProxyServerEnable_Type()
)
cfprCallhomeHttpProxyProxyServerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeHttpProxyProxyServerEnable.setStatus("current")
_CfprCallhomeHttpProxyProxyServerPort_Type = Gauge32
_CfprCallhomeHttpProxyProxyServerPort_Object = MibTableColumn
cfprCallhomeHttpProxyProxyServerPort = _CfprCallhomeHttpProxyProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 7, 1, 5),
    _CfprCallhomeHttpProxyProxyServerPort_Type()
)
cfprCallhomeHttpProxyProxyServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeHttpProxyProxyServerPort.setStatus("current")
_CfprCallhomeHttpProxyProxyServerUrl_Type = SnmpAdminString
_CfprCallhomeHttpProxyProxyServerUrl_Object = MibTableColumn
cfprCallhomeHttpProxyProxyServerUrl = _CfprCallhomeHttpProxyProxyServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 7, 1, 6),
    _CfprCallhomeHttpProxyProxyServerUrl_Type()
)
cfprCallhomeHttpProxyProxyServerUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeHttpProxyProxyServerUrl.setStatus("current")
_CfprCallhomePeriodicSystemInventoryTable_Object = MibTable
cfprCallhomePeriodicSystemInventoryTable = _CfprCallhomePeriodicSystemInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8)
)
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryTable.setStatus("current")
_CfprCallhomePeriodicSystemInventoryEntry_Object = MibTableRow
cfprCallhomePeriodicSystemInventoryEntry = _CfprCallhomePeriodicSystemInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1)
)
cfprCallhomePeriodicSystemInventoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomePeriodicSystemInventoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryEntry.setStatus("current")
_CfprCallhomePeriodicSystemInventoryInstanceId_Type = CfprManagedObjectId
_CfprCallhomePeriodicSystemInventoryInstanceId_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryInstanceId = _CfprCallhomePeriodicSystemInventoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 1),
    _CfprCallhomePeriodicSystemInventoryInstanceId_Type()
)
cfprCallhomePeriodicSystemInventoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryInstanceId.setStatus("current")
_CfprCallhomePeriodicSystemInventoryDn_Type = CfprManagedObjectDn
_CfprCallhomePeriodicSystemInventoryDn_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryDn = _CfprCallhomePeriodicSystemInventoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 2),
    _CfprCallhomePeriodicSystemInventoryDn_Type()
)
cfprCallhomePeriodicSystemInventoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryDn.setStatus("current")
_CfprCallhomePeriodicSystemInventoryRn_Type = SnmpAdminString
_CfprCallhomePeriodicSystemInventoryRn_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryRn = _CfprCallhomePeriodicSystemInventoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 3),
    _CfprCallhomePeriodicSystemInventoryRn_Type()
)
cfprCallhomePeriodicSystemInventoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryRn.setStatus("current")
_CfprCallhomePeriodicSystemInventoryAdminState_Type = CfprCallhomeAdminState
_CfprCallhomePeriodicSystemInventoryAdminState_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryAdminState = _CfprCallhomePeriodicSystemInventoryAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 4),
    _CfprCallhomePeriodicSystemInventoryAdminState_Type()
)
cfprCallhomePeriodicSystemInventoryAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryAdminState.setStatus("current")
_CfprCallhomePeriodicSystemInventoryIntervalDays_Type = Gauge32
_CfprCallhomePeriodicSystemInventoryIntervalDays_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryIntervalDays = _CfprCallhomePeriodicSystemInventoryIntervalDays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 5),
    _CfprCallhomePeriodicSystemInventoryIntervalDays_Type()
)
cfprCallhomePeriodicSystemInventoryIntervalDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryIntervalDays.setStatus("current")
_CfprCallhomePeriodicSystemInventoryLastDeadline_Type = DateAndTime
_CfprCallhomePeriodicSystemInventoryLastDeadline_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryLastDeadline = _CfprCallhomePeriodicSystemInventoryLastDeadline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 6),
    _CfprCallhomePeriodicSystemInventoryLastDeadline_Type()
)
cfprCallhomePeriodicSystemInventoryLastDeadline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryLastDeadline.setStatus("current")
_CfprCallhomePeriodicSystemInventoryMaximumRetryCount_Type = Gauge32
_CfprCallhomePeriodicSystemInventoryMaximumRetryCount_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryMaximumRetryCount = _CfprCallhomePeriodicSystemInventoryMaximumRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 7),
    _CfprCallhomePeriodicSystemInventoryMaximumRetryCount_Type()
)
cfprCallhomePeriodicSystemInventoryMaximumRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryMaximumRetryCount.setStatus("current")
_CfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Type = Gauge32
_CfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds = _CfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 8),
    _CfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Type()
)
cfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds.setStatus("current")
_CfprCallhomePeriodicSystemInventoryNextDeadline_Type = DateAndTime
_CfprCallhomePeriodicSystemInventoryNextDeadline_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryNextDeadline = _CfprCallhomePeriodicSystemInventoryNextDeadline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 9),
    _CfprCallhomePeriodicSystemInventoryNextDeadline_Type()
)
cfprCallhomePeriodicSystemInventoryNextDeadline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryNextDeadline.setStatus("current")
_CfprCallhomePeriodicSystemInventoryPollIntervalSeconds_Type = Gauge32
_CfprCallhomePeriodicSystemInventoryPollIntervalSeconds_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryPollIntervalSeconds = _CfprCallhomePeriodicSystemInventoryPollIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 10),
    _CfprCallhomePeriodicSystemInventoryPollIntervalSeconds_Type()
)
cfprCallhomePeriodicSystemInventoryPollIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryPollIntervalSeconds.setStatus("current")
_CfprCallhomePeriodicSystemInventoryRetryCount_Type = Gauge32
_CfprCallhomePeriodicSystemInventoryRetryCount_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryRetryCount = _CfprCallhomePeriodicSystemInventoryRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 11),
    _CfprCallhomePeriodicSystemInventoryRetryCount_Type()
)
cfprCallhomePeriodicSystemInventoryRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryRetryCount.setStatus("current")
_CfprCallhomePeriodicSystemInventoryRetryDelayMinutes_Type = Gauge32
_CfprCallhomePeriodicSystemInventoryRetryDelayMinutes_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryRetryDelayMinutes = _CfprCallhomePeriodicSystemInventoryRetryDelayMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 12),
    _CfprCallhomePeriodicSystemInventoryRetryDelayMinutes_Type()
)
cfprCallhomePeriodicSystemInventoryRetryDelayMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryRetryDelayMinutes.setStatus("current")
_CfprCallhomePeriodicSystemInventorySendNow_Type = TruthValue
_CfprCallhomePeriodicSystemInventorySendNow_Object = MibTableColumn
cfprCallhomePeriodicSystemInventorySendNow = _CfprCallhomePeriodicSystemInventorySendNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 13),
    _CfprCallhomePeriodicSystemInventorySendNow_Type()
)
cfprCallhomePeriodicSystemInventorySendNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventorySendNow.setStatus("current")
_CfprCallhomePeriodicSystemInventoryTimeOfDayHour_Type = Gauge32
_CfprCallhomePeriodicSystemInventoryTimeOfDayHour_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryTimeOfDayHour = _CfprCallhomePeriodicSystemInventoryTimeOfDayHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 14),
    _CfprCallhomePeriodicSystemInventoryTimeOfDayHour_Type()
)
cfprCallhomePeriodicSystemInventoryTimeOfDayHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryTimeOfDayHour.setStatus("current")
_CfprCallhomePeriodicSystemInventoryTimeOfDayMinute_Type = Gauge32
_CfprCallhomePeriodicSystemInventoryTimeOfDayMinute_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryTimeOfDayMinute = _CfprCallhomePeriodicSystemInventoryTimeOfDayMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 15),
    _CfprCallhomePeriodicSystemInventoryTimeOfDayMinute_Type()
)
cfprCallhomePeriodicSystemInventoryTimeOfDayMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryTimeOfDayMinute.setStatus("current")
_CfprCallhomePeriodicSystemInventoryTimeOfLastAttempt_Type = DateAndTime
_CfprCallhomePeriodicSystemInventoryTimeOfLastAttempt_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryTimeOfLastAttempt = _CfprCallhomePeriodicSystemInventoryTimeOfLastAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 16),
    _CfprCallhomePeriodicSystemInventoryTimeOfLastAttempt_Type()
)
cfprCallhomePeriodicSystemInventoryTimeOfLastAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryTimeOfLastAttempt.setStatus("current")
_CfprCallhomePeriodicSystemInventoryTimeOfLastSuccess_Type = DateAndTime
_CfprCallhomePeriodicSystemInventoryTimeOfLastSuccess_Object = MibTableColumn
cfprCallhomePeriodicSystemInventoryTimeOfLastSuccess = _CfprCallhomePeriodicSystemInventoryTimeOfLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 8, 1, 17),
    _CfprCallhomePeriodicSystemInventoryTimeOfLastSuccess_Type()
)
cfprCallhomePeriodicSystemInventoryTimeOfLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePeriodicSystemInventoryTimeOfLastSuccess.setStatus("current")
_CfprCallhomePolicyTable_Object = MibTable
cfprCallhomePolicyTable = _CfprCallhomePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9)
)
if mibBuilder.loadTexts:
    cfprCallhomePolicyTable.setStatus("current")
_CfprCallhomePolicyEntry_Object = MibTableRow
cfprCallhomePolicyEntry = _CfprCallhomePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9, 1)
)
cfprCallhomePolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomePolicyEntry.setStatus("current")
_CfprCallhomePolicyInstanceId_Type = CfprManagedObjectId
_CfprCallhomePolicyInstanceId_Object = MibTableColumn
cfprCallhomePolicyInstanceId = _CfprCallhomePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9, 1, 1),
    _CfprCallhomePolicyInstanceId_Type()
)
cfprCallhomePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomePolicyInstanceId.setStatus("current")
_CfprCallhomePolicyDn_Type = CfprManagedObjectDn
_CfprCallhomePolicyDn_Object = MibTableColumn
cfprCallhomePolicyDn = _CfprCallhomePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9, 1, 2),
    _CfprCallhomePolicyDn_Type()
)
cfprCallhomePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePolicyDn.setStatus("current")
_CfprCallhomePolicyRn_Type = SnmpAdminString
_CfprCallhomePolicyRn_Object = MibTableColumn
cfprCallhomePolicyRn = _CfprCallhomePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9, 1, 3),
    _CfprCallhomePolicyRn_Type()
)
cfprCallhomePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePolicyRn.setStatus("current")
_CfprCallhomePolicyAdminState_Type = CfprCallhomePolicyAdminState
_CfprCallhomePolicyAdminState_Object = MibTableColumn
cfprCallhomePolicyAdminState = _CfprCallhomePolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9, 1, 4),
    _CfprCallhomePolicyAdminState_Type()
)
cfprCallhomePolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePolicyAdminState.setStatus("current")
_CfprCallhomePolicyCause_Type = CfprConditionCallHomeCause
_CfprCallhomePolicyCause_Object = MibTableColumn
cfprCallhomePolicyCause = _CfprCallhomePolicyCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9, 1, 5),
    _CfprCallhomePolicyCause_Type()
)
cfprCallhomePolicyCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePolicyCause.setStatus("current")
_CfprCallhomePolicyDescr_Type = SnmpAdminString
_CfprCallhomePolicyDescr_Object = MibTableColumn
cfprCallhomePolicyDescr = _CfprCallhomePolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9, 1, 6),
    _CfprCallhomePolicyDescr_Type()
)
cfprCallhomePolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePolicyDescr.setStatus("current")
_CfprCallhomePolicyName_Type = SnmpAdminString
_CfprCallhomePolicyName_Object = MibTableColumn
cfprCallhomePolicyName = _CfprCallhomePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 9, 1, 7),
    _CfprCallhomePolicyName_Type()
)
cfprCallhomePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomePolicyName.setStatus("current")
_CfprCallhomeProfileTable_Object = MibTable
cfprCallhomeProfileTable = _CfprCallhomeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10)
)
if mibBuilder.loadTexts:
    cfprCallhomeProfileTable.setStatus("current")
_CfprCallhomeProfileEntry_Object = MibTableRow
cfprCallhomeProfileEntry = _CfprCallhomeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1)
)
cfprCallhomeProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeProfileEntry.setStatus("current")
_CfprCallhomeProfileInstanceId_Type = CfprManagedObjectId
_CfprCallhomeProfileInstanceId_Object = MibTableColumn
cfprCallhomeProfileInstanceId = _CfprCallhomeProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 1),
    _CfprCallhomeProfileInstanceId_Type()
)
cfprCallhomeProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeProfileInstanceId.setStatus("current")
_CfprCallhomeProfileDn_Type = CfprManagedObjectDn
_CfprCallhomeProfileDn_Object = MibTableColumn
cfprCallhomeProfileDn = _CfprCallhomeProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 2),
    _CfprCallhomeProfileDn_Type()
)
cfprCallhomeProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileDn.setStatus("current")
_CfprCallhomeProfileRn_Type = SnmpAdminString
_CfprCallhomeProfileRn_Object = MibTableColumn
cfprCallhomeProfileRn = _CfprCallhomeProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 3),
    _CfprCallhomeProfileRn_Type()
)
cfprCallhomeProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileRn.setStatus("current")
_CfprCallhomeProfileAlertGroups_Type = CfprCallhomeAlertGroups
_CfprCallhomeProfileAlertGroups_Object = MibTableColumn
cfprCallhomeProfileAlertGroups = _CfprCallhomeProfileAlertGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 4),
    _CfprCallhomeProfileAlertGroups_Type()
)
cfprCallhomeProfileAlertGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileAlertGroups.setStatus("current")
_CfprCallhomeProfileDescr_Type = SnmpAdminString
_CfprCallhomeProfileDescr_Object = MibTableColumn
cfprCallhomeProfileDescr = _CfprCallhomeProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 5),
    _CfprCallhomeProfileDescr_Type()
)
cfprCallhomeProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileDescr.setStatus("current")
_CfprCallhomeProfileFormat_Type = CfprCallhomeFormat
_CfprCallhomeProfileFormat_Object = MibTableColumn
cfprCallhomeProfileFormat = _CfprCallhomeProfileFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 6),
    _CfprCallhomeProfileFormat_Type()
)
cfprCallhomeProfileFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileFormat.setStatus("current")
_CfprCallhomeProfileLevel_Type = CfprCallhomeLevel
_CfprCallhomeProfileLevel_Object = MibTableColumn
cfprCallhomeProfileLevel = _CfprCallhomeProfileLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 7),
    _CfprCallhomeProfileLevel_Type()
)
cfprCallhomeProfileLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileLevel.setStatus("current")
_CfprCallhomeProfileMaxSize_Type = Gauge32
_CfprCallhomeProfileMaxSize_Object = MibTableColumn
cfprCallhomeProfileMaxSize = _CfprCallhomeProfileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 8),
    _CfprCallhomeProfileMaxSize_Type()
)
cfprCallhomeProfileMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileMaxSize.setStatus("current")
_CfprCallhomeProfileName_Type = SnmpAdminString
_CfprCallhomeProfileName_Object = MibTableColumn
cfprCallhomeProfileName = _CfprCallhomeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 9),
    _CfprCallhomeProfileName_Type()
)
cfprCallhomeProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileName.setStatus("current")
_CfprCallhomeProfileReporting_Type = CfprCallhomeReportingType
_CfprCallhomeProfileReporting_Object = MibTableColumn
cfprCallhomeProfileReporting = _CfprCallhomeProfileReporting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 10, 1, 10),
    _CfprCallhomeProfileReporting_Type()
)
cfprCallhomeProfileReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeProfileReporting.setStatus("current")
_CfprCallhomeSmtpTable_Object = MibTable
cfprCallhomeSmtpTable = _CfprCallhomeSmtpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 11)
)
if mibBuilder.loadTexts:
    cfprCallhomeSmtpTable.setStatus("current")
_CfprCallhomeSmtpEntry_Object = MibTableRow
cfprCallhomeSmtpEntry = _CfprCallhomeSmtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 11, 1)
)
cfprCallhomeSmtpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeSmtpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeSmtpEntry.setStatus("current")
_CfprCallhomeSmtpInstanceId_Type = CfprManagedObjectId
_CfprCallhomeSmtpInstanceId_Object = MibTableColumn
cfprCallhomeSmtpInstanceId = _CfprCallhomeSmtpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 11, 1, 1),
    _CfprCallhomeSmtpInstanceId_Type()
)
cfprCallhomeSmtpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeSmtpInstanceId.setStatus("current")
_CfprCallhomeSmtpDn_Type = CfprManagedObjectDn
_CfprCallhomeSmtpDn_Object = MibTableColumn
cfprCallhomeSmtpDn = _CfprCallhomeSmtpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 11, 1, 2),
    _CfprCallhomeSmtpDn_Type()
)
cfprCallhomeSmtpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSmtpDn.setStatus("current")
_CfprCallhomeSmtpRn_Type = SnmpAdminString
_CfprCallhomeSmtpRn_Object = MibTableColumn
cfprCallhomeSmtpRn = _CfprCallhomeSmtpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 11, 1, 3),
    _CfprCallhomeSmtpRn_Type()
)
cfprCallhomeSmtpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSmtpRn.setStatus("current")
_CfprCallhomeSmtpHost_Type = SnmpAdminString
_CfprCallhomeSmtpHost_Object = MibTableColumn
cfprCallhomeSmtpHost = _CfprCallhomeSmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 11, 1, 4),
    _CfprCallhomeSmtpHost_Type()
)
cfprCallhomeSmtpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSmtpHost.setStatus("current")
_CfprCallhomeSmtpPort_Type = Gauge32
_CfprCallhomeSmtpPort_Object = MibTableColumn
cfprCallhomeSmtpPort = _CfprCallhomeSmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 11, 1, 5),
    _CfprCallhomeSmtpPort_Type()
)
cfprCallhomeSmtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSmtpPort.setStatus("current")
_CfprCallhomeSourceTable_Object = MibTable
cfprCallhomeSourceTable = _CfprCallhomeSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12)
)
if mibBuilder.loadTexts:
    cfprCallhomeSourceTable.setStatus("current")
_CfprCallhomeSourceEntry_Object = MibTableRow
cfprCallhomeSourceEntry = _CfprCallhomeSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1)
)
cfprCallhomeSourceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeSourceEntry.setStatus("current")
_CfprCallhomeSourceInstanceId_Type = CfprManagedObjectId
_CfprCallhomeSourceInstanceId_Object = MibTableColumn
cfprCallhomeSourceInstanceId = _CfprCallhomeSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 1),
    _CfprCallhomeSourceInstanceId_Type()
)
cfprCallhomeSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeSourceInstanceId.setStatus("current")
_CfprCallhomeSourceDn_Type = CfprManagedObjectDn
_CfprCallhomeSourceDn_Object = MibTableColumn
cfprCallhomeSourceDn = _CfprCallhomeSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 2),
    _CfprCallhomeSourceDn_Type()
)
cfprCallhomeSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceDn.setStatus("current")
_CfprCallhomeSourceRn_Type = SnmpAdminString
_CfprCallhomeSourceRn_Object = MibTableColumn
cfprCallhomeSourceRn = _CfprCallhomeSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 3),
    _CfprCallhomeSourceRn_Type()
)
cfprCallhomeSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceRn.setStatus("current")
_CfprCallhomeSourceAddr_Type = SnmpAdminString
_CfprCallhomeSourceAddr_Object = MibTableColumn
cfprCallhomeSourceAddr = _CfprCallhomeSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 4),
    _CfprCallhomeSourceAddr_Type()
)
cfprCallhomeSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceAddr.setStatus("current")
_CfprCallhomeSourceContact_Type = SnmpAdminString
_CfprCallhomeSourceContact_Object = MibTableColumn
cfprCallhomeSourceContact = _CfprCallhomeSourceContact_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 5),
    _CfprCallhomeSourceContact_Type()
)
cfprCallhomeSourceContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceContact.setStatus("current")
_CfprCallhomeSourceContract_Type = SnmpAdminString
_CfprCallhomeSourceContract_Object = MibTableColumn
cfprCallhomeSourceContract = _CfprCallhomeSourceContract_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 6),
    _CfprCallhomeSourceContract_Type()
)
cfprCallhomeSourceContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceContract.setStatus("current")
_CfprCallhomeSourceCustomer_Type = SnmpAdminString
_CfprCallhomeSourceCustomer_Object = MibTableColumn
cfprCallhomeSourceCustomer = _CfprCallhomeSourceCustomer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 7),
    _CfprCallhomeSourceCustomer_Type()
)
cfprCallhomeSourceCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceCustomer.setStatus("current")
_CfprCallhomeSourceEmail_Type = SnmpAdminString
_CfprCallhomeSourceEmail_Object = MibTableColumn
cfprCallhomeSourceEmail = _CfprCallhomeSourceEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 8),
    _CfprCallhomeSourceEmail_Type()
)
cfprCallhomeSourceEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceEmail.setStatus("current")
_CfprCallhomeSourceFrom_Type = SnmpAdminString
_CfprCallhomeSourceFrom_Object = MibTableColumn
cfprCallhomeSourceFrom = _CfprCallhomeSourceFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 9),
    _CfprCallhomeSourceFrom_Type()
)
cfprCallhomeSourceFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceFrom.setStatus("current")
_CfprCallhomeSourcePhone_Type = SnmpAdminString
_CfprCallhomeSourcePhone_Object = MibTableColumn
cfprCallhomeSourcePhone = _CfprCallhomeSourcePhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 10),
    _CfprCallhomeSourcePhone_Type()
)
cfprCallhomeSourcePhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourcePhone.setStatus("current")
_CfprCallhomeSourceReplyTo_Type = SnmpAdminString
_CfprCallhomeSourceReplyTo_Object = MibTableColumn
cfprCallhomeSourceReplyTo = _CfprCallhomeSourceReplyTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 11),
    _CfprCallhomeSourceReplyTo_Type()
)
cfprCallhomeSourceReplyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceReplyTo.setStatus("current")
_CfprCallhomeSourceSite_Type = SnmpAdminString
_CfprCallhomeSourceSite_Object = MibTableColumn
cfprCallhomeSourceSite = _CfprCallhomeSourceSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 12),
    _CfprCallhomeSourceSite_Type()
)
cfprCallhomeSourceSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceSite.setStatus("current")
_CfprCallhomeSourceUrgency_Type = CfprCallhomeUrgency
_CfprCallhomeSourceUrgency_Object = MibTableColumn
cfprCallhomeSourceUrgency = _CfprCallhomeSourceUrgency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 12, 1, 13),
    _CfprCallhomeSourceUrgency_Type()
)
cfprCallhomeSourceUrgency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeSourceUrgency.setStatus("current")
_CfprCallhomeTestAlertTable_Object = MibTable
cfprCallhomeTestAlertTable = _CfprCallhomeTestAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13)
)
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertTable.setStatus("current")
_CfprCallhomeTestAlertEntry_Object = MibTableRow
cfprCallhomeTestAlertEntry = _CfprCallhomeTestAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1)
)
cfprCallhomeTestAlertEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CALLHOME-MIB", "cfprCallhomeTestAlertInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertEntry.setStatus("current")
_CfprCallhomeTestAlertInstanceId_Type = CfprManagedObjectId
_CfprCallhomeTestAlertInstanceId_Object = MibTableColumn
cfprCallhomeTestAlertInstanceId = _CfprCallhomeTestAlertInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 1),
    _CfprCallhomeTestAlertInstanceId_Type()
)
cfprCallhomeTestAlertInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertInstanceId.setStatus("current")
_CfprCallhomeTestAlertDn_Type = CfprManagedObjectDn
_CfprCallhomeTestAlertDn_Object = MibTableColumn
cfprCallhomeTestAlertDn = _CfprCallhomeTestAlertDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 2),
    _CfprCallhomeTestAlertDn_Type()
)
cfprCallhomeTestAlertDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertDn.setStatus("current")
_CfprCallhomeTestAlertRn_Type = SnmpAdminString
_CfprCallhomeTestAlertRn_Object = MibTableColumn
cfprCallhomeTestAlertRn = _CfprCallhomeTestAlertRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 3),
    _CfprCallhomeTestAlertRn_Type()
)
cfprCallhomeTestAlertRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertRn.setStatus("current")
_CfprCallhomeTestAlertDescription_Type = SnmpAdminString
_CfprCallhomeTestAlertDescription_Object = MibTableColumn
cfprCallhomeTestAlertDescription = _CfprCallhomeTestAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 4),
    _CfprCallhomeTestAlertDescription_Type()
)
cfprCallhomeTestAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertDescription.setStatus("current")
_CfprCallhomeTestAlertGroup_Type = CfprCallhomeAlertGroup
_CfprCallhomeTestAlertGroup_Object = MibTableColumn
cfprCallhomeTestAlertGroup = _CfprCallhomeTestAlertGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 5),
    _CfprCallhomeTestAlertGroup_Type()
)
cfprCallhomeTestAlertGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertGroup.setStatus("current")
_CfprCallhomeTestAlertLevel_Type = CfprCallhomeAlertLevel
_CfprCallhomeTestAlertLevel_Object = MibTableColumn
cfprCallhomeTestAlertLevel = _CfprCallhomeTestAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 6),
    _CfprCallhomeTestAlertLevel_Type()
)
cfprCallhomeTestAlertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertLevel.setStatus("current")
_CfprCallhomeTestAlertMessageSubtype_Type = CfprCallhomeAlertMessageSubtype
_CfprCallhomeTestAlertMessageSubtype_Object = MibTableColumn
cfprCallhomeTestAlertMessageSubtype = _CfprCallhomeTestAlertMessageSubtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 7),
    _CfprCallhomeTestAlertMessageSubtype_Type()
)
cfprCallhomeTestAlertMessageSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertMessageSubtype.setStatus("current")
_CfprCallhomeTestAlertMessageType_Type = CfprCallhomeAlertMessageType
_CfprCallhomeTestAlertMessageType_Object = MibTableColumn
cfprCallhomeTestAlertMessageType = _CfprCallhomeTestAlertMessageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 8),
    _CfprCallhomeTestAlertMessageType_Type()
)
cfprCallhomeTestAlertMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertMessageType.setStatus("current")
_CfprCallhomeTestAlertSendNow_Type = TruthValue
_CfprCallhomeTestAlertSendNow_Object = MibTableColumn
cfprCallhomeTestAlertSendNow = _CfprCallhomeTestAlertSendNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 7, 13, 1, 9),
    _CfprCallhomeTestAlertSendNow_Type()
)
cfprCallhomeTestAlertSendNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCallhomeTestAlertSendNow.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-CALLHOME-MIB",
    **{"cfprCallhomeObjects": cfprCallhomeObjects,
       "cfprCallhomeAnonymousReportingTable": cfprCallhomeAnonymousReportingTable,
       "cfprCallhomeAnonymousReportingEntry": cfprCallhomeAnonymousReportingEntry,
       "cfprCallhomeAnonymousReportingInstanceId": cfprCallhomeAnonymousReportingInstanceId,
       "cfprCallhomeAnonymousReportingDn": cfprCallhomeAnonymousReportingDn,
       "cfprCallhomeAnonymousReportingRn": cfprCallhomeAnonymousReportingRn,
       "cfprCallhomeAnonymousReportingAdminState": cfprCallhomeAnonymousReportingAdminState,
       "cfprCallhomeAnonymousReportingCount": cfprCallhomeAnonymousReportingCount,
       "cfprCallhomeAnonymousReportingSleepInterval": cfprCallhomeAnonymousReportingSleepInterval,
       "cfprCallhomeAnonymousReportingUserAcknowledged": cfprCallhomeAnonymousReportingUserAcknowledged,
       "cfprCallhomeDestTable": cfprCallhomeDestTable,
       "cfprCallhomeDestEntry": cfprCallhomeDestEntry,
       "cfprCallhomeDestInstanceId": cfprCallhomeDestInstanceId,
       "cfprCallhomeDestDn": cfprCallhomeDestDn,
       "cfprCallhomeDestRn": cfprCallhomeDestRn,
       "cfprCallhomeDestAddress": cfprCallhomeDestAddress,
       "cfprCallhomeDestName": cfprCallhomeDestName,
       "cfprCallhomeDestProtocol": cfprCallhomeDestProtocol,
       "cfprCallhomeEpTable": cfprCallhomeEpTable,
       "cfprCallhomeEpEntry": cfprCallhomeEpEntry,
       "cfprCallhomeEpInstanceId": cfprCallhomeEpInstanceId,
       "cfprCallhomeEpDn": cfprCallhomeEpDn,
       "cfprCallhomeEpRn": cfprCallhomeEpRn,
       "cfprCallhomeEpAdminState": cfprCallhomeEpAdminState,
       "cfprCallhomeEpAlertThrottlingAdminState": cfprCallhomeEpAlertThrottlingAdminState,
       "cfprCallhomeEpConfigState": cfprCallhomeEpConfigState,
       "cfprCallhomeEpDescr": cfprCallhomeEpDescr,
       "cfprCallhomeEpFsmDescr": cfprCallhomeEpFsmDescr,
       "cfprCallhomeEpFsmPrev": cfprCallhomeEpFsmPrev,
       "cfprCallhomeEpFsmProgr": cfprCallhomeEpFsmProgr,
       "cfprCallhomeEpFsmRmtInvErrCode": cfprCallhomeEpFsmRmtInvErrCode,
       "cfprCallhomeEpFsmRmtInvErrDescr": cfprCallhomeEpFsmRmtInvErrDescr,
       "cfprCallhomeEpFsmRmtInvRslt": cfprCallhomeEpFsmRmtInvRslt,
       "cfprCallhomeEpFsmStageDescr": cfprCallhomeEpFsmStageDescr,
       "cfprCallhomeEpFsmStamp": cfprCallhomeEpFsmStamp,
       "cfprCallhomeEpFsmStatus": cfprCallhomeEpFsmStatus,
       "cfprCallhomeEpFsmTry": cfprCallhomeEpFsmTry,
       "cfprCallhomeEpIntId": cfprCallhomeEpIntId,
       "cfprCallhomeEpName": cfprCallhomeEpName,
       "cfprCallhomeEpPolicyLevel": cfprCallhomeEpPolicyLevel,
       "cfprCallhomeEpPolicyOwner": cfprCallhomeEpPolicyOwner,
       "cfprCallhomeEpFsmTable": cfprCallhomeEpFsmTable,
       "cfprCallhomeEpFsmEntry": cfprCallhomeEpFsmEntry,
       "cfprCallhomeEpFsmInstanceId": cfprCallhomeEpFsmInstanceId,
       "cfprCallhomeEpFsmDn": cfprCallhomeEpFsmDn,
       "cfprCallhomeEpFsmRn": cfprCallhomeEpFsmRn,
       "cfprCallhomeEpFsmCompletionTime": cfprCallhomeEpFsmCompletionTime,
       "cfprCallhomeEpFsmCurrentFsm": cfprCallhomeEpFsmCurrentFsm,
       "cfprCallhomeEpFsmDescrData": cfprCallhomeEpFsmDescrData,
       "cfprCallhomeEpFsmFsmStatus": cfprCallhomeEpFsmFsmStatus,
       "cfprCallhomeEpFsmProgress": cfprCallhomeEpFsmProgress,
       "cfprCallhomeEpFsmRmtErrCode": cfprCallhomeEpFsmRmtErrCode,
       "cfprCallhomeEpFsmRmtErrDescr": cfprCallhomeEpFsmRmtErrDescr,
       "cfprCallhomeEpFsmRmtRslt": cfprCallhomeEpFsmRmtRslt,
       "cfprCallhomeEpFsmStageTable": cfprCallhomeEpFsmStageTable,
       "cfprCallhomeEpFsmStageEntry": cfprCallhomeEpFsmStageEntry,
       "cfprCallhomeEpFsmStageInstanceId": cfprCallhomeEpFsmStageInstanceId,
       "cfprCallhomeEpFsmStageDn": cfprCallhomeEpFsmStageDn,
       "cfprCallhomeEpFsmStageRn": cfprCallhomeEpFsmStageRn,
       "cfprCallhomeEpFsmStageDescrData": cfprCallhomeEpFsmStageDescrData,
       "cfprCallhomeEpFsmStageLastUpdateTime": cfprCallhomeEpFsmStageLastUpdateTime,
       "cfprCallhomeEpFsmStageName": cfprCallhomeEpFsmStageName,
       "cfprCallhomeEpFsmStageOrder": cfprCallhomeEpFsmStageOrder,
       "cfprCallhomeEpFsmStageRetry": cfprCallhomeEpFsmStageRetry,
       "cfprCallhomeEpFsmStageStageStatus": cfprCallhomeEpFsmStageStageStatus,
       "cfprCallhomeEpFsmTaskTable": cfprCallhomeEpFsmTaskTable,
       "cfprCallhomeEpFsmTaskEntry": cfprCallhomeEpFsmTaskEntry,
       "cfprCallhomeEpFsmTaskInstanceId": cfprCallhomeEpFsmTaskInstanceId,
       "cfprCallhomeEpFsmTaskDn": cfprCallhomeEpFsmTaskDn,
       "cfprCallhomeEpFsmTaskRn": cfprCallhomeEpFsmTaskRn,
       "cfprCallhomeEpFsmTaskCompletion": cfprCallhomeEpFsmTaskCompletion,
       "cfprCallhomeEpFsmTaskFlags": cfprCallhomeEpFsmTaskFlags,
       "cfprCallhomeEpFsmTaskItem": cfprCallhomeEpFsmTaskItem,
       "cfprCallhomeEpFsmTaskSeqId": cfprCallhomeEpFsmTaskSeqId,
       "cfprCallhomeHttpProxyTable": cfprCallhomeHttpProxyTable,
       "cfprCallhomeHttpProxyEntry": cfprCallhomeHttpProxyEntry,
       "cfprCallhomeHttpProxyInstanceId": cfprCallhomeHttpProxyInstanceId,
       "cfprCallhomeHttpProxyDn": cfprCallhomeHttpProxyDn,
       "cfprCallhomeHttpProxyRn": cfprCallhomeHttpProxyRn,
       "cfprCallhomeHttpProxyProxyServerEnable": cfprCallhomeHttpProxyProxyServerEnable,
       "cfprCallhomeHttpProxyProxyServerPort": cfprCallhomeHttpProxyProxyServerPort,
       "cfprCallhomeHttpProxyProxyServerUrl": cfprCallhomeHttpProxyProxyServerUrl,
       "cfprCallhomePeriodicSystemInventoryTable": cfprCallhomePeriodicSystemInventoryTable,
       "cfprCallhomePeriodicSystemInventoryEntry": cfprCallhomePeriodicSystemInventoryEntry,
       "cfprCallhomePeriodicSystemInventoryInstanceId": cfprCallhomePeriodicSystemInventoryInstanceId,
       "cfprCallhomePeriodicSystemInventoryDn": cfprCallhomePeriodicSystemInventoryDn,
       "cfprCallhomePeriodicSystemInventoryRn": cfprCallhomePeriodicSystemInventoryRn,
       "cfprCallhomePeriodicSystemInventoryAdminState": cfprCallhomePeriodicSystemInventoryAdminState,
       "cfprCallhomePeriodicSystemInventoryIntervalDays": cfprCallhomePeriodicSystemInventoryIntervalDays,
       "cfprCallhomePeriodicSystemInventoryLastDeadline": cfprCallhomePeriodicSystemInventoryLastDeadline,
       "cfprCallhomePeriodicSystemInventoryMaximumRetryCount": cfprCallhomePeriodicSystemInventoryMaximumRetryCount,
       "cfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds": cfprCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds,
       "cfprCallhomePeriodicSystemInventoryNextDeadline": cfprCallhomePeriodicSystemInventoryNextDeadline,
       "cfprCallhomePeriodicSystemInventoryPollIntervalSeconds": cfprCallhomePeriodicSystemInventoryPollIntervalSeconds,
       "cfprCallhomePeriodicSystemInventoryRetryCount": cfprCallhomePeriodicSystemInventoryRetryCount,
       "cfprCallhomePeriodicSystemInventoryRetryDelayMinutes": cfprCallhomePeriodicSystemInventoryRetryDelayMinutes,
       "cfprCallhomePeriodicSystemInventorySendNow": cfprCallhomePeriodicSystemInventorySendNow,
       "cfprCallhomePeriodicSystemInventoryTimeOfDayHour": cfprCallhomePeriodicSystemInventoryTimeOfDayHour,
       "cfprCallhomePeriodicSystemInventoryTimeOfDayMinute": cfprCallhomePeriodicSystemInventoryTimeOfDayMinute,
       "cfprCallhomePeriodicSystemInventoryTimeOfLastAttempt": cfprCallhomePeriodicSystemInventoryTimeOfLastAttempt,
       "cfprCallhomePeriodicSystemInventoryTimeOfLastSuccess": cfprCallhomePeriodicSystemInventoryTimeOfLastSuccess,
       "cfprCallhomePolicyTable": cfprCallhomePolicyTable,
       "cfprCallhomePolicyEntry": cfprCallhomePolicyEntry,
       "cfprCallhomePolicyInstanceId": cfprCallhomePolicyInstanceId,
       "cfprCallhomePolicyDn": cfprCallhomePolicyDn,
       "cfprCallhomePolicyRn": cfprCallhomePolicyRn,
       "cfprCallhomePolicyAdminState": cfprCallhomePolicyAdminState,
       "cfprCallhomePolicyCause": cfprCallhomePolicyCause,
       "cfprCallhomePolicyDescr": cfprCallhomePolicyDescr,
       "cfprCallhomePolicyName": cfprCallhomePolicyName,
       "cfprCallhomeProfileTable": cfprCallhomeProfileTable,
       "cfprCallhomeProfileEntry": cfprCallhomeProfileEntry,
       "cfprCallhomeProfileInstanceId": cfprCallhomeProfileInstanceId,
       "cfprCallhomeProfileDn": cfprCallhomeProfileDn,
       "cfprCallhomeProfileRn": cfprCallhomeProfileRn,
       "cfprCallhomeProfileAlertGroups": cfprCallhomeProfileAlertGroups,
       "cfprCallhomeProfileDescr": cfprCallhomeProfileDescr,
       "cfprCallhomeProfileFormat": cfprCallhomeProfileFormat,
       "cfprCallhomeProfileLevel": cfprCallhomeProfileLevel,
       "cfprCallhomeProfileMaxSize": cfprCallhomeProfileMaxSize,
       "cfprCallhomeProfileName": cfprCallhomeProfileName,
       "cfprCallhomeProfileReporting": cfprCallhomeProfileReporting,
       "cfprCallhomeSmtpTable": cfprCallhomeSmtpTable,
       "cfprCallhomeSmtpEntry": cfprCallhomeSmtpEntry,
       "cfprCallhomeSmtpInstanceId": cfprCallhomeSmtpInstanceId,
       "cfprCallhomeSmtpDn": cfprCallhomeSmtpDn,
       "cfprCallhomeSmtpRn": cfprCallhomeSmtpRn,
       "cfprCallhomeSmtpHost": cfprCallhomeSmtpHost,
       "cfprCallhomeSmtpPort": cfprCallhomeSmtpPort,
       "cfprCallhomeSourceTable": cfprCallhomeSourceTable,
       "cfprCallhomeSourceEntry": cfprCallhomeSourceEntry,
       "cfprCallhomeSourceInstanceId": cfprCallhomeSourceInstanceId,
       "cfprCallhomeSourceDn": cfprCallhomeSourceDn,
       "cfprCallhomeSourceRn": cfprCallhomeSourceRn,
       "cfprCallhomeSourceAddr": cfprCallhomeSourceAddr,
       "cfprCallhomeSourceContact": cfprCallhomeSourceContact,
       "cfprCallhomeSourceContract": cfprCallhomeSourceContract,
       "cfprCallhomeSourceCustomer": cfprCallhomeSourceCustomer,
       "cfprCallhomeSourceEmail": cfprCallhomeSourceEmail,
       "cfprCallhomeSourceFrom": cfprCallhomeSourceFrom,
       "cfprCallhomeSourcePhone": cfprCallhomeSourcePhone,
       "cfprCallhomeSourceReplyTo": cfprCallhomeSourceReplyTo,
       "cfprCallhomeSourceSite": cfprCallhomeSourceSite,
       "cfprCallhomeSourceUrgency": cfprCallhomeSourceUrgency,
       "cfprCallhomeTestAlertTable": cfprCallhomeTestAlertTable,
       "cfprCallhomeTestAlertEntry": cfprCallhomeTestAlertEntry,
       "cfprCallhomeTestAlertInstanceId": cfprCallhomeTestAlertInstanceId,
       "cfprCallhomeTestAlertDn": cfprCallhomeTestAlertDn,
       "cfprCallhomeTestAlertRn": cfprCallhomeTestAlertRn,
       "cfprCallhomeTestAlertDescription": cfprCallhomeTestAlertDescription,
       "cfprCallhomeTestAlertGroup": cfprCallhomeTestAlertGroup,
       "cfprCallhomeTestAlertLevel": cfprCallhomeTestAlertLevel,
       "cfprCallhomeTestAlertMessageSubtype": cfprCallhomeTestAlertMessageSubtype,
       "cfprCallhomeTestAlertMessageType": cfprCallhomeTestAlertMessageType,
       "cfprCallhomeTestAlertSendNow": cfprCallhomeTestAlertSendNow}
)
