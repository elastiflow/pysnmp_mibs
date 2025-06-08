# SNMP MIB module (EION-LPLUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/eion_34226/EION-LPLUS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:58:48 2025
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

(eionMIB,) = mibBuilder.importSymbols(
    "EION-SYSTEM-MIB",
    "eionMIB")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

libraPlusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 2)
)
if mibBuilder.loadTexts:
    libraPlusMIB.setRevisions(
        ("2013-03-31 00:00",
         "1970-01-01 00:00",
         "2011-10-31 00:00",
         "2010-12-31 00:00",
         "2009-05-28 00:00",
         "2008-04-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EionACLType(TextualConvention, Integer32):
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
        *(("notInUse", 0),
          ("whiteList", 1),
          ("blackList", 2))
    )



class LibraPlusLinkStatus(TextualConvention, Integer32):
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



class LibraPlusAPMode(TextualConvention, Integer32):
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
        *(("master", 1),
          ("station", 2),
          ("monitor", 3))
    )



class LibraPlusAuthType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("ccmp", 2),
          ("tkip", 3),
          ("wep", 4))
    )



class LibraPlusAuthMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("shared", 2))
    )



class LibraPlusAuthKeySource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("string", 2))
    )



class LibraPlusOperMode(TextualConvention, Integer32):
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
        *(("normal", 0),
          ("turbo", 1),
          ("half", 2),
          ("quarter", 3))
    )



class LibraPlusWirelessCountryCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              12,
              31,
              32,
              36,
              40,
              48,
              51,
              52,
              56,
              68,
              76,
              84,
              96,
              100,
              112,
              116,
              124,
              152,
              156,
              158,
              170,
              188,
              191,
              196,
              200,
              203,
              208,
              214,
              218,
              222,
              233,
              234,
              246,
              250,
              268,
              276,
              300,
              320,
              340,
              344,
              348,
              352,
              356,
              360,
              364,
              368,
              372,
              376,
              380,
              388,
              392,
              393,
              394,
              395,
              398,
              400,
              404,
              408,
              410,
              411,
              414,
              422,
              428,
              434,
              438,
              440,
              442,
              446,
              458,
              484,
              492,
              504,
              506,
              512,
              528,
              554,
              558,
              578,
              586,
              591,
              600,
              604,
              608,
              616,
              620,
              630,
              634,
              642,
              643,
              682,
              702,
              703,
              704,
              705,
              710,
              716,
              724,
              752,
              756,
              760,
              764,
              780,
              784,
              788,
              792,
              804,
              807,
              818,
              826,
              840,
              858,
              860,
              862,
              887,
              918,
              998,
              999,
              1356,
              2356,
              5010,
              5011,
              5013,
              5014,
              5015,
              5016,
              5017,
              5018,
              5019,
              5020,
              5021,
              5022)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("albania", 8),
          ("algeria", 12),
          ("azerbaijan", 31),
          ("argentina", 32),
          ("australia", 36),
          ("austria", 40),
          ("bahrain", 48),
          ("armenia", 51),
          ("mexicoMexico", 52),
          ("belgium", 56),
          ("bolivia", 68),
          ("brazil", 76),
          ("belize", 84),
          ("bruneiDarussalam", 96),
          ("bulgaria", 100),
          ("belarus", 112),
          ("cambodia", 116),
          ("canada", 124),
          ("chile", 152),
          ("china", 156),
          ("taiwan", 158),
          ("colombia", 170),
          ("costaRica", 188),
          ("croatia", 191),
          ("cyprus", 196),
          ("nigeria", 200),
          ("czech", 203),
          ("denmark", 208),
          ("dominicanRepublic", 214),
          ("ecuador", 218),
          ("elSalvador", 222),
          ("estonia", 233),
          ("faeroeIslands", 234),
          ("finland", 246),
          ("france", 250),
          ("georgia", 268),
          ("germany", 276),
          ("greece", 300),
          ("guatemala", 320),
          ("honduras", 340),
          ("hongKong", 344),
          ("hungary", 348),
          ("iceland", 352),
          ("india", 356),
          ("indonesia", 360),
          ("iran", 364),
          ("iraq", 368),
          ("ireland", 372),
          ("israel", 376),
          ("italy", 380),
          ("jamaica", 388),
          ("japan", 392),
          ("japan1", 393),
          ("japan2", 394),
          ("japan3", 395),
          ("kazakhstan", 398),
          ("jordan", 400),
          ("kenya", 404),
          ("koreaNorth", 408),
          ("koreaRoc", 410),
          ("koreaRoc2", 411),
          ("kuwait", 414),
          ("lebanon", 422),
          ("latvia", 428),
          ("libya", 434),
          ("liechtenstein", 438),
          ("lithuania", 440),
          ("luxembourg", 442),
          ("macau", 446),
          ("malaysia", 458),
          ("mexico", 484),
          ("monaco", 492),
          ("morocco", 504),
          ("cr", 506),
          ("oman", 512),
          ("netherlands", 528),
          ("newZealand", 554),
          ("nicaragua", 558),
          ("norway", 578),
          ("pakistan", 586),
          ("panama", 591),
          ("paraguay", 600),
          ("peru", 604),
          ("philippines", 608),
          ("poland", 616),
          ("portugal", 620),
          ("puertoRico", 630),
          ("qatar", 634),
          ("romania", 642),
          ("russia", 643),
          ("saudiArabia", 682),
          ("singapore", 702),
          ("slovakia", 703),
          ("vietNam", 704),
          ("slovenia", 705),
          ("southAfrica", 710),
          ("zimbabwe", 716),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("syria", 760),
          ("thailand", 764),
          ("trinidadTYobago", 780),
          ("uae", 784),
          ("tunisia", 788),
          ("turkey", 792),
          ("ukraine", 804),
          ("macedonia", 807),
          ("egypt", 818),
          ("unitedKingdom", 826),
          ("usa", 840),
          ("uruguay", 858),
          ("uzbekistan", 860),
          ("venezuela", 862),
          ("yemen", 887),
          ("europeUnion", 918),
          ("extremeDefault", 998),
          ("unknown", 999),
          ("indiaMAX", 1356),
          ("indiaINT", 2356),
          ("legacy", 5010),
          ("base", 5011),
          ("sinwireAR", 5013),
          ("nigeriaLi", 5014),
          ("baseMAX", 5015),
          ("nigeriaLx", 5016),
          ("omanPDO", 5017),
          ("telconetEC", 5018),
          ("mexicomMexico", 5019),
          ("vanguardJordan", 5020),
          ("coppelMexico", 5021),
          ("navCanada", 5022))
    )



class LibraPlusTrafficShapingMode(TextualConvention, Integer32):
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
        *(("be", 0),
          ("independent", 1),
          ("shared", 2))
    )



# MIB Managed Objects in the order of their OIDs

_LPlusNotifications_ObjectIdentity = ObjectIdentity
lPlusNotifications = _LPlusNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0)
)
_LPlusObjects_ObjectIdentity = ObjectIdentity
lPlusObjects = _LPlusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1)
)
_LPlusRadioGenLastChange_Type = TimeTicks
_LPlusRadioGenLastChange_Object = MibScalar
lPlusRadioGenLastChange = _LPlusRadioGenLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 1),
    _LPlusRadioGenLastChange_Type()
)
lPlusRadioGenLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenLastChange.setStatus("current")
_LPlusRadioGenNumRows_Type = Unsigned32
_LPlusRadioGenNumRows_Object = MibScalar
lPlusRadioGenNumRows = _LPlusRadioGenNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 2),
    _LPlusRadioGenNumRows_Type()
)
lPlusRadioGenNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenNumRows.setStatus("current")
_LPlusRadioGenTable_Object = MibTable
lPlusRadioGenTable = _LPlusRadioGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lPlusRadioGenTable.setStatus("current")
_LPlusRadioGenTableEntry_Object = MibTableRow
lPlusRadioGenTableEntry = _LPlusRadioGenTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1)
)
lPlusRadioGenTableEntry.setIndexNames(
    (0, "EION-LPLUS-MIB", "lPlusRadioGenIndex"),
)
if mibBuilder.loadTexts:
    lPlusRadioGenTableEntry.setStatus("current")
_LPlusRadioGenIndex_Type = Unsigned32
_LPlusRadioGenIndex_Object = MibTableColumn
lPlusRadioGenIndex = _LPlusRadioGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 1),
    _LPlusRadioGenIndex_Type()
)
lPlusRadioGenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusRadioGenIndex.setStatus("current")
_LPlusRadioGenAPMode_Type = LibraPlusAPMode
_LPlusRadioGenAPMode_Object = MibTableColumn
lPlusRadioGenAPMode = _LPlusRadioGenAPMode_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 2),
    _LPlusRadioGenAPMode_Type()
)
lPlusRadioGenAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenAPMode.setStatus("current")
_LPlusRadioGenBeaconInterval_Type = Unsigned32
_LPlusRadioGenBeaconInterval_Object = MibTableColumn
lPlusRadioGenBeaconInterval = _LPlusRadioGenBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 3),
    _LPlusRadioGenBeaconInterval_Type()
)
lPlusRadioGenBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenBeaconInterval.setStatus("current")
_LPlusRadioGenChannel_Type = Unsigned32
_LPlusRadioGenChannel_Object = MibTableColumn
lPlusRadioGenChannel = _LPlusRadioGenChannel_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 4),
    _LPlusRadioGenChannel_Type()
)
lPlusRadioGenChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenChannel.setStatus("current")
_LPlusRadioGenCountryCode_Type = LibraPlusWirelessCountryCode
_LPlusRadioGenCountryCode_Object = MibTableColumn
lPlusRadioGenCountryCode = _LPlusRadioGenCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 5),
    _LPlusRadioGenCountryCode_Type()
)
lPlusRadioGenCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenCountryCode.setStatus("current")
_LPlusRadioGenFreq_Type = Unsigned32
_LPlusRadioGenFreq_Object = MibTableColumn
lPlusRadioGenFreq = _LPlusRadioGenFreq_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 6),
    _LPlusRadioGenFreq_Type()
)
lPlusRadioGenFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenFreq.setStatus("current")
_LPlusRadioGenAuthType_Type = LibraPlusAuthType
_LPlusRadioGenAuthType_Object = MibTableColumn
lPlusRadioGenAuthType = _LPlusRadioGenAuthType_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 7),
    _LPlusRadioGenAuthType_Type()
)
lPlusRadioGenAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenAuthType.setStatus("current")


