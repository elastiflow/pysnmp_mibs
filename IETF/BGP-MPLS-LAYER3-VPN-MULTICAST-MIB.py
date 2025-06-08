# SNMP MIB module (BGP-MPLS-LAYER3-VPN-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/BGP-MPLS-LAYER3-VPN-MULTICAST-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:24:51 2025
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

(IANAipMRouteProtocol,
 IANAipRouteProtocol) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(L2L3VpnMcastProviderTunnelType,) = mibBuilder.importSymbols(
    "L2L3-VPN-MULTICAST-TC-MIB",
    "L2L3VpnMcastProviderTunnelType")

(MplsL3VpnRouteDistinguisher,
 mplsL3VpnVrfName) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "MplsL3VpnRouteDistinguisher",
    "mplsL3VpnVrfName")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

mvpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 243)
)
if mibBuilder.loadTexts:
    mvpnMIB.setRevisions(
        ("2018-12-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MvpnNotifications_ObjectIdentity = ObjectIdentity
mvpnNotifications = _MvpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 243, 0)
)
_MvpnObjects_ObjectIdentity = ObjectIdentity
mvpnObjects = _MvpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 243, 1)
)
_MvpnScalars_ObjectIdentity = ObjectIdentity
mvpnScalars = _MvpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 243, 1, 1)
)
_MvpnMvrfs_Type = Gauge32
_MvpnMvrfs_Object = MibScalar
mvpnMvrfs = _MvpnMvrfs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 1),
    _MvpnMvrfs_Type()
)
mvpnMvrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMvrfs.setStatus("current")
_MvpnV4Mvrfs_Type = Gauge32
_MvpnV4Mvrfs_Object = MibScalar
mvpnV4Mvrfs = _MvpnV4Mvrfs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 2),
    _MvpnV4Mvrfs_Type()
)
mvpnV4Mvrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnV4Mvrfs.setStatus("current")
_MvpnV6Mvrfs_Type = Gauge32
_MvpnV6Mvrfs_Object = MibScalar
mvpnV6Mvrfs = _MvpnV6Mvrfs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 3),
    _MvpnV6Mvrfs_Type()
)
mvpnV6Mvrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnV6Mvrfs.setStatus("current")
_MvpnMldpMvrfs_Type = Gauge32
_MvpnMldpMvrfs_Object = MibScalar
mvpnMldpMvrfs = _MvpnMldpMvrfs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 4),
    _MvpnMldpMvrfs_Type()
)
mvpnMldpMvrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMldpMvrfs.setStatus("current")
_MvpnPimV4Mvrfs_Type = Gauge32
_MvpnPimV4Mvrfs_Object = MibScalar
mvpnPimV4Mvrfs = _MvpnPimV4Mvrfs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 5),
    _MvpnPimV4Mvrfs_Type()
)
mvpnPimV4Mvrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnPimV4Mvrfs.setStatus("current")
_MvpnPimV6Mvrfs_Type = Gauge32
_MvpnPimV6Mvrfs_Object = MibScalar
mvpnPimV6Mvrfs = _MvpnPimV6Mvrfs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 6),
    _MvpnPimV6Mvrfs_Type()
)
mvpnPimV6Mvrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnPimV6Mvrfs.setStatus("current")
_MvpnBgpV4Mvrfs_Type = Gauge32
_MvpnBgpV4Mvrfs_Object = MibScalar
mvpnBgpV4Mvrfs = _MvpnBgpV4Mvrfs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 7),
    _MvpnBgpV4Mvrfs_Type()
)
mvpnBgpV4Mvrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnBgpV4Mvrfs.setStatus("current")
_MvpnBgpV6Mvrfs_Type = Gauge32
_MvpnBgpV6Mvrfs_Object = MibScalar
mvpnBgpV6Mvrfs = _MvpnBgpV6Mvrfs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 8),
    _MvpnBgpV6Mvrfs_Type()
)
mvpnBgpV6Mvrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnBgpV6Mvrfs.setStatus("current")


class _MvpnSPTunnelLimit_Type(Unsigned32):
    """Custom type mvpnSPTunnelLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MvpnSPTunnelLimit_Type.__name__ = "Unsigned32"
_MvpnSPTunnelLimit_Object = MibScalar
mvpnSPTunnelLimit = _MvpnSPTunnelLimit_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 9),
    _MvpnSPTunnelLimit_Type()
)
mvpnSPTunnelLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvpnSPTunnelLimit.setStatus("current")
_MvpnBgpCmcastRouteWithdrawalTimer_Type = Unsigned32
_MvpnBgpCmcastRouteWithdrawalTimer_Object = MibScalar
mvpnBgpCmcastRouteWithdrawalTimer = _MvpnBgpCmcastRouteWithdrawalTimer_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 10),
    _MvpnBgpCmcastRouteWithdrawalTimer_Type()
)
mvpnBgpCmcastRouteWithdrawalTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvpnBgpCmcastRouteWithdrawalTimer.setStatus("current")
if mibBuilder.loadTexts:
    mvpnBgpCmcastRouteWithdrawalTimer.setUnits("milliseconds")
_MvpnBgpSrcSharedTreeJoinTimer_Type = Unsigned32
_MvpnBgpSrcSharedTreeJoinTimer_Object = MibScalar
mvpnBgpSrcSharedTreeJoinTimer = _MvpnBgpSrcSharedTreeJoinTimer_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 1, 11),
    _MvpnBgpSrcSharedTreeJoinTimer_Type()
)
mvpnBgpSrcSharedTreeJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvpnBgpSrcSharedTreeJoinTimer.setStatus("current")
if mibBuilder.loadTexts:
    mvpnBgpSrcSharedTreeJoinTimer.setUnits("milliseconds")
_MvpnGenericTable_Object = MibTable
mvpnGenericTable = _MvpnGenericTable_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2)
)
if mibBuilder.loadTexts:
    mvpnGenericTable.setStatus("current")
_MvpnGenericEntry_Object = MibTableRow
mvpnGenericEntry = _MvpnGenericEntry_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1)
)
mvpnGenericEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
)
if mibBuilder.loadTexts:
    mvpnGenericEntry.setStatus("current")


class _MvpnGenMvrfLastAction_Type(Integer32):
    """Custom type mvpnGenMvrfLastAction based on Integer32"""
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
        *(("createdMvrf", 1),
          ("deletedMvrf", 2),
          ("modifiedMvrfIpmsiConfig", 3),
          ("modifiedMvrfSpmsiConfig", 4))
    )


_MvpnGenMvrfLastAction_Type.__name__ = "Integer32"
_MvpnGenMvrfLastAction_Object = MibTableColumn
mvpnGenMvrfLastAction = _MvpnGenMvrfLastAction_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1, 2),
    _MvpnGenMvrfLastAction_Type()
)
mvpnGenMvrfLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnGenMvrfLastAction.setStatus("current")
_MvpnGenMvrfLastActionTime_Type = DateAndTime
_MvpnGenMvrfLastActionTime_Object = MibTableColumn
mvpnGenMvrfLastActionTime = _MvpnGenMvrfLastActionTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1, 3),
    _MvpnGenMvrfLastActionTime_Type()
)
mvpnGenMvrfLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnGenMvrfLastActionTime.setStatus("current")
_MvpnGenMvrfCreationTime_Type = DateAndTime
_MvpnGenMvrfCreationTime_Object = MibTableColumn
mvpnGenMvrfCreationTime = _MvpnGenMvrfCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1, 4),
    _MvpnGenMvrfCreationTime_Type()
)
mvpnGenMvrfCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnGenMvrfCreationTime.setStatus("current")


class _MvpnGenCmcastRouteProtocol_Type(Integer32):
    """Custom type mvpnGenCmcastRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pim", 1),
          ("bgp", 2))
    )


