# SNMP MIB module (EXTREME-MPLS-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-MPLS-TE-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
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

(extremeMplsMIB,) = mibBuilder.importSymbols(
    "EXTREME-MPLS-MIB",
    "extremeMplsMIB")

(mplsTunnelEgressLSRId,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance) = mibBuilder.importSymbols(
    "MPLS-TE-STD-MIB",
    "mplsTunnelEgressLSRId",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance")

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

extremeMplsTeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeMplsTeScalars_ObjectIdentity = ObjectIdentity
extremeMplsTeScalars = _ExtremeMplsTeScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 1)
)
_ExtremeMplsTeObjects_ObjectIdentity = ObjectIdentity
extremeMplsTeObjects = _ExtremeMplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2)
)
_ExtremeMplsTunnelTable_Object = MibTable
extremeMplsTunnelTable = _ExtremeMplsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1)
)
if mibBuilder.loadTexts:
    extremeMplsTunnelTable.setStatus("current")
_ExtremeMplsTunnelEntry_Object = MibTableRow
extremeMplsTunnelEntry = _ExtremeMplsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1, 1)
)
extremeMplsTunnelEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    extremeMplsTunnelEntry.setStatus("current")


class _MplsTunnelRedundancyType_Type(Integer32):
    """Custom type mplsTunnelRedundancyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_MplsTunnelRedundancyType_Type.__name__ = "Integer32"
_MplsTunnelRedundancyType_Object = MibTableColumn
mplsTunnelRedundancyType = _MplsTunnelRedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1, 1, 1),
    _MplsTunnelRedundancyType_Type()
)
mplsTunnelRedundancyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelRedundancyType.setStatus("current")


class _MplsTunnelRedundancyStatus_Type(Integer32):
    """Custom type mplsTunnelRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_MplsTunnelRedundancyStatus_Type.__name__ = "Integer32"
_MplsTunnelRedundancyStatus_Object = MibTableColumn
mplsTunnelRedundancyStatus = _MplsTunnelRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1, 1, 2),
    _MplsTunnelRedundancyStatus_Type()
)
mplsTunnelRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelRedundancyStatus.setStatus("current")


class _MplsTunnelTransportStatus_Type(Bits):
    """Custom type mplsTunnelTransportStatus based on Bits"""
    namedValues = NamedValues(
        *(("allowAllIp", 0),
          ("allowAssignedIpOnly", 1),
          ("allowAllLayer2Vpn", 2),
          ("allowAsignedLayer2VpnOnly", 3))
    )

_MplsTunnelTransportStatus_Type.__name__ = "Bits"
_MplsTunnelTransportStatus_Object = MibTableColumn
mplsTunnelTransportStatus = _MplsTunnelTransportStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1, 1, 3),
    _MplsTunnelTransportStatus_Type()
)
mplsTunnelTransportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelTransportStatus.setStatus("current")
_ExtremeMplsTeConformance_ObjectIdentity = ObjectIdentity
extremeMplsTeConformance = _ExtremeMplsTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-MPLS-TE-MIB",
    **{"extremeMplsTeMIB": extremeMplsTeMIB,
       "extremeMplsTeScalars": extremeMplsTeScalars,
       "extremeMplsTeObjects": extremeMplsTeObjects,
       "extremeMplsTunnelTable": extremeMplsTunnelTable,
       "extremeMplsTunnelEntry": extremeMplsTunnelEntry,
       "mplsTunnelRedundancyType": mplsTunnelRedundancyType,
       "mplsTunnelRedundancyStatus": mplsTunnelRedundancyStatus,
       "mplsTunnelTransportStatus": mplsTunnelTransportStatus,
       "extremeMplsTeConformance": extremeMplsTeConformance}
)
