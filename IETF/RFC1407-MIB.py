# SNMP MIB module (RFC1407-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IETF/RFC1407-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:29:12 2025
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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

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

_Ds3_ObjectIdentity = ObjectIdentity
ds3 = _Ds3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 30)
)
_Dsx3ConfigTable_Object = MibTable
dsx3ConfigTable = _Dsx3ConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5)
)
if mibBuilder.loadTexts:
    dsx3ConfigTable.setStatus("mandatory")
_Dsx3ConfigEntry_Object = MibTableRow
dsx3ConfigEntry = _Dsx3ConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1)
)
dsx3ConfigEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3LineIndex"),
)
if mibBuilder.loadTexts:
    dsx3ConfigEntry.setStatus("mandatory")


class _Dsx3LineIndex_Type(Integer32):
    """Custom type dsx3LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3LineIndex_Type.__name__ = "Integer32"
_Dsx3LineIndex_Object = MibTableColumn
dsx3LineIndex = _Dsx3LineIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 1),
    _Dsx3LineIndex_Type()
)
dsx3LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LineIndex.setStatus("mandatory")


class _Dsx3IfIndex_Type(Integer32):
    """Custom type dsx3IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3IfIndex_Type.__name__ = "Integer32"
_Dsx3IfIndex_Object = MibTableColumn
dsx3IfIndex = _Dsx3IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 2),
    _Dsx3IfIndex_Type()
)
dsx3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IfIndex.setStatus("mandatory")


class _Dsx3TimeElapsed_Type(Integer32):
    """Custom type dsx3TimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_Dsx3TimeElapsed_Type.__name__ = "Integer32"
_Dsx3TimeElapsed_Object = MibTableColumn
dsx3TimeElapsed = _Dsx3TimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 3),
    _Dsx3TimeElapsed_Type()
)
dsx3TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TimeElapsed.setStatus("mandatory")


class _Dsx3ValidIntervals_Type(Integer32):
    """Custom type dsx3ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Dsx3ValidIntervals_Type.__name__ = "Integer32"
_Dsx3ValidIntervals_Object = MibTableColumn
dsx3ValidIntervals = _Dsx3ValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 4),
    _Dsx3ValidIntervals_Type()
)
dsx3ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3ValidIntervals.setStatus("mandatory")


class _Dsx3LineType_Type(Integer32):
    """Custom type dsx3LineType based on Integer32"""
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
        *(("dsx3other", 1),
          ("dsx3M23", 2),
          ("dsx3SYNTRAN", 3),
          ("dsx3CbitParity", 4),
          ("dsx3ClearChannel", 5),
          ("e3other", 6),
          ("e3Framed", 7),
          ("e3Plcp", 8))
    )


_Dsx3LineType_Type.__name__ = "Integer32"
_Dsx3LineType_Object = MibTableColumn
dsx3LineType = _Dsx3LineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 5),
    _Dsx3LineType_Type()
)
dsx3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineType.setStatus("mandatory")


class _Dsx3LineCoding_Type(Integer32):
    """Custom type dsx3LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsx3Other", 1),
          ("dsx3B3ZS", 2),
          ("e3HDB3", 3))
    )


_Dsx3LineCoding_Type.__name__ = "Integer32"
_Dsx3LineCoding_Object = MibTableColumn
dsx3LineCoding = _Dsx3LineCoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 6),
    _Dsx3LineCoding_Type()
)
dsx3LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineCoding.setStatus("mandatory")


class _Dsx3SendCode_Type(Integer32):
    """Custom type dsx3SendCode based on Integer32"""
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
        *(("dsx3SendNoCode", 1),
          ("dsx3SendLineCode", 2),
          ("dsx3SendPayloadCode", 3),
          ("dsx3SendResetCode", 4),
          ("dsx3SendDS1LoopCode", 5),
          ("dsx3SendTestPattern", 6))
    )


_Dsx3SendCode_Type.__name__ = "Integer32"
_Dsx3SendCode_Object = MibTableColumn
dsx3SendCode = _Dsx3SendCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 7),
    _Dsx3SendCode_Type()
)
dsx3SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3SendCode.setStatus("mandatory")


class _Dsx3CircuitIdentifier_Type(DisplayString):
    """Custom type dsx3CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dsx3CircuitIdentifier_Type.__name__ = "DisplayString"
_Dsx3CircuitIdentifier_Object = MibTableColumn
dsx3CircuitIdentifier = _Dsx3CircuitIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 8),
    _Dsx3CircuitIdentifier_Type()
)
dsx3CircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3CircuitIdentifier.setStatus("mandatory")


class _Dsx3LoopbackConfig_Type(Integer32):
    """Custom type dsx3LoopbackConfig based on Integer32"""
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
        *(("dsx3NoLoop", 1),
          ("dsx3PayloadLoop", 2),
          ("dsx3LineLoop", 3),
          ("dsx3OtherLoop", 4))
    )


