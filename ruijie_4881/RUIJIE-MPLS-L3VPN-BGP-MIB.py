# SNMP MIB module (RUIJIE-MPLS-L3VPN-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MPLS-L3VPN-BGP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(bgp4PathAttrIpAddrPrefix,
 bgp4PathAttrIpAddrPrefixLen,
 bgp4PathAttrPeer) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrIpAddrPrefix",
    "bgp4PathAttrIpAddrPrefixLen",
    "bgp4PathAttrPeer")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsL3VpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "mplsL3VpnVrfName")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ruijiemplsL3VpnNbrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100)
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnNbrMIB.setRevisions(
        ("2011-09-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijiemplsL3VpnVrfBgpNbrTable_Object = MibTable
ruijiemplsL3VpnVrfBgpNbrTable = _RuijiemplsL3VpnVrfBgpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 1)
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpNbrTable.setStatus("current")
_RuijiemplsL3VpnVrfBgpNbrEntry_Object = MibTableRow
ruijiemplsL3VpnVrfBgpNbrEntry = _RuijiemplsL3VpnVrfBgpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 1, 1)
)
ruijiemplsL3VpnVrfBgpNbrEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpNbrAddr"),
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpNbrEntry.setStatus("current")


class _RuijiemplsL3VpnVrfBgpNbrRole_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpNbrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ce", 1),
          ("pe", 2))
    )


_RuijiemplsL3VpnVrfBgpNbrRole_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpNbrRole_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpNbrRole = _RuijiemplsL3VpnVrfBgpNbrRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 1, 1, 1),
    _RuijiemplsL3VpnVrfBgpNbrRole_Type()
)
ruijiemplsL3VpnVrfBgpNbrRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpNbrRole.setStatus("current")
_RuijiemplsL3VpnVrfBgpNbrType_Type = InetAddressType
_RuijiemplsL3VpnVrfBgpNbrType_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpNbrType = _RuijiemplsL3VpnVrfBgpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 1, 1, 2),
    _RuijiemplsL3VpnVrfBgpNbrType_Type()
)
ruijiemplsL3VpnVrfBgpNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpNbrType.setStatus("current")
_RuijiemplsL3VpnVrfBgpNbrAddr_Type = InetAddress
_RuijiemplsL3VpnVrfBgpNbrAddr_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpNbrAddr = _RuijiemplsL3VpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 1, 1, 3),
    _RuijiemplsL3VpnVrfBgpNbrAddr_Type()
)
ruijiemplsL3VpnVrfBgpNbrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpNbrAddr.setStatus("current")
_RuijiemplsL3VpnVrfBgpNbrRowStatus_Type = RowStatus
_RuijiemplsL3VpnVrfBgpNbrRowStatus_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpNbrRowStatus = _RuijiemplsL3VpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 1, 1, 4),
    _RuijiemplsL3VpnVrfBgpNbrRowStatus_Type()
)
ruijiemplsL3VpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpNbrRowStatus.setStatus("current")


class _RuijiemplsL3VpnVrfBgpNbrStorageType_Type(StorageType):
    """Custom type ruijiemplsL3VpnVrfBgpNbrStorageType based on StorageType"""
    defaultValue = 2


_RuijiemplsL3VpnVrfBgpNbrStorageType_Type.__name__ = "StorageType"
_RuijiemplsL3VpnVrfBgpNbrStorageType_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpNbrStorageType = _RuijiemplsL3VpnVrfBgpNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 1, 1, 5),
    _RuijiemplsL3VpnVrfBgpNbrStorageType_Type()
)
ruijiemplsL3VpnVrfBgpNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpNbrStorageType.setStatus("current")


