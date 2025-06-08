# SNMP MIB module (STG-SYSLOG-MIB-REL1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/STG-SYSLOG-MIB-REL1.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:11:01 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stratacom_ObjectIdentity = ObjectIdentity
stratacom = _Stratacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351)
)
_Svplus_ObjectIdentity = ObjectIdentity
svplus = _Svplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1)
)
_StgSyslogMIB_ObjectIdentity = ObjectIdentity
stgSyslogMIB = _StgSyslogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 163)
)
_StgSyslogTrapsGroup_ObjectIdentity = ObjectIdentity
stgSyslogTrapsGroup = _StgSyslogTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1)
)
_StglastSequenceNumber_Type = Integer32
_StglastSequenceNumber_Object = MibScalar
stglastSequenceNumber = _StglastSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 1),
    _StglastSequenceNumber_Type()
)
stglastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stglastSequenceNumber.setStatus("mandatory")


class _StgNodeName_Type(DisplayString):
    """Custom type stgNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StgNodeName_Type.__name__ = "DisplayString"
_StgNodeName_Object = MibScalar
stgNodeName = _StgNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 2),
    _StgNodeName_Type()
)
stgNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNodeName.setStatus("mandatory")


class _StgTrapFacility_Type(Integer32):
    """Custom type stgTrapFacility based on Integer32"""
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
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256)
        )
    )
    namedValues = NamedValues(
        *(("aaaa", 1),
          ("atm", 2),
          ("atmsig", 3),
          ("atmsscop", 4),
          ("controller", 5),
          ("dsx1", 6),
          ("ent-api", 7),
          ("fr", 8),
          ("fr-elmi", 9),
          ("fr-lmi", 10),
          ("ip", 11),
          ("ipfast", 12),
          ("ip-snmp", 13),
          ("link", 14),
          ("lineproto", 15),
          ("sched", 16),
          ("subsys", 17),
          ("sys", 18),
          ("adj", 19),
          ("aip", 20),
          ("alc", 21),
          ("align", 22),
          ("alps", 23),
          ("amdp2-fe", 24),
          ("appn", 25),
          ("arap", 26),
          ("aspp", 27),
          ("at", 28),
          ("atmces", 29),
          ("atmcore", 30),
          ("atmpa", 31),
          ("autorp", 32),
          ("bap", 33),
          ("bgp", 34),
          ("bri", 35),
          ("brimux", 36),
          ("bsc", 37),
          ("bstun", 38),
          ("c1600", 39),
          ("c2600", 40),
          ("c2katm", 41),
          ("c3600", 42),
          ("c542", 43),
          ("c5rsp", 44),
          ("c7200", 45),
          ("call-mgmt", 46),
          ("cbus", 47),
          ("cdm", 48),
          ("ci", 49),
          ("cipdump", 50),
          ("cirrus", 51),
          ("cirrus-pm", 52),
          ("clear", 53),
          ("clns", 54),
          ("cls", 55),
          ("clsdr", 56),
          ("cm622", 57),
          ("comp", 58),
          ("cpad", 59),
          ("cpm", 60),
          ("crypto", 61),
          ("csm", 62),
          ("ct3", 63),
          ("dbconn", 64),
          ("dbus", 65),
          ("dcu", 66),
          ("dec21140", 67),
          ("dialer", 68),
          ("dialshelf", 69),
          ("dlc", 70),
          ("dlsw", 71),
          ("dnet", 72),
          ("drip", 73),
          ("drp", 74),
          ("drvgrp", 75),
          ("dscclock", 76),
          ("dsc-env", 77),
          ("dscextclk", 78),
          ("dsi", 79),
          ("dspu", 80),
          ("dsx0", 81),
          ("dual", 82),
          ("dvmrp", 83),
          ("egp", 84),
          ("envm", 85),
          ("env-mon", 86),
          ("epad", 87),
          ("eswitch", 88),
          ("ethernet", 89),
          ("expression", 90),
          ("fabric", 91),
          ("fb", 92),
          ("fbinfo", 93),
          ("fddi", 94),
          ("filesys", 95),
          ("fpga", 96),
          ("ftc-trunk", 97),
          ("ftpserver", 98),
          ("fw", 99),
          ("grip", 100),
          ("grp", 101),
          ("grppos", 102),
          ("gsr-env", 103),
          ("gsripc", 104),
          ("gt64010", 105),
          ("hawkeye", 106),
          ("hd", 107),
          ("hmm-async", 108),
          ("hood", 109),
          ("hp100vg", 110),
          ("hub", 111),
          ("ibm2692", 112),
          ("idmgr", 113),
          ("idtatm25", 114),
          ("ifs", 115),
          ("igrp", 116),
          ("ilacc", 117),
          ("interface-api", 118),
          ("ipaccess", 119),
          ("ipc", 120),
          ("ipcgrp", 121),
          ("ipclc", 122),
          ("ipc-rsp-cbus", 123),
          ("ipflow", 124),
          ("ipmcast", 125),
          ("iprt", 126),
          ("ipx", 127),
          ("isdn", 128),
          ("lance", 129),
          ("lane", 130),
          ("lanmgr", 131),
          ("lapb", 132),
          ("lat", 133),
          ("lc", 134),
          ("lccef", 135),
          ("lccoredump", 136),
          ("lcinfo", 137),
          ("lclog", 138),
          ("lcplim", 139),
          ("lcpos", 140),
          ("les-fddi", 141),
          ("lex", 142),
          ("llc2", 143),
          ("llist", 144),
          ("lnmc", 145),
          ("lpd", 146),
          ("m32x", 147),
          ("mailbox", 148),
          ("mbri", 149),
          ("mbus", 150),
          ("mbus-sys", 151),
          ("mica", 152),
          ("mif68840", 153),
          ("mimic", 154),
          ("mk5", 155),
          ("mmodem", 156),
          ("modem", 157),
          ("modem-hist", 158),
          ("modem-nv", 159),
          ("mpa68360", 160),
          ("mpoa", 161),
          ("mroute", 162),
          ("mueslix", 163),
          ("network-clock", 164),
          ("nhrp", 165),
          ("nic100", 166),
          ("nim", 167),
          ("oir", 168),
          ("oobp", 169),
          ("ospf", 170),
          ("pa", 171),
          ("pad", 172),
          ("parser", 173),
          ("peruser", 174),
          ("pim", 175),
          ("pnni", 176),
          ("posdw", 177),
          ("ppp", 178),
          ("pquicc", 179),
          ("qa", 180),
          ("qem", 181),
          ("qllc", 182),
          ("quicc", 183),
          ("quicc-async", 184),
          ("quicc-ether", 185),
          ("quicc-serial", 186),
          ("radius", 187),
          ("radix", 188),
          ("rcmd", 189),
          ("rip", 190),
          ("rps", 191),
          ("rsp", 192),
          ("rsrb", 193),
          ("rtt", 194),
          ("s4t68360", 195),
          ("sdlc", 196),
          ("sdllc", 197),
          ("sec", 198),
          ("service", 199),
          ("sgbp", 200),
          ("shelf", 201),
          ("slip", 202),
          ("slotdump", 203),
          ("smf", 204),
          ("smrp", 205),
          ("snapshot", 206),
          ("snmp", 207),
          ("snmp-mgr", 208),
          ("sonet", 209),
          ("sonetmib", 210),
          ("sparc", 211),
          ("sse", 212),
          ("standby", 213),
          ("stun", 214),
          ("sw56", 215),
          ("switch", 216),
          ("sysctlr", 217),
          ("syslog-server", 218),
          ("sysmgt-rpc", 219),
          ("tac", 220),
          ("tagcon", 221),
          ("tbridge", 222),
          ("tcatm", 223),
          ("tcp", 224),
          ("tdm", 225),
          ("tdp", 226),
          ("te-lpdb", 227),
          ("tfib", 228),
          ("ti1570", 229),
          ("tib", 230),
          ("tmq", 231),
          ("tn", 232),
          ("tn3270", 233),
          ("tr", 234),
          ("traffeng", 235),
          ("trunk", 236),
          ("tsp-tunnel", 237),
          ("ttydriver", 238),
          ("tun", 239),
          ("ubr7200", 240),
          ("ucode", 241),
          ("unix", 242),
          ("util", 243),
          ("vines", 244),
          ("vip", 245),
          ("voice-fsm", 246),
          ("voice-rc", 247),
          ("vpdn", 248),
          ("vpm", 249),
          ("x25", 250),
          ("xcpa", 251),
          ("cnses", 252),
          ("pquicc-ether", 253),
          ("pquicc-ethernet", 254),
          ("xtagatm", 255),
          ("vsi-m", 256))
    )


_StgTrapFacility_Type.__name__ = "Integer32"
_StgTrapFacility_Object = MibScalar
stgTrapFacility = _StgTrapFacility_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 3),
    _StgTrapFacility_Type()
)
stgTrapFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTrapFacility.setStatus("mandatory")


class _StgTrapMnemonic_Type(DisplayString):
    """Custom type stgTrapMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StgTrapMnemonic_Type.__name__ = "DisplayString"
