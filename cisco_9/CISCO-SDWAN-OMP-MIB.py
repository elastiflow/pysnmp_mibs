# SNMP MIB module (CISCO-SDWAN-OMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDWAN-OMP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:58 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSdwanOmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003)
)
if mibBuilder.loadTexts:
    ciscoSdwanOmpMIB.setRevisions(
        ("2021-03-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IpPrefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(17, 17),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Groups1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class AttributeTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("original", 0),
          ("installed", 1))
    )



class ReceivedPrunes1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class AdvertisedPrunes1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class BfdStatusEnum(TextualConvention, Integer32):
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
        *(("up", 0),
          ("down", 1),
          ("inactive", 2))
    )



class PathStatusEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chosen", 0),
          ("backup", 1))
    )



class RibInStatusType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("c", 0),
          ("i", 1),
          ("red", 2),
          ("rej", 3),
          ("l", 4),
          ("r", 5),
          ("s", 6),
          ("ext", 7),
          ("inv", 8),
          ("u", 9),
          ("stg", 10),
          ("ia", 11),
          ("brr", 12),
          ("tgwr", 13))
    )


class AddrFamilyEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )



class LossReasonEnum(TextualConvention, Integer32):
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("invalid", 1),
          ("personality", 2),
          ("distance", 3),
          ("preference", 4),
          ("tloc-preference", 5),
          ("origin-protocol", 6),
          ("origin-protocol-subtype", 7),
          ("origin-metric", 8),
          ("peer-id", 9),
          ("tloc-id", 10),
          ("stale-entry", 11),
          ("site-id", 12),
          ("omp-version", 13),
          ("tloc-gen-id", 14),
          ("tloc-spi", 15),
          ("ultimate-tloc-id", 16),
          ("tloc-action", 17),
          ("path-inactive", 18),
          ("region-id", 19),
          ("region-path", 20),
          ("transport-gateway", 21),
          ("affinity-group", 22),
          ("migration-bgp-community", 23),
          ("as-path-length", 24),
          ("migration-omp-prefer", 25),
          ("sub-region-id", 26),
          ("br-preference", 27),
          ("derived-affinity-group-number", 28))
    )



class McastRouteEnum(TextualConvention, Integer32):
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
        *(("starGroup", 0),
          ("sourceGroup", 1),
          ("sourceActive", 2))
    )



class TlocColorEnum(TextualConvention, Integer32):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )



class TlocEncapEnum(TextualConvention, Integer32):
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
        *(("none", 0),
          ("gre", 1),
          ("ipsec", 2))
    )



class ProtocolEnum(TextualConvention, Integer32):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("proto-invalid", 0),
          ("static", 1),
          ("connected", 2),
          ("eBGP", 3),
          ("iBGP", 4),
          ("oSPF-intra-area", 5),
          ("oSPF-inter-area", 6),
          ("oSPF-external-1", 7),
          ("oSPF-external-2", 8),
          ("aggregate", 9),
          ("natpoolInside", 10),
          ("eigrp-sum", 11),
          ("eigrp-int", 12),
          ("eigrp-ext", 13),
          ("lisp", 14),
          ("isis-level-1", 15),
          ("isis-level-2", 16),
          ("oSPF-nssa-1", 17),
          ("oSPF-nssa-2", 18),
          ("oSPF-nat-dia", 19),
          ("rip", 20))
    )



class TlocActionEnum(TextualConvention, Integer32):
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
          ("strict", 1),
          ("primary", 2),
          ("ecmp", 3),
          ("backup", 4))
    )



class EncryptType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("null", 0),
          ("des", 1),
          ("des3", 2),
          ("aes128", 3),
          ("aes192", 4),
          ("aes256", 5),
          ("aes128Ctr", 6),
          ("aes192Ctr", 7),
          ("aes256Ctr", 8),
          ("aes128Gmac", 9),
          ("aes192Gmac", 10),
          ("aes256Gmac", 11))
    )


class IntegType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("esp", 1),
          ("ip-udp-esp", 2),
          ("ip-udp-esp-no-id", 3))
    )


class CarrierEnum(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("carrier1", 2),
          ("carrier2", 3),
          ("carrier3", 4),
          ("carrier4", 5),
          ("carrier5", 6),
          ("carrier6", 7),
          ("carrier7", 8),
          ("carrier8", 9))
    )



class NotificationSeverity(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )



class OperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )



class PeerState(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("init", 1),
          ("handshake", 2),
          ("up", 3),
          ("down", 4),
          ("init-in-gr", 5),
          ("down-in-gr", 6),
          ("handshake-in-gr", 7),
          ("up-in-gr", 8))
    )



class OmpPolicyState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("delete", 1))
    )



class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSdwanOmpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSdwanOmpMIBNotifs = _CiscoSdwanOmpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 0)
)
_CiscoSdwanOmpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanOmpMIBObjects = _CiscoSdwanOmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1)
)
_Omp_ObjectIdentity = ObjectIdentity
omp = _Omp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 1)
)
_OmpSummaryTable_ObjectIdentity = ObjectIdentity
ompSummaryTable = _OmpSummaryTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2)
)
_OmpSummary_ObjectIdentity = ObjectIdentity
ompSummary = _OmpSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1)
)


class _OmpSummaryOperstate_Type(Integer32):
    """Custom type ompSummaryOperstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dOWN", 1),
          ("uP", 2))
    )


_OmpSummaryOperstate_Type.__name__ = "Integer32"
_OmpSummaryOperstate_Object = MibScalar
ompSummaryOperstate = _OmpSummaryOperstate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 1),
    _OmpSummaryOperstate_Type()
)
ompSummaryOperstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryOperstate.setStatus("current")


class _OmpSummaryAdminstate_Type(Integer32):
    """Custom type ompSummaryAdminstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dOWN", 1),
          ("uP", 2))
    )


_OmpSummaryAdminstate_Type.__name__ = "Integer32"
_OmpSummaryAdminstate_Object = MibScalar
ompSummaryAdminstate = _OmpSummaryAdminstate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 2),
    _OmpSummaryAdminstate_Type()
)
ompSummaryAdminstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryAdminstate.setStatus("current")


class _OmpSummaryDevicetype_Type(Integer32):
    """Custom type ompSummaryDevicetype based on Integer32"""
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
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_OmpSummaryDevicetype_Type.__name__ = "Integer32"
_OmpSummaryDevicetype_Object = MibScalar
ompSummaryDevicetype = _OmpSummaryDevicetype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 3),
    _OmpSummaryDevicetype_Type()
)
ompSummaryDevicetype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryDevicetype.setStatus("current")
_OmpSummaryOmpuptime_Type = String
_OmpSummaryOmpuptime_Object = MibScalar
ompSummaryOmpuptime = _OmpSummaryOmpuptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 4),
    _OmpSummaryOmpuptime_Type()
)
ompSummaryOmpuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryOmpuptime.setStatus("current")
_OmpSummaryOmpdowntime_Type = String
_OmpSummaryOmpdowntime_Object = MibScalar
ompSummaryOmpdowntime = _OmpSummaryOmpdowntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 5),
    _OmpSummaryOmpdowntime_Type()
)
ompSummaryOmpdowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryOmpdowntime.setStatus("current")
_OmpSummaryRoutesReceived_Type = Unsigned32
_OmpSummaryRoutesReceived_Object = MibScalar
ompSummaryRoutesReceived = _OmpSummaryRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 6),
    _OmpSummaryRoutesReceived_Type()
)
ompSummaryRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryRoutesReceived.setStatus("current")
_OmpSummaryRoutesInstalled_Type = Unsigned32
_OmpSummaryRoutesInstalled_Object = MibScalar
ompSummaryRoutesInstalled = _OmpSummaryRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 7),
    _OmpSummaryRoutesInstalled_Type()
)
ompSummaryRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryRoutesInstalled.setStatus("current")
_OmpSummaryRoutesSent_Type = Unsigned32
_OmpSummaryRoutesSent_Object = MibScalar
ompSummaryRoutesSent = _OmpSummaryRoutesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 8),
    _OmpSummaryRoutesSent_Type()
)
ompSummaryRoutesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryRoutesSent.setStatus("current")
_OmpSummaryTlocsReceived_Type = Unsigned32
_OmpSummaryTlocsReceived_Object = MibScalar
ompSummaryTlocsReceived = _OmpSummaryTlocsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 9),
    _OmpSummaryTlocsReceived_Type()
)
ompSummaryTlocsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryTlocsReceived.setStatus("current")
_OmpSummaryTlocsInstalled_Type = Unsigned32
_OmpSummaryTlocsInstalled_Object = MibScalar
ompSummaryTlocsInstalled = _OmpSummaryTlocsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 10),
    _OmpSummaryTlocsInstalled_Type()
)
ompSummaryTlocsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryTlocsInstalled.setStatus("current")
_OmpSummaryTlocsSent_Type = Unsigned32
_OmpSummaryTlocsSent_Object = MibScalar
ompSummaryTlocsSent = _OmpSummaryTlocsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 11),
    _OmpSummaryTlocsSent_Type()
)
ompSummaryTlocsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryTlocsSent.setStatus("current")
_OmpSummaryServicesReceived_Type = Unsigned32
_OmpSummaryServicesReceived_Object = MibScalar
ompSummaryServicesReceived = _OmpSummaryServicesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 12),
    _OmpSummaryServicesReceived_Type()
)
ompSummaryServicesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryServicesReceived.setStatus("current")
_OmpSummaryServicesInstalled_Type = Unsigned32
_OmpSummaryServicesInstalled_Object = MibScalar
ompSummaryServicesInstalled = _OmpSummaryServicesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 13),
    _OmpSummaryServicesInstalled_Type()
)
ompSummaryServicesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryServicesInstalled.setStatus("current")
_OmpSummaryServicesSent_Type = Unsigned32
_OmpSummaryServicesSent_Object = MibScalar
ompSummaryServicesSent = _OmpSummaryServicesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 14),
    _OmpSummaryServicesSent_Type()
)
ompSummaryServicesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryServicesSent.setStatus("current")
_OmpSummaryMcastRoutesReceived_Type = Unsigned32
_OmpSummaryMcastRoutesReceived_Object = MibScalar
ompSummaryMcastRoutesReceived = _OmpSummaryMcastRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 15),
    _OmpSummaryMcastRoutesReceived_Type()
)
ompSummaryMcastRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMcastRoutesReceived.setStatus("current")
_OmpSummaryMcastRoutesInstalled_Type = Unsigned32
_OmpSummaryMcastRoutesInstalled_Object = MibScalar
ompSummaryMcastRoutesInstalled = _OmpSummaryMcastRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 16),
    _OmpSummaryMcastRoutesInstalled_Type()
)
ompSummaryMcastRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMcastRoutesInstalled.setStatus("current")
_OmpSummaryMcastRoutesSent_Type = Unsigned32
_OmpSummaryMcastRoutesSent_Object = MibScalar
ompSummaryMcastRoutesSent = _OmpSummaryMcastRoutesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 17),
    _OmpSummaryMcastRoutesSent_Type()
)
ompSummaryMcastRoutesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMcastRoutesSent.setStatus("current")
_OmpSummaryHelloReceived_Type = Unsigned32
_OmpSummaryHelloReceived_Object = MibScalar
ompSummaryHelloReceived = _OmpSummaryHelloReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 18),
    _OmpSummaryHelloReceived_Type()
)
ompSummaryHelloReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryHelloReceived.setStatus("current")
_OmpSummaryHelloSent_Type = Unsigned32
_OmpSummaryHelloSent_Object = MibScalar
ompSummaryHelloSent = _OmpSummaryHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 19),
    _OmpSummaryHelloSent_Type()
)
ompSummaryHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryHelloSent.setStatus("current")
_OmpSummaryHandshakeReceived_Type = Unsigned32
_OmpSummaryHandshakeReceived_Object = MibScalar
ompSummaryHandshakeReceived = _OmpSummaryHandshakeReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 20),
    _OmpSummaryHandshakeReceived_Type()
)
ompSummaryHandshakeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryHandshakeReceived.setStatus("current")
_OmpSummaryHandshakeSent_Type = Unsigned32
_OmpSummaryHandshakeSent_Object = MibScalar
ompSummaryHandshakeSent = _OmpSummaryHandshakeSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 21),
    _OmpSummaryHandshakeSent_Type()
)
ompSummaryHandshakeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryHandshakeSent.setStatus("current")
_OmpSummaryAlertReceived_Type = Unsigned32
_OmpSummaryAlertReceived_Object = MibScalar
ompSummaryAlertReceived = _OmpSummaryAlertReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 22),
    _OmpSummaryAlertReceived_Type()
)
ompSummaryAlertReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryAlertReceived.setStatus("current")
_OmpSummaryAlertSent_Type = Unsigned32
_OmpSummaryAlertSent_Object = MibScalar
ompSummaryAlertSent = _OmpSummaryAlertSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 23),
    _OmpSummaryAlertSent_Type()
)
ompSummaryAlertSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryAlertSent.setStatus("current")
_OmpSummaryInformReceived_Type = Unsigned32
_OmpSummaryInformReceived_Object = MibScalar
ompSummaryInformReceived = _OmpSummaryInformReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 24),
    _OmpSummaryInformReceived_Type()
)
ompSummaryInformReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryInformReceived.setStatus("current")
_OmpSummaryInformSent_Type = Unsigned32
_OmpSummaryInformSent_Object = MibScalar
ompSummaryInformSent = _OmpSummaryInformSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 25),
    _OmpSummaryInformSent_Type()
)
ompSummaryInformSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryInformSent.setStatus("current")
_OmpSummaryUpdateReceived_Type = Unsigned32
_OmpSummaryUpdateReceived_Object = MibScalar
ompSummaryUpdateReceived = _OmpSummaryUpdateReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 26),
    _OmpSummaryUpdateReceived_Type()
)
ompSummaryUpdateReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryUpdateReceived.setStatus("current")
_OmpSummaryUpdateSent_Type = Unsigned32
_OmpSummaryUpdateSent_Object = MibScalar
ompSummaryUpdateSent = _OmpSummaryUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 27),
    _OmpSummaryUpdateSent_Type()
)
ompSummaryUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryUpdateSent.setStatus("current")
_OmpSummaryPolicyReceived_Type = Unsigned32
_OmpSummaryPolicyReceived_Object = MibScalar
ompSummaryPolicyReceived = _OmpSummaryPolicyReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 28),
    _OmpSummaryPolicyReceived_Type()
)
ompSummaryPolicyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPolicyReceived.setStatus("current")
_OmpSummaryPolicySent_Type = Unsigned32
_OmpSummaryPolicySent_Object = MibScalar
ompSummaryPolicySent = _OmpSummaryPolicySent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 29),
    _OmpSummaryPolicySent_Type()
)
ompSummaryPolicySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPolicySent.setStatus("current")
_OmpSummaryPacketsReceived_Type = Unsigned32
_OmpSummaryPacketsReceived_Object = MibScalar
ompSummaryPacketsReceived = _OmpSummaryPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 30),
    _OmpSummaryPacketsReceived_Type()
)
ompSummaryPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPacketsReceived.setStatus("current")
_OmpSummaryPacketsSent_Type = Unsigned32
_OmpSummaryPacketsSent_Object = MibScalar
ompSummaryPacketsSent = _OmpSummaryPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 31),
    _OmpSummaryPacketsSent_Type()
)
ompSummaryPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPacketsSent.setStatus("current")
_OmpSummaryVsmartPeers_Type = Unsigned32
_OmpSummaryVsmartPeers_Object = MibScalar
ompSummaryVsmartPeers = _OmpSummaryVsmartPeers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 32),
    _OmpSummaryVsmartPeers_Type()
)
ompSummaryVsmartPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryVsmartPeers.setStatus("current")
_OmpSummarySiteType_Type = String
_OmpSummarySiteType_Object = MibScalar
ompSummarySiteType = _OmpSummarySiteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 1, 33),
    _OmpSummarySiteType_Type()
)
ompSummarySiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummarySiteType.setStatus("current")
_OmpSummaryMtPeersTable_Object = MibTable
ompSummaryMtPeersTable = _OmpSummaryMtPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ompSummaryMtPeersTable.setStatus("current")
_OmpSummaryMtPeersEntry_Object = MibTableRow
ompSummaryMtPeersEntry = _OmpSummaryMtPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1)
)
ompSummaryMtPeersEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersPeer"),
)
if mibBuilder.loadTexts:
    ompSummaryMtPeersEntry.setStatus("current")
_OmpSummaryMtPeersTenantId_Type = UnsignedShort
_OmpSummaryMtPeersTenantId_Object = MibTableColumn
ompSummaryMtPeersTenantId = _OmpSummaryMtPeersTenantId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 1),
    _OmpSummaryMtPeersTenantId_Type()
)
ompSummaryMtPeersTenantId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompSummaryMtPeersTenantId.setStatus("current")
_OmpSummaryMtPeersPeer_Type = InetAddressIP
_OmpSummaryMtPeersPeer_Object = MibTableColumn
ompSummaryMtPeersPeer = _OmpSummaryMtPeersPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 2),
    _OmpSummaryMtPeersPeer_Type()
)
ompSummaryMtPeersPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompSummaryMtPeersPeer.setStatus("current")


class _OmpSummaryMtPeersType_Type(Integer32):
    """Custom type ompSummaryMtPeersType based on Integer32"""
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
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_OmpSummaryMtPeersType_Type.__name__ = "Integer32"
_OmpSummaryMtPeersType_Object = MibTableColumn
ompSummaryMtPeersType = _OmpSummaryMtPeersType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 3),
    _OmpSummaryMtPeersType_Type()
)
ompSummaryMtPeersType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersType.setStatus("current")


