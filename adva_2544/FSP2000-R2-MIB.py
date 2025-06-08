# SNMP MIB module (FSP2000-R2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/FSP2000-R2-MIB.mib
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

(fsp2000,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp2000")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsp2000MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2)
)
if mibBuilder.loadTexts:
    fsp2000MIB.setRevisions(
        ("2005-01-24 00:00",
         "2004-09-24 00:00",
         "2004-09-16 00:00",
         "2004-08-09 00:00",
         "2004-05-31 00:00",
         "2004-03-31 00:00",
         "2003-12-05 00:00",
         "2003-02-20 10:26",
         "2002-11-26 10:26",
         "2002-09-16 15:30",
         "2002-07-23 15:30",
         "2002-07-08 15:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IndexTranslation(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
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



class InterfaceAlarmTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              8,
              9,
              10,
              11,
              12,
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
              40)
        )
    )
    namedValues = NamedValues(
        *(("lossOfSignal", 1),
          ("lossOfLinkPulse", 2),
          ("lossOfSync", 3),
          ("partitioned", 5),
          ("laserTecEoL", 7),
          ("ifModuleTempOoR", 8),
          ("laserTempOoR", 9),
          ("lossOfOop", 10),
          ("oipTooHigh", 11),
          ("oopTooLow", 12),
          ("lossOfSignalT", 15),
          ("telemetryInput1", 16),
          ("telemetryInput2", 17),
          ("telemetryInput3", 18),
          ("attAtRTooHigh", 19),
          ("attAtRTooLow", 20),
          ("attAtTTooHigh", 21),
          ("attAtTTooLow", 22),
          ("intrusionAtR", 23),
          ("intrusionAtT", 24),
          ("oipTooLow", 25),
          ("oopTooHigh", 26),
          ("laserCurrentTooLow", 27),
          ("laserCurrentTooHigh", 28),
          ("attRxMonitoringLow", 30),
          ("attRxMonitoringHigh", 31),
          ("attTxMonitoringLow", 32),
          ("attTxMonitoringHigh", 33),
          ("laserFailure", 34),
          ("pumpLaserFailure", 35),
          ("receiverFailure", 36),
          ("oopOoR", 37),
          ("tempSafetyShutdown", 38),
          ("laserTempTooLow", 39),
          ("laserTempTooHigh", 40))
    )



class EquipmentAlarmTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
        *(("fanFail", 1),
          ("fanPowerFail", 2),
          ("powerFail", 3),
          ("tempTooHigh", 6),
          ("tempTooLow", 7),
          ("voltageTooHigh", 8),
          ("voltageTooLow", 9),
          ("eqNotAccepted", 10),
          ("eqMismatch", 11),
          ("eqNotApproved", 12))
    )



class TrapAlarmSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("warning", 5),
          ("cleared", 6))
    )



class TrapCounter(TextualConvention, Counter32):
    status = "current"


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



class SwitchAdminState(TextualConvention, Integer32):
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
        *(("lockToA", 1),
          ("lockToB", 2),
          ("unlockSwitch", 3))
    )



class SwitchOperState(TextualConvention, Integer32):
    status = "current"
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
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("containerEmpty", 1),
          ("containsAcceptedUnit", 2),
          ("containsNotAcceptedUnit", 3),
          ("containsUnknownUnit", 4))
    )



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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mb125", 2),
          ("mb155", 3),
          ("mb200", 4),
          ("mb270", 6),
          ("mb622", 7),
          ("mb1062", 8),
          ("mb1250", 10),
          ("mb2125", 11),
          ("mb2488", 12),
          ("mb2500", 13),
          ("mb9953", 14),
          ("mb10312", 15),
          ("mb1062cl", 16),
          ("mb155als2", 18),
          ("mb622als2", 19),
          ("mb2488als2", 20),
          ("adaptive3R", 21),
          ("adaptive3ROddRates", 22),
          ("mb10518", 23),
          ("mb10709", 24),
          ("mb11095", 25),
          ("mb9953als2", 26),
          ("mb11317", 27))
    )



class ClockDataRateBitfield(TextualConvention, Integer32):
    status = "current"


class LaserTxConfig(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOn", 3),
          ("laserAuto", 6))
    )



class LaserTxStatus(TextualConvention, Integer32):
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
        *(("on", 1),
          ("off", 2),
          ("standby", 3),
          ("unknown", 4))
    )



class ModuleType(TextualConvention, Integer32):
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
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("nemiv2", 2),
          ("demiv2", 3),
          ("wcm", 4),
          ("hstwcm", 5),
          ("tcm2", 6),
          ("tcm4", 7),
          ("tcm8", 8),
          ("rsmosc", 9),
          ("oscm", 10),
          ("rsm", 11),
          ("rsmsf", 12),
          ("rsmoscolm", 13),
          ("rsmoscolmsf", 14),
          ("rsmolm", 15),
          ("rsmolmsf", 16),
          ("edfa", 17),
          ("hub", 18),
          ("mdxm", 19),
          ("mdxmsf", 20),
          ("cmdxm", 21),
          ("bsm", 22),
          ("bsmsf", 23),
          ("oscsm", 24),
          ("nemiv1", 25),
          ("demiv1", 26),
          ("sfp", 27),
          ("tcm2pl", 28),
          ("wcmpl", 29),
          ("ilm", 30),
          ("ilmsf", 31),
          ("oscmolm", 32),
          ("tcm2plr", 33),
          ("wcmplr", 34),
          ("wcmpl10G", 35),
          ("cscfm", 36),
          ("xfp", 37),
          ("edfagc", 38),
          ("clsm", 39),
          ("tcm4pl10G", 40),
          ("sfpcopper", 41))
    )



class NEState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("ucmUpdate", 2))
    )



class BandScheme(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("cwdmr2", 2),
          ("dwdmr2", 3),
          ("dwdmr2IL", 4))
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
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("downloading", 2),
          ("downloadLoginFailed", 3),
          ("downloadFileNotFound", 4),
          ("downloadFileNoAccess", 5),
          ("downloadFailure", 6),
          ("downloadedReadyForActivation", 7),
          ("activatingSoftware", 8),
          ("integrityCheckFailed", 9),
          ("softwareActivated", 10),
          ("rebooting", 11),
          ("rebootFailed", 12),
          ("updateLocked", 13))
    )



class AccessState(TextualConvention, Integer32):
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
        *(("noAccess", 1),
          ("limitedAccess", 2),
          ("fullAccess", 3))
    )



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



class TransmissionMode(TextualConvention, Integer32):
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
        *(("converter", 1),
          ("converterB", 2),
          ("regenerator", 3),
          ("hotStandby", 4),
          ("back2Back", 5))
    )



class TransmissionModeBitfield(TextualConvention, Integer32):
    status = "current"


class KBytes(TextualConvention, Gauge32):
    status = "current"


class OLMGradientThreshold(TextualConvention, Integer32):
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
        *(("use0point5dB", 1),
          ("use1dB", 2),
          ("use1point5dB", 3),
          ("use2dB", 4),
          ("use2point5dB", 5),
          ("use3dB", 6),
          ("notUsed", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Fsp2000Products_ObjectIdentity = ObjectIdentity
fsp2000Products = _Fsp2000Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 1)
)
_Fsp2000V1_ObjectIdentity = ObjectIdentity
fsp2000V1 = _Fsp2000V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    fsp2000V1.setStatus("current")
_AlarmMIB_ObjectIdentity = ObjectIdentity
alarmMIB = _AlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1)
)
_AlarmFilters_ObjectIdentity = ObjectIdentity
alarmFilters = _AlarmFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1)
)
_InterfaceAlarmReportControlTable_Object = MibTable
interfaceAlarmReportControlTable = _InterfaceAlarmReportControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceAlarmReportControlTable.setStatus("current")
_InterfaceAlarmReportControlEntry_Object = MibTableRow
interfaceAlarmReportControlEntry = _InterfaceAlarmReportControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 1, 1)
)
interfaceAlarmReportControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceAlarmReportControlEntry.setStatus("current")
_InterfaceAlarmReportControlState_Type = ArcState
_InterfaceAlarmReportControlState_Object = MibTableColumn
interfaceAlarmReportControlState = _InterfaceAlarmReportControlState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 1, 1, 1),
    _InterfaceAlarmReportControlState_Type()
)
interfaceAlarmReportControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceAlarmReportControlState.setStatus("current")
_EquipmentAlarmReportControlTable_Object = MibTable
equipmentAlarmReportControlTable = _EquipmentAlarmReportControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    equipmentAlarmReportControlTable.setStatus("current")
_EquipmentAlarmReportControlEntry_Object = MibTableRow
equipmentAlarmReportControlEntry = _EquipmentAlarmReportControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 2, 1)
)
equipmentAlarmReportControlEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    equipmentAlarmReportControlEntry.setStatus("current")
_EquipmentAlarmReportControlState_Type = ArcState
_EquipmentAlarmReportControlState_Object = MibTableColumn
equipmentAlarmReportControlState = _EquipmentAlarmReportControlState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 2, 1, 1),
    _EquipmentAlarmReportControlState_Type()
)
equipmentAlarmReportControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentAlarmReportControlState.setStatus("current")
_InterfaceAlarmSeverityTable_Object = MibTable
interfaceAlarmSeverityTable = _InterfaceAlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    interfaceAlarmSeverityTable.setStatus("current")
_InterfaceAlarmSeverityEntry_Object = MibTableRow
interfaceAlarmSeverityEntry = _InterfaceAlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 3, 1)
)
interfaceAlarmSeverityEntry.setIndexNames(
    (0, "FSP2000-R2-MIB", "interfaceAlarmSeverityType"),
)
if mibBuilder.loadTexts:
    interfaceAlarmSeverityEntry.setStatus("current")
_InterfaceAlarmSeverityType_Type = InterfaceAlarmTypes
_InterfaceAlarmSeverityType_Object = MibTableColumn
interfaceAlarmSeverityType = _InterfaceAlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 3, 1, 1),
    _InterfaceAlarmSeverityType_Type()
)
interfaceAlarmSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceAlarmSeverityType.setStatus("current")
_InterfaceAlarmSeverityValue_Type = TrapAlarmSeverity
_InterfaceAlarmSeverityValue_Object = MibTableColumn
interfaceAlarmSeverityValue = _InterfaceAlarmSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 3, 1, 2),
    _InterfaceAlarmSeverityValue_Type()
)
interfaceAlarmSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceAlarmSeverityValue.setStatus("current")
_EquipmentAlarmSeverityTable_Object = MibTable
equipmentAlarmSeverityTable = _EquipmentAlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    equipmentAlarmSeverityTable.setStatus("current")
_EquipmentAlarmSeverityEntry_Object = MibTableRow
equipmentAlarmSeverityEntry = _EquipmentAlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 4, 1)
)
equipmentAlarmSeverityEntry.setIndexNames(
    (0, "FSP2000-R2-MIB", "equipmentAlarmSeverityType"),
)
if mibBuilder.loadTexts:
    equipmentAlarmSeverityEntry.setStatus("current")
_EquipmentAlarmSeverityType_Type = EquipmentAlarmTypes
_EquipmentAlarmSeverityType_Object = MibTableColumn
equipmentAlarmSeverityType = _EquipmentAlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 4, 1, 1),
    _EquipmentAlarmSeverityType_Type()
)
equipmentAlarmSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentAlarmSeverityType.setStatus("current")
_EquipmentAlarmSeverityValue_Type = TrapAlarmSeverity
_EquipmentAlarmSeverityValue_Object = MibTableColumn
equipmentAlarmSeverityValue = _EquipmentAlarmSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 1, 4, 1, 2),
    _EquipmentAlarmSeverityValue_Type()
)
equipmentAlarmSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentAlarmSeverityValue.setStatus("current")
_CurrentAlarms_ObjectIdentity = ObjectIdentity
currentAlarms = _CurrentAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2)
)
_InterfaceCurrentAlarmTable_Object = MibTable
interfaceCurrentAlarmTable = _InterfaceCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceCurrentAlarmTable.setStatus("current")
_InterfaceCurrentAlarmEntry_Object = MibTableRow
interfaceCurrentAlarmEntry = _InterfaceCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2, 1, 1)
)
interfaceCurrentAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "interfaceCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    interfaceCurrentAlarmEntry.setStatus("current")
_InterfaceCurrentAlarmType_Type = InterfaceAlarmTypes
_InterfaceCurrentAlarmType_Object = MibTableColumn
interfaceCurrentAlarmType = _InterfaceCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2, 1, 1, 1),
    _InterfaceCurrentAlarmType_Type()
)
interfaceCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceCurrentAlarmType.setStatus("current")
_InterfaceCurrentAlarmSeverity_Type = TrapAlarmSeverity
_InterfaceCurrentAlarmSeverity_Object = MibTableColumn
interfaceCurrentAlarmSeverity = _InterfaceCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2, 1, 1, 2),
    _InterfaceCurrentAlarmSeverity_Type()
)
interfaceCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCurrentAlarmSeverity.setStatus("current")
_EquipmentCurrentAlarmTable_Object = MibTable
equipmentCurrentAlarmTable = _EquipmentCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    equipmentCurrentAlarmTable.setStatus("current")
_EquipmentCurrentAlarmEntry_Object = MibTableRow
equipmentCurrentAlarmEntry = _EquipmentCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2, 2, 1)
)
equipmentCurrentAlarmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "equipmentCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    equipmentCurrentAlarmEntry.setStatus("current")
_EquipmentCurrentAlarmType_Type = EquipmentAlarmTypes
_EquipmentCurrentAlarmType_Object = MibTableColumn
equipmentCurrentAlarmType = _EquipmentCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2, 2, 1, 1),
    _EquipmentCurrentAlarmType_Type()
)
equipmentCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentCurrentAlarmType.setStatus("current")
_EquipmentCurrentAlarmSeverity_Type = TrapAlarmSeverity
_EquipmentCurrentAlarmSeverity_Object = MibTableColumn
equipmentCurrentAlarmSeverity = _EquipmentCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 2, 2, 1, 2),
    _EquipmentCurrentAlarmSeverity_Type()
)
equipmentCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentCurrentAlarmSeverity.setStatus("current")
_NeAlarms_ObjectIdentity = ObjectIdentity
neAlarms = _NeAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 3)
)


class _NeAlarmAuthFailSource_Type(Integer32):
    """Custom type neAlarmAuthFailSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nofail", 1),
          ("snmpagent", 2),
          ("logincmd", 3),
          ("sucmd", 4),
          ("webitf", 5),
          ("sshd", 7),
          ("ftpcmd", 8),
          ("ppp", 9))
    )


_NeAlarmAuthFailSource_Type.__name__ = "Integer32"
_NeAlarmAuthFailSource_Object = MibScalar
neAlarmAuthFailSource = _NeAlarmAuthFailSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 3, 1),
    _NeAlarmAuthFailSource_Type()
)
neAlarmAuthFailSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmAuthFailSource.setStatus("current")
_NeAlarmAuthFailDescription_Type = DisplayString
_NeAlarmAuthFailDescription_Object = MibScalar
neAlarmAuthFailDescription = _NeAlarmAuthFailDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 1, 3, 2),
    _NeAlarmAuthFailDescription_Type()
)
neAlarmAuthFailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmAuthFailDescription.setStatus("current")
_AdminMIB_ObjectIdentity = ObjectIdentity
adminMIB = _AdminMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2)
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
        ("fsp2000", 1)
    )


_NeType_Type.__name__ = "Integer32"
_NeType_Object = MibScalar
neType = _NeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 2),
    _NeMibVariant_Type()
)
neMibVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMibVariant.setStatus("current")
_NeTrapsinkTable_Object = MibTable
neTrapsinkTable = _NeTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 3)
)
if mibBuilder.loadTexts:
    neTrapsinkTable.setStatus("current")
_NeTrapsinkEntry_Object = MibTableRow
neTrapsinkEntry = _NeTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 3, 1)
)
neTrapsinkEntry.setIndexNames(
    (0, "FSP2000-R2-MIB", "neTrapsinkAddress"),
)
if mibBuilder.loadTexts:
    neTrapsinkEntry.setStatus("current")
_NeTrapsinkAddress_Type = IpAddress
_NeTrapsinkAddress_Object = MibTableColumn
neTrapsinkAddress = _NeTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 3, 1, 1),
    _NeTrapsinkAddress_Type()
)
neTrapsinkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neTrapsinkAddress.setStatus("current")
_NeTrapsinkCommunity_Type = DisplayString
_NeTrapsinkCommunity_Object = MibTableColumn
neTrapsinkCommunity = _NeTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 3, 1, 2),
    _NeTrapsinkCommunity_Type()
)
neTrapsinkCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkCommunity.setStatus("current")


class _NeTrapsinkPort_Type(Integer32):
    """Custom type neTrapsinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NeTrapsinkPort_Type.__name__ = "Integer32"
_NeTrapsinkPort_Object = MibTableColumn
neTrapsinkPort = _NeTrapsinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 3, 1, 3),
    _NeTrapsinkPort_Type()
)
neTrapsinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkPort.setStatus("current")
_NeTrapsinkRowStatus_Type = RowStatus
_NeTrapsinkRowStatus_Object = MibTableColumn
neTrapsinkRowStatus = _NeTrapsinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 3, 1, 4),
    _NeTrapsinkRowStatus_Type()
)
neTrapsinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkRowStatus.setStatus("current")
_NeManufacturer_Type = DisplayString
_NeManufacturer_Object = MibScalar
neManufacturer = _NeManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 4),
    _NeManufacturer_Type()
)
neManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neManufacturer.setStatus("current")
_NeState_Type = NEState
_NeState_Object = MibScalar
neState = _NeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 5),
    _NeState_Type()
)
neState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neState.setStatus("current")
_NeEventsLogged_Type = TrapCounter
_NeEventsLogged_Object = MibScalar
neEventsLogged = _NeEventsLogged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 6),
    _NeEventsLogged_Type()
)
neEventsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventsLogged.setStatus("current")
_NeEventLogTable_Object = MibTable
neEventLogTable = _NeEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 7)
)
if mibBuilder.loadTexts:
    neEventLogTable.setStatus("current")
_NeEventLogEntry_Object = MibTableRow
neEventLogEntry = _NeEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 7, 1)
)
neEventLogEntry.setIndexNames(
    (0, "FSP2000-R2-MIB", "neEventLogIndex"),
)
if mibBuilder.loadTexts:
    neEventLogEntry.setStatus("current")
_NeEventLogIndex_Type = Unsigned32
_NeEventLogIndex_Object = MibTableColumn
neEventLogIndex = _NeEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 7, 1, 1),
    _NeEventLogIndex_Type()
)
neEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neEventLogIndex.setStatus("current")
_NeEventLogTimeStamp_Type = DateAndTime
_NeEventLogTimeStamp_Object = MibTableColumn
neEventLogTimeStamp = _NeEventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 7, 1, 2),
    _NeEventLogTimeStamp_Type()
)
neEventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogTimeStamp.setStatus("current")
_NeEventLogNotificationOID_Type = ObjectIdentifier
_NeEventLogNotificationOID_Object = MibTableColumn
neEventLogNotificationOID = _NeEventLogNotificationOID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 7, 1, 3),
    _NeEventLogNotificationOID_Type()
)
neEventLogNotificationOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogNotificationOID.setStatus("current")
_NeEventLogIndexTranslation_Type = IndexTranslation
_NeEventLogIndexTranslation_Object = MibTableColumn
neEventLogIndexTranslation = _NeEventLogIndexTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 7, 1, 4),
    _NeEventLogIndexTranslation_Type()
)
neEventLogIndexTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogIndexTranslation.setStatus("current")
_NeEventLogVarTable_Object = MibTable
neEventLogVarTable = _NeEventLogVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8)
)
if mibBuilder.loadTexts:
    neEventLogVarTable.setStatus("current")
_NeEventLogVarEntry_Object = MibTableRow
neEventLogVarEntry = _NeEventLogVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8, 1)
)
neEventLogVarEntry.setIndexNames(
    (0, "FSP2000-R2-MIB", "neEventLogIndex"),
    (0, "FSP2000-R2-MIB", "neEventLogVarIndex"),
)
if mibBuilder.loadTexts:
    neEventLogVarEntry.setStatus("current")
_NeEventLogVarIndex_Type = Unsigned32
_NeEventLogVarIndex_Object = MibTableColumn
neEventLogVarIndex = _NeEventLogVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8, 1, 1),
    _NeEventLogVarIndex_Type()
)
neEventLogVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neEventLogVarIndex.setStatus("current")
_NeEventLogVarId_Type = ObjectIdentifier
_NeEventLogVarId_Object = MibTableColumn
neEventLogVarId = _NeEventLogVarId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8, 1, 2),
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
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("integer32", 1),
          ("ipAddress", 2),
          ("octetString", 3),
          ("objectId", 4))
    )


_NeEventLogVarType_Type.__name__ = "Integer32"
_NeEventLogVarType_Object = MibTableColumn
neEventLogVarType = _NeEventLogVarType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8, 1, 3),
    _NeEventLogVarType_Type()
)
neEventLogVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarType.setStatus("current")
_NeEventLogVarInteger32Val_Type = Integer32
_NeEventLogVarInteger32Val_Object = MibTableColumn
neEventLogVarInteger32Val = _NeEventLogVarInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8, 1, 4),
    _NeEventLogVarInteger32Val_Type()
)
neEventLogVarInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarInteger32Val.setStatus("current")
_NeEventLogVarIpAddressVal_Type = IpAddress
_NeEventLogVarIpAddressVal_Object = MibTableColumn
neEventLogVarIpAddressVal = _NeEventLogVarIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8, 1, 5),
    _NeEventLogVarIpAddressVal_Type()
)
neEventLogVarIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarIpAddressVal.setStatus("current")


class _NeEventLogVarOctetStringVal_Type(OctetString):
    """Custom type neEventLogVarOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NeEventLogVarOctetStringVal_Type.__name__ = "OctetString"
_NeEventLogVarOctetStringVal_Object = MibTableColumn
neEventLogVarOctetStringVal = _NeEventLogVarOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8, 1, 6),
    _NeEventLogVarOctetStringVal_Type()
)
neEventLogVarOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarOctetStringVal.setStatus("current")
_NeEventLogVarOidVal_Type = ObjectIdentifier
_NeEventLogVarOidVal_Object = MibTableColumn
neEventLogVarOidVal = _NeEventLogVarOidVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 8, 1, 7),
    _NeEventLogVarOidVal_Type()
)
neEventLogVarOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarOidVal.setStatus("current")
_NeSNMPSet_Type = AccessState
_NeSNMPSet_Object = MibScalar
neSNMPSet = _NeSNMPSet_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 9),
    _NeSNMPSet_Type()
)
neSNMPSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neSNMPSet.setStatus("deprecated")
_SoftwareUpgradeMIB_ObjectIdentity = ObjectIdentity
softwareUpgradeMIB = _SoftwareUpgradeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10)
)
_SupportFspSwUpgradeTable_Type = AvailState
_SupportFspSwUpgradeTable_Object = MibScalar
supportFspSwUpgradeTable = _SupportFspSwUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 1),
    _SupportFspSwUpgradeTable_Type()
)
supportFspSwUpgradeTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportFspSwUpgradeTable.setStatus("current")
_ActiveApplicationSwVersion_Type = DisplayString
_ActiveApplicationSwVersion_Object = MibScalar
activeApplicationSwVersion = _ActiveApplicationSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 2),
    _ActiveApplicationSwVersion_Type()
)
activeApplicationSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeApplicationSwVersion.setStatus("current")
_InactiveApplicationSwVersion_Type = DisplayString
_InactiveApplicationSwVersion_Object = MibScalar
inactiveApplicationSwVersion = _InactiveApplicationSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 3),
    _InactiveApplicationSwVersion_Type()
)
inactiveApplicationSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inactiveApplicationSwVersion.setStatus("current")
_ActiveOperatingSwVersion_Type = DisplayString
_ActiveOperatingSwVersion_Object = MibScalar
activeOperatingSwVersion = _ActiveOperatingSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 4),
    _ActiveOperatingSwVersion_Type()
)
activeOperatingSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeOperatingSwVersion.setStatus("current")
_InactiveOperatingSwVersion_Type = DisplayString
_InactiveOperatingSwVersion_Object = MibScalar
inactiveOperatingSwVersion = _InactiveOperatingSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 5),
    _InactiveOperatingSwVersion_Type()
)
inactiveOperatingSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inactiveOperatingSwVersion.setStatus("current")
_FspSwUpgradeTable_Object = MibTable
fspSwUpgradeTable = _FspSwUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6)
)
if mibBuilder.loadTexts:
    fspSwUpgradeTable.setStatus("current")
_FspSwUpgradeEntry_Object = MibTableRow
fspSwUpgradeEntry = _FspSwUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1)
)
fspSwUpgradeEntry.setIndexNames(
    (0, "FSP2000-R2-MIB", "fspSwUpgradeIndex"),
)
if mibBuilder.loadTexts:
    fspSwUpgradeEntry.setStatus("current")


class _FspSwUpgradeIndex_Type(Integer32):
    """Custom type fspSwUpgradeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_FspSwUpgradeIndex_Type.__name__ = "Integer32"
_FspSwUpgradeIndex_Object = MibTableColumn
fspSwUpgradeIndex = _FspSwUpgradeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 1),
    _FspSwUpgradeIndex_Type()
)
fspSwUpgradeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fspSwUpgradeIndex.setStatus("current")
_FspSwUpgradeServerIpAddress_Type = IpAddress
_FspSwUpgradeServerIpAddress_Object = MibTableColumn
fspSwUpgradeServerIpAddress = _FspSwUpgradeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 2),
    _FspSwUpgradeServerIpAddress_Type()
)
fspSwUpgradeServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeServerIpAddress.setStatus("current")
_FspSwUpgradeServerLogin_Type = DisplayString
_FspSwUpgradeServerLogin_Object = MibTableColumn
fspSwUpgradeServerLogin = _FspSwUpgradeServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 3),
    _FspSwUpgradeServerLogin_Type()
)
fspSwUpgradeServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeServerLogin.setStatus("current")
_FspSwUpgradeServerPassword_Type = DisplayString
_FspSwUpgradeServerPassword_Object = MibTableColumn
fspSwUpgradeServerPassword = _FspSwUpgradeServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 4),
    _FspSwUpgradeServerPassword_Type()
)
fspSwUpgradeServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeServerPassword.setStatus("current")
_FspSwUpgradeServerFileLocation_Type = DisplayString
_FspSwUpgradeServerFileLocation_Object = MibTableColumn
fspSwUpgradeServerFileLocation = _FspSwUpgradeServerFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 5),
    _FspSwUpgradeServerFileLocation_Type()
)
fspSwUpgradeServerFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeServerFileLocation.setStatus("current")
_FspSwUpgradeFileName_Type = DisplayString
_FspSwUpgradeFileName_Object = MibTableColumn
fspSwUpgradeFileName = _FspSwUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 7),
    _FspSwUpgradeType_Type()
)
fspSwUpgradeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspSwUpgradeType.setStatus("current")


class _FspSwUpgradeProtocol_Type(Integer32):
    """Custom type fspSwUpgradeProtocol based on Integer32"""
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
        *(("ftp", 1),
          ("tftp", 2),
          ("local", 3),
          ("scp", 4))
    )


_FspSwUpgradeProtocol_Type.__name__ = "Integer32"
_FspSwUpgradeProtocol_Object = MibTableColumn
fspSwUpgradeProtocol = _FspSwUpgradeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 8),
    _FspSwUpgradeProtocol_Type()
)
fspSwUpgradeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeProtocol.setStatus("current")


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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("download", 2),
          ("activate", 3),
          ("downloadActivate", 4),
          ("downloadActivateReboot", 5),
          ("activateReboot", 6),
          ("reboot", 7))
    )


_FspSwUpgradeRequest_Type.__name__ = "Integer32"
_FspSwUpgradeRequest_Object = MibTableColumn
fspSwUpgradeRequest = _FspSwUpgradeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 9),
    _FspSwUpgradeRequest_Type()
)
fspSwUpgradeRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspSwUpgradeRequest.setStatus("current")
_FspSwUpgradeStatus_Type = SwUpgradeStatusType
_FspSwUpgradeStatus_Object = MibTableColumn
fspSwUpgradeStatus = _FspSwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 10, 6, 1, 10),
    _FspSwUpgradeStatus_Type()
)
fspSwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspSwUpgradeStatus.setStatus("current")
_NeTrapsenderAddress_Type = IpAddress
_NeTrapsenderAddress_Object = MibScalar
neTrapsenderAddress = _NeTrapsenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 11),
    _NeTrapsenderAddress_Type()
)
neTrapsenderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTrapsenderAddress.setStatus("current")
_SnmpWriteAccessRestriction_Type = EnableState
_SnmpWriteAccessRestriction_Object = MibScalar
snmpWriteAccessRestriction = _SnmpWriteAccessRestriction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 12),
    _SnmpWriteAccessRestriction_Type()
)
snmpWriteAccessRestriction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpWriteAccessRestriction.setStatus("current")
_SnmpWriteAccessTable_Object = MibTable
snmpWriteAccessTable = _SnmpWriteAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 13)
)
if mibBuilder.loadTexts:
    snmpWriteAccessTable.setStatus("current")
_SnmpWriteAccessEntry_Object = MibTableRow
snmpWriteAccessEntry = _SnmpWriteAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 13, 1)
)
snmpWriteAccessEntry.setIndexNames(
    (0, "FSP2000-R2-MIB", "snmpWriteAccessNmsAddress"),
)
if mibBuilder.loadTexts:
    snmpWriteAccessEntry.setStatus("current")
_SnmpWriteAccessNmsAddress_Type = IpAddress
_SnmpWriteAccessNmsAddress_Object = MibTableColumn
snmpWriteAccessNmsAddress = _SnmpWriteAccessNmsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 13, 1, 1),
    _SnmpWriteAccessNmsAddress_Type()
)
snmpWriteAccessNmsAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpWriteAccessNmsAddress.setStatus("current")
_SnmpWriteAccessNmsName_Type = DisplayString
_SnmpWriteAccessNmsName_Object = MibTableColumn
snmpWriteAccessNmsName = _SnmpWriteAccessNmsName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 13, 1, 2),
    _SnmpWriteAccessNmsName_Type()
)
snmpWriteAccessNmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpWriteAccessNmsName.setStatus("current")
_NeMemorySizeTotal_Type = KBytes
_NeMemorySizeTotal_Object = MibScalar
neMemorySizeTotal = _NeMemorySizeTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 14),
    _NeMemorySizeTotal_Type()
)
neMemorySizeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMemorySizeTotal.setStatus("current")
_NeMemorySizeFree_Type = KBytes
_NeMemorySizeFree_Object = MibScalar
neMemorySizeFree = _NeMemorySizeFree_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 15),
    _NeMemorySizeFree_Type()
)
neMemorySizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMemorySizeFree.setStatus("current")
_NeStorageTable_Object = MibTable
neStorageTable = _NeStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 16)
)
if mibBuilder.loadTexts:
    neStorageTable.setStatus("current")
_NeStorageEntry_Object = MibTableRow
neStorageEntry = _NeStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 16, 1)
)
neStorageEntry.setIndexNames(
    (0, "FSP2000-R2-MIB", "neStorageIndex"),
)
if mibBuilder.loadTexts:
    neStorageEntry.setStatus("current")
_NeStorageIndex_Type = Unsigned32
_NeStorageIndex_Object = MibTableColumn
neStorageIndex = _NeStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 16, 1, 1),
    _NeStorageIndex_Type()
)
neStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neStorageIndex.setStatus("current")
_NeStorageDescr_Type = SnmpAdminString
_NeStorageDescr_Object = MibTableColumn
neStorageDescr = _NeStorageDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 16, 1, 2),
    _NeStorageDescr_Type()
)
neStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStorageDescr.setStatus("current")
_NeStorageCapacity_Type = KBytes
_NeStorageCapacity_Object = MibTableColumn
neStorageCapacity = _NeStorageCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 16, 1, 3),
    _NeStorageCapacity_Type()
)
neStorageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStorageCapacity.setStatus("current")
_NeStorageAvailable_Type = KBytes
_NeStorageAvailable_Object = MibTableColumn
neStorageAvailable = _NeStorageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 2, 16, 1, 4),
    _NeStorageAvailable_Type()
)
neStorageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStorageAvailable.setStatus("current")
_TrapMIB_ObjectIdentity = ObjectIdentity
trapMIB = _TrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3)
)
_TrapMIBPrefix_ObjectIdentity = ObjectIdentity
trapMIBPrefix = _TrapMIBPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0)
)
_TrapVariables_ObjectIdentity = ObjectIdentity
trapVariables = _TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 1)
)
_ContainerState_Type = ContainerState
_ContainerState_Object = MibScalar
containerState = _ContainerState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 1, 1),
    _ContainerState_Type()
)
containerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    containerState.setStatus("current")
_ContainsPhysicalIndex_Type = PhysicalIndex
_ContainsPhysicalIndex_Object = MibScalar
containsPhysicalIndex = _ContainsPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 1, 2),
    _ContainsPhysicalIndex_Type()
)
containsPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    containsPhysicalIndex.setStatus("current")
_TimeStamp_Type = DateAndTime
_TimeStamp_Object = MibScalar
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 1, 3),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timeStamp.setStatus("current")
_IndexTranslation_Type = IndexTranslation
_IndexTranslation_Object = MibScalar
indexTranslation = _IndexTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 1, 4),
    _IndexTranslation_Type()
)
indexTranslation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    indexTranslation.setStatus("current")
_ObjectId_Type = ObjectIdentifier
_ObjectId_Object = MibScalar
objectId = _ObjectId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 1, 5),
    _ObjectId_Type()
)
objectId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    objectId.setStatus("current")
_ConfigurationMIB_ObjectIdentity = ObjectIdentity
configurationMIB = _ConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4)
)
_InterfaceConfiguration_ObjectIdentity = ObjectIdentity
interfaceConfiguration = _InterfaceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1)
)
_InterfaceTTTable_Object = MibTable
interfaceTTTable = _InterfaceTTTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceTTTable.setStatus("current")
_InterfaceTTEntry_Object = MibTableRow
interfaceTTEntry = _InterfaceTTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1)
)
interfaceTTEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceTTEntry.setStatus("current")
_InterfaceTTLoopState_Type = OnOff
_InterfaceTTLoopState_Object = MibTableColumn
interfaceTTLoopState = _InterfaceTTLoopState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 1),
    _InterfaceTTLoopState_Type()
)
interfaceTTLoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTLoopState.setStatus("current")
_InterfaceTTLaserTxConfig_Type = LaserTxConfig
_InterfaceTTLaserTxConfig_Object = MibTableColumn
interfaceTTLaserTxConfig = _InterfaceTTLaserTxConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 2),
    _InterfaceTTLaserTxConfig_Type()
)
interfaceTTLaserTxConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTLaserTxConfig.setStatus("current")


class _InterfaceTTLaserTxCurrent_Type(Integer32):
    """Custom type interfaceTTLaserTxCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 150),
    )


_InterfaceTTLaserTxCurrent_Type.__name__ = "Integer32"
_InterfaceTTLaserTxCurrent_Object = MibTableColumn
interfaceTTLaserTxCurrent = _InterfaceTTLaserTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 3),
    _InterfaceTTLaserTxCurrent_Type()
)
interfaceTTLaserTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTLaserTxCurrent.setStatus("current")


class _InterfaceTTLaserTxTemp_Type(Integer32):
    """Custom type interfaceTTLaserTxTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 90),
    )


_InterfaceTTLaserTxTemp_Type.__name__ = "Integer32"
_InterfaceTTLaserTxTemp_Object = MibTableColumn
interfaceTTLaserTxTemp = _InterfaceTTLaserTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 4),
    _InterfaceTTLaserTxTemp_Type()
)
interfaceTTLaserTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTLaserTxTemp.setStatus("deprecated")
_InterfaceTTRxClockFreq_Type = ClockDataRate
_InterfaceTTRxClockFreq_Object = MibTableColumn
interfaceTTRxClockFreq = _InterfaceTTRxClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 5),
    _InterfaceTTRxClockFreq_Type()
)
interfaceTTRxClockFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTRxClockFreq.setStatus("current")
_InterfaceTTRxClockType_Type = ClockDataRateBitfield
_InterfaceTTRxClockType_Object = MibTableColumn
interfaceTTRxClockType = _InterfaceTTRxClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 6),
    _InterfaceTTRxClockType_Type()
)
interfaceTTRxClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTRxClockType.setStatus("current")
_InterfaceTTWavelength_Type = DisplayString
_InterfaceTTWavelength_Object = MibTableColumn
interfaceTTWavelength = _InterfaceTTWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 7),
    _InterfaceTTWavelength_Type()
)
interfaceTTWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTWavelength.setStatus("current")
_InterfaceTTOpticalInputPower_Type = Integer32
_InterfaceTTOpticalInputPower_Object = MibTableColumn
interfaceTTOpticalInputPower = _InterfaceTTOpticalInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 8),
    _InterfaceTTOpticalInputPower_Type()
)
interfaceTTOpticalInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTOpticalInputPower.setStatus("current")
_InterfaceTTOpticalOutputPower_Type = Integer32
_InterfaceTTOpticalOutputPower_Object = MibTableColumn
interfaceTTOpticalOutputPower = _InterfaceTTOpticalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 9),
    _InterfaceTTOpticalOutputPower_Type()
)
interfaceTTOpticalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTOpticalOutputPower.setStatus("current")
_InterfaceTTConnector_Type = DisplayString
_InterfaceTTConnector_Object = MibTableColumn
interfaceTTConnector = _InterfaceTTConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 10),
    _InterfaceTTConnector_Type()
)
interfaceTTConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTConnector.setStatus("current")
_InterfaceTTFiberType_Type = DisplayString
_InterfaceTTFiberType_Object = MibTableColumn
interfaceTTFiberType = _InterfaceTTFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 11),
    _InterfaceTTFiberType_Type()
)
interfaceTTFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTFiberType.setStatus("current")
_InterfaceTTResultDRTranspLow_Type = Integer32
_InterfaceTTResultDRTranspLow_Object = MibTableColumn
interfaceTTResultDRTranspLow = _InterfaceTTResultDRTranspLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 12),
    _InterfaceTTResultDRTranspLow_Type()
)
interfaceTTResultDRTranspLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTResultDRTranspLow.setStatus("current")
_InterfaceTTResultDRTranspHigh_Type = Integer32
_InterfaceTTResultDRTranspHigh_Object = MibTableColumn
interfaceTTResultDRTranspHigh = _InterfaceTTResultDRTranspHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 13),
    _InterfaceTTResultDRTranspHigh_Type()
)
interfaceTTResultDRTranspHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTResultDRTranspHigh.setStatus("current")
_InterfaceTTIncommingDataRate_Type = Integer32
_InterfaceTTIncommingDataRate_Object = MibTableColumn
interfaceTTIncommingDataRate = _InterfaceTTIncommingDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 14),
    _InterfaceTTIncommingDataRate_Type()
)
interfaceTTIncommingDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTIncommingDataRate.setStatus("current")


