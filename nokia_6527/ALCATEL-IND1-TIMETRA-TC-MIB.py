# SNMP MIB module (ALCATEL-IND1-TIMETRA-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALCATEL-IND1-TIMETRA-TC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:55:46 2025
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

(timetraModules,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraModules")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

timetraTCMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 2)
)
if mibBuilder.loadTexts:
    timetraTCMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-23 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-05-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TmnxPortID(TextualConvention, Unsigned32):
    status = "current"


class TmnxEncapVal(TextualConvention, Unsigned32):
    status = "current"


class QTag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class QTagOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class TmnxStrSapId(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class IpAddressPrefixLength(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )



class TmnxActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doAction", 1),
          ("notApplicable", 2))
    )



class TmnxAdminState(TextualConvention, Integer32):
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
        *(("noop", 1),
          ("inService", 2),
          ("outOfService", 3))
    )



class TmnxOperState(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("transition", 4))
    )



class TmnxStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )



class TmnxEnabledDisabled(TextualConvention, Integer32):
    status = "current"
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



class TNamedItem(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TNamedItemOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TItemDescription(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TItemLongDescription(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )



class TmnxVRtrID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class TmnxVRtrIDOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )



class TmnxBgpAutonomousSystem(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxBgpLocalPreference(TextualConvention, Unsigned32):
    status = "current"


class TmnxBgpPreference(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxCustId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class TmnxServId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class ServiceAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class ServiceOperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class TPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TSapIngressPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TSapEgressPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TPolicyStatementNameOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TmnxVcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10,
              11,
              17,
              18,
              19,
              20,
              21,
              23,
              25,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("frDlciMartini", 1),
          ("atmSdu", 2),
          ("atmCell", 3),
          ("ethernetVlan", 4),
          ("ethernet", 5),
          ("atmVccCell", 9),
          ("atmVpcCell", 10),
          ("ipipe", 11),
          ("satopE1", 17),
          ("satopT1", 18),
          ("satopE3", 19),
          ("satopT3", 20),
          ("cesopsn", 21),
          ("cesopsnCas", 23),
          ("frDlci", 25),
          ("mirrorDest", 4096))
    )



class TmnxVcId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxVcIdOrNone(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class Dot1PPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class ServiceAccessPoint(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TLspExpValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TIpProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TIpOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TTcpUdpPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TTcpUdpPortOperator(TextualConvention, Integer32):
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
        *(("none", 0),
          ("eq", 1),
          ("range", 2),
          ("lt", 3),
          ("gt", 4))
    )



class TFrameType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e802dot3", 0),
          ("e802dot2LLC", 1),
          ("e802dot2SNAP", 2),
          ("ethernetII", 3))
    )



class TQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TIngressQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TEgressQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TDSCPName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TDSCPNameOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TDSCPValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class TDSCPValueOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )



class TDSCPFilterActionValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TFCName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TFCNameOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TFCSet(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("be", 0),
          ("l2", 1),
          ("af", 2),
          ("l1", 3),
          ("h2", 4),
          ("ef", 5),
          ("h1", 6),
          ("nc", 7))
    )


class TFCType(TextualConvention, Integer32):
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
        *(("be", 0),
          ("l2", 1),
          ("af", 2),
          ("l1", 3),
          ("h2", 4),
          ("ef", 5),
          ("h1", 6),
          ("nc", 7))
    )



class TmnxTunnelType(TextualConvention, Integer32):
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
        *(("sdp", 1),
          ("ldp", 2),
          ("rsvp", 3),
          ("gre", 4),
          ("bypass", 5),
          ("invalid", 6))
    )



class TmnxTunnelID(TextualConvention, Unsigned32):
    status = "current"


class TmnxBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxVPNRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class SdpBindId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TmnxVRtrMplsLspID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TPortSchedulerPIR(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 40000000),
    )



class TPortSchedulerCIR(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 40000000),
    )



class TWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class TPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TSecondaryShaper10GPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )



class TPIRRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TPIRRateOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class TmnxDHCP6MsgType(TextualConvention, Integer32):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("dhcp6MsgTypeSolicit", 1),
          ("dhcp6MsgTypeAdvertise", 2),
          ("dhcp6MsgTypeRequest", 3),
          ("dhcp6MsgTypeConfirm", 4),
          ("dhcp6MsgTypeRenew", 5),
          ("dhcp6MsgTypeRebind", 6),
          ("dhcp6MsgTypeReply", 7),
          ("dhcp6MsgTypeRelease", 8),
          ("dhcp6MsgTypeDecline", 9),
          ("dhcp6MsgTypeReconfigure", 10),
          ("dhcp6MsgTypeInfoRequest", 11),
          ("dhcp6MsgTypeRelayForw", 12),
          ("dhcp6MsgTypeRelayReply", 13),
          ("dhcp6MsgTypeMaxValue", 14))
    )



class TmnxOspfInstance(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )



class TmnxBGPFamilyType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ipv4Unicast", 0),
          ("ipv4Multicast", 1),
          ("ipv4UastMcast", 2),
          ("ipv4MplsLabel", 3),
          ("ipv4Vpn", 4),
          ("ipv6Unicast", 5),
          ("ipv6Multicast", 6),
          ("ipv6UcastMcast", 7),
          ("ipv6MplsLabel", 8),
          ("ipv6Vpn", 9))
    )


class TmnxIgmpGroupFilterMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )



class TmnxIgmpGroupType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )



class TmnxIgmpVersion(TextualConvention, Integer32):
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )



class TmnxMldGroupFilterMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )



class TmnxMldGroupType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )



class TmnxMldVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )



class TmnxManagedRouteStatus(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("installed", 0),
          ("notYetInstalled", 1),
          ("wrongAntiSpoofType", 2),
          ("outOfMemory", 3),
          ("shadowed", 4),
          ("routeTableFull", 5),
          ("parentInterfaceDown", 6))
    )



class TmnxAncpString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class TmnxAncpStringOrZero(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class TmnxMulticastAddrFamily(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Multicast", 0),
          ("ipv6Multicast", 1))
    )



class TmnxSubIdentString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxSubIdentStringOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubProfileString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxSubProfileStringOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxSlaProfileString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxSlaProfileStringOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxAppProfileString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxAppProfileStringOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxSubMgtIntDestIdOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubMgtIntDestId(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxDhcpOptionType(TextualConvention, Integer32):
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
        *(("ipv4", 1),
          ("ascii", 2),
          ("hex", 3))
    )



class TmnxDhcpVendorOption(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("systemId", 0),
          ("clientMac", 1),
          ("serviceId", 2),
          ("sapId", 3))
    )


