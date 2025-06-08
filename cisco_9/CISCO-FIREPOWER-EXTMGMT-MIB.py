# SNMP MIB module (CISCO-FIREPOWER-EXTMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-EXTMGMT-MIB.mib
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

(CfprAaaConfigState,
 CfprExtmgmtArpTargetsMaxDeadlineTimeout,
 CfprExtmgmtArpTargetsNumberOfArpRequests,
 CfprExtmgmtGatewayPingMaxDeadlineTimeout,
 CfprExtmgmtGatewayPingNumberOfPingRequests,
 CfprExtmgmtIfFailureReason,
 CfprExtmgmtIfMonPolicyAdminState,
 CfprExtmgmtIfMonPolicyMonitorMechanism,
 CfprExtmgmtIfType,
 CfprExtmgmtMiiStatusMaxRetryCount,
 CfprExtmgmtMiiStatusRetryInterval,
 CfprExtmgmtNdiscTargetsMaxDeadlineTimeout,
 CfprExtmgmtNdiscTargetsNumberOfNdiscRequests,
 CfprNetworkIfStatus,
 CfprNetworkLocale,
 CfprNetworkPortRole,
 CfprNetworkPortType,
 CfprNetworkSwitchId,
 CfprNetworkTransport,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAaaConfigState",
    "CfprExtmgmtArpTargetsMaxDeadlineTimeout",
    "CfprExtmgmtArpTargetsNumberOfArpRequests",
    "CfprExtmgmtGatewayPingMaxDeadlineTimeout",
    "CfprExtmgmtGatewayPingNumberOfPingRequests",
    "CfprExtmgmtIfFailureReason",
    "CfprExtmgmtIfMonPolicyAdminState",
    "CfprExtmgmtIfMonPolicyMonitorMechanism",
    "CfprExtmgmtIfType",
    "CfprExtmgmtMiiStatusMaxRetryCount",
    "CfprExtmgmtMiiStatusRetryInterval",
    "CfprExtmgmtNdiscTargetsMaxDeadlineTimeout",
    "CfprExtmgmtNdiscTargetsNumberOfNdiscRequests",
    "CfprNetworkIfStatus",
    "CfprNetworkLocale",
    "CfprNetworkPortRole",
    "CfprNetworkPortType",
    "CfprNetworkSwitchId",
    "CfprNetworkTransport",
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

cfprExtmgmtObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprExtmgmtArpTargetsTable_Object = MibTable
cfprExtmgmtArpTargetsTable = _CfprExtmgmtArpTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1)
)
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsTable.setStatus("current")
_CfprExtmgmtArpTargetsEntry_Object = MibTableRow
cfprExtmgmtArpTargetsEntry = _CfprExtmgmtArpTargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1)
)
cfprExtmgmtArpTargetsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTMGMT-MIB", "cfprExtmgmtArpTargetsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsEntry.setStatus("current")
_CfprExtmgmtArpTargetsInstanceId_Type = CfprManagedObjectId
_CfprExtmgmtArpTargetsInstanceId_Object = MibTableColumn
cfprExtmgmtArpTargetsInstanceId = _CfprExtmgmtArpTargetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 1),
    _CfprExtmgmtArpTargetsInstanceId_Type()
)
cfprExtmgmtArpTargetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsInstanceId.setStatus("current")
_CfprExtmgmtArpTargetsDn_Type = CfprManagedObjectDn
_CfprExtmgmtArpTargetsDn_Object = MibTableColumn
cfprExtmgmtArpTargetsDn = _CfprExtmgmtArpTargetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 2),
    _CfprExtmgmtArpTargetsDn_Type()
)
cfprExtmgmtArpTargetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsDn.setStatus("current")
_CfprExtmgmtArpTargetsRn_Type = SnmpAdminString
_CfprExtmgmtArpTargetsRn_Object = MibTableColumn
cfprExtmgmtArpTargetsRn = _CfprExtmgmtArpTargetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 3),
    _CfprExtmgmtArpTargetsRn_Type()
)
cfprExtmgmtArpTargetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsRn.setStatus("current")
_CfprExtmgmtArpTargetsConfigState_Type = CfprAaaConfigState
_CfprExtmgmtArpTargetsConfigState_Object = MibTableColumn
cfprExtmgmtArpTargetsConfigState = _CfprExtmgmtArpTargetsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 4),
    _CfprExtmgmtArpTargetsConfigState_Type()
)
cfprExtmgmtArpTargetsConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsConfigState.setStatus("current")
_CfprExtmgmtArpTargetsConfigStatusMessage_Type = SnmpAdminString
_CfprExtmgmtArpTargetsConfigStatusMessage_Object = MibTableColumn
cfprExtmgmtArpTargetsConfigStatusMessage = _CfprExtmgmtArpTargetsConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 5),
    _CfprExtmgmtArpTargetsConfigStatusMessage_Type()
)
cfprExtmgmtArpTargetsConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsConfigStatusMessage.setStatus("current")
_CfprExtmgmtArpTargetsMaxDeadlineTimeout_Type = CfprExtmgmtArpTargetsMaxDeadlineTimeout
_CfprExtmgmtArpTargetsMaxDeadlineTimeout_Object = MibTableColumn
cfprExtmgmtArpTargetsMaxDeadlineTimeout = _CfprExtmgmtArpTargetsMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 6),
    _CfprExtmgmtArpTargetsMaxDeadlineTimeout_Type()
)
cfprExtmgmtArpTargetsMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsMaxDeadlineTimeout.setStatus("current")
_CfprExtmgmtArpTargetsNumberOfArpRequests_Type = CfprExtmgmtArpTargetsNumberOfArpRequests
_CfprExtmgmtArpTargetsNumberOfArpRequests_Object = MibTableColumn
cfprExtmgmtArpTargetsNumberOfArpRequests = _CfprExtmgmtArpTargetsNumberOfArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 7),
    _CfprExtmgmtArpTargetsNumberOfArpRequests_Type()
)
cfprExtmgmtArpTargetsNumberOfArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsNumberOfArpRequests.setStatus("current")
_CfprExtmgmtArpTargetsTargetIp1_Type = InetAddressIPv4
_CfprExtmgmtArpTargetsTargetIp1_Object = MibTableColumn
cfprExtmgmtArpTargetsTargetIp1 = _CfprExtmgmtArpTargetsTargetIp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 8),
    _CfprExtmgmtArpTargetsTargetIp1_Type()
)
cfprExtmgmtArpTargetsTargetIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsTargetIp1.setStatus("current")
_CfprExtmgmtArpTargetsTargetIp2_Type = InetAddressIPv4
_CfprExtmgmtArpTargetsTargetIp2_Object = MibTableColumn
cfprExtmgmtArpTargetsTargetIp2 = _CfprExtmgmtArpTargetsTargetIp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 9),
    _CfprExtmgmtArpTargetsTargetIp2_Type()
)
cfprExtmgmtArpTargetsTargetIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsTargetIp2.setStatus("current")
_CfprExtmgmtArpTargetsTargetIp3_Type = InetAddressIPv4
_CfprExtmgmtArpTargetsTargetIp3_Object = MibTableColumn
cfprExtmgmtArpTargetsTargetIp3 = _CfprExtmgmtArpTargetsTargetIp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 1, 1, 10),
    _CfprExtmgmtArpTargetsTargetIp3_Type()
)
cfprExtmgmtArpTargetsTargetIp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtArpTargetsTargetIp3.setStatus("current")
_CfprExtmgmtGatewayPingTable_Object = MibTable
cfprExtmgmtGatewayPingTable = _CfprExtmgmtGatewayPingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 2)
)
if mibBuilder.loadTexts:
    cfprExtmgmtGatewayPingTable.setStatus("current")
