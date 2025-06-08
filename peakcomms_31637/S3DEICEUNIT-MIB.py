# SNMP MIB module (S3DEICEUNIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/S3DEICEUNIT-MIB.mib
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

(FaultStatus,
 OnOffType,
 YesNoType,
 s3Satcom) = mibBuilder.importSymbols(
    "S3DEFINITIONS-MIB",
    "FaultStatus",
    "OnOffType",
    "YesNoType",
    "s3Satcom")

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

s3Deice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 2)
)
if mibBuilder.loadTexts:
    s3Deice.setRevisions(
        ("2016-10-18 20:35",
         "2016-03-03 16:44",
         "2014-09-25 09:34",
         "2014-03-07 15:00",
         "2014-02-02 15:00",
         "2014-01-31 08:00",
         "2014-01-29 14:00",
         "2014-01-14 12:00",
         "2014-01-14 11:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DeIceCardType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("relayCard", 1),
          ("temperatureCard", 2),
          ("currentCard", 3))
    )



class RelayCardId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-99,
              -1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", -99),
          ("cpu", -1),
          ("relay1", 0),
          ("relay2", 1),
          ("relay3", 2),
          ("relay4", 3))
    )



class TempSensorTypes(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("pt100", 1),
          ("pt1000", 2),
          ("kty84v130", 3))
    )



class RelayGroupFunctionality(TextualConvention, Integer32):
    status = "current"
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("summaryAlarm", 1),
          ("stage1", 2),
          ("stage2", 3),
          ("stage3", 4),
          ("auxHeater1", 5),
          ("auxHeater2", 6),
          ("auxHeater3", 7),
          ("auxHeater4", 8),
          ("auxHeater5", 9),
          ("rainBlower", 10),
          ("stage1TB", 11),
          ("stage2TB", 12),
          ("stage3TB", 13),
          ("auxHeater1TB", 14),
          ("auxHeater2TB", 15),
          ("auxHeater3TB", 16),
          ("auxHeater4TB", 17),
          ("auxHeater5TB", 18),
          ("rainBlowerTB", 19))
    )



class InputFunction(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rainDetector", 1),
          ("iceDetector", 2),
          ("deIceEnable", 3),
          ("breakSupply", 4),
          ("auto", 5),
          ("forceOn", 6),
          ("enableStage2", 7),
          ("enableStage3", 8))
    )



class OperationalModes(TextualConvention, Integer32):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("independent", 1),
          ("followStage1", 2),
          ("followStage2", 3),
          ("followStage3", 4),
          ("followRainBlower", 5),
          ("followAuxHeater1", 6),
          ("followAuxHeater2", 7),
          ("followAuxHeater3", 8),
          ("followAuxHeater4", 9),
          ("followAuxHeater5", 10))
    )



class AuxModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceOff", 0),
          ("forceOn", 1),
          ("auto", 2))
    )



class CurrentSensorFunctions(TextualConvention, Integer32):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("misc", 1),
          ("stage1", 2),
          ("stage2", 3),
          ("stage3", 4),
          ("auxHeater1", 5),
          ("auxHeater2", 6),
          ("auxHeater3", 7),
          ("auxHeater4", 8),
          ("auxHeater5", 9),
          ("rainBlower", 10),
          ("stage123", 11))
    )



class TemperatureSensorFunctions(TextualConvention, Integer32):
    status = "current"
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
        *(("undefined", 0),
          ("misc", 1),
          ("stage1", 2),
          ("stage2", 3),
          ("stage3", 4),
          ("auxHeater1", 5),
          ("auxHeater2", 6),
          ("auxHeater3", 7),
          ("auxHeater4", 8),
          ("auxHeater5", 9),
          ("rainBlower", 10),
          ("stage123", 11),
          ("ambient", 12))
    )



class AuxCircuitFunctions(TextualConvention, Integer32):
    status = "current"
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
        *(("undefined", 0),
          ("rainBlower", 1),
          ("auxHeater1", 2),
          ("auxHeater2", 3),
          ("auxHeater3", 4),
          ("auxHeater4", 5),
          ("auxHeater5", 6))
    )



class AlarmEnabledType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("lower", 1),
          ("upper", 2),
          ("upperAndLower", 3),
          ("sensorFault", 4))
    )



class MainDeiceModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("modeOff", 0),
          ("modeAuto", 1),
          ("modeOn", 2),
          ("modeExtEnableOff", 4),
          ("modeExtEnableAuto", 5),
          ("modeExtEnableOn", 6),
          ("modeExternalAuto", 9),
          ("modeExternalForceOn", 10))
    )



class ExternalEnableMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externEnableModeManual", 0),
          ("externEnableModeOffAuto", 1),
          ("externEnableModeOffOn", 2))
    )



class AuxModePendingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pendingNone", 0),
          ("pendingOff", 1),
          ("pendingOn", 2))
    )



# MIB Managed Objects in the order of their OIDs

_GeneralInfoTable_Object = MibTable
generalInfoTable = _GeneralInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 1)
)
if mibBuilder.loadTexts:
    generalInfoTable.setStatus("current")
_GeneralInfoTableEntry_Object = MibTableRow
generalInfoTableEntry = _GeneralInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 1, 1)
)
generalInfoTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "generalInfoTableEntryIndex"),
)
if mibBuilder.loadTexts:
    generalInfoTableEntry.setStatus("current")


class _GeneralInfoTableEntryIndex_Type(Integer32):
    """Custom type generalInfoTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeneralInfoTableEntryIndex_Type.__name__ = "Integer32"
_GeneralInfoTableEntryIndex_Object = MibTableColumn
generalInfoTableEntryIndex = _GeneralInfoTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 1, 1, 1),
    _GeneralInfoTableEntryIndex_Type()
)
generalInfoTableEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generalInfoTableEntryIndex.setStatus("current")


class _NumRelayGroups_Type(Integer32):
    """Custom type numRelayGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36),
    )


_NumRelayGroups_Type.__name__ = "Integer32"
_NumRelayGroups_Object = MibTableColumn
numRelayGroups = _NumRelayGroups_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 1, 1, 2),
    _NumRelayGroups_Type()
)
numRelayGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numRelayGroups.setStatus("current")


class _NumCurrentCards_Type(Integer32):
    """Custom type numCurrentCards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NumCurrentCards_Type.__name__ = "Integer32"
_NumCurrentCards_Object = MibTableColumn
numCurrentCards = _NumCurrentCards_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 1, 1, 3),
    _NumCurrentCards_Type()
)
numCurrentCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCurrentCards.setStatus("current")


class _NumTemperatureCards_Type(Integer32):
    """Custom type numTemperatureCards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NumTemperatureCards_Type.__name__ = "Integer32"
_NumTemperatureCards_Object = MibTableColumn
numTemperatureCards = _NumTemperatureCards_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 1, 1, 4),
    _NumTemperatureCards_Type()
)
numTemperatureCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numTemperatureCards.setStatus("current")
_OptionCardTable_Object = MibTable
optionCardTable = _OptionCardTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2)
)
if mibBuilder.loadTexts:
    optionCardTable.setStatus("current")
_OptionCardTableEntry_Object = MibTableRow
optionCardTableEntry = _OptionCardTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1)
)
optionCardTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "optionCardTableEntryIndex"),
)
if mibBuilder.loadTexts:
    optionCardTableEntry.setStatus("current")


class _OptionCardTableEntryIndex_Type(Integer32):
    """Custom type optionCardTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 68),
    )


_OptionCardTableEntryIndex_Type.__name__ = "Integer32"
_OptionCardTableEntryIndex_Object = MibTableColumn
optionCardTableEntryIndex = _OptionCardTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1, 1),
    _OptionCardTableEntryIndex_Type()
)
optionCardTableEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optionCardTableEntryIndex.setStatus("current")
_OptionCardType_Type = DeIceCardType
_OptionCardType_Object = MibTableColumn
optionCardType = _OptionCardType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1, 2),
    _OptionCardType_Type()
)
optionCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optionCardType.setStatus("current")
_OptionCardAddress_Type = Integer32
_OptionCardAddress_Object = MibTableColumn
optionCardAddress = _OptionCardAddress_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1, 3),
    _OptionCardAddress_Type()
)
optionCardAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optionCardAddress.setStatus("current")


class _OptionCardName_Type(OctetString):
    """Custom type optionCardName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OptionCardName_Type.__name__ = "OctetString"
_OptionCardName_Object = MibTableColumn
optionCardName = _OptionCardName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1, 4),
    _OptionCardName_Type()
)
optionCardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optionCardName.setStatus("current")


class _OptionCardFirmwareRevision_Type(OctetString):
    """Custom type optionCardFirmwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OptionCardFirmwareRevision_Type.__name__ = "OctetString"
_OptionCardFirmwareRevision_Object = MibTableColumn
optionCardFirmwareRevision = _OptionCardFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1, 5),
    _OptionCardFirmwareRevision_Type()
)
optionCardFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optionCardFirmwareRevision.setStatus("current")


class _OptionCardSerialNumber_Type(OctetString):
    """Custom type optionCardSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_OptionCardSerialNumber_Type.__name__ = "OctetString"
