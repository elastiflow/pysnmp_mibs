# SNMP MIB module (ACD-TWAMP-GEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/accedian_22420/ACD-TWAMP-GEN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:08:00 2025
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdTwampGen = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19)
)
if mibBuilder.loadTexts:
    acdTwampGen.setRevisions(
        ("2016-09-23 01:00",
         "2016-05-26 01:00",
         "2014-02-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdTwampGenResultTable_Object = MibTable
acdTwampGenResultTable = _AcdTwampGenResultTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1)
)
if mibBuilder.loadTexts:
    acdTwampGenResultTable.setStatus("current")
_AcdTwampGenResultEntry_Object = MibTableRow
acdTwampGenResultEntry = _AcdTwampGenResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1)
)
acdTwampGenResultEntry.setIndexNames(
    (0, "ACD-TWAMP-GEN-MIB", "acdTwampGenResultID"),
)
if mibBuilder.loadTexts:
    acdTwampGenResultEntry.setStatus("current")
_AcdTwampGenResultID_Type = Unsigned32
_AcdTwampGenResultID_Object = MibTableColumn
acdTwampGenResultID = _AcdTwampGenResultID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 1),
    _AcdTwampGenResultID_Type()
)
acdTwampGenResultID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdTwampGenResultID.setStatus("current")


