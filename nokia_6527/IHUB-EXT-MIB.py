# SNMP MIB module (IHUB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/IHUB-EXT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:25 2025
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

(Dot1agCfmMepId,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepId",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(dot3adAggPortEntry,) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortEntry")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(isisSysAdminState,) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "isisSysAdminState")

(MplsTunnelIndex,) = mibBuilder.importSymbols(
    "MPLS-TE-MIB",
    "MplsTunnelIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tBgpPeerNgMaxPrefix,) = mibBuilder.importSymbols(
    "TIMETRA-BGP-MIB",
    "tBgpPeerNgMaxPrefix")

(TFilterID,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterID")

(tmnxDot1agCfmSapMipEntry,
 tmnxDot1agCfmSdpBindStackEntry,
 tmnxDot1agCfmSdpMipEntry,
 tmnxDot1agCfmStackEntry) = mibBuilder.importSymbols(
    "TIMETRA-IEEE8021-CFM-MIB",
    "tmnxDot1agCfmSapMipEntry",
    "tmnxDot1agCfmSdpBindStackEntry",
    "tmnxDot1agCfmSdpMipEntry",
    "tmnxDot1agCfmStackEntry")

(vRtrIsisOperState,) = mibBuilder.importSymbols(
    "TIMETRA-ISIS-MIB",
    "vRtrIsisOperState")

(tLagConfigEntry,
 tLagIndex) = mibBuilder.importSymbols(
    "TIMETRA-LAG-MIB",
    "tLagConfigEntry",
    "tLagIndex")

(tMirrorSourceIndex,) = mibBuilder.importSymbols(
    "TIMETRA-MIRROR-MIB",
    "tMirrorSourceIndex")

(tmnxNtpServersEntry,) = mibBuilder.importSymbols(
    "TIMETRA-NTP-MIB",
    "tmnxNtpServersEntry")

(tmnxOspfAdminState,
 tmnxOspfExtLsdbLimit,
 tmnxOspfRouterId) = mibBuilder.importSymbols(
    "TIMETRA-OSPF-NG-MIB",
    "tmnxOspfAdminState",
    "tmnxOspfExtLsdbLimit",
    "tmnxOspfRouterId")

(tmnxPortEtherEntry,
 tmnxPortNotifyPortId,
 tmnxPortPortID) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortEtherEntry",
    "tmnxPortNotifyPortId",
    "tmnxPortPortID")

(sapBaseInfoEntry,
 sapBaseStatsEntry,
 sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapBaseInfoEntry",
    "sapBaseStatsEntry",
    "sapEncapValue",
    "sapPortId")

(tCpmIpFilterEntry,) = mibBuilder.importSymbols(
    "TIMETRA-SECURITY-MIB",
    "tCpmIpFilterEntry")

(iesIfEntry,
 svcBaseInfoEntry,
 svcId,
 svcTlsInfoEntry,
 svcVplsVlanId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "iesIfEntry",
    "svcBaseInfoEntry",
    "svcId",
    "svcTlsInfoEntry",
    "svcVplsVlanId")

(SdpBindId,
 TCIRRate,
 TNamedItem,
 TNetworkPolicyID,
 TPIRRate,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxManagedRouteStatus,
 TmnxPortID,
 TmnxServId,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "SdpBindId",
    "TCIRRate",
    "TNamedItem",
    "TNetworkPolicyID",
    "TPIRRate",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxManagedRouteStatus",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVRtrMplsLspID")

(vRtrConfEntry,
 vRtrID,
 vRtrIfEntry,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrConfEntry",
    "vRtrID",
    "vRtrIfEntry",
    "vRtrIfIndex")


# MODULE-IDENTITY

ihubExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85)
)
if mibBuilder.loadTexts:
    ihubExtMIB.setRevisions(
        ("2014-03-05 00:00",
         "2014-01-27 00:00",
         "2013-12-12 00:00",
         "2013-08-19 00:00",
         "2013-06-16 00:00",
         "2013-05-08 00:00",
         "2013-04-10 00:00",
         "2013-03-25 00:00",
         "2013-03-18 00:00",
         "2013-02-26 00:00",
         "2013-01-25 00:00",
         "2012-07-11 00:00",
         "2012-05-26 00:00",
         "2012-05-22 00:00",
         "2012-02-03 00:00",
         "2012-02-03 00:00",
         "2011-11-16 00:00",
         "2011-11-13 00:00",
         "2011-08-30 00:00",
         "2011-05-12 00:00",
         "2011-05-10 00:00",
         "2011-04-29 00:00",
         "2011-04-26 00:00",
         "2011-04-18 00:00",
         "2011-02-02 00:00",
         "2010-12-17 00:00",
         "2011-01-03 00:00",
         "2011-04-14 00:00",
         "2010-10-07 00:00",
         "2010-05-17 00:00",
         "2010-03-05 00:00",
         "2010-03-01 00:00",
         "2010-02-19 00:00",
         "2009-07-09 00:00",
         "2009-05-26 00:00",
         "2009-05-07 00:00",
         "2009-03-05 00:00",
         "2009-02-18 00:00",
         "2009-02-05 00:00",
         "2009-01-14 00:00",
         "2009-01-11 00:00",
         "2008-12-18 00:00",
         "2008-11-27 00:00",
         "2008-11-07 00:00",
         "2008-10-08 00:00",
         "2008-09-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IhubRateLimitBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 262144),
    )



class THundredthsOfPercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )



class TLossRatioHundrethsOfPercent(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
        ValueRangeConstraint(65535, 65535),
    )



class EthCfmY1731PMType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("ethCfmTWSlm", 1),
          ("ethCfmSingleEndedLoss", 2),
          ("ethCfmTWDelay", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FadPortExt_ObjectIdentity = ObjectIdentity
fadPortExt = _FadPortExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1)
)
_FadPortExtTable_Object = MibTable
fadPortExtTable = _FadPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1)
)
if mibBuilder.loadTexts:
    fadPortExtTable.setStatus("current")
_FadPortExtEntry_Object = MibTableRow
fadPortExtEntry = _FadPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fadPortExtEntry.setStatus("current")


class _FadPortExtType_Type(Integer32):
    """Custom type fadPortExtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("residential", 1),
          ("regular", 2))
    )


_FadPortExtType_Type.__name__ = "Integer32"
_FadPortExtType_Object = MibTableColumn
fadPortExtType = _FadPortExtType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 1),
    _FadPortExtType_Type()
)
fadPortExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtType.setStatus("current")


class _FadPortExtBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type fadPortExtBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_FadPortExtBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_FadPortExtBurstSize_Object = MibTableColumn
fadPortExtBurstSize = _FadPortExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 2),
    _FadPortExtBurstSize_Type()
)
fadPortExtBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtBurstSize.setStatus("current")


class _FadPortExtEgressRate_Type(Integer32):
    """Custom type fadPortExtEgressRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_FadPortExtEgressRate_Type.__name__ = "Integer32"
_FadPortExtEgressRate_Object = MibTableColumn
fadPortExtEgressRate = _FadPortExtEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 3),
    _FadPortExtEgressRate_Type()
)
fadPortExtEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtEgressRate.setStatus("current")


class _FadPortExtLoopbackMode_Type(Integer32):
    """Custom type fadPortExtLoopbackMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tunnel", 1))
    )


_FadPortExtLoopbackMode_Type.__name__ = "Integer32"
_FadPortExtLoopbackMode_Object = MibTableColumn
fadPortExtLoopbackMode = _FadPortExtLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 4),
    _FadPortExtLoopbackMode_Type()
)
fadPortExtLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtLoopbackMode.setStatus("current")


class _FadPortExtLoopbackVlan_Type(Integer32):
    """Custom type fadPortExtLoopbackVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_FadPortExtLoopbackVlan_Type.__name__ = "Integer32"
_FadPortExtLoopbackVlan_Object = MibTableColumn
fadPortExtLoopbackVlan = _FadPortExtLoopbackVlan_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 5),
    _FadPortExtLoopbackVlan_Type()
)
fadPortExtLoopbackVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtLoopbackVlan.setStatus("current")


class _FadPortExtQosRemarkConfig_Type(Integer32):
    """Custom type fadPortExtQosRemarkConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_FadPortExtQosRemarkConfig_Type.__name__ = "Integer32"
_FadPortExtQosRemarkConfig_Object = MibTableColumn
fadPortExtQosRemarkConfig = _FadPortExtQosRemarkConfig_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 6),
    _FadPortExtQosRemarkConfig_Type()
)
fadPortExtQosRemarkConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtQosRemarkConfig.setStatus("current")
_FadPortStateChangeCount_Type = Counter32
_FadPortStateChangeCount_Object = MibTableColumn
fadPortStateChangeCount = _FadPortStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 7),
    _FadPortStateChangeCount_Type()
)
fadPortStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortStateChangeCount.setStatus("current")


class _FadPortExtUseVlanDot1qEtype_Type(TruthValue):
    """Custom type fadPortExtUseVlanDot1qEtype based on TruthValue"""
    defaultValue = 2


_FadPortExtUseVlanDot1qEtype_Type.__name__ = "TruthValue"
_FadPortExtUseVlanDot1qEtype_Object = MibTableColumn
fadPortExtUseVlanDot1qEtype = _FadPortExtUseVlanDot1qEtype_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 8),
    _FadPortExtUseVlanDot1qEtype_Type()
)
fadPortExtUseVlanDot1qEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtUseVlanDot1qEtype.setStatus("current")


class _FadPortExtUsedOutputBwThreshold_Type(THundredthsOfPercent):
    """Custom type fadPortExtUsedOutputBwThreshold based on THundredthsOfPercent"""
    defaultValue = 10000


_FadPortExtUsedOutputBwThreshold_Type.__name__ = "THundredthsOfPercent"
_FadPortExtUsedOutputBwThreshold_Object = MibTableColumn
fadPortExtUsedOutputBwThreshold = _FadPortExtUsedOutputBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 9),
    _FadPortExtUsedOutputBwThreshold_Type()
)
fadPortExtUsedOutputBwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtUsedOutputBwThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtUsedOutputBwThreshold.setUnits("Hundredths of a percent")


class _FadPortExtUsedInputBwThreshold_Type(THundredthsOfPercent):
    """Custom type fadPortExtUsedInputBwThreshold based on THundredthsOfPercent"""
    defaultValue = 10000


_FadPortExtUsedInputBwThreshold_Type.__name__ = "THundredthsOfPercent"
_FadPortExtUsedInputBwThreshold_Object = MibTableColumn
fadPortExtUsedInputBwThreshold = _FadPortExtUsedInputBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 10),
    _FadPortExtUsedInputBwThreshold_Type()
)
fadPortExtUsedInputBwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtUsedInputBwThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtUsedInputBwThreshold.setUnits("Hundredths of a percent")


class _FadPortExtRxCRCAlignErrorsThreshold_Type(THundredthsOfPercent):
    """Custom type fadPortExtRxCRCAlignErrorsThreshold based on THundredthsOfPercent"""
    defaultValue = 10000


_FadPortExtRxCRCAlignErrorsThreshold_Type.__name__ = "THundredthsOfPercent"
_FadPortExtRxCRCAlignErrorsThreshold_Object = MibTableColumn
fadPortExtRxCRCAlignErrorsThreshold = _FadPortExtRxCRCAlignErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 11),
    _FadPortExtRxCRCAlignErrorsThreshold_Type()
)
fadPortExtRxCRCAlignErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtRxCRCAlignErrorsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtRxCRCAlignErrorsThreshold.setUnits("Hundredths of a percent")


class _FadPortExtTxCRCAlignErrorsThreshold_Type(THundredthsOfPercent):
    """Custom type fadPortExtTxCRCAlignErrorsThreshold based on THundredthsOfPercent"""
    defaultValue = 10000


_FadPortExtTxCRCAlignErrorsThreshold_Type.__name__ = "THundredthsOfPercent"
_FadPortExtTxCRCAlignErrorsThreshold_Object = MibTableColumn
fadPortExtTxCRCAlignErrorsThreshold = _FadPortExtTxCRCAlignErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 12),
    _FadPortExtTxCRCAlignErrorsThreshold_Type()
)
fadPortExtTxCRCAlignErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtTxCRCAlignErrorsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtTxCRCAlignErrorsThreshold.setUnits("Hundredths of a percent")


class _FadPortExtTxCollisionsThreshold_Type(THundredthsOfPercent):
    """Custom type fadPortExtTxCollisionsThreshold based on THundredthsOfPercent"""
    defaultValue = 10000


_FadPortExtTxCollisionsThreshold_Type.__name__ = "THundredthsOfPercent"
_FadPortExtTxCollisionsThreshold_Object = MibTableColumn
fadPortExtTxCollisionsThreshold = _FadPortExtTxCollisionsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 13),
    _FadPortExtTxCollisionsThreshold_Type()
)
fadPortExtTxCollisionsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtTxCollisionsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtTxCollisionsThreshold.setUnits("Hundredths of a percent")


class _FadPortExtTcaInterval_Type(Integer32):
    """Custom type fadPortExtTcaInterval based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FadPortExtTcaInterval_Type.__name__ = "Integer32"
_FadPortExtTcaInterval_Object = MibTableColumn
fadPortExtTcaInterval = _FadPortExtTcaInterval_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 14),
    _FadPortExtTcaInterval_Type()
)
fadPortExtTcaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtTcaInterval.setStatus("current")


class _FadPortExtSuppressLinkStateAlarm_Type(Integer32):
    """Custom type fadPortExtSuppressLinkStateAlarm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FadPortExtSuppressLinkStateAlarm_Type.__name__ = "Integer32"
_FadPortExtSuppressLinkStateAlarm_Object = MibTableColumn
fadPortExtSuppressLinkStateAlarm = _FadPortExtSuppressLinkStateAlarm_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 1, 1, 15),
    _FadPortExtSuppressLinkStateAlarm_Type()
)
fadPortExtSuppressLinkStateAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadPortExtSuppressLinkStateAlarm.setStatus("current")
_FadPortExtNotifications_ObjectIdentity = ObjectIdentity
fadPortExtNotifications = _FadPortExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 2)
)
_FadPortExtStatistics_ObjectIdentity = ObjectIdentity
fadPortExtStatistics = _FadPortExtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3)
)
_FadPortExtStatsTable_Object = MibTable
fadPortExtStatsTable = _FadPortExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fadPortExtStatsTable.setStatus("current")
_FadPortExtStatsEntry_Object = MibTableRow
fadPortExtStatsEntry = _FadPortExtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fadPortExtStatsEntry.setStatus("current")
_FadPortExtStatsRxPkts64Octets_Type = Counter64
_FadPortExtStatsRxPkts64Octets_Object = MibTableColumn
fadPortExtStatsRxPkts64Octets = _FadPortExtStatsRxPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 1),
    _FadPortExtStatsRxPkts64Octets_Type()
)
fadPortExtStatsRxPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts64Octets.setUnits("Packets")
_FadPortExtStatsTxPkts64Octets_Type = Counter64
_FadPortExtStatsTxPkts64Octets_Object = MibTableColumn
fadPortExtStatsTxPkts64Octets = _FadPortExtStatsTxPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 2),
    _FadPortExtStatsTxPkts64Octets_Type()
)
fadPortExtStatsTxPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts64Octets.setUnits("Packets")
_FadPortExtStatsRxPkts65to127Octets_Type = Counter64
_FadPortExtStatsRxPkts65to127Octets_Object = MibTableColumn
fadPortExtStatsRxPkts65to127Octets = _FadPortExtStatsRxPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 3),
    _FadPortExtStatsRxPkts65to127Octets_Type()
)
fadPortExtStatsRxPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts65to127Octets.setUnits("Packets")
_FadPortExtStatsTxPkts65to127Octets_Type = Counter64
_FadPortExtStatsTxPkts65to127Octets_Object = MibTableColumn
fadPortExtStatsTxPkts65to127Octets = _FadPortExtStatsTxPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 4),
    _FadPortExtStatsTxPkts65to127Octets_Type()
)
fadPortExtStatsTxPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts65to127Octets.setUnits("Packets")
_FadPortExtStatsRxPkts128to255Octets_Type = Counter64
_FadPortExtStatsRxPkts128to255Octets_Object = MibTableColumn
fadPortExtStatsRxPkts128to255Octets = _FadPortExtStatsRxPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 5),
    _FadPortExtStatsRxPkts128to255Octets_Type()
)
fadPortExtStatsRxPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts128to255Octets.setUnits("Packets")
_FadPortExtStatsTxPkts128to255Octets_Type = Counter64
_FadPortExtStatsTxPkts128to255Octets_Object = MibTableColumn
fadPortExtStatsTxPkts128to255Octets = _FadPortExtStatsTxPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 6),
    _FadPortExtStatsTxPkts128to255Octets_Type()
)
fadPortExtStatsTxPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts128to255Octets.setUnits("Packets")
_FadPortExtStatsRxPkts256to511Octets_Type = Counter64
_FadPortExtStatsRxPkts256to511Octets_Object = MibTableColumn
fadPortExtStatsRxPkts256to511Octets = _FadPortExtStatsRxPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 7),
    _FadPortExtStatsRxPkts256to511Octets_Type()
)
fadPortExtStatsRxPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts256to511Octets.setUnits("Packets")
_FadPortExtStatsTxPkts256to511Octets_Type = Counter64
_FadPortExtStatsTxPkts256to511Octets_Object = MibTableColumn
fadPortExtStatsTxPkts256to511Octets = _FadPortExtStatsTxPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 8),
    _FadPortExtStatsTxPkts256to511Octets_Type()
)
fadPortExtStatsTxPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts256to511Octets.setUnits("Packets")
_FadPortExtStatsRxPkts512to1023Octets_Type = Counter64
_FadPortExtStatsRxPkts512to1023Octets_Object = MibTableColumn
fadPortExtStatsRxPkts512to1023Octets = _FadPortExtStatsRxPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 9),
    _FadPortExtStatsRxPkts512to1023Octets_Type()
)
fadPortExtStatsRxPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts512to1023Octets.setUnits("Packets")
_FadPortExtStatsTxPkts512to1023Octets_Type = Counter64
_FadPortExtStatsTxPkts512to1023Octets_Object = MibTableColumn
fadPortExtStatsTxPkts512to1023Octets = _FadPortExtStatsTxPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 10),
    _FadPortExtStatsTxPkts512to1023Octets_Type()
)
fadPortExtStatsTxPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts512to1023Octets.setUnits("Packets")
_FadPortExtStatsRxPkts1024to1518Octets_Type = Counter64
_FadPortExtStatsRxPkts1024to1518Octets_Object = MibTableColumn
fadPortExtStatsRxPkts1024to1518Octets = _FadPortExtStatsRxPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 11),
    _FadPortExtStatsRxPkts1024to1518Octets_Type()
)
fadPortExtStatsRxPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxPkts1024to1518Octets.setUnits("Packets")
_FadPortExtStatsTxPkts1024to1518Octets_Type = Counter64
_FadPortExtStatsTxPkts1024to1518Octets_Object = MibTableColumn
fadPortExtStatsTxPkts1024to1518Octets = _FadPortExtStatsTxPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 12),
    _FadPortExtStatsTxPkts1024to1518Octets_Type()
)
fadPortExtStatsTxPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxPkts1024to1518Octets.setUnits("Packets")
_FadPortExtStatsRxOversizePkts_Type = Counter64
_FadPortExtStatsRxOversizePkts_Object = MibTableColumn
fadPortExtStatsRxOversizePkts = _FadPortExtStatsRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 13),
    _FadPortExtStatsRxOversizePkts_Type()
)
fadPortExtStatsRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxOversizePkts.setUnits("Packets")
_FadPortExtStatsTxOversizePkts_Type = Counter64
_FadPortExtStatsTxOversizePkts_Object = MibTableColumn
fadPortExtStatsTxOversizePkts = _FadPortExtStatsTxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 14),
    _FadPortExtStatsTxOversizePkts_Type()
)
fadPortExtStatsTxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxOversizePkts.setUnits("Packets")
_FadPortExtStatsRxFragments_Type = Counter64
_FadPortExtStatsRxFragments_Object = MibTableColumn
fadPortExtStatsRxFragments = _FadPortExtStatsRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 15),
    _FadPortExtStatsRxFragments_Type()
)
fadPortExtStatsRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxFragments.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxFragments.setUnits("Packets")
_FadPortExtStatsTxFragments_Type = Counter64
_FadPortExtStatsTxFragments_Object = MibTableColumn
fadPortExtStatsTxFragments = _FadPortExtStatsTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 16),
    _FadPortExtStatsTxFragments_Type()
)
fadPortExtStatsTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxFragments.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxFragments.setUnits("Packets")
_FadPortExtStatsRxJabbers_Type = Counter64
_FadPortExtStatsRxJabbers_Object = MibTableColumn
fadPortExtStatsRxJabbers = _FadPortExtStatsRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 17),
    _FadPortExtStatsRxJabbers_Type()
)
fadPortExtStatsRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxJabbers.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxJabbers.setUnits("Packets")
_FadPortExtStatsTxJabbers_Type = Counter64
_FadPortExtStatsTxJabbers_Object = MibTableColumn
fadPortExtStatsTxJabbers = _FadPortExtStatsTxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 18),
    _FadPortExtStatsTxJabbers_Type()
)
fadPortExtStatsTxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxJabbers.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxJabbers.setUnits("Packets")
_FadPortExtStatsRxUndersizePkts_Type = Counter64
_FadPortExtStatsRxUndersizePkts_Object = MibTableColumn
fadPortExtStatsRxUndersizePkts = _FadPortExtStatsRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 19),
    _FadPortExtStatsRxUndersizePkts_Type()
)
fadPortExtStatsRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxUndersizePkts.setUnits("Packets")
_FadPortExtStatsTxUndersizePkts_Type = Counter64
_FadPortExtStatsTxUndersizePkts_Object = MibTableColumn
fadPortExtStatsTxUndersizePkts = _FadPortExtStatsTxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 20),
    _FadPortExtStatsTxUndersizePkts_Type()
)
fadPortExtStatsTxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxUndersizePkts.setUnits("Packets")
_FadPortExtStatsRxDropEvents_Type = Counter64
_FadPortExtStatsRxDropEvents_Object = MibTableColumn
fadPortExtStatsRxDropEvents = _FadPortExtStatsRxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 21),
    _FadPortExtStatsRxDropEvents_Type()
)
fadPortExtStatsRxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxDropEvents.setStatus("current")
_FadPortExtStatsTxDropEvents_Type = Counter64
_FadPortExtStatsTxDropEvents_Object = MibTableColumn
fadPortExtStatsTxDropEvents = _FadPortExtStatsTxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 22),
    _FadPortExtStatsTxDropEvents_Type()
)
fadPortExtStatsTxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxDropEvents.setStatus("current")
_FadPortExtStatsRxCRCAlignErrors_Type = Counter64
_FadPortExtStatsRxCRCAlignErrors_Object = MibTableColumn
fadPortExtStatsRxCRCAlignErrors = _FadPortExtStatsRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 23),
    _FadPortExtStatsRxCRCAlignErrors_Type()
)
fadPortExtStatsRxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsRxCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsRxCRCAlignErrors.setUnits("Packets")
_FadPortExtStatsTxCRCAlignErrors_Type = Counter64
_FadPortExtStatsTxCRCAlignErrors_Object = MibTableColumn
fadPortExtStatsTxCRCAlignErrors = _FadPortExtStatsTxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 3, 1, 1, 24),
    _FadPortExtStatsTxCRCAlignErrors_Type()
)
fadPortExtStatsTxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtStatsTxCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    fadPortExtStatsTxCRCAlignErrors.setUnits("Packets")
_FadPortExtPMStatistics_ObjectIdentity = ObjectIdentity
fadPortExtPMStatistics = _FadPortExtPMStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4)
)
_FadPortExtPMCurrent15MinIntervalTable_Object = MibTable
fadPortExtPMCurrent15MinIntervalTable = _FadPortExtPMCurrent15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinIntervalTable.setStatus("current")
_FadPortExtPMCurrent15MinIntervalEntry_Object = MibTableRow
fadPortExtPMCurrent15MinIntervalEntry = _FadPortExtPMCurrent15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1)
)
fadPortExtPMCurrent15MinIntervalEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinIntervalEntry.setStatus("current")


class _FadPortExtPMCurrent15MinTimeElapsed_Type(Integer32):
    """Custom type fadPortExtPMCurrent15MinTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadPortExtPMCurrent15MinTimeElapsed_Type.__name__ = "Integer32"
_FadPortExtPMCurrent15MinTimeElapsed_Object = MibTableColumn
fadPortExtPMCurrent15MinTimeElapsed = _FadPortExtPMCurrent15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 1),
    _FadPortExtPMCurrent15MinTimeElapsed_Type()
)
fadPortExtPMCurrent15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinTimeElapsed.setStatus("current")


class _FadPortExtPMCurrent15MinTimeMeasured_Type(Integer32):
    """Custom type fadPortExtPMCurrent15MinTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadPortExtPMCurrent15MinTimeMeasured_Type.__name__ = "Integer32"
_FadPortExtPMCurrent15MinTimeMeasured_Object = MibTableColumn
fadPortExtPMCurrent15MinTimeMeasured = _FadPortExtPMCurrent15MinTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 2),
    _FadPortExtPMCurrent15MinTimeMeasured_Type()
)
fadPortExtPMCurrent15MinTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinTimeMeasured.setStatus("current")
_FadPortExtPMCurrent15MinInPackets_Type = Counter64
_FadPortExtPMCurrent15MinInPackets_Object = MibTableColumn
fadPortExtPMCurrent15MinInPackets = _FadPortExtPMCurrent15MinInPackets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 3),
    _FadPortExtPMCurrent15MinInPackets_Type()
)
fadPortExtPMCurrent15MinInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinInPackets.setStatus("current")
_FadPortExtPMCurrent15MinInOctets_Type = Counter64
_FadPortExtPMCurrent15MinInOctets_Object = MibTableColumn
fadPortExtPMCurrent15MinInOctets = _FadPortExtPMCurrent15MinInOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 4),
    _FadPortExtPMCurrent15MinInOctets_Type()
)
fadPortExtPMCurrent15MinInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinInOctets.setStatus("current")
_FadPortExtPMCurrent15MinInErrors_Type = Counter64
_FadPortExtPMCurrent15MinInErrors_Object = MibTableColumn
fadPortExtPMCurrent15MinInErrors = _FadPortExtPMCurrent15MinInErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 5),
    _FadPortExtPMCurrent15MinInErrors_Type()
)
fadPortExtPMCurrent15MinInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinInErrors.setStatus("current")
_FadPortExtPMCurrent15MinInPacketDrops_Type = Counter64
_FadPortExtPMCurrent15MinInPacketDrops_Object = MibTableColumn
fadPortExtPMCurrent15MinInPacketDrops = _FadPortExtPMCurrent15MinInPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 6),
    _FadPortExtPMCurrent15MinInPacketDrops_Type()
)
fadPortExtPMCurrent15MinInPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinInPacketDrops.setStatus("current")
_FadPortExtPMCurrent15MinInDiscards_Type = Counter64
_FadPortExtPMCurrent15MinInDiscards_Object = MibTableColumn
fadPortExtPMCurrent15MinInDiscards = _FadPortExtPMCurrent15MinInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 7),
    _FadPortExtPMCurrent15MinInDiscards_Type()
)
fadPortExtPMCurrent15MinInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinInDiscards.setStatus("current")
_FadPortExtPMCurrent15MinOutPackets_Type = Counter64
_FadPortExtPMCurrent15MinOutPackets_Object = MibTableColumn
fadPortExtPMCurrent15MinOutPackets = _FadPortExtPMCurrent15MinOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 8),
    _FadPortExtPMCurrent15MinOutPackets_Type()
)
fadPortExtPMCurrent15MinOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinOutPackets.setStatus("current")
_FadPortExtPMCurrent15MinOutOctets_Type = Counter64
_FadPortExtPMCurrent15MinOutOctets_Object = MibTableColumn
fadPortExtPMCurrent15MinOutOctets = _FadPortExtPMCurrent15MinOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 9),
    _FadPortExtPMCurrent15MinOutOctets_Type()
)
fadPortExtPMCurrent15MinOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinOutOctets.setStatus("current")
_FadPortExtPMCurrent15MinOutErrors_Type = Counter64
_FadPortExtPMCurrent15MinOutErrors_Object = MibTableColumn
fadPortExtPMCurrent15MinOutErrors = _FadPortExtPMCurrent15MinOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 10),
    _FadPortExtPMCurrent15MinOutErrors_Type()
)
fadPortExtPMCurrent15MinOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinOutErrors.setStatus("current")
_FadPortExtPMCurrent15MinOutPacketDrops_Type = Counter64
_FadPortExtPMCurrent15MinOutPacketDrops_Object = MibTableColumn
fadPortExtPMCurrent15MinOutPacketDrops = _FadPortExtPMCurrent15MinOutPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 11),
    _FadPortExtPMCurrent15MinOutPacketDrops_Type()
)
fadPortExtPMCurrent15MinOutPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinOutPacketDrops.setStatus("current")
_FadPortExtPMCurrent15MinOutDiscards_Type = Counter64
_FadPortExtPMCurrent15MinOutDiscards_Object = MibTableColumn
fadPortExtPMCurrent15MinOutDiscards = _FadPortExtPMCurrent15MinOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 12),
    _FadPortExtPMCurrent15MinOutDiscards_Type()
)
fadPortExtPMCurrent15MinOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinOutDiscards.setStatus("current")


class _FadPortExtPM15MinValidIntervals_Type(Integer32):
    """Custom type fadPortExtPM15MinValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_FadPortExtPM15MinValidIntervals_Type.__name__ = "Integer32"
_FadPortExtPM15MinValidIntervals_Object = MibTableColumn
fadPortExtPM15MinValidIntervals = _FadPortExtPM15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 13),
    _FadPortExtPM15MinValidIntervals_Type()
)
fadPortExtPM15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPM15MinValidIntervals.setStatus("current")
_FadPortExtPMCurrent15MinInvalidDataFlag_Type = TruthValue
_FadPortExtPMCurrent15MinInvalidDataFlag_Object = MibTableColumn
fadPortExtPMCurrent15MinInvalidDataFlag = _FadPortExtPMCurrent15MinInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 14),
    _FadPortExtPMCurrent15MinInvalidDataFlag_Type()
)
fadPortExtPMCurrent15MinInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinInvalidDataFlag.setStatus("current")
_FadPortExtPMCurrent15MinOutputBw_Type = Counter64
_FadPortExtPMCurrent15MinOutputBw_Object = MibTableColumn
fadPortExtPMCurrent15MinOutputBw = _FadPortExtPMCurrent15MinOutputBw_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 15),
    _FadPortExtPMCurrent15MinOutputBw_Type()
)
fadPortExtPMCurrent15MinOutputBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinOutputBw.setStatus("current")
_FadPortExtPMCurrent15MinInputBw_Type = Counter64
_FadPortExtPMCurrent15MinInputBw_Object = MibTableColumn
fadPortExtPMCurrent15MinInputBw = _FadPortExtPMCurrent15MinInputBw_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 16),
    _FadPortExtPMCurrent15MinInputBw_Type()
)
fadPortExtPMCurrent15MinInputBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinInputBw.setStatus("current")
_FadPortExtPMCurrent15MinRxCRCAlignErrors_Type = Counter64
_FadPortExtPMCurrent15MinRxCRCAlignErrors_Object = MibTableColumn
fadPortExtPMCurrent15MinRxCRCAlignErrors = _FadPortExtPMCurrent15MinRxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 17),
    _FadPortExtPMCurrent15MinRxCRCAlignErrors_Type()
)
fadPortExtPMCurrent15MinRxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinRxCRCAlignErrors.setStatus("current")
_FadPortExtPMCurrent15MinTxCRCAlignErrors_Type = Counter64
_FadPortExtPMCurrent15MinTxCRCAlignErrors_Object = MibTableColumn
fadPortExtPMCurrent15MinTxCRCAlignErrors = _FadPortExtPMCurrent15MinTxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 18),
    _FadPortExtPMCurrent15MinTxCRCAlignErrors_Type()
)
fadPortExtPMCurrent15MinTxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinTxCRCAlignErrors.setStatus("current")
_FadPortExtPMCurrent15MinTxCollisions_Type = Counter64
_FadPortExtPMCurrent15MinTxCollisions_Object = MibTableColumn
fadPortExtPMCurrent15MinTxCollisions = _FadPortExtPMCurrent15MinTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 1, 1, 19),
    _FadPortExtPMCurrent15MinTxCollisions_Type()
)
fadPortExtPMCurrent15MinTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent15MinTxCollisions.setStatus("current")
_FadPortExtPMCurrent1DayIntervalTable_Object = MibTable
fadPortExtPMCurrent1DayIntervalTable = _FadPortExtPMCurrent1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayIntervalTable.setStatus("current")
_FadPortExtPMCurrent1DayIntervalEntry_Object = MibTableRow
fadPortExtPMCurrent1DayIntervalEntry = _FadPortExtPMCurrent1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1)
)
fadPortExtPMCurrent1DayIntervalEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayIntervalEntry.setStatus("current")


class _FadPortExtPMCurrent1DayTimeElapsed_Type(Integer32):
    """Custom type fadPortExtPMCurrent1DayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadPortExtPMCurrent1DayTimeElapsed_Type.__name__ = "Integer32"
_FadPortExtPMCurrent1DayTimeElapsed_Object = MibTableColumn
fadPortExtPMCurrent1DayTimeElapsed = _FadPortExtPMCurrent1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 1),
    _FadPortExtPMCurrent1DayTimeElapsed_Type()
)
fadPortExtPMCurrent1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayTimeElapsed.setStatus("current")


class _FadPortExtPMCurrent1DayTimeMeasured_Type(Integer32):
    """Custom type fadPortExtPMCurrent1DayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadPortExtPMCurrent1DayTimeMeasured_Type.__name__ = "Integer32"
_FadPortExtPMCurrent1DayTimeMeasured_Object = MibTableColumn
fadPortExtPMCurrent1DayTimeMeasured = _FadPortExtPMCurrent1DayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 2),
    _FadPortExtPMCurrent1DayTimeMeasured_Type()
)
fadPortExtPMCurrent1DayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayTimeMeasured.setStatus("current")
_FadPortExtPMCurrent1DayInPackets_Type = Counter64
_FadPortExtPMCurrent1DayInPackets_Object = MibTableColumn
fadPortExtPMCurrent1DayInPackets = _FadPortExtPMCurrent1DayInPackets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 3),
    _FadPortExtPMCurrent1DayInPackets_Type()
)
fadPortExtPMCurrent1DayInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayInPackets.setStatus("current")
_FadPortExtPMCurrent1DayInOctets_Type = Counter64
_FadPortExtPMCurrent1DayInOctets_Object = MibTableColumn
fadPortExtPMCurrent1DayInOctets = _FadPortExtPMCurrent1DayInOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 4),
    _FadPortExtPMCurrent1DayInOctets_Type()
)
fadPortExtPMCurrent1DayInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayInOctets.setStatus("current")
_FadPortExtPMCurrent1DayInErrors_Type = Counter64
_FadPortExtPMCurrent1DayInErrors_Object = MibTableColumn
fadPortExtPMCurrent1DayInErrors = _FadPortExtPMCurrent1DayInErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 5),
    _FadPortExtPMCurrent1DayInErrors_Type()
)
fadPortExtPMCurrent1DayInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayInErrors.setStatus("current")
_FadPortExtPMCurrent1DayInPacketDrops_Type = Counter64
_FadPortExtPMCurrent1DayInPacketDrops_Object = MibTableColumn
fadPortExtPMCurrent1DayInPacketDrops = _FadPortExtPMCurrent1DayInPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 6),
    _FadPortExtPMCurrent1DayInPacketDrops_Type()
)
fadPortExtPMCurrent1DayInPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayInPacketDrops.setStatus("current")
_FadPortExtPMCurrent1DayInDiscards_Type = Counter64
_FadPortExtPMCurrent1DayInDiscards_Object = MibTableColumn
fadPortExtPMCurrent1DayInDiscards = _FadPortExtPMCurrent1DayInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 7),
    _FadPortExtPMCurrent1DayInDiscards_Type()
)
fadPortExtPMCurrent1DayInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayInDiscards.setStatus("current")
_FadPortExtPMCurrent1DayOutPackets_Type = Counter64
_FadPortExtPMCurrent1DayOutPackets_Object = MibTableColumn
fadPortExtPMCurrent1DayOutPackets = _FadPortExtPMCurrent1DayOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 8),
    _FadPortExtPMCurrent1DayOutPackets_Type()
)
fadPortExtPMCurrent1DayOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayOutPackets.setStatus("current")
_FadPortExtPMCurrent1DayOutOctets_Type = Counter64
_FadPortExtPMCurrent1DayOutOctets_Object = MibTableColumn
fadPortExtPMCurrent1DayOutOctets = _FadPortExtPMCurrent1DayOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 9),
    _FadPortExtPMCurrent1DayOutOctets_Type()
)
fadPortExtPMCurrent1DayOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayOutOctets.setStatus("current")
_FadPortExtPMCurrent1DayOutErrors_Type = Counter64
_FadPortExtPMCurrent1DayOutErrors_Object = MibTableColumn
fadPortExtPMCurrent1DayOutErrors = _FadPortExtPMCurrent1DayOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 10),
    _FadPortExtPMCurrent1DayOutErrors_Type()
)
fadPortExtPMCurrent1DayOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayOutErrors.setStatus("current")
_FadPortExtPMCurrent1DayOutPacketDrops_Type = Counter64
_FadPortExtPMCurrent1DayOutPacketDrops_Object = MibTableColumn
fadPortExtPMCurrent1DayOutPacketDrops = _FadPortExtPMCurrent1DayOutPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 11),
    _FadPortExtPMCurrent1DayOutPacketDrops_Type()
)
fadPortExtPMCurrent1DayOutPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayOutPacketDrops.setStatus("current")
_FadPortExtPMCurrent1DayOutDiscards_Type = Counter64
_FadPortExtPMCurrent1DayOutDiscards_Object = MibTableColumn
fadPortExtPMCurrent1DayOutDiscards = _FadPortExtPMCurrent1DayOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 12),
    _FadPortExtPMCurrent1DayOutDiscards_Type()
)
fadPortExtPMCurrent1DayOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayOutDiscards.setStatus("current")


