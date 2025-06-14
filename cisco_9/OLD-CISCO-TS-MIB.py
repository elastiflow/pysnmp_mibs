# SNMP MIB module (OLD-CISCO-TS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/OLD-CISCO-TS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:08 2025
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lts_ObjectIdentity = ObjectIdentity
lts = _Lts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 9)
)
_TsLines_Type = Integer32
_TsLines_Object = MibScalar
tsLines = _TsLines_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 1),
    _TsLines_Type()
)
tsLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLines.setStatus("deprecated")
_LtsLineTable_Object = MibTable
ltsLineTable = _LtsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2)
)
if mibBuilder.loadTexts:
    ltsLineTable.setStatus("deprecated")
_LtsLineEntry_Object = MibTableRow
ltsLineEntry = _LtsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1)
)
ltsLineEntry.setIndexNames(
    (0, "OLD-CISCO-TS-MIB", "tsLineNumber"),
)
if mibBuilder.loadTexts:
    ltsLineEntry.setStatus("deprecated")
_TsLineActive_Type = Integer32
_TsLineActive_Object = MibTableColumn
tsLineActive = _TsLineActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 1),
    _TsLineActive_Type()
)
tsLineActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineActive.setStatus("deprecated")


class _TsLineType_Type(Integer32):
    """Custom type tsLineType based on Integer32"""
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
        *(("unknown", 1),
          ("console", 2),
          ("terminal", 3),
          ("line-printer", 4),
          ("virtual-terminal", 5),
          ("auxiliary", 6))
    )


_TsLineType_Type.__name__ = "Integer32"
_TsLineType_Object = MibTableColumn
tsLineType = _TsLineType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 2),
    _TsLineType_Type()
)
tsLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineType.setStatus("deprecated")
_TsLineAutobaud_Type = Integer32
_TsLineAutobaud_Object = MibTableColumn
tsLineAutobaud = _TsLineAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 3),
    _TsLineAutobaud_Type()
)
tsLineAutobaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineAutobaud.setStatus("deprecated")
_TsLineSpeedin_Type = Integer32
_TsLineSpeedin_Object = MibTableColumn
tsLineSpeedin = _TsLineSpeedin_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 4),
    _TsLineSpeedin_Type()
)
tsLineSpeedin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineSpeedin.setStatus("deprecated")
_TsLineSpeedout_Type = Integer32
_TsLineSpeedout_Object = MibTableColumn
tsLineSpeedout = _TsLineSpeedout_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 5),
    _TsLineSpeedout_Type()
)
tsLineSpeedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineSpeedout.setStatus("deprecated")


class _TsLineFlow_Type(Integer32):
    """Custom type tsLineFlow based on Integer32"""
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
        *(("unknown", 1),
          ("none", 2),
          ("software-input", 3),
          ("software-output", 4),
          ("software-both", 5),
          ("hardware-input", 6),
          ("hardware-output", 7),
          ("hardware-both", 8))
    )


_TsLineFlow_Type.__name__ = "Integer32"
_TsLineFlow_Object = MibTableColumn
tsLineFlow = _TsLineFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 6),
    _TsLineFlow_Type()
)
tsLineFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineFlow.setStatus("deprecated")


class _TsLineModem_Type(Integer32):
    """Custom type tsLineModem based on Integer32"""
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
        *(("unknown", 1),
          ("none", 2),
          ("call-in", 3),
          ("call-out", 4),
          ("cts-required", 5),
          ("ri-is-cd", 6),
          ("inout", 7))
    )


