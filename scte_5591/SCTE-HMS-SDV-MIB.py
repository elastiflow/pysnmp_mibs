# SNMP MIB module (SCTE-HMS-SDV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-SDV-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:36:31 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hmsScteSdvMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1)
)
if mibBuilder.loadTexts:
    hmsScteSdvMib.setRevisions(
        ("2008-09-24 15:30",
         "2008-05-22 10:30",
         "2007-04-18 17:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SdvServerMIBObjects_ObjectIdentity = ObjectIdentity
sdvServerMIBObjects = _SdvServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1)
)
_SdvsmName_Type = OctetString
_SdvsmName_Object = MibScalar
sdvsmName = _SdvsmName_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 1),
    _SdvsmName_Type()
)
sdvsmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdvsmName.setStatus("current")
_SdvsmMacAddress_Type = MacAddress
_SdvsmMacAddress_Object = MibScalar
sdvsmMacAddress = _SdvsmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 2),
    _SdvsmMacAddress_Type()
)
sdvsmMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdvsmMacAddress.setStatus("current")
_SdvsmConfigObjects_ObjectIdentity = ObjectIdentity
sdvsmConfigObjects = _SdvsmConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sdvsmConfigObjects.setStatus("current")
_SdvsmMiniCarouselTable_Object = MibTable
sdvsmMiniCarouselTable = _SdvsmMiniCarouselTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sdvsmMiniCarouselTable.setStatus("current")
_SdvsmMiniCarouselEntry_Object = MibTableRow
sdvsmMiniCarouselEntry = _SdvsmMiniCarouselEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1, 1)
)
sdvsmMiniCarouselEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmServiceGroupID"),
)
if mibBuilder.loadTexts:
    sdvsmMiniCarouselEntry.setStatus("current")


class _SdvsmMiniCarouselPath_Type(Integer32):
    """Custom type sdvsmMiniCarouselPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oob", 1),
          ("ib", 2))
    )


_SdvsmMiniCarouselPath_Type.__name__ = "Integer32"
_SdvsmMiniCarouselPath_Object = MibTableColumn
sdvsmMiniCarouselPath = _SdvsmMiniCarouselPath_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1, 1, 1),
    _SdvsmMiniCarouselPath_Type()
)
sdvsmMiniCarouselPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselPath.setStatus("current")
_SdvsmMiniCarouselBitRate_Type = Integer32
_SdvsmMiniCarouselBitRate_Object = MibTableColumn
sdvsmMiniCarouselBitRate = _SdvsmMiniCarouselBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1, 1, 2),
    _SdvsmMiniCarouselBitRate_Type()
)
sdvsmMiniCarouselBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselBitRate.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselBitRate.setUnits("bps")
_SdvsmMiniCarouselDestIpAddrType_Type = InetAddressType
_SdvsmMiniCarouselDestIpAddrType_Object = MibTableColumn
sdvsmMiniCarouselDestIpAddrType = _SdvsmMiniCarouselDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1, 1, 3),
    _SdvsmMiniCarouselDestIpAddrType_Type()
)
sdvsmMiniCarouselDestIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselDestIpAddrType.setStatus("current")
_SdvsmMiniCarouselDestIpAddr_Type = InetAddress
_SdvsmMiniCarouselDestIpAddr_Object = MibTableColumn
sdvsmMiniCarouselDestIpAddr = _SdvsmMiniCarouselDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1, 1, 4),
    _SdvsmMiniCarouselDestIpAddr_Type()
)
sdvsmMiniCarouselDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselDestIpAddr.setStatus("current")


class _SdvsmMiniCarouselUdpPort_Type(Integer32):
    """Custom type sdvsmMiniCarouselUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmMiniCarouselUdpPort_Type.__name__ = "Integer32"
_SdvsmMiniCarouselUdpPort_Object = MibTableColumn
sdvsmMiniCarouselUdpPort = _SdvsmMiniCarouselUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1, 1, 5),
    _SdvsmMiniCarouselUdpPort_Type()
)
sdvsmMiniCarouselUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselUdpPort.setStatus("current")
_SdvsmMiniCarouselSize_Type = Integer32
_SdvsmMiniCarouselSize_Object = MibTableColumn
sdvsmMiniCarouselSize = _SdvsmMiniCarouselSize_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1, 1, 6),
    _SdvsmMiniCarouselSize_Type()
)
sdvsmMiniCarouselSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselSize.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselSize.setUnits("bytes")


class _SdvsmMiniCarouselTransmissionFrequency_Type(Integer32):
    """Custom type sdvsmMiniCarouselTransmissionFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SdvsmMiniCarouselTransmissionFrequency_Type.__name__ = "Integer32"
_SdvsmMiniCarouselTransmissionFrequency_Object = MibTableColumn
sdvsmMiniCarouselTransmissionFrequency = _SdvsmMiniCarouselTransmissionFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 1, 1, 7),
    _SdvsmMiniCarouselTransmissionFrequency_Type()
)
sdvsmMiniCarouselTransmissionFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselTransmissionFrequency.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmMiniCarouselTransmissionFrequency.setUnits("# mini-carousel/second")
_SdvsmClientTable_Object = MibTable
sdvsmClientTable = _SdvsmClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sdvsmClientTable.setStatus("current")
_SdvsmClientEntry_Object = MibTableRow
sdvsmClientEntry = _SdvsmClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1)
)
sdvsmClientEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmServiceGroupID"),
)
if mibBuilder.loadTexts:
    sdvsmClientEntry.setStatus("current")
_SdvsmClientRexmitPgmSelectInterval_Type = Integer32
_SdvsmClientRexmitPgmSelectInterval_Object = MibTableColumn
sdvsmClientRexmitPgmSelectInterval = _SdvsmClientRexmitPgmSelectInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 1),
    _SdvsmClientRexmitPgmSelectInterval_Type()
)
sdvsmClientRexmitPgmSelectInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientRexmitPgmSelectInterval.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmClientRexmitPgmSelectInterval.setUnits("seconds")
_SdvsmClientLastUserActivityInterval_Type = Integer32
_SdvsmClientLastUserActivityInterval_Object = MibTableColumn
sdvsmClientLastUserActivityInterval = _SdvsmClientLastUserActivityInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 2),
    _SdvsmClientLastUserActivityInterval_Type()
)
sdvsmClientLastUserActivityInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientLastUserActivityInterval.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmClientLastUserActivityInterval.setUnits("seconds")
_SdvsmClientMsgRespTimeout_Type = Integer32
_SdvsmClientMsgRespTimeout_Object = MibTableColumn
sdvsmClientMsgRespTimeout = _SdvsmClientMsgRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 3),
    _SdvsmClientMsgRespTimeout_Type()
)
sdvsmClientMsgRespTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientMsgRespTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmClientMsgRespTimeout.setUnits("milliseconds")
_SdvsmClientMsgReqMaxRetries_Type = Integer32
_SdvsmClientMsgReqMaxRetries_Object = MibTableColumn
sdvsmClientMsgReqMaxRetries = _SdvsmClientMsgReqMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 4),
    _SdvsmClientMsgReqMaxRetries_Type()
)
sdvsmClientMsgReqMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientMsgReqMaxRetries.setStatus("current")
_SdvsmClientMsgReqMinRetryInterval_Type = Integer32
_SdvsmClientMsgReqMinRetryInterval_Object = MibTableColumn
sdvsmClientMsgReqMinRetryInterval = _SdvsmClientMsgReqMinRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 5),
    _SdvsmClientMsgReqMinRetryInterval_Type()
)
sdvsmClientMsgReqMinRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientMsgReqMinRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmClientMsgReqMinRetryInterval.setUnits("milliseconds")
_SdvsmClientMsgReqMaxRetryInterval_Type = Integer32
_SdvsmClientMsgReqMaxRetryInterval_Object = MibTableColumn
sdvsmClientMsgReqMaxRetryInterval = _SdvsmClientMsgReqMaxRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 6),
    _SdvsmClientMsgReqMaxRetryInterval_Type()
)
sdvsmClientMsgReqMaxRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientMsgReqMaxRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmClientMsgReqMaxRetryInterval.setUnits("milliseconds")
_SdvsmClientUserInteractionTimeout_Type = Integer32
_SdvsmClientUserInteractionTimeout_Object = MibTableColumn
sdvsmClientUserInteractionTimeout = _SdvsmClientUserInteractionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 7),
    _SdvsmClientUserInteractionTimeout_Type()
)
sdvsmClientUserInteractionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientUserInteractionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmClientUserInteractionTimeout.setUnits("seconds")
_SdvsmClientDefaultCaSystemId_Type = Integer32
_SdvsmClientDefaultCaSystemId_Object = MibTableColumn
sdvsmClientDefaultCaSystemId = _SdvsmClientDefaultCaSystemId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 8),
    _SdvsmClientDefaultCaSystemId_Type()
)
sdvsmClientDefaultCaSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientDefaultCaSystemId.setStatus("current")
_SdvsmClientDefaultEncoding_Type = Integer32
_SdvsmClientDefaultEncoding_Object = MibTableColumn
sdvsmClientDefaultEncoding = _SdvsmClientDefaultEncoding_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 9),
    _SdvsmClientDefaultEncoding_Type()
)
sdvsmClientDefaultEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientDefaultEncoding.setStatus("current")
_SdvsmClientDefaultCapabilities_Type = Integer32
_SdvsmClientDefaultCapabilities_Object = MibTableColumn
sdvsmClientDefaultCapabilities = _SdvsmClientDefaultCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 10),
    _SdvsmClientDefaultCapabilities_Type()
)
sdvsmClientDefaultCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientDefaultCapabilities.setStatus("current")
_SdvsmClientTunerHealthTest_Type = Integer32
_SdvsmClientTunerHealthTest_Object = MibTableColumn
sdvsmClientTunerHealthTest = _SdvsmClientTunerHealthTest_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 11),
    _SdvsmClientTunerHealthTest_Type()
)
sdvsmClientTunerHealthTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientTunerHealthTest.setStatus("current")
_SdvsmClientMinimizeChannelReport_Type = Integer32
_SdvsmClientMinimizeChannelReport_Object = MibTableColumn
sdvsmClientMinimizeChannelReport = _SdvsmClientMinimizeChannelReport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 2, 1, 12),
    _SdvsmClientMinimizeChannelReport_Type()
)
sdvsmClientMinimizeChannelReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmClientMinimizeChannelReport.setStatus("current")
_SdvsmFrequencyPlanTable_Object = MibTable
sdvsmFrequencyPlanTable = _SdvsmFrequencyPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanTable.setStatus("current")
_SdvsmFrequencyPlanEntry_Object = MibTableRow
sdvsmFrequencyPlanEntry = _SdvsmFrequencyPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1)
)
sdvsmFrequencyPlanEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmServiceGroupID"),
)
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanEntry.setStatus("current")
_SdvsmFrequencyPlanIndex_Type = Unsigned32
_SdvsmFrequencyPlanIndex_Object = MibTableColumn
sdvsmFrequencyPlanIndex = _SdvsmFrequencyPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 1),
    _SdvsmFrequencyPlanIndex_Type()
)
sdvsmFrequencyPlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanIndex.setStatus("current")
_SdvsmFrequencyPlanIpAddrType_Type = InetAddressType
_SdvsmFrequencyPlanIpAddrType_Object = MibTableColumn
sdvsmFrequencyPlanIpAddrType = _SdvsmFrequencyPlanIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 2),
    _SdvsmFrequencyPlanIpAddrType_Type()
)
sdvsmFrequencyPlanIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanIpAddrType.setStatus("current")
_SdvsmFrequencyPlanReportIpAddr_Type = InetAddress
_SdvsmFrequencyPlanReportIpAddr_Object = MibTableColumn
sdvsmFrequencyPlanReportIpAddr = _SdvsmFrequencyPlanReportIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 3),
    _SdvsmFrequencyPlanReportIpAddr_Type()
)
sdvsmFrequencyPlanReportIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanReportIpAddr.setStatus("current")
_SdvsmFrequencyPlanReportPort_Type = Integer32
_SdvsmFrequencyPlanReportPort_Object = MibTableColumn
sdvsmFrequencyPlanReportPort = _SdvsmFrequencyPlanReportPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 4),
    _SdvsmFrequencyPlanReportPort_Type()
)
sdvsmFrequencyPlanReportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanReportPort.setStatus("current")


class _SdvsmFrequencyPlanReportInterval_Type(Integer32):
    """Custom type sdvsmFrequencyPlanReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SdvsmFrequencyPlanReportInterval_Type.__name__ = "Integer32"
