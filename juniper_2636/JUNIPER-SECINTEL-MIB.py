# SNMP MIB module (JUNIPER-SECINTEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-SECINTEL-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:30:07 2025
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

(jnxJsSecIntel,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsSecIntel")

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

jnxJsSecIntelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 23, 1)
)
if mibBuilder.loadTexts:
    jnxJsSecIntelMib.setRevisions(
        ("2020-09-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsSecIntelNotifications_ObjectIdentity = ObjectIdentity
jnxJsSecIntelNotifications = _JnxJsSecIntelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 23, 1, 0)
)
_JnxJsSecIntelObjects_ObjectIdentity = ObjectIdentity
jnxJsSecIntelObjects = _JnxJsSecIntelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 23, 1, 1)
)
_JnxJsSecIntelTrapVars_ObjectIdentity = ObjectIdentity
jnxJsSecIntelTrapVars = _JnxJsSecIntelTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 23, 1, 1, 1)
)
_JnxJsSecIntelChannelType_Type = DisplayString
_JnxJsSecIntelChannelType_Object = MibScalar
jnxJsSecIntelChannelType = _JnxJsSecIntelChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 23, 1, 1, 1, 1),
    _JnxJsSecIntelChannelType_Type()
)
jnxJsSecIntelChannelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsSecIntelChannelType.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsSecIntelChannelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 23, 1, 0, 1)
)
jnxJsSecIntelChannelUp.setObjects(
    ("JUNIPER-SECINTEL-MIB", "jnxJsSecIntelChannelType")
)
if mibBuilder.loadTexts:
    jnxJsSecIntelChannelUp.setStatus(
        "current"
    )

jnxJsSecIntelChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 23, 1, 0, 2)
)
jnxJsSecIntelChannelDown.setObjects(
    ("JUNIPER-SECINTEL-MIB", "jnxJsSecIntelChannelType")
)
if mibBuilder.loadTexts:
    jnxJsSecIntelChannelDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SECINTEL-MIB",
    **{"jnxJsSecIntelMib": jnxJsSecIntelMib,
       "jnxJsSecIntelNotifications": jnxJsSecIntelNotifications,
       "jnxJsSecIntelChannelUp": jnxJsSecIntelChannelUp,
       "jnxJsSecIntelChannelDown": jnxJsSecIntelChannelDown,
       "jnxJsSecIntelObjects": jnxJsSecIntelObjects,
       "jnxJsSecIntelTrapVars": jnxJsSecIntelTrapVars,
       "jnxJsSecIntelChannelType": jnxJsSecIntelChannelType}
)
