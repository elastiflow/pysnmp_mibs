# SNMP MIB module (ALU-REMOTE-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-REMOTE-MONITORING-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:25 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

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

(tmnxChassisIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex")

(TItemLongDescription,
 TNamedItemOrEmpty) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemLongDescription",
    "TNamedItemOrEmpty")


# MODULE-IDENTITY

aluRMMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    aluRMMIBModule.setRevisions(
        ("1908-01-09 00:00",
         "1921-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluRMAlias(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class AluRMExtAlarmID(TextualConvention, Unsigned32):
    status = "current"


class AluRMAdminStatus(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("disabled", 1),
          ("enabled", 2))
    )



class AluRMOperStatus(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("ghost", 1),
          ("not-monitored", 2),
          ("ok", 3),
          ("active", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AluRMMIBConformance_ObjectIdentity = ObjectIdentity
aluRMMIBConformance = _AluRMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11)
)
_AluRMConformance_ObjectIdentity = ObjectIdentity
aluRMConformance = _AluRMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11)
)
_AluRMCompliances_ObjectIdentity = ObjectIdentity
aluRMCompliances = _AluRMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11, 1)
)
_AluRMComp7705_ObjectIdentity = ObjectIdentity
aluRMComp7705 = _AluRMComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11, 1, 1)
)
_AluRMGroups_ObjectIdentity = ObjectIdentity
aluRMGroups = _AluRMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11, 2)
)
_AluRMObjPrefix_ObjectIdentity = ObjectIdentity
aluRMObjPrefix = _AluRMObjPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11)
)
_AluRMObjs_ObjectIdentity = ObjectIdentity
aluRMObjs = _AluRMObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1)
)
_AluRMTriggerTable_Object = MibTable
aluRMTriggerTable = _AluRMTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    aluRMTriggerTable.setStatus("current")
_AluRMTriggerEntry_Object = MibTableRow
aluRMTriggerEntry = _AluRMTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1)
)
aluRMTriggerEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-REMOTE-MONITORING-MIB", "aluRMTriggerID"),
)
if mibBuilder.loadTexts:
    aluRMTriggerEntry.setStatus("current")
_AluRMTriggerID_Type = AluRMExtAlarmID
_AluRMTriggerID_Object = MibTableColumn
aluRMTriggerID = _AluRMTriggerID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 1),
    _AluRMTriggerID_Type()
)
aluRMTriggerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluRMTriggerID.setStatus("current")
_AluRMTriggerName_Type = TNamedItemOrEmpty
_AluRMTriggerName_Object = MibTableColumn
aluRMTriggerName = _AluRMTriggerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 2),
    _AluRMTriggerName_Type()
)
aluRMTriggerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRMTriggerName.setStatus("current")


class _AluRMTriggerAdminStatus_Type(AluRMAdminStatus):
    """Custom type aluRMTriggerAdminStatus based on AluRMAdminStatus"""
    defaultValue = 2


_AluRMTriggerAdminStatus_Type.__name__ = "AluRMAdminStatus"
_AluRMTriggerAdminStatus_Object = MibTableColumn
aluRMTriggerAdminStatus = _AluRMTriggerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 3),
    _AluRMTriggerAdminStatus_Type()
)
aluRMTriggerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMTriggerAdminStatus.setStatus("current")
_AluRMTriggerOperStatus_Type = AluRMOperStatus
_AluRMTriggerOperStatus_Object = MibTableColumn
aluRMTriggerOperStatus = _AluRMTriggerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 4),
    _AluRMTriggerOperStatus_Type()
)
aluRMTriggerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRMTriggerOperStatus.setStatus("current")


class _AluRMTriggerDescription_Type(TItemLongDescription):
    """Custom type aluRMTriggerDescription based on TItemLongDescription"""
    defaultHexValue = ""


