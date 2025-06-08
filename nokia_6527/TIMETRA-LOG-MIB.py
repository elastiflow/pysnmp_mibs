# SNMP MIB module (TIMETRA-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-LOG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:47 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,
 SnmpMessageProcessingModel,
 SnmpSecurityLevel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpMessageProcessingModel",
    "SnmpSecurityLevel")

(snmpNotifyEntry,) = mibBuilder.importSymbols(
    "SNMP-NOTIFICATION-MIB",
    "snmpNotifyEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,
 sysObjectID) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysObjectID")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TFilterAction,
 TFilterActionOrDefault) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterAction",
    "TFilterActionOrDefault")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(THsmdaCounterIdOrZero,
 THsmdaCounterIdOrZeroOrAll,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TQueueId,
 TQueueIdOrAll,
 TmnxAccPlcyAACounters,
 TmnxAccPlcyAASubAttributes,
 TmnxAccPlcyOECounters,
 TmnxAccPlcyOICounters,
 TmnxAccPlcyQECounters,
 TmnxAccPlcyQICounters,
 TmnxActionType,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "THsmdaCounterIdOrZero",
    "THsmdaCounterIdOrZeroOrAll",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TQueueId",
    "TQueueIdOrAll",
    "TmnxAccPlcyAACounters",
    "TmnxAccPlcyAASubAttributes",
    "TmnxAccPlcyOECounters",
    "TmnxAccPlcyOICounters",
    "TmnxAccPlcyQECounters",
    "TmnxAccPlcyQICounters",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxOperState")


# MODULE-IDENTITY

timetraLogMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    timetraLogMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-15 00:00",
         "2005-01-24 00:00",
         "2004-05-27 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-11-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPerceivedSeverity(TextualConvention, Integer32):
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
        *(("none", 0),
          ("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



class TmnxSyslogId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )



class TmnxSyslogIdOrEmpty(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 40),
    )



class TmnxSyslogFacility(TextualConvention, Integer32):
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
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 0),
          ("user", 1),
          ("mail", 2),
          ("systemd", 3),
          ("auth", 4),
          ("syslogd", 5),
          ("printer", 6),
          ("netnews", 7),
          ("uucp", 8),
          ("cron", 9),
          ("authpriv", 10),
          ("ftp", 11),
          ("ntp", 12),
          ("logaudit", 13),
          ("logalert", 14),
          ("cron2", 15),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )



class TmnxUdpPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxSyslogSeverity(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )



class TmnxLogFileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )



class TmnxLogFileType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("eventLog", 1),
          ("accountingPolicy", 2))
    )



class TmnxLogIdIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TmnxCFlash(TextualConvention, Unsigned32):
    status = "current"


class TmnxLogFilterId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1001),
    )



class TmnxLogFilterEntryId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )



class TmnxLogFilterOperator(TextualConvention, Integer32):
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
        *(("off", 1),
          ("equal", 2),
          ("notEqual", 3),
          ("lessThan", 4),
          ("lessThanOrEqual", 5),
          ("greaterThan", 6),
          ("greaterThanOrEqual", 7))
    )



class TmnxEventNumber(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_TmnxLogConformance_ObjectIdentity = ObjectIdentity
tmnxLogConformance = _TmnxLogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12)
)
_TmnxLogCompliances_ObjectIdentity = ObjectIdentity
tmnxLogCompliances = _TmnxLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1)
)
_TmnxLogGroups_ObjectIdentity = ObjectIdentity
tmnxLogGroups = _TmnxLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2)
)
_TmnxLogObjs_ObjectIdentity = ObjectIdentity
tmnxLogObjs = _TmnxLogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12)
)
_TmnxLogNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxLogNotificationObjects = _TmnxLogNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1)
)
_TmnxLogFileDeletedLogId_Type = TmnxLogIdIndex
_TmnxLogFileDeletedLogId_Object = MibScalar
tmnxLogFileDeletedLogId = _TmnxLogFileDeletedLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 1),
    _TmnxLogFileDeletedLogId_Type()
)
tmnxLogFileDeletedLogId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedLogId.setStatus("current")
_TmnxLogFileDeletedFileId_Type = TmnxLogFileId
_TmnxLogFileDeletedFileId_Object = MibScalar
tmnxLogFileDeletedFileId = _TmnxLogFileDeletedFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 2),
    _TmnxLogFileDeletedFileId_Type()
)
tmnxLogFileDeletedFileId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedFileId.setStatus("current")
_TmnxLogFileDeletedLogType_Type = TmnxLogFileType
_TmnxLogFileDeletedLogType_Object = MibScalar
tmnxLogFileDeletedLogType = _TmnxLogFileDeletedLogType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 3),
    _TmnxLogFileDeletedLogType_Type()
)
tmnxLogFileDeletedLogType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedLogType.setStatus("current")
_TmnxLogFileDeletedLocation_Type = TmnxCFlash
_TmnxLogFileDeletedLocation_Object = MibScalar
tmnxLogFileDeletedLocation = _TmnxLogFileDeletedLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 4),
    _TmnxLogFileDeletedLocation_Type()
)
tmnxLogFileDeletedLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedLocation.setStatus("current")
_TmnxLogFileDeletedName_Type = DisplayString
_TmnxLogFileDeletedName_Object = MibScalar
tmnxLogFileDeletedName = _TmnxLogFileDeletedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 5),
    _TmnxLogFileDeletedName_Type()
)
tmnxLogFileDeletedName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedName.setStatus("current")
_TmnxLogFileDeletedCreateTime_Type = DateAndTime
_TmnxLogFileDeletedCreateTime_Object = MibScalar
tmnxLogFileDeletedCreateTime = _TmnxLogFileDeletedCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 6),
    _TmnxLogFileDeletedCreateTime_Type()
)
tmnxLogFileDeletedCreateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedCreateTime.setStatus("current")


class _TmnxLogTraceErrorTitle_Type(DisplayString):
    """Custom type tmnxLogTraceErrorTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TmnxLogTraceErrorTitle_Type.__name__ = "DisplayString"
_TmnxLogTraceErrorTitle_Object = MibScalar
tmnxLogTraceErrorTitle = _TmnxLogTraceErrorTitle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 7),
    _TmnxLogTraceErrorTitle_Type()
)
tmnxLogTraceErrorTitle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogTraceErrorTitle.setStatus("current")


class _TmnxLogTraceErrorSubject_Type(DisplayString):
    """Custom type tmnxLogTraceErrorSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TmnxLogTraceErrorSubject_Type.__name__ = "DisplayString"
_TmnxLogTraceErrorSubject_Object = MibScalar
tmnxLogTraceErrorSubject = _TmnxLogTraceErrorSubject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 8),
    _TmnxLogTraceErrorSubject_Type()
)
tmnxLogTraceErrorSubject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogTraceErrorSubject.setStatus("current")
_TmnxLogTraceErrorMessage_Type = DisplayString
_TmnxLogTraceErrorMessage_Object = MibScalar
tmnxLogTraceErrorMessage = _TmnxLogTraceErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 9),
    _TmnxLogTraceErrorMessage_Type()
)
tmnxLogTraceErrorMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogTraceErrorMessage.setStatus("current")
_TmnxLogThrottledEventID_Type = ObjectIdentifier
_TmnxLogThrottledEventID_Object = MibScalar
tmnxLogThrottledEventID = _TmnxLogThrottledEventID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 10),
    _TmnxLogThrottledEventID_Type()
)
tmnxLogThrottledEventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogThrottledEventID.setStatus("current")
_TmnxLogThrottledEvents_Type = Unsigned32
_TmnxLogThrottledEvents_Object = MibScalar
tmnxLogThrottledEvents = _TmnxLogThrottledEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 11),
    _TmnxLogThrottledEvents_Type()
)
tmnxLogThrottledEvents.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogThrottledEvents.setStatus("current")
_TmnxSysLogTargetId_Type = TmnxSyslogId
_TmnxSysLogTargetId_Object = MibScalar
tmnxSysLogTargetId = _TmnxSysLogTargetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 12),
    _TmnxSysLogTargetId_Type()
)
tmnxSysLogTargetId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLogTargetId.setStatus("current")
_TmnxSysLogTargetProblemDescr_Type = DisplayString
_TmnxSysLogTargetProblemDescr_Object = MibScalar
tmnxSysLogTargetProblemDescr = _TmnxSysLogTargetProblemDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 13),
    _TmnxSysLogTargetProblemDescr_Type()
)
tmnxSysLogTargetProblemDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLogTargetProblemDescr.setStatus("current")


class _TmnxLogNotifyApInterval_Type(Integer32):
    """Custom type tmnxLogNotifyApInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_TmnxLogNotifyApInterval_Type.__name__ = "Integer32"
_TmnxLogNotifyApInterval_Object = MibScalar
tmnxLogNotifyApInterval = _TmnxLogNotifyApInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 14),
    _TmnxLogNotifyApInterval_Type()
)
tmnxLogNotifyApInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogNotifyApInterval.setStatus("current")
_TmnxStdReplayStartEvent_Type = Unsigned32
_TmnxStdReplayStartEvent_Object = MibScalar
tmnxStdReplayStartEvent = _TmnxStdReplayStartEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 15),
    _TmnxStdReplayStartEvent_Type()
)
tmnxStdReplayStartEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxStdReplayStartEvent.setStatus("current")
_TmnxStdReplayEndEvent_Type = Unsigned32
_TmnxStdReplayEndEvent_Object = MibScalar
tmnxStdReplayEndEvent = _TmnxStdReplayEndEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 16),
    _TmnxStdReplayEndEvent_Type()
)
tmnxStdReplayEndEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxStdReplayEndEvent.setStatus("current")


class _TmnxLogMaxLogs_Type(Unsigned32):
    """Custom type tmnxLogMaxLogs based on Unsigned32"""
    defaultValue = 45


_TmnxLogMaxLogs_Type.__name__ = "Unsigned32"
_TmnxLogMaxLogs_Object = MibScalar
tmnxLogMaxLogs = _TmnxLogMaxLogs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 2),
    _TmnxLogMaxLogs_Type()
)
tmnxLogMaxLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogMaxLogs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogMaxLogs.setUnits("logs")
_TmnxLogFileIdTable_Object = MibTable
tmnxLogFileIdTable = _TmnxLogFileIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    tmnxLogFileIdTable.setStatus("current")
_TmnxLogFileIdEntry_Object = MibTableRow
tmnxLogFileIdEntry = _TmnxLogFileIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1)
)
tmnxLogFileIdEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogFileId"),
)
if mibBuilder.loadTexts:
    tmnxLogFileIdEntry.setStatus("current")
_TmnxLogFileId_Type = TmnxLogFileId
_TmnxLogFileId_Object = MibTableColumn
tmnxLogFileId = _TmnxLogFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 1),
    _TmnxLogFileId_Type()
)
tmnxLogFileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogFileId.setStatus("current")
_TmnxLogFileIdRowStatus_Type = RowStatus
_TmnxLogFileIdRowStatus_Object = MibTableColumn
tmnxLogFileIdRowStatus = _TmnxLogFileIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 2),
    _TmnxLogFileIdRowStatus_Type()
)
tmnxLogFileIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdRowStatus.setStatus("current")


class _TmnxLogFileIdStorageType_Type(StorageType):
    """Custom type tmnxLogFileIdStorageType based on StorageType"""
    defaultValue = 3


_TmnxLogFileIdStorageType_Type.__name__ = "StorageType"
_TmnxLogFileIdStorageType_Object = MibTableColumn
tmnxLogFileIdStorageType = _TmnxLogFileIdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 3),
    _TmnxLogFileIdStorageType_Type()
)
tmnxLogFileIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdStorageType.setStatus("current")


class _TmnxLogFileIdRolloverTime_Type(Integer32):
    """Custom type tmnxLogFileIdRolloverTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10080),
    )


_TmnxLogFileIdRolloverTime_Type.__name__ = "Integer32"
_TmnxLogFileIdRolloverTime_Object = MibTableColumn
tmnxLogFileIdRolloverTime = _TmnxLogFileIdRolloverTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 4),
    _TmnxLogFileIdRolloverTime_Type()
)
tmnxLogFileIdRolloverTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdRolloverTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogFileIdRolloverTime.setUnits("minutes")


class _TmnxLogFileIdRetainTime_Type(Integer32):
    """Custom type tmnxLogFileIdRetainTime based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_TmnxLogFileIdRetainTime_Type.__name__ = "Integer32"
_TmnxLogFileIdRetainTime_Object = MibTableColumn
tmnxLogFileIdRetainTime = _TmnxLogFileIdRetainTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 5),
    _TmnxLogFileIdRetainTime_Type()
)
tmnxLogFileIdRetainTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdRetainTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogFileIdRetainTime.setUnits("hours")


class _TmnxLogFileIdAdminLocation_Type(TmnxCFlash):
    """Custom type tmnxLogFileIdAdminLocation based on TmnxCFlash"""
    defaultValue = 0


_TmnxLogFileIdAdminLocation_Type.__name__ = "TmnxCFlash"
_TmnxLogFileIdAdminLocation_Object = MibTableColumn
tmnxLogFileIdAdminLocation = _TmnxLogFileIdAdminLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 6),
    _TmnxLogFileIdAdminLocation_Type()
)
tmnxLogFileIdAdminLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdAdminLocation.setStatus("current")
_TmnxLogFileIdOperLocation_Type = TmnxCFlash
_TmnxLogFileIdOperLocation_Object = MibTableColumn
tmnxLogFileIdOperLocation = _TmnxLogFileIdOperLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 7),
    _TmnxLogFileIdOperLocation_Type()
)
tmnxLogFileIdOperLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdOperLocation.setStatus("current")


class _TmnxLogFileIdDescription_Type(TItemDescription):
    """Custom type tmnxLogFileIdDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogFileIdDescription_Type.__name__ = "TItemDescription"
_TmnxLogFileIdDescription_Object = MibTableColumn
tmnxLogFileIdDescription = _TmnxLogFileIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 8),
    _TmnxLogFileIdDescription_Type()
)
tmnxLogFileIdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdDescription.setStatus("current")
_TmnxLogFileIdLogType_Type = TmnxLogFileType
_TmnxLogFileIdLogType_Object = MibTableColumn
tmnxLogFileIdLogType = _TmnxLogFileIdLogType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 9),
    _TmnxLogFileIdLogType_Type()
)
tmnxLogFileIdLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdLogType.setStatus("current")


class _TmnxLogFileIdLogId_Type(Integer32):
    """Custom type tmnxLogFileIdLogId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxLogFileIdLogId_Type.__name__ = "Integer32"
_TmnxLogFileIdLogId_Object = MibTableColumn
tmnxLogFileIdLogId = _TmnxLogFileIdLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 10),
    _TmnxLogFileIdLogId_Type()
)
tmnxLogFileIdLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdLogId.setStatus("current")
_TmnxLogFileIdPathName_Type = DisplayString
_TmnxLogFileIdPathName_Object = MibTableColumn
tmnxLogFileIdPathName = _TmnxLogFileIdPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 11),
    _TmnxLogFileIdPathName_Type()
)
tmnxLogFileIdPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdPathName.setStatus("current")
_TmnxLogFileIdCreateTime_Type = DateAndTime
_TmnxLogFileIdCreateTime_Object = MibTableColumn
tmnxLogFileIdCreateTime = _TmnxLogFileIdCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 12),
    _TmnxLogFileIdCreateTime_Type()
)
tmnxLogFileIdCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdCreateTime.setStatus("current")


class _TmnxLogFileIdBackupLoc_Type(TmnxCFlash):
    """Custom type tmnxLogFileIdBackupLoc based on TmnxCFlash"""
    defaultValue = 0


_TmnxLogFileIdBackupLoc_Type.__name__ = "TmnxCFlash"
_TmnxLogFileIdBackupLoc_Object = MibTableColumn
tmnxLogFileIdBackupLoc = _TmnxLogFileIdBackupLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 13),
    _TmnxLogFileIdBackupLoc_Type()
)
tmnxLogFileIdBackupLoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdBackupLoc.setStatus("current")
_TmnxLogApTable_Object = MibTable
tmnxLogApTable = _TmnxLogApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4)
)
if mibBuilder.loadTexts:
    tmnxLogApTable.setStatus("current")
_TmnxLogApEntry_Object = MibTableRow
tmnxLogApEntry = _TmnxLogApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1)
)
tmnxLogApEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogApPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxLogApEntry.setStatus("current")


class _TmnxLogApPolicyId_Type(Integer32):
    """Custom type tmnxLogApPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TmnxLogApPolicyId_Type.__name__ = "Integer32"
_TmnxLogApPolicyId_Object = MibTableColumn
tmnxLogApPolicyId = _TmnxLogApPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 1),
    _TmnxLogApPolicyId_Type()
)
tmnxLogApPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogApPolicyId.setStatus("current")
_TmnxLogApRowStatus_Type = RowStatus
_TmnxLogApRowStatus_Object = MibTableColumn
tmnxLogApRowStatus = _TmnxLogApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 2),
    _TmnxLogApRowStatus_Type()
)
tmnxLogApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApRowStatus.setStatus("current")