class _LPlusRadioGenEncKey_Type(DisplayString):
    """Custom type lPlusRadioGenEncKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LPlusRadioGenEncKey_Type.__name__ = "DisplayString"
_LPlusRadioGenEncKey_Object = MibTableColumn
lPlusRadioGenEncKey = _LPlusRadioGenEncKey_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 8),
    _LPlusRadioGenEncKey_Type()
)
lPlusRadioGenEncKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenEncKey.setStatus("current")
_LPlusRadioGenEncMtd_Type = LibraPlusAuthMode
_LPlusRadioGenEncMtd_Object = MibTableColumn
lPlusRadioGenEncMtd = _LPlusRadioGenEncMtd_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 9),
    _LPlusRadioGenEncMtd_Type()
)
lPlusRadioGenEncMtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenEncMtd.setStatus("current")
_LPlusRadioGenAuthKeySrc_Type = LibraPlusAuthKeySource
_LPlusRadioGenAuthKeySrc_Object = MibTableColumn
lPlusRadioGenAuthKeySrc = _LPlusRadioGenAuthKeySrc_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 10),
    _LPlusRadioGenAuthKeySrc_Type()
)
lPlusRadioGenAuthKeySrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenAuthKeySrc.setStatus("current")


class _LPlusRadioGenMAC_Type(DisplayString):
    """Custom type lPlusRadioGenMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LPlusRadioGenMAC_Type.__name__ = "DisplayString"
_LPlusRadioGenMAC_Object = MibTableColumn
lPlusRadioGenMAC = _LPlusRadioGenMAC_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 11),
    _LPlusRadioGenMAC_Type()
)
lPlusRadioGenMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenMAC.setStatus("current")
_LPlusRadioGenIP_Type = IpAddress
_LPlusRadioGenIP_Object = MibTableColumn
lPlusRadioGenIP = _LPlusRadioGenIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 12),
    _LPlusRadioGenIP_Type()
)
lPlusRadioGenIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenIP.setStatus("current")
_LPlusRadioGenIPMask_Type = IpAddress
_LPlusRadioGenIPMask_Object = MibTableColumn
lPlusRadioGenIPMask = _LPlusRadioGenIPMask_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 13),
    _LPlusRadioGenIPMask_Type()
)
lPlusRadioGenIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenIPMask.setStatus("current")


class _LPlusRadioGenSSID_Type(DisplayString):
    """Custom type lPlusRadioGenSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusRadioGenSSID_Type.__name__ = "DisplayString"
_LPlusRadioGenSSID_Object = MibTableColumn
lPlusRadioGenSSID = _LPlusRadioGenSSID_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 14),
    _LPlusRadioGenSSID_Type()
)
lPlusRadioGenSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenSSID.setStatus("current")
_LPlusRadioGenHideSSID_Type = TruthValue
_LPlusRadioGenHideSSID_Object = MibTableColumn
lPlusRadioGenHideSSID = _LPlusRadioGenHideSSID_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 15),
    _LPlusRadioGenHideSSID_Type()
)
lPlusRadioGenHideSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenHideSSID.setStatus("current")
_LPlusRadioGenEnableWDS_Type = TruthValue
_LPlusRadioGenEnableWDS_Object = MibTableColumn
lPlusRadioGenEnableWDS = _LPlusRadioGenEnableWDS_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 16),
    _LPlusRadioGenEnableWDS_Type()
)
lPlusRadioGenEnableWDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenEnableWDS.setStatus("current")
_LPlusRadioGenEnableWMM_Type = TruthValue
_LPlusRadioGenEnableWMM_Object = MibTableColumn
lPlusRadioGenEnableWMM = _LPlusRadioGenEnableWMM_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 17),
    _LPlusRadioGenEnableWMM_Type()
)
lPlusRadioGenEnableWMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenEnableWMM.setStatus("current")
_LPlusRadioGenEnableFF_Type = TruthValue
_LPlusRadioGenEnableFF_Object = MibTableColumn
lPlusRadioGenEnableFF = _LPlusRadioGenEnableFF_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 18),
    _LPlusRadioGenEnableFF_Type()
)
lPlusRadioGenEnableFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenEnableFF.setStatus("current")
_LPlusRadioGenEnableBurst_Type = TruthValue
_LPlusRadioGenEnableBurst_Object = MibTableColumn
lPlusRadioGenEnableBurst = _LPlusRadioGenEnableBurst_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 19),
    _LPlusRadioGenEnableBurst_Type()
)
lPlusRadioGenEnableBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenEnableBurst.setStatus("current")
_LPlusRadioGenEnableDFS_Type = TruthValue
_LPlusRadioGenEnableDFS_Object = MibTableColumn
lPlusRadioGenEnableDFS = _LPlusRadioGenEnableDFS_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 20),
    _LPlusRadioGenEnableDFS_Type()
)
lPlusRadioGenEnableDFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenEnableDFS.setStatus("current")
_LPlusRadioGenEnableRTS_Type = TruthValue
_LPlusRadioGenEnableRTS_Object = MibTableColumn
lPlusRadioGenEnableRTS = _LPlusRadioGenEnableRTS_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 21),
    _LPlusRadioGenEnableRTS_Type()
)
lPlusRadioGenEnableRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenEnableRTS.setStatus("current")
_LPlusRadioGenDistance_Type = Unsigned32
_LPlusRadioGenDistance_Object = MibTableColumn
lPlusRadioGenDistance = _LPlusRadioGenDistance_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 22),
    _LPlusRadioGenDistance_Type()
)
lPlusRadioGenDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenDistance.setStatus("current")


class _LPlusRadioGenAPMAC_Type(DisplayString):
    """Custom type lPlusRadioGenAPMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LPlusRadioGenAPMAC_Type.__name__ = "DisplayString"
_LPlusRadioGenAPMAC_Object = MibTableColumn
lPlusRadioGenAPMAC = _LPlusRadioGenAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 23),
    _LPlusRadioGenAPMAC_Type()
)
lPlusRadioGenAPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenAPMAC.setStatus("current")
_LPlusRadioGenLinkStatus_Type = LibraPlusLinkStatus
_LPlusRadioGenLinkStatus_Object = MibTableColumn
lPlusRadioGenLinkStatus = _LPlusRadioGenLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 24),
    _LPlusRadioGenLinkStatus_Type()
)
lPlusRadioGenLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenLinkStatus.setStatus("current")
_LPlusRadioGenTxBitrate_Type = Unsigned32
_LPlusRadioGenTxBitrate_Object = MibTableColumn
lPlusRadioGenTxBitrate = _LPlusRadioGenTxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 25),
    _LPlusRadioGenTxBitrate_Type()
)
lPlusRadioGenTxBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenTxBitrate.setStatus("current")
_LPlusRadioGenTxPower_Type = Unsigned32
_LPlusRadioGenTxPower_Object = MibTableColumn
lPlusRadioGenTxPower = _LPlusRadioGenTxPower_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 26),
    _LPlusRadioGenTxPower_Type()
)
lPlusRadioGenTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenTxPower.setStatus("current")


class _LPlusRadioGenACLName_Type(DisplayString):
    """Custom type lPlusRadioGenACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_LPlusRadioGenACLName_Type.__name__ = "DisplayString"
_LPlusRadioGenACLName_Object = MibTableColumn
lPlusRadioGenACLName = _LPlusRadioGenACLName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 27),
    _LPlusRadioGenACLName_Type()
)
lPlusRadioGenACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenACLName.setStatus("current")
_LPlusRadioGenACLTableStatus_Type = EionACLType
_LPlusRadioGenACLTableStatus_Object = MibTableColumn
lPlusRadioGenACLTableStatus = _LPlusRadioGenACLTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 28),
    _LPlusRadioGenACLTableStatus_Type()
)
lPlusRadioGenACLTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenACLTableStatus.setStatus("current")
_LPlusRadioGenChannelWidth_Type = Unsigned32
_LPlusRadioGenChannelWidth_Object = MibTableColumn
lPlusRadioGenChannelWidth = _LPlusRadioGenChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 29),
    _LPlusRadioGenChannelWidth_Type()
)
lPlusRadioGenChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenChannelWidth.setStatus("current")
_LPlusRadioGenFragThresh_Type = Unsigned32
_LPlusRadioGenFragThresh_Object = MibTableColumn
lPlusRadioGenFragThresh = _LPlusRadioGenFragThresh_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 30),
    _LPlusRadioGenFragThresh_Type()
)
lPlusRadioGenFragThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenFragThresh.setStatus("current")
_LPlusRadioGenOperMode_Type = LibraPlusOperMode
_LPlusRadioGenOperMode_Object = MibTableColumn
lPlusRadioGenOperMode = _LPlusRadioGenOperMode_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 31),
    _LPlusRadioGenOperMode_Type()
)
lPlusRadioGenOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenOperMode.setStatus("current")
_LPlusRadioGenIntraSecBridge_Type = TruthValue
_LPlusRadioGenIntraSecBridge_Object = MibTableColumn
lPlusRadioGenIntraSecBridge = _LPlusRadioGenIntraSecBridge_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 32),
    _LPlusRadioGenIntraSecBridge_Type()
)
lPlusRadioGenIntraSecBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioGenIntraSecBridge.setStatus("current")
_LPlusRadioGenAssociationLimit_Type = Unsigned32
_LPlusRadioGenAssociationLimit_Object = MibTableColumn
lPlusRadioGenAssociationLimit = _LPlusRadioGenAssociationLimit_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 3, 1, 33),
    _LPlusRadioGenAssociationLimit_Type()
)
lPlusRadioGenAssociationLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioGenAssociationLimit.setStatus("current")
_LPlusRadioPeerLastChange_Type = TimeTicks
_LPlusRadioPeerLastChange_Object = MibScalar
lPlusRadioPeerLastChange = _LPlusRadioPeerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 4),
    _LPlusRadioPeerLastChange_Type()
)
lPlusRadioPeerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerLastChange.setStatus("current")
_LPlusRadioPeerNumRows_Type = Unsigned32
_LPlusRadioPeerNumRows_Object = MibScalar
lPlusRadioPeerNumRows = _LPlusRadioPeerNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 5),
    _LPlusRadioPeerNumRows_Type()
)
lPlusRadioPeerNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerNumRows.setStatus("current")
_LPlusRadioPeerTable_Object = MibTable
lPlusRadioPeerTable = _LPlusRadioPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6)
)
if mibBuilder.loadTexts:
    lPlusRadioPeerTable.setStatus("current")
_LPlusRadioPeerEntry_Object = MibTableRow
lPlusRadioPeerEntry = _LPlusRadioPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1)
)
lPlusRadioPeerEntry.setIndexNames(
    (0, "EION-LPLUS-MIB", "lPlusRadioPeerIndex"),
)
if mibBuilder.loadTexts:
    lPlusRadioPeerEntry.setStatus("current")


class _LPlusRadioPeerIndex_Type(Unsigned32):
    """Custom type lPlusRadioPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LPlusRadioPeerIndex_Type.__name__ = "Unsigned32"
_LPlusRadioPeerIndex_Object = MibTableColumn
lPlusRadioPeerIndex = _LPlusRadioPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 1),
    _LPlusRadioPeerIndex_Type()
)
lPlusRadioPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusRadioPeerIndex.setStatus("current")


class _LPlusRadioPeerRadioIndex_Type(Unsigned32):
    """Custom type lPlusRadioPeerRadioIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LPlusRadioPeerRadioIndex_Type.__name__ = "Unsigned32"
_LPlusRadioPeerRadioIndex_Object = MibTableColumn
lPlusRadioPeerRadioIndex = _LPlusRadioPeerRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 2),
    _LPlusRadioPeerRadioIndex_Type()
)
lPlusRadioPeerRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerRadioIndex.setStatus("current")


class _LPlusRadioPeerMAC_Type(DisplayString):
    """Custom type lPlusRadioPeerMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LPlusRadioPeerMAC_Type.__name__ = "DisplayString"
