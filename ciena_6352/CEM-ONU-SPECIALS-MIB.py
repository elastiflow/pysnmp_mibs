# SNMP MIB module (CEM-ONU-SPECIALS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-ONU-SPECIALS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(cnOnuSpecials,) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "cnOnuSpecials")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

cnOnuSpecialsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cn1000ConfigurationStatus(TextualConvention, Integer32):
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
        *(("configSucceeded", 1),
          ("configPending", 2),
          ("configFailed", 3),
          ("deleteInProgress", 4),
          ("deleteFailed", 5),
          ("configInProgress", 6))
    )



class CnOnuFourWireCuLoading(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonLoaded", 1),
          ("loaded", 2))
    )



class CnOnuCuCommonRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class CnOnuFourWireCu7db(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wh", 1),
          ("bk", 2))
    )



class CnOnuFourWireCuCardType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("fourWire0", 1)
    )



class CnOnuCuEsPotsCardType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("esPotsSink", 1),
          ("esPotsFeed", 2))
    )



class CnOnuCuBool(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )



class CnOnuCuDdsCardType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dds", 1)
    )



# MIB Managed Objects in the order of their OIDs

_CnOnuFourWireCuTable_Object = MibTable
cnOnuFourWireCuTable = _CnOnuFourWireCuTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    cnOnuFourWireCuTable.setStatus("current")
_CnOnuFourWireCuEntry_Object = MibTableRow
cnOnuFourWireCuEntry = _CnOnuFourWireCuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1)
)
cnOnuFourWireCuEntry.setIndexNames(
    (0, "CEM-ONU-SPECIALS-MIB", "cnOnuShelf"),
    (0, "CEM-ONU-SPECIALS-MIB", "cnOnuSlot"),
)
if mibBuilder.loadTexts:
    cnOnuFourWireCuEntry.setStatus("current")
_CnOnuFourWireCuConfigStatus_Type = Cn1000ConfigurationStatus
_CnOnuFourWireCuConfigStatus_Object = MibTableColumn
cnOnuFourWireCuConfigStatus = _CnOnuFourWireCuConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 1),
    _CnOnuFourWireCuConfigStatus_Type()
)
cnOnuFourWireCuConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnOnuFourWireCuConfigStatus.setStatus("current")
_CnOnuFourWireCuLoading_Type = CnOnuFourWireCuLoading
_CnOnuFourWireCuLoading_Object = MibTableColumn
cnOnuFourWireCuLoading = _CnOnuFourWireCuLoading_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 2),
    _CnOnuFourWireCuLoading_Type()
)
cnOnuFourWireCuLoading.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCuLoading.setStatus("current")


class _CnOnuFourWireCuImpedance_Type(Integer32):
    """Custom type cnOnuFourWireCuImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_CnOnuFourWireCuImpedance_Type.__name__ = "Integer32"
_CnOnuFourWireCuImpedance_Object = MibTableColumn
cnOnuFourWireCuImpedance = _CnOnuFourWireCuImpedance_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 3),
    _CnOnuFourWireCuImpedance_Type()
)
cnOnuFourWireCuImpedance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCuImpedance.setStatus("current")
_CnOnuFourWireCuHeight_Type = CnOnuCuCommonRange
_CnOnuFourWireCuHeight_Object = MibTableColumn
cnOnuFourWireCuHeight = _CnOnuFourWireCuHeight_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 4),
    _CnOnuFourWireCuHeight_Type()
)
cnOnuFourWireCuHeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCuHeight.setStatus("current")
_CnOnuFourWireCuBandwidth_Type = CnOnuCuCommonRange
_CnOnuFourWireCuBandwidth_Object = MibTableColumn
cnOnuFourWireCuBandwidth = _CnOnuFourWireCuBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 5),
    _CnOnuFourWireCuBandwidth_Type()
)
cnOnuFourWireCuBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCuBandwidth.setStatus("current")
_CnOnuFourWireCuSlope_Type = CnOnuCuCommonRange
_CnOnuFourWireCuSlope_Object = MibTableColumn
cnOnuFourWireCuSlope = _CnOnuFourWireCuSlope_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 6),
    _CnOnuFourWireCuSlope_Type()
)
cnOnuFourWireCuSlope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCuSlope.setStatus("current")
_CnOnuFourWireCu7dbj3_Type = CnOnuFourWireCu7db
_CnOnuFourWireCu7dbj3_Object = MibTableColumn
cnOnuFourWireCu7dbj3 = _CnOnuFourWireCu7dbj3_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 7),
    _CnOnuFourWireCu7dbj3_Type()
)
cnOnuFourWireCu7dbj3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCu7dbj3.setStatus("current")
_CnOnuFourWireCu7dbrcv_Type = CnOnuFourWireCu7db
_CnOnuFourWireCu7dbrcv_Object = MibTableColumn
cnOnuFourWireCu7dbrcv = _CnOnuFourWireCu7dbrcv_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 8),
    _CnOnuFourWireCu7dbrcv_Type()
)
cnOnuFourWireCu7dbrcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnOnuFourWireCu7dbrcv.setStatus("current")
_CnOnuFourWireCu7dbtrmt_Type = CnOnuFourWireCu7db
_CnOnuFourWireCu7dbtrmt_Object = MibTableColumn
cnOnuFourWireCu7dbtrmt = _CnOnuFourWireCu7dbtrmt_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 9),
    _CnOnuFourWireCu7dbtrmt_Type()
)
cnOnuFourWireCu7dbtrmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCu7dbtrmt.setStatus("current")


class _CnOnuFourWireCuRcvatt_Type(OctetString):
    """Custom type cnOnuFourWireCuRcvatt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnOnuFourWireCuRcvatt_Type.__name__ = "OctetString"
