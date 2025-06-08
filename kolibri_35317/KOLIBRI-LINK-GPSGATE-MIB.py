# SNMP MIB module (KOLIBRI-LINK-GPSGATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-LINK-GPSGATE-MIB.mib
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

(koliLinkGPSGate,
 kolibriInstanceName,
 kolibriLinkAddress) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliLinkGPSGate",
    "kolibriInstanceName",
    "kolibriLinkAddress")

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

koliLinkGPSGateModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 0)
)
if mibBuilder.loadTexts:
    koliLinkGPSGateModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliLinkGPSGateTraps_ObjectIdentity = ObjectIdentity
koliLinkGPSGateTraps = _KoliLinkGPSGateTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1)
)
_KoliLinkGPSGateTrap_ObjectIdentity = ObjectIdentity
koliLinkGPSGateTrap = _KoliLinkGPSGateTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1, 0)
)
_KoliLinkGPSGateValue_ObjectIdentity = ObjectIdentity
koliLinkGPSGateValue = _KoliLinkGPSGateValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 2)
)
_KoliLinkGPSGateAddress_Type = IpAddress
_KoliLinkGPSGateAddress_Object = MibScalar
koliLinkGPSGateAddress = _KoliLinkGPSGateAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 2, 1),
    _KoliLinkGPSGateAddress_Type()
)
koliLinkGPSGateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliLinkGPSGateAddress.setStatus("current")


class _KoliLinkGPSGatePort_Type(Integer32):
    """Custom type koliLinkGPSGatePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_KoliLinkGPSGatePort_Type.__name__ = "Integer32"
_KoliLinkGPSGatePort_Object = MibScalar
koliLinkGPSGatePort = _KoliLinkGPSGatePort_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 2, 2),
    _KoliLinkGPSGatePort_Type()
)
koliLinkGPSGatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliLinkGPSGatePort.setStatus("current")

# Managed Objects groups

koliLinkGPSGateObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 3)
)
koliLinkGPSGateObjects.setObjects(
      *(("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateAddress"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGatePort"))
)
if mibBuilder.loadTexts:
    koliLinkGPSGateObjects.setStatus("current")


# Notification objects

koliLinkGPSGateServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1, 0, 1)
)
koliLinkGPSGateServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkGPSGateServiceStart.setStatus(
        "current"
    )

koliLinkGPSGateServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1, 0, 2)
)
koliLinkGPSGateServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkGPSGateServiceStop.setStatus(
        "current"
    )

koliLinkGPSGateGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1, 0, 7)
)
koliLinkGPSGateGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkGPSGateGenericException.setStatus(
        "current"
    )

koliLinkGPSGateLinkConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1, 0, 11)
)
koliLinkGPSGateLinkConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriLinkAddress"))
)
if mibBuilder.loadTexts:
    koliLinkGPSGateLinkConnected.setStatus(
        "current"
    )

koliLinkGPSGateLinkDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1, 0, 12)
)
koliLinkGPSGateLinkDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriLinkAddress"))
)
if mibBuilder.loadTexts:
    koliLinkGPSGateLinkDisconnected.setStatus(
        "current"
    )

koliLinkGPSGateGPSGateFirstConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1, 0, 13)
)
koliLinkGPSGateGPSGateFirstConnection.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateAddress"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGatePort"))
)
if mibBuilder.loadTexts:
    koliLinkGPSGateGPSGateFirstConnection.setStatus(
        "current"
    )

koliLinkGPSGateGPSGateConnectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 1, 0, 14)
)
koliLinkGPSGateGPSGateConnectionFailed.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateAddress"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGatePort"))
)
if mibBuilder.loadTexts:
    koliLinkGPSGateGPSGateConnectionFailed.setStatus(
        "current"
    )


# Notifications groups

koliLinkGPSGateNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 3, 4)
)
koliLinkGPSGateNotifications.setObjects(
      *(("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateServiceStart"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateServiceStop"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateGenericException"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateLinkConnected"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateLinkDisconnected"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateGPSGateFirstConnection"),
        ("KOLIBRI-LINK-GPSGATE-MIB", "koliLinkGPSGateGPSGateConnectionFailed"))
)
if mibBuilder.loadTexts:
    koliLinkGPSGateNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-LINK-GPSGATE-MIB",
    **{"koliLinkGPSGateModule": koliLinkGPSGateModule,
       "koliLinkGPSGateTraps": koliLinkGPSGateTraps,
       "koliLinkGPSGateTrap": koliLinkGPSGateTrap,
       "koliLinkGPSGateServiceStart": koliLinkGPSGateServiceStart,
       "koliLinkGPSGateServiceStop": koliLinkGPSGateServiceStop,
       "koliLinkGPSGateGenericException": koliLinkGPSGateGenericException,
       "koliLinkGPSGateLinkConnected": koliLinkGPSGateLinkConnected,
       "koliLinkGPSGateLinkDisconnected": koliLinkGPSGateLinkDisconnected,
       "koliLinkGPSGateGPSGateFirstConnection": koliLinkGPSGateGPSGateFirstConnection,
       "koliLinkGPSGateGPSGateConnectionFailed": koliLinkGPSGateGPSGateConnectionFailed,
       "koliLinkGPSGateValue": koliLinkGPSGateValue,
       "koliLinkGPSGateAddress": koliLinkGPSGateAddress,
       "koliLinkGPSGatePort": koliLinkGPSGatePort,
       "koliLinkGPSGateObjects": koliLinkGPSGateObjects,
       "koliLinkGPSGateNotifications": koliLinkGPSGateNotifications}
)
