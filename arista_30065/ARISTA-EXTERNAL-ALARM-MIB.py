# SNMP MIB module (ARISTA-EXTERNAL-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-EXTERNAL-ALARM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

aristaExternalAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25)
)
if mibBuilder.loadTexts:
    aristaExternalAlarmMIB.setRevisions(
        ("2018-02-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaExternalAlarmMibNotifications_ObjectIdentity = ObjectIdentity
aristaExternalAlarmMibNotifications = _AristaExternalAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 0)
)
_AristaExternalAlarmMibObjects_ObjectIdentity = ObjectIdentity
aristaExternalAlarmMibObjects = _AristaExternalAlarmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1)
)
_AristaExternalAlarmTable_Object = MibTable
aristaExternalAlarmTable = _AristaExternalAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1)
)
if mibBuilder.loadTexts:
    aristaExternalAlarmTable.setStatus("current")
_AristaExternalAlarmTableEntry_Object = MibTableRow
aristaExternalAlarmTableEntry = _AristaExternalAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1)
)
aristaExternalAlarmTableEntry.setIndexNames(
    (0, "ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmId"),
)
if mibBuilder.loadTexts:
    aristaExternalAlarmTableEntry.setStatus("current")
_AristaExternalAlarmId_Type = Unsigned32
_AristaExternalAlarmId_Object = MibTableColumn
aristaExternalAlarmId = _AristaExternalAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1, 1),
    _AristaExternalAlarmId_Type()
)
aristaExternalAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaExternalAlarmId.setStatus("current")
_AristaExternalAlarmAsserted_Type = TruthValue
_AristaExternalAlarmAsserted_Object = MibTableColumn
aristaExternalAlarmAsserted = _AristaExternalAlarmAsserted_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1, 2),
    _AristaExternalAlarmAsserted_Type()
)
aristaExternalAlarmAsserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaExternalAlarmAsserted.setStatus("current")
_AristaExternalAlarmCount_Type = Unsigned32
_AristaExternalAlarmCount_Object = MibTableColumn
aristaExternalAlarmCount = _AristaExternalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1, 3),
    _AristaExternalAlarmCount_Type()
)
aristaExternalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaExternalAlarmCount.setStatus("current")
_AristaExternalAlarmLastAsserted_Type = TimeStamp
_AristaExternalAlarmLastAsserted_Object = MibTableColumn
aristaExternalAlarmLastAsserted = _AristaExternalAlarmLastAsserted_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1, 4),
    _AristaExternalAlarmLastAsserted_Type()
)
aristaExternalAlarmLastAsserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaExternalAlarmLastAsserted.setStatus("current")
_AristaExternalAlarmLastDeasserted_Type = TimeStamp
_AristaExternalAlarmLastDeasserted_Object = MibTableColumn
aristaExternalAlarmLastDeasserted = _AristaExternalAlarmLastDeasserted_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1, 5),
    _AristaExternalAlarmLastDeasserted_Type()
)
aristaExternalAlarmLastDeasserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaExternalAlarmLastDeasserted.setStatus("current")
_AristaExternalAlarmDescription_Type = DisplayString
_AristaExternalAlarmDescription_Object = MibTableColumn
aristaExternalAlarmDescription = _AristaExternalAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1, 6),
    _AristaExternalAlarmDescription_Type()
)
aristaExternalAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaExternalAlarmDescription.setStatus("current")


class _AristaExternalAlarmPolarity_Type(Integer32):
    """Custom type aristaExternalAlarmPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_AristaExternalAlarmPolarity_Type.__name__ = "Integer32"
_AristaExternalAlarmPolarity_Object = MibTableColumn
aristaExternalAlarmPolarity = _AristaExternalAlarmPolarity_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1, 7),
    _AristaExternalAlarmPolarity_Type()
)
aristaExternalAlarmPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaExternalAlarmPolarity.setStatus("current")


class _AristaExternalAlarmAction_Type(Integer32):
    """Custom type aristaExternalAlarmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("syslog", 2),
          ("snmpTrap", 3))
    )


