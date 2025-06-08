# SNMP MIB module (CISCO-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DHCP-RELAY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:02:45 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "InterfaceIndexOrZero")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 833)
)
if mibBuilder.loadTexts:
    ciscoDhcpRelayMIB.setRevisions(
        ("2016-09-16 00:00",
         "2016-06-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDhcpRelayMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDhcpRelayMIBNotifs = _CiscoDhcpRelayMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 0)
)
_CiscoDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDhcpRelayMIBObjects = _CiscoDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1)
)
_CiscoDhcpRelayStats_ObjectIdentity = ObjectIdentity
ciscoDhcpRelayStats = _CiscoDhcpRelayStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1)
)
_CdrStatsTable_Object = MibTable
cdrStatsTable = _CdrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdrStatsTable.setStatus("current")
_CdrStatsEntry_Object = MibTableRow
cdrStatsEntry = _CdrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 1, 1)
)
cdrStatsEntry.setIndexNames(
    (0, "CISCO-DHCP-RELAY-MIB", "cdrStatsIfIndex"),
    (0, "CISCO-DHCP-RELAY-MIB", "cdrStatsPktType"),
)
if mibBuilder.loadTexts:
    cdrStatsEntry.setStatus("current")
_CdrStatsIfIndex_Type = InterfaceIndexOrZero
_CdrStatsIfIndex_Object = MibTableColumn
cdrStatsIfIndex = _CdrStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 1, 1, 1),
    _CdrStatsIfIndex_Type()
)
cdrStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdrStatsIfIndex.setStatus("current")


