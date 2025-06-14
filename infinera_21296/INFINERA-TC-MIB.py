# SNMP MIB module (INFINERA-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/infinera_21296/INFINERA-TC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:16 2025
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

(common,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "common")

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

infnTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    infnTextualConventions.setRevisions(
        ("2010-07-09 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FloatArbitraryPrecision(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FloatTenths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class FloatHundredths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class FloatThousandths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class InfnAdminState(TextualConvention, Integer32):
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
        *(("locked", 1),
          ("maintenance", 2),
          ("unlocked", 3))
    )



class InfnArc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("inhibited", 2))
    )



class InfnAvailabilityState(TextualConvention, Integer32):
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
        *(("available", 1),
          ("partiallyAvailable", 2),
          ("unavailable", 3))
    )



class InfnChassisType(TextualConvention, Integer32):
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
        *(("cBand", 1),
          ("lBand", 2),
          ("hybrid", 3),
          ("dtc", 4),
          ("otc", 5),
          ("unknown", 6),
          ("dtcA", 7),
          ("dtcB", 8),
          ("mtcA", 9),
          ("atcA", 10),
          ("atcP", 11))
    )



class InfnCircuitPackType(TextualConvention, Integer32):
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
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("dlm", 2),
          ("bmm", 3),
          ("oam", 4),
          ("mcm", 5),
          ("omm", 6),
          ("scm", 7),
          ("tam", 8),
          ("tom", 9),
          ("xfp", 10),
          ("pem", 11),
          ("fan", 12),
          ("dfb", 13),
          ("chassis", 14),
          ("me", 15),
          ("owm", 16),
          ("tem", 17),
          ("xlm", 18),
          ("ram", 19),
          ("gam", 20),
          ("orm", 21),
          ("dse", 22),
          ("amm", 30),
          ("ofm", 31),
          ("sim", 32),
          ("pcm", 33),
          ("aam", 34),
          ("opsw", 35))
    )



