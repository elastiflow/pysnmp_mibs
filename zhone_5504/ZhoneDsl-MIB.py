# SNMP MIB module (ZhoneDsl-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/phyDsl.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:10:21 2025
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

(adslLineEntry,) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslLineEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zhoneDsl,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneDsl",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneDslMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 3)
)
if mibBuilder.loadTexts:
    zhoneDslMib.setRevisions(
        ("2002-09-06 13:37",
         "2002-07-08 12:35",
         "2002-06-06 13:13",
         "2002-04-01 10:47",
         "2002-03-20 12:23",
         "2002-02-11 10:00",
         "2001-11-20 02:40",
         "2001-10-10 10:47",
         "2001-03-06 21:13",
         "2000-12-27 11:27",
         "2000-12-01 11:50",
         "2000-11-17 16:05",
         "2000-11-17 10:19",
         "2000-09-21 11:30",
         "2000-09-12 13:14")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneDslLineTable_Object = MibTable
zhoneDslLineTable = _ZhoneDslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1)
)
if mibBuilder.loadTexts:
    zhoneDslLineTable.setStatus("current")
_ZhoneDslLineEntry_Object = MibTableRow
zhoneDslLineEntry = _ZhoneDslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1)
)
zhoneDslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneDslLineEntry.setStatus("current")


class _ZhoneDslLineType_Type(Integer32):
    """Custom type zhoneDslLineType based on Integer32"""
    defaultValue = 3

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
        *(("hdsl2", 1),
          ("shdsl", 2),
          ("sdsl", 3),
          ("adsl", 4),
          ("shdsllatest", 5),
          ("sdsllatest", 6))
    )


_ZhoneDslLineType_Type.__name__ = "Integer32"
_ZhoneDslLineType_Object = MibTableColumn
zhoneDslLineType = _ZhoneDslLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 1),
    _ZhoneDslLineType_Type()
)
zhoneDslLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDslLineType.setStatus("current")


class _ZhoneDslLineCapabilities_Type(Bits):
    """Custom type zhoneDslLineCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("hdsl2", 0),
          ("shdsl", 1),
          ("sdsl", 2),
          ("adsl", 3),
          ("shdsllatest", 4),
          ("sdsllatest", 5))
    )

_ZhoneDslLineCapabilities_Type.__name__ = "Bits"
_ZhoneDslLineCapabilities_Object = MibTableColumn
zhoneDslLineCapabilities = _ZhoneDslLineCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 2),
    _ZhoneDslLineCapabilities_Type()
)
zhoneDslLineCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslLineCapabilities.setStatus("current")


class _ZhoneDslConfigUnitMode_Type(Integer32):
    """Custom type zhoneDslConfigUnitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("co", 1),
          ("cpe", 2))
    )


_ZhoneDslConfigUnitMode_Type.__name__ = "Integer32"
_ZhoneDslConfigUnitMode_Object = MibTableColumn
zhoneDslConfigUnitMode = _ZhoneDslConfigUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 3),
    _ZhoneDslConfigUnitMode_Type()
)
zhoneDslConfigUnitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDslConfigUnitMode.setStatus("current")


class _ZhoneDslTipRingStatus_Type(Integer32):
    """Custom type zhoneDslTipRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reverse", 2))
    )


_ZhoneDslTipRingStatus_Type.__name__ = "Integer32"
_ZhoneDslTipRingStatus_Object = MibTableColumn
zhoneDslTipRingStatus = _ZhoneDslTipRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 4),
    _ZhoneDslTipRingStatus_Type()
)
zhoneDslTipRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslTipRingStatus.setStatus("current")


class _ZhoneDslLineStatus_Type(Integer32):
    """Custom type zhoneDslLineStatus based on Integer32"""
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
        *(("down", 1),
          ("downloading", 2),
          ("activated", 3),
          ("training", 4),
          ("up", 5),
          ("test", 6))
    )


_ZhoneDslLineStatus_Type.__name__ = "Integer32"
_ZhoneDslLineStatus_Object = MibTableColumn
zhoneDslLineStatus = _ZhoneDslLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 5),
    _ZhoneDslLineStatus_Type()
)
zhoneDslLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslLineStatus.setStatus("current")
_ZhoneDslUpLineRate_Type = Integer32
_ZhoneDslUpLineRate_Object = MibTableColumn
zhoneDslUpLineRate = _ZhoneDslUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 6),
    _ZhoneDslUpLineRate_Type()
)
zhoneDslUpLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslUpLineRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslUpLineRate.setUnits("bps")
_ZhoneDslDownLineRate_Type = Integer32
_ZhoneDslDownLineRate_Object = MibTableColumn
zhoneDslDownLineRate = _ZhoneDslDownLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 7),
    _ZhoneDslDownLineRate_Type()
)
zhoneDslDownLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslDownLineRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslDownLineRate.setUnits("bps")


class _ZhoneDslConfigProfName_Type(ZhoneAdminString):
    """Custom type zhoneDslConfigProfName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ZhoneDslConfigProfName_Type.__name__ = "ZhoneAdminString"
_ZhoneDslConfigProfName_Object = MibTableColumn
zhoneDslConfigProfName = _ZhoneDslConfigProfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 8),
    _ZhoneDslConfigProfName_Type()
)
zhoneDslConfigProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDslConfigProfName.setStatus("current")


class _ZhoneDslAlarmProfName_Type(ZhoneAdminString):
    """Custom type zhoneDslAlarmProfName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ZhoneDslAlarmProfName_Type.__name__ = "ZhoneAdminString"
_ZhoneDslAlarmProfName_Object = MibTableColumn
zhoneDslAlarmProfName = _ZhoneDslAlarmProfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 9),
    _ZhoneDslAlarmProfName_Type()
)
zhoneDslAlarmProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDslAlarmProfName.setStatus("current")
_ZhoneDslMaxAttainableUpLineRate_Type = Integer32
_ZhoneDslMaxAttainableUpLineRate_Object = MibTableColumn
zhoneDslMaxAttainableUpLineRate = _ZhoneDslMaxAttainableUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 10),
    _ZhoneDslMaxAttainableUpLineRate_Type()
)
zhoneDslMaxAttainableUpLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslMaxAttainableUpLineRate.setStatus("current")
_ZhoneDslMaxAttainableDownLineRate_Type = Integer32
_ZhoneDslMaxAttainableDownLineRate_Object = MibTableColumn
zhoneDslMaxAttainableDownLineRate = _ZhoneDslMaxAttainableDownLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 11),
    _ZhoneDslMaxAttainableDownLineRate_Type()
)
zhoneDslMaxAttainableDownLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslMaxAttainableDownLineRate.setStatus("current")
_ZhoneDslLineSnrMgn_Type = Integer32
_ZhoneDslLineSnrMgn_Object = MibTableColumn
zhoneDslLineSnrMgn = _ZhoneDslLineSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 12),
    _ZhoneDslLineSnrMgn_Type()
)
zhoneDslLineSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslLineSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslLineSnrMgn.setUnits("tenths dB")
_ZhoneDslLineAtn_Type = Integer32
_ZhoneDslLineAtn_Object = MibTableColumn
zhoneDslLineAtn = _ZhoneDslLineAtn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 13),
    _ZhoneDslLineAtn_Type()
)
zhoneDslLineAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslLineAtn.setUnits("tenths dB")


class _ZhoneDslLineAlarmStatus_Type(Bits):
    """Custom type zhoneDslLineAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("powerBackoff", 1),
          ("deviceFault", 2),
          ("dcContinuityFault", 3),
          ("snrMarginAlarm", 4),
          ("loopAttenuationAlarm", 5),
          ("loswFailureAlarm", 6),
          ("configInitFailure", 7),
          ("protocolInitFailure", 8),
          ("noNeighborPresent", 9),
          ("loopBackActive", 10))
    )

_ZhoneDslLineAlarmStatus_Type.__name__ = "Bits"
_ZhoneDslLineAlarmStatus_Object = MibTableColumn
zhoneDslLineAlarmStatus = _ZhoneDslLineAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 14),
    _ZhoneDslLineAlarmStatus_Type()
)
zhoneDslLineAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslLineAlarmStatus.setStatus("current")


class _ZhoneDslLineStatusChangeTrapEnable_Type(Integer32):
    """Custom type zhoneDslLineStatusChangeTrapEnable based on Integer32"""
    defaultValue = 1

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


_ZhoneDslLineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_ZhoneDslLineStatusChangeTrapEnable_Object = MibTableColumn
zhoneDslLineStatusChangeTrapEnable = _ZhoneDslLineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 15),
    _ZhoneDslLineStatusChangeTrapEnable_Type()
)
zhoneDslLineStatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDslLineStatusChangeTrapEnable.setStatus("current")


class _ZhoneDslLineCurrOutputPwr_Type(Integer32):
    """Custom type zhoneDslLineCurrOutputPwr based on Integer32"""
    defaultValue = 0


_ZhoneDslLineCurrOutputPwr_Type.__name__ = "Integer32"
_ZhoneDslLineCurrOutputPwr_Object = MibTableColumn
zhoneDslLineCurrOutputPwr = _ZhoneDslLineCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 16),
    _ZhoneDslLineCurrOutputPwr_Type()
)
zhoneDslLineCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslLineCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslLineCurrOutputPwr.setUnits("tenths dBm")
_ZhoneHdsl2ConfigProfileTable_Object = MibTable
zhoneHdsl2ConfigProfileTable = _ZhoneHdsl2ConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2)
)
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigProfileTable.setStatus("current")
_ZhoneHdsl2ConfigProfileEntry_Object = MibTableRow
zhoneHdsl2ConfigProfileEntry = _ZhoneHdsl2ConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2, 1)
)
zhoneHdsl2ConfigProfileEntry.setIndexNames(
    (1, "ZhoneDsl-MIB", "zhoneHdsl2ConfigProfileName"),
)
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigProfileEntry.setStatus("current")


