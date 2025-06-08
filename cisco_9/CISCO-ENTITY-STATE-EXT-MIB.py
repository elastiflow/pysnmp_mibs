# SNMP MIB module (CISCO-ENTITY-STATE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ENTITY-STATE-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:13:16 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entStateAlarm,
 entStateEntry,
 entStateStandby) = mibBuilder.importSymbols(
    "ENTITY-STATE-MIB",
    "entStateAlarm",
    "entStateEntry",
    "entStateStandby")

(EntityStandbyStatus,) = mibBuilder.importSymbols(
    "ENTITY-STATE-TC-MIB",
    "EntityStandbyStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoEntityStateExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 747)
)
if mibBuilder.loadTexts:
    ciscoEntityStateExtMIB.setRevisions(
        ("2010-06-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEntityStateExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEntityStateExtMIBNotifs = _CiscoEntityStateExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 0)
)
_CiscoEntityStateExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityStateExtMIBObjects = _CiscoEntityStateExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1)
)
_CeStateExtTable_Object = MibTable
ceStateExtTable = _CeStateExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 1)
)
if mibBuilder.loadTexts:
    ceStateExtTable.setStatus("current")
_CeStateExtEntry_Object = MibTableRow
ceStateExtEntry = _CeStateExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceStateExtEntry.setStatus("current")
_CeStateExtPrevStandbyState_Type = EntityStandbyStatus
_CeStateExtPrevStandbyState_Object = MibTableColumn
ceStateExtPrevStandbyState = _CeStateExtPrevStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 1, 1, 1),
    _CeStateExtPrevStandbyState_Type()
)
ceStateExtPrevStandbyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ceStateExtPrevStandbyState.setStatus("current")


class _CeStateExtSwitchoverNotifEnable_Type(Integer32):
    """Custom type ceStateExtSwitchoverNotifEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followsGlobal", 1),
          ("disabled", 2))
    )


_CeStateExtSwitchoverNotifEnable_Type.__name__ = "Integer32"
_CeStateExtSwitchoverNotifEnable_Object = MibTableColumn
ceStateExtSwitchoverNotifEnable = _CeStateExtSwitchoverNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 1, 1, 2),
    _CeStateExtSwitchoverNotifEnable_Type()
)
ceStateExtSwitchoverNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceStateExtSwitchoverNotifEnable.setStatus("current")


class _CeStateExtStandbyStatusNotifEnable_Type(Integer32):
    """Custom type ceStateExtStandbyStatusNotifEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followsGlobal", 1),
          ("disabled", 2))
    )


_CeStateExtStandbyStatusNotifEnable_Type.__name__ = "Integer32"
_CeStateExtStandbyStatusNotifEnable_Object = MibTableColumn
ceStateExtStandbyStatusNotifEnable = _CeStateExtStandbyStatusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 1, 1, 3),
    _CeStateExtStandbyStatusNotifEnable_Type()
)
ceStateExtStandbyStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceStateExtStandbyStatusNotifEnable.setStatus("current")


class _CeStateExtOperNotifEnable_Type(Integer32):
    """Custom type ceStateExtOperNotifEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followsGlobal", 1),
          ("disabled", 2))
    )


_CeStateExtOperNotifEnable_Type.__name__ = "Integer32"
_CeStateExtOperNotifEnable_Object = MibTableColumn
ceStateExtOperNotifEnable = _CeStateExtOperNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 1, 1, 4),
    _CeStateExtOperNotifEnable_Type()
)
ceStateExtOperNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceStateExtOperNotifEnable.setStatus("current")
_CiscoEntityStateExtNotifControl_ObjectIdentity = ObjectIdentity
ciscoEntityStateExtNotifControl = _CiscoEntityStateExtNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 2)
)


class _CeStateExtGlobalSwitchoverNotifEnable_Type(Integer32):
    """Custom type ceStateExtGlobalSwitchoverNotifEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CeStateExtGlobalSwitchoverNotifEnable_Type.__name__ = "Integer32"
_CeStateExtGlobalSwitchoverNotifEnable_Object = MibScalar
ceStateExtGlobalSwitchoverNotifEnable = _CeStateExtGlobalSwitchoverNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 2, 1),
    _CeStateExtGlobalSwitchoverNotifEnable_Type()
)
ceStateExtGlobalSwitchoverNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceStateExtGlobalSwitchoverNotifEnable.setStatus("current")


class _CeStateExtGlobalStandbyStatusNotifEnable_Type(Integer32):
    """Custom type ceStateExtGlobalStandbyStatusNotifEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CeStateExtGlobalStandbyStatusNotifEnable_Type.__name__ = "Integer32"
_CeStateExtGlobalStandbyStatusNotifEnable_Object = MibScalar
ceStateExtGlobalStandbyStatusNotifEnable = _CeStateExtGlobalStandbyStatusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 2, 2),
    _CeStateExtGlobalStandbyStatusNotifEnable_Type()
)
ceStateExtGlobalStandbyStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceStateExtGlobalStandbyStatusNotifEnable.setStatus("current")


class _CeStateExtGlobalOperNotifEnable_Type(Integer32):
    """Custom type ceStateExtGlobalOperNotifEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CeStateExtGlobalOperNotifEnable_Type.__name__ = "Integer32"