_AluRMTriggerDescription_Type.__name__ = "TItemLongDescription"
_AluRMTriggerDescription_Object = MibTableColumn
aluRMTriggerDescription = _AluRMTriggerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 5),
    _AluRMTriggerDescription_Type()
)
aluRMTriggerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMTriggerDescription.setStatus("current")


class _AluRMTriggerDetectDebounce_Type(Unsigned32):
    """Custom type aluRMTriggerDetectDebounce based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AluRMTriggerDetectDebounce_Type.__name__ = "Unsigned32"
_AluRMTriggerDetectDebounce_Object = MibTableColumn
aluRMTriggerDetectDebounce = _AluRMTriggerDetectDebounce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 6),
    _AluRMTriggerDetectDebounce_Type()
)
aluRMTriggerDetectDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMTriggerDetectDebounce.setStatus("current")
if mibBuilder.loadTexts:
    aluRMTriggerDetectDebounce.setUnits("seconds")


class _AluRMTriggerClearDebounce_Type(Unsigned32):
    """Custom type aluRMTriggerClearDebounce based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AluRMTriggerClearDebounce_Type.__name__ = "Unsigned32"
_AluRMTriggerClearDebounce_Object = MibTableColumn
aluRMTriggerClearDebounce = _AluRMTriggerClearDebounce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 7),
    _AluRMTriggerClearDebounce_Type()
)
aluRMTriggerClearDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMTriggerClearDebounce.setStatus("current")
if mibBuilder.loadTexts:
    aluRMTriggerClearDebounce.setUnits("seconds")
_AluRMTriggerAnalogVoltage_Type = Integer32
_AluRMTriggerAnalogVoltage_Object = MibTableColumn
aluRMTriggerAnalogVoltage = _AluRMTriggerAnalogVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 8),
    _AluRMTriggerAnalogVoltage_Type()
)
aluRMTriggerAnalogVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRMTriggerAnalogVoltage.setStatus("current")
if mibBuilder.loadTexts:
    aluRMTriggerAnalogVoltage.setUnits("millivoltage")


class _AluRMTriggerDigitalState_Type(Integer32):
    """Custom type aluRMTriggerDigitalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("closed", 1),
          ("open", 2))
    )


_AluRMTriggerDigitalState_Type.__name__ = "Integer32"
_AluRMTriggerDigitalState_Object = MibTableColumn
aluRMTriggerDigitalState = _AluRMTriggerDigitalState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 9),
    _AluRMTriggerDigitalState_Type()
)
aluRMTriggerDigitalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRMTriggerDigitalState.setStatus("current")
_AluRMTriggerAlias_Type = AluRMAlias
_AluRMTriggerAlias_Object = MibTableColumn
aluRMTriggerAlias = _AluRMTriggerAlias_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 10),
    _AluRMTriggerAlias_Type()
)
aluRMTriggerAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMTriggerAlias.setStatus("current")


class _AluRMTriggerDigitalNorm_Type(Integer32):
    """Custom type aluRMTriggerDigitalNorm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("normally-closed", 1),
          ("normally-open", 2))
    )


_AluRMTriggerDigitalNorm_Type.__name__ = "Integer32"
_AluRMTriggerDigitalNorm_Object = MibTableColumn
aluRMTriggerDigitalNorm = _AluRMTriggerDigitalNorm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 1, 1, 11),
    _AluRMTriggerDigitalNorm_Type()
)
aluRMTriggerDigitalNorm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMTriggerDigitalNorm.setStatus("current")
_AluRMRelayTable_Object = MibTable
aluRMRelayTable = _AluRMRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2)
)
if mibBuilder.loadTexts:
    aluRMRelayTable.setStatus("current")
_AluRMRelayEntry_Object = MibTableRow
aluRMRelayEntry = _AluRMRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2, 1)
)
aluRMRelayEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-REMOTE-MONITORING-MIB", "aluRMRelayID"),
)
if mibBuilder.loadTexts:
    aluRMRelayEntry.setStatus("current")
