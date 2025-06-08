# SNMP MIB module (TIMETRA-SCHEDULER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SCHEDULER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:35:22 2025
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

(schedEntry,) = mibBuilder.importSymbols(
    "DISMAN-SCHEDULE-MIB",
    "schedEntry")

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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(sapBaseInfoEntry,) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapBaseInfoEntry")

(ServObjName,
 custMultiServiceSiteEntry) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "ServObjName",
    "custMultiServiceSiteEntry")

(TItemDescription,
 TNamedItem) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem")


# MODULE-IDENTITY

tmnxSchedulerMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 37)
)
if mibBuilder.loadTexts:
    tmnxSchedulerMIBModule.setRevisions(
        ("2007-01-01 00:00",
         "2006-03-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPolicyOrFilterId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxTimeRangeDay(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )



class TmnxTimeRangeHour(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )



class TmnxTimeRangePeriodicEndHour(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )



class TmnxTimeRangeMinute(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )



class TmnxTimeRangeMonth(TextualConvention, Integer32):
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
        *(("january", 0),
          ("february", 1),
          ("march", 2),
          ("april", 3),
          ("may", 4),
          ("june", 5),
          ("july", 6),
          ("august", 7),
          ("september", 8),
          ("october", 9),
          ("november", 10),
          ("december", 11))
    )



class TmnxTimeRangeWeekday(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6),
          ("daily", 7),
          ("weekDay", 8),
          ("weekend", 9))
    )



class TmnxTimeRangeYear(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2005, 2099),
    )



class TmnxTodSuiteControlledObj(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ingressIpFilter", 0),
          ("ingressIPv6Filter", 1),
          ("ingressMacFilter", 2),
          ("ingressQosPlcy", 3),
          ("ingressQosSchedPlcy", 4),
          ("egressIpFilter", 5),
          ("egressIPv6Filter", 6),
          ("egressMacFilter", 7),
          ("egressQosPlcy", 8),
          ("egressQosSchedPlcy", 9))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSchedulerCompliance_ObjectIdentity = ObjectIdentity
tmnxSchedulerCompliance = _TmnxSchedulerCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37)
)
_TmnxSchedulerCompliances_ObjectIdentity = ObjectIdentity
tmnxSchedulerCompliances = _TmnxSchedulerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 1)
)
_TmnxTimeOfDayPlcyGroups_ObjectIdentity = ObjectIdentity
tmnxTimeOfDayPlcyGroups = _TmnxTimeOfDayPlcyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 2)
)
_TmnxCronSchedGroups_ObjectIdentity = ObjectIdentity
tmnxCronSchedGroups = _TmnxCronSchedGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 3)
)
_TmnxScheduler_ObjectIdentity = ObjectIdentity
tmnxScheduler = _TmnxScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37)
)
_TmnxTimeOfDayPlcyObjects_ObjectIdentity = ObjectIdentity
tmnxTimeOfDayPlcyObjects = _TmnxTimeOfDayPlcyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1)
)
_TmnxTimeRangeObjects_ObjectIdentity = ObjectIdentity
tmnxTimeRangeObjects = _TmnxTimeRangeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1)
)
_TmnxTimeRangeTableLastChange_Type = TimeStamp
_TmnxTimeRangeTableLastChange_Object = MibScalar
tmnxTimeRangeTableLastChange = _TmnxTimeRangeTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 1),
    _TmnxTimeRangeTableLastChange_Type()
)
tmnxTimeRangeTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTimeRangeTableLastChange.setStatus("current")
_TmnxTimeRangeTable_Object = MibTable
tmnxTimeRangeTable = _TmnxTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxTimeRangeTable.setStatus("current")
_TmnxTimeRangeEntry_Object = MibTableRow
tmnxTimeRangeEntry = _TmnxTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 2, 1)
)
tmnxTimeRangeEntry.setIndexNames(
    (0, "TIMETRA-SCHEDULER-MIB", "tTimeRangeName"),
)
if mibBuilder.loadTexts:
    tmnxTimeRangeEntry.setStatus("current")
_TTimeRangeName_Type = TNamedItem
_TTimeRangeName_Object = MibTableColumn
tTimeRangeName = _TTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 2, 1, 1),
    _TTimeRangeName_Type()
)
tTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTimeRangeName.setStatus("current")
_TTimeRangeRowStatus_Type = RowStatus
_TTimeRangeRowStatus_Object = MibTableColumn
tTimeRangeRowStatus = _TTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 2, 1, 2),
    _TTimeRangeRowStatus_Type()
)
tTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTimeRangeRowStatus.setStatus("current")
_TTimeRangeLastMgmtChange_Type = TimeStamp
_TTimeRangeLastMgmtChange_Object = MibTableColumn
tTimeRangeLastMgmtChange = _TTimeRangeLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 2, 1, 3),
    _TTimeRangeLastMgmtChange_Type()
)
tTimeRangeLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTimeRangeLastMgmtChange.setStatus("current")


