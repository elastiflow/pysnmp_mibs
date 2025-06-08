# SNMP MIB module (CIE1000-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-ALARM-MIB.mib
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
 CIE1000RowEditorState) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
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

cie1000AlarmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136)
)
if mibBuilder.loadTexts:
    cie1000AlarmMib.setRevisions(
        ("2016-02-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cie1000AlarmMibObjects_ObjectIdentity = ObjectIdentity
cie1000AlarmMibObjects = _Cie1000AlarmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1)
)
_Cie1000AlarmConfig_ObjectIdentity = ObjectIdentity
cie1000AlarmConfig = _Cie1000AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2)
)
_Cie1000AlarmConfigTable_Object = MibTable
cie1000AlarmConfigTable = _Cie1000AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000AlarmConfigTable.setStatus("current")
_Cie1000AlarmConfigEntry_Object = MibTableRow
cie1000AlarmConfigEntry = _Cie1000AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 1, 1)
)
cie1000AlarmConfigEntry.setIndexNames(
    (0, "CIE1000-ALARM-MIB", "cie1000AlarmConfigAlarmName"),
)
if mibBuilder.loadTexts:
    cie1000AlarmConfigEntry.setStatus("current")


class _Cie1000AlarmConfigAlarmName_Type(CIE1000DisplayString):
    """Custom type cie1000AlarmConfigAlarmName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Cie1000AlarmConfigAlarmName_Type.__name__ = "CIE1000DisplayString"
_Cie1000AlarmConfigAlarmName_Object = MibTableColumn
cie1000AlarmConfigAlarmName = _Cie1000AlarmConfigAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 1, 1, 1),
    _Cie1000AlarmConfigAlarmName_Type()
)
cie1000AlarmConfigAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000AlarmConfigAlarmName.setStatus("current")


class _Cie1000AlarmConfigExpression_Type(CIE1000DisplayString):
    """Custom type cie1000AlarmConfigExpression based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_Cie1000AlarmConfigExpression_Type.__name__ = "CIE1000DisplayString"
_Cie1000AlarmConfigExpression_Object = MibTableColumn
cie1000AlarmConfigExpression = _Cie1000AlarmConfigExpression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 1, 1, 2),
    _Cie1000AlarmConfigExpression_Type()
)
cie1000AlarmConfigExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AlarmConfigExpression.setStatus("current")
_Cie1000AlarmConfigAction_Type = CIE1000RowEditorState
_Cie1000AlarmConfigAction_Object = MibTableColumn
cie1000AlarmConfigAction = _Cie1000AlarmConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 1, 1, 100),
    _Cie1000AlarmConfigAction_Type()
)
cie1000AlarmConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AlarmConfigAction.setStatus("current")
_Cie1000AlarmConfigTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000AlarmConfigTableRowEditor = _Cie1000AlarmConfigTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 2)
)


class _Cie1000AlarmConfigTableRowEditorAlarmName_Type(CIE1000DisplayString):
    """Custom type cie1000AlarmConfigTableRowEditorAlarmName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Cie1000AlarmConfigTableRowEditorAlarmName_Type.__name__ = "CIE1000DisplayString"
_Cie1000AlarmConfigTableRowEditorAlarmName_Object = MibScalar
cie1000AlarmConfigTableRowEditorAlarmName = _Cie1000AlarmConfigTableRowEditorAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 2, 1),
    _Cie1000AlarmConfigTableRowEditorAlarmName_Type()
)
cie1000AlarmConfigTableRowEditorAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AlarmConfigTableRowEditorAlarmName.setStatus("current")


class _Cie1000AlarmConfigTableRowEditorExpression_Type(CIE1000DisplayString):
    """Custom type cie1000AlarmConfigTableRowEditorExpression based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_Cie1000AlarmConfigTableRowEditorExpression_Type.__name__ = "CIE1000DisplayString"
