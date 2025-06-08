# SNMP MIB module (KOLIBRI-SERVICE-WATCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-SERVICE-WATCH-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:40 2025
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

(koliWatch,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliWatch",
    "kolibriInstanceName")

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

koliWatchModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 0)
)
if mibBuilder.loadTexts:
    koliWatchModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliWatchTraps_ObjectIdentity = ObjectIdentity
koliWatchTraps = _KoliWatchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 1)
)
_KoliWatchTrap_ObjectIdentity = ObjectIdentity
koliWatchTrap = _KoliWatchTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 1, 0)
)
_KoliWatchValue_ObjectIdentity = ObjectIdentity
koliWatchValue = _KoliWatchValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 2)
)


class _KoliWatchCount_Type(Integer32):
    """Custom type koliWatchCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_KoliWatchCount_Type.__name__ = "Integer32"
_KoliWatchCount_Object = MibScalar
koliWatchCount = _KoliWatchCount_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 2, 1),
    _KoliWatchCount_Type()
)
koliWatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliWatchCount.setStatus("current")

# Managed Objects groups

koliWatchObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 3)
)
koliWatchObjects.setObjects(
    ("KOLIBRI-SERVICE-WATCH-MIB", "koliWatchCount")
)
if mibBuilder.loadTexts:
    koliWatchObjects.setStatus("current")


# Notification objects

koliWatchServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 1, 0, 1)
)
koliWatchServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliWatchServiceStart.setStatus(
        "current"
    )

koliWatchServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 1, 0, 2)
)
koliWatchServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliWatchServiceStop.setStatus(
        "current"
    )

koliWatchGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 1, 0, 7)
)
koliWatchGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliWatchGenericException.setStatus(
        "current"
    )

koliWatchFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 1, 0, 13)
)
koliWatchFailChange.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-SERVICE-WATCH-MIB", "koliWatchCount"))
)
if mibBuilder.loadTexts:
    koliWatchFailChange.setStatus(
        "current"
    )


# Notifications groups

koliWatchNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 4, 4)
)
koliWatchNotifications.setObjects(
      *(("KOLIBRI-SERVICE-WATCH-MIB", "koliWatchServiceStart"),
        ("KOLIBRI-SERVICE-WATCH-MIB", "koliWatchServiceStop"),
        ("KOLIBRI-SERVICE-WATCH-MIB", "koliWatchGenericException"),
        ("KOLIBRI-SERVICE-WATCH-MIB", "koliWatchFailChange"))
)
if mibBuilder.loadTexts:
    koliWatchNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-SERVICE-WATCH-MIB",
    **{"koliWatchModule": koliWatchModule,
       "koliWatchTraps": koliWatchTraps,
       "koliWatchTrap": koliWatchTrap,
       "koliWatchServiceStart": koliWatchServiceStart,
       "koliWatchServiceStop": koliWatchServiceStop,
       "koliWatchGenericException": koliWatchGenericException,
       "koliWatchFailChange": koliWatchFailChange,
       "koliWatchValue": koliWatchValue,
       "koliWatchCount": koliWatchCount,
       "koliWatchObjects": koliWatchObjects,
       "koliWatchNotifications": koliWatchNotifications}
)
