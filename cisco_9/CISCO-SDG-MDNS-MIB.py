# SNMP MIB module (CISCO-SDG-MDNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDG-MDNS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:57 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,
 InterfaceIndexOrZero,
 TimeIntervalMin) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort",
    "InterfaceIndexOrZero",
    "TimeIntervalMin")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoSdgMdnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 851)
)
if mibBuilder.loadTexts:
    ciscoSdgMdnsMIB.setRevisions(
        ("2017-05-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CSdgMdnsMIBObjects_ObjectIdentity = ObjectIdentity
cSdgMdnsMIBObjects = _CSdgMdnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1)
)
_CsmStatistics_ObjectIdentity = ObjectIdentity
csmStatistics = _CsmStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1)
)
_CsmGlobalStatistics_ObjectIdentity = ObjectIdentity
csmGlobalStatistics = _CsmGlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1)
)
_CsmAvgInRateMin_Type = TimeIntervalMin
_CsmAvgInRateMin_Object = MibScalar
csmAvgInRateMin = _CsmAvgInRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1, 1),
    _CsmAvgInRateMin_Type()
)
csmAvgInRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmAvgInRateMin.setStatus("current")
_CsmAvgInRateFMin_Type = TimeIntervalMin
_CsmAvgInRateFMin_Object = MibScalar
csmAvgInRateFMin = _CsmAvgInRateFMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1, 2),
    _CsmAvgInRateFMin_Type()
)
csmAvgInRateFMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmAvgInRateFMin.setStatus("current")
_CsmAvgInRateHr_Type = TimeIntervalMin
_CsmAvgInRateHr_Object = MibScalar
csmAvgInRateHr = _CsmAvgInRateHr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1, 3),
    _CsmAvgInRateHr_Type()
)
csmAvgInRateHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmAvgInRateHr.setStatus("current")
_CsmAvgOutRateMin_Type = TimeIntervalMin
_CsmAvgOutRateMin_Object = MibScalar
csmAvgOutRateMin = _CsmAvgOutRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1, 4),
    _CsmAvgOutRateMin_Type()
)
csmAvgOutRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmAvgOutRateMin.setStatus("current")
_CsmAvgOutRateFMin_Type = TimeIntervalMin
_CsmAvgOutRateFMin_Object = MibScalar
csmAvgOutRateFMin = _CsmAvgOutRateFMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1, 5),
    _CsmAvgOutRateFMin_Type()
)
csmAvgOutRateFMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmAvgOutRateFMin.setStatus("current")
_CsmAvgOutRateHr_Type = TimeIntervalMin
_CsmAvgOutRateHr_Object = MibScalar
csmAvgOutRateHr = _CsmAvgOutRateHr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1, 6),
    _CsmAvgOutRateHr_Type()
)
csmAvgOutRateHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmAvgOutRateHr.setStatus("current")
_CsmCacheLimit_Type = Integer32
_CsmCacheLimit_Object = MibScalar
csmCacheLimit = _CsmCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1, 7),
    _CsmCacheLimit_Type()
)
csmCacheLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCacheLimit.setStatus("current")
if mibBuilder.loadTexts:
    csmCacheLimit.setUnits("0")
_CsmCacheMemInUse_Type = Integer32
_CsmCacheMemInUse_Object = MibScalar
csmCacheMemInUse = _CsmCacheMemInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 1, 8),
    _CsmCacheMemInUse_Type()
)
csmCacheMemInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCacheMemInUse.setStatus("current")
if mibBuilder.loadTexts:
    csmCacheMemInUse.setUnits("0")
_CsmSdgStatisticsTable_Object = MibTable
csmSdgStatisticsTable = _CsmSdgStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2)
)
if mibBuilder.loadTexts:
    csmSdgStatisticsTable.setStatus("current")
_CsmSdgStatisticsEntry_Object = MibTableRow
csmSdgStatisticsEntry = _CsmSdgStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1)
)
csmSdgStatisticsEntry.setIndexNames(
    (0, "CISCO-SDG-MDNS-MIB", "csmInterface"),
)
if mibBuilder.loadTexts:
    csmSdgStatisticsEntry.setStatus("current")
