# SNMP MIB module (BELAIR-MESH) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-MESH.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairInterfaces,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairInterfaces")

(BelAirAdminState,
 BelAirEncryptionType,
 BelAirRowStatus) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState",
    "BelAirEncryptionType",
    "BelAirRowStatus")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

belairMeshMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4)
)
if mibBuilder.loadTexts:
    belairMeshMib.setRevisions(
        ("2008-12-03 18:00",
         "2008-11-04 14:39",
         "2008-08-22 14:48",
         "2007-12-05 13:00",
         "2007-10-29 16:30",
         "2007-04-13 18:00",
         "2006-01-12 12:15",
         "2005-10-27 14:00",
         "2005-09-12 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BelAirMeshPortalState(TextualConvention, Integer32):
    status = "current"
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
        *(("yes", 1),
          ("no", 2),
          ("auto", 3),
          ("unknown", 4))
    )



class BelAirMeshPointType(TextualConvention, Integer32):
    status = "current"
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
        *(("terminationPoint", 1),
          ("pointToPoint", 2),
          ("multiPoint", 3),
          ("disabled", 4))
    )



class BelAirMeshPointTopology(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("p2p", 1),
          ("star", 2),
          ("mesh", 3),
          ("mobile", 4),
          ("protection", 5),
          ("singleChannelMesh", 6))
    )



class BelAirMeshPointLinkMap(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_BelairMeshObjects_ObjectIdentity = ObjectIdentity
belairMeshObjects = _BelairMeshObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1)
)
if mibBuilder.loadTexts:
    belairMeshObjects.setStatus("current")
_BelairMeshPointTable_Object = MibTable
belairMeshPointTable = _BelairMeshPointTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    belairMeshPointTable.setStatus("current")
_BelairMeshPointEntry_Object = MibTableRow
belairMeshPointEntry = _BelairMeshPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1)
)
belairMeshPointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    belairMeshPointEntry.setStatus("current")


class _BelairMeshPointId_Type(OctetString):
    """Custom type belairMeshPointId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BelairMeshPointId_Type.__name__ = "OctetString"
_BelairMeshPointId_Object = MibTableColumn
belairMeshPointId = _BelairMeshPointId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 1),
    _BelairMeshPointId_Type()
)
belairMeshPointId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointId.setStatus("current")
_BelairMeshPointChannel_Type = Integer32
_BelairMeshPointChannel_Object = MibTableColumn
belairMeshPointChannel = _BelairMeshPointChannel_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 2),
    _BelairMeshPointChannel_Type()
)
belairMeshPointChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointChannel.setStatus("deprecated")
_BelairMeshPointPrivacyType_Type = BelAirEncryptionType
_BelairMeshPointPrivacyType_Object = MibTableColumn
belairMeshPointPrivacyType = _BelairMeshPointPrivacyType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 3),
    _BelairMeshPointPrivacyType_Type()
)
belairMeshPointPrivacyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointPrivacyType.setStatus("current")


class _BelairMeshPointEncryptionKey_Type(OctetString):
    """Custom type belairMeshPointEncryptionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BelairMeshPointEncryptionKey_Type.__name__ = "OctetString"
