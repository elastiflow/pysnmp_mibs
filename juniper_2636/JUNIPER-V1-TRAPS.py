# SNMP MIB module (JUNIPER-V1-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-V1-TRAPS.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:31:34 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ospf_ObjectIdentity = ObjectIdentity
ospf = _Ospf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14)
)
_OspfGeneralGroup_ObjectIdentity = ObjectIdentity
ospfGeneralGroup = _OspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 1)
)
_OspfRouterId_ObjectIdentity = ObjectIdentity
ospfRouterId = _OspfRouterId_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 1, 1)
)
_OspfExtLsdbLimit_ObjectIdentity = ObjectIdentity
ospfExtLsdbLimit = _OspfExtLsdbLimit_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 1, 11)
)
_OspfLsdbTable_ObjectIdentity = ObjectIdentity
ospfLsdbTable = _OspfLsdbTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 4)
)
_OspfLsdbEntry_ObjectIdentity = ObjectIdentity
ospfLsdbEntry = _OspfLsdbEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 4, 1)
)
_OspfLsdbAreaId_ObjectIdentity = ObjectIdentity
ospfLsdbAreaId = _OspfLsdbAreaId_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 1)
)
_OspfLsdbType_ObjectIdentity = ObjectIdentity
ospfLsdbType = _OspfLsdbType_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 2)
)
_OspfLsdbLsid_ObjectIdentity = ObjectIdentity
ospfLsdbLsid = _OspfLsdbLsid_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 3)
)
_OspfLsdbRouterId_ObjectIdentity = ObjectIdentity
ospfLsdbRouterId = _OspfLsdbRouterId_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 4)
)
_OspfIfTable_ObjectIdentity = ObjectIdentity
ospfIfTable = _OspfIfTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 7)
)
_OspfIfEntry_ObjectIdentity = ObjectIdentity
ospfIfEntry = _OspfIfEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 7, 1)
)
_OspfIfIpAddress_ObjectIdentity = ObjectIdentity
ospfIfIpAddress = _OspfIfIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 1)
)
_OspfAddressLessIf_ObjectIdentity = ObjectIdentity
ospfAddressLessIf = _OspfAddressLessIf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 2)
)
_OspfIfState_ObjectIdentity = ObjectIdentity
ospfIfState = _OspfIfState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 12)
)
_OspfVirtIfTable_ObjectIdentity = ObjectIdentity
ospfVirtIfTable = _OspfVirtIfTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 9)
)
_OspfVirtIfEntry_ObjectIdentity = ObjectIdentity
ospfVirtIfEntry = _OspfVirtIfEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 9, 1)
)
_OspfVirtIfAreaId_ObjectIdentity = ObjectIdentity
ospfVirtIfAreaId = _OspfVirtIfAreaId_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 1)
)
_OspfVirtIfNeighbor_ObjectIdentity = ObjectIdentity
ospfVirtIfNeighbor = _OspfVirtIfNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 2)
)
_OspfVirtIfState_ObjectIdentity = ObjectIdentity
ospfVirtIfState = _OspfVirtIfState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 7)
)
_OspfNbrTable_ObjectIdentity = ObjectIdentity
ospfNbrTable = _OspfNbrTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 10)
)
_OspfNbrEntry_ObjectIdentity = ObjectIdentity
ospfNbrEntry = _OspfNbrEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 10, 1)
)
_OspfNbrIpAddr_ObjectIdentity = ObjectIdentity
ospfNbrIpAddr = _OspfNbrIpAddr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 1)
)
_OspfNbrAddressLessIndex_ObjectIdentity = ObjectIdentity
ospfNbrAddressLessIndex = _OspfNbrAddressLessIndex_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 2)
)
_OspfNbrRtrId_ObjectIdentity = ObjectIdentity
ospfNbrRtrId = _OspfNbrRtrId_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 3)
)
_OspfNbrState_ObjectIdentity = ObjectIdentity
ospfNbrState = _OspfNbrState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 6)
)
_OspfVirtNbrTable_ObjectIdentity = ObjectIdentity
ospfVirtNbrTable = _OspfVirtNbrTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 11)
)
_OspfVirtNbrEntry_ObjectIdentity = ObjectIdentity
ospfVirtNbrEntry = _OspfVirtNbrEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 11, 1)
)
_OspfVirtNbrArea_ObjectIdentity = ObjectIdentity
ospfVirtNbrArea = _OspfVirtNbrArea_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 1)
)
_OspfVirtNbrRtrId_ObjectIdentity = ObjectIdentity
ospfVirtNbrRtrId = _OspfVirtNbrRtrId_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 2)
)
_OspfVirtNbrState_ObjectIdentity = ObjectIdentity
ospfVirtNbrState = _OspfVirtNbrState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 5)
)
_OspfTrap_ObjectIdentity = ObjectIdentity
ospfTrap = _OspfTrap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16)
)
_OspfTrapControl_ObjectIdentity = ObjectIdentity
ospfTrapControl = _OspfTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 1)
)
_OspfConfigErrorType_ObjectIdentity = ObjectIdentity
ospfConfigErrorType = _OspfConfigErrorType_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 1, 2)
)
_OspfPacketType_ObjectIdentity = ObjectIdentity
ospfPacketType = _OspfPacketType_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 1, 3)
)
_OspfPacketSrc_ObjectIdentity = ObjectIdentity
ospfPacketSrc = _OspfPacketSrc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 16, 1, 4)
)
_Bgp_ObjectIdentity = ObjectIdentity
bgp = _Bgp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15)
)
_BgpPeerTable_ObjectIdentity = ObjectIdentity
bgpPeerTable = _BgpPeerTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 3)
)
_BgpPeerEntry_ObjectIdentity = ObjectIdentity
bgpPeerEntry = _BgpPeerEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 3, 1)
)
_BgpPeerState_ObjectIdentity = ObjectIdentity
bgpPeerState = _BgpPeerState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 2)
)
_BgpPeerLastError_ObjectIdentity = ObjectIdentity
bgpPeerLastError = _BgpPeerLastError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 14)
)
_JuniperMIB_ObjectIdentity = ObjectIdentity
juniperMIB = _JuniperMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636)
)
_JnxMibs_ObjectIdentity = ObjectIdentity
jnxMibs = _JnxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3)
)
_JnxBoxAnatomy_ObjectIdentity = ObjectIdentity
jnxBoxAnatomy = _JnxBoxAnatomy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1)
)
_JnxContentsTable_ObjectIdentity = ObjectIdentity
jnxContentsTable = _JnxContentsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8)
)
_JnxContentsEntry_ObjectIdentity = ObjectIdentity
jnxContentsEntry = _JnxContentsEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1)
)
_JnxContentsContainerIndex_ObjectIdentity = ObjectIdentity
jnxContentsContainerIndex = _JnxContentsContainerIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 1)
)
_JnxContentsL1Index_ObjectIdentity = ObjectIdentity
jnxContentsL1Index = _JnxContentsL1Index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 2)
)
_JnxContentsL2Index_ObjectIdentity = ObjectIdentity
jnxContentsL2Index = _JnxContentsL2Index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 3)
)
_JnxContentsL3Index_ObjectIdentity = ObjectIdentity
jnxContentsL3Index = _JnxContentsL3Index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 4)
)
_JnxContentsDescr_ObjectIdentity = ObjectIdentity
jnxContentsDescr = _JnxContentsDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 6)
)
_Mpls_ObjectIdentity = ObjectIdentity
mpls = _Mpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2)
)
_MplsLspList_ObjectIdentity = ObjectIdentity
mplsLspList = _MplsLspList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3)
)
_MplsLspEntry_ObjectIdentity = ObjectIdentity
mplsLspEntry = _MplsLspEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1)
)
_MplsLspName_ObjectIdentity = ObjectIdentity
mplsLspName = _MplsLspName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 1)
)
_MplsPathName_ObjectIdentity = ObjectIdentity
mplsPathName = _MplsPathName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 17)
)

