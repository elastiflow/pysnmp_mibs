# SNMP MIB module (RUIJIE-MPLSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MPLSOAM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ruijieMplsOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMplsOamPs_ObjectIdentity = ObjectIdentity
ruijieMplsOamPs = _RuijieMplsOamPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1)
)
_RuijieMplsOamObjects_ObjectIdentity = ObjectIdentity
ruijieMplsOamObjects = _RuijieMplsOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1)
)


class _RuijieMplsOamCapability_Type(Unsigned32):
    """Custom type ruijieMplsOamCapability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieMplsOamCapability_Type.__name__ = "Unsigned32"
_RuijieMplsOamCapability_Object = MibScalar
ruijieMplsOamCapability = _RuijieMplsOamCapability_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 1),
    _RuijieMplsOamCapability_Type()
)
ruijieMplsOamCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMplsOamCapability.setStatus("current")
_RuijieMplsOamIgrTable_Object = MibTable
ruijieMplsOamIgrTable = _RuijieMplsOamIgrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieMplsOamIgrTable.setStatus("current")
_RuijieMplsOamIgrEntry_Object = MibTableRow
ruijieMplsOamIgrEntry = _RuijieMplsOamIgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1)
)
ruijieMplsOamIgrEntry.setIndexNames(
    (0, "RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrIndex"),
)
if mibBuilder.loadTexts:
    ruijieMplsOamIgrEntry.setStatus("current")
_RuijieMplsOamIgrIndex_Type = Unsigned32
_RuijieMplsOamIgrIndex_Object = MibTableColumn
ruijieMplsOamIgrIndex = _RuijieMplsOamIgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 1),
    _RuijieMplsOamIgrIndex_Type()
)
ruijieMplsOamIgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrIndex.setStatus("current")
_RuijieMplsOamIgrLspName_Type = OctetString
_RuijieMplsOamIgrLspName_Object = MibTableColumn
ruijieMplsOamIgrLspName = _RuijieMplsOamIgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 2),
    _RuijieMplsOamIgrLspName_Type()
)
ruijieMplsOamIgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrLspName.setStatus("current")


class _RuijieMplsOamIgrLspId_Type(Integer32):
    """Custom type ruijieMplsOamIgrLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieMplsOamIgrLspId_Type.__name__ = "Integer32"
_RuijieMplsOamIgrLspId_Object = MibTableColumn
ruijieMplsOamIgrLspId = _RuijieMplsOamIgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 3),
    _RuijieMplsOamIgrLspId_Type()
)
ruijieMplsOamIgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrLspId.setStatus("current")


class _RuijieMplsOamIgrDetType_Type(Integer32):
    """Custom type ruijieMplsOamIgrDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cv", 1),
          ("ffd", 2))
    )


_RuijieMplsOamIgrDetType_Type.__name__ = "Integer32"
_RuijieMplsOamIgrDetType_Object = MibTableColumn
ruijieMplsOamIgrDetType = _RuijieMplsOamIgrDetType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 4),
    _RuijieMplsOamIgrDetType_Type()
)
ruijieMplsOamIgrDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrDetType.setStatus("current")


class _RuijieMplsOamIgrDetFreq_Type(Integer32):
    """Custom type ruijieMplsOamIgrDetFreq based on Integer32"""
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
        *(("cv1000ms", 0),
          ("ffd50ms2", 1),
          ("ffd100ms3", 2),
          ("ffd200ms4", 3),
          ("ffd500ms5", 4))
    )


_RuijieMplsOamIgrDetFreq_Type.__name__ = "Integer32"
_RuijieMplsOamIgrDetFreq_Object = MibTableColumn
ruijieMplsOamIgrDetFreq = _RuijieMplsOamIgrDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 5),
    _RuijieMplsOamIgrDetFreq_Type()
)
ruijieMplsOamIgrDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrDetFreq.setStatus("current")


class _RuijieMplsOamIgrRevType_Type(Integer32):
    """Custom type ruijieMplsOamIgrRevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("share", 2))
    )


