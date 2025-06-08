# SNMP MIB module (BELAIR-WRM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-WRM.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairInterfaces,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairInterfaces")

(BelAirEncryptionKey,
 BelAirEncryptionType) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirEncryptionKey",
    "BelAirEncryptionType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

belairWrmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6)
)
if mibBuilder.loadTexts:
    belairWrmMib.setRevisions(
        ("2008-10-08 11:00",
         "2006-10-13 11:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairWrmObjects_ObjectIdentity = ObjectIdentity
belairWrmObjects = _BelairWrmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1)
)
_BaWrmIfConfigTable_Object = MibTable
baWrmIfConfigTable = _BaWrmIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1)
)
if mibBuilder.loadTexts:
    baWrmIfConfigTable.setStatus("current")
_BaWrmIfConfigEntry_Object = MibTableRow
baWrmIfConfigEntry = _BaWrmIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1)
)
baWrmIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baWrmIfConfigEntry.setStatus("current")


class _BaWrmIfMode_Type(Integer32):
    """Custom type baWrmIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bs", 1),
          ("ss", 2))
    )


_BaWrmIfMode_Type.__name__ = "Integer32"
_BaWrmIfMode_Object = MibTableColumn
baWrmIfMode = _BaWrmIfMode_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 1),
    _BaWrmIfMode_Type()
)
baWrmIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfMode.setStatus("current")


class _BaWrmIfBsId_Type(OctetString):
    """Custom type baWrmIfBsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_BaWrmIfBsId_Type.__name__ = "OctetString"
_BaWrmIfBsId_Object = MibTableColumn
baWrmIfBsId = _BaWrmIfBsId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 2),
    _BaWrmIfBsId_Type()
)
baWrmIfBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfBsId.setStatus("current")


class _BaWrmIfEncryptionType_Type(BelAirEncryptionType):
    """Custom type baWrmIfEncryptionType based on BelAirEncryptionType"""
    defaultValue = 4


_BaWrmIfEncryptionType_Type.__name__ = "BelAirEncryptionType"
_BaWrmIfEncryptionType_Object = MibTableColumn
baWrmIfEncryptionType = _BaWrmIfEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 3),
    _BaWrmIfEncryptionType_Type()
)
baWrmIfEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfEncryptionType.setStatus("current")
_BaWrmIfEncryptionKey_Type = BelAirEncryptionKey
_BaWrmIfEncryptionKey_Object = MibTableColumn
baWrmIfEncryptionKey = _BaWrmIfEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 4),
    _BaWrmIfEncryptionKey_Type()
)
baWrmIfEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfEncryptionKey.setStatus("current")
_BaWrmIfChannelNumber_Type = Integer32
_BaWrmIfChannelNumber_Object = MibTableColumn
baWrmIfChannelNumber = _BaWrmIfChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 5),
    _BaWrmIfChannelNumber_Type()
)
baWrmIfChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfChannelNumber.setStatus("current")
_BaWrmIfChannelBandwidth_Type = Integer32
_BaWrmIfChannelBandwidth_Object = MibTableColumn
baWrmIfChannelBandwidth = _BaWrmIfChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 6),
    _BaWrmIfChannelBandwidth_Type()
)
baWrmIfChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    baWrmIfChannelBandwidth.setUnits("kHZ")


class _BaWrmIfTxPowerLevel_Type(Integer32):
    """Custom type baWrmIfTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BaWrmIfTxPowerLevel_Type.__name__ = "Integer32"
_BaWrmIfTxPowerLevel_Object = MibTableColumn
baWrmIfTxPowerLevel = _BaWrmIfTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 7),
    _BaWrmIfTxPowerLevel_Type()
)
baWrmIfTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfTxPowerLevel.setStatus("deprecated")


class _BaWrmIfAntennaGainLevel_Type(Integer32):
    """Custom type baWrmIfAntennaGainLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BaWrmIfAntennaGainLevel_Type.__name__ = "Integer32"
_BaWrmIfAntennaGainLevel_Object = MibTableColumn
baWrmIfAntennaGainLevel = _BaWrmIfAntennaGainLevel_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 8),
    _BaWrmIfAntennaGainLevel_Type()
)
baWrmIfAntennaGainLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfAntennaGainLevel.setStatus("deprecated")


class _BaWrmIfTimeElapsed_Type(Integer32):
    """Custom type baWrmIfTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_BaWrmIfTimeElapsed_Type.__name__ = "Integer32"
_BaWrmIfTimeElapsed_Object = MibTableColumn
baWrmIfTimeElapsed = _BaWrmIfTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 9),
    _BaWrmIfTimeElapsed_Type()
)
baWrmIfTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIfTimeElapsed.setStatus("current")


class _BaWrmIfFrameSize_Type(Integer32):
    """Custom type baWrmIfFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2500, 2500),
        ValueRangeConstraint(4000, 4000),
        ValueRangeConstraint(5000, 5000),
        ValueRangeConstraint(8000, 8000),
        ValueRangeConstraint(10000, 10000),
        ValueRangeConstraint(12500, 12500),
        ValueRangeConstraint(20000, 20000),
    )


_BaWrmIfFrameSize_Type.__name__ = "Integer32"
_BaWrmIfFrameSize_Object = MibTableColumn
baWrmIfFrameSize = _BaWrmIfFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 10),
    _BaWrmIfFrameSize_Type()
)
baWrmIfFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    baWrmIfFrameSize.setUnits("us")


class _BaWrmIfModulationType_Type(Integer32):
    """Custom type baWrmIfModulationType based on Integer32"""
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
              1001)
        )
    )
    namedValues = NamedValues(
        *(("bpskCc1Over2", 0),
          ("qpskRsCcCc1Over2", 1),
          ("qpskRsCcCc3Over4", 2),
          ("sixteenQamRsCcCc1Over2", 3),
          ("sixteenQamRsCcCc3Over4", 4),
          ("sixtyFourQamRsCcCc2Over3", 5),
          ("sixtyFourQamRsCcCc3Over4", 6),
          ("dynamic", 1001))
    )


_BaWrmIfModulationType_Type.__name__ = "Integer32"
_BaWrmIfModulationType_Object = MibTableColumn
baWrmIfModulationType = _BaWrmIfModulationType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 11),
    _BaWrmIfModulationType_Type()
)
baWrmIfModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfModulationType.setStatus("current")
_BaWrmIfTxPower_Type = Integer32
_BaWrmIfTxPower_Object = MibTableColumn
baWrmIfTxPower = _BaWrmIfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 12),
    _BaWrmIfTxPower_Type()
)
baWrmIfTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfTxPower.setStatus("current")
if mibBuilder.loadTexts:
    baWrmIfTxPower.setUnits("dBm/100")
