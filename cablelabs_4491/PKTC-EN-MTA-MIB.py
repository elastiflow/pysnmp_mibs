# SNMP MIB module (PKTC-EN-MTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/PKTC-EN-MTA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:18 2025
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

(pktcEnhancements,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEnhancements")

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

pktcEnMtaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    pktcEnMtaMib.setRevisions(
        ("2005-01-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEnMtaMibObjects_ObjectIdentity = ObjectIdentity
pktcEnMtaMibObjects = _PktcEnMtaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 1)
)
_PktcEnMtaDevBase_ObjectIdentity = ObjectIdentity
pktcEnMtaDevBase = _PktcEnMtaDevBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 1, 1)
)


class _PktcEnMtaDevMltplGrantsPerInterval_Type(Integer32):
    """Custom type pktcEnMtaDevMltplGrantsPerInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enablemgpifunctionality", 1),
          ("disablemgpifunctionality", 2))
    )


_PktcEnMtaDevMltplGrantsPerInterval_Type.__name__ = "Integer32"
_PktcEnMtaDevMltplGrantsPerInterval_Object = MibScalar
pktcEnMtaDevMltplGrantsPerInterval = _PktcEnMtaDevMltplGrantsPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 1, 1, 1),
    _PktcEnMtaDevMltplGrantsPerInterval_Type()
)
pktcEnMtaDevMltplGrantsPerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnMtaDevMltplGrantsPerInterval.setStatus("current")
_PktcEnMtaDevServer_ObjectIdentity = ObjectIdentity
pktcEnMtaDevServer = _PktcEnMtaDevServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 1, 2)
)
_PktcEnMtaDevSecurity_ObjectIdentity = ObjectIdentity
pktcEnMtaDevSecurity = _PktcEnMtaDevSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 1, 3)
)
_PktcEnMtaNotificationPrefix_ObjectIdentity = ObjectIdentity
pktcEnMtaNotificationPrefix = _PktcEnMtaNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 2)
)
_PktcEnMtaNotification_ObjectIdentity = ObjectIdentity
pktcEnMtaNotification = _PktcEnMtaNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 2, 0)
)
_PktcEnMtaConformance_ObjectIdentity = ObjectIdentity
pktcEnMtaConformance = _PktcEnMtaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 3)
)
_PktcEnMtaCompliances_ObjectIdentity = ObjectIdentity
pktcEnMtaCompliances = _PktcEnMtaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 3, 1)
)
_PktcEnMtaGroups_ObjectIdentity = ObjectIdentity
pktcEnMtaGroups = _PktcEnMtaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 3, 2)
)

# Managed Objects groups

pktcEnMtaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 3, 2, 1)
)
pktcEnMtaGroup.setObjects(
    ("PKTC-EN-MTA-MIB", "pktcEnMtaDevMltplGrantsPerInterval")
)
if mibBuilder.loadTexts:
    pktcEnMtaGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEnMtaBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 1, 3, 1, 3)
)
pktcEnMtaBasicCompliance.setObjects(
    ("PKTC-EN-MTA-MIB", "pktcEnMtaGroup")
)
if mibBuilder.loadTexts:
    pktcEnMtaBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-EN-MTA-MIB",
    **{"pktcEnMtaMib": pktcEnMtaMib,
       "pktcEnMtaMibObjects": pktcEnMtaMibObjects,
       "pktcEnMtaDevBase": pktcEnMtaDevBase,
       "pktcEnMtaDevMltplGrantsPerInterval": pktcEnMtaDevMltplGrantsPerInterval,
       "pktcEnMtaDevServer": pktcEnMtaDevServer,
       "pktcEnMtaDevSecurity": pktcEnMtaDevSecurity,
       "pktcEnMtaNotificationPrefix": pktcEnMtaNotificationPrefix,
       "pktcEnMtaNotification": pktcEnMtaNotification,
       "pktcEnMtaConformance": pktcEnMtaConformance,
       "pktcEnMtaCompliances": pktcEnMtaCompliances,
       "pktcEnMtaBasicCompliance": pktcEnMtaBasicCompliance,
       "pktcEnMtaGroups": pktcEnMtaGroups,
       "pktcEnMtaGroup": pktcEnMtaGroup}
)
