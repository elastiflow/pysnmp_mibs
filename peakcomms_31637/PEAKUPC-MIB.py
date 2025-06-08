# SNMP MIB module (PEAKUPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKUPC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(ChannelExpectedType,
 ChannelMissingType,
 ChannelModeType,
 ChannelType,
 EnableType,
 FaultType,
 YesNoType,
 converters) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "ChannelExpectedType",
    "ChannelMissingType",
    "ChannelModeType",
    "ChannelType",
    "EnableType",
    "FaultType",
    "YesNoType",
    "converters")

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

peakUPCModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9)
)
if mibBuilder.loadTexts:
    peakUPCModule.setRevisions(
        ("2015-09-15 10:00",
         "2014-03-18 12:00",
         "2013-04-04 12:00",
         "2012-12-18 09:00",
         "2011-05-24 09:00",
         "2011-02-22 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UPCCalibratedType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notCalibrated", 1),
          ("calibrated", 2))
    )



class UPCModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )



class UPCStepSizeType(TextualConvention, Integer32):
    status = "current"
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
        *(("ss0o1dB", 1),
          ("ss0o2dB", 2),
          ("ss0o5dB", 3),
          ("ss1o0dB", 4),
          ("ss2o0dB", 5))
    )



class UPCSlewRateType(TextualConvention, Integer32):
    status = "current"
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
        *(("srOFF", 1),
          ("sr10s", 2),
          ("sr20s", 3),
          ("sr50s", 4),
          ("sr100s", 5))
    )



# MIB Managed Objects in the order of their OIDs

_UpcCTable_Object = MibTable
upcCTable = _UpcCTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    upcCTable.setStatus("current")
_UpcCTableEntry_Object = MibTableRow
upcCTableEntry = _UpcCTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1)
)
upcCTableEntry.setIndexNames(
    (0, "PEAKUPC-MIB", "upcCIndex"),
)
if mibBuilder.loadTexts:
    upcCTableEntry.setStatus("current")


class _UpcCIndex_Type(Integer32):
    """Custom type upcCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_UpcCIndex_Type.__name__ = "Integer32"
_UpcCIndex_Object = MibTableColumn
upcCIndex = _UpcCIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 1),
    _UpcCIndex_Type()
)
upcCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upcCIndex.setStatus("current")
_UpcCChannelNo_Type = Integer32
_UpcCChannelNo_Object = MibTableColumn
upcCChannelNo = _UpcCChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 2),
    _UpcCChannelNo_Type()
)
upcCChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcCChannelNo.setStatus("current")
_UpcCType_Type = ChannelType
_UpcCType_Object = MibTableColumn
upcCType = _UpcCType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 3),
    _UpcCType_Type()
)
upcCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcCType.setStatus("current")
_UpcCMode_Type = ChannelModeType
_UpcCMode_Object = MibTableColumn
upcCMode = _UpcCMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 4),
    _UpcCMode_Type()
)
upcCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcCMode.setStatus("current")
_UpcCCompRatio_Type = OctetString
_UpcCCompRatio_Object = MibTableColumn
upcCCompRatio = _UpcCCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 5),
    _UpcCCompRatio_Type()
)
upcCCompRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcCCompRatio.setStatus("current")
_UpcCAttenuation_Type = OctetString
_UpcCAttenuation_Object = MibTableColumn
upcCAttenuation = _UpcCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 6),
    _UpcCAttenuation_Type()
)
upcCAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcCAttenuation.setStatus("current")
_UpcCOffset_Type = OctetString
_UpcCOffset_Object = MibTableColumn
upcCOffset = _UpcCOffset_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 7),
    _UpcCOffset_Type()
)
upcCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcCOffset.setStatus("current")
_UpcCExtExpected_Type = ChannelExpectedType
_UpcCExtExpected_Object = MibTableColumn
upcCExtExpected = _UpcCExtExpected_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 8),
    _UpcCExtExpected_Type()
)
upcCExtExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcCExtExpected.setStatus("current")
_UpcCExtMissing_Type = ChannelMissingType
_UpcCExtMissing_Object = MibTableColumn
upcCExtMissing = _UpcCExtMissing_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 9),
    _UpcCExtMissing_Type()
)
upcCExtMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcCExtMissing.setStatus("current")


class _UpcCSerialNo_Type(Integer32):
    """Custom type upcCSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_UpcCSerialNo_Type.__name__ = "Integer32"
