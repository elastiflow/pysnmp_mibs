# SNMP MIB module (CIE1000-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-SYSLOG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000DisplayString,
 CIE1000InetAddress) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InetAddress")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

cie1000SyslogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37)
)
if mibBuilder.loadTexts:
    cie1000SyslogMib.setRevisions(
        ("2014-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000SyslogLevelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("all", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000SyslogMibObjects_ObjectIdentity = ObjectIdentity
cie1000SyslogMibObjects = _Cie1000SyslogMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1)
)
_Cie1000SyslogConfig_ObjectIdentity = ObjectIdentity
cie1000SyslogConfig = _Cie1000SyslogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 2)
)
_Cie1000SyslogConfigServer_ObjectIdentity = ObjectIdentity
cie1000SyslogConfigServer = _Cie1000SyslogConfigServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 2, 1)
)
_Cie1000SyslogConfigServerMode_Type = TruthValue
_Cie1000SyslogConfigServerMode_Object = MibScalar
cie1000SyslogConfigServerMode = _Cie1000SyslogConfigServerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 2, 1, 1),
    _Cie1000SyslogConfigServerMode_Type()
)
cie1000SyslogConfigServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SyslogConfigServerMode.setStatus("current")
_Cie1000SyslogConfigServerAddress_Type = CIE1000InetAddress
_Cie1000SyslogConfigServerAddress_Object = MibScalar
cie1000SyslogConfigServerAddress = _Cie1000SyslogConfigServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 2, 1, 2),
    _Cie1000SyslogConfigServerAddress_Type()
)
cie1000SyslogConfigServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SyslogConfigServerAddress.setStatus("current")
_Cie1000SyslogConfigServerLevel_Type = CIE1000SyslogLevelType
_Cie1000SyslogConfigServerLevel_Object = MibScalar
cie1000SyslogConfigServerLevel = _Cie1000SyslogConfigServerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 2, 1, 3),
    _Cie1000SyslogConfigServerLevel_Type()
)
cie1000SyslogConfigServerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SyslogConfigServerLevel.setStatus("current")
_Cie1000SyslogStatus_ObjectIdentity = ObjectIdentity
cie1000SyslogStatus = _Cie1000SyslogStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 3)
)
_Cie1000SyslogStatusHistoryTable_Object = MibTable
cie1000SyslogStatusHistoryTable = _Cie1000SyslogStatusHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000SyslogStatusHistoryTable.setStatus("current")
_Cie1000SyslogStatusHistoryEntry_Object = MibTableRow
cie1000SyslogStatusHistoryEntry = _Cie1000SyslogStatusHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 3, 1, 1)
)
cie1000SyslogStatusHistoryEntry.setIndexNames(
    (0, "CIE1000-SYSLOG-MIB", "cie1000SyslogStatusHistorySwitchId"),
    (0, "CIE1000-SYSLOG-MIB", "cie1000SyslogStatusHistoryMsgId"),
)
if mibBuilder.loadTexts:
    cie1000SyslogStatusHistoryEntry.setStatus("current")


class _Cie1000SyslogStatusHistorySwitchId_Type(Integer32):
    """Custom type cie1000SyslogStatusHistorySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000SyslogStatusHistorySwitchId_Type.__name__ = "Integer32"
_Cie1000SyslogStatusHistorySwitchId_Object = MibTableColumn
cie1000SyslogStatusHistorySwitchId = _Cie1000SyslogStatusHistorySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 3, 1, 1, 1),
    _Cie1000SyslogStatusHistorySwitchId_Type()
)
cie1000SyslogStatusHistorySwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SyslogStatusHistorySwitchId.setStatus("current")


class _Cie1000SyslogStatusHistoryMsgId_Type(Integer32):
    """Custom type cie1000SyslogStatusHistoryMsgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000SyslogStatusHistoryMsgId_Type.__name__ = "Integer32"