class TmnxPppoeUserNameOrEmpty(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class TCpmProtPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TMlpppQoSProfileId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "TmnxPortID": TmnxPortID,
       "TmnxEncapVal": TmnxEncapVal,
       "QTag": QTag,
       "QTagOrZero": QTagOrZero,
       "TmnxStrSapId": TmnxStrSapId,
       "IpAddressPrefixLength": IpAddressPrefixLength,
       "TmnxActionType": TmnxActionType,
       "TmnxAdminState": TmnxAdminState,
       "TmnxOperState": TmnxOperState,
       "TmnxStatus": TmnxStatus,
       "TmnxEnabledDisabled": TmnxEnabledDisabled,
       "TNamedItem": TNamedItem,
       "TNamedItemOrEmpty": TNamedItemOrEmpty,
       "TItemDescription": TItemDescription,
       "TItemLongDescription": TItemLongDescription,
       "TmnxVRtrID": TmnxVRtrID,
       "TmnxVRtrIDOrZero": TmnxVRtrIDOrZero,
       "TmnxBgpAutonomousSystem": TmnxBgpAutonomousSystem,
       "TmnxBgpLocalPreference": TmnxBgpLocalPreference,
       "TmnxBgpPreference": TmnxBgpPreference,
       "TmnxCustId": TmnxCustId,
       "TmnxServId": TmnxServId,
       "ServiceAdminStatus": ServiceAdminStatus,
       "ServiceOperStatus": ServiceOperStatus,
       "TPolicyID": TPolicyID,
       "TSapIngressPolicyID": TSapIngressPolicyID,
       "TSapEgressPolicyID": TSapEgressPolicyID,
       "TPolicyStatementNameOrEmpty": TPolicyStatementNameOrEmpty,
       "TmnxVcType": TmnxVcType,
       "TmnxVcId": TmnxVcId,
       "TmnxVcIdOrNone": TmnxVcIdOrNone,
       "Dot1PPriority": Dot1PPriority,
       "ServiceAccessPoint": ServiceAccessPoint,
       "TLspExpValue": TLspExpValue,
       "TIpProtocol": TIpProtocol,
       "TIpOption": TIpOption,
       "TTcpUdpPort": TTcpUdpPort,
       "TTcpUdpPortOperator": TTcpUdpPortOperator,
       "TFrameType": TFrameType,
       "TQueueId": TQueueId,
       "TIngressQueueId": TIngressQueueId,
       "TEgressQueueId": TEgressQueueId,
       "TDSCPName": TDSCPName,
       "TDSCPNameOrEmpty": TDSCPNameOrEmpty,
       "TDSCPValue": TDSCPValue,
       "TDSCPValueOrNone": TDSCPValueOrNone,
       "TDSCPFilterActionValue": TDSCPFilterActionValue,
       "TFCName": TFCName,
       "TFCNameOrEmpty": TFCNameOrEmpty,
       "TFCSet": TFCSet,
       "TFCType": TFCType,
       "TmnxTunnelType": TmnxTunnelType,
       "TmnxTunnelID": TmnxTunnelID,
       "TmnxBgpRouteTarget": TmnxBgpRouteTarget,
       "TmnxVPNRouteDistinguisher": TmnxVPNRouteDistinguisher,
       "SdpBindId": SdpBindId,
       "TmnxVRtrMplsLspID": TmnxVRtrMplsLspID,
       "TPortSchedulerPIR": TPortSchedulerPIR,
       "TPortSchedulerCIR": TPortSchedulerCIR,
       "TWeight": TWeight,
       "TCIRRate": TCIRRate,
       "TPIRRate": TPIRRate,
       "TSecondaryShaper10GPIRRate": TSecondaryShaper10GPIRRate,
       "TPIRRateOverride": TPIRRateOverride,
       "TPIRRateOrZero": TPIRRateOrZero,
       "TmnxDHCP6MsgType": TmnxDHCP6MsgType,
       "TmnxOspfInstance": TmnxOspfInstance,
       "TmnxBGPFamilyType": TmnxBGPFamilyType,
       "TmnxIgmpGroupFilterMode": TmnxIgmpGroupFilterMode,
       "TmnxIgmpGroupType": TmnxIgmpGroupType,
       "TmnxIgmpVersion": TmnxIgmpVersion,
       "TmnxMldGroupFilterMode": TmnxMldGroupFilterMode,
       "TmnxMldGroupType": TmnxMldGroupType,
       "TmnxMldVersion": TmnxMldVersion,
       "TmnxManagedRouteStatus": TmnxManagedRouteStatus,
       "TmnxAncpString": TmnxAncpString,
       "TmnxAncpStringOrZero": TmnxAncpStringOrZero,
       "TmnxMulticastAddrFamily": TmnxMulticastAddrFamily,
       "TmnxSubIdentString": TmnxSubIdentString,
       "TmnxSubIdentStringOrEmpty": TmnxSubIdentStringOrEmpty,
       "TmnxSubProfileString": TmnxSubProfileString,
       "TmnxSubProfileStringOrEmpty": TmnxSubProfileStringOrEmpty,
       "TmnxSlaProfileString": TmnxSlaProfileString,
       "TmnxSlaProfileStringOrEmpty": TmnxSlaProfileStringOrEmpty,
       "TmnxAppProfileString": TmnxAppProfileString,
       "TmnxAppProfileStringOrEmpty": TmnxAppProfileStringOrEmpty,
       "TmnxSubMgtIntDestIdOrEmpty": TmnxSubMgtIntDestIdOrEmpty,
       "TmnxSubMgtIntDestId": TmnxSubMgtIntDestId,
       "TmnxDhcpOptionType": TmnxDhcpOptionType,
       "TmnxDhcpVendorOption": TmnxDhcpVendorOption,
       "TmnxPppoeUserNameOrEmpty": TmnxPppoeUserNameOrEmpty,
       "TCpmProtPolicyID": TCpmProtPolicyID,
       "TMlpppQoSProfileId": TMlpppQoSProfileId,
       "timetraTCMIBModule": timetraTCMIBModule}
)
