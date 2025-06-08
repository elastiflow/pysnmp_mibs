# SNMP MIB module (KOLIBRI-SERVICE-ARCHIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-SERVICE-ARCHIVE-MIB.mib
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

(koliArchive,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliArchive",
    "kolibriInstanceName")

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

koliArchiveModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 0)
)
if mibBuilder.loadTexts:
    koliArchiveModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliArchiveTraps_ObjectIdentity = ObjectIdentity
koliArchiveTraps = _KoliArchiveTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 1)
)
_KoliArchiveTrap_ObjectIdentity = ObjectIdentity
koliArchiveTrap = _KoliArchiveTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 1, 0)
)

# Managed Objects groups


# Notification objects

koliArchiveServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 1, 0, 1)
)
koliArchiveServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliArchiveServiceStart.setStatus(
        "current"
    )

koliArchiveServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 1, 0, 2)
)
koliArchiveServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliArchiveServiceStop.setStatus(
        "current"
    )

koliArchiveGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 1, 0, 7)
)
koliArchiveGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliArchiveGenericException.setStatus(
        "current"
    )

koliArchiveDBFirstConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 1, 0, 11)
)
koliArchiveDBFirstConnect.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliArchiveDBFirstConnect.setStatus(
        "current"
    )

koliArchiveDBConnectFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 1, 0, 12)
)
koliArchiveDBConnectFail.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliArchiveDBConnectFail.setStatus(
        "current"
    )

koliArchiveJobFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 1, 0, 13)
)
koliArchiveJobFailed.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliArchiveJobFailed.setStatus(
        "current"
    )


# Notifications groups

koliArchiveNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 6, 4)
)
koliArchiveNotifications.setObjects(
      *(("KOLIBRI-SERVICE-ARCHIVE-MIB", "koliArchiveServiceStart"),
        ("KOLIBRI-SERVICE-ARCHIVE-MIB", "koliArchiveServiceStop"),
        ("KOLIBRI-SERVICE-ARCHIVE-MIB", "koliArchiveGenericException"),
        ("KOLIBRI-SERVICE-ARCHIVE-MIB", "koliArchiveDBFirstConnect"),
        ("KOLIBRI-SERVICE-ARCHIVE-MIB", "koliArchiveDBConnectFail"),
        ("KOLIBRI-SERVICE-ARCHIVE-MIB", "koliArchiveJobFailed"))
)
if mibBuilder.loadTexts:
    koliArchiveNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-SERVICE-ARCHIVE-MIB",
    **{"koliArchiveModule": koliArchiveModule,
       "koliArchiveTraps": koliArchiveTraps,
       "koliArchiveTrap": koliArchiveTrap,
       "koliArchiveServiceStart": koliArchiveServiceStart,
       "koliArchiveServiceStop": koliArchiveServiceStop,
       "koliArchiveGenericException": koliArchiveGenericException,
       "koliArchiveDBFirstConnect": koliArchiveDBFirstConnect,
       "koliArchiveDBConnectFail": koliArchiveDBConnectFail,
       "koliArchiveJobFailed": koliArchiveJobFailed,
       "koliArchiveNotifications": koliArchiveNotifications}
)