class _ZhoneHdsl2ConfigProfileName_Type(ZhoneAdminString):
    """Custom type zhoneHdsl2ConfigProfileName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ZhoneHdsl2ConfigProfileName_Type.__name__ = "ZhoneAdminString"
_ZhoneHdsl2ConfigProfileName_Object = MibTableColumn
zhoneHdsl2ConfigProfileName = _ZhoneHdsl2ConfigProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2, 1, 1),
    _ZhoneHdsl2ConfigProfileName_Type()
)
zhoneHdsl2ConfigProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigProfileName.setStatus("current")


class _ZhoneHdsl2ConfigTransmitPowerBackoffMode_Type(Integer32):
    """Custom type zhoneHdsl2ConfigTransmitPowerBackoffMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backoffDisable", 1),
          ("backoffEnable", 2),
          ("noChangeBackoff", 3))
    )


_ZhoneHdsl2ConfigTransmitPowerBackoffMode_Type.__name__ = "Integer32"
_ZhoneHdsl2ConfigTransmitPowerBackoffMode_Object = MibTableColumn
zhoneHdsl2ConfigTransmitPowerBackoffMode = _ZhoneHdsl2ConfigTransmitPowerBackoffMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2, 1, 2),
    _ZhoneHdsl2ConfigTransmitPowerBackoffMode_Type()
)
zhoneHdsl2ConfigTransmitPowerBackoffMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigTransmitPowerBackoffMode.setStatus("current")


class _ZhoneHdsl2ConfigDecoderCoeffA_Type(Integer32):
    """Custom type zhoneHdsl2ConfigDecoderCoeffA based on Integer32"""
    defaultValue = 366

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_ZhoneHdsl2ConfigDecoderCoeffA_Type.__name__ = "Integer32"
_ZhoneHdsl2ConfigDecoderCoeffA_Object = MibTableColumn
zhoneHdsl2ConfigDecoderCoeffA = _ZhoneHdsl2ConfigDecoderCoeffA_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2, 1, 3),
    _ZhoneHdsl2ConfigDecoderCoeffA_Type()
)
zhoneHdsl2ConfigDecoderCoeffA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigDecoderCoeffA.setStatus("current")


class _ZhoneHdsl2ConfigDecoderCoeffB_Type(Integer32):
    """Custom type zhoneHdsl2ConfigDecoderCoeffB based on Integer32"""
    defaultValue = 817

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_ZhoneHdsl2ConfigDecoderCoeffB_Type.__name__ = "Integer32"
_ZhoneHdsl2ConfigDecoderCoeffB_Object = MibTableColumn
zhoneHdsl2ConfigDecoderCoeffB = _ZhoneHdsl2ConfigDecoderCoeffB_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2, 1, 4),
    _ZhoneHdsl2ConfigDecoderCoeffB_Type()
)
zhoneHdsl2ConfigDecoderCoeffB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigDecoderCoeffB.setStatus("current")


class _ZhoneHdsl2ConfigFrameSyncWord_Type(Integer32):
    """Custom type zhoneHdsl2ConfigFrameSyncWord based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZhoneHdsl2ConfigFrameSyncWord_Type.__name__ = "Integer32"
_ZhoneHdsl2ConfigFrameSyncWord_Object = MibTableColumn
zhoneHdsl2ConfigFrameSyncWord = _ZhoneHdsl2ConfigFrameSyncWord_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2, 1, 5),
    _ZhoneHdsl2ConfigFrameSyncWord_Type()
)
zhoneHdsl2ConfigFrameSyncWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigFrameSyncWord.setStatus("current")


class _ZhoneHdsl2ConfigStuffBits_Type(Integer32):
    """Custom type zhoneHdsl2ConfigStuffBits based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZhoneHdsl2ConfigStuffBits_Type.__name__ = "Integer32"
_ZhoneHdsl2ConfigStuffBits_Object = MibTableColumn
zhoneHdsl2ConfigStuffBits = _ZhoneHdsl2ConfigStuffBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2, 1, 6),
    _ZhoneHdsl2ConfigStuffBits_Type()
)
zhoneHdsl2ConfigStuffBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigStuffBits.setStatus("current")
_ZhoneHdsl2ConfigRowStatus_Type = ZhoneRowStatus
_ZhoneHdsl2ConfigRowStatus_Object = MibTableColumn
zhoneHdsl2ConfigRowStatus = _ZhoneHdsl2ConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 2, 1, 7),
    _ZhoneHdsl2ConfigRowStatus_Type()
)
zhoneHdsl2ConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigRowStatus.setStatus("current")
_ZhoneSdslConfigProfileTable_Object = MibTable
zhoneSdslConfigProfileTable = _ZhoneSdslConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3)
)
if mibBuilder.loadTexts:
    zhoneSdslConfigProfileTable.setStatus("current")
_ZhoneSdslConfigProfileEntry_Object = MibTableRow
zhoneSdslConfigProfileEntry = _ZhoneSdslConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1)
)
zhoneSdslConfigProfileEntry.setIndexNames(
    (1, "ZhoneDsl-MIB", "zhoneSdslConfigProfileName"),
)
if mibBuilder.loadTexts:
    zhoneSdslConfigProfileEntry.setStatus("current")


class _ZhoneSdslConfigProfileName_Type(ZhoneAdminString):
    """Custom type zhoneSdslConfigProfileName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ZhoneSdslConfigProfileName_Type.__name__ = "ZhoneAdminString"
_ZhoneSdslConfigProfileName_Object = MibTableColumn
zhoneSdslConfigProfileName = _ZhoneSdslConfigProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 1),
    _ZhoneSdslConfigProfileName_Type()
)
zhoneSdslConfigProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneSdslConfigProfileName.setStatus("current")


class _ZhoneSdslConfigLineRate_Type(Integer32):
    """Custom type zhoneSdslConfigLineRate based on Integer32"""
    defaultValue = 24

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
              16,
              17,
              18,
              19,
              20,
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
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84)
        )
    )
    namedValues = NamedValues(
        *(("line-rate-144kbps", 1),
          ("line-rate-160kbps", 2),
          ("line-rate-192kbps", 3),
          ("line-rate-208kbps", 4),
          ("line-rate-224kbps", 5),
          ("line-rate-256kbps", 6),
          ("line-rate-272kbps", 7),
          ("line-rate-320kbps", 8),
          ("line-rate-368kbps", 9),
          ("line-rate-384kbps", 10),
          ("line-rate-400kbps", 11),
          ("line-rate-416kbps", 12),
          ("line-rate-528kbps", 13),
          ("line-rate-768kbps", 14),
          ("line-rate-784kbps", 16),
          ("line-rate-1040kbps", 17),
          ("line-rate-1152kbps", 18),
          ("line-rate-1168kbps", 19),
          ("line-rate-1536kbps", 20),
          ("line-rate-1552kbps", 22),
          ("line-rate-1568kbps", 23),
          ("line-rate-2320kbps", 24),
          ("line-rate-176kbps", 25),
          ("line-rate-240kbps", 26),
          ("line-rate-288kbps", 27),
          ("line-rate-304kbps", 28),
          ("line-rate-336kbps", 29),
          ("line-rate-352kbps", 30),
          ("line-rate-432kbps", 31),
          ("line-rate-464kbps", 32),
          ("line-rate-496kbps", 33),
          ("line-rate-560kbps", 34),
          ("line-rate-592kbps", 35),
          ("line-rate-624kbps", 36),
          ("line-rate-656kbps", 37),
          ("line-rate-688kbps", 38),
          ("line-rate-720kbps", 39),
          ("line-rate-752kbps", 40),
          ("line-rate-816kbps", 41),
          ("line-rate-848kbps", 42),
          ("line-rate-880kbps", 43),
          ("line-rate-912kbps", 44),
          ("line-rate-944kbps", 45),
          ("line-rate-976kbps", 46),
          ("line-rate-1008kbps", 47),
          ("line-rate-1072kbps", 48),
          ("line-rate-1104kbps", 49),
          ("line-rate-1136kbps", 50),
          ("line-rate-1200kbps", 51),
          ("line-rate-1232kbps", 52),
          ("line-rate-1264kbps", 53),
          ("line-rate-1296kbps", 54),
          ("line-rate-1328kbps", 55),
          ("line-rate-1360kbps", 56),
          ("line-rate-1392kbps", 57),
          ("line-rate-1424kbps", 58),
          ("line-rate-1456kbps", 59),
          ("line-rate-1488kbps", 60),
          ("line-rate-1520kbps", 61),
          ("line-rate-1584kbps", 62),
          ("line-rate-1616kbps", 63),
          ("line-rate-1648kbps", 64),
          ("line-rate-1680kbps", 65),
          ("line-rate-1712kbps", 66),
          ("line-rate-1744kbps", 67),
          ("line-rate-1776kbps", 68),
          ("line-rate-1808kbps", 69),
          ("line-rate-1840kbps", 70),
          ("line-rate-1872kbps", 71),
          ("line-rate-1904kbps", 72),
          ("line-rate-1936kbps", 73),
          ("line-rate-1968kbps", 74),
          ("line-rate-2000kbps", 75),
          ("line-rate-2032kbps", 76),
          ("line-rate-2064kbps", 77),
          ("line-rate-2096kbps", 78),
          ("line-rate-2128kbps", 79),
          ("line-rate-2160kbps", 80),
          ("line-rate-2192kbps", 81),
          ("line-rate-2224kbps", 82),
          ("line-rate-2256kbps", 83),
          ("line-rate-2288kbps", 84))
    )


_ZhoneSdslConfigLineRate_Type.__name__ = "Integer32"
_ZhoneSdslConfigLineRate_Object = MibTableColumn
zhoneSdslConfigLineRate = _ZhoneSdslConfigLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 2),
    _ZhoneSdslConfigLineRate_Type()
)
zhoneSdslConfigLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSdslConfigLineRate.setStatus("current")


class _ZhoneSdslConfigFixBitRate_Type(Integer32):
    """Custom type zhoneSdslConfigFixBitRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-bit-enable", 1),
          ("fix-bit-disable", 2))
    )


