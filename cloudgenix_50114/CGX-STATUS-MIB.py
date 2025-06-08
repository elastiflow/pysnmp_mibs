# SNMP MIB module (CGX-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cloudgenix_50114/CGX-STATUS-MIB.mib
# Produced by pysmi-1.6.1 at Wed Jun  4 13:56:22 2025
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

(CgxDegreesC,
 CgxVolts,
 cgxMgmt) = mibBuilder.importSymbols(
    "CLOUDGENIX-SMI",
    "CgxDegreesC",
    "CgxVolts",
    "cgxMgmt")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cgxStatusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2)
)
if mibBuilder.loadTexts:
    cgxStatusMIB.setRevisions(
        ("2022-02-24 19:35",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CgxStatusNotifications_ObjectIdentity = ObjectIdentity
cgxStatusNotifications = _CgxStatusNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 0)
)
_CgxStatusObjects_ObjectIdentity = ObjectIdentity
cgxStatusObjects = _CgxStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 1)
)
_CgxStatusStats_ObjectIdentity = ObjectIdentity
cgxStatusStats = _CgxStatusStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 1, 1)
)
_CgxStatusConfig_ObjectIdentity = ObjectIdentity
cgxStatusConfig = _CgxStatusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 1, 2)
)
_CgxTunnelObjects_ObjectIdentity = ObjectIdentity
cgxTunnelObjects = _CgxTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 1, 3)
)
_CgxStatusConformance_ObjectIdentity = ObjectIdentity
cgxStatusConformance = _CgxStatusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 2)
)
_CgxStatusCompliances_ObjectIdentity = ObjectIdentity
cgxStatusCompliances = _CgxStatusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 2, 1)
)
_CgxStatusGroups_ObjectIdentity = ObjectIdentity
cgxStatusGroups = _CgxStatusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 2, 2)
)
_CgxTunnelMIB_ObjectIdentity = ObjectIdentity
cgxTunnelMIB = _CgxTunnelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10)
)
_CgxTunnelTable_Object = MibTable
cgxTunnelTable = _CgxTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1)
)
if mibBuilder.loadTexts:
    cgxTunnelTable.setStatus("current")
_CgxTunnelEntry_Object = MibTableRow
cgxTunnelEntry = _CgxTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1)
)
cgxTunnelEntry.setIndexNames(
    (0, "CGX-STATUS-MIB", "cgxTunnelIndex"),
)
if mibBuilder.loadTexts:
    cgxTunnelEntry.setStatus("current")


