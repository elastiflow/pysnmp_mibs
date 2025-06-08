# SNMP MIB module (TN-OAM-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-OAM-TEST-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:44 2025
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

(Dot1agCfmMepIdOrZero,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(SdpId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "SdpId")

(TFCName,
 TItemDescription,
 TProfile,
 TmnxAdminState,
 TmnxServId,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TFCName",
    "TItemDescription",
    "TProfile",
    "TmnxAdminState",
    "TmnxServId",
    "TmnxVRtrID")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnOamTestMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 11)
)
if mibBuilder.loadTexts:
    tnOamTestMIBModule.setRevisions(
        ("1913-08-22 00:00",
         "1913-03-26 00:00",
         "1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-09 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-11-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOamTestMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 0),
          ("ping", 1),
          ("traceroute", 2))
    )



class TmnxOamPingRtnCode(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("fecEgress", 1),
          ("fecNoMap", 2),
          ("notDownstream", 3),
          ("downstream", 4),
          ("downstreamNotLabel", 5),
          ("downstreamNotMac", 6),
          ("downstreamNotMacFlood", 7),
          ("malformedEchoRequest", 8),
          ("tlvNotUnderstood", 9),
          ("downstreamNotInMfib", 10),
          ("downstreamMismatched", 11),
          ("upstreamIfIdUnkn", 12),
          ("noMplsFwd", 13),
          ("noLabelAtStackDepth", 14),
          ("protoIntfMismatched", 15),
          ("terminatedByOneLabel", 16))
    )



class TmnxOamAddressType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4Address", 1),
          ("ipv6Address", 2),
          ("macAddress", 3),
          ("sapId", 4),
          ("sdpId", 5),
          ("localCpu", 6),
          ("ipv4Unnumbered", 7),
          ("ipv6Unnumbered", 8))
    )



class TmnxOamResponseStatus(TextualConvention, Integer32):
    status = "current"
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133)
        )
    )
    namedValues = NamedValues(
        *(("responseReceived", 1),
          ("unknown", 2),
          ("internalError", 3),
          ("maxConcurrentLimitReached", 4),
          ("requestTimedOut", 5),
          ("unknownOrigSdpId", 6),
          ("downOrigSdpId", 7),
          ("requestTerminated", 8),
          ("invalidOriginatorId", 9),
          ("invalidResponderId", 10),
          ("unknownRespSdpId", 11),
          ("downRespSdpId", 12),
          ("invalidServiceId", 13),
          ("invalidSdp", 14),
          ("downServiceSdp", 15),
          ("noServiceEgressLabel", 16),
          ("invalidHostAddress", 17),
          ("invalidMacAddress", 18),
          ("invalidLspName", 19),
          ("macIsLocal", 20),
          ("farEndUnreachable", 21),
          ("downOriginatorId", 22),
          ("downResponderId", 23),
          ("changedResponderId", 24),
          ("downOrigSvcId", 25),
          ("downRespSvcId", 26),
          ("noServiceIngressLabel", 27),
          ("mismatchCustId", 28),
          ("mismatchSvcType", 29),
          ("mismatchSvcMtu", 30),
          ("mismatchSvcLabel", 31),
          ("noSdpBoundToSvc", 32),
          ("downOrigSdpBinding", 33),
          ("invalidLspPathName", 34),
          ("noLspEndpointAddr", 35),
          ("invalidLspId", 36),
          ("downLspPath", 37),
          ("invalidLspProtocol", 38),
          ("invalidLspLabel", 39),
          ("routeIsLocal", 40),
          ("noRouteToDest", 41),
          ("localExtranetRoute", 42),
          ("srcIpInBgpVpnRoute", 43),
          ("srcIpInvalid", 44),
          ("bgpDaemonBusy", 45),
          ("mcastNotEnabled", 46),
          ("mTraceNoSGFlow", 47),
          ("mTraceSysIpNotCfg", 48),
          ("noFwdEntryInMfib", 49),
          ("dnsNameNotFound", 50),
          ("noSocket", 51),
          ("socketOptVprnIdFail", 52),
          ("socketOptIfInexFail", 53),
          ("socketOptNextHopFail", 54),
          ("socketOptMtuDiscFail", 55),
          ("socketOptSndbufFail", 56),
          ("socketOptHdrincFail", 57),
          ("socketOptTosFail", 58),
          ("socketOptTtlFail", 59),
          ("bindSocketFail", 60),
          ("noRouteByIntf", 61),
          ("noIntf", 62),
          ("noLocalIp", 63),
          ("sendtoFail", 64),
          ("rcvdWrongType", 65),
          ("noDirectInterface", 66),
          ("nexthopUnreachable", 67),
          ("socketOptHwTimeStampFail", 68),
          ("noSpokeSdpInVll", 69),
          ("farEndVccvNotSupported", 70),
          ("noVcEgressLabel", 71),
          ("socketOptIpSessionFail", 72),
          ("rcvdWrongSize", 73),
          ("dnsLookupFail", 74),
          ("noIpv6SrcAddrOnIntf", 75),
          ("multipathNotSupported", 76),
          ("nhIntfNameNotFound", 77),
          ("msPwInvalidReplyMode", 78),
          ("ancpNoAncpString", 79),
          ("ancpNoSubscriber", 80),
          ("ancpNoAncpStringForSubscriber", 81),
          ("ancpNoAccessNodeforAncpString", 82),
          ("ancpNoAncpCapabilityNegotiated", 83),
          ("ancpOtherTestInProgress", 84),
          ("ancpMaxNbrAncpTestsInProgress", 85),
          ("spokeSdpOperDown", 86),
          ("noMsPwVccvInReplyDir", 87),
          ("p2mpLspNameOrInstInvalid", 88),
          ("p2mpLspS2LPathDown", 89),
          ("p2mpLspS2LAddressInvalid", 90),
          ("p2mpLspNotOperational", 91),
          ("p2mpLspTrMultipleReplies", 92),
          ("invalidMepId", 93),
          ("multipleReplies", 94),
          ("packetSizeTooBig", 95),
          ("gtpPingError", 96),
          ("gtpPingRsrcUnavailable", 97),
          ("gtpPingDupRequest", 98),
          ("gtpPingCleanUpInProg", 99),
          ("invalidInterface", 100),
          ("p2mpLspNotFound", 101),
          ("ethCfmSlmInLoss", 102),
          ("ethCfmSlmOutLoss", 103),
          ("ethCfmSlmUnacknowledged", 104),
          ("spokeSdpFecNoBndFound", 105),
          ("mtraceNotSupportedP2mp", 106),
          ("useFec129Parameters", 107),
          ("dnsServerUnexpectedResponse", 108),
          ("dnsServerResponseFormErr", 109),
          ("dnsServerResponseServFail", 110),
          ("dnsServerResponseNotImp", 111),
          ("dnsServerResponseRefused", 112),
          ("sendFailUndefinedServiceId", 113),
          ("sendFailWrongServiceType", 114),
          ("sendFailSubnettedService", 115),
          ("invalidRespServiceId", 116),
          ("adminDownOrigSdpBind", 117),
          ("operDownRespSdpBind", 118),
          ("adminDownRespSdpBind", 119),
          ("sdpBindVcidMismatch", 120),
          ("sdpBindTypeMismatch", 121),
          ("sdpBindVcTypeMismatch", 122),
          ("sdpBindVlanVcTagMismatch", 123),
          ("adminDownOrigSvc", 124),
          ("adminDownRespSvc", 125),
          ("adminDownOrigSdpId", 126),
          ("adminDownRespSdpId", 127),
          ("mTraceSourceIsNotRemote", 128),
          ("invalidVirtualRouterId", 129),
          ("ldpPrefixIsLocal", 130),
          ("sourceIpIsNotLocal", 131),
          ("nextHopIpIsLocal", 132),
          ("targetIpIsLocal", 133))
    )



class TmnxOamSignalProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("static", 1),
          ("bgp", 2),
          ("ldp", 3),
          ("rsvpTe", 4),
          ("crLdp", 5))
    )



class TmnxOamTestResponsePlane(TextualConvention, Integer32):
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
        *(("controlPlane", 1),
          ("dataPlane", 2),
          ("none", 3))
    )



class TmnxOamSaaThreshold(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noThreshold", 0),
          ("inJitter", 1),
          ("outJitter", 2),
          ("rtJitter", 3),
          ("inLoss", 4),
          ("outLoss", 5),
          ("rtLoss", 6),
          ("inLatency", 7),
          ("outLatency", 8),
          ("rtLatency", 9))
    )



class TmnxOamVcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("meshSdp", 5),
          ("spokeSdp", 11))
    )



class TmnxOamLTtraceDisStatusBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("timeout", 0),
          ("maxPath", 1),
          ("maxHop", 2),
          ("unexploredPath", 3),
          ("noResource", 4))
    )


class TmnxOamTestResult(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undetermined", 0),
          ("success", 1),
          ("failed", 2),
          ("aborted", 3),
          ("txResourcesUnavail", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TnOamTestObjs_ObjectIdentity = ObjectIdentity
tnOamTestObjs = _TnOamTestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11)
)
_TnOamPingObjs_ObjectIdentity = ObjectIdentity
tnOamPingObjs = _TnOamPingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1)
)
_TnOamPingCtlAttributeTotal_Type = Integer32
_TnOamPingCtlAttributeTotal_Object = MibScalar
tnOamPingCtlAttributeTotal = _TnOamPingCtlAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 3),
    _TnOamPingCtlAttributeTotal_Type()
)
tnOamPingCtlAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlAttributeTotal.setStatus("current")
_TnOamPingCtlTable_Object = MibTable
tnOamPingCtlTable = _TnOamPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4)
)
if mibBuilder.loadTexts:
    tnOamPingCtlTable.setStatus("current")
_TnOamPingCtlEntry_Object = MibTableRow
tnOamPingCtlEntry = _TnOamPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1)
)
tnOamPingCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamPingCtlEntry.setStatus("current")


class _TnOamPingCtlTestIndex_Type(SnmpAdminString):
    """Custom type tnOamPingCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnOamPingCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TnOamPingCtlTestIndex_Object = MibTableColumn
tnOamPingCtlTestIndex = _TnOamPingCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 1),
    _TnOamPingCtlTestIndex_Type()
)
tnOamPingCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamPingCtlTestIndex.setStatus("current")
_TnOamPingCtlRowStatus_Type = RowStatus
_TnOamPingCtlRowStatus_Object = MibTableColumn
tnOamPingCtlRowStatus = _TnOamPingCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 2),
    _TnOamPingCtlRowStatus_Type()
)
tnOamPingCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlRowStatus.setStatus("current")


class _TnOamPingCtlStorageType_Type(StorageType):
    """Custom type tnOamPingCtlStorageType based on StorageType"""
    defaultValue = 2


_TnOamPingCtlStorageType_Type.__name__ = "StorageType"
_TnOamPingCtlStorageType_Object = MibTableColumn
tnOamPingCtlStorageType = _TnOamPingCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 3),
    _TnOamPingCtlStorageType_Type()
)
tnOamPingCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlStorageType.setStatus("current")


class _TnOamPingCtlDescr_Type(SnmpAdminString):
    """Custom type tnOamPingCtlDescr based on SnmpAdminString"""
    defaultHexValue = ""


_TnOamPingCtlDescr_Type.__name__ = "SnmpAdminString"
_TnOamPingCtlDescr_Object = MibTableColumn
tnOamPingCtlDescr = _TnOamPingCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 4),
    _TnOamPingCtlDescr_Type()
)
tnOamPingCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlDescr.setStatus("current")


class _TnOamPingCtlTestMode_Type(Integer32):
    """Custom type tnOamPingCtlTestMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sdpPing", 1),
          ("mtuPing", 2),
          ("svcPing", 3),
          ("macPing", 5),
          ("macPopulate", 6),
          ("macPurge", 7),
          ("lspPing", 8),
          ("vprnPing", 9),
          ("atmPing", 10),
          ("mfibPing", 11),
          ("cpePing", 12),
          ("mrInfo", 13),
          ("vccvPing", 14),
          ("icmpPing", 15),
          ("dnsPing", 16),
          ("ancpLoopback", 17),
          ("p2mpLspPing", 18),
          ("ethCfmLoopback", 19),
          ("ethCfmTwoWayDelay", 20),
          ("mobGtpPing", 21),
          ("ethCfmTwoWaySlm", 22),
          ("ethCfmTwoWayLm", 23))
    )