class _TmnxLogApStorageType_Type(StorageType):
    """Custom type tmnxLogApStorageType based on StorageType"""
    defaultValue = 3


_TmnxLogApStorageType_Type.__name__ = "StorageType"
_TmnxLogApStorageType_Object = MibTableColumn
tmnxLogApStorageType = _TmnxLogApStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 3),
    _TmnxLogApStorageType_Type()
)
tmnxLogApStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApStorageType.setStatus("current")


class _TmnxLogApAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxLogApAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxLogApAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxLogApAdminStatus_Object = MibTableColumn
tmnxLogApAdminStatus = _TmnxLogApAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 4),
    _TmnxLogApAdminStatus_Type()
)
tmnxLogApAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApAdminStatus.setStatus("current")
_TmnxLogApOperStatus_Type = TmnxOperState
_TmnxLogApOperStatus_Object = MibTableColumn
tmnxLogApOperStatus = _TmnxLogApOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 5),
    _TmnxLogApOperStatus_Type()
)
tmnxLogApOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApOperStatus.setStatus("current")


class _TmnxLogApInterval_Type(Integer32):
    """Custom type tmnxLogApInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TmnxLogApInterval_Type.__name__ = "Integer32"
_TmnxLogApInterval_Object = MibTableColumn
tmnxLogApInterval = _TmnxLogApInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 6),
    _TmnxLogApInterval_Type()
)
tmnxLogApInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogApInterval.setUnits("minutes")


class _TmnxLogApDescription_Type(TItemDescription):
    """Custom type tmnxLogApDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogApDescription_Type.__name__ = "TItemDescription"
_TmnxLogApDescription_Object = MibTableColumn
tmnxLogApDescription = _TmnxLogApDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 7),
    _TmnxLogApDescription_Type()
)
tmnxLogApDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApDescription.setStatus("current")


class _TmnxLogApDefault_Type(TruthValue):
    """Custom type tmnxLogApDefault based on TruthValue"""
    defaultValue = 2


_TmnxLogApDefault_Type.__name__ = "TruthValue"
_TmnxLogApDefault_Object = MibTableColumn
tmnxLogApDefault = _TmnxLogApDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 8),
    _TmnxLogApDefault_Type()
)
tmnxLogApDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApDefault.setStatus("current")


class _TmnxLogApRecord_Type(Integer32):
    """Custom type tmnxLogApRecord based on Integer32"""
    defaultValue = 0

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
              62)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("svcIngressOctet", 1),
          ("svcEgressOctet", 2),
          ("svcIngressPkt", 3),
          ("svcEgressPkt", 4),
          ("netIngressOctet", 5),
          ("netEgressOctet", 6),
          ("netIngressPkt", 7),
          ("netEgressPkt", 8),
          ("compactSvcInOctet", 9),
          ("combinedSvcIngress", 10),
          ("combinedNetInEgOctet", 11),
          ("combinedSvcInEgOctet", 12),
          ("completeSvcInEg", 13),
          ("combinedSvcSdpInEg", 14),
          ("completeSvcSdpInEg", 15),
          ("completeSubscrIngrEgr", 16),
          ("bsxProtocol", 17),
          ("bsxApplication", 18),
          ("bsxAppGroup", 19),
          ("bsxSubscriberProtocol", 20),
          ("bsxSubscriberApplication", 21),
          ("bsxSubscriberAppGroup", 22),
          ("customRecordSubscriber", 23),
          ("customRecordService", 24),
          ("customRecordAa", 25),
          ("queueGroupOctets", 26),
          ("queueGroupPackets", 27),
          ("combinedQueueGroup", 28),
          ("combinedMplsLspIngress", 29),
          ("combinedMplsLspEgress", 30),
          ("combinedLdpLspEgress", 31),
          ("saa", 32),
          ("video", 33),
          ("kpiSystem", 34),
          ("kpiBearerMgmt", 35),
          ("kpiBearerTraffic", 36),
          ("kpiRefPoint", 37),
          ("kpiPathMgmt", 38),
          ("kciIom3", 39),
          ("kciSystem", 40),
          ("kciBearerMgmt", 41),
          ("kciPathMgmt", 42),
          ("completeKpi", 43),
          ("completeKci", 44),
          ("kpiBearerGroup", 45),
          ("kpiRefPathGroup", 46),
          ("kpiKciBearerMgmt", 47),
          ("kpiKciPathMgmt", 48),
          ("kpiKciSystem", 49),
          ("completeKpiKci", 50),
          ("aaPerformance", 51),
          ("completeEthernetPort", 52),
          ("extendedSvcIngrEgr", 53),
          ("completeNetIngrEgr", 54),
          ("aaPartition", 55),
          ("completeOamPm", 56),
          ("kpiRefPtSecErrorCauseCode", 57),
          ("kpiBearerTrafficGtpEndpoint", 58),
          ("kpiIpReas", 59),
          ("kpiRadiusGroup", 60),
          ("kpiRefPtFailureCauseCode", 61),
          ("kpiDhcpGroup", 62))
    )


_TmnxLogApRecord_Type.__name__ = "Integer32"
_TmnxLogApRecord_Object = MibTableColumn
tmnxLogApRecord = _TmnxLogApRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 9),
    _TmnxLogApRecord_Type()
)
tmnxLogApRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApRecord.setStatus("current")
_TmnxLogApToFileId_Type = TmnxLogFileId
_TmnxLogApToFileId_Object = MibTableColumn
tmnxLogApToFileId = _TmnxLogApToFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 10),
    _TmnxLogApToFileId_Type()
)
tmnxLogApToFileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApToFileId.setStatus("current")


class _TmnxLogApPortType_Type(Integer32):
    """Custom type tmnxLogApPortType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("access", 1),
          ("network", 2),
          ("sdp", 3),
          ("subscriber", 4),
          ("appAssure", 5),
          ("qgrp", 6),
          ("saa", 7),
          ("mplsLspIngr", 8),
          ("mplsLspEgr", 9),
          ("ldpLspEgr", 10),
          ("video", 11),
          ("mobileGateway", 12),
          ("ethernet", 13),
          ("oamPm", 14))
    )


_TmnxLogApPortType_Type.__name__ = "Integer32"
_TmnxLogApPortType_Object = MibTableColumn
tmnxLogApPortType = _TmnxLogApPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 11),
    _TmnxLogApPortType_Type()
)
tmnxLogApPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApPortType.setStatus("current")


class _TmnxLogApDefaultInterval_Type(TruthValue):
    """Custom type tmnxLogApDefaultInterval based on TruthValue"""
    defaultValue = 1


_TmnxLogApDefaultInterval_Type.__name__ = "TruthValue"
_TmnxLogApDefaultInterval_Object = MibTableColumn
tmnxLogApDefaultInterval = _TmnxLogApDefaultInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 12),
    _TmnxLogApDefaultInterval_Type()
)
tmnxLogApDefaultInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApDefaultInterval.setStatus("current")
_TmnxLogApDataLossCount_Type = Counter32
_TmnxLogApDataLossCount_Object = MibTableColumn
tmnxLogApDataLossCount = _TmnxLogApDataLossCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 13),
    _TmnxLogApDataLossCount_Type()
)
tmnxLogApDataLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApDataLossCount.setStatus("current")
_TmnxLogApLastDataLossTimeStamp_Type = TimeStamp
_TmnxLogApLastDataLossTimeStamp_Object = MibTableColumn
tmnxLogApLastDataLossTimeStamp = _TmnxLogApLastDataLossTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 14),
    _TmnxLogApLastDataLossTimeStamp_Type()
)
tmnxLogApLastDataLossTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApLastDataLossTimeStamp.setStatus("current")


class _TmnxLogApToFileType_Type(Integer32):
    """Custom type tmnxLogApToFileType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fileId", 0),
          ("noFile", 1))
    )


_TmnxLogApToFileType_Type.__name__ = "Integer32"
_TmnxLogApToFileType_Object = MibTableColumn
tmnxLogApToFileType = _TmnxLogApToFileType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 15),
    _TmnxLogApToFileType_Type()
)
tmnxLogApToFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApToFileType.setStatus("current")


class _TmnxLogApIncludeSystemInfo_Type(TruthValue):
    """Custom type tmnxLogApIncludeSystemInfo based on TruthValue"""
    defaultValue = 2


_TmnxLogApIncludeSystemInfo_Type.__name__ = "TruthValue"
_TmnxLogApIncludeSystemInfo_Object = MibTableColumn
tmnxLogApIncludeSystemInfo = _TmnxLogApIncludeSystemInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 16),
    _TmnxLogApIncludeSystemInfo_Type()
)
tmnxLogApIncludeSystemInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApIncludeSystemInfo.setStatus("current")
_TmnxLogIdTable_Object = MibTable
tmnxLogIdTable = _TmnxLogIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5)
)
if mibBuilder.loadTexts:
    tmnxLogIdTable.setStatus("current")
_TmnxLogIdEntry_Object = MibTableRow
tmnxLogIdEntry = _TmnxLogIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1)
)
tmnxLogIdEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogIdIndex"),
)
if mibBuilder.loadTexts:
    tmnxLogIdEntry.setStatus("current")
_TmnxLogIdIndex_Type = TmnxLogIdIndex
_TmnxLogIdIndex_Object = MibTableColumn
tmnxLogIdIndex = _TmnxLogIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 1),
    _TmnxLogIdIndex_Type()
)
tmnxLogIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogIdIndex.setStatus("current")
_TmnxLogIdRowStatus_Type = RowStatus
_TmnxLogIdRowStatus_Object = MibTableColumn
tmnxLogIdRowStatus = _TmnxLogIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 2),
    _TmnxLogIdRowStatus_Type()
)
tmnxLogIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdRowStatus.setStatus("current")


class _TmnxLogIdStorageType_Type(StorageType):
    """Custom type tmnxLogIdStorageType based on StorageType"""
    defaultValue = 3


_TmnxLogIdStorageType_Type.__name__ = "StorageType"
_TmnxLogIdStorageType_Object = MibTableColumn
tmnxLogIdStorageType = _TmnxLogIdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 3),
    _TmnxLogIdStorageType_Type()
)
tmnxLogIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdStorageType.setStatus("current")


class _TmnxLogIdAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxLogIdAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxLogIdAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxLogIdAdminStatus_Object = MibTableColumn
tmnxLogIdAdminStatus = _TmnxLogIdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 4),
    _TmnxLogIdAdminStatus_Type()
)
tmnxLogIdAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdAdminStatus.setStatus("current")
_TmnxLogIdOperStatus_Type = TmnxOperState
_TmnxLogIdOperStatus_Object = MibTableColumn
tmnxLogIdOperStatus = _TmnxLogIdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 5),
    _TmnxLogIdOperStatus_Type()
)
tmnxLogIdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogIdOperStatus.setStatus("current")


class _TmnxLogIdDescription_Type(TItemDescription):
    """Custom type tmnxLogIdDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogIdDescription_Type.__name__ = "TItemDescription"
_TmnxLogIdDescription_Object = MibTableColumn
tmnxLogIdDescription = _TmnxLogIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 6),
    _TmnxLogIdDescription_Type()
)
tmnxLogIdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdDescription.setStatus("current")


class _TmnxLogIdFilterId_Type(TmnxLogFilterId):
    """Custom type tmnxLogIdFilterId based on TmnxLogFilterId"""
    defaultValue = 0


_TmnxLogIdFilterId_Type.__name__ = "TmnxLogFilterId"
_TmnxLogIdFilterId_Object = MibTableColumn
tmnxLogIdFilterId = _TmnxLogIdFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 7),
    _TmnxLogIdFilterId_Type()
)
tmnxLogIdFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdFilterId.setStatus("current")


class _TmnxLogIdSource_Type(Bits):
    """Custom type tmnxLogIdSource based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("main", 0),
          ("security", 1),
          ("change", 2),
          ("debugTrace", 3),
          ("li", 4))
    )

_TmnxLogIdSource_Type.__name__ = "Bits"
_TmnxLogIdSource_Object = MibTableColumn
tmnxLogIdSource = _TmnxLogIdSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 8),
    _TmnxLogIdSource_Type()
)
tmnxLogIdSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdSource.setStatus("current")


class _TmnxLogIdDestination_Type(Integer32):
    """Custom type tmnxLogIdDestination based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("console", 1),
          ("syslog", 2),
          ("snmpTraps", 3),
          ("file", 4),
          ("memory", 5))
    )


_TmnxLogIdDestination_Type.__name__ = "Integer32"
_TmnxLogIdDestination_Object = MibTableColumn
tmnxLogIdDestination = _TmnxLogIdDestination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 9),
    _TmnxLogIdDestination_Type()
)
tmnxLogIdDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdDestination.setStatus("current")
_TmnxLogIdFileId_Type = TmnxLogFileId
_TmnxLogIdFileId_Object = MibTableColumn
tmnxLogIdFileId = _TmnxLogIdFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 10),
    _TmnxLogIdFileId_Type()
)
tmnxLogIdFileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdFileId.setStatus("current")


class _TmnxLogIdSyslogId_Type(TmnxSyslogIdOrEmpty):
    """Custom type tmnxLogIdSyslogId based on TmnxSyslogIdOrEmpty"""
    defaultValue = 0


_TmnxLogIdSyslogId_Type.__name__ = "TmnxSyslogIdOrEmpty"
_TmnxLogIdSyslogId_Object = MibTableColumn
tmnxLogIdSyslogId = _TmnxLogIdSyslogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 11),
    _TmnxLogIdSyslogId_Type()
)
tmnxLogIdSyslogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdSyslogId.setStatus("current")


class _TmnxLogIdMaxMemorySize_Type(Unsigned32):
    """Custom type tmnxLogIdMaxMemorySize based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 3000),
    )


_TmnxLogIdMaxMemorySize_Type.__name__ = "Unsigned32"
_TmnxLogIdMaxMemorySize_Object = MibTableColumn
tmnxLogIdMaxMemorySize = _TmnxLogIdMaxMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 12),
    _TmnxLogIdMaxMemorySize_Type()
)
tmnxLogIdMaxMemorySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdMaxMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogIdMaxMemorySize.setUnits("events")


class _TmnxLogIdConsoleSession_Type(TruthValue):
    """Custom type tmnxLogIdConsoleSession based on TruthValue"""
    defaultValue = 2


_TmnxLogIdConsoleSession_Type.__name__ = "TruthValue"
_TmnxLogIdConsoleSession_Object = MibTableColumn
tmnxLogIdConsoleSession = _TmnxLogIdConsoleSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 13),
    _TmnxLogIdConsoleSession_Type()
)
tmnxLogIdConsoleSession.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdConsoleSession.setStatus("current")
_TmnxLogIdForwarded_Type = Counter64
_TmnxLogIdForwarded_Object = MibTableColumn
tmnxLogIdForwarded = _TmnxLogIdForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 14),
    _TmnxLogIdForwarded_Type()
)
tmnxLogIdForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogIdForwarded.setStatus("current")
_TmnxLogIdDropped_Type = Counter64
_TmnxLogIdDropped_Object = MibTableColumn
tmnxLogIdDropped = _TmnxLogIdDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 15),
    _TmnxLogIdDropped_Type()
)
tmnxLogIdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogIdDropped.setStatus("current")


class _TmnxLogIdTimeFormat_Type(Integer32):
    """Custom type tmnxLogIdTimeFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("utc", 1),
          ("local", 2))
    )


_TmnxLogIdTimeFormat_Type.__name__ = "Integer32"
_TmnxLogIdTimeFormat_Object = MibTableColumn
tmnxLogIdTimeFormat = _TmnxLogIdTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 16),
    _TmnxLogIdTimeFormat_Type()
)
tmnxLogIdTimeFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdTimeFormat.setStatus("current")
_TmnxLogFilterTable_Object = MibTable
tmnxLogFilterTable = _TmnxLogFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6)
)
if mibBuilder.loadTexts:
    tmnxLogFilterTable.setStatus("current")
_TmnxLogFilterEntry_Object = MibTableRow
tmnxLogFilterEntry = _TmnxLogFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1)
)
tmnxLogFilterEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogFilterId"),
)
if mibBuilder.loadTexts:
    tmnxLogFilterEntry.setStatus("current")


class _TmnxLogFilterId_Type(TmnxLogFilterId):
    """Custom type tmnxLogFilterId based on TmnxLogFilterId"""
    subtypeSpec = TmnxLogFilterId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1001),
    )


_TmnxLogFilterId_Type.__name__ = "TmnxLogFilterId"
_TmnxLogFilterId_Object = MibTableColumn
tmnxLogFilterId = _TmnxLogFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 1),
    _TmnxLogFilterId_Type()
)
tmnxLogFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogFilterId.setStatus("current")
_TmnxLogFilterRowStatus_Type = RowStatus
_TmnxLogFilterRowStatus_Object = MibTableColumn
tmnxLogFilterRowStatus = _TmnxLogFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 2),
    _TmnxLogFilterRowStatus_Type()
)
tmnxLogFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterRowStatus.setStatus("current")


class _TmnxLogFilterDescription_Type(TItemDescription):
    """Custom type tmnxLogFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogFilterDescription_Type.__name__ = "TItemDescription"