_BaWrmIfAntennaGain_Type = Integer32
_BaWrmIfAntennaGain_Object = MibTableColumn
baWrmIfAntennaGain = _BaWrmIfAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 13),
    _BaWrmIfAntennaGain_Type()
)
baWrmIfAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    baWrmIfAntennaGain.setUnits("dBi/100")


class _BaWrmIfLinkDistance_Type(Integer32):
    """Custom type baWrmIfLinkDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BaWrmIfLinkDistance_Type.__name__ = "Integer32"
_BaWrmIfLinkDistance_Object = MibTableColumn
baWrmIfLinkDistance = _BaWrmIfLinkDistance_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 1, 1, 14),
    _BaWrmIfLinkDistance_Type()
)
baWrmIfLinkDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baWrmIfLinkDistance.setStatus("current")
if mibBuilder.loadTexts:
    baWrmIfLinkDistance.setUnits("km")
_BaWrmCommonCurrTable_Object = MibTable
baWrmCommonCurrTable = _BaWrmCommonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2)
)
if mibBuilder.loadTexts:
    baWrmCommonCurrTable.setStatus("current")
_BaWrmCommonCurrEntry_Object = MibTableRow
baWrmCommonCurrEntry = _BaWrmCommonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1)
)
baWrmCommonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baWrmCommonCurrEntry.setStatus("current")
_BaWrmCurrRxBursts_Type = PerfCurrentCount
_BaWrmCurrRxBursts_Object = MibTableColumn
baWrmCurrRxBursts = _BaWrmCurrRxBursts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 1),
    _BaWrmCurrRxBursts_Type()
)
baWrmCurrRxBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrRxBursts.setStatus("current")
_BaWrmCurrRxBurstErrors_Type = PerfCurrentCount
_BaWrmCurrRxBurstErrors_Object = MibTableColumn
baWrmCurrRxBurstErrors = _BaWrmCurrRxBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 2),
    _BaWrmCurrRxBurstErrors_Type()
)
baWrmCurrRxBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrRxBurstErrors.setStatus("current")
_BaWrmCurrTxBursts_Type = PerfCurrentCount
_BaWrmCurrTxBursts_Object = MibTableColumn
baWrmCurrTxBursts = _BaWrmCurrTxBursts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 3),
    _BaWrmCurrTxBursts_Type()
)
baWrmCurrTxBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrTxBursts.setStatus("current")
_BaWrmCurrTxBurstErrors_Type = PerfCurrentCount
_BaWrmCurrTxBurstErrors_Object = MibTableColumn
baWrmCurrTxBurstErrors = _BaWrmCurrTxBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 4),
    _BaWrmCurrTxBurstErrors_Type()
)
baWrmCurrTxBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrTxBurstErrors.setStatus("current")
_BaWrmCurrRxPdus_Type = PerfCurrentCount
_BaWrmCurrRxPdus_Object = MibTableColumn
baWrmCurrRxPdus = _BaWrmCurrRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 5),
    _BaWrmCurrRxPdus_Type()
)
baWrmCurrRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrRxPdus.setStatus("current")
_BaWrmCurrRxPduErrors_Type = PerfCurrentCount
_BaWrmCurrRxPduErrors_Object = MibTableColumn
baWrmCurrRxPduErrors = _BaWrmCurrRxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 6),
    _BaWrmCurrRxPduErrors_Type()
)
baWrmCurrRxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrRxPduErrors.setStatus("current")
_BaWrmCurrPduCrcErrors_Type = PerfCurrentCount
_BaWrmCurrPduCrcErrors_Object = MibTableColumn
baWrmCurrPduCrcErrors = _BaWrmCurrPduCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 7),
    _BaWrmCurrPduCrcErrors_Type()
)
baWrmCurrPduCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrPduCrcErrors.setStatus("current")
_BaWrmCurrTxPdus_Type = PerfCurrentCount
_BaWrmCurrTxPdus_Object = MibTableColumn
baWrmCurrTxPdus = _BaWrmCurrTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 8),
    _BaWrmCurrTxPdus_Type()
)
baWrmCurrTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrTxPdus.setStatus("current")
_BaWrmCurrTxPduErrors_Type = PerfCurrentCount
_BaWrmCurrTxPduErrors_Object = MibTableColumn
baWrmCurrTxPduErrors = _BaWrmCurrTxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 2, 1, 9),
    _BaWrmCurrTxPduErrors_Type()
)
baWrmCurrTxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmCurrTxPduErrors.setStatus("current")
_BaWrmCommonIntervalTable_Object = MibTable
baWrmCommonIntervalTable = _BaWrmCommonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3)
)
if mibBuilder.loadTexts:
    baWrmCommonIntervalTable.setStatus("current")
_BaWrmCommonIntervalEntry_Object = MibTableRow
baWrmCommonIntervalEntry = _BaWrmCommonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1)
)
baWrmCommonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-WRM", "baWrmIntervalNumber"),
)
if mibBuilder.loadTexts:
    baWrmCommonIntervalEntry.setStatus("current")


class _BaWrmIntervalNumber_Type(Integer32):
    """Custom type baWrmIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_BaWrmIntervalNumber_Type.__name__ = "Integer32"