class _TTimeRangeDescription_Type(TItemDescription):
    """Custom type tTimeRangeDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TTimeRangeDescription_Type.__name__ = "TItemDescription"
_TTimeRangeDescription_Object = MibTableColumn
tTimeRangeDescription = _TTimeRangeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 2, 1, 4),
    _TTimeRangeDescription_Type()
)
tTimeRangeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTimeRangeDescription.setStatus("current")
_TTimeRangeTriggers_Type = Counter32
_TTimeRangeTriggers_Object = MibTableColumn
tTimeRangeTriggers = _TTimeRangeTriggers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 2, 1, 5),
    _TTimeRangeTriggers_Type()
)
tTimeRangeTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTimeRangeTriggers.setStatus("current")
_TTimeRangeActive_Type = TruthValue
_TTimeRangeActive_Object = MibTableColumn
tTimeRangeActive = _TTimeRangeActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 2, 1, 6),
    _TTimeRangeActive_Type()
)
tTimeRangeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTimeRangeActive.setStatus("current")
_TmnxPeriodTRngeParmsTblLstChnge_Type = TimeStamp
_TmnxPeriodTRngeParmsTblLstChnge_Object = MibScalar
tmnxPeriodTRngeParmsTblLstChnge = _TmnxPeriodTRngeParmsTblLstChnge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 3),
    _TmnxPeriodTRngeParmsTblLstChnge_Type()
)
tmnxPeriodTRngeParmsTblLstChnge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPeriodTRngeParmsTblLstChnge.setStatus("current")
_TmnxPeriodicTimeRangeParmsTable_Object = MibTable
tmnxPeriodicTimeRangeParmsTable = _TmnxPeriodicTimeRangeParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxPeriodicTimeRangeParmsTable.setStatus("current")
_TmnxPeriodicTimeRangeParmsEntry_Object = MibTableRow
tmnxPeriodicTimeRangeParmsEntry = _TmnxPeriodicTimeRangeParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1)
)
tmnxPeriodicTimeRangeParmsEntry.setIndexNames(
    (0, "TIMETRA-SCHEDULER-MIB", "tTimeRangeName"),
    (0, "TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeStartWeekDay"),
    (0, "TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeStartHour"),
    (0, "TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeStartMinute"),
)
if mibBuilder.loadTexts:
    tmnxPeriodicTimeRangeParmsEntry.setStatus("current")
_TPeriodicTimeRangeStartWeekDay_Type = TmnxTimeRangeWeekday
_TPeriodicTimeRangeStartWeekDay_Object = MibTableColumn
tPeriodicTimeRangeStartWeekDay = _TPeriodicTimeRangeStartWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 1),
    _TPeriodicTimeRangeStartWeekDay_Type()
)
tPeriodicTimeRangeStartWeekDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeStartWeekDay.setStatus("current")
_TPeriodicTimeRangeStartHour_Type = TmnxTimeRangeHour
_TPeriodicTimeRangeStartHour_Object = MibTableColumn
tPeriodicTimeRangeStartHour = _TPeriodicTimeRangeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 2),
    _TPeriodicTimeRangeStartHour_Type()
)
tPeriodicTimeRangeStartHour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeStartHour.setStatus("current")
_TPeriodicTimeRangeStartMinute_Type = TmnxTimeRangeMinute
_TPeriodicTimeRangeStartMinute_Object = MibTableColumn
tPeriodicTimeRangeStartMinute = _TPeriodicTimeRangeStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 3),
    _TPeriodicTimeRangeStartMinute_Type()
)
tPeriodicTimeRangeStartMinute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeStartMinute.setStatus("current")
_TPeriodicTimeRangeRowStatus_Type = RowStatus
_TPeriodicTimeRangeRowStatus_Object = MibTableColumn
tPeriodicTimeRangeRowStatus = _TPeriodicTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 4),
    _TPeriodicTimeRangeRowStatus_Type()
)
tPeriodicTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeRowStatus.setStatus("current")
_TPeriodicTimeRangeLastMgmtChg_Type = TimeStamp
_TPeriodicTimeRangeLastMgmtChg_Object = MibTableColumn
tPeriodicTimeRangeLastMgmtChg = _TPeriodicTimeRangeLastMgmtChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 5),
    _TPeriodicTimeRangeLastMgmtChg_Type()
)
tPeriodicTimeRangeLastMgmtChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeLastMgmtChg.setStatus("current")
_TPeriodicTimeRangeEndWeekDay_Type = TmnxTimeRangeWeekday
_TPeriodicTimeRangeEndWeekDay_Object = MibTableColumn
tPeriodicTimeRangeEndWeekDay = _TPeriodicTimeRangeEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 6),
    _TPeriodicTimeRangeEndWeekDay_Type()
)
tPeriodicTimeRangeEndWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeEndWeekDay.setStatus("current")


class _TPeriodicTimeRangeEndHour_Type(TmnxTimeRangePeriodicEndHour):
    """Custom type tPeriodicTimeRangeEndHour based on TmnxTimeRangePeriodicEndHour"""
    defaultValue = 24


_TPeriodicTimeRangeEndHour_Type.__name__ = "TmnxTimeRangePeriodicEndHour"
_TPeriodicTimeRangeEndHour_Object = MibTableColumn
tPeriodicTimeRangeEndHour = _TPeriodicTimeRangeEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 7),
    _TPeriodicTimeRangeEndHour_Type()
)
tPeriodicTimeRangeEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeEndHour.setStatus("current")


class _TPeriodicTimeRangeEndMinute_Type(TmnxTimeRangeMinute):
    """Custom type tPeriodicTimeRangeEndMinute based on TmnxTimeRangeMinute"""
    defaultValue = 0


_TPeriodicTimeRangeEndMinute_Type.__name__ = "TmnxTimeRangeMinute"
_TPeriodicTimeRangeEndMinute_Object = MibTableColumn
tPeriodicTimeRangeEndMinute = _TPeriodicTimeRangeEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 8),
    _TPeriodicTimeRangeEndMinute_Type()
)
tPeriodicTimeRangeEndMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeEndMinute.setStatus("current")
_TPeriodicTimeRangeActive_Type = TruthValue
_TPeriodicTimeRangeActive_Object = MibTableColumn
tPeriodicTimeRangeActive = _TPeriodicTimeRangeActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 4, 1, 9),
    _TPeriodicTimeRangeActive_Type()
)
tPeriodicTimeRangeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPeriodicTimeRangeActive.setStatus("current")
_TmnxAbsTRngeParmsTblLstChnge_Type = TimeStamp
_TmnxAbsTRngeParmsTblLstChnge_Object = MibScalar
tmnxAbsTRngeParmsTblLstChnge = _TmnxAbsTRngeParmsTblLstChnge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 5),
    _TmnxAbsTRngeParmsTblLstChnge_Type()
)
tmnxAbsTRngeParmsTblLstChnge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAbsTRngeParmsTblLstChnge.setStatus("current")
_TmnxAbsoluteTimeRangeParmsTable_Object = MibTable
tmnxAbsoluteTimeRangeParmsTable = _TmnxAbsoluteTimeRangeParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxAbsoluteTimeRangeParmsTable.setStatus("current")
_TmnxAbsoluteTimeRangeParmsEntry_Object = MibTableRow
tmnxAbsoluteTimeRangeParmsEntry = _TmnxAbsoluteTimeRangeParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1)
)
tmnxAbsoluteTimeRangeParmsEntry.setIndexNames(
    (0, "TIMETRA-SCHEDULER-MIB", "tTimeRangeName"),
    (0, "TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeStartYear"),
    (0, "TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeStartMonth"),
    (0, "TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeStartDay"),
    (0, "TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeStartHour"),
    (0, "TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeStartMinute"),
)
if mibBuilder.loadTexts:
    tmnxAbsoluteTimeRangeParmsEntry.setStatus("current")
_TAbsoluteTimeRangeStartYear_Type = TmnxTimeRangeYear
_TAbsoluteTimeRangeStartYear_Object = MibTableColumn
tAbsoluteTimeRangeStartYear = _TAbsoluteTimeRangeStartYear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 1),
    _TAbsoluteTimeRangeStartYear_Type()
)
tAbsoluteTimeRangeStartYear.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeStartYear.setStatus("current")
_TAbsoluteTimeRangeStartMonth_Type = TmnxTimeRangeMonth
_TAbsoluteTimeRangeStartMonth_Object = MibTableColumn
tAbsoluteTimeRangeStartMonth = _TAbsoluteTimeRangeStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 2),
    _TAbsoluteTimeRangeStartMonth_Type()
)
tAbsoluteTimeRangeStartMonth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeStartMonth.setStatus("current")
_TAbsoluteTimeRangeStartDay_Type = TmnxTimeRangeDay
_TAbsoluteTimeRangeStartDay_Object = MibTableColumn
tAbsoluteTimeRangeStartDay = _TAbsoluteTimeRangeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 3),
    _TAbsoluteTimeRangeStartDay_Type()
)
tAbsoluteTimeRangeStartDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeStartDay.setStatus("current")
_TAbsoluteTimeRangeStartHour_Type = TmnxTimeRangeHour
_TAbsoluteTimeRangeStartHour_Object = MibTableColumn
tAbsoluteTimeRangeStartHour = _TAbsoluteTimeRangeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 4),
    _TAbsoluteTimeRangeStartHour_Type()
)
tAbsoluteTimeRangeStartHour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeStartHour.setStatus("current")
_TAbsoluteTimeRangeStartMinute_Type = TmnxTimeRangeMinute
_TAbsoluteTimeRangeStartMinute_Object = MibTableColumn
tAbsoluteTimeRangeStartMinute = _TAbsoluteTimeRangeStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 5),
    _TAbsoluteTimeRangeStartMinute_Type()
)
tAbsoluteTimeRangeStartMinute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeStartMinute.setStatus("current")
_TAbsoluteTimeRangeRowStatus_Type = RowStatus
_TAbsoluteTimeRangeRowStatus_Object = MibTableColumn
tAbsoluteTimeRangeRowStatus = _TAbsoluteTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 6),
    _TAbsoluteTimeRangeRowStatus_Type()
)
tAbsoluteTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeRowStatus.setStatus("current")
_TAbsoluteTimeRangeLastMgmtChg_Type = TimeStamp
_TAbsoluteTimeRangeLastMgmtChg_Object = MibTableColumn
tAbsoluteTimeRangeLastMgmtChg = _TAbsoluteTimeRangeLastMgmtChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 7),
    _TAbsoluteTimeRangeLastMgmtChg_Type()
)
tAbsoluteTimeRangeLastMgmtChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeLastMgmtChg.setStatus("current")


class _TAbsoluteTimeRangeEndYear_Type(TmnxTimeRangeYear):
    """Custom type tAbsoluteTimeRangeEndYear based on TmnxTimeRangeYear"""
    defaultValue = 2099


_TAbsoluteTimeRangeEndYear_Type.__name__ = "TmnxTimeRangeYear"
_TAbsoluteTimeRangeEndYear_Object = MibTableColumn
tAbsoluteTimeRangeEndYear = _TAbsoluteTimeRangeEndYear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 8),
    _TAbsoluteTimeRangeEndYear_Type()
)
tAbsoluteTimeRangeEndYear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeEndYear.setStatus("current")


class _TAbsoluteTimeRangeEndMonth_Type(TmnxTimeRangeMonth):
    """Custom type tAbsoluteTimeRangeEndMonth based on TmnxTimeRangeMonth"""
    defaultValue = 11


_TAbsoluteTimeRangeEndMonth_Type.__name__ = "TmnxTimeRangeMonth"
_TAbsoluteTimeRangeEndMonth_Object = MibTableColumn
tAbsoluteTimeRangeEndMonth = _TAbsoluteTimeRangeEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 9),
    _TAbsoluteTimeRangeEndMonth_Type()
)
tAbsoluteTimeRangeEndMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeEndMonth.setStatus("current")


class _TAbsoluteTimeRangeEndDay_Type(TmnxTimeRangeDay):
    """Custom type tAbsoluteTimeRangeEndDay based on TmnxTimeRangeDay"""
    defaultValue = 31


_TAbsoluteTimeRangeEndDay_Type.__name__ = "TmnxTimeRangeDay"
_TAbsoluteTimeRangeEndDay_Object = MibTableColumn
tAbsoluteTimeRangeEndDay = _TAbsoluteTimeRangeEndDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 10),
    _TAbsoluteTimeRangeEndDay_Type()
)
tAbsoluteTimeRangeEndDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeEndDay.setStatus("current")


class _TAbsoluteTimeRangeEndHour_Type(TmnxTimeRangeHour):
    """Custom type tAbsoluteTimeRangeEndHour based on TmnxTimeRangeHour"""
    defaultValue = 23


_TAbsoluteTimeRangeEndHour_Type.__name__ = "TmnxTimeRangeHour"
_TAbsoluteTimeRangeEndHour_Object = MibTableColumn
tAbsoluteTimeRangeEndHour = _TAbsoluteTimeRangeEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 11),
    _TAbsoluteTimeRangeEndHour_Type()
)
tAbsoluteTimeRangeEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeEndHour.setStatus("current")


class _TAbsoluteTimeRangeEndMinute_Type(TmnxTimeRangeMinute):
    """Custom type tAbsoluteTimeRangeEndMinute based on TmnxTimeRangeMinute"""
    defaultValue = 59


_TAbsoluteTimeRangeEndMinute_Type.__name__ = "TmnxTimeRangeMinute"
_TAbsoluteTimeRangeEndMinute_Object = MibTableColumn
tAbsoluteTimeRangeEndMinute = _TAbsoluteTimeRangeEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 12),
    _TAbsoluteTimeRangeEndMinute_Type()
)
tAbsoluteTimeRangeEndMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeEndMinute.setStatus("current")
_TAbsoluteTimeRangeActive_Type = TruthValue
_TAbsoluteTimeRangeActive_Object = MibTableColumn
tAbsoluteTimeRangeActive = _TAbsoluteTimeRangeActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 1, 6, 1, 13),
    _TAbsoluteTimeRangeActive_Type()
)
tAbsoluteTimeRangeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAbsoluteTimeRangeActive.setStatus("current")
_TmnxToDSuiteObjects_ObjectIdentity = ObjectIdentity
tmnxToDSuiteObjects = _TmnxToDSuiteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3)
)
_TmnxTodSuiteTableLastChange_Type = TimeStamp
_TmnxTodSuiteTableLastChange_Object = MibScalar
tmnxTodSuiteTableLastChange = _TmnxTodSuiteTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 1),
    _TmnxTodSuiteTableLastChange_Type()
)
tmnxTodSuiteTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTodSuiteTableLastChange.setStatus("current")
_TmnxTodSuiteTable_Object = MibTable
tmnxTodSuiteTable = _TmnxTodSuiteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxTodSuiteTable.setStatus("current")
_TmnxTodSuiteEntry_Object = MibTableRow
tmnxTodSuiteEntry = _TmnxTodSuiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1)
)
tmnxTodSuiteEntry.setIndexNames(
    (0, "TIMETRA-SCHEDULER-MIB", "tTodSuiteName"),
)
if mibBuilder.loadTexts:
    tmnxTodSuiteEntry.setStatus("current")
_TTodSuiteName_Type = TNamedItem
_TTodSuiteName_Object = MibTableColumn
tTodSuiteName = _TTodSuiteName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 1),
    _TTodSuiteName_Type()
)
tTodSuiteName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTodSuiteName.setStatus("current")
_TTodSuiteRowStatus_Type = RowStatus
_TTodSuiteRowStatus_Object = MibTableColumn
tTodSuiteRowStatus = _TTodSuiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 2),
    _TTodSuiteRowStatus_Type()
)
tTodSuiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTodSuiteRowStatus.setStatus("current")
_TTodSuiteLastChanged_Type = TimeStamp
_TTodSuiteLastChanged_Object = MibTableColumn
tTodSuiteLastChanged = _TTodSuiteLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 3),
    _TTodSuiteLastChanged_Type()
)
tTodSuiteLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteLastChanged.setStatus("current")


class _TTodSuiteDescription_Type(TItemDescription):
    """Custom type tTodSuiteDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TTodSuiteDescription_Type.__name__ = "TItemDescription"
