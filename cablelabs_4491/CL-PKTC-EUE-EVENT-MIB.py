# SNMP MIB module (CL-PKTC-EUE-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PKTC-EUE-EVENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

pktcEUEEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEUEEventNotifications_ObjectIdentity = ObjectIdentity
pktcEUEEventNotifications = _PktcEUEEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 0)
)
_PktcEUEEventObjects_ObjectIdentity = ObjectIdentity
pktcEUEEventObjects = _PktcEUEEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 1)
)


class _PktcEUEMEMVersion_Type(SnmpAdminString):
    """Custom type pktcEUEMEMVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUEMEMVersion_Type.__name__ = "SnmpAdminString"
_PktcEUEMEMVersion_Object = MibScalar
pktcEUEMEMVersion = _PktcEUEMEMVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 1, 1),
    _PktcEUEMEMVersion_Type()
)
pktcEUEMEMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEMEMVersion.setStatus("current")
_PktcEUEEventConformance_ObjectIdentity = ObjectIdentity
pktcEUEEventConformance = _PktcEUEEventConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2)
)
_PktcEUEEventCompliances_ObjectIdentity = ObjectIdentity
pktcEUEEventCompliances = _PktcEUEEventCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 1)
)
_PktcEUEEventGroups_ObjectIdentity = ObjectIdentity
pktcEUEEventGroups = _PktcEUEEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 2)
)

# Managed Objects groups

pktcEUEMEMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 2, 1)
)
pktcEUEMEMGroup.setObjects(
    ("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMVersion")
)
if mibBuilder.loadTexts:
    pktcEUEMEMGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUEEventCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 1, 1)
)
pktcEUEEventCompliance.setObjects(
      *(("PKTC-EVENT-MIB", "pktcEventGroup"),
        ("PKTC-EVENT-MIB", "pktcEventNotificationGroup"),
        ("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMGroup"))
)
if mibBuilder.loadTexts:
    pktcEUEEventCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-EVENT-MIB",
    **{"pktcEUEEventMIB": pktcEUEEventMIB,
       "pktcEUEEventNotifications": pktcEUEEventNotifications,
       "pktcEUEEventObjects": pktcEUEEventObjects,
       "pktcEUEMEMVersion": pktcEUEMEMVersion,
       "pktcEUEEventConformance": pktcEUEEventConformance,
       "pktcEUEEventCompliances": pktcEUEEventCompliances,
       "pktcEUEEventCompliance": pktcEUEEventCompliance,
       "pktcEUEEventGroups": pktcEUEEventGroups,
       "pktcEUEMEMGroup": pktcEUEMEMGroup}
)