_ZhoneSdslConfigFixBitRate_Type.__name__ = "Integer32"
_ZhoneSdslConfigFixBitRate_Object = MibTableColumn
zhoneSdslConfigFixBitRate = _ZhoneSdslConfigFixBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 3),
    _ZhoneSdslConfigFixBitRate_Type()
)
zhoneSdslConfigFixBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSdslConfigFixBitRate.setStatus("current")


class _ZhoneSdslConfigConnectMode_Type(Integer32):
    """Custom type zhoneSdslConfigConnectMode based on Integer32"""
    defaultValue = 4

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
        *(("basic-2b1q-mode", 1),
          ("globespan-neg-mode", 2),
          ("copper-mtn-mode", 3),
          ("flowpoint-mode", 4))
    )


_ZhoneSdslConfigConnectMode_Type.__name__ = "Integer32"
_ZhoneSdslConfigConnectMode_Object = MibTableColumn
zhoneSdslConfigConnectMode = _ZhoneSdslConfigConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 4),
    _ZhoneSdslConfigConnectMode_Type()
)
zhoneSdslConfigConnectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSdslConfigConnectMode.setStatus("current")


class _ZhoneSdslConfigNTR_Type(Integer32):
    """Custom type zhoneSdslConfigNTR based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntr-disable", 1),
          ("ntr-enable", 2))
    )


_ZhoneSdslConfigNTR_Type.__name__ = "Integer32"
_ZhoneSdslConfigNTR_Object = MibTableColumn
zhoneSdslConfigNTR = _ZhoneSdslConfigNTR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 5),
    _ZhoneSdslConfigNTR_Type()
)
zhoneSdslConfigNTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSdslConfigNTR.setStatus("current")


class _ZhoneSdslConfigFramerType_Type(Integer32):
    """Custom type zhoneSdslConfigFramerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm-clear-channel", 1),
          ("atm-dlcc", 2),
          ("atm-g991-1", 3))
    )


_ZhoneSdslConfigFramerType_Type.__name__ = "Integer32"
_ZhoneSdslConfigFramerType_Object = MibTableColumn
zhoneSdslConfigFramerType = _ZhoneSdslConfigFramerType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 6),
    _ZhoneSdslConfigFramerType_Type()
)
zhoneSdslConfigFramerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSdslConfigFramerType.setStatus("current")


class _ZhoneSdslConfigPowerScale_Type(Integer32):
    """Custom type zhoneSdslConfigPowerScale based on Integer32"""
    defaultValue = 29952

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_ZhoneSdslConfigPowerScale_Type.__name__ = "Integer32"
_ZhoneSdslConfigPowerScale_Object = MibTableColumn
zhoneSdslConfigPowerScale = _ZhoneSdslConfigPowerScale_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 7),
    _ZhoneSdslConfigPowerScale_Type()
)
zhoneSdslConfigPowerScale.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSdslConfigPowerScale.setStatus("current")
_ZhoneSdslConfigRowStatus_Type = ZhoneRowStatus
_ZhoneSdslConfigRowStatus_Object = MibTableColumn
zhoneSdslConfigRowStatus = _ZhoneSdslConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 8),
    _ZhoneSdslConfigRowStatus_Type()
)
zhoneSdslConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSdslConfigRowStatus.setStatus("current")
_ZhoneHdsl2StatusTable_Object = MibTable
zhoneHdsl2StatusTable = _ZhoneHdsl2StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4)
)
if mibBuilder.loadTexts:
    zhoneHdsl2StatusTable.setStatus("current")
_ZhoneHdsl2StatusEntry_Object = MibTableRow
zhoneHdsl2StatusEntry = _ZhoneHdsl2StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1)
)
zhoneHdsl2StatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneHdsl2StatusEntry.setStatus("current")


class _ZhoneHdsl2DriftAlarm_Type(Integer32):
    """Custom type zhoneHdsl2DriftAlarm based on Integer32"""
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
        *(("rxClkAlarm", 1),
          ("txClkAlarm", 2),
          ("txRxClkAlarm", 3),
          ("noDriftAlarm", 4),
          ("notApplicable", 5))
    )


_ZhoneHdsl2DriftAlarm_Type.__name__ = "Integer32"
_ZhoneHdsl2DriftAlarm_Object = MibTableColumn
zhoneHdsl2DriftAlarm = _ZhoneHdsl2DriftAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 1),
    _ZhoneHdsl2DriftAlarm_Type()
)
zhoneHdsl2DriftAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2DriftAlarm.setStatus("current")


class _ZhoneHdsl2FramerIBStatus_Type(OctetString):
    """Custom type zhoneHdsl2FramerIBStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_ZhoneHdsl2FramerIBStatus_Type.__name__ = "OctetString"
_ZhoneHdsl2FramerIBStatus_Object = MibTableColumn
zhoneHdsl2FramerIBStatus = _ZhoneHdsl2FramerIBStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 2),
    _ZhoneHdsl2FramerIBStatus_Type()
)
zhoneHdsl2FramerIBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2FramerIBStatus.setStatus("current")
_ZhoneHdsl2LocalPSDMaskStatus_Type = Integer32
_ZhoneHdsl2LocalPSDMaskStatus_Object = MibTableColumn
zhoneHdsl2LocalPSDMaskStatus = _ZhoneHdsl2LocalPSDMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 3),
    _ZhoneHdsl2LocalPSDMaskStatus_Type()
)
zhoneHdsl2LocalPSDMaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2LocalPSDMaskStatus.setStatus("current")
_ZhoneHdsl2LoopAttenuation_Type = Integer32
_ZhoneHdsl2LoopAttenuation_Object = MibTableColumn
zhoneHdsl2LoopAttenuation = _ZhoneHdsl2LoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 4),
    _ZhoneHdsl2LoopAttenuation_Type()
)
zhoneHdsl2LoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2LoopAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    zhoneHdsl2LoopAttenuation.setUnits("tenth DB")


class _ZhoneHdsl2LossWordStatus_Type(Integer32):
    """Custom type zhoneHdsl2LossWordStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLosswDefect", 1),
          ("losswDefect", 2))
    )


_ZhoneHdsl2LossWordStatus_Type.__name__ = "Integer32"
_ZhoneHdsl2LossWordStatus_Object = MibTableColumn
zhoneHdsl2LossWordStatus = _ZhoneHdsl2LossWordStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 5),
    _ZhoneHdsl2LossWordStatus_Type()
)
zhoneHdsl2LossWordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2LossWordStatus.setStatus("current")
_ZhoneHdsl2RmtPSDMaskStatus_Type = Integer32
_ZhoneHdsl2RmtPSDMaskStatus_Object = MibTableColumn
zhoneHdsl2RmtPSDMaskStatus = _ZhoneHdsl2RmtPSDMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 6),
    _ZhoneHdsl2RmtPSDMaskStatus_Type()
)
zhoneHdsl2RmtPSDMaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtPSDMaskStatus.setStatus("current")
_ZhoneHdsl2RmtCountryCode_Type = Integer32
_ZhoneHdsl2RmtCountryCode_Object = MibTableColumn
zhoneHdsl2RmtCountryCode = _ZhoneHdsl2RmtCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 7),
    _ZhoneHdsl2RmtCountryCode_Type()
)
zhoneHdsl2RmtCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtCountryCode.setStatus("current")
_ZhoneHdsl2RmtVersion_Type = Integer32
_ZhoneHdsl2RmtVersion_Object = MibTableColumn
zhoneHdsl2RmtVersion = _ZhoneHdsl2RmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 8),
    _ZhoneHdsl2RmtVersion_Type()
)
zhoneHdsl2RmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtVersion.setStatus("current")
_ZhoneHdsl2RmtProviderCode_Type = Integer32
_ZhoneHdsl2RmtProviderCode_Object = MibTableColumn
zhoneHdsl2RmtProviderCode = _ZhoneHdsl2RmtProviderCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 9),
    _ZhoneHdsl2RmtProviderCode_Type()
)
zhoneHdsl2RmtProviderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtProviderCode.setStatus("current")


class _ZhoneHdsl2RmtVendorData_Type(OctetString):
    """Custom type zhoneHdsl2RmtVendorData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZhoneHdsl2RmtVendorData_Type.__name__ = "OctetString"
_ZhoneHdsl2RmtVendorData_Object = MibTableColumn
zhoneHdsl2RmtVendorData = _ZhoneHdsl2RmtVendorData_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 10),
    _ZhoneHdsl2RmtVendorData_Type()
)
zhoneHdsl2RmtVendorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtVendorData.setStatus("current")


class _ZhoneHdsl2RmtTxEncoderA_Type(Integer32):
    """Custom type zhoneHdsl2RmtTxEncoderA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_ZhoneHdsl2RmtTxEncoderA_Type.__name__ = "Integer32"
_ZhoneHdsl2RmtTxEncoderA_Object = MibTableColumn
zhoneHdsl2RmtTxEncoderA = _ZhoneHdsl2RmtTxEncoderA_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 11),
    _ZhoneHdsl2RmtTxEncoderA_Type()
)
zhoneHdsl2RmtTxEncoderA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtTxEncoderA.setStatus("current")


class _ZhoneHdsl2RmtTxEncoderB_Type(Integer32):
    """Custom type zhoneHdsl2RmtTxEncoderB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_ZhoneHdsl2RmtTxEncoderB_Type.__name__ = "Integer32"
_ZhoneHdsl2RmtTxEncoderB_Object = MibTableColumn
zhoneHdsl2RmtTxEncoderB = _ZhoneHdsl2RmtTxEncoderB_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 12),
    _ZhoneHdsl2RmtTxEncoderB_Type()
)
zhoneHdsl2RmtTxEncoderB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtTxEncoderB.setStatus("current")


class _ZhoneHdsl2FrameSyncWord_Type(Integer32):
    """Custom type zhoneHdsl2FrameSyncWord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZhoneHdsl2FrameSyncWord_Type.__name__ = "Integer32"
_ZhoneHdsl2FrameSyncWord_Object = MibTableColumn
zhoneHdsl2FrameSyncWord = _ZhoneHdsl2FrameSyncWord_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 13),
    _ZhoneHdsl2FrameSyncWord_Type()
)
zhoneHdsl2FrameSyncWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2FrameSyncWord.setStatus("current")


