# SNMP MIB module (WWP-LEOS-VPLS-TAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-LEOS-VPLS-TAG-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:32:44 2025
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosVplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28)
)
if mibBuilder.loadTexts:
    wwpLeosVplsMIB.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosVplsMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBObjects = _WwpLeosVplsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1)
)
_WwpLeosVpls_ObjectIdentity = ObjectIdentity
wwpLeosVpls = _WwpLeosVpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1)
)
_WwpLeosVplsVirtualCircuitTable_Object = MibTable
wwpLeosVplsVirtualCircuitTable = _WwpLeosVplsVirtualCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitTable.setStatus("current")
_WwpLeosVplsVirtualCircuitEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitEntry = _WwpLeosVplsVirtualCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1)
)
wwpLeosVplsVirtualCircuitEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualCircuitIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEntry.setStatus("current")


class _WwpLeosVplsVirtualCircuitIndex_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualCircuitIndex_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitIndex_Object = MibTableColumn
wwpLeosVplsVirtualCircuitIndex = _WwpLeosVplsVirtualCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 1),
    _WwpLeosVplsVirtualCircuitIndex_Type()
)
wwpLeosVplsVirtualCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitIndex.setStatus("current")
_WwpLeosVplsVirtualCircuitProviderVlanId_Type = VlanId
_WwpLeosVplsVirtualCircuitProviderVlanId_Object = MibTableColumn
wwpLeosVplsVirtualCircuitProviderVlanId = _WwpLeosVplsVirtualCircuitProviderVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 2),
    _WwpLeosVplsVirtualCircuitProviderVlanId_Type()
)
wwpLeosVplsVirtualCircuitProviderVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitProviderVlanId.setStatus("current")


class _WwpLeosVplsVirtualCircuitType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mpls", 2))
    )


_WwpLeosVplsVirtualCircuitType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitType_Object = MibTableColumn
wwpLeosVplsVirtualCircuitType = _WwpLeosVplsVirtualCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 3),
    _WwpLeosVplsVirtualCircuitType_Type()
)
wwpLeosVplsVirtualCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitType.setStatus("current")


class _WwpLeosVplsVirtualCircuitName_Type(DisplayString):
    """Custom type wwpLeosVplsVirtualCircuitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WwpLeosVplsVirtualCircuitName_Type.__name__ = "DisplayString"
_WwpLeosVplsVirtualCircuitName_Object = MibTableColumn
wwpLeosVplsVirtualCircuitName = _WwpLeosVplsVirtualCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 4),
    _WwpLeosVplsVirtualCircuitName_Type()
)
wwpLeosVplsVirtualCircuitName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitName.setStatus("current")


class _WwpLeosVplsVirtualCircuitIngressVcLabel_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitIngressVcLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsVirtualCircuitIngressVcLabel_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitIngressVcLabel_Object = MibTableColumn
wwpLeosVplsVirtualCircuitIngressVcLabel = _WwpLeosVplsVirtualCircuitIngressVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 5),
    _WwpLeosVplsVirtualCircuitIngressVcLabel_Type()
)
wwpLeosVplsVirtualCircuitIngressVcLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitIngressVcLabel.setStatus("current")


class _WwpLeosVplsVirtualCircuitEgressVcLabel_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitEgressVcLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsVirtualCircuitEgressVcLabel_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitEgressVcLabel_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEgressVcLabel = _WwpLeosVplsVirtualCircuitEgressVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 6),
    _WwpLeosVplsVirtualCircuitEgressVcLabel_Type()
)
wwpLeosVplsVirtualCircuitEgressVcLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEgressVcLabel.setStatus("current")


class _WwpLeosVplsVirtualCircuitTunnelIndx_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitTunnelIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualCircuitTunnelIndx_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitTunnelIndx_Object = MibTableColumn
wwpLeosVplsVirtualCircuitTunnelIndx = _WwpLeosVplsVirtualCircuitTunnelIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 7),
    _WwpLeosVplsVirtualCircuitTunnelIndx_Type()
)
wwpLeosVplsVirtualCircuitTunnelIndx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitTunnelIndx.setStatus("current")
_WwpLeosVplsVirtualCircuitStatus_Type = RowStatus
_WwpLeosVplsVirtualCircuitStatus_Object = MibTableColumn
wwpLeosVplsVirtualCircuitStatus = _WwpLeosVplsVirtualCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 8),
    _WwpLeosVplsVirtualCircuitStatus_Type()
)
wwpLeosVplsVirtualCircuitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitStatus.setStatus("current")
_WwpLeosVplsVirtualCircuitEtherTypeTable_Object = MibTable
wwpLeosVplsVirtualCircuitEtherTypeTable = _WwpLeosVplsVirtualCircuitEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEtherTypeTable.setStatus("current")
_WwpLeosVplsVirtualCircuitEtherTypeEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitEtherTypeEntry = _WwpLeosVplsVirtualCircuitEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 2, 1)
)
wwpLeosVplsVirtualCircuitEtherTypeEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualCircuitPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEtherTypeEntry.setStatus("current")


class _WwpLeosVplsVirtualCircuitPortId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualCircuitPortId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitPortId_Object = MibTableColumn
wwpLeosVplsVirtualCircuitPortId = _WwpLeosVplsVirtualCircuitPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 2, 1, 1),
    _WwpLeosVplsVirtualCircuitPortId_Type()
)
wwpLeosVplsVirtualCircuitPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitPortId.setStatus("current")


class _WwpLeosVplsVirtualCircuitEtherType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitEtherType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type8100", 1),
          ("type9100", 2))
    )


_WwpLeosVplsVirtualCircuitEtherType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitEtherType_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEtherType = _WwpLeosVplsVirtualCircuitEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 2, 1, 2),
    _WwpLeosVplsVirtualCircuitEtherType_Type()
)
wwpLeosVplsVirtualCircuitEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEtherType.setStatus("current")
_WwpLeosVplsTunnelGlobalAttrs_ObjectIdentity = ObjectIdentity
wwpLeosVplsTunnelGlobalAttrs = _WwpLeosVplsTunnelGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 3)
)


class _WwpLeosVplsTunnelFixedTTL_Type(Integer32):
    """Custom type wwpLeosVplsTunnelFixedTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_WwpLeosVplsTunnelFixedTTL_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelFixedTTL_Object = MibScalar