class _RuijiemplsL3VpnVrfBgpNbrRemoteAS_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpNbrRemoteAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijiemplsL3VpnVrfBgpNbrRemoteAS_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpNbrRemoteAS_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpNbrRemoteAS = _RuijiemplsL3VpnVrfBgpNbrRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 1, 1, 6),
    _RuijiemplsL3VpnVrfBgpNbrRemoteAS_Type()
)
ruijiemplsL3VpnVrfBgpNbrRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpNbrRemoteAS.setStatus("current")
_RuijiemplsL3VpnVrfBgpPAtrTable_Object = MibTable
ruijiemplsL3VpnVrfBgpPAtrTable = _RuijiemplsL3VpnVrfBgpPAtrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2)
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrTable.setStatus("current")
_RuijiemplsL3VpnVrfBgpPAtrEntry_Object = MibTableRow
ruijiemplsL3VpnVrfBgpPAtrEntry = _RuijiemplsL3VpnVrfBgpPAtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1)
)
ruijiemplsL3VpnVrfBgpPAtrEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"),
    (0, "BGP4-MIB", "bgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrEntry.setStatus("current")
_RuijiemplsL3VpnVrfBgpPAtrPeerType_Type = InetAddressType
_RuijiemplsL3VpnVrfBgpPAtrPeerType_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrPeerType = _RuijiemplsL3VpnVrfBgpPAtrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 1),
    _RuijiemplsL3VpnVrfBgpPAtrPeerType_Type()
)
ruijiemplsL3VpnVrfBgpPAtrPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrPeerType.setStatus("current")
_RuijiemplsL3VpnVrfBgpPAtrIpAddrPfxType_Type = InetAddressType
_RuijiemplsL3VpnVrfBgpPAtrIpAddrPfxType_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrIpAddrPfxType = _RuijiemplsL3VpnVrfBgpPAtrIpAddrPfxType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 2),
    _RuijiemplsL3VpnVrfBgpPAtrIpAddrPfxType_Type()
)
ruijiemplsL3VpnVrfBgpPAtrIpAddrPfxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrIpAddrPfxType.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrOrigin_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_RuijiemplsL3VpnVrfBgpPAtrOrigin_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpPAtrOrigin_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrOrigin = _RuijiemplsL3VpnVrfBgpPAtrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 3),
    _RuijiemplsL3VpnVrfBgpPAtrOrigin_Type()
)
ruijiemplsL3VpnVrfBgpPAtrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrOrigin.setStatus("current")
_RuijiemplsL3VpnVrfBgpPAtrNextHop_Type = InetAddress
_RuijiemplsL3VpnVrfBgpPAtrNextHop_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrNextHop = _RuijiemplsL3VpnVrfBgpPAtrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 4),
    _RuijiemplsL3VpnVrfBgpPAtrNextHop_Type()
)
ruijiemplsL3VpnVrfBgpPAtrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrNextHop.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrASPathSegment_Type(OctetString):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_RuijiemplsL3VpnVrfBgpPAtrASPathSegment_Type.__name__ = "OctetString"
_RuijiemplsL3VpnVrfBgpPAtrASPathSegment_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrASPathSegment = _RuijiemplsL3VpnVrfBgpPAtrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 5),
    _RuijiemplsL3VpnVrfBgpPAtrASPathSegment_Type()
)
ruijiemplsL3VpnVrfBgpPAtrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrASPathSegment.setStatus("current")
_RuijiemplsL3VpnVrfBgpPAtrNextHopType_Type = InetAddressType
_RuijiemplsL3VpnVrfBgpPAtrNextHopType_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrNextHopType = _RuijiemplsL3VpnVrfBgpPAtrNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 6),
    _RuijiemplsL3VpnVrfBgpPAtrNextHopType_Type()
)
ruijiemplsL3VpnVrfBgpPAtrNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrNextHopType.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrMultiExitDisc_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RuijiemplsL3VpnVrfBgpPAtrMultiExitDisc_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpPAtrMultiExitDisc_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrMultiExitDisc = _RuijiemplsL3VpnVrfBgpPAtrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 7),
    _RuijiemplsL3VpnVrfBgpPAtrMultiExitDisc_Type()
)
ruijiemplsL3VpnVrfBgpPAtrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrMultiExitDisc.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrLocalPref_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RuijiemplsL3VpnVrfBgpPAtrLocalPref_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpPAtrLocalPref_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrLocalPref = _RuijiemplsL3VpnVrfBgpPAtrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 8),
    _RuijiemplsL3VpnVrfBgpPAtrLocalPref_Type()
)
ruijiemplsL3VpnVrfBgpPAtrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrLocalPref.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrAtomicAggregate_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRrouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_RuijiemplsL3VpnVrfBgpPAtrAtomicAggregate_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpPAtrAtomicAggregate_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrAtomicAggregate = _RuijiemplsL3VpnVrfBgpPAtrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 9),
    _RuijiemplsL3VpnVrfBgpPAtrAtomicAggregate_Type()
)
ruijiemplsL3VpnVrfBgpPAtrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrAtomicAggregate.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrAggregatorAS_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijiemplsL3VpnVrfBgpPAtrAggregatorAS_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpPAtrAggregatorAS_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrAggregatorAS = _RuijiemplsL3VpnVrfBgpPAtrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 10),
    _RuijiemplsL3VpnVrfBgpPAtrAggregatorAS_Type()
)
ruijiemplsL3VpnVrfBgpPAtrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrAggregatorAS.setStatus("current")
_RuijiemplsL3VpnVrfBgpPAtrAggrAddrType_Type = InetAddressType
_RuijiemplsL3VpnVrfBgpPAtrAggrAddrType_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrAggrAddrType = _RuijiemplsL3VpnVrfBgpPAtrAggrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 11),
    _RuijiemplsL3VpnVrfBgpPAtrAggrAddrType_Type()
)
ruijiemplsL3VpnVrfBgpPAtrAggrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrAggrAddrType.setStatus("current")
_RuijiemplsL3VpnVrfBgpPAtrAggregatorAddr_Type = InetAddress
_RuijiemplsL3VpnVrfBgpPAtrAggregatorAddr_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrAggregatorAddr = _RuijiemplsL3VpnVrfBgpPAtrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 12),
    _RuijiemplsL3VpnVrfBgpPAtrAggregatorAddr_Type()
)
ruijiemplsL3VpnVrfBgpPAtrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrAggregatorAddr.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrCalcLocalPref_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RuijiemplsL3VpnVrfBgpPAtrCalcLocalPref_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpPAtrCalcLocalPref_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrCalcLocalPref = _RuijiemplsL3VpnVrfBgpPAtrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 13),
    _RuijiemplsL3VpnVrfBgpPAtrCalcLocalPref_Type()
)
ruijiemplsL3VpnVrfBgpPAtrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrCalcLocalPref.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrBest_Type(Integer32):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrBest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_RuijiemplsL3VpnVrfBgpPAtrBest_Type.__name__ = "Integer32"
_RuijiemplsL3VpnVrfBgpPAtrBest_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrBest = _RuijiemplsL3VpnVrfBgpPAtrBest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 14),
    _RuijiemplsL3VpnVrfBgpPAtrBest_Type()
)
ruijiemplsL3VpnVrfBgpPAtrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrBest.setStatus("current")