_Dsx3LoopbackConfig_Type.__name__ = "Integer32"
_Dsx3LoopbackConfig_Object = MibTableColumn
dsx3LoopbackConfig = _Dsx3LoopbackConfig_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 9),
    _Dsx3LoopbackConfig_Type()
)
dsx3LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LoopbackConfig.setStatus("mandatory")


class _Dsx3LineStatus_Type(Integer32):
    """Custom type dsx3LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_Dsx3LineStatus_Type.__name__ = "Integer32"
_Dsx3LineStatus_Object = MibTableColumn
dsx3LineStatus = _Dsx3LineStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 10),
    _Dsx3LineStatus_Type()
)
dsx3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LineStatus.setStatus("mandatory")


class _Dsx3TransmitClockSource_Type(Integer32):
    """Custom type dsx3TransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3))
    )


_Dsx3TransmitClockSource_Type.__name__ = "Integer32"
_Dsx3TransmitClockSource_Object = MibTableColumn
dsx3TransmitClockSource = _Dsx3TransmitClockSource_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 11),
    _Dsx3TransmitClockSource_Type()
)
dsx3TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3TransmitClockSource.setStatus("mandatory")
_Dsx3CurrentTable_Object = MibTable
dsx3CurrentTable = _Dsx3CurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6)
)
if mibBuilder.loadTexts:
    dsx3CurrentTable.setStatus("mandatory")
_Dsx3CurrentEntry_Object = MibTableRow
dsx3CurrentEntry = _Dsx3CurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1)
)
dsx3CurrentEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3CurrentIndex"),
)
if mibBuilder.loadTexts:
    dsx3CurrentEntry.setStatus("mandatory")


class _Dsx3CurrentIndex_Type(Integer32):
    """Custom type dsx3CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3CurrentIndex_Type.__name__ = "Integer32"
_Dsx3CurrentIndex_Object = MibTableColumn
dsx3CurrentIndex = _Dsx3CurrentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 1),
    _Dsx3CurrentIndex_Type()
)
dsx3CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentIndex.setStatus("mandatory")
_Dsx3CurrentPESs_Type = Gauge32
_Dsx3CurrentPESs_Object = MibTableColumn
dsx3CurrentPESs = _Dsx3CurrentPESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 2),
    _Dsx3CurrentPESs_Type()
)
dsx3CurrentPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentPESs.setStatus("mandatory")
_Dsx3CurrentPSESs_Type = Gauge32
_Dsx3CurrentPSESs_Object = MibTableColumn
dsx3CurrentPSESs = _Dsx3CurrentPSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 3),
    _Dsx3CurrentPSESs_Type()
)
dsx3CurrentPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentPSESs.setStatus("mandatory")
_Dsx3CurrentSEFSs_Type = Gauge32
_Dsx3CurrentSEFSs_Object = MibTableColumn
dsx3CurrentSEFSs = _Dsx3CurrentSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 4),
    _Dsx3CurrentSEFSs_Type()
)
dsx3CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentSEFSs.setStatus("mandatory")
_Dsx3CurrentUASs_Type = Gauge32
_Dsx3CurrentUASs_Object = MibTableColumn
dsx3CurrentUASs = _Dsx3CurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 5),
    _Dsx3CurrentUASs_Type()
)
dsx3CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentUASs.setStatus("mandatory")
_Dsx3CurrentLCVs_Type = Gauge32
_Dsx3CurrentLCVs_Object = MibTableColumn
dsx3CurrentLCVs = _Dsx3CurrentLCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 6),
    _Dsx3CurrentLCVs_Type()
)
dsx3CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentLCVs.setStatus("mandatory")
_Dsx3CurrentPCVs_Type = Gauge32
_Dsx3CurrentPCVs_Object = MibTableColumn
dsx3CurrentPCVs = _Dsx3CurrentPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 7),
    _Dsx3CurrentPCVs_Type()
)
dsx3CurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentPCVs.setStatus("mandatory")
_Dsx3CurrentLESs_Type = Gauge32
_Dsx3CurrentLESs_Object = MibTableColumn
dsx3CurrentLESs = _Dsx3CurrentLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 8),
    _Dsx3CurrentLESs_Type()
)
dsx3CurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentLESs.setStatus("mandatory")
_Dsx3CurrentCCVs_Type = Gauge32
_Dsx3CurrentCCVs_Object = MibTableColumn
dsx3CurrentCCVs = _Dsx3CurrentCCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 9),
    _Dsx3CurrentCCVs_Type()
)
dsx3CurrentCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentCCVs.setStatus("mandatory")
_Dsx3CurrentCESs_Type = Gauge32
_Dsx3CurrentCESs_Object = MibTableColumn
dsx3CurrentCESs = _Dsx3CurrentCESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 10),
    _Dsx3CurrentCESs_Type()
)
dsx3CurrentCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentCESs.setStatus("mandatory")
_Dsx3CurrentCSESs_Type = Gauge32
_Dsx3CurrentCSESs_Object = MibTableColumn
dsx3CurrentCSESs = _Dsx3CurrentCSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 11),
    _Dsx3CurrentCSESs_Type()
)
dsx3CurrentCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CurrentCSESs.setStatus("mandatory")
_Dsx3IntervalTable_Object = MibTable
dsx3IntervalTable = _Dsx3IntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7)
)
if mibBuilder.loadTexts:
    dsx3IntervalTable.setStatus("mandatory")
_Dsx3IntervalEntry_Object = MibTableRow
dsx3IntervalEntry = _Dsx3IntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1)
)
dsx3IntervalEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3IntervalIndex"),
    (0, "RFC1407-MIB", "dsx3IntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx3IntervalEntry.setStatus("mandatory")


class _Dsx3IntervalIndex_Type(Integer32):
    """Custom type dsx3IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3IntervalIndex_Type.__name__ = "Integer32"