_TnOamPingCtlTestMode_Type.__name__ = "Integer32"
_TnOamPingCtlTestMode_Object = MibTableColumn
tnOamPingCtlTestMode = _TnOamPingCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 5),
    _TnOamPingCtlTestMode_Type()
)
tnOamPingCtlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTestMode.setStatus("current")


class _TnOamPingCtlAdminStatus_Type(Integer32):
    """Custom type tnOamPingCtlAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnOamPingCtlAdminStatus_Type.__name__ = "Integer32"
_TnOamPingCtlAdminStatus_Object = MibTableColumn
tnOamPingCtlAdminStatus = _TnOamPingCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 6),
    _TnOamPingCtlAdminStatus_Type()
)
tnOamPingCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlAdminStatus.setStatus("current")


class _TnOamPingCtlOrigSdpId_Type(SdpId):
    """Custom type tnOamPingCtlOrigSdpId based on SdpId"""
    defaultValue = 0


_TnOamPingCtlOrigSdpId_Type.__name__ = "SdpId"
_TnOamPingCtlOrigSdpId_Object = MibTableColumn
tnOamPingCtlOrigSdpId = _TnOamPingCtlOrigSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 7),
    _TnOamPingCtlOrigSdpId_Type()
)
tnOamPingCtlOrigSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlOrigSdpId.setStatus("current")


class _TnOamPingCtlRespSdpId_Type(SdpId):
    """Custom type tnOamPingCtlRespSdpId based on SdpId"""
    defaultValue = 0


_TnOamPingCtlRespSdpId_Type.__name__ = "SdpId"
_TnOamPingCtlRespSdpId_Object = MibTableColumn
tnOamPingCtlRespSdpId = _TnOamPingCtlRespSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 8),
    _TnOamPingCtlRespSdpId_Type()
)
tnOamPingCtlRespSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlRespSdpId.setStatus("current")


class _TnOamPingCtlFcName_Type(TFCName):
    """Custom type tnOamPingCtlFcName based on TFCName"""
    defaultValue = OctetString("be")


_TnOamPingCtlFcName_Type.__name__ = "TFCName"
_TnOamPingCtlFcName_Object = MibTableColumn
tnOamPingCtlFcName = _TnOamPingCtlFcName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 9),
    _TnOamPingCtlFcName_Type()
)
tnOamPingCtlFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlFcName.setStatus("current")


class _TnOamPingCtlProfile_Type(TProfile):
    """Custom type tnOamPingCtlProfile based on TProfile"""
    defaultValue = 2


_TnOamPingCtlProfile_Type.__name__ = "TProfile"
_TnOamPingCtlProfile_Object = MibTableColumn
tnOamPingCtlProfile = _TnOamPingCtlProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 10),
    _TnOamPingCtlProfile_Type()
)
tnOamPingCtlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlProfile.setStatus("current")


class _TnOamPingCtlMtuStartSize_Type(Unsigned32):
    """Custom type tnOamPingCtlMtuStartSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9198),
    )


_TnOamPingCtlMtuStartSize_Type.__name__ = "Unsigned32"
_TnOamPingCtlMtuStartSize_Object = MibTableColumn
tnOamPingCtlMtuStartSize = _TnOamPingCtlMtuStartSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 11),
    _TnOamPingCtlMtuStartSize_Type()
)
tnOamPingCtlMtuStartSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuStartSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuStartSize.setUnits("Octets")


class _TnOamPingCtlMtuEndSize_Type(Unsigned32):
    """Custom type tnOamPingCtlMtuEndSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9198),
    )


_TnOamPingCtlMtuEndSize_Type.__name__ = "Unsigned32"
_TnOamPingCtlMtuEndSize_Object = MibTableColumn
tnOamPingCtlMtuEndSize = _TnOamPingCtlMtuEndSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 12),
    _TnOamPingCtlMtuEndSize_Type()
)
tnOamPingCtlMtuEndSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuEndSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuEndSize.setUnits("Octets")


class _TnOamPingCtlMtuStepSize_Type(Unsigned32):
    """Custom type tnOamPingCtlMtuStepSize based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_TnOamPingCtlMtuStepSize_Type.__name__ = "Unsigned32"
_TnOamPingCtlMtuStepSize_Object = MibTableColumn
tnOamPingCtlMtuStepSize = _TnOamPingCtlMtuStepSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 13),
    _TnOamPingCtlMtuStepSize_Type()
)
tnOamPingCtlMtuStepSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuStepSize.setUnits("Octets")


class _TnOamPingCtlTargetIpAddress_Type(IpAddress):
    """Custom type tnOamPingCtlTargetIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnOamPingCtlTargetIpAddress_Type.__name__ = "IpAddress"
_TnOamPingCtlTargetIpAddress_Object = MibTableColumn
tnOamPingCtlTargetIpAddress = _TnOamPingCtlTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 14),
    _TnOamPingCtlTargetIpAddress_Type()
)
tnOamPingCtlTargetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTargetIpAddress.setStatus("obsolete")


class _TnOamPingCtlServiceId_Type(TmnxServId):
    """Custom type tnOamPingCtlServiceId based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnOamPingCtlServiceId_Type.__name__ = "TmnxServId"