_CfprExtmgmtGatewayPingEntry_Object = MibTableRow
cfprExtmgmtGatewayPingEntry = _CfprExtmgmtGatewayPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 2, 1)
)
cfprExtmgmtGatewayPingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTMGMT-MIB", "cfprExtmgmtGatewayPingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtmgmtGatewayPingEntry.setStatus("current")
_CfprExtmgmtGatewayPingInstanceId_Type = CfprManagedObjectId
_CfprExtmgmtGatewayPingInstanceId_Object = MibTableColumn
cfprExtmgmtGatewayPingInstanceId = _CfprExtmgmtGatewayPingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 2, 1, 1),
    _CfprExtmgmtGatewayPingInstanceId_Type()
)
cfprExtmgmtGatewayPingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtmgmtGatewayPingInstanceId.setStatus("current")
_CfprExtmgmtGatewayPingDn_Type = CfprManagedObjectDn
_CfprExtmgmtGatewayPingDn_Object = MibTableColumn
cfprExtmgmtGatewayPingDn = _CfprExtmgmtGatewayPingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 2, 1, 2),
    _CfprExtmgmtGatewayPingDn_Type()
)
cfprExtmgmtGatewayPingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtGatewayPingDn.setStatus("current")
_CfprExtmgmtGatewayPingRn_Type = SnmpAdminString
_CfprExtmgmtGatewayPingRn_Object = MibTableColumn
cfprExtmgmtGatewayPingRn = _CfprExtmgmtGatewayPingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 2, 1, 3),
    _CfprExtmgmtGatewayPingRn_Type()
)
cfprExtmgmtGatewayPingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtGatewayPingRn.setStatus("current")
_CfprExtmgmtGatewayPingMaxDeadlineTimeout_Type = CfprExtmgmtGatewayPingMaxDeadlineTimeout
_CfprExtmgmtGatewayPingMaxDeadlineTimeout_Object = MibTableColumn
cfprExtmgmtGatewayPingMaxDeadlineTimeout = _CfprExtmgmtGatewayPingMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 2, 1, 4),
    _CfprExtmgmtGatewayPingMaxDeadlineTimeout_Type()
)
cfprExtmgmtGatewayPingMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtGatewayPingMaxDeadlineTimeout.setStatus("current")
_CfprExtmgmtGatewayPingNumberOfPingRequests_Type = CfprExtmgmtGatewayPingNumberOfPingRequests
_CfprExtmgmtGatewayPingNumberOfPingRequests_Object = MibTableColumn
cfprExtmgmtGatewayPingNumberOfPingRequests = _CfprExtmgmtGatewayPingNumberOfPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 2, 1, 5),
    _CfprExtmgmtGatewayPingNumberOfPingRequests_Type()
)
cfprExtmgmtGatewayPingNumberOfPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtGatewayPingNumberOfPingRequests.setStatus("current")
_CfprExtmgmtIfTable_Object = MibTable
cfprExtmgmtIfTable = _CfprExtmgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3)
)
if mibBuilder.loadTexts:
    cfprExtmgmtIfTable.setStatus("current")