_Dsx3IntervalIndex_Object = MibTableColumn
dsx3IntervalIndex = _Dsx3IntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 1),
    _Dsx3IntervalIndex_Type()
)
dsx3IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalIndex.setStatus("mandatory")


class _Dsx3IntervalNumber_Type(Integer32):
    """Custom type dsx3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Dsx3IntervalNumber_Type.__name__ = "Integer32"
_Dsx3IntervalNumber_Object = MibTableColumn
dsx3IntervalNumber = _Dsx3IntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 2),
    _Dsx3IntervalNumber_Type()
)
dsx3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalNumber.setStatus("mandatory")
_Dsx3IntervalPESs_Type = Gauge32
_Dsx3IntervalPESs_Object = MibTableColumn
dsx3IntervalPESs = _Dsx3IntervalPESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 3),
    _Dsx3IntervalPESs_Type()
)
dsx3IntervalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalPESs.setStatus("mandatory")
_Dsx3IntervalPSESs_Type = Gauge32
_Dsx3IntervalPSESs_Object = MibTableColumn
dsx3IntervalPSESs = _Dsx3IntervalPSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 4),
    _Dsx3IntervalPSESs_Type()
)
dsx3IntervalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalPSESs.setStatus("mandatory")
_Dsx3IntervalSEFSs_Type = Gauge32
_Dsx3IntervalSEFSs_Object = MibTableColumn
dsx3IntervalSEFSs = _Dsx3IntervalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 5),
    _Dsx3IntervalSEFSs_Type()
)
dsx3IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalSEFSs.setStatus("mandatory")
_Dsx3IntervalUASs_Type = Gauge32
_Dsx3IntervalUASs_Object = MibTableColumn
dsx3IntervalUASs = _Dsx3IntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 6),
    _Dsx3IntervalUASs_Type()
)
dsx3IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalUASs.setStatus("mandatory")
_Dsx3IntervalLCVs_Type = Gauge32
_Dsx3IntervalLCVs_Object = MibTableColumn
dsx3IntervalLCVs = _Dsx3IntervalLCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 7),
    _Dsx3IntervalLCVs_Type()
)
dsx3IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalLCVs.setStatus("mandatory")
_Dsx3IntervalPCVs_Type = Gauge32
_Dsx3IntervalPCVs_Object = MibTableColumn
dsx3IntervalPCVs = _Dsx3IntervalPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 8),
    _Dsx3IntervalPCVs_Type()
)
dsx3IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalPCVs.setStatus("mandatory")
_Dsx3IntervalLESs_Type = Gauge32
_Dsx3IntervalLESs_Object = MibTableColumn
dsx3IntervalLESs = _Dsx3IntervalLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 9),
    _Dsx3IntervalLESs_Type()
)
dsx3IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalLESs.setStatus("mandatory")
_Dsx3IntervalCCVs_Type = Gauge32
_Dsx3IntervalCCVs_Object = MibTableColumn
dsx3IntervalCCVs = _Dsx3IntervalCCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 10),
    _Dsx3IntervalCCVs_Type()
)
dsx3IntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalCCVs.setStatus("mandatory")
_Dsx3IntervalCESs_Type = Gauge32
_Dsx3IntervalCESs_Object = MibTableColumn
dsx3IntervalCESs = _Dsx3IntervalCESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 11),
    _Dsx3IntervalCESs_Type()
)
dsx3IntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalCESs.setStatus("mandatory")
_Dsx3IntervalCSESs_Type = Gauge32
_Dsx3IntervalCSESs_Object = MibTableColumn
dsx3IntervalCSESs = _Dsx3IntervalCSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 12),
    _Dsx3IntervalCSESs_Type()
)
dsx3IntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3IntervalCSESs.setStatus("mandatory")
_Dsx3TotalTable_Object = MibTable
dsx3TotalTable = _Dsx3TotalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8)
)
if mibBuilder.loadTexts:
    dsx3TotalTable.setStatus("mandatory")
_Dsx3TotalEntry_Object = MibTableRow
dsx3TotalEntry = _Dsx3TotalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1)
)
dsx3TotalEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3TotalIndex"),
)
if mibBuilder.loadTexts:
    dsx3TotalEntry.setStatus("mandatory")


class _Dsx3TotalIndex_Type(Integer32):
    """Custom type dsx3TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3TotalIndex_Type.__name__ = "Integer32"
