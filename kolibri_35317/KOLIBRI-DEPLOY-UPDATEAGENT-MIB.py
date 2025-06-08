# SNMP MIB module (KOLIBRI-DEPLOY-UPDATEAGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-DEPLOY-UPDATEAGENT-MIB.mib
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

(koliUpdateAgent,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliUpdateAgent",
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

koliUpdateAgentModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 2, 0)
)
if mibBuilder.loadTexts:
    koliUpdateAgentModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliUpdateAgentTraps_ObjectIdentity = ObjectIdentity
koliUpdateAgentTraps = _KoliUpdateAgentTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 2, 1)
)
_KoliUpdateAgentTrap_ObjectIdentity = ObjectIdentity
koliUpdateAgentTrap = _KoliUpdateAgentTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 2, 1, 0)
)

# Managed Objects groups


# Notification objects

koliUpdateAgentServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 2, 1, 0, 1)
)
koliUpdateAgentServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUpdateAgentServiceStart.setStatus(
        "current"
    )

koliUpdateAgentServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 2, 1, 0, 2)
)
koliUpdateAgentServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUpdateAgentServiceStop.setStatus(
        "current"
    )

koliUpdateAgentGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 2, 1, 0, 7)
)
koliUpdateAgentGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUpdateAgentGenericException.setStatus(
        "current"
    )


# Notifications groups

koliUpdateAgentNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 2, 4)
)
koliUpdateAgentNotifications.setObjects(
      *(("KOLIBRI-DEPLOY-UPDATEAGENT-MIB", "koliUpdateAgentServiceStart"),
        ("KOLIBRI-DEPLOY-UPDATEAGENT-MIB", "koliUpdateAgentServiceStop"),
        ("KOLIBRI-DEPLOY-UPDATEAGENT-MIB", "koliUpdateAgentGenericException"))
)
if mibBuilder.loadTexts:
    koliUpdateAgentNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-DEPLOY-UPDATEAGENT-MIB",
    **{"koliUpdateAgentModule": koliUpdateAgentModule,
       "koliUpdateAgentTraps": koliUpdateAgentTraps,
       "koliUpdateAgentTrap": koliUpdateAgentTrap,
       "koliUpdateAgentServiceStart": koliUpdateAgentServiceStart,
       "koliUpdateAgentServiceStop": koliUpdateAgentServiceStop,
       "koliUpdateAgentGenericException": koliUpdateAgentGenericException,
       "koliUpdateAgentNotifications": koliUpdateAgentNotifications}
)