_TnOamPingCtlServiceId_Object = MibTableColumn
tnOamPingCtlServiceId = _TnOamPingCtlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 15),
    _TnOamPingCtlServiceId_Type()
)
tnOamPingCtlServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlServiceId.setStatus("current")


class _TnOamPingCtlLocalSdp_Type(TruthValue):
    """Custom type tnOamPingCtlLocalSdp based on TruthValue"""
    defaultValue = 2


_TnOamPingCtlLocalSdp_Type.__name__ = "TruthValue"
_TnOamPingCtlLocalSdp_Object = MibTableColumn
tnOamPingCtlLocalSdp = _TnOamPingCtlLocalSdp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 16),
    _TnOamPingCtlLocalSdp_Type()
)
tnOamPingCtlLocalSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlLocalSdp.setStatus("current")


class _TnOamPingCtlRemoteSdp_Type(TruthValue):
    """Custom type tnOamPingCtlRemoteSdp based on TruthValue"""
    defaultValue = 2


_TnOamPingCtlRemoteSdp_Type.__name__ = "TruthValue"
_TnOamPingCtlRemoteSdp_Object = MibTableColumn
tnOamPingCtlRemoteSdp = _TnOamPingCtlRemoteSdp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 17),
    _TnOamPingCtlRemoteSdp_Type()
)
tnOamPingCtlRemoteSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlRemoteSdp.setStatus("current")


class _TnOamPingCtlSize_Type(Unsigned32):
    """Custom type tnOamPingCtlSize based on Unsigned32"""
    defaultValue = 72

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_TnOamPingCtlSize_Type.__name__ = "Unsigned32"
_TnOamPingCtlSize_Object = MibTableColumn
tnOamPingCtlSize = _TnOamPingCtlSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 18),
    _TnOamPingCtlSize_Type()
)
tnOamPingCtlSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlSize.setUnits("octets")


class _TnOamPingCtlTimeOut_Type(Unsigned32):
    """Custom type tnOamPingCtlTimeOut based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120000),
    )


_TnOamPingCtlTimeOut_Type.__name__ = "Unsigned32"
_TnOamPingCtlTimeOut_Object = MibTableColumn
tnOamPingCtlTimeOut = _TnOamPingCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 19),
    _TnOamPingCtlTimeOut_Type()
)
tnOamPingCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlTimeOut.setUnits("milliseconds")


class _TnOamPingCtlProbeCount_Type(Unsigned32):
    """Custom type tnOamPingCtlProbeCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TnOamPingCtlProbeCount_Type.__name__ = "Unsigned32"
_TnOamPingCtlProbeCount_Object = MibTableColumn
tnOamPingCtlProbeCount = _TnOamPingCtlProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 20),
    _TnOamPingCtlProbeCount_Type()
)
tnOamPingCtlProbeCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlProbeCount.setUnits("probes")


class _TnOamPingCtlInterval_Type(Unsigned32):
    """Custom type tnOamPingCtlInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90000),
    )


_TnOamPingCtlInterval_Type.__name__ = "Unsigned32"
_TnOamPingCtlInterval_Object = MibTableColumn
tnOamPingCtlInterval = _TnOamPingCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 21),
    _TnOamPingCtlInterval_Type()
)
tnOamPingCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlInterval.setUnits("milliseconds")


class _TnOamPingCtlMaxRows_Type(Unsigned32):
    """Custom type tnOamPingCtlMaxRows based on Unsigned32"""
    defaultValue = 300


_TnOamPingCtlMaxRows_Type.__name__ = "Unsigned32"
_TnOamPingCtlMaxRows_Object = MibTableColumn
tnOamPingCtlMaxRows = _TnOamPingCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 22),
    _TnOamPingCtlMaxRows_Type()
)
tnOamPingCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlMaxRows.setStatus("obsolete")
if mibBuilder.loadTexts:
    tnOamPingCtlMaxRows.setUnits("rows")


class _TnOamPingCtlTrapGeneration_Type(Bits):
    """Custom type tnOamPingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("probeFailure", 0),
          ("testFailure", 1),
          ("testCompletion", 2))
    )

_TnOamPingCtlTrapGeneration_Type.__name__ = "Bits"
_TnOamPingCtlTrapGeneration_Object = MibTableColumn
tnOamPingCtlTrapGeneration = _TnOamPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 23),
    _TnOamPingCtlTrapGeneration_Type()
)
tnOamPingCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTrapGeneration.setStatus("current")


class _TnOamPingCtlTrapProbeFailureFilter_Type(Unsigned32):
    """Custom type tnOamPingCtlTrapProbeFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TnOamPingCtlTrapProbeFailureFilter_Type.__name__ = "Unsigned32"
_TnOamPingCtlTrapProbeFailureFilter_Object = MibTableColumn
tnOamPingCtlTrapProbeFailureFilter = _TnOamPingCtlTrapProbeFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 24),
    _TnOamPingCtlTrapProbeFailureFilter_Type()
)
tnOamPingCtlTrapProbeFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTrapProbeFailureFilter.setStatus("current")


class _TnOamPingCtlTrapTestFailureFilter_Type(Unsigned32):
    """Custom type tnOamPingCtlTrapTestFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TnOamPingCtlTrapTestFailureFilter_Type.__name__ = "Unsigned32"
_TnOamPingCtlTrapTestFailureFilter_Object = MibTableColumn
tnOamPingCtlTrapTestFailureFilter = _TnOamPingCtlTrapTestFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 25),
    _TnOamPingCtlTrapTestFailureFilter_Type()
)
tnOamPingCtlTrapTestFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTrapTestFailureFilter.setStatus("current")