class InfnEqptType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7,
              9,
              11,
              13,
              15,
              17,
              19,
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
              256,
              257,
              258,
              259,
              260,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              433,
              434,
              435,
              436,
              437,
              438,
              439,
              440,
              441,
              442,
              443,
              444,
              445,
              446,
              447,
              448,
              449,
              450,
              451,
              453,
              454,
              455,
              456,
              457,
              458,
              459,
              460,
              461,
              462,
              463,
              464,
              465,
              466,
              467,
              468,
              469,
              470,
              471,
              472,
              473,
              474,
              475,
              476,
              477,
              478,
              479,
              480,
              481,
              482,
              483,
              484,
              485,
              486,
              487,
              488,
              491,
              492,
              493,
              494,
              495)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("bmm4C1", 3),
          ("bmm4C2", 5),
          ("bmm4C3", 7),
          ("bmm4C2ms", 9),
          ("bmm4C3ms", 11),
          ("oamC1", 13),
          ("oamC2", 15),
          ("oamC3", 17),
          ("oamC2ms", 19),
          ("oamC3ms", 21),
          ("dlm1C1", 22),
          ("dlm3C1", 23),
          ("dlm5C1", 24),
          ("dlm7C1", 25),
          ("dlm1C2", 26),
          ("dlm3C2", 27),
          ("dlm5C2", 28),
          ("dlm7C2", 29),
          ("dlm2C1", 30),
          ("dlm4C1", 31),
          ("dlm6C1", 32),
          ("dlm8C1", 33),
          ("dlm2C2", 34),
          ("dlm4C2", 35),
          ("dlm6C2", 36),
          ("dlm8C2", 37),
          ("tam2p10g", 38),
          ("tamOC192", 39),
          ("tam10XG", 40),
          ("tam4p2d5g", 41),
          ("tam4p1g", 42),
          ("tomMrDwdmLR2", 44),
          ("none", 45),
          ("dlm", 46),
          ("bmm", 47),
          ("oam", 48),
          ("mcm", 49),
          ("omm", 50),
          ("scm", 51),
          ("tamUNSUPPORTED", 52),
          ("tomMrCwdmLR2", 53),
          ("ormCxh1MsLL", 54),
          ("pem", 55),
          ("fan", 56),
          ("chassis", 58),
          ("me", 59),
          ("owm", 60),
          ("tom", 61),
          ("tom10gSR1", 62),
          ("tom2d5gSR1", 63),
          ("tom2d5gIR1", 64),
          ("tom622mSR1", 65),
          ("tom1gLX", 66),
          ("tom1gSX", 67),
          ("bmm8C1A", 68),
          ("bmm8C2msA", 69),
          ("bmm8C3msA", 70),
          ("bmm8C1B", 71),
          ("bmm8C2msB", 72),
          ("bmm8C3msB", 73),
          ("bmm4C1B", 74),
          ("bmm4C2msB", 75),
          ("bmm4C3msB", 76),
          ("bmm4C1C", 77),
          ("bmm4C2msC", 78),
          ("bmm4C3msC", 79),
          ("bmm4CX1A", 80),
          ("bmm4CX2msA", 81),
          ("bmm4CX3msA", 82),
          ("bmm8CXH1", 83),
          ("bmm8CXH2ms", 84),
          ("bmm8CXH3ms", 85),
          ("oamC1B", 86),
          ("oamC2msB", 87),
          ("oamC3msB", 88),
          ("oamC1C", 89),
          ("oamC2msC", 90),
          ("oamC3msC", 91),
          ("oamCX1A", 92),
          ("oamCX2msA", 93),
          ("oamCX3msA", 94),
          ("oamCXH1", 95),
          ("oamCXH2ms", 96),
          ("oamCXH3ms", 97),
          ("mcmA", 98),
          ("mcmB", 99),
          ("tom10gIR2", 100),
          ("tom10gLR2", 101),
          ("tom10gSR2", 102),
          ("tom2d5gIR2", 103),
          ("tom2d5gLR2", 104),
          ("tom10gSR0", 105),
          ("tom2d5gmrIR1", 106),
          ("tom40gVSR", 107),
          ("tom1gZX", 108),
          ("tem", 109),
          ("dPemA", 110),
          ("oPemA", 111),
          ("dFantrayB", 112),
          ("oFantrayB", 113),
          ("tam8p1g", 114),
          ("tam4p2d38g", 115),
          ("tam1p40g", 116),
          ("tam2p10gr", 117),
          ("tam2p10gt", 118),
          ("tamFut3", 119),
          ("dIOPANEL", 120),
          ("oIOPANEL", 121),
          ("mFANTRAY", 122),
          ("xlm", 123),
          ("xlm1C2", 124),
          ("xlm2C2", 125),
          ("xlm3C2", 126),
          ("xlm4C2", 127),
          ("xlm5C2", 128),
          ("xlm6C2", 129),
          ("xlm7C2", 130),
          ("xlm8C2", 131),
          ("dlm1C1B", 132),
          ("dlm2C1B", 133),
          ("dlm3C1B", 134),
          ("dlm4C1B", 135),
          ("dlm5C1B", 136),
          ("dlm6C1B", 137),
          ("dlm7C1B", 138),
          ("dlm8C1B", 139),
          ("mIOPANEL", 140),
          ("tom2d5gMRC47LR2", 141),
          ("tom2d5gMRC49LR2", 142),
          ("tom2d5gMRC51LR2", 143),
          ("tom2d5gMRC53LR2", 144),
          ("tom2d5gMRC55LR2", 145),
          ("tom2d5gMRC57LR2", 146),
          ("tom2d5gMRC59LR2", 147),
          ("tom2d5gMRC61LR2", 148),
          ("tom40g", 149),
          ("tom10g", 150),
          ("tom2d5g", 151),
          ("tom2d5gMR", 152),
          ("tom1g", 153),
          ("tom622m", 154),
          ("tom622mMR", 155),
          ("tom155m", 156),
          ("tom10gDL48LR2", 157),
          ("tom10gDQ48LR2", 158),
          ("tom10gDL00LR2", 159),
          ("tom10gDQ00LR2", 160),
          ("tom10gDC01LR2", 161),
          ("tom10gDH01LR2", 162),
          ("tom10gDC61LR2", 163),
          ("tom10gDH61LR2", 164),
          ("tom10gWdm", 165),
          ("tom40GWdm", 166),
          ("bmm1H4CX2", 167),
          ("ram1", 168),
          ("ram2OR", 169),
          ("rem2", 170),
          ("xlm1C3", 171),
          ("xlm2C3", 172),
          ("xlm3C3", 173),
          ("xlm4C3", 174),
          ("xlm5C3", 175),
          ("xlm6C3", 176),
          ("xlm7C3", 177),
          ("xlm8C3", 178),
          ("bmm2p8CXH2ms", 179),
          ("bmm2p8CH3ms", 180),
          ("oamCXH1ms", 181),
          ("gam", 182),
          ("gam1", 183),
          ("dlm1C3", 184),
          ("dlm2C3", 185),
          ("dlm3C3", 186),
          ("dlm4C3", 187),
          ("dlm5C3", 188),
          ("dlm6C3", 189),
          ("dlm7C3", 190),
          ("dlm8C3", 191),
          ("tom10gDWDMLR2", 192),
          ("bmm2h4r3ms", 193),
          ("bmm2h4b3", 194),
          ("bmm2p8ceh3", 195),
          ("axlmT4d1C4", 196),
          ("axlmT4d3C4", 197),
          ("axlmT4d5C4", 198),
          ("axlmT4d7C4", 199),
          ("adlmT4d1C4", 200),
          ("adlmT4d3C4", 201),
          ("adlmT4d5C4", 202),
          ("adlmT4d7C4", 203),
          ("orm", 204),
          ("ormChx1Ms", 205),
          ("dse", 206),
          ("dse1", 207),
          ("axlmT4d1C2", 208),
          ("axlmT4d3C2", 209),
          ("axlmT4d5C2", 210),
          ("axlmT4d7C2", 211),
          ("axlmT4d1C5", 212),
          ("axlmT4d3C5", 213),
          ("axlmT4d5C5", 214),
          ("axlmT4d7C5", 215),
          ("adlmT4d1C2", 216),
          ("adlmT4d3C2", 217),
          ("adlmT4d5C2", 218),
          ("adlmT4d7C2", 219),
          ("adlmT4d1C5", 220),
          ("adlmT4d3C5", 221),
          ("adlmT4d5C5", 222),
          ("adlmT4d7C5", 223),
          ("slmT4d1C3", 224),
          ("slmT4d3C3", 225),
          ("slmT4d5C3", 226),
          ("slmT4d7C3", 227),
          ("slmT4d1C4", 228),
          ("slmT4d3C4", 229),
          ("slmT4d5C4", 230),
          ("slmT4d7C4", 231),
          ("slmT4d1C5", 232),
          ("slmT4d3C5", 233),
          ("slmT4d5C5", 234),
          ("slmT4d7C5", 235),
          ("tam2p10gm", 236),
          ("tam8p2d5gm", 237),
          ("tom2d5gSR0", 238),
          ("tom4gLR1", 239),
          ("tom4gIR11", 240),
          ("tom4gSR0", 241),
          ("tom8gLR1", 242),
          ("tom8gIR1", 243),
          ("tom8gSR0", 244),
          ("tom2d5GMRCnn", 245),
          ("mcmC", 246),
          ("tom1d485gHdRx", 247),
          ("tom1d485gHdTx", 248),
          ("tom1d4835gHdRx", 249),
          ("tom1d4835gHdTx", 250),
          ("tom8gSmLcL", 251),
          ("tom25gmrSR1", 252),
          ("tom10gDwaLR2", 253),
          ("bmm2p8Ch1Ms", 254),
          ("bmm2p8Ceh1", 255),
          ("gam2", 256),
          ("ormCxh1", 257),
          ("tom8g", 258),
          ("scm1", 259),
          ("ormCxh1LL", 260),
          ("amm-a", 300),
          ("amm", 301),
          ("aam-b1", 302),
          ("aam-b2", 303),
          ("aam-p1", 304),
          ("aam-p2", 305),
          ("aam-atn", 306),
          ("aam", 307),
          ("ofm-10-dm", 308),
          ("ofm-10-dm-5059", 309),
          ("ofm-10-dm-4049", 310),
          ("ofm-10-dm-2837", 311),
          ("ofm-10-dm-1827", 312),
          ("ofm-8-cm", 313),
          ("ofm-8-cm-4761", 314),
          ("ofm-4-da", 315),
          ("ofm-4-da-5659", 316),
          ("ofm-4-da-5255", 317),
          ("ofm-4-da-4851", 318),
          ("ofm-4-da-4447", 319),
          ("ofm-4-da-4043", 320),
          ("ofm-4-da-3437", 321),
          ("ofm-4-da-3033", 322),
          ("ofm-4-da-2629", 323),
          ("ofm-4-da-2225", 324),
          ("ofm-4-da-1821", 325),
          ("ofm-2-ca", 326),
          ("ofm-2-ca-4755", 327),
          ("ofm-2-ca-4957", 328),
          ("ofm-2-ca-5159", 329),
          ("ofm-2-ca-5361", 330),
          ("ofm-1-osc-1", 331),
          ("ofm", 332),
          ("sim-1-10g", 333),
          ("sim-2-25gmr", 334),
          ("sim", 335),
          ("a-fan-tray-a", 336),
          ("a-fan", 337),
          ("pcm-ac", 338),
          ("pcm-dc", 339),
          ("pcm", 340),
          ("tom-sfp", 341),
          ("tom2d5gMRD18LR2", 342),
          ("tom2d5gMRD19LR2", 343),
          ("tom2d5gMRD20LR2", 344),
          ("tom2d5gMRD21LR2", 345),
          ("tom2d5gMRD22LR2", 346),
          ("tom2d5gMRD23LR2", 347),
          ("tom2d5gMRD24LR2", 348),
          ("tom2d5gMRD25LR2", 349),
          ("tom2d5gMRD26LR2", 350),
          ("tom2d5gMRD27LR2", 351),
          ("tom2d5gMRD28LR2", 352),
          ("tom2d5gMRD29LR2", 353),
          ("tom2d5gMRD30LR2", 354),
          ("tom2d5gMRD31LR2", 355),
          ("tom2d5gMRD32LR2", 356),
          ("tom2d5gMRD33LR2", 357),
          ("tom2d5gMRD34LR2", 358),
          ("tom2d5gMRD35LR2", 359),
          ("tom2d5gMRD36LR2", 360),
          ("tom2d5gMRD37LR2", 361),
          ("tom2d5gMRD38LR2", 362),
          ("tom2d5gMRD39LR2", 363),
          ("tom2d5gMRD40LR2", 364),
          ("tom2d5gMRD41LR2", 365),
          ("tom2d5gMRD42LR2", 366),
          ("tom2d5gMRD43LR2", 367),
          ("tom2d5gMRD44LR2", 368),
          ("tom2d5gMRD45LR2", 369),
          ("tom2d5gMRD46LR2", 370),
          ("tom2d5gMRD47LR2", 371),
          ("tom2d5gMRD48LR2", 372),
          ("tom2d5gMRD49LR2", 373),
          ("tom2d5gMRD50LR2", 374),
          ("tom2d5gMRD51LR2", 375),
          ("tom2d5gMRD52LR2", 376),
          ("tom2d5gMRD53LR2", 377),
          ("tom2d5gMRD54LR2", 378),
          ("tom2d5gMRD55LR2", 379),
          ("tom2d5gMRD56LR2", 380),
          ("tom2d5gMRD57LR2", 381),
          ("tom2d5gMRD58LR2", 382),
          ("tom2d5gMRD59LR2", 383),
          ("tom100mC45lr2", 384),
          ("tom-1g-cxx-lr2", 385),
          ("tom2d5gMRDdwdm-lr2", 386),
          ("tom2d5gMRDcwdm-lr2", 387),
          ("tom-xfp", 388),
          ("tom10gD18LR2", 389),
          ("tom10gD19LR2", 390),
          ("tom10gD20LR2", 391),
          ("tom10gD21LR2", 392),
          ("tom10gD22LR2", 393),
          ("tom10gD23LR2", 394),
          ("tom10gD24LR2", 395),
          ("tom10gD25LR2", 396),
          ("tom10gD26LR2", 397),
          ("tom10gD27LR2", 398),
          ("tom10gD28LR2", 399),
          ("tom10gD29LR2", 400),
          ("tom10gD30LR2", 401),
          ("tom10gD31LR2", 402),
          ("tom10gD32LR2", 403),
          ("tom10gD33LR2", 404),
          ("tom10gD34LR2", 405),
          ("tom10gD35LR2", 406),
          ("tom10gD36LR2", 407),
          ("tom10gD37LR2", 408),
          ("tom10gD38LR2", 409),
          ("tom10gD39LR2", 410),
          ("tom10gD40LR2", 411),
          ("tom10gD41LR2", 412),
          ("tom10gD42LR2", 413),
          ("tom10gD43LR2", 414),
          ("tom10gD44LR2", 415),
          ("tom10gD45LR2", 416),
          ("tom10gD46LR2", 417),
          ("tom10gD47LR2", 418),
          ("tom10gD48LR2", 419),
          ("tom10gD49LR2", 420),
          ("tom10gD50LR2", 421),
          ("tom10gD51LR2", 422),
          ("tom10gD52LR2", 423),
          ("tom10gD53LR2", 424),
          ("tom10gD54LR2", 425),
          ("tom10gD55LR2", 426),
          ("tom10gD56LR2", 427),
          ("tom10gD57LR2", 428),
          ("tom10gD58LR2", 429),
          ("tom10gD59LR2", 430),
          ("tom10gC51LR2", 431),
          ("tom10gC53LR2", 432),
          ("tom10gC55LR2", 433),
          ("tom10gC57LR2", 434),
          ("tom10gdwaLR2", 435),
          ("tom10gcwdmLR2", 436),
          ("tom2d5gmrSR1", 437),
          ("ofm-4-dav-5659", 438),
          ("ofm-4-dav-5255", 439),
          ("ofm-4-dav-4851", 440),
          ("ofm-4-dav-4447", 441),
          ("ofm-4-dav-4043", 442),
          ("ofm-4-dav-3437", 443),
          ("ofm-4-dav-3033", 444),
          ("ofm-4-dav-2629", 445),
          ("ofm-4-dav-2225", 446),
          ("ofm-4-dav-1821", 447),
          ("ofm-2-dav-5859", 448),
          ("ofm-2-dav-5657", 449),
          ("ofm-2-dav-5455", 450),
          ("ofm-2-dav-5253", 451),
          ("ofm-2-dav-5051", 453),
          ("ofm-2-dav-4849", 454),
          ("ofm-2-dav-4647", 455),
          ("ofm-2-dav-4445", 456),
          ("ofm-2-dav-4243", 457),
          ("ofm-2-dav-4041", 458),
          ("ofm-2-dav-3637", 459),
          ("ofm-2-dav-3435", 460),
          ("ofm-2-dav-3233", 461),
          ("ofm-2-dav-3031", 462),
          ("ofm-2-dav-2829", 463),
          ("ofm-2-dav-2627", 464),
          ("ofm-2-dav-2425", 465),
          ("ofm-2-dav-2223", 466),
          ("ofm-2-dav-2021", 467),
          ("ofm-2-dav-1819", 468),
          ("ofm-1-ca-47", 469),
          ("ofm-1-ca-49", 470),
          ("ofm-1-ca-51", 471),
          ("ofm-1-ca-53", 472),
          ("ofm-1-ca-55", 473),
          ("ofm-1-ca-57", 474),
          ("ofm-1-ca-59", 475),
          ("ofm-1-ca-61", 476),
          ("ofm-6-cdm-4761", 477),
          ("ofm-1-ca", 478),
          ("ofm-1-wdm", 479),
          ("opsw-1", 480),
          ("opsw-2", 481),
          ("sim-t-1-10gt", 482),
          ("tom2d5gMRIR2", 483),
          ("tom2d5gMRLR2", 484),
          ("tom8gXSM-LC-L", 485),
          ("tom10gDtLR2", 486),
          ("sim-a-8-25GMT", 487),
          ("sim-t-1-10gp", 488),
          ("tom1gBaseT", 491),
          ("sim-t-1-10gm", 492),
          ("tom8gSR1", 493),
          ("tom10gC47LR2", 494),
          ("tom10gC49LR2", 495))
    )