_UpcCSerialNo_Object = MibTableColumn
upcCSerialNo = _UpcCSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 1, 1, 10),
    _UpcCSerialNo_Type()
)
upcCSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcCSerialNo.setStatus("current")
_UpcClearSkyCalibrated_Type = UPCCalibratedType
_UpcClearSkyCalibrated_Object = MibScalar
upcClearSkyCalibrated = _UpcClearSkyCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 2),
    _UpcClearSkyCalibrated_Type()
)
upcClearSkyCalibrated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcClearSkyCalibrated.setStatus("current")
_UpcExtChannelsCalibrated_Type = UPCCalibratedType
_UpcExtChannelsCalibrated_Object = MibScalar
upcExtChannelsCalibrated = _UpcExtChannelsCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 3),
    _UpcExtChannelsCalibrated_Type()
)
upcExtChannelsCalibrated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcExtChannelsCalibrated.setStatus("current")
_UpcMode_Type = UPCModeType
_UpcMode_Object = MibScalar
upcMode = _UpcMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 4),
    _UpcMode_Type()
)
upcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcMode.setStatus("current")
_UpcClearSkyBeaconLevel_Type = OctetString
_UpcClearSkyBeaconLevel_Object = MibScalar
upcClearSkyBeaconLevel = _UpcClearSkyBeaconLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 5),
    _UpcClearSkyBeaconLevel_Type()
)
upcClearSkyBeaconLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcClearSkyBeaconLevel.setStatus("current")
_UpcSampledBeaconLevel_Type = OctetString
_UpcSampledBeaconLevel_Object = MibScalar
upcSampledBeaconLevel = _UpcSampledBeaconLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 6),
    _UpcSampledBeaconLevel_Type()
)
upcSampledBeaconLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcSampledBeaconLevel.setStatus("current")
_UpcCompensationRange_Type = OctetString
_UpcCompensationRange_Object = MibScalar
upcCompensationRange = _UpcCompensationRange_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 7),
    _UpcCompensationRange_Type()
)
upcCompensationRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcCompensationRange.setStatus("current")
_UpcCompensationRatio_Type = OctetString
_UpcCompensationRatio_Object = MibScalar
upcCompensationRatio = _UpcCompensationRatio_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 8),
    _UpcCompensationRatio_Type()
)
upcCompensationRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcCompensationRatio.setStatus("current")
_UpcStepSize_Type = UPCStepSizeType
_UpcStepSize_Object = MibScalar
upcStepSize = _UpcStepSize_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 9),
    _UpcStepSize_Type()
)
upcStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcStepSize.setStatus("current")
_UpcSlewRate_Type = UPCSlewRateType
_UpcSlewRate_Object = MibScalar
upcSlewRate = _UpcSlewRate_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 10),
    _UpcSlewRate_Type()
)
upcSlewRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcSlewRate.setStatus("current")
_UpcSamplePeriod_Type = OctetString
_UpcSamplePeriod_Object = MibScalar
upcSamplePeriod = _UpcSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 11),
    _UpcSamplePeriod_Type()
)
upcSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcSamplePeriod.setStatus("current")
_UpcAttenuation_Type = OctetString
_UpcAttenuation_Object = MibScalar
upcAttenuation = _UpcAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 12),
    _UpcAttenuation_Type()
)
upcAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcAttenuation.setStatus("current")
_UpcScintillation_Type = EnableType
_UpcScintillation_Object = MibScalar
upcScintillation = _UpcScintillation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 13),
    _UpcScintillation_Type()
)
upcScintillation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcScintillation.setStatus("current")
_UpcHysteresis_Type = OctetString
_UpcHysteresis_Object = MibScalar
upcHysteresis = _UpcHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 14),
    _UpcHysteresis_Type()
)
upcHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upcHysteresis.setStatus("current")
_ExpModule_ObjectIdentity = ObjectIdentity
expModule = _ExpModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15)
)
_ExpPresent_Type = YesNoType
_ExpPresent_Object = MibScalar
expPresent = _ExpPresent_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 1),
    _ExpPresent_Type()
)
expPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expPresent.setStatus("current")