_RuijieMplsOamIgrRevType_Type.__name__ = "Integer32"
_RuijieMplsOamIgrRevType_Object = MibTableColumn
ruijieMplsOamIgrRevType = _RuijieMplsOamIgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 6),
    _RuijieMplsOamIgrRevType_Type()
)
ruijieMplsOamIgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrRevType.setStatus("current")
_RuijieMplsOamIgrRevLspName_Type = OctetString
_RuijieMplsOamIgrRevLspName_Object = MibTableColumn
ruijieMplsOamIgrRevLspName = _RuijieMplsOamIgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 7),
    _RuijieMplsOamIgrRevLspName_Type()
)
ruijieMplsOamIgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrRevLspName.setStatus("current")


class _RuijieMplsOamIgrEnable_Type(Integer32):
    """Custom type ruijieMplsOamIgrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieMplsOamIgrEnable_Type.__name__ = "Integer32"
_RuijieMplsOamIgrEnable_Object = MibTableColumn
ruijieMplsOamIgrEnable = _RuijieMplsOamIgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 8),
    _RuijieMplsOamIgrEnable_Type()
)
ruijieMplsOamIgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrEnable.setStatus("current")


class _RuijieMplsOamIgrValid_Type(Integer32):
    """Custom type ruijieMplsOamIgrValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieMplsOamIgrValid_Type.__name__ = "Integer32"
_RuijieMplsOamIgrValid_Object = MibTableColumn
ruijieMplsOamIgrValid = _RuijieMplsOamIgrValid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 9),
    _RuijieMplsOamIgrValid_Type()
)
ruijieMplsOamIgrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrValid.setStatus("current")


class _RuijieMplsOamIgrAvaState_Type(Integer32):
    """Custom type ruijieMplsOamIgrAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieMplsOamIgrAvaState_Type.__name__ = "Integer32"
_RuijieMplsOamIgrAvaState_Object = MibTableColumn
ruijieMplsOamIgrAvaState = _RuijieMplsOamIgrAvaState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 10),
    _RuijieMplsOamIgrAvaState_Type()
)
ruijieMplsOamIgrAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrAvaState.setStatus("current")


class _RuijieMplsOamIgrDefectType_Type(Integer32):
    """Custom type ruijieMplsOamIgrDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieMplsOamIgrDefectType_Type.__name__ = "Integer32"
_RuijieMplsOamIgrDefectType_Object = MibTableColumn
ruijieMplsOamIgrDefectType = _RuijieMplsOamIgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 11),
    _RuijieMplsOamIgrDefectType_Type()
)
ruijieMplsOamIgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrDefectType.setStatus("current")
_RuijieMplsOamIgrRowStatus_Type = RowStatus
_RuijieMplsOamIgrRowStatus_Object = MibTableColumn
ruijieMplsOamIgrRowStatus = _RuijieMplsOamIgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 2, 1, 12),
    _RuijieMplsOamIgrRowStatus_Type()
)
ruijieMplsOamIgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamIgrRowStatus.setStatus("current")
_RuijieMplsOamEgrTable_Object = MibTable
ruijieMplsOamEgrTable = _RuijieMplsOamEgrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieMplsOamEgrTable.setStatus("current")
_RuijieMplsOamEgrEntry_Object = MibTableRow
ruijieMplsOamEgrEntry = _RuijieMplsOamEgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1)
)
ruijieMplsOamEgrEntry.setIndexNames(
    (0, "RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrIndex"),
)
if mibBuilder.loadTexts:
    ruijieMplsOamEgrEntry.setStatus("current")
_RuijieMplsOamEgrIndex_Type = Unsigned32
_RuijieMplsOamEgrIndex_Object = MibTableColumn
ruijieMplsOamEgrIndex = _RuijieMplsOamEgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 1),
    _RuijieMplsOamEgrIndex_Type()
)
ruijieMplsOamEgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrIndex.setStatus("current")
_RuijieMplsOamEgrLspName_Type = OctetString
_RuijieMplsOamEgrLspName_Object = MibTableColumn
ruijieMplsOamEgrLspName = _RuijieMplsOamEgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 2),
    _RuijieMplsOamEgrLspName_Type()
)
ruijieMplsOamEgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrLspName.setStatus("current")
_RuijieMplsOamEgrLsrId_Type = IpAddress
_RuijieMplsOamEgrLsrId_Object = MibTableColumn
ruijieMplsOamEgrLsrId = _RuijieMplsOamEgrLsrId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 3),
    _RuijieMplsOamEgrLsrId_Type()
)
ruijieMplsOamEgrLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrLsrId.setStatus("current")