_TmnxLogFilterDescription_Object = MibTableColumn
tmnxLogFilterDescription = _TmnxLogFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 3),
    _TmnxLogFilterDescription_Type()
)
tmnxLogFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterDescription.setStatus("current")


class _TmnxLogFilterDefaultAction_Type(TFilterAction):
    """Custom type tmnxLogFilterDefaultAction based on TFilterAction"""
    defaultValue = 2


_TmnxLogFilterDefaultAction_Type.__name__ = "TFilterAction"
_TmnxLogFilterDefaultAction_Object = MibTableColumn
tmnxLogFilterDefaultAction = _TmnxLogFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 4),
    _TmnxLogFilterDefaultAction_Type()
)
tmnxLogFilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterDefaultAction.setStatus("current")
_TmnxLogFilterInUse_Type = TruthValue
_TmnxLogFilterInUse_Object = MibTableColumn
tmnxLogFilterInUse = _TmnxLogFilterInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 5),
    _TmnxLogFilterInUse_Type()
)
tmnxLogFilterInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFilterInUse.setStatus("current")
_TmnxLogFilterParamsTable_Object = MibTable
tmnxLogFilterParamsTable = _TmnxLogFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7)
)
if mibBuilder.loadTexts:
    tmnxLogFilterParamsTable.setStatus("current")
_TmnxLogFilterParamsEntry_Object = MibTableRow
tmnxLogFilterParamsEntry = _TmnxLogFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1)
)
tmnxLogFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogFilterId"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogFilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tmnxLogFilterParamsEntry.setStatus("current")
_TmnxLogFilterParamsIndex_Type = TmnxLogFilterEntryId
_TmnxLogFilterParamsIndex_Object = MibTableColumn
tmnxLogFilterParamsIndex = _TmnxLogFilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 1),
    _TmnxLogFilterParamsIndex_Type()
)
tmnxLogFilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsIndex.setStatus("current")
_TmnxLogFilterParamsRowStatus_Type = RowStatus
_TmnxLogFilterParamsRowStatus_Object = MibTableColumn
tmnxLogFilterParamsRowStatus = _TmnxLogFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 2),
    _TmnxLogFilterParamsRowStatus_Type()
)
tmnxLogFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsRowStatus.setStatus("current")


class _TmnxLogFilterParamsDescription_Type(TItemDescription):
    """Custom type tmnxLogFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogFilterParamsDescription_Type.__name__ = "TItemDescription"
_TmnxLogFilterParamsDescription_Object = MibTableColumn
tmnxLogFilterParamsDescription = _TmnxLogFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 3),
    _TmnxLogFilterParamsDescription_Type()
)
tmnxLogFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsDescription.setStatus("current")


class _TmnxLogFilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tmnxLogFilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 3


_TmnxLogFilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TmnxLogFilterParamsAction_Object = MibTableColumn
tmnxLogFilterParamsAction = _TmnxLogFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 4),
    _TmnxLogFilterParamsAction_Type()
)
tmnxLogFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsAction.setStatus("current")


class _TmnxLogFilterParamsApplication_Type(TNamedItemOrEmpty):
    """Custom type tmnxLogFilterParamsApplication based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLogFilterParamsApplication_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLogFilterParamsApplication_Object = MibTableColumn
tmnxLogFilterParamsApplication = _TmnxLogFilterParamsApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 5),
    _TmnxLogFilterParamsApplication_Type()
)
tmnxLogFilterParamsApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsApplication.setStatus("current")


class _TmnxLogFilterParamsApplOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsApplOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsApplOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsApplOperator_Object = MibTableColumn
tmnxLogFilterParamsApplOperator = _TmnxLogFilterParamsApplOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 6),
    _TmnxLogFilterParamsApplOperator_Type()
)
tmnxLogFilterParamsApplOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsApplOperator.setStatus("current")


class _TmnxLogFilterParamsNumber_Type(TmnxEventNumber):
    """Custom type tmnxLogFilterParamsNumber based on TmnxEventNumber"""
    defaultValue = 0


_TmnxLogFilterParamsNumber_Type.__name__ = "TmnxEventNumber"
_TmnxLogFilterParamsNumber_Object = MibTableColumn
tmnxLogFilterParamsNumber = _TmnxLogFilterParamsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 7),
    _TmnxLogFilterParamsNumber_Type()
)
tmnxLogFilterParamsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsNumber.setStatus("current")


class _TmnxLogFilterParamsNumberOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsNumberOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsNumberOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsNumberOperator_Object = MibTableColumn
tmnxLogFilterParamsNumberOperator = _TmnxLogFilterParamsNumberOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 8),
    _TmnxLogFilterParamsNumberOperator_Type()
)
tmnxLogFilterParamsNumberOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsNumberOperator.setStatus("current")


class _TmnxLogFilterParamsSeverity_Type(TmnxPerceivedSeverity):
    """Custom type tmnxLogFilterParamsSeverity based on TmnxPerceivedSeverity"""
    defaultValue = 0


_TmnxLogFilterParamsSeverity_Type.__name__ = "TmnxPerceivedSeverity"
_TmnxLogFilterParamsSeverity_Object = MibTableColumn
tmnxLogFilterParamsSeverity = _TmnxLogFilterParamsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 9),
    _TmnxLogFilterParamsSeverity_Type()
)
tmnxLogFilterParamsSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSeverity.setStatus("current")


class _TmnxLogFilterParamsSeverityOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsSeverityOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsSeverityOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsSeverityOperator_Object = MibTableColumn
tmnxLogFilterParamsSeverityOperator = _TmnxLogFilterParamsSeverityOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 10),
    _TmnxLogFilterParamsSeverityOperator_Type()
)
tmnxLogFilterParamsSeverityOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSeverityOperator.setStatus("current")


class _TmnxLogFilterParamsSubject_Type(TNamedItemOrEmpty):
    """Custom type tmnxLogFilterParamsSubject based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLogFilterParamsSubject_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLogFilterParamsSubject_Object = MibTableColumn
tmnxLogFilterParamsSubject = _TmnxLogFilterParamsSubject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 11),
    _TmnxLogFilterParamsSubject_Type()
)
tmnxLogFilterParamsSubject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSubject.setStatus("current")


class _TmnxLogFilterParamsSubjectOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsSubjectOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsSubjectOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsSubjectOperator_Object = MibTableColumn
tmnxLogFilterParamsSubjectOperator = _TmnxLogFilterParamsSubjectOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 12),
    _TmnxLogFilterParamsSubjectOperator_Type()
)
tmnxLogFilterParamsSubjectOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSubjectOperator.setStatus("current")


class _TmnxLogFilterParamsSubjectRegexp_Type(TruthValue):
    """Custom type tmnxLogFilterParamsSubjectRegexp based on TruthValue"""
    defaultValue = 2


_TmnxLogFilterParamsSubjectRegexp_Type.__name__ = "TruthValue"
_TmnxLogFilterParamsSubjectRegexp_Object = MibTableColumn
tmnxLogFilterParamsSubjectRegexp = _TmnxLogFilterParamsSubjectRegexp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 13),
    _TmnxLogFilterParamsSubjectRegexp_Type()
)
tmnxLogFilterParamsSubjectRegexp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSubjectRegexp.setStatus("current")


class _TmnxLogFilterParamsRouter_Type(TNamedItemOrEmpty):
    """Custom type tmnxLogFilterParamsRouter based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLogFilterParamsRouter_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLogFilterParamsRouter_Object = MibTableColumn
tmnxLogFilterParamsRouter = _TmnxLogFilterParamsRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 14),
    _TmnxLogFilterParamsRouter_Type()
)
tmnxLogFilterParamsRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsRouter.setStatus("current")


class _TmnxLogFilterParamsRouterOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsRouterOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsRouterOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsRouterOperator_Object = MibTableColumn
tmnxLogFilterParamsRouterOperator = _TmnxLogFilterParamsRouterOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 15),
    _TmnxLogFilterParamsRouterOperator_Type()
)
tmnxLogFilterParamsRouterOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsRouterOperator.setStatus("current")


class _TmnxLogFilterParamsRouterRegexp_Type(TruthValue):
    """Custom type tmnxLogFilterParamsRouterRegexp based on TruthValue"""
    defaultValue = 2


_TmnxLogFilterParamsRouterRegexp_Type.__name__ = "TruthValue"
_TmnxLogFilterParamsRouterRegexp_Object = MibTableColumn
tmnxLogFilterParamsRouterRegexp = _TmnxLogFilterParamsRouterRegexp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 16),
    _TmnxLogFilterParamsRouterRegexp_Type()
)
tmnxLogFilterParamsRouterRegexp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsRouterRegexp.setStatus("current")
_TmnxSyslogTargetTable_Object = MibTable
tmnxSyslogTargetTable = _TmnxSyslogTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8)
)
if mibBuilder.loadTexts:
    tmnxSyslogTargetTable.setStatus("current")
_TmnxSyslogTargetEntry_Object = MibTableRow
tmnxSyslogTargetEntry = _TmnxSyslogTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1)
)
tmnxSyslogTargetEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxSyslogTargetIndex"),
)
if mibBuilder.loadTexts:
    tmnxSyslogTargetEntry.setStatus("current")
_TmnxSyslogTargetIndex_Type = TmnxSyslogId
_TmnxSyslogTargetIndex_Object = MibTableColumn
tmnxSyslogTargetIndex = _TmnxSyslogTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 1),
    _TmnxSyslogTargetIndex_Type()
)
tmnxSyslogTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSyslogTargetIndex.setStatus("current")
_TmnxSyslogTargetRowStatus_Type = RowStatus
_TmnxSyslogTargetRowStatus_Object = MibTableColumn
tmnxSyslogTargetRowStatus = _TmnxSyslogTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 2),
    _TmnxSyslogTargetRowStatus_Type()
)
tmnxSyslogTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetRowStatus.setStatus("current")


class _TmnxSyslogTargetDescription_Type(TItemDescription):
    """Custom type tmnxSyslogTargetDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSyslogTargetDescription_Type.__name__ = "TItemDescription"
_TmnxSyslogTargetDescription_Object = MibTableColumn
tmnxSyslogTargetDescription = _TmnxSyslogTargetDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 3),
    _TmnxSyslogTargetDescription_Type()
)
tmnxSyslogTargetDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetDescription.setStatus("current")


class _TmnxSyslogTargetAddress_Type(IpAddress):
    """Custom type tmnxSyslogTargetAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxSyslogTargetAddress_Type.__name__ = "IpAddress"
_TmnxSyslogTargetAddress_Object = MibTableColumn
tmnxSyslogTargetAddress = _TmnxSyslogTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 4),
    _TmnxSyslogTargetAddress_Type()
)
tmnxSyslogTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetAddress.setStatus("obsolete")


class _TmnxSyslogTargetUdpPort_Type(TmnxUdpPort):
    """Custom type tmnxSyslogTargetUdpPort based on TmnxUdpPort"""
    defaultValue = 514


_TmnxSyslogTargetUdpPort_Type.__name__ = "TmnxUdpPort"
_TmnxSyslogTargetUdpPort_Object = MibTableColumn
tmnxSyslogTargetUdpPort = _TmnxSyslogTargetUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 5),
    _TmnxSyslogTargetUdpPort_Type()
)
tmnxSyslogTargetUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetUdpPort.setStatus("current")


class _TmnxSyslogTargetFacility_Type(TmnxSyslogFacility):
    """Custom type tmnxSyslogTargetFacility based on TmnxSyslogFacility"""
    defaultValue = 23


_TmnxSyslogTargetFacility_Type.__name__ = "TmnxSyslogFacility"
_TmnxSyslogTargetFacility_Object = MibTableColumn
tmnxSyslogTargetFacility = _TmnxSyslogTargetFacility_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 6),
    _TmnxSyslogTargetFacility_Type()
)
tmnxSyslogTargetFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetFacility.setStatus("current")


class _TmnxSyslogTargetSeverity_Type(TmnxSyslogSeverity):
    """Custom type tmnxSyslogTargetSeverity based on TmnxSyslogSeverity"""
    defaultValue = 6


_TmnxSyslogTargetSeverity_Type.__name__ = "TmnxSyslogSeverity"
_TmnxSyslogTargetSeverity_Object = MibTableColumn
tmnxSyslogTargetSeverity = _TmnxSyslogTargetSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 7),
    _TmnxSyslogTargetSeverity_Type()
)
tmnxSyslogTargetSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetSeverity.setStatus("current")


class _TmnxSyslogTargetMessagePrefix_Type(TNamedItemOrEmpty):
    """Custom type tmnxSyslogTargetMessagePrefix based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSyslogTargetMessagePrefix_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSyslogTargetMessagePrefix_Object = MibTableColumn
tmnxSyslogTargetMessagePrefix = _TmnxSyslogTargetMessagePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 8),
    _TmnxSyslogTargetMessagePrefix_Type()
)
tmnxSyslogTargetMessagePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetMessagePrefix.setStatus("current")
_TmnxSyslogTargetMessagesDropped_Type = Counter32
_TmnxSyslogTargetMessagesDropped_Object = MibTableColumn
tmnxSyslogTargetMessagesDropped = _TmnxSyslogTargetMessagesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 9),
    _TmnxSyslogTargetMessagesDropped_Type()
)
tmnxSyslogTargetMessagesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyslogTargetMessagesDropped.setStatus("current")


class _TmnxSyslogTargetAddrType_Type(InetAddressType):
    """Custom type tmnxSyslogTargetAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxSyslogTargetAddrType_Type.__name__ = "InetAddressType"
_TmnxSyslogTargetAddrType_Object = MibTableColumn
tmnxSyslogTargetAddrType = _TmnxSyslogTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 10),
    _TmnxSyslogTargetAddrType_Type()
)
tmnxSyslogTargetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetAddrType.setStatus("current")


class _TmnxSyslogTargetAddr_Type(InetAddress):
    """Custom type tmnxSyslogTargetAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxSyslogTargetAddr_Type.__name__ = "InetAddress"
_TmnxSyslogTargetAddr_Object = MibTableColumn
tmnxSyslogTargetAddr = _TmnxSyslogTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 11),
    _TmnxSyslogTargetAddr_Type()
)
tmnxSyslogTargetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetAddr.setStatus("current")
_TmnxEventAppTable_Object = MibTable
tmnxEventAppTable = _TmnxEventAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 9)
)
if mibBuilder.loadTexts:
    tmnxEventAppTable.setStatus("current")
_TmnxEventAppEntry_Object = MibTableRow
tmnxEventAppEntry = _TmnxEventAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 9, 1)
)
tmnxEventAppEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEventAppIndex"),
)
if mibBuilder.loadTexts:
    tmnxEventAppEntry.setStatus("current")
_TmnxEventAppIndex_Type = Unsigned32
_TmnxEventAppIndex_Object = MibTableColumn
tmnxEventAppIndex = _TmnxEventAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 9, 1, 1),
    _TmnxEventAppIndex_Type()
)
tmnxEventAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEventAppIndex.setStatus("current")
_TmnxEventAppName_Type = TNamedItem
_TmnxEventAppName_Object = MibTableColumn
tmnxEventAppName = _TmnxEventAppName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 9, 1, 2),
    _TmnxEventAppName_Type()
)
tmnxEventAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventAppName.setStatus("current")
_TmnxEventTable_Object = MibTable
tmnxEventTable = _TmnxEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10)
)
if mibBuilder.loadTexts:
    tmnxEventTable.setStatus("current")
_TmnxEventEntry_Object = MibTableRow
tmnxEventEntry = _TmnxEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1)
)
tmnxEventEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEventAppIndex"),
    (0, "TIMETRA-LOG-MIB", "tmnxEventID"),
)
if mibBuilder.loadTexts:
    tmnxEventEntry.setStatus("current")
_TmnxEventID_Type = Unsigned32
_TmnxEventID_Object = MibTableColumn
tmnxEventID = _TmnxEventID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 1),
    _TmnxEventID_Type()
)
tmnxEventID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEventID.setStatus("current")
_TmnxEventName_Type = TNamedItem
_TmnxEventName_Object = MibTableColumn
tmnxEventName = _TmnxEventName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 2),
    _TmnxEventName_Type()
)
tmnxEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventName.setStatus("current")
_TmnxEventSeverity_Type = TmnxPerceivedSeverity
_TmnxEventSeverity_Object = MibTableColumn
tmnxEventSeverity = _TmnxEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 3),
    _TmnxEventSeverity_Type()
)
tmnxEventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSeverity.setStatus("current")
_TmnxEventControl_Type = TruthValue
_TmnxEventControl_Object = MibTableColumn
tmnxEventControl = _TmnxEventControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 4),
    _TmnxEventControl_Type()
)
tmnxEventControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventControl.setStatus("current")
_TmnxEventCounter_Type = Counter32
_TmnxEventCounter_Object = MibTableColumn
tmnxEventCounter = _TmnxEventCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 5),
    _TmnxEventCounter_Type()
)
tmnxEventCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventCounter.setStatus("current")
_TmnxEventDropCount_Type = Counter32
_TmnxEventDropCount_Object = MibTableColumn
tmnxEventDropCount = _TmnxEventDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 6),
    _TmnxEventDropCount_Type()
)
tmnxEventDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventDropCount.setStatus("current")


class _TmnxEventReset_Type(TmnxActionType):
    """Custom type tmnxEventReset based on TmnxActionType"""
    defaultValue = 2


_TmnxEventReset_Type.__name__ = "TmnxActionType"
_TmnxEventReset_Object = MibTableColumn
tmnxEventReset = _TmnxEventReset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 7),
    _TmnxEventReset_Type()
)
tmnxEventReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventReset.setStatus("current")


class _TmnxEventThrottle_Type(TruthValue):
    """Custom type tmnxEventThrottle based on TruthValue"""
    defaultValue = 2


_TmnxEventThrottle_Type.__name__ = "TruthValue"
_TmnxEventThrottle_Object = MibTableColumn
tmnxEventThrottle = _TmnxEventThrottle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 8),
    _TmnxEventThrottle_Type()
)
tmnxEventThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventThrottle.setStatus("current")
_TmnxEventSpecThrottle_Type = TruthValue
_TmnxEventSpecThrottle_Object = MibTableColumn
tmnxEventSpecThrottle = _TmnxEventSpecThrottle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 9),
    _TmnxEventSpecThrottle_Type()
)
tmnxEventSpecThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottle.setStatus("current")


class _TmnxEventSpecThrottleLimit_Type(Unsigned32):
    """Custom type tmnxEventSpecThrottleLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 20000),
    )


