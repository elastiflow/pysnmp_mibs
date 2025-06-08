# SNMP MIB module (FspR7-SPEQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/FspR7-SPEQ-MIB.mib
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

(EntityClass,
 EntityIndex,
 ServiceImpairment,
 TrapAlarmSeverity,
 fspR7,
 neEventLogIdentityTranslation,
 neEventLogTimeStamp) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "EntityClass",
    "EntityIndex",
    "ServiceImpairment",
    "TrapAlarmSeverity",
    "fspR7",
    "neEventLogIdentityTranslation",
    "neEventLogTimeStamp")

(FspR7AdminState,
 FspR7AdminStateCaps,
 FspR7DisableEnable,
 FspR7EnableDisable,
 FspR7EntitySecondaryStates,
 FspR7Integer32Caps,
 FspR7OperState) = mibBuilder.importSymbols(
    "FspR7-MIB",
    "FspR7AdminState",
    "FspR7AdminStateCaps",
    "FspR7DisableEnable",
    "FspR7EnableDisable",
    "FspR7EntitySecondaryStates",
    "FspR7Integer32Caps",
    "FspR7OperState")

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
 enterprises,
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpModules")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

speqMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4)
)
if mibBuilder.loadTexts:
    speqMIB.setRevisions(
        ("2012-11-01 00:00",
         "2010-10-29 00:00",
         "2010-08-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FspR7SpeqAmpApsOper(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("ready", 1),
          ("inhibit", 2))
    )



class FspR7SpeqFendAmpApsOper(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("unknown", 1),
          ("ready", 2),
          ("inhibit", 3))
    )



class FspR7SpeqConfig(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("none", 1),
          ("disable", 2),
          ("enableGainAdopt", 3),
          ("enableNoGainAdopt", 4),
          ("qualify", 5))
    )



class FspR7SpeqDisableEnable(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("enable", 1),
          ("disable", 2))
    )



class FspR7SpeqFarEndConfig(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("unknown", 1),
          ("enable", 2),
          ("disable", 3))
    )



class FspR7SpeqNormalOutage(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("unknown", 1),
          ("normal", 2),
          ("outage", 3))
    )



class FspR7SpeqOperate(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("rls", 1),
          ("opr", 2))
    )



class FspR7SpeqOperateCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capRls", 1),
          ("capOpr", 2))
    )


class FspR7SpeqQualify(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("preAmp", 1),
          ("boosterAmp", 2),
          ("lineAmp", 3),
          ("brmn", 4))
    )



class FspR7SpeqOptLineService(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("addDrop", 1),
          ("passThrough", 2),
          ("hybrid", 3))
    )



class FspR7SpeqPpcLimit(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("four", 1),
          ("one", 2),
          ("seven", 3))
    )



class FspR7SpeqStatus(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("none", 1),
          ("inProgress", 2),
          ("lockedOut", 3))
    )



class FspR7SpeqStandingConditionTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              120000,
              120002,
              120004,
              120005,
              120006,
              120007,
              120008,
              120009,
              120010,
              120011,
              120012)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("oosDisabledSpeq", 120000),
          ("oosMaintenanceSpeq", 120002),
          ("messageLossSpeq", 120004),
          ("oscFiberMissingSpeq", 120005),
          ("optLowSpeq", 120006),
          ("ppcOutOfRangeSpeq", 120007),
          ("gainTooHighSpeq", 120008),
          ("gainTooLowSpeq", 120009),
          ("gainAdoptFailedSpeq", 120010),
          ("processLockedOutSpeq", 120011),
          ("ppcLimitExceededSpeq", 120012))
    )



# MIB Managed Objects in the order of their OIDs

_SpeqEntityMIB_ObjectIdentity = ObjectIdentity
speqEntityMIB = _SpeqEntityMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10)
)
_SpeqEntityTable_Object = MibTable
speqEntityTable = _SpeqEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 1)
)
if mibBuilder.loadTexts:
    speqEntityTable.setStatus("current")
_SpeqEntityEntry_Object = MibTableRow
speqEntityEntry = _SpeqEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 1, 1)
)
speqEntityEntry.setIndexNames(
    (0, "FspR7-SPEQ-MIB", "speqEntityIndex"),
)
if mibBuilder.loadTexts:
    speqEntityEntry.setStatus("current")
_SpeqEntityIndex_Type = EntityIndex
_SpeqEntityIndex_Object = MibTableColumn
speqEntityIndex = _SpeqEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 1, 1, 1),
    _SpeqEntityIndex_Type()
)
speqEntityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    speqEntityIndex.setStatus("current")
_SpeqEntityContainedIn_Type = EntityIndex
_SpeqEntityContainedIn_Object = MibTableColumn
speqEntityContainedIn = _SpeqEntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 1, 1, 2),
    _SpeqEntityContainedIn_Type()
)
speqEntityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqEntityContainedIn.setStatus("current")