_TTodSuiteDescription_Object = MibTableColumn
tTodSuiteDescription = _TTodSuiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 4),
    _TTodSuiteDescription_Type()
)
tTodSuiteDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTodSuiteDescription.setStatus("current")
_TTodSuiteOprIngrIpFilterIndex_Type = TmnxPolicyOrFilterId
_TTodSuiteOprIngrIpFilterIndex_Object = MibTableColumn
tTodSuiteOprIngrIpFilterIndex = _TTodSuiteOprIngrIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 5),
    _TTodSuiteOprIngrIpFilterIndex_Type()
)
tTodSuiteOprIngrIpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprIngrIpFilterIndex.setStatus("current")
_TTodSuiteOprIngrIpv6FilterIndex_Type = TmnxPolicyOrFilterId
_TTodSuiteOprIngrIpv6FilterIndex_Object = MibTableColumn
tTodSuiteOprIngrIpv6FilterIndex = _TTodSuiteOprIngrIpv6FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 6),
    _TTodSuiteOprIngrIpv6FilterIndex_Type()
)
tTodSuiteOprIngrIpv6FilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprIngrIpv6FilterIndex.setStatus("current")
_TTodSuiteOprIngrMacFilterIndex_Type = TmnxPolicyOrFilterId
_TTodSuiteOprIngrMacFilterIndex_Object = MibTableColumn
tTodSuiteOprIngrMacFilterIndex = _TTodSuiteOprIngrMacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 7),
    _TTodSuiteOprIngrMacFilterIndex_Type()
)
tTodSuiteOprIngrMacFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprIngrMacFilterIndex.setStatus("current")
_TTodSuiteOprIngrQosPolicyId_Type = TmnxPolicyOrFilterId
_TTodSuiteOprIngrQosPolicyId_Object = MibTableColumn
tTodSuiteOprIngrQosPolicyId = _TTodSuiteOprIngrQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 8),
    _TTodSuiteOprIngrQosPolicyId_Type()
)
tTodSuiteOprIngrQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprIngrQosPolicyId.setStatus("current")
_TTodSuiteOprIngrQosSchedulerPlcy_Type = ServObjName
_TTodSuiteOprIngrQosSchedulerPlcy_Object = MibTableColumn
tTodSuiteOprIngrQosSchedulerPlcy = _TTodSuiteOprIngrQosSchedulerPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 9),
    _TTodSuiteOprIngrQosSchedulerPlcy_Type()
)
tTodSuiteOprIngrQosSchedulerPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprIngrQosSchedulerPlcy.setStatus("current")
_TTodSuiteOprEgrIpFilterIndex_Type = TmnxPolicyOrFilterId
_TTodSuiteOprEgrIpFilterIndex_Object = MibTableColumn
tTodSuiteOprEgrIpFilterIndex = _TTodSuiteOprEgrIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 10),
    _TTodSuiteOprEgrIpFilterIndex_Type()
)
tTodSuiteOprEgrIpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprEgrIpFilterIndex.setStatus("current")
_TTodSuiteOprEgrIpv6FilterIndex_Type = TmnxPolicyOrFilterId
_TTodSuiteOprEgrIpv6FilterIndex_Object = MibTableColumn
tTodSuiteOprEgrIpv6FilterIndex = _TTodSuiteOprEgrIpv6FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 11),
    _TTodSuiteOprEgrIpv6FilterIndex_Type()
)
tTodSuiteOprEgrIpv6FilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprEgrIpv6FilterIndex.setStatus("current")
_TTodSuiteOprEgrMacFilterIndex_Type = TmnxPolicyOrFilterId
_TTodSuiteOprEgrMacFilterIndex_Object = MibTableColumn
tTodSuiteOprEgrMacFilterIndex = _TTodSuiteOprEgrMacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 12),
    _TTodSuiteOprEgrMacFilterIndex_Type()
)
tTodSuiteOprEgrMacFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprEgrMacFilterIndex.setStatus("current")
_TTodSuiteOprEgrQosPolicyId_Type = TmnxPolicyOrFilterId
_TTodSuiteOprEgrQosPolicyId_Object = MibTableColumn
tTodSuiteOprEgrQosPolicyId = _TTodSuiteOprEgrQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 13),
    _TTodSuiteOprEgrQosPolicyId_Type()
)
tTodSuiteOprEgrQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprEgrQosPolicyId.setStatus("current")
_TTodSuiteOprEgrQosSchedulerPlcy_Type = ServObjName
_TTodSuiteOprEgrQosSchedulerPlcy_Object = MibTableColumn
tTodSuiteOprEgrQosSchedulerPlcy = _TTodSuiteOprEgrQosSchedulerPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 2, 1, 14),
    _TTodSuiteOprEgrQosSchedulerPlcy_Type()
)
tTodSuiteOprEgrQosSchedulerPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteOprEgrQosSchedulerPlcy.setStatus("current")
_TmnxTodSuiteParmsLastChange_Type = TimeStamp
_TmnxTodSuiteParmsLastChange_Object = MibScalar
tmnxTodSuiteParmsLastChange = _TmnxTodSuiteParmsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 3),
    _TmnxTodSuiteParmsLastChange_Type()
)
tmnxTodSuiteParmsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTodSuiteParmsLastChange.setStatus("current")
_TmnxTodSuiteParmsTable_Object = MibTable
tmnxTodSuiteParmsTable = _TmnxTodSuiteParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxTodSuiteParmsTable.setStatus("current")
_TmnxTodSuiteParmsEntry_Object = MibTableRow
tmnxTodSuiteParmsEntry = _TmnxTodSuiteParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4, 1)
)
tmnxTodSuiteParmsEntry.setIndexNames(
    (0, "TIMETRA-SCHEDULER-MIB", "tTodSuiteName"),
    (0, "TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsApplicObj"),
    (0, "TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsTimeRange"),
)
if mibBuilder.loadTexts:
    tmnxTodSuiteParmsEntry.setStatus("current")