class _RuijieMplsOamEgrLspId_Type(Integer32):
    """Custom type ruijieMplsOamEgrLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieMplsOamEgrLspId_Type.__name__ = "Integer32"
_RuijieMplsOamEgrLspId_Object = MibTableColumn
ruijieMplsOamEgrLspId = _RuijieMplsOamEgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 4),
    _RuijieMplsOamEgrLspId_Type()
)
ruijieMplsOamEgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrLspId.setStatus("current")


class _RuijieMplsOamEgrDetType_Type(Integer32):
    """Custom type ruijieMplsOamEgrDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptability", 0),
          ("cv", 1),
          ("ffd", 2))
    )


_RuijieMplsOamEgrDetType_Type.__name__ = "Integer32"
_RuijieMplsOamEgrDetType_Object = MibTableColumn
ruijieMplsOamEgrDetType = _RuijieMplsOamEgrDetType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 5),
    _RuijieMplsOamEgrDetType_Type()
)
ruijieMplsOamEgrDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrDetType.setStatus("current")


class _RuijieMplsOamEgrDetFreq_Type(Integer32):
    """Custom type ruijieMplsOamEgrDetFreq based on Integer32"""
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
        *(("cv1000ms", 0),
          ("ffd50ms2", 1),
          ("ffd100ms3", 2),
          ("ffd200ms4", 3),
          ("ffd500ms5", 4),
          ("invalid6", 5))
    )


_RuijieMplsOamEgrDetFreq_Type.__name__ = "Integer32"
_RuijieMplsOamEgrDetFreq_Object = MibTableColumn
ruijieMplsOamEgrDetFreq = _RuijieMplsOamEgrDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 6),
    _RuijieMplsOamEgrDetFreq_Type()
)
ruijieMplsOamEgrDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrDetFreq.setStatus("current")


class _RuijieMplsOamEgrRevType_Type(Integer32):
    """Custom type ruijieMplsOamEgrRevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("share", 1))
    )


_RuijieMplsOamEgrRevType_Type.__name__ = "Integer32"
_RuijieMplsOamEgrRevType_Object = MibTableColumn
ruijieMplsOamEgrRevType = _RuijieMplsOamEgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 7),
    _RuijieMplsOamEgrRevType_Type()
)
ruijieMplsOamEgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrRevType.setStatus("current")
_RuijieMplsOamEgrRevLspName_Type = OctetString
_RuijieMplsOamEgrRevLspName_Object = MibTableColumn
ruijieMplsOamEgrRevLspName = _RuijieMplsOamEgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 8),
    _RuijieMplsOamEgrRevLspName_Type()
)
ruijieMplsOamEgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrRevLspName.setStatus("current")


class _RuijieMplsOamEgrAutoEn_Type(Integer32):
    """Custom type ruijieMplsOamEgrAutoEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieMplsOamEgrAutoEn_Type.__name__ = "Integer32"
_RuijieMplsOamEgrAutoEn_Object = MibTableColumn
ruijieMplsOamEgrAutoEn = _RuijieMplsOamEgrAutoEn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 9),
    _RuijieMplsOamEgrAutoEn_Type()
)
ruijieMplsOamEgrAutoEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrAutoEn.setStatus("current")


class _RuijieMplsOamEgrAutoOvertime_Type(Integer32):
    """Custom type ruijieMplsOamEgrAutoOvertime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieMplsOamEgrAutoOvertime_Type.__name__ = "Integer32"
_RuijieMplsOamEgrAutoOvertime_Object = MibTableColumn
ruijieMplsOamEgrAutoOvertime = _RuijieMplsOamEgrAutoOvertime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 10),
    _RuijieMplsOamEgrAutoOvertime_Type()
)
ruijieMplsOamEgrAutoOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrAutoOvertime.setStatus("current")


class _RuijieMplsOamEgrBDIFreq_Type(Integer32):
    """Custom type ruijieMplsOamEgrBDIFreq based on Integer32"""
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
        *(("cv1000ms", 0),
          ("ffd50ms2", 1),
          ("ffd100ms3", 2),
          ("ffd200ms4", 3),
          ("ffd500ms5", 4))
    )


_RuijieMplsOamEgrBDIFreq_Type.__name__ = "Integer32"
_RuijieMplsOamEgrBDIFreq_Object = MibTableColumn
ruijieMplsOamEgrBDIFreq = _RuijieMplsOamEgrBDIFreq_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 11),
    _RuijieMplsOamEgrBDIFreq_Type()
)
ruijieMplsOamEgrBDIFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrBDIFreq.setStatus("current")


class _RuijieMplsOamEgrEnable_Type(Integer32):
    """Custom type ruijieMplsOamEgrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieMplsOamEgrEnable_Type.__name__ = "Integer32"