_CnOnuFourWireCuRcvatt_Object = MibTableColumn
cnOnuFourWireCuRcvatt = _CnOnuFourWireCuRcvatt_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 10),
    _CnOnuFourWireCuRcvatt_Type()
)
cnOnuFourWireCuRcvatt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCuRcvatt.setStatus("current")


class _CnOnuFourWireCuTrmtatt_Type(OctetString):
    """Custom type cnOnuFourWireCuTrmtatt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnOnuFourWireCuTrmtatt_Type.__name__ = "OctetString"
_CnOnuFourWireCuTrmtatt_Object = MibTableColumn
cnOnuFourWireCuTrmtatt = _CnOnuFourWireCuTrmtatt_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 11),
    _CnOnuFourWireCuTrmtatt_Type()
)
cnOnuFourWireCuTrmtatt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCuTrmtatt.setStatus("current")


class _CnOnuFourWireCuFunctionCode_Type(Integer32):
    """Custom type cnOnuFourWireCuFunctionCode based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dx4n", 1),
          ("dx4r", 2),
          ("eto4", 3),
          ("fxs1", 4),
          ("fxs2", 5),
          ("fxs3", 6),
          ("fxs5", 7),
          ("fxt1", 8),
          ("fxt2", 9),
          ("fxt3", 10),
          ("fxt5", 11),
          ("to4", 12))
    )


_CnOnuFourWireCuFunctionCode_Type.__name__ = "Integer32"
_CnOnuFourWireCuFunctionCode_Object = MibTableColumn
cnOnuFourWireCuFunctionCode = _CnOnuFourWireCuFunctionCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 12),
    _CnOnuFourWireCuFunctionCode_Type()
)
cnOnuFourWireCuFunctionCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuFourWireCuFunctionCode.setStatus("current")
_CnOnuFourWireCuCardType_Type = CnOnuFourWireCuCardType
_CnOnuFourWireCuCardType_Object = MibTableColumn
cnOnuFourWireCuCardType = _CnOnuFourWireCuCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 13),
    _CnOnuFourWireCuCardType_Type()
)
cnOnuFourWireCuCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnOnuFourWireCuCardType.setStatus("current")


class _CnOnuSlot_Type(Integer32):
    """Custom type cnOnuSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CnOnuSlot_Type.__name__ = "Integer32"
_CnOnuSlot_Object = MibTableColumn
cnOnuSlot = _CnOnuSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 15),
    _CnOnuSlot_Type()
)
cnOnuSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnOnuSlot.setStatus("current")


class _CnOnuShelf_Type(Integer32):
    """Custom type cnOnuShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CnOnuShelf_Type.__name__ = "Integer32"
