# SNMP MIB module (ME1200-AGGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-AGGR-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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
 ME1200InterfaceIndex,
 ME1200PortListStackable,
 ME1200RowEditorState) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
    "ME1200PortListStackable",
    "ME1200RowEditorState")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200AggrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19)
)
if mibBuilder.loadTexts:
    me1200AggrMib.setRevisions(
        ("2016-03-03 00:00",
         "2015-03-23 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2014-01-22 00:00",
         "2013-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200PortStatusSpeed(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("speed10M", 1),
          ("speed100M", 2),
          ("speed1G", 3),
          ("speed2G5", 4),
          ("speed5G", 5),
          ("speed10G", 6),
          ("speed12G", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200AggrMibObjects_ObjectIdentity = ObjectIdentity
me1200AggrMibObjects = _Me1200AggrMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1)
)
_Me1200AggrConfig_ObjectIdentity = ObjectIdentity
me1200AggrConfig = _Me1200AggrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2)
)
_Me1200AggrModeGlobals_ObjectIdentity = ObjectIdentity
me1200AggrModeGlobals = _Me1200AggrModeGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 1)
)
_Me1200AggrModeGlobalsSmacAddr_Type = TruthValue
_Me1200AggrModeGlobalsSmacAddr_Object = MibScalar
me1200AggrModeGlobalsSmacAddr = _Me1200AggrModeGlobalsSmacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 1, 1),
    _Me1200AggrModeGlobalsSmacAddr_Type()
)
me1200AggrModeGlobalsSmacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrModeGlobalsSmacAddr.setStatus("current")
_Me1200AggrModeGlobalsDmacAddr_Type = TruthValue
_Me1200AggrModeGlobalsDmacAddr_Object = MibScalar
me1200AggrModeGlobalsDmacAddr = _Me1200AggrModeGlobalsDmacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 1, 2),
    _Me1200AggrModeGlobalsDmacAddr_Type()
)
me1200AggrModeGlobalsDmacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrModeGlobalsDmacAddr.setStatus("current")
_Me1200AggrModeGlobalsSourceAndDestinationIpAddr_Type = TruthValue
_Me1200AggrModeGlobalsSourceAndDestinationIpAddr_Object = MibScalar
me1200AggrModeGlobalsSourceAndDestinationIpAddr = _Me1200AggrModeGlobalsSourceAndDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 1, 3),
    _Me1200AggrModeGlobalsSourceAndDestinationIpAddr_Type()
)
me1200AggrModeGlobalsSourceAndDestinationIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrModeGlobalsSourceAndDestinationIpAddr.setStatus("current")
_Me1200AggrModeGlobalsTcpOrUdpSportAndDportNo_Type = TruthValue
_Me1200AggrModeGlobalsTcpOrUdpSportAndDportNo_Object = MibScalar
me1200AggrModeGlobalsTcpOrUdpSportAndDportNo = _Me1200AggrModeGlobalsTcpOrUdpSportAndDportNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 1, 4),
    _Me1200AggrModeGlobalsTcpOrUdpSportAndDportNo_Type()
)
me1200AggrModeGlobalsTcpOrUdpSportAndDportNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrModeGlobalsTcpOrUdpSportAndDportNo.setStatus("current")
_Me1200AggrGroupConfigTable_Object = MibTable
me1200AggrGroupConfigTable = _Me1200AggrGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200AggrGroupConfigTable.setStatus("current")
_Me1200AggrGroupConfigEntry_Object = MibTableRow
me1200AggrGroupConfigEntry = _Me1200AggrGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 2, 1)
)
me1200AggrGroupConfigEntry.setIndexNames(
    (0, "ME1200-AGGR-MIB", "me1200AggrGroupConfigAggrIndexNo"),
)
if mibBuilder.loadTexts:
    me1200AggrGroupConfigEntry.setStatus("current")