_OptionCardSerialNumber_Object = MibTableColumn
optionCardSerialNumber = _OptionCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1, 6),
    _OptionCardSerialNumber_Type()
)
optionCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optionCardSerialNumber.setStatus("current")
_OptionCardOptionVal_Type = Integer32
_OptionCardOptionVal_Object = MibTableColumn
optionCardOptionVal = _OptionCardOptionVal_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1, 7),
    _OptionCardOptionVal_Type()
)
optionCardOptionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optionCardOptionVal.setStatus("current")
_OptionCardCommsFail_Type = FaultStatus
_OptionCardCommsFail_Object = MibTableColumn
optionCardCommsFail = _OptionCardCommsFail_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 2, 1, 8),
    _OptionCardCommsFail_Type()
)
optionCardCommsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optionCardCommsFail.setStatus("current")
_RelayGroupTable_Object = MibTable
relayGroupTable = _RelayGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3)
)
if mibBuilder.loadTexts:
    relayGroupTable.setStatus("current")
_RelayGroupTableEntry_Object = MibTableRow
relayGroupTableEntry = _RelayGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1)
)
relayGroupTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "relayGroupTableEntryIndex"),
)
if mibBuilder.loadTexts:
    relayGroupTableEntry.setStatus("current")


class _RelayGroupTableEntryIndex_Type(Integer32):
    """Custom type relayGroupTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36),
    )


_RelayGroupTableEntryIndex_Type.__name__ = "Integer32"
_RelayGroupTableEntryIndex_Object = MibTableColumn
relayGroupTableEntryIndex = _RelayGroupTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 1),
    _RelayGroupTableEntryIndex_Type()
)
relayGroupTableEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    relayGroupTableEntryIndex.setStatus("current")


class _RelayGroupName_Type(OctetString):
    """Custom type relayGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RelayGroupName_Type.__name__ = "OctetString"
_RelayGroupName_Object = MibTableColumn
relayGroupName = _RelayGroupName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 2),
    _RelayGroupName_Type()
)
relayGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupName.setStatus("current")
_RelayGroupFunction_Type = RelayGroupFunctionality
_RelayGroupFunction_Object = MibTableColumn
relayGroupFunction = _RelayGroupFunction_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 3),
    _RelayGroupFunction_Type()
)
relayGroupFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupFunction.setStatus("current")
_RelayGroupBoardID0_Type = RelayCardId
_RelayGroupBoardID0_Object = MibTableColumn
relayGroupBoardID0 = _RelayGroupBoardID0_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 4),
    _RelayGroupBoardID0_Type()
)
relayGroupBoardID0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupBoardID0.setStatus("current")


class _RelayGroupIndexNum0_Type(Integer32):
    """Custom type relayGroupIndexNum0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_RelayGroupIndexNum0_Type.__name__ = "Integer32"
_RelayGroupIndexNum0_Object = MibTableColumn
relayGroupIndexNum0 = _RelayGroupIndexNum0_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 5),
    _RelayGroupIndexNum0_Type()
)
relayGroupIndexNum0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupIndexNum0.setStatus("current")
_RelayGroupInverted0_Type = YesNoType
_RelayGroupInverted0_Object = MibTableColumn
relayGroupInverted0 = _RelayGroupInverted0_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 6),
    _RelayGroupInverted0_Type()
)
relayGroupInverted0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupInverted0.setStatus("current")
_RelayGroupBoardID1_Type = RelayCardId
_RelayGroupBoardID1_Object = MibTableColumn
relayGroupBoardID1 = _RelayGroupBoardID1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 7),
    _RelayGroupBoardID1_Type()
)
relayGroupBoardID1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupBoardID1.setStatus("current")


class _RelayGroupIndexNum1_Type(Integer32):
    """Custom type relayGroupIndexNum1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_RelayGroupIndexNum1_Type.__name__ = "Integer32"
_RelayGroupIndexNum1_Object = MibTableColumn
relayGroupIndexNum1 = _RelayGroupIndexNum1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 8),
    _RelayGroupIndexNum1_Type()
)
relayGroupIndexNum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupIndexNum1.setStatus("current")
_RelayGroupInverted1_Type = YesNoType
_RelayGroupInverted1_Object = MibTableColumn
relayGroupInverted1 = _RelayGroupInverted1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 9),
    _RelayGroupInverted1_Type()
)
relayGroupInverted1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupInverted1.setStatus("current")
_RelayGroupBoardID2_Type = RelayCardId
_RelayGroupBoardID2_Object = MibTableColumn
relayGroupBoardID2 = _RelayGroupBoardID2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 10),
    _RelayGroupBoardID2_Type()
)
relayGroupBoardID2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupBoardID2.setStatus("current")


class _RelayGroupIndexNum2_Type(Integer32):
    """Custom type relayGroupIndexNum2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_RelayGroupIndexNum2_Type.__name__ = "Integer32"
_RelayGroupIndexNum2_Object = MibTableColumn
relayGroupIndexNum2 = _RelayGroupIndexNum2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 11),
    _RelayGroupIndexNum2_Type()
)
relayGroupIndexNum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupIndexNum2.setStatus("current")
_RelayGroupInverted2_Type = YesNoType
_RelayGroupInverted2_Object = MibTableColumn
relayGroupInverted2 = _RelayGroupInverted2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 3, 1, 12),
    _RelayGroupInverted2_Type()
)
relayGroupInverted2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayGroupInverted2.setStatus("current")
_CurrentSensorTable_Object = MibTable
currentSensorTable = _CurrentSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4)
)
if mibBuilder.loadTexts:
    currentSensorTable.setStatus("current")
_CurrentSensorTableEntry_Object = MibTableRow
currentSensorTableEntry = _CurrentSensorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1)
)
currentSensorTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "currentSensorTableIndex"),
)
if mibBuilder.loadTexts:
    currentSensorTableEntry.setStatus("current")


class _CurrentSensorTableIndex_Type(Integer32):
    """Custom type currentSensorTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CurrentSensorTableIndex_Type.__name__ = "Integer32"
_CurrentSensorTableIndex_Object = MibTableColumn
currentSensorTableIndex = _CurrentSensorTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 1),
    _CurrentSensorTableIndex_Type()
)
currentSensorTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentSensorTableIndex.setStatus("current")


class _CurrentSensorName_Type(OctetString):
    """Custom type currentSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CurrentSensorName_Type.__name__ = "OctetString"
_CurrentSensorName_Object = MibTableColumn
currentSensorName = _CurrentSensorName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 2),
    _CurrentSensorName_Type()
)
currentSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentSensorName.setStatus("current")
_CurrentSensorFunction_Type = CurrentSensorFunctions
_CurrentSensorFunction_Object = MibTableColumn
currentSensorFunction = _CurrentSensorFunction_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 3),
    _CurrentSensorFunction_Type()
)
currentSensorFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentSensorFunction.setStatus("current")


class _UpperLimit0_Type(Integer32):
    """Custom type upperLimit0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3300),
    )


_UpperLimit0_Type.__name__ = "Integer32"
_UpperLimit0_Object = MibTableColumn
upperLimit0 = _UpperLimit0_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 4),
    _UpperLimit0_Type()
)
upperLimit0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upperLimit0.setStatus("current")


class _LowerLimit0_Type(Integer32):
    """Custom type lowerLimit0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3300),
    )


_LowerLimit0_Type.__name__ = "Integer32"
_LowerLimit0_Object = MibTableColumn
lowerLimit0 = _LowerLimit0_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 5),
    _LowerLimit0_Type()
)
lowerLimit0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowerLimit0.setStatus("current")


class _UpperLimit1_Type(Integer32):
    """Custom type upperLimit1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3300),
    )


_UpperLimit1_Type.__name__ = "Integer32"
_UpperLimit1_Object = MibTableColumn
upperLimit1 = _UpperLimit1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 6),
    _UpperLimit1_Type()
)
upperLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upperLimit1.setStatus("current")


class _LowerLimit1_Type(Integer32):
    """Custom type lowerLimit1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3300),
    )


_LowerLimit1_Type.__name__ = "Integer32"
_LowerLimit1_Object = MibTableColumn
lowerLimit1 = _LowerLimit1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 7),
    _LowerLimit1_Type()
)
lowerLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowerLimit1.setStatus("current")


class _UpperLimit2_Type(Integer32):
    """Custom type upperLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3300),
    )


_UpperLimit2_Type.__name__ = "Integer32"
_UpperLimit2_Object = MibTableColumn
upperLimit2 = _UpperLimit2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 8),
    _UpperLimit2_Type()
)
upperLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upperLimit2.setStatus("current")


class _LowerLimit2_Type(Integer32):
    """Custom type lowerLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3300),
    )


_LowerLimit2_Type.__name__ = "Integer32"
_LowerLimit2_Object = MibTableColumn
lowerLimit2 = _LowerLimit2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 9),
    _LowerLimit2_Type()
)
lowerLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowerLimit2.setStatus("current")
_AlarmLimitsEnabled_Type = AlarmEnabledType
_AlarmLimitsEnabled_Object = MibTableColumn
alarmLimitsEnabled = _AlarmLimitsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 4, 1, 10),
    _AlarmLimitsEnabled_Type()
)
alarmLimitsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLimitsEnabled.setStatus("current")
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("current")
_TemperatureSensorTableEntry_Object = MibTableRow
temperatureSensorTableEntry = _TemperatureSensorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1)
)
temperatureSensorTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "temperatureSensorTableIndex"),
)
if mibBuilder.loadTexts:
    temperatureSensorTableEntry.setStatus("current")


class _TemperatureSensorTableIndex_Type(Integer32):
    """Custom type temperatureSensorTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TemperatureSensorTableIndex_Type.__name__ = "Integer32"
