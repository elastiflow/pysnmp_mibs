# SNMP MIB module (RUIJIE-BGP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-BGP4-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:44 2025
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

(bgpPeerEntry,
 bgpPeerRemoteAddr) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgpPeerEntry",
    "bgpPeerRemoteAddr")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InetAddress,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetAutonomousSystemNumber")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieBgp4MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38)
)
if mibBuilder.loadTexts:
    ruijieBgp4MIB.setRevisions(
        ("2003-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieBgpID(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class RuijieBgpVrfName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



# MIB Managed Objects in the order of their OIDs

_RuijieBgpBaseScalars_ObjectIdentity = ObjectIdentity
ruijieBgpBaseScalars = _RuijieBgpBaseScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1)
)
_RuijieBgpSupportedCapabilities_ObjectIdentity = ObjectIdentity
ruijieBgpSupportedCapabilities = _RuijieBgpSupportedCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 1)
)
_RuijieBgpCapabilitySupportAvailable_Type = TruthValue
_RuijieBgpCapabilitySupportAvailable_Object = MibScalar
ruijieBgpCapabilitySupportAvailable = _RuijieBgpCapabilitySupportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 1, 1),
    _RuijieBgpCapabilitySupportAvailable_Type()
)
ruijieBgpCapabilitySupportAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpCapabilitySupportAvailable.setStatus("current")
_RuijieBgpSupportedCapabilitiesTable_Object = MibTable
ruijieBgpSupportedCapabilitiesTable = _RuijieBgpSupportedCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieBgpSupportedCapabilitiesTable.setStatus("current")
_RuijieBgpSupportedCapabilitiesEntry_Object = MibTableRow
ruijieBgpSupportedCapabilitiesEntry = _RuijieBgpSupportedCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 1, 2, 1)
)
ruijieBgpSupportedCapabilitiesEntry.setIndexNames(
    (0, "RUIJIE-BGP4-MIB", "ruijieBgpSupportedCapabilityCode"),
)
if mibBuilder.loadTexts:
    ruijieBgpSupportedCapabilitiesEntry.setStatus("current")