_BelairMeshPointEncryptionKey_Object = MibTableColumn
belairMeshPointEncryptionKey = _BelairMeshPointEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 4),
    _BelairMeshPointEncryptionKey_Type()
)
belairMeshPointEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointEncryptionKey.setStatus("current")
_BelairMeshPoinConfigedPortalState_Type = BelAirMeshPortalState
_BelairMeshPoinConfigedPortalState_Object = MibTableColumn
belairMeshPoinConfigedPortalState = _BelairMeshPoinConfigedPortalState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 5),
    _BelairMeshPoinConfigedPortalState_Type()
)
belairMeshPoinConfigedPortalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPoinConfigedPortalState.setStatus("current")
_BelairMeshPointActualPortalState_Type = BelAirMeshPortalState
_BelairMeshPointActualPortalState_Object = MibTableColumn
belairMeshPointActualPortalState = _BelairMeshPointActualPortalState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 6),
    _BelairMeshPointActualPortalState_Type()
)
belairMeshPointActualPortalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshPointActualPortalState.setStatus("current")
_BelairMeshPointType_Type = BelAirMeshPointType
_BelairMeshPointType_Object = MibTableColumn
belairMeshPointType = _BelairMeshPointType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 7),
    _BelairMeshPointType_Type()
)
belairMeshPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointType.setStatus("current")
_BelairMeshPointTopology_Type = BelAirMeshPointTopology
_BelairMeshPointTopology_Object = MibTableColumn
belairMeshPointTopology = _BelairMeshPointTopology_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 8),
    _BelairMeshPointTopology_Type()
)
belairMeshPointTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointTopology.setStatus("current")
_BelairMeshPointLinkMap_Type = BelAirMeshPointLinkMap
_BelairMeshPointLinkMap_Object = MibTableColumn
belairMeshPointLinkMap = _BelairMeshPointLinkMap_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 9),
    _BelairMeshPointLinkMap_Type()
)
belairMeshPointLinkMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointLinkMap.setStatus("current")
_BelairMeshPointAdminState_Type = BelAirAdminState
_BelairMeshPointAdminState_Object = MibTableColumn
belairMeshPointAdminState = _BelairMeshPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 10),
    _BelairMeshPointAdminState_Type()
)
belairMeshPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointAdminState.setStatus("current")


class _BelairMeshPointMinRssi_Type(Integer32):
    """Custom type belairMeshPointMinRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_BelairMeshPointMinRssi_Type.__name__ = "Integer32"
_BelairMeshPointMinRssi_Object = MibTableColumn
belairMeshPointMinRssi = _BelairMeshPointMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 11),
    _BelairMeshPointMinRssi_Type()
)
belairMeshPointMinRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointMinRssi.setStatus("current")


class _BelairMeshPointMobileId_Type(OctetString):
    """Custom type belairMeshPointMobileId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BelairMeshPointMobileId_Type.__name__ = "OctetString"
_BelairMeshPointMobileId_Object = MibTableColumn
belairMeshPointMobileId = _BelairMeshPointMobileId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 12),
    _BelairMeshPointMobileId_Type()
)
belairMeshPointMobileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointMobileId.setStatus("current")
_BelairMeshPointMobileAdminState_Type = BelAirAdminState
_BelairMeshPointMobileAdminState_Object = MibTableColumn
belairMeshPointMobileAdminState = _BelairMeshPointMobileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 13),
    _BelairMeshPointMobileAdminState_Type()
)
belairMeshPointMobileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointMobileAdminState.setStatus("current")
_BelairMeshPointMobileLinkType_Type = BelAirMeshPointTopology
_BelairMeshPointMobileLinkType_Object = MibTableColumn
belairMeshPointMobileLinkType = _BelairMeshPointMobileLinkType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 14),
    _BelairMeshPointMobileLinkType_Type()
)
belairMeshPointMobileLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointMobileLinkType.setStatus("current")
_BelairMeshPointMobileLinkRole_Type = BelAirMeshPointType
_BelairMeshPointMobileLinkRole_Object = MibTableColumn
belairMeshPointMobileLinkRole = _BelairMeshPointMobileLinkRole_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 1, 1, 15),
    _BelairMeshPointMobileLinkRole_Type()
)
belairMeshPointMobileLinkRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairMeshPointMobileLinkRole.setStatus("current")
_BelairMeshIfTable_Object = MibTable
belairMeshIfTable = _BelairMeshIfTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2)
)
if mibBuilder.loadTexts:
    belairMeshIfTable.setStatus("current")
_BelairMeshIfEntry_Object = MibTableRow
belairMeshIfEntry = _BelairMeshIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1)
)
belairMeshIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-MESH", "belairMeshIfIndex"),
)
if mibBuilder.loadTexts:
    belairMeshIfEntry.setStatus("current")
_BelairMeshIfIndex_Type = InterfaceIndex
_BelairMeshIfIndex_Object = MibTableColumn
belairMeshIfIndex = _BelairMeshIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 1),
    _BelairMeshIfIndex_Type()
)
belairMeshIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairMeshIfIndex.setStatus("current")
_BelairMeshIfPeerMac_Type = MacAddress
_BelairMeshIfPeerMac_Object = MibTableColumn
belairMeshIfPeerMac = _BelairMeshIfPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 2),
    _BelairMeshIfPeerMac_Type()
)
belairMeshIfPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfPeerMac.setStatus("current")


