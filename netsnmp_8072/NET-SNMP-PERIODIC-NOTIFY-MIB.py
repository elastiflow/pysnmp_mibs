# SNMP MIB module (NET-SNMP-PERIODIC-NOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/netsnmp_8072/NET-SNMP-PERIODIC-NOTIFY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:28:10 2025
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

(netSnmpModuleIDs,
 netSnmpNotifications,
 netSnmpObjects) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmpModuleIDs",
    "netSnmpNotifications",
    "netSnmpObjects")

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

netSnmpPeriodicNotifyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5)
)
if mibBuilder.loadTexts:
    netSnmpPeriodicNotifyMib.setRevisions(
        ("2011-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsPNScalars_ObjectIdentity = ObjectIdentity
nsPNScalars = _NsPNScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 1)
)
_NsPNTables_ObjectIdentity = ObjectIdentity
nsPNTables = _NsPNTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 2)
)
_NsPNotifyObjects_ObjectIdentity = ObjectIdentity
nsPNotifyObjects = _NsPNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3)
)
_NsPNPeriodicTime_Type = Unsigned32
_NsPNPeriodicTime_Object = MibScalar
nsPNPeriodicTime = _NsPNPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 1),
    _NsPNPeriodicTime_Type()
)
nsPNPeriodicTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsPNPeriodicTime.setStatus("current")
_NsPNotifyMessageNumber_Type = Unsigned32
_NsPNotifyMessageNumber_Object = MibScalar
nsPNotifyMessageNumber = _NsPNotifyMessageNumber_Object(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 2),
    _NsPNotifyMessageNumber_Type()
)
nsPNotifyMessageNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsPNotifyMessageNumber.setStatus("current")
_NsPNotifyMaxMessageNumber_Type = Unsigned32
_NsPNotifyMaxMessageNumber_Object = MibScalar
nsPNotifyMaxMessageNumber = _NsPNotifyMaxMessageNumber_Object(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 3),
    _NsPNotifyMaxMessageNumber_Type()
)
nsPNotifyMaxMessageNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsPNotifyMaxMessageNumber.setStatus("current")
_NsPNotificationPrefix_ObjectIdentity = ObjectIdentity
nsPNotificationPrefix = _NsPNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4)
)
_NsPNotifications_ObjectIdentity = ObjectIdentity
nsPNotifications = _NsPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 0)
)
_NsPNotificationObjects_ObjectIdentity = ObjectIdentity
nsPNotificationObjects = _NsPNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 1)
)

# Managed Objects groups


# Notification objects

nsNotifyPeriodicNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 0, 1)
)
if mibBuilder.loadTexts:
    nsNotifyPeriodicNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-PERIODIC-NOTIFY-MIB",
    **{"netSnmpPeriodicNotifyMib": netSnmpPeriodicNotifyMib,
       "nsPNScalars": nsPNScalars,
       "nsPNTables": nsPNTables,
       "nsPNotifyObjects": nsPNotifyObjects,
       "nsPNPeriodicTime": nsPNPeriodicTime,
       "nsPNotifyMessageNumber": nsPNotifyMessageNumber,
       "nsPNotifyMaxMessageNumber": nsPNotifyMaxMessageNumber,
       "nsPNotificationPrefix": nsPNotificationPrefix,
       "nsPNotifications": nsPNotifications,
       "nsNotifyPeriodicNotification": nsNotifyPeriodicNotification,
       "nsPNotificationObjects": nsPNotificationObjects}
)