class _RuijieBgpSupportedCapabilityCode_Type(Unsigned32):
    """Custom type ruijieBgpSupportedCapabilityCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieBgpSupportedCapabilityCode_Type.__name__ = "Unsigned32"
_RuijieBgpSupportedCapabilityCode_Object = MibTableColumn
ruijieBgpSupportedCapabilityCode = _RuijieBgpSupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 1, 2, 1, 1),
    _RuijieBgpSupportedCapabilityCode_Type()
)
ruijieBgpSupportedCapabilityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpSupportedCapabilityCode.setStatus("current")
_RuijieBgpSupportedCapability_Type = TruthValue
_RuijieBgpSupportedCapability_Object = MibTableColumn
ruijieBgpSupportedCapability = _RuijieBgpSupportedCapability_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 1, 2, 1, 2),
    _RuijieBgpSupportedCapability_Type()
)
ruijieBgpSupportedCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpSupportedCapability.setStatus("current")
_RuijieBgpBaseScalarExtensions_ObjectIdentity = ObjectIdentity
ruijieBgpBaseScalarExtensions = _RuijieBgpBaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 2)
)
_RuijieBgpBaseScalarRouteReflectExts_ObjectIdentity = ObjectIdentity
ruijieBgpBaseScalarRouteReflectExts = _RuijieBgpBaseScalarRouteReflectExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 2, 1)
)
_RuijieBgpRouteReflector_Type = TruthValue
_RuijieBgpRouteReflector_Object = MibScalar
ruijieBgpRouteReflector = _RuijieBgpRouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 2, 1, 1),
    _RuijieBgpRouteReflector_Type()
)
ruijieBgpRouteReflector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpRouteReflector.setStatus("current")
_RuijieBgpClusterId_Type = RuijieBgpID
_RuijieBgpClusterId_Object = MibScalar
ruijieBgpClusterId = _RuijieBgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 2, 1, 2),
    _RuijieBgpClusterId_Type()
)
ruijieBgpClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpClusterId.setStatus("current")
_RuijieBgpBaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
ruijieBgpBaseScalarASConfedExts = _RuijieBgpBaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 2, 2)
)
_RuijieBgpConfederationRouter_Type = TruthValue
_RuijieBgpConfederationRouter_Object = MibScalar
ruijieBgpConfederationRouter = _RuijieBgpConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 2, 2, 1),
    _RuijieBgpConfederationRouter_Type()
)
ruijieBgpConfederationRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpConfederationRouter.setStatus("current")
_RuijieBgpConfederationId_Type = InetAutonomousSystemNumber
_RuijieBgpConfederationId_Object = MibScalar
ruijieBgpConfederationId = _RuijieBgpConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 2, 2, 2),
    _RuijieBgpConfederationId_Type()
)
ruijieBgpConfederationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpConfederationId.setStatus("current")
_RuijieBgpRpkiSession_ObjectIdentity = ObjectIdentity
ruijieBgpRpkiSession = _RuijieBgpRpkiSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 3)
)
_RuijieBgpRpkiTrap_ObjectIdentity = ObjectIdentity
ruijieBgpRpkiTrap = _RuijieBgpRpkiTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 3, 1)
)
_RuijieBgpRpkiSessionLimit_ObjectIdentity = ObjectIdentity
ruijieBgpRpkiSessionLimit = _RuijieBgpRpkiSessionLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 3, 2)
)
_RuijieBgpRpkiSessionAddrType_Type = InetAddressType
_RuijieBgpRpkiSessionAddrType_Object = MibScalar
ruijieBgpRpkiSessionAddrType = _RuijieBgpRpkiSessionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 3, 2, 1),
    _RuijieBgpRpkiSessionAddrType_Type()
)
ruijieBgpRpkiSessionAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpRpkiSessionAddrType.setStatus("current")
_RuijieBgpRpkiSessionAddr_Type = InetAddress
_RuijieBgpRpkiSessionAddr_Object = MibScalar
ruijieBgpRpkiSessionAddr = _RuijieBgpRpkiSessionAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 3, 2, 2),
    _RuijieBgpRpkiSessionAddr_Type()
)
ruijieBgpRpkiSessionAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpRpkiSessionAddr.setStatus("current")


class _RuijieBgpRpkiSessionRoaLimit_Type(Unsigned32):
    """Custom type ruijieBgpRpkiSessionRoaLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RuijieBgpRpkiSessionRoaLimit_Type.__name__ = "Unsigned32"
_RuijieBgpRpkiSessionRoaLimit_Object = MibScalar
ruijieBgpRpkiSessionRoaLimit = _RuijieBgpRpkiSessionRoaLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 3, 2, 3),
    _RuijieBgpRpkiSessionRoaLimit_Type()
)
ruijieBgpRpkiSessionRoaLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpRpkiSessionRoaLimit.setStatus("current")
_RuijieBgpPeer_ObjectIdentity = ObjectIdentity
ruijieBgpPeer = _RuijieBgpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2)
)
_RuijieBgpPeerPrefixInfoTable_Object = MibTable
ruijieBgpPeerPrefixInfoTable = _RuijieBgpPeerPrefixInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerPrefixInfoTable.setStatus("current")
_RuijieBgpPeerPrefixInfoEntry_Object = MibTableRow
ruijieBgpPeerPrefixInfoEntry = _RuijieBgpPeerPrefixInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerPrefixInfoEntry.setStatus("current")