_Cie1000AlarmConfigTableRowEditorExpression_Object = MibScalar
cie1000AlarmConfigTableRowEditorExpression = _Cie1000AlarmConfigTableRowEditorExpression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 2, 2),
    _Cie1000AlarmConfigTableRowEditorExpression_Type()
)
cie1000AlarmConfigTableRowEditorExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AlarmConfigTableRowEditorExpression.setStatus("current")
_Cie1000AlarmConfigTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000AlarmConfigTableRowEditorAction_Object = MibScalar
cie1000AlarmConfigTableRowEditorAction = _Cie1000AlarmConfigTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 2, 2, 100),
    _Cie1000AlarmConfigTableRowEditorAction_Type()
)
cie1000AlarmConfigTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AlarmConfigTableRowEditorAction.setStatus("current")
_Cie1000AlarmStatus_ObjectIdentity = ObjectIdentity
cie1000AlarmStatus = _Cie1000AlarmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 3)
)
_Cie1000AlarmStatusTable_Object = MibTable
cie1000AlarmStatusTable = _Cie1000AlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000AlarmStatusTable.setStatus("current")
_Cie1000AlarmStatusEntry_Object = MibTableRow
cie1000AlarmStatusEntry = _Cie1000AlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 3, 1, 1)
)
cie1000AlarmStatusEntry.setIndexNames(
    (0, "CIE1000-ALARM-MIB", "cie1000AlarmStatusAlarmName"),
)
if mibBuilder.loadTexts:
    cie1000AlarmStatusEntry.setStatus("current")


class _Cie1000AlarmStatusAlarmName_Type(CIE1000DisplayString):
    """Custom type cie1000AlarmStatusAlarmName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Cie1000AlarmStatusAlarmName_Type.__name__ = "CIE1000DisplayString"
_Cie1000AlarmStatusAlarmName_Object = MibTableColumn
cie1000AlarmStatusAlarmName = _Cie1000AlarmStatusAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 3, 1, 1, 1),
    _Cie1000AlarmStatusAlarmName_Type()
)
cie1000AlarmStatusAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000AlarmStatusAlarmName.setStatus("current")
_Cie1000AlarmStatusSuppressed_Type = TruthValue
_Cie1000AlarmStatusSuppressed_Object = MibTableColumn
cie1000AlarmStatusSuppressed = _Cie1000AlarmStatusSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 3, 1, 1, 2),
    _Cie1000AlarmStatusSuppressed_Type()
)
cie1000AlarmStatusSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000AlarmStatusSuppressed.setStatus("current")
_Cie1000AlarmStatusActive_Type = TruthValue
_Cie1000AlarmStatusActive_Object = MibTableColumn
cie1000AlarmStatusActive = _Cie1000AlarmStatusActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 3, 1, 1, 3),
    _Cie1000AlarmStatusActive_Type()
)
cie1000AlarmStatusActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000AlarmStatusActive.setStatus("current")
_Cie1000AlarmStatusExposedActive_Type = TruthValue
_Cie1000AlarmStatusExposedActive_Object = MibTableColumn
cie1000AlarmStatusExposedActive = _Cie1000AlarmStatusExposedActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 3, 1, 1, 4),
    _Cie1000AlarmStatusExposedActive_Type()
)
cie1000AlarmStatusExposedActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000AlarmStatusExposedActive.setStatus("current")
_Cie1000AlarmControl_ObjectIdentity = ObjectIdentity
cie1000AlarmControl = _Cie1000AlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 4)
)
_Cie1000AlarmControlTable_Object = MibTable
cie1000AlarmControlTable = _Cie1000AlarmControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cie1000AlarmControlTable.setStatus("current")
_Cie1000AlarmControlEntry_Object = MibTableRow
cie1000AlarmControlEntry = _Cie1000AlarmControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 4, 1, 1)
)
cie1000AlarmControlEntry.setIndexNames(
    (0, "CIE1000-ALARM-MIB", "cie1000AlarmControlAlarmName"),
)
if mibBuilder.loadTexts:
    cie1000AlarmControlEntry.setStatus("current")


class _Cie1000AlarmControlAlarmName_Type(CIE1000DisplayString):
    """Custom type cie1000AlarmControlAlarmName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Cie1000AlarmControlAlarmName_Type.__name__ = "CIE1000DisplayString"
