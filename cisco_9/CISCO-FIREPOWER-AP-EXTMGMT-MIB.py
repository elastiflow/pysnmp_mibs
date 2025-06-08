# SNMP MIB module (CISCO-FIREPOWER-AP-EXTMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-EXTMGMT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:52 2025
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

(CfprApAaaConfigState,
 CfprApExtmgmtArpTargetsMaxDeadlineTimeout,
 CfprApExtmgmtArpTargetsNumberOfArpRequests,
 CfprApExtmgmtGatewayPingMaxDeadlineTimeout,
 CfprApExtmgmtGatewayPingNumberOfPingRequests,
 CfprApExtmgmtIfMonPolicyAdminState,
 CfprApExtmgmtIfMonPolicyMonitorMechanism,
 CfprApExtmgmtIfType,
 CfprApExtmgmtMiiStatusMaxRetryCount,
 CfprApExtmgmtMiiStatusRetryInterval,
 CfprApExtmgmtNdiscTargetsMaxDeadlineTimeout,
 CfprApExtmgmtNdiscTargetsNumberOfNdiscRequests,
 CfprApNetworkIfStatus,
 CfprApNetworkLocale,
 CfprApNetworkPortRole,
 CfprApNetworkPortType,
 CfprApNetworkSwitchId,
 CfprApNetworkTransport,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAaaConfigState",
    "CfprApExtmgmtArpTargetsMaxDeadlineTimeout",
    "CfprApExtmgmtArpTargetsNumberOfArpRequests",
    "CfprApExtmgmtGatewayPingMaxDeadlineTimeout",
    "CfprApExtmgmtGatewayPingNumberOfPingRequests",
    "CfprApExtmgmtIfMonPolicyAdminState",
    "CfprApExtmgmtIfMonPolicyMonitorMechanism",
    "CfprApExtmgmtIfType",
    "CfprApExtmgmtMiiStatusMaxRetryCount",
    "CfprApExtmgmtMiiStatusRetryInterval",
    "CfprApExtmgmtNdiscTargetsMaxDeadlineTimeout",
    "CfprApExtmgmtNdiscTargetsNumberOfNdiscRequests",
    "CfprApNetworkIfStatus",
    "CfprApNetworkLocale",
    "CfprApNetworkPortRole",
    "CfprApNetworkPortType",
    "CfprApNetworkSwitchId",
    "CfprApNetworkTransport",
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

cfprApExtmgmtObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApExtmgmtArpTargetsTable_Object = MibTable
cfprApExtmgmtArpTargetsTable = _CfprApExtmgmtArpTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1)
)
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsTable.setStatus("current")
_CfprApExtmgmtArpTargetsEntry_Object = MibTableRow
cfprApExtmgmtArpTargetsEntry = _CfprApExtmgmtArpTargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1)
)
cfprApExtmgmtArpTargetsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTMGMT-MIB", "cfprApExtmgmtArpTargetsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsEntry.setStatus("current")
_CfprApExtmgmtArpTargetsInstanceId_Type = CfprApManagedObjectId
_CfprApExtmgmtArpTargetsInstanceId_Object = MibTableColumn
cfprApExtmgmtArpTargetsInstanceId = _CfprApExtmgmtArpTargetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 1),
    _CfprApExtmgmtArpTargetsInstanceId_Type()
)
cfprApExtmgmtArpTargetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsInstanceId.setStatus("current")
_CfprApExtmgmtArpTargetsDn_Type = CfprApManagedObjectDn
_CfprApExtmgmtArpTargetsDn_Object = MibTableColumn
cfprApExtmgmtArpTargetsDn = _CfprApExtmgmtArpTargetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 2),
    _CfprApExtmgmtArpTargetsDn_Type()
)
cfprApExtmgmtArpTargetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsDn.setStatus("current")
_CfprApExtmgmtArpTargetsRn_Type = SnmpAdminString
_CfprApExtmgmtArpTargetsRn_Object = MibTableColumn
cfprApExtmgmtArpTargetsRn = _CfprApExtmgmtArpTargetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 3),
    _CfprApExtmgmtArpTargetsRn_Type()
)
cfprApExtmgmtArpTargetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsRn.setStatus("current")
_CfprApExtmgmtArpTargetsConfigState_Type = CfprApAaaConfigState
_CfprApExtmgmtArpTargetsConfigState_Object = MibTableColumn
cfprApExtmgmtArpTargetsConfigState = _CfprApExtmgmtArpTargetsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 4),
    _CfprApExtmgmtArpTargetsConfigState_Type()
)
cfprApExtmgmtArpTargetsConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsConfigState.setStatus("current")
_CfprApExtmgmtArpTargetsConfigStatusMessage_Type = SnmpAdminString
_CfprApExtmgmtArpTargetsConfigStatusMessage_Object = MibTableColumn
cfprApExtmgmtArpTargetsConfigStatusMessage = _CfprApExtmgmtArpTargetsConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 5),
    _CfprApExtmgmtArpTargetsConfigStatusMessage_Type()
)
cfprApExtmgmtArpTargetsConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsConfigStatusMessage.setStatus("current")
_CfprApExtmgmtArpTargetsMaxDeadlineTimeout_Type = CfprApExtmgmtArpTargetsMaxDeadlineTimeout
_CfprApExtmgmtArpTargetsMaxDeadlineTimeout_Object = MibTableColumn
cfprApExtmgmtArpTargetsMaxDeadlineTimeout = _CfprApExtmgmtArpTargetsMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 6),
    _CfprApExtmgmtArpTargetsMaxDeadlineTimeout_Type()
)
cfprApExtmgmtArpTargetsMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsMaxDeadlineTimeout.setStatus("current")
_CfprApExtmgmtArpTargetsNumberOfArpRequests_Type = CfprApExtmgmtArpTargetsNumberOfArpRequests
_CfprApExtmgmtArpTargetsNumberOfArpRequests_Object = MibTableColumn
cfprApExtmgmtArpTargetsNumberOfArpRequests = _CfprApExtmgmtArpTargetsNumberOfArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 7),
    _CfprApExtmgmtArpTargetsNumberOfArpRequests_Type()
)
cfprApExtmgmtArpTargetsNumberOfArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsNumberOfArpRequests.setStatus("current")
_CfprApExtmgmtArpTargetsTargetIp1_Type = InetAddressIPv4
_CfprApExtmgmtArpTargetsTargetIp1_Object = MibTableColumn
cfprApExtmgmtArpTargetsTargetIp1 = _CfprApExtmgmtArpTargetsTargetIp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 8),
    _CfprApExtmgmtArpTargetsTargetIp1_Type()
)
cfprApExtmgmtArpTargetsTargetIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsTargetIp1.setStatus("current")
_CfprApExtmgmtArpTargetsTargetIp2_Type = InetAddressIPv4
_CfprApExtmgmtArpTargetsTargetIp2_Object = MibTableColumn
cfprApExtmgmtArpTargetsTargetIp2 = _CfprApExtmgmtArpTargetsTargetIp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 9),
    _CfprApExtmgmtArpTargetsTargetIp2_Type()
)
cfprApExtmgmtArpTargetsTargetIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsTargetIp2.setStatus("current")
_CfprApExtmgmtArpTargetsTargetIp3_Type = InetAddressIPv4
_CfprApExtmgmtArpTargetsTargetIp3_Object = MibTableColumn
cfprApExtmgmtArpTargetsTargetIp3 = _CfprApExtmgmtArpTargetsTargetIp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 1, 1, 10),
    _CfprApExtmgmtArpTargetsTargetIp3_Type()
)
cfprApExtmgmtArpTargetsTargetIp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtArpTargetsTargetIp3.setStatus("current")
_CfprApExtmgmtGatewayPingTable_Object = MibTable
cfprApExtmgmtGatewayPingTable = _CfprApExtmgmtGatewayPingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 2)
)
if mibBuilder.loadTexts:
    cfprApExtmgmtGatewayPingTable.setStatus("current")