class _CdrStatsPktType_Type(Integer32):
    """Custom type cdrStatsPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("discover", 1),
          ("offer", 2),
          ("request", 3),
          ("ack", 4),
          ("release", 5),
          ("decline", 6),
          ("inform", 7),
          ("nack", 8),
          ("dhcpL3Fwd", 9),
          ("nonDhcp", 10))
    )


_CdrStatsPktType_Type.__name__ = "Integer32"
_CdrStatsPktType_Object = MibTableColumn
cdrStatsPktType = _CdrStatsPktType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 1, 1, 2),
    _CdrStatsPktType_Type()
)
cdrStatsPktType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdrStatsPktType.setStatus("current")
_CdrStatsPktsReceived_Type = Counter32
_CdrStatsPktsReceived_Object = MibTableColumn
cdrStatsPktsReceived = _CdrStatsPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 1, 1, 3),
    _CdrStatsPktsReceived_Type()
)
cdrStatsPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrStatsPktsReceived.setStatus("current")
_CdrStatsPktsForwarded_Type = Counter32
_CdrStatsPktsForwarded_Object = MibTableColumn
cdrStatsPktsForwarded = _CdrStatsPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 1, 1, 4),
    _CdrStatsPktsForwarded_Type()
)
cdrStatsPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrStatsPktsForwarded.setStatus("current")
_CdrStatsPktsDropped_Type = Counter32
_CdrStatsPktsDropped_Object = MibTableColumn
cdrStatsPktsDropped = _CdrStatsPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 1, 1, 5),
    _CdrStatsPktsDropped_Type()
)
cdrStatsPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrStatsPktsDropped.setStatus("current")
_CdrDropStatsTable_Object = MibTable
cdrDropStatsTable = _CdrDropStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdrDropStatsTable.setStatus("current")
_CdrDropStatsEntry_Object = MibTableRow
cdrDropStatsEntry = _CdrDropStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1)
)
cdrDropStatsEntry.setIndexNames(
    (0, "CISCO-DHCP-RELAY-MIB", "cdrDropStatsIfIndex"),
)
if mibBuilder.loadTexts:
    cdrDropStatsEntry.setStatus("current")
_CdrDropStatsIfIndex_Type = InterfaceIndexOrZero
_CdrDropStatsIfIndex_Object = MibTableColumn
cdrDropStatsIfIndex = _CdrDropStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 1),
    _CdrDropStatsIfIndex_Type()
)
cdrDropStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdrDropStatsIfIndex.setStatus("current")
_CdrDropStatsRelayNotEnabled_Type = Counter32
_CdrDropStatsRelayNotEnabled_Object = MibTableColumn
cdrDropStatsRelayNotEnabled = _CdrDropStatsRelayNotEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 2),
    _CdrDropStatsRelayNotEnabled_Type()
)
cdrDropStatsRelayNotEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsRelayNotEnabled.setStatus("current")
_CdrDropStatsInvalidMsgType_Type = Counter32
_CdrDropStatsInvalidMsgType_Object = MibTableColumn
cdrDropStatsInvalidMsgType = _CdrDropStatsInvalidMsgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 3),
    _CdrDropStatsInvalidMsgType_Type()
)
cdrDropStatsInvalidMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsInvalidMsgType.setStatus("current")
_CdrDropStatsInterfaceError_Type = Counter32
_CdrDropStatsInterfaceError_Object = MibTableColumn
cdrDropStatsInterfaceError = _CdrDropStatsInterfaceError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 4),
    _CdrDropStatsInterfaceError_Type()
)
cdrDropStatsInterfaceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsInterfaceError.setStatus("current")
_CdrDropStatsTxFailureServer_Type = Counter32
_CdrDropStatsTxFailureServer_Object = MibTableColumn
cdrDropStatsTxFailureServer = _CdrDropStatsTxFailureServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 5),
    _CdrDropStatsTxFailureServer_Type()
)
cdrDropStatsTxFailureServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsTxFailureServer.setStatus("current")
_CdrDropStatsTxFailureClient_Type = Counter32
_CdrDropStatsTxFailureClient_Object = MibTableColumn
cdrDropStatsTxFailureClient = _CdrDropStatsTxFailureClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 6),
    _CdrDropStatsTxFailureClient_Type()
)
cdrDropStatsTxFailureClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsTxFailureClient.setStatus("current")
_CdrDropStatsUnknownOpInterface_Type = Counter32
_CdrDropStatsUnknownOpInterface_Object = MibTableColumn
cdrDropStatsUnknownOpInterface = _CdrDropStatsUnknownOpInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 7),
    _CdrDropStatsUnknownOpInterface_Type()
)
cdrDropStatsUnknownOpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsUnknownOpInterface.setStatus("current")
_CdrDropStatsUnknownVrfOrInterface_Type = Counter32
_CdrDropStatsUnknownVrfOrInterface_Object = MibTableColumn
cdrDropStatsUnknownVrfOrInterface = _CdrDropStatsUnknownVrfOrInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 8),
    _CdrDropStatsUnknownVrfOrInterface_Type()
)
cdrDropStatsUnknownVrfOrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsUnknownVrfOrInterface.setStatus("current")
_CdrDropStatsMaxHopsExceeded_Type = Counter32
_CdrDropStatsMaxHopsExceeded_Object = MibTableColumn
cdrDropStatsMaxHopsExceeded = _CdrDropStatsMaxHopsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 9),
    _CdrDropStatsMaxHopsExceeded_Type()
)
cdrDropStatsMaxHopsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsMaxHopsExceeded.setStatus("current")
_CdrDropStatsOpt82ValidationFailure_Type = Counter32
_CdrDropStatsOpt82ValidationFailure_Object = MibTableColumn
cdrDropStatsOpt82ValidationFailure = _CdrDropStatsOpt82ValidationFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 10),
    _CdrDropStatsOpt82ValidationFailure_Type()
)
cdrDropStatsOpt82ValidationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsOpt82ValidationFailure.setStatus("current")
_CdrDropStatsMalformedPkts_Type = Counter32
_CdrDropStatsMalformedPkts_Object = MibTableColumn
cdrDropStatsMalformedPkts = _CdrDropStatsMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 11),
    _CdrDropStatsMalformedPkts_Type()
)
cdrDropStatsMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsMalformedPkts.setStatus("current")
_CdrDropStatsUntrustablePort_Type = Counter32
_CdrDropStatsUntrustablePort_Object = MibTableColumn
cdrDropStatsUntrustablePort = _CdrDropStatsUntrustablePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 12),
    _CdrDropStatsUntrustablePort_Type()
)
cdrDropStatsUntrustablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsUntrustablePort.setStatus("current")
_CdrDropStatsReqDroppedOnMCT_Type = Counter32
_CdrDropStatsReqDroppedOnMCT_Object = MibTableColumn
cdrDropStatsReqDroppedOnMCT = _CdrDropStatsReqDroppedOnMCT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 2, 1, 13),
    _CdrDropStatsReqDroppedOnMCT_Type()
)
cdrDropStatsReqDroppedOnMCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDropStatsReqDroppedOnMCT.setStatus("current")
_CdrIPv6StatsTable_Object = MibTable
cdrIPv6StatsTable = _CdrIPv6StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdrIPv6StatsTable.setStatus("current")
_CdrIPv6StatsEntry_Object = MibTableRow
cdrIPv6StatsEntry = _CdrIPv6StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 3, 1)
)
cdrIPv6StatsEntry.setIndexNames(
    (0, "CISCO-DHCP-RELAY-MIB", "cdrIPv6StatsIfIndex"),
    (0, "CISCO-DHCP-RELAY-MIB", "cdrIPv6StatsPktType"),
)
if mibBuilder.loadTexts:
    cdrIPv6StatsEntry.setStatus("current")
_CdrIPv6StatsIfIndex_Type = InterfaceIndexOrZero
_CdrIPv6StatsIfIndex_Object = MibTableColumn
cdrIPv6StatsIfIndex = _CdrIPv6StatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 3, 1, 1),
    _CdrIPv6StatsIfIndex_Type()
)
cdrIPv6StatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdrIPv6StatsIfIndex.setStatus("current")


class _CdrIPv6StatsPktType_Type(Integer32):
    """Custom type cdrIPv6StatsPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("solicit", 1),
          ("advertise", 2),
          ("request", 3),
          ("confirm", 4),
          ("renew", 5),
          ("rebind", 6),
          ("reply", 7),
          ("release", 8),
          ("decline", 9),
          ("reconfigure", 10),
          ("infoRequest", 11),
          ("relayForward", 12),
          ("relayReply", 13),
          ("unknown", 14))
    )