_MvpnGenCmcastRouteProtocol_Type.__name__ = "Integer32"
_MvpnGenCmcastRouteProtocol_Object = MibTableColumn
mvpnGenCmcastRouteProtocol = _MvpnGenCmcastRouteProtocol_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1, 5),
    _MvpnGenCmcastRouteProtocol_Type()
)
mvpnGenCmcastRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnGenCmcastRouteProtocol.setStatus("current")
_MvpnGenIpmsiInfo_Type = RowPointer
_MvpnGenIpmsiInfo_Object = MibTableColumn
mvpnGenIpmsiInfo = _MvpnGenIpmsiInfo_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1, 6),
    _MvpnGenIpmsiInfo_Type()
)
mvpnGenIpmsiInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnGenIpmsiInfo.setStatus("current")
_MvpnGenInterAsPmsiInfo_Type = RowPointer
_MvpnGenInterAsPmsiInfo_Object = MibTableColumn
mvpnGenInterAsPmsiInfo = _MvpnGenInterAsPmsiInfo_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1, 7),
    _MvpnGenInterAsPmsiInfo_Type()
)
mvpnGenInterAsPmsiInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnGenInterAsPmsiInfo.setStatus("current")


class _MvpnGenUmhSelection_Type(Integer32):
    """Custom type mvpnGenUmhSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highestPeAddress", 1),
          ("cRootGroupHashing", 2),
          ("ucastUmhRoute", 3))
    )


_MvpnGenUmhSelection_Type.__name__ = "Integer32"
_MvpnGenUmhSelection_Object = MibTableColumn
mvpnGenUmhSelection = _MvpnGenUmhSelection_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1, 8),
    _MvpnGenUmhSelection_Type()
)
mvpnGenUmhSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnGenUmhSelection.setStatus("current")


class _MvpnGenCustomerSiteType_Type(Integer32):
    """Custom type mvpnGenCustomerSiteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("senderReceiver", 1),
          ("receiverOnly", 2),
          ("senderOnly", 3))
    )


_MvpnGenCustomerSiteType_Type.__name__ = "Integer32"
_MvpnGenCustomerSiteType_Object = MibTableColumn
mvpnGenCustomerSiteType = _MvpnGenCustomerSiteType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 2, 1, 9),
    _MvpnGenCustomerSiteType_Type()
)
mvpnGenCustomerSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnGenCustomerSiteType.setStatus("current")
_MvpnBgpTable_Object = MibTable
mvpnBgpTable = _MvpnBgpTable_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3)
)
if mibBuilder.loadTexts:
    mvpnBgpTable.setStatus("current")
_MvpnBgpEntry_Object = MibTableRow
mvpnBgpEntry = _MvpnBgpEntry_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1)
)
mvpnBgpEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
)
if mibBuilder.loadTexts:
    mvpnBgpEntry.setStatus("current")


class _MvpnBgpMode_Type(Integer32):
    """Custom type mvpnBgpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("rptSpt", 1),
          ("sptOnly", 2))
    )


_MvpnBgpMode_Type.__name__ = "Integer32"
_MvpnBgpMode_Object = MibTableColumn
mvpnBgpMode = _MvpnBgpMode_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1, 1),
    _MvpnBgpMode_Type()
)
mvpnBgpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnBgpMode.setStatus("current")
_MvpnBgpVrfRouteImportExtendedCommunity_Type = MplsL3VpnRouteDistinguisher
_MvpnBgpVrfRouteImportExtendedCommunity_Object = MibTableColumn
mvpnBgpVrfRouteImportExtendedCommunity = _MvpnBgpVrfRouteImportExtendedCommunity_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1, 2),
    _MvpnBgpVrfRouteImportExtendedCommunity_Type()
)
mvpnBgpVrfRouteImportExtendedCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnBgpVrfRouteImportExtendedCommunity.setStatus("current")
_MvpnBgpSrcASExtendedCommunity_Type = Unsigned32
_MvpnBgpSrcASExtendedCommunity_Object = MibTableColumn
mvpnBgpSrcASExtendedCommunity = _MvpnBgpSrcASExtendedCommunity_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1, 3),
    _MvpnBgpSrcASExtendedCommunity_Type()
)
mvpnBgpSrcASExtendedCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnBgpSrcASExtendedCommunity.setStatus("current")


class _MvpnBgpMsgRateLimit_Type(Unsigned32):
    """Custom type mvpnBgpMsgRateLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MvpnBgpMsgRateLimit_Type.__name__ = "Unsigned32"
_MvpnBgpMsgRateLimit_Object = MibTableColumn
mvpnBgpMsgRateLimit = _MvpnBgpMsgRateLimit_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1, 4),
    _MvpnBgpMsgRateLimit_Type()
)
mvpnBgpMsgRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvpnBgpMsgRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    mvpnBgpMsgRateLimit.setUnits("messages per second")


class _MvpnBgpMaxSpmsiAdRoutes_Type(Unsigned32):
    """Custom type mvpnBgpMaxSpmsiAdRoutes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MvpnBgpMaxSpmsiAdRoutes_Type.__name__ = "Unsigned32"
_MvpnBgpMaxSpmsiAdRoutes_Object = MibTableColumn
mvpnBgpMaxSpmsiAdRoutes = _MvpnBgpMaxSpmsiAdRoutes_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1, 5),
    _MvpnBgpMaxSpmsiAdRoutes_Type()
)
mvpnBgpMaxSpmsiAdRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvpnBgpMaxSpmsiAdRoutes.setStatus("current")


class _MvpnBgpMaxSpmsiAdRouteFreq_Type(Unsigned32):
    """Custom type mvpnBgpMaxSpmsiAdRouteFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MvpnBgpMaxSpmsiAdRouteFreq_Type.__name__ = "Unsigned32"
_MvpnBgpMaxSpmsiAdRouteFreq_Object = MibTableColumn
mvpnBgpMaxSpmsiAdRouteFreq = _MvpnBgpMaxSpmsiAdRouteFreq_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1, 6),
    _MvpnBgpMaxSpmsiAdRouteFreq_Type()
)
mvpnBgpMaxSpmsiAdRouteFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvpnBgpMaxSpmsiAdRouteFreq.setStatus("current")
if mibBuilder.loadTexts:
    mvpnBgpMaxSpmsiAdRouteFreq.setUnits("routes per second")


class _MvpnBgpMaxSrcActiveAdRoutes_Type(Unsigned32):
    """Custom type mvpnBgpMaxSrcActiveAdRoutes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MvpnBgpMaxSrcActiveAdRoutes_Type.__name__ = "Unsigned32"
_MvpnBgpMaxSrcActiveAdRoutes_Object = MibTableColumn
mvpnBgpMaxSrcActiveAdRoutes = _MvpnBgpMaxSrcActiveAdRoutes_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1, 7),
    _MvpnBgpMaxSrcActiveAdRoutes_Type()
)
mvpnBgpMaxSrcActiveAdRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvpnBgpMaxSrcActiveAdRoutes.setStatus("current")


class _MvpnBgpMaxSrcActiveAdRouteFreq_Type(Unsigned32):
    """Custom type mvpnBgpMaxSrcActiveAdRouteFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MvpnBgpMaxSrcActiveAdRouteFreq_Type.__name__ = "Unsigned32"
_MvpnBgpMaxSrcActiveAdRouteFreq_Object = MibTableColumn
mvpnBgpMaxSrcActiveAdRouteFreq = _MvpnBgpMaxSrcActiveAdRouteFreq_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 3, 1, 8),
    _MvpnBgpMaxSrcActiveAdRouteFreq_Type()
)
mvpnBgpMaxSrcActiveAdRouteFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvpnBgpMaxSrcActiveAdRouteFreq.setStatus("current")
if mibBuilder.loadTexts:
    mvpnBgpMaxSrcActiveAdRouteFreq.setUnits("routes per second")
