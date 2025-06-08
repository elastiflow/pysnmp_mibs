# SNMP MIB module (CISCO-ROUTE-POLICIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ROUTE-POLICIES-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:37 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoRoutePoliciesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 578)
)
if mibBuilder.loadTexts:
    ciscoRoutePoliciesMIB.setRevisions(
        ("2006-08-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoRoutePoliciesMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoRoutePoliciesMIBNotifs = _CiscoRoutePoliciesMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 578, 0)
)
_CiscoRoutePoliciesMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRoutePoliciesMIBObjects = _CiscoRoutePoliciesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 578, 1)
)
_CrpPolicies_ObjectIdentity = ObjectIdentity
crpPolicies = _CrpPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1)
)
if mibBuilder.loadTexts:
    crpPolicies.setStatus("current")
_CrpPolicyIfIndex_ObjectIdentity = ObjectIdentity
crpPolicyIfIndex = _CrpPolicyIfIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1, 1)
)
if mibBuilder.loadTexts:
    crpPolicyIfIndex.setStatus("current")
_CiscoRoutePoliciesMIBConform_ObjectIdentity = ObjectIdentity
ciscoRoutePoliciesMIBConform = _CiscoRoutePoliciesMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 578, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ROUTE-POLICIES-MIB",
    **{"ciscoRoutePoliciesMIB": ciscoRoutePoliciesMIB,
       "ciscoRoutePoliciesMIBNotifs": ciscoRoutePoliciesMIBNotifs,
       "ciscoRoutePoliciesMIBObjects": ciscoRoutePoliciesMIBObjects,
       "crpPolicies": crpPolicies,
       "crpPolicyIfIndex": crpPolicyIfIndex,
       "ciscoRoutePoliciesMIBConform": ciscoRoutePoliciesMIBConform}
)
