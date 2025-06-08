# SNMP MIB module (CIE1000-AGGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-AGGR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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
 CIE1000InterfaceIndex,
 CIE1000PortList,
 CIE1000PortStatusSpeed,
 CIE1000RowEditorState) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InterfaceIndex",
    "CIE1000PortList",
    "CIE1000PortStatusSpeed",
    "CIE1000RowEditorState")

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

cie1000AggrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19)
)
if mibBuilder.loadTexts:
    cie1000AggrMib.setRevisions(
        ("2015-07-07 00:00",
         "2014-11-18 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cie1000AggrMibObjects_ObjectIdentity = ObjectIdentity
cie1000AggrMibObjects = _Cie1000AggrMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1)
)
_Cie1000AggrConfig_ObjectIdentity = ObjectIdentity
cie1000AggrConfig = _Cie1000AggrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2)
)
_Cie1000AggrConfigModeGlobals_ObjectIdentity = ObjectIdentity
cie1000AggrConfigModeGlobals = _Cie1000AggrConfigModeGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 1)
)
_Cie1000AggrConfigModeGlobalsSmacAddr_Type = TruthValue
_Cie1000AggrConfigModeGlobalsSmacAddr_Object = MibScalar
cie1000AggrConfigModeGlobalsSmacAddr = _Cie1000AggrConfigModeGlobalsSmacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 1, 1),
    _Cie1000AggrConfigModeGlobalsSmacAddr_Type()
)
cie1000AggrConfigModeGlobalsSmacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigModeGlobalsSmacAddr.setStatus("current")
_Cie1000AggrConfigModeGlobalsDmacAddr_Type = TruthValue
_Cie1000AggrConfigModeGlobalsDmacAddr_Object = MibScalar
cie1000AggrConfigModeGlobalsDmacAddr = _Cie1000AggrConfigModeGlobalsDmacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 1, 2),
    _Cie1000AggrConfigModeGlobalsDmacAddr_Type()
)
cie1000AggrConfigModeGlobalsDmacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigModeGlobalsDmacAddr.setStatus("current")
_Cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr_Type = TruthValue
_Cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr_Object = MibScalar
cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr = _Cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 1, 3),
    _Cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr_Type()
)
cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr.setStatus("current")
_Cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo_Type = TruthValue
_Cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo_Object = MibScalar
cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo = _Cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 1, 4),
    _Cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo_Type()
)
cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo.setStatus("current")
_Cie1000AggrConfigGroupTable_Object = MibTable
cie1000AggrConfigGroupTable = _Cie1000AggrConfigGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupTable.setStatus("current")
_Cie1000AggrConfigGroupEntry_Object = MibTableRow
cie1000AggrConfigGroupEntry = _Cie1000AggrConfigGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 2, 1)
)
cie1000AggrConfigGroupEntry.setIndexNames(
    (0, "CIE1000-AGGR-MIB", "cie1000AggrConfigGroupAggrIndexNo"),
)
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupEntry.setStatus("current")
_Cie1000AggrConfigGroupAggrIndexNo_Type = CIE1000InterfaceIndex
_Cie1000AggrConfigGroupAggrIndexNo_Object = MibTableColumn
cie1000AggrConfigGroupAggrIndexNo = _Cie1000AggrConfigGroupAggrIndexNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 2, 1, 1),
    _Cie1000AggrConfigGroupAggrIndexNo_Type()
)
cie1000AggrConfigGroupAggrIndexNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupAggrIndexNo.setStatus("current")
_Cie1000AggrConfigGroupPortMembers_Type = CIE1000PortList
_Cie1000AggrConfigGroupPortMembers_Object = MibTableColumn
cie1000AggrConfigGroupPortMembers = _Cie1000AggrConfigGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 2, 1, 2),
    _Cie1000AggrConfigGroupPortMembers_Type()
)
cie1000AggrConfigGroupPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupPortMembers.setStatus("current")
_Cie1000AggrConfigGroupAction_Type = CIE1000RowEditorState
_Cie1000AggrConfigGroupAction_Object = MibTableColumn
cie1000AggrConfigGroupAction = _Cie1000AggrConfigGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 2, 1, 100),
    _Cie1000AggrConfigGroupAction_Type()
)
cie1000AggrConfigGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupAction.setStatus("current")
_Cie1000AggrConfigGroupTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000AggrConfigGroupTableRowEditor = _Cie1000AggrConfigGroupTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 3)
)
_Cie1000AggrConfigGroupTableRowEditorAggrIndexNo_Type = CIE1000InterfaceIndex
_Cie1000AggrConfigGroupTableRowEditorAggrIndexNo_Object = MibScalar
cie1000AggrConfigGroupTableRowEditorAggrIndexNo = _Cie1000AggrConfigGroupTableRowEditorAggrIndexNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 3, 1),
    _Cie1000AggrConfigGroupTableRowEditorAggrIndexNo_Type()
)
cie1000AggrConfigGroupTableRowEditorAggrIndexNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupTableRowEditorAggrIndexNo.setStatus("current")
_Cie1000AggrConfigGroupTableRowEditorPortMembers_Type = CIE1000PortList
_Cie1000AggrConfigGroupTableRowEditorPortMembers_Object = MibScalar
cie1000AggrConfigGroupTableRowEditorPortMembers = _Cie1000AggrConfigGroupTableRowEditorPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 3, 2),
    _Cie1000AggrConfigGroupTableRowEditorPortMembers_Type()
)
cie1000AggrConfigGroupTableRowEditorPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupTableRowEditorPortMembers.setStatus("current")
_Cie1000AggrConfigGroupTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000AggrConfigGroupTableRowEditorAction_Object = MibScalar
cie1000AggrConfigGroupTableRowEditorAction = _Cie1000AggrConfigGroupTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 2, 3, 100),
    _Cie1000AggrConfigGroupTableRowEditorAction_Type()
)
cie1000AggrConfigGroupTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupTableRowEditorAction.setStatus("current")
_Cie1000AggrStatus_ObjectIdentity = ObjectIdentity
cie1000AggrStatus = _Cie1000AggrStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 3)
)
_Cie1000AggrStatusGroupTable_Object = MibTable
cie1000AggrStatusGroupTable = _Cie1000AggrStatusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000AggrStatusGroupTable.setStatus("current")
_Cie1000AggrStatusGroupEntry_Object = MibTableRow
cie1000AggrStatusGroupEntry = _Cie1000AggrStatusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 3, 1, 1)
)
cie1000AggrStatusGroupEntry.setIndexNames(
    (0, "CIE1000-AGGR-MIB", "cie1000AggrStatusGroupAggrIndexNo"),
)
if mibBuilder.loadTexts:
    cie1000AggrStatusGroupEntry.setStatus("current")