class _AcdTwampGenResultInstName_Type(DisplayString):
    """Custom type acdTwampGenResultInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdTwampGenResultInstName_Type.__name__ = "DisplayString"
_AcdTwampGenResultInstName_Object = MibTableColumn
acdTwampGenResultInstName = _AcdTwampGenResultInstName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 2),
    _AcdTwampGenResultInstName_Type()
)
acdTwampGenResultInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultInstName.setStatus("current")
_AcdTwampGenResultPeriodNb_Type = Unsigned32
_AcdTwampGenResultPeriodNb_Object = MibTableColumn
acdTwampGenResultPeriodNb = _AcdTwampGenResultPeriodNb_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 3),
    _AcdTwampGenResultPeriodNb_Type()
)
acdTwampGenResultPeriodNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPeriodNb.setStatus("current")
_AcdTwampGenResultPeriodTime_Type = DateAndTime
_AcdTwampGenResultPeriodTime_Object = MibTableColumn
acdTwampGenResultPeriodTime = _AcdTwampGenResultPeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 4),
    _AcdTwampGenResultPeriodTime_Type()
)
acdTwampGenResultPeriodTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPeriodTime.setStatus("current")
_AcdTwampGenResultCurrTxPacketCount_Type = Counter64
_AcdTwampGenResultCurrTxPacketCount_Object = MibTableColumn
acdTwampGenResultCurrTxPacketCount = _AcdTwampGenResultCurrTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 5),
    _AcdTwampGenResultCurrTxPacketCount_Type()
)
acdTwampGenResultCurrTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultCurrTxPacketCount.setStatus("current")
_AcdTwampGenResultCurrRxPacketCount_Type = Counter64
_AcdTwampGenResultCurrRxPacketCount_Object = MibTableColumn
acdTwampGenResultCurrRxPacketCount = _AcdTwampGenResultCurrRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 6),
    _AcdTwampGenResultCurrRxPacketCount_Type()
)
acdTwampGenResultCurrRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultCurrRxPacketCount.setStatus("current")
_AcdTwampGenResultTwoWayDelayValid_Type = TruthValue
_AcdTwampGenResultTwoWayDelayValid_Object = MibTableColumn
acdTwampGenResultTwoWayDelayValid = _AcdTwampGenResultTwoWayDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 7),
    _AcdTwampGenResultTwoWayDelayValid_Type()
)
acdTwampGenResultTwoWayDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDelayValid.setStatus("current")
_AcdTwampGenResultTwoWayDelayInstValue_Type = Integer32
_AcdTwampGenResultTwoWayDelayInstValue_Object = MibTableColumn
acdTwampGenResultTwoWayDelayInstValue = _AcdTwampGenResultTwoWayDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 8),
    _AcdTwampGenResultTwoWayDelayInstValue_Type()
)
acdTwampGenResultTwoWayDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDelayInstValue.setStatus("current")
_AcdTwampGenResultTwoWayDelayCurrSamples_Type = Unsigned32
_AcdTwampGenResultTwoWayDelayCurrSamples_Object = MibTableColumn
acdTwampGenResultTwoWayDelayCurrSamples = _AcdTwampGenResultTwoWayDelayCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 9),
    _AcdTwampGenResultTwoWayDelayCurrSamples_Type()
)
acdTwampGenResultTwoWayDelayCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDelayCurrSamples.setStatus("current")
_AcdTwampGenResultTwoWayDelayCurrMinValue_Type = Integer32
_AcdTwampGenResultTwoWayDelayCurrMinValue_Object = MibTableColumn
acdTwampGenResultTwoWayDelayCurrMinValue = _AcdTwampGenResultTwoWayDelayCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 10),
    _AcdTwampGenResultTwoWayDelayCurrMinValue_Type()
)
acdTwampGenResultTwoWayDelayCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDelayCurrMinValue.setStatus("current")
_AcdTwampGenResultTwoWayDelayCurrMaxValue_Type = Integer32
_AcdTwampGenResultTwoWayDelayCurrMaxValue_Object = MibTableColumn
acdTwampGenResultTwoWayDelayCurrMaxValue = _AcdTwampGenResultTwoWayDelayCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 11),
    _AcdTwampGenResultTwoWayDelayCurrMaxValue_Type()
)
acdTwampGenResultTwoWayDelayCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDelayCurrMaxValue.setStatus("current")
_AcdTwampGenResultTwoWayDelayCurrAvgValue_Type = Integer32
_AcdTwampGenResultTwoWayDelayCurrAvgValue_Object = MibTableColumn
acdTwampGenResultTwoWayDelayCurrAvgValue = _AcdTwampGenResultTwoWayDelayCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 12),
    _AcdTwampGenResultTwoWayDelayCurrAvgValue_Type()
)
acdTwampGenResultTwoWayDelayCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDelayCurrAvgValue.setStatus("current")
_AcdTwampGenResultTwoWayDelayCurrThreshEx_Type = Unsigned32
_AcdTwampGenResultTwoWayDelayCurrThreshEx_Object = MibTableColumn
acdTwampGenResultTwoWayDelayCurrThreshEx = _AcdTwampGenResultTwoWayDelayCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 13),
    _AcdTwampGenResultTwoWayDelayCurrThreshEx_Type()
)
acdTwampGenResultTwoWayDelayCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDelayCurrThreshEx.setStatus("current")
_AcdTwampGenResultTwoWayDvValid_Type = TruthValue
_AcdTwampGenResultTwoWayDvValid_Object = MibTableColumn
acdTwampGenResultTwoWayDvValid = _AcdTwampGenResultTwoWayDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 14),
    _AcdTwampGenResultTwoWayDvValid_Type()
)
acdTwampGenResultTwoWayDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDvValid.setStatus("current")
_AcdTwampGenResultTwoWayDvInstValue_Type = Integer32
_AcdTwampGenResultTwoWayDvInstValue_Object = MibTableColumn
acdTwampGenResultTwoWayDvInstValue = _AcdTwampGenResultTwoWayDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 15),
    _AcdTwampGenResultTwoWayDvInstValue_Type()
)
acdTwampGenResultTwoWayDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDvInstValue.setStatus("current")
_AcdTwampGenResultTwoWayDvCurrSamples_Type = Unsigned32
_AcdTwampGenResultTwoWayDvCurrSamples_Object = MibTableColumn
acdTwampGenResultTwoWayDvCurrSamples = _AcdTwampGenResultTwoWayDvCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 16),
    _AcdTwampGenResultTwoWayDvCurrSamples_Type()
)
acdTwampGenResultTwoWayDvCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDvCurrSamples.setStatus("current")
_AcdTwampGenResultTwoWayDvCurrMinValue_Type = Integer32
_AcdTwampGenResultTwoWayDvCurrMinValue_Object = MibTableColumn
acdTwampGenResultTwoWayDvCurrMinValue = _AcdTwampGenResultTwoWayDvCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 17),
    _AcdTwampGenResultTwoWayDvCurrMinValue_Type()
)
acdTwampGenResultTwoWayDvCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDvCurrMinValue.setStatus("current")
_AcdTwampGenResultTwoWayDvCurrMaxValue_Type = Integer32
_AcdTwampGenResultTwoWayDvCurrMaxValue_Object = MibTableColumn
acdTwampGenResultTwoWayDvCurrMaxValue = _AcdTwampGenResultTwoWayDvCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 18),
    _AcdTwampGenResultTwoWayDvCurrMaxValue_Type()
)
acdTwampGenResultTwoWayDvCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDvCurrMaxValue.setStatus("current")
_AcdTwampGenResultTwoWayDvCurrAvgValue_Type = Integer32
_AcdTwampGenResultTwoWayDvCurrAvgValue_Object = MibTableColumn
acdTwampGenResultTwoWayDvCurrAvgValue = _AcdTwampGenResultTwoWayDvCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 19),
    _AcdTwampGenResultTwoWayDvCurrAvgValue_Type()
)
acdTwampGenResultTwoWayDvCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDvCurrAvgValue.setStatus("current")
_AcdTwampGenResultTwoWayDvCurrThreshEx_Type = Unsigned32
_AcdTwampGenResultTwoWayDvCurrThreshEx_Object = MibTableColumn
acdTwampGenResultTwoWayDvCurrThreshEx = _AcdTwampGenResultTwoWayDvCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 20),
    _AcdTwampGenResultTwoWayDvCurrThreshEx_Type()
)
acdTwampGenResultTwoWayDvCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultTwoWayDvCurrThreshEx.setStatus("current")
_AcdTwampGenResultOneWayNeDelayValid_Type = TruthValue
_AcdTwampGenResultOneWayNeDelayValid_Object = MibTableColumn
acdTwampGenResultOneWayNeDelayValid = _AcdTwampGenResultOneWayNeDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 21),
    _AcdTwampGenResultOneWayNeDelayValid_Type()
)
acdTwampGenResultOneWayNeDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDelayValid.setStatus("current")
_AcdTwampGenResultOneWayNeDelayInstValue_Type = Integer32
_AcdTwampGenResultOneWayNeDelayInstValue_Object = MibTableColumn
acdTwampGenResultOneWayNeDelayInstValue = _AcdTwampGenResultOneWayNeDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 22),
    _AcdTwampGenResultOneWayNeDelayInstValue_Type()
)
acdTwampGenResultOneWayNeDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDelayInstValue.setStatus("current")
_AcdTwampGenResultOneWayNeDelayCurrSamples_Type = Unsigned32
_AcdTwampGenResultOneWayNeDelayCurrSamples_Object = MibTableColumn
acdTwampGenResultOneWayNeDelayCurrSamples = _AcdTwampGenResultOneWayNeDelayCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 23),
    _AcdTwampGenResultOneWayNeDelayCurrSamples_Type()
)
acdTwampGenResultOneWayNeDelayCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDelayCurrSamples.setStatus("current")
_AcdTwampGenResultOneWayNeDelayCurrMinValue_Type = Integer32
_AcdTwampGenResultOneWayNeDelayCurrMinValue_Object = MibTableColumn
acdTwampGenResultOneWayNeDelayCurrMinValue = _AcdTwampGenResultOneWayNeDelayCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 24),
    _AcdTwampGenResultOneWayNeDelayCurrMinValue_Type()
)
acdTwampGenResultOneWayNeDelayCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDelayCurrMinValue.setStatus("current")
_AcdTwampGenResultOneWayNeDelayCurrMaxValue_Type = Integer32
_AcdTwampGenResultOneWayNeDelayCurrMaxValue_Object = MibTableColumn
acdTwampGenResultOneWayNeDelayCurrMaxValue = _AcdTwampGenResultOneWayNeDelayCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 25),
    _AcdTwampGenResultOneWayNeDelayCurrMaxValue_Type()
)
acdTwampGenResultOneWayNeDelayCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDelayCurrMaxValue.setStatus("current")
_AcdTwampGenResultOneWayNeDelayCurrAvgValue_Type = Integer32
_AcdTwampGenResultOneWayNeDelayCurrAvgValue_Object = MibTableColumn
acdTwampGenResultOneWayNeDelayCurrAvgValue = _AcdTwampGenResultOneWayNeDelayCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 26),
    _AcdTwampGenResultOneWayNeDelayCurrAvgValue_Type()
)
acdTwampGenResultOneWayNeDelayCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDelayCurrAvgValue.setStatus("current")
_AcdTwampGenResultOneWayNeDelayCurrThreshEx_Type = Unsigned32
_AcdTwampGenResultOneWayNeDelayCurrThreshEx_Object = MibTableColumn
acdTwampGenResultOneWayNeDelayCurrThreshEx = _AcdTwampGenResultOneWayNeDelayCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 27),
    _AcdTwampGenResultOneWayNeDelayCurrThreshEx_Type()
)
acdTwampGenResultOneWayNeDelayCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDelayCurrThreshEx.setStatus("current")
_AcdTwampGenResultOneWayNeDvValid_Type = TruthValue
_AcdTwampGenResultOneWayNeDvValid_Object = MibTableColumn
acdTwampGenResultOneWayNeDvValid = _AcdTwampGenResultOneWayNeDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 28),
    _AcdTwampGenResultOneWayNeDvValid_Type()
)
acdTwampGenResultOneWayNeDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDvValid.setStatus("current")
_AcdTwampGenResultOneWayNeDvInstValue_Type = Integer32
_AcdTwampGenResultOneWayNeDvInstValue_Object = MibTableColumn
acdTwampGenResultOneWayNeDvInstValue = _AcdTwampGenResultOneWayNeDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 29),
    _AcdTwampGenResultOneWayNeDvInstValue_Type()
)
acdTwampGenResultOneWayNeDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDvInstValue.setStatus("current")
_AcdTwampGenResultOneWayNeDvCurrSamples_Type = Unsigned32
_AcdTwampGenResultOneWayNeDvCurrSamples_Object = MibTableColumn
acdTwampGenResultOneWayNeDvCurrSamples = _AcdTwampGenResultOneWayNeDvCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 30),
    _AcdTwampGenResultOneWayNeDvCurrSamples_Type()
)
acdTwampGenResultOneWayNeDvCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDvCurrSamples.setStatus("current")
_AcdTwampGenResultOneWayNeDvCurrMinValue_Type = Integer32
_AcdTwampGenResultOneWayNeDvCurrMinValue_Object = MibTableColumn
acdTwampGenResultOneWayNeDvCurrMinValue = _AcdTwampGenResultOneWayNeDvCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 31),
    _AcdTwampGenResultOneWayNeDvCurrMinValue_Type()
)
acdTwampGenResultOneWayNeDvCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDvCurrMinValue.setStatus("current")
_AcdTwampGenResultOneWayNeDvCurrMaxValue_Type = Integer32
_AcdTwampGenResultOneWayNeDvCurrMaxValue_Object = MibTableColumn
acdTwampGenResultOneWayNeDvCurrMaxValue = _AcdTwampGenResultOneWayNeDvCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 32),
    _AcdTwampGenResultOneWayNeDvCurrMaxValue_Type()
)
acdTwampGenResultOneWayNeDvCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDvCurrMaxValue.setStatus("current")
_AcdTwampGenResultOneWayNeDvCurrAvgValue_Type = Integer32
_AcdTwampGenResultOneWayNeDvCurrAvgValue_Object = MibTableColumn
acdTwampGenResultOneWayNeDvCurrAvgValue = _AcdTwampGenResultOneWayNeDvCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 33),
    _AcdTwampGenResultOneWayNeDvCurrAvgValue_Type()
)
acdTwampGenResultOneWayNeDvCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDvCurrAvgValue.setStatus("current")
_AcdTwampGenResultOneWayNeDvCurrThreshEx_Type = Unsigned32
_AcdTwampGenResultOneWayNeDvCurrThreshEx_Object = MibTableColumn
acdTwampGenResultOneWayNeDvCurrThreshEx = _AcdTwampGenResultOneWayNeDvCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 34),
    _AcdTwampGenResultOneWayNeDvCurrThreshEx_Type()
)
acdTwampGenResultOneWayNeDvCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayNeDvCurrThreshEx.setStatus("current")
_AcdTwampGenResultOneWayFeDelayValid_Type = TruthValue
_AcdTwampGenResultOneWayFeDelayValid_Object = MibTableColumn
acdTwampGenResultOneWayFeDelayValid = _AcdTwampGenResultOneWayFeDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 35),
    _AcdTwampGenResultOneWayFeDelayValid_Type()
)
acdTwampGenResultOneWayFeDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDelayValid.setStatus("current")
_AcdTwampGenResultOneWayFeDelayInstValue_Type = Integer32
_AcdTwampGenResultOneWayFeDelayInstValue_Object = MibTableColumn
acdTwampGenResultOneWayFeDelayInstValue = _AcdTwampGenResultOneWayFeDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 36),
    _AcdTwampGenResultOneWayFeDelayInstValue_Type()
)
acdTwampGenResultOneWayFeDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDelayInstValue.setStatus("current")
_AcdTwampGenResultOneWayFeDelayCurrSamples_Type = Unsigned32
_AcdTwampGenResultOneWayFeDelayCurrSamples_Object = MibTableColumn
acdTwampGenResultOneWayFeDelayCurrSamples = _AcdTwampGenResultOneWayFeDelayCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 37),
    _AcdTwampGenResultOneWayFeDelayCurrSamples_Type()
)
acdTwampGenResultOneWayFeDelayCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDelayCurrSamples.setStatus("current")
_AcdTwampGenResultOneWayFeDelayCurrMinValue_Type = Integer32
_AcdTwampGenResultOneWayFeDelayCurrMinValue_Object = MibTableColumn
acdTwampGenResultOneWayFeDelayCurrMinValue = _AcdTwampGenResultOneWayFeDelayCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 38),
    _AcdTwampGenResultOneWayFeDelayCurrMinValue_Type()
)
acdTwampGenResultOneWayFeDelayCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDelayCurrMinValue.setStatus("current")
_AcdTwampGenResultOneWayFeDelayCurrMaxValue_Type = Integer32
_AcdTwampGenResultOneWayFeDelayCurrMaxValue_Object = MibTableColumn
acdTwampGenResultOneWayFeDelayCurrMaxValue = _AcdTwampGenResultOneWayFeDelayCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 39),
    _AcdTwampGenResultOneWayFeDelayCurrMaxValue_Type()
)
acdTwampGenResultOneWayFeDelayCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDelayCurrMaxValue.setStatus("current")
_AcdTwampGenResultOneWayFeDelayCurrAvgValue_Type = Integer32
_AcdTwampGenResultOneWayFeDelayCurrAvgValue_Object = MibTableColumn
acdTwampGenResultOneWayFeDelayCurrAvgValue = _AcdTwampGenResultOneWayFeDelayCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 40),
    _AcdTwampGenResultOneWayFeDelayCurrAvgValue_Type()
)
acdTwampGenResultOneWayFeDelayCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDelayCurrAvgValue.setStatus("current")
_AcdTwampGenResultOneWayFeDelayCurrThreshEx_Type = Unsigned32
_AcdTwampGenResultOneWayFeDelayCurrThreshEx_Object = MibTableColumn
acdTwampGenResultOneWayFeDelayCurrThreshEx = _AcdTwampGenResultOneWayFeDelayCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 41),
    _AcdTwampGenResultOneWayFeDelayCurrThreshEx_Type()
)
acdTwampGenResultOneWayFeDelayCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDelayCurrThreshEx.setStatus("current")
_AcdTwampGenResultOneWayFeDvValid_Type = TruthValue
_AcdTwampGenResultOneWayFeDvValid_Object = MibTableColumn
acdTwampGenResultOneWayFeDvValid = _AcdTwampGenResultOneWayFeDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 42),
    _AcdTwampGenResultOneWayFeDvValid_Type()
)
acdTwampGenResultOneWayFeDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDvValid.setStatus("current")
_AcdTwampGenResultOneWayFeDvInstValue_Type = Integer32
_AcdTwampGenResultOneWayFeDvInstValue_Object = MibTableColumn
acdTwampGenResultOneWayFeDvInstValue = _AcdTwampGenResultOneWayFeDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 43),
    _AcdTwampGenResultOneWayFeDvInstValue_Type()
)
acdTwampGenResultOneWayFeDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDvInstValue.setStatus("current")
_AcdTwampGenResultOneWayFeDvCurrSamples_Type = Unsigned32
_AcdTwampGenResultOneWayFeDvCurrSamples_Object = MibTableColumn
acdTwampGenResultOneWayFeDvCurrSamples = _AcdTwampGenResultOneWayFeDvCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 44),
    _AcdTwampGenResultOneWayFeDvCurrSamples_Type()
)
acdTwampGenResultOneWayFeDvCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDvCurrSamples.setStatus("current")
_AcdTwampGenResultOneWayFeDvCurrMinValue_Type = Integer32
_AcdTwampGenResultOneWayFeDvCurrMinValue_Object = MibTableColumn
acdTwampGenResultOneWayFeDvCurrMinValue = _AcdTwampGenResultOneWayFeDvCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 45),
    _AcdTwampGenResultOneWayFeDvCurrMinValue_Type()
)
acdTwampGenResultOneWayFeDvCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDvCurrMinValue.setStatus("current")
_AcdTwampGenResultOneWayFeDvCurrMaxValue_Type = Integer32
_AcdTwampGenResultOneWayFeDvCurrMaxValue_Object = MibTableColumn
acdTwampGenResultOneWayFeDvCurrMaxValue = _AcdTwampGenResultOneWayFeDvCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 46),
    _AcdTwampGenResultOneWayFeDvCurrMaxValue_Type()
)
acdTwampGenResultOneWayFeDvCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDvCurrMaxValue.setStatus("current")
_AcdTwampGenResultOneWayFeDvCurrAvgValue_Type = Integer32
_AcdTwampGenResultOneWayFeDvCurrAvgValue_Object = MibTableColumn
acdTwampGenResultOneWayFeDvCurrAvgValue = _AcdTwampGenResultOneWayFeDvCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 47),
    _AcdTwampGenResultOneWayFeDvCurrAvgValue_Type()
)
acdTwampGenResultOneWayFeDvCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDvCurrAvgValue.setStatus("current")
_AcdTwampGenResultOneWayFeDvCurrThreshEx_Type = Unsigned32
_AcdTwampGenResultOneWayFeDvCurrThreshEx_Object = MibTableColumn
acdTwampGenResultOneWayFeDvCurrThreshEx = _AcdTwampGenResultOneWayFeDvCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 48),
    _AcdTwampGenResultOneWayFeDvCurrThreshEx_Type()
)
acdTwampGenResultOneWayFeDvCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultOneWayFeDvCurrThreshEx.setStatus("current")
_AcdTwampGenResultPktLossCurrSamples_Type = Unsigned32
_AcdTwampGenResultPktLossCurrSamples_Object = MibTableColumn
acdTwampGenResultPktLossCurrSamples = _AcdTwampGenResultPktLossCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 49),
    _AcdTwampGenResultPktLossCurrSamples_Type()
)
acdTwampGenResultPktLossCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPktLossCurrSamples.setStatus("current")
_AcdTwampGenResultPktLossCurrLostPackets_Type = Unsigned32
_AcdTwampGenResultPktLossCurrLostPackets_Object = MibTableColumn
acdTwampGenResultPktLossCurrLostPackets = _AcdTwampGenResultPktLossCurrLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 50),
    _AcdTwampGenResultPktLossCurrLostPackets_Type()
)
acdTwampGenResultPktLossCurrLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPktLossCurrLostPackets.setStatus("current")
_AcdTwampGenResultPktLossCurrLossRatio_Type = Unsigned32
_AcdTwampGenResultPktLossCurrLossRatio_Object = MibTableColumn
acdTwampGenResultPktLossCurrLossRatio = _AcdTwampGenResultPktLossCurrLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 51),
    _AcdTwampGenResultPktLossCurrLossRatio_Type()
)
acdTwampGenResultPktLossCurrLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPktLossCurrLossRatio.setStatus("current")
_AcdTwampGenResultPktLossCurrOutOfOrder_Type = Unsigned32
_AcdTwampGenResultPktLossCurrOutOfOrder_Object = MibTableColumn
acdTwampGenResultPktLossCurrOutOfOrder = _AcdTwampGenResultPktLossCurrOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 52),
    _AcdTwampGenResultPktLossCurrOutOfOrder_Type()
)
acdTwampGenResultPktLossCurrOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPktLossCurrOutOfOrder.setStatus("current")
_AcdTwampGenResultPktLossCurrDuplicate_Type = Unsigned32
_AcdTwampGenResultPktLossCurrDuplicate_Object = MibTableColumn
acdTwampGenResultPktLossCurrDuplicate = _AcdTwampGenResultPktLossCurrDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 53),
    _AcdTwampGenResultPktLossCurrDuplicate_Type()
)
acdTwampGenResultPktLossCurrDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPktLossCurrDuplicate.setStatus("current")
_AcdTwampGenResultPktLossCurrGaps_Type = Unsigned32
_AcdTwampGenResultPktLossCurrGaps_Object = MibTableColumn
acdTwampGenResultPktLossCurrGaps = _AcdTwampGenResultPktLossCurrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 54),
    _AcdTwampGenResultPktLossCurrGaps_Type()
)
acdTwampGenResultPktLossCurrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPktLossCurrGaps.setStatus("current")
_AcdTwampGenResultPktLossCurrLargestGap_Type = Unsigned32
_AcdTwampGenResultPktLossCurrLargestGap_Object = MibTableColumn
acdTwampGenResultPktLossCurrLargestGap = _AcdTwampGenResultPktLossCurrLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 1, 1, 55),
    _AcdTwampGenResultPktLossCurrLargestGap_Type()
)
acdTwampGenResultPktLossCurrLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenResultPktLossCurrLargestGap.setStatus("current")
_AcdTwampGenStatusTable_Object = MibTable
acdTwampGenStatusTable = _AcdTwampGenStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2)
)
if mibBuilder.loadTexts:
    acdTwampGenStatusTable.setStatus("current")
_AcdTwampGenStatusEntry_Object = MibTableRow
acdTwampGenStatusEntry = _AcdTwampGenStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1)
)
acdTwampGenStatusEntry.setIndexNames(
    (0, "ACD-TWAMP-GEN-MIB", "acdTwampGenStatusID"),
)
if mibBuilder.loadTexts:
    acdTwampGenStatusEntry.setStatus("current")
_AcdTwampGenStatusID_Type = Unsigned32
_AcdTwampGenStatusID_Object = MibTableColumn
acdTwampGenStatusID = _AcdTwampGenStatusID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 1),
    _AcdTwampGenStatusID_Type()
)
acdTwampGenStatusID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdTwampGenStatusID.setStatus("current")


class _AcdTwampGenStatusInstName_Type(DisplayString):
    """Custom type acdTwampGenStatusInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdTwampGenStatusInstName_Type.__name__ = "DisplayString"
