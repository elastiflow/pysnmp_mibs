# SNMP MIB module (NDS-DTH3-AUDIOXLR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-AUDIOXLR.mib
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

_AudioXlr_ObjectIdentity = ObjectIdentity
audioXlr = _AudioXlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18)
)


class _AudioXlrHardwareRelease_Type(DisplayString):
    """Custom type audioXlrHardwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AudioXlrHardwareRelease_Type.__name__ = "DisplayString"
_AudioXlrHardwareRelease_Object = MibScalar
audioXlrHardwareRelease = _AudioXlrHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 1),
    _AudioXlrHardwareRelease_Type()
)
audioXlrHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioXlrHardwareRelease.setStatus("current")


class _AudioXlrFirmwareRelease_Type(DisplayString):
    """Custom type audioXlrFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AudioXlrFirmwareRelease_Type.__name__ = "DisplayString"
_AudioXlrFirmwareRelease_Object = MibScalar
audioXlrFirmwareRelease = _AudioXlrFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 2),
    _AudioXlrFirmwareRelease_Type()
)
audioXlrFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioXlrFirmwareRelease.setStatus("current")
_AudioXlrnextTimeDate_Type = DateAndTime
_AudioXlrnextTimeDate_Object = MibScalar
audioXlrnextTimeDate = _AudioXlrnextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 3),
    _AudioXlrnextTimeDate_Type()
)
audioXlrnextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioXlrnextTimeDate.setStatus("current")
_AudioXlrTable_Object = MibTable
audioXlrTable = _AudioXlrTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4)
)
if mibBuilder.loadTexts:
    audioXlrTable.setStatus("current")
_AudioXlrEntry_Object = MibTableRow
audioXlrEntry = _AudioXlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4, 1)
)
audioXlrEntry.setIndexNames(
    (0, "NDS-DTH3-AUDIOXLR", "audioXlrCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    audioXlrEntry.setStatus("current")


class _AudioXlrCurrentNextIndex_Type(Integer32):
    """Custom type audioXlrCurrentNextIndex based on Integer32"""
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


_AudioXlrCurrentNextIndex_Type.__name__ = "Integer32"
_AudioXlrCurrentNextIndex_Object = MibTableColumn
audioXlrCurrentNextIndex = _AudioXlrCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4, 1, 1),
    _AudioXlrCurrentNextIndex_Type()
)
audioXlrCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioXlrCurrentNextIndex.setStatus("current")


class _AudioXlrInputFormat_Type(Integer32):
    """Custom type audioXlrInputFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("digital", 0),
          ("analogue", 1))
    )


_AudioXlrInputFormat_Type.__name__ = "Integer32"
_AudioXlrInputFormat_Object = MibTableColumn
audioXlrInputFormat = _AudioXlrInputFormat_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4, 1, 2),
    _AudioXlrInputFormat_Type()
)
audioXlrInputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioXlrInputFormat.setStatus("current")


class _AudioXlrInputTermination_Type(Integer32):
    """Custom type audioXlrInputTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("term20kOhms", 0),
          ("term600Ohms", 1))
    )


_AudioXlrInputTermination_Type.__name__ = "Integer32"
_AudioXlrInputTermination_Object = MibTableColumn
audioXlrInputTermination = _AudioXlrInputTermination_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4, 1, 3),
    _AudioXlrInputTermination_Type()
)
audioXlrInputTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioXlrInputTermination.setStatus("current")


class _AudioXlrInputClipLevel_Type(Integer32):
    """Custom type audioXlrInputClipLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gain15dB", 0),
          ("gain18dB", 1))
    )


_AudioXlrInputClipLevel_Type.__name__ = "Integer32"
_AudioXlrInputClipLevel_Object = MibTableColumn
audioXlrInputClipLevel = _AudioXlrInputClipLevel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4, 1, 4),
    _AudioXlrInputClipLevel_Type()
)
audioXlrInputClipLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioXlrInputClipLevel.setStatus("current")


class _AudioXlrOutputSource_Type(Integer32):
    """Custom type audioXlrOutputSource based on Integer32"""
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
        *(("mute", 0),
          ("embedded-1", 1),
          ("embedded-2", 2),
          ("embedded-3", 3),
          ("embedded-4", 4),
          ("decoder-1", 5),
          ("decoder-2", 6),
          ("xlr-input", 7))
    )


_AudioXlrOutputSource_Type.__name__ = "Integer32"
_AudioXlrOutputSource_Object = MibTableColumn
audioXlrOutputSource = _AudioXlrOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4, 1, 5),
    _AudioXlrOutputSource_Type()
)
audioXlrOutputSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioXlrOutputSource.setStatus("current")


class _AudioXlrOutputFormat_Type(Integer32):
    """Custom type audioXlrOutputFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("digital", 0),
          ("analogue", 1))
    )


_AudioXlrOutputFormat_Type.__name__ = "Integer32"
_AudioXlrOutputFormat_Object = MibTableColumn
audioXlrOutputFormat = _AudioXlrOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4, 1, 6),
    _AudioXlrOutputFormat_Type()
)
audioXlrOutputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioXlrOutputFormat.setStatus("current")


class _AudioXlrOutputFSR_Type(Integer32):
    """Custom type audioXlrOutputFSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fsr15dB", 0),
          ("fsr18dB", 1))
    )


_AudioXlrOutputFSR_Type.__name__ = "Integer32"
_AudioXlrOutputFSR_Object = MibTableColumn
audioXlrOutputFSR = _AudioXlrOutputFSR_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 18, 4, 1, 7),
    _AudioXlrOutputFSR_Type()
)
audioXlrOutputFSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioXlrOutputFSR.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-AUDIOXLR",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "audioXlr": audioXlr,
       "audioXlrHardwareRelease": audioXlrHardwareRelease,
       "audioXlrFirmwareRelease": audioXlrFirmwareRelease,
       "audioXlrnextTimeDate": audioXlrnextTimeDate,
       "audioXlrTable": audioXlrTable,
       "audioXlrEntry": audioXlrEntry,
       "audioXlrCurrentNextIndex": audioXlrCurrentNextIndex,
       "audioXlrInputFormat": audioXlrInputFormat,
       "audioXlrInputTermination": audioXlrInputTermination,
       "audioXlrInputClipLevel": audioXlrInputClipLevel,
       "audioXlrOutputSource": audioXlrOutputSource,
       "audioXlrOutputFormat": audioXlrOutputFormat,
       "audioXlrOutputFSR": audioXlrOutputFSR}
)