_StgTrapMnemonic_Object = MibScalar
stgTrapMnemonic = _StgTrapMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 4),
    _StgTrapMnemonic_Type()
)
stgTrapMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTrapMnemonic.setStatus("mandatory")
_StgTrapMessage_Type = DisplayString
_StgTrapMessage_Object = MibScalar
stgTrapMessage = _StgTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 5),
    _StgTrapMessage_Type()
)
stgTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTrapMessage.setStatus("mandatory")


class _StgTrapSeverity_Type(Integer32):
    """Custom type stgTrapSeverity based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notification", 6),
          ("informational", 7),
          ("debug", 8))
    )


_StgTrapSeverity_Type.__name__ = "Integer32"
_StgTrapSeverity_Object = MibScalar
stgTrapSeverity = _StgTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 6),
    _StgTrapSeverity_Type()
)
stgTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTrapSeverity.setStatus("mandatory")
_StgTrapRepeatCount_Type = Integer32
_StgTrapRepeatCount_Object = MibScalar
stgTrapRepeatCount = _StgTrapRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 7),
    _StgTrapRepeatCount_Type()
)
stgTrapRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTrapRepeatCount.setStatus("mandatory")
_StgTrapTimeStamp_Type = DisplayString
_StgTrapTimeStamp_Object = MibScalar
stgTrapTimeStamp = _StgTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 8),
    _StgTrapTimeStamp_Type()
)
stgTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTrapTimeStamp.setStatus("mandatory")
_StgControllerID_Type = DisplayString
_StgControllerID_Object = MibScalar
stgControllerID = _StgControllerID_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 9),
    _StgControllerID_Type()
)
stgControllerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgControllerID.setStatus("mandatory")
_StgControllerSubID_Type = DisplayString
_StgControllerSubID_Object = MibScalar
stgControllerSubID = _StgControllerSubID_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 10),
    _StgControllerSubID_Type()
)
stgControllerSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgControllerSubID.setStatus("mandatory")


class _StgState_Type(Integer32):
    """Custom type stgState based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("administratively-up", 3),
          ("administratively-down", 4))
    )


_StgState_Type.__name__ = "Integer32"
_StgState_Object = MibScalar
stgState = _StgState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 11),
    _StgState_Type()
)
stgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgState.setStatus("mandatory")


class _StgResult_Type(Integer32):
    """Custom type stgResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("passed", 1),
          ("failed", 2),
          ("empty", 3))
    )


_StgResult_Type.__name__ = "Integer32"
_StgResult_Object = MibScalar
stgResult = _StgResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 12),
    _StgResult_Type()
)
stgResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgResult.setStatus("mandatory")
_StgControllerLoopbackMode_Type = DisplayString
_StgControllerLoopbackMode_Object = MibScalar
stgControllerLoopbackMode = _StgControllerLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 13),
    _StgControllerLoopbackMode_Type()
)
stgControllerLoopbackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgControllerLoopbackMode.setStatus("mandatory")


class _StgLinkID_Type(DisplayString):
    """Custom type stgLinkID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_StgLinkID_Type.__name__ = "DisplayString"
_StgLinkID_Object = MibScalar
stgLinkID = _StgLinkID_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 14),
    _StgLinkID_Type()
)
stgLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgLinkID.setStatus("mandatory")
_StgLinkLoopbackMode_Type = DisplayString
_StgLinkLoopbackMode_Object = MibScalar
stgLinkLoopbackMode = _StgLinkLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 15),
    _StgLinkLoopbackMode_Type()
)
stgLinkLoopbackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgLinkLoopbackMode.setStatus("mandatory")
_StgInterfaceID_Type = DisplayString
_StgInterfaceID_Object = MibScalar
stgInterfaceID = _StgInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 16),
    _StgInterfaceID_Type()
)
stgInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgInterfaceID.setStatus("mandatory")
_StgDLCINumber_Type = Integer32
_StgDLCINumber_Object = MibScalar
stgDLCINumber = _StgDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 17),
    _StgDLCINumber_Type()
)
stgDLCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgDLCINumber.setStatus("mandatory")
_StgATMInterface_Type = DisplayString
_StgATMInterface_Object = MibScalar
stgATMInterface = _StgATMInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 18),
    _StgATMInterface_Type()
)
stgATMInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgATMInterface.setStatus("mandatory")


class _StgTrapReason_Type(Integer32):
    """Custom type stgTrapReason based on Integer32"""
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
              70)
        )
    )
    namedValues = NamedValues(
        *(("emergency-system-unusable", 1),
          ("immediate-action-needed", 2),
          ("critical-condition", 3),
          ("error-condition", 4),
          ("warning-condition", 5),
          ("normal-but-significant-condition", 6),
          ("informational-message-only", 7),
          ("appears-during-debugging-only", 8),
          ("internal-error-sw-or-hw", 9),
          ("internal-software-error", 10),
          ("internal-hardware-error", 11),
          ("fatal-internal-logic-error", 12),
          ("socket-select-failed", 13),
          ("msg-send-to-CA-server-failed", 14),
          ("unable-to-open-socket", 15),
          ("unable-to-open-udp-socket", 16),
          ("unknown-socket-protocol", 17),
          ("socket-bind-failed", 18),
          ("failed-to-create-vc", 19),
          ("not-supported", 20),
          ("unsupported-combination-of-isdn-wan-cards", 21),
          ("unmatched-version", 22),
          ("bad-subsystem-version-number", 23),
          ("kernel-and-subsystem-versions-differ", 24),
          ("probable-mismatch-microcode-version-with-ios", 25),
          ("not-enough-memory", 26),
          ("failed-to-start-periodic-accounting-process", 27),
          ("process-enqueue-failed", 28),
          ("too-many-processes", 29),
          ("failed-to-process-ca-cert", 30),
          ("failed-to-create-process", 31),
          ("process-aborted-bcos-runaway-process", 32),
          ("probably-performance-collector-process-terminated", 33),
          ("entityApiProcess-not-created", 34),
          ("snmp-took-too-long-to-process", 35),
          ("router-config-changed", 36),
          ("internal-inconsistency", 37),
          ("unexpected-event", 38),
          ("session-cleanup-error", 39),
          ("peer-state-machine-operation-failed", 40),
          ("peer-violated-tdp-protocol", 41),
          ("bad-vpi-range", 42),
          ("pie-transimission-failed", 43),
          ("pie-bad-address-length", 44),
          ("pie-bad-metric-length", 45),
          ("pie-bad-metric-list-type", 46),
          ("pie-unknown-type", 47),
          ("pie-unexpected-address-list-type", 48),
          ("pie-unexpected-binding-list-type", 49),
          ("pie-unknown-address-list-type", 50),
          ("pie-unknown-binding-list-type", 51),
          ("hop-count-equaled", 52),
          ("possible-route-loop", 53),
          ("switch-cross-connect-setup-failed", 54),
          ("metric-database-operation-failed", 55),
          ("routing-table-operation-failed", 56),
          ("loop-prevention-control-process-init-failure", 57),
          ("state-machine-operation-failed", 58),
          ("all-available-local-tags-allocated", 59),
          ("delete-path-from-empty-net", 60),
          ("cant-allocate-router-id", 61),
          ("lsa-not-found", 62),
          ("invalid-length-field", 63),
          ("misconfigured-ospf", 64),
          ("invalid-lsa", 65),
          ("unexpected-signalling-message", 66),
          ("unknown-mesage", 67),
          ("invalid-lfn", 68),
          ("invalid-tid", 69),
          ("socket-send-failed", 70))
    )