class _OmpSummaryMtPeersDomainId_Type(Unsigned32):
    """Custom type ompSummaryMtPeersDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpSummaryMtPeersDomainId_Type.__name__ = "Unsigned32"
_OmpSummaryMtPeersDomainId_Object = MibTableColumn
ompSummaryMtPeersDomainId = _OmpSummaryMtPeersDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 4),
    _OmpSummaryMtPeersDomainId_Type()
)
ompSummaryMtPeersDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersDomainId.setStatus("current")
_OmpSummaryMtPeersSiteId_Type = Unsigned32
_OmpSummaryMtPeersSiteId_Object = MibTableColumn
ompSummaryMtPeersSiteId = _OmpSummaryMtPeersSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 5),
    _OmpSummaryMtPeersSiteId_Type()
)
ompSummaryMtPeersSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersSiteId.setStatus("current")
_OmpSummaryMtPeersRegionId_Type = String
_OmpSummaryMtPeersRegionId_Object = MibTableColumn
ompSummaryMtPeersRegionId = _OmpSummaryMtPeersRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 6),
    _OmpSummaryMtPeersRegionId_Type()
)
ompSummaryMtPeersRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRegionId.setStatus("current")


class _OmpSummaryMtPeersState_Type(Integer32):
    """Custom type ompSummaryMtPeersState based on Integer32"""
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
        *(("invalid", 0),
          ("init", 1),
          ("handshake", 2),
          ("up", 3),
          ("down", 4),
          ("init-in-gr", 5),
          ("down-in-gr", 6),
          ("handshake-in-gr", 7),
          ("up-in-gr", 8))
    )


_OmpSummaryMtPeersState_Type.__name__ = "Integer32"
_OmpSummaryMtPeersState_Object = MibTableColumn
ompSummaryMtPeersState = _OmpSummaryMtPeersState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 7),
    _OmpSummaryMtPeersState_Type()
)
ompSummaryMtPeersState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersState.setStatus("current")
_OmpSummaryMtPeersVersion_Type = UnsignedByte
_OmpSummaryMtPeersVersion_Object = MibTableColumn
ompSummaryMtPeersVersion = _OmpSummaryMtPeersVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 8),
    _OmpSummaryMtPeersVersion_Type()
)
ompSummaryMtPeersVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersVersion.setStatus("current")
_OmpSummaryMtPeersLegit_Type = TruthValue
_OmpSummaryMtPeersLegit_Object = MibTableColumn
ompSummaryMtPeersLegit = _OmpSummaryMtPeersLegit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 9),
    _OmpSummaryMtPeersLegit_Type()
)
ompSummaryMtPeersLegit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersLegit.setStatus("current")
_OmpSummaryMtPeersUpcount_Type = Unsigned32
_OmpSummaryMtPeersUpcount_Object = MibTableColumn
ompSummaryMtPeersUpcount = _OmpSummaryMtPeersUpcount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 10),
    _OmpSummaryMtPeersUpcount_Type()
)
ompSummaryMtPeersUpcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersUpcount.setStatus("current")
_OmpSummaryMtPeersDowncount_Type = Unsigned32
_OmpSummaryMtPeersDowncount_Object = MibTableColumn
ompSummaryMtPeersDowncount = _OmpSummaryMtPeersDowncount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 11),
    _OmpSummaryMtPeersDowncount_Type()
)
ompSummaryMtPeersDowncount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersDowncount.setStatus("current")
_OmpSummaryMtPeersLastuptime_Type = String
_OmpSummaryMtPeersLastuptime_Object = MibTableColumn
ompSummaryMtPeersLastuptime = _OmpSummaryMtPeersLastuptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 12),
    _OmpSummaryMtPeersLastuptime_Type()
)
ompSummaryMtPeersLastuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersLastuptime.setStatus("current")
_OmpSummaryMtPeersLastdowntime_Type = String
_OmpSummaryMtPeersLastdowntime_Object = MibTableColumn
ompSummaryMtPeersLastdowntime = _OmpSummaryMtPeersLastdowntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 13),
    _OmpSummaryMtPeersLastdowntime_Type()
)
ompSummaryMtPeersLastdowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersLastdowntime.setStatus("current")
_OmpSummaryMtPeersUpTime_Type = String
_OmpSummaryMtPeersUpTime_Object = MibTableColumn
ompSummaryMtPeersUpTime = _OmpSummaryMtPeersUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 14),
    _OmpSummaryMtPeersUpTime_Type()
)
ompSummaryMtPeersUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersUpTime.setStatus("current")
_OmpSummaryMtPeersDownTime_Type = String
_OmpSummaryMtPeersDownTime_Object = MibTableColumn
ompSummaryMtPeersDownTime = _OmpSummaryMtPeersDownTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 15),
    _OmpSummaryMtPeersDownTime_Type()
)
ompSummaryMtPeersDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersDownTime.setStatus("current")
_OmpSummaryMtPeersHoldtime_Type = Unsigned32
_OmpSummaryMtPeersHoldtime_Object = MibTableColumn
ompSummaryMtPeersHoldtime = _OmpSummaryMtPeersHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 16),
    _OmpSummaryMtPeersHoldtime_Type()
)
ompSummaryMtPeersHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersHoldtime.setStatus("current")
_OmpSummaryMtPeersSitepolicy_Type = String
_OmpSummaryMtPeersSitepolicy_Object = MibTableColumn
ompSummaryMtPeersSitepolicy = _OmpSummaryMtPeersSitepolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 17),
    _OmpSummaryMtPeersSitepolicy_Type()
)
ompSummaryMtPeersSitepolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersSitepolicy.setStatus("current")
_OmpSummaryMtPeersPolicyin_Type = String
_OmpSummaryMtPeersPolicyin_Object = MibTableColumn
ompSummaryMtPeersPolicyin = _OmpSummaryMtPeersPolicyin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 18),
    _OmpSummaryMtPeersPolicyin_Type()
)
ompSummaryMtPeersPolicyin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersPolicyin.setStatus("current")
_OmpSummaryMtPeersPolicyout_Type = String
_OmpSummaryMtPeersPolicyout_Object = MibTableColumn
ompSummaryMtPeersPolicyout = _OmpSummaryMtPeersPolicyout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 19),
    _OmpSummaryMtPeersPolicyout_Type()
)
ompSummaryMtPeersPolicyout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersPolicyout.setStatus("current")


class _OmpSummaryMtPeersGracefulRestart_Type(Integer32):
    """Custom type ompSummaryMtPeersGracefulRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 0),
          ("not-supported", 1),
          ("in-progress", 2))
    )


_OmpSummaryMtPeersGracefulRestart_Type.__name__ = "Integer32"
_OmpSummaryMtPeersGracefulRestart_Object = MibTableColumn
ompSummaryMtPeersGracefulRestart = _OmpSummaryMtPeersGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 20),
    _OmpSummaryMtPeersGracefulRestart_Type()
)
ompSummaryMtPeersGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersGracefulRestart.setStatus("current")
_OmpSummaryMtPeersGracefulRestartInterval_Type = Unsigned32
_OmpSummaryMtPeersGracefulRestartInterval_Object = MibTableColumn
ompSummaryMtPeersGracefulRestartInterval = _OmpSummaryMtPeersGracefulRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 21),
    _OmpSummaryMtPeersGracefulRestartInterval_Type()
)
ompSummaryMtPeersGracefulRestartInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersGracefulRestartInterval.setStatus("current")
_OmpSummaryMtPeersHelloReceived_Type = Unsigned32
_OmpSummaryMtPeersHelloReceived_Object = MibTableColumn
ompSummaryMtPeersHelloReceived = _OmpSummaryMtPeersHelloReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 22),
    _OmpSummaryMtPeersHelloReceived_Type()
)
ompSummaryMtPeersHelloReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersHelloReceived.setStatus("current")
_OmpSummaryMtPeersHelloSent_Type = Unsigned32
_OmpSummaryMtPeersHelloSent_Object = MibTableColumn
ompSummaryMtPeersHelloSent = _OmpSummaryMtPeersHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 23),
    _OmpSummaryMtPeersHelloSent_Type()
)
ompSummaryMtPeersHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersHelloSent.setStatus("current")
_OmpSummaryMtPeersHandshakeReceived_Type = Unsigned32
_OmpSummaryMtPeersHandshakeReceived_Object = MibTableColumn
ompSummaryMtPeersHandshakeReceived = _OmpSummaryMtPeersHandshakeReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 24),
    _OmpSummaryMtPeersHandshakeReceived_Type()
)
ompSummaryMtPeersHandshakeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersHandshakeReceived.setStatus("current")
_OmpSummaryMtPeersHandshakeSent_Type = Unsigned32
_OmpSummaryMtPeersHandshakeSent_Object = MibTableColumn
ompSummaryMtPeersHandshakeSent = _OmpSummaryMtPeersHandshakeSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 25),
    _OmpSummaryMtPeersHandshakeSent_Type()
)
ompSummaryMtPeersHandshakeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersHandshakeSent.setStatus("current")
_OmpSummaryMtPeersAlertReceived_Type = Unsigned32
_OmpSummaryMtPeersAlertReceived_Object = MibTableColumn
ompSummaryMtPeersAlertReceived = _OmpSummaryMtPeersAlertReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 26),
    _OmpSummaryMtPeersAlertReceived_Type()
)
ompSummaryMtPeersAlertReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersAlertReceived.setStatus("current")
_OmpSummaryMtPeersAlertSent_Type = Unsigned32
_OmpSummaryMtPeersAlertSent_Object = MibTableColumn
ompSummaryMtPeersAlertSent = _OmpSummaryMtPeersAlertSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 27),
    _OmpSummaryMtPeersAlertSent_Type()
)
ompSummaryMtPeersAlertSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersAlertSent.setStatus("current")
_OmpSummaryMtPeersInformReceived_Type = Unsigned32
_OmpSummaryMtPeersInformReceived_Object = MibTableColumn
ompSummaryMtPeersInformReceived = _OmpSummaryMtPeersInformReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 28),
    _OmpSummaryMtPeersInformReceived_Type()
)
ompSummaryMtPeersInformReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersInformReceived.setStatus("current")
_OmpSummaryMtPeersInformSent_Type = Unsigned32
_OmpSummaryMtPeersInformSent_Object = MibTableColumn
ompSummaryMtPeersInformSent = _OmpSummaryMtPeersInformSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 29),
    _OmpSummaryMtPeersInformSent_Type()
)
ompSummaryMtPeersInformSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersInformSent.setStatus("current")
_OmpSummaryMtPeersUpdateReceived_Type = Unsigned32
_OmpSummaryMtPeersUpdateReceived_Object = MibTableColumn
ompSummaryMtPeersUpdateReceived = _OmpSummaryMtPeersUpdateReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 30),
    _OmpSummaryMtPeersUpdateReceived_Type()
)
ompSummaryMtPeersUpdateReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersUpdateReceived.setStatus("current")
_OmpSummaryMtPeersUpdateSent_Type = Unsigned32
_OmpSummaryMtPeersUpdateSent_Object = MibTableColumn
ompSummaryMtPeersUpdateSent = _OmpSummaryMtPeersUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 31),
    _OmpSummaryMtPeersUpdateSent_Type()
)
ompSummaryMtPeersUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersUpdateSent.setStatus("current")
_OmpSummaryMtPeersPolicyReceived_Type = Unsigned32
_OmpSummaryMtPeersPolicyReceived_Object = MibTableColumn
ompSummaryMtPeersPolicyReceived = _OmpSummaryMtPeersPolicyReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 32),
    _OmpSummaryMtPeersPolicyReceived_Type()
)
ompSummaryMtPeersPolicyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersPolicyReceived.setStatus("current")
_OmpSummaryMtPeersPolicySent_Type = Unsigned32
_OmpSummaryMtPeersPolicySent_Object = MibTableColumn
ompSummaryMtPeersPolicySent = _OmpSummaryMtPeersPolicySent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 33),
    _OmpSummaryMtPeersPolicySent_Type()
)
ompSummaryMtPeersPolicySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersPolicySent.setStatus("current")
_OmpSummaryMtPeersPacketsReceived_Type = Unsigned32
_OmpSummaryMtPeersPacketsReceived_Object = MibTableColumn
ompSummaryMtPeersPacketsReceived = _OmpSummaryMtPeersPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 34),
    _OmpSummaryMtPeersPacketsReceived_Type()
)
ompSummaryMtPeersPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersPacketsReceived.setStatus("current")
_OmpSummaryMtPeersPacketsSent_Type = Unsigned32
_OmpSummaryMtPeersPacketsSent_Object = MibTableColumn
ompSummaryMtPeersPacketsSent = _OmpSummaryMtPeersPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 35),
    _OmpSummaryMtPeersPacketsSent_Type()
)
ompSummaryMtPeersPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersPacketsSent.setStatus("current")
_OmpSummaryMtPeersRoutesReceived_Type = Unsigned32
_OmpSummaryMtPeersRoutesReceived_Object = MibTableColumn
ompSummaryMtPeersRoutesReceived = _OmpSummaryMtPeersRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 36),
    _OmpSummaryMtPeersRoutesReceived_Type()
)
ompSummaryMtPeersRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesReceived.setStatus("current")
_OmpSummaryMtPeersRoutesInstalled_Type = Unsigned32
_OmpSummaryMtPeersRoutesInstalled_Object = MibTableColumn
ompSummaryMtPeersRoutesInstalled = _OmpSummaryMtPeersRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 37),
    _OmpSummaryMtPeersRoutesInstalled_Type()
)
ompSummaryMtPeersRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesInstalled.setStatus("current")
_OmpSummaryMtPeersRoutesSent_Type = Unsigned32
_OmpSummaryMtPeersRoutesSent_Object = MibTableColumn
ompSummaryMtPeersRoutesSent = _OmpSummaryMtPeersRoutesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 38),
    _OmpSummaryMtPeersRoutesSent_Type()
)
ompSummaryMtPeersRoutesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesSent.setStatus("current")
_OmpSummaryMtPeersTlocsReceived_Type = Unsigned32
_OmpSummaryMtPeersTlocsReceived_Object = MibTableColumn
ompSummaryMtPeersTlocsReceived = _OmpSummaryMtPeersTlocsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 39),
    _OmpSummaryMtPeersTlocsReceived_Type()
)
ompSummaryMtPeersTlocsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersTlocsReceived.setStatus("current")
_OmpSummaryMtPeersTlocsInstalled_Type = Unsigned32
_OmpSummaryMtPeersTlocsInstalled_Object = MibTableColumn
ompSummaryMtPeersTlocsInstalled = _OmpSummaryMtPeersTlocsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 40),
    _OmpSummaryMtPeersTlocsInstalled_Type()
)
ompSummaryMtPeersTlocsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersTlocsInstalled.setStatus("current")
_OmpSummaryMtPeersTlocsSent_Type = Unsigned32
_OmpSummaryMtPeersTlocsSent_Object = MibTableColumn
ompSummaryMtPeersTlocsSent = _OmpSummaryMtPeersTlocsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 41),
    _OmpSummaryMtPeersTlocsSent_Type()
)
ompSummaryMtPeersTlocsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersTlocsSent.setStatus("current")
_OmpSummaryMtPeersServicesReceived_Type = Unsigned32
_OmpSummaryMtPeersServicesReceived_Object = MibTableColumn
ompSummaryMtPeersServicesReceived = _OmpSummaryMtPeersServicesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 42),
    _OmpSummaryMtPeersServicesReceived_Type()
)
ompSummaryMtPeersServicesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersServicesReceived.setStatus("current")
_OmpSummaryMtPeersServicesInstalled_Type = Unsigned32
_OmpSummaryMtPeersServicesInstalled_Object = MibTableColumn
ompSummaryMtPeersServicesInstalled = _OmpSummaryMtPeersServicesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 43),
    _OmpSummaryMtPeersServicesInstalled_Type()
)
ompSummaryMtPeersServicesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersServicesInstalled.setStatus("current")
_OmpSummaryMtPeersServicesSent_Type = Unsigned32
_OmpSummaryMtPeersServicesSent_Object = MibTableColumn
ompSummaryMtPeersServicesSent = _OmpSummaryMtPeersServicesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 44),
    _OmpSummaryMtPeersServicesSent_Type()
)
ompSummaryMtPeersServicesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersServicesSent.setStatus("current")
_OmpSummaryMtPeersMcastRoutesReceived_Type = Unsigned32
_OmpSummaryMtPeersMcastRoutesReceived_Object = MibTableColumn
ompSummaryMtPeersMcastRoutesReceived = _OmpSummaryMtPeersMcastRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 45),
    _OmpSummaryMtPeersMcastRoutesReceived_Type()
)
ompSummaryMtPeersMcastRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersMcastRoutesReceived.setStatus("current")
_OmpSummaryMtPeersMcastRoutesInstalled_Type = Unsigned32
_OmpSummaryMtPeersMcastRoutesInstalled_Object = MibTableColumn
ompSummaryMtPeersMcastRoutesInstalled = _OmpSummaryMtPeersMcastRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 46),
    _OmpSummaryMtPeersMcastRoutesInstalled_Type()
)
ompSummaryMtPeersMcastRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersMcastRoutesInstalled.setStatus("current")
_OmpSummaryMtPeersMcastRoutesSent_Type = Unsigned32
_OmpSummaryMtPeersMcastRoutesSent_Object = MibTableColumn
ompSummaryMtPeersMcastRoutesSent = _OmpSummaryMtPeersMcastRoutesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 47),
    _OmpSummaryMtPeersMcastRoutesSent_Type()
)
ompSummaryMtPeersMcastRoutesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersMcastRoutesSent.setStatus("current")
_OmpSummaryMtPeersControlUp_Type = TruthValue
_OmpSummaryMtPeersControlUp_Object = MibTableColumn
ompSummaryMtPeersControlUp = _OmpSummaryMtPeersControlUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 48),
    _OmpSummaryMtPeersControlUp_Type()
)
ompSummaryMtPeersControlUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersControlUp.setStatus("current")
_OmpSummaryMtPeersStaging_Type = TruthValue
_OmpSummaryMtPeersStaging_Object = MibTableColumn
ompSummaryMtPeersStaging = _OmpSummaryMtPeersStaging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 49),
    _OmpSummaryMtPeersStaging_Type()
)
ompSummaryMtPeersStaging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersStaging.setStatus("current")