class InfnLoopbackType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("terminal", 2),
          ("facility", 3))
    )



class InfnManagedObjectType(TextualConvention, Integer32):
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
              218)
        )
    )
    namedValues = NamedValues(
        *(("acci", 1),
          ("acco", 2),
          ("alarm", 3),
          ("alarmSap", 4),
          ("association", 5),
          ("bandCtp", 6),
          ("bandPtp", 7),
          ("bmm", 8),
          ("bmmOcgPtp", 9),
          ("channelCtp", 10),
          ("chassis", 11),
          ("configTimerAlarm", 12),
          ("ctrlLink", 13),
          ("dbControl", 14),
          ("dcfPtp", 15),
          ("dchCtp", 16),
          ("dlm", 17),
          ("dlmOcgPtp", 18),
          ("dtpCtp", 19),
          ("digitalSncp1Port", 20),
          ("fan", 21),
          ("fanShelf", 22),
          ("gam", 23),
          ("gamOcgPtp", 24),
          ("gigeClientCtp", 25),
          ("gre", 26),
          ("groupTp", 27),
          ("interopCpNeighbor", 28),
          ("interopCpTeInterface", 29),
          ("ioShelf", 30),
          ("internalLink", 31),
          ("lbandPtp", 32),
          ("localSnc", 33),
          ("localSubSnc", 34),
          ("mcm", 35),
          ("me", 36),
          ("nctGigE", 37),
          ("ntpd", 38),
          ("oam", 39),
          ("omm", 40),
          ("oscCtp", 41),
          ("osctCtp", 42),
          ("otsPtp", 43),
          ("owCtp", 44),
          ("owm", 45),
          ("pem", 46),
          ("radiusAuthServer", 47),
          ("ram", 48),
          ("remoteSnc", 49),
          ("remoteSubSnc", 50),
          ("resourceOwner", 51),
          ("sdhClientCtp", 52),
          ("securityProfile", 53),
          ("session", 54),
          ("slot", 55),
          ("sonetClientCtp", 56),
          ("staticRoute", 57),
          ("subClient", 58),
          ("swControl", 59),
          ("tam", 60),
          ("tom", 61),
          ("tribPtp", 62),
          ("tribPtpYcablePg", 63),
          ("teLink", 64),
          ("topoNode", 65),
          ("user", 66),
          ("vcCtp", 67),
          ("vcg", 68),
          ("xcon", 69),
          ("xfr", 70),
          ("xlm", 71),
          ("tem", 72),
          ("snmpCommunity", 73),
          ("snmpAccessList", 74),
          ("snmpConfig", 75),
          ("snmpTrapConfig", 76),
          ("dse", 77),
          ("dsePtp", 78),
          ("gmplsControlChannel", 79),
          ("orm", 80),
          ("osaPtp", 81),
          ("snmpCommunityTable", 82),
          ("snmpNotifyFP", 83),
          ("snmpNotifyFilter", 84),
          ("snmpNotify", 85),
          ("snmpProxy", 86),
          ("snmpTargetAddr", 87),
          ("snmpTargetParams", 88),
          ("snmpUsm", 89),
          ("snmpV3AdminUser", 90),
          ("snmpV3Config", 91),
          ("snmpVacmAccess", 92),
          ("snmpVacmContext", 93),
          ("snmpVacmSecToGroup", 94),
          ("snmpVacmVTFamily", 95),
          ("teEndPoint", 96),
          ("teInterface", 97),
          ("oduClientCtp", 98),
          ("oduktClientCtp", 99),
          ("fcClientCtp", 100),
          ("remoteNe", 101),
          ("scm", 102),
          ("amm", 200),
          ("ofm", 201),
          ("sim", 202),
          ("pcm", 203),
          ("atnOcgPtp", 204),
          ("clitermcfg", 205),
          ("clrChClientCtp", 206),
          ("dcnPtp", 207),
          ("fiberPatch", 208),
          ("hostAccess", 209),
          ("ncPtp", 210),
          ("oscPtp", 211),
          ("otuClientCtp", 212),
          ("stpConfig", 213),
          ("aam", 214),
          ("opsw", 215),
          ("adaptLink", 216),
          ("osncPg", 217),
          ("nmSnc", 218))
    )



