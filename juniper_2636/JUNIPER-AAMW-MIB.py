# SNMP MIB module (JUNIPER-AAMW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-AAMW-MIB.mib
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

(jnxJsAAMW,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsAAMW")

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

jnxJsAAMWMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 21, 1)
)
if mibBuilder.loadTexts:
    jnxJsAAMWMib.setRevisions(
        ("2020-09-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsAAMWNotifications_ObjectIdentity = ObjectIdentity
jnxJsAAMWNotifications = _JnxJsAAMWNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 21, 1, 0)
)
_JnxJsAAMWObjects_ObjectIdentity = ObjectIdentity
jnxJsAAMWObjects = _JnxJsAAMWObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 21, 1, 1)
)
_JnxJsAAMWTrapVars_ObjectIdentity = ObjectIdentity
jnxJsAAMWTrapVars = _JnxJsAAMWTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 21, 1, 1, 1)
)
_JnxJsAAMWChannelType_Type = DisplayString
_JnxJsAAMWChannelType_Object = MibScalar
jnxJsAAMWChannelType = _JnxJsAAMWChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 21, 1, 1, 1, 1),
    _JnxJsAAMWChannelType_Type()
)
jnxJsAAMWChannelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsAAMWChannelType.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsAAMWChannelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 21, 1, 0, 1)
)
jnxJsAAMWChannelUp.setObjects(
    ("JUNIPER-AAMW-MIB", "jnxJsAAMWChannelType")
)
if mibBuilder.loadTexts:
    jnxJsAAMWChannelUp.setStatus(
        "current"
    )

jnxJsAAMWChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 21, 1, 0, 2)
)
jnxJsAAMWChannelDown.setObjects(
    ("JUNIPER-AAMW-MIB", "jnxJsAAMWChannelType")
)
if mibBuilder.loadTexts:
    jnxJsAAMWChannelDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-AAMW-MIB",
    **{"jnxJsAAMWMib": jnxJsAAMWMib,
       "jnxJsAAMWNotifications": jnxJsAAMWNotifications,
       "jnxJsAAMWChannelUp": jnxJsAAMWChannelUp,
       "jnxJsAAMWChannelDown": jnxJsAAMWChannelDown,
       "jnxJsAAMWObjects": jnxJsAAMWObjects,
       "jnxJsAAMWTrapVars": jnxJsAAMWTrapVars,
       "jnxJsAAMWChannelType": jnxJsAAMWChannelType}
)