_CsmInterface_Type = InterfaceIndexOrZero
_CsmInterface_Object = MibTableColumn
csmInterface = _CsmInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 1),
    _CsmInterface_Type()
)
csmInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csmInterface.setStatus("current")
_CsmMdnsPakSent_Type = Counter32
_CsmMdnsPakSent_Object = MibTableColumn
csmMdnsPakSent = _CsmMdnsPakSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 2),
    _CsmMdnsPakSent_Type()
)
csmMdnsPakSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmMdnsPakSent.setStatus("current")
_CsmIpv4PakSent_Type = Counter32
_CsmIpv4PakSent_Object = MibTableColumn
csmIpv4PakSent = _CsmIpv4PakSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 3),
    _CsmIpv4PakSent_Type()
)
csmIpv4PakSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv4PakSent.setStatus("current")
_CsmIpv6PakSent_Type = Counter32
_CsmIpv6PakSent_Object = MibTableColumn
csmIpv6PakSent = _CsmIpv6PakSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 4),
    _CsmIpv6PakSent_Type()
)
csmIpv6PakSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv6PakSent.setStatus("current")
_CsmIpv4AdvertisementsSentCnt_Type = Counter32
_CsmIpv4AdvertisementsSentCnt_Object = MibTableColumn
csmIpv4AdvertisementsSentCnt = _CsmIpv4AdvertisementsSentCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 5),
    _CsmIpv4AdvertisementsSentCnt_Type()
)
csmIpv4AdvertisementsSentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv4AdvertisementsSentCnt.setStatus("current")
_CsmIpv6AdvertisementsSentCnt_Type = Counter32
_CsmIpv6AdvertisementsSentCnt_Object = MibTableColumn
csmIpv6AdvertisementsSentCnt = _CsmIpv6AdvertisementsSentCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 6),
    _CsmIpv6AdvertisementsSentCnt_Type()
)
csmIpv6AdvertisementsSentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv6AdvertisementsSentCnt.setStatus("current")
_CsmIpv4QuerySentCnt_Type = Counter32
_CsmIpv4QuerySentCnt_Object = MibTableColumn
csmIpv4QuerySentCnt = _CsmIpv4QuerySentCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 7),
    _CsmIpv4QuerySentCnt_Type()
)
csmIpv4QuerySentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv4QuerySentCnt.setStatus("current")
_CsmIpv6QuerySentCnt_Type = Counter32
_CsmIpv6QuerySentCnt_Object = MibTableColumn
csmIpv6QuerySentCnt = _CsmIpv6QuerySentCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 8),
    _CsmIpv6QuerySentCnt_Type()
)
csmIpv6QuerySentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv6QuerySentCnt.setStatus("current")
_CsmUnicastSentCnt_Type = Counter32
_CsmUnicastSentCnt_Object = MibTableColumn
csmUnicastSentCnt = _CsmUnicastSentCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 9),
    _CsmUnicastSentCnt_Type()
)
csmUnicastSentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmUnicastSentCnt.setStatus("current")
_CsmMdnsPakRateLtd_Type = Counter32
_CsmMdnsPakRateLtd_Object = MibTableColumn
csmMdnsPakRateLtd = _CsmMdnsPakRateLtd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 10),
    _CsmMdnsPakRateLtd_Type()
)
csmMdnsPakRateLtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmMdnsPakRateLtd.setStatus("current")
_CsmMdnsPakRcvd_Type = Counter32
_CsmMdnsPakRcvd_Object = MibTableColumn
csmMdnsPakRcvd = _CsmMdnsPakRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 11),
    _CsmMdnsPakRcvd_Type()
)
csmMdnsPakRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmMdnsPakRcvd.setStatus("current")
_CsmAdvertisementsReceived_Type = Counter32
_CsmAdvertisementsReceived_Object = MibTableColumn
csmAdvertisementsReceived = _CsmAdvertisementsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 12),
    _CsmAdvertisementsReceived_Type()
)
csmAdvertisementsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmAdvertisementsReceived.setStatus("current")
_CsmQueriesReceived_Type = Counter32
_CsmQueriesReceived_Object = MibTableColumn
csmQueriesReceived = _CsmQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 13),
    _CsmQueriesReceived_Type()
)
csmQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmQueriesReceived.setStatus("current")
_CsmIpv4AdvertisementsRcvdCnt_Type = Counter32
_CsmIpv4AdvertisementsRcvdCnt_Object = MibTableColumn
csmIpv4AdvertisementsRcvdCnt = _CsmIpv4AdvertisementsRcvdCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 14),
    _CsmIpv4AdvertisementsRcvdCnt_Type()
)
csmIpv4AdvertisementsRcvdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv4AdvertisementsRcvdCnt.setStatus("current")
_CsmIpv6AdvertisementsRcvdCnt_Type = Counter32
_CsmIpv6AdvertisementsRcvdCnt_Object = MibTableColumn
csmIpv6AdvertisementsRcvdCnt = _CsmIpv6AdvertisementsRcvdCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 15),
    _CsmIpv6AdvertisementsRcvdCnt_Type()
)
csmIpv6AdvertisementsRcvdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv6AdvertisementsRcvdCnt.setStatus("current")
_CsmIpv4QueryRcvdCnt_Type = Counter32
_CsmIpv4QueryRcvdCnt_Object = MibTableColumn
csmIpv4QueryRcvdCnt = _CsmIpv4QueryRcvdCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 16),
    _CsmIpv4QueryRcvdCnt_Type()
)
csmIpv4QueryRcvdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv4QueryRcvdCnt.setStatus("current")
_CsmIpv6QueryRcvdCnt_Type = Counter32
_CsmIpv6QueryRcvdCnt_Object = MibTableColumn
csmIpv6QueryRcvdCnt = _CsmIpv6QueryRcvdCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 17),
    _CsmIpv6QueryRcvdCnt_Type()
)
csmIpv6QueryRcvdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmIpv6QueryRcvdCnt.setStatus("current")
_CsmPakDropped_Type = Counter32
_CsmPakDropped_Object = MibTableColumn
csmPakDropped = _CsmPakDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 18),
    _CsmPakDropped_Type()
)
csmPakDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmPakDropped.setStatus("current")
_CsmMdnsGatewayState_Type = Integer32
_CsmMdnsGatewayState_Object = MibTableColumn
csmMdnsGatewayState = _CsmMdnsGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 2, 1, 19),
    _CsmMdnsGatewayState_Type()
)
csmMdnsGatewayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmMdnsGatewayState.setStatus("current")
_CsmControllerStatistics_ObjectIdentity = ObjectIdentity
csmControllerStatistics = _CsmControllerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3)
)
_CsmCntrlIpAddrType_Type = InetAddressType
_CsmCntrlIpAddrType_Object = MibScalar
csmCntrlIpAddrType = _CsmCntrlIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 1),
    _CsmCntrlIpAddrType_Type()
)
csmCntrlIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlIpAddrType.setStatus("current")
_CsmCntrlIpAddr_Type = InetAddress
_CsmCntrlIpAddr_Object = MibScalar
csmCntrlIpAddr = _CsmCntrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 2),
    _CsmCntrlIpAddr_Type()
)
csmCntrlIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlIpAddr.setStatus("current")
_CsmCntrlConnState_Type = Integer32
_CsmCntrlConnState_Object = MibScalar
csmCntrlConnState = _CsmCntrlConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 3),
    _CsmCntrlConnState_Type()
)
csmCntrlConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlConnState.setStatus("current")
_CsmCntrlSrcPort_Type = CiscoPort
_CsmCntrlSrcPort_Object = MibScalar
csmCntrlSrcPort = _CsmCntrlSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 4),
    _CsmCntrlSrcPort_Type()
)
csmCntrlSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlSrcPort.setStatus("current")
_CsmCntrlDestPort_Type = CiscoPort
_CsmCntrlDestPort_Object = MibScalar
csmCntrlDestPort = _CsmCntrlDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 5),
    _CsmCntrlDestPort_Type()
)
csmCntrlDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlDestPort.setStatus("current")
_CsmCntrlSrcInterface_Type = OctetString
_CsmCntrlSrcInterface_Object = MibScalar
csmCntrlSrcInterface = _CsmCntrlSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 6),
    _CsmCntrlSrcInterface_Type()
)
csmCntrlSrcInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlSrcInterface.setStatus("current")
_CsmCntrlMD5Status_Type = TruthValue
_CsmCntrlMD5Status_Object = MibScalar
csmCntrlMD5Status = _CsmCntrlMD5Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 7),
    _CsmCntrlMD5Status_Type()
)
csmCntrlMD5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlMD5Status.setStatus("current")
_CsmCntrlKeepAliveTimer_Type = TimeInterval
_CsmCntrlKeepAliveTimer_Object = MibScalar
csmCntrlKeepAliveTimer = _CsmCntrlKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 8),
    _CsmCntrlKeepAliveTimer_Type()
)
csmCntrlKeepAliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlKeepAliveTimer.setStatus("current")
_CsmCntrlDeadTimer_Type = TimeInterval
_CsmCntrlDeadTimer_Object = MibScalar
csmCntrlDeadTimer = _CsmCntrlDeadTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 9),
    _CsmCntrlDeadTimer_Type()
)
csmCntrlDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlDeadTimer.setStatus("current")
_CsmCntrlTotalBCPMsgSent_Type = Counter32
_CsmCntrlTotalBCPMsgSent_Object = MibScalar
csmCntrlTotalBCPMsgSent = _CsmCntrlTotalBCPMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 10),
    _CsmCntrlTotalBCPMsgSent_Type()
)
csmCntrlTotalBCPMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlTotalBCPMsgSent.setStatus("current")
_CsmCntrlTotalBCPMsgRcvd_Type = Counter32
_CsmCntrlTotalBCPMsgRcvd_Object = MibScalar
csmCntrlTotalBCPMsgRcvd = _CsmCntrlTotalBCPMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 11),
    _CsmCntrlTotalBCPMsgRcvd_Type()
)
csmCntrlTotalBCPMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlTotalBCPMsgRcvd.setStatus("current")
_CsmCntrlBCPWithdrawMsgSent_Type = Counter32
_CsmCntrlBCPWithdrawMsgSent_Object = MibScalar
csmCntrlBCPWithdrawMsgSent = _CsmCntrlBCPWithdrawMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 12),
    _CsmCntrlBCPWithdrawMsgSent_Type()
)
csmCntrlBCPWithdrawMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlBCPWithdrawMsgSent.setStatus("current")
_CsmCntrlIpv4QueryRequests_Type = Counter32
_CsmCntrlIpv4QueryRequests_Object = MibScalar
csmCntrlIpv4QueryRequests = _CsmCntrlIpv4QueryRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 13),
    _CsmCntrlIpv4QueryRequests_Type()
)
csmCntrlIpv4QueryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlIpv4QueryRequests.setStatus("current")
_CsmCntrlIpv4QueryResponses_Type = Counter32
_CsmCntrlIpv4QueryResponses_Object = MibScalar
csmCntrlIpv4QueryResponses = _CsmCntrlIpv4QueryResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 14),
    _CsmCntrlIpv4QueryResponses_Type()
)
csmCntrlIpv4QueryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlIpv4QueryResponses.setStatus("current")
_CsmCntrlIpv6QueryRequests_Type = Counter32
_CsmCntrlIpv6QueryRequests_Object = MibScalar
csmCntrlIpv6QueryRequests = _CsmCntrlIpv6QueryRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 15),
    _CsmCntrlIpv6QueryRequests_Type()
)
csmCntrlIpv6QueryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlIpv6QueryRequests.setStatus("current")
_CsmCntrlIpv6QueryResponses_Type = Counter32
_CsmCntrlIpv6QueryResponses_Object = MibScalar
csmCntrlIpv6QueryResponses = _CsmCntrlIpv6QueryResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 16),
    _CsmCntrlIpv6QueryResponses_Type()
)
csmCntrlIpv6QueryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlIpv6QueryResponses.setStatus("current")
_CsmCntrlIpv4ServiceAdvertised_Type = Counter32
_CsmCntrlIpv4ServiceAdvertised_Object = MibScalar
csmCntrlIpv4ServiceAdvertised = _CsmCntrlIpv4ServiceAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 17),
    _CsmCntrlIpv4ServiceAdvertised_Type()
)
csmCntrlIpv4ServiceAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlIpv4ServiceAdvertised.setStatus("current")
_CsmCntrlIpv6ServiceAdvertised_Type = Counter32
_CsmCntrlIpv6ServiceAdvertised_Object = MibScalar
csmCntrlIpv6ServiceAdvertised = _CsmCntrlIpv6ServiceAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 18),
    _CsmCntrlIpv6ServiceAdvertised_Type()
)
csmCntrlIpv6ServiceAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlIpv6ServiceAdvertised.setStatus("current")
_CsmCntrlPktRcvdCnt_Type = Counter32
_CsmCntrlPktRcvdCnt_Object = MibScalar
csmCntrlPktRcvdCnt = _CsmCntrlPktRcvdCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 19),
    _CsmCntrlPktRcvdCnt_Type()
)
csmCntrlPktRcvdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlPktRcvdCnt.setStatus("current")
_CsmCntrlAnnouncementQueueSize_Type = Integer32
_CsmCntrlAnnouncementQueueSize_Object = MibScalar
csmCntrlAnnouncementQueueSize = _CsmCntrlAnnouncementQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 20),
    _CsmCntrlAnnouncementQueueSize_Type()
)
csmCntrlAnnouncementQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlAnnouncementQueueSize.setStatus("current")
_CsmCntrlAnnouncementTimer_Type = TimeInterval
_CsmCntrlAnnouncementTimer_Object = MibScalar
csmCntrlAnnouncementTimer = _CsmCntrlAnnouncementTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 21),
    _CsmCntrlAnnouncementTimer_Type()
)
csmCntrlAnnouncementTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlAnnouncementTimer.setStatus("current")
_CsmCntrlAnnouncementsExported_Type = Counter32
_CsmCntrlAnnouncementsExported_Object = MibScalar
csmCntrlAnnouncementsExported = _CsmCntrlAnnouncementsExported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 22),
    _CsmCntrlAnnouncementsExported_Type()
)
csmCntrlAnnouncementsExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlAnnouncementsExported.setStatus("current")
_CsmCntrlPendingAnnouncements_Type = Counter32
_CsmCntrlPendingAnnouncements_Object = MibScalar
csmCntrlPendingAnnouncements = _CsmCntrlPendingAnnouncements_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 23),
    _CsmCntrlPendingAnnouncements_Type()
)
csmCntrlPendingAnnouncements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlPendingAnnouncements.setStatus("current")
_CsmCntrlNextAnnouncementTime_Type = TimeInterval
_CsmCntrlNextAnnouncementTime_Object = MibScalar
csmCntrlNextAnnouncementTime = _CsmCntrlNextAnnouncementTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 24),
    _CsmCntrlNextAnnouncementTime_Type()
)
csmCntrlNextAnnouncementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlNextAnnouncementTime.setStatus("current")
_CsmCntrlQuerySuppression_Type = TruthValue
_CsmCntrlQuerySuppression_Object = MibScalar
csmCntrlQuerySuppression = _CsmCntrlQuerySuppression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 25),
    _CsmCntrlQuerySuppression_Type()
)
csmCntrlQuerySuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlQuerySuppression.setStatus("current")
_CsmCntrlPendingQueries_Type = Counter32
_CsmCntrlPendingQueries_Object = MibScalar
csmCntrlPendingQueries = _CsmCntrlPendingQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 26),
    _CsmCntrlPendingQueries_Type()
)
csmCntrlPendingQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlPendingQueries.setStatus("current")
_CsmCntrlQueryQueueSize_Type = Integer32
_CsmCntrlQueryQueueSize_Object = MibScalar
csmCntrlQueryQueueSize = _CsmCntrlQueryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 27),
    _CsmCntrlQueryQueueSize_Type()
)
csmCntrlQueryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlQueryQueueSize.setStatus("current")
_CsmCntrlQueryTimer_Type = TimeInterval
_CsmCntrlQueryTimer_Object = MibScalar
csmCntrlQueryTimer = _CsmCntrlQueryTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 28),
    _CsmCntrlQueryTimer_Type()
)
csmCntrlQueryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlQueryTimer.setStatus("current")
_CsmCntrlNextQueryTime_Type = TimeInterval
_CsmCntrlNextQueryTime_Object = MibScalar
csmCntrlNextQueryTime = _CsmCntrlNextQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 29),
    _CsmCntrlNextQueryTime_Type()
)
csmCntrlNextQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlNextQueryTime.setStatus("current")
_CsmCntrlTotalQueryExported_Type = Counter32
_CsmCntrlTotalQueryExported_Object = MibScalar
csmCntrlTotalQueryExported = _CsmCntrlTotalQueryExported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 30),
    _CsmCntrlTotalQueryExported_Type()
)
csmCntrlTotalQueryExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlTotalQueryExported.setStatus("current")
_CsmCntrlTotalResync_Type = Counter32
_CsmCntrlTotalResync_Object = MibScalar
csmCntrlTotalResync = _CsmCntrlTotalResync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 31),
    _CsmCntrlTotalResync_Type()
)
csmCntrlTotalResync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlTotalResync.setStatus("current")
_CsmCntrlLastResync_Type = DateAndTime
_CsmCntrlLastResync_Object = MibScalar
csmCntrlLastResync = _CsmCntrlLastResync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 3, 32),
    _CsmCntrlLastResync_Type()
)
csmCntrlLastResync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmCntrlLastResync.setStatus("current")
_CsmSdgCacheStatisticsTable_Object = MibTable
csmSdgCacheStatisticsTable = _CsmSdgCacheStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4)
)
if mibBuilder.loadTexts:
    csmSdgCacheStatisticsTable.setStatus("current")