class _ZhoneHdsl2StuffBits_Type(Integer32):
    """Custom type zhoneHdsl2StuffBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZhoneHdsl2StuffBits_Type.__name__ = "Integer32"
_ZhoneHdsl2StuffBits_Object = MibTableColumn
zhoneHdsl2StuffBits = _ZhoneHdsl2StuffBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 14),
    _ZhoneHdsl2StuffBits_Type()
)
zhoneHdsl2StuffBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2StuffBits.setStatus("current")
_ZhoneSdslStatusTable_Object = MibTable
zhoneSdslStatusTable = _ZhoneSdslStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5)
)
if mibBuilder.loadTexts:
    zhoneSdslStatusTable.setStatus("current")
_ZhoneSdslStatusEntry_Object = MibTableRow
zhoneSdslStatusEntry = _ZhoneSdslStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1)
)
zhoneSdslStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneSdslStatusEntry.setStatus("current")


class _ZhoneSdslFixBitStatus_Type(Integer32):
    """Custom type zhoneSdslFixBitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-bit-enable", 1),
          ("fix-bit-disable", 2))
    )


_ZhoneSdslFixBitStatus_Type.__name__ = "Integer32"
_ZhoneSdslFixBitStatus_Object = MibTableColumn
zhoneSdslFixBitStatus = _ZhoneSdslFixBitStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 1),
    _ZhoneSdslFixBitStatus_Type()
)
zhoneSdslFixBitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSdslFixBitStatus.setStatus("current")
_ZhoneSdslDSPVersion_Type = Integer32
_ZhoneSdslDSPVersion_Object = MibTableColumn
zhoneSdslDSPVersion = _ZhoneSdslDSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 2),
    _ZhoneSdslDSPVersion_Type()
)
zhoneSdslDSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSdslDSPVersion.setStatus("current")


class _ZhoneSdslFirmwareVersion_Type(OctetString):
    """Custom type zhoneSdslFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ZhoneSdslFirmwareVersion_Type.__name__ = "OctetString"
_ZhoneSdslFirmwareVersion_Object = MibTableColumn
zhoneSdslFirmwareVersion = _ZhoneSdslFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 3),
    _ZhoneSdslFirmwareVersion_Type()
)
zhoneSdslFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSdslFirmwareVersion.setStatus("current")
_ZhoneDslPerfDataTotalTable_Object = MibTable
zhoneDslPerfDataTotalTable = _ZhoneDslPerfDataTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6)
)
if mibBuilder.loadTexts:
    zhoneDslPerfDataTotalTable.setStatus("current")
_ZhoneDslPerfDataTotalEntry_Object = MibTableRow
zhoneDslPerfDataTotalEntry = _ZhoneDslPerfDataTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1)
)
if mibBuilder.loadTexts:
    zhoneDslPerfDataTotalEntry.setStatus("current")
_ZhoneDslPerfTotalLofs_Type = Counter32
_ZhoneDslPerfTotalLofs_Object = MibTableColumn
zhoneDslPerfTotalLofs = _ZhoneDslPerfTotalLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 1),
    _ZhoneDslPerfTotalLofs_Type()
)
zhoneDslPerfTotalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalLofs.setStatus("current")
_ZhoneDslPerfTotalLoss_Type = Counter32
_ZhoneDslPerfTotalLoss_Object = MibTableColumn
zhoneDslPerfTotalLoss = _ZhoneDslPerfTotalLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 2),
    _ZhoneDslPerfTotalLoss_Type()
)
zhoneDslPerfTotalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalLoss.setStatus("current")
_ZhoneDslPerfTotalLols_Type = Counter32
_ZhoneDslPerfTotalLols_Object = MibTableColumn
zhoneDslPerfTotalLols = _ZhoneDslPerfTotalLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 3),
    _ZhoneDslPerfTotalLols_Type()
)
zhoneDslPerfTotalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalLols.setStatus("current")
_ZhoneDslPerfTotalInits_Type = Counter32
_ZhoneDslPerfTotalInits_Object = MibTableColumn
zhoneDslPerfTotalInits = _ZhoneDslPerfTotalInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 4),
    _ZhoneDslPerfTotalInits_Type()
)
zhoneDslPerfTotalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalInits.setStatus("current")
_ZhoneDslPerfTotalES_Type = Counter32
_ZhoneDslPerfTotalES_Object = MibTableColumn
zhoneDslPerfTotalES = _ZhoneDslPerfTotalES_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 5),
    _ZhoneDslPerfTotalES_Type()
)
zhoneDslPerfTotalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalES.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalES.setUnits("seconds")
_ZhoneDslPerfTotalSES_Type = Counter32
_ZhoneDslPerfTotalSES_Object = MibTableColumn
zhoneDslPerfTotalSES = _ZhoneDslPerfTotalSES_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 6),
    _ZhoneDslPerfTotalSES_Type()
)
zhoneDslPerfTotalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalSES.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalSES.setUnits("seconds")
_ZhoneDslPerfTotalCRCAnomalies_Type = Counter32
_ZhoneDslPerfTotalCRCAnomalies_Object = MibTableColumn
zhoneDslPerfTotalCRCAnomalies = _ZhoneDslPerfTotalCRCAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 7),
    _ZhoneDslPerfTotalCRCAnomalies_Type()
)
zhoneDslPerfTotalCRCAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalCRCAnomalies.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalCRCAnomalies.setUnits("seconds")
_ZhoneDslPerfTotalLOSWS_Type = Counter32
_ZhoneDslPerfTotalLOSWS_Object = MibTableColumn
zhoneDslPerfTotalLOSWS = _ZhoneDslPerfTotalLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 8),
    _ZhoneDslPerfTotalLOSWS_Type()
)
zhoneDslPerfTotalLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalLOSWS.setUnits("seconds")
_ZhoneDslPerfTotalUAS_Type = Counter32
_ZhoneDslPerfTotalUAS_Object = MibTableColumn
zhoneDslPerfTotalUAS = _ZhoneDslPerfTotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 9),
    _ZhoneDslPerfTotalUAS_Type()
)
zhoneDslPerfTotalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalUAS.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfTotalUAS.setUnits("seconds")
_ZhoneDslPerfDataCurTable_Object = MibTable
zhoneDslPerfDataCurTable = _ZhoneDslPerfDataCurTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7)
)
if mibBuilder.loadTexts:
    zhoneDslPerfDataCurTable.setStatus("current")
_ZhoneDslPerfDataCurEntry_Object = MibTableRow
zhoneDslPerfDataCurEntry = _ZhoneDslPerfDataCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1)
)
if mibBuilder.loadTexts:
    zhoneDslPerfDataCurEntry.setStatus("current")
_ZhoneDslPerfLofs_Type = Counter32
_ZhoneDslPerfLofs_Object = MibTableColumn
zhoneDslPerfLofs = _ZhoneDslPerfLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 1),
    _ZhoneDslPerfLofs_Type()
)
zhoneDslPerfLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfLofs.setStatus("current")
_ZhoneDslPerfLoss_Type = Counter32
_ZhoneDslPerfLoss_Object = MibTableColumn
zhoneDslPerfLoss = _ZhoneDslPerfLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 2),
    _ZhoneDslPerfLoss_Type()
)
zhoneDslPerfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfLoss.setStatus("current")
_ZhoneDslPerfLols_Type = Counter32
_ZhoneDslPerfLols_Object = MibTableColumn
zhoneDslPerfLols = _ZhoneDslPerfLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 3),
    _ZhoneDslPerfLols_Type()
)
zhoneDslPerfLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfLols.setStatus("current")
_ZhoneDslPerfInits_Type = Counter32
_ZhoneDslPerfInits_Object = MibTableColumn
zhoneDslPerfInits = _ZhoneDslPerfInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 4),
    _ZhoneDslPerfInits_Type()
)
zhoneDslPerfInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfInits.setStatus("current")


class _ZhoneDslPerfTimeElapsed_Type(Integer32):
    """Custom type zhoneDslPerfTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_ZhoneDslPerfTimeElapsed_Type.__name__ = "Integer32"
_ZhoneDslPerfTimeElapsed_Object = MibTableColumn
zhoneDslPerfTimeElapsed = _ZhoneDslPerfTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 5),
    _ZhoneDslPerfTimeElapsed_Type()
)
zhoneDslPerfTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfTimeElapsed.setUnits("seconds")


class _ZhoneDslPerfES_Type(Integer32):
    """Custom type zhoneDslPerfES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslPerfES_Type.__name__ = "Integer32"
_ZhoneDslPerfES_Object = MibTableColumn
zhoneDslPerfES = _ZhoneDslPerfES_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 6),
    _ZhoneDslPerfES_Type()
)
zhoneDslPerfES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfES.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfES.setUnits("seconds")


class _ZhoneDslPerfSES_Type(Integer32):
    """Custom type zhoneDslPerfSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslPerfSES_Type.__name__ = "Integer32"
_ZhoneDslPerfSES_Object = MibTableColumn
zhoneDslPerfSES = _ZhoneDslPerfSES_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 7),
    _ZhoneDslPerfSES_Type()
)
zhoneDslPerfSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfSES.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfSES.setUnits("seconds")


class _ZhoneDslPerfCRCAnomalies_Type(Integer32):
    """Custom type zhoneDslPerfCRCAnomalies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslPerfCRCAnomalies_Type.__name__ = "Integer32"
_ZhoneDslPerfCRCAnomalies_Object = MibTableColumn
zhoneDslPerfCRCAnomalies = _ZhoneDslPerfCRCAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 8),
    _ZhoneDslPerfCRCAnomalies_Type()
)
zhoneDslPerfCRCAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfCRCAnomalies.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfCRCAnomalies.setUnits("seconds")


class _ZhoneDslPerfLOSWS_Type(Integer32):
    """Custom type zhoneDslPerfLOSWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslPerfLOSWS_Type.__name__ = "Integer32"