_TemperatureSensorTableIndex_Object = MibTableColumn
temperatureSensorTableIndex = _TemperatureSensorTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1, 1),
    _TemperatureSensorTableIndex_Type()
)
temperatureSensorTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temperatureSensorTableIndex.setStatus("current")
_TempSensorType_Type = TempSensorTypes
_TempSensorType_Object = MibTableColumn
tempSensorType = _TempSensorType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1, 2),
    _TempSensorType_Type()
)
tempSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorType.setStatus("current")


class _TempSensorName_Type(OctetString):
    """Custom type tempSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TempSensorName_Type.__name__ = "OctetString"
_TempSensorName_Object = MibTableColumn
tempSensorName = _TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1, 3),
    _TempSensorName_Type()
)
tempSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensorName.setStatus("current")
_TempSensorFunction_Type = TemperatureSensorFunctions
_TempSensorFunction_Object = MibTableColumn
tempSensorFunction = _TempSensorFunction_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1, 4),
    _TempSensorFunction_Type()
)
tempSensorFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensorFunction.setStatus("current")
_TempSensorOffset2Wire_Type = Integer32
_TempSensorOffset2Wire_Object = MibTableColumn
tempSensorOffset2Wire = _TempSensorOffset2Wire_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1, 5),
    _TempSensorOffset2Wire_Type()
)
tempSensorOffset2Wire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensorOffset2Wire.setStatus("current")


class _TempUpperLimitInCx10_Type(Integer32):
    """Custom type tempUpperLimitInCx10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 3000),
    )


_TempUpperLimitInCx10_Type.__name__ = "Integer32"
_TempUpperLimitInCx10_Object = MibTableColumn
tempUpperLimitInCx10 = _TempUpperLimitInCx10_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1, 6),
    _TempUpperLimitInCx10_Type()
)
tempUpperLimitInCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempUpperLimitInCx10.setStatus("current")


class _TempLowerLimitInCx10_Type(Integer32):
    """Custom type tempLowerLimitInCx10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 3000),
    )


_TempLowerLimitInCx10_Type.__name__ = "Integer32"
_TempLowerLimitInCx10_Object = MibTableColumn
tempLowerLimitInCx10 = _TempLowerLimitInCx10_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1, 7),
    _TempLowerLimitInCx10_Type()
)
tempLowerLimitInCx10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowerLimitInCx10.setStatus("current")
_AlarmLimitsEn_Type = AlarmEnabledType
_AlarmLimitsEn_Object = MibTableColumn
alarmLimitsEn = _AlarmLimitsEn_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 5, 1, 8),
    _AlarmLimitsEn_Type()
)
alarmLimitsEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLimitsEn.setStatus("current")
_OptoInputsTable_Object = MibTable
optoInputsTable = _OptoInputsTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 6)
)
if mibBuilder.loadTexts:
    optoInputsTable.setStatus("current")
_OptoInputsEntry_Object = MibTableRow
optoInputsEntry = _OptoInputsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 6, 1)
)
optoInputsEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "optoInputsEntryIndex"),
)
if mibBuilder.loadTexts:
    optoInputsEntry.setStatus("current")


class _OptoInputsEntryIndex_Type(Integer32):
    """Custom type optoInputsEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OptoInputsEntryIndex_Type.__name__ = "Integer32"
_OptoInputsEntryIndex_Object = MibTableColumn
optoInputsEntryIndex = _OptoInputsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 6, 1, 1),
    _OptoInputsEntryIndex_Type()
)
optoInputsEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optoInputsEntryIndex.setStatus("current")


class _OptoInputName_Type(OctetString):
    """Custom type optoInputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OptoInputName_Type.__name__ = "OctetString"
_OptoInputName_Object = MibTableColumn
optoInputName = _OptoInputName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 6, 1, 2),
    _OptoInputName_Type()
)
optoInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optoInputName.setStatus("current")
_OptoInputFunction_Type = InputFunction
_OptoInputFunction_Object = MibTableColumn
optoInputFunction = _OptoInputFunction_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 6, 1, 3),
    _OptoInputFunction_Type()
)
optoInputFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optoInputFunction.setStatus("current")
_OptoInputInverted_Type = YesNoType
_OptoInputInverted_Object = MibTableColumn
optoInputInverted = _OptoInputInverted_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 6, 1, 4),
    _OptoInputInverted_Type()
)
optoInputInverted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optoInputInverted.setStatus("current")
_DeIceControllerConfigTable_Object = MibTable
deIceControllerConfigTable = _DeIceControllerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7)
)
if mibBuilder.loadTexts:
    deIceControllerConfigTable.setStatus("current")
_DeIceControllerConfigEntry_Object = MibTableRow
deIceControllerConfigEntry = _DeIceControllerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1)
)
deIceControllerConfigEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "deIceControllerConfigEntryIndex"),
)
if mibBuilder.loadTexts:
    deIceControllerConfigEntry.setStatus("current")


class _DeIceControllerConfigEntryIndex_Type(Integer32):
    """Custom type deIceControllerConfigEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DeIceControllerConfigEntryIndex_Type.__name__ = "Integer32"
_DeIceControllerConfigEntryIndex_Object = MibTableColumn
deIceControllerConfigEntryIndex = _DeIceControllerConfigEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 1),
    _DeIceControllerConfigEntryIndex_Type()
)
deIceControllerConfigEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deIceControllerConfigEntryIndex.setStatus("current")


class _SystemName_Type(OctetString):
    """Custom type systemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SystemName_Type.__name__ = "OctetString"
_SystemName_Object = MibTableColumn
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 2),
    _SystemName_Type()
)
systemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemName.setStatus("current")
_RainDetectorFitted_Type = YesNoType
_RainDetectorFitted_Object = MibTableColumn
rainDetectorFitted = _RainDetectorFitted_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 3),
    _RainDetectorFitted_Type()
)
rainDetectorFitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rainDetectorFitted.setStatus("current")
_UseRainSensorAndTambAsIceDetector_Type = YesNoType
_UseRainSensorAndTambAsIceDetector_Object = MibTableColumn
useRainSensorAndTambAsIceDetector = _UseRainSensorAndTambAsIceDetector_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 4),
    _UseRainSensorAndTambAsIceDetector_Type()
)
useRainSensorAndTambAsIceDetector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useRainSensorAndTambAsIceDetector.setStatus("current")


class _IceFormationUpperTemp_Type(Integer32):
    """Custom type iceFormationUpperTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_IceFormationUpperTemp_Type.__name__ = "Integer32"
_IceFormationUpperTemp_Object = MibTableColumn
iceFormationUpperTemp = _IceFormationUpperTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 5),
    _IceFormationUpperTemp_Type()
)
iceFormationUpperTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iceFormationUpperTemp.setStatus("current")


class _IceFormationLowerTemp_Type(Integer32):
    """Custom type iceFormationLowerTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 0),
    )


_IceFormationLowerTemp_Type.__name__ = "Integer32"
_IceFormationLowerTemp_Object = MibTableColumn
iceFormationLowerTemp = _IceFormationLowerTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 6),
    _IceFormationLowerTemp_Type()
)
iceFormationLowerTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iceFormationLowerTemp.setStatus("current")
_IceDetectorFitted_Type = YesNoType
_IceDetectorFitted_Object = MibTableColumn
iceDetectorFitted = _IceDetectorFitted_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 7),
    _IceDetectorFitted_Type()
)
iceDetectorFitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iceDetectorFitted.setStatus("current")
_AlarmActivationDelay_Type = Integer32
_AlarmActivationDelay_Object = MibTableColumn
alarmActivationDelay = _AlarmActivationDelay_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 8),
    _AlarmActivationDelay_Type()
)
alarmActivationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmActivationDelay.setStatus("current")
_RestartController_Type = YesNoType
_RestartController_Object = MibTableColumn
restartController = _RestartController_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 9),
    _RestartController_Type()
)
restartController.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartController.setStatus("current")


class _BreakSupplyName_Type(OctetString):
    """Custom type breakSupplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BreakSupplyName_Type.__name__ = "OctetString"
_BreakSupplyName_Object = MibTableColumn
breakSupplyName = _BreakSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 10),
    _BreakSupplyName_Type()
)
breakSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakSupplyName.setStatus("current")