_CsmSdgCacheStatisticsEntry_Object = MibTableRow
csmSdgCacheStatisticsEntry = _CsmSdgCacheStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4, 1)
)
csmSdgCacheStatisticsEntry.setIndexNames(
    (0, "CISCO-SDG-MDNS-MIB", "csmCacheInterface"),
)
if mibBuilder.loadTexts:
    csmSdgCacheStatisticsEntry.setStatus("current")
_CsmCacheInterface_Type = InterfaceIndexOrZero
_CsmCacheInterface_Object = MibTableColumn
csmCacheInterface = _CsmCacheInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4, 1, 1),
    _CsmCacheInterface_Type()
)
csmCacheInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csmCacheInterface.setStatus("current")
_CsmNumOfSrvTypes_Type = Integer32
_CsmNumOfSrvTypes_Object = MibTableColumn
csmNumOfSrvTypes = _CsmNumOfSrvTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4, 1, 2),
    _CsmNumOfSrvTypes_Type()
)
csmNumOfSrvTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmNumOfSrvTypes.setStatus("current")
if mibBuilder.loadTexts:
    csmNumOfSrvTypes.setUnits("0")
_CsmNumOfAAAARecords_Type = Counter32
_CsmNumOfAAAARecords_Object = MibTableColumn
csmNumOfAAAARecords = _CsmNumOfAAAARecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4, 1, 3),
    _CsmNumOfAAAARecords_Type()
)
csmNumOfAAAARecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmNumOfAAAARecords.setStatus("current")
if mibBuilder.loadTexts:
    csmNumOfAAAARecords.setUnits("0")