_Cie1000AggrStatusGroupAggrIndexNo_Type = CIE1000InterfaceIndex
_Cie1000AggrStatusGroupAggrIndexNo_Object = MibTableColumn
cie1000AggrStatusGroupAggrIndexNo = _Cie1000AggrStatusGroupAggrIndexNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 3, 1, 1, 1),
    _Cie1000AggrStatusGroupAggrIndexNo_Type()
)
cie1000AggrStatusGroupAggrIndexNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000AggrStatusGroupAggrIndexNo.setStatus("current")
_Cie1000AggrStatusGroupConfiguredPorts_Type = CIE1000PortList
_Cie1000AggrStatusGroupConfiguredPorts_Object = MibTableColumn
cie1000AggrStatusGroupConfiguredPorts = _Cie1000AggrStatusGroupConfiguredPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 3, 1, 1, 2),
    _Cie1000AggrStatusGroupConfiguredPorts_Type()
)
cie1000AggrStatusGroupConfiguredPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000AggrStatusGroupConfiguredPorts.setStatus("current")
_Cie1000AggrStatusGroupAggregatedPorts_Type = CIE1000PortList
_Cie1000AggrStatusGroupAggregatedPorts_Object = MibTableColumn
cie1000AggrStatusGroupAggregatedPorts = _Cie1000AggrStatusGroupAggregatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 3, 1, 1, 3),
    _Cie1000AggrStatusGroupAggregatedPorts_Type()
)
cie1000AggrStatusGroupAggregatedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000AggrStatusGroupAggregatedPorts.setStatus("current")
_Cie1000AggrStatusGroupSpeed_Type = CIE1000PortStatusSpeed
_Cie1000AggrStatusGroupSpeed_Object = MibTableColumn
cie1000AggrStatusGroupSpeed = _Cie1000AggrStatusGroupSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 3, 1, 1, 4),
    _Cie1000AggrStatusGroupSpeed_Type()
)
cie1000AggrStatusGroupSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000AggrStatusGroupSpeed.setStatus("current")