class _TnOamPingCtlSAA_Type(TruthValue):
    """Custom type tnOamPingCtlSAA based on TruthValue"""
    defaultValue = 2


_TnOamPingCtlSAA_Type.__name__ = "TruthValue"
_TnOamPingCtlSAA_Object = MibTableColumn
tnOamPingCtlSAA = _TnOamPingCtlSAA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 26),
    _TnOamPingCtlSAA_Type()
)
tnOamPingCtlSAA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlSAA.setStatus("current")
_TnOamPingCtlRuns_Type = Counter32
_TnOamPingCtlRuns_Object = MibTableColumn
tnOamPingCtlRuns = _TnOamPingCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 27),
    _TnOamPingCtlRuns_Type()
)
tnOamPingCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlRuns.setStatus("current")
_TnOamPingCtlFailures_Type = Counter32
_TnOamPingCtlFailures_Object = MibTableColumn
tnOamPingCtlFailures = _TnOamPingCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 28),
    _TnOamPingCtlFailures_Type()
)
tnOamPingCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlFailures.setStatus("current")
_TnOamPingCtlLastRunResult_Type = TmnxOamTestResult
_TnOamPingCtlLastRunResult_Object = MibTableColumn
tnOamPingCtlLastRunResult = _TnOamPingCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 29),
    _TnOamPingCtlLastRunResult_Type()
)
tnOamPingCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlLastRunResult.setStatus("current")
_TnOamPingCtlLastChanged_Type = TimeStamp
_TnOamPingCtlLastChanged_Object = MibTableColumn
tnOamPingCtlLastChanged = _TnOamPingCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 30),
    _TnOamPingCtlLastChanged_Type()
)
tnOamPingCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlLastChanged.setStatus("current")


class _TnOamPingCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tnOamPingCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TnOamPingCtlVRtrID_Type.__name__ = "TmnxVRtrID"
_TnOamPingCtlVRtrID_Object = MibTableColumn
tnOamPingCtlVRtrID = _TnOamPingCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 31),
    _TnOamPingCtlVRtrID_Type()
)
tnOamPingCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlVRtrID.setStatus("current")


class _TnOamPingCtlTgtAddrType_Type(InetAddressType):
    """Custom type tnOamPingCtlTgtAddrType based on InetAddressType"""
    defaultValue = 0


_TnOamPingCtlTgtAddrType_Type.__name__ = "InetAddressType"
_TnOamPingCtlTgtAddrType_Object = MibTableColumn
tnOamPingCtlTgtAddrType = _TnOamPingCtlTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 32),
    _TnOamPingCtlTgtAddrType_Type()
)
tnOamPingCtlTgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTgtAddrType.setStatus("current")


class _TnOamPingCtlTgtAddress_Type(InetAddress):
    """Custom type tnOamPingCtlTgtAddress based on InetAddress"""
    defaultHexValue = ""


_TnOamPingCtlTgtAddress_Type.__name__ = "InetAddress"
_TnOamPingCtlTgtAddress_Object = MibTableColumn
tnOamPingCtlTgtAddress = _TnOamPingCtlTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 33),
    _TnOamPingCtlTgtAddress_Type()
)
tnOamPingCtlTgtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTgtAddress.setStatus("current")


class _TnOamPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tnOamPingCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TnOamPingCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TnOamPingCtlSrcAddrType_Object = MibTableColumn
tnOamPingCtlSrcAddrType = _TnOamPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 34),
    _TnOamPingCtlSrcAddrType_Type()
)
tnOamPingCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlSrcAddrType.setStatus("current")


class _TnOamPingCtlSrcAddress_Type(InetAddress):
    """Custom type tnOamPingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamPingCtlSrcAddress_Type.__name__ = "InetAddress"
_TnOamPingCtlSrcAddress_Object = MibTableColumn
tnOamPingCtlSrcAddress = _TnOamPingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 35),
    _TnOamPingCtlSrcAddress_Type()
)
tnOamPingCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlSrcAddress.setStatus("current")


class _TnOamPingCtlDnsName_Type(OctetString):
    """Custom type tnOamPingCtlDnsName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOamPingCtlDnsName_Type.__name__ = "OctetString"
_TnOamPingCtlDnsName_Object = MibTableColumn
tnOamPingCtlDnsName = _TnOamPingCtlDnsName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 36),
    _TnOamPingCtlDnsName_Type()
)
tnOamPingCtlDnsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlDnsName.setStatus("current")


class _TnOamPingCtlDNSRecord_Type(Integer32):
    """Custom type tnOamPingCtlDNSRecord based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Arecord", 1),
          ("ipv6AAAArecord", 2))
    )


_TnOamPingCtlDNSRecord_Type.__name__ = "Integer32"
_TnOamPingCtlDNSRecord_Object = MibTableColumn
tnOamPingCtlDNSRecord = _TnOamPingCtlDNSRecord_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 37),
    _TnOamPingCtlDNSRecord_Type()
)
tnOamPingCtlDNSRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlDNSRecord.setStatus("current")


class _TnOamPingCtlIntervalUnits_Type(Integer32):
    """Custom type tnOamPingCtlIntervalUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seconds", 1),
          ("centiseconds", 2))
    )


_TnOamPingCtlIntervalUnits_Type.__name__ = "Integer32"
_TnOamPingCtlIntervalUnits_Object = MibTableColumn
tnOamPingCtlIntervalUnits = _TnOamPingCtlIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 38),
    _TnOamPingCtlIntervalUnits_Type()
)
tnOamPingCtlIntervalUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlIntervalUnits.setStatus("current")
_TnOamEthCfmPingCtlTable_Object = MibTable
tnOamEthCfmPingCtlTable = _TnOamEthCfmPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44)
)
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlTable.setStatus("current")
_TnOamEthCfmPingCtlEntry_Object = MibTableRow
tnOamEthCfmPingCtlEntry = _TnOamEthCfmPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1)
)
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlEntry.setStatus("current")