_AluRMRelayID_Type = AluRMExtAlarmID
_AluRMRelayID_Object = MibTableColumn
aluRMRelayID = _AluRMRelayID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2, 1, 1),
    _AluRMRelayID_Type()
)
aluRMRelayID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluRMRelayID.setStatus("current")
_AluRMRelayName_Type = TNamedItemOrEmpty
_AluRMRelayName_Object = MibTableColumn
aluRMRelayName = _AluRMRelayName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2, 1, 2),
    _AluRMRelayName_Type()
)
aluRMRelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRMRelayName.setStatus("current")


class _AluRMRelayMode_Type(Integer32):
    """Custom type aluRMRelayMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 1),
          ("triggered", 2))
    )


_AluRMRelayMode_Type.__name__ = "Integer32"
_AluRMRelayMode_Object = MibTableColumn
aluRMRelayMode = _AluRMRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2, 1, 3),
    _AluRMRelayMode_Type()
)
aluRMRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMRelayMode.setStatus("current")


class _AluRMRelayAdminStatus_Type(AluRMAdminStatus):
    """Custom type aluRMRelayAdminStatus based on AluRMAdminStatus"""
    defaultValue = 2


_AluRMRelayAdminStatus_Type.__name__ = "AluRMAdminStatus"
_AluRMRelayAdminStatus_Object = MibTableColumn
aluRMRelayAdminStatus = _AluRMRelayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2, 1, 4),
    _AluRMRelayAdminStatus_Type()
)
aluRMRelayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMRelayAdminStatus.setStatus("current")
_AluRMRelayOperStatus_Type = AluRMOperStatus
_AluRMRelayOperStatus_Object = MibTableColumn
aluRMRelayOperStatus = _AluRMRelayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2, 1, 5),
    _AluRMRelayOperStatus_Type()
)
aluRMRelayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRMRelayOperStatus.setStatus("current")


class _AluRMRelayDescription_Type(TItemLongDescription):
    """Custom type aluRMRelayDescription based on TItemLongDescription"""
    defaultHexValue = ""


_AluRMRelayDescription_Type.__name__ = "TItemLongDescription"
_AluRMRelayDescription_Object = MibTableColumn
aluRMRelayDescription = _AluRMRelayDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2, 1, 6),
    _AluRMRelayDescription_Type()
)
aluRMRelayDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMRelayDescription.setStatus("current")
_AluRMRelayAlias_Type = AluRMAlias
_AluRMRelayAlias_Object = MibTableColumn
aluRMRelayAlias = _AluRMRelayAlias_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 2, 1, 7),
    _AluRMRelayAlias_Type()
)
aluRMRelayAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluRMRelayAlias.setStatus("current")
_AluRMAlarmTable_Object = MibTable
aluRMAlarmTable = _AluRMAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3)
)
if mibBuilder.loadTexts:
    aluRMAlarmTable.setStatus("current")
_AluRMAlarmEntry_Object = MibTableRow
aluRMAlarmEntry = _AluRMAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1)
)
aluRMAlarmEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-REMOTE-MONITORING-MIB", "aluRMAlarmID"),
)
if mibBuilder.loadTexts:
    aluRMAlarmEntry.setStatus("current")


class _AluRMAlarmID_Type(Unsigned32):
    """Custom type aluRMAlarmID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AluRMAlarmID_Type.__name__ = "Unsigned32"
_AluRMAlarmID_Object = MibTableColumn
aluRMAlarmID = _AluRMAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 1),
    _AluRMAlarmID_Type()
)
aluRMAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluRMAlarmID.setStatus("current")
_AluRMAlarmRowStatus_Type = RowStatus
_AluRMAlarmRowStatus_Object = MibTableColumn
aluRMAlarmRowStatus = _AluRMAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 2),
    _AluRMAlarmRowStatus_Type()
)
aluRMAlarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmRowStatus.setStatus("current")


class _AluRMAlarmAdminStatus_Type(AluRMAdminStatus):
    """Custom type aluRMAlarmAdminStatus based on AluRMAdminStatus"""
    defaultValue = 1


