# SNMP MIB module (KOLIBRI-DISPATCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-DISPATCH-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:39 2025
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

(koliDispatch,
 kolibriAudioAddress,
 kolibriControlAddress,
 kolibriControlStandby,
 kolibriDAIAddress,
 kolibriLogAddress,
 kolibriLoggingAddress,
 kolibriMapAddress,
 kolibriVideoAddress) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliDispatch",
    "kolibriAudioAddress",
    "kolibriControlAddress",
    "kolibriControlStandby",
    "kolibriDAIAddress",
    "kolibriLogAddress",
    "kolibriLoggingAddress",
    "kolibriMapAddress",
    "kolibriVideoAddress")

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

koliDispatchModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 0)
)
if mibBuilder.loadTexts:
    koliDispatchModule.setRevisions(
        ("2017-04-18 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliDispatchTraps_ObjectIdentity = ObjectIdentity
koliDispatchTraps = _KoliDispatchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1)
)
_KoliDispatchTrap_ObjectIdentity = ObjectIdentity
koliDispatchTrap = _KoliDispatchTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0)
)

# Managed Objects groups


# Notification objects

koliDispatchStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    koliDispatchStarted.setStatus(
        "current"
    )

koliDispatchStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 2)
)
if mibBuilder.loadTexts:
    koliDispatchStopped.setStatus(
        "current"
    )

koliDispatchAudioConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 11)
)
koliDispatchAudioConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriAudioAddress")
)
if mibBuilder.loadTexts:
    koliDispatchAudioConnected.setStatus(
        "current"
    )

koliDispatchAudioDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 12)
)
koliDispatchAudioDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriAudioAddress")
)
if mibBuilder.loadTexts:
    koliDispatchAudioDisconnected.setStatus(
        "current"
    )

koliDispatchControlConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 13)
)
koliDispatchControlConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriControlAddress"),
        ("KOLIBRI-MIB", "kolibriControlStandby"))
)
if mibBuilder.loadTexts:
    koliDispatchControlConnected.setStatus(
        "current"
    )

koliDispatchControlDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 14)
)
koliDispatchControlDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriControlAddress"),
        ("KOLIBRI-MIB", "kolibriControlStandby"))
)
if mibBuilder.loadTexts:
    koliDispatchControlDisconnected.setStatus(
        "current"
    )

koliDispatchLogConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 15)
)
koliDispatchLogConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriLogAddress")
)
if mibBuilder.loadTexts:
    koliDispatchLogConnected.setStatus(
        "current"
    )

koliDispatchLogDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 16)
)
koliDispatchLogDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriLogAddress")
)
if mibBuilder.loadTexts:
    koliDispatchLogDisconnected.setStatus(
        "current"
    )

koliDispatchDAIConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 17)
)
koliDispatchDAIConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriDAIAddress")
)
if mibBuilder.loadTexts:
    koliDispatchDAIConnected.setStatus(
        "current"
    )

koliDispatchDAIDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 18)
)
koliDispatchDAIDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriDAIAddress")
)
if mibBuilder.loadTexts:
    koliDispatchDAIDisconnected.setStatus(
        "current"
    )

koliDispatchLoggingConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 19)
)
koliDispatchLoggingConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriLoggingAddress")
)
if mibBuilder.loadTexts:
    koliDispatchLoggingConnected.setStatus(
        "current"
    )

koliDispatchLoggingDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 20)
)
koliDispatchLoggingDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriLoggingAddress")
)
if mibBuilder.loadTexts:
    koliDispatchLoggingDisconnected.setStatus(
        "current"
    )

koliDispatchMapConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 21)
)
koliDispatchMapConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriMapAddress")
)
if mibBuilder.loadTexts:
    koliDispatchMapConnected.setStatus(
        "current"
    )

koliDispatchMapDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 22)
)
koliDispatchMapDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriMapAddress")
)
if mibBuilder.loadTexts:
    koliDispatchMapDisconnected.setStatus(
        "current"
    )

koliDispatchVideoConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 23)
)
koliDispatchVideoConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriVideoAddress")
)
if mibBuilder.loadTexts:
    koliDispatchVideoConnected.setStatus(
        "current"
    )

koliDispatchVideoDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 1, 0, 24)
)
koliDispatchVideoDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriVideoAddress")
)
if mibBuilder.loadTexts:
    koliDispatchVideoDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliDispatchNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 1, 1, 4)
)
koliDispatchNotifications.setObjects(
      *(("KOLIBRI-DISPATCH-MIB", "koliDispatchStarted"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchStopped"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchAudioConnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchAudioDisconnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchControlConnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchControlDisconnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchLogConnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchLogDisconnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchDAIConnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchDAIDisconnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchLoggingConnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchLoggingDisconnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchMapConnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchMapDisconnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchVideoConnected"),
        ("KOLIBRI-DISPATCH-MIB", "koliDispatchVideoDisconnected"))
)
if mibBuilder.loadTexts:
    koliDispatchNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-DISPATCH-MIB",
    **{"koliDispatchModule": koliDispatchModule,
       "koliDispatchTraps": koliDispatchTraps,
       "koliDispatchTrap": koliDispatchTrap,
       "koliDispatchStarted": koliDispatchStarted,
       "koliDispatchStopped": koliDispatchStopped,
       "koliDispatchAudioConnected": koliDispatchAudioConnected,
       "koliDispatchAudioDisconnected": koliDispatchAudioDisconnected,
       "koliDispatchControlConnected": koliDispatchControlConnected,
       "koliDispatchControlDisconnected": koliDispatchControlDisconnected,
       "koliDispatchLogConnected": koliDispatchLogConnected,
       "koliDispatchLogDisconnected": koliDispatchLogDisconnected,
       "koliDispatchDAIConnected": koliDispatchDAIConnected,
       "koliDispatchDAIDisconnected": koliDispatchDAIDisconnected,
       "koliDispatchLoggingConnected": koliDispatchLoggingConnected,
       "koliDispatchLoggingDisconnected": koliDispatchLoggingDisconnected,
       "koliDispatchMapConnected": koliDispatchMapConnected,
       "koliDispatchMapDisconnected": koliDispatchMapDisconnected,
       "koliDispatchVideoConnected": koliDispatchVideoConnected,
       "koliDispatchVideoDisconnected": koliDispatchVideoDisconnected,
       "koliDispatchNotifications": koliDispatchNotifications}
)