_ZhoneDslPerfLOSWS_Object = MibTableColumn
zhoneDslPerfLOSWS = _ZhoneDslPerfLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 9),
    _ZhoneDslPerfLOSWS_Type()
)
zhoneDslPerfLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfLOSWS.setUnits("seconds")


class _ZhoneDslPerfUAS_Type(Integer32):
    """Custom type zhoneDslPerfUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslPerfUAS_Type.__name__ = "Integer32"
_ZhoneDslPerfUAS_Object = MibTableColumn
zhoneDslPerfUAS = _ZhoneDslPerfUAS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 7, 1, 10),
    _ZhoneDslPerfUAS_Type()
)
zhoneDslPerfUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfUAS.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfUAS.setUnits("seconds")
_ZhoneDslAlarmProfileTable_Object = MibTable
zhoneDslAlarmProfileTable = _ZhoneDslAlarmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 8)
)
if mibBuilder.loadTexts:
    zhoneDslAlarmProfileTable.setStatus("current")
_ZhoneDslAlarmProfileEntry_Object = MibTableRow
zhoneDslAlarmProfileEntry = _ZhoneDslAlarmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 8, 1)
)
zhoneDslAlarmProfileEntry.setIndexNames(
    (1, "ZhoneDsl-MIB", "zhoneDslAlarmProfileName"),
)
if mibBuilder.loadTexts:
    zhoneDslAlarmProfileEntry.setStatus("current")


class _ZhoneDslAlarmProfileName_Type(ZhoneAdminString):
    """Custom type zhoneDslAlarmProfileName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ZhoneDslAlarmProfileName_Type.__name__ = "ZhoneAdminString"
_ZhoneDslAlarmProfileName_Object = MibTableColumn
zhoneDslAlarmProfileName = _ZhoneDslAlarmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 8, 1, 1),
    _ZhoneDslAlarmProfileName_Type()
)
zhoneDslAlarmProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneDslAlarmProfileName.setStatus("current")


class _ZhoneDslThreshold15MinLoss_Type(Integer32):
    """Custom type zhoneDslThreshold15MinLoss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslThreshold15MinLoss_Type.__name__ = "Integer32"
_ZhoneDslThreshold15MinLoss_Object = MibTableColumn
zhoneDslThreshold15MinLoss = _ZhoneDslThreshold15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 8, 1, 2),
    _ZhoneDslThreshold15MinLoss_Type()
)
zhoneDslThreshold15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLoss.setStatus("current")


class _ZhoneDslThreshold15MinLols_Type(Integer32):
    """Custom type zhoneDslThreshold15MinLols based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslThreshold15MinLols_Type.__name__ = "Integer32"
_ZhoneDslThreshold15MinLols_Object = MibTableColumn
zhoneDslThreshold15MinLols = _ZhoneDslThreshold15MinLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 8, 1, 3),
    _ZhoneDslThreshold15MinLols_Type()
)
zhoneDslThreshold15MinLols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLols.setStatus("current")


class _ZhoneDslThreshold15MinLofs_Type(Integer32):
    """Custom type zhoneDslThreshold15MinLofs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslThreshold15MinLofs_Type.__name__ = "Integer32"
_ZhoneDslThreshold15MinLofs_Object = MibTableColumn
zhoneDslThreshold15MinLofs = _ZhoneDslThreshold15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 8, 1, 4),
    _ZhoneDslThreshold15MinLofs_Type()
)
zhoneDslThreshold15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLofs.setStatus("current")
_ZhoneDslAlarmRowStatus_Type = ZhoneRowStatus
_ZhoneDslAlarmRowStatus_Object = MibTableColumn
zhoneDslAlarmRowStatus = _ZhoneDslAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 8, 1, 5),
    _ZhoneDslAlarmRowStatus_Type()
)
zhoneDslAlarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslAlarmRowStatus.setStatus("current")
_ZhoneShdslConfigProfileTable_Object = MibTable
zhoneShdslConfigProfileTable = _ZhoneShdslConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9)
)
if mibBuilder.loadTexts:
    zhoneShdslConfigProfileTable.setStatus("current")
_ZhoneShdslConfigProfileEntry_Object = MibTableRow
zhoneShdslConfigProfileEntry = _ZhoneShdslConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1)
)
zhoneShdslConfigProfileEntry.setIndexNames(
    (1, "ZhoneDsl-MIB", "zhoneShdslConfigProfileName"),
)
if mibBuilder.loadTexts:
    zhoneShdslConfigProfileEntry.setStatus("current")


class _ZhoneShdslConfigProfileName_Type(ZhoneAdminString):
    """Custom type zhoneShdslConfigProfileName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ZhoneShdslConfigProfileName_Type.__name__ = "ZhoneAdminString"
_ZhoneShdslConfigProfileName_Object = MibTableColumn
zhoneShdslConfigProfileName = _ZhoneShdslConfigProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 1),
    _ZhoneShdslConfigProfileName_Type()
)
zhoneShdslConfigProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneShdslConfigProfileName.setStatus("current")


class _ZhoneShdslConfigLineRate_Type(Integer32):
    """Custom type zhoneShdslConfigLineRate based on Integer32"""
    defaultValue = 73

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
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76)
        )
    )
    namedValues = NamedValues(
        *(("line-rate-72kbps", 1),
          ("line-rate-80kbps", 2),
          ("line-rate-136kbps", 3),
          ("line-rate-144kbps", 4),
          ("line-rate-200kbps", 5),
          ("line-rate-208kbps", 6),
          ("line-rate-264kbps", 7),
          ("line-rate-272kbps", 8),
          ("line-rate-328kbps", 9),
          ("line-rate-336kbps", 10),
          ("line-rate-392kbps", 11),
          ("line-rate-400kbps", 12),
          ("line-rate-456kbps", 13),
          ("line-rate-464kbps", 14),
          ("line-rate-520kbps", 15),
          ("line-rate-528kbps", 16),
          ("line-rate-584kbps", 17),
          ("line-rate-592kbps", 18),
          ("line-rate-648kbps", 19),
          ("line-rate-656kbps", 20),
          ("line-rate-712kbps", 21),
          ("line-rate-720kbps", 22),
          ("line-rate-776kbps", 23),
          ("line-rate-784kbps", 24),
          ("line-rate-840kbps", 25),
          ("line-rate-848kbps", 26),
          ("line-rate-904kbps", 27),
          ("line-rate-912kbps", 28),
          ("line-rate-968kbps", 29),
          ("line-rate-976kbps", 30),
          ("line-rate-1032kbps", 31),
          ("line-rate-1040kbps", 32),
          ("line-rate-1096kbps", 33),
          ("line-rate-1104kbps", 34),
          ("line-rate-1160kbps", 35),
          ("line-rate-1168kbps", 36),
          ("line-rate-1224kbps", 37),
          ("line-rate-1232kbps", 38),
          ("line-rate-1288kbps", 39),
          ("line-rate-1296kbps", 40),
          ("line-rate-1352kbps", 41),
          ("line-rate-1360kbps", 42),
          ("line-rate-1416kbps", 43),
          ("line-rate-1424kbps", 44),
          ("line-rate-1480kbps", 45),
          ("line-rate-1488kbps", 46),
          ("line-rate-1544kbps", 47),
          ("line-rate-1552kbps", 48),
          ("line-rate-1608kbps", 49),
          ("line-rate-1616kbps", 50),
          ("line-rate-1672kbps", 51),
          ("line-rate-1680kbps", 52),
          ("line-rate-1736kbps", 53),
          ("line-rate-1744kbps", 54),
          ("line-rate-1800kbps", 55),
          ("line-rate-1808kbps", 56),
          ("line-rate-1864kbps", 57),
          ("line-rate-1872kbps", 58),
          ("line-rate-1928kbps", 59),
          ("line-rate-1936kbps", 60),
          ("line-rate-1992kbps", 61),
          ("line-rate-2000kbps", 62),
          ("line-rate-2056kbps", 63),
          ("line-rate-2064kbps", 64),
          ("line-rate-2120kbps", 65),
          ("line-rate-2128kbps", 66),
          ("line-rate-2184kbps", 67),
          ("line-rate-2192kbps", 68),
          ("line-rate-2248kbps", 69),
          ("line-rate-2256kbps", 70),
          ("line-rate-2312kbps", 71),
          ("line-rate-2320kbps", 72),
          ("line-rate-2368kbps", 73),
          ("line-rate-192kbps", 74),
          ("line-rate-384kbps", 75),
          ("line-rate-416kbps", 76))
    )


_ZhoneShdslConfigLineRate_Type.__name__ = "Integer32"
_ZhoneShdslConfigLineRate_Object = MibTableColumn
zhoneShdslConfigLineRate = _ZhoneShdslConfigLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 2),
    _ZhoneShdslConfigLineRate_Type()
)
zhoneShdslConfigLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigLineRate.setStatus("current")


class _ZhoneShdslConfigTransmitPowerBackoffMode_Type(Integer32):
    """Custom type zhoneShdslConfigTransmitPowerBackoffMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backoffDisable", 1),
          ("backoffEnable", 2),
          ("noChangeBackoff", 3))
    )


_ZhoneShdslConfigTransmitPowerBackoffMode_Type.__name__ = "Integer32"
_ZhoneShdslConfigTransmitPowerBackoffMode_Object = MibTableColumn
zhoneShdslConfigTransmitPowerBackoffMode = _ZhoneShdslConfigTransmitPowerBackoffMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 3),
    _ZhoneShdslConfigTransmitPowerBackoffMode_Type()
)
zhoneShdslConfigTransmitPowerBackoffMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigTransmitPowerBackoffMode.setStatus("current")


class _ZhoneShdslConfigFixBitRate_Type(Integer32):
    """Custom type zhoneShdslConfigFixBitRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-bit-enable", 1),
          ("fix-bit-disable", 2))
    )


_ZhoneShdslConfigFixBitRate_Type.__name__ = "Integer32"
_ZhoneShdslConfigFixBitRate_Object = MibTableColumn
zhoneShdslConfigFixBitRate = _ZhoneShdslConfigFixBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 4),
    _ZhoneShdslConfigFixBitRate_Type()
)
zhoneShdslConfigFixBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigFixBitRate.setStatus("current")