_AcdTwampGenStatusInstName_Object = MibTableColumn
acdTwampGenStatusInstName = _AcdTwampGenStatusInstName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 2),
    _AcdTwampGenStatusInstName_Type()
)
acdTwampGenStatusInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusInstName.setStatus("current")
_AcdTwampGenStatusTwoWayDelayAlert_Type = TruthValue
_AcdTwampGenStatusTwoWayDelayAlert_Object = MibTableColumn
acdTwampGenStatusTwoWayDelayAlert = _AcdTwampGenStatusTwoWayDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 3),
    _AcdTwampGenStatusTwoWayDelayAlert_Type()
)
acdTwampGenStatusTwoWayDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusTwoWayDelayAlert.setStatus("current")
_AcdTwampGenStatusTwoWayAvgDelayAlert_Type = TruthValue
_AcdTwampGenStatusTwoWayAvgDelayAlert_Object = MibTableColumn
acdTwampGenStatusTwoWayAvgDelayAlert = _AcdTwampGenStatusTwoWayAvgDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 4),
    _AcdTwampGenStatusTwoWayAvgDelayAlert_Type()
)
acdTwampGenStatusTwoWayAvgDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusTwoWayAvgDelayAlert.setStatus("current")
_AcdTwampGenStatusTwoWayDvAlert_Type = TruthValue
_AcdTwampGenStatusTwoWayDvAlert_Object = MibTableColumn
acdTwampGenStatusTwoWayDvAlert = _AcdTwampGenStatusTwoWayDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 5),
    _AcdTwampGenStatusTwoWayDvAlert_Type()
)
acdTwampGenStatusTwoWayDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusTwoWayDvAlert.setStatus("current")
_AcdTwampGenStatusTwoWayAvgDvAlert_Type = TruthValue
_AcdTwampGenStatusTwoWayAvgDvAlert_Object = MibTableColumn
acdTwampGenStatusTwoWayAvgDvAlert = _AcdTwampGenStatusTwoWayAvgDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 6),
    _AcdTwampGenStatusTwoWayAvgDvAlert_Type()
)
acdTwampGenStatusTwoWayAvgDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusTwoWayAvgDvAlert.setStatus("current")
_AcdTwampGenStatusOneWayNeDelayAlert_Type = TruthValue
_AcdTwampGenStatusOneWayNeDelayAlert_Object = MibTableColumn
acdTwampGenStatusOneWayNeDelayAlert = _AcdTwampGenStatusOneWayNeDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 7),
    _AcdTwampGenStatusOneWayNeDelayAlert_Type()
)
acdTwampGenStatusOneWayNeDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusOneWayNeDelayAlert.setStatus("current")
_AcdTwampGenStatusOneWayNeAvgDelayAlert_Type = TruthValue
_AcdTwampGenStatusOneWayNeAvgDelayAlert_Object = MibTableColumn
acdTwampGenStatusOneWayNeAvgDelayAlert = _AcdTwampGenStatusOneWayNeAvgDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 8),
    _AcdTwampGenStatusOneWayNeAvgDelayAlert_Type()
)
acdTwampGenStatusOneWayNeAvgDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusOneWayNeAvgDelayAlert.setStatus("current")
_AcdTwampGenStatusOneWayNeDvAlert_Type = TruthValue
_AcdTwampGenStatusOneWayNeDvAlert_Object = MibTableColumn
acdTwampGenStatusOneWayNeDvAlert = _AcdTwampGenStatusOneWayNeDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 9),
    _AcdTwampGenStatusOneWayNeDvAlert_Type()
)
acdTwampGenStatusOneWayNeDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusOneWayNeDvAlert.setStatus("current")
_AcdTwampGenStatusOneWayNeAvgDvAlert_Type = TruthValue
_AcdTwampGenStatusOneWayNeAvgDvAlert_Object = MibTableColumn
acdTwampGenStatusOneWayNeAvgDvAlert = _AcdTwampGenStatusOneWayNeAvgDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 10),
    _AcdTwampGenStatusOneWayNeAvgDvAlert_Type()
)
acdTwampGenStatusOneWayNeAvgDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusOneWayNeAvgDvAlert.setStatus("current")
_AcdTwampGenStatusOneWayFeDelayAlert_Type = TruthValue
_AcdTwampGenStatusOneWayFeDelayAlert_Object = MibTableColumn
acdTwampGenStatusOneWayFeDelayAlert = _AcdTwampGenStatusOneWayFeDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 11),
    _AcdTwampGenStatusOneWayFeDelayAlert_Type()
)
acdTwampGenStatusOneWayFeDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusOneWayFeDelayAlert.setStatus("current")
_AcdTwampGenStatusOneWayFeAvgDelayAlert_Type = TruthValue
_AcdTwampGenStatusOneWayFeAvgDelayAlert_Object = MibTableColumn
acdTwampGenStatusOneWayFeAvgDelayAlert = _AcdTwampGenStatusOneWayFeAvgDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 12),
    _AcdTwampGenStatusOneWayFeAvgDelayAlert_Type()
)
acdTwampGenStatusOneWayFeAvgDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusOneWayFeAvgDelayAlert.setStatus("current")
_AcdTwampGenStatusOneWayFeDvAlert_Type = TruthValue
_AcdTwampGenStatusOneWayFeDvAlert_Object = MibTableColumn
acdTwampGenStatusOneWayFeDvAlert = _AcdTwampGenStatusOneWayFeDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 13),
    _AcdTwampGenStatusOneWayFeDvAlert_Type()
)
acdTwampGenStatusOneWayFeDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusOneWayFeDvAlert.setStatus("current")
_AcdTwampGenStatusOneWayFeAvgDvAlert_Type = TruthValue
_AcdTwampGenStatusOneWayFeAvgDvAlert_Object = MibTableColumn
acdTwampGenStatusOneWayFeAvgDvAlert = _AcdTwampGenStatusOneWayFeAvgDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 14),
    _AcdTwampGenStatusOneWayFeAvgDvAlert_Type()
)
acdTwampGenStatusOneWayFeAvgDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusOneWayFeAvgDvAlert.setStatus("current")
_AcdTwampGenStatusPacketLossContinuityCheckAlert_Type = TruthValue
_AcdTwampGenStatusPacketLossContinuityCheckAlert_Object = MibTableColumn
acdTwampGenStatusPacketLossContinuityCheckAlert = _AcdTwampGenStatusPacketLossContinuityCheckAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 15),
    _AcdTwampGenStatusPacketLossContinuityCheckAlert_Type()
)
acdTwampGenStatusPacketLossContinuityCheckAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusPacketLossContinuityCheckAlert.setStatus("current")
_AcdTwampGenStatusPacketLossExcessivePacketLossAlert_Type = TruthValue
_AcdTwampGenStatusPacketLossExcessivePacketLossAlert_Object = MibTableColumn
acdTwampGenStatusPacketLossExcessivePacketLossAlert = _AcdTwampGenStatusPacketLossExcessivePacketLossAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 2, 1, 16),
    _AcdTwampGenStatusPacketLossExcessivePacketLossAlert_Type()
)
acdTwampGenStatusPacketLossExcessivePacketLossAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenStatusPacketLossExcessivePacketLossAlert.setStatus("current")
_AcdTwampGenCfgTable_Object = MibTable
acdTwampGenCfgTable = _AcdTwampGenCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3)
)
if mibBuilder.loadTexts:
    acdTwampGenCfgTable.setStatus("current")
_AcdTwampGenCfgEntry_Object = MibTableRow
acdTwampGenCfgEntry = _AcdTwampGenCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1)
)
acdTwampGenCfgEntry.setIndexNames(
    (0, "ACD-TWAMP-GEN-MIB", "acdTwampGenCfgID"),
)
if mibBuilder.loadTexts:
    acdTwampGenCfgEntry.setStatus("current")
_AcdTwampGenCfgID_Type = Unsigned32
_AcdTwampGenCfgID_Object = MibTableColumn
acdTwampGenCfgID = _AcdTwampGenCfgID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 1),
    _AcdTwampGenCfgID_Type()
)
acdTwampGenCfgID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdTwampGenCfgID.setStatus("current")


class _AcdTwampGenCfgName_Type(DisplayString):
    """Custom type acdTwampGenCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdTwampGenCfgName_Type.__name__ = "DisplayString"
_AcdTwampGenCfgName_Object = MibTableColumn
acdTwampGenCfgName = _AcdTwampGenCfgName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 2),
    _AcdTwampGenCfgName_Type()
)
acdTwampGenCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgName.setStatus("current")


class _AcdTwampGenCfgState_Type(Integer32):
    """Custom type acdTwampGenCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_AcdTwampGenCfgState_Type.__name__ = "Integer32"