class _FadPortExtPM1DayValidIntervals_Type(Integer32):
    """Custom type fadPortExtPM1DayValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FadPortExtPM1DayValidIntervals_Type.__name__ = "Integer32"
_FadPortExtPM1DayValidIntervals_Object = MibTableColumn
fadPortExtPM1DayValidIntervals = _FadPortExtPM1DayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 13),
    _FadPortExtPM1DayValidIntervals_Type()
)
fadPortExtPM1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPM1DayValidIntervals.setStatus("current")
_FadPortExtPMCurrent1DayInvalidDataFlag_Type = TruthValue
_FadPortExtPMCurrent1DayInvalidDataFlag_Object = MibTableColumn
fadPortExtPMCurrent1DayInvalidDataFlag = _FadPortExtPMCurrent1DayInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 2, 1, 14),
    _FadPortExtPMCurrent1DayInvalidDataFlag_Type()
)
fadPortExtPMCurrent1DayInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMCurrent1DayInvalidDataFlag.setStatus("current")
_FadPortExtPMPrevious15MinIntervalTable_Object = MibTable
fadPortExtPMPrevious15MinIntervalTable = _FadPortExtPMPrevious15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3)
)
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinIntervalTable.setStatus("current")
_FadPortExtPMPrevious15MinIntervalEntry_Object = MibTableRow
fadPortExtPMPrevious15MinIntervalEntry = _FadPortExtPMPrevious15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1)
)
fadPortExtPMPrevious15MinIntervalEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "IHUB-EXT-MIB", "fadPortExtPMPrevious15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinIntervalEntry.setStatus("current")


class _FadPortExtPMPrevious15MinIntervalNumber_Type(Integer32):
    """Custom type fadPortExtPMPrevious15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_FadPortExtPMPrevious15MinIntervalNumber_Type.__name__ = "Integer32"
_FadPortExtPMPrevious15MinIntervalNumber_Object = MibTableColumn
fadPortExtPMPrevious15MinIntervalNumber = _FadPortExtPMPrevious15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 1),
    _FadPortExtPMPrevious15MinIntervalNumber_Type()
)
fadPortExtPMPrevious15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinIntervalNumber.setStatus("current")


class _FadPortExtPMPrevious15MinTimeMeasured_Type(Integer32):
    """Custom type fadPortExtPMPrevious15MinTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadPortExtPMPrevious15MinTimeMeasured_Type.__name__ = "Integer32"
_FadPortExtPMPrevious15MinTimeMeasured_Object = MibTableColumn
fadPortExtPMPrevious15MinTimeMeasured = _FadPortExtPMPrevious15MinTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 2),
    _FadPortExtPMPrevious15MinTimeMeasured_Type()
)
fadPortExtPMPrevious15MinTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinTimeMeasured.setStatus("current")
_FadPortExtPMPrevious15MinInPackets_Type = Counter64
_FadPortExtPMPrevious15MinInPackets_Object = MibTableColumn
fadPortExtPMPrevious15MinInPackets = _FadPortExtPMPrevious15MinInPackets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 3),
    _FadPortExtPMPrevious15MinInPackets_Type()
)
fadPortExtPMPrevious15MinInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinInPackets.setStatus("current")
_FadPortExtPMPrevious15MinInOctets_Type = Counter64
_FadPortExtPMPrevious15MinInOctets_Object = MibTableColumn
fadPortExtPMPrevious15MinInOctets = _FadPortExtPMPrevious15MinInOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 4),
    _FadPortExtPMPrevious15MinInOctets_Type()
)
fadPortExtPMPrevious15MinInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinInOctets.setStatus("current")
_FadPortExtPMPrevious15MinInErrors_Type = Counter64
_FadPortExtPMPrevious15MinInErrors_Object = MibTableColumn
fadPortExtPMPrevious15MinInErrors = _FadPortExtPMPrevious15MinInErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 5),
    _FadPortExtPMPrevious15MinInErrors_Type()
)
fadPortExtPMPrevious15MinInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinInErrors.setStatus("current")
_FadPortExtPMPrevious15MinInPacketDrops_Type = Counter64
_FadPortExtPMPrevious15MinInPacketDrops_Object = MibTableColumn
fadPortExtPMPrevious15MinInPacketDrops = _FadPortExtPMPrevious15MinInPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 6),
    _FadPortExtPMPrevious15MinInPacketDrops_Type()
)
fadPortExtPMPrevious15MinInPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinInPacketDrops.setStatus("current")
_FadPortExtPMPrevious15MinInDiscards_Type = Counter64
_FadPortExtPMPrevious15MinInDiscards_Object = MibTableColumn
fadPortExtPMPrevious15MinInDiscards = _FadPortExtPMPrevious15MinInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 7),
    _FadPortExtPMPrevious15MinInDiscards_Type()
)
fadPortExtPMPrevious15MinInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinInDiscards.setStatus("current")
_FadPortExtPMPrevious15MinOutPackets_Type = Counter64
_FadPortExtPMPrevious15MinOutPackets_Object = MibTableColumn
fadPortExtPMPrevious15MinOutPackets = _FadPortExtPMPrevious15MinOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 8),
    _FadPortExtPMPrevious15MinOutPackets_Type()
)
fadPortExtPMPrevious15MinOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinOutPackets.setStatus("current")
_FadPortExtPMPrevious15MinOutOctets_Type = Counter64
_FadPortExtPMPrevious15MinOutOctets_Object = MibTableColumn
fadPortExtPMPrevious15MinOutOctets = _FadPortExtPMPrevious15MinOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 9),
    _FadPortExtPMPrevious15MinOutOctets_Type()
)
fadPortExtPMPrevious15MinOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinOutOctets.setStatus("current")
_FadPortExtPMPrevious15MinOutErrors_Type = Counter64
_FadPortExtPMPrevious15MinOutErrors_Object = MibTableColumn
fadPortExtPMPrevious15MinOutErrors = _FadPortExtPMPrevious15MinOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 10),
    _FadPortExtPMPrevious15MinOutErrors_Type()
)
fadPortExtPMPrevious15MinOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinOutErrors.setStatus("current")
_FadPortExtPMPrevious15MinOutPacketDrops_Type = Counter64
_FadPortExtPMPrevious15MinOutPacketDrops_Object = MibTableColumn
fadPortExtPMPrevious15MinOutPacketDrops = _FadPortExtPMPrevious15MinOutPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 11),
    _FadPortExtPMPrevious15MinOutPacketDrops_Type()
)
fadPortExtPMPrevious15MinOutPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinOutPacketDrops.setStatus("current")
_FadPortExtPMPrevious15MinOutDiscards_Type = Counter64
_FadPortExtPMPrevious15MinOutDiscards_Object = MibTableColumn
fadPortExtPMPrevious15MinOutDiscards = _FadPortExtPMPrevious15MinOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 12),
    _FadPortExtPMPrevious15MinOutDiscards_Type()
)
fadPortExtPMPrevious15MinOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinOutDiscards.setStatus("current")
_FadPortExtPMPrevious15MinInvalidDataFlag_Type = TruthValue
_FadPortExtPMPrevious15MinInvalidDataFlag_Object = MibTableColumn
fadPortExtPMPrevious15MinInvalidDataFlag = _FadPortExtPMPrevious15MinInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 3, 1, 13),
    _FadPortExtPMPrevious15MinInvalidDataFlag_Type()
)
fadPortExtPMPrevious15MinInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious15MinInvalidDataFlag.setStatus("current")
_FadPortExtPMPrevious1DayIntervalTable_Object = MibTable
fadPortExtPMPrevious1DayIntervalTable = _FadPortExtPMPrevious1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4)
)
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayIntervalTable.setStatus("current")
_FadPortExtPMPrevious1DayIntervalEntry_Object = MibTableRow
fadPortExtPMPrevious1DayIntervalEntry = _FadPortExtPMPrevious1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1)
)
fadPortExtPMPrevious1DayIntervalEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "IHUB-EXT-MIB", "fadPortExtPMPrevious1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayIntervalEntry.setStatus("current")


class _FadPortExtPMPrevious1DayIntervalNumber_Type(Integer32):
    """Custom type fadPortExtPMPrevious1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FadPortExtPMPrevious1DayIntervalNumber_Type.__name__ = "Integer32"
_FadPortExtPMPrevious1DayIntervalNumber_Object = MibTableColumn
fadPortExtPMPrevious1DayIntervalNumber = _FadPortExtPMPrevious1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 1),
    _FadPortExtPMPrevious1DayIntervalNumber_Type()
)
fadPortExtPMPrevious1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayIntervalNumber.setStatus("current")


class _FadPortExtPMPrevious1DayTimeMeasured_Type(Integer32):
    """Custom type fadPortExtPMPrevious1DayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadPortExtPMPrevious1DayTimeMeasured_Type.__name__ = "Integer32"
_FadPortExtPMPrevious1DayTimeMeasured_Object = MibTableColumn
fadPortExtPMPrevious1DayTimeMeasured = _FadPortExtPMPrevious1DayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 2),
    _FadPortExtPMPrevious1DayTimeMeasured_Type()
)
fadPortExtPMPrevious1DayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayTimeMeasured.setStatus("current")
_FadPortExtPMPrevious1DayInPackets_Type = Counter64
_FadPortExtPMPrevious1DayInPackets_Object = MibTableColumn
fadPortExtPMPrevious1DayInPackets = _FadPortExtPMPrevious1DayInPackets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 3),
    _FadPortExtPMPrevious1DayInPackets_Type()
)
fadPortExtPMPrevious1DayInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayInPackets.setStatus("current")
_FadPortExtPMPrevious1DayInOctets_Type = Counter64
_FadPortExtPMPrevious1DayInOctets_Object = MibTableColumn
fadPortExtPMPrevious1DayInOctets = _FadPortExtPMPrevious1DayInOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 4),
    _FadPortExtPMPrevious1DayInOctets_Type()
)
fadPortExtPMPrevious1DayInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayInOctets.setStatus("current")
_FadPortExtPMPrevious1DayInErrors_Type = Counter64
_FadPortExtPMPrevious1DayInErrors_Object = MibTableColumn
fadPortExtPMPrevious1DayInErrors = _FadPortExtPMPrevious1DayInErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 5),
    _FadPortExtPMPrevious1DayInErrors_Type()
)
fadPortExtPMPrevious1DayInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayInErrors.setStatus("current")
_FadPortExtPMPrevious1DayInPacketDrops_Type = Counter64
_FadPortExtPMPrevious1DayInPacketDrops_Object = MibTableColumn
fadPortExtPMPrevious1DayInPacketDrops = _FadPortExtPMPrevious1DayInPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 6),
    _FadPortExtPMPrevious1DayInPacketDrops_Type()
)
fadPortExtPMPrevious1DayInPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayInPacketDrops.setStatus("current")
_FadPortExtPMPrevious1DayInDiscards_Type = Counter64
_FadPortExtPMPrevious1DayInDiscards_Object = MibTableColumn
fadPortExtPMPrevious1DayInDiscards = _FadPortExtPMPrevious1DayInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 7),
    _FadPortExtPMPrevious1DayInDiscards_Type()
)
fadPortExtPMPrevious1DayInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayInDiscards.setStatus("current")
_FadPortExtPMPrevious1DayOutPackets_Type = Counter64
_FadPortExtPMPrevious1DayOutPackets_Object = MibTableColumn
fadPortExtPMPrevious1DayOutPackets = _FadPortExtPMPrevious1DayOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 8),
    _FadPortExtPMPrevious1DayOutPackets_Type()
)
fadPortExtPMPrevious1DayOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayOutPackets.setStatus("current")
_FadPortExtPMPrevious1DayOutOctets_Type = Counter64
_FadPortExtPMPrevious1DayOutOctets_Object = MibTableColumn
fadPortExtPMPrevious1DayOutOctets = _FadPortExtPMPrevious1DayOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 9),
    _FadPortExtPMPrevious1DayOutOctets_Type()
)
fadPortExtPMPrevious1DayOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayOutOctets.setStatus("current")
_FadPortExtPMPrevious1DayOutErrors_Type = Counter64
_FadPortExtPMPrevious1DayOutErrors_Object = MibTableColumn
fadPortExtPMPrevious1DayOutErrors = _FadPortExtPMPrevious1DayOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 10),
    _FadPortExtPMPrevious1DayOutErrors_Type()
)
fadPortExtPMPrevious1DayOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayOutErrors.setStatus("current")
_FadPortExtPMPrevious1DayOutPacketDrops_Type = Counter64
_FadPortExtPMPrevious1DayOutPacketDrops_Object = MibTableColumn
fadPortExtPMPrevious1DayOutPacketDrops = _FadPortExtPMPrevious1DayOutPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 11),
    _FadPortExtPMPrevious1DayOutPacketDrops_Type()
)
fadPortExtPMPrevious1DayOutPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayOutPacketDrops.setStatus("current")
_FadPortExtPMPrevious1DayOutDiscards_Type = Counter64
_FadPortExtPMPrevious1DayOutDiscards_Object = MibTableColumn
fadPortExtPMPrevious1DayOutDiscards = _FadPortExtPMPrevious1DayOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 12),
    _FadPortExtPMPrevious1DayOutDiscards_Type()
)
fadPortExtPMPrevious1DayOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayOutDiscards.setStatus("current")
_FadPortExtPMPrevious1DayInvalidDataFlag_Type = TruthValue
_FadPortExtPMPrevious1DayInvalidDataFlag_Object = MibTableColumn
fadPortExtPMPrevious1DayInvalidDataFlag = _FadPortExtPMPrevious1DayInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 4, 4, 1, 13),
    _FadPortExtPMPrevious1DayInvalidDataFlag_Type()
)
fadPortExtPMPrevious1DayInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadPortExtPMPrevious1DayInvalidDataFlag.setStatus("current")
_FadSvcBaseExt_ObjectIdentity = ObjectIdentity
fadSvcBaseExt = _FadSvcBaseExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2)
)
_FadSvcBaseExtTable_Object = MibTable
fadSvcBaseExtTable = _FadSvcBaseExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1)
)
if mibBuilder.loadTexts:
    fadSvcBaseExtTable.setStatus("current")
_FadSvcBaseExtEntry_Object = MibTableRow
fadSvcBaseExtEntry = _FadSvcBaseExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fadSvcBaseExtEntry.setStatus("current")


class _FadConfigIngressQosPolicyId_Type(Integer32):
    """Custom type fadConfigIngressQosPolicyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FadConfigIngressQosPolicyId_Type.__name__ = "Integer32"
_FadConfigIngressQosPolicyId_Object = MibTableColumn
fadConfigIngressQosPolicyId = _FadConfigIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 1),
    _FadConfigIngressQosPolicyId_Type()
)
fadConfigIngressQosPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadConfigIngressQosPolicyId.setStatus("current")


class _FadActualIngressQosPolicyId_Type(Integer32):
    """Custom type fadActualIngressQosPolicyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FadActualIngressQosPolicyId_Type.__name__ = "Integer32"
_FadActualIngressQosPolicyId_Object = MibTableColumn
fadActualIngressQosPolicyId = _FadActualIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 2),
    _FadActualIngressQosPolicyId_Type()
)
fadActualIngressQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadActualIngressQosPolicyId.setStatus("current")


class _FadConfigSgtPolicyId_Type(Integer32):
    """Custom type fadConfigSgtPolicyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FadConfigSgtPolicyId_Type.__name__ = "Integer32"
_FadConfigSgtPolicyId_Object = MibTableColumn
fadConfigSgtPolicyId = _FadConfigSgtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 3),
    _FadConfigSgtPolicyId_Type()
)
fadConfigSgtPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadConfigSgtPolicyId.setStatus("current")


class _FadActualSgtPolicyId_Type(Integer32):
    """Custom type fadActualSgtPolicyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FadActualSgtPolicyId_Type.__name__ = "Integer32"
_FadActualSgtPolicyId_Object = MibTableColumn
fadActualSgtPolicyId = _FadActualSgtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 4),
    _FadActualSgtPolicyId_Type()
)
fadActualSgtPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadActualSgtPolicyId.setStatus("current")


class _FadEgressCirRate_Type(TCIRRate):
    """Custom type fadEgressCirRate based on TCIRRate"""
    defaultValue = -1


_FadEgressCirRate_Type.__name__ = "TCIRRate"
_FadEgressCirRate_Object = MibTableColumn
fadEgressCirRate = _FadEgressCirRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 5),
    _FadEgressCirRate_Type()
)
fadEgressCirRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadEgressCirRate.setStatus("current")


class _FadEgressPirRate_Type(TPIRRate):
    """Custom type fadEgressPirRate based on TPIRRate"""
    defaultValue = -1


_FadEgressPirRate_Type.__name__ = "TPIRRate"
_FadEgressPirRate_Object = MibTableColumn
fadEgressPirRate = _FadEgressPirRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 6),
    _FadEgressPirRate_Type()
)
fadEgressPirRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadEgressPirRate.setStatus("current")


class _FadEgressCBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type fadEgressCBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_FadEgressCBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_FadEgressCBurstSize_Object = MibTableColumn
fadEgressCBurstSize = _FadEgressCBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 7),
    _FadEgressCBurstSize_Type()
)
fadEgressCBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadEgressCBurstSize.setStatus("current")


class _FadEgressPBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type fadEgressPBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_FadEgressPBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_FadEgressPBurstSize_Object = MibTableColumn
fadEgressPBurstSize = _FadEgressPBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 8),
    _FadEgressPBurstSize_Type()
)
fadEgressPBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadEgressPBurstSize.setStatus("current")


class _FadSgtPolicyOverride_Type(TmnxEnabledDisabled):
    """Custom type fadSgtPolicyOverride based on TmnxEnabledDisabled"""
    defaultValue = 1


_FadSgtPolicyOverride_Type.__name__ = "TmnxEnabledDisabled"
_FadSgtPolicyOverride_Object = MibTableColumn
fadSgtPolicyOverride = _FadSgtPolicyOverride_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 9),
    _FadSgtPolicyOverride_Type()
)
fadSgtPolicyOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadSgtPolicyOverride.setStatus("current")


class _FadIngressNetworkQosPolicyId_Type(Integer32):
    """Custom type fadIngressNetworkQosPolicyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FadIngressNetworkQosPolicyId_Type.__name__ = "Integer32"
_FadIngressNetworkQosPolicyId_Object = MibTableColumn
fadIngressNetworkQosPolicyId = _FadIngressNetworkQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 10),
    _FadIngressNetworkQosPolicyId_Type()
)
fadIngressNetworkQosPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadIngressNetworkQosPolicyId.setStatus("current")


class _FadEgressNetworkQosPolicyId_Type(Integer32):
    """Custom type fadEgressNetworkQosPolicyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FadEgressNetworkQosPolicyId_Type.__name__ = "Integer32"
_FadEgressNetworkQosPolicyId_Object = MibTableColumn
fadEgressNetworkQosPolicyId = _FadEgressNetworkQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 11),
    _FadEgressNetworkQosPolicyId_Type()
)
fadEgressNetworkQosPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadEgressNetworkQosPolicyId.setStatus("current")


class _FadVlanDot1qEtype_Type(Unsigned32):
    """Custom type fadVlanDot1qEtype based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1536, 65535),
    )


_FadVlanDot1qEtype_Type.__name__ = "Unsigned32"
_FadVlanDot1qEtype_Object = MibTableColumn
fadVlanDot1qEtype = _FadVlanDot1qEtype_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 12),
    _FadVlanDot1qEtype_Type()
)
fadVlanDot1qEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadVlanDot1qEtype.setStatus("current")


class _FadIngressCirRate_Type(TCIRRate):
    """Custom type fadIngressCirRate based on TCIRRate"""
    defaultValue = -1


_FadIngressCirRate_Type.__name__ = "TCIRRate"
_FadIngressCirRate_Object = MibTableColumn
fadIngressCirRate = _FadIngressCirRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 13),
    _FadIngressCirRate_Type()
)
fadIngressCirRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadIngressCirRate.setStatus("current")


class _FadIngressPirRate_Type(TPIRRate):
    """Custom type fadIngressPirRate based on TPIRRate"""
    defaultValue = -1


_FadIngressPirRate_Type.__name__ = "TPIRRate"
_FadIngressPirRate_Object = MibTableColumn
fadIngressPirRate = _FadIngressPirRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 14),
    _FadIngressPirRate_Type()
)
fadIngressPirRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadIngressPirRate.setStatus("current")


class _FadIngressCBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type fadIngressCBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_FadIngressCBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_FadIngressCBurstSize_Object = MibTableColumn
fadIngressCBurstSize = _FadIngressCBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 15),
    _FadIngressCBurstSize_Type()
)
fadIngressCBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadIngressCBurstSize.setStatus("current")


class _FadIngressPBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type fadIngressPBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_FadIngressPBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_FadIngressPBurstSize_Object = MibTableColumn
fadIngressPBurstSize = _FadIngressPBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 16),
    _FadIngressPBurstSize_Type()
)
fadIngressPBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadIngressPBurstSize.setStatus("current")


class _FadSvcEnableStormControl_Type(TruthValue):
    """Custom type fadSvcEnableStormControl based on TruthValue"""
    defaultValue = 2


_FadSvcEnableStormControl_Type.__name__ = "TruthValue"
_FadSvcEnableStormControl_Object = MibTableColumn
fadSvcEnableStormControl = _FadSvcEnableStormControl_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 1, 1, 17),
    _FadSvcEnableStormControl_Type()
)
fadSvcEnableStormControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadSvcEnableStormControl.setStatus("current")
_FadSvcBaseExtNextFreeSvcId_Type = TmnxServId
_FadSvcBaseExtNextFreeSvcId_Object = MibScalar
fadSvcBaseExtNextFreeSvcId = _FadSvcBaseExtNextFreeSvcId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 2),
    _FadSvcBaseExtNextFreeSvcId_Type()
)
fadSvcBaseExtNextFreeSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSvcBaseExtNextFreeSvcId.setStatus("current")
_FadSvcBaseExtVlanTable_Object = MibTable
fadSvcBaseExtVlanTable = _FadSvcBaseExtVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 3)
)
if mibBuilder.loadTexts:
    fadSvcBaseExtVlanTable.setStatus("current")
_FadSvcBaseExtVlanEntry_Object = MibTableRow
fadSvcBaseExtVlanEntry = _FadSvcBaseExtVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 3, 1)
)
fadSvcBaseExtVlanEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcVplsVlanId"),
)
if mibBuilder.loadTexts:
    fadSvcBaseExtVlanEntry.setStatus("current")
_FadVplsSvcId_Type = TmnxServId
_FadVplsSvcId_Object = MibTableColumn
fadVplsSvcId = _FadVplsSvcId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 2, 3, 1, 1),
    _FadVplsSvcId_Type()
)
fadVplsSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadVplsSvcId.setStatus("current")
_FadSvcTlsExt_ObjectIdentity = ObjectIdentity
fadSvcTlsExt = _FadSvcTlsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 3)
)
_FadSvcTlsExtTable_Object = MibTable
fadSvcTlsExtTable = _FadSvcTlsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 3, 1)
)
if mibBuilder.loadTexts:
    fadSvcTlsExtTable.setStatus("current")
_FadSvcTlsExtEntry_Object = MibTableRow
fadSvcTlsExtEntry = _FadSvcTlsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fadSvcTlsExtEntry.setStatus("current")


class _FadVplsU2uDistinctSaps_Type(TmnxEnabledDisabled):
    """Custom type fadVplsU2uDistinctSaps based on TmnxEnabledDisabled"""
    defaultValue = 2


_FadVplsU2uDistinctSaps_Type.__name__ = "TmnxEnabledDisabled"
_FadVplsU2uDistinctSaps_Object = MibTableColumn
fadVplsU2uDistinctSaps = _FadVplsU2uDistinctSaps_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 3, 1, 1, 1),
    _FadVplsU2uDistinctSaps_Type()
)
fadVplsU2uDistinctSaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadVplsU2uDistinctSaps.setStatus("current")


class _FadVplsUnrestrictMacMove_Type(TmnxEnabledDisabled):
    """Custom type fadVplsUnrestrictMacMove based on TmnxEnabledDisabled"""
    defaultValue = 2


_FadVplsUnrestrictMacMove_Type.__name__ = "TmnxEnabledDisabled"
_FadVplsUnrestrictMacMove_Object = MibTableColumn
fadVplsUnrestrictMacMove = _FadVplsUnrestrictMacMove_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 3, 1, 1, 2),
    _FadVplsUnrestrictMacMove_Type()
)
fadVplsUnrestrictMacMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadVplsUnrestrictMacMove.setStatus("current")


class _FadVplsExtFwdDeviceIpAddressType_Type(InetAddressType):
    """Custom type fadVplsExtFwdDeviceIpAddressType based on InetAddressType"""
    defaultValue = 0


_FadVplsExtFwdDeviceIpAddressType_Type.__name__ = "InetAddressType"
_FadVplsExtFwdDeviceIpAddressType_Object = MibTableColumn
fadVplsExtFwdDeviceIpAddressType = _FadVplsExtFwdDeviceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 3, 1, 1, 3),
    _FadVplsExtFwdDeviceIpAddressType_Type()
)
fadVplsExtFwdDeviceIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadVplsExtFwdDeviceIpAddressType.setStatus("current")
_FadVplsExtFwdDeviceIpAddress_Type = InetAddress
_FadVplsExtFwdDeviceIpAddress_Object = MibTableColumn
fadVplsExtFwdDeviceIpAddress = _FadVplsExtFwdDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 3, 1, 1, 4),
    _FadVplsExtFwdDeviceIpAddress_Type()
)
fadVplsExtFwdDeviceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadVplsExtFwdDeviceIpAddress.setStatus("current")
_FadMirrorService_ObjectIdentity = ObjectIdentity
fadMirrorService = _FadMirrorService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 4)
)
_FadMirrorSourceCpuTable_Object = MibTable
fadMirrorSourceCpuTable = _FadMirrorSourceCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 4, 1)
)
if mibBuilder.loadTexts:
    fadMirrorSourceCpuTable.setStatus("current")
_FadMirrorSourceCpuEntry_Object = MibTableRow
fadMirrorSourceCpuEntry = _FadMirrorSourceCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 4, 1, 1)
)
fadMirrorSourceCpuEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "IHUB-EXT-MIB", "fadMirrorSourceCpuPortIndex"),
)
if mibBuilder.loadTexts:
    fadMirrorSourceCpuEntry.setStatus("current")
_FadMirrorSourceCpuPortIndex_Type = TmnxPortID
_FadMirrorSourceCpuPortIndex_Object = MibTableColumn
fadMirrorSourceCpuPortIndex = _FadMirrorSourceCpuPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 4, 1, 1, 1),
    _FadMirrorSourceCpuPortIndex_Type()
)
fadMirrorSourceCpuPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadMirrorSourceCpuPortIndex.setStatus("current")
_FadMirrorSourceCpuRowStatus_Type = RowStatus
_FadMirrorSourceCpuRowStatus_Object = MibTableColumn
fadMirrorSourceCpuRowStatus = _FadMirrorSourceCpuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 4, 1, 1, 2),
    _FadMirrorSourceCpuRowStatus_Type()
)
fadMirrorSourceCpuRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadMirrorSourceCpuRowStatus.setStatus("current")
_FadMirrorSourceCpuEgressEnabled_Type = TruthValue
_FadMirrorSourceCpuEgressEnabled_Object = MibTableColumn
fadMirrorSourceCpuEgressEnabled = _FadMirrorSourceCpuEgressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 4, 1, 1, 3),
    _FadMirrorSourceCpuEgressEnabled_Type()
)
fadMirrorSourceCpuEgressEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadMirrorSourceCpuEgressEnabled.setStatus("current")
_FadMirrorSourceCpuIngressEnabled_Type = TruthValue
_FadMirrorSourceCpuIngressEnabled_Object = MibTableColumn
fadMirrorSourceCpuIngressEnabled = _FadMirrorSourceCpuIngressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 4, 1, 1, 4),
    _FadMirrorSourceCpuIngressEnabled_Type()
)
fadMirrorSourceCpuIngressEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadMirrorSourceCpuIngressEnabled.setStatus("current")
_FadMirrorSourceCpuLastChgd_Type = TimeStamp
_FadMirrorSourceCpuLastChgd_Object = MibTableColumn
fadMirrorSourceCpuLastChgd = _FadMirrorSourceCpuLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 4, 1, 1, 5),
    _FadMirrorSourceCpuLastChgd_Type()
)
fadMirrorSourceCpuLastChgd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadMirrorSourceCpuLastChgd.setStatus("current")
_FadIesIfExt_ObjectIdentity = ObjectIdentity
fadIesIfExt = _FadIesIfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 5)
)
_FadIesIfExtTable_Object = MibTable
fadIesIfExtTable = _FadIesIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 5, 1)
)
if mibBuilder.loadTexts:
    fadIesIfExtTable.setStatus("current")
_FadIesIfExtEntry_Object = MibTableRow
fadIesIfExtEntry = _FadIesIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 5, 1, 1)
)
if mibBuilder.loadTexts:
    fadIesIfExtEntry.setStatus("current")


class _FadIesIfUserGateway_Type(Integer32):
    """Custom type fadIesIfUserGateway based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("auto-create", 2))
    )


_FadIesIfUserGateway_Type.__name__ = "Integer32"
_FadIesIfUserGateway_Object = MibTableColumn
fadIesIfUserGateway = _FadIesIfUserGateway_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 5, 1, 1, 1),
    _FadIesIfUserGateway_Type()
)
fadIesIfUserGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadIesIfUserGateway.setStatus("current")
_FadFdbExt_ObjectIdentity = ObjectIdentity
fadFdbExt = _FadFdbExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6)
)
_FadFdbExtObjects_ObjectIdentity = ObjectIdentity
fadFdbExtObjects = _FadFdbExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1)
)
_FadFdbExtNotifyObjs_ObjectIdentity = ObjectIdentity
fadFdbExtNotifyObjs = _FadFdbExtNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1)
)
_FadDupMacIndex_Type = Integer32
_FadDupMacIndex_Object = MibScalar
fadDupMacIndex = _FadDupMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 1),
    _FadDupMacIndex_Type()
)
fadDupMacIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacIndex.setStatus("current")
_FadDupMacAddr_Type = MacAddress
_FadDupMacAddr_Object = MibScalar
fadDupMacAddr = _FadDupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 2),
    _FadDupMacAddr_Type()
)
fadDupMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacAddr.setStatus("current")
_FadDupMacSapPortId_Type = TmnxPortID
_FadDupMacSapPortId_Object = MibScalar
fadDupMacSapPortId = _FadDupMacSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 3),
    _FadDupMacSapPortId_Type()
)
fadDupMacSapPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacSapPortId.setStatus("current")
_FadDupMacSapEncapValue_Type = TmnxEncapVal
_FadDupMacSapEncapValue_Object = MibScalar
fadDupMacSapEncapValue = _FadDupMacSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 4),
    _FadDupMacSapEncapValue_Type()
)
fadDupMacSapEncapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacSapEncapValue.setStatus("current")
_FadDupMacDupCVlan_Type = TmnxEncapVal
_FadDupMacDupCVlan_Object = MibScalar
fadDupMacDupCVlan = _FadDupMacDupCVlan_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 5),
    _FadDupMacDupCVlan_Type()
)
fadDupMacDupCVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacDupCVlan.setStatus("current")
_FadDupMacDupSapPortId_Type = TmnxPortID
_FadDupMacDupSapPortId_Object = MibScalar
fadDupMacDupSapPortId = _FadDupMacDupSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 6),
    _FadDupMacDupSapPortId_Type()
)
fadDupMacDupSapPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacDupSapPortId.setStatus("current")
_FadDupMacDupSapEncapValue_Type = TmnxEncapVal
_FadDupMacDupSapEncapValue_Object = MibScalar
fadDupMacDupSapEncapValue = _FadDupMacDupSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 7),
    _FadDupMacDupSapEncapValue_Type()
)
fadDupMacDupSapEncapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacDupSapEncapValue.setStatus("current")


class _FadDupMacType_Type(Integer32):
    """Custom type fadDupMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 1),
          ("self", 2))
    )


_FadDupMacType_Type.__name__ = "Integer32"
_FadDupMacType_Object = MibScalar
fadDupMacType = _FadDupMacType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 8),
    _FadDupMacType_Type()
)
fadDupMacType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacType.setStatus("current")
_FadDupMacSdpBindId_Type = SdpBindId
_FadDupMacSdpBindId_Object = MibScalar
fadDupMacSdpBindId = _FadDupMacSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 9),
    _FadDupMacSdpBindId_Type()
)
fadDupMacSdpBindId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacSdpBindId.setStatus("current")
_FadDupMacDupSdpBindId_Type = SdpBindId
_FadDupMacDupSdpBindId_Object = MibScalar
fadDupMacDupSdpBindId = _FadDupMacDupSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 1, 1, 10),
    _FadDupMacDupSdpBindId_Type()
)
fadDupMacDupSdpBindId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadDupMacDupSdpBindId.setStatus("current")
_FadFdbExtNotifications_ObjectIdentity = ObjectIdentity
fadFdbExtNotifications = _FadFdbExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 2)
)
_FadOspfExt_ObjectIdentity = ObjectIdentity
fadOspfExt = _FadOspfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 7)
)
_FadOspfExtObjects_ObjectIdentity = ObjectIdentity
fadOspfExtObjects = _FadOspfExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 7, 1)
)