class _RuijiemplsL3VpnVrfBgpPAtrUnknown_Type(OctetString):
    """Custom type ruijiemplsL3VpnVrfBgpPAtrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijiemplsL3VpnVrfBgpPAtrUnknown_Type.__name__ = "OctetString"
_RuijiemplsL3VpnVrfBgpPAtrUnknown_Object = MibTableColumn
ruijiemplsL3VpnVrfBgpPAtrUnknown = _RuijiemplsL3VpnVrfBgpPAtrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 2, 1, 15),
    _RuijiemplsL3VpnVrfBgpPAtrUnknown_Type()
)
ruijiemplsL3VpnVrfBgpPAtrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpPAtrUnknown.setStatus("current")
_RuijiemplsL3VpnVrfBgpNbrCom_ObjectIdentity = ObjectIdentity
ruijiemplsL3VpnVrfBgpNbrCom = _RuijiemplsL3VpnVrfBgpNbrCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 3)
)
_RuijiemplsL3VpnVrfBgpCompliances_ObjectIdentity = ObjectIdentity
ruijiemplsL3VpnVrfBgpCompliances = _RuijiemplsL3VpnVrfBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 3, 1)
)
_RuijiemplsL3VpnVrfBgpGroups_ObjectIdentity = ObjectIdentity
ruijiemplsL3VpnVrfBgpGroups = _RuijiemplsL3VpnVrfBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 3, 2)
)

# Managed Objects groups

ruijiemplsL3VpnVrfBgpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 3, 2, 1)
)
ruijiemplsL3VpnVrfBgpGroup.setObjects(
      *(("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpNbrRole"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpNbrType"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpNbrAddr"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpNbrRowStatus"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpNbrStorageType"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpNbrRemoteAS"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrPeerType"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrIpAddrPfxType"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrOrigin"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrASPathSegment"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrNextHopType"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrNextHop"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrMultiExitDisc"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrLocalPref"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrAtomicAggregate"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrAggregatorAS"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrAggrAddrType"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrAggregatorAddr"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrCalcLocalPref"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrBest"),
        ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpPAtrUnknown"))
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijiemplsL3VpnVrfBgpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 100, 3, 1, 1)
)
ruijiemplsL3VpnVrfBgpCompliance.setObjects(
    ("RUIJIE-MPLS-L3VPN-BGP-MIB", "ruijiemplsL3VpnVrfBgpGroup")
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnVrfBgpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MPLS-L3VPN-BGP-MIB",
    **{"ruijiemplsL3VpnNbrMIB": ruijiemplsL3VpnNbrMIB,
       "ruijiemplsL3VpnVrfBgpNbrTable": ruijiemplsL3VpnVrfBgpNbrTable,
       "ruijiemplsL3VpnVrfBgpNbrEntry": ruijiemplsL3VpnVrfBgpNbrEntry,
       "ruijiemplsL3VpnVrfBgpNbrRole": ruijiemplsL3VpnVrfBgpNbrRole,
       "ruijiemplsL3VpnVrfBgpNbrType": ruijiemplsL3VpnVrfBgpNbrType,
       "ruijiemplsL3VpnVrfBgpNbrAddr": ruijiemplsL3VpnVrfBgpNbrAddr,
       "ruijiemplsL3VpnVrfBgpNbrRowStatus": ruijiemplsL3VpnVrfBgpNbrRowStatus,
       "ruijiemplsL3VpnVrfBgpNbrStorageType": ruijiemplsL3VpnVrfBgpNbrStorageType,
       "ruijiemplsL3VpnVrfBgpNbrRemoteAS": ruijiemplsL3VpnVrfBgpNbrRemoteAS,
       "ruijiemplsL3VpnVrfBgpPAtrTable": ruijiemplsL3VpnVrfBgpPAtrTable,
       "ruijiemplsL3VpnVrfBgpPAtrEntry": ruijiemplsL3VpnVrfBgpPAtrEntry,
       "ruijiemplsL3VpnVrfBgpPAtrPeerType": ruijiemplsL3VpnVrfBgpPAtrPeerType,
       "ruijiemplsL3VpnVrfBgpPAtrIpAddrPfxType": ruijiemplsL3VpnVrfBgpPAtrIpAddrPfxType,
       "ruijiemplsL3VpnVrfBgpPAtrOrigin": ruijiemplsL3VpnVrfBgpPAtrOrigin,
       "ruijiemplsL3VpnVrfBgpPAtrNextHop": ruijiemplsL3VpnVrfBgpPAtrNextHop,
       "ruijiemplsL3VpnVrfBgpPAtrASPathSegment": ruijiemplsL3VpnVrfBgpPAtrASPathSegment,
       "ruijiemplsL3VpnVrfBgpPAtrNextHopType": ruijiemplsL3VpnVrfBgpPAtrNextHopType,
       "ruijiemplsL3VpnVrfBgpPAtrMultiExitDisc": ruijiemplsL3VpnVrfBgpPAtrMultiExitDisc,
       "ruijiemplsL3VpnVrfBgpPAtrLocalPref": ruijiemplsL3VpnVrfBgpPAtrLocalPref,
       "ruijiemplsL3VpnVrfBgpPAtrAtomicAggregate": ruijiemplsL3VpnVrfBgpPAtrAtomicAggregate,
       "ruijiemplsL3VpnVrfBgpPAtrAggregatorAS": ruijiemplsL3VpnVrfBgpPAtrAggregatorAS,
       "ruijiemplsL3VpnVrfBgpPAtrAggrAddrType": ruijiemplsL3VpnVrfBgpPAtrAggrAddrType,
       "ruijiemplsL3VpnVrfBgpPAtrAggregatorAddr": ruijiemplsL3VpnVrfBgpPAtrAggregatorAddr,
       "ruijiemplsL3VpnVrfBgpPAtrCalcLocalPref": ruijiemplsL3VpnVrfBgpPAtrCalcLocalPref,
       "ruijiemplsL3VpnVrfBgpPAtrBest": ruijiemplsL3VpnVrfBgpPAtrBest,
       "ruijiemplsL3VpnVrfBgpPAtrUnknown": ruijiemplsL3VpnVrfBgpPAtrUnknown,
       "ruijiemplsL3VpnVrfBgpNbrCom": ruijiemplsL3VpnVrfBgpNbrCom,
       "ruijiemplsL3VpnVrfBgpCompliances": ruijiemplsL3VpnVrfBgpCompliances,
       "ruijiemplsL3VpnVrfBgpCompliance": ruijiemplsL3VpnVrfBgpCompliance,
       "ruijiemplsL3VpnVrfBgpGroups": ruijiemplsL3VpnVrfBgpGroups,
       "ruijiemplsL3VpnVrfBgpGroup": ruijiemplsL3VpnVrfBgpGroup}
)