_AcdTwampGenCfgState_Object = MibTableColumn
acdTwampGenCfgState = _AcdTwampGenCfgState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 3),
    _AcdTwampGenCfgState_Type()
)
acdTwampGenCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgState.setStatus("current")
_AcdTwampGenCfgInterval_Type = Unsigned32
_AcdTwampGenCfgInterval_Object = MibTableColumn
acdTwampGenCfgInterval = _AcdTwampGenCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 4),
    _AcdTwampGenCfgInterval_Type()
)
acdTwampGenCfgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgInterval.setStatus("current")
_AcdTwampGenCfgReferencePeriod_Type = Unsigned32
_AcdTwampGenCfgReferencePeriod_Object = MibTableColumn
acdTwampGenCfgReferencePeriod = _AcdTwampGenCfgReferencePeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 5),
    _AcdTwampGenCfgReferencePeriod_Type()
)
acdTwampGenCfgReferencePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgReferencePeriod.setStatus("current")
_AcdTwampGenCfgPktSize_Type = Unsigned32
_AcdTwampGenCfgPktSize_Object = MibTableColumn
acdTwampGenCfgPktSize = _AcdTwampGenCfgPktSize_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 6),
    _AcdTwampGenCfgPktSize_Type()
)
acdTwampGenCfgPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgPktSize.setStatus("current")
_AcdTwampGenCfgDestIPv4Addr_Type = IpAddress
_AcdTwampGenCfgDestIPv4Addr_Object = MibTableColumn
acdTwampGenCfgDestIPv4Addr = _AcdTwampGenCfgDestIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 7),
    _AcdTwampGenCfgDestIPv4Addr_Type()
)
acdTwampGenCfgDestIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgDestIPv4Addr.setStatus("current")
_AcdTwampGenCfgSourcePortNumber_Type = Unsigned32
_AcdTwampGenCfgSourcePortNumber_Object = MibTableColumn
acdTwampGenCfgSourcePortNumber = _AcdTwampGenCfgSourcePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 8),
    _AcdTwampGenCfgSourcePortNumber_Type()
)
acdTwampGenCfgSourcePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgSourcePortNumber.setStatus("current")
_AcdTwampGenCfgDestPortNumber_Type = Unsigned32
_AcdTwampGenCfgDestPortNumber_Object = MibTableColumn
acdTwampGenCfgDestPortNumber = _AcdTwampGenCfgDestPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 9),
    _AcdTwampGenCfgDestPortNumber_Type()
)
acdTwampGenCfgDestPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgDestPortNumber.setStatus("current")
_AcdTwampGenCfgDscp_Type = Unsigned32
_AcdTwampGenCfgDscp_Object = MibTableColumn
acdTwampGenCfgDscp = _AcdTwampGenCfgDscp_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 10),
    _AcdTwampGenCfgDscp_Type()
)
acdTwampGenCfgDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgDscp.setStatus("current")
_AcdTwampGenCfgEcn_Type = Unsigned32
_AcdTwampGenCfgEcn_Object = MibTableColumn
acdTwampGenCfgEcn = _AcdTwampGenCfgEcn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 11),
    _AcdTwampGenCfgEcn_Type()
)
acdTwampGenCfgEcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgEcn.setStatus("current")
_AcdTwampGenCfgVlan1Priority_Type = Unsigned32
_AcdTwampGenCfgVlan1Priority_Object = MibTableColumn
acdTwampGenCfgVlan1Priority = _AcdTwampGenCfgVlan1Priority_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 12),
    _AcdTwampGenCfgVlan1Priority_Type()
)
acdTwampGenCfgVlan1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgVlan1Priority.setStatus("current")
_AcdTwampGenCfgTwoWayMaxDelay_Type = Unsigned32
_AcdTwampGenCfgTwoWayMaxDelay_Object = MibTableColumn
acdTwampGenCfgTwoWayMaxDelay = _AcdTwampGenCfgTwoWayMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 13),
    _AcdTwampGenCfgTwoWayMaxDelay_Type()
)
acdTwampGenCfgTwoWayMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgTwoWayMaxDelay.setStatus("current")
_AcdTwampGenCfgTwoWayMaxDelayThrs_Type = Unsigned32
_AcdTwampGenCfgTwoWayMaxDelayThrs_Object = MibTableColumn
acdTwampGenCfgTwoWayMaxDelayThrs = _AcdTwampGenCfgTwoWayMaxDelayThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 14),
    _AcdTwampGenCfgTwoWayMaxDelayThrs_Type()
)
acdTwampGenCfgTwoWayMaxDelayThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgTwoWayMaxDelayThrs.setStatus("current")
_AcdTwampGenCfgTwoWayAvgDelayThrs_Type = Unsigned32
_AcdTwampGenCfgTwoWayAvgDelayThrs_Object = MibTableColumn
acdTwampGenCfgTwoWayAvgDelayThrs = _AcdTwampGenCfgTwoWayAvgDelayThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 15),
    _AcdTwampGenCfgTwoWayAvgDelayThrs_Type()
)
acdTwampGenCfgTwoWayAvgDelayThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgTwoWayAvgDelayThrs.setStatus("current")
_AcdTwampGenCfgTwoWayMaxDv_Type = Unsigned32
_AcdTwampGenCfgTwoWayMaxDv_Object = MibTableColumn
acdTwampGenCfgTwoWayMaxDv = _AcdTwampGenCfgTwoWayMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 16),
    _AcdTwampGenCfgTwoWayMaxDv_Type()
)
acdTwampGenCfgTwoWayMaxDv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgTwoWayMaxDv.setStatus("current")
_AcdTwampGenCfgTwoWayMaxDvThrs_Type = Unsigned32
_AcdTwampGenCfgTwoWayMaxDvThrs_Object = MibTableColumn
acdTwampGenCfgTwoWayMaxDvThrs = _AcdTwampGenCfgTwoWayMaxDvThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 17),
    _AcdTwampGenCfgTwoWayMaxDvThrs_Type()
)
acdTwampGenCfgTwoWayMaxDvThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgTwoWayMaxDvThrs.setStatus("current")
_AcdTwampGenCfgTwoWayAvgDvThrs_Type = Unsigned32
_AcdTwampGenCfgTwoWayAvgDvThrs_Object = MibTableColumn
acdTwampGenCfgTwoWayAvgDvThrs = _AcdTwampGenCfgTwoWayAvgDvThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 18),
    _AcdTwampGenCfgTwoWayAvgDvThrs_Type()
)
acdTwampGenCfgTwoWayAvgDvThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgTwoWayAvgDvThrs.setStatus("current")
_AcdTwampGenCfgOneWayNearEndMaxDelay_Type = Unsigned32
_AcdTwampGenCfgOneWayNearEndMaxDelay_Object = MibTableColumn
acdTwampGenCfgOneWayNearEndMaxDelay = _AcdTwampGenCfgOneWayNearEndMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 19),
    _AcdTwampGenCfgOneWayNearEndMaxDelay_Type()
)
acdTwampGenCfgOneWayNearEndMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayNearEndMaxDelay.setStatus("current")
_AcdTwampGenCfgOneWayNearEndMaxDelayThrs_Type = Unsigned32
_AcdTwampGenCfgOneWayNearEndMaxDelayThrs_Object = MibTableColumn
acdTwampGenCfgOneWayNearEndMaxDelayThrs = _AcdTwampGenCfgOneWayNearEndMaxDelayThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 20),
    _AcdTwampGenCfgOneWayNearEndMaxDelayThrs_Type()
)
acdTwampGenCfgOneWayNearEndMaxDelayThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayNearEndMaxDelayThrs.setStatus("current")
_AcdTwampGenCfgOneWayNearEndAvgDelayThrs_Type = Unsigned32
_AcdTwampGenCfgOneWayNearEndAvgDelayThrs_Object = MibTableColumn
acdTwampGenCfgOneWayNearEndAvgDelayThrs = _AcdTwampGenCfgOneWayNearEndAvgDelayThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 21),
    _AcdTwampGenCfgOneWayNearEndAvgDelayThrs_Type()
)
acdTwampGenCfgOneWayNearEndAvgDelayThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayNearEndAvgDelayThrs.setStatus("current")
_AcdTwampGenCfgOneWayNearEndMaxDv_Type = Unsigned32
_AcdTwampGenCfgOneWayNearEndMaxDv_Object = MibTableColumn
acdTwampGenCfgOneWayNearEndMaxDv = _AcdTwampGenCfgOneWayNearEndMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 22),
    _AcdTwampGenCfgOneWayNearEndMaxDv_Type()
)
acdTwampGenCfgOneWayNearEndMaxDv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayNearEndMaxDv.setStatus("current")
_AcdTwampGenCfgOneWayNearEndMaxDvThrs_Type = Unsigned32
_AcdTwampGenCfgOneWayNearEndMaxDvThrs_Object = MibTableColumn
acdTwampGenCfgOneWayNearEndMaxDvThrs = _AcdTwampGenCfgOneWayNearEndMaxDvThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 23),
    _AcdTwampGenCfgOneWayNearEndMaxDvThrs_Type()
)
acdTwampGenCfgOneWayNearEndMaxDvThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayNearEndMaxDvThrs.setStatus("current")
_AcdTwampGenCfgOneWayNearEndAvgDvThrs_Type = Unsigned32
_AcdTwampGenCfgOneWayNearEndAvgDvThrs_Object = MibTableColumn
acdTwampGenCfgOneWayNearEndAvgDvThrs = _AcdTwampGenCfgOneWayNearEndAvgDvThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 24),
    _AcdTwampGenCfgOneWayNearEndAvgDvThrs_Type()
)
acdTwampGenCfgOneWayNearEndAvgDvThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayNearEndAvgDvThrs.setStatus("current")
_AcdTwampGenCfgOneWayFarEndMaxDelay_Type = Unsigned32
_AcdTwampGenCfgOneWayFarEndMaxDelay_Object = MibTableColumn
acdTwampGenCfgOneWayFarEndMaxDelay = _AcdTwampGenCfgOneWayFarEndMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 25),
    _AcdTwampGenCfgOneWayFarEndMaxDelay_Type()
)
acdTwampGenCfgOneWayFarEndMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayFarEndMaxDelay.setStatus("current")
_AcdTwampGenCfgOneWayFarEndMaxDelayThrs_Type = Unsigned32
_AcdTwampGenCfgOneWayFarEndMaxDelayThrs_Object = MibTableColumn
acdTwampGenCfgOneWayFarEndMaxDelayThrs = _AcdTwampGenCfgOneWayFarEndMaxDelayThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 26),
    _AcdTwampGenCfgOneWayFarEndMaxDelayThrs_Type()
)
acdTwampGenCfgOneWayFarEndMaxDelayThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayFarEndMaxDelayThrs.setStatus("current")
_AcdTwampGenCfgOneWayFarEndAvgDelayThrs_Type = Unsigned32
_AcdTwampGenCfgOneWayFarEndAvgDelayThrs_Object = MibTableColumn
acdTwampGenCfgOneWayFarEndAvgDelayThrs = _AcdTwampGenCfgOneWayFarEndAvgDelayThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 27),
    _AcdTwampGenCfgOneWayFarEndAvgDelayThrs_Type()
)
acdTwampGenCfgOneWayFarEndAvgDelayThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayFarEndAvgDelayThrs.setStatus("current")
_AcdTwampGenCfgOneWayFarEndMaxDv_Type = Unsigned32
_AcdTwampGenCfgOneWayFarEndMaxDv_Object = MibTableColumn
acdTwampGenCfgOneWayFarEndMaxDv = _AcdTwampGenCfgOneWayFarEndMaxDv_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 28),
    _AcdTwampGenCfgOneWayFarEndMaxDv_Type()
)
acdTwampGenCfgOneWayFarEndMaxDv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayFarEndMaxDv.setStatus("current")
_AcdTwampGenCfgOneWayFarEndMaxDvThrs_Type = Unsigned32
_AcdTwampGenCfgOneWayFarEndMaxDvThrs_Object = MibTableColumn
acdTwampGenCfgOneWayFarEndMaxDvThrs = _AcdTwampGenCfgOneWayFarEndMaxDvThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 29),
    _AcdTwampGenCfgOneWayFarEndMaxDvThrs_Type()
)
acdTwampGenCfgOneWayFarEndMaxDvThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayFarEndMaxDvThrs.setStatus("current")
_AcdTwampGenCfgOneWayFarEndAvgDvThrs_Type = Unsigned32
_AcdTwampGenCfgOneWayFarEndAvgDvThrs_Object = MibTableColumn
acdTwampGenCfgOneWayFarEndAvgDvThrs = _AcdTwampGenCfgOneWayFarEndAvgDvThrs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 30),
    _AcdTwampGenCfgOneWayFarEndAvgDvThrs_Type()
)
acdTwampGenCfgOneWayFarEndAvgDvThrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgOneWayFarEndAvgDvThrs.setStatus("current")
_AcdTwampGenCfgPacketLossContinuityCheck_Type = Unsigned32
_AcdTwampGenCfgPacketLossContinuityCheck_Object = MibTableColumn
acdTwampGenCfgPacketLossContinuityCheck = _AcdTwampGenCfgPacketLossContinuityCheck_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 31),
    _AcdTwampGenCfgPacketLossContinuityCheck_Type()
)
acdTwampGenCfgPacketLossContinuityCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgPacketLossContinuityCheck.setStatus("current")
_AcdTwampGenCfgPacketLossRate_Type = Unsigned32
_AcdTwampGenCfgPacketLossRate_Object = MibTableColumn
acdTwampGenCfgPacketLossRate = _AcdTwampGenCfgPacketLossRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 3, 1, 32),
    _AcdTwampGenCfgPacketLossRate_Type()
)
acdTwampGenCfgPacketLossRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdTwampGenCfgPacketLossRate.setStatus("current")
_AcdTwampGenHistResultTable_Object = MibTable
acdTwampGenHistResultTable = _AcdTwampGenHistResultTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4)
)
if mibBuilder.loadTexts:
    acdTwampGenHistResultTable.setStatus("current")
