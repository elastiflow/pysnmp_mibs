# SNMP MIB module (CISCO-IETF-PPVPN-MPLS-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-IETF-PPVPN-MPLS-VPN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:29:56 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(mplsVpnVrfConfHighRouteThreshold,
 mplsVpnVrfPerfCurrNumRoutes) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfConfHighRouteThreshold",
    "mplsVpnVrfPerfCurrNumRoutes")

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

ciscoMplsVpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999)
)
if mibBuilder.loadTexts:
    ciscoMplsVpnMIB.setRevisions(
        ("2003-04-17 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CMplsVpnNotifs_ObjectIdentity = ObjectIdentity
cMplsVpnNotifs = _CMplsVpnNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 0)
)
_CMplsVpnObjects_ObjectIdentity = ObjectIdentity
cMplsVpnObjects = _CMplsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1)
)
_CMplsVpnConform_ObjectIdentity = ObjectIdentity
cMplsVpnConform = _CMplsVpnConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2)
)
_CMplsVpnCompliances_ObjectIdentity = ObjectIdentity
cMplsVpnCompliances = _CMplsVpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1)
)
_CMplsVpnGroups_ObjectIdentity = ObjectIdentity
cMplsVpnGroups = _CMplsVpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2)
)

# Managed Objects groups


# Notification objects

cMplsNumVrfRouteMaxThreshCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)
)
cMplsNumVrfRouteMaxThreshCleared.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"))
)
if mibBuilder.loadTexts:
    cMplsNumVrfRouteMaxThreshCleared.setStatus(
        "current"
    )


# Notifications groups

cMplsVpnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 1)
)
cMplsVpnNotificationGroup.setObjects(
    ("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsNumVrfRouteMaxThreshCleared")
)
if mibBuilder.loadTexts:
    cMplsVpnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cMplsVpnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)
)
cMplsVpnCompliance.setObjects(
    ("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsVpnNotificationGroup")
)
if mibBuilder.loadTexts:
    cMplsVpnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PPVPN-MPLS-VPN-MIB",
    **{"ciscoMplsVpnMIB": ciscoMplsVpnMIB,
       "cMplsVpnNotifs": cMplsVpnNotifs,
       "cMplsNumVrfRouteMaxThreshCleared": cMplsNumVrfRouteMaxThreshCleared,
       "cMplsVpnObjects": cMplsVpnObjects,
       "cMplsVpnConform": cMplsVpnConform,
       "cMplsVpnCompliances": cMplsVpnCompliances,
       "cMplsVpnCompliance": cMplsVpnCompliance,
       "cMplsVpnGroups": cMplsVpnGroups,
       "cMplsVpnNotificationGroup": cMplsVpnNotificationGroup}
)