_TmnxEventSpecThrottleLimit_Type.__name__ = "Unsigned32"
_TmnxEventSpecThrottleLimit_Object = MibTableColumn
tmnxEventSpecThrottleLimit = _TmnxEventSpecThrottleLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 10),
    _TmnxEventSpecThrottleLimit_Type()
)
tmnxEventSpecThrottleLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleLimit.setUnits("events")


class _TmnxEventSpecThrottleIntval_Type(Unsigned32):
    """Custom type tmnxEventSpecThrottleIntval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1200),
    )


_TmnxEventSpecThrottleIntval_Type.__name__ = "Unsigned32"
_TmnxEventSpecThrottleIntval_Object = MibTableColumn
tmnxEventSpecThrottleIntval = _TmnxEventSpecThrottleIntval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 11),
    _TmnxEventSpecThrottleIntval_Type()
)
tmnxEventSpecThrottleIntval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleIntval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleIntval.setUnits("seconds")
_TmnxEventSpecThrottleDef_Type = TruthValue
_TmnxEventSpecThrottleDef_Object = MibTableColumn
tmnxEventSpecThrottleDef = _TmnxEventSpecThrottleDef_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 12),
    _TmnxEventSpecThrottleDef_Type()
)
tmnxEventSpecThrottleDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleDef.setStatus("current")


class _TmnxEventSpecThrottleLimitDef_Type(Unsigned32):
    """Custom type tmnxEventSpecThrottleLimitDef based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 20000),
    )


_TmnxEventSpecThrottleLimitDef_Type.__name__ = "Unsigned32"
_TmnxEventSpecThrottleLimitDef_Object = MibTableColumn
tmnxEventSpecThrottleLimitDef = _TmnxEventSpecThrottleLimitDef_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 13),
    _TmnxEventSpecThrottleLimitDef_Type()
)
tmnxEventSpecThrottleLimitDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleLimitDef.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleLimitDef.setUnits("events")


class _TmnxEventSpecThrottleIntvalDef_Type(Unsigned32):
    """Custom type tmnxEventSpecThrottleIntvalDef based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1200),
    )


_TmnxEventSpecThrottleIntvalDef_Type.__name__ = "Unsigned32"
_TmnxEventSpecThrottleIntvalDef_Object = MibTableColumn
tmnxEventSpecThrottleIntvalDef = _TmnxEventSpecThrottleIntvalDef_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 14),
    _TmnxEventSpecThrottleIntvalDef_Type()
)
tmnxEventSpecThrottleIntvalDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleIntvalDef.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleIntvalDef.setUnits("seconds")
_TmnxSnmpTrapGroupTable_Object = MibTable
tmnxSnmpTrapGroupTable = _TmnxSnmpTrapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11)
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapGroupTable.setStatus("obsolete")
_TmnxSnmpTrapGroupEntry_Object = MibTableRow
tmnxSnmpTrapGroupEntry = _TmnxSnmpTrapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1)
)
tmnxSnmpTrapGroupEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxStgIndex"),
    (0, "TIMETRA-LOG-MIB", "tmnxStgDestAddress"),
    (0, "TIMETRA-LOG-MIB", "tmnxStgDestPort"),
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapGroupEntry.setStatus("obsolete")
_TmnxStgIndex_Type = TmnxLogIdIndex
_TmnxStgIndex_Object = MibTableColumn
tmnxStgIndex = _TmnxStgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 1),
    _TmnxStgIndex_Type()
)
tmnxStgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStgIndex.setStatus("obsolete")


class _TmnxStgDestAddress_Type(IpAddress):
    """Custom type tmnxStgDestAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxStgDestAddress_Type.__name__ = "IpAddress"
_TmnxStgDestAddress_Object = MibTableColumn
tmnxStgDestAddress = _TmnxStgDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 2),
    _TmnxStgDestAddress_Type()
)
tmnxStgDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStgDestAddress.setStatus("obsolete")


class _TmnxStgDestPort_Type(TmnxUdpPort):
    """Custom type tmnxStgDestPort based on TmnxUdpPort"""
    defaultValue = 162


_TmnxStgDestPort_Type.__name__ = "TmnxUdpPort"
_TmnxStgDestPort_Object = MibTableColumn
tmnxStgDestPort = _TmnxStgDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 3),
    _TmnxStgDestPort_Type()
)
tmnxStgDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStgDestPort.setStatus("obsolete")
_TmnxStgRowStatus_Type = RowStatus
_TmnxStgRowStatus_Object = MibTableColumn
tmnxStgRowStatus = _TmnxStgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 4),
    _TmnxStgRowStatus_Type()
)
tmnxStgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgRowStatus.setStatus("obsolete")


class _TmnxStgDescription_Type(TItemDescription):
    """Custom type tmnxStgDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxStgDescription_Type.__name__ = "TItemDescription"
_TmnxStgDescription_Object = MibTableColumn
tmnxStgDescription = _TmnxStgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 5),
    _TmnxStgDescription_Type()
)
tmnxStgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgDescription.setStatus("obsolete")


class _TmnxStgVersion_Type(SnmpMessageProcessingModel):
    """Custom type tmnxStgVersion based on SnmpMessageProcessingModel"""
    defaultValue = 3


_TmnxStgVersion_Type.__name__ = "SnmpMessageProcessingModel"
_TmnxStgVersion_Object = MibTableColumn
tmnxStgVersion = _TmnxStgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 6),
    _TmnxStgVersion_Type()
)
tmnxStgVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgVersion.setStatus("obsolete")


class _TmnxStgNotifyCommunity_Type(OctetString):
    """Custom type tmnxStgNotifyCommunity based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxStgNotifyCommunity_Type.__name__ = "OctetString"
_TmnxStgNotifyCommunity_Object = MibTableColumn
tmnxStgNotifyCommunity = _TmnxStgNotifyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 7),
    _TmnxStgNotifyCommunity_Type()
)
tmnxStgNotifyCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgNotifyCommunity.setStatus("obsolete")


class _TmnxStgSecurityLevel_Type(SnmpSecurityLevel):
    """Custom type tmnxStgSecurityLevel based on SnmpSecurityLevel"""
    defaultValue = 1


_TmnxStgSecurityLevel_Type.__name__ = "SnmpSecurityLevel"
_TmnxStgSecurityLevel_Object = MibTableColumn
tmnxStgSecurityLevel = _TmnxStgSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 8),
    _TmnxStgSecurityLevel_Type()
)
tmnxStgSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgSecurityLevel.setStatus("obsolete")


class _TmnxEventTest_Type(TmnxActionType):
    """Custom type tmnxEventTest based on TmnxActionType"""
    defaultValue = 2


_TmnxEventTest_Type.__name__ = "TmnxActionType"
_TmnxEventTest_Object = MibScalar
tmnxEventTest = _TmnxEventTest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 12),
    _TmnxEventTest_Type()
)
tmnxEventTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventTest.setStatus("current")


class _TmnxEventThrottleLimit_Type(Unsigned32):
    """Custom type tmnxEventThrottleLimit based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_TmnxEventThrottleLimit_Type.__name__ = "Unsigned32"
_TmnxEventThrottleLimit_Object = MibScalar
tmnxEventThrottleLimit = _TmnxEventThrottleLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 13),
    _TmnxEventThrottleLimit_Type()
)
tmnxEventThrottleLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventThrottleLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventThrottleLimit.setUnits("events")


class _TmnxEventThrottleInterval_Type(Unsigned32):
    """Custom type tmnxEventThrottleInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_TmnxEventThrottleInterval_Type.__name__ = "Unsigned32"
_TmnxEventThrottleInterval_Object = MibScalar
tmnxEventThrottleInterval = _TmnxEventThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 14),
    _TmnxEventThrottleInterval_Type()
)
tmnxEventThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventThrottleInterval.setUnits("seconds")
_TmnxSnmpSetErrsMax_Type = Unsigned32
_TmnxSnmpSetErrsMax_Object = MibScalar
tmnxSnmpSetErrsMax = _TmnxSnmpSetErrsMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 15),
    _TmnxSnmpSetErrsMax_Type()
)
tmnxSnmpSetErrsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSnmpSetErrsMax.setStatus("current")
_TmnxSnmpSetErrsTable_Object = MibTable
tmnxSnmpSetErrsTable = _TmnxSnmpSetErrsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16)
)
if mibBuilder.loadTexts:
    tmnxSnmpSetErrsTable.setStatus("current")
_TmnxSnmpSetErrsEntry_Object = MibTableRow
tmnxSnmpSetErrsEntry = _TmnxSnmpSetErrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1)
)
tmnxSnmpSetErrsEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxSseAddressType"),
    (0, "TIMETRA-LOG-MIB", "tmnxSseAddress"),
    (0, "TIMETRA-LOG-MIB", "tmnxSseSnmpPort"),
    (0, "TIMETRA-LOG-MIB", "tmnxSseRequestId"),
)
if mibBuilder.loadTexts:
    tmnxSnmpSetErrsEntry.setStatus("current")
_TmnxSseAddressType_Type = InetAddressType
_TmnxSseAddressType_Object = MibTableColumn
tmnxSseAddressType = _TmnxSseAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 1),
    _TmnxSseAddressType_Type()
)
tmnxSseAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSseAddressType.setStatus("current")


class _TmnxSseAddress_Type(InetAddress):
    """Custom type tmnxSseAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSseAddress_Type.__name__ = "InetAddress"
_TmnxSseAddress_Object = MibTableColumn
tmnxSseAddress = _TmnxSseAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 2),
    _TmnxSseAddress_Type()
)
tmnxSseAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSseAddress.setStatus("current")
_TmnxSseSnmpPort_Type = TmnxUdpPort
_TmnxSseSnmpPort_Object = MibTableColumn
tmnxSseSnmpPort = _TmnxSseSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 3),
    _TmnxSseSnmpPort_Type()
)
tmnxSseSnmpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSseSnmpPort.setStatus("current")
_TmnxSseRequestId_Type = Unsigned32
_TmnxSseRequestId_Object = MibTableColumn
tmnxSseRequestId = _TmnxSseRequestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 4),
    _TmnxSseRequestId_Type()
)
tmnxSseRequestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSseRequestId.setStatus("current")
_TmnxSseVersion_Type = SnmpMessageProcessingModel
_TmnxSseVersion_Object = MibTableColumn
tmnxSseVersion = _TmnxSseVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 5),
    _TmnxSseVersion_Type()
)
tmnxSseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseVersion.setStatus("current")
_TmnxSseSeverityLevel_Type = TmnxPerceivedSeverity
_TmnxSseSeverityLevel_Object = MibTableColumn
tmnxSseSeverityLevel = _TmnxSseSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 6),
    _TmnxSseSeverityLevel_Type()
)
tmnxSseSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseSeverityLevel.setStatus("current")
_TmnxSseModuleId_Type = Unsigned32
_TmnxSseModuleId_Object = MibTableColumn
tmnxSseModuleId = _TmnxSseModuleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 7),
    _TmnxSseModuleId_Type()
)
tmnxSseModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseModuleId.setStatus("current")
_TmnxSseModuleName_Type = TNamedItem
_TmnxSseModuleName_Object = MibTableColumn
tmnxSseModuleName = _TmnxSseModuleName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 8),
    _TmnxSseModuleName_Type()
)
tmnxSseModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseModuleName.setStatus("current")
_TmnxSseErrorCode_Type = Unsigned32
_TmnxSseErrorCode_Object = MibTableColumn
tmnxSseErrorCode = _TmnxSseErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 9),
    _TmnxSseErrorCode_Type()
)
tmnxSseErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseErrorCode.setStatus("current")


class _TmnxSseErrorName_Type(DisplayString):
    """Custom type tmnxSseErrorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxSseErrorName_Type.__name__ = "DisplayString"
_TmnxSseErrorName_Object = MibTableColumn
tmnxSseErrorName = _TmnxSseErrorName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 10),
    _TmnxSseErrorName_Type()
)
tmnxSseErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseErrorName.setStatus("current")


class _TmnxSseErrorMsg_Type(DisplayString):
    """Custom type tmnxSseErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxSseErrorMsg_Type.__name__ = "DisplayString"
_TmnxSseErrorMsg_Object = MibTableColumn
tmnxSseErrorMsg = _TmnxSseErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 11),
    _TmnxSseErrorMsg_Type()
)
tmnxSseErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseErrorMsg.setStatus("current")


class _TmnxSseExtraText_Type(OctetString):
    """Custom type tmnxSseExtraText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 320),
    )


_TmnxSseExtraText_Type.__name__ = "OctetString"
_TmnxSseExtraText_Object = MibTableColumn
tmnxSseExtraText = _TmnxSseExtraText_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 12),
    _TmnxSseExtraText_Type()
)
tmnxSseExtraText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseExtraText.setStatus("current")
_TmnxSseTimestamp_Type = TimeStamp
_TmnxSseTimestamp_Object = MibTableColumn
tmnxSseTimestamp = _TmnxSseTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 13),
    _TmnxSseTimestamp_Type()
)
tmnxSseTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseTimestamp.setStatus("current")
_TmnxSnmpTrapLogTable_Object = MibTable
tmnxSnmpTrapLogTable = _TmnxSnmpTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 17)
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapLogTable.setStatus("current")
_TmnxSnmpTrapLogEntry_Object = MibTableRow
tmnxSnmpTrapLogEntry = _TmnxSnmpTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 17, 1)
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapLogEntry.setStatus("current")


class _TmnxSnmpTrapLogDescription_Type(TItemDescription):
    """Custom type tmnxSnmpTrapLogDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSnmpTrapLogDescription_Type.__name__ = "TItemDescription"
_TmnxSnmpTrapLogDescription_Object = MibTableColumn
tmnxSnmpTrapLogDescription = _TmnxSnmpTrapLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 17, 1, 1),
    _TmnxSnmpTrapLogDescription_Type()
)
tmnxSnmpTrapLogDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSnmpTrapLogDescription.setStatus("current")
_TmnxSnmpTrapDestTable_Object = MibTable
tmnxSnmpTrapDestTable = _TmnxSnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18)
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapDestTable.setStatus("current")
_TmnxSnmpTrapDestEntry_Object = MibTableRow
tmnxSnmpTrapDestEntry = _TmnxSnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1)
)
tmnxSnmpTrapDestEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxStdIndex"),
    (1, "TIMETRA-LOG-MIB", "tmnxStdName"),
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapDestEntry.setStatus("current")
_TmnxStdIndex_Type = TmnxLogIdIndex
_TmnxStdIndex_Object = MibTableColumn
tmnxStdIndex = _TmnxStdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 1),
    _TmnxStdIndex_Type()
)
tmnxStdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStdIndex.setStatus("current")


class _TmnxStdName_Type(SnmpAdminString):
    """Custom type tmnxStdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 28),
    )


_TmnxStdName_Type.__name__ = "SnmpAdminString"
_TmnxStdName_Object = MibTableColumn
tmnxStdName = _TmnxStdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 2),
    _TmnxStdName_Type()
)
tmnxStdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStdName.setStatus("current")
_TmnxStdRowStatus_Type = RowStatus
_TmnxStdRowStatus_Object = MibTableColumn
tmnxStdRowStatus = _TmnxStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 3),
    _TmnxStdRowStatus_Type()
)
tmnxStdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdRowStatus.setStatus("current")
_TmnxStdRowLastChanged_Type = TimeStamp
_TmnxStdRowLastChanged_Object = MibTableColumn
tmnxStdRowLastChanged = _TmnxStdRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 4),
    _TmnxStdRowLastChanged_Type()
)
tmnxStdRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxStdRowLastChanged.setStatus("current")


class _TmnxStdDestAddrType_Type(InetAddressType):
    """Custom type tmnxStdDestAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxStdDestAddrType_Type.__name__ = "InetAddressType"
_TmnxStdDestAddrType_Object = MibTableColumn
tmnxStdDestAddrType = _TmnxStdDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 5),
    _TmnxStdDestAddrType_Type()
)
tmnxStdDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDestAddrType.setStatus("current")


class _TmnxStdDestAddr_Type(InetAddress):
    """Custom type tmnxStdDestAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxStdDestAddr_Type.__name__ = "InetAddress"
