# SNMP MIB module (NDS-DTH3-MUX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-MUX.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MuxEnc_ObjectIdentity = ObjectIdentity
muxEnc = _MuxEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2)
)


class _MuxVersion_Type(DisplayString):
    """Custom type muxVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MuxVersion_Type.__name__ = "DisplayString"
_MuxVersion_Object = MibScalar
muxVersion = _MuxVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 1),
    _MuxVersion_Type()
)
muxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVersion.setStatus("current")
_MuxnextTimeDate_Type = DateAndTime
_MuxnextTimeDate_Object = MibScalar
muxnextTimeDate = _MuxnextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 2),
    _MuxnextTimeDate_Type()
)
muxnextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxnextTimeDate.setStatus("current")
_MuxTable_Object = MibTable
muxTable = _MuxTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    muxTable.setStatus("current")
_MuxEntry_Object = MibTableRow
muxEntry = _MuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1)
)
muxEntry.setIndexNames(
    (0, "NDS-DTH3-MUX", "muxCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    muxEntry.setStatus("current")


class _MuxCurrentNextIndex_Type(Integer32):
    """Custom type muxCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_MuxCurrentNextIndex_Type.__name__ = "Integer32"
_MuxCurrentNextIndex_Object = MibTableColumn
muxCurrentNextIndex = _MuxCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 1),
    _MuxCurrentNextIndex_Type()
)
muxCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxCurrentNextIndex.setStatus("current")


class _MuxFormat_Type(Integer32):
    """Custom type muxFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("baseband", 0),
          ("iFOutput", 1))
    )


_MuxFormat_Type.__name__ = "Integer32"
_MuxFormat_Object = MibTableColumn
muxFormat = _MuxFormat_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 2),
    _MuxFormat_Type()
)
muxFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxFormat.setStatus("current")


class _MuxOnAir_Type(Integer32):
    """Custom type muxOnAir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MuxOnAir_Type.__name__ = "Integer32"
_MuxOnAir_Object = MibTableColumn
muxOnAir = _MuxOnAir_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 3),
    _MuxOnAir_Type()
)
muxOnAir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxOnAir.setStatus("current")


class _MuxOpMode_Type(Integer32):
    """Custom type muxOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("proprietary", 0),
          ("transport", 1))
    )


_MuxOpMode_Type.__name__ = "Integer32"
_MuxOpMode_Object = MibTableColumn
muxOpMode = _MuxOpMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 4),
    _MuxOpMode_Type()
)
muxOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxOpMode.setStatus("current")


class _MuxBitRate_Type(Integer32):
    """Custom type muxBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160000000),
    )


_MuxBitRate_Type.__name__ = "Integer32"
_MuxBitRate_Object = MibTableColumn
muxBitRate = _MuxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 5),
    _MuxBitRate_Type()
)
muxBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxBitRate.setStatus("current")


class _MuxClock_Type(Integer32):
    """Custom type muxClock based on Integer32"""
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
        *(("xtal", 0),
          ("video", 1),
          ("tAXI", 2),
          ("hsync", 3))
    )


_MuxClock_Type.__name__ = "Integer32"
_MuxClock_Object = MibTableColumn
muxClock = _MuxClock_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 6),
    _MuxClock_Type()
)
muxClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxClock.setStatus("current")


class _MuxAutoPriority_Type(Integer32):
    """Custom type muxAutoPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MuxAutoPriority_Type.__name__ = "Integer32"
_MuxAutoPriority_Object = MibTableColumn
muxAutoPriority = _MuxAutoPriority_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 7),
    _MuxAutoPriority_Type()
)
muxAutoPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxAutoPriority.setStatus("current")


class _MuxAutoPID_Type(Integer32):
    """Custom type muxAutoPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MuxAutoPID_Type.__name__ = "Integer32"
_MuxAutoPID_Object = MibTableColumn
muxAutoPID = _MuxAutoPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 8),
    _MuxAutoPID_Type()
)
muxAutoPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxAutoPID.setStatus("current")


