# SNMP MIB module (KOLIBRI-COMM-TRBOCOMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-COMM-TRBOCOMM-MIB.mib
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

(koliTRBOComm,
 kolibriAudioAddress,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriCommDevice,
 kolibriExtClientConnection,
 kolibriExtClientName,
 kolibriExtClientTargetPort,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliTRBOComm",
    "kolibriAudioAddress",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriCommDevice",
    "kolibriExtClientConnection",
    "kolibriExtClientName",
    "kolibriExtClientTargetPort",
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

koliTRBOCommModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 0)
)
if mibBuilder.loadTexts:
    koliTRBOCommModule.setRevisions(
        ("2017-04-19 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliTRBOCommTraps_ObjectIdentity = ObjectIdentity
koliTRBOCommTraps = _KoliTRBOCommTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1)
)
_KoliTRBOCommTrap_ObjectIdentity = ObjectIdentity
koliTRBOCommTrap = _KoliTRBOCommTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0)
)

# Managed Objects groups


# Notification objects

koliTRBOCommServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 1)
)
koliTRBOCommServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommServiceStart.setStatus(
        "current"
    )

koliTRBOCommServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 2)
)
koliTRBOCommServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommServiceStop.setStatus(
        "current"
    )

koliTRBOCommClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 3)
)
koliTRBOCommClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliTRBOCommClientConnected.setStatus(
        "current"
    )

koliTRBOCommClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 4)
)
koliTRBOCommClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliTRBOCommClientDisconnected.setStatus(
        "current"
    )

koliTRBOCommGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 7)
)
koliTRBOCommGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommGenericException.setStatus(
        "current"
    )

koliTRBOCommDeviceConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 11)
)
koliTRBOCommDeviceConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommDevice"))
)
if mibBuilder.loadTexts:
    koliTRBOCommDeviceConnected.setStatus(
        "current"
    )

koliTRBOCommDeviceDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 12)
)
koliTRBOCommDeviceDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommDevice"))
)
if mibBuilder.loadTexts:
    koliTRBOCommDeviceDisconnected.setStatus(
        "current"
    )

koliTRBOCommAudioConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 21)
)
koliTRBOCommAudioConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliTRBOCommAudioConnected.setStatus(
        "current"
    )

koliTRBOCommAudioDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 22)
)
koliTRBOCommAudioDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliTRBOCommAudioDisconnected.setStatus(
        "current"
    )

koliTRBOCommXNLConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 41)
)
koliTRBOCommXNLConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommXNLConnected.setStatus(
        "current"
    )

koliTRBOCommXNLDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 42)
)
koliTRBOCommXNLDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommXNLDisconnected.setStatus(
        "current"
    )

koliTRBOCommTMSStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 43)
)
koliTRBOCommTMSStarted.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommTMSStarted.setStatus(
        "current"
    )

koliTRBOCommTMSStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 44)
)
koliTRBOCommTMSStopped.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommTMSStopped.setStatus(
        "current"
    )

koliTRBOCommARSStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 45)
)
koliTRBOCommARSStarted.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommARSStarted.setStatus(
        "current"
    )

koliTRBOCommARSStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 46)
)
koliTRBOCommARSStopped.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommARSStopped.setStatus(
        "current"
    )

koliTRBOCommLSStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 47)
)
koliTRBOCommLSStarted.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommLSStarted.setStatus(
        "current"
    )

koliTRBOCommLSStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 48)
)
koliTRBOCommLSStopped.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOCommLSStopped.setStatus(
        "current"
    )

koliTRBOCommExtClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 49)
)
koliTRBOCommExtClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriExtClientConnection"),
        ("KOLIBRI-MIB", "kolibriExtClientName"),
        ("KOLIBRI-MIB", "kolibriExtClientTargetPort"))
)
if mibBuilder.loadTexts:
    koliTRBOCommExtClientConnected.setStatus(
        "current"
    )

koliTRBOCommExtClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 50)
)
koliTRBOCommExtClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriExtClientConnection"),
        ("KOLIBRI-MIB", "kolibriExtClientName"),
        ("KOLIBRI-MIB", "kolibriExtClientTargetPort"))
)
if mibBuilder.loadTexts:
    koliTRBOCommExtClientDisconnected.setStatus(
        "current"
    )

koliTRBOCommExtUDPClientStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 51)
)
koliTRBOCommExtUDPClientStarted.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriExtClientConnection"),
        ("KOLIBRI-MIB", "kolibriExtClientName"),
        ("KOLIBRI-MIB", "kolibriExtClientTargetPort"))
)
if mibBuilder.loadTexts:
    koliTRBOCommExtUDPClientStarted.setStatus(
        "current"
    )

koliTRBOCommExtUDPClientStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 1, 0, 52)
)
koliTRBOCommExtUDPClientStopped.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriExtClientConnection"),
        ("KOLIBRI-MIB", "kolibriExtClientName"),
        ("KOLIBRI-MIB", "kolibriExtClientTargetPort"))
)
if mibBuilder.loadTexts:
    koliTRBOCommExtUDPClientStopped.setStatus(
        "current"
    )


# Notifications groups

koliTRBOCommNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 6, 4)
)
koliTRBOCommNotifications.setObjects(
      *(("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommServiceStart"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommServiceStop"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommClientConnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommClientDisconnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommGenericException"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommDeviceConnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommDeviceDisconnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommAudioConnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommAudioDisconnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommXNLConnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommXNLDisconnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommTMSStarted"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommTMSStopped"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommARSStarted"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommARSStopped"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommLSStarted"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommLSStopped"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommExtClientConnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommExtClientDisconnected"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommExtUDPClientStarted"),
        ("KOLIBRI-COMM-TRBOCOMM-MIB", "koliTRBOCommExtUDPClientStopped"))
)
if mibBuilder.loadTexts:
    koliTRBOCommNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-COMM-TRBOCOMM-MIB",
    **{"koliTRBOCommModule": koliTRBOCommModule,
       "koliTRBOCommTraps": koliTRBOCommTraps,
       "koliTRBOCommTrap": koliTRBOCommTrap,
       "koliTRBOCommServiceStart": koliTRBOCommServiceStart,
       "koliTRBOCommServiceStop": koliTRBOCommServiceStop,
       "koliTRBOCommClientConnected": koliTRBOCommClientConnected,
       "koliTRBOCommClientDisconnected": koliTRBOCommClientDisconnected,
       "koliTRBOCommGenericException": koliTRBOCommGenericException,
       "koliTRBOCommDeviceConnected": koliTRBOCommDeviceConnected,
       "koliTRBOCommDeviceDisconnected": koliTRBOCommDeviceDisconnected,
       "koliTRBOCommAudioConnected": koliTRBOCommAudioConnected,
       "koliTRBOCommAudioDisconnected": koliTRBOCommAudioDisconnected,
       "koliTRBOCommXNLConnected": koliTRBOCommXNLConnected,
       "koliTRBOCommXNLDisconnected": koliTRBOCommXNLDisconnected,
       "koliTRBOCommTMSStarted": koliTRBOCommTMSStarted,
       "koliTRBOCommTMSStopped": koliTRBOCommTMSStopped,
       "koliTRBOCommARSStarted": koliTRBOCommARSStarted,
       "koliTRBOCommARSStopped": koliTRBOCommARSStopped,
       "koliTRBOCommLSStarted": koliTRBOCommLSStarted,
       "koliTRBOCommLSStopped": koliTRBOCommLSStopped,
       "koliTRBOCommExtClientConnected": koliTRBOCommExtClientConnected,
       "koliTRBOCommExtClientDisconnected": koliTRBOCommExtClientDisconnected,
       "koliTRBOCommExtUDPClientStarted": koliTRBOCommExtUDPClientStarted,
       "koliTRBOCommExtUDPClientStopped": koliTRBOCommExtUDPClientStopped,
       "koliTRBOCommNotifications": koliTRBOCommNotifications}
)
