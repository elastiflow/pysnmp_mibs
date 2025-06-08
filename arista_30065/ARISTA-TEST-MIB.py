# SNMP MIB module (ARISTA-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-TEST-MIB.mib
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

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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

aristaTestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3)
)
if mibBuilder.loadTexts:
    aristaTestMIB.setRevisions(
        ("2014-08-15 00:00",
         "2011-03-31 13:00",
         "2010-12-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaTestNotifications_ObjectIdentity = ObjectIdentity
aristaTestNotifications = _AristaTestNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 0)
)
_AristaTestNotificationPrefix_ObjectIdentity = ObjectIdentity
aristaTestNotificationPrefix = _AristaTestNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0)
)
_AristaTestObjects_ObjectIdentity = ObjectIdentity
aristaTestObjects = _AristaTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 1)
)
_AristaTestNotificationCounter_Type = ZeroBasedCounter32
_AristaTestNotificationCounter_Object = MibScalar
aristaTestNotificationCounter = _AristaTestNotificationCounter_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 1),
    _AristaTestNotificationCounter_Type()
)
aristaTestNotificationCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaTestNotificationCounter.setStatus("current")


class _AristaTestNotificationComment_Type(DisplayString):
    """Custom type aristaTestNotificationComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaTestNotificationComment_Type.__name__ = "DisplayString"
_AristaTestNotificationComment_Object = MibScalar
aristaTestNotificationComment = _AristaTestNotificationComment_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 2),
    _AristaTestNotificationComment_Type()
)
aristaTestNotificationComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaTestNotificationComment.setStatus("current")
_AristaTestConformance_ObjectIdentity = ObjectIdentity
aristaTestConformance = _AristaTestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 2)
)
_AristaTestCompliances_ObjectIdentity = ObjectIdentity
aristaTestCompliances = _AristaTestCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1)
)
_AristaTestGroups_ObjectIdentity = ObjectIdentity
aristaTestGroups = _AristaTestGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2)
)

# Managed Objects groups

aristaTestObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 1)
)
aristaTestObjectsGroup.setObjects(
      *(("ARISTA-TEST-MIB", "aristaTestNotificationCounter"),
        ("ARISTA-TEST-MIB", "aristaTestNotificationComment"))
)
if mibBuilder.loadTexts:
    aristaTestObjectsGroup.setStatus("current")


# Notification objects

aristaTestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0, 1)
)
aristaTestNotification.setObjects(
      *(("ARISTA-TEST-MIB", "aristaTestNotificationCounter"),
        ("ARISTA-TEST-MIB", "aristaTestNotificationComment"))
)
if mibBuilder.loadTexts:
    aristaTestNotification.setStatus(
        "current"
    )


# Notifications groups

aristaTestNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 2)
)
aristaTestNotificationsGroup.setObjects(
    ("ARISTA-TEST-MIB", "aristaTestNotification")
)
if mibBuilder.loadTexts:
    aristaTestNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaTestCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1, 1)
)
aristaTestCompliance.setObjects(
      *(("ARISTA-TEST-MIB", "aristaTestObjectsGroup"),
        ("ARISTA-TEST-MIB", "aristaTestNotificationsGroup"))
)
if mibBuilder.loadTexts:
    aristaTestCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-TEST-MIB",
    **{"aristaTestMIB": aristaTestMIB,
       "aristaTestNotifications": aristaTestNotifications,
       "aristaTestNotificationPrefix": aristaTestNotificationPrefix,
       "aristaTestNotification": aristaTestNotification,
       "aristaTestObjects": aristaTestObjects,
       "aristaTestNotificationCounter": aristaTestNotificationCounter,
       "aristaTestNotificationComment": aristaTestNotificationComment,
       "aristaTestConformance": aristaTestConformance,
       "aristaTestCompliances": aristaTestCompliances,
       "aristaTestCompliance": aristaTestCompliance,
       "aristaTestGroups": aristaTestGroups,
       "aristaTestObjectsGroup": aristaTestObjectsGroup,
       "aristaTestNotificationsGroup": aristaTestNotificationsGroup}
)