_TmnxStdDestAddr_Object = MibTableColumn
tmnxStdDestAddr = _TmnxStdDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 6),
    _TmnxStdDestAddr_Type()
)
tmnxStdDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDestAddr.setStatus("current")


class _TmnxStdDestPort_Type(TmnxUdpPort):
    """Custom type tmnxStdDestPort based on TmnxUdpPort"""
    defaultValue = 162


_TmnxStdDestPort_Type.__name__ = "TmnxUdpPort"
_TmnxStdDestPort_Object = MibTableColumn
tmnxStdDestPort = _TmnxStdDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 7),
    _TmnxStdDestPort_Type()
)
tmnxStdDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDestPort.setStatus("current")


class _TmnxStdDescription_Type(TItemDescription):
    """Custom type tmnxStdDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxStdDescription_Type.__name__ = "TItemDescription"
_TmnxStdDescription_Object = MibTableColumn
tmnxStdDescription = _TmnxStdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 8),
    _TmnxStdDescription_Type()
)
tmnxStdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDescription.setStatus("current")


class _TmnxStdVersion_Type(SnmpMessageProcessingModel):
    """Custom type tmnxStdVersion based on SnmpMessageProcessingModel"""
    defaultValue = 3


_TmnxStdVersion_Type.__name__ = "SnmpMessageProcessingModel"
_TmnxStdVersion_Object = MibTableColumn
tmnxStdVersion = _TmnxStdVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 9),
    _TmnxStdVersion_Type()
)
tmnxStdVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdVersion.setStatus("current")


class _TmnxStdNotifyCommunity_Type(OctetString):
    """Custom type tmnxStdNotifyCommunity based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TmnxStdNotifyCommunity_Type.__name__ = "OctetString"
_TmnxStdNotifyCommunity_Object = MibTableColumn
tmnxStdNotifyCommunity = _TmnxStdNotifyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 10),
    _TmnxStdNotifyCommunity_Type()
)
tmnxStdNotifyCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdNotifyCommunity.setStatus("current")


class _TmnxStdSecurityLevel_Type(SnmpSecurityLevel):
    """Custom type tmnxStdSecurityLevel based on SnmpSecurityLevel"""
    defaultValue = 1


_TmnxStdSecurityLevel_Type.__name__ = "SnmpSecurityLevel"
_TmnxStdSecurityLevel_Object = MibTableColumn
tmnxStdSecurityLevel = _TmnxStdSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 11),
    _TmnxStdSecurityLevel_Type()
)
tmnxStdSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdSecurityLevel.setStatus("current")


class _TmnxStdReplay_Type(TruthValue):
    """Custom type tmnxStdReplay based on TruthValue"""
    defaultValue = 2


_TmnxStdReplay_Type.__name__ = "TruthValue"
_TmnxStdReplay_Object = MibTableColumn
tmnxStdReplay = _TmnxStdReplay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 12),
    _TmnxStdReplay_Type()
)
tmnxStdReplay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdReplay.setStatus("current")
_TmnxStdReplayStart_Type = Unsigned32
_TmnxStdReplayStart_Object = MibTableColumn
tmnxStdReplayStart = _TmnxStdReplayStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 13),
    _TmnxStdReplayStart_Type()
)
tmnxStdReplayStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxStdReplayStart.setStatus("current")
_TmnxStdReplayLastTime_Type = TimeStamp
_TmnxStdReplayLastTime_Object = MibTableColumn
tmnxStdReplayLastTime = _TmnxStdReplayLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 14),
    _TmnxStdReplayLastTime_Type()
)
tmnxStdReplayLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxStdReplayLastTime.setStatus("current")


class _TmnxStdMaxTargets_Type(Unsigned32):
    """Custom type tmnxStdMaxTargets based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_TmnxStdMaxTargets_Type.__name__ = "Unsigned32"
_TmnxStdMaxTargets_Object = MibScalar
tmnxStdMaxTargets = _TmnxStdMaxTargets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 19),
    _TmnxStdMaxTargets_Type()
)
tmnxStdMaxTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxStdMaxTargets.setStatus("current")
if mibBuilder.loadTexts:
    tmnxStdMaxTargets.setUnits("trap-targets")
_TmnxLogApCustRecordTable_Object = MibTable
tmnxLogApCustRecordTable = _TmnxLogApCustRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20)
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordTable.setStatus("current")
_TmnxLogApCustRecordEntry_Object = MibTableRow
tmnxLogApCustRecordEntry = _TmnxLogApCustRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordEntry.setStatus("current")
_TmnxLogApCrLastChanged_Type = TimeStamp
_TmnxLogApCrLastChanged_Object = MibTableColumn
tmnxLogApCrLastChanged = _TmnxLogApCrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 1),
    _TmnxLogApCrLastChanged_Type()
)
tmnxLogApCrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApCrLastChanged.setStatus("current")


class _TmnxLogApCrSignChangeDelta_Type(Unsigned32):
    """Custom type tmnxLogApCrSignChangeDelta based on Unsigned32"""
    defaultValue = 0


_TmnxLogApCrSignChangeDelta_Type.__name__ = "Unsigned32"
_TmnxLogApCrSignChangeDelta_Object = MibTableColumn
tmnxLogApCrSignChangeDelta = _TmnxLogApCrSignChangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 2),
    _TmnxLogApCrSignChangeDelta_Type()
)
tmnxLogApCrSignChangeDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeDelta.setStatus("current")


class _TmnxLogApCrSignChangeQueue_Type(TQueueIdOrAll):
    """Custom type tmnxLogApCrSignChangeQueue based on TQueueIdOrAll"""
    defaultValue = 0


_TmnxLogApCrSignChangeQueue_Type.__name__ = "TQueueIdOrAll"
_TmnxLogApCrSignChangeQueue_Object = MibTableColumn
tmnxLogApCrSignChangeQueue = _TmnxLogApCrSignChangeQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 3),
    _TmnxLogApCrSignChangeQueue_Type()
)
tmnxLogApCrSignChangeQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeQueue.setStatus("current")


class _TmnxLogApCrSignChangeOCntr_Type(THsmdaCounterIdOrZeroOrAll):
    """Custom type tmnxLogApCrSignChangeOCntr based on THsmdaCounterIdOrZeroOrAll"""
    defaultValue = 0


_TmnxLogApCrSignChangeOCntr_Type.__name__ = "THsmdaCounterIdOrZeroOrAll"
_TmnxLogApCrSignChangeOCntr_Object = MibTableColumn
tmnxLogApCrSignChangeOCntr = _TmnxLogApCrSignChangeOCntr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 4),
    _TmnxLogApCrSignChangeOCntr_Type()
)
tmnxLogApCrSignChangeOCntr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeOCntr.setStatus("current")


class _TmnxLogApCrSignChangeQICounters_Type(TmnxAccPlcyQICounters):
    """Custom type tmnxLogApCrSignChangeQICounters based on TmnxAccPlcyQICounters"""
    defaultHexValue = "00"


_TmnxLogApCrSignChangeQICounters_Type.__name__ = "TmnxAccPlcyQICounters"
_TmnxLogApCrSignChangeQICounters_Object = MibTableColumn
tmnxLogApCrSignChangeQICounters = _TmnxLogApCrSignChangeQICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 5),
    _TmnxLogApCrSignChangeQICounters_Type()
)
tmnxLogApCrSignChangeQICounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeQICounters.setStatus("current")


class _TmnxLogApCrSignChangeQECounters_Type(TmnxAccPlcyQECounters):
    """Custom type tmnxLogApCrSignChangeQECounters based on TmnxAccPlcyQECounters"""
    defaultHexValue = "00"


_TmnxLogApCrSignChangeQECounters_Type.__name__ = "TmnxAccPlcyQECounters"
_TmnxLogApCrSignChangeQECounters_Object = MibTableColumn
tmnxLogApCrSignChangeQECounters = _TmnxLogApCrSignChangeQECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 6),
    _TmnxLogApCrSignChangeQECounters_Type()
)
tmnxLogApCrSignChangeQECounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeQECounters.setStatus("current")


class _TmnxLogApCrSignChangeOICounters_Type(TmnxAccPlcyOICounters):
    """Custom type tmnxLogApCrSignChangeOICounters based on TmnxAccPlcyOICounters"""
    defaultHexValue = "00"


_TmnxLogApCrSignChangeOICounters_Type.__name__ = "TmnxAccPlcyOICounters"
_TmnxLogApCrSignChangeOICounters_Object = MibTableColumn
tmnxLogApCrSignChangeOICounters = _TmnxLogApCrSignChangeOICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 7),
    _TmnxLogApCrSignChangeOICounters_Type()
)
tmnxLogApCrSignChangeOICounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeOICounters.setStatus("current")


class _TmnxLogApCrSignChangeOECounters_Type(TmnxAccPlcyOECounters):
    """Custom type tmnxLogApCrSignChangeOECounters based on TmnxAccPlcyOECounters"""
    defaultHexValue = "00"


_TmnxLogApCrSignChangeOECounters_Type.__name__ = "TmnxAccPlcyOECounters"
_TmnxLogApCrSignChangeOECounters_Object = MibTableColumn
tmnxLogApCrSignChangeOECounters = _TmnxLogApCrSignChangeOECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 8),
    _TmnxLogApCrSignChangeOECounters_Type()
)
tmnxLogApCrSignChangeOECounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeOECounters.setStatus("current")


class _TmnxLogApCrSignChangeAACounters_Type(TmnxAccPlcyAACounters):
    """Custom type tmnxLogApCrSignChangeAACounters based on TmnxAccPlcyAACounters"""
    defaultHexValue = "00"


_TmnxLogApCrSignChangeAACounters_Type.__name__ = "TmnxAccPlcyAACounters"
_TmnxLogApCrSignChangeAACounters_Object = MibTableColumn
tmnxLogApCrSignChangeAACounters = _TmnxLogApCrSignChangeAACounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 9),
    _TmnxLogApCrSignChangeAACounters_Type()
)
tmnxLogApCrSignChangeAACounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeAACounters.setStatus("current")


class _TmnxLogApCrAACounters_Type(TmnxAccPlcyAACounters):
    """Custom type tmnxLogApCrAACounters based on TmnxAccPlcyAACounters"""
    defaultHexValue = "00"


_TmnxLogApCrAACounters_Type.__name__ = "TmnxAccPlcyAACounters"
_TmnxLogApCrAACounters_Object = MibTableColumn
tmnxLogApCrAACounters = _TmnxLogApCrAACounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 10),
    _TmnxLogApCrAACounters_Type()
)
tmnxLogApCrAACounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrAACounters.setStatus("current")


class _TmnxLogApCrAASubAttributes_Type(TmnxAccPlcyAASubAttributes):
    """Custom type tmnxLogApCrAASubAttributes based on TmnxAccPlcyAASubAttributes"""
    defaultHexValue = "00"


_TmnxLogApCrAASubAttributes_Type.__name__ = "TmnxAccPlcyAASubAttributes"
_TmnxLogApCrAASubAttributes_Object = MibTableColumn
tmnxLogApCrAASubAttributes = _TmnxLogApCrAASubAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 11),
    _TmnxLogApCrAASubAttributes_Type()
)
tmnxLogApCrAASubAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrAASubAttributes.setStatus("current")
_TmnxLogApCustRecordQueueTable_Object = MibTable
tmnxLogApCustRecordQueueTable = _TmnxLogApCustRecordQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21)
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordQueueTable.setStatus("current")
_TmnxLogApCustRecordQueueEntry_Object = MibTableRow
tmnxLogApCustRecordQueueEntry = _TmnxLogApCustRecordQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1)
)
tmnxLogApCustRecordQueueEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogApPolicyId"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogApCrQueueId"),
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordQueueEntry.setStatus("current")


class _TmnxLogApCrQueueId_Type(TQueueId):
    """Custom type tmnxLogApCrQueueId based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxLogApCrQueueId_Type.__name__ = "TQueueId"
_TmnxLogApCrQueueId_Object = MibTableColumn
tmnxLogApCrQueueId = _TmnxLogApCrQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 1),
    _TmnxLogApCrQueueId_Type()
)
tmnxLogApCrQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueId.setStatus("current")
_TmnxLogApCrQueueRowStatus_Type = RowStatus
_TmnxLogApCrQueueRowStatus_Object = MibTableColumn
tmnxLogApCrQueueRowStatus = _TmnxLogApCrQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 2),
    _TmnxLogApCrQueueRowStatus_Type()
)
tmnxLogApCrQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueRowStatus.setStatus("current")
_TmnxLogApCrQueueLastChanged_Type = TimeStamp
_TmnxLogApCrQueueLastChanged_Object = MibTableColumn
tmnxLogApCrQueueLastChanged = _TmnxLogApCrQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 3),
    _TmnxLogApCrQueueLastChanged_Type()
)
tmnxLogApCrQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueLastChanged.setStatus("current")


class _TmnxLogApCrQueueICounters_Type(TmnxAccPlcyQICounters):
    """Custom type tmnxLogApCrQueueICounters based on TmnxAccPlcyQICounters"""
    defaultHexValue = "00"


_TmnxLogApCrQueueICounters_Type.__name__ = "TmnxAccPlcyQICounters"
_TmnxLogApCrQueueICounters_Object = MibTableColumn
tmnxLogApCrQueueICounters = _TmnxLogApCrQueueICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 4),
    _TmnxLogApCrQueueICounters_Type()
)
tmnxLogApCrQueueICounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueICounters.setStatus("current")


class _TmnxLogApCrQueueECounters_Type(TmnxAccPlcyQECounters):
    """Custom type tmnxLogApCrQueueECounters based on TmnxAccPlcyQECounters"""
    defaultHexValue = "00"


_TmnxLogApCrQueueECounters_Type.__name__ = "TmnxAccPlcyQECounters"
_TmnxLogApCrQueueECounters_Object = MibTableColumn
tmnxLogApCrQueueECounters = _TmnxLogApCrQueueECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 5),
    _TmnxLogApCrQueueECounters_Type()
)
tmnxLogApCrQueueECounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueECounters.setStatus("current")
_TmnxLogApCrOverrideCntrTable_Object = MibTable
tmnxLogApCrOverrideCntrTable = _TmnxLogApCrOverrideCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22)
)
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrTable.setStatus("current")
_TmnxLogApCrOverrideCntrEntry_Object = MibTableRow
tmnxLogApCrOverrideCntrEntry = _TmnxLogApCrOverrideCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1)
)
tmnxLogApCrOverrideCntrEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogApPolicyId"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrId"),
)
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrEntry.setStatus("current")


class _TmnxLogApCrOverrideCntrId_Type(THsmdaCounterIdOrZero):
    """Custom type tmnxLogApCrOverrideCntrId based on THsmdaCounterIdOrZero"""
    subtypeSpec = THsmdaCounterIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxLogApCrOverrideCntrId_Type.__name__ = "THsmdaCounterIdOrZero"
_TmnxLogApCrOverrideCntrId_Object = MibTableColumn
tmnxLogApCrOverrideCntrId = _TmnxLogApCrOverrideCntrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 1),
    _TmnxLogApCrOverrideCntrId_Type()
)
tmnxLogApCrOverrideCntrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrId.setStatus("current")
_TmnxLogApCrOverrideCntrRowStatus_Type = RowStatus
_TmnxLogApCrOverrideCntrRowStatus_Object = MibTableColumn
tmnxLogApCrOverrideCntrRowStatus = _TmnxLogApCrOverrideCntrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 2),
    _TmnxLogApCrOverrideCntrRowStatus_Type()
)
tmnxLogApCrOverrideCntrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrRowStatus.setStatus("current")
_TmnxLogApCrOverrideCntrLastChngd_Type = TimeStamp
_TmnxLogApCrOverrideCntrLastChngd_Object = MibTableColumn
tmnxLogApCrOverrideCntrLastChngd = _TmnxLogApCrOverrideCntrLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 3),
    _TmnxLogApCrOverrideCntrLastChngd_Type()
)
tmnxLogApCrOverrideCntrLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrLastChngd.setStatus("current")


class _TmnxLogApCrOverrideCntrICounters_Type(TmnxAccPlcyOICounters):
    """Custom type tmnxLogApCrOverrideCntrICounters based on TmnxAccPlcyOICounters"""
    defaultHexValue = "00"


_TmnxLogApCrOverrideCntrICounters_Type.__name__ = "TmnxAccPlcyOICounters"
_TmnxLogApCrOverrideCntrICounters_Object = MibTableColumn
tmnxLogApCrOverrideCntrICounters = _TmnxLogApCrOverrideCntrICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 4),
    _TmnxLogApCrOverrideCntrICounters_Type()
)
tmnxLogApCrOverrideCntrICounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrICounters.setStatus("current")


class _TmnxLogApCrOverrideCntrECounters_Type(TmnxAccPlcyOECounters):
    """Custom type tmnxLogApCrOverrideCntrECounters based on TmnxAccPlcyOECounters"""
    defaultHexValue = "00"