_RuijieMplsOamEgrEnable_Object = MibTableColumn
ruijieMplsOamEgrEnable = _RuijieMplsOamEgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 12),
    _RuijieMplsOamEgrEnable_Type()
)
ruijieMplsOamEgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrEnable.setStatus("current")


class _RuijieMplsOamEgrValid_Type(Integer32):
    """Custom type ruijieMplsOamEgrValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_RuijieMplsOamEgrValid_Type.__name__ = "Integer32"
_RuijieMplsOamEgrValid_Object = MibTableColumn
ruijieMplsOamEgrValid = _RuijieMplsOamEgrValid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 13),
    _RuijieMplsOamEgrValid_Type()
)
ruijieMplsOamEgrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrValid.setStatus("current")


class _RuijieMplsOamEgrAvaState_Type(Integer32):
    """Custom type ruijieMplsOamEgrAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieMplsOamEgrAvaState_Type.__name__ = "Integer32"
_RuijieMplsOamEgrAvaState_Object = MibTableColumn
ruijieMplsOamEgrAvaState = _RuijieMplsOamEgrAvaState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 14),
    _RuijieMplsOamEgrAvaState_Type()
)
ruijieMplsOamEgrAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrAvaState.setStatus("current")


class _RuijieMplsOamEgrDefectType_Type(Integer32):
    """Custom type ruijieMplsOamEgrDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieMplsOamEgrDefectType_Type.__name__ = "Integer32"
_RuijieMplsOamEgrDefectType_Object = MibTableColumn
ruijieMplsOamEgrDefectType = _RuijieMplsOamEgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 15),
    _RuijieMplsOamEgrDefectType_Type()
)
ruijieMplsOamEgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrDefectType.setStatus("current")
_RuijieMplsOamEgrRowStatus_Type = RowStatus
_RuijieMplsOamEgrRowStatus_Object = MibTableColumn
ruijieMplsOamEgrRowStatus = _RuijieMplsOamEgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 3, 1, 16),
    _RuijieMplsOamEgrRowStatus_Type()
)
ruijieMplsOamEgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMplsOamEgrRowStatus.setStatus("current")


class _RuijieMplsOamTrapOpen_Type(Unsigned32):
    """Custom type ruijieMplsOamTrapOpen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieMplsOamTrapOpen_Type.__name__ = "Unsigned32"
_RuijieMplsOamTrapOpen_Object = MibScalar
ruijieMplsOamTrapOpen = _RuijieMplsOamTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 1, 4),
    _RuijieMplsOamTrapOpen_Type()
)
ruijieMplsOamTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMplsOamTrapOpen.setStatus("current")
_RuijieMplsOamNotifications_ObjectIdentity = ObjectIdentity
ruijieMplsOamNotifications = _RuijieMplsOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2)
)
_RuijieMplsPsObjects_ObjectIdentity = ObjectIdentity
ruijieMplsPsObjects = _RuijieMplsPsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3)
)
_RuijieMplsPsTable_Object = MibTable
ruijieMplsPsTable = _RuijieMplsPsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieMplsPsTable.setStatus("current")
_RuijieMplsPsEntry_Object = MibTableRow
ruijieMplsPsEntry = _RuijieMplsPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1)
)
ruijieMplsPsEntry.setIndexNames(
    (0, "RUIJIE-MPLSOAM-MIB", "ruijieMplsPsIndex"),
)
if mibBuilder.loadTexts:
    ruijieMplsPsEntry.setStatus("current")
_RuijieMplsPsIndex_Type = Unsigned32
_RuijieMplsPsIndex_Object = MibTableColumn
ruijieMplsPsIndex = _RuijieMplsPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 1),
    _RuijieMplsPsIndex_Type()
)
ruijieMplsPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsIndex.setStatus("current")
_RuijieMplsPsGroupName_Type = OctetString
_RuijieMplsPsGroupName_Object = MibTableColumn
ruijieMplsPsGroupName = _RuijieMplsPsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 2),
    _RuijieMplsPsGroupName_Type()
)
ruijieMplsPsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsGroupName.setStatus("current")