class _InterfaceTTDisparityCtrl_Type(Integer32):
    """Custom type interfaceTTDisparityCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disparityOn", 2),
          ("disparityOff", 3))
    )


_InterfaceTTDisparityCtrl_Type.__name__ = "Integer32"
_InterfaceTTDisparityCtrl_Object = MibTableColumn
interfaceTTDisparityCtrl = _InterfaceTTDisparityCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 15),
    _InterfaceTTDisparityCtrl_Type()
)
interfaceTTDisparityCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTDisparityCtrl.setStatus("current")
_InterfaceTTLaserTxStatus_Type = LaserTxStatus
_InterfaceTTLaserTxStatus_Object = MibTableColumn
interfaceTTLaserTxStatus = _InterfaceTTLaserTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 16),
    _InterfaceTTLaserTxStatus_Type()
)
interfaceTTLaserTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTLaserTxStatus.setStatus("current")


class _InterfaceTTLocalLOSSuppression_Type(Integer32):
    """Custom type interfaceTTLocalLOSSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("localLosSuppressionOn", 2),
          ("localLosSuppressionOff", 3))
    )


_InterfaceTTLocalLOSSuppression_Type.__name__ = "Integer32"
_InterfaceTTLocalLOSSuppression_Object = MibTableColumn
interfaceTTLocalLOSSuppression = _InterfaceTTLocalLOSSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 17),
    _InterfaceTTLocalLOSSuppression_Type()
)
interfaceTTLocalLOSSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTTLocalLOSSuppression.setStatus("current")
_InterfaceTTLaserTxTempTenth_Type = Integer32
_InterfaceTTLaserTxTempTenth_Object = MibTableColumn
interfaceTTLaserTxTempTenth = _InterfaceTTLaserTxTempTenth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 1, 1, 18),
    _InterfaceTTLaserTxTempTenth_Type()
)
interfaceTTLaserTxTempTenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTTLaserTxTempTenth.setStatus("current")
_ElectricalInterfaceTable_Object = MibTable
electricalInterfaceTable = _ElectricalInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    electricalInterfaceTable.setStatus("current")
_ElectricalInterfaceEntry_Object = MibTableRow
electricalInterfaceEntry = _ElectricalInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 2, 1)
)
electricalInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    electricalInterfaceEntry.setStatus("current")
_ElectricalInterfaceTxAutoNeg_Type = OnOff
_ElectricalInterfaceTxAutoNeg_Object = MibTableColumn
electricalInterfaceTxAutoNeg = _ElectricalInterfaceTxAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 2, 1, 1),
    _ElectricalInterfaceTxAutoNeg_Type()
)
electricalInterfaceTxAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceTxAutoNeg.setStatus("current")


class _ElectricalInterfaceDuplexMode_Type(Integer32):
    """Custom type electricalInterfaceDuplexMode based on Integer32"""
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


_ElectricalInterfaceDuplexMode_Type.__name__ = "Integer32"
_ElectricalInterfaceDuplexMode_Object = MibTableColumn
electricalInterfaceDuplexMode = _ElectricalInterfaceDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 2, 1, 2),
    _ElectricalInterfaceDuplexMode_Type()
)
electricalInterfaceDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceDuplexMode.setStatus("current")


class _ElectricalInterfaceLineSpeed_Type(Integer32):
    """Custom type electricalInterfaceLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3))
    )


_ElectricalInterfaceLineSpeed_Type.__name__ = "Integer32"
_ElectricalInterfaceLineSpeed_Object = MibTableColumn
electricalInterfaceLineSpeed = _ElectricalInterfaceLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 2, 1, 3),
    _ElectricalInterfaceLineSpeed_Type()
)
electricalInterfaceLineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceLineSpeed.setStatus("current")


class _ElectricalInterfaceLoopState_Type(Integer32):
    """Custom type electricalInterfaceLoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notApplicable", 3))
    )


_ElectricalInterfaceLoopState_Type.__name__ = "Integer32"
_ElectricalInterfaceLoopState_Object = MibTableColumn
electricalInterfaceLoopState = _ElectricalInterfaceLoopState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 2, 1, 4),
    _ElectricalInterfaceLoopState_Type()
)
electricalInterfaceLoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceLoopState.setStatus("current")
_ElectricalInterfaceRxClockFreq_Type = ClockDataRate
_ElectricalInterfaceRxClockFreq_Object = MibTableColumn
electricalInterfaceRxClockFreq = _ElectricalInterfaceRxClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 2, 1, 5),
    _ElectricalInterfaceRxClockFreq_Type()
)
electricalInterfaceRxClockFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalInterfaceRxClockFreq.setStatus("current")
_ElectricalInterfaceRxClockType_Type = ClockDataRateBitfield
_ElectricalInterfaceRxClockType_Object = MibTableColumn
electricalInterfaceRxClockType = _ElectricalInterfaceRxClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 2, 1, 6),
    _ElectricalInterfaceRxClockType_Type()
)
electricalInterfaceRxClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    electricalInterfaceRxClockType.setStatus("current")
_EdfaInterfaceTable_Object = MibTable
edfaInterfaceTable = _EdfaInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    edfaInterfaceTable.setStatus("current")
_EdfaInterfaceEntry_Object = MibTableRow
edfaInterfaceEntry = _EdfaInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1)
)
edfaInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    edfaInterfaceEntry.setStatus("current")


class _EdfaInterfaceOpticalBandType_Type(Integer32):
    """Custom type edfaInterfaceOpticalBandType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("cband", 2),
          ("lband", 3))
    )


_EdfaInterfaceOpticalBandType_Type.__name__ = "Integer32"
_EdfaInterfaceOpticalBandType_Object = MibTableColumn
edfaInterfaceOpticalBandType = _EdfaInterfaceOpticalBandType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 1),
    _EdfaInterfaceOpticalBandType_Type()
)
edfaInterfaceOpticalBandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceOpticalBandType.setStatus("current")
_EdfaInterfacePumpLaserTxConfig_Type = LaserTxConfig
_EdfaInterfacePumpLaserTxConfig_Object = MibTableColumn
edfaInterfacePumpLaserTxConfig = _EdfaInterfacePumpLaserTxConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 2),
    _EdfaInterfacePumpLaserTxConfig_Type()
)
edfaInterfacePumpLaserTxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserTxConfig.setStatus("current")


class _EdfaInterfaceOpticalInputPower_Type(Integer32):
    """Custom type edfaInterfaceOpticalInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(-400, 200),
    )


_EdfaInterfaceOpticalInputPower_Type.__name__ = "Integer32"
_EdfaInterfaceOpticalInputPower_Object = MibTableColumn
edfaInterfaceOpticalInputPower = _EdfaInterfaceOpticalInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 3),
    _EdfaInterfaceOpticalInputPower_Type()
)
edfaInterfaceOpticalInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceOpticalInputPower.setStatus("current")


class _EdfaInterfaceOpticalOutputPower_Type(Integer32):
    """Custom type edfaInterfaceOpticalOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(-400, 250),
    )


_EdfaInterfaceOpticalOutputPower_Type.__name__ = "Integer32"
_EdfaInterfaceOpticalOutputPower_Object = MibTableColumn
edfaInterfaceOpticalOutputPower = _EdfaInterfaceOpticalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 4),
    _EdfaInterfaceOpticalOutputPower_Type()
)
edfaInterfaceOpticalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceOpticalOutputPower.setStatus("current")


class _EdfaInterfaceModuleTemp_Type(Integer32):
    """Custom type edfaInterfaceModuleTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 90),
    )


_EdfaInterfaceModuleTemp_Type.__name__ = "Integer32"
_EdfaInterfaceModuleTemp_Object = MibTableColumn
edfaInterfaceModuleTemp = _EdfaInterfaceModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 5),
    _EdfaInterfaceModuleTemp_Type()
)
edfaInterfaceModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceModuleTemp.setStatus("current")


class _EdfaInterfacePumpLaserPower_Type(Integer32):
    """Custom type edfaInterfacePumpLaserPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(0, 150),
    )


_EdfaInterfacePumpLaserPower_Type.__name__ = "Integer32"
_EdfaInterfacePumpLaserPower_Object = MibTableColumn
edfaInterfacePumpLaserPower = _EdfaInterfacePumpLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 6),
    _EdfaInterfacePumpLaserPower_Type()
)
edfaInterfacePumpLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserPower.setStatus("current")


class _EdfaInterfacePumpLaserCurrent_Type(Integer32):
    """Custom type edfaInterfacePumpLaserCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(0, 1024),
    )


_EdfaInterfacePumpLaserCurrent_Type.__name__ = "Integer32"
_EdfaInterfacePumpLaserCurrent_Object = MibTableColumn
edfaInterfacePumpLaserCurrent = _EdfaInterfacePumpLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 7),
    _EdfaInterfacePumpLaserCurrent_Type()
)
edfaInterfacePumpLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserCurrent.setStatus("current")


class _EdfaInterfacePumpLaserTxTemp_Type(Integer32):
    """Custom type edfaInterfacePumpLaserTxTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 300),
    )


_EdfaInterfacePumpLaserTxTemp_Type.__name__ = "Integer32"
_EdfaInterfacePumpLaserTxTemp_Object = MibTableColumn
edfaInterfacePumpLaserTxTemp = _EdfaInterfacePumpLaserTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 8),
    _EdfaInterfacePumpLaserTxTemp_Type()
)
edfaInterfacePumpLaserTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserTxTemp.setStatus("current")


class _EdfaInterfacePumpLaserConfig_Type(Integer32):
    """Custom type edfaInterfacePumpLaserConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(0, 100),
    )


_EdfaInterfacePumpLaserConfig_Type.__name__ = "Integer32"
_EdfaInterfacePumpLaserConfig_Object = MibTableColumn
edfaInterfacePumpLaserConfig = _EdfaInterfacePumpLaserConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 9),
    _EdfaInterfacePumpLaserConfig_Type()
)
edfaInterfacePumpLaserConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserConfig.setStatus("current")


class _EdfaInterfaceTECCurrent_Type(Integer32):
    """Custom type edfaInterfaceTECCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(0, 2000),
    )


_EdfaInterfaceTECCurrent_Type.__name__ = "Integer32"
_EdfaInterfaceTECCurrent_Object = MibTableColumn
edfaInterfaceTECCurrent = _EdfaInterfaceTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 10),
    _EdfaInterfaceTECCurrent_Type()
)
edfaInterfaceTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceTECCurrent.setStatus("current")


class _EdfaInterfaceMaxOperPower_Type(Integer32):
    """Custom type edfaInterfaceMaxOperPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(0, 255),
    )


_EdfaInterfaceMaxOperPower_Type.__name__ = "Integer32"
_EdfaInterfaceMaxOperPower_Object = MibTableColumn
edfaInterfaceMaxOperPower = _EdfaInterfaceMaxOperPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 11),
    _EdfaInterfaceMaxOperPower_Type()
)
edfaInterfaceMaxOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceMaxOperPower.setStatus("current")
_EdfaInterfaceOIPAlarmOnOff_Type = OnOff
_EdfaInterfaceOIPAlarmOnOff_Object = MibTableColumn
edfaInterfaceOIPAlarmOnOff = _EdfaInterfaceOIPAlarmOnOff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 12),
    _EdfaInterfaceOIPAlarmOnOff_Type()
)
edfaInterfaceOIPAlarmOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfaceOIPAlarmOnOff.setStatus("current")
_EdfaInterfacePumpLaserTxStatus_Type = LaserTxStatus
_EdfaInterfacePumpLaserTxStatus_Object = MibTableColumn
edfaInterfacePumpLaserTxStatus = _EdfaInterfacePumpLaserTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 3, 1, 13),
    _EdfaInterfacePumpLaserTxStatus_Type()
)
edfaInterfacePumpLaserTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaInterfacePumpLaserTxStatus.setStatus("current")
_RemoteOptSwitchInterfaceTable_Object = MibTable
remoteOptSwitchInterfaceTable = _RemoteOptSwitchInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    remoteOptSwitchInterfaceTable.setStatus("current")
_RemoteOptSwitchInterfaceEntry_Object = MibTableRow
remoteOptSwitchInterfaceEntry = _RemoteOptSwitchInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 4, 1)
)
remoteOptSwitchInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    remoteOptSwitchInterfaceEntry.setStatus("current")
_RemoteOptSwitchInterfaceLambda_Type = DisplayString
_RemoteOptSwitchInterfaceLambda_Object = MibTableColumn
remoteOptSwitchInterfaceLambda = _RemoteOptSwitchInterfaceLambda_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 4, 1, 1),
    _RemoteOptSwitchInterfaceLambda_Type()
)
remoteOptSwitchInterfaceLambda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOptSwitchInterfaceLambda.setStatus("current")


class _OlmInterfaceLineAttR_Type(Integer32):
    """Custom type olmInterfaceLineAttR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 300),
    )


_OlmInterfaceLineAttR_Type.__name__ = "Integer32"
_OlmInterfaceLineAttR_Object = MibTableColumn
olmInterfaceLineAttR = _OlmInterfaceLineAttR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 4, 1, 2),
    _OlmInterfaceLineAttR_Type()
)
olmInterfaceLineAttR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmInterfaceLineAttR.setStatus("current")


class _OlmInterfaceLineAttT_Type(Integer32):
    """Custom type olmInterfaceLineAttT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 300),
    )


_OlmInterfaceLineAttT_Type.__name__ = "Integer32"
_OlmInterfaceLineAttT_Object = MibTableColumn
olmInterfaceLineAttT = _OlmInterfaceLineAttT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 1, 4, 1, 3),
    _OlmInterfaceLineAttT_Type()
)
olmInterfaceLineAttT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmInterfaceLineAttT.setStatus("current")
_EquipmentConfiguration_ObjectIdentity = ObjectIdentity
equipmentConfiguration = _EquipmentConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")


class _ModuleCapabilities_Type(Integer32):
    """Custom type moduleCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleCapabilities_Type.__name__ = "Integer32"
_ModuleCapabilities_Object = MibTableColumn
moduleCapabilities = _ModuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 1),
    _ModuleCapabilities_Type()
)
moduleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapabilities.setStatus("current")


class _ModuleEnvironmentTemp1_Type(Integer32):
    """Custom type moduleEnvironmentTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 128),
    )


_ModuleEnvironmentTemp1_Type.__name__ = "Integer32"
_ModuleEnvironmentTemp1_Object = MibTableColumn
moduleEnvironmentTemp1 = _ModuleEnvironmentTemp1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 2),
    _ModuleEnvironmentTemp1_Type()
)
moduleEnvironmentTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEnvironmentTemp1.setStatus("current")


class _ModuleEnvironmentTemp1Max_Type(Integer32):
    """Custom type moduleEnvironmentTemp1Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 128),
    )


_ModuleEnvironmentTemp1Max_Type.__name__ = "Integer32"
_ModuleEnvironmentTemp1Max_Object = MibTableColumn
moduleEnvironmentTemp1Max = _ModuleEnvironmentTemp1Max_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 3),
    _ModuleEnvironmentTemp1Max_Type()
)
moduleEnvironmentTemp1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEnvironmentTemp1Max.setStatus("current")


class _ModuleVoltage1_Type(Integer32):
    """Custom type moduleVoltage1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(2000, 5500),
    )


_ModuleVoltage1_Type.__name__ = "Integer32"
_ModuleVoltage1_Object = MibTableColumn
moduleVoltage1 = _ModuleVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 4),
    _ModuleVoltage1_Type()
)
moduleVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltage1.setStatus("current")


class _ModuleVoltage1Max_Type(Integer32):
    """Custom type moduleVoltage1Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(2000, 5500),
    )


_ModuleVoltage1Max_Type.__name__ = "Integer32"
_ModuleVoltage1Max_Object = MibTableColumn
moduleVoltage1Max = _ModuleVoltage1Max_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 5),
    _ModuleVoltage1Max_Type()
)
moduleVoltage1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltage1Max.setStatus("current")


class _ModuleVoltage1Min_Type(Integer32):
    """Custom type moduleVoltage1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(2000, 5500),
    )


_ModuleVoltage1Min_Type.__name__ = "Integer32"
_ModuleVoltage1Min_Object = MibTableColumn
moduleVoltage1Min = _ModuleVoltage1Min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 6),
    _ModuleVoltage1Min_Type()
)
moduleVoltage1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltage1Min.setStatus("current")
_ModuleComment_Type = DisplayString
_ModuleComment_Object = MibTableColumn
moduleComment = _ModuleComment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 7),
    _ModuleComment_Type()
)
moduleComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleComment.setStatus("current")
_ModuleType_Type = ModuleType
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 8),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("current")
_ModuleOfficialName_Type = DisplayString
_ModuleOfficialName_Object = MibTableColumn
moduleOfficialName = _ModuleOfficialName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 1, 1, 9),
    _ModuleOfficialName_Type()
)
moduleOfficialName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleOfficialName.setStatus("current")
_WavelengthChannelModuleTable_Object = MibTable
wavelengthChannelModuleTable = _WavelengthChannelModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    wavelengthChannelModuleTable.setStatus("current")
_WavelengthChannelModuleEntry_Object = MibTableRow
wavelengthChannelModuleEntry = _WavelengthChannelModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1)
)
wavelengthChannelModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    wavelengthChannelModuleEntry.setStatus("current")
_WavelengthChannelModuleRegState_Type = OnOff
_WavelengthChannelModuleRegState_Object = MibTableColumn
wavelengthChannelModuleRegState = _WavelengthChannelModuleRegState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 1),
    _WavelengthChannelModuleRegState_Type()
)
wavelengthChannelModuleRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wavelengthChannelModuleRegState.setStatus("deprecated")
_WavelengthChannelModuleChannel_Type = Integer32
_WavelengthChannelModuleChannel_Object = MibTableColumn
wavelengthChannelModuleChannel = _WavelengthChannelModuleChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 2),
    _WavelengthChannelModuleChannel_Type()
)
wavelengthChannelModuleChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wavelengthChannelModuleChannel.setStatus("current")
_WavelengthChannelModuleScheme_Type = BandScheme
_WavelengthChannelModuleScheme_Object = MibTableColumn
wavelengthChannelModuleScheme = _WavelengthChannelModuleScheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 3),
    _WavelengthChannelModuleScheme_Type()
)
wavelengthChannelModuleScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wavelengthChannelModuleScheme.setStatus("current")
_WdmChannelModuleLowDRTransp_Type = Integer32
_WdmChannelModuleLowDRTransp_Object = MibTableColumn
wdmChannelModuleLowDRTransp = _WdmChannelModuleLowDRTransp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 4),
    _WdmChannelModuleLowDRTransp_Type()
)
wdmChannelModuleLowDRTransp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmChannelModuleLowDRTransp.setStatus("current")
_WdmChannelModuleHighDRTransp_Type = Integer32
_WdmChannelModuleHighDRTransp_Object = MibTableColumn
wdmChannelModuleHighDRTransp = _WdmChannelModuleHighDRTransp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 5),
    _WdmChannelModuleHighDRTransp_Type()
)
wdmChannelModuleHighDRTransp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmChannelModuleHighDRTransp.setStatus("current")
_WavelengthChannelModuleChName_Type = DisplayString
_WavelengthChannelModuleChName_Object = MibTableColumn
wavelengthChannelModuleChName = _WavelengthChannelModuleChName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 6),
    _WavelengthChannelModuleChName_Type()
)
wavelengthChannelModuleChName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wavelengthChannelModuleChName.setStatus("current")
_WdmChannelModuleTMMode_Type = TransmissionMode
_WdmChannelModuleTMMode_Object = MibTableColumn
wdmChannelModuleTMMode = _WdmChannelModuleTMMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 7),
    _WdmChannelModuleTMMode_Type()
)
wdmChannelModuleTMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmChannelModuleTMMode.setStatus("current")
_WdmChannelModuleTMCap_Type = TransmissionModeBitfield
_WdmChannelModuleTMCap_Object = MibTableColumn
wdmChannelModuleTMCap = _WdmChannelModuleTMCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 8),
    _WdmChannelModuleTMCap_Type()
)
wdmChannelModuleTMCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmChannelModuleTMCap.setStatus("current")
_WdmChannelModuleTMCurrentCap_Type = TransmissionModeBitfield
_WdmChannelModuleTMCurrentCap_Object = MibTableColumn
wdmChannelModuleTMCurrentCap = _WdmChannelModuleTMCurrentCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 2, 1, 9),
    _WdmChannelModuleTMCurrentCap_Type()
)
wdmChannelModuleTMCurrentCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmChannelModuleTMCurrentCap.setStatus("current")
_RemoteOptSwitchTable_Object = MibTable
remoteOptSwitchTable = _RemoteOptSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    remoteOptSwitchTable.setStatus("current")
_RemoteOptSwitchEntry_Object = MibTableRow
remoteOptSwitchEntry = _RemoteOptSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 3, 1)
)
remoteOptSwitchEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    remoteOptSwitchEntry.setStatus("current")
_RemoteOptSwitchOperState_Type = SwitchOperState
_RemoteOptSwitchOperState_Object = MibTableColumn
remoteOptSwitchOperState = _RemoteOptSwitchOperState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 3, 1, 1),
    _RemoteOptSwitchOperState_Type()
)
remoteOptSwitchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOptSwitchOperState.setStatus("current")
_RemoteOptSwitchAdminState_Type = SwitchAdminState
_RemoteOptSwitchAdminState_Object = MibTableColumn
remoteOptSwitchAdminState = _RemoteOptSwitchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 3, 1, 2),
    _RemoteOptSwitchAdminState_Type()
)
remoteOptSwitchAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteOptSwitchAdminState.setStatus("current")
_RemoteOptSwitchALS_Type = OnOff
_RemoteOptSwitchALS_Object = MibTableColumn
remoteOptSwitchALS = _RemoteOptSwitchALS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 3, 1, 3),
    _RemoteOptSwitchALS_Type()
)
remoteOptSwitchALS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOptSwitchALS.setStatus("current")


class _RemoteOptSwitchRevertiveMode_Type(Integer32):
    """Custom type remoteOptSwitchRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 1),
          ("revertive", 2))
    )


_RemoteOptSwitchRevertiveMode_Type.__name__ = "Integer32"
_RemoteOptSwitchRevertiveMode_Object = MibTableColumn
remoteOptSwitchRevertiveMode = _RemoteOptSwitchRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 3, 1, 4),
    _RemoteOptSwitchRevertiveMode_Type()
)
remoteOptSwitchRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteOptSwitchRevertiveMode.setStatus("current")


class _RemoteOptSwitchPreferredLine_Type(Integer32):
    """Custom type remoteOptSwitchPreferredLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preferredLineA", 1),
          ("preferredLineB", 2),
          ("preferredNone", 3))
    )


_RemoteOptSwitchPreferredLine_Type.__name__ = "Integer32"
_RemoteOptSwitchPreferredLine_Object = MibTableColumn
remoteOptSwitchPreferredLine = _RemoteOptSwitchPreferredLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 3, 1, 5),
    _RemoteOptSwitchPreferredLine_Type()
)
remoteOptSwitchPreferredLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteOptSwitchPreferredLine.setStatus("current")
_OscModuleTable_Object = MibTable
oscModuleTable = _OscModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    oscModuleTable.setStatus("current")
_OscModuleEntry_Object = MibTableRow
oscModuleEntry = _OscModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 4, 1)
)
oscModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    oscModuleEntry.setStatus("current")


class _OscModuleVoltage2_Type(Integer32):
    """Custom type oscModuleVoltage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(2800, 3800),
    )


_OscModuleVoltage2_Type.__name__ = "Integer32"
_OscModuleVoltage2_Object = MibTableColumn
oscModuleVoltage2 = _OscModuleVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 4, 1, 1),
    _OscModuleVoltage2_Type()
)
oscModuleVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscModuleVoltage2.setStatus("current")


class _OscModuleVoltage3_Type(Integer32):
    """Custom type oscModuleVoltage3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(2000, 3000),
    )


_OscModuleVoltage3_Type.__name__ = "Integer32"
_OscModuleVoltage3_Object = MibTableColumn
oscModuleVoltage3 = _OscModuleVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 4, 1, 2),
    _OscModuleVoltage3_Type()
)
oscModuleVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscModuleVoltage3.setStatus("current")
_MdxModuleTable_Object = MibTable
mdxModuleTable = _MdxModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    mdxModuleTable.setStatus("current")
_MdxModuleEntry_Object = MibTableRow
mdxModuleEntry = _MdxModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 5, 1)
)
mdxModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mdxModuleEntry.setStatus("current")


class _MdxModuleWDMType_Type(Integer32):
    """Custom type mdxModuleWDMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("muxdmux", 4),
          ("muxdmuxsf", 7))
    )


_MdxModuleWDMType_Type.__name__ = "Integer32"
_MdxModuleWDMType_Object = MibTableColumn
mdxModuleWDMType = _MdxModuleWDMType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 5, 1, 1),
    _MdxModuleWDMType_Type()
)
mdxModuleWDMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdxModuleWDMType.setStatus("current")
_MdxModuleScheme_Type = BandScheme
_MdxModuleScheme_Object = MibTableColumn
mdxModuleScheme = _MdxModuleScheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 5, 1, 2),
    _MdxModuleScheme_Type()
)
mdxModuleScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdxModuleScheme.setStatus("current")


class _MdxModuleChannelRange_Type(Integer32):
    """Custom type mdxModuleChannelRange based on Integer32"""
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
              37)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("channel1to4", 2),
          ("channel5to8", 3),
          ("channel9to12", 4),
          ("channel13to16", 5),
          ("channel17to20", 6),
          ("channel21to24", 7),
          ("channel25to28", 8),
          ("channel29to32", 9),
          ("channel1to4dmx17to20", 10),
          ("channel5to8dmx21to24", 11),
          ("channel9to12dmx25to28", 12),
          ("channel13to16dmx29to32", 13),
          ("channel17to20dmx1to4", 14),
          ("channel21to24dmx5to8", 15),
          ("channel25to28dmx9to12", 16),
          ("channel29to32dmx13to16", 17),
          ("channelE1toE4", 18),
          ("channelE5toE8", 19),
          ("channelE9toE12", 20),
          ("channelE13toE16", 21),
          ("channelE17toE20", 22),
          ("channelE21toE24", 23),
          ("channelE25toE28", 24),
          ("channelE29toE32", 25),
          ("channelE1toE4dmxE17toE20", 26),
          ("channelE5toE8dmxE21toE24", 27),
          ("channelE9toE12dmxE25toE28", 28),
          ("channelE13toE16dmxE29toE32", 29),
          ("channelE17toE20dmxE1toE4", 30),
          ("channelE21toE24dmxE5toE8", 31),
          ("channelE25toE28dmxE9toE12", 32),
          ("channelE29toE32dmxE13toE16", 33),
          ("channelCwdmBandA", 34),
          ("channelCwdmBandB", 35),
          ("channelCwdmBandAdmxBandB", 36),
          ("channelCwdmBandBdmxBandA", 37))
    )


_MdxModuleChannelRange_Type.__name__ = "Integer32"
_MdxModuleChannelRange_Object = MibTableColumn
mdxModuleChannelRange = _MdxModuleChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 5, 1, 3),
    _MdxModuleChannelRange_Type()
)
mdxModuleChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdxModuleChannelRange.setStatus("current")
_MdxModuleUpgradePort_Type = DisplayString
_MdxModuleUpgradePort_Object = MibTableColumn
mdxModuleUpgradePort = _MdxModuleUpgradePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 5, 1, 4),
    _MdxModuleUpgradePort_Type()
)
mdxModuleUpgradePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdxModuleUpgradePort.setStatus("current")
_BandSplitterModuleTable_Object = MibTable
bandSplitterModuleTable = _BandSplitterModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    bandSplitterModuleTable.setStatus("current")
_BandSplitterModuleEntry_Object = MibTableRow
bandSplitterModuleEntry = _BandSplitterModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 6, 1)
)
bandSplitterModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    bandSplitterModuleEntry.setStatus("current")
_BandSplitterModuleScheme_Type = BandScheme
_BandSplitterModuleScheme_Object = MibTableColumn
bandSplitterModuleScheme = _BandSplitterModuleScheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 6, 1, 1),
    _BandSplitterModuleScheme_Type()
)
bandSplitterModuleScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandSplitterModuleScheme.setStatus("current")


class _BandSplitterModuleBandRange_Type(Integer32):
    """Custom type bandSplitterModuleBandRange based on Integer32"""
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
        *(("unknown", 1),
          ("bandLC1and3and5and7", 2),
          ("bandC1to4", 3),
          ("bandL5to8", 4),
          ("bandC1to4dmxL5to8", 5),
          ("bandL5to8dmxC1to4", 6),
          ("bandCwdm1470to1610", 7))
    )


_BandSplitterModuleBandRange_Type.__name__ = "Integer32"
_BandSplitterModuleBandRange_Object = MibTableColumn
bandSplitterModuleBandRange = _BandSplitterModuleBandRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 6, 1, 2),
    _BandSplitterModuleBandRange_Type()
)
bandSplitterModuleBandRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandSplitterModuleBandRange.setStatus("current")


class _BandSplitterModuleType_Type(Integer32):
    """Custom type bandSplitterModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("dualFiber", 2),
          ("singleFiber", 3))
    )


_BandSplitterModuleType_Type.__name__ = "Integer32"
_BandSplitterModuleType_Object = MibTableColumn
bandSplitterModuleType = _BandSplitterModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 6, 1, 3),
    _BandSplitterModuleType_Type()
)
bandSplitterModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandSplitterModuleType.setStatus("current")
_OlmModuleTable_Object = MibTable
olmModuleTable = _OlmModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7)
)
if mibBuilder.loadTexts:
    olmModuleTable.setStatus("current")
_OlmModuleEntry_Object = MibTableRow
olmModuleEntry = _OlmModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7, 1)
)
olmModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    olmModuleEntry.setStatus("current")


class _OlmModuleSwitchOver_Type(Integer32):
    """Custom type olmModuleSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oip", 1),
          ("loss", 2),
          ("none", 3))
    )


_OlmModuleSwitchOver_Type.__name__ = "Integer32"
_OlmModuleSwitchOver_Object = MibTableColumn
olmModuleSwitchOver = _OlmModuleSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7, 1, 1),
    _OlmModuleSwitchOver_Type()
)
olmModuleSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmModuleSwitchOver.setStatus("current")


class _OlmModuleThreshold_Type(Integer32):
    """Custom type olmModuleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OlmModuleThreshold_Type.__name__ = "Integer32"
_OlmModuleThreshold_Object = MibTableColumn
olmModuleThreshold = _OlmModuleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7, 1, 2),
    _OlmModuleThreshold_Type()
)
olmModuleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmModuleThreshold.setStatus("current")


class _OlmModuleHysteresis_Type(Integer32):
    """Custom type olmModuleHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OlmModuleHysteresis_Type.__name__ = "Integer32"
_OlmModuleHysteresis_Object = MibTableColumn
olmModuleHysteresis = _OlmModuleHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7, 1, 3),
    _OlmModuleHysteresis_Type()
)
olmModuleHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmModuleHysteresis.setStatus("current")


class _OlmModuleOTDRWindowStatus_Type(Integer32):
    """Custom type olmModuleOTDRWindowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("normal", 2),
          ("measurementInProgress", 3))
    )


_OlmModuleOTDRWindowStatus_Type.__name__ = "Integer32"
_OlmModuleOTDRWindowStatus_Object = MibTableColumn
olmModuleOTDRWindowStatus = _OlmModuleOTDRWindowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7, 1, 4),
    _OlmModuleOTDRWindowStatus_Type()
)
olmModuleOTDRWindowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmModuleOTDRWindowStatus.setStatus("current")


class _OlmModuleOTDRWindowTime_Type(Integer32):
    """Custom type olmModuleOTDRWindowTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_OlmModuleOTDRWindowTime_Type.__name__ = "Integer32"
_OlmModuleOTDRWindowTime_Object = MibTableColumn
olmModuleOTDRWindowTime = _OlmModuleOTDRWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7, 1, 5),
    _OlmModuleOTDRWindowTime_Type()
)
olmModuleOTDRWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmModuleOTDRWindowTime.setStatus("current")


class _OlmModuleMinThreshold_Type(Integer32):
    """Custom type olmModuleMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OlmModuleMinThreshold_Type.__name__ = "Integer32"
_OlmModuleMinThreshold_Object = MibTableColumn
olmModuleMinThreshold = _OlmModuleMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7, 1, 6),
    _OlmModuleMinThreshold_Type()
)
olmModuleMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmModuleMinThreshold.setStatus("current")


class _OlmModuleMaxThreshold_Type(Integer32):
    """Custom type olmModuleMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OlmModuleMaxThreshold_Type.__name__ = "Integer32"
_OlmModuleMaxThreshold_Object = MibTableColumn
olmModuleMaxThreshold = _OlmModuleMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 7, 1, 7),
    _OlmModuleMaxThreshold_Type()
)
olmModuleMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olmModuleMaxThreshold.setStatus("current")
_SfpTransceiverSubModuleTable_Object = MibTable
sfpTransceiverSubModuleTable = _SfpTransceiverSubModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 8)
)
if mibBuilder.loadTexts:
    sfpTransceiverSubModuleTable.setStatus("current")
_SfpTransceiverSubModuleEntry_Object = MibTableRow
sfpTransceiverSubModuleEntry = _SfpTransceiverSubModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 8, 1)
)
sfpTransceiverSubModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sfpTransceiverSubModuleEntry.setStatus("current")


class _SfpTransceiverApprovedByADVA_Type(Integer32):
    """Custom type sfpTransceiverApprovedByADVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("approved", 1),
          ("notApproved", 2))
    )


_SfpTransceiverApprovedByADVA_Type.__name__ = "Integer32"
_SfpTransceiverApprovedByADVA_Object = MibTableColumn
sfpTransceiverApprovedByADVA = _SfpTransceiverApprovedByADVA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 8, 1, 1),
    _SfpTransceiverApprovedByADVA_Type()
)
sfpTransceiverApprovedByADVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTransceiverApprovedByADVA.setStatus("current")
_SfpTransceiverLinkLength_Type = DisplayString
_SfpTransceiverLinkLength_Object = MibTableColumn
sfpTransceiverLinkLength = _SfpTransceiverLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 8, 1, 2),
    _SfpTransceiverLinkLength_Type()
)
sfpTransceiverLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTransceiverLinkLength.setStatus("current")
_SfpTransceiverChannelName_Type = DisplayString
_SfpTransceiverChannelName_Object = MibTableColumn
sfpTransceiverChannelName = _SfpTransceiverChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 8, 1, 3),
    _SfpTransceiverChannelName_Type()
)
sfpTransceiverChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTransceiverChannelName.setStatus("current")
_SfpTransceiverWaveLengthScheme_Type = BandScheme
_SfpTransceiverWaveLengthScheme_Object = MibTableColumn
sfpTransceiverWaveLengthScheme = _SfpTransceiverWaveLengthScheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 8, 1, 4),
    _SfpTransceiverWaveLengthScheme_Type()
)
sfpTransceiverWaveLengthScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTransceiverWaveLengthScheme.setStatus("current")
_InterleaverModuleTable_Object = MibTable
interleaverModuleTable = _InterleaverModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 9)
)
if mibBuilder.loadTexts:
    interleaverModuleTable.setStatus("current")
_InterleaverModuleEntry_Object = MibTableRow
interleaverModuleEntry = _InterleaverModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 9, 1)
)
interleaverModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    interleaverModuleEntry.setStatus("current")


class _InterleaverModuleType_Type(Integer32):
    """Custom type interleaverModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("dualFiber", 2),
          ("singleFiber", 3))
    )


_InterleaverModuleType_Type.__name__ = "Integer32"
_InterleaverModuleType_Object = MibTableColumn
interleaverModuleType = _InterleaverModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 9, 1, 1),
    _InterleaverModuleType_Type()
)
interleaverModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interleaverModuleType.setStatus("current")
_InterleaverModuleSpacing_Type = DisplayString
_InterleaverModuleSpacing_Object = MibTableColumn
interleaverModuleSpacing = _InterleaverModuleSpacing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 9, 1, 2),
    _InterleaverModuleSpacing_Type()
)
interleaverModuleSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interleaverModuleSpacing.setStatus("current")
_ChannelFilterModuleTable_Object = MibTable
channelFilterModuleTable = _ChannelFilterModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 10)
)
if mibBuilder.loadTexts:
    channelFilterModuleTable.setStatus("current")
_ChannelFilterModuleEntry_Object = MibTableRow
channelFilterModuleEntry = _ChannelFilterModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 10, 1)
)
channelFilterModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    channelFilterModuleEntry.setStatus("current")
_ChannelFilterModuleScheme_Type = BandScheme
_ChannelFilterModuleScheme_Object = MibTableColumn
channelFilterModuleScheme = _ChannelFilterModuleScheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 10, 1, 1),
    _ChannelFilterModuleScheme_Type()
)
channelFilterModuleScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelFilterModuleScheme.setStatus("current")
_ChannelFilterModuleChannelName_Type = DisplayString
_ChannelFilterModuleChannelName_Object = MibTableColumn
channelFilterModuleChannelName = _ChannelFilterModuleChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 4, 2, 10, 1, 2),
    _ChannelFilterModuleChannelName_Type()
)
channelFilterModuleChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelFilterModuleChannelName.setStatus("current")
_Fsp2000Conformance_ObjectIdentity = ObjectIdentity
fsp2000Conformance = _Fsp2000Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 5)
)
_PerformanceMIB_ObjectIdentity = ObjectIdentity
performanceMIB = _PerformanceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6)
)
_PerformanceAdmin_ObjectIdentity = ObjectIdentity
performanceAdmin = _PerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1)
)
_PhysicalPerformanceAdmin_ObjectIdentity = ObjectIdentity
physicalPerformanceAdmin = _PhysicalPerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1)
)
_OlmPPHWthresholdTable_Object = MibTable
olmPPHWthresholdTable = _OlmPPHWthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    olmPPHWthresholdTable.setStatus("current")
_OlmPPHWthresholdEntry_Object = MibTableRow
olmPPHWthresholdEntry = _OlmPPHWthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 1, 1)
)
olmPPHWthresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    olmPPHWthresholdEntry.setStatus("current")


class _OlmPPHWthresholdLowAtt_Type(Integer32):
    """Custom type olmPPHWthresholdLowAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OlmPPHWthresholdLowAtt_Type.__name__ = "Integer32"
_OlmPPHWthresholdLowAtt_Object = MibTableColumn
olmPPHWthresholdLowAtt = _OlmPPHWthresholdLowAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 1, 1, 1),
    _OlmPPHWthresholdLowAtt_Type()
)
olmPPHWthresholdLowAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmPPHWthresholdLowAtt.setStatus("current")


class _OlmPPHWthresholdHighAtt_Type(Integer32):
    """Custom type olmPPHWthresholdHighAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OlmPPHWthresholdHighAtt_Type.__name__ = "Integer32"
_OlmPPHWthresholdHighAtt_Object = MibTableColumn
olmPPHWthresholdHighAtt = _OlmPPHWthresholdHighAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 1, 1, 2),
    _OlmPPHWthresholdHighAtt_Type()
)
olmPPHWthresholdHighAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olmPPHWthresholdHighAtt.setStatus("current")
_OLMPPthresholdTable_Object = MibTable
oLMPPthresholdTable = _OLMPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    oLMPPthresholdTable.setStatus("current")
_OLMPPthresholdEntry_Object = MibTableRow
oLMPPthresholdEntry = _OLMPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 2, 1)
)
oLMPPthresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    oLMPPthresholdEntry.setStatus("current")
_OLMPPthresholdAttGradient_Type = OLMGradientThreshold
_OLMPPthresholdAttGradient_Object = MibTableColumn
oLMPPthresholdAttGradient = _OLMPPthresholdAttGradient_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 2, 1, 1),
    _OLMPPthresholdAttGradient_Type()
)
oLMPPthresholdAttGradient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oLMPPthresholdAttGradient.setStatus("current")
_OLMIfPPthresholdTable_Object = MibTable
oLMIfPPthresholdTable = _OLMIfPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    oLMIfPPthresholdTable.setStatus("current")
_OLMIfPPthresholdEntry_Object = MibTableRow
oLMIfPPthresholdEntry = _OLMIfPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 3, 1)
)
oLMIfPPthresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oLMIfPPthresholdEntry.setStatus("current")


class _OLMIfPPthresholdLowTxAtt_Type(Integer32):
    """Custom type oLMIfPPthresholdLowTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 300),
    )