_SdvsmFrequencyPlanReportInterval_Object = MibTableColumn
sdvsmFrequencyPlanReportInterval = _SdvsmFrequencyPlanReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 5),
    _SdvsmFrequencyPlanReportInterval_Type()
)
sdvsmFrequencyPlanReportInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanReportInterval.setUnits("hours")
_SdvsmFrequencyPlanMinFreqScanCount_Type = Integer32
_SdvsmFrequencyPlanMinFreqScanCount_Object = MibTableColumn
sdvsmFrequencyPlanMinFreqScanCount = _SdvsmFrequencyPlanMinFreqScanCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 6),
    _SdvsmFrequencyPlanMinFreqScanCount_Type()
)
sdvsmFrequencyPlanMinFreqScanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanMinFreqScanCount.setStatus("current")
_SdvsmFrequencyPlanMaxFreqScanTime_Type = Integer32
_SdvsmFrequencyPlanMaxFreqScanTime_Object = MibTableColumn
sdvsmFrequencyPlanMaxFreqScanTime = _SdvsmFrequencyPlanMaxFreqScanTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 7),
    _SdvsmFrequencyPlanMaxFreqScanTime_Type()
)
sdvsmFrequencyPlanMaxFreqScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanMaxFreqScanTime.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanMaxFreqScanTime.setUnits("seconds")


class _SdvsmFrequencyPlanDiscoveryMethod_Type(Integer32):
    """Custom type sdvsmFrequencyPlanDiscoveryMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frequencyPlusModulation", 1),
          ("sourceID", 2),
          ("virtualChannel", 3))
    )


_SdvsmFrequencyPlanDiscoveryMethod_Type.__name__ = "Integer32"
_SdvsmFrequencyPlanDiscoveryMethod_Object = MibTableColumn
sdvsmFrequencyPlanDiscoveryMethod = _SdvsmFrequencyPlanDiscoveryMethod_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 8),
    _SdvsmFrequencyPlanDiscoveryMethod_Type()
)
sdvsmFrequencyPlanDiscoveryMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanDiscoveryMethod.setStatus("current")
_SdvsmFrequencyPlanServiceGroup_Type = Integer32
_SdvsmFrequencyPlanServiceGroup_Object = MibTableColumn
sdvsmFrequencyPlanServiceGroup = _SdvsmFrequencyPlanServiceGroup_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 3, 1, 9),
    _SdvsmFrequencyPlanServiceGroup_Type()
)
sdvsmFrequencyPlanServiceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanServiceGroup.setStatus("current")
_SdvsmFrequencyPlanFreqTable_Object = MibTable
sdvsmFrequencyPlanFreqTable = _SdvsmFrequencyPlanFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanFreqTable.setStatus("current")
_SdvsmFrequencyPlanFreqEntry_Object = MibTableRow
sdvsmFrequencyPlanFreqEntry = _SdvsmFrequencyPlanFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 4, 1)
)
sdvsmFrequencyPlanFreqEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanIndex"),
)
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanFreqEntry.setStatus("current")
_SdvsmFrequencyPlanFrequency_Type = Integer32
_SdvsmFrequencyPlanFrequency_Object = MibTableColumn
sdvsmFrequencyPlanFrequency = _SdvsmFrequencyPlanFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 4, 1, 1),
    _SdvsmFrequencyPlanFrequency_Type()
)
sdvsmFrequencyPlanFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanFrequency.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanFrequency.setUnits("Hertz")
_SdvsmFrequencyPlanTSID_Type = Integer32
_SdvsmFrequencyPlanTSID_Object = MibTableColumn
sdvsmFrequencyPlanTSID = _SdvsmFrequencyPlanTSID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 4, 1, 2),
    _SdvsmFrequencyPlanTSID_Type()
)
sdvsmFrequencyPlanTSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmFrequencyPlanTSID.setStatus("current")
_SdvsmMpegProgNumRangeTable_Object = MibTable
sdvsmMpegProgNumRangeTable = _SdvsmMpegProgNumRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    sdvsmMpegProgNumRangeTable.setStatus("current")
_SdvsmMpegProgNumRangeEntry_Object = MibTableRow
sdvsmMpegProgNumRangeEntry = _SdvsmMpegProgNumRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 5, 1)
)
sdvsmMpegProgNumRangeEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmMpegProgNumRangeIndex"),
)
if mibBuilder.loadTexts:
    sdvsmMpegProgNumRangeEntry.setStatus("current")


class _SdvsmMpegProgNumRangeIndex_Type(Integer32):
    """Custom type sdvsmMpegProgNumRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SdvsmMpegProgNumRangeIndex_Type.__name__ = "Integer32"
_SdvsmMpegProgNumRangeIndex_Object = MibTableColumn
sdvsmMpegProgNumRangeIndex = _SdvsmMpegProgNumRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 5, 1, 1),
    _SdvsmMpegProgNumRangeIndex_Type()
)
sdvsmMpegProgNumRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdvsmMpegProgNumRangeIndex.setStatus("current")


class _SdvsmMpegProgNumRangeLowEnd_Type(Integer32):
    """Custom type sdvsmMpegProgNumRangeLowEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmMpegProgNumRangeLowEnd_Type.__name__ = "Integer32"
_SdvsmMpegProgNumRangeLowEnd_Object = MibTableColumn
sdvsmMpegProgNumRangeLowEnd = _SdvsmMpegProgNumRangeLowEnd_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 5, 1, 2),
    _SdvsmMpegProgNumRangeLowEnd_Type()
)
sdvsmMpegProgNumRangeLowEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMpegProgNumRangeLowEnd.setStatus("current")


class _SdvsmMpegProgNumRangeHighEnd_Type(Integer32):
    """Custom type sdvsmMpegProgNumRangeHighEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmMpegProgNumRangeHighEnd_Type.__name__ = "Integer32"
_SdvsmMpegProgNumRangeHighEnd_Object = MibTableColumn
sdvsmMpegProgNumRangeHighEnd = _SdvsmMpegProgNumRangeHighEnd_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 5, 1, 3),
    _SdvsmMpegProgNumRangeHighEnd_Type()
)
sdvsmMpegProgNumRangeHighEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmMpegProgNumRangeHighEnd.setStatus("current")
_SdvsmOdrmrTable_Object = MibTable
sdvsmOdrmrTable = _SdvsmOdrmrTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    sdvsmOdrmrTable.setStatus("current")
_SdvsmOdrmrEntry_Object = MibTableRow
sdvsmOdrmrEntry = _SdvsmOdrmrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 6, 1)
)
sdvsmOdrmrEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmOdrmrIndex"),
)
if mibBuilder.loadTexts:
    sdvsmOdrmrEntry.setStatus("current")


class _SdvsmOdrmrIndex_Type(Integer32):
    """Custom type sdvsmOdrmrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SdvsmOdrmrIndex_Type.__name__ = "Integer32"
_SdvsmOdrmrIndex_Object = MibTableColumn
sdvsmOdrmrIndex = _SdvsmOdrmrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 6, 1, 1),
    _SdvsmOdrmrIndex_Type()
)
sdvsmOdrmrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdvsmOdrmrIndex.setStatus("current")
_SdvsmOdrmrName_Type = DisplayString
_SdvsmOdrmrName_Object = MibTableColumn
sdvsmOdrmrName = _SdvsmOdrmrName_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 6, 1, 2),
    _SdvsmOdrmrName_Type()
)
sdvsmOdrmrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOdrmrName.setStatus("current")
_SdvsmOdrmrIpAddrType_Type = InetAddressType
_SdvsmOdrmrIpAddrType_Object = MibTableColumn
sdvsmOdrmrIpAddrType = _SdvsmOdrmrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 6, 1, 3),
    _SdvsmOdrmrIpAddrType_Type()
)
sdvsmOdrmrIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOdrmrIpAddrType.setStatus("current")
_SdvsmOdrmrIpAddr_Type = InetAddress
_SdvsmOdrmrIpAddr_Object = MibTableColumn
sdvsmOdrmrIpAddr = _SdvsmOdrmrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 6, 1, 4),
    _SdvsmOdrmrIpAddr_Type()
)
sdvsmOdrmrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOdrmrIpAddr.setStatus("current")


class _SdvsmOdrmrTcpPort_Type(Integer32):
    """Custom type sdvsmOdrmrTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdvsmOdrmrTcpPort_Type.__name__ = "Integer32"