class _RuijieMplsPsType_Type(Integer32):
    """Custom type ruijieMplsPsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuijieMplsPsType_Type.__name__ = "Integer32"
_RuijieMplsPsType_Object = MibTableColumn
ruijieMplsPsType = _RuijieMplsPsType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 3),
    _RuijieMplsPsType_Type()
)
ruijieMplsPsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsType.setStatus("current")
_RuijieMplsPsWorkLspName_Type = OctetString
_RuijieMplsPsWorkLspName_Object = MibTableColumn
ruijieMplsPsWorkLspName = _RuijieMplsPsWorkLspName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 4),
    _RuijieMplsPsWorkLspName_Type()
)
ruijieMplsPsWorkLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsWorkLspName.setStatus("current")


class _RuijieMplsPsWorkLspId_Type(Integer32):
    """Custom type ruijieMplsPsWorkLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieMplsPsWorkLspId_Type.__name__ = "Integer32"
_RuijieMplsPsWorkLspId_Object = MibTableColumn
ruijieMplsPsWorkLspId = _RuijieMplsPsWorkLspId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 5),
    _RuijieMplsPsWorkLspId_Type()
)
ruijieMplsPsWorkLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsWorkLspId.setStatus("current")
_RuijieMplsPsProtectLspName_Type = OctetString
_RuijieMplsPsProtectLspName_Object = MibTableColumn
ruijieMplsPsProtectLspName = _RuijieMplsPsProtectLspName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 6),
    _RuijieMplsPsProtectLspName_Type()
)
ruijieMplsPsProtectLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsProtectLspName.setStatus("current")


class _RuijieMplsPsProtectLspId_Type(Integer32):
    """Custom type ruijieMplsPsProtectLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieMplsPsProtectLspId_Type.__name__ = "Integer32"
_RuijieMplsPsProtectLspId_Object = MibTableColumn
ruijieMplsPsProtectLspId = _RuijieMplsPsProtectLspId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 7),
    _RuijieMplsPsProtectLspId_Type()
)
ruijieMplsPsProtectLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsProtectLspId.setStatus("current")


class _RuijieMplsPsRevertiveMode_Type(Integer32):
    """Custom type ruijieMplsPsRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieMplsPsRevertiveMode_Type.__name__ = "Integer32"
_RuijieMplsPsRevertiveMode_Object = MibTableColumn
ruijieMplsPsRevertiveMode = _RuijieMplsPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 8),
    _RuijieMplsPsRevertiveMode_Type()
)
ruijieMplsPsRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsRevertiveMode.setStatus("current")


class _RuijieMplsPsWTR_Type(Integer32):
    """Custom type ruijieMplsPsWTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_RuijieMplsPsWTR_Type.__name__ = "Integer32"
_RuijieMplsPsWTR_Object = MibTableColumn
ruijieMplsPsWTR = _RuijieMplsPsWTR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 9),
    _RuijieMplsPsWTR_Type()
)
ruijieMplsPsWTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsWTR.setStatus("current")


class _RuijieMplsPsHoldOff_Type(Integer32):
    """Custom type ruijieMplsPsHoldOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieMplsPsHoldOff_Type.__name__ = "Integer32"
_RuijieMplsPsHoldOff_Object = MibTableColumn
ruijieMplsPsHoldOff = _RuijieMplsPsHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 10),
    _RuijieMplsPsHoldOff_Type()
)
ruijieMplsPsHoldOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsHoldOff.setStatus("current")


class _RuijieMplsPsSwitchCondition_Type(Integer32):
    """Custom type ruijieMplsPsSwitchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_RuijieMplsPsSwitchCondition_Type.__name__ = "Integer32"
_RuijieMplsPsSwitchCondition_Object = MibTableColumn
ruijieMplsPsSwitchCondition = _RuijieMplsPsSwitchCondition_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 11),
    _RuijieMplsPsSwitchCondition_Type()
)
ruijieMplsPsSwitchCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsSwitchCondition.setStatus("current")


class _RuijieMplsPsWorkLspState_Type(Integer32):
    """Custom type ruijieMplsPsWorkLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieMplsPsWorkLspState_Type.__name__ = "Integer32"