class _ExtEnableName_Type(OctetString):
    """Custom type extEnableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtEnableName_Type.__name__ = "OctetString"
_ExtEnableName_Object = MibTableColumn
extEnableName = _ExtEnableName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 11),
    _ExtEnableName_Type()
)
extEnableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extEnableName.setStatus("current")
_CurrentAlarmDelaySec_Type = Integer32
_CurrentAlarmDelaySec_Object = MibTableColumn
currentAlarmDelaySec = _CurrentAlarmDelaySec_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 12),
    _CurrentAlarmDelaySec_Type()
)
currentAlarmDelaySec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentAlarmDelaySec.setStatus("current")
_ExtEnableFitted_Type = YesNoType
_ExtEnableFitted_Object = MibTableColumn
extEnableFitted = _ExtEnableFitted_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 7, 1, 13),
    _ExtEnableFitted_Type()
)
extEnableFitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEnableFitted.setStatus("current")
_MainDeIceConfigTable_Object = MibTable
mainDeIceConfigTable = _MainDeIceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8)
)
if mibBuilder.loadTexts:
    mainDeIceConfigTable.setStatus("current")
_MainDeIceConfigEntry_Object = MibTableRow
mainDeIceConfigEntry = _MainDeIceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1)
)
mainDeIceConfigEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "mainDeIceConfigEntryIndex"),
)
if mibBuilder.loadTexts:
    mainDeIceConfigEntry.setStatus("current")


class _MainDeIceConfigEntryIndex_Type(Integer32):
    """Custom type mainDeIceConfigEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MainDeIceConfigEntryIndex_Type.__name__ = "Integer32"
_MainDeIceConfigEntryIndex_Object = MibTableColumn
mainDeIceConfigEntryIndex = _MainDeIceConfigEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 1),
    _MainDeIceConfigEntryIndex_Type()
)
mainDeIceConfigEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainDeIceConfigEntryIndex.setStatus("current")


class _NumDeIceStages_Type(Integer32):
    """Custom type numDeIceStages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NumDeIceStages_Type.__name__ = "Integer32"
_NumDeIceStages_Object = MibTableColumn
numDeIceStages = _NumDeIceStages_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 2),
    _NumDeIceStages_Type()
)
numDeIceStages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numDeIceStages.setStatus("current")
_Stage1UsesBreakPower_Type = YesNoType
_Stage1UsesBreakPower_Object = MibTableColumn
stage1UsesBreakPower = _Stage1UsesBreakPower_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 3),
    _Stage1UsesBreakPower_Type()
)
stage1UsesBreakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage1UsesBreakPower.setStatus("current")
_Stage2UsesBreakPower_Type = YesNoType
_Stage2UsesBreakPower_Object = MibTableColumn
stage2UsesBreakPower = _Stage2UsesBreakPower_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 4),
    _Stage2UsesBreakPower_Type()
)
stage2UsesBreakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage2UsesBreakPower.setStatus("current")
_Stage3UsesBreakPower_Type = YesNoType
_Stage3UsesBreakPower_Object = MibTableColumn
stage3UsesBreakPower = _Stage3UsesBreakPower_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 5),
    _Stage3UsesBreakPower_Type()
)
stage3UsesBreakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage3UsesBreakPower.setStatus("current")
_Stage123ObeysExtEnable_Type = YesNoType
_Stage123ObeysExtEnable_Object = MibTableColumn
stage123ObeysExtEnable = _Stage123ObeysExtEnable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 6),
    _Stage123ObeysExtEnable_Type()
)
stage123ObeysExtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage123ObeysExtEnable.setStatus("current")
_ActivationDelayStage1_Type = Integer32
_ActivationDelayStage1_Object = MibTableColumn
activationDelayStage1 = _ActivationDelayStage1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 7),
    _ActivationDelayStage1_Type()
)
activationDelayStage1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activationDelayStage1.setStatus("current")
_ActivationDelayStage2_Type = Integer32
_ActivationDelayStage2_Object = MibTableColumn
activationDelayStage2 = _ActivationDelayStage2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 8),
    _ActivationDelayStage2_Type()
)
activationDelayStage2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activationDelayStage2.setStatus("current")
_ActivationDelayStage3_Type = Integer32
_ActivationDelayStage3_Object = MibTableColumn
activationDelayStage3 = _ActivationDelayStage3_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 9),
    _ActivationDelayStage3_Type()
)
activationDelayStage3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activationDelayStage3.setStatus("current")
_RunOnTimeStage1_Type = Integer32
_RunOnTimeStage1_Object = MibTableColumn
runOnTimeStage1 = _RunOnTimeStage1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 10),
    _RunOnTimeStage1_Type()
)
runOnTimeStage1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runOnTimeStage1.setStatus("current")
_RunOnTimeStage2_Type = Integer32
_RunOnTimeStage2_Object = MibTableColumn
runOnTimeStage2 = _RunOnTimeStage2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 11),
    _RunOnTimeStage2_Type()
)
runOnTimeStage2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runOnTimeStage2.setStatus("current")
_RunOnTimeStage3_Type = Integer32
_RunOnTimeStage3_Object = MibTableColumn
runOnTimeStage3 = _RunOnTimeStage3_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 12),
    _RunOnTimeStage3_Type()
)
runOnTimeStage3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runOnTimeStage3.setStatus("current")


class _AutoMode_Type(Integer32):
    """Custom type autoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AutoMode_Type.__name__ = "Integer32"
_AutoMode_Object = MibTableColumn
autoMode = _AutoMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 13),
    _AutoMode_Type()
)
autoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoMode.setStatus("deprecated")


class _ForceOn_Type(Integer32):
    """Custom type forceOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ForceOn_Type.__name__ = "Integer32"
_ForceOn_Object = MibTableColumn
forceOn = _ForceOn_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 14),
    _ForceOn_Type()
)
forceOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forceOn.setStatus("deprecated")


class _Stage2Enabled_Type(Integer32):
    """Custom type stage2Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Stage2Enabled_Type.__name__ = "Integer32"
_Stage2Enabled_Object = MibTableColumn
stage2Enabled = _Stage2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 15),
    _Stage2Enabled_Type()
)
stage2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage2Enabled.setStatus("current")


class _Stage3Enabled_Type(Integer32):
    """Custom type stage3Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Stage3Enabled_Type.__name__ = "Integer32"
_Stage3Enabled_Object = MibTableColumn
stage3Enabled = _Stage3Enabled_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 16),
    _Stage3Enabled_Type()
)
stage3Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage3Enabled.setStatus("current")
_MainDeIceMode_Type = MainDeiceModeType
_MainDeIceMode_Object = MibTableColumn
mainDeIceMode = _MainDeIceMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 17),
    _MainDeIceMode_Type()
)
mainDeIceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainDeIceMode.setStatus("current")
_ExtEnableMode_Type = ExternalEnableMode
_ExtEnableMode_Object = MibTableColumn
extEnableMode = _ExtEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 18),
    _ExtEnableMode_Type()
)
extEnableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEnableMode.setStatus("current")
_Stage1TempSensorFn_Type = TemperatureSensorFunctions
_Stage1TempSensorFn_Object = MibTableColumn
stage1TempSensorFn = _Stage1TempSensorFn_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 19),
    _Stage1TempSensorFn_Type()
)
stage1TempSensorFn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage1TempSensorFn.setStatus("current")
_Stage2TempSensorFn_Type = TemperatureSensorFunctions
_Stage2TempSensorFn_Object = MibTableColumn
stage2TempSensorFn = _Stage2TempSensorFn_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 20),
    _Stage2TempSensorFn_Type()
)
stage2TempSensorFn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage2TempSensorFn.setStatus("current")
_Stage3TempSensorFn_Type = TemperatureSensorFunctions
_Stage3TempSensorFn_Object = MibTableColumn
stage3TempSensorFn = _Stage3TempSensorFn_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 21),
    _Stage3TempSensorFn_Type()
)
stage3TempSensorFn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage3TempSensorFn.setStatus("current")
_Stage1OnTemp_Type = Integer32
_Stage1OnTemp_Object = MibTableColumn
stage1OnTemp = _Stage1OnTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 22),
    _Stage1OnTemp_Type()
)
stage1OnTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage1OnTemp.setStatus("current")
_Stage1OffTemp_Type = Integer32
_Stage1OffTemp_Object = MibTableColumn
stage1OffTemp = _Stage1OffTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 23),
    _Stage1OffTemp_Type()
)
stage1OffTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage1OffTemp.setStatus("current")
_Stage2OnTemp_Type = Integer32
_Stage2OnTemp_Object = MibTableColumn
stage2OnTemp = _Stage2OnTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 24),
    _Stage2OnTemp_Type()
)
stage2OnTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage2OnTemp.setStatus("current")
_Stage2OffTemp_Type = Integer32
_Stage2OffTemp_Object = MibTableColumn
stage2OffTemp = _Stage2OffTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 25),
    _Stage2OffTemp_Type()
)
stage2OffTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage2OffTemp.setStatus("current")
_Stage3OnTemp_Type = Integer32
_Stage3OnTemp_Object = MibTableColumn
stage3OnTemp = _Stage3OnTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 26),
    _Stage3OnTemp_Type()
)
stage3OnTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage3OnTemp.setStatus("current")
_Stage3OffTemp_Type = Integer32
_Stage3OffTemp_Object = MibTableColumn
stage3OffTemp = _Stage3OffTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 8, 1, 27),
    _Stage3OffTemp_Type()
)
stage3OffTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stage3OffTemp.setStatus("current")
_RelayStatusTable_Object = MibTable
relayStatusTable = _RelayStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 9)
)
if mibBuilder.loadTexts:
    relayStatusTable.setStatus("current")
_RelayStatusTableEntry_Object = MibTableRow
relayStatusTableEntry = _RelayStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 9, 1)
)
relayStatusTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "relayStatusTableIndex"),
)
if mibBuilder.loadTexts:
    relayStatusTableEntry.setStatus("current")


class _RelayStatusTableIndex_Type(Integer32):
    """Custom type relayStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36),
    )