class _MuxPCRSource_Type(Integer32):
    """Custom type muxPCRSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_MuxPCRSource_Type.__name__ = "Integer32"
_MuxPCRSource_Object = MibTableColumn
muxPCRSource = _MuxPCRSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 9),
    _MuxPCRSource_Type()
)
muxPCRSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxPCRSource.setStatus("current")


class _MuxPCRPID_Type(Integer32):
    """Custom type muxPCRPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_MuxPCRPID_Type.__name__ = "Integer32"
_MuxPCRPID_Object = MibTableColumn
muxPCRPID = _MuxPCRPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 10),
    _MuxPCRPID_Type()
)
muxPCRPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxPCRPID.setStatus("current")


class _MuxPCRInterval_Type(Integer32):
    """Custom type muxPCRInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MuxPCRInterval_Type.__name__ = "Integer32"
_MuxPCRInterval_Object = MibTableColumn
muxPCRInterval = _MuxPCRInterval_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 11),
    _MuxPCRInterval_Type()
)
muxPCRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxPCRInterval.setStatus("current")


class _MuxCAType_Type(Integer32):
    """Custom type muxCAType based on Integer32"""
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
        *(("off", 0),
          ("rAS1", 1),
          ("rAS2", 2),
          ("bISS-Mode-1", 3),
          ("bISS-E", 4),
          ("bISS-Mode-2", 5))
    )


_MuxCAType_Type.__name__ = "Integer32"
_MuxCAType_Object = MibTableColumn
muxCAType = _MuxCAType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 12),
    _MuxCAType_Type()
)
muxCAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxCAType.setStatus("current")


class _MuxScrambling_Type(Integer32):
    """Custom type muxScrambling based on Integer32"""
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
        *(("off", 0),
          ("on-variableKey", 1),
          ("on-fixedKey1", 2),
          ("on-fixedKey2", 3),
          ("on-fixedKey3", 4))
    )


_MuxScrambling_Type.__name__ = "Integer32"
_MuxScrambling_Object = MibTableColumn
muxScrambling = _MuxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 13),
    _MuxScrambling_Type()
)
muxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxScrambling.setStatus("current")


class _MuxScrambleCode_Type(Integer32):
    """Custom type muxScrambleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_MuxScrambleCode_Type.__name__ = "Integer32"
_MuxScrambleCode_Object = MibTableColumn
muxScrambleCode = _MuxScrambleCode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 14),
    _MuxScrambleCode_Type()
)
muxScrambleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxScrambleCode.setStatus("current")


class _MuxTAXIPort_Type(Integer32):
    """Custom type muxTAXIPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("portA", 0),
          ("portB", 1))
    )


_MuxTAXIPort_Type.__name__ = "Integer32"
_MuxTAXIPort_Object = MibTableColumn
muxTAXIPort = _MuxTAXIPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 15),
    _MuxTAXIPort_Type()
)
muxTAXIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxTAXIPort.setStatus("current")


class _MuxBISSSessionWord_Type(OctetString):
    """Custom type muxBISSSessionWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 7),
    )


_MuxBISSSessionWord_Type.__name__ = "OctetString"
_MuxBISSSessionWord_Object = MibTableColumn
muxBISSSessionWord = _MuxBISSSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 16),
    _MuxBISSSessionWord_Type()
)
muxBISSSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxBISSSessionWord.setStatus("current")


class _MuxBISS2KeyEscrow_Type(Integer32):
    """Custom type muxBISS2KeyEscrow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MuxBISS2KeyEscrow_Type.__name__ = "Integer32"
_MuxBISS2KeyEscrow_Object = MibTableColumn
muxBISS2KeyEscrow = _MuxBISS2KeyEscrow_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 17),
    _MuxBISS2KeyEscrow_Type()
)
muxBISS2KeyEscrow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxBISS2KeyEscrow.setStatus("current")


class _MuxBISSEncryptedSessionWord_Type(OctetString):
    """Custom type muxBISSEncryptedSessionWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_MuxBISSEncryptedSessionWord_Type.__name__ = "OctetString"
