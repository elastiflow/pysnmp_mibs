# SNMP MIB module (RUIJIE-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-LOG-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ruijieLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieLogMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LogSeverity(TextualConvention, Integer32):
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



class LogTimeStamp(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("datetime", 2),
          ("uptime", 3))
    )



class LogSyslogFacility(TextualConvention, Integer32):
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
          ("system", 3),
          ("security", 4),
          ("syslogd", 5),
          ("lineprinter", 6),
          ("network", 7),
          ("uUCP", 8),
          ("clockdaemon", 9),
          ("authorization", 10),
          ("fTP", 11),
          ("nTP", 12),
          ("logaudit", 13),
          ("logalert", 14),
          ("clockdaemon2", 15),
          ("localuse0", 16),
          ("localuse1", 17),
          ("localuse2", 18),
          ("localuse3", 19),
          ("localuse4", 20),
          ("localuse5", 21),
          ("localuse6", 22),
          ("localuse7", 23))
    )



# MIB Managed Objects in the order of their OIDs

_RuijieLogMIBObjects_ObjectIdentity = ObjectIdentity
ruijieLogMIBObjects = _RuijieLogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1)
)


class _RuijieLogGlobalStatus_Type(EnabledStatus):
    """Custom type ruijieLogGlobalStatus based on EnabledStatus"""
    defaultValue = 1


_RuijieLogGlobalStatus_Type.__name__ = "EnabledStatus"
_RuijieLogGlobalStatus_Object = MibScalar
ruijieLogGlobalStatus = _RuijieLogGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 1),
    _RuijieLogGlobalStatus_Type()
)
ruijieLogGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogGlobalStatus.setStatus("current")


class _RuijieLogSendConsoleStatus_Type(EnabledStatus):
    """Custom type ruijieLogSendConsoleStatus based on EnabledStatus"""
    defaultValue = 1


_RuijieLogSendConsoleStatus_Type.__name__ = "EnabledStatus"
_RuijieLogSendConsoleStatus_Object = MibScalar
ruijieLogSendConsoleStatus = _RuijieLogSendConsoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 2),
    _RuijieLogSendConsoleStatus_Type()
)
ruijieLogSendConsoleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSendConsoleStatus.setStatus("current")


class _RuijieLogSendConsoleMaxSeverity_Type(LogSeverity):
    """Custom type ruijieLogSendConsoleMaxSeverity based on LogSeverity"""
    defaultValue = 7


_RuijieLogSendConsoleMaxSeverity_Type.__name__ = "LogSeverity"
_RuijieLogSendConsoleMaxSeverity_Object = MibScalar
ruijieLogSendConsoleMaxSeverity = _RuijieLogSendConsoleMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 3),
    _RuijieLogSendConsoleMaxSeverity_Type()
)
ruijieLogSendConsoleMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSendConsoleMaxSeverity.setStatus("current")


class _RuijieLogSendMonitorStatus_Type(EnabledStatus):
    """Custom type ruijieLogSendMonitorStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieLogSendMonitorStatus_Type.__name__ = "EnabledStatus"
_RuijieLogSendMonitorStatus_Object = MibScalar
ruijieLogSendMonitorStatus = _RuijieLogSendMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 4),
    _RuijieLogSendMonitorStatus_Type()
)
ruijieLogSendMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSendMonitorStatus.setStatus("current")


class _RuijieLogSendMonitorMaxSeverity_Type(LogSeverity):
    """Custom type ruijieLogSendMonitorMaxSeverity based on LogSeverity"""
    defaultValue = 7


_RuijieLogSendMonitorMaxSeverity_Type.__name__ = "LogSeverity"
_RuijieLogSendMonitorMaxSeverity_Object = MibScalar
ruijieLogSendMonitorMaxSeverity = _RuijieLogSendMonitorMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 5),
    _RuijieLogSendMonitorMaxSeverity_Type()
)
ruijieLogSendMonitorMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSendMonitorMaxSeverity.setStatus("current")


class _RuijieLogSaveFileName_Type(DisplayString):
    """Custom type ruijieLogSaveFileName based on DisplayString"""
    defaultValue = OctetString("")


_RuijieLogSaveFileName_Type.__name__ = "DisplayString"
_RuijieLogSaveFileName_Object = MibScalar
ruijieLogSaveFileName = _RuijieLogSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 6),
    _RuijieLogSaveFileName_Type()
)
ruijieLogSaveFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSaveFileName.setStatus("current")


class _RuijieLogFileMaxSeverity_Type(LogSeverity):
    """Custom type ruijieLogFileMaxSeverity based on LogSeverity"""
    defaultValue = 5


_RuijieLogFileMaxSeverity_Type.__name__ = "LogSeverity"
_RuijieLogFileMaxSeverity_Object = MibScalar
ruijieLogFileMaxSeverity = _RuijieLogFileMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 7),
    _RuijieLogFileMaxSeverity_Type()
)
ruijieLogFileMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogFileMaxSeverity.setStatus("current")


class _RuijieLogFileMaxSize_Type(Integer32):
    """Custom type ruijieLogFileMaxSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 2000000),
    )