_SdvsmOdrmrTcpPort_Object = MibTableColumn
sdvsmOdrmrTcpPort = _SdvsmOdrmrTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 6, 1, 5),
    _SdvsmOdrmrTcpPort_Type()
)
sdvsmOdrmrTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOdrmrTcpPort.setStatus("current")
_SdvsmAdZoneTable_Object = MibTable
sdvsmAdZoneTable = _SdvsmAdZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    sdvsmAdZoneTable.setStatus("current")
_SdvsmAdZoneEntry_Object = MibTableRow
sdvsmAdZoneEntry = _SdvsmAdZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 7, 1)
)
sdvsmAdZoneEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmServiceGroupID"),
)
if mibBuilder.loadTexts:
    sdvsmAdZoneEntry.setStatus("current")
_SdvsmAdZoneID_Type = Unsigned32
_SdvsmAdZoneID_Object = MibTableColumn
sdvsmAdZoneID = _SdvsmAdZoneID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 7, 1, 1),
    _SdvsmAdZoneID_Type()
)
sdvsmAdZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmAdZoneID.setStatus("current")
_SdvsmOfferedPrograms_ObjectIdentity = ObjectIdentity
sdvsmOfferedPrograms = _SdvsmOfferedPrograms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    sdvsmOfferedPrograms.setStatus("current")
_SdvsmOfferedProgramTable_Object = MibTable
sdvsmOfferedProgramTable = _SdvsmOfferedProgramTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    sdvsmOfferedProgramTable.setStatus("current")
_SdvsmOfferedProgramEntry_Object = MibTableRow
sdvsmOfferedProgramEntry = _SdvsmOfferedProgramEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1)
)
sdvsmOfferedProgramEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramSourceID"),
    (0, "SCTE-HMS-SDV-MIB", "sdvsmAdZoneID"),
)
if mibBuilder.loadTexts:
    sdvsmOfferedProgramEntry.setStatus("current")


class _SdvsmOfferedProgramSourceID_Type(Integer32):
    """Custom type sdvsmOfferedProgramSourceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmOfferedProgramSourceID_Type.__name__ = "Integer32"
_SdvsmOfferedProgramSourceID_Object = MibTableColumn
sdvsmOfferedProgramSourceID = _SdvsmOfferedProgramSourceID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 1),
    _SdvsmOfferedProgramSourceID_Type()
)
sdvsmOfferedProgramSourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramSourceID.setStatus("current")
_SdvsmOfferedProgramName_Type = DisplayString
_SdvsmOfferedProgramName_Object = MibTableColumn
sdvsmOfferedProgramName = _SdvsmOfferedProgramName_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 2),
    _SdvsmOfferedProgramName_Type()
)
sdvsmOfferedProgramName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramName.setStatus("current")


class _SdvsmOfferedProgramPriority_Type(Integer32):
    """Custom type sdvsmOfferedProgramPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SdvsmOfferedProgramPriority_Type.__name__ = "Integer32"
_SdvsmOfferedProgramPriority_Object = MibTableColumn
sdvsmOfferedProgramPriority = _SdvsmOfferedProgramPriority_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 3),
    _SdvsmOfferedProgramPriority_Type()
)
sdvsmOfferedProgramPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramPriority.setStatus("current")


class _SdvsmOfferedProgramEncryption_Type(Integer32):
    """Custom type sdvsmOfferedProgramEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dvb", 2),
          ("mediaCipher", 3),
          ("powerKEY", 4),
          ("nds", 5))
    )


_SdvsmOfferedProgramEncryption_Type.__name__ = "Integer32"
_SdvsmOfferedProgramEncryption_Object = MibTableColumn
sdvsmOfferedProgramEncryption = _SdvsmOfferedProgramEncryption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 4),
    _SdvsmOfferedProgramEncryption_Type()
)
sdvsmOfferedProgramEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramEncryption.setStatus("current")


class _SdvsmOfferedProgramEncoding_Type(Integer32):
    """Custom type sdvsmOfferedProgramEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mpeg2", 1),
          ("h264", 2),
          ("vc1", 3))
    )


_SdvsmOfferedProgramEncoding_Type.__name__ = "Integer32"
_SdvsmOfferedProgramEncoding_Object = MibTableColumn
sdvsmOfferedProgramEncoding = _SdvsmOfferedProgramEncoding_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 5),
    _SdvsmOfferedProgramEncoding_Type()
)
sdvsmOfferedProgramEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramEncoding.setStatus("current")


class _SdvsmOfferedProgramResolution_Type(Integer32):
    """Custom type sdvsmOfferedProgramResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sd", 1),
          ("hd", 2))
    )


_SdvsmOfferedProgramResolution_Type.__name__ = "Integer32"
_SdvsmOfferedProgramResolution_Object = MibTableColumn
sdvsmOfferedProgramResolution = _SdvsmOfferedProgramResolution_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 6),
    _SdvsmOfferedProgramResolution_Type()
)
sdvsmOfferedProgramResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramResolution.setStatus("current")
_SdvsmOfferedProgramBW_Type = Integer32
_SdvsmOfferedProgramBW_Object = MibTableColumn
sdvsmOfferedProgramBW = _SdvsmOfferedProgramBW_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 7),
    _SdvsmOfferedProgramBW_Type()
)
sdvsmOfferedProgramBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramBW.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramBW.setUnits("bps")


class _SdvsmOfferedProgramReclaimTime_Type(Integer32):
    """Custom type sdvsmOfferedProgramReclaimTime based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 65535),
    )


_SdvsmOfferedProgramReclaimTime_Type.__name__ = "Integer32"
_SdvsmOfferedProgramReclaimTime_Object = MibTableColumn
sdvsmOfferedProgramReclaimTime = _SdvsmOfferedProgramReclaimTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 8),
    _SdvsmOfferedProgramReclaimTime_Type()
)
sdvsmOfferedProgramReclaimTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramReclaimTime.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramReclaimTime.setUnits("minutes")


class _SdvsmOfferedProgramRecapAckTime_Type(Integer32):
    """Custom type sdvsmOfferedProgramRecapAckTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 9999),
    )


_SdvsmOfferedProgramRecapAckTime_Type.__name__ = "Integer32"
_SdvsmOfferedProgramRecapAckTime_Object = MibTableColumn
sdvsmOfferedProgramRecapAckTime = _SdvsmOfferedProgramRecapAckTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 9),
    _SdvsmOfferedProgramRecapAckTime_Type()
)
sdvsmOfferedProgramRecapAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramRecapAckTime.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramRecapAckTime.setUnits("seconds")
_SdvsmOfferedProgramInputMpegNo_Type = Integer32
_SdvsmOfferedProgramInputMpegNo_Object = MibTableColumn
sdvsmOfferedProgramInputMpegNo = _SdvsmOfferedProgramInputMpegNo_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 10),
    _SdvsmOfferedProgramInputMpegNo_Type()
)
sdvsmOfferedProgramInputMpegNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramInputMpegNo.setStatus("current")


class _SdvsmOfferedProgramState_Type(Integer32):
    """Custom type sdvsmOfferedProgramState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switched", 1),
          ("dynamic", 2))
    )


_SdvsmOfferedProgramState_Type.__name__ = "Integer32"
_SdvsmOfferedProgramState_Object = MibTableColumn
sdvsmOfferedProgramState = _SdvsmOfferedProgramState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 11),
    _SdvsmOfferedProgramState_Type()
)
sdvsmOfferedProgramState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramState.setStatus("current")
_SdvsmOfferedProgramProviderID_Type = Integer32
_SdvsmOfferedProgramProviderID_Object = MibTableColumn
sdvsmOfferedProgramProviderID = _SdvsmOfferedProgramProviderID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 12),
    _SdvsmOfferedProgramProviderID_Type()
)
sdvsmOfferedProgramProviderID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramProviderID.setStatus("current")
_SdvsmOfferedProgramAssetID_Type = Integer32
_SdvsmOfferedProgramAssetID_Object = MibTableColumn
sdvsmOfferedProgramAssetID = _SdvsmOfferedProgramAssetID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 1, 1, 13),
    _SdvsmOfferedProgramAssetID_Type()
)
sdvsmOfferedProgramAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramAssetID.setStatus("current")
_SdvsmOfferedProgramMulticastTable_Object = MibTable
sdvsmOfferedProgramMulticastTable = _SdvsmOfferedProgramMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    sdvsmOfferedProgramMulticastTable.setStatus("current")
_SdvsmOfferedProgramMulticastEntry_Object = MibTableRow
sdvsmOfferedProgramMulticastEntry = _SdvsmOfferedProgramMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 2, 1)
)
sdvsmOfferedProgramMulticastEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramSourceID"),
    (0, "SCTE-HMS-SDV-MIB", "sdvsmAdZoneID"),
)
if mibBuilder.loadTexts:
    sdvsmOfferedProgramMulticastEntry.setStatus("current")
_SdvsmOfferedProgramMulticastSourceIpAddrType_Type = InetAddressType
_SdvsmOfferedProgramMulticastSourceIpAddrType_Object = MibTableColumn
sdvsmOfferedProgramMulticastSourceIpAddrType = _SdvsmOfferedProgramMulticastSourceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 2, 1, 1),
    _SdvsmOfferedProgramMulticastSourceIpAddrType_Type()
)
sdvsmOfferedProgramMulticastSourceIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramMulticastSourceIpAddrType.setStatus("current")
_SdvsmOfferedProgramMulticastSourceIpAddr_Type = InetAddress
_SdvsmOfferedProgramMulticastSourceIpAddr_Object = MibTableColumn
sdvsmOfferedProgramMulticastSourceIpAddr = _SdvsmOfferedProgramMulticastSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 2, 1, 2),
    _SdvsmOfferedProgramMulticastSourceIpAddr_Type()
)
sdvsmOfferedProgramMulticastSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramMulticastSourceIpAddr.setStatus("current")
_SdvsmOfferedProgramMulticastIpAddrType_Type = InetAddressType
_SdvsmOfferedProgramMulticastIpAddrType_Object = MibTableColumn
sdvsmOfferedProgramMulticastIpAddrType = _SdvsmOfferedProgramMulticastIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 2, 1, 3),
    _SdvsmOfferedProgramMulticastIpAddrType_Type()
)
sdvsmOfferedProgramMulticastIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramMulticastIpAddrType.setStatus("current")
_SdvsmOfferedProgramMulticastIpAddr_Type = InetAddress
_SdvsmOfferedProgramMulticastIpAddr_Object = MibTableColumn
sdvsmOfferedProgramMulticastIpAddr = _SdvsmOfferedProgramMulticastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 2, 1, 4),
    _SdvsmOfferedProgramMulticastIpAddr_Type()
)
sdvsmOfferedProgramMulticastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramMulticastIpAddr.setStatus("current")