class InfnOperationalState(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", 3))
    )



class InfnEnableDisable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class InfnFiberType(TextualConvention, Integer32):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("smf", 2),
          ("eLeaf", 3),
          ("trueWaveReducedSlope", 4),
          ("trueWaveClassic", 5),
          ("ls", 6),
          ("dsf", 7),
          ("pre1993SMF", 8),
          ("originalLEAF", 9),
          ("trueWavePlus", 10),
          ("metroCore", 11),
          ("allwave", 12),
          ("silicaCoreFiber", 13),
          ("terraLight", 14),
          ("fiberPatch", 15))
    )



class InfnDcmType(TextualConvention, Integer32):
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
              41)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dcm1H100N", 2),
          ("dcm1H200N", 3),
          ("dcm1H300N", 4),
          ("dcm1H400N", 5),
          ("dcm1H500N", 6),
          ("dcm1H600N", 7),
          ("dcm1H700N", 8),
          ("dcm1H800N", 9),
          ("dcm1H900N", 10),
          ("dcm1H1000N", 11),
          ("dcm1H1100N", 12),
          ("dcm1H1200N", 13),
          ("dcm1H1300H", 14),
          ("dcm1F1400N", 15),
          ("dcm1F1500N", 16),
          ("dcm1F1600N", 17),
          ("dcm1F1700N", 18),
          ("dcm1F1800N", 19),
          ("dcm1F1900N", 20),
          ("dcm1H100P", 21),
          ("dcm1H200P", 22),
          ("dcm1F300P", 23),
          ("dcm1F400L", 24),
          ("unspecified", 25),
          ("dcm2H3000N", 26),
          ("dcm2H4000N", 27),
          ("dcm1F1700nLL", 28),
          ("dcm1F1900nLL", 29),
          ("dse", 30),
          ("pse1", 31),
          ("pse1b", 32),
          ("dcm3F800S", 33),
          ("dcm3F1000S", 34),
          ("dcm3F1600S", 35),
          ("dcm3F1800S", 36),
          ("pse", 37),
          ("dcm300pPlus100P", 38),
          ("dcm300pPlus200P", 39),
          ("dcm300pPlus300P", 40),
          ("dcm3F150S2", 41))
    )