class _FadOspfOperState_Type(Integer32):
    """Custom type fadOspfOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_FadOspfOperState_Type.__name__ = "Integer32"
_FadOspfOperState_Object = MibScalar
fadOspfOperState = _FadOspfOperState_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 7, 1, 1),
    _FadOspfOperState_Type()
)
fadOspfOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadOspfOperState.setStatus("current")
_FadOspfExtNotifications_ObjectIdentity = ObjectIdentity
fadOspfExtNotifications = _FadOspfExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 7, 2)
)
_FadBgpExt_ObjectIdentity = ObjectIdentity
fadBgpExt = _FadBgpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 8)
)
_FadBgpExtNotifications_ObjectIdentity = ObjectIdentity
fadBgpExtNotifications = _FadBgpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 8, 1)
)
_FadCpmIpFilterExt_ObjectIdentity = ObjectIdentity
fadCpmIpFilterExt = _FadCpmIpFilterExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 9)
)
_FadCpmIpFilterExtTable_Object = MibTable
fadCpmIpFilterExtTable = _FadCpmIpFilterExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 9, 1)
)
if mibBuilder.loadTexts:
    fadCpmIpFilterExtTable.setStatus("current")
_FadCpmIpFilterExtEntry_Object = MibTableRow
fadCpmIpFilterExtEntry = _FadCpmIpFilterExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 9, 1, 1)
)
if mibBuilder.loadTexts:
    fadCpmIpFilterExtEntry.setStatus("current")


class _FadSvcId_Type(TmnxServId):
    """Custom type fadSvcId based on TmnxServId"""
    defaultValue = 0


_FadSvcId_Type.__name__ = "TmnxServId"
_FadSvcId_Object = MibTableColumn
fadSvcId = _FadSvcId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 9, 1, 1, 1),
    _FadSvcId_Type()
)
fadSvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadSvcId.setStatus("current")
_FadIsisExt_ObjectIdentity = ObjectIdentity
fadIsisExt = _FadIsisExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 10)
)
_FadIsisExtObjects_ObjectIdentity = ObjectIdentity
fadIsisExtObjects = _FadIsisExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 10, 1)
)
_FadIsisExtNotifications_ObjectIdentity = ObjectIdentity
fadIsisExtNotifications = _FadIsisExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 10, 2)
)
_FadIPv6Ext_ObjectIdentity = ObjectIdentity
fadIPv6Ext = _FadIPv6Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11)
)
_FadIPv6ExtObjects_ObjectIdentity = ObjectIdentity
fadIPv6ExtObjects = _FadIPv6ExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1)
)
_FadVrtrV6ExtTable_Object = MibTable
fadVrtrV6ExtTable = _FadVrtrV6ExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 1)
)
if mibBuilder.loadTexts:
    fadVrtrV6ExtTable.setStatus("current")
_FadVrtrV6ExtEntry_Object = MibTableRow
fadVrtrV6ExtEntry = _FadVrtrV6ExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fadVrtrV6ExtEntry.setStatus("current")
_FadVrtrV6ManagedRoutes_Type = Gauge32
_FadVrtrV6ManagedRoutes_Object = MibTableColumn
fadVrtrV6ManagedRoutes = _FadVrtrV6ManagedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 1, 1, 1),
    _FadVrtrV6ManagedRoutes_Type()
)
fadVrtrV6ManagedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadVrtrV6ManagedRoutes.setStatus("current")
_FadVrtrV6ManagedActiveRoutes_Type = Gauge32
_FadVrtrV6ManagedActiveRoutes_Object = MibTableColumn
fadVrtrV6ManagedActiveRoutes = _FadVrtrV6ManagedActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 1, 1, 2),
    _FadVrtrV6ManagedActiveRoutes_Type()
)
fadVrtrV6ManagedActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadVrtrV6ManagedActiveRoutes.setStatus("current")
_FadVrtrV6StatConfiguredIfs_Type = Gauge32
_FadVrtrV6StatConfiguredIfs_Object = MibScalar
fadVrtrV6StatConfiguredIfs = _FadVrtrV6StatConfiguredIfs_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 2),
    _FadVrtrV6StatConfiguredIfs_Type()
)
fadVrtrV6StatConfiguredIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadVrtrV6StatConfiguredIfs.setStatus("current")
_FadDhcp6RouteTable_Object = MibTable
fadDhcp6RouteTable = _FadDhcp6RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 3)
)
if mibBuilder.loadTexts:
    fadDhcp6RouteTable.setStatus("current")
_FadDhcp6RouteEntry_Object = MibTableRow
fadDhcp6RouteEntry = _FadDhcp6RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 3, 1)
)
fadDhcp6RouteEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "IHUB-EXT-MIB", "fadDhcp6RouteDestType"),
    (0, "IHUB-EXT-MIB", "fadDhcp6RouteDest"),
    (0, "IHUB-EXT-MIB", "fadDhcp6RoutePfxLen"),
)
if mibBuilder.loadTexts:
    fadDhcp6RouteEntry.setStatus("current")
_FadDhcp6RouteDestType_Type = InetAddressType
_FadDhcp6RouteDestType_Object = MibTableColumn
fadDhcp6RouteDestType = _FadDhcp6RouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 3, 1, 1),
    _FadDhcp6RouteDestType_Type()
)
fadDhcp6RouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadDhcp6RouteDestType.setStatus("current")
_FadDhcp6RouteDest_Type = InetAddress
_FadDhcp6RouteDest_Object = MibTableColumn
fadDhcp6RouteDest = _FadDhcp6RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 3, 1, 2),
    _FadDhcp6RouteDest_Type()
)
fadDhcp6RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadDhcp6RouteDest.setStatus("current")
_FadDhcp6RoutePfxLen_Type = InetAddressPrefixLength
_FadDhcp6RoutePfxLen_Object = MibTableColumn
fadDhcp6RoutePfxLen = _FadDhcp6RoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 3, 1, 3),
    _FadDhcp6RoutePfxLen_Type()
)
fadDhcp6RoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadDhcp6RoutePfxLen.setStatus("current")
_FadDhcp6RouteNextHopType_Type = InetAddressType
_FadDhcp6RouteNextHopType_Object = MibTableColumn
fadDhcp6RouteNextHopType = _FadDhcp6RouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 3, 1, 4),
    _FadDhcp6RouteNextHopType_Type()
)
fadDhcp6RouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDhcp6RouteNextHopType.setStatus("current")
_FadDhcp6RouteNextHop_Type = InetAddress
_FadDhcp6RouteNextHop_Object = MibTableColumn
fadDhcp6RouteNextHop = _FadDhcp6RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 3, 1, 5),
    _FadDhcp6RouteNextHop_Type()
)
fadDhcp6RouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDhcp6RouteNextHop.setStatus("current")
_FadDhcp6RouteStatus_Type = TmnxManagedRouteStatus
_FadDhcp6RouteStatus_Object = MibTableColumn
fadDhcp6RouteStatus = _FadDhcp6RouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 1, 3, 1, 6),
    _FadDhcp6RouteStatus_Type()
)
fadDhcp6RouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDhcp6RouteStatus.setStatus("current")
_FadIPv6ExtNotifications_ObjectIdentity = ObjectIdentity
fadIPv6ExtNotifications = _FadIPv6ExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 2)
)
_FadIPv6ExtNotifyObjects_ObjectIdentity = ObjectIdentity
fadIPv6ExtNotifyObjects = _FadIPv6ExtNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 3)
)
_FadMaxNbrCacheEntries_Type = Integer32
_FadMaxNbrCacheEntries_Object = MibScalar
fadMaxNbrCacheEntries = _FadMaxNbrCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 3, 1),
    _FadMaxNbrCacheEntries_Type()
)
fadMaxNbrCacheEntries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fadMaxNbrCacheEntries.setStatus("current")
_FadL2L3FilterExt_ObjectIdentity = ObjectIdentity
fadL2L3FilterExt = _FadL2L3FilterExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 12)
)


class _FadFilterMode_Type(Integer32):
    """Custom type fadFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layers2and3", 2),
          ("layer3", 3))
    )


_FadFilterMode_Type.__name__ = "Integer32"
_FadFilterMode_Object = MibScalar
fadFilterMode = _FadFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 12, 1),
    _FadFilterMode_Type()
)
fadFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadFilterMode.setStatus("current")
_FadMaxNumberIngressL2Filters_Type = Integer32
_FadMaxNumberIngressL2Filters_Object = MibScalar
fadMaxNumberIngressL2Filters = _FadMaxNumberIngressL2Filters_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 12, 2),
    _FadMaxNumberIngressL2Filters_Type()
)
fadMaxNumberIngressL2Filters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadMaxNumberIngressL2Filters.setStatus("current")
_FadMaxNumberIngressL3Filters_Type = Integer32
_FadMaxNumberIngressL3Filters_Object = MibScalar
fadMaxNumberIngressL3Filters = _FadMaxNumberIngressL3Filters_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 12, 3),
    _FadMaxNumberIngressL3Filters_Type()
)
fadMaxNumberIngressL3Filters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadMaxNumberIngressL3Filters.setStatus("current")
_FadSourceIpExt_ObjectIdentity = ObjectIdentity
fadSourceIpExt = _FadSourceIpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 13)
)
_FadSourceIpExtTable_Object = MibTable
fadSourceIpExtTable = _FadSourceIpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 13, 1)
)
if mibBuilder.loadTexts:
    fadSourceIpExtTable.setStatus("current")
_FadSourceIpExtEntry_Object = MibTableRow
fadSourceIpExtEntry = _FadSourceIpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 13, 1, 1)
)
fadSourceIpExtEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    fadSourceIpExtEntry.setStatus("current")


class _FadSourceIpExtAddrType_Type(Integer32):
    """Custom type fadSourceIpExtAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("system", 2))
    )


_FadSourceIpExtAddrType_Type.__name__ = "Integer32"
_FadSourceIpExtAddrType_Object = MibTableColumn
fadSourceIpExtAddrType = _FadSourceIpExtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 13, 1, 1, 1),
    _FadSourceIpExtAddrType_Type()
)
fadSourceIpExtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadSourceIpExtAddrType.setStatus("current")
_FadSourceIpExtRowStatus_Type = RowStatus
_FadSourceIpExtRowStatus_Object = MibTableColumn
fadSourceIpExtRowStatus = _FadSourceIpExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 13, 1, 1, 2),
    _FadSourceIpExtRowStatus_Type()
)
fadSourceIpExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadSourceIpExtRowStatus.setStatus("current")
_FadMacIpFilterExt_ObjectIdentity = ObjectIdentity
fadMacIpFilterExt = _FadMacIpFilterExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 14)
)
_FadNextFreeIpFilterId_Type = TFilterID
_FadNextFreeIpFilterId_Object = MibScalar
fadNextFreeIpFilterId = _FadNextFreeIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 14, 1),
    _FadNextFreeIpFilterId_Type()
)
fadNextFreeIpFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadNextFreeIpFilterId.setStatus("current")
_FadNextFreeIpv6FilterId_Type = TFilterID
_FadNextFreeIpv6FilterId_Object = MibScalar
fadNextFreeIpv6FilterId = _FadNextFreeIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 14, 2),
    _FadNextFreeIpv6FilterId_Type()
)
fadNextFreeIpv6FilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadNextFreeIpv6FilterId.setStatus("current")
_FadNextFreeMacFilterId_Type = TFilterID
_FadNextFreeMacFilterId_Object = MibScalar
fadNextFreeMacFilterId = _FadNextFreeMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 14, 3),
    _FadNextFreeMacFilterId_Type()
)
fadNextFreeMacFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadNextFreeMacFilterId.setStatus("current")
_FadLagExt_ObjectIdentity = ObjectIdentity
fadLagExt = _FadLagExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15)
)
_FadLagPortTable_Object = MibTable
fadLagPortTable = _FadLagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 1)
)
if mibBuilder.loadTexts:
    fadLagPortTable.setStatus("current")
_FadLagPortEntry_Object = MibTableRow
fadLagPortEntry = _FadLagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 1, 1)
)
if mibBuilder.loadTexts:
    fadLagPortEntry.setStatus("current")


class _FadLagPortSubgroup_Type(Integer32):
    """Custom type fadLagPortSubgroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FadLagPortSubgroup_Type.__name__ = "Integer32"
_FadLagPortSubgroup_Object = MibTableColumn
fadLagPortSubgroup = _FadLagPortSubgroup_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 1, 1, 1),
    _FadLagPortSubgroup_Type()
)
fadLagPortSubgroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadLagPortSubgroup.setStatus("current")
_FadLagConfigExtTable_Object = MibTable
fadLagConfigExtTable = _FadLagConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 2)
)
if mibBuilder.loadTexts:
    fadLagConfigExtTable.setStatus("current")
_FadLagConfigExtEntry_Object = MibTableRow
fadLagConfigExtEntry = _FadLagConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 2, 1)
)
if mibBuilder.loadTexts:
    fadLagConfigExtEntry.setStatus("current")


class _FadLagActiveSubgroup_Type(Integer32):
    """Custom type fadLagActiveSubgroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FadLagActiveSubgroup_Type.__name__ = "Integer32"
_FadLagActiveSubgroup_Object = MibTableColumn
fadLagActiveSubgroup = _FadLagActiveSubgroup_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 2, 1, 1),
    _FadLagActiveSubgroup_Type()
)
fadLagActiveSubgroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadLagActiveSubgroup.setStatus("current")


class _FadLagForceSubgroupSelect_Type(Integer32):
    """Custom type fadLagForceSubgroupSelect based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2),
    )


_FadLagForceSubgroupSelect_Type.__name__ = "Integer32"
_FadLagForceSubgroupSelect_Object = MibTableColumn
fadLagForceSubgroupSelect = _FadLagForceSubgroupSelect_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 2, 1, 2),
    _FadLagForceSubgroupSelect_Type()
)
fadLagForceSubgroupSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadLagForceSubgroupSelect.setStatus("current")
_FadLagSubgroupSwitchCount_Type = Counter32
_FadLagSubgroupSwitchCount_Object = MibTableColumn
fadLagSubgroupSwitchCount = _FadLagSubgroupSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 2, 1, 3),
    _FadLagSubgroupSwitchCount_Type()
)
fadLagSubgroupSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadLagSubgroupSwitchCount.setStatus("current")


class _FadLagSubgroupSwitchDetectTime_Type(Integer32):
    """Custom type fadLagSubgroupSwitchDetectTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FadLagSubgroupSwitchDetectTime_Type.__name__ = "Integer32"
_FadLagSubgroupSwitchDetectTime_Object = MibTableColumn
fadLagSubgroupSwitchDetectTime = _FadLagSubgroupSwitchDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 2, 1, 4),
    _FadLagSubgroupSwitchDetectTime_Type()
)
fadLagSubgroupSwitchDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadLagSubgroupSwitchDetectTime.setStatus("current")
_FadLagSubgroupTable_Object = MibTable
fadLagSubgroupTable = _FadLagSubgroupTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 3)
)
if mibBuilder.loadTexts:
    fadLagSubgroupTable.setStatus("current")
_FadLagSubgroupEntry_Object = MibTableRow
fadLagSubgroupEntry = _FadLagSubgroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 3, 1)
)
fadLagSubgroupEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
    (0, "IHUB-EXT-MIB", "fadLagSubgroupIndex"),
)
if mibBuilder.loadTexts:
    fadLagSubgroupEntry.setStatus("current")


class _FadLagSubgroupIndex_Type(Integer32):
    """Custom type fadLagSubgroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FadLagSubgroupIndex_Type.__name__ = "Integer32"
_FadLagSubgroupIndex_Object = MibTableColumn
fadLagSubgroupIndex = _FadLagSubgroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 3, 1, 1),
    _FadLagSubgroupIndex_Type()
)
fadLagSubgroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadLagSubgroupIndex.setStatus("current")


class _FadLagSubgroupPreference_Type(Integer32):
    """Custom type fadLagSubgroupPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FadLagSubgroupPreference_Type.__name__ = "Integer32"
_FadLagSubgroupPreference_Object = MibTableColumn
fadLagSubgroupPreference = _FadLagSubgroupPreference_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 3, 1, 2),
    _FadLagSubgroupPreference_Type()
)
fadLagSubgroupPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadLagSubgroupPreference.setStatus("current")


class _FadLagSubgroupThreshold_Type(Integer32):
    """Custom type fadLagSubgroupThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FadLagSubgroupThreshold_Type.__name__ = "Integer32"
_FadLagSubgroupThreshold_Object = MibTableColumn
fadLagSubgroupThreshold = _FadLagSubgroupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 15, 3, 1, 3),
    _FadLagSubgroupThreshold_Type()
)
fadLagSubgroupThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadLagSubgroupThreshold.setStatus("current")
_FadNtpExt_ObjectIdentity = ObjectIdentity
fadNtpExt = _FadNtpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 16)
)
_FadNtpExtSystem_ObjectIdentity = ObjectIdentity
fadNtpExtSystem = _FadNtpExtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 16, 1)
)


class _FadNtpSysPollRate_Type(Integer32):
    """Custom type fadNtpSysPollRate based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_FadNtpSysPollRate_Type.__name__ = "Integer32"
_FadNtpSysPollRate_Object = MibScalar
fadNtpSysPollRate = _FadNtpSysPollRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 16, 1, 1),
    _FadNtpSysPollRate_Type()
)
fadNtpSysPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadNtpSysPollRate.setStatus("current")
_FadNtpExtServers_ObjectIdentity = ObjectIdentity
fadNtpExtServers = _FadNtpExtServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 16, 2)
)
_FadNtpExtServersTable_Object = MibTable
fadNtpExtServersTable = _FadNtpExtServersTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 16, 2, 1)
)
if mibBuilder.loadTexts:
    fadNtpExtServersTable.setStatus("current")
_FadNtpExtServersEntry_Object = MibTableRow
fadNtpExtServersEntry = _FadNtpExtServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fadNtpExtServersEntry.setStatus("current")
_FadNtpExtServersPort_Type = InetPortNumber
_FadNtpExtServersPort_Object = MibTableColumn
fadNtpExtServersPort = _FadNtpExtServersPort_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 16, 2, 1, 1, 1),
    _FadNtpExtServersPort_Type()
)
fadNtpExtServersPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadNtpExtServersPort.setStatus("current")
_FadSapBaseExt_ObjectIdentity = ObjectIdentity
fadSapBaseExt = _FadSapBaseExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17)
)
_FadSapBaseInfoExtTable_Object = MibTable
fadSapBaseInfoExtTable = _FadSapBaseInfoExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 1)
)
if mibBuilder.loadTexts:
    fadSapBaseInfoExtTable.setStatus("current")
_FadSapBaseInfoExtEntry_Object = MibTableRow
fadSapBaseInfoExtEntry = _FadSapBaseInfoExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 1, 1)
)
if mibBuilder.loadTexts:
    fadSapBaseInfoExtEntry.setStatus("current")


class _FadRestrictedTagging_Type(TruthValue):
    """Custom type fadRestrictedTagging based on TruthValue"""
    defaultValue = 2


_FadRestrictedTagging_Type.__name__ = "TruthValue"
_FadRestrictedTagging_Object = MibTableColumn
fadRestrictedTagging = _FadRestrictedTagging_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 1, 1, 1),
    _FadRestrictedTagging_Type()
)
fadRestrictedTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadRestrictedTagging.setStatus("current")


class _FadSapConfigPersistentControl_Type(TruthValue):
    """Custom type fadSapConfigPersistentControl based on TruthValue"""
    defaultValue = 1


_FadSapConfigPersistentControl_Type.__name__ = "TruthValue"
_FadSapConfigPersistentControl_Object = MibTableColumn
fadSapConfigPersistentControl = _FadSapConfigPersistentControl_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 1, 1, 2),
    _FadSapConfigPersistentControl_Type()
)
fadSapConfigPersistentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadSapConfigPersistentControl.setStatus("current")
_FadSapBaseExtPM_ObjectIdentity = ObjectIdentity
fadSapBaseExtPM = _FadSapBaseExtPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2)
)
_FadSapStatsConfigTable_Object = MibTable
fadSapStatsConfigTable = _FadSapStatsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 1)
)
if mibBuilder.loadTexts:
    fadSapStatsConfigTable.setStatus("current")
_FadSapStatsConfigEntry_Object = MibTableRow
fadSapStatsConfigEntry = _FadSapStatsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fadSapStatsConfigEntry.setStatus("current")
_FadSapStatsStatus_Type = TruthValue
_FadSapStatsStatus_Object = MibTableColumn
fadSapStatsStatus = _FadSapStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 1, 1, 1),
    _FadSapStatsStatus_Type()
)
fadSapStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadSapStatsStatus.setStatus("current")
_FadSapStatsEnabledTime_Type = TimeStamp
_FadSapStatsEnabledTime_Object = MibTableColumn
fadSapStatsEnabledTime = _FadSapStatsEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 1, 1, 2),
    _FadSapStatsEnabledTime_Type()
)
fadSapStatsEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapStatsEnabledTime.setStatus("current")
_FadSapStatsTable_Object = MibTable
fadSapStatsTable = _FadSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 2)
)
if mibBuilder.loadTexts:
    fadSapStatsTable.setStatus("current")
_FadSapStatsEntry_Object = MibTableRow
fadSapStatsEntry = _FadSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fadSapStatsEntry.setStatus("current")
_FadSapStatsIngressPkts_Type = Counter64
_FadSapStatsIngressPkts_Object = MibTableColumn
fadSapStatsIngressPkts = _FadSapStatsIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 2, 1, 1),
    _FadSapStatsIngressPkts_Type()
)
fadSapStatsIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapStatsIngressPkts.setStatus("current")
_FadSapStatsIngressOctets_Type = Counter64
_FadSapStatsIngressOctets_Object = MibTableColumn
fadSapStatsIngressOctets = _FadSapStatsIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 2, 1, 2),
    _FadSapStatsIngressOctets_Type()
)
fadSapStatsIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapStatsIngressOctets.setStatus("current")
_FadSapStatsEgressPkts_Type = Counter64
_FadSapStatsEgressPkts_Object = MibTableColumn
fadSapStatsEgressPkts = _FadSapStatsEgressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 2, 1, 3),
    _FadSapStatsEgressPkts_Type()
)
fadSapStatsEgressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapStatsEgressPkts.setStatus("current")
_FadSapStatsEgressOctets_Type = Counter64
_FadSapStatsEgressOctets_Object = MibTableColumn
fadSapStatsEgressOctets = _FadSapStatsEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 2, 1, 4),
    _FadSapStatsEgressOctets_Type()
)
fadSapStatsEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapStatsEgressOctets.setStatus("current")
_FadSapPMCurrent15MinIntervalTable_Object = MibTable
fadSapPMCurrent15MinIntervalTable = _FadSapPMCurrent15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3)
)
if mibBuilder.loadTexts:
    fadSapPMCurrent15MinIntervalTable.setStatus("current")
_FadSapPMCurrent15MinIntervalEntry_Object = MibTableRow
fadSapPMCurrent15MinIntervalEntry = _FadSapPMCurrent15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3, 1)
)
fadSapPMCurrent15MinIntervalEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    fadSapPMCurrent15MinIntervalEntry.setStatus("current")


class _FadSapPMCurrent15MinTimeElapsed_Type(Integer32):
    """Custom type fadSapPMCurrent15MinTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadSapPMCurrent15MinTimeElapsed_Type.__name__ = "Integer32"
_FadSapPMCurrent15MinTimeElapsed_Object = MibTableColumn
fadSapPMCurrent15MinTimeElapsed = _FadSapPMCurrent15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3, 1, 1),
    _FadSapPMCurrent15MinTimeElapsed_Type()
)
fadSapPMCurrent15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent15MinTimeElapsed.setStatus("current")


class _FadSapPMCurrent15MinTimeMeasured_Type(Integer32):
    """Custom type fadSapPMCurrent15MinTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadSapPMCurrent15MinTimeMeasured_Type.__name__ = "Integer32"
_FadSapPMCurrent15MinTimeMeasured_Object = MibTableColumn
fadSapPMCurrent15MinTimeMeasured = _FadSapPMCurrent15MinTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3, 1, 2),
    _FadSapPMCurrent15MinTimeMeasured_Type()
)
fadSapPMCurrent15MinTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent15MinTimeMeasured.setStatus("current")
_FadSapPMCurrent15MinIngressPkts_Type = Counter64
_FadSapPMCurrent15MinIngressPkts_Object = MibTableColumn
fadSapPMCurrent15MinIngressPkts = _FadSapPMCurrent15MinIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3, 1, 3),
    _FadSapPMCurrent15MinIngressPkts_Type()
)
fadSapPMCurrent15MinIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent15MinIngressPkts.setStatus("current")
_FadSapPMCurrent15MinIngressOctets_Type = Counter64
_FadSapPMCurrent15MinIngressOctets_Object = MibTableColumn
fadSapPMCurrent15MinIngressOctets = _FadSapPMCurrent15MinIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3, 1, 4),
    _FadSapPMCurrent15MinIngressOctets_Type()
)
fadSapPMCurrent15MinIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent15MinIngressOctets.setStatus("current")
_FadSapPMCurrent15MinEgressPkts_Type = Counter64
_FadSapPMCurrent15MinEgressPkts_Object = MibTableColumn
fadSapPMCurrent15MinEgressPkts = _FadSapPMCurrent15MinEgressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3, 1, 5),
    _FadSapPMCurrent15MinEgressPkts_Type()
)
fadSapPMCurrent15MinEgressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent15MinEgressPkts.setStatus("current")
_FadSapPMCurrent15MinEgressOctets_Type = Counter64
_FadSapPMCurrent15MinEgressOctets_Object = MibTableColumn
fadSapPMCurrent15MinEgressOctets = _FadSapPMCurrent15MinEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3, 1, 6),
    _FadSapPMCurrent15MinEgressOctets_Type()
)
fadSapPMCurrent15MinEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent15MinEgressOctets.setStatus("current")


class _FadSapPM15MinValidIntervals_Type(Integer32):
    """Custom type fadSapPM15MinValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FadSapPM15MinValidIntervals_Type.__name__ = "Integer32"
_FadSapPM15MinValidIntervals_Object = MibTableColumn
fadSapPM15MinValidIntervals = _FadSapPM15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 3, 1, 7),
    _FadSapPM15MinValidIntervals_Type()
)
fadSapPM15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPM15MinValidIntervals.setStatus("current")
_FadSapPMCurrent1DayIntervalTable_Object = MibTable
fadSapPMCurrent1DayIntervalTable = _FadSapPMCurrent1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4)
)
if mibBuilder.loadTexts:
    fadSapPMCurrent1DayIntervalTable.setStatus("current")
_FadSapPMCurrent1DayIntervalEntry_Object = MibTableRow
fadSapPMCurrent1DayIntervalEntry = _FadSapPMCurrent1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4, 1)
)
fadSapPMCurrent1DayIntervalEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    fadSapPMCurrent1DayIntervalEntry.setStatus("current")


class _FadSapPMCurrent1DayTimeElapsed_Type(Integer32):
    """Custom type fadSapPMCurrent1DayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadSapPMCurrent1DayTimeElapsed_Type.__name__ = "Integer32"
_FadSapPMCurrent1DayTimeElapsed_Object = MibTableColumn
fadSapPMCurrent1DayTimeElapsed = _FadSapPMCurrent1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4, 1, 1),
    _FadSapPMCurrent1DayTimeElapsed_Type()
)
fadSapPMCurrent1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent1DayTimeElapsed.setStatus("current")


class _FadSapPMCurrent1DayTimeMeasured_Type(Integer32):
    """Custom type fadSapPMCurrent1DayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadSapPMCurrent1DayTimeMeasured_Type.__name__ = "Integer32"
_FadSapPMCurrent1DayTimeMeasured_Object = MibTableColumn
fadSapPMCurrent1DayTimeMeasured = _FadSapPMCurrent1DayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4, 1, 2),
    _FadSapPMCurrent1DayTimeMeasured_Type()
)
fadSapPMCurrent1DayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent1DayTimeMeasured.setStatus("current")
_FadSapPMCurrent1DayIngressPkts_Type = Counter64
_FadSapPMCurrent1DayIngressPkts_Object = MibTableColumn
fadSapPMCurrent1DayIngressPkts = _FadSapPMCurrent1DayIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4, 1, 3),
    _FadSapPMCurrent1DayIngressPkts_Type()
)
fadSapPMCurrent1DayIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent1DayIngressPkts.setStatus("current")
_FadSapPMCurrent1DayIngressOctets_Type = Counter64
_FadSapPMCurrent1DayIngressOctets_Object = MibTableColumn
fadSapPMCurrent1DayIngressOctets = _FadSapPMCurrent1DayIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4, 1, 4),
    _FadSapPMCurrent1DayIngressOctets_Type()
)
fadSapPMCurrent1DayIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent1DayIngressOctets.setStatus("current")
_FadSapPMCurrent1DayEgressPkts_Type = Counter64
_FadSapPMCurrent1DayEgressPkts_Object = MibTableColumn
fadSapPMCurrent1DayEgressPkts = _FadSapPMCurrent1DayEgressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4, 1, 5),
    _FadSapPMCurrent1DayEgressPkts_Type()
)
fadSapPMCurrent1DayEgressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent1DayEgressPkts.setStatus("current")
_FadSapPMCurrent1DayEgressOctets_Type = Counter64
_FadSapPMCurrent1DayEgressOctets_Object = MibTableColumn
fadSapPMCurrent1DayEgressOctets = _FadSapPMCurrent1DayEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4, 1, 6),
    _FadSapPMCurrent1DayEgressOctets_Type()
)
fadSapPMCurrent1DayEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMCurrent1DayEgressOctets.setStatus("current")


class _FadSapPM1DayValidIntervals_Type(Integer32):
    """Custom type fadSapPM1DayValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FadSapPM1DayValidIntervals_Type.__name__ = "Integer32"
_FadSapPM1DayValidIntervals_Object = MibTableColumn
fadSapPM1DayValidIntervals = _FadSapPM1DayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 4, 1, 7),
    _FadSapPM1DayValidIntervals_Type()
)
fadSapPM1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPM1DayValidIntervals.setStatus("current")
_FadSapPMPrevious15MinIntervalTable_Object = MibTable
fadSapPMPrevious15MinIntervalTable = _FadSapPMPrevious15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 5)
)
if mibBuilder.loadTexts:
    fadSapPMPrevious15MinIntervalTable.setStatus("current")
_FadSapPMPrevious15MinIntervalEntry_Object = MibTableRow
fadSapPMPrevious15MinIntervalEntry = _FadSapPMPrevious15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 5, 1)
)
fadSapPMPrevious15MinIntervalEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "IHUB-EXT-MIB", "fadSapPMPrevious15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    fadSapPMPrevious15MinIntervalEntry.setStatus("current")


class _FadSapPMPrevious15MinIntervalNumber_Type(Integer32):
    """Custom type fadSapPMPrevious15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FadSapPMPrevious15MinIntervalNumber_Type.__name__ = "Integer32"
_FadSapPMPrevious15MinIntervalNumber_Object = MibTableColumn
fadSapPMPrevious15MinIntervalNumber = _FadSapPMPrevious15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 5, 1, 1),
    _FadSapPMPrevious15MinIntervalNumber_Type()
)
fadSapPMPrevious15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious15MinIntervalNumber.setStatus("current")


class _FadSapPMPrevious15MinTimeMeasured_Type(Integer32):
    """Custom type fadSapPMPrevious15MinTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadSapPMPrevious15MinTimeMeasured_Type.__name__ = "Integer32"
_FadSapPMPrevious15MinTimeMeasured_Object = MibTableColumn
fadSapPMPrevious15MinTimeMeasured = _FadSapPMPrevious15MinTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 5, 1, 2),
    _FadSapPMPrevious15MinTimeMeasured_Type()
)
fadSapPMPrevious15MinTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious15MinTimeMeasured.setStatus("current")
_FadSapPMPrevious15MinIngressPkts_Type = Counter64
_FadSapPMPrevious15MinIngressPkts_Object = MibTableColumn
fadSapPMPrevious15MinIngressPkts = _FadSapPMPrevious15MinIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 5, 1, 3),
    _FadSapPMPrevious15MinIngressPkts_Type()
)
fadSapPMPrevious15MinIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious15MinIngressPkts.setStatus("current")
_FadSapPMPrevious15MinIngressOctets_Type = Counter64
_FadSapPMPrevious15MinIngressOctets_Object = MibTableColumn
fadSapPMPrevious15MinIngressOctets = _FadSapPMPrevious15MinIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 5, 1, 4),
    _FadSapPMPrevious15MinIngressOctets_Type()
)
fadSapPMPrevious15MinIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious15MinIngressOctets.setStatus("current")
_FadSapPMPrevious15MinEgressPkts_Type = Counter64
_FadSapPMPrevious15MinEgressPkts_Object = MibTableColumn
fadSapPMPrevious15MinEgressPkts = _FadSapPMPrevious15MinEgressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 5, 1, 5),
    _FadSapPMPrevious15MinEgressPkts_Type()
)
fadSapPMPrevious15MinEgressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious15MinEgressPkts.setStatus("current")
_FadSapPMPrevious15MinEgressOctets_Type = Counter64
_FadSapPMPrevious15MinEgressOctets_Object = MibTableColumn
fadSapPMPrevious15MinEgressOctets = _FadSapPMPrevious15MinEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 5, 1, 6),
    _FadSapPMPrevious15MinEgressOctets_Type()
)
fadSapPMPrevious15MinEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious15MinEgressOctets.setStatus("current")
_FadSapPMPrevious1DayIntervalTable_Object = MibTable
fadSapPMPrevious1DayIntervalTable = _FadSapPMPrevious1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 6)
)
if mibBuilder.loadTexts:
    fadSapPMPrevious1DayIntervalTable.setStatus("current")
_FadSapPMPrevious1DayIntervalEntry_Object = MibTableRow
fadSapPMPrevious1DayIntervalEntry = _FadSapPMPrevious1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 6, 1)
)
fadSapPMPrevious1DayIntervalEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "IHUB-EXT-MIB", "fadSapPMPrevious1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    fadSapPMPrevious1DayIntervalEntry.setStatus("current")


class _FadSapPMPrevious1DayIntervalNumber_Type(Integer32):
    """Custom type fadSapPMPrevious1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FadSapPMPrevious1DayIntervalNumber_Type.__name__ = "Integer32"
_FadSapPMPrevious1DayIntervalNumber_Object = MibTableColumn
fadSapPMPrevious1DayIntervalNumber = _FadSapPMPrevious1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 6, 1, 1),
    _FadSapPMPrevious1DayIntervalNumber_Type()
)
fadSapPMPrevious1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious1DayIntervalNumber.setStatus("current")


class _FadSapPMPrevious1DayTimeMeasured_Type(Integer32):
    """Custom type fadSapPMPrevious1DayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadSapPMPrevious1DayTimeMeasured_Type.__name__ = "Integer32"
_FadSapPMPrevious1DayTimeMeasured_Object = MibTableColumn
fadSapPMPrevious1DayTimeMeasured = _FadSapPMPrevious1DayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 6, 1, 2),
    _FadSapPMPrevious1DayTimeMeasured_Type()
)
fadSapPMPrevious1DayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious1DayTimeMeasured.setStatus("current")
_FadSapPMPrevious1DayIngressPkts_Type = Counter64
_FadSapPMPrevious1DayIngressPkts_Object = MibTableColumn
fadSapPMPrevious1DayIngressPkts = _FadSapPMPrevious1DayIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 6, 1, 3),
    _FadSapPMPrevious1DayIngressPkts_Type()
)
fadSapPMPrevious1DayIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious1DayIngressPkts.setStatus("current")
_FadSapPMPrevious1DayIngressOctets_Type = Counter64
_FadSapPMPrevious1DayIngressOctets_Object = MibTableColumn
fadSapPMPrevious1DayIngressOctets = _FadSapPMPrevious1DayIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 6, 1, 4),
    _FadSapPMPrevious1DayIngressOctets_Type()
)
fadSapPMPrevious1DayIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious1DayIngressOctets.setStatus("current")
_FadSapPMPrevious1DayEgressPkts_Type = Counter64
_FadSapPMPrevious1DayEgressPkts_Object = MibTableColumn
fadSapPMPrevious1DayEgressPkts = _FadSapPMPrevious1DayEgressPkts_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 6, 1, 5),
    _FadSapPMPrevious1DayEgressPkts_Type()
)
fadSapPMPrevious1DayEgressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious1DayEgressPkts.setStatus("current")
_FadSapPMPrevious1DayEgressOctets_Type = Counter64
_FadSapPMPrevious1DayEgressOctets_Object = MibTableColumn
fadSapPMPrevious1DayEgressOctets = _FadSapPMPrevious1DayEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 17, 2, 6, 1, 6),
    _FadSapPMPrevious1DayEgressOctets_Type()
)
fadSapPMPrevious1DayEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadSapPMPrevious1DayEgressOctets.setStatus("current")
_FadSysU2UExt_ObjectIdentity = ObjectIdentity
fadSysU2UExt = _FadSysU2UExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 18)
)


class _FadSysU2USameSap_Type(TruthValue):
    """Custom type fadSysU2USameSap based on TruthValue"""
    defaultValue = 2


_FadSysU2USameSap_Type.__name__ = "TruthValue"
_FadSysU2USameSap_Object = MibScalar
fadSysU2USameSap = _FadSysU2USameSap_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 18, 1),
    _FadSysU2USameSap_Type()
)
fadSysU2USameSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadSysU2USameSap.setStatus("current")
_FadCfmExt_ObjectIdentity = ObjectIdentity
fadCfmExt = _FadCfmExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19)
)
_FadNumCcmEnabledMeps_Type = Counter32
_FadNumCcmEnabledMeps_Object = MibScalar
fadNumCcmEnabledMeps = _FadNumCcmEnabledMeps_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 1),
    _FadNumCcmEnabledMeps_Type()
)
fadNumCcmEnabledMeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadNumCcmEnabledMeps.setStatus("current")
_FadDot1agCfmStackTable_Object = MibTable
fadDot1agCfmStackTable = _FadDot1agCfmStackTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 2)
)
if mibBuilder.loadTexts:
    fadDot1agCfmStackTable.setStatus("current")
_FadDot1agCfmStackEntry_Object = MibTableRow
fadDot1agCfmStackEntry = _FadDot1agCfmStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 2, 1)
)
if mibBuilder.loadTexts:
    fadDot1agCfmStackEntry.setStatus("current")


class _FadDot1agCfmSapMpOperStatus_Type(Integer32):
    """Custom type fadDot1agCfmSapMpOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FadDot1agCfmSapMpOperStatus_Type.__name__ = "Integer32"