_MvpnPmsiTable_Object = MibTable
mvpnPmsiTable = _MvpnPmsiTable_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4)
)
if mibBuilder.loadTexts:
    mvpnPmsiTable.setStatus("current")
_MvpnPmsiEntry_Object = MibTableRow
mvpnPmsiEntry = _MvpnPmsiEntry_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4, 1)
)
mvpnPmsiEntry.setIndexNames(
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    mvpnPmsiEntry.setStatus("current")
_MvpnPmsiTunnelIfIndex_Type = InterfaceIndex
_MvpnPmsiTunnelIfIndex_Object = MibTableColumn
mvpnPmsiTunnelIfIndex = _MvpnPmsiTunnelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4, 1, 1),
    _MvpnPmsiTunnelIfIndex_Type()
)
mvpnPmsiTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnPmsiTunnelIfIndex.setStatus("current")
_MvpnPmsiRD_Type = MplsL3VpnRouteDistinguisher
_MvpnPmsiRD_Object = MibTableColumn
mvpnPmsiRD = _MvpnPmsiRD_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4, 1, 3),
    _MvpnPmsiRD_Type()
)
mvpnPmsiRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnPmsiRD.setStatus("current")
_MvpnPmsiTunnelType_Type = L2L3VpnMcastProviderTunnelType
_MvpnPmsiTunnelType_Object = MibTableColumn
mvpnPmsiTunnelType = _MvpnPmsiTunnelType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4, 1, 4),
    _MvpnPmsiTunnelType_Type()
)
mvpnPmsiTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnPmsiTunnelType.setStatus("current")
_MvpnPmsiTunnelAttribute_Type = RowPointer
_MvpnPmsiTunnelAttribute_Object = MibTableColumn
mvpnPmsiTunnelAttribute = _MvpnPmsiTunnelAttribute_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4, 1, 5),
    _MvpnPmsiTunnelAttribute_Type()
)
mvpnPmsiTunnelAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnPmsiTunnelAttribute.setStatus("current")
_MvpnPmsiTunnelPimGroupAddrType_Type = InetAddressType
_MvpnPmsiTunnelPimGroupAddrType_Object = MibTableColumn
mvpnPmsiTunnelPimGroupAddrType = _MvpnPmsiTunnelPimGroupAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4, 1, 6),
    _MvpnPmsiTunnelPimGroupAddrType_Type()
)
mvpnPmsiTunnelPimGroupAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnPmsiTunnelPimGroupAddrType.setStatus("current")
_MvpnPmsiTunnelPimGroupAddr_Type = InetAddress
_MvpnPmsiTunnelPimGroupAddr_Object = MibTableColumn
mvpnPmsiTunnelPimGroupAddr = _MvpnPmsiTunnelPimGroupAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4, 1, 7),
    _MvpnPmsiTunnelPimGroupAddr_Type()
)
mvpnPmsiTunnelPimGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnPmsiTunnelPimGroupAddr.setStatus("current")


class _MvpnPmsiEncapsulationType_Type(Integer32):
    """Custom type mvpnPmsiEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greIp", 1),
          ("ipIp", 2),
          ("mpls", 3))
    )


_MvpnPmsiEncapsulationType_Type.__name__ = "Integer32"
_MvpnPmsiEncapsulationType_Object = MibTableColumn
mvpnPmsiEncapsulationType = _MvpnPmsiEncapsulationType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 4, 1, 8),
    _MvpnPmsiEncapsulationType_Type()
)
mvpnPmsiEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnPmsiEncapsulationType.setStatus("current")
_MvpnSpmsiTable_Object = MibTable
mvpnSpmsiTable = _MvpnSpmsiTable_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5)
)
if mibBuilder.loadTexts:
    mvpnSpmsiTable.setStatus("current")
_MvpnSpmsiEntry_Object = MibTableRow
mvpnSpmsiEntry = _MvpnSpmsiEntry_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5, 1)
)
mvpnSpmsiEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnSpmsiCmcastGroupAddrType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnSpmsiCmcastGroupAddr"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnSpmsiCmcastGroupPrefixLen"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnSpmsiCmcastSourceAddrType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnSpmsiCmcastSourceAddr"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnSpmsiCmcastSourcePrefixLen"),
)
if mibBuilder.loadTexts:
    mvpnSpmsiEntry.setStatus("current")
_MvpnSpmsiCmcastGroupAddrType_Type = InetAddressType
_MvpnSpmsiCmcastGroupAddrType_Object = MibTableColumn
mvpnSpmsiCmcastGroupAddrType = _MvpnSpmsiCmcastGroupAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5, 1, 1),
    _MvpnSpmsiCmcastGroupAddrType_Type()
)
mvpnSpmsiCmcastGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnSpmsiCmcastGroupAddrType.setStatus("current")
_MvpnSpmsiCmcastGroupAddr_Type = InetAddress
_MvpnSpmsiCmcastGroupAddr_Object = MibTableColumn
mvpnSpmsiCmcastGroupAddr = _MvpnSpmsiCmcastGroupAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5, 1, 2),
    _MvpnSpmsiCmcastGroupAddr_Type()
)
mvpnSpmsiCmcastGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnSpmsiCmcastGroupAddr.setStatus("current")
_MvpnSpmsiCmcastGroupPrefixLen_Type = InetAddressPrefixLength
_MvpnSpmsiCmcastGroupPrefixLen_Object = MibTableColumn
mvpnSpmsiCmcastGroupPrefixLen = _MvpnSpmsiCmcastGroupPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5, 1, 3),
    _MvpnSpmsiCmcastGroupPrefixLen_Type()
)
mvpnSpmsiCmcastGroupPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnSpmsiCmcastGroupPrefixLen.setStatus("current")
_MvpnSpmsiCmcastSourceAddrType_Type = InetAddressType
_MvpnSpmsiCmcastSourceAddrType_Object = MibTableColumn
mvpnSpmsiCmcastSourceAddrType = _MvpnSpmsiCmcastSourceAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5, 1, 4),
    _MvpnSpmsiCmcastSourceAddrType_Type()
)
mvpnSpmsiCmcastSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnSpmsiCmcastSourceAddrType.setStatus("current")
_MvpnSpmsiCmcastSourceAddr_Type = InetAddress
_MvpnSpmsiCmcastSourceAddr_Object = MibTableColumn
mvpnSpmsiCmcastSourceAddr = _MvpnSpmsiCmcastSourceAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5, 1, 5),
    _MvpnSpmsiCmcastSourceAddr_Type()
)
mvpnSpmsiCmcastSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnSpmsiCmcastSourceAddr.setStatus("current")
_MvpnSpmsiCmcastSourcePrefixLen_Type = InetAddressPrefixLength
_MvpnSpmsiCmcastSourcePrefixLen_Object = MibTableColumn
mvpnSpmsiCmcastSourcePrefixLen = _MvpnSpmsiCmcastSourcePrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5, 1, 6),
    _MvpnSpmsiCmcastSourcePrefixLen_Type()
)
mvpnSpmsiCmcastSourcePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnSpmsiCmcastSourcePrefixLen.setStatus("current")
_MvpnSpmsiPmsiPointer_Type = RowPointer
_MvpnSpmsiPmsiPointer_Object = MibTableColumn
mvpnSpmsiPmsiPointer = _MvpnSpmsiPmsiPointer_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 5, 1, 7),
    _MvpnSpmsiPmsiPointer_Type()
)
mvpnSpmsiPmsiPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnSpmsiPmsiPointer.setStatus("current")
_MvpnAdvtStatsTable_Object = MibTable
mvpnAdvtStatsTable = _MvpnAdvtStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6)
)
if mibBuilder.loadTexts:
    mvpnAdvtStatsTable.setStatus("current")
_MvpnAdvtStatsEntry_Object = MibTableRow
mvpnAdvtStatsEntry = _MvpnAdvtStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1)
)
mvpnAdvtStatsEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtPeerAddrType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtPeerAddr"),
)
if mibBuilder.loadTexts:
    mvpnAdvtStatsEntry.setStatus("current")


class _MvpnAdvtType_Type(Integer32):
    """Custom type mvpnAdvtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intraAsIpmsi", 0),
          ("interAsIpmsi", 1),
          ("sPmsi", 2))
    )