wwpLeosVplsTunnelFixedTTL = _WwpLeosVplsTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 3, 1),
    _WwpLeosVplsTunnelFixedTTL_Type()
)
wwpLeosVplsTunnelFixedTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelFixedTTL.setStatus("current")
_WwpLeosVplsTunnelTable_Object = MibTable
wwpLeosVplsTunnelTable = _WwpLeosVplsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelTable.setStatus("current")
_WwpLeosVplsTunnelEntry_Object = MibTableRow
wwpLeosVplsTunnelEntry = _WwpLeosVplsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1)
)
wwpLeosVplsTunnelEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsTunnelId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelEntry.setStatus("current")


class _WwpLeosVplsTunnelId_Type(Integer32):
    """Custom type wwpLeosVplsTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsTunnelId_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelId_Object = MibTableColumn
wwpLeosVplsTunnelId = _WwpLeosVplsTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 1),
    _WwpLeosVplsTunnelId_Type()
)
wwpLeosVplsTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelId.setStatus("current")


class _WwpLeosVplsTunnelName_Type(DisplayString):
    """Custom type wwpLeosVplsTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WwpLeosVplsTunnelName_Type.__name__ = "DisplayString"
_WwpLeosVplsTunnelName_Object = MibTableColumn
wwpLeosVplsTunnelName = _WwpLeosVplsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 2),
    _WwpLeosVplsTunnelName_Type()
)
wwpLeosVplsTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelName.setStatus("current")


class _WwpLeosVplsTunnelIngressLabel_Type(Integer32):
    """Custom type wwpLeosVplsTunnelIngressLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsTunnelIngressLabel_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelIngressLabel_Object = MibTableColumn
wwpLeosVplsTunnelIngressLabel = _WwpLeosVplsTunnelIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 3),
    _WwpLeosVplsTunnelIngressLabel_Type()
)
wwpLeosVplsTunnelIngressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelIngressLabel.setStatus("current")


class _WwpLeosVplsTunnelEgressLabel_Type(Integer32):
    """Custom type wwpLeosVplsTunnelEgressLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsTunnelEgressLabel_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelEgressLabel_Object = MibTableColumn
wwpLeosVplsTunnelEgressLabel = _WwpLeosVplsTunnelEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 4),
    _WwpLeosVplsTunnelEgressLabel_Type()
)
wwpLeosVplsTunnelEgressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelEgressLabel.setStatus("current")


