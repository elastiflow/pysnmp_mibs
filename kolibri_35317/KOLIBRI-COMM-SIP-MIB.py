# SNMP MIB module (KOLIBRI-COMM-SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-COMM-SIP-MIB.mib
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

(koliSIP,
 kolibriAudioAddress,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriInstanceName,
 kolibriVideoAddress) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliSIP",
    "kolibriAudioAddress",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriInstanceName",
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

koliSIPModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 0)
)
if mibBuilder.loadTexts:
    koliSIPModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2017-04-18 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliSIPTraps_ObjectIdentity = ObjectIdentity
koliSIPTraps = _KoliSIPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1)
)
_KoliSIPTrap_ObjectIdentity = ObjectIdentity
koliSIPTrap = _KoliSIPTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0)
)

# Managed Objects groups


# Notification objects

koliSIPServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 1)
)
koliSIPServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliSIPServiceStart.setStatus(
        "current"
    )

koliSIPServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 2)
)
koliSIPServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliSIPServiceStop.setStatus(
        "current"
    )

koliSIPClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 3)
)
koliSIPClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliSIPClientConnected.setStatus(
        "current"
    )

koliSIPClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 4)
)
koliSIPClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliSIPClientDisconnected.setStatus(
        "current"
    )

koliSIPGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 7)
)
koliSIPGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliSIPGenericException.setStatus(
        "current"
    )

koliSIPAudioConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 21)
)
koliSIPAudioConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliSIPAudioConnected.setStatus(
        "current"
    )

koliSIPAudioDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 22)
)
koliSIPAudioDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliSIPAudioDisconnected.setStatus(
        "current"
    )

koliSIPVideoConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 31)
)
koliSIPVideoConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriVideoAddress"))
)
if mibBuilder.loadTexts:
    koliSIPVideoConnected.setStatus(
        "current"
    )

koliSIPVideoDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 1, 0, 32)
)
koliSIPVideoDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriVideoAddress"))
)
if mibBuilder.loadTexts:
    koliSIPVideoDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliSIPNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 2, 4)
)
koliSIPNotifications.setObjects(
      *(("KOLIBRI-COMM-SIP-MIB", "koliSIPServiceStart"),
        ("KOLIBRI-COMM-SIP-MIB", "koliSIPServiceStop"),
        ("KOLIBRI-COMM-SIP-MIB", "koliSIPClientConnected"),
        ("KOLIBRI-COMM-SIP-MIB", "koliSIPClientDisconnected"),
        ("KOLIBRI-COMM-SIP-MIB", "koliSIPGenericException"),
        ("KOLIBRI-COMM-SIP-MIB", "koliSIPAudioConnected"),
        ("KOLIBRI-COMM-SIP-MIB", "koliSIPAudioDisconnected"),
        ("KOLIBRI-COMM-SIP-MIB", "koliSIPVideoConnected"),
        ("KOLIBRI-COMM-SIP-MIB", "koliSIPVideoDisconnected"))
)
if mibBuilder.loadTexts:
    koliSIPNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-COMM-SIP-MIB",
    **{"koliSIPModule": koliSIPModule,
       "koliSIPTraps": koliSIPTraps,
       "koliSIPTrap": koliSIPTrap,
       "koliSIPServiceStart": koliSIPServiceStart,
       "koliSIPServiceStop": koliSIPServiceStop,
       "koliSIPClientConnected": koliSIPClientConnected,
       "koliSIPClientDisconnected": koliSIPClientDisconnected,
       "koliSIPGenericException": koliSIPGenericException,
       "koliSIPAudioConnected": koliSIPAudioConnected,
       "koliSIPAudioDisconnected": koliSIPAudioDisconnected,
       "koliSIPVideoConnected": koliSIPVideoConnected,
       "koliSIPVideoDisconnected": koliSIPVideoDisconnected,
       "koliSIPNotifications": koliSIPNotifications}
)