_RelayStatusTableIndex_Type.__name__ = "Integer32"
_RelayStatusTableIndex_Object = MibTableColumn
relayStatusTableIndex = _RelayStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 9, 1, 1),
    _RelayStatusTableIndex_Type()
)
relayStatusTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    relayStatusTableIndex.setStatus("current")
_RelayState_Type = OnOffType
_RelayState_Object = MibTableColumn
relayState = _RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 9, 1, 2),
    _RelayState_Type()
)
relayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayState.setStatus("current")
_RelayOnTime_Type = DateAndTime
_RelayOnTime_Object = MibTableColumn
relayOnTime = _RelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 9, 1, 3),
    _RelayOnTime_Type()
)
relayOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayOnTime.setStatus("current")
_RelayOffTime_Type = DateAndTime
_RelayOffTime_Object = MibTableColumn
relayOffTime = _RelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 9, 1, 4),
    _RelayOffTime_Type()
)
relayOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayOffTime.setStatus("current")
_CurrentStatusTable_Object = MibTable
currentStatusTable = _CurrentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 10)
)
if mibBuilder.loadTexts:
    currentStatusTable.setStatus("current")
_CurrentStatusTableEntry_Object = MibTableRow
currentStatusTableEntry = _CurrentStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 10, 1)
)
currentStatusTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "currentStatusTableIndex"),
)
if mibBuilder.loadTexts:
    currentStatusTableEntry.setStatus("current")


class _CurrentStatusTableIndex_Type(Integer32):
    """Custom type currentStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CurrentStatusTableIndex_Type.__name__ = "Integer32"
_CurrentStatusTableIndex_Object = MibTableColumn
currentStatusTableIndex = _CurrentStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 10, 1, 1),
    _CurrentStatusTableIndex_Type()
)
currentStatusTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentStatusTableIndex.setStatus("current")


class _CurrentInAmpsx100_Type(Integer32):
    """Custom type currentInAmpsx100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3300),
    )


_CurrentInAmpsx100_Type.__name__ = "Integer32"
_CurrentInAmpsx100_Object = MibTableColumn
currentInAmpsx100 = _CurrentInAmpsx100_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 10, 1, 2),
    _CurrentInAmpsx100_Type()
)
currentInAmpsx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInAmpsx100.setStatus("current")


class _LimitSetInUse_Type(Integer32):
    """Custom type limitSetInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LimitSetInUse_Type.__name__ = "Integer32"
_LimitSetInUse_Object = MibTableColumn
limitSetInUse = _LimitSetInUse_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 10, 1, 3),
    _LimitSetInUse_Type()
)
limitSetInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitSetInUse.setStatus("current")
_ActiveAlarmsC_Type = AlarmEnabledType
_ActiveAlarmsC_Object = MibTableColumn
activeAlarmsC = _ActiveAlarmsC_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 10, 1, 4),
    _ActiveAlarmsC_Type()
)
activeAlarmsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmsC.setStatus("current")
_TempProbeStatusTable_Object = MibTable
tempProbeStatusTable = _TempProbeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 11)
)
if mibBuilder.loadTexts:
    tempProbeStatusTable.setStatus("current")
_TempProbeStatusTableEntry_Object = MibTableRow
tempProbeStatusTableEntry = _TempProbeStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 11, 1)
)
tempProbeStatusTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "tempProbeStatusTableIndex"),
)
if mibBuilder.loadTexts:
    tempProbeStatusTableEntry.setStatus("current")


class _TempProbeStatusTableIndex_Type(Integer32):
    """Custom type tempProbeStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TempProbeStatusTableIndex_Type.__name__ = "Integer32"
_TempProbeStatusTableIndex_Object = MibTableColumn
tempProbeStatusTableIndex = _TempProbeStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 11, 1, 1),
    _TempProbeStatusTableIndex_Type()
)
tempProbeStatusTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempProbeStatusTableIndex.setStatus("current")


class _TempInCx10_Type(Integer32):
    """Custom type tempInCx10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 2500),
    )


_TempInCx10_Type.__name__ = "Integer32"
_TempInCx10_Object = MibTableColumn
tempInCx10 = _TempInCx10_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 11, 1, 2),
    _TempInCx10_Type()
)
tempInCx10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempInCx10.setStatus("current")
_ActiveAlarmsT_Type = AlarmEnabledType
_ActiveAlarmsT_Object = MibTableColumn
activeAlarmsT = _ActiveAlarmsT_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 11, 1, 3),
    _ActiveAlarmsT_Type()
)
activeAlarmsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmsT.setStatus("current")
_DeIceControllerStatusTable_Object = MibTable
deIceControllerStatusTable = _DeIceControllerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12)
)
if mibBuilder.loadTexts:
    deIceControllerStatusTable.setStatus("current")
_DeIceControllerStatusEntry_Object = MibTableRow
deIceControllerStatusEntry = _DeIceControllerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1)
)
deIceControllerStatusEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "deIceControllerStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    deIceControllerStatusEntry.setStatus("current")


class _DeIceControllerStatusEntryIndex_Type(Integer32):
    """Custom type deIceControllerStatusEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DeIceControllerStatusEntryIndex_Type.__name__ = "Integer32"
_DeIceControllerStatusEntryIndex_Object = MibTableColumn
deIceControllerStatusEntryIndex = _DeIceControllerStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 1),
    _DeIceControllerStatusEntryIndex_Type()
)
deIceControllerStatusEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deIceControllerStatusEntryIndex.setStatus("current")
_ExtEnable_Type = YesNoType
_ExtEnable_Object = MibTableColumn
extEnable = _ExtEnable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 2),
    _ExtEnable_Type()
)
extEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extEnable.setStatus("current")
_RainDetStatus_Type = YesNoType
_RainDetStatus_Object = MibTableColumn
rainDetStatus = _RainDetStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 3),
    _RainDetStatus_Type()
)
rainDetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rainDetStatus.setStatus("current")
_IceDetStatus_Type = YesNoType
_IceDetStatus_Object = MibTableColumn
iceDetStatus = _IceDetStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 4),
    _IceDetStatus_Type()
)
iceDetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iceDetStatus.setStatus("current")
_IcingConditionsExist_Type = YesNoType
_IcingConditionsExist_Object = MibTableColumn
icingConditionsExist = _IcingConditionsExist_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 5),
    _IcingConditionsExist_Type()
)
icingConditionsExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icingConditionsExist.setStatus("current")
_BreakSupplyStatus_Type = YesNoType
_BreakSupplyStatus_Object = MibTableColumn
breakSupplyStatus = _BreakSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 6),
    _BreakSupplyStatus_Type()
)
breakSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakSupplyStatus.setStatus("current")


class _SummaryAlm_Type(Integer32):
    """Custom type summaryAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SummaryAlm_Type.__name__ = "Integer32"
_SummaryAlm_Object = MibTableColumn
summaryAlm = _SummaryAlm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 7),
    _SummaryAlm_Type()
)
summaryAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryAlm.setStatus("current")
_RestartRequired_Type = YesNoType
_RestartRequired_Object = MibTableColumn
restartRequired = _RestartRequired_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 8),
    _RestartRequired_Type()
)
restartRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartRequired.setStatus("current")
_OptoLogicalState1_Type = OnOffType
_OptoLogicalState1_Object = MibTableColumn
optoLogicalState1 = _OptoLogicalState1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 9),
    _OptoLogicalState1_Type()
)
optoLogicalState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optoLogicalState1.setStatus("current")
_OptoLogicalState2_Type = OnOffType
_OptoLogicalState2_Object = MibTableColumn
optoLogicalState2 = _OptoLogicalState2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 10),
    _OptoLogicalState2_Type()
)
optoLogicalState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optoLogicalState2.setStatus("current")
_OptoLogicalState3_Type = OnOffType
_OptoLogicalState3_Object = MibTableColumn
optoLogicalState3 = _OptoLogicalState3_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 11),
    _OptoLogicalState3_Type()
)
optoLogicalState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optoLogicalState3.setStatus("current")
_OptoLogicalState4_Type = OnOffType
_OptoLogicalState4_Object = MibTableColumn
optoLogicalState4 = _OptoLogicalState4_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 12),
    _OptoLogicalState4_Type()
)
optoLogicalState4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optoLogicalState4.setStatus("current")
_OptoLogicalState5_Type = OnOffType
_OptoLogicalState5_Object = MibTableColumn
optoLogicalState5 = _OptoLogicalState5_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 13),
    _OptoLogicalState5_Type()
)
optoLogicalState5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optoLogicalState5.setStatus("current")
_OptoLogicalState6_Type = OnOffType
_OptoLogicalState6_Object = MibTableColumn
optoLogicalState6 = _OptoLogicalState6_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 14),
    _OptoLogicalState6_Type()
)
optoLogicalState6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optoLogicalState6.setStatus("current")
_OptoLogicalState7_Type = OnOffType
_OptoLogicalState7_Object = MibTableColumn
optoLogicalState7 = _OptoLogicalState7_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 15),
    _OptoLogicalState7_Type()
)
optoLogicalState7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optoLogicalState7.setStatus("current")
_OptoLogicalState8_Type = OnOffType
_OptoLogicalState8_Object = MibTableColumn
optoLogicalState8 = _OptoLogicalState8_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 12, 1, 16),
    _OptoLogicalState8_Type()
)
optoLogicalState8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optoLogicalState8.setStatus("current")
_MainDeIceStatusTable_Object = MibTable
mainDeIceStatusTable = _MainDeIceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13)
)
if mibBuilder.loadTexts:
    mainDeIceStatusTable.setStatus("current")
_MainDeIceStatusEntry_Object = MibTableRow
mainDeIceStatusEntry = _MainDeIceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1)
)
mainDeIceStatusEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "deIceControllerStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    mainDeIceStatusEntry.setStatus("current")


class _MainDeIceStatusEntryIndex_Type(Integer32):
    """Custom type mainDeIceStatusEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MainDeIceStatusEntryIndex_Type.__name__ = "Integer32"