_FadDot1agCfmSapMpOperStatus_Object = MibTableColumn
fadDot1agCfmSapMpOperStatus = _FadDot1agCfmSapMpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 2, 1, 1),
    _FadDot1agCfmSapMpOperStatus_Type()
)
fadDot1agCfmSapMpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmSapMpOperStatus.setStatus("current")


class _FadDot1agCfmStackMpSvcId_Type(TmnxServId):
    """Custom type fadDot1agCfmStackMpSvcId based on TmnxServId"""
    defaultValue = 0


_FadDot1agCfmStackMpSvcId_Type.__name__ = "TmnxServId"
_FadDot1agCfmStackMpSvcId_Object = MibTableColumn
fadDot1agCfmStackMpSvcId = _FadDot1agCfmStackMpSvcId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 2, 1, 2),
    _FadDot1agCfmStackMpSvcId_Type()
)
fadDot1agCfmStackMpSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmStackMpSvcId.setStatus("current")
_FadDot1agCfmSdpBindStackTable_Object = MibTable
fadDot1agCfmSdpBindStackTable = _FadDot1agCfmSdpBindStackTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 3)
)
if mibBuilder.loadTexts:
    fadDot1agCfmSdpBindStackTable.setStatus("current")
_FadDot1agCfmSdpBindStackEntry_Object = MibTableRow
fadDot1agCfmSdpBindStackEntry = _FadDot1agCfmSdpBindStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 3, 1)
)
if mibBuilder.loadTexts:
    fadDot1agCfmSdpBindStackEntry.setStatus("current")


class _FadDot1agCfmSdpMpOperStatus_Type(Integer32):
    """Custom type fadDot1agCfmSdpMpOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FadDot1agCfmSdpMpOperStatus_Type.__name__ = "Integer32"
_FadDot1agCfmSdpMpOperStatus_Object = MibTableColumn
fadDot1agCfmSdpMpOperStatus = _FadDot1agCfmSdpMpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 3, 1, 1),
    _FadDot1agCfmSdpMpOperStatus_Type()
)
fadDot1agCfmSdpMpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmSdpMpOperStatus.setStatus("current")


class _FadDot1agCfmSdpBindMpSvcId_Type(TmnxServId):
    """Custom type fadDot1agCfmSdpBindMpSvcId based on TmnxServId"""
    defaultValue = 0


_FadDot1agCfmSdpBindMpSvcId_Type.__name__ = "TmnxServId"
_FadDot1agCfmSdpBindMpSvcId_Object = MibTableColumn
fadDot1agCfmSdpBindMpSvcId = _FadDot1agCfmSdpBindMpSvcId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 3, 1, 2),
    _FadDot1agCfmSdpBindMpSvcId_Type()
)
fadDot1agCfmSdpBindMpSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmSdpBindMpSvcId.setStatus("current")
_FadDot1agCfmMepTable_Object = MibTable
fadDot1agCfmMepTable = _FadDot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4)
)
if mibBuilder.loadTexts:
    fadDot1agCfmMepTable.setStatus("current")
_FadDot1agCfmMepEntry_Object = MibTableRow
fadDot1agCfmMepEntry = _FadDot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1)
)
if mibBuilder.loadTexts:
    fadDot1agCfmMepEntry.setStatus("current")


class _FadDot1agCfmMpSvcId_Type(TmnxServId):
    """Custom type fadDot1agCfmMpSvcId based on TmnxServId"""
    defaultValue = 0


_FadDot1agCfmMpSvcId_Type.__name__ = "TmnxServId"
_FadDot1agCfmMpSvcId_Object = MibTableColumn
fadDot1agCfmMpSvcId = _FadDot1agCfmMpSvcId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 1),
    _FadDot1agCfmMpSvcId_Type()
)
fadDot1agCfmMpSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMpSvcId.setStatus("current")


class _FadDot1agCfmMepLbmTestTlvIncluded_Type(TruthValue):
    """Custom type fadDot1agCfmMepLbmTestTlvIncluded based on TruthValue"""
    defaultValue = 2


_FadDot1agCfmMepLbmTestTlvIncluded_Type.__name__ = "TruthValue"
_FadDot1agCfmMepLbmTestTlvIncluded_Object = MibTableColumn
fadDot1agCfmMepLbmTestTlvIncluded = _FadDot1agCfmMepLbmTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 2),
    _FadDot1agCfmMepLbmTestTlvIncluded_Type()
)
fadDot1agCfmMepLbmTestTlvIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLbmTestTlvIncluded.setStatus("current")


class _FadDot1agCfmMepLbmTestPattern_Type(Integer32):
    """Custom type fadDot1agCfmMepLbmTestPattern based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allZerosNoCrc", 0),
          ("allZerosCrc", 1),
          ("prbsNoCrc", 2),
          ("prbsCrc", 3),
          ("allOnesNoCrc", 4),
          ("allOnesCrc", 5))
    )


_FadDot1agCfmMepLbmTestPattern_Type.__name__ = "Integer32"
_FadDot1agCfmMepLbmTestPattern_Object = MibTableColumn
fadDot1agCfmMepLbmTestPattern = _FadDot1agCfmMepLbmTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 3),
    _FadDot1agCfmMepLbmTestPattern_Type()
)
fadDot1agCfmMepLbmTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLbmTestPattern.setStatus("current")


class _FadDot1agCfmMepTransmitLbmTestTlvLen_Type(Unsigned32):
    """Custom type fadDot1agCfmMepTransmitLbmTestTlvLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_FadDot1agCfmMepTransmitLbmTestTlvLen_Type.__name__ = "Unsigned32"
_FadDot1agCfmMepTransmitLbmTestTlvLen_Object = MibTableColumn
fadDot1agCfmMepTransmitLbmTestTlvLen = _FadDot1agCfmMepTransmitLbmTestTlvLen_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 4),
    _FadDot1agCfmMepTransmitLbmTestTlvLen_Type()
)
fadDot1agCfmMepTransmitLbmTestTlvLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadDot1agCfmMepTransmitLbmTestTlvLen.setStatus("current")
_FadDot1agCfmMepLbrInBitErrors_Type = Counter32
_FadDot1agCfmMepLbrInBitErrors_Object = MibTableColumn
fadDot1agCfmMepLbrInBitErrors = _FadDot1agCfmMepLbrInBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 5),
    _FadDot1agCfmMepLbrInBitErrors_Type()
)
fadDot1agCfmMepLbrInBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLbrInBitErrors.setStatus("current")
_FadDot1agCfmMepLbrInCrcErrors_Type = Counter32
_FadDot1agCfmMepLbrInCrcErrors_Object = MibTableColumn
fadDot1agCfmMepLbrInCrcErrors = _FadDot1agCfmMepLbrInCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 6),
    _FadDot1agCfmMepLbrInCrcErrors_Type()
)
fadDot1agCfmMepLbrInCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLbrInCrcErrors.setStatus("current")


class _FadDot1agCfmMepY1731PmEnabled_Type(TruthValue):
    """Custom type fadDot1agCfmMepY1731PmEnabled based on TruthValue"""
    defaultValue = 2


_FadDot1agCfmMepY1731PmEnabled_Type.__name__ = "TruthValue"
_FadDot1agCfmMepY1731PmEnabled_Object = MibTableColumn
fadDot1agCfmMepY1731PmEnabled = _FadDot1agCfmMepY1731PmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 7),
    _FadDot1agCfmMepY1731PmEnabled_Type()
)
fadDot1agCfmMepY1731PmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadDot1agCfmMepY1731PmEnabled.setStatus("current")


class _FadDot1agCfmMepY1731SingleLMPriorityBmp_Type(Integer32):
    """Custom type fadDot1agCfmMepY1731SingleLMPriorityBmp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_FadDot1agCfmMepY1731SingleLMPriorityBmp_Type.__name__ = "Integer32"
_FadDot1agCfmMepY1731SingleLMPriorityBmp_Object = MibTableColumn
fadDot1agCfmMepY1731SingleLMPriorityBmp = _FadDot1agCfmMepY1731SingleLMPriorityBmp_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 8),
    _FadDot1agCfmMepY1731SingleLMPriorityBmp_Type()
)
fadDot1agCfmMepY1731SingleLMPriorityBmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadDot1agCfmMepY1731SingleLMPriorityBmp.setStatus("current")


class _FadDot1agCfmMepSingleLMMacAddress_Type(MacAddress):
    """Custom type fadDot1agCfmMepSingleLMMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_FadDot1agCfmMepSingleLMMacAddress_Type.__name__ = "MacAddress"
_FadDot1agCfmMepSingleLMMacAddress_Object = MibTableColumn
fadDot1agCfmMepSingleLMMacAddress = _FadDot1agCfmMepSingleLMMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 9),
    _FadDot1agCfmMepSingleLMMacAddress_Type()
)
fadDot1agCfmMepSingleLMMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadDot1agCfmMepSingleLMMacAddress.setStatus("current")


class _FadDot1agCfmMepSingleLMPriority_Type(Unsigned32):
    """Custom type fadDot1agCfmMepSingleLMPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FadDot1agCfmMepSingleLMPriority_Type.__name__ = "Unsigned32"
_FadDot1agCfmMepSingleLMPriority_Object = MibTableColumn
fadDot1agCfmMepSingleLMPriority = _FadDot1agCfmMepSingleLMPriority_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 10),
    _FadDot1agCfmMepSingleLMPriority_Type()
)
fadDot1agCfmMepSingleLMPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadDot1agCfmMepSingleLMPriority.setStatus("current")


class _FadDot1agCfmMepSingleLMCount_Type(Unsigned32):
    """Custom type fadDot1agCfmMepSingleLMCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_FadDot1agCfmMepSingleLMCount_Type.__name__ = "Unsigned32"
_FadDot1agCfmMepSingleLMCount_Object = MibTableColumn
fadDot1agCfmMepSingleLMCount = _FadDot1agCfmMepSingleLMCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 11),
    _FadDot1agCfmMepSingleLMCount_Type()
)
fadDot1agCfmMepSingleLMCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadDot1agCfmMepSingleLMCount.setStatus("current")


class _FadDot1agCfmMepSingleLMInterval_Type(Unsigned32):
    """Custom type fadDot1agCfmMepSingleLMInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000),
    )


_FadDot1agCfmMepSingleLMInterval_Type.__name__ = "Unsigned32"
_FadDot1agCfmMepSingleLMInterval_Object = MibTableColumn
fadDot1agCfmMepSingleLMInterval = _FadDot1agCfmMepSingleLMInterval_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 4, 1, 12),
    _FadDot1agCfmMepSingleLMInterval_Type()
)
fadDot1agCfmMepSingleLMInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadDot1agCfmMepSingleLMInterval.setStatus("current")
if mibBuilder.loadTexts:
    fadDot1agCfmMepSingleLMInterval.setUnits("milliseconds")
_FadDot1agCfmSapMipTable_Object = MibTable
fadDot1agCfmSapMipTable = _FadDot1agCfmSapMipTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 5)
)
if mibBuilder.loadTexts:
    fadDot1agCfmSapMipTable.setStatus("current")
_FadDot1agCfmSapMipEntry_Object = MibTableRow
fadDot1agCfmSapMipEntry = _FadDot1agCfmSapMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 5, 1)
)
if mibBuilder.loadTexts:
    fadDot1agCfmSapMipEntry.setStatus("current")


class _FadDot1agCfmMipSvcId_Type(TmnxServId):
    """Custom type fadDot1agCfmMipSvcId based on TmnxServId"""
    defaultValue = 0


_FadDot1agCfmMipSvcId_Type.__name__ = "TmnxServId"
_FadDot1agCfmMipSvcId_Object = MibTableColumn
fadDot1agCfmMipSvcId = _FadDot1agCfmMipSvcId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 5, 1, 1),
    _FadDot1agCfmMipSvcId_Type()
)
fadDot1agCfmMipSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMipSvcId.setStatus("current")


class _FadY1731CfmNextFreeSessionId_Type(Integer32):
    """Custom type fadY1731CfmNextFreeSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_FadY1731CfmNextFreeSessionId_Type.__name__ = "Integer32"
_FadY1731CfmNextFreeSessionId_Object = MibScalar
fadY1731CfmNextFreeSessionId = _FadY1731CfmNextFreeSessionId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 6),
    _FadY1731CfmNextFreeSessionId_Type()
)
fadY1731CfmNextFreeSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmNextFreeSessionId.setStatus("current")
_FadY1731CfmPMConfigTable_Object = MibTable
fadY1731CfmPMConfigTable = _FadY1731CfmPMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigTable.setStatus("current")
_FadY1731CfmPMConfigEntry_Object = MibTableRow
fadY1731CfmPMConfigEntry = _FadY1731CfmPMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1)
)
fadY1731CfmPMConfigEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigEntry.setStatus("current")


class _FadY1731CfmPMConfigSessionId_Type(Integer32):
    """Custom type fadY1731CfmPMConfigSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_FadY1731CfmPMConfigSessionId_Type.__name__ = "Integer32"
_FadY1731CfmPMConfigSessionId_Object = MibTableColumn
fadY1731CfmPMConfigSessionId = _FadY1731CfmPMConfigSessionId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 1),
    _FadY1731CfmPMConfigSessionId_Type()
)
fadY1731CfmPMConfigSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigSessionId.setStatus("current")
_FadY1731CfmPMConfigRowStatus_Type = RowStatus
_FadY1731CfmPMConfigRowStatus_Object = MibTableColumn
fadY1731CfmPMConfigRowStatus = _FadY1731CfmPMConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 2),
    _FadY1731CfmPMConfigRowStatus_Type()
)
fadY1731CfmPMConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigRowStatus.setStatus("current")


class _FadY1731CfmPMConfigMepMacAddress_Type(MacAddress):
    """Custom type fadY1731CfmPMConfigMepMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_FadY1731CfmPMConfigMepMacAddress_Type.__name__ = "MacAddress"
_FadY1731CfmPMConfigMepMacAddress_Object = MibTableColumn
fadY1731CfmPMConfigMepMacAddress = _FadY1731CfmPMConfigMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 3),
    _FadY1731CfmPMConfigMepMacAddress_Type()
)
fadY1731CfmPMConfigMepMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigMepMacAddress.setStatus("current")


class _FadY1731CfmPMConfigType_Type(EthCfmY1731PMType):
    """Custom type fadY1731CfmPMConfigType based on EthCfmY1731PMType"""
    defaultValue = 0


_FadY1731CfmPMConfigType_Type.__name__ = "EthCfmY1731PMType"
_FadY1731CfmPMConfigType_Object = MibTableColumn
fadY1731CfmPMConfigType = _FadY1731CfmPMConfigType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 4),
    _FadY1731CfmPMConfigType_Type()
)
fadY1731CfmPMConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigType.setStatus("current")


class _FadY1731CfmPMConfigAdminStatus_Type(Integer32):
    """Custom type fadY1731CfmPMConfigAdminStatus based on Integer32"""
    defaultValue = 2

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


_FadY1731CfmPMConfigAdminStatus_Type.__name__ = "Integer32"
_FadY1731CfmPMConfigAdminStatus_Object = MibTableColumn
fadY1731CfmPMConfigAdminStatus = _FadY1731CfmPMConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 5),
    _FadY1731CfmPMConfigAdminStatus_Type()
)
fadY1731CfmPMConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigAdminStatus.setStatus("current")


class _FadY1731CfmPMConfigPriority_Type(Unsigned32):
    """Custom type fadY1731CfmPMConfigPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FadY1731CfmPMConfigPriority_Type.__name__ = "Unsigned32"
_FadY1731CfmPMConfigPriority_Object = MibTableColumn
fadY1731CfmPMConfigPriority = _FadY1731CfmPMConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 6),
    _FadY1731CfmPMConfigPriority_Type()
)
fadY1731CfmPMConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigPriority.setStatus("current")


class _FadY1731CfmPMConfigInterval_Type(Unsigned32):
    """Custom type fadY1731CfmPMConfigInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(60, 300),
    )


_FadY1731CfmPMConfigInterval_Type.__name__ = "Unsigned32"
_FadY1731CfmPMConfigInterval_Object = MibTableColumn
fadY1731CfmPMConfigInterval = _FadY1731CfmPMConfigInterval_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 7),
    _FadY1731CfmPMConfigInterval_Type()
)
fadY1731CfmPMConfigInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigInterval.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigInterval.setUnits("seconds")


class _FadY1731CfmPMConfigMeasurementInterval_Type(Unsigned32):
    """Custom type fadY1731CfmPMConfigMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(300, 300),
    )


_FadY1731CfmPMConfigMeasurementInterval_Type.__name__ = "Unsigned32"
_FadY1731CfmPMConfigMeasurementInterval_Object = MibTableColumn
fadY1731CfmPMConfigMeasurementInterval = _FadY1731CfmPMConfigMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 8),
    _FadY1731CfmPMConfigMeasurementInterval_Type()
)
fadY1731CfmPMConfigMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigMeasurementInterval.setUnits("seconds")


class _FadY1731CfmPMConfigDataSize_Type(Unsigned32):
    """Custom type fadY1731CfmPMConfigDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_FadY1731CfmPMConfigDataSize_Type.__name__ = "Unsigned32"
_FadY1731CfmPMConfigDataSize_Object = MibTableColumn
fadY1731CfmPMConfigDataSize = _FadY1731CfmPMConfigDataSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 7, 1, 9),
    _FadY1731CfmPMConfigDataSize_Type()
)
fadY1731CfmPMConfigDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigDataSize.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMConfigDataSize.setUnits("octets")
_FadY1731CfmPMCurrent15MinIntervalLossTable_Object = MibTable
fadY1731CfmPMCurrent15MinIntervalLossTable = _FadY1731CfmPMCurrent15MinIntervalLossTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinIntervalLossTable.setStatus("current")
_FadY1731CfmPMCurrent15MinIntervalLossEntry_Object = MibTableRow
fadY1731CfmPMCurrent15MinIntervalLossEntry = _FadY1731CfmPMCurrent15MinIntervalLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1)
)
fadY1731CfmPMCurrent15MinIntervalLossEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinIntervalLossEntry.setStatus("current")
_FadY1731CfmPMCurrent15MinTestType_Type = EthCfmY1731PMType
_FadY1731CfmPMCurrent15MinTestType_Object = MibTableColumn
fadY1731CfmPMCurrent15MinTestType = _FadY1731CfmPMCurrent15MinTestType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 1),
    _FadY1731CfmPMCurrent15MinTestType_Type()
)
fadY1731CfmPMCurrent15MinTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinTestType.setStatus("current")


class _FadY1731CfmPMCurrent15MinTimeElapsed_Type(Integer32):
    """Custom type fadY1731CfmPMCurrent15MinTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadY1731CfmPMCurrent15MinTimeElapsed_Type.__name__ = "Integer32"
_FadY1731CfmPMCurrent15MinTimeElapsed_Object = MibTableColumn
fadY1731CfmPMCurrent15MinTimeElapsed = _FadY1731CfmPMCurrent15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 2),
    _FadY1731CfmPMCurrent15MinTimeElapsed_Type()
)
fadY1731CfmPMCurrent15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinTimeElapsed.setStatus("current")


class _FadY1731CfmPMCurrent15MinTimeMeasured_Type(Integer32):
    """Custom type fadY1731CfmPMCurrent15MinTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadY1731CfmPMCurrent15MinTimeMeasured_Type.__name__ = "Integer32"
_FadY1731CfmPMCurrent15MinTimeMeasured_Object = MibTableColumn
fadY1731CfmPMCurrent15MinTimeMeasured = _FadY1731CfmPMCurrent15MinTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 3),
    _FadY1731CfmPMCurrent15MinTimeMeasured_Type()
)
fadY1731CfmPMCurrent15MinTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinTimeMeasured.setStatus("current")


class _FadY1731CfmPM15MinValidIntervals_Type(Integer32):
    """Custom type fadY1731CfmPM15MinValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_FadY1731CfmPM15MinValidIntervals_Type.__name__ = "Integer32"
_FadY1731CfmPM15MinValidIntervals_Object = MibTableColumn
fadY1731CfmPM15MinValidIntervals = _FadY1731CfmPM15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 4),
    _FadY1731CfmPM15MinValidIntervals_Type()
)
fadY1731CfmPM15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPM15MinValidIntervals.setStatus("current")
_FadY1731CfmPMCurrent15MinInvalidDataFlag_Type = TruthValue
_FadY1731CfmPMCurrent15MinInvalidDataFlag_Object = MibTableColumn
fadY1731CfmPMCurrent15MinInvalidDataFlag = _FadY1731CfmPMCurrent15MinInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 5),
    _FadY1731CfmPMCurrent15MinInvalidDataFlag_Type()
)
fadY1731CfmPMCurrent15MinInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinInvalidDataFlag.setStatus("current")
_FadY1731CfmPMCurrent15MinPDUSent_Type = Counter32
_FadY1731CfmPMCurrent15MinPDUSent_Object = MibTableColumn
fadY1731CfmPMCurrent15MinPDUSent = _FadY1731CfmPMCurrent15MinPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 6),
    _FadY1731CfmPMCurrent15MinPDUSent_Type()
)
fadY1731CfmPMCurrent15MinPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinPDUSent.setStatus("current")
_FadY1731CfmPMCurrent15MinPDURecv_Type = Counter32
_FadY1731CfmPMCurrent15MinPDURecv_Object = MibTableColumn
fadY1731CfmPMCurrent15MinPDURecv = _FadY1731CfmPMCurrent15MinPDURecv_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 7),
    _FadY1731CfmPMCurrent15MinPDURecv_Type()
)
fadY1731CfmPMCurrent15MinPDURecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinPDURecv.setStatus("current")
_FadY1731CfmPMCurrent15MinRxLocal_Type = Counter64
_FadY1731CfmPMCurrent15MinRxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinRxLocal = _FadY1731CfmPMCurrent15MinRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 8),
    _FadY1731CfmPMCurrent15MinRxLocal_Type()
)
fadY1731CfmPMCurrent15MinRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinRxLocal.setStatus("current")
_FadY1731CfmPMCurrent15MinRxPeer_Type = Counter64
_FadY1731CfmPMCurrent15MinRxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinRxPeer = _FadY1731CfmPMCurrent15MinRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 9),
    _FadY1731CfmPMCurrent15MinRxPeer_Type()
)
fadY1731CfmPMCurrent15MinRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinRxPeer.setStatus("current")
_FadY1731CfmPMCurrent15MinTxLocal_Type = Counter64
_FadY1731CfmPMCurrent15MinTxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinTxLocal = _FadY1731CfmPMCurrent15MinTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 10),
    _FadY1731CfmPMCurrent15MinTxLocal_Type()
)
fadY1731CfmPMCurrent15MinTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinTxLocal.setStatus("current")
_FadY1731CfmPMCurrent15MinTxPeer_Type = Counter64
_FadY1731CfmPMCurrent15MinTxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinTxPeer = _FadY1731CfmPMCurrent15MinTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 11),
    _FadY1731CfmPMCurrent15MinTxPeer_Type()
)
fadY1731CfmPMCurrent15MinTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinTxPeer.setStatus("current")
_FadY1731CfmPMCurrent15MinLossLocal_Type = Counter64
_FadY1731CfmPMCurrent15MinLossLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinLossLocal = _FadY1731CfmPMCurrent15MinLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 12),
    _FadY1731CfmPMCurrent15MinLossLocal_Type()
)
fadY1731CfmPMCurrent15MinLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossLocal.setStatus("current")
_FadY1731CfmPMCurrent15MinLossPeer_Type = Counter64
_FadY1731CfmPMCurrent15MinLossPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinLossPeer = _FadY1731CfmPMCurrent15MinLossPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 13),
    _FadY1731CfmPMCurrent15MinLossPeer_Type()
)
fadY1731CfmPMCurrent15MinLossPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossPeer.setStatus("current")
_FadY1731CfmPMCurrent15MinLossRatioMinLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent15MinLossRatioMinLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinLossRatioMinLocal = _FadY1731CfmPMCurrent15MinLossRatioMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 14),
    _FadY1731CfmPMCurrent15MinLossRatioMinLocal_Type()
)
fadY1731CfmPMCurrent15MinLossRatioMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioMinLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent15MinLossRatioMaxLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent15MinLossRatioMaxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinLossRatioMaxLocal = _FadY1731CfmPMCurrent15MinLossRatioMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 15),
    _FadY1731CfmPMCurrent15MinLossRatioMaxLocal_Type()
)
fadY1731CfmPMCurrent15MinLossRatioMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioMaxLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent15MinLossRatioAvgLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent15MinLossRatioAvgLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinLossRatioAvgLocal = _FadY1731CfmPMCurrent15MinLossRatioAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 16),
    _FadY1731CfmPMCurrent15MinLossRatioAvgLocal_Type()
)
fadY1731CfmPMCurrent15MinLossRatioAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioAvgLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent15MinLossRatioMinPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent15MinLossRatioMinPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinLossRatioMinPeer = _FadY1731CfmPMCurrent15MinLossRatioMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 17),
    _FadY1731CfmPMCurrent15MinLossRatioMinPeer_Type()
)
fadY1731CfmPMCurrent15MinLossRatioMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioMinPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent15MinLossRatioMaxPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent15MinLossRatioMaxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinLossRatioMaxPeer = _FadY1731CfmPMCurrent15MinLossRatioMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 18),
    _FadY1731CfmPMCurrent15MinLossRatioMaxPeer_Type()
)
fadY1731CfmPMCurrent15MinLossRatioMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioMaxPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent15MinLossRatioAvgPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent15MinLossRatioAvgPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinLossRatioAvgPeer = _FadY1731CfmPMCurrent15MinLossRatioAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 19),
    _FadY1731CfmPMCurrent15MinLossRatioAvgPeer_Type()
)
fadY1731CfmPMCurrent15MinLossRatioAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinLossRatioAvgPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent15MinTestId_Type = Unsigned32
_FadY1731CfmPMCurrent15MinTestId_Object = MibTableColumn
fadY1731CfmPMCurrent15MinTestId = _FadY1731CfmPMCurrent15MinTestId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 20),
    _FadY1731CfmPMCurrent15MinTestId_Type()
)
fadY1731CfmPMCurrent15MinTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinTestId.setStatus("current")
_FadY1731CfmPMCurrent15MinRemoteMepId_Type = Dot1agCfmMepId
_FadY1731CfmPMCurrent15MinRemoteMepId_Object = MibTableColumn
fadY1731CfmPMCurrent15MinRemoteMepId = _FadY1731CfmPMCurrent15MinRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 21),
    _FadY1731CfmPMCurrent15MinRemoteMepId_Type()
)
fadY1731CfmPMCurrent15MinRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinRemoteMepId.setStatus("current")
_FadY1731CfmPMCurrent15MinUnack_Type = Counter32
_FadY1731CfmPMCurrent15MinUnack_Object = MibTableColumn
fadY1731CfmPMCurrent15MinUnack = _FadY1731CfmPMCurrent15MinUnack_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 22),
    _FadY1731CfmPMCurrent15MinUnack_Type()
)
fadY1731CfmPMCurrent15MinUnack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinUnack.setStatus("current")
_FadY1731CfmPMCurrent15MinPDUDiscarded_Type = Counter32
_FadY1731CfmPMCurrent15MinPDUDiscarded_Object = MibTableColumn
fadY1731CfmPMCurrent15MinPDUDiscarded = _FadY1731CfmPMCurrent15MinPDUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 23),
    _FadY1731CfmPMCurrent15MinPDUDiscarded_Type()
)
fadY1731CfmPMCurrent15MinPDUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinPDUDiscarded.setStatus("current")


class _FadY1731CfmPMCurrent15MinDataSize_Type(Unsigned32):
    """Custom type fadY1731CfmPMCurrent15MinDataSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_FadY1731CfmPMCurrent15MinDataSize_Type.__name__ = "Unsigned32"
_FadY1731CfmPMCurrent15MinDataSize_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDataSize = _FadY1731CfmPMCurrent15MinDataSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 8, 1, 24),
    _FadY1731CfmPMCurrent15MinDataSize_Type()
)
fadY1731CfmPMCurrent15MinDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDataSize.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDataSize.setUnits("octets")
_FadY1731CfmPMCurrent1DayIntervalLossTable_Object = MibTable
fadY1731CfmPMCurrent1DayIntervalLossTable = _FadY1731CfmPMCurrent1DayIntervalLossTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayIntervalLossTable.setStatus("current")
_FadY1731CfmPMCurrent1DayIntervalLossEntry_Object = MibTableRow
fadY1731CfmPMCurrent1DayIntervalLossEntry = _FadY1731CfmPMCurrent1DayIntervalLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1)
)
fadY1731CfmPMCurrent1DayIntervalLossEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayIntervalLossEntry.setStatus("current")
_FadY1731CfmPMCurrent1DayTestType_Type = EthCfmY1731PMType
_FadY1731CfmPMCurrent1DayTestType_Object = MibTableColumn
fadY1731CfmPMCurrent1DayTestType = _FadY1731CfmPMCurrent1DayTestType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 1),
    _FadY1731CfmPMCurrent1DayTestType_Type()
)
fadY1731CfmPMCurrent1DayTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayTestType.setStatus("current")


class _FadY1731CfmPMCurrent1DayTimeElapsed_Type(Integer32):
    """Custom type fadY1731CfmPMCurrent1DayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadY1731CfmPMCurrent1DayTimeElapsed_Type.__name__ = "Integer32"
_FadY1731CfmPMCurrent1DayTimeElapsed_Object = MibTableColumn
fadY1731CfmPMCurrent1DayTimeElapsed = _FadY1731CfmPMCurrent1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 2),
    _FadY1731CfmPMCurrent1DayTimeElapsed_Type()
)
fadY1731CfmPMCurrent1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayTimeElapsed.setStatus("current")


class _FadY1731CfmPMCurrent1DayTimeMeasured_Type(Integer32):
    """Custom type fadY1731CfmPMCurrent1DayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadY1731CfmPMCurrent1DayTimeMeasured_Type.__name__ = "Integer32"
_FadY1731CfmPMCurrent1DayTimeMeasured_Object = MibTableColumn
fadY1731CfmPMCurrent1DayTimeMeasured = _FadY1731CfmPMCurrent1DayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 3),
    _FadY1731CfmPMCurrent1DayTimeMeasured_Type()
)
fadY1731CfmPMCurrent1DayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayTimeMeasured.setStatus("current")


class _FadY1731CfmPM1DayValidIntervals_Type(Integer32):
    """Custom type fadY1731CfmPM1DayValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FadY1731CfmPM1DayValidIntervals_Type.__name__ = "Integer32"
_FadY1731CfmPM1DayValidIntervals_Object = MibTableColumn
fadY1731CfmPM1DayValidIntervals = _FadY1731CfmPM1DayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 4),
    _FadY1731CfmPM1DayValidIntervals_Type()
)
fadY1731CfmPM1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPM1DayValidIntervals.setStatus("current")
_FadY1731CfmPMCurrent1DayInvalidDataFlag_Type = TruthValue
_FadY1731CfmPMCurrent1DayInvalidDataFlag_Object = MibTableColumn
fadY1731CfmPMCurrent1DayInvalidDataFlag = _FadY1731CfmPMCurrent1DayInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 5),
    _FadY1731CfmPMCurrent1DayInvalidDataFlag_Type()
)
fadY1731CfmPMCurrent1DayInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayInvalidDataFlag.setStatus("current")
_FadY1731CfmPMCurrent1DayPDUSent_Type = Counter32
_FadY1731CfmPMCurrent1DayPDUSent_Object = MibTableColumn
fadY1731CfmPMCurrent1DayPDUSent = _FadY1731CfmPMCurrent1DayPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 6),
    _FadY1731CfmPMCurrent1DayPDUSent_Type()
)
fadY1731CfmPMCurrent1DayPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayPDUSent.setStatus("current")
_FadY1731CfmPMCurrent1DayPDURecv_Type = Counter32
_FadY1731CfmPMCurrent1DayPDURecv_Object = MibTableColumn
fadY1731CfmPMCurrent1DayPDURecv = _FadY1731CfmPMCurrent1DayPDURecv_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 7),
    _FadY1731CfmPMCurrent1DayPDURecv_Type()
)
fadY1731CfmPMCurrent1DayPDURecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayPDURecv.setStatus("current")
_FadY1731CfmPMCurrent1DayRxLocal_Type = Counter64
_FadY1731CfmPMCurrent1DayRxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayRxLocal = _FadY1731CfmPMCurrent1DayRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 8),
    _FadY1731CfmPMCurrent1DayRxLocal_Type()
)
fadY1731CfmPMCurrent1DayRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayRxLocal.setStatus("current")
_FadY1731CfmPMCurrent1DayRxPeer_Type = Counter64
_FadY1731CfmPMCurrent1DayRxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayRxPeer = _FadY1731CfmPMCurrent1DayRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 9),
    _FadY1731CfmPMCurrent1DayRxPeer_Type()
)
fadY1731CfmPMCurrent1DayRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayRxPeer.setStatus("current")
_FadY1731CfmPMCurrent1DayTxLocal_Type = Counter64
_FadY1731CfmPMCurrent1DayTxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayTxLocal = _FadY1731CfmPMCurrent1DayTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 10),
    _FadY1731CfmPMCurrent1DayTxLocal_Type()
)
fadY1731CfmPMCurrent1DayTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayTxLocal.setStatus("current")
_FadY1731CfmPMCurrent1DayTxPeer_Type = Counter64
_FadY1731CfmPMCurrent1DayTxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayTxPeer = _FadY1731CfmPMCurrent1DayTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 11),
    _FadY1731CfmPMCurrent1DayTxPeer_Type()
)
fadY1731CfmPMCurrent1DayTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayTxPeer.setStatus("current")
_FadY1731CfmPMCurrent1DayLossLocal_Type = Counter64
_FadY1731CfmPMCurrent1DayLossLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayLossLocal = _FadY1731CfmPMCurrent1DayLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 12),
    _FadY1731CfmPMCurrent1DayLossLocal_Type()
)
fadY1731CfmPMCurrent1DayLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossLocal.setStatus("current")
_FadY1731CfmPMCurrent1DayLossPeer_Type = Counter64
_FadY1731CfmPMCurrent1DayLossPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayLossPeer = _FadY1731CfmPMCurrent1DayLossPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 13),
    _FadY1731CfmPMCurrent1DayLossPeer_Type()
)
fadY1731CfmPMCurrent1DayLossPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossPeer.setStatus("current")
_FadY1731CfmPMCurrent1DayLossRatioMinLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent1DayLossRatioMinLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayLossRatioMinLocal = _FadY1731CfmPMCurrent1DayLossRatioMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 14),
    _FadY1731CfmPMCurrent1DayLossRatioMinLocal_Type()
)
fadY1731CfmPMCurrent1DayLossRatioMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioMinLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent1DayLossRatioMaxLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent1DayLossRatioMaxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayLossRatioMaxLocal = _FadY1731CfmPMCurrent1DayLossRatioMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 15),
    _FadY1731CfmPMCurrent1DayLossRatioMaxLocal_Type()
)
fadY1731CfmPMCurrent1DayLossRatioMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioMaxLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent1DayLossRatioAvgLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent1DayLossRatioAvgLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayLossRatioAvgLocal = _FadY1731CfmPMCurrent1DayLossRatioAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 16),
    _FadY1731CfmPMCurrent1DayLossRatioAvgLocal_Type()
)
fadY1731CfmPMCurrent1DayLossRatioAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioAvgLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent1DayLossRatioMinPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent1DayLossRatioMinPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayLossRatioMinPeer = _FadY1731CfmPMCurrent1DayLossRatioMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 17),
    _FadY1731CfmPMCurrent1DayLossRatioMinPeer_Type()
)
fadY1731CfmPMCurrent1DayLossRatioMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioMinPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent1DayLossRatioMaxPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent1DayLossRatioMaxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayLossRatioMaxPeer = _FadY1731CfmPMCurrent1DayLossRatioMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 18),
    _FadY1731CfmPMCurrent1DayLossRatioMaxPeer_Type()
)
fadY1731CfmPMCurrent1DayLossRatioMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioMaxPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent1DayLossRatioAvgPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMCurrent1DayLossRatioAvgPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayLossRatioAvgPeer = _FadY1731CfmPMCurrent1DayLossRatioAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 19),
    _FadY1731CfmPMCurrent1DayLossRatioAvgPeer_Type()
)
fadY1731CfmPMCurrent1DayLossRatioAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayLossRatioAvgPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMCurrent1DayTestId_Type = Unsigned32
_FadY1731CfmPMCurrent1DayTestId_Object = MibTableColumn
fadY1731CfmPMCurrent1DayTestId = _FadY1731CfmPMCurrent1DayTestId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 20),
    _FadY1731CfmPMCurrent1DayTestId_Type()
)
fadY1731CfmPMCurrent1DayTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayTestId.setStatus("current")
_FadY1731CfmPMCurrent1DayRemoteMepId_Type = Dot1agCfmMepId
_FadY1731CfmPMCurrent1DayRemoteMepId_Object = MibTableColumn
fadY1731CfmPMCurrent1DayRemoteMepId = _FadY1731CfmPMCurrent1DayRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 21),
    _FadY1731CfmPMCurrent1DayRemoteMepId_Type()
)
fadY1731CfmPMCurrent1DayRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayRemoteMepId.setStatus("current")
_FadY1731CfmPMCurrent1DayUnack_Type = Counter32
_FadY1731CfmPMCurrent1DayUnack_Object = MibTableColumn
fadY1731CfmPMCurrent1DayUnack = _FadY1731CfmPMCurrent1DayUnack_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 22),
    _FadY1731CfmPMCurrent1DayUnack_Type()
)
fadY1731CfmPMCurrent1DayUnack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayUnack.setStatus("current")
_FadY1731CfmPMCurrent1DayPDUDiscarded_Type = Counter32
_FadY1731CfmPMCurrent1DayPDUDiscarded_Object = MibTableColumn
fadY1731CfmPMCurrent1DayPDUDiscarded = _FadY1731CfmPMCurrent1DayPDUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 23),
    _FadY1731CfmPMCurrent1DayPDUDiscarded_Type()
)
fadY1731CfmPMCurrent1DayPDUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayPDUDiscarded.setStatus("current")