_TTodSuiteParmsApplicObj_Type = TmnxTodSuiteControlledObj
_TTodSuiteParmsApplicObj_Object = MibTableColumn
tTodSuiteParmsApplicObj = _TTodSuiteParmsApplicObj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4, 1, 1),
    _TTodSuiteParmsApplicObj_Type()
)
tTodSuiteParmsApplicObj.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTodSuiteParmsApplicObj.setStatus("current")
_TTodSuiteParmsTimeRange_Type = TNamedItem
_TTodSuiteParmsTimeRange_Object = MibTableColumn
tTodSuiteParmsTimeRange = _TTodSuiteParmsTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4, 1, 2),
    _TTodSuiteParmsTimeRange_Type()
)
tTodSuiteParmsTimeRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTodSuiteParmsTimeRange.setStatus("current")
_TTodSuiteParmsRowStatus_Type = RowStatus
_TTodSuiteParmsRowStatus_Object = MibTableColumn
tTodSuiteParmsRowStatus = _TTodSuiteParmsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4, 1, 3),
    _TTodSuiteParmsRowStatus_Type()
)
tTodSuiteParmsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTodSuiteParmsRowStatus.setStatus("current")


class _TTodSuiteParmsPriority_Type(Integer32):
    """Custom type tTodSuiteParmsPriority based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TTodSuiteParmsPriority_Type.__name__ = "Integer32"
_TTodSuiteParmsPriority_Object = MibTableColumn
tTodSuiteParmsPriority = _TTodSuiteParmsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4, 1, 4),
    _TTodSuiteParmsPriority_Type()
)
tTodSuiteParmsPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTodSuiteParmsPriority.setStatus("current")
_TTodSuiteParmsLastMgmtChg_Type = TimeStamp
_TTodSuiteParmsLastMgmtChg_Object = MibTableColumn
tTodSuiteParmsLastMgmtChg = _TTodSuiteParmsLastMgmtChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4, 1, 5),
    _TTodSuiteParmsLastMgmtChg_Type()
)
tTodSuiteParmsLastMgmtChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTodSuiteParmsLastMgmtChg.setStatus("current")


class _TTodSuiteParmsFltrOrPlcyId_Type(TmnxPolicyOrFilterId):
    """Custom type tTodSuiteParmsFltrOrPlcyId based on TmnxPolicyOrFilterId"""
    defaultValue = 0


_TTodSuiteParmsFltrOrPlcyId_Type.__name__ = "TmnxPolicyOrFilterId"
_TTodSuiteParmsFltrOrPlcyId_Object = MibTableColumn
tTodSuiteParmsFltrOrPlcyId = _TTodSuiteParmsFltrOrPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4, 1, 6),
    _TTodSuiteParmsFltrOrPlcyId_Type()
)
tTodSuiteParmsFltrOrPlcyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTodSuiteParmsFltrOrPlcyId.setStatus("current")


class _TTodSuiteParmsPlcyName_Type(ServObjName):
    """Custom type tTodSuiteParmsPlcyName based on ServObjName"""
    defaultValue = OctetString("")


_TTodSuiteParmsPlcyName_Type.__name__ = "ServObjName"
_TTodSuiteParmsPlcyName_Object = MibTableColumn
tTodSuiteParmsPlcyName = _TTodSuiteParmsPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 3, 4, 1, 7),
    _TTodSuiteParmsPlcyName_Type()
)
tTodSuiteParmsPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTodSuiteParmsPlcyName.setStatus("current")
_TmnxTimeRangeNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxTimeRangeNotifyObjects = _TmnxTimeRangeNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 5)
)
_TmnxToDSuiteNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxToDSuiteNotifyObjects = _TmnxToDSuiteNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 6)
)
_TTodNotifSuiteName_Type = DisplayString
_TTodNotifSuiteName_Object = MibScalar
tTodNotifSuiteName = _TTodNotifSuiteName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 6, 1),
    _TTodNotifSuiteName_Type()
)
tTodNotifSuiteName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tTodNotifSuiteName.setStatus("obsolete")
_TTodNotifSuiteParmsApplicObj_Type = TmnxTodSuiteControlledObj
_TTodNotifSuiteParmsApplicObj_Object = MibScalar
tTodNotifSuiteParmsApplicObj = _TTodNotifSuiteParmsApplicObj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 6, 2),
    _TTodNotifSuiteParmsApplicObj_Type()
)
tTodNotifSuiteParmsApplicObj.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tTodNotifSuiteParmsApplicObj.setStatus("obsolete")
_TTodNotifSuiteParmsFltrOrPlcyId_Type = TmnxPolicyOrFilterId
_TTodNotifSuiteParmsFltrOrPlcyId_Object = MibScalar
tTodNotifSuiteParmsFltrOrPlcyId = _TTodNotifSuiteParmsFltrOrPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 6, 3),
    _TTodNotifSuiteParmsFltrOrPlcyId_Type()
)
tTodNotifSuiteParmsFltrOrPlcyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tTodNotifSuiteParmsFltrOrPlcyId.setStatus("obsolete")
_TTodNotifSuiteParmsPlcyName_Type = ServObjName
_TTodNotifSuiteParmsPlcyName_Object = MibScalar
tTodNotifSuiteParmsPlcyName = _TTodNotifSuiteParmsPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 6, 4),
    _TTodNotifSuiteParmsPlcyName_Type()
)
tTodNotifSuiteParmsPlcyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tTodNotifSuiteParmsPlcyName.setStatus("obsolete")
_TTodSuiteProblemDescription_Type = DisplayString
_TTodSuiteProblemDescription_Object = MibScalar
tTodSuiteProblemDescription = _TTodSuiteProblemDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 6, 5),
    _TTodSuiteProblemDescription_Type()
)
tTodSuiteProblemDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tTodSuiteProblemDescription.setStatus("obsolete")
_TmnxTodToolsGroup_ObjectIdentity = ObjectIdentity
tmnxTodToolsGroup = _TmnxTodToolsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7)
)
_TmnxTodToolRetryIpFltrDownload_Type = TmnxPolicyOrFilterId
_TmnxTodToolRetryIpFltrDownload_Object = MibScalar
tmnxTodToolRetryIpFltrDownload = _TmnxTodToolRetryIpFltrDownload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 1),
    _TmnxTodToolRetryIpFltrDownload_Type()
)
tmnxTodToolRetryIpFltrDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTodToolRetryIpFltrDownload.setStatus("current")
_TmnxTodToolRetryMacFltrDownload_Type = TmnxPolicyOrFilterId
_TmnxTodToolRetryMacFltrDownload_Object = MibScalar
tmnxTodToolRetryMacFltrDownload = _TmnxTodToolRetryMacFltrDownload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 2),
    _TmnxTodToolRetryMacFltrDownload_Type()
)
tmnxTodToolRetryMacFltrDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTodToolRetryMacFltrDownload.setStatus("current")
_TmnxTodToolRetryIPv6FltrDownload_Type = TmnxPolicyOrFilterId
_TmnxTodToolRetryIPv6FltrDownload_Object = MibScalar
tmnxTodToolRetryIPv6FltrDownload = _TmnxTodToolRetryIPv6FltrDownload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 3),
    _TmnxTodToolRetryIPv6FltrDownload_Type()
)
tmnxTodToolRetryIPv6FltrDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTodToolRetryIPv6FltrDownload.setStatus("current")
_TmnxTodToolReEvaluateSapTable_Object = MibTable
tmnxTodToolReEvaluateSapTable = _TmnxTodToolReEvaluateSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 4)
)
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateSapTable.setStatus("current")
_TmnxTodToolReEvaluateSapEntry_Object = MibTableRow
tmnxTodToolReEvaluateSapEntry = _TmnxTodToolReEvaluateSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateSapEntry.setStatus("current")


class _TmnxTodToolReEvaluateSap_Type(Integer32):
    """Custom type tmnxTodToolReEvaluateSap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TmnxTodToolReEvaluateSap_Type.__name__ = "Integer32"