_MvpnAdvtType_Type.__name__ = "Integer32"
_MvpnAdvtType_Object = MibTableColumn
mvpnAdvtType = _MvpnAdvtType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 1),
    _MvpnAdvtType_Type()
)
mvpnAdvtType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnAdvtType.setStatus("current")
_MvpnAdvtPeerAddrType_Type = InetAddressType
_MvpnAdvtPeerAddrType_Object = MibTableColumn
mvpnAdvtPeerAddrType = _MvpnAdvtPeerAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 2),
    _MvpnAdvtPeerAddrType_Type()
)
mvpnAdvtPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnAdvtPeerAddrType.setStatus("current")
_MvpnAdvtPeerAddr_Type = InetAddress
_MvpnAdvtPeerAddr_Object = MibTableColumn
mvpnAdvtPeerAddr = _MvpnAdvtPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 3),
    _MvpnAdvtPeerAddr_Type()
)
mvpnAdvtPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnAdvtPeerAddr.setStatus("current")
_MvpnAdvtSent_Type = Counter32
_MvpnAdvtSent_Object = MibTableColumn
mvpnAdvtSent = _MvpnAdvtSent_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 4),
    _MvpnAdvtSent_Type()
)
mvpnAdvtSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnAdvtSent.setStatus("current")
_MvpnAdvtReceived_Type = Counter32
_MvpnAdvtReceived_Object = MibTableColumn
mvpnAdvtReceived = _MvpnAdvtReceived_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 5),
    _MvpnAdvtReceived_Type()
)
mvpnAdvtReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnAdvtReceived.setStatus("current")
_MvpnAdvtReceivedError_Type = Counter32
_MvpnAdvtReceivedError_Object = MibTableColumn
mvpnAdvtReceivedError = _MvpnAdvtReceivedError_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 6),
    _MvpnAdvtReceivedError_Type()
)
mvpnAdvtReceivedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnAdvtReceivedError.setStatus("current")
_MvpnAdvtReceivedMalformedTunnelType_Type = Counter32
_MvpnAdvtReceivedMalformedTunnelType_Object = MibTableColumn
mvpnAdvtReceivedMalformedTunnelType = _MvpnAdvtReceivedMalformedTunnelType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 7),
    _MvpnAdvtReceivedMalformedTunnelType_Type()
)
mvpnAdvtReceivedMalformedTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnAdvtReceivedMalformedTunnelType.setStatus("current")
_MvpnAdvtReceivedMalformedTunnelId_Type = Counter32
_MvpnAdvtReceivedMalformedTunnelId_Object = MibTableColumn
mvpnAdvtReceivedMalformedTunnelId = _MvpnAdvtReceivedMalformedTunnelId_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 8),
    _MvpnAdvtReceivedMalformedTunnelId_Type()
)
mvpnAdvtReceivedMalformedTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnAdvtReceivedMalformedTunnelId.setStatus("current")
_MvpnAdvtLastSentTime_Type = DateAndTime
_MvpnAdvtLastSentTime_Object = MibTableColumn
mvpnAdvtLastSentTime = _MvpnAdvtLastSentTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 9),
    _MvpnAdvtLastSentTime_Type()
)
mvpnAdvtLastSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnAdvtLastSentTime.setStatus("current")
_MvpnAdvtLastReceivedTime_Type = DateAndTime
_MvpnAdvtLastReceivedTime_Object = MibTableColumn
mvpnAdvtLastReceivedTime = _MvpnAdvtLastReceivedTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 10),
    _MvpnAdvtLastReceivedTime_Type()
)
mvpnAdvtLastReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnAdvtLastReceivedTime.setStatus("current")
_MvpnAdvtCounterDiscontinuityTime_Type = TimeStamp
_MvpnAdvtCounterDiscontinuityTime_Object = MibTableColumn
mvpnAdvtCounterDiscontinuityTime = _MvpnAdvtCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 6, 1, 11),
    _MvpnAdvtCounterDiscontinuityTime_Type()
)
mvpnAdvtCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnAdvtCounterDiscontinuityTime.setStatus("current")
_MvpnMrouteTable_Object = MibTable
mvpnMrouteTable = _MvpnMrouteTable_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7)
)
if mibBuilder.loadTexts:
    mvpnMrouteTable.setStatus("current")
_MvpnMrouteEntry_Object = MibTableRow
mvpnMrouteEntry = _MvpnMrouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1)
)
mvpnMrouteEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteCmcastGroupAddrType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteCmcastGroupAddr"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteCmcastGroupPrefixLength"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteCmcastSourceAddrType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteCmcastSourceAddrs"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteCmcastSourcePrefixLength"),
)
if mibBuilder.loadTexts:
    mvpnMrouteEntry.setStatus("current")