_Me1200AggrGroupConfigAggrIndexNo_Type = ME1200InterfaceIndex
_Me1200AggrGroupConfigAggrIndexNo_Object = MibTableColumn
me1200AggrGroupConfigAggrIndexNo = _Me1200AggrGroupConfigAggrIndexNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 2, 1, 1),
    _Me1200AggrGroupConfigAggrIndexNo_Type()
)
me1200AggrGroupConfigAggrIndexNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AggrGroupConfigAggrIndexNo.setStatus("current")
_Me1200AggrGroupConfigPortMembers_Type = ME1200PortListStackable
_Me1200AggrGroupConfigPortMembers_Object = MibTableColumn
me1200AggrGroupConfigPortMembers = _Me1200AggrGroupConfigPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 2, 1, 2),
    _Me1200AggrGroupConfigPortMembers_Type()
)
me1200AggrGroupConfigPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrGroupConfigPortMembers.setStatus("current")
_Me1200AggrGroupConfigAction_Type = ME1200RowEditorState
_Me1200AggrGroupConfigAction_Object = MibTableColumn
me1200AggrGroupConfigAction = _Me1200AggrGroupConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 2, 1, 100),
    _Me1200AggrGroupConfigAction_Type()
)
me1200AggrGroupConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrGroupConfigAction.setStatus("current")
_Me1200AggrGroupConfigTableRowEditor_ObjectIdentity = ObjectIdentity
me1200AggrGroupConfigTableRowEditor = _Me1200AggrGroupConfigTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 3)
)
_Me1200AggrGroupConfigTableRowEditorAggrIndexNo_Type = ME1200InterfaceIndex
_Me1200AggrGroupConfigTableRowEditorAggrIndexNo_Object = MibScalar
me1200AggrGroupConfigTableRowEditorAggrIndexNo = _Me1200AggrGroupConfigTableRowEditorAggrIndexNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 3, 1),
    _Me1200AggrGroupConfigTableRowEditorAggrIndexNo_Type()
)
me1200AggrGroupConfigTableRowEditorAggrIndexNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrGroupConfigTableRowEditorAggrIndexNo.setStatus("current")
_Me1200AggrGroupConfigTableRowEditorPortMembers_Type = ME1200PortListStackable
_Me1200AggrGroupConfigTableRowEditorPortMembers_Object = MibScalar
me1200AggrGroupConfigTableRowEditorPortMembers = _Me1200AggrGroupConfigTableRowEditorPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 3, 2),
    _Me1200AggrGroupConfigTableRowEditorPortMembers_Type()
)
me1200AggrGroupConfigTableRowEditorPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrGroupConfigTableRowEditorPortMembers.setStatus("current")
_Me1200AggrGroupConfigTableRowEditorAction_Type = ME1200RowEditorState
_Me1200AggrGroupConfigTableRowEditorAction_Object = MibScalar
me1200AggrGroupConfigTableRowEditorAction = _Me1200AggrGroupConfigTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 2, 3, 100),
    _Me1200AggrGroupConfigTableRowEditorAction_Type()
)
me1200AggrGroupConfigTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AggrGroupConfigTableRowEditorAction.setStatus("current")
_Me1200AggrStatus_ObjectIdentity = ObjectIdentity
me1200AggrStatus = _Me1200AggrStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 3)
)
_Me1200AggrGroupStatusTable_Object = MibTable
me1200AggrGroupStatusTable = _Me1200AggrGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200AggrGroupStatusTable.setStatus("current")
_Me1200AggrGroupStatusEntry_Object = MibTableRow
me1200AggrGroupStatusEntry = _Me1200AggrGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 3, 3, 1)
)
me1200AggrGroupStatusEntry.setIndexNames(
    (0, "ME1200-AGGR-MIB", "me1200AggrGroupStatusAggrIndexNo"),
)
if mibBuilder.loadTexts:
    me1200AggrGroupStatusEntry.setStatus("current")
_Me1200AggrGroupStatusAggrIndexNo_Type = ME1200InterfaceIndex
_Me1200AggrGroupStatusAggrIndexNo_Object = MibTableColumn
me1200AggrGroupStatusAggrIndexNo = _Me1200AggrGroupStatusAggrIndexNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 3, 3, 1, 1),
    _Me1200AggrGroupStatusAggrIndexNo_Type()
)
me1200AggrGroupStatusAggrIndexNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AggrGroupStatusAggrIndexNo.setStatus("current")
_Me1200AggrGroupStatusConfiguredPorts_Type = ME1200PortListStackable
_Me1200AggrGroupStatusConfiguredPorts_Object = MibTableColumn
me1200AggrGroupStatusConfiguredPorts = _Me1200AggrGroupStatusConfiguredPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 3, 3, 1, 2),
    _Me1200AggrGroupStatusConfiguredPorts_Type()
)
me1200AggrGroupStatusConfiguredPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AggrGroupStatusConfiguredPorts.setStatus("current")
_Me1200AggrGroupStatusAggregatedPorts_Type = ME1200PortListStackable
_Me1200AggrGroupStatusAggregatedPorts_Object = MibTableColumn
me1200AggrGroupStatusAggregatedPorts = _Me1200AggrGroupStatusAggregatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 3, 3, 1, 3),
    _Me1200AggrGroupStatusAggregatedPorts_Type()
)
me1200AggrGroupStatusAggregatedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AggrGroupStatusAggregatedPorts.setStatus("current")
_Me1200AggrGroupStatusSpeed_Type = ME1200PortStatusSpeed
_Me1200AggrGroupStatusSpeed_Object = MibTableColumn
me1200AggrGroupStatusSpeed = _Me1200AggrGroupStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 3, 3, 1, 4),
    _Me1200AggrGroupStatusSpeed_Type()
)
me1200AggrGroupStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AggrGroupStatusSpeed.setStatus("current")