_Dsx3TotalIndex_Object = MibTableColumn
dsx3TotalIndex = _Dsx3TotalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 1),
    _Dsx3TotalIndex_Type()
)
dsx3TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalIndex.setStatus("mandatory")
_Dsx3TotalPESs_Type = Gauge32
_Dsx3TotalPESs_Object = MibTableColumn
dsx3TotalPESs = _Dsx3TotalPESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 2),
    _Dsx3TotalPESs_Type()
)
dsx3TotalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalPESs.setStatus("mandatory")
_Dsx3TotalPSESs_Type = Gauge32
_Dsx3TotalPSESs_Object = MibTableColumn
dsx3TotalPSESs = _Dsx3TotalPSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 3),
    _Dsx3TotalPSESs_Type()
)
dsx3TotalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalPSESs.setStatus("mandatory")
_Dsx3TotalSEFSs_Type = Gauge32
_Dsx3TotalSEFSs_Object = MibTableColumn
dsx3TotalSEFSs = _Dsx3TotalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 4),
    _Dsx3TotalSEFSs_Type()
)
dsx3TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalSEFSs.setStatus("mandatory")
_Dsx3TotalUASs_Type = Gauge32
_Dsx3TotalUASs_Object = MibTableColumn
dsx3TotalUASs = _Dsx3TotalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 5),
    _Dsx3TotalUASs_Type()
)
dsx3TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalUASs.setStatus("mandatory")
_Dsx3TotalLCVs_Type = Gauge32
_Dsx3TotalLCVs_Object = MibTableColumn
dsx3TotalLCVs = _Dsx3TotalLCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 6),
    _Dsx3TotalLCVs_Type()
)
dsx3TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalLCVs.setStatus("mandatory")
_Dsx3TotalPCVs_Type = Gauge32
_Dsx3TotalPCVs_Object = MibTableColumn
dsx3TotalPCVs = _Dsx3TotalPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 7),
    _Dsx3TotalPCVs_Type()
)
dsx3TotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalPCVs.setStatus("mandatory")
_Dsx3TotalLESs_Type = Gauge32
_Dsx3TotalLESs_Object = MibTableColumn
dsx3TotalLESs = _Dsx3TotalLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 8),
    _Dsx3TotalLESs_Type()
)
dsx3TotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalLESs.setStatus("mandatory")
_Dsx3TotalCCVs_Type = Gauge32
_Dsx3TotalCCVs_Object = MibTableColumn
dsx3TotalCCVs = _Dsx3TotalCCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 9),
    _Dsx3TotalCCVs_Type()
)
dsx3TotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalCCVs.setStatus("mandatory")
_Dsx3TotalCESs_Type = Gauge32
_Dsx3TotalCESs_Object = MibTableColumn
dsx3TotalCESs = _Dsx3TotalCESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 10),
    _Dsx3TotalCESs_Type()
)
dsx3TotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalCESs.setStatus("mandatory")
_Dsx3TotalCSESs_Type = Gauge32
_Dsx3TotalCSESs_Object = MibTableColumn
dsx3TotalCSESs = _Dsx3TotalCSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 11),
    _Dsx3TotalCSESs_Type()
)
dsx3TotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TotalCSESs.setStatus("mandatory")
_Dsx3FarEndConfigTable_Object = MibTable
dsx3FarEndConfigTable = _Dsx3FarEndConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 9)
)
if mibBuilder.loadTexts:
    dsx3FarEndConfigTable.setStatus("mandatory")
_Dsx3FarEndConfigEntry_Object = MibTableRow
dsx3FarEndConfigEntry = _Dsx3FarEndConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 9, 1)
)
dsx3FarEndConfigEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3FarEndLineIndex"),
)
if mibBuilder.loadTexts:
    dsx3FarEndConfigEntry.setStatus("mandatory")


class _Dsx3FarEndLineIndex_Type(Integer32):
    """Custom type dsx3FarEndLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3FarEndLineIndex_Type.__name__ = "Integer32"
_Dsx3FarEndLineIndex_Object = MibTableColumn
dsx3FarEndLineIndex = _Dsx3FarEndLineIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 1),
    _Dsx3FarEndLineIndex_Type()
)
dsx3FarEndLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndLineIndex.setStatus("mandatory")


class _Dsx3FarEndEquipCode_Type(DisplayString):
    """Custom type dsx3FarEndEquipCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Dsx3FarEndEquipCode_Type.__name__ = "DisplayString"
_Dsx3FarEndEquipCode_Object = MibTableColumn
dsx3FarEndEquipCode = _Dsx3FarEndEquipCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 2),
    _Dsx3FarEndEquipCode_Type()
)
dsx3FarEndEquipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FarEndEquipCode.setStatus("mandatory")