class _OmpSummaryMtPeersRefresh_Type(Integer32):
    """Custom type ompSummaryMtPeersRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("supported", 0),
          ("not-supported", 1))
    )


_OmpSummaryMtPeersRefresh_Type.__name__ = "Integer32"
_OmpSummaryMtPeersRefresh_Object = MibTableColumn
ompSummaryMtPeersRefresh = _OmpSummaryMtPeersRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 50),
    _OmpSummaryMtPeersRefresh_Type()
)
ompSummaryMtPeersRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRefresh.setStatus("current")
_OmpSummaryMtPeersOverlayId_Type = Unsigned32
_OmpSummaryMtPeersOverlayId_Object = MibTableColumn
ompSummaryMtPeersOverlayId = _OmpSummaryMtPeersOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 51),
    _OmpSummaryMtPeersOverlayId_Type()
)
ompSummaryMtPeersOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersOverlayId.setStatus("current")
_OmpSummaryMtPeersRoutesReceivedIPv6_Type = Unsigned32
_OmpSummaryMtPeersRoutesReceivedIPv6_Object = MibTableColumn
ompSummaryMtPeersRoutesReceivedIPv6 = _OmpSummaryMtPeersRoutesReceivedIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 52),
    _OmpSummaryMtPeersRoutesReceivedIPv6_Type()
)
ompSummaryMtPeersRoutesReceivedIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesReceivedIPv6.setStatus("current")
_OmpSummaryMtPeersRoutesInstalledIPv6_Type = Unsigned32
_OmpSummaryMtPeersRoutesInstalledIPv6_Object = MibTableColumn
ompSummaryMtPeersRoutesInstalledIPv6 = _OmpSummaryMtPeersRoutesInstalledIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 53),
    _OmpSummaryMtPeersRoutesInstalledIPv6_Type()
)
ompSummaryMtPeersRoutesInstalledIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesInstalledIPv6.setStatus("current")
_OmpSummaryMtPeersRoutesSentIPv6_Type = Unsigned32
_OmpSummaryMtPeersRoutesSentIPv6_Object = MibTableColumn
ompSummaryMtPeersRoutesSentIPv6 = _OmpSummaryMtPeersRoutesSentIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 54),
    _OmpSummaryMtPeersRoutesSentIPv6_Type()
)
ompSummaryMtPeersRoutesSentIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesSentIPv6.setStatus("current")
_OmpSummaryMtPeersRoutesReceivedTotal_Type = Unsigned32
_OmpSummaryMtPeersRoutesReceivedTotal_Object = MibTableColumn
ompSummaryMtPeersRoutesReceivedTotal = _OmpSummaryMtPeersRoutesReceivedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 55),
    _OmpSummaryMtPeersRoutesReceivedTotal_Type()
)
ompSummaryMtPeersRoutesReceivedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesReceivedTotal.setStatus("current")
_OmpSummaryMtPeersRoutesInstalledTotal_Type = Unsigned32
_OmpSummaryMtPeersRoutesInstalledTotal_Object = MibTableColumn
ompSummaryMtPeersRoutesInstalledTotal = _OmpSummaryMtPeersRoutesInstalledTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 56),
    _OmpSummaryMtPeersRoutesInstalledTotal_Type()
)
ompSummaryMtPeersRoutesInstalledTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesInstalledTotal.setStatus("current")
_OmpSummaryMtPeersRoutesSentTotal_Type = Unsigned32
_OmpSummaryMtPeersRoutesSentTotal_Object = MibTableColumn
ompSummaryMtPeersRoutesSentTotal = _OmpSummaryMtPeersRoutesSentTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 57),
    _OmpSummaryMtPeersRoutesSentTotal_Type()
)
ompSummaryMtPeersRoutesSentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersRoutesSentTotal.setStatus("current")
_OmpSummaryMtPeersServicesReceivedIPv6_Type = Unsigned32
_OmpSummaryMtPeersServicesReceivedIPv6_Object = MibTableColumn
ompSummaryMtPeersServicesReceivedIPv6 = _OmpSummaryMtPeersServicesReceivedIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 58),
    _OmpSummaryMtPeersServicesReceivedIPv6_Type()
)
ompSummaryMtPeersServicesReceivedIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersServicesReceivedIPv6.setStatus("current")
_OmpSummaryMtPeersServicesInstalledIPv6_Type = Unsigned32
_OmpSummaryMtPeersServicesInstalledIPv6_Object = MibTableColumn
ompSummaryMtPeersServicesInstalledIPv6 = _OmpSummaryMtPeersServicesInstalledIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 59),
    _OmpSummaryMtPeersServicesInstalledIPv6_Type()
)
ompSummaryMtPeersServicesInstalledIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersServicesInstalledIPv6.setStatus("current")
_OmpSummaryMtPeersServicesSentIPv6_Type = Unsigned32
_OmpSummaryMtPeersServicesSentIPv6_Object = MibTableColumn
ompSummaryMtPeersServicesSentIPv6 = _OmpSummaryMtPeersServicesSentIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 2, 2, 1, 60),
    _OmpSummaryMtPeersServicesSentIPv6_Type()
)
ompSummaryMtPeersServicesSentIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMtPeersServicesSentIPv6.setStatus("current")
_OmpRoutesTable_ObjectIdentity = ObjectIdentity
ompRoutesTable = _OmpRoutesTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3)
)
_OmpRoutesTableFamilyTable_Object = MibTable
ompRoutesTableFamilyTable = _OmpRoutesTableFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyTable.setStatus("current")
_OmpRoutesTableFamilyEntry_Object = MibTableRow
ompRoutesTableFamilyEntry = _OmpRoutesTableFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 1, 1)
)
ompRoutesTableFamilyEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntry.setStatus("current")
_OmpRoutesTableFamilyAddressFamily_Type = AddrFamilyEnum
_OmpRoutesTableFamilyAddressFamily_Object = MibTableColumn
ompRoutesTableFamilyAddressFamily = _OmpRoutesTableFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 1, 1, 1),
    _OmpRoutesTableFamilyAddressFamily_Type()
)
ompRoutesTableFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyAddressFamily.setStatus("current")
_OmpRoutesTableFamilyEntriesTable_Object = MibTable
ompRoutesTableFamilyEntriesTable = _OmpRoutesTableFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesTable.setStatus("current")
_OmpRoutesTableFamilyEntriesEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesEntry = _OmpRoutesTableFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 2, 1)
)
ompRoutesTableFamilyEntriesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesPrefix"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesTenantId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesTenantId_Object = MibTableColumn
ompRoutesTableFamilyEntriesTenantId = _OmpRoutesTableFamilyEntriesTenantId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 2, 1, 1),
    _OmpRoutesTableFamilyEntriesTenantId_Type()
)
ompRoutesTableFamilyEntriesTenantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesTenantId.setStatus("current")


class _OmpRoutesTableFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompRoutesTableFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpRoutesTableFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpRoutesTableFamilyEntriesVpnId_Object = MibTableColumn
ompRoutesTableFamilyEntriesVpnId = _OmpRoutesTableFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 2, 1, 2),
    _OmpRoutesTableFamilyEntriesVpnId_Type()
)
ompRoutesTableFamilyEntriesVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesVpnId.setStatus("current")
_OmpRoutesTableFamilyEntriesPrefix_Type = IpPrefix
_OmpRoutesTableFamilyEntriesPrefix_Object = MibTableColumn
ompRoutesTableFamilyEntriesPrefix = _OmpRoutesTableFamilyEntriesPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 2, 1, 3),
    _OmpRoutesTableFamilyEntriesPrefix_Type()
)
ompRoutesTableFamilyEntriesPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesPrefix.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedTable_Object = MibTable
ompRoutesTableFamilyEntriesReceivedTable = _OmpRoutesTableFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedTable.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesReceivedEntry = _OmpRoutesTableFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3, 1)
)
ompRoutesTableFamilyEntriesReceivedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedFromPeer"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedPathId"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedFromPeer = _OmpRoutesTableFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3, 1, 1),
    _OmpRoutesTableFamilyEntriesReceivedFromPeer_Type()
)
ompRoutesTableFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedPathId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedPathId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedPathId = _OmpRoutesTableFamilyEntriesReceivedPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3, 1, 2),
    _OmpRoutesTableFamilyEntriesReceivedPathId_Type()
)
ompRoutesTableFamilyEntriesReceivedPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedPathId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedLabel_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedLabel_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedLabel = _OmpRoutesTableFamilyEntriesReceivedLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3, 1, 3),
    _OmpRoutesTableFamilyEntriesReceivedLabel_Type()
)
ompRoutesTableFamilyEntriesReceivedLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedLabel.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpRoutesTableFamilyEntriesReceivedStatus_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedStatus = _OmpRoutesTableFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3, 1, 4),
    _OmpRoutesTableFamilyEntriesReceivedStatus_Type()
)
ompRoutesTableFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedStatus.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpRoutesTableFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedLossReason = _OmpRoutesTableFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3, 1, 5),
    _OmpRoutesTableFamilyEntriesReceivedLossReason_Type()
)
ompRoutesTableFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedLossReason.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedLostToPeer_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedLostToPeer_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedLostToPeer = _OmpRoutesTableFamilyEntriesReceivedLostToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3, 1, 6),
    _OmpRoutesTableFamilyEntriesReceivedLostToPeer_Type()
)
ompRoutesTableFamilyEntriesReceivedLostToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedLostToPeer.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedLostToPathId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedLostToPathId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedLostToPathId = _OmpRoutesTableFamilyEntriesReceivedLostToPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 3, 1, 7),
    _OmpRoutesTableFamilyEntriesReceivedLostToPathId_Type()
)
ompRoutesTableFamilyEntriesReceivedLostToPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedLostToPathId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesTable_Object = MibTable
ompRoutesTableFamilyEntriesReceivedAttributesTable = _OmpRoutesTableFamilyEntriesReceivedAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTable.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesReceivedAttributesEntry = _OmpRoutesTableFamilyEntriesReceivedAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1)
)
ompRoutesTableFamilyEntriesReceivedAttributesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedFromPeer"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedPathId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesAttributeType"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesAttributeType_Type = AttributeTypeEnum
_OmpRoutesTableFamilyEntriesReceivedAttributesAttributeType_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesAttributeType = _OmpRoutesTableFamilyEntriesReceivedAttributesAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 1),
    _OmpRoutesTableFamilyEntriesReceivedAttributesAttributeType_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesAttributeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesAttributeType.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocIp_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocIp_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesTlocIp = _OmpRoutesTableFamilyEntriesReceivedAttributesTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 2),
    _OmpRoutesTableFamilyEntriesReceivedAttributesTlocIp_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTlocIp.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Type = TlocColorEnum
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesTlocColor = _OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 3),
    _OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTlocColor.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Type = TlocEncapEnum
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap = _OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 4),
    _OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Type = ProtocolEnum
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol = _OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 5),
    _OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginMetric_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginMetric_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric = _OmpRoutesTableFamilyEntriesReceivedAttributesOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 6),
    _OmpRoutesTableFamilyEntriesReceivedAttributesOriginMetric_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric.setStatus("current")


class _OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Type(Unsigned32):
    """Custom type ompRoutesTableFamilyEntriesReceivedAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesDomainId = _OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 7),
    _OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesDomainId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesSiteId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesSiteId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesSiteId = _OmpRoutesTableFamilyEntriesReceivedAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 8),
    _OmpRoutesTableFamilyEntriesReceivedAttributesSiteId_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesSiteId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesPreference_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesPreference_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesPreference = _OmpRoutesTableFamilyEntriesReceivedAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 9),
    _OmpRoutesTableFamilyEntriesReceivedAttributesPreference_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesPreference.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesTag_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesTag_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesTag = _OmpRoutesTableFamilyEntriesReceivedAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 10),
    _OmpRoutesTableFamilyEntriesReceivedAttributesTag_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTag.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen_Type = UnsignedShort
_OmpRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen = _OmpRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 11),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginator_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginator_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesOriginator = _OmpRoutesTableFamilyEntriesReceivedAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 12),
    _OmpRoutesTableFamilyEntriesReceivedAttributesOriginator_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesOriginator.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp = _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 13),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Type = TlocColorEnum
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor = _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 14),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Type = TlocEncapEnum
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap = _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 15),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Type = TlocActionEnum
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction = _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 16),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesOverlayId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesOverlayId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesOverlayId = _OmpRoutesTableFamilyEntriesReceivedAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 17),
    _OmpRoutesTableFamilyEntriesReceivedAttributesOverlayId_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesOverlayId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesAsPath_Type = String
_OmpRoutesTableFamilyEntriesReceivedAttributesAsPath_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesAsPath = _OmpRoutesTableFamilyEntriesReceivedAttributesAsPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 18),
    _OmpRoutesTableFamilyEntriesReceivedAttributesAsPath_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesAsPath.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesCommunity_Type = String
_OmpRoutesTableFamilyEntriesReceivedAttributesCommunity_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesCommunity = _OmpRoutesTableFamilyEntriesReceivedAttributesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 19),
    _OmpRoutesTableFamilyEntriesReceivedAttributesCommunity_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesCommunity.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesRegionId_Type = String
_OmpRoutesTableFamilyEntriesReceivedAttributesRegionId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesRegionId = _OmpRoutesTableFamilyEntriesReceivedAttributesRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 20),
    _OmpRoutesTableFamilyEntriesReceivedAttributesRegionId_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesRegionId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesRegionPath_Type = String
_OmpRoutesTableFamilyEntriesReceivedAttributesRegionPath_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesRegionPath = _OmpRoutesTableFamilyEntriesReceivedAttributesRegionPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 21),
    _OmpRoutesTableFamilyEntriesReceivedAttributesRegionPath_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesRegionPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesRegionPath.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesSiteType_Type = String
_OmpRoutesTableFamilyEntriesReceivedAttributesSiteType_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesSiteType = _OmpRoutesTableFamilyEntriesReceivedAttributesSiteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 4, 1, 22),
    _OmpRoutesTableFamilyEntriesReceivedAttributesSiteType_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesSiteType.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedTable_Object = MibTable
ompRoutesTableFamilyEntriesAdvertisedTable = _OmpRoutesTableFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedTable.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesAdvertisedEntry = _OmpRoutesTableFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 5, 1)
)
ompRoutesTableFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedToPeer = _OmpRoutesTableFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 5, 1, 1),
    _OmpRoutesTableFamilyEntriesAdvertisedToPeer_Type()
)
ompRoutesTableFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsTable_Object = MibTable
ompRoutesTableFamilyEntriesAdvertisedPathsTable = _OmpRoutesTableFamilyEntriesAdvertisedPathsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 6)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsTable.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesAdvertisedPathsEntry = _OmpRoutesTableFamilyEntriesAdvertisedPathsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 6, 1)
)
ompRoutesTableFamilyEntriesAdvertisedPathsEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedToPeer"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 6, 1, 1),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTable_Object = MibTable
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTable = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTable.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1)
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedToPeer"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 1),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 2),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 3),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Type = TlocColorEnum
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 4),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Type = TlocEncapEnum
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 5),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Type = ProtocolEnum
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 6),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 7),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric.setStatus("current")