class _FadY1731CfmPMCurrent1DayDataSize_Type(Unsigned32):
    """Custom type fadY1731CfmPMCurrent1DayDataSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_FadY1731CfmPMCurrent1DayDataSize_Type.__name__ = "Unsigned32"
_FadY1731CfmPMCurrent1DayDataSize_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDataSize = _FadY1731CfmPMCurrent1DayDataSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 9, 1, 24),
    _FadY1731CfmPMCurrent1DayDataSize_Type()
)
fadY1731CfmPMCurrent1DayDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDataSize.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDataSize.setUnits("octets")
_FadY1731CfmPMPrevious15MinIntervalLossTable_Object = MibTable
fadY1731CfmPMPrevious15MinIntervalLossTable = _FadY1731CfmPMPrevious15MinIntervalLossTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinIntervalLossTable.setStatus("current")
_FadY1731CfmPMPrevious15MinIntervalLossEntry_Object = MibTableRow
fadY1731CfmPMPrevious15MinIntervalLossEntry = _FadY1731CfmPMPrevious15MinIntervalLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1)
)
fadY1731CfmPMPrevious15MinIntervalLossEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMPrevious15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinIntervalLossEntry.setStatus("current")


class _FadY1731CfmPMPrevious15MinIntervalNumber_Type(Integer32):
    """Custom type fadY1731CfmPMPrevious15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_FadY1731CfmPMPrevious15MinIntervalNumber_Type.__name__ = "Integer32"
_FadY1731CfmPMPrevious15MinIntervalNumber_Object = MibTableColumn
fadY1731CfmPMPrevious15MinIntervalNumber = _FadY1731CfmPMPrevious15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 1),
    _FadY1731CfmPMPrevious15MinIntervalNumber_Type()
)
fadY1731CfmPMPrevious15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinIntervalNumber.setStatus("current")
_FadY1731CfmPMPrevious15MinTestType_Type = EthCfmY1731PMType
_FadY1731CfmPMPrevious15MinTestType_Object = MibTableColumn
fadY1731CfmPMPrevious15MinTestType = _FadY1731CfmPMPrevious15MinTestType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 2),
    _FadY1731CfmPMPrevious15MinTestType_Type()
)
fadY1731CfmPMPrevious15MinTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinTestType.setStatus("current")


class _FadY1731CfmPMPrevious15MinTimeMeasured_Type(Integer32):
    """Custom type fadY1731CfmPMPrevious15MinTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadY1731CfmPMPrevious15MinTimeMeasured_Type.__name__ = "Integer32"
_FadY1731CfmPMPrevious15MinTimeMeasured_Object = MibTableColumn
fadY1731CfmPMPrevious15MinTimeMeasured = _FadY1731CfmPMPrevious15MinTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 3),
    _FadY1731CfmPMPrevious15MinTimeMeasured_Type()
)
fadY1731CfmPMPrevious15MinTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinTimeMeasured.setStatus("current")
_FadY1731CfmPMPrevious15MinInvalidDataFlag_Type = TruthValue
_FadY1731CfmPMPrevious15MinInvalidDataFlag_Object = MibTableColumn
fadY1731CfmPMPrevious15MinInvalidDataFlag = _FadY1731CfmPMPrevious15MinInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 4),
    _FadY1731CfmPMPrevious15MinInvalidDataFlag_Type()
)
fadY1731CfmPMPrevious15MinInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinInvalidDataFlag.setStatus("current")
_FadY1731CfmPMPrevious15MinPDUSent_Type = Counter32
_FadY1731CfmPMPrevious15MinPDUSent_Object = MibTableColumn
fadY1731CfmPMPrevious15MinPDUSent = _FadY1731CfmPMPrevious15MinPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 5),
    _FadY1731CfmPMPrevious15MinPDUSent_Type()
)
fadY1731CfmPMPrevious15MinPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinPDUSent.setStatus("current")
_FadY1731CfmPMPrevious15MinPDURecv_Type = Counter32
_FadY1731CfmPMPrevious15MinPDURecv_Object = MibTableColumn
fadY1731CfmPMPrevious15MinPDURecv = _FadY1731CfmPMPrevious15MinPDURecv_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 6),
    _FadY1731CfmPMPrevious15MinPDURecv_Type()
)
fadY1731CfmPMPrevious15MinPDURecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinPDURecv.setStatus("current")
_FadY1731CfmPMPrevious15MinRxLocal_Type = Counter64
_FadY1731CfmPMPrevious15MinRxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinRxLocal = _FadY1731CfmPMPrevious15MinRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 7),
    _FadY1731CfmPMPrevious15MinRxLocal_Type()
)
fadY1731CfmPMPrevious15MinRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinRxLocal.setStatus("current")
_FadY1731CfmPMPrevious15MinRxPeer_Type = Counter64
_FadY1731CfmPMPrevious15MinRxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinRxPeer = _FadY1731CfmPMPrevious15MinRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 8),
    _FadY1731CfmPMPrevious15MinRxPeer_Type()
)
fadY1731CfmPMPrevious15MinRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinRxPeer.setStatus("current")
_FadY1731CfmPMPrevious15MinTxLocal_Type = Counter64
_FadY1731CfmPMPrevious15MinTxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinTxLocal = _FadY1731CfmPMPrevious15MinTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 9),
    _FadY1731CfmPMPrevious15MinTxLocal_Type()
)
fadY1731CfmPMPrevious15MinTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinTxLocal.setStatus("current")
_FadY1731CfmPMPrevious15MinTxPeer_Type = Counter64
_FadY1731CfmPMPrevious15MinTxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinTxPeer = _FadY1731CfmPMPrevious15MinTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 10),
    _FadY1731CfmPMPrevious15MinTxPeer_Type()
)
fadY1731CfmPMPrevious15MinTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinTxPeer.setStatus("current")
_FadY1731CfmPMPrevious15MinLossLocal_Type = Counter64
_FadY1731CfmPMPrevious15MinLossLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinLossLocal = _FadY1731CfmPMPrevious15MinLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 11),
    _FadY1731CfmPMPrevious15MinLossLocal_Type()
)
fadY1731CfmPMPrevious15MinLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossLocal.setStatus("current")
_FadY1731CfmPMPrevious15MinLossPeer_Type = Counter64
_FadY1731CfmPMPrevious15MinLossPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinLossPeer = _FadY1731CfmPMPrevious15MinLossPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 12),
    _FadY1731CfmPMPrevious15MinLossPeer_Type()
)
fadY1731CfmPMPrevious15MinLossPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossPeer.setStatus("current")
_FadY1731CfmPMPrevious15MinLossRatioMinLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious15MinLossRatioMinLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinLossRatioMinLocal = _FadY1731CfmPMPrevious15MinLossRatioMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 13),
    _FadY1731CfmPMPrevious15MinLossRatioMinLocal_Type()
)
fadY1731CfmPMPrevious15MinLossRatioMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioMinLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious15MinLossRatioMaxLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious15MinLossRatioMaxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinLossRatioMaxLocal = _FadY1731CfmPMPrevious15MinLossRatioMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 14),
    _FadY1731CfmPMPrevious15MinLossRatioMaxLocal_Type()
)
fadY1731CfmPMPrevious15MinLossRatioMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioMaxLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious15MinLossRatioAvgLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious15MinLossRatioAvgLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinLossRatioAvgLocal = _FadY1731CfmPMPrevious15MinLossRatioAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 15),
    _FadY1731CfmPMPrevious15MinLossRatioAvgLocal_Type()
)
fadY1731CfmPMPrevious15MinLossRatioAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioAvgLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious15MinLossRatioMinPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious15MinLossRatioMinPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinLossRatioMinPeer = _FadY1731CfmPMPrevious15MinLossRatioMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 16),
    _FadY1731CfmPMPrevious15MinLossRatioMinPeer_Type()
)
fadY1731CfmPMPrevious15MinLossRatioMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioMinPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious15MinLossRatioMaxPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious15MinLossRatioMaxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinLossRatioMaxPeer = _FadY1731CfmPMPrevious15MinLossRatioMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 17),
    _FadY1731CfmPMPrevious15MinLossRatioMaxPeer_Type()
)
fadY1731CfmPMPrevious15MinLossRatioMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioMaxPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious15MinLossRatioAvgPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious15MinLossRatioAvgPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinLossRatioAvgPeer = _FadY1731CfmPMPrevious15MinLossRatioAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 18),
    _FadY1731CfmPMPrevious15MinLossRatioAvgPeer_Type()
)
fadY1731CfmPMPrevious15MinLossRatioAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinLossRatioAvgPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious15MinTestId_Type = Unsigned32
_FadY1731CfmPMPrevious15MinTestId_Object = MibTableColumn
fadY1731CfmPMPrevious15MinTestId = _FadY1731CfmPMPrevious15MinTestId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 19),
    _FadY1731CfmPMPrevious15MinTestId_Type()
)
fadY1731CfmPMPrevious15MinTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinTestId.setStatus("current")
_FadY1731CfmPMPrevious15MinRemoteMepId_Type = Dot1agCfmMepId
_FadY1731CfmPMPrevious15MinRemoteMepId_Object = MibTableColumn
fadY1731CfmPMPrevious15MinRemoteMepId = _FadY1731CfmPMPrevious15MinRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 20),
    _FadY1731CfmPMPrevious15MinRemoteMepId_Type()
)
fadY1731CfmPMPrevious15MinRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinRemoteMepId.setStatus("current")
_FadY1731CfmPMPrevious15MinUnack_Type = Counter32
_FadY1731CfmPMPrevious15MinUnack_Object = MibTableColumn
fadY1731CfmPMPrevious15MinUnack = _FadY1731CfmPMPrevious15MinUnack_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 21),
    _FadY1731CfmPMPrevious15MinUnack_Type()
)
fadY1731CfmPMPrevious15MinUnack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinUnack.setStatus("current")
_FadY1731CfmPMPrevious15MinPDUDiscarded_Type = Counter32
_FadY1731CfmPMPrevious15MinPDUDiscarded_Object = MibTableColumn
fadY1731CfmPMPrevious15MinPDUDiscarded = _FadY1731CfmPMPrevious15MinPDUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 22),
    _FadY1731CfmPMPrevious15MinPDUDiscarded_Type()
)
fadY1731CfmPMPrevious15MinPDUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinPDUDiscarded.setStatus("current")


class _FadY1731CfmPMPrevious15MinDataSize_Type(Unsigned32):
    """Custom type fadY1731CfmPMPrevious15MinDataSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_FadY1731CfmPMPrevious15MinDataSize_Type.__name__ = "Unsigned32"
_FadY1731CfmPMPrevious15MinDataSize_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDataSize = _FadY1731CfmPMPrevious15MinDataSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 10, 1, 23),
    _FadY1731CfmPMPrevious15MinDataSize_Type()
)
fadY1731CfmPMPrevious15MinDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDataSize.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDataSize.setUnits("octets")
_FadY1731CfmPMPrevious1DayIntervalLossTable_Object = MibTable
fadY1731CfmPMPrevious1DayIntervalLossTable = _FadY1731CfmPMPrevious1DayIntervalLossTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayIntervalLossTable.setStatus("current")
_FadY1731CfmPMPrevious1DayIntervalLossEntry_Object = MibTableRow
fadY1731CfmPMPrevious1DayIntervalLossEntry = _FadY1731CfmPMPrevious1DayIntervalLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1)
)
fadY1731CfmPMPrevious1DayIntervalLossEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMPrevious1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayIntervalLossEntry.setStatus("current")


class _FadY1731CfmPMPrevious1DayIntervalNumber_Type(Integer32):
    """Custom type fadY1731CfmPMPrevious1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FadY1731CfmPMPrevious1DayIntervalNumber_Type.__name__ = "Integer32"
_FadY1731CfmPMPrevious1DayIntervalNumber_Object = MibTableColumn
fadY1731CfmPMPrevious1DayIntervalNumber = _FadY1731CfmPMPrevious1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 1),
    _FadY1731CfmPMPrevious1DayIntervalNumber_Type()
)
fadY1731CfmPMPrevious1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayIntervalNumber.setStatus("current")
_FadY1731CfmPMPrevious1DayTestType_Type = EthCfmY1731PMType
_FadY1731CfmPMPrevious1DayTestType_Object = MibTableColumn
fadY1731CfmPMPrevious1DayTestType = _FadY1731CfmPMPrevious1DayTestType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 2),
    _FadY1731CfmPMPrevious1DayTestType_Type()
)
fadY1731CfmPMPrevious1DayTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayTestType.setStatus("current")


class _FadY1731CfmPMPrevious1DayTimeMeasured_Type(Integer32):
    """Custom type fadY1731CfmPMPrevious1DayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadY1731CfmPMPrevious1DayTimeMeasured_Type.__name__ = "Integer32"
_FadY1731CfmPMPrevious1DayTimeMeasured_Object = MibTableColumn
fadY1731CfmPMPrevious1DayTimeMeasured = _FadY1731CfmPMPrevious1DayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 3),
    _FadY1731CfmPMPrevious1DayTimeMeasured_Type()
)
fadY1731CfmPMPrevious1DayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayTimeMeasured.setStatus("current")
_FadY1731CfmPMPrevious1DayInvalidDataFlag_Type = TruthValue
_FadY1731CfmPMPrevious1DayInvalidDataFlag_Object = MibTableColumn
fadY1731CfmPMPrevious1DayInvalidDataFlag = _FadY1731CfmPMPrevious1DayInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 4),
    _FadY1731CfmPMPrevious1DayInvalidDataFlag_Type()
)
fadY1731CfmPMPrevious1DayInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayInvalidDataFlag.setStatus("current")
_FadY1731CfmPMPrevious1DayPDUSent_Type = Counter32
_FadY1731CfmPMPrevious1DayPDUSent_Object = MibTableColumn
fadY1731CfmPMPrevious1DayPDUSent = _FadY1731CfmPMPrevious1DayPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 5),
    _FadY1731CfmPMPrevious1DayPDUSent_Type()
)
fadY1731CfmPMPrevious1DayPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayPDUSent.setStatus("current")
_FadY1731CfmPMPrevious1DayPDURecv_Type = Counter32
_FadY1731CfmPMPrevious1DayPDURecv_Object = MibTableColumn
fadY1731CfmPMPrevious1DayPDURecv = _FadY1731CfmPMPrevious1DayPDURecv_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 6),
    _FadY1731CfmPMPrevious1DayPDURecv_Type()
)
fadY1731CfmPMPrevious1DayPDURecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayPDURecv.setStatus("current")
_FadY1731CfmPMPrevious1DayRxLocal_Type = Counter64
_FadY1731CfmPMPrevious1DayRxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayRxLocal = _FadY1731CfmPMPrevious1DayRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 7),
    _FadY1731CfmPMPrevious1DayRxLocal_Type()
)
fadY1731CfmPMPrevious1DayRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayRxLocal.setStatus("current")
_FadY1731CfmPMPrevious1DayRxPeer_Type = Counter64
_FadY1731CfmPMPrevious1DayRxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayRxPeer = _FadY1731CfmPMPrevious1DayRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 8),
    _FadY1731CfmPMPrevious1DayRxPeer_Type()
)
fadY1731CfmPMPrevious1DayRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayRxPeer.setStatus("current")
_FadY1731CfmPMPrevious1DayTxLocal_Type = Counter64
_FadY1731CfmPMPrevious1DayTxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayTxLocal = _FadY1731CfmPMPrevious1DayTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 9),
    _FadY1731CfmPMPrevious1DayTxLocal_Type()
)
fadY1731CfmPMPrevious1DayTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayTxLocal.setStatus("current")
_FadY1731CfmPMPrevious1DayTxPeer_Type = Counter64
_FadY1731CfmPMPrevious1DayTxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayTxPeer = _FadY1731CfmPMPrevious1DayTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 10),
    _FadY1731CfmPMPrevious1DayTxPeer_Type()
)
fadY1731CfmPMPrevious1DayTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayTxPeer.setStatus("current")
_FadY1731CfmPMPrevious1DayLossLocal_Type = Counter64
_FadY1731CfmPMPrevious1DayLossLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayLossLocal = _FadY1731CfmPMPrevious1DayLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 11),
    _FadY1731CfmPMPrevious1DayLossLocal_Type()
)
fadY1731CfmPMPrevious1DayLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossLocal.setStatus("current")
_FadY1731CfmPMPrevious1DayLossPeer_Type = Counter64
_FadY1731CfmPMPrevious1DayLossPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayLossPeer = _FadY1731CfmPMPrevious1DayLossPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 12),
    _FadY1731CfmPMPrevious1DayLossPeer_Type()
)
fadY1731CfmPMPrevious1DayLossPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossPeer.setStatus("current")
_FadY1731CfmPMPrevious1DayLossRatioMinLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious1DayLossRatioMinLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayLossRatioMinLocal = _FadY1731CfmPMPrevious1DayLossRatioMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 13),
    _FadY1731CfmPMPrevious1DayLossRatioMinLocal_Type()
)
fadY1731CfmPMPrevious1DayLossRatioMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioMinLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious1DayLossRatioMaxLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious1DayLossRatioMaxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayLossRatioMaxLocal = _FadY1731CfmPMPrevious1DayLossRatioMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 14),
    _FadY1731CfmPMPrevious1DayLossRatioMaxLocal_Type()
)
fadY1731CfmPMPrevious1DayLossRatioMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioMaxLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious1DayLossRatioAvgLocal_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious1DayLossRatioAvgLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayLossRatioAvgLocal = _FadY1731CfmPMPrevious1DayLossRatioAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 15),
    _FadY1731CfmPMPrevious1DayLossRatioAvgLocal_Type()
)
fadY1731CfmPMPrevious1DayLossRatioAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioAvgLocal.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious1DayLossRatioMinPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious1DayLossRatioMinPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayLossRatioMinPeer = _FadY1731CfmPMPrevious1DayLossRatioMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 16),
    _FadY1731CfmPMPrevious1DayLossRatioMinPeer_Type()
)
fadY1731CfmPMPrevious1DayLossRatioMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioMinPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious1DayLossRatioMaxPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious1DayLossRatioMaxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayLossRatioMaxPeer = _FadY1731CfmPMPrevious1DayLossRatioMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 17),
    _FadY1731CfmPMPrevious1DayLossRatioMaxPeer_Type()
)
fadY1731CfmPMPrevious1DayLossRatioMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioMaxPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious1DayLossRatioAvgPeer_Type = TLossRatioHundrethsOfPercent
_FadY1731CfmPMPrevious1DayLossRatioAvgPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayLossRatioAvgPeer = _FadY1731CfmPMPrevious1DayLossRatioAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 18),
    _FadY1731CfmPMPrevious1DayLossRatioAvgPeer_Type()
)
fadY1731CfmPMPrevious1DayLossRatioAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayLossRatioAvgPeer.setUnits("hundredth of a percent")
_FadY1731CfmPMPrevious1DayTestId_Type = Unsigned32
_FadY1731CfmPMPrevious1DayTestId_Object = MibTableColumn
fadY1731CfmPMPrevious1DayTestId = _FadY1731CfmPMPrevious1DayTestId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 19),
    _FadY1731CfmPMPrevious1DayTestId_Type()
)
fadY1731CfmPMPrevious1DayTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayTestId.setStatus("current")
_FadY1731CfmPMPrevious1DayRemoteMepId_Type = Dot1agCfmMepId
_FadY1731CfmPMPrevious1DayRemoteMepId_Object = MibTableColumn
fadY1731CfmPMPrevious1DayRemoteMepId = _FadY1731CfmPMPrevious1DayRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 20),
    _FadY1731CfmPMPrevious1DayRemoteMepId_Type()
)
fadY1731CfmPMPrevious1DayRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayRemoteMepId.setStatus("current")
_FadY1731CfmPMPrevious1DayUnack_Type = Counter32
_FadY1731CfmPMPrevious1DayUnack_Object = MibTableColumn
fadY1731CfmPMPrevious1DayUnack = _FadY1731CfmPMPrevious1DayUnack_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 21),
    _FadY1731CfmPMPrevious1DayUnack_Type()
)
fadY1731CfmPMPrevious1DayUnack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayUnack.setStatus("current")
_FadY1731CfmPMPrevious1DayPDUDiscarded_Type = Counter32
_FadY1731CfmPMPrevious1DayPDUDiscarded_Object = MibTableColumn
fadY1731CfmPMPrevious1DayPDUDiscarded = _FadY1731CfmPMPrevious1DayPDUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 22),
    _FadY1731CfmPMPrevious1DayPDUDiscarded_Type()
)
fadY1731CfmPMPrevious1DayPDUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayPDUDiscarded.setStatus("current")


class _FadY1731CfmPMPrevious1DayDataSize_Type(Unsigned32):
    """Custom type fadY1731CfmPMPrevious1DayDataSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_FadY1731CfmPMPrevious1DayDataSize_Type.__name__ = "Unsigned32"
_FadY1731CfmPMPrevious1DayDataSize_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDataSize = _FadY1731CfmPMPrevious1DayDataSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 11, 1, 23),
    _FadY1731CfmPMPrevious1DayDataSize_Type()
)
fadY1731CfmPMPrevious1DayDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDataSize.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDataSize.setUnits("octets")
_FadY1731CfmPMCurrent15MinIntervalDelayTable_Object = MibTable
fadY1731CfmPMCurrent15MinIntervalDelayTable = _FadY1731CfmPMCurrent15MinIntervalDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinIntervalDelayTable.setStatus("current")
_FadY1731CfmPMCurrent15MinIntervalDelayEntry_Object = MibTableRow
fadY1731CfmPMCurrent15MinIntervalDelayEntry = _FadY1731CfmPMCurrent15MinIntervalDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1)
)
fadY1731CfmPMCurrent15MinIntervalDelayEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinIntervalDelayEntry.setStatus("current")


class _FadY1731CfmPMCurrent15MinDelayTimeElapsed_Type(Integer32):
    """Custom type fadY1731CfmPMCurrent15MinDelayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadY1731CfmPMCurrent15MinDelayTimeElapsed_Type.__name__ = "Integer32"
_FadY1731CfmPMCurrent15MinDelayTimeElapsed_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayTimeElapsed = _FadY1731CfmPMCurrent15MinDelayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 1),
    _FadY1731CfmPMCurrent15MinDelayTimeElapsed_Type()
)
fadY1731CfmPMCurrent15MinDelayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayTimeElapsed.setStatus("current")


class _FadY1731CfmPMCurrent15MinDelayTimeMeasured_Type(Integer32):
    """Custom type fadY1731CfmPMCurrent15MinDelayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadY1731CfmPMCurrent15MinDelayTimeMeasured_Type.__name__ = "Integer32"
_FadY1731CfmPMCurrent15MinDelayTimeMeasured_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayTimeMeasured = _FadY1731CfmPMCurrent15MinDelayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 2),
    _FadY1731CfmPMCurrent15MinDelayTimeMeasured_Type()
)
fadY1731CfmPMCurrent15MinDelayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayTimeMeasured.setStatus("current")


class _FadY1731CfmPM15MinDelayValidIntervals_Type(Integer32):
    """Custom type fadY1731CfmPM15MinDelayValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_FadY1731CfmPM15MinDelayValidIntervals_Type.__name__ = "Integer32"
_FadY1731CfmPM15MinDelayValidIntervals_Object = MibTableColumn
fadY1731CfmPM15MinDelayValidIntervals = _FadY1731CfmPM15MinDelayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 3),
    _FadY1731CfmPM15MinDelayValidIntervals_Type()
)
fadY1731CfmPM15MinDelayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPM15MinDelayValidIntervals.setStatus("current")
_FadY1731CfmPMCurrent15MinDelayInvalidDataFlag_Type = TruthValue
_FadY1731CfmPMCurrent15MinDelayInvalidDataFlag_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayInvalidDataFlag = _FadY1731CfmPMCurrent15MinDelayInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 4),
    _FadY1731CfmPMCurrent15MinDelayInvalidDataFlag_Type()
)
fadY1731CfmPMCurrent15MinDelayInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayInvalidDataFlag.setStatus("current")
_FadY1731CfmPMCurrent15MinDelayPDUSent_Type = Counter32
_FadY1731CfmPMCurrent15MinDelayPDUSent_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayPDUSent = _FadY1731CfmPMCurrent15MinDelayPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 5),
    _FadY1731CfmPMCurrent15MinDelayPDUSent_Type()
)
fadY1731CfmPMCurrent15MinDelayPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayPDUSent.setStatus("current")
_FadY1731CfmPMCurrent15MinDelayPDURecv_Type = Counter32
_FadY1731CfmPMCurrent15MinDelayPDURecv_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayPDURecv = _FadY1731CfmPMCurrent15MinDelayPDURecv_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 6),
    _FadY1731CfmPMCurrent15MinDelayPDURecv_Type()
)
fadY1731CfmPMCurrent15MinDelayPDURecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayPDURecv.setStatus("current")
_FadY1731CfmPMCurrent15MinDelayMinLocal_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayMinLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayMinLocal = _FadY1731CfmPMCurrent15MinDelayMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 7),
    _FadY1731CfmPMCurrent15MinDelayMinLocal_Type()
)
fadY1731CfmPMCurrent15MinDelayMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMinLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayMaxLocal_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayMaxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayMaxLocal = _FadY1731CfmPMCurrent15MinDelayMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 8),
    _FadY1731CfmPMCurrent15MinDelayMaxLocal_Type()
)
fadY1731CfmPMCurrent15MinDelayMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMaxLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayAvgLocal_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayAvgLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayAvgLocal = _FadY1731CfmPMCurrent15MinDelayAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 9),
    _FadY1731CfmPMCurrent15MinDelayAvgLocal_Type()
)
fadY1731CfmPMCurrent15MinDelayAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayAvgLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayMinPeer_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayMinPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayMinPeer = _FadY1731CfmPMCurrent15MinDelayMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 10),
    _FadY1731CfmPMCurrent15MinDelayMinPeer_Type()
)
fadY1731CfmPMCurrent15MinDelayMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMinPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayMaxPeer_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayMaxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayMaxPeer = _FadY1731CfmPMCurrent15MinDelayMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 11),
    _FadY1731CfmPMCurrent15MinDelayMaxPeer_Type()
)
fadY1731CfmPMCurrent15MinDelayMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMaxPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayAvgPeer_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayAvgPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayAvgPeer = _FadY1731CfmPMCurrent15MinDelayAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 12),
    _FadY1731CfmPMCurrent15MinDelayAvgPeer_Type()
)
fadY1731CfmPMCurrent15MinDelayAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayAvgPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayMinBidir_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayMinBidir_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayMinBidir = _FadY1731CfmPMCurrent15MinDelayMinBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 13),
    _FadY1731CfmPMCurrent15MinDelayMinBidir_Type()
)
fadY1731CfmPMCurrent15MinDelayMinBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMinBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMinBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayMaxBidir_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayMaxBidir_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayMaxBidir = _FadY1731CfmPMCurrent15MinDelayMaxBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 14),
    _FadY1731CfmPMCurrent15MinDelayMaxBidir_Type()
)
fadY1731CfmPMCurrent15MinDelayMaxBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMaxBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayMaxBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayAvgBidir_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayAvgBidir_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayAvgBidir = _FadY1731CfmPMCurrent15MinDelayAvgBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 15),
    _FadY1731CfmPMCurrent15MinDelayAvgBidir_Type()
)
fadY1731CfmPMCurrent15MinDelayAvgBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayAvgBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayAvgBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarMinLocal_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarMinLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarMinLocal = _FadY1731CfmPMCurrent15MinDelayVarMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 16),
    _FadY1731CfmPMCurrent15MinDelayVarMinLocal_Type()
)
fadY1731CfmPMCurrent15MinDelayVarMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMinLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarMaxLocal_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarMaxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarMaxLocal = _FadY1731CfmPMCurrent15MinDelayVarMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 17),
    _FadY1731CfmPMCurrent15MinDelayVarMaxLocal_Type()
)
fadY1731CfmPMCurrent15MinDelayVarMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMaxLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarAvgLocal_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarAvgLocal_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarAvgLocal = _FadY1731CfmPMCurrent15MinDelayVarAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 18),
    _FadY1731CfmPMCurrent15MinDelayVarAvgLocal_Type()
)
fadY1731CfmPMCurrent15MinDelayVarAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarAvgLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarMinPeer_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarMinPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarMinPeer = _FadY1731CfmPMCurrent15MinDelayVarMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 19),
    _FadY1731CfmPMCurrent15MinDelayVarMinPeer_Type()
)
fadY1731CfmPMCurrent15MinDelayVarMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMinPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarMaxPeer_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarMaxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarMaxPeer = _FadY1731CfmPMCurrent15MinDelayVarMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 20),
    _FadY1731CfmPMCurrent15MinDelayVarMaxPeer_Type()
)
fadY1731CfmPMCurrent15MinDelayVarMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMaxPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarAvgPeer_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarAvgPeer_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarAvgPeer = _FadY1731CfmPMCurrent15MinDelayVarAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 21),
    _FadY1731CfmPMCurrent15MinDelayVarAvgPeer_Type()
)
fadY1731CfmPMCurrent15MinDelayVarAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarAvgPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarMinBidir_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarMinBidir_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarMinBidir = _FadY1731CfmPMCurrent15MinDelayVarMinBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 22),
    _FadY1731CfmPMCurrent15MinDelayVarMinBidir_Type()
)
fadY1731CfmPMCurrent15MinDelayVarMinBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMinBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMinBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarMaxBidir_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarMaxBidir_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarMaxBidir = _FadY1731CfmPMCurrent15MinDelayVarMaxBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 23),
    _FadY1731CfmPMCurrent15MinDelayVarMaxBidir_Type()
)
fadY1731CfmPMCurrent15MinDelayVarMaxBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMaxBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarMaxBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayVarAvgBidir_Type = Unsigned32
_FadY1731CfmPMCurrent15MinDelayVarAvgBidir_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayVarAvgBidir = _FadY1731CfmPMCurrent15MinDelayVarAvgBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 24),
    _FadY1731CfmPMCurrent15MinDelayVarAvgBidir_Type()
)
fadY1731CfmPMCurrent15MinDelayVarAvgBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarAvgBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayVarAvgBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent15MinDelayPDUDiscarded_Type = Counter32
_FadY1731CfmPMCurrent15MinDelayPDUDiscarded_Object = MibTableColumn
fadY1731CfmPMCurrent15MinDelayPDUDiscarded = _FadY1731CfmPMCurrent15MinDelayPDUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 12, 1, 25),
    _FadY1731CfmPMCurrent15MinDelayPDUDiscarded_Type()
)
fadY1731CfmPMCurrent15MinDelayPDUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent15MinDelayPDUDiscarded.setStatus("current")
_FadY1731CfmPMCurrent1DayIntervalDelayTable_Object = MibTable
fadY1731CfmPMCurrent1DayIntervalDelayTable = _FadY1731CfmPMCurrent1DayIntervalDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayIntervalDelayTable.setStatus("current")
_FadY1731CfmPMCurrent1DayIntervalDelayEntry_Object = MibTableRow
fadY1731CfmPMCurrent1DayIntervalDelayEntry = _FadY1731CfmPMCurrent1DayIntervalDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1)
)
fadY1731CfmPMCurrent1DayIntervalDelayEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayIntervalDelayEntry.setStatus("current")


class _FadY1731CfmPMCurrent1DayDelayTimeElapsed_Type(Integer32):
    """Custom type fadY1731CfmPMCurrent1DayDelayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadY1731CfmPMCurrent1DayDelayTimeElapsed_Type.__name__ = "Integer32"
_FadY1731CfmPMCurrent1DayDelayTimeElapsed_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayTimeElapsed = _FadY1731CfmPMCurrent1DayDelayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 1),
    _FadY1731CfmPMCurrent1DayDelayTimeElapsed_Type()
)
fadY1731CfmPMCurrent1DayDelayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayTimeElapsed.setStatus("current")


class _FadY1731CfmPMCurrent1DayDelayTimeMeasured_Type(Integer32):
    """Custom type fadY1731CfmPMCurrent1DayDelayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadY1731CfmPMCurrent1DayDelayTimeMeasured_Type.__name__ = "Integer32"
_FadY1731CfmPMCurrent1DayDelayTimeMeasured_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayTimeMeasured = _FadY1731CfmPMCurrent1DayDelayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 2),
    _FadY1731CfmPMCurrent1DayDelayTimeMeasured_Type()
)
fadY1731CfmPMCurrent1DayDelayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayTimeMeasured.setStatus("current")