_RuijieLogFileMaxSize_Type.__name__ = "Integer32"
_RuijieLogFileMaxSize_Object = MibScalar
ruijieLogFileMaxSize = _RuijieLogFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 8),
    _RuijieLogFileMaxSize_Type()
)
ruijieLogFileMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogFileMaxSize.setStatus("current")


class _RuijieLogSendBufferStatus_Type(EnabledStatus):
    """Custom type ruijieLogSendBufferStatus based on EnabledStatus"""
    defaultValue = 1


_RuijieLogSendBufferStatus_Type.__name__ = "EnabledStatus"
_RuijieLogSendBufferStatus_Object = MibScalar
ruijieLogSendBufferStatus = _RuijieLogSendBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 9),
    _RuijieLogSendBufferStatus_Type()
)
ruijieLogSendBufferStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSendBufferStatus.setStatus("current")


class _RuijieLogSendBufferMaxSeverity_Type(LogSeverity):
    """Custom type ruijieLogSendBufferMaxSeverity based on LogSeverity"""
    defaultValue = 7


_RuijieLogSendBufferMaxSeverity_Type.__name__ = "LogSeverity"
_RuijieLogSendBufferMaxSeverity_Object = MibScalar
ruijieLogSendBufferMaxSeverity = _RuijieLogSendBufferMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 10),
    _RuijieLogSendBufferMaxSeverity_Type()
)
ruijieLogSendBufferMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSendBufferMaxSeverity.setStatus("current")
_RuijieLogClearBuffer_Type = Integer32
_RuijieLogClearBuffer_Object = MibScalar
ruijieLogClearBuffer = _RuijieLogClearBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 11),
    _RuijieLogClearBuffer_Type()
)
ruijieLogClearBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogClearBuffer.setStatus("current")
_RuijieLogHisRecordMaxNum_Type = Integer32
_RuijieLogHisRecordMaxNum_Object = MibScalar
ruijieLogHisRecordMaxNum = _RuijieLogHisRecordMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 12),
    _RuijieLogHisRecordMaxNum_Type()
)
ruijieLogHisRecordMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLogHisRecordMaxNum.setStatus("current")
_RuijieLogHisTable_Object = MibTable
ruijieLogHisTable = _RuijieLogHisTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    ruijieLogHisTable.setStatus("current")
_RuijieLogHisEntry_Object = MibTableRow
ruijieLogHisEntry = _RuijieLogHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1)
)
ruijieLogHisEntry.setIndexNames(
    (0, "RUIJIE-LOG-MIB", "ruijieLogHisIndex"),
)
if mibBuilder.loadTexts:
    ruijieLogHisEntry.setStatus("current")
_RuijieLogHisIndex_Type = Integer32
_RuijieLogHisIndex_Object = MibTableColumn
ruijieLogHisIndex = _RuijieLogHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 1),
    _RuijieLogHisIndex_Type()
)
ruijieLogHisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLogHisIndex.setStatus("current")
_RuijieLogHisSeverity_Type = LogSeverity
_RuijieLogHisSeverity_Object = MibTableColumn
ruijieLogHisSeverity = _RuijieLogHisSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 2),
    _RuijieLogHisSeverity_Type()
)
ruijieLogHisSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLogHisSeverity.setStatus("current")


class _RuijieLogHisMsgName_Type(DisplayString):
    """Custom type ruijieLogHisMsgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RuijieLogHisMsgName_Type.__name__ = "DisplayString"
_RuijieLogHisMsgName_Object = MibTableColumn
ruijieLogHisMsgName = _RuijieLogHisMsgName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 3),
    _RuijieLogHisMsgName_Type()
)
ruijieLogHisMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLogHisMsgName.setStatus("current")


class _RuijieLogHisDescription_Type(DisplayString):
    """Custom type ruijieLogHisDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RuijieLogHisDescription_Type.__name__ = "DisplayString"