class _SdvsmOfferedProgramMulticastPort_Type(Integer32):
    """Custom type sdvsmOfferedProgramMulticastPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmOfferedProgramMulticastPort_Type.__name__ = "Integer32"
_SdvsmOfferedProgramMulticastPort_Object = MibTableColumn
sdvsmOfferedProgramMulticastPort = _SdvsmOfferedProgramMulticastPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 2, 1, 5),
    _SdvsmOfferedProgramMulticastPort_Type()
)
sdvsmOfferedProgramMulticastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramMulticastPort.setStatus("current")


class _SdvsmOfferedProgramMulticastSourcePriority_Type(Integer32):
    """Custom type sdvsmOfferedProgramMulticastSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3))
    )


_SdvsmOfferedProgramMulticastSourcePriority_Type.__name__ = "Integer32"
_SdvsmOfferedProgramMulticastSourcePriority_Object = MibTableColumn
sdvsmOfferedProgramMulticastSourcePriority = _SdvsmOfferedProgramMulticastSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 3, 8, 2, 1, 6),
    _SdvsmOfferedProgramMulticastSourcePriority_Type()
)
sdvsmOfferedProgramMulticastSourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmOfferedProgramMulticastSourcePriority.setStatus("current")
_SdvsmSTBCapabilities_ObjectIdentity = ObjectIdentity
sdvsmSTBCapabilities = _SdvsmSTBCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sdvsmSTBCapabilities.setStatus("current")
_SdvsmSTBMacAddrTable_Object = MibTable
sdvsmSTBMacAddrTable = _SdvsmSTBMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sdvsmSTBMacAddrTable.setStatus("current")
_SdvsmSTBMacAddrEntry_Object = MibTableRow
sdvsmSTBMacAddrEntry = _SdvsmSTBMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 1, 1)
)
sdvsmSTBMacAddrEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmSTBIpAddr"),
)
if mibBuilder.loadTexts:
    sdvsmSTBMacAddrEntry.setStatus("current")
_SdvsmSTBMacAddress_Type = MacAddress
_SdvsmSTBMacAddress_Object = MibTableColumn
sdvsmSTBMacAddress = _SdvsmSTBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 1, 1, 1),
    _SdvsmSTBMacAddress_Type()
)
sdvsmSTBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBMacAddress.setStatus("current")
_SdvsmSTBTable_Object = MibTable
sdvsmSTBTable = _SdvsmSTBTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sdvsmSTBTable.setStatus("current")
_SdvsmSTBEntry_Object = MibTableRow
sdvsmSTBEntry = _SdvsmSTBEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1)
)
sdvsmSTBEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmSTBMacAddress"),
)
if mibBuilder.loadTexts:
    sdvsmSTBEntry.setStatus("current")
_SdvsmSTBIpAddrType_Type = InetAddressType
_SdvsmSTBIpAddrType_Object = MibTableColumn
sdvsmSTBIpAddrType = _SdvsmSTBIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 1),
    _SdvsmSTBIpAddrType_Type()
)
sdvsmSTBIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBIpAddrType.setStatus("current")
_SdvsmSTBIpAddr_Type = InetAddress
_SdvsmSTBIpAddr_Object = MibTableColumn
sdvsmSTBIpAddr = _SdvsmSTBIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 2),
    _SdvsmSTBIpAddr_Type()
)
sdvsmSTBIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdvsmSTBIpAddr.setStatus("current")
_SdvsmSTBCapabilityDescriptorResolution_Type = Integer32
_SdvsmSTBCapabilityDescriptorResolution_Object = MibTableColumn
sdvsmSTBCapabilityDescriptorResolution = _SdvsmSTBCapabilityDescriptorResolution_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 3),
    _SdvsmSTBCapabilityDescriptorResolution_Type()
)
sdvsmSTBCapabilityDescriptorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBCapabilityDescriptorResolution.setStatus("current")


class _SdvsmSTBStreamLUAEvent_Type(Integer32):
    """Custom type sdvsmSTBStreamLUAEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 1),
          ("tune", 2),
          ("keyPress", 3))
    )


_SdvsmSTBStreamLUAEvent_Type.__name__ = "Integer32"
_SdvsmSTBStreamLUAEvent_Object = MibTableColumn
sdvsmSTBStreamLUAEvent = _SdvsmSTBStreamLUAEvent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 4),
    _SdvsmSTBStreamLUAEvent_Type()
)
sdvsmSTBStreamLUAEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBStreamLUAEvent.setStatus("current")
_SdvsmSTBStreamLUATime_Type = DateAndTime
_SdvsmSTBStreamLUATime_Object = MibTableColumn
sdvsmSTBStreamLUATime = _SdvsmSTBStreamLUATime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 5),
    _SdvsmSTBStreamLUATime_Type()
)
sdvsmSTBStreamLUATime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBStreamLUATime.setStatus("current")
_SdvsmSTBStreamProgramID_Type = Integer32
_SdvsmSTBStreamProgramID_Object = MibTableColumn
sdvsmSTBStreamProgramID = _SdvsmSTBStreamProgramID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 6),
    _SdvsmSTBStreamProgramID_Type()
)
sdvsmSTBStreamProgramID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBStreamProgramID.setStatus("current")


class _SdvsmSTBCaSystemBitmap_Type(Integer32):
    """Custom type sdvsmSTBCaSystemBitmap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmSTBCaSystemBitmap_Type.__name__ = "Integer32"
_SdvsmSTBCaSystemBitmap_Object = MibTableColumn
sdvsmSTBCaSystemBitmap = _SdvsmSTBCaSystemBitmap_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 7),
    _SdvsmSTBCaSystemBitmap_Type()
)
sdvsmSTBCaSystemBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBCaSystemBitmap.setStatus("current")


class _SdvsmSTBCaSystemID_Type(Integer32):
    """Custom type sdvsmSTBCaSystemID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmSTBCaSystemID_Type.__name__ = "Integer32"
_SdvsmSTBCaSystemID_Object = MibTableColumn
sdvsmSTBCaSystemID = _SdvsmSTBCaSystemID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 8),
    _SdvsmSTBCaSystemID_Type()
)
sdvsmSTBCaSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBCaSystemID.setStatus("current")


class _SdvsmSTBNetworkBitmap_Type(Integer32):
    """Custom type sdvsmSTBNetworkBitmap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmSTBNetworkBitmap_Type.__name__ = "Integer32"
_SdvsmSTBNetworkBitmap_Object = MibTableColumn
sdvsmSTBNetworkBitmap = _SdvsmSTBNetworkBitmap_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 9),
    _SdvsmSTBNetworkBitmap_Type()
)
sdvsmSTBNetworkBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBNetworkBitmap.setStatus("current")
_SdvsmSTBDvrSize_Type = Integer32
_SdvsmSTBDvrSize_Object = MibTableColumn
sdvsmSTBDvrSize = _SdvsmSTBDvrSize_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 10),
    _SdvsmSTBDvrSize_Type()
)
sdvsmSTBDvrSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBDvrSize.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmSTBDvrSize.setUnits("GB")


class _SdvsmSTBTotalNumTuners_Type(Integer32):
    """Custom type sdvsmSTBTotalNumTuners based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmSTBTotalNumTuners_Type.__name__ = "Integer32"
_SdvsmSTBTotalNumTuners_Object = MibTableColumn
sdvsmSTBTotalNumTuners = _SdvsmSTBTotalNumTuners_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 4, 2, 1, 11),
    _SdvsmSTBTotalNumTuners_Type()
)
sdvsmSTBTotalNumTuners.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBTotalNumTuners.setStatus("current")
_SdvsmSTBTunerCapabilitiesTable_Object = MibTable
sdvsmSTBTunerCapabilitiesTable = _SdvsmSTBTunerCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sdvsmSTBTunerCapabilitiesTable.setStatus("current")
_SdvsmSTBTunerCapabilitiesEntry_Object = MibTableRow
sdvsmSTBTunerCapabilitiesEntry = _SdvsmSTBTunerCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 5, 1)
)
sdvsmSTBTunerCapabilitiesEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmSTBMacAddress"),
)
if mibBuilder.loadTexts:
    sdvsmSTBTunerCapabilitiesEntry.setStatus("current")
_SdvsmSTBTunerIdentifier_Type = Integer32
_SdvsmSTBTunerIdentifier_Object = MibTableColumn
sdvsmSTBTunerIdentifier = _SdvsmSTBTunerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 5, 1, 1),
    _SdvsmSTBTunerIdentifier_Type()
)
sdvsmSTBTunerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBTunerIdentifier.setStatus("current")


class _SdvsmSTBVideoDecodeBitmap_Type(Integer32):
    """Custom type sdvsmSTBVideoDecodeBitmap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmSTBVideoDecodeBitmap_Type.__name__ = "Integer32"
_SdvsmSTBVideoDecodeBitmap_Object = MibTableColumn
sdvsmSTBVideoDecodeBitmap = _SdvsmSTBVideoDecodeBitmap_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 5, 1, 2),
    _SdvsmSTBVideoDecodeBitmap_Type()
)
sdvsmSTBVideoDecodeBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBVideoDecodeBitmap.setStatus("current")