_AristaExternalAlarmAction_Type.__name__ = "Integer32"
_AristaExternalAlarmAction_Object = MibTableColumn
aristaExternalAlarmAction = _AristaExternalAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 1, 1, 1, 8),
    _AristaExternalAlarmAction_Type()
)
aristaExternalAlarmAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaExternalAlarmAction.setStatus("current")
_AristaExternalAlarmMibConformance_ObjectIdentity = ObjectIdentity
aristaExternalAlarmMibConformance = _AristaExternalAlarmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 2)
)
_AristaExternalAlarmMibCompliances_ObjectIdentity = ObjectIdentity
aristaExternalAlarmMibCompliances = _AristaExternalAlarmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 2, 1)
)
_AristaExternalAlarmMibGroups_ObjectIdentity = ObjectIdentity
aristaExternalAlarmMibGroups = _AristaExternalAlarmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 2, 2)
)

# Managed Objects groups

aristaExternalAlarmObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 2, 2, 1)
)
aristaExternalAlarmObjectsGroup.setObjects(
      *(("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmAsserted"),
        ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmCount"),
        ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmLastAsserted"),
        ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmLastDeasserted"),
        ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmDescription"),
        ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmPolarity"),
        ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmAction"))
)
if mibBuilder.loadTexts:
    aristaExternalAlarmObjectsGroup.setStatus("current")


# Notification objects

aristaExternalAlarmAssertedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 0, 1)
)
aristaExternalAlarmAssertedNotif.setObjects(
    ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmDescription")
)
if mibBuilder.loadTexts:
    aristaExternalAlarmAssertedNotif.setStatus(
        "current"
    )

aristaExternalAlarmDeassertedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 0, 2)
)
aristaExternalAlarmDeassertedNotif.setObjects(
    ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmDescription")
)
if mibBuilder.loadTexts:
    aristaExternalAlarmDeassertedNotif.setStatus(
        "current"
    )


# Notifications groups

aristaExternalAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 2, 2, 2)
)
aristaExternalAlarmNotificationsGroup.setObjects(
      *(("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmAssertedNotif"),
        ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmDeassertedNotif"))
)
if mibBuilder.loadTexts:
    aristaExternalAlarmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaExternalAlarmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 25, 2, 1, 1)
)
aristaExternalAlarmMibCompliance.setObjects(
      *(("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmObjectsGroup"),
        ("ARISTA-EXTERNAL-ALARM-MIB", "aristaExternalAlarmNotificationsGroup"))
)
if mibBuilder.loadTexts:
    aristaExternalAlarmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-EXTERNAL-ALARM-MIB",
    **{"aristaExternalAlarmMIB": aristaExternalAlarmMIB,
       "aristaExternalAlarmMibNotifications": aristaExternalAlarmMibNotifications,
       "aristaExternalAlarmAssertedNotif": aristaExternalAlarmAssertedNotif,
       "aristaExternalAlarmDeassertedNotif": aristaExternalAlarmDeassertedNotif,
       "aristaExternalAlarmMibObjects": aristaExternalAlarmMibObjects,
       "aristaExternalAlarmTable": aristaExternalAlarmTable,
       "aristaExternalAlarmTableEntry": aristaExternalAlarmTableEntry,
       "aristaExternalAlarmId": aristaExternalAlarmId,
       "aristaExternalAlarmAsserted": aristaExternalAlarmAsserted,
       "aristaExternalAlarmCount": aristaExternalAlarmCount,
       "aristaExternalAlarmLastAsserted": aristaExternalAlarmLastAsserted,
       "aristaExternalAlarmLastDeasserted": aristaExternalAlarmLastDeasserted,
       "aristaExternalAlarmDescription": aristaExternalAlarmDescription,
       "aristaExternalAlarmPolarity": aristaExternalAlarmPolarity,
       "aristaExternalAlarmAction": aristaExternalAlarmAction,
       "aristaExternalAlarmMibConformance": aristaExternalAlarmMibConformance,
       "aristaExternalAlarmMibCompliances": aristaExternalAlarmMibCompliances,
       "aristaExternalAlarmMibCompliance": aristaExternalAlarmMibCompliance,
       "aristaExternalAlarmMibGroups": aristaExternalAlarmMibGroups,
       "aristaExternalAlarmObjectsGroup": aristaExternalAlarmObjectsGroup,
       "aristaExternalAlarmNotificationsGroup": aristaExternalAlarmNotificationsGroup}
)