_CdrIPv6StatsPktType_Type.__name__ = "Integer32"
_CdrIPv6StatsPktType_Object = MibTableColumn
cdrIPv6StatsPktType = _CdrIPv6StatsPktType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 3, 1, 2),
    _CdrIPv6StatsPktType_Type()
)
cdrIPv6StatsPktType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdrIPv6StatsPktType.setStatus("current")
_CdrIPv6StatsPktsReceived_Type = Counter32
_CdrIPv6StatsPktsReceived_Object = MibTableColumn
cdrIPv6StatsPktsReceived = _CdrIPv6StatsPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 3, 1, 3),
    _CdrIPv6StatsPktsReceived_Type()
)
cdrIPv6StatsPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6StatsPktsReceived.setStatus("current")
_CdrIPv6StatsPktsForwarded_Type = Counter32
_CdrIPv6StatsPktsForwarded_Object = MibTableColumn
cdrIPv6StatsPktsForwarded = _CdrIPv6StatsPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 3, 1, 4),
    _CdrIPv6StatsPktsForwarded_Type()
)
cdrIPv6StatsPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6StatsPktsForwarded.setStatus("current")
_CdrIPv6StatsPktsDropped_Type = Counter32
_CdrIPv6StatsPktsDropped_Object = MibTableColumn
cdrIPv6StatsPktsDropped = _CdrIPv6StatsPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 3, 1, 5),
    _CdrIPv6StatsPktsDropped_Type()
)
cdrIPv6StatsPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6StatsPktsDropped.setStatus("current")
_CdrIPv6DropStatsTable_Object = MibTable
cdrIPv6DropStatsTable = _CdrIPv6DropStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdrIPv6DropStatsTable.setStatus("current")
_CdrIPv6DropStatsEntry_Object = MibTableRow
cdrIPv6DropStatsEntry = _CdrIPv6DropStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1)
)
cdrIPv6DropStatsEntry.setIndexNames(
    (0, "CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsIfIndex"),
)
if mibBuilder.loadTexts:
    cdrIPv6DropStatsEntry.setStatus("current")