_CeStateExtGlobalOperNotifEnable_Object = MibScalar
ceStateExtGlobalOperNotifEnable = _CeStateExtGlobalOperNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 1, 2, 3),
    _CeStateExtGlobalOperNotifEnable_Type()
)
ceStateExtGlobalOperNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceStateExtGlobalOperNotifEnable.setStatus("current")
_CiscoEntityStateExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoEntityStateExtMIBConform = _CiscoEntityStateExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 2)
)
_CiscoEntStateExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntStateExtMIBCompliances = _CiscoEntStateExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 2, 1)
)
_CiscoEntStateExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntStateExtMIBGroups = _CiscoEntStateExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 2, 2)
)
entStateEntry.registerAugmentions(
    ("CISCO-ENTITY-STATE-EXT-MIB",
     "ceStateExtEntry")
)
ceStateExtEntry.setIndexNames(*entStateEntry.getIndexNames())

# Managed Objects groups

ciscoEntStateExtNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 2, 2, 1)
)
ciscoEntStateExtNotifObjectsGroup.setObjects(
    ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtPrevStandbyState")
)
if mibBuilder.loadTexts:
    ciscoEntStateExtNotifObjectsGroup.setStatus("current")

ciscoEntStateExtNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 2, 2, 2)
)
ciscoEntStateExtNotifControlGroup.setObjects(
      *(("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtSwitchoverNotifEnable"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtStandbyStatusNotifEnable"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtOperNotifEnable"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtGlobalSwitchoverNotifEnable"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtGlobalStandbyStatusNotifEnable"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtGlobalOperNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoEntStateExtNotifControlGroup.setStatus("current")


# Notification objects

ceStateExtStandbySwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 0, 1)
)
ceStateExtStandbySwitchover.setObjects(
      *(("ENTITY-STATE-MIB", "entStateAlarm"),
        ("ENTITY-STATE-MIB", "entStateStandby"))
)
if mibBuilder.loadTexts:
    ceStateExtStandbySwitchover.setStatus(
        "current"
    )

ceStateExtStandbyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 0, 2)
)
ceStateExtStandbyStatusChange.setObjects(
      *(("ENTITY-STATE-MIB", "entStateAlarm"),
        ("ENTITY-STATE-MIB", "entStateStandby"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtPrevStandbyState"))
)
if mibBuilder.loadTexts:
    ceStateExtStandbyStatusChange.setStatus(
        "current"
    )


# Notifications groups

ciscoEntStateExtSwitchoverNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 2, 2, 3)
)
ciscoEntStateExtSwitchoverNotifGroup.setObjects(
    ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtStandbySwitchover")
)
if mibBuilder.loadTexts:
    ciscoEntStateExtSwitchoverNotifGroup.setStatus(
        "current"
    )

ciscoEntStateExtStatusNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 2, 2, 4)
)
ciscoEntStateExtStatusNotifGroup.setObjects(
    ("CISCO-ENTITY-STATE-EXT-MIB", "ceStateExtStandbyStatusChange")
)
if mibBuilder.loadTexts:
    ciscoEntStateExtStatusNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEntStateExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 747, 2, 1, 1)
)
ciscoEntStateExtMIBCompliance.setObjects(
      *(("CISCO-ENTITY-STATE-EXT-MIB", "ciscoEntStateExtNotifObjectsGroup"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ciscoEntStateExtNotifControlGroup"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ciscoEntStateExtSwitchoverNotifGroup"),
        ("CISCO-ENTITY-STATE-EXT-MIB", "ciscoEntStateExtStatusNotifGroup"))
)
if mibBuilder.loadTexts:
    ciscoEntStateExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-STATE-EXT-MIB",
    **{"ciscoEntityStateExtMIB": ciscoEntityStateExtMIB,
       "ciscoEntityStateExtMIBNotifs": ciscoEntityStateExtMIBNotifs,
       "ceStateExtStandbySwitchover": ceStateExtStandbySwitchover,
       "ceStateExtStandbyStatusChange": ceStateExtStandbyStatusChange,
       "ciscoEntityStateExtMIBObjects": ciscoEntityStateExtMIBObjects,
       "ceStateExtTable": ceStateExtTable,
       "ceStateExtEntry": ceStateExtEntry,
       "ceStateExtPrevStandbyState": ceStateExtPrevStandbyState,
       "ceStateExtSwitchoverNotifEnable": ceStateExtSwitchoverNotifEnable,
       "ceStateExtStandbyStatusNotifEnable": ceStateExtStandbyStatusNotifEnable,
       "ceStateExtOperNotifEnable": ceStateExtOperNotifEnable,
       "ciscoEntityStateExtNotifControl": ciscoEntityStateExtNotifControl,
       "ceStateExtGlobalSwitchoverNotifEnable": ceStateExtGlobalSwitchoverNotifEnable,
       "ceStateExtGlobalStandbyStatusNotifEnable": ceStateExtGlobalStandbyStatusNotifEnable,
       "ceStateExtGlobalOperNotifEnable": ceStateExtGlobalOperNotifEnable,
       "ciscoEntityStateExtMIBConform": ciscoEntityStateExtMIBConform,
       "ciscoEntStateExtMIBCompliances": ciscoEntStateExtMIBCompliances,
       "ciscoEntStateExtMIBCompliance": ciscoEntStateExtMIBCompliance,
       "ciscoEntStateExtMIBGroups": ciscoEntStateExtMIBGroups,
       "ciscoEntStateExtNotifObjectsGroup": ciscoEntStateExtNotifObjectsGroup,
       "ciscoEntStateExtNotifControlGroup": ciscoEntStateExtNotifControlGroup,
       "ciscoEntStateExtSwitchoverNotifGroup": ciscoEntStateExtSwitchoverNotifGroup,
       "ciscoEntStateExtStatusNotifGroup": ciscoEntStateExtStatusNotifGroup}
)