_TmnxLogApCrOverrideCntrECounters_Type.__name__ = "TmnxAccPlcyOECounters"
_TmnxLogApCrOverrideCntrECounters_Object = MibTableColumn
tmnxLogApCrOverrideCntrECounters = _TmnxLogApCrOverrideCntrECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 5),
    _TmnxLogApCrOverrideCntrECounters_Type()
)
tmnxLogApCrOverrideCntrECounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrECounters.setStatus("current")


class _TmnxEventPrimaryRoutePref_Type(Integer32):
    """Custom type tmnxEventPrimaryRoutePref based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outband", 2))
    )


_TmnxEventPrimaryRoutePref_Type.__name__ = "Integer32"
_TmnxEventPrimaryRoutePref_Object = MibScalar
tmnxEventPrimaryRoutePref = _TmnxEventPrimaryRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 23),
    _TmnxEventPrimaryRoutePref_Type()
)
tmnxEventPrimaryRoutePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventPrimaryRoutePref.setStatus("current")


class _TmnxEventSecondaryRoutePref_Type(Integer32):
    """Custom type tmnxEventSecondaryRoutePref based on Integer32"""
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
        *(("inband", 1),
          ("outband", 2),
          ("none", 3))
    )


_TmnxEventSecondaryRoutePref_Type.__name__ = "Integer32"
_TmnxEventSecondaryRoutePref_Object = MibScalar
tmnxEventSecondaryRoutePref = _TmnxEventSecondaryRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 24),
    _TmnxEventSecondaryRoutePref_Type()
)
tmnxEventSecondaryRoutePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSecondaryRoutePref.setStatus("current")


class _TmnxLogConfigEventsDamped_Type(TruthValue):
    """Custom type tmnxLogConfigEventsDamped based on TruthValue"""
    defaultValue = 1


_TmnxLogConfigEventsDamped_Type.__name__ = "TruthValue"
_TmnxLogConfigEventsDamped_Object = MibScalar
tmnxLogConfigEventsDamped = _TmnxLogConfigEventsDamped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 25),
    _TmnxLogConfigEventsDamped_Type()
)
tmnxLogConfigEventsDamped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogConfigEventsDamped.setStatus("current")
_TmnxLogEventHistoryObjs_ObjectIdentity = ObjectIdentity
tmnxLogEventHistoryObjs = _TmnxLogEventHistoryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26)
)
_TmnxLogEventHistGeneralObjs_ObjectIdentity = ObjectIdentity
tmnxLogEventHistGeneralObjs = _TmnxLogEventHistGeneralObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 1)
)
_TmnxLogExRbkOpTblLastChange_Type = TimeStamp
_TmnxLogExRbkOpTblLastChange_Object = MibScalar
tmnxLogExRbkOpTblLastChange = _TmnxLogExRbkOpTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 1, 1),
    _TmnxLogExRbkOpTblLastChange_Type()
)
tmnxLogExRbkOpTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpTblLastChange.setStatus("current")


class _TmnxLogExRbkOpMaxEntries_Type(Unsigned32):
    """Custom type tmnxLogExRbkOpMaxEntries based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxLogExRbkOpMaxEntries_Type.__name__ = "Unsigned32"
_TmnxLogExRbkOpMaxEntries_Object = MibScalar
tmnxLogExRbkOpMaxEntries = _TmnxLogExRbkOpMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 1, 2),
    _TmnxLogExRbkOpMaxEntries_Type()
)
tmnxLogExRbkOpMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpMaxEntries.setStatus("current")
_TmnxLogExecRollbackOpTable_Object = MibTable
tmnxLogExecRollbackOpTable = _TmnxLogExecRollbackOpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3)
)
if mibBuilder.loadTexts:
    tmnxLogExecRollbackOpTable.setStatus("current")
_TmnxLogExecRollbackOpEntry_Object = MibTableRow
tmnxLogExecRollbackOpEntry = _TmnxLogExecRollbackOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1)
)
tmnxLogExecRollbackOpEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogExRbkOpIndex"),
)
if mibBuilder.loadTexts:
    tmnxLogExecRollbackOpEntry.setStatus("current")
_TmnxLogExRbkOpIndex_Type = Unsigned32
_TmnxLogExRbkOpIndex_Object = MibTableColumn
tmnxLogExRbkOpIndex = _TmnxLogExRbkOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 1),
    _TmnxLogExRbkOpIndex_Type()
)
tmnxLogExRbkOpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpIndex.setStatus("current")
_TmnxLogExRbkOpLastChanged_Type = TimeStamp
_TmnxLogExRbkOpLastChanged_Object = MibTableColumn
tmnxLogExRbkOpLastChanged = _TmnxLogExRbkOpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 2),
    _TmnxLogExRbkOpLastChanged_Type()
)
tmnxLogExRbkOpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpLastChanged.setStatus("current")


class _TmnxLogExRbkOpType_Type(Integer32):
    """Custom type tmnxLogExRbkOpType based on Integer32"""
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
          ("exec", 1),
          ("rollback", 2))
    )


_TmnxLogExRbkOpType_Type.__name__ = "Integer32"
_TmnxLogExRbkOpType_Object = MibTableColumn
tmnxLogExRbkOpType = _TmnxLogExRbkOpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 3),
    _TmnxLogExRbkOpType_Type()
)
tmnxLogExRbkOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpType.setStatus("current")


class _TmnxLogExRbkOpStatus_Type(Integer32):
    """Custom type tmnxLogExRbkOpStatus based on Integer32"""
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
        *(("unknown", 0),
          ("inProgress", 1),
          ("success", 2),
          ("failed", 3))
    )


_TmnxLogExRbkOpStatus_Type.__name__ = "Integer32"
_TmnxLogExRbkOpStatus_Object = MibTableColumn
tmnxLogExRbkOpStatus = _TmnxLogExRbkOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 4),
    _TmnxLogExRbkOpStatus_Type()
)
tmnxLogExRbkOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpStatus.setStatus("current")
_TmnxLogExRbkOpBegin_Type = TimeStamp
_TmnxLogExRbkOpBegin_Object = MibTableColumn
tmnxLogExRbkOpBegin = _TmnxLogExRbkOpBegin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 5),
    _TmnxLogExRbkOpBegin_Type()
)
tmnxLogExRbkOpBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpBegin.setStatus("current")
_TmnxLogExRbkOpEnd_Type = TimeStamp
_TmnxLogExRbkOpEnd_Object = MibTableColumn
tmnxLogExRbkOpEnd = _TmnxLogExRbkOpEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 6),
    _TmnxLogExRbkOpEnd_Type()
)
tmnxLogExRbkOpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpEnd.setStatus("current")
_TmnxLogExRbkOpFile_Type = DisplayString
_TmnxLogExRbkOpFile_Object = MibTableColumn
tmnxLogExRbkOpFile = _TmnxLogExRbkOpFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 7),
    _TmnxLogExRbkOpFile_Type()
)
tmnxLogExRbkOpFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpFile.setStatus("current")
_TmnxLogExRbkOpUser_Type = TNamedItem
_TmnxLogExRbkOpUser_Object = MibTableColumn
tmnxLogExRbkOpUser = _TmnxLogExRbkOpUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 8),
    _TmnxLogExRbkOpUser_Type()
)
tmnxLogExRbkOpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpUser.setStatus("current")
_TmnxLogExRbkOpNumEvents_Type = Unsigned32
_TmnxLogExRbkOpNumEvents_Object = MibTableColumn
tmnxLogExRbkOpNumEvents = _TmnxLogExRbkOpNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 9),
    _TmnxLogExRbkOpNumEvents_Type()
)
tmnxLogExRbkOpNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpNumEvents.setStatus("current")
_TmnxLogExecRollbackEventTable_Object = MibTable
tmnxLogExecRollbackEventTable = _TmnxLogExecRollbackEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 4)
)
if mibBuilder.loadTexts:
    tmnxLogExecRollbackEventTable.setStatus("current")
_TmnxLogExecRollbackEventEntry_Object = MibTableRow
tmnxLogExecRollbackEventEntry = _TmnxLogExecRollbackEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 4, 1)
)
tmnxLogExecRollbackEventEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogExRbkOpIndex"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogExRbkEventIndex"),
)
if mibBuilder.loadTexts:
    tmnxLogExecRollbackEventEntry.setStatus("current")
_TmnxLogExRbkEventIndex_Type = Unsigned32
_TmnxLogExRbkEventIndex_Object = MibTableColumn
tmnxLogExRbkEventIndex = _TmnxLogExRbkEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 4, 1, 1),
    _TmnxLogExRbkEventIndex_Type()
)
tmnxLogExRbkEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogExRbkEventIndex.setStatus("current")
_TmnxLogExRbkEventOID_Type = ObjectIdentifier
_TmnxLogExRbkEventOID_Object = MibTableColumn
tmnxLogExRbkEventOID = _TmnxLogExRbkEventOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 4, 1, 2),
    _TmnxLogExRbkEventOID_Type()
)
tmnxLogExRbkEventOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkEventOID.setStatus("current")
_TmnxLogExRbkNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxLogExRbkNotifyObjects = _TmnxLogExRbkNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 5)
)
_TmnxLogExecRollbackOpIndex_Type = Unsigned32
_TmnxLogExecRollbackOpIndex_Object = MibScalar
tmnxLogExecRollbackOpIndex = _TmnxLogExecRollbackOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 5, 1),
    _TmnxLogExecRollbackOpIndex_Type()
)
tmnxLogExecRollbackOpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogExecRollbackOpIndex.setStatus("current")


class _TmnxLogColdStartWaitTime_Type(Unsigned32):
    """Custom type tmnxLogColdStartWaitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxLogColdStartWaitTime_Type.__name__ = "Unsigned32"
_TmnxLogColdStartWaitTime_Object = MibScalar
tmnxLogColdStartWaitTime = _TmnxLogColdStartWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 27),
    _TmnxLogColdStartWaitTime_Type()
)
tmnxLogColdStartWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogColdStartWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogColdStartWaitTime.setUnits("seconds")


class _TmnxLogRouteRecoveryWaitTime_Type(Unsigned32):
    """Custom type tmnxLogRouteRecoveryWaitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxLogRouteRecoveryWaitTime_Type.__name__ = "Unsigned32"
_TmnxLogRouteRecoveryWaitTime_Object = MibScalar
tmnxLogRouteRecoveryWaitTime = _TmnxLogRouteRecoveryWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 28),
    _TmnxLogRouteRecoveryWaitTime_Type()
)
tmnxLogRouteRecoveryWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogRouteRecoveryWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogRouteRecoveryWaitTime.setUnits("seconds")
_TmnxLogNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxLogNotifyPrefix = _TmnxLogNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12)
)
_TmnxLogNotifications_ObjectIdentity = ObjectIdentity
tmnxLogNotifications = _TmnxLogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0)
)
snmpNotifyEntry.registerAugmentions(
    ("TIMETRA-LOG-MIB",
     "tmnxSnmpTrapLogEntry")
)
tmnxSnmpTrapLogEntry.setIndexNames(*snmpNotifyEntry.getIndexNames())
tmnxLogApEntry.registerAugmentions(
    ("TIMETRA-LOG-MIB",
     "tmnxLogApCustRecordEntry")
)
tmnxLogApCustRecordEntry.setIndexNames(*tmnxLogApEntry.getIndexNames())

# Managed Objects groups

tmnxLogGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 1)
)
tmnxLogGlobalGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogMaxLogs")
)
if mibBuilder.loadTexts:
    tmnxLogGlobalGroup.setStatus("current")

tmnxLogAccountingPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 3)
)
tmnxLogAccountingPolicyGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogApRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApStorageType"),
        ("TIMETRA-LOG-MIB", "tmnxLogApAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApInterval"),
        ("TIMETRA-LOG-MIB", "tmnxLogApDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogApDefault"),
        ("TIMETRA-LOG-MIB", "tmnxLogApRecord"),
        ("TIMETRA-LOG-MIB", "tmnxLogApToFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogApPortType"))
)
if mibBuilder.loadTexts:
    tmnxLogAccountingPolicyGroup.setStatus("current")

tmnxLogFileIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 4)
)
tmnxLogFileIdGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdStorageType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRolloverTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRetainTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdPathName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"))
)
if mibBuilder.loadTexts:
    tmnxLogFileIdGroup.setStatus("current")

tmnxLogSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 5)
)
tmnxLogSyslogGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSyslogTargetRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetDescription"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetAddress"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetUdpPort"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetFacility"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetMessagePrefix"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetMessagesDropped"))
)
if mibBuilder.loadTexts:
    tmnxLogSyslogGroup.setStatus("obsolete")

tmnxSnmpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 6)
)
tmnxSnmpTrapGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxStgRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxStgDescription"),
        ("TIMETRA-LOG-MIB", "tmnxStgVersion"),
        ("TIMETRA-LOG-MIB", "tmnxStgNotifyCommunity"),
        ("TIMETRA-LOG-MIB", "tmnxStgSecurityLevel"))
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapGroup.setStatus("obsolete")

tmnxLogEventsR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 10)
)
tmnxLogEventsR2r1Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEventAppName"),
        ("TIMETRA-LOG-MIB", "tmnxEventName"),
        ("TIMETRA-LOG-MIB", "tmnxEventSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxEventControl"),
        ("TIMETRA-LOG-MIB", "tmnxEventCounter"),
        ("TIMETRA-LOG-MIB", "tmnxEventDropCount"),
        ("TIMETRA-LOG-MIB", "tmnxEventReset"),
        ("TIMETRA-LOG-MIB", "tmnxEventTest"))
)
if mibBuilder.loadTexts:
    tmnxLogEventsR2r1Group.setStatus("obsolete")

tmnxLogNotifyObjsR3r0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 13)
)
tmnxLogNotifyObjsR3r0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"))
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsR3r0Group.setStatus("obsolete")

tmnxLogV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 15)
)
tmnxLogV4v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogIdRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdStorageType"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdFilterId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdSource"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDestination"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdSyslogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdMaxMemorySize"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdConsoleSession"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdForwarded"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDropped"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdTimeFormat"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterDefaultAction"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterInUse"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsAction"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsApplication"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsApplOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNumber"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNumberOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSeverityOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubject"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubjectOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubjectRegexp"))
)
if mibBuilder.loadTexts:
    tmnxLogV4v0Group.setStatus("obsolete")

tmnxSnmpSetErrsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 16)
)
tmnxSnmpSetErrsGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsMax"),
        ("TIMETRA-LOG-MIB", "tmnxSseVersion"),
        ("TIMETRA-LOG-MIB", "tmnxSseSeverityLevel"),
        ("TIMETRA-LOG-MIB", "tmnxSseModuleId"),
        ("TIMETRA-LOG-MIB", "tmnxSseModuleName"),
        ("TIMETRA-LOG-MIB", "tmnxSseErrorCode"),
        ("TIMETRA-LOG-MIB", "tmnxSseErrorName"),
        ("TIMETRA-LOG-MIB", "tmnxSseErrorMsg"),
        ("TIMETRA-LOG-MIB", "tmnxSseExtraText"),
        ("TIMETRA-LOG-MIB", "tmnxSseTimestamp"))
)
if mibBuilder.loadTexts:
    tmnxSnmpSetErrsGroup.setStatus("current")

tmnxLogEventsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 17)
)
tmnxLogEventsV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEventAppName"),
        ("TIMETRA-LOG-MIB", "tmnxEventName"),
        ("TIMETRA-LOG-MIB", "tmnxEventSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxEventControl"),
        ("TIMETRA-LOG-MIB", "tmnxEventCounter"),
        ("TIMETRA-LOG-MIB", "tmnxEventDropCount"),
        ("TIMETRA-LOG-MIB", "tmnxEventReset"),
        ("TIMETRA-LOG-MIB", "tmnxEventThrottle"),
        ("TIMETRA-LOG-MIB", "tmnxEventTest"),
        ("TIMETRA-LOG-MIB", "tmnxEventThrottleLimit"),
        ("TIMETRA-LOG-MIB", "tmnxEventThrottleInterval"))
)
if mibBuilder.loadTexts:
    tmnxLogEventsV5v0Group.setStatus("current")

tmnxLogNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 18)
)
tmnxLogNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetId"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblemDescr"))
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV5v0Group.setStatus("obsolete")

tmnxLogSyslogV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 20)
)
tmnxLogSyslogV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSyslogTargetRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetDescription"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetUdpPort"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetFacility"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetMessagePrefix"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetMessagesDropped"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetAddrType"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetAddr"))
)
if mibBuilder.loadTexts:
    tmnxLogSyslogV5v0Group.setStatus("current")

tmnxSnmpTrapV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 21)
)
tmnxSnmpTrapV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSnmpTrapLogDescription"),
        ("TIMETRA-LOG-MIB", "tmnxStdRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxStdRowLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxStdDestAddrType"),
        ("TIMETRA-LOG-MIB", "tmnxStdDestAddr"),
        ("TIMETRA-LOG-MIB", "tmnxStdDestPort"),
        ("TIMETRA-LOG-MIB", "tmnxStdDescription"),
        ("TIMETRA-LOG-MIB", "tmnxStdVersion"),
        ("TIMETRA-LOG-MIB", "tmnxStdNotifyCommunity"),
        ("TIMETRA-LOG-MIB", "tmnxStdSecurityLevel"),
        ("TIMETRA-LOG-MIB", "tmnxStdMaxTargets"))
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapV5v0Group.setStatus("current")