class _ZhoneShdslConfigNTR_Type(Integer32):
    """Custom type zhoneShdslConfigNTR based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ntr-local-osc", 1),
          ("ntr-refck-8KHz", 2),
          ("ntr-refck-8192KHz", 3))
    )


_ZhoneShdslConfigNTR_Type.__name__ = "Integer32"
_ZhoneShdslConfigNTR_Object = MibTableColumn
zhoneShdslConfigNTR = _ZhoneShdslConfigNTR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 5),
    _ZhoneShdslConfigNTR_Type()
)
zhoneShdslConfigNTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigNTR.setStatus("current")


class _ZhoneShdslConfigClockOffset_Type(Integer32):
    """Custom type zhoneShdslConfigClockOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_ZhoneShdslConfigClockOffset_Type.__name__ = "Integer32"
_ZhoneShdslConfigClockOffset_Object = MibTableColumn
zhoneShdslConfigClockOffset = _ZhoneShdslConfigClockOffset_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 6),
    _ZhoneShdslConfigClockOffset_Type()
)
zhoneShdslConfigClockOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigClockOffset.setStatus("current")
if mibBuilder.loadTexts:
    zhoneShdslConfigClockOffset.setUnits("ppm")


class _ZhoneShdslConfigRepeaterId_Type(Integer32):
    """Custom type zhoneShdslConfigRepeaterId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("repeaterEnable", 1),
          ("repeaterDisable", 2),
          ("noChangeRepeater", 3))
    )


_ZhoneShdslConfigRepeaterId_Type.__name__ = "Integer32"
_ZhoneShdslConfigRepeaterId_Object = MibTableColumn
zhoneShdslConfigRepeaterId = _ZhoneShdslConfigRepeaterId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 7),
    _ZhoneShdslConfigRepeaterId_Type()
)
zhoneShdslConfigRepeaterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigRepeaterId.setStatus("current")


class _ZhoneShdslConfigStandard_Type(Integer32):
    """Custom type zhoneShdslConfigStandard based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annex-a", 1),
          ("annex-b", 2))
    )


_ZhoneShdslConfigStandard_Type.__name__ = "Integer32"
_ZhoneShdslConfigStandard_Object = MibTableColumn
zhoneShdslConfigStandard = _ZhoneShdslConfigStandard_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 8),
    _ZhoneShdslConfigStandard_Type()
)
zhoneShdslConfigStandard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigStandard.setStatus("current")


class _ZhoneShdslConfigStartupMargin_Type(Integer32):
    """Custom type zhoneShdslConfigStartupMargin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZhoneShdslConfigStartupMargin_Type.__name__ = "Integer32"
_ZhoneShdslConfigStartupMargin_Object = MibTableColumn
zhoneShdslConfigStartupMargin = _ZhoneShdslConfigStartupMargin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 9),
    _ZhoneShdslConfigStartupMargin_Type()
)
zhoneShdslConfigStartupMargin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigStartupMargin.setStatus("current")
if mibBuilder.loadTexts:
    zhoneShdslConfigStartupMargin.setUnits("dB")


class _ZhoneShdslConfigWireMode_Type(Integer32):
    """Custom type zhoneShdslConfigWireMode based on Integer32"""
    defaultValue = 1

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
        *(("four-wire-disable", 1),
          ("four-wire-enable-byte-interleave", 2),
          ("four-wire-enable-bit-interleave", 3),
          ("four-wire-enable-non-interleave", 4))
    )


_ZhoneShdslConfigWireMode_Type.__name__ = "Integer32"
_ZhoneShdslConfigWireMode_Object = MibTableColumn
zhoneShdslConfigWireMode = _ZhoneShdslConfigWireMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 10),
    _ZhoneShdslConfigWireMode_Type()
)
zhoneShdslConfigWireMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigWireMode.setStatus("current")


class _ZhoneShdslConfigFrameSync_Type(Integer32):
    """Custom type zhoneShdslConfigFrameSync based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneShdslConfigFrameSync_Type.__name__ = "Integer32"
_ZhoneShdslConfigFrameSync_Object = MibTableColumn
zhoneShdslConfigFrameSync = _ZhoneShdslConfigFrameSync_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 11),
    _ZhoneShdslConfigFrameSync_Type()
)
zhoneShdslConfigFrameSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigFrameSync.setStatus("current")


class _ZhoneShdslConfigDecoderCoeffA_Type(Integer32):
    """Custom type zhoneShdslConfigDecoderCoeffA based on Integer32"""
    defaultValue = 366

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_ZhoneShdslConfigDecoderCoeffA_Type.__name__ = "Integer32"
_ZhoneShdslConfigDecoderCoeffA_Object = MibTableColumn
zhoneShdslConfigDecoderCoeffA = _ZhoneShdslConfigDecoderCoeffA_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 12),
    _ZhoneShdslConfigDecoderCoeffA_Type()
)
zhoneShdslConfigDecoderCoeffA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigDecoderCoeffA.setStatus("current")


class _ZhoneShdslConfigDecoderCoeffB_Type(Integer32):
    """Custom type zhoneShdslConfigDecoderCoeffB based on Integer32"""
    defaultValue = 817

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_ZhoneShdslConfigDecoderCoeffB_Type.__name__ = "Integer32"
_ZhoneShdslConfigDecoderCoeffB_Object = MibTableColumn
zhoneShdslConfigDecoderCoeffB = _ZhoneShdslConfigDecoderCoeffB_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 13),
    _ZhoneShdslConfigDecoderCoeffB_Type()
)
zhoneShdslConfigDecoderCoeffB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigDecoderCoeffB.setStatus("current")


class _ZhoneShdslConfigPowerScale_Type(Integer32):
    """Custom type zhoneShdslConfigPowerScale based on Integer32"""
    defaultValue = 29952


_ZhoneShdslConfigPowerScale_Type.__name__ = "Integer32"
_ZhoneShdslConfigPowerScale_Object = MibTableColumn
zhoneShdslConfigPowerScale = _ZhoneShdslConfigPowerScale_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 14),
    _ZhoneShdslConfigPowerScale_Type()
)
zhoneShdslConfigPowerScale.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigPowerScale.setStatus("current")
_ZhoneShdslConfigRowStatus_Type = ZhoneRowStatus
_ZhoneShdslConfigRowStatus_Object = MibTableColumn
zhoneShdslConfigRowStatus = _ZhoneShdslConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 9, 1, 15),
    _ZhoneShdslConfigRowStatus_Type()
)
zhoneShdslConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneShdslConfigRowStatus.setStatus("current")
_ZhoneShdslStatusTable_Object = MibTable
zhoneShdslStatusTable = _ZhoneShdslStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 10)
)
if mibBuilder.loadTexts:
    zhoneShdslStatusTable.setStatus("current")
_ZhoneShdslStatusEntry_Object = MibTableRow
zhoneShdslStatusEntry = _ZhoneShdslStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 10, 1)
)
zhoneShdslStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneShdslStatusEntry.setStatus("current")


class _ZhoneShdslFixBitStatus_Type(Integer32):
    """Custom type zhoneShdslFixBitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-bit-enable", 1),
          ("fix-bit-disable", 2))
    )


_ZhoneShdslFixBitStatus_Type.__name__ = "Integer32"
_ZhoneShdslFixBitStatus_Object = MibTableColumn
zhoneShdslFixBitStatus = _ZhoneShdslFixBitStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 10, 1, 1),
    _ZhoneShdslFixBitStatus_Type()
)
zhoneShdslFixBitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShdslFixBitStatus.setStatus("current")
_ZhoneShdslDSPVersion_Type = Integer32
_ZhoneShdslDSPVersion_Object = MibTableColumn
zhoneShdslDSPVersion = _ZhoneShdslDSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 10, 1, 2),
    _ZhoneShdslDSPVersion_Type()
)
zhoneShdslDSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShdslDSPVersion.setStatus("current")


class _ZhoneShdslFirmwareVersion_Type(OctetString):
    """Custom type zhoneShdslFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ZhoneShdslFirmwareVersion_Type.__name__ = "OctetString"
_ZhoneShdslFirmwareVersion_Object = MibTableColumn
zhoneShdslFirmwareVersion = _ZhoneShdslFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 10, 1, 3),
    _ZhoneShdslFirmwareVersion_Type()
)
zhoneShdslFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShdslFirmwareVersion.setStatus("current")
_ZhoneShdslSignalQuality_Type = Integer32
_ZhoneShdslSignalQuality_Object = MibTableColumn
zhoneShdslSignalQuality = _ZhoneShdslSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 10, 1, 4),
    _ZhoneShdslSignalQuality_Type()
)
zhoneShdslSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShdslSignalQuality.setStatus("current")
_ZhoneShdslTransmitPower_Type = Integer32
_ZhoneShdslTransmitPower_Object = MibTableColumn
zhoneShdslTransmitPower = _ZhoneShdslTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 10, 1, 5),
    _ZhoneShdslTransmitPower_Type()
)
zhoneShdslTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShdslTransmitPower.setStatus("current")
if mibBuilder.loadTexts:
    zhoneShdslTransmitPower.setUnits("dBm")