_LPlusRadioPeerMAC_Object = MibTableColumn
lPlusRadioPeerMAC = _LPlusRadioPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 3),
    _LPlusRadioPeerMAC_Type()
)
lPlusRadioPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerMAC.setStatus("current")


class _LPlusRadioPeerRSSI_Type(Integer32):
    """Custom type lPlusRadioPeerRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, -20),
    )


_LPlusRadioPeerRSSI_Type.__name__ = "Integer32"
_LPlusRadioPeerRSSI_Object = MibTableColumn
lPlusRadioPeerRSSI = _LPlusRadioPeerRSSI_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 4),
    _LPlusRadioPeerRSSI_Type()
)
lPlusRadioPeerRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerRSSI.setStatus("current")
_LPlusRadioPeerNoiseLevel_Type = Integer32
_LPlusRadioPeerNoiseLevel_Object = MibTableColumn
lPlusRadioPeerNoiseLevel = _LPlusRadioPeerNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 5),
    _LPlusRadioPeerNoiseLevel_Type()
)
lPlusRadioPeerNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerNoiseLevel.setStatus("current")


class _LPlusRadioPeerLinkQuality_Type(DisplayString):
    """Custom type lPlusRadioPeerLinkQuality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_LPlusRadioPeerLinkQuality_Type.__name__ = "DisplayString"
_LPlusRadioPeerLinkQuality_Object = MibTableColumn
lPlusRadioPeerLinkQuality = _LPlusRadioPeerLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 6),
    _LPlusRadioPeerLinkQuality_Type()
)
lPlusRadioPeerLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerLinkQuality.setStatus("current")
_LPlusRadioPeerTxBitrate_Type = Unsigned32
_LPlusRadioPeerTxBitrate_Object = MibTableColumn
lPlusRadioPeerTxBitrate = _LPlusRadioPeerTxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 7),
    _LPlusRadioPeerTxBitrate_Type()
)
lPlusRadioPeerTxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerTxBitrate.setStatus("current")
_LPlusRadioPeerSNR_Type = Integer32
_LPlusRadioPeerSNR_Object = MibTableColumn
lPlusRadioPeerSNR = _LPlusRadioPeerSNR_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 8),
    _LPlusRadioPeerSNR_Type()
)
lPlusRadioPeerSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerSNR.setStatus("current")
_LPlusRadioPeerTx_Type = Counter32
_LPlusRadioPeerTx_Object = MibTableColumn
lPlusRadioPeerTx = _LPlusRadioPeerTx_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 9),
    _LPlusRadioPeerTx_Type()
)
lPlusRadioPeerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerTx.setStatus("current")
_LPlusRadioPeerRx_Type = Counter32
_LPlusRadioPeerRx_Object = MibTableColumn
lPlusRadioPeerRx = _LPlusRadioPeerRx_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 10),
    _LPlusRadioPeerRx_Type()
)
lPlusRadioPeerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerRx.setStatus("current")


class _LPlusRadioPeerCAPS_Type(DisplayString):
    """Custom type lPlusRadioPeerCAPS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LPlusRadioPeerCAPS_Type.__name__ = "DisplayString"
_LPlusRadioPeerCAPS_Object = MibTableColumn
lPlusRadioPeerCAPS = _LPlusRadioPeerCAPS_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 11),
    _LPlusRadioPeerCAPS_Type()
)
lPlusRadioPeerCAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerCAPS.setStatus("current")


class _LPlusRadioPeerFLAGS_Type(DisplayString):
    """Custom type lPlusRadioPeerFLAGS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LPlusRadioPeerFLAGS_Type.__name__ = "DisplayString"
_LPlusRadioPeerFLAGS_Object = MibTableColumn
lPlusRadioPeerFLAGS = _LPlusRadioPeerFLAGS_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 12),
    _LPlusRadioPeerFLAGS_Type()
)
lPlusRadioPeerFLAGS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerFLAGS.setStatus("current")
_LPlusRadioPeerTxRates_Type = Counter32
_LPlusRadioPeerTxRates_Object = MibTableColumn
lPlusRadioPeerTxRates = _LPlusRadioPeerTxRates_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 13),
    _LPlusRadioPeerTxRates_Type()
)
lPlusRadioPeerTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerTxRates.setStatus("current")
_LPlusRadioPeerRxRates_Type = Counter32
_LPlusRadioPeerRxRates_Object = MibTableColumn
lPlusRadioPeerRxRates = _LPlusRadioPeerRxRates_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 14),
    _LPlusRadioPeerRxRates_Type()
)
lPlusRadioPeerRxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerRxRates.setStatus("current")


class _LPlusRadioPeerName_Type(DisplayString):
    """Custom type lPlusRadioPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LPlusRadioPeerName_Type.__name__ = "DisplayString"
_LPlusRadioPeerName_Object = MibTableColumn
lPlusRadioPeerName = _LPlusRadioPeerName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 6, 1, 15),
    _LPlusRadioPeerName_Type()
)
lPlusRadioPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioPeerName.setStatus("current")
_LPlusRadioChan2FreqLastChange_Type = TimeTicks
_LPlusRadioChan2FreqLastChange_Object = MibScalar
lPlusRadioChan2FreqLastChange = _LPlusRadioChan2FreqLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 7),
    _LPlusRadioChan2FreqLastChange_Type()
)
lPlusRadioChan2FreqLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioChan2FreqLastChange.setStatus("current")
_LPlusRadioChan2FreqNumRows_Type = Unsigned32
_LPlusRadioChan2FreqNumRows_Object = MibScalar
lPlusRadioChan2FreqNumRows = _LPlusRadioChan2FreqNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 8),
    _LPlusRadioChan2FreqNumRows_Type()
)
lPlusRadioChan2FreqNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioChan2FreqNumRows.setStatus("current")
_LPlusRadioChan2FreqTable_Object = MibTable
lPlusRadioChan2FreqTable = _LPlusRadioChan2FreqTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 9)
)
if mibBuilder.loadTexts:
    lPlusRadioChan2FreqTable.setStatus("current")
_LPlusRadioChan2FreqEntry_Object = MibTableRow
lPlusRadioChan2FreqEntry = _LPlusRadioChan2FreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 9, 1)
)
lPlusRadioChan2FreqEntry.setIndexNames(
    (0, "EION-LPLUS-MIB", "lPlusRadioChan2FreqRadioIndex"),
    (0, "EION-LPLUS-MIB", "lPlusRadioChan2FreqChannel"),
)
if mibBuilder.loadTexts:
    lPlusRadioChan2FreqEntry.setStatus("current")


class _LPlusRadioChan2FreqRadioIndex_Type(Unsigned32):
    """Custom type lPlusRadioChan2FreqRadioIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LPlusRadioChan2FreqRadioIndex_Type.__name__ = "Unsigned32"
_LPlusRadioChan2FreqRadioIndex_Object = MibTableColumn
lPlusRadioChan2FreqRadioIndex = _LPlusRadioChan2FreqRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 9, 1, 1),
    _LPlusRadioChan2FreqRadioIndex_Type()
)
lPlusRadioChan2FreqRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusRadioChan2FreqRadioIndex.setStatus("current")


class _LPlusRadioChan2FreqChannel_Type(Unsigned32):
    """Custom type lPlusRadioChan2FreqChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LPlusRadioChan2FreqChannel_Type.__name__ = "Unsigned32"
_LPlusRadioChan2FreqChannel_Object = MibTableColumn
lPlusRadioChan2FreqChannel = _LPlusRadioChan2FreqChannel_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 9, 1, 2),
    _LPlusRadioChan2FreqChannel_Type()
)
lPlusRadioChan2FreqChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusRadioChan2FreqChannel.setStatus("current")
_LPlusRadioChan2FreqFrequency_Type = Unsigned32
_LPlusRadioChan2FreqFrequency_Object = MibTableColumn
lPlusRadioChan2FreqFrequency = _LPlusRadioChan2FreqFrequency_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 9, 1, 3),
    _LPlusRadioChan2FreqFrequency_Type()
)
lPlusRadioChan2FreqFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioChan2FreqFrequency.setStatus("current")
_LPlusRadioQosLastChange_Type = TimeTicks
_LPlusRadioQosLastChange_Object = MibScalar
lPlusRadioQosLastChange = _LPlusRadioQosLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 10),
    _LPlusRadioQosLastChange_Type()
)
lPlusRadioQosLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioQosLastChange.setStatus("current")
_LPlusRadioQosNumRows_Type = Unsigned32
_LPlusRadioQosNumRows_Object = MibScalar
lPlusRadioQosNumRows = _LPlusRadioQosNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 11),
    _LPlusRadioQosNumRows_Type()
)
lPlusRadioQosNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPlusRadioQosNumRows.setStatus("current")
_LPlusRadioQosTable_Object = MibTable
lPlusRadioQosTable = _LPlusRadioQosTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 12)
)
if mibBuilder.loadTexts:
    lPlusRadioQosTable.setStatus("current")
_LPlusRadioQosEntry_Object = MibTableRow
lPlusRadioQosEntry = _LPlusRadioQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 12, 1)
)
lPlusRadioQosEntry.setIndexNames(
    (0, "EION-LPLUS-MIB", "lPlusRadioQosName"),
)
if mibBuilder.loadTexts:
    lPlusRadioQosEntry.setStatus("current")


class _LPlusRadioQosName_Type(DisplayString):
    """Custom type lPlusRadioQosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusRadioQosName_Type.__name__ = "DisplayString"
_LPlusRadioQosName_Object = MibTableColumn
lPlusRadioQosName = _LPlusRadioQosName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 12, 1, 1),
    _LPlusRadioQosName_Type()
)
lPlusRadioQosName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusRadioQosName.setStatus("current")


