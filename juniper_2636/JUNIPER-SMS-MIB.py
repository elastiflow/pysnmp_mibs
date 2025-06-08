# SNMP MIB module (JUNIPER-SMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-SMS-MIB.mib
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

(jnxJsSMS,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsSMS")

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

jnxJsSMSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 22, 1)
)
if mibBuilder.loadTexts:
    jnxJsSMSMib.setRevisions(
        ("2020-09-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsSMSNotifications_ObjectIdentity = ObjectIdentity
jnxJsSMSNotifications = _JnxJsSMSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 22, 1, 0)
)
_JnxJsSMSObjects_ObjectIdentity = ObjectIdentity
jnxJsSMSObjects = _JnxJsSMSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 22, 1, 1)
)
_JnxJsSMSTrapVars_ObjectIdentity = ObjectIdentity
jnxJsSMSTrapVars = _JnxJsSMSTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 22, 1, 1, 1)
)
_JnxJsSMSChannelType_Type = DisplayString
_JnxJsSMSChannelType_Object = MibScalar
jnxJsSMSChannelType = _JnxJsSMSChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 22, 1, 1, 1, 1),
    _JnxJsSMSChannelType_Type()
)
jnxJsSMSChannelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsSMSChannelType.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsSMSChannelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 22, 1, 0, 1)
)
jnxJsSMSChannelUp.setObjects(
    ("JUNIPER-SMS-MIB", "jnxJsSMSChannelType")
)
if mibBuilder.loadTexts:
    jnxJsSMSChannelUp.setStatus(
        "current"
    )

jnxJsSMSChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 22, 1, 0, 2)
)
jnxJsSMSChannelDown.setObjects(
    ("JUNIPER-SMS-MIB", "jnxJsSMSChannelType")
)
if mibBuilder.loadTexts:
    jnxJsSMSChannelDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SMS-MIB",
    **{"jnxJsSMSMib": jnxJsSMSMib,
       "jnxJsSMSNotifications": jnxJsSMSNotifications,
       "jnxJsSMSChannelUp": jnxJsSMSChannelUp,
       "jnxJsSMSChannelDown": jnxJsSMSChannelDown,
       "jnxJsSMSObjects": jnxJsSMSObjects,
       "jnxJsSMSTrapVars": jnxJsSMSTrapVars,
       "jnxJsSMSChannelType": jnxJsSMSChannelType}
)