class _ZhoneShdslStartProgress_Type(Integer32):
    """Custom type zhoneShdslStartProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              24,
              26)
        )
    )
    namedValues = NamedValues(
        *(("startup-handshake-in-progress", 16),
          ("startup-training-in-progress", 24),
          ("startup-framer-sync-in-progress", 26))
    )


_ZhoneShdslStartProgress_Type.__name__ = "Integer32"
_ZhoneShdslStartProgress_Object = MibTableColumn
zhoneShdslStartProgress = _ZhoneShdslStartProgress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 10, 1, 6),
    _ZhoneShdslStartProgress_Type()
)
zhoneShdslStartProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShdslStartProgress.setStatus("current")
_ZhoneAdslLineExtTable_Object = MibTable
zhoneAdslLineExtTable = _ZhoneAdslLineExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11)
)
if mibBuilder.loadTexts:
    zhoneAdslLineExtTable.setStatus("current")
_ZhoneAdslLineExtEntry_Object = MibTableRow
zhoneAdslLineExtEntry = _ZhoneAdslLineExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1)
)
if mibBuilder.loadTexts:
    zhoneAdslLineExtEntry.setStatus("current")


class _ZhoneAdslTrellisModeEnabled_Type(TruthValue):
    """Custom type zhoneAdslTrellisModeEnabled based on TruthValue"""
    defaultValue = 1


_ZhoneAdslTrellisModeEnabled_Type.__name__ = "TruthValue"
_ZhoneAdslTrellisModeEnabled_Object = MibTableColumn
zhoneAdslTrellisModeEnabled = _ZhoneAdslTrellisModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 1),
    _ZhoneAdslTrellisModeEnabled_Type()
)
zhoneAdslTrellisModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslTrellisModeEnabled.setStatus("current")


class _ZhoneAdslNTRModeEnabled_Type(TruthValue):
    """Custom type zhoneAdslNTRModeEnabled based on TruthValue"""
    defaultValue = 1


_ZhoneAdslNTRModeEnabled_Type.__name__ = "TruthValue"
_ZhoneAdslNTRModeEnabled_Object = MibTableColumn
zhoneAdslNTRModeEnabled = _ZhoneAdslNTRModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 2),
    _ZhoneAdslNTRModeEnabled_Type()
)
zhoneAdslNTRModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslNTRModeEnabled.setStatus("current")


class _ZhoneAdslTransmissionMode_Type(Integer32):
    """Custom type zhoneAdslTransmissionMode based on Integer32"""
    defaultValue = 1

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
        *(("autoNegotiateMode", 1),
          ("fullRateMode", 2),
          ("gliteMode", 3),
          ("t1Mode", 4),
          ("gdmtMode", 5),
          ("ghsMode", 6))
    )


_ZhoneAdslTransmissionMode_Type.__name__ = "Integer32"
_ZhoneAdslTransmissionMode_Object = MibTableColumn
zhoneAdslTransmissionMode = _ZhoneAdslTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 3),
    _ZhoneAdslTransmissionMode_Type()
)
zhoneAdslTransmissionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslTransmissionMode.setStatus("current")


class _ZhoneAdslChannelMode_Type(Integer32):
    """Custom type zhoneAdslChannelMode based on Integer32"""
    defaultValue = 1

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
        *(("fastOnly", 1),
          ("interleavedOnly", 2),
          ("fastAndInterleaved", 3),
          ("fastOrInterleaved", 4))
    )


_ZhoneAdslChannelMode_Type.__name__ = "Integer32"
_ZhoneAdslChannelMode_Object = MibTableColumn
zhoneAdslChannelMode = _ZhoneAdslChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 4),
    _ZhoneAdslChannelMode_Type()
)
zhoneAdslChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslChannelMode.setStatus("current")


class _ZhoneAdslMaxDownstreamToneIndex_Type(Integer32):
    """Custom type zhoneAdslMaxDownstreamToneIndex based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 255),
    )


_ZhoneAdslMaxDownstreamToneIndex_Type.__name__ = "Integer32"
_ZhoneAdslMaxDownstreamToneIndex_Object = MibTableColumn
zhoneAdslMaxDownstreamToneIndex = _ZhoneAdslMaxDownstreamToneIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 5),
    _ZhoneAdslMaxDownstreamToneIndex_Type()
)
zhoneAdslMaxDownstreamToneIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslMaxDownstreamToneIndex.setStatus("current")


class _ZhoneAdslMinDownstreamToneIndex_Type(Integer32):
    """Custom type zhoneAdslMinDownstreamToneIndex based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 255),
    )


_ZhoneAdslMinDownstreamToneIndex_Type.__name__ = "Integer32"
_ZhoneAdslMinDownstreamToneIndex_Object = MibTableColumn
zhoneAdslMinDownstreamToneIndex = _ZhoneAdslMinDownstreamToneIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 6),
    _ZhoneAdslMinDownstreamToneIndex_Type()
)
zhoneAdslMinDownstreamToneIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslMinDownstreamToneIndex.setStatus("current")


class _ZhoneAdslMaxUpstreamToneIndex_Type(Integer32):
    """Custom type zhoneAdslMaxUpstreamToneIndex based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 30),
        ValueRangeConstraint(33, 60),
    )


_ZhoneAdslMaxUpstreamToneIndex_Type.__name__ = "Integer32"
_ZhoneAdslMaxUpstreamToneIndex_Object = MibTableColumn
zhoneAdslMaxUpstreamToneIndex = _ZhoneAdslMaxUpstreamToneIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 7),
    _ZhoneAdslMaxUpstreamToneIndex_Type()
)
zhoneAdslMaxUpstreamToneIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslMaxUpstreamToneIndex.setStatus("current")


class _ZhoneAdslMinUpstreamToneIndex_Type(Integer32):
    """Custom type zhoneAdslMinUpstreamToneIndex based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 30),
        ValueRangeConstraint(33, 60),
    )


_ZhoneAdslMinUpstreamToneIndex_Type.__name__ = "Integer32"
_ZhoneAdslMinUpstreamToneIndex_Object = MibTableColumn
zhoneAdslMinUpstreamToneIndex = _ZhoneAdslMinUpstreamToneIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 8),
    _ZhoneAdslMinUpstreamToneIndex_Type()
)
zhoneAdslMinUpstreamToneIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslMinUpstreamToneIndex.setStatus("current")


class _ZhoneAdslPotsBypassRelayMaxDuration_Type(Integer32):
    """Custom type zhoneAdslPotsBypassRelayMaxDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ZhoneAdslPotsBypassRelayMaxDuration_Type.__name__ = "Integer32"
_ZhoneAdslPotsBypassRelayMaxDuration_Object = MibTableColumn
zhoneAdslPotsBypassRelayMaxDuration = _ZhoneAdslPotsBypassRelayMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 9),
    _ZhoneAdslPotsBypassRelayMaxDuration_Type()
)
zhoneAdslPotsBypassRelayMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslPotsBypassRelayMaxDuration.setStatus("current")