class _SdvsmSTBAudioDecodeBitmap_Type(Integer32):
    """Custom type sdvsmSTBAudioDecodeBitmap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmSTBAudioDecodeBitmap_Type.__name__ = "Integer32"
_SdvsmSTBAudioDecodeBitmap_Object = MibTableColumn
sdvsmSTBAudioDecodeBitmap = _SdvsmSTBAudioDecodeBitmap_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 5, 1, 3),
    _SdvsmSTBAudioDecodeBitmap_Type()
)
sdvsmSTBAudioDecodeBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBAudioDecodeBitmap.setStatus("current")
_SdvsmServiceGroupTable_Object = MibTable
sdvsmServiceGroupTable = _SdvsmServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sdvsmServiceGroupTable.setStatus("current")
_SdvsmServiceGroupEntry_Object = MibTableRow
sdvsmServiceGroupEntry = _SdvsmServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1)
)
sdvsmServiceGroupEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmServiceGroupID"),
)
if mibBuilder.loadTexts:
    sdvsmServiceGroupEntry.setStatus("current")
_SdvsmServiceGroupID_Type = Unsigned32
_SdvsmServiceGroupID_Object = MibTableColumn
sdvsmServiceGroupID = _SdvsmServiceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 1),
    _SdvsmServiceGroupID_Type()
)
sdvsmServiceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupID.setStatus("current")
_SdvsmServiceGroupLowWaterMark_Type = Integer32
_SdvsmServiceGroupLowWaterMark_Object = MibTableColumn
sdvsmServiceGroupLowWaterMark = _SdvsmServiceGroupLowWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 2),
    _SdvsmServiceGroupLowWaterMark_Type()
)
sdvsmServiceGroupLowWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupLowWaterMark.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmServiceGroupLowWaterMark.setUnits("bps")
_SdvsmServiceGroupShareableBW_Type = Integer32
_SdvsmServiceGroupShareableBW_Object = MibTableColumn
sdvsmServiceGroupShareableBW = _SdvsmServiceGroupShareableBW_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 3),
    _SdvsmServiceGroupShareableBW_Type()
)
sdvsmServiceGroupShareableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupShareableBW.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmServiceGroupShareableBW.setUnits("bps")
_SdvsmServiceGroupHighWaterMark_Type = Integer32
_SdvsmServiceGroupHighWaterMark_Object = MibTableColumn
sdvsmServiceGroupHighWaterMark = _SdvsmServiceGroupHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 4),
    _SdvsmServiceGroupHighWaterMark_Type()
)
sdvsmServiceGroupHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupHighWaterMark.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmServiceGroupHighWaterMark.setUnits("bps")
_SdvsmServiceGroupTotalBW_Type = Integer32
_SdvsmServiceGroupTotalBW_Object = MibTableColumn
sdvsmServiceGroupTotalBW = _SdvsmServiceGroupTotalBW_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 5),
    _SdvsmServiceGroupTotalBW_Type()
)
sdvsmServiceGroupTotalBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupTotalBW.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmServiceGroupTotalBW.setUnits("bps")
_SdvsmServiceGroupActiveSdvBW_Type = Integer32
_SdvsmServiceGroupActiveSdvBW_Object = MibTableColumn
sdvsmServiceGroupActiveSdvBW = _SdvsmServiceGroupActiveSdvBW_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 6),
    _SdvsmServiceGroupActiveSdvBW_Type()
)
sdvsmServiceGroupActiveSdvBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupActiveSdvBW.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmServiceGroupActiveSdvBW.setUnits("bps")


class _SdvsmServiceGroupBwThreshold_Type(Integer32):
    """Custom type sdvsmServiceGroupBwThreshold based on Integer32"""
    defaultValue = 90


_SdvsmServiceGroupBwThreshold_Type.__name__ = "Integer32"
_SdvsmServiceGroupBwThreshold_Object = MibTableColumn
sdvsmServiceGroupBwThreshold = _SdvsmServiceGroupBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 7),
    _SdvsmServiceGroupBwThreshold_Type()
)
sdvsmServiceGroupBwThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupBwThreshold.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmServiceGroupBwThreshold.setUnits("%")
_SdvsmServiceGroupPeakBW_Type = Integer32
_SdvsmServiceGroupPeakBW_Object = MibTableColumn
sdvsmServiceGroupPeakBW = _SdvsmServiceGroupPeakBW_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 8),
    _SdvsmServiceGroupPeakBW_Type()
)
sdvsmServiceGroupPeakBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupPeakBW.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmServiceGroupPeakBW.setUnits("bps")
_SdvsmServiceGroupPeakTime_Type = DateAndTime
_SdvsmServiceGroupPeakTime_Object = MibTableColumn
sdvsmServiceGroupPeakTime = _SdvsmServiceGroupPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 9),
    _SdvsmServiceGroupPeakTime_Type()
)
sdvsmServiceGroupPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupPeakTime.setStatus("current")
_SdvsmServiceGroupPrevPeakTime_Type = DateAndTime
_SdvsmServiceGroupPrevPeakTime_Object = MibTableColumn
sdvsmServiceGroupPrevPeakTime = _SdvsmServiceGroupPrevPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 10),
    _SdvsmServiceGroupPrevPeakTime_Type()
)
sdvsmServiceGroupPrevPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupPrevPeakTime.setStatus("current")
_SdvsmServiceGroupPrevPeakBW_Type = Integer32
_SdvsmServiceGroupPrevPeakBW_Object = MibTableColumn
sdvsmServiceGroupPrevPeakBW = _SdvsmServiceGroupPrevPeakBW_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 11),
    _SdvsmServiceGroupPrevPeakBW_Type()
)
sdvsmServiceGroupPrevPeakBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupPrevPeakBW.setStatus("current")
if mibBuilder.loadTexts:
    sdvsmServiceGroupPrevPeakBW.setUnits("bps")
_SdvsmServiceGroupYearPeakTime_Type = DateAndTime
_SdvsmServiceGroupYearPeakTime_Object = MibTableColumn
sdvsmServiceGroupYearPeakTime = _SdvsmServiceGroupYearPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 12),
    _SdvsmServiceGroupYearPeakTime_Type()
)
sdvsmServiceGroupYearPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupYearPeakTime.setStatus("current")
_SdvsmServiceGroupCcRequests_Type = Integer32
_SdvsmServiceGroupCcRequests_Object = MibTableColumn
sdvsmServiceGroupCcRequests = _SdvsmServiceGroupCcRequests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 13),
    _SdvsmServiceGroupCcRequests_Type()
)
sdvsmServiceGroupCcRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupCcRequests.setStatus("current")
_SdvsmServiceGroupCcSDRequests_Type = Integer32
_SdvsmServiceGroupCcSDRequests_Object = MibTableColumn
sdvsmServiceGroupCcSDRequests = _SdvsmServiceGroupCcSDRequests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 14),
    _SdvsmServiceGroupCcSDRequests_Type()
)
sdvsmServiceGroupCcSDRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupCcSDRequests.setStatus("current")
_SdvsmServiceGroupCcHDequests_Type = Integer32
_SdvsmServiceGroupCcHDequests_Object = MibTableColumn
sdvsmServiceGroupCcHDequests = _SdvsmServiceGroupCcHDequests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 15),
    _SdvsmServiceGroupCcHDequests_Type()
)
sdvsmServiceGroupCcHDequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupCcHDequests.setStatus("current")
_SdvsmServiceGroupCcNCRequests_Type = Integer32
_SdvsmServiceGroupCcNCRequests_Object = MibTableColumn
sdvsmServiceGroupCcNCRequests = _SdvsmServiceGroupCcNCRequests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 16),
    _SdvsmServiceGroupCcNCRequests_Type()
)
sdvsmServiceGroupCcNCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupCcNCRequests.setStatus("current")
_SdvsmServiceGroupCcH264Requests_Type = Integer32
_SdvsmServiceGroupCcH264Requests_Object = MibTableColumn
sdvsmServiceGroupCcH264Requests = _SdvsmServiceGroupCcH264Requests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 17),
    _SdvsmServiceGroupCcH264Requests_Type()
)
sdvsmServiceGroupCcH264Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupCcH264Requests.setStatus("current")
_SdvsmServiceGroupCcVC1Requests_Type = Integer32
_SdvsmServiceGroupCcVC1Requests_Object = MibTableColumn
sdvsmServiceGroupCcVC1Requests = _SdvsmServiceGroupCcVC1Requests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 18),
    _SdvsmServiceGroupCcVC1Requests_Type()
)
sdvsmServiceGroupCcVC1Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupCcVC1Requests.setStatus("current")
_SdvsmServiceGroupFailedBindings_Type = Integer32
_SdvsmServiceGroupFailedBindings_Object = MibTableColumn
sdvsmServiceGroupFailedBindings = _SdvsmServiceGroupFailedBindings_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 19),
    _SdvsmServiceGroupFailedBindings_Type()
)
sdvsmServiceGroupFailedBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupFailedBindings.setStatus("current")
_SdvsmServiceGroupFailedSDBindings_Type = Integer32
_SdvsmServiceGroupFailedSDBindings_Object = MibTableColumn
sdvsmServiceGroupFailedSDBindings = _SdvsmServiceGroupFailedSDBindings_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 20),
    _SdvsmServiceGroupFailedSDBindings_Type()
)
sdvsmServiceGroupFailedSDBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupFailedSDBindings.setStatus("current")
_SdvsmServiceGroupFailedHDBindings_Type = Integer32
_SdvsmServiceGroupFailedHDBindings_Object = MibTableColumn
sdvsmServiceGroupFailedHDBindings = _SdvsmServiceGroupFailedHDBindings_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 21),
    _SdvsmServiceGroupFailedHDBindings_Type()
)
sdvsmServiceGroupFailedHDBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupFailedHDBindings.setStatus("current")
_SdvsmServiceGroupFailedNCBindings_Type = Integer32
_SdvsmServiceGroupFailedNCBindings_Object = MibTableColumn
sdvsmServiceGroupFailedNCBindings = _SdvsmServiceGroupFailedNCBindings_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 22),
    _SdvsmServiceGroupFailedNCBindings_Type()
)
sdvsmServiceGroupFailedNCBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupFailedNCBindings.setStatus("current")
_SdvsmServiceGroupFailedH264Bindings_Type = Integer32
_SdvsmServiceGroupFailedH264Bindings_Object = MibTableColumn
sdvsmServiceGroupFailedH264Bindings = _SdvsmServiceGroupFailedH264Bindings_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 23),
    _SdvsmServiceGroupFailedH264Bindings_Type()
)
sdvsmServiceGroupFailedH264Bindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupFailedH264Bindings.setStatus("current")
_SdvsmServiceGroupFailedVC1Bindings_Type = Integer32
_SdvsmServiceGroupFailedVC1Bindings_Object = MibTableColumn
sdvsmServiceGroupFailedVC1Bindings = _SdvsmServiceGroupFailedVC1Bindings_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 24),
    _SdvsmServiceGroupFailedVC1Bindings_Type()
)
sdvsmServiceGroupFailedVC1Bindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupFailedVC1Bindings.setStatus("current")
_SdvsmServiceGroupCcWM9Requests_Type = Integer32
_SdvsmServiceGroupCcWM9Requests_Object = MibTableColumn
sdvsmServiceGroupCcWM9Requests = _SdvsmServiceGroupCcWM9Requests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 25),
    _SdvsmServiceGroupCcWM9Requests_Type()
)
sdvsmServiceGroupCcWM9Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupCcWM9Requests.setStatus("current")
_SdvsmServiceGroupMCPIpAddrType_Type = InetAddressType
_SdvsmServiceGroupMCPIpAddrType_Object = MibTableColumn
sdvsmServiceGroupMCPIpAddrType = _SdvsmServiceGroupMCPIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 26),
    _SdvsmServiceGroupMCPIpAddrType_Type()
)
sdvsmServiceGroupMCPIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupMCPIpAddrType.setStatus("current")
_SdvsmServiceGroupMCPIpAddr_Type = InetAddress
_SdvsmServiceGroupMCPIpAddr_Object = MibTableColumn
sdvsmServiceGroupMCPIpAddr = _SdvsmServiceGroupMCPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 27),
    _SdvsmServiceGroupMCPIpAddr_Type()
)
sdvsmServiceGroupMCPIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupMCPIpAddr.setStatus("current")
_SdvsmServiceGroupMCversion_Type = Integer32
_SdvsmServiceGroupMCversion_Object = MibTableColumn
sdvsmServiceGroupMCversion = _SdvsmServiceGroupMCversion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 28),
    _SdvsmServiceGroupMCversion_Type()
)
sdvsmServiceGroupMCversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupMCversion.setStatus("current")
_SdvsmServiceGroupActiveSTBs_Type = Integer32
_SdvsmServiceGroupActiveSTBs_Object = MibTableColumn
sdvsmServiceGroupActiveSTBs = _SdvsmServiceGroupActiveSTBs_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 29),
    _SdvsmServiceGroupActiveSTBs_Type()
)
sdvsmServiceGroupActiveSTBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupActiveSTBs.setStatus("current")


class _SdvsmServiceGroupSTBCapacity_Type(Integer32):
    """Custom type sdvsmServiceGroupSTBCapacity based on Integer32"""
    defaultValue = 2000


_SdvsmServiceGroupSTBCapacity_Type.__name__ = "Integer32"
_SdvsmServiceGroupSTBCapacity_Object = MibTableColumn
sdvsmServiceGroupSTBCapacity = _SdvsmServiceGroupSTBCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 6, 1, 30),
    _SdvsmServiceGroupSTBCapacity_Type()
)
sdvsmServiceGroupSTBCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmServiceGroupSTBCapacity.setStatus("current")
_SdvsmActiveProgramTable_Object = MibTable
sdvsmActiveProgramTable = _SdvsmActiveProgramTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 7)
)
if mibBuilder.loadTexts:
    sdvsmActiveProgramTable.setStatus("current")
_SdvsmActiveProgramEntry_Object = MibTableRow
sdvsmActiveProgramEntry = _SdvsmActiveProgramEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 7, 1)
)
sdvsmActiveProgramEntry.setIndexNames(
    (0, "SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramSourceID"),
    (0, "SCTE-HMS-SDV-MIB", "sdvsmServiceGroupID"),
    (0, "SCTE-HMS-SDV-MIB", "sdvsmAdZoneID"),
)
if mibBuilder.loadTexts:
    sdvsmActiveProgramEntry.setStatus("current")


class _SdvsmActiveProgramSessionID_Type(OctetString):
    """Custom type sdvsmActiveProgramSessionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SdvsmActiveProgramSessionID_Type.__name__ = "OctetString"