_TsLineModem_Type.__name__ = "Integer32"
_TsLineModem_Object = MibTableColumn
tsLineModem = _TsLineModem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 7),
    _TsLineModem_Type()
)
tsLineModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineModem.setStatus("deprecated")
_TsLineLoc_Type = DisplayString
_TsLineLoc_Object = MibTableColumn
tsLineLoc = _TsLineLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 8),
    _TsLineLoc_Type()
)
tsLineLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineLoc.setStatus("deprecated")
_TsLineTerm_Type = DisplayString
_TsLineTerm_Object = MibTableColumn
tsLineTerm = _TsLineTerm_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 9),
    _TsLineTerm_Type()
)
tsLineTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineTerm.setStatus("deprecated")
_TsLineScrlen_Type = Integer32
_TsLineScrlen_Object = MibTableColumn
tsLineScrlen = _TsLineScrlen_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 10),
    _TsLineScrlen_Type()
)
tsLineScrlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineScrlen.setStatus("deprecated")
_TsLineScrwid_Type = Integer32
_TsLineScrwid_Object = MibTableColumn
tsLineScrwid = _TsLineScrwid_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 11),
    _TsLineScrwid_Type()
)
tsLineScrwid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineScrwid.setStatus("deprecated")
_TsLineEsc_Type = DisplayString
_TsLineEsc_Object = MibTableColumn
tsLineEsc = _TsLineEsc_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 12),
    _TsLineEsc_Type()
)
tsLineEsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineEsc.setStatus("deprecated")
_TsLineTmo_Type = Integer32
_TsLineTmo_Object = MibTableColumn
tsLineTmo = _TsLineTmo_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 13),
    _TsLineTmo_Type()
)
tsLineTmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineTmo.setStatus("deprecated")
_TsLineSestmo_Type = Integer32
_TsLineSestmo_Object = MibTableColumn
tsLineSestmo = _TsLineSestmo_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 14),
    _TsLineSestmo_Type()
)
tsLineSestmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineSestmo.setStatus("deprecated")
_TsLineRotary_Type = Integer32
_TsLineRotary_Object = MibTableColumn
tsLineRotary = _TsLineRotary_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 15),
    _TsLineRotary_Type()
)
tsLineRotary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineRotary.setStatus("deprecated")
_TsLineUses_Type = Integer32
_TsLineUses_Object = MibTableColumn
tsLineUses = _TsLineUses_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 16),
    _TsLineUses_Type()
)
tsLineUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineUses.setStatus("deprecated")
_TsLineNses_Type = Integer32
_TsLineNses_Object = MibTableColumn
tsLineNses = _TsLineNses_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 17),
    _TsLineNses_Type()
)
tsLineNses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineNses.setStatus("deprecated")
_TsLineUser_Type = DisplayString
_TsLineUser_Object = MibTableColumn
tsLineUser = _TsLineUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 18),
    _TsLineUser_Type()
)
tsLineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineUser.setStatus("deprecated")
_TsLineNoise_Type = Integer32
_TsLineNoise_Object = MibTableColumn
tsLineNoise = _TsLineNoise_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 19),
    _TsLineNoise_Type()
)
tsLineNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineNoise.setStatus("deprecated")
_TsLineNumber_Type = Integer32
_TsLineNumber_Object = MibTableColumn
tsLineNumber = _TsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 20),
    _TsLineNumber_Type()
)
tsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineNumber.setStatus("deprecated")
_TsLineTimeActive_Type = Integer32
_TsLineTimeActive_Object = MibTableColumn
tsLineTimeActive = _TsLineTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 21),
    _TsLineTimeActive_Type()
)
tsLineTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineTimeActive.setStatus("deprecated")
_LtsLineSessionTable_Object = MibTable
ltsLineSessionTable = _LtsLineSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3)
)
if mibBuilder.loadTexts:
    ltsLineSessionTable.setStatus("deprecated")
_LtsLineSessionEntry_Object = MibTableRow
ltsLineSessionEntry = _LtsLineSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1)
)
ltsLineSessionEntry.setIndexNames(
    (0, "OLD-CISCO-TS-MIB", "tslineSesLine"),
    (0, "OLD-CISCO-TS-MIB", "tslineSesSession"),
)
if mibBuilder.loadTexts:
    ltsLineSessionEntry.setStatus("deprecated")


class _TslineSesType_Type(Integer32):
    """Custom type tslineSesType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("pad", 2),
          ("stream", 3),
          ("rlogin", 4),
          ("telnet", 5),
          ("tcp", 6),
          ("lat", 7),
          ("mop", 8),
          ("slip", 9),
          ("xremote", 10),
          ("rshell", 11),
          ("ipc", 12),
          ("udptn", 13))
    )


_TslineSesType_Type.__name__ = "Integer32"
_TslineSesType_Object = MibTableColumn
tslineSesType = _TslineSesType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 1),
    _TslineSesType_Type()
)
tslineSesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesType.setStatus("deprecated")


class _TslineSesDir_Type(Integer32):
    """Custom type tslineSesDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_TslineSesDir_Type.__name__ = "Integer32"