_CdrIPv6DropStatsIfIndex_Type = InterfaceIndexOrZero
_CdrIPv6DropStatsIfIndex_Object = MibTableColumn
cdrIPv6DropStatsIfIndex = _CdrIPv6DropStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 1),
    _CdrIPv6DropStatsIfIndex_Type()
)
cdrIPv6DropStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsIfIndex.setStatus("current")
_CdrIPv6DropStatsRelayDisabled_Type = Counter32
_CdrIPv6DropStatsRelayDisabled_Object = MibTableColumn
cdrIPv6DropStatsRelayDisabled = _CdrIPv6DropStatsRelayDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 2),
    _CdrIPv6DropStatsRelayDisabled_Type()
)
cdrIPv6DropStatsRelayDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsRelayDisabled.setStatus("current")
_CdrIPv6DropStatsMaxHopsExceeded_Type = Counter32
_CdrIPv6DropStatsMaxHopsExceeded_Object = MibTableColumn
cdrIPv6DropStatsMaxHopsExceeded = _CdrIPv6DropStatsMaxHopsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 3),
    _CdrIPv6DropStatsMaxHopsExceeded_Type()
)
cdrIPv6DropStatsMaxHopsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsMaxHopsExceeded.setStatus("current")
_CdrIPv6DropStatsInvalidPkts_Type = Counter32
_CdrIPv6DropStatsInvalidPkts_Object = MibTableColumn
cdrIPv6DropStatsInvalidPkts = _CdrIPv6DropStatsInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 4),
    _CdrIPv6DropStatsInvalidPkts_Type()
)
cdrIPv6DropStatsInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsInvalidPkts.setStatus("current")
_CdrIPv6DropStatsUnknownOpInterface_Type = Counter32
_CdrIPv6DropStatsUnknownOpInterface_Object = MibTableColumn
cdrIPv6DropStatsUnknownOpInterface = _CdrIPv6DropStatsUnknownOpInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 5),
    _CdrIPv6DropStatsUnknownOpInterface_Type()
)
cdrIPv6DropStatsUnknownOpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsUnknownOpInterface.setStatus("current")
_CdrIPv6DropStatsInvalidVRF_Type = Counter32
_CdrIPv6DropStatsInvalidVRF_Object = MibTableColumn
cdrIPv6DropStatsInvalidVRF = _CdrIPv6DropStatsInvalidVRF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 6),
    _CdrIPv6DropStatsInvalidVRF_Type()
)
cdrIPv6DropStatsInvalidVRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsInvalidVRF.setStatus("current")
_CdrIPv6DropStatsOptionInsertionFailed_Type = Counter32
_CdrIPv6DropStatsOptionInsertionFailed_Object = MibTableColumn
cdrIPv6DropStatsOptionInsertionFailed = _CdrIPv6DropStatsOptionInsertionFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 7),
    _CdrIPv6DropStatsOptionInsertionFailed_Type()
)
cdrIPv6DropStatsOptionInsertionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsOptionInsertionFailed.setStatus("current")
_CdrIPv6DropStatsDirectReplyFromServer_Type = Counter32
_CdrIPv6DropStatsDirectReplyFromServer_Object = MibTableColumn
cdrIPv6DropStatsDirectReplyFromServer = _CdrIPv6DropStatsDirectReplyFromServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 8),
    _CdrIPv6DropStatsDirectReplyFromServer_Type()
)
cdrIPv6DropStatsDirectReplyFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsDirectReplyFromServer.setStatus("current")
_CdrIPv6DropStatsIPv6AddrNotConfigured_Type = Counter32
_CdrIPv6DropStatsIPv6AddrNotConfigured_Object = MibTableColumn
cdrIPv6DropStatsIPv6AddrNotConfigured = _CdrIPv6DropStatsIPv6AddrNotConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 9),
    _CdrIPv6DropStatsIPv6AddrNotConfigured_Type()
)
cdrIPv6DropStatsIPv6AddrNotConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsIPv6AddrNotConfigured.setStatus("current")
_CdrIPv6DropStatsInterfaceError_Type = Counter32
_CdrIPv6DropStatsInterfaceError_Object = MibTableColumn
cdrIPv6DropStatsInterfaceError = _CdrIPv6DropStatsInterfaceError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 10),
    _CdrIPv6DropStatsInterfaceError_Type()
)
cdrIPv6DropStatsInterfaceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsInterfaceError.setStatus("current")
_CdrIPv6DropStatsVpnOptionDisabled_Type = Counter32
_CdrIPv6DropStatsVpnOptionDisabled_Object = MibTableColumn
cdrIPv6DropStatsVpnOptionDisabled = _CdrIPv6DropStatsVpnOptionDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 11),
    _CdrIPv6DropStatsVpnOptionDisabled_Type()
)
cdrIPv6DropStatsVpnOptionDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsVpnOptionDisabled.setStatus("current")
_CdrIPv6DropStatsIpv6ExtnHeaderPresent_Type = Counter32
_CdrIPv6DropStatsIpv6ExtnHeaderPresent_Object = MibTableColumn
cdrIPv6DropStatsIpv6ExtnHeaderPresent = _CdrIPv6DropStatsIpv6ExtnHeaderPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 12),
    _CdrIPv6DropStatsIpv6ExtnHeaderPresent_Type()
)
cdrIPv6DropStatsIpv6ExtnHeaderPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsIpv6ExtnHeaderPresent.setStatus("current")
_CdrIPv6DropStatsReqDroppedOnMCT_Type = Counter32
_CdrIPv6DropStatsReqDroppedOnMCT_Object = MibTableColumn
cdrIPv6DropStatsReqDroppedOnMCT = _CdrIPv6DropStatsReqDroppedOnMCT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 1, 1, 4, 1, 13),
    _CdrIPv6DropStatsReqDroppedOnMCT_Type()
)
cdrIPv6DropStatsReqDroppedOnMCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrIPv6DropStatsReqDroppedOnMCT.setStatus("current")
_CiscoDhcpRelayMIBConform_ObjectIdentity = ObjectIdentity
ciscoDhcpRelayMIBConform = _CiscoDhcpRelayMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 2)
)
_CiscoDhcpRelayMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDhcpRelayMIBCompliances = _CiscoDhcpRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 2, 1)
)
_CiscoDhcpRelayMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDhcpRelayMIBGroups = _CiscoDhcpRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 2, 2)
)