class _WwpLeosVplsTunnelTransportVlanId_Type(Integer32):
    """Custom type wwpLeosVplsTunnelTransportVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsTunnelTransportVlanId_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelTransportVlanId_Object = MibTableColumn
wwpLeosVplsTunnelTransportVlanId = _WwpLeosVplsTunnelTransportVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 5),
    _WwpLeosVplsTunnelTransportVlanId_Type()
)
wwpLeosVplsTunnelTransportVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelTransportVlanId.setStatus("current")
_WwpLeosVplsTunnelDestAddrType_Type = AddressFamilyNumbers
_WwpLeosVplsTunnelDestAddrType_Object = MibTableColumn
wwpLeosVplsTunnelDestAddrType = _WwpLeosVplsTunnelDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 6),
    _WwpLeosVplsTunnelDestAddrType_Type()
)
wwpLeosVplsTunnelDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelDestAddrType.setStatus("current")
_WwpLeosVplsTunnelDestAddr_Type = DisplayString
_WwpLeosVplsTunnelDestAddr_Object = MibTableColumn
wwpLeosVplsTunnelDestAddr = _WwpLeosVplsTunnelDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 7),
    _WwpLeosVplsTunnelDestAddr_Type()
)
wwpLeosVplsTunnelDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelDestAddr.setStatus("current")
_WwpLeosVplsTunnelResolvedDestIp_Type = IpAddress
_WwpLeosVplsTunnelResolvedDestIp_Object = MibTableColumn
wwpLeosVplsTunnelResolvedDestIp = _WwpLeosVplsTunnelResolvedDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 8),
    _WwpLeosVplsTunnelResolvedDestIp_Type()
)
wwpLeosVplsTunnelResolvedDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelResolvedDestIp.setStatus("current")
_WwpLeosVplsTunnelDestResolvedMac_Type = MacAddress
_WwpLeosVplsTunnelDestResolvedMac_Object = MibTableColumn
wwpLeosVplsTunnelDestResolvedMac = _WwpLeosVplsTunnelDestResolvedMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 9),
    _WwpLeosVplsTunnelDestResolvedMac_Type()
)
wwpLeosVplsTunnelDestResolvedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelDestResolvedMac.setStatus("current")


class _WwpLeosVplsTunnelOperStatus_Type(Integer32):
    """Custom type wwpLeosVplsTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_WwpLeosVplsTunnelOperStatus_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelOperStatus_Object = MibTableColumn
wwpLeosVplsTunnelOperStatus = _WwpLeosVplsTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 10),
    _WwpLeosVplsTunnelOperStatus_Type()
)
wwpLeosVplsTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelOperStatus.setStatus("current")


class _WwpLeosVplsTunnelEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsTunnelEncapCosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("inheritVc", 2),
          ("inheritVs", 3))
    )


_WwpLeosVplsTunnelEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsTunnelEncapCosPolicy = _WwpLeosVplsTunnelEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 11),
    _WwpLeosVplsTunnelEncapCosPolicy_Type()
)
wwpLeosVplsTunnelEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelEncapCosPolicy.setStatus("current")


class _WwpLeosVplsTunnelEncapFixedExp_Type(Integer32):
    """Custom type wwpLeosVplsTunnelEncapFixedExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsTunnelEncapFixedExp_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelEncapFixedExp_Object = MibTableColumn
wwpLeosVplsTunnelEncapFixedExp = _WwpLeosVplsTunnelEncapFixedExp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 12),
    _WwpLeosVplsTunnelEncapFixedExp_Type()
)
wwpLeosVplsTunnelEncapFixedExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelEncapFixedExp.setStatus("current")


class _WwpLeosVplsTunnelTTLPolicy_Type(Integer32):
    """Custom type wwpLeosVplsTunnelTTLPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pipe", 1),
          ("uniform", 2))
    )


_WwpLeosVplsTunnelTTLPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelTTLPolicy_Object = MibTableColumn
wwpLeosVplsTunnelTTLPolicy = _WwpLeosVplsTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 13),
    _WwpLeosVplsTunnelTTLPolicy_Type()
)
wwpLeosVplsTunnelTTLPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelTTLPolicy.setStatus("current")
_WwpLeosVplsTunnelSrcIpAddrType_Type = AddressFamilyNumbers
_WwpLeosVplsTunnelSrcIpAddrType_Object = MibTableColumn
wwpLeosVplsTunnelSrcIpAddrType = _WwpLeosVplsTunnelSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 14),
    _WwpLeosVplsTunnelSrcIpAddrType_Type()
)
wwpLeosVplsTunnelSrcIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelSrcIpAddrType.setStatus("current")
_WwpLeosVplsTunnelSrcIpAddr_Type = DisplayString
_WwpLeosVplsTunnelSrcIpAddr_Object = MibTableColumn
wwpLeosVplsTunnelSrcIpAddr = _WwpLeosVplsTunnelSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 15),
    _WwpLeosVplsTunnelSrcIpAddr_Type()
)
wwpLeosVplsTunnelSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelSrcIpAddr.setStatus("current")
_WwpLeosVplsTunnelSrcResolvedIpAddr_Type = IpAddress
_WwpLeosVplsTunnelSrcResolvedIpAddr_Object = MibTableColumn
wwpLeosVplsTunnelSrcResolvedIpAddr = _WwpLeosVplsTunnelSrcResolvedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 16),
    _WwpLeosVplsTunnelSrcResolvedIpAddr_Type()
)
wwpLeosVplsTunnelSrcResolvedIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelSrcResolvedIpAddr.setStatus("current")
_WwpLeosVplsTunnelStatus_Type = RowStatus
_WwpLeosVplsTunnelStatus_Object = MibTableColumn
wwpLeosVplsTunnelStatus = _WwpLeosVplsTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 4, 1, 17),
    _WwpLeosVplsTunnelStatus_Type()
)
wwpLeosVplsTunnelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelStatus.setStatus("current")
_WwpLeosVplsVirtualSwitchTable_Object = MibTable
wwpLeosVplsVirtualSwitchTable = _WwpLeosVplsVirtualSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchTable.setStatus("current")
_WwpLeosVplsVirtualSwitchEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEntry = _WwpLeosVplsVirtualSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1)
)
wwpLeosVplsVirtualSwitchEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualSwitchIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchIndx_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchIndx_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchIndx_Object = MibTableColumn
wwpLeosVplsVirtualSwitchIndx = _WwpLeosVplsVirtualSwitchIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 1),
    _WwpLeosVplsVirtualSwitchIndx_Type()
)
wwpLeosVplsVirtualSwitchIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchIndx.setStatus("current")