_TmnxTodToolReEvaluateSap_Object = MibTableColumn
tmnxTodToolReEvaluateSap = _TmnxTodToolReEvaluateSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 4, 1, 1),
    _TmnxTodToolReEvaluateSap_Type()
)
tmnxTodToolReEvaluateSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateSap.setStatus("current")
_TmnxTodToolReEvaluateMssTable_Object = MibTable
tmnxTodToolReEvaluateMssTable = _TmnxTodToolReEvaluateMssTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 5)
)
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateMssTable.setStatus("current")
_TmnxTodToolReEvaluateMssEntry_Object = MibTableRow
tmnxTodToolReEvaluateMssEntry = _TmnxTodToolReEvaluateMssEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateMssEntry.setStatus("current")


class _TmnxTodToolReEvaluateMss_Type(Integer32):
    """Custom type tmnxTodToolReEvaluateMss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TmnxTodToolReEvaluateMss_Type.__name__ = "Integer32"
_TmnxTodToolReEvaluateMss_Object = MibTableColumn
tmnxTodToolReEvaluateMss = _TmnxTodToolReEvaluateMss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 5, 1, 1),
    _TmnxTodToolReEvaluateMss_Type()
)
tmnxTodToolReEvaluateMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateMss.setStatus("current")
_TmnxTodToolReEvaluateSuiteTable_Object = MibTable
tmnxTodToolReEvaluateSuiteTable = _TmnxTodToolReEvaluateSuiteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 6)
)
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateSuiteTable.setStatus("current")
_TmnxTodToolReEvaluateSuiteEntry_Object = MibTableRow
tmnxTodToolReEvaluateSuiteEntry = _TmnxTodToolReEvaluateSuiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateSuiteEntry.setStatus("current")


class _TmnxTodToolReEvaluateSuite_Type(Integer32):
    """Custom type tmnxTodToolReEvaluateSuite based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TmnxTodToolReEvaluateSuite_Type.__name__ = "Integer32"
_TmnxTodToolReEvaluateSuite_Object = MibTableColumn
tmnxTodToolReEvaluateSuite = _TmnxTodToolReEvaluateSuite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 1, 7, 6, 1, 1),
    _TmnxTodToolReEvaluateSuite_Type()
)
tmnxTodToolReEvaluateSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTodToolReEvaluateSuite.setStatus("current")
_TmnxCronObjects_ObjectIdentity = ObjectIdentity
tmnxCronObjects = _TmnxCronObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2)
)
_TmnxCronSchedTable_Object = MibTable
tmnxCronSchedTable = _TmnxCronSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxCronSchedTable.setStatus("current")
_TmnxCronSchedEntry_Object = MibTableRow
tmnxCronSchedEntry = _TmnxCronSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxCronSchedEntry.setStatus("current")