_BaWrmIntervalNumber_Object = MibTableColumn
baWrmIntervalNumber = _BaWrmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 1),
    _BaWrmIntervalNumber_Type()
)
baWrmIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baWrmIntervalNumber.setStatus("current")
_BaWrmIntervalValid_Type = TruthValue
_BaWrmIntervalValid_Object = MibTableColumn
baWrmIntervalValid = _BaWrmIntervalValid_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 2),
    _BaWrmIntervalValid_Type()
)
baWrmIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalValid.setStatus("current")
_BaWrmIntervalRxBursts_Type = PerfIntervalCount
_BaWrmIntervalRxBursts_Object = MibTableColumn
baWrmIntervalRxBursts = _BaWrmIntervalRxBursts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 3),
    _BaWrmIntervalRxBursts_Type()
)
baWrmIntervalRxBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalRxBursts.setStatus("current")
_BaWrmIntervalRxBurstErrors_Type = PerfIntervalCount
_BaWrmIntervalRxBurstErrors_Object = MibTableColumn
baWrmIntervalRxBurstErrors = _BaWrmIntervalRxBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 4),
    _BaWrmIntervalRxBurstErrors_Type()
)
baWrmIntervalRxBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalRxBurstErrors.setStatus("current")
_BaWrmIntervalTxBursts_Type = PerfIntervalCount
_BaWrmIntervalTxBursts_Object = MibTableColumn
baWrmIntervalTxBursts = _BaWrmIntervalTxBursts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 5),
    _BaWrmIntervalTxBursts_Type()
)
baWrmIntervalTxBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalTxBursts.setStatus("current")
_BaWrmIntervalTxBurstErrors_Type = PerfIntervalCount
_BaWrmIntervalTxBurstErrors_Object = MibTableColumn
baWrmIntervalTxBurstErrors = _BaWrmIntervalTxBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 6),
    _BaWrmIntervalTxBurstErrors_Type()
)
baWrmIntervalTxBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalTxBurstErrors.setStatus("current")
_BaWrmIntervalRxPdus_Type = PerfIntervalCount
_BaWrmIntervalRxPdus_Object = MibTableColumn
baWrmIntervalRxPdus = _BaWrmIntervalRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 7),
    _BaWrmIntervalRxPdus_Type()
)
baWrmIntervalRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalRxPdus.setStatus("current")
_BaWrmIntervalRxPduErrors_Type = PerfIntervalCount
_BaWrmIntervalRxPduErrors_Object = MibTableColumn
baWrmIntervalRxPduErrors = _BaWrmIntervalRxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 8),
    _BaWrmIntervalRxPduErrors_Type()
)
baWrmIntervalRxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalRxPduErrors.setStatus("current")
_BaWrmIntervalPduCrcErrors_Type = PerfIntervalCount
_BaWrmIntervalPduCrcErrors_Object = MibTableColumn
baWrmIntervalPduCrcErrors = _BaWrmIntervalPduCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 9),
    _BaWrmIntervalPduCrcErrors_Type()
)
baWrmIntervalPduCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalPduCrcErrors.setStatus("current")
_BaWrmIntervalTxPdus_Type = PerfIntervalCount
_BaWrmIntervalTxPdus_Object = MibTableColumn
baWrmIntervalTxPdus = _BaWrmIntervalTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 10),
    _BaWrmIntervalTxPdus_Type()
)
baWrmIntervalTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalTxPdus.setStatus("current")
_BaWrmIntervalTxPduErrors_Type = PerfIntervalCount
_BaWrmIntervalTxPduErrors_Object = MibTableColumn
baWrmIntervalTxPduErrors = _BaWrmIntervalTxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 3, 1, 11),
    _BaWrmIntervalTxPduErrors_Type()
)
baWrmIntervalTxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmIntervalTxPduErrors.setStatus("current")
_BaWrmCommonTotalTable_Object = MibTable
baWrmCommonTotalTable = _BaWrmCommonTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4)
)
if mibBuilder.loadTexts:
    baWrmCommonTotalTable.setStatus("current")
_BaWrmCommonTotalEntry_Object = MibTableRow
baWrmCommonTotalEntry = _BaWrmCommonTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1)
)
baWrmCommonTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baWrmCommonTotalEntry.setStatus("current")
_BaWrmTotalRxBursts_Type = PerfTotalCount
_BaWrmTotalRxBursts_Object = MibTableColumn
baWrmTotalRxBursts = _BaWrmTotalRxBursts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 1),
    _BaWrmTotalRxBursts_Type()
)
baWrmTotalRxBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalRxBursts.setStatus("current")
_BaWrmTotalRxBurstErrors_Type = PerfTotalCount
_BaWrmTotalRxBurstErrors_Object = MibTableColumn
baWrmTotalRxBurstErrors = _BaWrmTotalRxBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 2),
    _BaWrmTotalRxBurstErrors_Type()
)
baWrmTotalRxBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalRxBurstErrors.setStatus("current")
_BaWrmTotalTxBursts_Type = PerfTotalCount
_BaWrmTotalTxBursts_Object = MibTableColumn
baWrmTotalTxBursts = _BaWrmTotalTxBursts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 3),
    _BaWrmTotalTxBursts_Type()
)
baWrmTotalTxBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalTxBursts.setStatus("current")
_BaWrmTotalTxBurstErrors_Type = PerfTotalCount
_BaWrmTotalTxBurstErrors_Object = MibTableColumn
baWrmTotalTxBurstErrors = _BaWrmTotalTxBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 4),
    _BaWrmTotalTxBurstErrors_Type()
)
baWrmTotalTxBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalTxBurstErrors.setStatus("current")
_BaWrmTotalRxPdus_Type = PerfTotalCount
_BaWrmTotalRxPdus_Object = MibTableColumn
baWrmTotalRxPdus = _BaWrmTotalRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 5),
    _BaWrmTotalRxPdus_Type()
)
baWrmTotalRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalRxPdus.setStatus("current")
_BaWrmTotalRxPduErrors_Type = PerfTotalCount
_BaWrmTotalRxPduErrors_Object = MibTableColumn
baWrmTotalRxPduErrors = _BaWrmTotalRxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 6),
    _BaWrmTotalRxPduErrors_Type()
)
baWrmTotalRxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalRxPduErrors.setStatus("current")
_BaWrmTotalPduCrcErrors_Type = PerfTotalCount
_BaWrmTotalPduCrcErrors_Object = MibTableColumn
baWrmTotalPduCrcErrors = _BaWrmTotalPduCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 7),
    _BaWrmTotalPduCrcErrors_Type()
)
baWrmTotalPduCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalPduCrcErrors.setStatus("current")
_BaWrmTotalTxPdus_Type = PerfTotalCount
_BaWrmTotalTxPdus_Object = MibTableColumn
baWrmTotalTxPdus = _BaWrmTotalTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 8),
    _BaWrmTotalTxPdus_Type()
)
baWrmTotalTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalTxPdus.setStatus("current")
_BaWrmTotalTxPduErrors_Type = PerfTotalCount
_BaWrmTotalTxPduErrors_Object = MibTableColumn
baWrmTotalTxPduErrors = _BaWrmTotalTxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 4, 1, 9),
    _BaWrmTotalTxPduErrors_Type()
)
baWrmTotalTxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTotalTxPduErrors.setStatus("current")
_BaWrmBsCurrTable_Object = MibTable
baWrmBsCurrTable = _BaWrmBsCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 5)
)
if mibBuilder.loadTexts:
    baWrmBsCurrTable.setStatus("current")