_CnOnuShelf_Object = MibTableColumn
cnOnuShelf = _CnOnuShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 1, 1, 16),
    _CnOnuShelf_Type()
)
cnOnuShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnOnuShelf.setStatus("current")
_CnOnuCuEsPotsTable_Object = MibTable
cnOnuCuEsPotsTable = _CnOnuCuEsPotsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    cnOnuCuEsPotsTable.setStatus("current")
_CnOnuCuEsPotsEntry_Object = MibTableRow
cnOnuCuEsPotsEntry = _CnOnuCuEsPotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1)
)
cnOnuCuEsPotsEntry.setIndexNames(
    (0, "CEM-ONU-SPECIALS-MIB", "cnOnuShelf"),
    (0, "CEM-ONU-SPECIALS-MIB", "cnOnuSlot"),
    (0, "CEM-ONU-SPECIALS-MIB", "cnOnuPort"),
)
if mibBuilder.loadTexts:
    cnOnuCuEsPotsEntry.setStatus("current")


class _CnOnuPort_Type(Integer32):
    """Custom type cnOnuPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CnOnuPort_Type.__name__ = "Integer32"
_CnOnuPort_Object = MibTableColumn
cnOnuPort = _CnOnuPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 1),
    _CnOnuPort_Type()
)
cnOnuPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnOnuPort.setStatus("current")
_CnOnuCuEsPotsCardType_Type = CnOnuCuEsPotsCardType
_CnOnuCuEsPotsCardType_Object = MibTableColumn
cnOnuCuEsPotsCardType = _CnOnuCuEsPotsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 2),
    _CnOnuCuEsPotsCardType_Type()
)
cnOnuCuEsPotsCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsCardType.setStatus("current")


class _CnOnuCuEsPotsFuncCode_Type(Integer32):
    """Custom type cnOnuCuEsPotsFuncCode based on Integer32"""
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
        *(("unknown", 0),
          ("dpt", 1),
          ("fxo", 2),
          ("to", 3),
          ("dpo", 4),
          ("fxs", 5))
    )


_CnOnuCuEsPotsFuncCode_Type.__name__ = "Integer32"
_CnOnuCuEsPotsFuncCode_Object = MibTableColumn
cnOnuCuEsPotsFuncCode = _CnOnuCuEsPotsFuncCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 3),
    _CnOnuCuEsPotsFuncCode_Type()
)
cnOnuCuEsPotsFuncCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsFuncCode.setStatus("current")


class _CnOnuCuEsPotsImpedance_Type(Integer32):
    """Custom type cnOnuCuEsPotsImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 900),
    )


_CnOnuCuEsPotsImpedance_Type.__name__ = "Integer32"
_CnOnuCuEsPotsImpedance_Object = MibTableColumn
cnOnuCuEsPotsImpedance = _CnOnuCuEsPotsImpedance_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 4),
    _CnOnuCuEsPotsImpedance_Type()
)
cnOnuCuEsPotsImpedance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsImpedance.setStatus("current")
_CnOnuCuEsPotsBalance_Type = CnOnuCuCommonRange
_CnOnuCuEsPotsBalance_Object = MibTableColumn
cnOnuCuEsPotsBalance = _CnOnuCuEsPotsBalance_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 5),
    _CnOnuCuEsPotsBalance_Type()
)
cnOnuCuEsPotsBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsBalance.setStatus("current")


class _CnOnuCuEsPotsTrmtgain_Type(OctetString):
    """Custom type cnOnuCuEsPotsTrmtgain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnOnuCuEsPotsTrmtgain_Type.__name__ = "OctetString"
_CnOnuCuEsPotsTrmtgain_Object = MibTableColumn
cnOnuCuEsPotsTrmtgain = _CnOnuCuEsPotsTrmtgain_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 6),
    _CnOnuCuEsPotsTrmtgain_Type()
)
cnOnuCuEsPotsTrmtgain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsTrmtgain.setStatus("current")


class _CnOnuCuEsPotsRcvGain_Type(OctetString):
    """Custom type cnOnuCuEsPotsRcvGain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnOnuCuEsPotsRcvGain_Type.__name__ = "OctetString"
_CnOnuCuEsPotsRcvGain_Object = MibTableColumn
cnOnuCuEsPotsRcvGain = _CnOnuCuEsPotsRcvGain_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 7),
    _CnOnuCuEsPotsRcvGain_Type()
)
cnOnuCuEsPotsRcvGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsRcvGain.setStatus("current")