class _CgxTunnelIndex_Type(Integer32):
    """Custom type cgxTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CgxTunnelIndex_Type.__name__ = "Integer32"
_CgxTunnelIndex_Object = MibTableColumn
cgxTunnelIndex = _CgxTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 1),
    _CgxTunnelIndex_Type()
)
cgxTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelIndex.setStatus("current")
_CgxTunnelId_Type = DisplayString
_CgxTunnelId_Object = MibTableColumn
cgxTunnelId = _CgxTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 2),
    _CgxTunnelId_Type()
)
cgxTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelId.setStatus("current")
_CgxTunnelStatus_Type = DisplayString
_CgxTunnelStatus_Object = MibTableColumn
cgxTunnelStatus = _CgxTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 3),
    _CgxTunnelStatus_Type()
)
cgxTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelStatus.setStatus("current")
_CgxTunnelType_Type = DisplayString
_CgxTunnelType_Object = MibTableColumn
cgxTunnelType = _CgxTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 4),
    _CgxTunnelType_Type()
)
cgxTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelType.setStatus("current")
_CgxTunnelEncapsulation_Type = DisplayString
_CgxTunnelEncapsulation_Object = MibTableColumn
cgxTunnelEncapsulation = _CgxTunnelEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 5),
    _CgxTunnelEncapsulation_Type()
)
cgxTunnelEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelEncapsulation.setStatus("current")
_CgxTunnelLocalCircuitName_Type = DisplayString
_CgxTunnelLocalCircuitName_Object = MibTableColumn
cgxTunnelLocalCircuitName = _CgxTunnelLocalCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 6),
    _CgxTunnelLocalCircuitName_Type()
)
cgxTunnelLocalCircuitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelLocalCircuitName.setStatus("current")
_CgxTunnelLocalCircuitType_Type = DisplayString
_CgxTunnelLocalCircuitType_Object = MibTableColumn
cgxTunnelLocalCircuitType = _CgxTunnelLocalCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 7),
    _CgxTunnelLocalCircuitType_Type()
)
cgxTunnelLocalCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelLocalCircuitType.setStatus("current")
_CgxTunnelRemoteCircuitName_Type = DisplayString
_CgxTunnelRemoteCircuitName_Object = MibTableColumn
cgxTunnelRemoteCircuitName = _CgxTunnelRemoteCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 8),
    _CgxTunnelRemoteCircuitName_Type()
)
cgxTunnelRemoteCircuitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelRemoteCircuitName.setStatus("current")
_CgxTunnelRemoteSiteName_Type = DisplayString
_CgxTunnelRemoteSiteName_Object = MibTableColumn
cgxTunnelRemoteSiteName = _CgxTunnelRemoteSiteName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 9),
    _CgxTunnelRemoteSiteName_Type()
)
cgxTunnelRemoteSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelRemoteSiteName.setStatus("current")
_CgxTunnelParentInterface_Type = DisplayString
_CgxTunnelParentInterface_Object = MibTableColumn
cgxTunnelParentInterface = _CgxTunnelParentInterface_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 10),
    _CgxTunnelParentInterface_Type()
)
cgxTunnelParentInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelParentInterface.setStatus("current")
_CgxTunnelSrcAddress_Type = IpAddress
_CgxTunnelSrcAddress_Object = MibTableColumn
cgxTunnelSrcAddress = _CgxTunnelSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 11),
    _CgxTunnelSrcAddress_Type()
)
cgxTunnelSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelSrcAddress.setStatus("current")
_CgxTunnelDstAddress_Type = IpAddress
_CgxTunnelDstAddress_Object = MibTableColumn
cgxTunnelDstAddress = _CgxTunnelDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 12),
    _CgxTunnelDstAddress_Type()
)
cgxTunnelDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelDstAddress.setStatus("current")
_CgxTunnelRemotePublicIpAndPort_Type = DisplayString
_CgxTunnelRemotePublicIpAndPort_Object = MibTableColumn
cgxTunnelRemotePublicIpAndPort = _CgxTunnelRemotePublicIpAndPort_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 13),
    _CgxTunnelRemotePublicIpAndPort_Type()
)
cgxTunnelRemotePublicIpAndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelRemotePublicIpAndPort.setStatus("current")
_CgxTunnelUsable_Type = TruthValue
_CgxTunnelUsable_Object = MibTableColumn
cgxTunnelUsable = _CgxTunnelUsable_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 14),
    _CgxTunnelUsable_Type()
)
cgxTunnelUsable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelUsable.setStatus("current")
_CgxTunnelActive_Type = TruthValue
_CgxTunnelActive_Object = MibTableColumn
cgxTunnelActive = _CgxTunnelActive_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 15),
    _CgxTunnelActive_Type()
)
cgxTunnelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelActive.setStatus("current")
_CgxTunnelCiphersuite_Type = DisplayString
_CgxTunnelCiphersuite_Object = MibTableColumn
cgxTunnelCiphersuite = _CgxTunnelCiphersuite_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 16),
    _CgxTunnelCiphersuite_Type()
)
cgxTunnelCiphersuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelCiphersuite.setStatus("current")
_CgxTunnelPeerVepId_Type = DisplayString
_CgxTunnelPeerVepId_Object = MibTableColumn
cgxTunnelPeerVepId = _CgxTunnelPeerVepId_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 17),
    _CgxTunnelPeerVepId_Type()
)
cgxTunnelPeerVepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelPeerVepId.setStatus("current")
_CgxTunnelInByteCounts_Type = Counter64
_CgxTunnelInByteCounts_Object = MibTableColumn
cgxTunnelInByteCounts = _CgxTunnelInByteCounts_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 18),
    _CgxTunnelInByteCounts_Type()
)
cgxTunnelInByteCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelInByteCounts.setStatus("current")
_CgxTunnelInPacketCounts_Type = Counter64
_CgxTunnelInPacketCounts_Object = MibTableColumn
cgxTunnelInPacketCounts = _CgxTunnelInPacketCounts_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 19),
    _CgxTunnelInPacketCounts_Type()
)
cgxTunnelInPacketCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelInPacketCounts.setStatus("current")
_CgxTunnelOutByteCounts_Type = Counter64
_CgxTunnelOutByteCounts_Object = MibTableColumn
cgxTunnelOutByteCounts = _CgxTunnelOutByteCounts_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 20),
    _CgxTunnelOutByteCounts_Type()
)
cgxTunnelOutByteCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelOutByteCounts.setStatus("current")
_CgxTunnelOutPacketCounts_Type = Counter64
_CgxTunnelOutPacketCounts_Object = MibTableColumn
cgxTunnelOutPacketCounts = _CgxTunnelOutPacketCounts_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 10, 1, 1, 21),
    _CgxTunnelOutPacketCounts_Type()
)
cgxTunnelOutPacketCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxTunnelOutPacketCounts.setStatus("current")
_CgxIfExtensionMIB_ObjectIdentity = ObjectIdentity
cgxIfExtensionMIB = _CgxIfExtensionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11)
)
if mibBuilder.loadTexts:
    cgxIfExtensionMIB.setStatus("current")
_CgxIfSfpNumber_Type = Unsigned32
_CgxIfSfpNumber_Object = MibScalar
cgxIfSfpNumber = _CgxIfSfpNumber_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 10),
    _CgxIfSfpNumber_Type()
)
cgxIfSfpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpNumber.setStatus("current")
_CgxIfSfpTable_Object = MibTable
cgxIfSfpTable = _CgxIfSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11)
)
if mibBuilder.loadTexts:
    cgxIfSfpTable.setStatus("current")
_CgxIfSfpEntry_Object = MibTableRow
cgxIfSfpEntry = _CgxIfSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1)
)
cgxIfSfpEntry.setIndexNames(
    (0, "CGX-STATUS-MIB", "cgxIfSfpTableIfIndex"),
)
if mibBuilder.loadTexts:
    cgxIfSfpEntry.setStatus("current")
_CgxIfSfpTableIfIndex_Type = InterfaceIndex
_CgxIfSfpTableIfIndex_Object = MibTableColumn
cgxIfSfpTableIfIndex = _CgxIfSfpTableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 1),
    _CgxIfSfpTableIfIndex_Type()
)
cgxIfSfpTableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableIfIndex.setStatus("current")
_CgxIfSfpTableIfDescr_Type = DisplayString
_CgxIfSfpTableIfDescr_Object = MibTableColumn
cgxIfSfpTableIfDescr = _CgxIfSfpTableIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 2),
    _CgxIfSfpTableIfDescr_Type()
)
cgxIfSfpTableIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableIfDescr.setStatus("current")
_CgxIfSfpTableifType_Type = IANAifType
_CgxIfSfpTableifType_Object = MibTableColumn
cgxIfSfpTableifType = _CgxIfSfpTableifType_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 3),
    _CgxIfSfpTableifType_Type()
)
cgxIfSfpTableifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableifType.setStatus("current")
_CgxIfSfpTableSfpIdentifier_Type = DisplayString
_CgxIfSfpTableSfpIdentifier_Object = MibTableColumn
cgxIfSfpTableSfpIdentifier = _CgxIfSfpTableSfpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 4),
    _CgxIfSfpTableSfpIdentifier_Type()
)
cgxIfSfpTableSfpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableSfpIdentifier.setStatus("current")


class _CgxIfSfpTableExtendedIdentifier_Type(DisplayString):
    """Custom type cgxIfSfpTableExtendedIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_CgxIfSfpTableExtendedIdentifier_Type.__name__ = "DisplayString"
