# SNMP MIB module (ME1200-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-SYSLOG-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,
 ME1200InetAddress) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InetAddress")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200SyslogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37)
)
if mibBuilder.loadTexts:
    me1200SyslogMib.setRevisions(
        ("2014-03-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200SyslogLevelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("all", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200SyslogMibObjects_ObjectIdentity = ObjectIdentity
me1200SyslogMibObjects = _Me1200SyslogMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1)
)
_Me1200SyslogConfig_ObjectIdentity = ObjectIdentity
me1200SyslogConfig = _Me1200SyslogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 2)
)
_Me1200SyslogConfigServer_ObjectIdentity = ObjectIdentity
me1200SyslogConfigServer = _Me1200SyslogConfigServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 2, 1)
)
_Me1200SyslogConfigServerMode_Type = TruthValue
_Me1200SyslogConfigServerMode_Object = MibScalar
me1200SyslogConfigServerMode = _Me1200SyslogConfigServerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 2, 1, 1),
    _Me1200SyslogConfigServerMode_Type()
)
me1200SyslogConfigServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SyslogConfigServerMode.setStatus("current")
_Me1200SyslogConfigServerAddress_Type = ME1200InetAddress
_Me1200SyslogConfigServerAddress_Object = MibScalar
me1200SyslogConfigServerAddress = _Me1200SyslogConfigServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 2, 1, 2),
    _Me1200SyslogConfigServerAddress_Type()
)
me1200SyslogConfigServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SyslogConfigServerAddress.setStatus("current")
_Me1200SyslogConfigServerLevel_Type = ME1200SyslogLevelType
_Me1200SyslogConfigServerLevel_Object = MibScalar
me1200SyslogConfigServerLevel = _Me1200SyslogConfigServerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 2, 1, 3),
    _Me1200SyslogConfigServerLevel_Type()
)
me1200SyslogConfigServerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SyslogConfigServerLevel.setStatus("current")
_Me1200SyslogStatus_ObjectIdentity = ObjectIdentity
me1200SyslogStatus = _Me1200SyslogStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 3)
)
_Me1200SyslogStatusHistoryTable_Object = MibTable
me1200SyslogStatusHistoryTable = _Me1200SyslogStatusHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200SyslogStatusHistoryTable.setStatus("current")
_Me1200SyslogStatusHistoryEntry_Object = MibTableRow
me1200SyslogStatusHistoryEntry = _Me1200SyslogStatusHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 3, 1, 1)
)
me1200SyslogStatusHistoryEntry.setIndexNames(
    (0, "ME1200-SYSLOG-MIB", "me1200SyslogStatusHistorySwitchId"),
    (0, "ME1200-SYSLOG-MIB", "me1200SyslogStatusHistoryMsgId"),
)
if mibBuilder.loadTexts:
    me1200SyslogStatusHistoryEntry.setStatus("current")


class _Me1200SyslogStatusHistorySwitchId_Type(Integer32):
    """Custom type me1200SyslogStatusHistorySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200SyslogStatusHistorySwitchId_Type.__name__ = "Integer32"
_Me1200SyslogStatusHistorySwitchId_Object = MibTableColumn
me1200SyslogStatusHistorySwitchId = _Me1200SyslogStatusHistorySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 3, 1, 1, 1),
    _Me1200SyslogStatusHistorySwitchId_Type()
)
me1200SyslogStatusHistorySwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SyslogStatusHistorySwitchId.setStatus("current")


class _Me1200SyslogStatusHistoryMsgId_Type(Integer32):
    """Custom type me1200SyslogStatusHistoryMsgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200SyslogStatusHistoryMsgId_Type.__name__ = "Integer32"
_Me1200SyslogStatusHistoryMsgId_Object = MibTableColumn
me1200SyslogStatusHistoryMsgId = _Me1200SyslogStatusHistoryMsgId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 3, 1, 1, 2),
    _Me1200SyslogStatusHistoryMsgId_Type()
)
me1200SyslogStatusHistoryMsgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SyslogStatusHistoryMsgId.setStatus("current")
_Me1200SyslogStatusHistoryMsgLevel_Type = ME1200SyslogLevelType
_Me1200SyslogStatusHistoryMsgLevel_Object = MibTableColumn
me1200SyslogStatusHistoryMsgLevel = _Me1200SyslogStatusHistoryMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 3, 1, 1, 3),
    _Me1200SyslogStatusHistoryMsgLevel_Type()
)
me1200SyslogStatusHistoryMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SyslogStatusHistoryMsgLevel.setStatus("current")
_Me1200SyslogStatusHistoryMsgTimeStamp_Type = DateAndTime
_Me1200SyslogStatusHistoryMsgTimeStamp_Object = MibTableColumn
me1200SyslogStatusHistoryMsgTimeStamp = _Me1200SyslogStatusHistoryMsgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 3, 1, 1, 4),
    _Me1200SyslogStatusHistoryMsgTimeStamp_Type()
)
me1200SyslogStatusHistoryMsgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SyslogStatusHistoryMsgTimeStamp.setStatus("current")


