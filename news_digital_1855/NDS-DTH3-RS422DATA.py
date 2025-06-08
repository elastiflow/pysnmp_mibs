# SNMP MIB module (NDS-DTH3-RS422DATA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-RS422DATA.mib
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
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

_Rs422Enc_ObjectIdentity = ObjectIdentity
rs422Enc = _Rs422Enc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11)
)


class _Rs422ModuleNumber_Type(Integer32):
    """Custom type rs422ModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Rs422ModuleNumber_Type.__name__ = "Integer32"
_Rs422ModuleNumber_Object = MibScalar
rs422ModuleNumber = _Rs422ModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 1),
    _Rs422ModuleNumber_Type()
)
rs422ModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs422ModuleNumber.setStatus("current")
_Rs422ModuleTable_Object = MibTable
rs422ModuleTable = _Rs422ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 2)
)
if mibBuilder.loadTexts:
    rs422ModuleTable.setStatus("current")
_Rs422ModuleEntry_Object = MibTableRow
rs422ModuleEntry = _Rs422ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 2, 1)
)
rs422ModuleEntry.setIndexNames(
    (0, "NDS-DTH3-RS422DATA", "rs422ModIndex"),
)
if mibBuilder.loadTexts:
    rs422ModuleEntry.setStatus("current")


class _Rs422ModIndex_Type(Integer32):
    """Custom type rs422ModIndex based on Integer32"""
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4),
          ("module5", 5),
          ("module6", 6),
          ("module7", 7))
    )


_Rs422ModIndex_Type.__name__ = "Integer32"
_Rs422ModIndex_Object = MibTableColumn
rs422ModIndex = _Rs422ModIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 2, 1, 1),
    _Rs422ModIndex_Type()
)
rs422ModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs422ModIndex.setStatus("current")


class _Rs422HardwareRelease_Type(OctetString):
    """Custom type rs422HardwareRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Rs422HardwareRelease_Type.__name__ = "OctetString"
_Rs422HardwareRelease_Object = MibTableColumn
rs422HardwareRelease = _Rs422HardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 2, 1, 2),
    _Rs422HardwareRelease_Type()
)
rs422HardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs422HardwareRelease.setStatus("current")


class _Rs422SoftwareRelease_Type(OctetString):
    """Custom type rs422SoftwareRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Rs422SoftwareRelease_Type.__name__ = "OctetString"
_Rs422SoftwareRelease_Object = MibTableColumn
rs422SoftwareRelease = _Rs422SoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 2, 1, 3),
    _Rs422SoftwareRelease_Type()
)
rs422SoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs422SoftwareRelease.setStatus("current")


class _Rs422FirmwareRelease_Type(OctetString):
    """Custom type rs422FirmwareRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Rs422FirmwareRelease_Type.__name__ = "OctetString"
_Rs422FirmwareRelease_Object = MibTableColumn
rs422FirmwareRelease = _Rs422FirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 2, 1, 4),
    _Rs422FirmwareRelease_Type()
)
rs422FirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs422FirmwareRelease.setStatus("current")
_Rs422nextTimeDate_Type = OctetString
_Rs422nextTimeDate_Object = MibTableColumn
rs422nextTimeDate = _Rs422nextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 2, 1, 5),
    _Rs422nextTimeDate_Type()
)
rs422nextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422nextTimeDate.setStatus("current")
_Rs422Table_Object = MibTable
rs422Table = _Rs422Table_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3)
)
if mibBuilder.loadTexts:
    rs422Table.setStatus("current")
_Rs422Entry_Object = MibTableRow
rs422Entry = _Rs422Entry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1)
)
rs422Entry.setIndexNames(
    (0, "NDS-DTH3-RS422DATA", "rs422CurrentNextIndex"),
    (0, "NDS-DTH3-RS422DATA", "rs422ModuleIndex"),
)
if mibBuilder.loadTexts:
    rs422Entry.setStatus("current")