_Cie1000SyslogStatusHistoryMsgId_Object = MibTableColumn
cie1000SyslogStatusHistoryMsgId = _Cie1000SyslogStatusHistoryMsgId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 3, 1, 1, 2),
    _Cie1000SyslogStatusHistoryMsgId_Type()
)
cie1000SyslogStatusHistoryMsgId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SyslogStatusHistoryMsgId.setStatus("current")
_Cie1000SyslogStatusHistoryMsgLevel_Type = CIE1000SyslogLevelType
_Cie1000SyslogStatusHistoryMsgLevel_Object = MibTableColumn
cie1000SyslogStatusHistoryMsgLevel = _Cie1000SyslogStatusHistoryMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 3, 1, 1, 3),
    _Cie1000SyslogStatusHistoryMsgLevel_Type()
)
cie1000SyslogStatusHistoryMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SyslogStatusHistoryMsgLevel.setStatus("current")
_Cie1000SyslogStatusHistoryMsgTimeStamp_Type = DateAndTime
_Cie1000SyslogStatusHistoryMsgTimeStamp_Object = MibTableColumn
cie1000SyslogStatusHistoryMsgTimeStamp = _Cie1000SyslogStatusHistoryMsgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 3, 1, 1, 4),
    _Cie1000SyslogStatusHistoryMsgTimeStamp_Type()
)
cie1000SyslogStatusHistoryMsgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SyslogStatusHistoryMsgTimeStamp.setStatus("current")


class _Cie1000SyslogStatusHistoryMsgText_Type(CIE1000DisplayString):
    """Custom type cie1000SyslogStatusHistoryMsgText based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4000),
    )


_Cie1000SyslogStatusHistoryMsgText_Type.__name__ = "CIE1000DisplayString"
_Cie1000SyslogStatusHistoryMsgText_Object = MibTableColumn
cie1000SyslogStatusHistoryMsgText = _Cie1000SyslogStatusHistoryMsgText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 3, 1, 1, 5),
    _Cie1000SyslogStatusHistoryMsgText_Type()
)
cie1000SyslogStatusHistoryMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000SyslogStatusHistoryMsgText.setStatus("current")
_Cie1000SyslogControl_ObjectIdentity = ObjectIdentity
cie1000SyslogControl = _Cie1000SyslogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 4)
)
_Cie1000SyslogControlHistoryTable_Object = MibTable
cie1000SyslogControlHistoryTable = _Cie1000SyslogControlHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cie1000SyslogControlHistoryTable.setStatus("current")
_Cie1000SyslogControlHistoryEntry_Object = MibTableRow
cie1000SyslogControlHistoryEntry = _Cie1000SyslogControlHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 4, 1, 1)
)
cie1000SyslogControlHistoryEntry.setIndexNames(
    (0, "CIE1000-SYSLOG-MIB", "cie1000SyslogControlHistorySwitchId"),
    (0, "CIE1000-SYSLOG-MIB", "cie1000SyslogControlHistoryClearLevel"),
)
if mibBuilder.loadTexts:
    cie1000SyslogControlHistoryEntry.setStatus("current")


class _Cie1000SyslogControlHistorySwitchId_Type(Integer32):
    """Custom type cie1000SyslogControlHistorySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000SyslogControlHistorySwitchId_Type.__name__ = "Integer32"
_Cie1000SyslogControlHistorySwitchId_Object = MibTableColumn
cie1000SyslogControlHistorySwitchId = _Cie1000SyslogControlHistorySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 4, 1, 1, 1),
    _Cie1000SyslogControlHistorySwitchId_Type()
)
cie1000SyslogControlHistorySwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SyslogControlHistorySwitchId.setStatus("current")
_Cie1000SyslogControlHistoryClearLevel_Type = CIE1000SyslogLevelType
_Cie1000SyslogControlHistoryClearLevel_Object = MibTableColumn
cie1000SyslogControlHistoryClearLevel = _Cie1000SyslogControlHistoryClearLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 4, 1, 1, 2),
    _Cie1000SyslogControlHistoryClearLevel_Type()
)
cie1000SyslogControlHistoryClearLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SyslogControlHistoryClearLevel.setStatus("current")
_Cie1000SyslogControlHistoryClear_Type = TruthValue
_Cie1000SyslogControlHistoryClear_Object = MibTableColumn
cie1000SyslogControlHistoryClear = _Cie1000SyslogControlHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 1, 4, 1, 1, 3),
    _Cie1000SyslogControlHistoryClear_Type()
)
cie1000SyslogControlHistoryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SyslogControlHistoryClear.setStatus("current")
_Cie1000SyslogMibConformance_ObjectIdentity = ObjectIdentity
cie1000SyslogMibConformance = _Cie1000SyslogMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 2)
)
_Cie1000SyslogMibCompliances_ObjectIdentity = ObjectIdentity
cie1000SyslogMibCompliances = _Cie1000SyslogMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 2, 1)
)
_Cie1000SyslogMibGroups_ObjectIdentity = ObjectIdentity
cie1000SyslogMibGroups = _Cie1000SyslogMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 2, 2)
)

# Managed Objects groups