# Managed Objects groups

cdrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 2, 2, 1)
)
cdrStatsGroup.setObjects(
      *(("CISCO-DHCP-RELAY-MIB", "cdrStatsPktsReceived"),
        ("CISCO-DHCP-RELAY-MIB", "cdrStatsPktsForwarded"),
        ("CISCO-DHCP-RELAY-MIB", "cdrStatsPktsDropped"))
)
if mibBuilder.loadTexts:
    cdrStatsGroup.setStatus("current")

cdrDropStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 2, 2, 2)
)
cdrDropStatsGroup.setObjects(
      *(("CISCO-DHCP-RELAY-MIB", "cdrDropStatsRelayNotEnabled"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsInvalidMsgType"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsInterfaceError"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsTxFailureServer"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsTxFailureClient"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsUnknownOpInterface"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsUnknownVrfOrInterface"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsMaxHopsExceeded"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsOpt82ValidationFailure"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsMalformedPkts"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsUntrustablePort"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsReqDroppedOnMCT"))
)
if mibBuilder.loadTexts:
    cdrDropStatsGroup.setStatus("current")

cdrIPv6StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 2, 2, 3)
)
cdrIPv6StatsGroup.setObjects(
      *(("CISCO-DHCP-RELAY-MIB", "cdrIPv6StatsPktsReceived"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6StatsPktsForwarded"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6StatsPktsDropped"))
)
if mibBuilder.loadTexts:
    cdrIPv6StatsGroup.setStatus("current")