_RuijieLogHisDescription_Object = MibTableColumn
ruijieLogHisDescription = _RuijieLogHisDescription_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 4),
    _RuijieLogHisDescription_Type()
)
ruijieLogHisDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLogHisDescription.setStatus("current")
_RuijieLogHisTime_Type = DateAndTime
_RuijieLogHisTime_Object = MibTableColumn
ruijieLogHisTime = _RuijieLogHisTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 5),
    _RuijieLogHisTime_Type()
)
ruijieLogHisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLogHisTime.setStatus("current")
_RuijieLogHisStamps_Type = TimeStamp
_RuijieLogHisStamps_Object = MibTableColumn
ruijieLogHisStamps = _RuijieLogHisStamps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 13, 1, 6),
    _RuijieLogHisStamps_Type()
)
ruijieLogHisStamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLogHisStamps.setStatus("current")


class _RuijieLogSequenceGlobalStatus_Type(EnabledStatus):
    """Custom type ruijieLogSequenceGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieLogSequenceGlobalStatus_Type.__name__ = "EnabledStatus"
_RuijieLogSequenceGlobalStatus_Object = MibScalar
ruijieLogSequenceGlobalStatus = _RuijieLogSequenceGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 14),
    _RuijieLogSequenceGlobalStatus_Type()
)
ruijieLogSequenceGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSequenceGlobalStatus.setStatus("current")


class _RuijieLogTimeStampGlobalStatus_Type(LogTimeStamp):
    """Custom type ruijieLogTimeStampGlobalStatus based on LogTimeStamp"""
    defaultValue = 2


_RuijieLogTimeStampGlobalStatus_Type.__name__ = "LogTimeStamp"
_RuijieLogTimeStampGlobalStatus_Object = MibScalar
ruijieLogTimeStampGlobalStatus = _RuijieLogTimeStampGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 15),
    _RuijieLogTimeStampGlobalStatus_Type()
)
ruijieLogTimeStampGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogTimeStampGlobalStatus.setStatus("current")


class _RuijieLogSyslogRelayGlobalStatus_Type(EnabledStatus):
    """Custom type ruijieLogSyslogRelayGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieLogSyslogRelayGlobalStatus_Type.__name__ = "EnabledStatus"
_RuijieLogSyslogRelayGlobalStatus_Object = MibScalar
ruijieLogSyslogRelayGlobalStatus = _RuijieLogSyslogRelayGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 16),
    _RuijieLogSyslogRelayGlobalStatus_Type()
)
ruijieLogSyslogRelayGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSyslogRelayGlobalStatus.setStatus("current")


class _RuijieLogSyslogFacility_Type(LogSyslogFacility):
    """Custom type ruijieLogSyslogFacility based on LogSyslogFacility"""
    defaultValue = 23


_RuijieLogSyslogFacility_Type.__name__ = "LogSyslogFacility"
_RuijieLogSyslogFacility_Object = MibScalar
ruijieLogSyslogFacility = _RuijieLogSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 17),
    _RuijieLogSyslogFacility_Type()
)
ruijieLogSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSyslogFacility.setStatus("current")


class _RuijieLogSyslogSeverity_Type(LogSeverity):
    """Custom type ruijieLogSyslogSeverity based on LogSeverity"""
    defaultValue = 7


_RuijieLogSyslogSeverity_Type.__name__ = "LogSeverity"
_RuijieLogSyslogSeverity_Object = MibScalar
ruijieLogSyslogSeverity = _RuijieLogSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 18),
    _RuijieLogSyslogSeverity_Type()
)
ruijieLogSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSyslogSeverity.setStatus("current")
_RuijieLogSyslogServerTable_Object = MibTable
ruijieLogSyslogServerTable = _RuijieLogSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 19)
)
if mibBuilder.loadTexts:
    ruijieLogSyslogServerTable.setStatus("current")
_RuijieLogSyslogServerEntry_Object = MibTableRow
ruijieLogSyslogServerEntry = _RuijieLogSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 19, 1)
)
ruijieLogSyslogServerEntry.setIndexNames(
    (0, "RUIJIE-LOG-MIB", "ruijieLogSyslogServerIpAddr"),
)
if mibBuilder.loadTexts:
    ruijieLogSyslogServerEntry.setStatus("current")