_MainDeIceStatusEntryIndex_Object = MibTableColumn
mainDeIceStatusEntryIndex = _MainDeIceStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 1),
    _MainDeIceStatusEntryIndex_Type()
)
mainDeIceStatusEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainDeIceStatusEntryIndex.setStatus("current")


class _AutoStatus_Type(Integer32):
    """Custom type autoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AutoStatus_Type.__name__ = "Integer32"
_AutoStatus_Object = MibTableColumn
autoStatus = _AutoStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 2),
    _AutoStatus_Type()
)
autoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoStatus.setStatus("current")


class _ForceOnStatus_Type(Integer32):
    """Custom type forceOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ForceOnStatus_Type.__name__ = "Integer32"
_ForceOnStatus_Object = MibTableColumn
forceOnStatus = _ForceOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 3),
    _ForceOnStatus_Type()
)
forceOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forceOnStatus.setStatus("current")


class _Stage2EnabledStatus_Type(Integer32):
    """Custom type stage2EnabledStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Stage2EnabledStatus_Type.__name__ = "Integer32"
_Stage2EnabledStatus_Object = MibTableColumn
stage2EnabledStatus = _Stage2EnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 4),
    _Stage2EnabledStatus_Type()
)
stage2EnabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stage2EnabledStatus.setStatus("current")


class _Stage3EnabledStatus_Type(Integer32):
    """Custom type stage3EnabledStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Stage3EnabledStatus_Type.__name__ = "Integer32"
_Stage3EnabledStatus_Object = MibTableColumn
stage3EnabledStatus = _Stage3EnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 5),
    _Stage3EnabledStatus_Type()
)
stage3EnabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stage3EnabledStatus.setStatus("current")
_Stage1Active_Type = YesNoType
_Stage1Active_Object = MibTableColumn
stage1Active = _Stage1Active_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 10),
    _Stage1Active_Type()
)
stage1Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stage1Active.setStatus("current")
_Stage2Active_Type = YesNoType
_Stage2Active_Object = MibTableColumn
stage2Active = _Stage2Active_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 11),
    _Stage2Active_Type()
)
stage2Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stage2Active.setStatus("current")
_Stage3Active_Type = YesNoType
_Stage3Active_Object = MibTableColumn
stage3Active = _Stage3Active_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 12),
    _Stage3Active_Type()
)
stage3Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stage3Active.setStatus("current")
_MainDeIceModeStatus_Type = MainDeiceModeType
_MainDeIceModeStatus_Object = MibTableColumn
mainDeIceModeStatus = _MainDeIceModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 13),
    _MainDeIceModeStatus_Type()
)
mainDeIceModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainDeIceModeStatus.setStatus("current")
_Stage1RelayState_Type = YesNoType
_Stage1RelayState_Object = MibTableColumn
stage1RelayState = _Stage1RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 14),
    _Stage1RelayState_Type()
)
stage1RelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stage1RelayState.setStatus("current")
_Stage2RelayState_Type = YesNoType
_Stage2RelayState_Object = MibTableColumn
stage2RelayState = _Stage2RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 15),
    _Stage2RelayState_Type()
)
stage2RelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stage2RelayState.setStatus("current")
_Stage3RelayState_Type = YesNoType
_Stage3RelayState_Object = MibTableColumn
stage3RelayState = _Stage3RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 13, 1, 16),
    _Stage3RelayState_Type()
)
stage3RelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stage3RelayState.setStatus("current")
_EmailSetupTable_Object = MibTable
emailSetupTable = _EmailSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14)
)
if mibBuilder.loadTexts:
    emailSetupTable.setStatus("current")
_EmailSetupTableEntry_Object = MibTableRow
emailSetupTableEntry = _EmailSetupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1)
)
emailSetupTableEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "emailSetupTableIndex"),
)
if mibBuilder.loadTexts:
    emailSetupTableEntry.setStatus("current")


class _EmailSetupTableIndex_Type(Integer32):
    """Custom type emailSetupTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_EmailSetupTableIndex_Type.__name__ = "Integer32"
_EmailSetupTableIndex_Object = MibTableColumn
emailSetupTableIndex = _EmailSetupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 1),
    _EmailSetupTableIndex_Type()
)
emailSetupTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emailSetupTableIndex.setStatus("current")
_EnableEmailSupport_Type = YesNoType
_EnableEmailSupport_Object = MibTableColumn
enableEmailSupport = _EnableEmailSupport_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 2),
    _EnableEmailSupport_Type()
)
enableEmailSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableEmailSupport.setStatus("current")


class _EmailSmtpHost_Type(OctetString):
    """Custom type emailSmtpHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EmailSmtpHost_Type.__name__ = "OctetString"
_EmailSmtpHost_Object = MibTableColumn
emailSmtpHost = _EmailSmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 3),
    _EmailSmtpHost_Type()
)
emailSmtpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpHost.setStatus("current")
_EmailSmtpPort_Type = Integer32
_EmailSmtpPort_Object = MibTableColumn
emailSmtpPort = _EmailSmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 4),
    _EmailSmtpPort_Type()
)
emailSmtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpPort.setStatus("current")


class _EmailSmtpDomain_Type(OctetString):
    """Custom type emailSmtpDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EmailSmtpDomain_Type.__name__ = "OctetString"
_EmailSmtpDomain_Object = MibTableColumn
emailSmtpDomain = _EmailSmtpDomain_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 5),
    _EmailSmtpDomain_Type()
)
emailSmtpDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpDomain.setStatus("current")


class _EmailSmtpAuthUser_Type(OctetString):
    """Custom type emailSmtpAuthUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EmailSmtpAuthUser_Type.__name__ = "OctetString"
_EmailSmtpAuthUser_Object = MibTableColumn
emailSmtpAuthUser = _EmailSmtpAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 6),
    _EmailSmtpAuthUser_Type()
)
emailSmtpAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpAuthUser.setStatus("current")


class _EmailSmtpAuthPassword_Type(OctetString):
    """Custom type emailSmtpAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EmailSmtpAuthPassword_Type.__name__ = "OctetString"
_EmailSmtpAuthPassword_Object = MibTableColumn
emailSmtpAuthPassword = _EmailSmtpAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 7),
    _EmailSmtpAuthPassword_Type()
)
emailSmtpAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpAuthPassword.setStatus("current")


class _EmailSmtpTo_Type(OctetString):
    """Custom type emailSmtpTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EmailSmtpTo_Type.__name__ = "OctetString"
_EmailSmtpTo_Object = MibTableColumn
emailSmtpTo = _EmailSmtpTo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 8),
    _EmailSmtpTo_Type()
)
emailSmtpTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpTo.setStatus("current")


class _EmailSmtpCc_Type(OctetString):
    """Custom type emailSmtpCc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EmailSmtpCc_Type.__name__ = "OctetString"
_EmailSmtpCc_Object = MibTableColumn
emailSmtpCc = _EmailSmtpCc_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 9),
    _EmailSmtpCc_Type()
)
emailSmtpCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpCc.setStatus("current")


class _EmailSmtpBcc_Type(OctetString):
    """Custom type emailSmtpBcc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EmailSmtpBcc_Type.__name__ = "OctetString"
_EmailSmtpBcc_Object = MibTableColumn
emailSmtpBcc = _EmailSmtpBcc_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 10),
    _EmailSmtpBcc_Type()
)
emailSmtpBcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpBcc.setStatus("current")


class _EmailSmtpSubjectPrefig_Type(OctetString):
    """Custom type emailSmtpSubjectPrefig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EmailSmtpSubjectPrefig_Type.__name__ = "OctetString"
_EmailSmtpSubjectPrefig_Object = MibTableColumn
emailSmtpSubjectPrefig = _EmailSmtpSubjectPrefig_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 11),
    _EmailSmtpSubjectPrefig_Type()
)
emailSmtpSubjectPrefig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpSubjectPrefig.setStatus("current")


class _EmailSmtpReasons_Type(Integer32):
    """Custom type emailSmtpReasons based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EmailSmtpReasons_Type.__name__ = "Integer32"