class InfnOpsQualifierList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ancestorUnavailable", 0),
          ("ancestorLocked", 1),
          ("ancestorFaulted", 2),
          ("ancestorSilenced", 3),
          ("ancestorMaintenance", 4),
          ("ains", 5),
          ("dbUpload", 6),
          ("equipmentNotPresent", 7),
          ("equipmentMismatch", 8),
          ("faulted", 9),
          ("inTest", 10),
          ("loopback", 11),
          ("prbsMon", 12),
          ("prbsGen", 13),
          ("partiallyFaulted", 14),
          ("supportingUnavailbale", 15),
          ("supportingFaulted", 16),
          ("supportingLocked", 17),
          ("supportingSilenced", 18),
          ("supportingMaintenance", 19),
          ("softwareDownload", 20),
          ("turnedOff", 21),
          ("testSigMon", 22),
          ("testSigGen", 23))
    )


class InfnServiceType(TextualConvention, Integer32):
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
              68)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 1),
          ("bw10g", 2),
          ("bw2d5g", 3),
          ("oc48", 4),
          ("oc192", 5),
          ("bwtdm155", 6),
          ("bwtdm622", 7),
          ("stm16", 8),
          ("stm64", 9),
          ("ficon", 10),
          ("escon", 11),
          ("bw10Gbe", 12),
          ("oc3", 13),
          ("oc12", 14),
          ("stm1", 15),
          ("stm4", 16),
          ("bw10Gcc", 17),
          ("bw1Gbe", 18),
          ("bw2d5Gcc", 19),
          ("bw2d38Gcc", 20),
          ("bw1G", 21),
          ("bw2x1GbeChan", 22),
          ("bw40g", 23),
          ("stm256", 24),
          ("stm256L1", 25),
          ("stm256L2", 26),
          ("stm256L3", 27),
          ("stm256L4", 28),
          ("oc768", 29),
          ("oc768L1", 30),
          ("oc768L2", 31),
          ("oc768L3", 32),
          ("oc768L4", 33),
          ("bw4xoc192", 34),
          ("bw4xstm64", 35),
          ("bw10Gdtf", 36),
          ("bw1Gfc", 37),
          ("bw2Gfc", 38),
          ("bw4Gfc", 39),
          ("bw4Gcc", 40),
          ("bw8Gfc", 41),
          ("bw10Gfc", 42),
          ("otu1", 43),
          ("otu2", 44),
          ("otu1e", 45),
          ("otu2e", 46),
          ("odu1", 47),
          ("odu1e", 48),
          ("odu2", 49),
          ("odu2e", 50),
          ("dv6000", 51),
          ("escon200Mcc", 52),
          ("ib2d5Gcc", 53),
          ("ib10Gcc", 54),
          ("hd1d485Gcc", 55),
          ("hd1d483Gcc", 56),
          ("sd270Mcc", 57),
          ("dvb270Mcc", 58),
          ("hdSdi3GPal", 59),
          ("hdSdi3GNtsc", 60),
          ("bw4Gig", 61),
          ("bw8Gig", 62),
          ("bw1d25g", 63),
          ("otu2f", 64),
          ("odu2f", 65),
          ("bwVideo270", 66),
          ("bw4GFc1", 67),
          ("bw4GFc2", 68))
    )