tmnxLogV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 22)
)
tmnxLogV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogIdRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdStorageType"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdFilterId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdSource"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDestination"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdSyslogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdMaxMemorySize"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdConsoleSession"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdForwarded"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDropped"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdTimeFormat"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterDefaultAction"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterInUse"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsAction"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsApplication"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsApplOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNumber"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNumberOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSeverityOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubject"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubjectOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubjectRegexp"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRouter"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRouterOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRouterRegexp"))
)
if mibBuilder.loadTexts:
    tmnxLogV5v0Group.setStatus("current")

tmnxLogObsoleteObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 23)
)
tmnxLogObsoleteObjsV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSyslogTargetAddress"),
        ("TIMETRA-LOG-MIB", "tmnxStgRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxStgDescription"),
        ("TIMETRA-LOG-MIB", "tmnxStgVersion"),
        ("TIMETRA-LOG-MIB", "tmnxStgNotifyCommunity"),
        ("TIMETRA-LOG-MIB", "tmnxStgSecurityLevel"))
)
if mibBuilder.loadTexts:
    tmnxLogObsoleteObjsV5v0Group.setStatus("current")

tmnxLogNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 24)
)
tmnxLogNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetId"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblemDescr"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotifyApInterval"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStartEvent"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayEndEvent"))
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV6v0Group.setStatus("obsolete")

tmnxSnmpTrapDestV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 26)
)
tmnxSnmpTrapDestV6v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxStdReplay"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStart"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayLastTime"))
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapDestV6v0Group.setStatus("current")

tmnxLogAccountingPolicyV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 27)
)
tmnxLogAccountingPolicyV6v1Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApDefaultInterval")
)
if mibBuilder.loadTexts:
    tmnxLogAccountingPolicyV6v1Group.setStatus("current")

tmnxLogAccountingPolicyCRV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 28)
)
tmnxLogAccountingPolicyCRV7v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogApCrLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeDelta"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeQueue"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeOCntr"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeQICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeQECounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeOICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeOECounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeAACounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrAACounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrQueueRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrQueueLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrQueueICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrQueueECounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrLastChngd"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrECounters"))
)
if mibBuilder.loadTexts:
    tmnxLogAccountingPolicyCRV7v0Group.setStatus("current")

tmnxLogRoutePreferenceV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 29)
)
tmnxLogRoutePreferenceV7v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEventPrimaryRoutePref"),
        ("TIMETRA-LOG-MIB", "tmnxEventSecondaryRoutePref"))
)
if mibBuilder.loadTexts:
    tmnxLogRoutePreferenceV7v0Group.setStatus("current")

tmnxLogNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 30)
)
tmnxLogNotifyObjsV8v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorSubject"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetId"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblemDescr"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotifyApInterval"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStartEvent"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayEndEvent"))
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV8v0Group.setStatus("current")

tmnxLogEventDampedV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 32)
)
tmnxLogEventDampedV8v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogConfigEventsDamped")
)
if mibBuilder.loadTexts:
    tmnxLogEventDampedV8v0Group.setStatus("current")

tmnxLogApV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 33)
)
tmnxLogApV9v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogApDataLossCount"),
        ("TIMETRA-LOG-MIB", "tmnxLogApLastDataLossTimeStamp"))
)
if mibBuilder.loadTexts:
    tmnxLogApV9v0Group.setStatus("current")

tmnxLogExRbkOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 34)
)
tmnxLogExRbkOpGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogExRbkOpTblLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpMaxEntries"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpType"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpBegin"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpEnd"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpFile"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpUser"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpNumEvents"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkEventOID"))
)
if mibBuilder.loadTexts:
    tmnxLogExRbkOpGroup.setStatus("current")

tmnxLogNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 35)
)
tmnxLogNotifyObjsV10v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex")
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV10v0Group.setStatus("current")

tmnxLogApExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 36)
)
tmnxLogApExtGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApToFileType")
)
if mibBuilder.loadTexts:
    tmnxLogApExtGroup.setStatus("current")

tmnxLogAppRouteNotifV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 37)
)
tmnxLogAppRouteNotifV10v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogColdStartWaitTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogRouteRecoveryWaitTime"))
)
if mibBuilder.loadTexts:
    tmnxLogAppRouteNotifV10v0Group.setStatus("current")

tmnxLogApV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 38)
)
tmnxLogApV11v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApIncludeSystemInfo")
)
if mibBuilder.loadTexts:
    tmnxLogApV11v0Group.setStatus("current")

tmnxLogEventsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 40)
)
tmnxLogEventsV11v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEventSpecThrottle"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleLimit"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleIntval"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleDef"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleLimitDef"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleIntvalDef"))
)
if mibBuilder.loadTexts:
    tmnxLogEventsV11v0Group.setStatus("current")

tmnxLogApCrV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 41)
)
tmnxLogApCrV11v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApCrAASubAttributes")
)
if mibBuilder.loadTexts:
    tmnxLogApCrV11v0Group.setStatus("current")


# Notification objects

tmnxLogSpaceContention = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 1)
)
tmnxLogSpaceContention.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdRolloverTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRetainTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"))
)
if mibBuilder.loadTexts:
    tmnxLogSpaceContention.setStatus(
        "current"
    )

tmnxLogAdminLocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 2)
)
tmnxLogAdminLocFailed.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"))
)
if mibBuilder.loadTexts:
    tmnxLogAdminLocFailed.setStatus(
        "current"
    )

tmnxLogBackupLocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 3)
)
tmnxLogBackupLocFailed.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"))
)
if mibBuilder.loadTexts:
    tmnxLogBackupLocFailed.setStatus(
        "current"
    )

tmnxLogFileRollover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 4)
)
tmnxLogFileRollover.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdRolloverTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRetainTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdPathName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdCreateTime"))
)
if mibBuilder.loadTexts:
    tmnxLogFileRollover.setStatus(
        "current"
    )

tmnxLogFileDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 5)
)
tmnxLogFileDeleted.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"))
)
if mibBuilder.loadTexts:
    tmnxLogFileDeleted.setStatus(
        "current"
    )

tmnxTestEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 6)
)
tmnxTestEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    tmnxTestEvent.setStatus(
        "current"
    )

tmnxLogTraceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 7)
)
tmnxLogTraceError.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorSubject"))
)
if mibBuilder.loadTexts:
    tmnxLogTraceError.setStatus(
        "current"
    )

tmnxLogEventThrottled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 8)
)
tmnxLogEventThrottled.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"))
)
if mibBuilder.loadTexts:
    tmnxLogEventThrottled.setStatus(
        "current"
    )

tmnxSysLogTargetProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 9)
)
tmnxSysLogTargetProblem.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSysLogTargetId"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblemDescr"))
)
if mibBuilder.loadTexts:
    tmnxSysLogTargetProblem.setStatus(
        "current"
    )

tmnxLogAccountingDataLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 10)
)
tmnxLogAccountingDataLoss.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdRolloverTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRetainTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotifyApInterval"))
)
if mibBuilder.loadTexts:
    tmnxLogAccountingDataLoss.setStatus(
        "current"
    )

tmnxStdEventsReplayed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 11)
)
tmnxStdEventsReplayed.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxStdDestAddrType"),
        ("TIMETRA-LOG-MIB", "tmnxStdDestAddr"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStartEvent"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayEndEvent"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStart"))
)
if mibBuilder.loadTexts:
    tmnxStdEventsReplayed.setStatus(
        "current"
    )

tmnxLogEventOverrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 12)
)
tmnxLogEventOverrun.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"))
)
if mibBuilder.loadTexts:
    tmnxLogEventOverrun.setStatus(
        "current"
    )


# Notifications groups

tmnxLogNotificationR3r0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 14)
)
tmnxLogNotificationR3r0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogSpaceContention"),
        ("TIMETRA-LOG-MIB", "tmnxLogAdminLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogBackupLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileRollover"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeleted"),
        ("TIMETRA-LOG-MIB", "tmnxTestEvent"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceError"))
)
if mibBuilder.loadTexts:
    tmnxLogNotificationR3r0Group.setStatus(
        "obsolete"
    )

tmnxLogNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 19)
)
tmnxLogNotificationV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogSpaceContention"),
        ("TIMETRA-LOG-MIB", "tmnxLogAdminLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogBackupLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileRollover"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeleted"),
        ("TIMETRA-LOG-MIB", "tmnxTestEvent"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceError"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventThrottled"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblem"))
)
if mibBuilder.loadTexts:
    tmnxLogNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxLogNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 25)
)
tmnxLogNotificationV6v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogSpaceContention"),
        ("TIMETRA-LOG-MIB", "tmnxLogAdminLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogBackupLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileRollover"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeleted"),
        ("TIMETRA-LOG-MIB", "tmnxTestEvent"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceError"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventThrottled"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblem"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingDataLoss"),
        ("TIMETRA-LOG-MIB", "tmnxStdEventsReplayed"))
)
if mibBuilder.loadTexts:
    tmnxLogNotificationV6v0Group.setStatus(
        "current"
    )

tmnxLogNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 31)
)
tmnxLogNotificationV9v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogEventOverrun")
)
if mibBuilder.loadTexts:
    tmnxLogNotificationV9v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLogV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 4)
)
tmnxLogV4v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV4v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogGroup"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsR2r1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationR3r0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 5)
)
tmnxLogV5v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 6)
)
tmnxLogV6v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 7)
)
tmnxLogV6v1Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV6v1Compliance.setStatus(
        "current"
    )