_StgTrapReason_Type.__name__ = "Integer32"
_StgTrapReason_Object = MibScalar
stgTrapReason = _StgTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 19),
    _StgTrapReason_Type()
)
stgTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTrapReason.setStatus("mandatory")
_StgIOSVersionNumber_Type = Integer32
_StgIOSVersionNumber_Object = MibScalar
stgIOSVersionNumber = _StgIOSVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 20),
    _StgIOSVersionNumber_Type()
)
stgIOSVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgIOSVersionNumber.setStatus("mandatory")
_StgRouterIpAddr_Type = DisplayString
_StgRouterIpAddr_Object = MibScalar
stgRouterIpAddr = _StgRouterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 21),
    _StgRouterIpAddr_Type()
)
stgRouterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgRouterIpAddr.setStatus("mandatory")
_StgRouterConfigFrom_Type = DisplayString
_StgRouterConfigFrom_Object = MibScalar
stgRouterConfigFrom = _StgRouterConfigFrom_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 22),
    _StgRouterConfigFrom_Type()
)
stgRouterConfigFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgRouterConfigFrom.setStatus("mandatory")
_StgRouterConfigBy_Type = DisplayString
_StgRouterConfigBy_Object = MibScalar
stgRouterConfigBy = _StgRouterConfigBy_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 23),
    _StgRouterConfigBy_Type()
)
stgRouterConfigBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgRouterConfigBy.setStatus("mandatory")
_StgRouterConfigByIpAddr_Type = DisplayString
_StgRouterConfigByIpAddr_Object = MibScalar
stgRouterConfigByIpAddr = _StgRouterConfigByIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 24),
    _StgRouterConfigByIpAddr_Type()
)
stgRouterConfigByIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgRouterConfigByIpAddr.setStatus("mandatory")
_StgParentDeviceName_Type = DisplayString
_StgParentDeviceName_Object = MibScalar
stgParentDeviceName = _StgParentDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 25),
    _StgParentDeviceName_Type()
)
stgParentDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgParentDeviceName.setStatus("mandatory")
_StgParentDeviceIp_Type = DisplayString
_StgParentDeviceIp_Object = MibScalar
stgParentDeviceIp = _StgParentDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 26),
    _StgParentDeviceIp_Type()
)
stgParentDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgParentDeviceIp.setStatus("mandatory")
_StgParentDeviceSlotNo_Type = Integer32
_StgParentDeviceSlotNo_Object = MibScalar
stgParentDeviceSlotNo = _StgParentDeviceSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 27),
    _StgParentDeviceSlotNo_Type()
)
stgParentDeviceSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgParentDeviceSlotNo.setStatus("mandatory")
_StgInterface_Type = DisplayString
_StgInterface_Object = MibScalar
stgInterface = _StgInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 28),
    _StgInterface_Type()
)
stgInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgInterface.setStatus("mandatory")
_StgPeerId_Type = Integer32
_StgPeerId_Object = MibScalar
stgPeerId = _StgPeerId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 29),
    _StgPeerId_Type()
)
stgPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgPeerId.setStatus("mandatory")
_StgTagAllocationPool_Type = DisplayString
_StgTagAllocationPool_Object = MibScalar
stgTagAllocationPool = _StgTagAllocationPool_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 30),
    _StgTagAllocationPool_Type()
)
stgTagAllocationPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTagAllocationPool.setStatus("mandatory")
_StgPrefix_Type = DisplayString
_StgPrefix_Object = MibScalar
stgPrefix = _StgPrefix_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 31),
    _StgPrefix_Type()
)
stgPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgPrefix.setStatus("mandatory")
_StgEncapsulationLength_Type = Integer32
_StgEncapsulationLength_Object = MibScalar
stgEncapsulationLength = _StgEncapsulationLength_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 32),
    _StgEncapsulationLength_Type()
)
stgEncapsulationLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgEncapsulationLength.setStatus("mandatory")
_StgTagSize_Type = Integer32
_StgTagSize_Object = MibScalar
stgTagSize = _StgTagSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 33),
    _StgTagSize_Type()
)
stgTagSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTagSize.setStatus("mandatory")
_StgTag_Type = DisplayString
_StgTag_Object = MibScalar
stgTag = _StgTag_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 34),
    _StgTag_Type()
)
stgTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTag.setStatus("mandatory")
_StgIpAddress_Type = DisplayString
_StgIpAddress_Object = MibScalar
stgIpAddress = _StgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 35),
    _StgIpAddress_Type()
)
stgIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgIpAddress.setStatus("mandatory")
_StgNeighbor_Type = DisplayString
_StgNeighbor_Object = MibScalar
stgNeighbor = _StgNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 36),
    _StgNeighbor_Type()
)
stgNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNeighbor.setStatus("mandatory")
_StgPathName_Type = DisplayString
_StgPathName_Object = MibScalar
stgPathName = _StgPathName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 37),
    _StgPathName_Type()
)
stgPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgPathName.setStatus("mandatory")
_StgInfo_Type = DisplayString
_StgInfo_Object = MibScalar
stgInfo = _StgInfo_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 39),
    _StgInfo_Type()
)
stgInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgInfo.setStatus("mandatory")
_StgMaxPathAllowed_Type = Integer32
_StgMaxPathAllowed_Object = MibScalar
stgMaxPathAllowed = _StgMaxPathAllowed_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 40),
    _StgMaxPathAllowed_Type()
)
stgMaxPathAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgMaxPathAllowed.setStatus("mandatory")
_StgCurrPrefixCount_Type = Integer32
_StgCurrPrefixCount_Object = MibScalar
stgCurrPrefixCount = _StgCurrPrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 41),
    _StgCurrPrefixCount_Type()
)
stgCurrPrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurrPrefixCount.setStatus("mandatory")
_StgMaxPrefixCount_Type = Integer32
_StgMaxPrefixCount_Object = MibScalar
stgMaxPrefixCount = _StgMaxPrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 42),
    _StgMaxPrefixCount_Type()
)
stgMaxPrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgMaxPrefixCount.setStatus("mandatory")
_StgVsiVersion_Type = DisplayString
_StgVsiVersion_Object = MibScalar
stgVsiVersion = _StgVsiVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 43),
    _StgVsiVersion_Type()
)
stgVsiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgVsiVersion.setStatus("mandatory")
_StgSession_Type = Integer32
_StgSession_Object = MibScalar
stgSession = _StgSession_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 44),
    _StgSession_Type()
)
stgSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgSession.setStatus("mandatory")
_StgTagInterface_Type = DisplayString
_StgTagInterface_Object = MibScalar
stgTagInterface = _StgTagInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 45),
    _StgTagInterface_Type()
)
stgTagInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTagInterface.setStatus("mandatory")
_StgReason_Type = DisplayString
_StgReason_Object = MibScalar
stgReason = _StgReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 46),
    _StgReason_Type()
)
stgReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgReason.setStatus("mandatory")
_StgTagInterface1_Type = DisplayString
_StgTagInterface1_Object = MibScalar
stgTagInterface1 = _StgTagInterface1_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 47),
    _StgTagInterface1_Type()
)
stgTagInterface1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTagInterface1.setStatus("mandatory")
_StgTagInterface2_Type = DisplayString
_StgTagInterface2_Object = MibScalar
stgTagInterface2 = _StgTagInterface2_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 48),
    _StgTagInterface2_Type()
)
stgTagInterface2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTagInterface2.setStatus("mandatory")
_StgNeighborId_Type = Integer32
_StgNeighborId_Object = MibScalar
stgNeighborId = _StgNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 49),
    _StgNeighborId_Type()
)
stgNeighborId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNeighborId.setStatus("mandatory")
_StgNeighborStatus_Type = DisplayString
_StgNeighborStatus_Object = MibScalar
stgNeighborStatus = _StgNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 50),
    _StgNeighborStatus_Type()
)
stgNeighborStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNeighborStatus.setStatus("mandatory")