class _TmnxCronSchedCount_Type(Unsigned32):
    """Custom type tmnxCronSchedCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxCronSchedCount_Type.__name__ = "Unsigned32"
_TmnxCronSchedCount_Object = MibTableColumn
tmnxCronSchedCount = _TmnxCronSchedCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 1),
    _TmnxCronSchedCount_Type()
)
tmnxCronSchedCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCronSchedCount.setStatus("current")
_TmnxCronSchedLastMgmtChg_Type = TimeStamp
_TmnxCronSchedLastMgmtChg_Object = MibTableColumn
tmnxCronSchedLastMgmtChg = _TmnxCronSchedLastMgmtChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 2),
    _TmnxCronSchedLastMgmtChg_Type()
)
tmnxCronSchedLastMgmtChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCronSchedLastMgmtChg.setStatus("current")


class _TmnxCronSchedEndTime_Type(TruthValue):
    """Custom type tmnxCronSchedEndTime based on TruthValue"""
    defaultValue = 2


_TmnxCronSchedEndTime_Type.__name__ = "TruthValue"
_TmnxCronSchedEndTime_Object = MibTableColumn
tmnxCronSchedEndTime = _TmnxCronSchedEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 3),
    _TmnxCronSchedEndTime_Type()
)
tmnxCronSchedEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCronSchedEndTime.setStatus("current")


class _TmnxCronSchedEndWeekday_Type(TmnxTimeRangeWeekday):
    """Custom type tmnxCronSchedEndWeekday based on TmnxTimeRangeWeekday"""
    defaultValue = 7


_TmnxCronSchedEndWeekday_Type.__name__ = "TmnxTimeRangeWeekday"
_TmnxCronSchedEndWeekday_Object = MibTableColumn
tmnxCronSchedEndWeekday = _TmnxCronSchedEndWeekday_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 4),
    _TmnxCronSchedEndWeekday_Type()
)
tmnxCronSchedEndWeekday.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCronSchedEndWeekday.setStatus("current")


class _TmnxCronSchedEndYear_Type(TmnxTimeRangeYear):
    """Custom type tmnxCronSchedEndYear based on TmnxTimeRangeYear"""
    defaultValue = 2099


_TmnxCronSchedEndYear_Type.__name__ = "TmnxTimeRangeYear"
_TmnxCronSchedEndYear_Object = MibTableColumn
tmnxCronSchedEndYear = _TmnxCronSchedEndYear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 5),
    _TmnxCronSchedEndYear_Type()
)
tmnxCronSchedEndYear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCronSchedEndYear.setStatus("current")


class _TmnxCronSchedEndMonth_Type(TmnxTimeRangeMonth):
    """Custom type tmnxCronSchedEndMonth based on TmnxTimeRangeMonth"""
    defaultValue = 11


_TmnxCronSchedEndMonth_Type.__name__ = "TmnxTimeRangeMonth"
_TmnxCronSchedEndMonth_Object = MibTableColumn
tmnxCronSchedEndMonth = _TmnxCronSchedEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 6),
    _TmnxCronSchedEndMonth_Type()
)
tmnxCronSchedEndMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCronSchedEndMonth.setStatus("current")


class _TmnxCronSchedEndDay_Type(TmnxTimeRangeDay):
    """Custom type tmnxCronSchedEndDay based on TmnxTimeRangeDay"""
    defaultValue = 31


_TmnxCronSchedEndDay_Type.__name__ = "TmnxTimeRangeDay"
_TmnxCronSchedEndDay_Object = MibTableColumn
tmnxCronSchedEndDay = _TmnxCronSchedEndDay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 7),
    _TmnxCronSchedEndDay_Type()
)
tmnxCronSchedEndDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCronSchedEndDay.setStatus("current")


class _TmnxCronSchedEndHour_Type(TmnxTimeRangeHour):
    """Custom type tmnxCronSchedEndHour based on TmnxTimeRangeHour"""
    defaultValue = 23


_TmnxCronSchedEndHour_Type.__name__ = "TmnxTimeRangeHour"
_TmnxCronSchedEndHour_Object = MibTableColumn
tmnxCronSchedEndHour = _TmnxCronSchedEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 8),
    _TmnxCronSchedEndHour_Type()
)
tmnxCronSchedEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCronSchedEndHour.setStatus("current")


class _TmnxCronSchedEndMinute_Type(TmnxTimeRangeMinute):
    """Custom type tmnxCronSchedEndMinute based on TmnxTimeRangeMinute"""
    defaultValue = 59


_TmnxCronSchedEndMinute_Type.__name__ = "TmnxTimeRangeMinute"
_TmnxCronSchedEndMinute_Object = MibTableColumn
tmnxCronSchedEndMinute = _TmnxCronSchedEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 1, 1, 9),
    _TmnxCronSchedEndMinute_Type()
)
tmnxCronSchedEndMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCronSchedEndMinute.setStatus("current")
_TmnxCronSchedTblLastChange_Type = TimeStamp
_TmnxCronSchedTblLastChange_Object = MibScalar
tmnxCronSchedTblLastChange = _TmnxCronSchedTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 37, 2, 2),
    _TmnxCronSchedTblLastChange_Type()
)
tmnxCronSchedTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCronSchedTblLastChange.setStatus("current")
_TmnxSchedulerNotifications_ObjectIdentity = ObjectIdentity
tmnxSchedulerNotifications = _TmnxSchedulerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 37)
)
_TmnxSchedTimeRangeNotifications_ObjectIdentity = ObjectIdentity
tmnxSchedTimeRangeNotifications = _TmnxSchedTimeRangeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 37, 1)
)
_TmnxTimeRangeNotifications_ObjectIdentity = ObjectIdentity
tmnxTimeRangeNotifications = _TmnxTimeRangeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 37, 1, 0)
)
_TmnxSchedToDSuiteNotifications_ObjectIdentity = ObjectIdentity
tmnxSchedToDSuiteNotifications = _TmnxSchedToDSuiteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 37, 2)
)
_TmnxToDSuiteNotifications_ObjectIdentity = ObjectIdentity
tmnxToDSuiteNotifications = _TmnxToDSuiteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 37, 2, 0)
)
sapBaseInfoEntry.registerAugmentions(
    ("TIMETRA-SCHEDULER-MIB",
     "tmnxTodToolReEvaluateSapEntry")
)
tmnxTodToolReEvaluateSapEntry.setIndexNames(*sapBaseInfoEntry.getIndexNames())
custMultiServiceSiteEntry.registerAugmentions(
    ("TIMETRA-SCHEDULER-MIB",
     "tmnxTodToolReEvaluateMssEntry")
)
tmnxTodToolReEvaluateMssEntry.setIndexNames(*custMultiServiceSiteEntry.getIndexNames())
tmnxTodSuiteEntry.registerAugmentions(
    ("TIMETRA-SCHEDULER-MIB",
     "tmnxTodToolReEvaluateSuiteEntry")
)
tmnxTodToolReEvaluateSuiteEntry.setIndexNames(*tmnxTodSuiteEntry.getIndexNames())
schedEntry.registerAugmentions(
    ("TIMETRA-SCHEDULER-MIB",
     "tmnxCronSchedEntry")
)
tmnxCronSchedEntry.setIndexNames(*schedEntry.getIndexNames())

# Managed Objects groups

tmnxTodPolicyV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 2, 1)
)
tmnxTodPolicyV4v0Group.setObjects(
      *(("TIMETRA-SCHEDULER-MIB", "tmnxTimeRangeTableLastChange"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxPeriodTRngeParmsTblLstChnge"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxAbsTRngeParmsTblLstChnge"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodSuiteTableLastChange"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodSuiteParmsLastChange"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeLastMgmtChange"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeDescription"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeTriggers"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeActive"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeLastMgmtChg"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeEndWeekDay"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeEndHour"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeEndMinute"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeLastMgmtChg"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndYear"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndMonth"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndDay"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndHour"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndMinute"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteLastChanged"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteDescription"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrIpFilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrIpv6FilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrMacFilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrQosPolicyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrQosSchedulerPlcy"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrIpFilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrIpv6FilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrMacFilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrQosPolicyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrQosSchedulerPlcy"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsPriority"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsLastMgmtChg"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsFltrOrPlcyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsPlcyName"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeActive"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeActive"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteName"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsApplicObj"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsFltrOrPlcyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsPlcyName"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteProblemDescription"))
)
if mibBuilder.loadTexts:
    tmnxTodPolicyV4v0Group.setStatus("obsolete")

tmnxTodPolicyV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 2, 3)
)
tmnxTodPolicyV5v0Group.setObjects(
      *(("TIMETRA-SCHEDULER-MIB", "tmnxTimeRangeTableLastChange"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxPeriodTRngeParmsTblLstChnge"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxAbsTRngeParmsTblLstChnge"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodSuiteTableLastChange"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodSuiteParmsLastChange"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeLastMgmtChange"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeDescription"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeTriggers"),
        ("TIMETRA-SCHEDULER-MIB", "tTimeRangeActive"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeLastMgmtChg"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeEndWeekDay"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeEndHour"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeEndMinute"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeLastMgmtChg"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndYear"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndMonth"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndDay"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndHour"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeEndMinute"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteLastChanged"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteDescription"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrIpFilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrIpv6FilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrMacFilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrQosPolicyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprIngrQosSchedulerPlcy"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrIpFilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrIpv6FilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrMacFilterIndex"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrQosPolicyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteOprEgrQosSchedulerPlcy"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsRowStatus"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsPriority"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsLastMgmtChg"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsFltrOrPlcyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteParmsPlcyName"),
        ("TIMETRA-SCHEDULER-MIB", "tPeriodicTimeRangeActive"),
        ("TIMETRA-SCHEDULER-MIB", "tAbsoluteTimeRangeActive"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodToolRetryIpFltrDownload"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodToolRetryMacFltrDownload"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodToolRetryIPv6FltrDownload"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodToolReEvaluateSap"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodToolReEvaluateMss"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodToolReEvaluateSuite"))
)
if mibBuilder.loadTexts:
    tmnxTodPolicyV5v0Group.setStatus("current")

tmnxTodPolicyObsoletedV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 2, 5)
)
tmnxTodPolicyObsoletedV5v0Group.setObjects(
      *(("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteName"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsApplicObj"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsFltrOrPlcyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsPlcyName"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteProblemDescription"))
)
if mibBuilder.loadTexts:
    tmnxTodPolicyObsoletedV5v0Group.setStatus("current")

tmnxCronSchedV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 3, 1)
)
tmnxCronSchedV5v0Group.setObjects(
      *(("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedCount"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedLastMgmtChg"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedEndTime"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedEndWeekday"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedEndYear"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedEndMonth"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedEndDay"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedEndHour"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedEndMinute"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedTblLastChange"))
)
if mibBuilder.loadTexts:
    tmnxCronSchedV5v0Group.setStatus("current")


# Notification objects

tTodSuiteProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 37, 2, 0, 1)
)
tTodSuiteProblem.setObjects(
      *(("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteName"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsApplicObj"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsFltrOrPlcyId"),
        ("TIMETRA-SCHEDULER-MIB", "tTodNotifSuiteParmsPlcyName"),
        ("TIMETRA-SCHEDULER-MIB", "tTodSuiteProblemDescription"))
)
if mibBuilder.loadTexts:
    tTodSuiteProblem.setStatus(
        "obsolete"
    )


# Notifications groups

tmnxTodPolicyNotificationsV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 2, 2)
)
tmnxTodPolicyNotificationsV4v0Group.setObjects(
    ("TIMETRA-SCHEDULER-MIB", "tTodSuiteProblem")
)
if mibBuilder.loadTexts:
    tmnxTodPolicyNotificationsV4v0Group.setStatus(
        "obsolete"
    )

tmnxTodPolicyObsoletedNotificationsV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 2, 4)
)
tmnxTodPolicyObsoletedNotificationsV5v0Group.setObjects(
    ("TIMETRA-SCHEDULER-MIB", "tTodSuiteProblem")
)
if mibBuilder.loadTexts:
    tmnxTodPolicyObsoletedNotificationsV5v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxToDSchedV4v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 1, 1)
)
tmnxToDSchedV4v0MIBCompliance.setObjects(
      *(("TIMETRA-SCHEDULER-MIB", "tmnxTodPolicyV4v0Group"),
        ("TIMETRA-SCHEDULER-MIB", "tmnxTodPolicyNotificationsV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxToDSchedV4v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxToDSchedV5v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 1, 2)
)
tmnxToDSchedV5v0MIBCompliance.setObjects(
    ("TIMETRA-SCHEDULER-MIB", "tmnxTodPolicyV5v0Group")
)
if mibBuilder.loadTexts:
    tmnxToDSchedV5v0MIBCompliance.setStatus(
        "current"
    )

tmnxCronSchedV5v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 37, 1, 3)
)
tmnxCronSchedV5v0MIBCompliance.setObjects(
    ("TIMETRA-SCHEDULER-MIB", "tmnxCronSchedV5v0Group")
)
if mibBuilder.loadTexts:
    tmnxCronSchedV5v0MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SCHEDULER-MIB",
    **{"TmnxPolicyOrFilterId": TmnxPolicyOrFilterId,
       "TmnxTimeRangeDay": TmnxTimeRangeDay,
       "TmnxTimeRangeHour": TmnxTimeRangeHour,
       "TmnxTimeRangePeriodicEndHour": TmnxTimeRangePeriodicEndHour,
       "TmnxTimeRangeMinute": TmnxTimeRangeMinute,
       "TmnxTimeRangeMonth": TmnxTimeRangeMonth,
       "TmnxTimeRangeWeekday": TmnxTimeRangeWeekday,
       "TmnxTimeRangeYear": TmnxTimeRangeYear,
       "TmnxTodSuiteControlledObj": TmnxTodSuiteControlledObj,
       "tmnxSchedulerMIBModule": tmnxSchedulerMIBModule,
       "tmnxSchedulerCompliance": tmnxSchedulerCompliance,
       "tmnxSchedulerCompliances": tmnxSchedulerCompliances,
       "tmnxToDSchedV4v0MIBCompliance": tmnxToDSchedV4v0MIBCompliance,
       "tmnxToDSchedV5v0MIBCompliance": tmnxToDSchedV5v0MIBCompliance,
       "tmnxCronSchedV5v0MIBCompliance": tmnxCronSchedV5v0MIBCompliance,
       "tmnxTimeOfDayPlcyGroups": tmnxTimeOfDayPlcyGroups,
       "tmnxTodPolicyV4v0Group": tmnxTodPolicyV4v0Group,
       "tmnxTodPolicyNotificationsV4v0Group": tmnxTodPolicyNotificationsV4v0Group,
       "tmnxTodPolicyV5v0Group": tmnxTodPolicyV5v0Group,
       "tmnxTodPolicyObsoletedNotificationsV5v0Group": tmnxTodPolicyObsoletedNotificationsV5v0Group,
       "tmnxTodPolicyObsoletedV5v0Group": tmnxTodPolicyObsoletedV5v0Group,
       "tmnxCronSchedGroups": tmnxCronSchedGroups,
       "tmnxCronSchedV5v0Group": tmnxCronSchedV5v0Group,
       "tmnxScheduler": tmnxScheduler,
       "tmnxTimeOfDayPlcyObjects": tmnxTimeOfDayPlcyObjects,
       "tmnxTimeRangeObjects": tmnxTimeRangeObjects,
       "tmnxTimeRangeTableLastChange": tmnxTimeRangeTableLastChange,
       "tmnxTimeRangeTable": tmnxTimeRangeTable,
       "tmnxTimeRangeEntry": tmnxTimeRangeEntry,
       "tTimeRangeName": tTimeRangeName,
       "tTimeRangeRowStatus": tTimeRangeRowStatus,
       "tTimeRangeLastMgmtChange": tTimeRangeLastMgmtChange,
       "tTimeRangeDescription": tTimeRangeDescription,
       "tTimeRangeTriggers": tTimeRangeTriggers,
       "tTimeRangeActive": tTimeRangeActive,
       "tmnxPeriodTRngeParmsTblLstChnge": tmnxPeriodTRngeParmsTblLstChnge,
       "tmnxPeriodicTimeRangeParmsTable": tmnxPeriodicTimeRangeParmsTable,
       "tmnxPeriodicTimeRangeParmsEntry": tmnxPeriodicTimeRangeParmsEntry,
       "tPeriodicTimeRangeStartWeekDay": tPeriodicTimeRangeStartWeekDay,
       "tPeriodicTimeRangeStartHour": tPeriodicTimeRangeStartHour,
       "tPeriodicTimeRangeStartMinute": tPeriodicTimeRangeStartMinute,
       "tPeriodicTimeRangeRowStatus": tPeriodicTimeRangeRowStatus,
       "tPeriodicTimeRangeLastMgmtChg": tPeriodicTimeRangeLastMgmtChg,
       "tPeriodicTimeRangeEndWeekDay": tPeriodicTimeRangeEndWeekDay,
       "tPeriodicTimeRangeEndHour": tPeriodicTimeRangeEndHour,
       "tPeriodicTimeRangeEndMinute": tPeriodicTimeRangeEndMinute,
       "tPeriodicTimeRangeActive": tPeriodicTimeRangeActive,
       "tmnxAbsTRngeParmsTblLstChnge": tmnxAbsTRngeParmsTblLstChnge,
       "tmnxAbsoluteTimeRangeParmsTable": tmnxAbsoluteTimeRangeParmsTable,
       "tmnxAbsoluteTimeRangeParmsEntry": tmnxAbsoluteTimeRangeParmsEntry,
       "tAbsoluteTimeRangeStartYear": tAbsoluteTimeRangeStartYear,
       "tAbsoluteTimeRangeStartMonth": tAbsoluteTimeRangeStartMonth,
       "tAbsoluteTimeRangeStartDay": tAbsoluteTimeRangeStartDay,
       "tAbsoluteTimeRangeStartHour": tAbsoluteTimeRangeStartHour,
       "tAbsoluteTimeRangeStartMinute": tAbsoluteTimeRangeStartMinute,
       "tAbsoluteTimeRangeRowStatus": tAbsoluteTimeRangeRowStatus,
       "tAbsoluteTimeRangeLastMgmtChg": tAbsoluteTimeRangeLastMgmtChg,
       "tAbsoluteTimeRangeEndYear": tAbsoluteTimeRangeEndYear,
       "tAbsoluteTimeRangeEndMonth": tAbsoluteTimeRangeEndMonth,
       "tAbsoluteTimeRangeEndDay": tAbsoluteTimeRangeEndDay,
       "tAbsoluteTimeRangeEndHour": tAbsoluteTimeRangeEndHour,
       "tAbsoluteTimeRangeEndMinute": tAbsoluteTimeRangeEndMinute,
       "tAbsoluteTimeRangeActive": tAbsoluteTimeRangeActive,
       "tmnxToDSuiteObjects": tmnxToDSuiteObjects,
       "tmnxTodSuiteTableLastChange": tmnxTodSuiteTableLastChange,
       "tmnxTodSuiteTable": tmnxTodSuiteTable,
       "tmnxTodSuiteEntry": tmnxTodSuiteEntry,
       "tTodSuiteName": tTodSuiteName,
       "tTodSuiteRowStatus": tTodSuiteRowStatus,
       "tTodSuiteLastChanged": tTodSuiteLastChanged,
       "tTodSuiteDescription": tTodSuiteDescription,
       "tTodSuiteOprIngrIpFilterIndex": tTodSuiteOprIngrIpFilterIndex,
       "tTodSuiteOprIngrIpv6FilterIndex": tTodSuiteOprIngrIpv6FilterIndex,
       "tTodSuiteOprIngrMacFilterIndex": tTodSuiteOprIngrMacFilterIndex,
       "tTodSuiteOprIngrQosPolicyId": tTodSuiteOprIngrQosPolicyId,
       "tTodSuiteOprIngrQosSchedulerPlcy": tTodSuiteOprIngrQosSchedulerPlcy,
       "tTodSuiteOprEgrIpFilterIndex": tTodSuiteOprEgrIpFilterIndex,
       "tTodSuiteOprEgrIpv6FilterIndex": tTodSuiteOprEgrIpv6FilterIndex,
       "tTodSuiteOprEgrMacFilterIndex": tTodSuiteOprEgrMacFilterIndex,
       "tTodSuiteOprEgrQosPolicyId": tTodSuiteOprEgrQosPolicyId,
       "tTodSuiteOprEgrQosSchedulerPlcy": tTodSuiteOprEgrQosSchedulerPlcy,
       "tmnxTodSuiteParmsLastChange": tmnxTodSuiteParmsLastChange,
       "tmnxTodSuiteParmsTable": tmnxTodSuiteParmsTable,
       "tmnxTodSuiteParmsEntry": tmnxTodSuiteParmsEntry,
       "tTodSuiteParmsApplicObj": tTodSuiteParmsApplicObj,
       "tTodSuiteParmsTimeRange": tTodSuiteParmsTimeRange,
       "tTodSuiteParmsRowStatus": tTodSuiteParmsRowStatus,
       "tTodSuiteParmsPriority": tTodSuiteParmsPriority,
       "tTodSuiteParmsLastMgmtChg": tTodSuiteParmsLastMgmtChg,
       "tTodSuiteParmsFltrOrPlcyId": tTodSuiteParmsFltrOrPlcyId,
       "tTodSuiteParmsPlcyName": tTodSuiteParmsPlcyName,
       "tmnxTimeRangeNotifyObjects": tmnxTimeRangeNotifyObjects,
       "tmnxToDSuiteNotifyObjects": tmnxToDSuiteNotifyObjects,
       "tTodNotifSuiteName": tTodNotifSuiteName,
       "tTodNotifSuiteParmsApplicObj": tTodNotifSuiteParmsApplicObj,
       "tTodNotifSuiteParmsFltrOrPlcyId": tTodNotifSuiteParmsFltrOrPlcyId,
       "tTodNotifSuiteParmsPlcyName": tTodNotifSuiteParmsPlcyName,
       "tTodSuiteProblemDescription": tTodSuiteProblemDescription,
       "tmnxTodToolsGroup": tmnxTodToolsGroup,
       "tmnxTodToolRetryIpFltrDownload": tmnxTodToolRetryIpFltrDownload,
       "tmnxTodToolRetryMacFltrDownload": tmnxTodToolRetryMacFltrDownload,
       "tmnxTodToolRetryIPv6FltrDownload": tmnxTodToolRetryIPv6FltrDownload,
       "tmnxTodToolReEvaluateSapTable": tmnxTodToolReEvaluateSapTable,
       "tmnxTodToolReEvaluateSapEntry": tmnxTodToolReEvaluateSapEntry,
       "tmnxTodToolReEvaluateSap": tmnxTodToolReEvaluateSap,
       "tmnxTodToolReEvaluateMssTable": tmnxTodToolReEvaluateMssTable,
       "tmnxTodToolReEvaluateMssEntry": tmnxTodToolReEvaluateMssEntry,
       "tmnxTodToolReEvaluateMss": tmnxTodToolReEvaluateMss,
       "tmnxTodToolReEvaluateSuiteTable": tmnxTodToolReEvaluateSuiteTable,
       "tmnxTodToolReEvaluateSuiteEntry": tmnxTodToolReEvaluateSuiteEntry,
       "tmnxTodToolReEvaluateSuite": tmnxTodToolReEvaluateSuite,
       "tmnxCronObjects": tmnxCronObjects,
       "tmnxCronSchedTable": tmnxCronSchedTable,
       "tmnxCronSchedEntry": tmnxCronSchedEntry,
       "tmnxCronSchedCount": tmnxCronSchedCount,
       "tmnxCronSchedLastMgmtChg": tmnxCronSchedLastMgmtChg,
       "tmnxCronSchedEndTime": tmnxCronSchedEndTime,
       "tmnxCronSchedEndWeekday": tmnxCronSchedEndWeekday,
       "tmnxCronSchedEndYear": tmnxCronSchedEndYear,
       "tmnxCronSchedEndMonth": tmnxCronSchedEndMonth,
       "tmnxCronSchedEndDay": tmnxCronSchedEndDay,
       "tmnxCronSchedEndHour": tmnxCronSchedEndHour,
       "tmnxCronSchedEndMinute": tmnxCronSchedEndMinute,
       "tmnxCronSchedTblLastChange": tmnxCronSchedTblLastChange,
       "tmnxSchedulerNotifications": tmnxSchedulerNotifications,
       "tmnxSchedTimeRangeNotifications": tmnxSchedTimeRangeNotifications,
       "tmnxTimeRangeNotifications": tmnxTimeRangeNotifications,
       "tmnxSchedToDSuiteNotifications": tmnxSchedToDSuiteNotifications,
       "tmnxToDSuiteNotifications": tmnxToDSuiteNotifications,
       "tTodSuiteProblem": tTodSuiteProblem}
)