class _Dsx3FarEndLocationIDCode_Type(DisplayString):
    """Custom type dsx3FarEndLocationIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Dsx3FarEndLocationIDCode_Type.__name__ = "DisplayString"
_Dsx3FarEndLocationIDCode_Object = MibTableColumn
dsx3FarEndLocationIDCode = _Dsx3FarEndLocationIDCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 3),
    _Dsx3FarEndLocationIDCode_Type()
)
dsx3FarEndLocationIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FarEndLocationIDCode.setStatus("mandatory")


class _Dsx3FarEndFrameIDCode_Type(DisplayString):
    """Custom type dsx3FarEndFrameIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Dsx3FarEndFrameIDCode_Type.__name__ = "DisplayString"
_Dsx3FarEndFrameIDCode_Object = MibTableColumn
dsx3FarEndFrameIDCode = _Dsx3FarEndFrameIDCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 4),
    _Dsx3FarEndFrameIDCode_Type()
)
dsx3FarEndFrameIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FarEndFrameIDCode.setStatus("mandatory")


class _Dsx3FarEndUnitCode_Type(DisplayString):
    """Custom type dsx3FarEndUnitCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Dsx3FarEndUnitCode_Type.__name__ = "DisplayString"
_Dsx3FarEndUnitCode_Object = MibTableColumn
dsx3FarEndUnitCode = _Dsx3FarEndUnitCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 5),
    _Dsx3FarEndUnitCode_Type()
)
dsx3FarEndUnitCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FarEndUnitCode.setStatus("mandatory")


class _Dsx3FarEndFacilityIDCode_Type(DisplayString):
    """Custom type dsx3FarEndFacilityIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_Dsx3FarEndFacilityIDCode_Type.__name__ = "DisplayString"
_Dsx3FarEndFacilityIDCode_Object = MibTableColumn
dsx3FarEndFacilityIDCode = _Dsx3FarEndFacilityIDCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 6),
    _Dsx3FarEndFacilityIDCode_Type()
)
dsx3FarEndFacilityIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FarEndFacilityIDCode.setStatus("mandatory")
_Dsx3FarEndCurrentTable_Object = MibTable
dsx3FarEndCurrentTable = _Dsx3FarEndCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10)
)
if mibBuilder.loadTexts:
    dsx3FarEndCurrentTable.setStatus("mandatory")
_Dsx3FarEndCurrentEntry_Object = MibTableRow
dsx3FarEndCurrentEntry = _Dsx3FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10, 1)
)
dsx3FarEndCurrentEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3FarEndCurrentIndex"),
)
if mibBuilder.loadTexts:
    dsx3FarEndCurrentEntry.setStatus("mandatory")


class _Dsx3FarEndCurrentIndex_Type(Integer32):
    """Custom type dsx3FarEndCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3FarEndCurrentIndex_Type.__name__ = "Integer32"
_Dsx3FarEndCurrentIndex_Object = MibTableColumn
dsx3FarEndCurrentIndex = _Dsx3FarEndCurrentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 1),
    _Dsx3FarEndCurrentIndex_Type()
)
dsx3FarEndCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndCurrentIndex.setStatus("mandatory")


class _Dsx3FarEndTimeElapsed_Type(Integer32):
    """Custom type dsx3FarEndTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_Dsx3FarEndTimeElapsed_Type.__name__ = "Integer32"
_Dsx3FarEndTimeElapsed_Object = MibTableColumn
dsx3FarEndTimeElapsed = _Dsx3FarEndTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 2),
    _Dsx3FarEndTimeElapsed_Type()
)
dsx3FarEndTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndTimeElapsed.setStatus("mandatory")


