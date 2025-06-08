# SNMP MIB module (KOLIBRI-SERVICE-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-SERVICE-CONTROL-MIB.mib
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

(koliControl,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriCommAddress,
 kolibriCommInstance,
 kolibriCommReference,
 kolibriConfigAddress,
 kolibriControlAddress,
 kolibriGatewayAddress,
 kolibriGatewayConnection,
 kolibriGatewayName,
 kolibriInstanceName,
 kolibriLogAddress,
 kolibriLoggingAddress) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliControl",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriCommAddress",
    "kolibriCommInstance",
    "kolibriCommReference",
    "kolibriConfigAddress",
    "kolibriControlAddress",
    "kolibriGatewayAddress",
    "kolibriGatewayConnection",
    "kolibriGatewayName",
    "kolibriInstanceName",
    "kolibriLogAddress",
    "kolibriLoggingAddress")

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

koliControlModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 0)
)
if mibBuilder.loadTexts:
    koliControlModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliControlTraps_ObjectIdentity = ObjectIdentity
koliControlTraps = _KoliControlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1)
)
_KoliControlTrap_ObjectIdentity = ObjectIdentity
koliControlTrap = _KoliControlTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0)
)

# Managed Objects groups


# Notification objects

koliControlServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 1)
)
koliControlServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliControlServiceStart.setStatus(
        "current"
    )

koliControlServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 2)
)
koliControlServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliControlServiceStop.setStatus(
        "current"
    )

koliControlClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 3)
)
koliControlClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliControlClientConnected.setStatus(
        "current"
    )

koliControlClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 4)
)
koliControlClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliControlClientDisconnected.setStatus(
        "current"
    )

koliControlGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 7)
)
koliControlGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliControlGenericException.setStatus(
        "current"
    )

koliControlGatewayRegistration = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 10)
)
koliControlGatewayRegistration.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriGatewayConnection"),
        ("KOLIBRI-MIB", "kolibriGatewayName"))
)
if mibBuilder.loadTexts:
    koliControlGatewayRegistration.setStatus(
        "current"
    )

koliControlGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 11)
)
koliControlGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriGatewayConnection"),
        ("KOLIBRI-MIB", "kolibriGatewayAddress"))
)
if mibBuilder.loadTexts:
    koliControlGatewayConnected.setStatus(
        "current"
    )

koliControlGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 12)
)
koliControlGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriGatewayConnection"),
        ("KOLIBRI-MIB", "kolibriGatewayAddress"))
)
if mibBuilder.loadTexts:
    koliControlGatewayDisconnected.setStatus(
        "current"
    )

koliControlDongleFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 13)
)
koliControlDongleFail.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliControlDongleFail.setStatus(
        "current"
    )

koliControlDongleOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 14)
)
koliControlDongleOK.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliControlDongleOK.setStatus(
        "current"
    )

koliControlLogConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 15)
)
koliControlLogConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriLogAddress"))
)
if mibBuilder.loadTexts:
    koliControlLogConnected.setStatus(
        "current"
    )

koliControlLogDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 16)
)
koliControlLogDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriLogAddress"))
)
if mibBuilder.loadTexts:
    koliControlLogDisconnected.setStatus(
        "current"
    )

koliControlSyncConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 17)
)
koliControlSyncConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliControlSyncConnected.setStatus(
        "current"
    )

koliControlSyncDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 18)
)
koliControlSyncDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliControlSyncDisconnected.setStatus(
        "current"
    )

koliControlCommAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 19)
)
koliControlCommAvailable.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommAddress"),
        ("KOLIBRI-MIB", "kolibriCommReference"),
        ("KOLIBRI-MIB", "kolibriCommInstance"))
)
if mibBuilder.loadTexts:
    koliControlCommAvailable.setStatus(
        "current"
    )

koliControlCommUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 20)
)
koliControlCommUnavailable.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommAddress"),
        ("KOLIBRI-MIB", "kolibriCommReference"),
        ("KOLIBRI-MIB", "kolibriCommInstance"))
)
if mibBuilder.loadTexts:
    koliControlCommUnavailable.setStatus(
        "current"
    )

koliControlConfigConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 21)
)
koliControlConfigConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriConfigAddress"))
)
if mibBuilder.loadTexts:
    koliControlConfigConnected.setStatus(
        "current"
    )

koliControlConfigDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 22)
)
koliControlConfigDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriConfigAddress"))
)
if mibBuilder.loadTexts:
    koliControlConfigDisconnected.setStatus(
        "current"
    )

koliControlLoggingConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 23)
)
koliControlLoggingConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriLoggingAddress"))
)
if mibBuilder.loadTexts:
    koliControlLoggingConnected.setStatus(
        "current"
    )

koliControlLoggingDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 1, 0, 24)
)
koliControlLoggingDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriLoggingAddress"))
)
if mibBuilder.loadTexts:
    koliControlLoggingDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliControlNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 2, 4)
)
koliControlNotifications.setObjects(
      *(("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlServiceStart"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlServiceStop"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlClientConnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlClientDisconnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlGenericException"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlGatewayRegistration"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlGatewayConnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlGatewayDisconnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlDongleFail"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlDongleOK"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlLogConnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlLogDisconnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlSyncConnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlSyncDisconnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlCommAvailable"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlCommUnavailable"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlConfigConnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlConfigDisconnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlLoggingConnected"),
        ("KOLIBRI-SERVICE-CONTROL-MIB", "koliControlLoggingDisconnected"))
)
if mibBuilder.loadTexts:
    koliControlNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-SERVICE-CONTROL-MIB",
    **{"koliControlModule": koliControlModule,
       "koliControlTraps": koliControlTraps,
       "koliControlTrap": koliControlTrap,
       "koliControlServiceStart": koliControlServiceStart,
       "koliControlServiceStop": koliControlServiceStop,
       "koliControlClientConnected": koliControlClientConnected,
       "koliControlClientDisconnected": koliControlClientDisconnected,
       "koliControlGenericException": koliControlGenericException,
       "koliControlGatewayRegistration": koliControlGatewayRegistration,
       "koliControlGatewayConnected": koliControlGatewayConnected,
       "koliControlGatewayDisconnected": koliControlGatewayDisconnected,
       "koliControlDongleFail": koliControlDongleFail,
       "koliControlDongleOK": koliControlDongleOK,
       "koliControlLogConnected": koliControlLogConnected,
       "koliControlLogDisconnected": koliControlLogDisconnected,
       "koliControlSyncConnected": koliControlSyncConnected,
       "koliControlSyncDisconnected": koliControlSyncDisconnected,
       "koliControlCommAvailable": koliControlCommAvailable,
       "koliControlCommUnavailable": koliControlCommUnavailable,
       "koliControlConfigConnected": koliControlConfigConnected,
       "koliControlConfigDisconnected": koliControlConfigDisconnected,
       "koliControlLoggingConnected": koliControlLoggingConnected,
       "koliControlLoggingDisconnected": koliControlLoggingDisconnected,
       "koliControlNotifications": koliControlNotifications}
)
