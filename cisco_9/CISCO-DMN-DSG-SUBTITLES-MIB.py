# SNMP MIB module (CISCO-DMN-DSG-SUBTITLES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DMN-DSG-SUBTITLES-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:04:33 2025
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGSubtitle = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16)
)
if mibBuilder.loadTexts:
    ciscoDSGSubtitle.setRevisions(
        ("2013-07-10 12:20",
         "2010-08-30 11:00",
         "2009-12-07 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SubtitlesOPMode_Type(Integer32):
    """Custom type subtitlesOPMode based on Integer32"""
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
          ("on", 2),
          ("imiText", 3),
          ("dvb", 4))
    )


_SubtitlesOPMode_Type.__name__ = "Integer32"
_SubtitlesOPMode_Object = MibScalar
subtitlesOPMode = _SubtitlesOPMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 1),
    _SubtitlesOPMode_Type()
)
subtitlesOPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitlesOPMode.setStatus("current")


class _SubtitlesLangMenu_Type(Integer32):
    """Custom type subtitlesLangMenu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("languageList", 1),
          ("languageEntry", 2),
          ("pmtOrder", 3))
    )


_SubtitlesLangMenu_Type.__name__ = "Integer32"
_SubtitlesLangMenu_Object = MibScalar
subtitlesLangMenu = _SubtitlesLangMenu_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 2),
    _SubtitlesLangMenu_Type()
)
subtitlesLangMenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitlesLangMenu.setStatus("current")


class _SubtitlesLangList_Type(Integer32):
    """Custom type subtitlesLangList based on Integer32"""
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
              43)
        )
    )
    namedValues = NamedValues(
        *(("ara", 1),
          ("btk", 2),
          ("ben", 3),
          ("bul", 4),
          ("chi", 5),
          ("cze", 6),
          ("dan", 7),
          ("dut", 8),
          ("eng", 9),
          ("fin", 10),
          ("fre", 11),
          ("ger", 12),
          ("gre", 13),
          ("heb", 14),
          ("hin", 15),
          ("hun", 16),
          ("ice", 17),
          ("ind", 18),
          ("ita", 19),
          ("jpn", 20),
          ("kor", 21),
          ("may", 22),
          ("mul", 23),
          ("nor", 24),
          ("per", 25),
          ("pol", 26),
          ("por", 27),
          ("rum", 28),
          ("rus", 29),
          ("san", 30),
          ("scc", 31),
          ("sin", 32),
          ("slo", 33),
          ("slv", 34),
          ("som", 35),
          ("spa", 36),
          ("swe", 37),
          ("tai", 38),
          ("tam", 39),
          ("tha", 40),
          ("tur", 41),
          ("ukr", 42),
          ("vie", 43))
    )


_SubtitlesLangList_Type.__name__ = "Integer32"
_SubtitlesLangList_Object = MibScalar
subtitlesLangList = _SubtitlesLangList_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 3),
    _SubtitlesLangList_Type()
)
subtitlesLangList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitlesLangList.setStatus("current")


class _SubtitlesPMTOrder_Type(Integer32):
    """Custom type subtitlesPMTOrder based on Integer32"""
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
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("fifth", 5),
          ("sixth", 6),
          ("seventh", 7),
          ("eighth", 8))
    )


_SubtitlesPMTOrder_Type.__name__ = "Integer32"
_SubtitlesPMTOrder_Object = MibScalar
subtitlesPMTOrder = _SubtitlesPMTOrder_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 4),
    _SubtitlesPMTOrder_Type()
)
subtitlesPMTOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitlesPMTOrder.setStatus("current")


class _SubtitlesManualEntry_Type(DisplayString):
    """Custom type subtitlesManualEntry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SubtitlesManualEntry_Type.__name__ = "DisplayString"
_SubtitlesManualEntry_Object = MibScalar
subtitlesManualEntry = _SubtitlesManualEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 5),
    _SubtitlesManualEntry_Type()
)
subtitlesManualEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitlesManualEntry.setStatus("current")


class _SubtitlesIMITextPos_Type(Integer32):
    """Custom type subtitlesIMITextPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("extended", 2))
    )


_SubtitlesIMITextPos_Type.__name__ = "Integer32"
_SubtitlesIMITextPos_Object = MibScalar
subtitlesIMITextPos = _SubtitlesIMITextPos_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 6),
    _SubtitlesIMITextPos_Type()
)
subtitlesIMITextPos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitlesIMITextPos.setStatus("current")


class _SubtitlesForeGround_Type(Integer32):
    """Custom type subtitlesForeGround based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("yellow", 2),
          ("white", 3))
    )


_SubtitlesForeGround_Type.__name__ = "Integer32"
_SubtitlesForeGround_Object = MibScalar
subtitlesForeGround = _SubtitlesForeGround_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 7),
    _SubtitlesForeGround_Type()
)
subtitlesForeGround.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitlesForeGround.setStatus("current")


class _SubtitlesBackGround_Type(Integer32):
    """Custom type subtitlesBackGround based on Integer32"""
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
        *(("none", 1),
          ("auto", 2),
          ("shadow", 3),
          ("opaque", 4),
          ("semi", 5))
    )


_SubtitlesBackGround_Type.__name__ = "Integer32"
_SubtitlesBackGround_Object = MibScalar
subtitlesBackGround = _SubtitlesBackGround_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 8),
    _SubtitlesBackGround_Type()
)
subtitlesBackGround.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitlesBackGround.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-SUBTITLES-MIB",
    **{"ciscoDSGSubtitle": ciscoDSGSubtitle,
       "subtitlesOPMode": subtitlesOPMode,
       "subtitlesLangMenu": subtitlesLangMenu,
       "subtitlesLangList": subtitlesLangList,
       "subtitlesPMTOrder": subtitlesPMTOrder,
       "subtitlesManualEntry": subtitlesManualEntry,
       "subtitlesIMITextPos": subtitlesIMITextPos,
       "subtitlesForeGround": subtitlesForeGround,
       "subtitlesBackGround": subtitlesBackGround}
)