_CfprApExtmgmtGatewayPingEntry_Object = MibTableRow
cfprApExtmgmtGatewayPingEntry = _CfprApExtmgmtGatewayPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 2, 1)
)
cfprApExtmgmtGatewayPingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTMGMT-MIB", "cfprApExtmgmtGatewayPingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtmgmtGatewayPingEntry.setStatus("current")
_CfprApExtmgmtGatewayPingInstanceId_Type = CfprApManagedObjectId
_CfprApExtmgmtGatewayPingInstanceId_Object = MibTableColumn
cfprApExtmgmtGatewayPingInstanceId = _CfprApExtmgmtGatewayPingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 2, 1, 1),
    _CfprApExtmgmtGatewayPingInstanceId_Type()
)
cfprApExtmgmtGatewayPingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtmgmtGatewayPingInstanceId.setStatus("current")
_CfprApExtmgmtGatewayPingDn_Type = CfprApManagedObjectDn
_CfprApExtmgmtGatewayPingDn_Object = MibTableColumn
cfprApExtmgmtGatewayPingDn = _CfprApExtmgmtGatewayPingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 2, 1, 2),
    _CfprApExtmgmtGatewayPingDn_Type()
)
cfprApExtmgmtGatewayPingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtGatewayPingDn.setStatus("current")
_CfprApExtmgmtGatewayPingRn_Type = SnmpAdminString
_CfprApExtmgmtGatewayPingRn_Object = MibTableColumn
cfprApExtmgmtGatewayPingRn = _CfprApExtmgmtGatewayPingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 2, 1, 3),
    _CfprApExtmgmtGatewayPingRn_Type()
)
cfprApExtmgmtGatewayPingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtGatewayPingRn.setStatus("current")
_CfprApExtmgmtGatewayPingMaxDeadlineTimeout_Type = CfprApExtmgmtGatewayPingMaxDeadlineTimeout
_CfprApExtmgmtGatewayPingMaxDeadlineTimeout_Object = MibTableColumn
cfprApExtmgmtGatewayPingMaxDeadlineTimeout = _CfprApExtmgmtGatewayPingMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 2, 1, 4),
    _CfprApExtmgmtGatewayPingMaxDeadlineTimeout_Type()
)
cfprApExtmgmtGatewayPingMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtGatewayPingMaxDeadlineTimeout.setStatus("current")
_CfprApExtmgmtGatewayPingNumberOfPingRequests_Type = CfprApExtmgmtGatewayPingNumberOfPingRequests
_CfprApExtmgmtGatewayPingNumberOfPingRequests_Object = MibTableColumn
cfprApExtmgmtGatewayPingNumberOfPingRequests = _CfprApExtmgmtGatewayPingNumberOfPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 2, 1, 5),
    _CfprApExtmgmtGatewayPingNumberOfPingRequests_Type()
)
cfprApExtmgmtGatewayPingNumberOfPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtGatewayPingNumberOfPingRequests.setStatus("current")
_CfprApExtmgmtIfTable_Object = MibTable
cfprApExtmgmtIfTable = _CfprApExtmgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3)
)
if mibBuilder.loadTexts:
    cfprApExtmgmtIfTable.setStatus("current")