class _Dsx3FarEndValidIntervals_Type(Integer32):
    """Custom type dsx3FarEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Dsx3FarEndValidIntervals_Type.__name__ = "Integer32"
_Dsx3FarEndValidIntervals_Object = MibTableColumn
dsx3FarEndValidIntervals = _Dsx3FarEndValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 3),
    _Dsx3FarEndValidIntervals_Type()
)
dsx3FarEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndValidIntervals.setStatus("mandatory")
_Dsx3FarEndCurrentCESs_Type = Gauge32
_Dsx3FarEndCurrentCESs_Object = MibTableColumn
dsx3FarEndCurrentCESs = _Dsx3FarEndCurrentCESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 4),
    _Dsx3FarEndCurrentCESs_Type()
)
dsx3FarEndCurrentCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndCurrentCESs.setStatus("mandatory")
_Dsx3FarEndCurrentCSESs_Type = Gauge32
_Dsx3FarEndCurrentCSESs_Object = MibTableColumn
dsx3FarEndCurrentCSESs = _Dsx3FarEndCurrentCSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 5),
    _Dsx3FarEndCurrentCSESs_Type()
)
dsx3FarEndCurrentCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndCurrentCSESs.setStatus("mandatory")
_Dsx3FarEndCurrentCCVs_Type = Gauge32
_Dsx3FarEndCurrentCCVs_Object = MibTableColumn
dsx3FarEndCurrentCCVs = _Dsx3FarEndCurrentCCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 6),
    _Dsx3FarEndCurrentCCVs_Type()
)
dsx3FarEndCurrentCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndCurrentCCVs.setStatus("mandatory")
_Dsx3FarEndCurrentUASs_Type = Gauge32
_Dsx3FarEndCurrentUASs_Object = MibTableColumn
dsx3FarEndCurrentUASs = _Dsx3FarEndCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 7),
    _Dsx3FarEndCurrentUASs_Type()
)
dsx3FarEndCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndCurrentUASs.setStatus("mandatory")
_Dsx3FarEndIntervalTable_Object = MibTable
dsx3FarEndIntervalTable = _Dsx3FarEndIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 11)
)
if mibBuilder.loadTexts:
    dsx3FarEndIntervalTable.setStatus("mandatory")
_Dsx3FarEndIntervalEntry_Object = MibTableRow
dsx3FarEndIntervalEntry = _Dsx3FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 11, 1)
)
dsx3FarEndIntervalEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3FarEndIntervalIndex"),
    (0, "RFC1407-MIB", "dsx3FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx3FarEndIntervalEntry.setStatus("mandatory")


class _Dsx3FarEndIntervalIndex_Type(Integer32):
    """Custom type dsx3FarEndIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3FarEndIntervalIndex_Type.__name__ = "Integer32"
_Dsx3FarEndIntervalIndex_Object = MibTableColumn
dsx3FarEndIntervalIndex = _Dsx3FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 1),
    _Dsx3FarEndIntervalIndex_Type()
)
dsx3FarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndIntervalIndex.setStatus("mandatory")


class _Dsx3FarEndIntervalNumber_Type(Integer32):
    """Custom type dsx3FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Dsx3FarEndIntervalNumber_Type.__name__ = "Integer32"
_Dsx3FarEndIntervalNumber_Object = MibTableColumn
dsx3FarEndIntervalNumber = _Dsx3FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 2),
    _Dsx3FarEndIntervalNumber_Type()
)
dsx3FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndIntervalNumber.setStatus("mandatory")
_Dsx3FarEndIntervalCESs_Type = Gauge32
_Dsx3FarEndIntervalCESs_Object = MibTableColumn
dsx3FarEndIntervalCESs = _Dsx3FarEndIntervalCESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 3),
    _Dsx3FarEndIntervalCESs_Type()
)
dsx3FarEndIntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndIntervalCESs.setStatus("mandatory")
_Dsx3FarEndIntervalCSESs_Type = Gauge32
_Dsx3FarEndIntervalCSESs_Object = MibTableColumn
dsx3FarEndIntervalCSESs = _Dsx3FarEndIntervalCSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 4),
    _Dsx3FarEndIntervalCSESs_Type()
)
dsx3FarEndIntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndIntervalCSESs.setStatus("mandatory")
_Dsx3FarEndIntervalCCVs_Type = Gauge32
_Dsx3FarEndIntervalCCVs_Object = MibTableColumn
dsx3FarEndIntervalCCVs = _Dsx3FarEndIntervalCCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 5),
    _Dsx3FarEndIntervalCCVs_Type()
)
dsx3FarEndIntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndIntervalCCVs.setStatus("mandatory")
_Dsx3FarEndIntervalUASs_Type = Gauge32
_Dsx3FarEndIntervalUASs_Object = MibTableColumn
dsx3FarEndIntervalUASs = _Dsx3FarEndIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 6),
    _Dsx3FarEndIntervalUASs_Type()
)
dsx3FarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndIntervalUASs.setStatus("mandatory")
_Dsx3FarEndTotalTable_Object = MibTable
dsx3FarEndTotalTable = _Dsx3FarEndTotalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 12)
)
if mibBuilder.loadTexts:
    dsx3FarEndTotalTable.setStatus("mandatory")
_Dsx3FarEndTotalEntry_Object = MibTableRow
dsx3FarEndTotalEntry = _Dsx3FarEndTotalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 12, 1)
)
dsx3FarEndTotalEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3FarEndTotalIndex"),
)
if mibBuilder.loadTexts:
    dsx3FarEndTotalEntry.setStatus("mandatory")


class _Dsx3FarEndTotalIndex_Type(Integer32):
    """Custom type dsx3FarEndTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx3FarEndTotalIndex_Type.__name__ = "Integer32"