class _ExpSerialNo_Type(Integer32):
    """Custom type expSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_ExpSerialNo_Type.__name__ = "Integer32"
_ExpSerialNo_Object = MibScalar
expSerialNo = _ExpSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 2),
    _ExpSerialNo_Type()
)
expSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expSerialNo.setStatus("current")
_ExpSummaryAlarm_Type = FaultType
_ExpSummaryAlarm_Object = MibScalar
expSummaryAlarm = _ExpSummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 3),
    _ExpSummaryAlarm_Type()
)
expSummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expSummaryAlarm.setStatus("current")
_ExpPTable_Object = MibTable
expPTable = _ExpPTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 4)
)
if mibBuilder.loadTexts:
    expPTable.setStatus("current")
_ExpPTableEntry_Object = MibTableRow
expPTableEntry = _ExpPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 4, 1)
)
expPTableEntry.setIndexNames(
    (0, "PEAKUPC-MIB", "expPIndex"),
)
if mibBuilder.loadTexts:
    expPTableEntry.setStatus("current")


class _ExpPIndex_Type(Integer32):
    """Custom type expPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ExpPIndex_Type.__name__ = "Integer32"
_ExpPIndex_Object = MibTableColumn
expPIndex = _ExpPIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 4, 1, 1),
    _ExpPIndex_Type()
)
expPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expPIndex.setStatus("current")
_ExpPPresent_Type = YesNoType
_ExpPPresent_Object = MibTableColumn
expPPresent = _ExpPPresent_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 4, 1, 2),
    _ExpPPresent_Type()
)
expPPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expPPresent.setStatus("current")
_ExpPPowered_Type = YesNoType
_ExpPPowered_Object = MibTableColumn
expPPowered = _ExpPPowered_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 4, 1, 3),
    _ExpPPowered_Type()
)
expPPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expPPowered.setStatus("current")
_ExpCTable_Object = MibTable
expCTable = _ExpCTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5)
)
if mibBuilder.loadTexts:
    expCTable.setStatus("current")
_ExpCTableEntry_Object = MibTableRow
expCTableEntry = _ExpCTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5, 1)
)
expCTableEntry.setIndexNames(
    (0, "PEAKUPC-MIB", "expCIndex"),
)
if mibBuilder.loadTexts:
    expCTableEntry.setStatus("current")