class _BelairMeshIfRssi_Type(Integer32):
    """Custom type belairMeshIfRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_BelairMeshIfRssi_Type.__name__ = "Integer32"
_BelairMeshIfRssi_Object = MibTableColumn
belairMeshIfRssi = _BelairMeshIfRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 3),
    _BelairMeshIfRssi_Type()
)
belairMeshIfRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfRssi.setStatus("current")
if mibBuilder.loadTexts:
    belairMeshIfRssi.setUnits("dBm")
_BelairMeshIfForwardingTraffic_Type = TruthValue
_BelairMeshIfForwardingTraffic_Object = MibTableColumn
belairMeshIfForwardingTraffic = _BelairMeshIfForwardingTraffic_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 4),
    _BelairMeshIfForwardingTraffic_Type()
)
belairMeshIfForwardingTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfForwardingTraffic.setStatus("current")


class _BelairMeshIfLinkIndex_Type(Integer32):
    """Custom type belairMeshIfLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BelairMeshIfLinkIndex_Type.__name__ = "Integer32"
_BelairMeshIfLinkIndex_Object = MibTableColumn
belairMeshIfLinkIndex = _BelairMeshIfLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 5),
    _BelairMeshIfLinkIndex_Type()
)
belairMeshIfLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfLinkIndex.setStatus("current")
_BelairMeshIfAge_Type = Integer32
_BelairMeshIfAge_Object = MibTableColumn
belairMeshIfAge = _BelairMeshIfAge_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 6),
    _BelairMeshIfAge_Type()
)
belairMeshIfAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfAge.setStatus("current")


class _BelairMeshIfPeerSysName_Type(OctetString):
    """Custom type belairMeshIfPeerSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BelairMeshIfPeerSysName_Type.__name__ = "OctetString"
_BelairMeshIfPeerSysName_Object = MibTableColumn
belairMeshIfPeerSysName = _BelairMeshIfPeerSysName_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 7),
    _BelairMeshIfPeerSysName_Type()
)
belairMeshIfPeerSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfPeerSysName.setStatus("current")
_BelairMeshIfPeerNodeIp_Type = IpAddress
_BelairMeshIfPeerNodeIp_Object = MibTableColumn
belairMeshIfPeerNodeIp = _BelairMeshIfPeerNodeIp_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 8),
    _BelairMeshIfPeerNodeIp_Type()
)
belairMeshIfPeerNodeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfPeerNodeIp.setStatus("current")


class _BelairMeshIfLinkType_Type(Integer32):
    """Custom type belairMeshIfLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eBhlTypeFixed", 0),
          ("eBhlTypeMobile", 1))
    )


_BelairMeshIfLinkType_Type.__name__ = "Integer32"
_BelairMeshIfLinkType_Object = MibTableColumn
belairMeshIfLinkType = _BelairMeshIfLinkType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 9),
    _BelairMeshIfLinkType_Type()
)
belairMeshIfLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfLinkType.setStatus("current")


class _BelairMeshIfPeerFwdState_Type(Integer32):
    """Custom type belairMeshIfPeerFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ePsFwdUndef", 0),
          ("ePsFwdYes", 1),
          ("ePsFwdNo", 2))
    )


_BelairMeshIfPeerFwdState_Type.__name__ = "Integer32"
_BelairMeshIfPeerFwdState_Object = MibTableColumn
belairMeshIfPeerFwdState = _BelairMeshIfPeerFwdState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 10),
    _BelairMeshIfPeerFwdState_Type()
)
belairMeshIfPeerFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfPeerFwdState.setStatus("current")


class _BelairMeshIfPeerRssi_Type(Integer32):
    """Custom type belairMeshIfPeerRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_BelairMeshIfPeerRssi_Type.__name__ = "Integer32"
_BelairMeshIfPeerRssi_Object = MibTableColumn
belairMeshIfPeerRssi = _BelairMeshIfPeerRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 11),
    _BelairMeshIfPeerRssi_Type()
)
belairMeshIfPeerRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfPeerRssi.setStatus("current")
if mibBuilder.loadTexts:
    belairMeshIfPeerRssi.setUnits("dBm")