_EmailSmtpReasons_Object = MibTableColumn
emailSmtpReasons = _EmailSmtpReasons_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 14, 1, 12),
    _EmailSmtpReasons_Type()
)
emailSmtpReasons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpReasons.setStatus("current")
_AuxCircuitConfigTable_Object = MibTable
auxCircuitConfigTable = _AuxCircuitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15)
)
if mibBuilder.loadTexts:
    auxCircuitConfigTable.setStatus("current")
_AuxCircuitConfigEntry_Object = MibTableRow
auxCircuitConfigEntry = _AuxCircuitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1)
)
auxCircuitConfigEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "auxCircuitConfigIndex"),
)
if mibBuilder.loadTexts:
    auxCircuitConfigEntry.setStatus("current")


class _AuxCircuitConfigIndex_Type(Integer32):
    """Custom type auxCircuitConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AuxCircuitConfigIndex_Type.__name__ = "Integer32"
_AuxCircuitConfigIndex_Object = MibTableColumn
auxCircuitConfigIndex = _AuxCircuitConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 1),
    _AuxCircuitConfigIndex_Type()
)
auxCircuitConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    auxCircuitConfigIndex.setStatus("current")


class _AuxCircuitName_Type(OctetString):
    """Custom type auxCircuitName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AuxCircuitName_Type.__name__ = "OctetString"
_AuxCircuitName_Object = MibTableColumn
auxCircuitName = _AuxCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 2),
    _AuxCircuitName_Type()
)
auxCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitName.setStatus("current")
_AuxCircuitFunction_Type = AuxCircuitFunctions
_AuxCircuitFunction_Object = MibTableColumn
auxCircuitFunction = _AuxCircuitFunction_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 3),
    _AuxCircuitFunction_Type()
)
auxCircuitFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitFunction.setStatus("current")
_AuxCircuitFuncMode_Type = OperationalModes
_AuxCircuitFuncMode_Object = MibTableColumn
auxCircuitFuncMode = _AuxCircuitFuncMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 4),
    _AuxCircuitFuncMode_Type()
)
auxCircuitFuncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitFuncMode.setStatus("current")
_AuxCircuitAuxMode_Type = AuxModes
_AuxCircuitAuxMode_Object = MibTableColumn
auxCircuitAuxMode = _AuxCircuitAuxMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 5),
    _AuxCircuitAuxMode_Type()
)
auxCircuitAuxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitAuxMode.setStatus("current")
_AuxCircuitObeysExtEnable_Type = YesNoType
_AuxCircuitObeysExtEnable_Object = MibTableColumn
auxCircuitObeysExtEnable = _AuxCircuitObeysExtEnable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 6),
    _AuxCircuitObeysExtEnable_Type()
)
auxCircuitObeysExtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitObeysExtEnable.setStatus("current")
_AuxCircuitUsesBreakPower_Type = YesNoType
_AuxCircuitUsesBreakPower_Object = MibTableColumn
auxCircuitUsesBreakPower = _AuxCircuitUsesBreakPower_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 7),
    _AuxCircuitUsesBreakPower_Type()
)
auxCircuitUsesBreakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitUsesBreakPower.setStatus("current")
_AuxCircuitCurrentSensor_Type = CurrentSensorFunctions
_AuxCircuitCurrentSensor_Object = MibTableColumn
auxCircuitCurrentSensor = _AuxCircuitCurrentSensor_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 8),
    _AuxCircuitCurrentSensor_Type()
)
auxCircuitCurrentSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitCurrentSensor.setStatus("current")
_AuxCircuitRelayGroup_Type = Integer32
_AuxCircuitRelayGroup_Object = MibTableColumn
auxCircuitRelayGroup = _AuxCircuitRelayGroup_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 9),
    _AuxCircuitRelayGroup_Type()
)
auxCircuitRelayGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitRelayGroup.setStatus("current")
_AuxCircuitTempSensor_Type = TemperatureSensorFunctions
_AuxCircuitTempSensor_Object = MibTableColumn
auxCircuitTempSensor = _AuxCircuitTempSensor_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 10),
    _AuxCircuitTempSensor_Type()
)
auxCircuitTempSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitTempSensor.setStatus("current")
_AuxCircuitOnTemp_Type = Integer32
_AuxCircuitOnTemp_Object = MibTableColumn
auxCircuitOnTemp = _AuxCircuitOnTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 11),
    _AuxCircuitOnTemp_Type()
)
auxCircuitOnTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitOnTemp.setStatus("current")
_AuxCircuitOffTemp_Type = Integer32
_AuxCircuitOffTemp_Object = MibTableColumn
auxCircuitOffTemp = _AuxCircuitOffTemp_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 12),
    _AuxCircuitOffTemp_Type()
)
auxCircuitOffTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitOffTemp.setStatus("current")
_AuxCircuitActivationDelay_Type = Integer32
_AuxCircuitActivationDelay_Object = MibTableColumn
auxCircuitActivationDelay = _AuxCircuitActivationDelay_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 13),
    _AuxCircuitActivationDelay_Type()
)
auxCircuitActivationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitActivationDelay.setStatus("current")
_AuxCircuitRunOnTime_Type = Integer32
_AuxCircuitRunOnTime_Object = MibTableColumn
auxCircuitRunOnTime = _AuxCircuitRunOnTime_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 15, 1, 14),
    _AuxCircuitRunOnTime_Type()
)
auxCircuitRunOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCircuitRunOnTime.setStatus("current")
_AuxCircuitStatusTable_Object = MibTable
auxCircuitStatusTable = _AuxCircuitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 16)
)
if mibBuilder.loadTexts:
    auxCircuitStatusTable.setStatus("current")
_AuxCircuitStatusEntry_Object = MibTableRow
auxCircuitStatusEntry = _AuxCircuitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 16, 1)
)
auxCircuitStatusEntry.setIndexNames(
    (0, "S3DEICEUNIT-MIB", "auxCircuitStatusIndex"),
)
if mibBuilder.loadTexts:
    auxCircuitStatusEntry.setStatus("current")