class _WwpLeosVplsVirtualSwitchName_Type(DisplayString):
    """Custom type wwpLeosVplsVirtualSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WwpLeosVplsVirtualSwitchName_Type.__name__ = "DisplayString"
_WwpLeosVplsVirtualSwitchName_Object = MibTableColumn
wwpLeosVplsVirtualSwitchName = _WwpLeosVplsVirtualSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 2),
    _WwpLeosVplsVirtualSwitchName_Type()
)
wwpLeosVplsVirtualSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchName.setStatus("current")


class _WwpLeosVplsVirtualSwitchPriVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchPriVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVplsVirtualSwitchPriVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchPriVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchPriVc = _WwpLeosVplsVirtualSwitchPriVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 3),
    _WwpLeosVplsVirtualSwitchPriVc_Type()
)
wwpLeosVplsVirtualSwitchPriVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchPriVc.setStatus("current")


class _WwpLeosVplsVirtualSwitchSecVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchSecVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVplsVirtualSwitchSecVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchSecVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchSecVc = _WwpLeosVplsVirtualSwitchSecVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 4),
    _WwpLeosVplsVirtualSwitchSecVc_Type()
)
wwpLeosVplsVirtualSwitchSecVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchSecVc.setStatus("current")


class _WwpLeosVplsVirtualSwitchActiveVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchActiveVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primVc", 2),
          ("secVc", 3))
    )


_WwpLeosVplsVirtualSwitchActiveVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchActiveVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchActiveVc = _WwpLeosVplsVirtualSwitchActiveVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 5),
    _WwpLeosVplsVirtualSwitchActiveVc_Type()
)
wwpLeosVplsVirtualSwitchActiveVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchActiveVc.setStatus("current")


class _WwpLeosVplsVirtualSwitchEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEncapCosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("inheritDot1dPri", 2),
          ("inheritIpPrec", 3),
          ("inheritPhbg", 4))
    )


_WwpLeosVplsVirtualSwitchEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEncapCosPolicy = _WwpLeosVplsVirtualSwitchEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 6),
    _WwpLeosVplsVirtualSwitchEncapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEncapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEncapFixedDot1dPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEncapFixedDot1dPri = _WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 7),
    _WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchEncapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEncapFixedDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchDecapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchDecapCosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("inheritVc", 2),
          ("inheritTunnel", 3),
          ("leave", 4))
    )


_WwpLeosVplsVirtualSwitchDecapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchDecapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchDecapCosPolicy = _WwpLeosVplsVirtualSwitchDecapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 8),
    _WwpLeosVplsVirtualSwitchDecapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchDecapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchDecapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchDecapFixedDot1dPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchDecapFixedDot1dPri = _WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 9),
    _WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchDecapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchDecapFixedDot1dPri.setStatus("current")
_WwpLeosVplsVirtualSwitchSubscriberVlan_Type = VlanId
_WwpLeosVplsVirtualSwitchSubscriberVlan_Object = MibTableColumn
wwpLeosVplsVirtualSwitchSubscriberVlan = _WwpLeosVplsVirtualSwitchSubscriberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 10),
    _WwpLeosVplsVirtualSwitchSubscriberVlan_Type()
)
wwpLeosVplsVirtualSwitchSubscriberVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchSubscriberVlan.setStatus("current")


class _WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState = _WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 11),
    _WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type()
)
wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState.setStatus("current")


class _WwpLeosVplsVirtualSwitchType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mpls", 2))
    )


_WwpLeosVplsVirtualSwitchType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchType_Object = MibTableColumn
wwpLeosVplsVirtualSwitchType = _WwpLeosVplsVirtualSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 12),
    _WwpLeosVplsVirtualSwitchType_Type()
)
wwpLeosVplsVirtualSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchType.setStatus("current")
_WwpLeosVplsVirtualSwitchStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchStatus = _WwpLeosVplsVirtualSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 13),
    _WwpLeosVplsVirtualSwitchStatus_Type()
)
wwpLeosVplsVirtualSwitchStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchStatus.setStatus("current")
_WwpLeosVplsVirtualSwitchMemberTable_Object = MibTable
wwpLeosVplsVirtualSwitchMemberTable = _WwpLeosVplsVirtualSwitchMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberTable.setStatus("current")
_WwpLeosVplsVirtualSwitchMemberEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMemberEntry = _WwpLeosVplsVirtualSwitchMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 6, 1)
)
wwpLeosVplsVirtualSwitchMemberEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualSwitchIndx"),
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualSwitchMemberPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchMemberPortId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMemberPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchMemberPortId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMemberPortId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMemberPortId = _WwpLeosVplsVirtualSwitchMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 6, 1, 1),
    _WwpLeosVplsVirtualSwitchMemberPortId_Type()
)
wwpLeosVplsVirtualSwitchMemberPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberPortId.setStatus("current")
_WwpLeosVplsVirtualSwitchMemberStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchMemberStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMemberStatus = _WwpLeosVplsVirtualSwitchMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 6, 1, 2),
    _WwpLeosVplsVirtualSwitchMemberStatus_Type()
)
wwpLeosVplsVirtualSwitchMemberStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberStatus.setStatus("current")
_WwpLeosVplsSwitchCtrlProtocolTable_Object = MibTable
wwpLeosVplsSwitchCtrlProtocolTable = _WwpLeosVplsSwitchCtrlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchCtrlProtocolTable.setStatus("current")
_WwpLeosVplsSwitchCtrlProtocolEntry_Object = MibTableRow
wwpLeosVplsSwitchCtrlProtocolEntry = _WwpLeosVplsSwitchCtrlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 7, 1)
)
wwpLeosVplsSwitchCtrlProtocolEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualSwitchIndx"),
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsSwitchCtrlProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchCtrlProtocolEntry.setStatus("current")


class _WwpLeosVplsSwitchCtrlProtocolNum_Type(Integer32):
    """Custom type wwpLeosVplsSwitchCtrlProtocolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("l28021x", 1),
          ("rstp", 2),
          ("ciscoCdp", 3),
          ("ciscoDtp", 4),
          ("ciscoPagp", 5),
          ("ciscoPvst", 6),
          ("ciscoUplinkFast", 7),
          ("ciscoUdlp", 8),
          ("ciscoVtp", 9),
          ("gvrp", 10),
          ("lacp", 11),
          ("lacpMarker", 12),
          ("oam", 13),
          ("lldp", 14),
          ("vlanBridge", 15))
    )


_WwpLeosVplsSwitchCtrlProtocolNum_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchCtrlProtocolNum_Object = MibTableColumn
wwpLeosVplsSwitchCtrlProtocolNum = _WwpLeosVplsSwitchCtrlProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 7, 1, 1),
    _WwpLeosVplsSwitchCtrlProtocolNum_Type()
)
wwpLeosVplsSwitchCtrlProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchCtrlProtocolNum.setStatus("current")