class _CnOnuCuEsPotsSlope_Type(Integer32):
    """Custom type cnOnuCuEsPotsSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CnOnuCuEsPotsSlope_Type.__name__ = "Integer32"
_CnOnuCuEsPotsSlope_Object = MibTableColumn
cnOnuCuEsPotsSlope = _CnOnuCuEsPotsSlope_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 8),
    _CnOnuCuEsPotsSlope_Type()
)
cnOnuCuEsPotsSlope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsSlope.setStatus("current")
_CnOnuCuEsPotsTollDiversion_Type = CnOnuCuBool
_CnOnuCuEsPotsTollDiversion_Object = MibTableColumn
cnOnuCuEsPotsTollDiversion = _CnOnuCuEsPotsTollDiversion_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 9),
    _CnOnuCuEsPotsTollDiversion_Type()
)
cnOnuCuEsPotsTollDiversion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsTollDiversion.setStatus("current")


class _CnOnuCuEsPotsSignalling_Type(Integer32):
    """Custom type cnOnuCuEsPotsSignalling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gs", 1),
          ("ls", 2))
    )


_CnOnuCuEsPotsSignalling_Type.__name__ = "Integer32"
_CnOnuCuEsPotsSignalling_Object = MibTableColumn
cnOnuCuEsPotsSignalling = _CnOnuCuEsPotsSignalling_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 10),
    _CnOnuCuEsPotsSignalling_Type()
)
cnOnuCuEsPotsSignalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsSignalling.setStatus("current")
_CnOnuCuEsPotsOnhookTransmission_Type = CnOnuCuBool
_CnOnuCuEsPotsOnhookTransmission_Object = MibTableColumn
cnOnuCuEsPotsOnhookTransmission = _CnOnuCuEsPotsOnhookTransmission_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 12),
    _CnOnuCuEsPotsOnhookTransmission_Type()
)
cnOnuCuEsPotsOnhookTransmission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsOnhookTransmission.setStatus("current")
_CnOnuCuEsPotsConfigStatus_Type = Cn1000ConfigurationStatus
_CnOnuCuEsPotsConfigStatus_Object = MibTableColumn
cnOnuCuEsPotsConfigStatus = _CnOnuCuEsPotsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 13),
    _CnOnuCuEsPotsConfigStatus_Type()
)
cnOnuCuEsPotsConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsConfigStatus.setStatus("current")
_CnOnuCuEsPotsDeleteFlag_Type = CnOnuCuBool
_CnOnuCuEsPotsDeleteFlag_Object = MibTableColumn
cnOnuCuEsPotsDeleteFlag = _CnOnuCuEsPotsDeleteFlag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 2, 1, 14),
    _CnOnuCuEsPotsDeleteFlag_Type()
)
cnOnuCuEsPotsDeleteFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnOnuCuEsPotsDeleteFlag.setStatus("current")
_CnOnuCuDdsTable_Object = MibTable
cnOnuCuDdsTable = _CnOnuCuDdsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    cnOnuCuDdsTable.setStatus("current")
_CnOnuCuDdsEntry_Object = MibTableRow
cnOnuCuDdsEntry = _CnOnuCuDdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3, 1)
)
cnOnuCuDdsEntry.setIndexNames(
    (0, "CEM-ONU-SPECIALS-MIB", "cnOnuShelf"),
    (0, "CEM-ONU-SPECIALS-MIB", "cnOnuSlot"),
)
if mibBuilder.loadTexts:
    cnOnuCuDdsEntry.setStatus("current")
_CnOnuCuDdsCardType_Type = CnOnuCuDdsCardType
_CnOnuCuDdsCardType_Object = MibTableColumn
cnOnuCuDdsCardType = _CnOnuCuDdsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3, 1, 1),
    _CnOnuCuDdsCardType_Type()
)
cnOnuCuDdsCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnOnuCuDdsCardType.setStatus("current")


class _CnOnuCuDdsFuncCode_Type(Integer32):
    """Custom type cnOnuCuDdsFuncCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ocu", 1))
    )


_CnOnuCuDdsFuncCode_Type.__name__ = "Integer32"
_CnOnuCuDdsFuncCode_Object = MibTableColumn
cnOnuCuDdsFuncCode = _CnOnuCuDdsFuncCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3, 1, 2),
    _CnOnuCuDdsFuncCode_Type()
)
cnOnuCuDdsFuncCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuDdsFuncCode.setStatus("current")


class _CnOnuCuDdsDataRate_Type(Integer32):
    """Custom type cnOnuCuDdsDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(24,
              48,
              96,
              192,
              560,
              640)
        )
    )
    namedValues = NamedValues(
        *(("twentyfour", 24),
          ("fortyeight", 48),
          ("ninetysix", 96),
          ("oneninetytwo", 192),
          ("fiftysixk", 560),
          ("sixtyfourk", 640))
    )


