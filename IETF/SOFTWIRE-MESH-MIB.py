# SNMP MIB module (SOFTWIRE-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SOFTWIRE-MESH-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:08:32 2025
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

(IANAtunnelType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAtunnelType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

swmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 239)
)
if mibBuilder.loadTexts:
    swmMIB.setRevisions(
        ("2016-05-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwmObjects_ObjectIdentity = ObjectIdentity
swmObjects = _SwmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 239, 1)
)
_SwmSupportedTunnelTable_Object = MibTable
swmSupportedTunnelTable = _SwmSupportedTunnelTable_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 1)
)
if mibBuilder.loadTexts:
    swmSupportedTunnelTable.setStatus("current")
_SwmSupportedTunnelEntry_Object = MibTableRow
swmSupportedTunnelEntry = _SwmSupportedTunnelEntry_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 1, 1)
)
swmSupportedTunnelEntry.setIndexNames(
    (0, "SOFTWIRE-MESH-MIB", "swmSupportedTunnelType"),
)
if mibBuilder.loadTexts:
    swmSupportedTunnelEntry.setStatus("current")
_SwmSupportedTunnelType_Type = IANAtunnelType
_SwmSupportedTunnelType_Object = MibTableColumn
swmSupportedTunnelType = _SwmSupportedTunnelType_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 1, 1, 1),
    _SwmSupportedTunnelType_Type()
)
swmSupportedTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swmSupportedTunnelType.setStatus("current")
_SwmEncapsTable_Object = MibTable
swmEncapsTable = _SwmEncapsTable_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 2)
)
if mibBuilder.loadTexts:
    swmEncapsTable.setStatus("current")
_SwmEncapsEntry_Object = MibTableRow
swmEncapsEntry = _SwmEncapsEntry_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 2, 1)
)
swmEncapsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SOFTWIRE-MESH-MIB", "swmEncapsEIPDstType"),
    (0, "SOFTWIRE-MESH-MIB", "swmEncapsEIPDst"),
    (0, "SOFTWIRE-MESH-MIB", "swmEncapsEIPPrefixLength"),
)
if mibBuilder.loadTexts:
    swmEncapsEntry.setStatus("current")
_SwmEncapsEIPDstType_Type = InetAddressType
_SwmEncapsEIPDstType_Object = MibTableColumn
swmEncapsEIPDstType = _SwmEncapsEIPDstType_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 2, 1, 1),
    _SwmEncapsEIPDstType_Type()
)
swmEncapsEIPDstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swmEncapsEIPDstType.setStatus("current")
_SwmEncapsEIPDst_Type = InetAddress
_SwmEncapsEIPDst_Object = MibTableColumn
swmEncapsEIPDst = _SwmEncapsEIPDst_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 2, 1, 2),
    _SwmEncapsEIPDst_Type()
)
swmEncapsEIPDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swmEncapsEIPDst.setStatus("current")
_SwmEncapsEIPPrefixLength_Type = InetAddressPrefixLength
_SwmEncapsEIPPrefixLength_Object = MibTableColumn
swmEncapsEIPPrefixLength = _SwmEncapsEIPPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 2, 1, 3),
    _SwmEncapsEIPPrefixLength_Type()
)
swmEncapsEIPPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swmEncapsEIPPrefixLength.setStatus("current")
_SwmEncapsIIPDstType_Type = InetAddressType
_SwmEncapsIIPDstType_Object = MibTableColumn
swmEncapsIIPDstType = _SwmEncapsIIPDstType_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 2, 1, 4),
    _SwmEncapsIIPDstType_Type()
)
swmEncapsIIPDstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swmEncapsIIPDstType.setStatus("current")
_SwmEncapsIIPDst_Type = InetAddress
_SwmEncapsIIPDst_Object = MibTableColumn
swmEncapsIIPDst = _SwmEncapsIIPDst_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 2, 1, 5),
    _SwmEncapsIIPDst_Type()
)
swmEncapsIIPDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swmEncapsIIPDst.setStatus("current")
_SwmBGPNeighborTable_Object = MibTable
swmBGPNeighborTable = _SwmBGPNeighborTable_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 3)
)
if mibBuilder.loadTexts:
    swmBGPNeighborTable.setStatus("current")
_SwmBGPNeighborEntry_Object = MibTableRow
swmBGPNeighborEntry = _SwmBGPNeighborEntry_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 3, 1)
)
swmBGPNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SOFTWIRE-MESH-MIB", "swmBGPNeighborInetAddressType"),
    (0, "SOFTWIRE-MESH-MIB", "swmBGPNeighborInetAddress"),
)
if mibBuilder.loadTexts:
    swmBGPNeighborEntry.setStatus("current")
