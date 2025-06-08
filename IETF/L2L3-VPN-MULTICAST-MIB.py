# SNMP MIB module (L2L3-VPN-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/L2L3-VPN-MULTICAST-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:25:04 2025
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

(L2L3VpnMcastProviderTunnelId,
 L2L3VpnMcastProviderTunnelType) = mibBuilder.importSymbols(
    "L2L3-VPN-MULTICAST-TC-MIB",
    "L2L3VpnMcastProviderTunnelId",
    "L2L3VpnMcastProviderTunnelType")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel")

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
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "mib-2",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

l2L3VpnMcastMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 245)
)
if mibBuilder.loadTexts:
    l2L3VpnMcastMIB.setRevisions(
        ("2018-12-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_L2L3VpnMcastStates_ObjectIdentity = ObjectIdentity
l2L3VpnMcastStates = _L2L3VpnMcastStates_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 245, 1)
)
_L2L3VpnMcastPmsiTunnelAttributeTable_Object = MibTable
l2L3VpnMcastPmsiTunnelAttributeTable = _L2L3VpnMcastPmsiTunnelAttributeTable_Object(
    (1, 3, 6, 1, 2, 1, 245, 1, 1)
)
if mibBuilder.loadTexts:
    l2L3VpnMcastPmsiTunnelAttributeTable.setStatus("current")
_L2L3VpnMcastPmsiTunnelAttributeEntry_Object = MibTableRow
l2L3VpnMcastPmsiTunnelAttributeEntry = _L2L3VpnMcastPmsiTunnelAttributeEntry_Object(
    (1, 3, 6, 1, 2, 1, 245, 1, 1, 1)
)
l2L3VpnMcastPmsiTunnelAttributeEntry.setIndexNames(
    (0, "L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelAttributeType"),
    (0, "L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelAttributeId"),
)
if mibBuilder.loadTexts:
    l2L3VpnMcastPmsiTunnelAttributeEntry.setStatus("current")
_L2L3VpnMcastPmsiTunnelAttributeType_Type = L2L3VpnMcastProviderTunnelType
_L2L3VpnMcastPmsiTunnelAttributeType_Object = MibTableColumn
l2L3VpnMcastPmsiTunnelAttributeType = _L2L3VpnMcastPmsiTunnelAttributeType_Object(
    (1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 1),
    _L2L3VpnMcastPmsiTunnelAttributeType_Type()
)
l2L3VpnMcastPmsiTunnelAttributeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2L3VpnMcastPmsiTunnelAttributeType.setStatus("current")
_L2L3VpnMcastPmsiTunnelAttributeId_Type = L2L3VpnMcastProviderTunnelId
_L2L3VpnMcastPmsiTunnelAttributeId_Object = MibTableColumn
l2L3VpnMcastPmsiTunnelAttributeId = _L2L3VpnMcastPmsiTunnelAttributeId_Object(
    (1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 2),
    _L2L3VpnMcastPmsiTunnelAttributeId_Type()
)
l2L3VpnMcastPmsiTunnelAttributeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2L3VpnMcastPmsiTunnelAttributeId.setStatus("current")