class _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Type(Unsigned32):
    """Custom type ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 8),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 9),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 10),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTag_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTag_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 11),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTag_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Type = UnsignedShort
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 12),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 13),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 14),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Type = TlocColorEnum
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 15),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Type = TlocEncapEnum
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 16),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Type = TlocActionEnum
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 17),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 18),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath_Type = String
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 19),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity_Type = String
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 20),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId_Type = String
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 21),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath_Type = String
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 22),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType_Type = String
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 3, 7, 1, 23),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType.setStatus("current")
_OmpBestMatchRoute_ObjectIdentity = ObjectIdentity
ompBestMatchRoute = _OmpBestMatchRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 4)
)
_OmpTlocPaths_ObjectIdentity = ObjectIdentity
ompTlocPaths = _OmpTlocPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5)
)
_OmpTlocPathsEntriesTable_Object = MibTable
ompTlocPathsEntriesTable = _OmpTlocPathsEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesTable.setStatus("current")
_OmpTlocPathsEntriesEntry_Object = MibTableRow
ompTlocPathsEntriesEntry = _OmpTlocPathsEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 1, 1)
)
ompTlocPathsEntriesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesIp"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesColor"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesEncap"),
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesEntry.setStatus("current")
_OmpTlocPathsEntriesIp_Type = InetAddressIP
_OmpTlocPathsEntriesIp_Object = MibTableColumn
ompTlocPathsEntriesIp = _OmpTlocPathsEntriesIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 1, 1, 1),
    _OmpTlocPathsEntriesIp_Type()
)
ompTlocPathsEntriesIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesIp.setStatus("current")
_OmpTlocPathsEntriesColor_Type = TlocColorEnum
_OmpTlocPathsEntriesColor_Object = MibTableColumn
ompTlocPathsEntriesColor = _OmpTlocPathsEntriesColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 1, 1, 2),
    _OmpTlocPathsEntriesColor_Type()
)
ompTlocPathsEntriesColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesColor.setStatus("current")
_OmpTlocPathsEntriesEncap_Type = TlocEncapEnum
_OmpTlocPathsEntriesEncap_Object = MibTableColumn
ompTlocPathsEntriesEncap = _OmpTlocPathsEntriesEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 1, 1, 3),
    _OmpTlocPathsEntriesEncap_Type()
)
ompTlocPathsEntriesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesEncap.setStatus("current")
_OmpTlocPathsEntriesPathsTable_Object = MibTable
ompTlocPathsEntriesPathsTable = _OmpTlocPathsEntriesPathsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsTable.setStatus("current")
_OmpTlocPathsEntriesPathsEntry_Object = MibTableRow
ompTlocPathsEntriesPathsEntry = _OmpTlocPathsEntriesPathsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 2, 1)
)
ompTlocPathsEntriesPathsEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesIp"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesColor"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesEncap"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsIndex"),
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsEntry.setStatus("current")
_OmpTlocPathsEntriesPathsIndex_Type = Unsigned32
_OmpTlocPathsEntriesPathsIndex_Object = MibTableColumn
ompTlocPathsEntriesPathsIndex = _OmpTlocPathsEntriesPathsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 2, 1, 1),
    _OmpTlocPathsEntriesPathsIndex_Type()
)
ompTlocPathsEntriesPathsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsIndex.setStatus("current")
_OmpTlocPathsEntriesPathsPreference_Type = Unsigned32
_OmpTlocPathsEntriesPathsPreference_Object = MibTableColumn
ompTlocPathsEntriesPathsPreference = _OmpTlocPathsEntriesPathsPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 2, 1, 2),
    _OmpTlocPathsEntriesPathsPreference_Type()
)
ompTlocPathsEntriesPathsPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsPreference.setStatus("current")
_OmpTlocPathsEntriesPathsMtu_Type = Unsigned32
_OmpTlocPathsEntriesPathsMtu_Object = MibTableColumn
ompTlocPathsEntriesPathsMtu = _OmpTlocPathsEntriesPathsMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 2, 1, 3),
    _OmpTlocPathsEntriesPathsMtu_Type()
)
ompTlocPathsEntriesPathsMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsMtu.setStatus("current")
_OmpTlocPathsEntriesPathsBfdStatus_Type = BfdStatusEnum
_OmpTlocPathsEntriesPathsBfdStatus_Object = MibTableColumn
ompTlocPathsEntriesPathsBfdStatus = _OmpTlocPathsEntriesPathsBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 2, 1, 4),
    _OmpTlocPathsEntriesPathsBfdStatus_Type()
)
ompTlocPathsEntriesPathsBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsBfdStatus.setStatus("current")
_OmpTlocPathsEntriesPathsStatus_Type = PathStatusEnum
_OmpTlocPathsEntriesPathsStatus_Object = MibTableColumn
ompTlocPathsEntriesPathsStatus = _OmpTlocPathsEntriesPathsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 2, 1, 6),
    _OmpTlocPathsEntriesPathsStatus_Type()
)
ompTlocPathsEntriesPathsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsStatus.setStatus("current")
_OmpTlocPathsEntriesPathsStale_Type = TruthValue
_OmpTlocPathsEntriesPathsStale_Object = MibTableColumn
ompTlocPathsEntriesPathsStale = _OmpTlocPathsEntriesPathsStale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 2, 1, 7),
    _OmpTlocPathsEntriesPathsStale_Type()
)
ompTlocPathsEntriesPathsStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsStale.setStatus("current")
_OmpTlocPathsEntriesPathsLinksTable_Object = MibTable
ompTlocPathsEntriesPathsLinksTable = _OmpTlocPathsEntriesPathsLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksTable.setStatus("current")
_OmpTlocPathsEntriesPathsLinksEntry_Object = MibTableRow
ompTlocPathsEntriesPathsLinksEntry = _OmpTlocPathsEntriesPathsLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1)
)
ompTlocPathsEntriesPathsLinksEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesIp"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesColor"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesEncap"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsIndex"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsLinksLinkIndex"),
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksEntry.setStatus("current")
_OmpTlocPathsEntriesPathsLinksLinkIndex_Type = Unsigned32
_OmpTlocPathsEntriesPathsLinksLinkIndex_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksLinkIndex = _OmpTlocPathsEntriesPathsLinksLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1, 1),
    _OmpTlocPathsEntriesPathsLinksLinkIndex_Type()
)
ompTlocPathsEntriesPathsLinksLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksLinkIndex.setStatus("current")
_OmpTlocPathsEntriesPathsLinksFromTlocIp_Type = InetAddressIP
_OmpTlocPathsEntriesPathsLinksFromTlocIp_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksFromTlocIp = _OmpTlocPathsEntriesPathsLinksFromTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1, 2),
    _OmpTlocPathsEntriesPathsLinksFromTlocIp_Type()
)
ompTlocPathsEntriesPathsLinksFromTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksFromTlocIp.setStatus("current")
_OmpTlocPathsEntriesPathsLinksFromTlocColor_Type = TlocColorEnum
_OmpTlocPathsEntriesPathsLinksFromTlocColor_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksFromTlocColor = _OmpTlocPathsEntriesPathsLinksFromTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1, 3),
    _OmpTlocPathsEntriesPathsLinksFromTlocColor_Type()
)
ompTlocPathsEntriesPathsLinksFromTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksFromTlocColor.setStatus("current")
_OmpTlocPathsEntriesPathsLinksFromTlocEncap_Type = TlocEncapEnum
_OmpTlocPathsEntriesPathsLinksFromTlocEncap_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksFromTlocEncap = _OmpTlocPathsEntriesPathsLinksFromTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1, 4),
    _OmpTlocPathsEntriesPathsLinksFromTlocEncap_Type()
)
ompTlocPathsEntriesPathsLinksFromTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksFromTlocEncap.setStatus("current")
_OmpTlocPathsEntriesPathsLinksToTlocIp_Type = InetAddressIP
_OmpTlocPathsEntriesPathsLinksToTlocIp_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksToTlocIp = _OmpTlocPathsEntriesPathsLinksToTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1, 5),
    _OmpTlocPathsEntriesPathsLinksToTlocIp_Type()
)
ompTlocPathsEntriesPathsLinksToTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksToTlocIp.setStatus("current")
_OmpTlocPathsEntriesPathsLinksToTlocColor_Type = TlocColorEnum
_OmpTlocPathsEntriesPathsLinksToTlocColor_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksToTlocColor = _OmpTlocPathsEntriesPathsLinksToTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1, 6),
    _OmpTlocPathsEntriesPathsLinksToTlocColor_Type()
)
ompTlocPathsEntriesPathsLinksToTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksToTlocColor.setStatus("current")
_OmpTlocPathsEntriesPathsLinksToTlocEncap_Type = TlocEncapEnum
_OmpTlocPathsEntriesPathsLinksToTlocEncap_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksToTlocEncap = _OmpTlocPathsEntriesPathsLinksToTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1, 7),
    _OmpTlocPathsEntriesPathsLinksToTlocEncap_Type()
)
ompTlocPathsEntriesPathsLinksToTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksToTlocEncap.setStatus("current")
_OmpTlocPathsEntriesPathsLinksLabel_Type = Unsigned32
_OmpTlocPathsEntriesPathsLinksLabel_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksLabel = _OmpTlocPathsEntriesPathsLinksLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 5, 3, 1, 8),
    _OmpTlocPathsEntriesPathsLinksLabel_Type()
)
ompTlocPathsEntriesPathsLinksLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksLabel.setStatus("current")
_OmpTlocs_ObjectIdentity = ObjectIdentity
ompTlocs = _OmpTlocs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6)
)
_OmpTlocsFamilyTable_Object = MibTable
ompTlocsFamilyTable = _OmpTlocsFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyTable.setStatus("current")
_OmpTlocsFamilyEntry_Object = MibTableRow
ompTlocsFamilyEntry = _OmpTlocsFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 1, 1)
)
ompTlocsFamilyEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntry.setStatus("current")
_OmpTlocsFamilyAddressFamily_Type = AddrFamilyEnum
_OmpTlocsFamilyAddressFamily_Object = MibTableColumn
ompTlocsFamilyAddressFamily = _OmpTlocsFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 1, 1, 1),
    _OmpTlocsFamilyAddressFamily_Type()
)
ompTlocsFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyAddressFamily.setStatus("current")
_OmpTlocsFamilyEntriesTable_Object = MibTable
ompTlocsFamilyEntriesTable = _OmpTlocsFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesTable.setStatus("current")
_OmpTlocsFamilyEntriesEntry_Object = MibTableRow
ompTlocsFamilyEntriesEntry = _OmpTlocsFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 2, 1)
)
ompTlocsFamilyEntriesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesIp"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesColor"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesEncap"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesEntry.setStatus("current")
_OmpTlocsFamilyEntriesIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesIp_Object = MibTableColumn
ompTlocsFamilyEntriesIp = _OmpTlocsFamilyEntriesIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 2, 1, 1),
    _OmpTlocsFamilyEntriesIp_Type()
)
ompTlocsFamilyEntriesIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesIp.setStatus("current")
_OmpTlocsFamilyEntriesColor_Type = TlocColorEnum
_OmpTlocsFamilyEntriesColor_Object = MibTableColumn
ompTlocsFamilyEntriesColor = _OmpTlocsFamilyEntriesColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 2, 1, 2),
    _OmpTlocsFamilyEntriesColor_Type()
)
ompTlocsFamilyEntriesColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesColor.setStatus("current")
_OmpTlocsFamilyEntriesEncap_Type = TlocEncapEnum
_OmpTlocsFamilyEntriesEncap_Object = MibTableColumn
ompTlocsFamilyEntriesEncap = _OmpTlocsFamilyEntriesEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 2, 1, 3),
    _OmpTlocsFamilyEntriesEncap_Type()
)
ompTlocsFamilyEntriesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesEncap.setStatus("current")
_OmpTlocsFamilyEntriesReceivedTable_Object = MibTable
ompTlocsFamilyEntriesReceivedTable = _OmpTlocsFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 5)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedTable.setStatus("current")
_OmpTlocsFamilyEntriesReceivedEntry_Object = MibTableRow
ompTlocsFamilyEntriesReceivedEntry = _OmpTlocsFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 5, 1)
)
ompTlocsFamilyEntriesReceivedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesIp"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesColor"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesEncap"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedFromPeer"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedEntry.setStatus("current")
_OmpTlocsFamilyEntriesReceivedTenantId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedTenantId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedTenantId = _OmpTlocsFamilyEntriesReceivedTenantId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 5, 1, 1),
    _OmpTlocsFamilyEntriesReceivedTenantId_Type()
)
ompTlocsFamilyEntriesReceivedTenantId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedTenantId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedFromPeer = _OmpTlocsFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 5, 1, 2),
    _OmpTlocsFamilyEntriesReceivedFromPeer_Type()
)
ompTlocsFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpTlocsFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpTlocsFamilyEntriesReceivedStatus_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedStatus = _OmpTlocsFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 5, 1, 3),
    _OmpTlocsFamilyEntriesReceivedStatus_Type()
)
ompTlocsFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedStatus.setStatus("current")
_OmpTlocsFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpTlocsFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedLossReason = _OmpTlocsFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 5, 1, 4),
    _OmpTlocsFamilyEntriesReceivedLossReason_Type()
)
ompTlocsFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedLossReason.setStatus("current")
_OmpTlocsFamilyEntriesReceivedLostToPeer_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedLostToPeer_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedLostToPeer = _OmpTlocsFamilyEntriesReceivedLostToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 5, 1, 5),
    _OmpTlocsFamilyEntriesReceivedLostToPeer_Type()
)
ompTlocsFamilyEntriesReceivedLostToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedLostToPeer.setStatus("current")
_OmpTlocsFamilyEntriesReceivedLostToPathId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedLostToPathId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedLostToPathId = _OmpTlocsFamilyEntriesReceivedLostToPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 5, 1, 6),
    _OmpTlocsFamilyEntriesReceivedLostToPathId_Type()
)
ompTlocsFamilyEntriesReceivedLostToPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedLostToPathId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTable_Object = MibTable
ompTlocsFamilyEntriesReceivedAttributesTable = _OmpTlocsFamilyEntriesReceivedAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTable.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesEntry_Object = MibTableRow
ompTlocsFamilyEntriesReceivedAttributesEntry = _OmpTlocsFamilyEntriesReceivedAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1)
)
ompTlocsFamilyEntriesReceivedAttributesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesIp"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesColor"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesEncap"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedFromPeer"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesPseudoKey"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesEntry.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesPseudoKey_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesPseudoKey_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesPseudoKey = _OmpTlocsFamilyEntriesReceivedAttributesPseudoKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 1),
    _OmpTlocsFamilyEntriesReceivedAttributesPseudoKey_Type()
)
ompTlocsFamilyEntriesReceivedAttributesPseudoKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesPseudoKey.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesAttributeType_Type = AttributeTypeEnum
_OmpTlocsFamilyEntriesReceivedAttributesAttributeType_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesAttributeType = _OmpTlocsFamilyEntriesReceivedAttributesAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 2),
    _OmpTlocsFamilyEntriesReceivedAttributesAttributeType_Type()
)
ompTlocsFamilyEntriesReceivedAttributesAttributeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesAttributeType.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapKey_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapKey_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 3),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapKey_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapProto_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapProto_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 4),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapProto_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapSpi_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapSpi_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapSpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 5),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapSpi_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Type = EncryptType
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 6),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType_Type = IntegType
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 7),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 8),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 9),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 10),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 11),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 12),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 13),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 14),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 15),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesBfdStatus_Type = BfdStatusEnum
_OmpTlocsFamilyEntriesReceivedAttributesBfdStatus_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesBfdStatus = _OmpTlocsFamilyEntriesReceivedAttributesBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 16),
    _OmpTlocsFamilyEntriesReceivedAttributesBfdStatus_Type()
)
ompTlocsFamilyEntriesReceivedAttributesBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesBfdStatus.setStatus("current")


class _OmpTlocsFamilyEntriesReceivedAttributesDomainId_Type(Unsigned32):
    """Custom type ompTlocsFamilyEntriesReceivedAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpTlocsFamilyEntriesReceivedAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpTlocsFamilyEntriesReceivedAttributesDomainId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesDomainId = _OmpTlocsFamilyEntriesReceivedAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 17),
    _OmpTlocsFamilyEntriesReceivedAttributesDomainId_Type()
)
ompTlocsFamilyEntriesReceivedAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesDomainId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesSiteId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesSiteId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesSiteId = _OmpTlocsFamilyEntriesReceivedAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 18),
    _OmpTlocsFamilyEntriesReceivedAttributesSiteId_Type()
)
ompTlocsFamilyEntriesReceivedAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesSiteId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesPreference_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesPreference_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesPreference = _OmpTlocsFamilyEntriesReceivedAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 19),
    _OmpTlocsFamilyEntriesReceivedAttributesPreference_Type()
)
ompTlocsFamilyEntriesReceivedAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesPreference.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTag_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesTag_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTag = _OmpTlocsFamilyEntriesReceivedAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 20),
    _OmpTlocsFamilyEntriesReceivedAttributesTag_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTag.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesStale_Type = UnsignedByte
_OmpTlocsFamilyEntriesReceivedAttributesStale_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesStale = _OmpTlocsFamilyEntriesReceivedAttributesStale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 21),
    _OmpTlocsFamilyEntriesReceivedAttributesStale_Type()
)
ompTlocsFamilyEntriesReceivedAttributesStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesStale.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesCarrier_Type = CarrierEnum
_OmpTlocsFamilyEntriesReceivedAttributesCarrier_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesCarrier = _OmpTlocsFamilyEntriesReceivedAttributesCarrier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 22),
    _OmpTlocsFamilyEntriesReceivedAttributesCarrier_Type()
)
ompTlocsFamilyEntriesReceivedAttributesCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesCarrier.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesGroups_Type = Groups1
_OmpTlocsFamilyEntriesReceivedAttributesGroups_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesGroups = _OmpTlocsFamilyEntriesReceivedAttributesGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 23),
    _OmpTlocsFamilyEntriesReceivedAttributesGroups_Type()
)
ompTlocsFamilyEntriesReceivedAttributesGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesGroups.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen = _OmpTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 24),
    _OmpTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen_Type()
)
ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesWeight_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesWeight_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesWeight = _OmpTlocsFamilyEntriesReceivedAttributesWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 25),
    _OmpTlocsFamilyEntriesReceivedAttributesWeight_Type()
)
ompTlocsFamilyEntriesReceivedAttributesWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesWeight.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesGenId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesGenId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesGenId = _OmpTlocsFamilyEntriesReceivedAttributesGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 26),
    _OmpTlocsFamilyEntriesReceivedAttributesGenId_Type()
)
ompTlocsFamilyEntriesReceivedAttributesGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesGenId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesVersion_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesVersion_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesVersion = _OmpTlocsFamilyEntriesReceivedAttributesVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 27),
    _OmpTlocsFamilyEntriesReceivedAttributesVersion_Type()
)
ompTlocsFamilyEntriesReceivedAttributesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesVersion.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesOriginator_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesOriginator_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesOriginator = _OmpTlocsFamilyEntriesReceivedAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 28),
    _OmpTlocsFamilyEntriesReceivedAttributesOriginator_Type()
)
ompTlocsFamilyEntriesReceivedAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesOriginator.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesRestrict_Type = UnsignedByte
_OmpTlocsFamilyEntriesReceivedAttributesRestrict_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesRestrict = _OmpTlocsFamilyEntriesReceivedAttributesRestrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 29),
    _OmpTlocsFamilyEntriesReceivedAttributesRestrict_Type()
)
ompTlocsFamilyEntriesReceivedAttributesRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesRestrict.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesOverlayId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesOverlayId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesOverlayId = _OmpTlocsFamilyEntriesReceivedAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 30),
    _OmpTlocsFamilyEntriesReceivedAttributesOverlayId_Type()
)
ompTlocsFamilyEntriesReceivedAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesOverlayId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesBandwidth_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesBandwidth_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesBandwidth = _OmpTlocsFamilyEntriesReceivedAttributesBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 31),
    _OmpTlocsFamilyEntriesReceivedAttributesBandwidth_Type()
)
ompTlocsFamilyEntriesReceivedAttributesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesBandwidth.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesQosGroup_Type = String
_OmpTlocsFamilyEntriesReceivedAttributesQosGroup_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesQosGroup = _OmpTlocsFamilyEntriesReceivedAttributesQosGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 32),
    _OmpTlocsFamilyEntriesReceivedAttributesQosGroup_Type()
)
ompTlocsFamilyEntriesReceivedAttributesQosGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesQosGroup.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesOnDemand_Type = UnsignedByte
_OmpTlocsFamilyEntriesReceivedAttributesOnDemand_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesOnDemand = _OmpTlocsFamilyEntriesReceivedAttributesOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 33),
    _OmpTlocsFamilyEntriesReceivedAttributesOnDemand_Type()
)
ompTlocsFamilyEntriesReceivedAttributesOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesOnDemand.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesBandwidthDmin_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesBandwidthDmin_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesBandwidthDmin = _OmpTlocsFamilyEntriesReceivedAttributesBandwidthDmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 34),
    _OmpTlocsFamilyEntriesReceivedAttributesBandwidthDmin_Type()
)
ompTlocsFamilyEntriesReceivedAttributesBandwidthDmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesBandwidthDmin.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesBandwidthDown_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesBandwidthDown_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesBandwidthDown = _OmpTlocsFamilyEntriesReceivedAttributesBandwidthDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 35),
    _OmpTlocsFamilyEntriesReceivedAttributesBandwidthDown_Type()
)
ompTlocsFamilyEntriesReceivedAttributesBandwidthDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesBandwidthDown.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesBandwidthDmax_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesBandwidthDmax_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesBandwidthDmax = _OmpTlocsFamilyEntriesReceivedAttributesBandwidthDmax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 36),
    _OmpTlocsFamilyEntriesReceivedAttributesBandwidthDmax_Type()
)
ompTlocsFamilyEntriesReceivedAttributesBandwidthDmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesBandwidthDmax.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod = _OmpTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 37),
    _OmpTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod_Type()
)
ompTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesAdaptQosUp_Type = UnsignedByte
_OmpTlocsFamilyEntriesReceivedAttributesAdaptQosUp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesAdaptQosUp = _OmpTlocsFamilyEntriesReceivedAttributesAdaptQosUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 38),
    _OmpTlocsFamilyEntriesReceivedAttributesAdaptQosUp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesAdaptQosUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesAdaptQosUp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesSiteType_Type = String
_OmpTlocsFamilyEntriesReceivedAttributesSiteType_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesSiteType = _OmpTlocsFamilyEntriesReceivedAttributesSiteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 6, 1, 39),
    _OmpTlocsFamilyEntriesReceivedAttributesSiteType_Type()
)
ompTlocsFamilyEntriesReceivedAttributesSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesSiteType.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedTable_Object = MibTable
ompTlocsFamilyEntriesAdvertisedTable = _OmpTlocsFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 7)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedTable.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompTlocsFamilyEntriesAdvertisedEntry = _OmpTlocsFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 7, 1)
)
ompTlocsFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesIp"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesColor"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesEncap"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedTenantId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedTenantId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedTenantId = _OmpTlocsFamilyEntriesAdvertisedTenantId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 7, 1, 1),
    _OmpTlocsFamilyEntriesAdvertisedTenantId_Type()
)
ompTlocsFamilyEntriesAdvertisedTenantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedTenantId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedToPeer = _OmpTlocsFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 7, 1, 2),
    _OmpTlocsFamilyEntriesAdvertisedToPeer_Type()
)
ompTlocsFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTable_Object = MibTable
ompTlocsFamilyEntriesAdvertisedAttributesTable = _OmpTlocsFamilyEntriesAdvertisedAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTable.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesEntry_Object = MibTableRow
ompTlocsFamilyEntriesAdvertisedAttributesEntry = _OmpTlocsFamilyEntriesAdvertisedAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1)
)
ompTlocsFamilyEntriesAdvertisedAttributesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesIp"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesColor"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesEncap"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedToPeer"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesAttributeId"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesEntry.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesAttributeId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesAttributeId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesAttributeId = _OmpTlocsFamilyEntriesAdvertisedAttributesAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 1),
    _OmpTlocsFamilyEntriesAdvertisedAttributesAttributeId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesAttributeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesAttributeId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 2),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 3),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 4),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Type = EncryptType
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 5),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType_Type = IntegType
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 6),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 7),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 8),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 9),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 10),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 11),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 12),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 13),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 14),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort.setStatus("current")