_RuijieMplsPsWorkLspState_Object = MibTableColumn
ruijieMplsPsWorkLspState = _RuijieMplsPsWorkLspState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 12),
    _RuijieMplsPsWorkLspState_Type()
)
ruijieMplsPsWorkLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsWorkLspState.setStatus("current")


class _RuijieMplsPsProtLspState_Type(Integer32):
    """Custom type ruijieMplsPsProtLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieMplsPsProtLspState_Type.__name__ = "Integer32"
_RuijieMplsPsProtLspState_Object = MibTableColumn
ruijieMplsPsProtLspState = _RuijieMplsPsProtLspState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 13),
    _RuijieMplsPsProtLspState_Type()
)
ruijieMplsPsProtLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsProtLspState.setStatus("current")


class _RuijieMplsPsSwitchResult_Type(Integer32):
    """Custom type ruijieMplsPsSwitchResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieMplsPsSwitchResult_Type.__name__ = "Integer32"
_RuijieMplsPsSwitchResult_Object = MibTableColumn
ruijieMplsPsSwitchResult = _RuijieMplsPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 14),
    _RuijieMplsPsSwitchResult_Type()
)
ruijieMplsPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsSwitchResult.setStatus("current")
_RuijieMplsPsRowStatus_Type = RowStatus
_RuijieMplsPsRowStatus_Object = MibTableColumn
ruijieMplsPsRowStatus = _RuijieMplsPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 1, 1, 15),
    _RuijieMplsPsRowStatus_Type()
)
ruijieMplsPsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsPsRowStatus.setStatus("current")