tmnxLogV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 8)
)
tmnxLogV7v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 9)
)
tmnxLogV9v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 10)
)
tmnxLogV8v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 11)
)
tmnxLogV10v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpGroup"))
)
if mibBuilder.loadTexts:
    tmnxLogV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 12)
)
tmnxLogV11v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogApExtGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAppRouteNotifV10v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV11v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LOG-MIB",
    **{"TmnxPerceivedSeverity": TmnxPerceivedSeverity,
       "TmnxSyslogId": TmnxSyslogId,
       "TmnxSyslogIdOrEmpty": TmnxSyslogIdOrEmpty,
       "TmnxSyslogFacility": TmnxSyslogFacility,
       "TmnxUdpPort": TmnxUdpPort,
       "TmnxSyslogSeverity": TmnxSyslogSeverity,
       "TmnxLogFileId": TmnxLogFileId,
       "TmnxLogFileType": TmnxLogFileType,
       "TmnxLogIdIndex": TmnxLogIdIndex,
       "TmnxCFlash": TmnxCFlash,
       "TmnxLogFilterId": TmnxLogFilterId,
       "TmnxLogFilterEntryId": TmnxLogFilterEntryId,
       "TmnxLogFilterOperator": TmnxLogFilterOperator,
       "TmnxEventNumber": TmnxEventNumber,
       "timetraLogMIBModule": timetraLogMIBModule,
       "tmnxLogConformance": tmnxLogConformance,
       "tmnxLogCompliances": tmnxLogCompliances,
       "tmnxLogV4v0Compliance": tmnxLogV4v0Compliance,
       "tmnxLogV5v0Compliance": tmnxLogV5v0Compliance,
       "tmnxLogV6v0Compliance": tmnxLogV6v0Compliance,
       "tmnxLogV6v1Compliance": tmnxLogV6v1Compliance,
       "tmnxLogV7v0Compliance": tmnxLogV7v0Compliance,
       "tmnxLogV9v0Compliance": tmnxLogV9v0Compliance,
       "tmnxLogV8v0Compliance": tmnxLogV8v0Compliance,
       "tmnxLogV10v0Compliance": tmnxLogV10v0Compliance,
       "tmnxLogV11v0Compliance": tmnxLogV11v0Compliance,
       "tmnxLogGroups": tmnxLogGroups,
       "tmnxLogGlobalGroup": tmnxLogGlobalGroup,
       "tmnxLogAccountingPolicyGroup": tmnxLogAccountingPolicyGroup,
       "tmnxLogFileIdGroup": tmnxLogFileIdGroup,
       "tmnxLogSyslogGroup": tmnxLogSyslogGroup,
       "tmnxSnmpTrapGroup": tmnxSnmpTrapGroup,
       "tmnxLogEventsR2r1Group": tmnxLogEventsR2r1Group,
       "tmnxLogNotifyObjsR3r0Group": tmnxLogNotifyObjsR3r0Group,
       "tmnxLogNotificationR3r0Group": tmnxLogNotificationR3r0Group,
       "tmnxLogV4v0Group": tmnxLogV4v0Group,
       "tmnxSnmpSetErrsGroup": tmnxSnmpSetErrsGroup,
       "tmnxLogEventsV5v0Group": tmnxLogEventsV5v0Group,
       "tmnxLogNotifyObjsV5v0Group": tmnxLogNotifyObjsV5v0Group,
       "tmnxLogNotificationV5v0Group": tmnxLogNotificationV5v0Group,
       "tmnxLogSyslogV5v0Group": tmnxLogSyslogV5v0Group,
       "tmnxSnmpTrapV5v0Group": tmnxSnmpTrapV5v0Group,
       "tmnxLogV5v0Group": tmnxLogV5v0Group,
       "tmnxLogObsoleteObjsV5v0Group": tmnxLogObsoleteObjsV5v0Group,
       "tmnxLogNotifyObjsV6v0Group": tmnxLogNotifyObjsV6v0Group,
       "tmnxLogNotificationV6v0Group": tmnxLogNotificationV6v0Group,
       "tmnxSnmpTrapDestV6v0Group": tmnxSnmpTrapDestV6v0Group,
       "tmnxLogAccountingPolicyV6v1Group": tmnxLogAccountingPolicyV6v1Group,
       "tmnxLogAccountingPolicyCRV7v0Group": tmnxLogAccountingPolicyCRV7v0Group,
       "tmnxLogRoutePreferenceV7v0Group": tmnxLogRoutePreferenceV7v0Group,
       "tmnxLogNotifyObjsV8v0Group": tmnxLogNotifyObjsV8v0Group,
       "tmnxLogNotificationV9v0Group": tmnxLogNotificationV9v0Group,
       "tmnxLogEventDampedV8v0Group": tmnxLogEventDampedV8v0Group,
       "tmnxLogApV9v0Group": tmnxLogApV9v0Group,
       "tmnxLogExRbkOpGroup": tmnxLogExRbkOpGroup,
       "tmnxLogNotifyObjsV10v0Group": tmnxLogNotifyObjsV10v0Group,
       "tmnxLogApExtGroup": tmnxLogApExtGroup,
       "tmnxLogAppRouteNotifV10v0Group": tmnxLogAppRouteNotifV10v0Group,
       "tmnxLogApV11v0Group": tmnxLogApV11v0Group,
       "tmnxLogEventsV11v0Group": tmnxLogEventsV11v0Group,
       "tmnxLogApCrV11v0Group": tmnxLogApCrV11v0Group,
       "tmnxLogObjs": tmnxLogObjs,
       "tmnxLogNotificationObjects": tmnxLogNotificationObjects,
       "tmnxLogFileDeletedLogId": tmnxLogFileDeletedLogId,
       "tmnxLogFileDeletedFileId": tmnxLogFileDeletedFileId,
       "tmnxLogFileDeletedLogType": tmnxLogFileDeletedLogType,
       "tmnxLogFileDeletedLocation": tmnxLogFileDeletedLocation,
       "tmnxLogFileDeletedName": tmnxLogFileDeletedName,
       "tmnxLogFileDeletedCreateTime": tmnxLogFileDeletedCreateTime,
       "tmnxLogTraceErrorTitle": tmnxLogTraceErrorTitle,
       "tmnxLogTraceErrorSubject": tmnxLogTraceErrorSubject,
       "tmnxLogTraceErrorMessage": tmnxLogTraceErrorMessage,
       "tmnxLogThrottledEventID": tmnxLogThrottledEventID,
       "tmnxLogThrottledEvents": tmnxLogThrottledEvents,
       "tmnxSysLogTargetId": tmnxSysLogTargetId,
       "tmnxSysLogTargetProblemDescr": tmnxSysLogTargetProblemDescr,
       "tmnxLogNotifyApInterval": tmnxLogNotifyApInterval,
       "tmnxStdReplayStartEvent": tmnxStdReplayStartEvent,
       "tmnxStdReplayEndEvent": tmnxStdReplayEndEvent,
       "tmnxLogMaxLogs": tmnxLogMaxLogs,
       "tmnxLogFileIdTable": tmnxLogFileIdTable,
       "tmnxLogFileIdEntry": tmnxLogFileIdEntry,
       "tmnxLogFileId": tmnxLogFileId,
       "tmnxLogFileIdRowStatus": tmnxLogFileIdRowStatus,
       "tmnxLogFileIdStorageType": tmnxLogFileIdStorageType,
       "tmnxLogFileIdRolloverTime": tmnxLogFileIdRolloverTime,
       "tmnxLogFileIdRetainTime": tmnxLogFileIdRetainTime,
       "tmnxLogFileIdAdminLocation": tmnxLogFileIdAdminLocation,
       "tmnxLogFileIdOperLocation": tmnxLogFileIdOperLocation,
       "tmnxLogFileIdDescription": tmnxLogFileIdDescription,
       "tmnxLogFileIdLogType": tmnxLogFileIdLogType,
       "tmnxLogFileIdLogId": tmnxLogFileIdLogId,
       "tmnxLogFileIdPathName": tmnxLogFileIdPathName,
       "tmnxLogFileIdCreateTime": tmnxLogFileIdCreateTime,
       "tmnxLogFileIdBackupLoc": tmnxLogFileIdBackupLoc,
       "tmnxLogApTable": tmnxLogApTable,
       "tmnxLogApEntry": tmnxLogApEntry,
       "tmnxLogApPolicyId": tmnxLogApPolicyId,
       "tmnxLogApRowStatus": tmnxLogApRowStatus,
       "tmnxLogApStorageType": tmnxLogApStorageType,
       "tmnxLogApAdminStatus": tmnxLogApAdminStatus,
       "tmnxLogApOperStatus": tmnxLogApOperStatus,
       "tmnxLogApInterval": tmnxLogApInterval,
       "tmnxLogApDescription": tmnxLogApDescription,
       "tmnxLogApDefault": tmnxLogApDefault,
       "tmnxLogApRecord": tmnxLogApRecord,
       "tmnxLogApToFileId": tmnxLogApToFileId,
       "tmnxLogApPortType": tmnxLogApPortType,
       "tmnxLogApDefaultInterval": tmnxLogApDefaultInterval,
       "tmnxLogApDataLossCount": tmnxLogApDataLossCount,
       "tmnxLogApLastDataLossTimeStamp": tmnxLogApLastDataLossTimeStamp,
       "tmnxLogApToFileType": tmnxLogApToFileType,
       "tmnxLogApIncludeSystemInfo": tmnxLogApIncludeSystemInfo,
       "tmnxLogIdTable": tmnxLogIdTable,
       "tmnxLogIdEntry": tmnxLogIdEntry,
       "tmnxLogIdIndex": tmnxLogIdIndex,
       "tmnxLogIdRowStatus": tmnxLogIdRowStatus,
       "tmnxLogIdStorageType": tmnxLogIdStorageType,
       "tmnxLogIdAdminStatus": tmnxLogIdAdminStatus,
       "tmnxLogIdOperStatus": tmnxLogIdOperStatus,
       "tmnxLogIdDescription": tmnxLogIdDescription,
       "tmnxLogIdFilterId": tmnxLogIdFilterId,
       "tmnxLogIdSource": tmnxLogIdSource,
       "tmnxLogIdDestination": tmnxLogIdDestination,
       "tmnxLogIdFileId": tmnxLogIdFileId,
       "tmnxLogIdSyslogId": tmnxLogIdSyslogId,
       "tmnxLogIdMaxMemorySize": tmnxLogIdMaxMemorySize,
       "tmnxLogIdConsoleSession": tmnxLogIdConsoleSession,
       "tmnxLogIdForwarded": tmnxLogIdForwarded,
       "tmnxLogIdDropped": tmnxLogIdDropped,
       "tmnxLogIdTimeFormat": tmnxLogIdTimeFormat,
       "tmnxLogFilterTable": tmnxLogFilterTable,
       "tmnxLogFilterEntry": tmnxLogFilterEntry,
       "tmnxLogFilterId": tmnxLogFilterId,
       "tmnxLogFilterRowStatus": tmnxLogFilterRowStatus,
       "tmnxLogFilterDescription": tmnxLogFilterDescription,
       "tmnxLogFilterDefaultAction": tmnxLogFilterDefaultAction,
       "tmnxLogFilterInUse": tmnxLogFilterInUse,
       "tmnxLogFilterParamsTable": tmnxLogFilterParamsTable,
       "tmnxLogFilterParamsEntry": tmnxLogFilterParamsEntry,
       "tmnxLogFilterParamsIndex": tmnxLogFilterParamsIndex,
       "tmnxLogFilterParamsRowStatus": tmnxLogFilterParamsRowStatus,
       "tmnxLogFilterParamsDescription": tmnxLogFilterParamsDescription,
       "tmnxLogFilterParamsAction": tmnxLogFilterParamsAction,
       "tmnxLogFilterParamsApplication": tmnxLogFilterParamsApplication,
       "tmnxLogFilterParamsApplOperator": tmnxLogFilterParamsApplOperator,
       "tmnxLogFilterParamsNumber": tmnxLogFilterParamsNumber,
       "tmnxLogFilterParamsNumberOperator": tmnxLogFilterParamsNumberOperator,
       "tmnxLogFilterParamsSeverity": tmnxLogFilterParamsSeverity,
       "tmnxLogFilterParamsSeverityOperator": tmnxLogFilterParamsSeverityOperator,
       "tmnxLogFilterParamsSubject": tmnxLogFilterParamsSubject,
       "tmnxLogFilterParamsSubjectOperator": tmnxLogFilterParamsSubjectOperator,
       "tmnxLogFilterParamsSubjectRegexp": tmnxLogFilterParamsSubjectRegexp,
       "tmnxLogFilterParamsRouter": tmnxLogFilterParamsRouter,
       "tmnxLogFilterParamsRouterOperator": tmnxLogFilterParamsRouterOperator,
       "tmnxLogFilterParamsRouterRegexp": tmnxLogFilterParamsRouterRegexp,
       "tmnxSyslogTargetTable": tmnxSyslogTargetTable,
       "tmnxSyslogTargetEntry": tmnxSyslogTargetEntry,
       "tmnxSyslogTargetIndex": tmnxSyslogTargetIndex,
       "tmnxSyslogTargetRowStatus": tmnxSyslogTargetRowStatus,
       "tmnxSyslogTargetDescription": tmnxSyslogTargetDescription,
       "tmnxSyslogTargetAddress": tmnxSyslogTargetAddress,
       "tmnxSyslogTargetUdpPort": tmnxSyslogTargetUdpPort,
       "tmnxSyslogTargetFacility": tmnxSyslogTargetFacility,
       "tmnxSyslogTargetSeverity": tmnxSyslogTargetSeverity,
       "tmnxSyslogTargetMessagePrefix": tmnxSyslogTargetMessagePrefix,
       "tmnxSyslogTargetMessagesDropped": tmnxSyslogTargetMessagesDropped,
       "tmnxSyslogTargetAddrType": tmnxSyslogTargetAddrType,
       "tmnxSyslogTargetAddr": tmnxSyslogTargetAddr,
       "tmnxEventAppTable": tmnxEventAppTable,
       "tmnxEventAppEntry": tmnxEventAppEntry,
       "tmnxEventAppIndex": tmnxEventAppIndex,
       "tmnxEventAppName": tmnxEventAppName,
       "tmnxEventTable": tmnxEventTable,
       "tmnxEventEntry": tmnxEventEntry,
       "tmnxEventID": tmnxEventID,
       "tmnxEventName": tmnxEventName,
       "tmnxEventSeverity": tmnxEventSeverity,
       "tmnxEventControl": tmnxEventControl,
       "tmnxEventCounter": tmnxEventCounter,
       "tmnxEventDropCount": tmnxEventDropCount,
       "tmnxEventReset": tmnxEventReset,
       "tmnxEventThrottle": tmnxEventThrottle,
       "tmnxEventSpecThrottle": tmnxEventSpecThrottle,
       "tmnxEventSpecThrottleLimit": tmnxEventSpecThrottleLimit,
       "tmnxEventSpecThrottleIntval": tmnxEventSpecThrottleIntval,
       "tmnxEventSpecThrottleDef": tmnxEventSpecThrottleDef,
       "tmnxEventSpecThrottleLimitDef": tmnxEventSpecThrottleLimitDef,
       "tmnxEventSpecThrottleIntvalDef": tmnxEventSpecThrottleIntvalDef,
       "tmnxSnmpTrapGroupTable": tmnxSnmpTrapGroupTable,
       "tmnxSnmpTrapGroupEntry": tmnxSnmpTrapGroupEntry,
       "tmnxStgIndex": tmnxStgIndex,
       "tmnxStgDestAddress": tmnxStgDestAddress,
       "tmnxStgDestPort": tmnxStgDestPort,
       "tmnxStgRowStatus": tmnxStgRowStatus,
       "tmnxStgDescription": tmnxStgDescription,
       "tmnxStgVersion": tmnxStgVersion,
       "tmnxStgNotifyCommunity": tmnxStgNotifyCommunity,
       "tmnxStgSecurityLevel": tmnxStgSecurityLevel,
       "tmnxEventTest": tmnxEventTest,
       "tmnxEventThrottleLimit": tmnxEventThrottleLimit,
       "tmnxEventThrottleInterval": tmnxEventThrottleInterval,
       "tmnxSnmpSetErrsMax": tmnxSnmpSetErrsMax,
       "tmnxSnmpSetErrsTable": tmnxSnmpSetErrsTable,
       "tmnxSnmpSetErrsEntry": tmnxSnmpSetErrsEntry,
       "tmnxSseAddressType": tmnxSseAddressType,
       "tmnxSseAddress": tmnxSseAddress,
       "tmnxSseSnmpPort": tmnxSseSnmpPort,
       "tmnxSseRequestId": tmnxSseRequestId,
       "tmnxSseVersion": tmnxSseVersion,
       "tmnxSseSeverityLevel": tmnxSseSeverityLevel,
       "tmnxSseModuleId": tmnxSseModuleId,
       "tmnxSseModuleName": tmnxSseModuleName,
       "tmnxSseErrorCode": tmnxSseErrorCode,
       "tmnxSseErrorName": tmnxSseErrorName,
       "tmnxSseErrorMsg": tmnxSseErrorMsg,
       "tmnxSseExtraText": tmnxSseExtraText,
       "tmnxSseTimestamp": tmnxSseTimestamp,
       "tmnxSnmpTrapLogTable": tmnxSnmpTrapLogTable,
       "tmnxSnmpTrapLogEntry": tmnxSnmpTrapLogEntry,
       "tmnxSnmpTrapLogDescription": tmnxSnmpTrapLogDescription,
       "tmnxSnmpTrapDestTable": tmnxSnmpTrapDestTable,
       "tmnxSnmpTrapDestEntry": tmnxSnmpTrapDestEntry,
       "tmnxStdIndex": tmnxStdIndex,
       "tmnxStdName": tmnxStdName,
       "tmnxStdRowStatus": tmnxStdRowStatus,
       "tmnxStdRowLastChanged": tmnxStdRowLastChanged,
       "tmnxStdDestAddrType": tmnxStdDestAddrType,
       "tmnxStdDestAddr": tmnxStdDestAddr,
       "tmnxStdDestPort": tmnxStdDestPort,
       "tmnxStdDescription": tmnxStdDescription,
       "tmnxStdVersion": tmnxStdVersion,
       "tmnxStdNotifyCommunity": tmnxStdNotifyCommunity,
       "tmnxStdSecurityLevel": tmnxStdSecurityLevel,
       "tmnxStdReplay": tmnxStdReplay,
       "tmnxStdReplayStart": tmnxStdReplayStart,
       "tmnxStdReplayLastTime": tmnxStdReplayLastTime,
       "tmnxStdMaxTargets": tmnxStdMaxTargets,
       "tmnxLogApCustRecordTable": tmnxLogApCustRecordTable,
       "tmnxLogApCustRecordEntry": tmnxLogApCustRecordEntry,
       "tmnxLogApCrLastChanged": tmnxLogApCrLastChanged,
       "tmnxLogApCrSignChangeDelta": tmnxLogApCrSignChangeDelta,
       "tmnxLogApCrSignChangeQueue": tmnxLogApCrSignChangeQueue,
       "tmnxLogApCrSignChangeOCntr": tmnxLogApCrSignChangeOCntr,
       "tmnxLogApCrSignChangeQICounters": tmnxLogApCrSignChangeQICounters,
       "tmnxLogApCrSignChangeQECounters": tmnxLogApCrSignChangeQECounters,
       "tmnxLogApCrSignChangeOICounters": tmnxLogApCrSignChangeOICounters,
       "tmnxLogApCrSignChangeOECounters": tmnxLogApCrSignChangeOECounters,
       "tmnxLogApCrSignChangeAACounters": tmnxLogApCrSignChangeAACounters,
       "tmnxLogApCrAACounters": tmnxLogApCrAACounters,
       "tmnxLogApCrAASubAttributes": tmnxLogApCrAASubAttributes,
       "tmnxLogApCustRecordQueueTable": tmnxLogApCustRecordQueueTable,
       "tmnxLogApCustRecordQueueEntry": tmnxLogApCustRecordQueueEntry,
       "tmnxLogApCrQueueId": tmnxLogApCrQueueId,
       "tmnxLogApCrQueueRowStatus": tmnxLogApCrQueueRowStatus,
       "tmnxLogApCrQueueLastChanged": tmnxLogApCrQueueLastChanged,
       "tmnxLogApCrQueueICounters": tmnxLogApCrQueueICounters,
       "tmnxLogApCrQueueECounters": tmnxLogApCrQueueECounters,
       "tmnxLogApCrOverrideCntrTable": tmnxLogApCrOverrideCntrTable,
       "tmnxLogApCrOverrideCntrEntry": tmnxLogApCrOverrideCntrEntry,
       "tmnxLogApCrOverrideCntrId": tmnxLogApCrOverrideCntrId,
       "tmnxLogApCrOverrideCntrRowStatus": tmnxLogApCrOverrideCntrRowStatus,
       "tmnxLogApCrOverrideCntrLastChngd": tmnxLogApCrOverrideCntrLastChngd,
       "tmnxLogApCrOverrideCntrICounters": tmnxLogApCrOverrideCntrICounters,
       "tmnxLogApCrOverrideCntrECounters": tmnxLogApCrOverrideCntrECounters,
       "tmnxEventPrimaryRoutePref": tmnxEventPrimaryRoutePref,
       "tmnxEventSecondaryRoutePref": tmnxEventSecondaryRoutePref,
       "tmnxLogConfigEventsDamped": tmnxLogConfigEventsDamped,
       "tmnxLogEventHistoryObjs": tmnxLogEventHistoryObjs,
       "tmnxLogEventHistGeneralObjs": tmnxLogEventHistGeneralObjs,
       "tmnxLogExRbkOpTblLastChange": tmnxLogExRbkOpTblLastChange,
       "tmnxLogExRbkOpMaxEntries": tmnxLogExRbkOpMaxEntries,
       "tmnxLogExecRollbackOpTable": tmnxLogExecRollbackOpTable,
       "tmnxLogExecRollbackOpEntry": tmnxLogExecRollbackOpEntry,
       "tmnxLogExRbkOpIndex": tmnxLogExRbkOpIndex,
       "tmnxLogExRbkOpLastChanged": tmnxLogExRbkOpLastChanged,
       "tmnxLogExRbkOpType": tmnxLogExRbkOpType,
       "tmnxLogExRbkOpStatus": tmnxLogExRbkOpStatus,
       "tmnxLogExRbkOpBegin": tmnxLogExRbkOpBegin,
       "tmnxLogExRbkOpEnd": tmnxLogExRbkOpEnd,
       "tmnxLogExRbkOpFile": tmnxLogExRbkOpFile,
       "tmnxLogExRbkOpUser": tmnxLogExRbkOpUser,
       "tmnxLogExRbkOpNumEvents": tmnxLogExRbkOpNumEvents,
       "tmnxLogExecRollbackEventTable": tmnxLogExecRollbackEventTable,
       "tmnxLogExecRollbackEventEntry": tmnxLogExecRollbackEventEntry,
       "tmnxLogExRbkEventIndex": tmnxLogExRbkEventIndex,
       "tmnxLogExRbkEventOID": tmnxLogExRbkEventOID,
       "tmnxLogExRbkNotifyObjects": tmnxLogExRbkNotifyObjects,
       "tmnxLogExecRollbackOpIndex": tmnxLogExecRollbackOpIndex,
       "tmnxLogColdStartWaitTime": tmnxLogColdStartWaitTime,
       "tmnxLogRouteRecoveryWaitTime": tmnxLogRouteRecoveryWaitTime,
       "tmnxLogNotifyPrefix": tmnxLogNotifyPrefix,
       "tmnxLogNotifications": tmnxLogNotifications,
       "tmnxLogSpaceContention": tmnxLogSpaceContention,
       "tmnxLogAdminLocFailed": tmnxLogAdminLocFailed,
       "tmnxLogBackupLocFailed": tmnxLogBackupLocFailed,
       "tmnxLogFileRollover": tmnxLogFileRollover,
       "tmnxLogFileDeleted": tmnxLogFileDeleted,
       "tmnxTestEvent": tmnxTestEvent,
       "tmnxLogTraceError": tmnxLogTraceError,
       "tmnxLogEventThrottled": tmnxLogEventThrottled,
       "tmnxSysLogTargetProblem": tmnxSysLogTargetProblem,
       "tmnxLogAccountingDataLoss": tmnxLogAccountingDataLoss,
       "tmnxStdEventsReplayed": tmnxStdEventsReplayed,
       "tmnxLogEventOverrun": tmnxLogEventOverrun}
)