_OLMIfPPthresholdLowTxAtt_Type.__name__ = "Integer32"
_OLMIfPPthresholdLowTxAtt_Object = MibTableColumn
oLMIfPPthresholdLowTxAtt = _OLMIfPPthresholdLowTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 3, 1, 1),
    _OLMIfPPthresholdLowTxAtt_Type()
)
oLMIfPPthresholdLowTxAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oLMIfPPthresholdLowTxAtt.setStatus("current")


class _OLMIfPPthresholdHighTxAtt_Type(Integer32):
    """Custom type oLMIfPPthresholdHighTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 300),
    )


_OLMIfPPthresholdHighTxAtt_Type.__name__ = "Integer32"
_OLMIfPPthresholdHighTxAtt_Object = MibTableColumn
oLMIfPPthresholdHighTxAtt = _OLMIfPPthresholdHighTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 3, 1, 2),
    _OLMIfPPthresholdHighTxAtt_Type()
)
oLMIfPPthresholdHighTxAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oLMIfPPthresholdHighTxAtt.setStatus("current")


class _OLMIfPPthresholdLowRxAtt_Type(Integer32):
    """Custom type oLMIfPPthresholdLowRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 300),
    )


_OLMIfPPthresholdLowRxAtt_Type.__name__ = "Integer32"
_OLMIfPPthresholdLowRxAtt_Object = MibTableColumn
oLMIfPPthresholdLowRxAtt = _OLMIfPPthresholdLowRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 3, 1, 3),
    _OLMIfPPthresholdLowRxAtt_Type()
)
oLMIfPPthresholdLowRxAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oLMIfPPthresholdLowRxAtt.setStatus("current")


class _OLMIfPPthresholdHighRxAtt_Type(Integer32):
    """Custom type oLMIfPPthresholdHighRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, -255),
        ValueRangeConstraint(0, 300),
    )


_OLMIfPPthresholdHighRxAtt_Type.__name__ = "Integer32"
_OLMIfPPthresholdHighRxAtt_Object = MibTableColumn
oLMIfPPthresholdHighRxAtt = _OLMIfPPthresholdHighRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 3, 1, 4),
    _OLMIfPPthresholdHighRxAtt_Type()
)
oLMIfPPthresholdHighRxAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oLMIfPPthresholdHighRxAtt.setStatus("current")
_EdfaPPthresholdTable_Object = MibTable
edfaPPthresholdTable = _EdfaPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    edfaPPthresholdTable.setStatus("current")
_EdfaPPthresholdEntry_Object = MibTableRow
edfaPPthresholdEntry = _EdfaPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 4, 1)
)
edfaPPthresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    edfaPPthresholdEntry.setStatus("current")


class _EdfaPPthresholdHighPumpCurrent_Type(Integer32):
    """Custom type edfaPPthresholdHighPumpCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(0, 1024),
    )


_EdfaPPthresholdHighPumpCurrent_Type.__name__ = "Integer32"
_EdfaPPthresholdHighPumpCurrent_Object = MibTableColumn
edfaPPthresholdHighPumpCurrent = _EdfaPPthresholdHighPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 4, 1, 1),
    _EdfaPPthresholdHighPumpCurrent_Type()
)
edfaPPthresholdHighPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPPthresholdHighPumpCurrent.setStatus("current")


class _EdfaPPthresholdLowOIP_Type(Integer32):
    """Custom type edfaPPthresholdLowOIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65535, -65535),
        ValueRangeConstraint(-400, -50),
    )


_EdfaPPthresholdLowOIP_Type.__name__ = "Integer32"
_EdfaPPthresholdLowOIP_Object = MibTableColumn
edfaPPthresholdLowOIP = _EdfaPPthresholdLowOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 4, 1, 2),
    _EdfaPPthresholdLowOIP_Type()
)
edfaPPthresholdLowOIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPPthresholdLowOIP.setStatus("current")
_EdfaPPthresholdHighOIP_Type = Integer32
_EdfaPPthresholdHighOIP_Object = MibTableColumn
edfaPPthresholdHighOIP = _EdfaPPthresholdHighOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 4, 1, 3),
    _EdfaPPthresholdHighOIP_Type()
)
edfaPPthresholdHighOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPPthresholdHighOIP.setStatus("current")
_EdfaPPthresholdHighTempProt_Type = Integer32
_EdfaPPthresholdHighTempProt_Object = MibTableColumn
edfaPPthresholdHighTempProt = _EdfaPPthresholdHighTempProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 4, 1, 4),
    _EdfaPPthresholdHighTempProt_Type()
)
edfaPPthresholdHighTempProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPPthresholdHighTempProt.setStatus("current")
_IfTTPPthresholdTable_Object = MibTable
ifTTPPthresholdTable = _IfTTPPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ifTTPPthresholdTable.setStatus("current")
_IfTTPPthresholdEntry_Object = MibTableRow
ifTTPPthresholdEntry = _IfTTPPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1)
)
ifTTPPthresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifTTPPthresholdEntry.setStatus("current")
_IfTTPPthresholdLowLaserCurrent_Type = Integer32
_IfTTPPthresholdLowLaserCurrent_Object = MibTableColumn
ifTTPPthresholdLowLaserCurrent = _IfTTPPthresholdLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1, 1),
    _IfTTPPthresholdLowLaserCurrent_Type()
)
ifTTPPthresholdLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPPthresholdLowLaserCurrent.setStatus("current")
_IfTTPPthresholdHighLaserCurrent_Type = Integer32
_IfTTPPthresholdHighLaserCurrent_Object = MibTableColumn
ifTTPPthresholdHighLaserCurrent = _IfTTPPthresholdHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1, 2),
    _IfTTPPthresholdHighLaserCurrent_Type()
)
ifTTPPthresholdHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPPthresholdHighLaserCurrent.setStatus("current")
_IfTTPPthresholdLowOIP_Type = Integer32
_IfTTPPthresholdLowOIP_Object = MibTableColumn
ifTTPPthresholdLowOIP = _IfTTPPthresholdLowOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1, 3),
    _IfTTPPthresholdLowOIP_Type()
)
ifTTPPthresholdLowOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPPthresholdLowOIP.setStatus("current")
_IfTTPPthresholdHighOIP_Type = Integer32
_IfTTPPthresholdHighOIP_Object = MibTableColumn
ifTTPPthresholdHighOIP = _IfTTPPthresholdHighOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1, 4),
    _IfTTPPthresholdHighOIP_Type()
)
ifTTPPthresholdHighOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPPthresholdHighOIP.setStatus("current")
_IfTTPPthresholdLowOOP_Type = Integer32
_IfTTPPthresholdLowOOP_Object = MibTableColumn
ifTTPPthresholdLowOOP = _IfTTPPthresholdLowOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1, 5),
    _IfTTPPthresholdLowOOP_Type()
)
ifTTPPthresholdLowOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPPthresholdLowOOP.setStatus("current")
_IfTTPPthresholdHighOOP_Type = Integer32
_IfTTPPthresholdHighOOP_Object = MibTableColumn
ifTTPPthresholdHighOOP = _IfTTPPthresholdHighOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1, 6),
    _IfTTPPthresholdHighOOP_Type()
)
ifTTPPthresholdHighOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPPthresholdHighOOP.setStatus("current")
_IfTTPPthresholdLowLaserTemp_Type = Integer32
_IfTTPPthresholdLowLaserTemp_Object = MibTableColumn
ifTTPPthresholdLowLaserTemp = _IfTTPPthresholdLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1, 7),
    _IfTTPPthresholdLowLaserTemp_Type()
)
ifTTPPthresholdLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPPthresholdLowLaserTemp.setStatus("current")
_IfTTPPthresholdHighLaserTemp_Type = Integer32
_IfTTPPthresholdHighLaserTemp_Object = MibTableColumn
ifTTPPthresholdHighLaserTemp = _IfTTPPthresholdHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 5, 1, 8),
    _IfTTPPthresholdHighLaserTemp_Type()
)
ifTTPPthresholdHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPPthresholdHighLaserTemp.setStatus("current")
_ModulePPthresholdTable_Object = MibTable
modulePPthresholdTable = _ModulePPthresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 6)
)
if mibBuilder.loadTexts:
    modulePPthresholdTable.setStatus("current")
_ModulePPthresholdEntry_Object = MibTableRow
modulePPthresholdEntry = _ModulePPthresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 6, 1)
)
modulePPthresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    modulePPthresholdEntry.setStatus("current")
_ModulePPthresholdLowVolt_Type = Integer32
_ModulePPthresholdLowVolt_Object = MibTableColumn
modulePPthresholdLowVolt = _ModulePPthresholdLowVolt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 6, 1, 1),
    _ModulePPthresholdLowVolt_Type()
)
modulePPthresholdLowVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePPthresholdLowVolt.setStatus("current")
_ModulePPthresholdHighVolt_Type = Integer32
_ModulePPthresholdHighVolt_Object = MibTableColumn
modulePPthresholdHighVolt = _ModulePPthresholdHighVolt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 6, 1, 2),
    _ModulePPthresholdHighVolt_Type()
)
modulePPthresholdHighVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePPthresholdHighVolt.setStatus("current")
_ModulePPthresholdHighTemp_Type = Integer32
_ModulePPthresholdHighTemp_Object = MibTableColumn
modulePPthresholdHighTemp = _ModulePPthresholdHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 6, 1, 3),
    _ModulePPthresholdHighTemp_Type()
)
modulePPthresholdHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePPthresholdHighTemp.setStatus("current")
_ModulePPthresholdLowTemp_Type = Integer32
_ModulePPthresholdLowTemp_Object = MibTableColumn
modulePPthresholdLowTemp = _ModulePPthresholdLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 1, 6, 1, 4),
    _ModulePPthresholdLowTemp_Type()
)
modulePPthresholdLowTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePPthresholdLowTemp.setStatus("current")
_GeneralPerformanceAdmin_ObjectIdentity = ObjectIdentity
generalPerformanceAdmin = _GeneralPerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2)
)
_IfPerformanceStatusTable_Object = MibTable
ifPerformanceStatusTable = _IfPerformanceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ifPerformanceStatusTable.setStatus("current")
_IfPerformanceStatusEntry_Object = MibTableRow
ifPerformanceStatusEntry = _IfPerformanceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 1, 1)
)
ifPerformanceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifPerformanceStatusType"),
)
if mibBuilder.loadTexts:
    ifPerformanceStatusEntry.setStatus("current")


class _IfPerformanceStatusType_Type(Integer32):
    """Custom type ifPerformanceStatusType based on Integer32"""
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
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109)
        )
    )
    namedValues = NamedValues(
        *(("oLMPLP15minIntTable", 1),
          ("oLMPLP24hIntTable", 2),
          ("oLMPLP1weekIntTable", 3),
          ("edfaPLP15minIntTable", 4),
          ("edfaPLP24hIntTable", 5),
          ("edfaPLP1weekIntTable", 6),
          ("ifPLP15minIntTable", 7),
          ("ifPLP24hIntTable", 8),
          ("ifPLP1weekIntTable", 9),
          ("oLMPLA15minIntTable", 101),
          ("oLMPLA24hIntTable", 102),
          ("oLMPLA1weekIntTable", 103),
          ("edfaPLA15minIntTable", 104),
          ("edfaPLA24hIntTable", 105),
          ("edfaPLA1weekIntTable", 106),
          ("ifPLA15minIntTable", 107),
          ("ifPLA24hIntTable", 108),
          ("ifPLA1weekIntTable", 109))
    )


_IfPerformanceStatusType_Type.__name__ = "Integer32"
_IfPerformanceStatusType_Object = MibTableColumn
ifPerformanceStatusType = _IfPerformanceStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 1, 1, 1),
    _IfPerformanceStatusType_Type()
)
ifPerformanceStatusType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifPerformanceStatusType.setStatus("current")
_IfPerformanceStatusAvail_Type = AvailState
_IfPerformanceStatusAvail_Object = MibTableColumn
ifPerformanceStatusAvail = _IfPerformanceStatusAvail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 1, 1, 2),
    _IfPerformanceStatusAvail_Type()
)
ifPerformanceStatusAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerformanceStatusAvail.setStatus("current")
_IfPerformanceStatusLength_Type = Integer32
_IfPerformanceStatusLength_Object = MibTableColumn
ifPerformanceStatusLength = _IfPerformanceStatusLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 1, 1, 3),
    _IfPerformanceStatusLength_Type()
)
ifPerformanceStatusLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerformanceStatusLength.setStatus("current")
_ModulePerformanceStatusTable_Object = MibTable
modulePerformanceStatusTable = _ModulePerformanceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    modulePerformanceStatusTable.setStatus("current")
_ModulePerformanceStatusEntry_Object = MibTableRow
modulePerformanceStatusEntry = _ModulePerformanceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 2, 1)
)
modulePerformanceStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "modulePerformanceStatusType"),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("modulePLP15minIntTable", 1),
          ("modulePLP24hIntTable", 2),
          ("modulePLP1weekIntTable", 3))
    )


_ModulePerformanceStatusType_Type.__name__ = "Integer32"
_ModulePerformanceStatusType_Object = MibTableColumn
modulePerformanceStatusType = _ModulePerformanceStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 2, 1, 1),
    _ModulePerformanceStatusType_Type()
)
modulePerformanceStatusType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modulePerformanceStatusType.setStatus("current")
_ModulePerformanceStatusAvail_Type = AvailState
_ModulePerformanceStatusAvail_Object = MibTableColumn
modulePerformanceStatusAvail = _ModulePerformanceStatusAvail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 2, 1, 2),
    _ModulePerformanceStatusAvail_Type()
)
modulePerformanceStatusAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePerformanceStatusAvail.setStatus("current")
_ModulePerformanceStatusLength_Type = Integer32
_ModulePerformanceStatusLength_Object = MibTableColumn
modulePerformanceStatusLength = _ModulePerformanceStatusLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 1, 2, 2, 1, 3),
    _ModulePerformanceStatusLength_Type()
)
modulePerformanceStatusLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePerformanceStatusLength.setStatus("current")
_PerformanceMonitoring_ObjectIdentity = ObjectIdentity
performanceMonitoring = _PerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2)
)
_PhysicalLayerPerformanceMon_ObjectIdentity = ObjectIdentity
physicalLayerPerformanceMon = _PhysicalLayerPerformanceMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2)
)
_OLMPLP15minIntTable_Object = MibTable
oLMPLP15minIntTable = _OLMPLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oLMPLP15minIntTable.setStatus("current")
_OLMPLP15minIntEntry_Object = MibTableRow
oLMPLP15minIntEntry = _OLMPLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1)
)
oLMPLP15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "oLMPLP15minIntIndex"),
)
if mibBuilder.loadTexts:
    oLMPLP15minIntEntry.setStatus("current")


class _OLMPLP15minIntIndex_Type(Integer32):
    """Custom type oLMPLP15minIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_OLMPLP15minIntIndex_Type.__name__ = "Integer32"
_OLMPLP15minIntIndex_Object = MibTableColumn
oLMPLP15minIntIndex = _OLMPLP15minIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 1),
    _OLMPLP15minIntIndex_Type()
)
oLMPLP15minIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oLMPLP15minIntIndex.setStatus("current")


class _OLMPLP15minIntAverageRxAtt_Type(Integer32):
    """Custom type oLMPLP15minIntAverageRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP15minIntAverageRxAtt_Type.__name__ = "Integer32"
_OLMPLP15minIntAverageRxAtt_Object = MibTableColumn
oLMPLP15minIntAverageRxAtt = _OLMPLP15minIntAverageRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 2),
    _OLMPLP15minIntAverageRxAtt_Type()
)
oLMPLP15minIntAverageRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP15minIntAverageRxAtt.setStatus("current")


class _OLMPLP15minIntMinRxAtt_Type(Integer32):
    """Custom type oLMPLP15minIntMinRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP15minIntMinRxAtt_Type.__name__ = "Integer32"
_OLMPLP15minIntMinRxAtt_Object = MibTableColumn
oLMPLP15minIntMinRxAtt = _OLMPLP15minIntMinRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 3),
    _OLMPLP15minIntMinRxAtt_Type()
)
oLMPLP15minIntMinRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP15minIntMinRxAtt.setStatus("current")


class _OLMPLP15minIntMaxRxAtt_Type(Integer32):
    """Custom type oLMPLP15minIntMaxRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP15minIntMaxRxAtt_Type.__name__ = "Integer32"
_OLMPLP15minIntMaxRxAtt_Object = MibTableColumn
oLMPLP15minIntMaxRxAtt = _OLMPLP15minIntMaxRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 4),
    _OLMPLP15minIntMaxRxAtt_Type()
)
oLMPLP15minIntMaxRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP15minIntMaxRxAtt.setStatus("current")


class _OLMPLP15minIntAverageTxAtt_Type(Integer32):
    """Custom type oLMPLP15minIntAverageTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP15minIntAverageTxAtt_Type.__name__ = "Integer32"
_OLMPLP15minIntAverageTxAtt_Object = MibTableColumn
oLMPLP15minIntAverageTxAtt = _OLMPLP15minIntAverageTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 5),
    _OLMPLP15minIntAverageTxAtt_Type()
)
oLMPLP15minIntAverageTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP15minIntAverageTxAtt.setStatus("current")


class _OLMPLP15minIntMinTxAtt_Type(Integer32):
    """Custom type oLMPLP15minIntMinTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP15minIntMinTxAtt_Type.__name__ = "Integer32"
_OLMPLP15minIntMinTxAtt_Object = MibTableColumn
oLMPLP15minIntMinTxAtt = _OLMPLP15minIntMinTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 6),
    _OLMPLP15minIntMinTxAtt_Type()
)
oLMPLP15minIntMinTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP15minIntMinTxAtt.setStatus("current")


class _OLMPLP15minIntMaxTxAtt_Type(Integer32):
    """Custom type oLMPLP15minIntMaxTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP15minIntMaxTxAtt_Type.__name__ = "Integer32"
_OLMPLP15minIntMaxTxAtt_Object = MibTableColumn
oLMPLP15minIntMaxTxAtt = _OLMPLP15minIntMaxTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 7),
    _OLMPLP15minIntMaxTxAtt_Type()
)
oLMPLP15minIntMaxTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP15minIntMaxTxAtt.setStatus("current")
_OLMPLP15minIntValidData_Type = TruthValue
_OLMPLP15minIntValidData_Object = MibTableColumn
oLMPLP15minIntValidData = _OLMPLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 8),
    _OLMPLP15minIntValidData_Type()
)
oLMPLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP15minIntValidData.setStatus("current")
_OLMPLP15minIntTimeStamp_Type = DateAndTime
_OLMPLP15minIntTimeStamp_Object = MibTableColumn
oLMPLP15minIntTimeStamp = _OLMPLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 1, 1, 9),
    _OLMPLP15minIntTimeStamp_Type()
)
oLMPLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP15minIntTimeStamp.setStatus("current")
_OLMPLP24hIntTable_Object = MibTable
oLMPLP24hIntTable = _OLMPLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    oLMPLP24hIntTable.setStatus("current")
_OLMPLP24hIntEntry_Object = MibTableRow
oLMPLP24hIntEntry = _OLMPLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1)
)
oLMPLP24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "oLMPLP24hIntIndex"),
)
if mibBuilder.loadTexts:
    oLMPLP24hIntEntry.setStatus("current")


class _OLMPLP24hIntIndex_Type(Integer32):
    """Custom type oLMPLP24hIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_OLMPLP24hIntIndex_Type.__name__ = "Integer32"
_OLMPLP24hIntIndex_Object = MibTableColumn
oLMPLP24hIntIndex = _OLMPLP24hIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 1),
    _OLMPLP24hIntIndex_Type()
)
oLMPLP24hIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oLMPLP24hIntIndex.setStatus("current")


class _OLMPLP24hIntAverageRxAtt_Type(Integer32):
    """Custom type oLMPLP24hIntAverageRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP24hIntAverageRxAtt_Type.__name__ = "Integer32"
_OLMPLP24hIntAverageRxAtt_Object = MibTableColumn
oLMPLP24hIntAverageRxAtt = _OLMPLP24hIntAverageRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 2),
    _OLMPLP24hIntAverageRxAtt_Type()
)
oLMPLP24hIntAverageRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP24hIntAverageRxAtt.setStatus("current")


class _OLMPLP24hIntMinRxAtt_Type(Integer32):
    """Custom type oLMPLP24hIntMinRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP24hIntMinRxAtt_Type.__name__ = "Integer32"
_OLMPLP24hIntMinRxAtt_Object = MibTableColumn
oLMPLP24hIntMinRxAtt = _OLMPLP24hIntMinRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 3),
    _OLMPLP24hIntMinRxAtt_Type()
)
oLMPLP24hIntMinRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP24hIntMinRxAtt.setStatus("current")


class _OLMPLP24hIntMaxRxAtt_Type(Integer32):
    """Custom type oLMPLP24hIntMaxRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP24hIntMaxRxAtt_Type.__name__ = "Integer32"
_OLMPLP24hIntMaxRxAtt_Object = MibTableColumn
oLMPLP24hIntMaxRxAtt = _OLMPLP24hIntMaxRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 4),
    _OLMPLP24hIntMaxRxAtt_Type()
)
oLMPLP24hIntMaxRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP24hIntMaxRxAtt.setStatus("current")


class _OLMPLP24hIntAverageTxAtt_Type(Integer32):
    """Custom type oLMPLP24hIntAverageTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP24hIntAverageTxAtt_Type.__name__ = "Integer32"
_OLMPLP24hIntAverageTxAtt_Object = MibTableColumn
oLMPLP24hIntAverageTxAtt = _OLMPLP24hIntAverageTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 5),
    _OLMPLP24hIntAverageTxAtt_Type()
)
oLMPLP24hIntAverageTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP24hIntAverageTxAtt.setStatus("current")


class _OLMPLP24hIntMinTxAtt_Type(Integer32):
    """Custom type oLMPLP24hIntMinTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP24hIntMinTxAtt_Type.__name__ = "Integer32"
_OLMPLP24hIntMinTxAtt_Object = MibTableColumn
oLMPLP24hIntMinTxAtt = _OLMPLP24hIntMinTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 6),
    _OLMPLP24hIntMinTxAtt_Type()
)
oLMPLP24hIntMinTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP24hIntMinTxAtt.setStatus("current")


class _OLMPLP24hIntMaxTxAtt_Type(Integer32):
    """Custom type oLMPLP24hIntMaxTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP24hIntMaxTxAtt_Type.__name__ = "Integer32"
_OLMPLP24hIntMaxTxAtt_Object = MibTableColumn
oLMPLP24hIntMaxTxAtt = _OLMPLP24hIntMaxTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 7),
    _OLMPLP24hIntMaxTxAtt_Type()
)
oLMPLP24hIntMaxTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP24hIntMaxTxAtt.setStatus("current")
_OLMPLP24hIntValidData_Type = TruthValue
_OLMPLP24hIntValidData_Object = MibTableColumn
oLMPLP24hIntValidData = _OLMPLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 8),
    _OLMPLP24hIntValidData_Type()
)
oLMPLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP24hIntValidData.setStatus("current")
_OLMPLP24hIntTimeStamp_Type = DateAndTime
_OLMPLP24hIntTimeStamp_Object = MibTableColumn
oLMPLP24hIntTimeStamp = _OLMPLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 2, 1, 9),
    _OLMPLP24hIntTimeStamp_Type()
)
oLMPLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP24hIntTimeStamp.setStatus("current")
_OLMPLP1weekIntTable_Object = MibTable
oLMPLP1weekIntTable = _OLMPLP1weekIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3)
)
if mibBuilder.loadTexts:
    oLMPLP1weekIntTable.setStatus("current")
_OLMPLP1weekIntEntry_Object = MibTableRow
oLMPLP1weekIntEntry = _OLMPLP1weekIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1)
)
oLMPLP1weekIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "oLMPLP1weekIntIndex"),
)
if mibBuilder.loadTexts:
    oLMPLP1weekIntEntry.setStatus("current")


class _OLMPLP1weekIntIndex_Type(Integer32):
    """Custom type oLMPLP1weekIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_OLMPLP1weekIntIndex_Type.__name__ = "Integer32"
_OLMPLP1weekIntIndex_Object = MibTableColumn
oLMPLP1weekIntIndex = _OLMPLP1weekIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 1),
    _OLMPLP1weekIntIndex_Type()
)
oLMPLP1weekIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oLMPLP1weekIntIndex.setStatus("current")


class _OLMPLP1weekIntAverageRxAtt_Type(Integer32):
    """Custom type oLMPLP1weekIntAverageRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP1weekIntAverageRxAtt_Type.__name__ = "Integer32"
_OLMPLP1weekIntAverageRxAtt_Object = MibTableColumn
oLMPLP1weekIntAverageRxAtt = _OLMPLP1weekIntAverageRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 2),
    _OLMPLP1weekIntAverageRxAtt_Type()
)
oLMPLP1weekIntAverageRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP1weekIntAverageRxAtt.setStatus("current")


class _OLMPLP1weekIntMinRxAtt_Type(Integer32):
    """Custom type oLMPLP1weekIntMinRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP1weekIntMinRxAtt_Type.__name__ = "Integer32"
_OLMPLP1weekIntMinRxAtt_Object = MibTableColumn
oLMPLP1weekIntMinRxAtt = _OLMPLP1weekIntMinRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 3),
    _OLMPLP1weekIntMinRxAtt_Type()
)
oLMPLP1weekIntMinRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP1weekIntMinRxAtt.setStatus("current")


class _OLMPLP1weekIntMaxRxAtt_Type(Integer32):
    """Custom type oLMPLP1weekIntMaxRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP1weekIntMaxRxAtt_Type.__name__ = "Integer32"
_OLMPLP1weekIntMaxRxAtt_Object = MibTableColumn
oLMPLP1weekIntMaxRxAtt = _OLMPLP1weekIntMaxRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 4),
    _OLMPLP1weekIntMaxRxAtt_Type()
)
oLMPLP1weekIntMaxRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP1weekIntMaxRxAtt.setStatus("current")


class _OLMPLP1weekIntAverageTxAtt_Type(Integer32):
    """Custom type oLMPLP1weekIntAverageTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP1weekIntAverageTxAtt_Type.__name__ = "Integer32"
_OLMPLP1weekIntAverageTxAtt_Object = MibTableColumn
oLMPLP1weekIntAverageTxAtt = _OLMPLP1weekIntAverageTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 5),
    _OLMPLP1weekIntAverageTxAtt_Type()
)
oLMPLP1weekIntAverageTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP1weekIntAverageTxAtt.setStatus("current")


class _OLMPLP1weekIntMinTxAtt_Type(Integer32):
    """Custom type oLMPLP1weekIntMinTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP1weekIntMinTxAtt_Type.__name__ = "Integer32"
_OLMPLP1weekIntMinTxAtt_Object = MibTableColumn
oLMPLP1weekIntMinTxAtt = _OLMPLP1weekIntMinTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 6),
    _OLMPLP1weekIntMinTxAtt_Type()
)
oLMPLP1weekIntMinTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP1weekIntMinTxAtt.setStatus("current")


class _OLMPLP1weekIntMaxTxAtt_Type(Integer32):
    """Custom type oLMPLP1weekIntMaxTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLP1weekIntMaxTxAtt_Type.__name__ = "Integer32"
_OLMPLP1weekIntMaxTxAtt_Object = MibTableColumn
oLMPLP1weekIntMaxTxAtt = _OLMPLP1weekIntMaxTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 7),
    _OLMPLP1weekIntMaxTxAtt_Type()
)
oLMPLP1weekIntMaxTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP1weekIntMaxTxAtt.setStatus("current")
_OLMPLP1weekIntValidData_Type = TruthValue
_OLMPLP1weekIntValidData_Object = MibTableColumn
oLMPLP1weekIntValidData = _OLMPLP1weekIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 8),
    _OLMPLP1weekIntValidData_Type()
)
oLMPLP1weekIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP1weekIntValidData.setStatus("current")
_OLMPLP1weekIntTimeStamp_Type = DateAndTime
_OLMPLP1weekIntTimeStamp_Object = MibTableColumn
oLMPLP1weekIntTimeStamp = _OLMPLP1weekIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 3, 1, 9),
    _OLMPLP1weekIntTimeStamp_Type()
)
oLMPLP1weekIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLP1weekIntTimeStamp.setStatus("current")
_OLMPLPcurrentTable_Object = MibTable
oLMPLPcurrentTable = _OLMPLPcurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4)
)
if mibBuilder.loadTexts:
    oLMPLPcurrentTable.setStatus("current")
_OLMPLPcurrentEntry_Object = MibTableRow
oLMPLPcurrentEntry = _OLMPLPcurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1)
)
oLMPLPcurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "oLMPLPcurrentIndex"),
)
if mibBuilder.loadTexts:
    oLMPLPcurrentEntry.setStatus("current")


class _OLMPLPcurrentIndex_Type(Integer32):
    """Custom type oLMPLPcurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_OLMPLPcurrentIndex_Type.__name__ = "Integer32"
_OLMPLPcurrentIndex_Object = MibTableColumn
oLMPLPcurrentIndex = _OLMPLPcurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 1),
    _OLMPLPcurrentIndex_Type()
)
oLMPLPcurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oLMPLPcurrentIndex.setStatus("current")


class _OLMPLPcurrentAverageRxAtt_Type(Integer32):
    """Custom type oLMPLPcurrentAverageRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLPcurrentAverageRxAtt_Type.__name__ = "Integer32"
_OLMPLPcurrentAverageRxAtt_Object = MibTableColumn
oLMPLPcurrentAverageRxAtt = _OLMPLPcurrentAverageRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 2),
    _OLMPLPcurrentAverageRxAtt_Type()
)
oLMPLPcurrentAverageRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLPcurrentAverageRxAtt.setStatus("current")


class _OLMPLPcurrentMinRxAtt_Type(Integer32):
    """Custom type oLMPLPcurrentMinRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLPcurrentMinRxAtt_Type.__name__ = "Integer32"
_OLMPLPcurrentMinRxAtt_Object = MibTableColumn
oLMPLPcurrentMinRxAtt = _OLMPLPcurrentMinRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 3),
    _OLMPLPcurrentMinRxAtt_Type()
)
oLMPLPcurrentMinRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLPcurrentMinRxAtt.setStatus("current")


class _OLMPLPcurrentMaxRxAtt_Type(Integer32):
    """Custom type oLMPLPcurrentMaxRxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLPcurrentMaxRxAtt_Type.__name__ = "Integer32"
_OLMPLPcurrentMaxRxAtt_Object = MibTableColumn
oLMPLPcurrentMaxRxAtt = _OLMPLPcurrentMaxRxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 4),
    _OLMPLPcurrentMaxRxAtt_Type()
)
oLMPLPcurrentMaxRxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLPcurrentMaxRxAtt.setStatus("current")


class _OLMPLPcurrentAverageTxAtt_Type(Integer32):
    """Custom type oLMPLPcurrentAverageTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLPcurrentAverageTxAtt_Type.__name__ = "Integer32"
_OLMPLPcurrentAverageTxAtt_Object = MibTableColumn
oLMPLPcurrentAverageTxAtt = _OLMPLPcurrentAverageTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 5),
    _OLMPLPcurrentAverageTxAtt_Type()
)
oLMPLPcurrentAverageTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLPcurrentAverageTxAtt.setStatus("current")


class _OLMPLPcurrentMinTxAtt_Type(Integer32):
    """Custom type oLMPLPcurrentMinTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLPcurrentMinTxAtt_Type.__name__ = "Integer32"
_OLMPLPcurrentMinTxAtt_Object = MibTableColumn
oLMPLPcurrentMinTxAtt = _OLMPLPcurrentMinTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 6),
    _OLMPLPcurrentMinTxAtt_Type()
)
oLMPLPcurrentMinTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLPcurrentMinTxAtt.setStatus("current")


class _OLMPLPcurrentMaxTxAtt_Type(Integer32):
    """Custom type oLMPLPcurrentMaxTxAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OLMPLPcurrentMaxTxAtt_Type.__name__ = "Integer32"
_OLMPLPcurrentMaxTxAtt_Object = MibTableColumn
oLMPLPcurrentMaxTxAtt = _OLMPLPcurrentMaxTxAtt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 7),
    _OLMPLPcurrentMaxTxAtt_Type()
)
oLMPLPcurrentMaxTxAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLPcurrentMaxTxAtt.setStatus("current")
_OLMPLPcurrentValidData_Type = TruthValue
_OLMPLPcurrentValidData_Object = MibTableColumn
oLMPLPcurrentValidData = _OLMPLPcurrentValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 8),
    _OLMPLPcurrentValidData_Type()
)
oLMPLPcurrentValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLPcurrentValidData.setStatus("current")
_OLMPLPcurrentElapsedTime_Type = Integer32
_OLMPLPcurrentElapsedTime_Object = MibTableColumn
oLMPLPcurrentElapsedTime = _OLMPLPcurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 4, 1, 9),
    _OLMPLPcurrentElapsedTime_Type()
)
oLMPLPcurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLPcurrentElapsedTime.setStatus("current")
_EdfaPLP15minIntTable_Object = MibTable
edfaPLP15minIntTable = _EdfaPLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5)
)
if mibBuilder.loadTexts:
    edfaPLP15minIntTable.setStatus("current")
_EdfaPLP15minIntEntry_Object = MibTableRow
edfaPLP15minIntEntry = _EdfaPLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1)
)
edfaPLP15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "edfaPLP15minIntIndex"),
)
if mibBuilder.loadTexts:
    edfaPLP15minIntEntry.setStatus("current")


class _EdfaPLP15minIntIndex_Type(Integer32):
    """Custom type edfaPLP15minIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EdfaPLP15minIntIndex_Type.__name__ = "Integer32"
_EdfaPLP15minIntIndex_Object = MibTableColumn
edfaPLP15minIntIndex = _EdfaPLP15minIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 1),
    _EdfaPLP15minIntIndex_Type()
)
edfaPLP15minIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    edfaPLP15minIntIndex.setStatus("current")
_EdfaPLP15minIntValidData_Type = TruthValue
_EdfaPLP15minIntValidData_Object = MibTableColumn
edfaPLP15minIntValidData = _EdfaPLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 2),
    _EdfaPLP15minIntValidData_Type()
)
edfaPLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntValidData.setStatus("current")
_EdfaPLP15minIntTimeStamp_Type = DateAndTime
_EdfaPLP15minIntTimeStamp_Object = MibTableColumn
edfaPLP15minIntTimeStamp = _EdfaPLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 3),
    _EdfaPLP15minIntTimeStamp_Type()
)
edfaPLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntTimeStamp.setStatus("current")
_EdfaPLP15minIntAveragePumpCurr_Type = Integer32
_EdfaPLP15minIntAveragePumpCurr_Object = MibTableColumn
edfaPLP15minIntAveragePumpCurr = _EdfaPLP15minIntAveragePumpCurr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 4),
    _EdfaPLP15minIntAveragePumpCurr_Type()
)
edfaPLP15minIntAveragePumpCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAveragePumpCurr.setStatus("current")
_EdfaPLP15minIntMinPumpCurrent_Type = Integer32
_EdfaPLP15minIntMinPumpCurrent_Object = MibTableColumn
edfaPLP15minIntMinPumpCurrent = _EdfaPLP15minIntMinPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 5),
    _EdfaPLP15minIntMinPumpCurrent_Type()
)
edfaPLP15minIntMinPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinPumpCurrent.setStatus("current")
_EdfaPLP15minIntMaxPumpCurrent_Type = Integer32
_EdfaPLP15minIntMaxPumpCurrent_Object = MibTableColumn
edfaPLP15minIntMaxPumpCurrent = _EdfaPLP15minIntMaxPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 6),
    _EdfaPLP15minIntMaxPumpCurrent_Type()
)
edfaPLP15minIntMaxPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxPumpCurrent.setStatus("current")
_EdfaPLP15minIntAverageOIP_Type = Integer32
_EdfaPLP15minIntAverageOIP_Object = MibTableColumn
edfaPLP15minIntAverageOIP = _EdfaPLP15minIntAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 7),
    _EdfaPLP15minIntAverageOIP_Type()
)
edfaPLP15minIntAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntAverageOIP.setStatus("current")
_EdfaPLP15minIntMinOIP_Type = Integer32
_EdfaPLP15minIntMinOIP_Object = MibTableColumn
edfaPLP15minIntMinOIP = _EdfaPLP15minIntMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 8),
    _EdfaPLP15minIntMinOIP_Type()
)
edfaPLP15minIntMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMinOIP.setStatus("current")
_EdfaPLP15minIntMaxOIP_Type = Integer32
_EdfaPLP15minIntMaxOIP_Object = MibTableColumn
edfaPLP15minIntMaxOIP = _EdfaPLP15minIntMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 5, 1, 9),
    _EdfaPLP15minIntMaxOIP_Type()
)
edfaPLP15minIntMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP15minIntMaxOIP.setStatus("current")
_EdfaPLP24hIntTable_Object = MibTable
edfaPLP24hIntTable = _EdfaPLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6)
)
if mibBuilder.loadTexts:
    edfaPLP24hIntTable.setStatus("current")
_EdfaPLP24hIntEntry_Object = MibTableRow
edfaPLP24hIntEntry = _EdfaPLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1)
)
edfaPLP24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "edfaPLP24hIntIndex"),
)
if mibBuilder.loadTexts:
    edfaPLP24hIntEntry.setStatus("current")