class _BelairMeshIfTxFailedRate_Type(Unsigned32):
    """Custom type belairMeshIfTxFailedRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BelairMeshIfTxFailedRate_Type.__name__ = "Unsigned32"
_BelairMeshIfTxFailedRate_Object = MibTableColumn
belairMeshIfTxFailedRate = _BelairMeshIfTxFailedRate_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 2, 1, 12),
    _BelairMeshIfTxFailedRate_Type()
)
belairMeshIfTxFailedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshIfTxFailedRate.setStatus("current")
if mibBuilder.loadTexts:
    belairMeshIfTxFailedRate.setUnits("%")
_BelairMeshExcludedMacTable_Object = MibTable
belairMeshExcludedMacTable = _BelairMeshExcludedMacTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 3)
)
if mibBuilder.loadTexts:
    belairMeshExcludedMacTable.setStatus("current")
_BelairMeshExcludedMacEntry_Object = MibTableRow
belairMeshExcludedMacEntry = _BelairMeshExcludedMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 3, 1)
)
belairMeshExcludedMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-MESH", "belairMeshExcludedMacIndex"),
)
if mibBuilder.loadTexts:
    belairMeshExcludedMacEntry.setStatus("current")


class _BelairMeshExcludedMacIndex_Type(Integer32):
    """Custom type belairMeshExcludedMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BelairMeshExcludedMacIndex_Type.__name__ = "Integer32"
_BelairMeshExcludedMacIndex_Object = MibTableColumn
belairMeshExcludedMacIndex = _BelairMeshExcludedMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 3, 1, 1),
    _BelairMeshExcludedMacIndex_Type()
)
belairMeshExcludedMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairMeshExcludedMacIndex.setStatus("current")
_BelairMeshExcludedMacAddress_Type = MacAddress
_BelairMeshExcludedMacAddress_Object = MibTableColumn
belairMeshExcludedMacAddress = _BelairMeshExcludedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 3, 1, 2),
    _BelairMeshExcludedMacAddress_Type()
)
belairMeshExcludedMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairMeshExcludedMacAddress.setStatus("current")
_BelairMeshExcludedRowStatus_Type = BelAirRowStatus
_BelairMeshExcludedRowStatus_Object = MibTableColumn
belairMeshExcludedRowStatus = _BelairMeshExcludedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 3, 1, 3),
    _BelairMeshExcludedRowStatus_Type()
)
belairMeshExcludedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairMeshExcludedRowStatus.setStatus("current")
_BelairMeshSurveyTable_Object = MibTable
belairMeshSurveyTable = _BelairMeshSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4)
)
if mibBuilder.loadTexts:
    belairMeshSurveyTable.setStatus("current")
_BelairMeshSurveyEntry_Object = MibTableRow
belairMeshSurveyEntry = _BelairMeshSurveyEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1)
)
belairMeshSurveyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-MESH", "belairMeshSurveyMacAddress"),
)
if mibBuilder.loadTexts:
    belairMeshSurveyEntry.setStatus("current")
_BelairMeshSurveyMacAddress_Type = MacAddress
_BelairMeshSurveyMacAddress_Object = MibTableColumn
belairMeshSurveyMacAddress = _BelairMeshSurveyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 1),
    _BelairMeshSurveyMacAddress_Type()
)
belairMeshSurveyMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairMeshSurveyMacAddress.setStatus("current")