class _SpeqEntityClassInstanceNumber_Type(Integer32):
    """Custom type speqEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_SpeqEntityClassInstanceNumber_Type.__name__ = "Integer32"
_SpeqEntityClassInstanceNumber_Object = MibTableColumn
speqEntityClassInstanceNumber = _SpeqEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 1, 1, 3),
    _SpeqEntityClassInstanceNumber_Type()
)
speqEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqEntityClassInstanceNumber.setStatus("current")
_SpeqEntityIndexAid_Type = SnmpAdminString
_SpeqEntityIndexAid_Object = MibTableColumn
speqEntityIndexAid = _SpeqEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 1, 1, 4),
    _SpeqEntityIndexAid_Type()
)
speqEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqEntityIndexAid.setStatus("current")
_SpeqContainsTable_Object = MibTable
speqContainsTable = _SpeqContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 2)
)
if mibBuilder.loadTexts:
    speqContainsTable.setStatus("current")
_SpeqContainsEntry_Object = MibTableRow
speqContainsEntry = _SpeqContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 2, 1)
)
speqContainsEntry.setIndexNames(
    (0, "FspR7-SPEQ-MIB", "speqEntityIndex"),
    (0, "FspR7-SPEQ-MIB", "speqContainsIndex"),
)
if mibBuilder.loadTexts:
    speqContainsEntry.setStatus("current")
_SpeqContainsIndex_Type = EntityIndex
_SpeqContainsIndex_Object = MibTableColumn
speqContainsIndex = _SpeqContainsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 10, 2, 1, 1),
    _SpeqContainsIndex_Type()
)
speqContainsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqContainsIndex.setStatus("current")
_SpeqConfigurationMIB_ObjectIdentity = ObjectIdentity
speqConfigurationMIB = _SpeqConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12)
)
_SpeqConfiguration_Type = FspR7SpeqConfig
_SpeqConfiguration_Object = MibScalar
speqConfiguration = _SpeqConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 1),
    _SpeqConfiguration_Type()
)
speqConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqConfiguration.setStatus("current")
_SpeqDynamicComp_Type = FspR7SpeqDisableEnable
_SpeqDynamicComp_Object = MibScalar
speqDynamicComp = _SpeqDynamicComp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 2),
    _SpeqDynamicComp_Type()
)
speqDynamicComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqDynamicComp.setStatus("current")
_SpeqAmpAps_Type = FspR7DisableEnable
_SpeqAmpAps_Object = MibScalar
speqAmpAps = _SpeqAmpAps_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 3),
    _SpeqAmpAps_Type()
)
speqAmpAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqAmpAps.setStatus("current")
_SpeqAlsConf_Type = FspR7EnableDisable
_SpeqAlsConf_Object = MibScalar
speqAlsConf = _SpeqAlsConf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 4),
    _SpeqAlsConf_Type()
)
speqAlsConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqAlsConf.setStatus("current")
_SpeqConfigTable_Object = MibTable
speqConfigTable = _SpeqConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 10)
)
if mibBuilder.loadTexts:
    speqConfigTable.setStatus("current")
_SpeqConfigEntry_Object = MibTableRow
speqConfigEntry = _SpeqConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 10, 1)
)
speqConfigEntry.setIndexNames(
    (0, "FspR7-SPEQ-MIB", "speqEntityIndex"),
)
if mibBuilder.loadTexts:
    speqConfigEntry.setStatus("current")
_SpeqConfigAdmin_Type = FspR7AdminState
_SpeqConfigAdmin_Object = MibTableColumn
speqConfigAdmin = _SpeqConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 10, 1, 1),
    _SpeqConfigAdmin_Type()
)
speqConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqConfigAdmin.setStatus("current")


class _SpeqConfigOpticalSetpoint_Type(Integer32):
    """Custom type speqConfigOpticalSetpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 50),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_SpeqConfigOpticalSetpoint_Type.__name__ = "Integer32"
_SpeqConfigOpticalSetpoint_Object = MibTableColumn
speqConfigOpticalSetpoint = _SpeqConfigOpticalSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 10, 1, 2),
    _SpeqConfigOpticalSetpoint_Type()
)
speqConfigOpticalSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqConfigOpticalSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    speqConfigOpticalSetpoint.setUnits("0.1 dBm")