class _EdfaPLP24hIntIndex_Type(Integer32):
    """Custom type edfaPLP24hIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_EdfaPLP24hIntIndex_Type.__name__ = "Integer32"
_EdfaPLP24hIntIndex_Object = MibTableColumn
edfaPLP24hIntIndex = _EdfaPLP24hIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 1),
    _EdfaPLP24hIntIndex_Type()
)
edfaPLP24hIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    edfaPLP24hIntIndex.setStatus("current")
_EdfaPLP24hIntValidData_Type = TruthValue
_EdfaPLP24hIntValidData_Object = MibTableColumn
edfaPLP24hIntValidData = _EdfaPLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 2),
    _EdfaPLP24hIntValidData_Type()
)
edfaPLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntValidData.setStatus("current")
_EdfaPLP24hIntTimeStamp_Type = DateAndTime
_EdfaPLP24hIntTimeStamp_Object = MibTableColumn
edfaPLP24hIntTimeStamp = _EdfaPLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 3),
    _EdfaPLP24hIntTimeStamp_Type()
)
edfaPLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntTimeStamp.setStatus("current")
_EdfaPLP24hIntAveragePumpCurrent_Type = Integer32
_EdfaPLP24hIntAveragePumpCurrent_Object = MibTableColumn
edfaPLP24hIntAveragePumpCurrent = _EdfaPLP24hIntAveragePumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 4),
    _EdfaPLP24hIntAveragePumpCurrent_Type()
)
edfaPLP24hIntAveragePumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAveragePumpCurrent.setStatus("current")
_EdfaPLP24hIntMinPumpCurrent_Type = Integer32
_EdfaPLP24hIntMinPumpCurrent_Object = MibTableColumn
edfaPLP24hIntMinPumpCurrent = _EdfaPLP24hIntMinPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 5),
    _EdfaPLP24hIntMinPumpCurrent_Type()
)
edfaPLP24hIntMinPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinPumpCurrent.setStatus("current")
_EdfaPLP24hIntMaxPumpCurrent_Type = Integer32
_EdfaPLP24hIntMaxPumpCurrent_Object = MibTableColumn
edfaPLP24hIntMaxPumpCurrent = _EdfaPLP24hIntMaxPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 6),
    _EdfaPLP24hIntMaxPumpCurrent_Type()
)
edfaPLP24hIntMaxPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxPumpCurrent.setStatus("current")
_EdfaPLP24hIntAverageOIP_Type = Integer32
_EdfaPLP24hIntAverageOIP_Object = MibTableColumn
edfaPLP24hIntAverageOIP = _EdfaPLP24hIntAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 7),
    _EdfaPLP24hIntAverageOIP_Type()
)
edfaPLP24hIntAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntAverageOIP.setStatus("current")
_EdfaPLP24hIntMinOIP_Type = Integer32
_EdfaPLP24hIntMinOIP_Object = MibTableColumn
edfaPLP24hIntMinOIP = _EdfaPLP24hIntMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 8),
    _EdfaPLP24hIntMinOIP_Type()
)
edfaPLP24hIntMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMinOIP.setStatus("current")
_EdfaPLP24hIntMaxOIP_Type = Integer32
_EdfaPLP24hIntMaxOIP_Object = MibTableColumn
edfaPLP24hIntMaxOIP = _EdfaPLP24hIntMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 6, 1, 9),
    _EdfaPLP24hIntMaxOIP_Type()
)
edfaPLP24hIntMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP24hIntMaxOIP.setStatus("current")
_EdfaPLP1weekIntTable_Object = MibTable
edfaPLP1weekIntTable = _EdfaPLP1weekIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7)
)
if mibBuilder.loadTexts:
    edfaPLP1weekIntTable.setStatus("current")
_EdfaPLP1weekIntEntry_Object = MibTableRow
edfaPLP1weekIntEntry = _EdfaPLP1weekIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1)
)
edfaPLP1weekIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "edfaPLP1weekIntIndex"),
)
if mibBuilder.loadTexts:
    edfaPLP1weekIntEntry.setStatus("current")


class _EdfaPLP1weekIntIndex_Type(Integer32):
    """Custom type edfaPLP1weekIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_EdfaPLP1weekIntIndex_Type.__name__ = "Integer32"
_EdfaPLP1weekIntIndex_Object = MibTableColumn
edfaPLP1weekIntIndex = _EdfaPLP1weekIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 1),
    _EdfaPLP1weekIntIndex_Type()
)
edfaPLP1weekIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    edfaPLP1weekIntIndex.setStatus("current")
_EdfaPLP1weekIntValidData_Type = TruthValue
_EdfaPLP1weekIntValidData_Object = MibTableColumn
edfaPLP1weekIntValidData = _EdfaPLP1weekIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 2),
    _EdfaPLP1weekIntValidData_Type()
)
edfaPLP1weekIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP1weekIntValidData.setStatus("current")
_EdfaPLP1weekIntTimeStamp_Type = DateAndTime
_EdfaPLP1weekIntTimeStamp_Object = MibTableColumn
edfaPLP1weekIntTimeStamp = _EdfaPLP1weekIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 3),
    _EdfaPLP1weekIntTimeStamp_Type()
)
edfaPLP1weekIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP1weekIntTimeStamp.setStatus("current")
_EdfaPLP1weekIntAveragePumpCurr_Type = Integer32
_EdfaPLP1weekIntAveragePumpCurr_Object = MibTableColumn
edfaPLP1weekIntAveragePumpCurr = _EdfaPLP1weekIntAveragePumpCurr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 4),
    _EdfaPLP1weekIntAveragePumpCurr_Type()
)
edfaPLP1weekIntAveragePumpCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP1weekIntAveragePumpCurr.setStatus("current")
_EdfaPLP1weekIntMinPumpCurrent_Type = Integer32
_EdfaPLP1weekIntMinPumpCurrent_Object = MibTableColumn
edfaPLP1weekIntMinPumpCurrent = _EdfaPLP1weekIntMinPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 5),
    _EdfaPLP1weekIntMinPumpCurrent_Type()
)
edfaPLP1weekIntMinPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP1weekIntMinPumpCurrent.setStatus("current")
_EdfaPLP1weekIntMaxPumpCurrent_Type = Integer32
_EdfaPLP1weekIntMaxPumpCurrent_Object = MibTableColumn
edfaPLP1weekIntMaxPumpCurrent = _EdfaPLP1weekIntMaxPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 6),
    _EdfaPLP1weekIntMaxPumpCurrent_Type()
)
edfaPLP1weekIntMaxPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP1weekIntMaxPumpCurrent.setStatus("current")
_EdfaPLP1weekIntAverageOIP_Type = Integer32
_EdfaPLP1weekIntAverageOIP_Object = MibTableColumn
edfaPLP1weekIntAverageOIP = _EdfaPLP1weekIntAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 7),
    _EdfaPLP1weekIntAverageOIP_Type()
)
edfaPLP1weekIntAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP1weekIntAverageOIP.setStatus("current")
_EdfaPLP1weekIntMinOIP_Type = Integer32
_EdfaPLP1weekIntMinOIP_Object = MibTableColumn
edfaPLP1weekIntMinOIP = _EdfaPLP1weekIntMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 8),
    _EdfaPLP1weekIntMinOIP_Type()
)
edfaPLP1weekIntMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP1weekIntMinOIP.setStatus("current")
_EdfaPLP1weekIntMaxOIP_Type = Integer32
_EdfaPLP1weekIntMaxOIP_Object = MibTableColumn
edfaPLP1weekIntMaxOIP = _EdfaPLP1weekIntMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 7, 1, 9),
    _EdfaPLP1weekIntMaxOIP_Type()
)
edfaPLP1weekIntMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLP1weekIntMaxOIP.setStatus("current")
_EdfaPLPcurrentTable_Object = MibTable
edfaPLPcurrentTable = _EdfaPLPcurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8)
)
if mibBuilder.loadTexts:
    edfaPLPcurrentTable.setStatus("current")
_EdfaPLPcurrentEntry_Object = MibTableRow
edfaPLPcurrentEntry = _EdfaPLPcurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1)
)
edfaPLPcurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "edfaPLPcurrentIndex"),
)
if mibBuilder.loadTexts:
    edfaPLPcurrentEntry.setStatus("current")


class _EdfaPLPcurrentIndex_Type(Integer32):
    """Custom type edfaPLPcurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EdfaPLPcurrentIndex_Type.__name__ = "Integer32"
_EdfaPLPcurrentIndex_Object = MibTableColumn
edfaPLPcurrentIndex = _EdfaPLPcurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 1),
    _EdfaPLPcurrentIndex_Type()
)
edfaPLPcurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    edfaPLPcurrentIndex.setStatus("current")
_EdfaPLPcurrentValidData_Type = TruthValue
_EdfaPLPcurrentValidData_Object = MibTableColumn
edfaPLPcurrentValidData = _EdfaPLPcurrentValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 2),
    _EdfaPLPcurrentValidData_Type()
)
edfaPLPcurrentValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLPcurrentValidData.setStatus("current")
_EdfaPLPcurrentElapsedTime_Type = Integer32
_EdfaPLPcurrentElapsedTime_Object = MibTableColumn
edfaPLPcurrentElapsedTime = _EdfaPLPcurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 3),
    _EdfaPLPcurrentElapsedTime_Type()
)
edfaPLPcurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLPcurrentElapsedTime.setStatus("current")
_EdfaPLPcurrentAveragePumpCurr_Type = Integer32
_EdfaPLPcurrentAveragePumpCurr_Object = MibTableColumn
edfaPLPcurrentAveragePumpCurr = _EdfaPLPcurrentAveragePumpCurr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 4),
    _EdfaPLPcurrentAveragePumpCurr_Type()
)
edfaPLPcurrentAveragePumpCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLPcurrentAveragePumpCurr.setStatus("current")
_EdfaPLPcurrentMinPumpCurrent_Type = Integer32
_EdfaPLPcurrentMinPumpCurrent_Object = MibTableColumn
edfaPLPcurrentMinPumpCurrent = _EdfaPLPcurrentMinPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 5),
    _EdfaPLPcurrentMinPumpCurrent_Type()
)
edfaPLPcurrentMinPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLPcurrentMinPumpCurrent.setStatus("current")
_EdfaPLPcurrentMaxPumpCurrent_Type = Integer32
_EdfaPLPcurrentMaxPumpCurrent_Object = MibTableColumn
edfaPLPcurrentMaxPumpCurrent = _EdfaPLPcurrentMaxPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 6),
    _EdfaPLPcurrentMaxPumpCurrent_Type()
)
edfaPLPcurrentMaxPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLPcurrentMaxPumpCurrent.setStatus("current")
_EdfaPLPcurrentAverageOIP_Type = Integer32
_EdfaPLPcurrentAverageOIP_Object = MibTableColumn
edfaPLPcurrentAverageOIP = _EdfaPLPcurrentAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 7),
    _EdfaPLPcurrentAverageOIP_Type()
)
edfaPLPcurrentAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLPcurrentAverageOIP.setStatus("current")
_EdfaPLPcurrentMinOIP_Type = Integer32
_EdfaPLPcurrentMinOIP_Object = MibTableColumn
edfaPLPcurrentMinOIP = _EdfaPLPcurrentMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 8),
    _EdfaPLPcurrentMinOIP_Type()
)
edfaPLPcurrentMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLPcurrentMinOIP.setStatus("current")
_EdfaPLPcurrentMaxOIP_Type = Integer32
_EdfaPLPcurrentMaxOIP_Object = MibTableColumn
edfaPLPcurrentMaxOIP = _EdfaPLPcurrentMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 8, 1, 9),
    _EdfaPLPcurrentMaxOIP_Type()
)
edfaPLPcurrentMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLPcurrentMaxOIP.setStatus("current")
_IfTTPLP15minIntTable_Object = MibTable
ifTTPLP15minIntTable = _IfTTPLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9)
)
if mibBuilder.loadTexts:
    ifTTPLP15minIntTable.setStatus("current")
_IfTTPLP15minIntEntry_Object = MibTableRow
ifTTPLP15minIntEntry = _IfTTPLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1)
)
ifTTPLP15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifTTPLP15minIntIndex"),
)
if mibBuilder.loadTexts:
    ifTTPLP15minIntEntry.setStatus("current")


class _IfTTPLP15minIntIndex_Type(Integer32):
    """Custom type ifTTPLP15minIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IfTTPLP15minIntIndex_Type.__name__ = "Integer32"
_IfTTPLP15minIntIndex_Object = MibTableColumn
ifTTPLP15minIntIndex = _IfTTPLP15minIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 1),
    _IfTTPLP15minIntIndex_Type()
)
ifTTPLP15minIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTTPLP15minIntIndex.setStatus("current")
_IfTTPLP15minIntValidData_Type = TruthValue
_IfTTPLP15minIntValidData_Object = MibTableColumn
ifTTPLP15minIntValidData = _IfTTPLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 2),
    _IfTTPLP15minIntValidData_Type()
)
ifTTPLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntValidData.setStatus("current")
_IfTTPLP15minIntTimeStamp_Type = DateAndTime
_IfTTPLP15minIntTimeStamp_Object = MibTableColumn
ifTTPLP15minIntTimeStamp = _IfTTPLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 3),
    _IfTTPLP15minIntTimeStamp_Type()
)
ifTTPLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntTimeStamp.setStatus("current")
_IfTTPLP15minIntAverageLaserCurr_Type = Integer32
_IfTTPLP15minIntAverageLaserCurr_Object = MibTableColumn
ifTTPLP15minIntAverageLaserCurr = _IfTTPLP15minIntAverageLaserCurr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 4),
    _IfTTPLP15minIntAverageLaserCurr_Type()
)
ifTTPLP15minIntAverageLaserCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntAverageLaserCurr.setStatus("current")
_IfTTPLP15minIntMinLaserCurrent_Type = Integer32
_IfTTPLP15minIntMinLaserCurrent_Object = MibTableColumn
ifTTPLP15minIntMinLaserCurrent = _IfTTPLP15minIntMinLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 5),
    _IfTTPLP15minIntMinLaserCurrent_Type()
)
ifTTPLP15minIntMinLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntMinLaserCurrent.setStatus("current")
_IfTTPLP15minIntMaxLaserCurrent_Type = Integer32
_IfTTPLP15minIntMaxLaserCurrent_Object = MibTableColumn
ifTTPLP15minIntMaxLaserCurrent = _IfTTPLP15minIntMaxLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 6),
    _IfTTPLP15minIntMaxLaserCurrent_Type()
)
ifTTPLP15minIntMaxLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntMaxLaserCurrent.setStatus("current")
_IfTTPLP15minIntAverageOIP_Type = Integer32
_IfTTPLP15minIntAverageOIP_Object = MibTableColumn
ifTTPLP15minIntAverageOIP = _IfTTPLP15minIntAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 7),
    _IfTTPLP15minIntAverageOIP_Type()
)
ifTTPLP15minIntAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntAverageOIP.setStatus("current")
_IfTTPLP15minIntMinOIP_Type = Integer32
_IfTTPLP15minIntMinOIP_Object = MibTableColumn
ifTTPLP15minIntMinOIP = _IfTTPLP15minIntMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 8),
    _IfTTPLP15minIntMinOIP_Type()
)
ifTTPLP15minIntMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntMinOIP.setStatus("current")
_IfTTPLP15minIntMaxOIP_Type = Integer32
_IfTTPLP15minIntMaxOIP_Object = MibTableColumn
ifTTPLP15minIntMaxOIP = _IfTTPLP15minIntMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 9),
    _IfTTPLP15minIntMaxOIP_Type()
)
ifTTPLP15minIntMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntMaxOIP.setStatus("current")
_IfTTPLP15minIntAverageOOP_Type = Integer32
_IfTTPLP15minIntAverageOOP_Object = MibTableColumn
ifTTPLP15minIntAverageOOP = _IfTTPLP15minIntAverageOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 10),
    _IfTTPLP15minIntAverageOOP_Type()
)
ifTTPLP15minIntAverageOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntAverageOOP.setStatus("current")
_IfTTPLP15minIntMinOOP_Type = Integer32
_IfTTPLP15minIntMinOOP_Object = MibTableColumn
ifTTPLP15minIntMinOOP = _IfTTPLP15minIntMinOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 11),
    _IfTTPLP15minIntMinOOP_Type()
)
ifTTPLP15minIntMinOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntMinOOP.setStatus("current")
_IfTTPLP15minIntMaxOOP_Type = Integer32
_IfTTPLP15minIntMaxOOP_Object = MibTableColumn
ifTTPLP15minIntMaxOOP = _IfTTPLP15minIntMaxOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 9, 1, 12),
    _IfTTPLP15minIntMaxOOP_Type()
)
ifTTPLP15minIntMaxOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP15minIntMaxOOP.setStatus("current")
_IfTTPLP24hIntTable_Object = MibTable
ifTTPLP24hIntTable = _IfTTPLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10)
)
if mibBuilder.loadTexts:
    ifTTPLP24hIntTable.setStatus("current")
_IfTTPLP24hIntEntry_Object = MibTableRow
ifTTPLP24hIntEntry = _IfTTPLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1)
)
ifTTPLP24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifTTPLP24hIntIndex"),
)
if mibBuilder.loadTexts:
    ifTTPLP24hIntEntry.setStatus("current")


class _IfTTPLP24hIntIndex_Type(Integer32):
    """Custom type ifTTPLP24hIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IfTTPLP24hIntIndex_Type.__name__ = "Integer32"
_IfTTPLP24hIntIndex_Object = MibTableColumn
ifTTPLP24hIntIndex = _IfTTPLP24hIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 1),
    _IfTTPLP24hIntIndex_Type()
)
ifTTPLP24hIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTTPLP24hIntIndex.setStatus("current")
_IfTTPLP24hIntValidData_Type = TruthValue
_IfTTPLP24hIntValidData_Object = MibTableColumn
ifTTPLP24hIntValidData = _IfTTPLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 2),
    _IfTTPLP24hIntValidData_Type()
)
ifTTPLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntValidData.setStatus("current")
_IfTTPLP24hIntTimeStamp_Type = DateAndTime
_IfTTPLP24hIntTimeStamp_Object = MibTableColumn
ifTTPLP24hIntTimeStamp = _IfTTPLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 3),
    _IfTTPLP24hIntTimeStamp_Type()
)
ifTTPLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntTimeStamp.setStatus("current")
_IfTTPLP24hIntAverageLaserCurr_Type = Integer32
_IfTTPLP24hIntAverageLaserCurr_Object = MibTableColumn
ifTTPLP24hIntAverageLaserCurr = _IfTTPLP24hIntAverageLaserCurr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 4),
    _IfTTPLP24hIntAverageLaserCurr_Type()
)
ifTTPLP24hIntAverageLaserCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntAverageLaserCurr.setStatus("current")
_IfTTPLP24hIntMinLaserCurrent_Type = Integer32
_IfTTPLP24hIntMinLaserCurrent_Object = MibTableColumn
ifTTPLP24hIntMinLaserCurrent = _IfTTPLP24hIntMinLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 5),
    _IfTTPLP24hIntMinLaserCurrent_Type()
)
ifTTPLP24hIntMinLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntMinLaserCurrent.setStatus("current")
_IfTTPLP24hIntMaxLaserCurrent_Type = Integer32
_IfTTPLP24hIntMaxLaserCurrent_Object = MibTableColumn
ifTTPLP24hIntMaxLaserCurrent = _IfTTPLP24hIntMaxLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 6),
    _IfTTPLP24hIntMaxLaserCurrent_Type()
)
ifTTPLP24hIntMaxLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntMaxLaserCurrent.setStatus("current")
_IfTTPLP24hIntAverageOIP_Type = Integer32
_IfTTPLP24hIntAverageOIP_Object = MibTableColumn
ifTTPLP24hIntAverageOIP = _IfTTPLP24hIntAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 7),
    _IfTTPLP24hIntAverageOIP_Type()
)
ifTTPLP24hIntAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntAverageOIP.setStatus("current")
_IfTTPLP24hIntMinOIP_Type = Integer32
_IfTTPLP24hIntMinOIP_Object = MibTableColumn
ifTTPLP24hIntMinOIP = _IfTTPLP24hIntMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 8),
    _IfTTPLP24hIntMinOIP_Type()
)
ifTTPLP24hIntMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntMinOIP.setStatus("current")
_IfTTPLP24hIntMaxOIP_Type = Integer32
_IfTTPLP24hIntMaxOIP_Object = MibTableColumn
ifTTPLP24hIntMaxOIP = _IfTTPLP24hIntMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 9),
    _IfTTPLP24hIntMaxOIP_Type()
)
ifTTPLP24hIntMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntMaxOIP.setStatus("current")
_IfTTPLP24hIntAverageOOP_Type = Integer32
_IfTTPLP24hIntAverageOOP_Object = MibTableColumn
ifTTPLP24hIntAverageOOP = _IfTTPLP24hIntAverageOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 10),
    _IfTTPLP24hIntAverageOOP_Type()
)
ifTTPLP24hIntAverageOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntAverageOOP.setStatus("current")
_IfTTPLP24hIntMinOOP_Type = Integer32
_IfTTPLP24hIntMinOOP_Object = MibTableColumn
ifTTPLP24hIntMinOOP = _IfTTPLP24hIntMinOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 11),
    _IfTTPLP24hIntMinOOP_Type()
)
ifTTPLP24hIntMinOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntMinOOP.setStatus("current")
_IfTTPLP24hIntMaxOOP_Type = Integer32
_IfTTPLP24hIntMaxOOP_Object = MibTableColumn
ifTTPLP24hIntMaxOOP = _IfTTPLP24hIntMaxOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 10, 1, 12),
    _IfTTPLP24hIntMaxOOP_Type()
)
ifTTPLP24hIntMaxOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP24hIntMaxOOP.setStatus("current")
_IfTTPLP1weekIntTable_Object = MibTable
ifTTPLP1weekIntTable = _IfTTPLP1weekIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11)
)
if mibBuilder.loadTexts:
    ifTTPLP1weekIntTable.setStatus("current")
_IfTTPLP1weekIntEntry_Object = MibTableRow
ifTTPLP1weekIntEntry = _IfTTPLP1weekIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1)
)
ifTTPLP1weekIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifTTPLP1weekIntIndex"),
)
if mibBuilder.loadTexts:
    ifTTPLP1weekIntEntry.setStatus("current")


class _IfTTPLP1weekIntIndex_Type(Integer32):
    """Custom type ifTTPLP1weekIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_IfTTPLP1weekIntIndex_Type.__name__ = "Integer32"
_IfTTPLP1weekIntIndex_Object = MibTableColumn
ifTTPLP1weekIntIndex = _IfTTPLP1weekIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 1),
    _IfTTPLP1weekIntIndex_Type()
)
ifTTPLP1weekIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntIndex.setStatus("current")
_IfTTPLP1weekIntValidData_Type = TruthValue
_IfTTPLP1weekIntValidData_Object = MibTableColumn
ifTTPLP1weekIntValidData = _IfTTPLP1weekIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 2),
    _IfTTPLP1weekIntValidData_Type()
)
ifTTPLP1weekIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntValidData.setStatus("current")
_IfTTPLP1weekIntTimeStamp_Type = DateAndTime
_IfTTPLP1weekIntTimeStamp_Object = MibTableColumn
ifTTPLP1weekIntTimeStamp = _IfTTPLP1weekIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 3),
    _IfTTPLP1weekIntTimeStamp_Type()
)
ifTTPLP1weekIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntTimeStamp.setStatus("current")
_IfTTPLP1weekIntAverageLaserCurr_Type = Integer32
_IfTTPLP1weekIntAverageLaserCurr_Object = MibTableColumn
ifTTPLP1weekIntAverageLaserCurr = _IfTTPLP1weekIntAverageLaserCurr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 4),
    _IfTTPLP1weekIntAverageLaserCurr_Type()
)
ifTTPLP1weekIntAverageLaserCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntAverageLaserCurr.setStatus("current")
_IfTTPLP1weekIntMinLaserCurrent_Type = Integer32
_IfTTPLP1weekIntMinLaserCurrent_Object = MibTableColumn
ifTTPLP1weekIntMinLaserCurrent = _IfTTPLP1weekIntMinLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 5),
    _IfTTPLP1weekIntMinLaserCurrent_Type()
)
ifTTPLP1weekIntMinLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntMinLaserCurrent.setStatus("current")
_IfTTPLP1weekIntMaxLaserCurrent_Type = Integer32
_IfTTPLP1weekIntMaxLaserCurrent_Object = MibTableColumn
ifTTPLP1weekIntMaxLaserCurrent = _IfTTPLP1weekIntMaxLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 6),
    _IfTTPLP1weekIntMaxLaserCurrent_Type()
)
ifTTPLP1weekIntMaxLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntMaxLaserCurrent.setStatus("current")
_IfTTPLP1weekIntAverageOIP_Type = Integer32
_IfTTPLP1weekIntAverageOIP_Object = MibTableColumn
ifTTPLP1weekIntAverageOIP = _IfTTPLP1weekIntAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 7),
    _IfTTPLP1weekIntAverageOIP_Type()
)
ifTTPLP1weekIntAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntAverageOIP.setStatus("current")
_IfTTPLP1weekIntMinOIP_Type = Integer32
_IfTTPLP1weekIntMinOIP_Object = MibTableColumn
ifTTPLP1weekIntMinOIP = _IfTTPLP1weekIntMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 8),
    _IfTTPLP1weekIntMinOIP_Type()
)
ifTTPLP1weekIntMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntMinOIP.setStatus("current")
_IfTTPLP1weekIntMaxOIP_Type = Integer32
_IfTTPLP1weekIntMaxOIP_Object = MibTableColumn
ifTTPLP1weekIntMaxOIP = _IfTTPLP1weekIntMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 9),
    _IfTTPLP1weekIntMaxOIP_Type()
)
ifTTPLP1weekIntMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntMaxOIP.setStatus("current")
_IfTTPLP1weekIntAverageOOP_Type = Integer32
_IfTTPLP1weekIntAverageOOP_Object = MibTableColumn
ifTTPLP1weekIntAverageOOP = _IfTTPLP1weekIntAverageOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 10),
    _IfTTPLP1weekIntAverageOOP_Type()
)
ifTTPLP1weekIntAverageOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntAverageOOP.setStatus("current")
_IfTTPLP1weekIntMinOOP_Type = Integer32
_IfTTPLP1weekIntMinOOP_Object = MibTableColumn
ifTTPLP1weekIntMinOOP = _IfTTPLP1weekIntMinOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 11),
    _IfTTPLP1weekIntMinOOP_Type()
)
ifTTPLP1weekIntMinOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntMinOOP.setStatus("current")
_IfTTPLP1weekIntMaxOOP_Type = Integer32
_IfTTPLP1weekIntMaxOOP_Object = MibTableColumn
ifTTPLP1weekIntMaxOOP = _IfTTPLP1weekIntMaxOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 11, 1, 12),
    _IfTTPLP1weekIntMaxOOP_Type()
)
ifTTPLP1weekIntMaxOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLP1weekIntMaxOOP.setStatus("current")
_IfTTPLPcurrentTable_Object = MibTable
ifTTPLPcurrentTable = _IfTTPLPcurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12)
)
if mibBuilder.loadTexts:
    ifTTPLPcurrentTable.setStatus("current")
_IfTTPLPcurrentEntry_Object = MibTableRow
ifTTPLPcurrentEntry = _IfTTPLPcurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1)
)
ifTTPLPcurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifTTPLPcurrentIndex"),
)
if mibBuilder.loadTexts:
    ifTTPLPcurrentEntry.setStatus("current")


class _IfTTPLPcurrentIndex_Type(Integer32):
    """Custom type ifTTPLPcurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IfTTPLPcurrentIndex_Type.__name__ = "Integer32"
_IfTTPLPcurrentIndex_Object = MibTableColumn
ifTTPLPcurrentIndex = _IfTTPLPcurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 1),
    _IfTTPLPcurrentIndex_Type()
)
ifTTPLPcurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTTPLPcurrentIndex.setStatus("current")
_IfTTPLPcurrentValidData_Type = TruthValue
_IfTTPLPcurrentValidData_Object = MibTableColumn
ifTTPLPcurrentValidData = _IfTTPLPcurrentValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 2),
    _IfTTPLPcurrentValidData_Type()
)
ifTTPLPcurrentValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentValidData.setStatus("current")
_IfTTPLPcurrentElapsedTime_Type = Integer32
_IfTTPLPcurrentElapsedTime_Object = MibTableColumn
ifTTPLPcurrentElapsedTime = _IfTTPLPcurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 3),
    _IfTTPLPcurrentElapsedTime_Type()
)
ifTTPLPcurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentElapsedTime.setStatus("current")
_IfTTPLPcurrentAverageLaserCurr_Type = Integer32
_IfTTPLPcurrentAverageLaserCurr_Object = MibTableColumn
ifTTPLPcurrentAverageLaserCurr = _IfTTPLPcurrentAverageLaserCurr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 4),
    _IfTTPLPcurrentAverageLaserCurr_Type()
)
ifTTPLPcurrentAverageLaserCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentAverageLaserCurr.setStatus("current")
_IfTTPLPcurrentMinLaserCurrent_Type = Integer32
_IfTTPLPcurrentMinLaserCurrent_Object = MibTableColumn
ifTTPLPcurrentMinLaserCurrent = _IfTTPLPcurrentMinLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 5),
    _IfTTPLPcurrentMinLaserCurrent_Type()
)
ifTTPLPcurrentMinLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentMinLaserCurrent.setStatus("current")
_IfTTPLPcurrentMaxLaserCurrent_Type = Integer32
_IfTTPLPcurrentMaxLaserCurrent_Object = MibTableColumn
ifTTPLPcurrentMaxLaserCurrent = _IfTTPLPcurrentMaxLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 6),
    _IfTTPLPcurrentMaxLaserCurrent_Type()
)
ifTTPLPcurrentMaxLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentMaxLaserCurrent.setStatus("current")
_IfTTPLPcurrentAverageOIP_Type = Integer32
_IfTTPLPcurrentAverageOIP_Object = MibTableColumn
ifTTPLPcurrentAverageOIP = _IfTTPLPcurrentAverageOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 7),
    _IfTTPLPcurrentAverageOIP_Type()
)
ifTTPLPcurrentAverageOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentAverageOIP.setStatus("current")
_IfTTPLPcurrentMinOIP_Type = Integer32
_IfTTPLPcurrentMinOIP_Object = MibTableColumn
ifTTPLPcurrentMinOIP = _IfTTPLPcurrentMinOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 8),
    _IfTTPLPcurrentMinOIP_Type()
)
ifTTPLPcurrentMinOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentMinOIP.setStatus("current")
_IfTTPLPcurrentMaxOIP_Type = Integer32
_IfTTPLPcurrentMaxOIP_Object = MibTableColumn
ifTTPLPcurrentMaxOIP = _IfTTPLPcurrentMaxOIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 9),
    _IfTTPLPcurrentMaxOIP_Type()
)
ifTTPLPcurrentMaxOIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentMaxOIP.setStatus("current")
_IfTTPLPcurrentAverageOOP_Type = Integer32
_IfTTPLPcurrentAverageOOP_Object = MibTableColumn
ifTTPLPcurrentAverageOOP = _IfTTPLPcurrentAverageOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 10),
    _IfTTPLPcurrentAverageOOP_Type()
)
ifTTPLPcurrentAverageOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentAverageOOP.setStatus("current")
_IfTTPLPcurrentMinOOP_Type = Integer32
_IfTTPLPcurrentMinOOP_Object = MibTableColumn
ifTTPLPcurrentMinOOP = _IfTTPLPcurrentMinOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 11),
    _IfTTPLPcurrentMinOOP_Type()
)
ifTTPLPcurrentMinOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentMinOOP.setStatus("current")
_IfTTPLPcurrentMaxOOP_Type = Integer32
_IfTTPLPcurrentMaxOOP_Object = MibTableColumn
ifTTPLPcurrentMaxOOP = _IfTTPLPcurrentMaxOOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 12, 1, 12),
    _IfTTPLPcurrentMaxOOP_Type()
)
ifTTPLPcurrentMaxOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTTPLPcurrentMaxOOP.setStatus("current")
_ModulePLP15minIntTable_Object = MibTable
modulePLP15minIntTable = _ModulePLP15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13)
)
if mibBuilder.loadTexts:
    modulePLP15minIntTable.setStatus("current")
_ModulePLP15minIntEntry_Object = MibTableRow
modulePLP15minIntEntry = _ModulePLP15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1)
)
modulePLP15minIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "modulePLP15minIntIndex"),
)
if mibBuilder.loadTexts:
    modulePLP15minIntEntry.setStatus("current")


class _ModulePLP15minIntIndex_Type(Integer32):
    """Custom type modulePLP15minIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ModulePLP15minIntIndex_Type.__name__ = "Integer32"
_ModulePLP15minIntIndex_Object = MibTableColumn
modulePLP15minIntIndex = _ModulePLP15minIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 1),
    _ModulePLP15minIntIndex_Type()
)
modulePLP15minIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modulePLP15minIntIndex.setStatus("current")
_ModulePLP15minIntValidData_Type = TruthValue
_ModulePLP15minIntValidData_Object = MibTableColumn
modulePLP15minIntValidData = _ModulePLP15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 2),
    _ModulePLP15minIntValidData_Type()
)
modulePLP15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP15minIntValidData.setStatus("current")
_ModulePLP15minIntTimeStamp_Type = DateAndTime
_ModulePLP15minIntTimeStamp_Object = MibTableColumn
modulePLP15minIntTimeStamp = _ModulePLP15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 3),
    _ModulePLP15minIntTimeStamp_Type()
)
modulePLP15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP15minIntTimeStamp.setStatus("current")
_ModulePLP15minIntAverageTemp_Type = Integer32
_ModulePLP15minIntAverageTemp_Object = MibTableColumn
modulePLP15minIntAverageTemp = _ModulePLP15minIntAverageTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 4),
    _ModulePLP15minIntAverageTemp_Type()
)
modulePLP15minIntAverageTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP15minIntAverageTemp.setStatus("current")
_ModulePLP15minIntMinTemp_Type = Integer32
_ModulePLP15minIntMinTemp_Object = MibTableColumn
modulePLP15minIntMinTemp = _ModulePLP15minIntMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 5),
    _ModulePLP15minIntMinTemp_Type()
)
modulePLP15minIntMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP15minIntMinTemp.setStatus("current")
_ModulePLP15minIntMaxTemp_Type = Integer32
_ModulePLP15minIntMaxTemp_Object = MibTableColumn
modulePLP15minIntMaxTemp = _ModulePLP15minIntMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 6),
    _ModulePLP15minIntMaxTemp_Type()
)
modulePLP15minIntMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP15minIntMaxTemp.setStatus("current")
_ModulePLP15minIntAverageVoltage_Type = Integer32
_ModulePLP15minIntAverageVoltage_Object = MibTableColumn
modulePLP15minIntAverageVoltage = _ModulePLP15minIntAverageVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 7),
    _ModulePLP15minIntAverageVoltage_Type()
)
modulePLP15minIntAverageVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP15minIntAverageVoltage.setStatus("current")
_ModulePLP15minIntMinVoltage_Type = Integer32
_ModulePLP15minIntMinVoltage_Object = MibTableColumn
modulePLP15minIntMinVoltage = _ModulePLP15minIntMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 8),
    _ModulePLP15minIntMinVoltage_Type()
)
modulePLP15minIntMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP15minIntMinVoltage.setStatus("current")
_ModulePLP15minIntMaxVoltage_Type = Integer32
_ModulePLP15minIntMaxVoltage_Object = MibTableColumn
modulePLP15minIntMaxVoltage = _ModulePLP15minIntMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 13, 1, 9),
    _ModulePLP15minIntMaxVoltage_Type()
)
modulePLP15minIntMaxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP15minIntMaxVoltage.setStatus("current")
_ModulePLP24hIntTable_Object = MibTable
modulePLP24hIntTable = _ModulePLP24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14)
)
if mibBuilder.loadTexts:
    modulePLP24hIntTable.setStatus("current")
_ModulePLP24hIntEntry_Object = MibTableRow
modulePLP24hIntEntry = _ModulePLP24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1)
)
modulePLP24hIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "modulePLP24hIntIndex"),
)
if mibBuilder.loadTexts:
    modulePLP24hIntEntry.setStatus("current")


class _ModulePLP24hIntIndex_Type(Integer32):
    """Custom type modulePLP24hIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ModulePLP24hIntIndex_Type.__name__ = "Integer32"
_ModulePLP24hIntIndex_Object = MibTableColumn
modulePLP24hIntIndex = _ModulePLP24hIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 1),
    _ModulePLP24hIntIndex_Type()
)
modulePLP24hIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modulePLP24hIntIndex.setStatus("current")
_ModulePLP24hIntValidData_Type = TruthValue
_ModulePLP24hIntValidData_Object = MibTableColumn
modulePLP24hIntValidData = _ModulePLP24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 2),
    _ModulePLP24hIntValidData_Type()
)
modulePLP24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP24hIntValidData.setStatus("current")
_ModulePLP24hIntTimeStamp_Type = DateAndTime
_ModulePLP24hIntTimeStamp_Object = MibTableColumn
modulePLP24hIntTimeStamp = _ModulePLP24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 3),
    _ModulePLP24hIntTimeStamp_Type()
)
modulePLP24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP24hIntTimeStamp.setStatus("current")
_ModulePLP24hIntAverageTemp_Type = Integer32
_ModulePLP24hIntAverageTemp_Object = MibTableColumn
modulePLP24hIntAverageTemp = _ModulePLP24hIntAverageTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 4),
    _ModulePLP24hIntAverageTemp_Type()
)
modulePLP24hIntAverageTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP24hIntAverageTemp.setStatus("current")
_ModulePLP24hIntMinTemp_Type = Integer32
_ModulePLP24hIntMinTemp_Object = MibTableColumn
modulePLP24hIntMinTemp = _ModulePLP24hIntMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 5),
    _ModulePLP24hIntMinTemp_Type()
)
modulePLP24hIntMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP24hIntMinTemp.setStatus("current")
_ModulePLP24hIntMaxTemp_Type = Integer32
_ModulePLP24hIntMaxTemp_Object = MibTableColumn
modulePLP24hIntMaxTemp = _ModulePLP24hIntMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 6),
    _ModulePLP24hIntMaxTemp_Type()
)
modulePLP24hIntMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP24hIntMaxTemp.setStatus("current")
_ModulePLP24hIntAverageVoltage_Type = Integer32
_ModulePLP24hIntAverageVoltage_Object = MibTableColumn
modulePLP24hIntAverageVoltage = _ModulePLP24hIntAverageVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 7),
    _ModulePLP24hIntAverageVoltage_Type()
)
modulePLP24hIntAverageVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP24hIntAverageVoltage.setStatus("current")
_ModulePLP24hIntMinVoltage_Type = Integer32
_ModulePLP24hIntMinVoltage_Object = MibTableColumn
modulePLP24hIntMinVoltage = _ModulePLP24hIntMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 8),
    _ModulePLP24hIntMinVoltage_Type()
)
modulePLP24hIntMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP24hIntMinVoltage.setStatus("current")
_ModulePLP24hIntMaxVoltage_Type = Integer32
_ModulePLP24hIntMaxVoltage_Object = MibTableColumn
modulePLP24hIntMaxVoltage = _ModulePLP24hIntMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 14, 1, 9),
    _ModulePLP24hIntMaxVoltage_Type()
)
modulePLP24hIntMaxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP24hIntMaxVoltage.setStatus("current")
_ModulePLP1weekIntTable_Object = MibTable
modulePLP1weekIntTable = _ModulePLP1weekIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15)
)
if mibBuilder.loadTexts:
    modulePLP1weekIntTable.setStatus("current")
_ModulePLP1weekIntEntry_Object = MibTableRow
modulePLP1weekIntEntry = _ModulePLP1weekIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1)
)
modulePLP1weekIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "modulePLP1weekIntIndex"),
)
if mibBuilder.loadTexts:
    modulePLP1weekIntEntry.setStatus("current")


class _ModulePLP1weekIntIndex_Type(Integer32):
    """Custom type modulePLP1weekIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ModulePLP1weekIntIndex_Type.__name__ = "Integer32"