cdrIPv6DropStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 2, 2, 4)
)
cdrIPv6DropStatsGroup.setObjects(
      *(("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsRelayDisabled"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsMaxHopsExceeded"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsInvalidPkts"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsUnknownOpInterface"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsInvalidVRF"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsOptionInsertionFailed"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsDirectReplyFromServer"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsInterfaceError"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsIPv6AddrNotConfigured"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsVpnOptionDisabled"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsIpv6ExtnHeaderPresent"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsReqDroppedOnMCT"))
)
if mibBuilder.loadTexts:
    cdrIPv6DropStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDhcpRelayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 833, 2, 1, 1)
)
ciscoDhcpRelayMIBCompliance.setObjects(
      *(("CISCO-DHCP-RELAY-MIB", "cdrStatsGroup"),
        ("CISCO-DHCP-RELAY-MIB", "cdrDropStatsGroup"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6StatsGroup"),
        ("CISCO-DHCP-RELAY-MIB", "cdrIPv6DropStatsGroup"))
)
if mibBuilder.loadTexts:
    ciscoDhcpRelayMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DHCP-RELAY-MIB",
    **{"ciscoDhcpRelayMIB": ciscoDhcpRelayMIB,
       "ciscoDhcpRelayMIBNotifs": ciscoDhcpRelayMIBNotifs,
       "ciscoDhcpRelayMIBObjects": ciscoDhcpRelayMIBObjects,
       "ciscoDhcpRelayStats": ciscoDhcpRelayStats,
       "cdrStatsTable": cdrStatsTable,
       "cdrStatsEntry": cdrStatsEntry,
       "cdrStatsIfIndex": cdrStatsIfIndex,
       "cdrStatsPktType": cdrStatsPktType,
       "cdrStatsPktsReceived": cdrStatsPktsReceived,
       "cdrStatsPktsForwarded": cdrStatsPktsForwarded,
       "cdrStatsPktsDropped": cdrStatsPktsDropped,
       "cdrDropStatsTable": cdrDropStatsTable,
       "cdrDropStatsEntry": cdrDropStatsEntry,
       "cdrDropStatsIfIndex": cdrDropStatsIfIndex,
       "cdrDropStatsRelayNotEnabled": cdrDropStatsRelayNotEnabled,
       "cdrDropStatsInvalidMsgType": cdrDropStatsInvalidMsgType,
       "cdrDropStatsInterfaceError": cdrDropStatsInterfaceError,
       "cdrDropStatsTxFailureServer": cdrDropStatsTxFailureServer,
       "cdrDropStatsTxFailureClient": cdrDropStatsTxFailureClient,
       "cdrDropStatsUnknownOpInterface": cdrDropStatsUnknownOpInterface,
       "cdrDropStatsUnknownVrfOrInterface": cdrDropStatsUnknownVrfOrInterface,
       "cdrDropStatsMaxHopsExceeded": cdrDropStatsMaxHopsExceeded,
       "cdrDropStatsOpt82ValidationFailure": cdrDropStatsOpt82ValidationFailure,
       "cdrDropStatsMalformedPkts": cdrDropStatsMalformedPkts,
       "cdrDropStatsUntrustablePort": cdrDropStatsUntrustablePort,
       "cdrDropStatsReqDroppedOnMCT": cdrDropStatsReqDroppedOnMCT,
       "cdrIPv6StatsTable": cdrIPv6StatsTable,
       "cdrIPv6StatsEntry": cdrIPv6StatsEntry,
       "cdrIPv6StatsIfIndex": cdrIPv6StatsIfIndex,
       "cdrIPv6StatsPktType": cdrIPv6StatsPktType,
       "cdrIPv6StatsPktsReceived": cdrIPv6StatsPktsReceived,
       "cdrIPv6StatsPktsForwarded": cdrIPv6StatsPktsForwarded,
       "cdrIPv6StatsPktsDropped": cdrIPv6StatsPktsDropped,
       "cdrIPv6DropStatsTable": cdrIPv6DropStatsTable,
       "cdrIPv6DropStatsEntry": cdrIPv6DropStatsEntry,
       "cdrIPv6DropStatsIfIndex": cdrIPv6DropStatsIfIndex,
       "cdrIPv6DropStatsRelayDisabled": cdrIPv6DropStatsRelayDisabled,
       "cdrIPv6DropStatsMaxHopsExceeded": cdrIPv6DropStatsMaxHopsExceeded,
       "cdrIPv6DropStatsInvalidPkts": cdrIPv6DropStatsInvalidPkts,
       "cdrIPv6DropStatsUnknownOpInterface": cdrIPv6DropStatsUnknownOpInterface,
       "cdrIPv6DropStatsInvalidVRF": cdrIPv6DropStatsInvalidVRF,
       "cdrIPv6DropStatsOptionInsertionFailed": cdrIPv6DropStatsOptionInsertionFailed,
       "cdrIPv6DropStatsDirectReplyFromServer": cdrIPv6DropStatsDirectReplyFromServer,
       "cdrIPv6DropStatsIPv6AddrNotConfigured": cdrIPv6DropStatsIPv6AddrNotConfigured,
       "cdrIPv6DropStatsInterfaceError": cdrIPv6DropStatsInterfaceError,
       "cdrIPv6DropStatsVpnOptionDisabled": cdrIPv6DropStatsVpnOptionDisabled,
       "cdrIPv6DropStatsIpv6ExtnHeaderPresent": cdrIPv6DropStatsIpv6ExtnHeaderPresent,
       "cdrIPv6DropStatsReqDroppedOnMCT": cdrIPv6DropStatsReqDroppedOnMCT,
       "ciscoDhcpRelayMIBConform": ciscoDhcpRelayMIBConform,
       "ciscoDhcpRelayMIBCompliances": ciscoDhcpRelayMIBCompliances,
       "ciscoDhcpRelayMIBCompliance": ciscoDhcpRelayMIBCompliance,
       "ciscoDhcpRelayMIBGroups": ciscoDhcpRelayMIBGroups,
       "cdrStatsGroup": cdrStatsGroup,
       "cdrDropStatsGroup": cdrDropStatsGroup,
       "cdrIPv6StatsGroup": cdrIPv6StatsGroup,
       "cdrIPv6DropStatsGroup": cdrIPv6DropStatsGroup}
)