class _TnOamEthCfmPingCtlTgtMacAddr_Type(MacAddress):
    """Custom type tnOamEthCfmPingCtlTgtMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TnOamEthCfmPingCtlTgtMacAddr_Type.__name__ = "MacAddress"
_TnOamEthCfmPingCtlTgtMacAddr_Object = MibTableColumn
tnOamEthCfmPingCtlTgtMacAddr = _TnOamEthCfmPingCtlTgtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1, 1),
    _TnOamEthCfmPingCtlTgtMacAddr_Type()
)
tnOamEthCfmPingCtlTgtMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlTgtMacAddr.setStatus("current")


class _TnOamEthCfmPingCtlSrcMdIndex_Type(Unsigned32):
    """Custom type tnOamEthCfmPingCtlSrcMdIndex based on Unsigned32"""
    defaultValue = 0


_TnOamEthCfmPingCtlSrcMdIndex_Type.__name__ = "Unsigned32"
_TnOamEthCfmPingCtlSrcMdIndex_Object = MibTableColumn
tnOamEthCfmPingCtlSrcMdIndex = _TnOamEthCfmPingCtlSrcMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1, 2),
    _TnOamEthCfmPingCtlSrcMdIndex_Type()
)
tnOamEthCfmPingCtlSrcMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlSrcMdIndex.setStatus("current")


class _TnOamEthCfmPingCtlSrcMaIndex_Type(Unsigned32):
    """Custom type tnOamEthCfmPingCtlSrcMaIndex based on Unsigned32"""
    defaultValue = 0


_TnOamEthCfmPingCtlSrcMaIndex_Type.__name__ = "Unsigned32"
_TnOamEthCfmPingCtlSrcMaIndex_Object = MibTableColumn
tnOamEthCfmPingCtlSrcMaIndex = _TnOamEthCfmPingCtlSrcMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1, 3),
    _TnOamEthCfmPingCtlSrcMaIndex_Type()
)
tnOamEthCfmPingCtlSrcMaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlSrcMaIndex.setStatus("current")


class _TnOamEthCfmPingCtlSrcMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tnOamEthCfmPingCtlSrcMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TnOamEthCfmPingCtlSrcMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TnOamEthCfmPingCtlSrcMepId_Object = MibTableColumn
tnOamEthCfmPingCtlSrcMepId = _TnOamEthCfmPingCtlSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1, 4),
    _TnOamEthCfmPingCtlSrcMepId_Type()
)
tnOamEthCfmPingCtlSrcMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlSrcMepId.setStatus("current")
_TnOamSaaObjs_ObjectIdentity = ObjectIdentity
tnOamSaaObjs = _TnOamSaaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3)
)
_TnOamSaaCtlAttributeTotal_Type = Integer32
_TnOamSaaCtlAttributeTotal_Object = MibScalar
tnOamSaaCtlAttributeTotal = _TnOamSaaCtlAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 3),
    _TnOamSaaCtlAttributeTotal_Type()
)
tnOamSaaCtlAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlAttributeTotal.setStatus("current")
_TnOamSaaCtlTable_Object = MibTable
tnOamSaaCtlTable = _TnOamSaaCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4)
)
if mibBuilder.loadTexts:
    tnOamSaaCtlTable.setStatus("current")
_TnOamSaaCtlEntry_Object = MibTableRow
tnOamSaaCtlEntry = _TnOamSaaCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1)
)
tnOamSaaCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamSaaCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamSaaCtlEntry.setStatus("current")


class _TnOamSaaCtlTestIndex_Type(SnmpAdminString):
    """Custom type tnOamSaaCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnOamSaaCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TnOamSaaCtlTestIndex_Object = MibTableColumn
tnOamSaaCtlTestIndex = _TnOamSaaCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 1),
    _TnOamSaaCtlTestIndex_Type()
)
tnOamSaaCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamSaaCtlTestIndex.setStatus("current")
_TnOamSaaCtlRowStatus_Type = RowStatus
_TnOamSaaCtlRowStatus_Object = MibTableColumn
tnOamSaaCtlRowStatus = _TnOamSaaCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 2),
    _TnOamSaaCtlRowStatus_Type()
)
tnOamSaaCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlRowStatus.setStatus("current")


class _TnOamSaaCtlStorageType_Type(StorageType):
    """Custom type tnOamSaaCtlStorageType based on StorageType"""
    defaultValue = 3


_TnOamSaaCtlStorageType_Type.__name__ = "StorageType"
_TnOamSaaCtlStorageType_Object = MibTableColumn
tnOamSaaCtlStorageType = _TnOamSaaCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 3),
    _TnOamSaaCtlStorageType_Type()
)
tnOamSaaCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlStorageType.setStatus("current")
_TnOamSaaCtlLastChanged_Type = TimeStamp
_TnOamSaaCtlLastChanged_Object = MibTableColumn
tnOamSaaCtlLastChanged = _TnOamSaaCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 4),
    _TnOamSaaCtlLastChanged_Type()
)
tnOamSaaCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlLastChanged.setStatus("current")