_CnOnuCuDdsDataRate_Type.__name__ = "Integer32"
_CnOnuCuDdsDataRate_Object = MibTableColumn
cnOnuCuDdsDataRate = _CnOnuCuDdsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3, 1, 3),
    _CnOnuCuDdsDataRate_Type()
)
cnOnuCuDdsDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuDdsDataRate.setStatus("current")


class _CnOnuCuDdsErrorCorrection_Type(Integer32):
    """Custom type cnOnuCuDdsErrorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scec", 1),
          ("mvec", 2),
          ("none", 3))
    )


_CnOnuCuDdsErrorCorrection_Type.__name__ = "Integer32"
_CnOnuCuDdsErrorCorrection_Object = MibTableColumn
cnOnuCuDdsErrorCorrection = _CnOnuCuDdsErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3, 1, 4),
    _CnOnuCuDdsErrorCorrection_Type()
)
cnOnuCuDdsErrorCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuDdsErrorCorrection.setStatus("current")


class _CnOnuCuDdsAllZeroCode_Type(Integer32):
    """Custom type cnOnuCuDdsAllZeroCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 2))
    )


_CnOnuCuDdsAllZeroCode_Type.__name__ = "Integer32"
_CnOnuCuDdsAllZeroCode_Object = MibTableColumn
cnOnuCuDdsAllZeroCode = _CnOnuCuDdsAllZeroCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3, 1, 5),
    _CnOnuCuDdsAllZeroCode_Type()
)
cnOnuCuDdsAllZeroCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuDdsAllZeroCode.setStatus("current")