class _LPlusRadioQosRowStatus_Type(Integer32):
    """Custom type lPlusRadioQosRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("max", 1),
          ("be", 2))
    )


_LPlusRadioQosRowStatus_Type.__name__ = "Integer32"
_LPlusRadioQosRowStatus_Object = MibTableColumn
lPlusRadioQosRowStatus = _LPlusRadioQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 12, 1, 2),
    _LPlusRadioQosRowStatus_Type()
)
lPlusRadioQosRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioQosRowStatus.setStatus("current")
_LPlusRadioQosUplinkRate_Type = Unsigned32
_LPlusRadioQosUplinkRate_Object = MibTableColumn
lPlusRadioQosUplinkRate = _LPlusRadioQosUplinkRate_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 12, 1, 3),
    _LPlusRadioQosUplinkRate_Type()
)
lPlusRadioQosUplinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioQosUplinkRate.setStatus("current")
_LPlusRadioQosDownlinkRate_Type = Unsigned32
_LPlusRadioQosDownlinkRate_Object = MibTableColumn
lPlusRadioQosDownlinkRate = _LPlusRadioQosDownlinkRate_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 12, 1, 4),
    _LPlusRadioQosDownlinkRate_Type()
)
lPlusRadioQosDownlinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lPlusRadioQosDownlinkRate.setStatus("current")
_LPlusQoSTable_Object = MibTable
lPlusQoSTable = _LPlusQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 13)
)
if mibBuilder.loadTexts:
    lPlusQoSTable.setStatus("current")
_LPlusQoSEntry_Object = MibTableRow
lPlusQoSEntry = _LPlusQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 13, 1)
)
lPlusQoSEntry.setIndexNames(
    (0, "EION-LPLUS-MIB", "lPlusQoSIndex"),
)
if mibBuilder.loadTexts:
    lPlusQoSEntry.setStatus("current")
_LPlusQoSIndex_Type = Unsigned32
_LPlusQoSIndex_Object = MibTableColumn
lPlusQoSIndex = _LPlusQoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 13, 1, 1),
    _LPlusQoSIndex_Type()
)
lPlusQoSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusQoSIndex.setStatus("current")


class _LPlusQoSRowStatus_Type(RowStatus):
    """Custom type lPlusQoSRowStatus based on RowStatus"""
    defaultValue = 3


_LPlusQoSRowStatus_Type.__name__ = "RowStatus"
_LPlusQoSRowStatus_Object = MibTableColumn
lPlusQoSRowStatus = _LPlusQoSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 13, 1, 2),
    _LPlusQoSRowStatus_Type()
)
lPlusQoSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusQoSRowStatus.setStatus("current")


class _LPlusQoSCir_Type(Unsigned32):
    """Custom type lPlusQoSCir based on Unsigned32"""
    defaultValue = 0


_LPlusQoSCir_Type.__name__ = "Unsigned32"
_LPlusQoSCir_Object = MibTableColumn
lPlusQoSCir = _LPlusQoSCir_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 13, 1, 3),
    _LPlusQoSCir_Type()
)
lPlusQoSCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusQoSCir.setStatus("current")


class _LPlusQoSMir_Type(Unsigned32):
    """Custom type lPlusQoSMir based on Unsigned32"""
    defaultValue = 0


_LPlusQoSMir_Type.__name__ = "Unsigned32"
_LPlusQoSMir_Object = MibTableColumn
lPlusQoSMir = _LPlusQoSMir_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 13, 1, 4),
    _LPlusQoSMir_Type()
)
lPlusQoSMir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusQoSMir.setStatus("current")
_LPlusServiceFlowTable_Object = MibTable
lPlusServiceFlowTable = _LPlusServiceFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14)
)
if mibBuilder.loadTexts:
    lPlusServiceFlowTable.setStatus("current")
_LPlusServiceFlowEntry_Object = MibTableRow
lPlusServiceFlowEntry = _LPlusServiceFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1)
)
lPlusServiceFlowEntry.setIndexNames(
    (0, "EION-LPLUS-MIB", "lPlusServiceFlowIndex"),
)
if mibBuilder.loadTexts:
    lPlusServiceFlowEntry.setStatus("current")
_LPlusServiceFlowIndex_Type = Unsigned32
_LPlusServiceFlowIndex_Object = MibTableColumn
lPlusServiceFlowIndex = _LPlusServiceFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 1),
    _LPlusServiceFlowIndex_Type()
)
lPlusServiceFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusServiceFlowIndex.setStatus("current")


class _LPlusServiceFlowRowStatus_Type(RowStatus):
    """Custom type lPlusServiceFlowRowStatus based on RowStatus"""
    defaultValue = 3


_LPlusServiceFlowRowStatus_Type.__name__ = "RowStatus"
_LPlusServiceFlowRowStatus_Object = MibTableColumn
lPlusServiceFlowRowStatus = _LPlusServiceFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 2),
    _LPlusServiceFlowRowStatus_Type()
)
lPlusServiceFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowRowStatus.setStatus("current")
_LPlusServiceFlowULQoSTableIndex_Type = Unsigned32
_LPlusServiceFlowULQoSTableIndex_Object = MibTableColumn
lPlusServiceFlowULQoSTableIndex = _LPlusServiceFlowULQoSTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 3),
    _LPlusServiceFlowULQoSTableIndex_Type()
)
lPlusServiceFlowULQoSTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULQoSTableIndex.setStatus("current")
_LPlusServiceFlowDLQoSTableIndex_Type = Unsigned32
_LPlusServiceFlowDLQoSTableIndex_Object = MibTableColumn
lPlusServiceFlowDLQoSTableIndex = _LPlusServiceFlowDLQoSTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 4),
    _LPlusServiceFlowDLQoSTableIndex_Type()
)
lPlusServiceFlowDLQoSTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLQoSTableIndex.setStatus("current")


class _LPlusServiceFlowULDefault_Type(TruthValue):
    """Custom type lPlusServiceFlowULDefault based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowULDefault_Type.__name__ = "TruthValue"
_LPlusServiceFlowULDefault_Object = MibTableColumn
lPlusServiceFlowULDefault = _LPlusServiceFlowULDefault_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 5),
    _LPlusServiceFlowULDefault_Type()
)
lPlusServiceFlowULDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULDefault.setStatus("current")


class _LPlusServiceFlowDLDefault_Type(TruthValue):
    """Custom type lPlusServiceFlowDLDefault based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowDLDefault_Type.__name__ = "TruthValue"
_LPlusServiceFlowDLDefault_Object = MibTableColumn
lPlusServiceFlowDLDefault = _LPlusServiceFlowDLDefault_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 6),
    _LPlusServiceFlowDLDefault_Type()
)
lPlusServiceFlowDLDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLDefault.setStatus("current")


class _LPlusServiceFlowULClassDisabled_Type(TruthValue):
    """Custom type lPlusServiceFlowULClassDisabled based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowULClassDisabled_Type.__name__ = "TruthValue"
_LPlusServiceFlowULClassDisabled_Object = MibTableColumn
lPlusServiceFlowULClassDisabled = _LPlusServiceFlowULClassDisabled_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 7),
    _LPlusServiceFlowULClassDisabled_Type()
)
lPlusServiceFlowULClassDisabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULClassDisabled.setStatus("current")


class _LPlusServiceFlowULClassVlanId_Type(TruthValue):
    """Custom type lPlusServiceFlowULClassVlanId based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowULClassVlanId_Type.__name__ = "TruthValue"
_LPlusServiceFlowULClassVlanId_Object = MibTableColumn
lPlusServiceFlowULClassVlanId = _LPlusServiceFlowULClassVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 8),
    _LPlusServiceFlowULClassVlanId_Type()
)
lPlusServiceFlowULClassVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULClassVlanId.setStatus("current")


class _LPlusServiceFlowULClassVlanPrio_Type(TruthValue):
    """Custom type lPlusServiceFlowULClassVlanPrio based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowULClassVlanPrio_Type.__name__ = "TruthValue"
_LPlusServiceFlowULClassVlanPrio_Object = MibTableColumn
lPlusServiceFlowULClassVlanPrio = _LPlusServiceFlowULClassVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 9),
    _LPlusServiceFlowULClassVlanPrio_Type()
)
lPlusServiceFlowULClassVlanPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULClassVlanPrio.setStatus("current")


class _LPlusServiceFlowULClassIpTos_Type(TruthValue):
    """Custom type lPlusServiceFlowULClassIpTos based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowULClassIpTos_Type.__name__ = "TruthValue"
_LPlusServiceFlowULClassIpTos_Object = MibTableColumn
lPlusServiceFlowULClassIpTos = _LPlusServiceFlowULClassIpTos_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 10),
    _LPlusServiceFlowULClassIpTos_Type()
)
lPlusServiceFlowULClassIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULClassIpTos.setStatus("current")


class _LPlusServiceFlowULClassWmm_Type(TruthValue):
    """Custom type lPlusServiceFlowULClassWmm based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowULClassWmm_Type.__name__ = "TruthValue"
_LPlusServiceFlowULClassWmm_Object = MibTableColumn
lPlusServiceFlowULClassWmm = _LPlusServiceFlowULClassWmm_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 11),
    _LPlusServiceFlowULClassWmm_Type()
)
lPlusServiceFlowULClassWmm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULClassWmm.setStatus("current")


class _LPlusServiceFlowDLClassDisabled_Type(TruthValue):
    """Custom type lPlusServiceFlowDLClassDisabled based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowDLClassDisabled_Type.__name__ = "TruthValue"
_LPlusServiceFlowDLClassDisabled_Object = MibTableColumn
lPlusServiceFlowDLClassDisabled = _LPlusServiceFlowDLClassDisabled_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 12),
    _LPlusServiceFlowDLClassDisabled_Type()
)
lPlusServiceFlowDLClassDisabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLClassDisabled.setStatus("current")


class _LPlusServiceFlowDLClassVlanId_Type(TruthValue):
    """Custom type lPlusServiceFlowDLClassVlanId based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowDLClassVlanId_Type.__name__ = "TruthValue"
_LPlusServiceFlowDLClassVlanId_Object = MibTableColumn
lPlusServiceFlowDLClassVlanId = _LPlusServiceFlowDLClassVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 13),
    _LPlusServiceFlowDLClassVlanId_Type()
)
lPlusServiceFlowDLClassVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLClassVlanId.setStatus("current")


class _LPlusServiceFlowDLClassVlanPrio_Type(TruthValue):
    """Custom type lPlusServiceFlowDLClassVlanPrio based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowDLClassVlanPrio_Type.__name__ = "TruthValue"
_LPlusServiceFlowDLClassVlanPrio_Object = MibTableColumn
lPlusServiceFlowDLClassVlanPrio = _LPlusServiceFlowDLClassVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 14),
    _LPlusServiceFlowDLClassVlanPrio_Type()
)
lPlusServiceFlowDLClassVlanPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLClassVlanPrio.setStatus("current")


class _LPlusServiceFlowDLClassIpTos_Type(TruthValue):
    """Custom type lPlusServiceFlowDLClassIpTos based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowDLClassIpTos_Type.__name__ = "TruthValue"
_LPlusServiceFlowDLClassIpTos_Object = MibTableColumn
lPlusServiceFlowDLClassIpTos = _LPlusServiceFlowDLClassIpTos_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 15),
    _LPlusServiceFlowDLClassIpTos_Type()
)
lPlusServiceFlowDLClassIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLClassIpTos.setStatus("current")


class _LPlusServiceFlowDLClassWmm_Type(TruthValue):
    """Custom type lPlusServiceFlowDLClassWmm based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowDLClassWmm_Type.__name__ = "TruthValue"
_LPlusServiceFlowDLClassWmm_Object = MibTableColumn
lPlusServiceFlowDLClassWmm = _LPlusServiceFlowDLClassWmm_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 16),
    _LPlusServiceFlowDLClassWmm_Type()
)
lPlusServiceFlowDLClassWmm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLClassWmm.setStatus("current")


class _LPlusServiceFlowULValueVlanId_Type(DisplayString):
    """Custom type lPlusServiceFlowULValueVlanId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusServiceFlowULValueVlanId_Type.__name__ = "DisplayString"