class _Cie1000AggrStatusGroupType_Type(CIE1000DisplayString):
    """Custom type cie1000AggrStatusGroupType based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Cie1000AggrStatusGroupType_Type.__name__ = "CIE1000DisplayString"
_Cie1000AggrStatusGroupType_Object = MibTableColumn
cie1000AggrStatusGroupType = _Cie1000AggrStatusGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 1, 3, 1, 1, 5),
    _Cie1000AggrStatusGroupType_Type()
)
cie1000AggrStatusGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000AggrStatusGroupType.setStatus("current")
_Cie1000AggrMibConformance_ObjectIdentity = ObjectIdentity
cie1000AggrMibConformance = _Cie1000AggrMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 2)
)
_Cie1000AggrMibCompliances_ObjectIdentity = ObjectIdentity
cie1000AggrMibCompliances = _Cie1000AggrMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 2, 1)
)
_Cie1000AggrMibGroups_ObjectIdentity = ObjectIdentity
cie1000AggrMibGroups = _Cie1000AggrMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 2, 2)
)

# Managed Objects groups

cie1000AggrConfigModeGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 2, 2, 1)
)
cie1000AggrConfigModeGlobalsInfoGroup.setObjects(
      *(("CIE1000-AGGR-MIB", "cie1000AggrConfigModeGlobalsSmacAddr"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigModeGlobalsDmacAddr"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo"))
)
if mibBuilder.loadTexts:
    cie1000AggrConfigModeGlobalsInfoGroup.setStatus("current")

cie1000AggrConfigGroupTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 2, 2, 2)
)
cie1000AggrConfigGroupTableInfoGroup.setObjects(
      *(("CIE1000-AGGR-MIB", "cie1000AggrConfigGroupAggrIndexNo"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigGroupPortMembers"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigGroupAction"))
)
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupTableInfoGroup.setStatus("current")

cie1000AggrConfigGroupTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 2, 2, 3)
)
cie1000AggrConfigGroupTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-AGGR-MIB", "cie1000AggrConfigGroupTableRowEditorAggrIndexNo"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigGroupTableRowEditorPortMembers"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigGroupTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000AggrConfigGroupTableRowEditorInfoGroup.setStatus("current")

cie1000AggrStatusGroupTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 2, 2, 4)
)
cie1000AggrStatusGroupTableInfoGroup.setObjects(
      *(("CIE1000-AGGR-MIB", "cie1000AggrStatusGroupAggrIndexNo"),
        ("CIE1000-AGGR-MIB", "cie1000AggrStatusGroupConfiguredPorts"),
        ("CIE1000-AGGR-MIB", "cie1000AggrStatusGroupAggregatedPorts"),
        ("CIE1000-AGGR-MIB", "cie1000AggrStatusGroupSpeed"),
        ("CIE1000-AGGR-MIB", "cie1000AggrStatusGroupType"))
)
if mibBuilder.loadTexts:
    cie1000AggrStatusGroupTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000AggrMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 19, 2, 1, 1)
)
cie1000AggrMibCompliance.setObjects(
      *(("CIE1000-AGGR-MIB", "cie1000AggrConfigModeGlobalsInfoGroup"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigGroupTableInfoGroup"),
        ("CIE1000-AGGR-MIB", "cie1000AggrConfigGroupTableRowEditorInfoGroup"),
        ("CIE1000-AGGR-MIB", "cie1000AggrStatusGroupTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000AggrMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-AGGR-MIB",
    **{"cie1000AggrMib": cie1000AggrMib,
       "cie1000AggrMibObjects": cie1000AggrMibObjects,
       "cie1000AggrConfig": cie1000AggrConfig,
       "cie1000AggrConfigModeGlobals": cie1000AggrConfigModeGlobals,
       "cie1000AggrConfigModeGlobalsSmacAddr": cie1000AggrConfigModeGlobalsSmacAddr,
       "cie1000AggrConfigModeGlobalsDmacAddr": cie1000AggrConfigModeGlobalsDmacAddr,
       "cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr": cie1000AggrConfigModeGlobalsSourceAndDestinationIpAddr,
       "cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo": cie1000AggrConfigModeGlobalsTcpOrUdpSportAndDportNo,
       "cie1000AggrConfigGroupTable": cie1000AggrConfigGroupTable,
       "cie1000AggrConfigGroupEntry": cie1000AggrConfigGroupEntry,
       "cie1000AggrConfigGroupAggrIndexNo": cie1000AggrConfigGroupAggrIndexNo,
       "cie1000AggrConfigGroupPortMembers": cie1000AggrConfigGroupPortMembers,
       "cie1000AggrConfigGroupAction": cie1000AggrConfigGroupAction,
       "cie1000AggrConfigGroupTableRowEditor": cie1000AggrConfigGroupTableRowEditor,
       "cie1000AggrConfigGroupTableRowEditorAggrIndexNo": cie1000AggrConfigGroupTableRowEditorAggrIndexNo,
       "cie1000AggrConfigGroupTableRowEditorPortMembers": cie1000AggrConfigGroupTableRowEditorPortMembers,
       "cie1000AggrConfigGroupTableRowEditorAction": cie1000AggrConfigGroupTableRowEditorAction,
       "cie1000AggrStatus": cie1000AggrStatus,
       "cie1000AggrStatusGroupTable": cie1000AggrStatusGroupTable,
       "cie1000AggrStatusGroupEntry": cie1000AggrStatusGroupEntry,
       "cie1000AggrStatusGroupAggrIndexNo": cie1000AggrStatusGroupAggrIndexNo,
       "cie1000AggrStatusGroupConfiguredPorts": cie1000AggrStatusGroupConfiguredPorts,
       "cie1000AggrStatusGroupAggregatedPorts": cie1000AggrStatusGroupAggregatedPorts,
       "cie1000AggrStatusGroupSpeed": cie1000AggrStatusGroupSpeed,
       "cie1000AggrStatusGroupType": cie1000AggrStatusGroupType,
       "cie1000AggrMibConformance": cie1000AggrMibConformance,
       "cie1000AggrMibCompliances": cie1000AggrMibCompliances,
       "cie1000AggrMibCompliance": cie1000AggrMibCompliance,
       "cie1000AggrMibGroups": cie1000AggrMibGroups,
       "cie1000AggrConfigModeGlobalsInfoGroup": cie1000AggrConfigModeGlobalsInfoGroup,
       "cie1000AggrConfigGroupTableInfoGroup": cie1000AggrConfigGroupTableInfoGroup,
       "cie1000AggrConfigGroupTableRowEditorInfoGroup": cie1000AggrConfigGroupTableRowEditorInfoGroup,
       "cie1000AggrStatusGroupTableInfoGroup": cie1000AggrStatusGroupTableInfoGroup}
)