class _CnOnuCuDdsSecondaryChannel_Type(Integer32):
    """Custom type cnOnuCuDdsSecondaryChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnOnuCuDdsSecondaryChannel_Type.__name__ = "Integer32"
_CnOnuCuDdsSecondaryChannel_Object = MibTableColumn
cnOnuCuDdsSecondaryChannel = _CnOnuCuDdsSecondaryChannel_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3, 1, 6),
    _CnOnuCuDdsSecondaryChannel_Type()
)
cnOnuCuDdsSecondaryChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnOnuCuDdsSecondaryChannel.setStatus("current")
_CnOnuCuDdsConfigStatus_Type = Cn1000ConfigurationStatus
_CnOnuCuDdsConfigStatus_Object = MibTableColumn
cnOnuCuDdsConfigStatus = _CnOnuCuDdsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 1, 3, 1, 7),
    _CnOnuCuDdsConfigStatus_Type()
)
cnOnuCuDdsConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnOnuCuDdsConfigStatus.setStatus("current")
_CnOnuSpecialsCompliances_ObjectIdentity = ObjectIdentity
cnOnuSpecialsCompliances = _CnOnuSpecialsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 2)
)

# Managed Objects groups

cnOnuSpecialsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7, 2, 1)
)
cnOnuSpecialsMandatoryGroup.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuImpedance"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuHeight"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuBandwidth"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuSlope"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCu7dbj3"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCu7dbrcv"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCu7dbtrmt"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuRcvatt"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsFuncCode"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsImpedance"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsBalance"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsTrmtgain"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsRcvGain"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsSlope"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsTollDiversion"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsSignalling"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsOnhookTransmission"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuDdsFuncCode"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuDdsDataRate"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuDdsErrorCorrection"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuDdsAllZeroCode"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuLoading"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuCardType"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsCardType"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuDdsCardType"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuDdsConfigStatus"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsConfigStatus"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuConfigStatus"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuEsPotsDeleteFlag"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuCuDdsSecondaryChannel"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuTrmtatt"),
        ("CEM-ONU-SPECIALS-MIB", "cnOnuFourWireCuFunctionCode"))
)
if mibBuilder.loadTexts:
    cnOnuSpecialsMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-ONU-SPECIALS-MIB",
    **{"Cn1000ConfigurationStatus": Cn1000ConfigurationStatus,
       "CnOnuFourWireCuLoading": CnOnuFourWireCuLoading,
       "CnOnuCuCommonRange": CnOnuCuCommonRange,
       "CnOnuFourWireCu7db": CnOnuFourWireCu7db,
       "CnOnuFourWireCuCardType": CnOnuFourWireCuCardType,
       "CnOnuCuEsPotsCardType": CnOnuCuEsPotsCardType,
       "CnOnuCuBool": CnOnuCuBool,
       "CnOnuCuDdsCardType": CnOnuCuDdsCardType,
       "cnOnuSpecialsModule": cnOnuSpecialsModule,
       "cnOnuFourWireCuTable": cnOnuFourWireCuTable,
       "cnOnuFourWireCuEntry": cnOnuFourWireCuEntry,
       "cnOnuFourWireCuConfigStatus": cnOnuFourWireCuConfigStatus,
       "cnOnuFourWireCuLoading": cnOnuFourWireCuLoading,
       "cnOnuFourWireCuImpedance": cnOnuFourWireCuImpedance,
       "cnOnuFourWireCuHeight": cnOnuFourWireCuHeight,
       "cnOnuFourWireCuBandwidth": cnOnuFourWireCuBandwidth,
       "cnOnuFourWireCuSlope": cnOnuFourWireCuSlope,
       "cnOnuFourWireCu7dbj3": cnOnuFourWireCu7dbj3,
       "cnOnuFourWireCu7dbrcv": cnOnuFourWireCu7dbrcv,
       "cnOnuFourWireCu7dbtrmt": cnOnuFourWireCu7dbtrmt,
       "cnOnuFourWireCuRcvatt": cnOnuFourWireCuRcvatt,
       "cnOnuFourWireCuTrmtatt": cnOnuFourWireCuTrmtatt,
       "cnOnuFourWireCuFunctionCode": cnOnuFourWireCuFunctionCode,
       "cnOnuFourWireCuCardType": cnOnuFourWireCuCardType,
       "cnOnuSlot": cnOnuSlot,
       "cnOnuShelf": cnOnuShelf,
       "cnOnuCuEsPotsTable": cnOnuCuEsPotsTable,
       "cnOnuCuEsPotsEntry": cnOnuCuEsPotsEntry,
       "cnOnuPort": cnOnuPort,
       "cnOnuCuEsPotsCardType": cnOnuCuEsPotsCardType,
       "cnOnuCuEsPotsFuncCode": cnOnuCuEsPotsFuncCode,
       "cnOnuCuEsPotsImpedance": cnOnuCuEsPotsImpedance,
       "cnOnuCuEsPotsBalance": cnOnuCuEsPotsBalance,
       "cnOnuCuEsPotsTrmtgain": cnOnuCuEsPotsTrmtgain,
       "cnOnuCuEsPotsRcvGain": cnOnuCuEsPotsRcvGain,
       "cnOnuCuEsPotsSlope": cnOnuCuEsPotsSlope,
       "cnOnuCuEsPotsTollDiversion": cnOnuCuEsPotsTollDiversion,
       "cnOnuCuEsPotsSignalling": cnOnuCuEsPotsSignalling,
       "cnOnuCuEsPotsOnhookTransmission": cnOnuCuEsPotsOnhookTransmission,
       "cnOnuCuEsPotsConfigStatus": cnOnuCuEsPotsConfigStatus,
       "cnOnuCuEsPotsDeleteFlag": cnOnuCuEsPotsDeleteFlag,
       "cnOnuCuDdsTable": cnOnuCuDdsTable,
       "cnOnuCuDdsEntry": cnOnuCuDdsEntry,
       "cnOnuCuDdsCardType": cnOnuCuDdsCardType,
       "cnOnuCuDdsFuncCode": cnOnuCuDdsFuncCode,
       "cnOnuCuDdsDataRate": cnOnuCuDdsDataRate,
       "cnOnuCuDdsErrorCorrection": cnOnuCuDdsErrorCorrection,
       "cnOnuCuDdsAllZeroCode": cnOnuCuDdsAllZeroCode,
       "cnOnuCuDdsSecondaryChannel": cnOnuCuDdsSecondaryChannel,
       "cnOnuCuDdsConfigStatus": cnOnuCuDdsConfigStatus,
       "cnOnuSpecialsCompliances": cnOnuSpecialsCompliances,
       "cnOnuSpecialsMandatoryGroup": cnOnuSpecialsMandatoryGroup}
)