class _Rs422CurrentNextIndex_Type(Integer32):
    """Custom type rs422CurrentNextIndex based on Integer32"""
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


_Rs422CurrentNextIndex_Type.__name__ = "Integer32"
_Rs422CurrentNextIndex_Object = MibTableColumn
rs422CurrentNextIndex = _Rs422CurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 1),
    _Rs422CurrentNextIndex_Type()
)
rs422CurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs422CurrentNextIndex.setStatus("current")


class _Rs422ModuleIndex_Type(Integer32):
    """Custom type rs422ModuleIndex based on Integer32"""
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4),
          ("module5", 5),
          ("module6", 6),
          ("module7", 7))
    )


_Rs422ModuleIndex_Type.__name__ = "Integer32"
_Rs422ModuleIndex_Object = MibTableColumn
rs422ModuleIndex = _Rs422ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 2),
    _Rs422ModuleIndex_Type()
)
rs422ModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs422ModuleIndex.setStatus("current")


class _Rs422Encode_Type(Integer32):
    """Custom type rs422Encode based on Integer32"""
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


_Rs422Encode_Type.__name__ = "Integer32"
_Rs422Encode_Object = MibTableColumn
rs422Encode = _Rs422Encode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 9),
    _Rs422Encode_Type()
)
rs422Encode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422Encode.setStatus("current")


class _Rs422BitRate_Type(Integer32):
    """Custom type rs422BitRate based on Integer32"""
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
              63)
        )
    )
    namedValues = NamedValues(
        *(("bitrate64kBits-s-1", 0),
          ("bitrate128kBits-s-1", 1),
          ("bitrate192kBits-s-1", 2),
          ("bitrate256kBits-s-1", 3),
          ("bitrate320kBits-s-1", 4),
          ("bitrate384kBits-s-1", 5),
          ("bitrate448kBits-s-1", 6),
          ("bitrate512kBits-s-1", 7),
          ("bitrate576kBits-s-1", 8),
          ("bitrate640kBits-s-1", 9),
          ("bitrate704kBits-s-1", 10),
          ("bitrate768kBits-s-1", 11),
          ("bitrate832kBits-s-1", 12),
          ("bitrate896kBits-s-1", 13),
          ("bitrate960kBits-s-1", 14),
          ("bitrate1024kBits-s-1", 15),
          ("bitrate1088kBits-s-1", 16),
          ("bitrate1152kBits-s-1", 17),
          ("bitrate1216kBits-s-1", 18),
          ("bitrate1280kBits-s-1", 19),
          ("bitrate1344kBits-s-1", 20),
          ("bitrate1408kBits-s-1", 21),
          ("bitrate1472kBits-s-1", 22),
          ("bitrate1536kBits-s-1", 23),
          ("bitrate1600kBits-s-1", 24),
          ("bitrate1664kBits-s-1", 25),
          ("bitrate1728kBits-s-1", 26),
          ("bitrate1792kBits-s-1", 27),
          ("bitrate1856kBits-s-1", 28),
          ("bitrate1920kBits-s-1", 29),
          ("bitrate1984kBits-s-1", 30),
          ("bitrate2048kBits-s-1", 31),
          ("bitrate56kBits-s-2", 32),
          ("bitrate112kBits-s-2", 33),
          ("bitrate168kBits-s-2", 34),
          ("bitrate224kBits-s-2", 35),
          ("bitrate280kBits-s-2", 36),
          ("bitrate336kBits-s-2", 37),
          ("bitrate392kBits-s-2", 38),
          ("bitrate448kBits-s-2", 39),
          ("bitrate504kBits-s-2", 40),
          ("bitrate560kBits-s-2", 41),
          ("bitrate616kBits-s-2", 42),
          ("bitrate672kBits-s-2", 43),
          ("bitrate728kBits-s-2", 44),
          ("bitrate784kBits-s-2", 45),
          ("bitrate840kBits-s-2", 46),
          ("bitrate896kBits-s-2", 47),
          ("bitrate952kBits-s-2", 48),
          ("bitrate1008kBits-s-2", 49),
          ("bitrate1064kBits-s-2", 50),
          ("bitrate1120kBits-s-2", 51),
          ("bitrate1176kBits-s-2", 52),
          ("bitrate1232kBits-s-2", 53),
          ("bitrate1288kBits-s-2", 54),
          ("bitrate1344kBits-s-2", 55),
          ("bitrate1400kBits-s-2", 56),
          ("bitrate1456kBits-s-2", 57),
          ("bitrate1512kBits-s-2", 58),
          ("bitrate1568kBits-s-2", 59),
          ("bitrate1624kBits-s-2", 60),
          ("bitrate1680kBits-s-2", 61),
          ("bitrate1736kBits-s-2", 62),
          ("bitrate1792kBits-s-2", 63))
    )


