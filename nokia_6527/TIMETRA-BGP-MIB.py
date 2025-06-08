# SNMP MIB module (TIMETRA-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-BGP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:13 2025
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

(bgp4PathAttrIpAddrPrefix,
 bgp4PathAttrIpAddrPrefixLen,
 bgp4PathAttrPeer) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrIpAddrPrefix",
    "bgp4PathAttrIpAddrPrefixLen",
    "bgp4PathAttrPeer")

(InetAddress,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetAutonomousSystemNumber")

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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")

(TFilterLogId,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterLogId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(BgpConnectRetryTime,
 BgpHoldTime,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxBGPFamilyType,
 TmnxBgpAutonomousSystem,
 TmnxBgpLocalPreference,
 TmnxBgpPreference,
 TmnxCreateOrigin,
 TmnxEnabledDisabled,
 TmnxOperState,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "BgpConnectRetryTime",
    "BgpHoldTime",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxBGPFamilyType",
    "TmnxBgpAutonomousSystem",
    "TmnxBgpLocalPreference",
    "TmnxBgpPreference",
    "TmnxCreateOrigin",
    "TmnxEnabledDisabled",
    "TmnxOperState",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrID")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraBgpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 14)
)
if mibBuilder.loadTexts:
    timetraBgpMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-15 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-06-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BgpKeepAliveTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )



class BgpMinASOriginationTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )



class BgpLoopDetect(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("ignore", 2),
          ("off", 3),
          ("discardRoute", 4))
    )



class BgpMinRouteAdvertisement(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class BgpMEDSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igpCost", 1),
          ("metricVal", 2),
          ("noMedOut", 3))
    )



class BgpMEDValue(TextualConvention, Unsigned32):
    status = "current"


class BgpTimeToLive(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class BgpMultiPath(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class BgpPeerGroupName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class BgpPeerGroupNameOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class BgpPrefixLimit(TextualConvention, Unsigned32):
    status = "current"


class BgpPeerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noType", 1),
          ("internal", 2),
          ("external", 3))
    )



class BgpPeerState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )



class BgpPeerEvent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("start", 1),
          ("stop", 2),
          ("open", 3),
          ("close", 4),
          ("openFail", 5),
          ("error", 6),
          ("connectionRetry", 7),
          ("holdTime", 8),
          ("keepAlive", 9),
          ("receiveOpen", 10),
          ("receiveKeepAlive", 11),
          ("receiveUpdate", 12),
          ("receiveNotify", 13),
          ("startPassive", 14),
          ("parseError", 15),
          ("outOfMemory", 16),
          ("rtmLimitExceeded", 17),
          ("maxPrefixLimitExceeded", 18),
          ("maxPrefixLimitExceededLogged", 19),
          ("outOfProtectedNHIndex", 20),
          ("outOfNHIndex", 21),
          ("labelAllocFailed", 22),
          ("lspIdAllocFailed", 23),
          ("collisionResolution", 24),
          ("adminShutdown", 25),
          ("adminReset", 26),
          ("configChange", 27),
          ("peerTrackingPolicyMismatch", 28),
          ("receivedMalformedAttr", 29),
          ("adminResetHard", 30),
          ("peerDamping", 31))
    )



class BgpOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("disabled", 5))
    )



class TmnxIpFamily(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("unused", 0),
          ("ipv4", 1),
          ("vpnIpv4", 2),
          ("ipv6", 3),
          ("mcastIpv4", 4),
          ("vpnIpv6", 5),
          ("l2vpn", 6),
          ("mvpnIpv4", 7),
          ("mdtSafi", 8),
          ("mspw", 9),
          ("flowIpv4", 10),
          ("routeTarget", 11),
          ("mcastVpnIpv4", 12),
          ("mvpnIpv6", 13),
          ("flowIpv6", 14),
          ("evpn", 15),
          ("mcastIpv6", 16))
    )


class TmnxVpnCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("routeRefresh", 0),
          ("mpBGP", 1),
          ("orfExtendCommSend", 2),
          ("orfExtendCommRecv", 3),
          ("asn4Byte", 4))
    )


class TmnxAdvLabelAddressFamily(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("ipv6", 1),
          ("ipv4", 2))
    )


class TmnxAddPathAddressFamily(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("ipv4", 1),
          ("vpnIpv4", 2),
          ("ipv6", 3),
          ("vpnIpv6", 4))
    )


class TmnxAddPathSendLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16),
    )



class TmnxBgpFlowRouteExtCommAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("rateLimit", 1),
          ("sampleLog", 2),
          ("redirectToVrf", 3),
          ("nextEntry", 4),
          ("markDscp", 5),
          ("redirectToIp", 6),
          ("redirectToIf", 7))
    )



class TmnxIpNhChgFamily(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("labelIpv4", 0)
    )


class TmnxIpFamilyIdentifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("ipv4", 1),
          ("vpnIpv4", 2),
          ("ipv6", 3),
          ("mcastIpv4", 4),
          ("vpnIpv6", 5),
          ("l2vpn", 6),
          ("mvpnIpv4", 7),
          ("mdtSafi", 8),
          ("mspw", 9),
          ("flowIpv4", 10),
          ("routeTarget", 11),
          ("mcastVpnIpv4", 12),
          ("mvpnIpv6", 13),
          ("flowIpv6", 14),
          ("evpn", 15),
          ("mcastIpv6", 16))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxBgpConformance_ObjectIdentity = ObjectIdentity
tmnxBgpConformance = _TmnxBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14)
)
_TmnxBgpCompliances_ObjectIdentity = ObjectIdentity
tmnxBgpCompliances = _TmnxBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1)
)
_TmnxBgpGroups_ObjectIdentity = ObjectIdentity
tmnxBgpGroups = _TmnxBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2)
)
_TBgpObjects_ObjectIdentity = ObjectIdentity
tBgpObjects = _TBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14)
)
_TBgpGlobalObjects_ObjectIdentity = ObjectIdentity
tBgpGlobalObjects = _TBgpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 1)
)
_TBgpInstanceObjects_ObjectIdentity = ObjectIdentity
tBgpInstanceObjects = _TBgpInstanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2)
)
_TBgpInstanceTableLastChanged_Type = TimeStamp
_TBgpInstanceTableLastChanged_Object = MibScalar
tBgpInstanceTableLastChanged = _TBgpInstanceTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 1),
    _TBgpInstanceTableLastChanged_Type()
)
tBgpInstanceTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpInstanceTableLastChanged.setStatus("current")
_TBgpInstanceTable_Object = MibTable
tBgpInstanceTable = _TBgpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2)
)
if mibBuilder.loadTexts:
    tBgpInstanceTable.setStatus("current")
_TBgpInstanceEntry_Object = MibTableRow
tBgpInstanceEntry = _TBgpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1)
)
tBgpInstanceEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
)
if mibBuilder.loadTexts:
    tBgpInstanceEntry.setStatus("current")
_TBgpInstanceIndex_Type = TmnxVRtrID
_TBgpInstanceIndex_Object = MibTableColumn
tBgpInstanceIndex = _TBgpInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 1),
    _TBgpInstanceIndex_Type()
)
tBgpInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpInstanceIndex.setStatus("current")
_TBgpInstanceRowStatus_Type = RowStatus
_TBgpInstanceRowStatus_Object = MibTableColumn
tBgpInstanceRowStatus = _TBgpInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 2),
    _TBgpInstanceRowStatus_Type()
)
tBgpInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceRowStatus.setStatus("current")


class _TBgpInstanceShutdown_Type(TruthValue):
    """Custom type tBgpInstanceShutdown based on TruthValue"""
    defaultValue = 2


_TBgpInstanceShutdown_Type.__name__ = "TruthValue"
_TBgpInstanceShutdown_Object = MibTableColumn
tBgpInstanceShutdown = _TBgpInstanceShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 3),
    _TBgpInstanceShutdown_Type()
)
tBgpInstanceShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceShutdown.setStatus("current")


class _TBgpInstanceDescription_Type(DisplayString):
    """Custom type tBgpInstanceDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TBgpInstanceDescription_Type.__name__ = "DisplayString"
_TBgpInstanceDescription_Object = MibTableColumn
tBgpInstanceDescription = _TBgpInstanceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 4),
    _TBgpInstanceDescription_Type()
)
tBgpInstanceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDescription.setStatus("current")


class _TBgpInstanceAlwaysCompareMED_Type(Integer32):
    """Custom type tBgpInstanceAlwaysCompareMED based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("zero", 2),
          ("infinity", 3),
          ("on", 4))
    )


_TBgpInstanceAlwaysCompareMED_Type.__name__ = "Integer32"
_TBgpInstanceAlwaysCompareMED_Object = MibTableColumn
tBgpInstanceAlwaysCompareMED = _TBgpInstanceAlwaysCompareMED_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 5),
    _TBgpInstanceAlwaysCompareMED_Type()
)
tBgpInstanceAlwaysCompareMED.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceAlwaysCompareMED.setStatus("current")


class _TBgpInstanceAsPathIgnore_Type(TruthValue):
    """Custom type tBgpInstanceAsPathIgnore based on TruthValue"""
    defaultValue = 2


_TBgpInstanceAsPathIgnore_Type.__name__ = "TruthValue"
_TBgpInstanceAsPathIgnore_Object = MibTableColumn
tBgpInstanceAsPathIgnore = _TBgpInstanceAsPathIgnore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 6),
    _TBgpInstanceAsPathIgnore_Type()
)
tBgpInstanceAsPathIgnore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceAsPathIgnore.setStatus("obsolete")


class _TBgpInstanceBgpId_Type(IpAddress):
    """Custom type tBgpInstanceBgpId based on IpAddress"""
    defaultHexValue = "00000000"


_TBgpInstanceBgpId_Type.__name__ = "IpAddress"
_TBgpInstanceBgpId_Object = MibTableColumn
tBgpInstanceBgpId = _TBgpInstanceBgpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 7),
    _TBgpInstanceBgpId_Type()
)
tBgpInstanceBgpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceBgpId.setStatus("current")


class _TBgpInstanceConnectRetry_Type(BgpConnectRetryTime):
    """Custom type tBgpInstanceConnectRetry based on BgpConnectRetryTime"""
    defaultValue = 120


_TBgpInstanceConnectRetry_Type.__name__ = "BgpConnectRetryTime"
_TBgpInstanceConnectRetry_Object = MibTableColumn
tBgpInstanceConnectRetry = _TBgpInstanceConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 8),
    _TBgpInstanceConnectRetry_Type()
)
tBgpInstanceConnectRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceConnectRetry.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceConnectRetry.setUnits("seconds")


class _TBgpInstanceHoldTime_Type(BgpHoldTime):
    """Custom type tBgpInstanceHoldTime based on BgpHoldTime"""
    defaultValue = 90


_TBgpInstanceHoldTime_Type.__name__ = "BgpHoldTime"
_TBgpInstanceHoldTime_Object = MibTableColumn
tBgpInstanceHoldTime = _TBgpInstanceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 9),
    _TBgpInstanceHoldTime_Type()
)
tBgpInstanceHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceHoldTime.setUnits("seconds")


class _TBgpInstanceKeepAlive_Type(BgpKeepAliveTime):
    """Custom type tBgpInstanceKeepAlive based on BgpKeepAliveTime"""
    defaultValue = 30


_TBgpInstanceKeepAlive_Type.__name__ = "BgpKeepAliveTime"
_TBgpInstanceKeepAlive_Object = MibTableColumn
tBgpInstanceKeepAlive = _TBgpInstanceKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 10),
    _TBgpInstanceKeepAlive_Type()
)
tBgpInstanceKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceKeepAlive.setUnits("seconds")


class _TBgpInstanceMinASOrigination_Type(BgpMinASOriginationTime):
    """Custom type tBgpInstanceMinASOrigination based on BgpMinASOriginationTime"""
    defaultValue = 15


_TBgpInstanceMinASOrigination_Type.__name__ = "BgpMinASOriginationTime"
_TBgpInstanceMinASOrigination_Object = MibTableColumn
tBgpInstanceMinASOrigination = _TBgpInstanceMinASOrigination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 11),
    _TBgpInstanceMinASOrigination_Type()
)
tBgpInstanceMinASOrigination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMinASOrigination.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpInstanceMinASOrigination.setUnits("seconds")


class _TBgpInstanceDampening_Type(TruthValue):
    """Custom type tBgpInstanceDampening based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDampening_Type.__name__ = "TruthValue"
_TBgpInstanceDampening_Object = MibTableColumn
tBgpInstanceDampening = _TBgpInstanceDampening_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 12),
    _TBgpInstanceDampening_Type()
)
tBgpInstanceDampening.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDampening.setStatus("current")


class _TBgpInstanceLocalAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tBgpInstanceLocalAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TBgpInstanceLocalAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TBgpInstanceLocalAS_Object = MibTableColumn
tBgpInstanceLocalAS = _TBgpInstanceLocalAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 13),
    _TBgpInstanceLocalAS_Type()
)
tBgpInstanceLocalAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceLocalAS.setStatus("obsolete")


class _TBgpInstanceLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tBgpInstanceLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 100


_TBgpInstanceLocalPreference_Type.__name__ = "TmnxBgpLocalPreference"
_TBgpInstanceLocalPreference_Object = MibTableColumn
tBgpInstanceLocalPreference = _TBgpInstanceLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 14),
    _TBgpInstanceLocalPreference_Type()
)
tBgpInstanceLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceLocalPreference.setStatus("current")


class _TBgpInstanceLoopDetect_Type(BgpLoopDetect):
    """Custom type tBgpInstanceLoopDetect based on BgpLoopDetect"""
    defaultValue = 2


_TBgpInstanceLoopDetect_Type.__name__ = "BgpLoopDetect"
_TBgpInstanceLoopDetect_Object = MibTableColumn
tBgpInstanceLoopDetect = _TBgpInstanceLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 15),
    _TBgpInstanceLoopDetect_Type()
)
tBgpInstanceLoopDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceLoopDetect.setStatus("current")


class _TBgpInstanceMinRouteAdvertisement_Type(BgpMinRouteAdvertisement):
    """Custom type tBgpInstanceMinRouteAdvertisement based on BgpMinRouteAdvertisement"""
    defaultValue = 30


_TBgpInstanceMinRouteAdvertisement_Type.__name__ = "BgpMinRouteAdvertisement"
_TBgpInstanceMinRouteAdvertisement_Object = MibTableColumn
tBgpInstanceMinRouteAdvertisement = _TBgpInstanceMinRouteAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 16),
    _TBgpInstanceMinRouteAdvertisement_Type()
)
tBgpInstanceMinRouteAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMinRouteAdvertisement.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceMinRouteAdvertisement.setUnits("seconds")


class _TBgpInstanceMultipath_Type(BgpMultiPath):
    """Custom type tBgpInstanceMultipath based on BgpMultiPath"""
    defaultValue = 1


_TBgpInstanceMultipath_Type.__name__ = "BgpMultiPath"
_TBgpInstanceMultipath_Object = MibTableColumn
tBgpInstanceMultipath = _TBgpInstanceMultipath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 17),
    _TBgpInstanceMultipath_Type()
)
tBgpInstanceMultipath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMultipath.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceMultipath.setUnits("number-of-hops")


class _TBgpInstanceNoAggregatorID_Type(TruthValue):
    """Custom type tBgpInstanceNoAggregatorID based on TruthValue"""
    defaultValue = 2


_TBgpInstanceNoAggregatorID_Type.__name__ = "TruthValue"
_TBgpInstanceNoAggregatorID_Object = MibTableColumn
tBgpInstanceNoAggregatorID = _TBgpInstanceNoAggregatorID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 18),
    _TBgpInstanceNoAggregatorID_Type()
)
tBgpInstanceNoAggregatorID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceNoAggregatorID.setStatus("current")


class _TBgpInstancePreference_Type(TmnxBgpPreference):
    """Custom type tBgpInstancePreference based on TmnxBgpPreference"""
    defaultValue = 170

    subtypeSpec = TmnxBgpPreference.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TBgpInstancePreference_Type.__name__ = "TmnxBgpPreference"
_TBgpInstancePreference_Object = MibTableColumn
tBgpInstancePreference = _TBgpInstancePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 19),
    _TBgpInstancePreference_Type()
)
tBgpInstancePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePreference.setStatus("current")


class _TBgpInstanceRemovePrivateAS_Type(TruthValue):
    """Custom type tBgpInstanceRemovePrivateAS based on TruthValue"""
    defaultValue = 2


_TBgpInstanceRemovePrivateAS_Type.__name__ = "TruthValue"
_TBgpInstanceRemovePrivateAS_Object = MibTableColumn
tBgpInstanceRemovePrivateAS = _TBgpInstanceRemovePrivateAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 20),
    _TBgpInstanceRemovePrivateAS_Type()
)
tBgpInstanceRemovePrivateAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceRemovePrivateAS.setStatus("current")
_TBgpInstanceLastChanged_Type = TimeStamp
_TBgpInstanceLastChanged_Object = MibTableColumn
tBgpInstanceLastChanged = _TBgpInstanceLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 21),
    _TBgpInstanceLastChanged_Type()
)
tBgpInstanceLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpInstanceLastChanged.setStatus("current")


class _TBgpInstanceMultihop_Type(BgpTimeToLive):
    """Custom type tBgpInstanceMultihop based on BgpTimeToLive"""
    defaultValue = 0


_TBgpInstanceMultihop_Type.__name__ = "BgpTimeToLive"
_TBgpInstanceMultihop_Object = MibTableColumn
tBgpInstanceMultihop = _TBgpInstanceMultihop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 22),
    _TBgpInstanceMultihop_Type()
)
tBgpInstanceMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMultihop.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceMultihop.setUnits("TTL hops")


class _TBgpInstanceMEDSource_Type(BgpMEDSource):
    """Custom type tBgpInstanceMEDSource based on BgpMEDSource"""
    defaultValue = 3


_TBgpInstanceMEDSource_Type.__name__ = "BgpMEDSource"
_TBgpInstanceMEDSource_Object = MibTableColumn
tBgpInstanceMEDSource = _TBgpInstanceMEDSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 23),
    _TBgpInstanceMEDSource_Type()
)
tBgpInstanceMEDSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMEDSource.setStatus("current")


class _TBgpInstanceMEDValue_Type(BgpMEDValue):
    """Custom type tBgpInstanceMEDValue based on BgpMEDValue"""
    defaultValue = 0


_TBgpInstanceMEDValue_Type.__name__ = "BgpMEDValue"
_TBgpInstanceMEDValue_Object = MibTableColumn
tBgpInstanceMEDValue = _TBgpInstanceMEDValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 24),
    _TBgpInstanceMEDValue_Type()
)
tBgpInstanceMEDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMEDValue.setStatus("current")
_TBgpInstanceConfederationAS_Type = TmnxBgpAutonomousSystem
_TBgpInstanceConfederationAS_Object = MibTableColumn
tBgpInstanceConfederationAS = _TBgpInstanceConfederationAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 25),
    _TBgpInstanceConfederationAS_Type()
)
tBgpInstanceConfederationAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpInstanceConfederationAS.setStatus("obsolete")


class _TBgpInstanceImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceImportPolicy1_Object = MibTableColumn
tBgpInstanceImportPolicy1 = _TBgpInstanceImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 30),
    _TBgpInstanceImportPolicy1_Type()
)
tBgpInstanceImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceImportPolicy1.setStatus("obsolete")


class _TBgpInstanceImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceImportPolicy2_Object = MibTableColumn
tBgpInstanceImportPolicy2 = _TBgpInstanceImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 31),
    _TBgpInstanceImportPolicy2_Type()
)
tBgpInstanceImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceImportPolicy2.setStatus("obsolete")


class _TBgpInstanceImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceImportPolicy3_Object = MibTableColumn
tBgpInstanceImportPolicy3 = _TBgpInstanceImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 32),
    _TBgpInstanceImportPolicy3_Type()
)
tBgpInstanceImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceImportPolicy3.setStatus("obsolete")


class _TBgpInstanceImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceImportPolicy4_Object = MibTableColumn
tBgpInstanceImportPolicy4 = _TBgpInstanceImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 33),
    _TBgpInstanceImportPolicy4_Type()
)
tBgpInstanceImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceImportPolicy4.setStatus("obsolete")


class _TBgpInstanceImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceImportPolicy5_Object = MibTableColumn
tBgpInstanceImportPolicy5 = _TBgpInstanceImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 34),
    _TBgpInstanceImportPolicy5_Type()
)
tBgpInstanceImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceImportPolicy5.setStatus("obsolete")


class _TBgpInstanceExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceExportPolicy1_Object = MibTableColumn
tBgpInstanceExportPolicy1 = _TBgpInstanceExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 35),
    _TBgpInstanceExportPolicy1_Type()
)
tBgpInstanceExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceExportPolicy1.setStatus("obsolete")


class _TBgpInstanceExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceExportPolicy2_Object = MibTableColumn
tBgpInstanceExportPolicy2 = _TBgpInstanceExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 36),
    _TBgpInstanceExportPolicy2_Type()
)
tBgpInstanceExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceExportPolicy2.setStatus("obsolete")


class _TBgpInstanceExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceExportPolicy3_Object = MibTableColumn
tBgpInstanceExportPolicy3 = _TBgpInstanceExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 37),
    _TBgpInstanceExportPolicy3_Type()
)
tBgpInstanceExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceExportPolicy3.setStatus("obsolete")


class _TBgpInstanceExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceExportPolicy4_Object = MibTableColumn
tBgpInstanceExportPolicy4 = _TBgpInstanceExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 38),
    _TBgpInstanceExportPolicy4_Type()
)
tBgpInstanceExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceExportPolicy4.setStatus("obsolete")


class _TBgpInstanceExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceExportPolicy5_Object = MibTableColumn
tBgpInstanceExportPolicy5 = _TBgpInstanceExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 39),
    _TBgpInstanceExportPolicy5_Type()
)
tBgpInstanceExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceExportPolicy5.setStatus("obsolete")
_TBgpInstanceOperStatus_Type = BgpOperState
_TBgpInstanceOperStatus_Object = MibTableColumn
tBgpInstanceOperStatus = _TBgpInstanceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 40),
    _TBgpInstanceOperStatus_Type()
)
tBgpInstanceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpInstanceOperStatus.setStatus("current")


class _TBgpInstanceLocalASPrivate_Type(TruthValue):
    """Custom type tBgpInstanceLocalASPrivate based on TruthValue"""
    defaultValue = 2


_TBgpInstanceLocalASPrivate_Type.__name__ = "TruthValue"
_TBgpInstanceLocalASPrivate_Object = MibTableColumn
tBgpInstanceLocalASPrivate = _TBgpInstanceLocalASPrivate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 41),
    _TBgpInstanceLocalASPrivate_Type()
)
tBgpInstanceLocalASPrivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceLocalASPrivate.setStatus("current")


class _TBgpInstanceMd5Auth_Type(TruthValue):
    """Custom type tBgpInstanceMd5Auth based on TruthValue"""
    defaultValue = 2


_TBgpInstanceMd5Auth_Type.__name__ = "TruthValue"
_TBgpInstanceMd5Auth_Object = MibTableColumn
tBgpInstanceMd5Auth = _TBgpInstanceMd5Auth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 42),
    _TBgpInstanceMd5Auth_Type()
)
tBgpInstanceMd5Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMd5Auth.setStatus("current")


class _TBgpInstanceMd5AuthKey_Type(OctetString):
    """Custom type tBgpInstanceMd5AuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgpInstanceMd5AuthKey_Type.__name__ = "OctetString"
_TBgpInstanceMd5AuthKey_Object = MibTableColumn
tBgpInstanceMd5AuthKey = _TBgpInstanceMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 43),
    _TBgpInstanceMd5AuthKey_Type()
)
tBgpInstanceMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMd5AuthKey.setStatus("current")


class _TBgpInstanceClusterId_Type(IpAddress):
    """Custom type tBgpInstanceClusterId based on IpAddress"""
    defaultHexValue = "00000000"


_TBgpInstanceClusterId_Type.__name__ = "IpAddress"
_TBgpInstanceClusterId_Object = MibTableColumn
tBgpInstanceClusterId = _TBgpInstanceClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 44),
    _TBgpInstanceClusterId_Type()
)
tBgpInstanceClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceClusterId.setStatus("current")


class _TBgpInstanceDisableClientReflect_Type(TruthValue):
    """Custom type tBgpInstanceDisableClientReflect based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDisableClientReflect_Type.__name__ = "TruthValue"
_TBgpInstanceDisableClientReflect_Object = MibTableColumn
tBgpInstanceDisableClientReflect = _TBgpInstanceDisableClientReflect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 45),
    _TBgpInstanceDisableClientReflect_Type()
)
tBgpInstanceDisableClientReflect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDisableClientReflect.setStatus("current")


class _TBgpInstanceIBgpMultipath_Type(TruthValue):
    """Custom type tBgpInstanceIBgpMultipath based on TruthValue"""
    defaultValue = 2


_TBgpInstanceIBgpMultipath_Type.__name__ = "TruthValue"
_TBgpInstanceIBgpMultipath_Object = MibTableColumn
tBgpInstanceIBgpMultipath = _TBgpInstanceIBgpMultipath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 46),
    _TBgpInstanceIBgpMultipath_Type()
)
tBgpInstanceIBgpMultipath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceIBgpMultipath.setStatus("current")


class _TBgpInstanceFamily_Type(TmnxIpFamily):
    """Custom type tBgpInstanceFamily based on TmnxIpFamily"""
    defaultBinValue = "01"


_TBgpInstanceFamily_Type.__name__ = "TmnxIpFamily"
_TBgpInstanceFamily_Object = MibTableColumn
tBgpInstanceFamily = _TBgpInstanceFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 47),
    _TBgpInstanceFamily_Type()
)
tBgpInstanceFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceFamily.setStatus("current")


class _TBgpInstanceGracefulRestart_Type(TruthValue):
    """Custom type tBgpInstanceGracefulRestart based on TruthValue"""
    defaultValue = 2


_TBgpInstanceGracefulRestart_Type.__name__ = "TruthValue"
_TBgpInstanceGracefulRestart_Object = MibTableColumn
tBgpInstanceGracefulRestart = _TBgpInstanceGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 48),
    _TBgpInstanceGracefulRestart_Type()
)
tBgpInstanceGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceGracefulRestart.setStatus("current")


class _TBgpInstanceGRPathSelectDefer_Type(Unsigned32):
    """Custom type tBgpInstanceGRPathSelectDefer based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TBgpInstanceGRPathSelectDefer_Type.__name__ = "Unsigned32"
_TBgpInstanceGRPathSelectDefer_Object = MibTableColumn
tBgpInstanceGRPathSelectDefer = _TBgpInstanceGRPathSelectDefer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 49),
    _TBgpInstanceGRPathSelectDefer_Type()
)
tBgpInstanceGRPathSelectDefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceGRPathSelectDefer.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceGRPathSelectDefer.setUnits("seconds")


class _TBgpInstanceGRRestartTime_Type(Unsigned32):
    """Custom type tBgpInstanceGRRestartTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TBgpInstanceGRRestartTime_Type.__name__ = "Unsigned32"
_TBgpInstanceGRRestartTime_Object = MibTableColumn
tBgpInstanceGRRestartTime = _TBgpInstanceGRRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 50),
    _TBgpInstanceGRRestartTime_Type()
)
tBgpInstanceGRRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceGRRestartTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceGRRestartTime.setUnits("seconds")


class _TBgpInstanceGRStaleRoute_Type(Unsigned32):
    """Custom type tBgpInstanceGRStaleRoute based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TBgpInstanceGRStaleRoute_Type.__name__ = "Unsigned32"
_TBgpInstanceGRStaleRoute_Object = MibTableColumn
tBgpInstanceGRStaleRoute = _TBgpInstanceGRStaleRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 51),
    _TBgpInstanceGRStaleRoute_Type()
)
tBgpInstanceGRStaleRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceGRStaleRoute.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstanceGRStaleRoute.setUnits("seconds")


class _TBgpInstanceGRAdminState_Type(TmnxAdminState):
    """Custom type tBgpInstanceGRAdminState based on TmnxAdminState"""
    defaultValue = 2


_TBgpInstanceGRAdminState_Type.__name__ = "TmnxAdminState"
_TBgpInstanceGRAdminState_Object = MibTableColumn
tBgpInstanceGRAdminState = _TBgpInstanceGRAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 52),
    _TBgpInstanceGRAdminState_Type()
)
tBgpInstanceGRAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceGRAdminState.setStatus("current")
_TBgpInstanceGROperState_Type = TmnxOperState
_TBgpInstanceGROperState_Object = MibTableColumn
tBgpInstanceGROperState = _TBgpInstanceGROperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 53),
    _TBgpInstanceGROperState_Type()
)
tBgpInstanceGROperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpInstanceGROperState.setStatus("current")


class _TBgpInstanceVpnApplyImport_Type(TruthValue):
    """Custom type tBgpInstanceVpnApplyImport based on TruthValue"""
    defaultValue = 2


_TBgpInstanceVpnApplyImport_Type.__name__ = "TruthValue"
_TBgpInstanceVpnApplyImport_Object = MibTableColumn
tBgpInstanceVpnApplyImport = _TBgpInstanceVpnApplyImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 54),
    _TBgpInstanceVpnApplyImport_Type()
)
tBgpInstanceVpnApplyImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceVpnApplyImport.setStatus("current")


class _TBgpInstanceVpnApplyExport_Type(TruthValue):
    """Custom type tBgpInstanceVpnApplyExport based on TruthValue"""
    defaultValue = 2


_TBgpInstanceVpnApplyExport_Type.__name__ = "TruthValue"
_TBgpInstanceVpnApplyExport_Object = MibTableColumn
tBgpInstanceVpnApplyExport = _TBgpInstanceVpnApplyExport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 55),
    _TBgpInstanceVpnApplyExport_Type()
)
tBgpInstanceVpnApplyExport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceVpnApplyExport.setStatus("current")


class _TBgpInstanceIgpShortcut_Type(Bits):
    """Custom type tBgpInstanceIgpShortcut based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("te", 0),
          ("ldp", 1),
          ("ip", 2),
          ("mpls", 3),
          ("mpls-bgp", 4))
    )

_TBgpInstanceIgpShortcut_Type.__name__ = "Bits"
_TBgpInstanceIgpShortcut_Object = MibTableColumn
tBgpInstanceIgpShortcut = _TBgpInstanceIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 56),
    _TBgpInstanceIgpShortcut_Type()
)
tBgpInstanceIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceIgpShortcut.setStatus("current")


class _TBgpInstanceDisallowIgp_Type(TruthValue):
    """Custom type tBgpInstanceDisallowIgp based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDisallowIgp_Type.__name__ = "TruthValue"
_TBgpInstanceDisallowIgp_Object = MibTableColumn
tBgpInstanceDisallowIgp = _TBgpInstanceDisallowIgp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 57),
    _TBgpInstanceDisallowIgp_Type()
)
tBgpInstanceDisallowIgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDisallowIgp.setStatus("current")


class _TBgpInstanceOrf_Type(TruthValue):
    """Custom type tBgpInstanceOrf based on TruthValue"""
    defaultValue = 2


_TBgpInstanceOrf_Type.__name__ = "TruthValue"
_TBgpInstanceOrf_Object = MibTableColumn
tBgpInstanceOrf = _TBgpInstanceOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 58),
    _TBgpInstanceOrf_Type()
)
tBgpInstanceOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceOrf.setStatus("current")


class _TBgpInstanceExtCommsOrf_Type(TruthValue):
    """Custom type tBgpInstanceExtCommsOrf based on TruthValue"""
    defaultValue = 2


_TBgpInstanceExtCommsOrf_Type.__name__ = "TruthValue"
_TBgpInstanceExtCommsOrf_Object = MibTableColumn
tBgpInstanceExtCommsOrf = _TBgpInstanceExtCommsOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 59),
    _TBgpInstanceExtCommsOrf_Type()
)
tBgpInstanceExtCommsOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceExtCommsOrf.setStatus("current")


class _TBgpInstanceExtCommsSendOrf_Type(TruthValue):
    """Custom type tBgpInstanceExtCommsSendOrf based on TruthValue"""
    defaultValue = 2


_TBgpInstanceExtCommsSendOrf_Type.__name__ = "TruthValue"
_TBgpInstanceExtCommsSendOrf_Object = MibTableColumn
tBgpInstanceExtCommsSendOrf = _TBgpInstanceExtCommsSendOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 60),
    _TBgpInstanceExtCommsSendOrf_Type()
)
tBgpInstanceExtCommsSendOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceExtCommsSendOrf.setStatus("current")


class _TBgpInstanceExtCommsRecvOrf_Type(TruthValue):
    """Custom type tBgpInstanceExtCommsRecvOrf based on TruthValue"""
    defaultValue = 2


_TBgpInstanceExtCommsRecvOrf_Type.__name__ = "TruthValue"
_TBgpInstanceExtCommsRecvOrf_Object = MibTableColumn
tBgpInstanceExtCommsRecvOrf = _TBgpInstanceExtCommsRecvOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 61),
    _TBgpInstanceExtCommsRecvOrf_Type()
)
tBgpInstanceExtCommsRecvOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceExtCommsRecvOrf.setStatus("current")


class _TBgpInstanceAllowInterAsVpn_Type(TruthValue):
    """Custom type tBgpInstanceAllowInterAsVpn based on TruthValue"""
    defaultValue = 2


_TBgpInstanceAllowInterAsVpn_Type.__name__ = "TruthValue"
_TBgpInstanceAllowInterAsVpn_Object = MibTableColumn
tBgpInstanceAllowInterAsVpn = _TBgpInstanceAllowInterAsVpn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 62),
    _TBgpInstanceAllowInterAsVpn_Type()
)
tBgpInstanceAllowInterAsVpn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceAllowInterAsVpn.setStatus("current")


class _TBgpInstancePurgeTimer_Type(Unsigned32):
    """Custom type tBgpInstancePurgeTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TBgpInstancePurgeTimer_Type.__name__ = "Unsigned32"
_TBgpInstancePurgeTimer_Object = MibTableColumn
tBgpInstancePurgeTimer = _TBgpInstancePurgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 63),
    _TBgpInstancePurgeTimer_Type()
)
tBgpInstancePurgeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePurgeTimer.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstancePurgeTimer.setUnits("minutes")


class _TBgpInstanceLocalAS4Byte_Type(InetAutonomousSystemNumber):
    """Custom type tBgpInstanceLocalAS4Byte based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TBgpInstanceLocalAS4Byte_Type.__name__ = "InetAutonomousSystemNumber"
_TBgpInstanceLocalAS4Byte_Object = MibTableColumn
tBgpInstanceLocalAS4Byte = _TBgpInstanceLocalAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 64),
    _TBgpInstanceLocalAS4Byte_Type()
)
tBgpInstanceLocalAS4Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceLocalAS4Byte.setStatus("current")
_TBgpInstanceConfederationAS4Byte_Type = InetAutonomousSystemNumber
_TBgpInstanceConfederationAS4Byte_Object = MibTableColumn
tBgpInstanceConfederationAS4Byte = _TBgpInstanceConfederationAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 65),
    _TBgpInstanceConfederationAS4Byte_Type()
)
tBgpInstanceConfederationAS4Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpInstanceConfederationAS4Byte.setStatus("current")


class _TBgpInstanceDisable4ByteASN_Type(TruthValue):
    """Custom type tBgpInstanceDisable4ByteASN based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDisable4ByteASN_Type.__name__ = "TruthValue"
_TBgpInstanceDisable4ByteASN_Object = MibTableColumn
tBgpInstanceDisable4ByteASN = _TBgpInstanceDisable4ByteASN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 66),
    _TBgpInstanceDisable4ByteASN_Type()
)
tBgpInstanceDisable4ByteASN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDisable4ByteASN.setStatus("current")


class _TBgpInstanceMultipathEiBgpState_Type(TmnxEnabledDisabled):
    """Custom type tBgpInstanceMultipathEiBgpState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TBgpInstanceMultipathEiBgpState_Type.__name__ = "TmnxEnabledDisabled"
_TBgpInstanceMultipathEiBgpState_Object = MibTableColumn
tBgpInstanceMultipathEiBgpState = _TBgpInstanceMultipathEiBgpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 67),
    _TBgpInstanceMultipathEiBgpState_Type()
)
tBgpInstanceMultipathEiBgpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMultipathEiBgpState.setStatus("current")


class _TBgpInstanceHoldTimeIsStrict_Type(TruthValue):
    """Custom type tBgpInstanceHoldTimeIsStrict based on TruthValue"""
    defaultValue = 2


_TBgpInstanceHoldTimeIsStrict_Type.__name__ = "TruthValue"
_TBgpInstanceHoldTimeIsStrict_Object = MibTableColumn
tBgpInstanceHoldTimeIsStrict = _TBgpInstanceHoldTimeIsStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 68),
    _TBgpInstanceHoldTimeIsStrict_Type()
)
tBgpInstanceHoldTimeIsStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceHoldTimeIsStrict.setStatus("obsolete")


class _TBgpInstanceAsPathIgnoreFamily_Type(TmnxIpFamily):
    """Custom type tBgpInstanceAsPathIgnoreFamily based on TmnxIpFamily"""
    defaultBinValue = "0"


_TBgpInstanceAsPathIgnoreFamily_Type.__name__ = "TmnxIpFamily"
_TBgpInstanceAsPathIgnoreFamily_Object = MibTableColumn
tBgpInstanceAsPathIgnoreFamily = _TBgpInstanceAsPathIgnoreFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 69),
    _TBgpInstanceAsPathIgnoreFamily_Type()
)
tBgpInstanceAsPathIgnoreFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceAsPathIgnoreFamily.setStatus("current")


class _TBgpInstanceRemovePrivateASLmtd_Type(TruthValue):
    """Custom type tBgpInstanceRemovePrivateASLmtd based on TruthValue"""
    defaultValue = 2


_TBgpInstanceRemovePrivateASLmtd_Type.__name__ = "TruthValue"
_TBgpInstanceRemovePrivateASLmtd_Object = MibTableColumn
tBgpInstanceRemovePrivateASLmtd = _TBgpInstanceRemovePrivateASLmtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 70),
    _TBgpInstanceRemovePrivateASLmtd_Type()
)
tBgpInstanceRemovePrivateASLmtd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceRemovePrivateASLmtd.setStatus("current")


class _TBgpInstancePMTUDiscovery_Type(TruthValue):
    """Custom type tBgpInstancePMTUDiscovery based on TruthValue"""
    defaultValue = 2


_TBgpInstancePMTUDiscovery_Type.__name__ = "TruthValue"
_TBgpInstancePMTUDiscovery_Object = MibTableColumn
tBgpInstancePMTUDiscovery = _TBgpInstancePMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 71),
    _TBgpInstancePMTUDiscovery_Type()
)
tBgpInstancePMTUDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePMTUDiscovery.setStatus("current")


class _TBgpInstanceDisableRtTblInstall_Type(TruthValue):
    """Custom type tBgpInstanceDisableRtTblInstall based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDisableRtTblInstall_Type.__name__ = "TruthValue"
_TBgpInstanceDisableRtTblInstall_Object = MibTableColumn
tBgpInstanceDisableRtTblInstall = _TBgpInstanceDisableRtTblInstall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 72),
    _TBgpInstanceDisableRtTblInstall_Type()
)
tBgpInstanceDisableRtTblInstall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDisableRtTblInstall.setStatus("current")


class _TBgpInstanceNHResUseBgpRoutes_Type(TruthValue):
    """Custom type tBgpInstanceNHResUseBgpRoutes based on TruthValue"""
    defaultValue = 2


_TBgpInstanceNHResUseBgpRoutes_Type.__name__ = "TruthValue"
_TBgpInstanceNHResUseBgpRoutes_Object = MibTableColumn
tBgpInstanceNHResUseBgpRoutes = _TBgpInstanceNHResUseBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 73),
    _TBgpInstanceNHResUseBgpRoutes_Type()
)
tBgpInstanceNHResUseBgpRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceNHResUseBgpRoutes.setStatus("current")


class _TBgpInstanceEnableRRVpnFwding_Type(TruthValue):
    """Custom type tBgpInstanceEnableRRVpnFwding based on TruthValue"""
    defaultValue = 2


_TBgpInstanceEnableRRVpnFwding_Type.__name__ = "TruthValue"
_TBgpInstanceEnableRRVpnFwding_Object = MibTableColumn
tBgpInstanceEnableRRVpnFwding = _TBgpInstanceEnableRRVpnFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 2, 1, 74),
    _TBgpInstanceEnableRRVpnFwding_Type()
)
tBgpInstanceEnableRRVpnFwding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceEnableRRVpnFwding.setStatus("current")
_TBgpInstRteTargetTable_Object = MibTable
tBgpInstRteTargetTable = _TBgpInstRteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 3)
)
if mibBuilder.loadTexts:
    tBgpInstRteTargetTable.setStatus("current")
_TBgpInstRteTargetEntry_Object = MibTableRow
tBgpInstRteTargetEntry = _TBgpInstRteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 3, 1)
)
tBgpInstRteTargetEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (1, "TIMETRA-BGP-MIB", "tBgpInstanceRouteTarget"),
)
if mibBuilder.loadTexts:
    tBgpInstRteTargetEntry.setStatus("current")
_TBgpInstanceRouteTarget_Type = TNamedItem
_TBgpInstanceRouteTarget_Object = MibTableColumn
tBgpInstanceRouteTarget = _TBgpInstanceRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 3, 1, 1),
    _TBgpInstanceRouteTarget_Type()
)
tBgpInstanceRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpInstanceRouteTarget.setStatus("current")
_TBgpInstRteTargetRowStatus_Type = RowStatus
_TBgpInstRteTargetRowStatus_Object = MibTableColumn
tBgpInstRteTargetRowStatus = _TBgpInstRteTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 3, 1, 2),
    _TBgpInstRteTargetRowStatus_Type()
)
tBgpInstRteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstRteTargetRowStatus.setStatus("current")
_TBgp4PathAttrTable_Object = MibTable
tBgp4PathAttrTable = _TBgp4PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4)
)
if mibBuilder.loadTexts:
    tBgp4PathAttrTable.setStatus("current")
_TBgp4PathAttrEntry_Object = MibTableRow
tBgp4PathAttrEntry = _TBgp4PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4, 1)
)
tBgp4PathAttrEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgp4PathAttrRD"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"),
    (0, "BGP4-MIB", "bgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    tBgp4PathAttrEntry.setStatus("current")
_TBgp4PathAttrRD_Type = TmnxVPNRouteDistinguisher
_TBgp4PathAttrRD_Object = MibTableColumn
tBgp4PathAttrRD = _TBgp4PathAttrRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4, 1, 1),
    _TBgp4PathAttrRD_Type()
)
tBgp4PathAttrRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgp4PathAttrRD.setStatus("current")
_TBgp4PathAttrOriginID_Type = IpAddress
_TBgp4PathAttrOriginID_Object = MibTableColumn
tBgp4PathAttrOriginID = _TBgp4PathAttrOriginID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4, 1, 2),
    _TBgp4PathAttrOriginID_Type()
)
tBgp4PathAttrOriginID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgp4PathAttrOriginID.setStatus("current")


class _TBgp4PathAttrClusterList_Type(OctetString):
    """Custom type tBgp4PathAttrClusterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_TBgp4PathAttrClusterList_Type.__name__ = "OctetString"
_TBgp4PathAttrClusterList_Object = MibTableColumn
tBgp4PathAttrClusterList = _TBgp4PathAttrClusterList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4, 1, 3),
    _TBgp4PathAttrClusterList_Type()
)
tBgp4PathAttrClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgp4PathAttrClusterList.setStatus("current")


class _TBgp4PathAttrCommunity_Type(OctetString):
    """Custom type tBgp4PathAttrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_TBgp4PathAttrCommunity_Type.__name__ = "OctetString"
_TBgp4PathAttrCommunity_Object = MibTableColumn
tBgp4PathAttrCommunity = _TBgp4PathAttrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4, 1, 4),
    _TBgp4PathAttrCommunity_Type()
)
tBgp4PathAttrCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgp4PathAttrCommunity.setStatus("current")


class _TBgp4PathAttrExtCommunity_Type(OctetString):
    """Custom type tBgp4PathAttrExtCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_TBgp4PathAttrExtCommunity_Type.__name__ = "OctetString"
_TBgp4PathAttrExtCommunity_Object = MibTableColumn
tBgp4PathAttrExtCommunity = _TBgp4PathAttrExtCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4, 1, 5),
    _TBgp4PathAttrExtCommunity_Type()
)
tBgp4PathAttrExtCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgp4PathAttrExtCommunity.setStatus("current")


class _Tbgp4PathAttrASPathSegment_Type(OctetString):
    """Custom type tbgp4PathAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Tbgp4PathAttrASPathSegment_Type.__name__ = "OctetString"
_Tbgp4PathAttrASPathSegment_Object = MibTableColumn
tbgp4PathAttrASPathSegment = _Tbgp4PathAttrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4, 1, 6),
    _Tbgp4PathAttrASPathSegment_Type()
)
tbgp4PathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbgp4PathAttrASPathSegment.setStatus("current")
_Tbgp4PathAttrAggregatorAS_Type = InetAutonomousSystemNumber
_Tbgp4PathAttrAggregatorAS_Object = MibTableColumn
tbgp4PathAttrAggregatorAS = _Tbgp4PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 4, 1, 7),
    _Tbgp4PathAttrAggregatorAS_Type()
)
tbgp4PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbgp4PathAttrAggregatorAS.setStatus("current")
_TBgpSendOrfRouteTargetTable_Object = MibTable
tBgpSendOrfRouteTargetTable = _TBgpSendOrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 5)
)
if mibBuilder.loadTexts:
    tBgpSendOrfRouteTargetTable.setStatus("current")
_TBgpSendOrfRouteTargetEntry_Object = MibTableRow
tBgpSendOrfRouteTargetEntry = _TBgpSendOrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 5, 1)
)
tBgpSendOrfRouteTargetEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (1, "TIMETRA-BGP-MIB", "tBgpSendOrfRouteTarget"),
)
if mibBuilder.loadTexts:
    tBgpSendOrfRouteTargetEntry.setStatus("current")
_TBgpSendOrfRouteTarget_Type = TNamedItem
_TBgpSendOrfRouteTarget_Object = MibTableColumn
tBgpSendOrfRouteTarget = _TBgpSendOrfRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 5, 1, 1),
    _TBgpSendOrfRouteTarget_Type()
)
tBgpSendOrfRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpSendOrfRouteTarget.setStatus("current")
_TBgpSendOrfRTRowStatus_Type = RowStatus
_TBgpSendOrfRTRowStatus_Object = MibTableColumn
tBgpSendOrfRTRowStatus = _TBgpSendOrfRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 5, 1, 2),
    _TBgpSendOrfRTRowStatus_Type()
)
tBgpSendOrfRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpSendOrfRTRowStatus.setStatus("current")
_TBgpInstanceParamsTable_Object = MibTable
tBgpInstanceParamsTable = _TBgpInstanceParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6)
)
if mibBuilder.loadTexts:
    tBgpInstanceParamsTable.setStatus("current")
_TBgpInstanceParamsEntry_Object = MibTableRow
tBgpInstanceParamsEntry = _TBgpInstanceParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1)
)
tBgpInstanceParamsEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
)
if mibBuilder.loadTexts:
    tBgpInstanceParamsEntry.setStatus("current")


class _TBgpInstanceDisableFEFailover_Type(TruthValue):
    """Custom type tBgpInstanceDisableFEFailover based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDisableFEFailover_Type.__name__ = "TruthValue"
_TBgpInstanceDisableFEFailover_Object = MibTableColumn
tBgpInstanceDisableFEFailover = _TBgpInstanceDisableFEFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 1),
    _TBgpInstanceDisableFEFailover_Type()
)
tBgpInstanceDisableFEFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDisableFEFailover.setStatus("current")


class _TBgpInstanceDisableComms_Type(TruthValue):
    """Custom type tBgpInstanceDisableComms based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDisableComms_Type.__name__ = "TruthValue"
_TBgpInstanceDisableComms_Object = MibTableColumn
tBgpInstanceDisableComms = _TBgpInstanceDisableComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 2),
    _TBgpInstanceDisableComms_Type()
)
tBgpInstanceDisableComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDisableComms.setStatus("current")


class _TBgpInstanceDisableExtComms_Type(TruthValue):
    """Custom type tBgpInstanceDisableExtComms based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDisableExtComms_Type.__name__ = "TruthValue"
_TBgpInstanceDisableExtComms_Object = MibTableColumn
tBgpInstanceDisableExtComms = _TBgpInstanceDisableExtComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 3),
    _TBgpInstanceDisableExtComms_Type()
)
tBgpInstanceDisableExtComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDisableExtComms.setStatus("current")


class _TBgpInstanceDefaultOriginate_Type(TruthValue):
    """Custom type tBgpInstanceDefaultOriginate based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDefaultOriginate_Type.__name__ = "TruthValue"
_TBgpInstanceDefaultOriginate_Object = MibTableColumn
tBgpInstanceDefaultOriginate = _TBgpInstanceDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 4),
    _TBgpInstanceDefaultOriginate_Type()
)
tBgpInstanceDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDefaultOriginate.setStatus("current")


class _TBgpInstanceAdvertiseInactiveRts_Type(TruthValue):
    """Custom type tBgpInstanceAdvertiseInactiveRts based on TruthValue"""
    defaultValue = 2


_TBgpInstanceAdvertiseInactiveRts_Type.__name__ = "TruthValue"
_TBgpInstanceAdvertiseInactiveRts_Object = MibTableColumn
tBgpInstanceAdvertiseInactiveRts = _TBgpInstanceAdvertiseInactiveRts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 5),
    _TBgpInstanceAdvertiseInactiveRts_Type()
)
tBgpInstanceAdvertiseInactiveRts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceAdvertiseInactiveRts.setStatus("current")


class _TBgpInstancePeerTracking_Type(TruthValue):
    """Custom type tBgpInstancePeerTracking based on TruthValue"""
    defaultValue = 2


_TBgpInstancePeerTracking_Type.__name__ = "TruthValue"
_TBgpInstancePeerTracking_Object = MibTableColumn
tBgpInstancePeerTracking = _TBgpInstancePeerTracking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 6),
    _TBgpInstancePeerTracking_Type()
)
tBgpInstancePeerTracking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePeerTracking.setStatus("current")


class _TBgpInstanceAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tBgpInstanceAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TBgpInstanceAuthKeyChain_Object = MibTableColumn
tBgpInstanceAuthKeyChain = _TBgpInstanceAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 7),
    _TBgpInstanceAuthKeyChain_Type()
)
tBgpInstanceAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceAuthKeyChain.setStatus("current")


class _TBgpInstanceRapidWithdrawal_Type(TruthValue):
    """Custom type tBgpInstanceRapidWithdrawal based on TruthValue"""
    defaultValue = 2


_TBgpInstanceRapidWithdrawal_Type.__name__ = "TruthValue"
_TBgpInstanceRapidWithdrawal_Object = MibTableColumn
tBgpInstanceRapidWithdrawal = _TBgpInstanceRapidWithdrawal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 8),
    _TBgpInstanceRapidWithdrawal_Type()
)
tBgpInstanceRapidWithdrawal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceRapidWithdrawal.setStatus("current")


class _TBgpInstanceBfdEnabled_Type(TruthValue):
    """Custom type tBgpInstanceBfdEnabled based on TruthValue"""
    defaultValue = 2


_TBgpInstanceBfdEnabled_Type.__name__ = "TruthValue"
_TBgpInstanceBfdEnabled_Object = MibTableColumn
tBgpInstanceBfdEnabled = _TBgpInstanceBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 9),
    _TBgpInstanceBfdEnabled_Type()
)
tBgpInstanceBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceBfdEnabled.setStatus("current")


class _TBgpInstanceRapidUpdate_Type(TmnxIpFamily):
    """Custom type tBgpInstanceRapidUpdate based on TmnxIpFamily"""
    defaultBinValue = "0"


_TBgpInstanceRapidUpdate_Type.__name__ = "TmnxIpFamily"
_TBgpInstanceRapidUpdate_Object = MibTableColumn
tBgpInstanceRapidUpdate = _TBgpInstanceRapidUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 10),
    _TBgpInstanceRapidUpdate_Type()
)
tBgpInstanceRapidUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceRapidUpdate.setStatus("current")


class _TBgpInstanceEnableAddPath_Type(TruthValue):
    """Custom type tBgpInstanceEnableAddPath based on TruthValue"""
    defaultValue = 2


_TBgpInstanceEnableAddPath_Type.__name__ = "TruthValue"
_TBgpInstanceEnableAddPath_Object = MibTableColumn
tBgpInstanceEnableAddPath = _TBgpInstanceEnableAddPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 11),
    _TBgpInstanceEnableAddPath_Type()
)
tBgpInstanceEnableAddPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceEnableAddPath.setStatus("current")


class _TBgpInstanceRecvAddPath_Type(TmnxAddPathAddressFamily):
    """Custom type tBgpInstanceRecvAddPath based on TmnxAddPathAddressFamily"""
    defaultBinValue = "1"


_TBgpInstanceRecvAddPath_Type.__name__ = "TmnxAddPathAddressFamily"
_TBgpInstanceRecvAddPath_Object = MibTableColumn
tBgpInstanceRecvAddPath = _TBgpInstanceRecvAddPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 12),
    _TBgpInstanceRecvAddPath_Type()
)
tBgpInstanceRecvAddPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceRecvAddPath.setStatus("current")


class _TBgpInstanceIpv4AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpInstanceIpv4AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpInstanceIpv4AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpInstanceIpv4AddPathLimit_Object = MibTableColumn
tBgpInstanceIpv4AddPathLimit = _TBgpInstanceIpv4AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 13),
    _TBgpInstanceIpv4AddPathLimit_Type()
)
tBgpInstanceIpv4AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceIpv4AddPathLimit.setStatus("current")


class _TBgpInstanceVpnIpv4AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpInstanceVpnIpv4AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpInstanceVpnIpv4AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpInstanceVpnIpv4AddPathLimit_Object = MibTableColumn
tBgpInstanceVpnIpv4AddPathLimit = _TBgpInstanceVpnIpv4AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 14),
    _TBgpInstanceVpnIpv4AddPathLimit_Type()
)
tBgpInstanceVpnIpv4AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceVpnIpv4AddPathLimit.setStatus("current")


class _TBgpInstanceIpv6AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpInstanceIpv6AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpInstanceIpv6AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpInstanceIpv6AddPathLimit_Object = MibTableColumn
tBgpInstanceIpv6AddPathLimit = _TBgpInstanceIpv6AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 15),
    _TBgpInstanceIpv6AddPathLimit_Type()
)
tBgpInstanceIpv6AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceIpv6AddPathLimit.setStatus("current")


class _TBgpInstanceVpnIpv6AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpInstanceVpnIpv6AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpInstanceVpnIpv6AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpInstanceVpnIpv6AddPathLimit_Object = MibTableColumn
tBgpInstanceVpnIpv6AddPathLimit = _TBgpInstanceVpnIpv6AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 16),
    _TBgpInstanceVpnIpv6AddPathLimit_Type()
)
tBgpInstanceVpnIpv6AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceVpnIpv6AddPathLimit.setStatus("current")


class _TBgpInstanceTransportTunnel_Type(Bits):
    """Custom type tBgpInstanceTransportTunnel based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("ldp", 0),
          ("rsvp-te", 1),
          ("mpls", 2))
    )

_TBgpInstanceTransportTunnel_Type.__name__ = "Bits"
_TBgpInstanceTransportTunnel_Object = MibTableColumn
tBgpInstanceTransportTunnel = _TBgpInstanceTransportTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 17),
    _TBgpInstanceTransportTunnel_Type()
)
tBgpInstanceTransportTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceTransportTunnel.setStatus("current")


class _TBgpInstanceFlowspecValidate_Type(TruthValue):
    """Custom type tBgpInstanceFlowspecValidate based on TruthValue"""
    defaultValue = 2


_TBgpInstanceFlowspecValidate_Type.__name__ = "TruthValue"
_TBgpInstanceFlowspecValidate_Object = MibTableColumn
tBgpInstanceFlowspecValidate = _TBgpInstanceFlowspecValidate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 18),
    _TBgpInstanceFlowspecValidate_Type()
)
tBgpInstanceFlowspecValidate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceFlowspecValidate.setStatus("current")
_TBgpInstanceAdvertiseExternal_Type = TmnxIpFamily
_TBgpInstanceAdvertiseExternal_Object = MibTableColumn
tBgpInstanceAdvertiseExternal = _TBgpInstanceAdvertiseExternal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 19),
    _TBgpInstanceAdvertiseExternal_Type()
)
tBgpInstanceAdvertiseExternal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceAdvertiseExternal.setStatus("current")
_TBgpInstanceBackupPath_Type = TmnxIpFamily
_TBgpInstanceBackupPath_Object = MibTableColumn
tBgpInstanceBackupPath = _TBgpInstanceBackupPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 20),
    _TBgpInstanceBackupPath_Type()
)
tBgpInstanceBackupPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceBackupPath.setStatus("current")


class _TBgpInstanceIgnoreNextHopMetric_Type(TruthValue):
    """Custom type tBgpInstanceIgnoreNextHopMetric based on TruthValue"""
    defaultValue = 2


_TBgpInstanceIgnoreNextHopMetric_Type.__name__ = "TruthValue"
_TBgpInstanceIgnoreNextHopMetric_Object = MibTableColumn
tBgpInstanceIgnoreNextHopMetric = _TBgpInstanceIgnoreNextHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 21),
    _TBgpInstanceIgnoreNextHopMetric_Type()
)
tBgpInstanceIgnoreNextHopMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceIgnoreNextHopMetric.setStatus("current")


class _TBgpInstanceMpBgpKeep_Type(TruthValue):
    """Custom type tBgpInstanceMpBgpKeep based on TruthValue"""
    defaultValue = 2


_TBgpInstanceMpBgpKeep_Type.__name__ = "TruthValue"
_TBgpInstanceMpBgpKeep_Object = MibTableColumn
tBgpInstanceMpBgpKeep = _TBgpInstanceMpBgpKeep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 22),
    _TBgpInstanceMpBgpKeep_Type()
)
tBgpInstanceMpBgpKeep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMpBgpKeep.setStatus("current")


class _TBgpInstanceIgnoreRouterId_Type(TruthValue):
    """Custom type tBgpInstanceIgnoreRouterId based on TruthValue"""
    defaultValue = 2


_TBgpInstanceIgnoreRouterId_Type.__name__ = "TruthValue"
_TBgpInstanceIgnoreRouterId_Object = MibTableColumn
tBgpInstanceIgnoreRouterId = _TBgpInstanceIgnoreRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 23),
    _TBgpInstanceIgnoreRouterId_Type()
)
tBgpInstanceIgnoreRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceIgnoreRouterId.setStatus("current")


class _TBgpInstanceAlwaysCompMEDStrict_Type(TruthValue):
    """Custom type tBgpInstanceAlwaysCompMEDStrict based on TruthValue"""
    defaultValue = 1


_TBgpInstanceAlwaysCompMEDStrict_Type.__name__ = "TruthValue"
_TBgpInstanceAlwaysCompMEDStrict_Object = MibTableColumn
tBgpInstanceAlwaysCompMEDStrict = _TBgpInstanceAlwaysCompMEDStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 24),
    _TBgpInstanceAlwaysCompMEDStrict_Type()
)
tBgpInstanceAlwaysCompMEDStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceAlwaysCompMEDStrict.setStatus("current")


class _TBgpInstanceMinHoldTime_Type(BgpHoldTime):
    """Custom type tBgpInstanceMinHoldTime based on BgpHoldTime"""
    defaultValue = 0


_TBgpInstanceMinHoldTime_Type.__name__ = "BgpHoldTime"
_TBgpInstanceMinHoldTime_Object = MibTableColumn
tBgpInstanceMinHoldTime = _TBgpInstanceMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 25),
    _TBgpInstanceMinHoldTime_Type()
)
tBgpInstanceMinHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceMinHoldTime.setStatus("current")


class _TBgpInstRemovePrivateSkipPeerAs_Type(TruthValue):
    """Custom type tBgpInstRemovePrivateSkipPeerAs based on TruthValue"""
    defaultValue = 2


_TBgpInstRemovePrivateSkipPeerAs_Type.__name__ = "TruthValue"
_TBgpInstRemovePrivateSkipPeerAs_Object = MibTableColumn
tBgpInstRemovePrivateSkipPeerAs = _TBgpInstRemovePrivateSkipPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 26),
    _TBgpInstRemovePrivateSkipPeerAs_Type()
)
tBgpInstRemovePrivateSkipPeerAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstRemovePrivateSkipPeerAs.setStatus("current")


class _TBgpInstLocalASNoPrependGlobalAS_Type(TruthValue):
    """Custom type tBgpInstLocalASNoPrependGlobalAS based on TruthValue"""
    defaultValue = 2


_TBgpInstLocalASNoPrependGlobalAS_Type.__name__ = "TruthValue"
_TBgpInstLocalASNoPrependGlobalAS_Object = MibTableColumn
tBgpInstLocalASNoPrependGlobalAS = _TBgpInstLocalASNoPrependGlobalAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 27),
    _TBgpInstLocalASNoPrependGlobalAS_Type()
)
tBgpInstLocalASNoPrependGlobalAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstLocalASNoPrependGlobalAS.setStatus("current")


class _TBgpInstanceNHResPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstanceNHResPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstanceNHResPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstanceNHResPolicy_Object = MibTableColumn
tBgpInstanceNHResPolicy = _TBgpInstanceNHResPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 28),
    _TBgpInstanceNHResPolicy_Type()
)
tBgpInstanceNHResPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceNHResPolicy.setStatus("current")


class _TBgpInstancePeerTrackingPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePeerTrackingPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePeerTrackingPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePeerTrackingPolicy_Object = MibTableColumn
tBgpInstancePeerTrackingPolicy = _TBgpInstancePeerTrackingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 29),
    _TBgpInstancePeerTrackingPolicy_Type()
)
tBgpInstancePeerTrackingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePeerTrackingPolicy.setStatus("current")


class _TBgpInstGrRestartNotification_Type(TruthValue):
    """Custom type tBgpInstGrRestartNotification based on TruthValue"""
    defaultValue = 2


_TBgpInstGrRestartNotification_Type.__name__ = "TruthValue"
_TBgpInstGrRestartNotification_Object = MibTableColumn
tBgpInstGrRestartNotification = _TBgpInstGrRestartNotification_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 30),
    _TBgpInstGrRestartNotification_Type()
)
tBgpInstGrRestartNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstGrRestartNotification.setStatus("current")


class _TBgpInstanceFaultTolerance_Type(TruthValue):
    """Custom type tBgpInstanceFaultTolerance based on TruthValue"""
    defaultValue = 2


_TBgpInstanceFaultTolerance_Type.__name__ = "TruthValue"
_TBgpInstanceFaultTolerance_Object = MibTableColumn
tBgpInstanceFaultTolerance = _TBgpInstanceFaultTolerance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 31),
    _TBgpInstanceFaultTolerance_Type()
)
tBgpInstanceFaultTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceFaultTolerance.setStatus("current")


class _TBgpInstanceDampPeerOscillations_Type(TruthValue):
    """Custom type tBgpInstanceDampPeerOscillations based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDampPeerOscillations_Type.__name__ = "TruthValue"
_TBgpInstanceDampPeerOscillations_Object = MibTableColumn
tBgpInstanceDampPeerOscillations = _TBgpInstanceDampPeerOscillations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 32),
    _TBgpInstanceDampPeerOscillations_Type()
)
tBgpInstanceDampPeerOscillations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDampPeerOscillations.setStatus("current")


class _TBgpInstDmpPeerOscInitialWaitTim_Type(Unsigned32):
    """Custom type tBgpInstDmpPeerOscInitialWaitTim based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_TBgpInstDmpPeerOscInitialWaitTim_Type.__name__ = "Unsigned32"
_TBgpInstDmpPeerOscInitialWaitTim_Object = MibTableColumn
tBgpInstDmpPeerOscInitialWaitTim = _TBgpInstDmpPeerOscInitialWaitTim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 33),
    _TBgpInstDmpPeerOscInitialWaitTim_Type()
)
tBgpInstDmpPeerOscInitialWaitTim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstDmpPeerOscInitialWaitTim.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstDmpPeerOscInitialWaitTim.setUnits("minutes")


class _TBgpInstDmpPeerOscSecondWaitTime_Type(Unsigned32):
    """Custom type tBgpInstDmpPeerOscSecondWaitTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TBgpInstDmpPeerOscSecondWaitTime_Type.__name__ = "Unsigned32"
_TBgpInstDmpPeerOscSecondWaitTime_Object = MibTableColumn
tBgpInstDmpPeerOscSecondWaitTime = _TBgpInstDmpPeerOscSecondWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 34),
    _TBgpInstDmpPeerOscSecondWaitTime_Type()
)
tBgpInstDmpPeerOscSecondWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstDmpPeerOscSecondWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstDmpPeerOscSecondWaitTime.setUnits("minutes")


class _TBgpInstDmpPeerOscMaxWaitTime_Type(Unsigned32):
    """Custom type tBgpInstDmpPeerOscMaxWaitTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TBgpInstDmpPeerOscMaxWaitTime_Type.__name__ = "Unsigned32"
_TBgpInstDmpPeerOscMaxWaitTime_Object = MibTableColumn
tBgpInstDmpPeerOscMaxWaitTime = _TBgpInstDmpPeerOscMaxWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 35),
    _TBgpInstDmpPeerOscMaxWaitTime_Type()
)
tBgpInstDmpPeerOscMaxWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstDmpPeerOscMaxWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstDmpPeerOscMaxWaitTime.setUnits("minutes")


class _TBgpInstDmpPeerOscErrorInterval_Type(Unsigned32):
    """Custom type tBgpInstDmpPeerOscErrorInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_TBgpInstDmpPeerOscErrorInterval_Type.__name__ = "Unsigned32"
_TBgpInstDmpPeerOscErrorInterval_Object = MibTableColumn
tBgpInstDmpPeerOscErrorInterval = _TBgpInstDmpPeerOscErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 36),
    _TBgpInstDmpPeerOscErrorInterval_Type()
)
tBgpInstDmpPeerOscErrorInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstDmpPeerOscErrorInterval.setStatus("current")
if mibBuilder.loadTexts:
    tBgpInstDmpPeerOscErrorInterval.setUnits("minutes")


class _TBgpInstanceDeterministicMED_Type(TruthValue):
    """Custom type tBgpInstanceDeterministicMED based on TruthValue"""
    defaultValue = 2


_TBgpInstanceDeterministicMED_Type.__name__ = "TruthValue"
_TBgpInstanceDeterministicMED_Object = MibTableColumn
tBgpInstanceDeterministicMED = _TBgpInstanceDeterministicMED_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 37),
    _TBgpInstanceDeterministicMED_Type()
)
tBgpInstanceDeterministicMED.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceDeterministicMED.setStatus("current")


class _TBgpInstanceSplitHorizon_Type(TruthValue):
    """Custom type tBgpInstanceSplitHorizon based on TruthValue"""
    defaultValue = 2


_TBgpInstanceSplitHorizon_Type.__name__ = "TruthValue"
_TBgpInstanceSplitHorizon_Object = MibTableColumn
tBgpInstanceSplitHorizon = _TBgpInstanceSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 38),
    _TBgpInstanceSplitHorizon_Type()
)
tBgpInstanceSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceSplitHorizon.setStatus("current")


class _TBgpInstMvpnVrfImportSubTypeNew_Type(TruthValue):
    """Custom type tBgpInstMvpnVrfImportSubTypeNew based on TruthValue"""
    defaultValue = 2


_TBgpInstMvpnVrfImportSubTypeNew_Type.__name__ = "TruthValue"
_TBgpInstMvpnVrfImportSubTypeNew_Object = MibTableColumn
tBgpInstMvpnVrfImportSubTypeNew = _TBgpInstMvpnVrfImportSubTypeNew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 39),
    _TBgpInstMvpnVrfImportSubTypeNew_Type()
)
tBgpInstMvpnVrfImportSubTypeNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstMvpnVrfImportSubTypeNew.setStatus("current")


class _TBgpInstResolveLabelRoutesInRtm_Type(TruthValue):
    """Custom type tBgpInstResolveLabelRoutesInRtm based on TruthValue"""
    defaultValue = 2


_TBgpInstResolveLabelRoutesInRtm_Type.__name__ = "TruthValue"
_TBgpInstResolveLabelRoutesInRtm_Object = MibTableColumn
tBgpInstResolveLabelRoutesInRtm = _TBgpInstResolveLabelRoutesInRtm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 40),
    _TBgpInstResolveLabelRoutesInRtm_Type()
)
tBgpInstResolveLabelRoutesInRtm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstResolveLabelRoutesInRtm.setStatus("current")


class _TBgpInstanceCompOriginValidState_Type(TruthValue):
    """Custom type tBgpInstanceCompOriginValidState based on TruthValue"""
    defaultValue = 2


_TBgpInstanceCompOriginValidState_Type.__name__ = "TruthValue"
_TBgpInstanceCompOriginValidState_Object = MibTableColumn
tBgpInstanceCompOriginValidState = _TBgpInstanceCompOriginValidState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 41),
    _TBgpInstanceCompOriginValidState_Type()
)
tBgpInstanceCompOriginValidState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceCompOriginValidState.setStatus("current")


class _TBgpInstanceThirdPartyNextHop_Type(TruthValue):
    """Custom type tBgpInstanceThirdPartyNextHop based on TruthValue"""
    defaultValue = 2


_TBgpInstanceThirdPartyNextHop_Type.__name__ = "TruthValue"
_TBgpInstanceThirdPartyNextHop_Object = MibTableColumn
tBgpInstanceThirdPartyNextHop = _TBgpInstanceThirdPartyNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 42),
    _TBgpInstanceThirdPartyNextHop_Type()
)
tBgpInstanceThirdPartyNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceThirdPartyNextHop.setStatus("current")


class _TBgpInstanceOrigInvalidUnusable_Type(TruthValue):
    """Custom type tBgpInstanceOrigInvalidUnusable based on TruthValue"""
    defaultValue = 2


_TBgpInstanceOrigInvalidUnusable_Type.__name__ = "TruthValue"
_TBgpInstanceOrigInvalidUnusable_Object = MibTableColumn
tBgpInstanceOrigInvalidUnusable = _TBgpInstanceOrigInvalidUnusable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 43),
    _TBgpInstanceOrigInvalidUnusable_Type()
)
tBgpInstanceOrigInvalidUnusable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceOrigInvalidUnusable.setStatus("current")


class _TBgpInstanceIgnoreRtrIdInternal_Type(TmnxIpFamily):
    """Custom type tBgpInstanceIgnoreRtrIdInternal based on TmnxIpFamily"""
    defaultHexValue = ""


_TBgpInstanceIgnoreRtrIdInternal_Type.__name__ = "TmnxIpFamily"
_TBgpInstanceIgnoreRtrIdInternal_Object = MibTableColumn
tBgpInstanceIgnoreRtrIdInternal = _TBgpInstanceIgnoreRtrIdInternal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 44),
    _TBgpInstanceIgnoreRtrIdInternal_Type()
)
tBgpInstanceIgnoreRtrIdInternal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceIgnoreRtrIdInternal.setStatus("current")


class _TBgpInstanceIgnoreRtrIdExternal_Type(TmnxIpFamily):
    """Custom type tBgpInstanceIgnoreRtrIdExternal based on TmnxIpFamily"""
    defaultHexValue = ""


_TBgpInstanceIgnoreRtrIdExternal_Type.__name__ = "TmnxIpFamily"
_TBgpInstanceIgnoreRtrIdExternal_Object = MibTableColumn
tBgpInstanceIgnoreRtrIdExternal = _TBgpInstanceIgnoreRtrIdExternal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 6, 1, 45),
    _TBgpInstanceIgnoreRtrIdExternal_Type()
)
tBgpInstanceIgnoreRtrIdExternal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstanceIgnoreRtrIdExternal.setStatus("current")
_TBgpInstancePlcyTable_Object = MibTable
tBgpInstancePlcyTable = _TBgpInstancePlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7)
)
if mibBuilder.loadTexts:
    tBgpInstancePlcyTable.setStatus("current")
_TBgpInstancePlcyEntry_Object = MibTableRow
tBgpInstancePlcyEntry = _TBgpInstancePlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1)
)
if mibBuilder.loadTexts:
    tBgpInstancePlcyEntry.setStatus("current")


class _TBgpInstancePlcyImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy1_Object = MibTableColumn
tBgpInstancePlcyImportPolicy1 = _TBgpInstancePlcyImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 1),
    _TBgpInstancePlcyImportPolicy1_Type()
)
tBgpInstancePlcyImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy1.setStatus("current")


class _TBgpInstancePlcyImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy2_Object = MibTableColumn
tBgpInstancePlcyImportPolicy2 = _TBgpInstancePlcyImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 2),
    _TBgpInstancePlcyImportPolicy2_Type()
)
tBgpInstancePlcyImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy2.setStatus("current")


class _TBgpInstancePlcyImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy3_Object = MibTableColumn
tBgpInstancePlcyImportPolicy3 = _TBgpInstancePlcyImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 3),
    _TBgpInstancePlcyImportPolicy3_Type()
)
tBgpInstancePlcyImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy3.setStatus("current")


class _TBgpInstancePlcyImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy4_Object = MibTableColumn
tBgpInstancePlcyImportPolicy4 = _TBgpInstancePlcyImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 4),
    _TBgpInstancePlcyImportPolicy4_Type()
)
tBgpInstancePlcyImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy4.setStatus("current")


class _TBgpInstancePlcyImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy5_Object = MibTableColumn
tBgpInstancePlcyImportPolicy5 = _TBgpInstancePlcyImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 5),
    _TBgpInstancePlcyImportPolicy5_Type()
)
tBgpInstancePlcyImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy5.setStatus("current")


class _TBgpInstancePlcyImportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy6_Object = MibTableColumn
tBgpInstancePlcyImportPolicy6 = _TBgpInstancePlcyImportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 6),
    _TBgpInstancePlcyImportPolicy6_Type()
)
tBgpInstancePlcyImportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy6.setStatus("current")


class _TBgpInstancePlcyImportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy7_Object = MibTableColumn
tBgpInstancePlcyImportPolicy7 = _TBgpInstancePlcyImportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 7),
    _TBgpInstancePlcyImportPolicy7_Type()
)
tBgpInstancePlcyImportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy7.setStatus("current")


class _TBgpInstancePlcyImportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy8_Object = MibTableColumn
tBgpInstancePlcyImportPolicy8 = _TBgpInstancePlcyImportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 8),
    _TBgpInstancePlcyImportPolicy8_Type()
)
tBgpInstancePlcyImportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy8.setStatus("current")


class _TBgpInstancePlcyImportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy9_Object = MibTableColumn
tBgpInstancePlcyImportPolicy9 = _TBgpInstancePlcyImportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 9),
    _TBgpInstancePlcyImportPolicy9_Type()
)
tBgpInstancePlcyImportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy9.setStatus("current")


class _TBgpInstancePlcyImportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy10_Object = MibTableColumn
tBgpInstancePlcyImportPolicy10 = _TBgpInstancePlcyImportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 10),
    _TBgpInstancePlcyImportPolicy10_Type()
)
tBgpInstancePlcyImportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy10.setStatus("current")


class _TBgpInstancePlcyImportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy11_Object = MibTableColumn
tBgpInstancePlcyImportPolicy11 = _TBgpInstancePlcyImportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 11),
    _TBgpInstancePlcyImportPolicy11_Type()
)
tBgpInstancePlcyImportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy11.setStatus("current")


class _TBgpInstancePlcyImportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy12_Object = MibTableColumn
tBgpInstancePlcyImportPolicy12 = _TBgpInstancePlcyImportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 12),
    _TBgpInstancePlcyImportPolicy12_Type()
)
tBgpInstancePlcyImportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy12.setStatus("current")


class _TBgpInstancePlcyImportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy13_Object = MibTableColumn
tBgpInstancePlcyImportPolicy13 = _TBgpInstancePlcyImportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 13),
    _TBgpInstancePlcyImportPolicy13_Type()
)
tBgpInstancePlcyImportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy13.setStatus("current")


class _TBgpInstancePlcyImportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy14_Object = MibTableColumn
tBgpInstancePlcyImportPolicy14 = _TBgpInstancePlcyImportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 14),
    _TBgpInstancePlcyImportPolicy14_Type()
)
tBgpInstancePlcyImportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy14.setStatus("current")


class _TBgpInstancePlcyImportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyImportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyImportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyImportPolicy15_Object = MibTableColumn
tBgpInstancePlcyImportPolicy15 = _TBgpInstancePlcyImportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 15),
    _TBgpInstancePlcyImportPolicy15_Type()
)
tBgpInstancePlcyImportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyImportPolicy15.setStatus("current")


class _TBgpInstancePlcyExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy1_Object = MibTableColumn
tBgpInstancePlcyExportPolicy1 = _TBgpInstancePlcyExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 16),
    _TBgpInstancePlcyExportPolicy1_Type()
)
tBgpInstancePlcyExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy1.setStatus("current")


class _TBgpInstancePlcyExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy2_Object = MibTableColumn
tBgpInstancePlcyExportPolicy2 = _TBgpInstancePlcyExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 17),
    _TBgpInstancePlcyExportPolicy2_Type()
)
tBgpInstancePlcyExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy2.setStatus("current")


class _TBgpInstancePlcyExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy3_Object = MibTableColumn
tBgpInstancePlcyExportPolicy3 = _TBgpInstancePlcyExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 18),
    _TBgpInstancePlcyExportPolicy3_Type()
)
tBgpInstancePlcyExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy3.setStatus("current")


class _TBgpInstancePlcyExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy4_Object = MibTableColumn
tBgpInstancePlcyExportPolicy4 = _TBgpInstancePlcyExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 19),
    _TBgpInstancePlcyExportPolicy4_Type()
)
tBgpInstancePlcyExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy4.setStatus("current")


class _TBgpInstancePlcyExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy5_Object = MibTableColumn
tBgpInstancePlcyExportPolicy5 = _TBgpInstancePlcyExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 20),
    _TBgpInstancePlcyExportPolicy5_Type()
)
tBgpInstancePlcyExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy5.setStatus("current")


class _TBgpInstancePlcyExportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy6_Object = MibTableColumn
tBgpInstancePlcyExportPolicy6 = _TBgpInstancePlcyExportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 21),
    _TBgpInstancePlcyExportPolicy6_Type()
)
tBgpInstancePlcyExportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy6.setStatus("current")


class _TBgpInstancePlcyExportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy7_Object = MibTableColumn
tBgpInstancePlcyExportPolicy7 = _TBgpInstancePlcyExportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 22),
    _TBgpInstancePlcyExportPolicy7_Type()
)
tBgpInstancePlcyExportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy7.setStatus("current")


class _TBgpInstancePlcyExportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy8_Object = MibTableColumn
tBgpInstancePlcyExportPolicy8 = _TBgpInstancePlcyExportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 23),
    _TBgpInstancePlcyExportPolicy8_Type()
)
tBgpInstancePlcyExportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy8.setStatus("current")


class _TBgpInstancePlcyExportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy9_Object = MibTableColumn
tBgpInstancePlcyExportPolicy9 = _TBgpInstancePlcyExportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 24),
    _TBgpInstancePlcyExportPolicy9_Type()
)
tBgpInstancePlcyExportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy9.setStatus("current")


class _TBgpInstancePlcyExportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy10_Object = MibTableColumn
tBgpInstancePlcyExportPolicy10 = _TBgpInstancePlcyExportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 25),
    _TBgpInstancePlcyExportPolicy10_Type()
)
tBgpInstancePlcyExportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy10.setStatus("current")


class _TBgpInstancePlcyExportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy11_Object = MibTableColumn
tBgpInstancePlcyExportPolicy11 = _TBgpInstancePlcyExportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 26),
    _TBgpInstancePlcyExportPolicy11_Type()
)
tBgpInstancePlcyExportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy11.setStatus("current")


class _TBgpInstancePlcyExportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy12_Object = MibTableColumn
tBgpInstancePlcyExportPolicy12 = _TBgpInstancePlcyExportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 27),
    _TBgpInstancePlcyExportPolicy12_Type()
)
tBgpInstancePlcyExportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy12.setStatus("current")


class _TBgpInstancePlcyExportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy13_Object = MibTableColumn
tBgpInstancePlcyExportPolicy13 = _TBgpInstancePlcyExportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 28),
    _TBgpInstancePlcyExportPolicy13_Type()
)
tBgpInstancePlcyExportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy13.setStatus("current")


class _TBgpInstancePlcyExportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy14_Object = MibTableColumn
tBgpInstancePlcyExportPolicy14 = _TBgpInstancePlcyExportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 29),
    _TBgpInstancePlcyExportPolicy14_Type()
)
tBgpInstancePlcyExportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy14.setStatus("current")


class _TBgpInstancePlcyExportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpInstancePlcyExportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpInstancePlcyExportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpInstancePlcyExportPolicy15_Object = MibTableColumn
tBgpInstancePlcyExportPolicy15 = _TBgpInstancePlcyExportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 7, 1, 30),
    _TBgpInstancePlcyExportPolicy15_Type()
)
tBgpInstancePlcyExportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpInstancePlcyExportPolicy15.setStatus("current")
_TBgpRibLeakImportPolicyTblLstCh_Type = TimeStamp
_TBgpRibLeakImportPolicyTblLstCh_Object = MibScalar
tBgpRibLeakImportPolicyTblLstCh = _TBgpRibLeakImportPolicyTblLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 8),
    _TBgpRibLeakImportPolicyTblLstCh_Type()
)
tBgpRibLeakImportPolicyTblLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicyTblLstCh.setStatus("current")
_TBgpRibLeakImportPolicyTable_Object = MibTable
tBgpRibLeakImportPolicyTable = _TBgpRibLeakImportPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9)
)
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicyTable.setStatus("current")
_TBgpRibLeakImportPolicyEntry_Object = MibTableRow
tBgpRibLeakImportPolicyEntry = _TBgpRibLeakImportPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1)
)
tBgpRibLeakImportPolicyEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicyFamily"),
)
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicyEntry.setStatus("current")
_TBgpRibLeakImportPolicyFamily_Type = TmnxIpFamilyIdentifier
_TBgpRibLeakImportPolicyFamily_Object = MibTableColumn
tBgpRibLeakImportPolicyFamily = _TBgpRibLeakImportPolicyFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 1),
    _TBgpRibLeakImportPolicyFamily_Type()
)
tBgpRibLeakImportPolicyFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicyFamily.setStatus("current")
_TBgpRibLeakImportPolicyLstCh_Type = TimeStamp
_TBgpRibLeakImportPolicyLstCh_Object = MibTableColumn
tBgpRibLeakImportPolicyLstCh = _TBgpRibLeakImportPolicyLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 2),
    _TBgpRibLeakImportPolicyLstCh_Type()
)
tBgpRibLeakImportPolicyLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicyLstCh.setStatus("current")


class _TBgpRibLeakImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy1_Object = MibTableColumn
tBgpRibLeakImportPolicy1 = _TBgpRibLeakImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 3),
    _TBgpRibLeakImportPolicy1_Type()
)
tBgpRibLeakImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy1.setStatus("current")


class _TBgpRibLeakImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy2_Object = MibTableColumn
tBgpRibLeakImportPolicy2 = _TBgpRibLeakImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 4),
    _TBgpRibLeakImportPolicy2_Type()
)
tBgpRibLeakImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy2.setStatus("current")


class _TBgpRibLeakImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy3_Object = MibTableColumn
tBgpRibLeakImportPolicy3 = _TBgpRibLeakImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 5),
    _TBgpRibLeakImportPolicy3_Type()
)
tBgpRibLeakImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy3.setStatus("current")


class _TBgpRibLeakImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy4_Object = MibTableColumn
tBgpRibLeakImportPolicy4 = _TBgpRibLeakImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 6),
    _TBgpRibLeakImportPolicy4_Type()
)
tBgpRibLeakImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy4.setStatus("current")


class _TBgpRibLeakImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy5_Object = MibTableColumn
tBgpRibLeakImportPolicy5 = _TBgpRibLeakImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 7),
    _TBgpRibLeakImportPolicy5_Type()
)
tBgpRibLeakImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy5.setStatus("current")


class _TBgpRibLeakImportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy6_Object = MibTableColumn
tBgpRibLeakImportPolicy6 = _TBgpRibLeakImportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 8),
    _TBgpRibLeakImportPolicy6_Type()
)
tBgpRibLeakImportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy6.setStatus("current")


class _TBgpRibLeakImportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy7_Object = MibTableColumn
tBgpRibLeakImportPolicy7 = _TBgpRibLeakImportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 9),
    _TBgpRibLeakImportPolicy7_Type()
)
tBgpRibLeakImportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy7.setStatus("current")


class _TBgpRibLeakImportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy8_Object = MibTableColumn
tBgpRibLeakImportPolicy8 = _TBgpRibLeakImportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 10),
    _TBgpRibLeakImportPolicy8_Type()
)
tBgpRibLeakImportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy8.setStatus("current")


class _TBgpRibLeakImportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy9_Object = MibTableColumn
tBgpRibLeakImportPolicy9 = _TBgpRibLeakImportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 11),
    _TBgpRibLeakImportPolicy9_Type()
)
tBgpRibLeakImportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy9.setStatus("current")


class _TBgpRibLeakImportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy10_Object = MibTableColumn
tBgpRibLeakImportPolicy10 = _TBgpRibLeakImportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 12),
    _TBgpRibLeakImportPolicy10_Type()
)
tBgpRibLeakImportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy10.setStatus("current")


class _TBgpRibLeakImportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy11_Object = MibTableColumn
tBgpRibLeakImportPolicy11 = _TBgpRibLeakImportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 13),
    _TBgpRibLeakImportPolicy11_Type()
)
tBgpRibLeakImportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy11.setStatus("current")


class _TBgpRibLeakImportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy12_Object = MibTableColumn
tBgpRibLeakImportPolicy12 = _TBgpRibLeakImportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 14),
    _TBgpRibLeakImportPolicy12_Type()
)
tBgpRibLeakImportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy12.setStatus("current")


class _TBgpRibLeakImportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy13_Object = MibTableColumn
tBgpRibLeakImportPolicy13 = _TBgpRibLeakImportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 15),
    _TBgpRibLeakImportPolicy13_Type()
)
tBgpRibLeakImportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy13.setStatus("current")


class _TBgpRibLeakImportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy14_Object = MibTableColumn
tBgpRibLeakImportPolicy14 = _TBgpRibLeakImportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 16),
    _TBgpRibLeakImportPolicy14_Type()
)
tBgpRibLeakImportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy14.setStatus("current")


class _TBgpRibLeakImportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpRibLeakImportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpRibLeakImportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpRibLeakImportPolicy15_Object = MibTableColumn
tBgpRibLeakImportPolicy15 = _TBgpRibLeakImportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 2, 9, 1, 17),
    _TBgpRibLeakImportPolicy15_Type()
)
tBgpRibLeakImportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpRibLeakImportPolicy15.setStatus("current")
_TBgpPeerGroupObjects_ObjectIdentity = ObjectIdentity
tBgpPeerGroupObjects = _TBgpPeerGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3)
)
_TBgpPeerGroupTableLastChanged_Type = TimeStamp
_TBgpPeerGroupTableLastChanged_Object = MibScalar
tBgpPeerGroupTableLastChanged = _TBgpPeerGroupTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 1),
    _TBgpPeerGroupTableLastChanged_Type()
)
tBgpPeerGroupTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerGroupTableLastChanged.setStatus("current")


class _TBgpPeerGroupTableSpinlock_Type(TestAndIncr):
    """Custom type tBgpPeerGroupTableSpinlock based on TestAndIncr"""
    defaultValue = 0


_TBgpPeerGroupTableSpinlock_Type.__name__ = "TestAndIncr"
_TBgpPeerGroupTableSpinlock_Object = MibScalar
tBgpPeerGroupTableSpinlock = _TBgpPeerGroupTableSpinlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 2),
    _TBgpPeerGroupTableSpinlock_Type()
)
tBgpPeerGroupTableSpinlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tBgpPeerGroupTableSpinlock.setStatus("current")
_TBgpPeerGroupTable_Object = MibTable
tBgpPeerGroupTable = _TBgpPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3)
)
if mibBuilder.loadTexts:
    tBgpPeerGroupTable.setStatus("current")
_TBgpPeerGroupEntry_Object = MibTableRow
tBgpPeerGroupEntry = _TBgpPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1)
)
tBgpPeerGroupEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerGroupName"),
)
if mibBuilder.loadTexts:
    tBgpPeerGroupEntry.setStatus("current")
_TBgpPeerGroupName_Type = BgpPeerGroupName
_TBgpPeerGroupName_Object = MibTableColumn
tBgpPeerGroupName = _TBgpPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 1),
    _TBgpPeerGroupName_Type()
)
tBgpPeerGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupName.setStatus("current")
_TBgpPeerGroupRowStatus_Type = RowStatus
_TBgpPeerGroupRowStatus_Object = MibTableColumn
tBgpPeerGroupRowStatus = _TBgpPeerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 2),
    _TBgpPeerGroupRowStatus_Type()
)
tBgpPeerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupRowStatus.setStatus("current")


class _TBgpPeerGroupShutdown_Type(TruthValue):
    """Custom type tBgpPeerGroupShutdown based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupShutdown_Type.__name__ = "TruthValue"
_TBgpPeerGroupShutdown_Object = MibTableColumn
tBgpPeerGroupShutdown = _TBgpPeerGroupShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 3),
    _TBgpPeerGroupShutdown_Type()
)
tBgpPeerGroupShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupShutdown.setStatus("current")


class _TBgpPeerGroupDescription_Type(DisplayString):
    """Custom type tBgpPeerGroupDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TBgpPeerGroupDescription_Type.__name__ = "DisplayString"
_TBgpPeerGroupDescription_Object = MibTableColumn
tBgpPeerGroupDescription = _TBgpPeerGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 4),
    _TBgpPeerGroupDescription_Type()
)
tBgpPeerGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupDescription.setStatus("current")


class _TBgpPeerGroupConnectRetry_Type(BgpConnectRetryTime):
    """Custom type tBgpPeerGroupConnectRetry based on BgpConnectRetryTime"""
    defaultValue = 120


_TBgpPeerGroupConnectRetry_Type.__name__ = "BgpConnectRetryTime"
_TBgpPeerGroupConnectRetry_Object = MibTableColumn
tBgpPeerGroupConnectRetry = _TBgpPeerGroupConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 5),
    _TBgpPeerGroupConnectRetry_Type()
)
tBgpPeerGroupConnectRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupConnectRetry.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupConnectRetry.setUnits("seconds")


class _TBgpPeerGroupHoldTime_Type(BgpHoldTime):
    """Custom type tBgpPeerGroupHoldTime based on BgpHoldTime"""
    defaultValue = 90


_TBgpPeerGroupHoldTime_Type.__name__ = "BgpHoldTime"
_TBgpPeerGroupHoldTime_Object = MibTableColumn
tBgpPeerGroupHoldTime = _TBgpPeerGroupHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 6),
    _TBgpPeerGroupHoldTime_Type()
)
tBgpPeerGroupHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupHoldTime.setUnits("seconds")


class _TBgpPeerGroupKeepAlive_Type(BgpKeepAliveTime):
    """Custom type tBgpPeerGroupKeepAlive based on BgpKeepAliveTime"""
    defaultValue = 30


_TBgpPeerGroupKeepAlive_Type.__name__ = "BgpKeepAliveTime"
_TBgpPeerGroupKeepAlive_Object = MibTableColumn
tBgpPeerGroupKeepAlive = _TBgpPeerGroupKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 7),
    _TBgpPeerGroupKeepAlive_Type()
)
tBgpPeerGroupKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupKeepAlive.setUnits("seconds")


class _TBgpPeerGroupMinASOrigination_Type(BgpMinASOriginationTime):
    """Custom type tBgpPeerGroupMinASOrigination based on BgpMinASOriginationTime"""
    defaultValue = 15


_TBgpPeerGroupMinASOrigination_Type.__name__ = "BgpMinASOriginationTime"
_TBgpPeerGroupMinASOrigination_Object = MibTableColumn
tBgpPeerGroupMinASOrigination = _TBgpPeerGroupMinASOrigination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 8),
    _TBgpPeerGroupMinASOrigination_Type()
)
tBgpPeerGroupMinASOrigination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMinASOrigination.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerGroupMinASOrigination.setUnits("seconds")


class _TBgpPeerGroupDampening_Type(TruthValue):
    """Custom type tBgpPeerGroupDampening based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupDampening_Type.__name__ = "TruthValue"
_TBgpPeerGroupDampening_Object = MibTableColumn
tBgpPeerGroupDampening = _TBgpPeerGroupDampening_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 9),
    _TBgpPeerGroupDampening_Type()
)
tBgpPeerGroupDampening.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupDampening.setStatus("current")


class _TBgpPeerGroupLocalAddress_Type(IpAddress):
    """Custom type tBgpPeerGroupLocalAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TBgpPeerGroupLocalAddress_Type.__name__ = "IpAddress"
_TBgpPeerGroupLocalAddress_Object = MibTableColumn
tBgpPeerGroupLocalAddress = _TBgpPeerGroupLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 10),
    _TBgpPeerGroupLocalAddress_Type()
)
tBgpPeerGroupLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupLocalAddress.setStatus("obsolete")


class _TBgpPeerGroupLocalAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tBgpPeerGroupLocalAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TBgpPeerGroupLocalAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TBgpPeerGroupLocalAS_Object = MibTableColumn
tBgpPeerGroupLocalAS = _TBgpPeerGroupLocalAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 11),
    _TBgpPeerGroupLocalAS_Type()
)
tBgpPeerGroupLocalAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupLocalAS.setStatus("obsolete")


class _TBgpPeerGroupLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tBgpPeerGroupLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 100


_TBgpPeerGroupLocalPreference_Type.__name__ = "TmnxBgpLocalPreference"
_TBgpPeerGroupLocalPreference_Object = MibTableColumn
tBgpPeerGroupLocalPreference = _TBgpPeerGroupLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 12),
    _TBgpPeerGroupLocalPreference_Type()
)
tBgpPeerGroupLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupLocalPreference.setStatus("current")


class _TBgpPeerGroupLoopDetect_Type(BgpLoopDetect):
    """Custom type tBgpPeerGroupLoopDetect based on BgpLoopDetect"""
    defaultValue = 2


_TBgpPeerGroupLoopDetect_Type.__name__ = "BgpLoopDetect"
_TBgpPeerGroupLoopDetect_Object = MibTableColumn
tBgpPeerGroupLoopDetect = _TBgpPeerGroupLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 13),
    _TBgpPeerGroupLoopDetect_Type()
)
tBgpPeerGroupLoopDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupLoopDetect.setStatus("current")


class _TBgpPeerGroupMinRouteAdvertisement_Type(BgpMinRouteAdvertisement):
    """Custom type tBgpPeerGroupMinRouteAdvertisement based on BgpMinRouteAdvertisement"""
    defaultValue = 30


_TBgpPeerGroupMinRouteAdvertisement_Type.__name__ = "BgpMinRouteAdvertisement"
_TBgpPeerGroupMinRouteAdvertisement_Object = MibTableColumn
tBgpPeerGroupMinRouteAdvertisement = _TBgpPeerGroupMinRouteAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 14),
    _TBgpPeerGroupMinRouteAdvertisement_Type()
)
tBgpPeerGroupMinRouteAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMinRouteAdvertisement.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupMinRouteAdvertisement.setUnits("seconds")


class _TBgpPeerGroupMaxPrefix_Type(BgpPrefixLimit):
    """Custom type tBgpPeerGroupMaxPrefix based on BgpPrefixLimit"""
    defaultValue = 0


_TBgpPeerGroupMaxPrefix_Type.__name__ = "BgpPrefixLimit"
_TBgpPeerGroupMaxPrefix_Object = MibTableColumn
tBgpPeerGroupMaxPrefix = _TBgpPeerGroupMaxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 15),
    _TBgpPeerGroupMaxPrefix_Type()
)
tBgpPeerGroupMaxPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMaxPrefix.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupMaxPrefix.setUnits("number of routes")


class _TBgpPeerGroupMEDSource_Type(BgpMEDSource):
    """Custom type tBgpPeerGroupMEDSource based on BgpMEDSource"""
    defaultValue = 3


_TBgpPeerGroupMEDSource_Type.__name__ = "BgpMEDSource"
_TBgpPeerGroupMEDSource_Object = MibTableColumn
tBgpPeerGroupMEDSource = _TBgpPeerGroupMEDSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 16),
    _TBgpPeerGroupMEDSource_Type()
)
tBgpPeerGroupMEDSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMEDSource.setStatus("current")


class _TBgpPeerGroupMEDValue_Type(BgpMEDValue):
    """Custom type tBgpPeerGroupMEDValue based on BgpMEDValue"""
    defaultValue = 0


_TBgpPeerGroupMEDValue_Type.__name__ = "BgpMEDValue"
_TBgpPeerGroupMEDValue_Object = MibTableColumn
tBgpPeerGroupMEDValue = _TBgpPeerGroupMEDValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 17),
    _TBgpPeerGroupMEDValue_Type()
)
tBgpPeerGroupMEDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMEDValue.setStatus("current")


class _TBgpPeerGroupMultihop_Type(BgpTimeToLive):
    """Custom type tBgpPeerGroupMultihop based on BgpTimeToLive"""
    defaultValue = 0


_TBgpPeerGroupMultihop_Type.__name__ = "BgpTimeToLive"
_TBgpPeerGroupMultihop_Object = MibTableColumn
tBgpPeerGroupMultihop = _TBgpPeerGroupMultihop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 18),
    _TBgpPeerGroupMultihop_Type()
)
tBgpPeerGroupMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMultihop.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupMultihop.setUnits("TTL hops")


class _TBgpPeerGroupNextHopSelf_Type(TruthValue):
    """Custom type tBgpPeerGroupNextHopSelf based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupNextHopSelf_Type.__name__ = "TruthValue"
_TBgpPeerGroupNextHopSelf_Object = MibTableColumn
tBgpPeerGroupNextHopSelf = _TBgpPeerGroupNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 20),
    _TBgpPeerGroupNextHopSelf_Type()
)
tBgpPeerGroupNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupNextHopSelf.setStatus("current")


class _TBgpPeerGroupNoAggregatorID_Type(TruthValue):
    """Custom type tBgpPeerGroupNoAggregatorID based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupNoAggregatorID_Type.__name__ = "TruthValue"
_TBgpPeerGroupNoAggregatorID_Object = MibTableColumn
tBgpPeerGroupNoAggregatorID = _TBgpPeerGroupNoAggregatorID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 21),
    _TBgpPeerGroupNoAggregatorID_Type()
)
tBgpPeerGroupNoAggregatorID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupNoAggregatorID.setStatus("current")


class _TBgpPeerGroupPassive_Type(TruthValue):
    """Custom type tBgpPeerGroupPassive based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupPassive_Type.__name__ = "TruthValue"
_TBgpPeerGroupPassive_Object = MibTableColumn
tBgpPeerGroupPassive = _TBgpPeerGroupPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 22),
    _TBgpPeerGroupPassive_Type()
)
tBgpPeerGroupPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPassive.setStatus("current")


class _TBgpPeerGroupPeerAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tBgpPeerGroupPeerAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TBgpPeerGroupPeerAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TBgpPeerGroupPeerAS_Object = MibTableColumn
tBgpPeerGroupPeerAS = _TBgpPeerGroupPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 23),
    _TBgpPeerGroupPeerAS_Type()
)
tBgpPeerGroupPeerAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPeerAS.setStatus("obsolete")


class _TBgpPeerGroupPeerType_Type(BgpPeerType):
    """Custom type tBgpPeerGroupPeerType based on BgpPeerType"""
    defaultValue = 1


_TBgpPeerGroupPeerType_Type.__name__ = "BgpPeerType"
_TBgpPeerGroupPeerType_Object = MibTableColumn
tBgpPeerGroupPeerType = _TBgpPeerGroupPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 24),
    _TBgpPeerGroupPeerType_Type()
)
tBgpPeerGroupPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPeerType.setStatus("current")


class _TBgpPeerGroupPreference_Type(TmnxBgpPreference):
    """Custom type tBgpPeerGroupPreference based on TmnxBgpPreference"""
    defaultValue = 170

    subtypeSpec = TmnxBgpPreference.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TBgpPeerGroupPreference_Type.__name__ = "TmnxBgpPreference"
_TBgpPeerGroupPreference_Object = MibTableColumn
tBgpPeerGroupPreference = _TBgpPeerGroupPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 25),
    _TBgpPeerGroupPreference_Type()
)
tBgpPeerGroupPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPreference.setStatus("current")


class _TBgpPeerGroupRemovePrivateAS_Type(TruthValue):
    """Custom type tBgpPeerGroupRemovePrivateAS based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupRemovePrivateAS_Type.__name__ = "TruthValue"
_TBgpPeerGroupRemovePrivateAS_Object = MibTableColumn
tBgpPeerGroupRemovePrivateAS = _TBgpPeerGroupRemovePrivateAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 26),
    _TBgpPeerGroupRemovePrivateAS_Type()
)
tBgpPeerGroupRemovePrivateAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupRemovePrivateAS.setStatus("current")
_TBgpPeerGroupLastChanged_Type = TimeStamp
_TBgpPeerGroupLastChanged_Object = MibTableColumn
tBgpPeerGroupLastChanged = _TBgpPeerGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 27),
    _TBgpPeerGroupLastChanged_Type()
)
tBgpPeerGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerGroupLastChanged.setStatus("current")


class _TBgpPeerGroupInheritance_Type(Counter64):
    """Custom type tBgpPeerGroupInheritance based on Counter64"""
    defaultValue = 0


_TBgpPeerGroupInheritance_Type.__name__ = "Counter64"
_TBgpPeerGroupInheritance_Object = MibTableColumn
tBgpPeerGroupInheritance = _TBgpPeerGroupInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 28),
    _TBgpPeerGroupInheritance_Type()
)
tBgpPeerGroupInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupInheritance.setStatus("current")


class _TBgpPeerGroupImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupImportPolicy1_Object = MibTableColumn
tBgpPeerGroupImportPolicy1 = _TBgpPeerGroupImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 30),
    _TBgpPeerGroupImportPolicy1_Type()
)
tBgpPeerGroupImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupImportPolicy1.setStatus("obsolete")


class _TBgpPeerGroupImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupImportPolicy2_Object = MibTableColumn
tBgpPeerGroupImportPolicy2 = _TBgpPeerGroupImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 31),
    _TBgpPeerGroupImportPolicy2_Type()
)
tBgpPeerGroupImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupImportPolicy2.setStatus("obsolete")


class _TBgpPeerGroupImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupImportPolicy3_Object = MibTableColumn
tBgpPeerGroupImportPolicy3 = _TBgpPeerGroupImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 32),
    _TBgpPeerGroupImportPolicy3_Type()
)
tBgpPeerGroupImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupImportPolicy3.setStatus("obsolete")


class _TBgpPeerGroupImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupImportPolicy4_Object = MibTableColumn
tBgpPeerGroupImportPolicy4 = _TBgpPeerGroupImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 33),
    _TBgpPeerGroupImportPolicy4_Type()
)
tBgpPeerGroupImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupImportPolicy4.setStatus("obsolete")


class _TBgpPeerGroupImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupImportPolicy5_Object = MibTableColumn
tBgpPeerGroupImportPolicy5 = _TBgpPeerGroupImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 34),
    _TBgpPeerGroupImportPolicy5_Type()
)
tBgpPeerGroupImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupImportPolicy5.setStatus("obsolete")


class _TBgpPeerGroupExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupExportPolicy1_Object = MibTableColumn
tBgpPeerGroupExportPolicy1 = _TBgpPeerGroupExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 35),
    _TBgpPeerGroupExportPolicy1_Type()
)
tBgpPeerGroupExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupExportPolicy1.setStatus("obsolete")


class _TBgpPeerGroupExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupExportPolicy2_Object = MibTableColumn
tBgpPeerGroupExportPolicy2 = _TBgpPeerGroupExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 36),
    _TBgpPeerGroupExportPolicy2_Type()
)
tBgpPeerGroupExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupExportPolicy2.setStatus("obsolete")


class _TBgpPeerGroupExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupExportPolicy3_Object = MibTableColumn
tBgpPeerGroupExportPolicy3 = _TBgpPeerGroupExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 37),
    _TBgpPeerGroupExportPolicy3_Type()
)
tBgpPeerGroupExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupExportPolicy3.setStatus("obsolete")


class _TBgpPeerGroupExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupExportPolicy4_Object = MibTableColumn
tBgpPeerGroupExportPolicy4 = _TBgpPeerGroupExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 38),
    _TBgpPeerGroupExportPolicy4_Type()
)
tBgpPeerGroupExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupExportPolicy4.setStatus("obsolete")


class _TBgpPeerGroupExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupExportPolicy5_Object = MibTableColumn
tBgpPeerGroupExportPolicy5 = _TBgpPeerGroupExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 39),
    _TBgpPeerGroupExportPolicy5_Type()
)
tBgpPeerGroupExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupExportPolicy5.setStatus("obsolete")
_TBgpPeerGroupOperStatus_Type = BgpOperState
_TBgpPeerGroupOperStatus_Object = MibTableColumn
tBgpPeerGroupOperStatus = _TBgpPeerGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 40),
    _TBgpPeerGroupOperStatus_Type()
)
tBgpPeerGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerGroupOperStatus.setStatus("current")


class _TBgpPeerGroupLocalASPrivate_Type(TruthValue):
    """Custom type tBgpPeerGroupLocalASPrivate based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupLocalASPrivate_Type.__name__ = "TruthValue"
_TBgpPeerGroupLocalASPrivate_Object = MibTableColumn
tBgpPeerGroupLocalASPrivate = _TBgpPeerGroupLocalASPrivate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 41),
    _TBgpPeerGroupLocalASPrivate_Type()
)
tBgpPeerGroupLocalASPrivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupLocalASPrivate.setStatus("current")


class _TBgpPeerGroupMd5Auth_Type(TruthValue):
    """Custom type tBgpPeerGroupMd5Auth based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupMd5Auth_Type.__name__ = "TruthValue"
_TBgpPeerGroupMd5Auth_Object = MibTableColumn
tBgpPeerGroupMd5Auth = _TBgpPeerGroupMd5Auth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 42),
    _TBgpPeerGroupMd5Auth_Type()
)
tBgpPeerGroupMd5Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMd5Auth.setStatus("current")


class _TBgpPeerGroupMd5AuthKey_Type(OctetString):
    """Custom type tBgpPeerGroupMd5AuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgpPeerGroupMd5AuthKey_Type.__name__ = "OctetString"
_TBgpPeerGroupMd5AuthKey_Object = MibTableColumn
tBgpPeerGroupMd5AuthKey = _TBgpPeerGroupMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 43),
    _TBgpPeerGroupMd5AuthKey_Type()
)
tBgpPeerGroupMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMd5AuthKey.setStatus("current")


class _TBgpPeerGroupClusterId_Type(IpAddress):
    """Custom type tBgpPeerGroupClusterId based on IpAddress"""
    defaultHexValue = "00000000"


_TBgpPeerGroupClusterId_Type.__name__ = "IpAddress"
_TBgpPeerGroupClusterId_Object = MibTableColumn
tBgpPeerGroupClusterId = _TBgpPeerGroupClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 44),
    _TBgpPeerGroupClusterId_Type()
)
tBgpPeerGroupClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupClusterId.setStatus("current")


class _TBgpPeerGroupDisableClientReflect_Type(TruthValue):
    """Custom type tBgpPeerGroupDisableClientReflect based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupDisableClientReflect_Type.__name__ = "TruthValue"
_TBgpPeerGroupDisableClientReflect_Object = MibTableColumn
tBgpPeerGroupDisableClientReflect = _TBgpPeerGroupDisableClientReflect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 45),
    _TBgpPeerGroupDisableClientReflect_Type()
)
tBgpPeerGroupDisableClientReflect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupDisableClientReflect.setStatus("current")


class _TBgpPeerGroupGracefulRestart_Type(TruthValue):
    """Custom type tBgpPeerGroupGracefulRestart based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupGracefulRestart_Type.__name__ = "TruthValue"
_TBgpPeerGroupGracefulRestart_Object = MibTableColumn
tBgpPeerGroupGracefulRestart = _TBgpPeerGroupGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 46),
    _TBgpPeerGroupGracefulRestart_Type()
)
tBgpPeerGroupGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupGracefulRestart.setStatus("current")


class _TBgpPeerGroupGRRestartTime_Type(Unsigned32):
    """Custom type tBgpPeerGroupGRRestartTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TBgpPeerGroupGRRestartTime_Type.__name__ = "Unsigned32"
_TBgpPeerGroupGRRestartTime_Object = MibTableColumn
tBgpPeerGroupGRRestartTime = _TBgpPeerGroupGRRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 47),
    _TBgpPeerGroupGRRestartTime_Type()
)
tBgpPeerGroupGRRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupGRRestartTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupGRRestartTime.setUnits("seconds")


class _TBgpPeerGroupGRStaleRoute_Type(Unsigned32):
    """Custom type tBgpPeerGroupGRStaleRoute based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TBgpPeerGroupGRStaleRoute_Type.__name__ = "Unsigned32"
_TBgpPeerGroupGRStaleRoute_Object = MibTableColumn
tBgpPeerGroupGRStaleRoute = _TBgpPeerGroupGRStaleRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 48),
    _TBgpPeerGroupGRStaleRoute_Type()
)
tBgpPeerGroupGRStaleRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupGRStaleRoute.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupGRStaleRoute.setUnits("seconds")


class _TBgpPeerGroupGRAdminState_Type(TmnxAdminState):
    """Custom type tBgpPeerGroupGRAdminState based on TmnxAdminState"""
    defaultValue = 2


_TBgpPeerGroupGRAdminState_Type.__name__ = "TmnxAdminState"
_TBgpPeerGroupGRAdminState_Object = MibTableColumn
tBgpPeerGroupGRAdminState = _TBgpPeerGroupGRAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 49),
    _TBgpPeerGroupGRAdminState_Type()
)
tBgpPeerGroupGRAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupGRAdminState.setStatus("current")
_TBgpPeerGroupGROperState_Type = TmnxOperState
_TBgpPeerGroupGROperState_Object = MibTableColumn
tBgpPeerGroupGROperState = _TBgpPeerGroupGROperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 50),
    _TBgpPeerGroupGROperState_Type()
)
tBgpPeerGroupGROperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerGroupGROperState.setStatus("current")


class _TBgpPeerGroupFamily_Type(TmnxIpFamily):
    """Custom type tBgpPeerGroupFamily based on TmnxIpFamily"""
    defaultBinValue = "01"


_TBgpPeerGroupFamily_Type.__name__ = "TmnxIpFamily"
_TBgpPeerGroupFamily_Object = MibTableColumn
tBgpPeerGroupFamily = _TBgpPeerGroupFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 51),
    _TBgpPeerGroupFamily_Type()
)
tBgpPeerGroupFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupFamily.setStatus("current")


class _TBgpPeerGroupVpnApplyImport_Type(TruthValue):
    """Custom type tBgpPeerGroupVpnApplyImport based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupVpnApplyImport_Type.__name__ = "TruthValue"
_TBgpPeerGroupVpnApplyImport_Object = MibTableColumn
tBgpPeerGroupVpnApplyImport = _TBgpPeerGroupVpnApplyImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 52),
    _TBgpPeerGroupVpnApplyImport_Type()
)
tBgpPeerGroupVpnApplyImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupVpnApplyImport.setStatus("current")


class _TBgpPeerGroupVpnApplyExport_Type(TruthValue):
    """Custom type tBgpPeerGroupVpnApplyExport based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupVpnApplyExport_Type.__name__ = "TruthValue"
_TBgpPeerGroupVpnApplyExport_Object = MibTableColumn
tBgpPeerGroupVpnApplyExport = _TBgpPeerGroupVpnApplyExport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 53),
    _TBgpPeerGroupVpnApplyExport_Type()
)
tBgpPeerGroupVpnApplyExport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupVpnApplyExport.setStatus("current")


class _TBgpPeerGroupASOverride_Type(TruthValue):
    """Custom type tBgpPeerGroupASOverride based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupASOverride_Type.__name__ = "TruthValue"
_TBgpPeerGroupASOverride_Object = MibTableColumn
tBgpPeerGroupASOverride = _TBgpPeerGroupASOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 54),
    _TBgpPeerGroupASOverride_Type()
)
tBgpPeerGroupASOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupASOverride.setStatus("current")


class _TBgpPeerGroupOrf_Type(TruthValue):
    """Custom type tBgpPeerGroupOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupOrf_Type.__name__ = "TruthValue"
_TBgpPeerGroupOrf_Object = MibTableColumn
tBgpPeerGroupOrf = _TBgpPeerGroupOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 55),
    _TBgpPeerGroupOrf_Type()
)
tBgpPeerGroupOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupOrf.setStatus("current")


class _TBgpPeerGroupExtCommsOrf_Type(TruthValue):
    """Custom type tBgpPeerGroupExtCommsOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupExtCommsOrf_Type.__name__ = "TruthValue"
_TBgpPeerGroupExtCommsOrf_Object = MibTableColumn
tBgpPeerGroupExtCommsOrf = _TBgpPeerGroupExtCommsOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 56),
    _TBgpPeerGroupExtCommsOrf_Type()
)
tBgpPeerGroupExtCommsOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupExtCommsOrf.setStatus("current")


class _TBgpPeerGroupExtCommsSendOrf_Type(TruthValue):
    """Custom type tBgpPeerGroupExtCommsSendOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupExtCommsSendOrf_Type.__name__ = "TruthValue"
_TBgpPeerGroupExtCommsSendOrf_Object = MibTableColumn
tBgpPeerGroupExtCommsSendOrf = _TBgpPeerGroupExtCommsSendOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 57),
    _TBgpPeerGroupExtCommsSendOrf_Type()
)
tBgpPeerGroupExtCommsSendOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupExtCommsSendOrf.setStatus("current")


class _TBgpPeerGroupExtCommsRecvOrf_Type(TruthValue):
    """Custom type tBgpPeerGroupExtCommsRecvOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupExtCommsRecvOrf_Type.__name__ = "TruthValue"
_TBgpPeerGroupExtCommsRecvOrf_Object = MibTableColumn
tBgpPeerGroupExtCommsRecvOrf = _TBgpPeerGroupExtCommsRecvOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 58),
    _TBgpPeerGroupExtCommsRecvOrf_Type()
)
tBgpPeerGroupExtCommsRecvOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupExtCommsRecvOrf.setStatus("current")


class _TBgpPeerGroupDynamicPeerGroup_Type(TruthValue):
    """Custom type tBgpPeerGroupDynamicPeerGroup based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupDynamicPeerGroup_Type.__name__ = "TruthValue"
_TBgpPeerGroupDynamicPeerGroup_Object = MibTableColumn
tBgpPeerGroupDynamicPeerGroup = _TBgpPeerGroupDynamicPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 59),
    _TBgpPeerGroupDynamicPeerGroup_Type()
)
tBgpPeerGroupDynamicPeerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupDynamicPeerGroup.setStatus("current")


class _TBgpPeerGroupLocalAS4Byte_Type(InetAutonomousSystemNumber):
    """Custom type tBgpPeerGroupLocalAS4Byte based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TBgpPeerGroupLocalAS4Byte_Type.__name__ = "InetAutonomousSystemNumber"
_TBgpPeerGroupLocalAS4Byte_Object = MibTableColumn
tBgpPeerGroupLocalAS4Byte = _TBgpPeerGroupLocalAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 60),
    _TBgpPeerGroupLocalAS4Byte_Type()
)
tBgpPeerGroupLocalAS4Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupLocalAS4Byte.setStatus("current")


class _TBgpPeerGroupPeerAS4Byte_Type(InetAutonomousSystemNumber):
    """Custom type tBgpPeerGroupPeerAS4Byte based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TBgpPeerGroupPeerAS4Byte_Type.__name__ = "InetAutonomousSystemNumber"
_TBgpPeerGroupPeerAS4Byte_Object = MibTableColumn
tBgpPeerGroupPeerAS4Byte = _TBgpPeerGroupPeerAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 61),
    _TBgpPeerGroupPeerAS4Byte_Type()
)
tBgpPeerGroupPeerAS4Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPeerAS4Byte.setStatus("current")


class _TBgpPeerGroupDisable4ByteASN_Type(TruthValue):
    """Custom type tBgpPeerGroupDisable4ByteASN based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupDisable4ByteASN_Type.__name__ = "TruthValue"
_TBgpPeerGroupDisable4ByteASN_Object = MibTableColumn
tBgpPeerGroupDisable4ByteASN = _TBgpPeerGroupDisable4ByteASN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 62),
    _TBgpPeerGroupDisable4ByteASN_Type()
)
tBgpPeerGroupDisable4ByteASN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupDisable4ByteASN.setStatus("current")


class _TBgpPeerGroupHoldTimeIsStrict_Type(TruthValue):
    """Custom type tBgpPeerGroupHoldTimeIsStrict based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupHoldTimeIsStrict_Type.__name__ = "TruthValue"
_TBgpPeerGroupHoldTimeIsStrict_Object = MibTableColumn
tBgpPeerGroupHoldTimeIsStrict = _TBgpPeerGroupHoldTimeIsStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 63),
    _TBgpPeerGroupHoldTimeIsStrict_Type()
)
tBgpPeerGroupHoldTimeIsStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupHoldTimeIsStrict.setStatus("obsolete")


class _TBgpPeerGroupRemovePrivateASLmtd_Type(TruthValue):
    """Custom type tBgpPeerGroupRemovePrivateASLmtd based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupRemovePrivateASLmtd_Type.__name__ = "TruthValue"
_TBgpPeerGroupRemovePrivateASLmtd_Object = MibTableColumn
tBgpPeerGroupRemovePrivateASLmtd = _TBgpPeerGroupRemovePrivateASLmtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 64),
    _TBgpPeerGroupRemovePrivateASLmtd_Type()
)
tBgpPeerGroupRemovePrivateASLmtd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupRemovePrivateASLmtd.setStatus("current")


class _TBgpPeerGroupPMTUDiscovery_Type(TruthValue):
    """Custom type tBgpPeerGroupPMTUDiscovery based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupPMTUDiscovery_Type.__name__ = "TruthValue"
_TBgpPeerGroupPMTUDiscovery_Object = MibTableColumn
tBgpPeerGroupPMTUDiscovery = _TBgpPeerGroupPMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 65),
    _TBgpPeerGroupPMTUDiscovery_Type()
)
tBgpPeerGroupPMTUDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPMTUDiscovery.setStatus("current")


class _TBgpPeerGroupMaxPrefixLogOnly_Type(TruthValue):
    """Custom type tBgpPeerGroupMaxPrefixLogOnly based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupMaxPrefixLogOnly_Type.__name__ = "TruthValue"
_TBgpPeerGroupMaxPrefixLogOnly_Object = MibTableColumn
tBgpPeerGroupMaxPrefixLogOnly = _TBgpPeerGroupMaxPrefixLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 66),
    _TBgpPeerGroupMaxPrefixLogOnly_Type()
)
tBgpPeerGroupMaxPrefixLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMaxPrefixLogOnly.setStatus("current")


class _TBgpPeerGroupMaxPrefixThreshold_Type(Unsigned32):
    """Custom type tBgpPeerGroupMaxPrefixThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TBgpPeerGroupMaxPrefixThreshold_Type.__name__ = "Unsigned32"
_TBgpPeerGroupMaxPrefixThreshold_Object = MibTableColumn
tBgpPeerGroupMaxPrefixThreshold = _TBgpPeerGroupMaxPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 67),
    _TBgpPeerGroupMaxPrefixThreshold_Type()
)
tBgpPeerGroupMaxPrefixThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupMaxPrefixThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerGroupMaxPrefixThreshold.setUnits("percentage")


class _TBgpPeerGroupDisableCapNego_Type(TruthValue):
    """Custom type tBgpPeerGroupDisableCapNego based on TruthValue"""
    defaultValue = 2


_TBgpPeerGroupDisableCapNego_Type.__name__ = "TruthValue"
_TBgpPeerGroupDisableCapNego_Object = MibTableColumn
tBgpPeerGroupDisableCapNego = _TBgpPeerGroupDisableCapNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 68),
    _TBgpPeerGroupDisableCapNego_Type()
)
tBgpPeerGroupDisableCapNego.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupDisableCapNego.setStatus("current")
_TBgpPeerGroupCreationOrigin_Type = TmnxCreateOrigin
_TBgpPeerGroupCreationOrigin_Object = MibTableColumn
tBgpPeerGroupCreationOrigin = _TBgpPeerGroupCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 3, 1, 69),
    _TBgpPeerGroupCreationOrigin_Type()
)
tBgpPeerGroupCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerGroupCreationOrigin.setStatus("current")
_TBgpPGSendOrfRouteTargetTable_Object = MibTable
tBgpPGSendOrfRouteTargetTable = _TBgpPGSendOrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 4)
)
if mibBuilder.loadTexts:
    tBgpPGSendOrfRouteTargetTable.setStatus("current")
_TBgpPGSendOrfRouteTargetEntry_Object = MibTableRow
tBgpPGSendOrfRouteTargetEntry = _TBgpPGSendOrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 4, 1)
)
tBgpPGSendOrfRouteTargetEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerGroupName"),
    (1, "TIMETRA-BGP-MIB", "tBgpPGSendOrfRouteTarget"),
)
if mibBuilder.loadTexts:
    tBgpPGSendOrfRouteTargetEntry.setStatus("current")
_TBgpPGSendOrfRouteTarget_Type = TNamedItem
_TBgpPGSendOrfRouteTarget_Object = MibTableColumn
tBgpPGSendOrfRouteTarget = _TBgpPGSendOrfRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 4, 1, 1),
    _TBgpPGSendOrfRouteTarget_Type()
)
tBgpPGSendOrfRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpPGSendOrfRouteTarget.setStatus("current")
_TBgpPGSendOrfRTRowStatus_Type = RowStatus
_TBgpPGSendOrfRTRowStatus_Object = MibTableColumn
tBgpPGSendOrfRTRowStatus = _TBgpPGSendOrfRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 4, 1, 2),
    _TBgpPGSendOrfRTRowStatus_Type()
)
tBgpPGSendOrfRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGSendOrfRTRowStatus.setStatus("current")
_TBgpPeerGroupParamsTable_Object = MibTable
tBgpPeerGroupParamsTable = _TBgpPeerGroupParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5)
)
if mibBuilder.loadTexts:
    tBgpPeerGroupParamsTable.setStatus("current")
_TBgpPeerGroupParamsEntry_Object = MibTableRow
tBgpPeerGroupParamsEntry = _TBgpPeerGroupParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1)
)
tBgpPeerGroupParamsEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerGroupName"),
)
if mibBuilder.loadTexts:
    tBgpPeerGroupParamsEntry.setStatus("current")


class _TBgpPGParamsInheritance_Type(Counter64):
    """Custom type tBgpPGParamsInheritance based on Counter64"""
    defaultValue = 0


_TBgpPGParamsInheritance_Type.__name__ = "Counter64"
_TBgpPGParamsInheritance_Object = MibTableColumn
tBgpPGParamsInheritance = _TBgpPGParamsInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 1),
    _TBgpPGParamsInheritance_Type()
)
tBgpPGParamsInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGParamsInheritance.setStatus("current")


class _TBgpPGDisableFEFailover_Type(TruthValue):
    """Custom type tBgpPGDisableFEFailover based on TruthValue"""
    defaultValue = 2


_TBgpPGDisableFEFailover_Type.__name__ = "TruthValue"
_TBgpPGDisableFEFailover_Object = MibTableColumn
tBgpPGDisableFEFailover = _TBgpPGDisableFEFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 2),
    _TBgpPGDisableFEFailover_Type()
)
tBgpPGDisableFEFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDisableFEFailover.setStatus("current")


class _TBgpPGDisableComms_Type(TruthValue):
    """Custom type tBgpPGDisableComms based on TruthValue"""
    defaultValue = 2


_TBgpPGDisableComms_Type.__name__ = "TruthValue"
_TBgpPGDisableComms_Object = MibTableColumn
tBgpPGDisableComms = _TBgpPGDisableComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 3),
    _TBgpPGDisableComms_Type()
)
tBgpPGDisableComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDisableComms.setStatus("current")


class _TBgpPGDisableExtComms_Type(TruthValue):
    """Custom type tBgpPGDisableExtComms based on TruthValue"""
    defaultValue = 2


_TBgpPGDisableExtComms_Type.__name__ = "TruthValue"
_TBgpPGDisableExtComms_Object = MibTableColumn
tBgpPGDisableExtComms = _TBgpPGDisableExtComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 4),
    _TBgpPGDisableExtComms_Type()
)
tBgpPGDisableExtComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDisableExtComms.setStatus("current")


class _TBgpPGDefaultOriginate_Type(TruthValue):
    """Custom type tBgpPGDefaultOriginate based on TruthValue"""
    defaultValue = 2


_TBgpPGDefaultOriginate_Type.__name__ = "TruthValue"
_TBgpPGDefaultOriginate_Object = MibTableColumn
tBgpPGDefaultOriginate = _TBgpPGDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 5),
    _TBgpPGDefaultOriginate_Type()
)
tBgpPGDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDefaultOriginate.setStatus("current")


class _TBgpPGAdvertiseInactiveRts_Type(TruthValue):
    """Custom type tBgpPGAdvertiseInactiveRts based on TruthValue"""
    defaultValue = 2


_TBgpPGAdvertiseInactiveRts_Type.__name__ = "TruthValue"
_TBgpPGAdvertiseInactiveRts_Object = MibTableColumn
tBgpPGAdvertiseInactiveRts = _TBgpPGAdvertiseInactiveRts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 6),
    _TBgpPGAdvertiseInactiveRts_Type()
)
tBgpPGAdvertiseInactiveRts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGAdvertiseInactiveRts.setStatus("current")


class _TBgpPGMinTTLValue_Type(Unsigned32):
    """Custom type tBgpPGMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TBgpPGMinTTLValue_Type.__name__ = "Unsigned32"
_TBgpPGMinTTLValue_Object = MibTableColumn
tBgpPGMinTTLValue = _TBgpPGMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 7),
    _TBgpPGMinTTLValue_Type()
)
tBgpPGMinTTLValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGMinTTLValue.setStatus("current")


class _TBgpPGTTLLogId_Type(TFilterLogId):
    """Custom type tBgpPGTTLLogId based on TFilterLogId"""
    defaultValue = 0


_TBgpPGTTLLogId_Type.__name__ = "TFilterLogId"
_TBgpPGTTLLogId_Object = MibTableColumn
tBgpPGTTLLogId = _TBgpPGTTLLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 8),
    _TBgpPGTTLLogId_Type()
)
tBgpPGTTLLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGTTLLogId.setStatus("current")
_TBgpPGLocalAddressType_Type = InetAddressType
_TBgpPGLocalAddressType_Object = MibTableColumn
tBgpPGLocalAddressType = _TBgpPGLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 9),
    _TBgpPGLocalAddressType_Type()
)
tBgpPGLocalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGLocalAddressType.setStatus("current")


class _TBgpPGLocalAddress_Type(InetAddress):
    """Custom type tBgpPGLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TBgpPGLocalAddress_Type.__name__ = "InetAddress"
_TBgpPGLocalAddress_Object = MibTableColumn
tBgpPGLocalAddress = _TBgpPGLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 10),
    _TBgpPGLocalAddress_Type()
)
tBgpPGLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGLocalAddress.setStatus("current")


class _TBgpPGPeerTracking_Type(TruthValue):
    """Custom type tBgpPGPeerTracking based on TruthValue"""
    defaultValue = 2


_TBgpPGPeerTracking_Type.__name__ = "TruthValue"
_TBgpPGPeerTracking_Object = MibTableColumn
tBgpPGPeerTracking = _TBgpPGPeerTracking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 11),
    _TBgpPGPeerTracking_Type()
)
tBgpPGPeerTracking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGPeerTracking.setStatus("current")


class _TBgpPGAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tBgpPGAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TBgpPGAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TBgpPGAuthKeyChain_Object = MibTableColumn
tBgpPGAuthKeyChain = _TBgpPGAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 12),
    _TBgpPGAuthKeyChain_Type()
)
tBgpPGAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGAuthKeyChain.setStatus("current")


class _TBgpPGBfdEnabled_Type(TruthValue):
    """Custom type tBgpPGBfdEnabled based on TruthValue"""
    defaultValue = 2


_TBgpPGBfdEnabled_Type.__name__ = "TruthValue"
_TBgpPGBfdEnabled_Object = MibTableColumn
tBgpPGBfdEnabled = _TBgpPGBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 13),
    _TBgpPGBfdEnabled_Type()
)
tBgpPGBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGBfdEnabled.setStatus("current")


class _TBgpPGEnableAddPath_Type(TruthValue):
    """Custom type tBgpPGEnableAddPath based on TruthValue"""
    defaultValue = 2


_TBgpPGEnableAddPath_Type.__name__ = "TruthValue"
_TBgpPGEnableAddPath_Object = MibTableColumn
tBgpPGEnableAddPath = _TBgpPGEnableAddPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 14),
    _TBgpPGEnableAddPath_Type()
)
tBgpPGEnableAddPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGEnableAddPath.setStatus("current")


class _TBgpPGRecvAddPath_Type(TmnxAddPathAddressFamily):
    """Custom type tBgpPGRecvAddPath based on TmnxAddPathAddressFamily"""
    defaultBinValue = "1"


_TBgpPGRecvAddPath_Type.__name__ = "TmnxAddPathAddressFamily"
_TBgpPGRecvAddPath_Object = MibTableColumn
tBgpPGRecvAddPath = _TBgpPGRecvAddPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 15),
    _TBgpPGRecvAddPath_Type()
)
tBgpPGRecvAddPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGRecvAddPath.setStatus("current")


class _TBgpPGIpv4AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpPGIpv4AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpPGIpv4AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpPGIpv4AddPathLimit_Object = MibTableColumn
tBgpPGIpv4AddPathLimit = _TBgpPGIpv4AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 16),
    _TBgpPGIpv4AddPathLimit_Type()
)
tBgpPGIpv4AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGIpv4AddPathLimit.setStatus("current")


class _TBgpPGVpnIpv4AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpPGVpnIpv4AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpPGVpnIpv4AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpPGVpnIpv4AddPathLimit_Object = MibTableColumn
tBgpPGVpnIpv4AddPathLimit = _TBgpPGVpnIpv4AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 17),
    _TBgpPGVpnIpv4AddPathLimit_Type()
)
tBgpPGVpnIpv4AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGVpnIpv4AddPathLimit.setStatus("current")


class _TBgpPGIpv6AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpPGIpv6AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpPGIpv6AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpPGIpv6AddPathLimit_Object = MibTableColumn
tBgpPGIpv6AddPathLimit = _TBgpPGIpv6AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 18),
    _TBgpPGIpv6AddPathLimit_Type()
)
tBgpPGIpv6AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGIpv6AddPathLimit.setStatus("current")


class _TBgpPGVpnIpv6AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpPGVpnIpv6AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpPGVpnIpv6AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpPGVpnIpv6AddPathLimit_Object = MibTableColumn
tBgpPGVpnIpv6AddPathLimit = _TBgpPGVpnIpv6AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 19),
    _TBgpPGVpnIpv6AddPathLimit_Type()
)
tBgpPGVpnIpv6AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGVpnIpv6AddPathLimit.setStatus("current")


class _TBgpPGFlowspecValidate_Type(TruthValue):
    """Custom type tBgpPGFlowspecValidate based on TruthValue"""
    defaultValue = 2


_TBgpPGFlowspecValidate_Type.__name__ = "TruthValue"
_TBgpPGFlowspecValidate_Object = MibTableColumn
tBgpPGFlowspecValidate = _TBgpPGFlowspecValidate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 20),
    _TBgpPGFlowspecValidate_Type()
)
tBgpPGFlowspecValidate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGFlowspecValidate.setStatus("current")


class _TBgpPGUpdatedErrorHandling_Type(TruthValue):
    """Custom type tBgpPGUpdatedErrorHandling based on TruthValue"""
    defaultValue = 2


_TBgpPGUpdatedErrorHandling_Type.__name__ = "TruthValue"
_TBgpPGUpdatedErrorHandling_Object = MibTableColumn
tBgpPGUpdatedErrorHandling = _TBgpPGUpdatedErrorHandling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 21),
    _TBgpPGUpdatedErrorHandling_Type()
)
tBgpPGUpdatedErrorHandling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGUpdatedErrorHandling.setStatus("obsolete")


class _TBgpPGDefaultRouteTarget_Type(TruthValue):
    """Custom type tBgpPGDefaultRouteTarget based on TruthValue"""
    defaultValue = 2


_TBgpPGDefaultRouteTarget_Type.__name__ = "TruthValue"
_TBgpPGDefaultRouteTarget_Object = MibTableColumn
tBgpPGDefaultRouteTarget = _TBgpPGDefaultRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 22),
    _TBgpPGDefaultRouteTarget_Type()
)
tBgpPGDefaultRouteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDefaultRouteTarget.setStatus("current")


class _TBgpPGAigp_Type(TruthValue):
    """Custom type tBgpPGAigp based on TruthValue"""
    defaultValue = 2


_TBgpPGAigp_Type.__name__ = "TruthValue"
_TBgpPGAigp_Object = MibTableColumn
tBgpPGAigp = _TBgpPGAigp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 23),
    _TBgpPGAigp_Type()
)
tBgpPGAigp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGAigp.setStatus("current")


class _TBgpPGMinHoldTime_Type(BgpHoldTime):
    """Custom type tBgpPGMinHoldTime based on BgpHoldTime"""
    defaultValue = 0


_TBgpPGMinHoldTime_Type.__name__ = "BgpHoldTime"
_TBgpPGMinHoldTime_Object = MibTableColumn
tBgpPGMinHoldTime = _TBgpPGMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 24),
    _TBgpPGMinHoldTime_Type()
)
tBgpPGMinHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGMinHoldTime.setStatus("current")


class _TBgpPGRemovePrivateSkipPeerAs_Type(TruthValue):
    """Custom type tBgpPGRemovePrivateSkipPeerAs based on TruthValue"""
    defaultValue = 2


_TBgpPGRemovePrivateSkipPeerAs_Type.__name__ = "TruthValue"
_TBgpPGRemovePrivateSkipPeerAs_Object = MibTableColumn
tBgpPGRemovePrivateSkipPeerAs = _TBgpPGRemovePrivateSkipPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 25),
    _TBgpPGRemovePrivateSkipPeerAs_Type()
)
tBgpPGRemovePrivateSkipPeerAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGRemovePrivateSkipPeerAs.setStatus("current")


class _TBgpPGLocalASNoPrependGlobalAS_Type(TruthValue):
    """Custom type tBgpPGLocalASNoPrependGlobalAS based on TruthValue"""
    defaultValue = 2


_TBgpPGLocalASNoPrependGlobalAS_Type.__name__ = "TruthValue"
_TBgpPGLocalASNoPrependGlobalAS_Object = MibTableColumn
tBgpPGLocalASNoPrependGlobalAS = _TBgpPGLocalASNoPrependGlobalAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 26),
    _TBgpPGLocalASNoPrependGlobalAS_Type()
)
tBgpPGLocalASNoPrependGlobalAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGLocalASNoPrependGlobalAS.setStatus("current")


class _TBgpPGMaxPrefixIdleTimeOut_Type(Integer32):
    """Custom type tBgpPGMaxPrefixIdleTimeOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1024),
    )


_TBgpPGMaxPrefixIdleTimeOut_Type.__name__ = "Integer32"
_TBgpPGMaxPrefixIdleTimeOut_Object = MibTableColumn
tBgpPGMaxPrefixIdleTimeOut = _TBgpPGMaxPrefixIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 27),
    _TBgpPGMaxPrefixIdleTimeOut_Type()
)
tBgpPGMaxPrefixIdleTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGMaxPrefixIdleTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPGMaxPrefixIdleTimeOut.setUnits("minutes")


class _TBgpPGGRRestartNotification_Type(TruthValue):
    """Custom type tBgpPGGRRestartNotification based on TruthValue"""
    defaultValue = 2


_TBgpPGGRRestartNotification_Type.__name__ = "TruthValue"
_TBgpPGGRRestartNotification_Object = MibTableColumn
tBgpPGGRRestartNotification = _TBgpPGGRRestartNotification_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 28),
    _TBgpPGGRRestartNotification_Type()
)
tBgpPGGRRestartNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGGRRestartNotification.setStatus("current")


class _TBgpPGFaultTolerance_Type(TruthValue):
    """Custom type tBgpPGFaultTolerance based on TruthValue"""
    defaultValue = 2


_TBgpPGFaultTolerance_Type.__name__ = "TruthValue"
_TBgpPGFaultTolerance_Object = MibTableColumn
tBgpPGFaultTolerance = _TBgpPGFaultTolerance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 29),
    _TBgpPGFaultTolerance_Type()
)
tBgpPGFaultTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGFaultTolerance.setStatus("current")


class _TBgpPGDampPeerOscillations_Type(TruthValue):
    """Custom type tBgpPGDampPeerOscillations based on TruthValue"""
    defaultValue = 2


_TBgpPGDampPeerOscillations_Type.__name__ = "TruthValue"
_TBgpPGDampPeerOscillations_Object = MibTableColumn
tBgpPGDampPeerOscillations = _TBgpPGDampPeerOscillations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 30),
    _TBgpPGDampPeerOscillations_Type()
)
tBgpPGDampPeerOscillations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscillations.setStatus("current")


class _TBgpPGDampPeerOscInitialWaitTime_Type(Unsigned32):
    """Custom type tBgpPGDampPeerOscInitialWaitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_TBgpPGDampPeerOscInitialWaitTime_Type.__name__ = "Unsigned32"
_TBgpPGDampPeerOscInitialWaitTime_Object = MibTableColumn
tBgpPGDampPeerOscInitialWaitTime = _TBgpPGDampPeerOscInitialWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 31),
    _TBgpPGDampPeerOscInitialWaitTime_Type()
)
tBgpPGDampPeerOscInitialWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscInitialWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscInitialWaitTime.setUnits("minutes")


class _TBgpPGDampPeerOscSecondWaitTime_Type(Unsigned32):
    """Custom type tBgpPGDampPeerOscSecondWaitTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TBgpPGDampPeerOscSecondWaitTime_Type.__name__ = "Unsigned32"
_TBgpPGDampPeerOscSecondWaitTime_Object = MibTableColumn
tBgpPGDampPeerOscSecondWaitTime = _TBgpPGDampPeerOscSecondWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 32),
    _TBgpPGDampPeerOscSecondWaitTime_Type()
)
tBgpPGDampPeerOscSecondWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscSecondWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscSecondWaitTime.setUnits("minutes")


class _TBgpPGDampPeerOscMaxWaitTime_Type(Unsigned32):
    """Custom type tBgpPGDampPeerOscMaxWaitTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TBgpPGDampPeerOscMaxWaitTime_Type.__name__ = "Unsigned32"
_TBgpPGDampPeerOscMaxWaitTime_Object = MibTableColumn
tBgpPGDampPeerOscMaxWaitTime = _TBgpPGDampPeerOscMaxWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 33),
    _TBgpPGDampPeerOscMaxWaitTime_Type()
)
tBgpPGDampPeerOscMaxWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscMaxWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscMaxWaitTime.setUnits("minutes")


class _TBgpPGDampPeerOscErrorInterval_Type(Unsigned32):
    """Custom type tBgpPGDampPeerOscErrorInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_TBgpPGDampPeerOscErrorInterval_Type.__name__ = "Unsigned32"
_TBgpPGDampPeerOscErrorInterval_Object = MibTableColumn
tBgpPGDampPeerOscErrorInterval = _TBgpPGDampPeerOscErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 34),
    _TBgpPGDampPeerOscErrorInterval_Type()
)
tBgpPGDampPeerOscErrorInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscErrorInterval.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPGDampPeerOscErrorInterval.setUnits("minutes")


class _TBgpPGSplitHorizon_Type(TruthValue):
    """Custom type tBgpPGSplitHorizon based on TruthValue"""
    defaultValue = 2


_TBgpPGSplitHorizon_Type.__name__ = "TruthValue"
_TBgpPGSplitHorizon_Object = MibTableColumn
tBgpPGSplitHorizon = _TBgpPGSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 35),
    _TBgpPGSplitHorizon_Type()
)
tBgpPGSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGSplitHorizon.setStatus("current")


class _TBgpPGNHUnchangedFamily_Type(TmnxIpNhChgFamily):
    """Custom type tBgpPGNHUnchangedFamily based on TmnxIpNhChgFamily"""
    defaultHexValue = ""


_TBgpPGNHUnchangedFamily_Type.__name__ = "TmnxIpNhChgFamily"
_TBgpPGNHUnchangedFamily_Object = MibTableColumn
tBgpPGNHUnchangedFamily = _TBgpPGNHUnchangedFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 36),
    _TBgpPGNHUnchangedFamily_Type()
)
tBgpPGNHUnchangedFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGNHUnchangedFamily.setStatus("current")


class _TBgpPGEnableOriginValidation_Type(TmnxIpFamily):
    """Custom type tBgpPGEnableOriginValidation based on TmnxIpFamily"""
    defaultHexValue = ""


_TBgpPGEnableOriginValidation_Type.__name__ = "TmnxIpFamily"
_TBgpPGEnableOriginValidation_Object = MibTableColumn
tBgpPGEnableOriginValidation = _TBgpPGEnableOriginValidation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 37),
    _TBgpPGEnableOriginValidation_Type()
)
tBgpPGEnableOriginValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGEnableOriginValidation.setStatus("current")


class _TBgpPGThirdPartyNextHop_Type(TruthValue):
    """Custom type tBgpPGThirdPartyNextHop based on TruthValue"""
    defaultValue = 2


_TBgpPGThirdPartyNextHop_Type.__name__ = "TruthValue"
_TBgpPGThirdPartyNextHop_Object = MibTableColumn
tBgpPGThirdPartyNextHop = _TBgpPGThirdPartyNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 5, 1, 38),
    _TBgpPGThirdPartyNextHop_Type()
)
tBgpPGThirdPartyNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPGThirdPartyNextHop.setStatus("current")
_TBgpPeerGroupPlcyTable_Object = MibTable
tBgpPeerGroupPlcyTable = _TBgpPeerGroupPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6)
)
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyTable.setStatus("current")
_TBgpPeerGroupPlcyEntry_Object = MibTableRow
tBgpPeerGroupPlcyEntry = _TBgpPeerGroupPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1)
)
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyEntry.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy1_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy1 = _TBgpPeerGroupPlcyImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 1),
    _TBgpPeerGroupPlcyImportPolicy1_Type()
)
tBgpPeerGroupPlcyImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy1.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy2_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy2 = _TBgpPeerGroupPlcyImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 2),
    _TBgpPeerGroupPlcyImportPolicy2_Type()
)
tBgpPeerGroupPlcyImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy2.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy3_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy3 = _TBgpPeerGroupPlcyImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 3),
    _TBgpPeerGroupPlcyImportPolicy3_Type()
)
tBgpPeerGroupPlcyImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy3.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy4_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy4 = _TBgpPeerGroupPlcyImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 4),
    _TBgpPeerGroupPlcyImportPolicy4_Type()
)
tBgpPeerGroupPlcyImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy4.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy5_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy5 = _TBgpPeerGroupPlcyImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 5),
    _TBgpPeerGroupPlcyImportPolicy5_Type()
)
tBgpPeerGroupPlcyImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy5.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy6_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy6 = _TBgpPeerGroupPlcyImportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 6),
    _TBgpPeerGroupPlcyImportPolicy6_Type()
)
tBgpPeerGroupPlcyImportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy6.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy7_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy7 = _TBgpPeerGroupPlcyImportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 7),
    _TBgpPeerGroupPlcyImportPolicy7_Type()
)
tBgpPeerGroupPlcyImportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy7.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy8_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy8 = _TBgpPeerGroupPlcyImportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 8),
    _TBgpPeerGroupPlcyImportPolicy8_Type()
)
tBgpPeerGroupPlcyImportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy8.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy9_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy9 = _TBgpPeerGroupPlcyImportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 9),
    _TBgpPeerGroupPlcyImportPolicy9_Type()
)
tBgpPeerGroupPlcyImportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy9.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy10_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy10 = _TBgpPeerGroupPlcyImportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 10),
    _TBgpPeerGroupPlcyImportPolicy10_Type()
)
tBgpPeerGroupPlcyImportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy10.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy11_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy11 = _TBgpPeerGroupPlcyImportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 11),
    _TBgpPeerGroupPlcyImportPolicy11_Type()
)
tBgpPeerGroupPlcyImportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy11.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy12_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy12 = _TBgpPeerGroupPlcyImportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 12),
    _TBgpPeerGroupPlcyImportPolicy12_Type()
)
tBgpPeerGroupPlcyImportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy12.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy13_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy13 = _TBgpPeerGroupPlcyImportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 13),
    _TBgpPeerGroupPlcyImportPolicy13_Type()
)
tBgpPeerGroupPlcyImportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy13.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy14_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy14 = _TBgpPeerGroupPlcyImportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 14),
    _TBgpPeerGroupPlcyImportPolicy14_Type()
)
tBgpPeerGroupPlcyImportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy14.setStatus("current")


class _TBgpPeerGroupPlcyImportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyImportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyImportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyImportPolicy15_Object = MibTableColumn
tBgpPeerGroupPlcyImportPolicy15 = _TBgpPeerGroupPlcyImportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 15),
    _TBgpPeerGroupPlcyImportPolicy15_Type()
)
tBgpPeerGroupPlcyImportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyImportPolicy15.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy1_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy1 = _TBgpPeerGroupPlcyExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 16),
    _TBgpPeerGroupPlcyExportPolicy1_Type()
)
tBgpPeerGroupPlcyExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy1.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy2_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy2 = _TBgpPeerGroupPlcyExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 17),
    _TBgpPeerGroupPlcyExportPolicy2_Type()
)
tBgpPeerGroupPlcyExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy2.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy3_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy3 = _TBgpPeerGroupPlcyExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 18),
    _TBgpPeerGroupPlcyExportPolicy3_Type()
)
tBgpPeerGroupPlcyExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy3.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy4_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy4 = _TBgpPeerGroupPlcyExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 19),
    _TBgpPeerGroupPlcyExportPolicy4_Type()
)
tBgpPeerGroupPlcyExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy4.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy5_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy5 = _TBgpPeerGroupPlcyExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 20),
    _TBgpPeerGroupPlcyExportPolicy5_Type()
)
tBgpPeerGroupPlcyExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy5.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy6_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy6 = _TBgpPeerGroupPlcyExportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 21),
    _TBgpPeerGroupPlcyExportPolicy6_Type()
)
tBgpPeerGroupPlcyExportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy6.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy7_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy7 = _TBgpPeerGroupPlcyExportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 22),
    _TBgpPeerGroupPlcyExportPolicy7_Type()
)
tBgpPeerGroupPlcyExportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy7.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy8_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy8 = _TBgpPeerGroupPlcyExportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 23),
    _TBgpPeerGroupPlcyExportPolicy8_Type()
)
tBgpPeerGroupPlcyExportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy8.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy9_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy9 = _TBgpPeerGroupPlcyExportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 24),
    _TBgpPeerGroupPlcyExportPolicy9_Type()
)
tBgpPeerGroupPlcyExportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy9.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy10_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy10 = _TBgpPeerGroupPlcyExportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 25),
    _TBgpPeerGroupPlcyExportPolicy10_Type()
)
tBgpPeerGroupPlcyExportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy10.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy11_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy11 = _TBgpPeerGroupPlcyExportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 26),
    _TBgpPeerGroupPlcyExportPolicy11_Type()
)
tBgpPeerGroupPlcyExportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy11.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy12_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy12 = _TBgpPeerGroupPlcyExportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 27),
    _TBgpPeerGroupPlcyExportPolicy12_Type()
)
tBgpPeerGroupPlcyExportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy12.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy13_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy13 = _TBgpPeerGroupPlcyExportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 28),
    _TBgpPeerGroupPlcyExportPolicy13_Type()
)
tBgpPeerGroupPlcyExportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy13.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy14_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy14 = _TBgpPeerGroupPlcyExportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 29),
    _TBgpPeerGroupPlcyExportPolicy14_Type()
)
tBgpPeerGroupPlcyExportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy14.setStatus("current")


class _TBgpPeerGroupPlcyExportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerGroupPlcyExportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerGroupPlcyExportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerGroupPlcyExportPolicy15_Object = MibTableColumn
tBgpPeerGroupPlcyExportPolicy15 = _TBgpPeerGroupPlcyExportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 3, 6, 1, 30),
    _TBgpPeerGroupPlcyExportPolicy15_Type()
)
tBgpPeerGroupPlcyExportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGroupPlcyExportPolicy15.setStatus("current")
_TBgpPeerObjects_ObjectIdentity = ObjectIdentity
tBgpPeerObjects = _TBgpPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4)
)
_TBgpPeerTableLastChanged_Type = TimeStamp
_TBgpPeerTableLastChanged_Object = MibScalar
tBgpPeerTableLastChanged = _TBgpPeerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 1),
    _TBgpPeerTableLastChanged_Type()
)
tBgpPeerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerTableLastChanged.setStatus("current")


class _TBgpPeerTableSpinlock_Type(TestAndIncr):
    """Custom type tBgpPeerTableSpinlock based on TestAndIncr"""
    defaultValue = 0


_TBgpPeerTableSpinlock_Type.__name__ = "TestAndIncr"
_TBgpPeerTableSpinlock_Object = MibScalar
tBgpPeerTableSpinlock = _TBgpPeerTableSpinlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 2),
    _TBgpPeerTableSpinlock_Type()
)
tBgpPeerTableSpinlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tBgpPeerTableSpinlock.setStatus("current")
_TBgpPeerTable_Object = MibTable
tBgpPeerTable = _TBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3)
)
if mibBuilder.loadTexts:
    tBgpPeerTable.setStatus("obsolete")
_TBgpPeerEntry_Object = MibTableRow
tBgpPeerEntry = _TBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1)
)
tBgpPeerEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerAddress"),
)
if mibBuilder.loadTexts:
    tBgpPeerEntry.setStatus("obsolete")
_TBgpPeerAddress_Type = IpAddress
_TBgpPeerAddress_Object = MibTableColumn
tBgpPeerAddress = _TBgpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 1),
    _TBgpPeerAddress_Type()
)
tBgpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpPeerAddress.setStatus("obsolete")


class _TBgpPeerPeerGroup_Type(BgpPeerGroupNameOrEmpty):
    """Custom type tBgpPeerPeerGroup based on BgpPeerGroupNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPeerGroup_Type.__name__ = "BgpPeerGroupNameOrEmpty"
_TBgpPeerPeerGroup_Object = MibTableColumn
tBgpPeerPeerGroup = _TBgpPeerPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 2),
    _TBgpPeerPeerGroup_Type()
)
tBgpPeerPeerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPeerGroup.setStatus("obsolete")
_TBgpPeerRowStatus_Type = RowStatus
_TBgpPeerRowStatus_Object = MibTableColumn
tBgpPeerRowStatus = _TBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 3),
    _TBgpPeerRowStatus_Type()
)
tBgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerRowStatus.setStatus("obsolete")


class _TBgpPeerShutdown_Type(TruthValue):
    """Custom type tBgpPeerShutdown based on TruthValue"""
    defaultValue = 2


_TBgpPeerShutdown_Type.__name__ = "TruthValue"
_TBgpPeerShutdown_Object = MibTableColumn
tBgpPeerShutdown = _TBgpPeerShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 4),
    _TBgpPeerShutdown_Type()
)
tBgpPeerShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerShutdown.setStatus("obsolete")


class _TBgpPeerDescription_Type(DisplayString):
    """Custom type tBgpPeerDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TBgpPeerDescription_Type.__name__ = "DisplayString"
_TBgpPeerDescription_Object = MibTableColumn
tBgpPeerDescription = _TBgpPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 5),
    _TBgpPeerDescription_Type()
)
tBgpPeerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerDescription.setStatus("obsolete")


class _TBgpPeerConnectRetry_Type(BgpConnectRetryTime):
    """Custom type tBgpPeerConnectRetry based on BgpConnectRetryTime"""
    defaultValue = 120


_TBgpPeerConnectRetry_Type.__name__ = "BgpConnectRetryTime"
_TBgpPeerConnectRetry_Object = MibTableColumn
tBgpPeerConnectRetry = _TBgpPeerConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 6),
    _TBgpPeerConnectRetry_Type()
)
tBgpPeerConnectRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerConnectRetry.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerConnectRetry.setUnits("seconds")


class _TBgpPeerHoldTime_Type(BgpHoldTime):
    """Custom type tBgpPeerHoldTime based on BgpHoldTime"""
    defaultValue = 90


_TBgpPeerHoldTime_Type.__name__ = "BgpHoldTime"
_TBgpPeerHoldTime_Object = MibTableColumn
tBgpPeerHoldTime = _TBgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 7),
    _TBgpPeerHoldTime_Type()
)
tBgpPeerHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerHoldTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerHoldTime.setUnits("seconds")


class _TBgpPeerKeepAlive_Type(BgpKeepAliveTime):
    """Custom type tBgpPeerKeepAlive based on BgpKeepAliveTime"""
    defaultValue = 30


_TBgpPeerKeepAlive_Type.__name__ = "BgpKeepAliveTime"
_TBgpPeerKeepAlive_Object = MibTableColumn
tBgpPeerKeepAlive = _TBgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 8),
    _TBgpPeerKeepAlive_Type()
)
tBgpPeerKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerKeepAlive.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerKeepAlive.setUnits("seconds")


class _TBgpPeerMinASOrigination_Type(BgpMinASOriginationTime):
    """Custom type tBgpPeerMinASOrigination based on BgpMinASOriginationTime"""
    defaultValue = 15


_TBgpPeerMinASOrigination_Type.__name__ = "BgpMinASOriginationTime"
_TBgpPeerMinASOrigination_Object = MibTableColumn
tBgpPeerMinASOrigination = _TBgpPeerMinASOrigination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 9),
    _TBgpPeerMinASOrigination_Type()
)
tBgpPeerMinASOrigination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMinASOrigination.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerMinASOrigination.setUnits("seconds")


class _TBgpPeerDampening_Type(TruthValue):
    """Custom type tBgpPeerDampening based on TruthValue"""
    defaultValue = 2


_TBgpPeerDampening_Type.__name__ = "TruthValue"
_TBgpPeerDampening_Object = MibTableColumn
tBgpPeerDampening = _TBgpPeerDampening_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 10),
    _TBgpPeerDampening_Type()
)
tBgpPeerDampening.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerDampening.setStatus("obsolete")


class _TBgpPeerLocalAddress_Type(IpAddress):
    """Custom type tBgpPeerLocalAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TBgpPeerLocalAddress_Type.__name__ = "IpAddress"
_TBgpPeerLocalAddress_Object = MibTableColumn
tBgpPeerLocalAddress = _TBgpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 11),
    _TBgpPeerLocalAddress_Type()
)
tBgpPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerLocalAddress.setStatus("obsolete")


class _TBgpPeerLocalAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tBgpPeerLocalAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TBgpPeerLocalAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TBgpPeerLocalAS_Object = MibTableColumn
tBgpPeerLocalAS = _TBgpPeerLocalAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 12),
    _TBgpPeerLocalAS_Type()
)
tBgpPeerLocalAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerLocalAS.setStatus("obsolete")


class _TBgpPeerLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tBgpPeerLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 100


_TBgpPeerLocalPreference_Type.__name__ = "TmnxBgpLocalPreference"
_TBgpPeerLocalPreference_Object = MibTableColumn
tBgpPeerLocalPreference = _TBgpPeerLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 13),
    _TBgpPeerLocalPreference_Type()
)
tBgpPeerLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerLocalPreference.setStatus("obsolete")


class _TBgpPeerLoopDetect_Type(BgpLoopDetect):
    """Custom type tBgpPeerLoopDetect based on BgpLoopDetect"""
    defaultValue = 2


_TBgpPeerLoopDetect_Type.__name__ = "BgpLoopDetect"
_TBgpPeerLoopDetect_Object = MibTableColumn
tBgpPeerLoopDetect = _TBgpPeerLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 14),
    _TBgpPeerLoopDetect_Type()
)
tBgpPeerLoopDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerLoopDetect.setStatus("obsolete")


class _TBgpPeerMinRouteAdvertisement_Type(BgpMinRouteAdvertisement):
    """Custom type tBgpPeerMinRouteAdvertisement based on BgpMinRouteAdvertisement"""
    defaultValue = 30


_TBgpPeerMinRouteAdvertisement_Type.__name__ = "BgpMinRouteAdvertisement"
_TBgpPeerMinRouteAdvertisement_Object = MibTableColumn
tBgpPeerMinRouteAdvertisement = _TBgpPeerMinRouteAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 15),
    _TBgpPeerMinRouteAdvertisement_Type()
)
tBgpPeerMinRouteAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMinRouteAdvertisement.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerMinRouteAdvertisement.setUnits("seconds")


class _TBgpPeerMaxPrefix_Type(BgpPrefixLimit):
    """Custom type tBgpPeerMaxPrefix based on BgpPrefixLimit"""
    defaultValue = 0


_TBgpPeerMaxPrefix_Type.__name__ = "BgpPrefixLimit"
_TBgpPeerMaxPrefix_Object = MibTableColumn
tBgpPeerMaxPrefix = _TBgpPeerMaxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 16),
    _TBgpPeerMaxPrefix_Type()
)
tBgpPeerMaxPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMaxPrefix.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerMaxPrefix.setUnits("number of routes")


class _TBgpPeerMEDSource_Type(BgpMEDSource):
    """Custom type tBgpPeerMEDSource based on BgpMEDSource"""
    defaultValue = 3


_TBgpPeerMEDSource_Type.__name__ = "BgpMEDSource"
_TBgpPeerMEDSource_Object = MibTableColumn
tBgpPeerMEDSource = _TBgpPeerMEDSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 17),
    _TBgpPeerMEDSource_Type()
)
tBgpPeerMEDSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMEDSource.setStatus("obsolete")


class _TBgpPeerMEDValue_Type(BgpMEDValue):
    """Custom type tBgpPeerMEDValue based on BgpMEDValue"""
    defaultValue = 0


_TBgpPeerMEDValue_Type.__name__ = "BgpMEDValue"
_TBgpPeerMEDValue_Object = MibTableColumn
tBgpPeerMEDValue = _TBgpPeerMEDValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 18),
    _TBgpPeerMEDValue_Type()
)
tBgpPeerMEDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMEDValue.setStatus("obsolete")


class _TBgpPeerMultihop_Type(BgpTimeToLive):
    """Custom type tBgpPeerMultihop based on BgpTimeToLive"""
    defaultValue = 0


_TBgpPeerMultihop_Type.__name__ = "BgpTimeToLive"
_TBgpPeerMultihop_Object = MibTableColumn
tBgpPeerMultihop = _TBgpPeerMultihop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 19),
    _TBgpPeerMultihop_Type()
)
tBgpPeerMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMultihop.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerMultihop.setUnits("TTL hops")


class _TBgpPeerNextHopSelf_Type(TruthValue):
    """Custom type tBgpPeerNextHopSelf based on TruthValue"""
    defaultValue = 2


_TBgpPeerNextHopSelf_Type.__name__ = "TruthValue"
_TBgpPeerNextHopSelf_Object = MibTableColumn
tBgpPeerNextHopSelf = _TBgpPeerNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 21),
    _TBgpPeerNextHopSelf_Type()
)
tBgpPeerNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNextHopSelf.setStatus("obsolete")


class _TBgpPeerNoAggregatorID_Type(TruthValue):
    """Custom type tBgpPeerNoAggregatorID based on TruthValue"""
    defaultValue = 2


_TBgpPeerNoAggregatorID_Type.__name__ = "TruthValue"
_TBgpPeerNoAggregatorID_Object = MibTableColumn
tBgpPeerNoAggregatorID = _TBgpPeerNoAggregatorID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 22),
    _TBgpPeerNoAggregatorID_Type()
)
tBgpPeerNoAggregatorID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNoAggregatorID.setStatus("obsolete")


class _TBgpPeerPassive_Type(TruthValue):
    """Custom type tBgpPeerPassive based on TruthValue"""
    defaultValue = 2


_TBgpPeerPassive_Type.__name__ = "TruthValue"
_TBgpPeerPassive_Object = MibTableColumn
tBgpPeerPassive = _TBgpPeerPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 23),
    _TBgpPeerPassive_Type()
)
tBgpPeerPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPassive.setStatus("obsolete")


class _TBgpPeerPeerAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tBgpPeerPeerAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TBgpPeerPeerAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TBgpPeerPeerAS_Object = MibTableColumn
tBgpPeerPeerAS = _TBgpPeerPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 24),
    _TBgpPeerPeerAS_Type()
)
tBgpPeerPeerAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPeerAS.setStatus("obsolete")


class _TBgpPeerPeerType_Type(BgpPeerType):
    """Custom type tBgpPeerPeerType based on BgpPeerType"""
    defaultValue = 1


_TBgpPeerPeerType_Type.__name__ = "BgpPeerType"
_TBgpPeerPeerType_Object = MibTableColumn
tBgpPeerPeerType = _TBgpPeerPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 25),
    _TBgpPeerPeerType_Type()
)
tBgpPeerPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPeerType.setStatus("obsolete")


class _TBgpPeerPreference_Type(TmnxBgpPreference):
    """Custom type tBgpPeerPreference based on TmnxBgpPreference"""
    defaultValue = 170

    subtypeSpec = TmnxBgpPreference.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TBgpPeerPreference_Type.__name__ = "TmnxBgpPreference"
_TBgpPeerPreference_Object = MibTableColumn
tBgpPeerPreference = _TBgpPeerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 26),
    _TBgpPeerPreference_Type()
)
tBgpPeerPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPreference.setStatus("obsolete")


class _TBgpPeerRemovePrivateAS_Type(TruthValue):
    """Custom type tBgpPeerRemovePrivateAS based on TruthValue"""
    defaultValue = 2


_TBgpPeerRemovePrivateAS_Type.__name__ = "TruthValue"
_TBgpPeerRemovePrivateAS_Object = MibTableColumn
tBgpPeerRemovePrivateAS = _TBgpPeerRemovePrivateAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 27),
    _TBgpPeerRemovePrivateAS_Type()
)
tBgpPeerRemovePrivateAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerRemovePrivateAS.setStatus("obsolete")
_TBgpPeerLastChanged_Type = TimeStamp
_TBgpPeerLastChanged_Object = MibTableColumn
tBgpPeerLastChanged = _TBgpPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 28),
    _TBgpPeerLastChanged_Type()
)
tBgpPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerLastChanged.setStatus("obsolete")


class _TBgpPeerInheritance_Type(Counter64):
    """Custom type tBgpPeerInheritance based on Counter64"""
    defaultValue = 0


_TBgpPeerInheritance_Type.__name__ = "Counter64"
_TBgpPeerInheritance_Object = MibTableColumn
tBgpPeerInheritance = _TBgpPeerInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 29),
    _TBgpPeerInheritance_Type()
)
tBgpPeerInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerInheritance.setStatus("obsolete")


class _TBgpPeerImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerImportPolicy1_Object = MibTableColumn
tBgpPeerImportPolicy1 = _TBgpPeerImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 30),
    _TBgpPeerImportPolicy1_Type()
)
tBgpPeerImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerImportPolicy1.setStatus("obsolete")


class _TBgpPeerImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerImportPolicy2_Object = MibTableColumn
tBgpPeerImportPolicy2 = _TBgpPeerImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 31),
    _TBgpPeerImportPolicy2_Type()
)
tBgpPeerImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerImportPolicy2.setStatus("obsolete")


class _TBgpPeerImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerImportPolicy3_Object = MibTableColumn
tBgpPeerImportPolicy3 = _TBgpPeerImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 32),
    _TBgpPeerImportPolicy3_Type()
)
tBgpPeerImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerImportPolicy3.setStatus("obsolete")


class _TBgpPeerImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerImportPolicy4_Object = MibTableColumn
tBgpPeerImportPolicy4 = _TBgpPeerImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 33),
    _TBgpPeerImportPolicy4_Type()
)
tBgpPeerImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerImportPolicy4.setStatus("obsolete")


class _TBgpPeerImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerImportPolicy5_Object = MibTableColumn
tBgpPeerImportPolicy5 = _TBgpPeerImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 34),
    _TBgpPeerImportPolicy5_Type()
)
tBgpPeerImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerImportPolicy5.setStatus("obsolete")


class _TBgpPeerExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerExportPolicy1_Object = MibTableColumn
tBgpPeerExportPolicy1 = _TBgpPeerExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 35),
    _TBgpPeerExportPolicy1_Type()
)
tBgpPeerExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerExportPolicy1.setStatus("obsolete")


class _TBgpPeerExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerExportPolicy2_Object = MibTableColumn
tBgpPeerExportPolicy2 = _TBgpPeerExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 36),
    _TBgpPeerExportPolicy2_Type()
)
tBgpPeerExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerExportPolicy2.setStatus("obsolete")


class _TBgpPeerExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerExportPolicy3_Object = MibTableColumn
tBgpPeerExportPolicy3 = _TBgpPeerExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 37),
    _TBgpPeerExportPolicy3_Type()
)
tBgpPeerExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerExportPolicy3.setStatus("obsolete")


class _TBgpPeerExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerExportPolicy4_Object = MibTableColumn
tBgpPeerExportPolicy4 = _TBgpPeerExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 38),
    _TBgpPeerExportPolicy4_Type()
)
tBgpPeerExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerExportPolicy4.setStatus("obsolete")


class _TBgpPeerExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerExportPolicy5_Object = MibTableColumn
tBgpPeerExportPolicy5 = _TBgpPeerExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 39),
    _TBgpPeerExportPolicy5_Type()
)
tBgpPeerExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerExportPolicy5.setStatus("obsolete")
_TBgpPeerOperStatus_Type = BgpOperState
_TBgpPeerOperStatus_Object = MibTableColumn
tBgpPeerOperStatus = _TBgpPeerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 40),
    _TBgpPeerOperStatus_Type()
)
tBgpPeerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperStatus.setStatus("obsolete")


class _TBgpPeerLocalASPrivate_Type(TruthValue):
    """Custom type tBgpPeerLocalASPrivate based on TruthValue"""
    defaultValue = 2


_TBgpPeerLocalASPrivate_Type.__name__ = "TruthValue"
_TBgpPeerLocalASPrivate_Object = MibTableColumn
tBgpPeerLocalASPrivate = _TBgpPeerLocalASPrivate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 41),
    _TBgpPeerLocalASPrivate_Type()
)
tBgpPeerLocalASPrivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerLocalASPrivate.setStatus("obsolete")


class _TBgpPeerMd5Auth_Type(TruthValue):
    """Custom type tBgpPeerMd5Auth based on TruthValue"""
    defaultValue = 2


_TBgpPeerMd5Auth_Type.__name__ = "TruthValue"
_TBgpPeerMd5Auth_Object = MibTableColumn
tBgpPeerMd5Auth = _TBgpPeerMd5Auth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 42),
    _TBgpPeerMd5Auth_Type()
)
tBgpPeerMd5Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMd5Auth.setStatus("obsolete")


class _TBgpPeerMd5AuthKey_Type(OctetString):
    """Custom type tBgpPeerMd5AuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgpPeerMd5AuthKey_Type.__name__ = "OctetString"
_TBgpPeerMd5AuthKey_Object = MibTableColumn
tBgpPeerMd5AuthKey = _TBgpPeerMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 43),
    _TBgpPeerMd5AuthKey_Type()
)
tBgpPeerMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMd5AuthKey.setStatus("obsolete")


class _TBgpPeerClusterId_Type(IpAddress):
    """Custom type tBgpPeerClusterId based on IpAddress"""
    defaultHexValue = "00000000"


_TBgpPeerClusterId_Type.__name__ = "IpAddress"
_TBgpPeerClusterId_Object = MibTableColumn
tBgpPeerClusterId = _TBgpPeerClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 44),
    _TBgpPeerClusterId_Type()
)
tBgpPeerClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerClusterId.setStatus("obsolete")


class _TBgpPeerDisableClientReflect_Type(TruthValue):
    """Custom type tBgpPeerDisableClientReflect based on TruthValue"""
    defaultValue = 2


_TBgpPeerDisableClientReflect_Type.__name__ = "TruthValue"
_TBgpPeerDisableClientReflect_Object = MibTableColumn
tBgpPeerDisableClientReflect = _TBgpPeerDisableClientReflect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 45),
    _TBgpPeerDisableClientReflect_Type()
)
tBgpPeerDisableClientReflect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerDisableClientReflect.setStatus("obsolete")


class _TBgpPeerGracefulRestart_Type(TruthValue):
    """Custom type tBgpPeerGracefulRestart based on TruthValue"""
    defaultValue = 2


_TBgpPeerGracefulRestart_Type.__name__ = "TruthValue"
_TBgpPeerGracefulRestart_Object = MibTableColumn
tBgpPeerGracefulRestart = _TBgpPeerGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 46),
    _TBgpPeerGracefulRestart_Type()
)
tBgpPeerGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGracefulRestart.setStatus("obsolete")


class _TBgpPeerGRRestartTime_Type(Unsigned32):
    """Custom type tBgpPeerGRRestartTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TBgpPeerGRRestartTime_Type.__name__ = "Unsigned32"
_TBgpPeerGRRestartTime_Object = MibTableColumn
tBgpPeerGRRestartTime = _TBgpPeerGRRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 47),
    _TBgpPeerGRRestartTime_Type()
)
tBgpPeerGRRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGRRestartTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerGRRestartTime.setUnits("seconds")


class _TBgpPeerGRStaleRoute_Type(Unsigned32):
    """Custom type tBgpPeerGRStaleRoute based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TBgpPeerGRStaleRoute_Type.__name__ = "Unsigned32"
_TBgpPeerGRStaleRoute_Object = MibTableColumn
tBgpPeerGRStaleRoute = _TBgpPeerGRStaleRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 48),
    _TBgpPeerGRStaleRoute_Type()
)
tBgpPeerGRStaleRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGRStaleRoute.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerGRStaleRoute.setUnits("seconds")


class _TBgpPeerGRAdminState_Type(TmnxAdminState):
    """Custom type tBgpPeerGRAdminState based on TmnxAdminState"""
    defaultValue = 2


_TBgpPeerGRAdminState_Type.__name__ = "TmnxAdminState"
_TBgpPeerGRAdminState_Object = MibTableColumn
tBgpPeerGRAdminState = _TBgpPeerGRAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 49),
    _TBgpPeerGRAdminState_Type()
)
tBgpPeerGRAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerGRAdminState.setStatus("obsolete")
_TBgpPeerGROperState_Type = TmnxOperState
_TBgpPeerGROperState_Object = MibTableColumn
tBgpPeerGROperState = _TBgpPeerGROperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 50),
    _TBgpPeerGROperState_Type()
)
tBgpPeerGROperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerGROperState.setStatus("obsolete")


class _TBgpPeerFamily_Type(TmnxIpFamily):
    """Custom type tBgpPeerFamily based on TmnxIpFamily"""
    defaultBinValue = "01"


_TBgpPeerFamily_Type.__name__ = "TmnxIpFamily"
_TBgpPeerFamily_Object = MibTableColumn
tBgpPeerFamily = _TBgpPeerFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 51),
    _TBgpPeerFamily_Type()
)
tBgpPeerFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerFamily.setStatus("obsolete")
_TBgpPeerVpnRemoteFamily_Type = TmnxIpFamily
_TBgpPeerVpnRemoteFamily_Object = MibTableColumn
tBgpPeerVpnRemoteFamily = _TBgpPeerVpnRemoteFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 52),
    _TBgpPeerVpnRemoteFamily_Type()
)
tBgpPeerVpnRemoteFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerVpnRemoteFamily.setStatus("obsolete")


class _TBgpPeerVpnApplyImport_Type(TruthValue):
    """Custom type tBgpPeerVpnApplyImport based on TruthValue"""
    defaultValue = 2


_TBgpPeerVpnApplyImport_Type.__name__ = "TruthValue"
_TBgpPeerVpnApplyImport_Object = MibTableColumn
tBgpPeerVpnApplyImport = _TBgpPeerVpnApplyImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 53),
    _TBgpPeerVpnApplyImport_Type()
)
tBgpPeerVpnApplyImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerVpnApplyImport.setStatus("obsolete")


class _TBgpPeerVpnApplyExport_Type(TruthValue):
    """Custom type tBgpPeerVpnApplyExport based on TruthValue"""
    defaultValue = 2


_TBgpPeerVpnApplyExport_Type.__name__ = "TruthValue"
_TBgpPeerVpnApplyExport_Object = MibTableColumn
tBgpPeerVpnApplyExport = _TBgpPeerVpnApplyExport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 54),
    _TBgpPeerVpnApplyExport_Type()
)
tBgpPeerVpnApplyExport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerVpnApplyExport.setStatus("obsolete")
_TBgpPeerVpnLocalCaps_Type = TmnxVpnCapability
_TBgpPeerVpnLocalCaps_Object = MibTableColumn
tBgpPeerVpnLocalCaps = _TBgpPeerVpnLocalCaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 55),
    _TBgpPeerVpnLocalCaps_Type()
)
tBgpPeerVpnLocalCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerVpnLocalCaps.setStatus("obsolete")
_TBgpPeerVpnRemoteCaps_Type = TmnxVpnCapability
_TBgpPeerVpnRemoteCaps_Object = MibTableColumn
tBgpPeerVpnRemoteCaps = _TBgpPeerVpnRemoteCaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 56),
    _TBgpPeerVpnRemoteCaps_Type()
)
tBgpPeerVpnRemoteCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerVpnRemoteCaps.setStatus("obsolete")


class _TBgpPeerConnState_Type(Integer32):
    """Custom type tBgpPeerConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_TBgpPeerConnState_Type.__name__ = "Integer32"
_TBgpPeerConnState_Object = MibTableColumn
tBgpPeerConnState = _TBgpPeerConnState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 57),
    _TBgpPeerConnState_Type()
)
tBgpPeerConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerConnState.setStatus("obsolete")


class _TBgpPeerASOverride_Type(TruthValue):
    """Custom type tBgpPeerASOverride based on TruthValue"""
    defaultValue = 2


_TBgpPeerASOverride_Type.__name__ = "TruthValue"
_TBgpPeerASOverride_Object = MibTableColumn
tBgpPeerASOverride = _TBgpPeerASOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 58),
    _TBgpPeerASOverride_Type()
)
tBgpPeerASOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerASOverride.setStatus("obsolete")


class _TBgpPeerOrf_Type(TruthValue):
    """Custom type tBgpPeerOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerOrf_Type.__name__ = "TruthValue"
_TBgpPeerOrf_Object = MibTableColumn
tBgpPeerOrf = _TBgpPeerOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 59),
    _TBgpPeerOrf_Type()
)
tBgpPeerOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerOrf.setStatus("obsolete")


class _TBgpPeerExtCommsOrf_Type(TruthValue):
    """Custom type tBgpPeerExtCommsOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerExtCommsOrf_Type.__name__ = "TruthValue"
_TBgpPeerExtCommsOrf_Object = MibTableColumn
tBgpPeerExtCommsOrf = _TBgpPeerExtCommsOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 60),
    _TBgpPeerExtCommsOrf_Type()
)
tBgpPeerExtCommsOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerExtCommsOrf.setStatus("obsolete")


class _TBgpPeerExtCommsSendOrf_Type(TruthValue):
    """Custom type tBgpPeerExtCommsSendOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerExtCommsSendOrf_Type.__name__ = "TruthValue"
_TBgpPeerExtCommsSendOrf_Object = MibTableColumn
tBgpPeerExtCommsSendOrf = _TBgpPeerExtCommsSendOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 61),
    _TBgpPeerExtCommsSendOrf_Type()
)
tBgpPeerExtCommsSendOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerExtCommsSendOrf.setStatus("obsolete")


class _TBgpPeerExtCommsRecvOrf_Type(TruthValue):
    """Custom type tBgpPeerExtCommsRecvOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerExtCommsRecvOrf_Type.__name__ = "TruthValue"
_TBgpPeerExtCommsRecvOrf_Object = MibTableColumn
tBgpPeerExtCommsRecvOrf = _TBgpPeerExtCommsRecvOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 3, 1, 62),
    _TBgpPeerExtCommsRecvOrf_Type()
)
tBgpPeerExtCommsRecvOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerExtCommsRecvOrf.setStatus("obsolete")
_TBgpPeerOperTable_Object = MibTable
tBgpPeerOperTable = _TBgpPeerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4)
)
if mibBuilder.loadTexts:
    tBgpPeerOperTable.setStatus("obsolete")
_TBgpPeerOperEntry_Object = MibTableRow
tBgpPeerOperEntry = _TBgpPeerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1)
)
if mibBuilder.loadTexts:
    tBgpPeerOperEntry.setStatus("obsolete")
_TBgpPeerOperMsgOctetsRcvd_Type = Counter64
_TBgpPeerOperMsgOctetsRcvd_Object = MibTableColumn
tBgpPeerOperMsgOctetsRcvd = _TBgpPeerOperMsgOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 1),
    _TBgpPeerOperMsgOctetsRcvd_Type()
)
tBgpPeerOperMsgOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperMsgOctetsRcvd.setStatus("obsolete")
_TBgpPeerOperMsgOctetsSent_Type = Counter64
_TBgpPeerOperMsgOctetsSent_Object = MibTableColumn
tBgpPeerOperMsgOctetsSent = _TBgpPeerOperMsgOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 2),
    _TBgpPeerOperMsgOctetsSent_Type()
)
tBgpPeerOperMsgOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperMsgOctetsSent.setStatus("obsolete")
_TBgpPeerOperInputQueueMessages_Type = Gauge32
_TBgpPeerOperInputQueueMessages_Object = MibTableColumn
tBgpPeerOperInputQueueMessages = _TBgpPeerOperInputQueueMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 3),
    _TBgpPeerOperInputQueueMessages_Type()
)
tBgpPeerOperInputQueueMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperInputQueueMessages.setStatus("obsolete")
_TBgpPeerOperOutputQueueMessages_Type = Gauge32
_TBgpPeerOperOutputQueueMessages_Object = MibTableColumn
tBgpPeerOperOutputQueueMessages = _TBgpPeerOperOutputQueueMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 4),
    _TBgpPeerOperOutputQueueMessages_Type()
)
tBgpPeerOperOutputQueueMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperOutputQueueMessages.setStatus("obsolete")
_TBgpPeerOperReceivedPrefixes_Type = Counter32
_TBgpPeerOperReceivedPrefixes_Object = MibTableColumn
tBgpPeerOperReceivedPrefixes = _TBgpPeerOperReceivedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 5),
    _TBgpPeerOperReceivedPrefixes_Type()
)
tBgpPeerOperReceivedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperReceivedPrefixes.setStatus("obsolete")
_TBgpPeerOperSentPrefixes_Type = Counter32
_TBgpPeerOperSentPrefixes_Object = MibTableColumn
tBgpPeerOperSentPrefixes = _TBgpPeerOperSentPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 6),
    _TBgpPeerOperSentPrefixes_Type()
)
tBgpPeerOperSentPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperSentPrefixes.setStatus("obsolete")
_TBgpPeerOperActivePrefixes_Type = Gauge32
_TBgpPeerOperActivePrefixes_Object = MibTableColumn
tBgpPeerOperActivePrefixes = _TBgpPeerOperActivePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 7),
    _TBgpPeerOperActivePrefixes_Type()
)
tBgpPeerOperActivePrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperActivePrefixes.setStatus("obsolete")
_TBgpPeerOperReceivedPaths_Type = Counter32
_TBgpPeerOperReceivedPaths_Object = MibTableColumn
tBgpPeerOperReceivedPaths = _TBgpPeerOperReceivedPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 8),
    _TBgpPeerOperReceivedPaths_Type()
)
tBgpPeerOperReceivedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperReceivedPaths.setStatus("obsolete")
_TBgpPeerOperPathsSuppressedByDamping_Type = Counter32
_TBgpPeerOperPathsSuppressedByDamping_Object = MibTableColumn
tBgpPeerOperPathsSuppressedByDamping = _TBgpPeerOperPathsSuppressedByDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 9),
    _TBgpPeerOperPathsSuppressedByDamping_Type()
)
tBgpPeerOperPathsSuppressedByDamping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperPathsSuppressedByDamping.setStatus("obsolete")
_TBgpPeerOperFlaps_Type = Counter32
_TBgpPeerOperFlaps_Object = MibTableColumn
tBgpPeerOperFlaps = _TBgpPeerOperFlaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 10),
    _TBgpPeerOperFlaps_Type()
)
tBgpPeerOperFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperFlaps.setStatus("obsolete")
_TBgpPeerOperLastState_Type = BgpPeerState
_TBgpPeerOperLastState_Object = MibTableColumn
tBgpPeerOperLastState = _TBgpPeerOperLastState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 11),
    _TBgpPeerOperLastState_Type()
)
tBgpPeerOperLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperLastState.setStatus("obsolete")
_TBgpPeerOperLastEvent_Type = BgpPeerEvent
_TBgpPeerOperLastEvent_Object = MibTableColumn
tBgpPeerOperLastEvent = _TBgpPeerOperLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 12),
    _TBgpPeerOperLastEvent_Type()
)
tBgpPeerOperLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperLastEvent.setStatus("obsolete")
_TBgpPeerOperVpnReceivedPrefixes_Type = Counter32
_TBgpPeerOperVpnReceivedPrefixes_Object = MibTableColumn
tBgpPeerOperVpnReceivedPrefixes = _TBgpPeerOperVpnReceivedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 13),
    _TBgpPeerOperVpnReceivedPrefixes_Type()
)
tBgpPeerOperVpnReceivedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperVpnReceivedPrefixes.setStatus("obsolete")
_TBgpPeerOperVpnSentPrefixes_Type = Counter32
_TBgpPeerOperVpnSentPrefixes_Object = MibTableColumn
tBgpPeerOperVpnSentPrefixes = _TBgpPeerOperVpnSentPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 14),
    _TBgpPeerOperVpnSentPrefixes_Type()
)
tBgpPeerOperVpnSentPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperVpnSentPrefixes.setStatus("obsolete")
_TBgpPeerOperVpnActivePrefixes_Type = Gauge32
_TBgpPeerOperVpnActivePrefixes_Object = MibTableColumn
tBgpPeerOperVpnActivePrefixes = _TBgpPeerOperVpnActivePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 15),
    _TBgpPeerOperVpnActivePrefixes_Type()
)
tBgpPeerOperVpnActivePrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperVpnActivePrefixes.setStatus("obsolete")
_TBgpPeerOperGRSupport_Type = TruthValue
_TBgpPeerOperGRSupport_Object = MibTableColumn
tBgpPeerOperGRSupport = _TBgpPeerOperGRSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 16),
    _TBgpPeerOperGRSupport_Type()
)
tBgpPeerOperGRSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRSupport.setStatus("obsolete")
_TBgpPeerOperGRFamilyRestart_Type = TmnxBGPFamilyType
_TBgpPeerOperGRFamilyRestart_Object = MibTableColumn
tBgpPeerOperGRFamilyRestart = _TBgpPeerOperGRFamilyRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 17),
    _TBgpPeerOperGRFamilyRestart_Type()
)
tBgpPeerOperGRFamilyRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRFamilyRestart.setStatus("obsolete")
_TBgpPeerOperGRFamilyFwding_Type = TmnxBGPFamilyType
_TBgpPeerOperGRFamilyFwding_Object = MibTableColumn
tBgpPeerOperGRFamilyFwding = _TBgpPeerOperGRFamilyFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 18),
    _TBgpPeerOperGRFamilyFwding_Type()
)
tBgpPeerOperGRFamilyFwding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRFamilyFwding.setStatus("obsolete")
_TBgpPeerOperGRFamilyNegotiated_Type = TmnxBGPFamilyType
_TBgpPeerOperGRFamilyNegotiated_Object = MibTableColumn
tBgpPeerOperGRFamilyNegotiated = _TBgpPeerOperGRFamilyNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 19),
    _TBgpPeerOperGRFamilyNegotiated_Type()
)
tBgpPeerOperGRFamilyNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRFamilyNegotiated.setStatus("obsolete")
_TBgpPeerOperGRRecvEOR_Type = TmnxBGPFamilyType
_TBgpPeerOperGRRecvEOR_Object = MibTableColumn
tBgpPeerOperGRRecvEOR = _TBgpPeerOperGRRecvEOR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 20),
    _TBgpPeerOperGRRecvEOR_Type()
)
tBgpPeerOperGRRecvEOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRRecvEOR.setStatus("obsolete")
_TBgpPeerOperGRSendEOR_Type = TmnxBGPFamilyType
_TBgpPeerOperGRSendEOR_Object = MibTableColumn
tBgpPeerOperGRSendEOR = _TBgpPeerOperGRSendEOR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 21),
    _TBgpPeerOperGRSendEOR_Type()
)
tBgpPeerOperGRSendEOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRSendEOR.setStatus("obsolete")
_TBgpPeerOperGRStaleRoutesTime_Type = Unsigned32
_TBgpPeerOperGRStaleRoutesTime_Object = MibTableColumn
tBgpPeerOperGRStaleRoutesTime = _TBgpPeerOperGRStaleRoutesTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 22),
    _TBgpPeerOperGRStaleRoutesTime_Type()
)
tBgpPeerOperGRStaleRoutesTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRStaleRoutesTime.setStatus("obsolete")
_TBgpPeerOperGRRequestRestartTime_Type = Unsigned32
_TBgpPeerOperGRRequestRestartTime_Object = MibTableColumn
tBgpPeerOperGRRequestRestartTime = _TBgpPeerOperGRRequestRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 23),
    _TBgpPeerOperGRRequestRestartTime_Type()
)
tBgpPeerOperGRRequestRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRRequestRestartTime.setStatus("obsolete")


class _TBgpPeerOperGRStatus_Type(Integer32):
    """Custom type tBgpPeerOperGRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("restarting", 2),
          ("restart-complete", 3),
          ("helping", 4))
    )


_TBgpPeerOperGRStatus_Type.__name__ = "Integer32"
_TBgpPeerOperGRStatus_Object = MibTableColumn
tBgpPeerOperGRStatus = _TBgpPeerOperGRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 24),
    _TBgpPeerOperGRStatus_Type()
)
tBgpPeerOperGRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperGRStatus.setStatus("obsolete")
_TBgpPeerOperNumRestarts_Type = Unsigned32
_TBgpPeerOperNumRestarts_Object = MibTableColumn
tBgpPeerOperNumRestarts = _TBgpPeerOperNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 25),
    _TBgpPeerOperNumRestarts_Type()
)
tBgpPeerOperNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperNumRestarts.setStatus("obsolete")
_TBgpPeerOperLastRestartTime_Type = TimeStamp
_TBgpPeerOperLastRestartTime_Object = MibTableColumn
tBgpPeerOperLastRestartTime = _TBgpPeerOperLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 26),
    _TBgpPeerOperLastRestartTime_Type()
)
tBgpPeerOperLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperLastRestartTime.setStatus("obsolete")
_TBgpPeerOperV6ReceivedPrefixes_Type = Counter32
_TBgpPeerOperV6ReceivedPrefixes_Object = MibTableColumn
tBgpPeerOperV6ReceivedPrefixes = _TBgpPeerOperV6ReceivedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 27),
    _TBgpPeerOperV6ReceivedPrefixes_Type()
)
tBgpPeerOperV6ReceivedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperV6ReceivedPrefixes.setStatus("obsolete")
_TBgpPeerOperV6SentPrefixes_Type = Counter32
_TBgpPeerOperV6SentPrefixes_Object = MibTableColumn
tBgpPeerOperV6SentPrefixes = _TBgpPeerOperV6SentPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 28),
    _TBgpPeerOperV6SentPrefixes_Type()
)
tBgpPeerOperV6SentPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperV6SentPrefixes.setStatus("obsolete")
_TBgpPeerOperV6ActivePrefixes_Type = Gauge32
_TBgpPeerOperV6ActivePrefixes_Object = MibTableColumn
tBgpPeerOperV6ActivePrefixes = _TBgpPeerOperV6ActivePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 29),
    _TBgpPeerOperV6ActivePrefixes_Type()
)
tBgpPeerOperV6ActivePrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperV6ActivePrefixes.setStatus("obsolete")
_TBgpPeerOperV6ReceivedPaths_Type = Counter32
_TBgpPeerOperV6ReceivedPaths_Object = MibTableColumn
tBgpPeerOperV6ReceivedPaths = _TBgpPeerOperV6ReceivedPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 30),
    _TBgpPeerOperV6ReceivedPaths_Type()
)
tBgpPeerOperV6ReceivedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperV6ReceivedPaths.setStatus("obsolete")
_TBgpPeerOperV6SuppPathsDamping_Type = Counter32
_TBgpPeerOperV6SuppPathsDamping_Object = MibTableColumn
tBgpPeerOperV6SuppPathsDamping = _TBgpPeerOperV6SuppPathsDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 31),
    _TBgpPeerOperV6SuppPathsDamping_Type()
)
tBgpPeerOperV6SuppPathsDamping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperV6SuppPathsDamping.setStatus("obsolete")
_TBgpPeerOperVpnReceivedPaths_Type = Counter32
_TBgpPeerOperVpnReceivedPaths_Object = MibTableColumn
tBgpPeerOperVpnReceivedPaths = _TBgpPeerOperVpnReceivedPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 4, 1, 32),
    _TBgpPeerOperVpnReceivedPaths_Type()
)
tBgpPeerOperVpnReceivedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerOperVpnReceivedPaths.setStatus("obsolete")
_TBgpPeerSendOrfRouteTargetTable_Object = MibTable
tBgpPeerSendOrfRouteTargetTable = _TBgpPeerSendOrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 5)
)
if mibBuilder.loadTexts:
    tBgpPeerSendOrfRouteTargetTable.setStatus("obsolete")
_TBgpPeerSendOrfRouteTargetEntry_Object = MibTableRow
tBgpPeerSendOrfRouteTargetEntry = _TBgpPeerSendOrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 5, 1)
)
tBgpPeerSendOrfRouteTargetEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerAddress"),
    (1, "TIMETRA-BGP-MIB", "tBgpPeerSendOrfRouteTarget"),
)
if mibBuilder.loadTexts:
    tBgpPeerSendOrfRouteTargetEntry.setStatus("obsolete")
_TBgpPeerSendOrfRouteTarget_Type = TNamedItem
_TBgpPeerSendOrfRouteTarget_Object = MibTableColumn
tBgpPeerSendOrfRouteTarget = _TBgpPeerSendOrfRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 5, 1, 1),
    _TBgpPeerSendOrfRouteTarget_Type()
)
tBgpPeerSendOrfRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpPeerSendOrfRouteTarget.setStatus("obsolete")
_TBgpPeerSendOrfRTRowStatus_Type = RowStatus
_TBgpPeerSendOrfRTRowStatus_Object = MibTableColumn
tBgpPeerSendOrfRTRowStatus = _TBgpPeerSendOrfRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 5, 1, 2),
    _TBgpPeerSendOrfRTRowStatus_Type()
)
tBgpPeerSendOrfRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerSendOrfRTRowStatus.setStatus("obsolete")
_TBgpPeerParamsTable_Object = MibTable
tBgpPeerParamsTable = _TBgpPeerParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6)
)
if mibBuilder.loadTexts:
    tBgpPeerParamsTable.setStatus("obsolete")
_TBgpPeerParamsEntry_Object = MibTableRow
tBgpPeerParamsEntry = _TBgpPeerParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1)
)
tBgpPeerParamsEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerAddress"),
)
if mibBuilder.loadTexts:
    tBgpPeerParamsEntry.setStatus("obsolete")


class _TBgpPeerParamsInheritance_Type(Counter64):
    """Custom type tBgpPeerParamsInheritance based on Counter64"""
    defaultValue = 0


_TBgpPeerParamsInheritance_Type.__name__ = "Counter64"
_TBgpPeerParamsInheritance_Object = MibTableColumn
tBgpPeerParamsInheritance = _TBgpPeerParamsInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1, 1),
    _TBgpPeerParamsInheritance_Type()
)
tBgpPeerParamsInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerParamsInheritance.setStatus("obsolete")


class _TBgpPeerDisableFEFailover_Type(TruthValue):
    """Custom type tBgpPeerDisableFEFailover based on TruthValue"""
    defaultValue = 2


_TBgpPeerDisableFEFailover_Type.__name__ = "TruthValue"
_TBgpPeerDisableFEFailover_Object = MibTableColumn
tBgpPeerDisableFEFailover = _TBgpPeerDisableFEFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1, 2),
    _TBgpPeerDisableFEFailover_Type()
)
tBgpPeerDisableFEFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerDisableFEFailover.setStatus("obsolete")


class _TBgpPeerDisableComms_Type(TruthValue):
    """Custom type tBgpPeerDisableComms based on TruthValue"""
    defaultValue = 2


_TBgpPeerDisableComms_Type.__name__ = "TruthValue"
_TBgpPeerDisableComms_Object = MibTableColumn
tBgpPeerDisableComms = _TBgpPeerDisableComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1, 3),
    _TBgpPeerDisableComms_Type()
)
tBgpPeerDisableComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerDisableComms.setStatus("obsolete")


class _TBgpPeerDisableExtComms_Type(TruthValue):
    """Custom type tBgpPeerDisableExtComms based on TruthValue"""
    defaultValue = 2


_TBgpPeerDisableExtComms_Type.__name__ = "TruthValue"
_TBgpPeerDisableExtComms_Object = MibTableColumn
tBgpPeerDisableExtComms = _TBgpPeerDisableExtComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1, 4),
    _TBgpPeerDisableExtComms_Type()
)
tBgpPeerDisableExtComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerDisableExtComms.setStatus("obsolete")


class _TBgpPeerDefaultOriginate_Type(TruthValue):
    """Custom type tBgpPeerDefaultOriginate based on TruthValue"""
    defaultValue = 2


_TBgpPeerDefaultOriginate_Type.__name__ = "TruthValue"
_TBgpPeerDefaultOriginate_Object = MibTableColumn
tBgpPeerDefaultOriginate = _TBgpPeerDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1, 5),
    _TBgpPeerDefaultOriginate_Type()
)
tBgpPeerDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerDefaultOriginate.setStatus("obsolete")


class _TBgpPeerAdvertiseInactiveRts_Type(TruthValue):
    """Custom type tBgpPeerAdvertiseInactiveRts based on TruthValue"""
    defaultValue = 2


_TBgpPeerAdvertiseInactiveRts_Type.__name__ = "TruthValue"
_TBgpPeerAdvertiseInactiveRts_Object = MibTableColumn
tBgpPeerAdvertiseInactiveRts = _TBgpPeerAdvertiseInactiveRts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1, 6),
    _TBgpPeerAdvertiseInactiveRts_Type()
)
tBgpPeerAdvertiseInactiveRts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerAdvertiseInactiveRts.setStatus("obsolete")


class _TBgpPeerMinTTLValue_Type(Unsigned32):
    """Custom type tBgpPeerMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TBgpPeerMinTTLValue_Type.__name__ = "Unsigned32"
_TBgpPeerMinTTLValue_Object = MibTableColumn
tBgpPeerMinTTLValue = _TBgpPeerMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1, 7),
    _TBgpPeerMinTTLValue_Type()
)
tBgpPeerMinTTLValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerMinTTLValue.setStatus("obsolete")


class _TBgpPeerTTLLogId_Type(TFilterLogId):
    """Custom type tBgpPeerTTLLogId based on TFilterLogId"""
    defaultValue = 0


_TBgpPeerTTLLogId_Type.__name__ = "TFilterLogId"
_TBgpPeerTTLLogId_Object = MibTableColumn
tBgpPeerTTLLogId = _TBgpPeerTTLLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 6, 1, 8),
    _TBgpPeerTTLLogId_Type()
)
tBgpPeerTTLLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerTTLLogId.setStatus("obsolete")
_TBgpPeerNgTable_Object = MibTable
tBgpPeerNgTable = _TBgpPeerNgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7)
)
if mibBuilder.loadTexts:
    tBgpPeerNgTable.setStatus("current")
_TBgpPeerNgEntry_Object = MibTableRow
tBgpPeerNgEntry = _TBgpPeerNgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1)
)
tBgpPeerNgEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgAddressType"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgAddress"),
)
if mibBuilder.loadTexts:
    tBgpPeerNgEntry.setStatus("current")
_TBgpPeerNgInstanceIndex_Type = TmnxVRtrID
_TBgpPeerNgInstanceIndex_Object = MibTableColumn
tBgpPeerNgInstanceIndex = _TBgpPeerNgInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 1),
    _TBgpPeerNgInstanceIndex_Type()
)
tBgpPeerNgInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpPeerNgInstanceIndex.setStatus("current")
_TBgpPeerNgAddressType_Type = InetAddressType
_TBgpPeerNgAddressType_Object = MibTableColumn
tBgpPeerNgAddressType = _TBgpPeerNgAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 2),
    _TBgpPeerNgAddressType_Type()
)
tBgpPeerNgAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpPeerNgAddressType.setStatus("current")


class _TBgpPeerNgAddress_Type(InetAddress):
    """Custom type tBgpPeerNgAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_TBgpPeerNgAddress_Type.__name__ = "InetAddress"
_TBgpPeerNgAddress_Object = MibTableColumn
tBgpPeerNgAddress = _TBgpPeerNgAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 3),
    _TBgpPeerNgAddress_Type()
)
tBgpPeerNgAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpPeerNgAddress.setStatus("current")


class _TBgpPeerNgPeerGroup_Type(BgpPeerGroupNameOrEmpty):
    """Custom type tBgpPeerNgPeerGroup based on BgpPeerGroupNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgPeerGroup_Type.__name__ = "BgpPeerGroupNameOrEmpty"
_TBgpPeerNgPeerGroup_Object = MibTableColumn
tBgpPeerNgPeerGroup = _TBgpPeerNgPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 4),
    _TBgpPeerNgPeerGroup_Type()
)
tBgpPeerNgPeerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgPeerGroup.setStatus("current")
_TBgpPeerNgRowStatus_Type = RowStatus
_TBgpPeerNgRowStatus_Object = MibTableColumn
tBgpPeerNgRowStatus = _TBgpPeerNgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 5),
    _TBgpPeerNgRowStatus_Type()
)
tBgpPeerNgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgRowStatus.setStatus("current")


class _TBgpPeerNgShutdown_Type(TruthValue):
    """Custom type tBgpPeerNgShutdown based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgShutdown_Type.__name__ = "TruthValue"
_TBgpPeerNgShutdown_Object = MibTableColumn
tBgpPeerNgShutdown = _TBgpPeerNgShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 6),
    _TBgpPeerNgShutdown_Type()
)
tBgpPeerNgShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgShutdown.setStatus("current")


class _TBgpPeerNgDescription_Type(DisplayString):
    """Custom type tBgpPeerNgDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TBgpPeerNgDescription_Type.__name__ = "DisplayString"
_TBgpPeerNgDescription_Object = MibTableColumn
tBgpPeerNgDescription = _TBgpPeerNgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 7),
    _TBgpPeerNgDescription_Type()
)
tBgpPeerNgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDescription.setStatus("current")


class _TBgpPeerNgConnectRetry_Type(BgpConnectRetryTime):
    """Custom type tBgpPeerNgConnectRetry based on BgpConnectRetryTime"""
    defaultValue = 120


_TBgpPeerNgConnectRetry_Type.__name__ = "BgpConnectRetryTime"
_TBgpPeerNgConnectRetry_Object = MibTableColumn
tBgpPeerNgConnectRetry = _TBgpPeerNgConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 8),
    _TBgpPeerNgConnectRetry_Type()
)
tBgpPeerNgConnectRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgConnectRetry.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgConnectRetry.setUnits("seconds")


class _TBgpPeerNgHoldTime_Type(BgpHoldTime):
    """Custom type tBgpPeerNgHoldTime based on BgpHoldTime"""
    defaultValue = 90


_TBgpPeerNgHoldTime_Type.__name__ = "BgpHoldTime"
_TBgpPeerNgHoldTime_Object = MibTableColumn
tBgpPeerNgHoldTime = _TBgpPeerNgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 9),
    _TBgpPeerNgHoldTime_Type()
)
tBgpPeerNgHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgHoldTime.setUnits("seconds")


class _TBgpPeerNgKeepAlive_Type(BgpKeepAliveTime):
    """Custom type tBgpPeerNgKeepAlive based on BgpKeepAliveTime"""
    defaultValue = 30


_TBgpPeerNgKeepAlive_Type.__name__ = "BgpKeepAliveTime"
_TBgpPeerNgKeepAlive_Object = MibTableColumn
tBgpPeerNgKeepAlive = _TBgpPeerNgKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 10),
    _TBgpPeerNgKeepAlive_Type()
)
tBgpPeerNgKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgKeepAlive.setUnits("seconds")


class _TBgpPeerNgMinASOrigination_Type(BgpMinASOriginationTime):
    """Custom type tBgpPeerNgMinASOrigination based on BgpMinASOriginationTime"""
    defaultValue = 15


_TBgpPeerNgMinASOrigination_Type.__name__ = "BgpMinASOriginationTime"
_TBgpPeerNgMinASOrigination_Object = MibTableColumn
tBgpPeerNgMinASOrigination = _TBgpPeerNgMinASOrigination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 11),
    _TBgpPeerNgMinASOrigination_Type()
)
tBgpPeerNgMinASOrigination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMinASOrigination.setStatus("obsolete")
if mibBuilder.loadTexts:
    tBgpPeerNgMinASOrigination.setUnits("seconds")


class _TBgpPeerNgDampening_Type(TruthValue):
    """Custom type tBgpPeerNgDampening based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDampening_Type.__name__ = "TruthValue"
_TBgpPeerNgDampening_Object = MibTableColumn
tBgpPeerNgDampening = _TBgpPeerNgDampening_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 12),
    _TBgpPeerNgDampening_Type()
)
tBgpPeerNgDampening.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDampening.setStatus("current")


class _TBgpPeerNgLocalAddress_Type(InetAddress):
    """Custom type tBgpPeerNgLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TBgpPeerNgLocalAddress_Type.__name__ = "InetAddress"
_TBgpPeerNgLocalAddress_Object = MibTableColumn
tBgpPeerNgLocalAddress = _TBgpPeerNgLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 13),
    _TBgpPeerNgLocalAddress_Type()
)
tBgpPeerNgLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgLocalAddress.setStatus("current")
_TBgpPeerNgLocalAddressType_Type = InetAddressType
_TBgpPeerNgLocalAddressType_Object = MibTableColumn
tBgpPeerNgLocalAddressType = _TBgpPeerNgLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 14),
    _TBgpPeerNgLocalAddressType_Type()
)
tBgpPeerNgLocalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgLocalAddressType.setStatus("current")


class _TBgpPeerNgLocalAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tBgpPeerNgLocalAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TBgpPeerNgLocalAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TBgpPeerNgLocalAS_Object = MibTableColumn
tBgpPeerNgLocalAS = _TBgpPeerNgLocalAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 15),
    _TBgpPeerNgLocalAS_Type()
)
tBgpPeerNgLocalAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgLocalAS.setStatus("obsolete")


class _TBgpPeerNgLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tBgpPeerNgLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 100


_TBgpPeerNgLocalPreference_Type.__name__ = "TmnxBgpLocalPreference"
_TBgpPeerNgLocalPreference_Object = MibTableColumn
tBgpPeerNgLocalPreference = _TBgpPeerNgLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 16),
    _TBgpPeerNgLocalPreference_Type()
)
tBgpPeerNgLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgLocalPreference.setStatus("current")


class _TBgpPeerNgLoopDetect_Type(BgpLoopDetect):
    """Custom type tBgpPeerNgLoopDetect based on BgpLoopDetect"""
    defaultValue = 2


_TBgpPeerNgLoopDetect_Type.__name__ = "BgpLoopDetect"
_TBgpPeerNgLoopDetect_Object = MibTableColumn
tBgpPeerNgLoopDetect = _TBgpPeerNgLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 17),
    _TBgpPeerNgLoopDetect_Type()
)
tBgpPeerNgLoopDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgLoopDetect.setStatus("current")


class _TBgpPeerNgMinRouteAdvertisement_Type(BgpMinRouteAdvertisement):
    """Custom type tBgpPeerNgMinRouteAdvertisement based on BgpMinRouteAdvertisement"""
    defaultValue = 30


_TBgpPeerNgMinRouteAdvertisement_Type.__name__ = "BgpMinRouteAdvertisement"
_TBgpPeerNgMinRouteAdvertisement_Object = MibTableColumn
tBgpPeerNgMinRouteAdvertisement = _TBgpPeerNgMinRouteAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 18),
    _TBgpPeerNgMinRouteAdvertisement_Type()
)
tBgpPeerNgMinRouteAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMinRouteAdvertisement.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgMinRouteAdvertisement.setUnits("seconds")


class _TBgpPeerNgMaxPrefix_Type(BgpPrefixLimit):
    """Custom type tBgpPeerNgMaxPrefix based on BgpPrefixLimit"""
    defaultValue = 0


_TBgpPeerNgMaxPrefix_Type.__name__ = "BgpPrefixLimit"
_TBgpPeerNgMaxPrefix_Object = MibTableColumn
tBgpPeerNgMaxPrefix = _TBgpPeerNgMaxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 19),
    _TBgpPeerNgMaxPrefix_Type()
)
tBgpPeerNgMaxPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMaxPrefix.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgMaxPrefix.setUnits("number of routes")


class _TBgpPeerNgMEDSource_Type(BgpMEDSource):
    """Custom type tBgpPeerNgMEDSource based on BgpMEDSource"""
    defaultValue = 3


_TBgpPeerNgMEDSource_Type.__name__ = "BgpMEDSource"
_TBgpPeerNgMEDSource_Object = MibTableColumn
tBgpPeerNgMEDSource = _TBgpPeerNgMEDSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 20),
    _TBgpPeerNgMEDSource_Type()
)
tBgpPeerNgMEDSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMEDSource.setStatus("current")


class _TBgpPeerNgMEDValue_Type(BgpMEDValue):
    """Custom type tBgpPeerNgMEDValue based on BgpMEDValue"""
    defaultValue = 0


_TBgpPeerNgMEDValue_Type.__name__ = "BgpMEDValue"
_TBgpPeerNgMEDValue_Object = MibTableColumn
tBgpPeerNgMEDValue = _TBgpPeerNgMEDValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 21),
    _TBgpPeerNgMEDValue_Type()
)
tBgpPeerNgMEDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMEDValue.setStatus("current")


class _TBgpPeerNgMultihop_Type(BgpTimeToLive):
    """Custom type tBgpPeerNgMultihop based on BgpTimeToLive"""
    defaultValue = 0


_TBgpPeerNgMultihop_Type.__name__ = "BgpTimeToLive"
_TBgpPeerNgMultihop_Object = MibTableColumn
tBgpPeerNgMultihop = _TBgpPeerNgMultihop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 22),
    _TBgpPeerNgMultihop_Type()
)
tBgpPeerNgMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMultihop.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgMultihop.setUnits("TTL hops")


class _TBgpPeerNgNextHopSelf_Type(TruthValue):
    """Custom type tBgpPeerNgNextHopSelf based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgNextHopSelf_Type.__name__ = "TruthValue"
_TBgpPeerNgNextHopSelf_Object = MibTableColumn
tBgpPeerNgNextHopSelf = _TBgpPeerNgNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 23),
    _TBgpPeerNgNextHopSelf_Type()
)
tBgpPeerNgNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgNextHopSelf.setStatus("current")


class _TBgpPeerNgNoAggregatorID_Type(TruthValue):
    """Custom type tBgpPeerNgNoAggregatorID based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgNoAggregatorID_Type.__name__ = "TruthValue"
_TBgpPeerNgNoAggregatorID_Object = MibTableColumn
tBgpPeerNgNoAggregatorID = _TBgpPeerNgNoAggregatorID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 24),
    _TBgpPeerNgNoAggregatorID_Type()
)
tBgpPeerNgNoAggregatorID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgNoAggregatorID.setStatus("current")


class _TBgpPeerNgPassive_Type(TruthValue):
    """Custom type tBgpPeerNgPassive based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgPassive_Type.__name__ = "TruthValue"
_TBgpPeerNgPassive_Object = MibTableColumn
tBgpPeerNgPassive = _TBgpPeerNgPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 25),
    _TBgpPeerNgPassive_Type()
)
tBgpPeerNgPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgPassive.setStatus("current")


class _TBgpPeerNgPeerAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tBgpPeerNgPeerAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TBgpPeerNgPeerAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_TBgpPeerNgPeerAS_Object = MibTableColumn
tBgpPeerNgPeerAS = _TBgpPeerNgPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 26),
    _TBgpPeerNgPeerAS_Type()
)
tBgpPeerNgPeerAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgPeerAS.setStatus("obsolete")


class _TBgpPeerNgPeerType_Type(BgpPeerType):
    """Custom type tBgpPeerNgPeerType based on BgpPeerType"""
    defaultValue = 1


_TBgpPeerNgPeerType_Type.__name__ = "BgpPeerType"
_TBgpPeerNgPeerType_Object = MibTableColumn
tBgpPeerNgPeerType = _TBgpPeerNgPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 27),
    _TBgpPeerNgPeerType_Type()
)
tBgpPeerNgPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgPeerType.setStatus("current")


class _TBgpPeerNgPreference_Type(TmnxBgpPreference):
    """Custom type tBgpPeerNgPreference based on TmnxBgpPreference"""
    defaultValue = 170

    subtypeSpec = TmnxBgpPreference.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TBgpPeerNgPreference_Type.__name__ = "TmnxBgpPreference"
_TBgpPeerNgPreference_Object = MibTableColumn
tBgpPeerNgPreference = _TBgpPeerNgPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 28),
    _TBgpPeerNgPreference_Type()
)
tBgpPeerNgPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgPreference.setStatus("current")


class _TBgpPeerNgRemovePrivateAS_Type(TruthValue):
    """Custom type tBgpPeerNgRemovePrivateAS based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgRemovePrivateAS_Type.__name__ = "TruthValue"
_TBgpPeerNgRemovePrivateAS_Object = MibTableColumn
tBgpPeerNgRemovePrivateAS = _TBgpPeerNgRemovePrivateAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 29),
    _TBgpPeerNgRemovePrivateAS_Type()
)
tBgpPeerNgRemovePrivateAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgRemovePrivateAS.setStatus("current")
_TBgpPeerNgLastChanged_Type = TimeStamp
_TBgpPeerNgLastChanged_Object = MibTableColumn
tBgpPeerNgLastChanged = _TBgpPeerNgLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 30),
    _TBgpPeerNgLastChanged_Type()
)
tBgpPeerNgLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgLastChanged.setStatus("current")


class _TBgpPeerNgInheritance_Type(Counter64):
    """Custom type tBgpPeerNgInheritance based on Counter64"""
    defaultValue = 0


_TBgpPeerNgInheritance_Type.__name__ = "Counter64"
_TBgpPeerNgInheritance_Object = MibTableColumn
tBgpPeerNgInheritance = _TBgpPeerNgInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 31),
    _TBgpPeerNgInheritance_Type()
)
tBgpPeerNgInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgInheritance.setStatus("current")


class _TBgpPeerNgImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgImportPolicy1_Object = MibTableColumn
tBgpPeerNgImportPolicy1 = _TBgpPeerNgImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 32),
    _TBgpPeerNgImportPolicy1_Type()
)
tBgpPeerNgImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgImportPolicy1.setStatus("obsolete")


class _TBgpPeerNgImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgImportPolicy2_Object = MibTableColumn
tBgpPeerNgImportPolicy2 = _TBgpPeerNgImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 33),
    _TBgpPeerNgImportPolicy2_Type()
)
tBgpPeerNgImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgImportPolicy2.setStatus("obsolete")


class _TBgpPeerNgImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgImportPolicy3_Object = MibTableColumn
tBgpPeerNgImportPolicy3 = _TBgpPeerNgImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 34),
    _TBgpPeerNgImportPolicy3_Type()
)
tBgpPeerNgImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgImportPolicy3.setStatus("obsolete")


class _TBgpPeerNgImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgImportPolicy4_Object = MibTableColumn
tBgpPeerNgImportPolicy4 = _TBgpPeerNgImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 35),
    _TBgpPeerNgImportPolicy4_Type()
)
tBgpPeerNgImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgImportPolicy4.setStatus("obsolete")


class _TBgpPeerNgImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgImportPolicy5_Object = MibTableColumn
tBgpPeerNgImportPolicy5 = _TBgpPeerNgImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 36),
    _TBgpPeerNgImportPolicy5_Type()
)
tBgpPeerNgImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgImportPolicy5.setStatus("obsolete")


class _TBgpPeerNgExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgExportPolicy1_Object = MibTableColumn
tBgpPeerNgExportPolicy1 = _TBgpPeerNgExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 37),
    _TBgpPeerNgExportPolicy1_Type()
)
tBgpPeerNgExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgExportPolicy1.setStatus("obsolete")


class _TBgpPeerNgExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgExportPolicy2_Object = MibTableColumn
tBgpPeerNgExportPolicy2 = _TBgpPeerNgExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 38),
    _TBgpPeerNgExportPolicy2_Type()
)
tBgpPeerNgExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgExportPolicy2.setStatus("obsolete")


class _TBgpPeerNgExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgExportPolicy3_Object = MibTableColumn
tBgpPeerNgExportPolicy3 = _TBgpPeerNgExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 39),
    _TBgpPeerNgExportPolicy3_Type()
)
tBgpPeerNgExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgExportPolicy3.setStatus("obsolete")


class _TBgpPeerNgExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgExportPolicy4_Object = MibTableColumn
tBgpPeerNgExportPolicy4 = _TBgpPeerNgExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 40),
    _TBgpPeerNgExportPolicy4_Type()
)
tBgpPeerNgExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgExportPolicy4.setStatus("obsolete")


class _TBgpPeerNgExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerNgExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerNgExportPolicy5_Object = MibTableColumn
tBgpPeerNgExportPolicy5 = _TBgpPeerNgExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 41),
    _TBgpPeerNgExportPolicy5_Type()
)
tBgpPeerNgExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgExportPolicy5.setStatus("obsolete")
_TBgpPeerNgOperStatus_Type = BgpOperState
_TBgpPeerNgOperStatus_Object = MibTableColumn
tBgpPeerNgOperStatus = _TBgpPeerNgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 42),
    _TBgpPeerNgOperStatus_Type()
)
tBgpPeerNgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperStatus.setStatus("current")


class _TBgpPeerNgLocalASPrivate_Type(TruthValue):
    """Custom type tBgpPeerNgLocalASPrivate based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgLocalASPrivate_Type.__name__ = "TruthValue"
_TBgpPeerNgLocalASPrivate_Object = MibTableColumn
tBgpPeerNgLocalASPrivate = _TBgpPeerNgLocalASPrivate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 43),
    _TBgpPeerNgLocalASPrivate_Type()
)
tBgpPeerNgLocalASPrivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgLocalASPrivate.setStatus("current")


class _TBgpPeerNgMd5Auth_Type(TruthValue):
    """Custom type tBgpPeerNgMd5Auth based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgMd5Auth_Type.__name__ = "TruthValue"
_TBgpPeerNgMd5Auth_Object = MibTableColumn
tBgpPeerNgMd5Auth = _TBgpPeerNgMd5Auth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 44),
    _TBgpPeerNgMd5Auth_Type()
)
tBgpPeerNgMd5Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMd5Auth.setStatus("current")


class _TBgpPeerNgMd5AuthKey_Type(OctetString):
    """Custom type tBgpPeerNgMd5AuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgpPeerNgMd5AuthKey_Type.__name__ = "OctetString"
_TBgpPeerNgMd5AuthKey_Object = MibTableColumn
tBgpPeerNgMd5AuthKey = _TBgpPeerNgMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 45),
    _TBgpPeerNgMd5AuthKey_Type()
)
tBgpPeerNgMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMd5AuthKey.setStatus("current")


class _TBgpPeerNgClusterId_Type(IpAddress):
    """Custom type tBgpPeerNgClusterId based on IpAddress"""
    defaultHexValue = "00000000"


_TBgpPeerNgClusterId_Type.__name__ = "IpAddress"
_TBgpPeerNgClusterId_Object = MibTableColumn
tBgpPeerNgClusterId = _TBgpPeerNgClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 46),
    _TBgpPeerNgClusterId_Type()
)
tBgpPeerNgClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgClusterId.setStatus("current")


class _TBgpPeerNgDisableClientReflect_Type(TruthValue):
    """Custom type tBgpPeerNgDisableClientReflect based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDisableClientReflect_Type.__name__ = "TruthValue"
_TBgpPeerNgDisableClientReflect_Object = MibTableColumn
tBgpPeerNgDisableClientReflect = _TBgpPeerNgDisableClientReflect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 47),
    _TBgpPeerNgDisableClientReflect_Type()
)
tBgpPeerNgDisableClientReflect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDisableClientReflect.setStatus("current")


class _TBgpPeerNgGracefulRestart_Type(TruthValue):
    """Custom type tBgpPeerNgGracefulRestart based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgGracefulRestart_Type.__name__ = "TruthValue"
_TBgpPeerNgGracefulRestart_Object = MibTableColumn
tBgpPeerNgGracefulRestart = _TBgpPeerNgGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 48),
    _TBgpPeerNgGracefulRestart_Type()
)
tBgpPeerNgGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgGracefulRestart.setStatus("current")


class _TBgpPeerNgGRRestartTime_Type(Unsigned32):
    """Custom type tBgpPeerNgGRRestartTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TBgpPeerNgGRRestartTime_Type.__name__ = "Unsigned32"
_TBgpPeerNgGRRestartTime_Object = MibTableColumn
tBgpPeerNgGRRestartTime = _TBgpPeerNgGRRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 49),
    _TBgpPeerNgGRRestartTime_Type()
)
tBgpPeerNgGRRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgGRRestartTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgGRRestartTime.setUnits("seconds")


class _TBgpPeerNgGRStaleRoute_Type(Unsigned32):
    """Custom type tBgpPeerNgGRStaleRoute based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TBgpPeerNgGRStaleRoute_Type.__name__ = "Unsigned32"
_TBgpPeerNgGRStaleRoute_Object = MibTableColumn
tBgpPeerNgGRStaleRoute = _TBgpPeerNgGRStaleRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 50),
    _TBgpPeerNgGRStaleRoute_Type()
)
tBgpPeerNgGRStaleRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgGRStaleRoute.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgGRStaleRoute.setUnits("seconds")


class _TBgpPeerNgGRAdminState_Type(TmnxAdminState):
    """Custom type tBgpPeerNgGRAdminState based on TmnxAdminState"""
    defaultValue = 2


_TBgpPeerNgGRAdminState_Type.__name__ = "TmnxAdminState"
_TBgpPeerNgGRAdminState_Object = MibTableColumn
tBgpPeerNgGRAdminState = _TBgpPeerNgGRAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 51),
    _TBgpPeerNgGRAdminState_Type()
)
tBgpPeerNgGRAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgGRAdminState.setStatus("current")
_TBgpPeerNgGROperState_Type = TmnxOperState
_TBgpPeerNgGROperState_Object = MibTableColumn
tBgpPeerNgGROperState = _TBgpPeerNgGROperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 52),
    _TBgpPeerNgGROperState_Type()
)
tBgpPeerNgGROperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgGROperState.setStatus("current")


class _TBgpPeerNgFamily_Type(TmnxIpFamily):
    """Custom type tBgpPeerNgFamily based on TmnxIpFamily"""
    defaultBinValue = "01"


_TBgpPeerNgFamily_Type.__name__ = "TmnxIpFamily"
_TBgpPeerNgFamily_Object = MibTableColumn
tBgpPeerNgFamily = _TBgpPeerNgFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 53),
    _TBgpPeerNgFamily_Type()
)
tBgpPeerNgFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgFamily.setStatus("current")
_TBgpPeerNgVpnRemoteFamily_Type = TmnxIpFamily
_TBgpPeerNgVpnRemoteFamily_Object = MibTableColumn
tBgpPeerNgVpnRemoteFamily = _TBgpPeerNgVpnRemoteFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 54),
    _TBgpPeerNgVpnRemoteFamily_Type()
)
tBgpPeerNgVpnRemoteFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgVpnRemoteFamily.setStatus("current")


class _TBgpPeerNgVpnApplyImport_Type(TruthValue):
    """Custom type tBgpPeerNgVpnApplyImport based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgVpnApplyImport_Type.__name__ = "TruthValue"
_TBgpPeerNgVpnApplyImport_Object = MibTableColumn
tBgpPeerNgVpnApplyImport = _TBgpPeerNgVpnApplyImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 55),
    _TBgpPeerNgVpnApplyImport_Type()
)
tBgpPeerNgVpnApplyImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgVpnApplyImport.setStatus("current")


class _TBgpPeerNgVpnApplyExport_Type(TruthValue):
    """Custom type tBgpPeerNgVpnApplyExport based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgVpnApplyExport_Type.__name__ = "TruthValue"
_TBgpPeerNgVpnApplyExport_Object = MibTableColumn
tBgpPeerNgVpnApplyExport = _TBgpPeerNgVpnApplyExport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 56),
    _TBgpPeerNgVpnApplyExport_Type()
)
tBgpPeerNgVpnApplyExport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgVpnApplyExport.setStatus("current")
_TBgpPeerNgVpnLocalCaps_Type = TmnxVpnCapability
_TBgpPeerNgVpnLocalCaps_Object = MibTableColumn
tBgpPeerNgVpnLocalCaps = _TBgpPeerNgVpnLocalCaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 57),
    _TBgpPeerNgVpnLocalCaps_Type()
)
tBgpPeerNgVpnLocalCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgVpnLocalCaps.setStatus("current")
_TBgpPeerNgVpnRemoteCaps_Type = TmnxVpnCapability
_TBgpPeerNgVpnRemoteCaps_Object = MibTableColumn
tBgpPeerNgVpnRemoteCaps = _TBgpPeerNgVpnRemoteCaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 58),
    _TBgpPeerNgVpnRemoteCaps_Type()
)
tBgpPeerNgVpnRemoteCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgVpnRemoteCaps.setStatus("current")


class _TBgpPeerNgConnState_Type(Integer32):
    """Custom type tBgpPeerNgConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_TBgpPeerNgConnState_Type.__name__ = "Integer32"
_TBgpPeerNgConnState_Object = MibTableColumn
tBgpPeerNgConnState = _TBgpPeerNgConnState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 59),
    _TBgpPeerNgConnState_Type()
)
tBgpPeerNgConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgConnState.setStatus("current")


class _TBgpPeerNgASOverride_Type(TruthValue):
    """Custom type tBgpPeerNgASOverride based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgASOverride_Type.__name__ = "TruthValue"
_TBgpPeerNgASOverride_Object = MibTableColumn
tBgpPeerNgASOverride = _TBgpPeerNgASOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 60),
    _TBgpPeerNgASOverride_Type()
)
tBgpPeerNgASOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgASOverride.setStatus("current")


class _TBgpPeerNgOrf_Type(TruthValue):
    """Custom type tBgpPeerNgOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgOrf_Type.__name__ = "TruthValue"
_TBgpPeerNgOrf_Object = MibTableColumn
tBgpPeerNgOrf = _TBgpPeerNgOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 61),
    _TBgpPeerNgOrf_Type()
)
tBgpPeerNgOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgOrf.setStatus("current")


class _TBgpPeerNgExtCommsOrf_Type(TruthValue):
    """Custom type tBgpPeerNgExtCommsOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgExtCommsOrf_Type.__name__ = "TruthValue"
_TBgpPeerNgExtCommsOrf_Object = MibTableColumn
tBgpPeerNgExtCommsOrf = _TBgpPeerNgExtCommsOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 62),
    _TBgpPeerNgExtCommsOrf_Type()
)
tBgpPeerNgExtCommsOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgExtCommsOrf.setStatus("current")


class _TBgpPeerNgExtCommsSendOrf_Type(TruthValue):
    """Custom type tBgpPeerNgExtCommsSendOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgExtCommsSendOrf_Type.__name__ = "TruthValue"
_TBgpPeerNgExtCommsSendOrf_Object = MibTableColumn
tBgpPeerNgExtCommsSendOrf = _TBgpPeerNgExtCommsSendOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 63),
    _TBgpPeerNgExtCommsSendOrf_Type()
)
tBgpPeerNgExtCommsSendOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgExtCommsSendOrf.setStatus("current")


class _TBgpPeerNgExtCommsRecvOrf_Type(TruthValue):
    """Custom type tBgpPeerNgExtCommsRecvOrf based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgExtCommsRecvOrf_Type.__name__ = "TruthValue"
_TBgpPeerNgExtCommsRecvOrf_Object = MibTableColumn
tBgpPeerNgExtCommsRecvOrf = _TBgpPeerNgExtCommsRecvOrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 64),
    _TBgpPeerNgExtCommsRecvOrf_Type()
)
tBgpPeerNgExtCommsRecvOrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgExtCommsRecvOrf.setStatus("current")


class _TBgpPeerNgLocalAS4Byte_Type(InetAutonomousSystemNumber):
    """Custom type tBgpPeerNgLocalAS4Byte based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TBgpPeerNgLocalAS4Byte_Type.__name__ = "InetAutonomousSystemNumber"
_TBgpPeerNgLocalAS4Byte_Object = MibTableColumn
tBgpPeerNgLocalAS4Byte = _TBgpPeerNgLocalAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 65),
    _TBgpPeerNgLocalAS4Byte_Type()
)
tBgpPeerNgLocalAS4Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgLocalAS4Byte.setStatus("current")


class _TBgpPeerNgPeerAS4Byte_Type(InetAutonomousSystemNumber):
    """Custom type tBgpPeerNgPeerAS4Byte based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TBgpPeerNgPeerAS4Byte_Type.__name__ = "InetAutonomousSystemNumber"
_TBgpPeerNgPeerAS4Byte_Object = MibTableColumn
tBgpPeerNgPeerAS4Byte = _TBgpPeerNgPeerAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 66),
    _TBgpPeerNgPeerAS4Byte_Type()
)
tBgpPeerNgPeerAS4Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgPeerAS4Byte.setStatus("current")


class _TBgpPeerNgDisable4ByteASN_Type(TruthValue):
    """Custom type tBgpPeerNgDisable4ByteASN based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDisable4ByteASN_Type.__name__ = "TruthValue"
_TBgpPeerNgDisable4ByteASN_Object = MibTableColumn
tBgpPeerNgDisable4ByteASN = _TBgpPeerNgDisable4ByteASN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 67),
    _TBgpPeerNgDisable4ByteASN_Type()
)
tBgpPeerNgDisable4ByteASN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDisable4ByteASN.setStatus("current")


class _TBgpPeerNgHoldTimeIsStrict_Type(TruthValue):
    """Custom type tBgpPeerNgHoldTimeIsStrict based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgHoldTimeIsStrict_Type.__name__ = "TruthValue"
_TBgpPeerNgHoldTimeIsStrict_Object = MibTableColumn
tBgpPeerNgHoldTimeIsStrict = _TBgpPeerNgHoldTimeIsStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 68),
    _TBgpPeerNgHoldTimeIsStrict_Type()
)
tBgpPeerNgHoldTimeIsStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgHoldTimeIsStrict.setStatus("obsolete")


class _TBgpPeerNgL2vpnCiscoInterop_Type(TruthValue):
    """Custom type tBgpPeerNgL2vpnCiscoInterop based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgL2vpnCiscoInterop_Type.__name__ = "TruthValue"
_TBgpPeerNgL2vpnCiscoInterop_Object = MibTableColumn
tBgpPeerNgL2vpnCiscoInterop = _TBgpPeerNgL2vpnCiscoInterop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 69),
    _TBgpPeerNgL2vpnCiscoInterop_Type()
)
tBgpPeerNgL2vpnCiscoInterop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgL2vpnCiscoInterop.setStatus("current")


class _TBgpPeerNgRemovePrivateASLmtd_Type(TruthValue):
    """Custom type tBgpPeerNgRemovePrivateASLmtd based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgRemovePrivateASLmtd_Type.__name__ = "TruthValue"
_TBgpPeerNgRemovePrivateASLmtd_Object = MibTableColumn
tBgpPeerNgRemovePrivateASLmtd = _TBgpPeerNgRemovePrivateASLmtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 70),
    _TBgpPeerNgRemovePrivateASLmtd_Type()
)
tBgpPeerNgRemovePrivateASLmtd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgRemovePrivateASLmtd.setStatus("current")


class _TBgpPeerNgMaxPrefixLogOnly_Type(TruthValue):
    """Custom type tBgpPeerNgMaxPrefixLogOnly based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgMaxPrefixLogOnly_Type.__name__ = "TruthValue"
_TBgpPeerNgMaxPrefixLogOnly_Object = MibTableColumn
tBgpPeerNgMaxPrefixLogOnly = _TBgpPeerNgMaxPrefixLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 71),
    _TBgpPeerNgMaxPrefixLogOnly_Type()
)
tBgpPeerNgMaxPrefixLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMaxPrefixLogOnly.setStatus("current")


class _TBgpPeerNgMaxPrefixThreshold_Type(Unsigned32):
    """Custom type tBgpPeerNgMaxPrefixThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TBgpPeerNgMaxPrefixThreshold_Type.__name__ = "Unsigned32"
_TBgpPeerNgMaxPrefixThreshold_Object = MibTableColumn
tBgpPeerNgMaxPrefixThreshold = _TBgpPeerNgMaxPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 72),
    _TBgpPeerNgMaxPrefixThreshold_Type()
)
tBgpPeerNgMaxPrefixThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMaxPrefixThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgMaxPrefixThreshold.setUnits("percentage")


class _TBgpPeerNgDisableCapNegotiation_Type(TruthValue):
    """Custom type tBgpPeerNgDisableCapNegotiation based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDisableCapNegotiation_Type.__name__ = "TruthValue"
_TBgpPeerNgDisableCapNegotiation_Object = MibTableColumn
tBgpPeerNgDisableCapNegotiation = _TBgpPeerNgDisableCapNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 7, 1, 73),
    _TBgpPeerNgDisableCapNegotiation_Type()
)
tBgpPeerNgDisableCapNegotiation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDisableCapNegotiation.setStatus("current")
_TBgpPeerNgOperTable_Object = MibTable
tBgpPeerNgOperTable = _TBgpPeerNgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8)
)
if mibBuilder.loadTexts:
    tBgpPeerNgOperTable.setStatus("current")
_TBgpPeerNgOperEntry_Object = MibTableRow
tBgpPeerNgOperEntry = _TBgpPeerNgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1)
)
if mibBuilder.loadTexts:
    tBgpPeerNgOperEntry.setStatus("current")
_TBgpPeerNgOperMsgOctetsRcvd_Type = Counter64
_TBgpPeerNgOperMsgOctetsRcvd_Object = MibTableColumn
tBgpPeerNgOperMsgOctetsRcvd = _TBgpPeerNgOperMsgOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 1),
    _TBgpPeerNgOperMsgOctetsRcvd_Type()
)
tBgpPeerNgOperMsgOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMsgOctetsRcvd.setStatus("current")
_TBgpPeerNgOperMsgOctetsSent_Type = Counter64
_TBgpPeerNgOperMsgOctetsSent_Object = MibTableColumn
tBgpPeerNgOperMsgOctetsSent = _TBgpPeerNgOperMsgOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 2),
    _TBgpPeerNgOperMsgOctetsSent_Type()
)
tBgpPeerNgOperMsgOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMsgOctetsSent.setStatus("current")
_TBgpPeerNgOperInputQueueMsgs_Type = Gauge32
_TBgpPeerNgOperInputQueueMsgs_Object = MibTableColumn
tBgpPeerNgOperInputQueueMsgs = _TBgpPeerNgOperInputQueueMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 3),
    _TBgpPeerNgOperInputQueueMsgs_Type()
)
tBgpPeerNgOperInputQueueMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperInputQueueMsgs.setStatus("current")
_TBgpPeerNgOperOutputQueueMsgs_Type = Gauge32
_TBgpPeerNgOperOutputQueueMsgs_Object = MibTableColumn
tBgpPeerNgOperOutputQueueMsgs = _TBgpPeerNgOperOutputQueueMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 4),
    _TBgpPeerNgOperOutputQueueMsgs_Type()
)
tBgpPeerNgOperOutputQueueMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperOutputQueueMsgs.setStatus("current")
_TBgpPeerNgOperReceivedPrefixes_Type = Counter32
_TBgpPeerNgOperReceivedPrefixes_Object = MibTableColumn
tBgpPeerNgOperReceivedPrefixes = _TBgpPeerNgOperReceivedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 5),
    _TBgpPeerNgOperReceivedPrefixes_Type()
)
tBgpPeerNgOperReceivedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperReceivedPrefixes.setStatus("current")
_TBgpPeerNgOperSentPrefixes_Type = Counter32
_TBgpPeerNgOperSentPrefixes_Object = MibTableColumn
tBgpPeerNgOperSentPrefixes = _TBgpPeerNgOperSentPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 6),
    _TBgpPeerNgOperSentPrefixes_Type()
)
tBgpPeerNgOperSentPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperSentPrefixes.setStatus("current")
_TBgpPeerNgOperActivePrefixes_Type = Gauge32
_TBgpPeerNgOperActivePrefixes_Object = MibTableColumn
tBgpPeerNgOperActivePrefixes = _TBgpPeerNgOperActivePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 7),
    _TBgpPeerNgOperActivePrefixes_Type()
)
tBgpPeerNgOperActivePrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperActivePrefixes.setStatus("current")
_TBgpPeerNgOperReceivedPaths_Type = Counter32
_TBgpPeerNgOperReceivedPaths_Object = MibTableColumn
tBgpPeerNgOperReceivedPaths = _TBgpPeerNgOperReceivedPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 8),
    _TBgpPeerNgOperReceivedPaths_Type()
)
tBgpPeerNgOperReceivedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperReceivedPaths.setStatus("current")
_TBgpPeerNgOperPathsSupByDamping_Type = Counter32
_TBgpPeerNgOperPathsSupByDamping_Object = MibTableColumn
tBgpPeerNgOperPathsSupByDamping = _TBgpPeerNgOperPathsSupByDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 9),
    _TBgpPeerNgOperPathsSupByDamping_Type()
)
tBgpPeerNgOperPathsSupByDamping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperPathsSupByDamping.setStatus("obsolete")
_TBgpPeerNgOperFlaps_Type = Counter32
_TBgpPeerNgOperFlaps_Object = MibTableColumn
tBgpPeerNgOperFlaps = _TBgpPeerNgOperFlaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 10),
    _TBgpPeerNgOperFlaps_Type()
)
tBgpPeerNgOperFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlaps.setStatus("current")
_TBgpPeerNgOperLastState_Type = BgpPeerState
_TBgpPeerNgOperLastState_Object = MibTableColumn
tBgpPeerNgOperLastState = _TBgpPeerNgOperLastState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 11),
    _TBgpPeerNgOperLastState_Type()
)
tBgpPeerNgOperLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperLastState.setStatus("current")
_TBgpPeerNgOperLastEvent_Type = BgpPeerEvent
_TBgpPeerNgOperLastEvent_Object = MibTableColumn
tBgpPeerNgOperLastEvent = _TBgpPeerNgOperLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 12),
    _TBgpPeerNgOperLastEvent_Type()
)
tBgpPeerNgOperLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperLastEvent.setStatus("current")
_TBgpPeerNgOperVpnRecvPrefixes_Type = Counter32
_TBgpPeerNgOperVpnRecvPrefixes_Object = MibTableColumn
tBgpPeerNgOperVpnRecvPrefixes = _TBgpPeerNgOperVpnRecvPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 13),
    _TBgpPeerNgOperVpnRecvPrefixes_Type()
)
tBgpPeerNgOperVpnRecvPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnRecvPrefixes.setStatus("current")
_TBgpPeerNgOperVpnSentPrefixes_Type = Counter32
_TBgpPeerNgOperVpnSentPrefixes_Object = MibTableColumn
tBgpPeerNgOperVpnSentPrefixes = _TBgpPeerNgOperVpnSentPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 14),
    _TBgpPeerNgOperVpnSentPrefixes_Type()
)
tBgpPeerNgOperVpnSentPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnSentPrefixes.setStatus("current")
_TBgpPeerNgOperVpnActivePrefixes_Type = Gauge32
_TBgpPeerNgOperVpnActivePrefixes_Object = MibTableColumn
tBgpPeerNgOperVpnActivePrefixes = _TBgpPeerNgOperVpnActivePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 15),
    _TBgpPeerNgOperVpnActivePrefixes_Type()
)
tBgpPeerNgOperVpnActivePrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnActivePrefixes.setStatus("current")
_TBgpPeerNgOperGRSupport_Type = TruthValue
_TBgpPeerNgOperGRSupport_Object = MibTableColumn
tBgpPeerNgOperGRSupport = _TBgpPeerNgOperGRSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 16),
    _TBgpPeerNgOperGRSupport_Type()
)
tBgpPeerNgOperGRSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRSupport.setStatus("current")
_TBgpPeerNgOperGRFamilyRestart_Type = TmnxBGPFamilyType
_TBgpPeerNgOperGRFamilyRestart_Object = MibTableColumn
tBgpPeerNgOperGRFamilyRestart = _TBgpPeerNgOperGRFamilyRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 17),
    _TBgpPeerNgOperGRFamilyRestart_Type()
)
tBgpPeerNgOperGRFamilyRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRFamilyRestart.setStatus("current")
_TBgpPeerNgOperGRFamilyFwding_Type = TmnxBGPFamilyType
_TBgpPeerNgOperGRFamilyFwding_Object = MibTableColumn
tBgpPeerNgOperGRFamilyFwding = _TBgpPeerNgOperGRFamilyFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 18),
    _TBgpPeerNgOperGRFamilyFwding_Type()
)
tBgpPeerNgOperGRFamilyFwding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRFamilyFwding.setStatus("current")
_TBgpPeerNgOperGRFamilyNegotiated_Type = TmnxBGPFamilyType
_TBgpPeerNgOperGRFamilyNegotiated_Object = MibTableColumn
tBgpPeerNgOperGRFamilyNegotiated = _TBgpPeerNgOperGRFamilyNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 19),
    _TBgpPeerNgOperGRFamilyNegotiated_Type()
)
tBgpPeerNgOperGRFamilyNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRFamilyNegotiated.setStatus("current")
_TBgpPeerNgOperGRRecvEOR_Type = TmnxBGPFamilyType
_TBgpPeerNgOperGRRecvEOR_Object = MibTableColumn
tBgpPeerNgOperGRRecvEOR = _TBgpPeerNgOperGRRecvEOR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 20),
    _TBgpPeerNgOperGRRecvEOR_Type()
)
tBgpPeerNgOperGRRecvEOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRRecvEOR.setStatus("current")
_TBgpPeerNgOperGRSendEOR_Type = TmnxBGPFamilyType
_TBgpPeerNgOperGRSendEOR_Object = MibTableColumn
tBgpPeerNgOperGRSendEOR = _TBgpPeerNgOperGRSendEOR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 21),
    _TBgpPeerNgOperGRSendEOR_Type()
)
tBgpPeerNgOperGRSendEOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRSendEOR.setStatus("current")
_TBgpPeerNgOperGRStaleRoutesTime_Type = Unsigned32
_TBgpPeerNgOperGRStaleRoutesTime_Object = MibTableColumn
tBgpPeerNgOperGRStaleRoutesTime = _TBgpPeerNgOperGRStaleRoutesTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 22),
    _TBgpPeerNgOperGRStaleRoutesTime_Type()
)
tBgpPeerNgOperGRStaleRoutesTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRStaleRoutesTime.setStatus("current")
_TBgpPeerNgOperGRReqRestartTime_Type = Unsigned32
_TBgpPeerNgOperGRReqRestartTime_Object = MibTableColumn
tBgpPeerNgOperGRReqRestartTime = _TBgpPeerNgOperGRReqRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 23),
    _TBgpPeerNgOperGRReqRestartTime_Type()
)
tBgpPeerNgOperGRReqRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRReqRestartTime.setStatus("current")


class _TBgpPeerNgOperGRStatus_Type(Integer32):
    """Custom type tBgpPeerNgOperGRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("restarting", 2),
          ("restart-complete", 3),
          ("helping", 4))
    )


_TBgpPeerNgOperGRStatus_Type.__name__ = "Integer32"
_TBgpPeerNgOperGRStatus_Object = MibTableColumn
tBgpPeerNgOperGRStatus = _TBgpPeerNgOperGRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 24),
    _TBgpPeerNgOperGRStatus_Type()
)
tBgpPeerNgOperGRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRStatus.setStatus("current")
_TBgpPeerNgOperNumRestarts_Type = Unsigned32
_TBgpPeerNgOperNumRestarts_Object = MibTableColumn
tBgpPeerNgOperNumRestarts = _TBgpPeerNgOperNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 25),
    _TBgpPeerNgOperNumRestarts_Type()
)
tBgpPeerNgOperNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperNumRestarts.setStatus("current")
_TBgpPeerNgOperLastRestartTime_Type = TimeStamp
_TBgpPeerNgOperLastRestartTime_Object = MibTableColumn
tBgpPeerNgOperLastRestartTime = _TBgpPeerNgOperLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 26),
    _TBgpPeerNgOperLastRestartTime_Type()
)
tBgpPeerNgOperLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperLastRestartTime.setStatus("current")
_TBgpPeerNgOperV6ReceivedPrefixes_Type = Counter32
_TBgpPeerNgOperV6ReceivedPrefixes_Object = MibTableColumn
tBgpPeerNgOperV6ReceivedPrefixes = _TBgpPeerNgOperV6ReceivedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 27),
    _TBgpPeerNgOperV6ReceivedPrefixes_Type()
)
tBgpPeerNgOperV6ReceivedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperV6ReceivedPrefixes.setStatus("current")
_TBgpPeerNgOperV6SentPrefixes_Type = Counter32
_TBgpPeerNgOperV6SentPrefixes_Object = MibTableColumn
tBgpPeerNgOperV6SentPrefixes = _TBgpPeerNgOperV6SentPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 28),
    _TBgpPeerNgOperV6SentPrefixes_Type()
)
tBgpPeerNgOperV6SentPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperV6SentPrefixes.setStatus("current")
_TBgpPeerNgOperV6ActivePrefixes_Type = Gauge32
_TBgpPeerNgOperV6ActivePrefixes_Object = MibTableColumn
tBgpPeerNgOperV6ActivePrefixes = _TBgpPeerNgOperV6ActivePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 29),
    _TBgpPeerNgOperV6ActivePrefixes_Type()
)
tBgpPeerNgOperV6ActivePrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperV6ActivePrefixes.setStatus("current")
_TBgpPeerNgOperV6ReceivedPaths_Type = Counter32
_TBgpPeerNgOperV6ReceivedPaths_Object = MibTableColumn
tBgpPeerNgOperV6ReceivedPaths = _TBgpPeerNgOperV6ReceivedPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 30),
    _TBgpPeerNgOperV6ReceivedPaths_Type()
)
tBgpPeerNgOperV6ReceivedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperV6ReceivedPaths.setStatus("obsolete")
_TBgpPeerNgOperV6SuppPathsDamping_Type = Counter32
_TBgpPeerNgOperV6SuppPathsDamping_Object = MibTableColumn
tBgpPeerNgOperV6SuppPathsDamping = _TBgpPeerNgOperV6SuppPathsDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 31),
    _TBgpPeerNgOperV6SuppPathsDamping_Type()
)
tBgpPeerNgOperV6SuppPathsDamping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperV6SuppPathsDamping.setStatus("obsolete")
_TBgpPeerNgOperVpnReceivedPaths_Type = Counter32
_TBgpPeerNgOperVpnReceivedPaths_Object = MibTableColumn
tBgpPeerNgOperVpnReceivedPaths = _TBgpPeerNgOperVpnReceivedPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 32),
    _TBgpPeerNgOperVpnReceivedPaths_Type()
)
tBgpPeerNgOperVpnReceivedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnReceivedPaths.setStatus("obsolete")
_TBgpPeerNgOperV4SuppPfxDamp_Type = Counter32
_TBgpPeerNgOperV4SuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperV4SuppPfxDamp = _TBgpPeerNgOperV4SuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 33),
    _TBgpPeerNgOperV4SuppPfxDamp_Type()
)
tBgpPeerNgOperV4SuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperV4SuppPfxDamp.setStatus("current")
_TBgpPeerNgOperVpnSuppPfxDamp_Type = Counter32
_TBgpPeerNgOperVpnSuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperVpnSuppPfxDamp = _TBgpPeerNgOperVpnSuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 34),
    _TBgpPeerNgOperVpnSuppPfxDamp_Type()
)
tBgpPeerNgOperVpnSuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnSuppPfxDamp.setStatus("current")
_TBgpPeerNgOperV6SuppPfxDamp_Type = Counter32
_TBgpPeerNgOperV6SuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperV6SuppPfxDamp = _TBgpPeerNgOperV6SuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 35),
    _TBgpPeerNgOperV6SuppPfxDamp_Type()
)
tBgpPeerNgOperV6SuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperV6SuppPfxDamp.setStatus("current")
_TBgpPeerNgOperMCastV4SuppPfxDamp_Type = Counter32
_TBgpPeerNgOperMCastV4SuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperMCastV4SuppPfxDamp = _TBgpPeerNgOperMCastV4SuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 36),
    _TBgpPeerNgOperMCastV4SuppPfxDamp_Type()
)
tBgpPeerNgOperMCastV4SuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMCastV4SuppPfxDamp.setStatus("current")
_TBgpPeerNgOperMCastV4RecvPfxs_Type = Counter32
_TBgpPeerNgOperMCastV4RecvPfxs_Object = MibTableColumn
tBgpPeerNgOperMCastV4RecvPfxs = _TBgpPeerNgOperMCastV4RecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 37),
    _TBgpPeerNgOperMCastV4RecvPfxs_Type()
)
tBgpPeerNgOperMCastV4RecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMCastV4RecvPfxs.setStatus("current")
_TBgpPeerNgOperMCastV4SentPfxs_Type = Counter32
_TBgpPeerNgOperMCastV4SentPfxs_Object = MibTableColumn
tBgpPeerNgOperMCastV4SentPfxs = _TBgpPeerNgOperMCastV4SentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 38),
    _TBgpPeerNgOperMCastV4SentPfxs_Type()
)
tBgpPeerNgOperMCastV4SentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMCastV4SentPfxs.setStatus("current")
_TBgpPeerNgOperMCastV4ActivePfxs_Type = Counter32
_TBgpPeerNgOperMCastV4ActivePfxs_Object = MibTableColumn
tBgpPeerNgOperMCastV4ActivePfxs = _TBgpPeerNgOperMCastV4ActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 39),
    _TBgpPeerNgOperMCastV4ActivePfxs_Type()
)
tBgpPeerNgOperMCastV4ActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMCastV4ActivePfxs.setStatus("current")
_TBgpPeerNgOperVpnIpv6RecvPfxs_Type = Counter32
_TBgpPeerNgOperVpnIpv6RecvPfxs_Object = MibTableColumn
tBgpPeerNgOperVpnIpv6RecvPfxs = _TBgpPeerNgOperVpnIpv6RecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 40),
    _TBgpPeerNgOperVpnIpv6RecvPfxs_Type()
)
tBgpPeerNgOperVpnIpv6RecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnIpv6RecvPfxs.setStatus("current")
_TBgpPeerNgOperVpnIpv6SentPfxs_Type = Counter32
_TBgpPeerNgOperVpnIpv6SentPfxs_Object = MibTableColumn
tBgpPeerNgOperVpnIpv6SentPfxs = _TBgpPeerNgOperVpnIpv6SentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 41),
    _TBgpPeerNgOperVpnIpv6SentPfxs_Type()
)
tBgpPeerNgOperVpnIpv6SentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnIpv6SentPfxs.setStatus("current")
_TBgpPeerNgOperVpnIpv6ActivePfxs_Type = Gauge32
_TBgpPeerNgOperVpnIpv6ActivePfxs_Object = MibTableColumn
tBgpPeerNgOperVpnIpv6ActivePfxs = _TBgpPeerNgOperVpnIpv6ActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 42),
    _TBgpPeerNgOperVpnIpv6ActivePfxs_Type()
)
tBgpPeerNgOperVpnIpv6ActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnIpv6ActivePfxs.setStatus("current")
_TBgpPeerNgOperVpnIpv6SuppPfxDamp_Type = Counter32
_TBgpPeerNgOperVpnIpv6SuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperVpnIpv6SuppPfxDamp = _TBgpPeerNgOperVpnIpv6SuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 43),
    _TBgpPeerNgOperVpnIpv6SuppPfxDamp_Type()
)
tBgpPeerNgOperVpnIpv6SuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnIpv6SuppPfxDamp.setStatus("current")
_TBgpPeerNgOperMvpnV4SuppPfxDamp_Type = Counter32
_TBgpPeerNgOperMvpnV4SuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperMvpnV4SuppPfxDamp = _TBgpPeerNgOperMvpnV4SuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 44),
    _TBgpPeerNgOperMvpnV4SuppPfxDamp_Type()
)
tBgpPeerNgOperMvpnV4SuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMvpnV4SuppPfxDamp.setStatus("current")
_TBgpPeerNgOperMvpnV4RecvPfxs_Type = Counter32
_TBgpPeerNgOperMvpnV4RecvPfxs_Object = MibTableColumn
tBgpPeerNgOperMvpnV4RecvPfxs = _TBgpPeerNgOperMvpnV4RecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 45),
    _TBgpPeerNgOperMvpnV4RecvPfxs_Type()
)
tBgpPeerNgOperMvpnV4RecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMvpnV4RecvPfxs.setStatus("current")
_TBgpPeerNgOperMvpnV4SentPfxs_Type = Counter32
_TBgpPeerNgOperMvpnV4SentPfxs_Object = MibTableColumn
tBgpPeerNgOperMvpnV4SentPfxs = _TBgpPeerNgOperMvpnV4SentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 46),
    _TBgpPeerNgOperMvpnV4SentPfxs_Type()
)
tBgpPeerNgOperMvpnV4SentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMvpnV4SentPfxs.setStatus("current")
_TBgpPeerNgOperMvpnV4ActivePfxs_Type = Counter32
_TBgpPeerNgOperMvpnV4ActivePfxs_Object = MibTableColumn
tBgpPeerNgOperMvpnV4ActivePfxs = _TBgpPeerNgOperMvpnV4ActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 47),
    _TBgpPeerNgOperMvpnV4ActivePfxs_Type()
)
tBgpPeerNgOperMvpnV4ActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMvpnV4ActivePfxs.setStatus("current")
_TBgpPeerNgOperl2VpnSuppPfxDamp_Type = Counter32
_TBgpPeerNgOperl2VpnSuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperl2VpnSuppPfxDamp = _TBgpPeerNgOperl2VpnSuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 48),
    _TBgpPeerNgOperl2VpnSuppPfxDamp_Type()
)
tBgpPeerNgOperl2VpnSuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperl2VpnSuppPfxDamp.setStatus("current")
_TBgpPeerNgOperl2VpnRecvPfxs_Type = Counter32
_TBgpPeerNgOperl2VpnRecvPfxs_Object = MibTableColumn
tBgpPeerNgOperl2VpnRecvPfxs = _TBgpPeerNgOperl2VpnRecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 49),
    _TBgpPeerNgOperl2VpnRecvPfxs_Type()
)
tBgpPeerNgOperl2VpnRecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperl2VpnRecvPfxs.setStatus("current")
_TBgpPeerNgOperl2VpnSentPfxs_Type = Counter32
_TBgpPeerNgOperl2VpnSentPfxs_Object = MibTableColumn
tBgpPeerNgOperl2VpnSentPfxs = _TBgpPeerNgOperl2VpnSentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 50),
    _TBgpPeerNgOperl2VpnSentPfxs_Type()
)
tBgpPeerNgOperl2VpnSentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperl2VpnSentPfxs.setStatus("current")
_TBgpPeerNgOperl2VpnActivePfxs_Type = Counter32
_TBgpPeerNgOperl2VpnActivePfxs_Object = MibTableColumn
tBgpPeerNgOperl2VpnActivePfxs = _TBgpPeerNgOperl2VpnActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 51),
    _TBgpPeerNgOperl2VpnActivePfxs_Type()
)
tBgpPeerNgOperl2VpnActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperl2VpnActivePfxs.setStatus("current")
_TBgpPeerNgOperMdtSafiSuppPfxDamp_Type = Counter32
_TBgpPeerNgOperMdtSafiSuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperMdtSafiSuppPfxDamp = _TBgpPeerNgOperMdtSafiSuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 52),
    _TBgpPeerNgOperMdtSafiSuppPfxDamp_Type()
)
tBgpPeerNgOperMdtSafiSuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMdtSafiSuppPfxDamp.setStatus("current")
_TBgpPeerNgOperMdtSafiRecvPfxs_Type = Counter32
_TBgpPeerNgOperMdtSafiRecvPfxs_Object = MibTableColumn
tBgpPeerNgOperMdtSafiRecvPfxs = _TBgpPeerNgOperMdtSafiRecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 53),
    _TBgpPeerNgOperMdtSafiRecvPfxs_Type()
)
tBgpPeerNgOperMdtSafiRecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMdtSafiRecvPfxs.setStatus("current")
_TBgpPeerNgOperMdtSafiSentPfxs_Type = Counter32
_TBgpPeerNgOperMdtSafiSentPfxs_Object = MibTableColumn
tBgpPeerNgOperMdtSafiSentPfxs = _TBgpPeerNgOperMdtSafiSentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 54),
    _TBgpPeerNgOperMdtSafiSentPfxs_Type()
)
tBgpPeerNgOperMdtSafiSentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMdtSafiSentPfxs.setStatus("current")
_TBgpPeerNgOperMdtSafiActivePfxs_Type = Counter32
_TBgpPeerNgOperMdtSafiActivePfxs_Object = MibTableColumn
tBgpPeerNgOperMdtSafiActivePfxs = _TBgpPeerNgOperMdtSafiActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 55),
    _TBgpPeerNgOperMdtSafiActivePfxs_Type()
)
tBgpPeerNgOperMdtSafiActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMdtSafiActivePfxs.setStatus("current")
_TBgpPeerNgOperMsPwSuppPfxDamp_Type = Counter32
_TBgpPeerNgOperMsPwSuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperMsPwSuppPfxDamp = _TBgpPeerNgOperMsPwSuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 56),
    _TBgpPeerNgOperMsPwSuppPfxDamp_Type()
)
tBgpPeerNgOperMsPwSuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMsPwSuppPfxDamp.setStatus("current")
_TBgpPeerNgOperMsPwRecvPfxs_Type = Counter32
_TBgpPeerNgOperMsPwRecvPfxs_Object = MibTableColumn
tBgpPeerNgOperMsPwRecvPfxs = _TBgpPeerNgOperMsPwRecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 57),
    _TBgpPeerNgOperMsPwRecvPfxs_Type()
)
tBgpPeerNgOperMsPwRecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMsPwRecvPfxs.setStatus("current")
_TBgpPeerNgOperMsPwSentPfxs_Type = Counter32
_TBgpPeerNgOperMsPwSentPfxs_Object = MibTableColumn
tBgpPeerNgOperMsPwSentPfxs = _TBgpPeerNgOperMsPwSentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 58),
    _TBgpPeerNgOperMsPwSentPfxs_Type()
)
tBgpPeerNgOperMsPwSentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMsPwSentPfxs.setStatus("current")
_TBgpPeerNgOperMsPwActivePfxs_Type = Counter32
_TBgpPeerNgOperMsPwActivePfxs_Object = MibTableColumn
tBgpPeerNgOperMsPwActivePfxs = _TBgpPeerNgOperMsPwActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 59),
    _TBgpPeerNgOperMsPwActivePfxs_Type()
)
tBgpPeerNgOperMsPwActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMsPwActivePfxs.setStatus("current")
_TBgpPeerNgOperFlowIpv4SupPfxDamp_Type = Counter32
_TBgpPeerNgOperFlowIpv4SupPfxDamp_Object = MibTableColumn
tBgpPeerNgOperFlowIpv4SupPfxDamp = _TBgpPeerNgOperFlowIpv4SupPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 60),
    _TBgpPeerNgOperFlowIpv4SupPfxDamp_Type()
)
tBgpPeerNgOperFlowIpv4SupPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlowIpv4SupPfxDamp.setStatus("current")
_TBgpPeerNgOperFlowIpv4RecvPfxs_Type = Counter32
_TBgpPeerNgOperFlowIpv4RecvPfxs_Object = MibTableColumn
tBgpPeerNgOperFlowIpv4RecvPfxs = _TBgpPeerNgOperFlowIpv4RecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 61),
    _TBgpPeerNgOperFlowIpv4RecvPfxs_Type()
)
tBgpPeerNgOperFlowIpv4RecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlowIpv4RecvPfxs.setStatus("current")
_TBgpPeerNgOperFlowIpv4SentPfxs_Type = Counter32
_TBgpPeerNgOperFlowIpv4SentPfxs_Object = MibTableColumn
tBgpPeerNgOperFlowIpv4SentPfxs = _TBgpPeerNgOperFlowIpv4SentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 62),
    _TBgpPeerNgOperFlowIpv4SentPfxs_Type()
)
tBgpPeerNgOperFlowIpv4SentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlowIpv4SentPfxs.setStatus("current")
_TBgpPeerNgOperFlowIpv4ActivePfxs_Type = Counter32
_TBgpPeerNgOperFlowIpv4ActivePfxs_Object = MibTableColumn
tBgpPeerNgOperFlowIpv4ActivePfxs = _TBgpPeerNgOperFlowIpv4ActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 63),
    _TBgpPeerNgOperFlowIpv4ActivePfxs_Type()
)
tBgpPeerNgOperFlowIpv4ActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlowIpv4ActivePfxs.setStatus("current")
_TBgpPeerNgAddPathSendRemoteCaps_Type = TmnxAddPathAddressFamily
_TBgpPeerNgAddPathSendRemoteCaps_Object = MibTableColumn
tBgpPeerNgAddPathSendRemoteCaps = _TBgpPeerNgAddPathSendRemoteCaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 66),
    _TBgpPeerNgAddPathSendRemoteCaps_Type()
)
tBgpPeerNgAddPathSendRemoteCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgAddPathSendRemoteCaps.setStatus("current")
_TBgpPeerNgAddPathRecvRemoteCaps_Type = TmnxAddPathAddressFamily
_TBgpPeerNgAddPathRecvRemoteCaps_Object = MibTableColumn
tBgpPeerNgAddPathRecvRemoteCaps = _TBgpPeerNgAddPathRecvRemoteCaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 67),
    _TBgpPeerNgAddPathRecvRemoteCaps_Type()
)
tBgpPeerNgAddPathRecvRemoteCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgAddPathRecvRemoteCaps.setStatus("current")
_TBgpPeerNgOperBackupPrefixes_Type = Counter32
_TBgpPeerNgOperBackupPrefixes_Object = MibTableColumn
tBgpPeerNgOperBackupPrefixes = _TBgpPeerNgOperBackupPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 68),
    _TBgpPeerNgOperBackupPrefixes_Type()
)
tBgpPeerNgOperBackupPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperBackupPrefixes.setStatus("current")
_TBgpPeerNgOperV6BackupPrefixes_Type = Counter32
_TBgpPeerNgOperV6BackupPrefixes_Object = MibTableColumn
tBgpPeerNgOperV6BackupPrefixes = _TBgpPeerNgOperV6BackupPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 69),
    _TBgpPeerNgOperV6BackupPrefixes_Type()
)
tBgpPeerNgOperV6BackupPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperV6BackupPrefixes.setStatus("current")
_TBgpPeerNgOperRtTgtSuppPfxDamp_Type = Counter32
_TBgpPeerNgOperRtTgtSuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperRtTgtSuppPfxDamp = _TBgpPeerNgOperRtTgtSuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 70),
    _TBgpPeerNgOperRtTgtSuppPfxDamp_Type()
)
tBgpPeerNgOperRtTgtSuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperRtTgtSuppPfxDamp.setStatus("current")
_TBgpPeerNgOperRtTgtRecvPfxs_Type = Counter32
_TBgpPeerNgOperRtTgtRecvPfxs_Object = MibTableColumn
tBgpPeerNgOperRtTgtRecvPfxs = _TBgpPeerNgOperRtTgtRecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 71),
    _TBgpPeerNgOperRtTgtRecvPfxs_Type()
)
tBgpPeerNgOperRtTgtRecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperRtTgtRecvPfxs.setStatus("current")
_TBgpPeerNgOperRtTgtSentPfxs_Type = Counter32
_TBgpPeerNgOperRtTgtSentPfxs_Object = MibTableColumn
tBgpPeerNgOperRtTgtSentPfxs = _TBgpPeerNgOperRtTgtSentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 72),
    _TBgpPeerNgOperRtTgtSentPfxs_Type()
)
tBgpPeerNgOperRtTgtSentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperRtTgtSentPfxs.setStatus("current")
_TBgpPeerNgOperRtTgtActivePfxs_Type = Counter32
_TBgpPeerNgOperRtTgtActivePfxs_Object = MibTableColumn
tBgpPeerNgOperRtTgtActivePfxs = _TBgpPeerNgOperRtTgtActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 73),
    _TBgpPeerNgOperRtTgtActivePfxs_Type()
)
tBgpPeerNgOperRtTgtActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperRtTgtActivePfxs.setStatus("current")
_TBgpPeerNgOperVpnV4BackupPfxs_Type = Counter32
_TBgpPeerNgOperVpnV4BackupPfxs_Object = MibTableColumn
tBgpPeerNgOperVpnV4BackupPfxs = _TBgpPeerNgOperVpnV4BackupPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 74),
    _TBgpPeerNgOperVpnV4BackupPfxs_Type()
)
tBgpPeerNgOperVpnV4BackupPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnV4BackupPfxs.setStatus("current")
_TBgpPeerNgOperVpnV6BackupPfxs_Type = Counter32
_TBgpPeerNgOperVpnV6BackupPfxs_Object = MibTableColumn
tBgpPeerNgOperVpnV6BackupPfxs = _TBgpPeerNgOperVpnV6BackupPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 75),
    _TBgpPeerNgOperVpnV6BackupPfxs_Type()
)
tBgpPeerNgOperVpnV6BackupPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperVpnV6BackupPfxs.setStatus("current")
_TBgpPeerNgOperMcastVpnV4RecvPfxs_Type = Counter32
_TBgpPeerNgOperMcastVpnV4RecvPfxs_Object = MibTableColumn
tBgpPeerNgOperMcastVpnV4RecvPfxs = _TBgpPeerNgOperMcastVpnV4RecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 76),
    _TBgpPeerNgOperMcastVpnV4RecvPfxs_Type()
)
tBgpPeerNgOperMcastVpnV4RecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMcastVpnV4RecvPfxs.setStatus("current")
_TBgpPeerNgOperMcastVpnV4SentPfxs_Type = Counter32
_TBgpPeerNgOperMcastVpnV4SentPfxs_Object = MibTableColumn
tBgpPeerNgOperMcastVpnV4SentPfxs = _TBgpPeerNgOperMcastVpnV4SentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 77),
    _TBgpPeerNgOperMcastVpnV4SentPfxs_Type()
)
tBgpPeerNgOperMcastVpnV4SentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMcastVpnV4SentPfxs.setStatus("current")
_TBgpPeerNgOperMcastVpnV4ActPfxs_Type = Counter32
_TBgpPeerNgOperMcastVpnV4ActPfxs_Object = MibTableColumn
tBgpPeerNgOperMcastVpnV4ActPfxs = _TBgpPeerNgOperMcastVpnV4ActPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 78),
    _TBgpPeerNgOperMcastVpnV4ActPfxs_Type()
)
tBgpPeerNgOperMcastVpnV4ActPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMcastVpnV4ActPfxs.setStatus("current")
_TBgpPeerNgOperMvpnV6SuppPfxDamp_Type = Counter32
_TBgpPeerNgOperMvpnV6SuppPfxDamp_Object = MibTableColumn
tBgpPeerNgOperMvpnV6SuppPfxDamp = _TBgpPeerNgOperMvpnV6SuppPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 79),
    _TBgpPeerNgOperMvpnV6SuppPfxDamp_Type()
)
tBgpPeerNgOperMvpnV6SuppPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMvpnV6SuppPfxDamp.setStatus("current")
_TBgpPeerNgOperMvpnV6RecvPfxs_Type = Counter32
_TBgpPeerNgOperMvpnV6RecvPfxs_Object = MibTableColumn
tBgpPeerNgOperMvpnV6RecvPfxs = _TBgpPeerNgOperMvpnV6RecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 80),
    _TBgpPeerNgOperMvpnV6RecvPfxs_Type()
)
tBgpPeerNgOperMvpnV6RecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMvpnV6RecvPfxs.setStatus("current")
_TBgpPeerNgOperMvpnV6SentPfxs_Type = Counter32
_TBgpPeerNgOperMvpnV6SentPfxs_Object = MibTableColumn
tBgpPeerNgOperMvpnV6SentPfxs = _TBgpPeerNgOperMvpnV6SentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 81),
    _TBgpPeerNgOperMvpnV6SentPfxs_Type()
)
tBgpPeerNgOperMvpnV6SentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMvpnV6SentPfxs.setStatus("current")
_TBgpPeerNgOperMvpnV6ActivePfxs_Type = Counter32
_TBgpPeerNgOperMvpnV6ActivePfxs_Object = MibTableColumn
tBgpPeerNgOperMvpnV6ActivePfxs = _TBgpPeerNgOperMvpnV6ActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 82),
    _TBgpPeerNgOperMvpnV6ActivePfxs_Type()
)
tBgpPeerNgOperMvpnV6ActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMvpnV6ActivePfxs.setStatus("current")
_TBgpPeerNgOperFlowIpv6SupPfxDamp_Type = Counter32
_TBgpPeerNgOperFlowIpv6SupPfxDamp_Object = MibTableColumn
tBgpPeerNgOperFlowIpv6SupPfxDamp = _TBgpPeerNgOperFlowIpv6SupPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 83),
    _TBgpPeerNgOperFlowIpv6SupPfxDamp_Type()
)
tBgpPeerNgOperFlowIpv6SupPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlowIpv6SupPfxDamp.setStatus("current")
_TBgpPeerNgOperFlowIpv6RecvPfxs_Type = Counter32
_TBgpPeerNgOperFlowIpv6RecvPfxs_Object = MibTableColumn
tBgpPeerNgOperFlowIpv6RecvPfxs = _TBgpPeerNgOperFlowIpv6RecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 84),
    _TBgpPeerNgOperFlowIpv6RecvPfxs_Type()
)
tBgpPeerNgOperFlowIpv6RecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlowIpv6RecvPfxs.setStatus("current")
_TBgpPeerNgOperFlowIpv6SentPfxs_Type = Counter32
_TBgpPeerNgOperFlowIpv6SentPfxs_Object = MibTableColumn
tBgpPeerNgOperFlowIpv6SentPfxs = _TBgpPeerNgOperFlowIpv6SentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 85),
    _TBgpPeerNgOperFlowIpv6SentPfxs_Type()
)
tBgpPeerNgOperFlowIpv6SentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlowIpv6SentPfxs.setStatus("current")
_TBgpPeerNgOperFlowIpv6ActivePfxs_Type = Counter32
_TBgpPeerNgOperFlowIpv6ActivePfxs_Object = MibTableColumn
tBgpPeerNgOperFlowIpv6ActivePfxs = _TBgpPeerNgOperFlowIpv6ActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 86),
    _TBgpPeerNgOperFlowIpv6ActivePfxs_Type()
)
tBgpPeerNgOperFlowIpv6ActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperFlowIpv6ActivePfxs.setStatus("current")
_TBgpPeerNgOperEvpnSupPfxDamp_Type = Counter32
_TBgpPeerNgOperEvpnSupPfxDamp_Object = MibTableColumn
tBgpPeerNgOperEvpnSupPfxDamp = _TBgpPeerNgOperEvpnSupPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 87),
    _TBgpPeerNgOperEvpnSupPfxDamp_Type()
)
tBgpPeerNgOperEvpnSupPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperEvpnSupPfxDamp.setStatus("current")
_TBgpPeerNgOperEvpnRecvPfxs_Type = Counter32
_TBgpPeerNgOperEvpnRecvPfxs_Object = MibTableColumn
tBgpPeerNgOperEvpnRecvPfxs = _TBgpPeerNgOperEvpnRecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 88),
    _TBgpPeerNgOperEvpnRecvPfxs_Type()
)
tBgpPeerNgOperEvpnRecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperEvpnRecvPfxs.setStatus("current")
_TBgpPeerNgOperEvpnSentPfxs_Type = Counter32
_TBgpPeerNgOperEvpnSentPfxs_Object = MibTableColumn
tBgpPeerNgOperEvpnSentPfxs = _TBgpPeerNgOperEvpnSentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 89),
    _TBgpPeerNgOperEvpnSentPfxs_Type()
)
tBgpPeerNgOperEvpnSentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperEvpnSentPfxs.setStatus("current")
_TBgpPeerNgOperEvpnActivePfxs_Type = Counter32
_TBgpPeerNgOperEvpnActivePfxs_Object = MibTableColumn
tBgpPeerNgOperEvpnActivePfxs = _TBgpPeerNgOperEvpnActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 90),
    _TBgpPeerNgOperEvpnActivePfxs_Type()
)
tBgpPeerNgOperEvpnActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperEvpnActivePfxs.setStatus("current")
_TBgpPeerNgOperUpdateErrors_Type = Counter32
_TBgpPeerNgOperUpdateErrors_Object = MibTableColumn
tBgpPeerNgOperUpdateErrors = _TBgpPeerNgOperUpdateErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 91),
    _TBgpPeerNgOperUpdateErrors_Type()
)
tBgpPeerNgOperUpdateErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperUpdateErrors.setStatus("current")
_TBgpPeerNgOperGRNotifFamilyNego_Type = TmnxBGPFamilyType
_TBgpPeerNgOperGRNotifFamilyNego_Object = MibTableColumn
tBgpPeerNgOperGRNotifFamilyNego = _TBgpPeerNgOperGRNotifFamilyNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 92),
    _TBgpPeerNgOperGRNotifFamilyNego_Type()
)
tBgpPeerNgOperGRNotifFamilyNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperGRNotifFamilyNego.setStatus("current")
_TBgpPeerNgOperRemIdleHoldTime_Type = Unsigned32
_TBgpPeerNgOperRemIdleHoldTime_Object = MibTableColumn
tBgpPeerNgOperRemIdleHoldTime = _TBgpPeerNgOperRemIdleHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 93),
    _TBgpPeerNgOperRemIdleHoldTime_Type()
)
tBgpPeerNgOperRemIdleHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperRemIdleHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgOperRemIdleHoldTime.setUnits("seconds")
_TBgpPeerNgOperMcastV6SupPfxDamp_Type = Counter32
_TBgpPeerNgOperMcastV6SupPfxDamp_Object = MibTableColumn
tBgpPeerNgOperMcastV6SupPfxDamp = _TBgpPeerNgOperMcastV6SupPfxDamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 94),
    _TBgpPeerNgOperMcastV6SupPfxDamp_Type()
)
tBgpPeerNgOperMcastV6SupPfxDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMcastV6SupPfxDamp.setStatus("current")
_TBgpPeerNgOperMcastV6RecvPfxs_Type = Counter32
_TBgpPeerNgOperMcastV6RecvPfxs_Object = MibTableColumn
tBgpPeerNgOperMcastV6RecvPfxs = _TBgpPeerNgOperMcastV6RecvPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 95),
    _TBgpPeerNgOperMcastV6RecvPfxs_Type()
)
tBgpPeerNgOperMcastV6RecvPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMcastV6RecvPfxs.setStatus("current")
_TBgpPeerNgOperMcastV6SentPfxs_Type = Counter32
_TBgpPeerNgOperMcastV6SentPfxs_Object = MibTableColumn
tBgpPeerNgOperMcastV6SentPfxs = _TBgpPeerNgOperMcastV6SentPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 96),
    _TBgpPeerNgOperMcastV6SentPfxs_Type()
)
tBgpPeerNgOperMcastV6SentPfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMcastV6SentPfxs.setStatus("current")
_TBgpPeerNgOperMcastV6ActivePfxs_Type = Counter32
_TBgpPeerNgOperMcastV6ActivePfxs_Object = MibTableColumn
tBgpPeerNgOperMcastV6ActivePfxs = _TBgpPeerNgOperMcastV6ActivePfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 8, 1, 97),
    _TBgpPeerNgOperMcastV6ActivePfxs_Type()
)
tBgpPeerNgOperMcastV6ActivePfxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgOperMcastV6ActivePfxs.setStatus("current")
_TBgpPeerNgSendOrfRouteTargetTable_Object = MibTable
tBgpPeerNgSendOrfRouteTargetTable = _TBgpPeerNgSendOrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 9)
)
if mibBuilder.loadTexts:
    tBgpPeerNgSendOrfRouteTargetTable.setStatus("current")
_TBgpPeerNgSendOrfRouteTargetEntry_Object = MibTableRow
tBgpPeerNgSendOrfRouteTargetEntry = _TBgpPeerNgSendOrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 9, 1)
)
tBgpPeerNgSendOrfRouteTargetEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgAddressType"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgAddress"),
    (1, "TIMETRA-BGP-MIB", "tBgpPeerNgSendOrfRouteTarget"),
)
if mibBuilder.loadTexts:
    tBgpPeerNgSendOrfRouteTargetEntry.setStatus("current")
_TBgpPeerNgSendOrfRouteTarget_Type = TNamedItem
_TBgpPeerNgSendOrfRouteTarget_Object = MibTableColumn
tBgpPeerNgSendOrfRouteTarget = _TBgpPeerNgSendOrfRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 9, 1, 1),
    _TBgpPeerNgSendOrfRouteTarget_Type()
)
tBgpPeerNgSendOrfRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpPeerNgSendOrfRouteTarget.setStatus("current")
_TBgpPeerNgSendOrfRTRowStatus_Type = RowStatus
_TBgpPeerNgSendOrfRTRowStatus_Object = MibTableColumn
tBgpPeerNgSendOrfRTRowStatus = _TBgpPeerNgSendOrfRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 9, 1, 2),
    _TBgpPeerNgSendOrfRTRowStatus_Type()
)
tBgpPeerNgSendOrfRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgSendOrfRTRowStatus.setStatus("current")
_TBgpPeerNgParamsTable_Object = MibTable
tBgpPeerNgParamsTable = _TBgpPeerNgParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10)
)
if mibBuilder.loadTexts:
    tBgpPeerNgParamsTable.setStatus("current")
_TBgpPeerNgParamsEntry_Object = MibTableRow
tBgpPeerNgParamsEntry = _TBgpPeerNgParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1)
)
tBgpPeerNgParamsEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgAddressType"),
    (0, "TIMETRA-BGP-MIB", "tBgpPeerNgAddress"),
)
if mibBuilder.loadTexts:
    tBgpPeerNgParamsEntry.setStatus("current")


class _TBgpPeerNgParamsInheritance_Type(Counter64):
    """Custom type tBgpPeerNgParamsInheritance based on Counter64"""
    defaultValue = 0


_TBgpPeerNgParamsInheritance_Type.__name__ = "Counter64"
_TBgpPeerNgParamsInheritance_Object = MibTableColumn
tBgpPeerNgParamsInheritance = _TBgpPeerNgParamsInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 1),
    _TBgpPeerNgParamsInheritance_Type()
)
tBgpPeerNgParamsInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgParamsInheritance.setStatus("current")


class _TBgpPeerNgDisableFEFailover_Type(TruthValue):
    """Custom type tBgpPeerNgDisableFEFailover based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDisableFEFailover_Type.__name__ = "TruthValue"
_TBgpPeerNgDisableFEFailover_Object = MibTableColumn
tBgpPeerNgDisableFEFailover = _TBgpPeerNgDisableFEFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 2),
    _TBgpPeerNgDisableFEFailover_Type()
)
tBgpPeerNgDisableFEFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDisableFEFailover.setStatus("current")


class _TBgpPeerNgDisableComms_Type(TruthValue):
    """Custom type tBgpPeerNgDisableComms based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDisableComms_Type.__name__ = "TruthValue"
_TBgpPeerNgDisableComms_Object = MibTableColumn
tBgpPeerNgDisableComms = _TBgpPeerNgDisableComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 3),
    _TBgpPeerNgDisableComms_Type()
)
tBgpPeerNgDisableComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDisableComms.setStatus("current")


class _TBgpPeerNgDisableExtComms_Type(TruthValue):
    """Custom type tBgpPeerNgDisableExtComms based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDisableExtComms_Type.__name__ = "TruthValue"
_TBgpPeerNgDisableExtComms_Object = MibTableColumn
tBgpPeerNgDisableExtComms = _TBgpPeerNgDisableExtComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 4),
    _TBgpPeerNgDisableExtComms_Type()
)
tBgpPeerNgDisableExtComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDisableExtComms.setStatus("current")


class _TBgpPeerNgDefaultOriginate_Type(TruthValue):
    """Custom type tBgpPeerNgDefaultOriginate based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDefaultOriginate_Type.__name__ = "TruthValue"
_TBgpPeerNgDefaultOriginate_Object = MibTableColumn
tBgpPeerNgDefaultOriginate = _TBgpPeerNgDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 5),
    _TBgpPeerNgDefaultOriginate_Type()
)
tBgpPeerNgDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDefaultOriginate.setStatus("current")


class _TBgpPeerNgAdvertiseInactiveRts_Type(TruthValue):
    """Custom type tBgpPeerNgAdvertiseInactiveRts based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgAdvertiseInactiveRts_Type.__name__ = "TruthValue"
_TBgpPeerNgAdvertiseInactiveRts_Object = MibTableColumn
tBgpPeerNgAdvertiseInactiveRts = _TBgpPeerNgAdvertiseInactiveRts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 6),
    _TBgpPeerNgAdvertiseInactiveRts_Type()
)
tBgpPeerNgAdvertiseInactiveRts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgAdvertiseInactiveRts.setStatus("current")


class _TBgpPeerNgMinTTLValue_Type(Unsigned32):
    """Custom type tBgpPeerNgMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TBgpPeerNgMinTTLValue_Type.__name__ = "Unsigned32"
_TBgpPeerNgMinTTLValue_Object = MibTableColumn
tBgpPeerNgMinTTLValue = _TBgpPeerNgMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 7),
    _TBgpPeerNgMinTTLValue_Type()
)
tBgpPeerNgMinTTLValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMinTTLValue.setStatus("current")


class _TBgpPeerNgTracking_Type(TruthValue):
    """Custom type tBgpPeerNgTracking based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgTracking_Type.__name__ = "TruthValue"
_TBgpPeerNgTracking_Object = MibTableColumn
tBgpPeerNgTracking = _TBgpPeerNgTracking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 8),
    _TBgpPeerNgTracking_Type()
)
tBgpPeerNgTracking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgTracking.setStatus("current")
_TBgpPeerNgAdvLabelAddrFamily_Type = TmnxAdvLabelAddressFamily
_TBgpPeerNgAdvLabelAddrFamily_Object = MibTableColumn
tBgpPeerNgAdvLabelAddrFamily = _TBgpPeerNgAdvLabelAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 9),
    _TBgpPeerNgAdvLabelAddrFamily_Type()
)
tBgpPeerNgAdvLabelAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgAdvLabelAddrFamily.setStatus("current")


class _TBgpPeerNgAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tBgpPeerNgAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TBgpPeerNgAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TBgpPeerNgAuthKeyChain_Object = MibTableColumn
tBgpPeerNgAuthKeyChain = _TBgpPeerNgAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 10),
    _TBgpPeerNgAuthKeyChain_Type()
)
tBgpPeerNgAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgAuthKeyChain.setStatus("current")


class _TBgpPeerNgLastError_Type(OctetString):
    """Custom type tBgpPeerNgLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TBgpPeerNgLastError_Type.__name__ = "OctetString"
_TBgpPeerNgLastError_Object = MibTableColumn
tBgpPeerNgLastError = _TBgpPeerNgLastError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 11),
    _TBgpPeerNgLastError_Type()
)
tBgpPeerNgLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeerNgLastError.setStatus("current")


class _TBgpPeerNgBfdEnabled_Type(TruthValue):
    """Custom type tBgpPeerNgBfdEnabled based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgBfdEnabled_Type.__name__ = "TruthValue"
_TBgpPeerNgBfdEnabled_Object = MibTableColumn
tBgpPeerNgBfdEnabled = _TBgpPeerNgBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 12),
    _TBgpPeerNgBfdEnabled_Type()
)
tBgpPeerNgBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgBfdEnabled.setStatus("current")


class _TBgpPeerNgPMTUDiscovery_Type(TruthValue):
    """Custom type tBgpPeerNgPMTUDiscovery based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgPMTUDiscovery_Type.__name__ = "TruthValue"
_TBgpPeerNgPMTUDiscovery_Object = MibTableColumn
tBgpPeerNgPMTUDiscovery = _TBgpPeerNgPMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 13),
    _TBgpPeerNgPMTUDiscovery_Type()
)
tBgpPeerNgPMTUDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgPMTUDiscovery.setStatus("current")


class _TBgpPeerNgAdvertiseLdpPrefix_Type(TruthValue):
    """Custom type tBgpPeerNgAdvertiseLdpPrefix based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgAdvertiseLdpPrefix_Type.__name__ = "TruthValue"
_TBgpPeerNgAdvertiseLdpPrefix_Object = MibTableColumn
tBgpPeerNgAdvertiseLdpPrefix = _TBgpPeerNgAdvertiseLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 14),
    _TBgpPeerNgAdvertiseLdpPrefix_Type()
)
tBgpPeerNgAdvertiseLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgAdvertiseLdpPrefix.setStatus("current")


class _TBgpPeerNgEnableAddPath_Type(TruthValue):
    """Custom type tBgpPeerNgEnableAddPath based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgEnableAddPath_Type.__name__ = "TruthValue"
_TBgpPeerNgEnableAddPath_Object = MibTableColumn
tBgpPeerNgEnableAddPath = _TBgpPeerNgEnableAddPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 15),
    _TBgpPeerNgEnableAddPath_Type()
)
tBgpPeerNgEnableAddPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgEnableAddPath.setStatus("current")


class _TBgpPeerNgRecvAddPath_Type(TmnxAddPathAddressFamily):
    """Custom type tBgpPeerNgRecvAddPath based on TmnxAddPathAddressFamily"""
    defaultBinValue = "1"


_TBgpPeerNgRecvAddPath_Type.__name__ = "TmnxAddPathAddressFamily"
_TBgpPeerNgRecvAddPath_Object = MibTableColumn
tBgpPeerNgRecvAddPath = _TBgpPeerNgRecvAddPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 16),
    _TBgpPeerNgRecvAddPath_Type()
)
tBgpPeerNgRecvAddPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgRecvAddPath.setStatus("current")


class _TBgpPeerNgIpv4AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpPeerNgIpv4AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpPeerNgIpv4AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpPeerNgIpv4AddPathLimit_Object = MibTableColumn
tBgpPeerNgIpv4AddPathLimit = _TBgpPeerNgIpv4AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 17),
    _TBgpPeerNgIpv4AddPathLimit_Type()
)
tBgpPeerNgIpv4AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgIpv4AddPathLimit.setStatus("current")


class _TBgpPeerNgVpnIpv4AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpPeerNgVpnIpv4AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpPeerNgVpnIpv4AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpPeerNgVpnIpv4AddPathLimit_Object = MibTableColumn
tBgpPeerNgVpnIpv4AddPathLimit = _TBgpPeerNgVpnIpv4AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 18),
    _TBgpPeerNgVpnIpv4AddPathLimit_Type()
)
tBgpPeerNgVpnIpv4AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgVpnIpv4AddPathLimit.setStatus("current")


class _TBgpPeerNgIpv6AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpPeerNgIpv6AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpPeerNgIpv6AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpPeerNgIpv6AddPathLimit_Object = MibTableColumn
tBgpPeerNgIpv6AddPathLimit = _TBgpPeerNgIpv6AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 19),
    _TBgpPeerNgIpv6AddPathLimit_Type()
)
tBgpPeerNgIpv6AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgIpv6AddPathLimit.setStatus("current")


class _TBgpPeerNgVpnIpv6AddPathLimit_Type(TmnxAddPathSendLimit):
    """Custom type tBgpPeerNgVpnIpv6AddPathLimit based on TmnxAddPathSendLimit"""
    defaultValue = 0


_TBgpPeerNgVpnIpv6AddPathLimit_Type.__name__ = "TmnxAddPathSendLimit"
_TBgpPeerNgVpnIpv6AddPathLimit_Object = MibTableColumn
tBgpPeerNgVpnIpv6AddPathLimit = _TBgpPeerNgVpnIpv6AddPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 20),
    _TBgpPeerNgVpnIpv6AddPathLimit_Type()
)
tBgpPeerNgVpnIpv6AddPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgVpnIpv6AddPathLimit.setStatus("current")


class _TBgpPeerNgFlowspecValidate_Type(TruthValue):
    """Custom type tBgpPeerNgFlowspecValidate based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgFlowspecValidate_Type.__name__ = "TruthValue"
_TBgpPeerNgFlowspecValidate_Object = MibTableColumn
tBgpPeerNgFlowspecValidate = _TBgpPeerNgFlowspecValidate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 21),
    _TBgpPeerNgFlowspecValidate_Type()
)
tBgpPeerNgFlowspecValidate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgFlowspecValidate.setStatus("current")


class _TBgpPeerNgUpdatedErrorHandling_Type(TruthValue):
    """Custom type tBgpPeerNgUpdatedErrorHandling based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgUpdatedErrorHandling_Type.__name__ = "TruthValue"
_TBgpPeerNgUpdatedErrorHandling_Object = MibTableColumn
tBgpPeerNgUpdatedErrorHandling = _TBgpPeerNgUpdatedErrorHandling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 22),
    _TBgpPeerNgUpdatedErrorHandling_Type()
)
tBgpPeerNgUpdatedErrorHandling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgUpdatedErrorHandling.setStatus("obsolete")


class _TBgpPeerNgDefaultRouteTarget_Type(TruthValue):
    """Custom type tBgpPeerNgDefaultRouteTarget based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDefaultRouteTarget_Type.__name__ = "TruthValue"
_TBgpPeerNgDefaultRouteTarget_Object = MibTableColumn
tBgpPeerNgDefaultRouteTarget = _TBgpPeerNgDefaultRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 23),
    _TBgpPeerNgDefaultRouteTarget_Type()
)
tBgpPeerNgDefaultRouteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDefaultRouteTarget.setStatus("current")


class _TBgpPeerNgAigp_Type(TruthValue):
    """Custom type tBgpPeerNgAigp based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgAigp_Type.__name__ = "TruthValue"
_TBgpPeerNgAigp_Object = MibTableColumn
tBgpPeerNgAigp = _TBgpPeerNgAigp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 24),
    _TBgpPeerNgAigp_Type()
)
tBgpPeerNgAigp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgAigp.setStatus("current")


class _TBgpPeerNgMinHoldTime_Type(BgpHoldTime):
    """Custom type tBgpPeerNgMinHoldTime based on BgpHoldTime"""
    defaultValue = 0


_TBgpPeerNgMinHoldTime_Type.__name__ = "BgpHoldTime"
_TBgpPeerNgMinHoldTime_Object = MibTableColumn
tBgpPeerNgMinHoldTime = _TBgpPeerNgMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 25),
    _TBgpPeerNgMinHoldTime_Type()
)
tBgpPeerNgMinHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMinHoldTime.setStatus("current")


class _TBgpPeerNgSplitHorizon_Type(TruthValue):
    """Custom type tBgpPeerNgSplitHorizon based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgSplitHorizon_Type.__name__ = "TruthValue"
_TBgpPeerNgSplitHorizon_Object = MibTableColumn
tBgpPeerNgSplitHorizon = _TBgpPeerNgSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 26),
    _TBgpPeerNgSplitHorizon_Type()
)
tBgpPeerNgSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgSplitHorizon.setStatus("current")


class _TBgpPeerNgRemPrivateSkipPeerAs_Type(TruthValue):
    """Custom type tBgpPeerNgRemPrivateSkipPeerAs based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgRemPrivateSkipPeerAs_Type.__name__ = "TruthValue"
_TBgpPeerNgRemPrivateSkipPeerAs_Object = MibTableColumn
tBgpPeerNgRemPrivateSkipPeerAs = _TBgpPeerNgRemPrivateSkipPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 27),
    _TBgpPeerNgRemPrivateSkipPeerAs_Type()
)
tBgpPeerNgRemPrivateSkipPeerAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgRemPrivateSkipPeerAs.setStatus("current")


class _TBgpPeerNgLclASNoPrependGlobalAS_Type(TruthValue):
    """Custom type tBgpPeerNgLclASNoPrependGlobalAS based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgLclASNoPrependGlobalAS_Type.__name__ = "TruthValue"
_TBgpPeerNgLclASNoPrependGlobalAS_Object = MibTableColumn
tBgpPeerNgLclASNoPrependGlobalAS = _TBgpPeerNgLclASNoPrependGlobalAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 28),
    _TBgpPeerNgLclASNoPrependGlobalAS_Type()
)
tBgpPeerNgLclASNoPrependGlobalAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgLclASNoPrependGlobalAS.setStatus("current")


class _TBgpPeerNgMaxPrefixIdleTimeOut_Type(Integer32):
    """Custom type tBgpPeerNgMaxPrefixIdleTimeOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1024),
    )


_TBgpPeerNgMaxPrefixIdleTimeOut_Type.__name__ = "Integer32"
_TBgpPeerNgMaxPrefixIdleTimeOut_Object = MibTableColumn
tBgpPeerNgMaxPrefixIdleTimeOut = _TBgpPeerNgMaxPrefixIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 29),
    _TBgpPeerNgMaxPrefixIdleTimeOut_Type()
)
tBgpPeerNgMaxPrefixIdleTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgMaxPrefixIdleTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgMaxPrefixIdleTimeOut.setUnits("minutes")


class _TBgpPeerNgGRRestartNotification_Type(TruthValue):
    """Custom type tBgpPeerNgGRRestartNotification based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgGRRestartNotification_Type.__name__ = "TruthValue"
_TBgpPeerNgGRRestartNotification_Object = MibTableColumn
tBgpPeerNgGRRestartNotification = _TBgpPeerNgGRRestartNotification_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 30),
    _TBgpPeerNgGRRestartNotification_Type()
)
tBgpPeerNgGRRestartNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgGRRestartNotification.setStatus("current")


class _TBgpPeerNgFaultTolerance_Type(TruthValue):
    """Custom type tBgpPeerNgFaultTolerance based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgFaultTolerance_Type.__name__ = "TruthValue"
_TBgpPeerNgFaultTolerance_Object = MibTableColumn
tBgpPeerNgFaultTolerance = _TBgpPeerNgFaultTolerance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 31),
    _TBgpPeerNgFaultTolerance_Type()
)
tBgpPeerNgFaultTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgFaultTolerance.setStatus("current")


class _TBgpPeerNgDampPeerOscillations_Type(TruthValue):
    """Custom type tBgpPeerNgDampPeerOscillations based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgDampPeerOscillations_Type.__name__ = "TruthValue"
_TBgpPeerNgDampPeerOscillations_Object = MibTableColumn
tBgpPeerNgDampPeerOscillations = _TBgpPeerNgDampPeerOscillations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 32),
    _TBgpPeerNgDampPeerOscillations_Type()
)
tBgpPeerNgDampPeerOscillations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDampPeerOscillations.setStatus("current")


class _TBgpPeerNgDampOscInitialWaitTime_Type(Unsigned32):
    """Custom type tBgpPeerNgDampOscInitialWaitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_TBgpPeerNgDampOscInitialWaitTime_Type.__name__ = "Unsigned32"
_TBgpPeerNgDampOscInitialWaitTime_Object = MibTableColumn
tBgpPeerNgDampOscInitialWaitTime = _TBgpPeerNgDampOscInitialWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 33),
    _TBgpPeerNgDampOscInitialWaitTime_Type()
)
tBgpPeerNgDampOscInitialWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDampOscInitialWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgDampOscInitialWaitTime.setUnits("minutes")


class _TBgpPeerNgDampOscSecondWaitTime_Type(Unsigned32):
    """Custom type tBgpPeerNgDampOscSecondWaitTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TBgpPeerNgDampOscSecondWaitTime_Type.__name__ = "Unsigned32"
_TBgpPeerNgDampOscSecondWaitTime_Object = MibTableColumn
tBgpPeerNgDampOscSecondWaitTime = _TBgpPeerNgDampOscSecondWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 34),
    _TBgpPeerNgDampOscSecondWaitTime_Type()
)
tBgpPeerNgDampOscSecondWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDampOscSecondWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgDampOscSecondWaitTime.setUnits("minutes")


class _TBgpPeerNgDampOscMaxWaitTime_Type(Unsigned32):
    """Custom type tBgpPeerNgDampOscMaxWaitTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TBgpPeerNgDampOscMaxWaitTime_Type.__name__ = "Unsigned32"
_TBgpPeerNgDampOscMaxWaitTime_Object = MibTableColumn
tBgpPeerNgDampOscMaxWaitTime = _TBgpPeerNgDampOscMaxWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 35),
    _TBgpPeerNgDampOscMaxWaitTime_Type()
)
tBgpPeerNgDampOscMaxWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDampOscMaxWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgDampOscMaxWaitTime.setUnits("minutes")


class _TBgpPeerNgDampOscErrorInterval_Type(Unsigned32):
    """Custom type tBgpPeerNgDampOscErrorInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_TBgpPeerNgDampOscErrorInterval_Type.__name__ = "Unsigned32"
_TBgpPeerNgDampOscErrorInterval_Object = MibTableColumn
tBgpPeerNgDampOscErrorInterval = _TBgpPeerNgDampOscErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 36),
    _TBgpPeerNgDampOscErrorInterval_Type()
)
tBgpPeerNgDampOscErrorInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgDampOscErrorInterval.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPeerNgDampOscErrorInterval.setUnits("minutes")


class _TBgpPeerNgNhUnchangedFamily_Type(TmnxIpNhChgFamily):
    """Custom type tBgpPeerNgNhUnchangedFamily based on TmnxIpNhChgFamily"""
    defaultHexValue = ""


_TBgpPeerNgNhUnchangedFamily_Type.__name__ = "TmnxIpNhChgFamily"
_TBgpPeerNgNhUnchangedFamily_Object = MibTableColumn
tBgpPeerNgNhUnchangedFamily = _TBgpPeerNgNhUnchangedFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 37),
    _TBgpPeerNgNhUnchangedFamily_Type()
)
tBgpPeerNgNhUnchangedFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgNhUnchangedFamily.setStatus("current")


class _TBgpPeerNgEnableOriginValidation_Type(TmnxIpFamily):
    """Custom type tBgpPeerNgEnableOriginValidation based on TmnxIpFamily"""
    defaultHexValue = ""


_TBgpPeerNgEnableOriginValidation_Type.__name__ = "TmnxIpFamily"
_TBgpPeerNgEnableOriginValidation_Object = MibTableColumn
tBgpPeerNgEnableOriginValidation = _TBgpPeerNgEnableOriginValidation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 38),
    _TBgpPeerNgEnableOriginValidation_Type()
)
tBgpPeerNgEnableOriginValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgEnableOriginValidation.setStatus("current")


class _TBgpPeerNgThirdPartyNextHop_Type(TruthValue):
    """Custom type tBgpPeerNgThirdPartyNextHop based on TruthValue"""
    defaultValue = 2


_TBgpPeerNgThirdPartyNextHop_Type.__name__ = "TruthValue"
_TBgpPeerNgThirdPartyNextHop_Object = MibTableColumn
tBgpPeerNgThirdPartyNextHop = _TBgpPeerNgThirdPartyNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 10, 1, 39),
    _TBgpPeerNgThirdPartyNextHop_Type()
)
tBgpPeerNgThirdPartyNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerNgThirdPartyNextHop.setStatus("current")
_TBgpPeerPlcyTable_Object = MibTable
tBgpPeerPlcyTable = _TBgpPeerPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11)
)
if mibBuilder.loadTexts:
    tBgpPeerPlcyTable.setStatus("current")
_TBgpPeerPlcyEntry_Object = MibTableRow
tBgpPeerPlcyEntry = _TBgpPeerPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1)
)
if mibBuilder.loadTexts:
    tBgpPeerPlcyEntry.setStatus("current")


class _TBgpPeerPlcyImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy1_Object = MibTableColumn
tBgpPeerPlcyImportPolicy1 = _TBgpPeerPlcyImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 1),
    _TBgpPeerPlcyImportPolicy1_Type()
)
tBgpPeerPlcyImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy1.setStatus("current")


class _TBgpPeerPlcyImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy2_Object = MibTableColumn
tBgpPeerPlcyImportPolicy2 = _TBgpPeerPlcyImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 2),
    _TBgpPeerPlcyImportPolicy2_Type()
)
tBgpPeerPlcyImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy2.setStatus("current")


class _TBgpPeerPlcyImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy3_Object = MibTableColumn
tBgpPeerPlcyImportPolicy3 = _TBgpPeerPlcyImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 3),
    _TBgpPeerPlcyImportPolicy3_Type()
)
tBgpPeerPlcyImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy3.setStatus("current")


class _TBgpPeerPlcyImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy4_Object = MibTableColumn
tBgpPeerPlcyImportPolicy4 = _TBgpPeerPlcyImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 4),
    _TBgpPeerPlcyImportPolicy4_Type()
)
tBgpPeerPlcyImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy4.setStatus("current")


class _TBgpPeerPlcyImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy5_Object = MibTableColumn
tBgpPeerPlcyImportPolicy5 = _TBgpPeerPlcyImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 5),
    _TBgpPeerPlcyImportPolicy5_Type()
)
tBgpPeerPlcyImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy5.setStatus("current")


class _TBgpPeerPlcyImportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy6_Object = MibTableColumn
tBgpPeerPlcyImportPolicy6 = _TBgpPeerPlcyImportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 6),
    _TBgpPeerPlcyImportPolicy6_Type()
)
tBgpPeerPlcyImportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy6.setStatus("current")


class _TBgpPeerPlcyImportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy7_Object = MibTableColumn
tBgpPeerPlcyImportPolicy7 = _TBgpPeerPlcyImportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 7),
    _TBgpPeerPlcyImportPolicy7_Type()
)
tBgpPeerPlcyImportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy7.setStatus("current")


class _TBgpPeerPlcyImportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy8_Object = MibTableColumn
tBgpPeerPlcyImportPolicy8 = _TBgpPeerPlcyImportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 8),
    _TBgpPeerPlcyImportPolicy8_Type()
)
tBgpPeerPlcyImportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy8.setStatus("current")


class _TBgpPeerPlcyImportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy9_Object = MibTableColumn
tBgpPeerPlcyImportPolicy9 = _TBgpPeerPlcyImportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 9),
    _TBgpPeerPlcyImportPolicy9_Type()
)
tBgpPeerPlcyImportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy9.setStatus("current")


class _TBgpPeerPlcyImportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy10_Object = MibTableColumn
tBgpPeerPlcyImportPolicy10 = _TBgpPeerPlcyImportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 10),
    _TBgpPeerPlcyImportPolicy10_Type()
)
tBgpPeerPlcyImportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy10.setStatus("current")


class _TBgpPeerPlcyImportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy11_Object = MibTableColumn
tBgpPeerPlcyImportPolicy11 = _TBgpPeerPlcyImportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 11),
    _TBgpPeerPlcyImportPolicy11_Type()
)
tBgpPeerPlcyImportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy11.setStatus("current")


class _TBgpPeerPlcyImportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy12_Object = MibTableColumn
tBgpPeerPlcyImportPolicy12 = _TBgpPeerPlcyImportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 12),
    _TBgpPeerPlcyImportPolicy12_Type()
)
tBgpPeerPlcyImportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy12.setStatus("current")


class _TBgpPeerPlcyImportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy13_Object = MibTableColumn
tBgpPeerPlcyImportPolicy13 = _TBgpPeerPlcyImportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 13),
    _TBgpPeerPlcyImportPolicy13_Type()
)
tBgpPeerPlcyImportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy13.setStatus("current")


class _TBgpPeerPlcyImportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy14_Object = MibTableColumn
tBgpPeerPlcyImportPolicy14 = _TBgpPeerPlcyImportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 14),
    _TBgpPeerPlcyImportPolicy14_Type()
)
tBgpPeerPlcyImportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy14.setStatus("current")


class _TBgpPeerPlcyImportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyImportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyImportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyImportPolicy15_Object = MibTableColumn
tBgpPeerPlcyImportPolicy15 = _TBgpPeerPlcyImportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 15),
    _TBgpPeerPlcyImportPolicy15_Type()
)
tBgpPeerPlcyImportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyImportPolicy15.setStatus("current")


class _TBgpPeerPlcyExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy1_Object = MibTableColumn
tBgpPeerPlcyExportPolicy1 = _TBgpPeerPlcyExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 16),
    _TBgpPeerPlcyExportPolicy1_Type()
)
tBgpPeerPlcyExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy1.setStatus("current")


class _TBgpPeerPlcyExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy2_Object = MibTableColumn
tBgpPeerPlcyExportPolicy2 = _TBgpPeerPlcyExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 17),
    _TBgpPeerPlcyExportPolicy2_Type()
)
tBgpPeerPlcyExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy2.setStatus("current")


class _TBgpPeerPlcyExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy3_Object = MibTableColumn
tBgpPeerPlcyExportPolicy3 = _TBgpPeerPlcyExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 18),
    _TBgpPeerPlcyExportPolicy3_Type()
)
tBgpPeerPlcyExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy3.setStatus("current")


class _TBgpPeerPlcyExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy4_Object = MibTableColumn
tBgpPeerPlcyExportPolicy4 = _TBgpPeerPlcyExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 19),
    _TBgpPeerPlcyExportPolicy4_Type()
)
tBgpPeerPlcyExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy4.setStatus("current")


class _TBgpPeerPlcyExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy5_Object = MibTableColumn
tBgpPeerPlcyExportPolicy5 = _TBgpPeerPlcyExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 20),
    _TBgpPeerPlcyExportPolicy5_Type()
)
tBgpPeerPlcyExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy5.setStatus("current")


class _TBgpPeerPlcyExportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy6_Object = MibTableColumn
tBgpPeerPlcyExportPolicy6 = _TBgpPeerPlcyExportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 21),
    _TBgpPeerPlcyExportPolicy6_Type()
)
tBgpPeerPlcyExportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy6.setStatus("current")


class _TBgpPeerPlcyExportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy7_Object = MibTableColumn
tBgpPeerPlcyExportPolicy7 = _TBgpPeerPlcyExportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 22),
    _TBgpPeerPlcyExportPolicy7_Type()
)
tBgpPeerPlcyExportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy7.setStatus("current")


class _TBgpPeerPlcyExportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy8_Object = MibTableColumn
tBgpPeerPlcyExportPolicy8 = _TBgpPeerPlcyExportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 23),
    _TBgpPeerPlcyExportPolicy8_Type()
)
tBgpPeerPlcyExportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy8.setStatus("current")


class _TBgpPeerPlcyExportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy9_Object = MibTableColumn
tBgpPeerPlcyExportPolicy9 = _TBgpPeerPlcyExportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 24),
    _TBgpPeerPlcyExportPolicy9_Type()
)
tBgpPeerPlcyExportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy9.setStatus("current")


class _TBgpPeerPlcyExportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy10_Object = MibTableColumn
tBgpPeerPlcyExportPolicy10 = _TBgpPeerPlcyExportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 25),
    _TBgpPeerPlcyExportPolicy10_Type()
)
tBgpPeerPlcyExportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy10.setStatus("current")


class _TBgpPeerPlcyExportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy11_Object = MibTableColumn
tBgpPeerPlcyExportPolicy11 = _TBgpPeerPlcyExportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 26),
    _TBgpPeerPlcyExportPolicy11_Type()
)
tBgpPeerPlcyExportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy11.setStatus("current")


class _TBgpPeerPlcyExportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy12_Object = MibTableColumn
tBgpPeerPlcyExportPolicy12 = _TBgpPeerPlcyExportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 27),
    _TBgpPeerPlcyExportPolicy12_Type()
)
tBgpPeerPlcyExportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy12.setStatus("current")


class _TBgpPeerPlcyExportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy13_Object = MibTableColumn
tBgpPeerPlcyExportPolicy13 = _TBgpPeerPlcyExportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 28),
    _TBgpPeerPlcyExportPolicy13_Type()
)
tBgpPeerPlcyExportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy13.setStatus("current")


class _TBgpPeerPlcyExportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy14_Object = MibTableColumn
tBgpPeerPlcyExportPolicy14 = _TBgpPeerPlcyExportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 29),
    _TBgpPeerPlcyExportPolicy14_Type()
)
tBgpPeerPlcyExportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy14.setStatus("current")


class _TBgpPeerPlcyExportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeerPlcyExportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeerPlcyExportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeerPlcyExportPolicy15_Object = MibTableColumn
tBgpPeerPlcyExportPolicy15 = _TBgpPeerPlcyExportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 4, 11, 1, 30),
    _TBgpPeerPlcyExportPolicy15_Type()
)
tBgpPeerPlcyExportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeerPlcyExportPolicy15.setStatus("current")
_TBgpInstanceConfederationObjects_ObjectIdentity = ObjectIdentity
tBgpInstanceConfederationObjects = _TBgpInstanceConfederationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5)
)
_TBgpConfederationTableLastChanged_Type = TimeStamp
_TBgpConfederationTableLastChanged_Object = MibScalar
tBgpConfederationTableLastChanged = _TBgpConfederationTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 1),
    _TBgpConfederationTableLastChanged_Type()
)
tBgpConfederationTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpConfederationTableLastChanged.setStatus("obsolete")
_TBgpConfederationTable_Object = MibTable
tBgpConfederationTable = _TBgpConfederationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 2)
)
if mibBuilder.loadTexts:
    tBgpConfederationTable.setStatus("obsolete")
_TBgpConfederationEntry_Object = MibTableRow
tBgpConfederationEntry = _TBgpConfederationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 2, 1)
)
tBgpConfederationEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpConfederationAS"),
    (0, "TIMETRA-BGP-MIB", "tBgpConfederationMemberAS"),
)
if mibBuilder.loadTexts:
    tBgpConfederationEntry.setStatus("obsolete")
_TBgpConfederationAS_Type = TmnxBgpAutonomousSystem
_TBgpConfederationAS_Object = MibTableColumn
tBgpConfederationAS = _TBgpConfederationAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 2, 1, 1),
    _TBgpConfederationAS_Type()
)
tBgpConfederationAS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpConfederationAS.setStatus("obsolete")
_TBgpConfederationMemberAS_Type = TmnxBgpAutonomousSystem
_TBgpConfederationMemberAS_Object = MibTableColumn
tBgpConfederationMemberAS = _TBgpConfederationMemberAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 2, 1, 2),
    _TBgpConfederationMemberAS_Type()
)
tBgpConfederationMemberAS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpConfederationMemberAS.setStatus("obsolete")
_TBgpConfederationRowStatus_Type = RowStatus
_TBgpConfederationRowStatus_Object = MibTableColumn
tBgpConfederationRowStatus = _TBgpConfederationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 2, 1, 3),
    _TBgpConfederationRowStatus_Type()
)
tBgpConfederationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpConfederationRowStatus.setStatus("obsolete")
_TBgpConfederation4BytTblLstChngd_Type = TimeStamp
_TBgpConfederation4BytTblLstChngd_Object = MibScalar
tBgpConfederation4BytTblLstChngd = _TBgpConfederation4BytTblLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 3),
    _TBgpConfederation4BytTblLstChngd_Type()
)
tBgpConfederation4BytTblLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpConfederation4BytTblLstChngd.setStatus("current")
_TBgpConfederation4ByteTable_Object = MibTable
tBgpConfederation4ByteTable = _TBgpConfederation4ByteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 4)
)
if mibBuilder.loadTexts:
    tBgpConfederation4ByteTable.setStatus("current")
_TBgpConfederation4ByteEntry_Object = MibTableRow
tBgpConfederation4ByteEntry = _TBgpConfederation4ByteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 4, 1)
)
tBgpConfederation4ByteEntry.setIndexNames(
    (0, "TIMETRA-BGP-MIB", "tBgpInstanceIndex"),
    (0, "TIMETRA-BGP-MIB", "tBgpConfederation4ByteAS"),
    (0, "TIMETRA-BGP-MIB", "tBgpConfederation4ByteMemberAS"),
)
if mibBuilder.loadTexts:
    tBgpConfederation4ByteEntry.setStatus("current")
_TBgpConfederation4ByteAS_Type = InetAutonomousSystemNumber
_TBgpConfederation4ByteAS_Object = MibTableColumn
tBgpConfederation4ByteAS = _TBgpConfederation4ByteAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 4, 1, 1),
    _TBgpConfederation4ByteAS_Type()
)
tBgpConfederation4ByteAS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpConfederation4ByteAS.setStatus("current")
_TBgpConfederation4ByteMemberAS_Type = InetAutonomousSystemNumber
_TBgpConfederation4ByteMemberAS_Object = MibTableColumn
tBgpConfederation4ByteMemberAS = _TBgpConfederation4ByteMemberAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 4, 1, 2),
    _TBgpConfederation4ByteMemberAS_Type()
)
tBgpConfederation4ByteMemberAS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpConfederation4ByteMemberAS.setStatus("current")
_TBgpConfederation4ByteRowStatus_Type = RowStatus
_TBgpConfederation4ByteRowStatus_Object = MibTableColumn
tBgpConfederation4ByteRowStatus = _TBgpConfederation4ByteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 5, 4, 1, 3),
    _TBgpConfederation4ByteRowStatus_Type()
)
tBgpConfederation4ByteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpConfederation4ByteRowStatus.setStatus("current")
_TBgpPeeringPolicyObjects_ObjectIdentity = ObjectIdentity
tBgpPeeringPolicyObjects = _TBgpPeeringPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6)
)
_TBgpPeeringPolicyTableLastChngd_Type = TimeStamp
_TBgpPeeringPolicyTableLastChngd_Object = MibScalar
tBgpPeeringPolicyTableLastChngd = _TBgpPeeringPolicyTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 1),
    _TBgpPeeringPolicyTableLastChngd_Type()
)
tBgpPeeringPolicyTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPeeringPolicyTableLastChngd.setStatus("current")
_TBgpPeeringPolicyTable_Object = MibTable
tBgpPeeringPolicyTable = _TBgpPeeringPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2)
)
if mibBuilder.loadTexts:
    tBgpPeeringPolicyTable.setStatus("current")
_TBgpPeeringPolicyEntry_Object = MibTableRow
tBgpPeeringPolicyEntry = _TBgpPeeringPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1)
)
tBgpPeeringPolicyEntry.setIndexNames(
    (1, "TIMETRA-BGP-MIB", "tBgpPeeringPolicyName"),
)
if mibBuilder.loadTexts:
    tBgpPeeringPolicyEntry.setStatus("current")
_TBgpPeeringPolicyName_Type = TNamedItem
_TBgpPeeringPolicyName_Object = MibTableColumn
tBgpPeeringPolicyName = _TBgpPeeringPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 1),
    _TBgpPeeringPolicyName_Type()
)
tBgpPeeringPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tBgpPeeringPolicyName.setStatus("current")
_TBgpPrngPlcyRowStatus_Type = RowStatus
_TBgpPrngPlcyRowStatus_Object = MibTableColumn
tBgpPrngPlcyRowStatus = _TBgpPrngPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 2),
    _TBgpPrngPlcyRowStatus_Type()
)
tBgpPrngPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyRowStatus.setStatus("current")
_TBgpPrngPlcyLastChngd_Type = TimeStamp
_TBgpPrngPlcyLastChngd_Object = MibTableColumn
tBgpPrngPlcyLastChngd = _TBgpPrngPlcyLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 3),
    _TBgpPrngPlcyLastChngd_Type()
)
tBgpPrngPlcyLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBgpPrngPlcyLastChngd.setStatus("current")


class _TBgpPrngPlcyDescription_Type(DisplayString):
    """Custom type tBgpPrngPlcyDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TBgpPrngPlcyDescription_Type.__name__ = "DisplayString"
_TBgpPrngPlcyDescription_Object = MibTableColumn
tBgpPrngPlcyDescription = _TBgpPrngPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 4),
    _TBgpPrngPlcyDescription_Type()
)
tBgpPrngPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyDescription.setStatus("current")


class _TBgpPrngPlcyInheritance_Type(Counter64):
    """Custom type tBgpPrngPlcyInheritance based on Counter64"""
    defaultValue = 0


_TBgpPrngPlcyInheritance_Type.__name__ = "Counter64"
_TBgpPrngPlcyInheritance_Object = MibTableColumn
tBgpPrngPlcyInheritance = _TBgpPrngPlcyInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 5),
    _TBgpPrngPlcyInheritance_Type()
)
tBgpPrngPlcyInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyInheritance.setStatus("current")


class _TBgpPrngPlcyAdvertiseInactiveRts_Type(TruthValue):
    """Custom type tBgpPrngPlcyAdvertiseInactiveRts based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyAdvertiseInactiveRts_Type.__name__ = "TruthValue"
_TBgpPrngPlcyAdvertiseInactiveRts_Object = MibTableColumn
tBgpPrngPlcyAdvertiseInactiveRts = _TBgpPrngPlcyAdvertiseInactiveRts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 6),
    _TBgpPrngPlcyAdvertiseInactiveRts_Type()
)
tBgpPrngPlcyAdvertiseInactiveRts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyAdvertiseInactiveRts.setStatus("current")


class _TBgpPrngPlcyNoAggregatorID_Type(TruthValue):
    """Custom type tBgpPrngPlcyNoAggregatorID based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyNoAggregatorID_Type.__name__ = "TruthValue"
_TBgpPrngPlcyNoAggregatorID_Object = MibTableColumn
tBgpPrngPlcyNoAggregatorID = _TBgpPrngPlcyNoAggregatorID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 7),
    _TBgpPrngPlcyNoAggregatorID_Type()
)
tBgpPrngPlcyNoAggregatorID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyNoAggregatorID.setStatus("current")


class _TBgpPrngPlcyASOverride_Type(TruthValue):
    """Custom type tBgpPrngPlcyASOverride based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyASOverride_Type.__name__ = "TruthValue"
_TBgpPrngPlcyASOverride_Object = MibTableColumn
tBgpPrngPlcyASOverride = _TBgpPrngPlcyASOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 8),
    _TBgpPrngPlcyASOverride_Type()
)
tBgpPrngPlcyASOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyASOverride.setStatus("current")


class _TBgpPrngPlcyAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tBgpPrngPlcyAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TBgpPrngPlcyAuthKeyChain_Object = MibTableColumn
tBgpPrngPlcyAuthKeyChain = _TBgpPrngPlcyAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 9),
    _TBgpPrngPlcyAuthKeyChain_Type()
)
tBgpPrngPlcyAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyAuthKeyChain.setStatus("current")


class _TBgpPrngPlcyMd5Auth_Type(TruthValue):
    """Custom type tBgpPrngPlcyMd5Auth based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyMd5Auth_Type.__name__ = "TruthValue"
_TBgpPrngPlcyMd5Auth_Object = MibTableColumn
tBgpPrngPlcyMd5Auth = _TBgpPrngPlcyMd5Auth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 10),
    _TBgpPrngPlcyMd5Auth_Type()
)
tBgpPrngPlcyMd5Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMd5Auth.setStatus("current")


class _TBgpPrngPlcyMd5AuthKey_Type(OctetString):
    """Custom type tBgpPrngPlcyMd5AuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgpPrngPlcyMd5AuthKey_Type.__name__ = "OctetString"
_TBgpPrngPlcyMd5AuthKey_Object = MibTableColumn
tBgpPrngPlcyMd5AuthKey = _TBgpPrngPlcyMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 11),
    _TBgpPrngPlcyMd5AuthKey_Type()
)
tBgpPrngPlcyMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMd5AuthKey.setStatus("current")


class _TBgpPrngPlcyClusterId_Type(IpAddress):
    """Custom type tBgpPrngPlcyClusterId based on IpAddress"""
    defaultHexValue = "00000000"


_TBgpPrngPlcyClusterId_Type.__name__ = "IpAddress"
_TBgpPrngPlcyClusterId_Object = MibTableColumn
tBgpPrngPlcyClusterId = _TBgpPrngPlcyClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 12),
    _TBgpPrngPlcyClusterId_Type()
)
tBgpPrngPlcyClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyClusterId.setStatus("current")


class _TBgpPrngPlcyConnectRetry_Type(BgpConnectRetryTime):
    """Custom type tBgpPrngPlcyConnectRetry based on BgpConnectRetryTime"""
    defaultValue = 120


_TBgpPrngPlcyConnectRetry_Type.__name__ = "BgpConnectRetryTime"
_TBgpPrngPlcyConnectRetry_Object = MibTableColumn
tBgpPrngPlcyConnectRetry = _TBgpPrngPlcyConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 13),
    _TBgpPrngPlcyConnectRetry_Type()
)
tBgpPrngPlcyConnectRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyConnectRetry.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPrngPlcyConnectRetry.setUnits("seconds")


class _TBgpPrngPlcyDampening_Type(TruthValue):
    """Custom type tBgpPrngPlcyDampening based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyDampening_Type.__name__ = "TruthValue"
_TBgpPrngPlcyDampening_Object = MibTableColumn
tBgpPrngPlcyDampening = _TBgpPrngPlcyDampening_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 14),
    _TBgpPrngPlcyDampening_Type()
)
tBgpPrngPlcyDampening.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyDampening.setStatus("current")


class _TBgpPrngPlcyDisableClientReflect_Type(TruthValue):
    """Custom type tBgpPrngPlcyDisableClientReflect based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyDisableClientReflect_Type.__name__ = "TruthValue"
_TBgpPrngPlcyDisableClientReflect_Object = MibTableColumn
tBgpPrngPlcyDisableClientReflect = _TBgpPrngPlcyDisableClientReflect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 15),
    _TBgpPrngPlcyDisableClientReflect_Type()
)
tBgpPrngPlcyDisableClientReflect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyDisableClientReflect.setStatus("current")


class _TBgpPrngPlcyDisableComms_Type(TruthValue):
    """Custom type tBgpPrngPlcyDisableComms based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyDisableComms_Type.__name__ = "TruthValue"
_TBgpPrngPlcyDisableComms_Object = MibTableColumn
tBgpPrngPlcyDisableComms = _TBgpPrngPlcyDisableComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 16),
    _TBgpPrngPlcyDisableComms_Type()
)
tBgpPrngPlcyDisableComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyDisableComms.setStatus("current")


class _TBgpPrngPlcyDisableExtComms_Type(TruthValue):
    """Custom type tBgpPrngPlcyDisableExtComms based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyDisableExtComms_Type.__name__ = "TruthValue"
_TBgpPrngPlcyDisableExtComms_Object = MibTableColumn
tBgpPrngPlcyDisableExtComms = _TBgpPrngPlcyDisableExtComms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 17),
    _TBgpPrngPlcyDisableExtComms_Type()
)
tBgpPrngPlcyDisableExtComms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyDisableExtComms.setStatus("current")


class _TBgpPrngPlcyDisableFEFailover_Type(TruthValue):
    """Custom type tBgpPrngPlcyDisableFEFailover based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyDisableFEFailover_Type.__name__ = "TruthValue"
_TBgpPrngPlcyDisableFEFailover_Object = MibTableColumn
tBgpPrngPlcyDisableFEFailover = _TBgpPrngPlcyDisableFEFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 18),
    _TBgpPrngPlcyDisableFEFailover_Type()
)
tBgpPrngPlcyDisableFEFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyDisableFEFailover.setStatus("current")


class _TBgpPrngPlcyImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyImportPolicy1_Object = MibTableColumn
tBgpPrngPlcyImportPolicy1 = _TBgpPrngPlcyImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 19),
    _TBgpPrngPlcyImportPolicy1_Type()
)
tBgpPrngPlcyImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyImportPolicy1.setStatus("obsolete")


class _TBgpPrngPlcyImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyImportPolicy2_Object = MibTableColumn
tBgpPrngPlcyImportPolicy2 = _TBgpPrngPlcyImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 20),
    _TBgpPrngPlcyImportPolicy2_Type()
)
tBgpPrngPlcyImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyImportPolicy2.setStatus("obsolete")


class _TBgpPrngPlcyImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyImportPolicy3_Object = MibTableColumn
tBgpPrngPlcyImportPolicy3 = _TBgpPrngPlcyImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 21),
    _TBgpPrngPlcyImportPolicy3_Type()
)
tBgpPrngPlcyImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyImportPolicy3.setStatus("obsolete")


class _TBgpPrngPlcyImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyImportPolicy4_Object = MibTableColumn
tBgpPrngPlcyImportPolicy4 = _TBgpPrngPlcyImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 22),
    _TBgpPrngPlcyImportPolicy4_Type()
)
tBgpPrngPlcyImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyImportPolicy4.setStatus("obsolete")


class _TBgpPrngPlcyImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyImportPolicy5_Object = MibTableColumn
tBgpPrngPlcyImportPolicy5 = _TBgpPrngPlcyImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 23),
    _TBgpPrngPlcyImportPolicy5_Type()
)
tBgpPrngPlcyImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyImportPolicy5.setStatus("obsolete")


class _TBgpPrngPlcyExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyExportPolicy1_Object = MibTableColumn
tBgpPrngPlcyExportPolicy1 = _TBgpPrngPlcyExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 24),
    _TBgpPrngPlcyExportPolicy1_Type()
)
tBgpPrngPlcyExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyExportPolicy1.setStatus("obsolete")


class _TBgpPrngPlcyExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyExportPolicy2_Object = MibTableColumn
tBgpPrngPlcyExportPolicy2 = _TBgpPrngPlcyExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 25),
    _TBgpPrngPlcyExportPolicy2_Type()
)
tBgpPrngPlcyExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyExportPolicy2.setStatus("obsolete")


class _TBgpPrngPlcyExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyExportPolicy3_Object = MibTableColumn
tBgpPrngPlcyExportPolicy3 = _TBgpPrngPlcyExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 26),
    _TBgpPrngPlcyExportPolicy3_Type()
)
tBgpPrngPlcyExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyExportPolicy3.setStatus("obsolete")


class _TBgpPrngPlcyExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyExportPolicy4_Object = MibTableColumn
tBgpPrngPlcyExportPolicy4 = _TBgpPrngPlcyExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 27),
    _TBgpPrngPlcyExportPolicy4_Type()
)
tBgpPrngPlcyExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyExportPolicy4.setStatus("obsolete")


class _TBgpPrngPlcyExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPrngPlcyExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPrngPlcyExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPrngPlcyExportPolicy5_Object = MibTableColumn
tBgpPrngPlcyExportPolicy5 = _TBgpPrngPlcyExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 28),
    _TBgpPrngPlcyExportPolicy5_Type()
)
tBgpPrngPlcyExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyExportPolicy5.setStatus("obsolete")


class _TBgpPrngPlcyHoldTime_Type(BgpHoldTime):
    """Custom type tBgpPrngPlcyHoldTime based on BgpHoldTime"""
    defaultValue = 90


_TBgpPrngPlcyHoldTime_Type.__name__ = "BgpHoldTime"
_TBgpPrngPlcyHoldTime_Object = MibTableColumn
tBgpPrngPlcyHoldTime = _TBgpPrngPlcyHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 29),
    _TBgpPrngPlcyHoldTime_Type()
)
tBgpPrngPlcyHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPrngPlcyHoldTime.setUnits("seconds")


class _TBgpPrngPlcyKeepAlive_Type(BgpKeepAliveTime):
    """Custom type tBgpPrngPlcyKeepAlive based on BgpKeepAliveTime"""
    defaultValue = 30


_TBgpPrngPlcyKeepAlive_Type.__name__ = "BgpKeepAliveTime"
_TBgpPrngPlcyKeepAlive_Object = MibTableColumn
tBgpPrngPlcyKeepAlive = _TBgpPrngPlcyKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 30),
    _TBgpPrngPlcyKeepAlive_Type()
)
tBgpPrngPlcyKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPrngPlcyKeepAlive.setUnits("seconds")
_TBgpPrngPlcyLocalAddressType_Type = InetAddressType
_TBgpPrngPlcyLocalAddressType_Object = MibTableColumn
tBgpPrngPlcyLocalAddressType = _TBgpPrngPlcyLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 31),
    _TBgpPrngPlcyLocalAddressType_Type()
)
tBgpPrngPlcyLocalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyLocalAddressType.setStatus("current")


class _TBgpPrngPlcyLocalAddress_Type(InetAddress):
    """Custom type tBgpPrngPlcyLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TBgpPrngPlcyLocalAddress_Type.__name__ = "InetAddress"
_TBgpPrngPlcyLocalAddress_Object = MibTableColumn
tBgpPrngPlcyLocalAddress = _TBgpPrngPlcyLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 32),
    _TBgpPrngPlcyLocalAddress_Type()
)
tBgpPrngPlcyLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyLocalAddress.setStatus("current")


class _TBgpPrngPlcyLocalAS_Type(InetAutonomousSystemNumber):
    """Custom type tBgpPrngPlcyLocalAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TBgpPrngPlcyLocalAS_Type.__name__ = "InetAutonomousSystemNumber"
_TBgpPrngPlcyLocalAS_Object = MibTableColumn
tBgpPrngPlcyLocalAS = _TBgpPrngPlcyLocalAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 33),
    _TBgpPrngPlcyLocalAS_Type()
)
tBgpPrngPlcyLocalAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyLocalAS.setStatus("current")


class _TBgpPrngPlcyLocalASPrivate_Type(TruthValue):
    """Custom type tBgpPrngPlcyLocalASPrivate based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyLocalASPrivate_Type.__name__ = "TruthValue"
_TBgpPrngPlcyLocalASPrivate_Object = MibTableColumn
tBgpPrngPlcyLocalASPrivate = _TBgpPrngPlcyLocalASPrivate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 34),
    _TBgpPrngPlcyLocalASPrivate_Type()
)
tBgpPrngPlcyLocalASPrivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyLocalASPrivate.setStatus("current")


class _TBgpPrngPlcyLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tBgpPrngPlcyLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 100


_TBgpPrngPlcyLocalPreference_Type.__name__ = "TmnxBgpLocalPreference"
_TBgpPrngPlcyLocalPreference_Object = MibTableColumn
tBgpPrngPlcyLocalPreference = _TBgpPrngPlcyLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 35),
    _TBgpPrngPlcyLocalPreference_Type()
)
tBgpPrngPlcyLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyLocalPreference.setStatus("current")


class _TBgpPrngPlcyLoopDetect_Type(BgpLoopDetect):
    """Custom type tBgpPrngPlcyLoopDetect based on BgpLoopDetect"""
    defaultValue = 2


_TBgpPrngPlcyLoopDetect_Type.__name__ = "BgpLoopDetect"
_TBgpPrngPlcyLoopDetect_Object = MibTableColumn
tBgpPrngPlcyLoopDetect = _TBgpPrngPlcyLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 36),
    _TBgpPrngPlcyLoopDetect_Type()
)
tBgpPrngPlcyLoopDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyLoopDetect.setStatus("current")


class _TBgpPrngPlcyMEDSource_Type(BgpMEDSource):
    """Custom type tBgpPrngPlcyMEDSource based on BgpMEDSource"""
    defaultValue = 3


_TBgpPrngPlcyMEDSource_Type.__name__ = "BgpMEDSource"
_TBgpPrngPlcyMEDSource_Object = MibTableColumn
tBgpPrngPlcyMEDSource = _TBgpPrngPlcyMEDSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 37),
    _TBgpPrngPlcyMEDSource_Type()
)
tBgpPrngPlcyMEDSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMEDSource.setStatus("current")


class _TBgpPrngPlcyMEDValue_Type(BgpMEDValue):
    """Custom type tBgpPrngPlcyMEDValue based on BgpMEDValue"""
    defaultValue = 0


_TBgpPrngPlcyMEDValue_Type.__name__ = "BgpMEDValue"
_TBgpPrngPlcyMEDValue_Object = MibTableColumn
tBgpPrngPlcyMEDValue = _TBgpPrngPlcyMEDValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 38),
    _TBgpPrngPlcyMEDValue_Type()
)
tBgpPrngPlcyMEDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMEDValue.setStatus("current")


class _TBgpPrngPlcyMinASOrigination_Type(BgpMinASOriginationTime):
    """Custom type tBgpPrngPlcyMinASOrigination based on BgpMinASOriginationTime"""
    defaultValue = 15


_TBgpPrngPlcyMinASOrigination_Type.__name__ = "BgpMinASOriginationTime"
_TBgpPrngPlcyMinASOrigination_Object = MibTableColumn
tBgpPrngPlcyMinASOrigination = _TBgpPrngPlcyMinASOrigination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 39),
    _TBgpPrngPlcyMinASOrigination_Type()
)
tBgpPrngPlcyMinASOrigination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMinASOrigination.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMinASOrigination.setUnits("seconds")


class _TBgpPrngPlcyMinRteAdvertisement_Type(BgpMinRouteAdvertisement):
    """Custom type tBgpPrngPlcyMinRteAdvertisement based on BgpMinRouteAdvertisement"""
    defaultValue = 30


_TBgpPrngPlcyMinRteAdvertisement_Type.__name__ = "BgpMinRouteAdvertisement"
_TBgpPrngPlcyMinRteAdvertisement_Object = MibTableColumn
tBgpPrngPlcyMinRteAdvertisement = _TBgpPrngPlcyMinRteAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 40),
    _TBgpPrngPlcyMinRteAdvertisement_Type()
)
tBgpPrngPlcyMinRteAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMinRteAdvertisement.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMinRteAdvertisement.setUnits("seconds")


class _TBgpPrngPlcyMultihop_Type(BgpTimeToLive):
    """Custom type tBgpPrngPlcyMultihop based on BgpTimeToLive"""
    defaultValue = 0


_TBgpPrngPlcyMultihop_Type.__name__ = "BgpTimeToLive"
_TBgpPrngPlcyMultihop_Object = MibTableColumn
tBgpPrngPlcyMultihop = _TBgpPrngPlcyMultihop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 41),
    _TBgpPrngPlcyMultihop_Type()
)
tBgpPrngPlcyMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMultihop.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMultihop.setUnits("TTL hops")


class _TBgpPrngPlcyNextHopSelf_Type(TruthValue):
    """Custom type tBgpPrngPlcyNextHopSelf based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyNextHopSelf_Type.__name__ = "TruthValue"
_TBgpPrngPlcyNextHopSelf_Object = MibTableColumn
tBgpPrngPlcyNextHopSelf = _TBgpPrngPlcyNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 42),
    _TBgpPrngPlcyNextHopSelf_Type()
)
tBgpPrngPlcyNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyNextHopSelf.setStatus("current")


class _TBgpPrngPlcyPassive_Type(TruthValue):
    """Custom type tBgpPrngPlcyPassive based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyPassive_Type.__name__ = "TruthValue"
_TBgpPrngPlcyPassive_Object = MibTableColumn
tBgpPrngPlcyPassive = _TBgpPrngPlcyPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 43),
    _TBgpPrngPlcyPassive_Type()
)
tBgpPrngPlcyPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyPassive.setStatus("current")


class _TBgpPrngPlcyPeerAS_Type(InetAutonomousSystemNumber):
    """Custom type tBgpPrngPlcyPeerAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TBgpPrngPlcyPeerAS_Type.__name__ = "InetAutonomousSystemNumber"
_TBgpPrngPlcyPeerAS_Object = MibTableColumn
tBgpPrngPlcyPeerAS = _TBgpPrngPlcyPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 44),
    _TBgpPrngPlcyPeerAS_Type()
)
tBgpPrngPlcyPeerAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyPeerAS.setStatus("current")


class _TBgpPrngPlcyPreference_Type(TmnxBgpPreference):
    """Custom type tBgpPrngPlcyPreference based on TmnxBgpPreference"""
    defaultValue = 170

    subtypeSpec = TmnxBgpPreference.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TBgpPrngPlcyPreference_Type.__name__ = "TmnxBgpPreference"
_TBgpPrngPlcyPreference_Object = MibTableColumn
tBgpPrngPlcyPreference = _TBgpPrngPlcyPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 45),
    _TBgpPrngPlcyPreference_Type()
)
tBgpPrngPlcyPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyPreference.setStatus("current")


class _TBgpPrngPlcyMaxPrefix_Type(BgpPrefixLimit):
    """Custom type tBgpPrngPlcyMaxPrefix based on BgpPrefixLimit"""
    defaultValue = 0


_TBgpPrngPlcyMaxPrefix_Type.__name__ = "BgpPrefixLimit"
_TBgpPrngPlcyMaxPrefix_Object = MibTableColumn
tBgpPrngPlcyMaxPrefix = _TBgpPrngPlcyMaxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 46),
    _TBgpPrngPlcyMaxPrefix_Type()
)
tBgpPrngPlcyMaxPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMaxPrefix.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMaxPrefix.setUnits("number of routes")


class _TBgpPrngPlcyRemovePrivateAS_Type(TruthValue):
    """Custom type tBgpPrngPlcyRemovePrivateAS based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyRemovePrivateAS_Type.__name__ = "TruthValue"
_TBgpPrngPlcyRemovePrivateAS_Object = MibTableColumn
tBgpPrngPlcyRemovePrivateAS = _TBgpPrngPlcyRemovePrivateAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 47),
    _TBgpPrngPlcyRemovePrivateAS_Type()
)
tBgpPrngPlcyRemovePrivateAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyRemovePrivateAS.setStatus("current")


class _TBgpPrngPlcyMinTTLValue_Type(Unsigned32):
    """Custom type tBgpPrngPlcyMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TBgpPrngPlcyMinTTLValue_Type.__name__ = "Unsigned32"
_TBgpPrngPlcyMinTTLValue_Object = MibTableColumn
tBgpPrngPlcyMinTTLValue = _TBgpPrngPlcyMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 48),
    _TBgpPrngPlcyMinTTLValue_Type()
)
tBgpPrngPlcyMinTTLValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMinTTLValue.setStatus("current")


class _TBgpPrngPlcyPeerType_Type(BgpPeerType):
    """Custom type tBgpPrngPlcyPeerType based on BgpPeerType"""
    defaultValue = 1


_TBgpPrngPlcyPeerType_Type.__name__ = "BgpPeerType"
_TBgpPrngPlcyPeerType_Object = MibTableColumn
tBgpPrngPlcyPeerType = _TBgpPrngPlcyPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 49),
    _TBgpPrngPlcyPeerType_Type()
)
tBgpPrngPlcyPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyPeerType.setStatus("current")


class _TBgpPrngPlcyDisable4ByteASN_Type(TruthValue):
    """Custom type tBgpPrngPlcyDisable4ByteASN based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyDisable4ByteASN_Type.__name__ = "TruthValue"
_TBgpPrngPlcyDisable4ByteASN_Object = MibTableColumn
tBgpPrngPlcyDisable4ByteASN = _TBgpPrngPlcyDisable4ByteASN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 50),
    _TBgpPrngPlcyDisable4ByteASN_Type()
)
tBgpPrngPlcyDisable4ByteASN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyDisable4ByteASN.setStatus("current")


class _TBgpPrngPlcyRemovePrivateASLmtd_Type(TruthValue):
    """Custom type tBgpPrngPlcyRemovePrivateASLmtd based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyRemovePrivateASLmtd_Type.__name__ = "TruthValue"
_TBgpPrngPlcyRemovePrivateASLmtd_Object = MibTableColumn
tBgpPrngPlcyRemovePrivateASLmtd = _TBgpPrngPlcyRemovePrivateASLmtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 51),
    _TBgpPrngPlcyRemovePrivateASLmtd_Type()
)
tBgpPrngPlcyRemovePrivateASLmtd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyRemovePrivateASLmtd.setStatus("current")


class _TBgpPrngPlcyMaxPrefixLogOnly_Type(TruthValue):
    """Custom type tBgpPrngPlcyMaxPrefixLogOnly based on TruthValue"""
    defaultValue = 2


_TBgpPrngPlcyMaxPrefixLogOnly_Type.__name__ = "TruthValue"
_TBgpPrngPlcyMaxPrefixLogOnly_Object = MibTableColumn
tBgpPrngPlcyMaxPrefixLogOnly = _TBgpPrngPlcyMaxPrefixLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 52),
    _TBgpPrngPlcyMaxPrefixLogOnly_Type()
)
tBgpPrngPlcyMaxPrefixLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMaxPrefixLogOnly.setStatus("current")


class _TBgpPrngPlcyMaxPrefixThreshold_Type(Unsigned32):
    """Custom type tBgpPrngPlcyMaxPrefixThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TBgpPrngPlcyMaxPrefixThreshold_Type.__name__ = "Unsigned32"
_TBgpPrngPlcyMaxPrefixThreshold_Object = MibTableColumn
tBgpPrngPlcyMaxPrefixThreshold = _TBgpPrngPlcyMaxPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 2, 1, 53),
    _TBgpPrngPlcyMaxPrefixThreshold_Type()
)
tBgpPrngPlcyMaxPrefixThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMaxPrefixThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tBgpPrngPlcyMaxPrefixThreshold.setUnits("percentage")
_TBgpPeeringPlcyTable_Object = MibTable
tBgpPeeringPlcyTable = _TBgpPeeringPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3)
)
if mibBuilder.loadTexts:
    tBgpPeeringPlcyTable.setStatus("current")
_TBgpPeeringPlcyEntry_Object = MibTableRow
tBgpPeeringPlcyEntry = _TBgpPeeringPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tBgpPeeringPlcyEntry.setStatus("current")


class _TBgpPeeringPlcyImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy1_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy1 = _TBgpPeeringPlcyImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 1),
    _TBgpPeeringPlcyImportPolicy1_Type()
)
tBgpPeeringPlcyImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy1.setStatus("current")


class _TBgpPeeringPlcyImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy2_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy2 = _TBgpPeeringPlcyImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 2),
    _TBgpPeeringPlcyImportPolicy2_Type()
)
tBgpPeeringPlcyImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy2.setStatus("current")


class _TBgpPeeringPlcyImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy3_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy3 = _TBgpPeeringPlcyImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 3),
    _TBgpPeeringPlcyImportPolicy3_Type()
)
tBgpPeeringPlcyImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy3.setStatus("current")


class _TBgpPeeringPlcyImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy4_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy4 = _TBgpPeeringPlcyImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 4),
    _TBgpPeeringPlcyImportPolicy4_Type()
)
tBgpPeeringPlcyImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy4.setStatus("current")


class _TBgpPeeringPlcyImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy5_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy5 = _TBgpPeeringPlcyImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 5),
    _TBgpPeeringPlcyImportPolicy5_Type()
)
tBgpPeeringPlcyImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy5.setStatus("current")


class _TBgpPeeringPlcyImportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy6_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy6 = _TBgpPeeringPlcyImportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 6),
    _TBgpPeeringPlcyImportPolicy6_Type()
)
tBgpPeeringPlcyImportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy6.setStatus("current")


class _TBgpPeeringPlcyImportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy7_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy7 = _TBgpPeeringPlcyImportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 7),
    _TBgpPeeringPlcyImportPolicy7_Type()
)
tBgpPeeringPlcyImportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy7.setStatus("current")


class _TBgpPeeringPlcyImportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy8_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy8 = _TBgpPeeringPlcyImportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 8),
    _TBgpPeeringPlcyImportPolicy8_Type()
)
tBgpPeeringPlcyImportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy8.setStatus("current")


class _TBgpPeeringPlcyImportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy9_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy9 = _TBgpPeeringPlcyImportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 9),
    _TBgpPeeringPlcyImportPolicy9_Type()
)
tBgpPeeringPlcyImportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy9.setStatus("current")


class _TBgpPeeringPlcyImportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy10_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy10 = _TBgpPeeringPlcyImportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 10),
    _TBgpPeeringPlcyImportPolicy10_Type()
)
tBgpPeeringPlcyImportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy10.setStatus("current")


class _TBgpPeeringPlcyImportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy11_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy11 = _TBgpPeeringPlcyImportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 11),
    _TBgpPeeringPlcyImportPolicy11_Type()
)
tBgpPeeringPlcyImportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy11.setStatus("current")


class _TBgpPeeringPlcyImportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy12_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy12 = _TBgpPeeringPlcyImportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 12),
    _TBgpPeeringPlcyImportPolicy12_Type()
)
tBgpPeeringPlcyImportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy12.setStatus("current")


class _TBgpPeeringPlcyImportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy13_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy13 = _TBgpPeeringPlcyImportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 13),
    _TBgpPeeringPlcyImportPolicy13_Type()
)
tBgpPeeringPlcyImportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy13.setStatus("current")


class _TBgpPeeringPlcyImportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy14_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy14 = _TBgpPeeringPlcyImportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 14),
    _TBgpPeeringPlcyImportPolicy14_Type()
)
tBgpPeeringPlcyImportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy14.setStatus("current")


class _TBgpPeeringPlcyImportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyImportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyImportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyImportPolicy15_Object = MibTableColumn
tBgpPeeringPlcyImportPolicy15 = _TBgpPeeringPlcyImportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 15),
    _TBgpPeeringPlcyImportPolicy15_Type()
)
tBgpPeeringPlcyImportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyImportPolicy15.setStatus("current")


class _TBgpPeeringPlcyExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy1_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy1 = _TBgpPeeringPlcyExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 16),
    _TBgpPeeringPlcyExportPolicy1_Type()
)
tBgpPeeringPlcyExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy1.setStatus("current")


class _TBgpPeeringPlcyExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy2_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy2 = _TBgpPeeringPlcyExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 17),
    _TBgpPeeringPlcyExportPolicy2_Type()
)
tBgpPeeringPlcyExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy2.setStatus("current")


class _TBgpPeeringPlcyExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy3_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy3 = _TBgpPeeringPlcyExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 18),
    _TBgpPeeringPlcyExportPolicy3_Type()
)
tBgpPeeringPlcyExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy3.setStatus("current")


class _TBgpPeeringPlcyExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy4_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy4 = _TBgpPeeringPlcyExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 19),
    _TBgpPeeringPlcyExportPolicy4_Type()
)
tBgpPeeringPlcyExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy4.setStatus("current")


class _TBgpPeeringPlcyExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy5_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy5 = _TBgpPeeringPlcyExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 20),
    _TBgpPeeringPlcyExportPolicy5_Type()
)
tBgpPeeringPlcyExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy5.setStatus("current")


class _TBgpPeeringPlcyExportPolicy6_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy6 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy6_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy6_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy6 = _TBgpPeeringPlcyExportPolicy6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 21),
    _TBgpPeeringPlcyExportPolicy6_Type()
)
tBgpPeeringPlcyExportPolicy6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy6.setStatus("current")


class _TBgpPeeringPlcyExportPolicy7_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy7 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy7_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy7_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy7 = _TBgpPeeringPlcyExportPolicy7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 22),
    _TBgpPeeringPlcyExportPolicy7_Type()
)
tBgpPeeringPlcyExportPolicy7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy7.setStatus("current")


class _TBgpPeeringPlcyExportPolicy8_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy8 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy8_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy8_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy8 = _TBgpPeeringPlcyExportPolicy8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 23),
    _TBgpPeeringPlcyExportPolicy8_Type()
)
tBgpPeeringPlcyExportPolicy8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy8.setStatus("current")


class _TBgpPeeringPlcyExportPolicy9_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy9 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy9_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy9_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy9 = _TBgpPeeringPlcyExportPolicy9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 24),
    _TBgpPeeringPlcyExportPolicy9_Type()
)
tBgpPeeringPlcyExportPolicy9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy9.setStatus("current")


class _TBgpPeeringPlcyExportPolicy10_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy10 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy10_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy10_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy10 = _TBgpPeeringPlcyExportPolicy10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 25),
    _TBgpPeeringPlcyExportPolicy10_Type()
)
tBgpPeeringPlcyExportPolicy10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy10.setStatus("current")


class _TBgpPeeringPlcyExportPolicy11_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy11 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy11_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy11_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy11 = _TBgpPeeringPlcyExportPolicy11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 26),
    _TBgpPeeringPlcyExportPolicy11_Type()
)
tBgpPeeringPlcyExportPolicy11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy11.setStatus("current")


class _TBgpPeeringPlcyExportPolicy12_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy12 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy12_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy12_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy12 = _TBgpPeeringPlcyExportPolicy12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 27),
    _TBgpPeeringPlcyExportPolicy12_Type()
)
tBgpPeeringPlcyExportPolicy12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy12.setStatus("current")


class _TBgpPeeringPlcyExportPolicy13_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy13 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy13_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy13_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy13 = _TBgpPeeringPlcyExportPolicy13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 28),
    _TBgpPeeringPlcyExportPolicy13_Type()
)
tBgpPeeringPlcyExportPolicy13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy13.setStatus("current")


class _TBgpPeeringPlcyExportPolicy14_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy14 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy14_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy14_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy14 = _TBgpPeeringPlcyExportPolicy14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 29),
    _TBgpPeeringPlcyExportPolicy14_Type()
)
tBgpPeeringPlcyExportPolicy14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy14.setStatus("current")


class _TBgpPeeringPlcyExportPolicy15_Type(TPolicyStatementNameOrEmpty):
    """Custom type tBgpPeeringPlcyExportPolicy15 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TBgpPeeringPlcyExportPolicy15_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TBgpPeeringPlcyExportPolicy15_Object = MibTableColumn
tBgpPeeringPlcyExportPolicy15 = _TBgpPeeringPlcyExportPolicy15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 6, 3, 1, 30),
    _TBgpPeeringPlcyExportPolicy15_Type()
)
tBgpPeeringPlcyExportPolicy15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tBgpPeeringPlcyExportPolicy15.setStatus("current")
_TBgpNotificationObjs_ObjectIdentity = ObjectIdentity
tBgpNotificationObjs = _TBgpNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7)
)
_TBgpPeerNgAddrType_Type = InetAddressType
_TBgpPeerNgAddrType_Object = MibScalar
tBgpPeerNgAddrType = _TBgpPeerNgAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 1),
    _TBgpPeerNgAddrType_Type()
)
tBgpPeerNgAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpPeerNgAddrType.setStatus("current")
_TBgpPeerNgAddr_Type = InetAddress
_TBgpPeerNgAddr_Object = MibScalar
tBgpPeerNgAddr = _TBgpPeerNgAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 2),
    _TBgpPeerNgAddr_Type()
)
tBgpPeerNgAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpPeerNgAddr.setStatus("current")
_TBgpFlowspecExtCommunityAction_Type = TmnxBgpFlowRouteExtCommAction
_TBgpFlowspecExtCommunityAction_Object = MibScalar
tBgpFlowspecExtCommunityAction = _TBgpFlowspecExtCommunityAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 3),
    _TBgpFlowspecExtCommunityAction_Type()
)
tBgpFlowspecExtCommunityAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpFlowspecExtCommunityAction.setStatus("current")
_TBgpPeerFlowRouteDestAddrType_Type = InetAddressType
_TBgpPeerFlowRouteDestAddrType_Object = MibScalar
tBgpPeerFlowRouteDestAddrType = _TBgpPeerFlowRouteDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 4),
    _TBgpPeerFlowRouteDestAddrType_Type()
)
tBgpPeerFlowRouteDestAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpPeerFlowRouteDestAddrType.setStatus("current")
_TBgpPeerFlowRouteDestAddr_Type = InetAddress
_TBgpPeerFlowRouteDestAddr_Object = MibScalar
tBgpPeerFlowRouteDestAddr = _TBgpPeerFlowRouteDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 5),
    _TBgpPeerFlowRouteDestAddr_Type()
)
tBgpPeerFlowRouteDestAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpPeerFlowRouteDestAddr.setStatus("current")


class _TBgpFlowRouteInvalidReason_Type(DisplayString):
    """Custom type tBgpFlowRouteInvalidReason based on DisplayString"""
    defaultHexValue = ""


_TBgpFlowRouteInvalidReason_Type.__name__ = "DisplayString"
_TBgpFlowRouteInvalidReason_Object = MibScalar
tBgpFlowRouteInvalidReason = _TBgpFlowRouteInvalidReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 6),
    _TBgpFlowRouteInvalidReason_Type()
)
tBgpFlowRouteInvalidReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpFlowRouteInvalidReason.setStatus("current")


class _TBgpFlowRouteNLRI_Type(OctetString):
    """Custom type tBgpFlowRouteNLRI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TBgpFlowRouteNLRI_Type.__name__ = "OctetString"
_TBgpFlowRouteNLRI_Object = MibScalar
tBgpFlowRouteNLRI = _TBgpFlowRouteNLRI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 7),
    _TBgpFlowRouteNLRI_Type()
)
tBgpFlowRouteNLRI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpFlowRouteNLRI.setStatus("current")


class _TBgpFlowspecExtCommActionValue_Type(OctetString):
    """Custom type tBgpFlowspecExtCommActionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TBgpFlowspecExtCommActionValue_Type.__name__ = "OctetString"
_TBgpFlowspecExtCommActionValue_Object = MibScalar
tBgpFlowspecExtCommActionValue = _TBgpFlowspecExtCommActionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 8),
    _TBgpFlowspecExtCommActionValue_Type()
)
tBgpFlowspecExtCommActionValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpFlowspecExtCommActionValue.setStatus("current")
_TBgp4OptTransPathAttrType_Type = Integer32
_TBgp4OptTransPathAttrType_Object = MibScalar
tBgp4OptTransPathAttrType = _TBgp4OptTransPathAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 9),
    _TBgp4OptTransPathAttrType_Type()
)
tBgp4OptTransPathAttrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4OptTransPathAttrType.setStatus("obsolete")
_TBgp4OptTransPathAttrLength_Type = Unsigned32
_TBgp4OptTransPathAttrLength_Object = MibScalar
tBgp4OptTransPathAttrLength = _TBgp4OptTransPathAttrLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 10),
    _TBgp4OptTransPathAttrLength_Type()
)
tBgp4OptTransPathAttrLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4OptTransPathAttrLength.setStatus("obsolete")


class _TBgp4OptTransPathAttribute_Type(OctetString):
    """Custom type tBgp4OptTransPathAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_TBgp4OptTransPathAttribute_Type.__name__ = "OctetString"
_TBgp4OptTransPathAttribute_Object = MibScalar
tBgp4OptTransPathAttribute = _TBgp4OptTransPathAttribute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 11),
    _TBgp4OptTransPathAttribute_Type()
)
tBgp4OptTransPathAttribute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4OptTransPathAttribute.setStatus("obsolete")
_TBgp4OTWithdrawnRouteLength_Type = Unsigned32
_TBgp4OTWithdrawnRouteLength_Object = MibScalar
tBgp4OTWithdrawnRouteLength = _TBgp4OTWithdrawnRouteLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 12),
    _TBgp4OTWithdrawnRouteLength_Type()
)
tBgp4OTWithdrawnRouteLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4OTWithdrawnRouteLength.setStatus("obsolete")


class _TBgp4OTWithdrawnRoutePrefix_Type(OctetString):
    """Custom type tBgp4OTWithdrawnRoutePrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgp4OTWithdrawnRoutePrefix_Type.__name__ = "OctetString"
_TBgp4OTWithdrawnRoutePrefix_Object = MibScalar
tBgp4OTWithdrawnRoutePrefix = _TBgp4OTWithdrawnRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 13),
    _TBgp4OTWithdrawnRoutePrefix_Type()
)
tBgp4OTWithdrawnRoutePrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4OTWithdrawnRoutePrefix.setStatus("obsolete")


class _TBgpRouteInvalidReason_Type(DisplayString):
    """Custom type tBgpRouteInvalidReason based on DisplayString"""
    defaultHexValue = ""


_TBgpRouteInvalidReason_Type.__name__ = "DisplayString"
_TBgpRouteInvalidReason_Object = MibScalar
tBgpRouteInvalidReason = _TBgpRouteInvalidReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 14),
    _TBgpRouteInvalidReason_Type()
)
tBgpRouteInvalidReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpRouteInvalidReason.setStatus("current")


class _TBgpRouteNLRI_Type(OctetString):
    """Custom type tBgpRouteNLRI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgpRouteNLRI_Type.__name__ = "OctetString"
_TBgpRouteNLRI_Object = MibScalar
tBgpRouteNLRI = _TBgpRouteNLRI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 15),
    _TBgpRouteNLRI_Type()
)
tBgpRouteNLRI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgpRouteNLRI.setStatus("current")
_TBgp4PathAttrType_Type = Integer32
_TBgp4PathAttrType_Object = MibScalar
tBgp4PathAttrType = _TBgp4PathAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 16),
    _TBgp4PathAttrType_Type()
)
tBgp4PathAttrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4PathAttrType.setStatus("current")
_TBgp4PathAttrLength_Type = Unsigned32
_TBgp4PathAttrLength_Object = MibScalar
tBgp4PathAttrLength = _TBgp4PathAttrLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 17),
    _TBgp4PathAttrLength_Type()
)
tBgp4PathAttrLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4PathAttrLength.setStatus("current")


class _TBgp4PathAttribute_Type(OctetString):
    """Custom type tBgp4PathAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_TBgp4PathAttribute_Type.__name__ = "OctetString"
_TBgp4PathAttribute_Object = MibScalar
tBgp4PathAttribute = _TBgp4PathAttribute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 18),
    _TBgp4PathAttribute_Type()
)
tBgp4PathAttribute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4PathAttribute.setStatus("current")


class _TBgp4WithdrawnRoutePrefix_Type(OctetString):
    """Custom type tBgp4WithdrawnRoutePrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgp4WithdrawnRoutePrefix_Type.__name__ = "OctetString"
_TBgp4WithdrawnRoutePrefix_Object = MibScalar
tBgp4WithdrawnRoutePrefix = _TBgp4WithdrawnRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 19),
    _TBgp4WithdrawnRoutePrefix_Type()
)
tBgp4WithdrawnRoutePrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4WithdrawnRoutePrefix.setStatus("current")


class _TBgp4UpdateMessage_Type(OctetString):
    """Custom type tBgp4UpdateMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgp4UpdateMessage_Type.__name__ = "OctetString"
_TBgp4UpdateMessage_Object = MibScalar
tBgp4UpdateMessage = _TBgp4UpdateMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 20),
    _TBgp4UpdateMessage_Type()
)
tBgp4UpdateMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4UpdateMessage.setStatus("current")


class _TBgp4BadErrorMessage_Type(OctetString):
    """Custom type tBgp4BadErrorMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TBgp4BadErrorMessage_Type.__name__ = "OctetString"
_TBgp4BadErrorMessage_Object = MibScalar
tBgp4BadErrorMessage = _TBgp4BadErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 21),
    _TBgp4BadErrorMessage_Type()
)
tBgp4BadErrorMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4BadErrorMessage.setStatus("current")


class _TBgp4BadErrorMessageType_Type(Integer32):
    """Custom type tBgp4BadErrorMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("badNetworkError", 1)
    )


_TBgp4BadErrorMessageType_Type.__name__ = "Integer32"
_TBgp4BadErrorMessageType_Object = MibScalar
tBgp4BadErrorMessageType = _TBgp4BadErrorMessageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 14, 7, 22),
    _TBgp4BadErrorMessageType_Type()
)
tBgp4BadErrorMessageType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tBgp4BadErrorMessageType.setStatus("current")
_TBgpNotificationsPrefix_ObjectIdentity = ObjectIdentity
tBgpNotificationsPrefix = _TBgpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14)
)
_TBgpNotifications_ObjectIdentity = ObjectIdentity
tBgpNotifications = _TBgpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0)
)
tBgpInstanceEntry.registerAugmentions(
    ("TIMETRA-BGP-MIB",
     "tBgpInstancePlcyEntry")
)
tBgpInstancePlcyEntry.setIndexNames(*tBgpInstanceEntry.getIndexNames())
tBgpPeerGroupEntry.registerAugmentions(
    ("TIMETRA-BGP-MIB",
     "tBgpPeerGroupPlcyEntry")
)
tBgpPeerGroupPlcyEntry.setIndexNames(*tBgpPeerGroupEntry.getIndexNames())
tBgpPeerEntry.registerAugmentions(
    ("TIMETRA-BGP-MIB",
     "tBgpPeerOperEntry")
)
tBgpPeerOperEntry.setIndexNames(*tBgpPeerEntry.getIndexNames())
tBgpPeerNgEntry.registerAugmentions(
    ("TIMETRA-BGP-MIB",
     "tBgpPeerNgOperEntry")
)
tBgpPeerNgOperEntry.setIndexNames(*tBgpPeerNgEntry.getIndexNames())
tBgpPeerNgEntry.registerAugmentions(
    ("TIMETRA-BGP-MIB",
     "tBgpPeerPlcyEntry")
)
tBgpPeerPlcyEntry.setIndexNames(*tBgpPeerNgEntry.getIndexNames())
tBgpPeeringPolicyEntry.registerAugmentions(
    ("TIMETRA-BGP-MIB",
     "tBgpPeeringPlcyEntry")
)
tBgpPeeringPlcyEntry.setIndexNames(*tBgpPeeringPolicyEntry.getIndexNames())

# Managed Objects groups

tmnxBgpConfederationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 5)
)
tmnxBgpConfederationGroup.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpConfederationTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpConfederationRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxBgpConfederationGroup.setStatus("obsolete")

tmnxBgp4PathAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 6)
)
tmnxBgp4PathAttrGroup.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgp4PathAttrOriginID"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttrClusterList"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttrCommunity"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttrExtCommunity"))
)
if mibBuilder.loadTexts:
    tmnxBgp4PathAttrGroup.setStatus("current")

tmnxBgpPeerV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 19)
)
tmnxBgpPeerV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnLocalCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsRcvd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsSent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperInputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperOutputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperPathsSupByDamping"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastEvent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnRecvPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSupport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyNegotiated"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRRecvEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSendEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStaleRoutesTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRReqRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperNumRestarts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SuppPathsDamping"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnReceivedPaths"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerV4v0Group.setStatus("obsolete")

tmnxBgpInstanceV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 20)
)
tmnxBgpInstanceV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDescription"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAlwaysCompareMED"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAsPathIgnore"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceBgpId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDampening"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultipath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePreference"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConfederationAS"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIBgpMultipath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceFamily"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRPathSelectDefer"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIgpShortcut"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisallowIgp"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstRteTargetRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAllowInterAsVpn"))
)
if mibBuilder.loadTexts:
    tmnxBgpInstanceV4v0Group.setStatus("obsolete")

tmnxBgpObsoleteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 21)
)
tmnxBgpObsoleteV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPeerRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnRemoteFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnLocalCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerConnState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperMsgOctetsRcvd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperMsgOctetsSent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperInputQueueMessages"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperOutputQueueMessages"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperPathsSuppressedByDamping"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperFlaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperLastState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperLastEvent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperVpnReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperVpnSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperVpnActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRSupport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRFamilyRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRFamilyFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRFamilyNegotiated"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRRecvEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRSendEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRStaleRoutesTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRRequestRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperNumRestarts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperLastRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6ReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6SentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6ActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6ReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6SuppPathsDamping"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperVpnReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerParamsInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDefaultOriginate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMinTTLValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerTTLLogId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalAddress"))
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteV4v0Group.setStatus("obsolete")

tmnxBgpPeerParamsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 22)
)
tmnxBgpPeerParamsV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgParamsInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDefaultOriginate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinTTLValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgTracking"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerParamsV4v0Group.setStatus("obsolete")

tmnxBgpPeerGroupParamsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 23)
)
tmnxBgpPeerGroupParamsV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPGParamsInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPGDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpPGDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpPGDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpPGDefaultOriginate"),
        ("TIMETRA-BGP-MIB", "tBgpPGAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpPGMinTTLValue"),
        ("TIMETRA-BGP-MIB", "tBgpPGTTLLogId"),
        ("TIMETRA-BGP-MIB", "tBgpPGLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPGLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPGPeerTracking"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerGroupParamsV4v0Group.setStatus("obsolete")

tmnxBgpPeerGroupV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 24)
)
tmnxBgpPeerGroupV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerGroupTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupName"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPGSendOrfRTRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerGroupV4v0Group.setStatus("obsolete")

tmnxBgpInstanceParamsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 27)
)
tmnxBgpInstanceParamsV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDefaultOriginate"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePeerTracking"))
)
if mibBuilder.loadTexts:
    tmnxBgpInstanceParamsV4v0Group.setStatus("obsolete")

tmnxBgpPeerV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 28)
)
tmnxBgpPeerV5v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnLocalCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsRcvd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsSent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperInputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperOutputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastEvent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnRecvPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSupport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyNegotiated"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRRecvEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSendEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStaleRoutesTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRReqRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperNumRestarts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4ActivePfxs"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerV5v0Group.setStatus("obsolete")

tmnxBgpObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 29)
)
tmnxBgpObsoleteV5v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPeerRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnRemoteFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnLocalCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerVpnRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerConnState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperMsgOctetsRcvd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperMsgOctetsSent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperInputQueueMessages"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperOutputQueueMessages"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperPathsSuppressedByDamping"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperFlaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperLastState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperLastEvent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperVpnReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperVpnSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperVpnActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRSupport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRFamilyRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRFamilyFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRFamilyNegotiated"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRRecvEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRSendEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRStaleRoutesTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRRequestRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperGRStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperNumRestarts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperLastRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6ReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6SentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6ActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6ReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperV6SuppPathsDamping"),
        ("TIMETRA-BGP-MIB", "tBgpPeerOperVpnReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerParamsInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpPeerDefaultOriginate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerMinTTLValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerTTLLogId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperPathsSupByDamping"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SuppPathsDamping"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnReceivedPaths"))
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteV5v0Group.setStatus("current")

tmnxBgpPeerParamsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 30)
)
tmnxBgpPeerParamsV5v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgParamsInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDefaultOriginate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinTTLValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgTracking"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAdvLabelAddrFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAuthKeyChain"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLastError"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerParamsV5v0Group.setStatus("current")

tmnxBgpInstanceParamsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 31)
)
tmnxBgpInstanceParamsV5v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDefaultOriginate"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePeerTracking"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAuthKeyChain"))
)
if mibBuilder.loadTexts:
    tmnxBgpInstanceParamsV5v0Group.setStatus("current")

tmnxBgpPeerGroupParamsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 32)
)
tmnxBgpPeerGroupParamsV5v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPGParamsInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPGDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpPGDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpPGDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpPGDefaultOriginate"),
        ("TIMETRA-BGP-MIB", "tBgpPGAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpPGMinTTLValue"),
        ("TIMETRA-BGP-MIB", "tBgpPGTTLLogId"),
        ("TIMETRA-BGP-MIB", "tBgpPGLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPGLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPGPeerTracking"),
        ("TIMETRA-BGP-MIB", "tBgpPGAuthKeyChain"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerGroupParamsV5v0Group.setStatus("current")

tmnxBgpInstanceParamsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 34)
)
tmnxBgpInstanceParamsV6v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceRapidWithdrawal"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceBfdEnabled"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePurgeTimer"))
)
if mibBuilder.loadTexts:
    tmnxBgpInstanceParamsV6v0Group.setStatus("current")

tmnxBgpPeerGroupParamsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 35)
)
tmnxBgpPeerGroupParamsV6v0Group.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPGBfdEnabled")
)
if mibBuilder.loadTexts:
    tmnxBgpPeerGroupParamsV6v0Group.setStatus("current")

tmnxBgpPeerParamsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 36)
)
tmnxBgpPeerParamsV6v0Group.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPeerNgBfdEnabled")
)
if mibBuilder.loadTexts:
    tmnxBgpPeerParamsV6v0Group.setStatus("current")

tmnxBgpPeerV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 37)
)
tmnxBgpPeerV6v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnLocalCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsRcvd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsSent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperInputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperOutputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastEvent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnRecvPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSupport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyNegotiated"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRRecvEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSendEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStaleRoutesTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRReqRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperNumRestarts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6SuppPfxDamp"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerV6v0Group.setStatus("obsolete")

tmnxBgpPeeringPolicyV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 38)
)
tmnxBgpPeeringPolicyV7v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeeringPolicyTableLastChngd"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLastChngd"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyAuthKeyChain"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMinRteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMinTTLValue"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDynamicPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyRemovePrivateASLmtd"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeeringPolicyV7v0Group.setStatus("obsolete")

tmnxBgp4ByteASNV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 39)
)
tmnxBgp4ByteASNV7v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tbgp4PathAttrASPathSegment"),
        ("TIMETRA-BGP-MIB", "tbgp4PathAttrAggregatorAS"),
        ("TIMETRA-BGP-MIB", "tBgpConfederation4BytTblLstChngd"),
        ("TIMETRA-BGP-MIB", "tBgpConfederation4ByteRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxBgp4ByteASNV7v0Group.setStatus("current")

tmnxBgpInstanceV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 40)
)
tmnxBgpInstanceV7v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDescription"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAlwaysCompareMED"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceBgpId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDampening"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultipath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePreference"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIBgpMultipath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceFamily"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRPathSelectDefer"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIgpShortcut"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisallowIgp"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstRteTargetRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAllowInterAsVpn"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConfederationAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultipathEiBgpState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceHoldTimeIsStrict"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRemovePrivateASLmtd"))
)
if mibBuilder.loadTexts:
    tmnxBgpInstanceV7v0Group.setStatus("obsolete")

tmnxBgpPeerGroupV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 41)
)
tmnxBgpPeerGroupV7v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerGroupTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupName"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPGSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupHoldTimeIsStrict"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRemovePrivateASLmtd"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerGroupV7v0Group.setStatus("obsolete")

tmnxBgpPeerV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 42)
)
tmnxBgpPeerV7v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnLocalCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsRcvd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsSent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperInputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperOutputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastEvent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnRecvPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSupport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyNegotiated"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRRecvEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSendEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStaleRoutesTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRReqRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperNumRestarts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTimeIsStrict"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgL2vpnCiscoInterop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateASLmtd"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerV7v0Group.setStatus("obsolete")

tmnxBgpObsoleteV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 43)
)
tmnxBgpObsoleteV7v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConfederationAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpConfederationTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpConfederationRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteV7v0Group.setStatus("current")

tmnxBgpNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 44)
)
tmnxBgpNotifyObjsV7v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgpRouteInvalidReason"),
        ("TIMETRA-BGP-MIB", "tBgpRouteNLRI"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotifyObjsV7v0Group.setStatus("current")

tmnxBgpInstanceV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 46)
)
tmnxBgpInstanceV8v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceRapidUpdate"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAsPathIgnoreFamily"))
)
if mibBuilder.loadTexts:
    tmnxBgpInstanceV8v0Group.setStatus("current")

tmnxBgpObsoleteV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 47)
)
tmnxBgpObsoleteV8v0Group.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpInstanceAsPathIgnore")
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteV8v0Group.setStatus("current")

tmnxBgpPeerV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 48)
)
tmnxBgpPeerV8v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperl2VpnSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperl2VpnRecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperl2VpnSentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperl2VpnActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMdtSafiSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMdtSafiRecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMdtSafiSentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMdtSafiActivePfxs"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerV8v0Group.setStatus("current")

tmnxBgpGlobalV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 49)
)
tmnxBgpGlobalV8v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstancePMTUDiscovery"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPMTUDiscovery"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPMTUDiscovery"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAdvertiseLdpPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMaxPrefixLogOnly"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMaxPrefixThreshold"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefixLogOnly"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefixThreshold"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMaxPrefixLogOnly"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMaxPrefixThreshold"))
)
if mibBuilder.loadTexts:
    tmnxBgpGlobalV8v0Group.setStatus("current")

tmnxBgpAddPathV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 50)
)
tmnxBgpAddPathV9v0R4Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceEnableAddPath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRecvAddPath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIpv4AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnIpv4AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIpv6AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnIpv6AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPGEnableAddPath"),
        ("TIMETRA-BGP-MIB", "tBgpPGRecvAddPath"),
        ("TIMETRA-BGP-MIB", "tBgpPGIpv4AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPGVpnIpv4AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPGIpv6AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPGVpnIpv6AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgEnableAddPath"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRecvAddPath"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgIpv4AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnIpv4AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgIpv6AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnIpv6AddPathLimit"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddPathSendRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddPathRecvRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperBackupPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6BackupPrefixes"))
)
if mibBuilder.loadTexts:
    tmnxBgpAddPathV9v0R4Group.setStatus("current")

tmnxBgpPeerV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 51)
)
tmnxBgpPeerV9v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsPwSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsPwRecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsPwSentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsPwActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlowIpv4SupPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlowIpv4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlowIpv4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlowIpv4ActivePfxs"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerV9v0Group.setStatus("current")

tmnxBgpGlobalV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 52)
)
tmnxBgpGlobalV9v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceTransportTunnel"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAdvertiseExternal"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceBackupPath"),
        ("TIMETRA-BGP-MIB", "tBgpPGUpdatedErrorHandling"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgUpdatedErrorHandling"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableRtTblInstall"))
)
if mibBuilder.loadTexts:
    tmnxBgpGlobalV9v0Group.setStatus("obsolete")

tmnxBgpFlowSpecV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 53)
)
tmnxBgpFlowSpecV9v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPGFlowspecValidate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgFlowspecValidate"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceFlowspecValidate"))
)
if mibBuilder.loadTexts:
    tmnxBgpFlowSpecV9v0Group.setStatus("current")

tmnxBgpDisableCapNegoV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 54)
)
tmnxBgpDisableCapNegoV9v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerGroupDisableCapNego"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableCapNegotiation"))
)
if mibBuilder.loadTexts:
    tmnxBgpDisableCapNegoV9v0Group.setStatus("current")

tmnxBgpNotifyObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 55)
)
tmnxBgpNotifyObjsV9v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpFlowspecExtCommunityAction"),
        ("TIMETRA-BGP-MIB", "tBgpFlowspecExtCommActionValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerFlowRouteDestAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerFlowRouteDestAddr"),
        ("TIMETRA-BGP-MIB", "tBgpFlowRouteInvalidReason"),
        ("TIMETRA-BGP-MIB", "tBgpFlowRouteNLRI"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttrType"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttrLength"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttribute"),
        ("TIMETRA-BGP-MIB", "tBgp4OTWithdrawnRouteLength"),
        ("TIMETRA-BGP-MIB", "tBgp4OTWithdrawnRoutePrefix"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotifyObjsV9v0Group.setStatus("obsolete")

tmnxBgpGlobalV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 57)
)
tmnxBgpGlobalV10v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceIgnoreNextHopMetric"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMpBgpKeep"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIgnoreRouterId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAlwaysCompMEDStrict"),
        ("TIMETRA-BGP-MIB", "tBgpPGAigp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAigp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnV4BackupPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnV6BackupPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMinHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPGMinHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgSplitHorizon"),
        ("TIMETRA-BGP-MIB", "tBgpInstRemovePrivateSkipPeerAs"),
        ("TIMETRA-BGP-MIB", "tBgpPGRemovePrivateSkipPeerAs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemPrivateSkipPeerAs"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceNHResUseBgpRoutes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMcastVpnV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMcastVpnV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMcastVpnV4ActPfxs"))
)
if mibBuilder.loadTexts:
    tmnxBgpGlobalV10v0Group.setStatus("current")

tmnxBgpRTConstraintV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 58)
)
tmnxBgpRTConstraintV10v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPGDefaultRouteTarget"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDefaultRouteTarget"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperRtTgtSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperRtTgtRecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperRtTgtSentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperRtTgtActivePfxs"))
)
if mibBuilder.loadTexts:
    tmnxBgpRTConstraintV10v0Group.setStatus("current")

tmnxBgpInstanceV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 59)
)
tmnxBgpInstanceV10v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDescription"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAlwaysCompareMED"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceBgpId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDampening"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultipath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePreference"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIBgpMultipath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceFamily"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRPathSelectDefer"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIgpShortcut"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisallowIgp"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstRteTargetRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAllowInterAsVpn"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConfederationAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultipathEiBgpState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRemovePrivateASLmtd"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy15"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy15"))
)
if mibBuilder.loadTexts:
    tmnxBgpInstanceV10v0Group.setStatus("obsolete")

tmnxBgpPeerGroupV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 60)
)
tmnxBgpPeerGroupV10v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerGroupTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupName"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPGSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRemovePrivateASLmtd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy15"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy15"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerGroupV10v0Group.setStatus("obsolete")

tmnxBgpPeerV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 61)
)
tmnxBgpPeerV10v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnLocalCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsRcvd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsSent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperInputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperOutputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastEvent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnRecvPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSupport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyNegotiated"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRRecvEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSendEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStaleRoutesTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRReqRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperNumRestarts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgL2vpnCiscoInterop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateASLmtd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy15"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy15"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerV10v0Group.setStatus("obsolete")

tmnxBgpPeeringPlcyV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 62)
)
tmnxBgpPeeringPlcyV10v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyImportPolicy15"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeeringPlcyExportPolicy15"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeeringPlcyV10v0Group.setStatus("current")

tmnxBgpPeeringPolicyV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 63)
)
tmnxBgpPeeringPolicyV10v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeeringPolicyTableLastChngd"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLastChngd"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyAdvertiseInactiveRts"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyAuthKeyChain"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisableComms"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisableExtComms"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisableFEFailover"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMinRteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyPeerAS"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyMinTTLValue"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDynamicPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyRemovePrivateASLmtd"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeeringPolicyV10v0Group.setStatus("current")

tmnxBgpObsoleteV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 64)
)
tmnxBgpObsoleteV10v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceHoldTimeIsStrict"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupHoldTimeIsStrict"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTimeIsStrict"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPrngPlcyExportPolicy5"))
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteV10v0Group.setStatus("current")

tmnxBgpGlobalV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 65)
)
tmnxBgpGlobalV11v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstLocalASNoPrependGlobalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPGLocalASNoPrependGlobalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLclASNoPrependGlobalAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV6RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV6SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV6ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceEnableRRVpnFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPGMaxPrefixIdleTimeOut"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefixIdleTimeOut"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlowIpv6SupPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlowIpv6RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlowIpv6SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlowIpv6ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceNHResPolicy"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePeerTrackingPolicy"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceTransportTunnel"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAdvertiseExternal"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceBackupPath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableRtTblInstall"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDeterministicMED"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceSplitHorizon"),
        ("TIMETRA-BGP-MIB", "tBgpPGSplitHorizon"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIgnoreRtrIdInternal"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIgnoreRtrIdExternal"))
)
if mibBuilder.loadTexts:
    tmnxBgpGlobalV11v0Group.setStatus("current")

tmnxBgpPeerGroupV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 66)
)
tmnxBgpPeerGroupV11v0Group.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPeerGroupCreationOrigin")
)
if mibBuilder.loadTexts:
    tmnxBgpPeerGroupV11v0Group.setStatus("current")

tmnxBgpObsoleteV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 67)
)
tmnxBgpObsoleteV11v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPGUpdatedErrorHandling"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgUpdatedErrorHandling"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttrType"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttrLength"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttribute"),
        ("TIMETRA-BGP-MIB", "tBgp4OTWithdrawnRouteLength"),
        ("TIMETRA-BGP-MIB", "tBgp4OTWithdrawnRoutePrefix"))
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteV11v0Group.setStatus("current")

tmnxBgpGlobalDCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 68)
)
tmnxBgpGlobalDCGroup.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgOperEvpnSupPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperEvpnRecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperEvpnSentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperEvpnActivePfxs"))
)
if mibBuilder.loadTexts:
    tmnxBgpGlobalDCGroup.setStatus("current")

tmnxBgpDPOscilationV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 69)
)
tmnxBgpDPOscilationV11v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstGrRestartNotification"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceFaultTolerance"),
        ("TIMETRA-BGP-MIB", "tBgpPGGRRestartNotification"),
        ("TIMETRA-BGP-MIB", "tBgpPGFaultTolerance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRRestartNotification"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgFaultTolerance"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDampPeerOscillations"),
        ("TIMETRA-BGP-MIB", "tBgpInstDmpPeerOscInitialWaitTim"),
        ("TIMETRA-BGP-MIB", "tBgpInstDmpPeerOscSecondWaitTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstDmpPeerOscMaxWaitTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstDmpPeerOscErrorInterval"),
        ("TIMETRA-BGP-MIB", "tBgpPGDampPeerOscillations"),
        ("TIMETRA-BGP-MIB", "tBgpPGDampPeerOscInitialWaitTime"),
        ("TIMETRA-BGP-MIB", "tBgpPGDampPeerOscSecondWaitTime"),
        ("TIMETRA-BGP-MIB", "tBgpPGDampPeerOscMaxWaitTime"),
        ("TIMETRA-BGP-MIB", "tBgpPGDampPeerOscErrorInterval"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampPeerOscillations"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampOscInitialWaitTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampOscSecondWaitTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampOscMaxWaitTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampOscErrorInterval"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperUpdateErrors"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRNotifFamilyNego"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperRemIdleHoldTime"))
)
if mibBuilder.loadTexts:
    tmnxBgpDPOscilationV11v0Group.setStatus("current")

tmnxBgpNotifyObjsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 70)
)
tmnxBgpNotifyObjsV11v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgp4PathAttrType"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttrLength"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttribute"),
        ("TIMETRA-BGP-MIB", "tBgp4WithdrawnRoutePrefix"),
        ("TIMETRA-BGP-MIB", "tBgp4UpdateMessage"),
        ("TIMETRA-BGP-MIB", "tBgpFlowspecExtCommunityAction"),
        ("TIMETRA-BGP-MIB", "tBgpFlowspecExtCommActionValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerFlowRouteDestAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerFlowRouteDestAddr"),
        ("TIMETRA-BGP-MIB", "tBgpFlowRouteInvalidReason"),
        ("TIMETRA-BGP-MIB", "tBgpFlowRouteNLRI"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotifyObjsV11v0Group.setStatus("current")

tmnxBgpMvpnVrfImportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 73)
)
tmnxBgpMvpnVrfImportGroup.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpInstMvpnVrfImportSubTypeNew")
)
if mibBuilder.loadTexts:
    tmnxBgpMvpnVrfImportGroup.setStatus("current")

tmnxBgpNHUnchangedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 74)
)
tmnxBgpNHUnchangedGroup.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPGNHUnchangedFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNhUnchangedFamily"))
)
if mibBuilder.loadTexts:
    tmnxBgpNHUnchangedGroup.setStatus("current")

tmnxBgpResolveLabelRoutesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 75)
)
tmnxBgpResolveLabelRoutesGroup.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpInstResolveLabelRoutesInRtm")
)
if mibBuilder.loadTexts:
    tmnxBgpResolveLabelRoutesGroup.setStatus("current")

tmnxBgpInstanceV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 76)
)
tmnxBgpInstanceV12v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDescription"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAlwaysCompareMED"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceBgpId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDampening"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultipath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePreference"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIBgpMultipath"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceFamily"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRPathSelectDefer"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceIgpShortcut"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisallowIgp"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpInstRteTargetRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceAllowInterAsVpn"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceConfederationAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceMultipathEiBgpState"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceRemovePrivateASLmtd"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyImportPolicy15"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpInstancePlcyExportPolicy15"))
)
if mibBuilder.loadTexts:
    tmnxBgpInstanceV12v0Group.setStatus("current")

tmnxBgpPeerGroupV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 77)
)
tmnxBgpPeerGroupV12v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerGroupTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupName"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPGSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPeerAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupRemovePrivateASLmtd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyImportPolicy15"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupPlcyExportPolicy15"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerGroupV12v0Group.setStatus("current")

tmnxBgpPeerV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 78)
)
tmnxBgpPeerV12v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerTableLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerTableSpinlock"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerGroup"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgShutdown"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDescription"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnectRetry"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgKeepAlive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDampening"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddress"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAddressType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLoopDetect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinRouteAdvertisement"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDSource"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMEDValue"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMultihop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNextHopSelf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgNoAggregatorID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPassive"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPreference"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateAS"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLastChanged"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgInheritance"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalASPrivate"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5Auth"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMd5AuthKey"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgClusterId"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisableClientReflect"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGracefulRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStaleRoute"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRAdminState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGROperState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteFamily"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyImport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnApplyExport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnLocalCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgVpnRemoteCaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgASOverride"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsSendOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgExtCommsRecvOrf"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsRcvd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMsgOctetsSent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperInputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperOutputQueueMsgs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperReceivedPaths"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperFlaps"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastState"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastEvent"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnRecvPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgSendOrfRTRowStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSupport"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyRestart"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyFwding"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRFamilyNegotiated"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRRecvEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRSendEOR"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStaleRoutesTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRReqRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStatus"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperNumRestarts"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperLastRestartTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ReceivedPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SentPrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6ActivePrefixes"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnSuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperV6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMCastV4ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperVpnIpv6SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgLocalAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgPeerAS4Byte"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgDisable4ByteASN"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4SuppPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMvpnV4ActivePfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgL2vpnCiscoInterop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgRemovePrivateASLmtd"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyImportPolicy15"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpPeerPlcyExportPolicy15"))
)
if mibBuilder.loadTexts:
    tmnxBgpPeerV12v0Group.setStatus("current")

tmnxBgpObsoleteV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 79)
)
tmnxBgpObsoleteV12v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGroupMinASOrigination"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinASOrigination"))
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteV12v0Group.setStatus("current")

tmnxBgpMcastIpv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 80)
)
tmnxBgpMcastIpv6Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgOperMcastV6SupPfxDamp"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMcastV6RecvPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMcastV6SentPfxs"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgOperMcastV6ActivePfxs"))
)
if mibBuilder.loadTexts:
    tmnxBgpMcastIpv6Group.setStatus("current")

tmnxBgpPrefixOriginValidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 81)
)
tmnxBgpPrefixOriginValidGroup.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceCompOriginValidState"),
        ("TIMETRA-BGP-MIB", "tBgpPGEnableOriginValidation"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgEnableOriginValidation"),
        ("TIMETRA-BGP-MIB", "tBgpInstanceOrigInvalidUnusable"))
)
if mibBuilder.loadTexts:
    tmnxBgpPrefixOriginValidGroup.setStatus("current")

tmnxBgpThirdPartyNHGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 82)
)
tmnxBgpThirdPartyNHGroup.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpInstanceThirdPartyNextHop"),
        ("TIMETRA-BGP-MIB", "tBgpPGThirdPartyNextHop"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgThirdPartyNextHop"))
)
if mibBuilder.loadTexts:
    tmnxBgpThirdPartyNHGroup.setStatus("current")

tmnxBgpNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 84)
)
tmnxBgpNotifyObjsV12v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgp4BadErrorMessage"),
        ("TIMETRA-BGP-MIB", "tBgp4BadErrorMessageType"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotifyObjsV12v0Group.setStatus("current")

tmnxBgpRibLeakImportV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 88)
)
tmnxBgpRibLeakImportV12v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicyTblLstCh"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicyLstCh"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy1"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy2"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy3"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy4"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy5"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy6"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy7"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy8"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy9"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy10"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy11"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy12"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy13"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy14"),
        ("TIMETRA-BGP-MIB", "tBgpRibLeakImportPolicy15"))
)
if mibBuilder.loadTexts:
    tmnxBgpRibLeakImportV12v0Group.setStatus("current")


# Notification objects

tBgpMaxPrefix90 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 1)
)
tBgpMaxPrefix90.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPeerMaxPrefix")
)
if mibBuilder.loadTexts:
    tBgpMaxPrefix90.setStatus(
        "obsolete"
    )

tBgpMaxPrefix100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 2)
)
tBgpMaxPrefix100.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPeerMaxPrefix")
)
if mibBuilder.loadTexts:
    tBgpMaxPrefix100.setStatus(
        "obsolete"
    )

tBgpPeerGRStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 3)
)
tBgpPeerGRStatusChange.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPeerOperGRStatus")
)
if mibBuilder.loadTexts:
    tBgpPeerGRStatusChange.setStatus(
        "obsolete"
    )

tBgpMaxNgPrefix90 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 4)
)
tBgpMaxNgPrefix90.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefixThreshold"))
)
if mibBuilder.loadTexts:
    tBgpMaxNgPrefix90.setStatus(
        "obsolete"
    )

tBgpMaxNgPrefix100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 5)
)
tBgpMaxNgPrefix100.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix")
)
if mibBuilder.loadTexts:
    tBgpMaxNgPrefix100.setStatus(
        "current"
    )

tBgpPeerNgGRStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 6)
)
tBgpPeerNgGRStatusChange.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPeerNgOperGRStatus")
)
if mibBuilder.loadTexts:
    tBgpPeerNgGRStatusChange.setStatus(
        "current"
    )

tBgpNgEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 7)
)
tBgpNgEstablished.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgLastError"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnState"))
)
if mibBuilder.loadTexts:
    tBgpNgEstablished.setStatus(
        "current"
    )

tBgpNgBackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 8)
)
tBgpNgBackwardTransition.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgLastError"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgConnState"))
)
if mibBuilder.loadTexts:
    tBgpNgBackwardTransition.setStatus(
        "current"
    )

tBgpPeerNgHoldTimeInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 9)
)
tBgpPeerNgHoldTimeInconsistent.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTime"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMinHoldTime"))
)
if mibBuilder.loadTexts:
    tBgpPeerNgHoldTimeInconsistent.setStatus(
        "current"
    )

tBgpFlowspecUnsupportdComAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 10)
)
tBgpFlowspecUnsupportdComAction.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpFlowspecExtCommunityAction"),
        ("TIMETRA-BGP-MIB", "tBgpFlowspecExtCommActionValue"))
)
if mibBuilder.loadTexts:
    tBgpFlowspecUnsupportdComAction.setStatus(
        "current"
    )

tBgpFlowRouteInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 11)
)
tBgpFlowRouteInvalid.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgpPeerFlowRouteDestAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerFlowRouteDestAddr"),
        ("TIMETRA-BGP-MIB", "tBgpFlowRouteInvalidReason"),
        ("TIMETRA-BGP-MIB", "tBgpFlowRouteNLRI"))
)
if mibBuilder.loadTexts:
    tBgpFlowRouteInvalid.setStatus(
        "current"
    )

tBgpMaxNgPrefixThreshReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 12)
)
tBgpMaxNgPrefixThreshReached.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefixThreshold"))
)
if mibBuilder.loadTexts:
    tBgpMaxNgPrefixThreshReached.setStatus(
        "current"
    )

tBgp4OptTransPathAttrInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 13)
)
tBgp4OptTransPathAttrInvalid.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttrType"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttrLength"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttribute"))
)
if mibBuilder.loadTexts:
    tBgp4OptTransPathAttrInvalid.setStatus(
        "obsolete"
    )

tBgp4OptTransWithdrawnRoutes = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 14)
)
tBgp4OptTransWithdrawnRoutes.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgp4OTWithdrawnRouteLength"),
        ("TIMETRA-BGP-MIB", "tBgp4OTWithdrawnRoutePrefix"))
)
if mibBuilder.loadTexts:
    tBgp4OptTransWithdrawnRoutes.setStatus(
        "obsolete"
    )

tBgp4RouteInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 15)
)
tBgp4RouteInvalid.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgpRouteInvalidReason"),
        ("TIMETRA-BGP-MIB", "tBgpRouteNLRI"))
)
if mibBuilder.loadTexts:
    tBgp4RouteInvalid.setStatus(
        "current"
    )

tBgp4PathAttrInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 16)
)
tBgp4PathAttrInvalid.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttrType"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttrLength"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttribute"))
)
if mibBuilder.loadTexts:
    tBgp4PathAttrInvalid.setStatus(
        "current"
    )

tBgp4WithdrawnRtFromUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 17)
)
tBgp4WithdrawnRtFromUpdateError.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgp4WithdrawnRoutePrefix"))
)
if mibBuilder.loadTexts:
    tBgp4WithdrawnRtFromUpdateError.setStatus(
        "current"
    )

tBgp4UpdateInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 18)
)
tBgp4UpdateInvalid.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddrType"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgAddr"),
        ("TIMETRA-BGP-MIB", "tBgp4UpdateMessage"))
)
if mibBuilder.loadTexts:
    tBgp4UpdateInvalid.setStatus(
        "current"
    )

tBgpReceivedInvalidNlri = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 14, 0, 19)
)
tBgpReceivedInvalidNlri.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-BGP-MIB", "tBgp4BadErrorMessage"),
        ("TIMETRA-BGP-MIB", "tBgp4BadErrorMessageType"))
)
if mibBuilder.loadTexts:
    tBgpReceivedInvalidNlri.setStatus(
        "current"
    )


# Notifications groups

tmnxBgpNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 25)
)
tmnxBgpNotificationV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpMaxNgPrefix90"),
        ("TIMETRA-BGP-MIB", "tBgpMaxNgPrefix100"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStatusChange"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxBgpObsoleteNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 26)
)
tmnxBgpObsoleteNotificationV4v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpMaxPrefix90"),
        ("TIMETRA-BGP-MIB", "tBgpMaxPrefix100"),
        ("TIMETRA-BGP-MIB", "tBgpPeerGRStatusChange"))
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteNotificationV4v0Group.setStatus(
        "current"
    )

tmnxBgpNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 33)
)
tmnxBgpNotificationV5v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpMaxNgPrefix90"),
        ("TIMETRA-BGP-MIB", "tBgpMaxNgPrefix100"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStatusChange"),
        ("TIMETRA-BGP-MIB", "tBgpNgEstablished"),
        ("TIMETRA-BGP-MIB", "tBgpNgBackwardTransition"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxBgpNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 45)
)
tmnxBgpNotificationV7v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpPeerNgHoldTimeInconsistent"),
        ("TIMETRA-BGP-MIB", "tBgp4RouteInvalid"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotificationV7v0Group.setStatus(
        "current"
    )

tmnxBgpNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 56)
)
tmnxBgpNotificationV9v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgpMaxNgPrefix100"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStatusChange"),
        ("TIMETRA-BGP-MIB", "tBgpNgEstablished"),
        ("TIMETRA-BGP-MIB", "tBgpNgBackwardTransition"),
        ("TIMETRA-BGP-MIB", "tBgpFlowspecUnsupportdComAction"),
        ("TIMETRA-BGP-MIB", "tBgpFlowRouteInvalid"),
        ("TIMETRA-BGP-MIB", "tBgpMaxNgPrefixThreshReached"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttrInvalid"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransWithdrawnRoutes"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotificationV9v0Group.setStatus(
        "obsolete"
    )

tmnxBgpNotificationV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 71)
)
tmnxBgpNotificationV11v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgp4UpdateInvalid"),
        ("TIMETRA-BGP-MIB", "tBgp4PathAttrInvalid"),
        ("TIMETRA-BGP-MIB", "tBgp4WithdrawnRtFromUpdateError"),
        ("TIMETRA-BGP-MIB", "tBgpMaxNgPrefix100"),
        ("TIMETRA-BGP-MIB", "tBgpPeerNgGRStatusChange"),
        ("TIMETRA-BGP-MIB", "tBgpNgEstablished"),
        ("TIMETRA-BGP-MIB", "tBgpNgBackwardTransition"),
        ("TIMETRA-BGP-MIB", "tBgpFlowspecUnsupportdComAction"),
        ("TIMETRA-BGP-MIB", "tBgpFlowRouteInvalid"),
        ("TIMETRA-BGP-MIB", "tBgpMaxNgPrefixThreshReached"))
)
if mibBuilder.loadTexts:
    tmnxBgpNotificationV11v0Group.setStatus(
        "current"
    )

tmnxBgpObsoleteNtfnV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 72)
)
tmnxBgpObsoleteNtfnV11v0Group.setObjects(
      *(("TIMETRA-BGP-MIB", "tBgp4OptTransPathAttrInvalid"),
        ("TIMETRA-BGP-MIB", "tBgp4OptTransWithdrawnRoutes"))
)
if mibBuilder.loadTexts:
    tmnxBgpObsoleteNtfnV11v0Group.setStatus(
        "current"
    )

tmnxBgpNotificationV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 2, 83)
)
tmnxBgpNotificationV12v0Group.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpReceivedInvalidNlri")
)
if mibBuilder.loadTexts:
    tmnxBgpNotificationV12v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxBgpV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 4)
)
tmnxBgpV4v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpInstanceV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpConfederationGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4PathAttrGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpObsoleteV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpObsoleteNotificationV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxBgpV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxBgpV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 5)
)
tmnxBgpV5v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpInstanceV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpConfederationGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4PathAttrGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpObsoleteV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpObsoleteNotificationV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxBgpV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxBgpV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 6)
)
tmnxBgpV6v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpInstanceV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV4v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpConfederationGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4PathAttrGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxBgpV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxBgpV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 7)
)
tmnxBgpV7v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4PathAttrGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeeringPolicyV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4ByteASNV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxBgpV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxBgpV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 8)
)
tmnxBgpV8v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4PathAttrGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeeringPolicyV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4ByteASNV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxBgpV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxBgpV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 9)
)
tmnxBgpV9v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4PathAttrGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeeringPolicyV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4ByteASNV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpAddPathV9v0R4Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpFlowSpecV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpDisableCapNegoV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxBgpV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxBgpV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 10)
)
tmnxBgpV10v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4PathAttrGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeeringPolicyV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4ByteASNV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpAddPathV9v0R4Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpFlowSpecV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpDisableCapNegoV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeeringPlcyV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpRTConstraintV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxBgpV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxBgpV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 11)
)
tmnxBgpV11v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV5v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4PathAttrGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerParamsV6v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeeringPolicyV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgp4ByteASNV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV11v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV7v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV8v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpAddPathV9v0R4Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpFlowSpecV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpDisableCapNegoV9v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeeringPlcyV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpRTConstraintV10v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalV11v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpGlobalDCGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpDPOscilationV11v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV11v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV11v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpMvpnVrfImportGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNHUnchangedGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpMcastIpv6Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPrefixOriginValidGroup"))
)
if mibBuilder.loadTexts:
    tmnxBgpV11v0Compliance.setStatus(
        "current"
    )

tmnxBgpV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 14, 1, 12)
)
tmnxBgpV12v0Compliance.setObjects(
      *(("TIMETRA-BGP-MIB", "tmnxBgpResolveLabelRoutesGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpThirdPartyNHGroup"),
        ("TIMETRA-BGP-MIB", "tmnxBgpInstanceV12v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerGroupV12v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpPeerV12v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpObsoleteV12v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotificationV12v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpNotifyObjsV12v0Group"),
        ("TIMETRA-BGP-MIB", "tmnxBgpRibLeakImportV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxBgpV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-BGP-MIB",
    **{"BgpKeepAliveTime": BgpKeepAliveTime,
       "BgpMinASOriginationTime": BgpMinASOriginationTime,
       "BgpLoopDetect": BgpLoopDetect,
       "BgpMinRouteAdvertisement": BgpMinRouteAdvertisement,
       "BgpMEDSource": BgpMEDSource,
       "BgpMEDValue": BgpMEDValue,
       "BgpTimeToLive": BgpTimeToLive,
       "BgpMultiPath": BgpMultiPath,
       "BgpPeerGroupName": BgpPeerGroupName,
       "BgpPeerGroupNameOrEmpty": BgpPeerGroupNameOrEmpty,
       "BgpPrefixLimit": BgpPrefixLimit,
       "BgpPeerType": BgpPeerType,
       "BgpPeerState": BgpPeerState,
       "BgpPeerEvent": BgpPeerEvent,
       "BgpOperState": BgpOperState,
       "TmnxIpFamily": TmnxIpFamily,
       "TmnxVpnCapability": TmnxVpnCapability,
       "TmnxAdvLabelAddressFamily": TmnxAdvLabelAddressFamily,
       "TmnxAddPathAddressFamily": TmnxAddPathAddressFamily,
       "TmnxAddPathSendLimit": TmnxAddPathSendLimit,
       "TmnxBgpFlowRouteExtCommAction": TmnxBgpFlowRouteExtCommAction,
       "TmnxIpNhChgFamily": TmnxIpNhChgFamily,
       "TmnxIpFamilyIdentifier": TmnxIpFamilyIdentifier,
       "timetraBgpMIBModule": timetraBgpMIBModule,
       "tmnxBgpConformance": tmnxBgpConformance,
       "tmnxBgpCompliances": tmnxBgpCompliances,
       "tmnxBgpV4v0Compliance": tmnxBgpV4v0Compliance,
       "tmnxBgpV5v0Compliance": tmnxBgpV5v0Compliance,
       "tmnxBgpV6v0Compliance": tmnxBgpV6v0Compliance,
       "tmnxBgpV7v0Compliance": tmnxBgpV7v0Compliance,
       "tmnxBgpV8v0Compliance": tmnxBgpV8v0Compliance,
       "tmnxBgpV9v0Compliance": tmnxBgpV9v0Compliance,
       "tmnxBgpV10v0Compliance": tmnxBgpV10v0Compliance,
       "tmnxBgpV11v0Compliance": tmnxBgpV11v0Compliance,
       "tmnxBgpV12v0Compliance": tmnxBgpV12v0Compliance,
       "tmnxBgpGroups": tmnxBgpGroups,
       "tmnxBgpConfederationGroup": tmnxBgpConfederationGroup,
       "tmnxBgp4PathAttrGroup": tmnxBgp4PathAttrGroup,
       "tmnxBgpPeerV4v0Group": tmnxBgpPeerV4v0Group,
       "tmnxBgpInstanceV4v0Group": tmnxBgpInstanceV4v0Group,
       "tmnxBgpObsoleteV4v0Group": tmnxBgpObsoleteV4v0Group,
       "tmnxBgpPeerParamsV4v0Group": tmnxBgpPeerParamsV4v0Group,
       "tmnxBgpPeerGroupParamsV4v0Group": tmnxBgpPeerGroupParamsV4v0Group,
       "tmnxBgpPeerGroupV4v0Group": tmnxBgpPeerGroupV4v0Group,
       "tmnxBgpNotificationV4v0Group": tmnxBgpNotificationV4v0Group,
       "tmnxBgpObsoleteNotificationV4v0Group": tmnxBgpObsoleteNotificationV4v0Group,
       "tmnxBgpInstanceParamsV4v0Group": tmnxBgpInstanceParamsV4v0Group,
       "tmnxBgpPeerV5v0Group": tmnxBgpPeerV5v0Group,
       "tmnxBgpObsoleteV5v0Group": tmnxBgpObsoleteV5v0Group,
       "tmnxBgpPeerParamsV5v0Group": tmnxBgpPeerParamsV5v0Group,
       "tmnxBgpInstanceParamsV5v0Group": tmnxBgpInstanceParamsV5v0Group,
       "tmnxBgpPeerGroupParamsV5v0Group": tmnxBgpPeerGroupParamsV5v0Group,
       "tmnxBgpNotificationV5v0Group": tmnxBgpNotificationV5v0Group,
       "tmnxBgpInstanceParamsV6v0Group": tmnxBgpInstanceParamsV6v0Group,
       "tmnxBgpPeerGroupParamsV6v0Group": tmnxBgpPeerGroupParamsV6v0Group,
       "tmnxBgpPeerParamsV6v0Group": tmnxBgpPeerParamsV6v0Group,
       "tmnxBgpPeerV6v0Group": tmnxBgpPeerV6v0Group,
       "tmnxBgpPeeringPolicyV7v0Group": tmnxBgpPeeringPolicyV7v0Group,
       "tmnxBgp4ByteASNV7v0Group": tmnxBgp4ByteASNV7v0Group,
       "tmnxBgpInstanceV7v0Group": tmnxBgpInstanceV7v0Group,
       "tmnxBgpPeerGroupV7v0Group": tmnxBgpPeerGroupV7v0Group,
       "tmnxBgpPeerV7v0Group": tmnxBgpPeerV7v0Group,
       "tmnxBgpObsoleteV7v0Group": tmnxBgpObsoleteV7v0Group,
       "tmnxBgpNotifyObjsV7v0Group": tmnxBgpNotifyObjsV7v0Group,
       "tmnxBgpNotificationV7v0Group": tmnxBgpNotificationV7v0Group,
       "tmnxBgpInstanceV8v0Group": tmnxBgpInstanceV8v0Group,
       "tmnxBgpObsoleteV8v0Group": tmnxBgpObsoleteV8v0Group,
       "tmnxBgpPeerV8v0Group": tmnxBgpPeerV8v0Group,
       "tmnxBgpGlobalV8v0Group": tmnxBgpGlobalV8v0Group,
       "tmnxBgpAddPathV9v0R4Group": tmnxBgpAddPathV9v0R4Group,
       "tmnxBgpPeerV9v0Group": tmnxBgpPeerV9v0Group,
       "tmnxBgpGlobalV9v0Group": tmnxBgpGlobalV9v0Group,
       "tmnxBgpFlowSpecV9v0Group": tmnxBgpFlowSpecV9v0Group,
       "tmnxBgpDisableCapNegoV9v0Group": tmnxBgpDisableCapNegoV9v0Group,
       "tmnxBgpNotifyObjsV9v0Group": tmnxBgpNotifyObjsV9v0Group,
       "tmnxBgpNotificationV9v0Group": tmnxBgpNotificationV9v0Group,
       "tmnxBgpGlobalV10v0Group": tmnxBgpGlobalV10v0Group,
       "tmnxBgpRTConstraintV10v0Group": tmnxBgpRTConstraintV10v0Group,
       "tmnxBgpInstanceV10v0Group": tmnxBgpInstanceV10v0Group,
       "tmnxBgpPeerGroupV10v0Group": tmnxBgpPeerGroupV10v0Group,
       "tmnxBgpPeerV10v0Group": tmnxBgpPeerV10v0Group,
       "tmnxBgpPeeringPlcyV10v0Group": tmnxBgpPeeringPlcyV10v0Group,
       "tmnxBgpPeeringPolicyV10v0Group": tmnxBgpPeeringPolicyV10v0Group,
       "tmnxBgpObsoleteV10v0Group": tmnxBgpObsoleteV10v0Group,
       "tmnxBgpGlobalV11v0Group": tmnxBgpGlobalV11v0Group,
       "tmnxBgpPeerGroupV11v0Group": tmnxBgpPeerGroupV11v0Group,
       "tmnxBgpObsoleteV11v0Group": tmnxBgpObsoleteV11v0Group,
       "tmnxBgpGlobalDCGroup": tmnxBgpGlobalDCGroup,
       "tmnxBgpDPOscilationV11v0Group": tmnxBgpDPOscilationV11v0Group,
       "tmnxBgpNotifyObjsV11v0Group": tmnxBgpNotifyObjsV11v0Group,
       "tmnxBgpNotificationV11v0Group": tmnxBgpNotificationV11v0Group,
       "tmnxBgpObsoleteNtfnV11v0Group": tmnxBgpObsoleteNtfnV11v0Group,
       "tmnxBgpMvpnVrfImportGroup": tmnxBgpMvpnVrfImportGroup,
       "tmnxBgpNHUnchangedGroup": tmnxBgpNHUnchangedGroup,
       "tmnxBgpResolveLabelRoutesGroup": tmnxBgpResolveLabelRoutesGroup,
       "tmnxBgpInstanceV12v0Group": tmnxBgpInstanceV12v0Group,
       "tmnxBgpPeerGroupV12v0Group": tmnxBgpPeerGroupV12v0Group,
       "tmnxBgpPeerV12v0Group": tmnxBgpPeerV12v0Group,
       "tmnxBgpObsoleteV12v0Group": tmnxBgpObsoleteV12v0Group,
       "tmnxBgpMcastIpv6Group": tmnxBgpMcastIpv6Group,
       "tmnxBgpPrefixOriginValidGroup": tmnxBgpPrefixOriginValidGroup,
       "tmnxBgpThirdPartyNHGroup": tmnxBgpThirdPartyNHGroup,
       "tmnxBgpNotificationV12v0Group": tmnxBgpNotificationV12v0Group,
       "tmnxBgpNotifyObjsV12v0Group": tmnxBgpNotifyObjsV12v0Group,
       "tmnxBgpRibLeakImportV12v0Group": tmnxBgpRibLeakImportV12v0Group,
       "tBgpObjects": tBgpObjects,
       "tBgpGlobalObjects": tBgpGlobalObjects,
       "tBgpInstanceObjects": tBgpInstanceObjects,
       "tBgpInstanceTableLastChanged": tBgpInstanceTableLastChanged,
       "tBgpInstanceTable": tBgpInstanceTable,
       "tBgpInstanceEntry": tBgpInstanceEntry,
       "tBgpInstanceIndex": tBgpInstanceIndex,
       "tBgpInstanceRowStatus": tBgpInstanceRowStatus,
       "tBgpInstanceShutdown": tBgpInstanceShutdown,
       "tBgpInstanceDescription": tBgpInstanceDescription,
       "tBgpInstanceAlwaysCompareMED": tBgpInstanceAlwaysCompareMED,
       "tBgpInstanceAsPathIgnore": tBgpInstanceAsPathIgnore,
       "tBgpInstanceBgpId": tBgpInstanceBgpId,
       "tBgpInstanceConnectRetry": tBgpInstanceConnectRetry,
       "tBgpInstanceHoldTime": tBgpInstanceHoldTime,
       "tBgpInstanceKeepAlive": tBgpInstanceKeepAlive,
       "tBgpInstanceMinASOrigination": tBgpInstanceMinASOrigination,
       "tBgpInstanceDampening": tBgpInstanceDampening,
       "tBgpInstanceLocalAS": tBgpInstanceLocalAS,
       "tBgpInstanceLocalPreference": tBgpInstanceLocalPreference,
       "tBgpInstanceLoopDetect": tBgpInstanceLoopDetect,
       "tBgpInstanceMinRouteAdvertisement": tBgpInstanceMinRouteAdvertisement,
       "tBgpInstanceMultipath": tBgpInstanceMultipath,
       "tBgpInstanceNoAggregatorID": tBgpInstanceNoAggregatorID,
       "tBgpInstancePreference": tBgpInstancePreference,
       "tBgpInstanceRemovePrivateAS": tBgpInstanceRemovePrivateAS,
       "tBgpInstanceLastChanged": tBgpInstanceLastChanged,
       "tBgpInstanceMultihop": tBgpInstanceMultihop,
       "tBgpInstanceMEDSource": tBgpInstanceMEDSource,
       "tBgpInstanceMEDValue": tBgpInstanceMEDValue,
       "tBgpInstanceConfederationAS": tBgpInstanceConfederationAS,
       "tBgpInstanceImportPolicy1": tBgpInstanceImportPolicy1,
       "tBgpInstanceImportPolicy2": tBgpInstanceImportPolicy2,
       "tBgpInstanceImportPolicy3": tBgpInstanceImportPolicy3,
       "tBgpInstanceImportPolicy4": tBgpInstanceImportPolicy4,
       "tBgpInstanceImportPolicy5": tBgpInstanceImportPolicy5,
       "tBgpInstanceExportPolicy1": tBgpInstanceExportPolicy1,
       "tBgpInstanceExportPolicy2": tBgpInstanceExportPolicy2,
       "tBgpInstanceExportPolicy3": tBgpInstanceExportPolicy3,
       "tBgpInstanceExportPolicy4": tBgpInstanceExportPolicy4,
       "tBgpInstanceExportPolicy5": tBgpInstanceExportPolicy5,
       "tBgpInstanceOperStatus": tBgpInstanceOperStatus,
       "tBgpInstanceLocalASPrivate": tBgpInstanceLocalASPrivate,
       "tBgpInstanceMd5Auth": tBgpInstanceMd5Auth,
       "tBgpInstanceMd5AuthKey": tBgpInstanceMd5AuthKey,
       "tBgpInstanceClusterId": tBgpInstanceClusterId,
       "tBgpInstanceDisableClientReflect": tBgpInstanceDisableClientReflect,
       "tBgpInstanceIBgpMultipath": tBgpInstanceIBgpMultipath,
       "tBgpInstanceFamily": tBgpInstanceFamily,
       "tBgpInstanceGracefulRestart": tBgpInstanceGracefulRestart,
       "tBgpInstanceGRPathSelectDefer": tBgpInstanceGRPathSelectDefer,
       "tBgpInstanceGRRestartTime": tBgpInstanceGRRestartTime,
       "tBgpInstanceGRStaleRoute": tBgpInstanceGRStaleRoute,
       "tBgpInstanceGRAdminState": tBgpInstanceGRAdminState,
       "tBgpInstanceGROperState": tBgpInstanceGROperState,
       "tBgpInstanceVpnApplyImport": tBgpInstanceVpnApplyImport,
       "tBgpInstanceVpnApplyExport": tBgpInstanceVpnApplyExport,
       "tBgpInstanceIgpShortcut": tBgpInstanceIgpShortcut,
       "tBgpInstanceDisallowIgp": tBgpInstanceDisallowIgp,
       "tBgpInstanceOrf": tBgpInstanceOrf,
       "tBgpInstanceExtCommsOrf": tBgpInstanceExtCommsOrf,
       "tBgpInstanceExtCommsSendOrf": tBgpInstanceExtCommsSendOrf,
       "tBgpInstanceExtCommsRecvOrf": tBgpInstanceExtCommsRecvOrf,
       "tBgpInstanceAllowInterAsVpn": tBgpInstanceAllowInterAsVpn,
       "tBgpInstancePurgeTimer": tBgpInstancePurgeTimer,
       "tBgpInstanceLocalAS4Byte": tBgpInstanceLocalAS4Byte,
       "tBgpInstanceConfederationAS4Byte": tBgpInstanceConfederationAS4Byte,
       "tBgpInstanceDisable4ByteASN": tBgpInstanceDisable4ByteASN,
       "tBgpInstanceMultipathEiBgpState": tBgpInstanceMultipathEiBgpState,
       "tBgpInstanceHoldTimeIsStrict": tBgpInstanceHoldTimeIsStrict,
       "tBgpInstanceAsPathIgnoreFamily": tBgpInstanceAsPathIgnoreFamily,
       "tBgpInstanceRemovePrivateASLmtd": tBgpInstanceRemovePrivateASLmtd,
       "tBgpInstancePMTUDiscovery": tBgpInstancePMTUDiscovery,
       "tBgpInstanceDisableRtTblInstall": tBgpInstanceDisableRtTblInstall,
       "tBgpInstanceNHResUseBgpRoutes": tBgpInstanceNHResUseBgpRoutes,
       "tBgpInstanceEnableRRVpnFwding": tBgpInstanceEnableRRVpnFwding,
       "tBgpInstRteTargetTable": tBgpInstRteTargetTable,
       "tBgpInstRteTargetEntry": tBgpInstRteTargetEntry,
       "tBgpInstanceRouteTarget": tBgpInstanceRouteTarget,
       "tBgpInstRteTargetRowStatus": tBgpInstRteTargetRowStatus,
       "tBgp4PathAttrTable": tBgp4PathAttrTable,
       "tBgp4PathAttrEntry": tBgp4PathAttrEntry,
       "tBgp4PathAttrRD": tBgp4PathAttrRD,
       "tBgp4PathAttrOriginID": tBgp4PathAttrOriginID,
       "tBgp4PathAttrClusterList": tBgp4PathAttrClusterList,
       "tBgp4PathAttrCommunity": tBgp4PathAttrCommunity,
       "tBgp4PathAttrExtCommunity": tBgp4PathAttrExtCommunity,
       "tbgp4PathAttrASPathSegment": tbgp4PathAttrASPathSegment,
       "tbgp4PathAttrAggregatorAS": tbgp4PathAttrAggregatorAS,
       "tBgpSendOrfRouteTargetTable": tBgpSendOrfRouteTargetTable,
       "tBgpSendOrfRouteTargetEntry": tBgpSendOrfRouteTargetEntry,
       "tBgpSendOrfRouteTarget": tBgpSendOrfRouteTarget,
       "tBgpSendOrfRTRowStatus": tBgpSendOrfRTRowStatus,
       "tBgpInstanceParamsTable": tBgpInstanceParamsTable,
       "tBgpInstanceParamsEntry": tBgpInstanceParamsEntry,
       "tBgpInstanceDisableFEFailover": tBgpInstanceDisableFEFailover,
       "tBgpInstanceDisableComms": tBgpInstanceDisableComms,
       "tBgpInstanceDisableExtComms": tBgpInstanceDisableExtComms,
       "tBgpInstanceDefaultOriginate": tBgpInstanceDefaultOriginate,
       "tBgpInstanceAdvertiseInactiveRts": tBgpInstanceAdvertiseInactiveRts,
       "tBgpInstancePeerTracking": tBgpInstancePeerTracking,
       "tBgpInstanceAuthKeyChain": tBgpInstanceAuthKeyChain,
       "tBgpInstanceRapidWithdrawal": tBgpInstanceRapidWithdrawal,
       "tBgpInstanceBfdEnabled": tBgpInstanceBfdEnabled,
       "tBgpInstanceRapidUpdate": tBgpInstanceRapidUpdate,
       "tBgpInstanceEnableAddPath": tBgpInstanceEnableAddPath,
       "tBgpInstanceRecvAddPath": tBgpInstanceRecvAddPath,
       "tBgpInstanceIpv4AddPathLimit": tBgpInstanceIpv4AddPathLimit,
       "tBgpInstanceVpnIpv4AddPathLimit": tBgpInstanceVpnIpv4AddPathLimit,
       "tBgpInstanceIpv6AddPathLimit": tBgpInstanceIpv6AddPathLimit,
       "tBgpInstanceVpnIpv6AddPathLimit": tBgpInstanceVpnIpv6AddPathLimit,
       "tBgpInstanceTransportTunnel": tBgpInstanceTransportTunnel,
       "tBgpInstanceFlowspecValidate": tBgpInstanceFlowspecValidate,
       "tBgpInstanceAdvertiseExternal": tBgpInstanceAdvertiseExternal,
       "tBgpInstanceBackupPath": tBgpInstanceBackupPath,
       "tBgpInstanceIgnoreNextHopMetric": tBgpInstanceIgnoreNextHopMetric,
       "tBgpInstanceMpBgpKeep": tBgpInstanceMpBgpKeep,
       "tBgpInstanceIgnoreRouterId": tBgpInstanceIgnoreRouterId,
       "tBgpInstanceAlwaysCompMEDStrict": tBgpInstanceAlwaysCompMEDStrict,
       "tBgpInstanceMinHoldTime": tBgpInstanceMinHoldTime,
       "tBgpInstRemovePrivateSkipPeerAs": tBgpInstRemovePrivateSkipPeerAs,
       "tBgpInstLocalASNoPrependGlobalAS": tBgpInstLocalASNoPrependGlobalAS,
       "tBgpInstanceNHResPolicy": tBgpInstanceNHResPolicy,
       "tBgpInstancePeerTrackingPolicy": tBgpInstancePeerTrackingPolicy,
       "tBgpInstGrRestartNotification": tBgpInstGrRestartNotification,
       "tBgpInstanceFaultTolerance": tBgpInstanceFaultTolerance,
       "tBgpInstanceDampPeerOscillations": tBgpInstanceDampPeerOscillations,
       "tBgpInstDmpPeerOscInitialWaitTim": tBgpInstDmpPeerOscInitialWaitTim,
       "tBgpInstDmpPeerOscSecondWaitTime": tBgpInstDmpPeerOscSecondWaitTime,
       "tBgpInstDmpPeerOscMaxWaitTime": tBgpInstDmpPeerOscMaxWaitTime,
       "tBgpInstDmpPeerOscErrorInterval": tBgpInstDmpPeerOscErrorInterval,
       "tBgpInstanceDeterministicMED": tBgpInstanceDeterministicMED,
       "tBgpInstanceSplitHorizon": tBgpInstanceSplitHorizon,
       "tBgpInstMvpnVrfImportSubTypeNew": tBgpInstMvpnVrfImportSubTypeNew,
       "tBgpInstResolveLabelRoutesInRtm": tBgpInstResolveLabelRoutesInRtm,
       "tBgpInstanceCompOriginValidState": tBgpInstanceCompOriginValidState,
       "tBgpInstanceThirdPartyNextHop": tBgpInstanceThirdPartyNextHop,
       "tBgpInstanceOrigInvalidUnusable": tBgpInstanceOrigInvalidUnusable,
       "tBgpInstanceIgnoreRtrIdInternal": tBgpInstanceIgnoreRtrIdInternal,
       "tBgpInstanceIgnoreRtrIdExternal": tBgpInstanceIgnoreRtrIdExternal,
       "tBgpInstancePlcyTable": tBgpInstancePlcyTable,
       "tBgpInstancePlcyEntry": tBgpInstancePlcyEntry,
       "tBgpInstancePlcyImportPolicy1": tBgpInstancePlcyImportPolicy1,
       "tBgpInstancePlcyImportPolicy2": tBgpInstancePlcyImportPolicy2,
       "tBgpInstancePlcyImportPolicy3": tBgpInstancePlcyImportPolicy3,
       "tBgpInstancePlcyImportPolicy4": tBgpInstancePlcyImportPolicy4,
       "tBgpInstancePlcyImportPolicy5": tBgpInstancePlcyImportPolicy5,
       "tBgpInstancePlcyImportPolicy6": tBgpInstancePlcyImportPolicy6,
       "tBgpInstancePlcyImportPolicy7": tBgpInstancePlcyImportPolicy7,
       "tBgpInstancePlcyImportPolicy8": tBgpInstancePlcyImportPolicy8,
       "tBgpInstancePlcyImportPolicy9": tBgpInstancePlcyImportPolicy9,
       "tBgpInstancePlcyImportPolicy10": tBgpInstancePlcyImportPolicy10,
       "tBgpInstancePlcyImportPolicy11": tBgpInstancePlcyImportPolicy11,
       "tBgpInstancePlcyImportPolicy12": tBgpInstancePlcyImportPolicy12,
       "tBgpInstancePlcyImportPolicy13": tBgpInstancePlcyImportPolicy13,
       "tBgpInstancePlcyImportPolicy14": tBgpInstancePlcyImportPolicy14,
       "tBgpInstancePlcyImportPolicy15": tBgpInstancePlcyImportPolicy15,
       "tBgpInstancePlcyExportPolicy1": tBgpInstancePlcyExportPolicy1,
       "tBgpInstancePlcyExportPolicy2": tBgpInstancePlcyExportPolicy2,
       "tBgpInstancePlcyExportPolicy3": tBgpInstancePlcyExportPolicy3,
       "tBgpInstancePlcyExportPolicy4": tBgpInstancePlcyExportPolicy4,
       "tBgpInstancePlcyExportPolicy5": tBgpInstancePlcyExportPolicy5,
       "tBgpInstancePlcyExportPolicy6": tBgpInstancePlcyExportPolicy6,
       "tBgpInstancePlcyExportPolicy7": tBgpInstancePlcyExportPolicy7,
       "tBgpInstancePlcyExportPolicy8": tBgpInstancePlcyExportPolicy8,
       "tBgpInstancePlcyExportPolicy9": tBgpInstancePlcyExportPolicy9,
       "tBgpInstancePlcyExportPolicy10": tBgpInstancePlcyExportPolicy10,
       "tBgpInstancePlcyExportPolicy11": tBgpInstancePlcyExportPolicy11,
       "tBgpInstancePlcyExportPolicy12": tBgpInstancePlcyExportPolicy12,
       "tBgpInstancePlcyExportPolicy13": tBgpInstancePlcyExportPolicy13,
       "tBgpInstancePlcyExportPolicy14": tBgpInstancePlcyExportPolicy14,
       "tBgpInstancePlcyExportPolicy15": tBgpInstancePlcyExportPolicy15,
       "tBgpRibLeakImportPolicyTblLstCh": tBgpRibLeakImportPolicyTblLstCh,
       "tBgpRibLeakImportPolicyTable": tBgpRibLeakImportPolicyTable,
       "tBgpRibLeakImportPolicyEntry": tBgpRibLeakImportPolicyEntry,
       "tBgpRibLeakImportPolicyFamily": tBgpRibLeakImportPolicyFamily,
       "tBgpRibLeakImportPolicyLstCh": tBgpRibLeakImportPolicyLstCh,
       "tBgpRibLeakImportPolicy1": tBgpRibLeakImportPolicy1,
       "tBgpRibLeakImportPolicy2": tBgpRibLeakImportPolicy2,
       "tBgpRibLeakImportPolicy3": tBgpRibLeakImportPolicy3,
       "tBgpRibLeakImportPolicy4": tBgpRibLeakImportPolicy4,
       "tBgpRibLeakImportPolicy5": tBgpRibLeakImportPolicy5,
       "tBgpRibLeakImportPolicy6": tBgpRibLeakImportPolicy6,
       "tBgpRibLeakImportPolicy7": tBgpRibLeakImportPolicy7,
       "tBgpRibLeakImportPolicy8": tBgpRibLeakImportPolicy8,
       "tBgpRibLeakImportPolicy9": tBgpRibLeakImportPolicy9,
       "tBgpRibLeakImportPolicy10": tBgpRibLeakImportPolicy10,
       "tBgpRibLeakImportPolicy11": tBgpRibLeakImportPolicy11,
       "tBgpRibLeakImportPolicy12": tBgpRibLeakImportPolicy12,
       "tBgpRibLeakImportPolicy13": tBgpRibLeakImportPolicy13,
       "tBgpRibLeakImportPolicy14": tBgpRibLeakImportPolicy14,
       "tBgpRibLeakImportPolicy15": tBgpRibLeakImportPolicy15,
       "tBgpPeerGroupObjects": tBgpPeerGroupObjects,
       "tBgpPeerGroupTableLastChanged": tBgpPeerGroupTableLastChanged,
       "tBgpPeerGroupTableSpinlock": tBgpPeerGroupTableSpinlock,
       "tBgpPeerGroupTable": tBgpPeerGroupTable,
       "tBgpPeerGroupEntry": tBgpPeerGroupEntry,
       "tBgpPeerGroupName": tBgpPeerGroupName,
       "tBgpPeerGroupRowStatus": tBgpPeerGroupRowStatus,
       "tBgpPeerGroupShutdown": tBgpPeerGroupShutdown,
       "tBgpPeerGroupDescription": tBgpPeerGroupDescription,
       "tBgpPeerGroupConnectRetry": tBgpPeerGroupConnectRetry,
       "tBgpPeerGroupHoldTime": tBgpPeerGroupHoldTime,
       "tBgpPeerGroupKeepAlive": tBgpPeerGroupKeepAlive,
       "tBgpPeerGroupMinASOrigination": tBgpPeerGroupMinASOrigination,
       "tBgpPeerGroupDampening": tBgpPeerGroupDampening,
       "tBgpPeerGroupLocalAddress": tBgpPeerGroupLocalAddress,
       "tBgpPeerGroupLocalAS": tBgpPeerGroupLocalAS,
       "tBgpPeerGroupLocalPreference": tBgpPeerGroupLocalPreference,
       "tBgpPeerGroupLoopDetect": tBgpPeerGroupLoopDetect,
       "tBgpPeerGroupMinRouteAdvertisement": tBgpPeerGroupMinRouteAdvertisement,
       "tBgpPeerGroupMaxPrefix": tBgpPeerGroupMaxPrefix,
       "tBgpPeerGroupMEDSource": tBgpPeerGroupMEDSource,
       "tBgpPeerGroupMEDValue": tBgpPeerGroupMEDValue,
       "tBgpPeerGroupMultihop": tBgpPeerGroupMultihop,
       "tBgpPeerGroupNextHopSelf": tBgpPeerGroupNextHopSelf,
       "tBgpPeerGroupNoAggregatorID": tBgpPeerGroupNoAggregatorID,
       "tBgpPeerGroupPassive": tBgpPeerGroupPassive,
       "tBgpPeerGroupPeerAS": tBgpPeerGroupPeerAS,
       "tBgpPeerGroupPeerType": tBgpPeerGroupPeerType,
       "tBgpPeerGroupPreference": tBgpPeerGroupPreference,
       "tBgpPeerGroupRemovePrivateAS": tBgpPeerGroupRemovePrivateAS,
       "tBgpPeerGroupLastChanged": tBgpPeerGroupLastChanged,
       "tBgpPeerGroupInheritance": tBgpPeerGroupInheritance,
       "tBgpPeerGroupImportPolicy1": tBgpPeerGroupImportPolicy1,
       "tBgpPeerGroupImportPolicy2": tBgpPeerGroupImportPolicy2,
       "tBgpPeerGroupImportPolicy3": tBgpPeerGroupImportPolicy3,
       "tBgpPeerGroupImportPolicy4": tBgpPeerGroupImportPolicy4,
       "tBgpPeerGroupImportPolicy5": tBgpPeerGroupImportPolicy5,
       "tBgpPeerGroupExportPolicy1": tBgpPeerGroupExportPolicy1,
       "tBgpPeerGroupExportPolicy2": tBgpPeerGroupExportPolicy2,
       "tBgpPeerGroupExportPolicy3": tBgpPeerGroupExportPolicy3,
       "tBgpPeerGroupExportPolicy4": tBgpPeerGroupExportPolicy4,
       "tBgpPeerGroupExportPolicy5": tBgpPeerGroupExportPolicy5,
       "tBgpPeerGroupOperStatus": tBgpPeerGroupOperStatus,
       "tBgpPeerGroupLocalASPrivate": tBgpPeerGroupLocalASPrivate,
       "tBgpPeerGroupMd5Auth": tBgpPeerGroupMd5Auth,
       "tBgpPeerGroupMd5AuthKey": tBgpPeerGroupMd5AuthKey,
       "tBgpPeerGroupClusterId": tBgpPeerGroupClusterId,
       "tBgpPeerGroupDisableClientReflect": tBgpPeerGroupDisableClientReflect,
       "tBgpPeerGroupGracefulRestart": tBgpPeerGroupGracefulRestart,
       "tBgpPeerGroupGRRestartTime": tBgpPeerGroupGRRestartTime,
       "tBgpPeerGroupGRStaleRoute": tBgpPeerGroupGRStaleRoute,
       "tBgpPeerGroupGRAdminState": tBgpPeerGroupGRAdminState,
       "tBgpPeerGroupGROperState": tBgpPeerGroupGROperState,
       "tBgpPeerGroupFamily": tBgpPeerGroupFamily,
       "tBgpPeerGroupVpnApplyImport": tBgpPeerGroupVpnApplyImport,
       "tBgpPeerGroupVpnApplyExport": tBgpPeerGroupVpnApplyExport,
       "tBgpPeerGroupASOverride": tBgpPeerGroupASOverride,
       "tBgpPeerGroupOrf": tBgpPeerGroupOrf,
       "tBgpPeerGroupExtCommsOrf": tBgpPeerGroupExtCommsOrf,
       "tBgpPeerGroupExtCommsSendOrf": tBgpPeerGroupExtCommsSendOrf,
       "tBgpPeerGroupExtCommsRecvOrf": tBgpPeerGroupExtCommsRecvOrf,
       "tBgpPeerGroupDynamicPeerGroup": tBgpPeerGroupDynamicPeerGroup,
       "tBgpPeerGroupLocalAS4Byte": tBgpPeerGroupLocalAS4Byte,
       "tBgpPeerGroupPeerAS4Byte": tBgpPeerGroupPeerAS4Byte,
       "tBgpPeerGroupDisable4ByteASN": tBgpPeerGroupDisable4ByteASN,
       "tBgpPeerGroupHoldTimeIsStrict": tBgpPeerGroupHoldTimeIsStrict,
       "tBgpPeerGroupRemovePrivateASLmtd": tBgpPeerGroupRemovePrivateASLmtd,
       "tBgpPeerGroupPMTUDiscovery": tBgpPeerGroupPMTUDiscovery,
       "tBgpPeerGroupMaxPrefixLogOnly": tBgpPeerGroupMaxPrefixLogOnly,
       "tBgpPeerGroupMaxPrefixThreshold": tBgpPeerGroupMaxPrefixThreshold,
       "tBgpPeerGroupDisableCapNego": tBgpPeerGroupDisableCapNego,
       "tBgpPeerGroupCreationOrigin": tBgpPeerGroupCreationOrigin,
       "tBgpPGSendOrfRouteTargetTable": tBgpPGSendOrfRouteTargetTable,
       "tBgpPGSendOrfRouteTargetEntry": tBgpPGSendOrfRouteTargetEntry,
       "tBgpPGSendOrfRouteTarget": tBgpPGSendOrfRouteTarget,
       "tBgpPGSendOrfRTRowStatus": tBgpPGSendOrfRTRowStatus,
       "tBgpPeerGroupParamsTable": tBgpPeerGroupParamsTable,
       "tBgpPeerGroupParamsEntry": tBgpPeerGroupParamsEntry,
       "tBgpPGParamsInheritance": tBgpPGParamsInheritance,
       "tBgpPGDisableFEFailover": tBgpPGDisableFEFailover,
       "tBgpPGDisableComms": tBgpPGDisableComms,
       "tBgpPGDisableExtComms": tBgpPGDisableExtComms,
       "tBgpPGDefaultOriginate": tBgpPGDefaultOriginate,
       "tBgpPGAdvertiseInactiveRts": tBgpPGAdvertiseInactiveRts,
       "tBgpPGMinTTLValue": tBgpPGMinTTLValue,
       "tBgpPGTTLLogId": tBgpPGTTLLogId,
       "tBgpPGLocalAddressType": tBgpPGLocalAddressType,
       "tBgpPGLocalAddress": tBgpPGLocalAddress,
       "tBgpPGPeerTracking": tBgpPGPeerTracking,
       "tBgpPGAuthKeyChain": tBgpPGAuthKeyChain,
       "tBgpPGBfdEnabled": tBgpPGBfdEnabled,
       "tBgpPGEnableAddPath": tBgpPGEnableAddPath,
       "tBgpPGRecvAddPath": tBgpPGRecvAddPath,
       "tBgpPGIpv4AddPathLimit": tBgpPGIpv4AddPathLimit,
       "tBgpPGVpnIpv4AddPathLimit": tBgpPGVpnIpv4AddPathLimit,
       "tBgpPGIpv6AddPathLimit": tBgpPGIpv6AddPathLimit,
       "tBgpPGVpnIpv6AddPathLimit": tBgpPGVpnIpv6AddPathLimit,
       "tBgpPGFlowspecValidate": tBgpPGFlowspecValidate,
       "tBgpPGUpdatedErrorHandling": tBgpPGUpdatedErrorHandling,
       "tBgpPGDefaultRouteTarget": tBgpPGDefaultRouteTarget,
       "tBgpPGAigp": tBgpPGAigp,
       "tBgpPGMinHoldTime": tBgpPGMinHoldTime,
       "tBgpPGRemovePrivateSkipPeerAs": tBgpPGRemovePrivateSkipPeerAs,
       "tBgpPGLocalASNoPrependGlobalAS": tBgpPGLocalASNoPrependGlobalAS,
       "tBgpPGMaxPrefixIdleTimeOut": tBgpPGMaxPrefixIdleTimeOut,
       "tBgpPGGRRestartNotification": tBgpPGGRRestartNotification,
       "tBgpPGFaultTolerance": tBgpPGFaultTolerance,
       "tBgpPGDampPeerOscillations": tBgpPGDampPeerOscillations,
       "tBgpPGDampPeerOscInitialWaitTime": tBgpPGDampPeerOscInitialWaitTime,
       "tBgpPGDampPeerOscSecondWaitTime": tBgpPGDampPeerOscSecondWaitTime,
       "tBgpPGDampPeerOscMaxWaitTime": tBgpPGDampPeerOscMaxWaitTime,
       "tBgpPGDampPeerOscErrorInterval": tBgpPGDampPeerOscErrorInterval,
       "tBgpPGSplitHorizon": tBgpPGSplitHorizon,
       "tBgpPGNHUnchangedFamily": tBgpPGNHUnchangedFamily,
       "tBgpPGEnableOriginValidation": tBgpPGEnableOriginValidation,
       "tBgpPGThirdPartyNextHop": tBgpPGThirdPartyNextHop,
       "tBgpPeerGroupPlcyTable": tBgpPeerGroupPlcyTable,
       "tBgpPeerGroupPlcyEntry": tBgpPeerGroupPlcyEntry,
       "tBgpPeerGroupPlcyImportPolicy1": tBgpPeerGroupPlcyImportPolicy1,
       "tBgpPeerGroupPlcyImportPolicy2": tBgpPeerGroupPlcyImportPolicy2,
       "tBgpPeerGroupPlcyImportPolicy3": tBgpPeerGroupPlcyImportPolicy3,
       "tBgpPeerGroupPlcyImportPolicy4": tBgpPeerGroupPlcyImportPolicy4,
       "tBgpPeerGroupPlcyImportPolicy5": tBgpPeerGroupPlcyImportPolicy5,
       "tBgpPeerGroupPlcyImportPolicy6": tBgpPeerGroupPlcyImportPolicy6,
       "tBgpPeerGroupPlcyImportPolicy7": tBgpPeerGroupPlcyImportPolicy7,
       "tBgpPeerGroupPlcyImportPolicy8": tBgpPeerGroupPlcyImportPolicy8,
       "tBgpPeerGroupPlcyImportPolicy9": tBgpPeerGroupPlcyImportPolicy9,
       "tBgpPeerGroupPlcyImportPolicy10": tBgpPeerGroupPlcyImportPolicy10,
       "tBgpPeerGroupPlcyImportPolicy11": tBgpPeerGroupPlcyImportPolicy11,
       "tBgpPeerGroupPlcyImportPolicy12": tBgpPeerGroupPlcyImportPolicy12,
       "tBgpPeerGroupPlcyImportPolicy13": tBgpPeerGroupPlcyImportPolicy13,
       "tBgpPeerGroupPlcyImportPolicy14": tBgpPeerGroupPlcyImportPolicy14,
       "tBgpPeerGroupPlcyImportPolicy15": tBgpPeerGroupPlcyImportPolicy15,
       "tBgpPeerGroupPlcyExportPolicy1": tBgpPeerGroupPlcyExportPolicy1,
       "tBgpPeerGroupPlcyExportPolicy2": tBgpPeerGroupPlcyExportPolicy2,
       "tBgpPeerGroupPlcyExportPolicy3": tBgpPeerGroupPlcyExportPolicy3,
       "tBgpPeerGroupPlcyExportPolicy4": tBgpPeerGroupPlcyExportPolicy4,
       "tBgpPeerGroupPlcyExportPolicy5": tBgpPeerGroupPlcyExportPolicy5,
       "tBgpPeerGroupPlcyExportPolicy6": tBgpPeerGroupPlcyExportPolicy6,
       "tBgpPeerGroupPlcyExportPolicy7": tBgpPeerGroupPlcyExportPolicy7,
       "tBgpPeerGroupPlcyExportPolicy8": tBgpPeerGroupPlcyExportPolicy8,
       "tBgpPeerGroupPlcyExportPolicy9": tBgpPeerGroupPlcyExportPolicy9,
       "tBgpPeerGroupPlcyExportPolicy10": tBgpPeerGroupPlcyExportPolicy10,
       "tBgpPeerGroupPlcyExportPolicy11": tBgpPeerGroupPlcyExportPolicy11,
       "tBgpPeerGroupPlcyExportPolicy12": tBgpPeerGroupPlcyExportPolicy12,
       "tBgpPeerGroupPlcyExportPolicy13": tBgpPeerGroupPlcyExportPolicy13,
       "tBgpPeerGroupPlcyExportPolicy14": tBgpPeerGroupPlcyExportPolicy14,
       "tBgpPeerGroupPlcyExportPolicy15": tBgpPeerGroupPlcyExportPolicy15,
       "tBgpPeerObjects": tBgpPeerObjects,
       "tBgpPeerTableLastChanged": tBgpPeerTableLastChanged,
       "tBgpPeerTableSpinlock": tBgpPeerTableSpinlock,
       "tBgpPeerTable": tBgpPeerTable,
       "tBgpPeerEntry": tBgpPeerEntry,
       "tBgpPeerAddress": tBgpPeerAddress,
       "tBgpPeerPeerGroup": tBgpPeerPeerGroup,
       "tBgpPeerRowStatus": tBgpPeerRowStatus,
       "tBgpPeerShutdown": tBgpPeerShutdown,
       "tBgpPeerDescription": tBgpPeerDescription,
       "tBgpPeerConnectRetry": tBgpPeerConnectRetry,
       "tBgpPeerHoldTime": tBgpPeerHoldTime,
       "tBgpPeerKeepAlive": tBgpPeerKeepAlive,
       "tBgpPeerMinASOrigination": tBgpPeerMinASOrigination,
       "tBgpPeerDampening": tBgpPeerDampening,
       "tBgpPeerLocalAddress": tBgpPeerLocalAddress,
       "tBgpPeerLocalAS": tBgpPeerLocalAS,
       "tBgpPeerLocalPreference": tBgpPeerLocalPreference,
       "tBgpPeerLoopDetect": tBgpPeerLoopDetect,
       "tBgpPeerMinRouteAdvertisement": tBgpPeerMinRouteAdvertisement,
       "tBgpPeerMaxPrefix": tBgpPeerMaxPrefix,
       "tBgpPeerMEDSource": tBgpPeerMEDSource,
       "tBgpPeerMEDValue": tBgpPeerMEDValue,
       "tBgpPeerMultihop": tBgpPeerMultihop,
       "tBgpPeerNextHopSelf": tBgpPeerNextHopSelf,
       "tBgpPeerNoAggregatorID": tBgpPeerNoAggregatorID,
       "tBgpPeerPassive": tBgpPeerPassive,
       "tBgpPeerPeerAS": tBgpPeerPeerAS,
       "tBgpPeerPeerType": tBgpPeerPeerType,
       "tBgpPeerPreference": tBgpPeerPreference,
       "tBgpPeerRemovePrivateAS": tBgpPeerRemovePrivateAS,
       "tBgpPeerLastChanged": tBgpPeerLastChanged,
       "tBgpPeerInheritance": tBgpPeerInheritance,
       "tBgpPeerImportPolicy1": tBgpPeerImportPolicy1,
       "tBgpPeerImportPolicy2": tBgpPeerImportPolicy2,
       "tBgpPeerImportPolicy3": tBgpPeerImportPolicy3,
       "tBgpPeerImportPolicy4": tBgpPeerImportPolicy4,
       "tBgpPeerImportPolicy5": tBgpPeerImportPolicy5,
       "tBgpPeerExportPolicy1": tBgpPeerExportPolicy1,
       "tBgpPeerExportPolicy2": tBgpPeerExportPolicy2,
       "tBgpPeerExportPolicy3": tBgpPeerExportPolicy3,
       "tBgpPeerExportPolicy4": tBgpPeerExportPolicy4,
       "tBgpPeerExportPolicy5": tBgpPeerExportPolicy5,
       "tBgpPeerOperStatus": tBgpPeerOperStatus,
       "tBgpPeerLocalASPrivate": tBgpPeerLocalASPrivate,
       "tBgpPeerMd5Auth": tBgpPeerMd5Auth,
       "tBgpPeerMd5AuthKey": tBgpPeerMd5AuthKey,
       "tBgpPeerClusterId": tBgpPeerClusterId,
       "tBgpPeerDisableClientReflect": tBgpPeerDisableClientReflect,
       "tBgpPeerGracefulRestart": tBgpPeerGracefulRestart,
       "tBgpPeerGRRestartTime": tBgpPeerGRRestartTime,
       "tBgpPeerGRStaleRoute": tBgpPeerGRStaleRoute,
       "tBgpPeerGRAdminState": tBgpPeerGRAdminState,
       "tBgpPeerGROperState": tBgpPeerGROperState,
       "tBgpPeerFamily": tBgpPeerFamily,
       "tBgpPeerVpnRemoteFamily": tBgpPeerVpnRemoteFamily,
       "tBgpPeerVpnApplyImport": tBgpPeerVpnApplyImport,
       "tBgpPeerVpnApplyExport": tBgpPeerVpnApplyExport,
       "tBgpPeerVpnLocalCaps": tBgpPeerVpnLocalCaps,
       "tBgpPeerVpnRemoteCaps": tBgpPeerVpnRemoteCaps,
       "tBgpPeerConnState": tBgpPeerConnState,
       "tBgpPeerASOverride": tBgpPeerASOverride,
       "tBgpPeerOrf": tBgpPeerOrf,
       "tBgpPeerExtCommsOrf": tBgpPeerExtCommsOrf,
       "tBgpPeerExtCommsSendOrf": tBgpPeerExtCommsSendOrf,
       "tBgpPeerExtCommsRecvOrf": tBgpPeerExtCommsRecvOrf,
       "tBgpPeerOperTable": tBgpPeerOperTable,
       "tBgpPeerOperEntry": tBgpPeerOperEntry,
       "tBgpPeerOperMsgOctetsRcvd": tBgpPeerOperMsgOctetsRcvd,
       "tBgpPeerOperMsgOctetsSent": tBgpPeerOperMsgOctetsSent,
       "tBgpPeerOperInputQueueMessages": tBgpPeerOperInputQueueMessages,
       "tBgpPeerOperOutputQueueMessages": tBgpPeerOperOutputQueueMessages,
       "tBgpPeerOperReceivedPrefixes": tBgpPeerOperReceivedPrefixes,
       "tBgpPeerOperSentPrefixes": tBgpPeerOperSentPrefixes,
       "tBgpPeerOperActivePrefixes": tBgpPeerOperActivePrefixes,
       "tBgpPeerOperReceivedPaths": tBgpPeerOperReceivedPaths,
       "tBgpPeerOperPathsSuppressedByDamping": tBgpPeerOperPathsSuppressedByDamping,
       "tBgpPeerOperFlaps": tBgpPeerOperFlaps,
       "tBgpPeerOperLastState": tBgpPeerOperLastState,
       "tBgpPeerOperLastEvent": tBgpPeerOperLastEvent,
       "tBgpPeerOperVpnReceivedPrefixes": tBgpPeerOperVpnReceivedPrefixes,
       "tBgpPeerOperVpnSentPrefixes": tBgpPeerOperVpnSentPrefixes,
       "tBgpPeerOperVpnActivePrefixes": tBgpPeerOperVpnActivePrefixes,
       "tBgpPeerOperGRSupport": tBgpPeerOperGRSupport,
       "tBgpPeerOperGRFamilyRestart": tBgpPeerOperGRFamilyRestart,
       "tBgpPeerOperGRFamilyFwding": tBgpPeerOperGRFamilyFwding,
       "tBgpPeerOperGRFamilyNegotiated": tBgpPeerOperGRFamilyNegotiated,
       "tBgpPeerOperGRRecvEOR": tBgpPeerOperGRRecvEOR,
       "tBgpPeerOperGRSendEOR": tBgpPeerOperGRSendEOR,
       "tBgpPeerOperGRStaleRoutesTime": tBgpPeerOperGRStaleRoutesTime,
       "tBgpPeerOperGRRequestRestartTime": tBgpPeerOperGRRequestRestartTime,
       "tBgpPeerOperGRStatus": tBgpPeerOperGRStatus,
       "tBgpPeerOperNumRestarts": tBgpPeerOperNumRestarts,
       "tBgpPeerOperLastRestartTime": tBgpPeerOperLastRestartTime,
       "tBgpPeerOperV6ReceivedPrefixes": tBgpPeerOperV6ReceivedPrefixes,
       "tBgpPeerOperV6SentPrefixes": tBgpPeerOperV6SentPrefixes,
       "tBgpPeerOperV6ActivePrefixes": tBgpPeerOperV6ActivePrefixes,
       "tBgpPeerOperV6ReceivedPaths": tBgpPeerOperV6ReceivedPaths,
       "tBgpPeerOperV6SuppPathsDamping": tBgpPeerOperV6SuppPathsDamping,
       "tBgpPeerOperVpnReceivedPaths": tBgpPeerOperVpnReceivedPaths,
       "tBgpPeerSendOrfRouteTargetTable": tBgpPeerSendOrfRouteTargetTable,
       "tBgpPeerSendOrfRouteTargetEntry": tBgpPeerSendOrfRouteTargetEntry,
       "tBgpPeerSendOrfRouteTarget": tBgpPeerSendOrfRouteTarget,
       "tBgpPeerSendOrfRTRowStatus": tBgpPeerSendOrfRTRowStatus,
       "tBgpPeerParamsTable": tBgpPeerParamsTable,
       "tBgpPeerParamsEntry": tBgpPeerParamsEntry,
       "tBgpPeerParamsInheritance": tBgpPeerParamsInheritance,
       "tBgpPeerDisableFEFailover": tBgpPeerDisableFEFailover,
       "tBgpPeerDisableComms": tBgpPeerDisableComms,
       "tBgpPeerDisableExtComms": tBgpPeerDisableExtComms,
       "tBgpPeerDefaultOriginate": tBgpPeerDefaultOriginate,
       "tBgpPeerAdvertiseInactiveRts": tBgpPeerAdvertiseInactiveRts,
       "tBgpPeerMinTTLValue": tBgpPeerMinTTLValue,
       "tBgpPeerTTLLogId": tBgpPeerTTLLogId,
       "tBgpPeerNgTable": tBgpPeerNgTable,
       "tBgpPeerNgEntry": tBgpPeerNgEntry,
       "tBgpPeerNgInstanceIndex": tBgpPeerNgInstanceIndex,
       "tBgpPeerNgAddressType": tBgpPeerNgAddressType,
       "tBgpPeerNgAddress": tBgpPeerNgAddress,
       "tBgpPeerNgPeerGroup": tBgpPeerNgPeerGroup,
       "tBgpPeerNgRowStatus": tBgpPeerNgRowStatus,
       "tBgpPeerNgShutdown": tBgpPeerNgShutdown,
       "tBgpPeerNgDescription": tBgpPeerNgDescription,
       "tBgpPeerNgConnectRetry": tBgpPeerNgConnectRetry,
       "tBgpPeerNgHoldTime": tBgpPeerNgHoldTime,
       "tBgpPeerNgKeepAlive": tBgpPeerNgKeepAlive,
       "tBgpPeerNgMinASOrigination": tBgpPeerNgMinASOrigination,
       "tBgpPeerNgDampening": tBgpPeerNgDampening,
       "tBgpPeerNgLocalAddress": tBgpPeerNgLocalAddress,
       "tBgpPeerNgLocalAddressType": tBgpPeerNgLocalAddressType,
       "tBgpPeerNgLocalAS": tBgpPeerNgLocalAS,
       "tBgpPeerNgLocalPreference": tBgpPeerNgLocalPreference,
       "tBgpPeerNgLoopDetect": tBgpPeerNgLoopDetect,
       "tBgpPeerNgMinRouteAdvertisement": tBgpPeerNgMinRouteAdvertisement,
       "tBgpPeerNgMaxPrefix": tBgpPeerNgMaxPrefix,
       "tBgpPeerNgMEDSource": tBgpPeerNgMEDSource,
       "tBgpPeerNgMEDValue": tBgpPeerNgMEDValue,
       "tBgpPeerNgMultihop": tBgpPeerNgMultihop,
       "tBgpPeerNgNextHopSelf": tBgpPeerNgNextHopSelf,
       "tBgpPeerNgNoAggregatorID": tBgpPeerNgNoAggregatorID,
       "tBgpPeerNgPassive": tBgpPeerNgPassive,
       "tBgpPeerNgPeerAS": tBgpPeerNgPeerAS,
       "tBgpPeerNgPeerType": tBgpPeerNgPeerType,
       "tBgpPeerNgPreference": tBgpPeerNgPreference,
       "tBgpPeerNgRemovePrivateAS": tBgpPeerNgRemovePrivateAS,
       "tBgpPeerNgLastChanged": tBgpPeerNgLastChanged,
       "tBgpPeerNgInheritance": tBgpPeerNgInheritance,
       "tBgpPeerNgImportPolicy1": tBgpPeerNgImportPolicy1,
       "tBgpPeerNgImportPolicy2": tBgpPeerNgImportPolicy2,
       "tBgpPeerNgImportPolicy3": tBgpPeerNgImportPolicy3,
       "tBgpPeerNgImportPolicy4": tBgpPeerNgImportPolicy4,
       "tBgpPeerNgImportPolicy5": tBgpPeerNgImportPolicy5,
       "tBgpPeerNgExportPolicy1": tBgpPeerNgExportPolicy1,
       "tBgpPeerNgExportPolicy2": tBgpPeerNgExportPolicy2,
       "tBgpPeerNgExportPolicy3": tBgpPeerNgExportPolicy3,
       "tBgpPeerNgExportPolicy4": tBgpPeerNgExportPolicy4,
       "tBgpPeerNgExportPolicy5": tBgpPeerNgExportPolicy5,
       "tBgpPeerNgOperStatus": tBgpPeerNgOperStatus,
       "tBgpPeerNgLocalASPrivate": tBgpPeerNgLocalASPrivate,
       "tBgpPeerNgMd5Auth": tBgpPeerNgMd5Auth,
       "tBgpPeerNgMd5AuthKey": tBgpPeerNgMd5AuthKey,
       "tBgpPeerNgClusterId": tBgpPeerNgClusterId,
       "tBgpPeerNgDisableClientReflect": tBgpPeerNgDisableClientReflect,
       "tBgpPeerNgGracefulRestart": tBgpPeerNgGracefulRestart,
       "tBgpPeerNgGRRestartTime": tBgpPeerNgGRRestartTime,
       "tBgpPeerNgGRStaleRoute": tBgpPeerNgGRStaleRoute,
       "tBgpPeerNgGRAdminState": tBgpPeerNgGRAdminState,
       "tBgpPeerNgGROperState": tBgpPeerNgGROperState,
       "tBgpPeerNgFamily": tBgpPeerNgFamily,
       "tBgpPeerNgVpnRemoteFamily": tBgpPeerNgVpnRemoteFamily,
       "tBgpPeerNgVpnApplyImport": tBgpPeerNgVpnApplyImport,
       "tBgpPeerNgVpnApplyExport": tBgpPeerNgVpnApplyExport,
       "tBgpPeerNgVpnLocalCaps": tBgpPeerNgVpnLocalCaps,
       "tBgpPeerNgVpnRemoteCaps": tBgpPeerNgVpnRemoteCaps,
       "tBgpPeerNgConnState": tBgpPeerNgConnState,
       "tBgpPeerNgASOverride": tBgpPeerNgASOverride,
       "tBgpPeerNgOrf": tBgpPeerNgOrf,
       "tBgpPeerNgExtCommsOrf": tBgpPeerNgExtCommsOrf,
       "tBgpPeerNgExtCommsSendOrf": tBgpPeerNgExtCommsSendOrf,
       "tBgpPeerNgExtCommsRecvOrf": tBgpPeerNgExtCommsRecvOrf,
       "tBgpPeerNgLocalAS4Byte": tBgpPeerNgLocalAS4Byte,
       "tBgpPeerNgPeerAS4Byte": tBgpPeerNgPeerAS4Byte,
       "tBgpPeerNgDisable4ByteASN": tBgpPeerNgDisable4ByteASN,
       "tBgpPeerNgHoldTimeIsStrict": tBgpPeerNgHoldTimeIsStrict,
       "tBgpPeerNgL2vpnCiscoInterop": tBgpPeerNgL2vpnCiscoInterop,
       "tBgpPeerNgRemovePrivateASLmtd": tBgpPeerNgRemovePrivateASLmtd,
       "tBgpPeerNgMaxPrefixLogOnly": tBgpPeerNgMaxPrefixLogOnly,
       "tBgpPeerNgMaxPrefixThreshold": tBgpPeerNgMaxPrefixThreshold,
       "tBgpPeerNgDisableCapNegotiation": tBgpPeerNgDisableCapNegotiation,
       "tBgpPeerNgOperTable": tBgpPeerNgOperTable,
       "tBgpPeerNgOperEntry": tBgpPeerNgOperEntry,
       "tBgpPeerNgOperMsgOctetsRcvd": tBgpPeerNgOperMsgOctetsRcvd,
       "tBgpPeerNgOperMsgOctetsSent": tBgpPeerNgOperMsgOctetsSent,
       "tBgpPeerNgOperInputQueueMsgs": tBgpPeerNgOperInputQueueMsgs,
       "tBgpPeerNgOperOutputQueueMsgs": tBgpPeerNgOperOutputQueueMsgs,
       "tBgpPeerNgOperReceivedPrefixes": tBgpPeerNgOperReceivedPrefixes,
       "tBgpPeerNgOperSentPrefixes": tBgpPeerNgOperSentPrefixes,
       "tBgpPeerNgOperActivePrefixes": tBgpPeerNgOperActivePrefixes,
       "tBgpPeerNgOperReceivedPaths": tBgpPeerNgOperReceivedPaths,
       "tBgpPeerNgOperPathsSupByDamping": tBgpPeerNgOperPathsSupByDamping,
       "tBgpPeerNgOperFlaps": tBgpPeerNgOperFlaps,
       "tBgpPeerNgOperLastState": tBgpPeerNgOperLastState,
       "tBgpPeerNgOperLastEvent": tBgpPeerNgOperLastEvent,
       "tBgpPeerNgOperVpnRecvPrefixes": tBgpPeerNgOperVpnRecvPrefixes,
       "tBgpPeerNgOperVpnSentPrefixes": tBgpPeerNgOperVpnSentPrefixes,
       "tBgpPeerNgOperVpnActivePrefixes": tBgpPeerNgOperVpnActivePrefixes,
       "tBgpPeerNgOperGRSupport": tBgpPeerNgOperGRSupport,
       "tBgpPeerNgOperGRFamilyRestart": tBgpPeerNgOperGRFamilyRestart,
       "tBgpPeerNgOperGRFamilyFwding": tBgpPeerNgOperGRFamilyFwding,
       "tBgpPeerNgOperGRFamilyNegotiated": tBgpPeerNgOperGRFamilyNegotiated,
       "tBgpPeerNgOperGRRecvEOR": tBgpPeerNgOperGRRecvEOR,
       "tBgpPeerNgOperGRSendEOR": tBgpPeerNgOperGRSendEOR,
       "tBgpPeerNgOperGRStaleRoutesTime": tBgpPeerNgOperGRStaleRoutesTime,
       "tBgpPeerNgOperGRReqRestartTime": tBgpPeerNgOperGRReqRestartTime,
       "tBgpPeerNgOperGRStatus": tBgpPeerNgOperGRStatus,
       "tBgpPeerNgOperNumRestarts": tBgpPeerNgOperNumRestarts,
       "tBgpPeerNgOperLastRestartTime": tBgpPeerNgOperLastRestartTime,
       "tBgpPeerNgOperV6ReceivedPrefixes": tBgpPeerNgOperV6ReceivedPrefixes,
       "tBgpPeerNgOperV6SentPrefixes": tBgpPeerNgOperV6SentPrefixes,
       "tBgpPeerNgOperV6ActivePrefixes": tBgpPeerNgOperV6ActivePrefixes,
       "tBgpPeerNgOperV6ReceivedPaths": tBgpPeerNgOperV6ReceivedPaths,
       "tBgpPeerNgOperV6SuppPathsDamping": tBgpPeerNgOperV6SuppPathsDamping,
       "tBgpPeerNgOperVpnReceivedPaths": tBgpPeerNgOperVpnReceivedPaths,
       "tBgpPeerNgOperV4SuppPfxDamp": tBgpPeerNgOperV4SuppPfxDamp,
       "tBgpPeerNgOperVpnSuppPfxDamp": tBgpPeerNgOperVpnSuppPfxDamp,
       "tBgpPeerNgOperV6SuppPfxDamp": tBgpPeerNgOperV6SuppPfxDamp,
       "tBgpPeerNgOperMCastV4SuppPfxDamp": tBgpPeerNgOperMCastV4SuppPfxDamp,
       "tBgpPeerNgOperMCastV4RecvPfxs": tBgpPeerNgOperMCastV4RecvPfxs,
       "tBgpPeerNgOperMCastV4SentPfxs": tBgpPeerNgOperMCastV4SentPfxs,
       "tBgpPeerNgOperMCastV4ActivePfxs": tBgpPeerNgOperMCastV4ActivePfxs,
       "tBgpPeerNgOperVpnIpv6RecvPfxs": tBgpPeerNgOperVpnIpv6RecvPfxs,
       "tBgpPeerNgOperVpnIpv6SentPfxs": tBgpPeerNgOperVpnIpv6SentPfxs,
       "tBgpPeerNgOperVpnIpv6ActivePfxs": tBgpPeerNgOperVpnIpv6ActivePfxs,
       "tBgpPeerNgOperVpnIpv6SuppPfxDamp": tBgpPeerNgOperVpnIpv6SuppPfxDamp,
       "tBgpPeerNgOperMvpnV4SuppPfxDamp": tBgpPeerNgOperMvpnV4SuppPfxDamp,
       "tBgpPeerNgOperMvpnV4RecvPfxs": tBgpPeerNgOperMvpnV4RecvPfxs,
       "tBgpPeerNgOperMvpnV4SentPfxs": tBgpPeerNgOperMvpnV4SentPfxs,
       "tBgpPeerNgOperMvpnV4ActivePfxs": tBgpPeerNgOperMvpnV4ActivePfxs,
       "tBgpPeerNgOperl2VpnSuppPfxDamp": tBgpPeerNgOperl2VpnSuppPfxDamp,
       "tBgpPeerNgOperl2VpnRecvPfxs": tBgpPeerNgOperl2VpnRecvPfxs,
       "tBgpPeerNgOperl2VpnSentPfxs": tBgpPeerNgOperl2VpnSentPfxs,
       "tBgpPeerNgOperl2VpnActivePfxs": tBgpPeerNgOperl2VpnActivePfxs,
       "tBgpPeerNgOperMdtSafiSuppPfxDamp": tBgpPeerNgOperMdtSafiSuppPfxDamp,
       "tBgpPeerNgOperMdtSafiRecvPfxs": tBgpPeerNgOperMdtSafiRecvPfxs,
       "tBgpPeerNgOperMdtSafiSentPfxs": tBgpPeerNgOperMdtSafiSentPfxs,
       "tBgpPeerNgOperMdtSafiActivePfxs": tBgpPeerNgOperMdtSafiActivePfxs,
       "tBgpPeerNgOperMsPwSuppPfxDamp": tBgpPeerNgOperMsPwSuppPfxDamp,
       "tBgpPeerNgOperMsPwRecvPfxs": tBgpPeerNgOperMsPwRecvPfxs,
       "tBgpPeerNgOperMsPwSentPfxs": tBgpPeerNgOperMsPwSentPfxs,
       "tBgpPeerNgOperMsPwActivePfxs": tBgpPeerNgOperMsPwActivePfxs,
       "tBgpPeerNgOperFlowIpv4SupPfxDamp": tBgpPeerNgOperFlowIpv4SupPfxDamp,
       "tBgpPeerNgOperFlowIpv4RecvPfxs": tBgpPeerNgOperFlowIpv4RecvPfxs,
       "tBgpPeerNgOperFlowIpv4SentPfxs": tBgpPeerNgOperFlowIpv4SentPfxs,
       "tBgpPeerNgOperFlowIpv4ActivePfxs": tBgpPeerNgOperFlowIpv4ActivePfxs,
       "tBgpPeerNgAddPathSendRemoteCaps": tBgpPeerNgAddPathSendRemoteCaps,
       "tBgpPeerNgAddPathRecvRemoteCaps": tBgpPeerNgAddPathRecvRemoteCaps,
       "tBgpPeerNgOperBackupPrefixes": tBgpPeerNgOperBackupPrefixes,
       "tBgpPeerNgOperV6BackupPrefixes": tBgpPeerNgOperV6BackupPrefixes,
       "tBgpPeerNgOperRtTgtSuppPfxDamp": tBgpPeerNgOperRtTgtSuppPfxDamp,
       "tBgpPeerNgOperRtTgtRecvPfxs": tBgpPeerNgOperRtTgtRecvPfxs,
       "tBgpPeerNgOperRtTgtSentPfxs": tBgpPeerNgOperRtTgtSentPfxs,
       "tBgpPeerNgOperRtTgtActivePfxs": tBgpPeerNgOperRtTgtActivePfxs,
       "tBgpPeerNgOperVpnV4BackupPfxs": tBgpPeerNgOperVpnV4BackupPfxs,
       "tBgpPeerNgOperVpnV6BackupPfxs": tBgpPeerNgOperVpnV6BackupPfxs,
       "tBgpPeerNgOperMcastVpnV4RecvPfxs": tBgpPeerNgOperMcastVpnV4RecvPfxs,
       "tBgpPeerNgOperMcastVpnV4SentPfxs": tBgpPeerNgOperMcastVpnV4SentPfxs,
       "tBgpPeerNgOperMcastVpnV4ActPfxs": tBgpPeerNgOperMcastVpnV4ActPfxs,
       "tBgpPeerNgOperMvpnV6SuppPfxDamp": tBgpPeerNgOperMvpnV6SuppPfxDamp,
       "tBgpPeerNgOperMvpnV6RecvPfxs": tBgpPeerNgOperMvpnV6RecvPfxs,
       "tBgpPeerNgOperMvpnV6SentPfxs": tBgpPeerNgOperMvpnV6SentPfxs,
       "tBgpPeerNgOperMvpnV6ActivePfxs": tBgpPeerNgOperMvpnV6ActivePfxs,
       "tBgpPeerNgOperFlowIpv6SupPfxDamp": tBgpPeerNgOperFlowIpv6SupPfxDamp,
       "tBgpPeerNgOperFlowIpv6RecvPfxs": tBgpPeerNgOperFlowIpv6RecvPfxs,
       "tBgpPeerNgOperFlowIpv6SentPfxs": tBgpPeerNgOperFlowIpv6SentPfxs,
       "tBgpPeerNgOperFlowIpv6ActivePfxs": tBgpPeerNgOperFlowIpv6ActivePfxs,
       "tBgpPeerNgOperEvpnSupPfxDamp": tBgpPeerNgOperEvpnSupPfxDamp,
       "tBgpPeerNgOperEvpnRecvPfxs": tBgpPeerNgOperEvpnRecvPfxs,
       "tBgpPeerNgOperEvpnSentPfxs": tBgpPeerNgOperEvpnSentPfxs,
       "tBgpPeerNgOperEvpnActivePfxs": tBgpPeerNgOperEvpnActivePfxs,
       "tBgpPeerNgOperUpdateErrors": tBgpPeerNgOperUpdateErrors,
       "tBgpPeerNgOperGRNotifFamilyNego": tBgpPeerNgOperGRNotifFamilyNego,
       "tBgpPeerNgOperRemIdleHoldTime": tBgpPeerNgOperRemIdleHoldTime,
       "tBgpPeerNgOperMcastV6SupPfxDamp": tBgpPeerNgOperMcastV6SupPfxDamp,
       "tBgpPeerNgOperMcastV6RecvPfxs": tBgpPeerNgOperMcastV6RecvPfxs,
       "tBgpPeerNgOperMcastV6SentPfxs": tBgpPeerNgOperMcastV6SentPfxs,
       "tBgpPeerNgOperMcastV6ActivePfxs": tBgpPeerNgOperMcastV6ActivePfxs,
       "tBgpPeerNgSendOrfRouteTargetTable": tBgpPeerNgSendOrfRouteTargetTable,
       "tBgpPeerNgSendOrfRouteTargetEntry": tBgpPeerNgSendOrfRouteTargetEntry,
       "tBgpPeerNgSendOrfRouteTarget": tBgpPeerNgSendOrfRouteTarget,
       "tBgpPeerNgSendOrfRTRowStatus": tBgpPeerNgSendOrfRTRowStatus,
       "tBgpPeerNgParamsTable": tBgpPeerNgParamsTable,
       "tBgpPeerNgParamsEntry": tBgpPeerNgParamsEntry,
       "tBgpPeerNgParamsInheritance": tBgpPeerNgParamsInheritance,
       "tBgpPeerNgDisableFEFailover": tBgpPeerNgDisableFEFailover,
       "tBgpPeerNgDisableComms": tBgpPeerNgDisableComms,
       "tBgpPeerNgDisableExtComms": tBgpPeerNgDisableExtComms,
       "tBgpPeerNgDefaultOriginate": tBgpPeerNgDefaultOriginate,
       "tBgpPeerNgAdvertiseInactiveRts": tBgpPeerNgAdvertiseInactiveRts,
       "tBgpPeerNgMinTTLValue": tBgpPeerNgMinTTLValue,
       "tBgpPeerNgTracking": tBgpPeerNgTracking,
       "tBgpPeerNgAdvLabelAddrFamily": tBgpPeerNgAdvLabelAddrFamily,
       "tBgpPeerNgAuthKeyChain": tBgpPeerNgAuthKeyChain,
       "tBgpPeerNgLastError": tBgpPeerNgLastError,
       "tBgpPeerNgBfdEnabled": tBgpPeerNgBfdEnabled,
       "tBgpPeerNgPMTUDiscovery": tBgpPeerNgPMTUDiscovery,
       "tBgpPeerNgAdvertiseLdpPrefix": tBgpPeerNgAdvertiseLdpPrefix,
       "tBgpPeerNgEnableAddPath": tBgpPeerNgEnableAddPath,
       "tBgpPeerNgRecvAddPath": tBgpPeerNgRecvAddPath,
       "tBgpPeerNgIpv4AddPathLimit": tBgpPeerNgIpv4AddPathLimit,
       "tBgpPeerNgVpnIpv4AddPathLimit": tBgpPeerNgVpnIpv4AddPathLimit,
       "tBgpPeerNgIpv6AddPathLimit": tBgpPeerNgIpv6AddPathLimit,
       "tBgpPeerNgVpnIpv6AddPathLimit": tBgpPeerNgVpnIpv6AddPathLimit,
       "tBgpPeerNgFlowspecValidate": tBgpPeerNgFlowspecValidate,
       "tBgpPeerNgUpdatedErrorHandling": tBgpPeerNgUpdatedErrorHandling,
       "tBgpPeerNgDefaultRouteTarget": tBgpPeerNgDefaultRouteTarget,
       "tBgpPeerNgAigp": tBgpPeerNgAigp,
       "tBgpPeerNgMinHoldTime": tBgpPeerNgMinHoldTime,
       "tBgpPeerNgSplitHorizon": tBgpPeerNgSplitHorizon,
       "tBgpPeerNgRemPrivateSkipPeerAs": tBgpPeerNgRemPrivateSkipPeerAs,
       "tBgpPeerNgLclASNoPrependGlobalAS": tBgpPeerNgLclASNoPrependGlobalAS,
       "tBgpPeerNgMaxPrefixIdleTimeOut": tBgpPeerNgMaxPrefixIdleTimeOut,
       "tBgpPeerNgGRRestartNotification": tBgpPeerNgGRRestartNotification,
       "tBgpPeerNgFaultTolerance": tBgpPeerNgFaultTolerance,
       "tBgpPeerNgDampPeerOscillations": tBgpPeerNgDampPeerOscillations,
       "tBgpPeerNgDampOscInitialWaitTime": tBgpPeerNgDampOscInitialWaitTime,
       "tBgpPeerNgDampOscSecondWaitTime": tBgpPeerNgDampOscSecondWaitTime,
       "tBgpPeerNgDampOscMaxWaitTime": tBgpPeerNgDampOscMaxWaitTime,
       "tBgpPeerNgDampOscErrorInterval": tBgpPeerNgDampOscErrorInterval,
       "tBgpPeerNgNhUnchangedFamily": tBgpPeerNgNhUnchangedFamily,
       "tBgpPeerNgEnableOriginValidation": tBgpPeerNgEnableOriginValidation,
       "tBgpPeerNgThirdPartyNextHop": tBgpPeerNgThirdPartyNextHop,
       "tBgpPeerPlcyTable": tBgpPeerPlcyTable,
       "tBgpPeerPlcyEntry": tBgpPeerPlcyEntry,
       "tBgpPeerPlcyImportPolicy1": tBgpPeerPlcyImportPolicy1,
       "tBgpPeerPlcyImportPolicy2": tBgpPeerPlcyImportPolicy2,
       "tBgpPeerPlcyImportPolicy3": tBgpPeerPlcyImportPolicy3,
       "tBgpPeerPlcyImportPolicy4": tBgpPeerPlcyImportPolicy4,
       "tBgpPeerPlcyImportPolicy5": tBgpPeerPlcyImportPolicy5,
       "tBgpPeerPlcyImportPolicy6": tBgpPeerPlcyImportPolicy6,
       "tBgpPeerPlcyImportPolicy7": tBgpPeerPlcyImportPolicy7,
       "tBgpPeerPlcyImportPolicy8": tBgpPeerPlcyImportPolicy8,
       "tBgpPeerPlcyImportPolicy9": tBgpPeerPlcyImportPolicy9,
       "tBgpPeerPlcyImportPolicy10": tBgpPeerPlcyImportPolicy10,
       "tBgpPeerPlcyImportPolicy11": tBgpPeerPlcyImportPolicy11,
       "tBgpPeerPlcyImportPolicy12": tBgpPeerPlcyImportPolicy12,
       "tBgpPeerPlcyImportPolicy13": tBgpPeerPlcyImportPolicy13,
       "tBgpPeerPlcyImportPolicy14": tBgpPeerPlcyImportPolicy14,
       "tBgpPeerPlcyImportPolicy15": tBgpPeerPlcyImportPolicy15,
       "tBgpPeerPlcyExportPolicy1": tBgpPeerPlcyExportPolicy1,
       "tBgpPeerPlcyExportPolicy2": tBgpPeerPlcyExportPolicy2,
       "tBgpPeerPlcyExportPolicy3": tBgpPeerPlcyExportPolicy3,
       "tBgpPeerPlcyExportPolicy4": tBgpPeerPlcyExportPolicy4,
       "tBgpPeerPlcyExportPolicy5": tBgpPeerPlcyExportPolicy5,
       "tBgpPeerPlcyExportPolicy6": tBgpPeerPlcyExportPolicy6,
       "tBgpPeerPlcyExportPolicy7": tBgpPeerPlcyExportPolicy7,
       "tBgpPeerPlcyExportPolicy8": tBgpPeerPlcyExportPolicy8,
       "tBgpPeerPlcyExportPolicy9": tBgpPeerPlcyExportPolicy9,
       "tBgpPeerPlcyExportPolicy10": tBgpPeerPlcyExportPolicy10,
       "tBgpPeerPlcyExportPolicy11": tBgpPeerPlcyExportPolicy11,
       "tBgpPeerPlcyExportPolicy12": tBgpPeerPlcyExportPolicy12,
       "tBgpPeerPlcyExportPolicy13": tBgpPeerPlcyExportPolicy13,
       "tBgpPeerPlcyExportPolicy14": tBgpPeerPlcyExportPolicy14,
       "tBgpPeerPlcyExportPolicy15": tBgpPeerPlcyExportPolicy15,
       "tBgpInstanceConfederationObjects": tBgpInstanceConfederationObjects,
       "tBgpConfederationTableLastChanged": tBgpConfederationTableLastChanged,
       "tBgpConfederationTable": tBgpConfederationTable,
       "tBgpConfederationEntry": tBgpConfederationEntry,
       "tBgpConfederationAS": tBgpConfederationAS,
       "tBgpConfederationMemberAS": tBgpConfederationMemberAS,
       "tBgpConfederationRowStatus": tBgpConfederationRowStatus,
       "tBgpConfederation4BytTblLstChngd": tBgpConfederation4BytTblLstChngd,
       "tBgpConfederation4ByteTable": tBgpConfederation4ByteTable,
       "tBgpConfederation4ByteEntry": tBgpConfederation4ByteEntry,
       "tBgpConfederation4ByteAS": tBgpConfederation4ByteAS,
       "tBgpConfederation4ByteMemberAS": tBgpConfederation4ByteMemberAS,
       "tBgpConfederation4ByteRowStatus": tBgpConfederation4ByteRowStatus,
       "tBgpPeeringPolicyObjects": tBgpPeeringPolicyObjects,
       "tBgpPeeringPolicyTableLastChngd": tBgpPeeringPolicyTableLastChngd,
       "tBgpPeeringPolicyTable": tBgpPeeringPolicyTable,
       "tBgpPeeringPolicyEntry": tBgpPeeringPolicyEntry,
       "tBgpPeeringPolicyName": tBgpPeeringPolicyName,
       "tBgpPrngPlcyRowStatus": tBgpPrngPlcyRowStatus,
       "tBgpPrngPlcyLastChngd": tBgpPrngPlcyLastChngd,
       "tBgpPrngPlcyDescription": tBgpPrngPlcyDescription,
       "tBgpPrngPlcyInheritance": tBgpPrngPlcyInheritance,
       "tBgpPrngPlcyAdvertiseInactiveRts": tBgpPrngPlcyAdvertiseInactiveRts,
       "tBgpPrngPlcyNoAggregatorID": tBgpPrngPlcyNoAggregatorID,
       "tBgpPrngPlcyASOverride": tBgpPrngPlcyASOverride,
       "tBgpPrngPlcyAuthKeyChain": tBgpPrngPlcyAuthKeyChain,
       "tBgpPrngPlcyMd5Auth": tBgpPrngPlcyMd5Auth,
       "tBgpPrngPlcyMd5AuthKey": tBgpPrngPlcyMd5AuthKey,
       "tBgpPrngPlcyClusterId": tBgpPrngPlcyClusterId,
       "tBgpPrngPlcyConnectRetry": tBgpPrngPlcyConnectRetry,
       "tBgpPrngPlcyDampening": tBgpPrngPlcyDampening,
       "tBgpPrngPlcyDisableClientReflect": tBgpPrngPlcyDisableClientReflect,
       "tBgpPrngPlcyDisableComms": tBgpPrngPlcyDisableComms,
       "tBgpPrngPlcyDisableExtComms": tBgpPrngPlcyDisableExtComms,
       "tBgpPrngPlcyDisableFEFailover": tBgpPrngPlcyDisableFEFailover,
       "tBgpPrngPlcyImportPolicy1": tBgpPrngPlcyImportPolicy1,
       "tBgpPrngPlcyImportPolicy2": tBgpPrngPlcyImportPolicy2,
       "tBgpPrngPlcyImportPolicy3": tBgpPrngPlcyImportPolicy3,
       "tBgpPrngPlcyImportPolicy4": tBgpPrngPlcyImportPolicy4,
       "tBgpPrngPlcyImportPolicy5": tBgpPrngPlcyImportPolicy5,
       "tBgpPrngPlcyExportPolicy1": tBgpPrngPlcyExportPolicy1,
       "tBgpPrngPlcyExportPolicy2": tBgpPrngPlcyExportPolicy2,
       "tBgpPrngPlcyExportPolicy3": tBgpPrngPlcyExportPolicy3,
       "tBgpPrngPlcyExportPolicy4": tBgpPrngPlcyExportPolicy4,
       "tBgpPrngPlcyExportPolicy5": tBgpPrngPlcyExportPolicy5,
       "tBgpPrngPlcyHoldTime": tBgpPrngPlcyHoldTime,
       "tBgpPrngPlcyKeepAlive": tBgpPrngPlcyKeepAlive,
       "tBgpPrngPlcyLocalAddressType": tBgpPrngPlcyLocalAddressType,
       "tBgpPrngPlcyLocalAddress": tBgpPrngPlcyLocalAddress,
       "tBgpPrngPlcyLocalAS": tBgpPrngPlcyLocalAS,
       "tBgpPrngPlcyLocalASPrivate": tBgpPrngPlcyLocalASPrivate,
       "tBgpPrngPlcyLocalPreference": tBgpPrngPlcyLocalPreference,
       "tBgpPrngPlcyLoopDetect": tBgpPrngPlcyLoopDetect,
       "tBgpPrngPlcyMEDSource": tBgpPrngPlcyMEDSource,
       "tBgpPrngPlcyMEDValue": tBgpPrngPlcyMEDValue,
       "tBgpPrngPlcyMinASOrigination": tBgpPrngPlcyMinASOrigination,
       "tBgpPrngPlcyMinRteAdvertisement": tBgpPrngPlcyMinRteAdvertisement,
       "tBgpPrngPlcyMultihop": tBgpPrngPlcyMultihop,
       "tBgpPrngPlcyNextHopSelf": tBgpPrngPlcyNextHopSelf,
       "tBgpPrngPlcyPassive": tBgpPrngPlcyPassive,
       "tBgpPrngPlcyPeerAS": tBgpPrngPlcyPeerAS,
       "tBgpPrngPlcyPreference": tBgpPrngPlcyPreference,
       "tBgpPrngPlcyMaxPrefix": tBgpPrngPlcyMaxPrefix,
       "tBgpPrngPlcyRemovePrivateAS": tBgpPrngPlcyRemovePrivateAS,
       "tBgpPrngPlcyMinTTLValue": tBgpPrngPlcyMinTTLValue,
       "tBgpPrngPlcyPeerType": tBgpPrngPlcyPeerType,
       "tBgpPrngPlcyDisable4ByteASN": tBgpPrngPlcyDisable4ByteASN,
       "tBgpPrngPlcyRemovePrivateASLmtd": tBgpPrngPlcyRemovePrivateASLmtd,
       "tBgpPrngPlcyMaxPrefixLogOnly": tBgpPrngPlcyMaxPrefixLogOnly,
       "tBgpPrngPlcyMaxPrefixThreshold": tBgpPrngPlcyMaxPrefixThreshold,
       "tBgpPeeringPlcyTable": tBgpPeeringPlcyTable,
       "tBgpPeeringPlcyEntry": tBgpPeeringPlcyEntry,
       "tBgpPeeringPlcyImportPolicy1": tBgpPeeringPlcyImportPolicy1,
       "tBgpPeeringPlcyImportPolicy2": tBgpPeeringPlcyImportPolicy2,
       "tBgpPeeringPlcyImportPolicy3": tBgpPeeringPlcyImportPolicy3,
       "tBgpPeeringPlcyImportPolicy4": tBgpPeeringPlcyImportPolicy4,
       "tBgpPeeringPlcyImportPolicy5": tBgpPeeringPlcyImportPolicy5,
       "tBgpPeeringPlcyImportPolicy6": tBgpPeeringPlcyImportPolicy6,
       "tBgpPeeringPlcyImportPolicy7": tBgpPeeringPlcyImportPolicy7,
       "tBgpPeeringPlcyImportPolicy8": tBgpPeeringPlcyImportPolicy8,
       "tBgpPeeringPlcyImportPolicy9": tBgpPeeringPlcyImportPolicy9,
       "tBgpPeeringPlcyImportPolicy10": tBgpPeeringPlcyImportPolicy10,
       "tBgpPeeringPlcyImportPolicy11": tBgpPeeringPlcyImportPolicy11,
       "tBgpPeeringPlcyImportPolicy12": tBgpPeeringPlcyImportPolicy12,
       "tBgpPeeringPlcyImportPolicy13": tBgpPeeringPlcyImportPolicy13,
       "tBgpPeeringPlcyImportPolicy14": tBgpPeeringPlcyImportPolicy14,
       "tBgpPeeringPlcyImportPolicy15": tBgpPeeringPlcyImportPolicy15,
       "tBgpPeeringPlcyExportPolicy1": tBgpPeeringPlcyExportPolicy1,
       "tBgpPeeringPlcyExportPolicy2": tBgpPeeringPlcyExportPolicy2,
       "tBgpPeeringPlcyExportPolicy3": tBgpPeeringPlcyExportPolicy3,
       "tBgpPeeringPlcyExportPolicy4": tBgpPeeringPlcyExportPolicy4,
       "tBgpPeeringPlcyExportPolicy5": tBgpPeeringPlcyExportPolicy5,
       "tBgpPeeringPlcyExportPolicy6": tBgpPeeringPlcyExportPolicy6,
       "tBgpPeeringPlcyExportPolicy7": tBgpPeeringPlcyExportPolicy7,
       "tBgpPeeringPlcyExportPolicy8": tBgpPeeringPlcyExportPolicy8,
       "tBgpPeeringPlcyExportPolicy9": tBgpPeeringPlcyExportPolicy9,
       "tBgpPeeringPlcyExportPolicy10": tBgpPeeringPlcyExportPolicy10,
       "tBgpPeeringPlcyExportPolicy11": tBgpPeeringPlcyExportPolicy11,
       "tBgpPeeringPlcyExportPolicy12": tBgpPeeringPlcyExportPolicy12,
       "tBgpPeeringPlcyExportPolicy13": tBgpPeeringPlcyExportPolicy13,
       "tBgpPeeringPlcyExportPolicy14": tBgpPeeringPlcyExportPolicy14,
       "tBgpPeeringPlcyExportPolicy15": tBgpPeeringPlcyExportPolicy15,
       "tBgpNotificationObjs": tBgpNotificationObjs,
       "tBgpPeerNgAddrType": tBgpPeerNgAddrType,
       "tBgpPeerNgAddr": tBgpPeerNgAddr,
       "tBgpFlowspecExtCommunityAction": tBgpFlowspecExtCommunityAction,
       "tBgpPeerFlowRouteDestAddrType": tBgpPeerFlowRouteDestAddrType,
       "tBgpPeerFlowRouteDestAddr": tBgpPeerFlowRouteDestAddr,
       "tBgpFlowRouteInvalidReason": tBgpFlowRouteInvalidReason,
       "tBgpFlowRouteNLRI": tBgpFlowRouteNLRI,
       "tBgpFlowspecExtCommActionValue": tBgpFlowspecExtCommActionValue,
       "tBgp4OptTransPathAttrType": tBgp4OptTransPathAttrType,
       "tBgp4OptTransPathAttrLength": tBgp4OptTransPathAttrLength,
       "tBgp4OptTransPathAttribute": tBgp4OptTransPathAttribute,
       "tBgp4OTWithdrawnRouteLength": tBgp4OTWithdrawnRouteLength,
       "tBgp4OTWithdrawnRoutePrefix": tBgp4OTWithdrawnRoutePrefix,
       "tBgpRouteInvalidReason": tBgpRouteInvalidReason,
       "tBgpRouteNLRI": tBgpRouteNLRI,
       "tBgp4PathAttrType": tBgp4PathAttrType,
       "tBgp4PathAttrLength": tBgp4PathAttrLength,
       "tBgp4PathAttribute": tBgp4PathAttribute,
       "tBgp4WithdrawnRoutePrefix": tBgp4WithdrawnRoutePrefix,
       "tBgp4UpdateMessage": tBgp4UpdateMessage,
       "tBgp4BadErrorMessage": tBgp4BadErrorMessage,
       "tBgp4BadErrorMessageType": tBgp4BadErrorMessageType,
       "tBgpNotificationsPrefix": tBgpNotificationsPrefix,
       "tBgpNotifications": tBgpNotifications,
       "tBgpMaxPrefix90": tBgpMaxPrefix90,
       "tBgpMaxPrefix100": tBgpMaxPrefix100,
       "tBgpPeerGRStatusChange": tBgpPeerGRStatusChange,
       "tBgpMaxNgPrefix90": tBgpMaxNgPrefix90,
       "tBgpMaxNgPrefix100": tBgpMaxNgPrefix100,
       "tBgpPeerNgGRStatusChange": tBgpPeerNgGRStatusChange,
       "tBgpNgEstablished": tBgpNgEstablished,
       "tBgpNgBackwardTransition": tBgpNgBackwardTransition,
       "tBgpPeerNgHoldTimeInconsistent": tBgpPeerNgHoldTimeInconsistent,
       "tBgpFlowspecUnsupportdComAction": tBgpFlowspecUnsupportdComAction,
       "tBgpFlowRouteInvalid": tBgpFlowRouteInvalid,
       "tBgpMaxNgPrefixThreshReached": tBgpMaxNgPrefixThreshReached,
       "tBgp4OptTransPathAttrInvalid": tBgp4OptTransPathAttrInvalid,
       "tBgp4OptTransWithdrawnRoutes": tBgp4OptTransWithdrawnRoutes,
       "tBgp4RouteInvalid": tBgp4RouteInvalid,
       "tBgp4PathAttrInvalid": tBgp4PathAttrInvalid,
       "tBgp4WithdrawnRtFromUpdateError": tBgp4WithdrawnRtFromUpdateError,
       "tBgp4UpdateInvalid": tBgp4UpdateInvalid,
       "tBgpReceivedInvalidNlri": tBgpReceivedInvalidNlri}
)