class _Me1200AggrGroupStatusType_Type(ME1200DisplayString):
    """Custom type me1200AggrGroupStatusType based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Me1200AggrGroupStatusType_Type.__name__ = "ME1200DisplayString"
_Me1200AggrGroupStatusType_Object = MibTableColumn
me1200AggrGroupStatusType = _Me1200AggrGroupStatusType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 3, 3, 1, 5),
    _Me1200AggrGroupStatusType_Type()
)
me1200AggrGroupStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AggrGroupStatusType.setStatus("current")
_Me1200AggrNotificationPrefix_ObjectIdentity = ObjectIdentity
me1200AggrNotificationPrefix = _Me1200AggrNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 5)
)
_Me1200AggrNotification_ObjectIdentity = ObjectIdentity
me1200AggrNotification = _Me1200AggrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 5, 0)
)
_Me1200AggrMibConformance_ObjectIdentity = ObjectIdentity
me1200AggrMibConformance = _Me1200AggrMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2)
)
_Me1200AggrMibCompliances_ObjectIdentity = ObjectIdentity
me1200AggrMibCompliances = _Me1200AggrMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2, 1)
)
_Me1200AggrMibGroups_ObjectIdentity = ObjectIdentity
me1200AggrMibGroups = _Me1200AggrMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2, 2)
)

# Managed Objects groups

me1200AggrModeGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2, 2, 1)
)
me1200AggrModeGlobalsInfoGroup.setObjects(
      *(("ME1200-AGGR-MIB", "me1200AggrModeGlobalsSmacAddr"),
        ("ME1200-AGGR-MIB", "me1200AggrModeGlobalsDmacAddr"),
        ("ME1200-AGGR-MIB", "me1200AggrModeGlobalsSourceAndDestinationIpAddr"),
        ("ME1200-AGGR-MIB", "me1200AggrModeGlobalsTcpOrUdpSportAndDportNo"))
)
if mibBuilder.loadTexts:
    me1200AggrModeGlobalsInfoGroup.setStatus("current")

me1200AggrGroupConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2, 2, 2)
)
me1200AggrGroupConfigTableInfoGroup.setObjects(
      *(("ME1200-AGGR-MIB", "me1200AggrGroupConfigPortMembers"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupConfigAction"))
)
if mibBuilder.loadTexts:
    me1200AggrGroupConfigTableInfoGroup.setStatus("current")

me1200AggrGroupConfigTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2, 2, 3)
)
me1200AggrGroupConfigTableRowEditorInfoGroup.setObjects(
      *(("ME1200-AGGR-MIB", "me1200AggrGroupConfigTableRowEditorAggrIndexNo"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupConfigTableRowEditorPortMembers"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupConfigTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200AggrGroupConfigTableRowEditorInfoGroup.setStatus("current")

me1200AggrGroupStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2, 2, 4)
)
me1200AggrGroupStatusTableInfoGroup.setObjects(
      *(("ME1200-AGGR-MIB", "me1200AggrGroupStatusConfiguredPorts"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupStatusAggregatedPorts"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupStatusSpeed"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupStatusType"))
)
if mibBuilder.loadTexts:
    me1200AggrGroupStatusTableInfoGroup.setStatus("current")


# Notification objects

me1200AggrNotificationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 1, 5, 0, 1)
)
me1200AggrNotificationChange.setObjects(
      *(("ME1200-AGGR-MIB", "me1200AggrGroupStatusConfiguredPorts"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupStatusAggregatedPorts"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupStatusSpeed"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupStatusType"))
)
if mibBuilder.loadTexts:
    me1200AggrNotificationChange.setStatus(
        "current"
    )


# Notifications groups

me1200AggrNotificationInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2, 2, 5)
)
me1200AggrNotificationInfoGroup.setObjects(
    ("ME1200-AGGR-MIB", "me1200AggrNotificationChange")
)
if mibBuilder.loadTexts:
    me1200AggrNotificationInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200AggrMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 19, 2, 1, 1)
)
me1200AggrMibCompliance.setObjects(
      *(("ME1200-AGGR-MIB", "me1200AggrModeGlobalsInfoGroup"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupConfigTableInfoGroup"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupConfigTableRowEditorInfoGroup"),
        ("ME1200-AGGR-MIB", "me1200AggrGroupStatusTableInfoGroup"),
        ("ME1200-AGGR-MIB", "me1200AggrNotificationInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200AggrMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-AGGR-MIB",
    **{"ME1200PortStatusSpeed": ME1200PortStatusSpeed,
       "me1200AggrMib": me1200AggrMib,
       "me1200AggrMibObjects": me1200AggrMibObjects,
       "me1200AggrConfig": me1200AggrConfig,
       "me1200AggrModeGlobals": me1200AggrModeGlobals,
       "me1200AggrModeGlobalsSmacAddr": me1200AggrModeGlobalsSmacAddr,
       "me1200AggrModeGlobalsDmacAddr": me1200AggrModeGlobalsDmacAddr,
       "me1200AggrModeGlobalsSourceAndDestinationIpAddr": me1200AggrModeGlobalsSourceAndDestinationIpAddr,
       "me1200AggrModeGlobalsTcpOrUdpSportAndDportNo": me1200AggrModeGlobalsTcpOrUdpSportAndDportNo,
       "me1200AggrGroupConfigTable": me1200AggrGroupConfigTable,
       "me1200AggrGroupConfigEntry": me1200AggrGroupConfigEntry,
       "me1200AggrGroupConfigAggrIndexNo": me1200AggrGroupConfigAggrIndexNo,
       "me1200AggrGroupConfigPortMembers": me1200AggrGroupConfigPortMembers,
       "me1200AggrGroupConfigAction": me1200AggrGroupConfigAction,
       "me1200AggrGroupConfigTableRowEditor": me1200AggrGroupConfigTableRowEditor,
       "me1200AggrGroupConfigTableRowEditorAggrIndexNo": me1200AggrGroupConfigTableRowEditorAggrIndexNo,
       "me1200AggrGroupConfigTableRowEditorPortMembers": me1200AggrGroupConfigTableRowEditorPortMembers,
       "me1200AggrGroupConfigTableRowEditorAction": me1200AggrGroupConfigTableRowEditorAction,
       "me1200AggrStatus": me1200AggrStatus,
       "me1200AggrGroupStatusTable": me1200AggrGroupStatusTable,
       "me1200AggrGroupStatusEntry": me1200AggrGroupStatusEntry,
       "me1200AggrGroupStatusAggrIndexNo": me1200AggrGroupStatusAggrIndexNo,
       "me1200AggrGroupStatusConfiguredPorts": me1200AggrGroupStatusConfiguredPorts,
       "me1200AggrGroupStatusAggregatedPorts": me1200AggrGroupStatusAggregatedPorts,
       "me1200AggrGroupStatusSpeed": me1200AggrGroupStatusSpeed,
       "me1200AggrGroupStatusType": me1200AggrGroupStatusType,
       "me1200AggrNotificationPrefix": me1200AggrNotificationPrefix,
       "me1200AggrNotification": me1200AggrNotification,
       "me1200AggrNotificationChange": me1200AggrNotificationChange,
       "me1200AggrMibConformance": me1200AggrMibConformance,
       "me1200AggrMibCompliances": me1200AggrMibCompliances,
       "me1200AggrMibCompliance": me1200AggrMibCompliance,
       "me1200AggrMibGroups": me1200AggrMibGroups,
       "me1200AggrModeGlobalsInfoGroup": me1200AggrModeGlobalsInfoGroup,
       "me1200AggrGroupConfigTableInfoGroup": me1200AggrGroupConfigTableInfoGroup,
       "me1200AggrGroupConfigTableRowEditorInfoGroup": me1200AggrGroupConfigTableRowEditorInfoGroup,
       "me1200AggrGroupStatusTableInfoGroup": me1200AggrGroupStatusTableInfoGroup,
       "me1200AggrNotificationInfoGroup": me1200AggrNotificationInfoGroup}
)