class _RuijieBgpPeerPrefixLimit_Type(Unsigned32):
    """Custom type ruijieBgpPeerPrefixLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieBgpPeerPrefixLimit_Type.__name__ = "Unsigned32"
_RuijieBgpPeerPrefixLimit_Object = MibTableColumn
ruijieBgpPeerPrefixLimit = _RuijieBgpPeerPrefixLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 1, 1, 1),
    _RuijieBgpPeerPrefixLimit_Type()
)
ruijieBgpPeerPrefixLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerPrefixLimit.setStatus("deprecated")
_RuijieBgpPeerPrefixAccepted_Type = Counter32
_RuijieBgpPeerPrefixAccepted_Object = MibTableColumn
ruijieBgpPeerPrefixAccepted = _RuijieBgpPeerPrefixAccepted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 1, 1, 2),
    _RuijieBgpPeerPrefixAccepted_Type()
)
ruijieBgpPeerPrefixAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerPrefixAccepted.setStatus("deprecated")
_RuijieBgpPeerPrefixAdvertised_Type = Counter32
_RuijieBgpPeerPrefixAdvertised_Object = MibTableColumn
ruijieBgpPeerPrefixAdvertised = _RuijieBgpPeerPrefixAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 1, 1, 3),
    _RuijieBgpPeerPrefixAdvertised_Type()
)
ruijieBgpPeerPrefixAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerPrefixAdvertised.setStatus("deprecated")
_RuijieBgpPeerCapabilities_ObjectIdentity = ObjectIdentity
ruijieBgpPeerCapabilities = _RuijieBgpPeerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2)
)
_RuijieBgpPeerCapsAnnouncedTable_Object = MibTable
ruijieBgpPeerCapsAnnouncedTable = _RuijieBgpPeerCapsAnnouncedTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerCapsAnnouncedTable.setStatus("current")
_RuijieBgpPeerCapsAnnouncedEntry_Object = MibTableRow
ruijieBgpPeerCapsAnnouncedEntry = _RuijieBgpPeerCapsAnnouncedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2, 1, 1)
)
ruijieBgpPeerCapsAnnouncedEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "RUIJIE-BGP4-MIB", "ruijieBgpPeerCapAnnouncedCode"),
)
if mibBuilder.loadTexts:
    ruijieBgpPeerCapsAnnouncedEntry.setStatus("current")


class _RuijieBgpPeerCapAnnouncedCode_Type(Unsigned32):
    """Custom type ruijieBgpPeerCapAnnouncedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieBgpPeerCapAnnouncedCode_Type.__name__ = "Unsigned32"
_RuijieBgpPeerCapAnnouncedCode_Object = MibTableColumn
ruijieBgpPeerCapAnnouncedCode = _RuijieBgpPeerCapAnnouncedCode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2, 1, 1, 1),
    _RuijieBgpPeerCapAnnouncedCode_Type()
)
ruijieBgpPeerCapAnnouncedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerCapAnnouncedCode.setStatus("current")


class _RuijieBgpPeerCapAnnouncedValue_Type(OctetString):
    """Custom type ruijieBgpPeerCapAnnouncedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieBgpPeerCapAnnouncedValue_Type.__name__ = "OctetString"
_RuijieBgpPeerCapAnnouncedValue_Object = MibTableColumn
ruijieBgpPeerCapAnnouncedValue = _RuijieBgpPeerCapAnnouncedValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2, 1, 1, 2),
    _RuijieBgpPeerCapAnnouncedValue_Type()
)
ruijieBgpPeerCapAnnouncedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerCapAnnouncedValue.setStatus("current")
_RuijieBgpPeerCapsReceivedTable_Object = MibTable
ruijieBgpPeerCapsReceivedTable = _RuijieBgpPeerCapsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerCapsReceivedTable.setStatus("current")
_RuijieBgpPeerCapsReceivedEntry_Object = MibTableRow
ruijieBgpPeerCapsReceivedEntry = _RuijieBgpPeerCapsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2, 2, 1)
)
ruijieBgpPeerCapsReceivedEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "RUIJIE-BGP4-MIB", "ruijieBgpPeerCapReceivedCode"),
)
if mibBuilder.loadTexts:
    ruijieBgpPeerCapsReceivedEntry.setStatus("current")


class _RuijieBgpPeerCapReceivedCode_Type(Unsigned32):
    """Custom type ruijieBgpPeerCapReceivedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieBgpPeerCapReceivedCode_Type.__name__ = "Unsigned32"
_RuijieBgpPeerCapReceivedCode_Object = MibTableColumn
ruijieBgpPeerCapReceivedCode = _RuijieBgpPeerCapReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2, 2, 1, 1),
    _RuijieBgpPeerCapReceivedCode_Type()
)
ruijieBgpPeerCapReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerCapReceivedCode.setStatus("current")


