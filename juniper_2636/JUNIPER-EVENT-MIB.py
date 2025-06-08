# SNMP MIB module (JUNIPER-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-EVENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:48:42 2025
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

(jnxEventNotifications,
 jnxMibs) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxEventNotifications",
    "jnxMibs")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

jnxEvent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 37)
)
if mibBuilder.loadTexts:
    jnxEvent.setRevisions(
        ("2006-08-16 21:53",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxEventNotifyVars_ObjectIdentity = ObjectIdentity
jnxEventNotifyVars = _JnxEventNotifyVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 37, 1)
)
if mibBuilder.loadTexts:
    jnxEventNotifyVars.setStatus("current")
_JnxEventTrapDescr_Type = DisplayString
_JnxEventTrapDescr_Object = MibScalar
jnxEventTrapDescr = _JnxEventTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 1),
    _JnxEventTrapDescr_Type()
)
jnxEventTrapDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxEventTrapDescr.setStatus("current")
_JnxEventAvTable_Object = MibTable
jnxEventAvTable = _JnxEventAvTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2)
)
if mibBuilder.loadTexts:
    jnxEventAvTable.setStatus("current")
_JnxEventAvEntry_Object = MibTableRow
jnxEventAvEntry = _JnxEventAvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1)
)
jnxEventAvEntry.setIndexNames(
    (0, "JUNIPER-EVENT-MIB", "jnxEventAvIndex"),
)
if mibBuilder.loadTexts:
    jnxEventAvEntry.setStatus("current")
_JnxEventAvIndex_Type = Unsigned32
_JnxEventAvIndex_Object = MibTableColumn
jnxEventAvIndex = _JnxEventAvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 1),
    _JnxEventAvIndex_Type()
)
jnxEventAvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxEventAvIndex.setStatus("current")
_JnxEventAvAttribute_Type = DisplayString
_JnxEventAvAttribute_Object = MibTableColumn
jnxEventAvAttribute = _JnxEventAvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 2),
    _JnxEventAvAttribute_Type()
)
jnxEventAvAttribute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxEventAvAttribute.setStatus("current")
_JnxEventAvValue_Type = DisplayString
_JnxEventAvValue_Object = MibTableColumn
jnxEventAvValue = _JnxEventAvValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 3),
    _JnxEventAvValue_Type()
)
jnxEventAvValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxEventAvValue.setStatus("current")
_JnxEventNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxEventNotificationPrefix = _JnxEventNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 13, 0)
)
if mibBuilder.loadTexts:
    jnxEventNotificationPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 13, 0, 1)
)
jnxEventTrap.setObjects(
    ("JUNIPER-EVENT-MIB", "jnxEventTrapDescr")
)
if mibBuilder.loadTexts:
    jnxEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-EVENT-MIB",
    **{"jnxEvent": jnxEvent,
       "jnxEventNotifyVars": jnxEventNotifyVars,
       "jnxEventTrapDescr": jnxEventTrapDescr,
       "jnxEventAvTable": jnxEventAvTable,
       "jnxEventAvEntry": jnxEventAvEntry,
       "jnxEventAvIndex": jnxEventAvIndex,
       "jnxEventAvAttribute": jnxEventAvAttribute,
       "jnxEventAvValue": jnxEventAvValue,
       "jnxEventNotificationPrefix": jnxEventNotificationPrefix,
       "jnxEventTrap": jnxEventTrap}
)