_BaWrmBsCurrEntry_Object = MibTableRow
baWrmBsCurrEntry = _BaWrmBsCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 5, 1)
)
baWrmBsCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baWrmBsCurrEntry.setStatus("current")
_BaWrmBsCurrRngReqReceived_Type = PerfCurrentCount
_BaWrmBsCurrRngReqReceived_Object = MibTableColumn
baWrmBsCurrRngReqReceived = _BaWrmBsCurrRngReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 5, 1, 1),
    _BaWrmBsCurrRngReqReceived_Type()
)
baWrmBsCurrRngReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmBsCurrRngReqReceived.setStatus("current")
_BaWrmBsCurrRngRspSent_Type = PerfCurrentCount
_BaWrmBsCurrRngRspSent_Object = MibTableColumn
baWrmBsCurrRngRspSent = _BaWrmBsCurrRngRspSent_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 5, 1, 2),
    _BaWrmBsCurrRngRspSent_Type()
)
baWrmBsCurrRngRspSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmBsCurrRngRspSent.setStatus("current")
_BaWrmBsIntervalTable_Object = MibTable
baWrmBsIntervalTable = _BaWrmBsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 6)
)
if mibBuilder.loadTexts:
    baWrmBsIntervalTable.setStatus("current")
_BaWrmBsIntervalEntry_Object = MibTableRow
baWrmBsIntervalEntry = _BaWrmBsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 6, 1)
)
baWrmBsIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-WRM", "baWrmBsIntervalNumber"),
)
if mibBuilder.loadTexts:
    baWrmBsIntervalEntry.setStatus("current")


class _BaWrmBsIntervalNumber_Type(Integer32):
    """Custom type baWrmBsIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_BaWrmBsIntervalNumber_Type.__name__ = "Integer32"
_BaWrmBsIntervalNumber_Object = MibTableColumn
baWrmBsIntervalNumber = _BaWrmBsIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 6, 1, 1),
    _BaWrmBsIntervalNumber_Type()
)
baWrmBsIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baWrmBsIntervalNumber.setStatus("current")
_BaWrmBsIntervalValid_Type = TruthValue
_BaWrmBsIntervalValid_Object = MibTableColumn
baWrmBsIntervalValid = _BaWrmBsIntervalValid_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 6, 1, 2),
    _BaWrmBsIntervalValid_Type()
)
baWrmBsIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmBsIntervalValid.setStatus("current")
_BaWrmBsIntervalRngReqReceived_Type = PerfIntervalCount
_BaWrmBsIntervalRngReqReceived_Object = MibTableColumn
baWrmBsIntervalRngReqReceived = _BaWrmBsIntervalRngReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 6, 1, 3),
    _BaWrmBsIntervalRngReqReceived_Type()
)
baWrmBsIntervalRngReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmBsIntervalRngReqReceived.setStatus("current")
_BaWrmBsIntervalRngRspSent_Type = PerfIntervalCount
_BaWrmBsIntervalRngRspSent_Object = MibTableColumn
baWrmBsIntervalRngRspSent = _BaWrmBsIntervalRngRspSent_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 6, 1, 4),
    _BaWrmBsIntervalRngRspSent_Type()
)
baWrmBsIntervalRngRspSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmBsIntervalRngRspSent.setStatus("current")
_BaWrmBsTotalTable_Object = MibTable
baWrmBsTotalTable = _BaWrmBsTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 7)
)
if mibBuilder.loadTexts:
    baWrmBsTotalTable.setStatus("current")
_BaWrmBsTotalEntry_Object = MibTableRow
baWrmBsTotalEntry = _BaWrmBsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 7, 1)
)
baWrmBsTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baWrmBsTotalEntry.setStatus("current")
_BaWrmBsTotalRngReqReceived_Type = PerfTotalCount
_BaWrmBsTotalRngReqReceived_Object = MibTableColumn
baWrmBsTotalRngReqReceived = _BaWrmBsTotalRngReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 7, 1, 1),
    _BaWrmBsTotalRngReqReceived_Type()
)
baWrmBsTotalRngReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmBsTotalRngReqReceived.setStatus("current")
_BaWrmBsTotalRngRspSent_Type = PerfTotalCount
_BaWrmBsTotalRngRspSent_Object = MibTableColumn
baWrmBsTotalRngRspSent = _BaWrmBsTotalRngRspSent_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 7, 1, 2),
    _BaWrmBsTotalRngRspSent_Type()
)
baWrmBsTotalRngRspSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmBsTotalRngRspSent.setStatus("current")
_BaWrmSsCurrTable_Object = MibTable
baWrmSsCurrTable = _BaWrmSsCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 8)
)
if mibBuilder.loadTexts:
    baWrmSsCurrTable.setStatus("current")
_BaWrmSsCurrEntry_Object = MibTableRow
baWrmSsCurrEntry = _BaWrmSsCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 8, 1)
)
baWrmSsCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baWrmSsCurrEntry.setStatus("current")
_BaWrmSsCurrRxDlMapPdus_Type = PerfCurrentCount
_BaWrmSsCurrRxDlMapPdus_Object = MibTableColumn
baWrmSsCurrRxDlMapPdus = _BaWrmSsCurrRxDlMapPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 8, 1, 1),
    _BaWrmSsCurrRxDlMapPdus_Type()
)
baWrmSsCurrRxDlMapPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsCurrRxDlMapPdus.setStatus("current")
_BaWrmSsCurrRxUlMapPdus_Type = PerfCurrentCount
_BaWrmSsCurrRxUlMapPdus_Object = MibTableColumn
baWrmSsCurrRxUlMapPdus = _BaWrmSsCurrRxUlMapPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 8, 1, 2),
    _BaWrmSsCurrRxUlMapPdus_Type()
)
baWrmSsCurrRxUlMapPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsCurrRxUlMapPdus.setStatus("current")
_BaWrmSsCurrRxDlFps_Type = PerfCurrentCount
_BaWrmSsCurrRxDlFps_Object = MibTableColumn
baWrmSsCurrRxDlFps = _BaWrmSsCurrRxDlFps_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 8, 1, 3),
    _BaWrmSsCurrRxDlFps_Type()
)
baWrmSsCurrRxDlFps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsCurrRxDlFps.setStatus("current")
_BaWrmSsCurrRngReqSent_Type = PerfCurrentCount
_BaWrmSsCurrRngReqSent_Object = MibTableColumn
baWrmSsCurrRngReqSent = _BaWrmSsCurrRngReqSent_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 8, 1, 4),
    _BaWrmSsCurrRngReqSent_Type()
)
baWrmSsCurrRngReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsCurrRngReqSent.setStatus("current")
_BaWrmSsCurrRngRspReceived_Type = PerfCurrentCount
_BaWrmSsCurrRngRspReceived_Object = MibTableColumn
baWrmSsCurrRngRspReceived = _BaWrmSsCurrRngRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 8, 1, 5),
    _BaWrmSsCurrRngRspReceived_Type()
)
baWrmSsCurrRngRspReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsCurrRngRspReceived.setStatus("current")
_BaWrmSsIntervalTable_Object = MibTable
baWrmSsIntervalTable = _BaWrmSsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9)
)
if mibBuilder.loadTexts:
    baWrmSsIntervalTable.setStatus("current")
_BaWrmSsIntervalEntry_Object = MibTableRow
baWrmSsIntervalEntry = _BaWrmSsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9, 1)
)
baWrmSsIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-WRM", "baWrmSsIntervalNumber"),
)
if mibBuilder.loadTexts:
    baWrmSsIntervalEntry.setStatus("current")


class _BaWrmSsIntervalNumber_Type(Integer32):
    """Custom type baWrmSsIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_BaWrmSsIntervalNumber_Type.__name__ = "Integer32"
