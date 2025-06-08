# SNMP MIB module (CISCO-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/CISCO-SMI.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cisco = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoProducts_ObjectIdentity = ObjectIdentity
ciscoProducts = _CiscoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1)
)
_CiscoBroadcastEquipment_ObjectIdentity = ObjectIdentity
ciscoBroadcastEquipment = _CiscoBroadcastEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 1)
)
_CiscoCAHeadendSoftware_ObjectIdentity = ObjectIdentity
ciscoCAHeadendSoftware = _CiscoCAHeadendSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)
_CiscoMibs_ObjectIdentity = ObjectIdentity
ciscoMibs = _CiscoMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2)
)
_CiscoAgentCapabilities_ObjectIdentity = ObjectIdentity
ciscoAgentCapabilities = _CiscoAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SMI",
    **{"cisco": cisco,
       "ciscoProducts": ciscoProducts,
       "ciscoBroadcastEquipment": ciscoBroadcastEquipment,
       "ciscoCAHeadendSoftware": ciscoCAHeadendSoftware,
       "ciscoMibs": ciscoMibs,
       "ciscoAgentCapabilities": ciscoAgentCapabilities}
)