_MvpnMrouteCmcastGroupAddrType_Type = InetAddressType
_MvpnMrouteCmcastGroupAddrType_Object = MibTableColumn
mvpnMrouteCmcastGroupAddrType = _MvpnMrouteCmcastGroupAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 1),
    _MvpnMrouteCmcastGroupAddrType_Type()
)
mvpnMrouteCmcastGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteCmcastGroupAddrType.setStatus("current")
_MvpnMrouteCmcastGroupAddr_Type = InetAddress
_MvpnMrouteCmcastGroupAddr_Object = MibTableColumn
mvpnMrouteCmcastGroupAddr = _MvpnMrouteCmcastGroupAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 2),
    _MvpnMrouteCmcastGroupAddr_Type()
)
mvpnMrouteCmcastGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteCmcastGroupAddr.setStatus("current")
_MvpnMrouteCmcastGroupPrefixLength_Type = InetAddressPrefixLength
_MvpnMrouteCmcastGroupPrefixLength_Object = MibTableColumn
mvpnMrouteCmcastGroupPrefixLength = _MvpnMrouteCmcastGroupPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 3),
    _MvpnMrouteCmcastGroupPrefixLength_Type()
)
mvpnMrouteCmcastGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteCmcastGroupPrefixLength.setStatus("current")
_MvpnMrouteCmcastSourceAddrType_Type = InetAddressType
_MvpnMrouteCmcastSourceAddrType_Object = MibTableColumn
mvpnMrouteCmcastSourceAddrType = _MvpnMrouteCmcastSourceAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 4),
    _MvpnMrouteCmcastSourceAddrType_Type()
)
mvpnMrouteCmcastSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteCmcastSourceAddrType.setStatus("current")
_MvpnMrouteCmcastSourceAddrs_Type = InetAddress
_MvpnMrouteCmcastSourceAddrs_Object = MibTableColumn
mvpnMrouteCmcastSourceAddrs = _MvpnMrouteCmcastSourceAddrs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 5),
    _MvpnMrouteCmcastSourceAddrs_Type()
)
mvpnMrouteCmcastSourceAddrs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteCmcastSourceAddrs.setStatus("current")
_MvpnMrouteCmcastSourcePrefixLength_Type = InetAddressPrefixLength
_MvpnMrouteCmcastSourcePrefixLength_Object = MibTableColumn
mvpnMrouteCmcastSourcePrefixLength = _MvpnMrouteCmcastSourcePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 6),
    _MvpnMrouteCmcastSourcePrefixLength_Type()
)
mvpnMrouteCmcastSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteCmcastSourcePrefixLength.setStatus("current")
_MvpnMrouteUpstreamNeighborAddrType_Type = InetAddressType
_MvpnMrouteUpstreamNeighborAddrType_Object = MibTableColumn
mvpnMrouteUpstreamNeighborAddrType = _MvpnMrouteUpstreamNeighborAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 7),
    _MvpnMrouteUpstreamNeighborAddrType_Type()
)
mvpnMrouteUpstreamNeighborAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteUpstreamNeighborAddrType.setStatus("current")
_MvpnMrouteUpstreamNeighborAddr_Type = InetAddress
_MvpnMrouteUpstreamNeighborAddr_Object = MibTableColumn
mvpnMrouteUpstreamNeighborAddr = _MvpnMrouteUpstreamNeighborAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 8),
    _MvpnMrouteUpstreamNeighborAddr_Type()
)
mvpnMrouteUpstreamNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteUpstreamNeighborAddr.setStatus("current")
_MvpnMrouteInIfIndex_Type = InterfaceIndexOrZero
_MvpnMrouteInIfIndex_Object = MibTableColumn
mvpnMrouteInIfIndex = _MvpnMrouteInIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 9),
    _MvpnMrouteInIfIndex_Type()
)
mvpnMrouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteInIfIndex.setStatus("current")
_MvpnMrouteExpiryTime_Type = TimeTicks
_MvpnMrouteExpiryTime_Object = MibTableColumn
mvpnMrouteExpiryTime = _MvpnMrouteExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 10),
    _MvpnMrouteExpiryTime_Type()
)
mvpnMrouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteExpiryTime.setStatus("current")
_MvpnMrouteProtocol_Type = IANAipMRouteProtocol
_MvpnMrouteProtocol_Object = MibTableColumn
mvpnMrouteProtocol = _MvpnMrouteProtocol_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 11),
    _MvpnMrouteProtocol_Type()
)
mvpnMrouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteProtocol.setStatus("current")
_MvpnMrouteRtProtocol_Type = IANAipRouteProtocol
_MvpnMrouteRtProtocol_Object = MibTableColumn
mvpnMrouteRtProtocol = _MvpnMrouteRtProtocol_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 12),
    _MvpnMrouteRtProtocol_Type()
)
mvpnMrouteRtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteRtProtocol.setStatus("current")
_MvpnMrouteRtAddrType_Type = InetAddressType
_MvpnMrouteRtAddrType_Object = MibTableColumn
mvpnMrouteRtAddrType = _MvpnMrouteRtAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 13),
    _MvpnMrouteRtAddrType_Type()
)
mvpnMrouteRtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteRtAddrType.setStatus("current")
_MvpnMrouteRtAddr_Type = InetAddress
_MvpnMrouteRtAddr_Object = MibTableColumn
mvpnMrouteRtAddr = _MvpnMrouteRtAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 14),
    _MvpnMrouteRtAddr_Type()
)
mvpnMrouteRtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteRtAddr.setStatus("current")
_MvpnMrouteRtPrefixLength_Type = InetAddressPrefixLength
_MvpnMrouteRtPrefixLength_Object = MibTableColumn
mvpnMrouteRtPrefixLength = _MvpnMrouteRtPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 15),
    _MvpnMrouteRtPrefixLength_Type()
)
mvpnMrouteRtPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteRtPrefixLength.setStatus("current")


class _MvpnMrouteRtType_Type(Integer32):
    """Custom type mvpnMrouteRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_MvpnMrouteRtType_Type.__name__ = "Integer32"
_MvpnMrouteRtType_Object = MibTableColumn
mvpnMrouteRtType = _MvpnMrouteRtType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 16),
    _MvpnMrouteRtType_Type()
)
mvpnMrouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteRtType.setStatus("current")
_MvpnMrouteOctets_Type = Counter64
_MvpnMrouteOctets_Object = MibTableColumn
mvpnMrouteOctets = _MvpnMrouteOctets_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 17),
    _MvpnMrouteOctets_Type()
)
mvpnMrouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteOctets.setStatus("current")
_MvpnMroutePkts_Type = Counter64
_MvpnMroutePkts_Object = MibTableColumn
mvpnMroutePkts = _MvpnMroutePkts_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 18),
    _MvpnMroutePkts_Type()
)
mvpnMroutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMroutePkts.setStatus("current")
_MvpnMrouteTtlDroppedOctets_Type = Counter64
_MvpnMrouteTtlDroppedOctets_Object = MibTableColumn
mvpnMrouteTtlDroppedOctets = _MvpnMrouteTtlDroppedOctets_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 19),
    _MvpnMrouteTtlDroppedOctets_Type()
)
mvpnMrouteTtlDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteTtlDroppedOctets.setStatus("current")
_MvpnMrouteTtlDroppedPackets_Type = Counter64
_MvpnMrouteTtlDroppedPackets_Object = MibTableColumn
mvpnMrouteTtlDroppedPackets = _MvpnMrouteTtlDroppedPackets_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 20),
    _MvpnMrouteTtlDroppedPackets_Type()
)
mvpnMrouteTtlDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteTtlDroppedPackets.setStatus("current")
_MvpnMrouteDroppedInOctets_Type = Counter64
_MvpnMrouteDroppedInOctets_Object = MibTableColumn
mvpnMrouteDroppedInOctets = _MvpnMrouteDroppedInOctets_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 21),
    _MvpnMrouteDroppedInOctets_Type()
)
mvpnMrouteDroppedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteDroppedInOctets.setStatus("current")
_MvpnMrouteDroppedInPackets_Type = Counter64
_MvpnMrouteDroppedInPackets_Object = MibTableColumn
mvpnMrouteDroppedInPackets = _MvpnMrouteDroppedInPackets_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 22),
    _MvpnMrouteDroppedInPackets_Type()
)
mvpnMrouteDroppedInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteDroppedInPackets.setStatus("current")
_MvpnMroutePmsiPointer_Type = RowPointer
_MvpnMroutePmsiPointer_Object = MibTableColumn
mvpnMroutePmsiPointer = _MvpnMroutePmsiPointer_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 23),
    _MvpnMroutePmsiPointer_Type()
)
mvpnMroutePmsiPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMroutePmsiPointer.setStatus("current")
_MvpnMrouteNumberOfLocalReplication_Type = Unsigned32
_MvpnMrouteNumberOfLocalReplication_Object = MibTableColumn
mvpnMrouteNumberOfLocalReplication = _MvpnMrouteNumberOfLocalReplication_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 24),
    _MvpnMrouteNumberOfLocalReplication_Type()
)
mvpnMrouteNumberOfLocalReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNumberOfLocalReplication.setStatus("current")
_MvpnMrouteNumberOfRemoteReplication_Type = Unsigned32
_MvpnMrouteNumberOfRemoteReplication_Object = MibTableColumn
mvpnMrouteNumberOfRemoteReplication = _MvpnMrouteNumberOfRemoteReplication_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 25),
    _MvpnMrouteNumberOfRemoteReplication_Type()
)
mvpnMrouteNumberOfRemoteReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNumberOfRemoteReplication.setStatus("current")
_MvpnMrouteCounterDiscontinuityTime_Type = TimeStamp
_MvpnMrouteCounterDiscontinuityTime_Object = MibTableColumn
mvpnMrouteCounterDiscontinuityTime = _MvpnMrouteCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 7, 1, 26),
    _MvpnMrouteCounterDiscontinuityTime_Type()
)
mvpnMrouteCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteCounterDiscontinuityTime.setStatus("current")
_MvpnMrouteNextHopTable_Object = MibTable
mvpnMrouteNextHopTable = _MvpnMrouteNextHopTable_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8)
)
if mibBuilder.loadTexts:
    mvpnMrouteNextHopTable.setStatus("current")
_MvpnMrouteNextHopEntry_Object = MibTableRow
mvpnMrouteNextHopEntry = _MvpnMrouteNextHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1)
)
mvpnMrouteNextHopEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopGroupAddrType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopGroupAddr"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopGroupPrefixLength"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopSourceAddrType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopSourceAddrs"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopSourcePrefixLength"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopIfIndex"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopAddrType"),
    (0, "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopAddr"),
)
if mibBuilder.loadTexts:
    mvpnMrouteNextHopEntry.setStatus("current")
_MvpnMrouteNextHopGroupAddrType_Type = InetAddressType
_MvpnMrouteNextHopGroupAddrType_Object = MibTableColumn
mvpnMrouteNextHopGroupAddrType = _MvpnMrouteNextHopGroupAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 1),
    _MvpnMrouteNextHopGroupAddrType_Type()
)
mvpnMrouteNextHopGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopGroupAddrType.setStatus("current")
_MvpnMrouteNextHopGroupAddr_Type = InetAddress
_MvpnMrouteNextHopGroupAddr_Object = MibTableColumn
mvpnMrouteNextHopGroupAddr = _MvpnMrouteNextHopGroupAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 2),
    _MvpnMrouteNextHopGroupAddr_Type()
)
mvpnMrouteNextHopGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopGroupAddr.setStatus("current")
_MvpnMrouteNextHopGroupPrefixLength_Type = InetAddressPrefixLength
_MvpnMrouteNextHopGroupPrefixLength_Object = MibTableColumn
mvpnMrouteNextHopGroupPrefixLength = _MvpnMrouteNextHopGroupPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 3),
    _MvpnMrouteNextHopGroupPrefixLength_Type()
)
mvpnMrouteNextHopGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopGroupPrefixLength.setStatus("current")
_MvpnMrouteNextHopSourceAddrType_Type = InetAddressType
_MvpnMrouteNextHopSourceAddrType_Object = MibTableColumn
mvpnMrouteNextHopSourceAddrType = _MvpnMrouteNextHopSourceAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 4),
    _MvpnMrouteNextHopSourceAddrType_Type()
)
mvpnMrouteNextHopSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopSourceAddrType.setStatus("current")
_MvpnMrouteNextHopSourceAddrs_Type = InetAddress
_MvpnMrouteNextHopSourceAddrs_Object = MibTableColumn
mvpnMrouteNextHopSourceAddrs = _MvpnMrouteNextHopSourceAddrs_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 5),
    _MvpnMrouteNextHopSourceAddrs_Type()
)
mvpnMrouteNextHopSourceAddrs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopSourceAddrs.setStatus("current")
_MvpnMrouteNextHopSourcePrefixLength_Type = InetAddressPrefixLength
_MvpnMrouteNextHopSourcePrefixLength_Object = MibTableColumn
mvpnMrouteNextHopSourcePrefixLength = _MvpnMrouteNextHopSourcePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 6),
    _MvpnMrouteNextHopSourcePrefixLength_Type()
)
mvpnMrouteNextHopSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopSourcePrefixLength.setStatus("current")
_MvpnMrouteNextHopIfIndex_Type = InterfaceIndex
_MvpnMrouteNextHopIfIndex_Object = MibTableColumn
mvpnMrouteNextHopIfIndex = _MvpnMrouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 7),
    _MvpnMrouteNextHopIfIndex_Type()
)
mvpnMrouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopIfIndex.setStatus("current")
_MvpnMrouteNextHopAddrType_Type = InetAddressType
_MvpnMrouteNextHopAddrType_Object = MibTableColumn
mvpnMrouteNextHopAddrType = _MvpnMrouteNextHopAddrType_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 8),
    _MvpnMrouteNextHopAddrType_Type()
)
mvpnMrouteNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopAddrType.setStatus("current")
_MvpnMrouteNextHopAddr_Type = InetAddress
_MvpnMrouteNextHopAddr_Object = MibTableColumn
mvpnMrouteNextHopAddr = _MvpnMrouteNextHopAddr_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 9),
    _MvpnMrouteNextHopAddr_Type()
)
mvpnMrouteNextHopAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopAddr.setStatus("current")


class _MvpnMrouteNextHopState_Type(Integer32):
    """Custom type mvpnMrouteNextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pruned", 1),
          ("forwarding", 2))
    )