_LPlusServiceFlowULValueVlanId_Object = MibTableColumn
lPlusServiceFlowULValueVlanId = _LPlusServiceFlowULValueVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 17),
    _LPlusServiceFlowULValueVlanId_Type()
)
lPlusServiceFlowULValueVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULValueVlanId.setStatus("current")


class _LPlusServiceFlowULValueVlanPrio_Type(DisplayString):
    """Custom type lPlusServiceFlowULValueVlanPrio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusServiceFlowULValueVlanPrio_Type.__name__ = "DisplayString"
_LPlusServiceFlowULValueVlanPrio_Object = MibTableColumn
lPlusServiceFlowULValueVlanPrio = _LPlusServiceFlowULValueVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 18),
    _LPlusServiceFlowULValueVlanPrio_Type()
)
lPlusServiceFlowULValueVlanPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULValueVlanPrio.setStatus("current")


class _LPlusServiceFlowULValueIpTos_Type(DisplayString):
    """Custom type lPlusServiceFlowULValueIpTos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusServiceFlowULValueIpTos_Type.__name__ = "DisplayString"
_LPlusServiceFlowULValueIpTos_Object = MibTableColumn
lPlusServiceFlowULValueIpTos = _LPlusServiceFlowULValueIpTos_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 19),
    _LPlusServiceFlowULValueIpTos_Type()
)
lPlusServiceFlowULValueIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULValueIpTos.setStatus("current")


class _LPlusServiceFlowULValueWmm_Type(Integer32):
    """Custom type lPlusServiceFlowULValueWmm based on Integer32"""
    defaultValue = 0

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
        *(("be", 0),
          ("bk", 1),
          ("vi", 2),
          ("vo", 3))
    )


_LPlusServiceFlowULValueWmm_Type.__name__ = "Integer32"
_LPlusServiceFlowULValueWmm_Object = MibTableColumn
lPlusServiceFlowULValueWmm = _LPlusServiceFlowULValueWmm_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 20),
    _LPlusServiceFlowULValueWmm_Type()
)
lPlusServiceFlowULValueWmm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULValueWmm.setStatus("current")


class _LPlusServiceFlowDLValueVlanId_Type(DisplayString):
    """Custom type lPlusServiceFlowDLValueVlanId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusServiceFlowDLValueVlanId_Type.__name__ = "DisplayString"
_LPlusServiceFlowDLValueVlanId_Object = MibTableColumn
lPlusServiceFlowDLValueVlanId = _LPlusServiceFlowDLValueVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 21),
    _LPlusServiceFlowDLValueVlanId_Type()
)
lPlusServiceFlowDLValueVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLValueVlanId.setStatus("current")


class _LPlusServiceFlowDLValueVlanPrio_Type(DisplayString):
    """Custom type lPlusServiceFlowDLValueVlanPrio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusServiceFlowDLValueVlanPrio_Type.__name__ = "DisplayString"
_LPlusServiceFlowDLValueVlanPrio_Object = MibTableColumn
lPlusServiceFlowDLValueVlanPrio = _LPlusServiceFlowDLValueVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 22),
    _LPlusServiceFlowDLValueVlanPrio_Type()
)
lPlusServiceFlowDLValueVlanPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLValueVlanPrio.setStatus("current")


class _LPlusServiceFlowDLValueIpTos_Type(DisplayString):
    """Custom type lPlusServiceFlowDLValueIpTos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusServiceFlowDLValueIpTos_Type.__name__ = "DisplayString"
_LPlusServiceFlowDLValueIpTos_Object = MibTableColumn
lPlusServiceFlowDLValueIpTos = _LPlusServiceFlowDLValueIpTos_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 23),
    _LPlusServiceFlowDLValueIpTos_Type()
)
lPlusServiceFlowDLValueIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLValueIpTos.setStatus("current")


class _LPlusServiceFlowDLValueWmm_Type(Integer32):
    """Custom type lPlusServiceFlowDLValueWmm based on Integer32"""
    defaultValue = 0

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
        *(("be", 0),
          ("bk", 1),
          ("vi", 2),
          ("vo", 3))
    )


_LPlusServiceFlowDLValueWmm_Type.__name__ = "Integer32"
_LPlusServiceFlowDLValueWmm_Object = MibTableColumn
lPlusServiceFlowDLValueWmm = _LPlusServiceFlowDLValueWmm_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 24),
    _LPlusServiceFlowDLValueWmm_Type()
)
lPlusServiceFlowDLValueWmm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLValueWmm.setStatus("current")


class _LPlusServiceFlowULAudio_Type(TruthValue):
    """Custom type lPlusServiceFlowULAudio based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowULAudio_Type.__name__ = "TruthValue"
_LPlusServiceFlowULAudio_Object = MibTableColumn
lPlusServiceFlowULAudio = _LPlusServiceFlowULAudio_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 25),
    _LPlusServiceFlowULAudio_Type()
)
lPlusServiceFlowULAudio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowULAudio.setStatus("current")


class _LPlusServiceFlowDLAudio_Type(TruthValue):
    """Custom type lPlusServiceFlowDLAudio based on TruthValue"""
    defaultValue = 2


_LPlusServiceFlowDLAudio_Type.__name__ = "TruthValue"
_LPlusServiceFlowDLAudio_Object = MibTableColumn
lPlusServiceFlowDLAudio = _LPlusServiceFlowDLAudio_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 14, 1, 26),
    _LPlusServiceFlowDLAudio_Type()
)
lPlusServiceFlowDLAudio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceFlowDLAudio.setStatus("current")
_LPlusServiceProfileTable_Object = MibTable
lPlusServiceProfileTable = _LPlusServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15)
)
if mibBuilder.loadTexts:
    lPlusServiceProfileTable.setStatus("current")
_LPlusServiceProfileEntry_Object = MibTableRow
lPlusServiceProfileEntry = _LPlusServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15, 1)
)
lPlusServiceProfileEntry.setIndexNames(
    (0, "EION-LPLUS-MIB", "lPlusServiceProfileIndex"),
)
if mibBuilder.loadTexts:
    lPlusServiceProfileEntry.setStatus("current")
_LPlusServiceProfileIndex_Type = Unsigned32
_LPlusServiceProfileIndex_Object = MibTableColumn
lPlusServiceProfileIndex = _LPlusServiceProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15, 1, 1),
    _LPlusServiceProfileIndex_Type()
)
lPlusServiceProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusServiceProfileIndex.setStatus("current")


class _LPlusServiceProfileRowStatus_Type(RowStatus):
    """Custom type lPlusServiceProfileRowStatus based on RowStatus"""
    defaultValue = 3


_LPlusServiceProfileRowStatus_Type.__name__ = "RowStatus"
_LPlusServiceProfileRowStatus_Object = MibTableColumn
lPlusServiceProfileRowStatus = _LPlusServiceProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15, 1, 2),
    _LPlusServiceProfileRowStatus_Type()
)
lPlusServiceProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceProfileRowStatus.setStatus("current")


class _LPlusServiceProfileScheduleType_Type(LibraPlusTrafficShapingMode):
    """Custom type lPlusServiceProfileScheduleType based on LibraPlusTrafficShapingMode"""
    defaultValue = 0


_LPlusServiceProfileScheduleType_Type.__name__ = "LibraPlusTrafficShapingMode"
_LPlusServiceProfileScheduleType_Object = MibTableColumn
lPlusServiceProfileScheduleType = _LPlusServiceProfileScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15, 1, 3),
    _LPlusServiceProfileScheduleType_Type()
)
lPlusServiceProfileScheduleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceProfileScheduleType.setStatus("current")


class _LPlusServiceProfileSF1_Type(Unsigned32):
    """Custom type lPlusServiceProfileSF1 based on Unsigned32"""
    defaultValue = 0


_LPlusServiceProfileSF1_Type.__name__ = "Unsigned32"
_LPlusServiceProfileSF1_Object = MibTableColumn
lPlusServiceProfileSF1 = _LPlusServiceProfileSF1_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15, 1, 4),
    _LPlusServiceProfileSF1_Type()
)
lPlusServiceProfileSF1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceProfileSF1.setStatus("current")


class _LPlusServiceProfileSF2_Type(Unsigned32):
    """Custom type lPlusServiceProfileSF2 based on Unsigned32"""
    defaultValue = 0


_LPlusServiceProfileSF2_Type.__name__ = "Unsigned32"
_LPlusServiceProfileSF2_Object = MibTableColumn
lPlusServiceProfileSF2 = _LPlusServiceProfileSF2_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15, 1, 5),
    _LPlusServiceProfileSF2_Type()
)
lPlusServiceProfileSF2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceProfileSF2.setStatus("current")


class _LPlusServiceProfileSF3_Type(Unsigned32):
    """Custom type lPlusServiceProfileSF3 based on Unsigned32"""
    defaultValue = 0


_LPlusServiceProfileSF3_Type.__name__ = "Unsigned32"
_LPlusServiceProfileSF3_Object = MibTableColumn
lPlusServiceProfileSF3 = _LPlusServiceProfileSF3_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15, 1, 6),
    _LPlusServiceProfileSF3_Type()
)
lPlusServiceProfileSF3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceProfileSF3.setStatus("current")


class _LPlusServiceProfileSF4_Type(Unsigned32):
    """Custom type lPlusServiceProfileSF4 based on Unsigned32"""
    defaultValue = 0


_LPlusServiceProfileSF4_Type.__name__ = "Unsigned32"
_LPlusServiceProfileSF4_Object = MibTableColumn
lPlusServiceProfileSF4 = _LPlusServiceProfileSF4_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 15, 1, 7),
    _LPlusServiceProfileSF4_Type()
)
lPlusServiceProfileSF4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusServiceProfileSF4.setStatus("current")
_LPlusCpeQoSConfigTable_Object = MibTable
lPlusCpeQoSConfigTable = _LPlusCpeQoSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 16)
)
if mibBuilder.loadTexts:
    lPlusCpeQoSConfigTable.setStatus("current")
_LPlusCpeQoSConfigEntry_Object = MibTableRow
lPlusCpeQoSConfigEntry = _LPlusCpeQoSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 16, 1)
)
lPlusCpeQoSConfigEntry.setIndexNames(
    (0, "EION-LPLUS-MIB", "lPlusCpeQoSConfigIndex"),
)
if mibBuilder.loadTexts:
    lPlusCpeQoSConfigEntry.setStatus("current")
_LPlusCpeQoSConfigIndex_Type = Unsigned32
_LPlusCpeQoSConfigIndex_Object = MibTableColumn
lPlusCpeQoSConfigIndex = _LPlusCpeQoSConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 16, 1, 1),
    _LPlusCpeQoSConfigIndex_Type()
)
lPlusCpeQoSConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPlusCpeQoSConfigIndex.setStatus("current")


class _LPlusCpeQoSConfigRowStatus_Type(RowStatus):
    """Custom type lPlusCpeQoSConfigRowStatus based on RowStatus"""
    defaultValue = 3


