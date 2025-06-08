# SNMP MIB module (WMAN-IF2-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-IF2-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:18:43 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

wmanIf2TcMib = ModuleIdentity(
    (1, 0, 8802, 16, 6)
)
if mibBuilder.loadTexts:
    wmanIf2TcMib.setRevisions(
        ("2009-01-28 00:00",
         "2008-12-01 00:00",
         "2008-10-01 00:00",
         "2008-07-22 00:00",
         "2008-05-27 00:00",
         "2008-03-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class WmanIf2TcBsIdType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class WmanIf2TcChannelNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )



class WmanIf2TcCidType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class WmanIf2TcCsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("gpcs", 0),
          ("packetIpV4", 1),
          ("packetIpV6", 2),
          ("packet802dot3Ethernet", 3),
          ("reserved4", 4),
          ("packetIpV4Over802dot3", 5),
          ("packetIpV6Over802dot3", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("atm", 9),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("packetIp", 14))
    )



class WmanIf2TcIpv6FlowLabel(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3



class WmanIf2TcPhsRuleVerify(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phsVerifyEnable", 0),
          ("phsVerifyDisable", 1))
    )



class WmanIf2TcSchedulingType(TextualConvention, Integer32):
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
        *(("undefined", 1),
          ("bestEffort", 2),
          ("nonRealTimePollingService", 3),
          ("realTimePollingService", 4),
          ("extRealTimePollingService", 5),
          ("unsolicitedGrantService", 6))
    )



class WmanIf2TcGlobalSrvClass(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ulDlIndicator", 0),
          ("maxSustainedRate0", 1),
          ("maxSustainedRate1", 2),
          ("maxSustainedRate2", 3),
          ("maxSustainedRate3", 4),
          ("maxSustainedRate4", 5),
          ("maxSustainedRate5", 6),
          ("trafficIndication", 7),
          ("maxTrafficBurst0", 8),
          ("maxTrafficBurst1", 9),
          ("maxTrafficBurst2", 10),
          ("maxTrafficBurst3", 11),
          ("maxTrafficBurst4", 12),
          ("maxTrafficBurst5", 13),
          ("minReservedRate0", 14),
          ("minReservedRate1", 15),
          ("minReservedRate2", 16),
          ("minReservedRate3", 17),
          ("minReservedRate4", 18),
          ("minReservedRate5", 19),
          ("maxLatency0", 20),
          ("maxLatency1", 21),
          ("maxLatency2", 22),
          ("maxLatency3", 23),
          ("maxLatency4", 24),
          ("maxLatency5", 25),
          ("sduIndicator", 26),
          ("pagingGeneration", 27),
          ("noBroadcastBr", 28),
          ("noMulticastBr", 29),
          ("noPiggybackReq", 30),
          ("noFragmentData", 31),
          ("noSurpressPayload", 32),
          ("noPackedSdu", 33),
          ("noCrcInMacPdu", 34),
          ("ulGrantType0", 35),
          ("ulGrantType1", 36),
          ("ulGrantType2", 37))
    )


class WmanIf2TcHarqAckDelay(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneframeoffset", 1),
          ("twoframesoffset", 2),
          ("threeframesoffset", 3))
    )



class WmanIf2TcMacVersion(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ieee802Dot16Of2001", 1),
          ("ieee802Dot16cOf2002andPredcessors", 2),
          ("ieee802Dot16aOf2003andPredcessors", 3),
          ("ieee802Dot16Of2004", 4),
          ("ieee802Dot16Of2004and16eOf2005", 5),
          ("ieee802Dot16Of2004and16efOf2005", 6),
          ("ieee802Dot16Of04and16efOf05and16gOf07", 7),
          ("ieee802Dot16Of2009", 8))
    )



class WmanIf2TcOfdmaCp(TextualConvention, Integer32):
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
        *(("oneForth", 0),
          ("oneEighth", 1),
          ("oneSixteenth", 2),
          ("oneThirtySecond", 3))
    )



class WmanIf2TcOfdmaFftSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fft2048", 0),
          ("fft1024", 1),
          ("fft512", 2),
          ("reserved", 3),
          ("fft128", 4))
    )



class WmanIf2TcOfdmaFrame(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("twoMs", 0),
          ("twoPointFiveMs", 1),
          ("fourMs", 2),
          ("fiveMs", 3),
          ("eightMs", 4),
          ("tenMs", 5),
          ("twelvePointFiveMs", 6),
          ("twentyMs", 7))
    )