_Rs422BitRate_Type.__name__ = "Integer32"
_Rs422BitRate_Object = MibTableColumn
rs422BitRate = _Rs422BitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 10),
    _Rs422BitRate_Type()
)
rs422BitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422BitRate.setStatus("current")


class _Rs422TestPattern_Type(Integer32):
    """Custom type rs422TestPattern based on Integer32"""
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


_Rs422TestPattern_Type.__name__ = "Integer32"
_Rs422TestPattern_Object = MibTableColumn
rs422TestPattern = _Rs422TestPattern_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 11),
    _Rs422TestPattern_Type()
)
rs422TestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422TestPattern.setStatus("current")


class _Rs422DMode_Type(Integer32):
    """Custom type rs422DMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internally-formatted", 0),
          ("externally-formatted", 1))
    )


_Rs422DMode_Type.__name__ = "Integer32"
_Rs422DMode_Object = MibTableColumn
rs422DMode = _Rs422DMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 12),
    _Rs422DMode_Type()
)
rs422DMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422DMode.setStatus("current")


class _Rs422Delay_Type(Integer32):
    """Custom type rs422Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_Rs422Delay_Type.__name__ = "Integer32"
_Rs422Delay_Object = MibTableColumn
rs422Delay = _Rs422Delay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 13),
    _Rs422Delay_Type()
)
rs422Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422Delay.setStatus("current")


class _Rs422PID_Type(Integer32):
    """Custom type rs422PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_Rs422PID_Type.__name__ = "Integer32"
_Rs422PID_Object = MibTableColumn
rs422PID = _Rs422PID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 14),
    _Rs422PID_Type()
)
rs422PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422PID.setStatus("current")


class _Rs422ComponentTag_Type(Integer32):
    """Custom type rs422ComponentTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Rs422ComponentTag_Type.__name__ = "Integer32"
_Rs422ComponentTag_Object = MibTableColumn
rs422ComponentTag = _Rs422ComponentTag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 11, 3, 1, 15),
    _Rs422ComponentTag_Type()
)
rs422ComponentTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs422ComponentTag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-RS422DATA",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "rs422Enc": rs422Enc,
       "rs422ModuleNumber": rs422ModuleNumber,
       "rs422ModuleTable": rs422ModuleTable,
       "rs422ModuleEntry": rs422ModuleEntry,
       "rs422ModIndex": rs422ModIndex,
       "rs422HardwareRelease": rs422HardwareRelease,
       "rs422SoftwareRelease": rs422SoftwareRelease,
       "rs422FirmwareRelease": rs422FirmwareRelease,
       "rs422nextTimeDate": rs422nextTimeDate,
       "rs422Table": rs422Table,
       "rs422Entry": rs422Entry,
       "rs422CurrentNextIndex": rs422CurrentNextIndex,
       "rs422ModuleIndex": rs422ModuleIndex,
       "rs422Encode": rs422Encode,
       "rs422BitRate": rs422BitRate,
       "rs422TestPattern": rs422TestPattern,
       "rs422DMode": rs422DMode,
       "rs422Delay": rs422Delay,
       "rs422PID": rs422PID,
       "rs422ComponentTag": rs422ComponentTag}
)