_BaWrmSsIntervalNumber_Object = MibTableColumn
baWrmSsIntervalNumber = _BaWrmSsIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9, 1, 1),
    _BaWrmSsIntervalNumber_Type()
)
baWrmSsIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baWrmSsIntervalNumber.setStatus("current")
_BaWrmSsIntervalValid_Type = TruthValue
_BaWrmSsIntervalValid_Object = MibTableColumn
baWrmSsIntervalValid = _BaWrmSsIntervalValid_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9, 1, 2),
    _BaWrmSsIntervalValid_Type()
)
baWrmSsIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsIntervalValid.setStatus("current")
_BaWrmSsIntervalRxDlMapPdus_Type = PerfIntervalCount
_BaWrmSsIntervalRxDlMapPdus_Object = MibTableColumn
baWrmSsIntervalRxDlMapPdus = _BaWrmSsIntervalRxDlMapPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9, 1, 3),
    _BaWrmSsIntervalRxDlMapPdus_Type()
)
baWrmSsIntervalRxDlMapPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsIntervalRxDlMapPdus.setStatus("current")
_BaWrmSsIntervalRxUlMapPdus_Type = PerfIntervalCount
_BaWrmSsIntervalRxUlMapPdus_Object = MibTableColumn
baWrmSsIntervalRxUlMapPdus = _BaWrmSsIntervalRxUlMapPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9, 1, 4),
    _BaWrmSsIntervalRxUlMapPdus_Type()
)
baWrmSsIntervalRxUlMapPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsIntervalRxUlMapPdus.setStatus("current")
_BaWrmSsIntervalRxDlFps_Type = PerfIntervalCount
_BaWrmSsIntervalRxDlFps_Object = MibTableColumn
baWrmSsIntervalRxDlFps = _BaWrmSsIntervalRxDlFps_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9, 1, 5),
    _BaWrmSsIntervalRxDlFps_Type()
)
baWrmSsIntervalRxDlFps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsIntervalRxDlFps.setStatus("current")
_BaWrmSsIntervalRngReqSent_Type = PerfIntervalCount
_BaWrmSsIntervalRngReqSent_Object = MibTableColumn
baWrmSsIntervalRngReqSent = _BaWrmSsIntervalRngReqSent_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9, 1, 6),
    _BaWrmSsIntervalRngReqSent_Type()
)
baWrmSsIntervalRngReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsIntervalRngReqSent.setStatus("current")
_BaWrmSsIntervalRngRspReceived_Type = PerfIntervalCount
_BaWrmSsIntervalRngRspReceived_Object = MibTableColumn
baWrmSsIntervalRngRspReceived = _BaWrmSsIntervalRngRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 9, 1, 7),
    _BaWrmSsIntervalRngRspReceived_Type()
)
baWrmSsIntervalRngRspReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsIntervalRngRspReceived.setStatus("current")
_BaWrmSsTotalTable_Object = MibTable
baWrmSsTotalTable = _BaWrmSsTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 10)
)
if mibBuilder.loadTexts:
    baWrmSsTotalTable.setStatus("current")
_BaWrmSsTotalEntry_Object = MibTableRow
baWrmSsTotalEntry = _BaWrmSsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 10, 1)
)
baWrmSsTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baWrmSsTotalEntry.setStatus("current")
_BaWrmSsTotalRxDlMapPdus_Type = PerfTotalCount
_BaWrmSsTotalRxDlMapPdus_Object = MibTableColumn
baWrmSsTotalRxDlMapPdus = _BaWrmSsTotalRxDlMapPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 10, 1, 1),
    _BaWrmSsTotalRxDlMapPdus_Type()
)
baWrmSsTotalRxDlMapPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsTotalRxDlMapPdus.setStatus("current")
_BaWrmSsTotalRxUlMapPdus_Type = PerfTotalCount
_BaWrmSsTotalRxUlMapPdus_Object = MibTableColumn
baWrmSsTotalRxUlMapPdus = _BaWrmSsTotalRxUlMapPdus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 10, 1, 2),
    _BaWrmSsTotalRxUlMapPdus_Type()
)
baWrmSsTotalRxUlMapPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsTotalRxUlMapPdus.setStatus("current")
_BaWrmSsTotalRxDlFps_Type = PerfTotalCount
_BaWrmSsTotalRxDlFps_Object = MibTableColumn
baWrmSsTotalRxDlFps = _BaWrmSsTotalRxDlFps_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 10, 1, 3),
    _BaWrmSsTotalRxDlFps_Type()
)
baWrmSsTotalRxDlFps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsTotalRxDlFps.setStatus("current")
_BaWrmSsTotalRngReqSent_Type = PerfTotalCount
_BaWrmSsTotalRngReqSent_Object = MibTableColumn
baWrmSsTotalRngReqSent = _BaWrmSsTotalRngReqSent_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 10, 1, 4),
    _BaWrmSsTotalRngReqSent_Type()
)
baWrmSsTotalRngReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsTotalRngReqSent.setStatus("current")
_BaWrmSsTotalRngRspReceived_Type = PerfTotalCount
_BaWrmSsTotalRngRspReceived_Object = MibTableColumn
baWrmSsTotalRngRspReceived = _BaWrmSsTotalRngRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 10, 1, 5),
    _BaWrmSsTotalRngRspReceived_Type()
)
baWrmSsTotalRngRspReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmSsTotalRngRspReceived.setStatus("current")
_BaWrmLinkInfoTable_Object = MibTable
baWrmLinkInfoTable = _BaWrmLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 11)
)
if mibBuilder.loadTexts:
    baWrmLinkInfoTable.setStatus("current")