class _BelairMeshSurveyLinkId_Type(OctetString):
    """Custom type belairMeshSurveyLinkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BelairMeshSurveyLinkId_Type.__name__ = "OctetString"
_BelairMeshSurveyLinkId_Object = MibTableColumn
belairMeshSurveyLinkId = _BelairMeshSurveyLinkId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 2),
    _BelairMeshSurveyLinkId_Type()
)
belairMeshSurveyLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyLinkId.setStatus("current")
_BelairMeshSurveyChannel_Type = Integer32
_BelairMeshSurveyChannel_Object = MibTableColumn
belairMeshSurveyChannel = _BelairMeshSurveyChannel_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 3),
    _BelairMeshSurveyChannel_Type()
)
belairMeshSurveyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyChannel.setStatus("current")
_BelairMeshSurveyPrivacy_Type = BelAirEncryptionType
_BelairMeshSurveyPrivacy_Object = MibTableColumn
belairMeshSurveyPrivacy = _BelairMeshSurveyPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 4),
    _BelairMeshSurveyPrivacy_Type()
)
belairMeshSurveyPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyPrivacy.setStatus("current")
_BelairMeshSurveyMpTopology_Type = BelAirMeshPointTopology
_BelairMeshSurveyMpTopology_Object = MibTableColumn
belairMeshSurveyMpTopology = _BelairMeshSurveyMpTopology_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 5),
    _BelairMeshSurveyMpTopology_Type()
)
belairMeshSurveyMpTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyMpTopology.setStatus("current")
_BelairMeshSurveyMpType_Type = BelAirMeshPointType
_BelairMeshSurveyMpType_Object = MibTableColumn
belairMeshSurveyMpType = _BelairMeshSurveyMpType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 6),
    _BelairMeshSurveyMpType_Type()
)
belairMeshSurveyMpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyMpType.setStatus("current")
_BelairMeshSurveyLinkMap_Type = Integer32
_BelairMeshSurveyLinkMap_Object = MibTableColumn
belairMeshSurveyLinkMap = _BelairMeshSurveyLinkMap_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 7),
    _BelairMeshSurveyLinkMap_Type()
)
belairMeshSurveyLinkMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyLinkMap.setStatus("current")
_BelairMeshSurveyRssi_Type = Integer32
_BelairMeshSurveyRssi_Object = MibTableColumn
belairMeshSurveyRssi = _BelairMeshSurveyRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 8),
    _BelairMeshSurveyRssi_Type()
)
belairMeshSurveyRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyRssi.setStatus("current")
_BelairMeshSurveySecsSinceLastSeen_Type = Integer32
_BelairMeshSurveySecsSinceLastSeen_Object = MibTableColumn
belairMeshSurveySecsSinceLastSeen = _BelairMeshSurveySecsSinceLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 9),
    _BelairMeshSurveySecsSinceLastSeen_Type()
)
belairMeshSurveySecsSinceLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveySecsSinceLastSeen.setStatus("current")
if mibBuilder.loadTexts:
    belairMeshSurveySecsSinceLastSeen.setUnits("Seconds")


class _BelairMeshSurveyActivityState_Type(Integer32):
    """Custom type belairMeshSurveyActivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("active", 1),
          ("aged", 2),
          ("stale", 3))
    )


_BelairMeshSurveyActivityState_Type.__name__ = "Integer32"
_BelairMeshSurveyActivityState_Object = MibTableColumn
belairMeshSurveyActivityState = _BelairMeshSurveyActivityState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 10),
    _BelairMeshSurveyActivityState_Type()
)
belairMeshSurveyActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyActivityState.setStatus("current")
_BelairMeshSurveyMobileAdmin_Type = BelAirAdminState
_BelairMeshSurveyMobileAdmin_Object = MibTableColumn
belairMeshSurveyMobileAdmin = _BelairMeshSurveyMobileAdmin_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 11),
    _BelairMeshSurveyMobileAdmin_Type()
)
belairMeshSurveyMobileAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyMobileAdmin.setStatus("current")
_BelairMeshSurveyMobileRole_Type = BelAirMeshPointType
_BelairMeshSurveyMobileRole_Object = MibTableColumn
belairMeshSurveyMobileRole = _BelairMeshSurveyMobileRole_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 12),
    _BelairMeshSurveyMobileRole_Type()
)
belairMeshSurveyMobileRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyMobileRole.setStatus("current")
_BelairMeshSurveyMobileType_Type = BelAirMeshPointTopology
_BelairMeshSurveyMobileType_Object = MibTableColumn
belairMeshSurveyMobileType = _BelairMeshSurveyMobileType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 13),
    _BelairMeshSurveyMobileType_Type()
)
belairMeshSurveyMobileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyMobileType.setStatus("current")