_LPlusCpeQoSConfigRowStatus_Type.__name__ = "RowStatus"
_LPlusCpeQoSConfigRowStatus_Object = MibTableColumn
lPlusCpeQoSConfigRowStatus = _LPlusCpeQoSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 16, 1, 2),
    _LPlusCpeQoSConfigRowStatus_Type()
)
lPlusCpeQoSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusCpeQoSConfigRowStatus.setStatus("current")


class _LPlusCpeQoSConfigName_Type(DisplayString):
    """Custom type lPlusCpeQoSConfigName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LPlusCpeQoSConfigName_Type.__name__ = "DisplayString"
_LPlusCpeQoSConfigName_Object = MibTableColumn
lPlusCpeQoSConfigName = _LPlusCpeQoSConfigName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 16, 1, 3),
    _LPlusCpeQoSConfigName_Type()
)
lPlusCpeQoSConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusCpeQoSConfigName.setStatus("current")


class _LPlusCpeQoSConfigMac_Type(DisplayString):
    """Custom type lPlusCpeQoSConfigMac based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_LPlusCpeQoSConfigMac_Type.__name__ = "DisplayString"
_LPlusCpeQoSConfigMac_Object = MibTableColumn
lPlusCpeQoSConfigMac = _LPlusCpeQoSConfigMac_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 16, 1, 4),
    _LPlusCpeQoSConfigMac_Type()
)
lPlusCpeQoSConfigMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusCpeQoSConfigMac.setStatus("current")


class _LPlusCpeQoSConfigSvcProfIndex_Type(Unsigned32):
    """Custom type lPlusCpeQoSConfigSvcProfIndex based on Unsigned32"""
    defaultValue = 0


_LPlusCpeQoSConfigSvcProfIndex_Type.__name__ = "Unsigned32"
_LPlusCpeQoSConfigSvcProfIndex_Object = MibTableColumn
lPlusCpeQoSConfigSvcProfIndex = _LPlusCpeQoSConfigSvcProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 1, 16, 1, 5),
    _LPlusCpeQoSConfigSvcProfIndex_Type()
)
lPlusCpeQoSConfigSvcProfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lPlusCpeQoSConfigSvcProfIndex.setStatus("current")
_LPlusConformance_ObjectIdentity = ObjectIdentity
lPlusConformance = _LPlusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2)
)
_LPlusCompliances_ObjectIdentity = ObjectIdentity
lPlusCompliances = _LPlusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 1)
)
_LPlusGroups_ObjectIdentity = ObjectIdentity
lPlusGroups = _LPlusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2)
)


class _LPlusRadioLoginStatus_Type(Integer32):
    """Custom type lPlusRadioLoginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("recover", 2))
    )


_LPlusRadioLoginStatus_Type.__name__ = "Integer32"
_LPlusRadioLoginStatus_Object = MibScalar
lPlusRadioLoginStatus = _LPlusRadioLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 3),
    _LPlusRadioLoginStatus_Type()
)
lPlusRadioLoginStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioLoginStatus.setStatus("current")
_LPlusPktErrRatePerMin_Type = Unsigned32
_LPlusPktErrRatePerMin_Object = MibScalar
lPlusPktErrRatePerMin = _LPlusPktErrRatePerMin_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 4),
    _LPlusPktErrRatePerMin_Type()
)
lPlusPktErrRatePerMin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusPktErrRatePerMin.setStatus("current")


class _LPlusRadioPktRateDirection_Type(Integer32):
    """Custom type lPlusRadioPktRateDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("receive", 2))
    )


_LPlusRadioPktRateDirection_Type.__name__ = "Integer32"
_LPlusRadioPktRateDirection_Object = MibScalar
lPlusRadioPktRateDirection = _LPlusRadioPktRateDirection_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 5),
    _LPlusRadioPktRateDirection_Type()
)
lPlusRadioPktRateDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioPktRateDirection.setStatus("current")


class _LPlusRadioRebootStatus_Type(Integer32):
    """Custom type lPlusRadioRebootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("user", 1)
    )


_LPlusRadioRebootStatus_Type.__name__ = "Integer32"
_LPlusRadioRebootStatus_Object = MibScalar
lPlusRadioRebootStatus = _LPlusRadioRebootStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 6),
    _LPlusRadioRebootStatus_Type()
)
lPlusRadioRebootStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioRebootStatus.setStatus("current")


class _LPlusRadioFrmWareVer_Type(DisplayString):
    """Custom type lPlusRadioFrmWareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LPlusRadioFrmWareVer_Type.__name__ = "DisplayString"
_LPlusRadioFrmWareVer_Object = MibScalar
lPlusRadioFrmWareVer = _LPlusRadioFrmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 7),
    _LPlusRadioFrmWareVer_Type()
)
lPlusRadioFrmWareVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioFrmWareVer.setStatus("current")


class _LPlusRadioAssocStatus_Type(Integer32):
    """Custom type lPlusRadioAssocStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assoc", 1),
          ("diassoc", 2))
    )


_LPlusRadioAssocStatus_Type.__name__ = "Integer32"
_LPlusRadioAssocStatus_Object = MibScalar
lPlusRadioAssocStatus = _LPlusRadioAssocStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 8),
    _LPlusRadioAssocStatus_Type()
)
lPlusRadioAssocStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioAssocStatus.setStatus("current")


class _LPlusRadioAuthStatus_Type(Integer32):
    """Custom type lPlusRadioAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_LPlusRadioAuthStatus_Type.__name__ = "Integer32"
_LPlusRadioAuthStatus_Object = MibScalar
lPlusRadioAuthStatus = _LPlusRadioAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 9),
    _LPlusRadioAuthStatus_Type()
)
lPlusRadioAuthStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioAuthStatus.setStatus("current")
_LPlusRadioWebIP_Type = IpAddress
_LPlusRadioWebIP_Object = MibScalar
lPlusRadioWebIP = _LPlusRadioWebIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 10),
    _LPlusRadioWebIP_Type()
)
lPlusRadioWebIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioWebIP.setStatus("current")