_CfprExtmgmtIfEntry_Object = MibTableRow
cfprExtmgmtIfEntry = _CfprExtmgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1)
)
cfprExtmgmtIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTMGMT-MIB", "cfprExtmgmtIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtmgmtIfEntry.setStatus("current")
_CfprExtmgmtIfInstanceId_Type = CfprManagedObjectId
_CfprExtmgmtIfInstanceId_Object = MibTableColumn
cfprExtmgmtIfInstanceId = _CfprExtmgmtIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 1),
    _CfprExtmgmtIfInstanceId_Type()
)
cfprExtmgmtIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtmgmtIfInstanceId.setStatus("current")
_CfprExtmgmtIfDn_Type = CfprManagedObjectDn
_CfprExtmgmtIfDn_Object = MibTableColumn
cfprExtmgmtIfDn = _CfprExtmgmtIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 2),
    _CfprExtmgmtIfDn_Type()
)
cfprExtmgmtIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfDn.setStatus("current")
_CfprExtmgmtIfRn_Type = SnmpAdminString
_CfprExtmgmtIfRn_Object = MibTableColumn
cfprExtmgmtIfRn = _CfprExtmgmtIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 3),
    _CfprExtmgmtIfRn_Type()
)
cfprExtmgmtIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfRn.setStatus("current")
_CfprExtmgmtIfEpDn_Type = SnmpAdminString
_CfprExtmgmtIfEpDn_Object = MibTableColumn
cfprExtmgmtIfEpDn = _CfprExtmgmtIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 4),
    _CfprExtmgmtIfEpDn_Type()
)
cfprExtmgmtIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfEpDn.setStatus("current")
_CfprExtmgmtIfFailReportCount_Type = Gauge32
_CfprExtmgmtIfFailReportCount_Object = MibTableColumn
cfprExtmgmtIfFailReportCount = _CfprExtmgmtIfFailReportCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 5),
    _CfprExtmgmtIfFailReportCount_Type()
)
cfprExtmgmtIfFailReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfFailReportCount.setStatus("current")
_CfprExtmgmtIfFltAggr_Type = Unsigned64
_CfprExtmgmtIfFltAggr_Object = MibTableColumn
cfprExtmgmtIfFltAggr = _CfprExtmgmtIfFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 6),
    _CfprExtmgmtIfFltAggr_Type()
)
cfprExtmgmtIfFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfFltAggr.setStatus("current")
_CfprExtmgmtIfId_Type = CfprNetworkSwitchId
_CfprExtmgmtIfId_Object = MibTableColumn
cfprExtmgmtIfId = _CfprExtmgmtIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 7),
    _CfprExtmgmtIfId_Type()
)
cfprExtmgmtIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfId.setStatus("current")
_CfprExtmgmtIfIfRole_Type = CfprNetworkPortRole
_CfprExtmgmtIfIfRole_Object = MibTableColumn
cfprExtmgmtIfIfRole = _CfprExtmgmtIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 8),
    _CfprExtmgmtIfIfRole_Type()
)
cfprExtmgmtIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfIfRole.setStatus("current")
_CfprExtmgmtIfIfType_Type = CfprNetworkPortType
_CfprExtmgmtIfIfType_Object = MibTableColumn
cfprExtmgmtIfIfType = _CfprExtmgmtIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 9),
    _CfprExtmgmtIfIfType_Type()
)
cfprExtmgmtIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfIfType.setStatus("current")
_CfprExtmgmtIfLastOperStateReport_Type = CfprNetworkIfStatus
_CfprExtmgmtIfLastOperStateReport_Object = MibTableColumn
cfprExtmgmtIfLastOperStateReport = _CfprExtmgmtIfLastOperStateReport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 10),
    _CfprExtmgmtIfLastOperStateReport_Type()
)
cfprExtmgmtIfLastOperStateReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfLastOperStateReport.setStatus("current")
_CfprExtmgmtIfLocale_Type = CfprNetworkLocale
_CfprExtmgmtIfLocale_Object = MibTableColumn
cfprExtmgmtIfLocale = _CfprExtmgmtIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 11),
    _CfprExtmgmtIfLocale_Type()
)
cfprExtmgmtIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfLocale.setStatus("current")
_CfprExtmgmtIfName_Type = SnmpAdminString
_CfprExtmgmtIfName_Object = MibTableColumn
cfprExtmgmtIfName = _CfprExtmgmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 12),
    _CfprExtmgmtIfName_Type()
)
cfprExtmgmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfName.setStatus("current")
_CfprExtmgmtIfOperState_Type = CfprNetworkIfStatus
_CfprExtmgmtIfOperState_Object = MibTableColumn
cfprExtmgmtIfOperState = _CfprExtmgmtIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 13),
    _CfprExtmgmtIfOperState_Type()
)
cfprExtmgmtIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfOperState.setStatus("current")
_CfprExtmgmtIfPeerDn_Type = SnmpAdminString
_CfprExtmgmtIfPeerDn_Object = MibTableColumn
cfprExtmgmtIfPeerDn = _CfprExtmgmtIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 14),
    _CfprExtmgmtIfPeerDn_Type()
)
cfprExtmgmtIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfPeerDn.setStatus("current")
_CfprExtmgmtIfTransport_Type = CfprNetworkTransport
_CfprExtmgmtIfTransport_Object = MibTableColumn
cfprExtmgmtIfTransport = _CfprExtmgmtIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 15),
    _CfprExtmgmtIfTransport_Type()
)
cfprExtmgmtIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfTransport.setStatus("current")
_CfprExtmgmtIfType_Type = CfprExtmgmtIfType
_CfprExtmgmtIfType_Object = MibTableColumn
cfprExtmgmtIfType = _CfprExtmgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 16),
    _CfprExtmgmtIfType_Type()
)
cfprExtmgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfType.setStatus("current")
_CfprExtmgmtIfFailureReason_Type = CfprExtmgmtIfFailureReason
_CfprExtmgmtIfFailureReason_Object = MibTableColumn
cfprExtmgmtIfFailureReason = _CfprExtmgmtIfFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 3, 1, 17),
    _CfprExtmgmtIfFailureReason_Type()
)
cfprExtmgmtIfFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfFailureReason.setStatus("current")
_CfprExtmgmtIfMonPolicyTable_Object = MibTable
cfprExtmgmtIfMonPolicyTable = _CfprExtmgmtIfMonPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4)
)
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyTable.setStatus("current")
_CfprExtmgmtIfMonPolicyEntry_Object = MibTableRow
cfprExtmgmtIfMonPolicyEntry = _CfprExtmgmtIfMonPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1)
)
cfprExtmgmtIfMonPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTMGMT-MIB", "cfprExtmgmtIfMonPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyEntry.setStatus("current")
_CfprExtmgmtIfMonPolicyInstanceId_Type = CfprManagedObjectId
_CfprExtmgmtIfMonPolicyInstanceId_Object = MibTableColumn
cfprExtmgmtIfMonPolicyInstanceId = _CfprExtmgmtIfMonPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 1),
    _CfprExtmgmtIfMonPolicyInstanceId_Type()
)
cfprExtmgmtIfMonPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyInstanceId.setStatus("current")
_CfprExtmgmtIfMonPolicyDn_Type = CfprManagedObjectDn
_CfprExtmgmtIfMonPolicyDn_Object = MibTableColumn
cfprExtmgmtIfMonPolicyDn = _CfprExtmgmtIfMonPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 2),
    _CfprExtmgmtIfMonPolicyDn_Type()
)
cfprExtmgmtIfMonPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyDn.setStatus("current")
_CfprExtmgmtIfMonPolicyRn_Type = SnmpAdminString
_CfprExtmgmtIfMonPolicyRn_Object = MibTableColumn
cfprExtmgmtIfMonPolicyRn = _CfprExtmgmtIfMonPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 3),
    _CfprExtmgmtIfMonPolicyRn_Type()
)
cfprExtmgmtIfMonPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyRn.setStatus("current")
_CfprExtmgmtIfMonPolicyAdminState_Type = CfprExtmgmtIfMonPolicyAdminState
_CfprExtmgmtIfMonPolicyAdminState_Object = MibTableColumn
cfprExtmgmtIfMonPolicyAdminState = _CfprExtmgmtIfMonPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 4),
    _CfprExtmgmtIfMonPolicyAdminState_Type()
)
cfprExtmgmtIfMonPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyAdminState.setStatus("current")
_CfprExtmgmtIfMonPolicyDescr_Type = SnmpAdminString
_CfprExtmgmtIfMonPolicyDescr_Object = MibTableColumn
cfprExtmgmtIfMonPolicyDescr = _CfprExtmgmtIfMonPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 5),
    _CfprExtmgmtIfMonPolicyDescr_Type()
)
cfprExtmgmtIfMonPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyDescr.setStatus("current")
_CfprExtmgmtIfMonPolicyEnableHAFailover_Type = TruthValue
_CfprExtmgmtIfMonPolicyEnableHAFailover_Object = MibTableColumn
cfprExtmgmtIfMonPolicyEnableHAFailover = _CfprExtmgmtIfMonPolicyEnableHAFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 6),
    _CfprExtmgmtIfMonPolicyEnableHAFailover_Type()
)
cfprExtmgmtIfMonPolicyEnableHAFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyEnableHAFailover.setStatus("current")
_CfprExtmgmtIfMonPolicyIntId_Type = SnmpAdminString
_CfprExtmgmtIfMonPolicyIntId_Object = MibTableColumn
cfprExtmgmtIfMonPolicyIntId = _CfprExtmgmtIfMonPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 7),
    _CfprExtmgmtIfMonPolicyIntId_Type()
)
cfprExtmgmtIfMonPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyIntId.setStatus("current")
_CfprExtmgmtIfMonPolicyMaxFailReportCount_Type = Gauge32
_CfprExtmgmtIfMonPolicyMaxFailReportCount_Object = MibTableColumn
cfprExtmgmtIfMonPolicyMaxFailReportCount = _CfprExtmgmtIfMonPolicyMaxFailReportCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 8),
    _CfprExtmgmtIfMonPolicyMaxFailReportCount_Type()
)
cfprExtmgmtIfMonPolicyMaxFailReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyMaxFailReportCount.setStatus("current")
_CfprExtmgmtIfMonPolicyMonitorMechanism_Type = CfprExtmgmtIfMonPolicyMonitorMechanism
_CfprExtmgmtIfMonPolicyMonitorMechanism_Object = MibTableColumn
cfprExtmgmtIfMonPolicyMonitorMechanism = _CfprExtmgmtIfMonPolicyMonitorMechanism_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 9),
    _CfprExtmgmtIfMonPolicyMonitorMechanism_Type()
)
cfprExtmgmtIfMonPolicyMonitorMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyMonitorMechanism.setStatus("current")
_CfprExtmgmtIfMonPolicyName_Type = SnmpAdminString
_CfprExtmgmtIfMonPolicyName_Object = MibTableColumn
cfprExtmgmtIfMonPolicyName = _CfprExtmgmtIfMonPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 10),
    _CfprExtmgmtIfMonPolicyName_Type()
)
cfprExtmgmtIfMonPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyName.setStatus("current")
_CfprExtmgmtIfMonPolicyPolicyLevel_Type = Gauge32
_CfprExtmgmtIfMonPolicyPolicyLevel_Object = MibTableColumn
cfprExtmgmtIfMonPolicyPolicyLevel = _CfprExtmgmtIfMonPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 11),
    _CfprExtmgmtIfMonPolicyPolicyLevel_Type()
)
cfprExtmgmtIfMonPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyPolicyLevel.setStatus("current")
_CfprExtmgmtIfMonPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprExtmgmtIfMonPolicyPolicyOwner_Object = MibTableColumn
cfprExtmgmtIfMonPolicyPolicyOwner = _CfprExtmgmtIfMonPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 12),
    _CfprExtmgmtIfMonPolicyPolicyOwner_Type()
)
cfprExtmgmtIfMonPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyPolicyOwner.setStatus("current")
_CfprExtmgmtIfMonPolicyPollInterval_Type = Gauge32
_CfprExtmgmtIfMonPolicyPollInterval_Object = MibTableColumn
cfprExtmgmtIfMonPolicyPollInterval = _CfprExtmgmtIfMonPolicyPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 4, 1, 13),
    _CfprExtmgmtIfMonPolicyPollInterval_Type()
)
cfprExtmgmtIfMonPolicyPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtIfMonPolicyPollInterval.setStatus("current")
_CfprExtmgmtMiiStatusTable_Object = MibTable
cfprExtmgmtMiiStatusTable = _CfprExtmgmtMiiStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 5)
)
if mibBuilder.loadTexts:
    cfprExtmgmtMiiStatusTable.setStatus("current")