_ModulePLP1weekIntIndex_Object = MibTableColumn
modulePLP1weekIntIndex = _ModulePLP1weekIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 1),
    _ModulePLP1weekIntIndex_Type()
)
modulePLP1weekIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modulePLP1weekIntIndex.setStatus("current")
_ModulePLP1weekIntValidData_Type = TruthValue
_ModulePLP1weekIntValidData_Object = MibTableColumn
modulePLP1weekIntValidData = _ModulePLP1weekIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 2),
    _ModulePLP1weekIntValidData_Type()
)
modulePLP1weekIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP1weekIntValidData.setStatus("current")
_ModulePLP1weekIntTimeStamp_Type = DateAndTime
_ModulePLP1weekIntTimeStamp_Object = MibTableColumn
modulePLP1weekIntTimeStamp = _ModulePLP1weekIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 3),
    _ModulePLP1weekIntTimeStamp_Type()
)
modulePLP1weekIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP1weekIntTimeStamp.setStatus("current")
_ModulePLP1weekIntAverageTemp_Type = Integer32
_ModulePLP1weekIntAverageTemp_Object = MibTableColumn
modulePLP1weekIntAverageTemp = _ModulePLP1weekIntAverageTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 4),
    _ModulePLP1weekIntAverageTemp_Type()
)
modulePLP1weekIntAverageTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP1weekIntAverageTemp.setStatus("current")
_ModulePLP1weekIntMinTemp_Type = Integer32
_ModulePLP1weekIntMinTemp_Object = MibTableColumn
modulePLP1weekIntMinTemp = _ModulePLP1weekIntMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 5),
    _ModulePLP1weekIntMinTemp_Type()
)
modulePLP1weekIntMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP1weekIntMinTemp.setStatus("current")
_ModulePLP1weekIntMaxTemp_Type = Integer32
_ModulePLP1weekIntMaxTemp_Object = MibTableColumn
modulePLP1weekIntMaxTemp = _ModulePLP1weekIntMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 6),
    _ModulePLP1weekIntMaxTemp_Type()
)
modulePLP1weekIntMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP1weekIntMaxTemp.setStatus("current")
_ModulePLP1weekIntAverageVoltage_Type = Integer32
_ModulePLP1weekIntAverageVoltage_Object = MibTableColumn
modulePLP1weekIntAverageVoltage = _ModulePLP1weekIntAverageVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 7),
    _ModulePLP1weekIntAverageVoltage_Type()
)
modulePLP1weekIntAverageVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP1weekIntAverageVoltage.setStatus("current")
_ModulePLP1weekIntMinVoltage_Type = Integer32
_ModulePLP1weekIntMinVoltage_Object = MibTableColumn
modulePLP1weekIntMinVoltage = _ModulePLP1weekIntMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 8),
    _ModulePLP1weekIntMinVoltage_Type()
)
modulePLP1weekIntMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP1weekIntMinVoltage.setStatus("current")
_ModulePLP1weekIntMaxVoltage_Type = Integer32
_ModulePLP1weekIntMaxVoltage_Object = MibTableColumn
modulePLP1weekIntMaxVoltage = _ModulePLP1weekIntMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 15, 1, 9),
    _ModulePLP1weekIntMaxVoltage_Type()
)
modulePLP1weekIntMaxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLP1weekIntMaxVoltage.setStatus("current")
_ModulePLPcurrentTable_Object = MibTable
modulePLPcurrentTable = _ModulePLPcurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16)
)
if mibBuilder.loadTexts:
    modulePLPcurrentTable.setStatus("current")
_ModulePLPcurrentEntry_Object = MibTableRow
modulePLPcurrentEntry = _ModulePLPcurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1)
)
modulePLPcurrentEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "modulePLPcurrentIndex"),
)
if mibBuilder.loadTexts:
    modulePLPcurrentEntry.setStatus("current")


class _ModulePLPcurrentIndex_Type(Integer32):
    """Custom type modulePLPcurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ModulePLPcurrentIndex_Type.__name__ = "Integer32"
_ModulePLPcurrentIndex_Object = MibTableColumn
modulePLPcurrentIndex = _ModulePLPcurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 1),
    _ModulePLPcurrentIndex_Type()
)
modulePLPcurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modulePLPcurrentIndex.setStatus("current")
_ModulePLPcurrentValidData_Type = TruthValue
_ModulePLPcurrentValidData_Object = MibTableColumn
modulePLPcurrentValidData = _ModulePLPcurrentValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 2),
    _ModulePLPcurrentValidData_Type()
)
modulePLPcurrentValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLPcurrentValidData.setStatus("current")
_ModulePLPcurrentElapsedTime_Type = Integer32
_ModulePLPcurrentElapsedTime_Object = MibTableColumn
modulePLPcurrentElapsedTime = _ModulePLPcurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 3),
    _ModulePLPcurrentElapsedTime_Type()
)
modulePLPcurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLPcurrentElapsedTime.setStatus("current")
_ModulePLPcurrentAverageTemp_Type = Integer32
_ModulePLPcurrentAverageTemp_Object = MibTableColumn
modulePLPcurrentAverageTemp = _ModulePLPcurrentAverageTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 4),
    _ModulePLPcurrentAverageTemp_Type()
)
modulePLPcurrentAverageTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLPcurrentAverageTemp.setStatus("current")
_ModulePLPcurrentMinTemp_Type = Integer32
_ModulePLPcurrentMinTemp_Object = MibTableColumn
modulePLPcurrentMinTemp = _ModulePLPcurrentMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 5),
    _ModulePLPcurrentMinTemp_Type()
)
modulePLPcurrentMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLPcurrentMinTemp.setStatus("current")
_ModulePLPcurrentMaxTemp_Type = Integer32
_ModulePLPcurrentMaxTemp_Object = MibTableColumn
modulePLPcurrentMaxTemp = _ModulePLPcurrentMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 6),
    _ModulePLPcurrentMaxTemp_Type()
)
modulePLPcurrentMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLPcurrentMaxTemp.setStatus("current")
_ModulePLPcurrentAverageVoltage_Type = Integer32
_ModulePLPcurrentAverageVoltage_Object = MibTableColumn
modulePLPcurrentAverageVoltage = _ModulePLPcurrentAverageVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 7),
    _ModulePLPcurrentAverageVoltage_Type()
)
modulePLPcurrentAverageVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLPcurrentAverageVoltage.setStatus("current")
_ModulePLPcurrentMinVoltage_Type = Integer32
_ModulePLPcurrentMinVoltage_Object = MibTableColumn
modulePLPcurrentMinVoltage = _ModulePLPcurrentMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 8),
    _ModulePLPcurrentMinVoltage_Type()
)
modulePLPcurrentMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLPcurrentMinVoltage.setStatus("current")
_ModulePLPcurrentMaxVoltage_Type = Integer32
_ModulePLPcurrentMaxVoltage_Object = MibTableColumn
modulePLPcurrentMaxVoltage = _ModulePLPcurrentMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 2, 16, 1, 9),
    _ModulePLPcurrentMaxVoltage_Type()
)
modulePLPcurrentMaxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePLPcurrentMaxVoltage.setStatus("current")
_PhysicalLayerAlarmMon_ObjectIdentity = ObjectIdentity
physicalLayerAlarmMon = _PhysicalLayerAlarmMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3)
)
_OLMPLA15minIntTable_Object = MibTable
oLMPLA15minIntTable = _OLMPLA15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1)
)
if mibBuilder.loadTexts:
    oLMPLA15minIntTable.setStatus("current")
_OLMPLA15minIntEntry_Object = MibTableRow
oLMPLA15minIntEntry = _OLMPLA15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1)
)
oLMPLA15minIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "oLMPLA15minIntIndex"),
)
if mibBuilder.loadTexts:
    oLMPLA15minIntEntry.setStatus("current")


class _OLMPLA15minIntIndex_Type(Integer32):
    """Custom type oLMPLA15minIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_OLMPLA15minIntIndex_Type.__name__ = "Integer32"
_OLMPLA15minIntIndex_Object = MibTableColumn
oLMPLA15minIntIndex = _OLMPLA15minIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 1),
    _OLMPLA15minIntIndex_Type()
)
oLMPLA15minIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oLMPLA15minIntIndex.setStatus("current")
_OLMPLA15minIntRxLOS_Type = Gauge32
_OLMPLA15minIntRxLOS_Object = MibTableColumn
oLMPLA15minIntRxLOS = _OLMPLA15minIntRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 2),
    _OLMPLA15minIntRxLOS_Type()
)
oLMPLA15minIntRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntRxLOS.setStatus("current")
_OLMPLA15minIntTxLOS_Type = Gauge32
_OLMPLA15minIntTxLOS_Object = MibTableColumn
oLMPLA15minIntTxLOS = _OLMPLA15minIntTxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 3),
    _OLMPLA15minIntTxLOS_Type()
)
oLMPLA15minIntTxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntTxLOS.setStatus("current")
_OLMPLA15minIntRxLow_Type = Gauge32
_OLMPLA15minIntRxLow_Object = MibTableColumn
oLMPLA15minIntRxLow = _OLMPLA15minIntRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 4),
    _OLMPLA15minIntRxLow_Type()
)
oLMPLA15minIntRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntRxLow.setStatus("current")
_OLMPLA15minIntRxHigh_Type = Gauge32
_OLMPLA15minIntRxHigh_Object = MibTableColumn
oLMPLA15minIntRxHigh = _OLMPLA15minIntRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 5),
    _OLMPLA15minIntRxHigh_Type()
)
oLMPLA15minIntRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntRxHigh.setStatus("current")
_OLMPLA15minIntTxLow_Type = Gauge32
_OLMPLA15minIntTxLow_Object = MibTableColumn
oLMPLA15minIntTxLow = _OLMPLA15minIntTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 6),
    _OLMPLA15minIntTxLow_Type()
)
oLMPLA15minIntTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntTxLow.setStatus("current")
_OLMPLA15minIntTxHigh_Type = Gauge32
_OLMPLA15minIntTxHigh_Object = MibTableColumn
oLMPLA15minIntTxHigh = _OLMPLA15minIntTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 7),
    _OLMPLA15minIntTxHigh_Type()
)
oLMPLA15minIntTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntTxHigh.setStatus("current")
_OLMPLA15minIntRxIntrusion_Type = Gauge32
_OLMPLA15minIntRxIntrusion_Object = MibTableColumn
oLMPLA15minIntRxIntrusion = _OLMPLA15minIntRxIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 8),
    _OLMPLA15minIntRxIntrusion_Type()
)
oLMPLA15minIntRxIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntRxIntrusion.setStatus("current")
_OLMPLA15minIntTxIntrusion_Type = Gauge32
_OLMPLA15minIntTxIntrusion_Object = MibTableColumn
oLMPLA15minIntTxIntrusion = _OLMPLA15minIntTxIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 9),
    _OLMPLA15minIntTxIntrusion_Type()
)
oLMPLA15minIntTxIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntTxIntrusion.setStatus("current")
_OLMPLA15minIntValidData_Type = TruthValue
_OLMPLA15minIntValidData_Object = MibTableColumn
oLMPLA15minIntValidData = _OLMPLA15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 10),
    _OLMPLA15minIntValidData_Type()
)
oLMPLA15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntValidData.setStatus("current")
_OLMPLA15minIntTimeStamp_Type = DateAndTime
_OLMPLA15minIntTimeStamp_Object = MibTableColumn
oLMPLA15minIntTimeStamp = _OLMPLA15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 11),
    _OLMPLA15minIntTimeStamp_Type()
)
oLMPLA15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntTimeStamp.setStatus("current")
_OLMPLA15minIntRxLowMon_Type = Gauge32
_OLMPLA15minIntRxLowMon_Object = MibTableColumn
oLMPLA15minIntRxLowMon = _OLMPLA15minIntRxLowMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 12),
    _OLMPLA15minIntRxLowMon_Type()
)
oLMPLA15minIntRxLowMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntRxLowMon.setStatus("current")
_OLMPLA15minIntRxHighMon_Type = Gauge32
_OLMPLA15minIntRxHighMon_Object = MibTableColumn
oLMPLA15minIntRxHighMon = _OLMPLA15minIntRxHighMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 13),
    _OLMPLA15minIntRxHighMon_Type()
)
oLMPLA15minIntRxHighMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntRxHighMon.setStatus("current")
_OLMPLA15minIntTxLowMon_Type = Gauge32
_OLMPLA15minIntTxLowMon_Object = MibTableColumn
oLMPLA15minIntTxLowMon = _OLMPLA15minIntTxLowMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 14),
    _OLMPLA15minIntTxLowMon_Type()
)
oLMPLA15minIntTxLowMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntTxLowMon.setStatus("current")
_OLMPLA15minIntTxHighMon_Type = Gauge32
_OLMPLA15minIntTxHighMon_Object = MibTableColumn
oLMPLA15minIntTxHighMon = _OLMPLA15minIntTxHighMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 1, 1, 15),
    _OLMPLA15minIntTxHighMon_Type()
)
oLMPLA15minIntTxHighMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA15minIntTxHighMon.setStatus("current")
_OLMPLA24hIntTable_Object = MibTable
oLMPLA24hIntTable = _OLMPLA24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2)
)
if mibBuilder.loadTexts:
    oLMPLA24hIntTable.setStatus("current")
_OLMPLA24hIntEntry_Object = MibTableRow
oLMPLA24hIntEntry = _OLMPLA24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1)
)
oLMPLA24hIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "oLMPLA24hIntIndex"),
)
if mibBuilder.loadTexts:
    oLMPLA24hIntEntry.setStatus("current")


class _OLMPLA24hIntIndex_Type(Integer32):
    """Custom type oLMPLA24hIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_OLMPLA24hIntIndex_Type.__name__ = "Integer32"
_OLMPLA24hIntIndex_Object = MibTableColumn
oLMPLA24hIntIndex = _OLMPLA24hIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 1),
    _OLMPLA24hIntIndex_Type()
)
oLMPLA24hIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oLMPLA24hIntIndex.setStatus("current")
_OLMPLA24hIntRxLOS_Type = Gauge32
_OLMPLA24hIntRxLOS_Object = MibTableColumn
oLMPLA24hIntRxLOS = _OLMPLA24hIntRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 2),
    _OLMPLA24hIntRxLOS_Type()
)
oLMPLA24hIntRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntRxLOS.setStatus("current")
_OLMPLA24hIntTxLOS_Type = Gauge32
_OLMPLA24hIntTxLOS_Object = MibTableColumn
oLMPLA24hIntTxLOS = _OLMPLA24hIntTxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 3),
    _OLMPLA24hIntTxLOS_Type()
)
oLMPLA24hIntTxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntTxLOS.setStatus("current")
_OLMPLA24hIntRxLow_Type = Gauge32
_OLMPLA24hIntRxLow_Object = MibTableColumn
oLMPLA24hIntRxLow = _OLMPLA24hIntRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 4),
    _OLMPLA24hIntRxLow_Type()
)
oLMPLA24hIntRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntRxLow.setStatus("current")
_OLMPLA24hIntRxHigh_Type = Gauge32
_OLMPLA24hIntRxHigh_Object = MibTableColumn
oLMPLA24hIntRxHigh = _OLMPLA24hIntRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 5),
    _OLMPLA24hIntRxHigh_Type()
)
oLMPLA24hIntRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntRxHigh.setStatus("current")
_OLMPLA24hIntTxLow_Type = Gauge32
_OLMPLA24hIntTxLow_Object = MibTableColumn
oLMPLA24hIntTxLow = _OLMPLA24hIntTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 6),
    _OLMPLA24hIntTxLow_Type()
)
oLMPLA24hIntTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntTxLow.setStatus("current")
_OLMPLA24hIntTxHigh_Type = Gauge32
_OLMPLA24hIntTxHigh_Object = MibTableColumn
oLMPLA24hIntTxHigh = _OLMPLA24hIntTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 7),
    _OLMPLA24hIntTxHigh_Type()
)
oLMPLA24hIntTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntTxHigh.setStatus("current")
_OLMPLA24hIntRxIntrusion_Type = Gauge32
_OLMPLA24hIntRxIntrusion_Object = MibTableColumn
oLMPLA24hIntRxIntrusion = _OLMPLA24hIntRxIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 8),
    _OLMPLA24hIntRxIntrusion_Type()
)
oLMPLA24hIntRxIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntRxIntrusion.setStatus("current")
_OLMPLA24hIntTxIntrusion_Type = Gauge32
_OLMPLA24hIntTxIntrusion_Object = MibTableColumn
oLMPLA24hIntTxIntrusion = _OLMPLA24hIntTxIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 9),
    _OLMPLA24hIntTxIntrusion_Type()
)
oLMPLA24hIntTxIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntTxIntrusion.setStatus("current")
_OLMPLA24hIntValidData_Type = TruthValue
_OLMPLA24hIntValidData_Object = MibTableColumn
oLMPLA24hIntValidData = _OLMPLA24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 10),
    _OLMPLA24hIntValidData_Type()
)
oLMPLA24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntValidData.setStatus("current")
_OLMPLA24hIntTimeStamp_Type = DateAndTime
_OLMPLA24hIntTimeStamp_Object = MibTableColumn
oLMPLA24hIntTimeStamp = _OLMPLA24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 11),
    _OLMPLA24hIntTimeStamp_Type()
)
oLMPLA24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntTimeStamp.setStatus("current")
_OLMPLA24hIntRxLowMon_Type = Gauge32
_OLMPLA24hIntRxLowMon_Object = MibTableColumn
oLMPLA24hIntRxLowMon = _OLMPLA24hIntRxLowMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 12),
    _OLMPLA24hIntRxLowMon_Type()
)
oLMPLA24hIntRxLowMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntRxLowMon.setStatus("current")
_OLMPLA24hIntRxHighMon_Type = Gauge32
_OLMPLA24hIntRxHighMon_Object = MibTableColumn
oLMPLA24hIntRxHighMon = _OLMPLA24hIntRxHighMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 13),
    _OLMPLA24hIntRxHighMon_Type()
)
oLMPLA24hIntRxHighMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntRxHighMon.setStatus("current")
_OLMPLA24hIntTxLowMon_Type = Gauge32
_OLMPLA24hIntTxLowMon_Object = MibTableColumn
oLMPLA24hIntTxLowMon = _OLMPLA24hIntTxLowMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 14),
    _OLMPLA24hIntTxLowMon_Type()
)
oLMPLA24hIntTxLowMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntTxLowMon.setStatus("current")
_OLMPLA24hIntTxHighMon_Type = Gauge32
_OLMPLA24hIntTxHighMon_Object = MibTableColumn
oLMPLA24hIntTxHighMon = _OLMPLA24hIntTxHighMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 2, 1, 15),
    _OLMPLA24hIntTxHighMon_Type()
)
oLMPLA24hIntTxHighMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA24hIntTxHighMon.setStatus("current")
_OLMPLA1weekIntTable_Object = MibTable
oLMPLA1weekIntTable = _OLMPLA1weekIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3)
)
if mibBuilder.loadTexts:
    oLMPLA1weekIntTable.setStatus("current")
_OLMPLA1weekIntEntry_Object = MibTableRow
oLMPLA1weekIntEntry = _OLMPLA1weekIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1)
)
oLMPLA1weekIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "oLMPLA1weekIntIndex"),
)
if mibBuilder.loadTexts:
    oLMPLA1weekIntEntry.setStatus("current")


class _OLMPLA1weekIntIndex_Type(Integer32):
    """Custom type oLMPLA1weekIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_OLMPLA1weekIntIndex_Type.__name__ = "Integer32"
_OLMPLA1weekIntIndex_Object = MibTableColumn
oLMPLA1weekIntIndex = _OLMPLA1weekIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 1),
    _OLMPLA1weekIntIndex_Type()
)
oLMPLA1weekIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oLMPLA1weekIntIndex.setStatus("current")
_OLMPLA1weekIntRxLOS_Type = Gauge32
_OLMPLA1weekIntRxLOS_Object = MibTableColumn
oLMPLA1weekIntRxLOS = _OLMPLA1weekIntRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 2),
    _OLMPLA1weekIntRxLOS_Type()
)
oLMPLA1weekIntRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntRxLOS.setStatus("current")
_OLMPLA1weekIntTxLOS_Type = Gauge32
_OLMPLA1weekIntTxLOS_Object = MibTableColumn
oLMPLA1weekIntTxLOS = _OLMPLA1weekIntTxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 3),
    _OLMPLA1weekIntTxLOS_Type()
)
oLMPLA1weekIntTxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntTxLOS.setStatus("current")
_OLMPLA1weekIntRxLow_Type = Gauge32
_OLMPLA1weekIntRxLow_Object = MibTableColumn
oLMPLA1weekIntRxLow = _OLMPLA1weekIntRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 4),
    _OLMPLA1weekIntRxLow_Type()
)
oLMPLA1weekIntRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntRxLow.setStatus("current")
_OLMPLA1weekIntRxHigh_Type = Gauge32
_OLMPLA1weekIntRxHigh_Object = MibTableColumn
oLMPLA1weekIntRxHigh = _OLMPLA1weekIntRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 5),
    _OLMPLA1weekIntRxHigh_Type()
)
oLMPLA1weekIntRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntRxHigh.setStatus("current")
_OLMPLA1weekIntTxLow_Type = Gauge32
_OLMPLA1weekIntTxLow_Object = MibTableColumn
oLMPLA1weekIntTxLow = _OLMPLA1weekIntTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 6),
    _OLMPLA1weekIntTxLow_Type()
)
oLMPLA1weekIntTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntTxLow.setStatus("current")
_OLMPLA1weekIntTxHigh_Type = Gauge32
_OLMPLA1weekIntTxHigh_Object = MibTableColumn
oLMPLA1weekIntTxHigh = _OLMPLA1weekIntTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 7),
    _OLMPLA1weekIntTxHigh_Type()
)
oLMPLA1weekIntTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntTxHigh.setStatus("current")
_OLMPLA1weekIntRxIntrusion_Type = Gauge32
_OLMPLA1weekIntRxIntrusion_Object = MibTableColumn
oLMPLA1weekIntRxIntrusion = _OLMPLA1weekIntRxIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 8),
    _OLMPLA1weekIntRxIntrusion_Type()
)
oLMPLA1weekIntRxIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntRxIntrusion.setStatus("current")
_OLMPLA1weekIntTxIntrusion_Type = Gauge32
_OLMPLA1weekIntTxIntrusion_Object = MibTableColumn
oLMPLA1weekIntTxIntrusion = _OLMPLA1weekIntTxIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 9),
    _OLMPLA1weekIntTxIntrusion_Type()
)
oLMPLA1weekIntTxIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntTxIntrusion.setStatus("current")
_OLMPLA1weekIntValidData_Type = TruthValue
_OLMPLA1weekIntValidData_Object = MibTableColumn
oLMPLA1weekIntValidData = _OLMPLA1weekIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 10),
    _OLMPLA1weekIntValidData_Type()
)
oLMPLA1weekIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntValidData.setStatus("current")
_OLMPLA1weekIntTimeStamp_Type = DateAndTime
_OLMPLA1weekIntTimeStamp_Object = MibTableColumn
oLMPLA1weekIntTimeStamp = _OLMPLA1weekIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 11),
    _OLMPLA1weekIntTimeStamp_Type()
)
oLMPLA1weekIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntTimeStamp.setStatus("current")
_OLMPLA1weekIntRxLowMon_Type = Gauge32
_OLMPLA1weekIntRxLowMon_Object = MibTableColumn
oLMPLA1weekIntRxLowMon = _OLMPLA1weekIntRxLowMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 12),
    _OLMPLA1weekIntRxLowMon_Type()
)
oLMPLA1weekIntRxLowMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntRxLowMon.setStatus("current")
_OLMPLA1weekIntRxHighMon_Type = Gauge32
_OLMPLA1weekIntRxHighMon_Object = MibTableColumn
oLMPLA1weekIntRxHighMon = _OLMPLA1weekIntRxHighMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 13),
    _OLMPLA1weekIntRxHighMon_Type()
)
oLMPLA1weekIntRxHighMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntRxHighMon.setStatus("current")
_OLMPLA1weekIntTxLowMon_Type = Gauge32
_OLMPLA1weekIntTxLowMon_Object = MibTableColumn
oLMPLA1weekIntTxLowMon = _OLMPLA1weekIntTxLowMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 14),
    _OLMPLA1weekIntTxLowMon_Type()
)
oLMPLA1weekIntTxLowMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntTxLowMon.setStatus("current")
_OLMPLA1weekIntTxHighMon_Type = Gauge32
_OLMPLA1weekIntTxHighMon_Object = MibTableColumn
oLMPLA1weekIntTxHighMon = _OLMPLA1weekIntTxHighMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 3, 1, 15),
    _OLMPLA1weekIntTxHighMon_Type()
)
oLMPLA1weekIntTxHighMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLA1weekIntTxHighMon.setStatus("current")
_OLMPLAcurrentTable_Object = MibTable
oLMPLAcurrentTable = _OLMPLAcurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4)
)
if mibBuilder.loadTexts:
    oLMPLAcurrentTable.setStatus("current")
_OLMPLAcurrentEntry_Object = MibTableRow
oLMPLAcurrentEntry = _OLMPLAcurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1)
)
oLMPLAcurrentEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP2000-R2-MIB", "oLMPLAcurrentIndex"),
)
if mibBuilder.loadTexts:
    oLMPLAcurrentEntry.setStatus("current")


class _OLMPLAcurrentIndex_Type(Integer32):
    """Custom type oLMPLAcurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_OLMPLAcurrentIndex_Type.__name__ = "Integer32"
_OLMPLAcurrentIndex_Object = MibTableColumn
oLMPLAcurrentIndex = _OLMPLAcurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 1),
    _OLMPLAcurrentIndex_Type()
)
oLMPLAcurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oLMPLAcurrentIndex.setStatus("current")
_OLMPLAcurrentRxLOS_Type = Gauge32
_OLMPLAcurrentRxLOS_Object = MibTableColumn
oLMPLAcurrentRxLOS = _OLMPLAcurrentRxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 2),
    _OLMPLAcurrentRxLOS_Type()
)
oLMPLAcurrentRxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentRxLOS.setStatus("current")
_OLMPLAcurrentTxLOS_Type = Gauge32
_OLMPLAcurrentTxLOS_Object = MibTableColumn
oLMPLAcurrentTxLOS = _OLMPLAcurrentTxLOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 3),
    _OLMPLAcurrentTxLOS_Type()
)
oLMPLAcurrentTxLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentTxLOS.setStatus("current")
_OLMPLAcurrentRxLow_Type = Gauge32
_OLMPLAcurrentRxLow_Object = MibTableColumn
oLMPLAcurrentRxLow = _OLMPLAcurrentRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 4),
    _OLMPLAcurrentRxLow_Type()
)
oLMPLAcurrentRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentRxLow.setStatus("current")
_OLMPLAcurrentRxHigh_Type = Gauge32
_OLMPLAcurrentRxHigh_Object = MibTableColumn
oLMPLAcurrentRxHigh = _OLMPLAcurrentRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 5),
    _OLMPLAcurrentRxHigh_Type()
)
oLMPLAcurrentRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentRxHigh.setStatus("current")
_OLMPLAcurrentTxLow_Type = Gauge32
_OLMPLAcurrentTxLow_Object = MibTableColumn
oLMPLAcurrentTxLow = _OLMPLAcurrentTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 6),
    _OLMPLAcurrentTxLow_Type()
)
oLMPLAcurrentTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentTxLow.setStatus("current")
_OLMPLAcurrentTxHigh_Type = Gauge32
_OLMPLAcurrentTxHigh_Object = MibTableColumn
oLMPLAcurrentTxHigh = _OLMPLAcurrentTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 7),
    _OLMPLAcurrentTxHigh_Type()
)
oLMPLAcurrentTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentTxHigh.setStatus("current")
_OLMPLAcurrentRxIntrusion_Type = Gauge32
_OLMPLAcurrentRxIntrusion_Object = MibTableColumn
oLMPLAcurrentRxIntrusion = _OLMPLAcurrentRxIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 8),
    _OLMPLAcurrentRxIntrusion_Type()
)
oLMPLAcurrentRxIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentRxIntrusion.setStatus("current")
_OLMPLAcurrentTxIntrusion_Type = Gauge32
_OLMPLAcurrentTxIntrusion_Object = MibTableColumn
oLMPLAcurrentTxIntrusion = _OLMPLAcurrentTxIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 9),
    _OLMPLAcurrentTxIntrusion_Type()
)
oLMPLAcurrentTxIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentTxIntrusion.setStatus("current")
_OLMPLAcurrentValidData_Type = TruthValue
_OLMPLAcurrentValidData_Object = MibTableColumn
oLMPLAcurrentValidData = _OLMPLAcurrentValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 10),
    _OLMPLAcurrentValidData_Type()
)
oLMPLAcurrentValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentValidData.setStatus("current")
_OLMPLAcurrentElapsedTime_Type = Integer32
_OLMPLAcurrentElapsedTime_Object = MibTableColumn
oLMPLAcurrentElapsedTime = _OLMPLAcurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 11),
    _OLMPLAcurrentElapsedTime_Type()
)
oLMPLAcurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentElapsedTime.setStatus("current")
_OLMPLAcurrentRxLowMon_Type = Gauge32
_OLMPLAcurrentRxLowMon_Object = MibTableColumn
oLMPLAcurrentRxLowMon = _OLMPLAcurrentRxLowMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 12),
    _OLMPLAcurrentRxLowMon_Type()
)
oLMPLAcurrentRxLowMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentRxLowMon.setStatus("current")
_OLMPLAcurrentRxHighMon_Type = Gauge32
_OLMPLAcurrentRxHighMon_Object = MibTableColumn
oLMPLAcurrentRxHighMon = _OLMPLAcurrentRxHighMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 13),
    _OLMPLAcurrentRxHighMon_Type()
)
oLMPLAcurrentRxHighMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentRxHighMon.setStatus("current")
_OLMPLAcurrentTxLowMon_Type = Gauge32
_OLMPLAcurrentTxLowMon_Object = MibTableColumn
oLMPLAcurrentTxLowMon = _OLMPLAcurrentTxLowMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 14),
    _OLMPLAcurrentTxLowMon_Type()
)
oLMPLAcurrentTxLowMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentTxLowMon.setStatus("current")
_OLMPLAcurrentTxHighMon_Type = Gauge32
_OLMPLAcurrentTxHighMon_Object = MibTableColumn
oLMPLAcurrentTxHighMon = _OLMPLAcurrentTxHighMon_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 4, 1, 15),
    _OLMPLAcurrentTxHighMon_Type()
)
oLMPLAcurrentTxHighMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oLMPLAcurrentTxHighMon.setStatus("current")
_EdfaPLA15minIntTable_Object = MibTable
edfaPLA15minIntTable = _EdfaPLA15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 5)
)
if mibBuilder.loadTexts:
    edfaPLA15minIntTable.setStatus("current")
_EdfaPLA15minIntEntry_Object = MibTableRow
edfaPLA15minIntEntry = _EdfaPLA15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 5, 1)
)
edfaPLA15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "edfaPLA15minIntIndex"),
)
if mibBuilder.loadTexts:
    edfaPLA15minIntEntry.setStatus("current")


class _EdfaPLA15minIntIndex_Type(Integer32):
    """Custom type edfaPLA15minIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EdfaPLA15minIntIndex_Type.__name__ = "Integer32"
_EdfaPLA15minIntIndex_Object = MibTableColumn
edfaPLA15minIntIndex = _EdfaPLA15minIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 5, 1, 1),
    _EdfaPLA15minIntIndex_Type()
)
edfaPLA15minIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    edfaPLA15minIntIndex.setStatus("current")
_EdfaPLA15minIntValidData_Type = TruthValue
_EdfaPLA15minIntValidData_Object = MibTableColumn
edfaPLA15minIntValidData = _EdfaPLA15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 5, 1, 2),
    _EdfaPLA15minIntValidData_Type()
)
edfaPLA15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntValidData.setStatus("current")
_EdfaPLA15minIntTimeStamp_Type = DateAndTime
_EdfaPLA15minIntTimeStamp_Object = MibTableColumn
edfaPLA15minIntTimeStamp = _EdfaPLA15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 5, 1, 3),
    _EdfaPLA15minIntTimeStamp_Type()
)
edfaPLA15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntTimeStamp.setStatus("current")
_EdfaPLA15minIntES_Type = Gauge32
_EdfaPLA15minIntES_Object = MibTableColumn
edfaPLA15minIntES = _EdfaPLA15minIntES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 5, 1, 4),
    _EdfaPLA15minIntES_Type()
)
edfaPLA15minIntES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntES.setStatus("current")
_EdfaPLA15minIntLossOfSignal_Type = Gauge32
_EdfaPLA15minIntLossOfSignal_Object = MibTableColumn
edfaPLA15minIntLossOfSignal = _EdfaPLA15minIntLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 5, 1, 5),
    _EdfaPLA15minIntLossOfSignal_Type()
)
edfaPLA15minIntLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntLossOfSignal.setStatus("current")
_EdfaPLA15minIntLossOfOop_Type = Gauge32
_EdfaPLA15minIntLossOfOop_Object = MibTableColumn
edfaPLA15minIntLossOfOop = _EdfaPLA15minIntLossOfOop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 5, 1, 6),
    _EdfaPLA15minIntLossOfOop_Type()
)
edfaPLA15minIntLossOfOop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA15minIntLossOfOop.setStatus("current")
_EdfaPLA24hIntTable_Object = MibTable
edfaPLA24hIntTable = _EdfaPLA24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 6)
)
if mibBuilder.loadTexts:
    edfaPLA24hIntTable.setStatus("current")
_EdfaPLA24hIntEntry_Object = MibTableRow
edfaPLA24hIntEntry = _EdfaPLA24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 6, 1)
)
edfaPLA24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "edfaPLA24hIntIndex"),
)
if mibBuilder.loadTexts:
    edfaPLA24hIntEntry.setStatus("current")


class _EdfaPLA24hIntIndex_Type(Integer32):
    """Custom type edfaPLA24hIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_EdfaPLA24hIntIndex_Type.__name__ = "Integer32"
_EdfaPLA24hIntIndex_Object = MibTableColumn
edfaPLA24hIntIndex = _EdfaPLA24hIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 6, 1, 1),
    _EdfaPLA24hIntIndex_Type()
)
edfaPLA24hIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    edfaPLA24hIntIndex.setStatus("current")
_EdfaPLA24hIntValidData_Type = TruthValue
_EdfaPLA24hIntValidData_Object = MibTableColumn
edfaPLA24hIntValidData = _EdfaPLA24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 6, 1, 2),
    _EdfaPLA24hIntValidData_Type()
)
edfaPLA24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntValidData.setStatus("current")
_EdfaPLA24hIntTimeStamp_Type = DateAndTime
_EdfaPLA24hIntTimeStamp_Object = MibTableColumn
edfaPLA24hIntTimeStamp = _EdfaPLA24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 6, 1, 3),
    _EdfaPLA24hIntTimeStamp_Type()
)
edfaPLA24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntTimeStamp.setStatus("current")
_EdfaPLA24hIntES_Type = Gauge32
_EdfaPLA24hIntES_Object = MibTableColumn
edfaPLA24hIntES = _EdfaPLA24hIntES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 6, 1, 4),
    _EdfaPLA24hIntES_Type()
)
edfaPLA24hIntES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntES.setStatus("current")
_EdfaPLA24hIntLossOfSignal_Type = Gauge32
_EdfaPLA24hIntLossOfSignal_Object = MibTableColumn
edfaPLA24hIntLossOfSignal = _EdfaPLA24hIntLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 6, 1, 5),
    _EdfaPLA24hIntLossOfSignal_Type()
)
edfaPLA24hIntLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntLossOfSignal.setStatus("current")
_EdfaPLA24hIntLossOfOop_Type = Gauge32
_EdfaPLA24hIntLossOfOop_Object = MibTableColumn
edfaPLA24hIntLossOfOop = _EdfaPLA24hIntLossOfOop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 6, 1, 6),
    _EdfaPLA24hIntLossOfOop_Type()
)
edfaPLA24hIntLossOfOop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA24hIntLossOfOop.setStatus("current")
_EdfaPLA1weekIntTable_Object = MibTable
edfaPLA1weekIntTable = _EdfaPLA1weekIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 7)
)
if mibBuilder.loadTexts:
    edfaPLA1weekIntTable.setStatus("current")
_EdfaPLA1weekIntEntry_Object = MibTableRow
edfaPLA1weekIntEntry = _EdfaPLA1weekIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 7, 1)
)
edfaPLA1weekIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "edfaPLA1weekIntIndex"),
)
if mibBuilder.loadTexts:
    edfaPLA1weekIntEntry.setStatus("current")


class _EdfaPLA1weekIntIndex_Type(Integer32):
    """Custom type edfaPLA1weekIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_EdfaPLA1weekIntIndex_Type.__name__ = "Integer32"
_EdfaPLA1weekIntIndex_Object = MibTableColumn
edfaPLA1weekIntIndex = _EdfaPLA1weekIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 7, 1, 1),
    _EdfaPLA1weekIntIndex_Type()
)
edfaPLA1weekIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    edfaPLA1weekIntIndex.setStatus("current")
_EdfaPLA1weekIntValidData_Type = TruthValue
_EdfaPLA1weekIntValidData_Object = MibTableColumn
edfaPLA1weekIntValidData = _EdfaPLA1weekIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 7, 1, 2),
    _EdfaPLA1weekIntValidData_Type()
)
edfaPLA1weekIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA1weekIntValidData.setStatus("current")
_EdfaPLA1weekIntTimeStamp_Type = DateAndTime
_EdfaPLA1weekIntTimeStamp_Object = MibTableColumn
edfaPLA1weekIntTimeStamp = _EdfaPLA1weekIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 7, 1, 3),
    _EdfaPLA1weekIntTimeStamp_Type()
)
edfaPLA1weekIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA1weekIntTimeStamp.setStatus("current")
_EdfaPLA1weekIntES_Type = Gauge32
_EdfaPLA1weekIntES_Object = MibTableColumn
edfaPLA1weekIntES = _EdfaPLA1weekIntES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 7, 1, 4),
    _EdfaPLA1weekIntES_Type()
)
edfaPLA1weekIntES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA1weekIntES.setStatus("current")
_EdfaPLA1weekIntLossOfSignal_Type = Gauge32
_EdfaPLA1weekIntLossOfSignal_Object = MibTableColumn
edfaPLA1weekIntLossOfSignal = _EdfaPLA1weekIntLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 7, 1, 5),
    _EdfaPLA1weekIntLossOfSignal_Type()
)
edfaPLA1weekIntLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA1weekIntLossOfSignal.setStatus("current")
_EdfaPLA1weekIntLossOfOop_Type = Gauge32
_EdfaPLA1weekIntLossOfOop_Object = MibTableColumn
edfaPLA1weekIntLossOfOop = _EdfaPLA1weekIntLossOfOop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 7, 1, 6),
    _EdfaPLA1weekIntLossOfOop_Type()
)
edfaPLA1weekIntLossOfOop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLA1weekIntLossOfOop.setStatus("current")
_EdfaPLAcurrentTable_Object = MibTable
edfaPLAcurrentTable = _EdfaPLAcurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 8)
)
if mibBuilder.loadTexts:
    edfaPLAcurrentTable.setStatus("current")
_EdfaPLAcurrentEntry_Object = MibTableRow
edfaPLAcurrentEntry = _EdfaPLAcurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 8, 1)
)
edfaPLAcurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "edfaPLAcurrentIndex"),
)
if mibBuilder.loadTexts:
    edfaPLAcurrentEntry.setStatus("current")