class _LPlusRadioPeerRSSIStatus_Type(Integer32):
    """Custom type lPlusRadioPeerRSSIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowthreshold", 1),
          ("highthreshold", 2))
    )


_LPlusRadioPeerRSSIStatus_Type.__name__ = "Integer32"
_LPlusRadioPeerRSSIStatus_Object = MibScalar
lPlusRadioPeerRSSIStatus = _LPlusRadioPeerRSSIStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 11),
    _LPlusRadioPeerRSSIStatus_Type()
)
lPlusRadioPeerRSSIStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioPeerRSSIStatus.setStatus("current")
_LPlusRadioLinkStatus_Type = LibraPlusLinkStatus
_LPlusRadioLinkStatus_Object = MibScalar
lPlusRadioLinkStatus = _LPlusRadioLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 12),
    _LPlusRadioLinkStatus_Type()
)
lPlusRadioLinkStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioLinkStatus.setStatus("current")


class _LPlusRadioUpgradeStatus_Type(Integer32):
    """Custom type lPlusRadioUpgradeStatus based on Integer32"""
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
        *(("inprogress", 0),
          ("success", 1),
          ("failed", 2),
          ("incompatible", 3))
    )


_LPlusRadioUpgradeStatus_Type.__name__ = "Integer32"
_LPlusRadioUpgradeStatus_Object = MibScalar
lPlusRadioUpgradeStatus = _LPlusRadioUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 2, 13),
    _LPlusRadioUpgradeStatus_Type()
)
lPlusRadioUpgradeStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lPlusRadioUpgradeStatus.setStatus("current")

# Managed Objects groups

lPlusRadioGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 1)
)
lPlusRadioGenGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioGenLastChange"),
        ("EION-LPLUS-MIB", "lPlusRadioGenNumRows"),
        ("EION-LPLUS-MIB", "lPlusRadioGenAPMode"),
        ("EION-LPLUS-MIB", "lPlusRadioGenBeaconInterval"),
        ("EION-LPLUS-MIB", "lPlusRadioGenChannel"),
        ("EION-LPLUS-MIB", "lPlusRadioGenCountryCode"),
        ("EION-LPLUS-MIB", "lPlusRadioGenFreq"),
        ("EION-LPLUS-MIB", "lPlusRadioGenAuthType"),
        ("EION-LPLUS-MIB", "lPlusRadioGenEncKey"),
        ("EION-LPLUS-MIB", "lPlusRadioGenEncMtd"),
        ("EION-LPLUS-MIB", "lPlusRadioGenAuthKeySrc"),
        ("EION-LPLUS-MIB", "lPlusRadioGenMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioGenIP"),
        ("EION-LPLUS-MIB", "lPlusRadioGenIPMask"),
        ("EION-LPLUS-MIB", "lPlusRadioGenSSID"),
        ("EION-LPLUS-MIB", "lPlusRadioGenHideSSID"),
        ("EION-LPLUS-MIB", "lPlusRadioGenEnableWDS"),
        ("EION-LPLUS-MIB", "lPlusRadioGenEnableWMM"),
        ("EION-LPLUS-MIB", "lPlusRadioGenEnableFF"),
        ("EION-LPLUS-MIB", "lPlusRadioGenEnableBurst"),
        ("EION-LPLUS-MIB", "lPlusRadioGenEnableDFS"),
        ("EION-LPLUS-MIB", "lPlusRadioGenEnableRTS"),
        ("EION-LPLUS-MIB", "lPlusRadioGenDistance"),
        ("EION-LPLUS-MIB", "lPlusRadioGenAPMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioGenLinkStatus"),
        ("EION-LPLUS-MIB", "lPlusRadioGenTxBitrate"),
        ("EION-LPLUS-MIB", "lPlusRadioGenTxPower"),
        ("EION-LPLUS-MIB", "lPlusRadioGenACLName"),
        ("EION-LPLUS-MIB", "lPlusRadioGenACLTableStatus"),
        ("EION-LPLUS-MIB", "lPlusRadioGenChannelWidth"),
        ("EION-LPLUS-MIB", "lPlusRadioGenFragThresh"),
        ("EION-LPLUS-MIB", "lPlusRadioGenOperMode"),
        ("EION-LPLUS-MIB", "lPlusRadioGenIntraSecBridge"),
        ("EION-LPLUS-MIB", "lPlusRadioGenAssociationLimit"))
)
if mibBuilder.loadTexts:
    lPlusRadioGenGroup.setStatus("current")

lPlusRadioPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 2)
)
lPlusRadioPeerGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioPeerLastChange"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerNumRows"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerRadioIndex"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerRSSI"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerNoiseLevel"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerLinkQuality"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerTxBitrate"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerSNR"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerTx"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerRx"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerCAPS"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerFLAGS"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerTxRates"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerRxRates"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerName"))
)
if mibBuilder.loadTexts:
    lPlusRadioPeerGroup.setStatus("current")

lPlusRadioChan2FreqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 3)
)
lPlusRadioChan2FreqGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioChan2FreqLastChange"),
        ("EION-LPLUS-MIB", "lPlusRadioChan2FreqNumRows"),
        ("EION-LPLUS-MIB", "lPlusRadioChan2FreqFrequency"))
)
if mibBuilder.loadTexts:
    lPlusRadioChan2FreqGroup.setStatus("current")

lPlusRadioQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 4)
)
lPlusRadioQosGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioQosLastChange"),
        ("EION-LPLUS-MIB", "lPlusRadioQosNumRows"),
        ("EION-LPLUS-MIB", "lPlusRadioQosRowStatus"),
        ("EION-LPLUS-MIB", "lPlusRadioQosUplinkRate"),
        ("EION-LPLUS-MIB", "lPlusRadioQosDownlinkRate"))
)
if mibBuilder.loadTexts:
    lPlusRadioQosGroup.setStatus("current")

libraPlusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 6)
)
libraPlusGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioLoginStatus"),
        ("EION-LPLUS-MIB", "lPlusPktErrRatePerMin"),
        ("EION-LPLUS-MIB", "lPlusRadioPktRateDirection"),
        ("EION-LPLUS-MIB", "lPlusRadioRebootStatus"),
        ("EION-LPLUS-MIB", "lPlusRadioFrmWareVer"),
        ("EION-LPLUS-MIB", "lPlusRadioAssocStatus"),
        ("EION-LPLUS-MIB", "lPlusRadioAuthStatus"),
        ("EION-LPLUS-MIB", "lPlusRadioWebIP"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerRSSIStatus"),
        ("EION-LPLUS-MIB", "lPlusRadioLinkStatus"),
        ("EION-LPLUS-MIB", "lPlusRadioUpgradeStatus"))
)
if mibBuilder.loadTexts:
    libraPlusGroup.setStatus("current")

lPlusQoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 7)
)
lPlusQoSGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusQoSRowStatus"),
        ("EION-LPLUS-MIB", "lPlusQoSCir"),
        ("EION-LPLUS-MIB", "lPlusQoSMir"))
)
if mibBuilder.loadTexts:
    lPlusQoSGroup.setStatus("current")

lPlusServiceFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 8)
)
lPlusServiceFlowGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusServiceFlowRowStatus"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULQoSTableIndex"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLQoSTableIndex"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULDefault"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLDefault"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULClassDisabled"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULClassVlanId"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULClassVlanPrio"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULClassIpTos"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULClassWmm"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLClassDisabled"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLClassVlanId"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLClassVlanPrio"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLClassIpTos"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLClassWmm"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULValueVlanId"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULValueVlanPrio"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULValueIpTos"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULValueWmm"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLValueVlanId"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLValueVlanPrio"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLValueIpTos"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLValueWmm"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowULAudio"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowDLAudio"))
)
if mibBuilder.loadTexts:
    lPlusServiceFlowGroup.setStatus("current")

lPlusServiceProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 9)
)
lPlusServiceProfileGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusServiceProfileRowStatus"),
        ("EION-LPLUS-MIB", "lPlusServiceProfileScheduleType"),
        ("EION-LPLUS-MIB", "lPlusServiceProfileSF1"),
        ("EION-LPLUS-MIB", "lPlusServiceProfileSF2"),
        ("EION-LPLUS-MIB", "lPlusServiceProfileSF3"),
        ("EION-LPLUS-MIB", "lPlusServiceProfileSF4"))
)
if mibBuilder.loadTexts:
    lPlusServiceProfileGroup.setStatus("current")

lPlusCpeQoSConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 10)
)
lPlusCpeQoSConfigGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusCpeQoSConfigRowStatus"),
        ("EION-LPLUS-MIB", "lPlusCpeQoSConfigName"),
        ("EION-LPLUS-MIB", "lPlusCpeQoSConfigMac"),
        ("EION-LPLUS-MIB", "lPlusCpeQoSConfigSvcProfIndex"))
)
if mibBuilder.loadTexts:
    lPlusCpeQoSConfigGroup.setStatus("current")


# Notification objects

lPlusTrapRadioLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 1)
)
lPlusTrapRadioLink.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioFrmWareVer"),
        ("EION-LPLUS-MIB", "lPlusRadioLinkStatus"))
)
if mibBuilder.loadTexts:
    lPlusTrapRadioLink.setStatus(
        "current"
    )

lPlusTrapRadioPeerAssoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 2)
)
lPlusTrapRadioPeerAssoc.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioPeerMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioAssocStatus"))
)
if mibBuilder.loadTexts:
    lPlusTrapRadioPeerAssoc.setStatus(
        "current"
    )

lPlusTrapRadioAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 3)
)
lPlusTrapRadioAuth.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioPeerMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioAuthStatus"))
)
if mibBuilder.loadTexts:
    lPlusTrapRadioAuth.setStatus(
        "current"
    )

lPlusTrapRadioReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 4)
)
lPlusTrapRadioReboot.setObjects(
    ("EION-LPLUS-MIB", "lPlusRadioRebootStatus")
)
if mibBuilder.loadTexts:
    lPlusTrapRadioReboot.setStatus(
        "current"
    )

lPlusTrapRadioLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 5)
)
lPlusTrapRadioLogin.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioWebIP"),
        ("EION-LPLUS-MIB", "lPlusRadioLoginStatus"))
)
if mibBuilder.loadTexts:
    lPlusTrapRadioLogin.setStatus(
        "current"
    )

lPlusTrapRadioPeerRSSI = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 6)
)
lPlusTrapRadioPeerRSSI.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioPeerMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerRSSIStatus"))
)
if mibBuilder.loadTexts:
    lPlusTrapRadioPeerRSSI.setStatus(
        "current"
    )

lPlusTrapRadioHighPktErrRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 7)
)
lPlusTrapRadioHighPktErrRate.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioGenMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioPktRateDirection"))
)
if mibBuilder.loadTexts:
    lPlusTrapRadioHighPktErrRate.setStatus(
        "current"
    )

lPlusTrapRadioDFSDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 8)
)
lPlusTrapRadioDFSDetection.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioGenMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioGenFreq"))
)
if mibBuilder.loadTexts:
    lPlusTrapRadioDFSDetection.setStatus(
        "current"
    )

lPlusTrapRadioDFSChannelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 9)
)
lPlusTrapRadioDFSChannelChange.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioGenMAC"),
        ("EION-LPLUS-MIB", "lPlusRadioGenFreq"))
)
if mibBuilder.loadTexts:
    lPlusTrapRadioDFSChannelChange.setStatus(
        "current"
    )

lPlusTrapRadioDeAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 10)
)
lPlusTrapRadioDeAuth.setObjects(
    ("EION-LPLUS-MIB", "lPlusRadioPeerMAC")
)
if mibBuilder.loadTexts:
    lPlusTrapRadioDeAuth.setStatus(
        "current"
    )

lPlusTrapRadioUpgradeStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 34226, 2, 0, 11)
)
lPlusTrapRadioUpgradeStatus.setObjects(
    ("EION-LPLUS-MIB", "lPlusRadioUpgradeStatus")
)
if mibBuilder.loadTexts:
    lPlusTrapRadioUpgradeStatus.setStatus(
        "current"
    )


# Notifications groups

lPlusRadioNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 2, 5)
)
lPlusRadioNotificationGroup.setObjects(
      *(("EION-LPLUS-MIB", "lPlusTrapRadioLink"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioPeerAssoc"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioAuth"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioReboot"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioLogin"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioPeerRSSI"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioHighPktErrRate"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioDFSDetection"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioDFSChannelChange"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioDeAuth"),
        ("EION-LPLUS-MIB", "lPlusTrapRadioUpgradeStatus"))
)
if mibBuilder.loadTexts:
    lPlusRadioNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lPlusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34226, 2, 2, 1, 1)
)
lPlusCompliance.setObjects(
      *(("EION-LPLUS-MIB", "lPlusRadioGenGroup"),
        ("EION-LPLUS-MIB", "lPlusRadioPeerGroup"),
        ("EION-LPLUS-MIB", "lPlusRadioChan2FreqGroup"),
        ("EION-LPLUS-MIB", "lPlusRadioQosGroup"),
        ("EION-LPLUS-MIB", "lPlusRadioNotificationGroup"),
        ("EION-LPLUS-MIB", "libraPlusGroup"),
        ("EION-LPLUS-MIB", "lPlusQoSGroup"),
        ("EION-LPLUS-MIB", "lPlusServiceFlowGroup"),
        ("EION-LPLUS-MIB", "lPlusServiceProfileGroup"),
        ("EION-LPLUS-MIB", "lPlusCpeQoSConfigGroup"))
)
if mibBuilder.loadTexts:
    lPlusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EION-LPLUS-MIB",
    **{"EionACLType": EionACLType,
       "LibraPlusLinkStatus": LibraPlusLinkStatus,
       "LibraPlusAPMode": LibraPlusAPMode,
       "LibraPlusAuthType": LibraPlusAuthType,
       "LibraPlusAuthMode": LibraPlusAuthMode,
       "LibraPlusAuthKeySource": LibraPlusAuthKeySource,
       "LibraPlusOperMode": LibraPlusOperMode,
       "LibraPlusWirelessCountryCode": LibraPlusWirelessCountryCode,
       "LibraPlusTrafficShapingMode": LibraPlusTrafficShapingMode,
       "libraPlusMIB": libraPlusMIB,
       "lPlusNotifications": lPlusNotifications,
       "lPlusTrapRadioLink": lPlusTrapRadioLink,
       "lPlusTrapRadioPeerAssoc": lPlusTrapRadioPeerAssoc,
       "lPlusTrapRadioAuth": lPlusTrapRadioAuth,
       "lPlusTrapRadioReboot": lPlusTrapRadioReboot,
       "lPlusTrapRadioLogin": lPlusTrapRadioLogin,
       "lPlusTrapRadioPeerRSSI": lPlusTrapRadioPeerRSSI,
       "lPlusTrapRadioHighPktErrRate": lPlusTrapRadioHighPktErrRate,
       "lPlusTrapRadioDFSDetection": lPlusTrapRadioDFSDetection,
       "lPlusTrapRadioDFSChannelChange": lPlusTrapRadioDFSChannelChange,
       "lPlusTrapRadioDeAuth": lPlusTrapRadioDeAuth,
       "lPlusTrapRadioUpgradeStatus": lPlusTrapRadioUpgradeStatus,
       "lPlusObjects": lPlusObjects,
       "lPlusRadioGenLastChange": lPlusRadioGenLastChange,
       "lPlusRadioGenNumRows": lPlusRadioGenNumRows,
       "lPlusRadioGenTable": lPlusRadioGenTable,
       "lPlusRadioGenTableEntry": lPlusRadioGenTableEntry,
       "lPlusRadioGenIndex": lPlusRadioGenIndex,
       "lPlusRadioGenAPMode": lPlusRadioGenAPMode,
       "lPlusRadioGenBeaconInterval": lPlusRadioGenBeaconInterval,
       "lPlusRadioGenChannel": lPlusRadioGenChannel,
       "lPlusRadioGenCountryCode": lPlusRadioGenCountryCode,
       "lPlusRadioGenFreq": lPlusRadioGenFreq,
       "lPlusRadioGenAuthType": lPlusRadioGenAuthType,
       "lPlusRadioGenEncKey": lPlusRadioGenEncKey,
       "lPlusRadioGenEncMtd": lPlusRadioGenEncMtd,
       "lPlusRadioGenAuthKeySrc": lPlusRadioGenAuthKeySrc,
       "lPlusRadioGenMAC": lPlusRadioGenMAC,
       "lPlusRadioGenIP": lPlusRadioGenIP,
       "lPlusRadioGenIPMask": lPlusRadioGenIPMask,
       "lPlusRadioGenSSID": lPlusRadioGenSSID,
       "lPlusRadioGenHideSSID": lPlusRadioGenHideSSID,
       "lPlusRadioGenEnableWDS": lPlusRadioGenEnableWDS,
       "lPlusRadioGenEnableWMM": lPlusRadioGenEnableWMM,
       "lPlusRadioGenEnableFF": lPlusRadioGenEnableFF,
       "lPlusRadioGenEnableBurst": lPlusRadioGenEnableBurst,
       "lPlusRadioGenEnableDFS": lPlusRadioGenEnableDFS,
       "lPlusRadioGenEnableRTS": lPlusRadioGenEnableRTS,
       "lPlusRadioGenDistance": lPlusRadioGenDistance,
       "lPlusRadioGenAPMAC": lPlusRadioGenAPMAC,
       "lPlusRadioGenLinkStatus": lPlusRadioGenLinkStatus,
       "lPlusRadioGenTxBitrate": lPlusRadioGenTxBitrate,
       "lPlusRadioGenTxPower": lPlusRadioGenTxPower,
       "lPlusRadioGenACLName": lPlusRadioGenACLName,
       "lPlusRadioGenACLTableStatus": lPlusRadioGenACLTableStatus,
       "lPlusRadioGenChannelWidth": lPlusRadioGenChannelWidth,
       "lPlusRadioGenFragThresh": lPlusRadioGenFragThresh,
       "lPlusRadioGenOperMode": lPlusRadioGenOperMode,
       "lPlusRadioGenIntraSecBridge": lPlusRadioGenIntraSecBridge,
       "lPlusRadioGenAssociationLimit": lPlusRadioGenAssociationLimit,
       "lPlusRadioPeerLastChange": lPlusRadioPeerLastChange,
       "lPlusRadioPeerNumRows": lPlusRadioPeerNumRows,
       "lPlusRadioPeerTable": lPlusRadioPeerTable,
       "lPlusRadioPeerEntry": lPlusRadioPeerEntry,
       "lPlusRadioPeerIndex": lPlusRadioPeerIndex,
       "lPlusRadioPeerRadioIndex": lPlusRadioPeerRadioIndex,
       "lPlusRadioPeerMAC": lPlusRadioPeerMAC,
       "lPlusRadioPeerRSSI": lPlusRadioPeerRSSI,
       "lPlusRadioPeerNoiseLevel": lPlusRadioPeerNoiseLevel,
       "lPlusRadioPeerLinkQuality": lPlusRadioPeerLinkQuality,
       "lPlusRadioPeerTxBitrate": lPlusRadioPeerTxBitrate,
       "lPlusRadioPeerSNR": lPlusRadioPeerSNR,
       "lPlusRadioPeerTx": lPlusRadioPeerTx,
       "lPlusRadioPeerRx": lPlusRadioPeerRx,
       "lPlusRadioPeerCAPS": lPlusRadioPeerCAPS,
       "lPlusRadioPeerFLAGS": lPlusRadioPeerFLAGS,
       "lPlusRadioPeerTxRates": lPlusRadioPeerTxRates,
       "lPlusRadioPeerRxRates": lPlusRadioPeerRxRates,
       "lPlusRadioPeerName": lPlusRadioPeerName,
       "lPlusRadioChan2FreqLastChange": lPlusRadioChan2FreqLastChange,
       "lPlusRadioChan2FreqNumRows": lPlusRadioChan2FreqNumRows,
       "lPlusRadioChan2FreqTable": lPlusRadioChan2FreqTable,
       "lPlusRadioChan2FreqEntry": lPlusRadioChan2FreqEntry,
       "lPlusRadioChan2FreqRadioIndex": lPlusRadioChan2FreqRadioIndex,
       "lPlusRadioChan2FreqChannel": lPlusRadioChan2FreqChannel,
       "lPlusRadioChan2FreqFrequency": lPlusRadioChan2FreqFrequency,
       "lPlusRadioQosLastChange": lPlusRadioQosLastChange,
       "lPlusRadioQosNumRows": lPlusRadioQosNumRows,
       "lPlusRadioQosTable": lPlusRadioQosTable,
       "lPlusRadioQosEntry": lPlusRadioQosEntry,
       "lPlusRadioQosName": lPlusRadioQosName,
       "lPlusRadioQosRowStatus": lPlusRadioQosRowStatus,
       "lPlusRadioQosUplinkRate": lPlusRadioQosUplinkRate,
       "lPlusRadioQosDownlinkRate": lPlusRadioQosDownlinkRate,
       "lPlusQoSTable": lPlusQoSTable,
       "lPlusQoSEntry": lPlusQoSEntry,
       "lPlusQoSIndex": lPlusQoSIndex,
       "lPlusQoSRowStatus": lPlusQoSRowStatus,
       "lPlusQoSCir": lPlusQoSCir,
       "lPlusQoSMir": lPlusQoSMir,
       "lPlusServiceFlowTable": lPlusServiceFlowTable,
       "lPlusServiceFlowEntry": lPlusServiceFlowEntry,
       "lPlusServiceFlowIndex": lPlusServiceFlowIndex,
       "lPlusServiceFlowRowStatus": lPlusServiceFlowRowStatus,
       "lPlusServiceFlowULQoSTableIndex": lPlusServiceFlowULQoSTableIndex,
       "lPlusServiceFlowDLQoSTableIndex": lPlusServiceFlowDLQoSTableIndex,
       "lPlusServiceFlowULDefault": lPlusServiceFlowULDefault,
       "lPlusServiceFlowDLDefault": lPlusServiceFlowDLDefault,
       "lPlusServiceFlowULClassDisabled": lPlusServiceFlowULClassDisabled,
       "lPlusServiceFlowULClassVlanId": lPlusServiceFlowULClassVlanId,
       "lPlusServiceFlowULClassVlanPrio": lPlusServiceFlowULClassVlanPrio,
       "lPlusServiceFlowULClassIpTos": lPlusServiceFlowULClassIpTos,
       "lPlusServiceFlowULClassWmm": lPlusServiceFlowULClassWmm,
       "lPlusServiceFlowDLClassDisabled": lPlusServiceFlowDLClassDisabled,
       "lPlusServiceFlowDLClassVlanId": lPlusServiceFlowDLClassVlanId,
       "lPlusServiceFlowDLClassVlanPrio": lPlusServiceFlowDLClassVlanPrio,
       "lPlusServiceFlowDLClassIpTos": lPlusServiceFlowDLClassIpTos,
       "lPlusServiceFlowDLClassWmm": lPlusServiceFlowDLClassWmm,
       "lPlusServiceFlowULValueVlanId": lPlusServiceFlowULValueVlanId,
       "lPlusServiceFlowULValueVlanPrio": lPlusServiceFlowULValueVlanPrio,
       "lPlusServiceFlowULValueIpTos": lPlusServiceFlowULValueIpTos,
       "lPlusServiceFlowULValueWmm": lPlusServiceFlowULValueWmm,
       "lPlusServiceFlowDLValueVlanId": lPlusServiceFlowDLValueVlanId,
       "lPlusServiceFlowDLValueVlanPrio": lPlusServiceFlowDLValueVlanPrio,
       "lPlusServiceFlowDLValueIpTos": lPlusServiceFlowDLValueIpTos,
       "lPlusServiceFlowDLValueWmm": lPlusServiceFlowDLValueWmm,
       "lPlusServiceFlowULAudio": lPlusServiceFlowULAudio,
       "lPlusServiceFlowDLAudio": lPlusServiceFlowDLAudio,
       "lPlusServiceProfileTable": lPlusServiceProfileTable,
       "lPlusServiceProfileEntry": lPlusServiceProfileEntry,
       "lPlusServiceProfileIndex": lPlusServiceProfileIndex,
       "lPlusServiceProfileRowStatus": lPlusServiceProfileRowStatus,
       "lPlusServiceProfileScheduleType": lPlusServiceProfileScheduleType,
       "lPlusServiceProfileSF1": lPlusServiceProfileSF1,
       "lPlusServiceProfileSF2": lPlusServiceProfileSF2,
       "lPlusServiceProfileSF3": lPlusServiceProfileSF3,
       "lPlusServiceProfileSF4": lPlusServiceProfileSF4,
       "lPlusCpeQoSConfigTable": lPlusCpeQoSConfigTable,
       "lPlusCpeQoSConfigEntry": lPlusCpeQoSConfigEntry,
       "lPlusCpeQoSConfigIndex": lPlusCpeQoSConfigIndex,
       "lPlusCpeQoSConfigRowStatus": lPlusCpeQoSConfigRowStatus,
       "lPlusCpeQoSConfigName": lPlusCpeQoSConfigName,
       "lPlusCpeQoSConfigMac": lPlusCpeQoSConfigMac,
       "lPlusCpeQoSConfigSvcProfIndex": lPlusCpeQoSConfigSvcProfIndex,
       "lPlusConformance": lPlusConformance,
       "lPlusCompliances": lPlusCompliances,
       "lPlusCompliance": lPlusCompliance,
       "lPlusGroups": lPlusGroups,
       "lPlusRadioGenGroup": lPlusRadioGenGroup,
       "lPlusRadioPeerGroup": lPlusRadioPeerGroup,
       "lPlusRadioChan2FreqGroup": lPlusRadioChan2FreqGroup,
       "lPlusRadioQosGroup": lPlusRadioQosGroup,
       "lPlusRadioNotificationGroup": lPlusRadioNotificationGroup,
       "libraPlusGroup": libraPlusGroup,
       "lPlusQoSGroup": lPlusQoSGroup,
       "lPlusServiceFlowGroup": lPlusServiceFlowGroup,
       "lPlusServiceProfileGroup": lPlusServiceProfileGroup,
       "lPlusCpeQoSConfigGroup": lPlusCpeQoSConfigGroup,
       "lPlusRadioLoginStatus": lPlusRadioLoginStatus,
       "lPlusPktErrRatePerMin": lPlusPktErrRatePerMin,
       "lPlusRadioPktRateDirection": lPlusRadioPktRateDirection,
       "lPlusRadioRebootStatus": lPlusRadioRebootStatus,
       "lPlusRadioFrmWareVer": lPlusRadioFrmWareVer,
       "lPlusRadioAssocStatus": lPlusRadioAssocStatus,
       "lPlusRadioAuthStatus": lPlusRadioAuthStatus,
       "lPlusRadioWebIP": lPlusRadioWebIP,
       "lPlusRadioPeerRSSIStatus": lPlusRadioPeerRSSIStatus,
       "lPlusRadioLinkStatus": lPlusRadioLinkStatus,
       "lPlusRadioUpgradeStatus": lPlusRadioUpgradeStatus}
)
