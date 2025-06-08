# SNMP MIB module (BROADHOP-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/broadhop_26878/BROADHOP-NOTIFICATION-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:03 2025
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

(broadhopComponentAdditionalInfo,
 broadhopComponentName,
 broadhopComponentNotificationName,
 broadhopComponentTime,
 broadhopNotificationFacility,
 broadhopNotificationSeverity) = mibBuilder.importSymbols(
    "BROADHOP-MIB",
    "broadhopComponentAdditionalInfo",
    "broadhopComponentName",
    "broadhopComponentNotificationName",
    "broadhopComponentTime",
    "broadhopNotificationFacility",
    "broadhopNotificationSeverity")

(broadhopProductsQNS,) = mibBuilder.importSymbols(
    "BROADHOP-QNS-MIB",
    "broadhopProductsQNS")

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

broadhopProductsQNSNotification = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 2)
)
if mibBuilder.loadTexts:
    broadhopProductsQNSNotification.setRevisions(
        ("2012-02-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BroadhopProductsQNSNotifications_ObjectIdentity = ObjectIdentity
broadhopProductsQNSNotifications = _BroadhopProductsQNSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 0)
)

# Managed Objects groups


# Notification objects

broadhopQNSComponentNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 0, 1)
)
broadhopQNSComponentNotification.setObjects(
      *(("BROADHOP-MIB", "broadhopComponentName"),
        ("BROADHOP-MIB", "broadhopComponentTime"),
        ("BROADHOP-MIB", "broadhopComponentNotificationName"),
        ("BROADHOP-MIB", "broadhopNotificationFacility"),
        ("BROADHOP-MIB", "broadhopNotificationSeverity"),
        ("BROADHOP-MIB", "broadhopComponentAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopQNSComponentNotification.setStatus(
        "current"
    )

broadhopQNSApplicationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 200, 2, 0, 2)
)
broadhopQNSApplicationNotification.setObjects(
      *(("BROADHOP-MIB", "broadhopComponentName"),
        ("BROADHOP-MIB", "broadhopComponentTime"),
        ("BROADHOP-MIB", "broadhopComponentNotificationName"),
        ("BROADHOP-MIB", "broadhopNotificationFacility"),
        ("BROADHOP-MIB", "broadhopNotificationSeverity"),
        ("BROADHOP-MIB", "broadhopComponentAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopQNSApplicationNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROADHOP-NOTIFICATION-MIB",
    **{"broadhopProductsQNSNotifications": broadhopProductsQNSNotifications,
       "broadhopQNSComponentNotification": broadhopQNSComponentNotification,
       "broadhopQNSApplicationNotification": broadhopQNSApplicationNotification,
       "broadhopProductsQNSNotification": broadhopProductsQNSNotification}
)