_Dsx3FarEndTotalIndex_Object = MibTableColumn
dsx3FarEndTotalIndex = _Dsx3FarEndTotalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 1),
    _Dsx3FarEndTotalIndex_Type()
)
dsx3FarEndTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndTotalIndex.setStatus("mandatory")
_Dsx3FarEndTotalCESs_Type = Gauge32
_Dsx3FarEndTotalCESs_Object = MibTableColumn
dsx3FarEndTotalCESs = _Dsx3FarEndTotalCESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 2),
    _Dsx3FarEndTotalCESs_Type()
)
dsx3FarEndTotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndTotalCESs.setStatus("mandatory")
_Dsx3FarEndTotalCSESs_Type = Gauge32
_Dsx3FarEndTotalCSESs_Object = MibTableColumn
dsx3FarEndTotalCSESs = _Dsx3FarEndTotalCSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 3),
    _Dsx3FarEndTotalCSESs_Type()
)
dsx3FarEndTotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndTotalCSESs.setStatus("mandatory")
_Dsx3FarEndTotalCCVs_Type = Gauge32
_Dsx3FarEndTotalCCVs_Object = MibTableColumn
dsx3FarEndTotalCCVs = _Dsx3FarEndTotalCCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 4),
    _Dsx3FarEndTotalCCVs_Type()
)
dsx3FarEndTotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndTotalCCVs.setStatus("mandatory")
_Dsx3FarEndTotalUASs_Type = Gauge32
_Dsx3FarEndTotalUASs_Object = MibTableColumn
dsx3FarEndTotalUASs = _Dsx3FarEndTotalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 5),
    _Dsx3FarEndTotalUASs_Type()
)
dsx3FarEndTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndTotalUASs.setStatus("mandatory")
_Dsx3FracTable_Object = MibTable
dsx3FracTable = _Dsx3FracTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 13)
)
if mibBuilder.loadTexts:
    dsx3FracTable.setStatus("mandatory")
_Dsx3FracEntry_Object = MibTableRow
dsx3FracEntry = _Dsx3FracEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 13, 1)
)
dsx3FracEntry.setIndexNames(
    (0, "RFC1407-MIB", "dsx3FracIndex"),
    (0, "RFC1407-MIB", "dsx3FracNumber"),
)
if mibBuilder.loadTexts:
    dsx3FracEntry.setStatus("mandatory")


class _Dsx3FracIndex_Type(Integer32):
    """Custom type dsx3FracIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx3FracIndex_Type.__name__ = "Integer32"
_Dsx3FracIndex_Object = MibTableColumn
dsx3FracIndex = _Dsx3FracIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 1),
    _Dsx3FracIndex_Type()
)
dsx3FracIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FracIndex.setStatus("mandatory")


class _Dsx3FracNumber_Type(Integer32):
    """Custom type dsx3FracNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Dsx3FracNumber_Type.__name__ = "Integer32"
_Dsx3FracNumber_Object = MibTableColumn
dsx3FracNumber = _Dsx3FracNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 2),
    _Dsx3FracNumber_Type()
)
dsx3FracNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FracNumber.setStatus("mandatory")