_CfprExtmgmtMiiStatusEntry_Object = MibTableRow
cfprExtmgmtMiiStatusEntry = _CfprExtmgmtMiiStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 5, 1)
)
cfprExtmgmtMiiStatusEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTMGMT-MIB", "cfprExtmgmtMiiStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtmgmtMiiStatusEntry.setStatus("current")
_CfprExtmgmtMiiStatusInstanceId_Type = CfprManagedObjectId
_CfprExtmgmtMiiStatusInstanceId_Object = MibTableColumn
cfprExtmgmtMiiStatusInstanceId = _CfprExtmgmtMiiStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 5, 1, 1),
    _CfprExtmgmtMiiStatusInstanceId_Type()
)
cfprExtmgmtMiiStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtmgmtMiiStatusInstanceId.setStatus("current")
_CfprExtmgmtMiiStatusDn_Type = CfprManagedObjectDn
_CfprExtmgmtMiiStatusDn_Object = MibTableColumn
cfprExtmgmtMiiStatusDn = _CfprExtmgmtMiiStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 5, 1, 2),
    _CfprExtmgmtMiiStatusDn_Type()
)
cfprExtmgmtMiiStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtMiiStatusDn.setStatus("current")
_CfprExtmgmtMiiStatusRn_Type = SnmpAdminString
_CfprExtmgmtMiiStatusRn_Object = MibTableColumn
cfprExtmgmtMiiStatusRn = _CfprExtmgmtMiiStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 5, 1, 3),
    _CfprExtmgmtMiiStatusRn_Type()
)
cfprExtmgmtMiiStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtMiiStatusRn.setStatus("current")
_CfprExtmgmtMiiStatusMaxRetryCount_Type = CfprExtmgmtMiiStatusMaxRetryCount
_CfprExtmgmtMiiStatusMaxRetryCount_Object = MibTableColumn
cfprExtmgmtMiiStatusMaxRetryCount = _CfprExtmgmtMiiStatusMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 5, 1, 4),
    _CfprExtmgmtMiiStatusMaxRetryCount_Type()
)
cfprExtmgmtMiiStatusMaxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtMiiStatusMaxRetryCount.setStatus("current")
_CfprExtmgmtMiiStatusRetryInterval_Type = CfprExtmgmtMiiStatusRetryInterval
_CfprExtmgmtMiiStatusRetryInterval_Object = MibTableColumn
cfprExtmgmtMiiStatusRetryInterval = _CfprExtmgmtMiiStatusRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 5, 1, 5),
    _CfprExtmgmtMiiStatusRetryInterval_Type()
)
cfprExtmgmtMiiStatusRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtMiiStatusRetryInterval.setStatus("current")
_CfprExtmgmtNdiscTargetsTable_Object = MibTable
cfprExtmgmtNdiscTargetsTable = _CfprExtmgmtNdiscTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6)
)
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsTable.setStatus("current")
_CfprExtmgmtNdiscTargetsEntry_Object = MibTableRow
cfprExtmgmtNdiscTargetsEntry = _CfprExtmgmtNdiscTargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1)
)
cfprExtmgmtNdiscTargetsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTMGMT-MIB", "cfprExtmgmtNdiscTargetsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsEntry.setStatus("current")
_CfprExtmgmtNdiscTargetsInstanceId_Type = CfprManagedObjectId
_CfprExtmgmtNdiscTargetsInstanceId_Object = MibTableColumn
cfprExtmgmtNdiscTargetsInstanceId = _CfprExtmgmtNdiscTargetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 1),
    _CfprExtmgmtNdiscTargetsInstanceId_Type()
)
cfprExtmgmtNdiscTargetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsInstanceId.setStatus("current")
_CfprExtmgmtNdiscTargetsDn_Type = CfprManagedObjectDn
_CfprExtmgmtNdiscTargetsDn_Object = MibTableColumn
cfprExtmgmtNdiscTargetsDn = _CfprExtmgmtNdiscTargetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 2),
    _CfprExtmgmtNdiscTargetsDn_Type()
)
cfprExtmgmtNdiscTargetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsDn.setStatus("current")
_CfprExtmgmtNdiscTargetsRn_Type = SnmpAdminString
_CfprExtmgmtNdiscTargetsRn_Object = MibTableColumn
cfprExtmgmtNdiscTargetsRn = _CfprExtmgmtNdiscTargetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 3),
    _CfprExtmgmtNdiscTargetsRn_Type()
)
cfprExtmgmtNdiscTargetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsRn.setStatus("current")
_CfprExtmgmtNdiscTargetsConfigState_Type = CfprAaaConfigState
_CfprExtmgmtNdiscTargetsConfigState_Object = MibTableColumn
cfprExtmgmtNdiscTargetsConfigState = _CfprExtmgmtNdiscTargetsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 4),
    _CfprExtmgmtNdiscTargetsConfigState_Type()
)
cfprExtmgmtNdiscTargetsConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsConfigState.setStatus("current")
_CfprExtmgmtNdiscTargetsConfigStatusMessage_Type = SnmpAdminString
_CfprExtmgmtNdiscTargetsConfigStatusMessage_Object = MibTableColumn
cfprExtmgmtNdiscTargetsConfigStatusMessage = _CfprExtmgmtNdiscTargetsConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 5),
    _CfprExtmgmtNdiscTargetsConfigStatusMessage_Type()
)
cfprExtmgmtNdiscTargetsConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsConfigStatusMessage.setStatus("current")
_CfprExtmgmtNdiscTargetsIpv6Target1_Type = InetAddressIPv6
_CfprExtmgmtNdiscTargetsIpv6Target1_Object = MibTableColumn
cfprExtmgmtNdiscTargetsIpv6Target1 = _CfprExtmgmtNdiscTargetsIpv6Target1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 6),
    _CfprExtmgmtNdiscTargetsIpv6Target1_Type()
)
cfprExtmgmtNdiscTargetsIpv6Target1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsIpv6Target1.setStatus("current")
_CfprExtmgmtNdiscTargetsIpv6Target2_Type = InetAddressIPv6
_CfprExtmgmtNdiscTargetsIpv6Target2_Object = MibTableColumn
cfprExtmgmtNdiscTargetsIpv6Target2 = _CfprExtmgmtNdiscTargetsIpv6Target2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 7),
    _CfprExtmgmtNdiscTargetsIpv6Target2_Type()
)
cfprExtmgmtNdiscTargetsIpv6Target2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsIpv6Target2.setStatus("current")
_CfprExtmgmtNdiscTargetsIpv6Target3_Type = InetAddressIPv6
_CfprExtmgmtNdiscTargetsIpv6Target3_Object = MibTableColumn
cfprExtmgmtNdiscTargetsIpv6Target3 = _CfprExtmgmtNdiscTargetsIpv6Target3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 8),
    _CfprExtmgmtNdiscTargetsIpv6Target3_Type()
)
cfprExtmgmtNdiscTargetsIpv6Target3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsIpv6Target3.setStatus("current")
_CfprExtmgmtNdiscTargetsMaxDeadlineTimeout_Type = CfprExtmgmtNdiscTargetsMaxDeadlineTimeout
_CfprExtmgmtNdiscTargetsMaxDeadlineTimeout_Object = MibTableColumn
cfprExtmgmtNdiscTargetsMaxDeadlineTimeout = _CfprExtmgmtNdiscTargetsMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 9),
    _CfprExtmgmtNdiscTargetsMaxDeadlineTimeout_Type()
)
cfprExtmgmtNdiscTargetsMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsMaxDeadlineTimeout.setStatus("current")
_CfprExtmgmtNdiscTargetsNumberOfNdiscRequests_Type = CfprExtmgmtNdiscTargetsNumberOfNdiscRequests
_CfprExtmgmtNdiscTargetsNumberOfNdiscRequests_Object = MibTableColumn
cfprExtmgmtNdiscTargetsNumberOfNdiscRequests = _CfprExtmgmtNdiscTargetsNumberOfNdiscRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 23, 6, 1, 10),
    _CfprExtmgmtNdiscTargetsNumberOfNdiscRequests_Type()
)
cfprExtmgmtNdiscTargetsNumberOfNdiscRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtmgmtNdiscTargetsNumberOfNdiscRequests.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-EXTMGMT-MIB",
    **{"cfprExtmgmtObjects": cfprExtmgmtObjects,
       "cfprExtmgmtArpTargetsTable": cfprExtmgmtArpTargetsTable,
       "cfprExtmgmtArpTargetsEntry": cfprExtmgmtArpTargetsEntry,
       "cfprExtmgmtArpTargetsInstanceId": cfprExtmgmtArpTargetsInstanceId,
       "cfprExtmgmtArpTargetsDn": cfprExtmgmtArpTargetsDn,
       "cfprExtmgmtArpTargetsRn": cfprExtmgmtArpTargetsRn,
       "cfprExtmgmtArpTargetsConfigState": cfprExtmgmtArpTargetsConfigState,
       "cfprExtmgmtArpTargetsConfigStatusMessage": cfprExtmgmtArpTargetsConfigStatusMessage,
       "cfprExtmgmtArpTargetsMaxDeadlineTimeout": cfprExtmgmtArpTargetsMaxDeadlineTimeout,
       "cfprExtmgmtArpTargetsNumberOfArpRequests": cfprExtmgmtArpTargetsNumberOfArpRequests,
       "cfprExtmgmtArpTargetsTargetIp1": cfprExtmgmtArpTargetsTargetIp1,
       "cfprExtmgmtArpTargetsTargetIp2": cfprExtmgmtArpTargetsTargetIp2,
       "cfprExtmgmtArpTargetsTargetIp3": cfprExtmgmtArpTargetsTargetIp3,
       "cfprExtmgmtGatewayPingTable": cfprExtmgmtGatewayPingTable,
       "cfprExtmgmtGatewayPingEntry": cfprExtmgmtGatewayPingEntry,
       "cfprExtmgmtGatewayPingInstanceId": cfprExtmgmtGatewayPingInstanceId,
       "cfprExtmgmtGatewayPingDn": cfprExtmgmtGatewayPingDn,
       "cfprExtmgmtGatewayPingRn": cfprExtmgmtGatewayPingRn,
       "cfprExtmgmtGatewayPingMaxDeadlineTimeout": cfprExtmgmtGatewayPingMaxDeadlineTimeout,
       "cfprExtmgmtGatewayPingNumberOfPingRequests": cfprExtmgmtGatewayPingNumberOfPingRequests,
       "cfprExtmgmtIfTable": cfprExtmgmtIfTable,
       "cfprExtmgmtIfEntry": cfprExtmgmtIfEntry,
       "cfprExtmgmtIfInstanceId": cfprExtmgmtIfInstanceId,
       "cfprExtmgmtIfDn": cfprExtmgmtIfDn,
       "cfprExtmgmtIfRn": cfprExtmgmtIfRn,
       "cfprExtmgmtIfEpDn": cfprExtmgmtIfEpDn,
       "cfprExtmgmtIfFailReportCount": cfprExtmgmtIfFailReportCount,
       "cfprExtmgmtIfFltAggr": cfprExtmgmtIfFltAggr,
       "cfprExtmgmtIfId": cfprExtmgmtIfId,
       "cfprExtmgmtIfIfRole": cfprExtmgmtIfIfRole,
       "cfprExtmgmtIfIfType": cfprExtmgmtIfIfType,
       "cfprExtmgmtIfLastOperStateReport": cfprExtmgmtIfLastOperStateReport,
       "cfprExtmgmtIfLocale": cfprExtmgmtIfLocale,
       "cfprExtmgmtIfName": cfprExtmgmtIfName,
       "cfprExtmgmtIfOperState": cfprExtmgmtIfOperState,
       "cfprExtmgmtIfPeerDn": cfprExtmgmtIfPeerDn,
       "cfprExtmgmtIfTransport": cfprExtmgmtIfTransport,
       "cfprExtmgmtIfType": cfprExtmgmtIfType,
       "cfprExtmgmtIfFailureReason": cfprExtmgmtIfFailureReason,
       "cfprExtmgmtIfMonPolicyTable": cfprExtmgmtIfMonPolicyTable,
       "cfprExtmgmtIfMonPolicyEntry": cfprExtmgmtIfMonPolicyEntry,
       "cfprExtmgmtIfMonPolicyInstanceId": cfprExtmgmtIfMonPolicyInstanceId,
       "cfprExtmgmtIfMonPolicyDn": cfprExtmgmtIfMonPolicyDn,
       "cfprExtmgmtIfMonPolicyRn": cfprExtmgmtIfMonPolicyRn,
       "cfprExtmgmtIfMonPolicyAdminState": cfprExtmgmtIfMonPolicyAdminState,
       "cfprExtmgmtIfMonPolicyDescr": cfprExtmgmtIfMonPolicyDescr,
       "cfprExtmgmtIfMonPolicyEnableHAFailover": cfprExtmgmtIfMonPolicyEnableHAFailover,
       "cfprExtmgmtIfMonPolicyIntId": cfprExtmgmtIfMonPolicyIntId,
       "cfprExtmgmtIfMonPolicyMaxFailReportCount": cfprExtmgmtIfMonPolicyMaxFailReportCount,
       "cfprExtmgmtIfMonPolicyMonitorMechanism": cfprExtmgmtIfMonPolicyMonitorMechanism,
       "cfprExtmgmtIfMonPolicyName": cfprExtmgmtIfMonPolicyName,
       "cfprExtmgmtIfMonPolicyPolicyLevel": cfprExtmgmtIfMonPolicyPolicyLevel,
       "cfprExtmgmtIfMonPolicyPolicyOwner": cfprExtmgmtIfMonPolicyPolicyOwner,
       "cfprExtmgmtIfMonPolicyPollInterval": cfprExtmgmtIfMonPolicyPollInterval,
       "cfprExtmgmtMiiStatusTable": cfprExtmgmtMiiStatusTable,
       "cfprExtmgmtMiiStatusEntry": cfprExtmgmtMiiStatusEntry,
       "cfprExtmgmtMiiStatusInstanceId": cfprExtmgmtMiiStatusInstanceId,
       "cfprExtmgmtMiiStatusDn": cfprExtmgmtMiiStatusDn,
       "cfprExtmgmtMiiStatusRn": cfprExtmgmtMiiStatusRn,
       "cfprExtmgmtMiiStatusMaxRetryCount": cfprExtmgmtMiiStatusMaxRetryCount,
       "cfprExtmgmtMiiStatusRetryInterval": cfprExtmgmtMiiStatusRetryInterval,
       "cfprExtmgmtNdiscTargetsTable": cfprExtmgmtNdiscTargetsTable,
       "cfprExtmgmtNdiscTargetsEntry": cfprExtmgmtNdiscTargetsEntry,
       "cfprExtmgmtNdiscTargetsInstanceId": cfprExtmgmtNdiscTargetsInstanceId,
       "cfprExtmgmtNdiscTargetsDn": cfprExtmgmtNdiscTargetsDn,
       "cfprExtmgmtNdiscTargetsRn": cfprExtmgmtNdiscTargetsRn,
       "cfprExtmgmtNdiscTargetsConfigState": cfprExtmgmtNdiscTargetsConfigState,
       "cfprExtmgmtNdiscTargetsConfigStatusMessage": cfprExtmgmtNdiscTargetsConfigStatusMessage,
       "cfprExtmgmtNdiscTargetsIpv6Target1": cfprExtmgmtNdiscTargetsIpv6Target1,
       "cfprExtmgmtNdiscTargetsIpv6Target2": cfprExtmgmtNdiscTargetsIpv6Target2,
       "cfprExtmgmtNdiscTargetsIpv6Target3": cfprExtmgmtNdiscTargetsIpv6Target3,
       "cfprExtmgmtNdiscTargetsMaxDeadlineTimeout": cfprExtmgmtNdiscTargetsMaxDeadlineTimeout,
       "cfprExtmgmtNdiscTargetsNumberOfNdiscRequests": cfprExtmgmtNdiscTargetsNumberOfNdiscRequests}
)