_AluRMAlarmAdminStatus_Type.__name__ = "AluRMAdminStatus"
_AluRMAlarmAdminStatus_Object = MibTableColumn
aluRMAlarmAdminStatus = _AluRMAlarmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 3),
    _AluRMAlarmAdminStatus_Type()
)
aluRMAlarmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmAdminStatus.setStatus("current")
_AluRMAlarmOperStatus_Type = AluRMOperStatus
_AluRMAlarmOperStatus_Object = MibTableColumn
aluRMAlarmOperStatus = _AluRMAlarmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 4),
    _AluRMAlarmOperStatus_Type()
)
aluRMAlarmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRMAlarmOperStatus.setStatus("current")


class _AluRMAlarmDescription_Type(TItemLongDescription):
    """Custom type aluRMAlarmDescription based on TItemLongDescription"""
    defaultHexValue = ""


_AluRMAlarmDescription_Type.__name__ = "TItemLongDescription"
_AluRMAlarmDescription_Object = MibTableColumn
aluRMAlarmDescription = _AluRMAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 5),
    _AluRMAlarmDescription_Type()
)
aluRMAlarmDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmDescription.setStatus("current")


class _AluRMAlarmTriggerRule_Type(Integer32):
    """Custom type aluRMAlarmTriggerRule based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any-trigger", 1),
          ("all-triggers", 2))
    )


_AluRMAlarmTriggerRule_Type.__name__ = "Integer32"
_AluRMAlarmTriggerRule_Object = MibTableColumn
aluRMAlarmTriggerRule = _AluRMAlarmTriggerRule_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 6),
    _AluRMAlarmTriggerRule_Type()
)
aluRMAlarmTriggerRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTriggerRule.setStatus("current")
_AluRMAlarmTrigger1_Type = AluRMExtAlarmID
_AluRMAlarmTrigger1_Object = MibTableColumn
aluRMAlarmTrigger1 = _AluRMAlarmTrigger1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 7),
    _AluRMAlarmTrigger1_Type()
)
aluRMAlarmTrigger1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTrigger1.setStatus("current")
_AluRMAlarmTrigger2_Type = AluRMExtAlarmID
_AluRMAlarmTrigger2_Object = MibTableColumn
aluRMAlarmTrigger2 = _AluRMAlarmTrigger2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 8),
    _AluRMAlarmTrigger2_Type()
)
aluRMAlarmTrigger2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTrigger2.setStatus("current")
_AluRMAlarmTrigger3_Type = AluRMExtAlarmID
_AluRMAlarmTrigger3_Object = MibTableColumn
aluRMAlarmTrigger3 = _AluRMAlarmTrigger3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 9),
    _AluRMAlarmTrigger3_Type()
)
aluRMAlarmTrigger3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTrigger3.setStatus("current")
_AluRMAlarmTrigger4_Type = AluRMExtAlarmID
_AluRMAlarmTrigger4_Object = MibTableColumn
aluRMAlarmTrigger4 = _AluRMAlarmTrigger4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 10),
    _AluRMAlarmTrigger4_Type()
)
aluRMAlarmTrigger4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTrigger4.setStatus("current")
_AluRMAlarmTrigger5_Type = AluRMExtAlarmID
_AluRMAlarmTrigger5_Object = MibTableColumn
aluRMAlarmTrigger5 = _AluRMAlarmTrigger5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 11),
    _AluRMAlarmTrigger5_Type()
)
aluRMAlarmTrigger5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTrigger5.setStatus("current")
_AluRMAlarmTrigger6_Type = AluRMExtAlarmID
_AluRMAlarmTrigger6_Object = MibTableColumn
aluRMAlarmTrigger6 = _AluRMAlarmTrigger6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 12),
    _AluRMAlarmTrigger6_Type()
)
aluRMAlarmTrigger6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTrigger6.setStatus("current")
_AluRMAlarmTrigger7_Type = AluRMExtAlarmID
_AluRMAlarmTrigger7_Object = MibTableColumn
aluRMAlarmTrigger7 = _AluRMAlarmTrigger7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 13),
    _AluRMAlarmTrigger7_Type()
)
aluRMAlarmTrigger7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTrigger7.setStatus("current")
_AluRMAlarmTrigger8_Type = AluRMExtAlarmID
_AluRMAlarmTrigger8_Object = MibTableColumn
aluRMAlarmTrigger8 = _AluRMAlarmTrigger8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 14),
    _AluRMAlarmTrigger8_Type()
)
aluRMAlarmTrigger8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTrigger8.setStatus("current")


class _AluRMAlarmSeverity_Type(Integer32):
    """Custom type aluRMAlarmSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )


_AluRMAlarmSeverity_Type.__name__ = "Integer32"
_AluRMAlarmSeverity_Object = MibTableColumn
aluRMAlarmSeverity = _AluRMAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 15),
    _AluRMAlarmSeverity_Type()
)
aluRMAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmSeverity.setStatus("current")


class _AluRMAlarmActionLog_Type(TruthValue):
    """Custom type aluRMAlarmActionLog based on TruthValue"""
    defaultValue = 1


_AluRMAlarmActionLog_Type.__name__ = "TruthValue"
_AluRMAlarmActionLog_Object = MibTableColumn
aluRMAlarmActionLog = _AluRMAlarmActionLog_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 16),
    _AluRMAlarmActionLog_Type()
)
aluRMAlarmActionLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmActionLog.setStatus("current")


class _AluRMAlarmActionAlarmRelay_Type(TruthValue):
    """Custom type aluRMAlarmActionAlarmRelay based on TruthValue"""
    defaultValue = 1


_AluRMAlarmActionAlarmRelay_Type.__name__ = "TruthValue"
_AluRMAlarmActionAlarmRelay_Object = MibTableColumn
aluRMAlarmActionAlarmRelay = _AluRMAlarmActionAlarmRelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 17),
    _AluRMAlarmActionAlarmRelay_Type()
)
aluRMAlarmActionAlarmRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmActionAlarmRelay.setStatus("current")


class _AluRMAlarmActionAuxRelay_Type(TruthValue):
    """Custom type aluRMAlarmActionAuxRelay based on TruthValue"""
    defaultValue = 2


_AluRMAlarmActionAuxRelay_Type.__name__ = "TruthValue"
_AluRMAlarmActionAuxRelay_Object = MibTableColumn
aluRMAlarmActionAuxRelay = _AluRMAlarmActionAuxRelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 18),
    _AluRMAlarmActionAuxRelay_Type()
)
aluRMAlarmActionAuxRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmActionAuxRelay.setStatus("current")
_AluRMAlarmAuxRelay_Type = AluRMExtAlarmID
_AluRMAlarmAuxRelay_Object = MibTableColumn
aluRMAlarmAuxRelay = _AluRMAlarmAuxRelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 19),
    _AluRMAlarmAuxRelay_Type()
)
aluRMAlarmAuxRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmAuxRelay.setStatus("current")
_AluRMAlarmDetectedTriggers_Type = Unsigned32
_AluRMAlarmDetectedTriggers_Object = MibTableColumn
aluRMAlarmDetectedTriggers = _AluRMAlarmDetectedTriggers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 20),
    _AluRMAlarmDetectedTriggers_Type()
)
aluRMAlarmDetectedTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluRMAlarmDetectedTriggers.setStatus("current")