class _Dsx3FracIfIndex_Type(Integer32):
    """Custom type dsx3FracIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx3FracIfIndex_Type.__name__ = "Integer32"
_Dsx3FracIfIndex_Object = MibTableColumn
dsx3FracIfIndex = _Dsx3FracIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 3),
    _Dsx3FracIfIndex_Type()
)
dsx3FracIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FracIfIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1407-MIB",
    **{"ds3": ds3,
       "dsx3ConfigTable": dsx3ConfigTable,
       "dsx3ConfigEntry": dsx3ConfigEntry,
       "dsx3LineIndex": dsx3LineIndex,
       "dsx3IfIndex": dsx3IfIndex,
       "dsx3TimeElapsed": dsx3TimeElapsed,
       "dsx3ValidIntervals": dsx3ValidIntervals,
       "dsx3LineType": dsx3LineType,
       "dsx3LineCoding": dsx3LineCoding,
       "dsx3SendCode": dsx3SendCode,
       "dsx3CircuitIdentifier": dsx3CircuitIdentifier,
       "dsx3LoopbackConfig": dsx3LoopbackConfig,
       "dsx3LineStatus": dsx3LineStatus,
       "dsx3TransmitClockSource": dsx3TransmitClockSource,
       "dsx3CurrentTable": dsx3CurrentTable,
       "dsx3CurrentEntry": dsx3CurrentEntry,
       "dsx3CurrentIndex": dsx3CurrentIndex,
       "dsx3CurrentPESs": dsx3CurrentPESs,
       "dsx3CurrentPSESs": dsx3CurrentPSESs,
       "dsx3CurrentSEFSs": dsx3CurrentSEFSs,
       "dsx3CurrentUASs": dsx3CurrentUASs,
       "dsx3CurrentLCVs": dsx3CurrentLCVs,
       "dsx3CurrentPCVs": dsx3CurrentPCVs,
       "dsx3CurrentLESs": dsx3CurrentLESs,
       "dsx3CurrentCCVs": dsx3CurrentCCVs,
       "dsx3CurrentCESs": dsx3CurrentCESs,
       "dsx3CurrentCSESs": dsx3CurrentCSESs,
       "dsx3IntervalTable": dsx3IntervalTable,
       "dsx3IntervalEntry": dsx3IntervalEntry,
       "dsx3IntervalIndex": dsx3IntervalIndex,
       "dsx3IntervalNumber": dsx3IntervalNumber,
       "dsx3IntervalPESs": dsx3IntervalPESs,
       "dsx3IntervalPSESs": dsx3IntervalPSESs,
       "dsx3IntervalSEFSs": dsx3IntervalSEFSs,
       "dsx3IntervalUASs": dsx3IntervalUASs,
       "dsx3IntervalLCVs": dsx3IntervalLCVs,
       "dsx3IntervalPCVs": dsx3IntervalPCVs,
       "dsx3IntervalLESs": dsx3IntervalLESs,
       "dsx3IntervalCCVs": dsx3IntervalCCVs,
       "dsx3IntervalCESs": dsx3IntervalCESs,
       "dsx3IntervalCSESs": dsx3IntervalCSESs,
       "dsx3TotalTable": dsx3TotalTable,
       "dsx3TotalEntry": dsx3TotalEntry,
       "dsx3TotalIndex": dsx3TotalIndex,
       "dsx3TotalPESs": dsx3TotalPESs,
       "dsx3TotalPSESs": dsx3TotalPSESs,
       "dsx3TotalSEFSs": dsx3TotalSEFSs,
       "dsx3TotalUASs": dsx3TotalUASs,
       "dsx3TotalLCVs": dsx3TotalLCVs,
       "dsx3TotalPCVs": dsx3TotalPCVs,
       "dsx3TotalLESs": dsx3TotalLESs,
       "dsx3TotalCCVs": dsx3TotalCCVs,
       "dsx3TotalCESs": dsx3TotalCESs,
       "dsx3TotalCSESs": dsx3TotalCSESs,
       "dsx3FarEndConfigTable": dsx3FarEndConfigTable,
       "dsx3FarEndConfigEntry": dsx3FarEndConfigEntry,
       "dsx3FarEndLineIndex": dsx3FarEndLineIndex,
       "dsx3FarEndEquipCode": dsx3FarEndEquipCode,
       "dsx3FarEndLocationIDCode": dsx3FarEndLocationIDCode,
       "dsx3FarEndFrameIDCode": dsx3FarEndFrameIDCode,
       "dsx3FarEndUnitCode": dsx3FarEndUnitCode,
       "dsx3FarEndFacilityIDCode": dsx3FarEndFacilityIDCode,
       "dsx3FarEndCurrentTable": dsx3FarEndCurrentTable,
       "dsx3FarEndCurrentEntry": dsx3FarEndCurrentEntry,
       "dsx3FarEndCurrentIndex": dsx3FarEndCurrentIndex,
       "dsx3FarEndTimeElapsed": dsx3FarEndTimeElapsed,
       "dsx3FarEndValidIntervals": dsx3FarEndValidIntervals,
       "dsx3FarEndCurrentCESs": dsx3FarEndCurrentCESs,
       "dsx3FarEndCurrentCSESs": dsx3FarEndCurrentCSESs,
       "dsx3FarEndCurrentCCVs": dsx3FarEndCurrentCCVs,
       "dsx3FarEndCurrentUASs": dsx3FarEndCurrentUASs,
       "dsx3FarEndIntervalTable": dsx3FarEndIntervalTable,
       "dsx3FarEndIntervalEntry": dsx3FarEndIntervalEntry,
       "dsx3FarEndIntervalIndex": dsx3FarEndIntervalIndex,
       "dsx3FarEndIntervalNumber": dsx3FarEndIntervalNumber,
       "dsx3FarEndIntervalCESs": dsx3FarEndIntervalCESs,
       "dsx3FarEndIntervalCSESs": dsx3FarEndIntervalCSESs,
       "dsx3FarEndIntervalCCVs": dsx3FarEndIntervalCCVs,
       "dsx3FarEndIntervalUASs": dsx3FarEndIntervalUASs,
       "dsx3FarEndTotalTable": dsx3FarEndTotalTable,
       "dsx3FarEndTotalEntry": dsx3FarEndTotalEntry,
       "dsx3FarEndTotalIndex": dsx3FarEndTotalIndex,
       "dsx3FarEndTotalCESs": dsx3FarEndTotalCESs,
       "dsx3FarEndTotalCSESs": dsx3FarEndTotalCSESs,
       "dsx3FarEndTotalCCVs": dsx3FarEndTotalCCVs,
       "dsx3FarEndTotalUASs": dsx3FarEndTotalUASs,
       "dsx3FracTable": dsx3FracTable,
       "dsx3FracEntry": dsx3FracEntry,
       "dsx3FracIndex": dsx3FracIndex,
       "dsx3FracNumber": dsx3FracNumber,
       "dsx3FracIfIndex": dsx3FracIfIndex}
)