_Cie1000AlarmControlAlarmName_Object = MibTableColumn
cie1000AlarmControlAlarmName = _Cie1000AlarmControlAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 4, 1, 1, 1),
    _Cie1000AlarmControlAlarmName_Type()
)
cie1000AlarmControlAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000AlarmControlAlarmName.setStatus("current")
_Cie1000AlarmControlSuppress_Type = TruthValue
_Cie1000AlarmControlSuppress_Object = MibTableColumn
cie1000AlarmControlSuppress = _Cie1000AlarmControlSuppress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 4, 1, 1, 2),
    _Cie1000AlarmControlSuppress_Type()
)
cie1000AlarmControlSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000AlarmControlSuppress.setStatus("current")
_Cie1000AlarmTrap_ObjectIdentity = ObjectIdentity
cie1000AlarmTrap = _Cie1000AlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 6)
)
_Cie1000AlarmMibConformance_ObjectIdentity = ObjectIdentity
cie1000AlarmMibConformance = _Cie1000AlarmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2)
)
_Cie1000AlarmMibCompliances_ObjectIdentity = ObjectIdentity
cie1000AlarmMibCompliances = _Cie1000AlarmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 1)
)
_Cie1000AlarmMibGroups_ObjectIdentity = ObjectIdentity
cie1000AlarmMibGroups = _Cie1000AlarmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 2)
)

# Managed Objects groups

cie1000AlarmConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 2, 1)
)
cie1000AlarmConfigTableInfoGroup.setObjects(
      *(("CIE1000-ALARM-MIB", "cie1000AlarmConfigAlarmName"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmConfigExpression"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmConfigAction"))
)
if mibBuilder.loadTexts:
    cie1000AlarmConfigTableInfoGroup.setStatus("current")

cie1000AlarmConfigTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 2, 2)
)
cie1000AlarmConfigTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-ALARM-MIB", "cie1000AlarmConfigTableRowEditorAlarmName"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmConfigTableRowEditorExpression"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmConfigTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000AlarmConfigTableRowEditorInfoGroup.setStatus("current")

cie1000AlarmStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 2, 3)
)
cie1000AlarmStatusInfoGroup.setObjects(
      *(("CIE1000-ALARM-MIB", "cie1000AlarmStatusAlarmName"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusSuppressed"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusActive"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusExposedActive"))
)
if mibBuilder.loadTexts:
    cie1000AlarmStatusInfoGroup.setStatus("current")

cie1000AlarmControlTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 2, 4)
)
cie1000AlarmControlTableInfoGroup.setObjects(
      *(("CIE1000-ALARM-MIB", "cie1000AlarmControlAlarmName"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmControlSuppress"))
)
if mibBuilder.loadTexts:
    cie1000AlarmControlTableInfoGroup.setStatus("current")


# Notification objects

cie1000AlarmTrapStatusAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 6, 1)
)
cie1000AlarmTrapStatusAdd.setObjects(
      *(("CIE1000-ALARM-MIB", "cie1000AlarmStatusAlarmName"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusSuppressed"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusActive"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusExposedActive"))
)
if mibBuilder.loadTexts:
    cie1000AlarmTrapStatusAdd.setStatus(
        "current"
    )

cie1000AlarmTrapStatusMod = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 6, 2)
)
cie1000AlarmTrapStatusMod.setObjects(
      *(("CIE1000-ALARM-MIB", "cie1000AlarmStatusAlarmName"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusSuppressed"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusActive"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusExposedActive"))
)
if mibBuilder.loadTexts:
    cie1000AlarmTrapStatusMod.setStatus(
        "current"
    )

cie1000AlarmTrapStatusDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 1, 6, 3)
)
cie1000AlarmTrapStatusDel.setObjects(
    ("CIE1000-ALARM-MIB", "cie1000AlarmStatusAlarmName")
)
if mibBuilder.loadTexts:
    cie1000AlarmTrapStatusDel.setStatus(
        "current"
    )


# Notifications groups

cie1000AlarmTrapStatusAddInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 2, 5)
)
cie1000AlarmTrapStatusAddInfoGroup.setObjects(
    ("CIE1000-ALARM-MIB", "cie1000AlarmTrapStatusAdd")
)
if mibBuilder.loadTexts:
    cie1000AlarmTrapStatusAddInfoGroup.setStatus(
        "current"
    )

cie1000AlarmTrapStatusModInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 2, 6)
)
cie1000AlarmTrapStatusModInfoGroup.setObjects(
    ("CIE1000-ALARM-MIB", "cie1000AlarmTrapStatusMod")
)
if mibBuilder.loadTexts:
    cie1000AlarmTrapStatusModInfoGroup.setStatus(
        "current"
    )

cie1000AlarmTrapStatusDelInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 2, 7)
)
cie1000AlarmTrapStatusDelInfoGroup.setObjects(
    ("CIE1000-ALARM-MIB", "cie1000AlarmTrapStatusDel")
)
if mibBuilder.loadTexts:
    cie1000AlarmTrapStatusDelInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cie1000AlarmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 136, 2, 1, 1)
)
cie1000AlarmMibCompliance.setObjects(
      *(("CIE1000-ALARM-MIB", "cie1000AlarmConfigTableInfoGroup"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmConfigTableRowEditorInfoGroup"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmStatusInfoGroup"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmControlTableInfoGroup"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmTrapStatusAddInfoGroup"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmTrapStatusModInfoGroup"),
        ("CIE1000-ALARM-MIB", "cie1000AlarmTrapStatusDelInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000AlarmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-ALARM-MIB",
    **{"cie1000AlarmMib": cie1000AlarmMib,
       "cie1000AlarmMibObjects": cie1000AlarmMibObjects,
       "cie1000AlarmConfig": cie1000AlarmConfig,
       "cie1000AlarmConfigTable": cie1000AlarmConfigTable,
       "cie1000AlarmConfigEntry": cie1000AlarmConfigEntry,
       "cie1000AlarmConfigAlarmName": cie1000AlarmConfigAlarmName,
       "cie1000AlarmConfigExpression": cie1000AlarmConfigExpression,
       "cie1000AlarmConfigAction": cie1000AlarmConfigAction,
       "cie1000AlarmConfigTableRowEditor": cie1000AlarmConfigTableRowEditor,
       "cie1000AlarmConfigTableRowEditorAlarmName": cie1000AlarmConfigTableRowEditorAlarmName,
       "cie1000AlarmConfigTableRowEditorExpression": cie1000AlarmConfigTableRowEditorExpression,
       "cie1000AlarmConfigTableRowEditorAction": cie1000AlarmConfigTableRowEditorAction,
       "cie1000AlarmStatus": cie1000AlarmStatus,
       "cie1000AlarmStatusTable": cie1000AlarmStatusTable,
       "cie1000AlarmStatusEntry": cie1000AlarmStatusEntry,
       "cie1000AlarmStatusAlarmName": cie1000AlarmStatusAlarmName,
       "cie1000AlarmStatusSuppressed": cie1000AlarmStatusSuppressed,
       "cie1000AlarmStatusActive": cie1000AlarmStatusActive,
       "cie1000AlarmStatusExposedActive": cie1000AlarmStatusExposedActive,
       "cie1000AlarmControl": cie1000AlarmControl,
       "cie1000AlarmControlTable": cie1000AlarmControlTable,
       "cie1000AlarmControlEntry": cie1000AlarmControlEntry,
       "cie1000AlarmControlAlarmName": cie1000AlarmControlAlarmName,
       "cie1000AlarmControlSuppress": cie1000AlarmControlSuppress,
       "cie1000AlarmTrap": cie1000AlarmTrap,
       "cie1000AlarmTrapStatusAdd": cie1000AlarmTrapStatusAdd,
       "cie1000AlarmTrapStatusMod": cie1000AlarmTrapStatusMod,
       "cie1000AlarmTrapStatusDel": cie1000AlarmTrapStatusDel,
       "cie1000AlarmMibConformance": cie1000AlarmMibConformance,
       "cie1000AlarmMibCompliances": cie1000AlarmMibCompliances,
       "cie1000AlarmMibCompliance": cie1000AlarmMibCompliance,
       "cie1000AlarmMibGroups": cie1000AlarmMibGroups,
       "cie1000AlarmConfigTableInfoGroup": cie1000AlarmConfigTableInfoGroup,
       "cie1000AlarmConfigTableRowEditorInfoGroup": cie1000AlarmConfigTableRowEditorInfoGroup,
       "cie1000AlarmStatusInfoGroup": cie1000AlarmStatusInfoGroup,
       "cie1000AlarmControlTableInfoGroup": cie1000AlarmControlTableInfoGroup,
       "cie1000AlarmTrapStatusAddInfoGroup": cie1000AlarmTrapStatusAddInfoGroup,
       "cie1000AlarmTrapStatusModInfoGroup": cie1000AlarmTrapStatusModInfoGroup,
       "cie1000AlarmTrapStatusDelInfoGroup": cie1000AlarmTrapStatusDelInfoGroup}
)