_CfprApExtmgmtIfEntry_Object = MibTableRow
cfprApExtmgmtIfEntry = _CfprApExtmgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1)
)
cfprApExtmgmtIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTMGMT-MIB", "cfprApExtmgmtIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtmgmtIfEntry.setStatus("current")
_CfprApExtmgmtIfInstanceId_Type = CfprApManagedObjectId
_CfprApExtmgmtIfInstanceId_Object = MibTableColumn
cfprApExtmgmtIfInstanceId = _CfprApExtmgmtIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 1),
    _CfprApExtmgmtIfInstanceId_Type()
)
cfprApExtmgmtIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfInstanceId.setStatus("current")
_CfprApExtmgmtIfDn_Type = CfprApManagedObjectDn
_CfprApExtmgmtIfDn_Object = MibTableColumn
cfprApExtmgmtIfDn = _CfprApExtmgmtIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 2),
    _CfprApExtmgmtIfDn_Type()
)
cfprApExtmgmtIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfDn.setStatus("current")
_CfprApExtmgmtIfRn_Type = SnmpAdminString
_CfprApExtmgmtIfRn_Object = MibTableColumn
cfprApExtmgmtIfRn = _CfprApExtmgmtIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 3),
    _CfprApExtmgmtIfRn_Type()
)
cfprApExtmgmtIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfRn.setStatus("current")
_CfprApExtmgmtIfEpDn_Type = SnmpAdminString
_CfprApExtmgmtIfEpDn_Object = MibTableColumn
cfprApExtmgmtIfEpDn = _CfprApExtmgmtIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 4),
    _CfprApExtmgmtIfEpDn_Type()
)
cfprApExtmgmtIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfEpDn.setStatus("current")
_CfprApExtmgmtIfFailReportCount_Type = Gauge32
_CfprApExtmgmtIfFailReportCount_Object = MibTableColumn
cfprApExtmgmtIfFailReportCount = _CfprApExtmgmtIfFailReportCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 5),
    _CfprApExtmgmtIfFailReportCount_Type()
)
cfprApExtmgmtIfFailReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfFailReportCount.setStatus("current")
_CfprApExtmgmtIfFltAggr_Type = Unsigned64
_CfprApExtmgmtIfFltAggr_Object = MibTableColumn
cfprApExtmgmtIfFltAggr = _CfprApExtmgmtIfFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 6),
    _CfprApExtmgmtIfFltAggr_Type()
)
cfprApExtmgmtIfFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfFltAggr.setStatus("current")
_CfprApExtmgmtIfId_Type = CfprApNetworkSwitchId
_CfprApExtmgmtIfId_Object = MibTableColumn
cfprApExtmgmtIfId = _CfprApExtmgmtIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 7),
    _CfprApExtmgmtIfId_Type()
)
cfprApExtmgmtIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfId.setStatus("current")
_CfprApExtmgmtIfIfRole_Type = CfprApNetworkPortRole
_CfprApExtmgmtIfIfRole_Object = MibTableColumn
cfprApExtmgmtIfIfRole = _CfprApExtmgmtIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 8),
    _CfprApExtmgmtIfIfRole_Type()
)
cfprApExtmgmtIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfIfRole.setStatus("current")
_CfprApExtmgmtIfIfType_Type = CfprApNetworkPortType
_CfprApExtmgmtIfIfType_Object = MibTableColumn
cfprApExtmgmtIfIfType = _CfprApExtmgmtIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 9),
    _CfprApExtmgmtIfIfType_Type()
)
cfprApExtmgmtIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfIfType.setStatus("current")
_CfprApExtmgmtIfLastOperStateReport_Type = CfprApNetworkIfStatus
_CfprApExtmgmtIfLastOperStateReport_Object = MibTableColumn
cfprApExtmgmtIfLastOperStateReport = _CfprApExtmgmtIfLastOperStateReport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 10),
    _CfprApExtmgmtIfLastOperStateReport_Type()
)
cfprApExtmgmtIfLastOperStateReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfLastOperStateReport.setStatus("current")
_CfprApExtmgmtIfLocale_Type = CfprApNetworkLocale
_CfprApExtmgmtIfLocale_Object = MibTableColumn
cfprApExtmgmtIfLocale = _CfprApExtmgmtIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 11),
    _CfprApExtmgmtIfLocale_Type()
)
cfprApExtmgmtIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfLocale.setStatus("current")
_CfprApExtmgmtIfName_Type = SnmpAdminString
_CfprApExtmgmtIfName_Object = MibTableColumn
cfprApExtmgmtIfName = _CfprApExtmgmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 12),
    _CfprApExtmgmtIfName_Type()
)
cfprApExtmgmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfName.setStatus("current")
_CfprApExtmgmtIfOperState_Type = CfprApNetworkIfStatus
_CfprApExtmgmtIfOperState_Object = MibTableColumn
cfprApExtmgmtIfOperState = _CfprApExtmgmtIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 13),
    _CfprApExtmgmtIfOperState_Type()
)
cfprApExtmgmtIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfOperState.setStatus("current")
_CfprApExtmgmtIfPeerDn_Type = SnmpAdminString
_CfprApExtmgmtIfPeerDn_Object = MibTableColumn
cfprApExtmgmtIfPeerDn = _CfprApExtmgmtIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 14),
    _CfprApExtmgmtIfPeerDn_Type()
)
cfprApExtmgmtIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfPeerDn.setStatus("current")
_CfprApExtmgmtIfTransport_Type = CfprApNetworkTransport
_CfprApExtmgmtIfTransport_Object = MibTableColumn
cfprApExtmgmtIfTransport = _CfprApExtmgmtIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 15),
    _CfprApExtmgmtIfTransport_Type()
)
cfprApExtmgmtIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfTransport.setStatus("current")
_CfprApExtmgmtIfType_Type = CfprApExtmgmtIfType
_CfprApExtmgmtIfType_Object = MibTableColumn
cfprApExtmgmtIfType = _CfprApExtmgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 3, 1, 16),
    _CfprApExtmgmtIfType_Type()
)
cfprApExtmgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfType.setStatus("current")
_CfprApExtmgmtIfMonPolicyTable_Object = MibTable
cfprApExtmgmtIfMonPolicyTable = _CfprApExtmgmtIfMonPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4)
)
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyTable.setStatus("current")
_CfprApExtmgmtIfMonPolicyEntry_Object = MibTableRow
cfprApExtmgmtIfMonPolicyEntry = _CfprApExtmgmtIfMonPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1)
)
cfprApExtmgmtIfMonPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTMGMT-MIB", "cfprApExtmgmtIfMonPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyEntry.setStatus("current")
_CfprApExtmgmtIfMonPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApExtmgmtIfMonPolicyInstanceId_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyInstanceId = _CfprApExtmgmtIfMonPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 1),
    _CfprApExtmgmtIfMonPolicyInstanceId_Type()
)
cfprApExtmgmtIfMonPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyInstanceId.setStatus("current")
_CfprApExtmgmtIfMonPolicyDn_Type = CfprApManagedObjectDn
_CfprApExtmgmtIfMonPolicyDn_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyDn = _CfprApExtmgmtIfMonPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 2),
    _CfprApExtmgmtIfMonPolicyDn_Type()
)
cfprApExtmgmtIfMonPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyDn.setStatus("current")
_CfprApExtmgmtIfMonPolicyRn_Type = SnmpAdminString
_CfprApExtmgmtIfMonPolicyRn_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyRn = _CfprApExtmgmtIfMonPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 3),
    _CfprApExtmgmtIfMonPolicyRn_Type()
)
cfprApExtmgmtIfMonPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyRn.setStatus("current")
_CfprApExtmgmtIfMonPolicyAdminState_Type = CfprApExtmgmtIfMonPolicyAdminState
_CfprApExtmgmtIfMonPolicyAdminState_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyAdminState = _CfprApExtmgmtIfMonPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 4),
    _CfprApExtmgmtIfMonPolicyAdminState_Type()
)
cfprApExtmgmtIfMonPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyAdminState.setStatus("current")
_CfprApExtmgmtIfMonPolicyDescr_Type = SnmpAdminString
_CfprApExtmgmtIfMonPolicyDescr_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyDescr = _CfprApExtmgmtIfMonPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 5),
    _CfprApExtmgmtIfMonPolicyDescr_Type()
)
cfprApExtmgmtIfMonPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyDescr.setStatus("current")
_CfprApExtmgmtIfMonPolicyEnableHAFailover_Type = TruthValue
_CfprApExtmgmtIfMonPolicyEnableHAFailover_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyEnableHAFailover = _CfprApExtmgmtIfMonPolicyEnableHAFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 6),
    _CfprApExtmgmtIfMonPolicyEnableHAFailover_Type()
)
cfprApExtmgmtIfMonPolicyEnableHAFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyEnableHAFailover.setStatus("current")
_CfprApExtmgmtIfMonPolicyIntId_Type = SnmpAdminString
_CfprApExtmgmtIfMonPolicyIntId_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyIntId = _CfprApExtmgmtIfMonPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 7),
    _CfprApExtmgmtIfMonPolicyIntId_Type()
)
cfprApExtmgmtIfMonPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyIntId.setStatus("current")
_CfprApExtmgmtIfMonPolicyMaxFailReportCount_Type = Gauge32
_CfprApExtmgmtIfMonPolicyMaxFailReportCount_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyMaxFailReportCount = _CfprApExtmgmtIfMonPolicyMaxFailReportCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 8),
    _CfprApExtmgmtIfMonPolicyMaxFailReportCount_Type()
)
cfprApExtmgmtIfMonPolicyMaxFailReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyMaxFailReportCount.setStatus("current")
_CfprApExtmgmtIfMonPolicyMonitorMechanism_Type = CfprApExtmgmtIfMonPolicyMonitorMechanism
_CfprApExtmgmtIfMonPolicyMonitorMechanism_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyMonitorMechanism = _CfprApExtmgmtIfMonPolicyMonitorMechanism_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 9),
    _CfprApExtmgmtIfMonPolicyMonitorMechanism_Type()
)
cfprApExtmgmtIfMonPolicyMonitorMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyMonitorMechanism.setStatus("current")
_CfprApExtmgmtIfMonPolicyName_Type = SnmpAdminString
_CfprApExtmgmtIfMonPolicyName_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyName = _CfprApExtmgmtIfMonPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 10),
    _CfprApExtmgmtIfMonPolicyName_Type()
)
cfprApExtmgmtIfMonPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyName.setStatus("current")
_CfprApExtmgmtIfMonPolicyPolicyLevel_Type = Gauge32
_CfprApExtmgmtIfMonPolicyPolicyLevel_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyPolicyLevel = _CfprApExtmgmtIfMonPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 11),
    _CfprApExtmgmtIfMonPolicyPolicyLevel_Type()
)
cfprApExtmgmtIfMonPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyPolicyLevel.setStatus("current")
_CfprApExtmgmtIfMonPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtmgmtIfMonPolicyPolicyOwner_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyPolicyOwner = _CfprApExtmgmtIfMonPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 12),
    _CfprApExtmgmtIfMonPolicyPolicyOwner_Type()
)
cfprApExtmgmtIfMonPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyPolicyOwner.setStatus("current")
_CfprApExtmgmtIfMonPolicyPollInterval_Type = Gauge32
_CfprApExtmgmtIfMonPolicyPollInterval_Object = MibTableColumn
cfprApExtmgmtIfMonPolicyPollInterval = _CfprApExtmgmtIfMonPolicyPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 4, 1, 13),
    _CfprApExtmgmtIfMonPolicyPollInterval_Type()
)
cfprApExtmgmtIfMonPolicyPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtIfMonPolicyPollInterval.setStatus("current")
_CfprApExtmgmtMiiStatusTable_Object = MibTable
cfprApExtmgmtMiiStatusTable = _CfprApExtmgmtMiiStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 5)
)
if mibBuilder.loadTexts:
    cfprApExtmgmtMiiStatusTable.setStatus("current")