class _RuijieBgpPeerCapReceivedValue_Type(OctetString):
    """Custom type ruijieBgpPeerCapReceivedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieBgpPeerCapReceivedValue_Type.__name__ = "OctetString"
_RuijieBgpPeerCapReceivedValue_Object = MibTableColumn
ruijieBgpPeerCapReceivedValue = _RuijieBgpPeerCapReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 2, 2, 1, 3),
    _RuijieBgpPeerCapReceivedValue_Type()
)
ruijieBgpPeerCapReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerCapReceivedValue.setStatus("current")
_RuijieBgpPeerExtensions_ObjectIdentity = ObjectIdentity
ruijieBgpPeerExtensions = _RuijieBgpPeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3)
)
_RuijieBgpPeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
ruijieBgpPeerRouteReflectionExts = _RuijieBgpPeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3, 1)
)
_RuijieBgpPeerReflectorClientTable_Object = MibTable
ruijieBgpPeerReflectorClientTable = _RuijieBgpPeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerReflectorClientTable.setStatus("current")
_RuijieBgpPeerReflectorClientEntry_Object = MibTableRow
ruijieBgpPeerReflectorClientEntry = _RuijieBgpPeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerReflectorClientEntry.setStatus("current")


class _RuijieBgpPeerReflectorClient_Type(Integer32):
    """Custom type ruijieBgpPeerReflectorClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonClient", 0),
          ("client", 1),
          ("meshedClient", 2))
    )


_RuijieBgpPeerReflectorClient_Type.__name__ = "Integer32"
_RuijieBgpPeerReflectorClient_Object = MibTableColumn
ruijieBgpPeerReflectorClient = _RuijieBgpPeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3, 1, 1, 1, 1),
    _RuijieBgpPeerReflectorClient_Type()
)
ruijieBgpPeerReflectorClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerReflectorClient.setStatus("current")
_RuijieBgpPeerASConfederationExts_ObjectIdentity = ObjectIdentity
ruijieBgpPeerASConfederationExts = _RuijieBgpPeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3, 2)
)
_RuijieBgpPeerConfedMemberTable_Object = MibTable
ruijieBgpPeerConfedMemberTable = _RuijieBgpPeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerConfedMemberTable.setStatus("current")
_RuijieBgpPeerConfedMemberEntry_Object = MibTableRow
ruijieBgpPeerConfedMemberEntry = _RuijieBgpPeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerConfedMemberEntry.setStatus("current")
_RuijieBgpPeerConfedMember_Type = TruthValue
_RuijieBgpPeerConfedMember_Object = MibTableColumn
ruijieBgpPeerConfedMember = _RuijieBgpPeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 3, 2, 1, 1, 1),
    _RuijieBgpPeerConfedMember_Type()
)
ruijieBgpPeerConfedMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerConfedMember.setStatus("current")
_RuijieBgpPeerTrap_ObjectIdentity = ObjectIdentity
ruijieBgpPeerTrap = _RuijieBgpPeerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4)
)
_RuijieBgpPeerTable_Object = MibTable
ruijieBgpPeerTable = _RuijieBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 5)
)
if mibBuilder.loadTexts:
    ruijieBgpPeerTable.setStatus("current")
_RuijieBgpPeerEntry_Object = MibTableRow
ruijieBgpPeerEntry = _RuijieBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 5, 1)
)
ruijieBgpPeerEntry.setIndexNames(
    (0, "RUIJIE-BGP4-MIB", "ruijieBgpPeerVrfName"),
    (0, "RUIJIE-BGP4-MIB", "ruijieBgpPeerType"),
    (0, "RUIJIE-BGP4-MIB", "ruijieBgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    ruijieBgpPeerEntry.setStatus("current")
_RuijieBgpPeerVrfName_Type = RuijieBgpVrfName
_RuijieBgpPeerVrfName_Object = MibTableColumn
ruijieBgpPeerVrfName = _RuijieBgpPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 5, 1, 1),
    _RuijieBgpPeerVrfName_Type()
)
ruijieBgpPeerVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerVrfName.setStatus("current")
_RuijieBgpPeerType_Type = InetAddressType
_RuijieBgpPeerType_Object = MibTableColumn
ruijieBgpPeerType = _RuijieBgpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 5, 1, 2),
    _RuijieBgpPeerType_Type()
)
ruijieBgpPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerType.setStatus("current")
_RuijieBgpPeerRemoteAddr_Type = InetAddress
_RuijieBgpPeerRemoteAddr_Object = MibTableColumn
ruijieBgpPeerRemoteAddr = _RuijieBgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 5, 1, 3),
    _RuijieBgpPeerRemoteAddr_Type()
)
ruijieBgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpPeerRemoteAddr.setStatus("current")