class _AluRMAlarmTHAnalogLevelOperation_Type(Integer32):
    """Custom type aluRMAlarmTHAnalogLevelOperation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-monitored", 0),
          ("greater-than", 1),
          ("less-than", 2))
    )


_AluRMAlarmTHAnalogLevelOperation_Type.__name__ = "Integer32"
_AluRMAlarmTHAnalogLevelOperation_Object = MibTableColumn
aluRMAlarmTHAnalogLevelOperation = _AluRMAlarmTHAnalogLevelOperation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 21),
    _AluRMAlarmTHAnalogLevelOperation_Type()
)
aluRMAlarmTHAnalogLevelOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTHAnalogLevelOperation.setStatus("current")


class _AluRMAlarmTHAnalogLevel_Type(Integer32):
    """Custom type aluRMAlarmTHAnalogLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 75000),
    )


_AluRMAlarmTHAnalogLevel_Type.__name__ = "Integer32"
_AluRMAlarmTHAnalogLevel_Object = MibTableColumn
aluRMAlarmTHAnalogLevel = _AluRMAlarmTHAnalogLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 1, 3, 1, 22),
    _AluRMAlarmTHAnalogLevel_Type()
)
aluRMAlarmTHAnalogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluRMAlarmTHAnalogLevel.setStatus("current")
if mibBuilder.loadTexts:
    aluRMAlarmTHAnalogLevel.setUnits("millivolts")
_AluRMNotifyObjs_ObjectIdentity = ObjectIdentity
aluRMNotifyObjs = _AluRMNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 2)
)
_AluRMAlarmNotifyID_Type = Unsigned32
_AluRMAlarmNotifyID_Object = MibScalar
aluRMAlarmNotifyID = _AluRMAlarmNotifyID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 2, 1),
    _AluRMAlarmNotifyID_Type()
)
aluRMAlarmNotifyID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluRMAlarmNotifyID.setStatus("current")
_AluRMAlarmNotifyDescription_Type = TItemLongDescription
_AluRMAlarmNotifyDescription_Object = MibScalar
aluRMAlarmNotifyDescription = _AluRMAlarmNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 2, 2),
    _AluRMAlarmNotifyDescription_Type()
)
aluRMAlarmNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluRMAlarmNotifyDescription.setStatus("current")
_AluRMNotifyID_Type = AluRMExtAlarmID
_AluRMNotifyID_Object = MibScalar
aluRMNotifyID = _AluRMNotifyID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 2, 3),
    _AluRMNotifyID_Type()
)
aluRMNotifyID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluRMNotifyID.setStatus("current")
_AluRMNotifyOperState_Type = AluRMOperStatus
_AluRMNotifyOperState_Object = MibScalar
aluRMNotifyOperState = _AluRMNotifyOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 11, 2, 4),
    _AluRMNotifyOperState_Type()
)
aluRMNotifyOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluRMNotifyOperState.setStatus("current")
_AluRMNotifyPrefix_ObjectIdentity = ObjectIdentity
aluRMNotifyPrefix = _AluRMNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 7)
)
_AluRMNotification_ObjectIdentity = ObjectIdentity
aluRMNotification = _AluRMNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 7, 0)
)

# Managed Objects groups

aluRMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11, 2, 1)
)
aluRMGroup.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerName"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerAdminStatus"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerOperStatus"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerDetectDebounce"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerClearDebounce"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerAnalogVoltage"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerDigitalState"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerAlias"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMRelayName"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMRelayMode"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMRelayAdminStatus"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMRelayOperStatus"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMRelayDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMRelayAlias"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmRowStatus"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmAdminStatus"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmOperStatus"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTriggerRule"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTrigger1"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTrigger2"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTrigger3"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTrigger4"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTrigger5"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTrigger6"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTrigger7"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTrigger8"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmSeverity"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmActionLog"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmActionAlarmRelay"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmActionAuxRelay"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmAuxRelay"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmDetectedTriggers"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTHAnalogLevelOperation"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmTHAnalogLevel"))
)
if mibBuilder.loadTexts:
    aluRMGroup.setStatus("current")

aluRMNotificationObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11, 2, 3)
)
aluRMNotificationObjsGroup.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyID"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMNotifyID"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMNotifyOperState"))
)
if mibBuilder.loadTexts:
    aluRMNotificationObjsGroup.setStatus("current")

aluRMDigitalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11, 2, 4)
)
aluRMDigitalGroup.setObjects(
    ("ALU-REMOTE-MONITORING-MIB", "aluRMTriggerDigitalNorm")
)
if mibBuilder.loadTexts:
    aluRMDigitalGroup.setStatus("current")


# Notification objects

aluRMCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 7, 0, 1)
)
aluRMCriticalAlarm.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyID"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmDetectedTriggers"))
)
if mibBuilder.loadTexts:
    aluRMCriticalAlarm.setStatus(
        "current"
    )

aluRMMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 7, 0, 2)
)
aluRMMajorAlarm.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyID"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmDetectedTriggers"))
)
if mibBuilder.loadTexts:
    aluRMMajorAlarm.setStatus(
        "current"
    )

aluRMMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 7, 0, 3)
)
aluRMMinorAlarm.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyID"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmDetectedTriggers"))
)
if mibBuilder.loadTexts:
    aluRMMinorAlarm.setStatus(
        "current"
    )

aluRMWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 7, 0, 4)
)
aluRMWarningAlarm.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyID"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmDetectedTriggers"))
)
if mibBuilder.loadTexts:
    aluRMWarningAlarm.setStatus(
        "current"
    )

aluRMClearingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 7, 0, 5)
)
aluRMClearingAlarm.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyID"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmNotifyDescription"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMAlarmDetectedTriggers"))
)
if mibBuilder.loadTexts:
    aluRMClearingAlarm.setStatus(
        "current"
    )

aluRMOperStateUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 7, 0, 6)
)
aluRMOperStateUpdate.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMNotifyID"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMNotifyOperState"))
)
if mibBuilder.loadTexts:
    aluRMOperStateUpdate.setStatus(
        "current"
    )


# Notifications groups

aluRMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11, 2, 2)
)
aluRMNotificationGroup.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMCriticalAlarm"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMMajorAlarm"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMMinorAlarm"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMWarningAlarm"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMClearingAlarm"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMOperStateUpdate"))
)
if mibBuilder.loadTexts:
    aluRMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluRMComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 11, 11, 1, 1, 1)
)
aluRMComp7705V1v0.setObjects(
      *(("ALU-REMOTE-MONITORING-MIB", "aluRMGroup"),
        ("ALU-REMOTE-MONITORING-MIB", "aluRMNotificationGroup"))
)
if mibBuilder.loadTexts:
    aluRMComp7705V1v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-REMOTE-MONITORING-MIB",
    **{"AluRMAlias": AluRMAlias,
       "AluRMExtAlarmID": AluRMExtAlarmID,
       "AluRMAdminStatus": AluRMAdminStatus,
       "AluRMOperStatus": AluRMOperStatus,
       "aluRMMIBModule": aluRMMIBModule,
       "aluRMMIBConformance": aluRMMIBConformance,
       "aluRMConformance": aluRMConformance,
       "aluRMCompliances": aluRMCompliances,
       "aluRMComp7705": aluRMComp7705,
       "aluRMComp7705V1v0": aluRMComp7705V1v0,
       "aluRMGroups": aluRMGroups,
       "aluRMGroup": aluRMGroup,
       "aluRMNotificationGroup": aluRMNotificationGroup,
       "aluRMNotificationObjsGroup": aluRMNotificationObjsGroup,
       "aluRMDigitalGroup": aluRMDigitalGroup,
       "aluRMObjPrefix": aluRMObjPrefix,
       "aluRMObjs": aluRMObjs,
       "aluRMTriggerTable": aluRMTriggerTable,
       "aluRMTriggerEntry": aluRMTriggerEntry,
       "aluRMTriggerID": aluRMTriggerID,
       "aluRMTriggerName": aluRMTriggerName,
       "aluRMTriggerAdminStatus": aluRMTriggerAdminStatus,
       "aluRMTriggerOperStatus": aluRMTriggerOperStatus,
       "aluRMTriggerDescription": aluRMTriggerDescription,
       "aluRMTriggerDetectDebounce": aluRMTriggerDetectDebounce,
       "aluRMTriggerClearDebounce": aluRMTriggerClearDebounce,
       "aluRMTriggerAnalogVoltage": aluRMTriggerAnalogVoltage,
       "aluRMTriggerDigitalState": aluRMTriggerDigitalState,
       "aluRMTriggerAlias": aluRMTriggerAlias,
       "aluRMTriggerDigitalNorm": aluRMTriggerDigitalNorm,
       "aluRMRelayTable": aluRMRelayTable,
       "aluRMRelayEntry": aluRMRelayEntry,
       "aluRMRelayID": aluRMRelayID,
       "aluRMRelayName": aluRMRelayName,
       "aluRMRelayMode": aluRMRelayMode,
       "aluRMRelayAdminStatus": aluRMRelayAdminStatus,
       "aluRMRelayOperStatus": aluRMRelayOperStatus,
       "aluRMRelayDescription": aluRMRelayDescription,
       "aluRMRelayAlias": aluRMRelayAlias,
       "aluRMAlarmTable": aluRMAlarmTable,
       "aluRMAlarmEntry": aluRMAlarmEntry,
       "aluRMAlarmID": aluRMAlarmID,
       "aluRMAlarmRowStatus": aluRMAlarmRowStatus,
       "aluRMAlarmAdminStatus": aluRMAlarmAdminStatus,
       "aluRMAlarmOperStatus": aluRMAlarmOperStatus,
       "aluRMAlarmDescription": aluRMAlarmDescription,
       "aluRMAlarmTriggerRule": aluRMAlarmTriggerRule,
       "aluRMAlarmTrigger1": aluRMAlarmTrigger1,
       "aluRMAlarmTrigger2": aluRMAlarmTrigger2,
       "aluRMAlarmTrigger3": aluRMAlarmTrigger3,
       "aluRMAlarmTrigger4": aluRMAlarmTrigger4,
       "aluRMAlarmTrigger5": aluRMAlarmTrigger5,
       "aluRMAlarmTrigger6": aluRMAlarmTrigger6,
       "aluRMAlarmTrigger7": aluRMAlarmTrigger7,
       "aluRMAlarmTrigger8": aluRMAlarmTrigger8,
       "aluRMAlarmSeverity": aluRMAlarmSeverity,
       "aluRMAlarmActionLog": aluRMAlarmActionLog,
       "aluRMAlarmActionAlarmRelay": aluRMAlarmActionAlarmRelay,
       "aluRMAlarmActionAuxRelay": aluRMAlarmActionAuxRelay,
       "aluRMAlarmAuxRelay": aluRMAlarmAuxRelay,
       "aluRMAlarmDetectedTriggers": aluRMAlarmDetectedTriggers,
       "aluRMAlarmTHAnalogLevelOperation": aluRMAlarmTHAnalogLevelOperation,
       "aluRMAlarmTHAnalogLevel": aluRMAlarmTHAnalogLevel,
       "aluRMNotifyObjs": aluRMNotifyObjs,
       "aluRMAlarmNotifyID": aluRMAlarmNotifyID,
       "aluRMAlarmNotifyDescription": aluRMAlarmNotifyDescription,
       "aluRMNotifyID": aluRMNotifyID,
       "aluRMNotifyOperState": aluRMNotifyOperState,
       "aluRMNotifyPrefix": aluRMNotifyPrefix,
       "aluRMNotification": aluRMNotification,
       "aluRMCriticalAlarm": aluRMCriticalAlarm,
       "aluRMMajorAlarm": aluRMMajorAlarm,
       "aluRMMinorAlarm": aluRMMinorAlarm,
       "aluRMWarningAlarm": aluRMWarningAlarm,
       "aluRMClearingAlarm": aluRMClearingAlarm,
       "aluRMOperStateUpdate": aluRMOperStateUpdate}
)