class _L2L3VpnMCastPmsiTunnelLeafInfoRequired_Type(Integer32):
    """Custom type l2L3VpnMCastPmsiTunnelLeafInfoRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("notAvailable", 2))
    )


_L2L3VpnMCastPmsiTunnelLeafInfoRequired_Type.__name__ = "Integer32"
_L2L3VpnMCastPmsiTunnelLeafInfoRequired_Object = MibTableColumn
l2L3VpnMCastPmsiTunnelLeafInfoRequired = _L2L3VpnMCastPmsiTunnelLeafInfoRequired_Object(
    (1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 3),
    _L2L3VpnMCastPmsiTunnelLeafInfoRequired_Type()
)
l2L3VpnMCastPmsiTunnelLeafInfoRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2L3VpnMCastPmsiTunnelLeafInfoRequired.setStatus("current")
_L2L3VpnMcastPmsiTunnelAttributeMplsLabel_Type = MplsLabel
_L2L3VpnMcastPmsiTunnelAttributeMplsLabel_Object = MibTableColumn
l2L3VpnMcastPmsiTunnelAttributeMplsLabel = _L2L3VpnMcastPmsiTunnelAttributeMplsLabel_Object(
    (1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 4),
    _L2L3VpnMcastPmsiTunnelAttributeMplsLabel_Type()
)
l2L3VpnMcastPmsiTunnelAttributeMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2L3VpnMcastPmsiTunnelAttributeMplsLabel.setStatus("current")


class _L2L3VpnMcastPmsiTunnelPointer_Type(RowPointer):
    """Custom type l2L3VpnMcastPmsiTunnelPointer based on RowPointer"""
    defaultValue = (0, 0)


_L2L3VpnMcastPmsiTunnelPointer_Type.__name__ = "RowPointer"
_L2L3VpnMcastPmsiTunnelPointer_Object = MibTableColumn
l2L3VpnMcastPmsiTunnelPointer = _L2L3VpnMcastPmsiTunnelPointer_Object(
    (1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 5),
    _L2L3VpnMcastPmsiTunnelPointer_Type()
)
l2L3VpnMcastPmsiTunnelPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2L3VpnMcastPmsiTunnelPointer.setStatus("current")


class _L2L3VpnMcastPmsiTunnelIf_Type(RowPointer):
    """Custom type l2L3VpnMcastPmsiTunnelIf based on RowPointer"""
    defaultValue = (0, 0)


_L2L3VpnMcastPmsiTunnelIf_Type.__name__ = "RowPointer"
_L2L3VpnMcastPmsiTunnelIf_Object = MibTableColumn
l2L3VpnMcastPmsiTunnelIf = _L2L3VpnMcastPmsiTunnelIf_Object(
    (1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 6),
    _L2L3VpnMcastPmsiTunnelIf_Type()
)
l2L3VpnMcastPmsiTunnelIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2L3VpnMcastPmsiTunnelIf.setStatus("current")
_L2L3VpnMcastConformance_ObjectIdentity = ObjectIdentity
l2L3VpnMcastConformance = _L2L3VpnMcastConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 245, 2)
)
_L2L3VpnMcastCompliances_ObjectIdentity = ObjectIdentity
l2L3VpnMcastCompliances = _L2L3VpnMcastCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 245, 2, 1)
)
_L2L3VpnMcastGroups_ObjectIdentity = ObjectIdentity
l2L3VpnMcastGroups = _L2L3VpnMcastGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 245, 2, 2)
)

# Managed Objects groups

l2L3VpnMcastCoreGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 245, 2, 2, 1)
)
l2L3VpnMcastCoreGroup.setObjects(
      *(("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMCastPmsiTunnelLeafInfoRequired"),
        ("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelAttributeMplsLabel"))
)
if mibBuilder.loadTexts:
    l2L3VpnMcastCoreGroup.setStatus("current")

l2L3VpnMcastOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 245, 2, 2, 2)
)
l2L3VpnMcastOptionalGroup.setObjects(
      *(("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelPointer"),
        ("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelIf"))
)
if mibBuilder.loadTexts:
    l2L3VpnMcastOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

l2L3VpnMcastCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 245, 2, 1, 1)
)
l2L3VpnMcastCoreCompliance.setObjects(
    ("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastCoreGroup")
)
if mibBuilder.loadTexts:
    l2L3VpnMcastCoreCompliance.setStatus(
        "current"
    )

l2L3VpnMcastFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 245, 2, 1, 2)
)
l2L3VpnMcastFullCompliance.setObjects(
      *(("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastCoreGroup"),
        ("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastOptionalGroup"))
)
if mibBuilder.loadTexts:
    l2L3VpnMcastFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "L2L3-VPN-MULTICAST-MIB",
    **{"l2L3VpnMcastMIB": l2L3VpnMcastMIB,
       "l2L3VpnMcastStates": l2L3VpnMcastStates,
       "l2L3VpnMcastPmsiTunnelAttributeTable": l2L3VpnMcastPmsiTunnelAttributeTable,
       "l2L3VpnMcastPmsiTunnelAttributeEntry": l2L3VpnMcastPmsiTunnelAttributeEntry,
       "l2L3VpnMcastPmsiTunnelAttributeType": l2L3VpnMcastPmsiTunnelAttributeType,
       "l2L3VpnMcastPmsiTunnelAttributeId": l2L3VpnMcastPmsiTunnelAttributeId,
       "l2L3VpnMCastPmsiTunnelLeafInfoRequired": l2L3VpnMCastPmsiTunnelLeafInfoRequired,
       "l2L3VpnMcastPmsiTunnelAttributeMplsLabel": l2L3VpnMcastPmsiTunnelAttributeMplsLabel,
       "l2L3VpnMcastPmsiTunnelPointer": l2L3VpnMcastPmsiTunnelPointer,
       "l2L3VpnMcastPmsiTunnelIf": l2L3VpnMcastPmsiTunnelIf,
       "l2L3VpnMcastConformance": l2L3VpnMcastConformance,
       "l2L3VpnMcastCompliances": l2L3VpnMcastCompliances,
       "l2L3VpnMcastCoreCompliance": l2L3VpnMcastCoreCompliance,
       "l2L3VpnMcastFullCompliance": l2L3VpnMcastFullCompliance,
       "l2L3VpnMcastGroups": l2L3VpnMcastGroups,
       "l2L3VpnMcastCoreGroup": l2L3VpnMcastCoreGroup,
       "l2L3VpnMcastOptionalGroup": l2L3VpnMcastOptionalGroup}
)