class WmanIf2TcReqTxPolicy(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("noBroadcastBwReq", 0),
          ("noMulticastBwReq", 1),
          ("noPiggybackReq", 2),
          ("noFragmentData", 3),
          ("noPHS", 4),
          ("noSduPacking", 5),
          ("noCrc", 6),
          ("reserved2", 7))
    )


class WmanIf2TcSfDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )



class WmanIf2TcFrameOffset(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("frameOffsetCQICH0", 0),
          ("frameOffsetCQICH1", 1),
          ("frameOffsetCQICH2", 2),
          ("frameOffsetCQICH3", 3),
          ("frameOffsetData0", 4),
          ("frameOffsetData1", 5),
          ("frameOffsetData2", 6),
          ("frameOffsetData3", 7))
    )


class WmanIf2TcPwrCntlBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bq0", 0),
          ("bq1", 1),
          ("bq2", 2),
          ("bq3", 3),
          ("bd0", 4),
          ("bd1", 5),
          ("bd2", 6),
          ("bd3", 7))
    )


class WmanIf2TcFddDlGrpGap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("gapLocation", 0),
          ("interGroup1", 1),
          ("interGroup2", 2))
    )


class WmanIf2TcAasBeamSel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAllowed", 0),
          ("allowed", 1))
    )



class WmanIf2TcTxPowerReport(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tprThreshold0", 0),
          ("tprThreshold1", 1),
          ("tprThreshold2", 2),
          ("tprThreshold3", 3),
          ("tprInterval0", 4),
          ("tprInterval1", 5),
          ("tprInterval2", 6),
          ("tprInterval3", 7),
          ("tprApAvg0", 8),
          ("tprApAvg1", 9),
          ("tprApAvg2", 10),
          ("tprApAvg3", 11),
          ("cqichTprThreshold0", 12),
          ("cqichTprThreshold1", 13),
          ("cqichTprThreshold2", 14),
          ("cqichTprThreshold3", 15),
          ("cqichTprInterval0", 16),
          ("cqichTprInterval1", 17),
          ("cqichTprInterval2", 18),
          ("cqichTprInterval3", 19),
          ("cqichTprApAvg0", 20),
          ("cqichTprApAvg1", 21),
          ("cqichTprApAvg2", 22),
          ("cqichTprApAvg3", 23))
    )


class WmanIf2TcUlPhyModeId(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("channelBw0", 0),
          ("channelBw1", 1),
          ("channelBw2", 2),
          ("channelBw3", 3),
          ("channelBw4", 4),
          ("channelBw5", 5),
          ("channelBw6", 6),
          ("channelBw7", 7),
          ("fftSize0", 8),
          ("fftSize1", 9),
          ("fftSize2", 10),
          ("cyclePrefix0", 11),
          ("cyclePrefix1", 12),
          ("cyclePrefix2", 13))
    )


class WmanIf2TcFastFeedback(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("subChannel0", 3),
          ("subChannel1", 4),
          ("subChannel2", 5),
          ("subChannel3", 6),
          ("subChannel4", 7),
          ("subChannel5", 8),
          ("subChannel6", 9),
          ("ofdmaSymbol0", 10),
          ("ofdmaSymbol1", 11),
          ("ofdmaSymbol2", 12),
          ("ofdmaSymbol3", 13),
          ("ofdmaSymbol4", 14),
          ("ofdmaSymbol5", 15),
          ("ofdmaSymbol6", 16),
          ("subChannelOffset0", 17),
          ("subChannelOffset1", 18),
          ("subChannelOffset2", 19),
          ("subChannelOffset3", 20),
          ("subChannelOffset4", 21),
          ("subChannelOffset5", 22),
          ("subChannelOffset6", 23),
          ("ofdmaSymbolOffset0", 24),
          ("ofdmaSymbolOffset1", 25),
          ("ofdmaSymbolOffset2", 26),
          ("ofdmaSymbolOffset3", 27),
          ("ofdmaSymbolOffset4", 28),
          ("ofdmaSymbolOffset5", 29),
          ("ofdmaSymbolOffset6", 30),
          ("ofdmaSymbolOffset7", 31),
          ("periodiicityFrames0", 32),
          ("periodiicityFrames1", 33),
          ("periodiicityFrames2", 34),
          ("allocationFrames0", 35),
          ("allocationFrames1", 36),
          ("allocationFrames2", 37),
          ("allocationFrames3", 38),
          ("allocationFrames4", 39))
    )