class InfnServiceTypeList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("notSet", 0),
          ("bw10g", 1),
          ("bw2d5g", 2),
          ("oc48", 3),
          ("oc192", 4),
          ("bwtdm155", 5),
          ("bwtdm622", 6),
          ("stm16", 7),
          ("stm64", 8),
          ("ficon", 9),
          ("escon", 10),
          ("bw10Gbe", 11),
          ("oc3", 12),
          ("oc12", 13),
          ("stm1", 14),
          ("stm4", 15),
          ("bw10Gcc", 16),
          ("bw1Gbe", 17),
          ("bw2d5Gcc", 18),
          ("bw2d38Gcc", 19),
          ("bw1G", 20),
          ("bw2x1GbeChan", 21),
          ("bw40g", 22),
          ("stm256", 23),
          ("stm256L1", 24),
          ("stm256L2", 25),
          ("stm256L3", 26),
          ("stm256L4", 27),
          ("oc768", 28),
          ("oc768L1", 29),
          ("oc768L2", 30),
          ("oc768L3", 31),
          ("oc768L4", 32),
          ("bw4xoc192", 33),
          ("bw4xstm64", 34),
          ("bw10Gdtf", 35),
          ("bw1Gfc", 36),
          ("bw2Gfc", 37),
          ("bw4Gfc", 38),
          ("bw4Gcc", 39),
          ("bw8Gfc", 40),
          ("bw10Gfc", 41),
          ("otu1", 42),
          ("otu2", 43),
          ("otu1e", 44),
          ("otu2e", 45),
          ("odu1", 46),
          ("odu1e", 47),
          ("odu2", 48),
          ("odu2e", 49),
          ("dv6000", 50),
          ("escon200Mcc", 51),
          ("ib2d5Gcc", 52),
          ("ib10Gcc", 53),
          ("hd1d485Gcc", 54),
          ("hd1d483Gcc", 55),
          ("sd270Mcc", 56),
          ("dvb270Mcc", 57),
          ("hdSdi3GPal", 58),
          ("hdSdi3GNtsc", 59),
          ("bw4g", 60),
          ("bw8g", 61),
          ("bw1d25g", 62),
          ("otu2f", 63),
          ("odu2f", 64),
          ("bwVideo270", 65),
          ("bw4GFc1", 66),
          ("bw4GFc2", 67))
    )