class _SpeqConfigPerChannelPower_Type(Integer32):
    """Custom type speqConfigPerChannelPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 80),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_SpeqConfigPerChannelPower_Type.__name__ = "Integer32"
_SpeqConfigPerChannelPower_Object = MibTableColumn
speqConfigPerChannelPower = _SpeqConfigPerChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 10, 1, 3),
    _SpeqConfigPerChannelPower_Type()
)
speqConfigPerChannelPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqConfigPerChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    speqConfigPerChannelPower.setUnits("0.1 dBm")


class _SpeqConfigGainCal_Type(Integer32):
    """Custom type speqConfigGainCal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 60),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_SpeqConfigGainCal_Type.__name__ = "Integer32"
_SpeqConfigGainCal_Object = MibTableColumn
speqConfigGainCal = _SpeqConfigGainCal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 10, 1, 4),
    _SpeqConfigGainCal_Type()
)
speqConfigGainCal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqConfigGainCal.setStatus("current")
if mibBuilder.loadTexts:
    speqConfigGainCal.setUnits("0.1 dBm")
_SpeqConfigOperate_Type = FspR7SpeqOperate
_SpeqConfigOperate_Object = MibTableColumn
speqConfigOperate = _SpeqConfigOperate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 10, 1, 5),
    _SpeqConfigOperate_Type()
)
speqConfigOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqConfigOperate.setStatus("current")
_SpeqConfigCapTable_Object = MibTable
speqConfigCapTable = _SpeqConfigCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 11)
)
if mibBuilder.loadTexts:
    speqConfigCapTable.setStatus("current")
_SpeqConfigCapEntry_Object = MibTableRow
speqConfigCapEntry = _SpeqConfigCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 11, 1)
)
speqConfigCapEntry.setIndexNames(
    (0, "FspR7-SPEQ-MIB", "speqEntityIndex"),
)
if mibBuilder.loadTexts:
    speqConfigCapEntry.setStatus("current")
_SpeqConfigCapAdmin_Type = FspR7AdminStateCaps
_SpeqConfigCapAdmin_Object = MibTableColumn
speqConfigCapAdmin = _SpeqConfigCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 11, 1, 1),
    _SpeqConfigCapAdmin_Type()
)
speqConfigCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqConfigCapAdmin.setStatus("current")
_SpeqConfigCapOpticalSetpoint_Type = FspR7Integer32Caps
_SpeqConfigCapOpticalSetpoint_Object = MibTableColumn
speqConfigCapOpticalSetpoint = _SpeqConfigCapOpticalSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 11, 1, 2),
    _SpeqConfigCapOpticalSetpoint_Type()
)
speqConfigCapOpticalSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqConfigCapOpticalSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    speqConfigCapOpticalSetpoint.setUnits("0.1 dBm")
_SpeqConfigCapPerChannelPower_Type = FspR7Integer32Caps
_SpeqConfigCapPerChannelPower_Object = MibTableColumn
speqConfigCapPerChannelPower = _SpeqConfigCapPerChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 11, 1, 3),
    _SpeqConfigCapPerChannelPower_Type()
)
speqConfigCapPerChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqConfigCapPerChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    speqConfigCapPerChannelPower.setUnits("0.1 dBm")
_SpeqConfigCapGainCal_Type = FspR7Integer32Caps
_SpeqConfigCapGainCal_Object = MibTableColumn
speqConfigCapGainCal = _SpeqConfigCapGainCal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 11, 1, 4),
    _SpeqConfigCapGainCal_Type()
)
speqConfigCapGainCal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqConfigCapGainCal.setStatus("current")
if mibBuilder.loadTexts:
    speqConfigCapGainCal.setUnits("0.1 dBm")
_SpeqConfigCapOperate_Type = FspR7SpeqOperateCaps
_SpeqConfigCapOperate_Object = MibTableColumn
speqConfigCapOperate = _SpeqConfigCapOperate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 12, 11, 1, 5),
    _SpeqConfigCapOperate_Type()
)
speqConfigCapOperate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqConfigCapOperate.setStatus("current")
_SpeqStatusMIB_ObjectIdentity = ObjectIdentity
speqStatusMIB = _SpeqStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13)
)
_SpeqStatusTable_Object = MibTable
speqStatusTable = _SpeqStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10)
)
if mibBuilder.loadTexts:
    speqStatusTable.setStatus("current")
_SpeqStatusEntry_Object = MibTableRow
speqStatusEntry = _SpeqStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1)
)
speqStatusEntry.setIndexNames(
    (0, "FspR7-SPEQ-MIB", "speqEntityIndex"),
)
if mibBuilder.loadTexts:
    speqStatusEntry.setStatus("current")