class WmanIf2TcHarqAckRegion(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("numOfSubchannels0", 0),
          ("numOfSubchannels1", 1),
          ("numOfSubchannels2", 2),
          ("numofSubchannels3", 3),
          ("numOfOfdmaSym0", 4),
          ("numOfOfdmaSym1", 5),
          ("numOfOfdmaSym2", 6),
          ("numOfOfdmaSym3", 7),
          ("numOfOfdmaSym4", 8),
          ("subChannelOffset0", 9),
          ("subChannelOffset1", 10),
          ("subChannelOffset2", 11),
          ("subChannelOffset3", 12),
          ("subChannelOffset4", 13),
          ("subChannelOffset5", 14),
          ("subChannelOffset6", 15),
          ("ofdmaSymbolOffset0", 16),
          ("ofdmaSymbolOffset1", 17),
          ("ofdmaSymbolOffset2", 18),
          ("ofdmaSymbolOffset3", 19),
          ("ofdmaSymbolOffset4", 20),
          ("ofdmaSymbolOffset5", 21),
          ("ofdmaSymbolOffset6", 22),
          ("ofdmaSymbolOffset7", 23),
          ("periodicityFrames0", 24),
          ("periodicityFrames1", 25),
          ("periodicityFrames2", 26),
          ("allocationFrames0", 27),
          ("allocationFrames1", 28),
          ("allocationFrames2", 29),
          ("allocationFrames3", 30),
          ("allocationFrames4", 31))
    )


class WmanIf2TcRangingRegion(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dedicatedRangingInd", 0),
          ("rangingMethod0", 1),
          ("rangingMethod1", 2),
          ("numOfSubchannels0", 3),
          ("numOfSubchannels1", 4),
          ("numOfSubchannels2", 5),
          ("numOfSubchannels3", 6),
          ("numOfSubchannels4", 7),
          ("numOfSubchannels5", 8),
          ("numOfSubchannels6", 9),
          ("numOfOfdmaSym0", 10),
          ("numOfOfdmaSym1", 11),
          ("numOfOfdmaSym2", 12),
          ("numOfOfdmaSym3", 13),
          ("numOfOfdmaSym4", 14),
          ("numOfOfdmaSym5", 15),
          ("numOfOfdmaSym6", 16),
          ("subchannelOffset0", 17),
          ("subchannelOffset1", 18),
          ("subchannelOffset2", 19),
          ("subchannelOffset3", 20),
          ("subchannelOffset4", 21),
          ("subchannelOffset5", 22),
          ("subchannelOffset6", 23),
          ("ofdmaSymbolOffset0", 24),
          ("ofdmaSymbolOffset1", 25),
          ("ofdmaSymbolOffset2", 26),
          ("ofdmaSymbolOffset3", 27),
          ("ofdmaSymbolOffset4", 28),
          ("ofdmaSymbolOffset5", 29),
          ("ofdmaSymbolOffset6", 30),
          ("ofdmaSymbolOffset7", 31),
          ("periodicityFrames0", 32),
          ("periodicityFrames1", 33),
          ("periodicityFrames2", 34),
          ("allocationFrames0", 35),
          ("allocationFrames1", 36),
          ("allocationFrames2", 37),
          ("allocationFrames3", 38),
          ("allocationFrames4", 39))
    )


class WmanIf2TcSoundingRegion(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved", 0),
          ("paprReductionSafetyZone0", 1),
          ("paprReductionSafetyZone1", 2),
          ("numOfSubchannels0", 3),
          ("numOfSubchannels1", 4),
          ("numOfSubchannels2", 5),
          ("numOfSubchannels3", 6),
          ("numOfSubchannels4", 7),
          ("numOfSubchannels5", 8),
          ("numOfSubchannels6", 9),
          ("numOfOfdmaSym0", 10),
          ("numOfOfdmaSym1", 11),
          ("numOfOfdmaSym2", 12),
          ("numOfOfdmaSym3", 13),
          ("numOfOfdmaSym4", 14),
          ("numOfOfdmaSym5", 15),
          ("numOfOfdmaSym6", 16),
          ("subchannelOffset0", 17),
          ("subchannelOffset1", 18),
          ("subchannelOffset2", 19),
          ("subchannelOffset3", 20),
          ("subchannelOffset4", 21),
          ("subchannelOffset5", 22),
          ("subchannelOffset6", 23),
          ("ofdmaSymbolOffset0", 24),
          ("ofdmaSymbolOffset1", 25),
          ("ofdmaSymbolOffset2", 26),
          ("ofdmaSymbolOffset3", 27),
          ("ofdmaSymbolOffset4", 28),
          ("ofdmaSymbolOffset5", 29),
          ("ofdmaSymbolOffset6", 30),
          ("ofdmaSymbolOffset7", 31),
          ("periodicityFrames0", 32),
          ("periodicityFrames1", 33),
          ("periodicityFrames2", 34),
          ("allocationFrames0", 35),
          ("allocationFrames1", 36),
          ("allocationFrames2", 37),
          ("allocationFrames3", 38),
          ("allocationFrames4", 39))
    )