class _ExpCIndex_Type(Integer32):
    """Custom type expCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ExpCIndex_Type.__name__ = "Integer32"
_ExpCIndex_Object = MibTableColumn
expCIndex = _ExpCIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5, 1, 1),
    _ExpCIndex_Type()
)
expCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expCIndex.setStatus("current")
_ExpCChannelNo_Type = Integer32
_ExpCChannelNo_Object = MibTableColumn
expCChannelNo = _ExpCChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5, 1, 2),
    _ExpCChannelNo_Type()
)
expCChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expCChannelNo.setStatus("current")
_ExpCType_Type = OctetString
_ExpCType_Object = MibTableColumn
expCType = _ExpCType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5, 1, 3),
    _ExpCType_Type()
)
expCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expCType.setStatus("current")
_ExpCMode_Type = ChannelModeType
_ExpCMode_Object = MibTableColumn
expCMode = _ExpCMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5, 1, 4),
    _ExpCMode_Type()
)
expCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expCMode.setStatus("current")
_ExpCCompRatio_Type = OctetString
_ExpCCompRatio_Object = MibTableColumn
expCCompRatio = _ExpCCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5, 1, 5),
    _ExpCCompRatio_Type()
)
expCCompRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expCCompRatio.setStatus("current")
_ExpCAttenuation_Type = OctetString
_ExpCAttenuation_Object = MibTableColumn
expCAttenuation = _ExpCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5, 1, 6),
    _ExpCAttenuation_Type()
)
expCAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expCAttenuation.setStatus("current")
_ExpCOffset_Type = OctetString
_ExpCOffset_Object = MibTableColumn
expCOffset = _ExpCOffset_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 5, 1, 7),
    _ExpCOffset_Type()
)
expCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expCOffset.setStatus("current")
_ExpOKSince_Type = OctetString
_ExpOKSince_Object = MibScalar
expOKSince = _ExpOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 15, 100),
    _ExpOKSince_Type()
)
expOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOKSince.setStatus("current")
_UpcOKSince_Type = OctetString
_UpcOKSince_Object = MibScalar
upcOKSince = _UpcOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 100),
    _UpcOKSince_Type()
)
upcOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcOKSince.setStatus("current")
_UpcIntegers_ObjectIdentity = ObjectIdentity
upcIntegers = _UpcIntegers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 109)
)
_UpcIClearSkyBeaconLevel_Type = Integer32
_UpcIClearSkyBeaconLevel_Object = MibScalar
upcIClearSkyBeaconLevel = _UpcIClearSkyBeaconLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 109, 1),
    _UpcIClearSkyBeaconLevel_Type()
)
upcIClearSkyBeaconLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcIClearSkyBeaconLevel.setStatus("current")
_UpcISampledBeaconLevel_Type = Integer32
_UpcISampledBeaconLevel_Object = MibScalar
upcISampledBeaconLevel = _UpcISampledBeaconLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 109, 2),
    _UpcISampledBeaconLevel_Type()
)
upcISampledBeaconLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcISampledBeaconLevel.setStatus("current")
_UpcIAttenuation_Type = Integer32
_UpcIAttenuation_Object = MibScalar
upcIAttenuation = _UpcIAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 109, 3),
    _UpcIAttenuation_Type()
)
upcIAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcIAttenuation.setStatus("current")
_UpcConvGroups_ObjectIdentity = ObjectIdentity
upcConvGroups = _UpcConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110)
)
_UpcConvConformance_ObjectIdentity = ObjectIdentity
upcConvConformance = _UpcConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 111)
)

# Managed Objects groups

upcCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110, 1)
)
upcCNFReqGrp.setObjects(
      *(("PEAKUPC-MIB", "upcCChannelNo"),
        ("PEAKUPC-MIB", "upcCType"),
        ("PEAKUPC-MIB", "upcCMode"),
        ("PEAKUPC-MIB", "upcCCompRatio"),
        ("PEAKUPC-MIB", "upcClearSkyCalibrated"),
        ("PEAKUPC-MIB", "upcExtChannelsCalibrated"),
        ("PEAKUPC-MIB", "upcMode"),
        ("PEAKUPC-MIB", "upcClearSkyBeaconLevel"),
        ("PEAKUPC-MIB", "upcSampledBeaconLevel"),
        ("PEAKUPC-MIB", "upcCompensationRange"),
        ("PEAKUPC-MIB", "upcCompensationRatio"),
        ("PEAKUPC-MIB", "upcStepSize"),
        ("PEAKUPC-MIB", "upcSlewRate"),
        ("PEAKUPC-MIB", "upcSamplePeriod"),
        ("PEAKUPC-MIB", "upcAttenuation"),
        ("PEAKUPC-MIB", "upcOKSince"))
)
if mibBuilder.loadTexts:
    upcCNFReqGrp.setStatus("current")

upcCNFExtraChannelGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110, 2)
)
upcCNFExtraChannelGrp.setObjects(
      *(("PEAKUPC-MIB", "upcCAttenuation"),
        ("PEAKUPC-MIB", "upcCOffset"),
        ("PEAKUPC-MIB", "upcCExtExpected"),
        ("PEAKUPC-MIB", "upcCExtMissing"),
        ("PEAKUPC-MIB", "upcCSerialNo"))
)
if mibBuilder.loadTexts:
    upcCNFExtraChannelGrp.setStatus("current")

upcCNFScintillationGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110, 3)
)
upcCNFScintillationGrp.setObjects(
    ("PEAKUPC-MIB", "upcScintillation")
)
if mibBuilder.loadTexts:
    upcCNFScintillationGrp.setStatus("current")

upcCNFHysteresisGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110, 4)
)
upcCNFHysteresisGrp.setObjects(
    ("PEAKUPC-MIB", "upcHysteresis")
)
if mibBuilder.loadTexts:
    upcCNFHysteresisGrp.setStatus("current")

upcICNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110, 5)
)
upcICNFReqGrp.setObjects(
      *(("PEAKUPC-MIB", "upcIClearSkyBeaconLevel"),
        ("PEAKUPC-MIB", "upcISampledBeaconLevel"),
        ("PEAKUPC-MIB", "upcIAttenuation"))
)
if mibBuilder.loadTexts:
    upcICNFReqGrp.setStatus("current")

expCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110, 6)
)
expCNFReqGrp.setObjects(
    ("PEAKUPC-MIB", "expPresent")
)
if mibBuilder.loadTexts:
    expCNFReqGrp.setStatus("current")

expCNFAttachedGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110, 7)
)
expCNFAttachedGrp.setObjects(
      *(("PEAKUPC-MIB", "expSerialNo"),
        ("PEAKUPC-MIB", "expSummaryAlarm"),
        ("PEAKUPC-MIB", "expOKSince"),
        ("PEAKUPC-MIB", "expPPresent"),
        ("PEAKUPC-MIB", "expPPowered"))
)
if mibBuilder.loadTexts:
    expCNFAttachedGrp.setStatus("current")

expCNFChannelGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 110, 8)
)
expCNFChannelGrp.setObjects(
      *(("PEAKUPC-MIB", "expCChannelNo"),
        ("PEAKUPC-MIB", "expCType"),
        ("PEAKUPC-MIB", "expCMode"),
        ("PEAKUPC-MIB", "expCCompRatio"),
        ("PEAKUPC-MIB", "expCAttenuation"),
        ("PEAKUPC-MIB", "expCOffset"))
)
if mibBuilder.loadTexts:
    expCNFChannelGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

upcCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 9, 111, 1)
)
upcCNFCompliance.setObjects(
      *(("PEAKUPC-MIB", "upcCNFReqGrp"),
        ("PEAKUPC-MIB", "upcICNFReqGrp"),
        ("PEAKUPC-MIB", "upcCNFExtraChannelGrp"),
        ("PEAKUPC-MIB", "expCNFReqGrp"),
        ("PEAKUPC-MIB", "upcCNFScintillationGrp"),
        ("PEAKUPC-MIB", "upcCNFHysteresisGrp"),
        ("PEAKUPC-MIB", "expCNFAttachedGrp"),
        ("PEAKUPC-MIB", "expCNFChannelGrp"))
)
if mibBuilder.loadTexts:
    upcCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKUPC-MIB",
    **{"UPCCalibratedType": UPCCalibratedType,
       "UPCModeType": UPCModeType,
       "UPCStepSizeType": UPCStepSizeType,
       "UPCSlewRateType": UPCSlewRateType,
       "peakUPCModule": peakUPCModule,
       "upcCTable": upcCTable,
       "upcCTableEntry": upcCTableEntry,
       "upcCIndex": upcCIndex,
       "upcCChannelNo": upcCChannelNo,
       "upcCType": upcCType,
       "upcCMode": upcCMode,
       "upcCCompRatio": upcCCompRatio,
       "upcCAttenuation": upcCAttenuation,
       "upcCOffset": upcCOffset,
       "upcCExtExpected": upcCExtExpected,
       "upcCExtMissing": upcCExtMissing,
       "upcCSerialNo": upcCSerialNo,
       "upcClearSkyCalibrated": upcClearSkyCalibrated,
       "upcExtChannelsCalibrated": upcExtChannelsCalibrated,
       "upcMode": upcMode,
       "upcClearSkyBeaconLevel": upcClearSkyBeaconLevel,
       "upcSampledBeaconLevel": upcSampledBeaconLevel,
       "upcCompensationRange": upcCompensationRange,
       "upcCompensationRatio": upcCompensationRatio,
       "upcStepSize": upcStepSize,
       "upcSlewRate": upcSlewRate,
       "upcSamplePeriod": upcSamplePeriod,
       "upcAttenuation": upcAttenuation,
       "upcScintillation": upcScintillation,
       "upcHysteresis": upcHysteresis,
       "expModule": expModule,
       "expPresent": expPresent,
       "expSerialNo": expSerialNo,
       "expSummaryAlarm": expSummaryAlarm,
       "expPTable": expPTable,
       "expPTableEntry": expPTableEntry,
       "expPIndex": expPIndex,
       "expPPresent": expPPresent,
       "expPPowered": expPPowered,
       "expCTable": expCTable,
       "expCTableEntry": expCTableEntry,
       "expCIndex": expCIndex,
       "expCChannelNo": expCChannelNo,
       "expCType": expCType,
       "expCMode": expCMode,
       "expCCompRatio": expCCompRatio,
       "expCAttenuation": expCAttenuation,
       "expCOffset": expCOffset,
       "expOKSince": expOKSince,
       "upcOKSince": upcOKSince,
       "upcIntegers": upcIntegers,
       "upcIClearSkyBeaconLevel": upcIClearSkyBeaconLevel,
       "upcISampledBeaconLevel": upcISampledBeaconLevel,
       "upcIAttenuation": upcIAttenuation,
       "upcConvGroups": upcConvGroups,
       "upcCNFReqGrp": upcCNFReqGrp,
       "upcCNFExtraChannelGrp": upcCNFExtraChannelGrp,
       "upcCNFScintillationGrp": upcCNFScintillationGrp,
       "upcCNFHysteresisGrp": upcCNFHysteresisGrp,
       "upcICNFReqGrp": upcICNFReqGrp,
       "expCNFReqGrp": expCNFReqGrp,
       "expCNFAttachedGrp": expCNFAttachedGrp,
       "expCNFChannelGrp": expCNFChannelGrp,
       "upcConvConformance": upcConvConformance,
       "upcCNFCompliance": upcCNFCompliance}
)