_CgxIfSfpTableExtendedIdentifier_Object = MibTableColumn
cgxIfSfpTableExtendedIdentifier = _CgxIfSfpTableExtendedIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 5),
    _CgxIfSfpTableExtendedIdentifier_Type()
)
cgxIfSfpTableExtendedIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableExtendedIdentifier.setStatus("current")
_CgxIfSfpTableConnector_Type = DisplayString
_CgxIfSfpTableConnector_Object = MibTableColumn
cgxIfSfpTableConnector = _CgxIfSfpTableConnector_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 6),
    _CgxIfSfpTableConnector_Type()
)
cgxIfSfpTableConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableConnector.setStatus("current")
_CgxIfSfpTableTransceiver_Type = DisplayString
_CgxIfSfpTableTransceiver_Object = MibTableColumn
cgxIfSfpTableTransceiver = _CgxIfSfpTableTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 7),
    _CgxIfSfpTableTransceiver_Type()
)
cgxIfSfpTableTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableTransceiver.setStatus("current")


class _CgxIfSfpTableTransceiverData_Type(OctetString):
    """Custom type cgxIfSfpTableTransceiverData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_CgxIfSfpTableTransceiverData_Type.__name__ = "OctetString"
_CgxIfSfpTableTransceiverData_Object = MibTableColumn
cgxIfSfpTableTransceiverData = _CgxIfSfpTableTransceiverData_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 8),
    _CgxIfSfpTableTransceiverData_Type()
)
cgxIfSfpTableTransceiverData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableTransceiverData.setStatus("current")
_CgxIfSfpTableEncoding_Type = DisplayString
_CgxIfSfpTableEncoding_Object = MibTableColumn
cgxIfSfpTableEncoding = _CgxIfSfpTableEncoding_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 9),
    _CgxIfSfpTableEncoding_Type()
)
cgxIfSfpTableEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableEncoding.setStatus("current")
_CgxIfSfpTableBitrateNominal_Type = Unsigned32
_CgxIfSfpTableBitrateNominal_Object = MibTableColumn
cgxIfSfpTableBitrateNominal = _CgxIfSfpTableBitrateNominal_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 10),
    _CgxIfSfpTableBitrateNominal_Type()
)
cgxIfSfpTableBitrateNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableBitrateNominal.setStatus("current")
_CgxIfSfpTableRateIdentifier_Type = DisplayString
_CgxIfSfpTableRateIdentifier_Object = MibTableColumn
cgxIfSfpTableRateIdentifier = _CgxIfSfpTableRateIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 11),
    _CgxIfSfpTableRateIdentifier_Type()
)
cgxIfSfpTableRateIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableRateIdentifier.setStatus("current")
_CgxIfSfpTableLengthSmfKm_Type = Unsigned32
_CgxIfSfpTableLengthSmfKm_Object = MibTableColumn
cgxIfSfpTableLengthSmfKm = _CgxIfSfpTableLengthSmfKm_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 12),
    _CgxIfSfpTableLengthSmfKm_Type()
)
cgxIfSfpTableLengthSmfKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableLengthSmfKm.setStatus("current")
_CgxIfSfpTableLengthSmf_Type = Unsigned32
_CgxIfSfpTableLengthSmf_Object = MibTableColumn
cgxIfSfpTableLengthSmf = _CgxIfSfpTableLengthSmf_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 13),
    _CgxIfSfpTableLengthSmf_Type()
)
cgxIfSfpTableLengthSmf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableLengthSmf.setStatus("current")
_CgxIfSfpTableLengthOM2_Type = Unsigned32
_CgxIfSfpTableLengthOM2_Object = MibTableColumn
cgxIfSfpTableLengthOM2 = _CgxIfSfpTableLengthOM2_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 14),
    _CgxIfSfpTableLengthOM2_Type()
)
cgxIfSfpTableLengthOM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableLengthOM2.setStatus("current")
_CgxIfSfpTableLengthOM1_Type = Unsigned32
_CgxIfSfpTableLengthOM1_Object = MibTableColumn
cgxIfSfpTableLengthOM1 = _CgxIfSfpTableLengthOM1_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 15),
    _CgxIfSfpTableLengthOM1_Type()
)
cgxIfSfpTableLengthOM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableLengthOM1.setStatus("current")
_CgxIfSfpTableLengthCopper_Type = Unsigned32
_CgxIfSfpTableLengthCopper_Object = MibTableColumn
cgxIfSfpTableLengthCopper = _CgxIfSfpTableLengthCopper_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 16),
    _CgxIfSfpTableLengthCopper_Type()
)
cgxIfSfpTableLengthCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableLengthCopper.setStatus("current")
_CgxIfSfpTableLengthOM3_Type = Unsigned32
_CgxIfSfpTableLengthOM3_Object = MibTableColumn
cgxIfSfpTableLengthOM3 = _CgxIfSfpTableLengthOM3_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 17),
    _CgxIfSfpTableLengthOM3_Type()
)
cgxIfSfpTableLengthOM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableLengthOM3.setStatus("current")
_CgxIfSfpTableVendorName_Type = DisplayString
_CgxIfSfpTableVendorName_Object = MibTableColumn
cgxIfSfpTableVendorName = _CgxIfSfpTableVendorName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 18),
    _CgxIfSfpTableVendorName_Type()
)
cgxIfSfpTableVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableVendorName.setStatus("current")
_CgxIfSfpTableVendorOUI_Type = DisplayString
_CgxIfSfpTableVendorOUI_Object = MibTableColumn
cgxIfSfpTableVendorOUI = _CgxIfSfpTableVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 19),
    _CgxIfSfpTableVendorOUI_Type()
)
cgxIfSfpTableVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableVendorOUI.setStatus("current")
_CgxIfSfpTableVendorPartNumber_Type = DisplayString
_CgxIfSfpTableVendorPartNumber_Object = MibTableColumn
cgxIfSfpTableVendorPartNumber = _CgxIfSfpTableVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 20),
    _CgxIfSfpTableVendorPartNumber_Type()
)
cgxIfSfpTableVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableVendorPartNumber.setStatus("current")
_CgxIfSfpTableVendorRevision_Type = DisplayString
_CgxIfSfpTableVendorRevision_Object = MibTableColumn
cgxIfSfpTableVendorRevision = _CgxIfSfpTableVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 21),
    _CgxIfSfpTableVendorRevision_Type()
)
cgxIfSfpTableVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableVendorRevision.setStatus("current")
_CgxIfSfpTableUpperBitrateMargin_Type = Unsigned32
_CgxIfSfpTableUpperBitrateMargin_Object = MibTableColumn
cgxIfSfpTableUpperBitrateMargin = _CgxIfSfpTableUpperBitrateMargin_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 22),
    _CgxIfSfpTableUpperBitrateMargin_Type()
)
cgxIfSfpTableUpperBitrateMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableUpperBitrateMargin.setStatus("current")
_CgxIfSfpTableLowerBitrateMargin_Type = Unsigned32
_CgxIfSfpTableLowerBitrateMargin_Object = MibTableColumn
cgxIfSfpTableLowerBitrateMargin = _CgxIfSfpTableLowerBitrateMargin_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 23),
    _CgxIfSfpTableLowerBitrateMargin_Type()
)
cgxIfSfpTableLowerBitrateMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableLowerBitrateMargin.setStatus("current")
_CgxIfSfpTableVendorSerialNumber_Type = DisplayString
_CgxIfSfpTableVendorSerialNumber_Object = MibTableColumn
cgxIfSfpTableVendorSerialNumber = _CgxIfSfpTableVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 24),
    _CgxIfSfpTableVendorSerialNumber_Type()
)
cgxIfSfpTableVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableVendorSerialNumber.setStatus("current")
_CgxIfSfpTableVendorDateCode_Type = DisplayString
_CgxIfSfpTableVendorDateCode_Object = MibTableColumn
cgxIfSfpTableVendorDateCode = _CgxIfSfpTableVendorDateCode_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 25),
    _CgxIfSfpTableVendorDateCode_Type()
)
cgxIfSfpTableVendorDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableVendorDateCode.setStatus("current")
_CgxIfSfpTableModuleTemperature_Type = CgxDegreesC
_CgxIfSfpTableModuleTemperature_Object = MibTableColumn
cgxIfSfpTableModuleTemperature = _CgxIfSfpTableModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 26),
    _CgxIfSfpTableModuleTemperature_Type()
)
cgxIfSfpTableModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableModuleTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cgxIfSfpTableModuleTemperature.setUnits("C")
_CgxIfSfpTableModuleVoltage_Type = CgxVolts
_CgxIfSfpTableModuleVoltage_Object = MibTableColumn
cgxIfSfpTableModuleVoltage = _CgxIfSfpTableModuleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 11, 11, 1, 27),
    _CgxIfSfpTableModuleVoltage_Type()
)
cgxIfSfpTableModuleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxIfSfpTableModuleVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cgxIfSfpTableModuleVoltage.setUnits("V")

# Managed Objects groups

cgxTunnelTableEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 2, 2, 1)
)
cgxTunnelTableEntryGroup.setObjects(
      *(("CGX-STATUS-MIB", "cgxTunnelId"),
        ("CGX-STATUS-MIB", "cgxTunnelType"),
        ("CGX-STATUS-MIB", "cgxTunnelEncapsulation"),
        ("CGX-STATUS-MIB", "cgxTunnelLocalCircuitName"),
        ("CGX-STATUS-MIB", "cgxTunnelLocalCircuitType"),
        ("CGX-STATUS-MIB", "cgxTunnelRemoteCircuitName"),
        ("CGX-STATUS-MIB", "cgxTunnelRemoteSiteName"),
        ("CGX-STATUS-MIB", "cgxTunnelParentInterface"),
        ("CGX-STATUS-MIB", "cgxTunnelSrcAddress"),
        ("CGX-STATUS-MIB", "cgxTunnelDstAddress"),
        ("CGX-STATUS-MIB", "cgxTunnelRemotePublicIpAndPort"),
        ("CGX-STATUS-MIB", "cgxTunnelUsable"),
        ("CGX-STATUS-MIB", "cgxTunnelActive"),
        ("CGX-STATUS-MIB", "cgxTunnelCiphersuite"),
        ("CGX-STATUS-MIB", "cgxTunnelPeerVepId"),
        ("CGX-STATUS-MIB", "cgxTunnelInByteCounts"),
        ("CGX-STATUS-MIB", "cgxTunnelInPacketCounts"),
        ("CGX-STATUS-MIB", "cgxTunnelOutByteCounts"),
        ("CGX-STATUS-MIB", "cgxTunnelOutPacketCounts"),
        ("CGX-STATUS-MIB", "cgxTunnelIndex"),
        ("CGX-STATUS-MIB", "cgxTunnelStatus"))
)
if mibBuilder.loadTexts:
    cgxTunnelTableEntryGroup.setStatus("current")

cgxIfSfpTableEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 2, 2, 2)
)
cgxIfSfpTableEntryGroup.setObjects(
      *(("CGX-STATUS-MIB", "cgxIfSfpTableBitrateNominal"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableConnector"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableEncoding"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableExtendedIdentifier"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableIfDescr"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableIfIndex"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableifType"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableLengthCopper"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableLengthOM1"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableLengthOM2"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableLengthOM3"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableLengthSmf"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableLengthSmfKm"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableLowerBitrateMargin"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableModuleTemperature"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableModuleVoltage"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableRateIdentifier"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableSfpIdentifier"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableTransceiver"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableTransceiverData"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableUpperBitrateMargin"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableVendorDateCode"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableVendorName"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableVendorOUI"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableVendorPartNumber"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableVendorRevision"),
        ("CGX-STATUS-MIB", "cgxIfSfpTableVendorSerialNumber"))
)
if mibBuilder.loadTexts:
    cgxIfSfpTableEntryGroup.setStatus("current")

cgxIfExtensionNumberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 2, 2, 3)
)
cgxIfExtensionNumberGroup.setObjects(
    ("CGX-STATUS-MIB", "cgxIfSfpNumber")
)
if mibBuilder.loadTexts:
    cgxIfExtensionNumberGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cgxStatusMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 50114, 10, 2, 2, 1, 1)
)
cgxStatusMIBCompliance.setObjects(
      *(("CGX-STATUS-MIB", "cgxIfSfpTableEntryGroup"),
        ("CGX-STATUS-MIB", "cgxTunnelTableEntryGroup"))
)
if mibBuilder.loadTexts:
    cgxStatusMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CGX-STATUS-MIB",
    **{"cgxStatusMIB": cgxStatusMIB,
       "cgxStatusNotifications": cgxStatusNotifications,
       "cgxStatusObjects": cgxStatusObjects,
       "cgxStatusStats": cgxStatusStats,
       "cgxStatusConfig": cgxStatusConfig,
       "cgxTunnelObjects": cgxTunnelObjects,
       "cgxStatusConformance": cgxStatusConformance,
       "cgxStatusCompliances": cgxStatusCompliances,
       "cgxStatusMIBCompliance": cgxStatusMIBCompliance,
       "cgxStatusGroups": cgxStatusGroups,
       "cgxTunnelTableEntryGroup": cgxTunnelTableEntryGroup,
       "cgxIfSfpTableEntryGroup": cgxIfSfpTableEntryGroup,
       "cgxIfExtensionNumberGroup": cgxIfExtensionNumberGroup,
       "cgxTunnelMIB": cgxTunnelMIB,
       "cgxTunnelTable": cgxTunnelTable,
       "cgxTunnelEntry": cgxTunnelEntry,
       "cgxTunnelIndex": cgxTunnelIndex,
       "cgxTunnelId": cgxTunnelId,
       "cgxTunnelStatus": cgxTunnelStatus,
       "cgxTunnelType": cgxTunnelType,
       "cgxTunnelEncapsulation": cgxTunnelEncapsulation,
       "cgxTunnelLocalCircuitName": cgxTunnelLocalCircuitName,
       "cgxTunnelLocalCircuitType": cgxTunnelLocalCircuitType,
       "cgxTunnelRemoteCircuitName": cgxTunnelRemoteCircuitName,
       "cgxTunnelRemoteSiteName": cgxTunnelRemoteSiteName,
       "cgxTunnelParentInterface": cgxTunnelParentInterface,
       "cgxTunnelSrcAddress": cgxTunnelSrcAddress,
       "cgxTunnelDstAddress": cgxTunnelDstAddress,
       "cgxTunnelRemotePublicIpAndPort": cgxTunnelRemotePublicIpAndPort,
       "cgxTunnelUsable": cgxTunnelUsable,
       "cgxTunnelActive": cgxTunnelActive,
       "cgxTunnelCiphersuite": cgxTunnelCiphersuite,
       "cgxTunnelPeerVepId": cgxTunnelPeerVepId,
       "cgxTunnelInByteCounts": cgxTunnelInByteCounts,
       "cgxTunnelInPacketCounts": cgxTunnelInPacketCounts,
       "cgxTunnelOutByteCounts": cgxTunnelOutByteCounts,
       "cgxTunnelOutPacketCounts": cgxTunnelOutPacketCounts,
       "cgxIfExtensionMIB": cgxIfExtensionMIB,
       "cgxIfSfpNumber": cgxIfSfpNumber,
       "cgxIfSfpTable": cgxIfSfpTable,
       "cgxIfSfpEntry": cgxIfSfpEntry,
       "cgxIfSfpTableIfIndex": cgxIfSfpTableIfIndex,
       "cgxIfSfpTableIfDescr": cgxIfSfpTableIfDescr,
       "cgxIfSfpTableifType": cgxIfSfpTableifType,
       "cgxIfSfpTableSfpIdentifier": cgxIfSfpTableSfpIdentifier,
       "cgxIfSfpTableExtendedIdentifier": cgxIfSfpTableExtendedIdentifier,
       "cgxIfSfpTableConnector": cgxIfSfpTableConnector,
       "cgxIfSfpTableTransceiver": cgxIfSfpTableTransceiver,
       "cgxIfSfpTableTransceiverData": cgxIfSfpTableTransceiverData,
       "cgxIfSfpTableEncoding": cgxIfSfpTableEncoding,
       "cgxIfSfpTableBitrateNominal": cgxIfSfpTableBitrateNominal,
       "cgxIfSfpTableRateIdentifier": cgxIfSfpTableRateIdentifier,
       "cgxIfSfpTableLengthSmfKm": cgxIfSfpTableLengthSmfKm,
       "cgxIfSfpTableLengthSmf": cgxIfSfpTableLengthSmf,
       "cgxIfSfpTableLengthOM2": cgxIfSfpTableLengthOM2,
       "cgxIfSfpTableLengthOM1": cgxIfSfpTableLengthOM1,
       "cgxIfSfpTableLengthCopper": cgxIfSfpTableLengthCopper,
       "cgxIfSfpTableLengthOM3": cgxIfSfpTableLengthOM3,
       "cgxIfSfpTableVendorName": cgxIfSfpTableVendorName,
       "cgxIfSfpTableVendorOUI": cgxIfSfpTableVendorOUI,
       "cgxIfSfpTableVendorPartNumber": cgxIfSfpTableVendorPartNumber,
       "cgxIfSfpTableVendorRevision": cgxIfSfpTableVendorRevision,
       "cgxIfSfpTableUpperBitrateMargin": cgxIfSfpTableUpperBitrateMargin,
       "cgxIfSfpTableLowerBitrateMargin": cgxIfSfpTableLowerBitrateMargin,
       "cgxIfSfpTableVendorSerialNumber": cgxIfSfpTableVendorSerialNumber,
       "cgxIfSfpTableVendorDateCode": cgxIfSfpTableVendorDateCode,
       "cgxIfSfpTableModuleTemperature": cgxIfSfpTableModuleTemperature,
       "cgxIfSfpTableModuleVoltage": cgxIfSfpTableModuleVoltage}
)