class WmanIf2TcRssiCinrAvg(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("defaultCinrAvg0", 0),
          ("defaultCinrAvg1", 1),
          ("defaultCinrAvg2", 2),
          ("defaultCinrAvg3", 3),
          ("defaultRssiAvg0", 4),
          ("defaultRssiAvg1", 5),
          ("defaultRssiAvg2", 6),
          ("defaultRssiAvg3", 7))
    )


class WmanIf2TcMihCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("mediaIndependentHandover", 0),
          ("eventService", 1),
          ("commandService", 2),
          ("informationService", 3),
          ("infoServiceDuringNtwkEntry", 4),
          ("esCsCapDiscoveryDuringNtwkEntry", 5))
    )


class WmanIf2TcHoSupportType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("handover", 0),
          ("mdHandover", 1),
          ("fbssHandover", 2))
    )


class WmanIf2TcPermutationTyp(TextualConvention, Integer32):
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
        *(("pusc", 1),
          ("fusc", 2),
          ("optionalFusc", 3),
          ("amc", 4))
    )



class WmanIf2TcArqBlockSize(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("m0", 0),
          ("m1", 1),
          ("m2", 2),
          ("m3", 3),
          ("n0", 4),
          ("n1", 5),
          ("n2", 6),
          ("n3", 7))
    )


class WmanIf2TcSduType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("variableLength", 0),
          ("fixedLength", 1))
    )



class WmanIf2TcFsnType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("threeBits", 0),
          ("elevenBits", 1))
    )



class WmanIf2TcMbsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("mbsInServingBs", 1),
          ("mbsInMultiBsZone", 2))
    )



class WmanIf2TcSfState(TextualConvention, Integer32):
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
        *(("inactive", 0),
          ("provisioned", 1),
          ("admitted", 2),
          ("active", 3))
    )



class WmanIf2TcArqDeliveInOrder(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("orderOfDeliveryNotPreserved", 0),
          ("orderOfDeliveryPreserved", 1))
    )



class WmanIf2TcArqDelvInOrder(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("orderOfDeliveryNotPreserved", 0),
          ("orderOfDeliveryPreserved", 1))
    )



class WmanIf2TcPwrCntlMode(TextualConvention, Integer32):
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
        *(("closedLoopPowerControl", 0),
          ("openLoopPassiveModeRetention", 1),
          ("openLoopPassiveModeReset", 2),
          ("openLoopActiveMode", 3))
    )



class WmanIf2TcCellType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("bsClasses0", 0),
          ("bsClasses1", 1),
          ("bsClasses2", 2),
          ("bsClasses3", 3),
          ("bsClasses4", 4),
          ("bsClasses5", 5),
          ("bsClasses6", 6),
          ("bsClasses7", 7),
          ("bsClasses8", 8),
          ("bsClasses9", 9),
          ("bsClasses10", 10),
          ("bsClasses11", 11),
          ("bsClasses12", 12),
          ("bsClasses13", 13),
          ("bsClasses14", 14),
          ("bsClasses15", 15))
    )



class WmanIf2TcCidDescriptor(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("a0", 0),
          ("a1", 1),
          ("a2", 2),
          ("a3", 3),
          ("a4", 4),
          ("m0", 5),
          ("m1", 6),
          ("m2", 7),
          ("m3", 8),
          ("m4", 9),
          ("m5", 10),
          ("m6", 11),
          ("m7", 12),
          ("m8", 13),
          ("m9", 14),
          ("m10", 15))
    )


class WmanIf2TcActionRule(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("discardPacket", 0)
    )


class WmanIf2TcIpTypOfServ(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("reserved1", 1),
          ("dscp1", 2),
          ("dscp2", 3),
          ("dscp3", 4),
          ("dscp4", 5),
          ("dscp5", 6),
          ("dscp6", 7))
    )