_TslineSesDir_Object = MibTableColumn
tslineSesDir = _TslineSesDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 2),
    _TslineSesDir_Type()
)
tslineSesDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesDir.setStatus("deprecated")
_TslineSesAddr_Type = IpAddress
_TslineSesAddr_Object = MibTableColumn
tslineSesAddr = _TslineSesAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 3),
    _TslineSesAddr_Type()
)
tslineSesAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesAddr.setStatus("deprecated")
_TslineSesName_Type = DisplayString
_TslineSesName_Object = MibTableColumn
tslineSesName = _TslineSesName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 4),
    _TslineSesName_Type()
)
tslineSesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesName.setStatus("deprecated")
_TslineSesCur_Type = Integer32
_TslineSesCur_Object = MibTableColumn
tslineSesCur = _TslineSesCur_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 5),
    _TslineSesCur_Type()
)
tslineSesCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesCur.setStatus("deprecated")
_TslineSesIdle_Type = Integer32
_TslineSesIdle_Object = MibTableColumn
tslineSesIdle = _TslineSesIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 6),
    _TslineSesIdle_Type()
)
tslineSesIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesIdle.setStatus("deprecated")
_TslineSesLine_Type = Integer32
_TslineSesLine_Object = MibTableColumn
tslineSesLine = _TslineSesLine_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 7),
    _TslineSesLine_Type()
)
tslineSesLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesLine.setStatus("deprecated")
_TslineSesSession_Type = Integer32
_TslineSesSession_Object = MibTableColumn
tslineSesSession = _TslineSesSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 8),
    _TslineSesSession_Type()
)
tslineSesSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesSession.setStatus("deprecated")
_TsMsgTtyLine_Type = Integer32
_TsMsgTtyLine_Object = MibScalar
tsMsgTtyLine = _TsMsgTtyLine_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 4),
    _TsMsgTtyLine_Type()
)
tsMsgTtyLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgTtyLine.setStatus("deprecated")
_TsMsgIntervaltim_Type = Integer32
_TsMsgIntervaltim_Object = MibScalar
tsMsgIntervaltim = _TsMsgIntervaltim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 5),
    _TsMsgIntervaltim_Type()
)
tsMsgIntervaltim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgIntervaltim.setStatus("deprecated")
_TsMsgDuration_Type = Integer32
_TsMsgDuration_Object = MibScalar
tsMsgDuration = _TsMsgDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 6),
    _TsMsgDuration_Type()
)
tsMsgDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgDuration.setStatus("deprecated")
_TsMsgText_Type = DisplayString
_TsMsgText_Object = MibScalar
tsMsgText = _TsMsgText_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 7),
    _TsMsgText_Type()
)
tsMsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgText.setStatus("deprecated")


class _TsMsgTmpBanner_Type(Integer32):
    """Custom type tsMsgTmpBanner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("additive", 2))
    )


_TsMsgTmpBanner_Type.__name__ = "Integer32"
_TsMsgTmpBanner_Object = MibScalar
tsMsgTmpBanner = _TsMsgTmpBanner_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 8),
    _TsMsgTmpBanner_Type()
)
tsMsgTmpBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgTmpBanner.setStatus("deprecated")


class _TsMsgSend_Type(Integer32):
    """Custom type tsMsgSend based on Integer32"""
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
        *(("nothing", 1),
          ("reload", 2),
          ("messagedone", 3),
          ("abort", 4))
    )


_TsMsgSend_Type.__name__ = "Integer32"
_TsMsgSend_Object = MibScalar
tsMsgSend = _TsMsgSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 9),
    _TsMsgSend_Type()
)
tsMsgSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgSend.setStatus("deprecated")
_TsClrTtyLine_Type = Integer32
_TsClrTtyLine_Object = MibScalar
tsClrTtyLine = _TsClrTtyLine_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 10),
    _TsClrTtyLine_Type()
)
tsClrTtyLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsClrTtyLine.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-TS-MIB",
    **{"lts": lts,
       "tsLines": tsLines,
       "ltsLineTable": ltsLineTable,
       "ltsLineEntry": ltsLineEntry,
       "tsLineActive": tsLineActive,
       "tsLineType": tsLineType,
       "tsLineAutobaud": tsLineAutobaud,
       "tsLineSpeedin": tsLineSpeedin,
       "tsLineSpeedout": tsLineSpeedout,
       "tsLineFlow": tsLineFlow,
       "tsLineModem": tsLineModem,
       "tsLineLoc": tsLineLoc,
       "tsLineTerm": tsLineTerm,
       "tsLineScrlen": tsLineScrlen,
       "tsLineScrwid": tsLineScrwid,
       "tsLineEsc": tsLineEsc,
       "tsLineTmo": tsLineTmo,
       "tsLineSestmo": tsLineSestmo,
       "tsLineRotary": tsLineRotary,
       "tsLineUses": tsLineUses,
       "tsLineNses": tsLineNses,
       "tsLineUser": tsLineUser,
       "tsLineNoise": tsLineNoise,
       "tsLineNumber": tsLineNumber,
       "tsLineTimeActive": tsLineTimeActive,
       "ltsLineSessionTable": ltsLineSessionTable,
       "ltsLineSessionEntry": ltsLineSessionEntry,
       "tslineSesType": tslineSesType,
       "tslineSesDir": tslineSesDir,
       "tslineSesAddr": tslineSesAddr,
       "tslineSesName": tslineSesName,
       "tslineSesCur": tslineSesCur,
       "tslineSesIdle": tslineSesIdle,
       "tslineSesLine": tslineSesLine,
       "tslineSesSession": tslineSesSession,
       "tsMsgTtyLine": tsMsgTtyLine,
       "tsMsgIntervaltim": tsMsgIntervaltim,
       "tsMsgDuration": tsMsgDuration,
       "tsMsgText": tsMsgText,
       "tsMsgTmpBanner": tsMsgTmpBanner,
       "tsMsgSend": tsMsgSend,
       "tsClrTtyLine": tsClrTtyLine}
)
