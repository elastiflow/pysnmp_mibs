# SNMP MIB module (ENTITY-STATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/ENTITY-STATE-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 13:47:14 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(EntityAdminState,
 EntityAlarmStatus,
 EntityOperState,
 EntityStandbyStatus,
 EntityUsageState) = mibBuilder.importSymbols(
    "ENTITY-STATE-TC-MIB",
    "EntityAdminState",
    "EntityAlarmStatus",
    "EntityOperState",
    "EntityStandbyStatus",
    "EntityUsageState")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

entityStateMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 131)
)
if mibBuilder.loadTexts:
    entityStateMIB.setRevisions(
        ("2005-11-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EntStateNotifications_ObjectIdentity = ObjectIdentity
entStateNotifications = _EntStateNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 131, 0)
)
_EntStateObjects_ObjectIdentity = ObjectIdentity
entStateObjects = _EntStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 131, 1)
)
_EntStateTable_Object = MibTable
entStateTable = _EntStateTable_Object(
    (1, 3, 6, 1, 2, 1, 131, 1, 1)
)
if mibBuilder.loadTexts:
    entStateTable.setStatus("current")
_EntStateEntry_Object = MibTableRow
entStateEntry = _EntStateEntry_Object(
    (1, 3, 6, 1, 2, 1, 131, 1, 1, 1)
)
entStateEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    entStateEntry.setStatus("current")
_EntStateLastChanged_Type = DateAndTime
_EntStateLastChanged_Object = MibTableColumn
entStateLastChanged = _EntStateLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 1),
    _EntStateLastChanged_Type()
)
entStateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entStateLastChanged.setStatus("current")
_EntStateAdmin_Type = EntityAdminState
_EntStateAdmin_Object = MibTableColumn
entStateAdmin = _EntStateAdmin_Object(
    (1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 2),
    _EntStateAdmin_Type()
)
entStateAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entStateAdmin.setStatus("current")
_EntStateOper_Type = EntityOperState
_EntStateOper_Object = MibTableColumn
entStateOper = _EntStateOper_Object(
    (1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 3),
    _EntStateOper_Type()
)
entStateOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entStateOper.setStatus("current")
_EntStateUsage_Type = EntityUsageState
_EntStateUsage_Object = MibTableColumn
entStateUsage = _EntStateUsage_Object(
    (1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 4),
    _EntStateUsage_Type()
)
entStateUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entStateUsage.setStatus("current")
_EntStateAlarm_Type = EntityAlarmStatus
_EntStateAlarm_Object = MibTableColumn
entStateAlarm = _EntStateAlarm_Object(
    (1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 5),
    _EntStateAlarm_Type()
)
entStateAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entStateAlarm.setStatus("current")
_EntStateStandby_Type = EntityStandbyStatus
_EntStateStandby_Object = MibTableColumn
entStateStandby = _EntStateStandby_Object(
    (1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 6),
    _EntStateStandby_Type()
)
entStateStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entStateStandby.setStatus("current")
_EntStateConformance_ObjectIdentity = ObjectIdentity
entStateConformance = _EntStateConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 131, 2)
)
_EntStateCompliances_ObjectIdentity = ObjectIdentity
entStateCompliances = _EntStateCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 131, 2, 1)
)
_EntStateGroups_ObjectIdentity = ObjectIdentity
entStateGroups = _EntStateGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 131, 2, 2)
)

# Managed Objects groups

entStateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 131, 2, 2, 1)
)
entStateGroup.setObjects(
      *(("ENTITY-STATE-MIB", "entStateLastChanged"),
        ("ENTITY-STATE-MIB", "entStateAdmin"),
        ("ENTITY-STATE-MIB", "entStateOper"),
        ("ENTITY-STATE-MIB", "entStateUsage"),
        ("ENTITY-STATE-MIB", "entStateAlarm"),
        ("ENTITY-STATE-MIB", "entStateStandby"))
)
if mibBuilder.loadTexts:
    entStateGroup.setStatus("current")


# Notification objects

entStateOperEnabled = NotificationType(
    (1, 3, 6, 1, 2, 1, 131, 0, 1)
)
entStateOperEnabled.setObjects(
      *(("ENTITY-STATE-MIB", "entStateAdmin"),
        ("ENTITY-STATE-MIB", "entStateAlarm"))
)
if mibBuilder.loadTexts:
    entStateOperEnabled.setStatus(
        "current"
    )

entStateOperDisabled = NotificationType(
    (1, 3, 6, 1, 2, 1, 131, 0, 2)
)
entStateOperDisabled.setObjects(
      *(("ENTITY-STATE-MIB", "entStateAdmin"),
        ("ENTITY-STATE-MIB", "entStateAlarm"))
)
if mibBuilder.loadTexts:
    entStateOperDisabled.setStatus(
        "current"
    )


# Notifications groups

entStateNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 131, 2, 2, 2)
)
entStateNotificationsGroup.setObjects(
      *(("ENTITY-STATE-MIB", "entStateOperEnabled"),
        ("ENTITY-STATE-MIB", "entStateOperDisabled"))
)
if mibBuilder.loadTexts:
    entStateNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

entStateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 131, 2, 1, 1)
)
entStateCompliance.setObjects(
      *(("ENTITY-STATE-MIB", "entStateGroup"),
        ("ENTITY-STATE-MIB", "entStateNotificationsGroup"))
)
if mibBuilder.loadTexts:
    entStateCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTITY-STATE-MIB",
    **{"entityStateMIB": entityStateMIB,
       "entStateNotifications": entStateNotifications,
       "entStateOperEnabled": entStateOperEnabled,
       "entStateOperDisabled": entStateOperDisabled,
       "entStateObjects": entStateObjects,
       "entStateTable": entStateTable,
       "entStateEntry": entStateEntry,
       "entStateLastChanged": entStateLastChanged,
       "entStateAdmin": entStateAdmin,
       "entStateOper": entStateOper,
       "entStateUsage": entStateUsage,
       "entStateAlarm": entStateAlarm,
       "entStateStandby": entStateStandby,
       "entStateConformance": entStateConformance,
       "entStateCompliances": entStateCompliances,
       "entStateCompliance": entStateCompliance,
       "entStateGroups": entStateGroups,
       "entStateGroup": entStateGroup,
       "entStateNotificationsGroup": entStateNotificationsGroup}
)