_MuxBISSEncryptedSessionWord_Object = MibTableColumn
muxBISSEncryptedSessionWord = _MuxBISSEncryptedSessionWord_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 18),
    _MuxBISSEncryptedSessionWord_Type()
)
muxBISSEncryptedSessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxBISSEncryptedSessionWord.setStatus("current")


class _MuxShortList_Type(OctetString):
    """Custom type muxShortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_MuxShortList_Type.__name__ = "OctetString"
_MuxShortList_Object = MibTableColumn
muxShortList = _MuxShortList_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 19),
    _MuxShortList_Type()
)
muxShortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxShortList.setStatus("current")


class _MuxPRBS_Type(Integer32):
    """Custom type muxPRBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MuxPRBS_Type.__name__ = "Integer32"
_MuxPRBS_Object = MibTableColumn
muxPRBS = _MuxPRBS_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 20),
    _MuxPRBS_Type()
)
muxPRBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxPRBS.setStatus("current")


class _MuxPRBSReset_Type(Integer32):
    """Custom type muxPRBSReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal-operation", 0),
          ("reset", 1))
    )


_MuxPRBSReset_Type.__name__ = "Integer32"
_MuxPRBSReset_Object = MibTableColumn
muxPRBSReset = _MuxPRBSReset_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 3, 1, 21),
    _MuxPRBSReset_Type()
)
muxPRBSReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxPRBSReset.setStatus("current")
_MuxStreamTable_Object = MibTable
muxStreamTable = _MuxStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    muxStreamTable.setStatus("current")
_MuxStreamEntry_Object = MibTableRow
muxStreamEntry = _MuxStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 4, 1)
)
muxStreamEntry.setIndexNames(
    (0, "NDS-DTH3-MUX", "muxCurrentNextStreamIndex"),
    (0, "NDS-DTH3-MUX", "muxStreamIndex"),
)
if mibBuilder.loadTexts:
    muxStreamEntry.setStatus("current")


class _MuxCurrentNextStreamIndex_Type(Integer32):
    """Custom type muxCurrentNextStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_MuxCurrentNextStreamIndex_Type.__name__ = "Integer32"
_MuxCurrentNextStreamIndex_Object = MibTableColumn
muxCurrentNextStreamIndex = _MuxCurrentNextStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 4, 1, 1),
    _MuxCurrentNextStreamIndex_Type()
)
muxCurrentNextStreamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxCurrentNextStreamIndex.setStatus("current")


class _MuxStreamIndex_Type(Integer32):
    """Custom type muxStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_MuxStreamIndex_Type.__name__ = "Integer32"
_MuxStreamIndex_Object = MibTableColumn
muxStreamIndex = _MuxStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 4, 1, 2),
    _MuxStreamIndex_Type()
)
muxStreamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxStreamIndex.setStatus("current")


class _MuxStreamType_Type(Integer32):
    """Custom type muxStreamType based on Integer32"""
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
        *(("none", 0),
          ("reserved", 1),
          ("pSIData", 2),
          ("video", 3),
          ("teletext", 4),
          ("audio", 5),
          ("asynchronousDataRS232", 6),
          ("synchronousDataRS422", 7))
    )


_MuxStreamType_Type.__name__ = "Integer32"
_MuxStreamType_Object = MibTableColumn
muxStreamType = _MuxStreamType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 4, 1, 3),
    _MuxStreamType_Type()
)
muxStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxStreamType.setStatus("current")


class _MuxStreamPID_Type(Integer32):
    """Custom type muxStreamPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_MuxStreamPID_Type.__name__ = "Integer32"
_MuxStreamPID_Object = MibTableColumn
muxStreamPID = _MuxStreamPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 4, 1, 4),
    _MuxStreamPID_Type()
)
muxStreamPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxStreamPID.setStatus("current")


class _MuxStreamPriority_Type(Integer32):
    """Custom type muxStreamPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MuxStreamPriority_Type.__name__ = "Integer32"
_MuxStreamPriority_Object = MibTableColumn
muxStreamPriority = _MuxStreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 4, 1, 5),
    _MuxStreamPriority_Type()
)
muxStreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxStreamPriority.setStatus("current")


class _MuxBitRate188_Type(Integer32):
    """Custom type muxBitRate188 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 110000000),
    )