# Managed Objects groups


# Notification objects

bgpEstablishedV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 1)
)
bgpEstablishedV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "bgpPeerLastError"),
        ("JUNIPER-V1-TRAPS", "bgpPeerState"))
)
if mibBuilder.loadTexts:
    bgpEstablishedV1.setStatus(
        ""
    )

bgpBackwardTransitionV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 2)
)
bgpBackwardTransitionV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "bgpPeerLastError"),
        ("JUNIPER-V1-TRAPS", "bgpPeerState"))
)
if mibBuilder.loadTexts:
    bgpBackwardTransitionV1.setStatus(
        ""
    )

jnxPowerSupplyFailureV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 3)
)
jnxPowerSupplyFailureV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "jnxContentsContainerIndex"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL1Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL2Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL3Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsDescr"))
)
if mibBuilder.loadTexts:
    jnxPowerSupplyFailureV1.setStatus(
        ""
    )

jnxFanFailureV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 4)
)
jnxFanFailureV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "jnxContentsContainerIndex"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL1Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL2Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL3Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsDescr"))
)
if mibBuilder.loadTexts:
    jnxFanFailureV1.setStatus(
        ""
    )

jnxOverTemperatureV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 5)
)
jnxOverTemperatureV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "jnxContentsContainerIndex"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL1Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL2Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsL3Index"),
        ("JUNIPER-V1-TRAPS", "jnxContentsDescr"))
)
if mibBuilder.loadTexts:
    jnxOverTemperatureV1.setStatus(
        ""
    )