_SwmBGPNeighborInetAddressType_Type = InetAddressType
_SwmBGPNeighborInetAddressType_Object = MibTableColumn
swmBGPNeighborInetAddressType = _SwmBGPNeighborInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 3, 1, 1),
    _SwmBGPNeighborInetAddressType_Type()
)
swmBGPNeighborInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swmBGPNeighborInetAddressType.setStatus("current")
_SwmBGPNeighborInetAddress_Type = InetAddress
_SwmBGPNeighborInetAddress_Object = MibTableColumn
swmBGPNeighborInetAddress = _SwmBGPNeighborInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 3, 1, 2),
    _SwmBGPNeighborInetAddress_Type()
)
swmBGPNeighborInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swmBGPNeighborInetAddress.setStatus("current")
_SwmBGPNeighborTunnelType_Type = IANAtunnelType
_SwmBGPNeighborTunnelType_Object = MibTableColumn
swmBGPNeighborTunnelType = _SwmBGPNeighborTunnelType_Object(
    (1, 3, 6, 1, 2, 1, 239, 1, 3, 1, 3),
    _SwmBGPNeighborTunnelType_Type()
)
swmBGPNeighborTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swmBGPNeighborTunnelType.setStatus("current")
_SwmConformance_ObjectIdentity = ObjectIdentity
swmConformance = _SwmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 239, 2)
)
_SwmCompliances_ObjectIdentity = ObjectIdentity
swmCompliances = _SwmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 239, 2, 1)
)
_SwmGroups_ObjectIdentity = ObjectIdentity
swmGroups = _SwmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 239, 2, 2)
)

# Managed Objects groups

swmSupportedTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 239, 2, 2, 1)
)
swmSupportedTunnelGroup.setObjects(
    ("SOFTWIRE-MESH-MIB", "swmSupportedTunnelType")
)
if mibBuilder.loadTexts:
    swmSupportedTunnelGroup.setStatus("current")

swmEncapsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 239, 2, 2, 2)
)
swmEncapsGroup.setObjects(
      *(("SOFTWIRE-MESH-MIB", "swmEncapsIIPDst"),
        ("SOFTWIRE-MESH-MIB", "swmEncapsIIPDstType"))
)
if mibBuilder.loadTexts:
    swmEncapsGroup.setStatus("current")

swmBGPNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 239, 2, 2, 3)
)
swmBGPNeighborGroup.setObjects(
    ("SOFTWIRE-MESH-MIB", "swmBGPNeighborTunnelType")
)
if mibBuilder.loadTexts:
    swmBGPNeighborGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

swmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 239, 2, 1, 1)
)
swmCompliance.setObjects(
      *(("SOFTWIRE-MESH-MIB", "swmSupportedTunnelGroup"),
        ("SOFTWIRE-MESH-MIB", "swmEncapsGroup"),
        ("SOFTWIRE-MESH-MIB", "swmBGPNeighborGroup"))
)
if mibBuilder.loadTexts:
    swmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SOFTWIRE-MESH-MIB",
    **{"swmMIB": swmMIB,
       "swmObjects": swmObjects,
       "swmSupportedTunnelTable": swmSupportedTunnelTable,
       "swmSupportedTunnelEntry": swmSupportedTunnelEntry,
       "swmSupportedTunnelType": swmSupportedTunnelType,
       "swmEncapsTable": swmEncapsTable,
       "swmEncapsEntry": swmEncapsEntry,
       "swmEncapsEIPDstType": swmEncapsEIPDstType,
       "swmEncapsEIPDst": swmEncapsEIPDst,
       "swmEncapsEIPPrefixLength": swmEncapsEIPPrefixLength,
       "swmEncapsIIPDstType": swmEncapsIIPDstType,
       "swmEncapsIIPDst": swmEncapsIIPDst,
       "swmBGPNeighborTable": swmBGPNeighborTable,
       "swmBGPNeighborEntry": swmBGPNeighborEntry,
       "swmBGPNeighborInetAddressType": swmBGPNeighborInetAddressType,
       "swmBGPNeighborInetAddress": swmBGPNeighborInetAddress,
       "swmBGPNeighborTunnelType": swmBGPNeighborTunnelType,
       "swmConformance": swmConformance,
       "swmCompliances": swmCompliances,
       "swmCompliance": swmCompliance,
       "swmGroups": swmGroups,
       "swmSupportedTunnelGroup": swmSupportedTunnelGroup,
       "swmEncapsGroup": swmEncapsGroup,
       "swmBGPNeighborGroup": swmBGPNeighborGroup}
)