_BaWrmLinkInfoEntry_Object = MibTableRow
baWrmLinkInfoEntry = _BaWrmLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 11, 1)
)
baWrmLinkInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-WRM", "baWrmLinkIndex"),
)
if mibBuilder.loadTexts:
    baWrmLinkInfoEntry.setStatus("current")


class _BaWrmLinkIndex_Type(Integer32):
    """Custom type baWrmLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_BaWrmLinkIndex_Type.__name__ = "Integer32"
_BaWrmLinkIndex_Object = MibTableColumn
baWrmLinkIndex = _BaWrmLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 11, 1, 1),
    _BaWrmLinkIndex_Type()
)
baWrmLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baWrmLinkIndex.setStatus("current")
_BaWrmPeerMacAddress_Type = MacAddress
_BaWrmPeerMacAddress_Object = MibTableColumn
baWrmPeerMacAddress = _BaWrmPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 11, 1, 2),
    _BaWrmPeerMacAddress_Type()
)
baWrmPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmPeerMacAddress.setStatus("current")
_BaWrmLinkRssi_Type = Integer32
_BaWrmLinkRssi_Object = MibTableColumn
baWrmLinkRssi = _BaWrmLinkRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 11, 1, 3),
    _BaWrmLinkRssi_Type()
)
baWrmLinkRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmLinkRssi.setStatus("current")
if mibBuilder.loadTexts:
    baWrmLinkRssi.setUnits("dBm")
_BaWrmLinkCinr_Type = Integer32
_BaWrmLinkCinr_Object = MibTableColumn
baWrmLinkCinr = _BaWrmLinkCinr_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 11, 1, 4),
    _BaWrmLinkCinr_Type()
)
baWrmLinkCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmLinkCinr.setStatus("current")
if mibBuilder.loadTexts:
    baWrmLinkCinr.setUnits("dB")


class _BaWrmLinkModulationType_Type(Integer32):
    """Custom type baWrmLinkModulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bpskCc1Over2", 0),
          ("qpskRsCcCc1Over2", 1),
          ("qpskRsCcCc3Over4", 2),
          ("sixteenQamRsCcCc1Over2", 3),
          ("sixteenQamRsCcCc3Over4", 4),
          ("sixtyFourQamRsCcCc2Over3", 5),
          ("sixtyFourQamRsCcCc3Over4", 6))
    )


_BaWrmLinkModulationType_Type.__name__ = "Integer32"
_BaWrmLinkModulationType_Object = MibTableColumn
baWrmLinkModulationType = _BaWrmLinkModulationType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 11, 1, 5),
    _BaWrmLinkModulationType_Type()
)
baWrmLinkModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmLinkModulationType.setStatus("current")
_BaWrmTxPowerTable_Object = MibTable
baWrmTxPowerTable = _BaWrmTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 12)
)
if mibBuilder.loadTexts:
    baWrmTxPowerTable.setStatus("deprecated")
_BaWrmTxPowerEntry_Object = MibTableRow
baWrmTxPowerEntry = _BaWrmTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 12, 1)
)
baWrmTxPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-WRM", "baWrmTxPowerLevel"),
)
if mibBuilder.loadTexts:
    baWrmTxPowerEntry.setStatus("deprecated")