class InfnFanSpeed(TextualConvention, Integer32):
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
        *(("low", 1),
          ("mid", 2),
          ("high", 3),
          ("unknown", 4))
    )



class InfnSimPayloadWrapperType(TextualConvention, Integer32):
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
        *(("otu", 1),
          ("dtf", 2),
          ("none", 3),
          ("unknown", 4))
    )



class InfnDcnSpeed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s10M", 1),
          ("s100M", 2))
    )



class InfnStpForwardingState(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("listening", 2),
          ("learning", 3),
          ("forwarding", 4),
          ("blocking", 5))
    )



class InfnGigeMaxPacketLen(TextualConvention, Integer32):
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
        *(("standard1518", 1),
          ("jumbo9216", 2),
          ("extremeJumbo18742", 3))
    )



class InfnOtuFecModeType(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("g709", 2),
          ("enhanced", 3))
    )



class InfnOtuTimReptMode(TextualConvention, Integer32):
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
        *(("off", 1),
          ("dapi", 2),
          ("sapi", 3),
          ("dapiSapi", 4))
    )



class InfnJ0TraceMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("overwrite", 2))
    )



class InfnJ0MessageCompliance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gr253r3", 1),
          ("ansiitu", 2))
    )



class InfnTribDisableAction(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("turnOffLaser", 1),
          ("sendAISL", 2),
          ("sendIDLE", 3),
          ("none", 4),
          ("disableTransmitter", 5),
          ("sendNOS", 6),
          ("sendAllZero", 7))
    )