class _FadY1731CfmPM1DayDelayValidIntervals_Type(Integer32):
    """Custom type fadY1731CfmPM1DayDelayValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FadY1731CfmPM1DayDelayValidIntervals_Type.__name__ = "Integer32"
_FadY1731CfmPM1DayDelayValidIntervals_Object = MibTableColumn
fadY1731CfmPM1DayDelayValidIntervals = _FadY1731CfmPM1DayDelayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 3),
    _FadY1731CfmPM1DayDelayValidIntervals_Type()
)
fadY1731CfmPM1DayDelayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPM1DayDelayValidIntervals.setStatus("current")
_FadY1731CfmPMCurrent1DayDelayInvalidDataFlag_Type = TruthValue
_FadY1731CfmPMCurrent1DayDelayInvalidDataFlag_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayInvalidDataFlag = _FadY1731CfmPMCurrent1DayDelayInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 4),
    _FadY1731CfmPMCurrent1DayDelayInvalidDataFlag_Type()
)
fadY1731CfmPMCurrent1DayDelayInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayInvalidDataFlag.setStatus("current")
_FadY1731CfmPMCurrent1DayDelayPDUSent_Type = Counter32
_FadY1731CfmPMCurrent1DayDelayPDUSent_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayPDUSent = _FadY1731CfmPMCurrent1DayDelayPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 5),
    _FadY1731CfmPMCurrent1DayDelayPDUSent_Type()
)
fadY1731CfmPMCurrent1DayDelayPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayPDUSent.setStatus("current")
_FadY1731CfmPMCurrent1DayDelayPDURecv_Type = Counter32
_FadY1731CfmPMCurrent1DayDelayPDURecv_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayPDURecv = _FadY1731CfmPMCurrent1DayDelayPDURecv_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 6),
    _FadY1731CfmPMCurrent1DayDelayPDURecv_Type()
)
fadY1731CfmPMCurrent1DayDelayPDURecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayPDURecv.setStatus("current")
_FadY1731CfmPMCurrent1DayDelayMinLocal_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayMinLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayMinLocal = _FadY1731CfmPMCurrent1DayDelayMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 7),
    _FadY1731CfmPMCurrent1DayDelayMinLocal_Type()
)
fadY1731CfmPMCurrent1DayDelayMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMinLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayMaxLocal_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayMaxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayMaxLocal = _FadY1731CfmPMCurrent1DayDelayMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 8),
    _FadY1731CfmPMCurrent1DayDelayMaxLocal_Type()
)
fadY1731CfmPMCurrent1DayDelayMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMaxLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayAvgLocal_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayAvgLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayAvgLocal = _FadY1731CfmPMCurrent1DayDelayAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 9),
    _FadY1731CfmPMCurrent1DayDelayAvgLocal_Type()
)
fadY1731CfmPMCurrent1DayDelayAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayAvgLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayMinPeer_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayMinPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayMinPeer = _FadY1731CfmPMCurrent1DayDelayMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 10),
    _FadY1731CfmPMCurrent1DayDelayMinPeer_Type()
)
fadY1731CfmPMCurrent1DayDelayMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMinPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayMaxPeer_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayMaxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayMaxPeer = _FadY1731CfmPMCurrent1DayDelayMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 11),
    _FadY1731CfmPMCurrent1DayDelayMaxPeer_Type()
)
fadY1731CfmPMCurrent1DayDelayMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMaxPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayAvgPeer_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayAvgPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayAvgPeer = _FadY1731CfmPMCurrent1DayDelayAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 12),
    _FadY1731CfmPMCurrent1DayDelayAvgPeer_Type()
)
fadY1731CfmPMCurrent1DayDelayAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayAvgPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayMinBidir_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayMinBidir_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayMinBidir = _FadY1731CfmPMCurrent1DayDelayMinBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 13),
    _FadY1731CfmPMCurrent1DayDelayMinBidir_Type()
)
fadY1731CfmPMCurrent1DayDelayMinBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMinBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMinBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayMaxBidir_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayMaxBidir_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayMaxBidir = _FadY1731CfmPMCurrent1DayDelayMaxBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 14),
    _FadY1731CfmPMCurrent1DayDelayMaxBidir_Type()
)
fadY1731CfmPMCurrent1DayDelayMaxBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMaxBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayMaxBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayAvgBidir_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayAvgBidir_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayAvgBidir = _FadY1731CfmPMCurrent1DayDelayAvgBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 15),
    _FadY1731CfmPMCurrent1DayDelayAvgBidir_Type()
)
fadY1731CfmPMCurrent1DayDelayAvgBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayAvgBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayAvgBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarMinLocal_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarMinLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarMinLocal = _FadY1731CfmPMCurrent1DayDelayVarMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 16),
    _FadY1731CfmPMCurrent1DayDelayVarMinLocal_Type()
)
fadY1731CfmPMCurrent1DayDelayVarMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMinLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarMaxLocal_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarMaxLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarMaxLocal = _FadY1731CfmPMCurrent1DayDelayVarMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 17),
    _FadY1731CfmPMCurrent1DayDelayVarMaxLocal_Type()
)
fadY1731CfmPMCurrent1DayDelayVarMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMaxLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarAvgLocal_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarAvgLocal_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarAvgLocal = _FadY1731CfmPMCurrent1DayDelayVarAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 18),
    _FadY1731CfmPMCurrent1DayDelayVarAvgLocal_Type()
)
fadY1731CfmPMCurrent1DayDelayVarAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarAvgLocal.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarMinPeer_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarMinPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarMinPeer = _FadY1731CfmPMCurrent1DayDelayVarMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 19),
    _FadY1731CfmPMCurrent1DayDelayVarMinPeer_Type()
)
fadY1731CfmPMCurrent1DayDelayVarMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMinPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarMaxPeer_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarMaxPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarMaxPeer = _FadY1731CfmPMCurrent1DayDelayVarMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 20),
    _FadY1731CfmPMCurrent1DayDelayVarMaxPeer_Type()
)
fadY1731CfmPMCurrent1DayDelayVarMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMaxPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarAvgPeer_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarAvgPeer_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarAvgPeer = _FadY1731CfmPMCurrent1DayDelayVarAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 21),
    _FadY1731CfmPMCurrent1DayDelayVarAvgPeer_Type()
)
fadY1731CfmPMCurrent1DayDelayVarAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarAvgPeer.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarMinBidir_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarMinBidir_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarMinBidir = _FadY1731CfmPMCurrent1DayDelayVarMinBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 22),
    _FadY1731CfmPMCurrent1DayDelayVarMinBidir_Type()
)
fadY1731CfmPMCurrent1DayDelayVarMinBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMinBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMinBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarMaxBidir_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarMaxBidir_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarMaxBidir = _FadY1731CfmPMCurrent1DayDelayVarMaxBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 23),
    _FadY1731CfmPMCurrent1DayDelayVarMaxBidir_Type()
)
fadY1731CfmPMCurrent1DayDelayVarMaxBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMaxBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarMaxBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayVarAvgBidir_Type = Unsigned32
_FadY1731CfmPMCurrent1DayDelayVarAvgBidir_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayVarAvgBidir = _FadY1731CfmPMCurrent1DayDelayVarAvgBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 24),
    _FadY1731CfmPMCurrent1DayDelayVarAvgBidir_Type()
)
fadY1731CfmPMCurrent1DayDelayVarAvgBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarAvgBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayVarAvgBidir.setUnits("microseconds")
_FadY1731CfmPMCurrent1DayDelayPDUDiscarded_Type = Counter32
_FadY1731CfmPMCurrent1DayDelayPDUDiscarded_Object = MibTableColumn
fadY1731CfmPMCurrent1DayDelayPDUDiscarded = _FadY1731CfmPMCurrent1DayDelayPDUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 13, 1, 25),
    _FadY1731CfmPMCurrent1DayDelayPDUDiscarded_Type()
)
fadY1731CfmPMCurrent1DayDelayPDUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMCurrent1DayDelayPDUDiscarded.setStatus("current")
_FadY1731CfmPMPrevious15MinIntervalDelayTable_Object = MibTable
fadY1731CfmPMPrevious15MinIntervalDelayTable = _FadY1731CfmPMPrevious15MinIntervalDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinIntervalDelayTable.setStatus("current")
_FadY1731CfmPMPrevious15MinIntervalDelayEntry_Object = MibTableRow
fadY1731CfmPMPrevious15MinIntervalDelayEntry = _FadY1731CfmPMPrevious15MinIntervalDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1)
)
fadY1731CfmPMPrevious15MinIntervalDelayEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMPrevious15MinDelayIntervalNumber"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinIntervalDelayEntry.setStatus("current")


class _FadY1731CfmPMPrevious15MinDelayIntervalNumber_Type(Integer32):
    """Custom type fadY1731CfmPMPrevious15MinDelayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_FadY1731CfmPMPrevious15MinDelayIntervalNumber_Type.__name__ = "Integer32"
_FadY1731CfmPMPrevious15MinDelayIntervalNumber_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayIntervalNumber = _FadY1731CfmPMPrevious15MinDelayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 1),
    _FadY1731CfmPMPrevious15MinDelayIntervalNumber_Type()
)
fadY1731CfmPMPrevious15MinDelayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayIntervalNumber.setStatus("current")


class _FadY1731CfmPMPrevious15MinDelayTimeMeasured_Type(Integer32):
    """Custom type fadY1731CfmPMPrevious15MinDelayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FadY1731CfmPMPrevious15MinDelayTimeMeasured_Type.__name__ = "Integer32"
_FadY1731CfmPMPrevious15MinDelayTimeMeasured_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayTimeMeasured = _FadY1731CfmPMPrevious15MinDelayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 2),
    _FadY1731CfmPMPrevious15MinDelayTimeMeasured_Type()
)
fadY1731CfmPMPrevious15MinDelayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayTimeMeasured.setStatus("current")
_FadY1731CfmPMPrevious15MinDelayInvalidDataFlag_Type = TruthValue
_FadY1731CfmPMPrevious15MinDelayInvalidDataFlag_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayInvalidDataFlag = _FadY1731CfmPMPrevious15MinDelayInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 3),
    _FadY1731CfmPMPrevious15MinDelayInvalidDataFlag_Type()
)
fadY1731CfmPMPrevious15MinDelayInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayInvalidDataFlag.setStatus("current")
_FadY1731CfmPMPrevious15MinDelayPDUSent_Type = Counter32
_FadY1731CfmPMPrevious15MinDelayPDUSent_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayPDUSent = _FadY1731CfmPMPrevious15MinDelayPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 4),
    _FadY1731CfmPMPrevious15MinDelayPDUSent_Type()
)
fadY1731CfmPMPrevious15MinDelayPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayPDUSent.setStatus("current")
_FadY1731CfmPMPrevious15MinDelayPDURecv_Type = Counter32
_FadY1731CfmPMPrevious15MinDelayPDURecv_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayPDURecv = _FadY1731CfmPMPrevious15MinDelayPDURecv_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 5),
    _FadY1731CfmPMPrevious15MinDelayPDURecv_Type()
)
fadY1731CfmPMPrevious15MinDelayPDURecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayPDURecv.setStatus("current")
_FadY1731CfmPMPrevious15MinDelayMinLocal_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayMinLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayMinLocal = _FadY1731CfmPMPrevious15MinDelayMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 6),
    _FadY1731CfmPMPrevious15MinDelayMinLocal_Type()
)
fadY1731CfmPMPrevious15MinDelayMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMinLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayMaxLocal_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayMaxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayMaxLocal = _FadY1731CfmPMPrevious15MinDelayMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 7),
    _FadY1731CfmPMPrevious15MinDelayMaxLocal_Type()
)
fadY1731CfmPMPrevious15MinDelayMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMaxLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayAvgLocal_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayAvgLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayAvgLocal = _FadY1731CfmPMPrevious15MinDelayAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 8),
    _FadY1731CfmPMPrevious15MinDelayAvgLocal_Type()
)
fadY1731CfmPMPrevious15MinDelayAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayAvgLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayMinPeer_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayMinPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayMinPeer = _FadY1731CfmPMPrevious15MinDelayMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 9),
    _FadY1731CfmPMPrevious15MinDelayMinPeer_Type()
)
fadY1731CfmPMPrevious15MinDelayMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMinPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayMaxPeer_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayMaxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayMaxPeer = _FadY1731CfmPMPrevious15MinDelayMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 10),
    _FadY1731CfmPMPrevious15MinDelayMaxPeer_Type()
)
fadY1731CfmPMPrevious15MinDelayMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMaxPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayAvgPeer_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayAvgPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayAvgPeer = _FadY1731CfmPMPrevious15MinDelayAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 11),
    _FadY1731CfmPMPrevious15MinDelayAvgPeer_Type()
)
fadY1731CfmPMPrevious15MinDelayAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayAvgPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayMinBidir_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayMinBidir_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayMinBidir = _FadY1731CfmPMPrevious15MinDelayMinBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 12),
    _FadY1731CfmPMPrevious15MinDelayMinBidir_Type()
)
fadY1731CfmPMPrevious15MinDelayMinBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMinBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMinBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayMaxBidir_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayMaxBidir_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayMaxBidir = _FadY1731CfmPMPrevious15MinDelayMaxBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 13),
    _FadY1731CfmPMPrevious15MinDelayMaxBidir_Type()
)
fadY1731CfmPMPrevious15MinDelayMaxBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMaxBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayMaxBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayAvgBidir_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayAvgBidir_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayAvgBidir = _FadY1731CfmPMPrevious15MinDelayAvgBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 14),
    _FadY1731CfmPMPrevious15MinDelayAvgBidir_Type()
)
fadY1731CfmPMPrevious15MinDelayAvgBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayAvgBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayAvgBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarMinLocal_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarMinLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarMinLocal = _FadY1731CfmPMPrevious15MinDelayVarMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 15),
    _FadY1731CfmPMPrevious15MinDelayVarMinLocal_Type()
)
fadY1731CfmPMPrevious15MinDelayVarMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMinLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarMaxLocal_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarMaxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarMaxLocal = _FadY1731CfmPMPrevious15MinDelayVarMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 16),
    _FadY1731CfmPMPrevious15MinDelayVarMaxLocal_Type()
)
fadY1731CfmPMPrevious15MinDelayVarMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMaxLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarAvgLocal_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarAvgLocal_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarAvgLocal = _FadY1731CfmPMPrevious15MinDelayVarAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 17),
    _FadY1731CfmPMPrevious15MinDelayVarAvgLocal_Type()
)
fadY1731CfmPMPrevious15MinDelayVarAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarAvgLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarMinPeer_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarMinPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarMinPeer = _FadY1731CfmPMPrevious15MinDelayVarMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 18),
    _FadY1731CfmPMPrevious15MinDelayVarMinPeer_Type()
)
fadY1731CfmPMPrevious15MinDelayVarMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMinPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarMaxPeer_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarMaxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarMaxPeer = _FadY1731CfmPMPrevious15MinDelayVarMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 19),
    _FadY1731CfmPMPrevious15MinDelayVarMaxPeer_Type()
)
fadY1731CfmPMPrevious15MinDelayVarMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMaxPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarAvgPeer_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarAvgPeer_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarAvgPeer = _FadY1731CfmPMPrevious15MinDelayVarAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 20),
    _FadY1731CfmPMPrevious15MinDelayVarAvgPeer_Type()
)
fadY1731CfmPMPrevious15MinDelayVarAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarAvgPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarMinBidir_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarMinBidir_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarMinBidir = _FadY1731CfmPMPrevious15MinDelayVarMinBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 21),
    _FadY1731CfmPMPrevious15MinDelayVarMinBidir_Type()
)
fadY1731CfmPMPrevious15MinDelayVarMinBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMinBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMinBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarMaxBidir_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarMaxBidir_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarMaxBidir = _FadY1731CfmPMPrevious15MinDelayVarMaxBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 22),
    _FadY1731CfmPMPrevious15MinDelayVarMaxBidir_Type()
)
fadY1731CfmPMPrevious15MinDelayVarMaxBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMaxBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarMaxBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayVarAvgBidir_Type = Unsigned32
_FadY1731CfmPMPrevious15MinDelayVarAvgBidir_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayVarAvgBidir = _FadY1731CfmPMPrevious15MinDelayVarAvgBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 23),
    _FadY1731CfmPMPrevious15MinDelayVarAvgBidir_Type()
)
fadY1731CfmPMPrevious15MinDelayVarAvgBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarAvgBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayVarAvgBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious15MinDelayPDUDiscarded_Type = Counter32
_FadY1731CfmPMPrevious15MinDelayPDUDiscarded_Object = MibTableColumn
fadY1731CfmPMPrevious15MinDelayPDUDiscarded = _FadY1731CfmPMPrevious15MinDelayPDUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 14, 1, 24),
    _FadY1731CfmPMPrevious15MinDelayPDUDiscarded_Type()
)
fadY1731CfmPMPrevious15MinDelayPDUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious15MinDelayPDUDiscarded.setStatus("current")
_FadY1731CfmPMPrevious1DayIntervalDelayTable_Object = MibTable
fadY1731CfmPMPrevious1DayIntervalDelayTable = _FadY1731CfmPMPrevious1DayIntervalDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15)
)
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayIntervalDelayTable.setStatus("current")
_FadY1731CfmPMPrevious1DayIntervalDelayEntry_Object = MibTableRow
fadY1731CfmPMPrevious1DayIntervalDelayEntry = _FadY1731CfmPMPrevious1DayIntervalDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1)
)
fadY1731CfmPMPrevious1DayIntervalDelayEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMConfigSessionId"),
    (0, "IHUB-EXT-MIB", "fadY1731CfmPMPrevious1DayDelayIntervalNumber"),
)
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayIntervalDelayEntry.setStatus("current")


class _FadY1731CfmPMPrevious1DayDelayIntervalNumber_Type(Integer32):
    """Custom type fadY1731CfmPMPrevious1DayDelayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FadY1731CfmPMPrevious1DayDelayIntervalNumber_Type.__name__ = "Integer32"
_FadY1731CfmPMPrevious1DayDelayIntervalNumber_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayIntervalNumber = _FadY1731CfmPMPrevious1DayDelayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 1),
    _FadY1731CfmPMPrevious1DayDelayIntervalNumber_Type()
)
fadY1731CfmPMPrevious1DayDelayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayIntervalNumber.setStatus("current")


class _FadY1731CfmPMPrevious1DayDelayTimeMeasured_Type(Integer32):
    """Custom type fadY1731CfmPMPrevious1DayDelayTimeMeasured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FadY1731CfmPMPrevious1DayDelayTimeMeasured_Type.__name__ = "Integer32"
_FadY1731CfmPMPrevious1DayDelayTimeMeasured_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayTimeMeasured = _FadY1731CfmPMPrevious1DayDelayTimeMeasured_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 2),
    _FadY1731CfmPMPrevious1DayDelayTimeMeasured_Type()
)
fadY1731CfmPMPrevious1DayDelayTimeMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayTimeMeasured.setStatus("current")
_FadY1731CfmPMPrevious1DayDelayInvalidDataFlag_Type = TruthValue
_FadY1731CfmPMPrevious1DayDelayInvalidDataFlag_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayInvalidDataFlag = _FadY1731CfmPMPrevious1DayDelayInvalidDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 3),
    _FadY1731CfmPMPrevious1DayDelayInvalidDataFlag_Type()
)
fadY1731CfmPMPrevious1DayDelayInvalidDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayInvalidDataFlag.setStatus("current")
_FadY1731CfmPMPrevious1DayDelayPDUSent_Type = Counter32
_FadY1731CfmPMPrevious1DayDelayPDUSent_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayPDUSent = _FadY1731CfmPMPrevious1DayDelayPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 4),
    _FadY1731CfmPMPrevious1DayDelayPDUSent_Type()
)
fadY1731CfmPMPrevious1DayDelayPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayPDUSent.setStatus("current")
_FadY1731CfmPMPrevious1DayDelayPDURecv_Type = Counter32
_FadY1731CfmPMPrevious1DayDelayPDURecv_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayPDURecv = _FadY1731CfmPMPrevious1DayDelayPDURecv_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 5),
    _FadY1731CfmPMPrevious1DayDelayPDURecv_Type()
)
fadY1731CfmPMPrevious1DayDelayPDURecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayPDURecv.setStatus("current")
_FadY1731CfmPMPrevious1DayDelayMinLocal_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayMinLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayMinLocal = _FadY1731CfmPMPrevious1DayDelayMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 6),
    _FadY1731CfmPMPrevious1DayDelayMinLocal_Type()
)
fadY1731CfmPMPrevious1DayDelayMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMinLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayMaxLocal_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayMaxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayMaxLocal = _FadY1731CfmPMPrevious1DayDelayMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 7),
    _FadY1731CfmPMPrevious1DayDelayMaxLocal_Type()
)
fadY1731CfmPMPrevious1DayDelayMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMaxLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayAvgLocal_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayAvgLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayAvgLocal = _FadY1731CfmPMPrevious1DayDelayAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 8),
    _FadY1731CfmPMPrevious1DayDelayAvgLocal_Type()
)
fadY1731CfmPMPrevious1DayDelayAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayAvgLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayMinPeer_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayMinPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayMinPeer = _FadY1731CfmPMPrevious1DayDelayMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 9),
    _FadY1731CfmPMPrevious1DayDelayMinPeer_Type()
)
fadY1731CfmPMPrevious1DayDelayMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMinPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayMaxPeer_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayMaxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayMaxPeer = _FadY1731CfmPMPrevious1DayDelayMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 10),
    _FadY1731CfmPMPrevious1DayDelayMaxPeer_Type()
)
fadY1731CfmPMPrevious1DayDelayMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMaxPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayAvgPeer_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayAvgPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayAvgPeer = _FadY1731CfmPMPrevious1DayDelayAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 11),
    _FadY1731CfmPMPrevious1DayDelayAvgPeer_Type()
)
fadY1731CfmPMPrevious1DayDelayAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayAvgPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayMinBidir_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayMinBidir_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayMinBidir = _FadY1731CfmPMPrevious1DayDelayMinBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 12),
    _FadY1731CfmPMPrevious1DayDelayMinBidir_Type()
)
fadY1731CfmPMPrevious1DayDelayMinBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMinBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMinBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayMaxBidir_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayMaxBidir_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayMaxBidir = _FadY1731CfmPMPrevious1DayDelayMaxBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 13),
    _FadY1731CfmPMPrevious1DayDelayMaxBidir_Type()
)
fadY1731CfmPMPrevious1DayDelayMaxBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMaxBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayMaxBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayAvgBidir_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayAvgBidir_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayAvgBidir = _FadY1731CfmPMPrevious1DayDelayAvgBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 14),
    _FadY1731CfmPMPrevious1DayDelayAvgBidir_Type()
)
fadY1731CfmPMPrevious1DayDelayAvgBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayAvgBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayAvgBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarMinLocal_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarMinLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarMinLocal = _FadY1731CfmPMPrevious1DayDelayVarMinLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 15),
    _FadY1731CfmPMPrevious1DayDelayVarMinLocal_Type()
)
fadY1731CfmPMPrevious1DayDelayVarMinLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMinLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMinLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarMaxLocal_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarMaxLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarMaxLocal = _FadY1731CfmPMPrevious1DayDelayVarMaxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 16),
    _FadY1731CfmPMPrevious1DayDelayVarMaxLocal_Type()
)
fadY1731CfmPMPrevious1DayDelayVarMaxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMaxLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMaxLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarAvgLocal_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarAvgLocal_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarAvgLocal = _FadY1731CfmPMPrevious1DayDelayVarAvgLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 17),
    _FadY1731CfmPMPrevious1DayDelayVarAvgLocal_Type()
)
fadY1731CfmPMPrevious1DayDelayVarAvgLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarAvgLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarAvgLocal.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarMinPeer_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarMinPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarMinPeer = _FadY1731CfmPMPrevious1DayDelayVarMinPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 18),
    _FadY1731CfmPMPrevious1DayDelayVarMinPeer_Type()
)
fadY1731CfmPMPrevious1DayDelayVarMinPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMinPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMinPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarMaxPeer_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarMaxPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarMaxPeer = _FadY1731CfmPMPrevious1DayDelayVarMaxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 19),
    _FadY1731CfmPMPrevious1DayDelayVarMaxPeer_Type()
)
fadY1731CfmPMPrevious1DayDelayVarMaxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMaxPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMaxPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarAvgPeer_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarAvgPeer_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarAvgPeer = _FadY1731CfmPMPrevious1DayDelayVarAvgPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 20),
    _FadY1731CfmPMPrevious1DayDelayVarAvgPeer_Type()
)
fadY1731CfmPMPrevious1DayDelayVarAvgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarAvgPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarAvgPeer.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarMinBidir_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarMinBidir_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarMinBidir = _FadY1731CfmPMPrevious1DayDelayVarMinBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 21),
    _FadY1731CfmPMPrevious1DayDelayVarMinBidir_Type()
)
fadY1731CfmPMPrevious1DayDelayVarMinBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMinBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMinBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarMaxBidir_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarMaxBidir_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarMaxBidir = _FadY1731CfmPMPrevious1DayDelayVarMaxBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 22),
    _FadY1731CfmPMPrevious1DayDelayVarMaxBidir_Type()
)
fadY1731CfmPMPrevious1DayDelayVarMaxBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMaxBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarMaxBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayVarAvgBidir_Type = Unsigned32
_FadY1731CfmPMPrevious1DayDelayVarAvgBidir_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayVarAvgBidir = _FadY1731CfmPMPrevious1DayDelayVarAvgBidir_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 23),
    _FadY1731CfmPMPrevious1DayDelayVarAvgBidir_Type()
)
fadY1731CfmPMPrevious1DayDelayVarAvgBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarAvgBidir.setStatus("current")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayVarAvgBidir.setUnits("microseconds")
_FadY1731CfmPMPrevious1DayDelayPDUDiscarded_Type = Counter32
_FadY1731CfmPMPrevious1DayDelayPDUDiscarded_Object = MibTableColumn
fadY1731CfmPMPrevious1DayDelayPDUDiscarded = _FadY1731CfmPMPrevious1DayDelayPDUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 15, 1, 24),
    _FadY1731CfmPMPrevious1DayDelayPDUDiscarded_Type()
)
fadY1731CfmPMPrevious1DayDelayPDUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadY1731CfmPMPrevious1DayDelayPDUDiscarded.setStatus("current")
_FadDot1agCfmMepLossRsltTable_Object = MibTable
fadDot1agCfmMepLossRsltTable = _FadDot1agCfmMepLossRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16)
)
if mibBuilder.loadTexts:
    fadDot1agCfmMepLossRsltTable.setStatus("current")
_FadDot1agCfmMepLossRsltEntry_Object = MibTableRow
fadDot1agCfmMepLossRsltEntry = _FadDot1agCfmMepLossRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1)
)
fadDot1agCfmMepLossRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IHUB-EXT-MIB", "fadDot1agCfmMepLmMacAddr"),
)
if mibBuilder.loadTexts:
    fadDot1agCfmMepLossRsltEntry.setStatus("current")
_FadDot1agCfmMepLmMacAddr_Type = MacAddress
_FadDot1agCfmMepLmMacAddr_Object = MibTableColumn
fadDot1agCfmMepLmMacAddr = _FadDot1agCfmMepLmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 1),
    _FadDot1agCfmMepLmMacAddr_Type()
)
fadDot1agCfmMepLmMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmMacAddr.setStatus("current")
_FadDot1agCfmMepLmPduSent_Type = Unsigned32
_FadDot1agCfmMepLmPduSent_Object = MibTableColumn
fadDot1agCfmMepLmPduSent = _FadDot1agCfmMepLmPduSent_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 2),
    _FadDot1agCfmMepLmPduSent_Type()
)
fadDot1agCfmMepLmPduSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmPduSent.setStatus("current")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmPduSent.setUnits("seconds")
_FadDot1agCfmMepLmPduReceived_Type = Unsigned32
_FadDot1agCfmMepLmPduReceived_Object = MibTableColumn
fadDot1agCfmMepLmPduReceived = _FadDot1agCfmMepLmPduReceived_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 3),
    _FadDot1agCfmMepLmPduReceived_Type()
)
fadDot1agCfmMepLmPduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmPduReceived.setStatus("current")
_FadDot1agCfmMepLmLatestChangeTime_Type = TimeStamp
_FadDot1agCfmMepLmLatestChangeTime_Object = MibTableColumn
fadDot1agCfmMepLmLatestChangeTime = _FadDot1agCfmMepLmLatestChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 4),
    _FadDot1agCfmMepLmLatestChangeTime_Type()
)
fadDot1agCfmMepLmLatestChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmLatestChangeTime.setStatus("current")
_FadDot1agCfmMepLmFramesRxLocal_Type = Counter64
_FadDot1agCfmMepLmFramesRxLocal_Object = MibTableColumn
fadDot1agCfmMepLmFramesRxLocal = _FadDot1agCfmMepLmFramesRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 5),
    _FadDot1agCfmMepLmFramesRxLocal_Type()
)
fadDot1agCfmMepLmFramesRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmFramesRxLocal.setStatus("current")
_FadDot1agCfmMepLmFramesRxPeer_Type = Counter64
_FadDot1agCfmMepLmFramesRxPeer_Object = MibTableColumn
fadDot1agCfmMepLmFramesRxPeer = _FadDot1agCfmMepLmFramesRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 6),
    _FadDot1agCfmMepLmFramesRxPeer_Type()
)
fadDot1agCfmMepLmFramesRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmFramesRxPeer.setStatus("current")
_FadDot1agCfmMepLmFramesTxLocal_Type = Counter64
_FadDot1agCfmMepLmFramesTxLocal_Object = MibTableColumn
fadDot1agCfmMepLmFramesTxLocal = _FadDot1agCfmMepLmFramesTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 7),
    _FadDot1agCfmMepLmFramesTxLocal_Type()
)
fadDot1agCfmMepLmFramesTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmFramesTxLocal.setStatus("current")
_FadDot1agCfmMepLmFramesTxPeer_Type = Counter64
_FadDot1agCfmMepLmFramesTxPeer_Object = MibTableColumn
fadDot1agCfmMepLmFramesTxPeer = _FadDot1agCfmMepLmFramesTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 8),
    _FadDot1agCfmMepLmFramesTxPeer_Type()
)
fadDot1agCfmMepLmFramesTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmFramesTxPeer.setStatus("current")
_FadDot1agCfmMepLmFramesLossLocal_Type = Counter64
_FadDot1agCfmMepLmFramesLossLocal_Object = MibTableColumn
fadDot1agCfmMepLmFramesLossLocal = _FadDot1agCfmMepLmFramesLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 9),
    _FadDot1agCfmMepLmFramesLossLocal_Type()
)
fadDot1agCfmMepLmFramesLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmFramesLossLocal.setStatus("current")
_FadDot1agCfmMepLmFramesLossPeer_Type = Counter64
_FadDot1agCfmMepLmFramesLossPeer_Object = MibTableColumn
fadDot1agCfmMepLmFramesLossPeer = _FadDot1agCfmMepLmFramesLossPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 10),
    _FadDot1agCfmMepLmFramesLossPeer_Type()
)
fadDot1agCfmMepLmFramesLossPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmFramesLossPeer.setStatus("current")
_FadDot1agCfmMepLmLossRatioLocal_Type = TLossRatioHundrethsOfPercent
_FadDot1agCfmMepLmLossRatioLocal_Object = MibTableColumn
fadDot1agCfmMepLmLossRatioLocal = _FadDot1agCfmMepLmLossRatioLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 11),
    _FadDot1agCfmMepLmLossRatioLocal_Type()
)
fadDot1agCfmMepLmLossRatioLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmLossRatioLocal.setStatus("current")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmLossRatioLocal.setUnits("hundredth of a percent")
_FadDot1agCfmMepLmLossRatioPeer_Type = TLossRatioHundrethsOfPercent
_FadDot1agCfmMepLmLossRatioPeer_Object = MibTableColumn
fadDot1agCfmMepLmLossRatioPeer = _FadDot1agCfmMepLmLossRatioPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 12),
    _FadDot1agCfmMepLmLossRatioPeer_Type()
)
fadDot1agCfmMepLmLossRatioPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmLossRatioPeer.setStatus("current")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmLossRatioPeer.setUnits("hundredth of a percent")
_FadDot1agCfmMepLmPrevTxLocal_Type = Counter32
_FadDot1agCfmMepLmPrevTxLocal_Object = MibTableColumn
fadDot1agCfmMepLmPrevTxLocal = _FadDot1agCfmMepLmPrevTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 13),
    _FadDot1agCfmMepLmPrevTxLocal_Type()
)
fadDot1agCfmMepLmPrevTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmPrevTxLocal.setStatus("current")
_FadDot1agCfmMepLmPrevRxLocal_Type = Counter32
_FadDot1agCfmMepLmPrevRxLocal_Object = MibTableColumn
fadDot1agCfmMepLmPrevRxLocal = _FadDot1agCfmMepLmPrevRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 14),
    _FadDot1agCfmMepLmPrevRxLocal_Type()
)
fadDot1agCfmMepLmPrevRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmPrevRxLocal.setStatus("current")
_FadDot1agCfmMepLmPrevTxPeer_Type = Counter32
_FadDot1agCfmMepLmPrevTxPeer_Object = MibTableColumn
fadDot1agCfmMepLmPrevTxPeer = _FadDot1agCfmMepLmPrevTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 15),
    _FadDot1agCfmMepLmPrevTxPeer_Type()
)
fadDot1agCfmMepLmPrevTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmPrevTxPeer.setStatus("current")
_FadDot1agCfmMepLmPrevRxPeer_Type = Counter32
_FadDot1agCfmMepLmPrevRxPeer_Object = MibTableColumn
fadDot1agCfmMepLmPrevRxPeer = _FadDot1agCfmMepLmPrevRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 16),
    _FadDot1agCfmMepLmPrevRxPeer_Type()
)
fadDot1agCfmMepLmPrevRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmPrevRxPeer.setStatus("current")
_FadDot1agCfmMepLmCurrTxLocal_Type = Counter32
_FadDot1agCfmMepLmCurrTxLocal_Object = MibTableColumn
fadDot1agCfmMepLmCurrTxLocal = _FadDot1agCfmMepLmCurrTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 17),
    _FadDot1agCfmMepLmCurrTxLocal_Type()
)
fadDot1agCfmMepLmCurrTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmCurrTxLocal.setStatus("current")
_FadDot1agCfmMepLmCurrRxLocal_Type = Counter32
_FadDot1agCfmMepLmCurrRxLocal_Object = MibTableColumn
fadDot1agCfmMepLmCurrRxLocal = _FadDot1agCfmMepLmCurrRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 18),
    _FadDot1agCfmMepLmCurrRxLocal_Type()
)
fadDot1agCfmMepLmCurrRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmCurrRxLocal.setStatus("current")
_FadDot1agCfmMepLmCurrTxPeer_Type = Counter32
_FadDot1agCfmMepLmCurrTxPeer_Object = MibTableColumn
fadDot1agCfmMepLmCurrTxPeer = _FadDot1agCfmMepLmCurrTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 19),
    _FadDot1agCfmMepLmCurrTxPeer_Type()
)
fadDot1agCfmMepLmCurrTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmCurrTxPeer.setStatus("current")
_FadDot1agCfmMepLmCurrRxPeer_Type = Counter32
_FadDot1agCfmMepLmCurrRxPeer_Object = MibTableColumn
fadDot1agCfmMepLmCurrRxPeer = _FadDot1agCfmMepLmCurrRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 20),
    _FadDot1agCfmMepLmCurrRxPeer_Type()
)
fadDot1agCfmMepLmCurrRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmCurrRxPeer.setStatus("current")
_FadDot1agCfmMepLmEnableDuration_Type = Unsigned32
_FadDot1agCfmMepLmEnableDuration_Object = MibTableColumn
fadDot1agCfmMepLmEnableDuration = _FadDot1agCfmMepLmEnableDuration_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 21),
    _FadDot1agCfmMepLmEnableDuration_Type()
)
fadDot1agCfmMepLmEnableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmEnableDuration.setStatus("current")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmEnableDuration.setUnits("seconds")
_FadDot1agCfmMepLmChangeCount_Type = Unsigned32
_FadDot1agCfmMepLmChangeCount_Object = MibTableColumn
fadDot1agCfmMepLmChangeCount = _FadDot1agCfmMepLmChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 19, 16, 1, 22),
    _FadDot1agCfmMepLmChangeCount_Type()
)
fadDot1agCfmMepLmChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadDot1agCfmMepLmChangeCount.setStatus("current")
_FadSysDot1qEtypeExt_ObjectIdentity = ObjectIdentity
fadSysDot1qEtypeExt = _FadSysDot1qEtypeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 20)
)


class _FadSysDefaultVlanDot1qEtype_Type(Unsigned32):
    """Custom type fadSysDefaultVlanDot1qEtype based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_FadSysDefaultVlanDot1qEtype_Type.__name__ = "Unsigned32"
_FadSysDefaultVlanDot1qEtype_Object = MibScalar
fadSysDefaultVlanDot1qEtype = _FadSysDefaultVlanDot1qEtype_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 20, 1),
    _FadSysDefaultVlanDot1qEtype_Type()
)
fadSysDefaultVlanDot1qEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadSysDefaultVlanDot1qEtype.setStatus("current")
_FadvRtrExt_ObjectIdentity = ObjectIdentity
fadvRtrExt = _FadvRtrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 21)
)
_FadvRtrIfExtTable_Object = MibTable
fadvRtrIfExtTable = _FadvRtrIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 21, 1)
)
if mibBuilder.loadTexts:
    fadvRtrIfExtTable.setStatus("current")