class _BaWrmTxPowerLevel_Type(Integer32):
    """Custom type baWrmTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BaWrmTxPowerLevel_Type.__name__ = "Integer32"
_BaWrmTxPowerLevel_Object = MibTableColumn
baWrmTxPowerLevel = _BaWrmTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 12, 1, 1),
    _BaWrmTxPowerLevel_Type()
)
baWrmTxPowerLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baWrmTxPowerLevel.setStatus("deprecated")
_BaWrmTxPower_Type = Integer32
_BaWrmTxPower_Object = MibTableColumn
baWrmTxPower = _BaWrmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 1, 12, 1, 2),
    _BaWrmTxPower_Type()
)
baWrmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baWrmTxPower.setStatus("deprecated")
if mibBuilder.loadTexts:
    baWrmTxPower.setUnits("dBm")
_BelairWrmTraps_ObjectIdentity = ObjectIdentity
belairWrmTraps = _BelairWrmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 2)
)
_BelairWrmConformance_ObjectIdentity = ObjectIdentity
belairWrmConformance = _BelairWrmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 3)
)

# Managed Objects groups

belairWrmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 3, 1)
)
belairWrmObjectGroup.setObjects(
      *(("BELAIR-WRM", "baWrmIfMode"),
        ("BELAIR-WRM", "baWrmIfBsId"),
        ("BELAIR-WRM", "baWrmIfEncryptionType"),
        ("BELAIR-WRM", "baWrmIfEncryptionKey"),
        ("BELAIR-WRM", "baWrmIfChannelNumber"),
        ("BELAIR-WRM", "baWrmIfChannelBandwidth"),
        ("BELAIR-WRM", "baWrmCurrRxBursts"),
        ("BELAIR-WRM", "baWrmCurrRxBurstErrors"),
        ("BELAIR-WRM", "baWrmCurrTxBursts"),
        ("BELAIR-WRM", "baWrmCurrTxBurstErrors"),
        ("BELAIR-WRM", "baWrmCurrRxPdus"),
        ("BELAIR-WRM", "baWrmCurrRxPduErrors"),
        ("BELAIR-WRM", "baWrmCurrPduCrcErrors"),
        ("BELAIR-WRM", "baWrmCurrTxPdus"),
        ("BELAIR-WRM", "baWrmCurrTxPduErrors"),
        ("BELAIR-WRM", "baWrmIntervalValid"),
        ("BELAIR-WRM", "baWrmIntervalRxBursts"),
        ("BELAIR-WRM", "baWrmIntervalRxBurstErrors"),
        ("BELAIR-WRM", "baWrmIntervalTxBursts"),
        ("BELAIR-WRM", "baWrmIntervalTxBurstErrors"),
        ("BELAIR-WRM", "baWrmIntervalRxPdus"),
        ("BELAIR-WRM", "baWrmIntervalRxPduErrors"),
        ("BELAIR-WRM", "baWrmIntervalPduCrcErrors"),
        ("BELAIR-WRM", "baWrmIntervalTxPdus"),
        ("BELAIR-WRM", "baWrmIntervalTxPduErrors"),
        ("BELAIR-WRM", "baWrmTotalRxBursts"),
        ("BELAIR-WRM", "baWrmTotalRxBurstErrors"),
        ("BELAIR-WRM", "baWrmTotalTxBursts"),
        ("BELAIR-WRM", "baWrmTotalTxBurstErrors"),
        ("BELAIR-WRM", "baWrmTotalRxPdus"),
        ("BELAIR-WRM", "baWrmTotalRxPduErrors"),
        ("BELAIR-WRM", "baWrmTotalPduCrcErrors"),
        ("BELAIR-WRM", "baWrmTotalTxPdus"),
        ("BELAIR-WRM", "baWrmTotalTxPduErrors"),
        ("BELAIR-WRM", "baWrmBsCurrRngReqReceived"),
        ("BELAIR-WRM", "baWrmBsCurrRngRspSent"),
        ("BELAIR-WRM", "baWrmBsIntervalValid"),
        ("BELAIR-WRM", "baWrmBsIntervalRngReqReceived"),
        ("BELAIR-WRM", "baWrmBsIntervalRngRspSent"),
        ("BELAIR-WRM", "baWrmBsTotalRngReqReceived"),
        ("BELAIR-WRM", "baWrmBsTotalRngRspSent"),
        ("BELAIR-WRM", "baWrmSsCurrRxDlMapPdus"),
        ("BELAIR-WRM", "baWrmSsCurrRxUlMapPdus"),
        ("BELAIR-WRM", "baWrmSsCurrRxDlFps"),
        ("BELAIR-WRM", "baWrmSsCurrRngReqSent"),
        ("BELAIR-WRM", "baWrmSsCurrRngRspReceived"),
        ("BELAIR-WRM", "baWrmSsIntervalValid"),
        ("BELAIR-WRM", "baWrmSsIntervalRxDlMapPdus"),
        ("BELAIR-WRM", "baWrmSsIntervalRxUlMapPdus"),
        ("BELAIR-WRM", "baWrmSsIntervalRxDlFps"),
        ("BELAIR-WRM", "baWrmSsIntervalRngReqSent"),
        ("BELAIR-WRM", "baWrmSsIntervalRngRspReceived"),
        ("BELAIR-WRM", "baWrmSsTotalRxDlMapPdus"),
        ("BELAIR-WRM", "baWrmSsTotalRxUlMapPdus"),
        ("BELAIR-WRM", "baWrmSsTotalRxDlFps"),
        ("BELAIR-WRM", "baWrmSsTotalRngReqSent"),
        ("BELAIR-WRM", "baWrmSsTotalRngRspReceived"),
        ("BELAIR-WRM", "baWrmPeerMacAddress"),
        ("BELAIR-WRM", "baWrmLinkRssi"),
        ("BELAIR-WRM", "baWrmLinkModulationType"),
        ("BELAIR-WRM", "baWrmLinkCinr"),
        ("BELAIR-WRM", "baWrmIfFrameSize"),
        ("BELAIR-WRM", "baWrmIfModulationType"),
        ("BELAIR-WRM", "baWrmIfAntennaGain"),
        ("BELAIR-WRM", "baWrmIfLinkDistance"),
        ("BELAIR-WRM", "baWrmIfTxPower"),
        ("BELAIR-WRM", "baWrmIfTimeElapsed"))
)
if mibBuilder.loadTexts:
    belairWrmObjectGroup.setStatus("current")

belairWrmDeprecatedObjGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 6, 3, 3)
)
belairWrmDeprecatedObjGrp.setObjects(
      *(("BELAIR-WRM", "baWrmIfTxPowerLevel"),
        ("BELAIR-WRM", "baWrmIfAntennaGainLevel"),
        ("BELAIR-WRM", "baWrmTxPower"))
)
if mibBuilder.loadTexts:
    belairWrmDeprecatedObjGrp.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-WRM",
    **{"belairWrmMib": belairWrmMib,
       "belairWrmObjects": belairWrmObjects,
       "baWrmIfConfigTable": baWrmIfConfigTable,
       "baWrmIfConfigEntry": baWrmIfConfigEntry,
       "baWrmIfMode": baWrmIfMode,
       "baWrmIfBsId": baWrmIfBsId,
       "baWrmIfEncryptionType": baWrmIfEncryptionType,
       "baWrmIfEncryptionKey": baWrmIfEncryptionKey,
       "baWrmIfChannelNumber": baWrmIfChannelNumber,
       "baWrmIfChannelBandwidth": baWrmIfChannelBandwidth,
       "baWrmIfTxPowerLevel": baWrmIfTxPowerLevel,
       "baWrmIfAntennaGainLevel": baWrmIfAntennaGainLevel,
       "baWrmIfTimeElapsed": baWrmIfTimeElapsed,
       "baWrmIfFrameSize": baWrmIfFrameSize,
       "baWrmIfModulationType": baWrmIfModulationType,
       "baWrmIfTxPower": baWrmIfTxPower,
       "baWrmIfAntennaGain": baWrmIfAntennaGain,
       "baWrmIfLinkDistance": baWrmIfLinkDistance,
       "baWrmCommonCurrTable": baWrmCommonCurrTable,
       "baWrmCommonCurrEntry": baWrmCommonCurrEntry,
       "baWrmCurrRxBursts": baWrmCurrRxBursts,
       "baWrmCurrRxBurstErrors": baWrmCurrRxBurstErrors,
       "baWrmCurrTxBursts": baWrmCurrTxBursts,
       "baWrmCurrTxBurstErrors": baWrmCurrTxBurstErrors,
       "baWrmCurrRxPdus": baWrmCurrRxPdus,
       "baWrmCurrRxPduErrors": baWrmCurrRxPduErrors,
       "baWrmCurrPduCrcErrors": baWrmCurrPduCrcErrors,
       "baWrmCurrTxPdus": baWrmCurrTxPdus,
       "baWrmCurrTxPduErrors": baWrmCurrTxPduErrors,
       "baWrmCommonIntervalTable": baWrmCommonIntervalTable,
       "baWrmCommonIntervalEntry": baWrmCommonIntervalEntry,
       "baWrmIntervalNumber": baWrmIntervalNumber,
       "baWrmIntervalValid": baWrmIntervalValid,
       "baWrmIntervalRxBursts": baWrmIntervalRxBursts,
       "baWrmIntervalRxBurstErrors": baWrmIntervalRxBurstErrors,
       "baWrmIntervalTxBursts": baWrmIntervalTxBursts,
       "baWrmIntervalTxBurstErrors": baWrmIntervalTxBurstErrors,
       "baWrmIntervalRxPdus": baWrmIntervalRxPdus,
       "baWrmIntervalRxPduErrors": baWrmIntervalRxPduErrors,
       "baWrmIntervalPduCrcErrors": baWrmIntervalPduCrcErrors,
       "baWrmIntervalTxPdus": baWrmIntervalTxPdus,
       "baWrmIntervalTxPduErrors": baWrmIntervalTxPduErrors,
       "baWrmCommonTotalTable": baWrmCommonTotalTable,
       "baWrmCommonTotalEntry": baWrmCommonTotalEntry,
       "baWrmTotalRxBursts": baWrmTotalRxBursts,
       "baWrmTotalRxBurstErrors": baWrmTotalRxBurstErrors,
       "baWrmTotalTxBursts": baWrmTotalTxBursts,
       "baWrmTotalTxBurstErrors": baWrmTotalTxBurstErrors,
       "baWrmTotalRxPdus": baWrmTotalRxPdus,
       "baWrmTotalRxPduErrors": baWrmTotalRxPduErrors,
       "baWrmTotalPduCrcErrors": baWrmTotalPduCrcErrors,
       "baWrmTotalTxPdus": baWrmTotalTxPdus,
       "baWrmTotalTxPduErrors": baWrmTotalTxPduErrors,
       "baWrmBsCurrTable": baWrmBsCurrTable,
       "baWrmBsCurrEntry": baWrmBsCurrEntry,
       "baWrmBsCurrRngReqReceived": baWrmBsCurrRngReqReceived,
       "baWrmBsCurrRngRspSent": baWrmBsCurrRngRspSent,
       "baWrmBsIntervalTable": baWrmBsIntervalTable,
       "baWrmBsIntervalEntry": baWrmBsIntervalEntry,
       "baWrmBsIntervalNumber": baWrmBsIntervalNumber,
       "baWrmBsIntervalValid": baWrmBsIntervalValid,
       "baWrmBsIntervalRngReqReceived": baWrmBsIntervalRngReqReceived,
       "baWrmBsIntervalRngRspSent": baWrmBsIntervalRngRspSent,
       "baWrmBsTotalTable": baWrmBsTotalTable,
       "baWrmBsTotalEntry": baWrmBsTotalEntry,
       "baWrmBsTotalRngReqReceived": baWrmBsTotalRngReqReceived,
       "baWrmBsTotalRngRspSent": baWrmBsTotalRngRspSent,
       "baWrmSsCurrTable": baWrmSsCurrTable,
       "baWrmSsCurrEntry": baWrmSsCurrEntry,
       "baWrmSsCurrRxDlMapPdus": baWrmSsCurrRxDlMapPdus,
       "baWrmSsCurrRxUlMapPdus": baWrmSsCurrRxUlMapPdus,
       "baWrmSsCurrRxDlFps": baWrmSsCurrRxDlFps,
       "baWrmSsCurrRngReqSent": baWrmSsCurrRngReqSent,
       "baWrmSsCurrRngRspReceived": baWrmSsCurrRngRspReceived,
       "baWrmSsIntervalTable": baWrmSsIntervalTable,
       "baWrmSsIntervalEntry": baWrmSsIntervalEntry,
       "baWrmSsIntervalNumber": baWrmSsIntervalNumber,
       "baWrmSsIntervalValid": baWrmSsIntervalValid,
       "baWrmSsIntervalRxDlMapPdus": baWrmSsIntervalRxDlMapPdus,
       "baWrmSsIntervalRxUlMapPdus": baWrmSsIntervalRxUlMapPdus,
       "baWrmSsIntervalRxDlFps": baWrmSsIntervalRxDlFps,
       "baWrmSsIntervalRngReqSent": baWrmSsIntervalRngReqSent,
       "baWrmSsIntervalRngRspReceived": baWrmSsIntervalRngRspReceived,
       "baWrmSsTotalTable": baWrmSsTotalTable,
       "baWrmSsTotalEntry": baWrmSsTotalEntry,
       "baWrmSsTotalRxDlMapPdus": baWrmSsTotalRxDlMapPdus,
       "baWrmSsTotalRxUlMapPdus": baWrmSsTotalRxUlMapPdus,
       "baWrmSsTotalRxDlFps": baWrmSsTotalRxDlFps,
       "baWrmSsTotalRngReqSent": baWrmSsTotalRngReqSent,
       "baWrmSsTotalRngRspReceived": baWrmSsTotalRngRspReceived,
       "baWrmLinkInfoTable": baWrmLinkInfoTable,
       "baWrmLinkInfoEntry": baWrmLinkInfoEntry,
       "baWrmLinkIndex": baWrmLinkIndex,
       "baWrmPeerMacAddress": baWrmPeerMacAddress,
       "baWrmLinkRssi": baWrmLinkRssi,
       "baWrmLinkCinr": baWrmLinkCinr,
       "baWrmLinkModulationType": baWrmLinkModulationType,
       "baWrmTxPowerTable": baWrmTxPowerTable,
       "baWrmTxPowerEntry": baWrmTxPowerEntry,
       "baWrmTxPowerLevel": baWrmTxPowerLevel,
       "baWrmTxPower": baWrmTxPower,
       "belairWrmTraps": belairWrmTraps,
       "belairWrmConformance": belairWrmConformance,
       "belairWrmObjectGroup": belairWrmObjectGroup,
       "belairWrmDeprecatedObjGrp": belairWrmDeprecatedObjGrp}
)