class _TnOamSaaCtlAdminStatus_Type(TmnxAdminState):
    """Custom type tnOamSaaCtlAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TnOamSaaCtlAdminStatus_Type.__name__ = "TmnxAdminState"
_TnOamSaaCtlAdminStatus_Object = MibTableColumn
tnOamSaaCtlAdminStatus = _TnOamSaaCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 5),
    _TnOamSaaCtlAdminStatus_Type()
)
tnOamSaaCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlAdminStatus.setStatus("current")


class _TnOamSaaCtlDescr_Type(TItemDescription):
    """Custom type tnOamSaaCtlDescr based on TItemDescription"""
    defaultHexValue = ""


_TnOamSaaCtlDescr_Type.__name__ = "TItemDescription"
_TnOamSaaCtlDescr_Object = MibTableColumn
tnOamSaaCtlDescr = _TnOamSaaCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 6),
    _TnOamSaaCtlDescr_Type()
)
tnOamSaaCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlDescr.setStatus("current")


class _TnOamSaaCtlTestMode_Type(TmnxOamTestMode):
    """Custom type tnOamSaaCtlTestMode based on TmnxOamTestMode"""
    defaultValue = 0


_TnOamSaaCtlTestMode_Type.__name__ = "TmnxOamTestMode"
_TnOamSaaCtlTestMode_Object = MibTableColumn
tnOamSaaCtlTestMode = _TnOamSaaCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 7),
    _TnOamSaaCtlTestMode_Type()
)
tnOamSaaCtlTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlTestMode.setStatus("current")
_TnOamSaaCtlRuns_Type = Counter32
_TnOamSaaCtlRuns_Object = MibTableColumn
tnOamSaaCtlRuns = _TnOamSaaCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 8),
    _TnOamSaaCtlRuns_Type()
)
tnOamSaaCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlRuns.setStatus("current")
_TnOamSaaCtlFailures_Type = Counter32
_TnOamSaaCtlFailures_Object = MibTableColumn
tnOamSaaCtlFailures = _TnOamSaaCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 9),
    _TnOamSaaCtlFailures_Type()
)
tnOamSaaCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlFailures.setStatus("current")
_TnOamSaaCtlLastRunResult_Type = TmnxOamTestResult
_TnOamSaaCtlLastRunResult_Object = MibTableColumn
tnOamSaaCtlLastRunResult = _TnOamSaaCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 10),
    _TnOamSaaCtlLastRunResult_Type()
)
tnOamSaaCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlLastRunResult.setStatus("current")


class _TnOamSaaCtlAcctPolicyId_Type(Integer32):
    """Custom type tnOamSaaCtlAcctPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnOamSaaCtlAcctPolicyId_Type.__name__ = "Integer32"
_TnOamSaaCtlAcctPolicyId_Object = MibTableColumn
tnOamSaaCtlAcctPolicyId = _TnOamSaaCtlAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 11),
    _TnOamSaaCtlAcctPolicyId_Type()
)
tnOamSaaCtlAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlAcctPolicyId.setStatus("current")


class _TnOamSaaCtlSuppressAccounting_Type(TruthValue):
    """Custom type tnOamSaaCtlSuppressAccounting based on TruthValue"""
    defaultValue = 2


_TnOamSaaCtlSuppressAccounting_Type.__name__ = "TruthValue"
_TnOamSaaCtlSuppressAccounting_Object = MibTableColumn
tnOamSaaCtlSuppressAccounting = _TnOamSaaCtlSuppressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 12),
    _TnOamSaaCtlSuppressAccounting_Type()
)
tnOamSaaCtlSuppressAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlSuppressAccounting.setStatus("current")


class _TnOamSaaCtlContinuous_Type(TruthValue):
    """Custom type tnOamSaaCtlContinuous based on TruthValue"""
    defaultValue = 2