class _EdfaPLAcurrentIndex_Type(Integer32):
    """Custom type edfaPLAcurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EdfaPLAcurrentIndex_Type.__name__ = "Integer32"
_EdfaPLAcurrentIndex_Object = MibTableColumn
edfaPLAcurrentIndex = _EdfaPLAcurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 8, 1, 1),
    _EdfaPLAcurrentIndex_Type()
)
edfaPLAcurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    edfaPLAcurrentIndex.setStatus("current")
_EdfaPLAcurrentValidData_Type = TruthValue
_EdfaPLAcurrentValidData_Object = MibTableColumn
edfaPLAcurrentValidData = _EdfaPLAcurrentValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 8, 1, 2),
    _EdfaPLAcurrentValidData_Type()
)
edfaPLAcurrentValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLAcurrentValidData.setStatus("current")
_EdfaPLAcurrentElapsedTime_Type = Integer32
_EdfaPLAcurrentElapsedTime_Object = MibTableColumn
edfaPLAcurrentElapsedTime = _EdfaPLAcurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 8, 1, 3),
    _EdfaPLAcurrentElapsedTime_Type()
)
edfaPLAcurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLAcurrentElapsedTime.setStatus("current")
_EdfaPLAcurrentES_Type = Gauge32
_EdfaPLAcurrentES_Object = MibTableColumn
edfaPLAcurrentES = _EdfaPLAcurrentES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 8, 1, 4),
    _EdfaPLAcurrentES_Type()
)
edfaPLAcurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLAcurrentES.setStatus("current")
_EdfaPLAcurrentLossOfSignal_Type = Gauge32
_EdfaPLAcurrentLossOfSignal_Object = MibTableColumn
edfaPLAcurrentLossOfSignal = _EdfaPLAcurrentLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 8, 1, 5),
    _EdfaPLAcurrentLossOfSignal_Type()
)
edfaPLAcurrentLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLAcurrentLossOfSignal.setStatus("current")
_EdfaPLAcurrentLossOfOop_Type = Gauge32
_EdfaPLAcurrentLossOfOop_Object = MibTableColumn
edfaPLAcurrentLossOfOop = _EdfaPLAcurrentLossOfOop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 8, 1, 6),
    _EdfaPLAcurrentLossOfOop_Type()
)
edfaPLAcurrentLossOfOop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPLAcurrentLossOfOop.setStatus("current")
_IfPLA15minIntTable_Object = MibTable
ifPLA15minIntTable = _IfPLA15minIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 9)
)
if mibBuilder.loadTexts:
    ifPLA15minIntTable.setStatus("current")
_IfPLA15minIntEntry_Object = MibTableRow
ifPLA15minIntEntry = _IfPLA15minIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 9, 1)
)
ifPLA15minIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifPLA15minIntIndex"),
)
if mibBuilder.loadTexts:
    ifPLA15minIntEntry.setStatus("current")


class _IfPLA15minIntIndex_Type(Integer32):
    """Custom type ifPLA15minIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IfPLA15minIntIndex_Type.__name__ = "Integer32"
_IfPLA15minIntIndex_Object = MibTableColumn
ifPLA15minIntIndex = _IfPLA15minIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 9, 1, 1),
    _IfPLA15minIntIndex_Type()
)
ifPLA15minIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifPLA15minIntIndex.setStatus("current")
_IfPLA15minIntValidData_Type = TruthValue
_IfPLA15minIntValidData_Object = MibTableColumn
ifPLA15minIntValidData = _IfPLA15minIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 9, 1, 2),
    _IfPLA15minIntValidData_Type()
)
ifPLA15minIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA15minIntValidData.setStatus("current")
_IfPLA15minIntTimeStamp_Type = DateAndTime
_IfPLA15minIntTimeStamp_Object = MibTableColumn
ifPLA15minIntTimeStamp = _IfPLA15minIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 9, 1, 3),
    _IfPLA15minIntTimeStamp_Type()
)
ifPLA15minIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA15minIntTimeStamp.setStatus("current")
_IfPLA15minIntES_Type = Gauge32
_IfPLA15minIntES_Object = MibTableColumn
ifPLA15minIntES = _IfPLA15minIntES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 9, 1, 4),
    _IfPLA15minIntES_Type()
)
ifPLA15minIntES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA15minIntES.setStatus("current")
_IfPLA15minIntLossOfSignal_Type = Gauge32
_IfPLA15minIntLossOfSignal_Object = MibTableColumn
ifPLA15minIntLossOfSignal = _IfPLA15minIntLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 9, 1, 5),
    _IfPLA15minIntLossOfSignal_Type()
)
ifPLA15minIntLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA15minIntLossOfSignal.setStatus("current")
_IfPLA15minIntLossOfSync_Type = Gauge32
_IfPLA15minIntLossOfSync_Object = MibTableColumn
ifPLA15minIntLossOfSync = _IfPLA15minIntLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 9, 1, 6),
    _IfPLA15minIntLossOfSync_Type()
)
ifPLA15minIntLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA15minIntLossOfSync.setStatus("current")
_IfPLA24hIntTable_Object = MibTable
ifPLA24hIntTable = _IfPLA24hIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 10)
)
if mibBuilder.loadTexts:
    ifPLA24hIntTable.setStatus("current")
_IfPLA24hIntEntry_Object = MibTableRow
ifPLA24hIntEntry = _IfPLA24hIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 10, 1)
)
ifPLA24hIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifPLA24hIntIndex"),
)
if mibBuilder.loadTexts:
    ifPLA24hIntEntry.setStatus("current")


class _IfPLA24hIntIndex_Type(Integer32):
    """Custom type ifPLA24hIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IfPLA24hIntIndex_Type.__name__ = "Integer32"
_IfPLA24hIntIndex_Object = MibTableColumn
ifPLA24hIntIndex = _IfPLA24hIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 10, 1, 1),
    _IfPLA24hIntIndex_Type()
)
ifPLA24hIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifPLA24hIntIndex.setStatus("current")
_IfPLA24hIntValidData_Type = TruthValue
_IfPLA24hIntValidData_Object = MibTableColumn
ifPLA24hIntValidData = _IfPLA24hIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 10, 1, 2),
    _IfPLA24hIntValidData_Type()
)
ifPLA24hIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA24hIntValidData.setStatus("current")
_IfPLA24hIntTimeStamp_Type = DateAndTime
_IfPLA24hIntTimeStamp_Object = MibTableColumn
ifPLA24hIntTimeStamp = _IfPLA24hIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 10, 1, 3),
    _IfPLA24hIntTimeStamp_Type()
)
ifPLA24hIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA24hIntTimeStamp.setStatus("current")
_IfPLA24hIntES_Type = Gauge32
_IfPLA24hIntES_Object = MibTableColumn
ifPLA24hIntES = _IfPLA24hIntES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 10, 1, 4),
    _IfPLA24hIntES_Type()
)
ifPLA24hIntES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA24hIntES.setStatus("current")
_IfPLA24hIntLossOfSignal_Type = Gauge32
_IfPLA24hIntLossOfSignal_Object = MibTableColumn
ifPLA24hIntLossOfSignal = _IfPLA24hIntLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 10, 1, 5),
    _IfPLA24hIntLossOfSignal_Type()
)
ifPLA24hIntLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA24hIntLossOfSignal.setStatus("current")
_IfPLA24hIntLossOfSync_Type = Gauge32
_IfPLA24hIntLossOfSync_Object = MibTableColumn
ifPLA24hIntLossOfSync = _IfPLA24hIntLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 10, 1, 6),
    _IfPLA24hIntLossOfSync_Type()
)
ifPLA24hIntLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA24hIntLossOfSync.setStatus("current")
_IfPLA1weekIntTable_Object = MibTable
ifPLA1weekIntTable = _IfPLA1weekIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 11)
)
if mibBuilder.loadTexts:
    ifPLA1weekIntTable.setStatus("current")
_IfPLA1weekIntEntry_Object = MibTableRow
ifPLA1weekIntEntry = _IfPLA1weekIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 11, 1)
)
ifPLA1weekIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifPLA1weekIntIndex"),
)
if mibBuilder.loadTexts:
    ifPLA1weekIntEntry.setStatus("current")


class _IfPLA1weekIntIndex_Type(Integer32):
    """Custom type ifPLA1weekIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_IfPLA1weekIntIndex_Type.__name__ = "Integer32"
_IfPLA1weekIntIndex_Object = MibTableColumn
ifPLA1weekIntIndex = _IfPLA1weekIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 11, 1, 1),
    _IfPLA1weekIntIndex_Type()
)
ifPLA1weekIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifPLA1weekIntIndex.setStatus("current")
_IfPLA1weekIntValidData_Type = TruthValue
_IfPLA1weekIntValidData_Object = MibTableColumn
ifPLA1weekIntValidData = _IfPLA1weekIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 11, 1, 2),
    _IfPLA1weekIntValidData_Type()
)
ifPLA1weekIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA1weekIntValidData.setStatus("current")
_IfPLA1weekIntTimeStamp_Type = DateAndTime
_IfPLA1weekIntTimeStamp_Object = MibTableColumn
ifPLA1weekIntTimeStamp = _IfPLA1weekIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 11, 1, 3),
    _IfPLA1weekIntTimeStamp_Type()
)
ifPLA1weekIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA1weekIntTimeStamp.setStatus("current")
_IfPLA1weekIntES_Type = Gauge32
_IfPLA1weekIntES_Object = MibTableColumn
ifPLA1weekIntES = _IfPLA1weekIntES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 11, 1, 4),
    _IfPLA1weekIntES_Type()
)
ifPLA1weekIntES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA1weekIntES.setStatus("current")
_IfPLA1weekIntLossOfSignal_Type = Gauge32
_IfPLA1weekIntLossOfSignal_Object = MibTableColumn
ifPLA1weekIntLossOfSignal = _IfPLA1weekIntLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 11, 1, 5),
    _IfPLA1weekIntLossOfSignal_Type()
)
ifPLA1weekIntLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA1weekIntLossOfSignal.setStatus("current")
_IfPLA1weekIntLossOfSync_Type = Gauge32
_IfPLA1weekIntLossOfSync_Object = MibTableColumn
ifPLA1weekIntLossOfSync = _IfPLA1weekIntLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 11, 1, 6),
    _IfPLA1weekIntLossOfSync_Type()
)
ifPLA1weekIntLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLA1weekIntLossOfSync.setStatus("current")
_IfPLAcurrentTable_Object = MibTable
ifPLAcurrentTable = _IfPLAcurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 12)
)
if mibBuilder.loadTexts:
    ifPLAcurrentTable.setStatus("current")
_IfPLAcurrentEntry_Object = MibTableRow
ifPLAcurrentEntry = _IfPLAcurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 12, 1)
)
ifPLAcurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP2000-R2-MIB", "ifPLAcurrentIndex"),
)
if mibBuilder.loadTexts:
    ifPLAcurrentEntry.setStatus("current")