class _WwpLeosVplsSwitchCtrlType_Type(Integer32):
    """Custom type wwpLeosVplsSwitchCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("peer", 2),
          ("tunnel", 3))
    )


_WwpLeosVplsSwitchCtrlType_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchCtrlType_Object = MibTableColumn
wwpLeosVplsSwitchCtrlType = _WwpLeosVplsSwitchCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 7, 1, 2),
    _WwpLeosVplsSwitchCtrlType_Type()
)
wwpLeosVplsSwitchCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchCtrlType.setStatus("current")
_WwpLeosVplsSwitchReservedVlanTable_Object = MibTable
wwpLeosVplsSwitchReservedVlanTable = _WwpLeosVplsSwitchReservedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 8)
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchReservedVlanTable.setStatus("current")
_WwpLeosVplsSwitchReservedVlanEntry_Object = MibTableRow
wwpLeosVplsSwitchReservedVlanEntry = _WwpLeosVplsSwitchReservedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 8, 1)
)
wwpLeosVplsSwitchReservedVlanEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsSwitchReservedVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchReservedVlanEntry.setStatus("current")


class _WwpLeosVplsSwitchReservedVlanId_Type(Integer32):
    """Custom type wwpLeosVplsSwitchReservedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosVplsSwitchReservedVlanId_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchReservedVlanId_Object = MibTableColumn
wwpLeosVplsSwitchReservedVlanId = _WwpLeosVplsSwitchReservedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 8, 1, 1),
    _WwpLeosVplsSwitchReservedVlanId_Type()
)
wwpLeosVplsSwitchReservedVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchReservedVlanId.setStatus("current")
_WwpLeosVplsSwitchReservedVlanStatus_Type = RowStatus
_WwpLeosVplsSwitchReservedVlanStatus_Object = MibTableColumn
wwpLeosVplsSwitchReservedVlanStatus = _WwpLeosVplsSwitchReservedVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 8, 1, 2),
    _WwpLeosVplsSwitchReservedVlanStatus_Type()
)
wwpLeosVplsSwitchReservedVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchReservedVlanStatus.setStatus("current")
_WwpLeosVplsVirtualCircuitStatsTable_Object = MibTable
wwpLeosVplsVirtualCircuitStatsTable = _WwpLeosVplsVirtualCircuitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitStatsTable.setStatus("current")
_WwpLeosVplsVirtualCircuitStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitStatsEntry = _WwpLeosVplsVirtualCircuitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 1)
)
wwpLeosVplsVirtualCircuitStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualCircuitIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitStatsEntry.setStatus("current")
_WwpLeosVplsVirtualCircuitTxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitTxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitTxBytesHi = _WwpLeosVplsVirtualCircuitTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 1, 1),
    _WwpLeosVplsVirtualCircuitTxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitTxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitTxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitTxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitTxBytesLo = _WwpLeosVplsVirtualCircuitTxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 1, 2),
    _WwpLeosVplsVirtualCircuitTxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitTxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitTxBytesLo.setStatus("current")
_WwpLeosVplsVirtualCircuitRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitRxBytesHi = _WwpLeosVplsVirtualCircuitRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 1, 3),
    _WwpLeosVplsVirtualCircuitRxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitRxBytesLo = _WwpLeosVplsVirtualCircuitRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 1, 4),
    _WwpLeosVplsVirtualCircuitRxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitRxBytesLo.setStatus("current")