_SdvsmActiveProgramSessionID_Object = MibTableColumn
sdvsmActiveProgramSessionID = _SdvsmActiveProgramSessionID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 7, 1, 1),
    _SdvsmActiveProgramSessionID_Type()
)
sdvsmActiveProgramSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmActiveProgramSessionID.setStatus("current")


class _SdvsmActiveProgramMpegPN_Type(Integer32):
    """Custom type sdvsmActiveProgramMpegPN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdvsmActiveProgramMpegPN_Type.__name__ = "Integer32"
_SdvsmActiveProgramMpegPN_Object = MibTableColumn
sdvsmActiveProgramMpegPN = _SdvsmActiveProgramMpegPN_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 7, 1, 2),
    _SdvsmActiveProgramMpegPN_Type()
)
sdvsmActiveProgramMpegPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmActiveProgramMpegPN.setStatus("current")
_SdvsmActiveProgramNumUsers_Type = Integer32
_SdvsmActiveProgramNumUsers_Object = MibTableColumn
sdvsmActiveProgramNumUsers = _SdvsmActiveProgramNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 7, 1, 3),
    _SdvsmActiveProgramNumUsers_Type()
)
sdvsmActiveProgramNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmActiveProgramNumUsers.setStatus("current")
_SdvsmActiveProgramBW_Type = Integer32
_SdvsmActiveProgramBW_Object = MibTableColumn
sdvsmActiveProgramBW = _SdvsmActiveProgramBW_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 7, 1, 4),
    _SdvsmActiveProgramBW_Type()
)
sdvsmActiveProgramBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmActiveProgramBW.setStatus("current")
_SdvsmActiveProgramIsfallback_Type = TruthValue
_SdvsmActiveProgramIsfallback_Object = MibTableColumn
sdvsmActiveProgramIsfallback = _SdvsmActiveProgramIsfallback_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 7, 1, 5),
    _SdvsmActiveProgramIsfallback_Type()
)
sdvsmActiveProgramIsfallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmActiveProgramIsfallback.setStatus("current")
_SdvsmDiagnostics_ObjectIdentity = ObjectIdentity
sdvsmDiagnostics = _SdvsmDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 8)
)


class _SdvsmNumberSTBs_Type(Integer32):
    """Custom type sdvsmNumberSTBs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_SdvsmNumberSTBs_Type.__name__ = "Integer32"
_SdvsmNumberSTBs_Object = MibScalar
sdvsmNumberSTBs = _SdvsmNumberSTBs_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 8, 1),
    _SdvsmNumberSTBs_Type()
)
sdvsmNumberSTBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmNumberSTBs.setStatus("current")


class _SdvsmSTBCapacityStatus_Type(Integer32):
    """Custom type sdvsmSTBCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("minor", 2),
          ("major", 3))
    )


_SdvsmSTBCapacityStatus_Type.__name__ = "Integer32"
_SdvsmSTBCapacityStatus_Object = MibScalar
sdvsmSTBCapacityStatus = _SdvsmSTBCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 8, 2),
    _SdvsmSTBCapacityStatus_Type()
)
sdvsmSTBCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSTBCapacityStatus.setStatus("current")


class _SdvsmSRMStatus_Type(Integer32):
    """Custom type sdvsmSRMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("major", 2))
    )


_SdvsmSRMStatus_Type.__name__ = "Integer32"
_SdvsmSRMStatus_Object = MibScalar
sdvsmSRMStatus = _SdvsmSRMStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 8, 3),
    _SdvsmSRMStatus_Type()
)
sdvsmSRMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSRMStatus.setStatus("current")
_SdvsmSRMRequests_Type = Integer32
_SdvsmSRMRequests_Object = MibScalar
sdvsmSRMRequests = _SdvsmSRMRequests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 8, 4),
    _SdvsmSRMRequests_Type()
)
sdvsmSRMRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSRMRequests.setStatus("current")
_SdvsmSRMRequestDenied_Type = Integer32
_SdvsmSRMRequestDenied_Object = MibScalar
sdvsmSRMRequestDenied = _SdvsmSRMRequestDenied_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 8, 5),
    _SdvsmSRMRequestDenied_Type()
)
sdvsmSRMRequestDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmSRMRequestDenied.setStatus("current")
_SdvsmInvalidSGRequests_Type = Integer32
_SdvsmInvalidSGRequests_Object = MibScalar
sdvsmInvalidSGRequests = _SdvsmInvalidSGRequests_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 1, 8, 6),
    _SdvsmInvalidSGRequests_Type()
)
sdvsmInvalidSGRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdvsmInvalidSGRequests.setStatus("current")
_SdvServerEvents_ObjectIdentity = ObjectIdentity
sdvServerEvents = _SdvServerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2)
)
_SdvServerEventsV2_ObjectIdentity = ObjectIdentity
sdvServerEventsV2 = _SdvServerEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2, 0)
)
_SdvServerConformance_ObjectIdentity = ObjectIdentity
sdvServerConformance = _SdvServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3)
)
_SdvServerCompliances_ObjectIdentity = ObjectIdentity
sdvServerCompliances = _SdvServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 1)
)
_SdvServerGroups_ObjectIdentity = ObjectIdentity
sdvServerGroups = _SdvServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 2)
)

# Managed Objects groups

sdvsmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 2, 1)
)
sdvsmConfigGroup.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmMiniCarouselPath"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMiniCarouselBitRate"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMiniCarouselDestIpAddrType"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMiniCarouselDestIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMiniCarouselUdpPort"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanIpAddrType"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanReportIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanReportPort"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanReportInterval"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanMinFreqScanCount"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanMaxFreqScanTime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanDiscoveryMethod"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanServiceGroup"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramSourceID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramPriority"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramEncryption"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramEncoding"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramResolution"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramBW"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramReclaimTime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramRecapAckTime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramInputMpegNo"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramState"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramProviderID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramAssetID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastSourceIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastPort"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMpegProgNumRangeLowEnd"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMiniCarouselSize"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMiniCarouselTransmissionFrequency"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanIndex"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMacAddress"),
        ("SCTE-HMS-SDV-MIB", "sdvsmName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMpegProgNumRangeHighEnd"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanFrequency"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanTSID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOdrmrName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOdrmrIpAddrType"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOdrmrIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOdrmrTcpPort"))
)
if mibBuilder.loadTexts:
    sdvsmConfigGroup.setStatus("current")

sdvsmDiagsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 2, 2)
)
sdvsmDiagsGroup.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmNumberSTBs"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBCapacityStatus"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSRMStatus"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSRMRequests"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSRMRequestDenied"),
        ("SCTE-HMS-SDV-MIB", "sdvsmInvalidSGRequests"))
)
if mibBuilder.loadTexts:
    sdvsmDiagsGroup.setStatus("current")

sdvsmServiceGrpObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 2, 3)
)
sdvsmServiceGrpObjsGroup.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupTotalBW"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupActiveSdvBW"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupBwThreshold"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupPeakBW"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupPeakTime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupPrevPeakTime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupPrevPeakBW"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupYearPeakTime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupCcRequests"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupCcSDRequests"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupCcHDequests"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupCcNCRequests"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupCcH264Requests"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupCcVC1Requests"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupFailedBindings"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupFailedSDBindings"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupFailedHDBindings"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupFailedNCBindings"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupFailedH264Bindings"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupFailedVC1Bindings"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupCcWM9Requests"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupMCPIpAddrType"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupMCPIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupMCversion"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupActiveSTBs"),
        ("SCTE-HMS-SDV-MIB", "sdvsmAdZoneID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupSTBCapacity"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupLowWaterMark"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupShareableBW"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGroupHighWaterMark"))
)
if mibBuilder.loadTexts:
    sdvsmServiceGrpObjsGroup.setStatus("current")

sdvsmProgramGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 2, 4)
)
sdvsmProgramGroup.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmActiveProgramSessionID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmActiveProgramMpegPN"),
        ("SCTE-HMS-SDV-MIB", "sdvsmActiveProgramNumUsers"),
        ("SCTE-HMS-SDV-MIB", "sdvsmActiveProgramBW"),
        ("SCTE-HMS-SDV-MIB", "sdvsmActiveProgramIsfallback"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramSourceID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramPriority"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramEncryption"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramEncoding"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramResolution"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramBW"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramReclaimTime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramRecapAckTime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramInputMpegNo"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramState"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramProviderID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramAssetID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastSourceIpAddrType"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastSourceIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastIpAddrType"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastPort"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramMulticastSourcePriority"))
)
if mibBuilder.loadTexts:
    sdvsmProgramGroup.setStatus("current")

sdvsmSTBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 2, 5)
)
sdvsmSTBGroup.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmSTBIpAddrType"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBIpAddr"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBCapabilityDescriptorResolution"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBStreamLUAEvent"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBStreamLUATime"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBStreamProgramID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBVideoDecodeBitmap"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBTunerIdentifier"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBAudioDecodeBitmap"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBCaSystemBitmap"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBCaSystemID"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBNetworkBitmap"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBDvrSize"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBTotalNumTuners"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBMacAddress"))
)
if mibBuilder.loadTexts:
    sdvsmSTBGroup.setStatus("current")

sdvsmClientConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 2, 6)
)
sdvsmClientConfigGroup.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmClientRexmitPgmSelectInterval"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientLastUserActivityInterval"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientMsgRespTimeout"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientMsgReqMaxRetries"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientMsgReqMinRetryInterval"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientMsgReqMaxRetryInterval"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientUserInteractionTimeout"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientDefaultCaSystemId"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientDefaultEncoding"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientDefaultCapabilities"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientTunerHealthTest"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientMinimizeChannelReport"))
)
if mibBuilder.loadTexts:
    sdvsmClientConfigGroup.setStatus("current")


# Notification objects

sdvsmInitTrapInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2, 0, 1)
)
sdvsmInitTrapInfo.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMacAddress"))
)
if mibBuilder.loadTexts:
    sdvsmInitTrapInfo.setStatus(
        "current"
    )

sdvsmHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2, 0, 2)
)
sdvsmHeartbeatTrap.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMacAddress"))
)
if mibBuilder.loadTexts:
    sdvsmHeartbeatTrap.setStatus(
        "current"
    )

sdvsmProvisionedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2, 0, 3)
)
sdvsmProvisionedTrap.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMacAddress"))
)
if mibBuilder.loadTexts:
    sdvsmProvisionedTrap.setStatus(
        "current"
    )

sdvSsmProgramViewersRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2, 0, 4)
)
sdvSsmProgramViewersRemovedTrap.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMacAddress"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramPriority"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramInputMpegNo"),
        ("SCTE-HMS-SDV-MIB", "sdvsmActiveProgramSessionID"))
)
if mibBuilder.loadTexts:
    sdvSsmProgramViewersRemovedTrap.setStatus(
        "current"
    )

sdvsmLackBWDeniedCC = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2, 0, 5)
)
sdvsmLackBWDeniedCC.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMacAddress"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmOfferedProgramBW"))
)
if mibBuilder.loadTexts:
    sdvsmLackBWDeniedCC.setStatus(
        "current"
    )

sdvsmExceededTunerCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2, 0, 6)
)
sdvsmExceededTunerCount.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMiniCarouselDestIpAddr"))
)
if mibBuilder.loadTexts:
    sdvsmExceededTunerCount.setStatus(
        "current"
    )

sdvsmAutoDiscoverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 2, 0, 7)
)
sdvsmAutoDiscoverFailure.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmName"),
        ("SCTE-HMS-SDV-MIB", "sdvsmMacAddress"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanServiceGroup"),
        ("SCTE-HMS-SDV-MIB", "sdvsmFrequencyPlanTSID"))
)
if mibBuilder.loadTexts:
    sdvsmAutoDiscoverFailure.setStatus(
        "current"
    )


# Notifications groups

sdvsmTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 2, 7)
)
sdvsmTrapGroup.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmInitTrapInfo"),
        ("SCTE-HMS-SDV-MIB", "sdvsmHeartbeatTrap"),
        ("SCTE-HMS-SDV-MIB", "sdvsmProvisionedTrap"),
        ("SCTE-HMS-SDV-MIB", "sdvSsmProgramViewersRemovedTrap"),
        ("SCTE-HMS-SDV-MIB", "sdvsmLackBWDeniedCC"),
        ("SCTE-HMS-SDV-MIB", "sdvsmExceededTunerCount"),
        ("SCTE-HMS-SDV-MIB", "sdvsmAutoDiscoverFailure"))
)
if mibBuilder.loadTexts:
    sdvsmTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sdvServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 6, 1, 3, 1, 1)
)
sdvServerCompliance.setObjects(
      *(("SCTE-HMS-SDV-MIB", "sdvsmConfigGroup"),
        ("SCTE-HMS-SDV-MIB", "sdvsmDiagsGroup"),
        ("SCTE-HMS-SDV-MIB", "sdvsmServiceGrpObjsGroup"),
        ("SCTE-HMS-SDV-MIB", "sdvsmSTBGroup"),
        ("SCTE-HMS-SDV-MIB", "sdvsmTrapGroup"),
        ("SCTE-HMS-SDV-MIB", "sdvsmProgramGroup"),
        ("SCTE-HMS-SDV-MIB", "sdvsmClientConfigGroup"))
)
if mibBuilder.loadTexts:
    sdvServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-SDV-MIB",
    **{"hmsScteSdvMib": hmsScteSdvMib,
       "sdvServerMIBObjects": sdvServerMIBObjects,
       "sdvsmName": sdvsmName,
       "sdvsmMacAddress": sdvsmMacAddress,
       "sdvsmConfigObjects": sdvsmConfigObjects,
       "sdvsmMiniCarouselTable": sdvsmMiniCarouselTable,
       "sdvsmMiniCarouselEntry": sdvsmMiniCarouselEntry,
       "sdvsmMiniCarouselPath": sdvsmMiniCarouselPath,
       "sdvsmMiniCarouselBitRate": sdvsmMiniCarouselBitRate,
       "sdvsmMiniCarouselDestIpAddrType": sdvsmMiniCarouselDestIpAddrType,
       "sdvsmMiniCarouselDestIpAddr": sdvsmMiniCarouselDestIpAddr,
       "sdvsmMiniCarouselUdpPort": sdvsmMiniCarouselUdpPort,
       "sdvsmMiniCarouselSize": sdvsmMiniCarouselSize,
       "sdvsmMiniCarouselTransmissionFrequency": sdvsmMiniCarouselTransmissionFrequency,
       "sdvsmClientTable": sdvsmClientTable,
       "sdvsmClientEntry": sdvsmClientEntry,
       "sdvsmClientRexmitPgmSelectInterval": sdvsmClientRexmitPgmSelectInterval,
       "sdvsmClientLastUserActivityInterval": sdvsmClientLastUserActivityInterval,
       "sdvsmClientMsgRespTimeout": sdvsmClientMsgRespTimeout,
       "sdvsmClientMsgReqMaxRetries": sdvsmClientMsgReqMaxRetries,
       "sdvsmClientMsgReqMinRetryInterval": sdvsmClientMsgReqMinRetryInterval,
       "sdvsmClientMsgReqMaxRetryInterval": sdvsmClientMsgReqMaxRetryInterval,
       "sdvsmClientUserInteractionTimeout": sdvsmClientUserInteractionTimeout,
       "sdvsmClientDefaultCaSystemId": sdvsmClientDefaultCaSystemId,
       "sdvsmClientDefaultEncoding": sdvsmClientDefaultEncoding,
       "sdvsmClientDefaultCapabilities": sdvsmClientDefaultCapabilities,
       "sdvsmClientTunerHealthTest": sdvsmClientTunerHealthTest,
       "sdvsmClientMinimizeChannelReport": sdvsmClientMinimizeChannelReport,
       "sdvsmFrequencyPlanTable": sdvsmFrequencyPlanTable,
       "sdvsmFrequencyPlanEntry": sdvsmFrequencyPlanEntry,
       "sdvsmFrequencyPlanIndex": sdvsmFrequencyPlanIndex,
       "sdvsmFrequencyPlanIpAddrType": sdvsmFrequencyPlanIpAddrType,
       "sdvsmFrequencyPlanReportIpAddr": sdvsmFrequencyPlanReportIpAddr,
       "sdvsmFrequencyPlanReportPort": sdvsmFrequencyPlanReportPort,
       "sdvsmFrequencyPlanReportInterval": sdvsmFrequencyPlanReportInterval,
       "sdvsmFrequencyPlanMinFreqScanCount": sdvsmFrequencyPlanMinFreqScanCount,
       "sdvsmFrequencyPlanMaxFreqScanTime": sdvsmFrequencyPlanMaxFreqScanTime,
       "sdvsmFrequencyPlanDiscoveryMethod": sdvsmFrequencyPlanDiscoveryMethod,
       "sdvsmFrequencyPlanServiceGroup": sdvsmFrequencyPlanServiceGroup,
       "sdvsmFrequencyPlanFreqTable": sdvsmFrequencyPlanFreqTable,
       "sdvsmFrequencyPlanFreqEntry": sdvsmFrequencyPlanFreqEntry,
       "sdvsmFrequencyPlanFrequency": sdvsmFrequencyPlanFrequency,
       "sdvsmFrequencyPlanTSID": sdvsmFrequencyPlanTSID,
       "sdvsmMpegProgNumRangeTable": sdvsmMpegProgNumRangeTable,
       "sdvsmMpegProgNumRangeEntry": sdvsmMpegProgNumRangeEntry,
       "sdvsmMpegProgNumRangeIndex": sdvsmMpegProgNumRangeIndex,
       "sdvsmMpegProgNumRangeLowEnd": sdvsmMpegProgNumRangeLowEnd,
       "sdvsmMpegProgNumRangeHighEnd": sdvsmMpegProgNumRangeHighEnd,
       "sdvsmOdrmrTable": sdvsmOdrmrTable,
       "sdvsmOdrmrEntry": sdvsmOdrmrEntry,
       "sdvsmOdrmrIndex": sdvsmOdrmrIndex,
       "sdvsmOdrmrName": sdvsmOdrmrName,
       "sdvsmOdrmrIpAddrType": sdvsmOdrmrIpAddrType,
       "sdvsmOdrmrIpAddr": sdvsmOdrmrIpAddr,
       "sdvsmOdrmrTcpPort": sdvsmOdrmrTcpPort,
       "sdvsmAdZoneTable": sdvsmAdZoneTable,
       "sdvsmAdZoneEntry": sdvsmAdZoneEntry,
       "sdvsmAdZoneID": sdvsmAdZoneID,
       "sdvsmOfferedPrograms": sdvsmOfferedPrograms,
       "sdvsmOfferedProgramTable": sdvsmOfferedProgramTable,
       "sdvsmOfferedProgramEntry": sdvsmOfferedProgramEntry,
       "sdvsmOfferedProgramSourceID": sdvsmOfferedProgramSourceID,
       "sdvsmOfferedProgramName": sdvsmOfferedProgramName,
       "sdvsmOfferedProgramPriority": sdvsmOfferedProgramPriority,
       "sdvsmOfferedProgramEncryption": sdvsmOfferedProgramEncryption,
       "sdvsmOfferedProgramEncoding": sdvsmOfferedProgramEncoding,
       "sdvsmOfferedProgramResolution": sdvsmOfferedProgramResolution,
       "sdvsmOfferedProgramBW": sdvsmOfferedProgramBW,
       "sdvsmOfferedProgramReclaimTime": sdvsmOfferedProgramReclaimTime,
       "sdvsmOfferedProgramRecapAckTime": sdvsmOfferedProgramRecapAckTime,
       "sdvsmOfferedProgramInputMpegNo": sdvsmOfferedProgramInputMpegNo,
       "sdvsmOfferedProgramState": sdvsmOfferedProgramState,
       "sdvsmOfferedProgramProviderID": sdvsmOfferedProgramProviderID,
       "sdvsmOfferedProgramAssetID": sdvsmOfferedProgramAssetID,
       "sdvsmOfferedProgramMulticastTable": sdvsmOfferedProgramMulticastTable,
       "sdvsmOfferedProgramMulticastEntry": sdvsmOfferedProgramMulticastEntry,
       "sdvsmOfferedProgramMulticastSourceIpAddrType": sdvsmOfferedProgramMulticastSourceIpAddrType,
       "sdvsmOfferedProgramMulticastSourceIpAddr": sdvsmOfferedProgramMulticastSourceIpAddr,
       "sdvsmOfferedProgramMulticastIpAddrType": sdvsmOfferedProgramMulticastIpAddrType,
       "sdvsmOfferedProgramMulticastIpAddr": sdvsmOfferedProgramMulticastIpAddr,
       "sdvsmOfferedProgramMulticastPort": sdvsmOfferedProgramMulticastPort,
       "sdvsmOfferedProgramMulticastSourcePriority": sdvsmOfferedProgramMulticastSourcePriority,
       "sdvsmSTBCapabilities": sdvsmSTBCapabilities,
       "sdvsmSTBMacAddrTable": sdvsmSTBMacAddrTable,
       "sdvsmSTBMacAddrEntry": sdvsmSTBMacAddrEntry,
       "sdvsmSTBMacAddress": sdvsmSTBMacAddress,
       "sdvsmSTBTable": sdvsmSTBTable,
       "sdvsmSTBEntry": sdvsmSTBEntry,
       "sdvsmSTBIpAddrType": sdvsmSTBIpAddrType,
       "sdvsmSTBIpAddr": sdvsmSTBIpAddr,
       "sdvsmSTBCapabilityDescriptorResolution": sdvsmSTBCapabilityDescriptorResolution,
       "sdvsmSTBStreamLUAEvent": sdvsmSTBStreamLUAEvent,
       "sdvsmSTBStreamLUATime": sdvsmSTBStreamLUATime,
       "sdvsmSTBStreamProgramID": sdvsmSTBStreamProgramID,
       "sdvsmSTBCaSystemBitmap": sdvsmSTBCaSystemBitmap,
       "sdvsmSTBCaSystemID": sdvsmSTBCaSystemID,
       "sdvsmSTBNetworkBitmap": sdvsmSTBNetworkBitmap,
       "sdvsmSTBDvrSize": sdvsmSTBDvrSize,
       "sdvsmSTBTotalNumTuners": sdvsmSTBTotalNumTuners,
       "sdvsmSTBTunerCapabilitiesTable": sdvsmSTBTunerCapabilitiesTable,
       "sdvsmSTBTunerCapabilitiesEntry": sdvsmSTBTunerCapabilitiesEntry,
       "sdvsmSTBTunerIdentifier": sdvsmSTBTunerIdentifier,
       "sdvsmSTBVideoDecodeBitmap": sdvsmSTBVideoDecodeBitmap,
       "sdvsmSTBAudioDecodeBitmap": sdvsmSTBAudioDecodeBitmap,
       "sdvsmServiceGroupTable": sdvsmServiceGroupTable,
       "sdvsmServiceGroupEntry": sdvsmServiceGroupEntry,
       "sdvsmServiceGroupID": sdvsmServiceGroupID,
       "sdvsmServiceGroupLowWaterMark": sdvsmServiceGroupLowWaterMark,
       "sdvsmServiceGroupShareableBW": sdvsmServiceGroupShareableBW,
       "sdvsmServiceGroupHighWaterMark": sdvsmServiceGroupHighWaterMark,
       "sdvsmServiceGroupTotalBW": sdvsmServiceGroupTotalBW,
       "sdvsmServiceGroupActiveSdvBW": sdvsmServiceGroupActiveSdvBW,
       "sdvsmServiceGroupBwThreshold": sdvsmServiceGroupBwThreshold,
       "sdvsmServiceGroupPeakBW": sdvsmServiceGroupPeakBW,
       "sdvsmServiceGroupPeakTime": sdvsmServiceGroupPeakTime,
       "sdvsmServiceGroupPrevPeakTime": sdvsmServiceGroupPrevPeakTime,
       "sdvsmServiceGroupPrevPeakBW": sdvsmServiceGroupPrevPeakBW,
       "sdvsmServiceGroupYearPeakTime": sdvsmServiceGroupYearPeakTime,
       "sdvsmServiceGroupCcRequests": sdvsmServiceGroupCcRequests,
       "sdvsmServiceGroupCcSDRequests": sdvsmServiceGroupCcSDRequests,
       "sdvsmServiceGroupCcHDequests": sdvsmServiceGroupCcHDequests,
       "sdvsmServiceGroupCcNCRequests": sdvsmServiceGroupCcNCRequests,
       "sdvsmServiceGroupCcH264Requests": sdvsmServiceGroupCcH264Requests,
       "sdvsmServiceGroupCcVC1Requests": sdvsmServiceGroupCcVC1Requests,
       "sdvsmServiceGroupFailedBindings": sdvsmServiceGroupFailedBindings,
       "sdvsmServiceGroupFailedSDBindings": sdvsmServiceGroupFailedSDBindings,
       "sdvsmServiceGroupFailedHDBindings": sdvsmServiceGroupFailedHDBindings,
       "sdvsmServiceGroupFailedNCBindings": sdvsmServiceGroupFailedNCBindings,
       "sdvsmServiceGroupFailedH264Bindings": sdvsmServiceGroupFailedH264Bindings,
       "sdvsmServiceGroupFailedVC1Bindings": sdvsmServiceGroupFailedVC1Bindings,
       "sdvsmServiceGroupCcWM9Requests": sdvsmServiceGroupCcWM9Requests,
       "sdvsmServiceGroupMCPIpAddrType": sdvsmServiceGroupMCPIpAddrType,
       "sdvsmServiceGroupMCPIpAddr": sdvsmServiceGroupMCPIpAddr,
       "sdvsmServiceGroupMCversion": sdvsmServiceGroupMCversion,
       "sdvsmServiceGroupActiveSTBs": sdvsmServiceGroupActiveSTBs,
       "sdvsmServiceGroupSTBCapacity": sdvsmServiceGroupSTBCapacity,
       "sdvsmActiveProgramTable": sdvsmActiveProgramTable,
       "sdvsmActiveProgramEntry": sdvsmActiveProgramEntry,
       "sdvsmActiveProgramSessionID": sdvsmActiveProgramSessionID,
       "sdvsmActiveProgramMpegPN": sdvsmActiveProgramMpegPN,
       "sdvsmActiveProgramNumUsers": sdvsmActiveProgramNumUsers,
       "sdvsmActiveProgramBW": sdvsmActiveProgramBW,
       "sdvsmActiveProgramIsfallback": sdvsmActiveProgramIsfallback,
       "sdvsmDiagnostics": sdvsmDiagnostics,
       "sdvsmNumberSTBs": sdvsmNumberSTBs,
       "sdvsmSTBCapacityStatus": sdvsmSTBCapacityStatus,
       "sdvsmSRMStatus": sdvsmSRMStatus,
       "sdvsmSRMRequests": sdvsmSRMRequests,
       "sdvsmSRMRequestDenied": sdvsmSRMRequestDenied,
       "sdvsmInvalidSGRequests": sdvsmInvalidSGRequests,
       "sdvServerEvents": sdvServerEvents,
       "sdvServerEventsV2": sdvServerEventsV2,
       "sdvsmInitTrapInfo": sdvsmInitTrapInfo,
       "sdvsmHeartbeatTrap": sdvsmHeartbeatTrap,
       "sdvsmProvisionedTrap": sdvsmProvisionedTrap,
       "sdvSsmProgramViewersRemovedTrap": sdvSsmProgramViewersRemovedTrap,
       "sdvsmLackBWDeniedCC": sdvsmLackBWDeniedCC,
       "sdvsmExceededTunerCount": sdvsmExceededTunerCount,
       "sdvsmAutoDiscoverFailure": sdvsmAutoDiscoverFailure,
       "sdvServerConformance": sdvServerConformance,
       "sdvServerCompliances": sdvServerCompliances,
       "sdvServerCompliance": sdvServerCompliance,
       "sdvServerGroups": sdvServerGroups,
       "sdvsmConfigGroup": sdvsmConfigGroup,
       "sdvsmDiagsGroup": sdvsmDiagsGroup,
       "sdvsmServiceGrpObjsGroup": sdvsmServiceGrpObjsGroup,
       "sdvsmProgramGroup": sdvsmProgramGroup,
       "sdvsmSTBGroup": sdvsmSTBGroup,
       "sdvsmClientConfigGroup": sdvsmClientConfigGroup,
       "sdvsmTrapGroup": sdvsmTrapGroup}
)