class _IfPLAcurrentIndex_Type(Integer32):
    """Custom type ifPLAcurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IfPLAcurrentIndex_Type.__name__ = "Integer32"
_IfPLAcurrentIndex_Object = MibTableColumn
ifPLAcurrentIndex = _IfPLAcurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 12, 1, 1),
    _IfPLAcurrentIndex_Type()
)
ifPLAcurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifPLAcurrentIndex.setStatus("current")
_IfPLAcurrentValidData_Type = TruthValue
_IfPLAcurrentValidData_Object = MibTableColumn
ifPLAcurrentValidData = _IfPLAcurrentValidData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 12, 1, 2),
    _IfPLAcurrentValidData_Type()
)
ifPLAcurrentValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLAcurrentValidData.setStatus("current")
_IfPLAcurrentElapsedTime_Type = Integer32
_IfPLAcurrentElapsedTime_Object = MibTableColumn
ifPLAcurrentElapsedTime = _IfPLAcurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 12, 1, 3),
    _IfPLAcurrentElapsedTime_Type()
)
ifPLAcurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLAcurrentElapsedTime.setStatus("current")
_IfPLAcurrentES_Type = Gauge32
_IfPLAcurrentES_Object = MibTableColumn
ifPLAcurrentES = _IfPLAcurrentES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 12, 1, 4),
    _IfPLAcurrentES_Type()
)
ifPLAcurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLAcurrentES.setStatus("current")
_IfPLAcurrentLossOfSignal_Type = Gauge32
_IfPLAcurrentLossOfSignal_Object = MibTableColumn
ifPLAcurrentLossOfSignal = _IfPLAcurrentLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 12, 1, 5),
    _IfPLAcurrentLossOfSignal_Type()
)
ifPLAcurrentLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLAcurrentLossOfSignal.setStatus("current")
_IfPLAcurrentLossOfSync_Type = Gauge32
_IfPLAcurrentLossOfSync_Object = MibTableColumn
ifPLAcurrentLossOfSync = _IfPLAcurrentLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 2, 3, 12, 1, 6),
    _IfPLAcurrentLossOfSync_Type()
)
ifPLAcurrentLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPLAcurrentLossOfSync.setStatus("current")
_PerformanceMIBConformance_ObjectIdentity = ObjectIdentity
performanceMIBConformance = _PerformanceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 3)
)

# Managed Objects groups

fsp2000Objects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 5, 1)
)
fsp2000Objects.setObjects(
      *(("FSP2000-R2-MIB", "interfaceAlarmReportControlState"),
        ("FSP2000-R2-MIB", "equipmentAlarmReportControlState"),
        ("FSP2000-R2-MIB", "interfaceAlarmSeverityValue"),
        ("FSP2000-R2-MIB", "equipmentAlarmSeverityValue"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "neAlarmAuthFailSource"),
        ("FSP2000-R2-MIB", "neAlarmAuthFailDescription"),
        ("FSP2000-R2-MIB", "neType"),
        ("FSP2000-R2-MIB", "neMibVariant"),
        ("FSP2000-R2-MIB", "neTrapsinkCommunity"),
        ("FSP2000-R2-MIB", "neTrapsinkPort"),
        ("FSP2000-R2-MIB", "neTrapsinkRowStatus"),
        ("FSP2000-R2-MIB", "neManufacturer"),
        ("FSP2000-R2-MIB", "neState"),
        ("FSP2000-R2-MIB", "neEventsLogged"),
        ("FSP2000-R2-MIB", "neEventLogTimeStamp"),
        ("FSP2000-R2-MIB", "neEventLogNotificationOID"),
        ("FSP2000-R2-MIB", "neEventLogIndexTranslation"),
        ("FSP2000-R2-MIB", "neEventLogVarId"),
        ("FSP2000-R2-MIB", "neEventLogVarType"),
        ("FSP2000-R2-MIB", "neEventLogVarInteger32Val"),
        ("FSP2000-R2-MIB", "neEventLogVarIpAddressVal"),
        ("FSP2000-R2-MIB", "neEventLogVarOctetStringVal"),
        ("FSP2000-R2-MIB", "neEventLogVarOidVal"),
        ("FSP2000-R2-MIB", "activeApplicationSwVersion"),
        ("FSP2000-R2-MIB", "inactiveApplicationSwVersion"),
        ("FSP2000-R2-MIB", "activeOperatingSwVersion"),
        ("FSP2000-R2-MIB", "inactiveOperatingSwVersion"),
        ("FSP2000-R2-MIB", "supportFspSwUpgradeTable"),
        ("FSP2000-R2-MIB", "fspSwUpgradeServerIpAddress"),
        ("FSP2000-R2-MIB", "fspSwUpgradeServerLogin"),
        ("FSP2000-R2-MIB", "fspSwUpgradeServerPassword"),
        ("FSP2000-R2-MIB", "fspSwUpgradeServerFileLocation"),
        ("FSP2000-R2-MIB", "fspSwUpgradeFileName"),
        ("FSP2000-R2-MIB", "fspSwUpgradeType"),
        ("FSP2000-R2-MIB", "fspSwUpgradeProtocol"),
        ("FSP2000-R2-MIB", "fspSwUpgradeRequest"),
        ("FSP2000-R2-MIB", "fspSwUpgradeStatus"),
        ("FSP2000-R2-MIB", "neTrapsenderAddress"),
        ("FSP2000-R2-MIB", "snmpWriteAccessRestriction"),
        ("FSP2000-R2-MIB", "snmpWriteAccessNmsName"),
        ("FSP2000-R2-MIB", "neMemorySizeTotal"),
        ("FSP2000-R2-MIB", "neMemorySizeFree"),
        ("FSP2000-R2-MIB", "neStorageDescr"),
        ("FSP2000-R2-MIB", "neStorageCapacity"),
        ("FSP2000-R2-MIB", "neStorageAvailable"),
        ("FSP2000-R2-MIB", "containerState"),
        ("FSP2000-R2-MIB", "containsPhysicalIndex"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"),
        ("FSP2000-R2-MIB", "objectId"),
        ("FSP2000-R2-MIB", "interfaceTTLoopState"),
        ("FSP2000-R2-MIB", "interfaceTTLaserTxConfig"),
        ("FSP2000-R2-MIB", "interfaceTTLaserTxCurrent"),
        ("FSP2000-R2-MIB", "interfaceTTRxClockFreq"),
        ("FSP2000-R2-MIB", "interfaceTTRxClockType"),
        ("FSP2000-R2-MIB", "interfaceTTWavelength"),
        ("FSP2000-R2-MIB", "interfaceTTOpticalInputPower"),
        ("FSP2000-R2-MIB", "interfaceTTOpticalOutputPower"),
        ("FSP2000-R2-MIB", "interfaceTTConnector"),
        ("FSP2000-R2-MIB", "interfaceTTFiberType"),
        ("FSP2000-R2-MIB", "interfaceTTResultDRTranspLow"),
        ("FSP2000-R2-MIB", "interfaceTTResultDRTranspHigh"),
        ("FSP2000-R2-MIB", "interfaceTTIncommingDataRate"),
        ("FSP2000-R2-MIB", "interfaceTTDisparityCtrl"),
        ("FSP2000-R2-MIB", "interfaceTTLaserTxStatus"),
        ("FSP2000-R2-MIB", "interfaceTTLocalLOSSuppression"),
        ("FSP2000-R2-MIB", "interfaceTTLaserTxTempTenth"),
        ("FSP2000-R2-MIB", "electricalInterfaceTxAutoNeg"),
        ("FSP2000-R2-MIB", "electricalInterfaceDuplexMode"),
        ("FSP2000-R2-MIB", "electricalInterfaceLineSpeed"),
        ("FSP2000-R2-MIB", "electricalInterfaceLoopState"),
        ("FSP2000-R2-MIB", "electricalInterfaceRxClockFreq"),
        ("FSP2000-R2-MIB", "electricalInterfaceRxClockType"),
        ("FSP2000-R2-MIB", "edfaInterfaceOpticalBandType"),
        ("FSP2000-R2-MIB", "edfaInterfacePumpLaserTxConfig"),
        ("FSP2000-R2-MIB", "edfaInterfaceOpticalInputPower"),
        ("FSP2000-R2-MIB", "edfaInterfaceOpticalOutputPower"),
        ("FSP2000-R2-MIB", "edfaInterfaceModuleTemp"),
        ("FSP2000-R2-MIB", "edfaInterfacePumpLaserPower"),
        ("FSP2000-R2-MIB", "edfaInterfacePumpLaserCurrent"),
        ("FSP2000-R2-MIB", "edfaInterfacePumpLaserTxTemp"),
        ("FSP2000-R2-MIB", "edfaInterfacePumpLaserConfig"),
        ("FSP2000-R2-MIB", "edfaInterfaceTECCurrent"),
        ("FSP2000-R2-MIB", "edfaInterfaceMaxOperPower"),
        ("FSP2000-R2-MIB", "edfaInterfaceOIPAlarmOnOff"),
        ("FSP2000-R2-MIB", "edfaInterfacePumpLaserTxStatus"),
        ("FSP2000-R2-MIB", "remoteOptSwitchInterfaceLambda"),
        ("FSP2000-R2-MIB", "olmInterfaceLineAttR"),
        ("FSP2000-R2-MIB", "olmInterfaceLineAttT"),
        ("FSP2000-R2-MIB", "moduleCapabilities"),
        ("FSP2000-R2-MIB", "moduleEnvironmentTemp1"),
        ("FSP2000-R2-MIB", "moduleEnvironmentTemp1Max"),
        ("FSP2000-R2-MIB", "moduleVoltage1"),
        ("FSP2000-R2-MIB", "moduleVoltage1Max"),
        ("FSP2000-R2-MIB", "moduleVoltage1Min"),
        ("FSP2000-R2-MIB", "moduleComment"),
        ("FSP2000-R2-MIB", "moduleType"),
        ("FSP2000-R2-MIB", "moduleOfficialName"),
        ("FSP2000-R2-MIB", "wavelengthChannelModuleChannel"),
        ("FSP2000-R2-MIB", "wavelengthChannelModuleScheme"),
        ("FSP2000-R2-MIB", "wavelengthChannelModuleChName"),
        ("FSP2000-R2-MIB", "wdmChannelModuleLowDRTransp"),
        ("FSP2000-R2-MIB", "wdmChannelModuleHighDRTransp"),
        ("FSP2000-R2-MIB", "wdmChannelModuleTMMode"),
        ("FSP2000-R2-MIB", "wdmChannelModuleTMCap"),
        ("FSP2000-R2-MIB", "wdmChannelModuleTMCurrentCap"),
        ("FSP2000-R2-MIB", "remoteOptSwitchOperState"),
        ("FSP2000-R2-MIB", "remoteOptSwitchAdminState"),
        ("FSP2000-R2-MIB", "remoteOptSwitchALS"),
        ("FSP2000-R2-MIB", "remoteOptSwitchRevertiveMode"),
        ("FSP2000-R2-MIB", "remoteOptSwitchPreferredLine"),
        ("FSP2000-R2-MIB", "oscModuleVoltage2"),
        ("FSP2000-R2-MIB", "oscModuleVoltage3"),
        ("FSP2000-R2-MIB", "mdxModuleWDMType"),
        ("FSP2000-R2-MIB", "mdxModuleScheme"),
        ("FSP2000-R2-MIB", "mdxModuleChannelRange"),
        ("FSP2000-R2-MIB", "mdxModuleUpgradePort"),
        ("FSP2000-R2-MIB", "bandSplitterModuleScheme"),
        ("FSP2000-R2-MIB", "bandSplitterModuleBandRange"),
        ("FSP2000-R2-MIB", "bandSplitterModuleType"),
        ("FSP2000-R2-MIB", "olmModuleSwitchOver"),
        ("FSP2000-R2-MIB", "olmModuleThreshold"),
        ("FSP2000-R2-MIB", "olmModuleHysteresis"),
        ("FSP2000-R2-MIB", "olmModuleOTDRWindowStatus"),
        ("FSP2000-R2-MIB", "olmModuleOTDRWindowTime"),
        ("FSP2000-R2-MIB", "olmModuleMinThreshold"),
        ("FSP2000-R2-MIB", "olmModuleMaxThreshold"),
        ("FSP2000-R2-MIB", "sfpTransceiverApprovedByADVA"),
        ("FSP2000-R2-MIB", "sfpTransceiverLinkLength"),
        ("FSP2000-R2-MIB", "sfpTransceiverChannelName"),
        ("FSP2000-R2-MIB", "sfpTransceiverWaveLengthScheme"),
        ("FSP2000-R2-MIB", "interleaverModuleType"),
        ("FSP2000-R2-MIB", "interleaverModuleSpacing"),
        ("FSP2000-R2-MIB", "channelFilterModuleScheme"),
        ("FSP2000-R2-MIB", "channelFilterModuleChannelName"))
)
if mibBuilder.loadTexts:
    fsp2000Objects.setStatus("current")

fsp2000DeprecatedObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 5, 3)
)
fsp2000DeprecatedObjects.setObjects(
      *(("FSP2000-R2-MIB", "wavelengthChannelModuleRegState"),
        ("FSP2000-R2-MIB", "neSNMPSet"),
        ("FSP2000-R2-MIB", "interfaceTTLaserTxTemp"))
)
if mibBuilder.loadTexts:
    fsp2000DeprecatedObjects.setStatus("deprecated")

performanceMIBObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 6, 3, 1)
)
performanceMIBObjects.setObjects(
      *(("FSP2000-R2-MIB", "olmPPHWthresholdLowAtt"),
        ("FSP2000-R2-MIB", "olmPPHWthresholdHighAtt"),
        ("FSP2000-R2-MIB", "oLMPPthresholdAttGradient"),
        ("FSP2000-R2-MIB", "oLMIfPPthresholdLowTxAtt"),
        ("FSP2000-R2-MIB", "oLMIfPPthresholdHighTxAtt"),
        ("FSP2000-R2-MIB", "oLMIfPPthresholdLowRxAtt"),
        ("FSP2000-R2-MIB", "oLMIfPPthresholdHighRxAtt"),
        ("FSP2000-R2-MIB", "edfaPPthresholdHighPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPPthresholdLowOIP"),
        ("FSP2000-R2-MIB", "edfaPPthresholdHighOIP"),
        ("FSP2000-R2-MIB", "edfaPPthresholdHighTempProt"),
        ("FSP2000-R2-MIB", "ifTTPPthresholdLowLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPPthresholdHighLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPPthresholdLowOIP"),
        ("FSP2000-R2-MIB", "ifTTPPthresholdHighOIP"),
        ("FSP2000-R2-MIB", "ifTTPPthresholdLowOOP"),
        ("FSP2000-R2-MIB", "ifTTPPthresholdHighOOP"),
        ("FSP2000-R2-MIB", "ifTTPPthresholdLowLaserTemp"),
        ("FSP2000-R2-MIB", "ifTTPPthresholdHighLaserTemp"),
        ("FSP2000-R2-MIB", "modulePPthresholdLowVolt"),
        ("FSP2000-R2-MIB", "modulePPthresholdHighVolt"),
        ("FSP2000-R2-MIB", "modulePPthresholdLowTemp"),
        ("FSP2000-R2-MIB", "modulePPthresholdHighTemp"),
        ("FSP2000-R2-MIB", "modulePerformanceStatusAvail"),
        ("FSP2000-R2-MIB", "modulePerformanceStatusLength"),
        ("FSP2000-R2-MIB", "ifPerformanceStatusAvail"),
        ("FSP2000-R2-MIB", "ifPerformanceStatusLength"),
        ("FSP2000-R2-MIB", "oLMPLP15minIntAverageRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP15minIntMinRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP15minIntMaxRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP15minIntAverageTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP15minIntMinTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP15minIntMaxTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP15minIntValidData"),
        ("FSP2000-R2-MIB", "oLMPLP15minIntTimeStamp"),
        ("FSP2000-R2-MIB", "oLMPLP24hIntAverageRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP24hIntMinRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP24hIntMaxRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP24hIntAverageTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP24hIntMinTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP24hIntMaxTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP24hIntValidData"),
        ("FSP2000-R2-MIB", "oLMPLP24hIntTimeStamp"),
        ("FSP2000-R2-MIB", "oLMPLP1weekIntAverageRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP1weekIntMinRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP1weekIntMaxRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP1weekIntAverageTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP1weekIntMinTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP1weekIntMaxTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLP1weekIntValidData"),
        ("FSP2000-R2-MIB", "oLMPLP1weekIntTimeStamp"),
        ("FSP2000-R2-MIB", "oLMPLPcurrentAverageRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLPcurrentMinRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLPcurrentMaxRxAtt"),
        ("FSP2000-R2-MIB", "oLMPLPcurrentAverageTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLPcurrentMinTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLPcurrentMaxTxAtt"),
        ("FSP2000-R2-MIB", "oLMPLPcurrentValidData"),
        ("FSP2000-R2-MIB", "oLMPLPcurrentElapsedTime"),
        ("FSP2000-R2-MIB", "edfaPLP15minIntAveragePumpCurr"),
        ("FSP2000-R2-MIB", "edfaPLP15minIntMinPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLP15minIntMaxPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLP15minIntAverageOIP"),
        ("FSP2000-R2-MIB", "edfaPLP15minIntMinOIP"),
        ("FSP2000-R2-MIB", "edfaPLP15minIntMaxOIP"),
        ("FSP2000-R2-MIB", "edfaPLP15minIntValidData"),
        ("FSP2000-R2-MIB", "edfaPLP15minIntTimeStamp"),
        ("FSP2000-R2-MIB", "edfaPLP24hIntAveragePumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLP24hIntMinPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLP24hIntMaxPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLP24hIntAverageOIP"),
        ("FSP2000-R2-MIB", "edfaPLP24hIntMinOIP"),
        ("FSP2000-R2-MIB", "edfaPLP24hIntMaxOIP"),
        ("FSP2000-R2-MIB", "edfaPLP24hIntValidData"),
        ("FSP2000-R2-MIB", "edfaPLP24hIntTimeStamp"),
        ("FSP2000-R2-MIB", "edfaPLP1weekIntAveragePumpCurr"),
        ("FSP2000-R2-MIB", "edfaPLP1weekIntMinPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLP1weekIntMaxPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLP1weekIntAverageOIP"),
        ("FSP2000-R2-MIB", "edfaPLP1weekIntMinOIP"),
        ("FSP2000-R2-MIB", "edfaPLP1weekIntMaxOIP"),
        ("FSP2000-R2-MIB", "edfaPLP1weekIntValidData"),
        ("FSP2000-R2-MIB", "edfaPLP1weekIntTimeStamp"),
        ("FSP2000-R2-MIB", "edfaPLPcurrentAveragePumpCurr"),
        ("FSP2000-R2-MIB", "edfaPLPcurrentMinPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLPcurrentMaxPumpCurrent"),
        ("FSP2000-R2-MIB", "edfaPLPcurrentAverageOIP"),
        ("FSP2000-R2-MIB", "edfaPLPcurrentMinOIP"),
        ("FSP2000-R2-MIB", "edfaPLPcurrentMaxOIP"),
        ("FSP2000-R2-MIB", "edfaPLPcurrentValidData"),
        ("FSP2000-R2-MIB", "edfaPLPcurrentElapsedTime"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntAverageLaserCurr"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntMinLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntMaxLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntAverageOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntMinOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntMaxOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntAverageOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntMinOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntMaxOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntValidData"),
        ("FSP2000-R2-MIB", "ifTTPLP15minIntTimeStamp"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntAverageLaserCurr"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntMinLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntMaxLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntAverageOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntMinOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntMaxOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntAverageOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntMinOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntMaxOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntValidData"),
        ("FSP2000-R2-MIB", "ifTTPLP24hIntTimeStamp"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntAverageLaserCurr"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntMinLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntMaxLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntAverageOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntMinOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntMaxOIP"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntAverageOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntMinOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntMaxOOP"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntValidData"),
        ("FSP2000-R2-MIB", "ifTTPLP1weekIntTimeStamp"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentAverageLaserCurr"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentMinLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentMaxLaserCurrent"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentAverageOIP"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentMinOIP"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentMaxOIP"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentAverageOOP"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentMinOOP"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentMaxOOP"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentValidData"),
        ("FSP2000-R2-MIB", "ifTTPLPcurrentElapsedTime"),
        ("FSP2000-R2-MIB", "modulePLP15minIntAverageTemp"),
        ("FSP2000-R2-MIB", "modulePLP15minIntMinTemp"),
        ("FSP2000-R2-MIB", "modulePLP15minIntMaxTemp"),
        ("FSP2000-R2-MIB", "modulePLP15minIntAverageVoltage"),
        ("FSP2000-R2-MIB", "modulePLP15minIntMinVoltage"),
        ("FSP2000-R2-MIB", "modulePLP15minIntMaxVoltage"),
        ("FSP2000-R2-MIB", "modulePLP15minIntValidData"),
        ("FSP2000-R2-MIB", "modulePLP15minIntTimeStamp"),
        ("FSP2000-R2-MIB", "modulePLP24hIntAverageTemp"),
        ("FSP2000-R2-MIB", "modulePLP24hIntMinTemp"),
        ("FSP2000-R2-MIB", "modulePLP24hIntMaxTemp"),
        ("FSP2000-R2-MIB", "modulePLP24hIntAverageVoltage"),
        ("FSP2000-R2-MIB", "modulePLP24hIntMinVoltage"),
        ("FSP2000-R2-MIB", "modulePLP24hIntMaxVoltage"),
        ("FSP2000-R2-MIB", "modulePLP24hIntValidData"),
        ("FSP2000-R2-MIB", "modulePLP24hIntTimeStamp"),
        ("FSP2000-R2-MIB", "modulePLP1weekIntAverageTemp"),
        ("FSP2000-R2-MIB", "modulePLP1weekIntMinTemp"),
        ("FSP2000-R2-MIB", "modulePLP1weekIntMaxTemp"),
        ("FSP2000-R2-MIB", "modulePLP1weekIntAverageVoltage"),
        ("FSP2000-R2-MIB", "modulePLP1weekIntMinVoltage"),
        ("FSP2000-R2-MIB", "modulePLP1weekIntMaxVoltage"),
        ("FSP2000-R2-MIB", "modulePLP1weekIntValidData"),
        ("FSP2000-R2-MIB", "modulePLP1weekIntTimeStamp"),
        ("FSP2000-R2-MIB", "modulePLPcurrentAverageTemp"),
        ("FSP2000-R2-MIB", "modulePLPcurrentMinTemp"),
        ("FSP2000-R2-MIB", "modulePLPcurrentMaxTemp"),
        ("FSP2000-R2-MIB", "modulePLPcurrentAverageVoltage"),
        ("FSP2000-R2-MIB", "modulePLPcurrentMinVoltage"),
        ("FSP2000-R2-MIB", "modulePLPcurrentMaxVoltage"),
        ("FSP2000-R2-MIB", "modulePLPcurrentValidData"),
        ("FSP2000-R2-MIB", "modulePLPcurrentElapsedTime"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntRxLOS"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntTxLOS"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntRxLow"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntRxHigh"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntTxLow"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntTxHigh"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntRxIntrusion"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntTxIntrusion"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntValidData"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntTimeStamp"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntRxLowMon"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntRxHighMon"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntTxLowMon"),
        ("FSP2000-R2-MIB", "oLMPLA15minIntTxHighMon"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntRxLOS"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntTxLOS"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntRxLow"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntRxHigh"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntTxLow"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntTxHigh"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntRxIntrusion"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntTxIntrusion"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntValidData"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntTimeStamp"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntRxLowMon"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntRxHighMon"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntTxLowMon"),
        ("FSP2000-R2-MIB", "oLMPLA24hIntTxHighMon"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntRxLOS"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntTxLOS"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntRxLow"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntRxHigh"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntTxLow"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntTxHigh"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntRxIntrusion"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntTxIntrusion"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntValidData"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntTimeStamp"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntRxLowMon"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntRxHighMon"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntTxLowMon"),
        ("FSP2000-R2-MIB", "oLMPLA1weekIntTxHighMon"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentRxLOS"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentTxLOS"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentRxLow"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentRxHigh"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentTxLow"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentTxHigh"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentRxIntrusion"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentTxIntrusion"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentValidData"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentElapsedTime"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentRxLowMon"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentRxHighMon"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentTxLowMon"),
        ("FSP2000-R2-MIB", "oLMPLAcurrentTxHighMon"),
        ("FSP2000-R2-MIB", "edfaPLA15minIntValidData"),
        ("FSP2000-R2-MIB", "edfaPLA15minIntTimeStamp"),
        ("FSP2000-R2-MIB", "edfaPLA15minIntES"),
        ("FSP2000-R2-MIB", "edfaPLA15minIntLossOfSignal"),
        ("FSP2000-R2-MIB", "edfaPLA15minIntLossOfOop"),
        ("FSP2000-R2-MIB", "edfaPLA24hIntValidData"),
        ("FSP2000-R2-MIB", "edfaPLA24hIntTimeStamp"),
        ("FSP2000-R2-MIB", "edfaPLA24hIntES"),
        ("FSP2000-R2-MIB", "edfaPLA24hIntLossOfSignal"),
        ("FSP2000-R2-MIB", "edfaPLA24hIntLossOfOop"),
        ("FSP2000-R2-MIB", "edfaPLA1weekIntValidData"),
        ("FSP2000-R2-MIB", "edfaPLA1weekIntTimeStamp"),
        ("FSP2000-R2-MIB", "edfaPLA1weekIntES"),
        ("FSP2000-R2-MIB", "edfaPLA1weekIntLossOfSignal"),
        ("FSP2000-R2-MIB", "edfaPLA1weekIntLossOfOop"),
        ("FSP2000-R2-MIB", "edfaPLAcurrentValidData"),
        ("FSP2000-R2-MIB", "edfaPLAcurrentElapsedTime"),
        ("FSP2000-R2-MIB", "edfaPLAcurrentES"),
        ("FSP2000-R2-MIB", "edfaPLAcurrentLossOfSignal"),
        ("FSP2000-R2-MIB", "edfaPLAcurrentLossOfOop"),
        ("FSP2000-R2-MIB", "ifPLA15minIntValidData"),
        ("FSP2000-R2-MIB", "ifPLA15minIntTimeStamp"),
        ("FSP2000-R2-MIB", "ifPLA15minIntES"),
        ("FSP2000-R2-MIB", "ifPLA15minIntLossOfSignal"),
        ("FSP2000-R2-MIB", "ifPLA15minIntLossOfSync"),
        ("FSP2000-R2-MIB", "ifPLA24hIntValidData"),
        ("FSP2000-R2-MIB", "ifPLA24hIntTimeStamp"),
        ("FSP2000-R2-MIB", "ifPLA24hIntES"),
        ("FSP2000-R2-MIB", "ifPLA24hIntLossOfSignal"),
        ("FSP2000-R2-MIB", "ifPLA24hIntLossOfSync"),
        ("FSP2000-R2-MIB", "ifPLA1weekIntValidData"),
        ("FSP2000-R2-MIB", "ifPLA1weekIntTimeStamp"),
        ("FSP2000-R2-MIB", "ifPLA1weekIntES"),
        ("FSP2000-R2-MIB", "ifPLA1weekIntLossOfSignal"),
        ("FSP2000-R2-MIB", "ifPLA1weekIntLossOfSync"),
        ("FSP2000-R2-MIB", "ifPLAcurrentValidData"),
        ("FSP2000-R2-MIB", "ifPLAcurrentElapsedTime"),
        ("FSP2000-R2-MIB", "ifPLAcurrentES"),
        ("FSP2000-R2-MIB", "ifPLAcurrentLossOfSignal"),
        ("FSP2000-R2-MIB", "ifPLAcurrentLossOfSync"))
)
if mibBuilder.loadTexts:
    performanceMIBObjects.setStatus("current")


# Notification objects

neTrapsinkTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 1)
)
neTrapsinkTest.setObjects(
      *(("FSP2000-R2-MIB", "neTrapsinkAddress"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neTrapsinkTest.setStatus(
        "current"
    )

equipmentHolderObjectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 2)
)
equipmentHolderObjectCreation.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentHolderObjectCreation.setStatus(
        "current"
    )

equipmentHolderObjectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 3)
)
equipmentHolderObjectDeletion.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentHolderObjectDeletion.setStatus(
        "current"
    )

containerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 4)
)
containerStateChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "containsPhysicalIndex"),
        ("FSP2000-R2-MIB", "containerState"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    containerStateChange.setStatus(
        "current"
    )

neAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 5)
)
neAttributeValueChange.setObjects(
      *(("FSP2000-R2-MIB", "objectId"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neAttributeValueChange.setStatus(
        "current"
    )

interfaceAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 6)
)
interfaceAttributeValueChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "objectId"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAttributeValueChange.setStatus(
        "current"
    )

equipmentAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 7)
)
equipmentAttributeValueChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "objectId"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAttributeValueChange.setStatus(
        "current"
    )

neAuthentificationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 8)
)
neAuthentificationFail.setObjects(
      *(("FSP2000-R2-MIB", "neAlarmAuthFailSource"),
        ("FSP2000-R2-MIB", "neAlarmAuthFailDescription"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neAuthentificationFail.setStatus(
        "current"
    )

neINNCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 9)
)
neINNCDown.setObjects(
      *(("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neINNCDown.setStatus(
        "current"
    )

neINNCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 10)
)
neINNCUp.setObjects(
      *(("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neINNCUp.setStatus(
        "current"
    )

neSoftwareUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 13)
)
neSoftwareUpdate.setObjects(
      *(("FSP2000-R2-MIB", "neState"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neSoftwareUpdate.setStatus(
        "current"
    )

neStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 14)
)
neStateChange.setObjects(
      *(("FSP2000-R2-MIB", "objectId"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neStateChange.setStatus(
        "current"
    )

interfaceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 15)
)
interfaceStateChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "objectId"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceStateChange.setStatus(
        "current"
    )

equipmentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 16)
)
equipmentStateChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "objectId"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentStateChange.setStatus(
        "current"
    )

resetAllTelemetryOutputs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 17)
)
resetAllTelemetryOutputs.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    resetAllTelemetryOutputs.setStatus(
        "current"
    )

interfaceAlarmSeverityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 18)
)
interfaceAlarmSeverityChange.setObjects(
      *(("FSP2000-R2-MIB", "interfaceAlarmSeverityType"),
        ("FSP2000-R2-MIB", "interfaceAlarmSeverityValue"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmSeverityChange.setStatus(
        "current"
    )

equipmentAlarmSeverityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 19)
)
equipmentAlarmSeverityChange.setObjects(
      *(("FSP2000-R2-MIB", "equipmentAlarmSeverityType"),
        ("FSP2000-R2-MIB", "equipmentAlarmSeverityValue"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmSeverityChange.setStatus(
        "current"
    )

neTrapsinkObjectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 20)
)
neTrapsinkObjectCreation.setObjects(
      *(("FSP2000-R2-MIB", "neTrapsinkAddress"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neTrapsinkObjectCreation.setStatus(
        "current"
    )

neTrapsinkObjectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 21)
)
neTrapsinkObjectDeletion.setObjects(
      *(("FSP2000-R2-MIB", "neTrapsinkAddress"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neTrapsinkObjectDeletion.setStatus(
        "current"
    )

neSNMPWriteAccessObjectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 22)
)
neSNMPWriteAccessObjectCreation.setObjects(
      *(("FSP2000-R2-MIB", "snmpWriteAccessNmsAddress"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neSNMPWriteAccessObjectCreation.setStatus(
        "current"
    )

neSNMPWriteAccessObjectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 23)
)
neSNMPWriteAccessObjectDeletion.setObjects(
      *(("FSP2000-R2-MIB", "snmpWriteAccessNmsAddress"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    neSNMPWriteAccessObjectDeletion.setStatus(
        "current"
    )

interfaceAlarmLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 500)
)
interfaceAlarmLossOfSignal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfSignal.setStatus(
        "current"
    )

interfaceAlarmNoLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 501)
)
interfaceAlarmNoLossOfSignal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfSignal.setStatus(
        "current"
    )

interfaceAlarmLossOfLinkPulse = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 502)
)
interfaceAlarmLossOfLinkPulse.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfLinkPulse.setStatus(
        "current"
    )

interfaceAlarmNoLossOfLinkPulse = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 503)
)
interfaceAlarmNoLossOfLinkPulse.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfLinkPulse.setStatus(
        "current"
    )

interfaceAlarmLossOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 504)
)
interfaceAlarmLossOfSync.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfSync.setStatus(
        "current"
    )

interfaceAlarmNoLossOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 505)
)
interfaceAlarmNoLossOfSync.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfSync.setStatus(
        "current"
    )

interfaceAlarmPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 506)
)
interfaceAlarmPartitioned.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmPartitioned.setStatus(
        "current"
    )

interfaceAlarmNoPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 507)
)
interfaceAlarmNoPartitioned.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoPartitioned.setStatus(
        "current"
    )

interfaceAlarmLaserTecEoL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 510)
)
interfaceAlarmLaserTecEoL.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTecEoL.setStatus(
        "current"
    )

interfaceAlarmNoLaserTecEoL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 511)
)
interfaceAlarmNoLaserTecEoL.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLaserTecEoL.setStatus(
        "current"
    )

interfaceAlarmIfModuleTempOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 512)
)
interfaceAlarmIfModuleTempOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmIfModuleTempOoR.setStatus(
        "current"
    )

interfaceAlarmIfModuleTempNotOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 513)
)
interfaceAlarmIfModuleTempNotOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmIfModuleTempNotOoR.setStatus(
        "current"
    )

interfaceAlarmLaserTempOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 514)
)
interfaceAlarmLaserTempOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTempOoR.setStatus(
        "current"
    )

interfaceAlarmLaserTempNotOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 515)
)
interfaceAlarmLaserTempNotOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTempNotOoR.setStatus(
        "current"
    )

interfaceAlarmLossOfOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 516)
)
interfaceAlarmLossOfOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfOOP.setStatus(
        "current"
    )

interfaceAlarmNoLossOfOOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 517)
)
interfaceAlarmNoLossOfOOP.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfOOP.setStatus(
        "current"
    )

interfaceAlarmOIPTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 518)
)
interfaceAlarmOIPTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOIPTooHigh.setStatus(
        "current"
    )

interfaceAlarmOIPNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 519)
)
interfaceAlarmOIPNotTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOIPNotTooHigh.setStatus(
        "current"
    )

interfaceAlarmOOPTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 520)
)
interfaceAlarmOOPTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOOPTooLow.setStatus(
        "current"
    )

interfaceAlarmOOPNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 521)
)
interfaceAlarmOOPNotTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOOPNotTooLow.setStatus(
        "current"
    )

interfaceAlarmLossOfSignalAtT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 526)
)
interfaceAlarmLossOfSignalAtT.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfSignalAtT.setStatus(
        "current"
    )

interfaceAlarmNoLossOfSignalAtT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 527)
)
interfaceAlarmNoLossOfSignalAtT.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfSignalAtT.setStatus(
        "current"
    )

telemetryStateOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 528)
)
telemetryStateOn.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    telemetryStateOn.setStatus(
        "current"
    )

telemetryStateOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 529)
)
telemetryStateOff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    telemetryStateOff.setStatus(
        "current"
    )

interfaceAlarmAttAtRTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 530)
)
interfaceAlarmAttAtRTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttAtRTooHigh.setStatus(
        "current"
    )

interfaceAlarmAttAtRNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 531)
)
interfaceAlarmAttAtRNotTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttAtRNotTooHigh.setStatus(
        "current"
    )

interfaceAlarmAttAtRTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 532)
)
interfaceAlarmAttAtRTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttAtRTooLow.setStatus(
        "current"
    )

interfaceAlarmAttAtRNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 533)
)
interfaceAlarmAttAtRNotTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttAtRNotTooLow.setStatus(
        "current"
    )

interfaceAlarmAttAtTTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 534)
)
interfaceAlarmAttAtTTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttAtTTooHigh.setStatus(
        "current"
    )

interfaceAlarmAttAtTNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 535)
)
interfaceAlarmAttAtTNotTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttAtTNotTooHigh.setStatus(
        "current"
    )

interfaceAlarmAttAtTTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 536)
)
interfaceAlarmAttAtTTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttAtTTooLow.setStatus(
        "current"
    )

interfaceAlarmAttAtTNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 537)
)
interfaceAlarmAttAtTNotTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttAtTNotTooLow.setStatus(
        "current"
    )

interfaceAlarmIntrusionAtR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 538)
)
interfaceAlarmIntrusionAtR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmIntrusionAtR.setStatus(
        "current"
    )

interfaceAlarmNoIntrusionAtR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 539)
)
interfaceAlarmNoIntrusionAtR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoIntrusionAtR.setStatus(
        "current"
    )

interfaceAlarmIntrusionAtT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 540)
)
interfaceAlarmIntrusionAtT.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmIntrusionAtT.setStatus(
        "current"
    )

interfaceAlarmNoIntrusionAtT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 541)
)
interfaceAlarmNoIntrusionAtT.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoIntrusionAtT.setStatus(
        "current"
    )

ifAlarmLaserBiasTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 542)
)
ifAlarmLaserBiasTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    ifAlarmLaserBiasTooLow.setStatus(
        "current"
    )

ifAlarmLaserBiasNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 543)
)
ifAlarmLaserBiasNotTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    ifAlarmLaserBiasNotTooLow.setStatus(
        "current"
    )

ifAlarmLaserBiasTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 544)
)
ifAlarmLaserBiasTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    ifAlarmLaserBiasTooHigh.setStatus(
        "current"
    )

ifAlarmLaserBiasNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 545)
)
ifAlarmLaserBiasNotTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    ifAlarmLaserBiasNotTooHigh.setStatus(
        "current"
    )

interfaceAlarmOIPTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 546)
)
interfaceAlarmOIPTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOIPTooLow.setStatus(
        "current"
    )

interfaceAlarmOIPNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 547)
)
interfaceAlarmOIPNotTooLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOIPNotTooLow.setStatus(
        "current"
    )

interfaceAlarmOOPTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 548)
)
interfaceAlarmOOPTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOOPTooHigh.setStatus(
        "current"
    )

interfaceAlarmOOPNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 549)
)
interfaceAlarmOOPNotTooHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOOPNotTooHigh.setStatus(
        "current"
    )

equipmentAlarmFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 552)
)
equipmentAlarmFanFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanFail.setStatus(
        "current"
    )

equipmentAlarmFanNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 553)
)
equipmentAlarmFanNoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanNoFail.setStatus(
        "current"
    )

equipmentAlarmFanPsFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 554)
)
equipmentAlarmFanPsFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanPsFail.setStatus(
        "current"
    )

equipmentAlarmFanPsNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 555)
)
equipmentAlarmFanPsNoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanPsNoFail.setStatus(
        "current"
    )

equipmentAlarmPsFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 556)
)
equipmentAlarmPsFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmPsFail.setStatus(
        "current"
    )

equipmentAlarmPsNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 557)
)
equipmentAlarmPsNoFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmPsNoFail.setStatus(
        "current"
    )

equipmentAlarmTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 560)
)
equipmentAlarmTempTooHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmTempTooHigh.setStatus(
        "current"
    )

equipmentAlarmTempNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 561)
)
equipmentAlarmTempNotTooHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmTempNotTooHigh.setStatus(
        "current"
    )

equipmentAlarmTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 562)
)
equipmentAlarmTempTooLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmTempTooLow.setStatus(
        "current"
    )

equipmentAlarmTempNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 563)
)
equipmentAlarmTempNotTooLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmTempNotTooLow.setStatus(
        "current"
    )

equipmentAlarmVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 564)
)
equipmentAlarmVoltageTooHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmVoltageTooHigh.setStatus(
        "current"
    )

equipmentAlarmVoltageNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 565)
)
equipmentAlarmVoltageNotTooHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmVoltageNotTooHigh.setStatus(
        "current"
    )

equipmentAlarmVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 566)
)
equipmentAlarmVoltageTooLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmVoltageTooLow.setStatus(
        "current"
    )

equipmentAlarmVoltageNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 567)
)
equipmentAlarmVoltageNotTooLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    equipmentAlarmVoltageNotTooLow.setStatus(
        "current"
    )

eqAlarmMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 570)
)
eqAlarmMismatch.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    eqAlarmMismatch.setStatus(
        "current"
    )

eqAlarmNoMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 571)
)
eqAlarmNoMismatch.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP2000-R2-MIB", "equipmentCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    eqAlarmNoMismatch.setStatus(
        "current"
    )

interfaceAlarmAttRxMonLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 602)
)
interfaceAlarmAttRxMonLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttRxMonLow.setStatus(
        "current"
    )

interfaceAlarmAttRxMonNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 603)
)
interfaceAlarmAttRxMonNotLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttRxMonNotLow.setStatus(
        "current"
    )

interfaceAlarmAttRxMonHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 604)
)
interfaceAlarmAttRxMonHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttRxMonHigh.setStatus(
        "current"
    )

interfaceAlarmAttRxMonNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 605)
)
interfaceAlarmAttRxMonNotHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttRxMonNotHigh.setStatus(
        "current"
    )

interfaceAlarmAttTxMonLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 606)
)
interfaceAlarmAttTxMonLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttTxMonLow.setStatus(
        "current"
    )

interfaceAlarmAttTxMonNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 607)
)
interfaceAlarmAttTxMonNotLow.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttTxMonNotLow.setStatus(
        "current"
    )

interfaceAlarmAttTxMonHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 608)
)
interfaceAlarmAttTxMonHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttTxMonHigh.setStatus(
        "current"
    )

interfaceAlarmAttTxMonNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 609)
)
interfaceAlarmAttTxMonNotHigh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmAttTxMonNotHigh.setStatus(
        "current"
    )

telemetryInput2StateOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 610)
)
telemetryInput2StateOn.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    telemetryInput2StateOn.setStatus(
        "current"
    )

telemetryInput2StateOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 611)
)
telemetryInput2StateOff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    telemetryInput2StateOff.setStatus(
        "current"
    )

telemetryInput3StateOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 612)
)
telemetryInput3StateOn.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    telemetryInput3StateOn.setStatus(
        "current"
    )

telemetryInput3StateOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 613)
)
telemetryInput3StateOff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    telemetryInput3StateOff.setStatus(
        "current"
    )

interfaceAlarmLaserFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 614)
)
interfaceAlarmLaserFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserFailure.setStatus(
        "current"
    )

interfaceAlarmLaserNoFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 615)
)
interfaceAlarmLaserNoFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserNoFailure.setStatus(
        "current"
    )

interfaceAlarmPumpLaserFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 616)
)
interfaceAlarmPumpLaserFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmPumpLaserFailure.setStatus(
        "current"
    )

interfaceAlarmPumpLaserNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 617)
)
interfaceAlarmPumpLaserNoFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmPumpLaserNoFail.setStatus(
        "current"
    )

interfaceAlarmReceiverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 618)
)
interfaceAlarmReceiverFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmReceiverFailure.setStatus(
        "current"
    )

interfaceAlarmReceiverNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 619)
)
interfaceAlarmReceiverNoFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmReceiverNoFail.setStatus(
        "current"
    )

interfaceAlarmOOPOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 620)
)
interfaceAlarmOOPOoR.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOOPOoR.setStatus(
        "current"
    )

interfaceAlarmOOPNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 621)
)
interfaceAlarmOOPNormal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmOOPNormal.setStatus(
        "current"
    )

ifAlarmTempSafetyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 622)
)
ifAlarmTempSafetyShutdown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    ifAlarmTempSafetyShutdown.setStatus(
        "current"
    )

ifAlarmTempSafetyShutdownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 623)
)
ifAlarmTempSafetyShutdownClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    ifAlarmTempSafetyShutdownClear.setStatus(
        "current"
    )

interfaceAlarmLaserTemp2Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 624)
)
interfaceAlarmLaserTemp2Low.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTemp2Low.setStatus(
        "current"
    )

interfaceAlarmLaserTempNot2Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 625)
)
interfaceAlarmLaserTempNot2Low.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTempNot2Low.setStatus(
        "current"
    )

interfaceAlarmLaserTemp2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 626)
)
interfaceAlarmLaserTemp2High.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTemp2High.setStatus(
        "current"
    )

interfaceAlarmLaserTempNot2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 3, 0, 627)
)
interfaceAlarmLaserTempNot2High.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP2000-R2-MIB", "interfaceCurrentAlarmSeverity"),
        ("FSP2000-R2-MIB", "timeStamp"),
        ("FSP2000-R2-MIB", "indexTranslation"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLaserTempNot2High.setStatus(
        "current"
    )


# Notifications groups

fsp2000Notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7, 2, 5, 2)
)
fsp2000Notifications.setObjects(
      *(("FSP2000-R2-MIB", "neTrapsinkTest"),
        ("FSP2000-R2-MIB", "equipmentHolderObjectCreation"),
        ("FSP2000-R2-MIB", "equipmentHolderObjectDeletion"),
        ("FSP2000-R2-MIB", "neTrapsinkObjectCreation"),
        ("FSP2000-R2-MIB", "neTrapsinkObjectDeletion"),
        ("FSP2000-R2-MIB", "neSNMPWriteAccessObjectCreation"),
        ("FSP2000-R2-MIB", "neSNMPWriteAccessObjectDeletion"),
        ("FSP2000-R2-MIB", "containerStateChange"),
        ("FSP2000-R2-MIB", "neAttributeValueChange"),
        ("FSP2000-R2-MIB", "interfaceAttributeValueChange"),
        ("FSP2000-R2-MIB", "equipmentAttributeValueChange"),
        ("FSP2000-R2-MIB", "neAuthentificationFail"),
        ("FSP2000-R2-MIB", "neINNCDown"),
        ("FSP2000-R2-MIB", "neINNCUp"),
        ("FSP2000-R2-MIB", "neSoftwareUpdate"),
        ("FSP2000-R2-MIB", "neStateChange"),
        ("FSP2000-R2-MIB", "interfaceStateChange"),
        ("FSP2000-R2-MIB", "equipmentStateChange"),
        ("FSP2000-R2-MIB", "resetAllTelemetryOutputs"),
        ("FSP2000-R2-MIB", "interfaceAlarmSeverityChange"),
        ("FSP2000-R2-MIB", "equipmentAlarmSeverityChange"),
        ("FSP2000-R2-MIB", "interfaceAlarmLossOfSignal"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoLossOfSignal"),
        ("FSP2000-R2-MIB", "interfaceAlarmLossOfLinkPulse"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoLossOfLinkPulse"),
        ("FSP2000-R2-MIB", "interfaceAlarmLossOfSync"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoLossOfSync"),
        ("FSP2000-R2-MIB", "interfaceAlarmPartitioned"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoPartitioned"),
        ("FSP2000-R2-MIB", "ifAlarmLaserBiasTooLow"),
        ("FSP2000-R2-MIB", "ifAlarmLaserBiasNotTooLow"),
        ("FSP2000-R2-MIB", "ifAlarmLaserBiasTooHigh"),
        ("FSP2000-R2-MIB", "ifAlarmLaserBiasNotTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserTecEoL"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoLaserTecEoL"),
        ("FSP2000-R2-MIB", "interfaceAlarmIfModuleTempOoR"),
        ("FSP2000-R2-MIB", "interfaceAlarmIfModuleTempNotOoR"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserTempOoR"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserTempNotOoR"),
        ("FSP2000-R2-MIB", "interfaceAlarmLossOfOOP"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoLossOfOOP"),
        ("FSP2000-R2-MIB", "interfaceAlarmOIPTooLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmOIPNotTooLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmOIPTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmOIPNotTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmOOPTooLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmOOPNotTooLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmOOPTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmOOPNotTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmLossOfSignalAtT"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoLossOfSignalAtT"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttAtRTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttAtRNotTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttAtRTooLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttAtRNotTooLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttAtTTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttAtTNotTooHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttAtTTooLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttAtTNotTooLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmIntrusionAtR"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoIntrusionAtR"),
        ("FSP2000-R2-MIB", "interfaceAlarmIntrusionAtT"),
        ("FSP2000-R2-MIB", "interfaceAlarmNoIntrusionAtT"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttRxMonLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttRxMonNotLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttRxMonHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttRxMonNotHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttTxMonLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttTxMonNotLow"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttTxMonHigh"),
        ("FSP2000-R2-MIB", "interfaceAlarmAttTxMonNotHigh"),
        ("FSP2000-R2-MIB", "telemetryStateOn"),
        ("FSP2000-R2-MIB", "telemetryStateOff"),
        ("FSP2000-R2-MIB", "telemetryInput2StateOn"),
        ("FSP2000-R2-MIB", "telemetryInput2StateOff"),
        ("FSP2000-R2-MIB", "telemetryInput3StateOn"),
        ("FSP2000-R2-MIB", "telemetryInput3StateOff"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserFailure"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserNoFailure"),
        ("FSP2000-R2-MIB", "interfaceAlarmPumpLaserFailure"),
        ("FSP2000-R2-MIB", "interfaceAlarmPumpLaserNoFail"),
        ("FSP2000-R2-MIB", "interfaceAlarmReceiverFailure"),
        ("FSP2000-R2-MIB", "interfaceAlarmReceiverNoFail"),
        ("FSP2000-R2-MIB", "interfaceAlarmOOPOoR"),
        ("FSP2000-R2-MIB", "interfaceAlarmOOPNormal"),
        ("FSP2000-R2-MIB", "ifAlarmTempSafetyShutdown"),
        ("FSP2000-R2-MIB", "ifAlarmTempSafetyShutdownClear"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserTemp2Low"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserTempNot2Low"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserTemp2High"),
        ("FSP2000-R2-MIB", "interfaceAlarmLaserTempNot2High"),
        ("FSP2000-R2-MIB", "equipmentAlarmFanFail"),
        ("FSP2000-R2-MIB", "equipmentAlarmFanNoFail"),
        ("FSP2000-R2-MIB", "equipmentAlarmFanPsFail"),
        ("FSP2000-R2-MIB", "equipmentAlarmFanPsNoFail"),
        ("FSP2000-R2-MIB", "equipmentAlarmPsFail"),
        ("FSP2000-R2-MIB", "equipmentAlarmPsNoFail"),
        ("FSP2000-R2-MIB", "equipmentAlarmTempTooHigh"),
        ("FSP2000-R2-MIB", "equipmentAlarmTempNotTooHigh"),
        ("FSP2000-R2-MIB", "equipmentAlarmTempTooLow"),
        ("FSP2000-R2-MIB", "equipmentAlarmTempNotTooLow"),
        ("FSP2000-R2-MIB", "equipmentAlarmVoltageTooHigh"),
        ("FSP2000-R2-MIB", "equipmentAlarmVoltageNotTooHigh"),
        ("FSP2000-R2-MIB", "equipmentAlarmVoltageTooLow"),
        ("FSP2000-R2-MIB", "equipmentAlarmVoltageNotTooLow"),
        ("FSP2000-R2-MIB", "eqAlarmMismatch"),
        ("FSP2000-R2-MIB", "eqAlarmNoMismatch"))
)
if mibBuilder.loadTexts:
    fsp2000Notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSP2000-R2-MIB",
    **{"IndexTranslation": IndexTranslation,
       "ArcState": ArcState,
       "InterfaceAlarmTypes": InterfaceAlarmTypes,
       "EquipmentAlarmTypes": EquipmentAlarmTypes,
       "TrapAlarmSeverity": TrapAlarmSeverity,
       "TrapCounter": TrapCounter,
       "OnOff": OnOff,
       "SwitchAdminState": SwitchAdminState,
       "SwitchOperState": SwitchOperState,
       "AvailState": AvailState,
       "ContainerState": ContainerState,
       "ClockDataRate": ClockDataRate,
       "ClockDataRateBitfield": ClockDataRateBitfield,
       "LaserTxConfig": LaserTxConfig,
       "LaserTxStatus": LaserTxStatus,
       "ModuleType": ModuleType,
       "NEState": NEState,
       "BandScheme": BandScheme,
       "SwUpgradeStatusType": SwUpgradeStatusType,
       "AccessState": AccessState,
       "EnableState": EnableState,
       "TransmissionMode": TransmissionMode,
       "TransmissionModeBitfield": TransmissionModeBitfield,
       "KBytes": KBytes,
       "OLMGradientThreshold": OLMGradientThreshold,
       "fsp2000Products": fsp2000Products,
       "fsp2000V1": fsp2000V1,
       "fsp2000MIB": fsp2000MIB,
       "alarmMIB": alarmMIB,
       "alarmFilters": alarmFilters,
       "interfaceAlarmReportControlTable": interfaceAlarmReportControlTable,
       "interfaceAlarmReportControlEntry": interfaceAlarmReportControlEntry,
       "interfaceAlarmReportControlState": interfaceAlarmReportControlState,
       "equipmentAlarmReportControlTable": equipmentAlarmReportControlTable,
       "equipmentAlarmReportControlEntry": equipmentAlarmReportControlEntry,
       "equipmentAlarmReportControlState": equipmentAlarmReportControlState,
       "interfaceAlarmSeverityTable": interfaceAlarmSeverityTable,
       "interfaceAlarmSeverityEntry": interfaceAlarmSeverityEntry,
       "interfaceAlarmSeverityType": interfaceAlarmSeverityType,
       "interfaceAlarmSeverityValue": interfaceAlarmSeverityValue,
       "equipmentAlarmSeverityTable": equipmentAlarmSeverityTable,
       "equipmentAlarmSeverityEntry": equipmentAlarmSeverityEntry,
       "equipmentAlarmSeverityType": equipmentAlarmSeverityType,
       "equipmentAlarmSeverityValue": equipmentAlarmSeverityValue,
       "currentAlarms": currentAlarms,
       "interfaceCurrentAlarmTable": interfaceCurrentAlarmTable,
       "interfaceCurrentAlarmEntry": interfaceCurrentAlarmEntry,
       "interfaceCurrentAlarmType": interfaceCurrentAlarmType,
       "interfaceCurrentAlarmSeverity": interfaceCurrentAlarmSeverity,
       "equipmentCurrentAlarmTable": equipmentCurrentAlarmTable,
       "equipmentCurrentAlarmEntry": equipmentCurrentAlarmEntry,
       "equipmentCurrentAlarmType": equipmentCurrentAlarmType,
       "equipmentCurrentAlarmSeverity": equipmentCurrentAlarmSeverity,
       "neAlarms": neAlarms,
       "neAlarmAuthFailSource": neAlarmAuthFailSource,
       "neAlarmAuthFailDescription": neAlarmAuthFailDescription,
       "adminMIB": adminMIB,
       "neType": neType,
       "neMibVariant": neMibVariant,
       "neTrapsinkTable": neTrapsinkTable,
       "neTrapsinkEntry": neTrapsinkEntry,
       "neTrapsinkAddress": neTrapsinkAddress,
       "neTrapsinkCommunity": neTrapsinkCommunity,
       "neTrapsinkPort": neTrapsinkPort,
       "neTrapsinkRowStatus": neTrapsinkRowStatus,
       "neManufacturer": neManufacturer,
       "neState": neState,
       "neEventsLogged": neEventsLogged,
       "neEventLogTable": neEventLogTable,
       "neEventLogEntry": neEventLogEntry,
       "neEventLogIndex": neEventLogIndex,
       "neEventLogTimeStamp": neEventLogTimeStamp,
       "neEventLogNotificationOID": neEventLogNotificationOID,
       "neEventLogIndexTranslation": neEventLogIndexTranslation,
       "neEventLogVarTable": neEventLogVarTable,
       "neEventLogVarEntry": neEventLogVarEntry,
       "neEventLogVarIndex": neEventLogVarIndex,
       "neEventLogVarId": neEventLogVarId,
       "neEventLogVarType": neEventLogVarType,
       "neEventLogVarInteger32Val": neEventLogVarInteger32Val,
       "neEventLogVarIpAddressVal": neEventLogVarIpAddressVal,
       "neEventLogVarOctetStringVal": neEventLogVarOctetStringVal,
       "neEventLogVarOidVal": neEventLogVarOidVal,
       "neSNMPSet": neSNMPSet,
       "softwareUpgradeMIB": softwareUpgradeMIB,
       "supportFspSwUpgradeTable": supportFspSwUpgradeTable,
       "activeApplicationSwVersion": activeApplicationSwVersion,
       "inactiveApplicationSwVersion": inactiveApplicationSwVersion,
       "activeOperatingSwVersion": activeOperatingSwVersion,
       "inactiveOperatingSwVersion": inactiveOperatingSwVersion,
       "fspSwUpgradeTable": fspSwUpgradeTable,
       "fspSwUpgradeEntry": fspSwUpgradeEntry,
       "fspSwUpgradeIndex": fspSwUpgradeIndex,
       "fspSwUpgradeServerIpAddress": fspSwUpgradeServerIpAddress,
       "fspSwUpgradeServerLogin": fspSwUpgradeServerLogin,
       "fspSwUpgradeServerPassword": fspSwUpgradeServerPassword,
       "fspSwUpgradeServerFileLocation": fspSwUpgradeServerFileLocation,
       "fspSwUpgradeFileName": fspSwUpgradeFileName,
       "fspSwUpgradeType": fspSwUpgradeType,
       "fspSwUpgradeProtocol": fspSwUpgradeProtocol,
       "fspSwUpgradeRequest": fspSwUpgradeRequest,
       "fspSwUpgradeStatus": fspSwUpgradeStatus,
       "neTrapsenderAddress": neTrapsenderAddress,
       "snmpWriteAccessRestriction": snmpWriteAccessRestriction,
       "snmpWriteAccessTable": snmpWriteAccessTable,
       "snmpWriteAccessEntry": snmpWriteAccessEntry,
       "snmpWriteAccessNmsAddress": snmpWriteAccessNmsAddress,
       "snmpWriteAccessNmsName": snmpWriteAccessNmsName,
       "neMemorySizeTotal": neMemorySizeTotal,
       "neMemorySizeFree": neMemorySizeFree,
       "neStorageTable": neStorageTable,
       "neStorageEntry": neStorageEntry,
       "neStorageIndex": neStorageIndex,
       "neStorageDescr": neStorageDescr,
       "neStorageCapacity": neStorageCapacity,
       "neStorageAvailable": neStorageAvailable,
       "trapMIB": trapMIB,
       "trapMIBPrefix": trapMIBPrefix,
       "neTrapsinkTest": neTrapsinkTest,
       "equipmentHolderObjectCreation": equipmentHolderObjectCreation,
       "equipmentHolderObjectDeletion": equipmentHolderObjectDeletion,
       "containerStateChange": containerStateChange,
       "neAttributeValueChange": neAttributeValueChange,
       "interfaceAttributeValueChange": interfaceAttributeValueChange,
       "equipmentAttributeValueChange": equipmentAttributeValueChange,
       "neAuthentificationFail": neAuthentificationFail,
       "neINNCDown": neINNCDown,
       "neINNCUp": neINNCUp,
       "neSoftwareUpdate": neSoftwareUpdate,
       "neStateChange": neStateChange,
       "interfaceStateChange": interfaceStateChange,
       "equipmentStateChange": equipmentStateChange,
       "resetAllTelemetryOutputs": resetAllTelemetryOutputs,
       "interfaceAlarmSeverityChange": interfaceAlarmSeverityChange,
       "equipmentAlarmSeverityChange": equipmentAlarmSeverityChange,
       "neTrapsinkObjectCreation": neTrapsinkObjectCreation,
       "neTrapsinkObjectDeletion": neTrapsinkObjectDeletion,
       "neSNMPWriteAccessObjectCreation": neSNMPWriteAccessObjectCreation,
       "neSNMPWriteAccessObjectDeletion": neSNMPWriteAccessObjectDeletion,
       "interfaceAlarmLossOfSignal": interfaceAlarmLossOfSignal,
       "interfaceAlarmNoLossOfSignal": interfaceAlarmNoLossOfSignal,
       "interfaceAlarmLossOfLinkPulse": interfaceAlarmLossOfLinkPulse,
       "interfaceAlarmNoLossOfLinkPulse": interfaceAlarmNoLossOfLinkPulse,
       "interfaceAlarmLossOfSync": interfaceAlarmLossOfSync,
       "interfaceAlarmNoLossOfSync": interfaceAlarmNoLossOfSync,
       "interfaceAlarmPartitioned": interfaceAlarmPartitioned,
       "interfaceAlarmNoPartitioned": interfaceAlarmNoPartitioned,
       "interfaceAlarmLaserTecEoL": interfaceAlarmLaserTecEoL,
       "interfaceAlarmNoLaserTecEoL": interfaceAlarmNoLaserTecEoL,
       "interfaceAlarmIfModuleTempOoR": interfaceAlarmIfModuleTempOoR,
       "interfaceAlarmIfModuleTempNotOoR": interfaceAlarmIfModuleTempNotOoR,
       "interfaceAlarmLaserTempOoR": interfaceAlarmLaserTempOoR,
       "interfaceAlarmLaserTempNotOoR": interfaceAlarmLaserTempNotOoR,
       "interfaceAlarmLossOfOOP": interfaceAlarmLossOfOOP,
       "interfaceAlarmNoLossOfOOP": interfaceAlarmNoLossOfOOP,
       "interfaceAlarmOIPTooHigh": interfaceAlarmOIPTooHigh,
       "interfaceAlarmOIPNotTooHigh": interfaceAlarmOIPNotTooHigh,
       "interfaceAlarmOOPTooLow": interfaceAlarmOOPTooLow,
       "interfaceAlarmOOPNotTooLow": interfaceAlarmOOPNotTooLow,
       "interfaceAlarmLossOfSignalAtT": interfaceAlarmLossOfSignalAtT,
       "interfaceAlarmNoLossOfSignalAtT": interfaceAlarmNoLossOfSignalAtT,
       "telemetryStateOn": telemetryStateOn,
       "telemetryStateOff": telemetryStateOff,
       "interfaceAlarmAttAtRTooHigh": interfaceAlarmAttAtRTooHigh,
       "interfaceAlarmAttAtRNotTooHigh": interfaceAlarmAttAtRNotTooHigh,
       "interfaceAlarmAttAtRTooLow": interfaceAlarmAttAtRTooLow,
       "interfaceAlarmAttAtRNotTooLow": interfaceAlarmAttAtRNotTooLow,
       "interfaceAlarmAttAtTTooHigh": interfaceAlarmAttAtTTooHigh,
       "interfaceAlarmAttAtTNotTooHigh": interfaceAlarmAttAtTNotTooHigh,
       "interfaceAlarmAttAtTTooLow": interfaceAlarmAttAtTTooLow,
       "interfaceAlarmAttAtTNotTooLow": interfaceAlarmAttAtTNotTooLow,
       "interfaceAlarmIntrusionAtR": interfaceAlarmIntrusionAtR,
       "interfaceAlarmNoIntrusionAtR": interfaceAlarmNoIntrusionAtR,
       "interfaceAlarmIntrusionAtT": interfaceAlarmIntrusionAtT,
       "interfaceAlarmNoIntrusionAtT": interfaceAlarmNoIntrusionAtT,
       "ifAlarmLaserBiasTooLow": ifAlarmLaserBiasTooLow,
       "ifAlarmLaserBiasNotTooLow": ifAlarmLaserBiasNotTooLow,
       "ifAlarmLaserBiasTooHigh": ifAlarmLaserBiasTooHigh,
       "ifAlarmLaserBiasNotTooHigh": ifAlarmLaserBiasNotTooHigh,
       "interfaceAlarmOIPTooLow": interfaceAlarmOIPTooLow,
       "interfaceAlarmOIPNotTooLow": interfaceAlarmOIPNotTooLow,
       "interfaceAlarmOOPTooHigh": interfaceAlarmOOPTooHigh,
       "interfaceAlarmOOPNotTooHigh": interfaceAlarmOOPNotTooHigh,
       "equipmentAlarmFanFail": equipmentAlarmFanFail,
       "equipmentAlarmFanNoFail": equipmentAlarmFanNoFail,
       "equipmentAlarmFanPsFail": equipmentAlarmFanPsFail,
       "equipmentAlarmFanPsNoFail": equipmentAlarmFanPsNoFail,
       "equipmentAlarmPsFail": equipmentAlarmPsFail,
       "equipmentAlarmPsNoFail": equipmentAlarmPsNoFail,
       "equipmentAlarmTempTooHigh": equipmentAlarmTempTooHigh,
       "equipmentAlarmTempNotTooHigh": equipmentAlarmTempNotTooHigh,
       "equipmentAlarmTempTooLow": equipmentAlarmTempTooLow,
       "equipmentAlarmTempNotTooLow": equipmentAlarmTempNotTooLow,
       "equipmentAlarmVoltageTooHigh": equipmentAlarmVoltageTooHigh,
       "equipmentAlarmVoltageNotTooHigh": equipmentAlarmVoltageNotTooHigh,
       "equipmentAlarmVoltageTooLow": equipmentAlarmVoltageTooLow,
       "equipmentAlarmVoltageNotTooLow": equipmentAlarmVoltageNotTooLow,
       "eqAlarmMismatch": eqAlarmMismatch,
       "eqAlarmNoMismatch": eqAlarmNoMismatch,
       "interfaceAlarmAttRxMonLow": interfaceAlarmAttRxMonLow,
       "interfaceAlarmAttRxMonNotLow": interfaceAlarmAttRxMonNotLow,
       "interfaceAlarmAttRxMonHigh": interfaceAlarmAttRxMonHigh,
       "interfaceAlarmAttRxMonNotHigh": interfaceAlarmAttRxMonNotHigh,
       "interfaceAlarmAttTxMonLow": interfaceAlarmAttTxMonLow,
       "interfaceAlarmAttTxMonNotLow": interfaceAlarmAttTxMonNotLow,
       "interfaceAlarmAttTxMonHigh": interfaceAlarmAttTxMonHigh,
       "interfaceAlarmAttTxMonNotHigh": interfaceAlarmAttTxMonNotHigh,
       "telemetryInput2StateOn": telemetryInput2StateOn,
       "telemetryInput2StateOff": telemetryInput2StateOff,
       "telemetryInput3StateOn": telemetryInput3StateOn,
       "telemetryInput3StateOff": telemetryInput3StateOff,
       "interfaceAlarmLaserFailure": interfaceAlarmLaserFailure,
       "interfaceAlarmLaserNoFailure": interfaceAlarmLaserNoFailure,
       "interfaceAlarmPumpLaserFailure": interfaceAlarmPumpLaserFailure,
       "interfaceAlarmPumpLaserNoFail": interfaceAlarmPumpLaserNoFail,
       "interfaceAlarmReceiverFailure": interfaceAlarmReceiverFailure,
       "interfaceAlarmReceiverNoFail": interfaceAlarmReceiverNoFail,
       "interfaceAlarmOOPOoR": interfaceAlarmOOPOoR,
       "interfaceAlarmOOPNormal": interfaceAlarmOOPNormal,
       "ifAlarmTempSafetyShutdown": ifAlarmTempSafetyShutdown,
       "ifAlarmTempSafetyShutdownClear": ifAlarmTempSafetyShutdownClear,
       "interfaceAlarmLaserTemp2Low": interfaceAlarmLaserTemp2Low,
       "interfaceAlarmLaserTempNot2Low": interfaceAlarmLaserTempNot2Low,
       "interfaceAlarmLaserTemp2High": interfaceAlarmLaserTemp2High,
       "interfaceAlarmLaserTempNot2High": interfaceAlarmLaserTempNot2High,
       "trapVariables": trapVariables,
       "containerState": containerState,
       "containsPhysicalIndex": containsPhysicalIndex,
       "timeStamp": timeStamp,
       "indexTranslation": indexTranslation,
       "objectId": objectId,
       "configurationMIB": configurationMIB,
       "interfaceConfiguration": interfaceConfiguration,
       "interfaceTTTable": interfaceTTTable,
       "interfaceTTEntry": interfaceTTEntry,
       "interfaceTTLoopState": interfaceTTLoopState,
       "interfaceTTLaserTxConfig": interfaceTTLaserTxConfig,
       "interfaceTTLaserTxCurrent": interfaceTTLaserTxCurrent,
       "interfaceTTLaserTxTemp": interfaceTTLaserTxTemp,
       "interfaceTTRxClockFreq": interfaceTTRxClockFreq,
       "interfaceTTRxClockType": interfaceTTRxClockType,
       "interfaceTTWavelength": interfaceTTWavelength,
       "interfaceTTOpticalInputPower": interfaceTTOpticalInputPower,
       "interfaceTTOpticalOutputPower": interfaceTTOpticalOutputPower,
       "interfaceTTConnector": interfaceTTConnector,
       "interfaceTTFiberType": interfaceTTFiberType,
       "interfaceTTResultDRTranspLow": interfaceTTResultDRTranspLow,
       "interfaceTTResultDRTranspHigh": interfaceTTResultDRTranspHigh,
       "interfaceTTIncommingDataRate": interfaceTTIncommingDataRate,
       "interfaceTTDisparityCtrl": interfaceTTDisparityCtrl,
       "interfaceTTLaserTxStatus": interfaceTTLaserTxStatus,
       "interfaceTTLocalLOSSuppression": interfaceTTLocalLOSSuppression,
       "interfaceTTLaserTxTempTenth": interfaceTTLaserTxTempTenth,
       "electricalInterfaceTable": electricalInterfaceTable,
       "electricalInterfaceEntry": electricalInterfaceEntry,
       "electricalInterfaceTxAutoNeg": electricalInterfaceTxAutoNeg,
       "electricalInterfaceDuplexMode": electricalInterfaceDuplexMode,
       "electricalInterfaceLineSpeed": electricalInterfaceLineSpeed,
       "electricalInterfaceLoopState": electricalInterfaceLoopState,
       "electricalInterfaceRxClockFreq": electricalInterfaceRxClockFreq,
       "electricalInterfaceRxClockType": electricalInterfaceRxClockType,
       "edfaInterfaceTable": edfaInterfaceTable,
       "edfaInterfaceEntry": edfaInterfaceEntry,
       "edfaInterfaceOpticalBandType": edfaInterfaceOpticalBandType,
       "edfaInterfacePumpLaserTxConfig": edfaInterfacePumpLaserTxConfig,
       "edfaInterfaceOpticalInputPower": edfaInterfaceOpticalInputPower,
       "edfaInterfaceOpticalOutputPower": edfaInterfaceOpticalOutputPower,
       "edfaInterfaceModuleTemp": edfaInterfaceModuleTemp,
       "edfaInterfacePumpLaserPower": edfaInterfacePumpLaserPower,
       "edfaInterfacePumpLaserCurrent": edfaInterfacePumpLaserCurrent,
       "edfaInterfacePumpLaserTxTemp": edfaInterfacePumpLaserTxTemp,
       "edfaInterfacePumpLaserConfig": edfaInterfacePumpLaserConfig,
       "edfaInterfaceTECCurrent": edfaInterfaceTECCurrent,
       "edfaInterfaceMaxOperPower": edfaInterfaceMaxOperPower,
       "edfaInterfaceOIPAlarmOnOff": edfaInterfaceOIPAlarmOnOff,
       "edfaInterfacePumpLaserTxStatus": edfaInterfacePumpLaserTxStatus,
       "remoteOptSwitchInterfaceTable": remoteOptSwitchInterfaceTable,
       "remoteOptSwitchInterfaceEntry": remoteOptSwitchInterfaceEntry,
       "remoteOptSwitchInterfaceLambda": remoteOptSwitchInterfaceLambda,
       "olmInterfaceLineAttR": olmInterfaceLineAttR,
       "olmInterfaceLineAttT": olmInterfaceLineAttT,
       "equipmentConfiguration": equipmentConfiguration,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleCapabilities": moduleCapabilities,
       "moduleEnvironmentTemp1": moduleEnvironmentTemp1,
       "moduleEnvironmentTemp1Max": moduleEnvironmentTemp1Max,
       "moduleVoltage1": moduleVoltage1,
       "moduleVoltage1Max": moduleVoltage1Max,
       "moduleVoltage1Min": moduleVoltage1Min,
       "moduleComment": moduleComment,
       "moduleType": moduleType,
       "moduleOfficialName": moduleOfficialName,
       "wavelengthChannelModuleTable": wavelengthChannelModuleTable,
       "wavelengthChannelModuleEntry": wavelengthChannelModuleEntry,
       "wavelengthChannelModuleRegState": wavelengthChannelModuleRegState,
       "wavelengthChannelModuleChannel": wavelengthChannelModuleChannel,
       "wavelengthChannelModuleScheme": wavelengthChannelModuleScheme,
       "wdmChannelModuleLowDRTransp": wdmChannelModuleLowDRTransp,
       "wdmChannelModuleHighDRTransp": wdmChannelModuleHighDRTransp,
       "wavelengthChannelModuleChName": wavelengthChannelModuleChName,
       "wdmChannelModuleTMMode": wdmChannelModuleTMMode,
       "wdmChannelModuleTMCap": wdmChannelModuleTMCap,
       "wdmChannelModuleTMCurrentCap": wdmChannelModuleTMCurrentCap,
       "remoteOptSwitchTable": remoteOptSwitchTable,
       "remoteOptSwitchEntry": remoteOptSwitchEntry,
       "remoteOptSwitchOperState": remoteOptSwitchOperState,
       "remoteOptSwitchAdminState": remoteOptSwitchAdminState,
       "remoteOptSwitchALS": remoteOptSwitchALS,
       "remoteOptSwitchRevertiveMode": remoteOptSwitchRevertiveMode,
       "remoteOptSwitchPreferredLine": remoteOptSwitchPreferredLine,
       "oscModuleTable": oscModuleTable,
       "oscModuleEntry": oscModuleEntry,
       "oscModuleVoltage2": oscModuleVoltage2,
       "oscModuleVoltage3": oscModuleVoltage3,
       "mdxModuleTable": mdxModuleTable,
       "mdxModuleEntry": mdxModuleEntry,
       "mdxModuleWDMType": mdxModuleWDMType,
       "mdxModuleScheme": mdxModuleScheme,
       "mdxModuleChannelRange": mdxModuleChannelRange,
       "mdxModuleUpgradePort": mdxModuleUpgradePort,
       "bandSplitterModuleTable": bandSplitterModuleTable,
       "bandSplitterModuleEntry": bandSplitterModuleEntry,
       "bandSplitterModuleScheme": bandSplitterModuleScheme,
       "bandSplitterModuleBandRange": bandSplitterModuleBandRange,
       "bandSplitterModuleType": bandSplitterModuleType,
       "olmModuleTable": olmModuleTable,
       "olmModuleEntry": olmModuleEntry,
       "olmModuleSwitchOver": olmModuleSwitchOver,
       "olmModuleThreshold": olmModuleThreshold,
       "olmModuleHysteresis": olmModuleHysteresis,
       "olmModuleOTDRWindowStatus": olmModuleOTDRWindowStatus,
       "olmModuleOTDRWindowTime": olmModuleOTDRWindowTime,
       "olmModuleMinThreshold": olmModuleMinThreshold,
       "olmModuleMaxThreshold": olmModuleMaxThreshold,
       "sfpTransceiverSubModuleTable": sfpTransceiverSubModuleTable,
       "sfpTransceiverSubModuleEntry": sfpTransceiverSubModuleEntry,
       "sfpTransceiverApprovedByADVA": sfpTransceiverApprovedByADVA,
       "sfpTransceiverLinkLength": sfpTransceiverLinkLength,
       "sfpTransceiverChannelName": sfpTransceiverChannelName,
       "sfpTransceiverWaveLengthScheme": sfpTransceiverWaveLengthScheme,
       "interleaverModuleTable": interleaverModuleTable,
       "interleaverModuleEntry": interleaverModuleEntry,
       "interleaverModuleType": interleaverModuleType,
       "interleaverModuleSpacing": interleaverModuleSpacing,
       "channelFilterModuleTable": channelFilterModuleTable,
       "channelFilterModuleEntry": channelFilterModuleEntry,
       "channelFilterModuleScheme": channelFilterModuleScheme,
       "channelFilterModuleChannelName": channelFilterModuleChannelName,
       "fsp2000Conformance": fsp2000Conformance,
       "fsp2000Objects": fsp2000Objects,
       "fsp2000Notifications": fsp2000Notifications,
       "fsp2000DeprecatedObjects": fsp2000DeprecatedObjects,
       "performanceMIB": performanceMIB,
       "performanceAdmin": performanceAdmin,
       "physicalPerformanceAdmin": physicalPerformanceAdmin,
       "olmPPHWthresholdTable": olmPPHWthresholdTable,
       "olmPPHWthresholdEntry": olmPPHWthresholdEntry,
       "olmPPHWthresholdLowAtt": olmPPHWthresholdLowAtt,
       "olmPPHWthresholdHighAtt": olmPPHWthresholdHighAtt,
       "oLMPPthresholdTable": oLMPPthresholdTable,
       "oLMPPthresholdEntry": oLMPPthresholdEntry,
       "oLMPPthresholdAttGradient": oLMPPthresholdAttGradient,
       "oLMIfPPthresholdTable": oLMIfPPthresholdTable,
       "oLMIfPPthresholdEntry": oLMIfPPthresholdEntry,
       "oLMIfPPthresholdLowTxAtt": oLMIfPPthresholdLowTxAtt,
       "oLMIfPPthresholdHighTxAtt": oLMIfPPthresholdHighTxAtt,
       "oLMIfPPthresholdLowRxAtt": oLMIfPPthresholdLowRxAtt,
       "oLMIfPPthresholdHighRxAtt": oLMIfPPthresholdHighRxAtt,
       "edfaPPthresholdTable": edfaPPthresholdTable,
       "edfaPPthresholdEntry": edfaPPthresholdEntry,
       "edfaPPthresholdHighPumpCurrent": edfaPPthresholdHighPumpCurrent,
       "edfaPPthresholdLowOIP": edfaPPthresholdLowOIP,
       "edfaPPthresholdHighOIP": edfaPPthresholdHighOIP,
       "edfaPPthresholdHighTempProt": edfaPPthresholdHighTempProt,
       "ifTTPPthresholdTable": ifTTPPthresholdTable,
       "ifTTPPthresholdEntry": ifTTPPthresholdEntry,
       "ifTTPPthresholdLowLaserCurrent": ifTTPPthresholdLowLaserCurrent,
       "ifTTPPthresholdHighLaserCurrent": ifTTPPthresholdHighLaserCurrent,
       "ifTTPPthresholdLowOIP": ifTTPPthresholdLowOIP,
       "ifTTPPthresholdHighOIP": ifTTPPthresholdHighOIP,
       "ifTTPPthresholdLowOOP": ifTTPPthresholdLowOOP,
       "ifTTPPthresholdHighOOP": ifTTPPthresholdHighOOP,
       "ifTTPPthresholdLowLaserTemp": ifTTPPthresholdLowLaserTemp,
       "ifTTPPthresholdHighLaserTemp": ifTTPPthresholdHighLaserTemp,
       "modulePPthresholdTable": modulePPthresholdTable,
       "modulePPthresholdEntry": modulePPthresholdEntry,
       "modulePPthresholdLowVolt": modulePPthresholdLowVolt,
       "modulePPthresholdHighVolt": modulePPthresholdHighVolt,
       "modulePPthresholdHighTemp": modulePPthresholdHighTemp,
       "modulePPthresholdLowTemp": modulePPthresholdLowTemp,
       "generalPerformanceAdmin": generalPerformanceAdmin,
       "ifPerformanceStatusTable": ifPerformanceStatusTable,
       "ifPerformanceStatusEntry": ifPerformanceStatusEntry,
       "ifPerformanceStatusType": ifPerformanceStatusType,
       "ifPerformanceStatusAvail": ifPerformanceStatusAvail,
       "ifPerformanceStatusLength": ifPerformanceStatusLength,
       "modulePerformanceStatusTable": modulePerformanceStatusTable,
       "modulePerformanceStatusEntry": modulePerformanceStatusEntry,
       "modulePerformanceStatusType": modulePerformanceStatusType,
       "modulePerformanceStatusAvail": modulePerformanceStatusAvail,
       "modulePerformanceStatusLength": modulePerformanceStatusLength,
       "performanceMonitoring": performanceMonitoring,
       "physicalLayerPerformanceMon": physicalLayerPerformanceMon,
       "oLMPLP15minIntTable": oLMPLP15minIntTable,
       "oLMPLP15minIntEntry": oLMPLP15minIntEntry,
       "oLMPLP15minIntIndex": oLMPLP15minIntIndex,
       "oLMPLP15minIntAverageRxAtt": oLMPLP15minIntAverageRxAtt,
       "oLMPLP15minIntMinRxAtt": oLMPLP15minIntMinRxAtt,
       "oLMPLP15minIntMaxRxAtt": oLMPLP15minIntMaxRxAtt,
       "oLMPLP15minIntAverageTxAtt": oLMPLP15minIntAverageTxAtt,
       "oLMPLP15minIntMinTxAtt": oLMPLP15minIntMinTxAtt,
       "oLMPLP15minIntMaxTxAtt": oLMPLP15minIntMaxTxAtt,
       "oLMPLP15minIntValidData": oLMPLP15minIntValidData,
       "oLMPLP15minIntTimeStamp": oLMPLP15minIntTimeStamp,
       "oLMPLP24hIntTable": oLMPLP24hIntTable,
       "oLMPLP24hIntEntry": oLMPLP24hIntEntry,
       "oLMPLP24hIntIndex": oLMPLP24hIntIndex,
       "oLMPLP24hIntAverageRxAtt": oLMPLP24hIntAverageRxAtt,
       "oLMPLP24hIntMinRxAtt": oLMPLP24hIntMinRxAtt,
       "oLMPLP24hIntMaxRxAtt": oLMPLP24hIntMaxRxAtt,
       "oLMPLP24hIntAverageTxAtt": oLMPLP24hIntAverageTxAtt,
       "oLMPLP24hIntMinTxAtt": oLMPLP24hIntMinTxAtt,
       "oLMPLP24hIntMaxTxAtt": oLMPLP24hIntMaxTxAtt,
       "oLMPLP24hIntValidData": oLMPLP24hIntValidData,
       "oLMPLP24hIntTimeStamp": oLMPLP24hIntTimeStamp,
       "oLMPLP1weekIntTable": oLMPLP1weekIntTable,
       "oLMPLP1weekIntEntry": oLMPLP1weekIntEntry,
       "oLMPLP1weekIntIndex": oLMPLP1weekIntIndex,
       "oLMPLP1weekIntAverageRxAtt": oLMPLP1weekIntAverageRxAtt,
       "oLMPLP1weekIntMinRxAtt": oLMPLP1weekIntMinRxAtt,
       "oLMPLP1weekIntMaxRxAtt": oLMPLP1weekIntMaxRxAtt,
       "oLMPLP1weekIntAverageTxAtt": oLMPLP1weekIntAverageTxAtt,
       "oLMPLP1weekIntMinTxAtt": oLMPLP1weekIntMinTxAtt,
       "oLMPLP1weekIntMaxTxAtt": oLMPLP1weekIntMaxTxAtt,
       "oLMPLP1weekIntValidData": oLMPLP1weekIntValidData,
       "oLMPLP1weekIntTimeStamp": oLMPLP1weekIntTimeStamp,
       "oLMPLPcurrentTable": oLMPLPcurrentTable,
       "oLMPLPcurrentEntry": oLMPLPcurrentEntry,
       "oLMPLPcurrentIndex": oLMPLPcurrentIndex,
       "oLMPLPcurrentAverageRxAtt": oLMPLPcurrentAverageRxAtt,
       "oLMPLPcurrentMinRxAtt": oLMPLPcurrentMinRxAtt,
       "oLMPLPcurrentMaxRxAtt": oLMPLPcurrentMaxRxAtt,
       "oLMPLPcurrentAverageTxAtt": oLMPLPcurrentAverageTxAtt,
       "oLMPLPcurrentMinTxAtt": oLMPLPcurrentMinTxAtt,
       "oLMPLPcurrentMaxTxAtt": oLMPLPcurrentMaxTxAtt,
       "oLMPLPcurrentValidData": oLMPLPcurrentValidData,
       "oLMPLPcurrentElapsedTime": oLMPLPcurrentElapsedTime,
       "edfaPLP15minIntTable": edfaPLP15minIntTable,
       "edfaPLP15minIntEntry": edfaPLP15minIntEntry,
       "edfaPLP15minIntIndex": edfaPLP15minIntIndex,
       "edfaPLP15minIntValidData": edfaPLP15minIntValidData,
       "edfaPLP15minIntTimeStamp": edfaPLP15minIntTimeStamp,
       "edfaPLP15minIntAveragePumpCurr": edfaPLP15minIntAveragePumpCurr,
       "edfaPLP15minIntMinPumpCurrent": edfaPLP15minIntMinPumpCurrent,
       "edfaPLP15minIntMaxPumpCurrent": edfaPLP15minIntMaxPumpCurrent,
       "edfaPLP15minIntAverageOIP": edfaPLP15minIntAverageOIP,
       "edfaPLP15minIntMinOIP": edfaPLP15minIntMinOIP,
       "edfaPLP15minIntMaxOIP": edfaPLP15minIntMaxOIP,
       "edfaPLP24hIntTable": edfaPLP24hIntTable,
       "edfaPLP24hIntEntry": edfaPLP24hIntEntry,
       "edfaPLP24hIntIndex": edfaPLP24hIntIndex,
       "edfaPLP24hIntValidData": edfaPLP24hIntValidData,
       "edfaPLP24hIntTimeStamp": edfaPLP24hIntTimeStamp,
       "edfaPLP24hIntAveragePumpCurrent": edfaPLP24hIntAveragePumpCurrent,
       "edfaPLP24hIntMinPumpCurrent": edfaPLP24hIntMinPumpCurrent,
       "edfaPLP24hIntMaxPumpCurrent": edfaPLP24hIntMaxPumpCurrent,
       "edfaPLP24hIntAverageOIP": edfaPLP24hIntAverageOIP,
       "edfaPLP24hIntMinOIP": edfaPLP24hIntMinOIP,
       "edfaPLP24hIntMaxOIP": edfaPLP24hIntMaxOIP,
       "edfaPLP1weekIntTable": edfaPLP1weekIntTable,
       "edfaPLP1weekIntEntry": edfaPLP1weekIntEntry,
       "edfaPLP1weekIntIndex": edfaPLP1weekIntIndex,
       "edfaPLP1weekIntValidData": edfaPLP1weekIntValidData,
       "edfaPLP1weekIntTimeStamp": edfaPLP1weekIntTimeStamp,
       "edfaPLP1weekIntAveragePumpCurr": edfaPLP1weekIntAveragePumpCurr,
       "edfaPLP1weekIntMinPumpCurrent": edfaPLP1weekIntMinPumpCurrent,
       "edfaPLP1weekIntMaxPumpCurrent": edfaPLP1weekIntMaxPumpCurrent,
       "edfaPLP1weekIntAverageOIP": edfaPLP1weekIntAverageOIP,
       "edfaPLP1weekIntMinOIP": edfaPLP1weekIntMinOIP,
       "edfaPLP1weekIntMaxOIP": edfaPLP1weekIntMaxOIP,
       "edfaPLPcurrentTable": edfaPLPcurrentTable,
       "edfaPLPcurrentEntry": edfaPLPcurrentEntry,
       "edfaPLPcurrentIndex": edfaPLPcurrentIndex,
       "edfaPLPcurrentValidData": edfaPLPcurrentValidData,
       "edfaPLPcurrentElapsedTime": edfaPLPcurrentElapsedTime,
       "edfaPLPcurrentAveragePumpCurr": edfaPLPcurrentAveragePumpCurr,
       "edfaPLPcurrentMinPumpCurrent": edfaPLPcurrentMinPumpCurrent,
       "edfaPLPcurrentMaxPumpCurrent": edfaPLPcurrentMaxPumpCurrent,
       "edfaPLPcurrentAverageOIP": edfaPLPcurrentAverageOIP,
       "edfaPLPcurrentMinOIP": edfaPLPcurrentMinOIP,
       "edfaPLPcurrentMaxOIP": edfaPLPcurrentMaxOIP,
       "ifTTPLP15minIntTable": ifTTPLP15minIntTable,
       "ifTTPLP15minIntEntry": ifTTPLP15minIntEntry,
       "ifTTPLP15minIntIndex": ifTTPLP15minIntIndex,
       "ifTTPLP15minIntValidData": ifTTPLP15minIntValidData,
       "ifTTPLP15minIntTimeStamp": ifTTPLP15minIntTimeStamp,
       "ifTTPLP15minIntAverageLaserCurr": ifTTPLP15minIntAverageLaserCurr,
       "ifTTPLP15minIntMinLaserCurrent": ifTTPLP15minIntMinLaserCurrent,
       "ifTTPLP15minIntMaxLaserCurrent": ifTTPLP15minIntMaxLaserCurrent,
       "ifTTPLP15minIntAverageOIP": ifTTPLP15minIntAverageOIP,
       "ifTTPLP15minIntMinOIP": ifTTPLP15minIntMinOIP,
       "ifTTPLP15minIntMaxOIP": ifTTPLP15minIntMaxOIP,
       "ifTTPLP15minIntAverageOOP": ifTTPLP15minIntAverageOOP,
       "ifTTPLP15minIntMinOOP": ifTTPLP15minIntMinOOP,
       "ifTTPLP15minIntMaxOOP": ifTTPLP15minIntMaxOOP,
       "ifTTPLP24hIntTable": ifTTPLP24hIntTable,
       "ifTTPLP24hIntEntry": ifTTPLP24hIntEntry,
       "ifTTPLP24hIntIndex": ifTTPLP24hIntIndex,
       "ifTTPLP24hIntValidData": ifTTPLP24hIntValidData,
       "ifTTPLP24hIntTimeStamp": ifTTPLP24hIntTimeStamp,
       "ifTTPLP24hIntAverageLaserCurr": ifTTPLP24hIntAverageLaserCurr,
       "ifTTPLP24hIntMinLaserCurrent": ifTTPLP24hIntMinLaserCurrent,
       "ifTTPLP24hIntMaxLaserCurrent": ifTTPLP24hIntMaxLaserCurrent,
       "ifTTPLP24hIntAverageOIP": ifTTPLP24hIntAverageOIP,
       "ifTTPLP24hIntMinOIP": ifTTPLP24hIntMinOIP,
       "ifTTPLP24hIntMaxOIP": ifTTPLP24hIntMaxOIP,
       "ifTTPLP24hIntAverageOOP": ifTTPLP24hIntAverageOOP,
       "ifTTPLP24hIntMinOOP": ifTTPLP24hIntMinOOP,
       "ifTTPLP24hIntMaxOOP": ifTTPLP24hIntMaxOOP,
       "ifTTPLP1weekIntTable": ifTTPLP1weekIntTable,
       "ifTTPLP1weekIntEntry": ifTTPLP1weekIntEntry,
       "ifTTPLP1weekIntIndex": ifTTPLP1weekIntIndex,
       "ifTTPLP1weekIntValidData": ifTTPLP1weekIntValidData,
       "ifTTPLP1weekIntTimeStamp": ifTTPLP1weekIntTimeStamp,
       "ifTTPLP1weekIntAverageLaserCurr": ifTTPLP1weekIntAverageLaserCurr,
       "ifTTPLP1weekIntMinLaserCurrent": ifTTPLP1weekIntMinLaserCurrent,
       "ifTTPLP1weekIntMaxLaserCurrent": ifTTPLP1weekIntMaxLaserCurrent,
       "ifTTPLP1weekIntAverageOIP": ifTTPLP1weekIntAverageOIP,
       "ifTTPLP1weekIntMinOIP": ifTTPLP1weekIntMinOIP,
       "ifTTPLP1weekIntMaxOIP": ifTTPLP1weekIntMaxOIP,
       "ifTTPLP1weekIntAverageOOP": ifTTPLP1weekIntAverageOOP,
       "ifTTPLP1weekIntMinOOP": ifTTPLP1weekIntMinOOP,
       "ifTTPLP1weekIntMaxOOP": ifTTPLP1weekIntMaxOOP,
       "ifTTPLPcurrentTable": ifTTPLPcurrentTable,
       "ifTTPLPcurrentEntry": ifTTPLPcurrentEntry,
       "ifTTPLPcurrentIndex": ifTTPLPcurrentIndex,
       "ifTTPLPcurrentValidData": ifTTPLPcurrentValidData,
       "ifTTPLPcurrentElapsedTime": ifTTPLPcurrentElapsedTime,
       "ifTTPLPcurrentAverageLaserCurr": ifTTPLPcurrentAverageLaserCurr,
       "ifTTPLPcurrentMinLaserCurrent": ifTTPLPcurrentMinLaserCurrent,
       "ifTTPLPcurrentMaxLaserCurrent": ifTTPLPcurrentMaxLaserCurrent,
       "ifTTPLPcurrentAverageOIP": ifTTPLPcurrentAverageOIP,
       "ifTTPLPcurrentMinOIP": ifTTPLPcurrentMinOIP,
       "ifTTPLPcurrentMaxOIP": ifTTPLPcurrentMaxOIP,
       "ifTTPLPcurrentAverageOOP": ifTTPLPcurrentAverageOOP,
       "ifTTPLPcurrentMinOOP": ifTTPLPcurrentMinOOP,
       "ifTTPLPcurrentMaxOOP": ifTTPLPcurrentMaxOOP,
       "modulePLP15minIntTable": modulePLP15minIntTable,
       "modulePLP15minIntEntry": modulePLP15minIntEntry,
       "modulePLP15minIntIndex": modulePLP15minIntIndex,
       "modulePLP15minIntValidData": modulePLP15minIntValidData,
       "modulePLP15minIntTimeStamp": modulePLP15minIntTimeStamp,
       "modulePLP15minIntAverageTemp": modulePLP15minIntAverageTemp,
       "modulePLP15minIntMinTemp": modulePLP15minIntMinTemp,
       "modulePLP15minIntMaxTemp": modulePLP15minIntMaxTemp,
       "modulePLP15minIntAverageVoltage": modulePLP15minIntAverageVoltage,
       "modulePLP15minIntMinVoltage": modulePLP15minIntMinVoltage,
       "modulePLP15minIntMaxVoltage": modulePLP15minIntMaxVoltage,
       "modulePLP24hIntTable": modulePLP24hIntTable,
       "modulePLP24hIntEntry": modulePLP24hIntEntry,
       "modulePLP24hIntIndex": modulePLP24hIntIndex,
       "modulePLP24hIntValidData": modulePLP24hIntValidData,
       "modulePLP24hIntTimeStamp": modulePLP24hIntTimeStamp,
       "modulePLP24hIntAverageTemp": modulePLP24hIntAverageTemp,
       "modulePLP24hIntMinTemp": modulePLP24hIntMinTemp,
       "modulePLP24hIntMaxTemp": modulePLP24hIntMaxTemp,
       "modulePLP24hIntAverageVoltage": modulePLP24hIntAverageVoltage,
       "modulePLP24hIntMinVoltage": modulePLP24hIntMinVoltage,
       "modulePLP24hIntMaxVoltage": modulePLP24hIntMaxVoltage,
       "modulePLP1weekIntTable": modulePLP1weekIntTable,
       "modulePLP1weekIntEntry": modulePLP1weekIntEntry,
       "modulePLP1weekIntIndex": modulePLP1weekIntIndex,
       "modulePLP1weekIntValidData": modulePLP1weekIntValidData,
       "modulePLP1weekIntTimeStamp": modulePLP1weekIntTimeStamp,
       "modulePLP1weekIntAverageTemp": modulePLP1weekIntAverageTemp,
       "modulePLP1weekIntMinTemp": modulePLP1weekIntMinTemp,
       "modulePLP1weekIntMaxTemp": modulePLP1weekIntMaxTemp,
       "modulePLP1weekIntAverageVoltage": modulePLP1weekIntAverageVoltage,
       "modulePLP1weekIntMinVoltage": modulePLP1weekIntMinVoltage,
       "modulePLP1weekIntMaxVoltage": modulePLP1weekIntMaxVoltage,
       "modulePLPcurrentTable": modulePLPcurrentTable,
       "modulePLPcurrentEntry": modulePLPcurrentEntry,
       "modulePLPcurrentIndex": modulePLPcurrentIndex,
       "modulePLPcurrentValidData": modulePLPcurrentValidData,
       "modulePLPcurrentElapsedTime": modulePLPcurrentElapsedTime,
       "modulePLPcurrentAverageTemp": modulePLPcurrentAverageTemp,
       "modulePLPcurrentMinTemp": modulePLPcurrentMinTemp,
       "modulePLPcurrentMaxTemp": modulePLPcurrentMaxTemp,
       "modulePLPcurrentAverageVoltage": modulePLPcurrentAverageVoltage,
       "modulePLPcurrentMinVoltage": modulePLPcurrentMinVoltage,
       "modulePLPcurrentMaxVoltage": modulePLPcurrentMaxVoltage,
       "physicalLayerAlarmMon": physicalLayerAlarmMon,
       "oLMPLA15minIntTable": oLMPLA15minIntTable,
       "oLMPLA15minIntEntry": oLMPLA15minIntEntry,
       "oLMPLA15minIntIndex": oLMPLA15minIntIndex,
       "oLMPLA15minIntRxLOS": oLMPLA15minIntRxLOS,
       "oLMPLA15minIntTxLOS": oLMPLA15minIntTxLOS,
       "oLMPLA15minIntRxLow": oLMPLA15minIntRxLow,
       "oLMPLA15minIntRxHigh": oLMPLA15minIntRxHigh,
       "oLMPLA15minIntTxLow": oLMPLA15minIntTxLow,
       "oLMPLA15minIntTxHigh": oLMPLA15minIntTxHigh,
       "oLMPLA15minIntRxIntrusion": oLMPLA15minIntRxIntrusion,
       "oLMPLA15minIntTxIntrusion": oLMPLA15minIntTxIntrusion,
       "oLMPLA15minIntValidData": oLMPLA15minIntValidData,
       "oLMPLA15minIntTimeStamp": oLMPLA15minIntTimeStamp,
       "oLMPLA15minIntRxLowMon": oLMPLA15minIntRxLowMon,
       "oLMPLA15minIntRxHighMon": oLMPLA15minIntRxHighMon,
       "oLMPLA15minIntTxLowMon": oLMPLA15minIntTxLowMon,
       "oLMPLA15minIntTxHighMon": oLMPLA15minIntTxHighMon,
       "oLMPLA24hIntTable": oLMPLA24hIntTable,
       "oLMPLA24hIntEntry": oLMPLA24hIntEntry,
       "oLMPLA24hIntIndex": oLMPLA24hIntIndex,
       "oLMPLA24hIntRxLOS": oLMPLA24hIntRxLOS,
       "oLMPLA24hIntTxLOS": oLMPLA24hIntTxLOS,
       "oLMPLA24hIntRxLow": oLMPLA24hIntRxLow,
       "oLMPLA24hIntRxHigh": oLMPLA24hIntRxHigh,
       "oLMPLA24hIntTxLow": oLMPLA24hIntTxLow,
       "oLMPLA24hIntTxHigh": oLMPLA24hIntTxHigh,
       "oLMPLA24hIntRxIntrusion": oLMPLA24hIntRxIntrusion,
       "oLMPLA24hIntTxIntrusion": oLMPLA24hIntTxIntrusion,
       "oLMPLA24hIntValidData": oLMPLA24hIntValidData,
       "oLMPLA24hIntTimeStamp": oLMPLA24hIntTimeStamp,
       "oLMPLA24hIntRxLowMon": oLMPLA24hIntRxLowMon,
       "oLMPLA24hIntRxHighMon": oLMPLA24hIntRxHighMon,
       "oLMPLA24hIntTxLowMon": oLMPLA24hIntTxLowMon,
       "oLMPLA24hIntTxHighMon": oLMPLA24hIntTxHighMon,
       "oLMPLA1weekIntTable": oLMPLA1weekIntTable,
       "oLMPLA1weekIntEntry": oLMPLA1weekIntEntry,
       "oLMPLA1weekIntIndex": oLMPLA1weekIntIndex,
       "oLMPLA1weekIntRxLOS": oLMPLA1weekIntRxLOS,
       "oLMPLA1weekIntTxLOS": oLMPLA1weekIntTxLOS,
       "oLMPLA1weekIntRxLow": oLMPLA1weekIntRxLow,
       "oLMPLA1weekIntRxHigh": oLMPLA1weekIntRxHigh,
       "oLMPLA1weekIntTxLow": oLMPLA1weekIntTxLow,
       "oLMPLA1weekIntTxHigh": oLMPLA1weekIntTxHigh,
       "oLMPLA1weekIntRxIntrusion": oLMPLA1weekIntRxIntrusion,
       "oLMPLA1weekIntTxIntrusion": oLMPLA1weekIntTxIntrusion,
       "oLMPLA1weekIntValidData": oLMPLA1weekIntValidData,
       "oLMPLA1weekIntTimeStamp": oLMPLA1weekIntTimeStamp,
       "oLMPLA1weekIntRxLowMon": oLMPLA1weekIntRxLowMon,
       "oLMPLA1weekIntRxHighMon": oLMPLA1weekIntRxHighMon,
       "oLMPLA1weekIntTxLowMon": oLMPLA1weekIntTxLowMon,
       "oLMPLA1weekIntTxHighMon": oLMPLA1weekIntTxHighMon,
       "oLMPLAcurrentTable": oLMPLAcurrentTable,
       "oLMPLAcurrentEntry": oLMPLAcurrentEntry,
       "oLMPLAcurrentIndex": oLMPLAcurrentIndex,
       "oLMPLAcurrentRxLOS": oLMPLAcurrentRxLOS,
       "oLMPLAcurrentTxLOS": oLMPLAcurrentTxLOS,
       "oLMPLAcurrentRxLow": oLMPLAcurrentRxLow,
       "oLMPLAcurrentRxHigh": oLMPLAcurrentRxHigh,
       "oLMPLAcurrentTxLow": oLMPLAcurrentTxLow,
       "oLMPLAcurrentTxHigh": oLMPLAcurrentTxHigh,
       "oLMPLAcurrentRxIntrusion": oLMPLAcurrentRxIntrusion,
       "oLMPLAcurrentTxIntrusion": oLMPLAcurrentTxIntrusion,
       "oLMPLAcurrentValidData": oLMPLAcurrentValidData,
       "oLMPLAcurrentElapsedTime": oLMPLAcurrentElapsedTime,
       "oLMPLAcurrentRxLowMon": oLMPLAcurrentRxLowMon,
       "oLMPLAcurrentRxHighMon": oLMPLAcurrentRxHighMon,
       "oLMPLAcurrentTxLowMon": oLMPLAcurrentTxLowMon,
       "oLMPLAcurrentTxHighMon": oLMPLAcurrentTxHighMon,
       "edfaPLA15minIntTable": edfaPLA15minIntTable,
       "edfaPLA15minIntEntry": edfaPLA15minIntEntry,
       "edfaPLA15minIntIndex": edfaPLA15minIntIndex,
       "edfaPLA15minIntValidData": edfaPLA15minIntValidData,
       "edfaPLA15minIntTimeStamp": edfaPLA15minIntTimeStamp,
       "edfaPLA15minIntES": edfaPLA15minIntES,
       "edfaPLA15minIntLossOfSignal": edfaPLA15minIntLossOfSignal,
       "edfaPLA15minIntLossOfOop": edfaPLA15minIntLossOfOop,
       "edfaPLA24hIntTable": edfaPLA24hIntTable,
       "edfaPLA24hIntEntry": edfaPLA24hIntEntry,
       "edfaPLA24hIntIndex": edfaPLA24hIntIndex,
       "edfaPLA24hIntValidData": edfaPLA24hIntValidData,
       "edfaPLA24hIntTimeStamp": edfaPLA24hIntTimeStamp,
       "edfaPLA24hIntES": edfaPLA24hIntES,
       "edfaPLA24hIntLossOfSignal": edfaPLA24hIntLossOfSignal,
       "edfaPLA24hIntLossOfOop": edfaPLA24hIntLossOfOop,
       "edfaPLA1weekIntTable": edfaPLA1weekIntTable,
       "edfaPLA1weekIntEntry": edfaPLA1weekIntEntry,
       "edfaPLA1weekIntIndex": edfaPLA1weekIntIndex,
       "edfaPLA1weekIntValidData": edfaPLA1weekIntValidData,
       "edfaPLA1weekIntTimeStamp": edfaPLA1weekIntTimeStamp,
       "edfaPLA1weekIntES": edfaPLA1weekIntES,
       "edfaPLA1weekIntLossOfSignal": edfaPLA1weekIntLossOfSignal,
       "edfaPLA1weekIntLossOfOop": edfaPLA1weekIntLossOfOop,
       "edfaPLAcurrentTable": edfaPLAcurrentTable,
       "edfaPLAcurrentEntry": edfaPLAcurrentEntry,
       "edfaPLAcurrentIndex": edfaPLAcurrentIndex,
       "edfaPLAcurrentValidData": edfaPLAcurrentValidData,
       "edfaPLAcurrentElapsedTime": edfaPLAcurrentElapsedTime,
       "edfaPLAcurrentES": edfaPLAcurrentES,
       "edfaPLAcurrentLossOfSignal": edfaPLAcurrentLossOfSignal,
       "edfaPLAcurrentLossOfOop": edfaPLAcurrentLossOfOop,
       "ifPLA15minIntTable": ifPLA15minIntTable,
       "ifPLA15minIntEntry": ifPLA15minIntEntry,
       "ifPLA15minIntIndex": ifPLA15minIntIndex,
       "ifPLA15minIntValidData": ifPLA15minIntValidData,
       "ifPLA15minIntTimeStamp": ifPLA15minIntTimeStamp,
       "ifPLA15minIntES": ifPLA15minIntES,
       "ifPLA15minIntLossOfSignal": ifPLA15minIntLossOfSignal,
       "ifPLA15minIntLossOfSync": ifPLA15minIntLossOfSync,
       "ifPLA24hIntTable": ifPLA24hIntTable,
       "ifPLA24hIntEntry": ifPLA24hIntEntry,
       "ifPLA24hIntIndex": ifPLA24hIntIndex,
       "ifPLA24hIntValidData": ifPLA24hIntValidData,
       "ifPLA24hIntTimeStamp": ifPLA24hIntTimeStamp,
       "ifPLA24hIntES": ifPLA24hIntES,
       "ifPLA24hIntLossOfSignal": ifPLA24hIntLossOfSignal,
       "ifPLA24hIntLossOfSync": ifPLA24hIntLossOfSync,
       "ifPLA1weekIntTable": ifPLA1weekIntTable,
       "ifPLA1weekIntEntry": ifPLA1weekIntEntry,
       "ifPLA1weekIntIndex": ifPLA1weekIntIndex,
       "ifPLA1weekIntValidData": ifPLA1weekIntValidData,
       "ifPLA1weekIntTimeStamp": ifPLA1weekIntTimeStamp,
       "ifPLA1weekIntES": ifPLA1weekIntES,
       "ifPLA1weekIntLossOfSignal": ifPLA1weekIntLossOfSignal,
       "ifPLA1weekIntLossOfSync": ifPLA1weekIntLossOfSync,
       "ifPLAcurrentTable": ifPLAcurrentTable,
       "ifPLAcurrentEntry": ifPLAcurrentEntry,
       "ifPLAcurrentIndex": ifPLAcurrentIndex,
       "ifPLAcurrentValidData": ifPLAcurrentValidData,
       "ifPLAcurrentElapsedTime": ifPLAcurrentElapsedTime,
       "ifPLAcurrentES": ifPLAcurrentES,
       "ifPLAcurrentLossOfSignal": ifPLAcurrentLossOfSignal,
       "ifPLAcurrentLossOfSync": ifPLAcurrentLossOfSync,
       "performanceMIBConformance": performanceMIBConformance,
       "performanceMIBObjects": performanceMIBObjects}
)