class _OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Type(Unsigned32):
    """Custom type ompTlocsFamilyEntriesAdvertisedAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesDomainId = _OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 15),
    _OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesDomainId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesSiteId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesSiteId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesSiteId = _OmpTlocsFamilyEntriesAdvertisedAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 16),
    _OmpTlocsFamilyEntriesAdvertisedAttributesSiteId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesSiteId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesPreference_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesPreference_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesPreference = _OmpTlocsFamilyEntriesAdvertisedAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 17),
    _OmpTlocsFamilyEntriesAdvertisedAttributesPreference_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesPreference.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTag_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesTag_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTag = _OmpTlocsFamilyEntriesAdvertisedAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 18),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTag_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTag.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesStale_Type = UnsignedByte
_OmpTlocsFamilyEntriesAdvertisedAttributesStale_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesStale = _OmpTlocsFamilyEntriesAdvertisedAttributesStale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 19),
    _OmpTlocsFamilyEntriesAdvertisedAttributesStale_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesStale.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Type = CarrierEnum
_OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesCarrier = _OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 20),
    _OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesCarrier.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesGroups_Type = Groups1
_OmpTlocsFamilyEntriesAdvertisedAttributesGroups_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesGroups = _OmpTlocsFamilyEntriesAdvertisedAttributesGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 21),
    _OmpTlocsFamilyEntriesAdvertisedAttributesGroups_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesGroups.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen = _OmpTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 22),
    _OmpTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesWeight_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesWeight_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesWeight = _OmpTlocsFamilyEntriesAdvertisedAttributesWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 23),
    _OmpTlocsFamilyEntriesAdvertisedAttributesWeight_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesWeight.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesGenId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesGenId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesGenId = _OmpTlocsFamilyEntriesAdvertisedAttributesGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 24),
    _OmpTlocsFamilyEntriesAdvertisedAttributesGenId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesGenId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesVersion_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesVersion_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesVersion = _OmpTlocsFamilyEntriesAdvertisedAttributesVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 25),
    _OmpTlocsFamilyEntriesAdvertisedAttributesVersion_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesVersion.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesOriginator_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesOriginator_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesOriginator = _OmpTlocsFamilyEntriesAdvertisedAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 26),
    _OmpTlocsFamilyEntriesAdvertisedAttributesOriginator_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesOriginator.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesRestrict_Type = UnsignedByte
_OmpTlocsFamilyEntriesAdvertisedAttributesRestrict_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesRestrict = _OmpTlocsFamilyEntriesAdvertisedAttributesRestrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 27),
    _OmpTlocsFamilyEntriesAdvertisedAttributesRestrict_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesRestrict.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesOverlayId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesOverlayId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesOverlayId = _OmpTlocsFamilyEntriesAdvertisedAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 28),
    _OmpTlocsFamilyEntriesAdvertisedAttributesOverlayId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesOverlayId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidth_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidth_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesBandwidth = _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 29),
    _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidth_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesBandwidth.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesQosGroup_Type = String
_OmpTlocsFamilyEntriesAdvertisedAttributesQosGroup_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesQosGroup = _OmpTlocsFamilyEntriesAdvertisedAttributesQosGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 30),
    _OmpTlocsFamilyEntriesAdvertisedAttributesQosGroup_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesQosGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesQosGroup.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin = _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 31),
    _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDown_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDown_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDown = _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 32),
    _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDown_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDown.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax = _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 33),
    _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod = _OmpTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 34),
    _OmpTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp = _OmpTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 35),
    _OmpTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesOnDemand_Type = UnsignedByte
_OmpTlocsFamilyEntriesAdvertisedAttributesOnDemand_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesOnDemand = _OmpTlocsFamilyEntriesAdvertisedAttributesOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 36),
    _OmpTlocsFamilyEntriesAdvertisedAttributesOnDemand_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesOnDemand.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesSiteType_Type = String
_OmpTlocsFamilyEntriesAdvertisedAttributesSiteType_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesSiteType = _OmpTlocsFamilyEntriesAdvertisedAttributesSiteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 6, 8, 1, 37),
    _OmpTlocsFamilyEntriesAdvertisedAttributesSiteType_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesSiteType.setStatus("current")
_OmpServices_ObjectIdentity = ObjectIdentity
ompServices = _OmpServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7)
)
_OmpServicesFamilyTable_Object = MibTable
ompServicesFamilyTable = _OmpServicesFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ompServicesFamilyTable.setStatus("current")
_OmpServicesFamilyEntry_Object = MibTableRow
ompServicesFamilyEntry = _OmpServicesFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 1, 1)
)
ompServicesFamilyEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntry.setStatus("current")
_OmpServicesFamilyAddressFamily_Type = AddrFamilyEnum
_OmpServicesFamilyAddressFamily_Object = MibTableColumn
ompServicesFamilyAddressFamily = _OmpServicesFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 1, 1, 1),
    _OmpServicesFamilyAddressFamily_Type()
)
ompServicesFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyAddressFamily.setStatus("current")
_OmpServicesFamilyEntriesTable_Object = MibTable
ompServicesFamilyEntriesTable = _OmpServicesFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesTable.setStatus("current")
_OmpServicesFamilyEntriesEntry_Object = MibTableRow
ompServicesFamilyEntriesEntry = _OmpServicesFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 2, 1)
)
ompServicesFamilyEntriesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesService"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesOriginator"),
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesEntry.setStatus("current")
_OmpServicesFamilyEntriesTenantId_Type = Unsigned32
_OmpServicesFamilyEntriesTenantId_Object = MibTableColumn
ompServicesFamilyEntriesTenantId = _OmpServicesFamilyEntriesTenantId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 2, 1, 1),
    _OmpServicesFamilyEntriesTenantId_Type()
)
ompServicesFamilyEntriesTenantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesTenantId.setStatus("current")


class _OmpServicesFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompServicesFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpServicesFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpServicesFamilyEntriesVpnId_Object = MibTableColumn
ompServicesFamilyEntriesVpnId = _OmpServicesFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 2, 1, 2),
    _OmpServicesFamilyEntriesVpnId_Type()
)
ompServicesFamilyEntriesVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesVpnId.setStatus("current")


class _OmpServicesFamilyEntriesService_Type(Integer32):
    """Custom type ompServicesFamilyEntriesService based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("vPN", 0),
          ("fW", 1),
          ("iDS", 2),
          ("iDP", 3),
          ("netsvc1", 4),
          ("netsvc2", 5),
          ("netsvc3", 6),
          ("netsvc4", 7),
          ("tE", 8),
          ("sig", 9),
          ("appqoe", 10))
    )


_OmpServicesFamilyEntriesService_Type.__name__ = "Integer32"
_OmpServicesFamilyEntriesService_Object = MibTableColumn
ompServicesFamilyEntriesService = _OmpServicesFamilyEntriesService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 2, 1, 3),
    _OmpServicesFamilyEntriesService_Type()
)
ompServicesFamilyEntriesService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesService.setStatus("current")
_OmpServicesFamilyEntriesOriginator_Type = InetAddressIP
_OmpServicesFamilyEntriesOriginator_Object = MibTableColumn
ompServicesFamilyEntriesOriginator = _OmpServicesFamilyEntriesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 2, 1, 4),
    _OmpServicesFamilyEntriesOriginator_Type()
)
ompServicesFamilyEntriesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesOriginator.setStatus("current")
_OmpServicesFamilyEntriesReceivedTable_Object = MibTable
ompServicesFamilyEntriesReceivedTable = _OmpServicesFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedTable.setStatus("current")
_OmpServicesFamilyEntriesReceivedEntry_Object = MibTableRow
ompServicesFamilyEntriesReceivedEntry = _OmpServicesFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1)
)
ompServicesFamilyEntriesReceivedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesService"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedFromPeer"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedPathId"),
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedEntry.setStatus("current")
_OmpServicesFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpServicesFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompServicesFamilyEntriesReceivedFromPeer = _OmpServicesFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 1),
    _OmpServicesFamilyEntriesReceivedFromPeer_Type()
)
ompServicesFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpServicesFamilyEntriesReceivedPathId_Type = Unsigned32
_OmpServicesFamilyEntriesReceivedPathId_Object = MibTableColumn
ompServicesFamilyEntriesReceivedPathId = _OmpServicesFamilyEntriesReceivedPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 2),
    _OmpServicesFamilyEntriesReceivedPathId_Type()
)
ompServicesFamilyEntriesReceivedPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedPathId.setStatus("current")
_OmpServicesFamilyEntriesReceivedRegionId_Type = String
_OmpServicesFamilyEntriesReceivedRegionId_Object = MibTableColumn
ompServicesFamilyEntriesReceivedRegionId = _OmpServicesFamilyEntriesReceivedRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 3),
    _OmpServicesFamilyEntriesReceivedRegionId_Type()
)
ompServicesFamilyEntriesReceivedRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedRegionId.setStatus("current")
_OmpServicesFamilyEntriesReceivedLabel_Type = Unsigned32
_OmpServicesFamilyEntriesReceivedLabel_Object = MibTableColumn
ompServicesFamilyEntriesReceivedLabel = _OmpServicesFamilyEntriesReceivedLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 4),
    _OmpServicesFamilyEntriesReceivedLabel_Type()
)
ompServicesFamilyEntriesReceivedLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedLabel.setStatus("current")
_OmpServicesFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpServicesFamilyEntriesReceivedStatus_Object = MibTableColumn
ompServicesFamilyEntriesReceivedStatus = _OmpServicesFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 5),
    _OmpServicesFamilyEntriesReceivedStatus_Type()
)
ompServicesFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedStatus.setStatus("current")
_OmpServicesFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpServicesFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompServicesFamilyEntriesReceivedLossReason = _OmpServicesFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 6),
    _OmpServicesFamilyEntriesReceivedLossReason_Type()
)
ompServicesFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedLossReason.setStatus("current")
_OmpServicesFamilyEntriesReceivedLostToPeer_Type = InetAddressIP
_OmpServicesFamilyEntriesReceivedLostToPeer_Object = MibTableColumn
ompServicesFamilyEntriesReceivedLostToPeer = _OmpServicesFamilyEntriesReceivedLostToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 7),
    _OmpServicesFamilyEntriesReceivedLostToPeer_Type()
)
ompServicesFamilyEntriesReceivedLostToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedLostToPeer.setStatus("current")
_OmpServicesFamilyEntriesReceivedLostToPathId_Type = Unsigned32
_OmpServicesFamilyEntriesReceivedLostToPathId_Object = MibTableColumn
ompServicesFamilyEntriesReceivedLostToPathId = _OmpServicesFamilyEntriesReceivedLostToPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 8),
    _OmpServicesFamilyEntriesReceivedLostToPathId_Type()
)
ompServicesFamilyEntriesReceivedLostToPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedLostToPathId.setStatus("current")
_OmpServicesFamilyEntriesReceivedVrfId_Type = Unsigned32
_OmpServicesFamilyEntriesReceivedVrfId_Object = MibTableColumn
ompServicesFamilyEntriesReceivedVrfId = _OmpServicesFamilyEntriesReceivedVrfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 3, 1, 9),
    _OmpServicesFamilyEntriesReceivedVrfId_Type()
)
ompServicesFamilyEntriesReceivedVrfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedVrfId.setStatus("current")
_OmpServicesFamilyEntriesAdvertisedTable_Object = MibTable
ompServicesFamilyEntriesAdvertisedTable = _OmpServicesFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 4)
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesAdvertisedTable.setStatus("current")
_OmpServicesFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompServicesFamilyEntriesAdvertisedEntry = _OmpServicesFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 4, 1)
)
ompServicesFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesService"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpServicesFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpServicesFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompServicesFamilyEntriesAdvertisedToPeer = _OmpServicesFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 7, 4, 1, 1),
    _OmpServicesFamilyEntriesAdvertisedToPeer_Type()
)
ompServicesFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpMulticastAutoDiscover_ObjectIdentity = ObjectIdentity
ompMulticastAutoDiscover = _OmpMulticastAutoDiscover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8)
)
_OmpMulticastAutoDiscoverFamilyTable_Object = MibTable
ompMulticastAutoDiscoverFamilyTable = _OmpMulticastAutoDiscoverFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyTable.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntry_Object = MibTableRow
ompMulticastAutoDiscoverFamilyEntry = _OmpMulticastAutoDiscoverFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 1, 1)
)
ompMulticastAutoDiscoverFamilyEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntry.setStatus("current")
_OmpMulticastAutoDiscoverFamilyAddressFamily_Type = AddrFamilyEnum
_OmpMulticastAutoDiscoverFamilyAddressFamily_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyAddressFamily = _OmpMulticastAutoDiscoverFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 1, 1, 1),
    _OmpMulticastAutoDiscoverFamilyAddressFamily_Type()
)
ompMulticastAutoDiscoverFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyAddressFamily.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesTable_Object = MibTable
ompMulticastAutoDiscoverFamilyEntriesTable = _OmpMulticastAutoDiscoverFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesTable.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesEntry_Object = MibTableRow
ompMulticastAutoDiscoverFamilyEntriesEntry = _OmpMulticastAutoDiscoverFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 2, 1)
)
ompMulticastAutoDiscoverFamilyEntriesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator"),
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesEntry.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesTenantId_Type = Unsigned32
_OmpMulticastAutoDiscoverFamilyEntriesTenantId_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesTenantId = _OmpMulticastAutoDiscoverFamilyEntriesTenantId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 2, 1, 1),
    _OmpMulticastAutoDiscoverFamilyEntriesTenantId_Type()
)
ompMulticastAutoDiscoverFamilyEntriesTenantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesTenantId.setStatus("current")


class _OmpMulticastAutoDiscoverFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompMulticastAutoDiscoverFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpMulticastAutoDiscoverFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpMulticastAutoDiscoverFamilyEntriesVpnId_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesVpnId = _OmpMulticastAutoDiscoverFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 2, 1, 2),
    _OmpMulticastAutoDiscoverFamilyEntriesVpnId_Type()
)
ompMulticastAutoDiscoverFamilyEntriesVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesVpnId.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesSourceOriginator_Type = InetAddressIP
_OmpMulticastAutoDiscoverFamilyEntriesSourceOriginator_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesSourceOriginator = _OmpMulticastAutoDiscoverFamilyEntriesSourceOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 2, 1, 3),
    _OmpMulticastAutoDiscoverFamilyEntriesSourceOriginator_Type()
)
ompMulticastAutoDiscoverFamilyEntriesSourceOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesSourceOriginator.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedTable_Object = MibTable
ompMulticastAutoDiscoverFamilyEntriesReceivedTable = _OmpMulticastAutoDiscoverFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedTable.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedEntry_Object = MibTableRow
ompMulticastAutoDiscoverFamilyEntriesReceivedEntry = _OmpMulticastAutoDiscoverFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 3, 1)
)
ompMulticastAutoDiscoverFamilyEntriesReceivedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer"),
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedEntry.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpMulticastAutoDiscoverFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer = _OmpMulticastAutoDiscoverFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 3, 1, 1),
    _OmpMulticastAutoDiscoverFamilyEntriesReceivedFromPeer_Type()
)
ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpMulticastAutoDiscoverFamilyEntriesReceivedStatus_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesReceivedStatus = _OmpMulticastAutoDiscoverFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 3, 1, 2),
    _OmpMulticastAutoDiscoverFamilyEntriesReceivedStatus_Type()
)
ompMulticastAutoDiscoverFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedStatus.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpMulticastAutoDiscoverFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason = _OmpMulticastAutoDiscoverFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 3, 1, 3),
    _OmpMulticastAutoDiscoverFamilyEntriesReceivedLossReason_Type()
)
ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesAdvertisedTable_Object = MibTable
ompMulticastAutoDiscoverFamilyEntriesAdvertisedTable = _OmpMulticastAutoDiscoverFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 4)
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesAdvertisedTable.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry = _OmpMulticastAutoDiscoverFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 4, 1)
)
ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer = _OmpMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 8, 4, 1, 1),
    _OmpMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer_Type()
)
ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpMulticastRoutes_ObjectIdentity = ObjectIdentity
ompMulticastRoutes = _OmpMulticastRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9)
)
_OmpMulticastRoutesFamilyTable_Object = MibTable
ompMulticastRoutesFamilyTable = _OmpMulticastRoutesFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyTable.setStatus("current")
_OmpMulticastRoutesFamilyEntry_Object = MibTableRow
ompMulticastRoutesFamilyEntry = _OmpMulticastRoutesFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 1, 1)
)
ompMulticastRoutesFamilyEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntry.setStatus("current")
_OmpMulticastRoutesFamilyAddressFamily_Type = AddrFamilyEnum
_OmpMulticastRoutesFamilyAddressFamily_Object = MibTableColumn
ompMulticastRoutesFamilyAddressFamily = _OmpMulticastRoutesFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 1, 1, 1),
    _OmpMulticastRoutesFamilyAddressFamily_Type()
)
ompMulticastRoutesFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyAddressFamily.setStatus("current")
_OmpMulticastRoutesFamilyEntriesTable_Object = MibTable
ompMulticastRoutesFamilyEntriesTable = _OmpMulticastRoutesFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesTable.setStatus("current")
_OmpMulticastRoutesFamilyEntriesEntry_Object = MibTableRow
ompMulticastRoutesFamilyEntriesEntry = _OmpMulticastRoutesFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2, 1)
)
ompMulticastRoutesFamilyEntriesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesType"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesDestination"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesGroup"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesSource"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesSourceOriginator"),
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesEntry.setStatus("current")
_OmpMulticastRoutesFamilyEntriesTenantId_Type = Unsigned32
_OmpMulticastRoutesFamilyEntriesTenantId_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesTenantId = _OmpMulticastRoutesFamilyEntriesTenantId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2, 1, 1),
    _OmpMulticastRoutesFamilyEntriesTenantId_Type()
)
ompMulticastRoutesFamilyEntriesTenantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesTenantId.setStatus("current")
_OmpMulticastRoutesFamilyEntriesType_Type = McastRouteEnum
_OmpMulticastRoutesFamilyEntriesType_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesType = _OmpMulticastRoutesFamilyEntriesType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2, 1, 2),
    _OmpMulticastRoutesFamilyEntriesType_Type()
)
ompMulticastRoutesFamilyEntriesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesType.setStatus("current")


class _OmpMulticastRoutesFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompMulticastRoutesFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpMulticastRoutesFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpMulticastRoutesFamilyEntriesVpnId_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesVpnId = _OmpMulticastRoutesFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2, 1, 3),
    _OmpMulticastRoutesFamilyEntriesVpnId_Type()
)
ompMulticastRoutesFamilyEntriesVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesVpnId.setStatus("current")
_OmpMulticastRoutesFamilyEntriesDestination_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesDestination_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesDestination = _OmpMulticastRoutesFamilyEntriesDestination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2, 1, 4),
    _OmpMulticastRoutesFamilyEntriesDestination_Type()
)
ompMulticastRoutesFamilyEntriesDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesDestination.setStatus("current")
_OmpMulticastRoutesFamilyEntriesGroup_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesGroup_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesGroup = _OmpMulticastRoutesFamilyEntriesGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2, 1, 5),
    _OmpMulticastRoutesFamilyEntriesGroup_Type()
)
ompMulticastRoutesFamilyEntriesGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesGroup.setStatus("current")
_OmpMulticastRoutesFamilyEntriesSource_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesSource_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesSource = _OmpMulticastRoutesFamilyEntriesSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2, 1, 6),
    _OmpMulticastRoutesFamilyEntriesSource_Type()
)
ompMulticastRoutesFamilyEntriesSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesSource.setStatus("current")
_OmpMulticastRoutesFamilyEntriesSourceOriginator_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesSourceOriginator_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesSourceOriginator = _OmpMulticastRoutesFamilyEntriesSourceOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 2, 1, 7),
    _OmpMulticastRoutesFamilyEntriesSourceOriginator_Type()
)
ompMulticastRoutesFamilyEntriesSourceOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesSourceOriginator.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedTable_Object = MibTable
ompMulticastRoutesFamilyEntriesReceivedTable = _OmpMulticastRoutesFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 3)
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedTable.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedEntry_Object = MibTableRow
ompMulticastRoutesFamilyEntriesReceivedEntry = _OmpMulticastRoutesFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 3, 1)
)
ompMulticastRoutesFamilyEntriesReceivedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesType"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesDestination"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesGroup"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesSource"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesSourceOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesReceivedFromPeer"),
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedEntry.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedFromPeer = _OmpMulticastRoutesFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 3, 1, 1),
    _OmpMulticastRoutesFamilyEntriesReceivedFromPeer_Type()
)
ompMulticastRoutesFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedRp_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesReceivedRp_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedRp = _OmpMulticastRoutesFamilyEntriesReceivedRp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 3, 1, 2),
    _OmpMulticastRoutesFamilyEntriesReceivedRp_Type()
)
ompMulticastRoutesFamilyEntriesReceivedRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedRp.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedReceivedPrunes_Type = ReceivedPrunes1
_OmpMulticastRoutesFamilyEntriesReceivedReceivedPrunes_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes = _OmpMulticastRoutesFamilyEntriesReceivedReceivedPrunes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 3, 1, 3),
    _OmpMulticastRoutesFamilyEntriesReceivedReceivedPrunes_Type()
)
ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpMulticastRoutesFamilyEntriesReceivedStatus_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedStatus = _OmpMulticastRoutesFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 3, 1, 4),
    _OmpMulticastRoutesFamilyEntriesReceivedStatus_Type()
)
ompMulticastRoutesFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedStatus.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpMulticastRoutesFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedLossReason = _OmpMulticastRoutesFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 3, 1, 5),
    _OmpMulticastRoutesFamilyEntriesReceivedLossReason_Type()
)
ompMulticastRoutesFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedLossReason.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedTable_Object = MibTable
ompMulticastRoutesFamilyEntriesAdvertisedTable = _OmpMulticastRoutesFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 4)
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedTable.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompMulticastRoutesFamilyEntriesAdvertisedEntry = _OmpMulticastRoutesFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 4, 1)
)
ompMulticastRoutesFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyAddressFamily"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesType"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesDestination"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesGroup"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesSource"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesSourceOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesAdvertisedToPeer = _OmpMulticastRoutesFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 4, 1, 1),
    _OmpMulticastRoutesFamilyEntriesAdvertisedToPeer_Type()
)
ompMulticastRoutesFamilyEntriesAdvertisedToPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedRp_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesAdvertisedRp_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesAdvertisedRp = _OmpMulticastRoutesFamilyEntriesAdvertisedRp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 4, 1, 2),
    _OmpMulticastRoutesFamilyEntriesAdvertisedRp_Type()
)
ompMulticastRoutesFamilyEntriesAdvertisedRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedRp.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes_Type = AdvertisedPrunes1
_OmpMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes = _OmpMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 9, 4, 1, 3),
    _OmpMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes_Type()
)
ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes.setStatus("current")
_OmpCloudexpressRoutes_ObjectIdentity = ObjectIdentity
ompCloudexpressRoutes = _OmpCloudexpressRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10)
)
_OmpCloudexpressEntriesTable_Object = MibTable
ompCloudexpressEntriesTable = _OmpCloudexpressEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesTable.setStatus("current")
_OmpCloudexpressEntriesEntry_Object = MibTableRow
ompCloudexpressEntriesEntry = _OmpCloudexpressEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1, 1)
)
ompCloudexpressEntriesEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAppId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAppType"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesSubAppId"),
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesEntry.setStatus("current")
_OmpCloudexpressEntriesTenantId_Type = Unsigned32
_OmpCloudexpressEntriesTenantId_Object = MibTableColumn
ompCloudexpressEntriesTenantId = _OmpCloudexpressEntriesTenantId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1, 1, 1),
    _OmpCloudexpressEntriesTenantId_Type()
)
ompCloudexpressEntriesTenantId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesTenantId.setStatus("current")