_FadvRtrIfExtEntry_Object = MibTableRow
fadvRtrIfExtEntry = _FadvRtrIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 21, 1, 1)
)
if mibBuilder.loadTexts:
    fadvRtrIfExtEntry.setStatus("current")


class _FadvRtrIfIngressQosLsrPolicyId_Type(TNetworkPolicyID):
    """Custom type fadvRtrIfIngressQosLsrPolicyId based on TNetworkPolicyID"""
    defaultValue = 1


_FadvRtrIfIngressQosLsrPolicyId_Type.__name__ = "TNetworkPolicyID"
_FadvRtrIfIngressQosLsrPolicyId_Object = MibTableColumn
fadvRtrIfIngressQosLsrPolicyId = _FadvRtrIfIngressQosLsrPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 21, 1, 1, 1),
    _FadvRtrIfIngressQosLsrPolicyId_Type()
)
fadvRtrIfIngressQosLsrPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fadvRtrIfIngressQosLsrPolicyId.setStatus("current")
_FadMplsNameMapper_ObjectIdentity = ObjectIdentity
fadMplsNameMapper = _FadMplsNameMapper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22)
)
_FadMplsTunnelNameMapperTable_Object = MibTable
fadMplsTunnelNameMapperTable = _FadMplsTunnelNameMapperTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22, 1)
)
if mibBuilder.loadTexts:
    fadMplsTunnelNameMapperTable.setStatus("current")
_FadMplsTunnelNameMapperEntry_Object = MibTableRow
fadMplsTunnelNameMapperEntry = _FadMplsTunnelNameMapperEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22, 1, 1)
)
fadMplsTunnelNameMapperEntry.setIndexNames(
    (0, "IHUB-EXT-MIB", "fadMplsTunnelName"),
)
if mibBuilder.loadTexts:
    fadMplsTunnelNameMapperEntry.setStatus("current")
_FadMplsTunnelName_Type = TNamedItem
_FadMplsTunnelName_Object = MibTableColumn
fadMplsTunnelName = _FadMplsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22, 1, 1, 1),
    _FadMplsTunnelName_Type()
)
fadMplsTunnelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadMplsTunnelName.setStatus("current")
_FadMplsTunnelIndex_Type = MplsTunnelIndex
_FadMplsTunnelIndex_Object = MibTableColumn
fadMplsTunnelIndex = _FadMplsTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22, 1, 1, 2),
    _FadMplsTunnelIndex_Type()
)
fadMplsTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadMplsTunnelIndex.setStatus("current")
_FadMplsLspNameMapperTable_Object = MibTable
fadMplsLspNameMapperTable = _FadMplsLspNameMapperTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22, 2)
)
if mibBuilder.loadTexts:
    fadMplsLspNameMapperTable.setStatus("current")
_FadMplsLspNameMapperEntry_Object = MibTableRow
fadMplsLspNameMapperEntry = _FadMplsLspNameMapperEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22, 2, 1)
)
fadMplsLspNameMapperEntry.setIndexNames(
    (0, "IHUB-EXT-MIB", "fadvRtrMplsLspName"),
)
if mibBuilder.loadTexts:
    fadMplsLspNameMapperEntry.setStatus("current")
_FadvRtrMplsLspName_Type = TNamedItem
_FadvRtrMplsLspName_Object = MibTableColumn
fadvRtrMplsLspName = _FadvRtrMplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22, 2, 1, 1),
    _FadvRtrMplsLspName_Type()
)
fadvRtrMplsLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadvRtrMplsLspName.setStatus("current")
_FadvRtrMplsLspIndex_Type = TmnxVRtrMplsLspID
_FadvRtrMplsLspIndex_Object = MibTableColumn
fadvRtrMplsLspIndex = _FadvRtrMplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 22, 2, 1, 2),
    _FadvRtrMplsLspIndex_Type()
)
fadvRtrMplsLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadvRtrMplsLspIndex.setStatus("current")
tmnxPortEtherEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadPortExtEntry")
)
fadPortExtEntry.setIndexNames(*tmnxPortEtherEntry.getIndexNames())
tmnxPortEtherEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadPortExtStatsEntry")
)
fadPortExtStatsEntry.setIndexNames(*tmnxPortEtherEntry.getIndexNames())
svcBaseInfoEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadSvcBaseExtEntry")
)
fadSvcBaseExtEntry.setIndexNames(*svcBaseInfoEntry.getIndexNames())
svcTlsInfoEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadSvcTlsExtEntry")
)
fadSvcTlsExtEntry.setIndexNames(*svcTlsInfoEntry.getIndexNames())
iesIfEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadIesIfExtEntry")
)
fadIesIfExtEntry.setIndexNames(*iesIfEntry.getIndexNames())
tCpmIpFilterEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadCpmIpFilterExtEntry")
)
fadCpmIpFilterExtEntry.setIndexNames(*tCpmIpFilterEntry.getIndexNames())
vRtrConfEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadVrtrV6ExtEntry")
)
fadVrtrV6ExtEntry.setIndexNames(*vRtrConfEntry.getIndexNames())
dot3adAggPortEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadLagPortEntry")
)
fadLagPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
tLagConfigEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadLagConfigExtEntry")
)
fadLagConfigExtEntry.setIndexNames(*tLagConfigEntry.getIndexNames())
tmnxNtpServersEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadNtpExtServersEntry")
)
fadNtpExtServersEntry.setIndexNames(*tmnxNtpServersEntry.getIndexNames())
sapBaseInfoEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadSapBaseInfoExtEntry")
)
fadSapBaseInfoExtEntry.setIndexNames(*sapBaseInfoEntry.getIndexNames())
sapBaseInfoEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadSapStatsConfigEntry")
)
fadSapStatsConfigEntry.setIndexNames(*sapBaseInfoEntry.getIndexNames())
sapBaseStatsEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadSapStatsEntry")
)
fadSapStatsEntry.setIndexNames(*sapBaseStatsEntry.getIndexNames())
tmnxDot1agCfmStackEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadDot1agCfmStackEntry")
)
fadDot1agCfmStackEntry.setIndexNames(*tmnxDot1agCfmStackEntry.getIndexNames())
tmnxDot1agCfmSdpBindStackEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadDot1agCfmSdpBindStackEntry")
)
fadDot1agCfmSdpBindStackEntry.setIndexNames(*tmnxDot1agCfmSdpBindStackEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadDot1agCfmMepEntry")
)
fadDot1agCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
tmnxDot1agCfmSapMipEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadDot1agCfmSapMipEntry")
)
fadDot1agCfmSapMipEntry.setIndexNames(*tmnxDot1agCfmSapMipEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("IHUB-EXT-MIB",
     "fadvRtrIfExtEntry")
)
fadvRtrIfExtEntry.setIndexNames(*vRtrIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fadPortConfigMismatchReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 2, 1)
)
fadPortConfigMismatchReport.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    fadPortConfigMismatchReport.setStatus(
        "current"
    )

fadPortConfigMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 1, 2, 2)
)
fadPortConfigMismatchClear.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    fadPortConfigMismatchClear.setStatus(
        "current"
    )

fadDupMacOccurence = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 2, 1)
)
fadDupMacOccurence.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("IHUB-EXT-MIB", "fadDupMacAddr"),
        ("IHUB-EXT-MIB", "fadDupMacSapPortId"),
        ("IHUB-EXT-MIB", "fadDupMacSapEncapValue"),
        ("IHUB-EXT-MIB", "fadDupMacSdpBindId"),
        ("IHUB-EXT-MIB", "fadDupMacDupCVlan"),
        ("IHUB-EXT-MIB", "fadDupMacDupSapPortId"),
        ("IHUB-EXT-MIB", "fadDupMacDupSapEncapValue"),
        ("IHUB-EXT-MIB", "fadDupMacDupSdpBindId"),
        ("IHUB-EXT-MIB", "fadDupMacIndex"),
        ("IHUB-EXT-MIB", "fadDupMacType"))
)
if mibBuilder.loadTexts:
    fadDupMacOccurence.setStatus(
        "current"
    )

fadDupMacClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 6, 2, 2)
)
fadDupMacClear.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("IHUB-EXT-MIB", "fadDupMacAddr"),
        ("IHUB-EXT-MIB", "fadDupMacSapPortId"),
        ("IHUB-EXT-MIB", "fadDupMacSapEncapValue"),
        ("IHUB-EXT-MIB", "fadDupMacSdpBindId"),
        ("IHUB-EXT-MIB", "fadDupMacDupCVlan"),
        ("IHUB-EXT-MIB", "fadDupMacDupSapPortId"),
        ("IHUB-EXT-MIB", "fadDupMacDupSapEncapValue"),
        ("IHUB-EXT-MIB", "fadDupMacDupSdpBindId"),
        ("IHUB-EXT-MIB", "fadDupMacIndex"),
        ("IHUB-EXT-MIB", "fadDupMacType"))
)
if mibBuilder.loadTexts:
    fadDupMacClear.setStatus(
        "current"
    )

fadOspfLsdbOverflowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 7, 2, 1)
)
fadOspfLsdbOverflowClear.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    fadOspfLsdbOverflowClear.setStatus(
        "current"
    )

fadOspfLsdbApproachingOverflowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 7, 2, 2)
)
fadOspfLsdbApproachingOverflowClear.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    fadOspfLsdbApproachingOverflowClear.setStatus(
        "current"
    )

fadOspfInstanceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 7, 2, 3)
)
fadOspfInstanceStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdminState"),
        ("IHUB-EXT-MIB", "fadOspfOperState"))
)
if mibBuilder.loadTexts:
    fadOspfInstanceStateChange.setStatus(
        "current"
    )

fadBgpMaxNgPrefix90Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 8, 1, 1)
)
fadBgpMaxNgPrefix90Clear.setObjects(
    ("TIMETRA-BGP-MIB", "tBgpPeerNgMaxPrefix")
)
if mibBuilder.loadTexts:
    fadBgpMaxNgPrefix90Clear.setStatus(
        "current"
    )

fadIsisInstanceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 10, 2, 1)
)
fadIsisInstanceStateChange.setObjects(
      *(("ISIS-MIB", "isisSysAdminState"),
        ("TIMETRA-ISIS-MIB", "vRtrIsisOperState"))
)
if mibBuilder.loadTexts:
    fadIsisInstanceStateChange.setStatus(
        "current"
    )

fadMaxNbrCacheEntriesTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 2, 1)
)
fadMaxNbrCacheEntriesTCA.setObjects(
    ("IHUB-EXT-MIB", "fadMaxNbrCacheEntries")
)
if mibBuilder.loadTexts:
    fadMaxNbrCacheEntriesTCA.setStatus(
        "current"
    )

fadMaxNbrCacheEntriesCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 85, 11, 2, 2)
)
fadMaxNbrCacheEntriesCleared.setObjects(
    ("IHUB-EXT-MIB", "fadMaxNbrCacheEntries")
)
if mibBuilder.loadTexts:
    fadMaxNbrCacheEntriesCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IHUB-EXT-MIB",
    **{"IhubRateLimitBurstSize": IhubRateLimitBurstSize,
       "THundredthsOfPercent": THundredthsOfPercent,
       "TLossRatioHundrethsOfPercent": TLossRatioHundrethsOfPercent,
       "EthCfmY1731PMType": EthCfmY1731PMType,
       "ihubExtMIB": ihubExtMIB,
       "fadPortExt": fadPortExt,
       "fadPortExtTable": fadPortExtTable,
       "fadPortExtEntry": fadPortExtEntry,
       "fadPortExtType": fadPortExtType,
       "fadPortExtBurstSize": fadPortExtBurstSize,
       "fadPortExtEgressRate": fadPortExtEgressRate,
       "fadPortExtLoopbackMode": fadPortExtLoopbackMode,
       "fadPortExtLoopbackVlan": fadPortExtLoopbackVlan,
       "fadPortExtQosRemarkConfig": fadPortExtQosRemarkConfig,
       "fadPortStateChangeCount": fadPortStateChangeCount,
       "fadPortExtUseVlanDot1qEtype": fadPortExtUseVlanDot1qEtype,
       "fadPortExtUsedOutputBwThreshold": fadPortExtUsedOutputBwThreshold,
       "fadPortExtUsedInputBwThreshold": fadPortExtUsedInputBwThreshold,
       "fadPortExtRxCRCAlignErrorsThreshold": fadPortExtRxCRCAlignErrorsThreshold,
       "fadPortExtTxCRCAlignErrorsThreshold": fadPortExtTxCRCAlignErrorsThreshold,
       "fadPortExtTxCollisionsThreshold": fadPortExtTxCollisionsThreshold,
       "fadPortExtTcaInterval": fadPortExtTcaInterval,
       "fadPortExtSuppressLinkStateAlarm": fadPortExtSuppressLinkStateAlarm,
       "fadPortExtNotifications": fadPortExtNotifications,
       "fadPortConfigMismatchReport": fadPortConfigMismatchReport,
       "fadPortConfigMismatchClear": fadPortConfigMismatchClear,
       "fadPortExtStatistics": fadPortExtStatistics,
       "fadPortExtStatsTable": fadPortExtStatsTable,
       "fadPortExtStatsEntry": fadPortExtStatsEntry,
       "fadPortExtStatsRxPkts64Octets": fadPortExtStatsRxPkts64Octets,
       "fadPortExtStatsTxPkts64Octets": fadPortExtStatsTxPkts64Octets,
       "fadPortExtStatsRxPkts65to127Octets": fadPortExtStatsRxPkts65to127Octets,
       "fadPortExtStatsTxPkts65to127Octets": fadPortExtStatsTxPkts65to127Octets,
       "fadPortExtStatsRxPkts128to255Octets": fadPortExtStatsRxPkts128to255Octets,
       "fadPortExtStatsTxPkts128to255Octets": fadPortExtStatsTxPkts128to255Octets,
       "fadPortExtStatsRxPkts256to511Octets": fadPortExtStatsRxPkts256to511Octets,
       "fadPortExtStatsTxPkts256to511Octets": fadPortExtStatsTxPkts256to511Octets,
       "fadPortExtStatsRxPkts512to1023Octets": fadPortExtStatsRxPkts512to1023Octets,
       "fadPortExtStatsTxPkts512to1023Octets": fadPortExtStatsTxPkts512to1023Octets,
       "fadPortExtStatsRxPkts1024to1518Octets": fadPortExtStatsRxPkts1024to1518Octets,
       "fadPortExtStatsTxPkts1024to1518Octets": fadPortExtStatsTxPkts1024to1518Octets,
       "fadPortExtStatsRxOversizePkts": fadPortExtStatsRxOversizePkts,
       "fadPortExtStatsTxOversizePkts": fadPortExtStatsTxOversizePkts,
       "fadPortExtStatsRxFragments": fadPortExtStatsRxFragments,
       "fadPortExtStatsTxFragments": fadPortExtStatsTxFragments,
       "fadPortExtStatsRxJabbers": fadPortExtStatsRxJabbers,
       "fadPortExtStatsTxJabbers": fadPortExtStatsTxJabbers,
       "fadPortExtStatsRxUndersizePkts": fadPortExtStatsRxUndersizePkts,
       "fadPortExtStatsTxUndersizePkts": fadPortExtStatsTxUndersizePkts,
       "fadPortExtStatsRxDropEvents": fadPortExtStatsRxDropEvents,
       "fadPortExtStatsTxDropEvents": fadPortExtStatsTxDropEvents,
       "fadPortExtStatsRxCRCAlignErrors": fadPortExtStatsRxCRCAlignErrors,
       "fadPortExtStatsTxCRCAlignErrors": fadPortExtStatsTxCRCAlignErrors,
       "fadPortExtPMStatistics": fadPortExtPMStatistics,
       "fadPortExtPMCurrent15MinIntervalTable": fadPortExtPMCurrent15MinIntervalTable,
       "fadPortExtPMCurrent15MinIntervalEntry": fadPortExtPMCurrent15MinIntervalEntry,
       "fadPortExtPMCurrent15MinTimeElapsed": fadPortExtPMCurrent15MinTimeElapsed,
       "fadPortExtPMCurrent15MinTimeMeasured": fadPortExtPMCurrent15MinTimeMeasured,
       "fadPortExtPMCurrent15MinInPackets": fadPortExtPMCurrent15MinInPackets,
       "fadPortExtPMCurrent15MinInOctets": fadPortExtPMCurrent15MinInOctets,
       "fadPortExtPMCurrent15MinInErrors": fadPortExtPMCurrent15MinInErrors,
       "fadPortExtPMCurrent15MinInPacketDrops": fadPortExtPMCurrent15MinInPacketDrops,
       "fadPortExtPMCurrent15MinInDiscards": fadPortExtPMCurrent15MinInDiscards,
       "fadPortExtPMCurrent15MinOutPackets": fadPortExtPMCurrent15MinOutPackets,
       "fadPortExtPMCurrent15MinOutOctets": fadPortExtPMCurrent15MinOutOctets,
       "fadPortExtPMCurrent15MinOutErrors": fadPortExtPMCurrent15MinOutErrors,
       "fadPortExtPMCurrent15MinOutPacketDrops": fadPortExtPMCurrent15MinOutPacketDrops,
       "fadPortExtPMCurrent15MinOutDiscards": fadPortExtPMCurrent15MinOutDiscards,
       "fadPortExtPM15MinValidIntervals": fadPortExtPM15MinValidIntervals,
       "fadPortExtPMCurrent15MinInvalidDataFlag": fadPortExtPMCurrent15MinInvalidDataFlag,
       "fadPortExtPMCurrent15MinOutputBw": fadPortExtPMCurrent15MinOutputBw,
       "fadPortExtPMCurrent15MinInputBw": fadPortExtPMCurrent15MinInputBw,
       "fadPortExtPMCurrent15MinRxCRCAlignErrors": fadPortExtPMCurrent15MinRxCRCAlignErrors,
       "fadPortExtPMCurrent15MinTxCRCAlignErrors": fadPortExtPMCurrent15MinTxCRCAlignErrors,
       "fadPortExtPMCurrent15MinTxCollisions": fadPortExtPMCurrent15MinTxCollisions,
       "fadPortExtPMCurrent1DayIntervalTable": fadPortExtPMCurrent1DayIntervalTable,
       "fadPortExtPMCurrent1DayIntervalEntry": fadPortExtPMCurrent1DayIntervalEntry,
       "fadPortExtPMCurrent1DayTimeElapsed": fadPortExtPMCurrent1DayTimeElapsed,
       "fadPortExtPMCurrent1DayTimeMeasured": fadPortExtPMCurrent1DayTimeMeasured,
       "fadPortExtPMCurrent1DayInPackets": fadPortExtPMCurrent1DayInPackets,
       "fadPortExtPMCurrent1DayInOctets": fadPortExtPMCurrent1DayInOctets,
       "fadPortExtPMCurrent1DayInErrors": fadPortExtPMCurrent1DayInErrors,
       "fadPortExtPMCurrent1DayInPacketDrops": fadPortExtPMCurrent1DayInPacketDrops,
       "fadPortExtPMCurrent1DayInDiscards": fadPortExtPMCurrent1DayInDiscards,
       "fadPortExtPMCurrent1DayOutPackets": fadPortExtPMCurrent1DayOutPackets,
       "fadPortExtPMCurrent1DayOutOctets": fadPortExtPMCurrent1DayOutOctets,
       "fadPortExtPMCurrent1DayOutErrors": fadPortExtPMCurrent1DayOutErrors,
       "fadPortExtPMCurrent1DayOutPacketDrops": fadPortExtPMCurrent1DayOutPacketDrops,
       "fadPortExtPMCurrent1DayOutDiscards": fadPortExtPMCurrent1DayOutDiscards,
       "fadPortExtPM1DayValidIntervals": fadPortExtPM1DayValidIntervals,
       "fadPortExtPMCurrent1DayInvalidDataFlag": fadPortExtPMCurrent1DayInvalidDataFlag,
       "fadPortExtPMPrevious15MinIntervalTable": fadPortExtPMPrevious15MinIntervalTable,
       "fadPortExtPMPrevious15MinIntervalEntry": fadPortExtPMPrevious15MinIntervalEntry,
       "fadPortExtPMPrevious15MinIntervalNumber": fadPortExtPMPrevious15MinIntervalNumber,
       "fadPortExtPMPrevious15MinTimeMeasured": fadPortExtPMPrevious15MinTimeMeasured,
       "fadPortExtPMPrevious15MinInPackets": fadPortExtPMPrevious15MinInPackets,
       "fadPortExtPMPrevious15MinInOctets": fadPortExtPMPrevious15MinInOctets,
       "fadPortExtPMPrevious15MinInErrors": fadPortExtPMPrevious15MinInErrors,
       "fadPortExtPMPrevious15MinInPacketDrops": fadPortExtPMPrevious15MinInPacketDrops,
       "fadPortExtPMPrevious15MinInDiscards": fadPortExtPMPrevious15MinInDiscards,
       "fadPortExtPMPrevious15MinOutPackets": fadPortExtPMPrevious15MinOutPackets,
       "fadPortExtPMPrevious15MinOutOctets": fadPortExtPMPrevious15MinOutOctets,
       "fadPortExtPMPrevious15MinOutErrors": fadPortExtPMPrevious15MinOutErrors,
       "fadPortExtPMPrevious15MinOutPacketDrops": fadPortExtPMPrevious15MinOutPacketDrops,
       "fadPortExtPMPrevious15MinOutDiscards": fadPortExtPMPrevious15MinOutDiscards,
       "fadPortExtPMPrevious15MinInvalidDataFlag": fadPortExtPMPrevious15MinInvalidDataFlag,
       "fadPortExtPMPrevious1DayIntervalTable": fadPortExtPMPrevious1DayIntervalTable,
       "fadPortExtPMPrevious1DayIntervalEntry": fadPortExtPMPrevious1DayIntervalEntry,
       "fadPortExtPMPrevious1DayIntervalNumber": fadPortExtPMPrevious1DayIntervalNumber,
       "fadPortExtPMPrevious1DayTimeMeasured": fadPortExtPMPrevious1DayTimeMeasured,
       "fadPortExtPMPrevious1DayInPackets": fadPortExtPMPrevious1DayInPackets,
       "fadPortExtPMPrevious1DayInOctets": fadPortExtPMPrevious1DayInOctets,
       "fadPortExtPMPrevious1DayInErrors": fadPortExtPMPrevious1DayInErrors,
       "fadPortExtPMPrevious1DayInPacketDrops": fadPortExtPMPrevious1DayInPacketDrops,
       "fadPortExtPMPrevious1DayInDiscards": fadPortExtPMPrevious1DayInDiscards,
       "fadPortExtPMPrevious1DayOutPackets": fadPortExtPMPrevious1DayOutPackets,
       "fadPortExtPMPrevious1DayOutOctets": fadPortExtPMPrevious1DayOutOctets,
       "fadPortExtPMPrevious1DayOutErrors": fadPortExtPMPrevious1DayOutErrors,
       "fadPortExtPMPrevious1DayOutPacketDrops": fadPortExtPMPrevious1DayOutPacketDrops,
       "fadPortExtPMPrevious1DayOutDiscards": fadPortExtPMPrevious1DayOutDiscards,
       "fadPortExtPMPrevious1DayInvalidDataFlag": fadPortExtPMPrevious1DayInvalidDataFlag,
       "fadSvcBaseExt": fadSvcBaseExt,
       "fadSvcBaseExtTable": fadSvcBaseExtTable,
       "fadSvcBaseExtEntry": fadSvcBaseExtEntry,
       "fadConfigIngressQosPolicyId": fadConfigIngressQosPolicyId,
       "fadActualIngressQosPolicyId": fadActualIngressQosPolicyId,
       "fadConfigSgtPolicyId": fadConfigSgtPolicyId,
       "fadActualSgtPolicyId": fadActualSgtPolicyId,
       "fadEgressCirRate": fadEgressCirRate,
       "fadEgressPirRate": fadEgressPirRate,
       "fadEgressCBurstSize": fadEgressCBurstSize,
       "fadEgressPBurstSize": fadEgressPBurstSize,
       "fadSgtPolicyOverride": fadSgtPolicyOverride,
       "fadIngressNetworkQosPolicyId": fadIngressNetworkQosPolicyId,
       "fadEgressNetworkQosPolicyId": fadEgressNetworkQosPolicyId,
       "fadVlanDot1qEtype": fadVlanDot1qEtype,
       "fadIngressCirRate": fadIngressCirRate,
       "fadIngressPirRate": fadIngressPirRate,
       "fadIngressCBurstSize": fadIngressCBurstSize,
       "fadIngressPBurstSize": fadIngressPBurstSize,
       "fadSvcEnableStormControl": fadSvcEnableStormControl,
       "fadSvcBaseExtNextFreeSvcId": fadSvcBaseExtNextFreeSvcId,
       "fadSvcBaseExtVlanTable": fadSvcBaseExtVlanTable,
       "fadSvcBaseExtVlanEntry": fadSvcBaseExtVlanEntry,
       "fadVplsSvcId": fadVplsSvcId,
       "fadSvcTlsExt": fadSvcTlsExt,
       "fadSvcTlsExtTable": fadSvcTlsExtTable,
       "fadSvcTlsExtEntry": fadSvcTlsExtEntry,
       "fadVplsU2uDistinctSaps": fadVplsU2uDistinctSaps,
       "fadVplsUnrestrictMacMove": fadVplsUnrestrictMacMove,
       "fadVplsExtFwdDeviceIpAddressType": fadVplsExtFwdDeviceIpAddressType,
       "fadVplsExtFwdDeviceIpAddress": fadVplsExtFwdDeviceIpAddress,
       "fadMirrorService": fadMirrorService,
       "fadMirrorSourceCpuTable": fadMirrorSourceCpuTable,
       "fadMirrorSourceCpuEntry": fadMirrorSourceCpuEntry,
       "fadMirrorSourceCpuPortIndex": fadMirrorSourceCpuPortIndex,
       "fadMirrorSourceCpuRowStatus": fadMirrorSourceCpuRowStatus,
       "fadMirrorSourceCpuEgressEnabled": fadMirrorSourceCpuEgressEnabled,
       "fadMirrorSourceCpuIngressEnabled": fadMirrorSourceCpuIngressEnabled,
       "fadMirrorSourceCpuLastChgd": fadMirrorSourceCpuLastChgd,
       "fadIesIfExt": fadIesIfExt,
       "fadIesIfExtTable": fadIesIfExtTable,
       "fadIesIfExtEntry": fadIesIfExtEntry,
       "fadIesIfUserGateway": fadIesIfUserGateway,
       "fadFdbExt": fadFdbExt,
       "fadFdbExtObjects": fadFdbExtObjects,
       "fadFdbExtNotifyObjs": fadFdbExtNotifyObjs,
       "fadDupMacIndex": fadDupMacIndex,
       "fadDupMacAddr": fadDupMacAddr,
       "fadDupMacSapPortId": fadDupMacSapPortId,
       "fadDupMacSapEncapValue": fadDupMacSapEncapValue,
       "fadDupMacDupCVlan": fadDupMacDupCVlan,
       "fadDupMacDupSapPortId": fadDupMacDupSapPortId,
       "fadDupMacDupSapEncapValue": fadDupMacDupSapEncapValue,
       "fadDupMacType": fadDupMacType,
       "fadDupMacSdpBindId": fadDupMacSdpBindId,
       "fadDupMacDupSdpBindId": fadDupMacDupSdpBindId,
       "fadFdbExtNotifications": fadFdbExtNotifications,
       "fadDupMacOccurence": fadDupMacOccurence,
       "fadDupMacClear": fadDupMacClear,
       "fadOspfExt": fadOspfExt,
       "fadOspfExtObjects": fadOspfExtObjects,
       "fadOspfOperState": fadOspfOperState,
       "fadOspfExtNotifications": fadOspfExtNotifications,
       "fadOspfLsdbOverflowClear": fadOspfLsdbOverflowClear,
       "fadOspfLsdbApproachingOverflowClear": fadOspfLsdbApproachingOverflowClear,
       "fadOspfInstanceStateChange": fadOspfInstanceStateChange,
       "fadBgpExt": fadBgpExt,
       "fadBgpExtNotifications": fadBgpExtNotifications,
       "fadBgpMaxNgPrefix90Clear": fadBgpMaxNgPrefix90Clear,
       "fadCpmIpFilterExt": fadCpmIpFilterExt,
       "fadCpmIpFilterExtTable": fadCpmIpFilterExtTable,
       "fadCpmIpFilterExtEntry": fadCpmIpFilterExtEntry,
       "fadSvcId": fadSvcId,
       "fadIsisExt": fadIsisExt,
       "fadIsisExtObjects": fadIsisExtObjects,
       "fadIsisExtNotifications": fadIsisExtNotifications,
       "fadIsisInstanceStateChange": fadIsisInstanceStateChange,
       "fadIPv6Ext": fadIPv6Ext,
       "fadIPv6ExtObjects": fadIPv6ExtObjects,
       "fadVrtrV6ExtTable": fadVrtrV6ExtTable,
       "fadVrtrV6ExtEntry": fadVrtrV6ExtEntry,
       "fadVrtrV6ManagedRoutes": fadVrtrV6ManagedRoutes,
       "fadVrtrV6ManagedActiveRoutes": fadVrtrV6ManagedActiveRoutes,
       "fadVrtrV6StatConfiguredIfs": fadVrtrV6StatConfiguredIfs,
       "fadDhcp6RouteTable": fadDhcp6RouteTable,
       "fadDhcp6RouteEntry": fadDhcp6RouteEntry,
       "fadDhcp6RouteDestType": fadDhcp6RouteDestType,
       "fadDhcp6RouteDest": fadDhcp6RouteDest,
       "fadDhcp6RoutePfxLen": fadDhcp6RoutePfxLen,
       "fadDhcp6RouteNextHopType": fadDhcp6RouteNextHopType,
       "fadDhcp6RouteNextHop": fadDhcp6RouteNextHop,
       "fadDhcp6RouteStatus": fadDhcp6RouteStatus,
       "fadIPv6ExtNotifications": fadIPv6ExtNotifications,
       "fadMaxNbrCacheEntriesTCA": fadMaxNbrCacheEntriesTCA,
       "fadMaxNbrCacheEntriesCleared": fadMaxNbrCacheEntriesCleared,
       "fadIPv6ExtNotifyObjects": fadIPv6ExtNotifyObjects,
       "fadMaxNbrCacheEntries": fadMaxNbrCacheEntries,
       "fadL2L3FilterExt": fadL2L3FilterExt,
       "fadFilterMode": fadFilterMode,
       "fadMaxNumberIngressL2Filters": fadMaxNumberIngressL2Filters,
       "fadMaxNumberIngressL3Filters": fadMaxNumberIngressL3Filters,
       "fadSourceIpExt": fadSourceIpExt,
       "fadSourceIpExtTable": fadSourceIpExtTable,
       "fadSourceIpExtEntry": fadSourceIpExtEntry,
       "fadSourceIpExtAddrType": fadSourceIpExtAddrType,
       "fadSourceIpExtRowStatus": fadSourceIpExtRowStatus,
       "fadMacIpFilterExt": fadMacIpFilterExt,
       "fadNextFreeIpFilterId": fadNextFreeIpFilterId,
       "fadNextFreeIpv6FilterId": fadNextFreeIpv6FilterId,
       "fadNextFreeMacFilterId": fadNextFreeMacFilterId,
       "fadLagExt": fadLagExt,
       "fadLagPortTable": fadLagPortTable,
       "fadLagPortEntry": fadLagPortEntry,
       "fadLagPortSubgroup": fadLagPortSubgroup,
       "fadLagConfigExtTable": fadLagConfigExtTable,
       "fadLagConfigExtEntry": fadLagConfigExtEntry,
       "fadLagActiveSubgroup": fadLagActiveSubgroup,
       "fadLagForceSubgroupSelect": fadLagForceSubgroupSelect,
       "fadLagSubgroupSwitchCount": fadLagSubgroupSwitchCount,
       "fadLagSubgroupSwitchDetectTime": fadLagSubgroupSwitchDetectTime,
       "fadLagSubgroupTable": fadLagSubgroupTable,
       "fadLagSubgroupEntry": fadLagSubgroupEntry,
       "fadLagSubgroupIndex": fadLagSubgroupIndex,
       "fadLagSubgroupPreference": fadLagSubgroupPreference,
       "fadLagSubgroupThreshold": fadLagSubgroupThreshold,
       "fadNtpExt": fadNtpExt,
       "fadNtpExtSystem": fadNtpExtSystem,
       "fadNtpSysPollRate": fadNtpSysPollRate,
       "fadNtpExtServers": fadNtpExtServers,
       "fadNtpExtServersTable": fadNtpExtServersTable,
       "fadNtpExtServersEntry": fadNtpExtServersEntry,
       "fadNtpExtServersPort": fadNtpExtServersPort,
       "fadSapBaseExt": fadSapBaseExt,
       "fadSapBaseInfoExtTable": fadSapBaseInfoExtTable,
       "fadSapBaseInfoExtEntry": fadSapBaseInfoExtEntry,
       "fadRestrictedTagging": fadRestrictedTagging,
       "fadSapConfigPersistentControl": fadSapConfigPersistentControl,
       "fadSapBaseExtPM": fadSapBaseExtPM,
       "fadSapStatsConfigTable": fadSapStatsConfigTable,
       "fadSapStatsConfigEntry": fadSapStatsConfigEntry,
       "fadSapStatsStatus": fadSapStatsStatus,
       "fadSapStatsEnabledTime": fadSapStatsEnabledTime,
       "fadSapStatsTable": fadSapStatsTable,
       "fadSapStatsEntry": fadSapStatsEntry,
       "fadSapStatsIngressPkts": fadSapStatsIngressPkts,
       "fadSapStatsIngressOctets": fadSapStatsIngressOctets,
       "fadSapStatsEgressPkts": fadSapStatsEgressPkts,
       "fadSapStatsEgressOctets": fadSapStatsEgressOctets,
       "fadSapPMCurrent15MinIntervalTable": fadSapPMCurrent15MinIntervalTable,
       "fadSapPMCurrent15MinIntervalEntry": fadSapPMCurrent15MinIntervalEntry,
       "fadSapPMCurrent15MinTimeElapsed": fadSapPMCurrent15MinTimeElapsed,
       "fadSapPMCurrent15MinTimeMeasured": fadSapPMCurrent15MinTimeMeasured,
       "fadSapPMCurrent15MinIngressPkts": fadSapPMCurrent15MinIngressPkts,
       "fadSapPMCurrent15MinIngressOctets": fadSapPMCurrent15MinIngressOctets,
       "fadSapPMCurrent15MinEgressPkts": fadSapPMCurrent15MinEgressPkts,
       "fadSapPMCurrent15MinEgressOctets": fadSapPMCurrent15MinEgressOctets,
       "fadSapPM15MinValidIntervals": fadSapPM15MinValidIntervals,
       "fadSapPMCurrent1DayIntervalTable": fadSapPMCurrent1DayIntervalTable,
       "fadSapPMCurrent1DayIntervalEntry": fadSapPMCurrent1DayIntervalEntry,
       "fadSapPMCurrent1DayTimeElapsed": fadSapPMCurrent1DayTimeElapsed,
       "fadSapPMCurrent1DayTimeMeasured": fadSapPMCurrent1DayTimeMeasured,
       "fadSapPMCurrent1DayIngressPkts": fadSapPMCurrent1DayIngressPkts,
       "fadSapPMCurrent1DayIngressOctets": fadSapPMCurrent1DayIngressOctets,
       "fadSapPMCurrent1DayEgressPkts": fadSapPMCurrent1DayEgressPkts,
       "fadSapPMCurrent1DayEgressOctets": fadSapPMCurrent1DayEgressOctets,
       "fadSapPM1DayValidIntervals": fadSapPM1DayValidIntervals,
       "fadSapPMPrevious15MinIntervalTable": fadSapPMPrevious15MinIntervalTable,
       "fadSapPMPrevious15MinIntervalEntry": fadSapPMPrevious15MinIntervalEntry,
       "fadSapPMPrevious15MinIntervalNumber": fadSapPMPrevious15MinIntervalNumber,
       "fadSapPMPrevious15MinTimeMeasured": fadSapPMPrevious15MinTimeMeasured,
       "fadSapPMPrevious15MinIngressPkts": fadSapPMPrevious15MinIngressPkts,
       "fadSapPMPrevious15MinIngressOctets": fadSapPMPrevious15MinIngressOctets,
       "fadSapPMPrevious15MinEgressPkts": fadSapPMPrevious15MinEgressPkts,
       "fadSapPMPrevious15MinEgressOctets": fadSapPMPrevious15MinEgressOctets,
       "fadSapPMPrevious1DayIntervalTable": fadSapPMPrevious1DayIntervalTable,
       "fadSapPMPrevious1DayIntervalEntry": fadSapPMPrevious1DayIntervalEntry,
       "fadSapPMPrevious1DayIntervalNumber": fadSapPMPrevious1DayIntervalNumber,
       "fadSapPMPrevious1DayTimeMeasured": fadSapPMPrevious1DayTimeMeasured,
       "fadSapPMPrevious1DayIngressPkts": fadSapPMPrevious1DayIngressPkts,
       "fadSapPMPrevious1DayIngressOctets": fadSapPMPrevious1DayIngressOctets,
       "fadSapPMPrevious1DayEgressPkts": fadSapPMPrevious1DayEgressPkts,
       "fadSapPMPrevious1DayEgressOctets": fadSapPMPrevious1DayEgressOctets,
       "fadSysU2UExt": fadSysU2UExt,
       "fadSysU2USameSap": fadSysU2USameSap,
       "fadCfmExt": fadCfmExt,
       "fadNumCcmEnabledMeps": fadNumCcmEnabledMeps,
       "fadDot1agCfmStackTable": fadDot1agCfmStackTable,
       "fadDot1agCfmStackEntry": fadDot1agCfmStackEntry,
       "fadDot1agCfmSapMpOperStatus": fadDot1agCfmSapMpOperStatus,
       "fadDot1agCfmStackMpSvcId": fadDot1agCfmStackMpSvcId,
       "fadDot1agCfmSdpBindStackTable": fadDot1agCfmSdpBindStackTable,
       "fadDot1agCfmSdpBindStackEntry": fadDot1agCfmSdpBindStackEntry,
       "fadDot1agCfmSdpMpOperStatus": fadDot1agCfmSdpMpOperStatus,
       "fadDot1agCfmSdpBindMpSvcId": fadDot1agCfmSdpBindMpSvcId,
       "fadDot1agCfmMepTable": fadDot1agCfmMepTable,
       "fadDot1agCfmMepEntry": fadDot1agCfmMepEntry,
       "fadDot1agCfmMpSvcId": fadDot1agCfmMpSvcId,
       "fadDot1agCfmMepLbmTestTlvIncluded": fadDot1agCfmMepLbmTestTlvIncluded,
       "fadDot1agCfmMepLbmTestPattern": fadDot1agCfmMepLbmTestPattern,
       "fadDot1agCfmMepTransmitLbmTestTlvLen": fadDot1agCfmMepTransmitLbmTestTlvLen,
       "fadDot1agCfmMepLbrInBitErrors": fadDot1agCfmMepLbrInBitErrors,
       "fadDot1agCfmMepLbrInCrcErrors": fadDot1agCfmMepLbrInCrcErrors,
       "fadDot1agCfmMepY1731PmEnabled": fadDot1agCfmMepY1731PmEnabled,
       "fadDot1agCfmMepY1731SingleLMPriorityBmp": fadDot1agCfmMepY1731SingleLMPriorityBmp,
       "fadDot1agCfmMepSingleLMMacAddress": fadDot1agCfmMepSingleLMMacAddress,
       "fadDot1agCfmMepSingleLMPriority": fadDot1agCfmMepSingleLMPriority,
       "fadDot1agCfmMepSingleLMCount": fadDot1agCfmMepSingleLMCount,
       "fadDot1agCfmMepSingleLMInterval": fadDot1agCfmMepSingleLMInterval,
       "fadDot1agCfmSapMipTable": fadDot1agCfmSapMipTable,
       "fadDot1agCfmSapMipEntry": fadDot1agCfmSapMipEntry,
       "fadDot1agCfmMipSvcId": fadDot1agCfmMipSvcId,
       "fadY1731CfmNextFreeSessionId": fadY1731CfmNextFreeSessionId,
       "fadY1731CfmPMConfigTable": fadY1731CfmPMConfigTable,
       "fadY1731CfmPMConfigEntry": fadY1731CfmPMConfigEntry,
       "fadY1731CfmPMConfigSessionId": fadY1731CfmPMConfigSessionId,
       "fadY1731CfmPMConfigRowStatus": fadY1731CfmPMConfigRowStatus,
       "fadY1731CfmPMConfigMepMacAddress": fadY1731CfmPMConfigMepMacAddress,
       "fadY1731CfmPMConfigType": fadY1731CfmPMConfigType,
       "fadY1731CfmPMConfigAdminStatus": fadY1731CfmPMConfigAdminStatus,
       "fadY1731CfmPMConfigPriority": fadY1731CfmPMConfigPriority,
       "fadY1731CfmPMConfigInterval": fadY1731CfmPMConfigInterval,
       "fadY1731CfmPMConfigMeasurementInterval": fadY1731CfmPMConfigMeasurementInterval,
       "fadY1731CfmPMConfigDataSize": fadY1731CfmPMConfigDataSize,
       "fadY1731CfmPMCurrent15MinIntervalLossTable": fadY1731CfmPMCurrent15MinIntervalLossTable,
       "fadY1731CfmPMCurrent15MinIntervalLossEntry": fadY1731CfmPMCurrent15MinIntervalLossEntry,
       "fadY1731CfmPMCurrent15MinTestType": fadY1731CfmPMCurrent15MinTestType,
       "fadY1731CfmPMCurrent15MinTimeElapsed": fadY1731CfmPMCurrent15MinTimeElapsed,
       "fadY1731CfmPMCurrent15MinTimeMeasured": fadY1731CfmPMCurrent15MinTimeMeasured,
       "fadY1731CfmPM15MinValidIntervals": fadY1731CfmPM15MinValidIntervals,
       "fadY1731CfmPMCurrent15MinInvalidDataFlag": fadY1731CfmPMCurrent15MinInvalidDataFlag,
       "fadY1731CfmPMCurrent15MinPDUSent": fadY1731CfmPMCurrent15MinPDUSent,
       "fadY1731CfmPMCurrent15MinPDURecv": fadY1731CfmPMCurrent15MinPDURecv,
       "fadY1731CfmPMCurrent15MinRxLocal": fadY1731CfmPMCurrent15MinRxLocal,
       "fadY1731CfmPMCurrent15MinRxPeer": fadY1731CfmPMCurrent15MinRxPeer,
       "fadY1731CfmPMCurrent15MinTxLocal": fadY1731CfmPMCurrent15MinTxLocal,
       "fadY1731CfmPMCurrent15MinTxPeer": fadY1731CfmPMCurrent15MinTxPeer,
       "fadY1731CfmPMCurrent15MinLossLocal": fadY1731CfmPMCurrent15MinLossLocal,
       "fadY1731CfmPMCurrent15MinLossPeer": fadY1731CfmPMCurrent15MinLossPeer,
       "fadY1731CfmPMCurrent15MinLossRatioMinLocal": fadY1731CfmPMCurrent15MinLossRatioMinLocal,
       "fadY1731CfmPMCurrent15MinLossRatioMaxLocal": fadY1731CfmPMCurrent15MinLossRatioMaxLocal,
       "fadY1731CfmPMCurrent15MinLossRatioAvgLocal": fadY1731CfmPMCurrent15MinLossRatioAvgLocal,
       "fadY1731CfmPMCurrent15MinLossRatioMinPeer": fadY1731CfmPMCurrent15MinLossRatioMinPeer,
       "fadY1731CfmPMCurrent15MinLossRatioMaxPeer": fadY1731CfmPMCurrent15MinLossRatioMaxPeer,
       "fadY1731CfmPMCurrent15MinLossRatioAvgPeer": fadY1731CfmPMCurrent15MinLossRatioAvgPeer,
       "fadY1731CfmPMCurrent15MinTestId": fadY1731CfmPMCurrent15MinTestId,
       "fadY1731CfmPMCurrent15MinRemoteMepId": fadY1731CfmPMCurrent15MinRemoteMepId,
       "fadY1731CfmPMCurrent15MinUnack": fadY1731CfmPMCurrent15MinUnack,
       "fadY1731CfmPMCurrent15MinPDUDiscarded": fadY1731CfmPMCurrent15MinPDUDiscarded,
       "fadY1731CfmPMCurrent15MinDataSize": fadY1731CfmPMCurrent15MinDataSize,
       "fadY1731CfmPMCurrent1DayIntervalLossTable": fadY1731CfmPMCurrent1DayIntervalLossTable,
       "fadY1731CfmPMCurrent1DayIntervalLossEntry": fadY1731CfmPMCurrent1DayIntervalLossEntry,
       "fadY1731CfmPMCurrent1DayTestType": fadY1731CfmPMCurrent1DayTestType,
       "fadY1731CfmPMCurrent1DayTimeElapsed": fadY1731CfmPMCurrent1DayTimeElapsed,
       "fadY1731CfmPMCurrent1DayTimeMeasured": fadY1731CfmPMCurrent1DayTimeMeasured,
       "fadY1731CfmPM1DayValidIntervals": fadY1731CfmPM1DayValidIntervals,
       "fadY1731CfmPMCurrent1DayInvalidDataFlag": fadY1731CfmPMCurrent1DayInvalidDataFlag,
       "fadY1731CfmPMCurrent1DayPDUSent": fadY1731CfmPMCurrent1DayPDUSent,
       "fadY1731CfmPMCurrent1DayPDURecv": fadY1731CfmPMCurrent1DayPDURecv,
       "fadY1731CfmPMCurrent1DayRxLocal": fadY1731CfmPMCurrent1DayRxLocal,
       "fadY1731CfmPMCurrent1DayRxPeer": fadY1731CfmPMCurrent1DayRxPeer,
       "fadY1731CfmPMCurrent1DayTxLocal": fadY1731CfmPMCurrent1DayTxLocal,
       "fadY1731CfmPMCurrent1DayTxPeer": fadY1731CfmPMCurrent1DayTxPeer,
       "fadY1731CfmPMCurrent1DayLossLocal": fadY1731CfmPMCurrent1DayLossLocal,
       "fadY1731CfmPMCurrent1DayLossPeer": fadY1731CfmPMCurrent1DayLossPeer,
       "fadY1731CfmPMCurrent1DayLossRatioMinLocal": fadY1731CfmPMCurrent1DayLossRatioMinLocal,
       "fadY1731CfmPMCurrent1DayLossRatioMaxLocal": fadY1731CfmPMCurrent1DayLossRatioMaxLocal,
       "fadY1731CfmPMCurrent1DayLossRatioAvgLocal": fadY1731CfmPMCurrent1DayLossRatioAvgLocal,
       "fadY1731CfmPMCurrent1DayLossRatioMinPeer": fadY1731CfmPMCurrent1DayLossRatioMinPeer,
       "fadY1731CfmPMCurrent1DayLossRatioMaxPeer": fadY1731CfmPMCurrent1DayLossRatioMaxPeer,
       "fadY1731CfmPMCurrent1DayLossRatioAvgPeer": fadY1731CfmPMCurrent1DayLossRatioAvgPeer,
       "fadY1731CfmPMCurrent1DayTestId": fadY1731CfmPMCurrent1DayTestId,
       "fadY1731CfmPMCurrent1DayRemoteMepId": fadY1731CfmPMCurrent1DayRemoteMepId,
       "fadY1731CfmPMCurrent1DayUnack": fadY1731CfmPMCurrent1DayUnack,
       "fadY1731CfmPMCurrent1DayPDUDiscarded": fadY1731CfmPMCurrent1DayPDUDiscarded,
       "fadY1731CfmPMCurrent1DayDataSize": fadY1731CfmPMCurrent1DayDataSize,
       "fadY1731CfmPMPrevious15MinIntervalLossTable": fadY1731CfmPMPrevious15MinIntervalLossTable,
       "fadY1731CfmPMPrevious15MinIntervalLossEntry": fadY1731CfmPMPrevious15MinIntervalLossEntry,
       "fadY1731CfmPMPrevious15MinIntervalNumber": fadY1731CfmPMPrevious15MinIntervalNumber,
       "fadY1731CfmPMPrevious15MinTestType": fadY1731CfmPMPrevious15MinTestType,
       "fadY1731CfmPMPrevious15MinTimeMeasured": fadY1731CfmPMPrevious15MinTimeMeasured,
       "fadY1731CfmPMPrevious15MinInvalidDataFlag": fadY1731CfmPMPrevious15MinInvalidDataFlag,
       "fadY1731CfmPMPrevious15MinPDUSent": fadY1731CfmPMPrevious15MinPDUSent,
       "fadY1731CfmPMPrevious15MinPDURecv": fadY1731CfmPMPrevious15MinPDURecv,
       "fadY1731CfmPMPrevious15MinRxLocal": fadY1731CfmPMPrevious15MinRxLocal,
       "fadY1731CfmPMPrevious15MinRxPeer": fadY1731CfmPMPrevious15MinRxPeer,
       "fadY1731CfmPMPrevious15MinTxLocal": fadY1731CfmPMPrevious15MinTxLocal,
       "fadY1731CfmPMPrevious15MinTxPeer": fadY1731CfmPMPrevious15MinTxPeer,
       "fadY1731CfmPMPrevious15MinLossLocal": fadY1731CfmPMPrevious15MinLossLocal,
       "fadY1731CfmPMPrevious15MinLossPeer": fadY1731CfmPMPrevious15MinLossPeer,
       "fadY1731CfmPMPrevious15MinLossRatioMinLocal": fadY1731CfmPMPrevious15MinLossRatioMinLocal,
       "fadY1731CfmPMPrevious15MinLossRatioMaxLocal": fadY1731CfmPMPrevious15MinLossRatioMaxLocal,
       "fadY1731CfmPMPrevious15MinLossRatioAvgLocal": fadY1731CfmPMPrevious15MinLossRatioAvgLocal,
       "fadY1731CfmPMPrevious15MinLossRatioMinPeer": fadY1731CfmPMPrevious15MinLossRatioMinPeer,
       "fadY1731CfmPMPrevious15MinLossRatioMaxPeer": fadY1731CfmPMPrevious15MinLossRatioMaxPeer,
       "fadY1731CfmPMPrevious15MinLossRatioAvgPeer": fadY1731CfmPMPrevious15MinLossRatioAvgPeer,
       "fadY1731CfmPMPrevious15MinTestId": fadY1731CfmPMPrevious15MinTestId,
       "fadY1731CfmPMPrevious15MinRemoteMepId": fadY1731CfmPMPrevious15MinRemoteMepId,
       "fadY1731CfmPMPrevious15MinUnack": fadY1731CfmPMPrevious15MinUnack,
       "fadY1731CfmPMPrevious15MinPDUDiscarded": fadY1731CfmPMPrevious15MinPDUDiscarded,
       "fadY1731CfmPMPrevious15MinDataSize": fadY1731CfmPMPrevious15MinDataSize,
       "fadY1731CfmPMPrevious1DayIntervalLossTable": fadY1731CfmPMPrevious1DayIntervalLossTable,
       "fadY1731CfmPMPrevious1DayIntervalLossEntry": fadY1731CfmPMPrevious1DayIntervalLossEntry,
       "fadY1731CfmPMPrevious1DayIntervalNumber": fadY1731CfmPMPrevious1DayIntervalNumber,
       "fadY1731CfmPMPrevious1DayTestType": fadY1731CfmPMPrevious1DayTestType,
       "fadY1731CfmPMPrevious1DayTimeMeasured": fadY1731CfmPMPrevious1DayTimeMeasured,
       "fadY1731CfmPMPrevious1DayInvalidDataFlag": fadY1731CfmPMPrevious1DayInvalidDataFlag,
       "fadY1731CfmPMPrevious1DayPDUSent": fadY1731CfmPMPrevious1DayPDUSent,
       "fadY1731CfmPMPrevious1DayPDURecv": fadY1731CfmPMPrevious1DayPDURecv,
       "fadY1731CfmPMPrevious1DayRxLocal": fadY1731CfmPMPrevious1DayRxLocal,
       "fadY1731CfmPMPrevious1DayRxPeer": fadY1731CfmPMPrevious1DayRxPeer,
       "fadY1731CfmPMPrevious1DayTxLocal": fadY1731CfmPMPrevious1DayTxLocal,
       "fadY1731CfmPMPrevious1DayTxPeer": fadY1731CfmPMPrevious1DayTxPeer,
       "fadY1731CfmPMPrevious1DayLossLocal": fadY1731CfmPMPrevious1DayLossLocal,
       "fadY1731CfmPMPrevious1DayLossPeer": fadY1731CfmPMPrevious1DayLossPeer,
       "fadY1731CfmPMPrevious1DayLossRatioMinLocal": fadY1731CfmPMPrevious1DayLossRatioMinLocal,
       "fadY1731CfmPMPrevious1DayLossRatioMaxLocal": fadY1731CfmPMPrevious1DayLossRatioMaxLocal,
       "fadY1731CfmPMPrevious1DayLossRatioAvgLocal": fadY1731CfmPMPrevious1DayLossRatioAvgLocal,
       "fadY1731CfmPMPrevious1DayLossRatioMinPeer": fadY1731CfmPMPrevious1DayLossRatioMinPeer,
       "fadY1731CfmPMPrevious1DayLossRatioMaxPeer": fadY1731CfmPMPrevious1DayLossRatioMaxPeer,
       "fadY1731CfmPMPrevious1DayLossRatioAvgPeer": fadY1731CfmPMPrevious1DayLossRatioAvgPeer,
       "fadY1731CfmPMPrevious1DayTestId": fadY1731CfmPMPrevious1DayTestId,
       "fadY1731CfmPMPrevious1DayRemoteMepId": fadY1731CfmPMPrevious1DayRemoteMepId,
       "fadY1731CfmPMPrevious1DayUnack": fadY1731CfmPMPrevious1DayUnack,
       "fadY1731CfmPMPrevious1DayPDUDiscarded": fadY1731CfmPMPrevious1DayPDUDiscarded,
       "fadY1731CfmPMPrevious1DayDataSize": fadY1731CfmPMPrevious1DayDataSize,
       "fadY1731CfmPMCurrent15MinIntervalDelayTable": fadY1731CfmPMCurrent15MinIntervalDelayTable,
       "fadY1731CfmPMCurrent15MinIntervalDelayEntry": fadY1731CfmPMCurrent15MinIntervalDelayEntry,
       "fadY1731CfmPMCurrent15MinDelayTimeElapsed": fadY1731CfmPMCurrent15MinDelayTimeElapsed,
       "fadY1731CfmPMCurrent15MinDelayTimeMeasured": fadY1731CfmPMCurrent15MinDelayTimeMeasured,
       "fadY1731CfmPM15MinDelayValidIntervals": fadY1731CfmPM15MinDelayValidIntervals,
       "fadY1731CfmPMCurrent15MinDelayInvalidDataFlag": fadY1731CfmPMCurrent15MinDelayInvalidDataFlag,
       "fadY1731CfmPMCurrent15MinDelayPDUSent": fadY1731CfmPMCurrent15MinDelayPDUSent,
       "fadY1731CfmPMCurrent15MinDelayPDURecv": fadY1731CfmPMCurrent15MinDelayPDURecv,
       "fadY1731CfmPMCurrent15MinDelayMinLocal": fadY1731CfmPMCurrent15MinDelayMinLocal,
       "fadY1731CfmPMCurrent15MinDelayMaxLocal": fadY1731CfmPMCurrent15MinDelayMaxLocal,
       "fadY1731CfmPMCurrent15MinDelayAvgLocal": fadY1731CfmPMCurrent15MinDelayAvgLocal,
       "fadY1731CfmPMCurrent15MinDelayMinPeer": fadY1731CfmPMCurrent15MinDelayMinPeer,
       "fadY1731CfmPMCurrent15MinDelayMaxPeer": fadY1731CfmPMCurrent15MinDelayMaxPeer,
       "fadY1731CfmPMCurrent15MinDelayAvgPeer": fadY1731CfmPMCurrent15MinDelayAvgPeer,
       "fadY1731CfmPMCurrent15MinDelayMinBidir": fadY1731CfmPMCurrent15MinDelayMinBidir,
       "fadY1731CfmPMCurrent15MinDelayMaxBidir": fadY1731CfmPMCurrent15MinDelayMaxBidir,
       "fadY1731CfmPMCurrent15MinDelayAvgBidir": fadY1731CfmPMCurrent15MinDelayAvgBidir,
       "fadY1731CfmPMCurrent15MinDelayVarMinLocal": fadY1731CfmPMCurrent15MinDelayVarMinLocal,
       "fadY1731CfmPMCurrent15MinDelayVarMaxLocal": fadY1731CfmPMCurrent15MinDelayVarMaxLocal,
       "fadY1731CfmPMCurrent15MinDelayVarAvgLocal": fadY1731CfmPMCurrent15MinDelayVarAvgLocal,
       "fadY1731CfmPMCurrent15MinDelayVarMinPeer": fadY1731CfmPMCurrent15MinDelayVarMinPeer,
       "fadY1731CfmPMCurrent15MinDelayVarMaxPeer": fadY1731CfmPMCurrent15MinDelayVarMaxPeer,
       "fadY1731CfmPMCurrent15MinDelayVarAvgPeer": fadY1731CfmPMCurrent15MinDelayVarAvgPeer,
       "fadY1731CfmPMCurrent15MinDelayVarMinBidir": fadY1731CfmPMCurrent15MinDelayVarMinBidir,
       "fadY1731CfmPMCurrent15MinDelayVarMaxBidir": fadY1731CfmPMCurrent15MinDelayVarMaxBidir,
       "fadY1731CfmPMCurrent15MinDelayVarAvgBidir": fadY1731CfmPMCurrent15MinDelayVarAvgBidir,
       "fadY1731CfmPMCurrent15MinDelayPDUDiscarded": fadY1731CfmPMCurrent15MinDelayPDUDiscarded,
       "fadY1731CfmPMCurrent1DayIntervalDelayTable": fadY1731CfmPMCurrent1DayIntervalDelayTable,
       "fadY1731CfmPMCurrent1DayIntervalDelayEntry": fadY1731CfmPMCurrent1DayIntervalDelayEntry,
       "fadY1731CfmPMCurrent1DayDelayTimeElapsed": fadY1731CfmPMCurrent1DayDelayTimeElapsed,
       "fadY1731CfmPMCurrent1DayDelayTimeMeasured": fadY1731CfmPMCurrent1DayDelayTimeMeasured,
       "fadY1731CfmPM1DayDelayValidIntervals": fadY1731CfmPM1DayDelayValidIntervals,
       "fadY1731CfmPMCurrent1DayDelayInvalidDataFlag": fadY1731CfmPMCurrent1DayDelayInvalidDataFlag,
       "fadY1731CfmPMCurrent1DayDelayPDUSent": fadY1731CfmPMCurrent1DayDelayPDUSent,
       "fadY1731CfmPMCurrent1DayDelayPDURecv": fadY1731CfmPMCurrent1DayDelayPDURecv,
       "fadY1731CfmPMCurrent1DayDelayMinLocal": fadY1731CfmPMCurrent1DayDelayMinLocal,
       "fadY1731CfmPMCurrent1DayDelayMaxLocal": fadY1731CfmPMCurrent1DayDelayMaxLocal,
       "fadY1731CfmPMCurrent1DayDelayAvgLocal": fadY1731CfmPMCurrent1DayDelayAvgLocal,
       "fadY1731CfmPMCurrent1DayDelayMinPeer": fadY1731CfmPMCurrent1DayDelayMinPeer,
       "fadY1731CfmPMCurrent1DayDelayMaxPeer": fadY1731CfmPMCurrent1DayDelayMaxPeer,
       "fadY1731CfmPMCurrent1DayDelayAvgPeer": fadY1731CfmPMCurrent1DayDelayAvgPeer,
       "fadY1731CfmPMCurrent1DayDelayMinBidir": fadY1731CfmPMCurrent1DayDelayMinBidir,
       "fadY1731CfmPMCurrent1DayDelayMaxBidir": fadY1731CfmPMCurrent1DayDelayMaxBidir,
       "fadY1731CfmPMCurrent1DayDelayAvgBidir": fadY1731CfmPMCurrent1DayDelayAvgBidir,
       "fadY1731CfmPMCurrent1DayDelayVarMinLocal": fadY1731CfmPMCurrent1DayDelayVarMinLocal,
       "fadY1731CfmPMCurrent1DayDelayVarMaxLocal": fadY1731CfmPMCurrent1DayDelayVarMaxLocal,
       "fadY1731CfmPMCurrent1DayDelayVarAvgLocal": fadY1731CfmPMCurrent1DayDelayVarAvgLocal,
       "fadY1731CfmPMCurrent1DayDelayVarMinPeer": fadY1731CfmPMCurrent1DayDelayVarMinPeer,
       "fadY1731CfmPMCurrent1DayDelayVarMaxPeer": fadY1731CfmPMCurrent1DayDelayVarMaxPeer,
       "fadY1731CfmPMCurrent1DayDelayVarAvgPeer": fadY1731CfmPMCurrent1DayDelayVarAvgPeer,
       "fadY1731CfmPMCurrent1DayDelayVarMinBidir": fadY1731CfmPMCurrent1DayDelayVarMinBidir,
       "fadY1731CfmPMCurrent1DayDelayVarMaxBidir": fadY1731CfmPMCurrent1DayDelayVarMaxBidir,
       "fadY1731CfmPMCurrent1DayDelayVarAvgBidir": fadY1731CfmPMCurrent1DayDelayVarAvgBidir,
       "fadY1731CfmPMCurrent1DayDelayPDUDiscarded": fadY1731CfmPMCurrent1DayDelayPDUDiscarded,
       "fadY1731CfmPMPrevious15MinIntervalDelayTable": fadY1731CfmPMPrevious15MinIntervalDelayTable,
       "fadY1731CfmPMPrevious15MinIntervalDelayEntry": fadY1731CfmPMPrevious15MinIntervalDelayEntry,
       "fadY1731CfmPMPrevious15MinDelayIntervalNumber": fadY1731CfmPMPrevious15MinDelayIntervalNumber,
       "fadY1731CfmPMPrevious15MinDelayTimeMeasured": fadY1731CfmPMPrevious15MinDelayTimeMeasured,
       "fadY1731CfmPMPrevious15MinDelayInvalidDataFlag": fadY1731CfmPMPrevious15MinDelayInvalidDataFlag,
       "fadY1731CfmPMPrevious15MinDelayPDUSent": fadY1731CfmPMPrevious15MinDelayPDUSent,
       "fadY1731CfmPMPrevious15MinDelayPDURecv": fadY1731CfmPMPrevious15MinDelayPDURecv,
       "fadY1731CfmPMPrevious15MinDelayMinLocal": fadY1731CfmPMPrevious15MinDelayMinLocal,
       "fadY1731CfmPMPrevious15MinDelayMaxLocal": fadY1731CfmPMPrevious15MinDelayMaxLocal,
       "fadY1731CfmPMPrevious15MinDelayAvgLocal": fadY1731CfmPMPrevious15MinDelayAvgLocal,
       "fadY1731CfmPMPrevious15MinDelayMinPeer": fadY1731CfmPMPrevious15MinDelayMinPeer,
       "fadY1731CfmPMPrevious15MinDelayMaxPeer": fadY1731CfmPMPrevious15MinDelayMaxPeer,
       "fadY1731CfmPMPrevious15MinDelayAvgPeer": fadY1731CfmPMPrevious15MinDelayAvgPeer,
       "fadY1731CfmPMPrevious15MinDelayMinBidir": fadY1731CfmPMPrevious15MinDelayMinBidir,
       "fadY1731CfmPMPrevious15MinDelayMaxBidir": fadY1731CfmPMPrevious15MinDelayMaxBidir,
       "fadY1731CfmPMPrevious15MinDelayAvgBidir": fadY1731CfmPMPrevious15MinDelayAvgBidir,
       "fadY1731CfmPMPrevious15MinDelayVarMinLocal": fadY1731CfmPMPrevious15MinDelayVarMinLocal,
       "fadY1731CfmPMPrevious15MinDelayVarMaxLocal": fadY1731CfmPMPrevious15MinDelayVarMaxLocal,
       "fadY1731CfmPMPrevious15MinDelayVarAvgLocal": fadY1731CfmPMPrevious15MinDelayVarAvgLocal,
       "fadY1731CfmPMPrevious15MinDelayVarMinPeer": fadY1731CfmPMPrevious15MinDelayVarMinPeer,
       "fadY1731CfmPMPrevious15MinDelayVarMaxPeer": fadY1731CfmPMPrevious15MinDelayVarMaxPeer,
       "fadY1731CfmPMPrevious15MinDelayVarAvgPeer": fadY1731CfmPMPrevious15MinDelayVarAvgPeer,
       "fadY1731CfmPMPrevious15MinDelayVarMinBidir": fadY1731CfmPMPrevious15MinDelayVarMinBidir,
       "fadY1731CfmPMPrevious15MinDelayVarMaxBidir": fadY1731CfmPMPrevious15MinDelayVarMaxBidir,
       "fadY1731CfmPMPrevious15MinDelayVarAvgBidir": fadY1731CfmPMPrevious15MinDelayVarAvgBidir,
       "fadY1731CfmPMPrevious15MinDelayPDUDiscarded": fadY1731CfmPMPrevious15MinDelayPDUDiscarded,
       "fadY1731CfmPMPrevious1DayIntervalDelayTable": fadY1731CfmPMPrevious1DayIntervalDelayTable,
       "fadY1731CfmPMPrevious1DayIntervalDelayEntry": fadY1731CfmPMPrevious1DayIntervalDelayEntry,
       "fadY1731CfmPMPrevious1DayDelayIntervalNumber": fadY1731CfmPMPrevious1DayDelayIntervalNumber,
       "fadY1731CfmPMPrevious1DayDelayTimeMeasured": fadY1731CfmPMPrevious1DayDelayTimeMeasured,
       "fadY1731CfmPMPrevious1DayDelayInvalidDataFlag": fadY1731CfmPMPrevious1DayDelayInvalidDataFlag,
       "fadY1731CfmPMPrevious1DayDelayPDUSent": fadY1731CfmPMPrevious1DayDelayPDUSent,
       "fadY1731CfmPMPrevious1DayDelayPDURecv": fadY1731CfmPMPrevious1DayDelayPDURecv,
       "fadY1731CfmPMPrevious1DayDelayMinLocal": fadY1731CfmPMPrevious1DayDelayMinLocal,
       "fadY1731CfmPMPrevious1DayDelayMaxLocal": fadY1731CfmPMPrevious1DayDelayMaxLocal,
       "fadY1731CfmPMPrevious1DayDelayAvgLocal": fadY1731CfmPMPrevious1DayDelayAvgLocal,
       "fadY1731CfmPMPrevious1DayDelayMinPeer": fadY1731CfmPMPrevious1DayDelayMinPeer,
       "fadY1731CfmPMPrevious1DayDelayMaxPeer": fadY1731CfmPMPrevious1DayDelayMaxPeer,
       "fadY1731CfmPMPrevious1DayDelayAvgPeer": fadY1731CfmPMPrevious1DayDelayAvgPeer,
       "fadY1731CfmPMPrevious1DayDelayMinBidir": fadY1731CfmPMPrevious1DayDelayMinBidir,
       "fadY1731CfmPMPrevious1DayDelayMaxBidir": fadY1731CfmPMPrevious1DayDelayMaxBidir,
       "fadY1731CfmPMPrevious1DayDelayAvgBidir": fadY1731CfmPMPrevious1DayDelayAvgBidir,
       "fadY1731CfmPMPrevious1DayDelayVarMinLocal": fadY1731CfmPMPrevious1DayDelayVarMinLocal,
       "fadY1731CfmPMPrevious1DayDelayVarMaxLocal": fadY1731CfmPMPrevious1DayDelayVarMaxLocal,
       "fadY1731CfmPMPrevious1DayDelayVarAvgLocal": fadY1731CfmPMPrevious1DayDelayVarAvgLocal,
       "fadY1731CfmPMPrevious1DayDelayVarMinPeer": fadY1731CfmPMPrevious1DayDelayVarMinPeer,
       "fadY1731CfmPMPrevious1DayDelayVarMaxPeer": fadY1731CfmPMPrevious1DayDelayVarMaxPeer,
       "fadY1731CfmPMPrevious1DayDelayVarAvgPeer": fadY1731CfmPMPrevious1DayDelayVarAvgPeer,
       "fadY1731CfmPMPrevious1DayDelayVarMinBidir": fadY1731CfmPMPrevious1DayDelayVarMinBidir,
       "fadY1731CfmPMPrevious1DayDelayVarMaxBidir": fadY1731CfmPMPrevious1DayDelayVarMaxBidir,
       "fadY1731CfmPMPrevious1DayDelayVarAvgBidir": fadY1731CfmPMPrevious1DayDelayVarAvgBidir,
       "fadY1731CfmPMPrevious1DayDelayPDUDiscarded": fadY1731CfmPMPrevious1DayDelayPDUDiscarded,
       "fadDot1agCfmMepLossRsltTable": fadDot1agCfmMepLossRsltTable,
       "fadDot1agCfmMepLossRsltEntry": fadDot1agCfmMepLossRsltEntry,
       "fadDot1agCfmMepLmMacAddr": fadDot1agCfmMepLmMacAddr,
       "fadDot1agCfmMepLmPduSent": fadDot1agCfmMepLmPduSent,
       "fadDot1agCfmMepLmPduReceived": fadDot1agCfmMepLmPduReceived,
       "fadDot1agCfmMepLmLatestChangeTime": fadDot1agCfmMepLmLatestChangeTime,
       "fadDot1agCfmMepLmFramesRxLocal": fadDot1agCfmMepLmFramesRxLocal,
       "fadDot1agCfmMepLmFramesRxPeer": fadDot1agCfmMepLmFramesRxPeer,
       "fadDot1agCfmMepLmFramesTxLocal": fadDot1agCfmMepLmFramesTxLocal,
       "fadDot1agCfmMepLmFramesTxPeer": fadDot1agCfmMepLmFramesTxPeer,
       "fadDot1agCfmMepLmFramesLossLocal": fadDot1agCfmMepLmFramesLossLocal,
       "fadDot1agCfmMepLmFramesLossPeer": fadDot1agCfmMepLmFramesLossPeer,
       "fadDot1agCfmMepLmLossRatioLocal": fadDot1agCfmMepLmLossRatioLocal,
       "fadDot1agCfmMepLmLossRatioPeer": fadDot1agCfmMepLmLossRatioPeer,
       "fadDot1agCfmMepLmPrevTxLocal": fadDot1agCfmMepLmPrevTxLocal,
       "fadDot1agCfmMepLmPrevRxLocal": fadDot1agCfmMepLmPrevRxLocal,
       "fadDot1agCfmMepLmPrevTxPeer": fadDot1agCfmMepLmPrevTxPeer,
       "fadDot1agCfmMepLmPrevRxPeer": fadDot1agCfmMepLmPrevRxPeer,
       "fadDot1agCfmMepLmCurrTxLocal": fadDot1agCfmMepLmCurrTxLocal,
       "fadDot1agCfmMepLmCurrRxLocal": fadDot1agCfmMepLmCurrRxLocal,
       "fadDot1agCfmMepLmCurrTxPeer": fadDot1agCfmMepLmCurrTxPeer,
       "fadDot1agCfmMepLmCurrRxPeer": fadDot1agCfmMepLmCurrRxPeer,
       "fadDot1agCfmMepLmEnableDuration": fadDot1agCfmMepLmEnableDuration,
       "fadDot1agCfmMepLmChangeCount": fadDot1agCfmMepLmChangeCount,
       "fadSysDot1qEtypeExt": fadSysDot1qEtypeExt,
       "fadSysDefaultVlanDot1qEtype": fadSysDefaultVlanDot1qEtype,
       "fadvRtrExt": fadvRtrExt,
       "fadvRtrIfExtTable": fadvRtrIfExtTable,
       "fadvRtrIfExtEntry": fadvRtrIfExtEntry,
       "fadvRtrIfIngressQosLsrPolicyId": fadvRtrIfIngressQosLsrPolicyId,
       "fadMplsNameMapper": fadMplsNameMapper,
       "fadMplsTunnelNameMapperTable": fadMplsTunnelNameMapperTable,
       "fadMplsTunnelNameMapperEntry": fadMplsTunnelNameMapperEntry,
       "fadMplsTunnelName": fadMplsTunnelName,
       "fadMplsTunnelIndex": fadMplsTunnelIndex,
       "fadMplsLspNameMapperTable": fadMplsLspNameMapperTable,
       "fadMplsLspNameMapperEntry": fadMplsLspNameMapperEntry,
       "fadvRtrMplsLspName": fadvRtrMplsLspName,
       "fadvRtrMplsLspIndex": fadvRtrMplsLspIndex}
)
