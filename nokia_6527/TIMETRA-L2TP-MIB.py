# SNMP MIB module (TIMETRA-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-L2TP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:24 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxPppCpState,) = mibBuilder.importSymbols(
    "TIMETRA-PPP-MIB",
    "TmnxPppCpState")

(iesIfIndex,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "iesIfIndex",
    "svcId")

(TBurstSizeBytesOverride,
 TCIRRateOverride,
 TDirection,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRateOverride,
 TQosOverrideType,
 TmnxAccessLoopEncapDataLink,
 TmnxAccessLoopEncaps1,
 TmnxAccessLoopEncaps2,
 TmnxActionType,
 TmnxAdminState,
 TmnxAncpStringOrZero,
 TmnxAppProfileStringOrEmpty,
 TmnxAsciiSpecification,
 TmnxBinarySpecification,
 TmnxDefSubIdSource,
 TmnxManagedRouteStatus,
 TmnxMlpppEpClass,
 TmnxOperState,
 TmnxPppNcpProtocol,
 TmnxPppoeSessionInfoOrigin,
 TmnxPppoeSessionType,
 TmnxPppoeUserNameOrEmpty,
 TmnxServId,
 TmnxSlaProfileStringOrEmpty,
 TmnxSubIdentStringOrEmpty,
 TmnxSubMgtIntDestIdOrEmpty,
 TmnxSubNasPortPrefixType,
 TmnxSubNasPortSuffixType,
 TmnxSubNasPortTypeType,
 TmnxSubProfileStringOrEmpty,
 TmnxSubRadServAlgorithm,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TBurstSizeBytesOverride",
    "TCIRRateOverride",
    "TDirection",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRateOverride",
    "TQosOverrideType",
    "TmnxAccessLoopEncapDataLink",
    "TmnxAccessLoopEncaps1",
    "TmnxAccessLoopEncaps2",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxAncpStringOrZero",
    "TmnxAppProfileStringOrEmpty",
    "TmnxAsciiSpecification",
    "TmnxBinarySpecification",
    "TmnxDefSubIdSource",
    "TmnxManagedRouteStatus",
    "TmnxMlpppEpClass",
    "TmnxOperState",
    "TmnxPppNcpProtocol",
    "TmnxPppoeSessionInfoOrigin",
    "TmnxPppoeSessionType",
    "TmnxPppoeUserNameOrEmpty",
    "TmnxServId",
    "TmnxSlaProfileStringOrEmpty",
    "TmnxSubIdentStringOrEmpty",
    "TmnxSubMgtIntDestIdOrEmpty",
    "TmnxSubNasPortPrefixType",
    "TmnxSubNasPortSuffixType",
    "TmnxSubNasPortTypeType",
    "TmnxSubProfileStringOrEmpty",
    "TmnxSubRadServAlgorithm",
    "TmnxVRtrIDOrZero")

(vRtrID,
 vRtrIfName) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfName")


# MODULE-IDENTITY

timetraL2tpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 60)
)
if mibBuilder.loadTexts:
    timetraL2tpMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxAlwaysNeverOrDefault(TextualConvention, Integer32):
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
        *(("default", 1),
          ("never", 2),
          ("always", 3))
    )



class TmnxAlwaysOrNever(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("never", 2),
          ("always", 3))
    )



class TmnxL2tpActionTypeDrain(TextualConvention, Integer32):
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
        *(("drain", 0),
          ("stopDrain", 1),
          ("notApplicable", 2))
    )



class TmnxL2tpAuthSecret(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TmnxL2tpAvpHidingMode(TextualConvention, Integer32):
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
        *(("default", 1),
          ("never", 2),
          ("sensitive", 3),
          ("always", 4))
    )



class TmnxL2tpCdnResult(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("lossCarrier", 1),
          ("generalError", 2),
          ("admin", 3),
          ("noFacTemporary", 4),
          ("noFacPermanent", 5),
          ("invalidDest", 6),
          ("noCarrier", 7),
          ("busy", 8),
          ("noDialTone", 9),
          ("notEstab", 10),
          ("noFraming", 11))
    )



class TmnxL2tpConnectionId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxL2tpDoChallenge(TextualConvention, Integer32):
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
        *(("default", 1),
          ("never", 2),
          ("always", 3))
    )



class TmnxL2tpErrorMessage(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxL2tpGeneralError(TextualConvention, Integer32):
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
        *(("noError", 0),
          ("noControl", 1),
          ("wrongLength", 2),
          ("fieldOutOfRange", 3),
          ("insufficientRes", 4),
          ("sessionIdInvalid", 5),
          ("vendorSpecific", 6),
          ("tryAnother", 7),
          ("unknownMandatory", 8))
    )



class TmnxL2tpHostNameOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TmnxL2tpIsaGrpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class TmnxL2tpIsaGrpIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class TmnxL2tpIsaMdaLoadBalanceMethod(TextualConvention, Integer32):
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
        *(("default", 0),
          ("perSession", 1),
          ("perTunnel", 2))
    )



class TmnxL2tpIsaMdaOperState(TextualConvention, Integer32):
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
          ("draining", 4),
          ("drained", 5))
    )



class TmnxL2tpLcpKaHoldUpMplier(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5),
    )



class TmnxL2tpLcpKaInterval(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 300),
    )



class TmnxL2tpMlpppEndpointClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("ipv4Address", 2),
          ("macAddress", 3))
    )



class TmnxL2tpMlpppMaxFragDelay(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 1000),
    )



class TmnxL2tpMlpppReassemblyTimeout(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )



class TmnxL2tpPeerAddrChangePolicy(TextualConvention, Integer32):
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
        *(("accept", 1),
          ("ignore", 2),
          ("reject", 3))
    )



class TmnxL2tpPppAuthentication(TextualConvention, Integer32):
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
        *(("default", 0),
          ("pap", 1),
          ("chap", 2),
          ("prefChap", 3),
          ("prefPap", 4))
    )



class TmnxL2tpPppMtu(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9212),
    )



class TmnxL2tpReceiveWindowSize(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 1024),
    )



class TmnxL2tpRoles(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("roleLAC", 0),
          ("roleLNS", 1))
    )


class TmnxL2tpSeOperState(TextualConvention, Integer32):
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
          ("idle", 1),
          ("waitTunnel", 2),
          ("waitReply", 3),
          ("waitAcceptance", 4),
          ("waitConnected", 5),
          ("established", 6),
          ("closed", 7),
          ("closedByPeer", 8))
    )



class TmnxL2tpSessionAssignMethod(TextualConvention, Integer32):
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
        *(("default", 0),
          ("existingFirst", 1),
          ("weighted", 2))
    )



class TmnxL2tpSessionId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxL2tpStopCcnResult(TextualConvention, Integer32):
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
        *(("noError", 0),
          ("generalReq", 1),
          ("generalErr", 2),
          ("alreadyExists", 3),
          ("reqNotAuth", 4),
          ("version", 5),
          ("reqShutDown", 6),
          ("fsmError", 7))
    )



class TmnxL2tpTgOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("drain", 2))
    )



class TmnxL2tpTransportType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("udpIp", 1))
    )



class TmnxL2tpTunnelDestructTO(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(60, 86400),
    )



class TmnxL2tpTunnelGroupName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class TmnxL2tpTunnelGroupNameOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class TmnxL2tpTunnelHelloInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(60, 3600),
    )



class TmnxL2tpTunnelId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxL2tpTunnelIdleTO(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 3600),
    )



class TmnxL2tpTunnelMaxRetx(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(2, 7),
    )



class TmnxL2tpTunnelName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class TmnxL2tpTunnelNameOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class TmnxL2tpTunnelPreference(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class TmnxL2tpTunnelSessionLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 131071),
    )



class TmnxL2tpTuOperState(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("idle", 2),
          ("waitReply", 3),
          ("waitConn", 4),
          ("establishedIdle", 5),
          ("established", 6),
          ("draining", 7),
          ("drained", 8),
          ("closed", 9),
          ("closedByPeer", 10))
    )



class TmnxL2tpTuProtStatsType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("event", 1),
          ("droppedMsgType", 2),
          ("acceptedMsgType", 3),
          ("originalTransmittedMsgType", 4),
          ("retransmittedMsgType", 5),
          ("incomingCDNresultCode", 6),
          ("incomingStopCCNresultCode", 7),
          ("incomingErrorCode", 8),
          ("outgoingCDNresultCode", 9),
          ("outgoingStopCCNresultCode", 10),
          ("outgoingErrorCode", 11))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxL2tpConformance_ObjectIdentity = ObjectIdentity
tmnxL2tpConformance = _TmnxL2tpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60)
)
_TmnxL2tpCompliances_ObjectIdentity = ObjectIdentity
tmnxL2tpCompliances = _TmnxL2tpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1)
)
_TmnxL2tpGroups_ObjectIdentity = ObjectIdentity
tmnxL2tpGroups = _TmnxL2tpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2)
)
_TmnxL2tp_ObjectIdentity = ObjectIdentity
tmnxL2tp = _TmnxL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60)
)
_TmnxL2tpObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpObjs = _TmnxL2tpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1)
)
_TmnxL2tpVrtrObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpVrtrObjs = _TmnxL2tpVrtrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1)
)
_TmnxL2tpVrtrCfgObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpVrtrCfgObjs = _TmnxL2tpVrtrCfgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1)
)
_TmnxL2tpTable_Object = MibTable
tmnxL2tpTable = _TmnxL2tpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpTable.setStatus("current")
_TmnxL2tpEntry_Object = MibTableRow
tmnxL2tpEntry = _TmnxL2tpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1)
)
tmnxL2tpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxL2tpEntry.setStatus("current")
_TmnxL2tpLastMgmtChange_Type = TimeStamp
_TmnxL2tpLastMgmtChange_Object = MibTableColumn
tmnxL2tpLastMgmtChange = _TmnxL2tpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 1),
    _TmnxL2tpLastMgmtChange_Type()
)
tmnxL2tpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLastMgmtChange.setStatus("current")


class _TmnxL2tpAdminState_Type(TmnxAdminState):
    """Custom type tmnxL2tpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxL2tpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxL2tpAdminState_Object = MibTableColumn
tmnxL2tpAdminState = _TmnxL2tpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 2),
    _TmnxL2tpAdminState_Type()
)
tmnxL2tpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpAdminState.setStatus("current")


class _TmnxL2tpSessionLimit_Type(TmnxL2tpTunnelSessionLimit):
    """Custom type tmnxL2tpSessionLimit based on TmnxL2tpTunnelSessionLimit"""
    defaultValue = 131071


_TmnxL2tpSessionLimit_Type.__name__ = "TmnxL2tpTunnelSessionLimit"
_TmnxL2tpSessionLimit_Object = MibTableColumn
tmnxL2tpSessionLimit = _TmnxL2tpSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 3),
    _TmnxL2tpSessionLimit_Type()
)
tmnxL2tpSessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpSessionLimit.setStatus("current")


class _TmnxL2tpReceiveWindowSize_Type(TmnxL2tpReceiveWindowSize):
    """Custom type tmnxL2tpReceiveWindowSize based on TmnxL2tpReceiveWindowSize"""
    defaultValue = 64


_TmnxL2tpReceiveWindowSize_Type.__name__ = "TmnxL2tpReceiveWindowSize"
_TmnxL2tpReceiveWindowSize_Object = MibTableColumn
tmnxL2tpReceiveWindowSize = _TmnxL2tpReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 4),
    _TmnxL2tpReceiveWindowSize_Type()
)
tmnxL2tpReceiveWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpReceiveWindowSize.setStatus("current")
_TmnxL2tpRowStatus_Type = RowStatus
_TmnxL2tpRowStatus_Object = MibTableColumn
tmnxL2tpRowStatus = _TmnxL2tpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 5),
    _TmnxL2tpRowStatus_Type()
)
tmnxL2tpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpRowStatus.setStatus("current")


class _TmnxL2tpPeerAddrChangePlcy_Type(TmnxL2tpPeerAddrChangePolicy):
    """Custom type tmnxL2tpPeerAddrChangePlcy based on TmnxL2tpPeerAddrChangePolicy"""
    defaultValue = 3


_TmnxL2tpPeerAddrChangePlcy_Type.__name__ = "TmnxL2tpPeerAddrChangePolicy"
_TmnxL2tpPeerAddrChangePlcy_Object = MibTableColumn
tmnxL2tpPeerAddrChangePlcy = _TmnxL2tpPeerAddrChangePlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 6),
    _TmnxL2tpPeerAddrChangePlcy_Type()
)
tmnxL2tpPeerAddrChangePlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpPeerAddrChangePlcy.setStatus("current")


class _TmnxL2tpAvpExclude_Type(Bits):
    """Custom type tmnxL2tpAvpExclude based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("callingNumber", 0),
          ("initialRxLcpConfReq", 1))
    )

_TmnxL2tpAvpExclude_Type.__name__ = "Bits"
_TmnxL2tpAvpExclude_Object = MibTableColumn
tmnxL2tpAvpExclude = _TmnxL2tpAvpExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 7),
    _TmnxL2tpAvpExclude_Type()
)
tmnxL2tpAvpExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpAvpExclude.setStatus("current")


class _TmnxL2tpAvpCallingNumberSpec_Type(TmnxAsciiSpecification):
    """Custom type tmnxL2tpAvpCallingNumberSpec based on TmnxAsciiSpecification"""
    defaultValue = OctetString("%S %s")


_TmnxL2tpAvpCallingNumberSpec_Type.__name__ = "TmnxAsciiSpecification"
_TmnxL2tpAvpCallingNumberSpec_Object = MibTableColumn
tmnxL2tpAvpCallingNumberSpec = _TmnxL2tpAvpCallingNumberSpec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 8),
    _TmnxL2tpAvpCallingNumberSpec_Type()
)
tmnxL2tpAvpCallingNumberSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpAvpCallingNumberSpec.setStatus("current")


class _TmnxL2tpAccountingPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpAccountingPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpAccountingPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpAccountingPolicy_Object = MibTableColumn
tmnxL2tpAccountingPolicy = _TmnxL2tpAccountingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 10),
    _TmnxL2tpAccountingPolicy_Type()
)
tmnxL2tpAccountingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpAccountingPolicy.setStatus("current")


class _TmnxL2tpHelloInterval_Type(TmnxL2tpTunnelHelloInterval):
    """Custom type tmnxL2tpHelloInterval based on TmnxL2tpTunnelHelloInterval"""
    defaultValue = 300


_TmnxL2tpHelloInterval_Type.__name__ = "TmnxL2tpTunnelHelloInterval"
_TmnxL2tpHelloInterval_Object = MibTableColumn
tmnxL2tpHelloInterval = _TmnxL2tpHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 11),
    _TmnxL2tpHelloInterval_Type()
)
tmnxL2tpHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpHelloInterval.setUnits("seconds")


class _TmnxL2tpIdleTO_Type(TmnxL2tpTunnelIdleTO):
    """Custom type tmnxL2tpIdleTO based on TmnxL2tpTunnelIdleTO"""
    defaultValue = -1


_TmnxL2tpIdleTO_Type.__name__ = "TmnxL2tpTunnelIdleTO"
_TmnxL2tpIdleTO_Object = MibTableColumn
tmnxL2tpIdleTO = _TmnxL2tpIdleTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 12),
    _TmnxL2tpIdleTO_Type()
)
tmnxL2tpIdleTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpIdleTO.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpIdleTO.setUnits("seconds")


class _TmnxL2tpDestructTO_Type(TmnxL2tpTunnelDestructTO):
    """Custom type tmnxL2tpDestructTO based on TmnxL2tpTunnelDestructTO"""
    defaultValue = 60


_TmnxL2tpDestructTO_Type.__name__ = "TmnxL2tpTunnelDestructTO"
_TmnxL2tpDestructTO_Object = MibTableColumn
tmnxL2tpDestructTO = _TmnxL2tpDestructTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 13),
    _TmnxL2tpDestructTO_Type()
)
tmnxL2tpDestructTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpDestructTO.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpDestructTO.setUnits("seconds")


class _TmnxL2tpMaxRetxEstab_Type(TmnxL2tpTunnelMaxRetx):
    """Custom type tmnxL2tpMaxRetxEstab based on TmnxL2tpTunnelMaxRetx"""
    defaultValue = 5


_TmnxL2tpMaxRetxEstab_Type.__name__ = "TmnxL2tpTunnelMaxRetx"
_TmnxL2tpMaxRetxEstab_Object = MibTableColumn
tmnxL2tpMaxRetxEstab = _TmnxL2tpMaxRetxEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 14),
    _TmnxL2tpMaxRetxEstab_Type()
)
tmnxL2tpMaxRetxEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpMaxRetxEstab.setStatus("current")


class _TmnxL2tpMaxRetxNotEstab_Type(TmnxL2tpTunnelMaxRetx):
    """Custom type tmnxL2tpMaxRetxNotEstab based on TmnxL2tpTunnelMaxRetx"""
    defaultValue = 5


_TmnxL2tpMaxRetxNotEstab_Type.__name__ = "TmnxL2tpTunnelMaxRetx"
_TmnxL2tpMaxRetxNotEstab_Object = MibTableColumn
tmnxL2tpMaxRetxNotEstab = _TmnxL2tpMaxRetxNotEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 15),
    _TmnxL2tpMaxRetxNotEstab_Type()
)
tmnxL2tpMaxRetxNotEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpMaxRetxNotEstab.setStatus("current")


class _TmnxL2tpTunnelSessionLimit_Type(TmnxL2tpTunnelSessionLimit):
    """Custom type tmnxL2tpTunnelSessionLimit based on TmnxL2tpTunnelSessionLimit"""
    defaultValue = 65535


_TmnxL2tpTunnelSessionLimit_Type.__name__ = "TmnxL2tpTunnelSessionLimit"
_TmnxL2tpTunnelSessionLimit_Object = MibTableColumn
tmnxL2tpTunnelSessionLimit = _TmnxL2tpTunnelSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 16),
    _TmnxL2tpTunnelSessionLimit_Type()
)
tmnxL2tpTunnelSessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTunnelSessionLimit.setStatus("current")


class _TmnxL2tpGroupSessionLimit_Type(TmnxL2tpTunnelSessionLimit):
    """Custom type tmnxL2tpGroupSessionLimit based on TmnxL2tpTunnelSessionLimit"""
    defaultValue = 131071


_TmnxL2tpGroupSessionLimit_Type.__name__ = "TmnxL2tpTunnelSessionLimit"
_TmnxL2tpGroupSessionLimit_Object = MibTableColumn
tmnxL2tpGroupSessionLimit = _TmnxL2tpGroupSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 17),
    _TmnxL2tpGroupSessionLimit_Type()
)
tmnxL2tpGroupSessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpGroupSessionLimit.setStatus("current")


class _TmnxL2tpAvpHiding_Type(TmnxL2tpAvpHidingMode):
    """Custom type tmnxL2tpAvpHiding based on TmnxL2tpAvpHidingMode"""
    defaultValue = 2


_TmnxL2tpAvpHiding_Type.__name__ = "TmnxL2tpAvpHidingMode"
_TmnxL2tpAvpHiding_Object = MibTableColumn
tmnxL2tpAvpHiding = _TmnxL2tpAvpHiding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 18),
    _TmnxL2tpAvpHiding_Type()
)
tmnxL2tpAvpHiding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpAvpHiding.setStatus("current")


class _TmnxL2tpDoChallenge_Type(TmnxL2tpDoChallenge):
    """Custom type tmnxL2tpDoChallenge based on TmnxL2tpDoChallenge"""
    defaultValue = 2


_TmnxL2tpDoChallenge_Type.__name__ = "TmnxL2tpDoChallenge"
_TmnxL2tpDoChallenge_Object = MibTableColumn
tmnxL2tpDoChallenge = _TmnxL2tpDoChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 19),
    _TmnxL2tpDoChallenge_Type()
)
tmnxL2tpDoChallenge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpDoChallenge.setStatus("current")


class _TmnxL2tpSecret_Type(TmnxL2tpAuthSecret):
    """Custom type tmnxL2tpSecret based on TmnxL2tpAuthSecret"""
    defaultHexValue = ""


_TmnxL2tpSecret_Type.__name__ = "TmnxL2tpAuthSecret"
_TmnxL2tpSecret_Object = MibTableColumn
tmnxL2tpSecret = _TmnxL2tpSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 20),
    _TmnxL2tpSecret_Type()
)
tmnxL2tpSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpSecret.setStatus("current")


class _TmnxL2tpSessionAssignMethod_Type(TmnxL2tpSessionAssignMethod):
    """Custom type tmnxL2tpSessionAssignMethod based on TmnxL2tpSessionAssignMethod"""
    defaultValue = 1


_TmnxL2tpSessionAssignMethod_Type.__name__ = "TmnxL2tpSessionAssignMethod"
_TmnxL2tpSessionAssignMethod_Object = MibTableColumn
tmnxL2tpSessionAssignMethod = _TmnxL2tpSessionAssignMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 21),
    _TmnxL2tpSessionAssignMethod_Type()
)
tmnxL2tpSessionAssignMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpSessionAssignMethod.setStatus("current")


class _TmnxL2tpLocalName_Type(TmnxL2tpHostNameOrEmpty):
    """Custom type tmnxL2tpLocalName based on TmnxL2tpHostNameOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpLocalName_Type.__name__ = "TmnxL2tpHostNameOrEmpty"
_TmnxL2tpLocalName_Object = MibTableColumn
tmnxL2tpLocalName = _TmnxL2tpLocalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 22),
    _TmnxL2tpLocalName_Type()
)
tmnxL2tpLocalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLocalName.setStatus("current")


class _TmnxL2tpAddrType_Type(InetAddressType):
    """Custom type tmnxL2tpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxL2tpAddrType_Type.__name__ = "InetAddressType"
_TmnxL2tpAddrType_Object = MibTableColumn
tmnxL2tpAddrType = _TmnxL2tpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 23),
    _TmnxL2tpAddrType_Type()
)
tmnxL2tpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpAddrType.setStatus("current")


class _TmnxL2tpAddr_Type(InetAddress):
    """Custom type tmnxL2tpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpAddr_Type.__name__ = "InetAddress"
_TmnxL2tpAddr_Object = MibTableColumn
tmnxL2tpAddr = _TmnxL2tpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 2, 1, 24),
    _TmnxL2tpAddr_Type()
)
tmnxL2tpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpAddr.setStatus("current")
_TmnxL2tpXtTable_Object = MibTable
tmnxL2tpXtTable = _TmnxL2tpXtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxL2tpXtTable.setStatus("current")
_TmnxL2tpXtEntry_Object = MibTableRow
tmnxL2tpXtEntry = _TmnxL2tpXtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpXtEntry.setStatus("current")


class _TmnxL2tpXtNextAttempt_Type(Integer32):
    """Custom type tmnxL2tpXtNextAttempt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("samePreferenceLevel", 0),
          ("nextPreferenceLevel", 1))
    )


_TmnxL2tpXtNextAttempt_Type.__name__ = "Integer32"
_TmnxL2tpXtNextAttempt_Object = MibTableColumn
tmnxL2tpXtNextAttempt = _TmnxL2tpXtNextAttempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 1),
    _TmnxL2tpXtNextAttempt_Type()
)
tmnxL2tpXtNextAttempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtNextAttempt.setStatus("current")
_TmnxL2tpXtLastMgmtChange_Type = TimeStamp
_TmnxL2tpXtLastMgmtChange_Object = MibTableColumn
tmnxL2tpXtLastMgmtChange = _TmnxL2tpXtLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 2),
    _TmnxL2tpXtLastMgmtChange_Type()
)
tmnxL2tpXtLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpXtLastMgmtChange.setStatus("current")


class _TmnxL2tpXtTuSelBlacklistReason_Type(Bits):
    """Custom type tmnxL2tpXtTuSelBlacklistReason based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("addrChangeTimeout", 0),
          ("cdnErrCode", 1),
          ("cdnInvDest", 2),
          ("cdnPermNoFacilities", 3),
          ("cdnTmpNoFacilities", 4),
          ("stopCcnErrCode", 5),
          ("stopCcnOther", 6),
          ("txCdnNotEstablishedInTime", 7))
    )

_TmnxL2tpXtTuSelBlacklistReason_Type.__name__ = "Bits"
_TmnxL2tpXtTuSelBlacklistReason_Object = MibTableColumn
tmnxL2tpXtTuSelBlacklistReason = _TmnxL2tpXtTuSelBlacklistReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 3),
    _TmnxL2tpXtTuSelBlacklistReason_Type()
)
tmnxL2tpXtTuSelBlacklistReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtTuSelBlacklistReason.setStatus("current")


class _TmnxL2tpXtTuSelBlacklistMaxTime_Type(Integer32):
    """Custom type tmnxL2tpXtTuSelBlacklistMaxTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxL2tpXtTuSelBlacklistMaxTime_Type.__name__ = "Integer32"
_TmnxL2tpXtTuSelBlacklistMaxTime_Object = MibTableColumn
tmnxL2tpXtTuSelBlacklistMaxTime = _TmnxL2tpXtTuSelBlacklistMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 4),
    _TmnxL2tpXtTuSelBlacklistMaxTime_Type()
)
tmnxL2tpXtTuSelBlacklistMaxTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtTuSelBlacklistMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpXtTuSelBlacklistMaxTime.setUnits("minutes")


class _TmnxL2tpXtTuSelBlacklistLength_Type(Integer32):
    """Custom type tmnxL2tpXtTuSelBlacklistLength based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )


_TmnxL2tpXtTuSelBlacklistLength_Type.__name__ = "Integer32"
_TmnxL2tpXtTuSelBlacklistLength_Object = MibTableColumn
tmnxL2tpXtTuSelBlacklistLength = _TmnxL2tpXtTuSelBlacklistLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 5),
    _TmnxL2tpXtTuSelBlacklistLength_Type()
)
tmnxL2tpXtTuSelBlacklistLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtTuSelBlacklistLength.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpXtTuSelBlacklistLength.setUnits("minutes")


class _TmnxL2tpXtTuSelBlacklistToAction_Type(Integer32):
    """Custom type tmnxL2tpXtTuSelBlacklistToAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("removeFromBlacklist", 0),
          ("tryOneSession", 1))
    )


_TmnxL2tpXtTuSelBlacklistToAction_Type.__name__ = "Integer32"
_TmnxL2tpXtTuSelBlacklistToAction_Object = MibTableColumn
tmnxL2tpXtTuSelBlacklistToAction = _TmnxL2tpXtTuSelBlacklistToAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 6),
    _TmnxL2tpXtTuSelBlacklistToAction_Type()
)
tmnxL2tpXtTuSelBlacklistToAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtTuSelBlacklistToAction.setStatus("current")


class _TmnxL2tpXtReplaceResultCodes_Type(Bits):
    """Custom type tmnxL2tpXtReplaceResultCodes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("cdnInvDest", 0),
          ("cdnPermNoFacilities", 1),
          ("cdnTmpNoFacilities", 2))
    )

_TmnxL2tpXtReplaceResultCodes_Type.__name__ = "Bits"
_TmnxL2tpXtReplaceResultCodes_Object = MibTableColumn
tmnxL2tpXtReplaceResultCodes = _TmnxL2tpXtReplaceResultCodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 7),
    _TmnxL2tpXtReplaceResultCodes_Type()
)
tmnxL2tpXtReplaceResultCodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtReplaceResultCodes.setStatus("current")


class _TmnxL2tpXtAvpCiscoNasPortEth_Type(TmnxBinarySpecification):
    """Custom type tmnxL2tpXtAvpCiscoNasPortEth based on TmnxBinarySpecification"""
    defaultValue = OctetString("")


_TmnxL2tpXtAvpCiscoNasPortEth_Type.__name__ = "TmnxBinarySpecification"
_TmnxL2tpXtAvpCiscoNasPortEth_Object = MibTableColumn
tmnxL2tpXtAvpCiscoNasPortEth = _TmnxL2tpXtAvpCiscoNasPortEth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 8),
    _TmnxL2tpXtAvpCiscoNasPortEth_Type()
)
tmnxL2tpXtAvpCiscoNasPortEth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtAvpCiscoNasPortEth.setStatus("current")


class _TmnxL2tpXtAvpCiscoNasPortAtm_Type(TmnxBinarySpecification):
    """Custom type tmnxL2tpXtAvpCiscoNasPortAtm based on TmnxBinarySpecification"""
    defaultValue = OctetString("")


_TmnxL2tpXtAvpCiscoNasPortAtm_Type.__name__ = "TmnxBinarySpecification"
_TmnxL2tpXtAvpCiscoNasPortAtm_Object = MibTableColumn
tmnxL2tpXtAvpCiscoNasPortAtm = _TmnxL2tpXtAvpCiscoNasPortAtm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 9),
    _TmnxL2tpXtAvpCiscoNasPortAtm_Type()
)
tmnxL2tpXtAvpCiscoNasPortAtm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtAvpCiscoNasPortAtm.setStatus("current")


class _TmnxL2tpXtDfBitLac_Type(TmnxAlwaysOrNever):
    """Custom type tmnxL2tpXtDfBitLac based on TmnxAlwaysOrNever"""
    defaultValue = 3


_TmnxL2tpXtDfBitLac_Type.__name__ = "TmnxAlwaysOrNever"
_TmnxL2tpXtDfBitLac_Object = MibTableColumn
tmnxL2tpXtDfBitLac = _TmnxL2tpXtDfBitLac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 1, 3, 1, 10),
    _TmnxL2tpXtDfBitLac_Type()
)
tmnxL2tpXtDfBitLac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpXtDfBitLac.setStatus("current")
_TmnxL2tpVrtrStatObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpVrtrStatObjs = _TmnxL2tpVrtrStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2)
)
_TmnxL2tpStatTable_Object = MibTable
tmnxL2tpStatTable = _TmnxL2tpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpStatTable.setStatus("current")
_TmnxL2tpStatEntry_Object = MibTableRow
tmnxL2tpStatEntry = _TmnxL2tpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1)
)
tmnxL2tpStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxL2tpStatEntry.setStatus("current")
_TmnxL2tpStatCleared_Type = TimeStamp
_TmnxL2tpStatCleared_Object = MibTableColumn
tmnxL2tpStatCleared = _TmnxL2tpStatCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 1),
    _TmnxL2tpStatCleared_Type()
)
tmnxL2tpStatCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatCleared.setStatus("current")
_TmnxL2tpStatTotalTunnels_Type = Counter32
_TmnxL2tpStatTotalTunnels_Object = MibTableColumn
tmnxL2tpStatTotalTunnels = _TmnxL2tpStatTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 2),
    _TmnxL2tpStatTotalTunnels_Type()
)
tmnxL2tpStatTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatTotalTunnels.setStatus("current")
_TmnxL2tpStatFailedTunnels_Type = Counter32
_TmnxL2tpStatFailedTunnels_Object = MibTableColumn
tmnxL2tpStatFailedTunnels = _TmnxL2tpStatFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 3),
    _TmnxL2tpStatFailedTunnels_Type()
)
tmnxL2tpStatFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatFailedTunnels.setStatus("current")
_TmnxL2tpStatFailedTuAuth_Type = Counter32
_TmnxL2tpStatFailedTuAuth_Object = MibTableColumn
tmnxL2tpStatFailedTuAuth = _TmnxL2tpStatFailedTuAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 4),
    _TmnxL2tpStatFailedTuAuth_Type()
)
tmnxL2tpStatFailedTuAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatFailedTuAuth.setStatus("current")
_TmnxL2tpStatActiveTunnels_Type = Gauge32
_TmnxL2tpStatActiveTunnels_Object = MibTableColumn
tmnxL2tpStatActiveTunnels = _TmnxL2tpStatActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 5),
    _TmnxL2tpStatActiveTunnels_Type()
)
tmnxL2tpStatActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatActiveTunnels.setStatus("current")
_TmnxL2tpStatTotalSessions_Type = Counter32
_TmnxL2tpStatTotalSessions_Object = MibTableColumn
tmnxL2tpStatTotalSessions = _TmnxL2tpStatTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 6),
    _TmnxL2tpStatTotalSessions_Type()
)
tmnxL2tpStatTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatTotalSessions.setStatus("current")
_TmnxL2tpStatFailedSessions_Type = Counter32
_TmnxL2tpStatFailedSessions_Object = MibTableColumn
tmnxL2tpStatFailedSessions = _TmnxL2tpStatFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 7),
    _TmnxL2tpStatFailedSessions_Type()
)
tmnxL2tpStatFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatFailedSessions.setStatus("current")
_TmnxL2tpStatActiveSessions_Type = Gauge32
_TmnxL2tpStatActiveSessions_Object = MibTableColumn
tmnxL2tpStatActiveSessions = _TmnxL2tpStatActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 8),
    _TmnxL2tpStatActiveSessions_Type()
)
tmnxL2tpStatActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatActiveSessions.setStatus("current")
_TmnxL2tpStatCurrentTunnels_Type = Gauge32
_TmnxL2tpStatCurrentTunnels_Object = MibTableColumn
tmnxL2tpStatCurrentTunnels = _TmnxL2tpStatCurrentTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 9),
    _TmnxL2tpStatCurrentTunnels_Type()
)
tmnxL2tpStatCurrentTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatCurrentTunnels.setStatus("current")
_TmnxL2tpStatCurrentSessions_Type = Gauge32
_TmnxL2tpStatCurrentSessions_Object = MibTableColumn
tmnxL2tpStatCurrentSessions = _TmnxL2tpStatCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 10),
    _TmnxL2tpStatCurrentSessions_Type()
)
tmnxL2tpStatCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatCurrentSessions.setStatus("current")
_TmnxL2tpStatCurrSelBlacklstLen_Type = Gauge32
_TmnxL2tpStatCurrSelBlacklstLen_Object = MibTableColumn
tmnxL2tpStatCurrSelBlacklstLen = _TmnxL2tpStatCurrSelBlacklstLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 11),
    _TmnxL2tpStatCurrSelBlacklstLen_Type()
)
tmnxL2tpStatCurrSelBlacklstLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatCurrSelBlacklstLen.setStatus("current")
_TmnxL2tpStatUnavailTunnelIds_Type = Gauge32
_TmnxL2tpStatUnavailTunnelIds_Object = MibTableColumn
tmnxL2tpStatUnavailTunnelIds = _TmnxL2tpStatUnavailTunnelIds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 1, 2, 1, 1, 12),
    _TmnxL2tpStatUnavailTunnelIds_Type()
)
tmnxL2tpStatUnavailTunnelIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpStatUnavailTunnelIds.setStatus("current")
_TmnxL2tpTgObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpTgObjs = _TmnxL2tpTgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2)
)
_TmnxL2tpTgCfgObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpTgCfgObjs = _TmnxL2tpTgCfgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1)
)
_TmnxL2tpTgCfgTable_Object = MibTable
tmnxL2tpTgCfgTable = _TmnxL2tpTgCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgTable.setStatus("current")
_TmnxL2tpTgCfgEntry_Object = MibTableRow
tmnxL2tpTgCfgEntry = _TmnxL2tpTgCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1)
)
tmnxL2tpTgCfgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgName"),
)
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgEntry.setStatus("current")
_TmnxL2tpTgCfgName_Type = TmnxL2tpTunnelGroupName
_TmnxL2tpTgCfgName_Object = MibTableColumn
tmnxL2tpTgCfgName = _TmnxL2tpTgCfgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 1),
    _TmnxL2tpTgCfgName_Type()
)
tmnxL2tpTgCfgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgName.setStatus("current")
_TmnxL2tpTgCfgRowStatus_Type = RowStatus
_TmnxL2tpTgCfgRowStatus_Object = MibTableColumn
tmnxL2tpTgCfgRowStatus = _TmnxL2tpTgCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 2),
    _TmnxL2tpTgCfgRowStatus_Type()
)
tmnxL2tpTgCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgRowStatus.setStatus("current")
_TmnxL2tpTgCfgLastMgmtChange_Type = TimeStamp
_TmnxL2tpTgCfgLastMgmtChange_Object = MibTableColumn
tmnxL2tpTgCfgLastMgmtChange = _TmnxL2tpTgCfgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 3),
    _TmnxL2tpTgCfgLastMgmtChange_Type()
)
tmnxL2tpTgCfgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgLastMgmtChange.setStatus("current")


class _TmnxL2tpTgCfgDescription_Type(TItemDescription):
    """Custom type tmnxL2tpTgCfgDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxL2tpTgCfgDescription_Type.__name__ = "TItemDescription"
_TmnxL2tpTgCfgDescription_Object = MibTableColumn
tmnxL2tpTgCfgDescription = _TmnxL2tpTgCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 4),
    _TmnxL2tpTgCfgDescription_Type()
)
tmnxL2tpTgCfgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgDescription.setStatus("current")


class _TmnxL2tpTgCfgAdminState_Type(TmnxAdminState):
    """Custom type tmnxL2tpTgCfgAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxL2tpTgCfgAdminState_Type.__name__ = "TmnxAdminState"
_TmnxL2tpTgCfgAdminState_Object = MibTableColumn
tmnxL2tpTgCfgAdminState = _TmnxL2tpTgCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 5),
    _TmnxL2tpTgCfgAdminState_Type()
)
tmnxL2tpTgCfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgAdminState.setStatus("current")


class _TmnxL2tpTgCfgSecret_Type(TmnxL2tpAuthSecret):
    """Custom type tmnxL2tpTgCfgSecret based on TmnxL2tpAuthSecret"""
    defaultHexValue = ""


_TmnxL2tpTgCfgSecret_Type.__name__ = "TmnxL2tpAuthSecret"
_TmnxL2tpTgCfgSecret_Object = MibTableColumn
tmnxL2tpTgCfgSecret = _TmnxL2tpTgCfgSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 6),
    _TmnxL2tpTgCfgSecret_Type()
)
tmnxL2tpTgCfgSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgSecret.setStatus("current")


class _TmnxL2tpTgCfgHelloInterval_Type(TmnxL2tpTunnelHelloInterval):
    """Custom type tmnxL2tpTgCfgHelloInterval based on TmnxL2tpTunnelHelloInterval"""
    defaultValue = -2


_TmnxL2tpTgCfgHelloInterval_Type.__name__ = "TmnxL2tpTunnelHelloInterval"
_TmnxL2tpTgCfgHelloInterval_Object = MibTableColumn
tmnxL2tpTgCfgHelloInterval = _TmnxL2tpTgCfgHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 7),
    _TmnxL2tpTgCfgHelloInterval_Type()
)
tmnxL2tpTgCfgHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgHelloInterval.setUnits("seconds")


class _TmnxL2tpTgCfgIdleTO_Type(TmnxL2tpTunnelIdleTO):
    """Custom type tmnxL2tpTgCfgIdleTO based on TmnxL2tpTunnelIdleTO"""
    defaultValue = -2


_TmnxL2tpTgCfgIdleTO_Type.__name__ = "TmnxL2tpTunnelIdleTO"
_TmnxL2tpTgCfgIdleTO_Object = MibTableColumn
tmnxL2tpTgCfgIdleTO = _TmnxL2tpTgCfgIdleTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 8),
    _TmnxL2tpTgCfgIdleTO_Type()
)
tmnxL2tpTgCfgIdleTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgIdleTO.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgIdleTO.setUnits("seconds")


class _TmnxL2tpTgCfgDestructTO_Type(TmnxL2tpTunnelDestructTO):
    """Custom type tmnxL2tpTgCfgDestructTO based on TmnxL2tpTunnelDestructTO"""
    defaultValue = -2


_TmnxL2tpTgCfgDestructTO_Type.__name__ = "TmnxL2tpTunnelDestructTO"
_TmnxL2tpTgCfgDestructTO_Object = MibTableColumn
tmnxL2tpTgCfgDestructTO = _TmnxL2tpTgCfgDestructTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 9),
    _TmnxL2tpTgCfgDestructTO_Type()
)
tmnxL2tpTgCfgDestructTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgDestructTO.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgDestructTO.setUnits("seconds")


class _TmnxL2tpTgCfgMaxRetxEstab_Type(TmnxL2tpTunnelMaxRetx):
    """Custom type tmnxL2tpTgCfgMaxRetxEstab based on TmnxL2tpTunnelMaxRetx"""
    defaultValue = -2


_TmnxL2tpTgCfgMaxRetxEstab_Type.__name__ = "TmnxL2tpTunnelMaxRetx"
_TmnxL2tpTgCfgMaxRetxEstab_Object = MibTableColumn
tmnxL2tpTgCfgMaxRetxEstab = _TmnxL2tpTgCfgMaxRetxEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 10),
    _TmnxL2tpTgCfgMaxRetxEstab_Type()
)
tmnxL2tpTgCfgMaxRetxEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgMaxRetxEstab.setStatus("current")


class _TmnxL2tpTgCfgMaxRetxNotEstab_Type(TmnxL2tpTunnelMaxRetx):
    """Custom type tmnxL2tpTgCfgMaxRetxNotEstab based on TmnxL2tpTunnelMaxRetx"""
    defaultValue = -2


_TmnxL2tpTgCfgMaxRetxNotEstab_Type.__name__ = "TmnxL2tpTunnelMaxRetx"
_TmnxL2tpTgCfgMaxRetxNotEstab_Object = MibTableColumn
tmnxL2tpTgCfgMaxRetxNotEstab = _TmnxL2tpTgCfgMaxRetxNotEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 11),
    _TmnxL2tpTgCfgMaxRetxNotEstab_Type()
)
tmnxL2tpTgCfgMaxRetxNotEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgMaxRetxNotEstab.setStatus("current")


class _TmnxL2tpTgCfgSessionLimit_Type(TmnxL2tpTunnelSessionLimit):
    """Custom type tmnxL2tpTgCfgSessionLimit based on TmnxL2tpTunnelSessionLimit"""
    defaultValue = -2


_TmnxL2tpTgCfgSessionLimit_Type.__name__ = "TmnxL2tpTunnelSessionLimit"
_TmnxL2tpTgCfgSessionLimit_Object = MibTableColumn
tmnxL2tpTgCfgSessionLimit = _TmnxL2tpTgCfgSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 12),
    _TmnxL2tpTgCfgSessionLimit_Type()
)
tmnxL2tpTgCfgSessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgSessionLimit.setStatus("current")


class _TmnxL2tpTgCfgAvpHiding_Type(TmnxL2tpAvpHidingMode):
    """Custom type tmnxL2tpTgCfgAvpHiding based on TmnxL2tpAvpHidingMode"""
    defaultValue = 1


_TmnxL2tpTgCfgAvpHiding_Type.__name__ = "TmnxL2tpAvpHidingMode"
_TmnxL2tpTgCfgAvpHiding_Object = MibTableColumn
tmnxL2tpTgCfgAvpHiding = _TmnxL2tpTgCfgAvpHiding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 13),
    _TmnxL2tpTgCfgAvpHiding_Type()
)
tmnxL2tpTgCfgAvpHiding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgAvpHiding.setStatus("current")


class _TmnxL2tpTgCfgSessionAssignMethod_Type(TmnxL2tpSessionAssignMethod):
    """Custom type tmnxL2tpTgCfgSessionAssignMethod based on TmnxL2tpSessionAssignMethod"""
    defaultValue = 0


_TmnxL2tpTgCfgSessionAssignMethod_Type.__name__ = "TmnxL2tpSessionAssignMethod"
_TmnxL2tpTgCfgSessionAssignMethod_Object = MibTableColumn
tmnxL2tpTgCfgSessionAssignMethod = _TmnxL2tpTgCfgSessionAssignMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 14),
    _TmnxL2tpTgCfgSessionAssignMethod_Type()
)
tmnxL2tpTgCfgSessionAssignMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgSessionAssignMethod.setStatus("current")


class _TmnxL2tpTgCfgLocalName_Type(TmnxL2tpHostNameOrEmpty):
    """Custom type tmnxL2tpTgCfgLocalName based on TmnxL2tpHostNameOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpTgCfgLocalName_Type.__name__ = "TmnxL2tpHostNameOrEmpty"
_TmnxL2tpTgCfgLocalName_Object = MibTableColumn
tmnxL2tpTgCfgLocalName = _TmnxL2tpTgCfgLocalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 15),
    _TmnxL2tpTgCfgLocalName_Type()
)
tmnxL2tpTgCfgLocalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgLocalName.setStatus("current")


class _TmnxL2tpTgCfgDoChallenge_Type(TmnxL2tpDoChallenge):
    """Custom type tmnxL2tpTgCfgDoChallenge based on TmnxL2tpDoChallenge"""
    defaultValue = 1


_TmnxL2tpTgCfgDoChallenge_Type.__name__ = "TmnxL2tpDoChallenge"
_TmnxL2tpTgCfgDoChallenge_Object = MibTableColumn
tmnxL2tpTgCfgDoChallenge = _TmnxL2tpTgCfgDoChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 16),
    _TmnxL2tpTgCfgDoChallenge_Type()
)
tmnxL2tpTgCfgDoChallenge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgDoChallenge.setStatus("current")


class _TmnxL2tpTgCfgReceiveWindowSize_Type(TmnxL2tpReceiveWindowSize):
    """Custom type tmnxL2tpTgCfgReceiveWindowSize based on TmnxL2tpReceiveWindowSize"""
    defaultValue = 0


_TmnxL2tpTgCfgReceiveWindowSize_Type.__name__ = "TmnxL2tpReceiveWindowSize"
_TmnxL2tpTgCfgReceiveWindowSize_Object = MibTableColumn
tmnxL2tpTgCfgReceiveWindowSize = _TmnxL2tpTgCfgReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 17),
    _TmnxL2tpTgCfgReceiveWindowSize_Type()
)
tmnxL2tpTgCfgReceiveWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgReceiveWindowSize.setStatus("current")


class _TmnxL2tpTgCfgIsaGrpId_Type(TmnxL2tpIsaGrpIdOrZero):
    """Custom type tmnxL2tpTgCfgIsaGrpId based on TmnxL2tpIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxL2tpTgCfgIsaGrpId_Type.__name__ = "TmnxL2tpIsaGrpIdOrZero"
_TmnxL2tpTgCfgIsaGrpId_Object = MibTableColumn
tmnxL2tpTgCfgIsaGrpId = _TmnxL2tpTgCfgIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 19),
    _TmnxL2tpTgCfgIsaGrpId_Type()
)
tmnxL2tpTgCfgIsaGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgIsaGrpId.setStatus("current")


class _TmnxL2tpTgCfgAddrType_Type(InetAddressType):
    """Custom type tmnxL2tpTgCfgAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxL2tpTgCfgAddrType_Type.__name__ = "InetAddressType"
_TmnxL2tpTgCfgAddrType_Object = MibTableColumn
tmnxL2tpTgCfgAddrType = _TmnxL2tpTgCfgAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 20),
    _TmnxL2tpTgCfgAddrType_Type()
)
tmnxL2tpTgCfgAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgAddrType.setStatus("current")


class _TmnxL2tpTgCfgAddr_Type(InetAddress):
    """Custom type tmnxL2tpTgCfgAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpTgCfgAddr_Type.__name__ = "InetAddress"
_TmnxL2tpTgCfgAddr_Object = MibTableColumn
tmnxL2tpTgCfgAddr = _TmnxL2tpTgCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 21),
    _TmnxL2tpTgCfgAddr_Type()
)
tmnxL2tpTgCfgAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgAddr.setStatus("current")


class _TmnxL2tpTgCfgLoadBalanceMethod_Type(TmnxL2tpIsaMdaLoadBalanceMethod):
    """Custom type tmnxL2tpTgCfgLoadBalanceMethod based on TmnxL2tpIsaMdaLoadBalanceMethod"""
    defaultValue = 1


_TmnxL2tpTgCfgLoadBalanceMethod_Type.__name__ = "TmnxL2tpIsaMdaLoadBalanceMethod"
_TmnxL2tpTgCfgLoadBalanceMethod_Object = MibTableColumn
tmnxL2tpTgCfgLoadBalanceMethod = _TmnxL2tpTgCfgLoadBalanceMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 25),
    _TmnxL2tpTgCfgLoadBalanceMethod_Type()
)
tmnxL2tpTgCfgLoadBalanceMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgLoadBalanceMethod.setStatus("current")


class _TmnxL2tpTgCfgAccountingPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpTgCfgAccountingPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpTgCfgAccountingPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpTgCfgAccountingPolicy_Object = MibTableColumn
tmnxL2tpTgCfgAccountingPolicy = _TmnxL2tpTgCfgAccountingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 2, 1, 26),
    _TmnxL2tpTgCfgAccountingPolicy_Type()
)
tmnxL2tpTgCfgAccountingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgAccountingPolicy.setStatus("current")
_TmnxL2tpLnsTgPppTable_Object = MibTable
tmnxL2tpLnsTgPppTable = _TmnxL2tpLnsTgPppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppTable.setStatus("current")
_TmnxL2tpLnsTgPppEntry_Object = MibTableRow
tmnxL2tpLnsTgPppEntry = _TmnxL2tpLnsTgPppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppEntry.setStatus("current")
_TmnxL2tpLnsTgPppLastMgmtChange_Type = TimeStamp
_TmnxL2tpLnsTgPppLastMgmtChange_Object = MibTableColumn
tmnxL2tpLnsTgPppLastMgmtChange = _TmnxL2tpLnsTgPppLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 1),
    _TmnxL2tpLnsTgPppLastMgmtChange_Type()
)
tmnxL2tpLnsTgPppLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppLastMgmtChange.setStatus("current")


class _TmnxL2tpLnsTgPppAuthPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsTgPppAuthPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpLnsTgPppAuthPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsTgPppAuthPlcy_Object = MibTableColumn
tmnxL2tpLnsTgPppAuthPlcy = _TmnxL2tpLnsTgPppAuthPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 2),
    _TmnxL2tpLnsTgPppAuthPlcy_Type()
)
tmnxL2tpLnsTgPppAuthPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppAuthPlcy.setStatus("current")


class _TmnxL2tpLnsTgPppAuthProtocol_Type(TmnxL2tpPppAuthentication):
    """Custom type tmnxL2tpLnsTgPppAuthProtocol based on TmnxL2tpPppAuthentication"""
    defaultValue = 3


_TmnxL2tpLnsTgPppAuthProtocol_Type.__name__ = "TmnxL2tpPppAuthentication"
_TmnxL2tpLnsTgPppAuthProtocol_Object = MibTableColumn
tmnxL2tpLnsTgPppAuthProtocol = _TmnxL2tpLnsTgPppAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 3),
    _TmnxL2tpLnsTgPppAuthProtocol_Type()
)
tmnxL2tpLnsTgPppAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppAuthProtocol.setStatus("current")


class _TmnxL2tpLnsTgPppUserDb_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsTgPppUserDb based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpLnsTgPppUserDb_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsTgPppUserDb_Object = MibTableColumn
tmnxL2tpLnsTgPppUserDb = _TmnxL2tpLnsTgPppUserDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 4),
    _TmnxL2tpLnsTgPppUserDb_Type()
)
tmnxL2tpLnsTgPppUserDb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppUserDb.setStatus("current")


class _TmnxL2tpLnsTgPppDefaultService_Type(TmnxServId):
    """Custom type tmnxL2tpLnsTgPppDefaultService based on TmnxServId"""
    defaultValue = 0


_TmnxL2tpLnsTgPppDefaultService_Type.__name__ = "TmnxServId"
_TmnxL2tpLnsTgPppDefaultService_Object = MibTableColumn
tmnxL2tpLnsTgPppDefaultService = _TmnxL2tpLnsTgPppDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 5),
    _TmnxL2tpLnsTgPppDefaultService_Type()
)
tmnxL2tpLnsTgPppDefaultService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppDefaultService.setStatus("current")


class _TmnxL2tpLnsTgPppDefaultGroupIf_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsTgPppDefaultGroupIf based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpLnsTgPppDefaultGroupIf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsTgPppDefaultGroupIf_Object = MibTableColumn
tmnxL2tpLnsTgPppDefaultGroupIf = _TmnxL2tpLnsTgPppDefaultGroupIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 6),
    _TmnxL2tpLnsTgPppDefaultGroupIf_Type()
)
tmnxL2tpLnsTgPppDefaultGroupIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppDefaultGroupIf.setStatus("current")


class _TmnxL2tpLnsTgPppProxyLcp_Type(TmnxAlwaysOrNever):
    """Custom type tmnxL2tpLnsTgPppProxyLcp based on TmnxAlwaysOrNever"""
    defaultValue = 2


_TmnxL2tpLnsTgPppProxyLcp_Type.__name__ = "TmnxAlwaysOrNever"
_TmnxL2tpLnsTgPppProxyLcp_Object = MibTableColumn
tmnxL2tpLnsTgPppProxyLcp = _TmnxL2tpLnsTgPppProxyLcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 7),
    _TmnxL2tpLnsTgPppProxyLcp_Type()
)
tmnxL2tpLnsTgPppProxyLcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppProxyLcp.setStatus("current")


class _TmnxL2tpLnsTgPppProxyAuth_Type(TmnxAlwaysOrNever):
    """Custom type tmnxL2tpLnsTgPppProxyAuth based on TmnxAlwaysOrNever"""
    defaultValue = 2


_TmnxL2tpLnsTgPppProxyAuth_Type.__name__ = "TmnxAlwaysOrNever"
_TmnxL2tpLnsTgPppProxyAuth_Object = MibTableColumn
tmnxL2tpLnsTgPppProxyAuth = _TmnxL2tpLnsTgPppProxyAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 8),
    _TmnxL2tpLnsTgPppProxyAuth_Type()
)
tmnxL2tpLnsTgPppProxyAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppProxyAuth.setStatus("current")


class _TmnxL2tpLnsTgPppMtu_Type(TmnxL2tpPppMtu):
    """Custom type tmnxL2tpLnsTgPppMtu based on TmnxL2tpPppMtu"""
    defaultValue = 1500


_TmnxL2tpLnsTgPppMtu_Type.__name__ = "TmnxL2tpPppMtu"
_TmnxL2tpLnsTgPppMtu_Object = MibTableColumn
tmnxL2tpLnsTgPppMtu = _TmnxL2tpLnsTgPppMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 9),
    _TmnxL2tpLnsTgPppMtu_Type()
)
tmnxL2tpLnsTgPppMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppMtu.setStatus("current")


class _TmnxL2tpLnsTgPppLcpKaInterval_Type(TmnxL2tpLcpKaInterval):
    """Custom type tmnxL2tpLnsTgPppLcpKaInterval based on TmnxL2tpLcpKaInterval"""
    defaultValue = 30


_TmnxL2tpLnsTgPppLcpKaInterval_Type.__name__ = "TmnxL2tpLcpKaInterval"
_TmnxL2tpLnsTgPppLcpKaInterval_Object = MibTableColumn
tmnxL2tpLnsTgPppLcpKaInterval = _TmnxL2tpLnsTgPppLcpKaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 10),
    _TmnxL2tpLnsTgPppLcpKaInterval_Type()
)
tmnxL2tpLnsTgPppLcpKaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppLcpKaInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppLcpKaInterval.setUnits("seconds")


class _TmnxL2tpLnsTgPppLcpKaHoldUp_Type(TmnxL2tpLcpKaHoldUpMplier):
    """Custom type tmnxL2tpLnsTgPppLcpKaHoldUp based on TmnxL2tpLcpKaHoldUpMplier"""
    defaultValue = 3


_TmnxL2tpLnsTgPppLcpKaHoldUp_Type.__name__ = "TmnxL2tpLcpKaHoldUpMplier"
_TmnxL2tpLnsTgPppLcpKaHoldUp_Object = MibTableColumn
tmnxL2tpLnsTgPppLcpKaHoldUp = _TmnxL2tpLnsTgPppLcpKaHoldUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 11),
    _TmnxL2tpLnsTgPppLcpKaHoldUp_Type()
)
tmnxL2tpLnsTgPppLcpKaHoldUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppLcpKaHoldUp.setStatus("current")


class _TmnxL2tpLnsTgPppIpcpSubnetNeg_Type(TmnxAlwaysOrNever):
    """Custom type tmnxL2tpLnsTgPppIpcpSubnetNeg based on TmnxAlwaysOrNever"""
    defaultValue = 2


_TmnxL2tpLnsTgPppIpcpSubnetNeg_Type.__name__ = "TmnxAlwaysOrNever"
_TmnxL2tpLnsTgPppIpcpSubnetNeg_Object = MibTableColumn
tmnxL2tpLnsTgPppIpcpSubnetNeg = _TmnxL2tpLnsTgPppIpcpSubnetNeg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 13),
    _TmnxL2tpLnsTgPppIpcpSubnetNeg_Type()
)
tmnxL2tpLnsTgPppIpcpSubnetNeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppIpcpSubnetNeg.setStatus("current")


class _TmnxL2tpLnsTgPppLcpIgnoreMagic_Type(TmnxAlwaysOrNever):
    """Custom type tmnxL2tpLnsTgPppLcpIgnoreMagic based on TmnxAlwaysOrNever"""
    defaultValue = 2


_TmnxL2tpLnsTgPppLcpIgnoreMagic_Type.__name__ = "TmnxAlwaysOrNever"
_TmnxL2tpLnsTgPppLcpIgnoreMagic_Object = MibTableColumn
tmnxL2tpLnsTgPppLcpIgnoreMagic = _TmnxL2tpLnsTgPppLcpIgnoreMagic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 20),
    _TmnxL2tpLnsTgPppLcpIgnoreMagic_Type()
)
tmnxL2tpLnsTgPppLcpIgnoreMagic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppLcpIgnoreMagic.setStatus("current")


class _TmnxL2tpLnsTgPppMinChapChall_Type(Unsigned32):
    """Custom type tmnxL2tpLnsTgPppMinChapChall based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 64),
    )


_TmnxL2tpLnsTgPppMinChapChall_Type.__name__ = "Unsigned32"
_TmnxL2tpLnsTgPppMinChapChall_Object = MibTableColumn
tmnxL2tpLnsTgPppMinChapChall = _TmnxL2tpLnsTgPppMinChapChall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 21),
    _TmnxL2tpLnsTgPppMinChapChall_Type()
)
tmnxL2tpLnsTgPppMinChapChall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppMinChapChall.setStatus("current")


class _TmnxL2tpLnsTgPppMaxChapChall_Type(Unsigned32):
    """Custom type tmnxL2tpLnsTgPppMaxChapChall based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 64),
    )


_TmnxL2tpLnsTgPppMaxChapChall_Type.__name__ = "Unsigned32"
_TmnxL2tpLnsTgPppMaxChapChall_Object = MibTableColumn
tmnxL2tpLnsTgPppMaxChapChall = _TmnxL2tpLnsTgPppMaxChapChall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 3, 1, 22),
    _TmnxL2tpLnsTgPppMaxChapChall_Type()
)
tmnxL2tpLnsTgPppMaxChapChall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppMaxChapChall.setStatus("current")
_TmnxL2tpTgMlpppTable_Object = MibTable
tmnxL2tpTgMlpppTable = _TmnxL2tpTgMlpppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppTable.setStatus("current")
_TmnxL2tpTgMlpppEntry_Object = MibTableRow
tmnxL2tpTgMlpppEntry = _TmnxL2tpTgMlpppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppEntry.setStatus("current")
_TmnxL2tpTgMlpppLastMgmtChange_Type = TimeStamp
_TmnxL2tpTgMlpppLastMgmtChange_Object = MibTableColumn
tmnxL2tpTgMlpppLastMgmtChange = _TmnxL2tpTgMlpppLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 1),
    _TmnxL2tpTgMlpppLastMgmtChange_Type()
)
tmnxL2tpTgMlpppLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppLastMgmtChange.setStatus("current")


class _TmnxL2tpTgMlpppAdminState_Type(TmnxAdminState):
    """Custom type tmnxL2tpTgMlpppAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxL2tpTgMlpppAdminState_Type.__name__ = "TmnxAdminState"
_TmnxL2tpTgMlpppAdminState_Object = MibTableColumn
tmnxL2tpTgMlpppAdminState = _TmnxL2tpTgMlpppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 2),
    _TmnxL2tpTgMlpppAdminState_Type()
)
tmnxL2tpTgMlpppAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppAdminState.setStatus("current")


class _TmnxL2tpTgMlpppMaxLinks_Type(Unsigned32):
    """Custom type tmnxL2tpTgMlpppMaxLinks based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxL2tpTgMlpppMaxLinks_Type.__name__ = "Unsigned32"
_TmnxL2tpTgMlpppMaxLinks_Object = MibTableColumn
tmnxL2tpTgMlpppMaxLinks = _TmnxL2tpTgMlpppMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 3),
    _TmnxL2tpTgMlpppMaxLinks_Type()
)
tmnxL2tpTgMlpppMaxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppMaxLinks.setStatus("current")


class _TmnxL2tpTgMlpppInterleave_Type(TmnxAlwaysOrNever):
    """Custom type tmnxL2tpTgMlpppInterleave based on TmnxAlwaysOrNever"""
    defaultValue = 2


_TmnxL2tpTgMlpppInterleave_Type.__name__ = "TmnxAlwaysOrNever"
_TmnxL2tpTgMlpppInterleave_Object = MibTableColumn
tmnxL2tpTgMlpppInterleave = _TmnxL2tpTgMlpppInterleave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 4),
    _TmnxL2tpTgMlpppInterleave_Type()
)
tmnxL2tpTgMlpppInterleave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppInterleave.setStatus("current")


class _TmnxL2tpTgMlpppMaxFragDelay_Type(TmnxL2tpMlpppMaxFragDelay):
    """Custom type tmnxL2tpTgMlpppMaxFragDelay based on TmnxL2tpMlpppMaxFragDelay"""
    defaultValue = 0


_TmnxL2tpTgMlpppMaxFragDelay_Type.__name__ = "TmnxL2tpMlpppMaxFragDelay"
_TmnxL2tpTgMlpppMaxFragDelay_Object = MibTableColumn
tmnxL2tpTgMlpppMaxFragDelay = _TmnxL2tpTgMlpppMaxFragDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 5),
    _TmnxL2tpTgMlpppMaxFragDelay_Type()
)
tmnxL2tpTgMlpppMaxFragDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppMaxFragDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppMaxFragDelay.setUnits("milliseconds")


class _TmnxL2tpTgMlpppReassemblyTo_Type(TmnxL2tpMlpppReassemblyTimeout):
    """Custom type tmnxL2tpTgMlpppReassemblyTo based on TmnxL2tpMlpppReassemblyTimeout"""
    defaultValue = 1000

    subtypeSpec = TmnxL2tpMlpppReassemblyTimeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_TmnxL2tpTgMlpppReassemblyTo_Type.__name__ = "TmnxL2tpMlpppReassemblyTimeout"
_TmnxL2tpTgMlpppReassemblyTo_Object = MibTableColumn
tmnxL2tpTgMlpppReassemblyTo = _TmnxL2tpTgMlpppReassemblyTo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 6),
    _TmnxL2tpTgMlpppReassemblyTo_Type()
)
tmnxL2tpTgMlpppReassemblyTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppReassemblyTo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppReassemblyTo.setUnits("milliseconds")


class _TmnxL2tpTgMlpppShortSeqNumberRx_Type(TmnxAlwaysOrNever):
    """Custom type tmnxL2tpTgMlpppShortSeqNumberRx based on TmnxAlwaysOrNever"""
    defaultValue = 2


_TmnxL2tpTgMlpppShortSeqNumberRx_Type.__name__ = "TmnxAlwaysOrNever"
_TmnxL2tpTgMlpppShortSeqNumberRx_Object = MibTableColumn
tmnxL2tpTgMlpppShortSeqNumberRx = _TmnxL2tpTgMlpppShortSeqNumberRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 7),
    _TmnxL2tpTgMlpppShortSeqNumberRx_Type()
)
tmnxL2tpTgMlpppShortSeqNumberRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppShortSeqNumberRx.setStatus("current")


class _TmnxL2tpTgMlpppEpClass_Type(TmnxL2tpMlpppEndpointClass):
    """Custom type tmnxL2tpTgMlpppEpClass based on TmnxL2tpMlpppEndpointClass"""
    defaultValue = 0


_TmnxL2tpTgMlpppEpClass_Type.__name__ = "TmnxL2tpMlpppEndpointClass"
_TmnxL2tpTgMlpppEpClass_Object = MibTableColumn
tmnxL2tpTgMlpppEpClass = _TmnxL2tpTgMlpppEpClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 8),
    _TmnxL2tpTgMlpppEpClass_Type()
)
tmnxL2tpTgMlpppEpClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppEpClass.setStatus("current")
_TmnxL2tpTgMlpppEpIpv4Address_Type = InetAddressIPv4
_TmnxL2tpTgMlpppEpIpv4Address_Object = MibTableColumn
tmnxL2tpTgMlpppEpIpv4Address = _TmnxL2tpTgMlpppEpIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 9),
    _TmnxL2tpTgMlpppEpIpv4Address_Type()
)
tmnxL2tpTgMlpppEpIpv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppEpIpv4Address.setStatus("current")
_TmnxL2tpTgMlpppEpMacAddress_Type = MacAddress
_TmnxL2tpTgMlpppEpMacAddress_Object = MibTableColumn
tmnxL2tpTgMlpppEpMacAddress = _TmnxL2tpTgMlpppEpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 4, 1, 10),
    _TmnxL2tpTgMlpppEpMacAddress_Type()
)
tmnxL2tpTgMlpppEpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgMlpppEpMacAddress.setStatus("current")
_TmnxL2tpTgXtTable_Object = MibTable
tmnxL2tpTgXtTable = _TmnxL2tpTgXtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgXtTable.setStatus("current")
_TmnxL2tpTgXtEntry_Object = MibTableRow
tmnxL2tpTgXtEntry = _TmnxL2tpTgXtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgXtEntry.setStatus("current")
_TmnxL2tpTgXtLastMgmtChange_Type = TimeStamp
_TmnxL2tpTgXtLastMgmtChange_Object = MibTableColumn
tmnxL2tpTgXtLastMgmtChange = _TmnxL2tpTgXtLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 5, 1, 1),
    _TmnxL2tpTgXtLastMgmtChange_Type()
)
tmnxL2tpTgXtLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgXtLastMgmtChange.setStatus("current")


class _TmnxL2tpTgXtDfBitLac_Type(TmnxAlwaysNeverOrDefault):
    """Custom type tmnxL2tpTgXtDfBitLac based on TmnxAlwaysNeverOrDefault"""
    defaultValue = 1


_TmnxL2tpTgXtDfBitLac_Type.__name__ = "TmnxAlwaysNeverOrDefault"
_TmnxL2tpTgXtDfBitLac_Object = MibTableColumn
tmnxL2tpTgXtDfBitLac = _TmnxL2tpTgXtDfBitLac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 1, 5, 1, 4),
    _TmnxL2tpTgXtDfBitLac_Type()
)
tmnxL2tpTgXtDfBitLac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTgXtDfBitLac.setStatus("current")
_TmnxL2tpTgStatObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpTgStatObjs = _TmnxL2tpTgStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2)
)
_TmnxL2tpTgStatTable_Object = MibTable
tmnxL2tpTgStatTable = _TmnxL2tpTgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgStatTable.setStatus("current")
_TmnxL2tpTgStatEntry_Object = MibTableRow
tmnxL2tpTgStatEntry = _TmnxL2tpTgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1)
)
tmnxL2tpTgStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTgStatName"),
)
if mibBuilder.loadTexts:
    tmnxL2tpTgStatEntry.setStatus("current")
_TmnxL2tpTgStatName_Type = TmnxL2tpTunnelGroupName
_TmnxL2tpTgStatName_Object = MibTableColumn
tmnxL2tpTgStatName = _TmnxL2tpTgStatName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 1),
    _TmnxL2tpTgStatName_Type()
)
tmnxL2tpTgStatName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatName.setStatus("current")
_TmnxL2tpTgStatState_Type = TmnxL2tpTgOperState
_TmnxL2tpTgStatState_Object = MibTableColumn
tmnxL2tpTgStatState = _TmnxL2tpTgStatState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 2),
    _TmnxL2tpTgStatState_Type()
)
tmnxL2tpTgStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatState.setStatus("current")
_TmnxL2tpTgStatCleared_Type = TimeStamp
_TmnxL2tpTgStatCleared_Object = MibTableColumn
tmnxL2tpTgStatCleared = _TmnxL2tpTgStatCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 3),
    _TmnxL2tpTgStatCleared_Type()
)
tmnxL2tpTgStatCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatCleared.setStatus("current")
_TmnxL2tpTgStatTotalTunnels_Type = Counter32
_TmnxL2tpTgStatTotalTunnels_Object = MibTableColumn
tmnxL2tpTgStatTotalTunnels = _TmnxL2tpTgStatTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 4),
    _TmnxL2tpTgStatTotalTunnels_Type()
)
tmnxL2tpTgStatTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatTotalTunnels.setStatus("current")
_TmnxL2tpTgStatFailedTunnels_Type = Counter32
_TmnxL2tpTgStatFailedTunnels_Object = MibTableColumn
tmnxL2tpTgStatFailedTunnels = _TmnxL2tpTgStatFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 5),
    _TmnxL2tpTgStatFailedTunnels_Type()
)
tmnxL2tpTgStatFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatFailedTunnels.setStatus("current")
_TmnxL2tpTgStatFailedTuAuth_Type = Counter32
_TmnxL2tpTgStatFailedTuAuth_Object = MibTableColumn
tmnxL2tpTgStatFailedTuAuth = _TmnxL2tpTgStatFailedTuAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 6),
    _TmnxL2tpTgStatFailedTuAuth_Type()
)
tmnxL2tpTgStatFailedTuAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatFailedTuAuth.setStatus("current")
_TmnxL2tpTgStatActiveTunnels_Type = Gauge32
_TmnxL2tpTgStatActiveTunnels_Object = MibTableColumn
tmnxL2tpTgStatActiveTunnels = _TmnxL2tpTgStatActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 7),
    _TmnxL2tpTgStatActiveTunnels_Type()
)
tmnxL2tpTgStatActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatActiveTunnels.setStatus("current")
_TmnxL2tpTgStatTunnels_Type = Gauge32
_TmnxL2tpTgStatTunnels_Object = MibTableColumn
tmnxL2tpTgStatTunnels = _TmnxL2tpTgStatTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 8),
    _TmnxL2tpTgStatTunnels_Type()
)
tmnxL2tpTgStatTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatTunnels.setStatus("current")
_TmnxL2tpTgStatTotalSessions_Type = Counter32
_TmnxL2tpTgStatTotalSessions_Object = MibTableColumn
tmnxL2tpTgStatTotalSessions = _TmnxL2tpTgStatTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 9),
    _TmnxL2tpTgStatTotalSessions_Type()
)
tmnxL2tpTgStatTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatTotalSessions.setStatus("current")
_TmnxL2tpTgStatFailedSessions_Type = Counter32
_TmnxL2tpTgStatFailedSessions_Object = MibTableColumn
tmnxL2tpTgStatFailedSessions = _TmnxL2tpTgStatFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 10),
    _TmnxL2tpTgStatFailedSessions_Type()
)
tmnxL2tpTgStatFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatFailedSessions.setStatus("current")
_TmnxL2tpTgStatActiveSessions_Type = Gauge32
_TmnxL2tpTgStatActiveSessions_Object = MibTableColumn
tmnxL2tpTgStatActiveSessions = _TmnxL2tpTgStatActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 11),
    _TmnxL2tpTgStatActiveSessions_Type()
)
tmnxL2tpTgStatActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatActiveSessions.setStatus("current")
_TmnxL2tpTgStatSessions_Type = Gauge32
_TmnxL2tpTgStatSessions_Object = MibTableColumn
tmnxL2tpTgStatSessions = _TmnxL2tpTgStatSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 12),
    _TmnxL2tpTgStatSessions_Type()
)
tmnxL2tpTgStatSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatSessions.setStatus("current")
_TmnxL2tpTgStatControlRxOctets_Type = CounterBasedGauge64
_TmnxL2tpTgStatControlRxOctets_Object = MibTableColumn
tmnxL2tpTgStatControlRxOctets = _TmnxL2tpTgStatControlRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 13),
    _TmnxL2tpTgStatControlRxOctets_Type()
)
tmnxL2tpTgStatControlRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatControlRxOctets.setStatus("current")
_TmnxL2tpTgStatControlRxOctetsLw_Type = Gauge32
_TmnxL2tpTgStatControlRxOctetsLw_Object = MibTableColumn
tmnxL2tpTgStatControlRxOctetsLw = _TmnxL2tpTgStatControlRxOctetsLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 14),
    _TmnxL2tpTgStatControlRxOctetsLw_Type()
)
tmnxL2tpTgStatControlRxOctetsLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatControlRxOctetsLw.setStatus("current")
_TmnxL2tpTgStatControlRxOctetsHw_Type = Gauge32
_TmnxL2tpTgStatControlRxOctetsHw_Object = MibTableColumn
tmnxL2tpTgStatControlRxOctetsHw = _TmnxL2tpTgStatControlRxOctetsHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 15),
    _TmnxL2tpTgStatControlRxOctetsHw_Type()
)
tmnxL2tpTgStatControlRxOctetsHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatControlRxOctetsHw.setStatus("current")
_TmnxL2tpTgStatControlRxPkts_Type = Gauge32
_TmnxL2tpTgStatControlRxPkts_Object = MibTableColumn
tmnxL2tpTgStatControlRxPkts = _TmnxL2tpTgStatControlRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 16),
    _TmnxL2tpTgStatControlRxPkts_Type()
)
tmnxL2tpTgStatControlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatControlRxPkts.setStatus("current")
_TmnxL2tpTgStatControlTxOctets_Type = CounterBasedGauge64
_TmnxL2tpTgStatControlTxOctets_Object = MibTableColumn
tmnxL2tpTgStatControlTxOctets = _TmnxL2tpTgStatControlTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 17),
    _TmnxL2tpTgStatControlTxOctets_Type()
)
tmnxL2tpTgStatControlTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatControlTxOctets.setStatus("current")
_TmnxL2tpTgStatControlTxOctetsLw_Type = Gauge32
_TmnxL2tpTgStatControlTxOctetsLw_Object = MibTableColumn
tmnxL2tpTgStatControlTxOctetsLw = _TmnxL2tpTgStatControlTxOctetsLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 18),
    _TmnxL2tpTgStatControlTxOctetsLw_Type()
)
tmnxL2tpTgStatControlTxOctetsLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatControlTxOctetsLw.setStatus("current")
_TmnxL2tpTgStatControlTxOctetsHw_Type = Gauge32
_TmnxL2tpTgStatControlTxOctetsHw_Object = MibTableColumn
tmnxL2tpTgStatControlTxOctetsHw = _TmnxL2tpTgStatControlTxOctetsHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 19),
    _TmnxL2tpTgStatControlTxOctetsHw_Type()
)
tmnxL2tpTgStatControlTxOctetsHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatControlTxOctetsHw.setStatus("current")
_TmnxL2tpTgStatControlTxPkts_Type = Gauge32
_TmnxL2tpTgStatControlTxPkts_Object = MibTableColumn
tmnxL2tpTgStatControlTxPkts = _TmnxL2tpTgStatControlTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 20),
    _TmnxL2tpTgStatControlTxPkts_Type()
)
tmnxL2tpTgStatControlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatControlTxPkts.setStatus("current")
_TmnxL2tpTgStatErrorTxPkts_Type = Gauge32
_TmnxL2tpTgStatErrorTxPkts_Object = MibTableColumn
tmnxL2tpTgStatErrorTxPkts = _TmnxL2tpTgStatErrorTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 21),
    _TmnxL2tpTgStatErrorTxPkts_Type()
)
tmnxL2tpTgStatErrorTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatErrorTxPkts.setStatus("current")
_TmnxL2tpTgStatErrorRxPkts_Type = Gauge32
_TmnxL2tpTgStatErrorRxPkts_Object = MibTableColumn
tmnxL2tpTgStatErrorRxPkts = _TmnxL2tpTgStatErrorRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 22),
    _TmnxL2tpTgStatErrorRxPkts_Type()
)
tmnxL2tpTgStatErrorRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatErrorRxPkts.setStatus("current")
_TmnxL2tpTgStatSessionLimit_Type = Gauge32
_TmnxL2tpTgStatSessionLimit_Object = MibTableColumn
tmnxL2tpTgStatSessionLimit = _TmnxL2tpTgStatSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 23),
    _TmnxL2tpTgStatSessionLimit_Type()
)
tmnxL2tpTgStatSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatSessionLimit.setStatus("current")
_TmnxL2tpTgStatSeAssignMethod_Type = TmnxL2tpSessionAssignMethod
_TmnxL2tpTgStatSeAssignMethod_Object = MibTableColumn
tmnxL2tpTgStatSeAssignMethod = _TmnxL2tpTgStatSeAssignMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 1, 1, 24),
    _TmnxL2tpTgStatSeAssignMethod_Type()
)
tmnxL2tpTgStatSeAssignMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgStatSeAssignMethod.setStatus("current")
_TmnxL2tpTgTuTable_Object = MibTable
tmnxL2tpTgTuTable = _TmnxL2tpTgTuTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgTuTable.setStatus("current")
_TmnxL2tpTgTuEntry_Object = MibTableRow
tmnxL2tpTgTuEntry = _TmnxL2tpTgTuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 2, 1)
)
tmnxL2tpTgTuEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTgStatName"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTgTuId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpTgTuEntry.setStatus("current")
_TmnxL2tpTgTuId_Type = TmnxL2tpConnectionId
_TmnxL2tpTgTuId_Object = MibTableColumn
tmnxL2tpTgTuId = _TmnxL2tpTgTuId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 2, 2, 1, 1),
    _TmnxL2tpTgTuId_Type()
)
tmnxL2tpTgTuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgTuId.setStatus("current")
_TmnxL2tpTgOpObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpTgOpObjs = _TmnxL2tpTgOpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 3)
)
_TmnxL2tpTgDrainTable_Object = MibTable
tmnxL2tpTgDrainTable = _TmnxL2tpTgDrainTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgDrainTable.setStatus("current")
_TmnxL2tpTgDrainEntry_Object = MibTableRow
tmnxL2tpTgDrainEntry = _TmnxL2tpTgDrainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTgDrainEntry.setStatus("current")


class _TmnxL2tpTgDrain_Type(TmnxL2tpActionTypeDrain):
    """Custom type tmnxL2tpTgDrain based on TmnxL2tpActionTypeDrain"""
    defaultValue = 2


_TmnxL2tpTgDrain_Type.__name__ = "TmnxL2tpActionTypeDrain"
_TmnxL2tpTgDrain_Object = MibTableColumn
tmnxL2tpTgDrain = _TmnxL2tpTgDrain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 2, 3, 1, 1, 1),
    _TmnxL2tpTgDrain_Type()
)
tmnxL2tpTgDrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxL2tpTgDrain.setStatus("current")
_TmnxL2tpTunnelObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpTunnelObjs = _TmnxL2tpTunnelObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3)
)
_TmnxL2tpTuCfgObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpTuCfgObjs = _TmnxL2tpTuCfgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1)
)
_TmnxL2tpTuCfgTable_Object = MibTable
tmnxL2tpTuCfgTable = _TmnxL2tpTuCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgTable.setStatus("current")
_TmnxL2tpTuCfgEntry_Object = MibTableRow
tmnxL2tpTuCfgEntry = _TmnxL2tpTuCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1)
)
tmnxL2tpTuCfgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgName"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgName"),
)
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgEntry.setStatus("current")
_TmnxL2tpTuCfgName_Type = TNamedItem
_TmnxL2tpTuCfgName_Object = MibTableColumn
tmnxL2tpTuCfgName = _TmnxL2tpTuCfgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 1),
    _TmnxL2tpTuCfgName_Type()
)
tmnxL2tpTuCfgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgName.setStatus("current")
_TmnxL2tpTuCfgRowStatus_Type = RowStatus
_TmnxL2tpTuCfgRowStatus_Object = MibTableColumn
tmnxL2tpTuCfgRowStatus = _TmnxL2tpTuCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 2),
    _TmnxL2tpTuCfgRowStatus_Type()
)
tmnxL2tpTuCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgRowStatus.setStatus("current")
_TmnxL2tpTuCfgLastMgmtChange_Type = TimeStamp
_TmnxL2tpTuCfgLastMgmtChange_Object = MibTableColumn
tmnxL2tpTuCfgLastMgmtChange = _TmnxL2tpTuCfgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 3),
    _TmnxL2tpTuCfgLastMgmtChange_Type()
)
tmnxL2tpTuCfgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgLastMgmtChange.setStatus("current")


class _TmnxL2tpTuCfgDescription_Type(TItemDescription):
    """Custom type tmnxL2tpTuCfgDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxL2tpTuCfgDescription_Type.__name__ = "TItemDescription"
_TmnxL2tpTuCfgDescription_Object = MibTableColumn
tmnxL2tpTuCfgDescription = _TmnxL2tpTuCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 4),
    _TmnxL2tpTuCfgDescription_Type()
)
tmnxL2tpTuCfgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgDescription.setStatus("current")


class _TmnxL2tpTuCfgAdminState_Type(TmnxAdminState):
    """Custom type tmnxL2tpTuCfgAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxL2tpTuCfgAdminState_Type.__name__ = "TmnxAdminState"
_TmnxL2tpTuCfgAdminState_Object = MibTableColumn
tmnxL2tpTuCfgAdminState = _TmnxL2tpTuCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 5),
    _TmnxL2tpTuCfgAdminState_Type()
)
tmnxL2tpTuCfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgAdminState.setStatus("current")


class _TmnxL2tpTuCfgPreference_Type(TmnxL2tpTunnelPreference):
    """Custom type tmnxL2tpTuCfgPreference based on TmnxL2tpTunnelPreference"""
    defaultValue = 50


_TmnxL2tpTuCfgPreference_Type.__name__ = "TmnxL2tpTunnelPreference"
_TmnxL2tpTuCfgPreference_Object = MibTableColumn
tmnxL2tpTuCfgPreference = _TmnxL2tpTuCfgPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 6),
    _TmnxL2tpTuCfgPreference_Type()
)
tmnxL2tpTuCfgPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgPreference.setStatus("current")


class _TmnxL2tpTuCfgPeerAddrType_Type(InetAddressType):
    """Custom type tmnxL2tpTuCfgPeerAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxL2tpTuCfgPeerAddrType_Type.__name__ = "InetAddressType"
_TmnxL2tpTuCfgPeerAddrType_Object = MibTableColumn
tmnxL2tpTuCfgPeerAddrType = _TmnxL2tpTuCfgPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 7),
    _TmnxL2tpTuCfgPeerAddrType_Type()
)
tmnxL2tpTuCfgPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgPeerAddrType.setStatus("current")


class _TmnxL2tpTuCfgPeerAddr_Type(InetAddress):
    """Custom type tmnxL2tpTuCfgPeerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpTuCfgPeerAddr_Type.__name__ = "InetAddress"
_TmnxL2tpTuCfgPeerAddr_Object = MibTableColumn
tmnxL2tpTuCfgPeerAddr = _TmnxL2tpTuCfgPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 8),
    _TmnxL2tpTuCfgPeerAddr_Type()
)
tmnxL2tpTuCfgPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgPeerAddr.setStatus("current")


class _TmnxL2tpTuCfgAddrType_Type(InetAddressType):
    """Custom type tmnxL2tpTuCfgAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxL2tpTuCfgAddrType_Type.__name__ = "InetAddressType"
_TmnxL2tpTuCfgAddrType_Object = MibTableColumn
tmnxL2tpTuCfgAddrType = _TmnxL2tpTuCfgAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 9),
    _TmnxL2tpTuCfgAddrType_Type()
)
tmnxL2tpTuCfgAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgAddrType.setStatus("current")


class _TmnxL2tpTuCfgAddr_Type(InetAddress):
    """Custom type tmnxL2tpTuCfgAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpTuCfgAddr_Type.__name__ = "InetAddress"
_TmnxL2tpTuCfgAddr_Object = MibTableColumn
tmnxL2tpTuCfgAddr = _TmnxL2tpTuCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 10),
    _TmnxL2tpTuCfgAddr_Type()
)
tmnxL2tpTuCfgAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgAddr.setStatus("current")


class _TmnxL2tpTuCfgLocalName_Type(TmnxL2tpHostNameOrEmpty):
    """Custom type tmnxL2tpTuCfgLocalName based on TmnxL2tpHostNameOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpTuCfgLocalName_Type.__name__ = "TmnxL2tpHostNameOrEmpty"
_TmnxL2tpTuCfgLocalName_Object = MibTableColumn
tmnxL2tpTuCfgLocalName = _TmnxL2tpTuCfgLocalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 11),
    _TmnxL2tpTuCfgLocalName_Type()
)
tmnxL2tpTuCfgLocalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgLocalName.setStatus("current")


class _TmnxL2tpTuCfgRemoteName_Type(TmnxL2tpHostNameOrEmpty):
    """Custom type tmnxL2tpTuCfgRemoteName based on TmnxL2tpHostNameOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpTuCfgRemoteName_Type.__name__ = "TmnxL2tpHostNameOrEmpty"
_TmnxL2tpTuCfgRemoteName_Object = MibTableColumn
tmnxL2tpTuCfgRemoteName = _TmnxL2tpTuCfgRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 12),
    _TmnxL2tpTuCfgRemoteName_Type()
)
tmnxL2tpTuCfgRemoteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgRemoteName.setStatus("current")


class _TmnxL2tpTuCfgSecret_Type(TmnxL2tpAuthSecret):
    """Custom type tmnxL2tpTuCfgSecret based on TmnxL2tpAuthSecret"""
    defaultHexValue = ""


_TmnxL2tpTuCfgSecret_Type.__name__ = "TmnxL2tpAuthSecret"
_TmnxL2tpTuCfgSecret_Object = MibTableColumn
tmnxL2tpTuCfgSecret = _TmnxL2tpTuCfgSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 13),
    _TmnxL2tpTuCfgSecret_Type()
)
tmnxL2tpTuCfgSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgSecret.setStatus("current")


class _TmnxL2tpTuCfgHelloInterval_Type(TmnxL2tpTunnelHelloInterval):
    """Custom type tmnxL2tpTuCfgHelloInterval based on TmnxL2tpTunnelHelloInterval"""
    defaultValue = -2


_TmnxL2tpTuCfgHelloInterval_Type.__name__ = "TmnxL2tpTunnelHelloInterval"
_TmnxL2tpTuCfgHelloInterval_Object = MibTableColumn
tmnxL2tpTuCfgHelloInterval = _TmnxL2tpTuCfgHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 14),
    _TmnxL2tpTuCfgHelloInterval_Type()
)
tmnxL2tpTuCfgHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgHelloInterval.setUnits("seconds")


class _TmnxL2tpTuCfgIdleTO_Type(TmnxL2tpTunnelIdleTO):
    """Custom type tmnxL2tpTuCfgIdleTO based on TmnxL2tpTunnelIdleTO"""
    defaultValue = -2


_TmnxL2tpTuCfgIdleTO_Type.__name__ = "TmnxL2tpTunnelIdleTO"
_TmnxL2tpTuCfgIdleTO_Object = MibTableColumn
tmnxL2tpTuCfgIdleTO = _TmnxL2tpTuCfgIdleTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 15),
    _TmnxL2tpTuCfgIdleTO_Type()
)
tmnxL2tpTuCfgIdleTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgIdleTO.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgIdleTO.setUnits("seconds")


class _TmnxL2tpTuCfgDestructTO_Type(TmnxL2tpTunnelDestructTO):
    """Custom type tmnxL2tpTuCfgDestructTO based on TmnxL2tpTunnelDestructTO"""
    defaultValue = -2


_TmnxL2tpTuCfgDestructTO_Type.__name__ = "TmnxL2tpTunnelDestructTO"
_TmnxL2tpTuCfgDestructTO_Object = MibTableColumn
tmnxL2tpTuCfgDestructTO = _TmnxL2tpTuCfgDestructTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 16),
    _TmnxL2tpTuCfgDestructTO_Type()
)
tmnxL2tpTuCfgDestructTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgDestructTO.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgDestructTO.setUnits("seconds")


class _TmnxL2tpTuCfgMaxRetxEstab_Type(TmnxL2tpTunnelMaxRetx):
    """Custom type tmnxL2tpTuCfgMaxRetxEstab based on TmnxL2tpTunnelMaxRetx"""
    defaultValue = -2


_TmnxL2tpTuCfgMaxRetxEstab_Type.__name__ = "TmnxL2tpTunnelMaxRetx"
_TmnxL2tpTuCfgMaxRetxEstab_Object = MibTableColumn
tmnxL2tpTuCfgMaxRetxEstab = _TmnxL2tpTuCfgMaxRetxEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 17),
    _TmnxL2tpTuCfgMaxRetxEstab_Type()
)
tmnxL2tpTuCfgMaxRetxEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgMaxRetxEstab.setStatus("current")


class _TmnxL2tpTuCfgMaxRetxNotEstab_Type(TmnxL2tpTunnelMaxRetx):
    """Custom type tmnxL2tpTuCfgMaxRetxNotEstab based on TmnxL2tpTunnelMaxRetx"""
    defaultValue = -2


_TmnxL2tpTuCfgMaxRetxNotEstab_Type.__name__ = "TmnxL2tpTunnelMaxRetx"
_TmnxL2tpTuCfgMaxRetxNotEstab_Object = MibTableColumn
tmnxL2tpTuCfgMaxRetxNotEstab = _TmnxL2tpTuCfgMaxRetxNotEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 18),
    _TmnxL2tpTuCfgMaxRetxNotEstab_Type()
)
tmnxL2tpTuCfgMaxRetxNotEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgMaxRetxNotEstab.setStatus("current")


class _TmnxL2tpTuCfgSessionLimit_Type(TmnxL2tpTunnelSessionLimit):
    """Custom type tmnxL2tpTuCfgSessionLimit based on TmnxL2tpTunnelSessionLimit"""
    defaultValue = -2


_TmnxL2tpTuCfgSessionLimit_Type.__name__ = "TmnxL2tpTunnelSessionLimit"
_TmnxL2tpTuCfgSessionLimit_Object = MibTableColumn
tmnxL2tpTuCfgSessionLimit = _TmnxL2tpTuCfgSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 19),
    _TmnxL2tpTuCfgSessionLimit_Type()
)
tmnxL2tpTuCfgSessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgSessionLimit.setStatus("current")


class _TmnxL2tpTuCfgAvpHiding_Type(TmnxL2tpAvpHidingMode):
    """Custom type tmnxL2tpTuCfgAvpHiding based on TmnxL2tpAvpHidingMode"""
    defaultValue = 1


_TmnxL2tpTuCfgAvpHiding_Type.__name__ = "TmnxL2tpAvpHidingMode"
_TmnxL2tpTuCfgAvpHiding_Object = MibTableColumn
tmnxL2tpTuCfgAvpHiding = _TmnxL2tpTuCfgAvpHiding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 20),
    _TmnxL2tpTuCfgAvpHiding_Type()
)
tmnxL2tpTuCfgAvpHiding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgAvpHiding.setStatus("current")


class _TmnxL2tpTuCfgAutoEstab_Type(TruthValue):
    """Custom type tmnxL2tpTuCfgAutoEstab based on TruthValue"""
    defaultValue = 2


_TmnxL2tpTuCfgAutoEstab_Type.__name__ = "TruthValue"
_TmnxL2tpTuCfgAutoEstab_Object = MibTableColumn
tmnxL2tpTuCfgAutoEstab = _TmnxL2tpTuCfgAutoEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 21),
    _TmnxL2tpTuCfgAutoEstab_Type()
)
tmnxL2tpTuCfgAutoEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgAutoEstab.setStatus("current")


class _TmnxL2tpTuCfgDoChallenge_Type(TmnxL2tpDoChallenge):
    """Custom type tmnxL2tpTuCfgDoChallenge based on TmnxL2tpDoChallenge"""
    defaultValue = 1


_TmnxL2tpTuCfgDoChallenge_Type.__name__ = "TmnxL2tpDoChallenge"
_TmnxL2tpTuCfgDoChallenge_Object = MibTableColumn
tmnxL2tpTuCfgDoChallenge = _TmnxL2tpTuCfgDoChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 22),
    _TmnxL2tpTuCfgDoChallenge_Type()
)
tmnxL2tpTuCfgDoChallenge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgDoChallenge.setStatus("current")


class _TmnxL2tpTuCfgReceiveWindowSize_Type(TmnxL2tpReceiveWindowSize):
    """Custom type tmnxL2tpTuCfgReceiveWindowSize based on TmnxL2tpReceiveWindowSize"""
    defaultValue = 0


_TmnxL2tpTuCfgReceiveWindowSize_Type.__name__ = "TmnxL2tpReceiveWindowSize"
_TmnxL2tpTuCfgReceiveWindowSize_Object = MibTableColumn
tmnxL2tpTuCfgReceiveWindowSize = _TmnxL2tpTuCfgReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 23),
    _TmnxL2tpTuCfgReceiveWindowSize_Type()
)
tmnxL2tpTuCfgReceiveWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgReceiveWindowSize.setStatus("current")


class _TmnxL2tpTuCfgIsaGrpId_Type(TmnxL2tpIsaGrpIdOrZero):
    """Custom type tmnxL2tpTuCfgIsaGrpId based on TmnxL2tpIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxL2tpTuCfgIsaGrpId_Type.__name__ = "TmnxL2tpIsaGrpIdOrZero"
_TmnxL2tpTuCfgIsaGrpId_Object = MibTableColumn
tmnxL2tpTuCfgIsaGrpId = _TmnxL2tpTuCfgIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 24),
    _TmnxL2tpTuCfgIsaGrpId_Type()
)
tmnxL2tpTuCfgIsaGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgIsaGrpId.setStatus("current")


class _TmnxL2tpTuCfgLoadBalanceMethod_Type(TmnxL2tpIsaMdaLoadBalanceMethod):
    """Custom type tmnxL2tpTuCfgLoadBalanceMethod based on TmnxL2tpIsaMdaLoadBalanceMethod"""
    defaultValue = 0


_TmnxL2tpTuCfgLoadBalanceMethod_Type.__name__ = "TmnxL2tpIsaMdaLoadBalanceMethod"
_TmnxL2tpTuCfgLoadBalanceMethod_Object = MibTableColumn
tmnxL2tpTuCfgLoadBalanceMethod = _TmnxL2tpTuCfgLoadBalanceMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 30),
    _TmnxL2tpTuCfgLoadBalanceMethod_Type()
)
tmnxL2tpTuCfgLoadBalanceMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgLoadBalanceMethod.setStatus("current")


class _TmnxL2tpTuCfgAccountingPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpTuCfgAccountingPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpTuCfgAccountingPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpTuCfgAccountingPolicy_Object = MibTableColumn
tmnxL2tpTuCfgAccountingPolicy = _TmnxL2tpTuCfgAccountingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 2, 1, 31),
    _TmnxL2tpTuCfgAccountingPolicy_Type()
)
tmnxL2tpTuCfgAccountingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgAccountingPolicy.setStatus("current")
_TmnxL2tpLnsTuPppTable_Object = MibTable
tmnxL2tpLnsTuPppTable = _TmnxL2tpLnsTuPppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppTable.setStatus("current")
_TmnxL2tpLnsTuPppEntry_Object = MibTableRow
tmnxL2tpLnsTuPppEntry = _TmnxL2tpLnsTuPppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppEntry.setStatus("current")
_TmnxL2tpLnsTuPppLastMgmtChange_Type = TimeStamp
_TmnxL2tpLnsTuPppLastMgmtChange_Object = MibTableColumn
tmnxL2tpLnsTuPppLastMgmtChange = _TmnxL2tpLnsTuPppLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 1),
    _TmnxL2tpLnsTuPppLastMgmtChange_Type()
)
tmnxL2tpLnsTuPppLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppLastMgmtChange.setStatus("current")


class _TmnxL2tpLnsTuPppAuthPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsTuPppAuthPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpLnsTuPppAuthPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsTuPppAuthPlcy_Object = MibTableColumn
tmnxL2tpLnsTuPppAuthPlcy = _TmnxL2tpLnsTuPppAuthPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 2),
    _TmnxL2tpLnsTuPppAuthPlcy_Type()
)
tmnxL2tpLnsTuPppAuthPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppAuthPlcy.setStatus("current")


class _TmnxL2tpLnsTuPppAuthProtocol_Type(TmnxL2tpPppAuthentication):
    """Custom type tmnxL2tpLnsTuPppAuthProtocol based on TmnxL2tpPppAuthentication"""
    defaultValue = 0


_TmnxL2tpLnsTuPppAuthProtocol_Type.__name__ = "TmnxL2tpPppAuthentication"
_TmnxL2tpLnsTuPppAuthProtocol_Object = MibTableColumn
tmnxL2tpLnsTuPppAuthProtocol = _TmnxL2tpLnsTuPppAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 3),
    _TmnxL2tpLnsTuPppAuthProtocol_Type()
)
tmnxL2tpLnsTuPppAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppAuthProtocol.setStatus("current")


class _TmnxL2tpLnsTuPppUserDb_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsTuPppUserDb based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxL2tpLnsTuPppUserDb_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsTuPppUserDb_Object = MibTableColumn
tmnxL2tpLnsTuPppUserDb = _TmnxL2tpLnsTuPppUserDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 4),
    _TmnxL2tpLnsTuPppUserDb_Type()
)
tmnxL2tpLnsTuPppUserDb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppUserDb.setStatus("current")


class _TmnxL2tpLnsTuPppDefaultService_Type(TmnxServId):
    """Custom type tmnxL2tpLnsTuPppDefaultService based on TmnxServId"""
    defaultValue = 0


_TmnxL2tpLnsTuPppDefaultService_Type.__name__ = "TmnxServId"
_TmnxL2tpLnsTuPppDefaultService_Object = MibTableColumn
tmnxL2tpLnsTuPppDefaultService = _TmnxL2tpLnsTuPppDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 5),
    _TmnxL2tpLnsTuPppDefaultService_Type()
)
tmnxL2tpLnsTuPppDefaultService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppDefaultService.setStatus("current")


class _TmnxL2tpLnsTuPppDefaultGroupIf_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsTuPppDefaultGroupIf based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpLnsTuPppDefaultGroupIf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsTuPppDefaultGroupIf_Object = MibTableColumn
tmnxL2tpLnsTuPppDefaultGroupIf = _TmnxL2tpLnsTuPppDefaultGroupIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 6),
    _TmnxL2tpLnsTuPppDefaultGroupIf_Type()
)
tmnxL2tpLnsTuPppDefaultGroupIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppDefaultGroupIf.setStatus("current")


class _TmnxL2tpLnsTuPppProxyLcp_Type(TmnxAlwaysNeverOrDefault):
    """Custom type tmnxL2tpLnsTuPppProxyLcp based on TmnxAlwaysNeverOrDefault"""
    defaultValue = 1


_TmnxL2tpLnsTuPppProxyLcp_Type.__name__ = "TmnxAlwaysNeverOrDefault"
_TmnxL2tpLnsTuPppProxyLcp_Object = MibTableColumn
tmnxL2tpLnsTuPppProxyLcp = _TmnxL2tpLnsTuPppProxyLcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 7),
    _TmnxL2tpLnsTuPppProxyLcp_Type()
)
tmnxL2tpLnsTuPppProxyLcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppProxyLcp.setStatus("current")


class _TmnxL2tpLnsTuPppProxyAuth_Type(TmnxAlwaysNeverOrDefault):
    """Custom type tmnxL2tpLnsTuPppProxyAuth based on TmnxAlwaysNeverOrDefault"""
    defaultValue = 1


_TmnxL2tpLnsTuPppProxyAuth_Type.__name__ = "TmnxAlwaysNeverOrDefault"
_TmnxL2tpLnsTuPppProxyAuth_Object = MibTableColumn
tmnxL2tpLnsTuPppProxyAuth = _TmnxL2tpLnsTuPppProxyAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 8),
    _TmnxL2tpLnsTuPppProxyAuth_Type()
)
tmnxL2tpLnsTuPppProxyAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppProxyAuth.setStatus("current")


class _TmnxL2tpLnsTuPppMtu_Type(TmnxL2tpPppMtu):
    """Custom type tmnxL2tpLnsTuPppMtu based on TmnxL2tpPppMtu"""
    defaultValue = 0


_TmnxL2tpLnsTuPppMtu_Type.__name__ = "TmnxL2tpPppMtu"
_TmnxL2tpLnsTuPppMtu_Object = MibTableColumn
tmnxL2tpLnsTuPppMtu = _TmnxL2tpLnsTuPppMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 9),
    _TmnxL2tpLnsTuPppMtu_Type()
)
tmnxL2tpLnsTuPppMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppMtu.setStatus("current")


class _TmnxL2tpLnsTuPppLcpKaInterval_Type(TmnxL2tpLcpKaInterval):
    """Custom type tmnxL2tpLnsTuPppLcpKaInterval based on TmnxL2tpLcpKaInterval"""
    defaultValue = 0


_TmnxL2tpLnsTuPppLcpKaInterval_Type.__name__ = "TmnxL2tpLcpKaInterval"
_TmnxL2tpLnsTuPppLcpKaInterval_Object = MibTableColumn
tmnxL2tpLnsTuPppLcpKaInterval = _TmnxL2tpLnsTuPppLcpKaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 10),
    _TmnxL2tpLnsTuPppLcpKaInterval_Type()
)
tmnxL2tpLnsTuPppLcpKaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppLcpKaInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppLcpKaInterval.setUnits("seconds")


class _TmnxL2tpLnsTuPppLcpKaHoldUp_Type(TmnxL2tpLcpKaHoldUpMplier):
    """Custom type tmnxL2tpLnsTuPppLcpKaHoldUp based on TmnxL2tpLcpKaHoldUpMplier"""
    defaultValue = 0


_TmnxL2tpLnsTuPppLcpKaHoldUp_Type.__name__ = "TmnxL2tpLcpKaHoldUpMplier"
_TmnxL2tpLnsTuPppLcpKaHoldUp_Object = MibTableColumn
tmnxL2tpLnsTuPppLcpKaHoldUp = _TmnxL2tpLnsTuPppLcpKaHoldUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 11),
    _TmnxL2tpLnsTuPppLcpKaHoldUp_Type()
)
tmnxL2tpLnsTuPppLcpKaHoldUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppLcpKaHoldUp.setStatus("current")


class _TmnxL2tpLnsTuPppIpcpSubnetNeg_Type(TmnxAlwaysNeverOrDefault):
    """Custom type tmnxL2tpLnsTuPppIpcpSubnetNeg based on TmnxAlwaysNeverOrDefault"""
    defaultValue = 1


_TmnxL2tpLnsTuPppIpcpSubnetNeg_Type.__name__ = "TmnxAlwaysNeverOrDefault"
_TmnxL2tpLnsTuPppIpcpSubnetNeg_Object = MibTableColumn
tmnxL2tpLnsTuPppIpcpSubnetNeg = _TmnxL2tpLnsTuPppIpcpSubnetNeg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 13),
    _TmnxL2tpLnsTuPppIpcpSubnetNeg_Type()
)
tmnxL2tpLnsTuPppIpcpSubnetNeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppIpcpSubnetNeg.setStatus("current")


class _TmnxL2tpLnsTuPppLcpIgnoreMagic_Type(TmnxAlwaysNeverOrDefault):
    """Custom type tmnxL2tpLnsTuPppLcpIgnoreMagic based on TmnxAlwaysNeverOrDefault"""
    defaultValue = 1


_TmnxL2tpLnsTuPppLcpIgnoreMagic_Type.__name__ = "TmnxAlwaysNeverOrDefault"
_TmnxL2tpLnsTuPppLcpIgnoreMagic_Object = MibTableColumn
tmnxL2tpLnsTuPppLcpIgnoreMagic = _TmnxL2tpLnsTuPppLcpIgnoreMagic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 14),
    _TmnxL2tpLnsTuPppLcpIgnoreMagic_Type()
)
tmnxL2tpLnsTuPppLcpIgnoreMagic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppLcpIgnoreMagic.setStatus("current")


class _TmnxL2tpLnsTuPppMinChapChall_Type(Unsigned32):
    """Custom type tmnxL2tpLnsTuPppMinChapChall based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 64),
    )


_TmnxL2tpLnsTuPppMinChapChall_Type.__name__ = "Unsigned32"
_TmnxL2tpLnsTuPppMinChapChall_Object = MibTableColumn
tmnxL2tpLnsTuPppMinChapChall = _TmnxL2tpLnsTuPppMinChapChall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 15),
    _TmnxL2tpLnsTuPppMinChapChall_Type()
)
tmnxL2tpLnsTuPppMinChapChall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppMinChapChall.setStatus("current")


class _TmnxL2tpLnsTuPppMaxChapChall_Type(Unsigned32):
    """Custom type tmnxL2tpLnsTuPppMaxChapChall based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 64),
    )


_TmnxL2tpLnsTuPppMaxChapChall_Type.__name__ = "Unsigned32"
_TmnxL2tpLnsTuPppMaxChapChall_Object = MibTableColumn
tmnxL2tpLnsTuPppMaxChapChall = _TmnxL2tpLnsTuPppMaxChapChall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 3, 1, 16),
    _TmnxL2tpLnsTuPppMaxChapChall_Type()
)
tmnxL2tpLnsTuPppMaxChapChall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppMaxChapChall.setStatus("current")
_TmnxL2tpTuMlpppTable_Object = MibTable
tmnxL2tpTuMlpppTable = _TmnxL2tpTuMlpppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppTable.setStatus("current")
_TmnxL2tpTuMlpppEntry_Object = MibTableRow
tmnxL2tpTuMlpppEntry = _TmnxL2tpTuMlpppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppEntry.setStatus("current")
_TmnxL2tpTuMlpppLastMgmtChange_Type = TimeStamp
_TmnxL2tpTuMlpppLastMgmtChange_Object = MibTableColumn
tmnxL2tpTuMlpppLastMgmtChange = _TmnxL2tpTuMlpppLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 1),
    _TmnxL2tpTuMlpppLastMgmtChange_Type()
)
tmnxL2tpTuMlpppLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppLastMgmtChange.setStatus("current")


class _TmnxL2tpTuMlpppAdminState_Type(TmnxAdminState):
    """Custom type tmnxL2tpTuMlpppAdminState based on TmnxAdminState"""
    defaultValue = 1


_TmnxL2tpTuMlpppAdminState_Type.__name__ = "TmnxAdminState"
_TmnxL2tpTuMlpppAdminState_Object = MibTableColumn
tmnxL2tpTuMlpppAdminState = _TmnxL2tpTuMlpppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 2),
    _TmnxL2tpTuMlpppAdminState_Type()
)
tmnxL2tpTuMlpppAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppAdminState.setStatus("current")


class _TmnxL2tpTuMlpppMaxLinks_Type(Unsigned32):
    """Custom type tmnxL2tpTuMlpppMaxLinks based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_TmnxL2tpTuMlpppMaxLinks_Type.__name__ = "Unsigned32"
_TmnxL2tpTuMlpppMaxLinks_Object = MibTableColumn
tmnxL2tpTuMlpppMaxLinks = _TmnxL2tpTuMlpppMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 3),
    _TmnxL2tpTuMlpppMaxLinks_Type()
)
tmnxL2tpTuMlpppMaxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppMaxLinks.setStatus("current")


class _TmnxL2tpTuMlpppInterleave_Type(TmnxAlwaysNeverOrDefault):
    """Custom type tmnxL2tpTuMlpppInterleave based on TmnxAlwaysNeverOrDefault"""
    defaultValue = 1


_TmnxL2tpTuMlpppInterleave_Type.__name__ = "TmnxAlwaysNeverOrDefault"
_TmnxL2tpTuMlpppInterleave_Object = MibTableColumn
tmnxL2tpTuMlpppInterleave = _TmnxL2tpTuMlpppInterleave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 4),
    _TmnxL2tpTuMlpppInterleave_Type()
)
tmnxL2tpTuMlpppInterleave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppInterleave.setStatus("current")


class _TmnxL2tpTuMlpppMaxFragDelay_Type(TmnxL2tpMlpppMaxFragDelay):
    """Custom type tmnxL2tpTuMlpppMaxFragDelay based on TmnxL2tpMlpppMaxFragDelay"""
    defaultValue = 0


_TmnxL2tpTuMlpppMaxFragDelay_Type.__name__ = "TmnxL2tpMlpppMaxFragDelay"
_TmnxL2tpTuMlpppMaxFragDelay_Object = MibTableColumn
tmnxL2tpTuMlpppMaxFragDelay = _TmnxL2tpTuMlpppMaxFragDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 5),
    _TmnxL2tpTuMlpppMaxFragDelay_Type()
)
tmnxL2tpTuMlpppMaxFragDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppMaxFragDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppMaxFragDelay.setUnits("milliseconds")


class _TmnxL2tpTuMlpppReassemblyTo_Type(TmnxL2tpMlpppReassemblyTimeout):
    """Custom type tmnxL2tpTuMlpppReassemblyTo based on TmnxL2tpMlpppReassemblyTimeout"""
    defaultValue = 0


_TmnxL2tpTuMlpppReassemblyTo_Type.__name__ = "TmnxL2tpMlpppReassemblyTimeout"
_TmnxL2tpTuMlpppReassemblyTo_Object = MibTableColumn
tmnxL2tpTuMlpppReassemblyTo = _TmnxL2tpTuMlpppReassemblyTo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 6),
    _TmnxL2tpTuMlpppReassemblyTo_Type()
)
tmnxL2tpTuMlpppReassemblyTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppReassemblyTo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppReassemblyTo.setUnits("milliseconds")


class _TmnxL2tpTuMlpppShortSeqNumberRx_Type(TmnxAlwaysNeverOrDefault):
    """Custom type tmnxL2tpTuMlpppShortSeqNumberRx based on TmnxAlwaysNeverOrDefault"""
    defaultValue = 1


_TmnxL2tpTuMlpppShortSeqNumberRx_Type.__name__ = "TmnxAlwaysNeverOrDefault"
_TmnxL2tpTuMlpppShortSeqNumberRx_Object = MibTableColumn
tmnxL2tpTuMlpppShortSeqNumberRx = _TmnxL2tpTuMlpppShortSeqNumberRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 7),
    _TmnxL2tpTuMlpppShortSeqNumberRx_Type()
)
tmnxL2tpTuMlpppShortSeqNumberRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppShortSeqNumberRx.setStatus("current")


class _TmnxL2tpTuMlpppEpClass_Type(TmnxL2tpMlpppEndpointClass):
    """Custom type tmnxL2tpTuMlpppEpClass based on TmnxL2tpMlpppEndpointClass"""
    defaultValue = 0


_TmnxL2tpTuMlpppEpClass_Type.__name__ = "TmnxL2tpMlpppEndpointClass"
_TmnxL2tpTuMlpppEpClass_Object = MibTableColumn
tmnxL2tpTuMlpppEpClass = _TmnxL2tpTuMlpppEpClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 8),
    _TmnxL2tpTuMlpppEpClass_Type()
)
tmnxL2tpTuMlpppEpClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppEpClass.setStatus("current")
_TmnxL2tpTuMlpppEpIpv4Address_Type = InetAddressIPv4
_TmnxL2tpTuMlpppEpIpv4Address_Object = MibTableColumn
tmnxL2tpTuMlpppEpIpv4Address = _TmnxL2tpTuMlpppEpIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 9),
    _TmnxL2tpTuMlpppEpIpv4Address_Type()
)
tmnxL2tpTuMlpppEpIpv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppEpIpv4Address.setStatus("current")
_TmnxL2tpTuMlpppEpMacAddress_Type = MacAddress
_TmnxL2tpTuMlpppEpMacAddress_Object = MibTableColumn
tmnxL2tpTuMlpppEpMacAddress = _TmnxL2tpTuMlpppEpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 4, 1, 10),
    _TmnxL2tpTuMlpppEpMacAddress_Type()
)
tmnxL2tpTuMlpppEpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuMlpppEpMacAddress.setStatus("current")
_TmnxL2tpTuXtTable_Object = MibTable
tmnxL2tpTuXtTable = _TmnxL2tpTuXtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuXtTable.setStatus("current")
_TmnxL2tpTuXtEntry_Object = MibTableRow
tmnxL2tpTuXtEntry = _TmnxL2tpTuXtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuXtEntry.setStatus("current")
_TmnxL2tpTuXtLastMgmtChange_Type = TimeStamp
_TmnxL2tpTuXtLastMgmtChange_Object = MibTableColumn
tmnxL2tpTuXtLastMgmtChange = _TmnxL2tpTuXtLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 5, 1, 1),
    _TmnxL2tpTuXtLastMgmtChange_Type()
)
tmnxL2tpTuXtLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuXtLastMgmtChange.setStatus("current")


class _TmnxL2tpTuXtDfBitLac_Type(TmnxAlwaysNeverOrDefault):
    """Custom type tmnxL2tpTuXtDfBitLac based on TmnxAlwaysNeverOrDefault"""
    defaultValue = 1


_TmnxL2tpTuXtDfBitLac_Type.__name__ = "TmnxAlwaysNeverOrDefault"
_TmnxL2tpTuXtDfBitLac_Object = MibTableColumn
tmnxL2tpTuXtDfBitLac = _TmnxL2tpTuXtDfBitLac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 1, 5, 1, 2),
    _TmnxL2tpTuXtDfBitLac_Type()
)
tmnxL2tpTuXtDfBitLac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpTuXtDfBitLac.setStatus("current")
_TmnxL2tpTuStatObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpTuStatObjs = _TmnxL2tpTuStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2)
)
_TmnxL2tpTuStatusTable_Object = MibTable
tmnxL2tpTuStatusTable = _TmnxL2tpTuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusTable.setStatus("current")
_TmnxL2tpTuStatusEntry_Object = MibTableRow
tmnxL2tpTuStatusEntry = _TmnxL2tpTuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1)
)
tmnxL2tpTuStatusEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusEntry.setStatus("current")
_TmnxL2tpTuStatusId_Type = TmnxL2tpConnectionId
_TmnxL2tpTuStatusId_Object = MibTableColumn
tmnxL2tpTuStatusId = _TmnxL2tpTuStatusId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 1),
    _TmnxL2tpTuStatusId_Type()
)
tmnxL2tpTuStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusId.setStatus("current")
_TmnxL2tpTuStatusState_Type = TmnxL2tpTuOperState
_TmnxL2tpTuStatusState_Object = MibTableColumn
tmnxL2tpTuStatusState = _TmnxL2tpTuStatusState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 2),
    _TmnxL2tpTuStatusState_Type()
)
tmnxL2tpTuStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusState.setStatus("current")
_TmnxL2tpTuStatusTunnelId_Type = TmnxL2tpTunnelId
_TmnxL2tpTuStatusTunnelId_Object = MibTableColumn
tmnxL2tpTuStatusTunnelId = _TmnxL2tpTuStatusTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 3),
    _TmnxL2tpTuStatusTunnelId_Type()
)
tmnxL2tpTuStatusTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusTunnelId.setStatus("current")
_TmnxL2tpTuStatusPreference_Type = TmnxL2tpTunnelPreference
_TmnxL2tpTuStatusPreference_Object = MibTableColumn
tmnxL2tpTuStatusPreference = _TmnxL2tpTuStatusPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 4),
    _TmnxL2tpTuStatusPreference_Type()
)
tmnxL2tpTuStatusPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusPreference.setStatus("current")
_TmnxL2tpTuStatusPeerAddrType_Type = InetAddressType
_TmnxL2tpTuStatusPeerAddrType_Object = MibTableColumn
tmnxL2tpTuStatusPeerAddrType = _TmnxL2tpTuStatusPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 5),
    _TmnxL2tpTuStatusPeerAddrType_Type()
)
tmnxL2tpTuStatusPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusPeerAddrType.setStatus("current")


class _TmnxL2tpTuStatusPeerAddr_Type(InetAddress):
    """Custom type tmnxL2tpTuStatusPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpTuStatusPeerAddr_Type.__name__ = "InetAddress"
_TmnxL2tpTuStatusPeerAddr_Object = MibTableColumn
tmnxL2tpTuStatusPeerAddr = _TmnxL2tpTuStatusPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 6),
    _TmnxL2tpTuStatusPeerAddr_Type()
)
tmnxL2tpTuStatusPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusPeerAddr.setStatus("current")
_TmnxL2tpTuStatusAddrType_Type = InetAddressType
_TmnxL2tpTuStatusAddrType_Object = MibTableColumn
tmnxL2tpTuStatusAddrType = _TmnxL2tpTuStatusAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 7),
    _TmnxL2tpTuStatusAddrType_Type()
)
tmnxL2tpTuStatusAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusAddrType.setStatus("current")


class _TmnxL2tpTuStatusAddr_Type(InetAddress):
    """Custom type tmnxL2tpTuStatusAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpTuStatusAddr_Type.__name__ = "InetAddress"
_TmnxL2tpTuStatusAddr_Object = MibTableColumn
tmnxL2tpTuStatusAddr = _TmnxL2tpTuStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 8),
    _TmnxL2tpTuStatusAddr_Type()
)
tmnxL2tpTuStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusAddr.setStatus("current")
_TmnxL2tpTuStatusLocalName_Type = TmnxL2tpHostNameOrEmpty
_TmnxL2tpTuStatusLocalName_Object = MibTableColumn
tmnxL2tpTuStatusLocalName = _TmnxL2tpTuStatusLocalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 9),
    _TmnxL2tpTuStatusLocalName_Type()
)
tmnxL2tpTuStatusLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusLocalName.setStatus("current")
_TmnxL2tpTuStatusRemoteName_Type = TmnxL2tpHostNameOrEmpty
_TmnxL2tpTuStatusRemoteName_Object = MibTableColumn
tmnxL2tpTuStatusRemoteName = _TmnxL2tpTuStatusRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 10),
    _TmnxL2tpTuStatusRemoteName_Type()
)
tmnxL2tpTuStatusRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRemoteName.setStatus("current")
_TmnxL2tpTuStatusAssignmentId_Type = TmnxL2tpTunnelNameOrEmpty
_TmnxL2tpTuStatusAssignmentId_Object = MibTableColumn
tmnxL2tpTuStatusAssignmentId = _TmnxL2tpTuStatusAssignmentId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 11),
    _TmnxL2tpTuStatusAssignmentId_Type()
)
tmnxL2tpTuStatusAssignmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusAssignmentId.setStatus("current")
_TmnxL2tpTuStatusHelloInterval_Type = TmnxL2tpTunnelHelloInterval
_TmnxL2tpTuStatusHelloInterval_Object = MibTableColumn
tmnxL2tpTuStatusHelloInterval = _TmnxL2tpTuStatusHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 13),
    _TmnxL2tpTuStatusHelloInterval_Type()
)
tmnxL2tpTuStatusHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusHelloInterval.setUnits("seconds")
_TmnxL2tpTuStatusIdleTO_Type = TmnxL2tpTunnelIdleTO
_TmnxL2tpTuStatusIdleTO_Object = MibTableColumn
tmnxL2tpTuStatusIdleTO = _TmnxL2tpTuStatusIdleTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 14),
    _TmnxL2tpTuStatusIdleTO_Type()
)
tmnxL2tpTuStatusIdleTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusIdleTO.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusIdleTO.setUnits("seconds")
_TmnxL2tpTuStatusDestructTO_Type = TmnxL2tpTunnelDestructTO
_TmnxL2tpTuStatusDestructTO_Object = MibTableColumn
tmnxL2tpTuStatusDestructTO = _TmnxL2tpTuStatusDestructTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 15),
    _TmnxL2tpTuStatusDestructTO_Type()
)
tmnxL2tpTuStatusDestructTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusDestructTO.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusDestructTO.setUnits("seconds")
_TmnxL2tpTuStatusMaxRetxEstab_Type = TmnxL2tpTunnelMaxRetx
_TmnxL2tpTuStatusMaxRetxEstab_Object = MibTableColumn
tmnxL2tpTuStatusMaxRetxEstab = _TmnxL2tpTuStatusMaxRetxEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 16),
    _TmnxL2tpTuStatusMaxRetxEstab_Type()
)
tmnxL2tpTuStatusMaxRetxEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusMaxRetxEstab.setStatus("current")
_TmnxL2tpTuStatusMaxRetxNotEstab_Type = TmnxL2tpTunnelMaxRetx
_TmnxL2tpTuStatusMaxRetxNotEstab_Object = MibTableColumn
tmnxL2tpTuStatusMaxRetxNotEstab = _TmnxL2tpTuStatusMaxRetxNotEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 17),
    _TmnxL2tpTuStatusMaxRetxNotEstab_Type()
)
tmnxL2tpTuStatusMaxRetxNotEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusMaxRetxNotEstab.setStatus("current")
_TmnxL2tpTuStatusSessionLimit_Type = TmnxL2tpTunnelSessionLimit
_TmnxL2tpTuStatusSessionLimit_Object = MibTableColumn
tmnxL2tpTuStatusSessionLimit = _TmnxL2tpTuStatusSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 18),
    _TmnxL2tpTuStatusSessionLimit_Type()
)
tmnxL2tpTuStatusSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusSessionLimit.setStatus("current")
_TmnxL2tpTuStatusAvpHiding_Type = TmnxL2tpAvpHidingMode
_TmnxL2tpTuStatusAvpHiding_Object = MibTableColumn
tmnxL2tpTuStatusAvpHiding = _TmnxL2tpTuStatusAvpHiding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 19),
    _TmnxL2tpTuStatusAvpHiding_Type()
)
tmnxL2tpTuStatusAvpHiding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusAvpHiding.setStatus("current")
_TmnxL2tpTuStatusGroupName_Type = TmnxL2tpTunnelGroupNameOrEmpty
_TmnxL2tpTuStatusGroupName_Object = MibTableColumn
tmnxL2tpTuStatusGroupName = _TmnxL2tpTuStatusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 20),
    _TmnxL2tpTuStatusGroupName_Type()
)
tmnxL2tpTuStatusGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusGroupName.setStatus("current")
_TmnxL2tpTuStatusRemoteTunnelId_Type = TmnxL2tpTunnelId
_TmnxL2tpTuStatusRemoteTunnelId_Object = MibTableColumn
tmnxL2tpTuStatusRemoteTunnelId = _TmnxL2tpTuStatusRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 21),
    _TmnxL2tpTuStatusRemoteTunnelId_Type()
)
tmnxL2tpTuStatusRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRemoteTunnelId.setStatus("current")
_TmnxL2tpTuStatusRemoteConnId_Type = TmnxL2tpConnectionId
_TmnxL2tpTuStatusRemoteConnId_Object = MibTableColumn
tmnxL2tpTuStatusRemoteConnId = _TmnxL2tpTuStatusRemoteConnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 22),
    _TmnxL2tpTuStatusRemoteConnId_Type()
)
tmnxL2tpTuStatusRemoteConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRemoteConnId.setStatus("current")
_TmnxL2tpTuStatusTransportType_Type = TmnxL2tpTransportType
_TmnxL2tpTuStatusTransportType_Object = MibTableColumn
tmnxL2tpTuStatusTransportType = _TmnxL2tpTuStatusTransportType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 23),
    _TmnxL2tpTuStatusTransportType_Type()
)
tmnxL2tpTuStatusTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusTransportType.setStatus("current")
_TmnxL2tpTuStatusUdpPort_Type = InetPortNumber
_TmnxL2tpTuStatusUdpPort_Object = MibTableColumn
tmnxL2tpTuStatusUdpPort = _TmnxL2tpTuStatusUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 24),
    _TmnxL2tpTuStatusUdpPort_Type()
)
tmnxL2tpTuStatusUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusUdpPort.setStatus("current")
_TmnxL2tpTuStatusRemoteUdpPort_Type = InetPortNumber
_TmnxL2tpTuStatusRemoteUdpPort_Object = MibTableColumn
tmnxL2tpTuStatusRemoteUdpPort = _TmnxL2tpTuStatusRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 25),
    _TmnxL2tpTuStatusRemoteUdpPort_Type()
)
tmnxL2tpTuStatusRemoteUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRemoteUdpPort.setStatus("current")
_TmnxL2tpTuStatusStartTime_Type = TimeStamp
_TmnxL2tpTuStatusStartTime_Object = MibTableColumn
tmnxL2tpTuStatusStartTime = _TmnxL2tpTuStatusStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 26),
    _TmnxL2tpTuStatusStartTime_Type()
)
tmnxL2tpTuStatusStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusStartTime.setStatus("current")
_TmnxL2tpTuStatusEstabTime_Type = TimeStamp
_TmnxL2tpTuStatusEstabTime_Object = MibTableColumn
tmnxL2tpTuStatusEstabTime = _TmnxL2tpTuStatusEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 27),
    _TmnxL2tpTuStatusEstabTime_Type()
)
tmnxL2tpTuStatusEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusEstabTime.setStatus("current")
_TmnxL2tpTuStatusIdleTime_Type = TimeStamp
_TmnxL2tpTuStatusIdleTime_Object = MibTableColumn
tmnxL2tpTuStatusIdleTime = _TmnxL2tpTuStatusIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 28),
    _TmnxL2tpTuStatusIdleTime_Type()
)
tmnxL2tpTuStatusIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusIdleTime.setStatus("current")
_TmnxL2tpTuStatusClosedTime_Type = TimeStamp
_TmnxL2tpTuStatusClosedTime_Object = MibTableColumn
tmnxL2tpTuStatusClosedTime = _TmnxL2tpTuStatusClosedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 29),
    _TmnxL2tpTuStatusClosedTime_Type()
)
tmnxL2tpTuStatusClosedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusClosedTime.setStatus("current")
_TmnxL2tpTuStatusStopCcnResult_Type = TmnxL2tpStopCcnResult
_TmnxL2tpTuStatusStopCcnResult_Object = MibTableColumn
tmnxL2tpTuStatusStopCcnResult = _TmnxL2tpTuStatusStopCcnResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 30),
    _TmnxL2tpTuStatusStopCcnResult_Type()
)
tmnxL2tpTuStatusStopCcnResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusStopCcnResult.setStatus("current")
_TmnxL2tpTuStatusGeneralError_Type = TmnxL2tpGeneralError
_TmnxL2tpTuStatusGeneralError_Object = MibTableColumn
tmnxL2tpTuStatusGeneralError = _TmnxL2tpTuStatusGeneralError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 31),
    _TmnxL2tpTuStatusGeneralError_Type()
)
tmnxL2tpTuStatusGeneralError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusGeneralError.setStatus("current")
_TmnxL2tpTuStatusErrorMessage_Type = TmnxL2tpErrorMessage
_TmnxL2tpTuStatusErrorMessage_Object = MibTableColumn
tmnxL2tpTuStatusErrorMessage = _TmnxL2tpTuStatusErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 32),
    _TmnxL2tpTuStatusErrorMessage_Type()
)
tmnxL2tpTuStatusErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusErrorMessage.setStatus("current")
_TmnxL2tpTuStatusDoChallenge_Type = TmnxL2tpDoChallenge
_TmnxL2tpTuStatusDoChallenge_Object = MibTableColumn
tmnxL2tpTuStatusDoChallenge = _TmnxL2tpTuStatusDoChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 33),
    _TmnxL2tpTuStatusDoChallenge_Type()
)
tmnxL2tpTuStatusDoChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusDoChallenge.setStatus("current")
_TmnxL2tpTuStatusRws_Type = Unsigned32
_TmnxL2tpTuStatusRws_Object = MibTableColumn
tmnxL2tpTuStatusRws = _TmnxL2tpTuStatusRws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 34),
    _TmnxL2tpTuStatusRws_Type()
)
tmnxL2tpTuStatusRws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRws.setUnits("seconds")
_TmnxL2tpTuStatusTxDestAddrType_Type = InetAddressType
_TmnxL2tpTuStatusTxDestAddrType_Object = MibTableColumn
tmnxL2tpTuStatusTxDestAddrType = _TmnxL2tpTuStatusTxDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 35),
    _TmnxL2tpTuStatusTxDestAddrType_Type()
)
tmnxL2tpTuStatusTxDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusTxDestAddrType.setStatus("current")


class _TmnxL2tpTuStatusTxDestAddr_Type(InetAddress):
    """Custom type tmnxL2tpTuStatusTxDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpTuStatusTxDestAddr_Type.__name__ = "InetAddress"
_TmnxL2tpTuStatusTxDestAddr_Object = MibTableColumn
tmnxL2tpTuStatusTxDestAddr = _TmnxL2tpTuStatusTxDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 36),
    _TmnxL2tpTuStatusTxDestAddr_Type()
)
tmnxL2tpTuStatusTxDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusTxDestAddr.setStatus("current")
_TmnxL2tpTuStatusRxSrcAddrType_Type = InetAddressType
_TmnxL2tpTuStatusRxSrcAddrType_Object = MibTableColumn
tmnxL2tpTuStatusRxSrcAddrType = _TmnxL2tpTuStatusRxSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 37),
    _TmnxL2tpTuStatusRxSrcAddrType_Type()
)
tmnxL2tpTuStatusRxSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRxSrcAddrType.setStatus("current")


class _TmnxL2tpTuStatusRxSrcAddr_Type(InetAddress):
    """Custom type tmnxL2tpTuStatusRxSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpTuStatusRxSrcAddr_Type.__name__ = "InetAddress"
_TmnxL2tpTuStatusRxSrcAddr_Object = MibTableColumn
tmnxL2tpTuStatusRxSrcAddr = _TmnxL2tpTuStatusRxSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 38),
    _TmnxL2tpTuStatusRxSrcAddr_Type()
)
tmnxL2tpTuStatusRxSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRxSrcAddr.setStatus("current")
_TmnxL2tpTuStatusAccountingPolicy_Type = TNamedItemOrEmpty
_TmnxL2tpTuStatusAccountingPolicy_Object = MibTableColumn
tmnxL2tpTuStatusAccountingPolicy = _TmnxL2tpTuStatusAccountingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 40),
    _TmnxL2tpTuStatusAccountingPolicy_Type()
)
tmnxL2tpTuStatusAccountingPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusAccountingPolicy.setStatus("current")


class _TmnxL2tpTuStatusSelBlacklstState_Type(Integer32):
    """Custom type tmnxL2tpTuStatusSelBlacklstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notBlacklisted", 0),
          ("blacklisted", 1),
          ("selectable", 2))
    )


_TmnxL2tpTuStatusSelBlacklstState_Type.__name__ = "Integer32"
_TmnxL2tpTuStatusSelBlacklstState_Object = MibTableColumn
tmnxL2tpTuStatusSelBlacklstState = _TmnxL2tpTuStatusSelBlacklstState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 41),
    _TmnxL2tpTuStatusSelBlacklstState_Type()
)
tmnxL2tpTuStatusSelBlacklstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusSelBlacklstState.setStatus("current")
_TmnxL2tpTuStatusSelBlacklstTime_Type = TimeStamp
_TmnxL2tpTuStatusSelBlacklstTime_Object = MibTableColumn
tmnxL2tpTuStatusSelBlacklstTime = _TmnxL2tpTuStatusSelBlacklstTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 42),
    _TmnxL2tpTuStatusSelBlacklstTime_Type()
)
tmnxL2tpTuStatusSelBlacklstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusSelBlacklstTime.setStatus("current")
_TmnxL2tpTuStatSelBlacklstTimeRem_Type = Unsigned32
_TmnxL2tpTuStatSelBlacklstTimeRem_Object = MibTableColumn
tmnxL2tpTuStatSelBlacklstTimeRem = _TmnxL2tpTuStatSelBlacklstTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 43),
    _TmnxL2tpTuStatSelBlacklstTimeRem_Type()
)
tmnxL2tpTuStatSelBlacklstTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatSelBlacklstTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatSelBlacklstTimeRem.setUnits("seconds")
_TmnxL2tpTuStatusTxDestUdpPort_Type = InetPortNumber
_TmnxL2tpTuStatusTxDestUdpPort_Object = MibTableColumn
tmnxL2tpTuStatusTxDestUdpPort = _TmnxL2tpTuStatusTxDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 44),
    _TmnxL2tpTuStatusTxDestUdpPort_Type()
)
tmnxL2tpTuStatusTxDestUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusTxDestUdpPort.setStatus("current")
_TmnxL2tpTuStatusRxSrcUdpPort_Type = InetPortNumber
_TmnxL2tpTuStatusRxSrcUdpPort_Object = MibTableColumn
tmnxL2tpTuStatusRxSrcUdpPort = _TmnxL2tpTuStatusRxSrcUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 45),
    _TmnxL2tpTuStatusRxSrcUdpPort_Type()
)
tmnxL2tpTuStatusRxSrcUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusRxSrcUdpPort.setStatus("current")
_TmnxL2tpTuStatusDfBitLac_Type = TruthValue
_TmnxL2tpTuStatusDfBitLac_Object = MibTableColumn
tmnxL2tpTuStatusDfBitLac = _TmnxL2tpTuStatusDfBitLac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 2, 1, 46),
    _TmnxL2tpTuStatusDfBitLac_Type()
)
tmnxL2tpTuStatusDfBitLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusDfBitLac.setStatus("current")
_TmnxL2tpTuStatsTable_Object = MibTable
tmnxL2tpTuStatsTable = _TmnxL2tpTuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsTable.setStatus("current")
_TmnxL2tpTuStatsEntry_Object = MibTableRow
tmnxL2tpTuStatsEntry = _TmnxL2tpTuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsEntry.setStatus("current")
_TmnxL2tpTuStatsLastCleared_Type = TimeStamp
_TmnxL2tpTuStatsLastCleared_Object = MibTableColumn
tmnxL2tpTuStatsLastCleared = _TmnxL2tpTuStatsLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 1),
    _TmnxL2tpTuStatsLastCleared_Type()
)
tmnxL2tpTuStatsLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsLastCleared.setStatus("current")
_TmnxL2tpTuStatsTotalSessions_Type = Counter32
_TmnxL2tpTuStatsTotalSessions_Object = MibTableColumn
tmnxL2tpTuStatsTotalSessions = _TmnxL2tpTuStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 2),
    _TmnxL2tpTuStatsTotalSessions_Type()
)
tmnxL2tpTuStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsTotalSessions.setStatus("current")
_TmnxL2tpTuStatsFailedSessions_Type = Counter32
_TmnxL2tpTuStatsFailedSessions_Object = MibTableColumn
tmnxL2tpTuStatsFailedSessions = _TmnxL2tpTuStatsFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 3),
    _TmnxL2tpTuStatsFailedSessions_Type()
)
tmnxL2tpTuStatsFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsFailedSessions.setStatus("current")
_TmnxL2tpTuStatsActiveSessions_Type = Gauge32
_TmnxL2tpTuStatsActiveSessions_Object = MibTableColumn
tmnxL2tpTuStatsActiveSessions = _TmnxL2tpTuStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 4),
    _TmnxL2tpTuStatsActiveSessions_Type()
)
tmnxL2tpTuStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsActiveSessions.setStatus("current")
_TmnxL2tpTuStatsSessions_Type = Gauge32
_TmnxL2tpTuStatsSessions_Object = MibTableColumn
tmnxL2tpTuStatsSessions = _TmnxL2tpTuStatsSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 5),
    _TmnxL2tpTuStatsSessions_Type()
)
tmnxL2tpTuStatsSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsSessions.setStatus("current")
_TmnxL2tpTuStatsControlRxOctets_Type = Counter64
_TmnxL2tpTuStatsControlRxOctets_Object = MibTableColumn
tmnxL2tpTuStatsControlRxOctets = _TmnxL2tpTuStatsControlRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 6),
    _TmnxL2tpTuStatsControlRxOctets_Type()
)
tmnxL2tpTuStatsControlRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsControlRxOctets.setStatus("current")
_TmnxL2tpTuStatsControlRxOctetsLw_Type = Counter32
_TmnxL2tpTuStatsControlRxOctetsLw_Object = MibTableColumn
tmnxL2tpTuStatsControlRxOctetsLw = _TmnxL2tpTuStatsControlRxOctetsLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 7),
    _TmnxL2tpTuStatsControlRxOctetsLw_Type()
)
tmnxL2tpTuStatsControlRxOctetsLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsControlRxOctetsLw.setStatus("current")
_TmnxL2tpTuStatsControlRxOctetsHw_Type = Counter32
_TmnxL2tpTuStatsControlRxOctetsHw_Object = MibTableColumn
tmnxL2tpTuStatsControlRxOctetsHw = _TmnxL2tpTuStatsControlRxOctetsHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 8),
    _TmnxL2tpTuStatsControlRxOctetsHw_Type()
)
tmnxL2tpTuStatsControlRxOctetsHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsControlRxOctetsHw.setStatus("current")
_TmnxL2tpTuStatsControlRxPkts_Type = Counter32
_TmnxL2tpTuStatsControlRxPkts_Object = MibTableColumn
tmnxL2tpTuStatsControlRxPkts = _TmnxL2tpTuStatsControlRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 9),
    _TmnxL2tpTuStatsControlRxPkts_Type()
)
tmnxL2tpTuStatsControlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsControlRxPkts.setStatus("current")
_TmnxL2tpTuStatsControlTxOctets_Type = Counter64
_TmnxL2tpTuStatsControlTxOctets_Object = MibTableColumn
tmnxL2tpTuStatsControlTxOctets = _TmnxL2tpTuStatsControlTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 10),
    _TmnxL2tpTuStatsControlTxOctets_Type()
)
tmnxL2tpTuStatsControlTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsControlTxOctets.setStatus("current")
_TmnxL2tpTuStatsControlTxOctetsLw_Type = Counter32
_TmnxL2tpTuStatsControlTxOctetsLw_Object = MibTableColumn
tmnxL2tpTuStatsControlTxOctetsLw = _TmnxL2tpTuStatsControlTxOctetsLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 11),
    _TmnxL2tpTuStatsControlTxOctetsLw_Type()
)
tmnxL2tpTuStatsControlTxOctetsLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsControlTxOctetsLw.setStatus("current")
_TmnxL2tpTuStatsControlTxOctetsHw_Type = Counter32
_TmnxL2tpTuStatsControlTxOctetsHw_Object = MibTableColumn
tmnxL2tpTuStatsControlTxOctetsHw = _TmnxL2tpTuStatsControlTxOctetsHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 12),
    _TmnxL2tpTuStatsControlTxOctetsHw_Type()
)
tmnxL2tpTuStatsControlTxOctetsHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsControlTxOctetsHw.setStatus("current")
_TmnxL2tpTuStatsControlTxPkts_Type = Counter32
_TmnxL2tpTuStatsControlTxPkts_Object = MibTableColumn
tmnxL2tpTuStatsControlTxPkts = _TmnxL2tpTuStatsControlTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 13),
    _TmnxL2tpTuStatsControlTxPkts_Type()
)
tmnxL2tpTuStatsControlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsControlTxPkts.setStatus("current")
_TmnxL2tpTuStatsErrorTxPkts_Type = Counter32
_TmnxL2tpTuStatsErrorTxPkts_Object = MibTableColumn
tmnxL2tpTuStatsErrorTxPkts = _TmnxL2tpTuStatsErrorTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 14),
    _TmnxL2tpTuStatsErrorTxPkts_Type()
)
tmnxL2tpTuStatsErrorTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsErrorTxPkts.setStatus("current")
_TmnxL2tpTuStatsErrorRxPkts_Type = Counter32
_TmnxL2tpTuStatsErrorRxPkts_Object = MibTableColumn
tmnxL2tpTuStatsErrorRxPkts = _TmnxL2tpTuStatsErrorRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 15),
    _TmnxL2tpTuStatsErrorRxPkts_Type()
)
tmnxL2tpTuStatsErrorRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsErrorRxPkts.setStatus("current")
_TmnxL2tpTuStatsFsmMsgAccepted_Type = Counter32
_TmnxL2tpTuStatsFsmMsgAccepted_Object = MibTableColumn
tmnxL2tpTuStatsFsmMsgAccepted = _TmnxL2tpTuStatsFsmMsgAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 16),
    _TmnxL2tpTuStatsFsmMsgAccepted_Type()
)
tmnxL2tpTuStatsFsmMsgAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsFsmMsgAccepted.setStatus("current")
_TmnxL2tpTuStatsFsmMsgDuplicateRx_Type = Counter32
_TmnxL2tpTuStatsFsmMsgDuplicateRx_Object = MibTableColumn
tmnxL2tpTuStatsFsmMsgDuplicateRx = _TmnxL2tpTuStatsFsmMsgDuplicateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 17),
    _TmnxL2tpTuStatsFsmMsgDuplicateRx_Type()
)
tmnxL2tpTuStatsFsmMsgDuplicateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsFsmMsgDuplicateRx.setStatus("current")
_TmnxL2tpTuStatsFsmMsgOutOfWndwRx_Type = Counter32
_TmnxL2tpTuStatsFsmMsgOutOfWndwRx_Object = MibTableColumn
tmnxL2tpTuStatsFsmMsgOutOfWndwRx = _TmnxL2tpTuStatsFsmMsgOutOfWndwRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 18),
    _TmnxL2tpTuStatsFsmMsgOutOfWndwRx_Type()
)
tmnxL2tpTuStatsFsmMsgOutOfWndwRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsFsmMsgOutOfWndwRx.setStatus("current")
_TmnxL2tpTuStatsQLengthUnsentMax_Type = Gauge32
_TmnxL2tpTuStatsQLengthUnsentMax_Object = MibTableColumn
tmnxL2tpTuStatsQLengthUnsentMax = _TmnxL2tpTuStatsQLengthUnsentMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 19),
    _TmnxL2tpTuStatsQLengthUnsentMax_Type()
)
tmnxL2tpTuStatsQLengthUnsentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsQLengthUnsentMax.setStatus("current")
_TmnxL2tpTuStatsQLengthUnsentCur_Type = Gauge32
_TmnxL2tpTuStatsQLengthUnsentCur_Object = MibTableColumn
tmnxL2tpTuStatsQLengthUnsentCur = _TmnxL2tpTuStatsQLengthUnsentCur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 20),
    _TmnxL2tpTuStatsQLengthUnsentCur_Type()
)
tmnxL2tpTuStatsQLengthUnsentCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsQLengthUnsentCur.setStatus("current")
_TmnxL2tpTuStatsQLengthAckMax_Type = Gauge32
_TmnxL2tpTuStatsQLengthAckMax_Object = MibTableColumn
tmnxL2tpTuStatsQLengthAckMax = _TmnxL2tpTuStatsQLengthAckMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 21),
    _TmnxL2tpTuStatsQLengthAckMax_Type()
)
tmnxL2tpTuStatsQLengthAckMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsQLengthAckMax.setStatus("current")
_TmnxL2tpTuStatsQLengthAckCur_Type = Gauge32
_TmnxL2tpTuStatsQLengthAckCur_Object = MibTableColumn
tmnxL2tpTuStatsQLengthAckCur = _TmnxL2tpTuStatsQLengthAckCur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 22),
    _TmnxL2tpTuStatsQLengthAckCur_Type()
)
tmnxL2tpTuStatsQLengthAckCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsQLengthAckCur.setStatus("current")
_TmnxL2tpTuStatsWindowSizeCur_Type = Gauge32
_TmnxL2tpTuStatsWindowSizeCur_Object = MibTableColumn
tmnxL2tpTuStatsWindowSizeCur = _TmnxL2tpTuStatsWindowSizeCur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 3, 1, 23),
    _TmnxL2tpTuStatsWindowSizeCur_Type()
)
tmnxL2tpTuStatsWindowSizeCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatsWindowSizeCur.setStatus("current")
_TmnxL2tpTuProtStatsTable_Object = MibTable
tmnxL2tpTuProtStatsTable = _TmnxL2tpTuProtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuProtStatsTable.setStatus("current")
_TmnxL2tpTuProtStatsEntry_Object = MibTableRow
tmnxL2tpTuProtStatsEntry = _TmnxL2tpTuProtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 4, 1)
)
tmnxL2tpTuProtStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusId"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuProtStatsType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuProtStatsInstance"),
)
if mibBuilder.loadTexts:
    tmnxL2tpTuProtStatsEntry.setStatus("current")
_TmnxL2tpTuProtStatsType_Type = TmnxL2tpTuProtStatsType
_TmnxL2tpTuProtStatsType_Object = MibTableColumn
tmnxL2tpTuProtStatsType = _TmnxL2tpTuProtStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 4, 1, 1),
    _TmnxL2tpTuProtStatsType_Type()
)
tmnxL2tpTuProtStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpTuProtStatsType.setStatus("current")


class _TmnxL2tpTuProtStatsInstance_Type(Unsigned32):
    """Custom type tmnxL2tpTuProtStatsInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_TmnxL2tpTuProtStatsInstance_Type.__name__ = "Unsigned32"
_TmnxL2tpTuProtStatsInstance_Object = MibTableColumn
tmnxL2tpTuProtStatsInstance = _TmnxL2tpTuProtStatsInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 4, 1, 2),
    _TmnxL2tpTuProtStatsInstance_Type()
)
tmnxL2tpTuProtStatsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpTuProtStatsInstance.setStatus("current")


class _TmnxL2tpTuProtStatsName_Type(DisplayString):
    """Custom type tmnxL2tpTuProtStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxL2tpTuProtStatsName_Type.__name__ = "DisplayString"
_TmnxL2tpTuProtStatsName_Object = MibTableColumn
tmnxL2tpTuProtStatsName = _TmnxL2tpTuProtStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 4, 1, 3),
    _TmnxL2tpTuProtStatsName_Type()
)
tmnxL2tpTuProtStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuProtStatsName.setStatus("current")
_TmnxL2tpTuProtStatsVal_Type = Counter32
_TmnxL2tpTuProtStatsVal_Object = MibTableColumn
tmnxL2tpTuProtStatsVal = _TmnxL2tpTuProtStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 2, 4, 1, 4),
    _TmnxL2tpTuProtStatsVal_Type()
)
tmnxL2tpTuProtStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuProtStatsVal.setStatus("current")
_TmnxL2tpTuOpObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpTuOpObjs = _TmnxL2tpTuOpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3)
)
_TmnxL2tpTuStartTable_Object = MibTable
tmnxL2tpTuStartTable = _TmnxL2tpTuStartTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStartTable.setStatus("current")
_TmnxL2tpTuStartEntry_Object = MibTableRow
tmnxL2tpTuStartEntry = _TmnxL2tpTuStartEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStartEntry.setStatus("current")


class _TmnxL2tpTuStart_Type(TmnxActionType):
    """Custom type tmnxL2tpTuStart based on TmnxActionType"""
    defaultValue = 2


_TmnxL2tpTuStart_Type.__name__ = "TmnxActionType"
_TmnxL2tpTuStart_Object = MibTableColumn
tmnxL2tpTuStart = _TmnxL2tpTuStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 1, 1, 1),
    _TmnxL2tpTuStart_Type()
)
tmnxL2tpTuStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxL2tpTuStart.setStatus("current")
_TmnxL2tpTuStopTable_Object = MibTable
tmnxL2tpTuStopTable = _TmnxL2tpTuStopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStopTable.setStatus("current")
_TmnxL2tpTuStopEntry_Object = MibTableRow
tmnxL2tpTuStopEntry = _TmnxL2tpTuStopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStopEntry.setStatus("current")


class _TmnxL2tpTuStop_Type(TmnxActionType):
    """Custom type tmnxL2tpTuStop based on TmnxActionType"""
    defaultValue = 2


_TmnxL2tpTuStop_Type.__name__ = "TmnxActionType"
_TmnxL2tpTuStop_Object = MibTableColumn
tmnxL2tpTuStop = _TmnxL2tpTuStop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 2, 1, 1),
    _TmnxL2tpTuStop_Type()
)
tmnxL2tpTuStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxL2tpTuStop.setStatus("current")
_TmnxL2tpTuDrainTable_Object = MibTable
tmnxL2tpTuDrainTable = _TmnxL2tpTuDrainTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuDrainTable.setStatus("current")
_TmnxL2tpTuDrainEntry_Object = MibTableRow
tmnxL2tpTuDrainEntry = _TmnxL2tpTuDrainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpTuDrainEntry.setStatus("current")


class _TmnxL2tpTuDrain_Type(TmnxL2tpActionTypeDrain):
    """Custom type tmnxL2tpTuDrain based on TmnxL2tpActionTypeDrain"""
    defaultValue = 2


_TmnxL2tpTuDrain_Type.__name__ = "TmnxL2tpActionTypeDrain"
_TmnxL2tpTuDrain_Object = MibTableColumn
tmnxL2tpTuDrain = _TmnxL2tpTuDrain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 3, 3, 3, 1, 1),
    _TmnxL2tpTuDrain_Type()
)
tmnxL2tpTuDrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxL2tpTuDrain.setStatus("current")
_TmnxL2tpPeerObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpPeerObjs = _TmnxL2tpPeerObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4)
)
_TmnxL2tpPeerStatObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpPeerStatObjs = _TmnxL2tpPeerStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1)
)
_TmnxL2tpPeerStatTable_Object = MibTable
tmnxL2tpPeerStatTable = _TmnxL2tpPeerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatTable.setStatus("current")
_TmnxL2tpPeerStatEntry_Object = MibTableRow
tmnxL2tpPeerStatEntry = _TmnxL2tpPeerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1)
)
tmnxL2tpPeerStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTransportType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPeerAddrType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPeerAddr"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRemoteUdpPort"),
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatEntry.setStatus("current")


class _TmnxL2tpPeerStatRole_Type(Integer32):
    """Custom type tmnxL2tpPeerStatRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roleLAC", 1),
          ("roleLNS", 2))
    )


_TmnxL2tpPeerStatRole_Type.__name__ = "Integer32"
_TmnxL2tpPeerStatRole_Object = MibTableColumn
tmnxL2tpPeerStatRole = _TmnxL2tpPeerStatRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 1),
    _TmnxL2tpPeerStatRole_Type()
)
tmnxL2tpPeerStatRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatRole.setStatus("obsolete")
_TmnxL2tpPeerStatActiveTunnels_Type = Gauge32
_TmnxL2tpPeerStatActiveTunnels_Object = MibTableColumn
tmnxL2tpPeerStatActiveTunnels = _TmnxL2tpPeerStatActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 2),
    _TmnxL2tpPeerStatActiveTunnels_Type()
)
tmnxL2tpPeerStatActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatActiveTunnels.setStatus("current")
_TmnxL2tpPeerStatTunnels_Type = Gauge32
_TmnxL2tpPeerStatTunnels_Object = MibTableColumn
tmnxL2tpPeerStatTunnels = _TmnxL2tpPeerStatTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 3),
    _TmnxL2tpPeerStatTunnels_Type()
)
tmnxL2tpPeerStatTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatTunnels.setStatus("current")
_TmnxL2tpPeerStatActiveSessions_Type = Gauge32
_TmnxL2tpPeerStatActiveSessions_Object = MibTableColumn
tmnxL2tpPeerStatActiveSessions = _TmnxL2tpPeerStatActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 4),
    _TmnxL2tpPeerStatActiveSessions_Type()
)
tmnxL2tpPeerStatActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatActiveSessions.setStatus("current")
_TmnxL2tpPeerStatSessions_Type = Gauge32
_TmnxL2tpPeerStatSessions_Object = MibTableColumn
tmnxL2tpPeerStatSessions = _TmnxL2tpPeerStatSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 5),
    _TmnxL2tpPeerStatSessions_Type()
)
tmnxL2tpPeerStatSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatSessions.setStatus("current")
_TmnxL2tpPeerStatDraining_Type = TruthValue
_TmnxL2tpPeerStatDraining_Object = MibTableColumn
tmnxL2tpPeerStatDraining = _TmnxL2tpPeerStatDraining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 6),
    _TmnxL2tpPeerStatDraining_Type()
)
tmnxL2tpPeerStatDraining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatDraining.setStatus("current")


class _TmnxL2tpPeerStatUnreachable_Type(Integer32):
    """Custom type tmnxL2tpPeerStatUnreachable based on Integer32"""
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
        *(("unreachable", 1),
          ("reachable", 2),
          ("selectable", 3),
          ("blacklisted", 4))
    )


_TmnxL2tpPeerStatUnreachable_Type.__name__ = "Integer32"
_TmnxL2tpPeerStatUnreachable_Object = MibTableColumn
tmnxL2tpPeerStatUnreachable = _TmnxL2tpPeerStatUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 7),
    _TmnxL2tpPeerStatUnreachable_Type()
)
tmnxL2tpPeerStatUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatUnreachable.setStatus("current")
_TmnxL2tpPeerStatUnreachableTime_Type = TimeStamp
_TmnxL2tpPeerStatUnreachableTime_Object = MibTableColumn
tmnxL2tpPeerStatUnreachableTime = _TmnxL2tpPeerStatUnreachableTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 8),
    _TmnxL2tpPeerStatUnreachableTime_Type()
)
tmnxL2tpPeerStatUnreachableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatUnreachableTime.setStatus("current")
_TmnxL2tpPeerStatControlRxOct_Type = Counter64
_TmnxL2tpPeerStatControlRxOct_Object = MibTableColumn
tmnxL2tpPeerStatControlRxOct = _TmnxL2tpPeerStatControlRxOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 9),
    _TmnxL2tpPeerStatControlRxOct_Type()
)
tmnxL2tpPeerStatControlRxOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatControlRxOct.setStatus("current")
_TmnxL2tpPeerStatControlRxOctLw_Type = Counter32
_TmnxL2tpPeerStatControlRxOctLw_Object = MibTableColumn
tmnxL2tpPeerStatControlRxOctLw = _TmnxL2tpPeerStatControlRxOctLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 10),
    _TmnxL2tpPeerStatControlRxOctLw_Type()
)
tmnxL2tpPeerStatControlRxOctLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatControlRxOctLw.setStatus("current")
_TmnxL2tpPeerStatControlRxOctHw_Type = Counter32
_TmnxL2tpPeerStatControlRxOctHw_Object = MibTableColumn
tmnxL2tpPeerStatControlRxOctHw = _TmnxL2tpPeerStatControlRxOctHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 11),
    _TmnxL2tpPeerStatControlRxOctHw_Type()
)
tmnxL2tpPeerStatControlRxOctHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatControlRxOctHw.setStatus("current")
_TmnxL2tpPeerStatControlRxPkts_Type = Counter32
_TmnxL2tpPeerStatControlRxPkts_Object = MibTableColumn
tmnxL2tpPeerStatControlRxPkts = _TmnxL2tpPeerStatControlRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 12),
    _TmnxL2tpPeerStatControlRxPkts_Type()
)
tmnxL2tpPeerStatControlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatControlRxPkts.setStatus("current")
_TmnxL2tpPeerStatControlTxOct_Type = Counter64
_TmnxL2tpPeerStatControlTxOct_Object = MibTableColumn
tmnxL2tpPeerStatControlTxOct = _TmnxL2tpPeerStatControlTxOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 13),
    _TmnxL2tpPeerStatControlTxOct_Type()
)
tmnxL2tpPeerStatControlTxOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatControlTxOct.setStatus("current")
_TmnxL2tpPeerStatControlTxOctLw_Type = Counter32
_TmnxL2tpPeerStatControlTxOctLw_Object = MibTableColumn
tmnxL2tpPeerStatControlTxOctLw = _TmnxL2tpPeerStatControlTxOctLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 14),
    _TmnxL2tpPeerStatControlTxOctLw_Type()
)
tmnxL2tpPeerStatControlTxOctLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatControlTxOctLw.setStatus("current")
_TmnxL2tpPeerStatControlTxOctHw_Type = Counter32
_TmnxL2tpPeerStatControlTxOctHw_Object = MibTableColumn
tmnxL2tpPeerStatControlTxOctHw = _TmnxL2tpPeerStatControlTxOctHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 15),
    _TmnxL2tpPeerStatControlTxOctHw_Type()
)
tmnxL2tpPeerStatControlTxOctHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatControlTxOctHw.setStatus("current")
_TmnxL2tpPeerStatControlTxPkts_Type = Counter32
_TmnxL2tpPeerStatControlTxPkts_Object = MibTableColumn
tmnxL2tpPeerStatControlTxPkts = _TmnxL2tpPeerStatControlTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 16),
    _TmnxL2tpPeerStatControlTxPkts_Type()
)
tmnxL2tpPeerStatControlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatControlTxPkts.setStatus("current")
_TmnxL2tpPeerStatErrorTxPkts_Type = Counter32
_TmnxL2tpPeerStatErrorTxPkts_Object = MibTableColumn
tmnxL2tpPeerStatErrorTxPkts = _TmnxL2tpPeerStatErrorTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 17),
    _TmnxL2tpPeerStatErrorTxPkts_Type()
)
tmnxL2tpPeerStatErrorTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatErrorTxPkts.setStatus("current")
_TmnxL2tpPeerStatErrorRxPkts_Type = Counter32
_TmnxL2tpPeerStatErrorRxPkts_Object = MibTableColumn
tmnxL2tpPeerStatErrorRxPkts = _TmnxL2tpPeerStatErrorRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 18),
    _TmnxL2tpPeerStatErrorRxPkts_Type()
)
tmnxL2tpPeerStatErrorRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatErrorRxPkts.setStatus("current")
_TmnxL2tpPeerStatMsgAccepted_Type = Counter32
_TmnxL2tpPeerStatMsgAccepted_Object = MibTableColumn
tmnxL2tpPeerStatMsgAccepted = _TmnxL2tpPeerStatMsgAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 19),
    _TmnxL2tpPeerStatMsgAccepted_Type()
)
tmnxL2tpPeerStatMsgAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatMsgAccepted.setStatus("current")
_TmnxL2tpPeerStatMsgDuplicateRx_Type = Counter32
_TmnxL2tpPeerStatMsgDuplicateRx_Object = MibTableColumn
tmnxL2tpPeerStatMsgDuplicateRx = _TmnxL2tpPeerStatMsgDuplicateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 20),
    _TmnxL2tpPeerStatMsgDuplicateRx_Type()
)
tmnxL2tpPeerStatMsgDuplicateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatMsgDuplicateRx.setStatus("current")
_TmnxL2tpPeerStatMsgOutOfWndwRx_Type = Counter32
_TmnxL2tpPeerStatMsgOutOfWndwRx_Object = MibTableColumn
tmnxL2tpPeerStatMsgOutOfWndwRx = _TmnxL2tpPeerStatMsgOutOfWndwRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 21),
    _TmnxL2tpPeerStatMsgOutOfWndwRx_Type()
)
tmnxL2tpPeerStatMsgOutOfWndwRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatMsgOutOfWndwRx.setStatus("current")
_TmnxL2tpPeerStatRolesCapability_Type = TmnxL2tpRoles
_TmnxL2tpPeerStatRolesCapability_Object = MibTableColumn
tmnxL2tpPeerStatRolesCapability = _TmnxL2tpPeerStatRolesCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 22),
    _TmnxL2tpPeerStatRolesCapability_Type()
)
tmnxL2tpPeerStatRolesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatRolesCapability.setStatus("current")
_TmnxL2tpPeerStatRoles_Type = TmnxL2tpRoles
_TmnxL2tpPeerStatRoles_Object = MibTableColumn
tmnxL2tpPeerStatRoles = _TmnxL2tpPeerStatRoles_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 23),
    _TmnxL2tpPeerStatRoles_Type()
)
tmnxL2tpPeerStatRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatRoles.setStatus("current")
_TmnxL2tpPeerStatUnreachTimeRem_Type = Unsigned32
_TmnxL2tpPeerStatUnreachTimeRem_Object = MibTableColumn
tmnxL2tpPeerStatUnreachTimeRem = _TmnxL2tpPeerStatUnreachTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 24),
    _TmnxL2tpPeerStatUnreachTimeRem_Type()
)
tmnxL2tpPeerStatUnreachTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatUnreachTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatUnreachTimeRem.setUnits("seconds")
_TmnxL2tpPeerStatLastCleared_Type = TimeStamp
_TmnxL2tpPeerStatLastCleared_Object = MibTableColumn
tmnxL2tpPeerStatLastCleared = _TmnxL2tpPeerStatLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 1, 1, 99),
    _TmnxL2tpPeerStatLastCleared_Type()
)
tmnxL2tpPeerStatLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatLastCleared.setStatus("current")
_TmnxL2tpPeerTuTable_Object = MibTable
tmnxL2tpPeerTuTable = _TmnxL2tpPeerTuTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerTuTable.setStatus("current")
_TmnxL2tpPeerTuEntry_Object = MibTableRow
tmnxL2tpPeerTuEntry = _TmnxL2tpPeerTuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 2, 1)
)
tmnxL2tpPeerTuEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTransportType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPeerAddrType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPeerAddr"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRemoteUdpPort"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpPeerTuId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerTuEntry.setStatus("current")
_TmnxL2tpPeerTuId_Type = TmnxL2tpConnectionId
_TmnxL2tpPeerTuId_Object = MibTableColumn
tmnxL2tpPeerTuId = _TmnxL2tpPeerTuId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 2, 1, 1),
    _TmnxL2tpPeerTuId_Type()
)
tmnxL2tpPeerTuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerTuId.setStatus("current")
_TmnxL2tpPeerProtStatsTable_Object = MibTable
tmnxL2tpPeerProtStatsTable = _TmnxL2tpPeerProtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsTable.setStatus("current")
_TmnxL2tpPeerProtStatsEntry_Object = MibTableRow
tmnxL2tpPeerProtStatsEntry = _TmnxL2tpPeerProtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1)
)
tmnxL2tpPeerProtStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsTransport"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsAddrType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsAddr"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsRemUdpPort"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsInstance"),
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsEntry.setStatus("current")
_TmnxL2tpPeerProtStatsTransport_Type = TmnxL2tpTransportType
_TmnxL2tpPeerProtStatsTransport_Object = MibTableColumn
tmnxL2tpPeerProtStatsTransport = _TmnxL2tpPeerProtStatsTransport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1, 1),
    _TmnxL2tpPeerProtStatsTransport_Type()
)
tmnxL2tpPeerProtStatsTransport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsTransport.setStatus("current")
_TmnxL2tpPeerProtStatsAddrType_Type = InetAddressType
_TmnxL2tpPeerProtStatsAddrType_Object = MibTableColumn
tmnxL2tpPeerProtStatsAddrType = _TmnxL2tpPeerProtStatsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1, 2),
    _TmnxL2tpPeerProtStatsAddrType_Type()
)
tmnxL2tpPeerProtStatsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsAddrType.setStatus("current")


class _TmnxL2tpPeerProtStatsAddr_Type(InetAddress):
    """Custom type tmnxL2tpPeerProtStatsAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpPeerProtStatsAddr_Type.__name__ = "InetAddress"
_TmnxL2tpPeerProtStatsAddr_Object = MibTableColumn
tmnxL2tpPeerProtStatsAddr = _TmnxL2tpPeerProtStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1, 3),
    _TmnxL2tpPeerProtStatsAddr_Type()
)
tmnxL2tpPeerProtStatsAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsAddr.setStatus("current")
_TmnxL2tpPeerProtStatsRemUdpPort_Type = InetPortNumber
_TmnxL2tpPeerProtStatsRemUdpPort_Object = MibTableColumn
tmnxL2tpPeerProtStatsRemUdpPort = _TmnxL2tpPeerProtStatsRemUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1, 4),
    _TmnxL2tpPeerProtStatsRemUdpPort_Type()
)
tmnxL2tpPeerProtStatsRemUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsRemUdpPort.setStatus("current")
_TmnxL2tpPeerProtStatsType_Type = TmnxL2tpTuProtStatsType
_TmnxL2tpPeerProtStatsType_Object = MibTableColumn
tmnxL2tpPeerProtStatsType = _TmnxL2tpPeerProtStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1, 5),
    _TmnxL2tpPeerProtStatsType_Type()
)
tmnxL2tpPeerProtStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsType.setStatus("current")


class _TmnxL2tpPeerProtStatsInstance_Type(Unsigned32):
    """Custom type tmnxL2tpPeerProtStatsInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_TmnxL2tpPeerProtStatsInstance_Type.__name__ = "Unsigned32"
_TmnxL2tpPeerProtStatsInstance_Object = MibTableColumn
tmnxL2tpPeerProtStatsInstance = _TmnxL2tpPeerProtStatsInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1, 6),
    _TmnxL2tpPeerProtStatsInstance_Type()
)
tmnxL2tpPeerProtStatsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsInstance.setStatus("current")


class _TmnxL2tpPeerProtStatsName_Type(DisplayString):
    """Custom type tmnxL2tpPeerProtStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxL2tpPeerProtStatsName_Type.__name__ = "DisplayString"
_TmnxL2tpPeerProtStatsName_Object = MibTableColumn
tmnxL2tpPeerProtStatsName = _TmnxL2tpPeerProtStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1, 7),
    _TmnxL2tpPeerProtStatsName_Type()
)
tmnxL2tpPeerProtStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsName.setStatus("current")
_TmnxL2tpPeerProtStatsVal_Type = Counter32
_TmnxL2tpPeerProtStatsVal_Object = MibTableColumn
tmnxL2tpPeerProtStatsVal = _TmnxL2tpPeerProtStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 1, 3, 1, 8),
    _TmnxL2tpPeerProtStatsVal_Type()
)
tmnxL2tpPeerProtStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpPeerProtStatsVal.setStatus("current")
_TmnxL2tpPeerOpObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpPeerOpObjs = _TmnxL2tpPeerOpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 2)
)
_TmnxL2tpPeerDrainTable_Object = MibTable
tmnxL2tpPeerDrainTable = _TmnxL2tpPeerDrainTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerDrainTable.setStatus("current")
_TmnxL2tpPeerDrainEntry_Object = MibTableRow
tmnxL2tpPeerDrainEntry = _TmnxL2tpPeerDrainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 2, 1, 1)
)
tmnxL2tpPeerDrainEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTransportType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPeerAddrType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPeerAddr"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRemoteUdpPort"),
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerDrainEntry.setStatus("current")


class _TmnxL2tpPeerDrain_Type(TmnxL2tpActionTypeDrain):
    """Custom type tmnxL2tpPeerDrain based on TmnxL2tpActionTypeDrain"""
    defaultValue = 2


_TmnxL2tpPeerDrain_Type.__name__ = "TmnxL2tpActionTypeDrain"
_TmnxL2tpPeerDrain_Object = MibTableColumn
tmnxL2tpPeerDrain = _TmnxL2tpPeerDrain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 4, 2, 1, 1, 1),
    _TmnxL2tpPeerDrain_Type()
)
tmnxL2tpPeerDrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxL2tpPeerDrain.setStatus("current")
_TmnxL2tpSessionObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpSessionObjs = _TmnxL2tpSessionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5)
)
_TmnxL2tpSeStatObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpSeStatObjs = _TmnxL2tpSeStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1)
)
_TmnxL2tpSeStatusTable_Object = MibTable
tmnxL2tpSeStatusTable = _TmnxL2tpSeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusTable.setStatus("current")
_TmnxL2tpSeStatusEntry_Object = MibTableRow
tmnxL2tpSeStatusEntry = _TmnxL2tpSeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1)
)
tmnxL2tpSeStatusEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusEntry.setStatus("current")
_TmnxL2tpSeStatusId_Type = TmnxL2tpConnectionId
_TmnxL2tpSeStatusId_Object = MibTableColumn
tmnxL2tpSeStatusId = _TmnxL2tpSeStatusId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 1),
    _TmnxL2tpSeStatusId_Type()
)
tmnxL2tpSeStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusId.setStatus("current")
_TmnxL2tpSeStatusState_Type = TmnxL2tpSeOperState
_TmnxL2tpSeStatusState_Object = MibTableColumn
tmnxL2tpSeStatusState = _TmnxL2tpSeStatusState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 2),
    _TmnxL2tpSeStatusState_Type()
)
tmnxL2tpSeStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusState.setStatus("current")
_TmnxL2tpSeStatusTunnelId_Type = TmnxL2tpTunnelId
_TmnxL2tpSeStatusTunnelId_Object = MibTableColumn
tmnxL2tpSeStatusTunnelId = _TmnxL2tpSeStatusTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 3),
    _TmnxL2tpSeStatusTunnelId_Type()
)
tmnxL2tpSeStatusTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusTunnelId.setStatus("current")
_TmnxL2tpSeStatusTunnelConnId_Type = TmnxL2tpConnectionId
_TmnxL2tpSeStatusTunnelConnId_Object = MibTableColumn
tmnxL2tpSeStatusTunnelConnId = _TmnxL2tpSeStatusTunnelConnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 4),
    _TmnxL2tpSeStatusTunnelConnId_Type()
)
tmnxL2tpSeStatusTunnelConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusTunnelConnId.setStatus("current")
_TmnxL2tpSeStatusSessionId_Type = TmnxL2tpSessionId
_TmnxL2tpSeStatusSessionId_Object = MibTableColumn
tmnxL2tpSeStatusSessionId = _TmnxL2tpSeStatusSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 5),
    _TmnxL2tpSeStatusSessionId_Type()
)
tmnxL2tpSeStatusSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusSessionId.setStatus("current")
_TmnxL2tpSeStatusRemoteTunnelId_Type = TmnxL2tpTunnelId
_TmnxL2tpSeStatusRemoteTunnelId_Object = MibTableColumn
tmnxL2tpSeStatusRemoteTunnelId = _TmnxL2tpSeStatusRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 6),
    _TmnxL2tpSeStatusRemoteTunnelId_Type()
)
tmnxL2tpSeStatusRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusRemoteTunnelId.setStatus("current")
_TmnxL2tpSeStatusRemoteSessionId_Type = TmnxL2tpSessionId
_TmnxL2tpSeStatusRemoteSessionId_Object = MibTableColumn
tmnxL2tpSeStatusRemoteSessionId = _TmnxL2tpSeStatusRemoteSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 7),
    _TmnxL2tpSeStatusRemoteSessionId_Type()
)
tmnxL2tpSeStatusRemoteSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusRemoteSessionId.setStatus("current")
_TmnxL2tpSeStatusRemoteConnId_Type = TmnxL2tpConnectionId
_TmnxL2tpSeStatusRemoteConnId_Object = MibTableColumn
tmnxL2tpSeStatusRemoteConnId = _TmnxL2tpSeStatusRemoteConnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 8),
    _TmnxL2tpSeStatusRemoteConnId_Type()
)
tmnxL2tpSeStatusRemoteConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusRemoteConnId.setStatus("current")
_TmnxL2tpSeStatusStartTime_Type = TimeStamp
_TmnxL2tpSeStatusStartTime_Object = MibTableColumn
tmnxL2tpSeStatusStartTime = _TmnxL2tpSeStatusStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 9),
    _TmnxL2tpSeStatusStartTime_Type()
)
tmnxL2tpSeStatusStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusStartTime.setStatus("current")
_TmnxL2tpSeStatusEstabTime_Type = TimeStamp
_TmnxL2tpSeStatusEstabTime_Object = MibTableColumn
tmnxL2tpSeStatusEstabTime = _TmnxL2tpSeStatusEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 10),
    _TmnxL2tpSeStatusEstabTime_Type()
)
tmnxL2tpSeStatusEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusEstabTime.setStatus("current")
_TmnxL2tpSeStatusClosedTime_Type = TimeStamp
_TmnxL2tpSeStatusClosedTime_Object = MibTableColumn
tmnxL2tpSeStatusClosedTime = _TmnxL2tpSeStatusClosedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 11),
    _TmnxL2tpSeStatusClosedTime_Type()
)
tmnxL2tpSeStatusClosedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusClosedTime.setStatus("current")
_TmnxL2tpSeStatusCdnResult_Type = TmnxL2tpCdnResult
_TmnxL2tpSeStatusCdnResult_Object = MibTableColumn
tmnxL2tpSeStatusCdnResult = _TmnxL2tpSeStatusCdnResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 12),
    _TmnxL2tpSeStatusCdnResult_Type()
)
tmnxL2tpSeStatusCdnResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusCdnResult.setStatus("current")
_TmnxL2tpSeStatusGeneralError_Type = TmnxL2tpGeneralError
_TmnxL2tpSeStatusGeneralError_Object = MibTableColumn
tmnxL2tpSeStatusGeneralError = _TmnxL2tpSeStatusGeneralError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 13),
    _TmnxL2tpSeStatusGeneralError_Type()
)
tmnxL2tpSeStatusGeneralError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusGeneralError.setStatus("current")
_TmnxL2tpSeStatusErrorMessage_Type = TmnxL2tpErrorMessage
_TmnxL2tpSeStatusErrorMessage_Object = MibTableColumn
tmnxL2tpSeStatusErrorMessage = _TmnxL2tpSeStatusErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 14),
    _TmnxL2tpSeStatusErrorMessage_Type()
)
tmnxL2tpSeStatusErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusErrorMessage.setStatus("current")
_TmnxL2tpSeStatusMlpppBundleIndex_Type = Unsigned32
_TmnxL2tpSeStatusMlpppBundleIndex_Object = MibTableColumn
tmnxL2tpSeStatusMlpppBundleIndex = _TmnxL2tpSeStatusMlpppBundleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 1, 1, 20),
    _TmnxL2tpSeStatusMlpppBundleIndex_Type()
)
tmnxL2tpSeStatusMlpppBundleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusMlpppBundleIndex.setStatus("current")
_TmnxL2tpLnsSePppTable_Object = MibTable
tmnxL2tpLnsSePppTable = _TmnxL2tpLnsSePppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppTable.setStatus("current")
_TmnxL2tpLnsSePppEntry_Object = MibTableRow
tmnxL2tpLnsSePppEntry = _TmnxL2tpLnsSePppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1)
)
tmnxL2tpLnsSePppEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppEntry.setStatus("current")
_TmnxL2tpLnsSePppUpTime_Type = TimeTicks
_TmnxL2tpLnsSePppUpTime_Object = MibTableColumn
tmnxL2tpLnsSePppUpTime = _TmnxL2tpLnsSePppUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 3),
    _TmnxL2tpLnsSePppUpTime_Type()
)
tmnxL2tpLnsSePppUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppUpTime.setStatus("obsolete")
_TmnxL2tpLnsSePppLcpState_Type = TmnxPppCpState
_TmnxL2tpLnsSePppLcpState_Object = MibTableColumn
tmnxL2tpLnsSePppLcpState = _TmnxL2tpLnsSePppLcpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 4),
    _TmnxL2tpLnsSePppLcpState_Type()
)
tmnxL2tpLnsSePppLcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppLcpState.setStatus("obsolete")
_TmnxL2tpLnsSePppIpcpState_Type = TmnxPppCpState
_TmnxL2tpLnsSePppIpcpState_Object = MibTableColumn
tmnxL2tpLnsSePppIpcpState = _TmnxL2tpLnsSePppIpcpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 5),
    _TmnxL2tpLnsSePppIpcpState_Type()
)
tmnxL2tpLnsSePppIpcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpcpState.setStatus("obsolete")
_TmnxL2tpLnsSePppPppMtu_Type = Unsigned32
_TmnxL2tpLnsSePppPppMtu_Object = MibTableColumn
tmnxL2tpLnsSePppPppMtu = _TmnxL2tpLnsSePppPppMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 6),
    _TmnxL2tpLnsSePppPppMtu_Type()
)
tmnxL2tpLnsSePppPppMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppPppMtu.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppPppMtu.setUnits("bytes")


class _TmnxL2tpLnsSePppPppAuthProtocol_Type(Integer32):
    """Custom type tmnxL2tpLnsSePppPppAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pap", 2),
          ("chap", 3))
    )


_TmnxL2tpLnsSePppPppAuthProtocol_Type.__name__ = "Integer32"
_TmnxL2tpLnsSePppPppAuthProtocol_Object = MibTableColumn
tmnxL2tpLnsSePppPppAuthProtocol = _TmnxL2tpLnsSePppPppAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 7),
    _TmnxL2tpLnsSePppPppAuthProtocol_Type()
)
tmnxL2tpLnsSePppPppAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppPppAuthProtocol.setStatus("obsolete")
_TmnxL2tpLnsSePppPppUserName_Type = TmnxPppoeUserNameOrEmpty
_TmnxL2tpLnsSePppPppUserName_Object = MibTableColumn
tmnxL2tpLnsSePppPppUserName = _TmnxL2tpLnsSePppPppUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 8),
    _TmnxL2tpLnsSePppPppUserName_Type()
)
tmnxL2tpLnsSePppPppUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppPppUserName.setStatus("obsolete")
_TmnxL2tpLnsSePppSubIdent_Type = TmnxSubIdentStringOrEmpty
_TmnxL2tpLnsSePppSubIdent_Object = MibTableColumn
tmnxL2tpLnsSePppSubIdent = _TmnxL2tpLnsSePppSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 9),
    _TmnxL2tpLnsSePppSubIdent_Type()
)
tmnxL2tpLnsSePppSubIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSubIdent.setStatus("obsolete")
_TmnxL2tpLnsSePppOriginSubIdent_Type = TmnxPppoeSessionInfoOrigin
_TmnxL2tpLnsSePppOriginSubIdent_Object = MibTableColumn
tmnxL2tpLnsSePppOriginSubIdent = _TmnxL2tpLnsSePppOriginSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 10),
    _TmnxL2tpLnsSePppOriginSubIdent_Type()
)
tmnxL2tpLnsSePppOriginSubIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppOriginSubIdent.setStatus("obsolete")
_TmnxL2tpLnsSePppSubProfString_Type = TmnxSubProfileStringOrEmpty
_TmnxL2tpLnsSePppSubProfString_Object = MibTableColumn
tmnxL2tpLnsSePppSubProfString = _TmnxL2tpLnsSePppSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 11),
    _TmnxL2tpLnsSePppSubProfString_Type()
)
tmnxL2tpLnsSePppSubProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSubProfString.setStatus("obsolete")
_TmnxL2tpLnsSePppSlaProfString_Type = TmnxSlaProfileStringOrEmpty
_TmnxL2tpLnsSePppSlaProfString_Object = MibTableColumn
tmnxL2tpLnsSePppSlaProfString = _TmnxL2tpLnsSePppSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 12),
    _TmnxL2tpLnsSePppSlaProfString_Type()
)
tmnxL2tpLnsSePppSlaProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSlaProfString.setStatus("obsolete")
_TmnxL2tpLnsSePppAncpString_Type = TmnxAncpStringOrZero
_TmnxL2tpLnsSePppAncpString_Object = MibTableColumn
tmnxL2tpLnsSePppAncpString = _TmnxL2tpLnsSePppAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 13),
    _TmnxL2tpLnsSePppAncpString_Type()
)
tmnxL2tpLnsSePppAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppAncpString.setStatus("obsolete")
_TmnxL2tpLnsSePppInterDestId_Type = TmnxSubMgtIntDestIdOrEmpty
_TmnxL2tpLnsSePppInterDestId_Object = MibTableColumn
tmnxL2tpLnsSePppInterDestId = _TmnxL2tpLnsSePppInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 14),
    _TmnxL2tpLnsSePppInterDestId_Type()
)
tmnxL2tpLnsSePppInterDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppInterDestId.setStatus("obsolete")
_TmnxL2tpLnsSePppAppProfString_Type = TmnxAppProfileStringOrEmpty
_TmnxL2tpLnsSePppAppProfString_Object = MibTableColumn
tmnxL2tpLnsSePppAppProfString = _TmnxL2tpLnsSePppAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 15),
    _TmnxL2tpLnsSePppAppProfString_Type()
)
tmnxL2tpLnsSePppAppProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppAppProfString.setStatus("obsolete")
_TmnxL2tpLnsSePppOriginStrings_Type = TmnxPppoeSessionInfoOrigin
_TmnxL2tpLnsSePppOriginStrings_Object = MibTableColumn
tmnxL2tpLnsSePppOriginStrings = _TmnxL2tpLnsSePppOriginStrings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 16),
    _TmnxL2tpLnsSePppOriginStrings_Type()
)
tmnxL2tpLnsSePppOriginStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppOriginStrings.setStatus("obsolete")


class _TmnxL2tpLnsSePppSessionTimeout_Type(Unsigned32):
    """Custom type tmnxL2tpLnsSePppSessionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxL2tpLnsSePppSessionTimeout_Type.__name__ = "Unsigned32"
_TmnxL2tpLnsSePppSessionTimeout_Object = MibTableColumn
tmnxL2tpLnsSePppSessionTimeout = _TmnxL2tpLnsSePppSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 17),
    _TmnxL2tpLnsSePppSessionTimeout_Type()
)
tmnxL2tpLnsSePppSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSessionTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSessionTimeout.setUnits("seconds")
_TmnxL2tpLnsSePppIpAddrType_Type = InetAddressType
_TmnxL2tpLnsSePppIpAddrType_Object = MibTableColumn
tmnxL2tpLnsSePppIpAddrType = _TmnxL2tpLnsSePppIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 18),
    _TmnxL2tpLnsSePppIpAddrType_Type()
)
tmnxL2tpLnsSePppIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpAddrType.setStatus("obsolete")


class _TmnxL2tpLnsSePppIpAddr_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxL2tpLnsSePppIpAddr_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppIpAddr_Object = MibTableColumn
tmnxL2tpLnsSePppIpAddr = _TmnxL2tpLnsSePppIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 19),
    _TmnxL2tpLnsSePppIpAddr_Type()
)
tmnxL2tpLnsSePppIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpAddr.setStatus("obsolete")
_TmnxL2tpLnsSePppPrimaryDnsType_Type = InetAddressType
_TmnxL2tpLnsSePppPrimaryDnsType_Object = MibTableColumn
tmnxL2tpLnsSePppPrimaryDnsType = _TmnxL2tpLnsSePppPrimaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 20),
    _TmnxL2tpLnsSePppPrimaryDnsType_Type()
)
tmnxL2tpLnsSePppPrimaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppPrimaryDnsType.setStatus("obsolete")


class _TmnxL2tpLnsSePppPrimaryDns_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppPrimaryDns based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxL2tpLnsSePppPrimaryDns_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppPrimaryDns_Object = MibTableColumn
tmnxL2tpLnsSePppPrimaryDns = _TmnxL2tpLnsSePppPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 21),
    _TmnxL2tpLnsSePppPrimaryDns_Type()
)
tmnxL2tpLnsSePppPrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppPrimaryDns.setStatus("obsolete")
_TmnxL2tpLnsSePppSecondaryDnsType_Type = InetAddressType
_TmnxL2tpLnsSePppSecondaryDnsType_Object = MibTableColumn
tmnxL2tpLnsSePppSecondaryDnsType = _TmnxL2tpLnsSePppSecondaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 22),
    _TmnxL2tpLnsSePppSecondaryDnsType_Type()
)
tmnxL2tpLnsSePppSecondaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSecondaryDnsType.setStatus("obsolete")


class _TmnxL2tpLnsSePppSecondaryDns_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppSecondaryDns based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxL2tpLnsSePppSecondaryDns_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppSecondaryDns_Object = MibTableColumn
tmnxL2tpLnsSePppSecondaryDns = _TmnxL2tpLnsSePppSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 23),
    _TmnxL2tpLnsSePppSecondaryDns_Type()
)
tmnxL2tpLnsSePppSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSecondaryDns.setStatus("obsolete")
_TmnxL2tpLnsSePppPrimaryNbnsType_Type = InetAddressType
_TmnxL2tpLnsSePppPrimaryNbnsType_Object = MibTableColumn
tmnxL2tpLnsSePppPrimaryNbnsType = _TmnxL2tpLnsSePppPrimaryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 24),
    _TmnxL2tpLnsSePppPrimaryNbnsType_Type()
)
tmnxL2tpLnsSePppPrimaryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppPrimaryNbnsType.setStatus("obsolete")


class _TmnxL2tpLnsSePppPrimaryNbns_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppPrimaryNbns based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxL2tpLnsSePppPrimaryNbns_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppPrimaryNbns_Object = MibTableColumn
tmnxL2tpLnsSePppPrimaryNbns = _TmnxL2tpLnsSePppPrimaryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 25),
    _TmnxL2tpLnsSePppPrimaryNbns_Type()
)
tmnxL2tpLnsSePppPrimaryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppPrimaryNbns.setStatus("obsolete")
_TmnxL2tpLnsSePppSecondNbnsType_Type = InetAddressType
_TmnxL2tpLnsSePppSecondNbnsType_Object = MibTableColumn
tmnxL2tpLnsSePppSecondNbnsType = _TmnxL2tpLnsSePppSecondNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 26),
    _TmnxL2tpLnsSePppSecondNbnsType_Type()
)
tmnxL2tpLnsSePppSecondNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSecondNbnsType.setStatus("obsolete")


class _TmnxL2tpLnsSePppSecondNbns_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppSecondNbns based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxL2tpLnsSePppSecondNbns_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppSecondNbns_Object = MibTableColumn
tmnxL2tpLnsSePppSecondNbns = _TmnxL2tpLnsSePppSecondNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 27),
    _TmnxL2tpLnsSePppSecondNbns_Type()
)
tmnxL2tpLnsSePppSecondNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSecondNbns.setStatus("obsolete")
_TmnxL2tpLnsSePppOriginIpcpInfo_Type = TmnxPppoeSessionInfoOrigin
_TmnxL2tpLnsSePppOriginIpcpInfo_Object = MibTableColumn
tmnxL2tpLnsSePppOriginIpcpInfo = _TmnxL2tpLnsSePppOriginIpcpInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 28),
    _TmnxL2tpLnsSePppOriginIpcpInfo_Type()
)
tmnxL2tpLnsSePppOriginIpcpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppOriginIpcpInfo.setStatus("obsolete")


class _TmnxL2tpLnsSePppCircuitId_Type(OctetString):
    """Custom type tmnxL2tpLnsSePppCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxL2tpLnsSePppCircuitId_Type.__name__ = "OctetString"
_TmnxL2tpLnsSePppCircuitId_Object = MibTableColumn
tmnxL2tpLnsSePppCircuitId = _TmnxL2tpLnsSePppCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 29),
    _TmnxL2tpLnsSePppCircuitId_Type()
)
tmnxL2tpLnsSePppCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppCircuitId.setStatus("obsolete")


class _TmnxL2tpLnsSePppRemoteId_Type(OctetString):
    """Custom type tmnxL2tpLnsSePppRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxL2tpLnsSePppRemoteId_Type.__name__ = "OctetString"
_TmnxL2tpLnsSePppRemoteId_Object = MibTableColumn
tmnxL2tpLnsSePppRemoteId = _TmnxL2tpLnsSePppRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 30),
    _TmnxL2tpLnsSePppRemoteId_Type()
)
tmnxL2tpLnsSePppRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppRemoteId.setStatus("obsolete")


class _TmnxL2tpLnsSePppAddressPool_Type(DisplayString):
    """Custom type tmnxL2tpLnsSePppAddressPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxL2tpLnsSePppAddressPool_Type.__name__ = "DisplayString"
_TmnxL2tpLnsSePppAddressPool_Object = MibTableColumn
tmnxL2tpLnsSePppAddressPool = _TmnxL2tpLnsSePppAddressPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 31),
    _TmnxL2tpLnsSePppAddressPool_Type()
)
tmnxL2tpLnsSePppAddressPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppAddressPool.setStatus("obsolete")
_TmnxL2tpLnsSePppType_Type = TmnxPppoeSessionType
_TmnxL2tpLnsSePppType_Object = MibTableColumn
tmnxL2tpLnsSePppType = _TmnxL2tpLnsSePppType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 32),
    _TmnxL2tpLnsSePppType_Type()
)
tmnxL2tpLnsSePppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppType.setStatus("obsolete")
_TmnxL2tpLnsSePppSvcId_Type = TmnxServId
_TmnxL2tpLnsSePppSvcId_Object = MibTableColumn
tmnxL2tpLnsSePppSvcId = _TmnxL2tpLnsSePppSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 33),
    _TmnxL2tpLnsSePppSvcId_Type()
)
tmnxL2tpLnsSePppSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSvcId.setStatus("obsolete")
_TmnxL2tpLnsSePppGrpIf_Type = InterfaceIndexOrZero
_TmnxL2tpLnsSePppGrpIf_Object = MibTableColumn
tmnxL2tpLnsSePppGrpIf = _TmnxL2tpLnsSePppGrpIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 34),
    _TmnxL2tpLnsSePppGrpIf_Type()
)
tmnxL2tpLnsSePppGrpIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppGrpIf.setStatus("obsolete")
_TmnxL2tpLnsSePppL2tpVrtrId_Type = TmnxVRtrIDOrZero
_TmnxL2tpLnsSePppL2tpVrtrId_Object = MibTableColumn
tmnxL2tpLnsSePppL2tpVrtrId = _TmnxL2tpLnsSePppL2tpVrtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 35),
    _TmnxL2tpLnsSePppL2tpVrtrId_Type()
)
tmnxL2tpLnsSePppL2tpVrtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppL2tpVrtrId.setStatus("obsolete")
_TmnxL2tpLnsSePppL2tpConnectionId_Type = Unsigned32
_TmnxL2tpLnsSePppL2tpConnectionId_Object = MibTableColumn
tmnxL2tpLnsSePppL2tpConnectionId = _TmnxL2tpLnsSePppL2tpConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 36),
    _TmnxL2tpLnsSePppL2tpConnectionId_Type()
)
tmnxL2tpLnsSePppL2tpConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppL2tpConnectionId.setStatus("obsolete")
_TmnxL2tpLnsSePppCategoryMapName_Type = TNamedItemOrEmpty
_TmnxL2tpLnsSePppCategoryMapName_Object = MibTableColumn
tmnxL2tpLnsSePppCategoryMapName = _TmnxL2tpLnsSePppCategoryMapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 37),
    _TmnxL2tpLnsSePppCategoryMapName_Type()
)
tmnxL2tpLnsSePppCategoryMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppCategoryMapName.setStatus("obsolete")


class _TmnxL2tpLnsSePppRadiusClassAttr_Type(OctetString):
    """Custom type tmnxL2tpLnsSePppRadiusClassAttr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxL2tpLnsSePppRadiusClassAttr_Type.__name__ = "OctetString"
_TmnxL2tpLnsSePppRadiusClassAttr_Object = MibTableColumn
tmnxL2tpLnsSePppRadiusClassAttr = _TmnxL2tpLnsSePppRadiusClassAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 38),
    _TmnxL2tpLnsSePppRadiusClassAttr_Type()
)
tmnxL2tpLnsSePppRadiusClassAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppRadiusClassAttr.setStatus("obsolete")


class _TmnxL2tpLnsSePppRadiusUserName_Type(DisplayString):
    """Custom type tmnxL2tpLnsSePppRadiusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TmnxL2tpLnsSePppRadiusUserName_Type.__name__ = "DisplayString"
_TmnxL2tpLnsSePppRadiusUserName_Object = MibTableColumn
tmnxL2tpLnsSePppRadiusUserName = _TmnxL2tpLnsSePppRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 39),
    _TmnxL2tpLnsSePppRadiusUserName_Type()
)
tmnxL2tpLnsSePppRadiusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppRadiusUserName.setStatus("obsolete")
_TmnxL2tpLnsSePppIpv6cpState_Type = TmnxPppCpState
_TmnxL2tpLnsSePppIpv6cpState_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6cpState = _TmnxL2tpLnsSePppIpv6cpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 40),
    _TmnxL2tpLnsSePppIpv6cpState_Type()
)
tmnxL2tpLnsSePppIpv6cpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6cpState.setStatus("obsolete")


class _TmnxL2tpLnsSePppInterfaceId_Type(OctetString):
    """Custom type tmnxL2tpLnsSePppInterfaceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxL2tpLnsSePppInterfaceId_Type.__name__ = "OctetString"
_TmnxL2tpLnsSePppInterfaceId_Object = MibTableColumn
tmnxL2tpLnsSePppInterfaceId = _TmnxL2tpLnsSePppInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 41),
    _TmnxL2tpLnsSePppInterfaceId_Type()
)
tmnxL2tpLnsSePppInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppInterfaceId.setStatus("obsolete")
_TmnxL2tpLnsSePppOriginIpv6cpInfo_Type = TmnxPppoeSessionInfoOrigin
_TmnxL2tpLnsSePppOriginIpv6cpInfo_Object = MibTableColumn
tmnxL2tpLnsSePppOriginIpv6cpInfo = _TmnxL2tpLnsSePppOriginIpv6cpInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 42),
    _TmnxL2tpLnsSePppOriginIpv6cpInfo_Type()
)
tmnxL2tpLnsSePppOriginIpv6cpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppOriginIpv6cpInfo.setStatus("obsolete")
_TmnxL2tpLnsSePppIpv6DnsType_Type = InetAddressType
_TmnxL2tpLnsSePppIpv6DnsType_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6DnsType = _TmnxL2tpLnsSePppIpv6DnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 43),
    _TmnxL2tpLnsSePppIpv6DnsType_Type()
)
tmnxL2tpLnsSePppIpv6DnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6DnsType.setStatus("obsolete")


class _TmnxL2tpLnsSePppIpv6Dns1_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppIpv6Dns1 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpLnsSePppIpv6Dns1_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppIpv6Dns1_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6Dns1 = _TmnxL2tpLnsSePppIpv6Dns1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 44),
    _TmnxL2tpLnsSePppIpv6Dns1_Type()
)
tmnxL2tpLnsSePppIpv6Dns1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6Dns1.setStatus("obsolete")


class _TmnxL2tpLnsSePppIpv6Dns2_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppIpv6Dns2 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpLnsSePppIpv6Dns2_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppIpv6Dns2_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6Dns2 = _TmnxL2tpLnsSePppIpv6Dns2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 45),
    _TmnxL2tpLnsSePppIpv6Dns2_Type()
)
tmnxL2tpLnsSePppIpv6Dns2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6Dns2.setStatus("obsolete")
_TmnxL2tpLnsSePppIpv6DelPfxType_Type = InetAddressType
_TmnxL2tpLnsSePppIpv6DelPfxType_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6DelPfxType = _TmnxL2tpLnsSePppIpv6DelPfxType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 46),
    _TmnxL2tpLnsSePppIpv6DelPfxType_Type()
)
tmnxL2tpLnsSePppIpv6DelPfxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6DelPfxType.setStatus("obsolete")


class _TmnxL2tpLnsSePppIpv6DelPfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxL2tpLnsSePppIpv6DelPfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxL2tpLnsSePppIpv6DelPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxL2tpLnsSePppIpv6DelPfxLen_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6DelPfxLen = _TmnxL2tpLnsSePppIpv6DelPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 47),
    _TmnxL2tpLnsSePppIpv6DelPfxLen_Type()
)
tmnxL2tpLnsSePppIpv6DelPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6DelPfxLen.setStatus("obsolete")


class _TmnxL2tpLnsSePppIpv6DelPfx_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppIpv6DelPfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpLnsSePppIpv6DelPfx_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppIpv6DelPfx_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6DelPfx = _TmnxL2tpLnsSePppIpv6DelPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 48),
    _TmnxL2tpLnsSePppIpv6DelPfx_Type()
)
tmnxL2tpLnsSePppIpv6DelPfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6DelPfx.setStatus("obsolete")
_TmnxL2tpLnsSePppIpv6PrefixType_Type = InetAddressType
_TmnxL2tpLnsSePppIpv6PrefixType_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6PrefixType = _TmnxL2tpLnsSePppIpv6PrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 49),
    _TmnxL2tpLnsSePppIpv6PrefixType_Type()
)
tmnxL2tpLnsSePppIpv6PrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6PrefixType.setStatus("obsolete")


class _TmnxL2tpLnsSePppIpv6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxL2tpLnsSePppIpv6PrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxL2tpLnsSePppIpv6PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxL2tpLnsSePppIpv6PrefixLen_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6PrefixLen = _TmnxL2tpLnsSePppIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 50),
    _TmnxL2tpLnsSePppIpv6PrefixLen_Type()
)
tmnxL2tpLnsSePppIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6PrefixLen.setStatus("obsolete")


class _TmnxL2tpLnsSePppIpv6Prefix_Type(InetAddress):
    """Custom type tmnxL2tpLnsSePppIpv6Prefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpLnsSePppIpv6Prefix_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSePppIpv6Prefix_Object = MibTableColumn
tmnxL2tpLnsSePppIpv6Prefix = _TmnxL2tpLnsSePppIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 51),
    _TmnxL2tpLnsSePppIpv6Prefix_Type()
)
tmnxL2tpLnsSePppIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppIpv6Prefix.setStatus("obsolete")
_TmnxL2tpLnsSePppSubPppIndex_Type = Unsigned32
_TmnxL2tpLnsSePppSubPppIndex_Object = MibTableColumn
tmnxL2tpLnsSePppSubPppIndex = _TmnxL2tpLnsSePppSubPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 2, 1, 52),
    _TmnxL2tpLnsSePppSubPppIndex_Type()
)
tmnxL2tpLnsSePppSubPppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSubPppIndex.setStatus("current")
_TmnxL2tpLnsSePppStatTable_Object = MibTable
tmnxL2tpLnsSePppStatTable = _TmnxL2tpLnsSePppStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTable.setStatus("obsolete")
_TmnxL2tpLnsSePppStatEntry_Object = MibTableRow
tmnxL2tpLnsSePppStatEntry = _TmnxL2tpLnsSePppStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1)
)
tmnxL2tpLnsSePppStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatEntry.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxUnkwnProto_Type = Counter32
_TmnxL2tpLnsSePppStatRxUnkwnProto_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxUnkwnProto = _TmnxL2tpLnsSePppStatRxUnkwnProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 2),
    _TmnxL2tpLnsSePppStatRxUnkwnProto_Type()
)
tmnxL2tpLnsSePppStatRxUnkwnProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxUnkwnProto.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpConfRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpConfRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpConfRq = _TmnxL2tpLnsSePppStatRxLcpConfRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 3),
    _TmnxL2tpLnsSePppStatRxLcpConfRq_Type()
)
tmnxL2tpLnsSePppStatRxLcpConfRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpConfRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpConfAk_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpConfAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpConfAk = _TmnxL2tpLnsSePppStatRxLcpConfAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 4),
    _TmnxL2tpLnsSePppStatRxLcpConfAk_Type()
)
tmnxL2tpLnsSePppStatRxLcpConfAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpConfAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpConfNk_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpConfNk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpConfNk = _TmnxL2tpLnsSePppStatRxLcpConfNk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 5),
    _TmnxL2tpLnsSePppStatRxLcpConfNk_Type()
)
tmnxL2tpLnsSePppStatRxLcpConfNk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpConfNk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpConfRj_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpConfRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpConfRj = _TmnxL2tpLnsSePppStatRxLcpConfRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 6),
    _TmnxL2tpLnsSePppStatRxLcpConfRj_Type()
)
tmnxL2tpLnsSePppStatRxLcpConfRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpConfRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpTermRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpTermRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpTermRq = _TmnxL2tpLnsSePppStatRxLcpTermRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 7),
    _TmnxL2tpLnsSePppStatRxLcpTermRq_Type()
)
tmnxL2tpLnsSePppStatRxLcpTermRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpTermRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpTermAk_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpTermAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpTermAk = _TmnxL2tpLnsSePppStatRxLcpTermAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 8),
    _TmnxL2tpLnsSePppStatRxLcpTermAk_Type()
)
tmnxL2tpLnsSePppStatRxLcpTermAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpTermAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpCodeRj_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpCodeRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpCodeRj = _TmnxL2tpLnsSePppStatRxLcpCodeRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 9),
    _TmnxL2tpLnsSePppStatRxLcpCodeRj_Type()
)
tmnxL2tpLnsSePppStatRxLcpCodeRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpCodeRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpEchoRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpEchoRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpEchoRq = _TmnxL2tpLnsSePppStatRxLcpEchoRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 10),
    _TmnxL2tpLnsSePppStatRxLcpEchoRq_Type()
)
tmnxL2tpLnsSePppStatRxLcpEchoRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpEchoRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpEchoRep_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpEchoRep_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpEchoRep = _TmnxL2tpLnsSePppStatRxLcpEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 11),
    _TmnxL2tpLnsSePppStatRxLcpEchoRep_Type()
)
tmnxL2tpLnsSePppStatRxLcpEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpEchoRep.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpProtRj_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpProtRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpProtRj = _TmnxL2tpLnsSePppStatRxLcpProtRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 12),
    _TmnxL2tpLnsSePppStatRxLcpProtRj_Type()
)
tmnxL2tpLnsSePppStatRxLcpProtRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpProtRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxLcpDiscRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxLcpDiscRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxLcpDiscRq = _TmnxL2tpLnsSePppStatRxLcpDiscRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 13),
    _TmnxL2tpLnsSePppStatRxLcpDiscRq_Type()
)
tmnxL2tpLnsSePppStatRxLcpDiscRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxLcpDiscRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpConfRq_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpConfRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpConfRq = _TmnxL2tpLnsSePppStatTxLcpConfRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 14),
    _TmnxL2tpLnsSePppStatTxLcpConfRq_Type()
)
tmnxL2tpLnsSePppStatTxLcpConfRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpConfRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpConfAk_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpConfAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpConfAk = _TmnxL2tpLnsSePppStatTxLcpConfAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 15),
    _TmnxL2tpLnsSePppStatTxLcpConfAk_Type()
)
tmnxL2tpLnsSePppStatTxLcpConfAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpConfAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpConfNk_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpConfNk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpConfNk = _TmnxL2tpLnsSePppStatTxLcpConfNk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 16),
    _TmnxL2tpLnsSePppStatTxLcpConfNk_Type()
)
tmnxL2tpLnsSePppStatTxLcpConfNk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpConfNk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpConfRj_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpConfRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpConfRj = _TmnxL2tpLnsSePppStatTxLcpConfRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 17),
    _TmnxL2tpLnsSePppStatTxLcpConfRj_Type()
)
tmnxL2tpLnsSePppStatTxLcpConfRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpConfRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpTermRq_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpTermRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpTermRq = _TmnxL2tpLnsSePppStatTxLcpTermRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 18),
    _TmnxL2tpLnsSePppStatTxLcpTermRq_Type()
)
tmnxL2tpLnsSePppStatTxLcpTermRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpTermRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpTermAk_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpTermAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpTermAk = _TmnxL2tpLnsSePppStatTxLcpTermAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 19),
    _TmnxL2tpLnsSePppStatTxLcpTermAk_Type()
)
tmnxL2tpLnsSePppStatTxLcpTermAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpTermAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpCodeRj_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpCodeRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpCodeRj = _TmnxL2tpLnsSePppStatTxLcpCodeRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 20),
    _TmnxL2tpLnsSePppStatTxLcpCodeRj_Type()
)
tmnxL2tpLnsSePppStatTxLcpCodeRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpCodeRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpEchoRq_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpEchoRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpEchoRq = _TmnxL2tpLnsSePppStatTxLcpEchoRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 21),
    _TmnxL2tpLnsSePppStatTxLcpEchoRq_Type()
)
tmnxL2tpLnsSePppStatTxLcpEchoRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpEchoRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpEchoRep_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpEchoRep_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpEchoRep = _TmnxL2tpLnsSePppStatTxLcpEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 22),
    _TmnxL2tpLnsSePppStatTxLcpEchoRep_Type()
)
tmnxL2tpLnsSePppStatTxLcpEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpEchoRep.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpProtRj_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpProtRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpProtRj = _TmnxL2tpLnsSePppStatTxLcpProtRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 23),
    _TmnxL2tpLnsSePppStatTxLcpProtRj_Type()
)
tmnxL2tpLnsSePppStatTxLcpProtRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpProtRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxLcpDiscRq_Type = Counter32
_TmnxL2tpLnsSePppStatTxLcpDiscRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxLcpDiscRq = _TmnxL2tpLnsSePppStatTxLcpDiscRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 24),
    _TmnxL2tpLnsSePppStatTxLcpDiscRq_Type()
)
tmnxL2tpLnsSePppStatTxLcpDiscRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxLcpDiscRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxPapAuthRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxPapAuthRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxPapAuthRq = _TmnxL2tpLnsSePppStatRxPapAuthRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 25),
    _TmnxL2tpLnsSePppStatRxPapAuthRq_Type()
)
tmnxL2tpLnsSePppStatRxPapAuthRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxPapAuthRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxPapAuthAk_Type = Counter32
_TmnxL2tpLnsSePppStatTxPapAuthAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxPapAuthAk = _TmnxL2tpLnsSePppStatTxPapAuthAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 26),
    _TmnxL2tpLnsSePppStatTxPapAuthAk_Type()
)
tmnxL2tpLnsSePppStatTxPapAuthAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxPapAuthAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxPapAuthNk_Type = Counter32
_TmnxL2tpLnsSePppStatTxPapAuthNk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxPapAuthNk = _TmnxL2tpLnsSePppStatTxPapAuthNk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 27),
    _TmnxL2tpLnsSePppStatTxPapAuthNk_Type()
)
tmnxL2tpLnsSePppStatTxPapAuthNk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxPapAuthNk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxChapResp_Type = Counter32
_TmnxL2tpLnsSePppStatRxChapResp_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxChapResp = _TmnxL2tpLnsSePppStatRxChapResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 28),
    _TmnxL2tpLnsSePppStatRxChapResp_Type()
)
tmnxL2tpLnsSePppStatRxChapResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxChapResp.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxChapChall_Type = Counter32
_TmnxL2tpLnsSePppStatTxChapChall_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxChapChall = _TmnxL2tpLnsSePppStatTxChapChall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 29),
    _TmnxL2tpLnsSePppStatTxChapChall_Type()
)
tmnxL2tpLnsSePppStatTxChapChall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxChapChall.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxChapSucc_Type = Counter32
_TmnxL2tpLnsSePppStatTxChapSucc_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxChapSucc = _TmnxL2tpLnsSePppStatTxChapSucc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 30),
    _TmnxL2tpLnsSePppStatTxChapSucc_Type()
)
tmnxL2tpLnsSePppStatTxChapSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxChapSucc.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxChapFail_Type = Counter32
_TmnxL2tpLnsSePppStatTxChapFail_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxChapFail = _TmnxL2tpLnsSePppStatTxChapFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 31),
    _TmnxL2tpLnsSePppStatTxChapFail_Type()
)
tmnxL2tpLnsSePppStatTxChapFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxChapFail.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpcpConfRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpcpConfRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpcpConfRq = _TmnxL2tpLnsSePppStatRxIpcpConfRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 32),
    _TmnxL2tpLnsSePppStatRxIpcpConfRq_Type()
)
tmnxL2tpLnsSePppStatRxIpcpConfRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpcpConfRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpcpConfAk_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpcpConfAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpcpConfAk = _TmnxL2tpLnsSePppStatRxIpcpConfAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 33),
    _TmnxL2tpLnsSePppStatRxIpcpConfAk_Type()
)
tmnxL2tpLnsSePppStatRxIpcpConfAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpcpConfAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpcpConfNk_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpcpConfNk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpcpConfNk = _TmnxL2tpLnsSePppStatRxIpcpConfNk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 34),
    _TmnxL2tpLnsSePppStatRxIpcpConfNk_Type()
)
tmnxL2tpLnsSePppStatRxIpcpConfNk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpcpConfNk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpcpConfRj_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpcpConfRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpcpConfRj = _TmnxL2tpLnsSePppStatRxIpcpConfRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 35),
    _TmnxL2tpLnsSePppStatRxIpcpConfRj_Type()
)
tmnxL2tpLnsSePppStatRxIpcpConfRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpcpConfRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpcpTermRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpcpTermRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpcpTermRq = _TmnxL2tpLnsSePppStatRxIpcpTermRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 36),
    _TmnxL2tpLnsSePppStatRxIpcpTermRq_Type()
)
tmnxL2tpLnsSePppStatRxIpcpTermRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpcpTermRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpcpTermAk_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpcpTermAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpcpTermAk = _TmnxL2tpLnsSePppStatRxIpcpTermAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 37),
    _TmnxL2tpLnsSePppStatRxIpcpTermAk_Type()
)
tmnxL2tpLnsSePppStatRxIpcpTermAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpcpTermAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpcpCodeRj_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpcpCodeRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpcpCodeRj = _TmnxL2tpLnsSePppStatRxIpcpCodeRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 38),
    _TmnxL2tpLnsSePppStatRxIpcpCodeRj_Type()
)
tmnxL2tpLnsSePppStatRxIpcpCodeRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpcpCodeRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpcpConfRq_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpcpConfRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpcpConfRq = _TmnxL2tpLnsSePppStatTxIpcpConfRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 39),
    _TmnxL2tpLnsSePppStatTxIpcpConfRq_Type()
)
tmnxL2tpLnsSePppStatTxIpcpConfRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpcpConfRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpcpConfAk_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpcpConfAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpcpConfAk = _TmnxL2tpLnsSePppStatTxIpcpConfAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 40),
    _TmnxL2tpLnsSePppStatTxIpcpConfAk_Type()
)
tmnxL2tpLnsSePppStatTxIpcpConfAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpcpConfAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpcpConfNk_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpcpConfNk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpcpConfNk = _TmnxL2tpLnsSePppStatTxIpcpConfNk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 41),
    _TmnxL2tpLnsSePppStatTxIpcpConfNk_Type()
)
tmnxL2tpLnsSePppStatTxIpcpConfNk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpcpConfNk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpcpConfRj_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpcpConfRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpcpConfRj = _TmnxL2tpLnsSePppStatTxIpcpConfRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 42),
    _TmnxL2tpLnsSePppStatTxIpcpConfRj_Type()
)
tmnxL2tpLnsSePppStatTxIpcpConfRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpcpConfRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpcpTermRq_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpcpTermRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpcpTermRq = _TmnxL2tpLnsSePppStatTxIpcpTermRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 43),
    _TmnxL2tpLnsSePppStatTxIpcpTermRq_Type()
)
tmnxL2tpLnsSePppStatTxIpcpTermRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpcpTermRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpcpTermAk_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpcpTermAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpcpTermAk = _TmnxL2tpLnsSePppStatTxIpcpTermAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 44),
    _TmnxL2tpLnsSePppStatTxIpcpTermAk_Type()
)
tmnxL2tpLnsSePppStatTxIpcpTermAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpcpTermAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpcpCodeRj_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpcpCodeRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpcpCodeRj = _TmnxL2tpLnsSePppStatTxIpcpCodeRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 45),
    _TmnxL2tpLnsSePppStatTxIpcpCodeRj_Type()
)
tmnxL2tpLnsSePppStatTxIpcpCodeRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpcpCodeRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpv6cpCfRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpv6cpCfRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpv6cpCfRq = _TmnxL2tpLnsSePppStatRxIpv6cpCfRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 46),
    _TmnxL2tpLnsSePppStatRxIpv6cpCfRq_Type()
)
tmnxL2tpLnsSePppStatRxIpv6cpCfRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpv6cpCfRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpv6cpCfAk_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpv6cpCfAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpv6cpCfAk = _TmnxL2tpLnsSePppStatRxIpv6cpCfAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 47),
    _TmnxL2tpLnsSePppStatRxIpv6cpCfAk_Type()
)
tmnxL2tpLnsSePppStatRxIpv6cpCfAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpv6cpCfAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpv6cpCfNk_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpv6cpCfNk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpv6cpCfNk = _TmnxL2tpLnsSePppStatRxIpv6cpCfNk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 48),
    _TmnxL2tpLnsSePppStatRxIpv6cpCfNk_Type()
)
tmnxL2tpLnsSePppStatRxIpv6cpCfNk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpv6cpCfNk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpv6cpCfRj_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpv6cpCfRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpv6cpCfRj = _TmnxL2tpLnsSePppStatRxIpv6cpCfRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 49),
    _TmnxL2tpLnsSePppStatRxIpv6cpCfRj_Type()
)
tmnxL2tpLnsSePppStatRxIpv6cpCfRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpv6cpCfRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpv6cpTmRq_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpv6cpTmRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpv6cpTmRq = _TmnxL2tpLnsSePppStatRxIpv6cpTmRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 50),
    _TmnxL2tpLnsSePppStatRxIpv6cpTmRq_Type()
)
tmnxL2tpLnsSePppStatRxIpv6cpTmRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpv6cpTmRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpv6cpTmAk_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpv6cpTmAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpv6cpTmAk = _TmnxL2tpLnsSePppStatRxIpv6cpTmAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 51),
    _TmnxL2tpLnsSePppStatRxIpv6cpTmAk_Type()
)
tmnxL2tpLnsSePppStatRxIpv6cpTmAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpv6cpTmAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatRxIpv6cpCdRj_Type = Counter32
_TmnxL2tpLnsSePppStatRxIpv6cpCdRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatRxIpv6cpCdRj = _TmnxL2tpLnsSePppStatRxIpv6cpCdRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 52),
    _TmnxL2tpLnsSePppStatRxIpv6cpCdRj_Type()
)
tmnxL2tpLnsSePppStatRxIpv6cpCdRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatRxIpv6cpCdRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpv6cpCfRq_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpv6cpCfRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpv6cpCfRq = _TmnxL2tpLnsSePppStatTxIpv6cpCfRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 53),
    _TmnxL2tpLnsSePppStatTxIpv6cpCfRq_Type()
)
tmnxL2tpLnsSePppStatTxIpv6cpCfRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpv6cpCfRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpv6cpCfAk_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpv6cpCfAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpv6cpCfAk = _TmnxL2tpLnsSePppStatTxIpv6cpCfAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 54),
    _TmnxL2tpLnsSePppStatTxIpv6cpCfAk_Type()
)
tmnxL2tpLnsSePppStatTxIpv6cpCfAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpv6cpCfAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpv6cpCfNk_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpv6cpCfNk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpv6cpCfNk = _TmnxL2tpLnsSePppStatTxIpv6cpCfNk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 55),
    _TmnxL2tpLnsSePppStatTxIpv6cpCfNk_Type()
)
tmnxL2tpLnsSePppStatTxIpv6cpCfNk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpv6cpCfNk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpv6cpCfRj_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpv6cpCfRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpv6cpCfRj = _TmnxL2tpLnsSePppStatTxIpv6cpCfRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 56),
    _TmnxL2tpLnsSePppStatTxIpv6cpCfRj_Type()
)
tmnxL2tpLnsSePppStatTxIpv6cpCfRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpv6cpCfRj.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpv6cpTmRq_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpv6cpTmRq_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpv6cpTmRq = _TmnxL2tpLnsSePppStatTxIpv6cpTmRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 57),
    _TmnxL2tpLnsSePppStatTxIpv6cpTmRq_Type()
)
tmnxL2tpLnsSePppStatTxIpv6cpTmRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpv6cpTmRq.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpv6cpTmAk_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpv6cpTmAk_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpv6cpTmAk = _TmnxL2tpLnsSePppStatTxIpv6cpTmAk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 58),
    _TmnxL2tpLnsSePppStatTxIpv6cpTmAk_Type()
)
tmnxL2tpLnsSePppStatTxIpv6cpTmAk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpv6cpTmAk.setStatus("obsolete")
_TmnxL2tpLnsSePppStatTxIpv6cpCdRj_Type = Counter32
_TmnxL2tpLnsSePppStatTxIpv6cpCdRj_Object = MibTableColumn
tmnxL2tpLnsSePppStatTxIpv6cpCdRj = _TmnxL2tpLnsSePppStatTxIpv6cpCdRj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 3, 1, 59),
    _TmnxL2tpLnsSePppStatTxIpv6cpCdRj_Type()
)
tmnxL2tpLnsSePppStatTxIpv6cpCdRj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppStatTxIpv6cpCdRj.setStatus("obsolete")
_TmnxL2tpLnsSeMRtTable_Object = MibTable
tmnxL2tpLnsSeMRtTable = _TmnxL2tpLnsSeMRtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeMRtTable.setStatus("obsolete")
_TmnxL2tpLnsSeMRtEntry_Object = MibTableRow
tmnxL2tpLnsSeMRtEntry = _TmnxL2tpLnsSeMRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 4, 1)
)
tmnxL2tpLnsSeMRtEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusId"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeMRtAddrType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeMRtAddr"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeMRtPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeMRtEntry.setStatus("obsolete")
_TmnxL2tpLnsSeMRtAddrType_Type = InetAddressType
_TmnxL2tpLnsSeMRtAddrType_Object = MibTableColumn
tmnxL2tpLnsSeMRtAddrType = _TmnxL2tpLnsSeMRtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 4, 1, 1),
    _TmnxL2tpLnsSeMRtAddrType_Type()
)
tmnxL2tpLnsSeMRtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeMRtAddrType.setStatus("obsolete")


class _TmnxL2tpLnsSeMRtAddr_Type(InetAddress):
    """Custom type tmnxL2tpLnsSeMRtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpLnsSeMRtAddr_Type.__name__ = "InetAddress"
_TmnxL2tpLnsSeMRtAddr_Object = MibTableColumn
tmnxL2tpLnsSeMRtAddr = _TmnxL2tpLnsSeMRtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 4, 1, 2),
    _TmnxL2tpLnsSeMRtAddr_Type()
)
tmnxL2tpLnsSeMRtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeMRtAddr.setStatus("obsolete")
_TmnxL2tpLnsSeMRtPrefixLen_Type = InetAddressPrefixLength
_TmnxL2tpLnsSeMRtPrefixLen_Object = MibTableColumn
tmnxL2tpLnsSeMRtPrefixLen = _TmnxL2tpLnsSeMRtPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 4, 1, 3),
    _TmnxL2tpLnsSeMRtPrefixLen_Type()
)
tmnxL2tpLnsSeMRtPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeMRtPrefixLen.setStatus("obsolete")
_TmnxL2tpLnsSeMRtStatus_Type = TmnxManagedRouteStatus
_TmnxL2tpLnsSeMRtStatus_Object = MibTableColumn
tmnxL2tpLnsSeMRtStatus = _TmnxL2tpLnsSeMRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 4, 1, 4),
    _TmnxL2tpLnsSeMRtStatus_Type()
)
tmnxL2tpLnsSeMRtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeMRtStatus.setStatus("obsolete")
_TmnxL2tpLnsSeOvrTable_Object = MibTable
tmnxL2tpLnsSeOvrTable = _TmnxL2tpLnsSeOvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrTable.setStatus("obsolete")
_TmnxL2tpLnsSeOvrEntry_Object = MibTableRow
tmnxL2tpLnsSeOvrEntry = _TmnxL2tpLnsSeOvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1)
)
tmnxL2tpLnsSeOvrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusId"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrDirection"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrType"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrTypeId"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrTypeName"),
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrEntry.setStatus("obsolete")


class _TmnxL2tpLnsSeOvrDirection_Type(TDirection):
    """Custom type tmnxL2tpLnsSeOvrDirection based on TDirection"""
    subtypeSpec = TDirection.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_TmnxL2tpLnsSeOvrDirection_Type.__name__ = "TDirection"
_TmnxL2tpLnsSeOvrDirection_Object = MibTableColumn
tmnxL2tpLnsSeOvrDirection = _TmnxL2tpLnsSeOvrDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1, 1),
    _TmnxL2tpLnsSeOvrDirection_Type()
)
tmnxL2tpLnsSeOvrDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrDirection.setStatus("obsolete")
_TmnxL2tpLnsSeOvrType_Type = TQosOverrideType
_TmnxL2tpLnsSeOvrType_Object = MibTableColumn
tmnxL2tpLnsSeOvrType = _TmnxL2tpLnsSeOvrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1, 2),
    _TmnxL2tpLnsSeOvrType_Type()
)
tmnxL2tpLnsSeOvrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrType.setStatus("obsolete")
_TmnxL2tpLnsSeOvrTypeId_Type = Integer32
_TmnxL2tpLnsSeOvrTypeId_Object = MibTableColumn
tmnxL2tpLnsSeOvrTypeId = _TmnxL2tpLnsSeOvrTypeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1, 3),
    _TmnxL2tpLnsSeOvrTypeId_Type()
)
tmnxL2tpLnsSeOvrTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrTypeId.setStatus("obsolete")
_TmnxL2tpLnsSeOvrTypeName_Type = TNamedItemOrEmpty
_TmnxL2tpLnsSeOvrTypeName_Object = MibTableColumn
tmnxL2tpLnsSeOvrTypeName = _TmnxL2tpLnsSeOvrTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1, 4),
    _TmnxL2tpLnsSeOvrTypeName_Type()
)
tmnxL2tpLnsSeOvrTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrTypeName.setStatus("obsolete")
_TmnxL2tpLnsSeOvrPIR_Type = TPIRRateOverride
_TmnxL2tpLnsSeOvrPIR_Object = MibTableColumn
tmnxL2tpLnsSeOvrPIR = _TmnxL2tpLnsSeOvrPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1, 5),
    _TmnxL2tpLnsSeOvrPIR_Type()
)
tmnxL2tpLnsSeOvrPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrPIR.setStatus("obsolete")
_TmnxL2tpLnsSeOvrCIR_Type = TCIRRateOverride
_TmnxL2tpLnsSeOvrCIR_Object = MibTableColumn
tmnxL2tpLnsSeOvrCIR = _TmnxL2tpLnsSeOvrCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1, 6),
    _TmnxL2tpLnsSeOvrCIR_Type()
)
tmnxL2tpLnsSeOvrCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrCIR.setStatus("obsolete")
_TmnxL2tpLnsSeOvrCBS_Type = TBurstSizeBytesOverride
_TmnxL2tpLnsSeOvrCBS_Object = MibTableColumn
tmnxL2tpLnsSeOvrCBS = _TmnxL2tpLnsSeOvrCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1, 7),
    _TmnxL2tpLnsSeOvrCBS_Type()
)
tmnxL2tpLnsSeOvrCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrCBS.setStatus("obsolete")
_TmnxL2tpLnsSeOvrMBS_Type = TBurstSizeBytesOverride
_TmnxL2tpLnsSeOvrMBS_Object = MibTableColumn
tmnxL2tpLnsSeOvrMBS = _TmnxL2tpLnsSeOvrMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 6, 1, 8),
    _TmnxL2tpLnsSeOvrMBS_Type()
)
tmnxL2tpLnsSeOvrMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeOvrMBS.setStatus("obsolete")
_TmnxL2tpLnsSeAleTable_Object = MibTable
tmnxL2tpLnsSeAleTable = _TmnxL2tpLnsSeAleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeAleTable.setStatus("obsolete")
_TmnxL2tpLnsSeAleEntry_Object = MibTableRow
tmnxL2tpLnsSeAleEntry = _TmnxL2tpLnsSeAleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 7, 1)
)
tmnxL2tpLnsSeAleEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeAleEntry.setStatus("obsolete")
_TmnxL2tpLnsSeAleDatalink_Type = TmnxAccessLoopEncapDataLink
_TmnxL2tpLnsSeAleDatalink_Object = MibTableColumn
tmnxL2tpLnsSeAleDatalink = _TmnxL2tpLnsSeAleDatalink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 7, 1, 1),
    _TmnxL2tpLnsSeAleDatalink_Type()
)
tmnxL2tpLnsSeAleDatalink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeAleDatalink.setStatus("obsolete")
_TmnxL2tpLnsSeAleEncaps1_Type = TmnxAccessLoopEncaps1
_TmnxL2tpLnsSeAleEncaps1_Object = MibTableColumn
tmnxL2tpLnsSeAleEncaps1 = _TmnxL2tpLnsSeAleEncaps1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 7, 1, 2),
    _TmnxL2tpLnsSeAleEncaps1_Type()
)
tmnxL2tpLnsSeAleEncaps1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeAleEncaps1.setStatus("obsolete")
_TmnxL2tpLnsSeAleEncaps2_Type = TmnxAccessLoopEncaps2
_TmnxL2tpLnsSeAleEncaps2_Object = MibTableColumn
tmnxL2tpLnsSeAleEncaps2 = _TmnxL2tpLnsSeAleEncaps2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 1, 7, 1, 3),
    _TmnxL2tpLnsSeAleEncaps2_Type()
)
tmnxL2tpLnsSeAleEncaps2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeAleEncaps2.setStatus("obsolete")
_TmnxL2tpSeOpObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpSeOpObjs = _TmnxL2tpSeOpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 2)
)
_TmnxL2tpSeStopTable_Object = MibTable
tmnxL2tpSeStopTable = _TmnxL2tpSeStopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpSeStopTable.setStatus("current")
_TmnxL2tpSeStopEntry_Object = MibTableRow
tmnxL2tpSeStopEntry = _TmnxL2tpSeStopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpSeStopEntry.setStatus("current")


class _TmnxL2tpSeStop_Type(TmnxActionType):
    """Custom type tmnxL2tpSeStop based on TmnxActionType"""
    defaultValue = 2


_TmnxL2tpSeStop_Type.__name__ = "TmnxActionType"
_TmnxL2tpSeStop_Object = MibTableColumn
tmnxL2tpSeStop = _TmnxL2tpSeStop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 5, 2, 1, 1, 1),
    _TmnxL2tpSeStop_Type()
)
tmnxL2tpSeStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxL2tpSeStop.setStatus("current")
_TmnxL2tpLnsIsaObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpLnsIsaObjs = _TmnxL2tpLnsIsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6)
)
_TmnxL2tpLnsIsaGrpObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpLnsIsaGrpObjs = _TmnxL2tpLnsIsaGrpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1)
)
_TmnxL2tpIsaGrpTable_Object = MibTable
tmnxL2tpIsaGrpTable = _TmnxL2tpIsaGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpTable.setStatus("current")
_TmnxL2tpIsaGrpEntry_Object = MibTableRow
tmnxL2tpIsaGrpEntry = _TmnxL2tpIsaGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1, 1)
)
tmnxL2tpIsaGrpEntry.setIndexNames(
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpEntry.setStatus("current")
_TmnxL2tpIsaGrpId_Type = TmnxL2tpIsaGrpId
_TmnxL2tpIsaGrpId_Object = MibTableColumn
tmnxL2tpIsaGrpId = _TmnxL2tpIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1, 1, 1),
    _TmnxL2tpIsaGrpId_Type()
)
tmnxL2tpIsaGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpId.setStatus("current")
_TmnxL2tpIsaGrpRowStatus_Type = RowStatus
_TmnxL2tpIsaGrpRowStatus_Object = MibTableColumn
tmnxL2tpIsaGrpRowStatus = _TmnxL2tpIsaGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1, 1, 2),
    _TmnxL2tpIsaGrpRowStatus_Type()
)
tmnxL2tpIsaGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpRowStatus.setStatus("current")
_TmnxL2tpIsaGrpLastMgmtChange_Type = TimeStamp
_TmnxL2tpIsaGrpLastMgmtChange_Object = MibTableColumn
tmnxL2tpIsaGrpLastMgmtChange = _TmnxL2tpIsaGrpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1, 1, 3),
    _TmnxL2tpIsaGrpLastMgmtChange_Type()
)
tmnxL2tpIsaGrpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpLastMgmtChange.setStatus("current")


class _TmnxL2tpIsaGrpDescription_Type(TItemDescription):
    """Custom type tmnxL2tpIsaGrpDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxL2tpIsaGrpDescription_Type.__name__ = "TItemDescription"
_TmnxL2tpIsaGrpDescription_Object = MibTableColumn
tmnxL2tpIsaGrpDescription = _TmnxL2tpIsaGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1, 1, 4),
    _TmnxL2tpIsaGrpDescription_Type()
)
tmnxL2tpIsaGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpDescription.setStatus("current")


class _TmnxL2tpIsaGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxL2tpIsaGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxL2tpIsaGrpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxL2tpIsaGrpAdminState_Object = MibTableColumn
tmnxL2tpIsaGrpAdminState = _TmnxL2tpIsaGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1, 1, 5),
    _TmnxL2tpIsaGrpAdminState_Type()
)
tmnxL2tpIsaGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpAdminState.setStatus("current")
_TmnxL2tpIsaGrpOperState_Type = TmnxOperState
_TmnxL2tpIsaGrpOperState_Object = MibTableColumn
tmnxL2tpIsaGrpOperState = _TmnxL2tpIsaGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1, 1, 6),
    _TmnxL2tpIsaGrpOperState_Type()
)
tmnxL2tpIsaGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpOperState.setStatus("current")


class _TmnxL2tpIsaGrpPortPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpIsaGrpPortPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpIsaGrpPortPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpIsaGrpPortPlcy_Object = MibTableColumn
tmnxL2tpIsaGrpPortPlcy = _TmnxL2tpIsaGrpPortPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 1, 1, 1, 8),
    _TmnxL2tpIsaGrpPortPlcy_Type()
)
tmnxL2tpIsaGrpPortPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpPortPlcy.setStatus("current")
_TmnxL2tpLnsIsaMdaObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpLnsIsaMdaObjs = _TmnxL2tpLnsIsaMdaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 2)
)
_TmnxL2tpIsaMdaTable_Object = MibTable
tmnxL2tpIsaMdaTable = _TmnxL2tpIsaMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaTable.setStatus("current")
_TmnxL2tpIsaMdaEntry_Object = MibTableRow
tmnxL2tpIsaMdaEntry = _TmnxL2tpIsaMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 2, 1, 1)
)
tmnxL2tpIsaMdaEntry.setIndexNames(
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaEntry.setStatus("current")
_TmnxL2tpIsaMdaRowStatus_Type = RowStatus
_TmnxL2tpIsaMdaRowStatus_Object = MibTableColumn
tmnxL2tpIsaMdaRowStatus = _TmnxL2tpIsaMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 2, 1, 1, 1),
    _TmnxL2tpIsaMdaRowStatus_Type()
)
tmnxL2tpIsaMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaRowStatus.setStatus("current")
_TmnxL2tpIsaMdaLastMgmtChange_Type = TimeStamp
_TmnxL2tpIsaMdaLastMgmtChange_Object = MibTableColumn
tmnxL2tpIsaMdaLastMgmtChange = _TmnxL2tpIsaMdaLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 2, 1, 1, 2),
    _TmnxL2tpIsaMdaLastMgmtChange_Type()
)
tmnxL2tpIsaMdaLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaLastMgmtChange.setStatus("current")
_TmnxL2tpIsaMdaDrain_Type = TruthValue
_TmnxL2tpIsaMdaDrain_Object = MibTableColumn
tmnxL2tpIsaMdaDrain = _TmnxL2tpIsaMdaDrain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 2, 1, 1, 3),
    _TmnxL2tpIsaMdaDrain_Type()
)
tmnxL2tpIsaMdaDrain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaDrain.setStatus("current")
_TmnxL2tpIsaMdaStop_Type = TmnxActionType
_TmnxL2tpIsaMdaStop_Object = MibTableColumn
tmnxL2tpIsaMdaStop = _TmnxL2tpIsaMdaStop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 2, 1, 1, 4),
    _TmnxL2tpIsaMdaStop_Type()
)
tmnxL2tpIsaMdaStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStop.setStatus("current")
_TmnxL2tpLnsIsaMdaStatObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpLnsIsaMdaStatObjs = _TmnxL2tpLnsIsaMdaStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 3)
)
_TmnxL2tpIsaMdaStatTable_Object = MibTable
tmnxL2tpIsaMdaStatTable = _TmnxL2tpIsaMdaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatTable.setStatus("current")
_TmnxL2tpIsaMdaStatEntry_Object = MibTableRow
tmnxL2tpIsaMdaStatEntry = _TmnxL2tpIsaMdaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatEntry.setStatus("current")
_TmnxL2tpIsaMdaStatOperState_Type = TmnxL2tpIsaMdaOperState
_TmnxL2tpIsaMdaStatOperState_Object = MibTableColumn
tmnxL2tpIsaMdaStatOperState = _TmnxL2tpIsaMdaStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 3, 1, 1, 1),
    _TmnxL2tpIsaMdaStatOperState_Type()
)
tmnxL2tpIsaMdaStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatOperState.setStatus("current")
_TmnxL2tpIsaMdaStatSessions_Type = Gauge32
_TmnxL2tpIsaMdaStatSessions_Object = MibTableColumn
tmnxL2tpIsaMdaStatSessions = _TmnxL2tpIsaMdaStatSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 3, 1, 1, 2),
    _TmnxL2tpIsaMdaStatSessions_Type()
)
tmnxL2tpIsaMdaStatSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatSessions.setStatus("current")
_TmnxL2tpIsaMdaVRtrTable_Object = MibTable
tmnxL2tpIsaMdaVRtrTable = _TmnxL2tpIsaMdaVRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaVRtrTable.setStatus("current")
_TmnxL2tpIsaMdaVRtrEntry_Object = MibTableRow
tmnxL2tpIsaMdaVRtrEntry = _TmnxL2tpIsaMdaVRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 3, 2, 1)
)
tmnxL2tpIsaMdaVRtrEntry.setIndexNames(
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaVRtrEntry.setStatus("current")
_TmnxL2tpIsaMdaVRtrOperState_Type = TmnxOperState
_TmnxL2tpIsaMdaVRtrOperState_Object = MibTableColumn
tmnxL2tpIsaMdaVRtrOperState = _TmnxL2tpIsaMdaVRtrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 3, 2, 1, 1),
    _TmnxL2tpIsaMdaVRtrOperState_Type()
)
tmnxL2tpIsaMdaVRtrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaVRtrOperState.setStatus("current")
_TmnxL2tpLnsIsaMdaStatisticsObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpLnsIsaMdaStatisticsObjs = _TmnxL2tpLnsIsaMdaStatisticsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 4)
)
_TmnxL2tpIsaMdaStatisticsTable_Object = MibTable
tmnxL2tpIsaMdaStatisticsTable = _TmnxL2tpIsaMdaStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatisticsTable.setStatus("current")
_TmnxL2tpIsaMdaStatisticsEntry_Object = MibTableRow
tmnxL2tpIsaMdaStatisticsEntry = _TmnxL2tpIsaMdaStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 4, 1, 1)
)
tmnxL2tpIsaMdaStatisticsEntry.setIndexNames(
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatsInstance"),
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatisticsEntry.setStatus("current")


class _TmnxL2tpIsaMdaStatsInstance_Type(Unsigned32):
    """Custom type tmnxL2tpIsaMdaStatsInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )


_TmnxL2tpIsaMdaStatsInstance_Type.__name__ = "Unsigned32"
_TmnxL2tpIsaMdaStatsInstance_Object = MibTableColumn
tmnxL2tpIsaMdaStatsInstance = _TmnxL2tpIsaMdaStatsInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 4, 1, 1, 1),
    _TmnxL2tpIsaMdaStatsInstance_Type()
)
tmnxL2tpIsaMdaStatsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatsInstance.setStatus("current")


class _TmnxL2tpIsaMdaStatsName_Type(DisplayString):
    """Custom type tmnxL2tpIsaMdaStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxL2tpIsaMdaStatsName_Type.__name__ = "DisplayString"
_TmnxL2tpIsaMdaStatsName_Object = MibTableColumn
tmnxL2tpIsaMdaStatsName = _TmnxL2tpIsaMdaStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 4, 1, 1, 2),
    _TmnxL2tpIsaMdaStatsName_Type()
)
tmnxL2tpIsaMdaStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatsName.setStatus("current")
_TmnxL2tpIsaMdaStatsVal_Type = Counter32
_TmnxL2tpIsaMdaStatsVal_Object = MibTableColumn
tmnxL2tpIsaMdaStatsVal = _TmnxL2tpIsaMdaStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 4, 1, 1, 3),
    _TmnxL2tpIsaMdaStatsVal_Type()
)
tmnxL2tpIsaMdaStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatsVal.setStatus("current")
_TmnxL2tpIsaMdaStatsValHw_Type = Counter32
_TmnxL2tpIsaMdaStatsValHw_Object = MibTableColumn
tmnxL2tpIsaMdaStatsValHw = _TmnxL2tpIsaMdaStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 4, 1, 1, 4),
    _TmnxL2tpIsaMdaStatsValHw_Type()
)
tmnxL2tpIsaMdaStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatsValHw.setStatus("current")
_TmnxL2tpIsaMdaStatsValue_Type = Counter64
_TmnxL2tpIsaMdaStatsValue_Object = MibTableColumn
tmnxL2tpIsaMdaStatsValue = _TmnxL2tpIsaMdaStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 6, 4, 1, 1, 5),
    _TmnxL2tpIsaMdaStatsValue_Type()
)
tmnxL2tpIsaMdaStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatsValue.setStatus("current")
_TmnxL2tpLnsSvcObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpLnsSvcObjs = _TmnxL2tpLnsSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7)
)
_TmnxL2tpLnsIfObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpLnsIfObjs = _TmnxL2tpLnsIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1)
)
_TmnxL2tpLnsIfTable_Object = MibTable
tmnxL2tpLnsIfTable = _TmnxL2tpLnsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfTable.setStatus("current")
_TmnxL2tpLnsIfEntry_Object = MibTableRow
tmnxL2tpLnsIfEntry = _TmnxL2tpLnsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1)
)
tmnxL2tpLnsIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfEntry.setStatus("current")
_TmnxL2tpLnsIfLastMgmtChange_Type = TimeStamp
_TmnxL2tpLnsIfLastMgmtChange_Object = MibTableColumn
tmnxL2tpLnsIfLastMgmtChange = _TmnxL2tpLnsIfLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 1),
    _TmnxL2tpLnsIfLastMgmtChange_Type()
)
tmnxL2tpLnsIfLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfLastMgmtChange.setStatus("current")


class _TmnxL2tpLnsIfDescription_Type(TItemDescription):
    """Custom type tmnxL2tpLnsIfDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxL2tpLnsIfDescription_Type.__name__ = "TItemDescription"
_TmnxL2tpLnsIfDescription_Object = MibTableColumn
tmnxL2tpLnsIfDescription = _TmnxL2tpLnsIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 2),
    _TmnxL2tpLnsIfDescription_Type()
)
tmnxL2tpLnsIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfDescription.setStatus("current")


class _TmnxL2tpLnsIfDefSubProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsIfDefSubProfile based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpLnsIfDefSubProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsIfDefSubProfile_Object = MibTableColumn
tmnxL2tpLnsIfDefSubProfile = _TmnxL2tpLnsIfDefSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 3),
    _TmnxL2tpLnsIfDefSubProfile_Type()
)
tmnxL2tpLnsIfDefSubProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfDefSubProfile.setStatus("current")


class _TmnxL2tpLnsIfDefSlaProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsIfDefSlaProfile based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpLnsIfDefSlaProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsIfDefSlaProfile_Object = MibTableColumn
tmnxL2tpLnsIfDefSlaProfile = _TmnxL2tpLnsIfDefSlaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 4),
    _TmnxL2tpLnsIfDefSlaProfile_Type()
)
tmnxL2tpLnsIfDefSlaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfDefSlaProfile.setStatus("current")


class _TmnxL2tpLnsIfDefAppProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsIfDefAppProfile based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpLnsIfDefAppProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsIfDefAppProfile_Object = MibTableColumn
tmnxL2tpLnsIfDefAppProfile = _TmnxL2tpLnsIfDefAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 5),
    _TmnxL2tpLnsIfDefAppProfile_Type()
)
tmnxL2tpLnsIfDefAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfDefAppProfile.setStatus("current")


class _TmnxL2tpLnsIfSubIdentPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsIfSubIdentPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpLnsIfSubIdentPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsIfSubIdentPolicy_Object = MibTableColumn
tmnxL2tpLnsIfSubIdentPolicy = _TmnxL2tpLnsIfSubIdentPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 6),
    _TmnxL2tpLnsIfSubIdentPolicy_Type()
)
tmnxL2tpLnsIfSubIdentPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfSubIdentPolicy.setStatus("current")


class _TmnxL2tpLnsIfDefSubIdent_Type(TmnxDefSubIdSource):
    """Custom type tmnxL2tpLnsIfDefSubIdent based on TmnxDefSubIdSource"""
    defaultValue = 2


_TmnxL2tpLnsIfDefSubIdent_Type.__name__ = "TmnxDefSubIdSource"
_TmnxL2tpLnsIfDefSubIdent_Object = MibTableColumn
tmnxL2tpLnsIfDefSubIdent = _TmnxL2tpLnsIfDefSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 7),
    _TmnxL2tpLnsIfDefSubIdent_Type()
)
tmnxL2tpLnsIfDefSubIdent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfDefSubIdent.setStatus("current")


class _TmnxL2tpLnsIfDefSubIdentString_Type(DisplayString):
    """Custom type tmnxL2tpLnsIfDefSubIdentString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxL2tpLnsIfDefSubIdentString_Type.__name__ = "DisplayString"
_TmnxL2tpLnsIfDefSubIdentString_Object = MibTableColumn
tmnxL2tpLnsIfDefSubIdentString = _TmnxL2tpLnsIfDefSubIdentString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 8),
    _TmnxL2tpLnsIfDefSubIdentString_Type()
)
tmnxL2tpLnsIfDefSubIdentString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfDefSubIdentString.setStatus("current")


class _TmnxL2tpLnsIfDefFilterProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpLnsIfDefFilterProfile based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpLnsIfDefFilterProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpLnsIfDefFilterProfile_Object = MibTableColumn
tmnxL2tpLnsIfDefFilterProfile = _TmnxL2tpLnsIfDefFilterProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 7, 1, 1, 1, 9),
    _TmnxL2tpLnsIfDefFilterProfile_Type()
)
tmnxL2tpLnsIfDefFilterProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfDefFilterProfile.setStatus("current")
_TmnxL2tpMlpppObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpMlpppObjs = _TmnxL2tpMlpppObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8)
)
_TmnxL2tpLacMlpppBundleTable_Object = MibTable
tmnxL2tpLacMlpppBundleTable = _TmnxL2tpLacMlpppBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleTable.setStatus("current")
_TmnxL2tpLacMlpppBundleEntry_Object = MibTableRow
tmnxL2tpLacMlpppBundleEntry = _TmnxL2tpLacMlpppBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1)
)
tmnxL2tpLacMlpppBundleEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleIndex"),
)
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleEntry.setStatus("current")
_TmnxL2tpLacMlpppBundleIndex_Type = Unsigned32
_TmnxL2tpLacMlpppBundleIndex_Object = MibTableColumn
tmnxL2tpLacMlpppBundleIndex = _TmnxL2tpLacMlpppBundleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1, 1),
    _TmnxL2tpLacMlpppBundleIndex_Type()
)
tmnxL2tpLacMlpppBundleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleIndex.setStatus("current")
_TmnxL2tpLacMlpppBundleSvcId_Type = TmnxServId
_TmnxL2tpLacMlpppBundleSvcId_Object = MibTableColumn
tmnxL2tpLacMlpppBundleSvcId = _TmnxL2tpLacMlpppBundleSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1, 2),
    _TmnxL2tpLacMlpppBundleSvcId_Type()
)
tmnxL2tpLacMlpppBundleSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleSvcId.setStatus("current")
_TmnxL2tpLacMlpppBundleFwdTuId_Type = TmnxL2tpTunnelId
_TmnxL2tpLacMlpppBundleFwdTuId_Object = MibTableColumn
tmnxL2tpLacMlpppBundleFwdTuId = _TmnxL2tpLacMlpppBundleFwdTuId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1, 3),
    _TmnxL2tpLacMlpppBundleFwdTuId_Type()
)
tmnxL2tpLacMlpppBundleFwdTuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleFwdTuId.setStatus("current")
_TmnxL2tpLacMlpppBundleUserName_Type = TmnxPppoeUserNameOrEmpty
_TmnxL2tpLacMlpppBundleUserName_Object = MibTableColumn
tmnxL2tpLacMlpppBundleUserName = _TmnxL2tpLacMlpppBundleUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1, 4),
    _TmnxL2tpLacMlpppBundleUserName_Type()
)
tmnxL2tpLacMlpppBundleUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleUserName.setStatus("current")
_TmnxL2tpLacMlpppBundleLocEpClass_Type = TmnxMlpppEpClass
_TmnxL2tpLacMlpppBundleLocEpClass_Object = MibTableColumn
tmnxL2tpLacMlpppBundleLocEpClass = _TmnxL2tpLacMlpppBundleLocEpClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1, 5),
    _TmnxL2tpLacMlpppBundleLocEpClass_Type()
)
tmnxL2tpLacMlpppBundleLocEpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleLocEpClass.setStatus("current")


class _TmnxL2tpLacMlpppBundleLocEpAddr_Type(OctetString):
    """Custom type tmnxL2tpLacMlpppBundleLocEpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxL2tpLacMlpppBundleLocEpAddr_Type.__name__ = "OctetString"
_TmnxL2tpLacMlpppBundleLocEpAddr_Object = MibTableColumn
tmnxL2tpLacMlpppBundleLocEpAddr = _TmnxL2tpLacMlpppBundleLocEpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1, 6),
    _TmnxL2tpLacMlpppBundleLocEpAddr_Type()
)
tmnxL2tpLacMlpppBundleLocEpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleLocEpAddr.setStatus("current")
_TmnxL2tpLacMlpppBundleRemEpClass_Type = TmnxMlpppEpClass
_TmnxL2tpLacMlpppBundleRemEpClass_Object = MibTableColumn
tmnxL2tpLacMlpppBundleRemEpClass = _TmnxL2tpLacMlpppBundleRemEpClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1, 7),
    _TmnxL2tpLacMlpppBundleRemEpClass_Type()
)
tmnxL2tpLacMlpppBundleRemEpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleRemEpClass.setStatus("current")


class _TmnxL2tpLacMlpppBundleRemEpAddr_Type(OctetString):
    """Custom type tmnxL2tpLacMlpppBundleRemEpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxL2tpLacMlpppBundleRemEpAddr_Type.__name__ = "OctetString"
_TmnxL2tpLacMlpppBundleRemEpAddr_Object = MibTableColumn
tmnxL2tpLacMlpppBundleRemEpAddr = _TmnxL2tpLacMlpppBundleRemEpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 1, 1, 8),
    _TmnxL2tpLacMlpppBundleRemEpAddr_Type()
)
tmnxL2tpLacMlpppBundleRemEpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppBundleRemEpAddr.setStatus("current")
_TmnxL2tpLacMlpppLinkTable_Object = MibTable
tmnxL2tpLacMlpppLinkTable = _TmnxL2tpLacMlpppLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppLinkTable.setStatus("current")
_TmnxL2tpLacMlpppLinkEntry_Object = MibTableRow
tmnxL2tpLacMlpppLinkEntry = _TmnxL2tpLacMlpppLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 2, 1)
)
tmnxL2tpLacMlpppLinkEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleIndex"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusId"),
)
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppLinkEntry.setStatus("current")
_TmnxL2tpLacMlpppLinkState_Type = TmnxL2tpSeOperState
_TmnxL2tpLacMlpppLinkState_Object = MibTableColumn
tmnxL2tpLacMlpppLinkState = _TmnxL2tpLacMlpppLinkState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 8, 2, 1, 1),
    _TmnxL2tpLacMlpppLinkState_Type()
)
tmnxL2tpLacMlpppLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLacMlpppLinkState.setStatus("current")
_TmnxL2tpTableLastCh_Type = TimeStamp
_TmnxL2tpTableLastCh_Object = MibScalar
tmnxL2tpTableLastCh = _TmnxL2tpTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 10),
    _TmnxL2tpTableLastCh_Type()
)
tmnxL2tpTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTableLastCh.setStatus("current")
_TmnxL2tpTgCfgTableLastCh_Type = TimeStamp
_TmnxL2tpTgCfgTableLastCh_Object = MibScalar
tmnxL2tpTgCfgTableLastCh = _TmnxL2tpTgCfgTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 11),
    _TmnxL2tpTgCfgTableLastCh_Type()
)
tmnxL2tpTgCfgTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgTableLastCh.setStatus("current")
_TmnxL2tpTuCfgTableLastCh_Type = TimeStamp
_TmnxL2tpTuCfgTableLastCh_Object = MibScalar
tmnxL2tpTuCfgTableLastCh = _TmnxL2tpTuCfgTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 12),
    _TmnxL2tpTuCfgTableLastCh_Type()
)
tmnxL2tpTuCfgTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgTableLastCh.setStatus("current")
_TmnxL2tpTuStatusTableLastCh_Type = TimeStamp
_TmnxL2tpTuStatusTableLastCh_Object = MibScalar
tmnxL2tpTuStatusTableLastCh = _TmnxL2tpTuStatusTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 13),
    _TmnxL2tpTuStatusTableLastCh_Type()
)
tmnxL2tpTuStatusTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuStatusTableLastCh.setStatus("current")
_TmnxL2tpSeStatusTableLastCh_Type = TimeStamp
_TmnxL2tpSeStatusTableLastCh_Object = MibScalar
tmnxL2tpSeStatusTableLastCh = _TmnxL2tpSeStatusTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 14),
    _TmnxL2tpSeStatusTableLastCh_Type()
)
tmnxL2tpSeStatusTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpSeStatusTableLastCh.setStatus("current")
_TmnxL2tpIsaGrpTableLastCh_Type = TimeStamp
_TmnxL2tpIsaGrpTableLastCh_Object = MibScalar
tmnxL2tpIsaGrpTableLastCh = _TmnxL2tpIsaGrpTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 15),
    _TmnxL2tpIsaGrpTableLastCh_Type()
)
tmnxL2tpIsaGrpTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaGrpTableLastCh.setStatus("current")
_TmnxL2tpIsaMdaTableLastCh_Type = TimeStamp
_TmnxL2tpIsaMdaTableLastCh_Object = MibScalar
tmnxL2tpIsaMdaTableLastCh = _TmnxL2tpIsaMdaTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 16),
    _TmnxL2tpIsaMdaTableLastCh_Type()
)
tmnxL2tpIsaMdaTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaTableLastCh.setStatus("current")
_TmnxL2tpIsaMdaStatTableLastCh_Type = TimeStamp
_TmnxL2tpIsaMdaStatTableLastCh_Object = MibScalar
tmnxL2tpIsaMdaStatTableLastCh = _TmnxL2tpIsaMdaStatTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 17),
    _TmnxL2tpIsaMdaStatTableLastCh_Type()
)
tmnxL2tpIsaMdaStatTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatTableLastCh.setStatus("current")
_TmnxL2tpLnsTgPppTableLastCh_Type = TimeStamp
_TmnxL2tpLnsTgPppTableLastCh_Object = MibScalar
tmnxL2tpLnsTgPppTableLastCh = _TmnxL2tpLnsTgPppTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 18),
    _TmnxL2tpLnsTgPppTableLastCh_Type()
)
tmnxL2tpLnsTgPppTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgPppTableLastCh.setStatus("current")
_TmnxL2tpLnsTuPppTableLastCh_Type = TimeStamp
_TmnxL2tpLnsTuPppTableLastCh_Object = MibScalar
tmnxL2tpLnsTuPppTableLastCh = _TmnxL2tpLnsTuPppTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 19),
    _TmnxL2tpLnsTuPppTableLastCh_Type()
)
tmnxL2tpLnsTuPppTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuPppTableLastCh.setStatus("current")
_TmnxL2tpLnsSePppTableLastCh_Type = TimeStamp
_TmnxL2tpLnsSePppTableLastCh_Object = MibScalar
tmnxL2tpLnsSePppTableLastCh = _TmnxL2tpLnsSePppTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 20),
    _TmnxL2tpLnsSePppTableLastCh_Type()
)
tmnxL2tpLnsSePppTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppTableLastCh.setStatus("current")
_TmnxL2tpLnsSeAleTableLastCh_Type = TimeStamp
_TmnxL2tpLnsSeAleTableLastCh_Object = MibScalar
tmnxL2tpLnsSeAleTableLastCh = _TmnxL2tpLnsSeAleTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 21),
    _TmnxL2tpLnsSeAleTableLastCh_Type()
)
tmnxL2tpLnsSeAleTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeAleTableLastCh.setStatus("obsolete")
_TmnxL2tpXtTableLastCh_Type = TimeStamp
_TmnxL2tpXtTableLastCh_Object = MibScalar
tmnxL2tpXtTableLastCh = _TmnxL2tpXtTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 22),
    _TmnxL2tpXtTableLastCh_Type()
)
tmnxL2tpXtTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpXtTableLastCh.setStatus("current")
_TmnxL2tpIsaMdaStatsTableLastCh_Type = TimeStamp
_TmnxL2tpIsaMdaStatsTableLastCh_Object = MibScalar
tmnxL2tpIsaMdaStatsTableLastCh = _TmnxL2tpIsaMdaStatsTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 23),
    _TmnxL2tpIsaMdaStatsTableLastCh_Type()
)
tmnxL2tpIsaMdaStatsTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaStatsTableLastCh.setStatus("current")
_TmnxL2tpTgXtTableLastCh_Type = TimeStamp
_TmnxL2tpTgXtTableLastCh_Object = MibScalar
tmnxL2tpTgXtTableLastCh = _TmnxL2tpTgXtTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 24),
    _TmnxL2tpTgXtTableLastCh_Type()
)
tmnxL2tpTgXtTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTgXtTableLastCh.setStatus("current")
_TmnxL2tpTuXtTableLastCh_Type = TimeStamp
_TmnxL2tpTuXtTableLastCh_Object = MibScalar
tmnxL2tpTuXtTableLastCh = _TmnxL2tpTuXtTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 25),
    _TmnxL2tpTuXtTableLastCh_Type()
)
tmnxL2tpTuXtTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpTuXtTableLastCh.setStatus("current")
_TmnxL2tpAccountingObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpAccountingObjs = _TmnxL2tpAccountingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100)
)
_TmnxL2tpApTable_Object = MibTable
tmnxL2tpApTable = _TmnxL2tpApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpApTable.setStatus("current")
_TmnxL2tpApEntry_Object = MibTableRow
tmnxL2tpApEntry = _TmnxL2tpApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1)
)
tmnxL2tpApEntry.setIndexNames(
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpApName"),
)
if mibBuilder.loadTexts:
    tmnxL2tpApEntry.setStatus("current")
_TmnxL2tpApName_Type = TNamedItem
_TmnxL2tpApName_Object = MibTableColumn
tmnxL2tpApName = _TmnxL2tpApName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 1),
    _TmnxL2tpApName_Type()
)
tmnxL2tpApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpApName.setStatus("current")
_TmnxL2tpApRowStatus_Type = RowStatus
_TmnxL2tpApRowStatus_Object = MibTableColumn
tmnxL2tpApRowStatus = _TmnxL2tpApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 2),
    _TmnxL2tpApRowStatus_Type()
)
tmnxL2tpApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApRowStatus.setStatus("current")
_TmnxL2tpApLastMgmtChange_Type = TimeStamp
_TmnxL2tpApLastMgmtChange_Object = MibTableColumn
tmnxL2tpApLastMgmtChange = _TmnxL2tpApLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 3),
    _TmnxL2tpApLastMgmtChange_Type()
)
tmnxL2tpApLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApLastMgmtChange.setStatus("current")


class _TmnxL2tpApDescription_Type(TItemDescription):
    """Custom type tmnxL2tpApDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxL2tpApDescription_Type.__name__ = "TItemDescription"
_TmnxL2tpApDescription_Object = MibTableColumn
tmnxL2tpApDescription = _TmnxL2tpApDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 4),
    _TmnxL2tpApDescription_Type()
)
tmnxL2tpApDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApDescription.setStatus("current")


class _TmnxL2tpApType_Type(Bits):
    """Custom type tmnxL2tpApType based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("session", 0),
          ("tunnel", 1))
    )

_TmnxL2tpApType_Type.__name__ = "Bits"
_TmnxL2tpApType_Object = MibTableColumn
tmnxL2tpApType = _TmnxL2tpApType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 5),
    _TmnxL2tpApType_Type()
)
tmnxL2tpApType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApType.setStatus("current")


class _TmnxL2tpApServerVRtrID_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxL2tpApServerVRtrID based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxL2tpApServerVRtrID_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxL2tpApServerVRtrID_Object = MibTableColumn
tmnxL2tpApServerVRtrID = _TmnxL2tpApServerVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 6),
    _TmnxL2tpApServerVRtrID_Type()
)
tmnxL2tpApServerVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServerVRtrID.setStatus("current")


class _TmnxL2tpApServerAlgorithm_Type(TmnxSubRadServAlgorithm):
    """Custom type tmnxL2tpApServerAlgorithm based on TmnxSubRadServAlgorithm"""
    defaultValue = 1

    subtypeSpec = TmnxSubRadServAlgorithm.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("roundRobin", 2))
    )


_TmnxL2tpApServerAlgorithm_Type.__name__ = "TmnxSubRadServAlgorithm"
_TmnxL2tpApServerAlgorithm_Object = MibTableColumn
tmnxL2tpApServerAlgorithm = _TmnxL2tpApServerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 7),
    _TmnxL2tpApServerAlgorithm_Type()
)
tmnxL2tpApServerAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServerAlgorithm.setStatus("current")


class _TmnxL2tpApServerRetry_Type(Unsigned32):
    """Custom type tmnxL2tpApServerRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxL2tpApServerRetry_Type.__name__ = "Unsigned32"
_TmnxL2tpApServerRetry_Object = MibTableColumn
tmnxL2tpApServerRetry = _TmnxL2tpApServerRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 8),
    _TmnxL2tpApServerRetry_Type()
)
tmnxL2tpApServerRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServerRetry.setStatus("current")


class _TmnxL2tpApServerSrcAddrType_Type(InetAddressType):
    """Custom type tmnxL2tpApServerSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxL2tpApServerSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxL2tpApServerSrcAddrType_Object = MibTableColumn
tmnxL2tpApServerSrcAddrType = _TmnxL2tpApServerSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 9),
    _TmnxL2tpApServerSrcAddrType_Type()
)
tmnxL2tpApServerSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServerSrcAddrType.setStatus("current")


class _TmnxL2tpApServerSrcAddr_Type(InetAddress):
    """Custom type tmnxL2tpApServerSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpApServerSrcAddr_Type.__name__ = "InetAddress"
_TmnxL2tpApServerSrcAddr_Object = MibTableColumn
tmnxL2tpApServerSrcAddr = _TmnxL2tpApServerSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 10),
    _TmnxL2tpApServerSrcAddr_Type()
)
tmnxL2tpApServerSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServerSrcAddr.setStatus("current")


class _TmnxL2tpApServerTimeout_Type(Unsigned32):
    """Custom type tmnxL2tpApServerTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxL2tpApServerTimeout_Type.__name__ = "Unsigned32"
_TmnxL2tpApServerTimeout_Object = MibTableColumn
tmnxL2tpApServerTimeout = _TmnxL2tpApServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 11),
    _TmnxL2tpApServerTimeout_Type()
)
tmnxL2tpApServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxL2tpApServerTimeout.setUnits("seconds")


class _TmnxL2tpApIncludeAttributes_Type(Bits):
    """Custom type tmnxL2tpApIncludeAttributes based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("nasIdentifier", 0),
          ("nasPort", 1),
          ("nasPortId", 2),
          ("nasPortType", 3))
    )

_TmnxL2tpApIncludeAttributes_Type.__name__ = "Bits"
_TmnxL2tpApIncludeAttributes_Object = MibTableColumn
tmnxL2tpApIncludeAttributes = _TmnxL2tpApIncludeAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 12),
    _TmnxL2tpApIncludeAttributes_Type()
)
tmnxL2tpApIncludeAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApIncludeAttributes.setStatus("current")


class _TmnxL2tpApRequestScriptPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpApRequestScriptPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpApRequestScriptPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpApRequestScriptPlcy_Object = MibTableColumn
tmnxL2tpApRequestScriptPlcy = _TmnxL2tpApRequestScriptPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 13),
    _TmnxL2tpApRequestScriptPlcy_Type()
)
tmnxL2tpApRequestScriptPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApRequestScriptPlcy.setStatus("current")


class _TmnxL2tpApNasPortIdPfixType_Type(TmnxSubNasPortPrefixType):
    """Custom type tmnxL2tpApNasPortIdPfixType based on TmnxSubNasPortPrefixType"""
    defaultValue = 0


_TmnxL2tpApNasPortIdPfixType_Type.__name__ = "TmnxSubNasPortPrefixType"
_TmnxL2tpApNasPortIdPfixType_Object = MibTableColumn
tmnxL2tpApNasPortIdPfixType = _TmnxL2tpApNasPortIdPfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 14),
    _TmnxL2tpApNasPortIdPfixType_Type()
)
tmnxL2tpApNasPortIdPfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApNasPortIdPfixType.setStatus("current")


class _TmnxL2tpApNasPortIdPfixString_Type(DisplayString):
    """Custom type tmnxL2tpApNasPortIdPfixString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxL2tpApNasPortIdPfixString_Type.__name__ = "DisplayString"
_TmnxL2tpApNasPortIdPfixString_Object = MibTableColumn
tmnxL2tpApNasPortIdPfixString = _TmnxL2tpApNasPortIdPfixString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 15),
    _TmnxL2tpApNasPortIdPfixString_Type()
)
tmnxL2tpApNasPortIdPfixString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApNasPortIdPfixString.setStatus("current")


class _TmnxL2tpApNasPortIdSfixType_Type(TmnxSubNasPortSuffixType):
    """Custom type tmnxL2tpApNasPortIdSfixType based on TmnxSubNasPortSuffixType"""
    defaultValue = 0


_TmnxL2tpApNasPortIdSfixType_Type.__name__ = "TmnxSubNasPortSuffixType"
_TmnxL2tpApNasPortIdSfixType_Object = MibTableColumn
tmnxL2tpApNasPortIdSfixType = _TmnxL2tpApNasPortIdSfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 16),
    _TmnxL2tpApNasPortIdSfixType_Type()
)
tmnxL2tpApNasPortIdSfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApNasPortIdSfixType.setStatus("current")


class _TmnxL2tpApNasPortTypeType_Type(TmnxSubNasPortTypeType):
    """Custom type tmnxL2tpApNasPortTypeType based on TmnxSubNasPortTypeType"""
    defaultValue = 1


_TmnxL2tpApNasPortTypeType_Type.__name__ = "TmnxSubNasPortTypeType"
_TmnxL2tpApNasPortTypeType_Object = MibTableColumn
tmnxL2tpApNasPortTypeType = _TmnxL2tpApNasPortTypeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 17),
    _TmnxL2tpApNasPortTypeType_Type()
)
tmnxL2tpApNasPortTypeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApNasPortTypeType.setStatus("current")


class _TmnxL2tpApNasPortTypeValue_Type(Unsigned32):
    """Custom type tmnxL2tpApNasPortTypeValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxL2tpApNasPortTypeValue_Type.__name__ = "Unsigned32"
_TmnxL2tpApNasPortTypeValue_Object = MibTableColumn
tmnxL2tpApNasPortTypeValue = _TmnxL2tpApNasPortTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 18),
    _TmnxL2tpApNasPortTypeValue_Type()
)
tmnxL2tpApNasPortTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApNasPortTypeValue.setStatus("current")


class _TmnxL2tpApNasPortBitspec_Type(TmnxBinarySpecification):
    """Custom type tmnxL2tpApNasPortBitspec based on TmnxBinarySpecification"""
    defaultValue = OctetString("")


_TmnxL2tpApNasPortBitspec_Type.__name__ = "TmnxBinarySpecification"
_TmnxL2tpApNasPortBitspec_Object = MibTableColumn
tmnxL2tpApNasPortBitspec = _TmnxL2tpApNasPortBitspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 19),
    _TmnxL2tpApNasPortBitspec_Type()
)
tmnxL2tpApNasPortBitspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApNasPortBitspec.setStatus("current")


class _TmnxL2tpApRadServPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxL2tpApRadServPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxL2tpApRadServPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxL2tpApRadServPlcy_Object = MibTableColumn
tmnxL2tpApRadServPlcy = _TmnxL2tpApRadServPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 1, 1, 20),
    _TmnxL2tpApRadServPlcy_Type()
)
tmnxL2tpApRadServPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApRadServPlcy.setStatus("current")
_TmnxL2tpApServTable_Object = MibTable
tmnxL2tpApServTable = _TmnxL2tpApServTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2)
)
if mibBuilder.loadTexts:
    tmnxL2tpApServTable.setStatus("current")
_TmnxL2tpApServEntry_Object = MibTableRow
tmnxL2tpApServEntry = _TmnxL2tpApServEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1)
)
tmnxL2tpApServEntry.setIndexNames(
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpApName"),
    (0, "TIMETRA-L2TP-MIB", "tmnxL2tpApServIndex"),
)
if mibBuilder.loadTexts:
    tmnxL2tpApServEntry.setStatus("current")


class _TmnxL2tpApServIndex_Type(Unsigned32):
    """Custom type tmnxL2tpApServIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxL2tpApServIndex_Type.__name__ = "Unsigned32"
_TmnxL2tpApServIndex_Object = MibTableColumn
tmnxL2tpApServIndex = _TmnxL2tpApServIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1, 1),
    _TmnxL2tpApServIndex_Type()
)
tmnxL2tpApServIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxL2tpApServIndex.setStatus("current")
_TmnxL2tpApServRowStatus_Type = RowStatus
_TmnxL2tpApServRowStatus_Object = MibTableColumn
tmnxL2tpApServRowStatus = _TmnxL2tpApServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1, 2),
    _TmnxL2tpApServRowStatus_Type()
)
tmnxL2tpApServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServRowStatus.setStatus("current")
_TmnxL2tpApServLastMgmtChange_Type = TimeStamp
_TmnxL2tpApServLastMgmtChange_Object = MibTableColumn
tmnxL2tpApServLastMgmtChange = _TmnxL2tpApServLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1, 3),
    _TmnxL2tpApServLastMgmtChange_Type()
)
tmnxL2tpApServLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServLastMgmtChange.setStatus("current")
_TmnxL2tpApServAddrType_Type = InetAddressType
_TmnxL2tpApServAddrType_Object = MibTableColumn
tmnxL2tpApServAddrType = _TmnxL2tpApServAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1, 5),
    _TmnxL2tpApServAddrType_Type()
)
tmnxL2tpApServAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServAddrType.setStatus("current")


class _TmnxL2tpApServAddr_Type(InetAddress):
    """Custom type tmnxL2tpApServAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxL2tpApServAddr_Type.__name__ = "InetAddress"
_TmnxL2tpApServAddr_Object = MibTableColumn
tmnxL2tpApServAddr = _TmnxL2tpApServAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1, 6),
    _TmnxL2tpApServAddr_Type()
)
tmnxL2tpApServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServAddr.setStatus("current")


class _TmnxL2tpApServSecret_Type(DisplayString):
    """Custom type tmnxL2tpApServSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 20),
    )


_TmnxL2tpApServSecret_Type.__name__ = "DisplayString"
_TmnxL2tpApServSecret_Object = MibTableColumn
tmnxL2tpApServSecret = _TmnxL2tpApServSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1, 7),
    _TmnxL2tpApServSecret_Type()
)
tmnxL2tpApServSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServSecret.setStatus("current")


class _TmnxL2tpApServAcctPort_Type(Unsigned32):
    """Custom type tmnxL2tpApServAcctPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxL2tpApServAcctPort_Type.__name__ = "Unsigned32"
_TmnxL2tpApServAcctPort_Object = MibTableColumn
tmnxL2tpApServAcctPort = _TmnxL2tpApServAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1, 8),
    _TmnxL2tpApServAcctPort_Type()
)
tmnxL2tpApServAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxL2tpApServAcctPort.setStatus("current")
_TmnxL2tpApServOperState_Type = TmnxOperState
_TmnxL2tpApServOperState_Object = MibTableColumn
tmnxL2tpApServOperState = _TmnxL2tpApServOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 2, 1, 9),
    _TmnxL2tpApServOperState_Type()
)
tmnxL2tpApServOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServOperState.setStatus("current")
_TmnxL2tpApServStatsTable_Object = MibTable
tmnxL2tpApServStatsTable = _TmnxL2tpApServStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3)
)
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsTable.setStatus("current")
_TmnxL2tpApServStatsEntry_Object = MibTableRow
tmnxL2tpApServStatsEntry = _TmnxL2tpApServStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsEntry.setStatus("current")
_TmnxL2tpApServStatsTxRequests_Type = Counter32
_TmnxL2tpApServStatsTxRequests_Object = MibTableColumn
tmnxL2tpApServStatsTxRequests = _TmnxL2tpApServStatsTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3, 1, 1),
    _TmnxL2tpApServStatsTxRequests_Type()
)
tmnxL2tpApServStatsTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsTxRequests.setStatus("current")
_TmnxL2tpApServStatsRxResponses_Type = Counter32
_TmnxL2tpApServStatsRxResponses_Object = MibTableColumn
tmnxL2tpApServStatsRxResponses = _TmnxL2tpApServStatsRxResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3, 1, 2),
    _TmnxL2tpApServStatsRxResponses_Type()
)
tmnxL2tpApServStatsRxResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsRxResponses.setStatus("current")
_TmnxL2tpApServStatsReqTimeout_Type = Counter32
_TmnxL2tpApServStatsReqTimeout_Object = MibTableColumn
tmnxL2tpApServStatsReqTimeout = _TmnxL2tpApServStatsReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3, 1, 3),
    _TmnxL2tpApServStatsReqTimeout_Type()
)
tmnxL2tpApServStatsReqTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsReqTimeout.setStatus("current")
_TmnxL2tpApServStatsReqSendFail_Type = Counter32
_TmnxL2tpApServStatsReqSendFail_Object = MibTableColumn
tmnxL2tpApServStatsReqSendFail = _TmnxL2tpApServStatsReqSendFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3, 1, 4),
    _TmnxL2tpApServStatsReqSendFail_Type()
)
tmnxL2tpApServStatsReqSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsReqSendFail.setStatus("current")
_TmnxL2tpApServStatsReqPending_Type = Counter32
_TmnxL2tpApServStatsReqPending_Object = MibTableColumn
tmnxL2tpApServStatsReqPending = _TmnxL2tpApServStatsReqPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3, 1, 5),
    _TmnxL2tpApServStatsReqPending_Type()
)
tmnxL2tpApServStatsReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsReqPending.setStatus("current")
_TmnxL2tpApServStatsRespInvAuth_Type = Counter32
_TmnxL2tpApServStatsRespInvAuth_Object = MibTableColumn
tmnxL2tpApServStatsRespInvAuth = _TmnxL2tpApServStatsRespInvAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3, 1, 6),
    _TmnxL2tpApServStatsRespInvAuth_Type()
)
tmnxL2tpApServStatsRespInvAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsRespInvAuth.setStatus("current")
_TmnxL2tpApServStatsSendRetries_Type = Counter32
_TmnxL2tpApServStatsSendRetries_Object = MibTableColumn
tmnxL2tpApServStatsSendRetries = _TmnxL2tpApServStatsSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 3, 1, 7),
    _TmnxL2tpApServStatsSendRetries_Type()
)
tmnxL2tpApServStatsSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServStatsSendRetries.setStatus("current")
_TmnxL2tpApTableLastCh_Type = TimeStamp
_TmnxL2tpApTableLastCh_Object = MibScalar
tmnxL2tpApTableLastCh = _TmnxL2tpApTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 100),
    _TmnxL2tpApTableLastCh_Type()
)
tmnxL2tpApTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApTableLastCh.setStatus("current")
_TmnxL2tpApServTableLastCh_Type = TimeStamp
_TmnxL2tpApServTableLastCh_Object = MibScalar
tmnxL2tpApServTableLastCh = _TmnxL2tpApServTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 1, 100, 101),
    _TmnxL2tpApServTableLastCh_Type()
)
tmnxL2tpApServTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxL2tpApServTableLastCh.setStatus("current")
_TmnxL2tpNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxL2tpNotificationObjs = _TmnxL2tpNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 2)
)
_TmnxL2tpNotifyDescription_Type = DisplayString
_TmnxL2tpNotifyDescription_Object = MibScalar
tmnxL2tpNotifyDescription = _TmnxL2tpNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 2, 1),
    _TmnxL2tpNotifyDescription_Type()
)
tmnxL2tpNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxL2tpNotifyDescription.setStatus("current")
_TmnxL2tpPppNcpFailureProtocol_Type = TmnxPppNcpProtocol
_TmnxL2tpPppNcpFailureProtocol_Object = MibScalar
tmnxL2tpPppNcpFailureProtocol = _TmnxL2tpPppNcpFailureProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 60, 2, 20),
    _TmnxL2tpPppNcpFailureProtocol_Type()
)
tmnxL2tpPppNcpFailureProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxL2tpPppNcpFailureProtocol.setStatus("current")
_TmnxL2tpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxL2tpNotifyPrefix = _TmnxL2tpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60)
)
_TmnxL2tpNotifications_ObjectIdentity = ObjectIdentity
tmnxL2tpNotifications = _TmnxL2tpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60, 0)
)
tmnxL2tpEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpXtEntry")
)
tmnxL2tpXtEntry.setIndexNames(*tmnxL2tpEntry.getIndexNames())
tmnxL2tpTgCfgEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpLnsTgPppEntry")
)
tmnxL2tpLnsTgPppEntry.setIndexNames(*tmnxL2tpTgCfgEntry.getIndexNames())
tmnxL2tpTgCfgEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTgMlpppEntry")
)
tmnxL2tpTgMlpppEntry.setIndexNames(*tmnxL2tpTgCfgEntry.getIndexNames())
tmnxL2tpTgCfgEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTgXtEntry")
)
tmnxL2tpTgXtEntry.setIndexNames(*tmnxL2tpTgCfgEntry.getIndexNames())
tmnxL2tpTgStatEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTgDrainEntry")
)
tmnxL2tpTgDrainEntry.setIndexNames(*tmnxL2tpTgStatEntry.getIndexNames())
tmnxL2tpTuCfgEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpLnsTuPppEntry")
)
tmnxL2tpLnsTuPppEntry.setIndexNames(*tmnxL2tpTuCfgEntry.getIndexNames())
tmnxL2tpTuCfgEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTuMlpppEntry")
)
tmnxL2tpTuMlpppEntry.setIndexNames(*tmnxL2tpTuCfgEntry.getIndexNames())
tmnxL2tpTuCfgEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTuXtEntry")
)
tmnxL2tpTuXtEntry.setIndexNames(*tmnxL2tpTuCfgEntry.getIndexNames())
tmnxL2tpTuStatusEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTuStatsEntry")
)
tmnxL2tpTuStatsEntry.setIndexNames(*tmnxL2tpTuStatusEntry.getIndexNames())
tmnxL2tpTuCfgEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTuStartEntry")
)
tmnxL2tpTuStartEntry.setIndexNames(*tmnxL2tpTuCfgEntry.getIndexNames())
tmnxL2tpTuStatusEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTuStopEntry")
)
tmnxL2tpTuStopEntry.setIndexNames(*tmnxL2tpTuStatusEntry.getIndexNames())
tmnxL2tpTuStatusEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpTuDrainEntry")
)
tmnxL2tpTuDrainEntry.setIndexNames(*tmnxL2tpTuStatusEntry.getIndexNames())
tmnxL2tpSeStatusEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpSeStopEntry")
)
tmnxL2tpSeStopEntry.setIndexNames(*tmnxL2tpSeStatusEntry.getIndexNames())
tmnxL2tpIsaMdaEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpIsaMdaStatEntry")
)
tmnxL2tpIsaMdaStatEntry.setIndexNames(*tmnxL2tpIsaMdaEntry.getIndexNames())
tmnxL2tpApServEntry.registerAugmentions(
    ("TIMETRA-L2TP-MIB",
     "tmnxL2tpApServStatsEntry")
)
tmnxL2tpApServStatsEntry.setIndexNames(*tmnxL2tpApServEntry.getIndexNames())

# Managed Objects groups

tmnxL2tpCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 1)
)
tmnxL2tpCfgGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAdminState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSessionLimit"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpReceiveWindowSize"))
)
if mibBuilder.loadTexts:
    tmnxL2tpCfgGroup.setStatus("obsolete")

tmnxL2tpTgCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 2)
)
tmnxL2tpTgCfgGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgRowStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgDescription"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgAdminState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgSecret"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgHelloInterval"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgIdleTO"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgDestructTO"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgMaxRetxEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgMaxRetxNotEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgSessionLimit"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgAvpHiding"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgSessionAssignMethod"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgLocalName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgDoChallenge"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgReceiveWindowSize"))
)
if mibBuilder.loadTexts:
    tmnxL2tpTgCfgGroup.setStatus("current")

tmnxL2tpTuCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 3)
)
tmnxL2tpTuCfgGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgRowStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgDescription"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgAdminState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgPreference"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgPeerAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgPeerAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgLocalName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgRemoteName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgSecret"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgHelloInterval"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgIdleTO"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgDestructTO"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgMaxRetxEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgMaxRetxNotEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgSessionLimit"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgAvpHiding"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgAutoEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgDoChallenge"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgReceiveWindowSize"))
)
if mibBuilder.loadTexts:
    tmnxL2tpTuCfgGroup.setStatus("current")

tmnxL2tpStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 4)
)
tmnxL2tpStatGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpStatCleared"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatTotalTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedTuAuth"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatActiveTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatTotalSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatActiveSessions"))
)
if mibBuilder.loadTexts:
    tmnxL2tpStatGroup.setStatus("obsolete")

tmnxL2tpTgStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 5)
)
tmnxL2tpTgStatGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatCleared"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatTotalTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatFailedTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatFailedTuAuth"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatActiveTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatTotalSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatFailedSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatActiveSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatControlRxOctets"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatControlRxOctetsLw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatControlRxOctetsHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatControlRxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatControlTxOctets"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatControlTxOctetsLw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatControlTxOctetsHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatControlTxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatErrorTxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatErrorRxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatSessionLimit"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatSeAssignMethod"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgTuId"))
)
if mibBuilder.loadTexts:
    tmnxL2tpTgStatGroup.setStatus("current")

tmnxL2tpPeerStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 7)
)
tmnxL2tpPeerStatGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatRole"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatActiveTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatActiveSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatDraining"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatUnreachable"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatUnreachableTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlRxOct"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlRxOctLw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlRxOctHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlRxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlTxOct"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlTxOctLw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlTxOctHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlTxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatErrorTxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatErrorRxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatMsgAccepted"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatMsgDuplicateRx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatMsgOutOfWndwRx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatLastCleared"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerTuId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsVal"))
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatGroup.setStatus("obsolete")

tmnxL2tpSeStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 8)
)
tmnxL2tpSeStatGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusTunnelId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusTunnelConnId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusSessionId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusRemoteTunnelId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusRemoteSessionId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusRemoteConnId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusStartTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusEstabTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRemoteName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusClosedTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusCdnResult"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusGeneralError"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusErrorMessage"))
)
if mibBuilder.loadTexts:
    tmnxL2tpSeStatGroup.setStatus("current")

tmnxL2tpPeerOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 9)
)
tmnxL2tpPeerOpGroup.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerDrain")
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerOpGroup.setStatus("current")

tmnxL2tpTgOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 10)
)
tmnxL2tpTgOpGroup.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpTgDrain")
)
if mibBuilder.loadTexts:
    tmnxL2tpTgOpGroup.setStatus("current")

tmnxL2tpTuOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 11)
)
tmnxL2tpTuOpGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTuStart"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStop"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuDrain"))
)
if mibBuilder.loadTexts:
    tmnxL2tpTuOpGroup.setStatus("current")

tmnxL2tpLnsIsaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 12)
)
tmnxL2tpLnsIsaGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpRowStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpDescription"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpAdminState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpOperState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaRowStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaDrain"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStop"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsIsaGroup.setStatus("current")

tmnxL2tpLnsIsaStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 13)
)
tmnxL2tpLnsIsaStatGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatOperState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaVRtrOperState"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsIsaStatGroup.setStatus("current")

tmnxL2tpLnsTgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 14)
)
tmnxL2tpLnsTgGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgDoChallenge"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgIsaGrpId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppAuthPlcy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppAuthProtocol"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppUserDb"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppDefaultService"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppDefaultGroupIf"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppProxyLcp"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppProxyAuth"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppMtu"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppLcpKaInterval"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppLcpKaHoldUp"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgGroup.setStatus("current")

tmnxL2tpLnsTuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 15)
)
tmnxL2tpLnsTuGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgIsaGrpId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppAuthPlcy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppAuthProtocol"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppUserDb"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppDefaultService"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppDefaultGroupIf"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppProxyLcp"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppProxyAuth"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppMtu"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppLcpKaInterval"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppLcpKaHoldUp"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuGroup.setStatus("current")

tmnxL2tpLnsSeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 16)
)
tmnxL2tpLnsSeGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppUpTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppLcpState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpcpState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPppMtu"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPppAuthProtocol"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPppUserName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSubIdent"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppOriginSubIdent"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSubProfString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSlaProfString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppAncpString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppInterDestId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppAppProfString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppOriginStrings"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSessionTimeout"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPrimaryDnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPrimaryDns"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSecondaryDnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSecondaryDns"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPrimaryNbnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPrimaryNbns"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSecondNbnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSecondNbns"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppOriginIpcpInfo"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppCircuitId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppRemoteId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppAddressPool"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSvcId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppGrpIf"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppL2tpVrtrId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppL2tpConnectionId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppCategoryMapName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppRadiusClassAttr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppRadiusUserName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6cpState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppInterfaceId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppOriginIpv6cpInfo"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6DnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6Dns1"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6Dns2"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6DelPfxType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6DelPfxLen"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6DelPfx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6PrefixType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6PrefixLen"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6Prefix"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxUnkwnProto"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpConfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpConfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpConfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpConfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpTermRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpTermAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpCodeRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpEchoRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpEchoRep"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpProtRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpDiscRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpConfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpConfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpConfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpConfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpTermRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpTermAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpCodeRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpEchoRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpEchoRep"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpProtRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpDiscRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxPapAuthRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxPapAuthAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxPapAuthNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxChapResp"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxChapChall"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxChapSucc"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxChapFail"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpConfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpConfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpConfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpConfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpTermRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpTermAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpCodeRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpConfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpConfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpConfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpConfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpTermRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpTermAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpCodeRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeMRtStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrPIR"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrCIR"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrCBS"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrMBS"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeAleTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeAleDatalink"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeAleEncaps1"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeAleEncaps2"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpTmRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpTmAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCdRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpTmRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpTmAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCdRj"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeGroup.setStatus("obsolete")

tmnxL2tpCfgV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 17)
)
tmnxL2tpCfgV8v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAdminState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSessionLimit"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpReceiveWindowSize"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpRowStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerAddrChangePlcy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAvpExclude"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAvpCallingNumberSpec"))
)
if mibBuilder.loadTexts:
    tmnxL2tpCfgV8v0Group.setStatus("current")

tmnxL2tpTuStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 18)
)
tmnxL2tpTuStatGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTunnelId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPreference"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPeerAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusPeerAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusLocalName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRemoteName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusAssignmentId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusHelloInterval"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusIdleTO"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusDestructTO"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusMaxRetxEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusMaxRetxNotEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusSessionLimit"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusAvpHiding"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusGroupName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRemoteTunnelId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRemoteConnId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTransportType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusUdpPort"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRemoteUdpPort"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusStartTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusEstabTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusIdleTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusClosedTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusStopCcnResult"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusGeneralError"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusErrorMessage"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusDoChallenge"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRws"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTxDestAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTxDestAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRxSrcAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRxSrcAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsLastCleared"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsTotalSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsFailedSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsActiveSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsControlRxOctets"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsControlRxOctetsLw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsControlRxOctetsHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsControlRxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsControlTxOctets"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsControlTxOctetsLw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsControlTxOctetsHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsControlTxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsErrorTxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsErrorRxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsFsmMsgAccepted"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsFsmMsgDuplicateRx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsFsmMsgOutOfWndwRx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsQLengthUnsentMax"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsQLengthUnsentCur"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsQLengthAckMax"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsQLengthAckCur"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatsWindowSizeCur"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuProtStatsName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuProtStatsVal"))
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStatGroup.setStatus("current")

tmnxL2tpPeerStatV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 19)
)
tmnxL2tpPeerStatV8v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatActiveTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatActiveSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatDraining"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatUnreachable"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatUnreachableTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlRxOct"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlRxOctLw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlRxOctHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlRxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlTxOct"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlTxOctLw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlTxOctHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatControlTxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatErrorTxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatErrorRxPkts"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatMsgAccepted"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatMsgDuplicateRx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatMsgOutOfWndwRx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatRolesCapability"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatRoles"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatLastCleared"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerTuId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerProtStatsVal"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatUnreachTimeRem"))
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerStatV8v0Group.setStatus("current")

tmnxL2tpLnsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 20)
)
tmnxL2tpLnsIfGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDescription"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefSubProfile"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefSlaProfile"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefAppProfile"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfSubIdentPolicy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefSubIdent"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefSubIdentString"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfGroup.setStatus("obsolete")

tmnxL2tpStatV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 21)
)
tmnxL2tpStatV8v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpStatCleared"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatTotalTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedTuAuth"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatActiveTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatTotalSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatActiveSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatCurrentTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatCurrentSessions"))
)
if mibBuilder.loadTexts:
    tmnxL2tpStatV8v0Group.setStatus("obsolete")

tmnxL2tpSeOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 22)
)
tmnxL2tpSeOpGroup.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStop")
)
if mibBuilder.loadTexts:
    tmnxL2tpSeOpGroup.setStatus("current")

tmnxL2tpStatV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 23)
)
tmnxL2tpStatV11v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpStatCleared"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatTotalTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedTuAuth"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatActiveTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatTotalSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatFailedSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatActiveSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatCurrentTunnels"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatCurrentSessions"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatCurrSelBlacklstLen"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpStatUnavailTunnelIds"))
)
if mibBuilder.loadTexts:
    tmnxL2tpStatV11v0Group.setStatus("current")

tmnxL2tpLnsTgV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 30)
)
tmnxL2tpLnsTgV9v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppIpcpSubnetNeg")
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgV9v0Group.setStatus("current")

tmnxL2tpLnsTuV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 31)
)
tmnxL2tpLnsTuV9v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppIpcpSubnetNeg")
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuV9v0Group.setStatus("current")

tmnxL2tpLnsIfV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 32)
)
tmnxL2tpLnsIfV9v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDescription"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefSubProfile"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefSlaProfile"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefAppProfile"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfSubIdentPolicy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefSubIdent"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefSubIdentString"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsIfV9v0Group.setStatus("current")

tmnxL2tpMlpppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 40)
)
tmnxL2tpMlpppGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgLoadBalanceMethod"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgLoadBalanceMethod"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppAdminState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppMaxLinks"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppInterleave"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppMaxFragDelay"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppReassemblyTo"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppShortSeqNumberRx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppEpClass"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppEpIpv4Address"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgMlpppEpMacAddress"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppAdminState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppMaxLinks"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppInterleave"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppMaxFragDelay"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppReassemblyTo"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppShortSeqNumberRx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppEpClass"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppEpIpv4Address"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuMlpppEpMacAddress"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleSvcId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleFwdTuId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleUserName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleLocEpClass"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleLocEpAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleRemEpClass"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppBundleRemEpAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLacMlpppLinkState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatusMlpppBundleIndex"))
)
if mibBuilder.loadTexts:
    tmnxL2tpMlpppGroup.setStatus("current")

tmnxL2tpLnsSeV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 41)
)
tmnxL2tpLnsSeV9v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSubPppIndex"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSeV9v0Group.setStatus("current")

tmnxL2tpFilterProfileV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 42)
)
tmnxL2tpFilterProfileV9v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfDefFilterProfile")
)
if mibBuilder.loadTexts:
    tmnxL2tpFilterProfileV9v0Group.setStatus("current")

tmnxL2tpTgV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 43)
)
tmnxL2tpTgV10v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgLoadBalanceMethod")
)
if mibBuilder.loadTexts:
    tmnxL2tpTgV10v0Group.setStatus("current")

tmnxL2tpTuV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 44)
)
tmnxL2tpTuV10v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgLoadBalanceMethod")
)
if mibBuilder.loadTexts:
    tmnxL2tpTuV10v0Group.setStatus("current")

tmnxL2tpAccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 45)
)
tmnxL2tpAccountingGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpApRowStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApDescription"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServerVRtrID"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServerAlgorithm"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServerRetry"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServerSrcAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServerSrcAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServerTimeout"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServRowStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServSecret"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServAcctPort"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServOperState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServStatsTxRequests"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServStatsRxResponses"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServStatsReqTimeout"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServStatsReqSendFail"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServStatsReqPending"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServStatsRespInvAuth"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServStatsSendRetries"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApServTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAccountingPolicy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgAccountingPolicy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgAccountingPolicy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApIncludeAttributes"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApRequestScriptPlcy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApNasPortIdPfixType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApNasPortIdPfixString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApNasPortIdSfixType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApNasPortTypeType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApNasPortTypeValue"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpApNasPortBitspec"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusAccountingPolicy"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusSelBlacklstState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusSelBlacklstTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatSelBlacklstTimeRem"))
)
if mibBuilder.loadTexts:
    tmnxL2tpAccountingGroup.setStatus("current")

tmnxL2tpLnsIsaV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 46)
)
tmnxL2tpLnsIsaV10v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaGrpPortPlcy")
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsIsaV10v0Group.setStatus("current")

tmnxL2tpV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 47)
)
tmnxL2tpV11v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpHelloInterval"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIdleTO"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpDestructTO"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpMaxRetxEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpMaxRetxNotEstab"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTunnelSessionLimit"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpGroupSessionLimit"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAvpHiding"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpDoChallenge"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSecret"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSessionAssignMethod"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLocalName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtNextAttempt"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtTuSelBlacklistReason"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtTuSelBlacklistMaxTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtTuSelBlacklistLength"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtTuSelBlacklistToAction"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtReplaceResultCodes"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtAvpCiscoNasPortEth"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtAvpCiscoNasPortAtm"))
)
if mibBuilder.loadTexts:
    tmnxL2tpV11v0Group.setStatus("current")

tmnxL2tpLnsTgV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 48)
)
tmnxL2tpLnsTgV11v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppLcpIgnoreMagic"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppMinChapChall"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgPppMaxChapChall"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTgV11v0Group.setStatus("current")

tmnxL2tpLnsTuV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 49)
)
tmnxL2tpLnsTuV11v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppLcpIgnoreMagic"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppMinChapChall"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuPppMaxChapChall"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsTuV11v0Group.setStatus("current")

tmnxL2tpTuStatV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 50)
)
tmnxL2tpTuStatV11v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusTxDestUdpPort"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusRxSrcUdpPort"))
)
if mibBuilder.loadTexts:
    tmnxL2tpTuStatV11v0Group.setStatus("current")

tmnxL2tpAccountingV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 55)
)
tmnxL2tpAccountingV12v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpApRadServPlcy")
)
if mibBuilder.loadTexts:
    tmnxL2tpAccountingV12v0Group.setStatus("current")

tmnxL2tpLnsIsaStatV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 56)
)
tmnxL2tpLnsIsaStatV12v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatsTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatsName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatsVal"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatsValHw"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaStatsValue"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsIsaStatV12v0Group.setStatus("current")

tmnxL2tpDontFragmentBitLacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 57)
)
tmnxL2tpDontFragmentBitLacGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpXtDfBitLac"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgXtTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgXtLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgXtDfBitLac"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuXtTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuXtLastMgmtChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuXtDfBitLac"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusDfBitLac"))
)
if mibBuilder.loadTexts:
    tmnxL2tpDontFragmentBitLacGroup.setStatus("current")

tmnxL2tpObsoletedObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 97)
)
tmnxL2tpObsoletedObjsV9v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppUpTime"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppLcpState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpcpState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPppMtu"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPppAuthProtocol"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPppUserName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSubIdent"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppOriginSubIdent"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSubProfString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSlaProfString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppAncpString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppInterDestId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppAppProfString"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppOriginStrings"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSessionTimeout"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpAddrType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpAddr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPrimaryDnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPrimaryDns"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSecondaryDnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSecondaryDns"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPrimaryNbnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPrimaryNbns"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSecondNbnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSecondNbns"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppOriginIpcpInfo"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppCircuitId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppRemoteId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppAddressPool"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSvcId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppGrpIf"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppL2tpVrtrId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppL2tpConnectionId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppCategoryMapName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppRadiusClassAttr"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppRadiusUserName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6cpState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppInterfaceId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppOriginIpv6cpInfo"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6DnsType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6Dns1"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6Dns2"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6DelPfxType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6DelPfxLen"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6DelPfx"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6PrefixType"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6PrefixLen"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppIpv6Prefix"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxUnkwnProto"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpConfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpConfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpConfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpConfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpTermRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpTermAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpCodeRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpEchoRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpEchoRep"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpProtRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxLcpDiscRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpConfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpConfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpConfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpConfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpTermRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpTermAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpCodeRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpEchoRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpEchoRep"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpProtRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxLcpDiscRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxPapAuthRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxPapAuthAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxPapAuthNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxChapResp"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxChapChall"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxChapSucc"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxChapFail"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpConfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpConfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpConfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpConfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpTermRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpTermAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpcpCodeRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpConfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpConfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpConfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpConfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpTermRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpTermAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpcpCodeRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCdRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpCfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpTmAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatRxIpv6cpTmRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCdRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCfAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCfNk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCfRj"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpCfRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpTmAk"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppStatTxIpv6cpTmRq"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeMRtStatus"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrPIR"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrCIR"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrCBS"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeOvrMBS"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeAleTableLastCh"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeAleDatalink"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeAleEncaps1"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeAleEncaps2"))
)
if mibBuilder.loadTexts:
    tmnxL2tpObsoletedObjsV9v0Group.setStatus("current")

tmnxL2tpObsoletedObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 98)
)
tmnxL2tpObsoletedObjsV8v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatRole")
)
if mibBuilder.loadTexts:
    tmnxL2tpObsoletedObjsV8v0Group.setStatus("current")

tmnxL2tpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 99)
)
tmnxL2tpNotifyObjsGroup.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyObjsGroup.setStatus("current")

tmnxL2tpNotifyObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 102)
)
tmnxL2tpNotifyObjsV9v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpPppNcpFailureProtocol")
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyObjsV9v0Group.setStatus("current")


# Notification objects

tmnxL2tpPeerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60, 0, 1)
)
tmnxL2tpPeerUnreachable.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatUnreachable"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxL2tpPeerUnreachable.setStatus(
        "current"
    )

tmnxL2tpIsaMdaVRtrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60, 0, 2)
)
tmnxL2tpIsaMdaVRtrStateChange.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaVRtrOperState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxL2tpIsaMdaVRtrStateChange.setStatus(
        "current"
    )

tmnxL2tpLnsSePppSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60, 0, 3)
)
tmnxL2tpLnsSePppSessionFailure.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPppUserName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSvcId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppGrpIf"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsSePppSessionFailure.setStatus(
        "current"
    )

tmnxL2tpLnsPppNcpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60, 0, 10)
)
tmnxL2tpLnsPppNcpFailure.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppPppUserName"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSvcId"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppGrpIf"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPppNcpFailureProtocol"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsPppNcpFailure.setStatus(
        "current"
    )

tmnxL2tpApFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60, 0, 11)
)
tmnxL2tpApFailure.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpApDescription"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxL2tpApFailure.setStatus(
        "current"
    )

tmnxL2tpTunnelBlacklisted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60, 0, 12)
)
tmnxL2tpTunnelBlacklisted.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatusSelBlacklstState"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxL2tpTunnelBlacklisted.setStatus(
        "current"
    )

tmnxL2tpTunnelSelBlacklistFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 60, 0, 13)
)
tmnxL2tpTunnelSelBlacklistFull.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpStatCurrSelBlacklstLen"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpXtTuSelBlacklistLength"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxL2tpTunnelSelBlacklistFull.setStatus(
        "current"
    )


# Notifications groups

tmnxL2tpNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 100)
)
tmnxL2tpNotifyGroup.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpPeerUnreachable"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpIsaMdaVRtrStateChange"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSePppSessionFailure"))
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyGroup.setStatus(
        "current"
    )

tmnxL2tpNotifyV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 101)
)
tmnxL2tpNotifyV9v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsPppNcpFailure")
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyV9v0Group.setStatus(
        "current"
    )

tmnxL2tpNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 103)
)
tmnxL2tpNotifyV10v0Group.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpApFailure")
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyV10v0Group.setStatus(
        "current"
    )

tmnxL2tpNotifyV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 2, 104)
)
tmnxL2tpNotifyV11v0Group.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTunnelBlacklisted"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTunnelSelBlacklistFull"))
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyV11v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxL2tpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 1)
)
tmnxL2tpCompliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpCompliance.setStatus(
        "obsolete"
    )

tmnxL2tpStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 2)
)
tmnxL2tpStatCompliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpStatCompliance.setStatus(
        "obsolete"
    )

tmnxL2tpOpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 3)
)
tmnxL2tpOpCompliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpTgOpGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuOpGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerOpGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeOpGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpOpCompliance.setStatus(
        "current"
    )

tmnxL2tpLnsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 4)
)
tmnxL2tpLnsCompliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsCompliance.setStatus(
        "obsolete"
    )

tmnxL2tpNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 5)
)
tmnxL2tpNotifyCompliance.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyCompliance.setStatus(
        "obsolete"
    )

tmnxL2tpV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 6)
)
tmnxL2tpV8v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpCfgV8v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpV8v0Compliance.setStatus(
        "current"
    )

tmnxL2tpStatV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 7)
)
tmnxL2tpStatV8v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpStatV8v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatV8v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpStatV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpLnsV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 10)
)
tmnxL2tpLnsV9v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpFilterProfileV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpNotifyV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 11)
)
tmnxL2tpNotifyV9v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpMlpppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 12)
)
tmnxL2tpMlpppCompliance.setObjects(
    ("TIMETRA-L2TP-MIB", "tmnxL2tpMlpppGroup")
)
if mibBuilder.loadTexts:
    tmnxL2tpMlpppCompliance.setStatus(
        "current"
    )

tmnxL2tpV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 13)
)
tmnxL2tpV10v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpCfgV8v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAccountingGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpNotifyV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 14)
)
tmnxL2tpNotifyV10v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpLnsV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 15)
)
tmnxL2tpLnsV10v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpFilterProfileV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 16)
)
tmnxL2tpV11v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpCfgV8v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAccountingGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpLnsV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 17)
)
tmnxL2tpLnsV11v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpFilterProfileV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpStatV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 18)
)
tmnxL2tpStatV11v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpStatV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatV8v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpStatV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpNotifyV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 19)
)
tmnxL2tpNotifyV11v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxL2tpV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 20)
)
tmnxL2tpV12v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpCfgV8v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuCfgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAccountingGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpAccountingV12v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpDontFragmentBitLacGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpV12v0Compliance.setStatus(
        "current"
    )

tmnxL2tpLnsV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 21)
)
tmnxL2tpLnsV12v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIsaStatV12v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTgV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsTuV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsSeV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpLnsIfV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpFilterProfileV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpLnsV12v0Compliance.setStatus(
        "current"
    )

tmnxL2tpStatV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 22)
)
tmnxL2tpStatV12v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpStatV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTgStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpTuStatV11v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpPeerStatV8v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpSeStatGroup"))
)
if mibBuilder.loadTexts:
    tmnxL2tpStatV12v0Compliance.setStatus(
        "current"
    )

tmnxL2tpNotifyV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 60, 1, 23)
)
tmnxL2tpNotifyV12v0Compliance.setObjects(
      *(("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyGroup"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV9v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV10v0Group"),
        ("TIMETRA-L2TP-MIB", "tmnxL2tpNotifyV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxL2tpNotifyV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-L2TP-MIB",
    **{"TmnxAlwaysNeverOrDefault": TmnxAlwaysNeverOrDefault,
       "TmnxAlwaysOrNever": TmnxAlwaysOrNever,
       "TmnxL2tpActionTypeDrain": TmnxL2tpActionTypeDrain,
       "TmnxL2tpAuthSecret": TmnxL2tpAuthSecret,
       "TmnxL2tpAvpHidingMode": TmnxL2tpAvpHidingMode,
       "TmnxL2tpCdnResult": TmnxL2tpCdnResult,
       "TmnxL2tpConnectionId": TmnxL2tpConnectionId,
       "TmnxL2tpDoChallenge": TmnxL2tpDoChallenge,
       "TmnxL2tpErrorMessage": TmnxL2tpErrorMessage,
       "TmnxL2tpGeneralError": TmnxL2tpGeneralError,
       "TmnxL2tpHostNameOrEmpty": TmnxL2tpHostNameOrEmpty,
       "TmnxL2tpIsaGrpId": TmnxL2tpIsaGrpId,
       "TmnxL2tpIsaGrpIdOrZero": TmnxL2tpIsaGrpIdOrZero,
       "TmnxL2tpIsaMdaLoadBalanceMethod": TmnxL2tpIsaMdaLoadBalanceMethod,
       "TmnxL2tpIsaMdaOperState": TmnxL2tpIsaMdaOperState,
       "TmnxL2tpLcpKaHoldUpMplier": TmnxL2tpLcpKaHoldUpMplier,
       "TmnxL2tpLcpKaInterval": TmnxL2tpLcpKaInterval,
       "TmnxL2tpMlpppEndpointClass": TmnxL2tpMlpppEndpointClass,
       "TmnxL2tpMlpppMaxFragDelay": TmnxL2tpMlpppMaxFragDelay,
       "TmnxL2tpMlpppReassemblyTimeout": TmnxL2tpMlpppReassemblyTimeout,
       "TmnxL2tpPeerAddrChangePolicy": TmnxL2tpPeerAddrChangePolicy,
       "TmnxL2tpPppAuthentication": TmnxL2tpPppAuthentication,
       "TmnxL2tpPppMtu": TmnxL2tpPppMtu,
       "TmnxL2tpReceiveWindowSize": TmnxL2tpReceiveWindowSize,
       "TmnxL2tpRoles": TmnxL2tpRoles,
       "TmnxL2tpSeOperState": TmnxL2tpSeOperState,
       "TmnxL2tpSessionAssignMethod": TmnxL2tpSessionAssignMethod,
       "TmnxL2tpSessionId": TmnxL2tpSessionId,
       "TmnxL2tpStopCcnResult": TmnxL2tpStopCcnResult,
       "TmnxL2tpTgOperState": TmnxL2tpTgOperState,
       "TmnxL2tpTransportType": TmnxL2tpTransportType,
       "TmnxL2tpTunnelDestructTO": TmnxL2tpTunnelDestructTO,
       "TmnxL2tpTunnelGroupName": TmnxL2tpTunnelGroupName,
       "TmnxL2tpTunnelGroupNameOrEmpty": TmnxL2tpTunnelGroupNameOrEmpty,
       "TmnxL2tpTunnelHelloInterval": TmnxL2tpTunnelHelloInterval,
       "TmnxL2tpTunnelId": TmnxL2tpTunnelId,
       "TmnxL2tpTunnelIdleTO": TmnxL2tpTunnelIdleTO,
       "TmnxL2tpTunnelMaxRetx": TmnxL2tpTunnelMaxRetx,
       "TmnxL2tpTunnelName": TmnxL2tpTunnelName,
       "TmnxL2tpTunnelNameOrEmpty": TmnxL2tpTunnelNameOrEmpty,
       "TmnxL2tpTunnelPreference": TmnxL2tpTunnelPreference,
       "TmnxL2tpTunnelSessionLimit": TmnxL2tpTunnelSessionLimit,
       "TmnxL2tpTuOperState": TmnxL2tpTuOperState,
       "TmnxL2tpTuProtStatsType": TmnxL2tpTuProtStatsType,
       "timetraL2tpMIBModule": timetraL2tpMIBModule,
       "tmnxL2tpConformance": tmnxL2tpConformance,
       "tmnxL2tpCompliances": tmnxL2tpCompliances,
       "tmnxL2tpCompliance": tmnxL2tpCompliance,
       "tmnxL2tpStatCompliance": tmnxL2tpStatCompliance,
       "tmnxL2tpOpCompliance": tmnxL2tpOpCompliance,
       "tmnxL2tpLnsCompliance": tmnxL2tpLnsCompliance,
       "tmnxL2tpNotifyCompliance": tmnxL2tpNotifyCompliance,
       "tmnxL2tpV8v0Compliance": tmnxL2tpV8v0Compliance,
       "tmnxL2tpStatV8v0Compliance": tmnxL2tpStatV8v0Compliance,
       "tmnxL2tpLnsV9v0Compliance": tmnxL2tpLnsV9v0Compliance,
       "tmnxL2tpNotifyV9v0Compliance": tmnxL2tpNotifyV9v0Compliance,
       "tmnxL2tpMlpppCompliance": tmnxL2tpMlpppCompliance,
       "tmnxL2tpV10v0Compliance": tmnxL2tpV10v0Compliance,
       "tmnxL2tpNotifyV10v0Compliance": tmnxL2tpNotifyV10v0Compliance,
       "tmnxL2tpLnsV10v0Compliance": tmnxL2tpLnsV10v0Compliance,
       "tmnxL2tpV11v0Compliance": tmnxL2tpV11v0Compliance,
       "tmnxL2tpLnsV11v0Compliance": tmnxL2tpLnsV11v0Compliance,
       "tmnxL2tpStatV11v0Compliance": tmnxL2tpStatV11v0Compliance,
       "tmnxL2tpNotifyV11v0Compliance": tmnxL2tpNotifyV11v0Compliance,
       "tmnxL2tpV12v0Compliance": tmnxL2tpV12v0Compliance,
       "tmnxL2tpLnsV12v0Compliance": tmnxL2tpLnsV12v0Compliance,
       "tmnxL2tpStatV12v0Compliance": tmnxL2tpStatV12v0Compliance,
       "tmnxL2tpNotifyV12v0Compliance": tmnxL2tpNotifyV12v0Compliance,
       "tmnxL2tpGroups": tmnxL2tpGroups,
       "tmnxL2tpCfgGroup": tmnxL2tpCfgGroup,
       "tmnxL2tpTgCfgGroup": tmnxL2tpTgCfgGroup,
       "tmnxL2tpTuCfgGroup": tmnxL2tpTuCfgGroup,
       "tmnxL2tpStatGroup": tmnxL2tpStatGroup,
       "tmnxL2tpTgStatGroup": tmnxL2tpTgStatGroup,
       "tmnxL2tpPeerStatGroup": tmnxL2tpPeerStatGroup,
       "tmnxL2tpSeStatGroup": tmnxL2tpSeStatGroup,
       "tmnxL2tpPeerOpGroup": tmnxL2tpPeerOpGroup,
       "tmnxL2tpTgOpGroup": tmnxL2tpTgOpGroup,
       "tmnxL2tpTuOpGroup": tmnxL2tpTuOpGroup,
       "tmnxL2tpLnsIsaGroup": tmnxL2tpLnsIsaGroup,
       "tmnxL2tpLnsIsaStatGroup": tmnxL2tpLnsIsaStatGroup,
       "tmnxL2tpLnsTgGroup": tmnxL2tpLnsTgGroup,
       "tmnxL2tpLnsTuGroup": tmnxL2tpLnsTuGroup,
       "tmnxL2tpLnsSeGroup": tmnxL2tpLnsSeGroup,
       "tmnxL2tpCfgV8v0Group": tmnxL2tpCfgV8v0Group,
       "tmnxL2tpTuStatGroup": tmnxL2tpTuStatGroup,
       "tmnxL2tpPeerStatV8v0Group": tmnxL2tpPeerStatV8v0Group,
       "tmnxL2tpLnsIfGroup": tmnxL2tpLnsIfGroup,
       "tmnxL2tpStatV8v0Group": tmnxL2tpStatV8v0Group,
       "tmnxL2tpSeOpGroup": tmnxL2tpSeOpGroup,
       "tmnxL2tpStatV11v0Group": tmnxL2tpStatV11v0Group,
       "tmnxL2tpLnsTgV9v0Group": tmnxL2tpLnsTgV9v0Group,
       "tmnxL2tpLnsTuV9v0Group": tmnxL2tpLnsTuV9v0Group,
       "tmnxL2tpLnsIfV9v0Group": tmnxL2tpLnsIfV9v0Group,
       "tmnxL2tpMlpppGroup": tmnxL2tpMlpppGroup,
       "tmnxL2tpLnsSeV9v0Group": tmnxL2tpLnsSeV9v0Group,
       "tmnxL2tpFilterProfileV9v0Group": tmnxL2tpFilterProfileV9v0Group,
       "tmnxL2tpTgV10v0Group": tmnxL2tpTgV10v0Group,
       "tmnxL2tpTuV10v0Group": tmnxL2tpTuV10v0Group,
       "tmnxL2tpAccountingGroup": tmnxL2tpAccountingGroup,
       "tmnxL2tpLnsIsaV10v0Group": tmnxL2tpLnsIsaV10v0Group,
       "tmnxL2tpV11v0Group": tmnxL2tpV11v0Group,
       "tmnxL2tpLnsTgV11v0Group": tmnxL2tpLnsTgV11v0Group,
       "tmnxL2tpLnsTuV11v0Group": tmnxL2tpLnsTuV11v0Group,
       "tmnxL2tpTuStatV11v0Group": tmnxL2tpTuStatV11v0Group,
       "tmnxL2tpAccountingV12v0Group": tmnxL2tpAccountingV12v0Group,
       "tmnxL2tpLnsIsaStatV12v0Group": tmnxL2tpLnsIsaStatV12v0Group,
       "tmnxL2tpDontFragmentBitLacGroup": tmnxL2tpDontFragmentBitLacGroup,
       "tmnxL2tpObsoletedObjsV9v0Group": tmnxL2tpObsoletedObjsV9v0Group,
       "tmnxL2tpObsoletedObjsV8v0Group": tmnxL2tpObsoletedObjsV8v0Group,
       "tmnxL2tpNotifyObjsGroup": tmnxL2tpNotifyObjsGroup,
       "tmnxL2tpNotifyGroup": tmnxL2tpNotifyGroup,
       "tmnxL2tpNotifyV9v0Group": tmnxL2tpNotifyV9v0Group,
       "tmnxL2tpNotifyObjsV9v0Group": tmnxL2tpNotifyObjsV9v0Group,
       "tmnxL2tpNotifyV10v0Group": tmnxL2tpNotifyV10v0Group,
       "tmnxL2tpNotifyV11v0Group": tmnxL2tpNotifyV11v0Group,
       "tmnxL2tp": tmnxL2tp,
       "tmnxL2tpObjs": tmnxL2tpObjs,
       "tmnxL2tpVrtrObjs": tmnxL2tpVrtrObjs,
       "tmnxL2tpVrtrCfgObjs": tmnxL2tpVrtrCfgObjs,
       "tmnxL2tpTable": tmnxL2tpTable,
       "tmnxL2tpEntry": tmnxL2tpEntry,
       "tmnxL2tpLastMgmtChange": tmnxL2tpLastMgmtChange,
       "tmnxL2tpAdminState": tmnxL2tpAdminState,
       "tmnxL2tpSessionLimit": tmnxL2tpSessionLimit,
       "tmnxL2tpReceiveWindowSize": tmnxL2tpReceiveWindowSize,
       "tmnxL2tpRowStatus": tmnxL2tpRowStatus,
       "tmnxL2tpPeerAddrChangePlcy": tmnxL2tpPeerAddrChangePlcy,
       "tmnxL2tpAvpExclude": tmnxL2tpAvpExclude,
       "tmnxL2tpAvpCallingNumberSpec": tmnxL2tpAvpCallingNumberSpec,
       "tmnxL2tpAccountingPolicy": tmnxL2tpAccountingPolicy,
       "tmnxL2tpHelloInterval": tmnxL2tpHelloInterval,
       "tmnxL2tpIdleTO": tmnxL2tpIdleTO,
       "tmnxL2tpDestructTO": tmnxL2tpDestructTO,
       "tmnxL2tpMaxRetxEstab": tmnxL2tpMaxRetxEstab,
       "tmnxL2tpMaxRetxNotEstab": tmnxL2tpMaxRetxNotEstab,
       "tmnxL2tpTunnelSessionLimit": tmnxL2tpTunnelSessionLimit,
       "tmnxL2tpGroupSessionLimit": tmnxL2tpGroupSessionLimit,
       "tmnxL2tpAvpHiding": tmnxL2tpAvpHiding,
       "tmnxL2tpDoChallenge": tmnxL2tpDoChallenge,
       "tmnxL2tpSecret": tmnxL2tpSecret,
       "tmnxL2tpSessionAssignMethod": tmnxL2tpSessionAssignMethod,
       "tmnxL2tpLocalName": tmnxL2tpLocalName,
       "tmnxL2tpAddrType": tmnxL2tpAddrType,
       "tmnxL2tpAddr": tmnxL2tpAddr,
       "tmnxL2tpXtTable": tmnxL2tpXtTable,
       "tmnxL2tpXtEntry": tmnxL2tpXtEntry,
       "tmnxL2tpXtNextAttempt": tmnxL2tpXtNextAttempt,
       "tmnxL2tpXtLastMgmtChange": tmnxL2tpXtLastMgmtChange,
       "tmnxL2tpXtTuSelBlacklistReason": tmnxL2tpXtTuSelBlacklistReason,
       "tmnxL2tpXtTuSelBlacklistMaxTime": tmnxL2tpXtTuSelBlacklistMaxTime,
       "tmnxL2tpXtTuSelBlacklistLength": tmnxL2tpXtTuSelBlacklistLength,
       "tmnxL2tpXtTuSelBlacklistToAction": tmnxL2tpXtTuSelBlacklistToAction,
       "tmnxL2tpXtReplaceResultCodes": tmnxL2tpXtReplaceResultCodes,
       "tmnxL2tpXtAvpCiscoNasPortEth": tmnxL2tpXtAvpCiscoNasPortEth,
       "tmnxL2tpXtAvpCiscoNasPortAtm": tmnxL2tpXtAvpCiscoNasPortAtm,
       "tmnxL2tpXtDfBitLac": tmnxL2tpXtDfBitLac,
       "tmnxL2tpVrtrStatObjs": tmnxL2tpVrtrStatObjs,
       "tmnxL2tpStatTable": tmnxL2tpStatTable,
       "tmnxL2tpStatEntry": tmnxL2tpStatEntry,
       "tmnxL2tpStatCleared": tmnxL2tpStatCleared,
       "tmnxL2tpStatTotalTunnels": tmnxL2tpStatTotalTunnels,
       "tmnxL2tpStatFailedTunnels": tmnxL2tpStatFailedTunnels,
       "tmnxL2tpStatFailedTuAuth": tmnxL2tpStatFailedTuAuth,
       "tmnxL2tpStatActiveTunnels": tmnxL2tpStatActiveTunnels,
       "tmnxL2tpStatTotalSessions": tmnxL2tpStatTotalSessions,
       "tmnxL2tpStatFailedSessions": tmnxL2tpStatFailedSessions,
       "tmnxL2tpStatActiveSessions": tmnxL2tpStatActiveSessions,
       "tmnxL2tpStatCurrentTunnels": tmnxL2tpStatCurrentTunnels,
       "tmnxL2tpStatCurrentSessions": tmnxL2tpStatCurrentSessions,
       "tmnxL2tpStatCurrSelBlacklstLen": tmnxL2tpStatCurrSelBlacklstLen,
       "tmnxL2tpStatUnavailTunnelIds": tmnxL2tpStatUnavailTunnelIds,
       "tmnxL2tpTgObjs": tmnxL2tpTgObjs,
       "tmnxL2tpTgCfgObjs": tmnxL2tpTgCfgObjs,
       "tmnxL2tpTgCfgTable": tmnxL2tpTgCfgTable,
       "tmnxL2tpTgCfgEntry": tmnxL2tpTgCfgEntry,
       "tmnxL2tpTgCfgName": tmnxL2tpTgCfgName,
       "tmnxL2tpTgCfgRowStatus": tmnxL2tpTgCfgRowStatus,
       "tmnxL2tpTgCfgLastMgmtChange": tmnxL2tpTgCfgLastMgmtChange,
       "tmnxL2tpTgCfgDescription": tmnxL2tpTgCfgDescription,
       "tmnxL2tpTgCfgAdminState": tmnxL2tpTgCfgAdminState,
       "tmnxL2tpTgCfgSecret": tmnxL2tpTgCfgSecret,
       "tmnxL2tpTgCfgHelloInterval": tmnxL2tpTgCfgHelloInterval,
       "tmnxL2tpTgCfgIdleTO": tmnxL2tpTgCfgIdleTO,
       "tmnxL2tpTgCfgDestructTO": tmnxL2tpTgCfgDestructTO,
       "tmnxL2tpTgCfgMaxRetxEstab": tmnxL2tpTgCfgMaxRetxEstab,
       "tmnxL2tpTgCfgMaxRetxNotEstab": tmnxL2tpTgCfgMaxRetxNotEstab,
       "tmnxL2tpTgCfgSessionLimit": tmnxL2tpTgCfgSessionLimit,
       "tmnxL2tpTgCfgAvpHiding": tmnxL2tpTgCfgAvpHiding,
       "tmnxL2tpTgCfgSessionAssignMethod": tmnxL2tpTgCfgSessionAssignMethod,
       "tmnxL2tpTgCfgLocalName": tmnxL2tpTgCfgLocalName,
       "tmnxL2tpTgCfgDoChallenge": tmnxL2tpTgCfgDoChallenge,
       "tmnxL2tpTgCfgReceiveWindowSize": tmnxL2tpTgCfgReceiveWindowSize,
       "tmnxL2tpTgCfgIsaGrpId": tmnxL2tpTgCfgIsaGrpId,
       "tmnxL2tpTgCfgAddrType": tmnxL2tpTgCfgAddrType,
       "tmnxL2tpTgCfgAddr": tmnxL2tpTgCfgAddr,
       "tmnxL2tpTgCfgLoadBalanceMethod": tmnxL2tpTgCfgLoadBalanceMethod,
       "tmnxL2tpTgCfgAccountingPolicy": tmnxL2tpTgCfgAccountingPolicy,
       "tmnxL2tpLnsTgPppTable": tmnxL2tpLnsTgPppTable,
       "tmnxL2tpLnsTgPppEntry": tmnxL2tpLnsTgPppEntry,
       "tmnxL2tpLnsTgPppLastMgmtChange": tmnxL2tpLnsTgPppLastMgmtChange,
       "tmnxL2tpLnsTgPppAuthPlcy": tmnxL2tpLnsTgPppAuthPlcy,
       "tmnxL2tpLnsTgPppAuthProtocol": tmnxL2tpLnsTgPppAuthProtocol,
       "tmnxL2tpLnsTgPppUserDb": tmnxL2tpLnsTgPppUserDb,
       "tmnxL2tpLnsTgPppDefaultService": tmnxL2tpLnsTgPppDefaultService,
       "tmnxL2tpLnsTgPppDefaultGroupIf": tmnxL2tpLnsTgPppDefaultGroupIf,
       "tmnxL2tpLnsTgPppProxyLcp": tmnxL2tpLnsTgPppProxyLcp,
       "tmnxL2tpLnsTgPppProxyAuth": tmnxL2tpLnsTgPppProxyAuth,
       "tmnxL2tpLnsTgPppMtu": tmnxL2tpLnsTgPppMtu,
       "tmnxL2tpLnsTgPppLcpKaInterval": tmnxL2tpLnsTgPppLcpKaInterval,
       "tmnxL2tpLnsTgPppLcpKaHoldUp": tmnxL2tpLnsTgPppLcpKaHoldUp,
       "tmnxL2tpLnsTgPppIpcpSubnetNeg": tmnxL2tpLnsTgPppIpcpSubnetNeg,
       "tmnxL2tpLnsTgPppLcpIgnoreMagic": tmnxL2tpLnsTgPppLcpIgnoreMagic,
       "tmnxL2tpLnsTgPppMinChapChall": tmnxL2tpLnsTgPppMinChapChall,
       "tmnxL2tpLnsTgPppMaxChapChall": tmnxL2tpLnsTgPppMaxChapChall,
       "tmnxL2tpTgMlpppTable": tmnxL2tpTgMlpppTable,
       "tmnxL2tpTgMlpppEntry": tmnxL2tpTgMlpppEntry,
       "tmnxL2tpTgMlpppLastMgmtChange": tmnxL2tpTgMlpppLastMgmtChange,
       "tmnxL2tpTgMlpppAdminState": tmnxL2tpTgMlpppAdminState,
       "tmnxL2tpTgMlpppMaxLinks": tmnxL2tpTgMlpppMaxLinks,
       "tmnxL2tpTgMlpppInterleave": tmnxL2tpTgMlpppInterleave,
       "tmnxL2tpTgMlpppMaxFragDelay": tmnxL2tpTgMlpppMaxFragDelay,
       "tmnxL2tpTgMlpppReassemblyTo": tmnxL2tpTgMlpppReassemblyTo,
       "tmnxL2tpTgMlpppShortSeqNumberRx": tmnxL2tpTgMlpppShortSeqNumberRx,
       "tmnxL2tpTgMlpppEpClass": tmnxL2tpTgMlpppEpClass,
       "tmnxL2tpTgMlpppEpIpv4Address": tmnxL2tpTgMlpppEpIpv4Address,
       "tmnxL2tpTgMlpppEpMacAddress": tmnxL2tpTgMlpppEpMacAddress,
       "tmnxL2tpTgXtTable": tmnxL2tpTgXtTable,
       "tmnxL2tpTgXtEntry": tmnxL2tpTgXtEntry,
       "tmnxL2tpTgXtLastMgmtChange": tmnxL2tpTgXtLastMgmtChange,
       "tmnxL2tpTgXtDfBitLac": tmnxL2tpTgXtDfBitLac,
       "tmnxL2tpTgStatObjs": tmnxL2tpTgStatObjs,
       "tmnxL2tpTgStatTable": tmnxL2tpTgStatTable,
       "tmnxL2tpTgStatEntry": tmnxL2tpTgStatEntry,
       "tmnxL2tpTgStatName": tmnxL2tpTgStatName,
       "tmnxL2tpTgStatState": tmnxL2tpTgStatState,
       "tmnxL2tpTgStatCleared": tmnxL2tpTgStatCleared,
       "tmnxL2tpTgStatTotalTunnels": tmnxL2tpTgStatTotalTunnels,
       "tmnxL2tpTgStatFailedTunnels": tmnxL2tpTgStatFailedTunnels,
       "tmnxL2tpTgStatFailedTuAuth": tmnxL2tpTgStatFailedTuAuth,
       "tmnxL2tpTgStatActiveTunnels": tmnxL2tpTgStatActiveTunnels,
       "tmnxL2tpTgStatTunnels": tmnxL2tpTgStatTunnels,
       "tmnxL2tpTgStatTotalSessions": tmnxL2tpTgStatTotalSessions,
       "tmnxL2tpTgStatFailedSessions": tmnxL2tpTgStatFailedSessions,
       "tmnxL2tpTgStatActiveSessions": tmnxL2tpTgStatActiveSessions,
       "tmnxL2tpTgStatSessions": tmnxL2tpTgStatSessions,
       "tmnxL2tpTgStatControlRxOctets": tmnxL2tpTgStatControlRxOctets,
       "tmnxL2tpTgStatControlRxOctetsLw": tmnxL2tpTgStatControlRxOctetsLw,
       "tmnxL2tpTgStatControlRxOctetsHw": tmnxL2tpTgStatControlRxOctetsHw,
       "tmnxL2tpTgStatControlRxPkts": tmnxL2tpTgStatControlRxPkts,
       "tmnxL2tpTgStatControlTxOctets": tmnxL2tpTgStatControlTxOctets,
       "tmnxL2tpTgStatControlTxOctetsLw": tmnxL2tpTgStatControlTxOctetsLw,
       "tmnxL2tpTgStatControlTxOctetsHw": tmnxL2tpTgStatControlTxOctetsHw,
       "tmnxL2tpTgStatControlTxPkts": tmnxL2tpTgStatControlTxPkts,
       "tmnxL2tpTgStatErrorTxPkts": tmnxL2tpTgStatErrorTxPkts,
       "tmnxL2tpTgStatErrorRxPkts": tmnxL2tpTgStatErrorRxPkts,
       "tmnxL2tpTgStatSessionLimit": tmnxL2tpTgStatSessionLimit,
       "tmnxL2tpTgStatSeAssignMethod": tmnxL2tpTgStatSeAssignMethod,
       "tmnxL2tpTgTuTable": tmnxL2tpTgTuTable,
       "tmnxL2tpTgTuEntry": tmnxL2tpTgTuEntry,
       "tmnxL2tpTgTuId": tmnxL2tpTgTuId,
       "tmnxL2tpTgOpObjs": tmnxL2tpTgOpObjs,
       "tmnxL2tpTgDrainTable": tmnxL2tpTgDrainTable,
       "tmnxL2tpTgDrainEntry": tmnxL2tpTgDrainEntry,
       "tmnxL2tpTgDrain": tmnxL2tpTgDrain,
       "tmnxL2tpTunnelObjs": tmnxL2tpTunnelObjs,
       "tmnxL2tpTuCfgObjs": tmnxL2tpTuCfgObjs,
       "tmnxL2tpTuCfgTable": tmnxL2tpTuCfgTable,
       "tmnxL2tpTuCfgEntry": tmnxL2tpTuCfgEntry,
       "tmnxL2tpTuCfgName": tmnxL2tpTuCfgName,
       "tmnxL2tpTuCfgRowStatus": tmnxL2tpTuCfgRowStatus,
       "tmnxL2tpTuCfgLastMgmtChange": tmnxL2tpTuCfgLastMgmtChange,
       "tmnxL2tpTuCfgDescription": tmnxL2tpTuCfgDescription,
       "tmnxL2tpTuCfgAdminState": tmnxL2tpTuCfgAdminState,
       "tmnxL2tpTuCfgPreference": tmnxL2tpTuCfgPreference,
       "tmnxL2tpTuCfgPeerAddrType": tmnxL2tpTuCfgPeerAddrType,
       "tmnxL2tpTuCfgPeerAddr": tmnxL2tpTuCfgPeerAddr,
       "tmnxL2tpTuCfgAddrType": tmnxL2tpTuCfgAddrType,
       "tmnxL2tpTuCfgAddr": tmnxL2tpTuCfgAddr,
       "tmnxL2tpTuCfgLocalName": tmnxL2tpTuCfgLocalName,
       "tmnxL2tpTuCfgRemoteName": tmnxL2tpTuCfgRemoteName,
       "tmnxL2tpTuCfgSecret": tmnxL2tpTuCfgSecret,
       "tmnxL2tpTuCfgHelloInterval": tmnxL2tpTuCfgHelloInterval,
       "tmnxL2tpTuCfgIdleTO": tmnxL2tpTuCfgIdleTO,
       "tmnxL2tpTuCfgDestructTO": tmnxL2tpTuCfgDestructTO,
       "tmnxL2tpTuCfgMaxRetxEstab": tmnxL2tpTuCfgMaxRetxEstab,
       "tmnxL2tpTuCfgMaxRetxNotEstab": tmnxL2tpTuCfgMaxRetxNotEstab,
       "tmnxL2tpTuCfgSessionLimit": tmnxL2tpTuCfgSessionLimit,
       "tmnxL2tpTuCfgAvpHiding": tmnxL2tpTuCfgAvpHiding,
       "tmnxL2tpTuCfgAutoEstab": tmnxL2tpTuCfgAutoEstab,
       "tmnxL2tpTuCfgDoChallenge": tmnxL2tpTuCfgDoChallenge,
       "tmnxL2tpTuCfgReceiveWindowSize": tmnxL2tpTuCfgReceiveWindowSize,
       "tmnxL2tpTuCfgIsaGrpId": tmnxL2tpTuCfgIsaGrpId,
       "tmnxL2tpTuCfgLoadBalanceMethod": tmnxL2tpTuCfgLoadBalanceMethod,
       "tmnxL2tpTuCfgAccountingPolicy": tmnxL2tpTuCfgAccountingPolicy,
       "tmnxL2tpLnsTuPppTable": tmnxL2tpLnsTuPppTable,
       "tmnxL2tpLnsTuPppEntry": tmnxL2tpLnsTuPppEntry,
       "tmnxL2tpLnsTuPppLastMgmtChange": tmnxL2tpLnsTuPppLastMgmtChange,
       "tmnxL2tpLnsTuPppAuthPlcy": tmnxL2tpLnsTuPppAuthPlcy,
       "tmnxL2tpLnsTuPppAuthProtocol": tmnxL2tpLnsTuPppAuthProtocol,
       "tmnxL2tpLnsTuPppUserDb": tmnxL2tpLnsTuPppUserDb,
       "tmnxL2tpLnsTuPppDefaultService": tmnxL2tpLnsTuPppDefaultService,
       "tmnxL2tpLnsTuPppDefaultGroupIf": tmnxL2tpLnsTuPppDefaultGroupIf,
       "tmnxL2tpLnsTuPppProxyLcp": tmnxL2tpLnsTuPppProxyLcp,
       "tmnxL2tpLnsTuPppProxyAuth": tmnxL2tpLnsTuPppProxyAuth,
       "tmnxL2tpLnsTuPppMtu": tmnxL2tpLnsTuPppMtu,
       "tmnxL2tpLnsTuPppLcpKaInterval": tmnxL2tpLnsTuPppLcpKaInterval,
       "tmnxL2tpLnsTuPppLcpKaHoldUp": tmnxL2tpLnsTuPppLcpKaHoldUp,
       "tmnxL2tpLnsTuPppIpcpSubnetNeg": tmnxL2tpLnsTuPppIpcpSubnetNeg,
       "tmnxL2tpLnsTuPppLcpIgnoreMagic": tmnxL2tpLnsTuPppLcpIgnoreMagic,
       "tmnxL2tpLnsTuPppMinChapChall": tmnxL2tpLnsTuPppMinChapChall,
       "tmnxL2tpLnsTuPppMaxChapChall": tmnxL2tpLnsTuPppMaxChapChall,
       "tmnxL2tpTuMlpppTable": tmnxL2tpTuMlpppTable,
       "tmnxL2tpTuMlpppEntry": tmnxL2tpTuMlpppEntry,
       "tmnxL2tpTuMlpppLastMgmtChange": tmnxL2tpTuMlpppLastMgmtChange,
       "tmnxL2tpTuMlpppAdminState": tmnxL2tpTuMlpppAdminState,
       "tmnxL2tpTuMlpppMaxLinks": tmnxL2tpTuMlpppMaxLinks,
       "tmnxL2tpTuMlpppInterleave": tmnxL2tpTuMlpppInterleave,
       "tmnxL2tpTuMlpppMaxFragDelay": tmnxL2tpTuMlpppMaxFragDelay,
       "tmnxL2tpTuMlpppReassemblyTo": tmnxL2tpTuMlpppReassemblyTo,
       "tmnxL2tpTuMlpppShortSeqNumberRx": tmnxL2tpTuMlpppShortSeqNumberRx,
       "tmnxL2tpTuMlpppEpClass": tmnxL2tpTuMlpppEpClass,
       "tmnxL2tpTuMlpppEpIpv4Address": tmnxL2tpTuMlpppEpIpv4Address,
       "tmnxL2tpTuMlpppEpMacAddress": tmnxL2tpTuMlpppEpMacAddress,
       "tmnxL2tpTuXtTable": tmnxL2tpTuXtTable,
       "tmnxL2tpTuXtEntry": tmnxL2tpTuXtEntry,
       "tmnxL2tpTuXtLastMgmtChange": tmnxL2tpTuXtLastMgmtChange,
       "tmnxL2tpTuXtDfBitLac": tmnxL2tpTuXtDfBitLac,
       "tmnxL2tpTuStatObjs": tmnxL2tpTuStatObjs,
       "tmnxL2tpTuStatusTable": tmnxL2tpTuStatusTable,
       "tmnxL2tpTuStatusEntry": tmnxL2tpTuStatusEntry,
       "tmnxL2tpTuStatusId": tmnxL2tpTuStatusId,
       "tmnxL2tpTuStatusState": tmnxL2tpTuStatusState,
       "tmnxL2tpTuStatusTunnelId": tmnxL2tpTuStatusTunnelId,
       "tmnxL2tpTuStatusPreference": tmnxL2tpTuStatusPreference,
       "tmnxL2tpTuStatusPeerAddrType": tmnxL2tpTuStatusPeerAddrType,
       "tmnxL2tpTuStatusPeerAddr": tmnxL2tpTuStatusPeerAddr,
       "tmnxL2tpTuStatusAddrType": tmnxL2tpTuStatusAddrType,
       "tmnxL2tpTuStatusAddr": tmnxL2tpTuStatusAddr,
       "tmnxL2tpTuStatusLocalName": tmnxL2tpTuStatusLocalName,
       "tmnxL2tpTuStatusRemoteName": tmnxL2tpTuStatusRemoteName,
       "tmnxL2tpTuStatusAssignmentId": tmnxL2tpTuStatusAssignmentId,
       "tmnxL2tpTuStatusHelloInterval": tmnxL2tpTuStatusHelloInterval,
       "tmnxL2tpTuStatusIdleTO": tmnxL2tpTuStatusIdleTO,
       "tmnxL2tpTuStatusDestructTO": tmnxL2tpTuStatusDestructTO,
       "tmnxL2tpTuStatusMaxRetxEstab": tmnxL2tpTuStatusMaxRetxEstab,
       "tmnxL2tpTuStatusMaxRetxNotEstab": tmnxL2tpTuStatusMaxRetxNotEstab,
       "tmnxL2tpTuStatusSessionLimit": tmnxL2tpTuStatusSessionLimit,
       "tmnxL2tpTuStatusAvpHiding": tmnxL2tpTuStatusAvpHiding,
       "tmnxL2tpTuStatusGroupName": tmnxL2tpTuStatusGroupName,
       "tmnxL2tpTuStatusRemoteTunnelId": tmnxL2tpTuStatusRemoteTunnelId,
       "tmnxL2tpTuStatusRemoteConnId": tmnxL2tpTuStatusRemoteConnId,
       "tmnxL2tpTuStatusTransportType": tmnxL2tpTuStatusTransportType,
       "tmnxL2tpTuStatusUdpPort": tmnxL2tpTuStatusUdpPort,
       "tmnxL2tpTuStatusRemoteUdpPort": tmnxL2tpTuStatusRemoteUdpPort,
       "tmnxL2tpTuStatusStartTime": tmnxL2tpTuStatusStartTime,
       "tmnxL2tpTuStatusEstabTime": tmnxL2tpTuStatusEstabTime,
       "tmnxL2tpTuStatusIdleTime": tmnxL2tpTuStatusIdleTime,
       "tmnxL2tpTuStatusClosedTime": tmnxL2tpTuStatusClosedTime,
       "tmnxL2tpTuStatusStopCcnResult": tmnxL2tpTuStatusStopCcnResult,
       "tmnxL2tpTuStatusGeneralError": tmnxL2tpTuStatusGeneralError,
       "tmnxL2tpTuStatusErrorMessage": tmnxL2tpTuStatusErrorMessage,
       "tmnxL2tpTuStatusDoChallenge": tmnxL2tpTuStatusDoChallenge,
       "tmnxL2tpTuStatusRws": tmnxL2tpTuStatusRws,
       "tmnxL2tpTuStatusTxDestAddrType": tmnxL2tpTuStatusTxDestAddrType,
       "tmnxL2tpTuStatusTxDestAddr": tmnxL2tpTuStatusTxDestAddr,
       "tmnxL2tpTuStatusRxSrcAddrType": tmnxL2tpTuStatusRxSrcAddrType,
       "tmnxL2tpTuStatusRxSrcAddr": tmnxL2tpTuStatusRxSrcAddr,
       "tmnxL2tpTuStatusAccountingPolicy": tmnxL2tpTuStatusAccountingPolicy,
       "tmnxL2tpTuStatusSelBlacklstState": tmnxL2tpTuStatusSelBlacklstState,
       "tmnxL2tpTuStatusSelBlacklstTime": tmnxL2tpTuStatusSelBlacklstTime,
       "tmnxL2tpTuStatSelBlacklstTimeRem": tmnxL2tpTuStatSelBlacklstTimeRem,
       "tmnxL2tpTuStatusTxDestUdpPort": tmnxL2tpTuStatusTxDestUdpPort,
       "tmnxL2tpTuStatusRxSrcUdpPort": tmnxL2tpTuStatusRxSrcUdpPort,
       "tmnxL2tpTuStatusDfBitLac": tmnxL2tpTuStatusDfBitLac,
       "tmnxL2tpTuStatsTable": tmnxL2tpTuStatsTable,
       "tmnxL2tpTuStatsEntry": tmnxL2tpTuStatsEntry,
       "tmnxL2tpTuStatsLastCleared": tmnxL2tpTuStatsLastCleared,
       "tmnxL2tpTuStatsTotalSessions": tmnxL2tpTuStatsTotalSessions,
       "tmnxL2tpTuStatsFailedSessions": tmnxL2tpTuStatsFailedSessions,
       "tmnxL2tpTuStatsActiveSessions": tmnxL2tpTuStatsActiveSessions,
       "tmnxL2tpTuStatsSessions": tmnxL2tpTuStatsSessions,
       "tmnxL2tpTuStatsControlRxOctets": tmnxL2tpTuStatsControlRxOctets,
       "tmnxL2tpTuStatsControlRxOctetsLw": tmnxL2tpTuStatsControlRxOctetsLw,
       "tmnxL2tpTuStatsControlRxOctetsHw": tmnxL2tpTuStatsControlRxOctetsHw,
       "tmnxL2tpTuStatsControlRxPkts": tmnxL2tpTuStatsControlRxPkts,
       "tmnxL2tpTuStatsControlTxOctets": tmnxL2tpTuStatsControlTxOctets,
       "tmnxL2tpTuStatsControlTxOctetsLw": tmnxL2tpTuStatsControlTxOctetsLw,
       "tmnxL2tpTuStatsControlTxOctetsHw": tmnxL2tpTuStatsControlTxOctetsHw,
       "tmnxL2tpTuStatsControlTxPkts": tmnxL2tpTuStatsControlTxPkts,
       "tmnxL2tpTuStatsErrorTxPkts": tmnxL2tpTuStatsErrorTxPkts,
       "tmnxL2tpTuStatsErrorRxPkts": tmnxL2tpTuStatsErrorRxPkts,
       "tmnxL2tpTuStatsFsmMsgAccepted": tmnxL2tpTuStatsFsmMsgAccepted,
       "tmnxL2tpTuStatsFsmMsgDuplicateRx": tmnxL2tpTuStatsFsmMsgDuplicateRx,
       "tmnxL2tpTuStatsFsmMsgOutOfWndwRx": tmnxL2tpTuStatsFsmMsgOutOfWndwRx,
       "tmnxL2tpTuStatsQLengthUnsentMax": tmnxL2tpTuStatsQLengthUnsentMax,
       "tmnxL2tpTuStatsQLengthUnsentCur": tmnxL2tpTuStatsQLengthUnsentCur,
       "tmnxL2tpTuStatsQLengthAckMax": tmnxL2tpTuStatsQLengthAckMax,
       "tmnxL2tpTuStatsQLengthAckCur": tmnxL2tpTuStatsQLengthAckCur,
       "tmnxL2tpTuStatsWindowSizeCur": tmnxL2tpTuStatsWindowSizeCur,
       "tmnxL2tpTuProtStatsTable": tmnxL2tpTuProtStatsTable,
       "tmnxL2tpTuProtStatsEntry": tmnxL2tpTuProtStatsEntry,
       "tmnxL2tpTuProtStatsType": tmnxL2tpTuProtStatsType,
       "tmnxL2tpTuProtStatsInstance": tmnxL2tpTuProtStatsInstance,
       "tmnxL2tpTuProtStatsName": tmnxL2tpTuProtStatsName,
       "tmnxL2tpTuProtStatsVal": tmnxL2tpTuProtStatsVal,
       "tmnxL2tpTuOpObjs": tmnxL2tpTuOpObjs,
       "tmnxL2tpTuStartTable": tmnxL2tpTuStartTable,
       "tmnxL2tpTuStartEntry": tmnxL2tpTuStartEntry,
       "tmnxL2tpTuStart": tmnxL2tpTuStart,
       "tmnxL2tpTuStopTable": tmnxL2tpTuStopTable,
       "tmnxL2tpTuStopEntry": tmnxL2tpTuStopEntry,
       "tmnxL2tpTuStop": tmnxL2tpTuStop,
       "tmnxL2tpTuDrainTable": tmnxL2tpTuDrainTable,
       "tmnxL2tpTuDrainEntry": tmnxL2tpTuDrainEntry,
       "tmnxL2tpTuDrain": tmnxL2tpTuDrain,
       "tmnxL2tpPeerObjs": tmnxL2tpPeerObjs,
       "tmnxL2tpPeerStatObjs": tmnxL2tpPeerStatObjs,
       "tmnxL2tpPeerStatTable": tmnxL2tpPeerStatTable,
       "tmnxL2tpPeerStatEntry": tmnxL2tpPeerStatEntry,
       "tmnxL2tpPeerStatRole": tmnxL2tpPeerStatRole,
       "tmnxL2tpPeerStatActiveTunnels": tmnxL2tpPeerStatActiveTunnels,
       "tmnxL2tpPeerStatTunnels": tmnxL2tpPeerStatTunnels,
       "tmnxL2tpPeerStatActiveSessions": tmnxL2tpPeerStatActiveSessions,
       "tmnxL2tpPeerStatSessions": tmnxL2tpPeerStatSessions,
       "tmnxL2tpPeerStatDraining": tmnxL2tpPeerStatDraining,
       "tmnxL2tpPeerStatUnreachable": tmnxL2tpPeerStatUnreachable,
       "tmnxL2tpPeerStatUnreachableTime": tmnxL2tpPeerStatUnreachableTime,
       "tmnxL2tpPeerStatControlRxOct": tmnxL2tpPeerStatControlRxOct,
       "tmnxL2tpPeerStatControlRxOctLw": tmnxL2tpPeerStatControlRxOctLw,
       "tmnxL2tpPeerStatControlRxOctHw": tmnxL2tpPeerStatControlRxOctHw,
       "tmnxL2tpPeerStatControlRxPkts": tmnxL2tpPeerStatControlRxPkts,
       "tmnxL2tpPeerStatControlTxOct": tmnxL2tpPeerStatControlTxOct,
       "tmnxL2tpPeerStatControlTxOctLw": tmnxL2tpPeerStatControlTxOctLw,
       "tmnxL2tpPeerStatControlTxOctHw": tmnxL2tpPeerStatControlTxOctHw,
       "tmnxL2tpPeerStatControlTxPkts": tmnxL2tpPeerStatControlTxPkts,
       "tmnxL2tpPeerStatErrorTxPkts": tmnxL2tpPeerStatErrorTxPkts,
       "tmnxL2tpPeerStatErrorRxPkts": tmnxL2tpPeerStatErrorRxPkts,
       "tmnxL2tpPeerStatMsgAccepted": tmnxL2tpPeerStatMsgAccepted,
       "tmnxL2tpPeerStatMsgDuplicateRx": tmnxL2tpPeerStatMsgDuplicateRx,
       "tmnxL2tpPeerStatMsgOutOfWndwRx": tmnxL2tpPeerStatMsgOutOfWndwRx,
       "tmnxL2tpPeerStatRolesCapability": tmnxL2tpPeerStatRolesCapability,
       "tmnxL2tpPeerStatRoles": tmnxL2tpPeerStatRoles,
       "tmnxL2tpPeerStatUnreachTimeRem": tmnxL2tpPeerStatUnreachTimeRem,
       "tmnxL2tpPeerStatLastCleared": tmnxL2tpPeerStatLastCleared,
       "tmnxL2tpPeerTuTable": tmnxL2tpPeerTuTable,
       "tmnxL2tpPeerTuEntry": tmnxL2tpPeerTuEntry,
       "tmnxL2tpPeerTuId": tmnxL2tpPeerTuId,
       "tmnxL2tpPeerProtStatsTable": tmnxL2tpPeerProtStatsTable,
       "tmnxL2tpPeerProtStatsEntry": tmnxL2tpPeerProtStatsEntry,
       "tmnxL2tpPeerProtStatsTransport": tmnxL2tpPeerProtStatsTransport,
       "tmnxL2tpPeerProtStatsAddrType": tmnxL2tpPeerProtStatsAddrType,
       "tmnxL2tpPeerProtStatsAddr": tmnxL2tpPeerProtStatsAddr,
       "tmnxL2tpPeerProtStatsRemUdpPort": tmnxL2tpPeerProtStatsRemUdpPort,
       "tmnxL2tpPeerProtStatsType": tmnxL2tpPeerProtStatsType,
       "tmnxL2tpPeerProtStatsInstance": tmnxL2tpPeerProtStatsInstance,
       "tmnxL2tpPeerProtStatsName": tmnxL2tpPeerProtStatsName,
       "tmnxL2tpPeerProtStatsVal": tmnxL2tpPeerProtStatsVal,
       "tmnxL2tpPeerOpObjs": tmnxL2tpPeerOpObjs,
       "tmnxL2tpPeerDrainTable": tmnxL2tpPeerDrainTable,
       "tmnxL2tpPeerDrainEntry": tmnxL2tpPeerDrainEntry,
       "tmnxL2tpPeerDrain": tmnxL2tpPeerDrain,
       "tmnxL2tpSessionObjs": tmnxL2tpSessionObjs,
       "tmnxL2tpSeStatObjs": tmnxL2tpSeStatObjs,
       "tmnxL2tpSeStatusTable": tmnxL2tpSeStatusTable,
       "tmnxL2tpSeStatusEntry": tmnxL2tpSeStatusEntry,
       "tmnxL2tpSeStatusId": tmnxL2tpSeStatusId,
       "tmnxL2tpSeStatusState": tmnxL2tpSeStatusState,
       "tmnxL2tpSeStatusTunnelId": tmnxL2tpSeStatusTunnelId,
       "tmnxL2tpSeStatusTunnelConnId": tmnxL2tpSeStatusTunnelConnId,
       "tmnxL2tpSeStatusSessionId": tmnxL2tpSeStatusSessionId,
       "tmnxL2tpSeStatusRemoteTunnelId": tmnxL2tpSeStatusRemoteTunnelId,
       "tmnxL2tpSeStatusRemoteSessionId": tmnxL2tpSeStatusRemoteSessionId,
       "tmnxL2tpSeStatusRemoteConnId": tmnxL2tpSeStatusRemoteConnId,
       "tmnxL2tpSeStatusStartTime": tmnxL2tpSeStatusStartTime,
       "tmnxL2tpSeStatusEstabTime": tmnxL2tpSeStatusEstabTime,
       "tmnxL2tpSeStatusClosedTime": tmnxL2tpSeStatusClosedTime,
       "tmnxL2tpSeStatusCdnResult": tmnxL2tpSeStatusCdnResult,
       "tmnxL2tpSeStatusGeneralError": tmnxL2tpSeStatusGeneralError,
       "tmnxL2tpSeStatusErrorMessage": tmnxL2tpSeStatusErrorMessage,
       "tmnxL2tpSeStatusMlpppBundleIndex": tmnxL2tpSeStatusMlpppBundleIndex,
       "tmnxL2tpLnsSePppTable": tmnxL2tpLnsSePppTable,
       "tmnxL2tpLnsSePppEntry": tmnxL2tpLnsSePppEntry,
       "tmnxL2tpLnsSePppUpTime": tmnxL2tpLnsSePppUpTime,
       "tmnxL2tpLnsSePppLcpState": tmnxL2tpLnsSePppLcpState,
       "tmnxL2tpLnsSePppIpcpState": tmnxL2tpLnsSePppIpcpState,
       "tmnxL2tpLnsSePppPppMtu": tmnxL2tpLnsSePppPppMtu,
       "tmnxL2tpLnsSePppPppAuthProtocol": tmnxL2tpLnsSePppPppAuthProtocol,
       "tmnxL2tpLnsSePppPppUserName": tmnxL2tpLnsSePppPppUserName,
       "tmnxL2tpLnsSePppSubIdent": tmnxL2tpLnsSePppSubIdent,
       "tmnxL2tpLnsSePppOriginSubIdent": tmnxL2tpLnsSePppOriginSubIdent,
       "tmnxL2tpLnsSePppSubProfString": tmnxL2tpLnsSePppSubProfString,
       "tmnxL2tpLnsSePppSlaProfString": tmnxL2tpLnsSePppSlaProfString,
       "tmnxL2tpLnsSePppAncpString": tmnxL2tpLnsSePppAncpString,
       "tmnxL2tpLnsSePppInterDestId": tmnxL2tpLnsSePppInterDestId,
       "tmnxL2tpLnsSePppAppProfString": tmnxL2tpLnsSePppAppProfString,
       "tmnxL2tpLnsSePppOriginStrings": tmnxL2tpLnsSePppOriginStrings,
       "tmnxL2tpLnsSePppSessionTimeout": tmnxL2tpLnsSePppSessionTimeout,
       "tmnxL2tpLnsSePppIpAddrType": tmnxL2tpLnsSePppIpAddrType,
       "tmnxL2tpLnsSePppIpAddr": tmnxL2tpLnsSePppIpAddr,
       "tmnxL2tpLnsSePppPrimaryDnsType": tmnxL2tpLnsSePppPrimaryDnsType,
       "tmnxL2tpLnsSePppPrimaryDns": tmnxL2tpLnsSePppPrimaryDns,
       "tmnxL2tpLnsSePppSecondaryDnsType": tmnxL2tpLnsSePppSecondaryDnsType,
       "tmnxL2tpLnsSePppSecondaryDns": tmnxL2tpLnsSePppSecondaryDns,
       "tmnxL2tpLnsSePppPrimaryNbnsType": tmnxL2tpLnsSePppPrimaryNbnsType,
       "tmnxL2tpLnsSePppPrimaryNbns": tmnxL2tpLnsSePppPrimaryNbns,
       "tmnxL2tpLnsSePppSecondNbnsType": tmnxL2tpLnsSePppSecondNbnsType,
       "tmnxL2tpLnsSePppSecondNbns": tmnxL2tpLnsSePppSecondNbns,
       "tmnxL2tpLnsSePppOriginIpcpInfo": tmnxL2tpLnsSePppOriginIpcpInfo,
       "tmnxL2tpLnsSePppCircuitId": tmnxL2tpLnsSePppCircuitId,
       "tmnxL2tpLnsSePppRemoteId": tmnxL2tpLnsSePppRemoteId,
       "tmnxL2tpLnsSePppAddressPool": tmnxL2tpLnsSePppAddressPool,
       "tmnxL2tpLnsSePppType": tmnxL2tpLnsSePppType,
       "tmnxL2tpLnsSePppSvcId": tmnxL2tpLnsSePppSvcId,
       "tmnxL2tpLnsSePppGrpIf": tmnxL2tpLnsSePppGrpIf,
       "tmnxL2tpLnsSePppL2tpVrtrId": tmnxL2tpLnsSePppL2tpVrtrId,
       "tmnxL2tpLnsSePppL2tpConnectionId": tmnxL2tpLnsSePppL2tpConnectionId,
       "tmnxL2tpLnsSePppCategoryMapName": tmnxL2tpLnsSePppCategoryMapName,
       "tmnxL2tpLnsSePppRadiusClassAttr": tmnxL2tpLnsSePppRadiusClassAttr,
       "tmnxL2tpLnsSePppRadiusUserName": tmnxL2tpLnsSePppRadiusUserName,
       "tmnxL2tpLnsSePppIpv6cpState": tmnxL2tpLnsSePppIpv6cpState,
       "tmnxL2tpLnsSePppInterfaceId": tmnxL2tpLnsSePppInterfaceId,
       "tmnxL2tpLnsSePppOriginIpv6cpInfo": tmnxL2tpLnsSePppOriginIpv6cpInfo,
       "tmnxL2tpLnsSePppIpv6DnsType": tmnxL2tpLnsSePppIpv6DnsType,
       "tmnxL2tpLnsSePppIpv6Dns1": tmnxL2tpLnsSePppIpv6Dns1,
       "tmnxL2tpLnsSePppIpv6Dns2": tmnxL2tpLnsSePppIpv6Dns2,
       "tmnxL2tpLnsSePppIpv6DelPfxType": tmnxL2tpLnsSePppIpv6DelPfxType,
       "tmnxL2tpLnsSePppIpv6DelPfxLen": tmnxL2tpLnsSePppIpv6DelPfxLen,
       "tmnxL2tpLnsSePppIpv6DelPfx": tmnxL2tpLnsSePppIpv6DelPfx,
       "tmnxL2tpLnsSePppIpv6PrefixType": tmnxL2tpLnsSePppIpv6PrefixType,
       "tmnxL2tpLnsSePppIpv6PrefixLen": tmnxL2tpLnsSePppIpv6PrefixLen,
       "tmnxL2tpLnsSePppIpv6Prefix": tmnxL2tpLnsSePppIpv6Prefix,
       "tmnxL2tpLnsSePppSubPppIndex": tmnxL2tpLnsSePppSubPppIndex,
       "tmnxL2tpLnsSePppStatTable": tmnxL2tpLnsSePppStatTable,
       "tmnxL2tpLnsSePppStatEntry": tmnxL2tpLnsSePppStatEntry,
       "tmnxL2tpLnsSePppStatRxUnkwnProto": tmnxL2tpLnsSePppStatRxUnkwnProto,
       "tmnxL2tpLnsSePppStatRxLcpConfRq": tmnxL2tpLnsSePppStatRxLcpConfRq,
       "tmnxL2tpLnsSePppStatRxLcpConfAk": tmnxL2tpLnsSePppStatRxLcpConfAk,
       "tmnxL2tpLnsSePppStatRxLcpConfNk": tmnxL2tpLnsSePppStatRxLcpConfNk,
       "tmnxL2tpLnsSePppStatRxLcpConfRj": tmnxL2tpLnsSePppStatRxLcpConfRj,
       "tmnxL2tpLnsSePppStatRxLcpTermRq": tmnxL2tpLnsSePppStatRxLcpTermRq,
       "tmnxL2tpLnsSePppStatRxLcpTermAk": tmnxL2tpLnsSePppStatRxLcpTermAk,
       "tmnxL2tpLnsSePppStatRxLcpCodeRj": tmnxL2tpLnsSePppStatRxLcpCodeRj,
       "tmnxL2tpLnsSePppStatRxLcpEchoRq": tmnxL2tpLnsSePppStatRxLcpEchoRq,
       "tmnxL2tpLnsSePppStatRxLcpEchoRep": tmnxL2tpLnsSePppStatRxLcpEchoRep,
       "tmnxL2tpLnsSePppStatRxLcpProtRj": tmnxL2tpLnsSePppStatRxLcpProtRj,
       "tmnxL2tpLnsSePppStatRxLcpDiscRq": tmnxL2tpLnsSePppStatRxLcpDiscRq,
       "tmnxL2tpLnsSePppStatTxLcpConfRq": tmnxL2tpLnsSePppStatTxLcpConfRq,
       "tmnxL2tpLnsSePppStatTxLcpConfAk": tmnxL2tpLnsSePppStatTxLcpConfAk,
       "tmnxL2tpLnsSePppStatTxLcpConfNk": tmnxL2tpLnsSePppStatTxLcpConfNk,
       "tmnxL2tpLnsSePppStatTxLcpConfRj": tmnxL2tpLnsSePppStatTxLcpConfRj,
       "tmnxL2tpLnsSePppStatTxLcpTermRq": tmnxL2tpLnsSePppStatTxLcpTermRq,
       "tmnxL2tpLnsSePppStatTxLcpTermAk": tmnxL2tpLnsSePppStatTxLcpTermAk,
       "tmnxL2tpLnsSePppStatTxLcpCodeRj": tmnxL2tpLnsSePppStatTxLcpCodeRj,
       "tmnxL2tpLnsSePppStatTxLcpEchoRq": tmnxL2tpLnsSePppStatTxLcpEchoRq,
       "tmnxL2tpLnsSePppStatTxLcpEchoRep": tmnxL2tpLnsSePppStatTxLcpEchoRep,
       "tmnxL2tpLnsSePppStatTxLcpProtRj": tmnxL2tpLnsSePppStatTxLcpProtRj,
       "tmnxL2tpLnsSePppStatTxLcpDiscRq": tmnxL2tpLnsSePppStatTxLcpDiscRq,
       "tmnxL2tpLnsSePppStatRxPapAuthRq": tmnxL2tpLnsSePppStatRxPapAuthRq,
       "tmnxL2tpLnsSePppStatTxPapAuthAk": tmnxL2tpLnsSePppStatTxPapAuthAk,
       "tmnxL2tpLnsSePppStatTxPapAuthNk": tmnxL2tpLnsSePppStatTxPapAuthNk,
       "tmnxL2tpLnsSePppStatRxChapResp": tmnxL2tpLnsSePppStatRxChapResp,
       "tmnxL2tpLnsSePppStatTxChapChall": tmnxL2tpLnsSePppStatTxChapChall,
       "tmnxL2tpLnsSePppStatTxChapSucc": tmnxL2tpLnsSePppStatTxChapSucc,
       "tmnxL2tpLnsSePppStatTxChapFail": tmnxL2tpLnsSePppStatTxChapFail,
       "tmnxL2tpLnsSePppStatRxIpcpConfRq": tmnxL2tpLnsSePppStatRxIpcpConfRq,
       "tmnxL2tpLnsSePppStatRxIpcpConfAk": tmnxL2tpLnsSePppStatRxIpcpConfAk,
       "tmnxL2tpLnsSePppStatRxIpcpConfNk": tmnxL2tpLnsSePppStatRxIpcpConfNk,
       "tmnxL2tpLnsSePppStatRxIpcpConfRj": tmnxL2tpLnsSePppStatRxIpcpConfRj,
       "tmnxL2tpLnsSePppStatRxIpcpTermRq": tmnxL2tpLnsSePppStatRxIpcpTermRq,
       "tmnxL2tpLnsSePppStatRxIpcpTermAk": tmnxL2tpLnsSePppStatRxIpcpTermAk,
       "tmnxL2tpLnsSePppStatRxIpcpCodeRj": tmnxL2tpLnsSePppStatRxIpcpCodeRj,
       "tmnxL2tpLnsSePppStatTxIpcpConfRq": tmnxL2tpLnsSePppStatTxIpcpConfRq,
       "tmnxL2tpLnsSePppStatTxIpcpConfAk": tmnxL2tpLnsSePppStatTxIpcpConfAk,
       "tmnxL2tpLnsSePppStatTxIpcpConfNk": tmnxL2tpLnsSePppStatTxIpcpConfNk,
       "tmnxL2tpLnsSePppStatTxIpcpConfRj": tmnxL2tpLnsSePppStatTxIpcpConfRj,
       "tmnxL2tpLnsSePppStatTxIpcpTermRq": tmnxL2tpLnsSePppStatTxIpcpTermRq,
       "tmnxL2tpLnsSePppStatTxIpcpTermAk": tmnxL2tpLnsSePppStatTxIpcpTermAk,
       "tmnxL2tpLnsSePppStatTxIpcpCodeRj": tmnxL2tpLnsSePppStatTxIpcpCodeRj,
       "tmnxL2tpLnsSePppStatRxIpv6cpCfRq": tmnxL2tpLnsSePppStatRxIpv6cpCfRq,
       "tmnxL2tpLnsSePppStatRxIpv6cpCfAk": tmnxL2tpLnsSePppStatRxIpv6cpCfAk,
       "tmnxL2tpLnsSePppStatRxIpv6cpCfNk": tmnxL2tpLnsSePppStatRxIpv6cpCfNk,
       "tmnxL2tpLnsSePppStatRxIpv6cpCfRj": tmnxL2tpLnsSePppStatRxIpv6cpCfRj,
       "tmnxL2tpLnsSePppStatRxIpv6cpTmRq": tmnxL2tpLnsSePppStatRxIpv6cpTmRq,
       "tmnxL2tpLnsSePppStatRxIpv6cpTmAk": tmnxL2tpLnsSePppStatRxIpv6cpTmAk,
       "tmnxL2tpLnsSePppStatRxIpv6cpCdRj": tmnxL2tpLnsSePppStatRxIpv6cpCdRj,
       "tmnxL2tpLnsSePppStatTxIpv6cpCfRq": tmnxL2tpLnsSePppStatTxIpv6cpCfRq,
       "tmnxL2tpLnsSePppStatTxIpv6cpCfAk": tmnxL2tpLnsSePppStatTxIpv6cpCfAk,
       "tmnxL2tpLnsSePppStatTxIpv6cpCfNk": tmnxL2tpLnsSePppStatTxIpv6cpCfNk,
       "tmnxL2tpLnsSePppStatTxIpv6cpCfRj": tmnxL2tpLnsSePppStatTxIpv6cpCfRj,
       "tmnxL2tpLnsSePppStatTxIpv6cpTmRq": tmnxL2tpLnsSePppStatTxIpv6cpTmRq,
       "tmnxL2tpLnsSePppStatTxIpv6cpTmAk": tmnxL2tpLnsSePppStatTxIpv6cpTmAk,
       "tmnxL2tpLnsSePppStatTxIpv6cpCdRj": tmnxL2tpLnsSePppStatTxIpv6cpCdRj,
       "tmnxL2tpLnsSeMRtTable": tmnxL2tpLnsSeMRtTable,
       "tmnxL2tpLnsSeMRtEntry": tmnxL2tpLnsSeMRtEntry,
       "tmnxL2tpLnsSeMRtAddrType": tmnxL2tpLnsSeMRtAddrType,
       "tmnxL2tpLnsSeMRtAddr": tmnxL2tpLnsSeMRtAddr,
       "tmnxL2tpLnsSeMRtPrefixLen": tmnxL2tpLnsSeMRtPrefixLen,
       "tmnxL2tpLnsSeMRtStatus": tmnxL2tpLnsSeMRtStatus,
       "tmnxL2tpLnsSeOvrTable": tmnxL2tpLnsSeOvrTable,
       "tmnxL2tpLnsSeOvrEntry": tmnxL2tpLnsSeOvrEntry,
       "tmnxL2tpLnsSeOvrDirection": tmnxL2tpLnsSeOvrDirection,
       "tmnxL2tpLnsSeOvrType": tmnxL2tpLnsSeOvrType,
       "tmnxL2tpLnsSeOvrTypeId": tmnxL2tpLnsSeOvrTypeId,
       "tmnxL2tpLnsSeOvrTypeName": tmnxL2tpLnsSeOvrTypeName,
       "tmnxL2tpLnsSeOvrPIR": tmnxL2tpLnsSeOvrPIR,
       "tmnxL2tpLnsSeOvrCIR": tmnxL2tpLnsSeOvrCIR,
       "tmnxL2tpLnsSeOvrCBS": tmnxL2tpLnsSeOvrCBS,
       "tmnxL2tpLnsSeOvrMBS": tmnxL2tpLnsSeOvrMBS,
       "tmnxL2tpLnsSeAleTable": tmnxL2tpLnsSeAleTable,
       "tmnxL2tpLnsSeAleEntry": tmnxL2tpLnsSeAleEntry,
       "tmnxL2tpLnsSeAleDatalink": tmnxL2tpLnsSeAleDatalink,
       "tmnxL2tpLnsSeAleEncaps1": tmnxL2tpLnsSeAleEncaps1,
       "tmnxL2tpLnsSeAleEncaps2": tmnxL2tpLnsSeAleEncaps2,
       "tmnxL2tpSeOpObjs": tmnxL2tpSeOpObjs,
       "tmnxL2tpSeStopTable": tmnxL2tpSeStopTable,
       "tmnxL2tpSeStopEntry": tmnxL2tpSeStopEntry,
       "tmnxL2tpSeStop": tmnxL2tpSeStop,
       "tmnxL2tpLnsIsaObjs": tmnxL2tpLnsIsaObjs,
       "tmnxL2tpLnsIsaGrpObjs": tmnxL2tpLnsIsaGrpObjs,
       "tmnxL2tpIsaGrpTable": tmnxL2tpIsaGrpTable,
       "tmnxL2tpIsaGrpEntry": tmnxL2tpIsaGrpEntry,
       "tmnxL2tpIsaGrpId": tmnxL2tpIsaGrpId,
       "tmnxL2tpIsaGrpRowStatus": tmnxL2tpIsaGrpRowStatus,
       "tmnxL2tpIsaGrpLastMgmtChange": tmnxL2tpIsaGrpLastMgmtChange,
       "tmnxL2tpIsaGrpDescription": tmnxL2tpIsaGrpDescription,
       "tmnxL2tpIsaGrpAdminState": tmnxL2tpIsaGrpAdminState,
       "tmnxL2tpIsaGrpOperState": tmnxL2tpIsaGrpOperState,
       "tmnxL2tpIsaGrpPortPlcy": tmnxL2tpIsaGrpPortPlcy,
       "tmnxL2tpLnsIsaMdaObjs": tmnxL2tpLnsIsaMdaObjs,
       "tmnxL2tpIsaMdaTable": tmnxL2tpIsaMdaTable,
       "tmnxL2tpIsaMdaEntry": tmnxL2tpIsaMdaEntry,
       "tmnxL2tpIsaMdaRowStatus": tmnxL2tpIsaMdaRowStatus,
       "tmnxL2tpIsaMdaLastMgmtChange": tmnxL2tpIsaMdaLastMgmtChange,
       "tmnxL2tpIsaMdaDrain": tmnxL2tpIsaMdaDrain,
       "tmnxL2tpIsaMdaStop": tmnxL2tpIsaMdaStop,
       "tmnxL2tpLnsIsaMdaStatObjs": tmnxL2tpLnsIsaMdaStatObjs,
       "tmnxL2tpIsaMdaStatTable": tmnxL2tpIsaMdaStatTable,
       "tmnxL2tpIsaMdaStatEntry": tmnxL2tpIsaMdaStatEntry,
       "tmnxL2tpIsaMdaStatOperState": tmnxL2tpIsaMdaStatOperState,
       "tmnxL2tpIsaMdaStatSessions": tmnxL2tpIsaMdaStatSessions,
       "tmnxL2tpIsaMdaVRtrTable": tmnxL2tpIsaMdaVRtrTable,
       "tmnxL2tpIsaMdaVRtrEntry": tmnxL2tpIsaMdaVRtrEntry,
       "tmnxL2tpIsaMdaVRtrOperState": tmnxL2tpIsaMdaVRtrOperState,
       "tmnxL2tpLnsIsaMdaStatisticsObjs": tmnxL2tpLnsIsaMdaStatisticsObjs,
       "tmnxL2tpIsaMdaStatisticsTable": tmnxL2tpIsaMdaStatisticsTable,
       "tmnxL2tpIsaMdaStatisticsEntry": tmnxL2tpIsaMdaStatisticsEntry,
       "tmnxL2tpIsaMdaStatsInstance": tmnxL2tpIsaMdaStatsInstance,
       "tmnxL2tpIsaMdaStatsName": tmnxL2tpIsaMdaStatsName,
       "tmnxL2tpIsaMdaStatsVal": tmnxL2tpIsaMdaStatsVal,
       "tmnxL2tpIsaMdaStatsValHw": tmnxL2tpIsaMdaStatsValHw,
       "tmnxL2tpIsaMdaStatsValue": tmnxL2tpIsaMdaStatsValue,
       "tmnxL2tpLnsSvcObjs": tmnxL2tpLnsSvcObjs,
       "tmnxL2tpLnsIfObjs": tmnxL2tpLnsIfObjs,
       "tmnxL2tpLnsIfTable": tmnxL2tpLnsIfTable,
       "tmnxL2tpLnsIfEntry": tmnxL2tpLnsIfEntry,
       "tmnxL2tpLnsIfLastMgmtChange": tmnxL2tpLnsIfLastMgmtChange,
       "tmnxL2tpLnsIfDescription": tmnxL2tpLnsIfDescription,
       "tmnxL2tpLnsIfDefSubProfile": tmnxL2tpLnsIfDefSubProfile,
       "tmnxL2tpLnsIfDefSlaProfile": tmnxL2tpLnsIfDefSlaProfile,
       "tmnxL2tpLnsIfDefAppProfile": tmnxL2tpLnsIfDefAppProfile,
       "tmnxL2tpLnsIfSubIdentPolicy": tmnxL2tpLnsIfSubIdentPolicy,
       "tmnxL2tpLnsIfDefSubIdent": tmnxL2tpLnsIfDefSubIdent,
       "tmnxL2tpLnsIfDefSubIdentString": tmnxL2tpLnsIfDefSubIdentString,
       "tmnxL2tpLnsIfDefFilterProfile": tmnxL2tpLnsIfDefFilterProfile,
       "tmnxL2tpMlpppObjs": tmnxL2tpMlpppObjs,
       "tmnxL2tpLacMlpppBundleTable": tmnxL2tpLacMlpppBundleTable,
       "tmnxL2tpLacMlpppBundleEntry": tmnxL2tpLacMlpppBundleEntry,
       "tmnxL2tpLacMlpppBundleIndex": tmnxL2tpLacMlpppBundleIndex,
       "tmnxL2tpLacMlpppBundleSvcId": tmnxL2tpLacMlpppBundleSvcId,
       "tmnxL2tpLacMlpppBundleFwdTuId": tmnxL2tpLacMlpppBundleFwdTuId,
       "tmnxL2tpLacMlpppBundleUserName": tmnxL2tpLacMlpppBundleUserName,
       "tmnxL2tpLacMlpppBundleLocEpClass": tmnxL2tpLacMlpppBundleLocEpClass,
       "tmnxL2tpLacMlpppBundleLocEpAddr": tmnxL2tpLacMlpppBundleLocEpAddr,
       "tmnxL2tpLacMlpppBundleRemEpClass": tmnxL2tpLacMlpppBundleRemEpClass,
       "tmnxL2tpLacMlpppBundleRemEpAddr": tmnxL2tpLacMlpppBundleRemEpAddr,
       "tmnxL2tpLacMlpppLinkTable": tmnxL2tpLacMlpppLinkTable,
       "tmnxL2tpLacMlpppLinkEntry": tmnxL2tpLacMlpppLinkEntry,
       "tmnxL2tpLacMlpppLinkState": tmnxL2tpLacMlpppLinkState,
       "tmnxL2tpTableLastCh": tmnxL2tpTableLastCh,
       "tmnxL2tpTgCfgTableLastCh": tmnxL2tpTgCfgTableLastCh,
       "tmnxL2tpTuCfgTableLastCh": tmnxL2tpTuCfgTableLastCh,
       "tmnxL2tpTuStatusTableLastCh": tmnxL2tpTuStatusTableLastCh,
       "tmnxL2tpSeStatusTableLastCh": tmnxL2tpSeStatusTableLastCh,
       "tmnxL2tpIsaGrpTableLastCh": tmnxL2tpIsaGrpTableLastCh,
       "tmnxL2tpIsaMdaTableLastCh": tmnxL2tpIsaMdaTableLastCh,
       "tmnxL2tpIsaMdaStatTableLastCh": tmnxL2tpIsaMdaStatTableLastCh,
       "tmnxL2tpLnsTgPppTableLastCh": tmnxL2tpLnsTgPppTableLastCh,
       "tmnxL2tpLnsTuPppTableLastCh": tmnxL2tpLnsTuPppTableLastCh,
       "tmnxL2tpLnsSePppTableLastCh": tmnxL2tpLnsSePppTableLastCh,
       "tmnxL2tpLnsSeAleTableLastCh": tmnxL2tpLnsSeAleTableLastCh,
       "tmnxL2tpXtTableLastCh": tmnxL2tpXtTableLastCh,
       "tmnxL2tpIsaMdaStatsTableLastCh": tmnxL2tpIsaMdaStatsTableLastCh,
       "tmnxL2tpTgXtTableLastCh": tmnxL2tpTgXtTableLastCh,
       "tmnxL2tpTuXtTableLastCh": tmnxL2tpTuXtTableLastCh,
       "tmnxL2tpAccountingObjs": tmnxL2tpAccountingObjs,
       "tmnxL2tpApTable": tmnxL2tpApTable,
       "tmnxL2tpApEntry": tmnxL2tpApEntry,
       "tmnxL2tpApName": tmnxL2tpApName,
       "tmnxL2tpApRowStatus": tmnxL2tpApRowStatus,
       "tmnxL2tpApLastMgmtChange": tmnxL2tpApLastMgmtChange,
       "tmnxL2tpApDescription": tmnxL2tpApDescription,
       "tmnxL2tpApType": tmnxL2tpApType,
       "tmnxL2tpApServerVRtrID": tmnxL2tpApServerVRtrID,
       "tmnxL2tpApServerAlgorithm": tmnxL2tpApServerAlgorithm,
       "tmnxL2tpApServerRetry": tmnxL2tpApServerRetry,
       "tmnxL2tpApServerSrcAddrType": tmnxL2tpApServerSrcAddrType,
       "tmnxL2tpApServerSrcAddr": tmnxL2tpApServerSrcAddr,
       "tmnxL2tpApServerTimeout": tmnxL2tpApServerTimeout,
       "tmnxL2tpApIncludeAttributes": tmnxL2tpApIncludeAttributes,
       "tmnxL2tpApRequestScriptPlcy": tmnxL2tpApRequestScriptPlcy,
       "tmnxL2tpApNasPortIdPfixType": tmnxL2tpApNasPortIdPfixType,
       "tmnxL2tpApNasPortIdPfixString": tmnxL2tpApNasPortIdPfixString,
       "tmnxL2tpApNasPortIdSfixType": tmnxL2tpApNasPortIdSfixType,
       "tmnxL2tpApNasPortTypeType": tmnxL2tpApNasPortTypeType,
       "tmnxL2tpApNasPortTypeValue": tmnxL2tpApNasPortTypeValue,
       "tmnxL2tpApNasPortBitspec": tmnxL2tpApNasPortBitspec,
       "tmnxL2tpApRadServPlcy": tmnxL2tpApRadServPlcy,
       "tmnxL2tpApServTable": tmnxL2tpApServTable,
       "tmnxL2tpApServEntry": tmnxL2tpApServEntry,
       "tmnxL2tpApServIndex": tmnxL2tpApServIndex,
       "tmnxL2tpApServRowStatus": tmnxL2tpApServRowStatus,
       "tmnxL2tpApServLastMgmtChange": tmnxL2tpApServLastMgmtChange,
       "tmnxL2tpApServAddrType": tmnxL2tpApServAddrType,
       "tmnxL2tpApServAddr": tmnxL2tpApServAddr,
       "tmnxL2tpApServSecret": tmnxL2tpApServSecret,
       "tmnxL2tpApServAcctPort": tmnxL2tpApServAcctPort,
       "tmnxL2tpApServOperState": tmnxL2tpApServOperState,
       "tmnxL2tpApServStatsTable": tmnxL2tpApServStatsTable,
       "tmnxL2tpApServStatsEntry": tmnxL2tpApServStatsEntry,
       "tmnxL2tpApServStatsTxRequests": tmnxL2tpApServStatsTxRequests,
       "tmnxL2tpApServStatsRxResponses": tmnxL2tpApServStatsRxResponses,
       "tmnxL2tpApServStatsReqTimeout": tmnxL2tpApServStatsReqTimeout,
       "tmnxL2tpApServStatsReqSendFail": tmnxL2tpApServStatsReqSendFail,
       "tmnxL2tpApServStatsReqPending": tmnxL2tpApServStatsReqPending,
       "tmnxL2tpApServStatsRespInvAuth": tmnxL2tpApServStatsRespInvAuth,
       "tmnxL2tpApServStatsSendRetries": tmnxL2tpApServStatsSendRetries,
       "tmnxL2tpApTableLastCh": tmnxL2tpApTableLastCh,
       "tmnxL2tpApServTableLastCh": tmnxL2tpApServTableLastCh,
       "tmnxL2tpNotificationObjs": tmnxL2tpNotificationObjs,
       "tmnxL2tpNotifyDescription": tmnxL2tpNotifyDescription,
       "tmnxL2tpPppNcpFailureProtocol": tmnxL2tpPppNcpFailureProtocol,
       "tmnxL2tpNotifyPrefix": tmnxL2tpNotifyPrefix,
       "tmnxL2tpNotifications": tmnxL2tpNotifications,
       "tmnxL2tpPeerUnreachable": tmnxL2tpPeerUnreachable,
       "tmnxL2tpIsaMdaVRtrStateChange": tmnxL2tpIsaMdaVRtrStateChange,
       "tmnxL2tpLnsSePppSessionFailure": tmnxL2tpLnsSePppSessionFailure,
       "tmnxL2tpLnsPppNcpFailure": tmnxL2tpLnsPppNcpFailure,
       "tmnxL2tpApFailure": tmnxL2tpApFailure,
       "tmnxL2tpTunnelBlacklisted": tmnxL2tpTunnelBlacklisted,
       "tmnxL2tpTunnelSelBlacklistFull": tmnxL2tpTunnelSelBlacklistFull}
)