_CsmNumOfTXTRecords_Type = Counter32
_CsmNumOfTXTRecords_Object = MibTableColumn
csmNumOfTXTRecords = _CsmNumOfTXTRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4, 1, 4),
    _CsmNumOfTXTRecords_Type()
)
csmNumOfTXTRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmNumOfTXTRecords.setStatus("current")
if mibBuilder.loadTexts:
    csmNumOfTXTRecords.setUnits("0")
_CsmNumOfSRVRecords_Type = Counter32
_CsmNumOfSRVRecords_Object = MibTableColumn
csmNumOfSRVRecords = _CsmNumOfSRVRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4, 1, 5),
    _CsmNumOfSRVRecords_Type()
)
csmNumOfSRVRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmNumOfSRVRecords.setStatus("current")
if mibBuilder.loadTexts:
    csmNumOfSRVRecords.setUnits("0")
_CsmNumOfPTRRecords_Type = Counter32
_CsmNumOfPTRRecords_Object = MibTableColumn
csmNumOfPTRRecords = _CsmNumOfPTRRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4, 1, 6),
    _CsmNumOfPTRRecords_Type()
)
csmNumOfPTRRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmNumOfPTRRecords.setStatus("current")
if mibBuilder.loadTexts:
    csmNumOfPTRRecords.setUnits("0")