class _Me1200SyslogStatusHistoryMsgText_Type(ME1200DisplayString):
    """Custom type me1200SyslogStatusHistoryMsgText based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200SyslogStatusHistoryMsgText_Type.__name__ = "ME1200DisplayString"
_Me1200SyslogStatusHistoryMsgText_Object = MibTableColumn
me1200SyslogStatusHistoryMsgText = _Me1200SyslogStatusHistoryMsgText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 3, 1, 1, 5),
    _Me1200SyslogStatusHistoryMsgText_Type()
)
me1200SyslogStatusHistoryMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SyslogStatusHistoryMsgText.setStatus("current")
_Me1200SyslogControl_ObjectIdentity = ObjectIdentity
me1200SyslogControl = _Me1200SyslogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 4)
)
_Me1200SyslogControlHistoryTable_Object = MibTable
me1200SyslogControlHistoryTable = _Me1200SyslogControlHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 4, 1)
)
if mibBuilder.loadTexts:
    me1200SyslogControlHistoryTable.setStatus("current")
_Me1200SyslogControlHistoryEntry_Object = MibTableRow
me1200SyslogControlHistoryEntry = _Me1200SyslogControlHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 4, 1, 1)
)
me1200SyslogControlHistoryEntry.setIndexNames(
    (0, "ME1200-SYSLOG-MIB", "me1200SyslogControlHistorySwitchId"),
    (0, "ME1200-SYSLOG-MIB", "me1200SyslogControlHistoryClearLevel"),
)
if mibBuilder.loadTexts:
    me1200SyslogControlHistoryEntry.setStatus("current")


class _Me1200SyslogControlHistorySwitchId_Type(Integer32):
    """Custom type me1200SyslogControlHistorySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200SyslogControlHistorySwitchId_Type.__name__ = "Integer32"
_Me1200SyslogControlHistorySwitchId_Object = MibTableColumn
me1200SyslogControlHistorySwitchId = _Me1200SyslogControlHistorySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 4, 1, 1, 1),
    _Me1200SyslogControlHistorySwitchId_Type()
)
me1200SyslogControlHistorySwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SyslogControlHistorySwitchId.setStatus("current")
_Me1200SyslogControlHistoryClearLevel_Type = ME1200SyslogLevelType
_Me1200SyslogControlHistoryClearLevel_Object = MibTableColumn
me1200SyslogControlHistoryClearLevel = _Me1200SyslogControlHistoryClearLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 4, 1, 1, 2),
    _Me1200SyslogControlHistoryClearLevel_Type()
)
me1200SyslogControlHistoryClearLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SyslogControlHistoryClearLevel.setStatus("current")
_Me1200SyslogControlHistoryClear_Type = TruthValue
_Me1200SyslogControlHistoryClear_Object = MibTableColumn
me1200SyslogControlHistoryClear = _Me1200SyslogControlHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 1, 4, 1, 1, 3),
    _Me1200SyslogControlHistoryClear_Type()
)
me1200SyslogControlHistoryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SyslogControlHistoryClear.setStatus("current")
_Me1200SyslogMibConformance_ObjectIdentity = ObjectIdentity
me1200SyslogMibConformance = _Me1200SyslogMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 2)
)
_Me1200SyslogMibCompliances_ObjectIdentity = ObjectIdentity
me1200SyslogMibCompliances = _Me1200SyslogMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 2, 1)
)
_Me1200SyslogMibGroups_ObjectIdentity = ObjectIdentity
me1200SyslogMibGroups = _Me1200SyslogMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 2, 2)
)

# Managed Objects groups