class _BelairMeshSurveyMobileId_Type(OctetString):
    """Custom type belairMeshSurveyMobileId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BelairMeshSurveyMobileId_Type.__name__ = "OctetString"
_BelairMeshSurveyMobileId_Object = MibTableColumn
belairMeshSurveyMobileId = _BelairMeshSurveyMobileId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 1, 4, 1, 14),
    _BelairMeshSurveyMobileId_Type()
)
belairMeshSurveyMobileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairMeshSurveyMobileId.setStatus("current")
_BelairMeshTraps_ObjectIdentity = ObjectIdentity
belairMeshTraps = _BelairMeshTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 2)
)
if mibBuilder.loadTexts:
    belairMeshTraps.setStatus("current")
_BelairMeshMibConformance_ObjectIdentity = ObjectIdentity
belairMeshMibConformance = _BelairMeshMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 3)
)
if mibBuilder.loadTexts:
    belairMeshMibConformance.setStatus("current")

# Managed Objects groups

belairMeshObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 3, 1)
)
belairMeshObjectsGroup.setObjects(
      *(("BELAIR-MESH", "belairMeshPointId"),
        ("BELAIR-MESH", "belairMeshPointPrivacyType"),
        ("BELAIR-MESH", "belairMeshPointEncryptionKey"),
        ("BELAIR-MESH", "belairMeshPoinConfigedPortalState"),
        ("BELAIR-MESH", "belairMeshPointActualPortalState"),
        ("BELAIR-MESH", "belairMeshPointType"),
        ("BELAIR-MESH", "belairMeshIfPeerMac"),
        ("BELAIR-MESH", "belairMeshIfRssi"),
        ("BELAIR-MESH", "belairMeshIfForwardingTraffic"),
        ("BELAIR-MESH", "belairMeshExcludedMacAddress"),
        ("BELAIR-MESH", "belairMeshPointAdminState"),
        ("BELAIR-MESH", "belairMeshIfLinkIndex"),
        ("BELAIR-MESH", "belairMeshSurveySecsSinceLastSeen"),
        ("BELAIR-MESH", "belairMeshSurveyRssi"),
        ("BELAIR-MESH", "belairMeshSurveyLinkMap"),
        ("BELAIR-MESH", "belairMeshSurveyMpType"),
        ("BELAIR-MESH", "belairMeshSurveyMpTopology"),
        ("BELAIR-MESH", "belairMeshSurveyPrivacy"),
        ("BELAIR-MESH", "belairMeshSurveyChannel"),
        ("BELAIR-MESH", "belairMeshSurveyLinkId"),
        ("BELAIR-MESH", "belairMeshPointMobileLinkRole"),
        ("BELAIR-MESH", "belairMeshPointMobileLinkType"),
        ("BELAIR-MESH", "belairMeshPointMobileAdminState"),
        ("BELAIR-MESH", "belairMeshPointMobileId"),
        ("BELAIR-MESH", "belairMeshPointMinRssi"),
        ("BELAIR-MESH", "belairMeshIfPeerFwdState"),
        ("BELAIR-MESH", "belairMeshIfLinkType"),
        ("BELAIR-MESH", "belairMeshIfPeerNodeIp"),
        ("BELAIR-MESH", "belairMeshIfPeerSysName"),
        ("BELAIR-MESH", "belairMeshIfAge"),
        ("BELAIR-MESH", "belairMeshIfPeerRssi"),
        ("BELAIR-MESH", "belairMeshSurveyMobileId"),
        ("BELAIR-MESH", "belairMeshSurveyMobileType"),
        ("BELAIR-MESH", "belairMeshSurveyMobileRole"),
        ("BELAIR-MESH", "belairMeshSurveyMobileAdmin"),
        ("BELAIR-MESH", "belairMeshSurveyActivityState"),
        ("BELAIR-MESH", "belairMeshIfTxFailedRate"),
        ("BELAIR-MESH", "belairMeshExcludedRowStatus"),
        ("BELAIR-MESH", "belairMeshPointTopology"),
        ("BELAIR-MESH", "belairMeshPointLinkMap"))
)
if mibBuilder.loadTexts:
    belairMeshObjectsGroup.setStatus("current")

belairMeshDeprecatedObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 4, 3, 2)
)
belairMeshDeprecatedObjGroup.setObjects(
    ("BELAIR-MESH", "belairMeshPointChannel")
)
if mibBuilder.loadTexts:
    belairMeshDeprecatedObjGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-MESH",
    **{"BelAirMeshPortalState": BelAirMeshPortalState,
       "BelAirMeshPointType": BelAirMeshPointType,
       "BelAirMeshPointTopology": BelAirMeshPointTopology,
       "BelAirMeshPointLinkMap": BelAirMeshPointLinkMap,
       "belairMeshMib": belairMeshMib,
       "belairMeshObjects": belairMeshObjects,
       "belairMeshPointTable": belairMeshPointTable,
       "belairMeshPointEntry": belairMeshPointEntry,
       "belairMeshPointId": belairMeshPointId,
       "belairMeshPointChannel": belairMeshPointChannel,
       "belairMeshPointPrivacyType": belairMeshPointPrivacyType,
       "belairMeshPointEncryptionKey": belairMeshPointEncryptionKey,
       "belairMeshPoinConfigedPortalState": belairMeshPoinConfigedPortalState,
       "belairMeshPointActualPortalState": belairMeshPointActualPortalState,
       "belairMeshPointType": belairMeshPointType,
       "belairMeshPointTopology": belairMeshPointTopology,
       "belairMeshPointLinkMap": belairMeshPointLinkMap,
       "belairMeshPointAdminState": belairMeshPointAdminState,
       "belairMeshPointMinRssi": belairMeshPointMinRssi,
       "belairMeshPointMobileId": belairMeshPointMobileId,
       "belairMeshPointMobileAdminState": belairMeshPointMobileAdminState,
       "belairMeshPointMobileLinkType": belairMeshPointMobileLinkType,
       "belairMeshPointMobileLinkRole": belairMeshPointMobileLinkRole,
       "belairMeshIfTable": belairMeshIfTable,
       "belairMeshIfEntry": belairMeshIfEntry,
       "belairMeshIfIndex": belairMeshIfIndex,
       "belairMeshIfPeerMac": belairMeshIfPeerMac,
       "belairMeshIfRssi": belairMeshIfRssi,
       "belairMeshIfForwardingTraffic": belairMeshIfForwardingTraffic,
       "belairMeshIfLinkIndex": belairMeshIfLinkIndex,
       "belairMeshIfAge": belairMeshIfAge,
       "belairMeshIfPeerSysName": belairMeshIfPeerSysName,
       "belairMeshIfPeerNodeIp": belairMeshIfPeerNodeIp,
       "belairMeshIfLinkType": belairMeshIfLinkType,
       "belairMeshIfPeerFwdState": belairMeshIfPeerFwdState,
       "belairMeshIfPeerRssi": belairMeshIfPeerRssi,
       "belairMeshIfTxFailedRate": belairMeshIfTxFailedRate,
       "belairMeshExcludedMacTable": belairMeshExcludedMacTable,
       "belairMeshExcludedMacEntry": belairMeshExcludedMacEntry,
       "belairMeshExcludedMacIndex": belairMeshExcludedMacIndex,
       "belairMeshExcludedMacAddress": belairMeshExcludedMacAddress,
       "belairMeshExcludedRowStatus": belairMeshExcludedRowStatus,
       "belairMeshSurveyTable": belairMeshSurveyTable,
       "belairMeshSurveyEntry": belairMeshSurveyEntry,
       "belairMeshSurveyMacAddress": belairMeshSurveyMacAddress,
       "belairMeshSurveyLinkId": belairMeshSurveyLinkId,
       "belairMeshSurveyChannel": belairMeshSurveyChannel,
       "belairMeshSurveyPrivacy": belairMeshSurveyPrivacy,
       "belairMeshSurveyMpTopology": belairMeshSurveyMpTopology,
       "belairMeshSurveyMpType": belairMeshSurveyMpType,
       "belairMeshSurveyLinkMap": belairMeshSurveyLinkMap,
       "belairMeshSurveyRssi": belairMeshSurveyRssi,
       "belairMeshSurveySecsSinceLastSeen": belairMeshSurveySecsSinceLastSeen,
       "belairMeshSurveyActivityState": belairMeshSurveyActivityState,
       "belairMeshSurveyMobileAdmin": belairMeshSurveyMobileAdmin,
       "belairMeshSurveyMobileRole": belairMeshSurveyMobileRole,
       "belairMeshSurveyMobileType": belairMeshSurveyMobileType,
       "belairMeshSurveyMobileId": belairMeshSurveyMobileId,
       "belairMeshTraps": belairMeshTraps,
       "belairMeshMibConformance": belairMeshMibConformance,
       "belairMeshObjectsGroup": belairMeshObjectsGroup,
       "belairMeshDeprecatedObjGroup": belairMeshDeprecatedObjGroup}
)