mplsLspUpV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 6)
)
mplsLspUpV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "mplsLspName"),
        ("JUNIPER-V1-TRAPS", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspUpV1.setStatus(
        ""
    )

mplsLspDownV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 7)
)
mplsLspDownV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "mplsLspName"),
        ("JUNIPER-V1-TRAPS", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspDownV1.setStatus(
        ""
    )

mplsLspChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 8)
)
mplsLspChangeV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "mplsLspName"),
        ("JUNIPER-V1-TRAPS", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspChangeV1.setStatus(
        ""
    )

ospfVirtIfStateChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 9)
)
ospfVirtIfStateChangeV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfAreaId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfNeighbor"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfState"))
)
if mibBuilder.loadTexts:
    ospfVirtIfStateChangeV1.setStatus(
        ""
    )

ospfNbrStateChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 10)
)
ospfNbrStateChangeV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfNbrIpAddr"),
        ("JUNIPER-V1-TRAPS", "ospfNbrAddressLessIndex"),
        ("JUNIPER-V1-TRAPS", "ospfNbrRtrId"),
        ("JUNIPER-V1-TRAPS", "ospfNbrState"))
)
if mibBuilder.loadTexts:
    ospfNbrStateChangeV1.setStatus(
        ""
    )

ospfVirtNbrStateChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 11)
)
ospfVirtNbrStateChangeV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtNbrArea"),
        ("JUNIPER-V1-TRAPS", "ospfVirtNbrRtrId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtNbrState"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrStateChangeV1.setStatus(
        ""
    )

ospfIfConfigErrorV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 12)
)
ospfIfConfigErrorV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfIfIpAddress"),
        ("JUNIPER-V1-TRAPS", "ospfAddressLessIf"),
        ("JUNIPER-V1-TRAPS", "ospfPacketSrc"),
        ("JUNIPER-V1-TRAPS", "ospfConfigErrorType"),
        ("JUNIPER-V1-TRAPS", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfConfigErrorV1.setStatus(
        ""
    )

ospfVirtIfConfigErrorV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 13)
)
ospfVirtIfConfigErrorV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfAreaId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfNeighbor"),
        ("JUNIPER-V1-TRAPS", "ospfConfigErrorType"),
        ("JUNIPER-V1-TRAPS", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfConfigErrorV1.setStatus(
        ""
    )

ospfIfAuthFailureV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 14)
)
ospfIfAuthFailureV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfIfIpAddress"),
        ("JUNIPER-V1-TRAPS", "ospfAddressLessIf"),
        ("JUNIPER-V1-TRAPS", "ospfPacketSrc"),
        ("JUNIPER-V1-TRAPS", "ospfConfigErrorType"),
        ("JUNIPER-V1-TRAPS", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfAuthFailureV1.setStatus(
        ""
    )

ospfVirtIfAuthFailureV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 15)
)
ospfVirtIfAuthFailureV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfAreaId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfNeighbor"),
        ("JUNIPER-V1-TRAPS", "ospfConfigErrorType"),
        ("JUNIPER-V1-TRAPS", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfAuthFailureV1.setStatus(
        ""
    )

ospfIfRxBadPacketV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 16)
)
ospfIfRxBadPacketV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfIfIpAddress"),
        ("JUNIPER-V1-TRAPS", "ospfAddressLessIf"),
        ("JUNIPER-V1-TRAPS", "ospfPacketSrc"),
        ("JUNIPER-V1-TRAPS", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfRxBadPacketV1.setStatus(
        ""
    )

ospfVirtIfRxBadPacketV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 17)
)
ospfVirtIfRxBadPacketV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfAreaId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfNeighbor"),
        ("JUNIPER-V1-TRAPS", "ospfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfRxBadPacketV1.setStatus(
        ""
    )

