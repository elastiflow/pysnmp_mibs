# SNMP MIB module (IANAifType-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/IANAifType-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 13:03:30 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ianaifType = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 30)
)
if mibBuilder.loadTexts:
    ianaifType.setRevisions(
        ("1996-02-21 11:23",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAifType(TextualConvention, Integer32):
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
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("regular1822", 2),
          ("hdh1822", 3),
          ("ddnX25", 4),
          ("rfc877x25", 5),
          ("ethernetCsmacd", 6),
          ("iso88023Csmacd", 7),
          ("iso88024TokenBus", 8),
          ("iso88025TokenRing", 9),
          ("iso88026Man", 10),
          ("starLan", 11),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("hyperchannel", 14),
          ("fddi", 15),
          ("lapb", 16),
          ("sdlc", 17),
          ("ds1", 18),
          ("e1", 19),
          ("basicISDN", 20),
          ("primaryISDN", 21),
          ("propPointToPointSerial", 22),
          ("ppp", 23),
          ("softwareLoopback", 24),
          ("eon", 25),
          ("ethernet3Mbit", 26),
          ("nsip", 27),
          ("slip", 28),
          ("ultra", 29),
          ("ds3", 30),
          ("sip", 31),
          ("frameRelay", 32),
          ("rs232", 33),
          ("para", 34),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("atm", 37),
          ("miox25", 38),
          ("sonet", 39),
          ("x25ple", 40),
          ("iso88022llc", 41),
          ("localTalk", 42),
          ("smdsDxi", 43),
          ("frameRelayService", 44),
          ("v35", 45),
          ("hssi", 46),
          ("hippi", 47),
          ("modem", 48),
          ("aal5", 49),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("smdsIcip", 52),
          ("propVirtual", 53),
          ("propMultiplexor", 54),
          ("ieee80212", 55),
          ("fibreChannel", 56),
          ("hippiInterface", 57),
          ("frameRelayInterconnect", 58),
          ("aflane8023", 59),
          ("aflane8025", 60),
          ("cctEmul", 61),
          ("fastEther", 62),
          ("isdn", 63),
          ("v11", 64),
          ("v36", 65),
          ("g703at64k", 66),
          ("g703at2mb", 67),
          ("qllc", 68),
          ("fastEtherFX", 69),
          ("channel", 70),
          ("ieee80211", 71),
          ("ibm370parChan", 72),
          ("escon", 73),
          ("dlsw", 74),
          ("isdns", 75),
          ("isdnu", 76),
          ("lapd", 77),
          ("ipSwitch", 78),
          ("rsrb", 79),
          ("atmLogical", 80),
          ("ds0", 81),
          ("ds0Bundle", 82),
          ("bsc", 83),
          ("async", 84),
          ("cnr", 85),
          ("iso88025Dtr", 86),
          ("eplrs", 87),
          ("arap", 88),
          ("propCnls", 89),
          ("hostPad", 90),
          ("termPad", 91),
          ("frameRelayMPI", 92),
          ("x213", 93),
          ("adsl", 94),
          ("radsl", 95),
          ("sdsl", 96),
          ("vdsl", 97),
          ("iso88025CRFPInt", 98),
          ("myrinet", 99),
          ("voiceEM", 100),
          ("voiceFXO", 101),
          ("voiceFXS", 102),
          ("voiceEncap", 103),
          ("voiceOverIp", 104),
          ("atmDxi", 105),
          ("atmFuni", 106),
          ("atmIma", 107),
          ("pppMultilinkBundle", 108),
          ("ipOverCdlc", 109),
          ("ipOverClaw", 110),
          ("stackToStack", 111),
          ("virtualIpAddress", 112),
          ("mpc", 113),
          ("ipOverAtm", 114),
          ("iso88025Fiber", 115),
          ("tdlc", 116),
          ("gigabitEthernet", 117),
          ("hdlc", 118),
          ("lapf", 119),
          ("v37", 120),
          ("x25mlp", 121),
          ("x25huntGroup", 122),
          ("trasnpHdlc", 123),
          ("interleave", 124),
          ("fast", 125),
          ("ip", 126),
          ("docsCableMaclayer", 127),
          ("docsCableDownstream", 128),
          ("docsCableUpstream", 129),
          ("a12MppSwitch", 130),
          ("tunnel", 131),
          ("coffee", 132),
          ("ces", 133),
          ("atmSubInterface", 134),
          ("l2vlan", 135),
          ("l3ipvlan", 136),
          ("l3ipxvlan", 137),
          ("digitalPowerline", 138),
          ("mediaMailOverIp", 139),
          ("dtm", 140),
          ("dcn", 141),
          ("ipForward", 142),
          ("msdsl", 143),
          ("ieee1394", 144))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANAifType-MIB",
    **{"IANAifType": IANAifType,
       "ianaifType": ianaifType}
)