class _ZhoneAdslPotsBypassRelayStatus_Type(Integer32):
    """Custom type zhoneAdslPotsBypassRelayStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("closed", 2))
    )


_ZhoneAdslPotsBypassRelayStatus_Type.__name__ = "Integer32"
_ZhoneAdslPotsBypassRelayStatus_Object = MibTableColumn
zhoneAdslPotsBypassRelayStatus = _ZhoneAdslPotsBypassRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 11, 1, 10),
    _ZhoneAdslPotsBypassRelayStatus_Type()
)
zhoneAdslPotsBypassRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslPotsBypassRelayStatus.setStatus("current")
_ZhoneDslTraps_ObjectIdentity = ObjectIdentity
zhoneDslTraps = _ZhoneDslTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 12)
)
if mibBuilder.loadTexts:
    zhoneDslTraps.setStatus("current")
_ZhoneDslV2Traps_ObjectIdentity = ObjectIdentity
zhoneDslV2Traps = _ZhoneDslV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 12, 0)
)
if mibBuilder.loadTexts:
    zhoneDslV2Traps.setStatus("current")
zhoneDslLineEntry.registerAugmentions(
    ("ZhoneDsl-MIB",
     "zhoneDslPerfDataTotalEntry")
)
zhoneDslPerfDataTotalEntry.setIndexNames(*zhoneDslLineEntry.getIndexNames())
zhoneDslLineEntry.registerAugmentions(
    ("ZhoneDsl-MIB",
     "zhoneDslPerfDataCurEntry")
)
zhoneDslPerfDataCurEntry.setIndexNames(*zhoneDslLineEntry.getIndexNames())
adslLineEntry.registerAugmentions(
    ("ZhoneDsl-MIB",
     "zhoneAdslLineExtEntry")
)
zhoneAdslLineExtEntry.setIndexNames(*adslLineEntry.getIndexNames())

# Managed Objects groups

zhoneAdslPotsBypassRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 13)
)
zhoneAdslPotsBypassRelayGroup.setObjects(
      *(("ZhoneDsl-MIB", "zhoneAdslPotsBypassRelayMaxDuration"),
        ("ZhoneDsl-MIB", "zhoneAdslPotsBypassRelayStatus"))
)
if mibBuilder.loadTexts:
    zhoneAdslPotsBypassRelayGroup.setStatus("current")


# Notification objects

zhoneAdslPotsBypassRelayChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 12, 0, 1)
)
zhoneAdslPotsBypassRelayChangeNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZhoneDsl-MIB", "zhoneAdslPotsBypassRelayStatus"))
)
if mibBuilder.loadTexts:
    zhoneAdslPotsBypassRelayChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneDsl-MIB",
    **{"zhoneDslLineTable": zhoneDslLineTable,
       "zhoneDslLineEntry": zhoneDslLineEntry,
       "zhoneDslLineType": zhoneDslLineType,
       "zhoneDslLineCapabilities": zhoneDslLineCapabilities,
       "zhoneDslConfigUnitMode": zhoneDslConfigUnitMode,
       "zhoneDslTipRingStatus": zhoneDslTipRingStatus,
       "zhoneDslLineStatus": zhoneDslLineStatus,
       "zhoneDslUpLineRate": zhoneDslUpLineRate,
       "zhoneDslDownLineRate": zhoneDslDownLineRate,
       "zhoneDslConfigProfName": zhoneDslConfigProfName,
       "zhoneDslAlarmProfName": zhoneDslAlarmProfName,
       "zhoneDslMaxAttainableUpLineRate": zhoneDslMaxAttainableUpLineRate,
       "zhoneDslMaxAttainableDownLineRate": zhoneDslMaxAttainableDownLineRate,
       "zhoneDslLineSnrMgn": zhoneDslLineSnrMgn,
       "zhoneDslLineAtn": zhoneDslLineAtn,
       "zhoneDslLineAlarmStatus": zhoneDslLineAlarmStatus,
       "zhoneDslLineStatusChangeTrapEnable": zhoneDslLineStatusChangeTrapEnable,
       "zhoneDslLineCurrOutputPwr": zhoneDslLineCurrOutputPwr,
       "zhoneHdsl2ConfigProfileTable": zhoneHdsl2ConfigProfileTable,
       "zhoneHdsl2ConfigProfileEntry": zhoneHdsl2ConfigProfileEntry,
       "zhoneHdsl2ConfigProfileName": zhoneHdsl2ConfigProfileName,
       "zhoneHdsl2ConfigTransmitPowerBackoffMode": zhoneHdsl2ConfigTransmitPowerBackoffMode,
       "zhoneHdsl2ConfigDecoderCoeffA": zhoneHdsl2ConfigDecoderCoeffA,
       "zhoneHdsl2ConfigDecoderCoeffB": zhoneHdsl2ConfigDecoderCoeffB,
       "zhoneHdsl2ConfigFrameSyncWord": zhoneHdsl2ConfigFrameSyncWord,
       "zhoneHdsl2ConfigStuffBits": zhoneHdsl2ConfigStuffBits,
       "zhoneHdsl2ConfigRowStatus": zhoneHdsl2ConfigRowStatus,
       "zhoneSdslConfigProfileTable": zhoneSdslConfigProfileTable,
       "zhoneSdslConfigProfileEntry": zhoneSdslConfigProfileEntry,
       "zhoneSdslConfigProfileName": zhoneSdslConfigProfileName,
       "zhoneSdslConfigLineRate": zhoneSdslConfigLineRate,
       "zhoneSdslConfigFixBitRate": zhoneSdslConfigFixBitRate,
       "zhoneSdslConfigConnectMode": zhoneSdslConfigConnectMode,
       "zhoneSdslConfigNTR": zhoneSdslConfigNTR,
       "zhoneSdslConfigFramerType": zhoneSdslConfigFramerType,
       "zhoneSdslConfigPowerScale": zhoneSdslConfigPowerScale,
       "zhoneSdslConfigRowStatus": zhoneSdslConfigRowStatus,
       "zhoneHdsl2StatusTable": zhoneHdsl2StatusTable,
       "zhoneHdsl2StatusEntry": zhoneHdsl2StatusEntry,
       "zhoneHdsl2DriftAlarm": zhoneHdsl2DriftAlarm,
       "zhoneHdsl2FramerIBStatus": zhoneHdsl2FramerIBStatus,
       "zhoneHdsl2LocalPSDMaskStatus": zhoneHdsl2LocalPSDMaskStatus,
       "zhoneHdsl2LoopAttenuation": zhoneHdsl2LoopAttenuation,
       "zhoneHdsl2LossWordStatus": zhoneHdsl2LossWordStatus,
       "zhoneHdsl2RmtPSDMaskStatus": zhoneHdsl2RmtPSDMaskStatus,
       "zhoneHdsl2RmtCountryCode": zhoneHdsl2RmtCountryCode,
       "zhoneHdsl2RmtVersion": zhoneHdsl2RmtVersion,
       "zhoneHdsl2RmtProviderCode": zhoneHdsl2RmtProviderCode,
       "zhoneHdsl2RmtVendorData": zhoneHdsl2RmtVendorData,
       "zhoneHdsl2RmtTxEncoderA": zhoneHdsl2RmtTxEncoderA,
       "zhoneHdsl2RmtTxEncoderB": zhoneHdsl2RmtTxEncoderB,
       "zhoneHdsl2FrameSyncWord": zhoneHdsl2FrameSyncWord,
       "zhoneHdsl2StuffBits": zhoneHdsl2StuffBits,
       "zhoneSdslStatusTable": zhoneSdslStatusTable,
       "zhoneSdslStatusEntry": zhoneSdslStatusEntry,
       "zhoneSdslFixBitStatus": zhoneSdslFixBitStatus,
       "zhoneSdslDSPVersion": zhoneSdslDSPVersion,
       "zhoneSdslFirmwareVersion": zhoneSdslFirmwareVersion,
       "zhoneDslPerfDataTotalTable": zhoneDslPerfDataTotalTable,
       "zhoneDslPerfDataTotalEntry": zhoneDslPerfDataTotalEntry,
       "zhoneDslPerfTotalLofs": zhoneDslPerfTotalLofs,
       "zhoneDslPerfTotalLoss": zhoneDslPerfTotalLoss,
       "zhoneDslPerfTotalLols": zhoneDslPerfTotalLols,
       "zhoneDslPerfTotalInits": zhoneDslPerfTotalInits,
       "zhoneDslPerfTotalES": zhoneDslPerfTotalES,
       "zhoneDslPerfTotalSES": zhoneDslPerfTotalSES,
       "zhoneDslPerfTotalCRCAnomalies": zhoneDslPerfTotalCRCAnomalies,
       "zhoneDslPerfTotalLOSWS": zhoneDslPerfTotalLOSWS,
       "zhoneDslPerfTotalUAS": zhoneDslPerfTotalUAS,
       "zhoneDslPerfDataCurTable": zhoneDslPerfDataCurTable,
       "zhoneDslPerfDataCurEntry": zhoneDslPerfDataCurEntry,
       "zhoneDslPerfLofs": zhoneDslPerfLofs,
       "zhoneDslPerfLoss": zhoneDslPerfLoss,
       "zhoneDslPerfLols": zhoneDslPerfLols,
       "zhoneDslPerfInits": zhoneDslPerfInits,
       "zhoneDslPerfTimeElapsed": zhoneDslPerfTimeElapsed,
       "zhoneDslPerfES": zhoneDslPerfES,
       "zhoneDslPerfSES": zhoneDslPerfSES,
       "zhoneDslPerfCRCAnomalies": zhoneDslPerfCRCAnomalies,
       "zhoneDslPerfLOSWS": zhoneDslPerfLOSWS,
       "zhoneDslPerfUAS": zhoneDslPerfUAS,
       "zhoneDslAlarmProfileTable": zhoneDslAlarmProfileTable,
       "zhoneDslAlarmProfileEntry": zhoneDslAlarmProfileEntry,
       "zhoneDslAlarmProfileName": zhoneDslAlarmProfileName,
       "zhoneDslThreshold15MinLoss": zhoneDslThreshold15MinLoss,
       "zhoneDslThreshold15MinLols": zhoneDslThreshold15MinLols,
       "zhoneDslThreshold15MinLofs": zhoneDslThreshold15MinLofs,
       "zhoneDslAlarmRowStatus": zhoneDslAlarmRowStatus,
       "zhoneShdslConfigProfileTable": zhoneShdslConfigProfileTable,
       "zhoneShdslConfigProfileEntry": zhoneShdslConfigProfileEntry,
       "zhoneShdslConfigProfileName": zhoneShdslConfigProfileName,
       "zhoneShdslConfigLineRate": zhoneShdslConfigLineRate,
       "zhoneShdslConfigTransmitPowerBackoffMode": zhoneShdslConfigTransmitPowerBackoffMode,
       "zhoneShdslConfigFixBitRate": zhoneShdslConfigFixBitRate,
       "zhoneShdslConfigNTR": zhoneShdslConfigNTR,
       "zhoneShdslConfigClockOffset": zhoneShdslConfigClockOffset,
       "zhoneShdslConfigRepeaterId": zhoneShdslConfigRepeaterId,
       "zhoneShdslConfigStandard": zhoneShdslConfigStandard,
       "zhoneShdslConfigStartupMargin": zhoneShdslConfigStartupMargin,
       "zhoneShdslConfigWireMode": zhoneShdslConfigWireMode,
       "zhoneShdslConfigFrameSync": zhoneShdslConfigFrameSync,
       "zhoneShdslConfigDecoderCoeffA": zhoneShdslConfigDecoderCoeffA,
       "zhoneShdslConfigDecoderCoeffB": zhoneShdslConfigDecoderCoeffB,
       "zhoneShdslConfigPowerScale": zhoneShdslConfigPowerScale,
       "zhoneShdslConfigRowStatus": zhoneShdslConfigRowStatus,
       "zhoneShdslStatusTable": zhoneShdslStatusTable,
       "zhoneShdslStatusEntry": zhoneShdslStatusEntry,
       "zhoneShdslFixBitStatus": zhoneShdslFixBitStatus,
       "zhoneShdslDSPVersion": zhoneShdslDSPVersion,
       "zhoneShdslFirmwareVersion": zhoneShdslFirmwareVersion,
       "zhoneShdslSignalQuality": zhoneShdslSignalQuality,
       "zhoneShdslTransmitPower": zhoneShdslTransmitPower,
       "zhoneShdslStartProgress": zhoneShdslStartProgress,
       "zhoneAdslLineExtTable": zhoneAdslLineExtTable,
       "zhoneAdslLineExtEntry": zhoneAdslLineExtEntry,
       "zhoneAdslTrellisModeEnabled": zhoneAdslTrellisModeEnabled,
       "zhoneAdslNTRModeEnabled": zhoneAdslNTRModeEnabled,
       "zhoneAdslTransmissionMode": zhoneAdslTransmissionMode,
       "zhoneAdslChannelMode": zhoneAdslChannelMode,
       "zhoneAdslMaxDownstreamToneIndex": zhoneAdslMaxDownstreamToneIndex,
       "zhoneAdslMinDownstreamToneIndex": zhoneAdslMinDownstreamToneIndex,
       "zhoneAdslMaxUpstreamToneIndex": zhoneAdslMaxUpstreamToneIndex,
       "zhoneAdslMinUpstreamToneIndex": zhoneAdslMinUpstreamToneIndex,
       "zhoneAdslPotsBypassRelayMaxDuration": zhoneAdslPotsBypassRelayMaxDuration,
       "zhoneAdslPotsBypassRelayStatus": zhoneAdslPotsBypassRelayStatus,
       "zhoneDslTraps": zhoneDslTraps,
       "zhoneDslV2Traps": zhoneDslV2Traps,
       "zhoneAdslPotsBypassRelayChangeNotification": zhoneAdslPotsBypassRelayChangeNotification,
       "zhoneAdslPotsBypassRelayGroup": zhoneAdslPotsBypassRelayGroup,
       "zhoneDslMib": zhoneDslMib}
)