class WmanIf2TcClassifierMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("priority", 0),
          ("ipProtocol", 1),
          ("ipMaskedSrcAddr", 2),
          ("ipMaskedDestAddr", 3),
          ("srcPort", 4),
          ("destPort", 5),
          ("destMacAddr", 6),
          ("srcMacAddr", 7),
          ("ethernetProtocol", 8),
          ("userPriority", 9),
          ("vlanId", 10),
          ("associatedPhsi", 11),
          ("ipv6FlowLabel", 12),
          ("actionRule", 13),
          ("ipTypeOfService", 14))
    )


class WmanIf2TcEthernetType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ethertype", 1),
          ("dsap", 2))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-IF2-TC-MIB",
    **{"WmanIf2TcBsIdType": WmanIf2TcBsIdType,
       "WmanIf2TcChannelNumber": WmanIf2TcChannelNumber,
       "WmanIf2TcCidType": WmanIf2TcCidType,
       "WmanIf2TcCsType": WmanIf2TcCsType,
       "WmanIf2TcIpv6FlowLabel": WmanIf2TcIpv6FlowLabel,
       "WmanIf2TcPhsRuleVerify": WmanIf2TcPhsRuleVerify,
       "WmanIf2TcSchedulingType": WmanIf2TcSchedulingType,
       "WmanIf2TcGlobalSrvClass": WmanIf2TcGlobalSrvClass,
       "WmanIf2TcHarqAckDelay": WmanIf2TcHarqAckDelay,
       "WmanIf2TcMacVersion": WmanIf2TcMacVersion,
       "WmanIf2TcOfdmaCp": WmanIf2TcOfdmaCp,
       "WmanIf2TcOfdmaFftSize": WmanIf2TcOfdmaFftSize,
       "WmanIf2TcOfdmaFrame": WmanIf2TcOfdmaFrame,
       "WmanIf2TcReqTxPolicy": WmanIf2TcReqTxPolicy,
       "WmanIf2TcSfDirection": WmanIf2TcSfDirection,
       "WmanIf2TcFrameOffset": WmanIf2TcFrameOffset,
       "WmanIf2TcPwrCntlBits": WmanIf2TcPwrCntlBits,
       "WmanIf2TcFddDlGrpGap": WmanIf2TcFddDlGrpGap,
       "WmanIf2TcAasBeamSel": WmanIf2TcAasBeamSel,
       "WmanIf2TcTxPowerReport": WmanIf2TcTxPowerReport,
       "WmanIf2TcUlPhyModeId": WmanIf2TcUlPhyModeId,
       "WmanIf2TcFastFeedback": WmanIf2TcFastFeedback,
       "WmanIf2TcHarqAckRegion": WmanIf2TcHarqAckRegion,
       "WmanIf2TcRangingRegion": WmanIf2TcRangingRegion,
       "WmanIf2TcSoundingRegion": WmanIf2TcSoundingRegion,
       "WmanIf2TcRssiCinrAvg": WmanIf2TcRssiCinrAvg,
       "WmanIf2TcMihCapability": WmanIf2TcMihCapability,
       "WmanIf2TcHoSupportType": WmanIf2TcHoSupportType,
       "WmanIf2TcPermutationTyp": WmanIf2TcPermutationTyp,
       "WmanIf2TcArqBlockSize": WmanIf2TcArqBlockSize,
       "WmanIf2TcSduType": WmanIf2TcSduType,
       "WmanIf2TcFsnType": WmanIf2TcFsnType,
       "WmanIf2TcMbsType": WmanIf2TcMbsType,
       "WmanIf2TcSfState": WmanIf2TcSfState,
       "WmanIf2TcArqDeliveInOrder": WmanIf2TcArqDeliveInOrder,
       "WmanIf2TcArqDelvInOrder": WmanIf2TcArqDelvInOrder,
       "WmanIf2TcPwrCntlMode": WmanIf2TcPwrCntlMode,
       "WmanIf2TcCellType": WmanIf2TcCellType,
       "WmanIf2TcCidDescriptor": WmanIf2TcCidDescriptor,
       "WmanIf2TcActionRule": WmanIf2TcActionRule,
       "WmanIf2TcIpTypOfServ": WmanIf2TcIpTypOfServ,
       "WmanIf2TcClassifierMap": WmanIf2TcClassifierMap,
       "WmanIf2TcEthernetType": WmanIf2TcEthernetType,
       "wmanIf2TcMib": wmanIf2TcMib}
)