_SpeqStatusOper_Type = FspR7OperState
_SpeqStatusOper_Object = MibTableColumn
speqStatusOper = _SpeqStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 1),
    _SpeqStatusOper_Type()
)
speqStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusOper.setStatus("current")
_SpeqStatusSecondaryStates_Type = FspR7EntitySecondaryStates
_SpeqStatusSecondaryStates_Object = MibTableColumn
speqStatusSecondaryStates = _SpeqStatusSecondaryStates_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 2),
    _SpeqStatusSecondaryStates_Type()
)
speqStatusSecondaryStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusSecondaryStates.setStatus("current")
_SpeqStatusQualify_Type = FspR7SpeqQualify
_SpeqStatusQualify_Object = MibTableColumn
speqStatusQualify = _SpeqStatusQualify_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 3),
    _SpeqStatusQualify_Type()
)
speqStatusQualify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusQualify.setStatus("current")
_SpeqStatusOpticalLineAid_Type = EntityIndex
_SpeqStatusOpticalLineAid_Object = MibTableColumn
speqStatusOpticalLineAid = _SpeqStatusOpticalLineAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 4),
    _SpeqStatusOpticalLineAid_Type()
)
speqStatusOpticalLineAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusOpticalLineAid.setStatus("current")
_SpeqStatusOscAid_Type = EntityIndex
_SpeqStatusOscAid_Object = MibTableColumn
speqStatusOscAid = _SpeqStatusOscAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 5),
    _SpeqStatusOscAid_Type()
)
speqStatusOscAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusOscAid.setStatus("current")
_SpeqStatusOpticalLineServiceType_Type = FspR7SpeqOptLineService
_SpeqStatusOpticalLineServiceType_Object = MibTableColumn
speqStatusOpticalLineServiceType = _SpeqStatusOpticalLineServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 6),
    _SpeqStatusOpticalLineServiceType_Type()
)
speqStatusOpticalLineServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusOpticalLineServiceType.setStatus("current")
_SpeqStatusPerChannelPowerLimit_Type = FspR7SpeqPpcLimit
_SpeqStatusPerChannelPowerLimit_Object = MibTableColumn
speqStatusPerChannelPowerLimit = _SpeqStatusPerChannelPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 7),
    _SpeqStatusPerChannelPowerLimit_Type()
)
speqStatusPerChannelPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusPerChannelPowerLimit.setStatus("current")
_SpeqStatusCalculatedGain_Type = Unsigned32
_SpeqStatusCalculatedGain_Object = MibTableColumn
speqStatusCalculatedGain = _SpeqStatusCalculatedGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 8),
    _SpeqStatusCalculatedGain_Type()
)
speqStatusCalculatedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusCalculatedGain.setStatus("current")
if mibBuilder.loadTexts:
    speqStatusCalculatedGain.setUnits("0.1 dB")
_SpeqStatusStatus_Type = FspR7SpeqStatus
_SpeqStatusStatus_Object = MibTableColumn
speqStatusStatus = _SpeqStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 9),
    _SpeqStatusStatus_Type()
)
speqStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusStatus.setStatus("current")
_SpeqStatusFarEndConfig_Type = FspR7SpeqFarEndConfig
_SpeqStatusFarEndConfig_Object = MibTableColumn
speqStatusFarEndConfig = _SpeqStatusFarEndConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 10),
    _SpeqStatusFarEndConfig_Type()
)
speqStatusFarEndConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusFarEndConfig.setStatus("current")
_SpeqStatusFarEndStatus_Type = FspR7SpeqStatus
_SpeqStatusFarEndStatus_Object = MibTableColumn
speqStatusFarEndStatus = _SpeqStatusFarEndStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 11),
    _SpeqStatusFarEndStatus_Type()
)
speqStatusFarEndStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusFarEndStatus.setStatus("current")
_SpeqStatusFarEndPpc_Type = Integer32
_SpeqStatusFarEndPpc_Object = MibTableColumn
speqStatusFarEndPpc = _SpeqStatusFarEndPpc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 12),
    _SpeqStatusFarEndPpc_Type()
)
speqStatusFarEndPpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusFarEndPpc.setStatus("current")
if mibBuilder.loadTexts:
    speqStatusFarEndPpc.setUnits("0.1 dBm")
_SpeqStatusFarEndOpt_Type = Integer32
_SpeqStatusFarEndOpt_Object = MibTableColumn
speqStatusFarEndOpt = _SpeqStatusFarEndOpt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 13),
    _SpeqStatusFarEndOpt_Type()
)
speqStatusFarEndOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusFarEndOpt.setStatus("current")
if mibBuilder.loadTexts:
    speqStatusFarEndOpt.setUnits("0.1 dBm")
_SpeqStatusFarEndOpr_Type = Integer32
_SpeqStatusFarEndOpr_Object = MibTableColumn
speqStatusFarEndOpr = _SpeqStatusFarEndOpr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 14),
    _SpeqStatusFarEndOpr_Type()
)
speqStatusFarEndOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusFarEndOpr.setStatus("current")
if mibBuilder.loadTexts:
    speqStatusFarEndOpr.setUnits("0.1 dBm")