_TnOamSaaCtlContinuous_Type.__name__ = "TruthValue"
_TnOamSaaCtlContinuous_Object = MibTableColumn
tnOamSaaCtlContinuous = _TnOamSaaCtlContinuous_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 13),
    _TnOamSaaCtlContinuous_Type()
)
tnOamSaaCtlContinuous.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlContinuous.setStatus("current")
_TnOamTestNotifications_ObjectIdentity = ObjectIdentity
tnOamTestNotifications = _TnOamTestNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11)
)
_TnOamPingNotifyPrefix_ObjectIdentity = ObjectIdentity
tnOamPingNotifyPrefix = _TnOamPingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 1)
)
_TnOamPingNotifications_ObjectIdentity = ObjectIdentity
tnOamPingNotifications = _TnOamPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 1, 0)
)
_TnOamTraceRouteNotifyPrefix_ObjectIdentity = ObjectIdentity
tnOamTraceRouteNotifyPrefix = _TnOamTraceRouteNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 2)
)
_TnOamTraceRouteNotifications_ObjectIdentity = ObjectIdentity
tnOamTraceRouteNotifications = _TnOamTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 2, 0)
)
_TnOamSaaNotifyPrefix_ObjectIdentity = ObjectIdentity
tnOamSaaNotifyPrefix = _TnOamSaaNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 3)
)
_TnOamSaaNotifications_ObjectIdentity = ObjectIdentity
tnOamSaaNotifications = _TnOamSaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 3, 0)
)
tnOamPingCtlEntry.registerAugmentions(
    ("TN-OAM-TEST-MIB",
     "tnOamEthCfmPingCtlEntry")
)
tnOamEthCfmPingCtlEntry.setIndexNames(*tnOamPingCtlEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-OAM-TEST-MIB",
    **{"TmnxOamTestMode": TmnxOamTestMode,
       "TmnxOamPingRtnCode": TmnxOamPingRtnCode,
       "TmnxOamAddressType": TmnxOamAddressType,
       "TmnxOamResponseStatus": TmnxOamResponseStatus,
       "TmnxOamSignalProtocol": TmnxOamSignalProtocol,
       "TmnxOamTestResponsePlane": TmnxOamTestResponsePlane,
       "TmnxOamSaaThreshold": TmnxOamSaaThreshold,
       "TmnxOamVcType": TmnxOamVcType,
       "TmnxOamLTtraceDisStatusBits": TmnxOamLTtraceDisStatusBits,
       "TmnxOamTestResult": TmnxOamTestResult,
       "tnOamTestMIBModule": tnOamTestMIBModule,
       "tnOamTestObjs": tnOamTestObjs,
       "tnOamPingObjs": tnOamPingObjs,
       "tnOamPingCtlAttributeTotal": tnOamPingCtlAttributeTotal,
       "tnOamPingCtlTable": tnOamPingCtlTable,
       "tnOamPingCtlEntry": tnOamPingCtlEntry,
       "tnOamPingCtlTestIndex": tnOamPingCtlTestIndex,
       "tnOamPingCtlRowStatus": tnOamPingCtlRowStatus,
       "tnOamPingCtlStorageType": tnOamPingCtlStorageType,
       "tnOamPingCtlDescr": tnOamPingCtlDescr,
       "tnOamPingCtlTestMode": tnOamPingCtlTestMode,
       "tnOamPingCtlAdminStatus": tnOamPingCtlAdminStatus,
       "tnOamPingCtlOrigSdpId": tnOamPingCtlOrigSdpId,
       "tnOamPingCtlRespSdpId": tnOamPingCtlRespSdpId,
       "tnOamPingCtlFcName": tnOamPingCtlFcName,
       "tnOamPingCtlProfile": tnOamPingCtlProfile,
       "tnOamPingCtlMtuStartSize": tnOamPingCtlMtuStartSize,
       "tnOamPingCtlMtuEndSize": tnOamPingCtlMtuEndSize,
       "tnOamPingCtlMtuStepSize": tnOamPingCtlMtuStepSize,
       "tnOamPingCtlTargetIpAddress": tnOamPingCtlTargetIpAddress,
       "tnOamPingCtlServiceId": tnOamPingCtlServiceId,
       "tnOamPingCtlLocalSdp": tnOamPingCtlLocalSdp,
       "tnOamPingCtlRemoteSdp": tnOamPingCtlRemoteSdp,
       "tnOamPingCtlSize": tnOamPingCtlSize,
       "tnOamPingCtlTimeOut": tnOamPingCtlTimeOut,
       "tnOamPingCtlProbeCount": tnOamPingCtlProbeCount,
       "tnOamPingCtlInterval": tnOamPingCtlInterval,
       "tnOamPingCtlMaxRows": tnOamPingCtlMaxRows,
       "tnOamPingCtlTrapGeneration": tnOamPingCtlTrapGeneration,
       "tnOamPingCtlTrapProbeFailureFilter": tnOamPingCtlTrapProbeFailureFilter,
       "tnOamPingCtlTrapTestFailureFilter": tnOamPingCtlTrapTestFailureFilter,
       "tnOamPingCtlSAA": tnOamPingCtlSAA,
       "tnOamPingCtlRuns": tnOamPingCtlRuns,
       "tnOamPingCtlFailures": tnOamPingCtlFailures,
       "tnOamPingCtlLastRunResult": tnOamPingCtlLastRunResult,
       "tnOamPingCtlLastChanged": tnOamPingCtlLastChanged,
       "tnOamPingCtlVRtrID": tnOamPingCtlVRtrID,
       "tnOamPingCtlTgtAddrType": tnOamPingCtlTgtAddrType,
       "tnOamPingCtlTgtAddress": tnOamPingCtlTgtAddress,
       "tnOamPingCtlSrcAddrType": tnOamPingCtlSrcAddrType,
       "tnOamPingCtlSrcAddress": tnOamPingCtlSrcAddress,
       "tnOamPingCtlDnsName": tnOamPingCtlDnsName,
       "tnOamPingCtlDNSRecord": tnOamPingCtlDNSRecord,
       "tnOamPingCtlIntervalUnits": tnOamPingCtlIntervalUnits,
       "tnOamEthCfmPingCtlTable": tnOamEthCfmPingCtlTable,
       "tnOamEthCfmPingCtlEntry": tnOamEthCfmPingCtlEntry,
       "tnOamEthCfmPingCtlTgtMacAddr": tnOamEthCfmPingCtlTgtMacAddr,
       "tnOamEthCfmPingCtlSrcMdIndex": tnOamEthCfmPingCtlSrcMdIndex,
       "tnOamEthCfmPingCtlSrcMaIndex": tnOamEthCfmPingCtlSrcMaIndex,
       "tnOamEthCfmPingCtlSrcMepId": tnOamEthCfmPingCtlSrcMepId,
       "tnOamSaaObjs": tnOamSaaObjs,
       "tnOamSaaCtlAttributeTotal": tnOamSaaCtlAttributeTotal,
       "tnOamSaaCtlTable": tnOamSaaCtlTable,
       "tnOamSaaCtlEntry": tnOamSaaCtlEntry,
       "tnOamSaaCtlTestIndex": tnOamSaaCtlTestIndex,
       "tnOamSaaCtlRowStatus": tnOamSaaCtlRowStatus,
       "tnOamSaaCtlStorageType": tnOamSaaCtlStorageType,
       "tnOamSaaCtlLastChanged": tnOamSaaCtlLastChanged,
       "tnOamSaaCtlAdminStatus": tnOamSaaCtlAdminStatus,
       "tnOamSaaCtlDescr": tnOamSaaCtlDescr,
       "tnOamSaaCtlTestMode": tnOamSaaCtlTestMode,
       "tnOamSaaCtlRuns": tnOamSaaCtlRuns,
       "tnOamSaaCtlFailures": tnOamSaaCtlFailures,
       "tnOamSaaCtlLastRunResult": tnOamSaaCtlLastRunResult,
       "tnOamSaaCtlAcctPolicyId": tnOamSaaCtlAcctPolicyId,
       "tnOamSaaCtlSuppressAccounting": tnOamSaaCtlSuppressAccounting,
       "tnOamSaaCtlContinuous": tnOamSaaCtlContinuous,
       "tnOamTestNotifications": tnOamTestNotifications,
       "tnOamPingNotifyPrefix": tnOamPingNotifyPrefix,
       "tnOamPingNotifications": tnOamPingNotifications,
       "tnOamTraceRouteNotifyPrefix": tnOamTraceRouteNotifyPrefix,
       "tnOamTraceRouteNotifications": tnOamTraceRouteNotifications,
       "tnOamSaaNotifyPrefix": tnOamSaaNotifyPrefix,
       "tnOamSaaNotifications": tnOamSaaNotifications}
)