class InfnServiceProvUsage(TextualConvention, Integer32):
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
        *(("inUse", 1),
          ("notInUse", 2),
          ("unknown", 3))
    )



class InfnCurrentDcnGatewayType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class InfnPhyConnDcnGwType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("primaryGw", 2),
          ("secondaryGw", 3))
    )



class InfnTestPattern(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("crpat", 2),
          ("cjtpat", 3),
          ("jspat", 4),
          ("jtspat", 5),
          ("prts1", 6),
          ("prts2", 7),
          ("sqwave", 8),
          ("prbs31", 9))
    )



class InfnSampleDuration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )



class InfnTcmList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tcm1Fac", 0),
          ("tcm1Term", 1),
          ("tcm2Fac", 2),
          ("tcm2Term", 3),
          ("tcm3Fac", 4),
          ("tcm3Term", 5),
          ("tcm4Fac", 6),
          ("tcm4Term", 7),
          ("tcm5Fac", 8),
          ("tcm5Term", 9),
          ("tcm6Fac", 10),
          ("tcm6Term", 11))
    )


class InfnOcgChannelMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ch1", 0),
          ("ch2", 1),
          ("ch3", 2),
          ("ch4", 3),
          ("ch5", 4),
          ("ch6", 5),
          ("ch7", 6),
          ("ch8", 7),
          ("ch9", 8),
          ("ch10", 9))
    )


class InfnServiceMode(TextualConvention, Integer32):
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
        *(("none", 1),
          ("adaptation", 2),
          ("transport", 3))
    )



class InfnMonitoringMode(TextualConvention, Integer32):
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
        *(("unused", 1),
          ("nim", 2),
          ("lim", 3),
          ("im", 4))
    )



class InfnValidityBitmap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("all", 0),
          ("fec", 1),
          ("rxOtu", 2),
          ("txOtu", 3),
          ("prbs", 4))
    )


class InfnOtuSMQ(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("odu1", 2),
          ("odu1e", 3),
          ("odu2", 4),
          ("odu2e", 5),
          ("withoutFecErrorFwd", 6),
          ("withFecErrorFwd", 7))
    )



class InfnOduSMQ(TextualConvention, Integer32):
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
        *(("none", 1),
          ("smqOc192", 2),
          ("smqStm64", 3),
          ("smq10Gbe", 4),
          ("smqOc48", 5),
          ("smqStm16", 6))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TC-MIB",
    **{"FloatArbitraryPrecision": FloatArbitraryPrecision,
       "FloatTenths": FloatTenths,
       "FloatHundredths": FloatHundredths,
       "FloatThousandths": FloatThousandths,
       "InfnAdminState": InfnAdminState,
       "InfnArc": InfnArc,
       "InfnAvailabilityState": InfnAvailabilityState,
       "InfnChassisType": InfnChassisType,
       "InfnCircuitPackType": InfnCircuitPackType,
       "InfnEqptType": InfnEqptType,
       "InfnLoopbackType": InfnLoopbackType,
       "InfnManagedObjectType": InfnManagedObjectType,
       "InfnOperationalState": InfnOperationalState,
       "InfnEnableDisable": InfnEnableDisable,
       "InfnFiberType": InfnFiberType,
       "InfnDcmType": InfnDcmType,
       "InfnOpsQualifierList": InfnOpsQualifierList,
       "InfnServiceType": InfnServiceType,
       "InfnServiceTypeList": InfnServiceTypeList,
       "InfnFanSpeed": InfnFanSpeed,
       "InfnSimPayloadWrapperType": InfnSimPayloadWrapperType,
       "InfnDcnSpeed": InfnDcnSpeed,
       "InfnStpForwardingState": InfnStpForwardingState,
       "InfnGigeMaxPacketLen": InfnGigeMaxPacketLen,
       "InfnOtuFecModeType": InfnOtuFecModeType,
       "InfnOtuTimReptMode": InfnOtuTimReptMode,
       "InfnJ0TraceMode": InfnJ0TraceMode,
       "InfnJ0MessageCompliance": InfnJ0MessageCompliance,
       "InfnTribDisableAction": InfnTribDisableAction,
       "InfnServiceProvUsage": InfnServiceProvUsage,
       "InfnCurrentDcnGatewayType": InfnCurrentDcnGatewayType,
       "InfnPhyConnDcnGwType": InfnPhyConnDcnGwType,
       "InfnTestPattern": InfnTestPattern,
       "InfnSampleDuration": InfnSampleDuration,
       "InfnTcmList": InfnTcmList,
       "InfnOcgChannelMap": InfnOcgChannelMap,
       "InfnServiceMode": InfnServiceMode,
       "InfnMonitoringMode": InfnMonitoringMode,
       "InfnValidityBitmap": InfnValidityBitmap,
       "InfnOtuSMQ": InfnOtuSMQ,
       "InfnOduSMQ": InfnOduSMQ,
       "infnTextualConventions": infnTextualConventions}
)