_WwpLeosVplsVirtualSwitchMemberStatsTable_Object = MibTable
wwpLeosVplsVirtualSwitchMemberStatsTable = _WwpLeosVplsVirtualSwitchMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberStatsTable.setStatus("current")
_WwpLeosVplsVirtualSwitchMemberStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMemberStatsEntry = _WwpLeosVplsVirtualSwitchMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10, 1)
)
wwpLeosVplsVirtualSwitchMemberStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualSwitchIndx"),
    (0, "WWP-LEOS-VPLS-TAG-MIB", "wwpLeosVplsVirtualSwitchMemberPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberStatsEntry.setStatus("current")
_WwpLeosVplsVirtualSwitchMemberRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualSwitchMemberRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMemberRxBytesHi = _WwpLeosVplsVirtualSwitchMemberRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10, 1, 1),
    _WwpLeosVplsVirtualSwitchMemberRxBytesHi_Type()
)
wwpLeosVplsVirtualSwitchMemberRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualSwitchMemberRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualSwitchMemberRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMemberRxBytesLo = _WwpLeosVplsVirtualSwitchMemberRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10, 1, 2),
    _WwpLeosVplsVirtualSwitchMemberRxBytesLo_Type()
)
wwpLeosVplsVirtualSwitchMemberRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberRxBytesLo.setStatus("current")
_WwpLeosVplsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBNotificationPrefix = _WwpLeosVplsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 2)
)
_WwpLeosVplsMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBNotifications = _WwpLeosVplsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 2, 0)
)
_WwpLeosVplsMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBConformance = _WwpLeosVplsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 3)
)
_WwpLeosVplsMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBCompliances = _WwpLeosVplsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 3, 1)
)
_WwpLeosVplsMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBGroups = _WwpLeosVplsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-VPLS-TAG-MIB",
    **{"VlanId": VlanId,
       "wwpLeosVplsMIB": wwpLeosVplsMIB,
       "wwpLeosVplsMIBObjects": wwpLeosVplsMIBObjects,
       "wwpLeosVpls": wwpLeosVpls,
       "wwpLeosVplsVirtualCircuitTable": wwpLeosVplsVirtualCircuitTable,
       "wwpLeosVplsVirtualCircuitEntry": wwpLeosVplsVirtualCircuitEntry,
       "wwpLeosVplsVirtualCircuitIndex": wwpLeosVplsVirtualCircuitIndex,
       "wwpLeosVplsVirtualCircuitProviderVlanId": wwpLeosVplsVirtualCircuitProviderVlanId,
       "wwpLeosVplsVirtualCircuitType": wwpLeosVplsVirtualCircuitType,
       "wwpLeosVplsVirtualCircuitName": wwpLeosVplsVirtualCircuitName,
       "wwpLeosVplsVirtualCircuitIngressVcLabel": wwpLeosVplsVirtualCircuitIngressVcLabel,
       "wwpLeosVplsVirtualCircuitEgressVcLabel": wwpLeosVplsVirtualCircuitEgressVcLabel,
       "wwpLeosVplsVirtualCircuitTunnelIndx": wwpLeosVplsVirtualCircuitTunnelIndx,
       "wwpLeosVplsVirtualCircuitStatus": wwpLeosVplsVirtualCircuitStatus,
       "wwpLeosVplsVirtualCircuitEtherTypeTable": wwpLeosVplsVirtualCircuitEtherTypeTable,
       "wwpLeosVplsVirtualCircuitEtherTypeEntry": wwpLeosVplsVirtualCircuitEtherTypeEntry,
       "wwpLeosVplsVirtualCircuitPortId": wwpLeosVplsVirtualCircuitPortId,
       "wwpLeosVplsVirtualCircuitEtherType": wwpLeosVplsVirtualCircuitEtherType,
       "wwpLeosVplsTunnelGlobalAttrs": wwpLeosVplsTunnelGlobalAttrs,
       "wwpLeosVplsTunnelFixedTTL": wwpLeosVplsTunnelFixedTTL,
       "wwpLeosVplsTunnelTable": wwpLeosVplsTunnelTable,
       "wwpLeosVplsTunnelEntry": wwpLeosVplsTunnelEntry,
       "wwpLeosVplsTunnelId": wwpLeosVplsTunnelId,
       "wwpLeosVplsTunnelName": wwpLeosVplsTunnelName,
       "wwpLeosVplsTunnelIngressLabel": wwpLeosVplsTunnelIngressLabel,
       "wwpLeosVplsTunnelEgressLabel": wwpLeosVplsTunnelEgressLabel,
       "wwpLeosVplsTunnelTransportVlanId": wwpLeosVplsTunnelTransportVlanId,
       "wwpLeosVplsTunnelDestAddrType": wwpLeosVplsTunnelDestAddrType,
       "wwpLeosVplsTunnelDestAddr": wwpLeosVplsTunnelDestAddr,
       "wwpLeosVplsTunnelResolvedDestIp": wwpLeosVplsTunnelResolvedDestIp,
       "wwpLeosVplsTunnelDestResolvedMac": wwpLeosVplsTunnelDestResolvedMac,
       "wwpLeosVplsTunnelOperStatus": wwpLeosVplsTunnelOperStatus,
       "wwpLeosVplsTunnelEncapCosPolicy": wwpLeosVplsTunnelEncapCosPolicy,
       "wwpLeosVplsTunnelEncapFixedExp": wwpLeosVplsTunnelEncapFixedExp,
       "wwpLeosVplsTunnelTTLPolicy": wwpLeosVplsTunnelTTLPolicy,
       "wwpLeosVplsTunnelSrcIpAddrType": wwpLeosVplsTunnelSrcIpAddrType,
       "wwpLeosVplsTunnelSrcIpAddr": wwpLeosVplsTunnelSrcIpAddr,
       "wwpLeosVplsTunnelSrcResolvedIpAddr": wwpLeosVplsTunnelSrcResolvedIpAddr,
       "wwpLeosVplsTunnelStatus": wwpLeosVplsTunnelStatus,
       "wwpLeosVplsVirtualSwitchTable": wwpLeosVplsVirtualSwitchTable,
       "wwpLeosVplsVirtualSwitchEntry": wwpLeosVplsVirtualSwitchEntry,
       "wwpLeosVplsVirtualSwitchIndx": wwpLeosVplsVirtualSwitchIndx,
       "wwpLeosVplsVirtualSwitchName": wwpLeosVplsVirtualSwitchName,
       "wwpLeosVplsVirtualSwitchPriVc": wwpLeosVplsVirtualSwitchPriVc,
       "wwpLeosVplsVirtualSwitchSecVc": wwpLeosVplsVirtualSwitchSecVc,
       "wwpLeosVplsVirtualSwitchActiveVc": wwpLeosVplsVirtualSwitchActiveVc,
       "wwpLeosVplsVirtualSwitchEncapCosPolicy": wwpLeosVplsVirtualSwitchEncapCosPolicy,
       "wwpLeosVplsVirtualSwitchEncapFixedDot1dPri": wwpLeosVplsVirtualSwitchEncapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchDecapCosPolicy": wwpLeosVplsVirtualSwitchDecapCosPolicy,
       "wwpLeosVplsVirtualSwitchDecapFixedDot1dPri": wwpLeosVplsVirtualSwitchDecapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchSubscriberVlan": wwpLeosVplsVirtualSwitchSubscriberVlan,
       "wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState": wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState,
       "wwpLeosVplsVirtualSwitchType": wwpLeosVplsVirtualSwitchType,
       "wwpLeosVplsVirtualSwitchStatus": wwpLeosVplsVirtualSwitchStatus,
       "wwpLeosVplsVirtualSwitchMemberTable": wwpLeosVplsVirtualSwitchMemberTable,
       "wwpLeosVplsVirtualSwitchMemberEntry": wwpLeosVplsVirtualSwitchMemberEntry,
       "wwpLeosVplsVirtualSwitchMemberPortId": wwpLeosVplsVirtualSwitchMemberPortId,
       "wwpLeosVplsVirtualSwitchMemberStatus": wwpLeosVplsVirtualSwitchMemberStatus,
       "wwpLeosVplsSwitchCtrlProtocolTable": wwpLeosVplsSwitchCtrlProtocolTable,
       "wwpLeosVplsSwitchCtrlProtocolEntry": wwpLeosVplsSwitchCtrlProtocolEntry,
       "wwpLeosVplsSwitchCtrlProtocolNum": wwpLeosVplsSwitchCtrlProtocolNum,
       "wwpLeosVplsSwitchCtrlType": wwpLeosVplsSwitchCtrlType,
       "wwpLeosVplsSwitchReservedVlanTable": wwpLeosVplsSwitchReservedVlanTable,
       "wwpLeosVplsSwitchReservedVlanEntry": wwpLeosVplsSwitchReservedVlanEntry,
       "wwpLeosVplsSwitchReservedVlanId": wwpLeosVplsSwitchReservedVlanId,
       "wwpLeosVplsSwitchReservedVlanStatus": wwpLeosVplsSwitchReservedVlanStatus,
       "wwpLeosVplsVirtualCircuitStatsTable": wwpLeosVplsVirtualCircuitStatsTable,
       "wwpLeosVplsVirtualCircuitStatsEntry": wwpLeosVplsVirtualCircuitStatsEntry,
       "wwpLeosVplsVirtualCircuitTxBytesHi": wwpLeosVplsVirtualCircuitTxBytesHi,
       "wwpLeosVplsVirtualCircuitTxBytesLo": wwpLeosVplsVirtualCircuitTxBytesLo,
       "wwpLeosVplsVirtualCircuitRxBytesHi": wwpLeosVplsVirtualCircuitRxBytesHi,
       "wwpLeosVplsVirtualCircuitRxBytesLo": wwpLeosVplsVirtualCircuitRxBytesLo,
       "wwpLeosVplsVirtualSwitchMemberStatsTable": wwpLeosVplsVirtualSwitchMemberStatsTable,
       "wwpLeosVplsVirtualSwitchMemberStatsEntry": wwpLeosVplsVirtualSwitchMemberStatsEntry,
       "wwpLeosVplsVirtualSwitchMemberRxBytesHi": wwpLeosVplsVirtualSwitchMemberRxBytesHi,
       "wwpLeosVplsVirtualSwitchMemberRxBytesLo": wwpLeosVplsVirtualSwitchMemberRxBytesLo,
       "wwpLeosVplsMIBNotificationPrefix": wwpLeosVplsMIBNotificationPrefix,
       "wwpLeosVplsMIBNotifications": wwpLeosVplsMIBNotifications,
       "wwpLeosVplsMIBConformance": wwpLeosVplsMIBConformance,
       "wwpLeosVplsMIBCompliances": wwpLeosVplsMIBCompliances,
       "wwpLeosVplsMIBGroups": wwpLeosVplsMIBGroups}
)