me1200SyslogConfigServerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 2, 2, 1)
)
me1200SyslogConfigServerInfoGroup.setObjects(
      *(("ME1200-SYSLOG-MIB", "me1200SyslogConfigServerMode"),
        ("ME1200-SYSLOG-MIB", "me1200SyslogConfigServerAddress"),
        ("ME1200-SYSLOG-MIB", "me1200SyslogConfigServerLevel"))
)
if mibBuilder.loadTexts:
    me1200SyslogConfigServerInfoGroup.setStatus("current")

me1200SyslogStatusHistoryTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 2, 2, 2)
)
me1200SyslogStatusHistoryTableInfoGroup.setObjects(
      *(("ME1200-SYSLOG-MIB", "me1200SyslogStatusHistoryMsgLevel"),
        ("ME1200-SYSLOG-MIB", "me1200SyslogStatusHistoryMsgTimeStamp"),
        ("ME1200-SYSLOG-MIB", "me1200SyslogStatusHistoryMsgText"))
)
if mibBuilder.loadTexts:
    me1200SyslogStatusHistoryTableInfoGroup.setStatus("current")

me1200SyslogControlHistoryTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 2, 2, 3)
)
me1200SyslogControlHistoryTableInfoGroup.setObjects(
    ("ME1200-SYSLOG-MIB", "me1200SyslogControlHistoryClear")
)
if mibBuilder.loadTexts:
    me1200SyslogControlHistoryTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200SyslogMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 37, 2, 1, 1)
)
me1200SyslogMibCompliance.setObjects(
      *(("ME1200-SYSLOG-MIB", "me1200SyslogConfigServerInfoGroup"),
        ("ME1200-SYSLOG-MIB", "me1200SyslogStatusHistoryTableInfoGroup"),
        ("ME1200-SYSLOG-MIB", "me1200SyslogControlHistoryTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200SyslogMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-SYSLOG-MIB",
    **{"ME1200SyslogLevelType": ME1200SyslogLevelType,
       "me1200SyslogMib": me1200SyslogMib,
       "me1200SyslogMibObjects": me1200SyslogMibObjects,
       "me1200SyslogConfig": me1200SyslogConfig,
       "me1200SyslogConfigServer": me1200SyslogConfigServer,
       "me1200SyslogConfigServerMode": me1200SyslogConfigServerMode,
       "me1200SyslogConfigServerAddress": me1200SyslogConfigServerAddress,
       "me1200SyslogConfigServerLevel": me1200SyslogConfigServerLevel,
       "me1200SyslogStatus": me1200SyslogStatus,
       "me1200SyslogStatusHistoryTable": me1200SyslogStatusHistoryTable,
       "me1200SyslogStatusHistoryEntry": me1200SyslogStatusHistoryEntry,
       "me1200SyslogStatusHistorySwitchId": me1200SyslogStatusHistorySwitchId,
       "me1200SyslogStatusHistoryMsgId": me1200SyslogStatusHistoryMsgId,
       "me1200SyslogStatusHistoryMsgLevel": me1200SyslogStatusHistoryMsgLevel,
       "me1200SyslogStatusHistoryMsgTimeStamp": me1200SyslogStatusHistoryMsgTimeStamp,
       "me1200SyslogStatusHistoryMsgText": me1200SyslogStatusHistoryMsgText,
       "me1200SyslogControl": me1200SyslogControl,
       "me1200SyslogControlHistoryTable": me1200SyslogControlHistoryTable,
       "me1200SyslogControlHistoryEntry": me1200SyslogControlHistoryEntry,
       "me1200SyslogControlHistorySwitchId": me1200SyslogControlHistorySwitchId,
       "me1200SyslogControlHistoryClearLevel": me1200SyslogControlHistoryClearLevel,
       "me1200SyslogControlHistoryClear": me1200SyslogControlHistoryClear,
       "me1200SyslogMibConformance": me1200SyslogMibConformance,
       "me1200SyslogMibCompliances": me1200SyslogMibCompliances,
       "me1200SyslogMibCompliance": me1200SyslogMibCompliance,
       "me1200SyslogMibGroups": me1200SyslogMibGroups,
       "me1200SyslogConfigServerInfoGroup": me1200SyslogConfigServerInfoGroup,
       "me1200SyslogStatusHistoryTableInfoGroup": me1200SyslogStatusHistoryTableInfoGroup,
       "me1200SyslogControlHistoryTableInfoGroup": me1200SyslogControlHistoryTableInfoGroup}
)