class _OmpCloudexpressEntriesVpnId_Type(Unsigned32):
    """Custom type ompCloudexpressEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpCloudexpressEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpCloudexpressEntriesVpnId_Object = MibTableColumn
ompCloudexpressEntriesVpnId = _OmpCloudexpressEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1, 1, 2),
    _OmpCloudexpressEntriesVpnId_Type()
)
ompCloudexpressEntriesVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesVpnId.setStatus("current")
_OmpCloudexpressEntriesOriginator_Type = InetAddressIP
_OmpCloudexpressEntriesOriginator_Object = MibTableColumn
ompCloudexpressEntriesOriginator = _OmpCloudexpressEntriesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1, 1, 3),
    _OmpCloudexpressEntriesOriginator_Type()
)
ompCloudexpressEntriesOriginator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesOriginator.setStatus("current")
_OmpCloudexpressEntriesAppId_Type = Unsigned32
_OmpCloudexpressEntriesAppId_Object = MibTableColumn
ompCloudexpressEntriesAppId = _OmpCloudexpressEntriesAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1, 1, 4),
    _OmpCloudexpressEntriesAppId_Type()
)
ompCloudexpressEntriesAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAppId.setStatus("current")
_OmpCloudexpressEntriesAppType_Type = UnsignedByte
_OmpCloudexpressEntriesAppType_Object = MibTableColumn
ompCloudexpressEntriesAppType = _OmpCloudexpressEntriesAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1, 1, 5),
    _OmpCloudexpressEntriesAppType_Type()
)
ompCloudexpressEntriesAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAppType.setStatus("current")
_OmpCloudexpressEntriesSubAppId_Type = Unsigned32
_OmpCloudexpressEntriesSubAppId_Object = MibTableColumn
ompCloudexpressEntriesSubAppId = _OmpCloudexpressEntriesSubAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1, 1, 6),
    _OmpCloudexpressEntriesSubAppId_Type()
)
ompCloudexpressEntriesSubAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesSubAppId.setStatus("current")
_OmpCloudexpressEntriesAppName_Type = String
_OmpCloudexpressEntriesAppName_Object = MibTableColumn
ompCloudexpressEntriesAppName = _OmpCloudexpressEntriesAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 1, 1, 7),
    _OmpCloudexpressEntriesAppName_Type()
)
ompCloudexpressEntriesAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAppName.setStatus("current")
_OmpCloudexpressEntriesReceivedTable_Object = MibTable
ompCloudexpressEntriesReceivedTable = _OmpCloudexpressEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedTable.setStatus("current")
_OmpCloudexpressEntriesReceivedEntry_Object = MibTableRow
ompCloudexpressEntriesReceivedEntry = _OmpCloudexpressEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 2, 1)
)
ompCloudexpressEntriesReceivedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAppId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAppType"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesSubAppId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesReceivedFromPeer"),
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedEntry.setStatus("current")
_OmpCloudexpressEntriesReceivedFromPeer_Type = InetAddressIP
_OmpCloudexpressEntriesReceivedFromPeer_Object = MibTableColumn
ompCloudexpressEntriesReceivedFromPeer = _OmpCloudexpressEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 2, 1, 1),
    _OmpCloudexpressEntriesReceivedFromPeer_Type()
)
ompCloudexpressEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedFromPeer.setStatus("current")
_OmpCloudexpressEntriesReceivedStatus_Type = RibInStatusType
_OmpCloudexpressEntriesReceivedStatus_Object = MibTableColumn
ompCloudexpressEntriesReceivedStatus = _OmpCloudexpressEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 2, 1, 2),
    _OmpCloudexpressEntriesReceivedStatus_Type()
)
ompCloudexpressEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedStatus.setStatus("current")
_OmpCloudexpressEntriesReceivedLossReason_Type = LossReasonEnum
_OmpCloudexpressEntriesReceivedLossReason_Object = MibTableColumn
ompCloudexpressEntriesReceivedLossReason = _OmpCloudexpressEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 2, 1, 3),
    _OmpCloudexpressEntriesReceivedLossReason_Type()
)
ompCloudexpressEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedLossReason.setStatus("current")
_OmpCloudexpressEntriesReceivedLatency_Type = Unsigned32
_OmpCloudexpressEntriesReceivedLatency_Object = MibTableColumn
ompCloudexpressEntriesReceivedLatency = _OmpCloudexpressEntriesReceivedLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 2, 1, 4),
    _OmpCloudexpressEntriesReceivedLatency_Type()
)
ompCloudexpressEntriesReceivedLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedLatency.setStatus("current")
_OmpCloudexpressEntriesReceivedLoss_Type = Unsigned32
_OmpCloudexpressEntriesReceivedLoss_Object = MibTableColumn
ompCloudexpressEntriesReceivedLoss = _OmpCloudexpressEntriesReceivedLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 2, 1, 5),
    _OmpCloudexpressEntriesReceivedLoss_Type()
)
ompCloudexpressEntriesReceivedLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedLoss.setStatus("current")
_OmpCloudexpressEntriesAdvertisedTable_Object = MibTable
ompCloudexpressEntriesAdvertisedTable = _OmpCloudexpressEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 3)
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedTable.setStatus("current")
_OmpCloudexpressEntriesAdvertisedEntry_Object = MibTableRow
ompCloudexpressEntriesAdvertisedEntry = _OmpCloudexpressEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 3, 1)
)
ompCloudexpressEntriesAdvertisedEntry.setIndexNames(
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesTenantId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesVpnId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesOriginator"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAppId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAppType"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesSubAppId"),
    (0, "CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedEntry.setStatus("current")
_OmpCloudexpressEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpCloudexpressEntriesAdvertisedToPeer_Object = MibTableColumn
ompCloudexpressEntriesAdvertisedToPeer = _OmpCloudexpressEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 3, 1, 1),
    _OmpCloudexpressEntriesAdvertisedToPeer_Type()
)
ompCloudexpressEntriesAdvertisedToPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedToPeer.setStatus("current")
_OmpCloudexpressEntriesAdvertisedLatency_Type = Unsigned32
_OmpCloudexpressEntriesAdvertisedLatency_Object = MibTableColumn
ompCloudexpressEntriesAdvertisedLatency = _OmpCloudexpressEntriesAdvertisedLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 3, 1, 2),
    _OmpCloudexpressEntriesAdvertisedLatency_Type()
)
ompCloudexpressEntriesAdvertisedLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedLatency.setStatus("current")
_OmpCloudexpressEntriesAdvertisedLoss_Type = Unsigned32
_OmpCloudexpressEntriesAdvertisedLoss_Object = MibTableColumn
ompCloudexpressEntriesAdvertisedLoss = _OmpCloudexpressEntriesAdvertisedLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 1, 10, 3, 1, 3),
    _OmpCloudexpressEntriesAdvertisedLoss_Type()
)
ompCloudexpressEntriesAdvertisedLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedLoss.setStatus("current")
_CiscoSdwanOmpMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanOmpMIBNotifObjects = _CiscoSdwanOmpMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 2)
)
_NetconfNotificationSeverity_Type = NotificationSeverity
_NetconfNotificationSeverity_Object = MibScalar
netconfNotificationSeverity = _NetconfNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 2),
    _NetconfNotificationSeverity_Type()
)
netconfNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netconfNotificationSeverity.setStatus("current")
_CiscoSdwanOmpNumberOfVsmarts_Type = Unsigned32
_CiscoSdwanOmpNumberOfVsmarts_Object = MibScalar
ciscoSdwanOmpNumberOfVsmarts = _CiscoSdwanOmpNumberOfVsmarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 3),
    _CiscoSdwanOmpNumberOfVsmarts_Type()
)
ciscoSdwanOmpNumberOfVsmarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanOmpNumberOfVsmarts.setStatus("current")
_CiscoSdwanOmpNewState_Type = OperState
_CiscoSdwanOmpNewState_Object = MibScalar
ciscoSdwanOmpNewState = _CiscoSdwanOmpNewState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 4),
    _CiscoSdwanOmpNewState_Type()
)
ciscoSdwanOmpNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanOmpNewState.setStatus("current")
_CiscoSdwanOmpPeer_Type = InetAddressIP
_CiscoSdwanOmpPeer_Object = MibScalar
ciscoSdwanOmpPeer = _CiscoSdwanOmpPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 5),
    _CiscoSdwanOmpPeer_Type()
)
ciscoSdwanOmpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanOmpPeer.setStatus("current")
_CiscoSdwanOmpPeerNewState_Type = PeerState
_CiscoSdwanOmpPeerNewState_Object = MibScalar
ciscoSdwanOmpPeerNewState = _CiscoSdwanOmpPeerNewState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 6),
    _CiscoSdwanOmpPeerNewState_Type()
)
ciscoSdwanOmpPeerNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanOmpPeerNewState.setStatus("current")
_CiscoSdwanOmpPolicy_Type = OmpPolicyState
_CiscoSdwanOmpPolicy_Object = MibScalar
ciscoSdwanOmpPolicy = _CiscoSdwanOmpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 7),
    _CiscoSdwanOmpPolicy_Type()
)
ciscoSdwanOmpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanOmpPolicy.setStatus("current")
_CiscoSdwanOmpVsmartPeer_Type = InetAddressIP
_CiscoSdwanOmpVsmartPeer_Object = MibScalar
ciscoSdwanOmpVsmartPeer = _CiscoSdwanOmpVsmartPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 8),
    _CiscoSdwanOmpVsmartPeer_Type()
)
ciscoSdwanOmpVsmartPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanOmpVsmartPeer.setStatus("current")
_CiscoSdwanOmpMIBConform_ObjectIdentity = ObjectIdentity
ciscoSdwanOmpMIBConform = _CiscoSdwanOmpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3)
)
_CiscoSdwanOmpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdwanOmpMIBCompliances = _CiscoSdwanOmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 1)
)
_CiscoSdwanOmpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdwanOmpMIBGroups = _CiscoSdwanOmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2)
)

# Managed Objects groups

cSdwanOmpNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 1)
)
cSdwanOmpNotifObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNumberOfVsmarts"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNewState"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeer"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeerNewState"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPolicy"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpVsmartPeer"))
)
if mibBuilder.loadTexts:
    cSdwanOmpNotifObjsGroup.setStatus("current")

cSdwanOmpSummaryObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 3)
)
cSdwanOmpSummaryObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompSummaryOperstate"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryAdminstate"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryDevicetype"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryOmpuptime"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryOmpdowntime"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryRoutesReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryRoutesInstalled"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryRoutesSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryTlocsReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryTlocsInstalled"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryTlocsSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryServicesReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryServicesInstalled"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryServicesSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMcastRoutesReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMcastRoutesInstalled"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMcastRoutesSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryHelloReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryHelloSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryHandshakeReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryHandshakeSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryAlertReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryAlertSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryInformReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryInformSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryUpdateReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryUpdateSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryPolicyReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryPolicySent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryPacketsReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryPacketsSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryVsmartPeers"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummarySiteType"))
)
if mibBuilder.loadTexts:
    cSdwanOmpSummaryObjsGroup.setStatus("current")

cSdwanOmpSummaryMtPeersObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 4)
)
cSdwanOmpSummaryMtPeersObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersType"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersDomainId"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersSiteId"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRegionId"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersState"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersVersion"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersLegit"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersUpcount"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersDowncount"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersLastuptime"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersLastdowntime"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersUpTime"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersDownTime"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersHoldtime"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersSitepolicy"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersPolicyin"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersPolicyout"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersGracefulRestart"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersGracefulRestartInterval"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersHelloReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersHelloSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersHandshakeReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersHandshakeSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersAlertReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersAlertSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersInformReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersInformSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersUpdateReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersUpdateSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersPolicyReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersPolicySent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersPacketsReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersPacketsSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesInstalled"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersTlocsReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersTlocsInstalled"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersTlocsSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersServicesReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersServicesInstalled"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersServicesSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersMcastRoutesReceived"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersMcastRoutesInstalled"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersMcastRoutesSent"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersControlUp"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersStaging"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRefresh"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersOverlayId"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesReceivedIPv6"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesInstalledIPv6"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesSentIPv6"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesReceivedTotal"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesInstalledTotal"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersRoutesSentTotal"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersServicesReceivedIPv6"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersServicesInstalledIPv6"),
        ("CISCO-SDWAN-OMP-MIB", "ompSummaryMtPeersServicesSentIPv6"))
)
if mibBuilder.loadTexts:
    cSdwanOmpSummaryMtPeersObjsGroup.setStatus("current")

cSdwanOmpRoutesObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 5)
)
cSdwanOmpRoutesObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyAddressFamily"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesTenantId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesVpnId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesPrefix"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedLabel"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedLossReason"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedLostToPeer"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedLostToPathId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesTlocIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesTlocColor"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesDomainId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesSiteId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesPreference"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesTag"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesOriginator"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesOverlayId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesAsPath"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesCommunity"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesRegionId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesRegionPath"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesReceivedAttributesSiteType"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedToPeer"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath"),
        ("CISCO-SDWAN-OMP-MIB", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType"))
)
if mibBuilder.loadTexts:
    cSdwanOmpRoutesObjsGroup.setStatus("current")

cSdwanOmpTlocPathsObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 6)
)
cSdwanOmpTlocPathsObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesColor"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesEncap"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsPreference"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsMtu"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsBfdStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsStale"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsLinksFromTlocIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsLinksFromTlocColor"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsLinksFromTlocEncap"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsLinksToTlocIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsLinksToTlocColor"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsLinksToTlocEncap"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocPathsEntriesPathsLinksLabel"))
)
if mibBuilder.loadTexts:
    cSdwanOmpTlocPathsObjsGroup.setStatus("current")

cSdwanOmpTlocsObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 7)
)
cSdwanOmpTlocsObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyAddressFamily"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesColor"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesEncap"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedLossReason"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedLostToPeer"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedLostToPathId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesAttributeType"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesBfdStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesDomainId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesSiteId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesPreference"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesTag"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesStale"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesCarrier"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesGroups"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesWeight"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesGenId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesVersion"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesOriginator"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesRestrict"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesOverlayId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesBandwidth"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesQosGroup"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesBandwidthDmin"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesBandwidthDown"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesBandwidthDmax"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesAdaptQosUp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesSiteType"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesReceivedAttributesOnDemand"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedTenantId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedToPeer"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesDomainId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesSiteId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesPreference"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesTag"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesStale"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesCarrier"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesGroups"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesWeight"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesGenId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesVersion"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesOriginator"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesRestrict"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesOverlayId"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesBandwidth"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDown"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesQosGroup"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesOnDemand"),
        ("CISCO-SDWAN-OMP-MIB", "ompTlocsFamilyEntriesAdvertisedAttributesSiteType"))
)
if mibBuilder.loadTexts:
    cSdwanOmpTlocsObjsGroup.setStatus("current")

cSdwanOmpServicesObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 8)
)
cSdwanOmpServicesObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyAddressFamily"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesTenantId"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesVpnId"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesService"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesOriginator"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedRegionId"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedLabel"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedLossReason"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedLostToPeer"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedLostToPathId"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesReceivedVrfId"),
        ("CISCO-SDWAN-OMP-MIB", "ompServicesFamilyEntriesAdvertisedToPeer"))
)
if mibBuilder.loadTexts:
    cSdwanOmpServicesObjsGroup.setStatus("current")

cSdwanOmpMulticastAutoDiscoverObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 9)
)
cSdwanOmpMulticastAutoDiscoverObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyAddressFamily"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesTenantId"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesVpnId"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesReceivedStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer"))
)
if mibBuilder.loadTexts:
    cSdwanOmpMulticastAutoDiscoverObjsGroup.setStatus("current")

cSdwanOmpMulticastRoutesObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 10)
)
cSdwanOmpMulticastRoutesObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyAddressFamily"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesTenantId"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesType"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesVpnId"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesDestination"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesGroup"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesSource"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesSourceOriginator"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesReceivedRp"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesReceivedStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesReceivedLossReason"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesAdvertisedRp"),
        ("CISCO-SDWAN-OMP-MIB", "ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes"))
)
if mibBuilder.loadTexts:
    cSdwanOmpMulticastRoutesObjsGroup.setStatus("current")

cSdwanOmpCloudexpressRoutesObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 11)
)
cSdwanOmpCloudexpressRoutesObjsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAppName"),
        ("CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesReceivedStatus"),
        ("CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesReceivedLossReason"),
        ("CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesReceivedLatency"),
        ("CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesReceivedLoss"),
        ("CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAdvertisedLatency"),
        ("CISCO-SDWAN-OMP-MIB", "ompCloudexpressEntriesAdvertisedLoss"))
)
if mibBuilder.loadTexts:
    cSdwanOmpCloudexpressRoutesObjsGroup.setStatus("current")


# Notification objects

ciscoSdwanOmpOmpNumberOfVsmartsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 1)
)
ciscoSdwanOmpOmpNumberOfVsmartsChange.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNumberOfVsmarts"))
)
if mibBuilder.loadTexts:
    ciscoSdwanOmpOmpNumberOfVsmartsChange.setStatus(
        "current"
    )

ciscoSdwanOmpOmpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 2)
)
ciscoSdwanOmpOmpStateChange.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNewState"))
)
if mibBuilder.loadTexts:
    ciscoSdwanOmpOmpStateChange.setStatus(
        "current"
    )

ciscoSdwanOmpOmpPeerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 3)
)
ciscoSdwanOmpOmpPeerStateChange.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeer"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeerNewState"))
)
if mibBuilder.loadTexts:
    ciscoSdwanOmpOmpPeerStateChange.setStatus(
        "current"
    )

ciscoSdwanOmpOmpPolicy = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 4)
)
ciscoSdwanOmpOmpPolicy.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPolicy"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpVsmartPeer"))
)
if mibBuilder.loadTexts:
    ciscoSdwanOmpOmpPolicy.setStatus(
        "current"
    )


# Notifications groups

cSdwanOmpNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 2)
)
cSdwanOmpNotifsGroup.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpNumberOfVsmartsChange"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpStateChange"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpPeerStateChange"),
        ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpPolicy"))
)
if mibBuilder.loadTexts:
    cSdwanOmpNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSdwanOmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 1, 1)
)
ciscoSdwanOmpMIBCompliance.setObjects(
      *(("CISCO-SDWAN-OMP-MIB", "cSdwanOmpNotifObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpNotifsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpSummaryObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpSummaryMtPeersObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpRoutesObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpTlocPathsObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpTlocsObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpServicesObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpMulticastAutoDiscoverObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpMulticastRoutesObjsGroup"),
        ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpCloudexpressRoutesObjsGroup"))
)
if mibBuilder.loadTexts:
    ciscoSdwanOmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDWAN-OMP-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "IpPrefix": IpPrefix,
       "String": String,
       "Groups1": Groups1,
       "AttributeTypeEnum": AttributeTypeEnum,
       "ReceivedPrunes1": ReceivedPrunes1,
       "AdvertisedPrunes1": AdvertisedPrunes1,
       "BfdStatusEnum": BfdStatusEnum,
       "PathStatusEnum": PathStatusEnum,
       "RibInStatusType": RibInStatusType,
       "AddrFamilyEnum": AddrFamilyEnum,
       "LossReasonEnum": LossReasonEnum,
       "McastRouteEnum": McastRouteEnum,
       "TlocColorEnum": TlocColorEnum,
       "TlocEncapEnum": TlocEncapEnum,
       "ProtocolEnum": ProtocolEnum,
       "TlocActionEnum": TlocActionEnum,
       "EncryptType": EncryptType,
       "IntegType": IntegType,
       "CarrierEnum": CarrierEnum,
       "NotificationSeverity": NotificationSeverity,
       "OperState": OperState,
       "PeerState": PeerState,
       "OmpPolicyState": OmpPolicyState,
       "InetAddressIP": InetAddressIP,
       "ciscoSdwanOmpMIB": ciscoSdwanOmpMIB,
       "ciscoSdwanOmpMIBNotifs": ciscoSdwanOmpMIBNotifs,
       "ciscoSdwanOmpOmpNumberOfVsmartsChange": ciscoSdwanOmpOmpNumberOfVsmartsChange,
       "ciscoSdwanOmpOmpStateChange": ciscoSdwanOmpOmpStateChange,
       "ciscoSdwanOmpOmpPeerStateChange": ciscoSdwanOmpOmpPeerStateChange,
       "ciscoSdwanOmpOmpPolicy": ciscoSdwanOmpOmpPolicy,
       "ciscoSdwanOmpMIBObjects": ciscoSdwanOmpMIBObjects,
       "omp": omp,
       "ompSummaryTable": ompSummaryTable,
       "ompSummary": ompSummary,
       "ompSummaryOperstate": ompSummaryOperstate,
       "ompSummaryAdminstate": ompSummaryAdminstate,
       "ompSummaryDevicetype": ompSummaryDevicetype,
       "ompSummaryOmpuptime": ompSummaryOmpuptime,
       "ompSummaryOmpdowntime": ompSummaryOmpdowntime,
       "ompSummaryRoutesReceived": ompSummaryRoutesReceived,
       "ompSummaryRoutesInstalled": ompSummaryRoutesInstalled,
       "ompSummaryRoutesSent": ompSummaryRoutesSent,
       "ompSummaryTlocsReceived": ompSummaryTlocsReceived,
       "ompSummaryTlocsInstalled": ompSummaryTlocsInstalled,
       "ompSummaryTlocsSent": ompSummaryTlocsSent,
       "ompSummaryServicesReceived": ompSummaryServicesReceived,
       "ompSummaryServicesInstalled": ompSummaryServicesInstalled,
       "ompSummaryServicesSent": ompSummaryServicesSent,
       "ompSummaryMcastRoutesReceived": ompSummaryMcastRoutesReceived,
       "ompSummaryMcastRoutesInstalled": ompSummaryMcastRoutesInstalled,
       "ompSummaryMcastRoutesSent": ompSummaryMcastRoutesSent,
       "ompSummaryHelloReceived": ompSummaryHelloReceived,
       "ompSummaryHelloSent": ompSummaryHelloSent,
       "ompSummaryHandshakeReceived": ompSummaryHandshakeReceived,
       "ompSummaryHandshakeSent": ompSummaryHandshakeSent,
       "ompSummaryAlertReceived": ompSummaryAlertReceived,
       "ompSummaryAlertSent": ompSummaryAlertSent,
       "ompSummaryInformReceived": ompSummaryInformReceived,
       "ompSummaryInformSent": ompSummaryInformSent,
       "ompSummaryUpdateReceived": ompSummaryUpdateReceived,
       "ompSummaryUpdateSent": ompSummaryUpdateSent,
       "ompSummaryPolicyReceived": ompSummaryPolicyReceived,
       "ompSummaryPolicySent": ompSummaryPolicySent,
       "ompSummaryPacketsReceived": ompSummaryPacketsReceived,
       "ompSummaryPacketsSent": ompSummaryPacketsSent,
       "ompSummaryVsmartPeers": ompSummaryVsmartPeers,
       "ompSummarySiteType": ompSummarySiteType,
       "ompSummaryMtPeersTable": ompSummaryMtPeersTable,
       "ompSummaryMtPeersEntry": ompSummaryMtPeersEntry,
       "ompSummaryMtPeersTenantId": ompSummaryMtPeersTenantId,
       "ompSummaryMtPeersPeer": ompSummaryMtPeersPeer,
       "ompSummaryMtPeersType": ompSummaryMtPeersType,
       "ompSummaryMtPeersDomainId": ompSummaryMtPeersDomainId,
       "ompSummaryMtPeersSiteId": ompSummaryMtPeersSiteId,
       "ompSummaryMtPeersRegionId": ompSummaryMtPeersRegionId,
       "ompSummaryMtPeersState": ompSummaryMtPeersState,
       "ompSummaryMtPeersVersion": ompSummaryMtPeersVersion,
       "ompSummaryMtPeersLegit": ompSummaryMtPeersLegit,
       "ompSummaryMtPeersUpcount": ompSummaryMtPeersUpcount,
       "ompSummaryMtPeersDowncount": ompSummaryMtPeersDowncount,
       "ompSummaryMtPeersLastuptime": ompSummaryMtPeersLastuptime,
       "ompSummaryMtPeersLastdowntime": ompSummaryMtPeersLastdowntime,
       "ompSummaryMtPeersUpTime": ompSummaryMtPeersUpTime,
       "ompSummaryMtPeersDownTime": ompSummaryMtPeersDownTime,
       "ompSummaryMtPeersHoldtime": ompSummaryMtPeersHoldtime,
       "ompSummaryMtPeersSitepolicy": ompSummaryMtPeersSitepolicy,
       "ompSummaryMtPeersPolicyin": ompSummaryMtPeersPolicyin,
       "ompSummaryMtPeersPolicyout": ompSummaryMtPeersPolicyout,
       "ompSummaryMtPeersGracefulRestart": ompSummaryMtPeersGracefulRestart,
       "ompSummaryMtPeersGracefulRestartInterval": ompSummaryMtPeersGracefulRestartInterval,
       "ompSummaryMtPeersHelloReceived": ompSummaryMtPeersHelloReceived,
       "ompSummaryMtPeersHelloSent": ompSummaryMtPeersHelloSent,
       "ompSummaryMtPeersHandshakeReceived": ompSummaryMtPeersHandshakeReceived,
       "ompSummaryMtPeersHandshakeSent": ompSummaryMtPeersHandshakeSent,
       "ompSummaryMtPeersAlertReceived": ompSummaryMtPeersAlertReceived,
       "ompSummaryMtPeersAlertSent": ompSummaryMtPeersAlertSent,
       "ompSummaryMtPeersInformReceived": ompSummaryMtPeersInformReceived,
       "ompSummaryMtPeersInformSent": ompSummaryMtPeersInformSent,
       "ompSummaryMtPeersUpdateReceived": ompSummaryMtPeersUpdateReceived,
       "ompSummaryMtPeersUpdateSent": ompSummaryMtPeersUpdateSent,
       "ompSummaryMtPeersPolicyReceived": ompSummaryMtPeersPolicyReceived,
       "ompSummaryMtPeersPolicySent": ompSummaryMtPeersPolicySent,
       "ompSummaryMtPeersPacketsReceived": ompSummaryMtPeersPacketsReceived,
       "ompSummaryMtPeersPacketsSent": ompSummaryMtPeersPacketsSent,
       "ompSummaryMtPeersRoutesReceived": ompSummaryMtPeersRoutesReceived,
       "ompSummaryMtPeersRoutesInstalled": ompSummaryMtPeersRoutesInstalled,
       "ompSummaryMtPeersRoutesSent": ompSummaryMtPeersRoutesSent,
       "ompSummaryMtPeersTlocsReceived": ompSummaryMtPeersTlocsReceived,
       "ompSummaryMtPeersTlocsInstalled": ompSummaryMtPeersTlocsInstalled,
       "ompSummaryMtPeersTlocsSent": ompSummaryMtPeersTlocsSent,
       "ompSummaryMtPeersServicesReceived": ompSummaryMtPeersServicesReceived,
       "ompSummaryMtPeersServicesInstalled": ompSummaryMtPeersServicesInstalled,
       "ompSummaryMtPeersServicesSent": ompSummaryMtPeersServicesSent,
       "ompSummaryMtPeersMcastRoutesReceived": ompSummaryMtPeersMcastRoutesReceived,
       "ompSummaryMtPeersMcastRoutesInstalled": ompSummaryMtPeersMcastRoutesInstalled,
       "ompSummaryMtPeersMcastRoutesSent": ompSummaryMtPeersMcastRoutesSent,
       "ompSummaryMtPeersControlUp": ompSummaryMtPeersControlUp,
       "ompSummaryMtPeersStaging": ompSummaryMtPeersStaging,
       "ompSummaryMtPeersRefresh": ompSummaryMtPeersRefresh,
       "ompSummaryMtPeersOverlayId": ompSummaryMtPeersOverlayId,
       "ompSummaryMtPeersRoutesReceivedIPv6": ompSummaryMtPeersRoutesReceivedIPv6,
       "ompSummaryMtPeersRoutesInstalledIPv6": ompSummaryMtPeersRoutesInstalledIPv6,
       "ompSummaryMtPeersRoutesSentIPv6": ompSummaryMtPeersRoutesSentIPv6,
       "ompSummaryMtPeersRoutesReceivedTotal": ompSummaryMtPeersRoutesReceivedTotal,
       "ompSummaryMtPeersRoutesInstalledTotal": ompSummaryMtPeersRoutesInstalledTotal,
       "ompSummaryMtPeersRoutesSentTotal": ompSummaryMtPeersRoutesSentTotal,
       "ompSummaryMtPeersServicesReceivedIPv6": ompSummaryMtPeersServicesReceivedIPv6,
       "ompSummaryMtPeersServicesInstalledIPv6": ompSummaryMtPeersServicesInstalledIPv6,
       "ompSummaryMtPeersServicesSentIPv6": ompSummaryMtPeersServicesSentIPv6,
       "ompRoutesTable": ompRoutesTable,
       "ompRoutesTableFamilyTable": ompRoutesTableFamilyTable,
       "ompRoutesTableFamilyEntry": ompRoutesTableFamilyEntry,
       "ompRoutesTableFamilyAddressFamily": ompRoutesTableFamilyAddressFamily,
       "ompRoutesTableFamilyEntriesTable": ompRoutesTableFamilyEntriesTable,
       "ompRoutesTableFamilyEntriesEntry": ompRoutesTableFamilyEntriesEntry,
       "ompRoutesTableFamilyEntriesTenantId": ompRoutesTableFamilyEntriesTenantId,
       "ompRoutesTableFamilyEntriesVpnId": ompRoutesTableFamilyEntriesVpnId,
       "ompRoutesTableFamilyEntriesPrefix": ompRoutesTableFamilyEntriesPrefix,
       "ompRoutesTableFamilyEntriesReceivedTable": ompRoutesTableFamilyEntriesReceivedTable,
       "ompRoutesTableFamilyEntriesReceivedEntry": ompRoutesTableFamilyEntriesReceivedEntry,
       "ompRoutesTableFamilyEntriesReceivedFromPeer": ompRoutesTableFamilyEntriesReceivedFromPeer,
       "ompRoutesTableFamilyEntriesReceivedPathId": ompRoutesTableFamilyEntriesReceivedPathId,
       "ompRoutesTableFamilyEntriesReceivedLabel": ompRoutesTableFamilyEntriesReceivedLabel,
       "ompRoutesTableFamilyEntriesReceivedStatus": ompRoutesTableFamilyEntriesReceivedStatus,
       "ompRoutesTableFamilyEntriesReceivedLossReason": ompRoutesTableFamilyEntriesReceivedLossReason,
       "ompRoutesTableFamilyEntriesReceivedLostToPeer": ompRoutesTableFamilyEntriesReceivedLostToPeer,
       "ompRoutesTableFamilyEntriesReceivedLostToPathId": ompRoutesTableFamilyEntriesReceivedLostToPathId,
       "ompRoutesTableFamilyEntriesReceivedAttributesTable": ompRoutesTableFamilyEntriesReceivedAttributesTable,
       "ompRoutesTableFamilyEntriesReceivedAttributesEntry": ompRoutesTableFamilyEntriesReceivedAttributesEntry,
       "ompRoutesTableFamilyEntriesReceivedAttributesAttributeType": ompRoutesTableFamilyEntriesReceivedAttributesAttributeType,
       "ompRoutesTableFamilyEntriesReceivedAttributesTlocIp": ompRoutesTableFamilyEntriesReceivedAttributesTlocIp,
       "ompRoutesTableFamilyEntriesReceivedAttributesTlocColor": ompRoutesTableFamilyEntriesReceivedAttributesTlocColor,
       "ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap": ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap,
       "ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol": ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol,
       "ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric": ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric,
       "ompRoutesTableFamilyEntriesReceivedAttributesDomainId": ompRoutesTableFamilyEntriesReceivedAttributesDomainId,
       "ompRoutesTableFamilyEntriesReceivedAttributesSiteId": ompRoutesTableFamilyEntriesReceivedAttributesSiteId,
       "ompRoutesTableFamilyEntriesReceivedAttributesPreference": ompRoutesTableFamilyEntriesReceivedAttributesPreference,
       "ompRoutesTableFamilyEntriesReceivedAttributesTag": ompRoutesTableFamilyEntriesReceivedAttributesTag,
       "ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen": ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen,
       "ompRoutesTableFamilyEntriesReceivedAttributesOriginator": ompRoutesTableFamilyEntriesReceivedAttributesOriginator,
       "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp": ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp,
       "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor": ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor,
       "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap": ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap,
       "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction": ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction,
       "ompRoutesTableFamilyEntriesReceivedAttributesOverlayId": ompRoutesTableFamilyEntriesReceivedAttributesOverlayId,
       "ompRoutesTableFamilyEntriesReceivedAttributesAsPath": ompRoutesTableFamilyEntriesReceivedAttributesAsPath,
       "ompRoutesTableFamilyEntriesReceivedAttributesCommunity": ompRoutesTableFamilyEntriesReceivedAttributesCommunity,
       "ompRoutesTableFamilyEntriesReceivedAttributesRegionId": ompRoutesTableFamilyEntriesReceivedAttributesRegionId,
       "ompRoutesTableFamilyEntriesReceivedAttributesRegionPath": ompRoutesTableFamilyEntriesReceivedAttributesRegionPath,
       "ompRoutesTableFamilyEntriesReceivedAttributesSiteType": ompRoutesTableFamilyEntriesReceivedAttributesSiteType,
       "ompRoutesTableFamilyEntriesAdvertisedTable": ompRoutesTableFamilyEntriesAdvertisedTable,
       "ompRoutesTableFamilyEntriesAdvertisedEntry": ompRoutesTableFamilyEntriesAdvertisedEntry,
       "ompRoutesTableFamilyEntriesAdvertisedToPeer": ompRoutesTableFamilyEntriesAdvertisedToPeer,
       "ompRoutesTableFamilyEntriesAdvertisedPathsTable": ompRoutesTableFamilyEntriesAdvertisedPathsTable,
       "ompRoutesTableFamilyEntriesAdvertisedPathsEntry": ompRoutesTableFamilyEntriesAdvertisedPathsEntry,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId": ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTable": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTable,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto": ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen": ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp": ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor": ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap": ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction": ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesRegionPath,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteType,
       "ompBestMatchRoute": ompBestMatchRoute,
       "ompTlocPaths": ompTlocPaths,
       "ompTlocPathsEntriesTable": ompTlocPathsEntriesTable,
       "ompTlocPathsEntriesEntry": ompTlocPathsEntriesEntry,
       "ompTlocPathsEntriesIp": ompTlocPathsEntriesIp,
       "ompTlocPathsEntriesColor": ompTlocPathsEntriesColor,
       "ompTlocPathsEntriesEncap": ompTlocPathsEntriesEncap,
       "ompTlocPathsEntriesPathsTable": ompTlocPathsEntriesPathsTable,
       "ompTlocPathsEntriesPathsEntry": ompTlocPathsEntriesPathsEntry,
       "ompTlocPathsEntriesPathsIndex": ompTlocPathsEntriesPathsIndex,
       "ompTlocPathsEntriesPathsPreference": ompTlocPathsEntriesPathsPreference,
       "ompTlocPathsEntriesPathsMtu": ompTlocPathsEntriesPathsMtu,
       "ompTlocPathsEntriesPathsBfdStatus": ompTlocPathsEntriesPathsBfdStatus,
       "ompTlocPathsEntriesPathsStatus": ompTlocPathsEntriesPathsStatus,
       "ompTlocPathsEntriesPathsStale": ompTlocPathsEntriesPathsStale,
       "ompTlocPathsEntriesPathsLinksTable": ompTlocPathsEntriesPathsLinksTable,
       "ompTlocPathsEntriesPathsLinksEntry": ompTlocPathsEntriesPathsLinksEntry,
       "ompTlocPathsEntriesPathsLinksLinkIndex": ompTlocPathsEntriesPathsLinksLinkIndex,
       "ompTlocPathsEntriesPathsLinksFromTlocIp": ompTlocPathsEntriesPathsLinksFromTlocIp,
       "ompTlocPathsEntriesPathsLinksFromTlocColor": ompTlocPathsEntriesPathsLinksFromTlocColor,
       "ompTlocPathsEntriesPathsLinksFromTlocEncap": ompTlocPathsEntriesPathsLinksFromTlocEncap,
       "ompTlocPathsEntriesPathsLinksToTlocIp": ompTlocPathsEntriesPathsLinksToTlocIp,
       "ompTlocPathsEntriesPathsLinksToTlocColor": ompTlocPathsEntriesPathsLinksToTlocColor,
       "ompTlocPathsEntriesPathsLinksToTlocEncap": ompTlocPathsEntriesPathsLinksToTlocEncap,
       "ompTlocPathsEntriesPathsLinksLabel": ompTlocPathsEntriesPathsLinksLabel,
       "ompTlocs": ompTlocs,
       "ompTlocsFamilyTable": ompTlocsFamilyTable,
       "ompTlocsFamilyEntry": ompTlocsFamilyEntry,
       "ompTlocsFamilyAddressFamily": ompTlocsFamilyAddressFamily,
       "ompTlocsFamilyEntriesTable": ompTlocsFamilyEntriesTable,
       "ompTlocsFamilyEntriesEntry": ompTlocsFamilyEntriesEntry,
       "ompTlocsFamilyEntriesIp": ompTlocsFamilyEntriesIp,
       "ompTlocsFamilyEntriesColor": ompTlocsFamilyEntriesColor,
       "ompTlocsFamilyEntriesEncap": ompTlocsFamilyEntriesEncap,
       "ompTlocsFamilyEntriesReceivedTable": ompTlocsFamilyEntriesReceivedTable,
       "ompTlocsFamilyEntriesReceivedEntry": ompTlocsFamilyEntriesReceivedEntry,
       "ompTlocsFamilyEntriesReceivedTenantId": ompTlocsFamilyEntriesReceivedTenantId,
       "ompTlocsFamilyEntriesReceivedFromPeer": ompTlocsFamilyEntriesReceivedFromPeer,
       "ompTlocsFamilyEntriesReceivedStatus": ompTlocsFamilyEntriesReceivedStatus,
       "ompTlocsFamilyEntriesReceivedLossReason": ompTlocsFamilyEntriesReceivedLossReason,
       "ompTlocsFamilyEntriesReceivedLostToPeer": ompTlocsFamilyEntriesReceivedLostToPeer,
       "ompTlocsFamilyEntriesReceivedLostToPathId": ompTlocsFamilyEntriesReceivedLostToPathId,
       "ompTlocsFamilyEntriesReceivedAttributesTable": ompTlocsFamilyEntriesReceivedAttributesTable,
       "ompTlocsFamilyEntriesReceivedAttributesEntry": ompTlocsFamilyEntriesReceivedAttributesEntry,
       "ompTlocsFamilyEntriesReceivedAttributesPseudoKey": ompTlocsFamilyEntriesReceivedAttributesPseudoKey,
       "ompTlocsFamilyEntriesReceivedAttributesAttributeType": ompTlocsFamilyEntriesReceivedAttributesAttributeType,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey": ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto": ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi": ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType": ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType": ompTlocsFamilyEntriesReceivedAttributesTlocEncapIntegType,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp": ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort": ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp": ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort": ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp": ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort": ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp": ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort": ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort,
       "ompTlocsFamilyEntriesReceivedAttributesBfdStatus": ompTlocsFamilyEntriesReceivedAttributesBfdStatus,
       "ompTlocsFamilyEntriesReceivedAttributesDomainId": ompTlocsFamilyEntriesReceivedAttributesDomainId,
       "ompTlocsFamilyEntriesReceivedAttributesSiteId": ompTlocsFamilyEntriesReceivedAttributesSiteId,
       "ompTlocsFamilyEntriesReceivedAttributesPreference": ompTlocsFamilyEntriesReceivedAttributesPreference,
       "ompTlocsFamilyEntriesReceivedAttributesTag": ompTlocsFamilyEntriesReceivedAttributesTag,
       "ompTlocsFamilyEntriesReceivedAttributesStale": ompTlocsFamilyEntriesReceivedAttributesStale,
       "ompTlocsFamilyEntriesReceivedAttributesCarrier": ompTlocsFamilyEntriesReceivedAttributesCarrier,
       "ompTlocsFamilyEntriesReceivedAttributesGroups": ompTlocsFamilyEntriesReceivedAttributesGroups,
       "ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen": ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen,
       "ompTlocsFamilyEntriesReceivedAttributesWeight": ompTlocsFamilyEntriesReceivedAttributesWeight,
       "ompTlocsFamilyEntriesReceivedAttributesGenId": ompTlocsFamilyEntriesReceivedAttributesGenId,
       "ompTlocsFamilyEntriesReceivedAttributesVersion": ompTlocsFamilyEntriesReceivedAttributesVersion,
       "ompTlocsFamilyEntriesReceivedAttributesOriginator": ompTlocsFamilyEntriesReceivedAttributesOriginator,
       "ompTlocsFamilyEntriesReceivedAttributesRestrict": ompTlocsFamilyEntriesReceivedAttributesRestrict,
       "ompTlocsFamilyEntriesReceivedAttributesOverlayId": ompTlocsFamilyEntriesReceivedAttributesOverlayId,
       "ompTlocsFamilyEntriesReceivedAttributesBandwidth": ompTlocsFamilyEntriesReceivedAttributesBandwidth,
       "ompTlocsFamilyEntriesReceivedAttributesQosGroup": ompTlocsFamilyEntriesReceivedAttributesQosGroup,
       "ompTlocsFamilyEntriesReceivedAttributesOnDemand": ompTlocsFamilyEntriesReceivedAttributesOnDemand,
       "ompTlocsFamilyEntriesReceivedAttributesBandwidthDmin": ompTlocsFamilyEntriesReceivedAttributesBandwidthDmin,
       "ompTlocsFamilyEntriesReceivedAttributesBandwidthDown": ompTlocsFamilyEntriesReceivedAttributesBandwidthDown,
       "ompTlocsFamilyEntriesReceivedAttributesBandwidthDmax": ompTlocsFamilyEntriesReceivedAttributesBandwidthDmax,
       "ompTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod": ompTlocsFamilyEntriesReceivedAttributesAdaptQosPeriod,
       "ompTlocsFamilyEntriesReceivedAttributesAdaptQosUp": ompTlocsFamilyEntriesReceivedAttributesAdaptQosUp,
       "ompTlocsFamilyEntriesReceivedAttributesSiteType": ompTlocsFamilyEntriesReceivedAttributesSiteType,
       "ompTlocsFamilyEntriesAdvertisedTable": ompTlocsFamilyEntriesAdvertisedTable,
       "ompTlocsFamilyEntriesAdvertisedEntry": ompTlocsFamilyEntriesAdvertisedEntry,
       "ompTlocsFamilyEntriesAdvertisedTenantId": ompTlocsFamilyEntriesAdvertisedTenantId,
       "ompTlocsFamilyEntriesAdvertisedToPeer": ompTlocsFamilyEntriesAdvertisedToPeer,
       "ompTlocsFamilyEntriesAdvertisedAttributesTable": ompTlocsFamilyEntriesAdvertisedAttributesTable,
       "ompTlocsFamilyEntriesAdvertisedAttributesEntry": ompTlocsFamilyEntriesAdvertisedAttributesEntry,
       "ompTlocsFamilyEntriesAdvertisedAttributesAttributeId": ompTlocsFamilyEntriesAdvertisedAttributesAttributeId,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapIntegType,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort,
       "ompTlocsFamilyEntriesAdvertisedAttributesDomainId": ompTlocsFamilyEntriesAdvertisedAttributesDomainId,
       "ompTlocsFamilyEntriesAdvertisedAttributesSiteId": ompTlocsFamilyEntriesAdvertisedAttributesSiteId,
       "ompTlocsFamilyEntriesAdvertisedAttributesPreference": ompTlocsFamilyEntriesAdvertisedAttributesPreference,
       "ompTlocsFamilyEntriesAdvertisedAttributesTag": ompTlocsFamilyEntriesAdvertisedAttributesTag,
       "ompTlocsFamilyEntriesAdvertisedAttributesStale": ompTlocsFamilyEntriesAdvertisedAttributesStale,
       "ompTlocsFamilyEntriesAdvertisedAttributesCarrier": ompTlocsFamilyEntriesAdvertisedAttributesCarrier,
       "ompTlocsFamilyEntriesAdvertisedAttributesGroups": ompTlocsFamilyEntriesAdvertisedAttributesGroups,
       "ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen": ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen,
       "ompTlocsFamilyEntriesAdvertisedAttributesWeight": ompTlocsFamilyEntriesAdvertisedAttributesWeight,
       "ompTlocsFamilyEntriesAdvertisedAttributesGenId": ompTlocsFamilyEntriesAdvertisedAttributesGenId,
       "ompTlocsFamilyEntriesAdvertisedAttributesVersion": ompTlocsFamilyEntriesAdvertisedAttributesVersion,
       "ompTlocsFamilyEntriesAdvertisedAttributesOriginator": ompTlocsFamilyEntriesAdvertisedAttributesOriginator,
       "ompTlocsFamilyEntriesAdvertisedAttributesRestrict": ompTlocsFamilyEntriesAdvertisedAttributesRestrict,
       "ompTlocsFamilyEntriesAdvertisedAttributesOverlayId": ompTlocsFamilyEntriesAdvertisedAttributesOverlayId,
       "ompTlocsFamilyEntriesAdvertisedAttributesBandwidth": ompTlocsFamilyEntriesAdvertisedAttributesBandwidth,
       "ompTlocsFamilyEntriesAdvertisedAttributesQosGroup": ompTlocsFamilyEntriesAdvertisedAttributesQosGroup,
       "ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin": ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmin,
       "ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDown": ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDown,
       "ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax": ompTlocsFamilyEntriesAdvertisedAttributesBandwidthDmax,
       "ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod": ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosPeriod,
       "ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp": ompTlocsFamilyEntriesAdvertisedAttributesAdaptQosUp,
       "ompTlocsFamilyEntriesAdvertisedAttributesOnDemand": ompTlocsFamilyEntriesAdvertisedAttributesOnDemand,
       "ompTlocsFamilyEntriesAdvertisedAttributesSiteType": ompTlocsFamilyEntriesAdvertisedAttributesSiteType,
       "ompServices": ompServices,
       "ompServicesFamilyTable": ompServicesFamilyTable,
       "ompServicesFamilyEntry": ompServicesFamilyEntry,
       "ompServicesFamilyAddressFamily": ompServicesFamilyAddressFamily,
       "ompServicesFamilyEntriesTable": ompServicesFamilyEntriesTable,
       "ompServicesFamilyEntriesEntry": ompServicesFamilyEntriesEntry,
       "ompServicesFamilyEntriesTenantId": ompServicesFamilyEntriesTenantId,
       "ompServicesFamilyEntriesVpnId": ompServicesFamilyEntriesVpnId,
       "ompServicesFamilyEntriesService": ompServicesFamilyEntriesService,
       "ompServicesFamilyEntriesOriginator": ompServicesFamilyEntriesOriginator,
       "ompServicesFamilyEntriesReceivedTable": ompServicesFamilyEntriesReceivedTable,
       "ompServicesFamilyEntriesReceivedEntry": ompServicesFamilyEntriesReceivedEntry,
       "ompServicesFamilyEntriesReceivedFromPeer": ompServicesFamilyEntriesReceivedFromPeer,
       "ompServicesFamilyEntriesReceivedPathId": ompServicesFamilyEntriesReceivedPathId,
       "ompServicesFamilyEntriesReceivedRegionId": ompServicesFamilyEntriesReceivedRegionId,
       "ompServicesFamilyEntriesReceivedLabel": ompServicesFamilyEntriesReceivedLabel,
       "ompServicesFamilyEntriesReceivedStatus": ompServicesFamilyEntriesReceivedStatus,
       "ompServicesFamilyEntriesReceivedLossReason": ompServicesFamilyEntriesReceivedLossReason,
       "ompServicesFamilyEntriesReceivedLostToPeer": ompServicesFamilyEntriesReceivedLostToPeer,
       "ompServicesFamilyEntriesReceivedLostToPathId": ompServicesFamilyEntriesReceivedLostToPathId,
       "ompServicesFamilyEntriesReceivedVrfId": ompServicesFamilyEntriesReceivedVrfId,
       "ompServicesFamilyEntriesAdvertisedTable": ompServicesFamilyEntriesAdvertisedTable,
       "ompServicesFamilyEntriesAdvertisedEntry": ompServicesFamilyEntriesAdvertisedEntry,
       "ompServicesFamilyEntriesAdvertisedToPeer": ompServicesFamilyEntriesAdvertisedToPeer,
       "ompMulticastAutoDiscover": ompMulticastAutoDiscover,
       "ompMulticastAutoDiscoverFamilyTable": ompMulticastAutoDiscoverFamilyTable,
       "ompMulticastAutoDiscoverFamilyEntry": ompMulticastAutoDiscoverFamilyEntry,
       "ompMulticastAutoDiscoverFamilyAddressFamily": ompMulticastAutoDiscoverFamilyAddressFamily,
       "ompMulticastAutoDiscoverFamilyEntriesTable": ompMulticastAutoDiscoverFamilyEntriesTable,
       "ompMulticastAutoDiscoverFamilyEntriesEntry": ompMulticastAutoDiscoverFamilyEntriesEntry,
       "ompMulticastAutoDiscoverFamilyEntriesTenantId": ompMulticastAutoDiscoverFamilyEntriesTenantId,
       "ompMulticastAutoDiscoverFamilyEntriesVpnId": ompMulticastAutoDiscoverFamilyEntriesVpnId,
       "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator": ompMulticastAutoDiscoverFamilyEntriesSourceOriginator,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedTable": ompMulticastAutoDiscoverFamilyEntriesReceivedTable,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedEntry": ompMulticastAutoDiscoverFamilyEntriesReceivedEntry,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer": ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedStatus": ompMulticastAutoDiscoverFamilyEntriesReceivedStatus,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason": ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason,
       "ompMulticastAutoDiscoverFamilyEntriesAdvertisedTable": ompMulticastAutoDiscoverFamilyEntriesAdvertisedTable,
       "ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry": ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry,
       "ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer": ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer,
       "ompMulticastRoutes": ompMulticastRoutes,
       "ompMulticastRoutesFamilyTable": ompMulticastRoutesFamilyTable,
       "ompMulticastRoutesFamilyEntry": ompMulticastRoutesFamilyEntry,
       "ompMulticastRoutesFamilyAddressFamily": ompMulticastRoutesFamilyAddressFamily,
       "ompMulticastRoutesFamilyEntriesTable": ompMulticastRoutesFamilyEntriesTable,
       "ompMulticastRoutesFamilyEntriesEntry": ompMulticastRoutesFamilyEntriesEntry,
       "ompMulticastRoutesFamilyEntriesTenantId": ompMulticastRoutesFamilyEntriesTenantId,
       "ompMulticastRoutesFamilyEntriesType": ompMulticastRoutesFamilyEntriesType,
       "ompMulticastRoutesFamilyEntriesVpnId": ompMulticastRoutesFamilyEntriesVpnId,
       "ompMulticastRoutesFamilyEntriesDestination": ompMulticastRoutesFamilyEntriesDestination,
       "ompMulticastRoutesFamilyEntriesGroup": ompMulticastRoutesFamilyEntriesGroup,
       "ompMulticastRoutesFamilyEntriesSource": ompMulticastRoutesFamilyEntriesSource,
       "ompMulticastRoutesFamilyEntriesSourceOriginator": ompMulticastRoutesFamilyEntriesSourceOriginator,
       "ompMulticastRoutesFamilyEntriesReceivedTable": ompMulticastRoutesFamilyEntriesReceivedTable,
       "ompMulticastRoutesFamilyEntriesReceivedEntry": ompMulticastRoutesFamilyEntriesReceivedEntry,
       "ompMulticastRoutesFamilyEntriesReceivedFromPeer": ompMulticastRoutesFamilyEntriesReceivedFromPeer,
       "ompMulticastRoutesFamilyEntriesReceivedRp": ompMulticastRoutesFamilyEntriesReceivedRp,
       "ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes": ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes,
       "ompMulticastRoutesFamilyEntriesReceivedStatus": ompMulticastRoutesFamilyEntriesReceivedStatus,
       "ompMulticastRoutesFamilyEntriesReceivedLossReason": ompMulticastRoutesFamilyEntriesReceivedLossReason,
       "ompMulticastRoutesFamilyEntriesAdvertisedTable": ompMulticastRoutesFamilyEntriesAdvertisedTable,
       "ompMulticastRoutesFamilyEntriesAdvertisedEntry": ompMulticastRoutesFamilyEntriesAdvertisedEntry,
       "ompMulticastRoutesFamilyEntriesAdvertisedToPeer": ompMulticastRoutesFamilyEntriesAdvertisedToPeer,
       "ompMulticastRoutesFamilyEntriesAdvertisedRp": ompMulticastRoutesFamilyEntriesAdvertisedRp,
       "ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes": ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes,
       "ompCloudexpressRoutes": ompCloudexpressRoutes,
       "ompCloudexpressEntriesTable": ompCloudexpressEntriesTable,
       "ompCloudexpressEntriesEntry": ompCloudexpressEntriesEntry,
       "ompCloudexpressEntriesTenantId": ompCloudexpressEntriesTenantId,
       "ompCloudexpressEntriesVpnId": ompCloudexpressEntriesVpnId,
       "ompCloudexpressEntriesOriginator": ompCloudexpressEntriesOriginator,
       "ompCloudexpressEntriesAppId": ompCloudexpressEntriesAppId,
       "ompCloudexpressEntriesAppType": ompCloudexpressEntriesAppType,
       "ompCloudexpressEntriesSubAppId": ompCloudexpressEntriesSubAppId,
       "ompCloudexpressEntriesAppName": ompCloudexpressEntriesAppName,
       "ompCloudexpressEntriesReceivedTable": ompCloudexpressEntriesReceivedTable,
       "ompCloudexpressEntriesReceivedEntry": ompCloudexpressEntriesReceivedEntry,
       "ompCloudexpressEntriesReceivedFromPeer": ompCloudexpressEntriesReceivedFromPeer,
       "ompCloudexpressEntriesReceivedStatus": ompCloudexpressEntriesReceivedStatus,
       "ompCloudexpressEntriesReceivedLossReason": ompCloudexpressEntriesReceivedLossReason,
       "ompCloudexpressEntriesReceivedLatency": ompCloudexpressEntriesReceivedLatency,
       "ompCloudexpressEntriesReceivedLoss": ompCloudexpressEntriesReceivedLoss,
       "ompCloudexpressEntriesAdvertisedTable": ompCloudexpressEntriesAdvertisedTable,
       "ompCloudexpressEntriesAdvertisedEntry": ompCloudexpressEntriesAdvertisedEntry,
       "ompCloudexpressEntriesAdvertisedToPeer": ompCloudexpressEntriesAdvertisedToPeer,
       "ompCloudexpressEntriesAdvertisedLatency": ompCloudexpressEntriesAdvertisedLatency,
       "ompCloudexpressEntriesAdvertisedLoss": ompCloudexpressEntriesAdvertisedLoss,
       "ciscoSdwanOmpMIBNotifObjects": ciscoSdwanOmpMIBNotifObjects,
       "netconfNotificationSeverity": netconfNotificationSeverity,
       "ciscoSdwanOmpNumberOfVsmarts": ciscoSdwanOmpNumberOfVsmarts,
       "ciscoSdwanOmpNewState": ciscoSdwanOmpNewState,
       "ciscoSdwanOmpPeer": ciscoSdwanOmpPeer,
       "ciscoSdwanOmpPeerNewState": ciscoSdwanOmpPeerNewState,
       "ciscoSdwanOmpPolicy": ciscoSdwanOmpPolicy,
       "ciscoSdwanOmpVsmartPeer": ciscoSdwanOmpVsmartPeer,
       "ciscoSdwanOmpMIBConform": ciscoSdwanOmpMIBConform,
       "ciscoSdwanOmpMIBCompliances": ciscoSdwanOmpMIBCompliances,
       "ciscoSdwanOmpMIBCompliance": ciscoSdwanOmpMIBCompliance,
       "ciscoSdwanOmpMIBGroups": ciscoSdwanOmpMIBGroups,
       "cSdwanOmpNotifObjsGroup": cSdwanOmpNotifObjsGroup,
       "cSdwanOmpNotifsGroup": cSdwanOmpNotifsGroup,
       "cSdwanOmpSummaryObjsGroup": cSdwanOmpSummaryObjsGroup,
       "cSdwanOmpSummaryMtPeersObjsGroup": cSdwanOmpSummaryMtPeersObjsGroup,
       "cSdwanOmpRoutesObjsGroup": cSdwanOmpRoutesObjsGroup,
       "cSdwanOmpTlocPathsObjsGroup": cSdwanOmpTlocPathsObjsGroup,
       "cSdwanOmpTlocsObjsGroup": cSdwanOmpTlocsObjsGroup,
       "cSdwanOmpServicesObjsGroup": cSdwanOmpServicesObjsGroup,
       "cSdwanOmpMulticastAutoDiscoverObjsGroup": cSdwanOmpMulticastAutoDiscoverObjsGroup,
       "cSdwanOmpMulticastRoutesObjsGroup": cSdwanOmpMulticastRoutesObjsGroup,
       "cSdwanOmpCloudexpressRoutesObjsGroup": cSdwanOmpCloudexpressRoutesObjsGroup}
)