_AcdTwampGenHistResultEntry_Object = MibTableRow
acdTwampGenHistResultEntry = _AcdTwampGenHistResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1)
)
acdTwampGenHistResultEntry.setIndexNames(
    (0, "ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultID"),
    (0, "ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultSampleIndex"),
)
if mibBuilder.loadTexts:
    acdTwampGenHistResultEntry.setStatus("current")
_AcdTwampGenHistResultID_Type = Unsigned32
_AcdTwampGenHistResultID_Object = MibTableColumn
acdTwampGenHistResultID = _AcdTwampGenHistResultID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 1),
    _AcdTwampGenHistResultID_Type()
)
acdTwampGenHistResultID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultID.setStatus("current")
_AcdTwampGenHistResultSampleIndex_Type = Unsigned32
_AcdTwampGenHistResultSampleIndex_Object = MibTableColumn
acdTwampGenHistResultSampleIndex = _AcdTwampGenHistResultSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 2),
    _AcdTwampGenHistResultSampleIndex_Type()
)
acdTwampGenHistResultSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultSampleIndex.setStatus("current")


class _AcdTwampGenHistResultInstName_Type(DisplayString):
    """Custom type acdTwampGenHistResultInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdTwampGenHistResultInstName_Type.__name__ = "DisplayString"
_AcdTwampGenHistResultInstName_Object = MibTableColumn
acdTwampGenHistResultInstName = _AcdTwampGenHistResultInstName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 3),
    _AcdTwampGenHistResultInstName_Type()
)
acdTwampGenHistResultInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultInstName.setStatus("current")
_AcdTwampGenHistResultPeriodTime_Type = DateAndTime
_AcdTwampGenHistResultPeriodTime_Object = MibTableColumn
acdTwampGenHistResultPeriodTime = _AcdTwampGenHistResultPeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 4),
    _AcdTwampGenHistResultPeriodTime_Type()
)
acdTwampGenHistResultPeriodTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultPeriodTime.setStatus("current")
_AcdTwampGenHistResultTxPacketCount_Type = Counter64
_AcdTwampGenHistResultTxPacketCount_Object = MibTableColumn
acdTwampGenHistResultTxPacketCount = _AcdTwampGenHistResultTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 5),
    _AcdTwampGenHistResultTxPacketCount_Type()
)
acdTwampGenHistResultTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTxPacketCount.setStatus("current")
_AcdTwampGenHistResultRxPacketCount_Type = Counter64
_AcdTwampGenHistResultRxPacketCount_Object = MibTableColumn
acdTwampGenHistResultRxPacketCount = _AcdTwampGenHistResultRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 6),
    _AcdTwampGenHistResultRxPacketCount_Type()
)
acdTwampGenHistResultRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultRxPacketCount.setStatus("current")
_AcdTwampGenHistResultTwoWayDelayValid_Type = TruthValue
_AcdTwampGenHistResultTwoWayDelayValid_Object = MibTableColumn
acdTwampGenHistResultTwoWayDelayValid = _AcdTwampGenHistResultTwoWayDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 7),
    _AcdTwampGenHistResultTwoWayDelayValid_Type()
)
acdTwampGenHistResultTwoWayDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDelayValid.setStatus("current")
_AcdTwampGenHistResultTwoWayDelayInstValue_Type = Integer32
_AcdTwampGenHistResultTwoWayDelayInstValue_Object = MibTableColumn
acdTwampGenHistResultTwoWayDelayInstValue = _AcdTwampGenHistResultTwoWayDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 8),
    _AcdTwampGenHistResultTwoWayDelayInstValue_Type()
)
acdTwampGenHistResultTwoWayDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDelayInstValue.setStatus("current")
_AcdTwampGenHistResultTwoWayDelaySamples_Type = Unsigned32
_AcdTwampGenHistResultTwoWayDelaySamples_Object = MibTableColumn
acdTwampGenHistResultTwoWayDelaySamples = _AcdTwampGenHistResultTwoWayDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 9),
    _AcdTwampGenHistResultTwoWayDelaySamples_Type()
)
acdTwampGenHistResultTwoWayDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDelaySamples.setStatus("current")
_AcdTwampGenHistResultTwoWayDelayMinValue_Type = Integer32
_AcdTwampGenHistResultTwoWayDelayMinValue_Object = MibTableColumn
acdTwampGenHistResultTwoWayDelayMinValue = _AcdTwampGenHistResultTwoWayDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 10),
    _AcdTwampGenHistResultTwoWayDelayMinValue_Type()
)
acdTwampGenHistResultTwoWayDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDelayMinValue.setStatus("current")
_AcdTwampGenHistResultTwoWayDelayMaxValue_Type = Integer32
_AcdTwampGenHistResultTwoWayDelayMaxValue_Object = MibTableColumn
acdTwampGenHistResultTwoWayDelayMaxValue = _AcdTwampGenHistResultTwoWayDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 11),
    _AcdTwampGenHistResultTwoWayDelayMaxValue_Type()
)
acdTwampGenHistResultTwoWayDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDelayMaxValue.setStatus("current")
_AcdTwampGenHistResultTwoWayDelayAvgValue_Type = Integer32
_AcdTwampGenHistResultTwoWayDelayAvgValue_Object = MibTableColumn
acdTwampGenHistResultTwoWayDelayAvgValue = _AcdTwampGenHistResultTwoWayDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 12),
    _AcdTwampGenHistResultTwoWayDelayAvgValue_Type()
)
acdTwampGenHistResultTwoWayDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDelayAvgValue.setStatus("current")
_AcdTwampGenHistResultTwoWayDelayThreshEx_Type = Unsigned32
_AcdTwampGenHistResultTwoWayDelayThreshEx_Object = MibTableColumn
acdTwampGenHistResultTwoWayDelayThreshEx = _AcdTwampGenHistResultTwoWayDelayThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 13),
    _AcdTwampGenHistResultTwoWayDelayThreshEx_Type()
)
acdTwampGenHistResultTwoWayDelayThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDelayThreshEx.setStatus("current")
_AcdTwampGenHistResultTwoWayDvValid_Type = TruthValue
_AcdTwampGenHistResultTwoWayDvValid_Object = MibTableColumn
acdTwampGenHistResultTwoWayDvValid = _AcdTwampGenHistResultTwoWayDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 14),
    _AcdTwampGenHistResultTwoWayDvValid_Type()
)
acdTwampGenHistResultTwoWayDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDvValid.setStatus("current")
_AcdTwampGenHistResultTwoWayDvInstValue_Type = Integer32
_AcdTwampGenHistResultTwoWayDvInstValue_Object = MibTableColumn
acdTwampGenHistResultTwoWayDvInstValue = _AcdTwampGenHistResultTwoWayDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 15),
    _AcdTwampGenHistResultTwoWayDvInstValue_Type()
)
acdTwampGenHistResultTwoWayDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDvInstValue.setStatus("current")
_AcdTwampGenHistResultTwoWayDvSamples_Type = Unsigned32
_AcdTwampGenHistResultTwoWayDvSamples_Object = MibTableColumn
acdTwampGenHistResultTwoWayDvSamples = _AcdTwampGenHistResultTwoWayDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 16),
    _AcdTwampGenHistResultTwoWayDvSamples_Type()
)
acdTwampGenHistResultTwoWayDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDvSamples.setStatus("current")
_AcdTwampGenHistResultTwoWayDvMinValue_Type = Integer32
_AcdTwampGenHistResultTwoWayDvMinValue_Object = MibTableColumn
acdTwampGenHistResultTwoWayDvMinValue = _AcdTwampGenHistResultTwoWayDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 17),
    _AcdTwampGenHistResultTwoWayDvMinValue_Type()
)
acdTwampGenHistResultTwoWayDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDvMinValue.setStatus("current")
_AcdTwampGenHistResultTwoWayDvMaxValue_Type = Integer32
_AcdTwampGenHistResultTwoWayDvMaxValue_Object = MibTableColumn
acdTwampGenHistResultTwoWayDvMaxValue = _AcdTwampGenHistResultTwoWayDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 18),
    _AcdTwampGenHistResultTwoWayDvMaxValue_Type()
)
acdTwampGenHistResultTwoWayDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDvMaxValue.setStatus("current")
_AcdTwampGenHistResultTwoWayDvAvgValue_Type = Integer32
_AcdTwampGenHistResultTwoWayDvAvgValue_Object = MibTableColumn
acdTwampGenHistResultTwoWayDvAvgValue = _AcdTwampGenHistResultTwoWayDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 19),
    _AcdTwampGenHistResultTwoWayDvAvgValue_Type()
)
acdTwampGenHistResultTwoWayDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDvAvgValue.setStatus("current")
_AcdTwampGenHistResultTwoWayDvThreshEx_Type = Unsigned32
_AcdTwampGenHistResultTwoWayDvThreshEx_Object = MibTableColumn
acdTwampGenHistResultTwoWayDvThreshEx = _AcdTwampGenHistResultTwoWayDvThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 20),
    _AcdTwampGenHistResultTwoWayDvThreshEx_Type()
)
acdTwampGenHistResultTwoWayDvThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultTwoWayDvThreshEx.setStatus("current")
_AcdTwampGenHistResultOneWayNeDelayValid_Type = TruthValue
_AcdTwampGenHistResultOneWayNeDelayValid_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDelayValid = _AcdTwampGenHistResultOneWayNeDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 21),
    _AcdTwampGenHistResultOneWayNeDelayValid_Type()
)
acdTwampGenHistResultOneWayNeDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDelayValid.setStatus("current")
_AcdTwampGenHistResultOneWayNeDelayInstValue_Type = Integer32
_AcdTwampGenHistResultOneWayNeDelayInstValue_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDelayInstValue = _AcdTwampGenHistResultOneWayNeDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 22),
    _AcdTwampGenHistResultOneWayNeDelayInstValue_Type()
)
acdTwampGenHistResultOneWayNeDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDelayInstValue.setStatus("current")
_AcdTwampGenHistResultOneWayNeDelaySamples_Type = Unsigned32
_AcdTwampGenHistResultOneWayNeDelaySamples_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDelaySamples = _AcdTwampGenHistResultOneWayNeDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 23),
    _AcdTwampGenHistResultOneWayNeDelaySamples_Type()
)
acdTwampGenHistResultOneWayNeDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDelaySamples.setStatus("current")
_AcdTwampGenHistResultOneWayNeDelayMinValue_Type = Integer32
_AcdTwampGenHistResultOneWayNeDelayMinValue_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDelayMinValue = _AcdTwampGenHistResultOneWayNeDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 24),
    _AcdTwampGenHistResultOneWayNeDelayMinValue_Type()
)
acdTwampGenHistResultOneWayNeDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDelayMinValue.setStatus("current")
_AcdTwampGenHistResultOneWayNeDelayMaxValue_Type = Integer32
_AcdTwampGenHistResultOneWayNeDelayMaxValue_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDelayMaxValue = _AcdTwampGenHistResultOneWayNeDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 25),
    _AcdTwampGenHistResultOneWayNeDelayMaxValue_Type()
)
acdTwampGenHistResultOneWayNeDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDelayMaxValue.setStatus("current")
_AcdTwampGenHistResultOneWayNeDelayAvgValue_Type = Integer32
_AcdTwampGenHistResultOneWayNeDelayAvgValue_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDelayAvgValue = _AcdTwampGenHistResultOneWayNeDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 26),
    _AcdTwampGenHistResultOneWayNeDelayAvgValue_Type()
)
acdTwampGenHistResultOneWayNeDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDelayAvgValue.setStatus("current")
_AcdTwampGenHistResultOneWayNeDelayThreshEx_Type = Unsigned32
_AcdTwampGenHistResultOneWayNeDelayThreshEx_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDelayThreshEx = _AcdTwampGenHistResultOneWayNeDelayThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 27),
    _AcdTwampGenHistResultOneWayNeDelayThreshEx_Type()
)
acdTwampGenHistResultOneWayNeDelayThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDelayThreshEx.setStatus("current")
_AcdTwampGenHistResultOneWayNeDvValid_Type = TruthValue
_AcdTwampGenHistResultOneWayNeDvValid_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDvValid = _AcdTwampGenHistResultOneWayNeDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 28),
    _AcdTwampGenHistResultOneWayNeDvValid_Type()
)
acdTwampGenHistResultOneWayNeDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDvValid.setStatus("current")
_AcdTwampGenHistResultOneWayNeDvInstValue_Type = Integer32
_AcdTwampGenHistResultOneWayNeDvInstValue_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDvInstValue = _AcdTwampGenHistResultOneWayNeDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 29),
    _AcdTwampGenHistResultOneWayNeDvInstValue_Type()
)
acdTwampGenHistResultOneWayNeDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDvInstValue.setStatus("current")
_AcdTwampGenHistResultOneWayNeDvSamples_Type = Unsigned32
_AcdTwampGenHistResultOneWayNeDvSamples_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDvSamples = _AcdTwampGenHistResultOneWayNeDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 30),
    _AcdTwampGenHistResultOneWayNeDvSamples_Type()
)
acdTwampGenHistResultOneWayNeDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDvSamples.setStatus("current")
_AcdTwampGenHistResultOneWayNeDvMinValue_Type = Integer32
_AcdTwampGenHistResultOneWayNeDvMinValue_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDvMinValue = _AcdTwampGenHistResultOneWayNeDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 31),
    _AcdTwampGenHistResultOneWayNeDvMinValue_Type()
)
acdTwampGenHistResultOneWayNeDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDvMinValue.setStatus("current")
_AcdTwampGenHistResultOneWayNeDvMaxValue_Type = Integer32
_AcdTwampGenHistResultOneWayNeDvMaxValue_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDvMaxValue = _AcdTwampGenHistResultOneWayNeDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 32),
    _AcdTwampGenHistResultOneWayNeDvMaxValue_Type()
)
acdTwampGenHistResultOneWayNeDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDvMaxValue.setStatus("current")
_AcdTwampGenHistResultOneWayNeDvAvgValue_Type = Integer32
_AcdTwampGenHistResultOneWayNeDvAvgValue_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDvAvgValue = _AcdTwampGenHistResultOneWayNeDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 33),
    _AcdTwampGenHistResultOneWayNeDvAvgValue_Type()
)
acdTwampGenHistResultOneWayNeDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDvAvgValue.setStatus("current")
_AcdTwampGenHistResultOneWayNeDvThreshEx_Type = Unsigned32
_AcdTwampGenHistResultOneWayNeDvThreshEx_Object = MibTableColumn
acdTwampGenHistResultOneWayNeDvThreshEx = _AcdTwampGenHistResultOneWayNeDvThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 34),
    _AcdTwampGenHistResultOneWayNeDvThreshEx_Type()
)
acdTwampGenHistResultOneWayNeDvThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayNeDvThreshEx.setStatus("current")
_AcdTwampGenHistResultOneWayFeDelayValid_Type = TruthValue
_AcdTwampGenHistResultOneWayFeDelayValid_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDelayValid = _AcdTwampGenHistResultOneWayFeDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 35),
    _AcdTwampGenHistResultOneWayFeDelayValid_Type()
)
acdTwampGenHistResultOneWayFeDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDelayValid.setStatus("current")
_AcdTwampGenHistResultOneWayFeDelayInstValue_Type = Integer32
_AcdTwampGenHistResultOneWayFeDelayInstValue_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDelayInstValue = _AcdTwampGenHistResultOneWayFeDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 36),
    _AcdTwampGenHistResultOneWayFeDelayInstValue_Type()
)
acdTwampGenHistResultOneWayFeDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDelayInstValue.setStatus("current")
_AcdTwampGenHistResultOneWayFeDelaySamples_Type = Unsigned32
_AcdTwampGenHistResultOneWayFeDelaySamples_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDelaySamples = _AcdTwampGenHistResultOneWayFeDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 37),
    _AcdTwampGenHistResultOneWayFeDelaySamples_Type()
)
acdTwampGenHistResultOneWayFeDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDelaySamples.setStatus("current")
_AcdTwampGenHistResultOneWayFeDelayMinValue_Type = Integer32
_AcdTwampGenHistResultOneWayFeDelayMinValue_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDelayMinValue = _AcdTwampGenHistResultOneWayFeDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 38),
    _AcdTwampGenHistResultOneWayFeDelayMinValue_Type()
)
acdTwampGenHistResultOneWayFeDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDelayMinValue.setStatus("current")
_AcdTwampGenHistResultOneWayFeDelayMaxValue_Type = Integer32
_AcdTwampGenHistResultOneWayFeDelayMaxValue_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDelayMaxValue = _AcdTwampGenHistResultOneWayFeDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 39),
    _AcdTwampGenHistResultOneWayFeDelayMaxValue_Type()
)
acdTwampGenHistResultOneWayFeDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDelayMaxValue.setStatus("current")
_AcdTwampGenHistResultOneWayFeDelayAvgValue_Type = Integer32
_AcdTwampGenHistResultOneWayFeDelayAvgValue_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDelayAvgValue = _AcdTwampGenHistResultOneWayFeDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 40),
    _AcdTwampGenHistResultOneWayFeDelayAvgValue_Type()
)
acdTwampGenHistResultOneWayFeDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDelayAvgValue.setStatus("current")
_AcdTwampGenHistResultOneWayFeDelayThreshEx_Type = Unsigned32
_AcdTwampGenHistResultOneWayFeDelayThreshEx_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDelayThreshEx = _AcdTwampGenHistResultOneWayFeDelayThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 41),
    _AcdTwampGenHistResultOneWayFeDelayThreshEx_Type()
)
acdTwampGenHistResultOneWayFeDelayThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDelayThreshEx.setStatus("current")
_AcdTwampGenHistResultOneWayFeDvValid_Type = TruthValue
_AcdTwampGenHistResultOneWayFeDvValid_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDvValid = _AcdTwampGenHistResultOneWayFeDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 42),
    _AcdTwampGenHistResultOneWayFeDvValid_Type()
)
acdTwampGenHistResultOneWayFeDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDvValid.setStatus("current")
_AcdTwampGenHistResultOneWayFeDvInstValue_Type = Integer32
_AcdTwampGenHistResultOneWayFeDvInstValue_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDvInstValue = _AcdTwampGenHistResultOneWayFeDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 43),
    _AcdTwampGenHistResultOneWayFeDvInstValue_Type()
)
acdTwampGenHistResultOneWayFeDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDvInstValue.setStatus("current")
_AcdTwampGenHistResultOneWayFeDvSamples_Type = Unsigned32
_AcdTwampGenHistResultOneWayFeDvSamples_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDvSamples = _AcdTwampGenHistResultOneWayFeDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 44),
    _AcdTwampGenHistResultOneWayFeDvSamples_Type()
)
acdTwampGenHistResultOneWayFeDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDvSamples.setStatus("current")
_AcdTwampGenHistResultOneWayFeDvMinValue_Type = Integer32
_AcdTwampGenHistResultOneWayFeDvMinValue_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDvMinValue = _AcdTwampGenHistResultOneWayFeDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 45),
    _AcdTwampGenHistResultOneWayFeDvMinValue_Type()
)
acdTwampGenHistResultOneWayFeDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDvMinValue.setStatus("current")
_AcdTwampGenHistResultOneWayFeDvMaxValue_Type = Integer32
_AcdTwampGenHistResultOneWayFeDvMaxValue_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDvMaxValue = _AcdTwampGenHistResultOneWayFeDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 46),
    _AcdTwampGenHistResultOneWayFeDvMaxValue_Type()
)
acdTwampGenHistResultOneWayFeDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDvMaxValue.setStatus("current")
_AcdTwampGenHistResultOneWayFeDvAvgValue_Type = Integer32
_AcdTwampGenHistResultOneWayFeDvAvgValue_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDvAvgValue = _AcdTwampGenHistResultOneWayFeDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 47),
    _AcdTwampGenHistResultOneWayFeDvAvgValue_Type()
)
acdTwampGenHistResultOneWayFeDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDvAvgValue.setStatus("current")
_AcdTwampGenHistResultOneWayFeDvThreshEx_Type = Unsigned32
_AcdTwampGenHistResultOneWayFeDvThreshEx_Object = MibTableColumn
acdTwampGenHistResultOneWayFeDvThreshEx = _AcdTwampGenHistResultOneWayFeDvThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 48),
    _AcdTwampGenHistResultOneWayFeDvThreshEx_Type()
)
acdTwampGenHistResultOneWayFeDvThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultOneWayFeDvThreshEx.setStatus("current")
_AcdTwampGenHistResultPktLossSamples_Type = Unsigned32
_AcdTwampGenHistResultPktLossSamples_Object = MibTableColumn
acdTwampGenHistResultPktLossSamples = _AcdTwampGenHistResultPktLossSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 49),
    _AcdTwampGenHistResultPktLossSamples_Type()
)
acdTwampGenHistResultPktLossSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultPktLossSamples.setStatus("current")
_AcdTwampGenHistResultPktLossLostPackets_Type = Unsigned32
_AcdTwampGenHistResultPktLossLostPackets_Object = MibTableColumn
acdTwampGenHistResultPktLossLostPackets = _AcdTwampGenHistResultPktLossLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 50),
    _AcdTwampGenHistResultPktLossLostPackets_Type()
)
acdTwampGenHistResultPktLossLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultPktLossLostPackets.setStatus("current")
_AcdTwampGenHistResultPktLossLossRatio_Type = Unsigned32
_AcdTwampGenHistResultPktLossLossRatio_Object = MibTableColumn
acdTwampGenHistResultPktLossLossRatio = _AcdTwampGenHistResultPktLossLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 51),
    _AcdTwampGenHistResultPktLossLossRatio_Type()
)
acdTwampGenHistResultPktLossLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultPktLossLossRatio.setStatus("current")
_AcdTwampGenHistResultPktLossOutOfOrder_Type = Unsigned32
_AcdTwampGenHistResultPktLossOutOfOrder_Object = MibTableColumn
acdTwampGenHistResultPktLossOutOfOrder = _AcdTwampGenHistResultPktLossOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 52),
    _AcdTwampGenHistResultPktLossOutOfOrder_Type()
)
acdTwampGenHistResultPktLossOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultPktLossOutOfOrder.setStatus("current")
_AcdTwampGenHistResultPktLossDuplicate_Type = Unsigned32
_AcdTwampGenHistResultPktLossDuplicate_Object = MibTableColumn
acdTwampGenHistResultPktLossDuplicate = _AcdTwampGenHistResultPktLossDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 53),
    _AcdTwampGenHistResultPktLossDuplicate_Type()
)
acdTwampGenHistResultPktLossDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultPktLossDuplicate.setStatus("current")
_AcdTwampGenHistResultPktLossGaps_Type = Unsigned32
_AcdTwampGenHistResultPktLossGaps_Object = MibTableColumn
acdTwampGenHistResultPktLossGaps = _AcdTwampGenHistResultPktLossGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 54),
    _AcdTwampGenHistResultPktLossGaps_Type()
)
acdTwampGenHistResultPktLossGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultPktLossGaps.setStatus("current")
_AcdTwampGenHistResultPktLossLargestGap_Type = Unsigned32
_AcdTwampGenHistResultPktLossLargestGap_Object = MibTableColumn
acdTwampGenHistResultPktLossLargestGap = _AcdTwampGenHistResultPktLossLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 4, 1, 55),
    _AcdTwampGenHistResultPktLossLargestGap_Type()
)
acdTwampGenHistResultPktLossLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTwampGenHistResultPktLossLargestGap.setStatus("current")
_AcdTwampGenNotifications_ObjectIdentity = ObjectIdentity
acdTwampGenNotifications = _AcdTwampGenNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 5)
)
_AcdTwampGenMIBObjects_ObjectIdentity = ObjectIdentity
acdTwampGenMIBObjects = _AcdTwampGenMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 6)
)
_AcdTwampGenConformance_ObjectIdentity = ObjectIdentity
acdTwampGenConformance = _AcdTwampGenConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 7)
)
_AcdTwampGenCompliances_ObjectIdentity = ObjectIdentity
acdTwampGenCompliances = _AcdTwampGenCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 7, 1)
)
_AcdTwampGenGroups_ObjectIdentity = ObjectIdentity
acdTwampGenGroups = _AcdTwampGenGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 7, 2)
)

# Managed Objects groups

acdTwampGenResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 7, 2, 1)
)
acdTwampGenResultGroup.setObjects(
      *(("ACD-TWAMP-GEN-MIB", "acdTwampGenResultInstName"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPeriodNb"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPeriodTime"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultCurrTxPacketCount"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultCurrRxPacketCount"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDelayValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDelayInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDelayCurrSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDelayCurrMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDelayCurrMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDelayCurrAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDelayCurrThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDvValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDvInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDvCurrSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDvCurrMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDvCurrMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDvCurrAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultTwoWayDvCurrThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDelayValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDelayInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDelayCurrSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDelayCurrMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDelayCurrMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDelayCurrAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDelayCurrThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDvValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDvInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDvCurrSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDvCurrMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDvCurrMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDvCurrAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayNeDvCurrThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDelayValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDelayInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDelayCurrSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDelayCurrMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDelayCurrMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDelayCurrAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDelayCurrThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDvValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDvInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDvCurrSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDvCurrMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDvCurrMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDvCurrAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultOneWayFeDvCurrThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPktLossCurrSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPktLossCurrLostPackets"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPktLossCurrLossRatio"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPktLossCurrOutOfOrder"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPktLossCurrDuplicate"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPktLossCurrGaps"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenResultPktLossCurrLargestGap"))
)
if mibBuilder.loadTexts:
    acdTwampGenResultGroup.setStatus("current")

acdTwampGenStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 7, 2, 2)
)
acdTwampGenStatusGroup.setObjects(
      *(("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusInstName"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusTwoWayDelayAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusTwoWayAvgDelayAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusTwoWayDvAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusTwoWayAvgDvAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusOneWayNeDelayAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusOneWayNeAvgDelayAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusOneWayNeDvAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusOneWayNeAvgDvAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusOneWayFeDelayAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusOneWayFeAvgDelayAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusOneWayFeDvAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusOneWayFeAvgDvAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusPacketLossContinuityCheckAlert"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusPacketLossExcessivePacketLossAlert"))
)
if mibBuilder.loadTexts:
    acdTwampGenStatusGroup.setStatus("current")

acdTwampGenCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 7, 2, 3)
)
acdTwampGenCfgGroup.setObjects(
      *(("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgName"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgState"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgInterval"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgReferencePeriod"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgPktSize"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgDestIPv4Addr"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgSourcePortNumber"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgDestPortNumber"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgDscp"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgEcn"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgVlan1Priority"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgTwoWayMaxDelay"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgTwoWayMaxDelayThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgTwoWayAvgDelayThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgTwoWayMaxDv"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgTwoWayMaxDvThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgTwoWayAvgDvThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayNearEndMaxDelay"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayNearEndMaxDelayThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayNearEndAvgDelayThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayNearEndMaxDv"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayNearEndMaxDvThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayNearEndAvgDvThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayFarEndMaxDelay"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayFarEndMaxDelayThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayFarEndAvgDelayThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayFarEndMaxDv"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayFarEndMaxDvThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgOneWayFarEndAvgDvThrs"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgPacketLossContinuityCheck"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgPacketLossRate"))
)
if mibBuilder.loadTexts:
    acdTwampGenCfgGroup.setStatus("current")

acdTwampGenHistResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 7, 2, 4)
)
acdTwampGenHistResultGroup.setObjects(
      *(("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultID"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultSampleIndex"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultInstName"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultPeriodTime"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTxPacketCount"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultRxPacketCount"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDelayValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDelayInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDelaySamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDelayMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDelayMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDelayAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDelayThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDvValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDvInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDvSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDvMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDvMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDvAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultTwoWayDvThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDelayValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDelayInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDelaySamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDelayMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDelayMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDelayAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDelayThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDvValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDvInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDvSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDvMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDvMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDvAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayNeDvThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDelayValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDelayInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDelaySamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDelayMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDelayMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDelayAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDelayThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDvValid"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDvInstValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDvSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDvMinValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDvMaxValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDvAvgValue"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultOneWayFeDvThreshEx"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultPktLossSamples"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultPktLossLostPackets"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultPktLossLossRatio"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultPktLossOutOfOrder"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultPktLossDuplicate"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultPktLossGaps"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultPktLossLargestGap"))
)
if mibBuilder.loadTexts:
    acdTwampGenHistResultGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdTwampGenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 19, 7, 1, 1)
)
acdTwampGenCompliance.setObjects(
      *(("ACD-TWAMP-GEN-MIB", "acdTwampGenResultGroup"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenStatusGroup"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenCfgGroup"),
        ("ACD-TWAMP-GEN-MIB", "acdTwampGenHistResultGroup"))
)
if mibBuilder.loadTexts:
    acdTwampGenCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-TWAMP-GEN-MIB",
    **{"acdTwampGen": acdTwampGen,
       "acdTwampGenResultTable": acdTwampGenResultTable,
       "acdTwampGenResultEntry": acdTwampGenResultEntry,
       "acdTwampGenResultID": acdTwampGenResultID,
       "acdTwampGenResultInstName": acdTwampGenResultInstName,
       "acdTwampGenResultPeriodNb": acdTwampGenResultPeriodNb,
       "acdTwampGenResultPeriodTime": acdTwampGenResultPeriodTime,
       "acdTwampGenResultCurrTxPacketCount": acdTwampGenResultCurrTxPacketCount,
       "acdTwampGenResultCurrRxPacketCount": acdTwampGenResultCurrRxPacketCount,
       "acdTwampGenResultTwoWayDelayValid": acdTwampGenResultTwoWayDelayValid,
       "acdTwampGenResultTwoWayDelayInstValue": acdTwampGenResultTwoWayDelayInstValue,
       "acdTwampGenResultTwoWayDelayCurrSamples": acdTwampGenResultTwoWayDelayCurrSamples,
       "acdTwampGenResultTwoWayDelayCurrMinValue": acdTwampGenResultTwoWayDelayCurrMinValue,
       "acdTwampGenResultTwoWayDelayCurrMaxValue": acdTwampGenResultTwoWayDelayCurrMaxValue,
       "acdTwampGenResultTwoWayDelayCurrAvgValue": acdTwampGenResultTwoWayDelayCurrAvgValue,
       "acdTwampGenResultTwoWayDelayCurrThreshEx": acdTwampGenResultTwoWayDelayCurrThreshEx,
       "acdTwampGenResultTwoWayDvValid": acdTwampGenResultTwoWayDvValid,
       "acdTwampGenResultTwoWayDvInstValue": acdTwampGenResultTwoWayDvInstValue,
       "acdTwampGenResultTwoWayDvCurrSamples": acdTwampGenResultTwoWayDvCurrSamples,
       "acdTwampGenResultTwoWayDvCurrMinValue": acdTwampGenResultTwoWayDvCurrMinValue,
       "acdTwampGenResultTwoWayDvCurrMaxValue": acdTwampGenResultTwoWayDvCurrMaxValue,
       "acdTwampGenResultTwoWayDvCurrAvgValue": acdTwampGenResultTwoWayDvCurrAvgValue,
       "acdTwampGenResultTwoWayDvCurrThreshEx": acdTwampGenResultTwoWayDvCurrThreshEx,
       "acdTwampGenResultOneWayNeDelayValid": acdTwampGenResultOneWayNeDelayValid,
       "acdTwampGenResultOneWayNeDelayInstValue": acdTwampGenResultOneWayNeDelayInstValue,
       "acdTwampGenResultOneWayNeDelayCurrSamples": acdTwampGenResultOneWayNeDelayCurrSamples,
       "acdTwampGenResultOneWayNeDelayCurrMinValue": acdTwampGenResultOneWayNeDelayCurrMinValue,
       "acdTwampGenResultOneWayNeDelayCurrMaxValue": acdTwampGenResultOneWayNeDelayCurrMaxValue,
       "acdTwampGenResultOneWayNeDelayCurrAvgValue": acdTwampGenResultOneWayNeDelayCurrAvgValue,
       "acdTwampGenResultOneWayNeDelayCurrThreshEx": acdTwampGenResultOneWayNeDelayCurrThreshEx,
       "acdTwampGenResultOneWayNeDvValid": acdTwampGenResultOneWayNeDvValid,
       "acdTwampGenResultOneWayNeDvInstValue": acdTwampGenResultOneWayNeDvInstValue,
       "acdTwampGenResultOneWayNeDvCurrSamples": acdTwampGenResultOneWayNeDvCurrSamples,
       "acdTwampGenResultOneWayNeDvCurrMinValue": acdTwampGenResultOneWayNeDvCurrMinValue,
       "acdTwampGenResultOneWayNeDvCurrMaxValue": acdTwampGenResultOneWayNeDvCurrMaxValue,
       "acdTwampGenResultOneWayNeDvCurrAvgValue": acdTwampGenResultOneWayNeDvCurrAvgValue,
       "acdTwampGenResultOneWayNeDvCurrThreshEx": acdTwampGenResultOneWayNeDvCurrThreshEx,
       "acdTwampGenResultOneWayFeDelayValid": acdTwampGenResultOneWayFeDelayValid,
       "acdTwampGenResultOneWayFeDelayInstValue": acdTwampGenResultOneWayFeDelayInstValue,
       "acdTwampGenResultOneWayFeDelayCurrSamples": acdTwampGenResultOneWayFeDelayCurrSamples,
       "acdTwampGenResultOneWayFeDelayCurrMinValue": acdTwampGenResultOneWayFeDelayCurrMinValue,
       "acdTwampGenResultOneWayFeDelayCurrMaxValue": acdTwampGenResultOneWayFeDelayCurrMaxValue,
       "acdTwampGenResultOneWayFeDelayCurrAvgValue": acdTwampGenResultOneWayFeDelayCurrAvgValue,
       "acdTwampGenResultOneWayFeDelayCurrThreshEx": acdTwampGenResultOneWayFeDelayCurrThreshEx,
       "acdTwampGenResultOneWayFeDvValid": acdTwampGenResultOneWayFeDvValid,
       "acdTwampGenResultOneWayFeDvInstValue": acdTwampGenResultOneWayFeDvInstValue,
       "acdTwampGenResultOneWayFeDvCurrSamples": acdTwampGenResultOneWayFeDvCurrSamples,
       "acdTwampGenResultOneWayFeDvCurrMinValue": acdTwampGenResultOneWayFeDvCurrMinValue,
       "acdTwampGenResultOneWayFeDvCurrMaxValue": acdTwampGenResultOneWayFeDvCurrMaxValue,
       "acdTwampGenResultOneWayFeDvCurrAvgValue": acdTwampGenResultOneWayFeDvCurrAvgValue,
       "acdTwampGenResultOneWayFeDvCurrThreshEx": acdTwampGenResultOneWayFeDvCurrThreshEx,
       "acdTwampGenResultPktLossCurrSamples": acdTwampGenResultPktLossCurrSamples,
       "acdTwampGenResultPktLossCurrLostPackets": acdTwampGenResultPktLossCurrLostPackets,
       "acdTwampGenResultPktLossCurrLossRatio": acdTwampGenResultPktLossCurrLossRatio,
       "acdTwampGenResultPktLossCurrOutOfOrder": acdTwampGenResultPktLossCurrOutOfOrder,
       "acdTwampGenResultPktLossCurrDuplicate": acdTwampGenResultPktLossCurrDuplicate,
       "acdTwampGenResultPktLossCurrGaps": acdTwampGenResultPktLossCurrGaps,
       "acdTwampGenResultPktLossCurrLargestGap": acdTwampGenResultPktLossCurrLargestGap,
       "acdTwampGenStatusTable": acdTwampGenStatusTable,
       "acdTwampGenStatusEntry": acdTwampGenStatusEntry,
       "acdTwampGenStatusID": acdTwampGenStatusID,
       "acdTwampGenStatusInstName": acdTwampGenStatusInstName,
       "acdTwampGenStatusTwoWayDelayAlert": acdTwampGenStatusTwoWayDelayAlert,
       "acdTwampGenStatusTwoWayAvgDelayAlert": acdTwampGenStatusTwoWayAvgDelayAlert,
       "acdTwampGenStatusTwoWayDvAlert": acdTwampGenStatusTwoWayDvAlert,
       "acdTwampGenStatusTwoWayAvgDvAlert": acdTwampGenStatusTwoWayAvgDvAlert,
       "acdTwampGenStatusOneWayNeDelayAlert": acdTwampGenStatusOneWayNeDelayAlert,
       "acdTwampGenStatusOneWayNeAvgDelayAlert": acdTwampGenStatusOneWayNeAvgDelayAlert,
       "acdTwampGenStatusOneWayNeDvAlert": acdTwampGenStatusOneWayNeDvAlert,
       "acdTwampGenStatusOneWayNeAvgDvAlert": acdTwampGenStatusOneWayNeAvgDvAlert,
       "acdTwampGenStatusOneWayFeDelayAlert": acdTwampGenStatusOneWayFeDelayAlert,
       "acdTwampGenStatusOneWayFeAvgDelayAlert": acdTwampGenStatusOneWayFeAvgDelayAlert,
       "acdTwampGenStatusOneWayFeDvAlert": acdTwampGenStatusOneWayFeDvAlert,
       "acdTwampGenStatusOneWayFeAvgDvAlert": acdTwampGenStatusOneWayFeAvgDvAlert,
       "acdTwampGenStatusPacketLossContinuityCheckAlert": acdTwampGenStatusPacketLossContinuityCheckAlert,
       "acdTwampGenStatusPacketLossExcessivePacketLossAlert": acdTwampGenStatusPacketLossExcessivePacketLossAlert,
       "acdTwampGenCfgTable": acdTwampGenCfgTable,
       "acdTwampGenCfgEntry": acdTwampGenCfgEntry,
       "acdTwampGenCfgID": acdTwampGenCfgID,
       "acdTwampGenCfgName": acdTwampGenCfgName,
       "acdTwampGenCfgState": acdTwampGenCfgState,
       "acdTwampGenCfgInterval": acdTwampGenCfgInterval,
       "acdTwampGenCfgReferencePeriod": acdTwampGenCfgReferencePeriod,
       "acdTwampGenCfgPktSize": acdTwampGenCfgPktSize,
       "acdTwampGenCfgDestIPv4Addr": acdTwampGenCfgDestIPv4Addr,
       "acdTwampGenCfgSourcePortNumber": acdTwampGenCfgSourcePortNumber,
       "acdTwampGenCfgDestPortNumber": acdTwampGenCfgDestPortNumber,
       "acdTwampGenCfgDscp": acdTwampGenCfgDscp,
       "acdTwampGenCfgEcn": acdTwampGenCfgEcn,
       "acdTwampGenCfgVlan1Priority": acdTwampGenCfgVlan1Priority,
       "acdTwampGenCfgTwoWayMaxDelay": acdTwampGenCfgTwoWayMaxDelay,
       "acdTwampGenCfgTwoWayMaxDelayThrs": acdTwampGenCfgTwoWayMaxDelayThrs,
       "acdTwampGenCfgTwoWayAvgDelayThrs": acdTwampGenCfgTwoWayAvgDelayThrs,
       "acdTwampGenCfgTwoWayMaxDv": acdTwampGenCfgTwoWayMaxDv,
       "acdTwampGenCfgTwoWayMaxDvThrs": acdTwampGenCfgTwoWayMaxDvThrs,
       "acdTwampGenCfgTwoWayAvgDvThrs": acdTwampGenCfgTwoWayAvgDvThrs,
       "acdTwampGenCfgOneWayNearEndMaxDelay": acdTwampGenCfgOneWayNearEndMaxDelay,
       "acdTwampGenCfgOneWayNearEndMaxDelayThrs": acdTwampGenCfgOneWayNearEndMaxDelayThrs,
       "acdTwampGenCfgOneWayNearEndAvgDelayThrs": acdTwampGenCfgOneWayNearEndAvgDelayThrs,
       "acdTwampGenCfgOneWayNearEndMaxDv": acdTwampGenCfgOneWayNearEndMaxDv,
       "acdTwampGenCfgOneWayNearEndMaxDvThrs": acdTwampGenCfgOneWayNearEndMaxDvThrs,
       "acdTwampGenCfgOneWayNearEndAvgDvThrs": acdTwampGenCfgOneWayNearEndAvgDvThrs,
       "acdTwampGenCfgOneWayFarEndMaxDelay": acdTwampGenCfgOneWayFarEndMaxDelay,
       "acdTwampGenCfgOneWayFarEndMaxDelayThrs": acdTwampGenCfgOneWayFarEndMaxDelayThrs,
       "acdTwampGenCfgOneWayFarEndAvgDelayThrs": acdTwampGenCfgOneWayFarEndAvgDelayThrs,
       "acdTwampGenCfgOneWayFarEndMaxDv": acdTwampGenCfgOneWayFarEndMaxDv,
       "acdTwampGenCfgOneWayFarEndMaxDvThrs": acdTwampGenCfgOneWayFarEndMaxDvThrs,
       "acdTwampGenCfgOneWayFarEndAvgDvThrs": acdTwampGenCfgOneWayFarEndAvgDvThrs,
       "acdTwampGenCfgPacketLossContinuityCheck": acdTwampGenCfgPacketLossContinuityCheck,
       "acdTwampGenCfgPacketLossRate": acdTwampGenCfgPacketLossRate,
       "acdTwampGenHistResultTable": acdTwampGenHistResultTable,
       "acdTwampGenHistResultEntry": acdTwampGenHistResultEntry,
       "acdTwampGenHistResultID": acdTwampGenHistResultID,
       "acdTwampGenHistResultSampleIndex": acdTwampGenHistResultSampleIndex,
       "acdTwampGenHistResultInstName": acdTwampGenHistResultInstName,
       "acdTwampGenHistResultPeriodTime": acdTwampGenHistResultPeriodTime,
       "acdTwampGenHistResultTxPacketCount": acdTwampGenHistResultTxPacketCount,
       "acdTwampGenHistResultRxPacketCount": acdTwampGenHistResultRxPacketCount,
       "acdTwampGenHistResultTwoWayDelayValid": acdTwampGenHistResultTwoWayDelayValid,
       "acdTwampGenHistResultTwoWayDelayInstValue": acdTwampGenHistResultTwoWayDelayInstValue,
       "acdTwampGenHistResultTwoWayDelaySamples": acdTwampGenHistResultTwoWayDelaySamples,
       "acdTwampGenHistResultTwoWayDelayMinValue": acdTwampGenHistResultTwoWayDelayMinValue,
       "acdTwampGenHistResultTwoWayDelayMaxValue": acdTwampGenHistResultTwoWayDelayMaxValue,
       "acdTwampGenHistResultTwoWayDelayAvgValue": acdTwampGenHistResultTwoWayDelayAvgValue,
       "acdTwampGenHistResultTwoWayDelayThreshEx": acdTwampGenHistResultTwoWayDelayThreshEx,
       "acdTwampGenHistResultTwoWayDvValid": acdTwampGenHistResultTwoWayDvValid,
       "acdTwampGenHistResultTwoWayDvInstValue": acdTwampGenHistResultTwoWayDvInstValue,
       "acdTwampGenHistResultTwoWayDvSamples": acdTwampGenHistResultTwoWayDvSamples,
       "acdTwampGenHistResultTwoWayDvMinValue": acdTwampGenHistResultTwoWayDvMinValue,
       "acdTwampGenHistResultTwoWayDvMaxValue": acdTwampGenHistResultTwoWayDvMaxValue,
       "acdTwampGenHistResultTwoWayDvAvgValue": acdTwampGenHistResultTwoWayDvAvgValue,
       "acdTwampGenHistResultTwoWayDvThreshEx": acdTwampGenHistResultTwoWayDvThreshEx,
       "acdTwampGenHistResultOneWayNeDelayValid": acdTwampGenHistResultOneWayNeDelayValid,
       "acdTwampGenHistResultOneWayNeDelayInstValue": acdTwampGenHistResultOneWayNeDelayInstValue,
       "acdTwampGenHistResultOneWayNeDelaySamples": acdTwampGenHistResultOneWayNeDelaySamples,
       "acdTwampGenHistResultOneWayNeDelayMinValue": acdTwampGenHistResultOneWayNeDelayMinValue,
       "acdTwampGenHistResultOneWayNeDelayMaxValue": acdTwampGenHistResultOneWayNeDelayMaxValue,
       "acdTwampGenHistResultOneWayNeDelayAvgValue": acdTwampGenHistResultOneWayNeDelayAvgValue,
       "acdTwampGenHistResultOneWayNeDelayThreshEx": acdTwampGenHistResultOneWayNeDelayThreshEx,
       "acdTwampGenHistResultOneWayNeDvValid": acdTwampGenHistResultOneWayNeDvValid,
       "acdTwampGenHistResultOneWayNeDvInstValue": acdTwampGenHistResultOneWayNeDvInstValue,
       "acdTwampGenHistResultOneWayNeDvSamples": acdTwampGenHistResultOneWayNeDvSamples,
       "acdTwampGenHistResultOneWayNeDvMinValue": acdTwampGenHistResultOneWayNeDvMinValue,
       "acdTwampGenHistResultOneWayNeDvMaxValue": acdTwampGenHistResultOneWayNeDvMaxValue,
       "acdTwampGenHistResultOneWayNeDvAvgValue": acdTwampGenHistResultOneWayNeDvAvgValue,
       "acdTwampGenHistResultOneWayNeDvThreshEx": acdTwampGenHistResultOneWayNeDvThreshEx,
       "acdTwampGenHistResultOneWayFeDelayValid": acdTwampGenHistResultOneWayFeDelayValid,
       "acdTwampGenHistResultOneWayFeDelayInstValue": acdTwampGenHistResultOneWayFeDelayInstValue,
       "acdTwampGenHistResultOneWayFeDelaySamples": acdTwampGenHistResultOneWayFeDelaySamples,
       "acdTwampGenHistResultOneWayFeDelayMinValue": acdTwampGenHistResultOneWayFeDelayMinValue,
       "acdTwampGenHistResultOneWayFeDelayMaxValue": acdTwampGenHistResultOneWayFeDelayMaxValue,
       "acdTwampGenHistResultOneWayFeDelayAvgValue": acdTwampGenHistResultOneWayFeDelayAvgValue,
       "acdTwampGenHistResultOneWayFeDelayThreshEx": acdTwampGenHistResultOneWayFeDelayThreshEx,
       "acdTwampGenHistResultOneWayFeDvValid": acdTwampGenHistResultOneWayFeDvValid,
       "acdTwampGenHistResultOneWayFeDvInstValue": acdTwampGenHistResultOneWayFeDvInstValue,
       "acdTwampGenHistResultOneWayFeDvSamples": acdTwampGenHistResultOneWayFeDvSamples,
       "acdTwampGenHistResultOneWayFeDvMinValue": acdTwampGenHistResultOneWayFeDvMinValue,
       "acdTwampGenHistResultOneWayFeDvMaxValue": acdTwampGenHistResultOneWayFeDvMaxValue,
       "acdTwampGenHistResultOneWayFeDvAvgValue": acdTwampGenHistResultOneWayFeDvAvgValue,
       "acdTwampGenHistResultOneWayFeDvThreshEx": acdTwampGenHistResultOneWayFeDvThreshEx,
       "acdTwampGenHistResultPktLossSamples": acdTwampGenHistResultPktLossSamples,
       "acdTwampGenHistResultPktLossLostPackets": acdTwampGenHistResultPktLossLostPackets,
       "acdTwampGenHistResultPktLossLossRatio": acdTwampGenHistResultPktLossLossRatio,
       "acdTwampGenHistResultPktLossOutOfOrder": acdTwampGenHistResultPktLossOutOfOrder,
       "acdTwampGenHistResultPktLossDuplicate": acdTwampGenHistResultPktLossDuplicate,
       "acdTwampGenHistResultPktLossGaps": acdTwampGenHistResultPktLossGaps,
       "acdTwampGenHistResultPktLossLargestGap": acdTwampGenHistResultPktLossLargestGap,
       "acdTwampGenNotifications": acdTwampGenNotifications,
       "acdTwampGenMIBObjects": acdTwampGenMIBObjects,
       "acdTwampGenConformance": acdTwampGenConformance,
       "acdTwampGenCompliances": acdTwampGenCompliances,
       "acdTwampGenCompliance": acdTwampGenCompliance,
       "acdTwampGenGroups": acdTwampGenGroups,
       "acdTwampGenResultGroup": acdTwampGenResultGroup,
       "acdTwampGenStatusGroup": acdTwampGenStatusGroup,
       "acdTwampGenCfgGroup": acdTwampGenCfgGroup,
       "acdTwampGenHistResultGroup": acdTwampGenHistResultGroup}
)