class _RuijieMplsPsTrapOpen_Type(Unsigned32):
    """Custom type ruijieMplsPsTrapOpen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieMplsPsTrapOpen_Type.__name__ = "Unsigned32"
_RuijieMplsPsTrapOpen_Object = MibScalar
ruijieMplsPsTrapOpen = _RuijieMplsPsTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 3, 2),
    _RuijieMplsPsTrapOpen_Type()
)
ruijieMplsPsTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMplsPsTrapOpen.setStatus("current")
_RuijieMplsPsNotifications_ObjectIdentity = ObjectIdentity
ruijieMplsPsNotifications = _RuijieMplsPsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 4)
)
_RuijieMplsOamPsConformance_ObjectIdentity = ObjectIdentity
ruijieMplsOamPsConformance = _RuijieMplsOamPsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 5)
)
_RuijieMplsOamPsCompliances_ObjectIdentity = ObjectIdentity
ruijieMplsOamPsCompliances = _RuijieMplsOamPsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 5, 1)
)
_RuijieMplsOamPsGroups_ObjectIdentity = ObjectIdentity
ruijieMplsOamPsGroups = _RuijieMplsOamPsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 5, 2)
)

# Managed Objects groups

ruijieMplsPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 5, 2, 1)
)
ruijieMplsPsGroup.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsGroupName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsType"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsWorkLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsWorkLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsProtectLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsProtectLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsRevertiveMode"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsWTR"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsHoldOff"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsSwitchCondition"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsWorkLspState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsProtLspState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsSwitchResult"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsRowStatus"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsIndex"))
)
if mibBuilder.loadTexts:
    ruijieMplsPsGroup.setStatus("current")


# Notification objects

ruijieMplsOamIgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 1)
)
ruijieMplsOamIgrLSPOutDefect.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrAvaState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamIgrLSPOutDefect.setStatus(
        "current"
    )

ruijieMplsOamIgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 2)
)
ruijieMplsOamIgrLSPInDefect.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrAvaState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamIgrLSPInDefect.setStatus(
        "current"
    )

ruijieMplsOamIgrLSPAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 3)
)
ruijieMplsOamIgrLSPAva.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrAvaState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamIgrLSPAva.setStatus(
        "current"
    )

ruijieMplsOamIgrLSPUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 4)
)
ruijieMplsOamIgrLSPUnAva.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrAvaState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamIgrLSPUnAva.setStatus(
        "current"
    )

ruijieMplsOamEgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 5)
)
ruijieMplsOamEgrLSPOutDefect.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLsrId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrAvaState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamEgrLSPOutDefect.setStatus(
        "current"
    )

ruijieMplsOamEgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 6)
)
ruijieMplsOamEgrLSPInDefect.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLsrId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrAvaState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamEgrLSPInDefect.setStatus(
        "current"
    )

ruijieMplsOamEgrLSPAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 7)
)
ruijieMplsOamEgrLSPAva.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLsrId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrAvaState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamEgrLSPAva.setStatus(
        "current"
    )

ruijieMplsOamEgrLSPUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 8)
)
ruijieMplsOamEgrLSPUnAva.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLsrId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrAvaState"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamEgrLSPUnAva.setStatus(
        "current"
    )

ruijieMplsOamEgrFirstPkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 9)
)
ruijieMplsOamEgrFirstPkt.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLsrId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrDetType"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrDetFreq"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamEgrFirstPkt.setStatus(
        "current"
    )

ruijieMplsOamEgrAutoProFDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 2, 10)
)
ruijieMplsOamEgrAutoProFDI.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrIndex"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLsrId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsOamEgrEnable"))
)
if mibBuilder.loadTexts:
    ruijieMplsOamEgrAutoProFDI.setStatus(
        "current"
    )

ruijieMplsPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 4, 1)
)
ruijieMplsPsSwitchPtoW.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsWorkLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsWorkLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsProtectLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsProtectLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    ruijieMplsPsSwitchPtoW.setStatus(
        "current"
    )

ruijieMplsPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 4, 2)
)
ruijieMplsPsSwitchWtoP.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsWorkLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsWorkLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsProtectLspName"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsProtectLspId"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    ruijieMplsPsSwitchWtoP.setStatus(
        "current"
    )


# Notifications groups

ruijieMplsPsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 5, 2, 2)
)
ruijieMplsPsNotificationGroup.setObjects(
      *(("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsSwitchPtoW"),
        ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsSwitchWtoP"))
)
if mibBuilder.loadTexts:
    ruijieMplsPsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieMplsOamPsGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 93, 1, 5, 1, 1)
)
ruijieMplsOamPsGroupCompliance.setObjects(
    ("RUIJIE-MPLSOAM-MIB", "ruijieMplsPsGroup")
)
if mibBuilder.loadTexts:
    ruijieMplsOamPsGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MPLSOAM-MIB",
    **{"ruijieMplsOam": ruijieMplsOam,
       "ruijieMplsOamPs": ruijieMplsOamPs,
       "ruijieMplsOamObjects": ruijieMplsOamObjects,
       "ruijieMplsOamCapability": ruijieMplsOamCapability,
       "ruijieMplsOamIgrTable": ruijieMplsOamIgrTable,
       "ruijieMplsOamIgrEntry": ruijieMplsOamIgrEntry,
       "ruijieMplsOamIgrIndex": ruijieMplsOamIgrIndex,
       "ruijieMplsOamIgrLspName": ruijieMplsOamIgrLspName,
       "ruijieMplsOamIgrLspId": ruijieMplsOamIgrLspId,
       "ruijieMplsOamIgrDetType": ruijieMplsOamIgrDetType,
       "ruijieMplsOamIgrDetFreq": ruijieMplsOamIgrDetFreq,
       "ruijieMplsOamIgrRevType": ruijieMplsOamIgrRevType,
       "ruijieMplsOamIgrRevLspName": ruijieMplsOamIgrRevLspName,
       "ruijieMplsOamIgrEnable": ruijieMplsOamIgrEnable,
       "ruijieMplsOamIgrValid": ruijieMplsOamIgrValid,
       "ruijieMplsOamIgrAvaState": ruijieMplsOamIgrAvaState,
       "ruijieMplsOamIgrDefectType": ruijieMplsOamIgrDefectType,
       "ruijieMplsOamIgrRowStatus": ruijieMplsOamIgrRowStatus,
       "ruijieMplsOamEgrTable": ruijieMplsOamEgrTable,
       "ruijieMplsOamEgrEntry": ruijieMplsOamEgrEntry,
       "ruijieMplsOamEgrIndex": ruijieMplsOamEgrIndex,
       "ruijieMplsOamEgrLspName": ruijieMplsOamEgrLspName,
       "ruijieMplsOamEgrLsrId": ruijieMplsOamEgrLsrId,
       "ruijieMplsOamEgrLspId": ruijieMplsOamEgrLspId,
       "ruijieMplsOamEgrDetType": ruijieMplsOamEgrDetType,
       "ruijieMplsOamEgrDetFreq": ruijieMplsOamEgrDetFreq,
       "ruijieMplsOamEgrRevType": ruijieMplsOamEgrRevType,
       "ruijieMplsOamEgrRevLspName": ruijieMplsOamEgrRevLspName,
       "ruijieMplsOamEgrAutoEn": ruijieMplsOamEgrAutoEn,
       "ruijieMplsOamEgrAutoOvertime": ruijieMplsOamEgrAutoOvertime,
       "ruijieMplsOamEgrBDIFreq": ruijieMplsOamEgrBDIFreq,
       "ruijieMplsOamEgrEnable": ruijieMplsOamEgrEnable,
       "ruijieMplsOamEgrValid": ruijieMplsOamEgrValid,
       "ruijieMplsOamEgrAvaState": ruijieMplsOamEgrAvaState,
       "ruijieMplsOamEgrDefectType": ruijieMplsOamEgrDefectType,
       "ruijieMplsOamEgrRowStatus": ruijieMplsOamEgrRowStatus,
       "ruijieMplsOamTrapOpen": ruijieMplsOamTrapOpen,
       "ruijieMplsOamNotifications": ruijieMplsOamNotifications,
       "ruijieMplsOamIgrLSPOutDefect": ruijieMplsOamIgrLSPOutDefect,
       "ruijieMplsOamIgrLSPInDefect": ruijieMplsOamIgrLSPInDefect,
       "ruijieMplsOamIgrLSPAva": ruijieMplsOamIgrLSPAva,
       "ruijieMplsOamIgrLSPUnAva": ruijieMplsOamIgrLSPUnAva,
       "ruijieMplsOamEgrLSPOutDefect": ruijieMplsOamEgrLSPOutDefect,
       "ruijieMplsOamEgrLSPInDefect": ruijieMplsOamEgrLSPInDefect,
       "ruijieMplsOamEgrLSPAva": ruijieMplsOamEgrLSPAva,
       "ruijieMplsOamEgrLSPUnAva": ruijieMplsOamEgrLSPUnAva,
       "ruijieMplsOamEgrFirstPkt": ruijieMplsOamEgrFirstPkt,
       "ruijieMplsOamEgrAutoProFDI": ruijieMplsOamEgrAutoProFDI,
       "ruijieMplsPsObjects": ruijieMplsPsObjects,
       "ruijieMplsPsTable": ruijieMplsPsTable,
       "ruijieMplsPsEntry": ruijieMplsPsEntry,
       "ruijieMplsPsIndex": ruijieMplsPsIndex,
       "ruijieMplsPsGroupName": ruijieMplsPsGroupName,
       "ruijieMplsPsType": ruijieMplsPsType,
       "ruijieMplsPsWorkLspName": ruijieMplsPsWorkLspName,
       "ruijieMplsPsWorkLspId": ruijieMplsPsWorkLspId,
       "ruijieMplsPsProtectLspName": ruijieMplsPsProtectLspName,
       "ruijieMplsPsProtectLspId": ruijieMplsPsProtectLspId,
       "ruijieMplsPsRevertiveMode": ruijieMplsPsRevertiveMode,
       "ruijieMplsPsWTR": ruijieMplsPsWTR,
       "ruijieMplsPsHoldOff": ruijieMplsPsHoldOff,
       "ruijieMplsPsSwitchCondition": ruijieMplsPsSwitchCondition,
       "ruijieMplsPsWorkLspState": ruijieMplsPsWorkLspState,
       "ruijieMplsPsProtLspState": ruijieMplsPsProtLspState,
       "ruijieMplsPsSwitchResult": ruijieMplsPsSwitchResult,
       "ruijieMplsPsRowStatus": ruijieMplsPsRowStatus,
       "ruijieMplsPsTrapOpen": ruijieMplsPsTrapOpen,
       "ruijieMplsPsNotifications": ruijieMplsPsNotifications,
       "ruijieMplsPsSwitchPtoW": ruijieMplsPsSwitchPtoW,
       "ruijieMplsPsSwitchWtoP": ruijieMplsPsSwitchWtoP,
       "ruijieMplsOamPsConformance": ruijieMplsOamPsConformance,
       "ruijieMplsOamPsCompliances": ruijieMplsOamPsCompliances,
       "ruijieMplsOamPsGroupCompliance": ruijieMplsOamPsGroupCompliance,
       "ruijieMplsOamPsGroups": ruijieMplsOamPsGroups,
       "ruijieMplsPsGroup": ruijieMplsPsGroup,
       "ruijieMplsPsNotificationGroup": ruijieMplsPsNotificationGroup}
)