_SpeqStatusNearEndOpt_Type = Integer32
_SpeqStatusNearEndOpt_Object = MibTableColumn
speqStatusNearEndOpt = _SpeqStatusNearEndOpt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 15),
    _SpeqStatusNearEndOpt_Type()
)
speqStatusNearEndOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusNearEndOpt.setStatus("current")
if mibBuilder.loadTexts:
    speqStatusNearEndOpt.setUnits("0.1 dBm")
_SpeqStatusNearEndOpr_Type = Integer32
_SpeqStatusNearEndOpr_Object = MibTableColumn
speqStatusNearEndOpr = _SpeqStatusNearEndOpr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 16),
    _SpeqStatusNearEndOpr_Type()
)
speqStatusNearEndOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusNearEndOpr.setStatus("current")
if mibBuilder.loadTexts:
    speqStatusNearEndOpr.setUnits("0.1 dBm")
_SpeqStatusAmpAps_Type = FspR7DisableEnable
_SpeqStatusAmpAps_Object = MibTableColumn
speqStatusAmpAps = _SpeqStatusAmpAps_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 17),
    _SpeqStatusAmpAps_Type()
)
speqStatusAmpAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusAmpAps.setStatus("current")
_SpeqStatusAmpApsOper_Type = FspR7SpeqAmpApsOper
_SpeqStatusAmpApsOper_Object = MibTableColumn
speqStatusAmpApsOper = _SpeqStatusAmpApsOper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 18),
    _SpeqStatusAmpApsOper_Type()
)
speqStatusAmpApsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusAmpApsOper.setStatus("current")
_SpeqStatusFarEndAmpApsOper_Type = FspR7SpeqFendAmpApsOper
_SpeqStatusFarEndAmpApsOper_Object = MibTableColumn
speqStatusFarEndAmpApsOper = _SpeqStatusFarEndAmpApsOper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 19),
    _SpeqStatusFarEndAmpApsOper_Type()
)
speqStatusFarEndAmpApsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusFarEndAmpApsOper.setStatus("current")
_SpeqStatusFarEndRcvSignal_Type = FspR7SpeqNormalOutage
_SpeqStatusFarEndRcvSignal_Object = MibTableColumn
speqStatusFarEndRcvSignal = _SpeqStatusFarEndRcvSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 20),
    _SpeqStatusFarEndRcvSignal_Type()
)
speqStatusFarEndRcvSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusFarEndRcvSignal.setStatus("current")
_SpeqStatusFarEndRcvOscSignal_Type = FspR7SpeqNormalOutage
_SpeqStatusFarEndRcvOscSignal_Object = MibTableColumn
speqStatusFarEndRcvOscSignal = _SpeqStatusFarEndRcvOscSignal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 13, 10, 1, 21),
    _SpeqStatusFarEndRcvOscSignal_Type()
)
speqStatusFarEndRcvOscSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqStatusFarEndRcvOscSignal.setStatus("current")
_SpeqAlarms_ObjectIdentity = ObjectIdentity
speqAlarms = _SpeqAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14)
)
_SpeqTraps_ObjectIdentity = ObjectIdentity
speqTraps = _SpeqTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1)
)
_SpeqTrapsPrefix_ObjectIdentity = ObjectIdentity
speqTrapsPrefix = _SpeqTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0)
)
_SpeqConditions_ObjectIdentity = ObjectIdentity
speqConditions = _SpeqConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2)
)
_SpeqConditionSeverityTable_Object = MibTable
speqConditionSeverityTable = _SpeqConditionSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 1)
)
if mibBuilder.loadTexts:
    speqConditionSeverityTable.setStatus("current")
_SpeqConditionSeverityEntry_Object = MibTableRow
speqConditionSeverityEntry = _SpeqConditionSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 1, 1)
)
speqConditionSeverityEntry.setIndexNames(
    (0, "FspR7-SPEQ-MIB", "speqEntityIndex"),
    (0, "FspR7-SPEQ-MIB", "speqConditionSeverityType"),
)
if mibBuilder.loadTexts:
    speqConditionSeverityEntry.setStatus("current")
_SpeqConditionSeverityType_Type = FspR7SpeqStandingConditionTypes
_SpeqConditionSeverityType_Object = MibTableColumn
speqConditionSeverityType = _SpeqConditionSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 1, 1, 1),
    _SpeqConditionSeverityType_Type()
)
speqConditionSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speqConditionSeverityType.setStatus("current")
_SpeqConditionSeverityValue_Type = TrapAlarmSeverity
_SpeqConditionSeverityValue_Object = MibTableColumn
speqConditionSeverityValue = _SpeqConditionSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 1, 1, 2),
    _SpeqConditionSeverityValue_Type()
)
speqConditionSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speqConditionSeverityValue.setStatus("current")
_SpeqCurrentConditionTable_Object = MibTable
speqCurrentConditionTable = _SpeqCurrentConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 2)
)
if mibBuilder.loadTexts:
    speqCurrentConditionTable.setStatus("current")