_MvpnMrouteNextHopState_Type.__name__ = "Integer32"
_MvpnMrouteNextHopState_Object = MibTableColumn
mvpnMrouteNextHopState = _MvpnMrouteNextHopState_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 10),
    _MvpnMrouteNextHopState_Type()
)
mvpnMrouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopState.setStatus("current")
_MvpnMrouteNextHopExpiryTime_Type = TimeTicks
_MvpnMrouteNextHopExpiryTime_Object = MibTableColumn
mvpnMrouteNextHopExpiryTime = _MvpnMrouteNextHopExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 11),
    _MvpnMrouteNextHopExpiryTime_Type()
)
mvpnMrouteNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopExpiryTime.setStatus("current")


class _MvpnMrouteNextHopClosestMemberHops_Type(Unsigned32):
    """Custom type mvpnMrouteNextHopClosestMemberHops based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MvpnMrouteNextHopClosestMemberHops_Type.__name__ = "Unsigned32"
_MvpnMrouteNextHopClosestMemberHops_Object = MibTableColumn
mvpnMrouteNextHopClosestMemberHops = _MvpnMrouteNextHopClosestMemberHops_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 12),
    _MvpnMrouteNextHopClosestMemberHops_Type()
)
mvpnMrouteNextHopClosestMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopClosestMemberHops.setStatus("current")
_MvpnMrouteNextHopProtocol_Type = IANAipMRouteProtocol
_MvpnMrouteNextHopProtocol_Object = MibTableColumn
mvpnMrouteNextHopProtocol = _MvpnMrouteNextHopProtocol_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 13),
    _MvpnMrouteNextHopProtocol_Type()
)
mvpnMrouteNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopProtocol.setStatus("current")
_MvpnMrouteNextHopOctets_Type = Counter64
_MvpnMrouteNextHopOctets_Object = MibTableColumn
mvpnMrouteNextHopOctets = _MvpnMrouteNextHopOctets_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 14),
    _MvpnMrouteNextHopOctets_Type()
)
mvpnMrouteNextHopOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopOctets.setStatus("current")
_MvpnMrouteNextHopPkts_Type = Counter64
_MvpnMrouteNextHopPkts_Object = MibTableColumn
mvpnMrouteNextHopPkts = _MvpnMrouteNextHopPkts_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 15),
    _MvpnMrouteNextHopPkts_Type()
)
mvpnMrouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopPkts.setStatus("current")
_MvpnMrouteNextHopCounterDiscontinuityTime_Type = TimeStamp
_MvpnMrouteNextHopCounterDiscontinuityTime_Object = MibTableColumn
mvpnMrouteNextHopCounterDiscontinuityTime = _MvpnMrouteNextHopCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 243, 1, 8, 1, 16),
    _MvpnMrouteNextHopCounterDiscontinuityTime_Type()
)
mvpnMrouteNextHopCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvpnMrouteNextHopCounterDiscontinuityTime.setStatus("current")
_MvpnConformance_ObjectIdentity = ObjectIdentity
mvpnConformance = _MvpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 243, 2)
)
_MvpnGroups_ObjectIdentity = ObjectIdentity
mvpnGroups = _MvpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 243, 2, 1)
)
_MvpnCompliances_ObjectIdentity = ObjectIdentity
mvpnCompliances = _MvpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 243, 2, 2)
)

# Managed Objects groups

mvpnScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 1)
)
mvpnScalarGroup.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMvrfs"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnV4Mvrfs"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnV6Mvrfs"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPimV4Mvrfs"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPimV6Mvrfs"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnSPTunnelLimit"))
)
if mibBuilder.loadTexts:
    mvpnScalarGroup.setStatus("current")

mvpnBgpScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 2)
)
mvpnBgpScalarGroup.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMldpMvrfs"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpV4Mvrfs"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpV6Mvrfs"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpCmcastRouteWithdrawalTimer"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpSrcSharedTreeJoinTimer"))
)
if mibBuilder.loadTexts:
    mvpnBgpScalarGroup.setStatus("current")

mvpnGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 3)
)
mvpnGenericGroup.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenMvrfLastAction"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenMvrfLastActionTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenMvrfCreationTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenCmcastRouteProtocol"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenIpmsiInfo"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenInterAsPmsiInfo"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenUmhSelection"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenCustomerSiteType"))
)
if mibBuilder.loadTexts:
    mvpnGenericGroup.setStatus("current")

mvpnBgpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 4)
)
mvpnBgpGroup.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpMode"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpVrfRouteImportExtendedCommunity"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpSrcASExtendedCommunity"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpMsgRateLimit"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpMaxSpmsiAdRoutes"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpMaxSpmsiAdRouteFreq"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpMaxSrcActiveAdRoutes"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpMaxSrcActiveAdRouteFreq"))
)
if mibBuilder.loadTexts:
    mvpnBgpGroup.setStatus("current")

mvpnPmsiGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 5)
)
mvpnPmsiGroup.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiRD"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiTunnelType"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiTunnelAttribute"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiTunnelPimGroupAddrType"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiTunnelPimGroupAddr"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiEncapsulationType"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnSpmsiPmsiPointer"))
)
if mibBuilder.loadTexts:
    mvpnPmsiGroup.setStatus("current")

mvpnAdvtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 6)
)
mvpnAdvtStatsGroup.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtSent"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtReceived"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtReceivedError"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtReceivedMalformedTunnelType"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtReceivedMalformedTunnelId"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtLastSentTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtLastReceivedTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mvpnAdvtStatsGroup.setStatus("current")

mvpnMrouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 7)
)
mvpnMrouteGroup.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteUpstreamNeighborAddrType"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteUpstreamNeighborAddr"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteInIfIndex"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteExpiryTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteProtocol"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteRtProtocol"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteRtAddrType"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteRtAddr"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteRtPrefixLength"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteRtType"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteOctets"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMroutePkts"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteTtlDroppedOctets"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteTtlDroppedPackets"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteDroppedInOctets"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteDroppedInPackets"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMroutePmsiPointer"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNumberOfLocalReplication"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNumberOfRemoteReplication"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mvpnMrouteGroup.setStatus("current")

mvpnMrouteNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 8)
)
mvpnMrouteNextHopGroup.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopState"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopExpiryTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopClosestMemberHops"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopProtocol"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopOctets"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopPkts"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mvpnMrouteNextHopGroup.setStatus("current")


# Notification objects

mvpnMvrfActionTaken = NotificationType(
    (1, 3, 6, 1, 2, 1, 243, 0, 1)
)
mvpnMvrfActionTaken.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenMvrfCreationTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenMvrfLastAction"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenMvrfLastActionTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenMvrfCreationTime"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenCmcastRouteProtocol"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenUmhSelection"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenCustomerSiteType"))
)
if mibBuilder.loadTexts:
    mvpnMvrfActionTaken.setStatus(
        "current"
    )


# Notifications groups

mvpnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 243, 2, 1, 9)
)
mvpnNotificationGroup.setObjects(
    ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMvrfActionTaken")
)
if mibBuilder.loadTexts:
    mvpnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mvpnModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 243, 2, 2, 1)
)
mvpnModuleFullCompliance.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnScalarGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenericGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtStatsGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnNotificationGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpScalarGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpGroup"))
)
if mibBuilder.loadTexts:
    mvpnModuleFullCompliance.setStatus(
        "current"
    )

mvpnModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 243, 2, 2, 2)
)
mvpnModuleReadOnlyCompliance.setObjects(
      *(("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnScalarGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnGenericGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnPmsiGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtStatsGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnMrouteNextHopGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnNotificationGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpScalarGroup"),
        ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnBgpGroup"))
)
if mibBuilder.loadTexts:
    mvpnModuleReadOnlyCompliance.setStatus(
        "current"
    )

mvpnModuleAdvtStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 243, 2, 2, 3)
)
mvpnModuleAdvtStatsCompliance.setObjects(
    ("BGP-MPLS-LAYER3-VPN-MULTICAST-MIB", "mvpnAdvtStatsGroup")
)
if mibBuilder.loadTexts:
    mvpnModuleAdvtStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BGP-MPLS-LAYER3-VPN-MULTICAST-MIB",
    **{"mvpnMIB": mvpnMIB,
       "mvpnNotifications": mvpnNotifications,
       "mvpnMvrfActionTaken": mvpnMvrfActionTaken,
       "mvpnObjects": mvpnObjects,
       "mvpnScalars": mvpnScalars,
       "mvpnMvrfs": mvpnMvrfs,
       "mvpnV4Mvrfs": mvpnV4Mvrfs,
       "mvpnV6Mvrfs": mvpnV6Mvrfs,
       "mvpnMldpMvrfs": mvpnMldpMvrfs,
       "mvpnPimV4Mvrfs": mvpnPimV4Mvrfs,
       "mvpnPimV6Mvrfs": mvpnPimV6Mvrfs,
       "mvpnBgpV4Mvrfs": mvpnBgpV4Mvrfs,
       "mvpnBgpV6Mvrfs": mvpnBgpV6Mvrfs,
       "mvpnSPTunnelLimit": mvpnSPTunnelLimit,
       "mvpnBgpCmcastRouteWithdrawalTimer": mvpnBgpCmcastRouteWithdrawalTimer,
       "mvpnBgpSrcSharedTreeJoinTimer": mvpnBgpSrcSharedTreeJoinTimer,
       "mvpnGenericTable": mvpnGenericTable,
       "mvpnGenericEntry": mvpnGenericEntry,
       "mvpnGenMvrfLastAction": mvpnGenMvrfLastAction,
       "mvpnGenMvrfLastActionTime": mvpnGenMvrfLastActionTime,
       "mvpnGenMvrfCreationTime": mvpnGenMvrfCreationTime,
       "mvpnGenCmcastRouteProtocol": mvpnGenCmcastRouteProtocol,
       "mvpnGenIpmsiInfo": mvpnGenIpmsiInfo,
       "mvpnGenInterAsPmsiInfo": mvpnGenInterAsPmsiInfo,
       "mvpnGenUmhSelection": mvpnGenUmhSelection,
       "mvpnGenCustomerSiteType": mvpnGenCustomerSiteType,
       "mvpnBgpTable": mvpnBgpTable,
       "mvpnBgpEntry": mvpnBgpEntry,
       "mvpnBgpMode": mvpnBgpMode,
       "mvpnBgpVrfRouteImportExtendedCommunity": mvpnBgpVrfRouteImportExtendedCommunity,
       "mvpnBgpSrcASExtendedCommunity": mvpnBgpSrcASExtendedCommunity,
       "mvpnBgpMsgRateLimit": mvpnBgpMsgRateLimit,
       "mvpnBgpMaxSpmsiAdRoutes": mvpnBgpMaxSpmsiAdRoutes,
       "mvpnBgpMaxSpmsiAdRouteFreq": mvpnBgpMaxSpmsiAdRouteFreq,
       "mvpnBgpMaxSrcActiveAdRoutes": mvpnBgpMaxSrcActiveAdRoutes,
       "mvpnBgpMaxSrcActiveAdRouteFreq": mvpnBgpMaxSrcActiveAdRouteFreq,
       "mvpnPmsiTable": mvpnPmsiTable,
       "mvpnPmsiEntry": mvpnPmsiEntry,
       "mvpnPmsiTunnelIfIndex": mvpnPmsiTunnelIfIndex,
       "mvpnPmsiRD": mvpnPmsiRD,
       "mvpnPmsiTunnelType": mvpnPmsiTunnelType,
       "mvpnPmsiTunnelAttribute": mvpnPmsiTunnelAttribute,
       "mvpnPmsiTunnelPimGroupAddrType": mvpnPmsiTunnelPimGroupAddrType,
       "mvpnPmsiTunnelPimGroupAddr": mvpnPmsiTunnelPimGroupAddr,
       "mvpnPmsiEncapsulationType": mvpnPmsiEncapsulationType,
       "mvpnSpmsiTable": mvpnSpmsiTable,
       "mvpnSpmsiEntry": mvpnSpmsiEntry,
       "mvpnSpmsiCmcastGroupAddrType": mvpnSpmsiCmcastGroupAddrType,
       "mvpnSpmsiCmcastGroupAddr": mvpnSpmsiCmcastGroupAddr,
       "mvpnSpmsiCmcastGroupPrefixLen": mvpnSpmsiCmcastGroupPrefixLen,
       "mvpnSpmsiCmcastSourceAddrType": mvpnSpmsiCmcastSourceAddrType,
       "mvpnSpmsiCmcastSourceAddr": mvpnSpmsiCmcastSourceAddr,
       "mvpnSpmsiCmcastSourcePrefixLen": mvpnSpmsiCmcastSourcePrefixLen,
       "mvpnSpmsiPmsiPointer": mvpnSpmsiPmsiPointer,
       "mvpnAdvtStatsTable": mvpnAdvtStatsTable,
       "mvpnAdvtStatsEntry": mvpnAdvtStatsEntry,
       "mvpnAdvtType": mvpnAdvtType,
       "mvpnAdvtPeerAddrType": mvpnAdvtPeerAddrType,
       "mvpnAdvtPeerAddr": mvpnAdvtPeerAddr,
       "mvpnAdvtSent": mvpnAdvtSent,
       "mvpnAdvtReceived": mvpnAdvtReceived,
       "mvpnAdvtReceivedError": mvpnAdvtReceivedError,
       "mvpnAdvtReceivedMalformedTunnelType": mvpnAdvtReceivedMalformedTunnelType,
       "mvpnAdvtReceivedMalformedTunnelId": mvpnAdvtReceivedMalformedTunnelId,
       "mvpnAdvtLastSentTime": mvpnAdvtLastSentTime,
       "mvpnAdvtLastReceivedTime": mvpnAdvtLastReceivedTime,
       "mvpnAdvtCounterDiscontinuityTime": mvpnAdvtCounterDiscontinuityTime,
       "mvpnMrouteTable": mvpnMrouteTable,
       "mvpnMrouteEntry": mvpnMrouteEntry,
       "mvpnMrouteCmcastGroupAddrType": mvpnMrouteCmcastGroupAddrType,
       "mvpnMrouteCmcastGroupAddr": mvpnMrouteCmcastGroupAddr,
       "mvpnMrouteCmcastGroupPrefixLength": mvpnMrouteCmcastGroupPrefixLength,
       "mvpnMrouteCmcastSourceAddrType": mvpnMrouteCmcastSourceAddrType,
       "mvpnMrouteCmcastSourceAddrs": mvpnMrouteCmcastSourceAddrs,
       "mvpnMrouteCmcastSourcePrefixLength": mvpnMrouteCmcastSourcePrefixLength,
       "mvpnMrouteUpstreamNeighborAddrType": mvpnMrouteUpstreamNeighborAddrType,
       "mvpnMrouteUpstreamNeighborAddr": mvpnMrouteUpstreamNeighborAddr,
       "mvpnMrouteInIfIndex": mvpnMrouteInIfIndex,
       "mvpnMrouteExpiryTime": mvpnMrouteExpiryTime,
       "mvpnMrouteProtocol": mvpnMrouteProtocol,
       "mvpnMrouteRtProtocol": mvpnMrouteRtProtocol,
       "mvpnMrouteRtAddrType": mvpnMrouteRtAddrType,
       "mvpnMrouteRtAddr": mvpnMrouteRtAddr,
       "mvpnMrouteRtPrefixLength": mvpnMrouteRtPrefixLength,
       "mvpnMrouteRtType": mvpnMrouteRtType,
       "mvpnMrouteOctets": mvpnMrouteOctets,
       "mvpnMroutePkts": mvpnMroutePkts,
       "mvpnMrouteTtlDroppedOctets": mvpnMrouteTtlDroppedOctets,
       "mvpnMrouteTtlDroppedPackets": mvpnMrouteTtlDroppedPackets,
       "mvpnMrouteDroppedInOctets": mvpnMrouteDroppedInOctets,
       "mvpnMrouteDroppedInPackets": mvpnMrouteDroppedInPackets,
       "mvpnMroutePmsiPointer": mvpnMroutePmsiPointer,
       "mvpnMrouteNumberOfLocalReplication": mvpnMrouteNumberOfLocalReplication,
       "mvpnMrouteNumberOfRemoteReplication": mvpnMrouteNumberOfRemoteReplication,
       "mvpnMrouteCounterDiscontinuityTime": mvpnMrouteCounterDiscontinuityTime,
       "mvpnMrouteNextHopTable": mvpnMrouteNextHopTable,
       "mvpnMrouteNextHopEntry": mvpnMrouteNextHopEntry,
       "mvpnMrouteNextHopGroupAddrType": mvpnMrouteNextHopGroupAddrType,
       "mvpnMrouteNextHopGroupAddr": mvpnMrouteNextHopGroupAddr,
       "mvpnMrouteNextHopGroupPrefixLength": mvpnMrouteNextHopGroupPrefixLength,
       "mvpnMrouteNextHopSourceAddrType": mvpnMrouteNextHopSourceAddrType,
       "mvpnMrouteNextHopSourceAddrs": mvpnMrouteNextHopSourceAddrs,
       "mvpnMrouteNextHopSourcePrefixLength": mvpnMrouteNextHopSourcePrefixLength,
       "mvpnMrouteNextHopIfIndex": mvpnMrouteNextHopIfIndex,
       "mvpnMrouteNextHopAddrType": mvpnMrouteNextHopAddrType,
       "mvpnMrouteNextHopAddr": mvpnMrouteNextHopAddr,
       "mvpnMrouteNextHopState": mvpnMrouteNextHopState,
       "mvpnMrouteNextHopExpiryTime": mvpnMrouteNextHopExpiryTime,
       "mvpnMrouteNextHopClosestMemberHops": mvpnMrouteNextHopClosestMemberHops,
       "mvpnMrouteNextHopProtocol": mvpnMrouteNextHopProtocol,
       "mvpnMrouteNextHopOctets": mvpnMrouteNextHopOctets,
       "mvpnMrouteNextHopPkts": mvpnMrouteNextHopPkts,
       "mvpnMrouteNextHopCounterDiscontinuityTime": mvpnMrouteNextHopCounterDiscontinuityTime,
       "mvpnConformance": mvpnConformance,
       "mvpnGroups": mvpnGroups,
       "mvpnScalarGroup": mvpnScalarGroup,
       "mvpnBgpScalarGroup": mvpnBgpScalarGroup,
       "mvpnGenericGroup": mvpnGenericGroup,
       "mvpnBgpGroup": mvpnBgpGroup,
       "mvpnPmsiGroup": mvpnPmsiGroup,
       "mvpnAdvtStatsGroup": mvpnAdvtStatsGroup,
       "mvpnMrouteGroup": mvpnMrouteGroup,
       "mvpnMrouteNextHopGroup": mvpnMrouteNextHopGroup,
       "mvpnNotificationGroup": mvpnNotificationGroup,
       "mvpnCompliances": mvpnCompliances,
       "mvpnModuleFullCompliance": mvpnModuleFullCompliance,
       "mvpnModuleReadOnlyCompliance": mvpnModuleReadOnlyCompliance,
       "mvpnModuleAdvtStatsCompliance": mvpnModuleAdvtStatsCompliance}
)
