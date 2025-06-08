# SNMP MIB module (EVENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/edenrock_37033/EVENTS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:58:45 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37033)
)
if mibBuilder.loadTexts:
    eventMIB.setRevisions(
        ("2015-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EventTraps_ObjectIdentity = ObjectIdentity
eventTraps = _EventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37033, 0)
)
_EventObjects_ObjectIdentity = ObjectIdentity
eventObjects = _EventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37033, 1)
)
_EventName_Type = OctetString
_EventName_Object = MibScalar
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 37033, 1, 1),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
_EventCategory_Type = OctetString
_EventCategory_Object = MibScalar
eventCategory = _EventCategory_Object(
    (1, 3, 6, 1, 4, 1, 37033, 1, 2),
    _EventCategory_Type()
)
eventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCategory.setStatus("current")
_EventMIBCompliances_ObjectIdentity = ObjectIdentity
eventMIBCompliances = _EventMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37033, 3)
)
_EventMIBGroups_ObjectIdentity = ObjectIdentity
eventMIBGroups = _EventMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37033, 4)
)

# Managed Objects groups

objectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 37033, 4, 2)
)
objectGroup.setObjects(
      *(("EVENTS-MIB", "eventName"),
        ("EVENTS-MIB", "eventCategory"))
)
if mibBuilder.loadTexts:
    objectGroup.setStatus("current")


# Notification objects

eventNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 37033, 0, 2)
)
eventNotice.setObjects(
      *(("EVENTS-MIB", "eventName"),
        ("EVENTS-MIB", "eventCategory"))
)
if mibBuilder.loadTexts:
    eventNotice.setStatus(
        "current"
    )


# Notifications groups

trapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 37033, 4, 1)
)
trapGroup.setObjects(
    ("EVENTS-MIB", "eventNotice")
)
if mibBuilder.loadTexts:
    trapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eventComplianceGroups = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 37033, 3, 1)
)
eventComplianceGroups.setObjects(
      *(("EVENTS-MIB", "trapGroup"),
        ("EVENTS-MIB", "objectGroup"))
)
if mibBuilder.loadTexts:
    eventComplianceGroups.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EVENTS-MIB",
    **{"eventMIB": eventMIB,
       "eventTraps": eventTraps,
       "eventNotice": eventNotice,
       "eventObjects": eventObjects,
       "eventName": eventName,
       "eventCategory": eventCategory,
       "eventMIBCompliances": eventMIBCompliances,
       "eventComplianceGroups": eventComplianceGroups,
       "eventMIBGroups": eventMIBGroups,
       "trapGroup": trapGroup,
       "objectGroup": objectGroup}
)