_SpeqCurrentConditionEntry_Object = MibTableRow
speqCurrentConditionEntry = _SpeqCurrentConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 2, 1)
)
speqCurrentConditionEntry.setIndexNames(
    (0, "FspR7-SPEQ-MIB", "speqEntityIndex"),
    (0, "FspR7-SPEQ-MIB", "speqCurrentConditionType"),
)
if mibBuilder.loadTexts:
    speqCurrentConditionEntry.setStatus("current")
_SpeqCurrentConditionType_Type = FspR7SpeqStandingConditionTypes
_SpeqCurrentConditionType_Object = MibTableColumn
speqCurrentConditionType = _SpeqCurrentConditionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 2, 1, 1),
    _SpeqCurrentConditionType_Type()
)
speqCurrentConditionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speqCurrentConditionType.setStatus("current")
_SpeqCurrentConditionSeverity_Type = TrapAlarmSeverity
_SpeqCurrentConditionSeverity_Object = MibTableColumn
speqCurrentConditionSeverity = _SpeqCurrentConditionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 2, 1, 2),
    _SpeqCurrentConditionSeverity_Type()
)
speqCurrentConditionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqCurrentConditionSeverity.setStatus("current")
_SpeqCurrentConditionAffect_Type = ServiceImpairment
_SpeqCurrentConditionAffect_Object = MibTableColumn
speqCurrentConditionAffect = _SpeqCurrentConditionAffect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 2, 1, 3),
    _SpeqCurrentConditionAffect_Type()
)
speqCurrentConditionAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqCurrentConditionAffect.setStatus("current")
_SpeqCurrentConditionTimeStamp_Type = DateAndTime
_SpeqCurrentConditionTimeStamp_Object = MibTableColumn
speqCurrentConditionTimeStamp = _SpeqCurrentConditionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 2, 2, 1, 4),
    _SpeqCurrentConditionTimeStamp_Type()
)
speqCurrentConditionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speqCurrentConditionTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects

alarmOosDisabledSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120000)
)
alarmOosDisabledSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmOosDisabledSpeq.setStatus(
        "current"
    )

alarmOosMaintenanceSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120002)
)
alarmOosMaintenanceSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmOosMaintenanceSpeq.setStatus(
        "current"
    )

alarmMessageLossSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120004)
)
alarmMessageLossSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmMessageLossSpeq.setStatus(
        "current"
    )

alarmOscFiberMissingSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120005)
)
alarmOscFiberMissingSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmOscFiberMissingSpeq.setStatus(
        "current"
    )

alarmOptLowSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120006)
)
alarmOptLowSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmOptLowSpeq.setStatus(
        "current"
    )

alarmPpcOutOfRangeSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120007)
)
alarmPpcOutOfRangeSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmPpcOutOfRangeSpeq.setStatus(
        "current"
    )

alarmGainTooHighSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120008)
)
alarmGainTooHighSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmGainTooHighSpeq.setStatus(
        "current"
    )

alarmGainTooLowSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120009)
)
alarmGainTooLowSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmGainTooLowSpeq.setStatus(
        "current"
    )

alarmGainAdoptFailedSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120010)
)
alarmGainAdoptFailedSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmGainAdoptFailedSpeq.setStatus(
        "current"
    )

alarmProcessLockedOutSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120011)
)
alarmProcessLockedOutSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmProcessLockedOutSpeq.setStatus(
        "current"
    )

alarmPpcLimitExceededSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 120012)
)
alarmPpcLimitExceededSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqCurrentConditionSeverity"),
        ("FspR7-SPEQ-MIB", "speqCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmPpcLimitExceededSpeq.setStatus(
        "current"
    )

speqCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 124001)
)
speqCreation.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    speqCreation.setStatus(
        "current"
    )

speqDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 124002)
)
speqDeletion.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    speqDeletion.setStatus(
        "current"
    )

speqStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 124003)
)
speqStateChange.setObjects(
      *(("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    speqStateChange.setStatus(
        "current"
    )

speqObjectChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 124004)
)
speqObjectChange.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    speqObjectChange.setStatus(
        "current"
    )

transientGainAutoAdjustSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126000)
)
transientGainAutoAdjustSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientGainAutoAdjustSpeq.setStatus(
        "current"
    )

transientGainNoAdjustSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126001)
)
transientGainNoAdjustSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientGainNoAdjustSpeq.setStatus(
        "current"
    )

transientGainAdjustFailedSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126002)
)
transientGainAdjustFailedSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientGainAdjustFailedSpeq.setStatus(
        "current"
    )

transientWaitSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126003)
)
transientWaitSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientWaitSpeq.setStatus(
        "current"
    )

transientDenySpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126004)
)
transientDenySpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientDenySpeq.setStatus(
        "current"
    )

transientPpcAdoptSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126005)
)
transientPpcAdoptSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientPpcAdoptSpeq.setStatus(
        "current"
    )

transientPpcLimitExceededSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126006)
)
transientPpcLimitExceededSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientPpcLimitExceededSpeq.setStatus(
        "deprecated"
    )

transientGainDynamicAdjustSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126007)
)
transientGainDynamicAdjustSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientGainDynamicAdjustSpeq.setStatus(
        "current"
    )

transientAmpApsEnabledSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126008)
)
transientAmpApsEnabledSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientAmpApsEnabledSpeq.setStatus(
        "current"
    )

transientAmpApsDisabledSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126009)
)
transientAmpApsDisabledSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientAmpApsDisabledSpeq.setStatus(
        "current"
    )

transientGainManualAdjustSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126010)
)
transientGainManualAdjustSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientGainManualAdjustSpeq.setStatus(
        "current"
    )

transientDynamicCompEnabledSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126011)
)
transientDynamicCompEnabledSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientDynamicCompEnabledSpeq.setStatus(
        "current"
    )

transientDynamicCompDisabledSpeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 4, 14, 1, 0, 126012)
)
transientDynamicCompDisabledSpeq.setObjects(
      *(("FspR7-SPEQ-MIB", "speqEntityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientDynamicCompDisabledSpeq.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FspR7-SPEQ-MIB",
    **{"FspR7SpeqAmpApsOper": FspR7SpeqAmpApsOper,
       "FspR7SpeqFendAmpApsOper": FspR7SpeqFendAmpApsOper,
       "FspR7SpeqConfig": FspR7SpeqConfig,
       "FspR7SpeqDisableEnable": FspR7SpeqDisableEnable,
       "FspR7SpeqFarEndConfig": FspR7SpeqFarEndConfig,
       "FspR7SpeqNormalOutage": FspR7SpeqNormalOutage,
       "FspR7SpeqOperate": FspR7SpeqOperate,
       "FspR7SpeqOperateCaps": FspR7SpeqOperateCaps,
       "FspR7SpeqQualify": FspR7SpeqQualify,
       "FspR7SpeqOptLineService": FspR7SpeqOptLineService,
       "FspR7SpeqPpcLimit": FspR7SpeqPpcLimit,
       "FspR7SpeqStatus": FspR7SpeqStatus,
       "FspR7SpeqStandingConditionTypes": FspR7SpeqStandingConditionTypes,
       "speqMIB": speqMIB,
       "speqEntityMIB": speqEntityMIB,
       "speqEntityTable": speqEntityTable,
       "speqEntityEntry": speqEntityEntry,
       "speqEntityIndex": speqEntityIndex,
       "speqEntityContainedIn": speqEntityContainedIn,
       "speqEntityClassInstanceNumber": speqEntityClassInstanceNumber,
       "speqEntityIndexAid": speqEntityIndexAid,
       "speqContainsTable": speqContainsTable,
       "speqContainsEntry": speqContainsEntry,
       "speqContainsIndex": speqContainsIndex,
       "speqConfigurationMIB": speqConfigurationMIB,
       "speqConfiguration": speqConfiguration,
       "speqDynamicComp": speqDynamicComp,
       "speqAmpAps": speqAmpAps,
       "speqAlsConf": speqAlsConf,
       "speqConfigTable": speqConfigTable,
       "speqConfigEntry": speqConfigEntry,
       "speqConfigAdmin": speqConfigAdmin,
       "speqConfigOpticalSetpoint": speqConfigOpticalSetpoint,
       "speqConfigPerChannelPower": speqConfigPerChannelPower,
       "speqConfigGainCal": speqConfigGainCal,
       "speqConfigOperate": speqConfigOperate,
       "speqConfigCapTable": speqConfigCapTable,
       "speqConfigCapEntry": speqConfigCapEntry,
       "speqConfigCapAdmin": speqConfigCapAdmin,
       "speqConfigCapOpticalSetpoint": speqConfigCapOpticalSetpoint,
       "speqConfigCapPerChannelPower": speqConfigCapPerChannelPower,
       "speqConfigCapGainCal": speqConfigCapGainCal,
       "speqConfigCapOperate": speqConfigCapOperate,
       "speqStatusMIB": speqStatusMIB,
       "speqStatusTable": speqStatusTable,
       "speqStatusEntry": speqStatusEntry,
       "speqStatusOper": speqStatusOper,
       "speqStatusSecondaryStates": speqStatusSecondaryStates,
       "speqStatusQualify": speqStatusQualify,
       "speqStatusOpticalLineAid": speqStatusOpticalLineAid,
       "speqStatusOscAid": speqStatusOscAid,
       "speqStatusOpticalLineServiceType": speqStatusOpticalLineServiceType,
       "speqStatusPerChannelPowerLimit": speqStatusPerChannelPowerLimit,
       "speqStatusCalculatedGain": speqStatusCalculatedGain,
       "speqStatusStatus": speqStatusStatus,
       "speqStatusFarEndConfig": speqStatusFarEndConfig,
       "speqStatusFarEndStatus": speqStatusFarEndStatus,
       "speqStatusFarEndPpc": speqStatusFarEndPpc,
       "speqStatusFarEndOpt": speqStatusFarEndOpt,
       "speqStatusFarEndOpr": speqStatusFarEndOpr,
       "speqStatusNearEndOpt": speqStatusNearEndOpt,
       "speqStatusNearEndOpr": speqStatusNearEndOpr,
       "speqStatusAmpAps": speqStatusAmpAps,
       "speqStatusAmpApsOper": speqStatusAmpApsOper,
       "speqStatusFarEndAmpApsOper": speqStatusFarEndAmpApsOper,
       "speqStatusFarEndRcvSignal": speqStatusFarEndRcvSignal,
       "speqStatusFarEndRcvOscSignal": speqStatusFarEndRcvOscSignal,
       "speqAlarms": speqAlarms,
       "speqTraps": speqTraps,
       "speqTrapsPrefix": speqTrapsPrefix,
       "alarmOosDisabledSpeq": alarmOosDisabledSpeq,
       "alarmOosMaintenanceSpeq": alarmOosMaintenanceSpeq,
       "alarmMessageLossSpeq": alarmMessageLossSpeq,
       "alarmOscFiberMissingSpeq": alarmOscFiberMissingSpeq,
       "alarmOptLowSpeq": alarmOptLowSpeq,
       "alarmPpcOutOfRangeSpeq": alarmPpcOutOfRangeSpeq,
       "alarmGainTooHighSpeq": alarmGainTooHighSpeq,
       "alarmGainTooLowSpeq": alarmGainTooLowSpeq,
       "alarmGainAdoptFailedSpeq": alarmGainAdoptFailedSpeq,
       "alarmProcessLockedOutSpeq": alarmProcessLockedOutSpeq,
       "alarmPpcLimitExceededSpeq": alarmPpcLimitExceededSpeq,
       "speqCreation": speqCreation,
       "speqDeletion": speqDeletion,
       "speqStateChange": speqStateChange,
       "speqObjectChange": speqObjectChange,
       "transientGainAutoAdjustSpeq": transientGainAutoAdjustSpeq,
       "transientGainNoAdjustSpeq": transientGainNoAdjustSpeq,
       "transientGainAdjustFailedSpeq": transientGainAdjustFailedSpeq,
       "transientWaitSpeq": transientWaitSpeq,
       "transientDenySpeq": transientDenySpeq,
       "transientPpcAdoptSpeq": transientPpcAdoptSpeq,
       "transientPpcLimitExceededSpeq": transientPpcLimitExceededSpeq,
       "transientGainDynamicAdjustSpeq": transientGainDynamicAdjustSpeq,
       "transientAmpApsEnabledSpeq": transientAmpApsEnabledSpeq,
       "transientAmpApsDisabledSpeq": transientAmpApsDisabledSpeq,
       "transientGainManualAdjustSpeq": transientGainManualAdjustSpeq,
       "transientDynamicCompEnabledSpeq": transientDynamicCompEnabledSpeq,
       "transientDynamicCompDisabledSpeq": transientDynamicCompDisabledSpeq,
       "speqConditions": speqConditions,
       "speqConditionSeverityTable": speqConditionSeverityTable,
       "speqConditionSeverityEntry": speqConditionSeverityEntry,
       "speqConditionSeverityType": speqConditionSeverityType,
       "speqConditionSeverityValue": speqConditionSeverityValue,
       "speqCurrentConditionTable": speqCurrentConditionTable,
       "speqCurrentConditionEntry": speqCurrentConditionEntry,
       "speqCurrentConditionType": speqCurrentConditionType,
       "speqCurrentConditionSeverity": speqCurrentConditionSeverity,
       "speqCurrentConditionAffect": speqCurrentConditionAffect,
       "speqCurrentConditionTimeStamp": speqCurrentConditionTimeStamp}
)