class _StgVCState_Type(Integer32):
    """Custom type stgVCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_StgVCState_Type.__name__ = "Integer32"
_StgVCState_Object = MibScalar
stgVCState = _StgVCState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 51),
    _StgVCState_Type()
)
stgVCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgVCState.setStatus("mandatory")
_StgVCId_Type = DisplayString
_StgVCId_Object = MibScalar
stgVCId = _StgVCId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 52),
    _StgVCId_Type()
)
stgVCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgVCId.setStatus("mandatory")
_StgInfoEltType_Type = Integer32
_StgInfoEltType_Object = MibScalar
stgInfoEltType = _StgInfoEltType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 53),
    _StgInfoEltType_Type()
)
stgInfoEltType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgInfoEltType.setStatus("mandatory")
_StgMessageType_Type = DisplayString
_StgMessageType_Object = MibScalar
stgMessageType = _StgMessageType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 54),
    _StgMessageType_Type()
)
stgMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgMessageType.setStatus("mandatory")
_StgApnName_Type = DisplayString
_StgApnName_Object = MibScalar
stgApnName = _StgApnName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 55),
    _StgApnName_Type()
)
stgApnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgApnName.setStatus("mandatory")
_StgTid_Type = DisplayString
_StgTid_Object = MibScalar
stgTid = _StgTid_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 56),
    _StgTid_Type()
)
stgTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgTid.setStatus("mandatory")
_StgMsgLen_Type = Integer32
_StgMsgLen_Object = MibScalar
stgMsgLen = _StgMsgLen_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 163, 1, 57),
    _StgMsgLen_Type()
)
stgMsgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgMsgLen.setStatus("mandatory")

# Managed Objects groups


# Notification objects

stgSyslogEmergencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26001)
)
stgSyslogEmergencyTrap.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogEmergencyTrap.setStatus(
        ""
    )

stgSyslogAlertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26002)
)
stgSyslogAlertTrap.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogAlertTrap.setStatus(
        ""
    )

stgSyslogCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26003)
)
stgSyslogCriticalTrap.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogCriticalTrap.setStatus(
        ""
    )

stgSyslogErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26004)
)
stgSyslogErrorTrap.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogErrorTrap.setStatus(
        ""
    )

stgSyslogWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26005)
)
stgSyslogWarningTrap.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogWarningTrap.setStatus(
        ""
    )

stgSyslogNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26006)
)
stgSyslogNotificationTrap.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogNotificationTrap.setStatus(
        ""
    )

stgSyslogInformationalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26007)
)
stgSyslogInformationalTrap.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogInformationalTrap.setStatus(
        ""
    )

stgSyslogDebugTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26008)
)
stgSyslogDebugTrap.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogDebugTrap.setStatus(
        ""
    )

stgSyslogRouterConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26010)
)
stgSyslogRouterConfigChanged.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterConfigFrom"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterConfigBy"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterConfigByIpAddr"))
)
if mibBuilder.loadTexts:
    stgSyslogRouterConfigChanged.setStatus(
        ""
    )

stgSyslogCtrlrStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26101)
)
stgSyslogCtrlrStateChanged.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgControllerID"),
        ("STG-SYSLOG-MIB-REL1", "stgControllerSubID"),
        ("STG-SYSLOG-MIB-REL1", "stgState"))
)
if mibBuilder.loadTexts:
    stgSyslogCtrlrStateChanged.setStatus(
        ""
    )

stgSyslogCtrlrEnteredRemoteLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26102)
)
stgSyslogCtrlrEnteredRemoteLoopback.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgControllerID"),
        ("STG-SYSLOG-MIB-REL1", "stgControllerSubID"),
        ("STG-SYSLOG-MIB-REL1", "stgState"),
        ("STG-SYSLOG-MIB-REL1", "stgResult"))
)
if mibBuilder.loadTexts:
    stgSyslogCtrlrEnteredRemoteLoopback.setStatus(
        ""
    )

stgSyslogCtrlrLoopStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26103)
)
stgSyslogCtrlrLoopStatusChanged.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgControllerID"),
        ("STG-SYSLOG-MIB-REL1", "stgControllerSubID"),
        ("STG-SYSLOG-MIB-REL1", "stgControllerLoopbackMode"))
)
if mibBuilder.loadTexts:
    stgSyslogCtrlrLoopStatusChanged.setStatus(
        ""
    )

stgSyslogLinkStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26111)
)
stgSyslogLinkStateChanged.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgLinkID"),
        ("STG-SYSLOG-MIB-REL1", "stgState"))
)
if mibBuilder.loadTexts:
    stgSyslogLinkStateChanged.setStatus(
        ""
    )

stgSyslogLinkEnteredRemoteLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26112)
)
stgSyslogLinkEnteredRemoteLoopback.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgLinkID"),
        ("STG-SYSLOG-MIB-REL1", "stgState"),
        ("STG-SYSLOG-MIB-REL1", "stgResult"))
)
if mibBuilder.loadTexts:
    stgSyslogLinkEnteredRemoteLoopback.setStatus(
        ""
    )

stgSyslogLinkLoopStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26113)
)
stgSyslogLinkLoopStatusChanged.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgLinkID"),
        ("STG-SYSLOG-MIB-REL1", "stgLinkLoopbackMode"))
)
if mibBuilder.loadTexts:
    stgSyslogLinkLoopStatusChanged.setStatus(
        ""
    )

stgSyslogLineProtoStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26121)
)
stgSyslogLineProtoStateChanged.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgInterfaceID"),
        ("STG-SYSLOG-MIB-REL1", "stgState"))
)
if mibBuilder.loadTexts:
    stgSyslogLineProtoStateChanged.setStatus(
        ""
    )

stgSyslogfrDLCIstatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26131)
)
stgSyslogfrDLCIstatusChange.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgInterfaceID"),
        ("STG-SYSLOG-MIB-REL1", "stgDLCINumber"),
        ("STG-SYSLOG-MIB-REL1", "stgState"))
)
if mibBuilder.loadTexts:
    stgSyslogfrDLCIstatusChange.setStatus(
        ""
    )

stgSyslogATMSoftStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26141)
)
stgSyslogATMSoftStart.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgATMInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogATMSoftStart.setStatus(
        ""
    )

stgSyslogATMFailedToCreateVC = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26142)
)
stgSyslogATMFailedToCreateVC.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogATMFailedToCreateVC.setStatus(
        ""
    )

stgSyslogATMAddressRegistrationEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26143)
)
stgSyslogATMAddressRegistrationEnabled.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgATMInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogATMAddressRegistrationEnabled.setStatus(
        ""
    )

stgSyslogATMPeerConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26144)
)
stgSyslogATMPeerConfigChanged.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgATMInterface"),
        ("STG-SYSLOG-MIB-REL1", "stgATMInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogATMPeerConfigChanged.setStatus(
        ""
    )

stgSyslogIMLIKeepAliveFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26145)
)
stgSyslogIMLIKeepAliveFailed.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgATMInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogIMLIKeepAliveFailed.setStatus(
        ""
    )

stgSyslogILMIAutoConfigDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26146)
)
stgSyslogILMIAutoConfigDisabled.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgATMInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogILMIAutoConfigDisabled.setStatus(
        ""
    )

stgSyslogATMVCStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26147)
)
stgSyslogATMVCStateChange.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgVCId"),
        ("STG-SYSLOG-MIB-REL1", "stgVCState"))
)
if mibBuilder.loadTexts:
    stgSyslogATMVCStateChange.setStatus(
        ""
    )

stgSyslogSocketError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26201)
)
stgSyslogSocketError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogSocketError.setStatus(
        ""
    )

stgSyslogNotSupportedError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26202)
)
stgSyslogNotSupportedError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogNotSupportedError.setStatus(
        ""
    )

stgSyslogVersionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26203)
)
stgSyslogVersionError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogVersionError.setStatus(
        ""
    )

stgSyslogNoMemoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26204)
)
stgSyslogNoMemoryError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogNoMemoryError.setStatus(
        ""
    )

stgSyslogProcessErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26205)
)
stgSyslogProcessErrors.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogProcessErrors.setStatus(
        ""
    )

stgSyslogDataStructureInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26206)
)
stgSyslogDataStructureInconsistent.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogDataStructureInconsistent.setStatus(
        ""
    )

stgSyslogUnexpectedFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26207)
)
stgSyslogUnexpectedFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogUnexpectedFailure.setStatus(
        ""
    )

stgSyslogNotImplementedError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26208)
)
stgSyslogNotImplementedError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogNotImplementedError.setStatus(
        ""
    )

stgSyslogNodeUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26301)
)
stgSyslogNodeUnreachable.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"))
)
if mibBuilder.loadTexts:
    stgSyslogNodeUnreachable.setStatus(
        ""
    )

stgSyslogNodeReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 26302)
)
stgSyslogNodeReachable.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"))
)
if mibBuilder.loadTexts:
    stgSyslogNodeReachable.setStatus(
        ""
    )

stgSyslogTDPProtocolOperationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27101)
)
stgSyslogTDPProtocolOperationError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTDPProtocolOperationError.setStatus(
        ""
    )

stgSyslogTDPCreateSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27102)
)
stgSyslogTDPCreateSessionFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogTDPCreateSessionFailure.setStatus(
        ""
    )

stgSyslogTDPSessionLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27103)
)
stgSyslogTDPSessionLoss.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgPeerId"))
)
if mibBuilder.loadTexts:
    stgSyslogTDPSessionLoss.setStatus(
        ""
    )

stgSyslogTDPInvalidPIE = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27104)
)
stgSyslogTDPInvalidPIE.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTDPInvalidPIE.setStatus(
        ""
    )

stgSyslogTagDataStructureInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27105)
)
stgSyslogTagDataStructureInitFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTagAllocationPool"))
)
if mibBuilder.loadTexts:
    stgSyslogTagDataStructureInitFailure.setStatus(
        ""
    )

stgSyslogTagLATRevNumWrapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27106)
)
stgSyslogTagLATRevNumWrapped.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"))
)
if mibBuilder.loadTexts:
    stgSyslogTagLATRevNumWrapped.setStatus(
        ""
    )

stgSyslogTCATMTagVirtualCircuitLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27151)
)
stgSyslogTCATMTagVirtualCircuitLost.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTCATMTagVirtualCircuitLost.setStatus(
        ""
    )

stgSyslogTCATMTagInvalidBind = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27152)
)
stgSyslogTCATMTagInvalidBind.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgInterface"),
        ("STG-SYSLOG-MIB-REL1", "stgPrefix"))
)
if mibBuilder.loadTexts:
    stgSyslogTCATMTagInvalidBind.setStatus(
        ""
    )

stgSyslogTCATMLoopdiscoveredInNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27153)
)
stgSyslogTCATMLoopdiscoveredInNetwork.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgPrefix"),
        ("STG-SYSLOG-MIB-REL1", "stgInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogTCATMLoopdiscoveredInNetwork.setStatus(
        ""
    )

stgSyslogTCATMTagSwitchingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27154)
)
stgSyslogTCATMTagSwitchingDisabled.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogTCATMTagSwitchingDisabled.setStatus(
        ""
    )

stgSyslogTCATMTagControlNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27155)
)
stgSyslogTCATMTagControlNotRunning.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"))
)
if mibBuilder.loadTexts:
    stgSyslogTCATMTagControlNotRunning.setStatus(
        ""
    )

stgSyslogTCATMVCResourcesExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27156)
)
stgSyslogTCATMVCResourcesExhausted.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTCATMVCResourcesExhausted.setStatus(
        ""
    )

stgSyslogTrafficEnggOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27201)
)
stgSyslogTrafficEnggOperationFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTrafficEnggOperationFailure.setStatus(
        ""
    )

stgSyslogLoopPreventionDBInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27202)
)
stgSyslogLoopPreventionDBInitFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"))
)
if mibBuilder.loadTexts:
    stgSyslogLoopPreventionDBInitFailure.setStatus(
        ""
    )

stgSyslogTIBOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27251)
)
stgSyslogTIBOperationFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTIBOperationFailure.setStatus(
        ""
    )

stgSyslogTIBInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27252)
)
stgSyslogTIBInitFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"))
)
if mibBuilder.loadTexts:
    stgSyslogTIBInitFailure.setStatus(
        ""
    )

stgSyslogTIBLocalTagAllocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27253)
)
stgSyslogTIBLocalTagAllocationFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgPrefix"))
)
if mibBuilder.loadTexts:
    stgSyslogTIBLocalTagAllocationFailure.setStatus(
        ""
    )

stgSyslogTFIBBadEncapsulation = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27254)
)
stgSyslogTFIBBadEncapsulation.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgEncapsulationLength"),
        ("STG-SYSLOG-MIB-REL1", "stgTagSize"),
        ("STG-SYSLOG-MIB-REL1", "stgTag"))
)
if mibBuilder.loadTexts:
    stgSyslogTFIBBadEncapsulation.setStatus(
        ""
    )

stgSyslogTFIBOperationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27255)
)
stgSyslogTFIBOperationError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTFIBOperationError.setStatus(
        ""
    )

stgSyslogTSPTunnelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27301)
)
stgSyslogTSPTunnelFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTSPTunnelFailure.setStatus(
        ""
    )

stgSyslogBGPPathDeleteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27351)
)
stgSyslogBGPPathDeleteFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPPathDeleteFailure.setStatus(
        ""
    )

stgSyslogBGPOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27352)
)
stgSyslogBGPOperationFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPOperationFailure.setStatus(
        ""
    )

stgSyslogCreateBGPSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27353)
)
stgSyslogCreateBGPSessionFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgNeighbor"))
)
if mibBuilder.loadTexts:
    stgSyslogCreateBGPSessionFailure.setStatus(
        ""
    )

stgSyslogBGPRadixTrieInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27354)
)
stgSyslogBGPRadixTrieInitFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPRadixTrieInitFailure.setStatus(
        ""
    )

stgSyslogBGPRadixTrieAddRouteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27355)
)
stgSyslogBGPRadixTrieAddRouteFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPRadixTrieAddRouteFailure.setStatus(
        ""
    )

stgSyslogBGPRadixTrieDeleteRouteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27356)
)
stgSyslogBGPRadixTrieDeleteRouteFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPRadixTrieDeleteRouteFailure.setStatus(
        ""
    )

stgSyslogBGPNeighborStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27357)
)
stgSyslogBGPNeighborStatusChange.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgNeighborId"),
        ("STG-SYSLOG-MIB-REL1", "stgNeighborStatus"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPNeighborStatusChange.setStatus(
        ""
    )

stgSyslogBGPInvalidASPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27358)
)
stgSyslogBGPInvalidASPath.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgPathName"),
        ("STG-SYSLOG-MIB-REL1", "stgPeerId"),
        ("STG-SYSLOG-MIB-REL1", "stgInfo"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPInvalidASPath.setStatus(
        ""
    )

stgSyslogBGPInvalidMask = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27359)
)
stgSyslogBGPInvalidMask.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgPeerId"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPInvalidMask.setStatus(
        ""
    )

stgSyslogBGPMaxParallelPathExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27360)
)
stgSyslogBGPMaxParallelPathExceeded.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"),
        ("STG-SYSLOG-MIB-REL1", "stgMaxPathAllowed"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPMaxParallelPathExceeded.setStatus(
        ""
    )

stgSyslogBGPPrefixCountThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27361)
)
stgSyslogBGPPrefixCountThresholdCrossed.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgPeerId"),
        ("STG-SYSLOG-MIB-REL1", "stgCurrPrefixCount"),
        ("STG-SYSLOG-MIB-REL1", "stgMaxPrefixCount"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPPrefixCountThresholdCrossed.setStatus(
        ""
    )

stgSyslogBGPMaxPrefixCountExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27362)
)
stgSyslogBGPMaxPrefixCountExceeded.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgPeerId"),
        ("STG-SYSLOG-MIB-REL1", "stgCurrPrefixCount"),
        ("STG-SYSLOG-MIB-REL1", "stgMaxPrefixCount"))
)
if mibBuilder.loadTexts:
    stgSyslogBGPMaxPrefixCountExceeded.setStatus(
        ""
    )

stgSyslogTSCIncompatibleVSIVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27401)
)
stgSyslogTSCIncompatibleVSIVersion.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgVsiVersion"),
        ("STG-SYSLOG-MIB-REL1", "stgSession"),
        ("STG-SYSLOG-MIB-REL1", "stgInterface"))
)
if mibBuilder.loadTexts:
    stgSyslogTSCIncompatibleVSIVersion.setStatus(
        ""
    )

stgSyslogTSCCrossConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27402)
)
stgSyslogTSCCrossConnectFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogTSCCrossConnectFailure.setStatus(
        ""
    )

stgSyslogXTAGATMOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27451)
)
stgSyslogXTAGATMOperationFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogXTAGATMOperationFailure.setStatus(
        ""
    )

stgSyslogXTAGATMCreateControlVCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27452)
)
stgSyslogXTAGATMCreateControlVCFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTagInterface"),
        ("STG-SYSLOG-MIB-REL1", "stgReason"))
)
if mibBuilder.loadTexts:
    stgSyslogXTAGATMCreateControlVCFailure.setStatus(
        ""
    )

stgSyslogXTAGATMVpiOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27453)
)
stgSyslogXTAGATMVpiOutOfRange.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTagInterface"),
        ("STG-SYSLOG-MIB-REL1", "stgReason"))
)
if mibBuilder.loadTexts:
    stgSyslogXTAGATMVpiOutOfRange.setStatus(
        ""
    )

stgSyslogXTAGATMExtPortConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27454)
)
stgSyslogXTAGATMExtPortConflict.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTagInterface1"),
        ("STG-SYSLOG-MIB-REL1", "stgTagInterface2"))
)
if mibBuilder.loadTexts:
    stgSyslogXTAGATMExtPortConflict.setStatus(
        ""
    )

stgSyslogOSPFOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27501)
)
stgSyslogOSPFOperationFailure.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogOSPFOperationFailure.setStatus(
        ""
    )

stgSyslogOSPFLinkStateAdvertisementError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27502)
)
stgSyslogOSPFLinkStateAdvertisementError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogOSPFLinkStateAdvertisementError.setStatus(
        ""
    )

stgSyslogOSPFInvalidPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27503)
)
stgSyslogOSPFInvalidPacket.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogOSPFInvalidPacket.setStatus(
        ""
    )

stgSyslogOSPFNoBacKboneAreaForABR = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27504)
)
stgSyslogOSPFNoBacKboneAreaForABR.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"))
)
if mibBuilder.loadTexts:
    stgSyslogOSPFNoBacKboneAreaForABR.setStatus(
        ""
    )

stgSyslogOSPFUnknownNeighbor = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 27505)
)
stgSyslogOSPFUnknownNeighbor.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgNeighborId"))
)
if mibBuilder.loadTexts:
    stgSyslogOSPFUnknownNeighbor.setStatus(
        ""
    )

stgSyslogGprsGtpMessageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29101)
)
stgSyslogGprsGtpMessageError.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpMessageError.setStatus(
        ""
    )

stgSyslogGprsGtpInvalidGtpHeader = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29102)
)
stgSyslogGprsGtpInvalidGtpHeader.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpInvalidGtpHeader.setStatus(
        ""
    )

syslogGprsGtpInvalidInformationElement = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29103)
)
syslogGprsGtpInvalidInformationElement.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgInfoEltType"),
        ("STG-SYSLOG-MIB-REL1", "stgMessageType"))
)
if mibBuilder.loadTexts:
    syslogGprsGtpInvalidInformationElement.setStatus(
        ""
    )

stgSyslogGprsGtpPDPActivationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29104)
)
stgSyslogGprsGtpPDPActivationFailed.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpPDPActivationFailed.setStatus(
        ""
    )

stgSyslogGprsGtpInvalidAccessPointName = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29105)
)
stgSyslogGprsGtpInvalidAccessPointName.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgApnName"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpInvalidAccessPointName.setStatus(
        ""
    )

stgSyslogGprsGtpPDPContextPurged = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29106)
)
stgSyslogGprsGtpPDPContextPurged.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTid"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpPDPContextPurged.setStatus(
        ""
    )

stgSyslogGprsGtpGTPMessageTooShort = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29107)
)
stgSyslogGprsGtpGTPMessageTooShort.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgMessageType"),
        ("STG-SYSLOG-MIB-REL1", "stgMsgLen"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpGTPMessageTooShort.setStatus(
        ""
    )

stgSyslogResourceExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29108)
)
stgSyslogResourceExhausted.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogResourceExhausted.setStatus(
        ""
    )

stgSyslogGprsGtpGSNPathFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29109)
)
stgSyslogGprsGtpGSNPathFailed.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpGSNPathFailed.setStatus(
        ""
    )

stgSyslogGprsGtpGSNPathRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29110)
)
stgSyslogGprsGtpGSNPathRecovered.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpGSNPathRecovered.setStatus(
        ""
    )

stgSyslogGprsGtpPDPContextActRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29111)
)
stgSyslogGprsGtpPDPContextActRejected.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"),
        ("STG-SYSLOG-MIB-REL1", "stgTid"),
        ("STG-SYSLOG-MIB-REL1", "stgReason"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpPDPContextActRejected.setStatus(
        ""
    )

stgSyslogGprsGtpPrimChargingGatewayUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29112)
)
stgSyslogGprsGtpPrimChargingGatewayUp.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpPrimChargingGatewayUp.setStatus(
        ""
    )

stgSyslogGprsGtpPrimChargingGatewayDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29113)
)
stgSyslogGprsGtpPrimChargingGatewayDown.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpPrimChargingGatewayDown.setStatus(
        ""
    )

stgSyslogGprsGtpSecChargingGatewayUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29114)
)
stgSyslogGprsGtpSecChargingGatewayUp.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpSecChargingGatewayUp.setStatus(
        ""
    )

stgSyslogGprsGtpSecChargingGatewayDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29115)
)
stgSyslogGprsGtpSecChargingGatewayDown.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpSecChargingGatewayDown.setStatus(
        ""
    )

stgSyslogGprsGtpGGSNStartUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29116)
)
stgSyslogGprsGtpGGSNStartUp.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpGGSNStartUp.setStatus(
        ""
    )

stgSyslogGprsGtpGGSNShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29117)
)
stgSyslogGprsGtpGGSNShutdown.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgIpAddress"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpGGSNShutdown.setStatus(
        ""
    )

stgSyslogGprsGtpLocalIpAddressAllocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29118)
)
stgSyslogGprsGtpLocalIpAddressAllocFailed.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpLocalIpAddressAllocFailed.setStatus(
        ""
    )

stgSyslogGprsGtpExtIpAddressAllocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29119)
)
stgSyslogGprsGtpExtIpAddressAllocFailed.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMessage"),
        ("STG-SYSLOG-MIB-REL1", "stgIOSVersionNumber"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpExtIpAddressAllocFailed.setStatus(
        ""
    )

stgSyslogGprsGtpPDPContextTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 29120)
)
stgSyslogGprsGtpPDPContextTimeout.setObjects(
      *(("STG-SYSLOG-MIB-REL1", "stglastSequenceNumber"),
        ("STG-SYSLOG-MIB-REL1", "stgNodeName"),
        ("STG-SYSLOG-MIB-REL1", "stgRouterIpAddr"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapReason"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapFacility"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapSeverity"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapMnemonic"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapRepeatCount"),
        ("STG-SYSLOG-MIB-REL1", "stgTrapTimeStamp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceName"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceIp"),
        ("STG-SYSLOG-MIB-REL1", "stgParentDeviceSlotNo"),
        ("STG-SYSLOG-MIB-REL1", "stgTid"))
)
if mibBuilder.loadTexts:
    stgSyslogGprsGtpPDPContextTimeout.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STG-SYSLOG-MIB-REL1",
    **{"stratacom": stratacom,
       "svplus": svplus,
       "stgSyslogEmergencyTrap": stgSyslogEmergencyTrap,
       "stgSyslogAlertTrap": stgSyslogAlertTrap,
       "stgSyslogCriticalTrap": stgSyslogCriticalTrap,
       "stgSyslogErrorTrap": stgSyslogErrorTrap,
       "stgSyslogWarningTrap": stgSyslogWarningTrap,
       "stgSyslogNotificationTrap": stgSyslogNotificationTrap,
       "stgSyslogInformationalTrap": stgSyslogInformationalTrap,
       "stgSyslogDebugTrap": stgSyslogDebugTrap,
       "stgSyslogRouterConfigChanged": stgSyslogRouterConfigChanged,
       "stgSyslogCtrlrStateChanged": stgSyslogCtrlrStateChanged,
       "stgSyslogCtrlrEnteredRemoteLoopback": stgSyslogCtrlrEnteredRemoteLoopback,
       "stgSyslogCtrlrLoopStatusChanged": stgSyslogCtrlrLoopStatusChanged,
       "stgSyslogLinkStateChanged": stgSyslogLinkStateChanged,
       "stgSyslogLinkEnteredRemoteLoopback": stgSyslogLinkEnteredRemoteLoopback,
       "stgSyslogLinkLoopStatusChanged": stgSyslogLinkLoopStatusChanged,
       "stgSyslogLineProtoStateChanged": stgSyslogLineProtoStateChanged,
       "stgSyslogfrDLCIstatusChange": stgSyslogfrDLCIstatusChange,
       "stgSyslogATMSoftStart": stgSyslogATMSoftStart,
       "stgSyslogATMFailedToCreateVC": stgSyslogATMFailedToCreateVC,
       "stgSyslogATMAddressRegistrationEnabled": stgSyslogATMAddressRegistrationEnabled,
       "stgSyslogATMPeerConfigChanged": stgSyslogATMPeerConfigChanged,
       "stgSyslogIMLIKeepAliveFailed": stgSyslogIMLIKeepAliveFailed,
       "stgSyslogILMIAutoConfigDisabled": stgSyslogILMIAutoConfigDisabled,
       "stgSyslogATMVCStateChange": stgSyslogATMVCStateChange,
       "stgSyslogSocketError": stgSyslogSocketError,
       "stgSyslogNotSupportedError": stgSyslogNotSupportedError,
       "stgSyslogVersionError": stgSyslogVersionError,
       "stgSyslogNoMemoryError": stgSyslogNoMemoryError,
       "stgSyslogProcessErrors": stgSyslogProcessErrors,
       "stgSyslogDataStructureInconsistent": stgSyslogDataStructureInconsistent,
       "stgSyslogUnexpectedFailure": stgSyslogUnexpectedFailure,
       "stgSyslogNotImplementedError": stgSyslogNotImplementedError,
       "stgSyslogNodeUnreachable": stgSyslogNodeUnreachable,
       "stgSyslogNodeReachable": stgSyslogNodeReachable,
       "stgSyslogTDPProtocolOperationError": stgSyslogTDPProtocolOperationError,
       "stgSyslogTDPCreateSessionFailure": stgSyslogTDPCreateSessionFailure,
       "stgSyslogTDPSessionLoss": stgSyslogTDPSessionLoss,
       "stgSyslogTDPInvalidPIE": stgSyslogTDPInvalidPIE,
       "stgSyslogTagDataStructureInitFailure": stgSyslogTagDataStructureInitFailure,
       "stgSyslogTagLATRevNumWrapped": stgSyslogTagLATRevNumWrapped,
       "stgSyslogTCATMTagVirtualCircuitLost": stgSyslogTCATMTagVirtualCircuitLost,
       "stgSyslogTCATMTagInvalidBind": stgSyslogTCATMTagInvalidBind,
       "stgSyslogTCATMLoopdiscoveredInNetwork": stgSyslogTCATMLoopdiscoveredInNetwork,
       "stgSyslogTCATMTagSwitchingDisabled": stgSyslogTCATMTagSwitchingDisabled,
       "stgSyslogTCATMTagControlNotRunning": stgSyslogTCATMTagControlNotRunning,
       "stgSyslogTCATMVCResourcesExhausted": stgSyslogTCATMVCResourcesExhausted,
       "stgSyslogTrafficEnggOperationFailure": stgSyslogTrafficEnggOperationFailure,
       "stgSyslogLoopPreventionDBInitFailure": stgSyslogLoopPreventionDBInitFailure,
       "stgSyslogTIBOperationFailure": stgSyslogTIBOperationFailure,
       "stgSyslogTIBInitFailure": stgSyslogTIBInitFailure,
       "stgSyslogTIBLocalTagAllocationFailure": stgSyslogTIBLocalTagAllocationFailure,
       "stgSyslogTFIBBadEncapsulation": stgSyslogTFIBBadEncapsulation,
       "stgSyslogTFIBOperationError": stgSyslogTFIBOperationError,
       "stgSyslogTSPTunnelFailure": stgSyslogTSPTunnelFailure,
       "stgSyslogBGPPathDeleteFailure": stgSyslogBGPPathDeleteFailure,
       "stgSyslogBGPOperationFailure": stgSyslogBGPOperationFailure,
       "stgSyslogCreateBGPSessionFailure": stgSyslogCreateBGPSessionFailure,
       "stgSyslogBGPRadixTrieInitFailure": stgSyslogBGPRadixTrieInitFailure,
       "stgSyslogBGPRadixTrieAddRouteFailure": stgSyslogBGPRadixTrieAddRouteFailure,
       "stgSyslogBGPRadixTrieDeleteRouteFailure": stgSyslogBGPRadixTrieDeleteRouteFailure,
       "stgSyslogBGPNeighborStatusChange": stgSyslogBGPNeighborStatusChange,
       "stgSyslogBGPInvalidASPath": stgSyslogBGPInvalidASPath,
       "stgSyslogBGPInvalidMask": stgSyslogBGPInvalidMask,
       "stgSyslogBGPMaxParallelPathExceeded": stgSyslogBGPMaxParallelPathExceeded,
       "stgSyslogBGPPrefixCountThresholdCrossed": stgSyslogBGPPrefixCountThresholdCrossed,
       "stgSyslogBGPMaxPrefixCountExceeded": stgSyslogBGPMaxPrefixCountExceeded,
       "stgSyslogTSCIncompatibleVSIVersion": stgSyslogTSCIncompatibleVSIVersion,
       "stgSyslogTSCCrossConnectFailure": stgSyslogTSCCrossConnectFailure,
       "stgSyslogXTAGATMOperationFailure": stgSyslogXTAGATMOperationFailure,
       "stgSyslogXTAGATMCreateControlVCFailure": stgSyslogXTAGATMCreateControlVCFailure,
       "stgSyslogXTAGATMVpiOutOfRange": stgSyslogXTAGATMVpiOutOfRange,
       "stgSyslogXTAGATMExtPortConflict": stgSyslogXTAGATMExtPortConflict,
       "stgSyslogOSPFOperationFailure": stgSyslogOSPFOperationFailure,
       "stgSyslogOSPFLinkStateAdvertisementError": stgSyslogOSPFLinkStateAdvertisementError,
       "stgSyslogOSPFInvalidPacket": stgSyslogOSPFInvalidPacket,
       "stgSyslogOSPFNoBacKboneAreaForABR": stgSyslogOSPFNoBacKboneAreaForABR,
       "stgSyslogOSPFUnknownNeighbor": stgSyslogOSPFUnknownNeighbor,
       "stgSyslogGprsGtpMessageError": stgSyslogGprsGtpMessageError,
       "stgSyslogGprsGtpInvalidGtpHeader": stgSyslogGprsGtpInvalidGtpHeader,
       "syslogGprsGtpInvalidInformationElement": syslogGprsGtpInvalidInformationElement,
       "stgSyslogGprsGtpPDPActivationFailed": stgSyslogGprsGtpPDPActivationFailed,
       "stgSyslogGprsGtpInvalidAccessPointName": stgSyslogGprsGtpInvalidAccessPointName,
       "stgSyslogGprsGtpPDPContextPurged": stgSyslogGprsGtpPDPContextPurged,
       "stgSyslogGprsGtpGTPMessageTooShort": stgSyslogGprsGtpGTPMessageTooShort,
       "stgSyslogResourceExhausted": stgSyslogResourceExhausted,
       "stgSyslogGprsGtpGSNPathFailed": stgSyslogGprsGtpGSNPathFailed,
       "stgSyslogGprsGtpGSNPathRecovered": stgSyslogGprsGtpGSNPathRecovered,
       "stgSyslogGprsGtpPDPContextActRejected": stgSyslogGprsGtpPDPContextActRejected,
       "stgSyslogGprsGtpPrimChargingGatewayUp": stgSyslogGprsGtpPrimChargingGatewayUp,
       "stgSyslogGprsGtpPrimChargingGatewayDown": stgSyslogGprsGtpPrimChargingGatewayDown,
       "stgSyslogGprsGtpSecChargingGatewayUp": stgSyslogGprsGtpSecChargingGatewayUp,
       "stgSyslogGprsGtpSecChargingGatewayDown": stgSyslogGprsGtpSecChargingGatewayDown,
       "stgSyslogGprsGtpGGSNStartUp": stgSyslogGprsGtpGGSNStartUp,
       "stgSyslogGprsGtpGGSNShutdown": stgSyslogGprsGtpGGSNShutdown,
       "stgSyslogGprsGtpLocalIpAddressAllocFailed": stgSyslogGprsGtpLocalIpAddressAllocFailed,
       "stgSyslogGprsGtpExtIpAddressAllocFailed": stgSyslogGprsGtpExtIpAddressAllocFailed,
       "stgSyslogGprsGtpPDPContextTimeout": stgSyslogGprsGtpPDPContextTimeout,
       "stgSyslogMIB": stgSyslogMIB,
       "stgSyslogTrapsGroup": stgSyslogTrapsGroup,
       "stglastSequenceNumber": stglastSequenceNumber,
       "stgNodeName": stgNodeName,
       "stgTrapFacility": stgTrapFacility,
       "stgTrapMnemonic": stgTrapMnemonic,
       "stgTrapMessage": stgTrapMessage,
       "stgTrapSeverity": stgTrapSeverity,
       "stgTrapRepeatCount": stgTrapRepeatCount,
       "stgTrapTimeStamp": stgTrapTimeStamp,
       "stgControllerID": stgControllerID,
       "stgControllerSubID": stgControllerSubID,
       "stgState": stgState,
       "stgResult": stgResult,
       "stgControllerLoopbackMode": stgControllerLoopbackMode,
       "stgLinkID": stgLinkID,
       "stgLinkLoopbackMode": stgLinkLoopbackMode,
       "stgInterfaceID": stgInterfaceID,
       "stgDLCINumber": stgDLCINumber,
       "stgATMInterface": stgATMInterface,
       "stgTrapReason": stgTrapReason,
       "stgIOSVersionNumber": stgIOSVersionNumber,
       "stgRouterIpAddr": stgRouterIpAddr,
       "stgRouterConfigFrom": stgRouterConfigFrom,
       "stgRouterConfigBy": stgRouterConfigBy,
       "stgRouterConfigByIpAddr": stgRouterConfigByIpAddr,
       "stgParentDeviceName": stgParentDeviceName,
       "stgParentDeviceIp": stgParentDeviceIp,
       "stgParentDeviceSlotNo": stgParentDeviceSlotNo,
       "stgInterface": stgInterface,
       "stgPeerId": stgPeerId,
       "stgTagAllocationPool": stgTagAllocationPool,
       "stgPrefix": stgPrefix,
       "stgEncapsulationLength": stgEncapsulationLength,
       "stgTagSize": stgTagSize,
       "stgTag": stgTag,
       "stgIpAddress": stgIpAddress,
       "stgNeighbor": stgNeighbor,
       "stgPathName": stgPathName,
       "stgInfo": stgInfo,
       "stgMaxPathAllowed": stgMaxPathAllowed,
       "stgCurrPrefixCount": stgCurrPrefixCount,
       "stgMaxPrefixCount": stgMaxPrefixCount,
       "stgVsiVersion": stgVsiVersion,
       "stgSession": stgSession,
       "stgTagInterface": stgTagInterface,
       "stgReason": stgReason,
       "stgTagInterface1": stgTagInterface1,
       "stgTagInterface2": stgTagInterface2,
       "stgNeighborId": stgNeighborId,
       "stgNeighborStatus": stgNeighborStatus,
       "stgVCState": stgVCState,
       "stgVCId": stgVCId,
       "stgInfoEltType": stgInfoEltType,
       "stgMessageType": stgMessageType,
       "stgApnName": stgApnName,
       "stgTid": stgTid,
       "stgMsgLen": stgMsgLen}
)