class _RuijiebgpPeerLastError_Type(OctetString):
    """Custom type ruijiebgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_RuijiebgpPeerLastError_Type.__name__ = "OctetString"
_RuijiebgpPeerLastError_Object = MibTableColumn
ruijiebgpPeerLastError = _RuijiebgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 5, 1, 4),
    _RuijiebgpPeerLastError_Type()
)
ruijiebgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiebgpPeerLastError.setStatus("current")


class _RuijiebgpPeerState_Type(Integer32):
    """Custom type ruijiebgpPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_RuijiebgpPeerState_Type.__name__ = "Integer32"
_RuijiebgpPeerState_Object = MibTableColumn
ruijiebgpPeerState = _RuijiebgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 5, 1, 5),
    _RuijiebgpPeerState_Type()
)
ruijiebgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiebgpPeerState.setStatus("current")
_RuijieBgpPeerRouteLimit_ObjectIdentity = ObjectIdentity
ruijieBgpPeerRouteLimit = _RuijieBgpPeerRouteLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 6)
)
_RuijieBgpAddressFamilyAfi_Type = AddressFamilyNumbers
_RuijieBgpAddressFamilyAfi_Object = MibScalar
ruijieBgpAddressFamilyAfi = _RuijieBgpAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 6, 1),
    _RuijieBgpAddressFamilyAfi_Type()
)
ruijieBgpAddressFamilyAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpAddressFamilyAfi.setStatus("current")


class _RuijieBgpAddressFamilySafi_Type(Integer32):
    """Custom type ruijieBgpAddressFamilySafi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              65,
              66,
              70,
              71,
              73,
              128,
              129,
              133,
              134,
              140)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("unicast-multicast", 3),
          ("mpls-label", 4),
          ("static-multicast", 5),
          ("mdt-map", 6),
          ("vpls", 65),
          ("mdt", 66),
          ("evpn", 70),
          ("bgp-ls", 71),
          ("sr-policy", 73),
          ("mpls-vpn", 128),
          ("vr-labeled", 129),
          ("flowspec", 133),
          ("flowspec-vpn", 134),
          ("vr-unlabeled", 140))
    )


_RuijieBgpAddressFamilySafi_Type.__name__ = "Integer32"
_RuijieBgpAddressFamilySafi_Object = MibScalar
ruijieBgpAddressFamilySafi = _RuijieBgpAddressFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 6, 2),
    _RuijieBgpAddressFamilySafi_Type()
)
ruijieBgpAddressFamilySafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpAddressFamilySafi.setStatus("current")
_RuijieBgpRouteLimitNum_Type = Unsigned32
_RuijieBgpRouteLimitNum_Object = MibScalar
ruijieBgpRouteLimitNum = _RuijieBgpRouteLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 6, 3),
    _RuijieBgpRouteLimitNum_Type()
)
ruijieBgpRouteLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpRouteLimitNum.setStatus("current")


class _RuijieBgpRouteLimitThreshold_Type(Integer32):
    """Custom type ruijieBgpRouteLimitThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieBgpRouteLimitThreshold_Type.__name__ = "Integer32"