class _AuxCircuitStatusIndex_Type(Integer32):
    """Custom type auxCircuitStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AuxCircuitStatusIndex_Type.__name__ = "Integer32"
_AuxCircuitStatusIndex_Object = MibTableColumn
auxCircuitStatusIndex = _AuxCircuitStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 16, 1, 1),
    _AuxCircuitStatusIndex_Type()
)
auxCircuitStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    auxCircuitStatusIndex.setStatus("current")
_AuxCircuitStatus_Type = OnOffType
_AuxCircuitStatus_Object = MibTableColumn
auxCircuitStatus = _AuxCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 16, 1, 2),
    _AuxCircuitStatus_Type()
)
auxCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCircuitStatus.setStatus("current")
_AuxModeChangePending_Type = AuxModePendingType
_AuxModeChangePending_Object = MibTableColumn
auxModeChangePending = _AuxModeChangePending_Object(
    (1, 3, 6, 1, 4, 1, 31637, 2, 16, 1, 3),
    _AuxModeChangePending_Type()
)
auxModeChangePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxModeChangePending.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S3DEICEUNIT-MIB",
    **{"DeIceCardType": DeIceCardType,
       "RelayCardId": RelayCardId,
       "TempSensorTypes": TempSensorTypes,
       "RelayGroupFunctionality": RelayGroupFunctionality,
       "InputFunction": InputFunction,
       "OperationalModes": OperationalModes,
       "AuxModes": AuxModes,
       "CurrentSensorFunctions": CurrentSensorFunctions,
       "TemperatureSensorFunctions": TemperatureSensorFunctions,
       "AuxCircuitFunctions": AuxCircuitFunctions,
       "AlarmEnabledType": AlarmEnabledType,
       "MainDeiceModeType": MainDeiceModeType,
       "ExternalEnableMode": ExternalEnableMode,
       "AuxModePendingType": AuxModePendingType,
       "s3Deice": s3Deice,
       "generalInfoTable": generalInfoTable,
       "generalInfoTableEntry": generalInfoTableEntry,
       "generalInfoTableEntryIndex": generalInfoTableEntryIndex,
       "numRelayGroups": numRelayGroups,
       "numCurrentCards": numCurrentCards,
       "numTemperatureCards": numTemperatureCards,
       "optionCardTable": optionCardTable,
       "optionCardTableEntry": optionCardTableEntry,
       "optionCardTableEntryIndex": optionCardTableEntryIndex,
       "optionCardType": optionCardType,
       "optionCardAddress": optionCardAddress,
       "optionCardName": optionCardName,
       "optionCardFirmwareRevision": optionCardFirmwareRevision,
       "optionCardSerialNumber": optionCardSerialNumber,
       "optionCardOptionVal": optionCardOptionVal,
       "optionCardCommsFail": optionCardCommsFail,
       "relayGroupTable": relayGroupTable,
       "relayGroupTableEntry": relayGroupTableEntry,
       "relayGroupTableEntryIndex": relayGroupTableEntryIndex,
       "relayGroupName": relayGroupName,
       "relayGroupFunction": relayGroupFunction,
       "relayGroupBoardID0": relayGroupBoardID0,
       "relayGroupIndexNum0": relayGroupIndexNum0,
       "relayGroupInverted0": relayGroupInverted0,
       "relayGroupBoardID1": relayGroupBoardID1,
       "relayGroupIndexNum1": relayGroupIndexNum1,
       "relayGroupInverted1": relayGroupInverted1,
       "relayGroupBoardID2": relayGroupBoardID2,
       "relayGroupIndexNum2": relayGroupIndexNum2,
       "relayGroupInverted2": relayGroupInverted2,
       "currentSensorTable": currentSensorTable,
       "currentSensorTableEntry": currentSensorTableEntry,
       "currentSensorTableIndex": currentSensorTableIndex,
       "currentSensorName": currentSensorName,
       "currentSensorFunction": currentSensorFunction,
       "upperLimit0": upperLimit0,
       "lowerLimit0": lowerLimit0,
       "upperLimit1": upperLimit1,
       "lowerLimit1": lowerLimit1,
       "upperLimit2": upperLimit2,
       "lowerLimit2": lowerLimit2,
       "alarmLimitsEnabled": alarmLimitsEnabled,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorTableEntry": temperatureSensorTableEntry,
       "temperatureSensorTableIndex": temperatureSensorTableIndex,
       "tempSensorType": tempSensorType,
       "tempSensorName": tempSensorName,
       "tempSensorFunction": tempSensorFunction,
       "tempSensorOffset2Wire": tempSensorOffset2Wire,
       "tempUpperLimitInCx10": tempUpperLimitInCx10,
       "tempLowerLimitInCx10": tempLowerLimitInCx10,
       "alarmLimitsEn": alarmLimitsEn,
       "optoInputsTable": optoInputsTable,
       "optoInputsEntry": optoInputsEntry,
       "optoInputsEntryIndex": optoInputsEntryIndex,
       "optoInputName": optoInputName,
       "optoInputFunction": optoInputFunction,
       "optoInputInverted": optoInputInverted,
       "deIceControllerConfigTable": deIceControllerConfigTable,
       "deIceControllerConfigEntry": deIceControllerConfigEntry,
       "deIceControllerConfigEntryIndex": deIceControllerConfigEntryIndex,
       "systemName": systemName,
       "rainDetectorFitted": rainDetectorFitted,
       "useRainSensorAndTambAsIceDetector": useRainSensorAndTambAsIceDetector,
       "iceFormationUpperTemp": iceFormationUpperTemp,
       "iceFormationLowerTemp": iceFormationLowerTemp,
       "iceDetectorFitted": iceDetectorFitted,
       "alarmActivationDelay": alarmActivationDelay,
       "restartController": restartController,
       "breakSupplyName": breakSupplyName,
       "extEnableName": extEnableName,
       "currentAlarmDelaySec": currentAlarmDelaySec,
       "extEnableFitted": extEnableFitted,
       "mainDeIceConfigTable": mainDeIceConfigTable,
       "mainDeIceConfigEntry": mainDeIceConfigEntry,
       "mainDeIceConfigEntryIndex": mainDeIceConfigEntryIndex,
       "numDeIceStages": numDeIceStages,
       "stage1UsesBreakPower": stage1UsesBreakPower,
       "stage2UsesBreakPower": stage2UsesBreakPower,
       "stage3UsesBreakPower": stage3UsesBreakPower,
       "stage123ObeysExtEnable": stage123ObeysExtEnable,
       "activationDelayStage1": activationDelayStage1,
       "activationDelayStage2": activationDelayStage2,
       "activationDelayStage3": activationDelayStage3,
       "runOnTimeStage1": runOnTimeStage1,
       "runOnTimeStage2": runOnTimeStage2,
       "runOnTimeStage3": runOnTimeStage3,
       "autoMode": autoMode,
       "forceOn": forceOn,
       "stage2Enabled": stage2Enabled,
       "stage3Enabled": stage3Enabled,
       "mainDeIceMode": mainDeIceMode,
       "extEnableMode": extEnableMode,
       "stage1TempSensorFn": stage1TempSensorFn,
       "stage2TempSensorFn": stage2TempSensorFn,
       "stage3TempSensorFn": stage3TempSensorFn,
       "stage1OnTemp": stage1OnTemp,
       "stage1OffTemp": stage1OffTemp,
       "stage2OnTemp": stage2OnTemp,
       "stage2OffTemp": stage2OffTemp,
       "stage3OnTemp": stage3OnTemp,
       "stage3OffTemp": stage3OffTemp,
       "relayStatusTable": relayStatusTable,
       "relayStatusTableEntry": relayStatusTableEntry,
       "relayStatusTableIndex": relayStatusTableIndex,
       "relayState": relayState,
       "relayOnTime": relayOnTime,
       "relayOffTime": relayOffTime,
       "currentStatusTable": currentStatusTable,
       "currentStatusTableEntry": currentStatusTableEntry,
       "currentStatusTableIndex": currentStatusTableIndex,
       "currentInAmpsx100": currentInAmpsx100,
       "limitSetInUse": limitSetInUse,
       "activeAlarmsC": activeAlarmsC,
       "tempProbeStatusTable": tempProbeStatusTable,
       "tempProbeStatusTableEntry": tempProbeStatusTableEntry,
       "tempProbeStatusTableIndex": tempProbeStatusTableIndex,
       "tempInCx10": tempInCx10,
       "activeAlarmsT": activeAlarmsT,
       "deIceControllerStatusTable": deIceControllerStatusTable,
       "deIceControllerStatusEntry": deIceControllerStatusEntry,
       "deIceControllerStatusEntryIndex": deIceControllerStatusEntryIndex,
       "extEnable": extEnable,
       "rainDetStatus": rainDetStatus,
       "iceDetStatus": iceDetStatus,
       "icingConditionsExist": icingConditionsExist,
       "breakSupplyStatus": breakSupplyStatus,
       "summaryAlm": summaryAlm,
       "restartRequired": restartRequired,
       "optoLogicalState1": optoLogicalState1,
       "optoLogicalState2": optoLogicalState2,
       "optoLogicalState3": optoLogicalState3,
       "optoLogicalState4": optoLogicalState4,
       "optoLogicalState5": optoLogicalState5,
       "optoLogicalState6": optoLogicalState6,
       "optoLogicalState7": optoLogicalState7,
       "optoLogicalState8": optoLogicalState8,
       "mainDeIceStatusTable": mainDeIceStatusTable,
       "mainDeIceStatusEntry": mainDeIceStatusEntry,
       "mainDeIceStatusEntryIndex": mainDeIceStatusEntryIndex,
       "autoStatus": autoStatus,
       "forceOnStatus": forceOnStatus,
       "stage2EnabledStatus": stage2EnabledStatus,
       "stage3EnabledStatus": stage3EnabledStatus,
       "stage1Active": stage1Active,
       "stage2Active": stage2Active,
       "stage3Active": stage3Active,
       "mainDeIceModeStatus": mainDeIceModeStatus,
       "stage1RelayState": stage1RelayState,
       "stage2RelayState": stage2RelayState,
       "stage3RelayState": stage3RelayState,
       "emailSetupTable": emailSetupTable,
       "emailSetupTableEntry": emailSetupTableEntry,
       "emailSetupTableIndex": emailSetupTableIndex,
       "enableEmailSupport": enableEmailSupport,
       "emailSmtpHost": emailSmtpHost,
       "emailSmtpPort": emailSmtpPort,
       "emailSmtpDomain": emailSmtpDomain,
       "emailSmtpAuthUser": emailSmtpAuthUser,
       "emailSmtpAuthPassword": emailSmtpAuthPassword,
       "emailSmtpTo": emailSmtpTo,
       "emailSmtpCc": emailSmtpCc,
       "emailSmtpBcc": emailSmtpBcc,
       "emailSmtpSubjectPrefig": emailSmtpSubjectPrefig,
       "emailSmtpReasons": emailSmtpReasons,
       "auxCircuitConfigTable": auxCircuitConfigTable,
       "auxCircuitConfigEntry": auxCircuitConfigEntry,
       "auxCircuitConfigIndex": auxCircuitConfigIndex,
       "auxCircuitName": auxCircuitName,
       "auxCircuitFunction": auxCircuitFunction,
       "auxCircuitFuncMode": auxCircuitFuncMode,
       "auxCircuitAuxMode": auxCircuitAuxMode,
       "auxCircuitObeysExtEnable": auxCircuitObeysExtEnable,
       "auxCircuitUsesBreakPower": auxCircuitUsesBreakPower,
       "auxCircuitCurrentSensor": auxCircuitCurrentSensor,
       "auxCircuitRelayGroup": auxCircuitRelayGroup,
       "auxCircuitTempSensor": auxCircuitTempSensor,
       "auxCircuitOnTemp": auxCircuitOnTemp,
       "auxCircuitOffTemp": auxCircuitOffTemp,
       "auxCircuitActivationDelay": auxCircuitActivationDelay,
       "auxCircuitRunOnTime": auxCircuitRunOnTime,
       "auxCircuitStatusTable": auxCircuitStatusTable,
       "auxCircuitStatusEntry": auxCircuitStatusEntry,
       "auxCircuitStatusIndex": auxCircuitStatusIndex,
       "auxCircuitStatus": auxCircuitStatus,
       "auxModeChangePending": auxModeChangePending}
)