cie1000SyslogConfigServerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 2, 2, 1)
)
cie1000SyslogConfigServerInfoGroup.setObjects(
      *(("CIE1000-SYSLOG-MIB", "cie1000SyslogConfigServerMode"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogConfigServerAddress"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogConfigServerLevel"))
)
if mibBuilder.loadTexts:
    cie1000SyslogConfigServerInfoGroup.setStatus("current")

cie1000SyslogStatusHistoryTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 2, 2, 2)
)
cie1000SyslogStatusHistoryTableInfoGroup.setObjects(
      *(("CIE1000-SYSLOG-MIB", "cie1000SyslogStatusHistorySwitchId"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogStatusHistoryMsgId"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogStatusHistoryMsgLevel"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogStatusHistoryMsgTimeStamp"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogStatusHistoryMsgText"))
)
if mibBuilder.loadTexts:
    cie1000SyslogStatusHistoryTableInfoGroup.setStatus("current")

cie1000SyslogControlHistoryTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 2, 2, 3)
)
cie1000SyslogControlHistoryTableInfoGroup.setObjects(
      *(("CIE1000-SYSLOG-MIB", "cie1000SyslogControlHistorySwitchId"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogControlHistoryClearLevel"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogControlHistoryClear"))
)
if mibBuilder.loadTexts:
    cie1000SyslogControlHistoryTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000SyslogMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 37, 2, 1, 1)
)
cie1000SyslogMibCompliance.setObjects(
      *(("CIE1000-SYSLOG-MIB", "cie1000SyslogConfigServerInfoGroup"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogStatusHistoryTableInfoGroup"),
        ("CIE1000-SYSLOG-MIB", "cie1000SyslogControlHistoryTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000SyslogMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-SYSLOG-MIB",
    **{"CIE1000SyslogLevelType": CIE1000SyslogLevelType,
       "cie1000SyslogMib": cie1000SyslogMib,
       "cie1000SyslogMibObjects": cie1000SyslogMibObjects,
       "cie1000SyslogConfig": cie1000SyslogConfig,
       "cie1000SyslogConfigServer": cie1000SyslogConfigServer,
       "cie1000SyslogConfigServerMode": cie1000SyslogConfigServerMode,
       "cie1000SyslogConfigServerAddress": cie1000SyslogConfigServerAddress,
       "cie1000SyslogConfigServerLevel": cie1000SyslogConfigServerLevel,
       "cie1000SyslogStatus": cie1000SyslogStatus,
       "cie1000SyslogStatusHistoryTable": cie1000SyslogStatusHistoryTable,
       "cie1000SyslogStatusHistoryEntry": cie1000SyslogStatusHistoryEntry,
       "cie1000SyslogStatusHistorySwitchId": cie1000SyslogStatusHistorySwitchId,
       "cie1000SyslogStatusHistoryMsgId": cie1000SyslogStatusHistoryMsgId,
       "cie1000SyslogStatusHistoryMsgLevel": cie1000SyslogStatusHistoryMsgLevel,
       "cie1000SyslogStatusHistoryMsgTimeStamp": cie1000SyslogStatusHistoryMsgTimeStamp,
       "cie1000SyslogStatusHistoryMsgText": cie1000SyslogStatusHistoryMsgText,
       "cie1000SyslogControl": cie1000SyslogControl,
       "cie1000SyslogControlHistoryTable": cie1000SyslogControlHistoryTable,
       "cie1000SyslogControlHistoryEntry": cie1000SyslogControlHistoryEntry,
       "cie1000SyslogControlHistorySwitchId": cie1000SyslogControlHistorySwitchId,
       "cie1000SyslogControlHistoryClearLevel": cie1000SyslogControlHistoryClearLevel,
       "cie1000SyslogControlHistoryClear": cie1000SyslogControlHistoryClear,
       "cie1000SyslogMibConformance": cie1000SyslogMibConformance,
       "cie1000SyslogMibCompliances": cie1000SyslogMibCompliances,
       "cie1000SyslogMibCompliance": cie1000SyslogMibCompliance,
       "cie1000SyslogMibGroups": cie1000SyslogMibGroups,
       "cie1000SyslogConfigServerInfoGroup": cie1000SyslogConfigServerInfoGroup,
       "cie1000SyslogStatusHistoryTableInfoGroup": cie1000SyslogStatusHistoryTableInfoGroup,
       "cie1000SyslogControlHistoryTableInfoGroup": cie1000SyslogControlHistoryTableInfoGroup}
)