_CsmNumOfARecords_Type = Counter32
_CsmNumOfARecords_Object = MibTableColumn
csmNumOfARecords = _CsmNumOfARecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 1, 1, 4, 1, 7),
    _CsmNumOfARecords_Type()
)
csmNumOfARecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmNumOfARecords.setStatus("current")
if mibBuilder.loadTexts:
    csmNumOfARecords.setUnits("0")
_CSdgMdnsMIBConformance_ObjectIdentity = ObjectIdentity
cSdgMdnsMIBConformance = _CSdgMdnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 2)
)
_CsmMIBCompliances_ObjectIdentity = ObjectIdentity
csmMIBCompliances = _CsmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 2, 1)
)
_CsmMIBGroups_ObjectIdentity = ObjectIdentity
csmMIBGroups = _CsmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 2, 2)
)

# Managed Objects groups

csmGlobalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 2, 2, 1)
)
csmGlobalStatisticsGroup.setObjects(
      *(("CISCO-SDG-MDNS-MIB", "csmAvgInRateMin"),
        ("CISCO-SDG-MDNS-MIB", "csmAvgInRateFMin"),
        ("CISCO-SDG-MDNS-MIB", "csmAvgInRateHr"),
        ("CISCO-SDG-MDNS-MIB", "csmAvgOutRateMin"),
        ("CISCO-SDG-MDNS-MIB", "csmAvgOutRateFMin"),
        ("CISCO-SDG-MDNS-MIB", "csmAvgOutRateHr"),
        ("CISCO-SDG-MDNS-MIB", "csmCacheLimit"),
        ("CISCO-SDG-MDNS-MIB", "csmCacheMemInUse"))
)
if mibBuilder.loadTexts:
    csmGlobalStatisticsGroup.setStatus("current")

csmSdgStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 2, 2, 2)
)
csmSdgStatisticsGroup.setObjects(
      *(("CISCO-SDG-MDNS-MIB", "csmMdnsPakSent"),
        ("CISCO-SDG-MDNS-MIB", "csmUnicastSentCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmMdnsPakRateLtd"),
        ("CISCO-SDG-MDNS-MIB", "csmMdnsPakRcvd"),
        ("CISCO-SDG-MDNS-MIB", "csmPakDropped"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv4AdvertisementsSentCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv4QuerySentCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv6AdvertisementsSentCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv6QuerySentCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv4AdvertisementsRcvdCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv4QueryRcvdCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv6AdvertisementsRcvdCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv6QueryRcvdCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmMdnsGatewayState"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv4PakSent"),
        ("CISCO-SDG-MDNS-MIB", "csmIpv6PakSent"),
        ("CISCO-SDG-MDNS-MIB", "csmAdvertisementsReceived"),
        ("CISCO-SDG-MDNS-MIB", "csmQueriesReceived"))
)
if mibBuilder.loadTexts:
    csmSdgStatisticsGroup.setStatus("current")

csmControllerStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 2, 2, 3)
)
csmControllerStatisticsGroup.setObjects(
      *(("CISCO-SDG-MDNS-MIB", "csmCntrlConnState"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlMD5Status"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlKeepAliveTimer"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlDeadTimer"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlTotalBCPMsgSent"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlTotalBCPMsgRcvd"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlTotalResync"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlLastResync"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlIpv4QueryResponses"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlIpv4QueryRequests"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlIpv6QueryRequests"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlIpv6QueryResponses"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlIpv4ServiceAdvertised"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlIpv6ServiceAdvertised"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlBCPWithdrawMsgSent"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlPktRcvdCnt"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlIpAddr"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlSrcPort"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlDestPort"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlAnnouncementQueueSize"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlAnnouncementTimer"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlPendingAnnouncements"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlAnnouncementsExported"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlNextAnnouncementTime"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlQuerySuppression"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlQueryQueueSize"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlQueryTimer"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlPendingQueries"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlTotalQueryExported"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlNextQueryTime"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlIpAddrType"),
        ("CISCO-SDG-MDNS-MIB", "csmCntrlSrcInterface"))
)
if mibBuilder.loadTexts:
    csmControllerStatisticsGroup.setStatus("current")

csmSdgCacheStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 2, 2, 4)
)
csmSdgCacheStatisticsGroup.setObjects(
      *(("CISCO-SDG-MDNS-MIB", "csmNumOfSrvTypes"),
        ("CISCO-SDG-MDNS-MIB", "csmNumOfTXTRecords"),
        ("CISCO-SDG-MDNS-MIB", "csmNumOfSRVRecords"),
        ("CISCO-SDG-MDNS-MIB", "csmNumOfARecords"),
        ("CISCO-SDG-MDNS-MIB", "csmNumOfAAAARecords"),
        ("CISCO-SDG-MDNS-MIB", "csmNumOfPTRRecords"))
)
if mibBuilder.loadTexts:
    csmSdgCacheStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 851, 2, 1, 1)
)
csmMIBCompliance.setObjects(
      *(("CISCO-SDG-MDNS-MIB", "csmGlobalStatisticsGroup"),
        ("CISCO-SDG-MDNS-MIB", "csmSdgStatisticsGroup"),
        ("CISCO-SDG-MDNS-MIB", "csmControllerStatisticsGroup"),
        ("CISCO-SDG-MDNS-MIB", "csmSdgCacheStatisticsGroup"))
)
if mibBuilder.loadTexts:
    csmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDG-MDNS-MIB",
    **{"ciscoSdgMdnsMIB": ciscoSdgMdnsMIB,
       "cSdgMdnsMIBObjects": cSdgMdnsMIBObjects,
       "csmStatistics": csmStatistics,
       "csmGlobalStatistics": csmGlobalStatistics,
       "csmAvgInRateMin": csmAvgInRateMin,
       "csmAvgInRateFMin": csmAvgInRateFMin,
       "csmAvgInRateHr": csmAvgInRateHr,
       "csmAvgOutRateMin": csmAvgOutRateMin,
       "csmAvgOutRateFMin": csmAvgOutRateFMin,
       "csmAvgOutRateHr": csmAvgOutRateHr,
       "csmCacheLimit": csmCacheLimit,
       "csmCacheMemInUse": csmCacheMemInUse,
       "csmSdgStatisticsTable": csmSdgStatisticsTable,
       "csmSdgStatisticsEntry": csmSdgStatisticsEntry,
       "csmInterface": csmInterface,
       "csmMdnsPakSent": csmMdnsPakSent,
       "csmIpv4PakSent": csmIpv4PakSent,
       "csmIpv6PakSent": csmIpv6PakSent,
       "csmIpv4AdvertisementsSentCnt": csmIpv4AdvertisementsSentCnt,
       "csmIpv6AdvertisementsSentCnt": csmIpv6AdvertisementsSentCnt,
       "csmIpv4QuerySentCnt": csmIpv4QuerySentCnt,
       "csmIpv6QuerySentCnt": csmIpv6QuerySentCnt,
       "csmUnicastSentCnt": csmUnicastSentCnt,
       "csmMdnsPakRateLtd": csmMdnsPakRateLtd,
       "csmMdnsPakRcvd": csmMdnsPakRcvd,
       "csmAdvertisementsReceived": csmAdvertisementsReceived,
       "csmQueriesReceived": csmQueriesReceived,
       "csmIpv4AdvertisementsRcvdCnt": csmIpv4AdvertisementsRcvdCnt,
       "csmIpv6AdvertisementsRcvdCnt": csmIpv6AdvertisementsRcvdCnt,
       "csmIpv4QueryRcvdCnt": csmIpv4QueryRcvdCnt,
       "csmIpv6QueryRcvdCnt": csmIpv6QueryRcvdCnt,
       "csmPakDropped": csmPakDropped,
       "csmMdnsGatewayState": csmMdnsGatewayState,
       "csmControllerStatistics": csmControllerStatistics,
       "csmCntrlIpAddrType": csmCntrlIpAddrType,
       "csmCntrlIpAddr": csmCntrlIpAddr,
       "csmCntrlConnState": csmCntrlConnState,
       "csmCntrlSrcPort": csmCntrlSrcPort,
       "csmCntrlDestPort": csmCntrlDestPort,
       "csmCntrlSrcInterface": csmCntrlSrcInterface,
       "csmCntrlMD5Status": csmCntrlMD5Status,
       "csmCntrlKeepAliveTimer": csmCntrlKeepAliveTimer,
       "csmCntrlDeadTimer": csmCntrlDeadTimer,
       "csmCntrlTotalBCPMsgSent": csmCntrlTotalBCPMsgSent,
       "csmCntrlTotalBCPMsgRcvd": csmCntrlTotalBCPMsgRcvd,
       "csmCntrlBCPWithdrawMsgSent": csmCntrlBCPWithdrawMsgSent,
       "csmCntrlIpv4QueryRequests": csmCntrlIpv4QueryRequests,
       "csmCntrlIpv4QueryResponses": csmCntrlIpv4QueryResponses,
       "csmCntrlIpv6QueryRequests": csmCntrlIpv6QueryRequests,
       "csmCntrlIpv6QueryResponses": csmCntrlIpv6QueryResponses,
       "csmCntrlIpv4ServiceAdvertised": csmCntrlIpv4ServiceAdvertised,
       "csmCntrlIpv6ServiceAdvertised": csmCntrlIpv6ServiceAdvertised,
       "csmCntrlPktRcvdCnt": csmCntrlPktRcvdCnt,
       "csmCntrlAnnouncementQueueSize": csmCntrlAnnouncementQueueSize,
       "csmCntrlAnnouncementTimer": csmCntrlAnnouncementTimer,
       "csmCntrlAnnouncementsExported": csmCntrlAnnouncementsExported,
       "csmCntrlPendingAnnouncements": csmCntrlPendingAnnouncements,
       "csmCntrlNextAnnouncementTime": csmCntrlNextAnnouncementTime,
       "csmCntrlQuerySuppression": csmCntrlQuerySuppression,
       "csmCntrlPendingQueries": csmCntrlPendingQueries,
       "csmCntrlQueryQueueSize": csmCntrlQueryQueueSize,
       "csmCntrlQueryTimer": csmCntrlQueryTimer,
       "csmCntrlNextQueryTime": csmCntrlNextQueryTime,
       "csmCntrlTotalQueryExported": csmCntrlTotalQueryExported,
       "csmCntrlTotalResync": csmCntrlTotalResync,
       "csmCntrlLastResync": csmCntrlLastResync,
       "csmSdgCacheStatisticsTable": csmSdgCacheStatisticsTable,
       "csmSdgCacheStatisticsEntry": csmSdgCacheStatisticsEntry,
       "csmCacheInterface": csmCacheInterface,
       "csmNumOfSrvTypes": csmNumOfSrvTypes,
       "csmNumOfAAAARecords": csmNumOfAAAARecords,
       "csmNumOfTXTRecords": csmNumOfTXTRecords,
       "csmNumOfSRVRecords": csmNumOfSRVRecords,
       "csmNumOfPTRRecords": csmNumOfPTRRecords,
       "csmNumOfARecords": csmNumOfARecords,
       "cSdgMdnsMIBConformance": cSdgMdnsMIBConformance,
       "csmMIBCompliances": csmMIBCompliances,
       "csmMIBCompliance": csmMIBCompliance,
       "csmMIBGroups": csmMIBGroups,
       "csmGlobalStatisticsGroup": csmGlobalStatisticsGroup,
       "csmSdgStatisticsGroup": csmSdgStatisticsGroup,
       "csmControllerStatisticsGroup": csmControllerStatisticsGroup,
       "csmSdgCacheStatisticsGroup": csmSdgCacheStatisticsGroup}
)