_CfprApExtmgmtMiiStatusEntry_Object = MibTableRow
cfprApExtmgmtMiiStatusEntry = _CfprApExtmgmtMiiStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 5, 1)
)
cfprApExtmgmtMiiStatusEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTMGMT-MIB", "cfprApExtmgmtMiiStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtmgmtMiiStatusEntry.setStatus("current")
_CfprApExtmgmtMiiStatusInstanceId_Type = CfprApManagedObjectId
_CfprApExtmgmtMiiStatusInstanceId_Object = MibTableColumn
cfprApExtmgmtMiiStatusInstanceId = _CfprApExtmgmtMiiStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 5, 1, 1),
    _CfprApExtmgmtMiiStatusInstanceId_Type()
)
cfprApExtmgmtMiiStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtmgmtMiiStatusInstanceId.setStatus("current")
_CfprApExtmgmtMiiStatusDn_Type = CfprApManagedObjectDn
_CfprApExtmgmtMiiStatusDn_Object = MibTableColumn
cfprApExtmgmtMiiStatusDn = _CfprApExtmgmtMiiStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 5, 1, 2),
    _CfprApExtmgmtMiiStatusDn_Type()
)
cfprApExtmgmtMiiStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtMiiStatusDn.setStatus("current")
_CfprApExtmgmtMiiStatusRn_Type = SnmpAdminString
_CfprApExtmgmtMiiStatusRn_Object = MibTableColumn
cfprApExtmgmtMiiStatusRn = _CfprApExtmgmtMiiStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 5, 1, 3),
    _CfprApExtmgmtMiiStatusRn_Type()
)
cfprApExtmgmtMiiStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtMiiStatusRn.setStatus("current")
_CfprApExtmgmtMiiStatusMaxRetryCount_Type = CfprApExtmgmtMiiStatusMaxRetryCount
_CfprApExtmgmtMiiStatusMaxRetryCount_Object = MibTableColumn
cfprApExtmgmtMiiStatusMaxRetryCount = _CfprApExtmgmtMiiStatusMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 5, 1, 4),
    _CfprApExtmgmtMiiStatusMaxRetryCount_Type()
)
cfprApExtmgmtMiiStatusMaxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtMiiStatusMaxRetryCount.setStatus("current")
_CfprApExtmgmtMiiStatusRetryInterval_Type = CfprApExtmgmtMiiStatusRetryInterval
_CfprApExtmgmtMiiStatusRetryInterval_Object = MibTableColumn
cfprApExtmgmtMiiStatusRetryInterval = _CfprApExtmgmtMiiStatusRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 5, 1, 5),
    _CfprApExtmgmtMiiStatusRetryInterval_Type()
)
cfprApExtmgmtMiiStatusRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtMiiStatusRetryInterval.setStatus("current")
_CfprApExtmgmtNdiscTargetsTable_Object = MibTable
cfprApExtmgmtNdiscTargetsTable = _CfprApExtmgmtNdiscTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6)
)
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsTable.setStatus("current")
_CfprApExtmgmtNdiscTargetsEntry_Object = MibTableRow
cfprApExtmgmtNdiscTargetsEntry = _CfprApExtmgmtNdiscTargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1)
)
cfprApExtmgmtNdiscTargetsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTMGMT-MIB", "cfprApExtmgmtNdiscTargetsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsEntry.setStatus("current")
_CfprApExtmgmtNdiscTargetsInstanceId_Type = CfprApManagedObjectId
_CfprApExtmgmtNdiscTargetsInstanceId_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsInstanceId = _CfprApExtmgmtNdiscTargetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 1),
    _CfprApExtmgmtNdiscTargetsInstanceId_Type()
)
cfprApExtmgmtNdiscTargetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsInstanceId.setStatus("current")
_CfprApExtmgmtNdiscTargetsDn_Type = CfprApManagedObjectDn
_CfprApExtmgmtNdiscTargetsDn_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsDn = _CfprApExtmgmtNdiscTargetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 2),
    _CfprApExtmgmtNdiscTargetsDn_Type()
)
cfprApExtmgmtNdiscTargetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsDn.setStatus("current")
_CfprApExtmgmtNdiscTargetsRn_Type = SnmpAdminString
_CfprApExtmgmtNdiscTargetsRn_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsRn = _CfprApExtmgmtNdiscTargetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 3),
    _CfprApExtmgmtNdiscTargetsRn_Type()
)
cfprApExtmgmtNdiscTargetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsRn.setStatus("current")
_CfprApExtmgmtNdiscTargetsConfigState_Type = CfprApAaaConfigState
_CfprApExtmgmtNdiscTargetsConfigState_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsConfigState = _CfprApExtmgmtNdiscTargetsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 4),
    _CfprApExtmgmtNdiscTargetsConfigState_Type()
)
cfprApExtmgmtNdiscTargetsConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsConfigState.setStatus("current")
_CfprApExtmgmtNdiscTargetsConfigStatusMessage_Type = SnmpAdminString
_CfprApExtmgmtNdiscTargetsConfigStatusMessage_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsConfigStatusMessage = _CfprApExtmgmtNdiscTargetsConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 5),
    _CfprApExtmgmtNdiscTargetsConfigStatusMessage_Type()
)
cfprApExtmgmtNdiscTargetsConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsConfigStatusMessage.setStatus("current")
_CfprApExtmgmtNdiscTargetsIpv6Target1_Type = InetAddressIPv6
_CfprApExtmgmtNdiscTargetsIpv6Target1_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsIpv6Target1 = _CfprApExtmgmtNdiscTargetsIpv6Target1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 6),
    _CfprApExtmgmtNdiscTargetsIpv6Target1_Type()
)
cfprApExtmgmtNdiscTargetsIpv6Target1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsIpv6Target1.setStatus("current")
_CfprApExtmgmtNdiscTargetsIpv6Target2_Type = InetAddressIPv6
_CfprApExtmgmtNdiscTargetsIpv6Target2_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsIpv6Target2 = _CfprApExtmgmtNdiscTargetsIpv6Target2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 7),
    _CfprApExtmgmtNdiscTargetsIpv6Target2_Type()
)
cfprApExtmgmtNdiscTargetsIpv6Target2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsIpv6Target2.setStatus("current")
_CfprApExtmgmtNdiscTargetsIpv6Target3_Type = InetAddressIPv6
_CfprApExtmgmtNdiscTargetsIpv6Target3_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsIpv6Target3 = _CfprApExtmgmtNdiscTargetsIpv6Target3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 8),
    _CfprApExtmgmtNdiscTargetsIpv6Target3_Type()
)
cfprApExtmgmtNdiscTargetsIpv6Target3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsIpv6Target3.setStatus("current")
_CfprApExtmgmtNdiscTargetsMaxDeadlineTimeout_Type = CfprApExtmgmtNdiscTargetsMaxDeadlineTimeout
_CfprApExtmgmtNdiscTargetsMaxDeadlineTimeout_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsMaxDeadlineTimeout = _CfprApExtmgmtNdiscTargetsMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 9),
    _CfprApExtmgmtNdiscTargetsMaxDeadlineTimeout_Type()
)
cfprApExtmgmtNdiscTargetsMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsMaxDeadlineTimeout.setStatus("current")
_CfprApExtmgmtNdiscTargetsNumberOfNdiscRequests_Type = CfprApExtmgmtNdiscTargetsNumberOfNdiscRequests
_CfprApExtmgmtNdiscTargetsNumberOfNdiscRequests_Object = MibTableColumn
cfprApExtmgmtNdiscTargetsNumberOfNdiscRequests = _CfprApExtmgmtNdiscTargetsNumberOfNdiscRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 23, 6, 1, 10),
    _CfprApExtmgmtNdiscTargetsNumberOfNdiscRequests_Type()
)
cfprApExtmgmtNdiscTargetsNumberOfNdiscRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtmgmtNdiscTargetsNumberOfNdiscRequests.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-EXTMGMT-MIB",
    **{"cfprApExtmgmtObjects": cfprApExtmgmtObjects,
       "cfprApExtmgmtArpTargetsTable": cfprApExtmgmtArpTargetsTable,
       "cfprApExtmgmtArpTargetsEntry": cfprApExtmgmtArpTargetsEntry,
       "cfprApExtmgmtArpTargetsInstanceId": cfprApExtmgmtArpTargetsInstanceId,
       "cfprApExtmgmtArpTargetsDn": cfprApExtmgmtArpTargetsDn,
       "cfprApExtmgmtArpTargetsRn": cfprApExtmgmtArpTargetsRn,
       "cfprApExtmgmtArpTargetsConfigState": cfprApExtmgmtArpTargetsConfigState,
       "cfprApExtmgmtArpTargetsConfigStatusMessage": cfprApExtmgmtArpTargetsConfigStatusMessage,
       "cfprApExtmgmtArpTargetsMaxDeadlineTimeout": cfprApExtmgmtArpTargetsMaxDeadlineTimeout,
       "cfprApExtmgmtArpTargetsNumberOfArpRequests": cfprApExtmgmtArpTargetsNumberOfArpRequests,
       "cfprApExtmgmtArpTargetsTargetIp1": cfprApExtmgmtArpTargetsTargetIp1,
       "cfprApExtmgmtArpTargetsTargetIp2": cfprApExtmgmtArpTargetsTargetIp2,
       "cfprApExtmgmtArpTargetsTargetIp3": cfprApExtmgmtArpTargetsTargetIp3,
       "cfprApExtmgmtGatewayPingTable": cfprApExtmgmtGatewayPingTable,
       "cfprApExtmgmtGatewayPingEntry": cfprApExtmgmtGatewayPingEntry,
       "cfprApExtmgmtGatewayPingInstanceId": cfprApExtmgmtGatewayPingInstanceId,
       "cfprApExtmgmtGatewayPingDn": cfprApExtmgmtGatewayPingDn,
       "cfprApExtmgmtGatewayPingRn": cfprApExtmgmtGatewayPingRn,
       "cfprApExtmgmtGatewayPingMaxDeadlineTimeout": cfprApExtmgmtGatewayPingMaxDeadlineTimeout,
       "cfprApExtmgmtGatewayPingNumberOfPingRequests": cfprApExtmgmtGatewayPingNumberOfPingRequests,
       "cfprApExtmgmtIfTable": cfprApExtmgmtIfTable,
       "cfprApExtmgmtIfEntry": cfprApExtmgmtIfEntry,
       "cfprApExtmgmtIfInstanceId": cfprApExtmgmtIfInstanceId,
       "cfprApExtmgmtIfDn": cfprApExtmgmtIfDn,
       "cfprApExtmgmtIfRn": cfprApExtmgmtIfRn,
       "cfprApExtmgmtIfEpDn": cfprApExtmgmtIfEpDn,
       "cfprApExtmgmtIfFailReportCount": cfprApExtmgmtIfFailReportCount,
       "cfprApExtmgmtIfFltAggr": cfprApExtmgmtIfFltAggr,
       "cfprApExtmgmtIfId": cfprApExtmgmtIfId,
       "cfprApExtmgmtIfIfRole": cfprApExtmgmtIfIfRole,
       "cfprApExtmgmtIfIfType": cfprApExtmgmtIfIfType,
       "cfprApExtmgmtIfLastOperStateReport": cfprApExtmgmtIfLastOperStateReport,
       "cfprApExtmgmtIfLocale": cfprApExtmgmtIfLocale,
       "cfprApExtmgmtIfName": cfprApExtmgmtIfName,
       "cfprApExtmgmtIfOperState": cfprApExtmgmtIfOperState,
       "cfprApExtmgmtIfPeerDn": cfprApExtmgmtIfPeerDn,
       "cfprApExtmgmtIfTransport": cfprApExtmgmtIfTransport,
       "cfprApExtmgmtIfType": cfprApExtmgmtIfType,
       "cfprApExtmgmtIfMonPolicyTable": cfprApExtmgmtIfMonPolicyTable,
       "cfprApExtmgmtIfMonPolicyEntry": cfprApExtmgmtIfMonPolicyEntry,
       "cfprApExtmgmtIfMonPolicyInstanceId": cfprApExtmgmtIfMonPolicyInstanceId,
       "cfprApExtmgmtIfMonPolicyDn": cfprApExtmgmtIfMonPolicyDn,
       "cfprApExtmgmtIfMonPolicyRn": cfprApExtmgmtIfMonPolicyRn,
       "cfprApExtmgmtIfMonPolicyAdminState": cfprApExtmgmtIfMonPolicyAdminState,
       "cfprApExtmgmtIfMonPolicyDescr": cfprApExtmgmtIfMonPolicyDescr,
       "cfprApExtmgmtIfMonPolicyEnableHAFailover": cfprApExtmgmtIfMonPolicyEnableHAFailover,
       "cfprApExtmgmtIfMonPolicyIntId": cfprApExtmgmtIfMonPolicyIntId,
       "cfprApExtmgmtIfMonPolicyMaxFailReportCount": cfprApExtmgmtIfMonPolicyMaxFailReportCount,
       "cfprApExtmgmtIfMonPolicyMonitorMechanism": cfprApExtmgmtIfMonPolicyMonitorMechanism,
       "cfprApExtmgmtIfMonPolicyName": cfprApExtmgmtIfMonPolicyName,
       "cfprApExtmgmtIfMonPolicyPolicyLevel": cfprApExtmgmtIfMonPolicyPolicyLevel,
       "cfprApExtmgmtIfMonPolicyPolicyOwner": cfprApExtmgmtIfMonPolicyPolicyOwner,
       "cfprApExtmgmtIfMonPolicyPollInterval": cfprApExtmgmtIfMonPolicyPollInterval,
       "cfprApExtmgmtMiiStatusTable": cfprApExtmgmtMiiStatusTable,
       "cfprApExtmgmtMiiStatusEntry": cfprApExtmgmtMiiStatusEntry,
       "cfprApExtmgmtMiiStatusInstanceId": cfprApExtmgmtMiiStatusInstanceId,
       "cfprApExtmgmtMiiStatusDn": cfprApExtmgmtMiiStatusDn,
       "cfprApExtmgmtMiiStatusRn": cfprApExtmgmtMiiStatusRn,
       "cfprApExtmgmtMiiStatusMaxRetryCount": cfprApExtmgmtMiiStatusMaxRetryCount,
       "cfprApExtmgmtMiiStatusRetryInterval": cfprApExtmgmtMiiStatusRetryInterval,
       "cfprApExtmgmtNdiscTargetsTable": cfprApExtmgmtNdiscTargetsTable,
       "cfprApExtmgmtNdiscTargetsEntry": cfprApExtmgmtNdiscTargetsEntry,
       "cfprApExtmgmtNdiscTargetsInstanceId": cfprApExtmgmtNdiscTargetsInstanceId,
       "cfprApExtmgmtNdiscTargetsDn": cfprApExtmgmtNdiscTargetsDn,
       "cfprApExtmgmtNdiscTargetsRn": cfprApExtmgmtNdiscTargetsRn,
       "cfprApExtmgmtNdiscTargetsConfigState": cfprApExtmgmtNdiscTargetsConfigState,
       "cfprApExtmgmtNdiscTargetsConfigStatusMessage": cfprApExtmgmtNdiscTargetsConfigStatusMessage,
       "cfprApExtmgmtNdiscTargetsIpv6Target1": cfprApExtmgmtNdiscTargetsIpv6Target1,
       "cfprApExtmgmtNdiscTargetsIpv6Target2": cfprApExtmgmtNdiscTargetsIpv6Target2,
       "cfprApExtmgmtNdiscTargetsIpv6Target3": cfprApExtmgmtNdiscTargetsIpv6Target3,
       "cfprApExtmgmtNdiscTargetsMaxDeadlineTimeout": cfprApExtmgmtNdiscTargetsMaxDeadlineTimeout,
       "cfprApExtmgmtNdiscTargetsNumberOfNdiscRequests": cfprApExtmgmtNdiscTargetsNumberOfNdiscRequests}
)