_RuijieLogSyslogServerIpAddr_Type = IpAddress
_RuijieLogSyslogServerIpAddr_Object = MibTableColumn
ruijieLogSyslogServerIpAddr = _RuijieLogSyslogServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 19, 1, 1),
    _RuijieLogSyslogServerIpAddr_Type()
)
ruijieLogSyslogServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLogSyslogServerIpAddr.setStatus("current")
_RuijieLogSyslogServerIpStatus_Type = ConfigStatus
_RuijieLogSyslogServerIpStatus_Object = MibTableColumn
ruijieLogSyslogServerIpStatus = _RuijieLogSyslogServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 19, 1, 2),
    _RuijieLogSyslogServerIpStatus_Type()
)
ruijieLogSyslogServerIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSyslogServerIpStatus.setStatus("current")
_RuijieLogSyslogSendSrcIfindex_Type = IfIndex
_RuijieLogSyslogSendSrcIfindex_Object = MibScalar
ruijieLogSyslogSendSrcIfindex = _RuijieLogSyslogSendSrcIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 20),
    _RuijieLogSyslogSendSrcIfindex_Type()
)
ruijieLogSyslogSendSrcIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSyslogSendSrcIfindex.setStatus("current")
_RuijieLogSyslogSendSrcIp_Type = IpAddress
_RuijieLogSyslogSendSrcIp_Object = MibScalar
ruijieLogSyslogSendSrcIp = _RuijieLogSyslogSendSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 1, 21),
    _RuijieLogSyslogSendSrcIp_Type()
)
ruijieLogSyslogSendSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLogSyslogSendSrcIp.setStatus("current")
_RuijieLogMIBConformance_ObjectIdentity = ObjectIdentity
ruijieLogMIBConformance = _RuijieLogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4)
)
_RuijieLogMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieLogMIBCompliances = _RuijieLogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 1)
)
_RuijieLogMIBGroups_ObjectIdentity = ObjectIdentity
ruijieLogMIBGroups = _RuijieLogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 2)
)

# Managed Objects groups

ruijieLogMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 2, 1)
)
ruijieLogMIBGroup.setObjects(
      *(("RUIJIE-LOG-MIB", "ruijieLogGlobalStatus"),
        ("RUIJIE-LOG-MIB", "ruijieLogSendConsoleStatus"),
        ("RUIJIE-LOG-MIB", "ruijieLogSendConsoleMaxSeverity"),
        ("RUIJIE-LOG-MIB", "ruijieLogSendMonitorStatus"),
        ("RUIJIE-LOG-MIB", "ruijieLogSendMonitorMaxSeverity"),
        ("RUIJIE-LOG-MIB", "ruijieLogSaveFileName"),
        ("RUIJIE-LOG-MIB", "ruijieLogFileMaxSeverity"),
        ("RUIJIE-LOG-MIB", "ruijieLogFileMaxSize"),
        ("RUIJIE-LOG-MIB", "ruijieLogSendBufferStatus"),
        ("RUIJIE-LOG-MIB", "ruijieLogSendBufferMaxSeverity"),
        ("RUIJIE-LOG-MIB", "ruijieLogClearBuffer"),
        ("RUIJIE-LOG-MIB", "ruijieLogHisRecordMaxNum"),
        ("RUIJIE-LOG-MIB", "ruijieLogHisIndex"),
        ("RUIJIE-LOG-MIB", "ruijieLogHisSeverity"),
        ("RUIJIE-LOG-MIB", "ruijieLogHisMsgName"),
        ("RUIJIE-LOG-MIB", "ruijieLogHisDescription"),
        ("RUIJIE-LOG-MIB", "ruijieLogHisTime"),
        ("RUIJIE-LOG-MIB", "ruijieLogSequenceGlobalStatus"),
        ("RUIJIE-LOG-MIB", "ruijieLogTimeStampGlobalStatus"),
        ("RUIJIE-LOG-MIB", "ruijieLogSyslogRelayGlobalStatus"),
        ("RUIJIE-LOG-MIB", "ruijieLogSyslogFacility"),
        ("RUIJIE-LOG-MIB", "ruijieLogSyslogSeverity"),
        ("RUIJIE-LOG-MIB", "ruijieLogSyslogServerIpAddr"),
        ("RUIJIE-LOG-MIB", "ruijieLogSyslogServerIpStatus"),
        ("RUIJIE-LOG-MIB", "ruijieLogSyslogSendSrcIfindex"),
        ("RUIJIE-LOG-MIB", "ruijieLogSyslogSendSrcIp"))
)
if mibBuilder.loadTexts:
    ruijieLogMIBGroup.setStatus("current")

ruijieLogHisStampsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 2, 2)
)
ruijieLogHisStampsMIBGroup.setObjects(
    ("RUIJIE-LOG-MIB", "ruijieLogHisStamps")
)
if mibBuilder.loadTexts:
    ruijieLogHisStampsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieLogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 4, 4, 1, 1)
)
ruijieLogMIBCompliance.setObjects(
      *(("RUIJIE-LOG-MIB", "ruijieLogMIBGroup"),
        ("RUIJIE-LOG-MIB", "ruijieLogHisStampsMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieLogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-LOG-MIB",
    **{"LogSeverity": LogSeverity,
       "LogTimeStamp": LogTimeStamp,
       "LogSyslogFacility": LogSyslogFacility,
       "ruijieLogMIB": ruijieLogMIB,
       "ruijieLogMIBObjects": ruijieLogMIBObjects,
       "ruijieLogGlobalStatus": ruijieLogGlobalStatus,
       "ruijieLogSendConsoleStatus": ruijieLogSendConsoleStatus,
       "ruijieLogSendConsoleMaxSeverity": ruijieLogSendConsoleMaxSeverity,
       "ruijieLogSendMonitorStatus": ruijieLogSendMonitorStatus,
       "ruijieLogSendMonitorMaxSeverity": ruijieLogSendMonitorMaxSeverity,
       "ruijieLogSaveFileName": ruijieLogSaveFileName,
       "ruijieLogFileMaxSeverity": ruijieLogFileMaxSeverity,
       "ruijieLogFileMaxSize": ruijieLogFileMaxSize,
       "ruijieLogSendBufferStatus": ruijieLogSendBufferStatus,
       "ruijieLogSendBufferMaxSeverity": ruijieLogSendBufferMaxSeverity,
       "ruijieLogClearBuffer": ruijieLogClearBuffer,
       "ruijieLogHisRecordMaxNum": ruijieLogHisRecordMaxNum,
       "ruijieLogHisTable": ruijieLogHisTable,
       "ruijieLogHisEntry": ruijieLogHisEntry,
       "ruijieLogHisIndex": ruijieLogHisIndex,
       "ruijieLogHisSeverity": ruijieLogHisSeverity,
       "ruijieLogHisMsgName": ruijieLogHisMsgName,
       "ruijieLogHisDescription": ruijieLogHisDescription,
       "ruijieLogHisTime": ruijieLogHisTime,
       "ruijieLogHisStamps": ruijieLogHisStamps,
       "ruijieLogSequenceGlobalStatus": ruijieLogSequenceGlobalStatus,
       "ruijieLogTimeStampGlobalStatus": ruijieLogTimeStampGlobalStatus,
       "ruijieLogSyslogRelayGlobalStatus": ruijieLogSyslogRelayGlobalStatus,
       "ruijieLogSyslogFacility": ruijieLogSyslogFacility,
       "ruijieLogSyslogSeverity": ruijieLogSyslogSeverity,
       "ruijieLogSyslogServerTable": ruijieLogSyslogServerTable,
       "ruijieLogSyslogServerEntry": ruijieLogSyslogServerEntry,
       "ruijieLogSyslogServerIpAddr": ruijieLogSyslogServerIpAddr,
       "ruijieLogSyslogServerIpStatus": ruijieLogSyslogServerIpStatus,
       "ruijieLogSyslogSendSrcIfindex": ruijieLogSyslogSendSrcIfindex,
       "ruijieLogSyslogSendSrcIp": ruijieLogSyslogSendSrcIp,
       "ruijieLogMIBConformance": ruijieLogMIBConformance,
       "ruijieLogMIBCompliances": ruijieLogMIBCompliances,
       "ruijieLogMIBCompliance": ruijieLogMIBCompliance,
       "ruijieLogMIBGroups": ruijieLogMIBGroups,
       "ruijieLogMIBGroup": ruijieLogMIBGroup,
       "ruijieLogHisStampsMIBGroup": ruijieLogHisStampsMIBGroup}
)