_RuijieBgpRouteLimitThreshold_Object = MibScalar
ruijieBgpRouteLimitThreshold = _RuijieBgpRouteLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 6, 4),
    _RuijieBgpRouteLimitThreshold_Type()
)
ruijieBgpRouteLimitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpRouteLimitThreshold.setStatus("current")
_RuijieBgpRouteLimitCurrentNum_Type = Unsigned32
_RuijieBgpRouteLimitCurrentNum_Object = MibScalar
ruijieBgpRouteLimitCurrentNum = _RuijieBgpRouteLimitCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 6, 5),
    _RuijieBgpRouteLimitCurrentNum_Type()
)
ruijieBgpRouteLimitCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpRouteLimitCurrentNum.setStatus("current")
_RuijieBgpRouteVrfName_Type = RuijieBgpVrfName
_RuijieBgpRouteVrfName_Object = MibScalar
ruijieBgpRouteVrfName = _RuijieBgpRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 6, 6),
    _RuijieBgpRouteVrfName_Type()
)
ruijieBgpRouteVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBgpRouteVrfName.setStatus("current")
_RuijieBgpConformance_ObjectIdentity = ObjectIdentity
ruijieBgpConformance = _RuijieBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 3)
)
_RuijieBgpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieBgpMIBCompliances = _RuijieBgpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 3, 1)
)
_RuijieBgpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieBgpMIBGroups = _RuijieBgpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 3, 2)
)
bgpPeerEntry.registerAugmentions(
    ("RUIJIE-BGP4-MIB",
     "ruijieBgpPeerPrefixInfoEntry")
)
ruijieBgpPeerPrefixInfoEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions(
    ("RUIJIE-BGP4-MIB",
     "ruijieBgpPeerReflectorClientEntry")
)
ruijieBgpPeerReflectorClientEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgpPeerEntry.registerAugmentions(
    ("RUIJIE-BGP4-MIB",
     "ruijieBgpPeerConfedMemberEntry")
)
ruijieBgpPeerConfedMemberEntry.setIndexNames(*bgpPeerEntry.getIndexNames())

# Managed Objects groups


# Notification objects

ruijiebgpRpkiRoaExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 3, 1, 1)
)
ruijiebgpRpkiRoaExceed.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijieBgpRouteVrfName"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRpkiSessionAddrType"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRpkiSessionAddr"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRpkiSessionRoaLimit"))
)
if mibBuilder.loadTexts:
    ruijiebgpRpkiRoaExceed.setStatus(
        "current"
    )

ruijiebgpRpkiRoaExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 1, 3, 1, 2)
)
ruijiebgpRpkiRoaExceedClear.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijieBgpRouteVrfName"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRpkiSessionAddrType"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRpkiSessionAddr"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRpkiSessionRoaLimit"))
)
if mibBuilder.loadTexts:
    ruijiebgpRpkiRoaExceedClear.setStatus(
        "current"
    )

ruijiebgpEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4, 1)
)
ruijiebgpEstablished.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijiebgpPeerLastError"),
        ("RUIJIE-BGP4-MIB", "ruijiebgpPeerState"))
)
if mibBuilder.loadTexts:
    ruijiebgpEstablished.setStatus(
        "current"
    )

ruijiebgpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4, 2)
)
ruijiebgpBackwardTransition.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijiebgpPeerLastError"),
        ("RUIJIE-BGP4-MIB", "ruijiebgpPeerState"))
)
if mibBuilder.loadTexts:
    ruijiebgpBackwardTransition.setStatus(
        "current"
    )

ruijiebgpRouteThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4, 3)
)
ruijiebgpRouteThresholdExceed.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijieBgpAddressFamilyAfi"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpAddressFamilySafi"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpPeerType"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpPeerRemoteAddr"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitNum"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    ruijiebgpRouteThresholdExceed.setStatus(
        "current"
    )

ruijiebgpRouteThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4, 4)
)
ruijiebgpRouteThresholdClear.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijieBgpAddressFamilyAfi"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpAddressFamilySafi"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpPeerType"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpPeerRemoteAddr"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitNum"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    ruijiebgpRouteThresholdClear.setStatus(
        "current"
    )

ruijiebgpRouteExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4, 5)
)
ruijiebgpRouteExceed.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijieBgpAddressFamilyAfi"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpAddressFamilySafi"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpPeerType"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpPeerRemoteAddr"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitNum"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    ruijiebgpRouteExceed.setStatus(
        "current"
    )

ruijiebgpRouteExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4, 6)
)
ruijiebgpRouteExceedClear.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijieBgpAddressFamilyAfi"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpAddressFamilySafi"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpPeerType"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpPeerRemoteAddr"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitNum"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    ruijiebgpRouteExceedClear.setStatus(
        "current"
    )

ruijiebgpVrfRouteExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4, 7)
)
ruijiebgpVrfRouteExceed.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijieBgpRouteVrfName"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitNum"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitCurrentNum"))
)
if mibBuilder.loadTexts:
    ruijiebgpVrfRouteExceed.setStatus(
        "current"
    )

ruijiebgpVrfRouteExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 38, 2, 4, 8)
)
ruijiebgpVrfRouteExceedClear.setObjects(
      *(("RUIJIE-BGP4-MIB", "ruijieBgpRouteVrfName"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitNum"),
        ("RUIJIE-BGP4-MIB", "ruijieBgpRouteLimitCurrentNum"))
)
if mibBuilder.loadTexts:
    ruijiebgpVrfRouteExceedClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-BGP4-MIB",
    **{"RuijieBgpID": RuijieBgpID,
       "RuijieBgpVrfName": RuijieBgpVrfName,
       "ruijieBgp4MIB": ruijieBgp4MIB,
       "ruijieBgpBaseScalars": ruijieBgpBaseScalars,
       "ruijieBgpSupportedCapabilities": ruijieBgpSupportedCapabilities,
       "ruijieBgpCapabilitySupportAvailable": ruijieBgpCapabilitySupportAvailable,
       "ruijieBgpSupportedCapabilitiesTable": ruijieBgpSupportedCapabilitiesTable,
       "ruijieBgpSupportedCapabilitiesEntry": ruijieBgpSupportedCapabilitiesEntry,
       "ruijieBgpSupportedCapabilityCode": ruijieBgpSupportedCapabilityCode,
       "ruijieBgpSupportedCapability": ruijieBgpSupportedCapability,
       "ruijieBgpBaseScalarExtensions": ruijieBgpBaseScalarExtensions,
       "ruijieBgpBaseScalarRouteReflectExts": ruijieBgpBaseScalarRouteReflectExts,
       "ruijieBgpRouteReflector": ruijieBgpRouteReflector,
       "ruijieBgpClusterId": ruijieBgpClusterId,
       "ruijieBgpBaseScalarASConfedExts": ruijieBgpBaseScalarASConfedExts,
       "ruijieBgpConfederationRouter": ruijieBgpConfederationRouter,
       "ruijieBgpConfederationId": ruijieBgpConfederationId,
       "ruijieBgpRpkiSession": ruijieBgpRpkiSession,
       "ruijieBgpRpkiTrap": ruijieBgpRpkiTrap,
       "ruijiebgpRpkiRoaExceed": ruijiebgpRpkiRoaExceed,
       "ruijiebgpRpkiRoaExceedClear": ruijiebgpRpkiRoaExceedClear,
       "ruijieBgpRpkiSessionLimit": ruijieBgpRpkiSessionLimit,
       "ruijieBgpRpkiSessionAddrType": ruijieBgpRpkiSessionAddrType,
       "ruijieBgpRpkiSessionAddr": ruijieBgpRpkiSessionAddr,
       "ruijieBgpRpkiSessionRoaLimit": ruijieBgpRpkiSessionRoaLimit,
       "ruijieBgpPeer": ruijieBgpPeer,
       "ruijieBgpPeerPrefixInfoTable": ruijieBgpPeerPrefixInfoTable,
       "ruijieBgpPeerPrefixInfoEntry": ruijieBgpPeerPrefixInfoEntry,
       "ruijieBgpPeerPrefixLimit": ruijieBgpPeerPrefixLimit,
       "ruijieBgpPeerPrefixAccepted": ruijieBgpPeerPrefixAccepted,
       "ruijieBgpPeerPrefixAdvertised": ruijieBgpPeerPrefixAdvertised,
       "ruijieBgpPeerCapabilities": ruijieBgpPeerCapabilities,
       "ruijieBgpPeerCapsAnnouncedTable": ruijieBgpPeerCapsAnnouncedTable,
       "ruijieBgpPeerCapsAnnouncedEntry": ruijieBgpPeerCapsAnnouncedEntry,
       "ruijieBgpPeerCapAnnouncedCode": ruijieBgpPeerCapAnnouncedCode,
       "ruijieBgpPeerCapAnnouncedValue": ruijieBgpPeerCapAnnouncedValue,
       "ruijieBgpPeerCapsReceivedTable": ruijieBgpPeerCapsReceivedTable,
       "ruijieBgpPeerCapsReceivedEntry": ruijieBgpPeerCapsReceivedEntry,
       "ruijieBgpPeerCapReceivedCode": ruijieBgpPeerCapReceivedCode,
       "ruijieBgpPeerCapReceivedValue": ruijieBgpPeerCapReceivedValue,
       "ruijieBgpPeerExtensions": ruijieBgpPeerExtensions,
       "ruijieBgpPeerRouteReflectionExts": ruijieBgpPeerRouteReflectionExts,
       "ruijieBgpPeerReflectorClientTable": ruijieBgpPeerReflectorClientTable,
       "ruijieBgpPeerReflectorClientEntry": ruijieBgpPeerReflectorClientEntry,
       "ruijieBgpPeerReflectorClient": ruijieBgpPeerReflectorClient,
       "ruijieBgpPeerASConfederationExts": ruijieBgpPeerASConfederationExts,
       "ruijieBgpPeerConfedMemberTable": ruijieBgpPeerConfedMemberTable,
       "ruijieBgpPeerConfedMemberEntry": ruijieBgpPeerConfedMemberEntry,
       "ruijieBgpPeerConfedMember": ruijieBgpPeerConfedMember,
       "ruijieBgpPeerTrap": ruijieBgpPeerTrap,
       "ruijiebgpEstablished": ruijiebgpEstablished,
       "ruijiebgpBackwardTransition": ruijiebgpBackwardTransition,
       "ruijiebgpRouteThresholdExceed": ruijiebgpRouteThresholdExceed,
       "ruijiebgpRouteThresholdClear": ruijiebgpRouteThresholdClear,
       "ruijiebgpRouteExceed": ruijiebgpRouteExceed,
       "ruijiebgpRouteExceedClear": ruijiebgpRouteExceedClear,
       "ruijiebgpVrfRouteExceed": ruijiebgpVrfRouteExceed,
       "ruijiebgpVrfRouteExceedClear": ruijiebgpVrfRouteExceedClear,
       "ruijieBgpPeerTable": ruijieBgpPeerTable,
       "ruijieBgpPeerEntry": ruijieBgpPeerEntry,
       "ruijieBgpPeerVrfName": ruijieBgpPeerVrfName,
       "ruijieBgpPeerType": ruijieBgpPeerType,
       "ruijieBgpPeerRemoteAddr": ruijieBgpPeerRemoteAddr,
       "ruijiebgpPeerLastError": ruijiebgpPeerLastError,
       "ruijiebgpPeerState": ruijiebgpPeerState,
       "ruijieBgpPeerRouteLimit": ruijieBgpPeerRouteLimit,
       "ruijieBgpAddressFamilyAfi": ruijieBgpAddressFamilyAfi,
       "ruijieBgpAddressFamilySafi": ruijieBgpAddressFamilySafi,
       "ruijieBgpRouteLimitNum": ruijieBgpRouteLimitNum,
       "ruijieBgpRouteLimitThreshold": ruijieBgpRouteLimitThreshold,
       "ruijieBgpRouteLimitCurrentNum": ruijieBgpRouteLimitCurrentNum,
       "ruijieBgpRouteVrfName": ruijieBgpRouteVrfName,
       "ruijieBgpConformance": ruijieBgpConformance,
       "ruijieBgpMIBCompliances": ruijieBgpMIBCompliances,
       "ruijieBgpMIBGroups": ruijieBgpMIBGroups}
)