_MuxBitRate188_Type.__name__ = "Integer32"
_MuxBitRate188_Object = MibScalar
muxBitRate188 = _MuxBitRate188_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 5),
    _MuxBitRate188_Type()
)
muxBitRate188.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxBitRate188.setStatus("current")


class _MuxUtilisedBitRate_Type(Integer32):
    """Custom type muxUtilisedBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_MuxUtilisedBitRate_Type.__name__ = "Integer32"
_MuxUtilisedBitRate_Object = MibScalar
muxUtilisedBitRate = _MuxUtilisedBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 6),
    _MuxUtilisedBitRate_Type()
)
muxUtilisedBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxUtilisedBitRate.setStatus("current")


class _MuxUtilisedBitRate188_Type(Integer32):
    """Custom type muxUtilisedBitRate188 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_MuxUtilisedBitRate188_Type.__name__ = "Integer32"
_MuxUtilisedBitRate188_Object = MibScalar
muxUtilisedBitRate188 = _MuxUtilisedBitRate188_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 7),
    _MuxUtilisedBitRate188_Type()
)
muxUtilisedBitRate188.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxUtilisedBitRate188.setStatus("current")


class _MuxBISSEInjectedID_Type(OctetString):
    """Custom type muxBISSEInjectedID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_MuxBISSEInjectedID_Type.__name__ = "OctetString"
_MuxBISSEInjectedID_Object = MibScalar
muxBISSEInjectedID = _MuxBISSEInjectedID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 8),
    _MuxBISSEInjectedID_Type()
)
muxBISSEInjectedID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxBISSEInjectedID.setStatus("current")


class _MuxHostBitrate188_Type(Integer32):
    """Custom type muxHostBitrate188 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MuxHostBitrate188_Type.__name__ = "Integer32"
_MuxHostBitrate188_Object = MibScalar
muxHostBitrate188 = _MuxHostBitrate188_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 2, 9),
    _MuxHostBitrate188_Type()
)
muxHostBitrate188.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxHostBitrate188.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-MUX",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "muxEnc": muxEnc,
       "muxVersion": muxVersion,
       "muxnextTimeDate": muxnextTimeDate,
       "muxTable": muxTable,
       "muxEntry": muxEntry,
       "muxCurrentNextIndex": muxCurrentNextIndex,
       "muxFormat": muxFormat,
       "muxOnAir": muxOnAir,
       "muxOpMode": muxOpMode,
       "muxBitRate": muxBitRate,
       "muxClock": muxClock,
       "muxAutoPriority": muxAutoPriority,
       "muxAutoPID": muxAutoPID,
       "muxPCRSource": muxPCRSource,
       "muxPCRPID": muxPCRPID,
       "muxPCRInterval": muxPCRInterval,
       "muxCAType": muxCAType,
       "muxScrambling": muxScrambling,
       "muxScrambleCode": muxScrambleCode,
       "muxTAXIPort": muxTAXIPort,
       "muxBISSSessionWord": muxBISSSessionWord,
       "muxBISS2KeyEscrow": muxBISS2KeyEscrow,
       "muxBISSEncryptedSessionWord": muxBISSEncryptedSessionWord,
       "muxShortList": muxShortList,
       "muxPRBS": muxPRBS,
       "muxPRBSReset": muxPRBSReset,
       "muxStreamTable": muxStreamTable,
       "muxStreamEntry": muxStreamEntry,
       "muxCurrentNextStreamIndex": muxCurrentNextStreamIndex,
       "muxStreamIndex": muxStreamIndex,
       "muxStreamType": muxStreamType,
       "muxStreamPID": muxStreamPID,
       "muxStreamPriority": muxStreamPriority,
       "muxBitRate188": muxBitRate188,
       "muxUtilisedBitRate": muxUtilisedBitRate,
       "muxUtilisedBitRate188": muxUtilisedBitRate188,
       "muxBISSEInjectedID": muxBISSEInjectedID,
       "muxHostBitrate188": muxHostBitrate188}
)