ospfTxRetransmitV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 18)
)
ospfTxRetransmitV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfIfIpAddress"),
        ("JUNIPER-V1-TRAPS", "ospfAddressLessIf"),
        ("JUNIPER-V1-TRAPS", "ospfNbrRtrId"),
        ("JUNIPER-V1-TRAPS", "ospfPacketType"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbType"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbLsid"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfTxRetransmitV1.setStatus(
        ""
    )

ospfVirtIfTxRetransmitV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 19)
)
ospfVirtIfTxRetransmitV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfAreaId"),
        ("JUNIPER-V1-TRAPS", "ospfVirtIfNeighbor"),
        ("JUNIPER-V1-TRAPS", "ospfPacketType"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbType"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbLsid"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfVirtIfTxRetransmitV1.setStatus(
        ""
    )

ospfOriginateLsaV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 20)
)
ospfOriginateLsaV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbAreaId"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbType"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbLsid"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfOriginateLsaV1.setStatus(
        ""
    )

ospfMaxAgeLsaV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 21)
)
ospfMaxAgeLsaV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbAreaId"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbType"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbLsid"),
        ("JUNIPER-V1-TRAPS", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfMaxAgeLsaV1.setStatus(
        ""
    )

ospfLsdbOverflowV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 22)
)
ospfLsdbOverflowV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    ospfLsdbOverflowV1.setStatus(
        ""
    )

ospfLsdbApproachingOverflowV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 23)
)
ospfLsdbApproachingOverflowV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    ospfLsdbApproachingOverflowV1.setStatus(
        ""
    )

ospfIfStateChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 24)
)
ospfIfStateChangeV1.setObjects(
      *(("JUNIPER-V1-TRAPS", "ospfRouterId"),
        ("JUNIPER-V1-TRAPS", "ospfIfIpAddress"),
        ("JUNIPER-V1-TRAPS", "ospfAddressLessIf"),
        ("JUNIPER-V1-TRAPS", "ospfIfState"))
)
if mibBuilder.loadTexts:
    ospfIfStateChangeV1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-V1-TRAPS",
    **{"ospf": ospf,
       "ospfGeneralGroup": ospfGeneralGroup,
       "ospfRouterId": ospfRouterId,
       "ospfExtLsdbLimit": ospfExtLsdbLimit,
       "ospfLsdbTable": ospfLsdbTable,
       "ospfLsdbEntry": ospfLsdbEntry,
       "ospfLsdbAreaId": ospfLsdbAreaId,
       "ospfLsdbType": ospfLsdbType,
       "ospfLsdbLsid": ospfLsdbLsid,
       "ospfLsdbRouterId": ospfLsdbRouterId,
       "ospfIfTable": ospfIfTable,
       "ospfIfEntry": ospfIfEntry,
       "ospfIfIpAddress": ospfIfIpAddress,
       "ospfAddressLessIf": ospfAddressLessIf,
       "ospfIfState": ospfIfState,
       "ospfVirtIfTable": ospfVirtIfTable,
       "ospfVirtIfEntry": ospfVirtIfEntry,
       "ospfVirtIfAreaId": ospfVirtIfAreaId,
       "ospfVirtIfNeighbor": ospfVirtIfNeighbor,
       "ospfVirtIfState": ospfVirtIfState,
       "ospfNbrTable": ospfNbrTable,
       "ospfNbrEntry": ospfNbrEntry,
       "ospfNbrIpAddr": ospfNbrIpAddr,
       "ospfNbrAddressLessIndex": ospfNbrAddressLessIndex,
       "ospfNbrRtrId": ospfNbrRtrId,
       "ospfNbrState": ospfNbrState,
       "ospfVirtNbrTable": ospfVirtNbrTable,
       "ospfVirtNbrEntry": ospfVirtNbrEntry,
       "ospfVirtNbrArea": ospfVirtNbrArea,
       "ospfVirtNbrRtrId": ospfVirtNbrRtrId,
       "ospfVirtNbrState": ospfVirtNbrState,
       "ospfTrap": ospfTrap,
       "ospfTrapControl": ospfTrapControl,
       "ospfConfigErrorType": ospfConfigErrorType,
       "ospfPacketType": ospfPacketType,
       "ospfPacketSrc": ospfPacketSrc,
       "bgp": bgp,
       "bgpPeerTable": bgpPeerTable,
       "bgpPeerEntry": bgpPeerEntry,
       "bgpPeerState": bgpPeerState,
       "bgpPeerLastError": bgpPeerLastError,
       "juniperMIB": juniperMIB,
       "bgpEstablishedV1": bgpEstablishedV1,
       "bgpBackwardTransitionV1": bgpBackwardTransitionV1,
       "jnxPowerSupplyFailureV1": jnxPowerSupplyFailureV1,
       "jnxFanFailureV1": jnxFanFailureV1,
       "jnxOverTemperatureV1": jnxOverTemperatureV1,
       "mplsLspUpV1": mplsLspUpV1,
       "mplsLspDownV1": mplsLspDownV1,
       "mplsLspChangeV1": mplsLspChangeV1,
       "ospfVirtIfStateChangeV1": ospfVirtIfStateChangeV1,
       "ospfNbrStateChangeV1": ospfNbrStateChangeV1,
       "ospfVirtNbrStateChangeV1": ospfVirtNbrStateChangeV1,
       "ospfIfConfigErrorV1": ospfIfConfigErrorV1,
       "ospfVirtIfConfigErrorV1": ospfVirtIfConfigErrorV1,
       "ospfIfAuthFailureV1": ospfIfAuthFailureV1,
       "ospfVirtIfAuthFailureV1": ospfVirtIfAuthFailureV1,
       "ospfIfRxBadPacketV1": ospfIfRxBadPacketV1,
       "ospfVirtIfRxBadPacketV1": ospfVirtIfRxBadPacketV1,
       "ospfTxRetransmitV1": ospfTxRetransmitV1,
       "ospfVirtIfTxRetransmitV1": ospfVirtIfTxRetransmitV1,
       "ospfOriginateLsaV1": ospfOriginateLsaV1,
       "ospfMaxAgeLsaV1": ospfMaxAgeLsaV1,
       "ospfLsdbOverflowV1": ospfLsdbOverflowV1,
       "ospfLsdbApproachingOverflowV1": ospfLsdbApproachingOverflowV1,
       "ospfIfStateChangeV1": ospfIfStateChangeV1,
       "jnxMibs": jnxMibs,
       "jnxBoxAnatomy": jnxBoxAnatomy,
       "jnxContentsTable": jnxContentsTable,
       "jnxContentsEntry": jnxContentsEntry,
       "jnxContentsContainerIndex": jnxContentsContainerIndex,
       "jnxContentsL1Index": jnxContentsL1Index,
       "jnxContentsL2Index": jnxContentsL2Index,
       "jnxContentsL3Index": jnxContentsL3Index,
       "jnxContentsDescr": jnxContentsDescr,
       "mpls": mpls,
       "mplsLspList": mplsLspList,
       "mplsLspEntry": mplsLspEntry,
       "mplsLspName": mplsLspName,
       "mplsPathName": mplsPathName}
)
