# SNMP MIB module (FSP3000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/FSP3000-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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

(fsp3000,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp3000")

(PhysicalClass,
 PhysicalIndex,
 entPhysicalClass,
 entPhysicalContainedIn,
 entPhysicalDescr,
 entPhysicalIndex,
 entPhysicalName,
 entPhysicalParentRelPos,
 entPhysicalVendorType) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalClass",
    "PhysicalIndex",
    "entPhysicalClass",
    "entPhysicalContainedIn",
    "entPhysicalDescr",
    "entPhysicalIndex",
    "entPhysicalName",
    "entPhysicalParentRelPos",
    "entPhysicalVendorType")

(InterfaceIndex,
 ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifEntry",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsp3000MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fsp3000MIB.setRevisions(
        ("2004-10-27 00:00",
         "2004-04-01 00:00",
         "2004-01-22 00:00",
         "2003-05-13 10:00",
         "2002-12-09 09:00",
         "2002-08-26 08:00",
         "2002-04-18 07:00",
         "2002-01-09 06:00",
         "2001-11-20 05:20",
         "2001-11-15 05:10",
         "2001-09-19 04:20",
         "2001-08-28 03:40",
         "2001-04-24 03:00",
         "2000-10-30 02:00",
         "2000-10-24 01:10",
         "2000-10-16 01:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceAlarmTypes(TextualConvention, Integer32):
    status = "current"
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("lossOfSignal", 1),
          ("lossOfLinkPulse", 2),
          ("lossOfClock", 3),
          ("txClockFail", 4),
          ("lossOfFrame", 5),
          ("rxESFail", 6),
          ("txESFail", 7),
          ("rxSignalOverload", 8),
          ("laserDegrade", 9),
          ("laserBiasEoL", 10),
          ("laserTecEoL", 11),
          ("subModTempOoR", 12),
          ("laserTempOoR", 13),
          ("lossOfOop", 14),
          ("lossOfOip", 15),
          ("hwOipTooHigh", 16),
          ("hwOopTooLow", 17),
          ("lineAIS", 18),
          ("lineRDI", 19),
          ("sectionTraceMismatch", 20),
          ("sectionTraceInconsistency", 21),
          ("lossOfPointer", 22),
          ("pathAIS", 23),
          ("pathRDI", 24),
          ("pathSignalDegrade", 25),
          ("servPathLossOfFrame", 26),
          ("servPathAIS", 27),
          ("servPathRDI", 28),
          ("servPathPLM", 29),
          ("servPathUNEQ", 30),
          ("pathPLM", 31),
          ("pathUNEQ", 32),
          ("otuFecLossOfFrame", 33),
          ("switchError", 34),
          ("sectionSignalDegrade", 35),
          ("lowestCurrent", 100),
          ("lowCurrent", 101),
          ("highCurrent", 102),
          ("highestCurrent", 103),
          ("lowestOIP", 104),
          ("lowOIP", 105),
          ("highOIP", 106),
          ("highestOIP", 107),
          ("lowestOOP", 108),
          ("lowOOP", 109),
          ("highOOP", 110),
          ("highestOOP", 111))
    )



class EquipmentAlarmTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              24,
              25,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("fuseFail1", 1),
          ("fuseFail2", 2),
          ("fanFail1", 4),
          ("fanFail2", 5),
          ("fanFail3", 6),
          ("fanPowerFail1", 7),
          ("fanPowerFail2", 8),
          ("powerFail", 9),
          ("extInput1", 10),
          ("extInput2", 11),
          ("extInput3", 12),
          ("extInput4", 13),
          ("extInput5", 14),
          ("extInput6", 15),
          ("extInput7", 16),
          ("extInput8", 17),
          ("extInput9", 18),
          ("extInput10", 19),
          ("extInput11", 20),
          ("extInput12", 21),
          ("lineANotAvail", 24),
          ("lineBNotAvail", 25),
          ("posError", 27),
          ("multipleFanFail", 28),
          ("oscmBranchError", 29),
          ("externalFanFail", 30),
          ("plannedCardMissing", 31),
          ("plannedCardMismatch", 32),
          ("provisionError", 33),
          ("noFeedback", 34),
          ("lowestTemp", 100),
          ("lowTemp", 101),
          ("highTemp", 102),
          ("highestTemp", 103),
          ("lowestVolt", 104),
          ("lowVolt", 105),
          ("highVolt", 106),
          ("highestVolt", 107),
          ("lowestCurrent", 108),
          ("lowCurrent", 109),
          ("highCurrent", 110),
          ("highestCurrent", 111))
    )



class InterfaceQoSReportTypes(TextualConvention, Integer32):
    status = "current"
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("sect15mESHigh", 1),
          ("sect15mSESHigh", 2),
          ("sect15mSEFSHigh", 3),
          ("sect15mCVHigh", 4),
          ("sect24hrESHigh", 5),
          ("sect24hrSESHigh", 6),
          ("sect24hSEFSHigh", 7),
          ("sect24hCVHigh", 8),
          ("path15mESHigh", 9),
          ("path15mSESHigh", 10),
          ("path15mCVHigh", 11),
          ("path15mUASHigh", 12),
          ("path24hESHigh", 13),
          ("path24hSESHigh", 14),
          ("path24hCVHigh", 15),
          ("path24hUASHigh", 16))
    )



class ProtectionGroupAlarmTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protectionFail", 1),
          ("configurationMismatch", 2))
    )



class TrapAlarmSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("indeterminate", 1),
          ("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("warning", 5),
          ("cleared", 6),
          ("inhibited", 7))
    )



class ProtectionCommand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("manualToEast", 4),
          ("manualToWest", 5),
          ("none", 6))
    )



class ProtectionSwitchMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("nonrevertive", 1)
    )



class ProtectionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trafficOnWest", 1),
          ("trafficOnEast", 2))
    )



class AlarmSwitching(TextualConvention, Integer32):
    status = "current"
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
        *(("swNotApplicable", 0),
          ("swEnable", 1),
          ("swDisable", 2),
          ("swEnabledEastOnly", 3),
          ("swEnabledWestOnly", 4),
          ("swNotSupported", 5))
    )



class OnOff(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class TxState(TextualConvention, Integer32):
    status = "current"
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
        *(("laserOrSwitchOn", 1),
          ("laserOrSwitchOff", 2),
          ("forcedOn", 3),
          ("forcedOff", 4),
          ("fail", 5),
          ("noInfo", 6),
          ("auto", 7))
    )



class SwitchCommand(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("lockToLineA", 2),
          ("lockToLineB", 3),
          ("unlockSwitch", 4))
    )



class AvailState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )



class ContainerState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("containerEmpty", 1),
          ("containerFilled", 2))
    )



class PlannedState(TextualConvention, Integer32):
    status = "current"
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
        *(("plannedNotAppl", 1),
          ("plannedNone", 2),
          ("plannedAccepted", 3),
          ("plannedEmptyAccepted", 4),
          ("plannedNotAccepted", 5),
          ("plannedEmptyNotAccepted", 6),
          ("plannedMissing", 7))
    )



class ContainsPhysicalIndex(PhysicalIndex):
    status = "current"


class ClockDataRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
        *(("none", 1),
          ("mb125", 2),
          ("mb155", 3),
          ("mb200", 4),
          ("mb622", 6),
          ("mb1062", 7),
          ("mb2488", 8),
          ("mb1250", 9),
          ("mb9953", 10),
          ("mb10312", 11),
          ("mb2125", 12))
    )



class ClockType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              15,
              16,
              18,
              19,
              20,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("fcF2488", 15),
          ("mcF1062F1250", 16),
          ("mcF125F155F200", 18),
          ("mcF155F622F1062", 19),
          ("mcF155F622F1250", 20),
          ("mcF622F1062F1250", 22),
          ("mcF9953F10312", 23),
          ("highSpeedMultirate", 24),
          ("lowSpeedMultirate", 25))
    )



class LaserType(TextualConvention, Integer32):
    status = "current"
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
        *(("versionNotApplicable", 0),
          ("standardVersion", 1),
          ("extendedVersion", 2),
          ("highPowerVersion", 3),
          ("unspecifiedVersion", 4),
          ("regionalVersion", 5))
    )



class LoginIdentity(TextualConvention, Integer32):
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
        *(("other", 0),
          ("root", 1),
          ("netadmin", 2))
    )



class TrapCounter(TextualConvention, Counter32):
    status = "current"


class EnableState(TextualConvention, Integer32):
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
        *(("stateNotApplicable", 0),
          ("stateEnabled", 1),
          ("stateDisabled", 2))
    )



class OtuFecState(TextualConvention, Integer32):
    status = "current"
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
        *(("notApplicable", 0),
          ("otuFecEnabled", 1),
          ("otuFecDisabled", 2),
          ("otuFecEnabledNoOverheadMon", 3),
          ("otuFecRsFec", 4),
          ("otuFecEnhFec", 5))
    )



class OtuFecSupported(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("otuNoFec", 0),
          ("otuNonStandardFEC", 1),
          ("otuG709Fec", 2),
          ("otuEnhFec", 4),
          ("otuG709EnhFec", 7))
    )



class ArcState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alm", 1),
          ("nalm", 2))
    )



class TimingSource(TextualConvention, Integer32):
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
        *(("timingNotApplicable", 0),
          ("internal", 1),
          ("loopTiming", 2))
    )



class ChannelRange(TextualConvention, Integer32):
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
        *(("chNotAvail", 0),
          ("ch1Ch4", 1),
          ("ch5Ch8", 2),
          ("ch9Ch12", 3),
          ("ch13Ch16", 4),
          ("ch17Ch20", 5),
          ("ch21Ch24", 6),
          ("ch25Ch28", 7),
          ("ch29Ch32", 8))
    )



class OscmTopologyMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oscmBackbone", 1),
          ("oscmBranch", 2),
          ("oscmUnknown", 3))
    )



class OscmBranchMode(TextualConvention, Integer32):
    status = "current"
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
        *(("oscmBranchUnprotected", 1),
          ("oscmBranchProtected", 2),
          ("oscmBranchNotAppl", 3),
          ("oscmBranchDualHomed", 4))
    )



class SwUpgradeStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("downloading", 2),
          ("downloadLoginFailed", 3),
          ("downloadFileNotFound", 4),
          ("downloadFailure", 6),
          ("downloadedReadyForActivation", 7),
          ("activatingSoftware", 8),
          ("integrityCheckFailed", 9),
          ("softwareActivated", 10),
          ("rebooting", 11))
    )



class IdentityTranslation(DisplayString):
    status = "current"


class AlsMode(TextualConvention, Integer32):
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
        *(("alsNotApplicable", 0),
          ("alsFspStandard", 1),
          ("alsSdhOptimised", 2))
    )



class AisState(TextualConvention, Integer32):
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
        *(("aisNotApplicable", 0),
          ("aisEnabled", 1),
          ("aisDisabled", 2),
          ("aisNotSupported", 3))
    )



class SectionType(TextualConvention, Integer32):
    status = "current"
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
        *(("sectES", 1),
          ("sectSES", 2),
          ("sectSEFS", 3),
          ("sectCV", 4))
    )



class PathType(TextualConvention, Integer32):
    status = "current"
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
        *(("pathES", 1),
          ("pathSES", 2),
          ("pathCV", 3),
          ("pathUAS", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Fsp3000Products_ObjectIdentity = ObjectIdentity
fsp3000Products = _Fsp3000Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 1)
)
_Fsp3000V1_ObjectIdentity = ObjectIdentity
fsp3000V1 = _Fsp3000V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fsp3000V1.setStatus("current")
_AlarmMIB_ObjectIdentity = ObjectIdentity
alarmMIB = _AlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1)
)
_AlarmFilters_ObjectIdentity = ObjectIdentity
alarmFilters = _AlarmFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1)
)
_InterfaceAlarmSeverityTable_Object = MibTable
interfaceAlarmSeverityTable = _InterfaceAlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceAlarmSeverityTable.setStatus("current")
_InterfaceAlarmSeverityEntry_Object = MibTableRow
interfaceAlarmSeverityEntry = _InterfaceAlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 1, 1)
)
interfaceAlarmSeverityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfaceAlarmSeverityType"),
)
if mibBuilder.loadTexts:
    interfaceAlarmSeverityEntry.setStatus("current")
_InterfaceAlarmSeverityType_Type = InterfaceAlarmTypes
_InterfaceAlarmSeverityType_Object = MibTableColumn
interfaceAlarmSeverityType = _InterfaceAlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 1, 1, 1),
    _InterfaceAlarmSeverityType_Type()
)
interfaceAlarmSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceAlarmSeverityType.setStatus("current")
_InterfaceAlarmSeverityValue_Type = TrapAlarmSeverity
_InterfaceAlarmSeverityValue_Object = MibTableColumn
interfaceAlarmSeverityValue = _InterfaceAlarmSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 1, 1, 2),
    _InterfaceAlarmSeverityValue_Type()
)
interfaceAlarmSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceAlarmSeverityValue.setStatus("current")
_EquipmentAlarmSeverityTable_Object = MibTable
equipmentAlarmSeverityTable = _EquipmentAlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    equipmentAlarmSeverityTable.setStatus("current")
_EquipmentAlarmSeverityEntry_Object = MibTableRow
equipmentAlarmSeverityEntry = _EquipmentAlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 2, 1)
)
equipmentAlarmSeverityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "equipmentAlarmSeverityType"),
)
if mibBuilder.loadTexts:
    equipmentAlarmSeverityEntry.setStatus("current")
_EquipmentAlarmSeverityType_Type = EquipmentAlarmTypes
_EquipmentAlarmSeverityType_Object = MibTableColumn
equipmentAlarmSeverityType = _EquipmentAlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 2, 1, 1),
    _EquipmentAlarmSeverityType_Type()
)
equipmentAlarmSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentAlarmSeverityType.setStatus("current")
_EquipmentAlarmSeverityValue_Type = TrapAlarmSeverity
_EquipmentAlarmSeverityValue_Object = MibTableColumn
equipmentAlarmSeverityValue = _EquipmentAlarmSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 2, 1, 2),
    _EquipmentAlarmSeverityValue_Type()
)
equipmentAlarmSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentAlarmSeverityValue.setStatus("current")
_InterfaceAlarmReportControlTable_Object = MibTable
interfaceAlarmReportControlTable = _InterfaceAlarmReportControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    interfaceAlarmReportControlTable.setStatus("current")
_InterfaceAlarmReportControlEntry_Object = MibTableRow
interfaceAlarmReportControlEntry = _InterfaceAlarmReportControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 3, 1)
)
interfaceAlarmReportControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceAlarmReportControlEntry.setStatus("current")
_InterfaceAlarmReportControlState_Type = ArcState
_InterfaceAlarmReportControlState_Object = MibTableColumn
interfaceAlarmReportControlState = _InterfaceAlarmReportControlState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 3, 1, 1),
    _InterfaceAlarmReportControlState_Type()
)
interfaceAlarmReportControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceAlarmReportControlState.setStatus("current")
_EquipmentAlarmReportControlTable_Object = MibTable
equipmentAlarmReportControlTable = _EquipmentAlarmReportControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    equipmentAlarmReportControlTable.setStatus("current")
_EquipmentAlarmReportControlEntry_Object = MibTableRow
equipmentAlarmReportControlEntry = _EquipmentAlarmReportControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 4, 1)
)
equipmentAlarmReportControlEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    equipmentAlarmReportControlEntry.setStatus("current")
_EquipmentAlarmReportControlState_Type = ArcState
_EquipmentAlarmReportControlState_Object = MibTableColumn
equipmentAlarmReportControlState = _EquipmentAlarmReportControlState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 4, 1, 1),
    _EquipmentAlarmReportControlState_Type()
)
equipmentAlarmReportControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentAlarmReportControlState.setStatus("current")
_InterfaceQoSReportSeverityTable_Object = MibTable
interfaceQoSReportSeverityTable = _InterfaceQoSReportSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    interfaceQoSReportSeverityTable.setStatus("current")
_InterfaceQoSReportSeverityEntry_Object = MibTableRow
interfaceQoSReportSeverityEntry = _InterfaceQoSReportSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 6, 1)
)
interfaceQoSReportSeverityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfaceQoSReportSeverityType"),
)
if mibBuilder.loadTexts:
    interfaceQoSReportSeverityEntry.setStatus("current")
_InterfaceQoSReportSeverityType_Type = InterfaceQoSReportTypes
_InterfaceQoSReportSeverityType_Object = MibTableColumn
interfaceQoSReportSeverityType = _InterfaceQoSReportSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 6, 1, 1),
    _InterfaceQoSReportSeverityType_Type()
)
interfaceQoSReportSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceQoSReportSeverityType.setStatus("current")
_InterfaceQoSReportSeverityValue_Type = TrapAlarmSeverity
_InterfaceQoSReportSeverityValue_Object = MibTableColumn
interfaceQoSReportSeverityValue = _InterfaceQoSReportSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 1, 6, 1, 2),
    _InterfaceQoSReportSeverityValue_Type()
)
interfaceQoSReportSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceQoSReportSeverityValue.setStatus("current")
_CurrentAlarms_ObjectIdentity = ObjectIdentity
currentAlarms = _CurrentAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2)
)
_InterfaceCurrentAlarmTable_Object = MibTable
interfaceCurrentAlarmTable = _InterfaceCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceCurrentAlarmTable.setStatus("current")
_InterfaceCurrentAlarmEntry_Object = MibTableRow
interfaceCurrentAlarmEntry = _InterfaceCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 1, 1)
)
interfaceCurrentAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfaceCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    interfaceCurrentAlarmEntry.setStatus("current")
_InterfaceCurrentAlarmType_Type = InterfaceAlarmTypes
_InterfaceCurrentAlarmType_Object = MibTableColumn
interfaceCurrentAlarmType = _InterfaceCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 1, 1, 1),
    _InterfaceCurrentAlarmType_Type()
)
interfaceCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceCurrentAlarmType.setStatus("current")
_InterfaceCurrentAlarmSeverity_Type = TrapAlarmSeverity
_InterfaceCurrentAlarmSeverity_Object = MibTableColumn
interfaceCurrentAlarmSeverity = _InterfaceCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 1, 1, 2),
    _InterfaceCurrentAlarmSeverity_Type()
)
interfaceCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCurrentAlarmSeverity.setStatus("current")
_EquipmentCurrentAlarmTable_Object = MibTable
equipmentCurrentAlarmTable = _EquipmentCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    equipmentCurrentAlarmTable.setStatus("current")
_EquipmentCurrentAlarmEntry_Object = MibTableRow
equipmentCurrentAlarmEntry = _EquipmentCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 2, 1)
)
equipmentCurrentAlarmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "equipmentCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    equipmentCurrentAlarmEntry.setStatus("current")
_EquipmentCurrentAlarmType_Type = EquipmentAlarmTypes
_EquipmentCurrentAlarmType_Object = MibTableColumn
equipmentCurrentAlarmType = _EquipmentCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 2, 1, 1),
    _EquipmentCurrentAlarmType_Type()
)
equipmentCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentCurrentAlarmType.setStatus("current")
_EquipmentCurrentAlarmSeverity_Type = TrapAlarmSeverity
_EquipmentCurrentAlarmSeverity_Object = MibTableColumn
equipmentCurrentAlarmSeverity = _EquipmentCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 2, 1, 2),
    _EquipmentCurrentAlarmSeverity_Type()
)
equipmentCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentCurrentAlarmSeverity.setStatus("current")
_InterfaceCurrentQoSReportTable_Object = MibTable
interfaceCurrentQoSReportTable = _InterfaceCurrentQoSReportTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    interfaceCurrentQoSReportTable.setStatus("current")
_InterfaceCurrentQoSReportEntry_Object = MibTableRow
interfaceCurrentQoSReportEntry = _InterfaceCurrentQoSReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 3, 1)
)
interfaceCurrentQoSReportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfaceCurrentQoSReportType"),
)
if mibBuilder.loadTexts:
    interfaceCurrentQoSReportEntry.setStatus("current")
_InterfaceCurrentQoSReportType_Type = InterfaceQoSReportTypes
_InterfaceCurrentQoSReportType_Object = MibTableColumn
interfaceCurrentQoSReportType = _InterfaceCurrentQoSReportType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 3, 1, 1),
    _InterfaceCurrentQoSReportType_Type()
)
interfaceCurrentQoSReportType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceCurrentQoSReportType.setStatus("current")
_InterfaceCurrentQoSReportSeverity_Type = TrapAlarmSeverity
_InterfaceCurrentQoSReportSeverity_Object = MibTableColumn
interfaceCurrentQoSReportSeverity = _InterfaceCurrentQoSReportSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 3, 1, 2),
    _InterfaceCurrentQoSReportSeverity_Type()
)
interfaceCurrentQoSReportSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCurrentQoSReportSeverity.setStatus("current")
_ProtectionGroupCurrentAlarmTable_Object = MibTable
protectionGroupCurrentAlarmTable = _ProtectionGroupCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    protectionGroupCurrentAlarmTable.setStatus("current")
_ProtectionGroupCurrentAlarmEntry_Object = MibTableRow
protectionGroupCurrentAlarmEntry = _ProtectionGroupCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 4, 1)
)
protectionGroupCurrentAlarmEntry.setIndexNames(
    (0, "FSP3000-MIB", "channelCardProtectionGroupIndex"),
    (0, "FSP3000-MIB", "protectionGroupCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    protectionGroupCurrentAlarmEntry.setStatus("current")
_ProtectionGroupCurrentAlarmType_Type = ProtectionGroupAlarmTypes
_ProtectionGroupCurrentAlarmType_Object = MibTableColumn
protectionGroupCurrentAlarmType = _ProtectionGroupCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 4, 1, 1),
    _ProtectionGroupCurrentAlarmType_Type()
)
protectionGroupCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protectionGroupCurrentAlarmType.setStatus("current")
_ProtectionGroupCurrentAlarmSeverity_Type = TrapAlarmSeverity
_ProtectionGroupCurrentAlarmSeverity_Object = MibTableColumn
protectionGroupCurrentAlarmSeverity = _ProtectionGroupCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 1, 2, 4, 1, 2),
    _ProtectionGroupCurrentAlarmSeverity_Type()
)
protectionGroupCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionGroupCurrentAlarmSeverity.setStatus("current")
_AdminMIB_ObjectIdentity = ObjectIdentity
adminMIB = _AdminMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2)
)


class _NeType_Type(Integer32):
    """Custom type neType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("fsp3000", 1)
    )


_NeType_Type.__name__ = "Integer32"
_NeType_Object = MibScalar
neType = _NeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 1),
    _NeType_Type()
)
neType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neType.setStatus("current")


class _NeMibVariant_Type(Integer32):
    """Custom type neMibVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_NeMibVariant_Type.__name__ = "Integer32"
_NeMibVariant_Object = MibScalar
neMibVariant = _NeMibVariant_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 2),
    _NeMibVariant_Type()
)
neMibVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMibVariant.setStatus("current")
_NeTrapsinkTable_Object = MibTable
neTrapsinkTable = _NeTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    neTrapsinkTable.setStatus("current")
_NeTrapsinkEntry_Object = MibTableRow
neTrapsinkEntry = _NeTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 3, 1)
)
neTrapsinkEntry.setIndexNames(
    (0, "FSP3000-MIB", "neTrapsinkNumber"),
)
if mibBuilder.loadTexts:
    neTrapsinkEntry.setStatus("current")


class _NeTrapsinkNumber_Type(Integer32):
    """Custom type neTrapsinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NeTrapsinkNumber_Type.__name__ = "Integer32"
_NeTrapsinkNumber_Object = MibTableColumn
neTrapsinkNumber = _NeTrapsinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 3, 1, 1),
    _NeTrapsinkNumber_Type()
)
neTrapsinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTrapsinkNumber.setStatus("current")


class _NeTrapsinkAddress_Type(DisplayString):
    """Custom type neTrapsinkAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_NeTrapsinkAddress_Type.__name__ = "DisplayString"
_NeTrapsinkAddress_Object = MibTableColumn
neTrapsinkAddress = _NeTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 3, 1, 2),
    _NeTrapsinkAddress_Type()
)
neTrapsinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkAddress.setStatus("current")


class _NeTrapsinkCommunity_Type(DisplayString):
    """Custom type neTrapsinkCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NeTrapsinkCommunity_Type.__name__ = "DisplayString"
_NeTrapsinkCommunity_Object = MibTableColumn
neTrapsinkCommunity = _NeTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 3, 1, 3),
    _NeTrapsinkCommunity_Type()
)
neTrapsinkCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkCommunity.setStatus("current")


class _NeTrapsinkPriority_Type(Integer32):
    """Custom type neTrapsinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_NeTrapsinkPriority_Type.__name__ = "Integer32"
_NeTrapsinkPriority_Object = MibTableColumn
neTrapsinkPriority = _NeTrapsinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 3, 1, 4),
    _NeTrapsinkPriority_Type()
)
neTrapsinkPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkPriority.setStatus("current")


class _NeTrapsinkPort_Type(Integer32):
    """Custom type neTrapsinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NeTrapsinkPort_Type.__name__ = "Integer32"
_NeTrapsinkPort_Object = MibTableColumn
neTrapsinkPort = _NeTrapsinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 3, 1, 5),
    _NeTrapsinkPort_Type()
)
neTrapsinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkPort.setStatus("current")
_NeLogfileTable_Object = MibTable
neLogfileTable = _NeLogfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    neLogfileTable.setStatus("current")
_NeLogfileEntry_Object = MibTableRow
neLogfileEntry = _NeLogfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 4, 1)
)
neLogfileEntry.setIndexNames(
    (0, "FSP3000-MIB", "neLogfileNumber"),
)
if mibBuilder.loadTexts:
    neLogfileEntry.setStatus("current")


class _NeLogfileNumber_Type(Integer32):
    """Custom type neLogfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NeLogfileNumber_Type.__name__ = "Integer32"
_NeLogfileNumber_Object = MibTableColumn
neLogfileNumber = _NeLogfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 4, 1, 1),
    _NeLogfileNumber_Type()
)
neLogfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neLogfileNumber.setStatus("current")
_NeLogfileName_Type = DisplayString
_NeLogfileName_Object = MibTableColumn
neLogfileName = _NeLogfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 4, 1, 2),
    _NeLogfileName_Type()
)
neLogfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neLogfileName.setStatus("current")


class _NeLogfileSize_Type(Integer32):
    """Custom type neLogfileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NeLogfileSize_Type.__name__ = "Integer32"
_NeLogfileSize_Object = MibTableColumn
neLogfileSize = _NeLogfileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 4, 1, 3),
    _NeLogfileSize_Type()
)
neLogfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neLogfileSize.setStatus("current")


class _NeLogfilePriority_Type(Integer32):
    """Custom type neLogfilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NeLogfilePriority_Type.__name__ = "Integer32"
_NeLogfilePriority_Object = MibTableColumn
neLogfilePriority = _NeLogfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 4, 1, 4),
    _NeLogfilePriority_Type()
)
neLogfilePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neLogfilePriority.setStatus("current")
_NeEventsLogged_Type = TrapCounter
_NeEventsLogged_Object = MibScalar
neEventsLogged = _NeEventsLogged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 5),
    _NeEventsLogged_Type()
)
neEventsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventsLogged.setStatus("current")
_NeNmsTable_Object = MibTable
neNmsTable = _NeNmsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 6)
)
if mibBuilder.loadTexts:
    neNmsTable.setStatus("current")
_NeNmsEntry_Object = MibTableRow
neNmsEntry = _NeNmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 6, 1)
)
neNmsEntry.setIndexNames(
    (0, "FSP3000-MIB", "neNmsNumber"),
)
if mibBuilder.loadTexts:
    neNmsEntry.setStatus("current")


class _NeNmsNumber_Type(Integer32):
    """Custom type neNmsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NeNmsNumber_Type.__name__ = "Integer32"
_NeNmsNumber_Object = MibTableColumn
neNmsNumber = _NeNmsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 6, 1, 1),
    _NeNmsNumber_Type()
)
neNmsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNmsNumber.setStatus("current")
_NeNmsAddress_Type = DisplayString
_NeNmsAddress_Object = MibTableColumn
neNmsAddress = _NeNmsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 6, 1, 2),
    _NeNmsAddress_Type()
)
neNmsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNmsAddress.setStatus("current")
_NeNmsName_Type = DisplayString
_NeNmsName_Object = MibTableColumn
neNmsName = _NeNmsName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 6, 1, 3),
    _NeNmsName_Type()
)
neNmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNmsName.setStatus("current")
_NeManufacturer_Type = DisplayString
_NeManufacturer_Object = MibScalar
neManufacturer = _NeManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 7),
    _NeManufacturer_Type()
)
neManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neManufacturer.setStatus("current")
_NeNmsFilter_Type = OnOff
_NeNmsFilter_Object = MibScalar
neNmsFilter = _NeNmsFilter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 8),
    _NeNmsFilter_Type()
)
neNmsFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNmsFilter.setStatus("current")


class _DcnDetectedTopologyType_Type(Integer32):
    """Custom type dcnDetectedTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dcnPointToPoint", 1),
          ("dcnChain", 2),
          ("dcnRing", 3))
    )


_DcnDetectedTopologyType_Type.__name__ = "Integer32"
_DcnDetectedTopologyType_Object = MibScalar
dcnDetectedTopologyType = _DcnDetectedTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 9),
    _DcnDetectedTopologyType_Type()
)
dcnDetectedTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnDetectedTopologyType.setStatus("deprecated")
_DcnTopologyTable_Object = MibTable
dcnTopologyTable = _DcnTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    dcnTopologyTable.setStatus("deprecated")
_DcnTopologyEntry_Object = MibTableRow
dcnTopologyEntry = _DcnTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 10, 1)
)
dcnTopologyEntry.setIndexNames(
    (0, "FSP3000-MIB", "dcnTopologyIndex"),
)
if mibBuilder.loadTexts:
    dcnTopologyEntry.setStatus("deprecated")


class _DcnTopologyIndex_Type(Integer32):
    """Custom type dcnTopologyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DcnTopologyIndex_Type.__name__ = "Integer32"
_DcnTopologyIndex_Object = MibTableColumn
dcnTopologyIndex = _DcnTopologyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 10, 1, 1),
    _DcnTopologyIndex_Type()
)
dcnTopologyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnTopologyIndex.setStatus("deprecated")
_DcnTopologyNodeIpAddress_Type = IpAddress
_DcnTopologyNodeIpAddress_Object = MibTableColumn
dcnTopologyNodeIpAddress = _DcnTopologyNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 10, 1, 2),
    _DcnTopologyNodeIpAddress_Type()
)
dcnTopologyNodeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnTopologyNodeIpAddress.setStatus("deprecated")


class _NeNextNeTrapsinkNumber_Type(Integer32):
    """Custom type neNextNeTrapsinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_NeNextNeTrapsinkNumber_Type.__name__ = "Integer32"
_NeNextNeTrapsinkNumber_Object = MibScalar
neNextNeTrapsinkNumber = _NeNextNeTrapsinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 11),
    _NeNextNeTrapsinkNumber_Type()
)
neNextNeTrapsinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNextNeTrapsinkNumber.setStatus("current")


class _NeEventLogSize_Type(Integer32):
    """Custom type neEventLogSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NeEventLogSize_Type.__name__ = "Integer32"
_NeEventLogSize_Object = MibScalar
neEventLogSize = _NeEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 12),
    _NeEventLogSize_Type()
)
neEventLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogSize.setStatus("current")
_NeEventLogTable_Object = MibTable
neEventLogTable = _NeEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 13)
)
if mibBuilder.loadTexts:
    neEventLogTable.setStatus("current")
_NeEventLogEntry_Object = MibTableRow
neEventLogEntry = _NeEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 13, 1)
)
neEventLogEntry.setIndexNames(
    (0, "FSP3000-MIB", "neEventLogIndex"),
)
if mibBuilder.loadTexts:
    neEventLogEntry.setStatus("current")
_NeEventLogIndex_Type = TrapCounter
_NeEventLogIndex_Object = MibTableColumn
neEventLogIndex = _NeEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 13, 1, 1),
    _NeEventLogIndex_Type()
)
neEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neEventLogIndex.setStatus("current")
_NeEventLogTimeStamp_Type = DateAndTime
_NeEventLogTimeStamp_Object = MibTableColumn
neEventLogTimeStamp = _NeEventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 13, 1, 2),
    _NeEventLogTimeStamp_Type()
)
neEventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogTimeStamp.setStatus("current")
_NeEventLogNotificationOID_Type = ObjectIdentifier
_NeEventLogNotificationOID_Object = MibTableColumn
neEventLogNotificationOID = _NeEventLogNotificationOID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 13, 1, 3),
    _NeEventLogNotificationOID_Type()
)
neEventLogNotificationOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogNotificationOID.setStatus("current")
_NeEventLogVarTable_Object = MibTable
neEventLogVarTable = _NeEventLogVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 14)
)
if mibBuilder.loadTexts:
    neEventLogVarTable.setStatus("current")
_NeEventLogVarEntry_Object = MibTableRow
neEventLogVarEntry = _NeEventLogVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 14, 1)
)
neEventLogVarEntry.setIndexNames(
    (0, "FSP3000-MIB", "neEventLogIndex"),
    (0, "FSP3000-MIB", "neEventLogVarIndex"),
)
if mibBuilder.loadTexts:
    neEventLogVarEntry.setStatus("current")
_NeEventLogVarIndex_Type = Unsigned32
_NeEventLogVarIndex_Object = MibTableColumn
neEventLogVarIndex = _NeEventLogVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 14, 1, 1),
    _NeEventLogVarIndex_Type()
)
neEventLogVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neEventLogVarIndex.setStatus("current")
_NeEventLogVarId_Type = ObjectIdentifier
_NeEventLogVarId_Object = MibTableColumn
neEventLogVarId = _NeEventLogVarId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 14, 1, 2),
    _NeEventLogVarId_Type()
)
neEventLogVarId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarId.setStatus("current")


class _NeEventLogVarType_Type(Integer32):
    """Custom type neEventLogVarType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("integer32", 4),
          ("octetString", 6))
    )


_NeEventLogVarType_Type.__name__ = "Integer32"
_NeEventLogVarType_Object = MibTableColumn
neEventLogVarType = _NeEventLogVarType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 14, 1, 3),
    _NeEventLogVarType_Type()
)
neEventLogVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarType.setStatus("current")
_NeEventLogVarInteger32Val_Type = Integer32
_NeEventLogVarInteger32Val_Object = MibTableColumn
neEventLogVarInteger32Val = _NeEventLogVarInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 14, 1, 4),
    _NeEventLogVarInteger32Val_Type()
)
neEventLogVarInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarInteger32Val.setStatus("current")


class _NeEventLogVarOctetStringVal_Type(OctetString):
    """Custom type neEventLogVarOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NeEventLogVarOctetStringVal_Type.__name__ = "OctetString"
_NeEventLogVarOctetStringVal_Object = MibTableColumn
neEventLogVarOctetStringVal = _NeEventLogVarOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 14, 1, 5),
    _NeEventLogVarOctetStringVal_Type()
)
neEventLogVarOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarOctetStringVal.setStatus("current")
_NeShelfTable_Object = MibTable
neShelfTable = _NeShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 15)
)
if mibBuilder.loadTexts:
    neShelfTable.setStatus("current")
_NeShelfEntry_Object = MibTableRow
neShelfEntry = _NeShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 15, 1)
)
neShelfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    neShelfEntry.setStatus("current")


class _NeShelfSize_Type(Integer32):
    """Custom type neShelfSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("size19", 1),
          ("size21", 2),
          ("sizeSL", 3))
    )


_NeShelfSize_Type.__name__ = "Integer32"
_NeShelfSize_Object = MibTableColumn
neShelfSize = _NeShelfSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 15, 1, 1),
    _NeShelfSize_Type()
)
neShelfSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neShelfSize.setStatus("current")


class _NeShelfIdentifier_Type(DisplayString):
    """Custom type neShelfIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NeShelfIdentifier_Type.__name__ = "DisplayString"
_NeShelfIdentifier_Object = MibTableColumn
neShelfIdentifier = _NeShelfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 15, 1, 2),
    _NeShelfIdentifier_Type()
)
neShelfIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neShelfIdentifier.setStatus("current")
_DcnSecurityMode_Type = EnableState
_DcnSecurityMode_Object = MibScalar
dcnSecurityMode = _DcnSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 16),
    _DcnSecurityMode_Type()
)
dcnSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcnSecurityMode.setStatus("current")
_OscmTopologyTable_Object = MibTable
oscmTopologyTable = _OscmTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 17)
)
if mibBuilder.loadTexts:
    oscmTopologyTable.setStatus("current")
_OscmTopologyEntry_Object = MibTableRow
oscmTopologyEntry = _OscmTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 17, 1)
)
oscmTopologyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "oscmTopologyIndex"),
)
if mibBuilder.loadTexts:
    oscmTopologyEntry.setStatus("current")


class _OscmTopologyIndex_Type(Integer32):
    """Custom type oscmTopologyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OscmTopologyIndex_Type.__name__ = "Integer32"
_OscmTopologyIndex_Object = MibTableColumn
oscmTopologyIndex = _OscmTopologyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 17, 1, 1),
    _OscmTopologyIndex_Type()
)
oscmTopologyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oscmTopologyIndex.setStatus("current")
_OscmTopologyAddress_Type = IpAddress
_OscmTopologyAddress_Object = MibTableColumn
oscmTopologyAddress = _OscmTopologyAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 17, 1, 2),
    _OscmTopologyAddress_Type()
)
oscmTopologyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscmTopologyAddress.setStatus("current")
_OscmTopologyNetmask_Type = IpAddress
_OscmTopologyNetmask_Object = MibTableColumn
oscmTopologyNetmask = _OscmTopologyNetmask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 17, 1, 3),
    _OscmTopologyNetmask_Type()
)
oscmTopologyNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscmTopologyNetmask.setStatus("current")
_OscmDetectedTopologyTable_Object = MibTable
oscmDetectedTopologyTable = _OscmDetectedTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 18)
)
if mibBuilder.loadTexts:
    oscmDetectedTopologyTable.setStatus("current")
_OscmDetectedTopologyEntry_Object = MibTableRow
oscmDetectedTopologyEntry = _OscmDetectedTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 18, 1)
)
oscmDetectedTopologyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    oscmDetectedTopologyEntry.setStatus("current")


class _OscmDetectedTopologyType_Type(Integer32):
    """Custom type oscmDetectedTopologyType based on Integer32"""
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
        *(("dcnPointToPoint", 1),
          ("dcnChain", 2),
          ("dcnRing", 3),
          ("dcnBranchPointToPoint", 4),
          ("dcnBranchPointToMultiPoint", 5),
          ("dcnBranchUndetected", 6))
    )


_OscmDetectedTopologyType_Type.__name__ = "Integer32"
_OscmDetectedTopologyType_Object = MibTableColumn
oscmDetectedTopologyType = _OscmDetectedTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 18, 1, 1),
    _OscmDetectedTopologyType_Type()
)
oscmDetectedTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscmDetectedTopologyType.setStatus("current")
_SoftwareUpgradeMIB_ObjectIdentity = ObjectIdentity
softwareUpgradeMIB = _SoftwareUpgradeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19)
)
_ActualFspSwVersion_Type = DisplayString
_ActualFspSwVersion_Object = MibScalar
actualFspSwVersion = _ActualFspSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 1),
    _ActualFspSwVersion_Type()
)
actualFspSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualFspSwVersion.setStatus("current")
_PreviousFspSwVersion_Type = DisplayString
_PreviousFspSwVersion_Object = MibScalar
previousFspSwVersion = _PreviousFspSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 2),
    _PreviousFspSwVersion_Type()
)
previousFspSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    previousFspSwVersion.setStatus("current")
_FspSwUpgradeTable_Object = MibTable
fspSwUpgradeTable = _FspSwUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3)
)
if mibBuilder.loadTexts:
    fspSwUpgradeTable.setStatus("current")
_FspSwUpgradeEntry_Object = MibTableRow
fspSwUpgradeEntry = _FspSwUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1)
)
fspSwUpgradeEntry.setIndexNames(
    (0, "FSP3000-MIB", "fspSwUpgradeIndex"),
)
if mibBuilder.loadTexts:
    fspSwUpgradeEntry.setStatus("current")


class _FspSwUpgradeIndex_Type(Integer32):
    """Custom type fspSwUpgradeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_FspSwUpgradeIndex_Type.__name__ = "Integer32"
_FspSwUpgradeIndex_Object = MibTableColumn
fspSwUpgradeIndex = _FspSwUpgradeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 1),
    _FspSwUpgradeIndex_Type()
)
fspSwUpgradeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fspSwUpgradeIndex.setStatus("current")
_FspSwUpgradeServerIpAddress_Type = IpAddress
_FspSwUpgradeServerIpAddress_Object = MibTableColumn
fspSwUpgradeServerIpAddress = _FspSwUpgradeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 2),
    _FspSwUpgradeServerIpAddress_Type()
)
fspSwUpgradeServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeServerIpAddress.setStatus("current")
_FspSwUpgradeServerLogin_Type = DisplayString
_FspSwUpgradeServerLogin_Object = MibTableColumn
fspSwUpgradeServerLogin = _FspSwUpgradeServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 3),
    _FspSwUpgradeServerLogin_Type()
)
fspSwUpgradeServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeServerLogin.setStatus("current")
_FspSwUpgradeServerPassword_Type = DisplayString
_FspSwUpgradeServerPassword_Object = MibTableColumn
fspSwUpgradeServerPassword = _FspSwUpgradeServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 4),
    _FspSwUpgradeServerPassword_Type()
)
fspSwUpgradeServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeServerPassword.setStatus("current")
_FspSwUpgradeServerFileLocation_Type = DisplayString
_FspSwUpgradeServerFileLocation_Object = MibTableColumn
fspSwUpgradeServerFileLocation = _FspSwUpgradeServerFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 5),
    _FspSwUpgradeServerFileLocation_Type()
)
fspSwUpgradeServerFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeServerFileLocation.setStatus("current")
_FspSwUpgradeFileName_Type = DisplayString
_FspSwUpgradeFileName_Object = MibTableColumn
fspSwUpgradeFileName = _FspSwUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 6),
    _FspSwUpgradeFileName_Type()
)
fspSwUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeFileName.setStatus("current")


class _FspSwUpgradeType_Type(Integer32):
    """Custom type fspSwUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upgradeNEMI", 1)
    )


_FspSwUpgradeType_Type.__name__ = "Integer32"
_FspSwUpgradeType_Object = MibTableColumn
fspSwUpgradeType = _FspSwUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 7),
    _FspSwUpgradeType_Type()
)
fspSwUpgradeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspSwUpgradeType.setStatus("current")


class _FspSwUpgradeRequest_Type(Integer32):
    """Custom type fspSwUpgradeRequest based on Integer32"""
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
        *(("none", 1),
          ("download", 2),
          ("activate", 3),
          ("downloadActivate", 4),
          ("downloadActivateReboot", 5),
          ("activateReboot", 6),
          ("reboot", 7),
          ("reInstallPreviousVersion", 8))
    )


_FspSwUpgradeRequest_Type.__name__ = "Integer32"
_FspSwUpgradeRequest_Object = MibTableColumn
fspSwUpgradeRequest = _FspSwUpgradeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 8),
    _FspSwUpgradeRequest_Type()
)
fspSwUpgradeRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeRequest.setStatus("current")
_FspSwUpgradeStatus_Type = SwUpgradeStatusType
_FspSwUpgradeStatus_Object = MibTableColumn
fspSwUpgradeStatus = _FspSwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 3, 1, 9),
    _FspSwUpgradeStatus_Type()
)
fspSwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspSwUpgradeStatus.setStatus("current")
_FspRebootTable_Object = MibTable
fspRebootTable = _FspRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 4)
)
if mibBuilder.loadTexts:
    fspRebootTable.setStatus("current")
_FspRebootEntry_Object = MibTableRow
fspRebootEntry = _FspRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 4, 1)
)
fspRebootEntry.setIndexNames(
    (0, "FSP3000-MIB", "fspSwUpgradeIndex"),
)
if mibBuilder.loadTexts:
    fspRebootEntry.setStatus("current")


class _FspRebootType_Type(Integer32):
    """Custom type fspRebootType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FspRebootType_Type.__name__ = "Integer32"
_FspRebootType_Object = MibTableColumn
fspRebootType = _FspRebootType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 4, 1, 1),
    _FspRebootType_Type()
)
fspRebootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspRebootType.setStatus("current")
_FspRebootTimeStamp_Type = DateAndTime
_FspRebootTimeStamp_Object = MibTableColumn
fspRebootTimeStamp = _FspRebootTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 4, 1, 2),
    _FspRebootTimeStamp_Type()
)
fspRebootTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspRebootTimeStamp.setStatus("current")
_UcmSwUpgradeTable_Object = MibTable
ucmSwUpgradeTable = _UcmSwUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 5)
)
if mibBuilder.loadTexts:
    ucmSwUpgradeTable.setStatus("current")
_UcmSwUpgradeEntry_Object = MibTableRow
ucmSwUpgradeEntry = _UcmSwUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 5, 1)
)
ucmSwUpgradeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ucmSwUpgradeEntry.setStatus("current")
_UcmSwUpgradeCurrentVersion_Type = DisplayString
_UcmSwUpgradeCurrentVersion_Object = MibTableColumn
ucmSwUpgradeCurrentVersion = _UcmSwUpgradeCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 5, 1, 1),
    _UcmSwUpgradeCurrentVersion_Type()
)
ucmSwUpgradeCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucmSwUpgradeCurrentVersion.setStatus("current")
_UcmSwUpgradeAvailableVersion_Type = DisplayString
_UcmSwUpgradeAvailableVersion_Object = MibTableColumn
ucmSwUpgradeAvailableVersion = _UcmSwUpgradeAvailableVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 5, 1, 2),
    _UcmSwUpgradeAvailableVersion_Type()
)
ucmSwUpgradeAvailableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucmSwUpgradeAvailableVersion.setStatus("current")


class _UcmSwUpgradeRequest_Type(Integer32):
    """Custom type ucmSwUpgradeRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("downloadActivate", 4))
    )


_UcmSwUpgradeRequest_Type.__name__ = "Integer32"
_UcmSwUpgradeRequest_Object = MibTableColumn
ucmSwUpgradeRequest = _UcmSwUpgradeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 5, 1, 3),
    _UcmSwUpgradeRequest_Type()
)
ucmSwUpgradeRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucmSwUpgradeRequest.setStatus("current")
_UcmSwUpgradeStatus_Type = SwUpgradeStatusType
_UcmSwUpgradeStatus_Object = MibTableColumn
ucmSwUpgradeStatus = _UcmSwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 19, 5, 1, 4),
    _UcmSwUpgradeStatus_Type()
)
ucmSwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucmSwUpgradeStatus.setStatus("current")
_PlannedConfigTable_Object = MibTable
plannedConfigTable = _PlannedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20)
)
if mibBuilder.loadTexts:
    plannedConfigTable.setStatus("current")
_PlannedConfigEntry_Object = MibTableRow
plannedConfigEntry = _PlannedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1)
)
plannedConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    plannedConfigEntry.setStatus("current")


class _PlannedConfigContainedIn_Type(Integer32):
    """Custom type plannedConfigContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PlannedConfigContainedIn_Type.__name__ = "Integer32"
_PlannedConfigContainedIn_Object = MibTableColumn
plannedConfigContainedIn = _PlannedConfigContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 1),
    _PlannedConfigContainedIn_Type()
)
plannedConfigContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plannedConfigContainedIn.setStatus("current")
_PlannedConfigClass_Type = PhysicalClass
_PlannedConfigClass_Object = MibTableColumn
plannedConfigClass = _PlannedConfigClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 2),
    _PlannedConfigClass_Type()
)
plannedConfigClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plannedConfigClass.setStatus("current")


class _PlannedConfigParentRelPos_Type(Integer32):
    """Custom type plannedConfigParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_PlannedConfigParentRelPos_Type.__name__ = "Integer32"
_PlannedConfigParentRelPos_Object = MibTableColumn
plannedConfigParentRelPos = _PlannedConfigParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 3),
    _PlannedConfigParentRelPos_Type()
)
plannedConfigParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plannedConfigParentRelPos.setStatus("current")
_PlannedConfigName_Type = SnmpAdminString
_PlannedConfigName_Object = MibTableColumn
plannedConfigName = _PlannedConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 4),
    _PlannedConfigName_Type()
)
plannedConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plannedConfigName.setStatus("current")
_PlannedConfigState_Type = PlannedState
_PlannedConfigState_Object = MibTableColumn
plannedConfigState = _PlannedConfigState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 5),
    _PlannedConfigState_Type()
)
plannedConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plannedConfigState.setStatus("current")


class _PlannedConfigRequest_Type(Integer32):
    """Custom type plannedConfigRequest based on Integer32"""
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
        *(("planningNotAppl", 1),
          ("planToCurrent", 2),
          ("planToInput", 3),
          ("notPlanned", 4),
          ("planNoRequest", 5))
    )


_PlannedConfigRequest_Type.__name__ = "Integer32"
_PlannedConfigRequest_Object = MibTableColumn
plannedConfigRequest = _PlannedConfigRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 6),
    _PlannedConfigRequest_Type()
)
plannedConfigRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plannedConfigRequest.setStatus("current")


class _PlannedConfigCardType_Type(Integer32):
    """Custom type plannedConfigCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PlannedConfigCardType_Type.__name__ = "Integer32"
_PlannedConfigCardType_Object = MibTableColumn
plannedConfigCardType = _PlannedConfigCardType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 7),
    _PlannedConfigCardType_Type()
)
plannedConfigCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plannedConfigCardType.setStatus("current")


class _PlannedConfigProperty1_Type(Integer32):
    """Custom type plannedConfigProperty1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PlannedConfigProperty1_Type.__name__ = "Integer32"
_PlannedConfigProperty1_Object = MibTableColumn
plannedConfigProperty1 = _PlannedConfigProperty1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 8),
    _PlannedConfigProperty1_Type()
)
plannedConfigProperty1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plannedConfigProperty1.setStatus("current")


class _PlannedConfigProperty2_Type(Integer32):
    """Custom type plannedConfigProperty2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PlannedConfigProperty2_Type.__name__ = "Integer32"
_PlannedConfigProperty2_Object = MibTableColumn
plannedConfigProperty2 = _PlannedConfigProperty2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 9),
    _PlannedConfigProperty2_Type()
)
plannedConfigProperty2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plannedConfigProperty2.setStatus("current")


class _PlannedConfigProperty3_Type(Integer32):
    """Custom type plannedConfigProperty3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PlannedConfigProperty3_Type.__name__ = "Integer32"
_PlannedConfigProperty3_Object = MibTableColumn
plannedConfigProperty3 = _PlannedConfigProperty3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 10),
    _PlannedConfigProperty3_Type()
)
plannedConfigProperty3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plannedConfigProperty3.setStatus("current")


class _PlannedConfigProperty4_Type(Integer32):
    """Custom type plannedConfigProperty4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PlannedConfigProperty4_Type.__name__ = "Integer32"
_PlannedConfigProperty4_Object = MibTableColumn
plannedConfigProperty4 = _PlannedConfigProperty4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 11),
    _PlannedConfigProperty4_Type()
)
plannedConfigProperty4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plannedConfigProperty4.setStatus("current")
_PlannedConfigDescr_Type = SnmpAdminString
_PlannedConfigDescr_Object = MibTableColumn
plannedConfigDescr = _PlannedConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 20, 1, 12),
    _PlannedConfigDescr_Type()
)
plannedConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plannedConfigDescr.setStatus("current")
_SupportedCardTable_Object = MibTable
supportedCardTable = _SupportedCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 21)
)
if mibBuilder.loadTexts:
    supportedCardTable.setStatus("current")
_SupportedCardEntry_Object = MibTableRow
supportedCardEntry = _SupportedCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 21, 1)
)
supportedCardEntry.setIndexNames(
    (0, "FSP3000-MIB", "supportedCardIndex"),
)
if mibBuilder.loadTexts:
    supportedCardEntry.setStatus("current")


class _SupportedCardIndex_Type(Integer32):
    """Custom type supportedCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SupportedCardIndex_Type.__name__ = "Integer32"
_SupportedCardIndex_Object = MibTableColumn
supportedCardIndex = _SupportedCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 21, 1, 1),
    _SupportedCardIndex_Type()
)
supportedCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    supportedCardIndex.setStatus("current")


class _SupportedCardType_Type(Integer32):
    """Custom type supportedCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SupportedCardType_Type.__name__ = "Integer32"
_SupportedCardType_Object = MibTableColumn
supportedCardType = _SupportedCardType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 21, 1, 2),
    _SupportedCardType_Type()
)
supportedCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportedCardType.setStatus("current")
_SupportedCardClockType_Type = ClockType
_SupportedCardClockType_Object = MibTableColumn
supportedCardClockType = _SupportedCardClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 21, 1, 3),
    _SupportedCardClockType_Type()
)
supportedCardClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportedCardClockType.setStatus("current")
_SupportedCardName_Type = SnmpAdminString
_SupportedCardName_Object = MibTableColumn
supportedCardName = _SupportedCardName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 21, 1, 4),
    _SupportedCardName_Type()
)
supportedCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportedCardName.setStatus("current")


class _SupportedCardProperties_Type(Integer32):
    """Custom type supportedCardProperties based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SupportedCardProperties_Type.__name__ = "Integer32"
_SupportedCardProperties_Object = MibTableColumn
supportedCardProperties = _SupportedCardProperties_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 21, 1, 5),
    _SupportedCardProperties_Type()
)
supportedCardProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportedCardProperties.setStatus("current")
_NeAutoProvisioning_Type = EnableState
_NeAutoProvisioning_Object = MibScalar
neAutoProvisioning = _NeAutoProvisioning_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 22),
    _NeAutoProvisioning_Type()
)
neAutoProvisioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAutoProvisioning.setStatus("current")
_NeCurrentDateAndTime_Type = DateAndTime
_NeCurrentDateAndTime_Object = MibScalar
neCurrentDateAndTime = _NeCurrentDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 23),
    _NeCurrentDateAndTime_Type()
)
neCurrentDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neCurrentDateAndTime.setStatus("current")
_NeBackupRestore_ObjectIdentity = ObjectIdentity
neBackupRestore = _NeBackupRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 30)
)


class _NeBackupRestoreRequest_Type(Integer32):
    """Custom type neBackupRestoreRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("runBackup", 2),
          ("runRestore", 3))
    )


_NeBackupRestoreRequest_Type.__name__ = "Integer32"
_NeBackupRestoreRequest_Object = MibScalar
neBackupRestoreRequest = _NeBackupRestoreRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 30, 1),
    _NeBackupRestoreRequest_Type()
)
neBackupRestoreRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neBackupRestoreRequest.setStatus("current")


class _NeBackupRestoreState_Type(Integer32):
    """Custom type neBackupRestoreState based on Integer32"""
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
        *(("noBackupAvailable", 1),
          ("backupInProgress", 2),
          ("backupAvailable", 3),
          ("restoreInProgress", 4))
    )


_NeBackupRestoreState_Type.__name__ = "Integer32"
_NeBackupRestoreState_Object = MibScalar
neBackupRestoreState = _NeBackupRestoreState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 30, 2),
    _NeBackupRestoreState_Type()
)
neBackupRestoreState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neBackupRestoreState.setStatus("current")
_NeBackupRestoreFile_Type = SnmpAdminString
_NeBackupRestoreFile_Object = MibScalar
neBackupRestoreFile = _NeBackupRestoreFile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 30, 3),
    _NeBackupRestoreFile_Type()
)
neBackupRestoreFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neBackupRestoreFile.setStatus("current")
_NeRestoreFileBackupDate_Type = DateAndTime
_NeRestoreFileBackupDate_Object = MibScalar
neRestoreFileBackupDate = _NeRestoreFileBackupDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 2, 30, 4),
    _NeRestoreFileBackupDate_Type()
)
neRestoreFileBackupDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neRestoreFileBackupDate.setStatus("current")
_TrapMIB_ObjectIdentity = ObjectIdentity
trapMIB = _TrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3)
)
_TrapMibPrefix_ObjectIdentity = ObjectIdentity
trapMibPrefix = _TrapMibPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0)
)
_TrapVariables_ObjectIdentity = ObjectIdentity
trapVariables = _TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 1)
)
_ContainerState_Type = ContainerState
_ContainerState_Object = MibScalar
containerState = _ContainerState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 1, 1),
    _ContainerState_Type()
)
containerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    containerState.setStatus("current")
_ContainsPhysicalIndex_Type = ContainsPhysicalIndex
_ContainsPhysicalIndex_Object = MibScalar
containsPhysicalIndex = _ContainsPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 1, 2),
    _ContainsPhysicalIndex_Type()
)
containsPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    containsPhysicalIndex.setStatus("current")
_LoginIdentity_Type = LoginIdentity
_LoginIdentity_Object = MibScalar
loginIdentity = _LoginIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 1, 3),
    _LoginIdentity_Type()
)
loginIdentity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loginIdentity.setStatus("current")


class _SourceAddress_Type(DisplayString):
    """Custom type sourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_SourceAddress_Type.__name__ = "DisplayString"
_SourceAddress_Object = MibScalar
sourceAddress = _SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 1, 4),
    _SourceAddress_Type()
)
sourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sourceAddress.setStatus("current")
_IdentityTranslation_Type = IdentityTranslation
_IdentityTranslation_Object = MibScalar
identityTranslation = _IdentityTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 1, 5),
    _IdentityTranslation_Type()
)
identityTranslation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    identityTranslation.setStatus("current")
_ConfigurationMIB_ObjectIdentity = ObjectIdentity
configurationMIB = _ConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4)
)
_InterfaceConfiguration_ObjectIdentity = ObjectIdentity
interfaceConfiguration = _InterfaceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1)
)
_InterfaceTrailTerminationTable_Object = MibTable
interfaceTrailTerminationTable = _InterfaceTrailTerminationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceTrailTerminationTable.setStatus("current")
_InterfaceTrailTerminationEntry_Object = MibTableRow
interfaceTrailTerminationEntry = _InterfaceTrailTerminationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1)
)
interfaceTrailTerminationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceTrailTerminationEntry.setStatus("current")


class _InterfaceTrailTerminationTrailIdentifier_Type(DisplayString):
    """Custom type interfaceTrailTerminationTrailIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_InterfaceTrailTerminationTrailIdentifier_Type.__name__ = "DisplayString"
_InterfaceTrailTerminationTrailIdentifier_Object = MibTableColumn
interfaceTrailTerminationTrailIdentifier = _InterfaceTrailTerminationTrailIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 1),
    _InterfaceTrailTerminationTrailIdentifier_Type()
)
interfaceTrailTerminationTrailIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationTrailIdentifier.setStatus("current")
_InterfaceTrailTerminationLoopState_Type = OnOff
_InterfaceTrailTerminationLoopState_Object = MibTableColumn
interfaceTrailTerminationLoopState = _InterfaceTrailTerminationLoopState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 2),
    _InterfaceTrailTerminationLoopState_Type()
)
interfaceTrailTerminationLoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationLoopState.setStatus("current")
_InterfaceTrailTerminationLaserTxState_Type = TxState
_InterfaceTrailTerminationLaserTxState_Object = MibTableColumn
interfaceTrailTerminationLaserTxState = _InterfaceTrailTerminationLaserTxState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 3),
    _InterfaceTrailTerminationLaserTxState_Type()
)
interfaceTrailTerminationLaserTxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationLaserTxState.setStatus("current")
_InterfaceTrailTerminationLaserTxCurrent_Type = Integer32
_InterfaceTrailTerminationLaserTxCurrent_Object = MibTableColumn
interfaceTrailTerminationLaserTxCurrent = _InterfaceTrailTerminationLaserTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 4),
    _InterfaceTrailTerminationLaserTxCurrent_Type()
)
interfaceTrailTerminationLaserTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationLaserTxCurrent.setStatus("current")
_InterfaceTrailTerminationLaserTxTemp_Type = Integer32
_InterfaceTrailTerminationLaserTxTemp_Object = MibTableColumn
interfaceTrailTerminationLaserTxTemp = _InterfaceTrailTerminationLaserTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 5),
    _InterfaceTrailTerminationLaserTxTemp_Type()
)
interfaceTrailTerminationLaserTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationLaserTxTemp.setStatus("current")
_InterfaceTrailTerminationRxClockFreq_Type = ClockDataRate
_InterfaceTrailTerminationRxClockFreq_Object = MibTableColumn
interfaceTrailTerminationRxClockFreq = _InterfaceTrailTerminationRxClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 6),
    _InterfaceTrailTerminationRxClockFreq_Type()
)
interfaceTrailTerminationRxClockFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationRxClockFreq.setStatus("current")
_InterfaceTrailTerminationRxClockType_Type = ClockType
_InterfaceTrailTerminationRxClockType_Object = MibTableColumn
interfaceTrailTerminationRxClockType = _InterfaceTrailTerminationRxClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 7),
    _InterfaceTrailTerminationRxClockType_Type()
)
interfaceTrailTerminationRxClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationRxClockType.setStatus("current")


class _InterfaceTrailTerminationWavelength_Type(DisplayString):
    """Custom type interfaceTrailTerminationWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_InterfaceTrailTerminationWavelength_Type.__name__ = "DisplayString"
_InterfaceTrailTerminationWavelength_Object = MibTableColumn
interfaceTrailTerminationWavelength = _InterfaceTrailTerminationWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 8),
    _InterfaceTrailTerminationWavelength_Type()
)
interfaceTrailTerminationWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationWavelength.setStatus("current")


class _InterfaceTrailTerminationFspChannelNo_Type(Integer32):
    """Custom type interfaceTrailTerminationFspChannelNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_InterfaceTrailTerminationFspChannelNo_Type.__name__ = "Integer32"
_InterfaceTrailTerminationFspChannelNo_Object = MibTableColumn
interfaceTrailTerminationFspChannelNo = _InterfaceTrailTerminationFspChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 9),
    _InterfaceTrailTerminationFspChannelNo_Type()
)
interfaceTrailTerminationFspChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationFspChannelNo.setStatus("current")
_InterfaceTrailTerminationOIP_Type = Integer32
_InterfaceTrailTerminationOIP_Object = MibTableColumn
interfaceTrailTerminationOIP = _InterfaceTrailTerminationOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 10),
    _InterfaceTrailTerminationOIP_Type()
)
interfaceTrailTerminationOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationOIP.setStatus("current")
_InterfaceTrailTerminationApdVoltage_Type = Integer32
_InterfaceTrailTerminationApdVoltage_Object = MibTableColumn
interfaceTrailTerminationApdVoltage = _InterfaceTrailTerminationApdVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 11),
    _InterfaceTrailTerminationApdVoltage_Type()
)
interfaceTrailTerminationApdVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationApdVoltage.setStatus("current")
_InterfaceTrailTerminationOOP_Type = Integer32
_InterfaceTrailTerminationOOP_Object = MibTableColumn
interfaceTrailTerminationOOP = _InterfaceTrailTerminationOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 12),
    _InterfaceTrailTerminationOOP_Type()
)
interfaceTrailTerminationOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationOOP.setStatus("current")
_InterfaceTrailTerminationLaserType_Type = LaserType
_InterfaceTrailTerminationLaserType_Object = MibTableColumn
interfaceTrailTerminationLaserType = _InterfaceTrailTerminationLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 13),
    _InterfaceTrailTerminationLaserType_Type()
)
interfaceTrailTerminationLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationLaserType.setStatus("current")
_InterfaceTrailTerminationFECState_Type = OtuFecState
_InterfaceTrailTerminationFECState_Object = MibTableColumn
interfaceTrailTerminationFECState = _InterfaceTrailTerminationFECState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 14),
    _InterfaceTrailTerminationFECState_Type()
)
interfaceTrailTerminationFECState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationFECState.setStatus("current")
_InterfaceTrailTerminationTimingSource_Type = TimingSource
_InterfaceTrailTerminationTimingSource_Object = MibTableColumn
interfaceTrailTerminationTimingSource = _InterfaceTrailTerminationTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 15),
    _InterfaceTrailTerminationTimingSource_Type()
)
interfaceTrailTerminationTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationTimingSource.setStatus("current")
_InterfaceTrailTerminationFECOHMonitoring_Type = EnableState
_InterfaceTrailTerminationFECOHMonitoring_Object = MibTableColumn
interfaceTrailTerminationFECOHMonitoring = _InterfaceTrailTerminationFECOHMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 16),
    _InterfaceTrailTerminationFECOHMonitoring_Type()
)
interfaceTrailTerminationFECOHMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationFECOHMonitoring.setStatus("current")
_InterfaceTrailTerminationFECSupported_Type = OtuFecSupported
_InterfaceTrailTerminationFECSupported_Object = MibTableColumn
interfaceTrailTerminationFECSupported = _InterfaceTrailTerminationFECSupported_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 1, 1, 17),
    _InterfaceTrailTerminationFECSupported_Type()
)
interfaceTrailTerminationFECSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationFECSupported.setStatus("current")
_ElectricalInterfaceTable_Object = MibTable
electricalInterfaceTable = _ElectricalInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    electricalInterfaceTable.setStatus("current")
_ElectricalInterfaceEntry_Object = MibTableRow
electricalInterfaceEntry = _ElectricalInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 2, 1)
)
electricalInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    electricalInterfaceEntry.setStatus("current")


class _ElectricalInterfaceIdentifier_Type(DisplayString):
    """Custom type electricalInterfaceIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ElectricalInterfaceIdentifier_Type.__name__ = "DisplayString"
_ElectricalInterfaceIdentifier_Object = MibTableColumn
electricalInterfaceIdentifier = _ElectricalInterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 2, 1, 1),
    _ElectricalInterfaceIdentifier_Type()
)
electricalInterfaceIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceIdentifier.setStatus("current")
_ElectricalInterfaceTxAutoNegotiation_Type = OnOff
_ElectricalInterfaceTxAutoNegotiation_Object = MibTableColumn
electricalInterfaceTxAutoNegotiation = _ElectricalInterfaceTxAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 2, 1, 2),
    _ElectricalInterfaceTxAutoNegotiation_Type()
)
electricalInterfaceTxAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceTxAutoNegotiation.setStatus("current")


class _ElectricalInterfaceTxMode_Type(Integer32):
    """Custom type electricalInterfaceTxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplexMode", 1),
          ("duplexMode", 2))
    )


_ElectricalInterfaceTxMode_Type.__name__ = "Integer32"
_ElectricalInterfaceTxMode_Object = MibTableColumn
electricalInterfaceTxMode = _ElectricalInterfaceTxMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 2, 1, 3),
    _ElectricalInterfaceTxMode_Type()
)
electricalInterfaceTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceTxMode.setStatus("current")


class _ElectricalInterfaceLineSpeed_Type(Integer32):
    """Custom type electricalInterfaceLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_ElectricalInterfaceLineSpeed_Type.__name__ = "Integer32"
_ElectricalInterfaceLineSpeed_Object = MibTableColumn
electricalInterfaceLineSpeed = _ElectricalInterfaceLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 2, 1, 4),
    _ElectricalInterfaceLineSpeed_Type()
)
electricalInterfaceLineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceLineSpeed.setStatus("current")
_EdfaInterfaceTable_Object = MibTable
edfaInterfaceTable = _EdfaInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    edfaInterfaceTable.setStatus("current")
_EdfaInterfaceEntry_Object = MibTableRow
edfaInterfaceEntry = _EdfaInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1)
)
edfaInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    edfaInterfaceEntry.setStatus("current")


class _EdfaInterfaceIdentifier_Type(DisplayString):
    """Custom type edfaInterfaceIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EdfaInterfaceIdentifier_Type.__name__ = "DisplayString"
_EdfaInterfaceIdentifier_Object = MibTableColumn
edfaInterfaceIdentifier = _EdfaInterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 1),
    _EdfaInterfaceIdentifier_Type()
)
edfaInterfaceIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaInterfaceIdentifier.setStatus("current")


class _EdfaInterfaceOpticalBandType_Type(Integer32):
    """Custom type edfaInterfaceOpticalBandType based on Integer32"""
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
        *(("notConfigured", 0),
          ("cBand", 1),
          ("lBand", 2),
          ("unknown", 3))
    )


_EdfaInterfaceOpticalBandType_Type.__name__ = "Integer32"
_EdfaInterfaceOpticalBandType_Object = MibTableColumn
edfaInterfaceOpticalBandType = _EdfaInterfaceOpticalBandType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 2),
    _EdfaInterfaceOpticalBandType_Type()
)
edfaInterfaceOpticalBandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceOpticalBandType.setStatus("current")
_EdfaInterfacePumpLaserTxState_Type = TxState
_EdfaInterfacePumpLaserTxState_Object = MibTableColumn
edfaInterfacePumpLaserTxState = _EdfaInterfacePumpLaserTxState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 3),
    _EdfaInterfacePumpLaserTxState_Type()
)
edfaInterfacePumpLaserTxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserTxState.setStatus("current")
_EdfaInterfaceOpticalInputPower_Type = Integer32
_EdfaInterfaceOpticalInputPower_Object = MibTableColumn
edfaInterfaceOpticalInputPower = _EdfaInterfaceOpticalInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 4),
    _EdfaInterfaceOpticalInputPower_Type()
)
edfaInterfaceOpticalInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceOpticalInputPower.setStatus("current")
_EdfaInterfaceOpticalOutputPower_Type = Integer32
_EdfaInterfaceOpticalOutputPower_Object = MibTableColumn
edfaInterfaceOpticalOutputPower = _EdfaInterfaceOpticalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 5),
    _EdfaInterfaceOpticalOutputPower_Type()
)
edfaInterfaceOpticalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceOpticalOutputPower.setStatus("current")


class _EdfaInterfaceSubModuleTemp_Type(Integer32):
    """Custom type edfaInterfaceSubModuleTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 83),
    )


_EdfaInterfaceSubModuleTemp_Type.__name__ = "Integer32"
_EdfaInterfaceSubModuleTemp_Object = MibTableColumn
edfaInterfaceSubModuleTemp = _EdfaInterfaceSubModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 6),
    _EdfaInterfaceSubModuleTemp_Type()
)
edfaInterfaceSubModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceSubModuleTemp.setStatus("current")
_EdfaInterfacePumpLaserPower_Type = Integer32
_EdfaInterfacePumpLaserPower_Object = MibTableColumn
edfaInterfacePumpLaserPower = _EdfaInterfacePumpLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 7),
    _EdfaInterfacePumpLaserPower_Type()
)
edfaInterfacePumpLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserPower.setStatus("current")
_EdfaInterfacePumpLaserCurrent_Type = Integer32
_EdfaInterfacePumpLaserCurrent_Object = MibTableColumn
edfaInterfacePumpLaserCurrent = _EdfaInterfacePumpLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 8),
    _EdfaInterfacePumpLaserCurrent_Type()
)
edfaInterfacePumpLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserCurrent.setStatus("current")


class _EdfaInterfacePumpLaserTxTemp_Type(Integer32):
    """Custom type edfaInterfacePumpLaserTxTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -999),
        ValueRangeConstraint(200, 300),
    )


_EdfaInterfacePumpLaserTxTemp_Type.__name__ = "Integer32"
_EdfaInterfacePumpLaserTxTemp_Object = MibTableColumn
edfaInterfacePumpLaserTxTemp = _EdfaInterfacePumpLaserTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 9),
    _EdfaInterfacePumpLaserTxTemp_Type()
)
edfaInterfacePumpLaserTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserTxTemp.setStatus("current")


class _EdfaInterfacePumpLaserConfig_Type(Integer32):
    """Custom type edfaInterfacePumpLaserConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -999),
        ValueRangeConstraint(0, 100),
    )


_EdfaInterfacePumpLaserConfig_Type.__name__ = "Integer32"
_EdfaInterfacePumpLaserConfig_Object = MibTableColumn
edfaInterfacePumpLaserConfig = _EdfaInterfacePumpLaserConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 10),
    _EdfaInterfacePumpLaserConfig_Type()
)
edfaInterfacePumpLaserConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserConfig.setStatus("current")


class _EdfaInterfaceTECCurrent_Type(Integer32):
    """Custom type edfaInterfaceTECCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -999),
        ValueRangeConstraint(0, 2000),
    )


_EdfaInterfaceTECCurrent_Type.__name__ = "Integer32"
_EdfaInterfaceTECCurrent_Object = MibTableColumn
edfaInterfaceTECCurrent = _EdfaInterfaceTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 11),
    _EdfaInterfaceTECCurrent_Type()
)
edfaInterfaceTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceTECCurrent.setStatus("current")


class _EdfaInterfaceMaxOperPower_Type(Integer32):
    """Custom type edfaInterfaceMaxOperPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -999),
        ValueRangeConstraint(0, 255),
    )


_EdfaInterfaceMaxOperPower_Type.__name__ = "Integer32"
_EdfaInterfaceMaxOperPower_Object = MibTableColumn
edfaInterfaceMaxOperPower = _EdfaInterfaceMaxOperPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 12),
    _EdfaInterfaceMaxOperPower_Type()
)
edfaInterfaceMaxOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceMaxOperPower.setStatus("current")


class _EdfaInterfaceType_Type(Integer32):
    """Custom type edfaInterfaceType based on Integer32"""
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
        *(("notApplicable", 1),
          ("singleStage", 2),
          ("firstStage", 3),
          ("secondStage", 4))
    )


_EdfaInterfaceType_Type.__name__ = "Integer32"
_EdfaInterfaceType_Object = MibTableColumn
edfaInterfaceType = _EdfaInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 3, 1, 14),
    _EdfaInterfaceType_Type()
)
edfaInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceType.setStatus("current")
_SonetSectionTraceTable_Object = MibTable
sonetSectionTraceTable = _SonetSectionTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    sonetSectionTraceTable.setStatus("current")
_SonetSectionTraceEntry_Object = MibTableRow
sonetSectionTraceEntry = _SonetSectionTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 4, 1)
)
sonetSectionTraceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetSectionTraceEntry.setStatus("current")


class _SonetSectionTraceToExpect_Type(OctetString):
    """Custom type sonetSectionTraceToExpect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_SonetSectionTraceToExpect_Type.__name__ = "OctetString"
_SonetSectionTraceToExpect_Object = MibTableColumn
sonetSectionTraceToExpect = _SonetSectionTraceToExpect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 4, 1, 1),
    _SonetSectionTraceToExpect_Type()
)
sonetSectionTraceToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionTraceToExpect.setStatus("current")


class _SonetSectionTraceReceived_Type(OctetString):
    """Custom type sonetSectionTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_SonetSectionTraceReceived_Type.__name__ = "OctetString"
_SonetSectionTraceReceived_Object = MibTableColumn
sonetSectionTraceReceived = _SonetSectionTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 4, 1, 2),
    _SonetSectionTraceReceived_Type()
)
sonetSectionTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionTraceReceived.setStatus("current")


class _SonetSectionTraceLength_Type(Integer32):
    """Custom type sonetSectionTraceLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(64, 64),
    )


_SonetSectionTraceLength_Type.__name__ = "Integer32"
_SonetSectionTraceLength_Object = MibTableColumn
sonetSectionTraceLength = _SonetSectionTraceLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 4, 1, 3),
    _SonetSectionTraceLength_Type()
)
sonetSectionTraceLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionTraceLength.setStatus("current")
_EccmInterfaceTable_Object = MibTable
eccmInterfaceTable = _EccmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    eccmInterfaceTable.setStatus("current")
_EccmInterfaceEntry_Object = MibTableRow
eccmInterfaceEntry = _EccmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 5, 1)
)
eccmInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eccmInterfaceEntry.setStatus("current")


class _EccmInterfaceIdentifier_Type(DisplayString):
    """Custom type eccmInterfaceIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EccmInterfaceIdentifier_Type.__name__ = "DisplayString"
_EccmInterfaceIdentifier_Object = MibTableColumn
eccmInterfaceIdentifier = _EccmInterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 5, 1, 1),
    _EccmInterfaceIdentifier_Type()
)
eccmInterfaceIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eccmInterfaceIdentifier.setStatus("current")
_EccmInterfaceSwitchState_Type = TxState
_EccmInterfaceSwitchState_Object = MibTableColumn
eccmInterfaceSwitchState = _EccmInterfaceSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 5, 1, 2),
    _EccmInterfaceSwitchState_Type()
)
eccmInterfaceSwitchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eccmInterfaceSwitchState.setStatus("current")


class _EccmInterfaceFspChannelNo_Type(Integer32):
    """Custom type eccmInterfaceFspChannelNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EccmInterfaceFspChannelNo_Type.__name__ = "Integer32"
_EccmInterfaceFspChannelNo_Object = MibTableColumn
eccmInterfaceFspChannelNo = _EccmInterfaceFspChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 5, 1, 3),
    _EccmInterfaceFspChannelNo_Type()
)
eccmInterfaceFspChannelNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eccmInterfaceFspChannelNo.setStatus("current")


class _EccmInterfaceWavelength_Type(DisplayString):
    """Custom type eccmInterfaceWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EccmInterfaceWavelength_Type.__name__ = "DisplayString"
_EccmInterfaceWavelength_Object = MibTableColumn
eccmInterfaceWavelength = _EccmInterfaceWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 5, 1, 4),
    _EccmInterfaceWavelength_Type()
)
eccmInterfaceWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmInterfaceWavelength.setStatus("current")
_EccmInterfaceOIP_Type = Integer32
_EccmInterfaceOIP_Object = MibTableColumn
eccmInterfaceOIP = _EccmInterfaceOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 5, 1, 5),
    _EccmInterfaceOIP_Type()
)
eccmInterfaceOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmInterfaceOIP.setStatus("current")
_ApsInterfaceTable_Object = MibTable
apsInterfaceTable = _ApsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    apsInterfaceTable.setStatus("current")
_ApsInterfaceEntry_Object = MibTableRow
apsInterfaceEntry = _ApsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 6, 1)
)
apsInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apsInterfaceEntry.setStatus("current")
_ApsInterfaceSwitchState_Type = TxState
_ApsInterfaceSwitchState_Object = MibTableColumn
apsInterfaceSwitchState = _ApsInterfaceSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 6, 1, 1),
    _ApsInterfaceSwitchState_Type()
)
apsInterfaceSwitchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsInterfaceSwitchState.setStatus("current")
_ApsInterfaceOIPLoad_Type = Integer32
_ApsInterfaceOIPLoad_Object = MibTableColumn
apsInterfaceOIPLoad = _ApsInterfaceOIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 6, 1, 2),
    _ApsInterfaceOIPLoad_Type()
)
apsInterfaceOIPLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsInterfaceOIPLoad.setStatus("current")
_ApsInterfaceOipOsc_Type = Integer32
_ApsInterfaceOipOsc_Object = MibTableColumn
apsInterfaceOipOsc = _ApsInterfaceOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 1, 6, 1, 3),
    _ApsInterfaceOipOsc_Type()
)
apsInterfaceOipOsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsInterfaceOipOsc.setStatus("current")
_EquipmentConfiguration_ObjectIdentity = ObjectIdentity
equipmentConfiguration = _EquipmentConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")


class _ModuleVoltage_Type(Integer32):
    """Custom type moduleVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4500, 5500),
    )


_ModuleVoltage_Type.__name__ = "Integer32"
_ModuleVoltage_Object = MibTableColumn
moduleVoltage = _ModuleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 1),
    _ModuleVoltage_Type()
)
moduleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltage.setStatus("current")


class _ModuleEnvironmentTemp_Type(Integer32):
    """Custom type moduleEnvironmentTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_ModuleEnvironmentTemp_Type.__name__ = "Integer32"
_ModuleEnvironmentTemp_Object = MibTableColumn
moduleEnvironmentTemp = _ModuleEnvironmentTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 2),
    _ModuleEnvironmentTemp_Type()
)
moduleEnvironmentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEnvironmentTemp.setStatus("current")
_ModuleEnvironmentTempMax_Type = Integer32
_ModuleEnvironmentTempMax_Object = MibTableColumn
moduleEnvironmentTempMax = _ModuleEnvironmentTempMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 3),
    _ModuleEnvironmentTempMax_Type()
)
moduleEnvironmentTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEnvironmentTempMax.setStatus("deprecated")


class _ModuleSupervisionState_Type(Integer32):
    """Custom type moduleSupervisionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("notifying", 2)
    )


_ModuleSupervisionState_Type.__name__ = "Integer32"
_ModuleSupervisionState_Object = MibTableColumn
moduleSupervisionState = _ModuleSupervisionState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 4),
    _ModuleSupervisionState_Type()
)
moduleSupervisionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSupervisionState.setStatus("current")


class _ModuleProtectionGroupIndex_Type(Integer32):
    """Custom type moduleProtectionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_ModuleProtectionGroupIndex_Type.__name__ = "Integer32"
_ModuleProtectionGroupIndex_Object = MibTableColumn
moduleProtectionGroupIndex = _ModuleProtectionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 5),
    _ModuleProtectionGroupIndex_Type()
)
moduleProtectionGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleProtectionGroupIndex.setStatus("current")


class _ModuleCardType_Type(Integer32):
    """Custom type moduleCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleCardType_Type.__name__ = "Integer32"
_ModuleCardType_Object = MibTableColumn
moduleCardType = _ModuleCardType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 6),
    _ModuleCardType_Type()
)
moduleCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCardType.setStatus("current")
_ModuleVoltageMax_Type = Integer32
_ModuleVoltageMax_Object = MibTableColumn
moduleVoltageMax = _ModuleVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 7),
    _ModuleVoltageMax_Type()
)
moduleVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltageMax.setStatus("deprecated")
_ModuleVoltageMin_Type = Integer32
_ModuleVoltageMin_Object = MibTableColumn
moduleVoltageMin = _ModuleVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 8),
    _ModuleVoltageMin_Type()
)
moduleVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltageMin.setStatus("deprecated")


class _ModuleCardMode_Type(Integer32):
    """Custom type moduleCardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noMode", 1),
          ("transponder", 2),
          ("regenerator", 3))
    )


_ModuleCardMode_Type.__name__ = "Integer32"
_ModuleCardMode_Object = MibTableColumn
moduleCardMode = _ModuleCardMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 9),
    _ModuleCardMode_Type()
)
moduleCardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleCardMode.setStatus("current")


class _ModuleSignalFormat_Type(Integer32):
    """Custom type moduleSignalFormat based on Integer32"""
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
        *(("notRelevantForModule", 1),
          ("sdh", 2),
          ("sonet", 3),
          ("transparent", 4),
          ("sdhOrSonet", 5))
    )


_ModuleSignalFormat_Type.__name__ = "Integer32"
_ModuleSignalFormat_Object = MibTableColumn
moduleSignalFormat = _ModuleSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 10),
    _ModuleSignalFormat_Type()
)
moduleSignalFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSignalFormat.setStatus("current")
_ModuleSdhSonetALSMode_Type = AlsMode
_ModuleSdhSonetALSMode_Object = MibTableColumn
moduleSdhSonetALSMode = _ModuleSdhSonetALSMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 11),
    _ModuleSdhSonetALSMode_Type()
)
moduleSdhSonetALSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSdhSonetALSMode.setStatus("current")
_ModuleSdhSonetAISGeneration_Type = AisState
_ModuleSdhSonetAISGeneration_Object = MibTableColumn
moduleSdhSonetAISGeneration = _ModuleSdhSonetAISGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 12),
    _ModuleSdhSonetAISGeneration_Type()
)
moduleSdhSonetAISGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSdhSonetAISGeneration.setStatus("current")
_ModuleCouplingLinkMode_Type = EnableState
_ModuleCouplingLinkMode_Object = MibTableColumn
moduleCouplingLinkMode = _ModuleCouplingLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 13),
    _ModuleCouplingLinkMode_Type()
)
moduleCouplingLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCouplingLinkMode.setStatus("current")
_ModuleFeederMode_Type = OnOff
_ModuleFeederMode_Object = MibTableColumn
moduleFeederMode = _ModuleFeederMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 14),
    _ModuleFeederMode_Type()
)
moduleFeederMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleFeederMode.setStatus("current")


class _ModuleSdhSonetThresholds_Type(Integer32):
    """Custom type moduleSdhSonetThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2),
          ("setToDefault", 3))
    )


_ModuleSdhSonetThresholds_Type.__name__ = "Integer32"
_ModuleSdhSonetThresholds_Object = MibTableColumn
moduleSdhSonetThresholds = _ModuleSdhSonetThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 1, 1, 15),
    _ModuleSdhSonetThresholds_Type()
)
moduleSdhSonetThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSdhSonetThresholds.setStatus("current")
_TelemetryModuleTable_Object = MibTable
telemetryModuleTable = _TelemetryModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    telemetryModuleTable.setStatus("current")
_TelemetryModuleEntry_Object = MibTableRow
telemetryModuleEntry = _TelemetryModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 2, 1)
)
telemetryModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "telemetryExtOutputIndex"),
)
if mibBuilder.loadTexts:
    telemetryModuleEntry.setStatus("current")


class _TelemetryExtOutputIndex_Type(Integer32):
    """Custom type telemetryExtOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TelemetryExtOutputIndex_Type.__name__ = "Integer32"
_TelemetryExtOutputIndex_Object = MibTableColumn
telemetryExtOutputIndex = _TelemetryExtOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 2, 1, 1),
    _TelemetryExtOutputIndex_Type()
)
telemetryExtOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    telemetryExtOutputIndex.setStatus("current")
_TelemetryExtOutputState_Type = OnOff
_TelemetryExtOutputState_Object = MibTableColumn
telemetryExtOutputState = _TelemetryExtOutputState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 2, 1, 2),
    _TelemetryExtOutputState_Type()
)
telemetryExtOutputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telemetryExtOutputState.setStatus("current")


class _TelemetryExtOutputIdentifier_Type(DisplayString):
    """Custom type telemetryExtOutputIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TelemetryExtOutputIdentifier_Type.__name__ = "DisplayString"
_TelemetryExtOutputIdentifier_Object = MibTableColumn
telemetryExtOutputIdentifier = _TelemetryExtOutputIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 2, 1, 3),
    _TelemetryExtOutputIdentifier_Type()
)
telemetryExtOutputIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telemetryExtOutputIdentifier.setStatus("current")
_ChannelCardProtectionTable_Object = MibTable
channelCardProtectionTable = _ChannelCardProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    channelCardProtectionTable.setStatus("current")
_ChannelCardProtectionEntry_Object = MibTableRow
channelCardProtectionEntry = _ChannelCardProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1)
)
channelCardProtectionEntry.setIndexNames(
    (0, "FSP3000-MIB", "channelCardProtectionGroupIndex"),
)
if mibBuilder.loadTexts:
    channelCardProtectionEntry.setStatus("current")


class _ChannelCardProtectionGroupIndex_Type(Integer32):
    """Custom type channelCardProtectionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_ChannelCardProtectionGroupIndex_Type.__name__ = "Integer32"
_ChannelCardProtectionGroupIndex_Object = MibTableColumn
channelCardProtectionGroupIndex = _ChannelCardProtectionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 1),
    _ChannelCardProtectionGroupIndex_Type()
)
channelCardProtectionGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCardProtectionGroupIndex.setStatus("current")
_ChannelCardProtectionWestSlot_Type = PhysicalIndex
_ChannelCardProtectionWestSlot_Object = MibTableColumn
channelCardProtectionWestSlot = _ChannelCardProtectionWestSlot_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 2),
    _ChannelCardProtectionWestSlot_Type()
)
channelCardProtectionWestSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCardProtectionWestSlot.setStatus("current")
_ChannelCardProtectionEastSlot_Type = PhysicalIndex
_ChannelCardProtectionEastSlot_Object = MibTableColumn
channelCardProtectionEastSlot = _ChannelCardProtectionEastSlot_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 3),
    _ChannelCardProtectionEastSlot_Type()
)
channelCardProtectionEastSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCardProtectionEastSlot.setStatus("current")
_ChannelCardProtectionLastRequest_Type = ProtectionCommand
_ChannelCardProtectionLastRequest_Object = MibTableColumn
channelCardProtectionLastRequest = _ChannelCardProtectionLastRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 4),
    _ChannelCardProtectionLastRequest_Type()
)
channelCardProtectionLastRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCardProtectionLastRequest.setStatus("current")
_ChannelCardProtectionSwitchMode_Type = ProtectionSwitchMode
_ChannelCardProtectionSwitchMode_Object = MibTableColumn
channelCardProtectionSwitchMode = _ChannelCardProtectionSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 5),
    _ChannelCardProtectionSwitchMode_Type()
)
channelCardProtectionSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCardProtectionSwitchMode.setStatus("current")
_ChannelCardProtectionState_Type = ProtectionState
_ChannelCardProtectionState_Object = MibTableColumn
channelCardProtectionState = _ChannelCardProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 6),
    _ChannelCardProtectionState_Type()
)
channelCardProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCardProtectionState.setStatus("current")


class _ChannelCardProtectionGroupStatus_Type(Integer32):
    """Custom type channelCardProtectionGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2),
          ("mismatch", 3))
    )


_ChannelCardProtectionGroupStatus_Type.__name__ = "Integer32"
_ChannelCardProtectionGroupStatus_Object = MibTableColumn
channelCardProtectionGroupStatus = _ChannelCardProtectionGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 7),
    _ChannelCardProtectionGroupStatus_Type()
)
channelCardProtectionGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCardProtectionGroupStatus.setStatus("current")


class _ChannelCardProtectionConfWorkingSlot_Type(Integer32):
    """Custom type channelCardProtectionConfWorkingSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("west", 1),
          ("east", 2))
    )


_ChannelCardProtectionConfWorkingSlot_Type.__name__ = "Integer32"
_ChannelCardProtectionConfWorkingSlot_Object = MibTableColumn
channelCardProtectionConfWorkingSlot = _ChannelCardProtectionConfWorkingSlot_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 8),
    _ChannelCardProtectionConfWorkingSlot_Type()
)
channelCardProtectionConfWorkingSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCardProtectionConfWorkingSlot.setStatus("current")
_ChannelCardProtectionSDswitching_Type = AlarmSwitching
_ChannelCardProtectionSDswitching_Object = MibTableColumn
channelCardProtectionSDswitching = _ChannelCardProtectionSDswitching_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 9),
    _ChannelCardProtectionSDswitching_Type()
)
channelCardProtectionSDswitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCardProtectionSDswitching.setStatus("current")
_ChannelCardProtectionSonetSdhSwitching_Type = AlarmSwitching
_ChannelCardProtectionSonetSdhSwitching_Object = MibTableColumn
channelCardProtectionSonetSdhSwitching = _ChannelCardProtectionSonetSdhSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 10),
    _ChannelCardProtectionSonetSdhSwitching_Type()
)
channelCardProtectionSonetSdhSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCardProtectionSonetSdhSwitching.setStatus("current")
_ChannelCardProtectionSwitchHoldOffTime_Type = Integer32
_ChannelCardProtectionSwitchHoldOffTime_Object = MibTableColumn
channelCardProtectionSwitchHoldOffTime = _ChannelCardProtectionSwitchHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 11),
    _ChannelCardProtectionSwitchHoldOffTime_Type()
)
channelCardProtectionSwitchHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCardProtectionSwitchHoldOffTime.setStatus("current")
_ChannelCardProtectionDualEndedSwitching_Type = AlarmSwitching
_ChannelCardProtectionDualEndedSwitching_Object = MibTableColumn
channelCardProtectionDualEndedSwitching = _ChannelCardProtectionDualEndedSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 3, 1, 12),
    _ChannelCardProtectionDualEndedSwitching_Type()
)
channelCardProtectionDualEndedSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCardProtectionDualEndedSwitching.setStatus("current")
_RemoteOpticalSwitchTable_Object = MibTable
remoteOpticalSwitchTable = _RemoteOpticalSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    remoteOpticalSwitchTable.setStatus("current")
_RemoteOpticalSwitchEntry_Object = MibTableRow
remoteOpticalSwitchEntry = _RemoteOpticalSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4, 1)
)
remoteOpticalSwitchEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    remoteOpticalSwitchEntry.setStatus("current")


class _RemoteOpticalSwitchActiveLine_Type(Integer32):
    """Custom type remoteOpticalSwitchActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineA", 1),
          ("lineB", 2))
    )


_RemoteOpticalSwitchActiveLine_Type.__name__ = "Integer32"
_RemoteOpticalSwitchActiveLine_Object = MibTableColumn
remoteOpticalSwitchActiveLine = _RemoteOpticalSwitchActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4, 1, 1),
    _RemoteOpticalSwitchActiveLine_Type()
)
remoteOpticalSwitchActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOpticalSwitchActiveLine.setStatus("current")


class _RemoteOpticalSwitchMode_Type(Integer32):
    """Custom type remoteOpticalSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("locked", 2))
    )


_RemoteOpticalSwitchMode_Type.__name__ = "Integer32"
_RemoteOpticalSwitchMode_Object = MibTableColumn
remoteOpticalSwitchMode = _RemoteOpticalSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4, 1, 2),
    _RemoteOpticalSwitchMode_Type()
)
remoteOpticalSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOpticalSwitchMode.setStatus("current")
_RemoteOpticalSwitchLastRequest_Type = SwitchCommand
_RemoteOpticalSwitchLastRequest_Object = MibTableColumn
remoteOpticalSwitchLastRequest = _RemoteOpticalSwitchLastRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4, 1, 3),
    _RemoteOpticalSwitchLastRequest_Type()
)
remoteOpticalSwitchLastRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteOpticalSwitchLastRequest.setStatus("current")
_RemoteOpticalSwitchRefLaserState_Type = OnOff
_RemoteOpticalSwitchRefLaserState_Object = MibTableColumn
remoteOpticalSwitchRefLaserState = _RemoteOpticalSwitchRefLaserState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4, 1, 4),
    _RemoteOpticalSwitchRefLaserState_Type()
)
remoteOpticalSwitchRefLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOpticalSwitchRefLaserState.setStatus("current")
_RemoteOpticalSwitchLineAState_Type = AvailState
_RemoteOpticalSwitchLineAState_Object = MibTableColumn
remoteOpticalSwitchLineAState = _RemoteOpticalSwitchLineAState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4, 1, 5),
    _RemoteOpticalSwitchLineAState_Type()
)
remoteOpticalSwitchLineAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOpticalSwitchLineAState.setStatus("current")
_RemoteOpticalSwitchLineBState_Type = AvailState
_RemoteOpticalSwitchLineBState_Object = MibTableColumn
remoteOpticalSwitchLineBState = _RemoteOpticalSwitchLineBState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4, 1, 6),
    _RemoteOpticalSwitchLineBState_Type()
)
remoteOpticalSwitchLineBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOpticalSwitchLineBState.setStatus("current")


class _RemoteOpticalSwitchTxBias_Type(Integer32):
    """Custom type remoteOpticalSwitchTxBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_RemoteOpticalSwitchTxBias_Type.__name__ = "Integer32"
_RemoteOpticalSwitchTxBias_Object = MibTableColumn
remoteOpticalSwitchTxBias = _RemoteOpticalSwitchTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 4, 1, 7),
    _RemoteOpticalSwitchTxBias_Type()
)
remoteOpticalSwitchTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOpticalSwitchTxBias.setStatus("current")
_TelemetryModuleInputTable_Object = MibTable
telemetryModuleInputTable = _TelemetryModuleInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    telemetryModuleInputTable.setStatus("current")
_TelemetryModuleInputEntry_Object = MibTableRow
telemetryModuleInputEntry = _TelemetryModuleInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 5, 1)
)
telemetryModuleInputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "telemetryExtInputIndex"),
)
if mibBuilder.loadTexts:
    telemetryModuleInputEntry.setStatus("current")


class _TelemetryExtInputIndex_Type(Integer32):
    """Custom type telemetryExtInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TelemetryExtInputIndex_Type.__name__ = "Integer32"
_TelemetryExtInputIndex_Object = MibTableColumn
telemetryExtInputIndex = _TelemetryExtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 5, 1, 1),
    _TelemetryExtInputIndex_Type()
)
telemetryExtInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    telemetryExtInputIndex.setStatus("current")


class _TelemetryExtInputIdentifier_Type(DisplayString):
    """Custom type telemetryExtInputIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TelemetryExtInputIdentifier_Type.__name__ = "DisplayString"
_TelemetryExtInputIdentifier_Object = MibTableColumn
telemetryExtInputIdentifier = _TelemetryExtInputIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 5, 1, 2),
    _TelemetryExtInputIdentifier_Type()
)
telemetryExtInputIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telemetryExtInputIdentifier.setStatus("current")
_FilterModuleTable_Object = MibTable
filterModuleTable = _FilterModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    filterModuleTable.setStatus("current")
_FilterModuleEntry_Object = MibTableRow
filterModuleEntry = _FilterModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 6, 1)
)
filterModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    filterModuleEntry.setStatus("current")
_FilterModuleChannelRange_Type = ChannelRange
_FilterModuleChannelRange_Object = MibTableColumn
filterModuleChannelRange = _FilterModuleChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 6, 1, 1),
    _FilterModuleChannelRange_Type()
)
filterModuleChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterModuleChannelRange.setStatus("current")


class _FilterModuleChannel_Type(Integer32):
    """Custom type filterModuleChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FilterModuleChannel_Type.__name__ = "Integer32"
_FilterModuleChannel_Object = MibTableColumn
filterModuleChannel = _FilterModuleChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 6, 1, 2),
    _FilterModuleChannel_Type()
)
filterModuleChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterModuleChannel.setStatus("current")
_OscmTable_Object = MibTable
oscmTable = _OscmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 7)
)
if mibBuilder.loadTexts:
    oscmTable.setStatus("current")
_OscmEntry_Object = MibTableRow
oscmEntry = _OscmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 7, 1)
)
oscmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    oscmEntry.setStatus("current")
_OscmTopologyMode_Type = OscmTopologyMode
_OscmTopologyMode_Object = MibTableColumn
oscmTopologyMode = _OscmTopologyMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 7, 1, 1),
    _OscmTopologyMode_Type()
)
oscmTopologyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscmTopologyMode.setStatus("current")
_OscmBranchMode_Type = OscmBranchMode
_OscmBranchMode_Object = MibTableColumn
oscmBranchMode = _OscmBranchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 7, 1, 2),
    _OscmBranchMode_Type()
)
oscmBranchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscmBranchMode.setStatus("current")


class _OscmActiveProtectionLine_Type(Integer32):
    """Custom type oscmActiveProtectionLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineNotAppl", 1),
          ("lineEast", 2),
          ("lineWest", 3))
    )


_OscmActiveProtectionLine_Type.__name__ = "Integer32"
_OscmActiveProtectionLine_Object = MibTableColumn
oscmActiveProtectionLine = _OscmActiveProtectionLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 7, 1, 3),
    _OscmActiveProtectionLine_Type()
)
oscmActiveProtectionLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscmActiveProtectionLine.setStatus("current")


class _OscmSwitchLastRequest_Type(Integer32):
    """Custom type oscmSwitchLastRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("swNone", 1),
          ("swManualToEast", 2),
          ("swManualToWest", 3))
    )


_OscmSwitchLastRequest_Type.__name__ = "Integer32"
_OscmSwitchLastRequest_Object = MibTableColumn
oscmSwitchLastRequest = _OscmSwitchLastRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 4, 2, 7, 1, 4),
    _OscmSwitchLastRequest_Type()
)
oscmSwitchLastRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscmSwitchLastRequest.setStatus("current")
_PerformanceMIB_ObjectIdentity = ObjectIdentity
performanceMIB = _PerformanceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5)
)
_PerformanceAdmin_ObjectIdentity = ObjectIdentity
performanceAdmin = _PerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1)
)
_SonetPerformanceAdmin_ObjectIdentity = ObjectIdentity
sonetPerformanceAdmin = _SonetPerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1)
)
_SonetSdhPerformanceAdmin_ObjectIdentity = ObjectIdentity
sonetSdhPerformanceAdmin = _SonetSdhPerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1)
)
_SonetSdhThresholdTable_Object = MibTable
sonetSdhThresholdTable = _SonetSdhThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sonetSdhThresholdTable.setStatus("current")
_SonetSdhThresholdEntry_Object = MibTableRow
sonetSdhThresholdEntry = _SonetSdhThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 1, 1)
)
sonetSdhThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sonetSdhThresholdEntry.setStatus("current")


class _SonetSdhThresholdType_Type(Integer32):
    """Custom type sonetSdhThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              1,
              2,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -255),
          ("otherBitErrorCounting", 1),
          ("bellcore1991", 2),
          ("itu", 4),
          ("ansi1997", 5),
          ("otherBlockErrorCounting", 255))
    )


_SonetSdhThresholdType_Type.__name__ = "Integer32"
_SonetSdhThresholdType_Object = MibTableColumn
sonetSdhThresholdType = _SonetSdhThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 1, 1, 1),
    _SonetSdhThresholdType_Type()
)
sonetSdhThresholdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSdhThresholdType.setStatus("current")


class _SonetSdhThresholdSESValue_Type(Integer32):
    """Custom type sonetSdhThresholdSESValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_SonetSdhThresholdSESValue_Type.__name__ = "Integer32"
_SonetSdhThresholdSESValue_Object = MibTableColumn
sonetSdhThresholdSESValue = _SonetSdhThresholdSESValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 1, 1, 2),
    _SonetSdhThresholdSESValue_Type()
)
sonetSdhThresholdSESValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSdhThresholdSESValue.setStatus("current")
_SectionQoSThresholdTable_Object = MibTable
sectionQoSThresholdTable = _SectionQoSThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sectionQoSThresholdTable.setStatus("current")
_SectionQoSThresholdEntry_Object = MibTableRow
sectionQoSThresholdEntry = _SectionQoSThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 2, 1)
)
sectionQoSThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "sectionQoSThresholdType"),
)
if mibBuilder.loadTexts:
    sectionQoSThresholdEntry.setStatus("current")
_SectionQoSThresholdType_Type = SectionType
_SectionQoSThresholdType_Object = MibTableColumn
sectionQoSThresholdType = _SectionQoSThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 2, 1, 1),
    _SectionQoSThresholdType_Type()
)
sectionQoSThresholdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sectionQoSThresholdType.setStatus("current")
_SectionQoSThreshold15minState_Type = EnableState
_SectionQoSThreshold15minState_Object = MibTableColumn
sectionQoSThreshold15minState = _SectionQoSThreshold15minState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 2, 1, 2),
    _SectionQoSThreshold15minState_Type()
)
sectionQoSThreshold15minState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sectionQoSThreshold15minState.setStatus("current")
_SectionQoSThreshold15minHigh_Type = Unsigned32
_SectionQoSThreshold15minHigh_Object = MibTableColumn
sectionQoSThreshold15minHigh = _SectionQoSThreshold15minHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 2, 1, 3),
    _SectionQoSThreshold15minHigh_Type()
)
sectionQoSThreshold15minHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sectionQoSThreshold15minHigh.setStatus("current")
_SectionQoSThreshold15minLow_Type = Unsigned32
_SectionQoSThreshold15minLow_Object = MibTableColumn
sectionQoSThreshold15minLow = _SectionQoSThreshold15minLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 2, 1, 4),
    _SectionQoSThreshold15minLow_Type()
)
sectionQoSThreshold15minLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sectionQoSThreshold15minLow.setStatus("current")
_SectionQoSThreshold24hrState_Type = EnableState
_SectionQoSThreshold24hrState_Object = MibTableColumn
sectionQoSThreshold24hrState = _SectionQoSThreshold24hrState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 2, 1, 5),
    _SectionQoSThreshold24hrState_Type()
)
sectionQoSThreshold24hrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sectionQoSThreshold24hrState.setStatus("current")
_SectionQoSThreshold24hrHigh_Type = Unsigned32
_SectionQoSThreshold24hrHigh_Object = MibTableColumn
sectionQoSThreshold24hrHigh = _SectionQoSThreshold24hrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 2, 1, 6),
    _SectionQoSThreshold24hrHigh_Type()
)
sectionQoSThreshold24hrHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sectionQoSThreshold24hrHigh.setStatus("current")
_PathQoSThresholdTable_Object = MibTable
pathQoSThresholdTable = _PathQoSThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pathQoSThresholdTable.setStatus("current")
_PathQoSThresholdEntry_Object = MibTableRow
pathQoSThresholdEntry = _PathQoSThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 3, 1)
)
pathQoSThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "pathQoSThresholdType"),
)
if mibBuilder.loadTexts:
    pathQoSThresholdEntry.setStatus("current")
_PathQoSThresholdType_Type = PathType
_PathQoSThresholdType_Object = MibTableColumn
pathQoSThresholdType = _PathQoSThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 3, 1, 1),
    _PathQoSThresholdType_Type()
)
pathQoSThresholdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pathQoSThresholdType.setStatus("current")
_PathQoSThreshold15minState_Type = EnableState
_PathQoSThreshold15minState_Object = MibTableColumn
pathQoSThreshold15minState = _PathQoSThreshold15minState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 3, 1, 2),
    _PathQoSThreshold15minState_Type()
)
pathQoSThreshold15minState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathQoSThreshold15minState.setStatus("current")
_PathQoSThreshold15minHigh_Type = Unsigned32
_PathQoSThreshold15minHigh_Object = MibTableColumn
pathQoSThreshold15minHigh = _PathQoSThreshold15minHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 3, 1, 3),
    _PathQoSThreshold15minHigh_Type()
)
pathQoSThreshold15minHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathQoSThreshold15minHigh.setStatus("current")
_PathQoSThreshold15minLow_Type = Unsigned32
_PathQoSThreshold15minLow_Object = MibTableColumn
pathQoSThreshold15minLow = _PathQoSThreshold15minLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 3, 1, 4),
    _PathQoSThreshold15minLow_Type()
)
pathQoSThreshold15minLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathQoSThreshold15minLow.setStatus("current")
_PathQoSThreshold24hrState_Type = EnableState
_PathQoSThreshold24hrState_Object = MibTableColumn
pathQoSThreshold24hrState = _PathQoSThreshold24hrState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 3, 1, 5),
    _PathQoSThreshold24hrState_Type()
)
pathQoSThreshold24hrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathQoSThreshold24hrState.setStatus("current")
_PathQoSThreshold24hrHigh_Type = Unsigned32
_PathQoSThreshold24hrHigh_Object = MibTableColumn
pathQoSThreshold24hrHigh = _PathQoSThreshold24hrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 1, 1, 3, 1, 6),
    _PathQoSThreshold24hrHigh_Type()
)
pathQoSThreshold24hrHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathQoSThreshold24hrHigh.setStatus("current")
_PhysicalPerformanceAdmin_ObjectIdentity = ObjectIdentity
physicalPerformanceAdmin = _PhysicalPerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2)
)
_ModulePPthresholdTable_Object = MibTable
modulePPthresholdTable = _ModulePPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    modulePPthresholdTable.setStatus("current")
_ModulePPthresholdEntry_Object = MibTableRow
modulePPthresholdEntry = _ModulePPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1)
)
modulePPthresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    modulePPthresholdEntry.setStatus("current")
_ModulePPthresholdLowestVolt_Type = Integer32
_ModulePPthresholdLowestVolt_Object = MibTableColumn
modulePPthresholdLowestVolt = _ModulePPthresholdLowestVolt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 1),
    _ModulePPthresholdLowestVolt_Type()
)
modulePPthresholdLowestVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPthresholdLowestVolt.setStatus("current")
_ModulePPthresholdLowVolt_Type = Integer32
_ModulePPthresholdLowVolt_Object = MibTableColumn
modulePPthresholdLowVolt = _ModulePPthresholdLowVolt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 2),
    _ModulePPthresholdLowVolt_Type()
)
modulePPthresholdLowVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPthresholdLowVolt.setStatus("current")
_ModulePPthresholdHighVolt_Type = Integer32
_ModulePPthresholdHighVolt_Object = MibTableColumn
modulePPthresholdHighVolt = _ModulePPthresholdHighVolt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 3),
    _ModulePPthresholdHighVolt_Type()
)
modulePPthresholdHighVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPthresholdHighVolt.setStatus("current")
_ModulePPthresholdHighestVolt_Type = Integer32
_ModulePPthresholdHighestVolt_Object = MibTableColumn
modulePPthresholdHighestVolt = _ModulePPthresholdHighestVolt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 4),
    _ModulePPthresholdHighestVolt_Type()
)
modulePPthresholdHighestVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPthresholdHighestVolt.setStatus("current")
_ModulePPhysteresisVolt_Type = Integer32
_ModulePPhysteresisVolt_Object = MibTableColumn
modulePPhysteresisVolt = _ModulePPhysteresisVolt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 5),
    _ModulePPhysteresisVolt_Type()
)
modulePPhysteresisVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPhysteresisVolt.setStatus("current")
_ModulePPthresholdLowestTemp_Type = Integer32
_ModulePPthresholdLowestTemp_Object = MibTableColumn
modulePPthresholdLowestTemp = _ModulePPthresholdLowestTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 6),
    _ModulePPthresholdLowestTemp_Type()
)
modulePPthresholdLowestTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPthresholdLowestTemp.setStatus("current")
_ModulePPthresholdLowTemp_Type = Integer32
_ModulePPthresholdLowTemp_Object = MibTableColumn
modulePPthresholdLowTemp = _ModulePPthresholdLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 7),
    _ModulePPthresholdLowTemp_Type()
)
modulePPthresholdLowTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPthresholdLowTemp.setStatus("current")
_ModulePPthresholdHighTemp_Type = Integer32
_ModulePPthresholdHighTemp_Object = MibTableColumn
modulePPthresholdHighTemp = _ModulePPthresholdHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 8),
    _ModulePPthresholdHighTemp_Type()
)
modulePPthresholdHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPthresholdHighTemp.setStatus("current")
_ModulePPthresholdHighestTemp_Type = Integer32
_ModulePPthresholdHighestTemp_Object = MibTableColumn
modulePPthresholdHighestTemp = _ModulePPthresholdHighestTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 9),
    _ModulePPthresholdHighestTemp_Type()
)
modulePPthresholdHighestTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPthresholdHighestTemp.setStatus("current")
_ModulePPhysteresisTemp_Type = Integer32
_ModulePPhysteresisTemp_Object = MibTableColumn
modulePPhysteresisTemp = _ModulePPhysteresisTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 1, 1, 10),
    _ModulePPhysteresisTemp_Type()
)
modulePPhysteresisTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePPhysteresisTemp.setStatus("current")
_RemOptSwPPthresholdTable_Object = MibTable
remOptSwPPthresholdTable = _RemOptSwPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    remOptSwPPthresholdTable.setStatus("current")
_RemOptSwPPthresholdEntry_Object = MibTableRow
remOptSwPPthresholdEntry = _RemOptSwPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 2, 1)
)
remOptSwPPthresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    remOptSwPPthresholdEntry.setStatus("current")
_RemOptSwPPthresholdLowestTxBias_Type = Integer32
_RemOptSwPPthresholdLowestTxBias_Object = MibTableColumn
remOptSwPPthresholdLowestTxBias = _RemOptSwPPthresholdLowestTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 2, 1, 1),
    _RemOptSwPPthresholdLowestTxBias_Type()
)
remOptSwPPthresholdLowestTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remOptSwPPthresholdLowestTxBias.setStatus("current")
_RemOptSwPPthresholdLowTxBias_Type = Integer32
_RemOptSwPPthresholdLowTxBias_Object = MibTableColumn
remOptSwPPthresholdLowTxBias = _RemOptSwPPthresholdLowTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 2, 1, 2),
    _RemOptSwPPthresholdLowTxBias_Type()
)
remOptSwPPthresholdLowTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remOptSwPPthresholdLowTxBias.setStatus("current")
_RemOptSwPPthresholdHighTxBias_Type = Integer32
_RemOptSwPPthresholdHighTxBias_Object = MibTableColumn
remOptSwPPthresholdHighTxBias = _RemOptSwPPthresholdHighTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 2, 1, 3),
    _RemOptSwPPthresholdHighTxBias_Type()
)
remOptSwPPthresholdHighTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remOptSwPPthresholdHighTxBias.setStatus("current")
_RemOptSwPPthresholdHighestTxBias_Type = Integer32
_RemOptSwPPthresholdHighestTxBias_Object = MibTableColumn
remOptSwPPthresholdHighestTxBias = _RemOptSwPPthresholdHighestTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 2, 1, 4),
    _RemOptSwPPthresholdHighestTxBias_Type()
)
remOptSwPPthresholdHighestTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remOptSwPPthresholdHighestTxBias.setStatus("current")
_RemOptSwPPhysteresisTxBias_Type = Integer32
_RemOptSwPPhysteresisTxBias_Object = MibTableColumn
remOptSwPPhysteresisTxBias = _RemOptSwPPhysteresisTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 2, 1, 5),
    _RemOptSwPPhysteresisTxBias_Type()
)
remOptSwPPhysteresisTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remOptSwPPhysteresisTxBias.setStatus("current")
_EdfaPPthresholdTable_Object = MibTable
edfaPPthresholdTable = _EdfaPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    edfaPPthresholdTable.setStatus("current")
_EdfaPPthresholdEntry_Object = MibTableRow
edfaPPthresholdEntry = _EdfaPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1)
)
edfaPPthresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    edfaPPthresholdEntry.setStatus("current")
_EdfaPPthresholdLowestPumpCurrent_Type = Integer32
_EdfaPPthresholdLowestPumpCurrent_Object = MibTableColumn
edfaPPthresholdLowestPumpCurrent = _EdfaPPthresholdLowestPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 1),
    _EdfaPPthresholdLowestPumpCurrent_Type()
)
edfaPPthresholdLowestPumpCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdLowestPumpCurrent.setStatus("current")
_EdfaPPthresholdLowPumpCurrent_Type = Integer32
_EdfaPPthresholdLowPumpCurrent_Object = MibTableColumn
edfaPPthresholdLowPumpCurrent = _EdfaPPthresholdLowPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 2),
    _EdfaPPthresholdLowPumpCurrent_Type()
)
edfaPPthresholdLowPumpCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdLowPumpCurrent.setStatus("current")
_EdfaPPthresholdHighPumpCurrent_Type = Integer32
_EdfaPPthresholdHighPumpCurrent_Object = MibTableColumn
edfaPPthresholdHighPumpCurrent = _EdfaPPthresholdHighPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 3),
    _EdfaPPthresholdHighPumpCurrent_Type()
)
edfaPPthresholdHighPumpCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdHighPumpCurrent.setStatus("current")
_EdfaPPthresholdHighestPumpCurrent_Type = Integer32
_EdfaPPthresholdHighestPumpCurrent_Object = MibTableColumn
edfaPPthresholdHighestPumpCurrent = _EdfaPPthresholdHighestPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 4),
    _EdfaPPthresholdHighestPumpCurrent_Type()
)
edfaPPthresholdHighestPumpCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdHighestPumpCurrent.setStatus("current")
_EdfaPPhysteresisPumpCurrent_Type = Integer32
_EdfaPPhysteresisPumpCurrent_Object = MibTableColumn
edfaPPhysteresisPumpCurrent = _EdfaPPhysteresisPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 5),
    _EdfaPPhysteresisPumpCurrent_Type()
)
edfaPPhysteresisPumpCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPhysteresisPumpCurrent.setStatus("current")
_EdfaPPthresholdLowestOIP_Type = Integer32
_EdfaPPthresholdLowestOIP_Object = MibTableColumn
edfaPPthresholdLowestOIP = _EdfaPPthresholdLowestOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 6),
    _EdfaPPthresholdLowestOIP_Type()
)
edfaPPthresholdLowestOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdLowestOIP.setStatus("current")
_EdfaPPthresholdLowOIP_Type = Integer32
_EdfaPPthresholdLowOIP_Object = MibTableColumn
edfaPPthresholdLowOIP = _EdfaPPthresholdLowOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 7),
    _EdfaPPthresholdLowOIP_Type()
)
edfaPPthresholdLowOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdLowOIP.setStatus("current")
_EdfaPPthresholdHighOIP_Type = Integer32
_EdfaPPthresholdHighOIP_Object = MibTableColumn
edfaPPthresholdHighOIP = _EdfaPPthresholdHighOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 8),
    _EdfaPPthresholdHighOIP_Type()
)
edfaPPthresholdHighOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdHighOIP.setStatus("current")
_EdfaPPthresholdHighestOIP_Type = Integer32
_EdfaPPthresholdHighestOIP_Object = MibTableColumn
edfaPPthresholdHighestOIP = _EdfaPPthresholdHighestOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 9),
    _EdfaPPthresholdHighestOIP_Type()
)
edfaPPthresholdHighestOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdHighestOIP.setStatus("current")
_EdfaPPhysteresisOIP_Type = Integer32
_EdfaPPhysteresisOIP_Object = MibTableColumn
edfaPPhysteresisOIP = _EdfaPPhysteresisOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 10),
    _EdfaPPhysteresisOIP_Type()
)
edfaPPhysteresisOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPhysteresisOIP.setStatus("current")
_EdfaPPthresholdLowestOOP_Type = Integer32
_EdfaPPthresholdLowestOOP_Object = MibTableColumn
edfaPPthresholdLowestOOP = _EdfaPPthresholdLowestOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 11),
    _EdfaPPthresholdLowestOOP_Type()
)
edfaPPthresholdLowestOOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdLowestOOP.setStatus("current")
_EdfaPPthresholdLowOOP_Type = Integer32
_EdfaPPthresholdLowOOP_Object = MibTableColumn
edfaPPthresholdLowOOP = _EdfaPPthresholdLowOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 12),
    _EdfaPPthresholdLowOOP_Type()
)
edfaPPthresholdLowOOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdLowOOP.setStatus("current")
_EdfaPPthresholdHighOOP_Type = Integer32
_EdfaPPthresholdHighOOP_Object = MibTableColumn
edfaPPthresholdHighOOP = _EdfaPPthresholdHighOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 13),
    _EdfaPPthresholdHighOOP_Type()
)
edfaPPthresholdHighOOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdHighOOP.setStatus("current")
_EdfaPPthresholdHighestOOP_Type = Integer32
_EdfaPPthresholdHighestOOP_Object = MibTableColumn
edfaPPthresholdHighestOOP = _EdfaPPthresholdHighestOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 14),
    _EdfaPPthresholdHighestOOP_Type()
)
edfaPPthresholdHighestOOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdHighestOOP.setStatus("current")
_EdfaPPhysteresisOOP_Type = Integer32
_EdfaPPhysteresisOOP_Object = MibTableColumn
edfaPPhysteresisOOP = _EdfaPPhysteresisOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 3, 1, 15),
    _EdfaPPhysteresisOOP_Type()
)
edfaPPhysteresisOOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPhysteresisOOP.setStatus("current")
_InterfaceTTPPthresholdTable_Object = MibTable
interfaceTTPPthresholdTable = _InterfaceTTPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    interfaceTTPPthresholdTable.setStatus("current")
_InterfaceTTPPthresholdEntry_Object = MibTableRow
interfaceTTPPthresholdEntry = _InterfaceTTPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1)
)
interfaceTTPPthresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceTTPPthresholdEntry.setStatus("current")
_InterfaceTTPPthresholdLowestTxBias_Type = Integer32
_InterfaceTTPPthresholdLowestTxBias_Object = MibTableColumn
interfaceTTPPthresholdLowestTxBias = _InterfaceTTPPthresholdLowestTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 1),
    _InterfaceTTPPthresholdLowestTxBias_Type()
)
interfaceTTPPthresholdLowestTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPthresholdLowestTxBias.setStatus("current")
_InterfaceTTPPthresholdLowTxBias_Type = Integer32
_InterfaceTTPPthresholdLowTxBias_Object = MibTableColumn
interfaceTTPPthresholdLowTxBias = _InterfaceTTPPthresholdLowTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 2),
    _InterfaceTTPPthresholdLowTxBias_Type()
)
interfaceTTPPthresholdLowTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPthresholdLowTxBias.setStatus("current")
_InterfaceTTPPthresholdHighTxBias_Type = Integer32
_InterfaceTTPPthresholdHighTxBias_Object = MibTableColumn
interfaceTTPPthresholdHighTxBias = _InterfaceTTPPthresholdHighTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 3),
    _InterfaceTTPPthresholdHighTxBias_Type()
)
interfaceTTPPthresholdHighTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPthresholdHighTxBias.setStatus("current")
_InterfaceTTPPthresholdHighestTxBias_Type = Integer32
_InterfaceTTPPthresholdHighestTxBias_Object = MibTableColumn
interfaceTTPPthresholdHighestTxBias = _InterfaceTTPPthresholdHighestTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 4),
    _InterfaceTTPPthresholdHighestTxBias_Type()
)
interfaceTTPPthresholdHighestTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPthresholdHighestTxBias.setStatus("current")
_InterfaceTTPPhysteresisTxBias_Type = Integer32
_InterfaceTTPPhysteresisTxBias_Object = MibTableColumn
interfaceTTPPhysteresisTxBias = _InterfaceTTPPhysteresisTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 5),
    _InterfaceTTPPhysteresisTxBias_Type()
)
interfaceTTPPhysteresisTxBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPhysteresisTxBias.setStatus("current")
_InterfaceTTPPthresholdLowestRxOIP_Type = Integer32
_InterfaceTTPPthresholdLowestRxOIP_Object = MibTableColumn
interfaceTTPPthresholdLowestRxOIP = _InterfaceTTPPthresholdLowestRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 6),
    _InterfaceTTPPthresholdLowestRxOIP_Type()
)
interfaceTTPPthresholdLowestRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPthresholdLowestRxOIP.setStatus("current")
_InterfaceTTPPthresholdLowRxOIP_Type = Integer32
_InterfaceTTPPthresholdLowRxOIP_Object = MibTableColumn
interfaceTTPPthresholdLowRxOIP = _InterfaceTTPPthresholdLowRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 7),
    _InterfaceTTPPthresholdLowRxOIP_Type()
)
interfaceTTPPthresholdLowRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPthresholdLowRxOIP.setStatus("current")
_InterfaceTTPPthresholdHighRxOIP_Type = Integer32
_InterfaceTTPPthresholdHighRxOIP_Object = MibTableColumn
interfaceTTPPthresholdHighRxOIP = _InterfaceTTPPthresholdHighRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 8),
    _InterfaceTTPPthresholdHighRxOIP_Type()
)
interfaceTTPPthresholdHighRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPthresholdHighRxOIP.setStatus("current")
_InterfaceTTPPthresholdHighestRxOIP_Type = Integer32
_InterfaceTTPPthresholdHighestRxOIP_Object = MibTableColumn
interfaceTTPPthresholdHighestRxOIP = _InterfaceTTPPthresholdHighestRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 9),
    _InterfaceTTPPthresholdHighestRxOIP_Type()
)
interfaceTTPPthresholdHighestRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPthresholdHighestRxOIP.setStatus("current")
_InterfaceTTPPhysteresisRxOIP_Type = Integer32
_InterfaceTTPPhysteresisRxOIP_Object = MibTableColumn
interfaceTTPPhysteresisRxOIP = _InterfaceTTPPhysteresisRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 4, 1, 10),
    _InterfaceTTPPhysteresisRxOIP_Type()
)
interfaceTTPPhysteresisRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTPPhysteresisRxOIP.setStatus("current")
_EccmPPthresholdTable_Object = MibTable
eccmPPthresholdTable = _EccmPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 5)
)
if mibBuilder.loadTexts:
    eccmPPthresholdTable.setStatus("current")
_EccmPPthresholdEntry_Object = MibTableRow
eccmPPthresholdEntry = _EccmPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 5, 1)
)
eccmPPthresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eccmPPthresholdEntry.setStatus("current")
_EccmPPthresholdLowestRxOIP_Type = Integer32
_EccmPPthresholdLowestRxOIP_Object = MibTableColumn
eccmPPthresholdLowestRxOIP = _EccmPPthresholdLowestRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 5, 1, 1),
    _EccmPPthresholdLowestRxOIP_Type()
)
eccmPPthresholdLowestRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eccmPPthresholdLowestRxOIP.setStatus("current")
_EccmPPthresholdLowRxOIP_Type = Integer32
_EccmPPthresholdLowRxOIP_Object = MibTableColumn
eccmPPthresholdLowRxOIP = _EccmPPthresholdLowRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 5, 1, 2),
    _EccmPPthresholdLowRxOIP_Type()
)
eccmPPthresholdLowRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eccmPPthresholdLowRxOIP.setStatus("current")
_EccmPPthresholdHighRxOIP_Type = Integer32
_EccmPPthresholdHighRxOIP_Object = MibTableColumn
eccmPPthresholdHighRxOIP = _EccmPPthresholdHighRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 5, 1, 3),
    _EccmPPthresholdHighRxOIP_Type()
)
eccmPPthresholdHighRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eccmPPthresholdHighRxOIP.setStatus("current")
_EccmPPthresholdHighestRxOIP_Type = Integer32
_EccmPPthresholdHighestRxOIP_Object = MibTableColumn
eccmPPthresholdHighestRxOIP = _EccmPPthresholdHighestRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 5, 1, 4),
    _EccmPPthresholdHighestRxOIP_Type()
)
eccmPPthresholdHighestRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eccmPPthresholdHighestRxOIP.setStatus("current")
_EccmPPhysteresisRxOIP_Type = Integer32
_EccmPPhysteresisRxOIP_Object = MibTableColumn
eccmPPhysteresisRxOIP = _EccmPPhysteresisRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 5, 1, 5),
    _EccmPPhysteresisRxOIP_Type()
)
eccmPPhysteresisRxOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eccmPPhysteresisRxOIP.setStatus("current")
_ApsPPthresholdTable_Object = MibTable
apsPPthresholdTable = _ApsPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 6)
)
if mibBuilder.loadTexts:
    apsPPthresholdTable.setStatus("current")
_ApsPPthresholdEntry_Object = MibTableRow
apsPPthresholdEntry = _ApsPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 6, 1)
)
apsPPthresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apsPPthresholdEntry.setStatus("current")
_ApsPPthresholdLowestOipOsc_Type = Integer32
_ApsPPthresholdLowestOipOsc_Object = MibTableColumn
apsPPthresholdLowestOipOsc = _ApsPPthresholdLowestOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 6, 1, 6),
    _ApsPPthresholdLowestOipOsc_Type()
)
apsPPthresholdLowestOipOsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsPPthresholdLowestOipOsc.setStatus("current")
_ApsPPthresholdLowOipOsc_Type = Integer32
_ApsPPthresholdLowOipOsc_Object = MibTableColumn
apsPPthresholdLowOipOsc = _ApsPPthresholdLowOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 6, 1, 7),
    _ApsPPthresholdLowOipOsc_Type()
)
apsPPthresholdLowOipOsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsPPthresholdLowOipOsc.setStatus("current")
_ApsPPthresholdHighOipOsc_Type = Integer32
_ApsPPthresholdHighOipOsc_Object = MibTableColumn
apsPPthresholdHighOipOsc = _ApsPPthresholdHighOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 6, 1, 8),
    _ApsPPthresholdHighOipOsc_Type()
)
apsPPthresholdHighOipOsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsPPthresholdHighOipOsc.setStatus("current")
_ApsPPthresholdHighestOipOsc_Type = Integer32
_ApsPPthresholdHighestOipOsc_Object = MibTableColumn
apsPPthresholdHighestOipOsc = _ApsPPthresholdHighestOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 6, 1, 9),
    _ApsPPthresholdHighestOipOsc_Type()
)
apsPPthresholdHighestOipOsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsPPthresholdHighestOipOsc.setStatus("current")
_ApsPPhysteresisOipOsc_Type = Integer32
_ApsPPhysteresisOipOsc_Object = MibTableColumn
apsPPhysteresisOipOsc = _ApsPPhysteresisOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 2, 6, 1, 10),
    _ApsPPhysteresisOipOsc_Type()
)
apsPPhysteresisOipOsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsPPhysteresisOipOsc.setStatus("current")
_GeneralPerformanceAdmin_ObjectIdentity = ObjectIdentity
generalPerformanceAdmin = _GeneralPerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3)
)
_AlarmAdminTable_Object = MibTable
alarmAdminTable = _AlarmAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alarmAdminTable.setStatus("current")
_AlarmAdminEntry_Object = MibTableRow
alarmAdminEntry = _AlarmAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 1, 1)
)
alarmAdminEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "alarmAdminType"),
)
if mibBuilder.loadTexts:
    alarmAdminEntry.setStatus("current")


class _AlarmAdminType_Type(Integer32):
    """Custom type alarmAdminType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pathSd", 1),
          ("sectionSd", 2))
    )


_AlarmAdminType_Type.__name__ = "Integer32"
_AlarmAdminType_Object = MibTableColumn
alarmAdminType = _AlarmAdminType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 1, 1, 1),
    _AlarmAdminType_Type()
)
alarmAdminType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmAdminType.setStatus("current")


class _AlarmAdminTypeDetails_Type(Integer32):
    """Custom type alarmAdminTypeDetails based on Integer32"""
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
        *(("sdNotApplicable", 0),
          ("bitSd", 1),
          ("blockSd", 2),
          ("sdNotSupported", 3))
    )


_AlarmAdminTypeDetails_Type.__name__ = "Integer32"
_AlarmAdminTypeDetails_Object = MibTableColumn
alarmAdminTypeDetails = _AlarmAdminTypeDetails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 1, 1, 2),
    _AlarmAdminTypeDetails_Type()
)
alarmAdminTypeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAdminTypeDetails.setStatus("current")


class _AlarmAdminTypeThreshold_Type(Integer32):
    """Custom type alarmAdminTypeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_AlarmAdminTypeThreshold_Type.__name__ = "Integer32"
_AlarmAdminTypeThreshold_Object = MibTableColumn
alarmAdminTypeThreshold = _AlarmAdminTypeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 1, 1, 3),
    _AlarmAdminTypeThreshold_Type()
)
alarmAdminTypeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmAdminTypeThreshold.setStatus("current")


class _AlarmAdminTypePeriod_Type(Integer32):
    """Custom type alarmAdminTypePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AlarmAdminTypePeriod_Type.__name__ = "Integer32"
_AlarmAdminTypePeriod_Object = MibTableColumn
alarmAdminTypePeriod = _AlarmAdminTypePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 1, 1, 4),
    _AlarmAdminTypePeriod_Type()
)
alarmAdminTypePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmAdminTypePeriod.setStatus("current")
_ModulePerformanceStatusTable_Object = MibTable
modulePerformanceStatusTable = _ModulePerformanceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    modulePerformanceStatusTable.setStatus("current")
_ModulePerformanceStatusEntry_Object = MibTableRow
modulePerformanceStatusEntry = _ModulePerformanceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 2, 1)
)
modulePerformanceStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "modulePerformanceStatusType"),
)
if mibBuilder.loadTexts:
    modulePerformanceStatusEntry.setStatus("current")


class _ModulePerformanceStatusType_Type(Integer32):
    """Custom type modulePerformanceStatusType based on Integer32"""
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
        *(("remOptSwPLP15minInterval", 1),
          ("remOptSwPLP24HourInterval", 2),
          ("remOptSwPLA15minInterval", 3),
          ("remOptSwPLA24HourInterval", 4))
    )


_ModulePerformanceStatusType_Type.__name__ = "Integer32"
_ModulePerformanceStatusType_Object = MibTableColumn
modulePerformanceStatusType = _ModulePerformanceStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 2, 1, 1),
    _ModulePerformanceStatusType_Type()
)
modulePerformanceStatusType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modulePerformanceStatusType.setStatus("current")
_ModulePerformanceStatusState_Type = AvailState
_ModulePerformanceStatusState_Object = MibTableColumn
modulePerformanceStatusState = _ModulePerformanceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 2, 1, 2),
    _ModulePerformanceStatusState_Type()
)
modulePerformanceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePerformanceStatusState.setStatus("current")
_InterfacePerformanceStatusTable_Object = MibTable
interfacePerformanceStatusTable = _InterfacePerformanceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    interfacePerformanceStatusTable.setStatus("current")
_InterfacePerformanceStatusEntry_Object = MibTableRow
interfacePerformanceStatusEntry = _InterfacePerformanceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 3, 1)
)
interfacePerformanceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfacePerformanceStatusType"),
)
if mibBuilder.loadTexts:
    interfacePerformanceStatusEntry.setStatus("current")


class _InterfacePerformanceStatusType_Type(Integer32):
    """Custom type interfacePerformanceStatusType based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("sonetSectionCurrent15min", 1),
          ("sonetSectionCurrent24h", 2),
          ("sonetSection15minInterval", 3),
          ("sonetSection24hInterval", 4),
          ("edfaPLP15minInterval", 5),
          ("edfaPLP24hInterval", 6),
          ("interfaceTTPLP15minInterval", 7),
          ("interfaceTTPLP24hInterval", 8),
          ("edfaPLA15minInterval", 9),
          ("edfaPLA24hInterval", 10),
          ("interfaceTTPLA15minInterval", 11),
          ("interfaceTTPLA24hInterval", 12),
          ("otuFecCurrent15min", 13),
          ("otuFecCurrent24h", 14),
          ("otuFec15minInterval", 15),
          ("otuFec24hInterval", 16),
          ("eccmPLP15minInterval", 17),
          ("eccmPLP24hInterval", 18),
          ("eccmPLA15minInterval", 19),
          ("eccmPLA24hInterval", 20),
          ("codingStatsCurrent15min", 21),
          ("codingStatsCurrent24h", 22),
          ("codingStats15minInterval", 23),
          ("codingStats24hInterval", 24),
          ("sonetPathCurrent15min", 25),
          ("sonetPathCurrent24h", 26),
          ("sonetPath15minInterval", 27),
          ("sonetPath24hInterval", 28),
          ("apsPLP15minInterval", 29),
          ("apsPLP24hInterval", 30),
          ("apsPLA15minInterval", 31),
          ("apsPLA24hInterval", 32))
    )


_InterfacePerformanceStatusType_Type.__name__ = "Integer32"
_InterfacePerformanceStatusType_Object = MibTableColumn
interfacePerformanceStatusType = _InterfacePerformanceStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 3, 1, 1),
    _InterfacePerformanceStatusType_Type()
)
interfacePerformanceStatusType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfacePerformanceStatusType.setStatus("current")
_InterfacePerformanceStatusState_Type = AvailState
_InterfacePerformanceStatusState_Object = MibTableColumn
interfacePerformanceStatusState = _InterfacePerformanceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 1, 3, 3, 1, 2),
    _InterfacePerformanceStatusState_Type()
)
interfacePerformanceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacePerformanceStatusState.setStatus("current")
_PerformanceMonitoring_ObjectIdentity = ObjectIdentity
performanceMonitoring = _PerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2)
)
_SonetPerformanceMon_ObjectIdentity = ObjectIdentity
sonetPerformanceMon = _SonetPerformanceMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1)
)
_SonetSectionPerformanceMon_ObjectIdentity = ObjectIdentity
sonetSectionPerformanceMon = _SonetSectionPerformanceMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1)
)
_SonetSectionCurrent15minTable_Object = MibTable
sonetSectionCurrent15minTable = _SonetSectionCurrent15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sonetSectionCurrent15minTable.setStatus("current")
_SonetSectionCurrent15minEntry_Object = MibTableRow
sonetSectionCurrent15minEntry = _SonetSectionCurrent15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 1, 1)
)
sonetSectionCurrent15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetSectionCurrent15minEntry.setStatus("current")


class _SonetSectionCurrent15minStatus_Type(Integer32):
    """Custom type sonetSectionCurrent15minStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SonetSectionCurrent15minStatus_Type.__name__ = "Integer32"
_SonetSectionCurrent15minStatus_Object = MibTableColumn
sonetSectionCurrent15minStatus = _SonetSectionCurrent15minStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 1, 1, 1),
    _SonetSectionCurrent15minStatus_Type()
)
sonetSectionCurrent15minStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minStatus.setStatus("current")
_SonetSectionCurrent15minESs_Type = Gauge32
_SonetSectionCurrent15minESs_Object = MibTableColumn
sonetSectionCurrent15minESs = _SonetSectionCurrent15minESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 1, 1, 2),
    _SonetSectionCurrent15minESs_Type()
)
sonetSectionCurrent15minESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minESs.setStatus("current")
_SonetSectionCurrent15minSESs_Type = Gauge32
_SonetSectionCurrent15minSESs_Object = MibTableColumn
sonetSectionCurrent15minSESs = _SonetSectionCurrent15minSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 1, 1, 3),
    _SonetSectionCurrent15minSESs_Type()
)
sonetSectionCurrent15minSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minSESs.setStatus("current")
_SonetSectionCurrent15minSEFSs_Type = Gauge32
_SonetSectionCurrent15minSEFSs_Object = MibTableColumn
sonetSectionCurrent15minSEFSs = _SonetSectionCurrent15minSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 1, 1, 4),
    _SonetSectionCurrent15minSEFSs_Type()
)
sonetSectionCurrent15minSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minSEFSs.setStatus("current")
_SonetSectionCurrent15minCVs_Type = Gauge32
_SonetSectionCurrent15minCVs_Object = MibTableColumn
sonetSectionCurrent15minCVs = _SonetSectionCurrent15minCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 1, 1, 5),
    _SonetSectionCurrent15minCVs_Type()
)
sonetSectionCurrent15minCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minCVs.setStatus("current")


class _SonetSectionCurrent15minTimeElapsed_Type(Integer32):
    """Custom type sonetSectionCurrent15minTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonetSectionCurrent15minTimeElapsed_Type.__name__ = "Integer32"
_SonetSectionCurrent15minTimeElapsed_Object = MibTableColumn
sonetSectionCurrent15minTimeElapsed = _SonetSectionCurrent15minTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 1, 1, 6),
    _SonetSectionCurrent15minTimeElapsed_Type()
)
sonetSectionCurrent15minTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minTimeElapsed.setStatus("current")
_SonetSectionCurrent24hTable_Object = MibTable
sonetSectionCurrent24hTable = _SonetSectionCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonetSectionCurrent24hTable.setStatus("current")
_SonetSectionCurrent24hEntry_Object = MibTableRow
sonetSectionCurrent24hEntry = _SonetSectionCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 2, 1)
)
sonetSectionCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetSectionCurrent24hEntry.setStatus("current")


class _SonetSectionCurrent24hStatus_Type(Integer32):
    """Custom type sonetSectionCurrent24hStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SonetSectionCurrent24hStatus_Type.__name__ = "Integer32"
_SonetSectionCurrent24hStatus_Object = MibTableColumn
sonetSectionCurrent24hStatus = _SonetSectionCurrent24hStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 2, 1, 1),
    _SonetSectionCurrent24hStatus_Type()
)
sonetSectionCurrent24hStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent24hStatus.setStatus("current")
_SonetSectionCurrent24hESs_Type = Gauge32
_SonetSectionCurrent24hESs_Object = MibTableColumn
sonetSectionCurrent24hESs = _SonetSectionCurrent24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 2, 1, 2),
    _SonetSectionCurrent24hESs_Type()
)
sonetSectionCurrent24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent24hESs.setStatus("current")
_SonetSectionCurrent24hSESs_Type = Gauge32
_SonetSectionCurrent24hSESs_Object = MibTableColumn
sonetSectionCurrent24hSESs = _SonetSectionCurrent24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 2, 1, 3),
    _SonetSectionCurrent24hSESs_Type()
)
sonetSectionCurrent24hSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent24hSESs.setStatus("current")
_SonetSectionCurrent24hSEFSs_Type = Gauge32
_SonetSectionCurrent24hSEFSs_Object = MibTableColumn
sonetSectionCurrent24hSEFSs = _SonetSectionCurrent24hSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 2, 1, 4),
    _SonetSectionCurrent24hSEFSs_Type()
)
sonetSectionCurrent24hSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent24hSEFSs.setStatus("current")
_SonetSectionCurrent24hCVs_Type = Gauge32
_SonetSectionCurrent24hCVs_Object = MibTableColumn
sonetSectionCurrent24hCVs = _SonetSectionCurrent24hCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 2, 1, 5),
    _SonetSectionCurrent24hCVs_Type()
)
sonetSectionCurrent24hCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent24hCVs.setStatus("current")


class _SonetSectionCurrent24hTimeElapsed_Type(Integer32):
    """Custom type sonetSectionCurrent24hTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SonetSectionCurrent24hTimeElapsed_Type.__name__ = "Integer32"
_SonetSectionCurrent24hTimeElapsed_Object = MibTableColumn
sonetSectionCurrent24hTimeElapsed = _SonetSectionCurrent24hTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 2, 1, 6),
    _SonetSectionCurrent24hTimeElapsed_Type()
)
sonetSectionCurrent24hTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrent24hTimeElapsed.setStatus("current")
_SonetSection15minIntervalTable_Object = MibTable
sonetSection15minIntervalTable = _SonetSection15minIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonetSection15minIntervalTable.setStatus("current")
_SonetSection15minIntervalEntry_Object = MibTableRow
sonetSection15minIntervalEntry = _SonetSection15minIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3, 1)
)
sonetSection15minIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "sonetSection15minIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetSection15minIntervalEntry.setStatus("current")


class _SonetSection15minIntervalNumber_Type(Integer32):
    """Custom type sonetSection15minIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonetSection15minIntervalNumber_Type.__name__ = "Integer32"
_SonetSection15minIntervalNumber_Object = MibTableColumn
sonetSection15minIntervalNumber = _SonetSection15minIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3, 1, 1),
    _SonetSection15minIntervalNumber_Type()
)
sonetSection15minIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection15minIntervalNumber.setStatus("current")
_SonetSection15minIntervalESs_Type = Gauge32
_SonetSection15minIntervalESs_Object = MibTableColumn
sonetSection15minIntervalESs = _SonetSection15minIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3, 1, 2),
    _SonetSection15minIntervalESs_Type()
)
sonetSection15minIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection15minIntervalESs.setStatus("current")
_SonetSection15minIntervalSESs_Type = Gauge32
_SonetSection15minIntervalSESs_Object = MibTableColumn
sonetSection15minIntervalSESs = _SonetSection15minIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3, 1, 3),
    _SonetSection15minIntervalSESs_Type()
)
sonetSection15minIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection15minIntervalSESs.setStatus("current")
_SonetSection15minIntervalSEFs_Type = Gauge32
_SonetSection15minIntervalSEFs_Object = MibTableColumn
sonetSection15minIntervalSEFs = _SonetSection15minIntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3, 1, 4),
    _SonetSection15minIntervalSEFs_Type()
)
sonetSection15minIntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection15minIntervalSEFs.setStatus("current")
_SonetSection15minIntervalCVs_Type = Gauge32
_SonetSection15minIntervalCVs_Object = MibTableColumn
sonetSection15minIntervalCVs = _SonetSection15minIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3, 1, 5),
    _SonetSection15minIntervalCVs_Type()
)
sonetSection15minIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection15minIntervalCVs.setStatus("current")
_SonetSection15minIntervalValidData_Type = TruthValue
_SonetSection15minIntervalValidData_Object = MibTableColumn
sonetSection15minIntervalValidData = _SonetSection15minIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3, 1, 6),
    _SonetSection15minIntervalValidData_Type()
)
sonetSection15minIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection15minIntervalValidData.setStatus("current")
_SonetSection15minIntervalTimeStamp_Type = DateAndTime
_SonetSection15minIntervalTimeStamp_Object = MibTableColumn
sonetSection15minIntervalTimeStamp = _SonetSection15minIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 3, 1, 7),
    _SonetSection15minIntervalTimeStamp_Type()
)
sonetSection15minIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection15minIntervalTimeStamp.setStatus("current")
_SonetSection24hIntervalTable_Object = MibTable
sonetSection24hIntervalTable = _SonetSection24hIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sonetSection24hIntervalTable.setStatus("current")
_SonetSection24hIntervalEntry_Object = MibTableRow
sonetSection24hIntervalEntry = _SonetSection24hIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4, 1)
)
sonetSection24hIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "sonetSection24hIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetSection24hIntervalEntry.setStatus("current")


class _SonetSection24hIntervalNumber_Type(Integer32):
    """Custom type sonetSection24hIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonetSection24hIntervalNumber_Type.__name__ = "Integer32"
_SonetSection24hIntervalNumber_Object = MibTableColumn
sonetSection24hIntervalNumber = _SonetSection24hIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4, 1, 1),
    _SonetSection24hIntervalNumber_Type()
)
sonetSection24hIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection24hIntervalNumber.setStatus("current")
_SonetSection24hIntervalESs_Type = Gauge32
_SonetSection24hIntervalESs_Object = MibTableColumn
sonetSection24hIntervalESs = _SonetSection24hIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4, 1, 2),
    _SonetSection24hIntervalESs_Type()
)
sonetSection24hIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection24hIntervalESs.setStatus("current")
_SonetSection24hIntervalSESs_Type = Gauge32
_SonetSection24hIntervalSESs_Object = MibTableColumn
sonetSection24hIntervalSESs = _SonetSection24hIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4, 1, 3),
    _SonetSection24hIntervalSESs_Type()
)
sonetSection24hIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection24hIntervalSESs.setStatus("current")
_SonetSection24hIntervalSEFs_Type = Gauge32
_SonetSection24hIntervalSEFs_Object = MibTableColumn
sonetSection24hIntervalSEFs = _SonetSection24hIntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4, 1, 4),
    _SonetSection24hIntervalSEFs_Type()
)
sonetSection24hIntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection24hIntervalSEFs.setStatus("current")
_SonetSection24hIntervalCVs_Type = Gauge32
_SonetSection24hIntervalCVs_Object = MibTableColumn
sonetSection24hIntervalCVs = _SonetSection24hIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4, 1, 5),
    _SonetSection24hIntervalCVs_Type()
)
sonetSection24hIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection24hIntervalCVs.setStatus("current")
_SonetSection24hIntervalValidData_Type = TruthValue
_SonetSection24hIntervalValidData_Object = MibTableColumn
sonetSection24hIntervalValidData = _SonetSection24hIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4, 1, 6),
    _SonetSection24hIntervalValidData_Type()
)
sonetSection24hIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection24hIntervalValidData.setStatus("current")
_SonetSection24hIntervalTimeStamp_Type = DateAndTime
_SonetSection24hIntervalTimeStamp_Object = MibTableColumn
sonetSection24hIntervalTimeStamp = _SonetSection24hIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 1, 4, 1, 7),
    _SonetSection24hIntervalTimeStamp_Type()
)
sonetSection24hIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSection24hIntervalTimeStamp.setStatus("current")
_SonetPathPerformanceMon_ObjectIdentity = ObjectIdentity
sonetPathPerformanceMon = _SonetPathPerformanceMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2)
)
_SonetPathCurrent15minTable_Object = MibTable
sonetPathCurrent15minTable = _SonetPathCurrent15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sonetPathCurrent15minTable.setStatus("current")
_SonetPathCurrent15minEntry_Object = MibTableRow
sonetPathCurrent15minEntry = _SonetPathCurrent15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1, 1)
)
sonetPathCurrent15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetPathCurrent15minEntry.setStatus("current")


class _SonetPathCurrent15minWidth_Type(Integer32):
    """Custom type sonetPathCurrent15minWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("sts48cSTM16", 5)
    )


_SonetPathCurrent15minWidth_Type.__name__ = "Integer32"
_SonetPathCurrent15minWidth_Object = MibTableColumn
sonetPathCurrent15minWidth = _SonetPathCurrent15minWidth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1, 1, 1),
    _SonetPathCurrent15minWidth_Type()
)
sonetPathCurrent15minWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent15minWidth.setStatus("current")


class _SonetPathCurrent15minStatus_Type(Integer32):
    """Custom type sonetPathCurrent15minStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SonetPathCurrent15minStatus_Type.__name__ = "Integer32"
_SonetPathCurrent15minStatus_Object = MibTableColumn
sonetPathCurrent15minStatus = _SonetPathCurrent15minStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1, 1, 2),
    _SonetPathCurrent15minStatus_Type()
)
sonetPathCurrent15minStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent15minStatus.setStatus("current")
_SonetPathCurrent15minESs_Type = Gauge32
_SonetPathCurrent15minESs_Object = MibTableColumn
sonetPathCurrent15minESs = _SonetPathCurrent15minESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1, 1, 3),
    _SonetPathCurrent15minESs_Type()
)
sonetPathCurrent15minESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent15minESs.setStatus("current")
_SonetPathCurrent15minSESs_Type = Gauge32
_SonetPathCurrent15minSESs_Object = MibTableColumn
sonetPathCurrent15minSESs = _SonetPathCurrent15minSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1, 1, 4),
    _SonetPathCurrent15minSESs_Type()
)
sonetPathCurrent15minSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent15minSESs.setStatus("current")
_SonetPathCurrent15minCVs_Type = Gauge32
_SonetPathCurrent15minCVs_Object = MibTableColumn
sonetPathCurrent15minCVs = _SonetPathCurrent15minCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1, 1, 5),
    _SonetPathCurrent15minCVs_Type()
)
sonetPathCurrent15minCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent15minCVs.setStatus("current")
_SonetPathCurrent15minUASs_Type = Gauge32
_SonetPathCurrent15minUASs_Object = MibTableColumn
sonetPathCurrent15minUASs = _SonetPathCurrent15minUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1, 1, 6),
    _SonetPathCurrent15minUASs_Type()
)
sonetPathCurrent15minUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent15minUASs.setStatus("current")


class _SonetPathCurrent15minTimeElapsed_Type(Integer32):
    """Custom type sonetPathCurrent15minTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SonetPathCurrent15minTimeElapsed_Type.__name__ = "Integer32"
_SonetPathCurrent15minTimeElapsed_Object = MibTableColumn
sonetPathCurrent15minTimeElapsed = _SonetPathCurrent15minTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 1, 1, 7),
    _SonetPathCurrent15minTimeElapsed_Type()
)
sonetPathCurrent15minTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent15minTimeElapsed.setStatus("current")
_SonetPathCurrent24hTable_Object = MibTable
sonetPathCurrent24hTable = _SonetPathCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonetPathCurrent24hTable.setStatus("current")
_SonetPathCurrent24hEntry_Object = MibTableRow
sonetPathCurrent24hEntry = _SonetPathCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2, 1)
)
sonetPathCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetPathCurrent24hEntry.setStatus("current")


class _SonetPathCurrent24hWidth_Type(Integer32):
    """Custom type sonetPathCurrent24hWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("sts48cSTM16", 5)
    )


_SonetPathCurrent24hWidth_Type.__name__ = "Integer32"
_SonetPathCurrent24hWidth_Object = MibTableColumn
sonetPathCurrent24hWidth = _SonetPathCurrent24hWidth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2, 1, 1),
    _SonetPathCurrent24hWidth_Type()
)
sonetPathCurrent24hWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent24hWidth.setStatus("current")


class _SonetPathCurrent24hStatus_Type(Integer32):
    """Custom type sonetPathCurrent24hStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SonetPathCurrent24hStatus_Type.__name__ = "Integer32"
_SonetPathCurrent24hStatus_Object = MibTableColumn
sonetPathCurrent24hStatus = _SonetPathCurrent24hStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2, 1, 2),
    _SonetPathCurrent24hStatus_Type()
)
sonetPathCurrent24hStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent24hStatus.setStatus("current")
_SonetPathCurrent24hESs_Type = Gauge32
_SonetPathCurrent24hESs_Object = MibTableColumn
sonetPathCurrent24hESs = _SonetPathCurrent24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2, 1, 3),
    _SonetPathCurrent24hESs_Type()
)
sonetPathCurrent24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent24hESs.setStatus("current")
_SonetPathCurrent24hSESs_Type = Gauge32
_SonetPathCurrent24hSESs_Object = MibTableColumn
sonetPathCurrent24hSESs = _SonetPathCurrent24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2, 1, 4),
    _SonetPathCurrent24hSESs_Type()
)
sonetPathCurrent24hSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent24hSESs.setStatus("current")
_SonetPathCurrent24hCVs_Type = Gauge32
_SonetPathCurrent24hCVs_Object = MibTableColumn
sonetPathCurrent24hCVs = _SonetPathCurrent24hCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2, 1, 5),
    _SonetPathCurrent24hCVs_Type()
)
sonetPathCurrent24hCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent24hCVs.setStatus("current")
_SonetPathCurrent24hUASs_Type = Gauge32
_SonetPathCurrent24hUASs_Object = MibTableColumn
sonetPathCurrent24hUASs = _SonetPathCurrent24hUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2, 1, 6),
    _SonetPathCurrent24hUASs_Type()
)
sonetPathCurrent24hUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent24hUASs.setStatus("current")


class _SonetPathCurrent24hTimeElapsed_Type(Integer32):
    """Custom type sonetPathCurrent24hTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SonetPathCurrent24hTimeElapsed_Type.__name__ = "Integer32"
_SonetPathCurrent24hTimeElapsed_Object = MibTableColumn
sonetPathCurrent24hTimeElapsed = _SonetPathCurrent24hTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 2, 1, 7),
    _SonetPathCurrent24hTimeElapsed_Type()
)
sonetPathCurrent24hTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrent24hTimeElapsed.setStatus("current")
_SonetPath15minIntervalTable_Object = MibTable
sonetPath15minIntervalTable = _SonetPath15minIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sonetPath15minIntervalTable.setStatus("current")
_SonetPath15minIntervalEntry_Object = MibTableRow
sonetPath15minIntervalEntry = _SonetPath15minIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3, 1)
)
sonetPath15minIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "sonetPath15minIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetPath15minIntervalEntry.setStatus("current")


class _SonetPath15minIntervalNumber_Type(Integer32):
    """Custom type sonetPath15minIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonetPath15minIntervalNumber_Type.__name__ = "Integer32"
_SonetPath15minIntervalNumber_Object = MibTableColumn
sonetPath15minIntervalNumber = _SonetPath15minIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3, 1, 1),
    _SonetPath15minIntervalNumber_Type()
)
sonetPath15minIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath15minIntervalNumber.setStatus("current")
_SonetPath15minIntervalESs_Type = Gauge32
_SonetPath15minIntervalESs_Object = MibTableColumn
sonetPath15minIntervalESs = _SonetPath15minIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3, 1, 2),
    _SonetPath15minIntervalESs_Type()
)
sonetPath15minIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath15minIntervalESs.setStatus("current")
_SonetPath15minIntervalSESs_Type = Gauge32
_SonetPath15minIntervalSESs_Object = MibTableColumn
sonetPath15minIntervalSESs = _SonetPath15minIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3, 1, 3),
    _SonetPath15minIntervalSESs_Type()
)
sonetPath15minIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath15minIntervalSESs.setStatus("current")
_SonetPath15minIntervalCVs_Type = Gauge32
_SonetPath15minIntervalCVs_Object = MibTableColumn
sonetPath15minIntervalCVs = _SonetPath15minIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3, 1, 4),
    _SonetPath15minIntervalCVs_Type()
)
sonetPath15minIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath15minIntervalCVs.setStatus("current")
_SonetPath15minIntervalUASs_Type = Gauge32
_SonetPath15minIntervalUASs_Object = MibTableColumn
sonetPath15minIntervalUASs = _SonetPath15minIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3, 1, 5),
    _SonetPath15minIntervalUASs_Type()
)
sonetPath15minIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath15minIntervalUASs.setStatus("current")
_SonetPath15minIntervalValidData_Type = TruthValue
_SonetPath15minIntervalValidData_Object = MibTableColumn
sonetPath15minIntervalValidData = _SonetPath15minIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3, 1, 6),
    _SonetPath15minIntervalValidData_Type()
)
sonetPath15minIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath15minIntervalValidData.setStatus("current")
_SonetPath15minIntervalTimeStamp_Type = DateAndTime
_SonetPath15minIntervalTimeStamp_Object = MibTableColumn
sonetPath15minIntervalTimeStamp = _SonetPath15minIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 3, 1, 7),
    _SonetPath15minIntervalTimeStamp_Type()
)
sonetPath15minIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath15minIntervalTimeStamp.setStatus("current")
_SonetPath24hIntervalTable_Object = MibTable
sonetPath24hIntervalTable = _SonetPath24hIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    sonetPath24hIntervalTable.setStatus("current")
_SonetPath24hIntervalEntry_Object = MibTableRow
sonetPath24hIntervalEntry = _SonetPath24hIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4, 1)
)
sonetPath24hIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "sonetPath24hIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonetPath24hIntervalEntry.setStatus("current")


class _SonetPath24hIntervalNumber_Type(Integer32):
    """Custom type sonetPath24hIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonetPath24hIntervalNumber_Type.__name__ = "Integer32"
_SonetPath24hIntervalNumber_Object = MibTableColumn
sonetPath24hIntervalNumber = _SonetPath24hIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4, 1, 1),
    _SonetPath24hIntervalNumber_Type()
)
sonetPath24hIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath24hIntervalNumber.setStatus("current")
_SonetPath24hIntervalESs_Type = Gauge32
_SonetPath24hIntervalESs_Object = MibTableColumn
sonetPath24hIntervalESs = _SonetPath24hIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4, 1, 2),
    _SonetPath24hIntervalESs_Type()
)
sonetPath24hIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath24hIntervalESs.setStatus("current")
_SonetPath24hIntervalSESs_Type = Gauge32
_SonetPath24hIntervalSESs_Object = MibTableColumn
sonetPath24hIntervalSESs = _SonetPath24hIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4, 1, 3),
    _SonetPath24hIntervalSESs_Type()
)
sonetPath24hIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath24hIntervalSESs.setStatus("current")
_SonetPath24hIntervalCVs_Type = Gauge32
_SonetPath24hIntervalCVs_Object = MibTableColumn
sonetPath24hIntervalCVs = _SonetPath24hIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4, 1, 4),
    _SonetPath24hIntervalCVs_Type()
)
sonetPath24hIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath24hIntervalCVs.setStatus("current")
_SonetPath24hIntervalUASs_Type = Gauge32
_SonetPath24hIntervalUASs_Object = MibTableColumn
sonetPath24hIntervalUASs = _SonetPath24hIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4, 1, 5),
    _SonetPath24hIntervalUASs_Type()
)
sonetPath24hIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath24hIntervalUASs.setStatus("current")
_SonetPath24hIntervalValidData_Type = TruthValue
_SonetPath24hIntervalValidData_Object = MibTableColumn
sonetPath24hIntervalValidData = _SonetPath24hIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4, 1, 6),
    _SonetPath24hIntervalValidData_Type()
)
sonetPath24hIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath24hIntervalValidData.setStatus("current")
_SonetPath24hIntervalTimeStamp_Type = DateAndTime
_SonetPath24hIntervalTimeStamp_Object = MibTableColumn
sonetPath24hIntervalTimeStamp = _SonetPath24hIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 1, 2, 4, 1, 7),
    _SonetPath24hIntervalTimeStamp_Type()
)
sonetPath24hIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPath24hIntervalTimeStamp.setStatus("current")
_PhysicalLayerPerformanceMon_ObjectIdentity = ObjectIdentity
physicalLayerPerformanceMon = _PhysicalLayerPerformanceMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2)
)
_RemOptSwPLP15minIntTable_Object = MibTable
remOptSwPLP15minIntTable = _RemOptSwPLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    remOptSwPLP15minIntTable.setStatus("current")
_RemOptSwPLP15minIntEntry_Object = MibTableRow
remOptSwPLP15minIntEntry = _RemOptSwPLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 1, 1)
)
remOptSwPLP15minIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "remOptSwPLP15minIntNumber"),
)
if mibBuilder.loadTexts:
    remOptSwPLP15minIntEntry.setStatus("current")


class _RemOptSwPLP15minIntNumber_Type(Integer32):
    """Custom type remOptSwPLP15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RemOptSwPLP15minIntNumber_Type.__name__ = "Integer32"
_RemOptSwPLP15minIntNumber_Object = MibTableColumn
remOptSwPLP15minIntNumber = _RemOptSwPLP15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 1, 1, 1),
    _RemOptSwPLP15minIntNumber_Type()
)
remOptSwPLP15minIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP15minIntNumber.setStatus("current")
_RemOptSwPLP15minIntAverageTxBias_Type = Integer32
_RemOptSwPLP15minIntAverageTxBias_Object = MibTableColumn
remOptSwPLP15minIntAverageTxBias = _RemOptSwPLP15minIntAverageTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 1, 1, 2),
    _RemOptSwPLP15minIntAverageTxBias_Type()
)
remOptSwPLP15minIntAverageTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP15minIntAverageTxBias.setStatus("current")
_RemOptSwPLP15minIntMinTxBias_Type = Integer32
_RemOptSwPLP15minIntMinTxBias_Object = MibTableColumn
remOptSwPLP15minIntMinTxBias = _RemOptSwPLP15minIntMinTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 1, 1, 3),
    _RemOptSwPLP15minIntMinTxBias_Type()
)
remOptSwPLP15minIntMinTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP15minIntMinTxBias.setStatus("current")
_RemOptSwPLP15minIntMaxTxBias_Type = Integer32
_RemOptSwPLP15minIntMaxTxBias_Object = MibTableColumn
remOptSwPLP15minIntMaxTxBias = _RemOptSwPLP15minIntMaxTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 1, 1, 4),
    _RemOptSwPLP15minIntMaxTxBias_Type()
)
remOptSwPLP15minIntMaxTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP15minIntMaxTxBias.setStatus("current")
_RemOptSwPLP15minIntValidData_Type = TruthValue
_RemOptSwPLP15minIntValidData_Object = MibTableColumn
remOptSwPLP15minIntValidData = _RemOptSwPLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 1, 1, 5),
    _RemOptSwPLP15minIntValidData_Type()
)
remOptSwPLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP15minIntValidData.setStatus("current")
_RemOptSwPLP15minIntTimeStamp_Type = DateAndTime
_RemOptSwPLP15minIntTimeStamp_Object = MibTableColumn
remOptSwPLP15minIntTimeStamp = _RemOptSwPLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 1, 1, 6),
    _RemOptSwPLP15minIntTimeStamp_Type()
)
remOptSwPLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP15minIntTimeStamp.setStatus("current")
_RemOptSwPLP24hIntTable_Object = MibTable
remOptSwPLP24hIntTable = _RemOptSwPLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    remOptSwPLP24hIntTable.setStatus("current")
_RemOptSwPLP24hIntEntry_Object = MibTableRow
remOptSwPLP24hIntEntry = _RemOptSwPLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 2, 1)
)
remOptSwPLP24hIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "remOptSwPLP24hIntNumber"),
)
if mibBuilder.loadTexts:
    remOptSwPLP24hIntEntry.setStatus("current")


class _RemOptSwPLP24hIntNumber_Type(Integer32):
    """Custom type remOptSwPLP24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RemOptSwPLP24hIntNumber_Type.__name__ = "Integer32"
_RemOptSwPLP24hIntNumber_Object = MibTableColumn
remOptSwPLP24hIntNumber = _RemOptSwPLP24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 2, 1, 1),
    _RemOptSwPLP24hIntNumber_Type()
)
remOptSwPLP24hIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP24hIntNumber.setStatus("current")
_RemOptSwPLP24hIntAverageTxBias_Type = Integer32
_RemOptSwPLP24hIntAverageTxBias_Object = MibTableColumn
remOptSwPLP24hIntAverageTxBias = _RemOptSwPLP24hIntAverageTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 2, 1, 2),
    _RemOptSwPLP24hIntAverageTxBias_Type()
)
remOptSwPLP24hIntAverageTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP24hIntAverageTxBias.setStatus("current")
_RemOptSwPLP24hIntMinTxBias_Type = Integer32
_RemOptSwPLP24hIntMinTxBias_Object = MibTableColumn
remOptSwPLP24hIntMinTxBias = _RemOptSwPLP24hIntMinTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 2, 1, 3),
    _RemOptSwPLP24hIntMinTxBias_Type()
)
remOptSwPLP24hIntMinTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP24hIntMinTxBias.setStatus("current")
_RemOptSwPLP24hIntMaxTxBias_Type = Integer32
_RemOptSwPLP24hIntMaxTxBias_Object = MibTableColumn
remOptSwPLP24hIntMaxTxBias = _RemOptSwPLP24hIntMaxTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 2, 1, 4),
    _RemOptSwPLP24hIntMaxTxBias_Type()
)
remOptSwPLP24hIntMaxTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP24hIntMaxTxBias.setStatus("current")
_RemOptSwPLP24hIntValidData_Type = TruthValue
_RemOptSwPLP24hIntValidData_Object = MibTableColumn
remOptSwPLP24hIntValidData = _RemOptSwPLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 2, 1, 5),
    _RemOptSwPLP24hIntValidData_Type()
)
remOptSwPLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP24hIntValidData.setStatus("current")
_RemOptSwPLP24hIntTimeStamp_Type = DateAndTime
_RemOptSwPLP24hIntTimeStamp_Object = MibTableColumn
remOptSwPLP24hIntTimeStamp = _RemOptSwPLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 2, 1, 6),
    _RemOptSwPLP24hIntTimeStamp_Type()
)
remOptSwPLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLP24hIntTimeStamp.setStatus("current")
_EdfaPLP15minIntTable_Object = MibTable
edfaPLP15minIntTable = _EdfaPLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3)
)
if mibBuilder.loadTexts:
    edfaPLP15minIntTable.setStatus("current")
_EdfaPLP15minIntEntry_Object = MibTableRow
edfaPLP15minIntEntry = _EdfaPLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1)
)
edfaPLP15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "edfaPLP15minIntNumber"),
)
if mibBuilder.loadTexts:
    edfaPLP15minIntEntry.setStatus("current")


class _EdfaPLP15minIntNumber_Type(Integer32):
    """Custom type edfaPLP15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EdfaPLP15minIntNumber_Type.__name__ = "Integer32"
_EdfaPLP15minIntNumber_Object = MibTableColumn
edfaPLP15minIntNumber = _EdfaPLP15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 1),
    _EdfaPLP15minIntNumber_Type()
)
edfaPLP15minIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntNumber.setStatus("current")
_EdfaPLP15minIntAveragePumpPower_Type = Integer32
_EdfaPLP15minIntAveragePumpPower_Object = MibTableColumn
edfaPLP15minIntAveragePumpPower = _EdfaPLP15minIntAveragePumpPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 2),
    _EdfaPLP15minIntAveragePumpPower_Type()
)
edfaPLP15minIntAveragePumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAveragePumpPower.setStatus("current")
_EdfaPLP15minIntMinPumpPower_Type = Integer32
_EdfaPLP15minIntMinPumpPower_Object = MibTableColumn
edfaPLP15minIntMinPumpPower = _EdfaPLP15minIntMinPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 3),
    _EdfaPLP15minIntMinPumpPower_Type()
)
edfaPLP15minIntMinPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinPumpPower.setStatus("current")
_EdfaPLP15minIntMaxPumpPower_Type = Integer32
_EdfaPLP15minIntMaxPumpPower_Object = MibTableColumn
edfaPLP15minIntMaxPumpPower = _EdfaPLP15minIntMaxPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 4),
    _EdfaPLP15minIntMaxPumpPower_Type()
)
edfaPLP15minIntMaxPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxPumpPower.setStatus("current")
_EdfaPLP15minIntAveragePumpCurrent_Type = Integer32
_EdfaPLP15minIntAveragePumpCurrent_Object = MibTableColumn
edfaPLP15minIntAveragePumpCurrent = _EdfaPLP15minIntAveragePumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 5),
    _EdfaPLP15minIntAveragePumpCurrent_Type()
)
edfaPLP15minIntAveragePumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAveragePumpCurrent.setStatus("current")
_EdfaPLP15minIntMinPumpCurrent_Type = Integer32
_EdfaPLP15minIntMinPumpCurrent_Object = MibTableColumn
edfaPLP15minIntMinPumpCurrent = _EdfaPLP15minIntMinPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 6),
    _EdfaPLP15minIntMinPumpCurrent_Type()
)
edfaPLP15minIntMinPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinPumpCurrent.setStatus("current")
_EdfaPLP15minIntMaxPumpCurrent_Type = Integer32
_EdfaPLP15minIntMaxPumpCurrent_Object = MibTableColumn
edfaPLP15minIntMaxPumpCurrent = _EdfaPLP15minIntMaxPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 7),
    _EdfaPLP15minIntMaxPumpCurrent_Type()
)
edfaPLP15minIntMaxPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxPumpCurrent.setStatus("current")
_EdfaPLP15minIntAverageTECCurrent_Type = Integer32
_EdfaPLP15minIntAverageTECCurrent_Object = MibTableColumn
edfaPLP15minIntAverageTECCurrent = _EdfaPLP15minIntAverageTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 8),
    _EdfaPLP15minIntAverageTECCurrent_Type()
)
edfaPLP15minIntAverageTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAverageTECCurrent.setStatus("current")
_EdfaPLP15minIntMinTECCurrent_Type = Integer32
_EdfaPLP15minIntMinTECCurrent_Object = MibTableColumn
edfaPLP15minIntMinTECCurrent = _EdfaPLP15minIntMinTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 9),
    _EdfaPLP15minIntMinTECCurrent_Type()
)
edfaPLP15minIntMinTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinTECCurrent.setStatus("current")
_EdfaPLP15minIntMaxTECCurrent_Type = Integer32
_EdfaPLP15minIntMaxTECCurrent_Object = MibTableColumn
edfaPLP15minIntMaxTECCurrent = _EdfaPLP15minIntMaxTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 10),
    _EdfaPLP15minIntMaxTECCurrent_Type()
)
edfaPLP15minIntMaxTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxTECCurrent.setStatus("current")
_EdfaPLP15minIntAveragePumpTxTemp_Type = Integer32
_EdfaPLP15minIntAveragePumpTxTemp_Object = MibTableColumn
edfaPLP15minIntAveragePumpTxTemp = _EdfaPLP15minIntAveragePumpTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 11),
    _EdfaPLP15minIntAveragePumpTxTemp_Type()
)
edfaPLP15minIntAveragePumpTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAveragePumpTxTemp.setStatus("current")
_EdfaPLP15minIntMinPumpTxTemp_Type = Integer32
_EdfaPLP15minIntMinPumpTxTemp_Object = MibTableColumn
edfaPLP15minIntMinPumpTxTemp = _EdfaPLP15minIntMinPumpTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 12),
    _EdfaPLP15minIntMinPumpTxTemp_Type()
)
edfaPLP15minIntMinPumpTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinPumpTxTemp.setStatus("current")
_EdfaPLP15minIntMaxPumpTxTemp_Type = Integer32
_EdfaPLP15minIntMaxPumpTxTemp_Object = MibTableColumn
edfaPLP15minIntMaxPumpTxTemp = _EdfaPLP15minIntMaxPumpTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 13),
    _EdfaPLP15minIntMaxPumpTxTemp_Type()
)
edfaPLP15minIntMaxPumpTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxPumpTxTemp.setStatus("current")
_EdfaPLP15minIntAverageSubModuleTemp_Type = Integer32
_EdfaPLP15minIntAverageSubModuleTemp_Object = MibTableColumn
edfaPLP15minIntAverageSubModuleTemp = _EdfaPLP15minIntAverageSubModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 14),
    _EdfaPLP15minIntAverageSubModuleTemp_Type()
)
edfaPLP15minIntAverageSubModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAverageSubModuleTemp.setStatus("current")
_EdfaPLP15minIntMinSubModuleTemp_Type = Integer32
_EdfaPLP15minIntMinSubModuleTemp_Object = MibTableColumn
edfaPLP15minIntMinSubModuleTemp = _EdfaPLP15minIntMinSubModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 15),
    _EdfaPLP15minIntMinSubModuleTemp_Type()
)
edfaPLP15minIntMinSubModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinSubModuleTemp.setStatus("current")
_EdfaPLP15minIntMaxSubModuleTemp_Type = Integer32
_EdfaPLP15minIntMaxSubModuleTemp_Object = MibTableColumn
edfaPLP15minIntMaxSubModuleTemp = _EdfaPLP15minIntMaxSubModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 16),
    _EdfaPLP15minIntMaxSubModuleTemp_Type()
)
edfaPLP15minIntMaxSubModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxSubModuleTemp.setStatus("current")
_EdfaPLP15minIntAverageOIP_Type = Integer32
_EdfaPLP15minIntAverageOIP_Object = MibTableColumn
edfaPLP15minIntAverageOIP = _EdfaPLP15minIntAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 17),
    _EdfaPLP15minIntAverageOIP_Type()
)
edfaPLP15minIntAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAverageOIP.setStatus("current")
_EdfaPLP15minIntMinOIP_Type = Integer32
_EdfaPLP15minIntMinOIP_Object = MibTableColumn
edfaPLP15minIntMinOIP = _EdfaPLP15minIntMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 18),
    _EdfaPLP15minIntMinOIP_Type()
)
edfaPLP15minIntMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinOIP.setStatus("current")
_EdfaPLP15minIntMaxOIP_Type = Integer32
_EdfaPLP15minIntMaxOIP_Object = MibTableColumn
edfaPLP15minIntMaxOIP = _EdfaPLP15minIntMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 19),
    _EdfaPLP15minIntMaxOIP_Type()
)
edfaPLP15minIntMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxOIP.setStatus("current")
_EdfaPLP15minIntAverageOOP_Type = Integer32
_EdfaPLP15minIntAverageOOP_Object = MibTableColumn
edfaPLP15minIntAverageOOP = _EdfaPLP15minIntAverageOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 20),
    _EdfaPLP15minIntAverageOOP_Type()
)
edfaPLP15minIntAverageOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAverageOOP.setStatus("current")
_EdfaPLP15minIntMinOOP_Type = Integer32
_EdfaPLP15minIntMinOOP_Object = MibTableColumn
edfaPLP15minIntMinOOP = _EdfaPLP15minIntMinOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 21),
    _EdfaPLP15minIntMinOOP_Type()
)
edfaPLP15minIntMinOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinOOP.setStatus("current")
_EdfaPLP15minIntMaxOOP_Type = Integer32
_EdfaPLP15minIntMaxOOP_Object = MibTableColumn
edfaPLP15minIntMaxOOP = _EdfaPLP15minIntMaxOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 22),
    _EdfaPLP15minIntMaxOOP_Type()
)
edfaPLP15minIntMaxOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxOOP.setStatus("current")
_EdfaPLP15minIntValidData_Type = TruthValue
_EdfaPLP15minIntValidData_Object = MibTableColumn
edfaPLP15minIntValidData = _EdfaPLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 23),
    _EdfaPLP15minIntValidData_Type()
)
edfaPLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntValidData.setStatus("current")
_EdfaPLP15minIntTimeStamp_Type = DateAndTime
_EdfaPLP15minIntTimeStamp_Object = MibTableColumn
edfaPLP15minIntTimeStamp = _EdfaPLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 3, 1, 24),
    _EdfaPLP15minIntTimeStamp_Type()
)
edfaPLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntTimeStamp.setStatus("current")
_EdfaPLP24hIntTable_Object = MibTable
edfaPLP24hIntTable = _EdfaPLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4)
)
if mibBuilder.loadTexts:
    edfaPLP24hIntTable.setStatus("current")
_EdfaPLP24hIntEntry_Object = MibTableRow
edfaPLP24hIntEntry = _EdfaPLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1)
)
edfaPLP24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "edfaPLP24hIntNumber"),
)
if mibBuilder.loadTexts:
    edfaPLP24hIntEntry.setStatus("current")


class _EdfaPLP24hIntNumber_Type(Integer32):
    """Custom type edfaPLP24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EdfaPLP24hIntNumber_Type.__name__ = "Integer32"
_EdfaPLP24hIntNumber_Object = MibTableColumn
edfaPLP24hIntNumber = _EdfaPLP24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 1),
    _EdfaPLP24hIntNumber_Type()
)
edfaPLP24hIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntNumber.setStatus("current")
_EdfaPLP24hIntAveragePumpPower_Type = Integer32
_EdfaPLP24hIntAveragePumpPower_Object = MibTableColumn
edfaPLP24hIntAveragePumpPower = _EdfaPLP24hIntAveragePumpPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 2),
    _EdfaPLP24hIntAveragePumpPower_Type()
)
edfaPLP24hIntAveragePumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAveragePumpPower.setStatus("current")
_EdfaPLP24hIntMinPumpPower_Type = Integer32
_EdfaPLP24hIntMinPumpPower_Object = MibTableColumn
edfaPLP24hIntMinPumpPower = _EdfaPLP24hIntMinPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 3),
    _EdfaPLP24hIntMinPumpPower_Type()
)
edfaPLP24hIntMinPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinPumpPower.setStatus("current")
_EdfaPLP24hIntMaxPumpPower_Type = Integer32
_EdfaPLP24hIntMaxPumpPower_Object = MibTableColumn
edfaPLP24hIntMaxPumpPower = _EdfaPLP24hIntMaxPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 4),
    _EdfaPLP24hIntMaxPumpPower_Type()
)
edfaPLP24hIntMaxPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxPumpPower.setStatus("current")
_EdfaPLP24hIntAveragePumpCurrent_Type = Integer32
_EdfaPLP24hIntAveragePumpCurrent_Object = MibTableColumn
edfaPLP24hIntAveragePumpCurrent = _EdfaPLP24hIntAveragePumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 5),
    _EdfaPLP24hIntAveragePumpCurrent_Type()
)
edfaPLP24hIntAveragePumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAveragePumpCurrent.setStatus("current")
_EdfaPLP24hIntMinPumpCurrent_Type = Integer32
_EdfaPLP24hIntMinPumpCurrent_Object = MibTableColumn
edfaPLP24hIntMinPumpCurrent = _EdfaPLP24hIntMinPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 6),
    _EdfaPLP24hIntMinPumpCurrent_Type()
)
edfaPLP24hIntMinPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinPumpCurrent.setStatus("current")
_EdfaPLP24hIntMaxPumpCurrent_Type = Integer32
_EdfaPLP24hIntMaxPumpCurrent_Object = MibTableColumn
edfaPLP24hIntMaxPumpCurrent = _EdfaPLP24hIntMaxPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 7),
    _EdfaPLP24hIntMaxPumpCurrent_Type()
)
edfaPLP24hIntMaxPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxPumpCurrent.setStatus("current")
_EdfaPLP24hIntAverageTECCurrent_Type = Integer32
_EdfaPLP24hIntAverageTECCurrent_Object = MibTableColumn
edfaPLP24hIntAverageTECCurrent = _EdfaPLP24hIntAverageTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 8),
    _EdfaPLP24hIntAverageTECCurrent_Type()
)
edfaPLP24hIntAverageTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAverageTECCurrent.setStatus("current")
_EdfaPLP24hIntMinTECCurrent_Type = Integer32
_EdfaPLP24hIntMinTECCurrent_Object = MibTableColumn
edfaPLP24hIntMinTECCurrent = _EdfaPLP24hIntMinTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 9),
    _EdfaPLP24hIntMinTECCurrent_Type()
)
edfaPLP24hIntMinTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinTECCurrent.setStatus("current")
_EdfaPLP24hIntMaxTECCurrent_Type = Integer32
_EdfaPLP24hIntMaxTECCurrent_Object = MibTableColumn
edfaPLP24hIntMaxTECCurrent = _EdfaPLP24hIntMaxTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 10),
    _EdfaPLP24hIntMaxTECCurrent_Type()
)
edfaPLP24hIntMaxTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxTECCurrent.setStatus("current")
_EdfaPLP24hIntAveragePumpTxTemp_Type = Integer32
_EdfaPLP24hIntAveragePumpTxTemp_Object = MibTableColumn
edfaPLP24hIntAveragePumpTxTemp = _EdfaPLP24hIntAveragePumpTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 11),
    _EdfaPLP24hIntAveragePumpTxTemp_Type()
)
edfaPLP24hIntAveragePumpTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAveragePumpTxTemp.setStatus("current")
_EdfaPLP24hIntMinPumpTxTemp_Type = Integer32
_EdfaPLP24hIntMinPumpTxTemp_Object = MibTableColumn
edfaPLP24hIntMinPumpTxTemp = _EdfaPLP24hIntMinPumpTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 12),
    _EdfaPLP24hIntMinPumpTxTemp_Type()
)
edfaPLP24hIntMinPumpTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinPumpTxTemp.setStatus("current")
_EdfaPLP24hIntMaxPumpTxTemp_Type = Integer32
_EdfaPLP24hIntMaxPumpTxTemp_Object = MibTableColumn
edfaPLP24hIntMaxPumpTxTemp = _EdfaPLP24hIntMaxPumpTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 13),
    _EdfaPLP24hIntMaxPumpTxTemp_Type()
)
edfaPLP24hIntMaxPumpTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxPumpTxTemp.setStatus("current")
_EdfaPLP24hIntAverageSubModuleTemp_Type = Integer32
_EdfaPLP24hIntAverageSubModuleTemp_Object = MibTableColumn
edfaPLP24hIntAverageSubModuleTemp = _EdfaPLP24hIntAverageSubModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 14),
    _EdfaPLP24hIntAverageSubModuleTemp_Type()
)
edfaPLP24hIntAverageSubModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAverageSubModuleTemp.setStatus("current")
_EdfaPLP24hIntMinSubModuleTemp_Type = Integer32
_EdfaPLP24hIntMinSubModuleTemp_Object = MibTableColumn
edfaPLP24hIntMinSubModuleTemp = _EdfaPLP24hIntMinSubModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 15),
    _EdfaPLP24hIntMinSubModuleTemp_Type()
)
edfaPLP24hIntMinSubModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinSubModuleTemp.setStatus("current")
_EdfaPLP24hIntMaxSubModuleTemp_Type = Integer32
_EdfaPLP24hIntMaxSubModuleTemp_Object = MibTableColumn
edfaPLP24hIntMaxSubModuleTemp = _EdfaPLP24hIntMaxSubModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 16),
    _EdfaPLP24hIntMaxSubModuleTemp_Type()
)
edfaPLP24hIntMaxSubModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxSubModuleTemp.setStatus("current")
_EdfaPLP24hIntAverageOIP_Type = Integer32
_EdfaPLP24hIntAverageOIP_Object = MibTableColumn
edfaPLP24hIntAverageOIP = _EdfaPLP24hIntAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 17),
    _EdfaPLP24hIntAverageOIP_Type()
)
edfaPLP24hIntAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAverageOIP.setStatus("current")
_EdfaPLP24hIntMinOIP_Type = Integer32
_EdfaPLP24hIntMinOIP_Object = MibTableColumn
edfaPLP24hIntMinOIP = _EdfaPLP24hIntMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 18),
    _EdfaPLP24hIntMinOIP_Type()
)
edfaPLP24hIntMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinOIP.setStatus("current")
_EdfaPLP24hIntMaxOIP_Type = Integer32
_EdfaPLP24hIntMaxOIP_Object = MibTableColumn
edfaPLP24hIntMaxOIP = _EdfaPLP24hIntMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 19),
    _EdfaPLP24hIntMaxOIP_Type()
)
edfaPLP24hIntMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxOIP.setStatus("current")
_EdfaPLP24hIntAverageOOP_Type = Integer32
_EdfaPLP24hIntAverageOOP_Object = MibTableColumn
edfaPLP24hIntAverageOOP = _EdfaPLP24hIntAverageOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 20),
    _EdfaPLP24hIntAverageOOP_Type()
)
edfaPLP24hIntAverageOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAverageOOP.setStatus("current")
_EdfaPLP24hIntMinOOP_Type = Integer32
_EdfaPLP24hIntMinOOP_Object = MibTableColumn
edfaPLP24hIntMinOOP = _EdfaPLP24hIntMinOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 21),
    _EdfaPLP24hIntMinOOP_Type()
)
edfaPLP24hIntMinOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinOOP.setStatus("current")
_EdfaPLP24hIntMaxOOP_Type = Integer32
_EdfaPLP24hIntMaxOOP_Object = MibTableColumn
edfaPLP24hIntMaxOOP = _EdfaPLP24hIntMaxOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 22),
    _EdfaPLP24hIntMaxOOP_Type()
)
edfaPLP24hIntMaxOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxOOP.setStatus("current")
_EdfaPLP24hIntValidData_Type = TruthValue
_EdfaPLP24hIntValidData_Object = MibTableColumn
edfaPLP24hIntValidData = _EdfaPLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 23),
    _EdfaPLP24hIntValidData_Type()
)
edfaPLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntValidData.setStatus("current")
_EdfaPLP24hIntTimeStamp_Type = DateAndTime
_EdfaPLP24hIntTimeStamp_Object = MibTableColumn
edfaPLP24hIntTimeStamp = _EdfaPLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 4, 1, 24),
    _EdfaPLP24hIntTimeStamp_Type()
)
edfaPLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntTimeStamp.setStatus("current")
_InterfaceTTPLP15minIntTable_Object = MibTable
interfaceTTPLP15minIntTable = _InterfaceTTPLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5)
)
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntTable.setStatus("current")
_InterfaceTTPLP15minIntEntry_Object = MibTableRow
interfaceTTPLP15minIntEntry = _InterfaceTTPLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1)
)
interfaceTTPLP15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfaceTTPLP15minIntNumber"),
)
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntEntry.setStatus("current")


class _InterfaceTTPLP15minIntNumber_Type(Integer32):
    """Custom type interfaceTTPLP15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_InterfaceTTPLP15minIntNumber_Type.__name__ = "Integer32"
_InterfaceTTPLP15minIntNumber_Object = MibTableColumn
interfaceTTPLP15minIntNumber = _InterfaceTTPLP15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 1),
    _InterfaceTTPLP15minIntNumber_Type()
)
interfaceTTPLP15minIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntNumber.setStatus("current")
_InterfaceTTPLP15minIntAverageTxBias_Type = Integer32
_InterfaceTTPLP15minIntAverageTxBias_Object = MibTableColumn
interfaceTTPLP15minIntAverageTxBias = _InterfaceTTPLP15minIntAverageTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 2),
    _InterfaceTTPLP15minIntAverageTxBias_Type()
)
interfaceTTPLP15minIntAverageTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntAverageTxBias.setStatus("current")
_InterfaceTTPLP15minIntMinTxBias_Type = Integer32
_InterfaceTTPLP15minIntMinTxBias_Object = MibTableColumn
interfaceTTPLP15minIntMinTxBias = _InterfaceTTPLP15minIntMinTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 3),
    _InterfaceTTPLP15minIntMinTxBias_Type()
)
interfaceTTPLP15minIntMinTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntMinTxBias.setStatus("current")
_InterfaceTTPLP15minIntMaxTxBias_Type = Integer32
_InterfaceTTPLP15minIntMaxTxBias_Object = MibTableColumn
interfaceTTPLP15minIntMaxTxBias = _InterfaceTTPLP15minIntMaxTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 4),
    _InterfaceTTPLP15minIntMaxTxBias_Type()
)
interfaceTTPLP15minIntMaxTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntMaxTxBias.setStatus("current")
_InterfaceTTPLP15minIntAverageTxLaserTemp_Type = Integer32
_InterfaceTTPLP15minIntAverageTxLaserTemp_Object = MibTableColumn
interfaceTTPLP15minIntAverageTxLaserTemp = _InterfaceTTPLP15minIntAverageTxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 5),
    _InterfaceTTPLP15minIntAverageTxLaserTemp_Type()
)
interfaceTTPLP15minIntAverageTxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntAverageTxLaserTemp.setStatus("current")
_InterfaceTTPLP15minIntMinTxLaserTemp_Type = Integer32
_InterfaceTTPLP15minIntMinTxLaserTemp_Object = MibTableColumn
interfaceTTPLP15minIntMinTxLaserTemp = _InterfaceTTPLP15minIntMinTxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 6),
    _InterfaceTTPLP15minIntMinTxLaserTemp_Type()
)
interfaceTTPLP15minIntMinTxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntMinTxLaserTemp.setStatus("current")
_InterfaceTTPLP15minIntMaxTxLaserTemp_Type = Integer32
_InterfaceTTPLP15minIntMaxTxLaserTemp_Object = MibTableColumn
interfaceTTPLP15minIntMaxTxLaserTemp = _InterfaceTTPLP15minIntMaxTxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 7),
    _InterfaceTTPLP15minIntMaxTxLaserTemp_Type()
)
interfaceTTPLP15minIntMaxTxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntMaxTxLaserTemp.setStatus("current")
_InterfaceTTPLP15minIntAverageRxOIP_Type = Integer32
_InterfaceTTPLP15minIntAverageRxOIP_Object = MibTableColumn
interfaceTTPLP15minIntAverageRxOIP = _InterfaceTTPLP15minIntAverageRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 8),
    _InterfaceTTPLP15minIntAverageRxOIP_Type()
)
interfaceTTPLP15minIntAverageRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntAverageRxOIP.setStatus("current")
_InterfaceTTPLP15minIntMinRxOIP_Type = Integer32
_InterfaceTTPLP15minIntMinRxOIP_Object = MibTableColumn
interfaceTTPLP15minIntMinRxOIP = _InterfaceTTPLP15minIntMinRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 9),
    _InterfaceTTPLP15minIntMinRxOIP_Type()
)
interfaceTTPLP15minIntMinRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntMinRxOIP.setStatus("current")
_InterfaceTTPLP15minIntMaxRxOIP_Type = Integer32
_InterfaceTTPLP15minIntMaxRxOIP_Object = MibTableColumn
interfaceTTPLP15minIntMaxRxOIP = _InterfaceTTPLP15minIntMaxRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 10),
    _InterfaceTTPLP15minIntMaxRxOIP_Type()
)
interfaceTTPLP15minIntMaxRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntMaxRxOIP.setStatus("current")
_InterfaceTTPLP15minIntAverageRxUAPD_Type = Integer32
_InterfaceTTPLP15minIntAverageRxUAPD_Object = MibTableColumn
interfaceTTPLP15minIntAverageRxUAPD = _InterfaceTTPLP15minIntAverageRxUAPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 11),
    _InterfaceTTPLP15minIntAverageRxUAPD_Type()
)
interfaceTTPLP15minIntAverageRxUAPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntAverageRxUAPD.setStatus("current")
_InterfaceTTPLP15minIntMinRxUAPD_Type = Integer32
_InterfaceTTPLP15minIntMinRxUAPD_Object = MibTableColumn
interfaceTTPLP15minIntMinRxUAPD = _InterfaceTTPLP15minIntMinRxUAPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 12),
    _InterfaceTTPLP15minIntMinRxUAPD_Type()
)
interfaceTTPLP15minIntMinRxUAPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntMinRxUAPD.setStatus("current")
_InterfaceTTPLP15minIntMaxRxUAPD_Type = Integer32
_InterfaceTTPLP15minIntMaxRxUAPD_Object = MibTableColumn
interfaceTTPLP15minIntMaxRxUAPD = _InterfaceTTPLP15minIntMaxRxUAPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 13),
    _InterfaceTTPLP15minIntMaxRxUAPD_Type()
)
interfaceTTPLP15minIntMaxRxUAPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntMaxRxUAPD.setStatus("current")
_InterfaceTTPLP15minIntValidData_Type = TruthValue
_InterfaceTTPLP15minIntValidData_Object = MibTableColumn
interfaceTTPLP15minIntValidData = _InterfaceTTPLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 14),
    _InterfaceTTPLP15minIntValidData_Type()
)
interfaceTTPLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntValidData.setStatus("current")
_InterfaceTTPLP15minIntTimeStamp_Type = DateAndTime
_InterfaceTTPLP15minIntTimeStamp_Object = MibTableColumn
interfaceTTPLP15minIntTimeStamp = _InterfaceTTPLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 5, 1, 15),
    _InterfaceTTPLP15minIntTimeStamp_Type()
)
interfaceTTPLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP15minIntTimeStamp.setStatus("current")
_InterfaceTTPLP24hIntTable_Object = MibTable
interfaceTTPLP24hIntTable = _InterfaceTTPLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6)
)
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntTable.setStatus("current")
_InterfaceTTPLP24hIntEntry_Object = MibTableRow
interfaceTTPLP24hIntEntry = _InterfaceTTPLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1)
)
interfaceTTPLP24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfaceTTPLP24hIntNumber"),
)
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntEntry.setStatus("current")


class _InterfaceTTPLP24hIntNumber_Type(Integer32):
    """Custom type interfaceTTPLP24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_InterfaceTTPLP24hIntNumber_Type.__name__ = "Integer32"
_InterfaceTTPLP24hIntNumber_Object = MibTableColumn
interfaceTTPLP24hIntNumber = _InterfaceTTPLP24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 1),
    _InterfaceTTPLP24hIntNumber_Type()
)
interfaceTTPLP24hIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntNumber.setStatus("current")
_InterfaceTTPLP24hIntAverageTxBias_Type = Integer32
_InterfaceTTPLP24hIntAverageTxBias_Object = MibTableColumn
interfaceTTPLP24hIntAverageTxBias = _InterfaceTTPLP24hIntAverageTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 2),
    _InterfaceTTPLP24hIntAverageTxBias_Type()
)
interfaceTTPLP24hIntAverageTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntAverageTxBias.setStatus("current")
_InterfaceTTPLP24hIntMinTxBias_Type = Integer32
_InterfaceTTPLP24hIntMinTxBias_Object = MibTableColumn
interfaceTTPLP24hIntMinTxBias = _InterfaceTTPLP24hIntMinTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 3),
    _InterfaceTTPLP24hIntMinTxBias_Type()
)
interfaceTTPLP24hIntMinTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntMinTxBias.setStatus("current")
_InterfaceTTPLP24hIntMaxTxBias_Type = Integer32
_InterfaceTTPLP24hIntMaxTxBias_Object = MibTableColumn
interfaceTTPLP24hIntMaxTxBias = _InterfaceTTPLP24hIntMaxTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 4),
    _InterfaceTTPLP24hIntMaxTxBias_Type()
)
interfaceTTPLP24hIntMaxTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntMaxTxBias.setStatus("current")
_InterfaceTTPLP24hIntAverageTxLaserTemp_Type = Integer32
_InterfaceTTPLP24hIntAverageTxLaserTemp_Object = MibTableColumn
interfaceTTPLP24hIntAverageTxLaserTemp = _InterfaceTTPLP24hIntAverageTxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 5),
    _InterfaceTTPLP24hIntAverageTxLaserTemp_Type()
)
interfaceTTPLP24hIntAverageTxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntAverageTxLaserTemp.setStatus("current")
_InterfaceTTPLP24hIntMinTxLaserTemp_Type = Integer32
_InterfaceTTPLP24hIntMinTxLaserTemp_Object = MibTableColumn
interfaceTTPLP24hIntMinTxLaserTemp = _InterfaceTTPLP24hIntMinTxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 6),
    _InterfaceTTPLP24hIntMinTxLaserTemp_Type()
)
interfaceTTPLP24hIntMinTxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntMinTxLaserTemp.setStatus("current")
_InterfaceTTPLP24hIntMaxTxLaserTemp_Type = Integer32
_InterfaceTTPLP24hIntMaxTxLaserTemp_Object = MibTableColumn
interfaceTTPLP24hIntMaxTxLaserTemp = _InterfaceTTPLP24hIntMaxTxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 7),
    _InterfaceTTPLP24hIntMaxTxLaserTemp_Type()
)
interfaceTTPLP24hIntMaxTxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntMaxTxLaserTemp.setStatus("current")
_InterfaceTTPLP24hIntAverageRxOIP_Type = Integer32
_InterfaceTTPLP24hIntAverageRxOIP_Object = MibTableColumn
interfaceTTPLP24hIntAverageRxOIP = _InterfaceTTPLP24hIntAverageRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 8),
    _InterfaceTTPLP24hIntAverageRxOIP_Type()
)
interfaceTTPLP24hIntAverageRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntAverageRxOIP.setStatus("current")
_InterfaceTTPLP24hIntMinRxOIP_Type = Integer32
_InterfaceTTPLP24hIntMinRxOIP_Object = MibTableColumn
interfaceTTPLP24hIntMinRxOIP = _InterfaceTTPLP24hIntMinRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 9),
    _InterfaceTTPLP24hIntMinRxOIP_Type()
)
interfaceTTPLP24hIntMinRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntMinRxOIP.setStatus("current")
_InterfaceTTPLP24hIntMaxRxOIP_Type = Integer32
_InterfaceTTPLP24hIntMaxRxOIP_Object = MibTableColumn
interfaceTTPLP24hIntMaxRxOIP = _InterfaceTTPLP24hIntMaxRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 10),
    _InterfaceTTPLP24hIntMaxRxOIP_Type()
)
interfaceTTPLP24hIntMaxRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntMaxRxOIP.setStatus("current")
_InterfaceTTPLP24hIntAverageRxUAPD_Type = Integer32
_InterfaceTTPLP24hIntAverageRxUAPD_Object = MibTableColumn
interfaceTTPLP24hIntAverageRxUAPD = _InterfaceTTPLP24hIntAverageRxUAPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 11),
    _InterfaceTTPLP24hIntAverageRxUAPD_Type()
)
interfaceTTPLP24hIntAverageRxUAPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntAverageRxUAPD.setStatus("current")
_InterfaceTTPLP24hIntMinRxUAPD_Type = Integer32
_InterfaceTTPLP24hIntMinRxUAPD_Object = MibTableColumn
interfaceTTPLP24hIntMinRxUAPD = _InterfaceTTPLP24hIntMinRxUAPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 12),
    _InterfaceTTPLP24hIntMinRxUAPD_Type()
)
interfaceTTPLP24hIntMinRxUAPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntMinRxUAPD.setStatus("current")
_InterfaceTTPLP24hIntMaxRxUAPD_Type = Integer32
_InterfaceTTPLP24hIntMaxRxUAPD_Object = MibTableColumn
interfaceTTPLP24hIntMaxRxUAPD = _InterfaceTTPLP24hIntMaxRxUAPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 13),
    _InterfaceTTPLP24hIntMaxRxUAPD_Type()
)
interfaceTTPLP24hIntMaxRxUAPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntMaxRxUAPD.setStatus("current")
_InterfaceTTPLP24hIntValidData_Type = TruthValue
_InterfaceTTPLP24hIntValidData_Object = MibTableColumn
interfaceTTPLP24hIntValidData = _InterfaceTTPLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 14),
    _InterfaceTTPLP24hIntValidData_Type()
)
interfaceTTPLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntValidData.setStatus("current")
_InterfaceTTPLP24hIntTimeStamp_Type = DateAndTime
_InterfaceTTPLP24hIntTimeStamp_Object = MibTableColumn
interfaceTTPLP24hIntTimeStamp = _InterfaceTTPLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 6, 1, 15),
    _InterfaceTTPLP24hIntTimeStamp_Type()
)
interfaceTTPLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLP24hIntTimeStamp.setStatus("current")
_EccmPLP15minIntTable_Object = MibTable
eccmPLP15minIntTable = _EccmPLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 7)
)
if mibBuilder.loadTexts:
    eccmPLP15minIntTable.setStatus("current")
_EccmPLP15minIntEntry_Object = MibTableRow
eccmPLP15minIntEntry = _EccmPLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 7, 1)
)
eccmPLP15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "eccmPLP15minIntNumber"),
)
if mibBuilder.loadTexts:
    eccmPLP15minIntEntry.setStatus("current")


class _EccmPLP15minIntNumber_Type(Integer32):
    """Custom type eccmPLP15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EccmPLP15minIntNumber_Type.__name__ = "Integer32"
_EccmPLP15minIntNumber_Object = MibTableColumn
eccmPLP15minIntNumber = _EccmPLP15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 7, 1, 1),
    _EccmPLP15minIntNumber_Type()
)
eccmPLP15minIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP15minIntNumber.setStatus("current")
_EccmPLP15minIntAverageRxOIP_Type = Integer32
_EccmPLP15minIntAverageRxOIP_Object = MibTableColumn
eccmPLP15minIntAverageRxOIP = _EccmPLP15minIntAverageRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 7, 1, 2),
    _EccmPLP15minIntAverageRxOIP_Type()
)
eccmPLP15minIntAverageRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP15minIntAverageRxOIP.setStatus("current")
_EccmPLP15minIntMinRxOIP_Type = Integer32
_EccmPLP15minIntMinRxOIP_Object = MibTableColumn
eccmPLP15minIntMinRxOIP = _EccmPLP15minIntMinRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 7, 1, 3),
    _EccmPLP15minIntMinRxOIP_Type()
)
eccmPLP15minIntMinRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP15minIntMinRxOIP.setStatus("current")
_EccmPLP15minIntMaxRxOIP_Type = Integer32
_EccmPLP15minIntMaxRxOIP_Object = MibTableColumn
eccmPLP15minIntMaxRxOIP = _EccmPLP15minIntMaxRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 7, 1, 4),
    _EccmPLP15minIntMaxRxOIP_Type()
)
eccmPLP15minIntMaxRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP15minIntMaxRxOIP.setStatus("current")
_EccmPLP15minIntValidData_Type = TruthValue
_EccmPLP15minIntValidData_Object = MibTableColumn
eccmPLP15minIntValidData = _EccmPLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 7, 1, 5),
    _EccmPLP15minIntValidData_Type()
)
eccmPLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP15minIntValidData.setStatus("current")
_EccmPLP15minIntTimeStamp_Type = DateAndTime
_EccmPLP15minIntTimeStamp_Object = MibTableColumn
eccmPLP15minIntTimeStamp = _EccmPLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 7, 1, 6),
    _EccmPLP15minIntTimeStamp_Type()
)
eccmPLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP15minIntTimeStamp.setStatus("current")
_EccmPLP24hIntTable_Object = MibTable
eccmPLP24hIntTable = _EccmPLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 8)
)
if mibBuilder.loadTexts:
    eccmPLP24hIntTable.setStatus("current")
_EccmPLP24hIntEntry_Object = MibTableRow
eccmPLP24hIntEntry = _EccmPLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 8, 1)
)
eccmPLP24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "eccmPLP24hIntNumber"),
)
if mibBuilder.loadTexts:
    eccmPLP24hIntEntry.setStatus("current")


class _EccmPLP24hIntNumber_Type(Integer32):
    """Custom type eccmPLP24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EccmPLP24hIntNumber_Type.__name__ = "Integer32"
_EccmPLP24hIntNumber_Object = MibTableColumn
eccmPLP24hIntNumber = _EccmPLP24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 8, 1, 1),
    _EccmPLP24hIntNumber_Type()
)
eccmPLP24hIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP24hIntNumber.setStatus("current")
_EccmPLP24hIntAverageRxOIP_Type = Integer32
_EccmPLP24hIntAverageRxOIP_Object = MibTableColumn
eccmPLP24hIntAverageRxOIP = _EccmPLP24hIntAverageRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 8, 1, 2),
    _EccmPLP24hIntAverageRxOIP_Type()
)
eccmPLP24hIntAverageRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP24hIntAverageRxOIP.setStatus("current")
_EccmPLP24hIntMinRxOIP_Type = Integer32
_EccmPLP24hIntMinRxOIP_Object = MibTableColumn
eccmPLP24hIntMinRxOIP = _EccmPLP24hIntMinRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 8, 1, 3),
    _EccmPLP24hIntMinRxOIP_Type()
)
eccmPLP24hIntMinRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP24hIntMinRxOIP.setStatus("current")
_EccmPLP24hIntMaxRxOIP_Type = Integer32
_EccmPLP24hIntMaxRxOIP_Object = MibTableColumn
eccmPLP24hIntMaxRxOIP = _EccmPLP24hIntMaxRxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 8, 1, 4),
    _EccmPLP24hIntMaxRxOIP_Type()
)
eccmPLP24hIntMaxRxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP24hIntMaxRxOIP.setStatus("current")
_EccmPLP24hIntValidData_Type = TruthValue
_EccmPLP24hIntValidData_Object = MibTableColumn
eccmPLP24hIntValidData = _EccmPLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 8, 1, 5),
    _EccmPLP24hIntValidData_Type()
)
eccmPLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP24hIntValidData.setStatus("current")
_EccmPLP24hIntTimeStamp_Type = DateAndTime
_EccmPLP24hIntTimeStamp_Object = MibTableColumn
eccmPLP24hIntTimeStamp = _EccmPLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 8, 1, 6),
    _EccmPLP24hIntTimeStamp_Type()
)
eccmPLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLP24hIntTimeStamp.setStatus("current")
_ApsPLP15minIntTable_Object = MibTable
apsPLP15minIntTable = _ApsPLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10)
)
if mibBuilder.loadTexts:
    apsPLP15minIntTable.setStatus("current")
_ApsPLP15minIntEntry_Object = MibTableRow
apsPLP15minIntEntry = _ApsPLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1)
)
apsPLP15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "apsPLP15minIntNumber"),
)
if mibBuilder.loadTexts:
    apsPLP15minIntEntry.setStatus("current")


class _ApsPLP15minIntNumber_Type(Integer32):
    """Custom type apsPLP15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApsPLP15minIntNumber_Type.__name__ = "Integer32"
_ApsPLP15minIntNumber_Object = MibTableColumn
apsPLP15minIntNumber = _ApsPLP15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 1),
    _ApsPLP15minIntNumber_Type()
)
apsPLP15minIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsPLP15minIntNumber.setStatus("current")
_ApsPLP15minIntAverageOIPLoad_Type = Integer32
_ApsPLP15minIntAverageOIPLoad_Object = MibTableColumn
apsPLP15minIntAverageOIPLoad = _ApsPLP15minIntAverageOIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 2),
    _ApsPLP15minIntAverageOIPLoad_Type()
)
apsPLP15minIntAverageOIPLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP15minIntAverageOIPLoad.setStatus("current")
_ApsPLP15minIntMinOIPLoad_Type = Integer32
_ApsPLP15minIntMinOIPLoad_Object = MibTableColumn
apsPLP15minIntMinOIPLoad = _ApsPLP15minIntMinOIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 3),
    _ApsPLP15minIntMinOIPLoad_Type()
)
apsPLP15minIntMinOIPLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP15minIntMinOIPLoad.setStatus("current")
_ApsPLP15minIntMaxOIPLoad_Type = Integer32
_ApsPLP15minIntMaxOIPLoad_Object = MibTableColumn
apsPLP15minIntMaxOIPLoad = _ApsPLP15minIntMaxOIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 4),
    _ApsPLP15minIntMaxOIPLoad_Type()
)
apsPLP15minIntMaxOIPLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP15minIntMaxOIPLoad.setStatus("current")
_ApsPLP15minIntAverageOipOsc_Type = Integer32
_ApsPLP15minIntAverageOipOsc_Object = MibTableColumn
apsPLP15minIntAverageOipOsc = _ApsPLP15minIntAverageOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 5),
    _ApsPLP15minIntAverageOipOsc_Type()
)
apsPLP15minIntAverageOipOsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP15minIntAverageOipOsc.setStatus("current")
_ApsPLP15minIntMinOipOsc_Type = Integer32
_ApsPLP15minIntMinOipOsc_Object = MibTableColumn
apsPLP15minIntMinOipOsc = _ApsPLP15minIntMinOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 6),
    _ApsPLP15minIntMinOipOsc_Type()
)
apsPLP15minIntMinOipOsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP15minIntMinOipOsc.setStatus("current")
_ApsPLP15minIntMaxOipOsc_Type = Integer32
_ApsPLP15minIntMaxOipOsc_Object = MibTableColumn
apsPLP15minIntMaxOipOsc = _ApsPLP15minIntMaxOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 7),
    _ApsPLP15minIntMaxOipOsc_Type()
)
apsPLP15minIntMaxOipOsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP15minIntMaxOipOsc.setStatus("current")
_ApsPLP15minIntValidData_Type = TruthValue
_ApsPLP15minIntValidData_Object = MibTableColumn
apsPLP15minIntValidData = _ApsPLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 8),
    _ApsPLP15minIntValidData_Type()
)
apsPLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP15minIntValidData.setStatus("current")
_ApsPLP15minIntTimeStamp_Type = DateAndTime
_ApsPLP15minIntTimeStamp_Object = MibTableColumn
apsPLP15minIntTimeStamp = _ApsPLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 10, 1, 9),
    _ApsPLP15minIntTimeStamp_Type()
)
apsPLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP15minIntTimeStamp.setStatus("current")
_ApsPLP24hIntTable_Object = MibTable
apsPLP24hIntTable = _ApsPLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11)
)
if mibBuilder.loadTexts:
    apsPLP24hIntTable.setStatus("current")
_ApsPLP24hIntEntry_Object = MibTableRow
apsPLP24hIntEntry = _ApsPLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1)
)
apsPLP24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "apsPLP24hIntNumber"),
)
if mibBuilder.loadTexts:
    apsPLP24hIntEntry.setStatus("current")


class _ApsPLP24hIntNumber_Type(Integer32):
    """Custom type apsPLP24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApsPLP24hIntNumber_Type.__name__ = "Integer32"
_ApsPLP24hIntNumber_Object = MibTableColumn
apsPLP24hIntNumber = _ApsPLP24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 1),
    _ApsPLP24hIntNumber_Type()
)
apsPLP24hIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsPLP24hIntNumber.setStatus("current")
_ApsPLP24hIntAverageOIPLoad_Type = Integer32
_ApsPLP24hIntAverageOIPLoad_Object = MibTableColumn
apsPLP24hIntAverageOIPLoad = _ApsPLP24hIntAverageOIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 2),
    _ApsPLP24hIntAverageOIPLoad_Type()
)
apsPLP24hIntAverageOIPLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP24hIntAverageOIPLoad.setStatus("current")
_ApsPLP24hIntMinOIPLoad_Type = Integer32
_ApsPLP24hIntMinOIPLoad_Object = MibTableColumn
apsPLP24hIntMinOIPLoad = _ApsPLP24hIntMinOIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 3),
    _ApsPLP24hIntMinOIPLoad_Type()
)
apsPLP24hIntMinOIPLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP24hIntMinOIPLoad.setStatus("current")
_ApsPLP24hIntMaxOIPLoad_Type = Integer32
_ApsPLP24hIntMaxOIPLoad_Object = MibTableColumn
apsPLP24hIntMaxOIPLoad = _ApsPLP24hIntMaxOIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 4),
    _ApsPLP24hIntMaxOIPLoad_Type()
)
apsPLP24hIntMaxOIPLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP24hIntMaxOIPLoad.setStatus("current")
_ApsPLP24hIntAverageOipOsc_Type = Integer32
_ApsPLP24hIntAverageOipOsc_Object = MibTableColumn
apsPLP24hIntAverageOipOsc = _ApsPLP24hIntAverageOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 5),
    _ApsPLP24hIntAverageOipOsc_Type()
)
apsPLP24hIntAverageOipOsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP24hIntAverageOipOsc.setStatus("current")
_ApsPLP24hIntMinOipOsc_Type = Integer32
_ApsPLP24hIntMinOipOsc_Object = MibTableColumn
apsPLP24hIntMinOipOsc = _ApsPLP24hIntMinOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 6),
    _ApsPLP24hIntMinOipOsc_Type()
)
apsPLP24hIntMinOipOsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP24hIntMinOipOsc.setStatus("current")
_ApsPLP24hIntMaxOipOsc_Type = Integer32
_ApsPLP24hIntMaxOipOsc_Object = MibTableColumn
apsPLP24hIntMaxOipOsc = _ApsPLP24hIntMaxOipOsc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 7),
    _ApsPLP24hIntMaxOipOsc_Type()
)
apsPLP24hIntMaxOipOsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP24hIntMaxOipOsc.setStatus("current")
_ApsPLP24hIntValidData_Type = TruthValue
_ApsPLP24hIntValidData_Object = MibTableColumn
apsPLP24hIntValidData = _ApsPLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 8),
    _ApsPLP24hIntValidData_Type()
)
apsPLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP24hIntValidData.setStatus("current")
_ApsPLP24hIntTimeStamp_Type = DateAndTime
_ApsPLP24hIntTimeStamp_Object = MibTableColumn
apsPLP24hIntTimeStamp = _ApsPLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 2, 11, 1, 9),
    _ApsPLP24hIntTimeStamp_Type()
)
apsPLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLP24hIntTimeStamp.setStatus("current")
_PhysicalLayerAlarmMon_ObjectIdentity = ObjectIdentity
physicalLayerAlarmMon = _PhysicalLayerAlarmMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3)
)
_RemOptSwPLA15minIntTable_Object = MibTable
remOptSwPLA15minIntTable = _RemOptSwPLA15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    remOptSwPLA15minIntTable.setStatus("current")
_RemOptSwPLA15minIntEntry_Object = MibTableRow
remOptSwPLA15minIntEntry = _RemOptSwPLA15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 1, 1)
)
remOptSwPLA15minIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "remOptSwPLA15minIntNumber"),
)
if mibBuilder.loadTexts:
    remOptSwPLA15minIntEntry.setStatus("current")


class _RemOptSwPLA15minIntNumber_Type(Integer32):
    """Custom type remOptSwPLA15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RemOptSwPLA15minIntNumber_Type.__name__ = "Integer32"
_RemOptSwPLA15minIntNumber_Object = MibTableColumn
remOptSwPLA15minIntNumber = _RemOptSwPLA15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 1, 1, 1),
    _RemOptSwPLA15minIntNumber_Type()
)
remOptSwPLA15minIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA15minIntNumber.setStatus("current")
_RemOptSwPLA15minIntLineARxLOS_Type = Gauge32
_RemOptSwPLA15minIntLineARxLOS_Object = MibTableColumn
remOptSwPLA15minIntLineARxLOS = _RemOptSwPLA15minIntLineARxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 1, 1, 2),
    _RemOptSwPLA15minIntLineARxLOS_Type()
)
remOptSwPLA15minIntLineARxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA15minIntLineARxLOS.setStatus("current")
_RemOptSwPLA15minIntLineBRxLOS_Type = Gauge32
_RemOptSwPLA15minIntLineBRxLOS_Object = MibTableColumn
remOptSwPLA15minIntLineBRxLOS = _RemOptSwPLA15minIntLineBRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 1, 1, 3),
    _RemOptSwPLA15minIntLineBRxLOS_Type()
)
remOptSwPLA15minIntLineBRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA15minIntLineBRxLOS.setStatus("current")
_RemOptSwPLA15minIntValidData_Type = TruthValue
_RemOptSwPLA15minIntValidData_Object = MibTableColumn
remOptSwPLA15minIntValidData = _RemOptSwPLA15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 1, 1, 4),
    _RemOptSwPLA15minIntValidData_Type()
)
remOptSwPLA15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA15minIntValidData.setStatus("current")
_RemOptSwPLA15minIntTimeStamp_Type = DateAndTime
_RemOptSwPLA15minIntTimeStamp_Object = MibTableColumn
remOptSwPLA15minIntTimeStamp = _RemOptSwPLA15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 1, 1, 5),
    _RemOptSwPLA15minIntTimeStamp_Type()
)
remOptSwPLA15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA15minIntTimeStamp.setStatus("current")
_RemOptSwPLA24hIntTable_Object = MibTable
remOptSwPLA24hIntTable = _RemOptSwPLA24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    remOptSwPLA24hIntTable.setStatus("current")
_RemOptSwPLA24hIntEntry_Object = MibTableRow
remOptSwPLA24hIntEntry = _RemOptSwPLA24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 2, 1)
)
remOptSwPLA24hIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP3000-MIB", "remOptSwPLA24hIntNumber"),
)
if mibBuilder.loadTexts:
    remOptSwPLA24hIntEntry.setStatus("current")


class _RemOptSwPLA24hIntNumber_Type(Integer32):
    """Custom type remOptSwPLA24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RemOptSwPLA24hIntNumber_Type.__name__ = "Integer32"
_RemOptSwPLA24hIntNumber_Object = MibTableColumn
remOptSwPLA24hIntNumber = _RemOptSwPLA24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 2, 1, 1),
    _RemOptSwPLA24hIntNumber_Type()
)
remOptSwPLA24hIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA24hIntNumber.setStatus("current")
_RemOptSwPLA24hIntLineARxLOS_Type = Gauge32
_RemOptSwPLA24hIntLineARxLOS_Object = MibTableColumn
remOptSwPLA24hIntLineARxLOS = _RemOptSwPLA24hIntLineARxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 2, 1, 2),
    _RemOptSwPLA24hIntLineARxLOS_Type()
)
remOptSwPLA24hIntLineARxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA24hIntLineARxLOS.setStatus("current")
_RemOptSwPLA24hIntLineBRxLOS_Type = Gauge32
_RemOptSwPLA24hIntLineBRxLOS_Object = MibTableColumn
remOptSwPLA24hIntLineBRxLOS = _RemOptSwPLA24hIntLineBRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 2, 1, 3),
    _RemOptSwPLA24hIntLineBRxLOS_Type()
)
remOptSwPLA24hIntLineBRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA24hIntLineBRxLOS.setStatus("current")
_RemOptSwPLA24hIntValidData_Type = TruthValue
_RemOptSwPLA24hIntValidData_Object = MibTableColumn
remOptSwPLA24hIntValidData = _RemOptSwPLA24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 2, 1, 4),
    _RemOptSwPLA24hIntValidData_Type()
)
remOptSwPLA24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA24hIntValidData.setStatus("current")
_RemOptSwPLA24hIntTimeStamp_Type = DateAndTime
_RemOptSwPLA24hIntTimeStamp_Object = MibTableColumn
remOptSwPLA24hIntTimeStamp = _RemOptSwPLA24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 2, 1, 5),
    _RemOptSwPLA24hIntTimeStamp_Type()
)
remOptSwPLA24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remOptSwPLA24hIntTimeStamp.setStatus("current")
_EdfaPLA15minIntTable_Object = MibTable
edfaPLA15minIntTable = _EdfaPLA15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 3)
)
if mibBuilder.loadTexts:
    edfaPLA15minIntTable.setStatus("current")
_EdfaPLA15minIntEntry_Object = MibTableRow
edfaPLA15minIntEntry = _EdfaPLA15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 3, 1)
)
edfaPLA15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "edfaPLA15minIntNumber"),
)
if mibBuilder.loadTexts:
    edfaPLA15minIntEntry.setStatus("current")


class _EdfaPLA15minIntNumber_Type(Integer32):
    """Custom type edfaPLA15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EdfaPLA15minIntNumber_Type.__name__ = "Integer32"
_EdfaPLA15minIntNumber_Object = MibTableColumn
edfaPLA15minIntNumber = _EdfaPLA15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 3, 1, 1),
    _EdfaPLA15minIntNumber_Type()
)
edfaPLA15minIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntNumber.setStatus("current")
_EdfaPLA15minIntLossOfOIP_Type = Gauge32
_EdfaPLA15minIntLossOfOIP_Object = MibTableColumn
edfaPLA15minIntLossOfOIP = _EdfaPLA15minIntLossOfOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 3, 1, 2),
    _EdfaPLA15minIntLossOfOIP_Type()
)
edfaPLA15minIntLossOfOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntLossOfOIP.setStatus("current")
_EdfaPLA15minIntHwOIPTooHigh_Type = Gauge32
_EdfaPLA15minIntHwOIPTooHigh_Object = MibTableColumn
edfaPLA15minIntHwOIPTooHigh = _EdfaPLA15minIntHwOIPTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 3, 1, 3),
    _EdfaPLA15minIntHwOIPTooHigh_Type()
)
edfaPLA15minIntHwOIPTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntHwOIPTooHigh.setStatus("current")
_EdfaPLA15minIntValidData_Type = TruthValue
_EdfaPLA15minIntValidData_Object = MibTableColumn
edfaPLA15minIntValidData = _EdfaPLA15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 3, 1, 4),
    _EdfaPLA15minIntValidData_Type()
)
edfaPLA15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntValidData.setStatus("current")
_EdfaPLA15minIntTimeStamp_Type = DateAndTime
_EdfaPLA15minIntTimeStamp_Object = MibTableColumn
edfaPLA15minIntTimeStamp = _EdfaPLA15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 3, 1, 5),
    _EdfaPLA15minIntTimeStamp_Type()
)
edfaPLA15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntTimeStamp.setStatus("current")
_EdfaPLA24hIntTable_Object = MibTable
edfaPLA24hIntTable = _EdfaPLA24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 4)
)
if mibBuilder.loadTexts:
    edfaPLA24hIntTable.setStatus("current")
_EdfaPLA24hIntEntry_Object = MibTableRow
edfaPLA24hIntEntry = _EdfaPLA24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 4, 1)
)
edfaPLA24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "edfaPLA24hIntNumber"),
)
if mibBuilder.loadTexts:
    edfaPLA24hIntEntry.setStatus("current")


class _EdfaPLA24hIntNumber_Type(Integer32):
    """Custom type edfaPLA24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EdfaPLA24hIntNumber_Type.__name__ = "Integer32"
_EdfaPLA24hIntNumber_Object = MibTableColumn
edfaPLA24hIntNumber = _EdfaPLA24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 4, 1, 1),
    _EdfaPLA24hIntNumber_Type()
)
edfaPLA24hIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntNumber.setStatus("current")
_EdfaPLA24hIntLossOfOIP_Type = Gauge32
_EdfaPLA24hIntLossOfOIP_Object = MibTableColumn
edfaPLA24hIntLossOfOIP = _EdfaPLA24hIntLossOfOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 4, 1, 2),
    _EdfaPLA24hIntLossOfOIP_Type()
)
edfaPLA24hIntLossOfOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntLossOfOIP.setStatus("current")
_EdfaPLA24hIntHwOIPTooHigh_Type = Gauge32
_EdfaPLA24hIntHwOIPTooHigh_Object = MibTableColumn
edfaPLA24hIntHwOIPTooHigh = _EdfaPLA24hIntHwOIPTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 4, 1, 3),
    _EdfaPLA24hIntHwOIPTooHigh_Type()
)
edfaPLA24hIntHwOIPTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntHwOIPTooHigh.setStatus("current")
_EdfaPLA24hIntValidData_Type = TruthValue
_EdfaPLA24hIntValidData_Object = MibTableColumn
edfaPLA24hIntValidData = _EdfaPLA24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 4, 1, 4),
    _EdfaPLA24hIntValidData_Type()
)
edfaPLA24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntValidData.setStatus("current")
_EdfaPLA24hIntTimeStamp_Type = DateAndTime
_EdfaPLA24hIntTimeStamp_Object = MibTableColumn
edfaPLA24hIntTimeStamp = _EdfaPLA24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 4, 1, 5),
    _EdfaPLA24hIntTimeStamp_Type()
)
edfaPLA24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntTimeStamp.setStatus("current")
_InterfaceTTPLA15minIntTable_Object = MibTable
interfaceTTPLA15minIntTable = _InterfaceTTPLA15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5)
)
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntTable.setStatus("current")
_InterfaceTTPLA15minIntEntry_Object = MibTableRow
interfaceTTPLA15minIntEntry = _InterfaceTTPLA15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1)
)
interfaceTTPLA15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfaceTTPLA15minIntNumber"),
)
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntEntry.setStatus("current")


class _InterfaceTTPLA15minIntNumber_Type(Integer32):
    """Custom type interfaceTTPLA15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_InterfaceTTPLA15minIntNumber_Type.__name__ = "Integer32"
_InterfaceTTPLA15minIntNumber_Object = MibTableColumn
interfaceTTPLA15minIntNumber = _InterfaceTTPLA15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1, 1),
    _InterfaceTTPLA15minIntNumber_Type()
)
interfaceTTPLA15minIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntNumber.setStatus("current")
_InterfaceTTPLA15minIntRxLOS_Type = Integer32
_InterfaceTTPLA15minIntRxLOS_Object = MibTableColumn
interfaceTTPLA15minIntRxLOS = _InterfaceTTPLA15minIntRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1, 2),
    _InterfaceTTPLA15minIntRxLOS_Type()
)
interfaceTTPLA15minIntRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntRxLOS.setStatus("current")
_InterfaceTTPLA15minIntRxLoLP_Type = Integer32
_InterfaceTTPLA15minIntRxLoLP_Object = MibTableColumn
interfaceTTPLA15minIntRxLoLP = _InterfaceTTPLA15minIntRxLoLP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1, 3),
    _InterfaceTTPLA15minIntRxLoLP_Type()
)
interfaceTTPLA15minIntRxLoLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntRxLoLP.setStatus("current")
_InterfaceTTPLA15minIntRxLossOfClk_Type = Integer32
_InterfaceTTPLA15minIntRxLossOfClk_Object = MibTableColumn
interfaceTTPLA15minIntRxLossOfClk = _InterfaceTTPLA15minIntRxLossOfClk_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1, 4),
    _InterfaceTTPLA15minIntRxLossOfClk_Type()
)
interfaceTTPLA15minIntRxLossOfClk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntRxLossOfClk.setStatus("current")
_InterfaceTTPLA15minIntRxLOF_Type = Integer32
_InterfaceTTPLA15minIntRxLOF_Object = MibTableColumn
interfaceTTPLA15minIntRxLOF = _InterfaceTTPLA15minIntRxLOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1, 5),
    _InterfaceTTPLA15minIntRxLOF_Type()
)
interfaceTTPLA15minIntRxLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntRxLOF.setStatus("current")
_InterfaceTTPLA15minIntRxSignalOverload_Type = Integer32
_InterfaceTTPLA15minIntRxSignalOverload_Object = MibTableColumn
interfaceTTPLA15minIntRxSignalOverload = _InterfaceTTPLA15minIntRxSignalOverload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1, 6),
    _InterfaceTTPLA15minIntRxSignalOverload_Type()
)
interfaceTTPLA15minIntRxSignalOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntRxSignalOverload.setStatus("current")
_InterfaceTTPLA15minIntValidData_Type = TruthValue
_InterfaceTTPLA15minIntValidData_Object = MibTableColumn
interfaceTTPLA15minIntValidData = _InterfaceTTPLA15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1, 7),
    _InterfaceTTPLA15minIntValidData_Type()
)
interfaceTTPLA15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntValidData.setStatus("current")
_InterfaceTTPLA15minIntTimeStamp_Type = DateAndTime
_InterfaceTTPLA15minIntTimeStamp_Object = MibTableColumn
interfaceTTPLA15minIntTimeStamp = _InterfaceTTPLA15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 5, 1, 8),
    _InterfaceTTPLA15minIntTimeStamp_Type()
)
interfaceTTPLA15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA15minIntTimeStamp.setStatus("current")
_InterfaceTTPLA24hIntTable_Object = MibTable
interfaceTTPLA24hIntTable = _InterfaceTTPLA24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6)
)
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntTable.setStatus("current")
_InterfaceTTPLA24hIntEntry_Object = MibTableRow
interfaceTTPLA24hIntEntry = _InterfaceTTPLA24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1)
)
interfaceTTPLA24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "interfaceTTPLA24hIntNumber"),
)
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntEntry.setStatus("current")


class _InterfaceTTPLA24hIntNumber_Type(Integer32):
    """Custom type interfaceTTPLA24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_InterfaceTTPLA24hIntNumber_Type.__name__ = "Integer32"
_InterfaceTTPLA24hIntNumber_Object = MibTableColumn
interfaceTTPLA24hIntNumber = _InterfaceTTPLA24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1, 1),
    _InterfaceTTPLA24hIntNumber_Type()
)
interfaceTTPLA24hIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntNumber.setStatus("current")
_InterfaceTTPLA24hIntRxLOS_Type = Integer32
_InterfaceTTPLA24hIntRxLOS_Object = MibTableColumn
interfaceTTPLA24hIntRxLOS = _InterfaceTTPLA24hIntRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1, 2),
    _InterfaceTTPLA24hIntRxLOS_Type()
)
interfaceTTPLA24hIntRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntRxLOS.setStatus("current")
_InterfaceTTPLA24hIntRxLoLP_Type = Integer32
_InterfaceTTPLA24hIntRxLoLP_Object = MibTableColumn
interfaceTTPLA24hIntRxLoLP = _InterfaceTTPLA24hIntRxLoLP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1, 3),
    _InterfaceTTPLA24hIntRxLoLP_Type()
)
interfaceTTPLA24hIntRxLoLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntRxLoLP.setStatus("current")
_InterfaceTTPLA24hIntRxLossOfClk_Type = Integer32
_InterfaceTTPLA24hIntRxLossOfClk_Object = MibTableColumn
interfaceTTPLA24hIntRxLossOfClk = _InterfaceTTPLA24hIntRxLossOfClk_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1, 4),
    _InterfaceTTPLA24hIntRxLossOfClk_Type()
)
interfaceTTPLA24hIntRxLossOfClk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntRxLossOfClk.setStatus("current")
_InterfaceTTPLA24hIntRxLOF_Type = Integer32
_InterfaceTTPLA24hIntRxLOF_Object = MibTableColumn
interfaceTTPLA24hIntRxLOF = _InterfaceTTPLA24hIntRxLOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1, 5),
    _InterfaceTTPLA24hIntRxLOF_Type()
)
interfaceTTPLA24hIntRxLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntRxLOF.setStatus("current")
_InterfaceTTPLA24hIntRxSignalOverload_Type = Integer32
_InterfaceTTPLA24hIntRxSignalOverload_Object = MibTableColumn
interfaceTTPLA24hIntRxSignalOverload = _InterfaceTTPLA24hIntRxSignalOverload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1, 6),
    _InterfaceTTPLA24hIntRxSignalOverload_Type()
)
interfaceTTPLA24hIntRxSignalOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntRxSignalOverload.setStatus("current")
_InterfaceTTPLA24hIntValidData_Type = TruthValue
_InterfaceTTPLA24hIntValidData_Object = MibTableColumn
interfaceTTPLA24hIntValidData = _InterfaceTTPLA24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1, 7),
    _InterfaceTTPLA24hIntValidData_Type()
)
interfaceTTPLA24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntValidData.setStatus("current")
_InterfaceTTPLA24hIntTimeStamp_Type = DateAndTime
_InterfaceTTPLA24hIntTimeStamp_Object = MibTableColumn
interfaceTTPLA24hIntTimeStamp = _InterfaceTTPLA24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 6, 1, 8),
    _InterfaceTTPLA24hIntTimeStamp_Type()
)
interfaceTTPLA24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTPLA24hIntTimeStamp.setStatus("current")
_EccmPLA15minIntTable_Object = MibTable
eccmPLA15minIntTable = _EccmPLA15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 7)
)
if mibBuilder.loadTexts:
    eccmPLA15minIntTable.setStatus("current")
_EccmPLA15minIntEntry_Object = MibTableRow
eccmPLA15minIntEntry = _EccmPLA15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 7, 1)
)
eccmPLA15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "eccmPLA15minIntNumber"),
)
if mibBuilder.loadTexts:
    eccmPLA15minIntEntry.setStatus("current")


class _EccmPLA15minIntNumber_Type(Integer32):
    """Custom type eccmPLA15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EccmPLA15minIntNumber_Type.__name__ = "Integer32"
_EccmPLA15minIntNumber_Object = MibTableColumn
eccmPLA15minIntNumber = _EccmPLA15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 7, 1, 1),
    _EccmPLA15minIntNumber_Type()
)
eccmPLA15minIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLA15minIntNumber.setStatus("current")
_EccmPLA15minIntRxLOS_Type = Gauge32
_EccmPLA15minIntRxLOS_Object = MibTableColumn
eccmPLA15minIntRxLOS = _EccmPLA15minIntRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 7, 1, 2),
    _EccmPLA15minIntRxLOS_Type()
)
eccmPLA15minIntRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLA15minIntRxLOS.setStatus("current")
_EccmPLA15minIntValidData_Type = TruthValue
_EccmPLA15minIntValidData_Object = MibTableColumn
eccmPLA15minIntValidData = _EccmPLA15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 7, 1, 3),
    _EccmPLA15minIntValidData_Type()
)
eccmPLA15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLA15minIntValidData.setStatus("current")
_EccmPLA15minIntTimeStamp_Type = DateAndTime
_EccmPLA15minIntTimeStamp_Object = MibTableColumn
eccmPLA15minIntTimeStamp = _EccmPLA15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 7, 1, 4),
    _EccmPLA15minIntTimeStamp_Type()
)
eccmPLA15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLA15minIntTimeStamp.setStatus("current")
_EccmPLA24hIntTable_Object = MibTable
eccmPLA24hIntTable = _EccmPLA24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 8)
)
if mibBuilder.loadTexts:
    eccmPLA24hIntTable.setStatus("current")
_EccmPLA24hIntEntry_Object = MibTableRow
eccmPLA24hIntEntry = _EccmPLA24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 8, 1)
)
eccmPLA24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "eccmPLA24hIntNumber"),
)
if mibBuilder.loadTexts:
    eccmPLA24hIntEntry.setStatus("current")


class _EccmPLA24hIntNumber_Type(Integer32):
    """Custom type eccmPLA24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EccmPLA24hIntNumber_Type.__name__ = "Integer32"
_EccmPLA24hIntNumber_Object = MibTableColumn
eccmPLA24hIntNumber = _EccmPLA24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 8, 1, 1),
    _EccmPLA24hIntNumber_Type()
)
eccmPLA24hIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLA24hIntNumber.setStatus("current")
_EccmPLA24hIntRxLOS_Type = Gauge32
_EccmPLA24hIntRxLOS_Object = MibTableColumn
eccmPLA24hIntRxLOS = _EccmPLA24hIntRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 8, 1, 2),
    _EccmPLA24hIntRxLOS_Type()
)
eccmPLA24hIntRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLA24hIntRxLOS.setStatus("current")
_EccmPLA24hIntValidData_Type = TruthValue
_EccmPLA24hIntValidData_Object = MibTableColumn
eccmPLA24hIntValidData = _EccmPLA24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 8, 1, 3),
    _EccmPLA24hIntValidData_Type()
)
eccmPLA24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLA24hIntValidData.setStatus("current")
_EccmPLA24hIntTimeStamp_Type = DateAndTime
_EccmPLA24hIntTimeStamp_Object = MibTableColumn
eccmPLA24hIntTimeStamp = _EccmPLA24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 8, 1, 4),
    _EccmPLA24hIntTimeStamp_Type()
)
eccmPLA24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccmPLA24hIntTimeStamp.setStatus("current")
_ApsPLA15minIntTable_Object = MibTable
apsPLA15minIntTable = _ApsPLA15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 9)
)
if mibBuilder.loadTexts:
    apsPLA15minIntTable.setStatus("current")
_ApsPLA15minIntEntry_Object = MibTableRow
apsPLA15minIntEntry = _ApsPLA15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 9, 1)
)
apsPLA15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "apsPLA15minIntNumber"),
)
if mibBuilder.loadTexts:
    apsPLA15minIntEntry.setStatus("current")


class _ApsPLA15minIntNumber_Type(Integer32):
    """Custom type apsPLA15minIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApsPLA15minIntNumber_Type.__name__ = "Integer32"
_ApsPLA15minIntNumber_Object = MibTableColumn
apsPLA15minIntNumber = _ApsPLA15minIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 9, 1, 1),
    _ApsPLA15minIntNumber_Type()
)
apsPLA15minIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsPLA15minIntNumber.setStatus("current")
_ApsPLA15minIntLossOfOIP_Type = Gauge32
_ApsPLA15minIntLossOfOIP_Object = MibTableColumn
apsPLA15minIntLossOfOIP = _ApsPLA15minIntLossOfOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 9, 1, 3),
    _ApsPLA15minIntLossOfOIP_Type()
)
apsPLA15minIntLossOfOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLA15minIntLossOfOIP.setStatus("current")
_ApsPLA15minIntValidData_Type = TruthValue
_ApsPLA15minIntValidData_Object = MibTableColumn
apsPLA15minIntValidData = _ApsPLA15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 9, 1, 5),
    _ApsPLA15minIntValidData_Type()
)
apsPLA15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLA15minIntValidData.setStatus("current")
_ApsPLA15minIntTimeStamp_Type = DateAndTime
_ApsPLA15minIntTimeStamp_Object = MibTableColumn
apsPLA15minIntTimeStamp = _ApsPLA15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 9, 1, 6),
    _ApsPLA15minIntTimeStamp_Type()
)
apsPLA15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLA15minIntTimeStamp.setStatus("current")
_ApsPLA24hIntTable_Object = MibTable
apsPLA24hIntTable = _ApsPLA24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 10)
)
if mibBuilder.loadTexts:
    apsPLA24hIntTable.setStatus("current")
_ApsPLA24hIntEntry_Object = MibTableRow
apsPLA24hIntEntry = _ApsPLA24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 10, 1)
)
apsPLA24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "apsPLA24hIntNumber"),
)
if mibBuilder.loadTexts:
    apsPLA24hIntEntry.setStatus("current")


class _ApsPLA24hIntNumber_Type(Integer32):
    """Custom type apsPLA24hIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApsPLA24hIntNumber_Type.__name__ = "Integer32"
_ApsPLA24hIntNumber_Object = MibTableColumn
apsPLA24hIntNumber = _ApsPLA24hIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 10, 1, 1),
    _ApsPLA24hIntNumber_Type()
)
apsPLA24hIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsPLA24hIntNumber.setStatus("current")
_ApsPLA24hIntLossOfOIP_Type = Gauge32
_ApsPLA24hIntLossOfOIP_Object = MibTableColumn
apsPLA24hIntLossOfOIP = _ApsPLA24hIntLossOfOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 10, 1, 3),
    _ApsPLA24hIntLossOfOIP_Type()
)
apsPLA24hIntLossOfOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLA24hIntLossOfOIP.setStatus("current")
_ApsPLA24hIntValidData_Type = TruthValue
_ApsPLA24hIntValidData_Object = MibTableColumn
apsPLA24hIntValidData = _ApsPLA24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 10, 1, 5),
    _ApsPLA24hIntValidData_Type()
)
apsPLA24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLA24hIntValidData.setStatus("current")
_ApsPLA24hIntTimeStamp_Type = DateAndTime
_ApsPLA24hIntTimeStamp_Object = MibTableColumn
apsPLA24hIntTimeStamp = _ApsPLA24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 3, 10, 1, 6),
    _ApsPLA24hIntTimeStamp_Type()
)
apsPLA24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPLA24hIntTimeStamp.setStatus("current")
_CodingStatsPerformanceMon_ObjectIdentity = ObjectIdentity
codingStatsPerformanceMon = _CodingStatsPerformanceMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4)
)
_CodingStatsCurrent15minTable_Object = MibTable
codingStatsCurrent15minTable = _CodingStatsCurrent15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    codingStatsCurrent15minTable.setStatus("current")
_CodingStatsCurrent15minEntry_Object = MibTableRow
codingStatsCurrent15minEntry = _CodingStatsCurrent15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 1, 1)
)
codingStatsCurrent15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    codingStatsCurrent15minEntry.setStatus("current")


class _CodingStatsCurrent15minStatus_Type(Integer32):
    """Custom type codingStatsCurrent15minStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CodingStatsCurrent15minStatus_Type.__name__ = "Integer32"
_CodingStatsCurrent15minStatus_Object = MibTableColumn
codingStatsCurrent15minStatus = _CodingStatsCurrent15minStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 1, 1, 1),
    _CodingStatsCurrent15minStatus_Type()
)
codingStatsCurrent15minStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent15minStatus.setStatus("current")
_CodingStatsCurrent15minESs_Type = Gauge32
_CodingStatsCurrent15minESs_Object = MibTableColumn
codingStatsCurrent15minESs = _CodingStatsCurrent15minESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 1, 1, 2),
    _CodingStatsCurrent15minESs_Type()
)
codingStatsCurrent15minESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent15minESs.setStatus("current")
_CodingStatsCurrent15minCVs_Type = Gauge32
_CodingStatsCurrent15minCVs_Object = MibTableColumn
codingStatsCurrent15minCVs = _CodingStatsCurrent15minCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 1, 1, 3),
    _CodingStatsCurrent15minCVs_Type()
)
codingStatsCurrent15minCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent15minCVs.setStatus("current")
_CodingStatsCurrent15minDEs_Type = Gauge32
_CodingStatsCurrent15minDEs_Object = MibTableColumn
codingStatsCurrent15minDEs = _CodingStatsCurrent15minDEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 1, 1, 4),
    _CodingStatsCurrent15minDEs_Type()
)
codingStatsCurrent15minDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent15minDEs.setStatus("current")


class _CodingStatsCurrent15minTimeElapsed_Type(Integer32):
    """Custom type codingStatsCurrent15minTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_CodingStatsCurrent15minTimeElapsed_Type.__name__ = "Integer32"
_CodingStatsCurrent15minTimeElapsed_Object = MibTableColumn
codingStatsCurrent15minTimeElapsed = _CodingStatsCurrent15minTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 1, 1, 5),
    _CodingStatsCurrent15minTimeElapsed_Type()
)
codingStatsCurrent15minTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent15minTimeElapsed.setStatus("current")
_CodingStatsCurrent24hTable_Object = MibTable
codingStatsCurrent24hTable = _CodingStatsCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 2)
)
if mibBuilder.loadTexts:
    codingStatsCurrent24hTable.setStatus("current")
_CodingStatsCurrent24hEntry_Object = MibTableRow
codingStatsCurrent24hEntry = _CodingStatsCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 2, 1)
)
codingStatsCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    codingStatsCurrent24hEntry.setStatus("current")


class _CodingStatsCurrent24hStatus_Type(Integer32):
    """Custom type codingStatsCurrent24hStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CodingStatsCurrent24hStatus_Type.__name__ = "Integer32"
_CodingStatsCurrent24hStatus_Object = MibTableColumn
codingStatsCurrent24hStatus = _CodingStatsCurrent24hStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 2, 1, 1),
    _CodingStatsCurrent24hStatus_Type()
)
codingStatsCurrent24hStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent24hStatus.setStatus("current")
_CodingStatsCurrent24hESs_Type = Gauge32
_CodingStatsCurrent24hESs_Object = MibTableColumn
codingStatsCurrent24hESs = _CodingStatsCurrent24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 2, 1, 2),
    _CodingStatsCurrent24hESs_Type()
)
codingStatsCurrent24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent24hESs.setStatus("current")
_CodingStatsCurrent24hCVs_Type = Gauge32
_CodingStatsCurrent24hCVs_Object = MibTableColumn
codingStatsCurrent24hCVs = _CodingStatsCurrent24hCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 2, 1, 3),
    _CodingStatsCurrent24hCVs_Type()
)
codingStatsCurrent24hCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent24hCVs.setStatus("current")
_CodingStatsCurrent24hDEs_Type = Gauge32
_CodingStatsCurrent24hDEs_Object = MibTableColumn
codingStatsCurrent24hDEs = _CodingStatsCurrent24hDEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 2, 1, 4),
    _CodingStatsCurrent24hDEs_Type()
)
codingStatsCurrent24hDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent24hDEs.setStatus("current")


class _CodingStatsCurrent24hTimeElapsed_Type(Integer32):
    """Custom type codingStatsCurrent24hTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CodingStatsCurrent24hTimeElapsed_Type.__name__ = "Integer32"
_CodingStatsCurrent24hTimeElapsed_Object = MibTableColumn
codingStatsCurrent24hTimeElapsed = _CodingStatsCurrent24hTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 2, 1, 5),
    _CodingStatsCurrent24hTimeElapsed_Type()
)
codingStatsCurrent24hTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStatsCurrent24hTimeElapsed.setStatus("current")
_CodingStats15minIntervalTable_Object = MibTable
codingStats15minIntervalTable = _CodingStats15minIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 3)
)
if mibBuilder.loadTexts:
    codingStats15minIntervalTable.setStatus("current")
_CodingStats15minIntervalEntry_Object = MibTableRow
codingStats15minIntervalEntry = _CodingStats15minIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 3, 1)
)
codingStats15minIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "codingStats15minIntervalNumber"),
)
if mibBuilder.loadTexts:
    codingStats15minIntervalEntry.setStatus("current")


class _CodingStats15minIntervalNumber_Type(Integer32):
    """Custom type codingStats15minIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CodingStats15minIntervalNumber_Type.__name__ = "Integer32"
_CodingStats15minIntervalNumber_Object = MibTableColumn
codingStats15minIntervalNumber = _CodingStats15minIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 3, 1, 1),
    _CodingStats15minIntervalNumber_Type()
)
codingStats15minIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats15minIntervalNumber.setStatus("current")
_CodingStats15minIntervalESs_Type = Gauge32
_CodingStats15minIntervalESs_Object = MibTableColumn
codingStats15minIntervalESs = _CodingStats15minIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 3, 1, 2),
    _CodingStats15minIntervalESs_Type()
)
codingStats15minIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats15minIntervalESs.setStatus("current")
_CodingStats15minIntervalCVs_Type = Gauge32
_CodingStats15minIntervalCVs_Object = MibTableColumn
codingStats15minIntervalCVs = _CodingStats15minIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 3, 1, 3),
    _CodingStats15minIntervalCVs_Type()
)
codingStats15minIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats15minIntervalCVs.setStatus("current")
_CodingStats15minIntervalDEs_Type = Gauge32
_CodingStats15minIntervalDEs_Object = MibTableColumn
codingStats15minIntervalDEs = _CodingStats15minIntervalDEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 3, 1, 4),
    _CodingStats15minIntervalDEs_Type()
)
codingStats15minIntervalDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats15minIntervalDEs.setStatus("current")
_CodingStats15minIntervalValidData_Type = TruthValue
_CodingStats15minIntervalValidData_Object = MibTableColumn
codingStats15minIntervalValidData = _CodingStats15minIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 3, 1, 5),
    _CodingStats15minIntervalValidData_Type()
)
codingStats15minIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats15minIntervalValidData.setStatus("current")
_CodingStats15minIntervalTimeStamp_Type = DateAndTime
_CodingStats15minIntervalTimeStamp_Object = MibTableColumn
codingStats15minIntervalTimeStamp = _CodingStats15minIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 3, 1, 6),
    _CodingStats15minIntervalTimeStamp_Type()
)
codingStats15minIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats15minIntervalTimeStamp.setStatus("current")
_CodingStats24hIntervalTable_Object = MibTable
codingStats24hIntervalTable = _CodingStats24hIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 4)
)
if mibBuilder.loadTexts:
    codingStats24hIntervalTable.setStatus("current")
_CodingStats24hIntervalEntry_Object = MibTableRow
codingStats24hIntervalEntry = _CodingStats24hIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 4, 1)
)
codingStats24hIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "codingStats24hIntervalNumber"),
)
if mibBuilder.loadTexts:
    codingStats24hIntervalEntry.setStatus("current")


class _CodingStats24hIntervalNumber_Type(Integer32):
    """Custom type codingStats24hIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CodingStats24hIntervalNumber_Type.__name__ = "Integer32"
_CodingStats24hIntervalNumber_Object = MibTableColumn
codingStats24hIntervalNumber = _CodingStats24hIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 4, 1, 1),
    _CodingStats24hIntervalNumber_Type()
)
codingStats24hIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats24hIntervalNumber.setStatus("current")
_CodingStats24hIntervalESs_Type = Gauge32
_CodingStats24hIntervalESs_Object = MibTableColumn
codingStats24hIntervalESs = _CodingStats24hIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 4, 1, 2),
    _CodingStats24hIntervalESs_Type()
)
codingStats24hIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats24hIntervalESs.setStatus("current")
_CodingStats24hIntervalCVs_Type = Gauge32
_CodingStats24hIntervalCVs_Object = MibTableColumn
codingStats24hIntervalCVs = _CodingStats24hIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 4, 1, 3),
    _CodingStats24hIntervalCVs_Type()
)
codingStats24hIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats24hIntervalCVs.setStatus("current")
_CodingStats24hIntervalDEs_Type = Gauge32
_CodingStats24hIntervalDEs_Object = MibTableColumn
codingStats24hIntervalDEs = _CodingStats24hIntervalDEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 4, 1, 4),
    _CodingStats24hIntervalDEs_Type()
)
codingStats24hIntervalDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats24hIntervalDEs.setStatus("current")
_CodingStats24hIntervalValidData_Type = TruthValue
_CodingStats24hIntervalValidData_Object = MibTableColumn
codingStats24hIntervalValidData = _CodingStats24hIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 4, 1, 5),
    _CodingStats24hIntervalValidData_Type()
)
codingStats24hIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats24hIntervalValidData.setStatus("current")
_CodingStats24hIntervalTimeStamp_Type = DateAndTime
_CodingStats24hIntervalTimeStamp_Object = MibTableColumn
codingStats24hIntervalTimeStamp = _CodingStats24hIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 4, 4, 1, 6),
    _CodingStats24hIntervalTimeStamp_Type()
)
codingStats24hIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codingStats24hIntervalTimeStamp.setStatus("current")
_OtuFecPerformanceMon_ObjectIdentity = ObjectIdentity
otuFecPerformanceMon = _OtuFecPerformanceMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5)
)
_OtuFecCurrent15minTable_Object = MibTable
otuFecCurrent15minTable = _OtuFecCurrent15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 1)
)
if mibBuilder.loadTexts:
    otuFecCurrent15minTable.setStatus("current")
_OtuFecCurrent15minEntry_Object = MibTableRow
otuFecCurrent15minEntry = _OtuFecCurrent15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 1, 1)
)
otuFecCurrent15minEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otuFecCurrent15minEntry.setStatus("current")
_OtuFecCurrent15minESs_Type = Gauge32
_OtuFecCurrent15minESs_Object = MibTableColumn
otuFecCurrent15minESs = _OtuFecCurrent15minESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 1, 1, 1),
    _OtuFecCurrent15minESs_Type()
)
otuFecCurrent15minESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent15minESs.setStatus("current")
_OtuFecCurrent15minSEFSs_Type = Gauge32
_OtuFecCurrent15minSEFSs_Object = MibTableColumn
otuFecCurrent15minSEFSs = _OtuFecCurrent15minSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 1, 1, 2),
    _OtuFecCurrent15minSEFSs_Type()
)
otuFecCurrent15minSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent15minSEFSs.setStatus("current")
_OtuFecCurrent15minCVs_Type = Gauge32
_OtuFecCurrent15minCVs_Object = MibTableColumn
otuFecCurrent15minCVs = _OtuFecCurrent15minCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 1, 1, 3),
    _OtuFecCurrent15minCVs_Type()
)
otuFecCurrent15minCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent15minCVs.setStatus("current")
_OtuFecCurrent15minUBEs_Type = Gauge32
_OtuFecCurrent15minUBEs_Object = MibTableColumn
otuFecCurrent15minUBEs = _OtuFecCurrent15minUBEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 1, 1, 4),
    _OtuFecCurrent15minUBEs_Type()
)
otuFecCurrent15minUBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent15minUBEs.setStatus("current")


class _OtuFecCurrent15minTimeElapsed_Type(Integer32):
    """Custom type otuFecCurrent15minTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_OtuFecCurrent15minTimeElapsed_Type.__name__ = "Integer32"
_OtuFecCurrent15minTimeElapsed_Object = MibTableColumn
otuFecCurrent15minTimeElapsed = _OtuFecCurrent15minTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 1, 1, 5),
    _OtuFecCurrent15minTimeElapsed_Type()
)
otuFecCurrent15minTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent15minTimeElapsed.setStatus("current")
_OtuFecCurrent24hTable_Object = MibTable
otuFecCurrent24hTable = _OtuFecCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    otuFecCurrent24hTable.setStatus("current")
_OtuFecCurrent24hEntry_Object = MibTableRow
otuFecCurrent24hEntry = _OtuFecCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 2, 1)
)
otuFecCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otuFecCurrent24hEntry.setStatus("current")
_OtuFecCurrent24hESs_Type = Gauge32
_OtuFecCurrent24hESs_Object = MibTableColumn
otuFecCurrent24hESs = _OtuFecCurrent24hESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 2, 1, 1),
    _OtuFecCurrent24hESs_Type()
)
otuFecCurrent24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent24hESs.setStatus("current")
_OtuFecCurrent24hSEFSs_Type = Gauge32
_OtuFecCurrent24hSEFSs_Object = MibTableColumn
otuFecCurrent24hSEFSs = _OtuFecCurrent24hSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 2, 1, 2),
    _OtuFecCurrent24hSEFSs_Type()
)
otuFecCurrent24hSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent24hSEFSs.setStatus("current")
_OtuFecCurrent24hCVs_Type = Gauge32
_OtuFecCurrent24hCVs_Object = MibTableColumn
otuFecCurrent24hCVs = _OtuFecCurrent24hCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 2, 1, 3),
    _OtuFecCurrent24hCVs_Type()
)
otuFecCurrent24hCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent24hCVs.setStatus("current")
_OtuFecCurrent24hUBEs_Type = Gauge32
_OtuFecCurrent24hUBEs_Object = MibTableColumn
otuFecCurrent24hUBEs = _OtuFecCurrent24hUBEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 2, 1, 4),
    _OtuFecCurrent24hUBEs_Type()
)
otuFecCurrent24hUBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent24hUBEs.setStatus("current")


class _OtuFecCurrent24hTimeElapsed_Type(Integer32):
    """Custom type otuFecCurrent24hTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_OtuFecCurrent24hTimeElapsed_Type.__name__ = "Integer32"
_OtuFecCurrent24hTimeElapsed_Object = MibTableColumn
otuFecCurrent24hTimeElapsed = _OtuFecCurrent24hTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 2, 1, 5),
    _OtuFecCurrent24hTimeElapsed_Type()
)
otuFecCurrent24hTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecCurrent24hTimeElapsed.setStatus("current")
_OtuFec15minIntervalTable_Object = MibTable
otuFec15minIntervalTable = _OtuFec15minIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3)
)
if mibBuilder.loadTexts:
    otuFec15minIntervalTable.setStatus("current")
_OtuFec15minIntervalEntry_Object = MibTableRow
otuFec15minIntervalEntry = _OtuFec15minIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3, 1)
)
otuFec15minIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "otuFec15minIntervalNumber"),
)
if mibBuilder.loadTexts:
    otuFec15minIntervalEntry.setStatus("current")


class _OtuFec15minIntervalNumber_Type(Integer32):
    """Custom type otuFec15minIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OtuFec15minIntervalNumber_Type.__name__ = "Integer32"
_OtuFec15minIntervalNumber_Object = MibTableColumn
otuFec15minIntervalNumber = _OtuFec15minIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3, 1, 1),
    _OtuFec15minIntervalNumber_Type()
)
otuFec15minIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec15minIntervalNumber.setStatus("current")
_OtuFec15minIntervalESs_Type = Gauge32
_OtuFec15minIntervalESs_Object = MibTableColumn
otuFec15minIntervalESs = _OtuFec15minIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3, 1, 2),
    _OtuFec15minIntervalESs_Type()
)
otuFec15minIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec15minIntervalESs.setStatus("current")
_OtuFec15minIntervalSEFSs_Type = Gauge32
_OtuFec15minIntervalSEFSs_Object = MibTableColumn
otuFec15minIntervalSEFSs = _OtuFec15minIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3, 1, 3),
    _OtuFec15minIntervalSEFSs_Type()
)
otuFec15minIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec15minIntervalSEFSs.setStatus("current")
_OtuFec15minIntervalCVs_Type = Gauge32
_OtuFec15minIntervalCVs_Object = MibTableColumn
otuFec15minIntervalCVs = _OtuFec15minIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3, 1, 4),
    _OtuFec15minIntervalCVs_Type()
)
otuFec15minIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec15minIntervalCVs.setStatus("current")
_OtuFec15minIntervalUBEs_Type = Gauge32
_OtuFec15minIntervalUBEs_Object = MibTableColumn
otuFec15minIntervalUBEs = _OtuFec15minIntervalUBEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3, 1, 5),
    _OtuFec15minIntervalUBEs_Type()
)
otuFec15minIntervalUBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec15minIntervalUBEs.setStatus("current")
_OtuFec15minIntervalValidData_Type = TruthValue
_OtuFec15minIntervalValidData_Object = MibTableColumn
otuFec15minIntervalValidData = _OtuFec15minIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3, 1, 6),
    _OtuFec15minIntervalValidData_Type()
)
otuFec15minIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec15minIntervalValidData.setStatus("current")
_OtuFec15minIntervalTimeStamp_Type = DateAndTime
_OtuFec15minIntervalTimeStamp_Object = MibTableColumn
otuFec15minIntervalTimeStamp = _OtuFec15minIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 3, 1, 7),
    _OtuFec15minIntervalTimeStamp_Type()
)
otuFec15minIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec15minIntervalTimeStamp.setStatus("current")
_OtuFec24hIntervalTable_Object = MibTable
otuFec24hIntervalTable = _OtuFec24hIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4)
)
if mibBuilder.loadTexts:
    otuFec24hIntervalTable.setStatus("current")
_OtuFec24hIntervalEntry_Object = MibTableRow
otuFec24hIntervalEntry = _OtuFec24hIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4, 1)
)
otuFec24hIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP3000-MIB", "otuFec24hIntervalNumber"),
)
if mibBuilder.loadTexts:
    otuFec24hIntervalEntry.setStatus("current")


class _OtuFec24hIntervalNumber_Type(Integer32):
    """Custom type otuFec24hIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OtuFec24hIntervalNumber_Type.__name__ = "Integer32"
_OtuFec24hIntervalNumber_Object = MibTableColumn
otuFec24hIntervalNumber = _OtuFec24hIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4, 1, 1),
    _OtuFec24hIntervalNumber_Type()
)
otuFec24hIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec24hIntervalNumber.setStatus("current")
_OtuFec24hIntervalESs_Type = Gauge32
_OtuFec24hIntervalESs_Object = MibTableColumn
otuFec24hIntervalESs = _OtuFec24hIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4, 1, 2),
    _OtuFec24hIntervalESs_Type()
)
otuFec24hIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec24hIntervalESs.setStatus("current")
_OtuFec24hIntervalSEFSs_Type = Gauge32
_OtuFec24hIntervalSEFSs_Object = MibTableColumn
otuFec24hIntervalSEFSs = _OtuFec24hIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4, 1, 3),
    _OtuFec24hIntervalSEFSs_Type()
)
otuFec24hIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec24hIntervalSEFSs.setStatus("current")
_OtuFec24hIntervalCVs_Type = Gauge32
_OtuFec24hIntervalCVs_Object = MibTableColumn
otuFec24hIntervalCVs = _OtuFec24hIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4, 1, 4),
    _OtuFec24hIntervalCVs_Type()
)
otuFec24hIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec24hIntervalCVs.setStatus("current")
_OtuFec24hIntervalUBEs_Type = Gauge32
_OtuFec24hIntervalUBEs_Object = MibTableColumn
otuFec24hIntervalUBEs = _OtuFec24hIntervalUBEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4, 1, 5),
    _OtuFec24hIntervalUBEs_Type()
)
otuFec24hIntervalUBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec24hIntervalUBEs.setStatus("current")
_OtuFec24hIntervalValidData_Type = TruthValue
_OtuFec24hIntervalValidData_Object = MibTableColumn
otuFec24hIntervalValidData = _OtuFec24hIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4, 1, 6),
    _OtuFec24hIntervalValidData_Type()
)
otuFec24hIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec24hIntervalValidData.setStatus("current")
_OtuFec24hIntervalTimeStamp_Type = DateAndTime
_OtuFec24hIntervalTimeStamp_Object = MibTableColumn
otuFec24hIntervalTimeStamp = _OtuFec24hIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 5, 2, 5, 4, 1, 7),
    _OtuFec24hIntervalTimeStamp_Type()
)
otuFec24hIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFec24hIntervalTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects

equipmentHolderObjectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 2)
)
equipmentHolderObjectCreation.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalClass"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentHolderObjectCreation.setStatus(
        "current"
    )

equipmentHolderObjectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 3)
)
equipmentHolderObjectDeletion.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentHolderObjectDeletion.setStatus(
        "current"
    )

containerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 4)
)
containerStateChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "containsPhysicalIndex"),
        ("FSP3000-MIB", "containerState"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    containerStateChange.setStatus(
        "current"
    )

protectionStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 5)
)
protectionStateChange.setObjects(
      *(("FSP3000-MIB", "channelCardProtectionGroupIndex"),
        ("FSP3000-MIB", "channelCardProtectionState"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    protectionStateChange.setStatus(
        "current"
    )

neAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 6)
)
neAttributeValueChange.setObjects(
      *(("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    neAttributeValueChange.setStatus(
        "current"
    )

interfaceAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 7)
)
interfaceAttributeValueChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAttributeValueChange.setStatus(
        "current"
    )

equipmentAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 8)
)
equipmentAttributeValueChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAttributeValueChange.setStatus(
        "current"
    )

protectionAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 9)
)
protectionAttributeValueChange.setObjects(
      *(("FSP3000-MIB", "channelCardProtectionGroupIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    protectionAttributeValueChange.setStatus(
        "current"
    )

dcnTopologyReported = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 13)
)
dcnTopologyReported.setObjects(
      *(("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    dcnTopologyReported.setStatus(
        "deprecated"
    )

equipmentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 14)
)
equipmentStateChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentStateChange.setStatus(
        "current"
    )

neTrapsinkObjectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 15)
)
neTrapsinkObjectCreation.setObjects(
      *(("FSP3000-MIB", "neTrapsinkNumber"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    neTrapsinkObjectCreation.setStatus(
        "current"
    )

neTrapsinkObjectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 16)
)
neTrapsinkObjectDeletion.setObjects(
      *(("FSP3000-MIB", "neTrapsinkNumber"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    neTrapsinkObjectDeletion.setStatus(
        "current"
    )

sonetSectionTraceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 17)
)
sonetSectionTraceChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    sonetSectionTraceChanged.setStatus(
        "current"
    )

loginDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 18)
)
loginDetected.setObjects(
      *(("FSP3000-MIB", "loginIdentity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    loginDetected.setStatus(
        "current"
    )

interfacePerfAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 21)
)
interfacePerfAttributeValueChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfacePerfAttributeValueChange.setStatus(
        "current"
    )

equipmentPerfAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 22)
)
equipmentPerfAttributeValueChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentPerfAttributeValueChange.setStatus(
        "current"
    )

snmpConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 23)
)
snmpConfigChanged.setObjects(
      *(("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    snmpConfigChanged.setStatus(
        "current"
    )

fspSwUpgradeStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 24)
)
fspSwUpgradeStateChange.setObjects(
      *(("FSP3000-MIB", "fspSwUpgradeIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    fspSwUpgradeStateChange.setStatus(
        "current"
    )

fspSwUpgradeAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 25)
)
fspSwUpgradeAttributeValueChange.setObjects(
      *(("FSP3000-MIB", "fspSwUpgradeIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    fspSwUpgradeAttributeValueChange.setStatus(
        "current"
    )

oscmTopologyReported = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 26)
)
oscmTopologyReported.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    oscmTopologyReported.setStatus(
        "current"
    )

sectionQoSThresholdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 27)
)
sectionQoSThresholdChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    sectionQoSThresholdChanged.setStatus(
        "current"
    )

pathQoSThresholdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 28)
)
pathQoSThresholdChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    pathQoSThresholdChanged.setStatus(
        "current"
    )

interfaceAlarmLowestCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 300)
)
interfaceAlarmLowestCurrent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLowestCurrent.setStatus(
        "current"
    )

interfaceAlarmNoLowestCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 301)
)
interfaceAlarmNoLowestCurrent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLowestCurrent.setStatus(
        "current"
    )

interfaceAlarmLowCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 302)
)
interfaceAlarmLowCurrent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLowCurrent.setStatus(
        "current"
    )

interfaceAlarmNoLowCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 303)
)
interfaceAlarmNoLowCurrent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLowCurrent.setStatus(
        "current"
    )

interfaceAlarmHighCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 304)
)
interfaceAlarmHighCurrent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHighCurrent.setStatus(
        "current"
    )

interfaceAlarmNoHighCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 305)
)
interfaceAlarmNoHighCurrent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoHighCurrent.setStatus(
        "current"
    )

interfaceAlarmHighestCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 306)
)
interfaceAlarmHighestCurrent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHighestCurrent.setStatus(
        "current"
    )

interfaceAlarmNoHighestCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 307)
)
interfaceAlarmNoHighestCurrent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoHighestCurrent.setStatus(
        "current"
    )

interfaceAlarmLowestOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 308)
)
interfaceAlarmLowestOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLowestOIP.setStatus(
        "current"
    )

interfaceAlarmNoLowestOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 309)
)
interfaceAlarmNoLowestOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLowestOIP.setStatus(
        "current"
    )

interfaceAlarmLowOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 310)
)
interfaceAlarmLowOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLowOIP.setStatus(
        "current"
    )

interfaceAlarmNoLowOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 311)
)
interfaceAlarmNoLowOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLowOIP.setStatus(
        "current"
    )

interfaceAlarmHighOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 312)
)
interfaceAlarmHighOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHighOIP.setStatus(
        "current"
    )

interfaceAlarmNoHighOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 313)
)
interfaceAlarmNoHighOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoHighOIP.setStatus(
        "current"
    )

interfaceAlarmHighestOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 314)
)
interfaceAlarmHighestOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHighestOIP.setStatus(
        "current"
    )

interfaceAlarmNoHighestOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 315)
)
interfaceAlarmNoHighestOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoHighestOIP.setStatus(
        "current"
    )

interfaceAlarmLowestOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 316)
)
interfaceAlarmLowestOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLowestOOP.setStatus(
        "current"
    )

interfaceAlarmNoLowestOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 317)
)
interfaceAlarmNoLowestOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLowestOOP.setStatus(
        "current"
    )

interfaceAlarmLowOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 318)
)
interfaceAlarmLowOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLowOOP.setStatus(
        "current"
    )

interfaceAlarmNoLowOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 319)
)
interfaceAlarmNoLowOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLowOOP.setStatus(
        "current"
    )

interfaceAlarmHighOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 320)
)
interfaceAlarmHighOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHighOOP.setStatus(
        "current"
    )

interfaceAlarmNoHighOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 321)
)
interfaceAlarmNoHighOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoHighOOP.setStatus(
        "current"
    )

interfaceAlarmHighestOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 322)
)
interfaceAlarmHighestOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHighestOOP.setStatus(
        "current"
    )

interfaceAlarmNoHighestOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 323)
)
interfaceAlarmNoHighestOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoHighestOOP.setStatus(
        "current"
    )

equipmentAlarmLowestTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 324)
)
equipmentAlarmLowestTemp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmLowestTemp.setStatus(
        "current"
    )

equipmentAlarmNoLowestTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 325)
)
equipmentAlarmNoLowestTemp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoLowestTemp.setStatus(
        "current"
    )

equipmentAlarmLowTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 326)
)
equipmentAlarmLowTemp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmLowTemp.setStatus(
        "current"
    )

equipmentAlarmNoLowTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 327)
)
equipmentAlarmNoLowTemp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoLowTemp.setStatus(
        "current"
    )

equipmentAlarmHighTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 328)
)
equipmentAlarmHighTemp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmHighTemp.setStatus(
        "current"
    )

equipmentAlarmNoHighTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 329)
)
equipmentAlarmNoHighTemp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoHighTemp.setStatus(
        "current"
    )

equipmentAlarmHighestTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 330)
)
equipmentAlarmHighestTemp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmHighestTemp.setStatus(
        "current"
    )

equipmentAlarmNoHighestTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 331)
)
equipmentAlarmNoHighestTemp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoHighestTemp.setStatus(
        "current"
    )

equipmentAlarmLowestVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 332)
)
equipmentAlarmLowestVolt.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmLowestVolt.setStatus(
        "current"
    )

equipmentAlarmNoLowestVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 333)
)
equipmentAlarmNoLowestVolt.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoLowestVolt.setStatus(
        "current"
    )

equipmentAlarmLowVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 334)
)
equipmentAlarmLowVolt.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmLowVolt.setStatus(
        "current"
    )

equipmentAlarmNoLowVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 335)
)
equipmentAlarmNoLowVolt.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoLowVolt.setStatus(
        "current"
    )

equipmentAlarmHighVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 336)
)
equipmentAlarmHighVolt.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmHighVolt.setStatus(
        "current"
    )

equipmentAlarmNoHighVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 337)
)
equipmentAlarmNoHighVolt.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoHighVolt.setStatus(
        "current"
    )

equipmentAlarmHighestVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 338)
)
equipmentAlarmHighestVolt.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmHighestVolt.setStatus(
        "current"
    )

equipmentAlarmNoHighestVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 339)
)
equipmentAlarmNoHighestVolt.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoHighestVolt.setStatus(
        "current"
    )

equipmentAlarmLowestCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 340)
)
equipmentAlarmLowestCurrent.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmLowestCurrent.setStatus(
        "current"
    )

equipmentAlarmNoLowestCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 341)
)
equipmentAlarmNoLowestCurrent.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoLowestCurrent.setStatus(
        "current"
    )

equipmentAlarmLowCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 342)
)
equipmentAlarmLowCurrent.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmLowCurrent.setStatus(
        "current"
    )

equipmentAlarmNoLowCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 343)
)
equipmentAlarmNoLowCurrent.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoLowCurrent.setStatus(
        "current"
    )

equipmentAlarmHighCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 344)
)
equipmentAlarmHighCurrent.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmHighCurrent.setStatus(
        "current"
    )

equipmentAlarmNoHighCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 345)
)
equipmentAlarmNoHighCurrent.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoHighCurrent.setStatus(
        "current"
    )

equipmentAlarmHighestCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 346)
)
equipmentAlarmHighestCurrent.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmHighestCurrent.setStatus(
        "current"
    )

equipmentAlarmNoHighestCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 347)
)
equipmentAlarmNoHighestCurrent.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoHighestCurrent.setStatus(
        "current"
    )

interfaceQoSReportSection15minES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 400)
)
interfaceQoSReportSection15minES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection15minES.setStatus(
        "current"
    )

interfaceQoSReportSection15minNoES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 401)
)
interfaceQoSReportSection15minNoES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection15minNoES.setStatus(
        "current"
    )

interfaceQoSReportSection15minSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 402)
)
interfaceQoSReportSection15minSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection15minSES.setStatus(
        "current"
    )

interfaceQoSReportSection15minNoSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 403)
)
interfaceQoSReportSection15minNoSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection15minNoSES.setStatus(
        "current"
    )

interfaceQoSReportSection15minSEFS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 404)
)
interfaceQoSReportSection15minSEFS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection15minSEFS.setStatus(
        "current"
    )

interfaceQoSReportSection15minNoSEFS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 405)
)
interfaceQoSReportSection15minNoSEFS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection15minNoSEFS.setStatus(
        "current"
    )

interfaceQoSReportSection15minCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 406)
)
interfaceQoSReportSection15minCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection15minCV.setStatus(
        "current"
    )

interfaceQoSReportSection15minNoCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 407)
)
interfaceQoSReportSection15minNoCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection15minNoCV.setStatus(
        "current"
    )

interfaceQoSReportSection24hrES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 408)
)
interfaceQoSReportSection24hrES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection24hrES.setStatus(
        "current"
    )

interfaceQoSReportSection24hrNoES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 409)
)
interfaceQoSReportSection24hrNoES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection24hrNoES.setStatus(
        "current"
    )

interfaceQoSReportSection24hrSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 410)
)
interfaceQoSReportSection24hrSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection24hrSES.setStatus(
        "current"
    )

interfaceQoSReportSection24hrNoSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 411)
)
interfaceQoSReportSection24hrNoSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection24hrNoSES.setStatus(
        "current"
    )

interfaceQoSReportSection24hrSEFS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 412)
)
interfaceQoSReportSection24hrSEFS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection24hrSEFS.setStatus(
        "current"
    )

interfaceQoSReportSection24hrNoSEFS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 413)
)
interfaceQoSReportSection24hrNoSEFS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection24hrNoSEFS.setStatus(
        "current"
    )

interfaceQoSReportSection24hrCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 414)
)
interfaceQoSReportSection24hrCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection24hrCV.setStatus(
        "current"
    )

interfaceQoSReportSection24hrNoCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 415)
)
interfaceQoSReportSection24hrNoCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportSection24hrNoCV.setStatus(
        "current"
    )

interfaceQoSReportPath15minES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 416)
)
interfaceQoSReportPath15minES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath15minES.setStatus(
        "current"
    )

interfaceQoSReportPath15minNoES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 417)
)
interfaceQoSReportPath15minNoES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath15minNoES.setStatus(
        "current"
    )

interfaceQoSReportPath15minSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 418)
)
interfaceQoSReportPath15minSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath15minSES.setStatus(
        "current"
    )

interfaceQoSReportPath15minNoSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 419)
)
interfaceQoSReportPath15minNoSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath15minNoSES.setStatus(
        "current"
    )

interfaceQoSReportPath15minCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 420)
)
interfaceQoSReportPath15minCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath15minCV.setStatus(
        "current"
    )

interfaceQoSReportPath15minNoCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 421)
)
interfaceQoSReportPath15minNoCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath15minNoCV.setStatus(
        "current"
    )

interfaceQoSReportPath15minUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 422)
)
interfaceQoSReportPath15minUAS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath15minUAS.setStatus(
        "current"
    )

interfaceQoSReportPath15minNoUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 423)
)
interfaceQoSReportPath15minNoUAS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath15minNoUAS.setStatus(
        "current"
    )

interfaceQoSReportPath24hrES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 424)
)
interfaceQoSReportPath24hrES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath24hrES.setStatus(
        "current"
    )

interfaceQoSReportPath24hrNoES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 425)
)
interfaceQoSReportPath24hrNoES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath24hrNoES.setStatus(
        "current"
    )

interfaceQoSReportPath24hrSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 426)
)
interfaceQoSReportPath24hrSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath24hrSES.setStatus(
        "current"
    )

interfaceQoSReportPath24hrNoSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 427)
)
interfaceQoSReportPath24hrNoSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath24hrNoSES.setStatus(
        "current"
    )

interfaceQoSReportPath24hrCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 428)
)
interfaceQoSReportPath24hrCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath24hrCV.setStatus(
        "current"
    )

interfaceQoSReportPath24hrNoCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 429)
)
interfaceQoSReportPath24hrNoCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath24hrNoCV.setStatus(
        "current"
    )

interfaceQoSReportPath24hrUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 430)
)
interfaceQoSReportPath24hrUAS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath24hrUAS.setStatus(
        "current"
    )

interfaceQoSReportPath24hrNoUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 431)
)
interfaceQoSReportPath24hrNoUAS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentQoSReportSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceQoSReportPath24hrNoUAS.setStatus(
        "current"
    )

interfaceAlarmLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 500)
)
interfaceAlarmLossOfSignal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfSignal.setStatus(
        "current"
    )

interfaceAlarmNoLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 501)
)
interfaceAlarmNoLossOfSignal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfSignal.setStatus(
        "current"
    )

interfaceAlarmLossOfLinkPulse = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 502)
)
interfaceAlarmLossOfLinkPulse.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfLinkPulse.setStatus(
        "current"
    )

interfaceAlarmNoLossOfLinkPulse = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 503)
)
interfaceAlarmNoLossOfLinkPulse.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfLinkPulse.setStatus(
        "current"
    )

equipmentAlarmFuse1Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 504)
)
equipmentAlarmFuse1Fail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFuse1Fail.setStatus(
        "current"
    )

equipmentAlarmFuse1NoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 505)
)
equipmentAlarmFuse1NoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFuse1NoFail.setStatus(
        "current"
    )

equipmentAlarmFuse2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 506)
)
equipmentAlarmFuse2Fail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFuse2Fail.setStatus(
        "current"
    )

equipmentAlarmFuse2NoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 507)
)
equipmentAlarmFuse2NoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFuse2NoFail.setStatus(
        "current"
    )

equipmentAlarmFan1Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 510)
)
equipmentAlarmFan1Fail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFan1Fail.setStatus(
        "current"
    )

equipmentAlarmFan1NoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 511)
)
equipmentAlarmFan1NoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFan1NoFail.setStatus(
        "current"
    )

equipmentAlarmFan2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 512)
)
equipmentAlarmFan2Fail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFan2Fail.setStatus(
        "current"
    )

equipmentAlarmFan2NoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 513)
)
equipmentAlarmFan2NoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFan2NoFail.setStatus(
        "current"
    )

equipmentAlarmFan3Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 514)
)
equipmentAlarmFan3Fail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFan3Fail.setStatus(
        "current"
    )

equipmentAlarmFan3NoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 515)
)
equipmentAlarmFan3NoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFan3NoFail.setStatus(
        "current"
    )

equipmentAlarmFanPs1Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 516)
)
equipmentAlarmFanPs1Fail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanPs1Fail.setStatus(
        "current"
    )

equipmentAlarmFanPs1NoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 517)
)
equipmentAlarmFanPs1NoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanPs1NoFail.setStatus(
        "current"
    )

equipmentAlarmFanPs2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 518)
)
equipmentAlarmFanPs2Fail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanPs2Fail.setStatus(
        "current"
    )

equipmentAlarmFanPs2NoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 519)
)
equipmentAlarmFanPs2NoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanPs2NoFail.setStatus(
        "current"
    )

equipmentAlarmPsFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 520)
)
equipmentAlarmPsFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmPsFail.setStatus(
        "current"
    )

equipmentAlarmPsNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 521)
)
equipmentAlarmPsNoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmPsNoFail.setStatus(
        "current"
    )

equipmentAlarmExtInput1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 522)
)
equipmentAlarmExtInput1.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput1.setStatus(
        "current"
    )

equipmentAlarmExtInput1Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 523)
)
equipmentAlarmExtInput1Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput1Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 524)
)
equipmentAlarmExtInput2.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput2.setStatus(
        "current"
    )

equipmentAlarmExtInput2Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 525)
)
equipmentAlarmExtInput2Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput2Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 526)
)
equipmentAlarmExtInput3.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput3.setStatus(
        "current"
    )

equipmentAlarmExtInput3Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 527)
)
equipmentAlarmExtInput3Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput3Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 528)
)
equipmentAlarmExtInput4.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput4.setStatus(
        "current"
    )

equipmentAlarmExtInput4Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 529)
)
equipmentAlarmExtInput4Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput4Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 530)
)
equipmentAlarmExtInput5.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput5.setStatus(
        "current"
    )

equipmentAlarmExtInput5Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 531)
)
equipmentAlarmExtInput5Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput5Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 532)
)
equipmentAlarmExtInput6.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput6.setStatus(
        "current"
    )

equipmentAlarmExtInput6Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 533)
)
equipmentAlarmExtInput6Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput6Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 534)
)
equipmentAlarmExtInput7.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput7.setStatus(
        "current"
    )

equipmentAlarmExtInput7Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 535)
)
equipmentAlarmExtInput7Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput7Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 536)
)
equipmentAlarmExtInput8.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput8.setStatus(
        "current"
    )

equipmentAlarmExtInput8Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 537)
)
equipmentAlarmExtInput8Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput8Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 538)
)
equipmentAlarmExtInput9.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput9.setStatus(
        "current"
    )

equipmentAlarmExtInput9Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 539)
)
equipmentAlarmExtInput9Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput9Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 540)
)
equipmentAlarmExtInput10.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput10.setStatus(
        "current"
    )

equipmentAlarmExtInput10Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 541)
)
equipmentAlarmExtInput10Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput10Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 542)
)
equipmentAlarmExtInput11.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput11.setStatus(
        "current"
    )

equipmentAlarmExtInput11Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 543)
)
equipmentAlarmExtInput11Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput11Ok.setStatus(
        "current"
    )

equipmentAlarmExtInput12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 544)
)
equipmentAlarmExtInput12.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput12.setStatus(
        "current"
    )

equipmentAlarmExtInput12Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 545)
)
equipmentAlarmExtInput12Ok.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExtInput12Ok.setStatus(
        "current"
    )

interfaceAlarmLossOfClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 546)
)
interfaceAlarmLossOfClock.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfClock.setStatus(
        "current"
    )

interfaceAlarmNoLossOfClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 547)
)
interfaceAlarmNoLossOfClock.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfClock.setStatus(
        "current"
    )

interfaceAlarmTxClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 548)
)
interfaceAlarmTxClockFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmTxClockFail.setStatus(
        "current"
    )

interfaceAlarmNoTxClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 549)
)
interfaceAlarmNoTxClockFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoTxClockFail.setStatus(
        "current"
    )

interfaceAlarmLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 553)
)
interfaceAlarmLossOfFrame.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfFrame.setStatus(
        "current"
    )

interfaceAlarmNoLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 554)
)
interfaceAlarmNoLossOfFrame.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfFrame.setStatus(
        "current"
    )

interfaceAlarmRxESFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 555)
)
interfaceAlarmRxESFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmRxESFail.setStatus(
        "current"
    )

interfaceAlarmNoRxESFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 556)
)
interfaceAlarmNoRxESFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoRxESFail.setStatus(
        "current"
    )

interfaceAlarmTxESFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 557)
)
interfaceAlarmTxESFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmTxESFail.setStatus(
        "current"
    )

interfaceAlarmNoTxESFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 558)
)
interfaceAlarmNoTxESFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoTxESFail.setStatus(
        "current"
    )

equipmentAlarmSwitchLineAnotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 559)
)
equipmentAlarmSwitchLineAnotAvail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmSwitchLineAnotAvail.setStatus(
        "current"
    )

equipmentAlarmSwitchLineAavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 560)
)
equipmentAlarmSwitchLineAavail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmSwitchLineAavail.setStatus(
        "current"
    )

equipmentAlarmSwitchLineBnotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 561)
)
equipmentAlarmSwitchLineBnotAvail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmSwitchLineBnotAvail.setStatus(
        "current"
    )

equipmentAlarmSwitchLineBavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 562)
)
equipmentAlarmSwitchLineBavail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmSwitchLineBavail.setStatus(
        "current"
    )

interfaceAlarmRxSignalOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 563)
)
interfaceAlarmRxSignalOverload.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmRxSignalOverload.setStatus(
        "current"
    )

interfaceAlarmNoRxSignalOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 564)
)
interfaceAlarmNoRxSignalOverload.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoRxSignalOverload.setStatus(
        "current"
    )

interfaceAlarmLaserDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 565)
)
interfaceAlarmLaserDegrade.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserDegrade.setStatus(
        "current"
    )

interfaceAlarmNoLaserDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 566)
)
interfaceAlarmNoLaserDegrade.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLaserDegrade.setStatus(
        "current"
    )

interfaceAlarmLaserBiasEoL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 567)
)
interfaceAlarmLaserBiasEoL.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserBiasEoL.setStatus(
        "current"
    )

interfaceAlarmNoLaserBiasEoL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 568)
)
interfaceAlarmNoLaserBiasEoL.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLaserBiasEoL.setStatus(
        "current"
    )

interfaceAlarmLaserTecEoL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 569)
)
interfaceAlarmLaserTecEoL.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTecEoL.setStatus(
        "current"
    )

interfaceAlarmNoLaserTecEoL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 570)
)
interfaceAlarmNoLaserTecEoL.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLaserTecEoL.setStatus(
        "current"
    )

interfaceAlarmSubModTempOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 571)
)
interfaceAlarmSubModTempOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmSubModTempOoR.setStatus(
        "current"
    )

interfaceAlarmSubModTempNotOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 572)
)
interfaceAlarmSubModTempNotOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmSubModTempNotOoR.setStatus(
        "current"
    )

interfaceAlarmLaserTempOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 573)
)
interfaceAlarmLaserTempOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTempOoR.setStatus(
        "current"
    )

interfaceAlarmLaserTempNotOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 574)
)
interfaceAlarmLaserTempNotOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTempNotOoR.setStatus(
        "current"
    )

interfaceAlarmLossOfOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 575)
)
interfaceAlarmLossOfOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfOOP.setStatus(
        "current"
    )

interfaceAlarmNoLossOfOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 576)
)
interfaceAlarmNoLossOfOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfOOP.setStatus(
        "current"
    )

interfaceAlarmLossOfOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 577)
)
interfaceAlarmLossOfOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfOIP.setStatus(
        "current"
    )

interfaceAlarmNoLossOfOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 578)
)
interfaceAlarmNoLossOfOIP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfOIP.setStatus(
        "current"
    )

interfaceAlarmHwOIPTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 579)
)
interfaceAlarmHwOIPTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHwOIPTooHigh.setStatus(
        "current"
    )

interfaceAlarmHwOIPNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 580)
)
interfaceAlarmHwOIPNotTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHwOIPNotTooHigh.setStatus(
        "current"
    )

interfaceAlarmHwOOPTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 581)
)
interfaceAlarmHwOOPTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHwOOPTooLow.setStatus(
        "current"
    )

interfaceAlarmHwOOPNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 582)
)
interfaceAlarmHwOOPNotTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmHwOOPNotTooLow.setStatus(
        "current"
    )

interfaceAlarmLineAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 583)
)
interfaceAlarmLineAIS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLineAIS.setStatus(
        "current"
    )

interfaceAlarmNoLineAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 584)
)
interfaceAlarmNoLineAIS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLineAIS.setStatus(
        "current"
    )

interfaceAlarmLineRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 585)
)
interfaceAlarmLineRDI.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLineRDI.setStatus(
        "current"
    )

interfaceAlarmNoLineRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 586)
)
interfaceAlarmNoLineRDI.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLineRDI.setStatus(
        "current"
    )

interfaceAlarmSectionTraceMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 587)
)
interfaceAlarmSectionTraceMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmSectionTraceMismatch.setStatus(
        "current"
    )

interfaceAlarmNoSectionTraceMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 588)
)
interfaceAlarmNoSectionTraceMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoSectionTraceMismatch.setStatus(
        "current"
    )

interfaceAlarmSectionTraceInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 589)
)
interfaceAlarmSectionTraceInconsistency.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmSectionTraceInconsistency.setStatus(
        "current"
    )

interfaceAlarmNoSectionTraceInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 590)
)
interfaceAlarmNoSectionTraceInconsistency.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoSectionTraceInconsistency.setStatus(
        "current"
    )

interfaceAlarmLossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 591)
)
interfaceAlarmLossOfPointer.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfPointer.setStatus(
        "current"
    )

interfaceAlarmNoLossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 592)
)
interfaceAlarmNoLossOfPointer.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfPointer.setStatus(
        "current"
    )

interfaceAlarmPathAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 593)
)
interfaceAlarmPathAIS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmPathAIS.setStatus(
        "current"
    )

interfaceAlarmNoPathAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 594)
)
interfaceAlarmNoPathAIS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoPathAIS.setStatus(
        "current"
    )

interfaceAlarmPathRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 595)
)
interfaceAlarmPathRDI.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmPathRDI.setStatus(
        "current"
    )

interfaceAlarmNoPathRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 596)
)
interfaceAlarmNoPathRDI.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoPathRDI.setStatus(
        "current"
    )

interfaceAlarmPathSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 597)
)
interfaceAlarmPathSignalDegrade.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmPathSignalDegrade.setStatus(
        "current"
    )

interfaceAlarmNoPathSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 598)
)
interfaceAlarmNoPathSignalDegrade.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoPathSignalDegrade.setStatus(
        "current"
    )

interfaceAlarmServicePathLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 599)
)
interfaceAlarmServicePathLOF.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmServicePathLOF.setStatus(
        "current"
    )

interfaceAlarmNoServicePathLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 600)
)
interfaceAlarmNoServicePathLOF.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoServicePathLOF.setStatus(
        "current"
    )

interfaceAlarmServicePathAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 601)
)
interfaceAlarmServicePathAIS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmServicePathAIS.setStatus(
        "current"
    )

interfaceAlarmNoServicePathAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 602)
)
interfaceAlarmNoServicePathAIS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoServicePathAIS.setStatus(
        "current"
    )

interfaceAlarmServicePathRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 603)
)
interfaceAlarmServicePathRDI.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmServicePathRDI.setStatus(
        "current"
    )

interfaceAlarmNoServicePathRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 604)
)
interfaceAlarmNoServicePathRDI.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoServicePathRDI.setStatus(
        "current"
    )

interfaceAlarmServicePathPLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 605)
)
interfaceAlarmServicePathPLM.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmServicePathPLM.setStatus(
        "current"
    )

interfaceAlarmNoServicePathPLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 606)
)
interfaceAlarmNoServicePathPLM.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoServicePathPLM.setStatus(
        "current"
    )

equipmentAlarmSwitchPosError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 609)
)
equipmentAlarmSwitchPosError.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmSwitchPosError.setStatus(
        "current"
    )

equipmentAlarmSwitchNoPosError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 610)
)
equipmentAlarmSwitchNoPosError.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmSwitchNoPosError.setStatus(
        "current"
    )

interfaceAlarmServicePathUNEQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 611)
)
interfaceAlarmServicePathUNEQ.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmServicePathUNEQ.setStatus(
        "current"
    )

interfaceAlarmNoServicePathUNEQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 612)
)
interfaceAlarmNoServicePathUNEQ.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoServicePathUNEQ.setStatus(
        "current"
    )

interfaceAlarmPathPLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 613)
)
interfaceAlarmPathPLM.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmPathPLM.setStatus(
        "current"
    )

interfaceAlarmNoPathPLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 614)
)
interfaceAlarmNoPathPLM.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoPathPLM.setStatus(
        "current"
    )

interfaceAlarmPathUNEQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 615)
)
interfaceAlarmPathUNEQ.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmPathUNEQ.setStatus(
        "current"
    )

interfaceAlarmNoPathUNEQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 616)
)
interfaceAlarmNoPathUNEQ.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoPathUNEQ.setStatus(
        "current"
    )

equipmentAlarmMultipleFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 617)
)
equipmentAlarmMultipleFanFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmMultipleFanFail.setStatus(
        "current"
    )

equipmentAlarmMultipleFanNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 618)
)
equipmentAlarmMultipleFanNoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmMultipleFanNoFail.setStatus(
        "current"
    )

equipmentAlarmOscmBranchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 619)
)
equipmentAlarmOscmBranchError.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmOscmBranchError.setStatus(
        "current"
    )

equipmentAlarmOscmBranchNoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 620)
)
equipmentAlarmOscmBranchNoError.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmOscmBranchNoError.setStatus(
        "current"
    )

interfaceAlarmOtuFecLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 621)
)
interfaceAlarmOtuFecLossOfFrame.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOtuFecLossOfFrame.setStatus(
        "current"
    )

interfaceAlarmNoOtuFecLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 622)
)
interfaceAlarmNoOtuFecLossOfFrame.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoOtuFecLossOfFrame.setStatus(
        "current"
    )

interfaceAlarmSwitchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 623)
)
interfaceAlarmSwitchError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmSwitchError.setStatus(
        "current"
    )

interfaceAlarmNoSwitchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 624)
)
interfaceAlarmNoSwitchError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoSwitchError.setStatus(
        "current"
    )

equipmentAlarmExternalFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 625)
)
equipmentAlarmExternalFanFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExternalFanFail.setStatus(
        "current"
    )

equipmentAlarmExternalFanNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 626)
)
equipmentAlarmExternalFanNoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmExternalFanNoFail.setStatus(
        "current"
    )

equipmentAlarmPlannedCardMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 627)
)
equipmentAlarmPlannedCardMissing.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmPlannedCardMissing.setStatus(
        "current"
    )

equipmentAlarmNoPlannedCardMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 628)
)
equipmentAlarmNoPlannedCardMissing.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoPlannedCardMissing.setStatus(
        "current"
    )

equipmentAlarmPlannedCardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 629)
)
equipmentAlarmPlannedCardMismatch.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmPlannedCardMismatch.setStatus(
        "current"
    )

equipmentAlarmNoPlannedCardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 630)
)
equipmentAlarmNoPlannedCardMismatch.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoPlannedCardMismatch.setStatus(
        "current"
    )

equipmentAlarmProvisionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 631)
)
equipmentAlarmProvisionError.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmProvisionError.setStatus(
        "current"
    )

equipmentAlarmNoProvisionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 632)
)
equipmentAlarmNoProvisionError.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoProvisionError.setStatus(
        "current"
    )

interfaceAlarmSectSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 633)
)
interfaceAlarmSectSignalDegrade.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmSectSignalDegrade.setStatus(
        "current"
    )

interfaceAlarmNoSectSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 634)
)
interfaceAlarmNoSectSignalDegrade.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP3000-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoSectSignalDegrade.setStatus(
        "current"
    )

equipmentAlarmNoFeedback = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 641)
)
equipmentAlarmNoFeedback.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoFeedback.setStatus(
        "current"
    )

equipmentAlarmFeedbackAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 642)
)
equipmentAlarmFeedbackAvailable.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP3000-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFeedbackAvailable.setStatus(
        "current"
    )

protectionGroupProtectionFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 700)
)
protectionGroupProtectionFail.setObjects(
      *(("FSP3000-MIB", "channelCardProtectionGroupIndex"),
        ("FSP3000-MIB", "protectionGroupCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    protectionGroupProtectionFail.setStatus(
        "current"
    )

protectionGroupProtectionNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 701)
)
protectionGroupProtectionNoFail.setObjects(
      *(("FSP3000-MIB", "channelCardProtectionGroupIndex"),
        ("FSP3000-MIB", "protectionGroupCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    protectionGroupProtectionNoFail.setStatus(
        "current"
    )

protectionGroupProtectionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 702)
)
protectionGroupProtectionMismatch.setObjects(
      *(("FSP3000-MIB", "channelCardProtectionGroupIndex"),
        ("FSP3000-MIB", "protectionGroupCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    protectionGroupProtectionMismatch.setStatus(
        "current"
    )

protectionGroupProtectionNoMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4, 2, 3, 0, 703)
)
protectionGroupProtectionNoMismatch.setObjects(
      *(("FSP3000-MIB", "channelCardProtectionGroupIndex"),
        ("FSP3000-MIB", "protectionGroupCurrentAlarmSeverity"),
        ("FSP3000-MIB", "neEventLogTimeStamp"),
        ("FSP3000-MIB", "identityTranslation"))
)
if mibBuilder.loadTexts:
    protectionGroupProtectionNoMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSP3000-MIB",
    **{"InterfaceAlarmTypes": InterfaceAlarmTypes,
       "EquipmentAlarmTypes": EquipmentAlarmTypes,
       "InterfaceQoSReportTypes": InterfaceQoSReportTypes,
       "ProtectionGroupAlarmTypes": ProtectionGroupAlarmTypes,
       "TrapAlarmSeverity": TrapAlarmSeverity,
       "ProtectionCommand": ProtectionCommand,
       "ProtectionSwitchMode": ProtectionSwitchMode,
       "ProtectionState": ProtectionState,
       "AlarmSwitching": AlarmSwitching,
       "OnOff": OnOff,
       "TxState": TxState,
       "SwitchCommand": SwitchCommand,
       "AvailState": AvailState,
       "ContainerState": ContainerState,
       "PlannedState": PlannedState,
       "ContainsPhysicalIndex": ContainsPhysicalIndex,
       "ClockDataRate": ClockDataRate,
       "ClockType": ClockType,
       "LaserType": LaserType,
       "LoginIdentity": LoginIdentity,
       "TrapCounter": TrapCounter,
       "EnableState": EnableState,
       "OtuFecState": OtuFecState,
       "OtuFecSupported": OtuFecSupported,
       "ArcState": ArcState,
       "TimingSource": TimingSource,
       "ChannelRange": ChannelRange,
       "OscmTopologyMode": OscmTopologyMode,
       "OscmBranchMode": OscmBranchMode,
       "SwUpgradeStatusType": SwUpgradeStatusType,
       "IdentityTranslation": IdentityTranslation,
       "AlsMode": AlsMode,
       "AisState": AisState,
       "SectionType": SectionType,
       "PathType": PathType,
       "fsp3000Products": fsp3000Products,
       "fsp3000V1": fsp3000V1,
       "fsp3000MIB": fsp3000MIB,
       "alarmMIB": alarmMIB,
       "alarmFilters": alarmFilters,
       "interfaceAlarmSeverityTable": interfaceAlarmSeverityTable,
       "interfaceAlarmSeverityEntry": interfaceAlarmSeverityEntry,
       "interfaceAlarmSeverityType": interfaceAlarmSeverityType,
       "interfaceAlarmSeverityValue": interfaceAlarmSeverityValue,
       "equipmentAlarmSeverityTable": equipmentAlarmSeverityTable,
       "equipmentAlarmSeverityEntry": equipmentAlarmSeverityEntry,
       "equipmentAlarmSeverityType": equipmentAlarmSeverityType,
       "equipmentAlarmSeverityValue": equipmentAlarmSeverityValue,
       "interfaceAlarmReportControlTable": interfaceAlarmReportControlTable,
       "interfaceAlarmReportControlEntry": interfaceAlarmReportControlEntry,
       "interfaceAlarmReportControlState": interfaceAlarmReportControlState,
       "equipmentAlarmReportControlTable": equipmentAlarmReportControlTable,
       "equipmentAlarmReportControlEntry": equipmentAlarmReportControlEntry,
       "equipmentAlarmReportControlState": equipmentAlarmReportControlState,
       "interfaceQoSReportSeverityTable": interfaceQoSReportSeverityTable,
       "interfaceQoSReportSeverityEntry": interfaceQoSReportSeverityEntry,
       "interfaceQoSReportSeverityType": interfaceQoSReportSeverityType,
       "interfaceQoSReportSeverityValue": interfaceQoSReportSeverityValue,
       "currentAlarms": currentAlarms,
       "interfaceCurrentAlarmTable": interfaceCurrentAlarmTable,
       "interfaceCurrentAlarmEntry": interfaceCurrentAlarmEntry,
       "interfaceCurrentAlarmType": interfaceCurrentAlarmType,
       "interfaceCurrentAlarmSeverity": interfaceCurrentAlarmSeverity,
       "equipmentCurrentAlarmTable": equipmentCurrentAlarmTable,
       "equipmentCurrentAlarmEntry": equipmentCurrentAlarmEntry,
       "equipmentCurrentAlarmType": equipmentCurrentAlarmType,
       "equipmentCurrentAlarmSeverity": equipmentCurrentAlarmSeverity,
       "interfaceCurrentQoSReportTable": interfaceCurrentQoSReportTable,
       "interfaceCurrentQoSReportEntry": interfaceCurrentQoSReportEntry,
       "interfaceCurrentQoSReportType": interfaceCurrentQoSReportType,
       "interfaceCurrentQoSReportSeverity": interfaceCurrentQoSReportSeverity,
       "protectionGroupCurrentAlarmTable": protectionGroupCurrentAlarmTable,
       "protectionGroupCurrentAlarmEntry": protectionGroupCurrentAlarmEntry,
       "protectionGroupCurrentAlarmType": protectionGroupCurrentAlarmType,
       "protectionGroupCurrentAlarmSeverity": protectionGroupCurrentAlarmSeverity,
       "adminMIB": adminMIB,
       "neType": neType,
       "neMibVariant": neMibVariant,
       "neTrapsinkTable": neTrapsinkTable,
       "neTrapsinkEntry": neTrapsinkEntry,
       "neTrapsinkNumber": neTrapsinkNumber,
       "neTrapsinkAddress": neTrapsinkAddress,
       "neTrapsinkCommunity": neTrapsinkCommunity,
       "neTrapsinkPriority": neTrapsinkPriority,
       "neTrapsinkPort": neTrapsinkPort,
       "neLogfileTable": neLogfileTable,
       "neLogfileEntry": neLogfileEntry,
       "neLogfileNumber": neLogfileNumber,
       "neLogfileName": neLogfileName,
       "neLogfileSize": neLogfileSize,
       "neLogfilePriority": neLogfilePriority,
       "neEventsLogged": neEventsLogged,
       "neNmsTable": neNmsTable,
       "neNmsEntry": neNmsEntry,
       "neNmsNumber": neNmsNumber,
       "neNmsAddress": neNmsAddress,
       "neNmsName": neNmsName,
       "neManufacturer": neManufacturer,
       "neNmsFilter": neNmsFilter,
       "dcnDetectedTopologyType": dcnDetectedTopologyType,
       "dcnTopologyTable": dcnTopologyTable,
       "dcnTopologyEntry": dcnTopologyEntry,
       "dcnTopologyIndex": dcnTopologyIndex,
       "dcnTopologyNodeIpAddress": dcnTopologyNodeIpAddress,
       "neNextNeTrapsinkNumber": neNextNeTrapsinkNumber,
       "neEventLogSize": neEventLogSize,
       "neEventLogTable": neEventLogTable,
       "neEventLogEntry": neEventLogEntry,
       "neEventLogIndex": neEventLogIndex,
       "neEventLogTimeStamp": neEventLogTimeStamp,
       "neEventLogNotificationOID": neEventLogNotificationOID,
       "neEventLogVarTable": neEventLogVarTable,
       "neEventLogVarEntry": neEventLogVarEntry,
       "neEventLogVarIndex": neEventLogVarIndex,
       "neEventLogVarId": neEventLogVarId,
       "neEventLogVarType": neEventLogVarType,
       "neEventLogVarInteger32Val": neEventLogVarInteger32Val,
       "neEventLogVarOctetStringVal": neEventLogVarOctetStringVal,
       "neShelfTable": neShelfTable,
       "neShelfEntry": neShelfEntry,
       "neShelfSize": neShelfSize,
       "neShelfIdentifier": neShelfIdentifier,
       "dcnSecurityMode": dcnSecurityMode,
       "oscmTopologyTable": oscmTopologyTable,
       "oscmTopologyEntry": oscmTopologyEntry,
       "oscmTopologyIndex": oscmTopologyIndex,
       "oscmTopologyAddress": oscmTopologyAddress,
       "oscmTopologyNetmask": oscmTopologyNetmask,
       "oscmDetectedTopologyTable": oscmDetectedTopologyTable,
       "oscmDetectedTopologyEntry": oscmDetectedTopologyEntry,
       "oscmDetectedTopologyType": oscmDetectedTopologyType,
       "softwareUpgradeMIB": softwareUpgradeMIB,
       "actualFspSwVersion": actualFspSwVersion,
       "previousFspSwVersion": previousFspSwVersion,
       "fspSwUpgradeTable": fspSwUpgradeTable,
       "fspSwUpgradeEntry": fspSwUpgradeEntry,
       "fspSwUpgradeIndex": fspSwUpgradeIndex,
       "fspSwUpgradeServerIpAddress": fspSwUpgradeServerIpAddress,
       "fspSwUpgradeServerLogin": fspSwUpgradeServerLogin,
       "fspSwUpgradeServerPassword": fspSwUpgradeServerPassword,
       "fspSwUpgradeServerFileLocation": fspSwUpgradeServerFileLocation,
       "fspSwUpgradeFileName": fspSwUpgradeFileName,
       "fspSwUpgradeType": fspSwUpgradeType,
       "fspSwUpgradeRequest": fspSwUpgradeRequest,
       "fspSwUpgradeStatus": fspSwUpgradeStatus,
       "fspRebootTable": fspRebootTable,
       "fspRebootEntry": fspRebootEntry,
       "fspRebootType": fspRebootType,
       "fspRebootTimeStamp": fspRebootTimeStamp,
       "ucmSwUpgradeTable": ucmSwUpgradeTable,
       "ucmSwUpgradeEntry": ucmSwUpgradeEntry,
       "ucmSwUpgradeCurrentVersion": ucmSwUpgradeCurrentVersion,
       "ucmSwUpgradeAvailableVersion": ucmSwUpgradeAvailableVersion,
       "ucmSwUpgradeRequest": ucmSwUpgradeRequest,
       "ucmSwUpgradeStatus": ucmSwUpgradeStatus,
       "plannedConfigTable": plannedConfigTable,
       "plannedConfigEntry": plannedConfigEntry,
       "plannedConfigContainedIn": plannedConfigContainedIn,
       "plannedConfigClass": plannedConfigClass,
       "plannedConfigParentRelPos": plannedConfigParentRelPos,
       "plannedConfigName": plannedConfigName,
       "plannedConfigState": plannedConfigState,
       "plannedConfigRequest": plannedConfigRequest,
       "plannedConfigCardType": plannedConfigCardType,
       "plannedConfigProperty1": plannedConfigProperty1,
       "plannedConfigProperty2": plannedConfigProperty2,
       "plannedConfigProperty3": plannedConfigProperty3,
       "plannedConfigProperty4": plannedConfigProperty4,
       "plannedConfigDescr": plannedConfigDescr,
       "supportedCardTable": supportedCardTable,
       "supportedCardEntry": supportedCardEntry,
       "supportedCardIndex": supportedCardIndex,
       "supportedCardType": supportedCardType,
       "supportedCardClockType": supportedCardClockType,
       "supportedCardName": supportedCardName,
       "supportedCardProperties": supportedCardProperties,
       "neAutoProvisioning": neAutoProvisioning,
       "neCurrentDateAndTime": neCurrentDateAndTime,
       "neBackupRestore": neBackupRestore,
       "neBackupRestoreRequest": neBackupRestoreRequest,
       "neBackupRestoreState": neBackupRestoreState,
       "neBackupRestoreFile": neBackupRestoreFile,
       "neRestoreFileBackupDate": neRestoreFileBackupDate,
       "trapMIB": trapMIB,
       "trapMibPrefix": trapMibPrefix,
       "equipmentHolderObjectCreation": equipmentHolderObjectCreation,
       "equipmentHolderObjectDeletion": equipmentHolderObjectDeletion,
       "containerStateChange": containerStateChange,
       "protectionStateChange": protectionStateChange,
       "neAttributeValueChange": neAttributeValueChange,
       "interfaceAttributeValueChange": interfaceAttributeValueChange,
       "equipmentAttributeValueChange": equipmentAttributeValueChange,
       "protectionAttributeValueChange": protectionAttributeValueChange,
       "dcnTopologyReported": dcnTopologyReported,
       "equipmentStateChange": equipmentStateChange,
       "neTrapsinkObjectCreation": neTrapsinkObjectCreation,
       "neTrapsinkObjectDeletion": neTrapsinkObjectDeletion,
       "sonetSectionTraceChanged": sonetSectionTraceChanged,
       "loginDetected": loginDetected,
       "interfacePerfAttributeValueChange": interfacePerfAttributeValueChange,
       "equipmentPerfAttributeValueChange": equipmentPerfAttributeValueChange,
       "snmpConfigChanged": snmpConfigChanged,
       "fspSwUpgradeStateChange": fspSwUpgradeStateChange,
       "fspSwUpgradeAttributeValueChange": fspSwUpgradeAttributeValueChange,
       "oscmTopologyReported": oscmTopologyReported,
       "sectionQoSThresholdChanged": sectionQoSThresholdChanged,
       "pathQoSThresholdChanged": pathQoSThresholdChanged,
       "interfaceAlarmLowestCurrent": interfaceAlarmLowestCurrent,
       "interfaceAlarmNoLowestCurrent": interfaceAlarmNoLowestCurrent,
       "interfaceAlarmLowCurrent": interfaceAlarmLowCurrent,
       "interfaceAlarmNoLowCurrent": interfaceAlarmNoLowCurrent,
       "interfaceAlarmHighCurrent": interfaceAlarmHighCurrent,
       "interfaceAlarmNoHighCurrent": interfaceAlarmNoHighCurrent,
       "interfaceAlarmHighestCurrent": interfaceAlarmHighestCurrent,
       "interfaceAlarmNoHighestCurrent": interfaceAlarmNoHighestCurrent,
       "interfaceAlarmLowestOIP": interfaceAlarmLowestOIP,
       "interfaceAlarmNoLowestOIP": interfaceAlarmNoLowestOIP,
       "interfaceAlarmLowOIP": interfaceAlarmLowOIP,
       "interfaceAlarmNoLowOIP": interfaceAlarmNoLowOIP,
       "interfaceAlarmHighOIP": interfaceAlarmHighOIP,
       "interfaceAlarmNoHighOIP": interfaceAlarmNoHighOIP,
       "interfaceAlarmHighestOIP": interfaceAlarmHighestOIP,
       "interfaceAlarmNoHighestOIP": interfaceAlarmNoHighestOIP,
       "interfaceAlarmLowestOOP": interfaceAlarmLowestOOP,
       "interfaceAlarmNoLowestOOP": interfaceAlarmNoLowestOOP,
       "interfaceAlarmLowOOP": interfaceAlarmLowOOP,
       "interfaceAlarmNoLowOOP": interfaceAlarmNoLowOOP,
       "interfaceAlarmHighOOP": interfaceAlarmHighOOP,
       "interfaceAlarmNoHighOOP": interfaceAlarmNoHighOOP,
       "interfaceAlarmHighestOOP": interfaceAlarmHighestOOP,
       "interfaceAlarmNoHighestOOP": interfaceAlarmNoHighestOOP,
       "equipmentAlarmLowestTemp": equipmentAlarmLowestTemp,
       "equipmentAlarmNoLowestTemp": equipmentAlarmNoLowestTemp,
       "equipmentAlarmLowTemp": equipmentAlarmLowTemp,
       "equipmentAlarmNoLowTemp": equipmentAlarmNoLowTemp,
       "equipmentAlarmHighTemp": equipmentAlarmHighTemp,
       "equipmentAlarmNoHighTemp": equipmentAlarmNoHighTemp,
       "equipmentAlarmHighestTemp": equipmentAlarmHighestTemp,
       "equipmentAlarmNoHighestTemp": equipmentAlarmNoHighestTemp,
       "equipmentAlarmLowestVolt": equipmentAlarmLowestVolt,
       "equipmentAlarmNoLowestVolt": equipmentAlarmNoLowestVolt,
       "equipmentAlarmLowVolt": equipmentAlarmLowVolt,
       "equipmentAlarmNoLowVolt": equipmentAlarmNoLowVolt,
       "equipmentAlarmHighVolt": equipmentAlarmHighVolt,
       "equipmentAlarmNoHighVolt": equipmentAlarmNoHighVolt,
       "equipmentAlarmHighestVolt": equipmentAlarmHighestVolt,
       "equipmentAlarmNoHighestVolt": equipmentAlarmNoHighestVolt,
       "equipmentAlarmLowestCurrent": equipmentAlarmLowestCurrent,
       "equipmentAlarmNoLowestCurrent": equipmentAlarmNoLowestCurrent,
       "equipmentAlarmLowCurrent": equipmentAlarmLowCurrent,
       "equipmentAlarmNoLowCurrent": equipmentAlarmNoLowCurrent,
       "equipmentAlarmHighCurrent": equipmentAlarmHighCurrent,
       "equipmentAlarmNoHighCurrent": equipmentAlarmNoHighCurrent,
       "equipmentAlarmHighestCurrent": equipmentAlarmHighestCurrent,
       "equipmentAlarmNoHighestCurrent": equipmentAlarmNoHighestCurrent,
       "interfaceQoSReportSection15minES": interfaceQoSReportSection15minES,
       "interfaceQoSReportSection15minNoES": interfaceQoSReportSection15minNoES,
       "interfaceQoSReportSection15minSES": interfaceQoSReportSection15minSES,
       "interfaceQoSReportSection15minNoSES": interfaceQoSReportSection15minNoSES,
       "interfaceQoSReportSection15minSEFS": interfaceQoSReportSection15minSEFS,
       "interfaceQoSReportSection15minNoSEFS": interfaceQoSReportSection15minNoSEFS,
       "interfaceQoSReportSection15minCV": interfaceQoSReportSection15minCV,
       "interfaceQoSReportSection15minNoCV": interfaceQoSReportSection15minNoCV,
       "interfaceQoSReportSection24hrES": interfaceQoSReportSection24hrES,
       "interfaceQoSReportSection24hrNoES": interfaceQoSReportSection24hrNoES,
       "interfaceQoSReportSection24hrSES": interfaceQoSReportSection24hrSES,
       "interfaceQoSReportSection24hrNoSES": interfaceQoSReportSection24hrNoSES,
       "interfaceQoSReportSection24hrSEFS": interfaceQoSReportSection24hrSEFS,
       "interfaceQoSReportSection24hrNoSEFS": interfaceQoSReportSection24hrNoSEFS,
       "interfaceQoSReportSection24hrCV": interfaceQoSReportSection24hrCV,
       "interfaceQoSReportSection24hrNoCV": interfaceQoSReportSection24hrNoCV,
       "interfaceQoSReportPath15minES": interfaceQoSReportPath15minES,
       "interfaceQoSReportPath15minNoES": interfaceQoSReportPath15minNoES,
       "interfaceQoSReportPath15minSES": interfaceQoSReportPath15minSES,
       "interfaceQoSReportPath15minNoSES": interfaceQoSReportPath15minNoSES,
       "interfaceQoSReportPath15minCV": interfaceQoSReportPath15minCV,
       "interfaceQoSReportPath15minNoCV": interfaceQoSReportPath15minNoCV,
       "interfaceQoSReportPath15minUAS": interfaceQoSReportPath15minUAS,
       "interfaceQoSReportPath15minNoUAS": interfaceQoSReportPath15minNoUAS,
       "interfaceQoSReportPath24hrES": interfaceQoSReportPath24hrES,
       "interfaceQoSReportPath24hrNoES": interfaceQoSReportPath24hrNoES,
       "interfaceQoSReportPath24hrSES": interfaceQoSReportPath24hrSES,
       "interfaceQoSReportPath24hrNoSES": interfaceQoSReportPath24hrNoSES,
       "interfaceQoSReportPath24hrCV": interfaceQoSReportPath24hrCV,
       "interfaceQoSReportPath24hrNoCV": interfaceQoSReportPath24hrNoCV,
       "interfaceQoSReportPath24hrUAS": interfaceQoSReportPath24hrUAS,
       "interfaceQoSReportPath24hrNoUAS": interfaceQoSReportPath24hrNoUAS,
       "interfaceAlarmLossOfSignal": interfaceAlarmLossOfSignal,
       "interfaceAlarmNoLossOfSignal": interfaceAlarmNoLossOfSignal,
       "interfaceAlarmLossOfLinkPulse": interfaceAlarmLossOfLinkPulse,
       "interfaceAlarmNoLossOfLinkPulse": interfaceAlarmNoLossOfLinkPulse,
       "equipmentAlarmFuse1Fail": equipmentAlarmFuse1Fail,
       "equipmentAlarmFuse1NoFail": equipmentAlarmFuse1NoFail,
       "equipmentAlarmFuse2Fail": equipmentAlarmFuse2Fail,
       "equipmentAlarmFuse2NoFail": equipmentAlarmFuse2NoFail,
       "equipmentAlarmFan1Fail": equipmentAlarmFan1Fail,
       "equipmentAlarmFan1NoFail": equipmentAlarmFan1NoFail,
       "equipmentAlarmFan2Fail": equipmentAlarmFan2Fail,
       "equipmentAlarmFan2NoFail": equipmentAlarmFan2NoFail,
       "equipmentAlarmFan3Fail": equipmentAlarmFan3Fail,
       "equipmentAlarmFan3NoFail": equipmentAlarmFan3NoFail,
       "equipmentAlarmFanPs1Fail": equipmentAlarmFanPs1Fail,
       "equipmentAlarmFanPs1NoFail": equipmentAlarmFanPs1NoFail,
       "equipmentAlarmFanPs2Fail": equipmentAlarmFanPs2Fail,
       "equipmentAlarmFanPs2NoFail": equipmentAlarmFanPs2NoFail,
       "equipmentAlarmPsFail": equipmentAlarmPsFail,
       "equipmentAlarmPsNoFail": equipmentAlarmPsNoFail,
       "equipmentAlarmExtInput1": equipmentAlarmExtInput1,
       "equipmentAlarmExtInput1Ok": equipmentAlarmExtInput1Ok,
       "equipmentAlarmExtInput2": equipmentAlarmExtInput2,
       "equipmentAlarmExtInput2Ok": equipmentAlarmExtInput2Ok,
       "equipmentAlarmExtInput3": equipmentAlarmExtInput3,
       "equipmentAlarmExtInput3Ok": equipmentAlarmExtInput3Ok,
       "equipmentAlarmExtInput4": equipmentAlarmExtInput4,
       "equipmentAlarmExtInput4Ok": equipmentAlarmExtInput4Ok,
       "equipmentAlarmExtInput5": equipmentAlarmExtInput5,
       "equipmentAlarmExtInput5Ok": equipmentAlarmExtInput5Ok,
       "equipmentAlarmExtInput6": equipmentAlarmExtInput6,
       "equipmentAlarmExtInput6Ok": equipmentAlarmExtInput6Ok,
       "equipmentAlarmExtInput7": equipmentAlarmExtInput7,
       "equipmentAlarmExtInput7Ok": equipmentAlarmExtInput7Ok,
       "equipmentAlarmExtInput8": equipmentAlarmExtInput8,
       "equipmentAlarmExtInput8Ok": equipmentAlarmExtInput8Ok,
       "equipmentAlarmExtInput9": equipmentAlarmExtInput9,
       "equipmentAlarmExtInput9Ok": equipmentAlarmExtInput9Ok,
       "equipmentAlarmExtInput10": equipmentAlarmExtInput10,
       "equipmentAlarmExtInput10Ok": equipmentAlarmExtInput10Ok,
       "equipmentAlarmExtInput11": equipmentAlarmExtInput11,
       "equipmentAlarmExtInput11Ok": equipmentAlarmExtInput11Ok,
       "equipmentAlarmExtInput12": equipmentAlarmExtInput12,
       "equipmentAlarmExtInput12Ok": equipmentAlarmExtInput12Ok,
       "interfaceAlarmLossOfClock": interfaceAlarmLossOfClock,
       "interfaceAlarmNoLossOfClock": interfaceAlarmNoLossOfClock,
       "interfaceAlarmTxClockFail": interfaceAlarmTxClockFail,
       "interfaceAlarmNoTxClockFail": interfaceAlarmNoTxClockFail,
       "interfaceAlarmLossOfFrame": interfaceAlarmLossOfFrame,
       "interfaceAlarmNoLossOfFrame": interfaceAlarmNoLossOfFrame,
       "interfaceAlarmRxESFail": interfaceAlarmRxESFail,
       "interfaceAlarmNoRxESFail": interfaceAlarmNoRxESFail,
       "interfaceAlarmTxESFail": interfaceAlarmTxESFail,
       "interfaceAlarmNoTxESFail": interfaceAlarmNoTxESFail,
       "equipmentAlarmSwitchLineAnotAvail": equipmentAlarmSwitchLineAnotAvail,
       "equipmentAlarmSwitchLineAavail": equipmentAlarmSwitchLineAavail,
       "equipmentAlarmSwitchLineBnotAvail": equipmentAlarmSwitchLineBnotAvail,
       "equipmentAlarmSwitchLineBavail": equipmentAlarmSwitchLineBavail,
       "interfaceAlarmRxSignalOverload": interfaceAlarmRxSignalOverload,
       "interfaceAlarmNoRxSignalOverload": interfaceAlarmNoRxSignalOverload,
       "interfaceAlarmLaserDegrade": interfaceAlarmLaserDegrade,
       "interfaceAlarmNoLaserDegrade": interfaceAlarmNoLaserDegrade,
       "interfaceAlarmLaserBiasEoL": interfaceAlarmLaserBiasEoL,
       "interfaceAlarmNoLaserBiasEoL": interfaceAlarmNoLaserBiasEoL,
       "interfaceAlarmLaserTecEoL": interfaceAlarmLaserTecEoL,
       "interfaceAlarmNoLaserTecEoL": interfaceAlarmNoLaserTecEoL,
       "interfaceAlarmSubModTempOoR": interfaceAlarmSubModTempOoR,
       "interfaceAlarmSubModTempNotOoR": interfaceAlarmSubModTempNotOoR,
       "interfaceAlarmLaserTempOoR": interfaceAlarmLaserTempOoR,
       "interfaceAlarmLaserTempNotOoR": interfaceAlarmLaserTempNotOoR,
       "interfaceAlarmLossOfOOP": interfaceAlarmLossOfOOP,
       "interfaceAlarmNoLossOfOOP": interfaceAlarmNoLossOfOOP,
       "interfaceAlarmLossOfOIP": interfaceAlarmLossOfOIP,
       "interfaceAlarmNoLossOfOIP": interfaceAlarmNoLossOfOIP,
       "interfaceAlarmHwOIPTooHigh": interfaceAlarmHwOIPTooHigh,
       "interfaceAlarmHwOIPNotTooHigh": interfaceAlarmHwOIPNotTooHigh,
       "interfaceAlarmHwOOPTooLow": interfaceAlarmHwOOPTooLow,
       "interfaceAlarmHwOOPNotTooLow": interfaceAlarmHwOOPNotTooLow,
       "interfaceAlarmLineAIS": interfaceAlarmLineAIS,
       "interfaceAlarmNoLineAIS": interfaceAlarmNoLineAIS,
       "interfaceAlarmLineRDI": interfaceAlarmLineRDI,
       "interfaceAlarmNoLineRDI": interfaceAlarmNoLineRDI,
       "interfaceAlarmSectionTraceMismatch": interfaceAlarmSectionTraceMismatch,
       "interfaceAlarmNoSectionTraceMismatch": interfaceAlarmNoSectionTraceMismatch,
       "interfaceAlarmSectionTraceInconsistency": interfaceAlarmSectionTraceInconsistency,
       "interfaceAlarmNoSectionTraceInconsistency": interfaceAlarmNoSectionTraceInconsistency,
       "interfaceAlarmLossOfPointer": interfaceAlarmLossOfPointer,
       "interfaceAlarmNoLossOfPointer": interfaceAlarmNoLossOfPointer,
       "interfaceAlarmPathAIS": interfaceAlarmPathAIS,
       "interfaceAlarmNoPathAIS": interfaceAlarmNoPathAIS,
       "interfaceAlarmPathRDI": interfaceAlarmPathRDI,
       "interfaceAlarmNoPathRDI": interfaceAlarmNoPathRDI,
       "interfaceAlarmPathSignalDegrade": interfaceAlarmPathSignalDegrade,
       "interfaceAlarmNoPathSignalDegrade": interfaceAlarmNoPathSignalDegrade,
       "interfaceAlarmServicePathLOF": interfaceAlarmServicePathLOF,
       "interfaceAlarmNoServicePathLOF": interfaceAlarmNoServicePathLOF,
       "interfaceAlarmServicePathAIS": interfaceAlarmServicePathAIS,
       "interfaceAlarmNoServicePathAIS": interfaceAlarmNoServicePathAIS,
       "interfaceAlarmServicePathRDI": interfaceAlarmServicePathRDI,
       "interfaceAlarmNoServicePathRDI": interfaceAlarmNoServicePathRDI,
       "interfaceAlarmServicePathPLM": interfaceAlarmServicePathPLM,
       "interfaceAlarmNoServicePathPLM": interfaceAlarmNoServicePathPLM,
       "equipmentAlarmSwitchPosError": equipmentAlarmSwitchPosError,
       "equipmentAlarmSwitchNoPosError": equipmentAlarmSwitchNoPosError,
       "interfaceAlarmServicePathUNEQ": interfaceAlarmServicePathUNEQ,
       "interfaceAlarmNoServicePathUNEQ": interfaceAlarmNoServicePathUNEQ,
       "interfaceAlarmPathPLM": interfaceAlarmPathPLM,
       "interfaceAlarmNoPathPLM": interfaceAlarmNoPathPLM,
       "interfaceAlarmPathUNEQ": interfaceAlarmPathUNEQ,
       "interfaceAlarmNoPathUNEQ": interfaceAlarmNoPathUNEQ,
       "equipmentAlarmMultipleFanFail": equipmentAlarmMultipleFanFail,
       "equipmentAlarmMultipleFanNoFail": equipmentAlarmMultipleFanNoFail,
       "equipmentAlarmOscmBranchError": equipmentAlarmOscmBranchError,
       "equipmentAlarmOscmBranchNoError": equipmentAlarmOscmBranchNoError,
       "interfaceAlarmOtuFecLossOfFrame": interfaceAlarmOtuFecLossOfFrame,
       "interfaceAlarmNoOtuFecLossOfFrame": interfaceAlarmNoOtuFecLossOfFrame,
       "interfaceAlarmSwitchError": interfaceAlarmSwitchError,
       "interfaceAlarmNoSwitchError": interfaceAlarmNoSwitchError,
       "equipmentAlarmExternalFanFail": equipmentAlarmExternalFanFail,
       "equipmentAlarmExternalFanNoFail": equipmentAlarmExternalFanNoFail,
       "equipmentAlarmPlannedCardMissing": equipmentAlarmPlannedCardMissing,
       "equipmentAlarmNoPlannedCardMissing": equipmentAlarmNoPlannedCardMissing,
       "equipmentAlarmPlannedCardMismatch": equipmentAlarmPlannedCardMismatch,
       "equipmentAlarmNoPlannedCardMismatch": equipmentAlarmNoPlannedCardMismatch,
       "equipmentAlarmProvisionError": equipmentAlarmProvisionError,
       "equipmentAlarmNoProvisionError": equipmentAlarmNoProvisionError,
       "interfaceAlarmSectSignalDegrade": interfaceAlarmSectSignalDegrade,
       "interfaceAlarmNoSectSignalDegrade": interfaceAlarmNoSectSignalDegrade,
       "equipmentAlarmNoFeedback": equipmentAlarmNoFeedback,
       "equipmentAlarmFeedbackAvailable": equipmentAlarmFeedbackAvailable,
       "protectionGroupProtectionFail": protectionGroupProtectionFail,
       "protectionGroupProtectionNoFail": protectionGroupProtectionNoFail,
       "protectionGroupProtectionMismatch": protectionGroupProtectionMismatch,
       "protectionGroupProtectionNoMismatch": protectionGroupProtectionNoMismatch,
       "trapVariables": trapVariables,
       "containerState": containerState,
       "containsPhysicalIndex": containsPhysicalIndex,
       "loginIdentity": loginIdentity,
       "sourceAddress": sourceAddress,
       "identityTranslation": identityTranslation,
       "configurationMIB": configurationMIB,
       "interfaceConfiguration": interfaceConfiguration,
       "interfaceTrailTerminationTable": interfaceTrailTerminationTable,
       "interfaceTrailTerminationEntry": interfaceTrailTerminationEntry,
       "interfaceTrailTerminationTrailIdentifier": interfaceTrailTerminationTrailIdentifier,
       "interfaceTrailTerminationLoopState": interfaceTrailTerminationLoopState,
       "interfaceTrailTerminationLaserTxState": interfaceTrailTerminationLaserTxState,
       "interfaceTrailTerminationLaserTxCurrent": interfaceTrailTerminationLaserTxCurrent,
       "interfaceTrailTerminationLaserTxTemp": interfaceTrailTerminationLaserTxTemp,
       "interfaceTrailTerminationRxClockFreq": interfaceTrailTerminationRxClockFreq,
       "interfaceTrailTerminationRxClockType": interfaceTrailTerminationRxClockType,
       "interfaceTrailTerminationWavelength": interfaceTrailTerminationWavelength,
       "interfaceTrailTerminationFspChannelNo": interfaceTrailTerminationFspChannelNo,
       "interfaceTrailTerminationOIP": interfaceTrailTerminationOIP,
       "interfaceTrailTerminationApdVoltage": interfaceTrailTerminationApdVoltage,
       "interfaceTrailTerminationOOP": interfaceTrailTerminationOOP,
       "interfaceTrailTerminationLaserType": interfaceTrailTerminationLaserType,
       "interfaceTrailTerminationFECState": interfaceTrailTerminationFECState,
       "interfaceTrailTerminationTimingSource": interfaceTrailTerminationTimingSource,
       "interfaceTrailTerminationFECOHMonitoring": interfaceTrailTerminationFECOHMonitoring,
       "interfaceTrailTerminationFECSupported": interfaceTrailTerminationFECSupported,
       "electricalInterfaceTable": electricalInterfaceTable,
       "electricalInterfaceEntry": electricalInterfaceEntry,
       "electricalInterfaceIdentifier": electricalInterfaceIdentifier,
       "electricalInterfaceTxAutoNegotiation": electricalInterfaceTxAutoNegotiation,
       "electricalInterfaceTxMode": electricalInterfaceTxMode,
       "electricalInterfaceLineSpeed": electricalInterfaceLineSpeed,
       "edfaInterfaceTable": edfaInterfaceTable,
       "edfaInterfaceEntry": edfaInterfaceEntry,
       "edfaInterfaceIdentifier": edfaInterfaceIdentifier,
       "edfaInterfaceOpticalBandType": edfaInterfaceOpticalBandType,
       "edfaInterfacePumpLaserTxState": edfaInterfacePumpLaserTxState,
       "edfaInterfaceOpticalInputPower": edfaInterfaceOpticalInputPower,
       "edfaInterfaceOpticalOutputPower": edfaInterfaceOpticalOutputPower,
       "edfaInterfaceSubModuleTemp": edfaInterfaceSubModuleTemp,
       "edfaInterfacePumpLaserPower": edfaInterfacePumpLaserPower,
       "edfaInterfacePumpLaserCurrent": edfaInterfacePumpLaserCurrent,
       "edfaInterfacePumpLaserTxTemp": edfaInterfacePumpLaserTxTemp,
       "edfaInterfacePumpLaserConfig": edfaInterfacePumpLaserConfig,
       "edfaInterfaceTECCurrent": edfaInterfaceTECCurrent,
       "edfaInterfaceMaxOperPower": edfaInterfaceMaxOperPower,
       "edfaInterfaceType": edfaInterfaceType,
       "sonetSectionTraceTable": sonetSectionTraceTable,
       "sonetSectionTraceEntry": sonetSectionTraceEntry,
       "sonetSectionTraceToExpect": sonetSectionTraceToExpect,
       "sonetSectionTraceReceived": sonetSectionTraceReceived,
       "sonetSectionTraceLength": sonetSectionTraceLength,
       "eccmInterfaceTable": eccmInterfaceTable,
       "eccmInterfaceEntry": eccmInterfaceEntry,
       "eccmInterfaceIdentifier": eccmInterfaceIdentifier,
       "eccmInterfaceSwitchState": eccmInterfaceSwitchState,
       "eccmInterfaceFspChannelNo": eccmInterfaceFspChannelNo,
       "eccmInterfaceWavelength": eccmInterfaceWavelength,
       "eccmInterfaceOIP": eccmInterfaceOIP,
       "apsInterfaceTable": apsInterfaceTable,
       "apsInterfaceEntry": apsInterfaceEntry,
       "apsInterfaceSwitchState": apsInterfaceSwitchState,
       "apsInterfaceOIPLoad": apsInterfaceOIPLoad,
       "apsInterfaceOipOsc": apsInterfaceOipOsc,
       "equipmentConfiguration": equipmentConfiguration,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleVoltage": moduleVoltage,
       "moduleEnvironmentTemp": moduleEnvironmentTemp,
       "moduleEnvironmentTempMax": moduleEnvironmentTempMax,
       "moduleSupervisionState": moduleSupervisionState,
       "moduleProtectionGroupIndex": moduleProtectionGroupIndex,
       "moduleCardType": moduleCardType,
       "moduleVoltageMax": moduleVoltageMax,
       "moduleVoltageMin": moduleVoltageMin,
       "moduleCardMode": moduleCardMode,
       "moduleSignalFormat": moduleSignalFormat,
       "moduleSdhSonetALSMode": moduleSdhSonetALSMode,
       "moduleSdhSonetAISGeneration": moduleSdhSonetAISGeneration,
       "moduleCouplingLinkMode": moduleCouplingLinkMode,
       "moduleFeederMode": moduleFeederMode,
       "moduleSdhSonetThresholds": moduleSdhSonetThresholds,
       "telemetryModuleTable": telemetryModuleTable,
       "telemetryModuleEntry": telemetryModuleEntry,
       "telemetryExtOutputIndex": telemetryExtOutputIndex,
       "telemetryExtOutputState": telemetryExtOutputState,
       "telemetryExtOutputIdentifier": telemetryExtOutputIdentifier,
       "channelCardProtectionTable": channelCardProtectionTable,
       "channelCardProtectionEntry": channelCardProtectionEntry,
       "channelCardProtectionGroupIndex": channelCardProtectionGroupIndex,
       "channelCardProtectionWestSlot": channelCardProtectionWestSlot,
       "channelCardProtectionEastSlot": channelCardProtectionEastSlot,
       "channelCardProtectionLastRequest": channelCardProtectionLastRequest,
       "channelCardProtectionSwitchMode": channelCardProtectionSwitchMode,
       "channelCardProtectionState": channelCardProtectionState,
       "channelCardProtectionGroupStatus": channelCardProtectionGroupStatus,
       "channelCardProtectionConfWorkingSlot": channelCardProtectionConfWorkingSlot,
       "channelCardProtectionSDswitching": channelCardProtectionSDswitching,
       "channelCardProtectionSonetSdhSwitching": channelCardProtectionSonetSdhSwitching,
       "channelCardProtectionSwitchHoldOffTime": channelCardProtectionSwitchHoldOffTime,
       "channelCardProtectionDualEndedSwitching": channelCardProtectionDualEndedSwitching,
       "remoteOpticalSwitchTable": remoteOpticalSwitchTable,
       "remoteOpticalSwitchEntry": remoteOpticalSwitchEntry,
       "remoteOpticalSwitchActiveLine": remoteOpticalSwitchActiveLine,
       "remoteOpticalSwitchMode": remoteOpticalSwitchMode,
       "remoteOpticalSwitchLastRequest": remoteOpticalSwitchLastRequest,
       "remoteOpticalSwitchRefLaserState": remoteOpticalSwitchRefLaserState,
       "remoteOpticalSwitchLineAState": remoteOpticalSwitchLineAState,
       "remoteOpticalSwitchLineBState": remoteOpticalSwitchLineBState,
       "remoteOpticalSwitchTxBias": remoteOpticalSwitchTxBias,
       "telemetryModuleInputTable": telemetryModuleInputTable,
       "telemetryModuleInputEntry": telemetryModuleInputEntry,
       "telemetryExtInputIndex": telemetryExtInputIndex,
       "telemetryExtInputIdentifier": telemetryExtInputIdentifier,
       "filterModuleTable": filterModuleTable,
       "filterModuleEntry": filterModuleEntry,
       "filterModuleChannelRange": filterModuleChannelRange,
       "filterModuleChannel": filterModuleChannel,
       "oscmTable": oscmTable,
       "oscmEntry": oscmEntry,
       "oscmTopologyMode": oscmTopologyMode,
       "oscmBranchMode": oscmBranchMode,
       "oscmActiveProtectionLine": oscmActiveProtectionLine,
       "oscmSwitchLastRequest": oscmSwitchLastRequest,
       "performanceMIB": performanceMIB,
       "performanceAdmin": performanceAdmin,
       "sonetPerformanceAdmin": sonetPerformanceAdmin,
       "sonetSdhPerformanceAdmin": sonetSdhPerformanceAdmin,
       "sonetSdhThresholdTable": sonetSdhThresholdTable,
       "sonetSdhThresholdEntry": sonetSdhThresholdEntry,
       "sonetSdhThresholdType": sonetSdhThresholdType,
       "sonetSdhThresholdSESValue": sonetSdhThresholdSESValue,
       "sectionQoSThresholdTable": sectionQoSThresholdTable,
       "sectionQoSThresholdEntry": sectionQoSThresholdEntry,
       "sectionQoSThresholdType": sectionQoSThresholdType,
       "sectionQoSThreshold15minState": sectionQoSThreshold15minState,
       "sectionQoSThreshold15minHigh": sectionQoSThreshold15minHigh,
       "sectionQoSThreshold15minLow": sectionQoSThreshold15minLow,
       "sectionQoSThreshold24hrState": sectionQoSThreshold24hrState,
       "sectionQoSThreshold24hrHigh": sectionQoSThreshold24hrHigh,
       "pathQoSThresholdTable": pathQoSThresholdTable,
       "pathQoSThresholdEntry": pathQoSThresholdEntry,
       "pathQoSThresholdType": pathQoSThresholdType,
       "pathQoSThreshold15minState": pathQoSThreshold15minState,
       "pathQoSThreshold15minHigh": pathQoSThreshold15minHigh,
       "pathQoSThreshold15minLow": pathQoSThreshold15minLow,
       "pathQoSThreshold24hrState": pathQoSThreshold24hrState,
       "pathQoSThreshold24hrHigh": pathQoSThreshold24hrHigh,
       "physicalPerformanceAdmin": physicalPerformanceAdmin,
       "modulePPthresholdTable": modulePPthresholdTable,
       "modulePPthresholdEntry": modulePPthresholdEntry,
       "modulePPthresholdLowestVolt": modulePPthresholdLowestVolt,
       "modulePPthresholdLowVolt": modulePPthresholdLowVolt,
       "modulePPthresholdHighVolt": modulePPthresholdHighVolt,
       "modulePPthresholdHighestVolt": modulePPthresholdHighestVolt,
       "modulePPhysteresisVolt": modulePPhysteresisVolt,
       "modulePPthresholdLowestTemp": modulePPthresholdLowestTemp,
       "modulePPthresholdLowTemp": modulePPthresholdLowTemp,
       "modulePPthresholdHighTemp": modulePPthresholdHighTemp,
       "modulePPthresholdHighestTemp": modulePPthresholdHighestTemp,
       "modulePPhysteresisTemp": modulePPhysteresisTemp,
       "remOptSwPPthresholdTable": remOptSwPPthresholdTable,
       "remOptSwPPthresholdEntry": remOptSwPPthresholdEntry,
       "remOptSwPPthresholdLowestTxBias": remOptSwPPthresholdLowestTxBias,
       "remOptSwPPthresholdLowTxBias": remOptSwPPthresholdLowTxBias,
       "remOptSwPPthresholdHighTxBias": remOptSwPPthresholdHighTxBias,
       "remOptSwPPthresholdHighestTxBias": remOptSwPPthresholdHighestTxBias,
       "remOptSwPPhysteresisTxBias": remOptSwPPhysteresisTxBias,
       "edfaPPthresholdTable": edfaPPthresholdTable,
       "edfaPPthresholdEntry": edfaPPthresholdEntry,
       "edfaPPthresholdLowestPumpCurrent": edfaPPthresholdLowestPumpCurrent,
       "edfaPPthresholdLowPumpCurrent": edfaPPthresholdLowPumpCurrent,
       "edfaPPthresholdHighPumpCurrent": edfaPPthresholdHighPumpCurrent,
       "edfaPPthresholdHighestPumpCurrent": edfaPPthresholdHighestPumpCurrent,
       "edfaPPhysteresisPumpCurrent": edfaPPhysteresisPumpCurrent,
       "edfaPPthresholdLowestOIP": edfaPPthresholdLowestOIP,
       "edfaPPthresholdLowOIP": edfaPPthresholdLowOIP,
       "edfaPPthresholdHighOIP": edfaPPthresholdHighOIP,
       "edfaPPthresholdHighestOIP": edfaPPthresholdHighestOIP,
       "edfaPPhysteresisOIP": edfaPPhysteresisOIP,
       "edfaPPthresholdLowestOOP": edfaPPthresholdLowestOOP,
       "edfaPPthresholdLowOOP": edfaPPthresholdLowOOP,
       "edfaPPthresholdHighOOP": edfaPPthresholdHighOOP,
       "edfaPPthresholdHighestOOP": edfaPPthresholdHighestOOP,
       "edfaPPhysteresisOOP": edfaPPhysteresisOOP,
       "interfaceTTPPthresholdTable": interfaceTTPPthresholdTable,
       "interfaceTTPPthresholdEntry": interfaceTTPPthresholdEntry,
       "interfaceTTPPthresholdLowestTxBias": interfaceTTPPthresholdLowestTxBias,
       "interfaceTTPPthresholdLowTxBias": interfaceTTPPthresholdLowTxBias,
       "interfaceTTPPthresholdHighTxBias": interfaceTTPPthresholdHighTxBias,
       "interfaceTTPPthresholdHighestTxBias": interfaceTTPPthresholdHighestTxBias,
       "interfaceTTPPhysteresisTxBias": interfaceTTPPhysteresisTxBias,
       "interfaceTTPPthresholdLowestRxOIP": interfaceTTPPthresholdLowestRxOIP,
       "interfaceTTPPthresholdLowRxOIP": interfaceTTPPthresholdLowRxOIP,
       "interfaceTTPPthresholdHighRxOIP": interfaceTTPPthresholdHighRxOIP,
       "interfaceTTPPthresholdHighestRxOIP": interfaceTTPPthresholdHighestRxOIP,
       "interfaceTTPPhysteresisRxOIP": interfaceTTPPhysteresisRxOIP,
       "eccmPPthresholdTable": eccmPPthresholdTable,
       "eccmPPthresholdEntry": eccmPPthresholdEntry,
       "eccmPPthresholdLowestRxOIP": eccmPPthresholdLowestRxOIP,
       "eccmPPthresholdLowRxOIP": eccmPPthresholdLowRxOIP,
       "eccmPPthresholdHighRxOIP": eccmPPthresholdHighRxOIP,
       "eccmPPthresholdHighestRxOIP": eccmPPthresholdHighestRxOIP,
       "eccmPPhysteresisRxOIP": eccmPPhysteresisRxOIP,
       "apsPPthresholdTable": apsPPthresholdTable,
       "apsPPthresholdEntry": apsPPthresholdEntry,
       "apsPPthresholdLowestOipOsc": apsPPthresholdLowestOipOsc,
       "apsPPthresholdLowOipOsc": apsPPthresholdLowOipOsc,
       "apsPPthresholdHighOipOsc": apsPPthresholdHighOipOsc,
       "apsPPthresholdHighestOipOsc": apsPPthresholdHighestOipOsc,
       "apsPPhysteresisOipOsc": apsPPhysteresisOipOsc,
       "generalPerformanceAdmin": generalPerformanceAdmin,
       "alarmAdminTable": alarmAdminTable,
       "alarmAdminEntry": alarmAdminEntry,
       "alarmAdminType": alarmAdminType,
       "alarmAdminTypeDetails": alarmAdminTypeDetails,
       "alarmAdminTypeThreshold": alarmAdminTypeThreshold,
       "alarmAdminTypePeriod": alarmAdminTypePeriod,
       "modulePerformanceStatusTable": modulePerformanceStatusTable,
       "modulePerformanceStatusEntry": modulePerformanceStatusEntry,
       "modulePerformanceStatusType": modulePerformanceStatusType,
       "modulePerformanceStatusState": modulePerformanceStatusState,
       "interfacePerformanceStatusTable": interfacePerformanceStatusTable,
       "interfacePerformanceStatusEntry": interfacePerformanceStatusEntry,
       "interfacePerformanceStatusType": interfacePerformanceStatusType,
       "interfacePerformanceStatusState": interfacePerformanceStatusState,
       "performanceMonitoring": performanceMonitoring,
       "sonetPerformanceMon": sonetPerformanceMon,
       "sonetSectionPerformanceMon": sonetSectionPerformanceMon,
       "sonetSectionCurrent15minTable": sonetSectionCurrent15minTable,
       "sonetSectionCurrent15minEntry": sonetSectionCurrent15minEntry,
       "sonetSectionCurrent15minStatus": sonetSectionCurrent15minStatus,
       "sonetSectionCurrent15minESs": sonetSectionCurrent15minESs,
       "sonetSectionCurrent15minSESs": sonetSectionCurrent15minSESs,
       "sonetSectionCurrent15minSEFSs": sonetSectionCurrent15minSEFSs,
       "sonetSectionCurrent15minCVs": sonetSectionCurrent15minCVs,
       "sonetSectionCurrent15minTimeElapsed": sonetSectionCurrent15minTimeElapsed,
       "sonetSectionCurrent24hTable": sonetSectionCurrent24hTable,
       "sonetSectionCurrent24hEntry": sonetSectionCurrent24hEntry,
       "sonetSectionCurrent24hStatus": sonetSectionCurrent24hStatus,
       "sonetSectionCurrent24hESs": sonetSectionCurrent24hESs,
       "sonetSectionCurrent24hSESs": sonetSectionCurrent24hSESs,
       "sonetSectionCurrent24hSEFSs": sonetSectionCurrent24hSEFSs,
       "sonetSectionCurrent24hCVs": sonetSectionCurrent24hCVs,
       "sonetSectionCurrent24hTimeElapsed": sonetSectionCurrent24hTimeElapsed,
       "sonetSection15minIntervalTable": sonetSection15minIntervalTable,
       "sonetSection15minIntervalEntry": sonetSection15minIntervalEntry,
       "sonetSection15minIntervalNumber": sonetSection15minIntervalNumber,
       "sonetSection15minIntervalESs": sonetSection15minIntervalESs,
       "sonetSection15minIntervalSESs": sonetSection15minIntervalSESs,
       "sonetSection15minIntervalSEFs": sonetSection15minIntervalSEFs,
       "sonetSection15minIntervalCVs": sonetSection15minIntervalCVs,
       "sonetSection15minIntervalValidData": sonetSection15minIntervalValidData,
       "sonetSection15minIntervalTimeStamp": sonetSection15minIntervalTimeStamp,
       "sonetSection24hIntervalTable": sonetSection24hIntervalTable,
       "sonetSection24hIntervalEntry": sonetSection24hIntervalEntry,
       "sonetSection24hIntervalNumber": sonetSection24hIntervalNumber,
       "sonetSection24hIntervalESs": sonetSection24hIntervalESs,
       "sonetSection24hIntervalSESs": sonetSection24hIntervalSESs,
       "sonetSection24hIntervalSEFs": sonetSection24hIntervalSEFs,
       "sonetSection24hIntervalCVs": sonetSection24hIntervalCVs,
       "sonetSection24hIntervalValidData": sonetSection24hIntervalValidData,
       "sonetSection24hIntervalTimeStamp": sonetSection24hIntervalTimeStamp,
       "sonetPathPerformanceMon": sonetPathPerformanceMon,
       "sonetPathCurrent15minTable": sonetPathCurrent15minTable,
       "sonetPathCurrent15minEntry": sonetPathCurrent15minEntry,
       "sonetPathCurrent15minWidth": sonetPathCurrent15minWidth,
       "sonetPathCurrent15minStatus": sonetPathCurrent15minStatus,
       "sonetPathCurrent15minESs": sonetPathCurrent15minESs,
       "sonetPathCurrent15minSESs": sonetPathCurrent15minSESs,
       "sonetPathCurrent15minCVs": sonetPathCurrent15minCVs,
       "sonetPathCurrent15minUASs": sonetPathCurrent15minUASs,
       "sonetPathCurrent15minTimeElapsed": sonetPathCurrent15minTimeElapsed,
       "sonetPathCurrent24hTable": sonetPathCurrent24hTable,
       "sonetPathCurrent24hEntry": sonetPathCurrent24hEntry,
       "sonetPathCurrent24hWidth": sonetPathCurrent24hWidth,
       "sonetPathCurrent24hStatus": sonetPathCurrent24hStatus,
       "sonetPathCurrent24hESs": sonetPathCurrent24hESs,
       "sonetPathCurrent24hSESs": sonetPathCurrent24hSESs,
       "sonetPathCurrent24hCVs": sonetPathCurrent24hCVs,
       "sonetPathCurrent24hUASs": sonetPathCurrent24hUASs,
       "sonetPathCurrent24hTimeElapsed": sonetPathCurrent24hTimeElapsed,
       "sonetPath15minIntervalTable": sonetPath15minIntervalTable,
       "sonetPath15minIntervalEntry": sonetPath15minIntervalEntry,
       "sonetPath15minIntervalNumber": sonetPath15minIntervalNumber,
       "sonetPath15minIntervalESs": sonetPath15minIntervalESs,
       "sonetPath15minIntervalSESs": sonetPath15minIntervalSESs,
       "sonetPath15minIntervalCVs": sonetPath15minIntervalCVs,
       "sonetPath15minIntervalUASs": sonetPath15minIntervalUASs,
       "sonetPath15minIntervalValidData": sonetPath15minIntervalValidData,
       "sonetPath15minIntervalTimeStamp": sonetPath15minIntervalTimeStamp,
       "sonetPath24hIntervalTable": sonetPath24hIntervalTable,
       "sonetPath24hIntervalEntry": sonetPath24hIntervalEntry,
       "sonetPath24hIntervalNumber": sonetPath24hIntervalNumber,
       "sonetPath24hIntervalESs": sonetPath24hIntervalESs,
       "sonetPath24hIntervalSESs": sonetPath24hIntervalSESs,
       "sonetPath24hIntervalCVs": sonetPath24hIntervalCVs,
       "sonetPath24hIntervalUASs": sonetPath24hIntervalUASs,
       "sonetPath24hIntervalValidData": sonetPath24hIntervalValidData,
       "sonetPath24hIntervalTimeStamp": sonetPath24hIntervalTimeStamp,
       "physicalLayerPerformanceMon": physicalLayerPerformanceMon,
       "remOptSwPLP15minIntTable": remOptSwPLP15minIntTable,
       "remOptSwPLP15minIntEntry": remOptSwPLP15minIntEntry,
       "remOptSwPLP15minIntNumber": remOptSwPLP15minIntNumber,
       "remOptSwPLP15minIntAverageTxBias": remOptSwPLP15minIntAverageTxBias,
       "remOptSwPLP15minIntMinTxBias": remOptSwPLP15minIntMinTxBias,
       "remOptSwPLP15minIntMaxTxBias": remOptSwPLP15minIntMaxTxBias,
       "remOptSwPLP15minIntValidData": remOptSwPLP15minIntValidData,
       "remOptSwPLP15minIntTimeStamp": remOptSwPLP15minIntTimeStamp,
       "remOptSwPLP24hIntTable": remOptSwPLP24hIntTable,
       "remOptSwPLP24hIntEntry": remOptSwPLP24hIntEntry,
       "remOptSwPLP24hIntNumber": remOptSwPLP24hIntNumber,
       "remOptSwPLP24hIntAverageTxBias": remOptSwPLP24hIntAverageTxBias,
       "remOptSwPLP24hIntMinTxBias": remOptSwPLP24hIntMinTxBias,
       "remOptSwPLP24hIntMaxTxBias": remOptSwPLP24hIntMaxTxBias,
       "remOptSwPLP24hIntValidData": remOptSwPLP24hIntValidData,
       "remOptSwPLP24hIntTimeStamp": remOptSwPLP24hIntTimeStamp,
       "edfaPLP15minIntTable": edfaPLP15minIntTable,
       "edfaPLP15minIntEntry": edfaPLP15minIntEntry,
       "edfaPLP15minIntNumber": edfaPLP15minIntNumber,
       "edfaPLP15minIntAveragePumpPower": edfaPLP15minIntAveragePumpPower,
       "edfaPLP15minIntMinPumpPower": edfaPLP15minIntMinPumpPower,
       "edfaPLP15minIntMaxPumpPower": edfaPLP15minIntMaxPumpPower,
       "edfaPLP15minIntAveragePumpCurrent": edfaPLP15minIntAveragePumpCurrent,
       "edfaPLP15minIntMinPumpCurrent": edfaPLP15minIntMinPumpCurrent,
       "edfaPLP15minIntMaxPumpCurrent": edfaPLP15minIntMaxPumpCurrent,
       "edfaPLP15minIntAverageTECCurrent": edfaPLP15minIntAverageTECCurrent,
       "edfaPLP15minIntMinTECCurrent": edfaPLP15minIntMinTECCurrent,
       "edfaPLP15minIntMaxTECCurrent": edfaPLP15minIntMaxTECCurrent,
       "edfaPLP15minIntAveragePumpTxTemp": edfaPLP15minIntAveragePumpTxTemp,
       "edfaPLP15minIntMinPumpTxTemp": edfaPLP15minIntMinPumpTxTemp,
       "edfaPLP15minIntMaxPumpTxTemp": edfaPLP15minIntMaxPumpTxTemp,
       "edfaPLP15minIntAverageSubModuleTemp": edfaPLP15minIntAverageSubModuleTemp,
       "edfaPLP15minIntMinSubModuleTemp": edfaPLP15minIntMinSubModuleTemp,
       "edfaPLP15minIntMaxSubModuleTemp": edfaPLP15minIntMaxSubModuleTemp,
       "edfaPLP15minIntAverageOIP": edfaPLP15minIntAverageOIP,
       "edfaPLP15minIntMinOIP": edfaPLP15minIntMinOIP,
       "edfaPLP15minIntMaxOIP": edfaPLP15minIntMaxOIP,
       "edfaPLP15minIntAverageOOP": edfaPLP15minIntAverageOOP,
       "edfaPLP15minIntMinOOP": edfaPLP15minIntMinOOP,
       "edfaPLP15minIntMaxOOP": edfaPLP15minIntMaxOOP,
       "edfaPLP15minIntValidData": edfaPLP15minIntValidData,
       "edfaPLP15minIntTimeStamp": edfaPLP15minIntTimeStamp,
       "edfaPLP24hIntTable": edfaPLP24hIntTable,
       "edfaPLP24hIntEntry": edfaPLP24hIntEntry,
       "edfaPLP24hIntNumber": edfaPLP24hIntNumber,
       "edfaPLP24hIntAveragePumpPower": edfaPLP24hIntAveragePumpPower,
       "edfaPLP24hIntMinPumpPower": edfaPLP24hIntMinPumpPower,
       "edfaPLP24hIntMaxPumpPower": edfaPLP24hIntMaxPumpPower,
       "edfaPLP24hIntAveragePumpCurrent": edfaPLP24hIntAveragePumpCurrent,
       "edfaPLP24hIntMinPumpCurrent": edfaPLP24hIntMinPumpCurrent,
       "edfaPLP24hIntMaxPumpCurrent": edfaPLP24hIntMaxPumpCurrent,
       "edfaPLP24hIntAverageTECCurrent": edfaPLP24hIntAverageTECCurrent,
       "edfaPLP24hIntMinTECCurrent": edfaPLP24hIntMinTECCurrent,
       "edfaPLP24hIntMaxTECCurrent": edfaPLP24hIntMaxTECCurrent,
       "edfaPLP24hIntAveragePumpTxTemp": edfaPLP24hIntAveragePumpTxTemp,
       "edfaPLP24hIntMinPumpTxTemp": edfaPLP24hIntMinPumpTxTemp,
       "edfaPLP24hIntMaxPumpTxTemp": edfaPLP24hIntMaxPumpTxTemp,
       "edfaPLP24hIntAverageSubModuleTemp": edfaPLP24hIntAverageSubModuleTemp,
       "edfaPLP24hIntMinSubModuleTemp": edfaPLP24hIntMinSubModuleTemp,
       "edfaPLP24hIntMaxSubModuleTemp": edfaPLP24hIntMaxSubModuleTemp,
       "edfaPLP24hIntAverageOIP": edfaPLP24hIntAverageOIP,
       "edfaPLP24hIntMinOIP": edfaPLP24hIntMinOIP,
       "edfaPLP24hIntMaxOIP": edfaPLP24hIntMaxOIP,
       "edfaPLP24hIntAverageOOP": edfaPLP24hIntAverageOOP,
       "edfaPLP24hIntMinOOP": edfaPLP24hIntMinOOP,
       "edfaPLP24hIntMaxOOP": edfaPLP24hIntMaxOOP,
       "edfaPLP24hIntValidData": edfaPLP24hIntValidData,
       "edfaPLP24hIntTimeStamp": edfaPLP24hIntTimeStamp,
       "interfaceTTPLP15minIntTable": interfaceTTPLP15minIntTable,
       "interfaceTTPLP15minIntEntry": interfaceTTPLP15minIntEntry,
       "interfaceTTPLP15minIntNumber": interfaceTTPLP15minIntNumber,
       "interfaceTTPLP15minIntAverageTxBias": interfaceTTPLP15minIntAverageTxBias,
       "interfaceTTPLP15minIntMinTxBias": interfaceTTPLP15minIntMinTxBias,
       "interfaceTTPLP15minIntMaxTxBias": interfaceTTPLP15minIntMaxTxBias,
       "interfaceTTPLP15minIntAverageTxLaserTemp": interfaceTTPLP15minIntAverageTxLaserTemp,
       "interfaceTTPLP15minIntMinTxLaserTemp": interfaceTTPLP15minIntMinTxLaserTemp,
       "interfaceTTPLP15minIntMaxTxLaserTemp": interfaceTTPLP15minIntMaxTxLaserTemp,
       "interfaceTTPLP15minIntAverageRxOIP": interfaceTTPLP15minIntAverageRxOIP,
       "interfaceTTPLP15minIntMinRxOIP": interfaceTTPLP15minIntMinRxOIP,
       "interfaceTTPLP15minIntMaxRxOIP": interfaceTTPLP15minIntMaxRxOIP,
       "interfaceTTPLP15minIntAverageRxUAPD": interfaceTTPLP15minIntAverageRxUAPD,
       "interfaceTTPLP15minIntMinRxUAPD": interfaceTTPLP15minIntMinRxUAPD,
       "interfaceTTPLP15minIntMaxRxUAPD": interfaceTTPLP15minIntMaxRxUAPD,
       "interfaceTTPLP15minIntValidData": interfaceTTPLP15minIntValidData,
       "interfaceTTPLP15minIntTimeStamp": interfaceTTPLP15minIntTimeStamp,
       "interfaceTTPLP24hIntTable": interfaceTTPLP24hIntTable,
       "interfaceTTPLP24hIntEntry": interfaceTTPLP24hIntEntry,
       "interfaceTTPLP24hIntNumber": interfaceTTPLP24hIntNumber,
       "interfaceTTPLP24hIntAverageTxBias": interfaceTTPLP24hIntAverageTxBias,
       "interfaceTTPLP24hIntMinTxBias": interfaceTTPLP24hIntMinTxBias,
       "interfaceTTPLP24hIntMaxTxBias": interfaceTTPLP24hIntMaxTxBias,
       "interfaceTTPLP24hIntAverageTxLaserTemp": interfaceTTPLP24hIntAverageTxLaserTemp,
       "interfaceTTPLP24hIntMinTxLaserTemp": interfaceTTPLP24hIntMinTxLaserTemp,
       "interfaceTTPLP24hIntMaxTxLaserTemp": interfaceTTPLP24hIntMaxTxLaserTemp,
       "interfaceTTPLP24hIntAverageRxOIP": interfaceTTPLP24hIntAverageRxOIP,
       "interfaceTTPLP24hIntMinRxOIP": interfaceTTPLP24hIntMinRxOIP,
       "interfaceTTPLP24hIntMaxRxOIP": interfaceTTPLP24hIntMaxRxOIP,
       "interfaceTTPLP24hIntAverageRxUAPD": interfaceTTPLP24hIntAverageRxUAPD,
       "interfaceTTPLP24hIntMinRxUAPD": interfaceTTPLP24hIntMinRxUAPD,
       "interfaceTTPLP24hIntMaxRxUAPD": interfaceTTPLP24hIntMaxRxUAPD,
       "interfaceTTPLP24hIntValidData": interfaceTTPLP24hIntValidData,
       "interfaceTTPLP24hIntTimeStamp": interfaceTTPLP24hIntTimeStamp,
       "eccmPLP15minIntTable": eccmPLP15minIntTable,
       "eccmPLP15minIntEntry": eccmPLP15minIntEntry,
       "eccmPLP15minIntNumber": eccmPLP15minIntNumber,
       "eccmPLP15minIntAverageRxOIP": eccmPLP15minIntAverageRxOIP,
       "eccmPLP15minIntMinRxOIP": eccmPLP15minIntMinRxOIP,
       "eccmPLP15minIntMaxRxOIP": eccmPLP15minIntMaxRxOIP,
       "eccmPLP15minIntValidData": eccmPLP15minIntValidData,
       "eccmPLP15minIntTimeStamp": eccmPLP15minIntTimeStamp,
       "eccmPLP24hIntTable": eccmPLP24hIntTable,
       "eccmPLP24hIntEntry": eccmPLP24hIntEntry,
       "eccmPLP24hIntNumber": eccmPLP24hIntNumber,
       "eccmPLP24hIntAverageRxOIP": eccmPLP24hIntAverageRxOIP,
       "eccmPLP24hIntMinRxOIP": eccmPLP24hIntMinRxOIP,
       "eccmPLP24hIntMaxRxOIP": eccmPLP24hIntMaxRxOIP,
       "eccmPLP24hIntValidData": eccmPLP24hIntValidData,
       "eccmPLP24hIntTimeStamp": eccmPLP24hIntTimeStamp,
       "apsPLP15minIntTable": apsPLP15minIntTable,
       "apsPLP15minIntEntry": apsPLP15minIntEntry,
       "apsPLP15minIntNumber": apsPLP15minIntNumber,
       "apsPLP15minIntAverageOIPLoad": apsPLP15minIntAverageOIPLoad,
       "apsPLP15minIntMinOIPLoad": apsPLP15minIntMinOIPLoad,
       "apsPLP15minIntMaxOIPLoad": apsPLP15minIntMaxOIPLoad,
       "apsPLP15minIntAverageOipOsc": apsPLP15minIntAverageOipOsc,
       "apsPLP15minIntMinOipOsc": apsPLP15minIntMinOipOsc,
       "apsPLP15minIntMaxOipOsc": apsPLP15minIntMaxOipOsc,
       "apsPLP15minIntValidData": apsPLP15minIntValidData,
       "apsPLP15minIntTimeStamp": apsPLP15minIntTimeStamp,
       "apsPLP24hIntTable": apsPLP24hIntTable,
       "apsPLP24hIntEntry": apsPLP24hIntEntry,
       "apsPLP24hIntNumber": apsPLP24hIntNumber,
       "apsPLP24hIntAverageOIPLoad": apsPLP24hIntAverageOIPLoad,
       "apsPLP24hIntMinOIPLoad": apsPLP24hIntMinOIPLoad,
       "apsPLP24hIntMaxOIPLoad": apsPLP24hIntMaxOIPLoad,
       "apsPLP24hIntAverageOipOsc": apsPLP24hIntAverageOipOsc,
       "apsPLP24hIntMinOipOsc": apsPLP24hIntMinOipOsc,
       "apsPLP24hIntMaxOipOsc": apsPLP24hIntMaxOipOsc,
       "apsPLP24hIntValidData": apsPLP24hIntValidData,
       "apsPLP24hIntTimeStamp": apsPLP24hIntTimeStamp,
       "physicalLayerAlarmMon": physicalLayerAlarmMon,
       "remOptSwPLA15minIntTable": remOptSwPLA15minIntTable,
       "remOptSwPLA15minIntEntry": remOptSwPLA15minIntEntry,
       "remOptSwPLA15minIntNumber": remOptSwPLA15minIntNumber,
       "remOptSwPLA15minIntLineARxLOS": remOptSwPLA15minIntLineARxLOS,
       "remOptSwPLA15minIntLineBRxLOS": remOptSwPLA15minIntLineBRxLOS,
       "remOptSwPLA15minIntValidData": remOptSwPLA15minIntValidData,
       "remOptSwPLA15minIntTimeStamp": remOptSwPLA15minIntTimeStamp,
       "remOptSwPLA24hIntTable": remOptSwPLA24hIntTable,
       "remOptSwPLA24hIntEntry": remOptSwPLA24hIntEntry,
       "remOptSwPLA24hIntNumber": remOptSwPLA24hIntNumber,
       "remOptSwPLA24hIntLineARxLOS": remOptSwPLA24hIntLineARxLOS,
       "remOptSwPLA24hIntLineBRxLOS": remOptSwPLA24hIntLineBRxLOS,
       "remOptSwPLA24hIntValidData": remOptSwPLA24hIntValidData,
       "remOptSwPLA24hIntTimeStamp": remOptSwPLA24hIntTimeStamp,
       "edfaPLA15minIntTable": edfaPLA15minIntTable,
       "edfaPLA15minIntEntry": edfaPLA15minIntEntry,
       "edfaPLA15minIntNumber": edfaPLA15minIntNumber,
       "edfaPLA15minIntLossOfOIP": edfaPLA15minIntLossOfOIP,
       "edfaPLA15minIntHwOIPTooHigh": edfaPLA15minIntHwOIPTooHigh,
       "edfaPLA15minIntValidData": edfaPLA15minIntValidData,
       "edfaPLA15minIntTimeStamp": edfaPLA15minIntTimeStamp,
       "edfaPLA24hIntTable": edfaPLA24hIntTable,
       "edfaPLA24hIntEntry": edfaPLA24hIntEntry,
       "edfaPLA24hIntNumber": edfaPLA24hIntNumber,
       "edfaPLA24hIntLossOfOIP": edfaPLA24hIntLossOfOIP,
       "edfaPLA24hIntHwOIPTooHigh": edfaPLA24hIntHwOIPTooHigh,
       "edfaPLA24hIntValidData": edfaPLA24hIntValidData,
       "edfaPLA24hIntTimeStamp": edfaPLA24hIntTimeStamp,
       "interfaceTTPLA15minIntTable": interfaceTTPLA15minIntTable,
       "interfaceTTPLA15minIntEntry": interfaceTTPLA15minIntEntry,
       "interfaceTTPLA15minIntNumber": interfaceTTPLA15minIntNumber,
       "interfaceTTPLA15minIntRxLOS": interfaceTTPLA15minIntRxLOS,
       "interfaceTTPLA15minIntRxLoLP": interfaceTTPLA15minIntRxLoLP,
       "interfaceTTPLA15minIntRxLossOfClk": interfaceTTPLA15minIntRxLossOfClk,
       "interfaceTTPLA15minIntRxLOF": interfaceTTPLA15minIntRxLOF,
       "interfaceTTPLA15minIntRxSignalOverload": interfaceTTPLA15minIntRxSignalOverload,
       "interfaceTTPLA15minIntValidData": interfaceTTPLA15minIntValidData,
       "interfaceTTPLA15minIntTimeStamp": interfaceTTPLA15minIntTimeStamp,
       "interfaceTTPLA24hIntTable": interfaceTTPLA24hIntTable,
       "interfaceTTPLA24hIntEntry": interfaceTTPLA24hIntEntry,
       "interfaceTTPLA24hIntNumber": interfaceTTPLA24hIntNumber,
       "interfaceTTPLA24hIntRxLOS": interfaceTTPLA24hIntRxLOS,
       "interfaceTTPLA24hIntRxLoLP": interfaceTTPLA24hIntRxLoLP,
       "interfaceTTPLA24hIntRxLossOfClk": interfaceTTPLA24hIntRxLossOfClk,
       "interfaceTTPLA24hIntRxLOF": interfaceTTPLA24hIntRxLOF,
       "interfaceTTPLA24hIntRxSignalOverload": interfaceTTPLA24hIntRxSignalOverload,
       "interfaceTTPLA24hIntValidData": interfaceTTPLA24hIntValidData,
       "interfaceTTPLA24hIntTimeStamp": interfaceTTPLA24hIntTimeStamp,
       "eccmPLA15minIntTable": eccmPLA15minIntTable,
       "eccmPLA15minIntEntry": eccmPLA15minIntEntry,
       "eccmPLA15minIntNumber": eccmPLA15minIntNumber,
       "eccmPLA15minIntRxLOS": eccmPLA15minIntRxLOS,
       "eccmPLA15minIntValidData": eccmPLA15minIntValidData,
       "eccmPLA15minIntTimeStamp": eccmPLA15minIntTimeStamp,
       "eccmPLA24hIntTable": eccmPLA24hIntTable,
       "eccmPLA24hIntEntry": eccmPLA24hIntEntry,
       "eccmPLA24hIntNumber": eccmPLA24hIntNumber,
       "eccmPLA24hIntRxLOS": eccmPLA24hIntRxLOS,
       "eccmPLA24hIntValidData": eccmPLA24hIntValidData,
       "eccmPLA24hIntTimeStamp": eccmPLA24hIntTimeStamp,
       "apsPLA15minIntTable": apsPLA15minIntTable,
       "apsPLA15minIntEntry": apsPLA15minIntEntry,
       "apsPLA15minIntNumber": apsPLA15minIntNumber,
       "apsPLA15minIntLossOfOIP": apsPLA15minIntLossOfOIP,
       "apsPLA15minIntValidData": apsPLA15minIntValidData,
       "apsPLA15minIntTimeStamp": apsPLA15minIntTimeStamp,
       "apsPLA24hIntTable": apsPLA24hIntTable,
       "apsPLA24hIntEntry": apsPLA24hIntEntry,
       "apsPLA24hIntNumber": apsPLA24hIntNumber,
       "apsPLA24hIntLossOfOIP": apsPLA24hIntLossOfOIP,
       "apsPLA24hIntValidData": apsPLA24hIntValidData,
       "apsPLA24hIntTimeStamp": apsPLA24hIntTimeStamp,
       "codingStatsPerformanceMon": codingStatsPerformanceMon,
       "codingStatsCurrent15minTable": codingStatsCurrent15minTable,
       "codingStatsCurrent15minEntry": codingStatsCurrent15minEntry,
       "codingStatsCurrent15minStatus": codingStatsCurrent15minStatus,
       "codingStatsCurrent15minESs": codingStatsCurrent15minESs,
       "codingStatsCurrent15minCVs": codingStatsCurrent15minCVs,
       "codingStatsCurrent15minDEs": codingStatsCurrent15minDEs,
       "codingStatsCurrent15minTimeElapsed": codingStatsCurrent15minTimeElapsed,
       "codingStatsCurrent24hTable": codingStatsCurrent24hTable,
       "codingStatsCurrent24hEntry": codingStatsCurrent24hEntry,
       "codingStatsCurrent24hStatus": codingStatsCurrent24hStatus,
       "codingStatsCurrent24hESs": codingStatsCurrent24hESs,
       "codingStatsCurrent24hCVs": codingStatsCurrent24hCVs,
       "codingStatsCurrent24hDEs": codingStatsCurrent24hDEs,
       "codingStatsCurrent24hTimeElapsed": codingStatsCurrent24hTimeElapsed,
       "codingStats15minIntervalTable": codingStats15minIntervalTable,
       "codingStats15minIntervalEntry": codingStats15minIntervalEntry,
       "codingStats15minIntervalNumber": codingStats15minIntervalNumber,
       "codingStats15minIntervalESs": codingStats15minIntervalESs,
       "codingStats15minIntervalCVs": codingStats15minIntervalCVs,
       "codingStats15minIntervalDEs": codingStats15minIntervalDEs,
       "codingStats15minIntervalValidData": codingStats15minIntervalValidData,
       "codingStats15minIntervalTimeStamp": codingStats15minIntervalTimeStamp,
       "codingStats24hIntervalTable": codingStats24hIntervalTable,
       "codingStats24hIntervalEntry": codingStats24hIntervalEntry,
       "codingStats24hIntervalNumber": codingStats24hIntervalNumber,
       "codingStats24hIntervalESs": codingStats24hIntervalESs,
       "codingStats24hIntervalCVs": codingStats24hIntervalCVs,
       "codingStats24hIntervalDEs": codingStats24hIntervalDEs,
       "codingStats24hIntervalValidData": codingStats24hIntervalValidData,
       "codingStats24hIntervalTimeStamp": codingStats24hIntervalTimeStamp,
       "otuFecPerformanceMon": otuFecPerformanceMon,
       "otuFecCurrent15minTable": otuFecCurrent15minTable,
       "otuFecCurrent15minEntry": otuFecCurrent15minEntry,
       "otuFecCurrent15minESs": otuFecCurrent15minESs,
       "otuFecCurrent15minSEFSs": otuFecCurrent15minSEFSs,
       "otuFecCurrent15minCVs": otuFecCurrent15minCVs,
       "otuFecCurrent15minUBEs": otuFecCurrent15minUBEs,
       "otuFecCurrent15minTimeElapsed": otuFecCurrent15minTimeElapsed,
       "otuFecCurrent24hTable": otuFecCurrent24hTable,
       "otuFecCurrent24hEntry": otuFecCurrent24hEntry,
       "otuFecCurrent24hESs": otuFecCurrent24hESs,
       "otuFecCurrent24hSEFSs": otuFecCurrent24hSEFSs,
       "otuFecCurrent24hCVs": otuFecCurrent24hCVs,
       "otuFecCurrent24hUBEs": otuFecCurrent24hUBEs,
       "otuFecCurrent24hTimeElapsed": otuFecCurrent24hTimeElapsed,
       "otuFec15minIntervalTable": otuFec15minIntervalTable,
       "otuFec15minIntervalEntry": otuFec15minIntervalEntry,
       "otuFec15minIntervalNumber": otuFec15minIntervalNumber,
       "otuFec15minIntervalESs": otuFec15minIntervalESs,
       "otuFec15minIntervalSEFSs": otuFec15minIntervalSEFSs,
       "otuFec15minIntervalCVs": otuFec15minIntervalCVs,
       "otuFec15minIntervalUBEs": otuFec15minIntervalUBEs,
       "otuFec15minIntervalValidData": otuFec15minIntervalValidData,
       "otuFec15minIntervalTimeStamp": otuFec15minIntervalTimeStamp,
       "otuFec24hIntervalTable": otuFec24hIntervalTable,
       "otuFec24hIntervalEntry": otuFec24hIntervalEntry,
       "otuFec24hIntervalNumber": otuFec24hIntervalNumber,
       "otuFec24hIntervalESs": otuFec24hIntervalESs,
       "otuFec24hIntervalSEFSs": otuFec24hIntervalSEFSs,
       "otuFec24hIntervalCVs": otuFec24hIntervalCVs,
       "otuFec24hIntervalUBEs": otuFec24hIntervalUBEs,
       "otuFec24hIntervalValidData": otuFec24hIntervalValidData,
       "otuFec24hIntervalTimeStamp": otuFec24hIntervalTimeStamp}
)
