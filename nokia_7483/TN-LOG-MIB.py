# SNMP MIB module (TN-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-LOG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(SnmpAdminString,
 SnmpSecurityLevel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpSecurityLevel")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(TFilterActionOrDefault,) = mibBuilder.importSymbols(
    "TN-FILTER-MIB",
    "TFilterActionOrDefault")

(TNamedItem,) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TNamedItem")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnSRLogMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 12)
)
if mibBuilder.loadTexts:
    tnSRLogMIBModule.setRevisions(
        ("1912-12-05 00:00",
         "1909-02-28 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-15 00:00",
         "1905-01-24 00:00",
         "1904-05-27 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-11-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ItuPerceivedSeverity(TextualConvention, Integer32):
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
        ValueRangeConstraint(1, 10),
    )



class TmnxSyslogIdOrEmpty(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
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

_TnSRLogObjs_ObjectIdentity = ObjectIdentity
tnSRLogObjs = _TnSRLogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12)
)
_TnEventAppTable_Object = MibTable
tnEventAppTable = _TnEventAppTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9)
)
if mibBuilder.loadTexts:
    tnEventAppTable.setStatus("current")
_TnEventAppEntry_Object = MibTableRow
tnEventAppEntry = _TnEventAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1)
)
tnEventAppEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LOG-MIB", "tnEventAppIndex"),
)
if mibBuilder.loadTexts:
    tnEventAppEntry.setStatus("current")
_TnEventAppIndex_Type = Unsigned32
_TnEventAppIndex_Object = MibTableColumn
tnEventAppIndex = _TnEventAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1, 1),
    _TnEventAppIndex_Type()
)
tnEventAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEventAppIndex.setStatus("current")
_TnEventAppName_Type = TNamedItem
_TnEventAppName_Object = MibTableColumn
tnEventAppName = _TnEventAppName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1, 2),
    _TnEventAppName_Type()
)
tnEventAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEventAppName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LOG-MIB",
    **{"ItuPerceivedSeverity": ItuPerceivedSeverity,
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
       "tnSRLogMIBModule": tnSRLogMIBModule,
       "tnSRLogObjs": tnSRLogObjs,
       "tnEventAppTable": tnEventAppTable,
       "tnEventAppEntry": tnEventAppEntry,
       "tnEventAppIndex": tnEventAppIndex,
       "tnEventAppName": tnEventAppName}
)
