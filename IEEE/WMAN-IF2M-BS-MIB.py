# SNMP MIB module (WMAN-IF2M-BS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-IF2M-BS-MIB.mib
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

wmanIf2mBsMib = ModuleIdentity(
    (1, 0, 8802, 16, 3)
)
if mibBuilder.loadTexts:
    wmanIf2mBsMib.setRevisions(
        ("2008-02-11 00:00",
         "2007-11-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class WmanIf2mOfdmaMobility(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("handoverSupport", 0),
          ("sleepModeSupport", 1),
          ("idleModeSupport", 2))
    )


class WmanIf2mHandoverType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("mdhcFbssHoNotSpported", 0),
          ("mdhcFbssDlMapsFromActiveBss", 1),
          ("mdhcDlMapFromAnchorBs", 2),
          ("mdhcDlMapsFromActiveBss", 3),
          ("mdhcUlMultipleTx", 4))
    )


class WmanIf2mCidType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class WmanIf2mPsClassId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class WmanIf2mPsClassType(TextualConvention, Integer32):
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
        *(("powerSavingClassTypeI", 1),
          ("powerSavingClassTypeII", 2),
          ("powerSavingClassTypeIII", 3))
    )



class WmanIf2mPsClassCidDir(TextualConvention, Integer32):
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
        *(("unspecified", 0),
          ("downlink", 1),
          ("uplink", 2))
    )



class WmanIf2mPowerSavingMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactionPs", 0),
          ("actionPs", 1))
    )



class WmanIf2mSkipOptBitMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("omitOperatorId", 0),
          ("omitNeighborBsId", 1),
          ("omitHoProcOptimization", 2),
          ("omitQosRelatedField", 3))
    )


class WmanIf2mNbrBsId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3



class WmanIf2mNbrOperatorId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3



class WmanIf2mPhyProfileId(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("colocatedFaInd", 0),
          ("faConfigInd", 1),
          ("timeFreqSyncInd1", 2),
          ("timeFreqSyncInd2", 3),
          ("bsEirpInd", 4),
          ("dcdUcdRefInd", 5),
          ("faIndexInd", 6),
          ("triggRefInd", 7))
    )


class WmanIf2mHoProcOptm(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("omitSbcReq", 0),
          ("omitPkmAuth", 1),
          ("omitPkmTek", 2),
          ("omitRegReq", 3),
          ("omitNtwkAddrAcq", 4),
          ("omitTimeOfDay", 5),
          ("omitTftp", 6),
          ("fullService", 7))
    )


class WmanIf2mSchedulingSupp(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ugs", 0),
          ("rtPs", 1),
          ("nrtPs", 2),
          ("be", 3),
          ("ertPs", 4))
    )


class WmanIf2mMacVersion(TextualConvention, Integer32):
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
          ("ieee802Dot16Of2008", 8))
    )



class WmanIf2mHarqAckDelay(TextualConvention, Integer32):
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



class WmanIf2mPowerSaveType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("psClassTypeI", 0),
          ("psClassTypeII", 1),
          ("psClassTypeIII", 2))
    )


class WmanIf2mHoTrigMatrix(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bsCinrMean", 0),
          ("bsRssiMean", 1),
          ("relativeDelay", 2),
          ("bsRoundTripDelay", 3))
    )


class WmanIf2mAssociationTyp(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("scanWoAssociation", 0),
          ("scanOrAssocWoCoordination", 1),
          ("assocWithCoordination", 2),
          ("ntwkAssistAssociation", 3),
          ("directAssociation", 4))
    )


class WmanIf2mOfdmaFftSize(TextualConvention, Integer32):
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
        *(("fft2048", 0),
          ("fft1024", 1),
          ("fft512", 2),
          ("fft128", 3))
    )



class WmanIf2mOfdmaCp(TextualConvention, Integer32):
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



class WmanIf2mOfdmaFrame(TextualConvention, Integer32):
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



class WmanIf2mPagingAction(TextualConvention, Integer32):
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
        *(("noAction", 0),
          ("performRanging", 1),
          ("enterNetwork", 2))
    )



class WmanIf2mSsMacAddrHash(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3



class WmanIf2mSfState(TextualConvention, Integer32):
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



class WmanIf2mGlobalSrvClass(TextualConvention, Bits):
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


class WmanIf2mSfDirection(TextualConvention, Integer32):
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



class WmanIf2mReqTxPolicy(TextualConvention, Bits):
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


class WmanIf2mPhsRuleVerify(TextualConvention, Integer32):
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



class WmanIf2mSchedulingType(TextualConvention, Integer32):
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



class WmanIf2mCsSpecification(TextualConvention, Integer32):
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
        *(("reserved", 0),
          ("packetIpV4", 1),
          ("packetIpV6", 2),
          ("packet802dot3Ethernet", 3),
          ("reserved4", 4),
          ("packetIpV4Over802dot3", 5),
          ("packetIpV6Over802dot3", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("atm", 9),
          ("packet802dot3EthernetRohcHc", 10),
          ("packet802dot3EthernetEcrtpHc", 11),
          ("packetIpRohcHc", 12),
          ("packetIpEcrtpHc", 13),
          ("packetIp", 14))
    )



class WmanIf2mIpv6FlowLabel(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3



class WmanIf2mClassifierBitMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("priority", 0),
          ("ipTos", 1),
          ("ipProtocol", 2),
          ("ipMaskedSrcAddr", 3),
          ("ipMaskedDestAddr", 4),
          ("srcPort", 5),
          ("destPort", 6),
          ("destMacAddr", 7),
          ("srcMacAddr", 8),
          ("ethernetProtocol", 9),
          ("userPriority", 10),
          ("vlanId", 11),
          ("ipv6FlowLabel", 12))
    )


class WmanIf2mReportMode(TextualConvention, Integer32):
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
        *(("noReport", 0),
          ("periodicReport", 1),
          ("eventTriggeredReport", 2))
    )



class WmanIf2mReportMatric(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bsCinrMean", 0),
          ("bsRssiMean", 1),
          ("relativeDelay", 2),
          ("bsRtd", 3))
    )


class WmanIf2mFullBsId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class WmanIf2mScanType(TextualConvention, Integer32):
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
        *(("scanWoAssociation", 0),
          ("scanWithAssociation0", 1),
          ("scanWithAssociation1", 2),
          ("scanWithAssociation2", 3))
    )



class WmanIf2mBsSsCapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("xxxReq", 1),
          ("xxxRsp", 2))
    )



class WmanIf2mBsCapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inheritedBsCap", 1),
          ("configedBsCap", 2))
    )



class WmanIf2mTrafficWkFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psNotBeDeactivated", 1),
          ("psBeDeactivated", 2))
    )



# MIB Managed Objects in the order of their OIDs

_WmanIf2mBsCm_ObjectIdentity = ObjectIdentity
wmanIf2mBsCm = _WmanIf2mBsCm_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1)
)
_WmanIf2mBsConfiguration_ObjectIdentity = ObjectIdentity
wmanIf2mBsConfiguration = _WmanIf2mBsConfiguration_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1, 1)
)
_WmanIf2mBsConfigurationTable_Object = MibTable
wmanIf2mBsConfigurationTable = _WmanIf2mBsConfigurationTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIf2mBsConfigurationTable.setStatus("current")
_WmanIf2mBsConfigurationEntry_Object = MibTableRow
wmanIf2mBsConfigurationEntry = _WmanIf2mBsConfigurationEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1)
)
wmanIf2mBsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsConfigurationEntry.setStatus("current")


class _WmanIf2mBsMobNbrAdvInterval_Type(Integer32):
    """Custom type wmanIf2mBsMobNbrAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WmanIf2mBsMobNbrAdvInterval_Type.__name__ = "Integer32"
_WmanIf2mBsMobNbrAdvInterval_Object = MibTableColumn
wmanIf2mBsMobNbrAdvInterval = _WmanIf2mBsMobNbrAdvInterval_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 1),
    _WmanIf2mBsMobNbrAdvInterval_Type()
)
wmanIf2mBsMobNbrAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsMobNbrAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsMobNbrAdvInterval.setUnits("seconds")


class _WmanIf2mBsAscAgingTimer_Type(Integer32):
    """Custom type wmanIf2mBsAscAgingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_WmanIf2mBsAscAgingTimer_Type.__name__ = "Integer32"
_WmanIf2mBsAscAgingTimer_Object = MibTableColumn
wmanIf2mBsAscAgingTimer = _WmanIf2mBsAscAgingTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 2),
    _WmanIf2mBsAscAgingTimer_Type()
)
wmanIf2mBsAscAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsAscAgingTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsAscAgingTimer.setUnits("milliseconds")


class _WmanIf2mBsPagingRetryCount_Type(Integer32):
    """Custom type wmanIf2mBsPagingRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WmanIf2mBsPagingRetryCount_Type.__name__ = "Integer32"
_WmanIf2mBsPagingRetryCount_Object = MibTableColumn
wmanIf2mBsPagingRetryCount = _WmanIf2mBsPagingRetryCount_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3),
    _WmanIf2mBsPagingRetryCount_Type()
)
wmanIf2mBsPagingRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingRetryCount.setStatus("current")


class _WmanIf2mBsModeSelectFeedbackProcTime_Type(Integer32):
    """Custom type wmanIf2mBsModeSelectFeedbackProcTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsModeSelectFeedbackProcTime_Type.__name__ = "Integer32"
_WmanIf2mBsModeSelectFeedbackProcTime_Object = MibTableColumn
wmanIf2mBsModeSelectFeedbackProcTime = _WmanIf2mBsModeSelectFeedbackProcTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4),
    _WmanIf2mBsModeSelectFeedbackProcTime_Type()
)
wmanIf2mBsModeSelectFeedbackProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsModeSelectFeedbackProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsModeSelectFeedbackProcTime.setUnits("microseconds")


class _WmanIf2mBsIdleModeSystemTimer_Type(Unsigned32):
    """Custom type wmanIf2mBsIdleModeSystemTimer based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 65536),
    )


_WmanIf2mBsIdleModeSystemTimer_Type.__name__ = "Unsigned32"
_WmanIf2mBsIdleModeSystemTimer_Object = MibTableColumn
wmanIf2mBsIdleModeSystemTimer = _WmanIf2mBsIdleModeSystemTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 5),
    _WmanIf2mBsIdleModeSystemTimer_Type()
)
wmanIf2mBsIdleModeSystemTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsIdleModeSystemTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsIdleModeSystemTimer.setUnits("seconds")


class _WmanIf2mBsMgmtResourceHoldingTimer_Type(Integer32):
    """Custom type wmanIf2mBsMgmtResourceHoldingTimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WmanIf2mBsMgmtResourceHoldingTimer_Type.__name__ = "Integer32"
_WmanIf2mBsMgmtResourceHoldingTimer_Object = MibTableColumn
wmanIf2mBsMgmtResourceHoldingTimer = _WmanIf2mBsMgmtResourceHoldingTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 6),
    _WmanIf2mBsMgmtResourceHoldingTimer_Type()
)
wmanIf2mBsMgmtResourceHoldingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsMgmtResourceHoldingTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsMgmtResourceHoldingTimer.setUnits("milliseconds")


class _WmanIf2mBsDregCommandRetryCount_Type(Integer32):
    """Custom type wmanIf2mBsDregCommandRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_WmanIf2mBsDregCommandRetryCount_Type.__name__ = "Integer32"
_WmanIf2mBsDregCommandRetryCount_Object = MibTableColumn
wmanIf2mBsDregCommandRetryCount = _WmanIf2mBsDregCommandRetryCount_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 7),
    _WmanIf2mBsDregCommandRetryCount_Type()
)
wmanIf2mBsDregCommandRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsDregCommandRetryCount.setStatus("current")


class _WmanIf2mBsT46Timer_Type(Integer32):
    """Custom type wmanIf2mBsT46Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsT46Timer_Type.__name__ = "Integer32"
_WmanIf2mBsT46Timer_Object = MibTableColumn
wmanIf2mBsT46Timer = _WmanIf2mBsT46Timer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 8),
    _WmanIf2mBsT46Timer_Type()
)
wmanIf2mBsT46Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsT46Timer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsT46Timer.setUnits("milliseconds")


class _WmanIf2mBsT47Timer_Type(Integer32):
    """Custom type wmanIf2mBsT47Timer based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1024),
    )


_WmanIf2mBsT47Timer_Type.__name__ = "Integer32"
_WmanIf2mBsT47Timer_Object = MibTableColumn
wmanIf2mBsT47Timer = _WmanIf2mBsT47Timer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 9),
    _WmanIf2mBsT47Timer_Type()
)
wmanIf2mBsT47Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsT47Timer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsT47Timer.setUnits("frames")


class _WmanIf2mBsPagingInterval_Type(Integer32):
    """Custom type wmanIf2mBsPagingInterval based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1024),
    )


_WmanIf2mBsPagingInterval_Type.__name__ = "Integer32"
_WmanIf2mBsPagingInterval_Object = MibTableColumn
wmanIf2mBsPagingInterval = _WmanIf2mBsPagingInterval_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 10),
    _WmanIf2mBsPagingInterval_Type()
)
wmanIf2mBsPagingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingInterval.setUnits("frames")


class _WmanIf2mBs2ndMgmtDlQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBs2ndMgmtDlQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBs2ndMgmtDlQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBs2ndMgmtDlQoSProfileIndex_Object = MibTableColumn
wmanIf2mBs2ndMgmtDlQoSProfileIndex = _WmanIf2mBs2ndMgmtDlQoSProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 11),
    _WmanIf2mBs2ndMgmtDlQoSProfileIndex_Type()
)
wmanIf2mBs2ndMgmtDlQoSProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBs2ndMgmtDlQoSProfileIndex.setStatus("current")


class _WmanIf2mBs2ndMgmtUlQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBs2ndMgmtUlQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBs2ndMgmtUlQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBs2ndMgmtUlQoSProfileIndex_Object = MibTableColumn
wmanIf2mBs2ndMgmtUlQoSProfileIndex = _WmanIf2mBs2ndMgmtUlQoSProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 12),
    _WmanIf2mBs2ndMgmtUlQoSProfileIndex_Type()
)
wmanIf2mBs2ndMgmtUlQoSProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBs2ndMgmtUlQoSProfileIndex.setStatus("current")


class _WmanIf2mBsBasicCidDlQosProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBsBasicCidDlQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsBasicCidDlQosProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBsBasicCidDlQosProfileIndex_Object = MibTableColumn
wmanIf2mBsBasicCidDlQosProfileIndex = _WmanIf2mBsBasicCidDlQosProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 13),
    _WmanIf2mBsBasicCidDlQosProfileIndex_Type()
)
wmanIf2mBsBasicCidDlQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsBasicCidDlQosProfileIndex.setStatus("current")


class _WmanIf2mBsBasicCidUlQosProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBsBasicCidUlQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsBasicCidUlQosProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBsBasicCidUlQosProfileIndex_Object = MibTableColumn
wmanIf2mBsBasicCidUlQosProfileIndex = _WmanIf2mBsBasicCidUlQosProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 14),
    _WmanIf2mBsBasicCidUlQosProfileIndex_Type()
)
wmanIf2mBsBasicCidUlQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsBasicCidUlQosProfileIndex.setStatus("current")


class _WmanIf2mBsPrimaryCidDlQosProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBsPrimaryCidDlQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsPrimaryCidDlQosProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBsPrimaryCidDlQosProfileIndex_Object = MibTableColumn
wmanIf2mBsPrimaryCidDlQosProfileIndex = _WmanIf2mBsPrimaryCidDlQosProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 15),
    _WmanIf2mBsPrimaryCidDlQosProfileIndex_Type()
)
wmanIf2mBsPrimaryCidDlQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsPrimaryCidDlQosProfileIndex.setStatus("current")


class _WmanIf2mBsPrimaryCidUlQosProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBsPrimaryCidUlQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsPrimaryCidUlQosProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBsPrimaryCidUlQosProfileIndex_Object = MibTableColumn
wmanIf2mBsPrimaryCidUlQosProfileIndex = _WmanIf2mBsPrimaryCidUlQosProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 16),
    _WmanIf2mBsPrimaryCidUlQosProfileIndex_Type()
)
wmanIf2mBsPrimaryCidUlQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsPrimaryCidUlQosProfileIndex.setStatus("current")
_WmanIf2mBsSsReqCapabilitiesTable_Object = MibTable
wmanIf2mBsSsReqCapabilitiesTable = _WmanIf2mBsSsReqCapabilitiesTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapabilitiesTable.setStatus("current")
_WmanIf2mBsSsReqCapabilitiesEntry_Object = MibTableRow
wmanIf2mBsSsReqCapabilitiesEntry = _WmanIf2mBsSsReqCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1)
)
wmanIf2mBsSsReqCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapabilitiesEntry.setStatus("current")
_WmanIf2mBsSsReqCapHandoverSupported_Type = WmanIf2mHandoverType
_WmanIf2mBsSsReqCapHandoverSupported_Object = MibTableColumn
wmanIf2mBsSsReqCapHandoverSupported = _WmanIf2mBsSsReqCapHandoverSupported_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 1),
    _WmanIf2mBsSsReqCapHandoverSupported_Type()
)
wmanIf2mBsSsReqCapHandoverSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapHandoverSupported.setStatus("current")
_WmanIf2mBsSsReqCapHoProcessTimer_Type = Unsigned32
_WmanIf2mBsSsReqCapHoProcessTimer_Object = MibTableColumn
wmanIf2mBsSsReqCapHoProcessTimer = _WmanIf2mBsSsReqCapHoProcessTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 2),
    _WmanIf2mBsSsReqCapHoProcessTimer_Type()
)
wmanIf2mBsSsReqCapHoProcessTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapHoProcessTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapHoProcessTimer.setUnits("frames")
_WmanIf2mBsSsReqCapMobilityFeature_Type = WmanIf2mOfdmaMobility
_WmanIf2mBsSsReqCapMobilityFeature_Object = MibTableColumn
wmanIf2mBsSsReqCapMobilityFeature = _WmanIf2mBsSsReqCapMobilityFeature_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 3),
    _WmanIf2mBsSsReqCapMobilityFeature_Type()
)
wmanIf2mBsSsReqCapMobilityFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapMobilityFeature.setStatus("current")
_WmanIf2mBsSsReqCapSleepRecoveryTime_Type = Unsigned32
_WmanIf2mBsSsReqCapSleepRecoveryTime_Object = MibTableColumn
wmanIf2mBsSsReqCapSleepRecoveryTime = _WmanIf2mBsSsReqCapSleepRecoveryTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 4),
    _WmanIf2mBsSsReqCapSleepRecoveryTime_Type()
)
wmanIf2mBsSsReqCapSleepRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapSleepRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapSleepRecoveryTime.setUnits("frames")
_WmanIf2mBsSsReqCapPreviousIpAddr_Type = OctetString
_WmanIf2mBsSsReqCapPreviousIpAddr_Object = MibTableColumn
wmanIf2mBsSsReqCapPreviousIpAddr = _WmanIf2mBsSsReqCapPreviousIpAddr_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 5),
    _WmanIf2mBsSsReqCapPreviousIpAddr_Type()
)
wmanIf2mBsSsReqCapPreviousIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapPreviousIpAddr.setStatus("current")
_WmanIf2mBsSsReqCapIdleModeTimeout_Type = Unsigned32
_WmanIf2mBsSsReqCapIdleModeTimeout_Object = MibTableColumn
wmanIf2mBsSsReqCapIdleModeTimeout = _WmanIf2mBsSsReqCapIdleModeTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 6),
    _WmanIf2mBsSsReqCapIdleModeTimeout_Type()
)
wmanIf2mBsSsReqCapIdleModeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapIdleModeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapIdleModeTimeout.setUnits("seconds")
_WmanIf2mBsSsReqCapHoConnProcessTime_Type = Unsigned32
_WmanIf2mBsSsReqCapHoConnProcessTime_Object = MibTableColumn
wmanIf2mBsSsReqCapHoConnProcessTime = _WmanIf2mBsSsReqCapHoConnProcessTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 7),
    _WmanIf2mBsSsReqCapHoConnProcessTime_Type()
)
wmanIf2mBsSsReqCapHoConnProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapHoConnProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapHoConnProcessTime.setUnits("milliseconds")
_WmanIf2mBsSsReqCapHoTekProcessTime_Type = Unsigned32
_WmanIf2mBsSsReqCapHoTekProcessTime_Object = MibTableColumn
wmanIf2mBsSsReqCapHoTekProcessTime = _WmanIf2mBsSsReqCapHoTekProcessTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 8),
    _WmanIf2mBsSsReqCapHoTekProcessTime_Type()
)
wmanIf2mBsSsReqCapHoTekProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapHoTekProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapHoTekProcessTime.setUnits("milliseconds")
_WmanIf2mBsSsReqCapPowerSavingType_Type = WmanIf2mPowerSaveType
_WmanIf2mBsSsReqCapPowerSavingType_Object = MibTableColumn
wmanIf2mBsSsReqCapPowerSavingType = _WmanIf2mBsSsReqCapPowerSavingType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 9),
    _WmanIf2mBsSsReqCapPowerSavingType_Type()
)
wmanIf2mBsSsReqCapPowerSavingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapPowerSavingType.setStatus("current")


class _WmanIf2mBsSsReqCapNumOfPsClassIandII_Type(Integer32):
    """Custom type wmanIf2mBsSsReqCapNumOfPsClassIandII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsSsReqCapNumOfPsClassIandII_Type.__name__ = "Integer32"
_WmanIf2mBsSsReqCapNumOfPsClassIandII_Object = MibTableColumn
wmanIf2mBsSsReqCapNumOfPsClassIandII = _WmanIf2mBsSsReqCapNumOfPsClassIandII_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 10),
    _WmanIf2mBsSsReqCapNumOfPsClassIandII_Type()
)
wmanIf2mBsSsReqCapNumOfPsClassIandII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapNumOfPsClassIandII.setStatus("current")


class _WmanIf2mBsSsReqCapNumOfPsClassIII_Type(Integer32):
    """Custom type wmanIf2mBsSsReqCapNumOfPsClassIII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsSsReqCapNumOfPsClassIII_Type.__name__ = "Integer32"
_WmanIf2mBsSsReqCapNumOfPsClassIII_Object = MibTableColumn
wmanIf2mBsSsReqCapNumOfPsClassIII = _WmanIf2mBsSsReqCapNumOfPsClassIII_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 11),
    _WmanIf2mBsSsReqCapNumOfPsClassIII_Type()
)
wmanIf2mBsSsReqCapNumOfPsClassIII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapNumOfPsClassIII.setStatus("current")
_WmanIf2mBsSsReqCapHoTrigMatrix_Type = WmanIf2mHoTrigMatrix
_WmanIf2mBsSsReqCapHoTrigMatrix_Object = MibTableColumn
wmanIf2mBsSsReqCapHoTrigMatrix = _WmanIf2mBsSsReqCapHoTrigMatrix_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 12),
    _WmanIf2mBsSsReqCapHoTrigMatrix_Type()
)
wmanIf2mBsSsReqCapHoTrigMatrix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapHoTrigMatrix.setStatus("current")
_WmanIf2mBsSsReqCapAssociationType_Type = WmanIf2mAssociationTyp
_WmanIf2mBsSsReqCapAssociationType_Object = MibTableColumn
wmanIf2mBsSsReqCapAssociationType = _WmanIf2mBsSsReqCapAssociationType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 2, 1, 13),
    _WmanIf2mBsSsReqCapAssociationType_Type()
)
wmanIf2mBsSsReqCapAssociationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsReqCapAssociationType.setStatus("current")
_WmanIf2mBsSsRspCapabilitiesTable_Object = MibTable
wmanIf2mBsSsRspCapabilitiesTable = _WmanIf2mBsSsRspCapabilitiesTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapabilitiesTable.setStatus("current")
_WmanIf2mBsSsRspCapabilitiesEntry_Object = MibTableRow
wmanIf2mBsSsRspCapabilitiesEntry = _WmanIf2mBsSsRspCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1)
)
wmanIf2mBsSsRspCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapabilitiesEntry.setStatus("current")
_WmanIf2mBsSsRspCapHandoverSupported_Type = WmanIf2mHandoverType
_WmanIf2mBsSsRspCapHandoverSupported_Object = MibTableColumn
wmanIf2mBsSsRspCapHandoverSupported = _WmanIf2mBsSsRspCapHandoverSupported_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 1),
    _WmanIf2mBsSsRspCapHandoverSupported_Type()
)
wmanIf2mBsSsRspCapHandoverSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapHandoverSupported.setStatus("current")
_WmanIf2mBsSsRspCapRetrainTime_Type = Unsigned32
_WmanIf2mBsSsRspCapRetrainTime_Object = MibTableColumn
wmanIf2mBsSsRspCapRetrainTime = _WmanIf2mBsSsRspCapRetrainTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 2),
    _WmanIf2mBsSsRspCapRetrainTime_Type()
)
wmanIf2mBsSsRspCapRetrainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapRetrainTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapRetrainTime.setUnits("100 milliseconds")
_WmanIf2mBsSsRspCapHoProcessTimer_Type = Unsigned32
_WmanIf2mBsSsRspCapHoProcessTimer_Object = MibTableColumn
wmanIf2mBsSsRspCapHoProcessTimer = _WmanIf2mBsSsRspCapHoProcessTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 3),
    _WmanIf2mBsSsRspCapHoProcessTimer_Type()
)
wmanIf2mBsSsRspCapHoProcessTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapHoProcessTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapHoProcessTimer.setUnits("frames")
_WmanIf2mBsSsRspCapRetransmissionTimer_Type = Unsigned32
_WmanIf2mBsSsRspCapRetransmissionTimer_Object = MibTableColumn
wmanIf2mBsSsRspCapRetransmissionTimer = _WmanIf2mBsSsRspCapRetransmissionTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 4),
    _WmanIf2mBsSsRspCapRetransmissionTimer_Type()
)
wmanIf2mBsSsRspCapRetransmissionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapRetransmissionTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapRetransmissionTimer.setUnits("frames")
_WmanIf2mBsSsRspCapMobilityFeature_Type = WmanIf2mOfdmaMobility
_WmanIf2mBsSsRspCapMobilityFeature_Object = MibTableColumn
wmanIf2mBsSsRspCapMobilityFeature = _WmanIf2mBsSsRspCapMobilityFeature_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 5),
    _WmanIf2mBsSsRspCapMobilityFeature_Type()
)
wmanIf2mBsSsRspCapMobilityFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapMobilityFeature.setStatus("current")
_WmanIf2mBsSsRspCapIdleModeTimeout_Type = Unsigned32
_WmanIf2mBsSsRspCapIdleModeTimeout_Object = MibTableColumn
wmanIf2mBsSsRspCapIdleModeTimeout = _WmanIf2mBsSsRspCapIdleModeTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 6),
    _WmanIf2mBsSsRspCapIdleModeTimeout_Type()
)
wmanIf2mBsSsRspCapIdleModeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapIdleModeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapIdleModeTimeout.setUnits("seconds")
_WmanIf2mBsSsRspCapHoConnProcessTime_Type = Unsigned32
_WmanIf2mBsSsRspCapHoConnProcessTime_Object = MibTableColumn
wmanIf2mBsSsRspCapHoConnProcessTime = _WmanIf2mBsSsRspCapHoConnProcessTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 7),
    _WmanIf2mBsSsRspCapHoConnProcessTime_Type()
)
wmanIf2mBsSsRspCapHoConnProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapHoConnProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapHoConnProcessTime.setUnits("milliseconds")
_WmanIf2mBsSsRspCapHoTekProcessTime_Type = Unsigned32
_WmanIf2mBsSsRspCapHoTekProcessTime_Object = MibTableColumn
wmanIf2mBsSsRspCapHoTekProcessTime = _WmanIf2mBsSsRspCapHoTekProcessTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 8),
    _WmanIf2mBsSsRspCapHoTekProcessTime_Type()
)
wmanIf2mBsSsRspCapHoTekProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapHoTekProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapHoTekProcessTime.setUnits("milliseconds")
_WmanIf2mBsSsRspCapPowerSavingType_Type = WmanIf2mPowerSaveType
_WmanIf2mBsSsRspCapPowerSavingType_Object = MibTableColumn
wmanIf2mBsSsRspCapPowerSavingType = _WmanIf2mBsSsRspCapPowerSavingType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 9),
    _WmanIf2mBsSsRspCapPowerSavingType_Type()
)
wmanIf2mBsSsRspCapPowerSavingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapPowerSavingType.setStatus("current")


class _WmanIf2mBsSsRspCapNumOfPsClassIandII_Type(Integer32):
    """Custom type wmanIf2mBsSsRspCapNumOfPsClassIandII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsSsRspCapNumOfPsClassIandII_Type.__name__ = "Integer32"
_WmanIf2mBsSsRspCapNumOfPsClassIandII_Object = MibTableColumn
wmanIf2mBsSsRspCapNumOfPsClassIandII = _WmanIf2mBsSsRspCapNumOfPsClassIandII_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 10),
    _WmanIf2mBsSsRspCapNumOfPsClassIandII_Type()
)
wmanIf2mBsSsRspCapNumOfPsClassIandII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapNumOfPsClassIandII.setStatus("current")


class _WmanIf2mBsSsRspCapNumOfPsClassIII_Type(Integer32):
    """Custom type wmanIf2mBsSsRspCapNumOfPsClassIII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsSsRspCapNumOfPsClassIII_Type.__name__ = "Integer32"
_WmanIf2mBsSsRspCapNumOfPsClassIII_Object = MibTableColumn
wmanIf2mBsSsRspCapNumOfPsClassIII = _WmanIf2mBsSsRspCapNumOfPsClassIII_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 11),
    _WmanIf2mBsSsRspCapNumOfPsClassIII_Type()
)
wmanIf2mBsSsRspCapNumOfPsClassIII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapNumOfPsClassIII.setStatus("current")
_WmanIf2mBsSsRspCapHoTrigMatrix_Type = WmanIf2mHoTrigMatrix
_WmanIf2mBsSsRspCapHoTrigMatrix_Object = MibTableColumn
wmanIf2mBsSsRspCapHoTrigMatrix = _WmanIf2mBsSsRspCapHoTrigMatrix_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 12),
    _WmanIf2mBsSsRspCapHoTrigMatrix_Type()
)
wmanIf2mBsSsRspCapHoTrigMatrix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapHoTrigMatrix.setStatus("current")
_WmanIf2mBsSsRspCapAssociationType_Type = WmanIf2mAssociationTyp
_WmanIf2mBsSsRspCapAssociationType_Object = MibTableColumn
wmanIf2mBsSsRspCapAssociationType = _WmanIf2mBsSsRspCapAssociationType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 3, 1, 13),
    _WmanIf2mBsSsRspCapAssociationType_Type()
)
wmanIf2mBsSsRspCapAssociationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsRspCapAssociationType.setStatus("current")
_WmanIf2mBsBasicCapabilitiesTable_Object = MibTable
wmanIf2mBsBasicCapabilitiesTable = _WmanIf2mBsBasicCapabilitiesTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wmanIf2mBsBasicCapabilitiesTable.setStatus("current")
_WmanIf2mBsBasicCapabilitiesEntry_Object = MibTableRow
wmanIf2mBsBasicCapabilitiesEntry = _WmanIf2mBsBasicCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1)
)
wmanIf2mBsBasicCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsBasicCapabilitiesEntry.setStatus("current")
_WmanIf2mBsCapHandoverSupported_Type = WmanIf2mHandoverType
_WmanIf2mBsCapHandoverSupported_Object = MibTableColumn
wmanIf2mBsCapHandoverSupported = _WmanIf2mBsCapHandoverSupported_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 1),
    _WmanIf2mBsCapHandoverSupported_Type()
)
wmanIf2mBsCapHandoverSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHandoverSupported.setStatus("current")
_WmanIf2mBsCapRetrainTime_Type = Unsigned32
_WmanIf2mBsCapRetrainTime_Object = MibTableColumn
wmanIf2mBsCapRetrainTime = _WmanIf2mBsCapRetrainTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 2),
    _WmanIf2mBsCapRetrainTime_Type()
)
wmanIf2mBsCapRetrainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapRetrainTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapRetrainTime.setUnits("100 milliseconds")
_WmanIf2mBsCapHoProcessTimer_Type = Unsigned32
_WmanIf2mBsCapHoProcessTimer_Object = MibTableColumn
wmanIf2mBsCapHoProcessTimer = _WmanIf2mBsCapHoProcessTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 3),
    _WmanIf2mBsCapHoProcessTimer_Type()
)
wmanIf2mBsCapHoProcessTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHoProcessTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHoProcessTimer.setUnits("frames")
_WmanIf2mBsCapRetransmissionTimer_Type = Unsigned32
_WmanIf2mBsCapRetransmissionTimer_Object = MibTableColumn
wmanIf2mBsCapRetransmissionTimer = _WmanIf2mBsCapRetransmissionTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 4),
    _WmanIf2mBsCapRetransmissionTimer_Type()
)
wmanIf2mBsCapRetransmissionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapRetransmissionTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapRetransmissionTimer.setUnits("frames")
_WmanIf2mBsCapMobilityFeature_Type = WmanIf2mOfdmaMobility
_WmanIf2mBsCapMobilityFeature_Object = MibTableColumn
wmanIf2mBsCapMobilityFeature = _WmanIf2mBsCapMobilityFeature_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 5),
    _WmanIf2mBsCapMobilityFeature_Type()
)
wmanIf2mBsCapMobilityFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapMobilityFeature.setStatus("current")
_WmanIf2mBsCapIdleModeTimeout_Type = Unsigned32
_WmanIf2mBsCapIdleModeTimeout_Object = MibTableColumn
wmanIf2mBsCapIdleModeTimeout = _WmanIf2mBsCapIdleModeTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 6),
    _WmanIf2mBsCapIdleModeTimeout_Type()
)
wmanIf2mBsCapIdleModeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapIdleModeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapIdleModeTimeout.setUnits("seconds")
_WmanIf2mBsCapHoConnProcessTime_Type = Unsigned32
_WmanIf2mBsCapHoConnProcessTime_Object = MibTableColumn
wmanIf2mBsCapHoConnProcessTime = _WmanIf2mBsCapHoConnProcessTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 7),
    _WmanIf2mBsCapHoConnProcessTime_Type()
)
wmanIf2mBsCapHoConnProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHoConnProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHoConnProcessTime.setUnits("milliseconds")
_WmanIf2mBsCapHoTekProcessTime_Type = Unsigned32
_WmanIf2mBsCapHoTekProcessTime_Object = MibTableColumn
wmanIf2mBsCapHoTekProcessTime = _WmanIf2mBsCapHoTekProcessTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 8),
    _WmanIf2mBsCapHoTekProcessTime_Type()
)
wmanIf2mBsCapHoTekProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHoTekProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHoTekProcessTime.setUnits("milliseconds")
_WmanIf2mBsCapPowerSavingType_Type = WmanIf2mPowerSaveType
_WmanIf2mBsCapPowerSavingType_Object = MibTableColumn
wmanIf2mBsCapPowerSavingType = _WmanIf2mBsCapPowerSavingType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 9),
    _WmanIf2mBsCapPowerSavingType_Type()
)
wmanIf2mBsCapPowerSavingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapPowerSavingType.setStatus("current")


class _WmanIf2mBsCapNumOfPsClassIandII_Type(Integer32):
    """Custom type wmanIf2mBsCapNumOfPsClassIandII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsCapNumOfPsClassIandII_Type.__name__ = "Integer32"
_WmanIf2mBsCapNumOfPsClassIandII_Object = MibTableColumn
wmanIf2mBsCapNumOfPsClassIandII = _WmanIf2mBsCapNumOfPsClassIandII_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 10),
    _WmanIf2mBsCapNumOfPsClassIandII_Type()
)
wmanIf2mBsCapNumOfPsClassIandII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapNumOfPsClassIandII.setStatus("current")


class _WmanIf2mBsCapNumOfPsClassIII_Type(Integer32):
    """Custom type wmanIf2mBsCapNumOfPsClassIII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsCapNumOfPsClassIII_Type.__name__ = "Integer32"
_WmanIf2mBsCapNumOfPsClassIII_Object = MibTableColumn
wmanIf2mBsCapNumOfPsClassIII = _WmanIf2mBsCapNumOfPsClassIII_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 11),
    _WmanIf2mBsCapNumOfPsClassIII_Type()
)
wmanIf2mBsCapNumOfPsClassIII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapNumOfPsClassIII.setStatus("current")
_WmanIf2mBsCapHoTrigMatrix_Type = WmanIf2mHoTrigMatrix
_WmanIf2mBsCapHoTrigMatrix_Object = MibTableColumn
wmanIf2mBsCapHoTrigMatrix = _WmanIf2mBsCapHoTrigMatrix_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 12),
    _WmanIf2mBsCapHoTrigMatrix_Type()
)
wmanIf2mBsCapHoTrigMatrix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHoTrigMatrix.setStatus("current")
_WmanIf2mBsCapAssociationType_Type = WmanIf2mAssociationTyp
_WmanIf2mBsCapAssociationType_Object = MibTableColumn
wmanIf2mBsCapAssociationType = _WmanIf2mBsCapAssociationType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 4, 1, 13),
    _WmanIf2mBsCapAssociationType_Type()
)
wmanIf2mBsCapAssociationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapAssociationType.setStatus("current")
_WmanIf2mBsCapabilitiesConfigTable_Object = MibTable
wmanIf2mBsCapabilitiesConfigTable = _WmanIf2mBsCapabilitiesConfigTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wmanIf2mBsCapabilitiesConfigTable.setStatus("current")
_WmanIf2mBsCapabilitiesConfigEntry_Object = MibTableRow
wmanIf2mBsCapabilitiesConfigEntry = _WmanIf2mBsCapabilitiesConfigEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1)
)
wmanIf2mBsCapabilitiesConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsCapabilitiesConfigEntry.setStatus("current")
_WmanIf2mBsCapCfgHandoverSupported_Type = WmanIf2mHandoverType
_WmanIf2mBsCapCfgHandoverSupported_Object = MibTableColumn
wmanIf2mBsCapCfgHandoverSupported = _WmanIf2mBsCapCfgHandoverSupported_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 1),
    _WmanIf2mBsCapCfgHandoverSupported_Type()
)
wmanIf2mBsCapCfgHandoverSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHandoverSupported.setStatus("current")


class _WmanIf2mBsCapCfgRetrainTime_Type(Unsigned32):
    """Custom type wmanIf2mBsCapCfgRetrainTime based on Unsigned32"""
    defaultValue = 1


_WmanIf2mBsCapCfgRetrainTime_Type.__name__ = "Unsigned32"
_WmanIf2mBsCapCfgRetrainTime_Object = MibTableColumn
wmanIf2mBsCapCfgRetrainTime = _WmanIf2mBsCapCfgRetrainTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 2),
    _WmanIf2mBsCapCfgRetrainTime_Type()
)
wmanIf2mBsCapCfgRetrainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgRetrainTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgRetrainTime.setUnits("100 milliseconds")
_WmanIf2mBsCapCfgHoProcessTimer_Type = Unsigned32
_WmanIf2mBsCapCfgHoProcessTimer_Object = MibTableColumn
wmanIf2mBsCapCfgHoProcessTimer = _WmanIf2mBsCapCfgHoProcessTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 3),
    _WmanIf2mBsCapCfgHoProcessTimer_Type()
)
wmanIf2mBsCapCfgHoProcessTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoProcessTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoProcessTimer.setUnits("frames")
_WmanIf2mBsCapCfgRetransmissionTimer_Type = Unsigned32
_WmanIf2mBsCapCfgRetransmissionTimer_Object = MibTableColumn
wmanIf2mBsCapCfgRetransmissionTimer = _WmanIf2mBsCapCfgRetransmissionTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 4),
    _WmanIf2mBsCapCfgRetransmissionTimer_Type()
)
wmanIf2mBsCapCfgRetransmissionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgRetransmissionTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgRetransmissionTimer.setUnits("frames")
_WmanIf2mBsCapCfgMobilityFeature_Type = WmanIf2mOfdmaMobility
_WmanIf2mBsCapCfgMobilityFeature_Object = MibTableColumn
wmanIf2mBsCapCfgMobilityFeature = _WmanIf2mBsCapCfgMobilityFeature_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 5),
    _WmanIf2mBsCapCfgMobilityFeature_Type()
)
wmanIf2mBsCapCfgMobilityFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgMobilityFeature.setStatus("current")


class _WmanIf2mBsCapCfgIdleModeTimeout_Type(Unsigned32):
    """Custom type wmanIf2mBsCapCfgIdleModeTimeout based on Unsigned32"""
    defaultValue = 4096


_WmanIf2mBsCapCfgIdleModeTimeout_Type.__name__ = "Unsigned32"
_WmanIf2mBsCapCfgIdleModeTimeout_Object = MibTableColumn
wmanIf2mBsCapCfgIdleModeTimeout = _WmanIf2mBsCapCfgIdleModeTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 6),
    _WmanIf2mBsCapCfgIdleModeTimeout_Type()
)
wmanIf2mBsCapCfgIdleModeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgIdleModeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgIdleModeTimeout.setUnits("seconds")
_WmanIf2mBsCapCfgHoConnProcessTime_Type = Unsigned32
_WmanIf2mBsCapCfgHoConnProcessTime_Object = MibTableColumn
wmanIf2mBsCapCfgHoConnProcessTime = _WmanIf2mBsCapCfgHoConnProcessTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 7),
    _WmanIf2mBsCapCfgHoConnProcessTime_Type()
)
wmanIf2mBsCapCfgHoConnProcessTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoConnProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoConnProcessTime.setUnits("milliseconds")
_WmanIf2mBsCapCfgHoTekProcessTime_Type = Unsigned32
_WmanIf2mBsCapCfgHoTekProcessTime_Object = MibTableColumn
wmanIf2mBsCapCfgHoTekProcessTime = _WmanIf2mBsCapCfgHoTekProcessTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 8),
    _WmanIf2mBsCapCfgHoTekProcessTime_Type()
)
wmanIf2mBsCapCfgHoTekProcessTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoTekProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoTekProcessTime.setUnits("milliseconds")
_WmanIf2mBsCapCfgPowerSavingType_Type = WmanIf2mPowerSaveType
_WmanIf2mBsCapCfgPowerSavingType_Object = MibTableColumn
wmanIf2mBsCapCfgPowerSavingType = _WmanIf2mBsCapCfgPowerSavingType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 9),
    _WmanIf2mBsCapCfgPowerSavingType_Type()
)
wmanIf2mBsCapCfgPowerSavingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgPowerSavingType.setStatus("current")


class _WmanIf2mBsCapCfgNumOfPsClassIandII_Type(Integer32):
    """Custom type wmanIf2mBsCapCfgNumOfPsClassIandII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsCapCfgNumOfPsClassIandII_Type.__name__ = "Integer32"
_WmanIf2mBsCapCfgNumOfPsClassIandII_Object = MibTableColumn
wmanIf2mBsCapCfgNumOfPsClassIandII = _WmanIf2mBsCapCfgNumOfPsClassIandII_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 10),
    _WmanIf2mBsCapCfgNumOfPsClassIandII_Type()
)
wmanIf2mBsCapCfgNumOfPsClassIandII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgNumOfPsClassIandII.setStatus("current")


class _WmanIf2mBsCapCfgNumOfPsClassIII_Type(Integer32):
    """Custom type wmanIf2mBsCapCfgNumOfPsClassIII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsCapCfgNumOfPsClassIII_Type.__name__ = "Integer32"
_WmanIf2mBsCapCfgNumOfPsClassIII_Object = MibTableColumn
wmanIf2mBsCapCfgNumOfPsClassIII = _WmanIf2mBsCapCfgNumOfPsClassIII_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 11),
    _WmanIf2mBsCapCfgNumOfPsClassIII_Type()
)
wmanIf2mBsCapCfgNumOfPsClassIII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgNumOfPsClassIII.setStatus("current")
_WmanIf2mBsCapCfgHoTrigMatrix_Type = WmanIf2mHoTrigMatrix
_WmanIf2mBsCapCfgHoTrigMatrix_Object = MibTableColumn
wmanIf2mBsCapCfgHoTrigMatrix = _WmanIf2mBsCapCfgHoTrigMatrix_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 12),
    _WmanIf2mBsCapCfgHoTrigMatrix_Type()
)
wmanIf2mBsCapCfgHoTrigMatrix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoTrigMatrix.setStatus("current")
_WmanIf2mBsCapCfgAssociationType_Type = WmanIf2mAssociationTyp
_WmanIf2mBsCapCfgAssociationType_Object = MibTableColumn
wmanIf2mBsCapCfgAssociationType = _WmanIf2mBsCapCfgAssociationType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 5, 1, 13),
    _WmanIf2mBsCapCfgAssociationType_Type()
)
wmanIf2mBsCapCfgAssociationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgAssociationType.setStatus("current")
_WmanIf2mBsSsCidUpdateTable_Object = MibTable
wmanIf2mBsSsCidUpdateTable = _WmanIf2mBsSsCidUpdateTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsCidUpdateTable.setStatus("current")
_WmanIf2mBsSsCidUpdateEntry_Object = MibTableRow
wmanIf2mBsSsCidUpdateEntry = _WmanIf2mBsSsCidUpdateEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 6, 1)
)
wmanIf2mBsSsCidUpdateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsSfId"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsCidUpdateEntry.setStatus("current")


class _WmanIf2mBsSsSfId_Type(Unsigned32):
    """Custom type wmanIf2mBsSsSfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2mBsSsSfId_Type.__name__ = "Unsigned32"
_WmanIf2mBsSsSfId_Object = MibTableColumn
wmanIf2mBsSsSfId = _WmanIf2mBsSsSfId_Object(
    (1, 0, 8802, 16, 3, 1, 1, 6, 1, 1),
    _WmanIf2mBsSsSfId_Type()
)
wmanIf2mBsSsSfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsSsSfId.setStatus("current")
_WmanIf2mBsSsNewCid_Type = WmanIf2mCidType
_WmanIf2mBsSsNewCid_Object = MibTableColumn
wmanIf2mBsSsNewCid = _WmanIf2mBsSsNewCid_Object(
    (1, 0, 8802, 16, 3, 1, 1, 6, 1, 2),
    _WmanIf2mBsSsNewCid_Type()
)
wmanIf2mBsSsNewCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsNewCid.setStatus("current")


class _WmanIf2mBsSsNewSaid_Type(Integer32):
    """Custom type wmanIf2mBsSsNewSaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsSsNewSaid_Type.__name__ = "Integer32"
_WmanIf2mBsSsNewSaid_Object = MibTableColumn
wmanIf2mBsSsNewSaid = _WmanIf2mBsSsNewSaid_Object(
    (1, 0, 8802, 16, 3, 1, 1, 6, 1, 3),
    _WmanIf2mBsSsNewSaid_Type()
)
wmanIf2mBsSsNewSaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsNewSaid.setStatus("current")


class _WmanIf2mBsSsOldSaid_Type(Integer32):
    """Custom type wmanIf2mBsSsOldSaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsSsOldSaid_Type.__name__ = "Integer32"
_WmanIf2mBsSsOldSaid_Object = MibTableColumn
wmanIf2mBsSsOldSaid = _WmanIf2mBsSsOldSaid_Object(
    (1, 0, 8802, 16, 3, 1, 1, 6, 1, 4),
    _WmanIf2mBsSsOldSaid_Type()
)
wmanIf2mBsSsOldSaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsOldSaid.setStatus("current")
_WmanIf2mBsPowerSavingMode_ObjectIdentity = ObjectIdentity
wmanIf2mBsPowerSavingMode = _WmanIf2mBsPowerSavingMode_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1, 2)
)
_WmanIf2mBsSsPwrSaving2CidMapTable_Object = MibTable
wmanIf2mBsSsPwrSaving2CidMapTable = _WmanIf2mBsSsPwrSaving2CidMapTable_Object(
    (1, 0, 8802, 16, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsPwrSaving2CidMapTable.setStatus("current")
_WmanIf2mBsSsPwrSaving2CidMapEntry_Object = MibTableRow
wmanIf2mBsSsPwrSaving2CidMapEntry = _WmanIf2mBsSsPwrSaving2CidMapEntry_Object(
    (1, 0, 8802, 16, 3, 1, 2, 1, 1)
)
wmanIf2mBsSsPwrSaving2CidMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsCid"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsPwrSaving2CidMapEntry.setStatus("current")
_WmanIf2mBsSsCid_Type = WmanIf2mCidType
_WmanIf2mBsSsCid_Object = MibTableColumn
wmanIf2mBsSsCid = _WmanIf2mBsSsCid_Object(
    (1, 0, 8802, 16, 3, 1, 2, 1, 1, 1),
    _WmanIf2mBsSsCid_Type()
)
wmanIf2mBsSsCid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsSsCid.setStatus("current")
_WmanIf2mBsSsPowerSavingClassId_Type = WmanIf2mPsClassId
_WmanIf2mBsSsPowerSavingClassId_Object = MibTableColumn
wmanIf2mBsSsPowerSavingClassId = _WmanIf2mBsSsPowerSavingClassId_Object(
    (1, 0, 8802, 16, 3, 1, 2, 1, 1, 2),
    _WmanIf2mBsSsPowerSavingClassId_Type()
)
wmanIf2mBsSsPowerSavingClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsPowerSavingClassId.setStatus("current")
_WmanIf2mBsSsPowerSavingClassesTable_Object = MibTable
wmanIf2mBsSsPowerSavingClassesTable = _WmanIf2mBsSsPowerSavingClassesTable_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsPowerSavingClassesTable.setStatus("current")
_WmanIf2mBsSsPowerSavingClassesEntry_Object = MibTableRow
wmanIf2mBsSsPowerSavingClassesEntry = _WmanIf2mBsSsPowerSavingClassesEntry_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1)
)
wmanIf2mBsSsPowerSavingClassesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsPsClassId"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsPowerSavingClassesEntry.setStatus("current")
_WmanIf2mBsSsPsClassId_Type = WmanIf2mPsClassId
_WmanIf2mBsSsPsClassId_Object = MibTableColumn
wmanIf2mBsSsPsClassId = _WmanIf2mBsSsPsClassId_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 1),
    _WmanIf2mBsSsPsClassId_Type()
)
wmanIf2mBsSsPsClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsSsPsClassId.setStatus("current")
_WmanIf2mBsSsStartFrameNumber_Type = Integer32
_WmanIf2mBsSsStartFrameNumber_Object = MibTableColumn
wmanIf2mBsSsStartFrameNumber = _WmanIf2mBsSsStartFrameNumber_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 2),
    _WmanIf2mBsSsStartFrameNumber_Type()
)
wmanIf2mBsSsStartFrameNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsStartFrameNumber.setStatus("current")
_WmanIf2mBsSsPowerSavingClassType_Type = WmanIf2mPsClassType
_WmanIf2mBsSsPowerSavingClassType_Object = MibTableColumn
wmanIf2mBsSsPowerSavingClassType = _WmanIf2mBsSsPowerSavingClassType_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 3),
    _WmanIf2mBsSsPowerSavingClassType_Type()
)
wmanIf2mBsSsPowerSavingClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsPowerSavingClassType.setStatus("current")
_WmanIf2mBsSsPsClassCidDirection_Type = WmanIf2mPsClassCidDir
_WmanIf2mBsSsPsClassCidDirection_Object = MibTableColumn
wmanIf2mBsSsPsClassCidDirection = _WmanIf2mBsSsPsClassCidDirection_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 4),
    _WmanIf2mBsSsPsClassCidDirection_Type()
)
wmanIf2mBsSsPsClassCidDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsPsClassCidDirection.setStatus("current")
_WmanIf2mBsSsTrafficTriggeredWakening_Type = WmanIf2mTrafficWkFlag
_WmanIf2mBsSsTrafficTriggeredWakening_Object = MibTableColumn
wmanIf2mBsSsTrafficTriggeredWakening = _WmanIf2mBsSsTrafficTriggeredWakening_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 5),
    _WmanIf2mBsSsTrafficTriggeredWakening_Type()
)
wmanIf2mBsSsTrafficTriggeredWakening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsTrafficTriggeredWakening.setStatus("current")


class _WmanIf2mBsSsInitialSleepWindow_Type(Integer32):
    """Custom type wmanIf2mBsSsInitialSleepWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsSsInitialSleepWindow_Type.__name__ = "Integer32"
_WmanIf2mBsSsInitialSleepWindow_Object = MibTableColumn
wmanIf2mBsSsInitialSleepWindow = _WmanIf2mBsSsInitialSleepWindow_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 6),
    _WmanIf2mBsSsInitialSleepWindow_Type()
)
wmanIf2mBsSsInitialSleepWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsInitialSleepWindow.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsInitialSleepWindow.setUnits("frame")


class _WmanIf2mBsSsFinalSleepWindowBase_Type(Integer32):
    """Custom type wmanIf2mBsSsFinalSleepWindowBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_WmanIf2mBsSsFinalSleepWindowBase_Type.__name__ = "Integer32"
_WmanIf2mBsSsFinalSleepWindowBase_Object = MibTableColumn
wmanIf2mBsSsFinalSleepWindowBase = _WmanIf2mBsSsFinalSleepWindowBase_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 7),
    _WmanIf2mBsSsFinalSleepWindowBase_Type()
)
wmanIf2mBsSsFinalSleepWindowBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsFinalSleepWindowBase.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsFinalSleepWindowBase.setUnits("frame")


class _WmanIf2mBsSsFinalSleepWindowExponent_Type(Integer32):
    """Custom type wmanIf2mBsSsFinalSleepWindowExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsSsFinalSleepWindowExponent_Type.__name__ = "Integer32"
_WmanIf2mBsSsFinalSleepWindowExponent_Object = MibTableColumn
wmanIf2mBsSsFinalSleepWindowExponent = _WmanIf2mBsSsFinalSleepWindowExponent_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 8),
    _WmanIf2mBsSsFinalSleepWindowExponent_Type()
)
wmanIf2mBsSsFinalSleepWindowExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsFinalSleepWindowExponent.setStatus("current")


class _WmanIf2mBsSsListeningWindow_Type(Integer32):
    """Custom type wmanIf2mBsSsListeningWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsSsListeningWindow_Type.__name__ = "Integer32"
_WmanIf2mBsSsListeningWindow_Object = MibTableColumn
wmanIf2mBsSsListeningWindow = _WmanIf2mBsSsListeningWindow_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 9),
    _WmanIf2mBsSsListeningWindow_Type()
)
wmanIf2mBsSsListeningWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsListeningWindow.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsListeningWindow.setUnits("frame")
_WmanIf2mBsSsPowerSavingMode_Type = WmanIf2mPowerSavingMode
_WmanIf2mBsSsPowerSavingMode_Object = MibTableColumn
wmanIf2mBsSsPowerSavingMode = _WmanIf2mBsSsPowerSavingMode_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 10),
    _WmanIf2mBsSsPowerSavingMode_Type()
)
wmanIf2mBsSsPowerSavingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsPowerSavingMode.setStatus("current")


class _WmanIf2mBsSsSlpId_Type(Integer32):
    """Custom type wmanIf2mBsSsSlpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_WmanIf2mBsSsSlpId_Type.__name__ = "Integer32"
_WmanIf2mBsSsSlpId_Object = MibTableColumn
wmanIf2mBsSsSlpId = _WmanIf2mBsSsSlpId_Object(
    (1, 0, 8802, 16, 3, 1, 2, 2, 1, 11),
    _WmanIf2mBsSsSlpId_Type()
)
wmanIf2mBsSsSlpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsSlpId.setStatus("current")
_WmanIf2mBsNeighborAdv_ObjectIdentity = ObjectIdentity
wmanIf2mBsNeighborAdv = _WmanIf2mBsNeighborAdv_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1, 3)
)
_WmanIf2mBsNeighborAdvCommonTable_Object = MibTable
wmanIf2mBsNeighborAdvCommonTable = _WmanIf2mBsNeighborAdvCommonTable_Object(
    (1, 0, 8802, 16, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborAdvCommonTable.setStatus("current")
_WmanIf2mBsNeighborAdvCommonEntry_Object = MibTableRow
wmanIf2mBsNeighborAdvCommonEntry = _WmanIf2mBsNeighborAdvCommonEntry_Object(
    (1, 0, 8802, 16, 3, 1, 3, 1, 1)
)
wmanIf2mBsNeighborAdvCommonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborAdvCommonEntry.setStatus("current")
_WmanIf2mBsSkipOptions_Type = WmanIf2mSkipOptBitMap
_WmanIf2mBsSkipOptions_Object = MibTableColumn
wmanIf2mBsSkipOptions = _WmanIf2mBsSkipOptions_Object(
    (1, 0, 8802, 16, 3, 1, 3, 1, 1, 1),
    _WmanIf2mBsSkipOptions_Type()
)
wmanIf2mBsSkipOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsSkipOptions.setStatus("current")
_WmanIf2mBsOperatorId_Type = WmanIf2mNbrOperatorId
_WmanIf2mBsOperatorId_Object = MibTableColumn
wmanIf2mBsOperatorId = _WmanIf2mBsOperatorId_Object(
    (1, 0, 8802, 16, 3, 1, 3, 1, 1, 2),
    _WmanIf2mBsOperatorId_Type()
)
wmanIf2mBsOperatorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOperatorId.setStatus("current")


class _WmanIf2mBsNumOfNeighbors_Type(Unsigned32):
    """Custom type wmanIf2mBsNumOfNeighbors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsNumOfNeighbors_Type.__name__ = "Unsigned32"
_WmanIf2mBsNumOfNeighbors_Object = MibTableColumn
wmanIf2mBsNumOfNeighbors = _WmanIf2mBsNumOfNeighbors_Object(
    (1, 0, 8802, 16, 3, 1, 3, 1, 1, 3),
    _WmanIf2mBsNumOfNeighbors_Type()
)
wmanIf2mBsNumOfNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsNumOfNeighbors.setStatus("current")


class _WmanIf2mBsConfigChangeCount_Type(Integer32):
    """Custom type wmanIf2mBsConfigChangeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsConfigChangeCount_Type.__name__ = "Integer32"
_WmanIf2mBsConfigChangeCount_Object = MibTableColumn
wmanIf2mBsConfigChangeCount = _WmanIf2mBsConfigChangeCount_Object(
    (1, 0, 8802, 16, 3, 1, 3, 1, 1, 4),
    _WmanIf2mBsConfigChangeCount_Type()
)
wmanIf2mBsConfigChangeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsConfigChangeCount.setStatus("current")
_WmanIf2mBsNeighborAdvertizementTable_Object = MibTable
wmanIf2mBsNeighborAdvertizementTable = _WmanIf2mBsNeighborAdvertizementTable_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborAdvertizementTable.setStatus("current")
_WmanIf2mBsNeighborAdvertizementEntry_Object = MibTableRow
wmanIf2mBsNeighborAdvertizementEntry = _WmanIf2mBsNeighborAdvertizementEntry_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1)
)
wmanIf2mBsNeighborAdvertizementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsNeighborBsIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborAdvertizementEntry.setStatus("current")


class _WmanIf2mBsNeighborBsIndex_Type(Integer32):
    """Custom type wmanIf2mBsNeighborBsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsNeighborBsIndex_Type.__name__ = "Integer32"
_WmanIf2mBsNeighborBsIndex_Object = MibTableColumn
wmanIf2mBsNeighborBsIndex = _WmanIf2mBsNeighborBsIndex_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 1),
    _WmanIf2mBsNeighborBsIndex_Type()
)
wmanIf2mBsNeighborBsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborBsIndex.setStatus("current")
_WmanIf2mBsNeighborBsId_Type = WmanIf2mNbrBsId
_WmanIf2mBsNeighborBsId_Object = MibTableColumn
wmanIf2mBsNeighborBsId = _WmanIf2mBsNeighborBsId_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 2),
    _WmanIf2mBsNeighborBsId_Type()
)
wmanIf2mBsNeighborBsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborBsId.setStatus("current")
_WmanIf2mBsPhyProfileId_Type = WmanIf2mPhyProfileId
_WmanIf2mBsPhyProfileId_Object = MibTableColumn
wmanIf2mBsPhyProfileId = _WmanIf2mBsPhyProfileId_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 3),
    _WmanIf2mBsPhyProfileId_Type()
)
wmanIf2mBsPhyProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsPhyProfileId.setStatus("current")


class _WmanIf2mBsFaIndex_Type(Unsigned32):
    """Custom type wmanIf2mBsFaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsFaIndex_Type.__name__ = "Unsigned32"
_WmanIf2mBsFaIndex_Object = MibTableColumn
wmanIf2mBsFaIndex = _WmanIf2mBsFaIndex_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 4),
    _WmanIf2mBsFaIndex_Type()
)
wmanIf2mBsFaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsFaIndex.setStatus("current")


class _WmanIf2mBsEirp_Type(Integer32):
    """Custom type wmanIf2mBsEirp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_WmanIf2mBsEirp_Type.__name__ = "Integer32"
_WmanIf2mBsEirp_Object = MibTableColumn
wmanIf2mBsEirp = _WmanIf2mBsEirp_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 5),
    _WmanIf2mBsEirp_Type()
)
wmanIf2mBsEirp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsEirp.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsEirp.setUnits("dBm")


class _WmanIf2mBsPreampleSubchIndex_Type(Unsigned32):
    """Custom type wmanIf2mBsPreampleSubchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsPreampleSubchIndex_Type.__name__ = "Unsigned32"
_WmanIf2mBsPreampleSubchIndex_Object = MibTableColumn
wmanIf2mBsPreampleSubchIndex = _WmanIf2mBsPreampleSubchIndex_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 6),
    _WmanIf2mBsPreampleSubchIndex_Type()
)
wmanIf2mBsPreampleSubchIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsPreampleSubchIndex.setStatus("current")
_WmanIf2mBsHandoverProcOptimization_Type = WmanIf2mHoProcOptm
_WmanIf2mBsHandoverProcOptimization_Object = MibTableColumn
wmanIf2mBsHandoverProcOptimization = _WmanIf2mBsHandoverProcOptimization_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 7),
    _WmanIf2mBsHandoverProcOptimization_Type()
)
wmanIf2mBsHandoverProcOptimization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsHandoverProcOptimization.setStatus("current")
_WmanIf2mBsSchedulingService_Type = WmanIf2mSchedulingSupp
_WmanIf2mBsSchedulingService_Object = MibTableColumn
wmanIf2mBsSchedulingService = _WmanIf2mBsSchedulingService_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 8),
    _WmanIf2mBsSchedulingService_Type()
)
wmanIf2mBsSchedulingService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsSchedulingService.setStatus("current")


class _WmanIf2mBsChannelBandwidth_Type(Integer32):
    """Custom type wmanIf2mBsChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WmanIf2mBsChannelBandwidth_Type.__name__ = "Integer32"
_WmanIf2mBsChannelBandwidth_Object = MibTableColumn
wmanIf2mBsChannelBandwidth = _WmanIf2mBsChannelBandwidth_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 9),
    _WmanIf2mBsChannelBandwidth_Type()
)
wmanIf2mBsChannelBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsChannelBandwidth.setUnits("125KHz")
_WmanIf2mBsFftSize_Type = WmanIf2mOfdmaFftSize
_WmanIf2mBsFftSize_Object = MibTableColumn
wmanIf2mBsFftSize = _WmanIf2mBsFftSize_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 10),
    _WmanIf2mBsFftSize_Type()
)
wmanIf2mBsFftSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsFftSize.setStatus("current")
_WmanIf2mBsCyclicPrefix_Type = WmanIf2mOfdmaCp
_WmanIf2mBsCyclicPrefix_Object = MibTableColumn
wmanIf2mBsCyclicPrefix = _WmanIf2mBsCyclicPrefix_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 11),
    _WmanIf2mBsCyclicPrefix_Type()
)
wmanIf2mBsCyclicPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsCyclicPrefix.setStatus("current")
_WmanIf2mBsFrameDurationCode_Type = WmanIf2mOfdmaFrame
_WmanIf2mBsFrameDurationCode_Object = MibTableColumn
wmanIf2mBsFrameDurationCode = _WmanIf2mBsFrameDurationCode_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 12),
    _WmanIf2mBsFrameDurationCode_Type()
)
wmanIf2mBsFrameDurationCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsFrameDurationCode.setStatus("current")
_WmanIf2mBsMobilityFeatureSupported_Type = WmanIf2mOfdmaMobility
_WmanIf2mBsMobilityFeatureSupported_Object = MibTableColumn
wmanIf2mBsMobilityFeatureSupported = _WmanIf2mBsMobilityFeatureSupported_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 13),
    _WmanIf2mBsMobilityFeatureSupported_Type()
)
wmanIf2mBsMobilityFeatureSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsMobilityFeatureSupported.setStatus("current")


class _WmanIf2mBsNrbBsPagingGroupListIndex_Type(Integer32):
    """Custom type wmanIf2mBsNrbBsPagingGroupListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsNrbBsPagingGroupListIndex_Type.__name__ = "Integer32"
_WmanIf2mBsNrbBsPagingGroupListIndex_Object = MibTableColumn
wmanIf2mBsNrbBsPagingGroupListIndex = _WmanIf2mBsNrbBsPagingGroupListIndex_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 14),
    _WmanIf2mBsNrbBsPagingGroupListIndex_Type()
)
wmanIf2mBsNrbBsPagingGroupListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsNrbBsPagingGroupListIndex.setStatus("current")
_WmanIf2BsNeighborAdvertizementRowStatus_Type = RowStatus
_WmanIf2BsNeighborAdvertizementRowStatus_Object = MibTableColumn
wmanIf2BsNeighborAdvertizementRowStatus = _WmanIf2BsNeighborAdvertizementRowStatus_Object(
    (1, 0, 8802, 16, 3, 1, 3, 2, 1, 15),
    _WmanIf2BsNeighborAdvertizementRowStatus_Type()
)
wmanIf2BsNeighborAdvertizementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsNeighborAdvertizementRowStatus.setStatus("current")
_WmanIf2mBsNeighborBsOfdmaUcdTable_Object = MibTable
wmanIf2mBsNeighborBsOfdmaUcdTable = _WmanIf2mBsNeighborBsOfdmaUcdTable_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborBsOfdmaUcdTable.setStatus("current")
_WmanIf2mBsNeighborBsOfdmaUcdEntry_Object = MibTableRow
wmanIf2mBsNeighborBsOfdmaUcdEntry = _WmanIf2mBsNeighborBsOfdmaUcdEntry_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1)
)
wmanIf2mBsNeighborBsOfdmaUcdEntry.setIndexNames(
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsNeighborBsId"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborBsOfdmaUcdEntry.setStatus("current")


class _WmanIf2mBsOfdmaCtBasedResvTimeout_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaCtBasedResvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2mBsOfdmaCtBasedResvTimeout_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaCtBasedResvTimeout_Object = MibTableColumn
wmanIf2mBsOfdmaCtBasedResvTimeout = _WmanIf2mBsOfdmaCtBasedResvTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 1),
    _WmanIf2mBsOfdmaCtBasedResvTimeout_Type()
)
wmanIf2mBsOfdmaCtBasedResvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCtBasedResvTimeout.setStatus("current")
_WmanIf2mBsOfdmaUplinkCenterFreq_Type = Unsigned32
_WmanIf2mBsOfdmaUplinkCenterFreq_Object = MibTableColumn
wmanIf2mBsOfdmaUplinkCenterFreq = _WmanIf2mBsOfdmaUplinkCenterFreq_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 2),
    _WmanIf2mBsOfdmaUplinkCenterFreq_Type()
)
wmanIf2mBsOfdmaUplinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaUplinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaUplinkCenterFreq.setUnits("kHz")


class _WmanIf2mBsOfdmaStartOfRngCodes_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaStartOfRngCodes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaStartOfRngCodes_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaStartOfRngCodes_Object = MibTableColumn
wmanIf2mBsOfdmaStartOfRngCodes = _WmanIf2mBsOfdmaStartOfRngCodes_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 3),
    _WmanIf2mBsOfdmaStartOfRngCodes_Type()
)
wmanIf2mBsOfdmaStartOfRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaStartOfRngCodes.setStatus("current")


class _WmanIf2mBsOfdmaPermutationBase_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaPermutationBase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaPermutationBase_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaPermutationBase_Object = MibTableColumn
wmanIf2mBsOfdmaPermutationBase = _WmanIf2mBsOfdmaPermutationBase_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 4),
    _WmanIf2mBsOfdmaPermutationBase_Type()
)
wmanIf2mBsOfdmaPermutationBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaPermutationBase.setStatus("current")


class _WmanIf2mBsOfdmaULAllocSubchBitmap_Type(OctetString):
    """Custom type wmanIf2mBsOfdmaULAllocSubchBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )
    fixedLength = 9


_WmanIf2mBsOfdmaULAllocSubchBitmap_Type.__name__ = "OctetString"
_WmanIf2mBsOfdmaULAllocSubchBitmap_Object = MibTableColumn
wmanIf2mBsOfdmaULAllocSubchBitmap = _WmanIf2mBsOfdmaULAllocSubchBitmap_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 5),
    _WmanIf2mBsOfdmaULAllocSubchBitmap_Type()
)
wmanIf2mBsOfdmaULAllocSubchBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaULAllocSubchBitmap.setStatus("current")


class _WmanIf2mBsOfdmaOptPermULAlloSubchBitmap_Type(OctetString):
    """Custom type wmanIf2mBsOfdmaOptPermULAlloSubchBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )
    fixedLength = 13


_WmanIf2mBsOfdmaOptPermULAlloSubchBitmap_Type.__name__ = "OctetString"
_WmanIf2mBsOfdmaOptPermULAlloSubchBitmap_Object = MibTableColumn
wmanIf2mBsOfdmaOptPermULAlloSubchBitmap = _WmanIf2mBsOfdmaOptPermULAlloSubchBitmap_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 6),
    _WmanIf2mBsOfdmaOptPermULAlloSubchBitmap_Type()
)
wmanIf2mBsOfdmaOptPermULAlloSubchBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaOptPermULAlloSubchBitmap.setStatus("current")


class _WmanIf2mBsOfdmaBandAMCAllocThreshold_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBandAMCAllocThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaBandAMCAllocThreshold_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBandAMCAllocThreshold_Object = MibTableColumn
wmanIf2mBsOfdmaBandAMCAllocThreshold = _WmanIf2mBsOfdmaBandAMCAllocThreshold_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 7),
    _WmanIf2mBsOfdmaBandAMCAllocThreshold_Type()
)
wmanIf2mBsOfdmaBandAMCAllocThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCAllocThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCAllocThreshold.setUnits("dB")


class _WmanIf2mBsOfdmaBandAMCReleaseThreshold_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBandAMCReleaseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaBandAMCReleaseThreshold_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBandAMCReleaseThreshold_Object = MibTableColumn
wmanIf2mBsOfdmaBandAMCReleaseThreshold = _WmanIf2mBsOfdmaBandAMCReleaseThreshold_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 8),
    _WmanIf2mBsOfdmaBandAMCReleaseThreshold_Type()
)
wmanIf2mBsOfdmaBandAMCReleaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCReleaseThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCReleaseThreshold.setUnits("dB")


class _WmanIf2mBsOfdmaBandAMCAllocTimer_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBandAMCAllocTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaBandAMCAllocTimer_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBandAMCAllocTimer_Object = MibTableColumn
wmanIf2mBsOfdmaBandAMCAllocTimer = _WmanIf2mBsOfdmaBandAMCAllocTimer_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 9),
    _WmanIf2mBsOfdmaBandAMCAllocTimer_Type()
)
wmanIf2mBsOfdmaBandAMCAllocTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCAllocTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCAllocTimer.setUnits("Frame")


class _WmanIf2mBsOfdmaBandAMCReleaseTimer_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBandAMCReleaseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaBandAMCReleaseTimer_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBandAMCReleaseTimer_Object = MibTableColumn
wmanIf2mBsOfdmaBandAMCReleaseTimer = _WmanIf2mBsOfdmaBandAMCReleaseTimer_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 10),
    _WmanIf2mBsOfdmaBandAMCReleaseTimer_Type()
)
wmanIf2mBsOfdmaBandAMCReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCReleaseTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCReleaseTimer.setUnits("Frame")


class _WmanIf2mBsOfdmaBandStatRepMAXPeriod_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBandStatRepMAXPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaBandStatRepMAXPeriod_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBandStatRepMAXPeriod_Object = MibTableColumn
wmanIf2mBsOfdmaBandStatRepMAXPeriod = _WmanIf2mBsOfdmaBandStatRepMAXPeriod_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 11),
    _WmanIf2mBsOfdmaBandStatRepMAXPeriod_Type()
)
wmanIf2mBsOfdmaBandStatRepMAXPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandStatRepMAXPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandStatRepMAXPeriod.setUnits("Frame")


class _WmanIf2mBsOfdmaBandAMCRetryTimer_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBandAMCRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaBandAMCRetryTimer_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBandAMCRetryTimer_Object = MibTableColumn
wmanIf2mBsOfdmaBandAMCRetryTimer = _WmanIf2mBsOfdmaBandAMCRetryTimer_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 12),
    _WmanIf2mBsOfdmaBandAMCRetryTimer_Type()
)
wmanIf2mBsOfdmaBandAMCRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAMCRetryTimer.setUnits("Frame")


class _WmanIf2mBsOfdmaHandoverRangingStart_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaHandoverRangingStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaHandoverRangingStart_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaHandoverRangingStart_Object = MibTableColumn
wmanIf2mBsOfdmaHandoverRangingStart = _WmanIf2mBsOfdmaHandoverRangingStart_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 13),
    _WmanIf2mBsOfdmaHandoverRangingStart_Type()
)
wmanIf2mBsOfdmaHandoverRangingStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHandoverRangingStart.setStatus("current")


class _WmanIf2mBsOfdmaHandoverRangingEnd_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaHandoverRangingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaHandoverRangingEnd_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaHandoverRangingEnd_Object = MibTableColumn
wmanIf2mBsOfdmaHandoverRangingEnd = _WmanIf2mBsOfdmaHandoverRangingEnd_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 14),
    _WmanIf2mBsOfdmaHandoverRangingEnd_Type()
)
wmanIf2mBsOfdmaHandoverRangingEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHandoverRangingEnd.setStatus("current")
_WmanIf2mBsOfdmaHARQAackDelayDLBurst_Type = WmanIf2mHarqAckDelay
_WmanIf2mBsOfdmaHARQAackDelayDLBurst_Object = MibTableColumn
wmanIf2mBsOfdmaHARQAackDelayDLBurst = _WmanIf2mBsOfdmaHARQAackDelayDLBurst_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 15),
    _WmanIf2mBsOfdmaHARQAackDelayDLBurst_Type()
)
wmanIf2mBsOfdmaHARQAackDelayDLBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHARQAackDelayDLBurst.setStatus("current")


class _WmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap_Type(OctetString):
    """Custom type wmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_WmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap_Type.__name__ = "OctetString"
_WmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap_Object = MibTableColumn
wmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap = _WmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 16),
    _WmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap_Type()
)
wmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap.setStatus("current")


class _WmanIf2mBsOfdmaMaxRetransmission_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaMaxRetransmission based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2mBsOfdmaMaxRetransmission_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaMaxRetransmission_Object = MibTableColumn
wmanIf2mBsOfdmaMaxRetransmission = _WmanIf2mBsOfdmaMaxRetransmission_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 17),
    _WmanIf2mBsOfdmaMaxRetransmission_Type()
)
wmanIf2mBsOfdmaMaxRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaMaxRetransmission.setStatus("current")


class _WmanIf2mBsOfdmaNormalizedCnOverride_Type(OctetString):
    """Custom type wmanIf2mBsOfdmaNormalizedCnOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_WmanIf2mBsOfdmaNormalizedCnOverride_Type.__name__ = "OctetString"
_WmanIf2mBsOfdmaNormalizedCnOverride_Object = MibTableColumn
wmanIf2mBsOfdmaNormalizedCnOverride = _WmanIf2mBsOfdmaNormalizedCnOverride_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 18),
    _WmanIf2mBsOfdmaNormalizedCnOverride_Type()
)
wmanIf2mBsOfdmaNormalizedCnOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaNormalizedCnOverride.setStatus("current")


class _WmanIf2mBsOfdmaSizeOfCqichId_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaSizeOfCqichId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsOfdmaSizeOfCqichId_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaSizeOfCqichId_Object = MibTableColumn
wmanIf2mBsOfdmaSizeOfCqichId = _WmanIf2mBsOfdmaSizeOfCqichId_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 19),
    _WmanIf2mBsOfdmaSizeOfCqichId_Type()
)
wmanIf2mBsOfdmaSizeOfCqichId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaSizeOfCqichId.setStatus("current")


class _WmanIf2mBsOfdmaNormalizedCnValue_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaNormalizedCnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2mBsOfdmaNormalizedCnValue_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaNormalizedCnValue_Object = MibTableColumn
wmanIf2mBsOfdmaNormalizedCnValue = _WmanIf2mBsOfdmaNormalizedCnValue_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 20),
    _WmanIf2mBsOfdmaNormalizedCnValue_Type()
)
wmanIf2mBsOfdmaNormalizedCnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaNormalizedCnValue.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaNormalizedCnValue.setUnits("dB")


class _WmanIf2mBsOfdmaNormalizedCnOverride2_Type(OctetString):
    """Custom type wmanIf2mBsOfdmaNormalizedCnOverride2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixedLength = 7


_WmanIf2mBsOfdmaNormalizedCnOverride2_Type.__name__ = "OctetString"
_WmanIf2mBsOfdmaNormalizedCnOverride2_Object = MibTableColumn
wmanIf2mBsOfdmaNormalizedCnOverride2 = _WmanIf2mBsOfdmaNormalizedCnOverride2_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 21),
    _WmanIf2mBsOfdmaNormalizedCnOverride2_Type()
)
wmanIf2mBsOfdmaNormalizedCnOverride2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaNormalizedCnOverride2.setStatus("current")


class _WmanIf2mBsOfdmaBandAmcEntryAvgCinr_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBandAmcEntryAvgCinr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2mBsOfdmaBandAmcEntryAvgCinr_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBandAmcEntryAvgCinr_Object = MibTableColumn
wmanIf2mBsOfdmaBandAmcEntryAvgCinr = _WmanIf2mBsOfdmaBandAmcEntryAvgCinr_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 22),
    _WmanIf2mBsOfdmaBandAmcEntryAvgCinr_Type()
)
wmanIf2mBsOfdmaBandAmcEntryAvgCinr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAmcEntryAvgCinr.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBandAmcEntryAvgCinr.setUnits("dB")


class _WmanIf2mBsOfdmaAasPreambleUpperBond_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaAasPreambleUpperBond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2mBsOfdmaAasPreambleUpperBond_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaAasPreambleUpperBond_Object = MibTableColumn
wmanIf2mBsOfdmaAasPreambleUpperBond = _WmanIf2mBsOfdmaAasPreambleUpperBond_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 23),
    _WmanIf2mBsOfdmaAasPreambleUpperBond_Type()
)
wmanIf2mBsOfdmaAasPreambleUpperBond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAasPreambleUpperBond.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAasPreambleUpperBond.setUnits("0.25 dB")


class _WmanIf2mBsOfdmaAasPreambleLowerBond_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaAasPreambleLowerBond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WmanIf2mBsOfdmaAasPreambleLowerBond_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaAasPreambleLowerBond_Object = MibTableColumn
wmanIf2mBsOfdmaAasPreambleLowerBond = _WmanIf2mBsOfdmaAasPreambleLowerBond_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 24),
    _WmanIf2mBsOfdmaAasPreambleLowerBond_Type()
)
wmanIf2mBsOfdmaAasPreambleLowerBond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAasPreambleLowerBond.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAasPreambleLowerBond.setUnits("0.25 dB")


class _WmanIf2mBsOfdmaAasBeamSelectAllowed_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaAasBeamSelectAllowed based on Integer32"""
    defaultValue = 1

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


_WmanIf2mBsOfdmaAasBeamSelectAllowed_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaAasBeamSelectAllowed_Object = MibTableColumn
wmanIf2mBsOfdmaAasBeamSelectAllowed = _WmanIf2mBsOfdmaAasBeamSelectAllowed_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 25),
    _WmanIf2mBsOfdmaAasBeamSelectAllowed_Type()
)
wmanIf2mBsOfdmaAasBeamSelectAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAasBeamSelectAllowed.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAasBeamSelectAllowed.setUnits("0.25 dB")


class _WmanIf2mBsOfdmaCqichIndicationFlag_Type(OctetString):
    """Custom type wmanIf2mBsOfdmaCqichIndicationFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIf2mBsOfdmaCqichIndicationFlag_Type.__name__ = "OctetString"
_WmanIf2mBsOfdmaCqichIndicationFlag_Object = MibTableColumn
wmanIf2mBsOfdmaCqichIndicationFlag = _WmanIf2mBsOfdmaCqichIndicationFlag_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 26),
    _WmanIf2mBsOfdmaCqichIndicationFlag_Type()
)
wmanIf2mBsOfdmaCqichIndicationFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCqichIndicationFlag.setStatus("current")
_WmanIf2mBsOfdmaUpPowerAdjStep_Type = Unsigned32
_WmanIf2mBsOfdmaUpPowerAdjStep_Object = MibTableColumn
wmanIf2mBsOfdmaUpPowerAdjStep = _WmanIf2mBsOfdmaUpPowerAdjStep_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 27),
    _WmanIf2mBsOfdmaUpPowerAdjStep_Type()
)
wmanIf2mBsOfdmaUpPowerAdjStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaUpPowerAdjStep.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaUpPowerAdjStep.setUnits("0.01 dB")
_WmanIf2mBsOfdmaDownPowerAdjStep_Type = Unsigned32
_WmanIf2mBsOfdmaDownPowerAdjStep_Object = MibTableColumn
wmanIf2mBsOfdmaDownPowerAdjStep = _WmanIf2mBsOfdmaDownPowerAdjStep_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 28),
    _WmanIf2mBsOfdmaDownPowerAdjStep_Type()
)
wmanIf2mBsOfdmaDownPowerAdjStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaDownPowerAdjStep.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaDownPowerAdjStep.setUnits("0.01 dB")
_WmanIf2mBsOfdmaMinPowerOffsetAdj_Type = Integer32
_WmanIf2mBsOfdmaMinPowerOffsetAdj_Object = MibTableColumn
wmanIf2mBsOfdmaMinPowerOffsetAdj = _WmanIf2mBsOfdmaMinPowerOffsetAdj_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 29),
    _WmanIf2mBsOfdmaMinPowerOffsetAdj_Type()
)
wmanIf2mBsOfdmaMinPowerOffsetAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaMinPowerOffsetAdj.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaMinPowerOffsetAdj.setUnits("0.1 dB")
_WmanIf2mBsOfdmaMaxPowerOffsetAdj_Type = Integer32
_WmanIf2mBsOfdmaMaxPowerOffsetAdj_Object = MibTableColumn
wmanIf2mBsOfdmaMaxPowerOffsetAdj = _WmanIf2mBsOfdmaMaxPowerOffsetAdj_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 30),
    _WmanIf2mBsOfdmaMaxPowerOffsetAdj_Type()
)
wmanIf2mBsOfdmaMaxPowerOffsetAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaMaxPowerOffsetAdj.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaMaxPowerOffsetAdj.setUnits("0.1 dB")


class _WmanIf2mBsOfdmaHandoverRngCodes_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaHandoverRngCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaHandoverRngCodes_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaHandoverRngCodes_Object = MibTableColumn
wmanIf2mBsOfdmaHandoverRngCodes = _WmanIf2mBsOfdmaHandoverRngCodes_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 31),
    _WmanIf2mBsOfdmaHandoverRngCodes_Type()
)
wmanIf2mBsOfdmaHandoverRngCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHandoverRngCodes.setStatus("current")
_WmanIf2mBsOfdmaInitialRngInterval_Type = Integer32
_WmanIf2mBsOfdmaInitialRngInterval_Object = MibTableColumn
wmanIf2mBsOfdmaInitialRngInterval = _WmanIf2mBsOfdmaInitialRngInterval_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 32),
    _WmanIf2mBsOfdmaInitialRngInterval_Type()
)
wmanIf2mBsOfdmaInitialRngInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaInitialRngInterval.setStatus("current")


class _WmanIf2mBsOfdmaTxPwrRepThreshold_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaTxPwrRepThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaTxPwrRepThreshold_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaTxPwrRepThreshold_Object = MibTableColumn
wmanIf2mBsOfdmaTxPwrRepThreshold = _WmanIf2mBsOfdmaTxPwrRepThreshold_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 33),
    _WmanIf2mBsOfdmaTxPwrRepThreshold_Type()
)
wmanIf2mBsOfdmaTxPwrRepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaTxPwrRepThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaTxPwrRepThreshold.setUnits("dB")


class _WmanIf2mBsOfdmaTprPower_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaTprPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaTprPower_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaTprPower_Object = MibTableColumn
wmanIf2mBsOfdmaTprPower = _WmanIf2mBsOfdmaTprPower_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 34),
    _WmanIf2mBsOfdmaTprPower_Type()
)
wmanIf2mBsOfdmaTprPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaTprPower.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaTprPower.setUnits("dB")


class _WmanIf2mBsOfdmaAlphaPavg_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaAlphaPavg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaAlphaPavg_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaAlphaPavg_Object = MibTableColumn
wmanIf2mBsOfdmaAlphaPavg = _WmanIf2mBsOfdmaAlphaPavg_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 35),
    _WmanIf2mBsOfdmaAlphaPavg_Type()
)
wmanIf2mBsOfdmaAlphaPavg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAlphaPavg.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAlphaPavg.setUnits("dB")


class _WmanIf2mBsOfdmaCqichTxPwrRepThreshold_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaCqichTxPwrRepThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaCqichTxPwrRepThreshold_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaCqichTxPwrRepThreshold_Object = MibTableColumn
wmanIf2mBsOfdmaCqichTxPwrRepThreshold = _WmanIf2mBsOfdmaCqichTxPwrRepThreshold_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 36),
    _WmanIf2mBsOfdmaCqichTxPwrRepThreshold_Type()
)
wmanIf2mBsOfdmaCqichTxPwrRepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCqichTxPwrRepThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCqichTxPwrRepThreshold.setUnits("dB")


class _WmanIf2mBsOfdmaCqichTprPower_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaCqichTprPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaCqichTprPower_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaCqichTprPower_Object = MibTableColumn
wmanIf2mBsOfdmaCqichTprPower = _WmanIf2mBsOfdmaCqichTprPower_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 37),
    _WmanIf2mBsOfdmaCqichTprPower_Type()
)
wmanIf2mBsOfdmaCqichTprPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCqichTprPower.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCqichTprPower.setUnits("dB")


class _WmanIf2mBsOfdmaCqichAlphaPavg_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaCqichAlphaPavg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaCqichAlphaPavg_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaCqichAlphaPavg_Object = MibTableColumn
wmanIf2mBsOfdmaCqichAlphaPavg = _WmanIf2mBsOfdmaCqichAlphaPavg_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 38),
    _WmanIf2mBsOfdmaCqichAlphaPavg_Type()
)
wmanIf2mBsOfdmaCqichAlphaPavg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCqichAlphaPavg.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCqichAlphaPavg.setUnits("dB")
_WmanIf2mBsOfdmaNormalizedCnChSounding_Type = Integer32
_WmanIf2mBsOfdmaNormalizedCnChSounding_Object = MibTableColumn
wmanIf2mBsOfdmaNormalizedCnChSounding = _WmanIf2mBsOfdmaNormalizedCnChSounding_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 39),
    _WmanIf2mBsOfdmaNormalizedCnChSounding_Type()
)
wmanIf2mBsOfdmaNormalizedCnChSounding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaNormalizedCnChSounding.setStatus("current")


class _WmanIf2mBsOfdmaInitialRngBackoffStart_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaInitialRngBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaInitialRngBackoffStart_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaInitialRngBackoffStart_Object = MibTableColumn
wmanIf2mBsOfdmaInitialRngBackoffStart = _WmanIf2mBsOfdmaInitialRngBackoffStart_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 40),
    _WmanIf2mBsOfdmaInitialRngBackoffStart_Type()
)
wmanIf2mBsOfdmaInitialRngBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaInitialRngBackoffStart.setStatus("current")


class _WmanIf2mBsOfdmaInitialRngBackoffEnd_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaInitialRngBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaInitialRngBackoffEnd_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaInitialRngBackoffEnd_Object = MibTableColumn
wmanIf2mBsOfdmaInitialRngBackoffEnd = _WmanIf2mBsOfdmaInitialRngBackoffEnd_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 41),
    _WmanIf2mBsOfdmaInitialRngBackoffEnd_Type()
)
wmanIf2mBsOfdmaInitialRngBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaInitialRngBackoffEnd.setStatus("current")


class _WmanIf2mBsOfdmaBwRequestBackoffStart_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBwRequestBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaBwRequestBackoffStart_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBwRequestBackoffStart_Object = MibTableColumn
wmanIf2mBsOfdmaBwRequestBackoffStart = _WmanIf2mBsOfdmaBwRequestBackoffStart_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 42),
    _WmanIf2mBsOfdmaBwRequestBackoffStart_Type()
)
wmanIf2mBsOfdmaBwRequestBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBwRequestBackoffStart.setStatus("current")


class _WmanIf2mBsOfdmaBwRequestBackoffEnd_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBwRequestBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaBwRequestBackoffEnd_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBwRequestBackoffEnd_Object = MibTableColumn
wmanIf2mBsOfdmaBwRequestBackoffEnd = _WmanIf2mBsOfdmaBwRequestBackoffEnd_Object(
    (1, 0, 8802, 16, 3, 1, 3, 3, 1, 43),
    _WmanIf2mBsOfdmaBwRequestBackoffEnd_Type()
)
wmanIf2mBsOfdmaBwRequestBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBwRequestBackoffEnd.setStatus("current")
_WmanIf2mBsNeighborBsOfdmaDcdTable_Object = MibTable
wmanIf2mBsNeighborBsOfdmaDcdTable = _WmanIf2mBsNeighborBsOfdmaDcdTable_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborBsOfdmaDcdTable.setStatus("current")
_WmanIf2mBsNeighborBsOfdmaDcdEntry_Object = MibTableRow
wmanIf2mBsNeighborBsOfdmaDcdEntry = _WmanIf2mBsNeighborBsOfdmaDcdEntry_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1)
)
wmanIf2mBsNeighborBsOfdmaDcdEntry.setIndexNames(
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsNeighborBsId"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborBsOfdmaDcdEntry.setStatus("current")


class _WmanIf2mBsOfdmaBsEIRP_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaBsEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_WmanIf2mBsOfdmaBsEIRP_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaBsEIRP_Object = MibTableColumn
wmanIf2mBsOfdmaBsEIRP = _WmanIf2mBsOfdmaBsEIRP_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 1),
    _WmanIf2mBsOfdmaBsEIRP_Type()
)
wmanIf2mBsOfdmaBsEIRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBsEIRP.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBsEIRP.setUnits("dBm")


class _WmanIf2mBsOfdmaChannelNumber_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_WmanIf2mBsOfdmaChannelNumber_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaChannelNumber_Object = MibTableColumn
wmanIf2mBsOfdmaChannelNumber = _WmanIf2mBsOfdmaChannelNumber_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 2),
    _WmanIf2mBsOfdmaChannelNumber_Type()
)
wmanIf2mBsOfdmaChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaChannelNumber.setStatus("current")


class _WmanIf2mBsOfdmaTTG_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaTTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaTTG_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaTTG_Object = MibTableColumn
wmanIf2mBsOfdmaTTG = _WmanIf2mBsOfdmaTTG_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 3),
    _WmanIf2mBsOfdmaTTG_Type()
)
wmanIf2mBsOfdmaTTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaTTG.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaTTG.setUnits("PS")


class _WmanIf2mBsOfdmaRTG_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaRTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaRTG_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaRTG_Object = MibTableColumn
wmanIf2mBsOfdmaRTG = _WmanIf2mBsOfdmaRTG_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 4),
    _WmanIf2mBsOfdmaRTG_Type()
)
wmanIf2mBsOfdmaRTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaRTG.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaRTG.setUnits("PS")


class _WmanIf2mBsOfdmaInitRngMaxRSS_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaInitRngMaxRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_WmanIf2mBsOfdmaInitRngMaxRSS_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaInitRngMaxRSS_Object = MibTableColumn
wmanIf2mBsOfdmaInitRngMaxRSS = _WmanIf2mBsOfdmaInitRngMaxRSS_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 5),
    _WmanIf2mBsOfdmaInitRngMaxRSS_Type()
)
wmanIf2mBsOfdmaInitRngMaxRSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaInitRngMaxRSS.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaInitRngMaxRSS.setUnits("dBm")
_WmanIf2mBsOfdmaDownlinkCenterFreq_Type = Unsigned32
_WmanIf2mBsOfdmaDownlinkCenterFreq_Object = MibTableColumn
wmanIf2mBsOfdmaDownlinkCenterFreq = _WmanIf2mBsOfdmaDownlinkCenterFreq_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 6),
    _WmanIf2mBsOfdmaDownlinkCenterFreq_Type()
)
wmanIf2mBsOfdmaDownlinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaDownlinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaDownlinkCenterFreq.setUnits("kHz")


class _WmanIf2mBsOfdmaBsId_Type(OctetString):
    """Custom type wmanIf2mBsOfdmaBsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_WmanIf2mBsOfdmaBsId_Type.__name__ = "OctetString"
_WmanIf2mBsOfdmaBsId_Object = MibTableColumn
wmanIf2mBsOfdmaBsId = _WmanIf2mBsOfdmaBsId_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 7),
    _WmanIf2mBsOfdmaBsId_Type()
)
wmanIf2mBsOfdmaBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaBsId.setStatus("current")
_WmanIf2mBsOfdmaMacVersion_Type = WmanIf2mMacVersion
_WmanIf2mBsOfdmaMacVersion_Object = MibTableColumn
wmanIf2mBsOfdmaMacVersion = _WmanIf2mBsOfdmaMacVersion_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 8),
    _WmanIf2mBsOfdmaMacVersion_Type()
)
wmanIf2mBsOfdmaMacVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaMacVersion.setStatus("current")


class _WmanIf2mBsOfdmaFrameDurationCode_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaFrameDurationCode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aasGap", 0),
          ("duration2ms", 1),
          ("duration2dot5ms", 2),
          ("duration4ms", 3),
          ("duration5ms", 4),
          ("duration8ms", 5),
          ("duration10ms", 6),
          ("duration12dot5ms", 7),
          ("duration20ms", 8))
    )


_WmanIf2mBsOfdmaFrameDurationCode_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaFrameDurationCode_Object = MibTableColumn
wmanIf2mBsOfdmaFrameDurationCode = _WmanIf2mBsOfdmaFrameDurationCode_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 9),
    _WmanIf2mBsOfdmaFrameDurationCode_Type()
)
wmanIf2mBsOfdmaFrameDurationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaFrameDurationCode.setStatus("current")
_WmanIf2mBsOfdmaHARQAackDelayULBurst_Type = WmanIf2mHarqAckDelay
_WmanIf2mBsOfdmaHARQAackDelayULBurst_Object = MibTableColumn
wmanIf2mBsOfdmaHARQAackDelayULBurst = _WmanIf2mBsOfdmaHARQAackDelayULBurst_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 10),
    _WmanIf2mBsOfdmaHARQAackDelayULBurst_Type()
)
wmanIf2mBsOfdmaHARQAackDelayULBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHARQAackDelayULBurst.setStatus("current")


class _WmanIf2mBsOfdmaHarqZonePermutation_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaHarqZonePermutation based on Integer32"""
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


_WmanIf2mBsOfdmaHarqZonePermutation_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaHarqZonePermutation_Object = MibTableColumn
wmanIf2mBsOfdmaHarqZonePermutation = _WmanIf2mBsOfdmaHarqZonePermutation_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 11),
    _WmanIf2mBsOfdmaHarqZonePermutation_Type()
)
wmanIf2mBsOfdmaHarqZonePermutation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHarqZonePermutation.setStatus("current")


class _WmanIf2mBsOfdmaHMaxRetransmission_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaHMaxRetransmission based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaHMaxRetransmission_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaHMaxRetransmission_Object = MibTableColumn
wmanIf2mBsOfdmaHMaxRetransmission = _WmanIf2mBsOfdmaHMaxRetransmission_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 12),
    _WmanIf2mBsOfdmaHMaxRetransmission_Type()
)
wmanIf2mBsOfdmaHMaxRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHMaxRetransmission.setStatus("current")


class _WmanIf2mBsOfdmaCinrAlphaAvg_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaCinrAlphaAvg based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaCinrAlphaAvg_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaCinrAlphaAvg_Object = MibTableColumn
wmanIf2mBsOfdmaCinrAlphaAvg = _WmanIf2mBsOfdmaCinrAlphaAvg_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 13),
    _WmanIf2mBsOfdmaCinrAlphaAvg_Type()
)
wmanIf2mBsOfdmaCinrAlphaAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaCinrAlphaAvg.setStatus("current")


class _WmanIf2mBsOfdmaRssiAlphaAvg_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaRssiAlphaAvg based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaRssiAlphaAvg_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaRssiAlphaAvg_Object = MibTableColumn
wmanIf2mBsOfdmaRssiAlphaAvg = _WmanIf2mBsOfdmaRssiAlphaAvg_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 14),
    _WmanIf2mBsOfdmaRssiAlphaAvg_Type()
)
wmanIf2mBsOfdmaRssiAlphaAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaRssiAlphaAvg.setStatus("current")


class _WmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap_Type(OctetString):
    """Custom type wmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_WmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap_Type.__name__ = "OctetString"
_WmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap_Object = MibTableColumn
wmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap = _WmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 15),
    _WmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap_Type()
)
wmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap.setStatus("current")


class _WmanIf2mBsOfdmaHandoverSupported_Type(Bits):
    """Custom type wmanIf2mBsOfdmaHandoverSupported based on Bits"""
    namedValues = NamedValues(
        *(("handover", 0),
          ("mdHandover", 1),
          ("fbssHandover", 2))
    )

_WmanIf2mBsOfdmaHandoverSupported_Type.__name__ = "Bits"
_WmanIf2mBsOfdmaHandoverSupported_Object = MibTableColumn
wmanIf2mBsOfdmaHandoverSupported = _WmanIf2mBsOfdmaHandoverSupported_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 16),
    _WmanIf2mBsOfdmaHandoverSupported_Type()
)
wmanIf2mBsOfdmaHandoverSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHandoverSupported.setStatus("current")


class _WmanIf2mBsOfdmaThresholdAddBsDivSet_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaThresholdAddBsDivSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaThresholdAddBsDivSet_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaThresholdAddBsDivSet_Object = MibTableColumn
wmanIf2mBsOfdmaThresholdAddBsDivSet = _WmanIf2mBsOfdmaThresholdAddBsDivSet_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 17),
    _WmanIf2mBsOfdmaThresholdAddBsDivSet_Type()
)
wmanIf2mBsOfdmaThresholdAddBsDivSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaThresholdAddBsDivSet.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaThresholdAddBsDivSet.setUnits("dB")


class _WmanIf2mBsOfdmaThresholdDelBsDivSet_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaThresholdDelBsDivSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaThresholdDelBsDivSet_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaThresholdDelBsDivSet_Object = MibTableColumn
wmanIf2mBsOfdmaThresholdDelBsDivSet = _WmanIf2mBsOfdmaThresholdDelBsDivSet_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 18),
    _WmanIf2mBsOfdmaThresholdDelBsDivSet_Type()
)
wmanIf2mBsOfdmaThresholdDelBsDivSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaThresholdDelBsDivSet.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaThresholdDelBsDivSet.setUnits("dB")


class _WmanIf2mBsOfdmaAsrSlotLength_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaAsrSlotLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaAsrSlotLength_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaAsrSlotLength_Object = MibTableColumn
wmanIf2mBsOfdmaAsrSlotLength = _WmanIf2mBsOfdmaAsrSlotLength_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 19),
    _WmanIf2mBsOfdmaAsrSlotLength_Type()
)
wmanIf2mBsOfdmaAsrSlotLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAsrSlotLength.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAsrSlotLength.setUnits("Frames")


class _WmanIf2mBsOfdmaAsrSwitchingPeriod_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaAsrSwitchingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsOfdmaAsrSwitchingPeriod_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaAsrSwitchingPeriod_Object = MibTableColumn
wmanIf2mBsOfdmaAsrSwitchingPeriod = _WmanIf2mBsOfdmaAsrSwitchingPeriod_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 20),
    _WmanIf2mBsOfdmaAsrSwitchingPeriod_Type()
)
wmanIf2mBsOfdmaAsrSwitchingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAsrSwitchingPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaAsrSwitchingPeriod.setUnits("ASR slots")


class _WmanIf2mBsOfdmaHysteresisMargin_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaHysteresisMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 57),
    )


_WmanIf2mBsOfdmaHysteresisMargin_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaHysteresisMargin_Object = MibTableColumn
wmanIf2mBsOfdmaHysteresisMargin = _WmanIf2mBsOfdmaHysteresisMargin_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 21),
    _WmanIf2mBsOfdmaHysteresisMargin_Type()
)
wmanIf2mBsOfdmaHysteresisMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHysteresisMargin.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaHysteresisMargin.setUnits("dB")
_WmanIf2mBsOfdmaTimeToTrigger_Type = Integer32
_WmanIf2mBsOfdmaTimeToTrigger_Object = MibTableColumn
wmanIf2mBsOfdmaTimeToTrigger = _WmanIf2mBsOfdmaTimeToTrigger_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 22),
    _WmanIf2mBsOfdmaTimeToTrigger_Type()
)
wmanIf2mBsOfdmaTimeToTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaTimeToTrigger.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaTimeToTrigger.setUnits("milliseconds")


class _WmanIf2mBsOfdmaRestartCount_Type(Integer32):
    """Custom type wmanIf2mBsOfdmaRestartCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsOfdmaRestartCount_Type.__name__ = "Integer32"
_WmanIf2mBsOfdmaRestartCount_Object = MibTableColumn
wmanIf2mBsOfdmaRestartCount = _WmanIf2mBsOfdmaRestartCount_Object(
    (1, 0, 8802, 16, 3, 1, 3, 4, 1, 23),
    _WmanIf2mBsOfdmaRestartCount_Type()
)
wmanIf2mBsOfdmaRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsOfdmaRestartCount.setStatus("current")
_WmanIf2mBsPaging_ObjectIdentity = ObjectIdentity
wmanIf2mBsPaging = _WmanIf2mBsPaging_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1, 4)
)
_WmanIf2mBsPagingAdvertizementTable_Object = MibTable
wmanIf2mBsPagingAdvertizementTable = _WmanIf2mBsPagingAdvertizementTable_Object(
    (1, 0, 8802, 16, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wmanIf2mBsPagingAdvertizementTable.setStatus("current")
_WmanIf2mBsPagingAdvertizementEntry_Object = MibTableRow
wmanIf2mBsPagingAdvertizementEntry = _WmanIf2mBsPagingAdvertizementEntry_Object(
    (1, 0, 8802, 16, 3, 1, 4, 1, 1)
)
wmanIf2mBsPagingAdvertizementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsPagingAdvertizementEntry.setStatus("current")


class _WmanIf2mBsPagingGroupListIndex_Type(Integer32):
    """Custom type wmanIf2mBsPagingGroupListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsPagingGroupListIndex_Type.__name__ = "Integer32"
_WmanIf2mBsPagingGroupListIndex_Object = MibTableColumn
wmanIf2mBsPagingGroupListIndex = _WmanIf2mBsPagingGroupListIndex_Object(
    (1, 0, 8802, 16, 3, 1, 4, 1, 1, 1),
    _WmanIf2mBsPagingGroupListIndex_Type()
)
wmanIf2mBsPagingGroupListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingGroupListIndex.setStatus("current")


class _WmanIf2mBsPagingRspWindow_Type(Integer32):
    """Custom type wmanIf2mBsPagingRspWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsPagingRspWindow_Type.__name__ = "Integer32"
_WmanIf2mBsPagingRspWindow_Object = MibTableColumn
wmanIf2mBsPagingRspWindow = _WmanIf2mBsPagingRspWindow_Object(
    (1, 0, 8802, 16, 3, 1, 4, 1, 1, 2),
    _WmanIf2mBsPagingRspWindow_Type()
)
wmanIf2mBsPagingRspWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingRspWindow.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingRspWindow.setUnits("Frames")
_WmanIf2mBsPagingAdvRowStatus_Type = RowStatus
_WmanIf2mBsPagingAdvRowStatus_Object = MibTableColumn
wmanIf2mBsPagingAdvRowStatus = _WmanIf2mBsPagingAdvRowStatus_Object(
    (1, 0, 8802, 16, 3, 1, 4, 1, 1, 3),
    _WmanIf2mBsPagingAdvRowStatus_Type()
)
wmanIf2mBsPagingAdvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingAdvRowStatus.setStatus("current")
_WmanIf2mBsMsPagedTable_Object = MibTable
wmanIf2mBsMsPagedTable = _WmanIf2mBsMsPagedTable_Object(
    (1, 0, 8802, 16, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wmanIf2mBsMsPagedTable.setStatus("current")
_WmanIf2mBsMsPagedEntry_Object = MibTableRow
wmanIf2mBsMsPagedEntry = _WmanIf2mBsMsPagedEntry_Object(
    (1, 0, 8802, 16, 3, 1, 4, 2, 1)
)
wmanIf2mBsMsPagedEntry.setIndexNames(
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsMsPagedEntry.setStatus("current")
_WmanIf2mBsSsMacAddrHash_Type = WmanIf2mSsMacAddrHash
_WmanIf2mBsSsMacAddrHash_Object = MibTableColumn
wmanIf2mBsSsMacAddrHash = _WmanIf2mBsSsMacAddrHash_Object(
    (1, 0, 8802, 16, 3, 1, 4, 2, 1, 1),
    _WmanIf2mBsSsMacAddrHash_Type()
)
wmanIf2mBsSsMacAddrHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsMacAddrHash.setStatus("current")
_WmanIf2mBsPagingActionCode_Type = WmanIf2mPagingAction
_WmanIf2mBsPagingActionCode_Object = MibTableColumn
wmanIf2mBsPagingActionCode = _WmanIf2mBsPagingActionCode_Object(
    (1, 0, 8802, 16, 3, 1, 4, 2, 1, 2),
    _WmanIf2mBsPagingActionCode_Type()
)
wmanIf2mBsPagingActionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingActionCode.setStatus("current")


class _WmanIf2mBsCdmaCode_Type(Integer32):
    """Custom type wmanIf2mBsCdmaCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsCdmaCode_Type.__name__ = "Integer32"
_WmanIf2mBsCdmaCode_Object = MibTableColumn
wmanIf2mBsCdmaCode = _WmanIf2mBsCdmaCode_Object(
    (1, 0, 8802, 16, 3, 1, 4, 2, 1, 3),
    _WmanIf2mBsCdmaCode_Type()
)
wmanIf2mBsCdmaCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCdmaCode.setStatus("current")


class _WmanIf2mBsTransmitOpportunity_Type(Integer32):
    """Custom type wmanIf2mBsTransmitOpportunity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsTransmitOpportunity_Type.__name__ = "Integer32"
_WmanIf2mBsTransmitOpportunity_Object = MibTableColumn
wmanIf2mBsTransmitOpportunity = _WmanIf2mBsTransmitOpportunity_Object(
    (1, 0, 8802, 16, 3, 1, 4, 2, 1, 4),
    _WmanIf2mBsTransmitOpportunity_Type()
)
wmanIf2mBsTransmitOpportunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsTransmitOpportunity.setStatus("current")
_WmanIf2mBsPagingGroupsTable_Object = MibTable
wmanIf2mBsPagingGroupsTable = _WmanIf2mBsPagingGroupsTable_Object(
    (1, 0, 8802, 16, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wmanIf2mBsPagingGroupsTable.setStatus("current")
_WmanIf2mBsPagingGroupsEntry_Object = MibTableRow
wmanIf2mBsPagingGroupsEntry = _WmanIf2mBsPagingGroupsEntry_Object(
    (1, 0, 8802, 16, 3, 1, 4, 3, 1)
)
wmanIf2mBsPagingGroupsEntry.setIndexNames(
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsPagingGroupListId"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsPagingGroupId"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsPagingGroupsEntry.setStatus("current")


class _WmanIf2mBsPagingGroupListId_Type(Integer32):
    """Custom type wmanIf2mBsPagingGroupListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsPagingGroupListId_Type.__name__ = "Integer32"
_WmanIf2mBsPagingGroupListId_Object = MibTableColumn
wmanIf2mBsPagingGroupListId = _WmanIf2mBsPagingGroupListId_Object(
    (1, 0, 8802, 16, 3, 1, 4, 3, 1, 1),
    _WmanIf2mBsPagingGroupListId_Type()
)
wmanIf2mBsPagingGroupListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingGroupListId.setStatus("current")


class _WmanIf2mBsPagingGroupId_Type(Integer32):
    """Custom type wmanIf2mBsPagingGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsPagingGroupId_Type.__name__ = "Integer32"
_WmanIf2mBsPagingGroupId_Object = MibTableColumn
wmanIf2mBsPagingGroupId = _WmanIf2mBsPagingGroupId_Object(
    (1, 0, 8802, 16, 3, 1, 4, 3, 1, 2),
    _WmanIf2mBsPagingGroupId_Type()
)
wmanIf2mBsPagingGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsPagingGroupId.setStatus("current")
_WmanIf2BsPagingGroupsRowStatus_Type = RowStatus
_WmanIf2BsPagingGroupsRowStatus_Object = MibTableColumn
wmanIf2BsPagingGroupsRowStatus = _WmanIf2BsPagingGroupsRowStatus_Object(
    (1, 0, 8802, 16, 3, 1, 4, 3, 1, 3),
    _WmanIf2BsPagingGroupsRowStatus_Type()
)
wmanIf2BsPagingGroupsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2BsPagingGroupsRowStatus.setStatus("current")
_WmanIf2mBsServiceFlow_ObjectIdentity = ObjectIdentity
wmanIf2mBsServiceFlow = _WmanIf2mBsServiceFlow_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1, 5)
)
_WmanIf2mBsServiceFlowTable_Object = MibTable
wmanIf2mBsServiceFlowTable = _WmanIf2mBsServiceFlowTable_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wmanIf2mBsServiceFlowTable.setStatus("current")
_WmanIf2mBsServiceFlowEntry_Object = MibTableRow
wmanIf2mBsServiceFlowEntry = _WmanIf2mBsServiceFlowEntry_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1)
)
wmanIf2mBsServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsSfId"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsServiceFlowEntry.setStatus("current")
_WmanIf2mBsSsMacAddress_Type = MacAddress
_WmanIf2mBsSsMacAddress_Object = MibTableColumn
wmanIf2mBsSsMacAddress = _WmanIf2mBsSsMacAddress_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 1),
    _WmanIf2mBsSsMacAddress_Type()
)
wmanIf2mBsSsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsSsMacAddress.setStatus("current")
_WmanIf2mBsServiceFlowDirection_Type = WmanIf2mSfDirection
_WmanIf2mBsServiceFlowDirection_Object = MibTableColumn
wmanIf2mBsServiceFlowDirection = _WmanIf2mBsServiceFlowDirection_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 2),
    _WmanIf2mBsServiceFlowDirection_Type()
)
wmanIf2mBsServiceFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsServiceFlowDirection.setStatus("current")
_WmanIf2mBsProvisionedGlobalServiceClass_Type = WmanIf2mGlobalSrvClass
_WmanIf2mBsProvisionedGlobalServiceClass_Object = MibTableColumn
wmanIf2mBsProvisionedGlobalServiceClass = _WmanIf2mBsProvisionedGlobalServiceClass_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 3),
    _WmanIf2mBsProvisionedGlobalServiceClass_Type()
)
wmanIf2mBsProvisionedGlobalServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsProvisionedGlobalServiceClass.setStatus("current")
_WmanIf2mBsAdmittedGlobalServiceClass_Type = WmanIf2mGlobalSrvClass
_WmanIf2mBsAdmittedGlobalServiceClass_Object = MibTableColumn
wmanIf2mBsAdmittedGlobalServiceClass = _WmanIf2mBsAdmittedGlobalServiceClass_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 4),
    _WmanIf2mBsAdmittedGlobalServiceClass_Type()
)
wmanIf2mBsAdmittedGlobalServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsAdmittedGlobalServiceClass.setStatus("current")
_WmanIf2mBsActiveGlobalServiceClass_Type = WmanIf2mGlobalSrvClass
_WmanIf2mBsActiveGlobalServiceClass_Object = MibTableColumn
wmanIf2mBsActiveGlobalServiceClass = _WmanIf2mBsActiveGlobalServiceClass_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 5),
    _WmanIf2mBsActiveGlobalServiceClass_Type()
)
wmanIf2mBsActiveGlobalServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsActiveGlobalServiceClass.setStatus("current")


class _WmanIf2mBsProvisionedQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBsProvisionedQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsProvisionedQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBsProvisionedQoSProfileIndex_Object = MibTableColumn
wmanIf2mBsProvisionedQoSProfileIndex = _WmanIf2mBsProvisionedQoSProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 6),
    _WmanIf2mBsProvisionedQoSProfileIndex_Type()
)
wmanIf2mBsProvisionedQoSProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsProvisionedQoSProfileIndex.setStatus("current")


class _WmanIf2mBsAdmittedQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBsAdmittedQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsAdmittedQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBsAdmittedQoSProfileIndex_Object = MibTableColumn
wmanIf2mBsAdmittedQoSProfileIndex = _WmanIf2mBsAdmittedQoSProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 7),
    _WmanIf2mBsAdmittedQoSProfileIndex_Type()
)
wmanIf2mBsAdmittedQoSProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsAdmittedQoSProfileIndex.setStatus("current")


class _WmanIf2mBsActiveQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBsActiveQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsActiveQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBsActiveQoSProfileIndex_Object = MibTableColumn
wmanIf2mBsActiveQoSProfileIndex = _WmanIf2mBsActiveQoSProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 8),
    _WmanIf2mBsActiveQoSProfileIndex_Type()
)
wmanIf2mBsActiveQoSProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsActiveQoSProfileIndex.setStatus("current")


class _WmanIf2mBsArqAttributeIndex_Type(Integer32):
    """Custom type wmanIf2mBsArqAttributeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsArqAttributeIndex_Type.__name__ = "Integer32"
_WmanIf2mBsArqAttributeIndex_Object = MibTableColumn
wmanIf2mBsArqAttributeIndex = _WmanIf2mBsArqAttributeIndex_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 9),
    _WmanIf2mBsArqAttributeIndex_Type()
)
wmanIf2mBsArqAttributeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqAttributeIndex.setStatus("current")
_WmanIf2mBsServiceFlowState_Type = WmanIf2mSfState
_WmanIf2mBsServiceFlowState_Object = MibTableColumn
wmanIf2mBsServiceFlowState = _WmanIf2mBsServiceFlowState_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 10),
    _WmanIf2mBsServiceFlowState_Type()
)
wmanIf2mBsServiceFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsServiceFlowState.setStatus("current")


class _WmanIf2mBsCid_Type(Integer32):
    """Custom type wmanIf2mBsCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsCid_Type.__name__ = "Integer32"
_WmanIf2mBsCid_Object = MibTableColumn
wmanIf2mBsCid = _WmanIf2mBsCid_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 11),
    _WmanIf2mBsCid_Type()
)
wmanIf2mBsCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCid.setStatus("current")
_WmanIf2mBsSfCsSpecification_Type = WmanIf2mCsSpecification
_WmanIf2mBsSfCsSpecification_Object = MibTableColumn
wmanIf2mBsSfCsSpecification = _WmanIf2mBsSfCsSpecification_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 12),
    _WmanIf2mBsSfCsSpecification_Type()
)
wmanIf2mBsSfCsSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSfCsSpecification.setStatus("current")
_WmanIf2mBsSfMinTolerableTrafficRate_Type = Unsigned32
_WmanIf2mBsSfMinTolerableTrafficRate_Object = MibTableColumn
wmanIf2mBsSfMinTolerableTrafficRate = _WmanIf2mBsSfMinTolerableTrafficRate_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 13),
    _WmanIf2mBsSfMinTolerableTrafficRate_Type()
)
wmanIf2mBsSfMinTolerableTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSfMinTolerableTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSfMinTolerableTrafficRate.setUnits("bps")
_WmanIf2mBsSfReqTxPolicy_Type = WmanIf2mReqTxPolicy
_WmanIf2mBsSfReqTxPolicy_Object = MibTableColumn
wmanIf2mBsSfReqTxPolicy = _WmanIf2mBsSfReqTxPolicy_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 14),
    _WmanIf2mBsSfReqTxPolicy_Type()
)
wmanIf2mBsSfReqTxPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSfReqTxPolicy.setStatus("current")


class _WmanIf2mBsSfTargetSaid_Type(Integer32):
    """Custom type wmanIf2mBsSfTargetSaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsSfTargetSaid_Type.__name__ = "Integer32"
_WmanIf2mBsSfTargetSaid_Object = MibTableColumn
wmanIf2mBsSfTargetSaid = _WmanIf2mBsSfTargetSaid_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 15),
    _WmanIf2mBsSfTargetSaid_Type()
)
wmanIf2mBsSfTargetSaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSfTargetSaid.setStatus("current")
_WmanIf2mBsSfEstablishTime_Type = TimeStamp
_WmanIf2mBsSfEstablishTime_Object = MibTableColumn
wmanIf2mBsSfEstablishTime = _WmanIf2mBsSfEstablishTime_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 16),
    _WmanIf2mBsSfEstablishTime_Type()
)
wmanIf2mBsSfEstablishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSfEstablishTime.setStatus("current")
_WmanIf2mBsSfTerminateTime_Type = TimeStamp
_WmanIf2mBsSfTerminateTime_Object = MibTableColumn
wmanIf2mBsSfTerminateTime = _WmanIf2mBsSfTerminateTime_Object(
    (1, 0, 8802, 16, 3, 1, 5, 1, 1, 17),
    _WmanIf2mBsSfTerminateTime_Type()
)
wmanIf2mBsSfTerminateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSfTerminateTime.setStatus("current")
_WmanIf2mBsClassifierRuleTable_Object = MibTable
wmanIf2mBsClassifierRuleTable = _WmanIf2mBsClassifierRuleTable_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleTable.setStatus("current")
_WmanIf2mBsClassifierRuleEntry_Object = MibTableRow
wmanIf2mBsClassifierRuleEntry = _WmanIf2mBsClassifierRuleEntry_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1)
)
wmanIf2mBsClassifierRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsSfId"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsClassifierRuleId"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleEntry.setStatus("current")


class _WmanIf2mBsClassifierRuleId_Type(Unsigned32):
    """Custom type wmanIf2mBsClassifierRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2mBsClassifierRuleId_Type.__name__ = "Unsigned32"
_WmanIf2mBsClassifierRuleId_Object = MibTableColumn
wmanIf2mBsClassifierRuleId = _WmanIf2mBsClassifierRuleId_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 1),
    _WmanIf2mBsClassifierRuleId_Type()
)
wmanIf2mBsClassifierRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleId.setStatus("current")


class _WmanIf2mBsClassifierRulePriority_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRulePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsClassifierRulePriority_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRulePriority_Object = MibTableColumn
wmanIf2mBsClassifierRulePriority = _WmanIf2mBsClassifierRulePriority_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 2),
    _WmanIf2mBsClassifierRulePriority_Type()
)
wmanIf2mBsClassifierRulePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRulePriority.setStatus("current")


class _WmanIf2mBsClassifierRuleIpTosLow_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleIpTosLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsClassifierRuleIpTosLow_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleIpTosLow_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpTosLow = _WmanIf2mBsClassifierRuleIpTosLow_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 3),
    _WmanIf2mBsClassifierRuleIpTosLow_Type()
)
wmanIf2mBsClassifierRuleIpTosLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpTosLow.setStatus("current")


class _WmanIf2mBsClassifierRuleIpTosHigh_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleIpTosHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsClassifierRuleIpTosHigh_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleIpTosHigh_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpTosHigh = _WmanIf2mBsClassifierRuleIpTosHigh_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 4),
    _WmanIf2mBsClassifierRuleIpTosHigh_Type()
)
wmanIf2mBsClassifierRuleIpTosHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpTosHigh.setStatus("current")


class _WmanIf2mBsClassifierRuleIpTosMask_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsClassifierRuleIpTosMask_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleIpTosMask_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpTosMask = _WmanIf2mBsClassifierRuleIpTosMask_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 5),
    _WmanIf2mBsClassifierRuleIpTosMask_Type()
)
wmanIf2mBsClassifierRuleIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpTosMask.setStatus("current")


class _WmanIf2mBsClassifierRuleIpProtocol_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsClassifierRuleIpProtocol_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleIpProtocol_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpProtocol = _WmanIf2mBsClassifierRuleIpProtocol_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 6),
    _WmanIf2mBsClassifierRuleIpProtocol_Type()
)
wmanIf2mBsClassifierRuleIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpProtocol.setStatus("current")
_WmanIf2mBsClassifierRuleIpSrcAddr_Type = InetAddress
_WmanIf2mBsClassifierRuleIpSrcAddr_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpSrcAddr = _WmanIf2mBsClassifierRuleIpSrcAddr_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 7),
    _WmanIf2mBsClassifierRuleIpSrcAddr_Type()
)
wmanIf2mBsClassifierRuleIpSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpSrcAddr.setStatus("current")
_WmanIf2mBsClassifierRuleIpSrcMask_Type = InetAddress
_WmanIf2mBsClassifierRuleIpSrcMask_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpSrcMask = _WmanIf2mBsClassifierRuleIpSrcMask_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 8),
    _WmanIf2mBsClassifierRuleIpSrcMask_Type()
)
wmanIf2mBsClassifierRuleIpSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpSrcMask.setStatus("current")
_WmanIf2mBsClassifierRuleIpDestAddr_Type = InetAddress
_WmanIf2mBsClassifierRuleIpDestAddr_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpDestAddr = _WmanIf2mBsClassifierRuleIpDestAddr_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 9),
    _WmanIf2mBsClassifierRuleIpDestAddr_Type()
)
wmanIf2mBsClassifierRuleIpDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpDestAddr.setStatus("current")
_WmanIf2mBsClassifierRuleIpDestMask_Type = InetAddress
_WmanIf2mBsClassifierRuleIpDestMask_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpDestMask = _WmanIf2mBsClassifierRuleIpDestMask_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 10),
    _WmanIf2mBsClassifierRuleIpDestMask_Type()
)
wmanIf2mBsClassifierRuleIpDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpDestMask.setStatus("current")


class _WmanIf2mBsClassifierRuleSrcPortStart_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleSrcPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsClassifierRuleSrcPortStart_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleSrcPortStart_Object = MibTableColumn
wmanIf2mBsClassifierRuleSrcPortStart = _WmanIf2mBsClassifierRuleSrcPortStart_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 11),
    _WmanIf2mBsClassifierRuleSrcPortStart_Type()
)
wmanIf2mBsClassifierRuleSrcPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleSrcPortStart.setStatus("current")


class _WmanIf2mBsClassifierRuleSrcPortEnd_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleSrcPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsClassifierRuleSrcPortEnd_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleSrcPortEnd_Object = MibTableColumn
wmanIf2mBsClassifierRuleSrcPortEnd = _WmanIf2mBsClassifierRuleSrcPortEnd_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 12),
    _WmanIf2mBsClassifierRuleSrcPortEnd_Type()
)
wmanIf2mBsClassifierRuleSrcPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleSrcPortEnd.setStatus("current")


class _WmanIf2mBsClassifierRuleDestPortStart_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsClassifierRuleDestPortStart_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleDestPortStart_Object = MibTableColumn
wmanIf2mBsClassifierRuleDestPortStart = _WmanIf2mBsClassifierRuleDestPortStart_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 13),
    _WmanIf2mBsClassifierRuleDestPortStart_Type()
)
wmanIf2mBsClassifierRuleDestPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleDestPortStart.setStatus("current")


class _WmanIf2mBsClassifierRuleDestPortEnd_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsClassifierRuleDestPortEnd_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleDestPortEnd_Object = MibTableColumn
wmanIf2mBsClassifierRuleDestPortEnd = _WmanIf2mBsClassifierRuleDestPortEnd_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 14),
    _WmanIf2mBsClassifierRuleDestPortEnd_Type()
)
wmanIf2mBsClassifierRuleDestPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleDestPortEnd.setStatus("current")
_WmanIf2mBsClassifierRuleDestMacAddr_Type = MacAddress
_WmanIf2mBsClassifierRuleDestMacAddr_Object = MibTableColumn
wmanIf2mBsClassifierRuleDestMacAddr = _WmanIf2mBsClassifierRuleDestMacAddr_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 15),
    _WmanIf2mBsClassifierRuleDestMacAddr_Type()
)
wmanIf2mBsClassifierRuleDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleDestMacAddr.setStatus("current")
_WmanIf2mBsClassifierRuleDestMacMask_Type = MacAddress
_WmanIf2mBsClassifierRuleDestMacMask_Object = MibTableColumn
wmanIf2mBsClassifierRuleDestMacMask = _WmanIf2mBsClassifierRuleDestMacMask_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 16),
    _WmanIf2mBsClassifierRuleDestMacMask_Type()
)
wmanIf2mBsClassifierRuleDestMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleDestMacMask.setStatus("current")
_WmanIf2mBsClassifierRuleSrcMacAddr_Type = MacAddress
_WmanIf2mBsClassifierRuleSrcMacAddr_Object = MibTableColumn
wmanIf2mBsClassifierRuleSrcMacAddr = _WmanIf2mBsClassifierRuleSrcMacAddr_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 17),
    _WmanIf2mBsClassifierRuleSrcMacAddr_Type()
)
wmanIf2mBsClassifierRuleSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleSrcMacAddr.setStatus("current")
_WmanIf2mBsClassifierRuleSrcMacMask_Type = MacAddress
_WmanIf2mBsClassifierRuleSrcMacMask_Object = MibTableColumn
wmanIf2mBsClassifierRuleSrcMacMask = _WmanIf2mBsClassifierRuleSrcMacMask_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 18),
    _WmanIf2mBsClassifierRuleSrcMacMask_Type()
)
wmanIf2mBsClassifierRuleSrcMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleSrcMacMask.setStatus("current")


class _WmanIf2mBsClassifierRuleEnetType_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleEnetType based on Integer32"""
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


_WmanIf2mBsClassifierRuleEnetType_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleEnetType_Object = MibTableColumn
wmanIf2mBsClassifierRuleEnetType = _WmanIf2mBsClassifierRuleEnetType_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 19),
    _WmanIf2mBsClassifierRuleEnetType_Type()
)
wmanIf2mBsClassifierRuleEnetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleEnetType.setStatus("current")


class _WmanIf2mBsClassifierRuleEnetProtocol_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsClassifierRuleEnetProtocol_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleEnetProtocol_Object = MibTableColumn
wmanIf2mBsClassifierRuleEnetProtocol = _WmanIf2mBsClassifierRuleEnetProtocol_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 20),
    _WmanIf2mBsClassifierRuleEnetProtocol_Type()
)
wmanIf2mBsClassifierRuleEnetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleEnetProtocol.setStatus("current")


class _WmanIf2mBsClassifierRuleUserPriLow_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsClassifierRuleUserPriLow_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleUserPriLow_Object = MibTableColumn
wmanIf2mBsClassifierRuleUserPriLow = _WmanIf2mBsClassifierRuleUserPriLow_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 21),
    _WmanIf2mBsClassifierRuleUserPriLow_Type()
)
wmanIf2mBsClassifierRuleUserPriLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleUserPriLow.setStatus("current")


class _WmanIf2mBsClassifierRuleUserPriHigh_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsClassifierRuleUserPriHigh_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleUserPriHigh_Object = MibTableColumn
wmanIf2mBsClassifierRuleUserPriHigh = _WmanIf2mBsClassifierRuleUserPriHigh_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 22),
    _WmanIf2mBsClassifierRuleUserPriHigh_Type()
)
wmanIf2mBsClassifierRuleUserPriHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleUserPriHigh.setStatus("current")


class _WmanIf2mBsClassifierRuleVlanId_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WmanIf2mBsClassifierRuleVlanId_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleVlanId_Object = MibTableColumn
wmanIf2mBsClassifierRuleVlanId = _WmanIf2mBsClassifierRuleVlanId_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 23),
    _WmanIf2mBsClassifierRuleVlanId_Type()
)
wmanIf2mBsClassifierRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleVlanId.setStatus("current")
_WmanIf2mBsClassifierRuleIpv6FlowLabel_Type = WmanIf2mIpv6FlowLabel
_WmanIf2mBsClassifierRuleIpv6FlowLabel_Object = MibTableColumn
wmanIf2mBsClassifierRuleIpv6FlowLabel = _WmanIf2mBsClassifierRuleIpv6FlowLabel_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 24),
    _WmanIf2mBsClassifierRuleIpv6FlowLabel_Type()
)
wmanIf2mBsClassifierRuleIpv6FlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleIpv6FlowLabel.setStatus("current")
_WmanIf2mBsClassifierRulePkts_Type = Counter64
_WmanIf2mBsClassifierRulePkts_Object = MibTableColumn
wmanIf2mBsClassifierRulePkts = _WmanIf2mBsClassifierRulePkts_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 25),
    _WmanIf2mBsClassifierRulePkts_Type()
)
wmanIf2mBsClassifierRulePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRulePkts.setStatus("current")
_WmanIf2mBsClassifierRuleBitMap_Type = WmanIf2mClassifierBitMap
_WmanIf2mBsClassifierRuleBitMap_Object = MibTableColumn
wmanIf2mBsClassifierRuleBitMap = _WmanIf2mBsClassifierRuleBitMap_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 26),
    _WmanIf2mBsClassifierRuleBitMap_Type()
)
wmanIf2mBsClassifierRuleBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleBitMap.setStatus("current")


class _WmanIf2mBsClassifierRuleAssociatedPhsi_Type(Integer32):
    """Custom type wmanIf2mBsClassifierRuleAssociatedPhsi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2mBsClassifierRuleAssociatedPhsi_Type.__name__ = "Integer32"
_WmanIf2mBsClassifierRuleAssociatedPhsi_Object = MibTableColumn
wmanIf2mBsClassifierRuleAssociatedPhsi = _WmanIf2mBsClassifierRuleAssociatedPhsi_Object(
    (1, 0, 8802, 16, 3, 1, 5, 2, 1, 27),
    _WmanIf2mBsClassifierRuleAssociatedPhsi_Type()
)
wmanIf2mBsClassifierRuleAssociatedPhsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsClassifierRuleAssociatedPhsi.setStatus("current")
_WmanIf2mBsPhsRuleTable_Object = MibTable
wmanIf2mBsPhsRuleTable = _WmanIf2mBsPhsRuleTable_Object(
    (1, 0, 8802, 16, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wmanIf2mBsPhsRuleTable.setStatus("current")
_WmanIf2mBsPhsRuleEntry_Object = MibTableRow
wmanIf2mBsPhsRuleEntry = _WmanIf2mBsPhsRuleEntry_Object(
    (1, 0, 8802, 16, 3, 1, 5, 3, 1)
)
wmanIf2mBsPhsRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsSfId"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsPhsRuleId"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsPhsRuleEntry.setStatus("current")


class _WmanIf2mBsPhsRuleId_Type(Integer32):
    """Custom type wmanIf2mBsPhsRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2mBsPhsRuleId_Type.__name__ = "Integer32"
_WmanIf2mBsPhsRuleId_Object = MibTableColumn
wmanIf2mBsPhsRuleId = _WmanIf2mBsPhsRuleId_Object(
    (1, 0, 8802, 16, 3, 1, 5, 3, 1, 1),
    _WmanIf2mBsPhsRuleId_Type()
)
wmanIf2mBsPhsRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsPhsRuleId.setStatus("current")


class _WmanIf2mBsPhsRulePhsField_Type(OctetString):
    """Custom type wmanIf2mBsPhsRulePhsField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2mBsPhsRulePhsField_Type.__name__ = "OctetString"
_WmanIf2mBsPhsRulePhsField_Object = MibTableColumn
wmanIf2mBsPhsRulePhsField = _WmanIf2mBsPhsRulePhsField_Object(
    (1, 0, 8802, 16, 3, 1, 5, 3, 1, 2),
    _WmanIf2mBsPhsRulePhsField_Type()
)
wmanIf2mBsPhsRulePhsField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsPhsRulePhsField.setStatus("current")


class _WmanIf2mBsPhsRulePhsMask_Type(OctetString):
    """Custom type wmanIf2mBsPhsRulePhsMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2mBsPhsRulePhsMask_Type.__name__ = "OctetString"
_WmanIf2mBsPhsRulePhsMask_Object = MibTableColumn
wmanIf2mBsPhsRulePhsMask = _WmanIf2mBsPhsRulePhsMask_Object(
    (1, 0, 8802, 16, 3, 1, 5, 3, 1, 3),
    _WmanIf2mBsPhsRulePhsMask_Type()
)
wmanIf2mBsPhsRulePhsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsPhsRulePhsMask.setStatus("current")


class _WmanIf2mBsPhsRulePhsSize_Type(Integer32):
    """Custom type wmanIf2mBsPhsRulePhsSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsPhsRulePhsSize_Type.__name__ = "Integer32"
_WmanIf2mBsPhsRulePhsSize_Object = MibTableColumn
wmanIf2mBsPhsRulePhsSize = _WmanIf2mBsPhsRulePhsSize_Object(
    (1, 0, 8802, 16, 3, 1, 5, 3, 1, 4),
    _WmanIf2mBsPhsRulePhsSize_Type()
)
wmanIf2mBsPhsRulePhsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsPhsRulePhsSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsPhsRulePhsSize.setUnits("byte")


class _WmanIf2mBsPhsRulePhsVerify_Type(WmanIf2mPhsRuleVerify):
    """Custom type wmanIf2mBsPhsRulePhsVerify based on WmanIf2mPhsRuleVerify"""
    defaultValue = 0


_WmanIf2mBsPhsRulePhsVerify_Type.__name__ = "WmanIf2mPhsRuleVerify"
_WmanIf2mBsPhsRulePhsVerify_Object = MibTableColumn
wmanIf2mBsPhsRulePhsVerify = _WmanIf2mBsPhsRulePhsVerify_Object(
    (1, 0, 8802, 16, 3, 1, 5, 3, 1, 5),
    _WmanIf2mBsPhsRulePhsVerify_Type()
)
wmanIf2mBsPhsRulePhsVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsPhsRulePhsVerify.setStatus("current")
_WmanIf2mBsQoSProfileTable_Object = MibTable
wmanIf2mBsQoSProfileTable = _WmanIf2mBsQoSProfileTable_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4)
)
if mibBuilder.loadTexts:
    wmanIf2mBsQoSProfileTable.setStatus("current")
_WmanIf2mBsQoSProfileEntry_Object = MibTableRow
wmanIf2mBsQoSProfileEntry = _WmanIf2mBsQoSProfileEntry_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1)
)
wmanIf2mBsQoSProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsQoSProfileIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsQoSProfileEntry.setStatus("current")


class _WmanIf2mBsQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2mBsQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2mBsQoSProfileIndex_Object = MibTableColumn
wmanIf2mBsQoSProfileIndex = _WmanIf2mBsQoSProfileIndex_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 1),
    _WmanIf2mBsQoSProfileIndex_Type()
)
wmanIf2mBsQoSProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsQoSProfileIndex.setStatus("current")


class _WmanIf2mBsQosServiceClassName_Type(OctetString):
    """Custom type wmanIf2mBsQosServiceClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_WmanIf2mBsQosServiceClassName_Type.__name__ = "OctetString"
_WmanIf2mBsQosServiceClassName_Object = MibTableColumn
wmanIf2mBsQosServiceClassName = _WmanIf2mBsQosServiceClassName_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 2),
    _WmanIf2mBsQosServiceClassName_Type()
)
wmanIf2mBsQosServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosServiceClassName.setStatus("current")


class _WmanIf2mBsQosUlGrantScheduleType_Type(WmanIf2mSchedulingType):
    """Custom type wmanIf2mBsQosUlGrantScheduleType based on WmanIf2mSchedulingType"""
    defaultValue = 2


_WmanIf2mBsQosUlGrantScheduleType_Type.__name__ = "WmanIf2mSchedulingType"
_WmanIf2mBsQosUlGrantScheduleType_Object = MibTableColumn
wmanIf2mBsQosUlGrantScheduleType = _WmanIf2mBsQosUlGrantScheduleType_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 3),
    _WmanIf2mBsQosUlGrantScheduleType_Type()
)
wmanIf2mBsQosUlGrantScheduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosUlGrantScheduleType.setStatus("current")


class _WmanIf2mBsQosTrafficPriority_Type(Integer32):
    """Custom type wmanIf2mBsQosTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2mBsQosTrafficPriority_Type.__name__ = "Integer32"
_WmanIf2mBsQosTrafficPriority_Object = MibTableColumn
wmanIf2mBsQosTrafficPriority = _WmanIf2mBsQosTrafficPriority_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 4),
    _WmanIf2mBsQosTrafficPriority_Type()
)
wmanIf2mBsQosTrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosTrafficPriority.setStatus("current")
_WmanIf2mBsQosMaximumSustainedRate_Type = Unsigned32
_WmanIf2mBsQosMaximumSustainedRate_Object = MibTableColumn
wmanIf2mBsQosMaximumSustainedRate = _WmanIf2mBsQosMaximumSustainedRate_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 5),
    _WmanIf2mBsQosMaximumSustainedRate_Type()
)
wmanIf2mBsQosMaximumSustainedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosMaximumSustainedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsQosMaximumSustainedRate.setUnits("bps")
_WmanIf2mBsQosMinimumReservedRate_Type = Unsigned32
_WmanIf2mBsQosMinimumReservedRate_Object = MibTableColumn
wmanIf2mBsQosMinimumReservedRate = _WmanIf2mBsQosMinimumReservedRate_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 6),
    _WmanIf2mBsQosMinimumReservedRate_Type()
)
wmanIf2mBsQosMinimumReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosMinimumReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsQosMinimumReservedRate.setUnits("bps")
_WmanIf2mBsQosMaximumTrafficBurst_Type = Unsigned32
_WmanIf2mBsQosMaximumTrafficBurst_Object = MibTableColumn
wmanIf2mBsQosMaximumTrafficBurst = _WmanIf2mBsQosMaximumTrafficBurst_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 7),
    _WmanIf2mBsQosMaximumTrafficBurst_Type()
)
wmanIf2mBsQosMaximumTrafficBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosMaximumTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsQosMaximumTrafficBurst.setUnits("byte")
_WmanIf2mBsQosToleratedJitter_Type = Unsigned32
_WmanIf2mBsQosToleratedJitter_Object = MibTableColumn
wmanIf2mBsQosToleratedJitter = _WmanIf2mBsQosToleratedJitter_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 8),
    _WmanIf2mBsQosToleratedJitter_Type()
)
wmanIf2mBsQosToleratedJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosToleratedJitter.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsQosToleratedJitter.setUnits("millisecond")
_WmanIf2mBsQosMaxLatency_Type = Unsigned32
_WmanIf2mBsQosMaxLatency_Object = MibTableColumn
wmanIf2mBsQosMaxLatency = _WmanIf2mBsQosMaxLatency_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 9),
    _WmanIf2mBsQosMaxLatency_Type()
)
wmanIf2mBsQosMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsQosMaxLatency.setUnits("millisecond")
_WmanIf2mBsQosUnsolicitedGrantInterval_Type = Unsigned32
_WmanIf2mBsQosUnsolicitedGrantInterval_Object = MibTableColumn
wmanIf2mBsQosUnsolicitedGrantInterval = _WmanIf2mBsQosUnsolicitedGrantInterval_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 10),
    _WmanIf2mBsQosUnsolicitedGrantInterval_Type()
)
wmanIf2mBsQosUnsolicitedGrantInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosUnsolicitedGrantInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsQosUnsolicitedGrantInterval.setUnits("millisecond")
_WmanIf2mBsQosSduSize_Type = Unsigned32
_WmanIf2mBsQosSduSize_Object = MibTableColumn
wmanIf2mBsQosSduSize = _WmanIf2mBsQosSduSize_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 11),
    _WmanIf2mBsQosSduSize_Type()
)
wmanIf2mBsQosSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosSduSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsQosSduSize.setUnits("byte")
_WmanIf2mBsQosUnsolicitedPollInterval_Type = Unsigned32
_WmanIf2mBsQosUnsolicitedPollInterval_Object = MibTableColumn
wmanIf2mBsQosUnsolicitedPollInterval = _WmanIf2mBsQosUnsolicitedPollInterval_Object(
    (1, 0, 8802, 16, 3, 1, 5, 4, 1, 12),
    _WmanIf2mBsQosUnsolicitedPollInterval_Type()
)
wmanIf2mBsQosUnsolicitedPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsQosUnsolicitedPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsQosUnsolicitedPollInterval.setUnits("millisecond")
_WmanIf2mBsArqAttributeTable_Object = MibTable
wmanIf2mBsArqAttributeTable = _WmanIf2mBsArqAttributeTable_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5)
)
if mibBuilder.loadTexts:
    wmanIf2mBsArqAttributeTable.setStatus("current")
_WmanIf2mBsArqAttributeEntry_Object = MibTableRow
wmanIf2mBsArqAttributeEntry = _WmanIf2mBsArqAttributeEntry_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1)
)
wmanIf2mBsArqAttributeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsArqIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsArqAttributeEntry.setStatus("current")


class _WmanIf2mBsArqIndex_Type(Integer32):
    """Custom type wmanIf2mBsArqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2mBsArqIndex_Type.__name__ = "Integer32"
_WmanIf2mBsArqIndex_Object = MibTableColumn
wmanIf2mBsArqIndex = _WmanIf2mBsArqIndex_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 1),
    _WmanIf2mBsArqIndex_Type()
)
wmanIf2mBsArqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsArqIndex.setStatus("current")
_WmanIf2mBsArqEnable_Type = TruthValue
_WmanIf2mBsArqEnable_Object = MibTableColumn
wmanIf2mBsArqEnable = _WmanIf2mBsArqEnable_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 2),
    _WmanIf2mBsArqEnable_Type()
)
wmanIf2mBsArqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqEnable.setStatus("current")


class _WmanIf2mBsArqWindowSize_Type(Integer32):
    """Custom type wmanIf2mBsArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIf2mBsArqWindowSize_Type.__name__ = "Integer32"
_WmanIf2mBsArqWindowSize_Object = MibTableColumn
wmanIf2mBsArqWindowSize = _WmanIf2mBsArqWindowSize_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 3),
    _WmanIf2mBsArqWindowSize_Type()
)
wmanIf2mBsArqWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqWindowSize.setStatus("current")


class _WmanIf2mBsArqBlockLifetime_Type(Integer32):
    """Custom type wmanIf2mBsArqBlockLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIf2mBsArqBlockLifetime_Object = MibTableColumn
wmanIf2mBsArqBlockLifetime = _WmanIf2mBsArqBlockLifetime_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 4),
    _WmanIf2mBsArqBlockLifetime_Type()
)
wmanIf2mBsArqBlockLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsArqBlockLifetime.setUnits("10 us")


class _WmanIf2mBsArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIf2mBsArqSyncLossTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIf2mBsArqSyncLossTimeout_Object = MibTableColumn
wmanIf2mBsArqSyncLossTimeout = _WmanIf2mBsArqSyncLossTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 5),
    _WmanIf2mBsArqSyncLossTimeout_Type()
)
wmanIf2mBsArqSyncLossTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsArqSyncLossTimeout.setUnits("10 us")
_WmanIf2mBsArqDeliverInOrder_Type = TruthValue
_WmanIf2mBsArqDeliverInOrder_Object = MibTableColumn
wmanIf2mBsArqDeliverInOrder = _WmanIf2mBsArqDeliverInOrder_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 6),
    _WmanIf2mBsArqDeliverInOrder_Type()
)
wmanIf2mBsArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqDeliverInOrder.setStatus("current")


class _WmanIf2mBsArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIf2mBsArqRxPurgeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIf2mBsArqRxPurgeTimeout_Object = MibTableColumn
wmanIf2mBsArqRxPurgeTimeout = _WmanIf2mBsArqRxPurgeTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 7),
    _WmanIf2mBsArqRxPurgeTimeout_Type()
)
wmanIf2mBsArqRxPurgeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsArqRxPurgeTimeout.setUnits("10 us")


class _WmanIf2mBsArqBlockSize_Type(Integer32):
    """Custom type wmanIf2mBsArqBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2040),
    )


_WmanIf2mBsArqBlockSize_Type.__name__ = "Integer32"
_WmanIf2mBsArqBlockSize_Object = MibTableColumn
wmanIf2mBsArqBlockSize = _WmanIf2mBsArqBlockSize_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 8),
    _WmanIf2mBsArqBlockSize_Type()
)
wmanIf2mBsArqBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsArqBlockSize.setUnits("byte")


class _WmanIf2mBsArqAckProcessingTime_Type(Integer32):
    """Custom type wmanIf2mBsArqAckProcessingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsArqAckProcessingTime_Type.__name__ = "Integer32"
_WmanIf2mBsArqAckProcessingTime_Object = MibTableColumn
wmanIf2mBsArqAckProcessingTime = _WmanIf2mBsArqAckProcessingTime_Object(
    (1, 0, 8802, 16, 3, 1, 5, 5, 1, 9),
    _WmanIf2mBsArqAckProcessingTime_Type()
)
wmanIf2mBsArqAckProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsArqAckProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsArqAckProcessingTime.setUnits("millisecond")
_WmanIf2mBsPm_ObjectIdentity = ObjectIdentity
wmanIf2mBsPm = _WmanIf2mBsPm_ObjectIdentity(
    (1, 0, 8802, 16, 3, 2)
)
_WmanIf2mBsSsSleepModeStatisticsTable_Object = MibTable
wmanIf2mBsSsSleepModeStatisticsTable = _WmanIf2mBsSsSleepModeStatisticsTable_Object(
    (1, 0, 8802, 16, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsSleepModeStatisticsTable.setStatus("current")
_WmanIf2mBsSsSleepModeStatisticsEntry_Object = MibTableRow
wmanIf2mBsSsSleepModeStatisticsEntry = _WmanIf2mBsSsSleepModeStatisticsEntry_Object(
    (1, 0, 8802, 16, 3, 2, 1, 1)
)
wmanIf2mBsSsSleepModeStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsCid"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsStatisticsIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsSsSleepModeStatisticsEntry.setStatus("current")


class _WmanIf2mBsSsStatisticsIndex_Type(Unsigned32):
    """Custom type wmanIf2mBsSsStatisticsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2mBsSsStatisticsIndex_Type.__name__ = "Unsigned32"
_WmanIf2mBsSsStatisticsIndex_Object = MibTableColumn
wmanIf2mBsSsStatisticsIndex = _WmanIf2mBsSsStatisticsIndex_Object(
    (1, 0, 8802, 16, 3, 2, 1, 1, 1),
    _WmanIf2mBsSsStatisticsIndex_Type()
)
wmanIf2mBsSsStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsSsStatisticsIndex.setStatus("current")


class _WmanIf2mBsSsSleepWindowStarted_Type(Unsigned32):
    """Custom type wmanIf2mBsSsSleepWindowStarted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 166777215),
    )


_WmanIf2mBsSsSleepWindowStarted_Type.__name__ = "Unsigned32"
_WmanIf2mBsSsSleepWindowStarted_Object = MibTableColumn
wmanIf2mBsSsSleepWindowStarted = _WmanIf2mBsSsSleepWindowStarted_Object(
    (1, 0, 8802, 16, 3, 2, 1, 1, 2),
    _WmanIf2mBsSsSleepWindowStarted_Type()
)
wmanIf2mBsSsSleepWindowStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsSleepWindowStarted.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsSleepWindowStarted.setUnits("frame")


class _WmanIf2mBsSsListeningWindowStarted_Type(Unsigned32):
    """Custom type wmanIf2mBsSsListeningWindowStarted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 166777215),
    )


_WmanIf2mBsSsListeningWindowStarted_Type.__name__ = "Unsigned32"
_WmanIf2mBsSsListeningWindowStarted_Object = MibTableColumn
wmanIf2mBsSsListeningWindowStarted = _WmanIf2mBsSsListeningWindowStarted_Object(
    (1, 0, 8802, 16, 3, 2, 1, 1, 3),
    _WmanIf2mBsSsListeningWindowStarted_Type()
)
wmanIf2mBsSsListeningWindowStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsListeningWindowStarted.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsSsListeningWindowStarted.setUnits("frame")
_WmanIf2mBsSsPendingMsdu_Type = Integer32
_WmanIf2mBsSsPendingMsdu_Object = MibTableColumn
wmanIf2mBsSsPendingMsdu = _WmanIf2mBsSsPendingMsdu_Object(
    (1, 0, 8802, 16, 3, 2, 1, 1, 4),
    _WmanIf2mBsSsPendingMsdu_Type()
)
wmanIf2mBsSsPendingMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsPendingMsdu.setStatus("current")
_WmanIf2mBsSsSleepWindowTimeStamp_Type = DateAndTime
_WmanIf2mBsSsSleepWindowTimeStamp_Object = MibTableColumn
wmanIf2mBsSsSleepWindowTimeStamp = _WmanIf2mBsSsSleepWindowTimeStamp_Object(
    (1, 0, 8802, 16, 3, 2, 1, 1, 5),
    _WmanIf2mBsSsSleepWindowTimeStamp_Type()
)
wmanIf2mBsSsSleepWindowTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsSsSleepWindowTimeStamp.setStatus("current")
_WmanIf2mBsMobileScanRequestTable_Object = MibTable
wmanIf2mBsMobileScanRequestTable = _WmanIf2mBsMobileScanRequestTable_Object(
    (1, 0, 8802, 16, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIf2mBsMobileScanRequestTable.setStatus("current")
_WmanIf2mBsMobileScanRequestEntry_Object = MibTableRow
wmanIf2mBsMobileScanRequestEntry = _WmanIf2mBsMobileScanRequestEntry_Object(
    (1, 0, 8802, 16, 3, 2, 2, 1)
)
wmanIf2mBsMobileScanRequestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsMobileScanRequestEntry.setStatus("current")


class _WmanIf2mBsScanReqDuration_Type(Integer32):
    """Custom type wmanIf2mBsScanReqDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsScanReqDuration_Type.__name__ = "Integer32"
_WmanIf2mBsScanReqDuration_Object = MibTableColumn
wmanIf2mBsScanReqDuration = _WmanIf2mBsScanReqDuration_Object(
    (1, 0, 8802, 16, 3, 2, 2, 1, 1),
    _WmanIf2mBsScanReqDuration_Type()
)
wmanIf2mBsScanReqDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanReqDuration.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsScanReqDuration.setUnits("frames")


class _WmanIf2mBsScanReqInterleavingInterval_Type(Integer32):
    """Custom type wmanIf2mBsScanReqInterleavingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsScanReqInterleavingInterval_Type.__name__ = "Integer32"
_WmanIf2mBsScanReqInterleavingInterval_Object = MibTableColumn
wmanIf2mBsScanReqInterleavingInterval = _WmanIf2mBsScanReqInterleavingInterval_Object(
    (1, 0, 8802, 16, 3, 2, 2, 1, 2),
    _WmanIf2mBsScanReqInterleavingInterval_Type()
)
wmanIf2mBsScanReqInterleavingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanReqInterleavingInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsScanReqInterleavingInterval.setUnits("frames")


class _WmanIf2mBsScanReqIteration_Type(Integer32):
    """Custom type wmanIf2mBsScanReqIteration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsScanReqIteration_Type.__name__ = "Integer32"
_WmanIf2mBsScanReqIteration_Object = MibTableColumn
wmanIf2mBsScanReqIteration = _WmanIf2mBsScanReqIteration_Object(
    (1, 0, 8802, 16, 3, 2, 2, 1, 3),
    _WmanIf2mBsScanReqIteration_Type()
)
wmanIf2mBsScanReqIteration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanReqIteration.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsScanReqIteration.setUnits("frames")


class _WmanIf2mBsNumOfRecommendedBs_Type(Integer32):
    """Custom type wmanIf2mBsNumOfRecommendedBs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsNumOfRecommendedBs_Type.__name__ = "Integer32"
_WmanIf2mBsNumOfRecommendedBs_Object = MibTableColumn
wmanIf2mBsNumOfRecommendedBs = _WmanIf2mBsNumOfRecommendedBs_Object(
    (1, 0, 8802, 16, 3, 2, 2, 1, 4),
    _WmanIf2mBsNumOfRecommendedBs_Type()
)
wmanIf2mBsNumOfRecommendedBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsNumOfRecommendedBs.setStatus("current")


class _WmanIf2mBsScanConfigChangeCount_Type(Integer32):
    """Custom type wmanIf2mBsScanConfigChangeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsScanConfigChangeCount_Type.__name__ = "Integer32"
_WmanIf2mBsScanConfigChangeCount_Object = MibTableColumn
wmanIf2mBsScanConfigChangeCount = _WmanIf2mBsScanConfigChangeCount_Object(
    (1, 0, 8802, 16, 3, 2, 2, 1, 5),
    _WmanIf2mBsScanConfigChangeCount_Type()
)
wmanIf2mBsScanConfigChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanConfigChangeCount.setStatus("current")
_WmanIf2mBsMobileScanResponseTable_Object = MibTable
wmanIf2mBsMobileScanResponseTable = _WmanIf2mBsMobileScanResponseTable_Object(
    (1, 0, 8802, 16, 3, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIf2mBsMobileScanResponseTable.setStatus("current")
_WmanIf2mBsMobileScanResponseEntry_Object = MibTableRow
wmanIf2mBsMobileScanResponseEntry = _WmanIf2mBsMobileScanResponseEntry_Object(
    (1, 0, 8802, 16, 3, 2, 3, 1)
)
wmanIf2mBsMobileScanResponseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsMobileScanResponseEntry.setStatus("current")


class _WmanIf2mBsScanRspDuration_Type(Integer32):
    """Custom type wmanIf2mBsScanRspDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsScanRspDuration_Type.__name__ = "Integer32"
_WmanIf2mBsScanRspDuration_Object = MibTableColumn
wmanIf2mBsScanRspDuration = _WmanIf2mBsScanRspDuration_Object(
    (1, 0, 8802, 16, 3, 2, 3, 1, 1),
    _WmanIf2mBsScanRspDuration_Type()
)
wmanIf2mBsScanRspDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanRspDuration.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsScanRspDuration.setUnits("frames")


class _WmanIf2mBsScanRspInterleavingInterval_Type(Integer32):
    """Custom type wmanIf2mBsScanRspInterleavingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsScanRspInterleavingInterval_Type.__name__ = "Integer32"
_WmanIf2mBsScanRspInterleavingInterval_Object = MibTableColumn
wmanIf2mBsScanRspInterleavingInterval = _WmanIf2mBsScanRspInterleavingInterval_Object(
    (1, 0, 8802, 16, 3, 2, 3, 1, 2),
    _WmanIf2mBsScanRspInterleavingInterval_Type()
)
wmanIf2mBsScanRspInterleavingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanRspInterleavingInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsScanRspInterleavingInterval.setUnits("frames")


class _WmanIf2mBsScanRspIteration_Type(Integer32):
    """Custom type wmanIf2mBsScanRspIteration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsScanRspIteration_Type.__name__ = "Integer32"
_WmanIf2mBsScanRspIteration_Object = MibTableColumn
wmanIf2mBsScanRspIteration = _WmanIf2mBsScanRspIteration_Object(
    (1, 0, 8802, 16, 3, 2, 3, 1, 3),
    _WmanIf2mBsScanRspIteration_Type()
)
wmanIf2mBsScanRspIteration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanRspIteration.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsScanRspIteration.setUnits("frames")
_WmanIf2mBsReportMode_Type = WmanIf2mReportMode
_WmanIf2mBsReportMode_Object = MibTableColumn
wmanIf2mBsReportMode = _WmanIf2mBsReportMode_Object(
    (1, 0, 8802, 16, 3, 2, 3, 1, 4),
    _WmanIf2mBsReportMode_Type()
)
wmanIf2mBsReportMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsReportMode.setStatus("current")


class _WmanIf2mBsReportPeriod_Type(Integer32):
    """Custom type wmanIf2mBsReportPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsReportPeriod_Type.__name__ = "Integer32"
_WmanIf2mBsReportPeriod_Object = MibTableColumn
wmanIf2mBsReportPeriod = _WmanIf2mBsReportPeriod_Object(
    (1, 0, 8802, 16, 3, 2, 3, 1, 5),
    _WmanIf2mBsReportPeriod_Type()
)
wmanIf2mBsReportPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsReportPeriod.setStatus("current")
_WmanIf2mBsReportMatric_Type = WmanIf2mReportMatric
_WmanIf2mBsReportMatric_Object = MibTableColumn
wmanIf2mBsReportMatric = _WmanIf2mBsReportMatric_Object(
    (1, 0, 8802, 16, 3, 2, 3, 1, 6),
    _WmanIf2mBsReportMatric_Type()
)
wmanIf2mBsReportMatric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsReportMatric.setStatus("current")


class _WmanIf2mBsStartFrame_Type(Integer32):
    """Custom type wmanIf2mBsStartFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsStartFrame_Type.__name__ = "Integer32"
_WmanIf2mBsStartFrame_Object = MibTableColumn
wmanIf2mBsStartFrame = _WmanIf2mBsStartFrame_Object(
    (1, 0, 8802, 16, 3, 2, 3, 1, 7),
    _WmanIf2mBsStartFrame_Type()
)
wmanIf2mBsStartFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsStartFrame.setStatus("current")
_WmanIf2mBsNeighborBsInfoTable_Object = MibTable
wmanIf2mBsNeighborBsInfoTable = _WmanIf2mBsNeighborBsInfoTable_Object(
    (1, 0, 8802, 16, 3, 2, 4)
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborBsInfoTable.setStatus("current")
_WmanIf2mBsNeighborBsInfoEntry_Object = MibTableRow
wmanIf2mBsNeighborBsInfoEntry = _WmanIf2mBsNeighborBsInfoEntry_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1)
)
wmanIf2mBsNeighborBsInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsNeighbirBsIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsNeighborBsInfoEntry.setStatus("current")


class _WmanIf2mBsNeighbirBsIndex_Type(Integer32):
    """Custom type wmanIf2mBsNeighbirBsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsNeighbirBsIndex_Type.__name__ = "Integer32"
_WmanIf2mBsNeighbirBsIndex_Object = MibTableColumn
wmanIf2mBsNeighbirBsIndex = _WmanIf2mBsNeighbirBsIndex_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 1),
    _WmanIf2mBsNeighbirBsIndex_Type()
)
wmanIf2mBsNeighbirBsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsNeighbirBsIndex.setStatus("current")
_WmanIf2mBsFullBsId_Type = WmanIf2mFullBsId
_WmanIf2mBsFullBsId_Object = MibTableColumn
wmanIf2mBsFullBsId = _WmanIf2mBsFullBsId_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 2),
    _WmanIf2mBsFullBsId_Type()
)
wmanIf2mBsFullBsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsFullBsId.setStatus("current")
_WmanIf2mBsScanningType_Type = WmanIf2mScanType
_WmanIf2mBsScanningType_Object = MibTableColumn
wmanIf2mBsScanningType = _WmanIf2mBsScanningType_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 3),
    _WmanIf2mBsScanningType_Type()
)
wmanIf2mBsScanningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanningType.setStatus("current")


class _WmanIf2mBsRendezvousTime_Type(Integer32):
    """Custom type wmanIf2mBsRendezvousTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsRendezvousTime_Type.__name__ = "Integer32"
_WmanIf2mBsRendezvousTime_Object = MibTableColumn
wmanIf2mBsRendezvousTime = _WmanIf2mBsRendezvousTime_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 4),
    _WmanIf2mBsRendezvousTime_Type()
)
wmanIf2mBsRendezvousTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsRendezvousTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsRendezvousTime.setUnits("frames")


class _WmanIf2mBsScanCdmaCode_Type(Integer32):
    """Custom type wmanIf2mBsScanCdmaCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsScanCdmaCode_Type.__name__ = "Integer32"
_WmanIf2mBsScanCdmaCode_Object = MibTableColumn
wmanIf2mBsScanCdmaCode = _WmanIf2mBsScanCdmaCode_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 5),
    _WmanIf2mBsScanCdmaCode_Type()
)
wmanIf2mBsScanCdmaCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsScanCdmaCode.setStatus("current")


class _WmanIf2mBsTxOpportunityOffset_Type(Integer32):
    """Custom type wmanIf2mBsTxOpportunityOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsTxOpportunityOffset_Type.__name__ = "Integer32"
_WmanIf2mBsTxOpportunityOffset_Object = MibTableColumn
wmanIf2mBsTxOpportunityOffset = _WmanIf2mBsTxOpportunityOffset_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 6),
    _WmanIf2mBsTxOpportunityOffset_Type()
)
wmanIf2mBsTxOpportunityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsTxOpportunityOffset.setStatus("current")


class _WmanIf2mBsCinrMean_Type(Integer32):
    """Custom type wmanIf2mBsCinrMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsCinrMean_Type.__name__ = "Integer32"
_WmanIf2mBsCinrMean_Object = MibTableColumn
wmanIf2mBsCinrMean = _WmanIf2mBsCinrMean_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 7),
    _WmanIf2mBsCinrMean_Type()
)
wmanIf2mBsCinrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCinrMean.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCinrMean.setUnits("0.5 dB")


class _WmanIf2mBsRssiMean_Type(Integer32):
    """Custom type wmanIf2mBsRssiMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsRssiMean_Type.__name__ = "Integer32"
_WmanIf2mBsRssiMean_Object = MibTableColumn
wmanIf2mBsRssiMean = _WmanIf2mBsRssiMean_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 8),
    _WmanIf2mBsRssiMean_Type()
)
wmanIf2mBsRssiMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsRssiMean.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsRssiMean.setUnits("0.25 dB")


class _WmanIf2mBsRelativeDelay_Type(Integer32):
    """Custom type wmanIf2mBsRelativeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsRelativeDelay_Type.__name__ = "Integer32"
_WmanIf2mBsRelativeDelay_Object = MibTableColumn
wmanIf2mBsRelativeDelay = _WmanIf2mBsRelativeDelay_Object(
    (1, 0, 8802, 16, 3, 2, 4, 1, 9),
    _WmanIf2mBsRelativeDelay_Type()
)
wmanIf2mBsRelativeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsRelativeDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsRelativeDelay.setUnits("samples")
_WmanIf2mBsDiversityBsInfoTable_Object = MibTable
wmanIf2mBsDiversityBsInfoTable = _WmanIf2mBsDiversityBsInfoTable_Object(
    (1, 0, 8802, 16, 3, 2, 5)
)
if mibBuilder.loadTexts:
    wmanIf2mBsDiversityBsInfoTable.setStatus("current")
_WmanIf2mBsDiversityBsInfoEntry_Object = MibTableRow
wmanIf2mBsDiversityBsInfoEntry = _WmanIf2mBsDiversityBsInfoEntry_Object(
    (1, 0, 8802, 16, 3, 2, 5, 1)
)
wmanIf2mBsDiversityBsInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsSsMacAddress"),
    (0, "WMAN-IF2M-BS-MIB", "wmanIf2mBsTempBsIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsDiversityBsInfoEntry.setStatus("current")


class _WmanIf2mBsTempBsIndex_Type(Integer32):
    """Custom type wmanIf2mBsTempBsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2mBsTempBsIndex_Type.__name__ = "Integer32"
_WmanIf2mBsTempBsIndex_Object = MibTableColumn
wmanIf2mBsTempBsIndex = _WmanIf2mBsTempBsIndex_Object(
    (1, 0, 8802, 16, 3, 2, 5, 1, 1),
    _WmanIf2mBsTempBsIndex_Type()
)
wmanIf2mBsTempBsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2mBsTempBsIndex.setStatus("current")


class _WmanIf2mBsFbssMdhoCinrMean_Type(Integer32):
    """Custom type wmanIf2mBsFbssMdhoCinrMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsFbssMdhoCinrMean_Type.__name__ = "Integer32"
_WmanIf2mBsFbssMdhoCinrMean_Object = MibTableColumn
wmanIf2mBsFbssMdhoCinrMean = _WmanIf2mBsFbssMdhoCinrMean_Object(
    (1, 0, 8802, 16, 3, 2, 5, 1, 2),
    _WmanIf2mBsFbssMdhoCinrMean_Type()
)
wmanIf2mBsFbssMdhoCinrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsFbssMdhoCinrMean.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsFbssMdhoCinrMean.setUnits("0.5 dB")


class _WmanIf2mBsFbssMdhoRssiMean_Type(Integer32):
    """Custom type wmanIf2mBsFbssMdhoRssiMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsFbssMdhoRssiMean_Type.__name__ = "Integer32"
_WmanIf2mBsFbssMdhoRssiMean_Object = MibTableColumn
wmanIf2mBsFbssMdhoRssiMean = _WmanIf2mBsFbssMdhoRssiMean_Object(
    (1, 0, 8802, 16, 3, 2, 5, 1, 3),
    _WmanIf2mBsFbssMdhoRssiMean_Type()
)
wmanIf2mBsFbssMdhoRssiMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsFbssMdhoRssiMean.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsFbssMdhoRssiMean.setUnits("0.25 dB")


class _WmanIf2mBsFbssMdhoRelativeDelay_Type(Integer32):
    """Custom type wmanIf2mBsFbssMdhoRelativeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsFbssMdhoRelativeDelay_Type.__name__ = "Integer32"
_WmanIf2mBsFbssMdhoRelativeDelay_Object = MibTableColumn
wmanIf2mBsFbssMdhoRelativeDelay = _WmanIf2mBsFbssMdhoRelativeDelay_Object(
    (1, 0, 8802, 16, 3, 2, 5, 1, 4),
    _WmanIf2mBsFbssMdhoRelativeDelay_Type()
)
wmanIf2mBsFbssMdhoRelativeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsFbssMdhoRelativeDelay.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsFbssMdhoRelativeDelay.setUnits("samples")


class _WmanIf2mBsFbssMdhoRtd_Type(Integer32):
    """Custom type wmanIf2mBsFbssMdhoRtd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsFbssMdhoRtd_Type.__name__ = "Integer32"
_WmanIf2mBsFbssMdhoRtd_Object = MibTableColumn
wmanIf2mBsFbssMdhoRtd = _WmanIf2mBsFbssMdhoRtd_Object(
    (1, 0, 8802, 16, 3, 2, 5, 1, 5),
    _WmanIf2mBsFbssMdhoRtd_Type()
)
wmanIf2mBsFbssMdhoRtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsFbssMdhoRtd.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsFbssMdhoRtd.setUnits("1/Fs")
_WmanIf2mBsFm_ObjectIdentity = ObjectIdentity
wmanIf2mBsFm = _WmanIf2mBsFm_ObjectIdentity(
    (1, 0, 8802, 16, 3, 3)
)
_WmanIf2mBsSm_ObjectIdentity = ObjectIdentity
wmanIf2mBsSm = _WmanIf2mBsSm_ObjectIdentity(
    (1, 0, 8802, 16, 3, 4)
)
_WmanIf2mBsAm_ObjectIdentity = ObjectIdentity
wmanIf2mBsAm = _WmanIf2mBsAm_ObjectIdentity(
    (1, 0, 8802, 16, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-IF2M-BS-MIB",
    **{"WmanIf2mOfdmaMobility": WmanIf2mOfdmaMobility,
       "WmanIf2mHandoverType": WmanIf2mHandoverType,
       "WmanIf2mCidType": WmanIf2mCidType,
       "WmanIf2mPsClassId": WmanIf2mPsClassId,
       "WmanIf2mPsClassType": WmanIf2mPsClassType,
       "WmanIf2mPsClassCidDir": WmanIf2mPsClassCidDir,
       "WmanIf2mPowerSavingMode": WmanIf2mPowerSavingMode,
       "WmanIf2mSkipOptBitMap": WmanIf2mSkipOptBitMap,
       "WmanIf2mNbrBsId": WmanIf2mNbrBsId,
       "WmanIf2mNbrOperatorId": WmanIf2mNbrOperatorId,
       "WmanIf2mPhyProfileId": WmanIf2mPhyProfileId,
       "WmanIf2mHoProcOptm": WmanIf2mHoProcOptm,
       "WmanIf2mSchedulingSupp": WmanIf2mSchedulingSupp,
       "WmanIf2mMacVersion": WmanIf2mMacVersion,
       "WmanIf2mHarqAckDelay": WmanIf2mHarqAckDelay,
       "WmanIf2mPowerSaveType": WmanIf2mPowerSaveType,
       "WmanIf2mHoTrigMatrix": WmanIf2mHoTrigMatrix,
       "WmanIf2mAssociationTyp": WmanIf2mAssociationTyp,
       "WmanIf2mOfdmaFftSize": WmanIf2mOfdmaFftSize,
       "WmanIf2mOfdmaCp": WmanIf2mOfdmaCp,
       "WmanIf2mOfdmaFrame": WmanIf2mOfdmaFrame,
       "WmanIf2mPagingAction": WmanIf2mPagingAction,
       "WmanIf2mSsMacAddrHash": WmanIf2mSsMacAddrHash,
       "WmanIf2mSfState": WmanIf2mSfState,
       "WmanIf2mGlobalSrvClass": WmanIf2mGlobalSrvClass,
       "WmanIf2mSfDirection": WmanIf2mSfDirection,
       "WmanIf2mReqTxPolicy": WmanIf2mReqTxPolicy,
       "WmanIf2mPhsRuleVerify": WmanIf2mPhsRuleVerify,
       "WmanIf2mSchedulingType": WmanIf2mSchedulingType,
       "WmanIf2mCsSpecification": WmanIf2mCsSpecification,
       "WmanIf2mIpv6FlowLabel": WmanIf2mIpv6FlowLabel,
       "WmanIf2mClassifierBitMap": WmanIf2mClassifierBitMap,
       "WmanIf2mReportMode": WmanIf2mReportMode,
       "WmanIf2mReportMatric": WmanIf2mReportMatric,
       "WmanIf2mFullBsId": WmanIf2mFullBsId,
       "WmanIf2mScanType": WmanIf2mScanType,
       "WmanIf2mBsSsCapType": WmanIf2mBsSsCapType,
       "WmanIf2mBsCapType": WmanIf2mBsCapType,
       "WmanIf2mTrafficWkFlag": WmanIf2mTrafficWkFlag,
       "wmanIf2mBsMib": wmanIf2mBsMib,
       "wmanIf2mBsCm": wmanIf2mBsCm,
       "wmanIf2mBsConfiguration": wmanIf2mBsConfiguration,
       "wmanIf2mBsConfigurationTable": wmanIf2mBsConfigurationTable,
       "wmanIf2mBsConfigurationEntry": wmanIf2mBsConfigurationEntry,
       "wmanIf2mBsMobNbrAdvInterval": wmanIf2mBsMobNbrAdvInterval,
       "wmanIf2mBsAscAgingTimer": wmanIf2mBsAscAgingTimer,
       "wmanIf2mBsPagingRetryCount": wmanIf2mBsPagingRetryCount,
       "wmanIf2mBsModeSelectFeedbackProcTime": wmanIf2mBsModeSelectFeedbackProcTime,
       "wmanIf2mBsIdleModeSystemTimer": wmanIf2mBsIdleModeSystemTimer,
       "wmanIf2mBsMgmtResourceHoldingTimer": wmanIf2mBsMgmtResourceHoldingTimer,
       "wmanIf2mBsDregCommandRetryCount": wmanIf2mBsDregCommandRetryCount,
       "wmanIf2mBsT46Timer": wmanIf2mBsT46Timer,
       "wmanIf2mBsT47Timer": wmanIf2mBsT47Timer,
       "wmanIf2mBsPagingInterval": wmanIf2mBsPagingInterval,
       "wmanIf2mBs2ndMgmtDlQoSProfileIndex": wmanIf2mBs2ndMgmtDlQoSProfileIndex,
       "wmanIf2mBs2ndMgmtUlQoSProfileIndex": wmanIf2mBs2ndMgmtUlQoSProfileIndex,
       "wmanIf2mBsBasicCidDlQosProfileIndex": wmanIf2mBsBasicCidDlQosProfileIndex,
       "wmanIf2mBsBasicCidUlQosProfileIndex": wmanIf2mBsBasicCidUlQosProfileIndex,
       "wmanIf2mBsPrimaryCidDlQosProfileIndex": wmanIf2mBsPrimaryCidDlQosProfileIndex,
       "wmanIf2mBsPrimaryCidUlQosProfileIndex": wmanIf2mBsPrimaryCidUlQosProfileIndex,
       "wmanIf2mBsSsReqCapabilitiesTable": wmanIf2mBsSsReqCapabilitiesTable,
       "wmanIf2mBsSsReqCapabilitiesEntry": wmanIf2mBsSsReqCapabilitiesEntry,
       "wmanIf2mBsSsReqCapHandoverSupported": wmanIf2mBsSsReqCapHandoverSupported,
       "wmanIf2mBsSsReqCapHoProcessTimer": wmanIf2mBsSsReqCapHoProcessTimer,
       "wmanIf2mBsSsReqCapMobilityFeature": wmanIf2mBsSsReqCapMobilityFeature,
       "wmanIf2mBsSsReqCapSleepRecoveryTime": wmanIf2mBsSsReqCapSleepRecoveryTime,
       "wmanIf2mBsSsReqCapPreviousIpAddr": wmanIf2mBsSsReqCapPreviousIpAddr,
       "wmanIf2mBsSsReqCapIdleModeTimeout": wmanIf2mBsSsReqCapIdleModeTimeout,
       "wmanIf2mBsSsReqCapHoConnProcessTime": wmanIf2mBsSsReqCapHoConnProcessTime,
       "wmanIf2mBsSsReqCapHoTekProcessTime": wmanIf2mBsSsReqCapHoTekProcessTime,
       "wmanIf2mBsSsReqCapPowerSavingType": wmanIf2mBsSsReqCapPowerSavingType,
       "wmanIf2mBsSsReqCapNumOfPsClassIandII": wmanIf2mBsSsReqCapNumOfPsClassIandII,
       "wmanIf2mBsSsReqCapNumOfPsClassIII": wmanIf2mBsSsReqCapNumOfPsClassIII,
       "wmanIf2mBsSsReqCapHoTrigMatrix": wmanIf2mBsSsReqCapHoTrigMatrix,
       "wmanIf2mBsSsReqCapAssociationType": wmanIf2mBsSsReqCapAssociationType,
       "wmanIf2mBsSsRspCapabilitiesTable": wmanIf2mBsSsRspCapabilitiesTable,
       "wmanIf2mBsSsRspCapabilitiesEntry": wmanIf2mBsSsRspCapabilitiesEntry,
       "wmanIf2mBsSsRspCapHandoverSupported": wmanIf2mBsSsRspCapHandoverSupported,
       "wmanIf2mBsSsRspCapRetrainTime": wmanIf2mBsSsRspCapRetrainTime,
       "wmanIf2mBsSsRspCapHoProcessTimer": wmanIf2mBsSsRspCapHoProcessTimer,
       "wmanIf2mBsSsRspCapRetransmissionTimer": wmanIf2mBsSsRspCapRetransmissionTimer,
       "wmanIf2mBsSsRspCapMobilityFeature": wmanIf2mBsSsRspCapMobilityFeature,
       "wmanIf2mBsSsRspCapIdleModeTimeout": wmanIf2mBsSsRspCapIdleModeTimeout,
       "wmanIf2mBsSsRspCapHoConnProcessTime": wmanIf2mBsSsRspCapHoConnProcessTime,
       "wmanIf2mBsSsRspCapHoTekProcessTime": wmanIf2mBsSsRspCapHoTekProcessTime,
       "wmanIf2mBsSsRspCapPowerSavingType": wmanIf2mBsSsRspCapPowerSavingType,
       "wmanIf2mBsSsRspCapNumOfPsClassIandII": wmanIf2mBsSsRspCapNumOfPsClassIandII,
       "wmanIf2mBsSsRspCapNumOfPsClassIII": wmanIf2mBsSsRspCapNumOfPsClassIII,
       "wmanIf2mBsSsRspCapHoTrigMatrix": wmanIf2mBsSsRspCapHoTrigMatrix,
       "wmanIf2mBsSsRspCapAssociationType": wmanIf2mBsSsRspCapAssociationType,
       "wmanIf2mBsBasicCapabilitiesTable": wmanIf2mBsBasicCapabilitiesTable,
       "wmanIf2mBsBasicCapabilitiesEntry": wmanIf2mBsBasicCapabilitiesEntry,
       "wmanIf2mBsCapHandoverSupported": wmanIf2mBsCapHandoverSupported,
       "wmanIf2mBsCapRetrainTime": wmanIf2mBsCapRetrainTime,
       "wmanIf2mBsCapHoProcessTimer": wmanIf2mBsCapHoProcessTimer,
       "wmanIf2mBsCapRetransmissionTimer": wmanIf2mBsCapRetransmissionTimer,
       "wmanIf2mBsCapMobilityFeature": wmanIf2mBsCapMobilityFeature,
       "wmanIf2mBsCapIdleModeTimeout": wmanIf2mBsCapIdleModeTimeout,
       "wmanIf2mBsCapHoConnProcessTime": wmanIf2mBsCapHoConnProcessTime,
       "wmanIf2mBsCapHoTekProcessTime": wmanIf2mBsCapHoTekProcessTime,
       "wmanIf2mBsCapPowerSavingType": wmanIf2mBsCapPowerSavingType,
       "wmanIf2mBsCapNumOfPsClassIandII": wmanIf2mBsCapNumOfPsClassIandII,
       "wmanIf2mBsCapNumOfPsClassIII": wmanIf2mBsCapNumOfPsClassIII,
       "wmanIf2mBsCapHoTrigMatrix": wmanIf2mBsCapHoTrigMatrix,
       "wmanIf2mBsCapAssociationType": wmanIf2mBsCapAssociationType,
       "wmanIf2mBsCapabilitiesConfigTable": wmanIf2mBsCapabilitiesConfigTable,
       "wmanIf2mBsCapabilitiesConfigEntry": wmanIf2mBsCapabilitiesConfigEntry,
       "wmanIf2mBsCapCfgHandoverSupported": wmanIf2mBsCapCfgHandoverSupported,
       "wmanIf2mBsCapCfgRetrainTime": wmanIf2mBsCapCfgRetrainTime,
       "wmanIf2mBsCapCfgHoProcessTimer": wmanIf2mBsCapCfgHoProcessTimer,
       "wmanIf2mBsCapCfgRetransmissionTimer": wmanIf2mBsCapCfgRetransmissionTimer,
       "wmanIf2mBsCapCfgMobilityFeature": wmanIf2mBsCapCfgMobilityFeature,
       "wmanIf2mBsCapCfgIdleModeTimeout": wmanIf2mBsCapCfgIdleModeTimeout,
       "wmanIf2mBsCapCfgHoConnProcessTime": wmanIf2mBsCapCfgHoConnProcessTime,
       "wmanIf2mBsCapCfgHoTekProcessTime": wmanIf2mBsCapCfgHoTekProcessTime,
       "wmanIf2mBsCapCfgPowerSavingType": wmanIf2mBsCapCfgPowerSavingType,
       "wmanIf2mBsCapCfgNumOfPsClassIandII": wmanIf2mBsCapCfgNumOfPsClassIandII,
       "wmanIf2mBsCapCfgNumOfPsClassIII": wmanIf2mBsCapCfgNumOfPsClassIII,
       "wmanIf2mBsCapCfgHoTrigMatrix": wmanIf2mBsCapCfgHoTrigMatrix,
       "wmanIf2mBsCapCfgAssociationType": wmanIf2mBsCapCfgAssociationType,
       "wmanIf2mBsSsCidUpdateTable": wmanIf2mBsSsCidUpdateTable,
       "wmanIf2mBsSsCidUpdateEntry": wmanIf2mBsSsCidUpdateEntry,
       "wmanIf2mBsSsSfId": wmanIf2mBsSsSfId,
       "wmanIf2mBsSsNewCid": wmanIf2mBsSsNewCid,
       "wmanIf2mBsSsNewSaid": wmanIf2mBsSsNewSaid,
       "wmanIf2mBsSsOldSaid": wmanIf2mBsSsOldSaid,
       "wmanIf2mBsPowerSavingMode": wmanIf2mBsPowerSavingMode,
       "wmanIf2mBsSsPwrSaving2CidMapTable": wmanIf2mBsSsPwrSaving2CidMapTable,
       "wmanIf2mBsSsPwrSaving2CidMapEntry": wmanIf2mBsSsPwrSaving2CidMapEntry,
       "wmanIf2mBsSsCid": wmanIf2mBsSsCid,
       "wmanIf2mBsSsPowerSavingClassId": wmanIf2mBsSsPowerSavingClassId,
       "wmanIf2mBsSsPowerSavingClassesTable": wmanIf2mBsSsPowerSavingClassesTable,
       "wmanIf2mBsSsPowerSavingClassesEntry": wmanIf2mBsSsPowerSavingClassesEntry,
       "wmanIf2mBsSsPsClassId": wmanIf2mBsSsPsClassId,
       "wmanIf2mBsSsStartFrameNumber": wmanIf2mBsSsStartFrameNumber,
       "wmanIf2mBsSsPowerSavingClassType": wmanIf2mBsSsPowerSavingClassType,
       "wmanIf2mBsSsPsClassCidDirection": wmanIf2mBsSsPsClassCidDirection,
       "wmanIf2mBsSsTrafficTriggeredWakening": wmanIf2mBsSsTrafficTriggeredWakening,
       "wmanIf2mBsSsInitialSleepWindow": wmanIf2mBsSsInitialSleepWindow,
       "wmanIf2mBsSsFinalSleepWindowBase": wmanIf2mBsSsFinalSleepWindowBase,
       "wmanIf2mBsSsFinalSleepWindowExponent": wmanIf2mBsSsFinalSleepWindowExponent,
       "wmanIf2mBsSsListeningWindow": wmanIf2mBsSsListeningWindow,
       "wmanIf2mBsSsPowerSavingMode": wmanIf2mBsSsPowerSavingMode,
       "wmanIf2mBsSsSlpId": wmanIf2mBsSsSlpId,
       "wmanIf2mBsNeighborAdv": wmanIf2mBsNeighborAdv,
       "wmanIf2mBsNeighborAdvCommonTable": wmanIf2mBsNeighborAdvCommonTable,
       "wmanIf2mBsNeighborAdvCommonEntry": wmanIf2mBsNeighborAdvCommonEntry,
       "wmanIf2mBsSkipOptions": wmanIf2mBsSkipOptions,
       "wmanIf2mBsOperatorId": wmanIf2mBsOperatorId,
       "wmanIf2mBsNumOfNeighbors": wmanIf2mBsNumOfNeighbors,
       "wmanIf2mBsConfigChangeCount": wmanIf2mBsConfigChangeCount,
       "wmanIf2mBsNeighborAdvertizementTable": wmanIf2mBsNeighborAdvertizementTable,
       "wmanIf2mBsNeighborAdvertizementEntry": wmanIf2mBsNeighborAdvertizementEntry,
       "wmanIf2mBsNeighborBsIndex": wmanIf2mBsNeighborBsIndex,
       "wmanIf2mBsNeighborBsId": wmanIf2mBsNeighborBsId,
       "wmanIf2mBsPhyProfileId": wmanIf2mBsPhyProfileId,
       "wmanIf2mBsFaIndex": wmanIf2mBsFaIndex,
       "wmanIf2mBsEirp": wmanIf2mBsEirp,
       "wmanIf2mBsPreampleSubchIndex": wmanIf2mBsPreampleSubchIndex,
       "wmanIf2mBsHandoverProcOptimization": wmanIf2mBsHandoverProcOptimization,
       "wmanIf2mBsSchedulingService": wmanIf2mBsSchedulingService,
       "wmanIf2mBsChannelBandwidth": wmanIf2mBsChannelBandwidth,
       "wmanIf2mBsFftSize": wmanIf2mBsFftSize,
       "wmanIf2mBsCyclicPrefix": wmanIf2mBsCyclicPrefix,
       "wmanIf2mBsFrameDurationCode": wmanIf2mBsFrameDurationCode,
       "wmanIf2mBsMobilityFeatureSupported": wmanIf2mBsMobilityFeatureSupported,
       "wmanIf2mBsNrbBsPagingGroupListIndex": wmanIf2mBsNrbBsPagingGroupListIndex,
       "wmanIf2BsNeighborAdvertizementRowStatus": wmanIf2BsNeighborAdvertizementRowStatus,
       "wmanIf2mBsNeighborBsOfdmaUcdTable": wmanIf2mBsNeighborBsOfdmaUcdTable,
       "wmanIf2mBsNeighborBsOfdmaUcdEntry": wmanIf2mBsNeighborBsOfdmaUcdEntry,
       "wmanIf2mBsOfdmaCtBasedResvTimeout": wmanIf2mBsOfdmaCtBasedResvTimeout,
       "wmanIf2mBsOfdmaUplinkCenterFreq": wmanIf2mBsOfdmaUplinkCenterFreq,
       "wmanIf2mBsOfdmaStartOfRngCodes": wmanIf2mBsOfdmaStartOfRngCodes,
       "wmanIf2mBsOfdmaPermutationBase": wmanIf2mBsOfdmaPermutationBase,
       "wmanIf2mBsOfdmaULAllocSubchBitmap": wmanIf2mBsOfdmaULAllocSubchBitmap,
       "wmanIf2mBsOfdmaOptPermULAlloSubchBitmap": wmanIf2mBsOfdmaOptPermULAlloSubchBitmap,
       "wmanIf2mBsOfdmaBandAMCAllocThreshold": wmanIf2mBsOfdmaBandAMCAllocThreshold,
       "wmanIf2mBsOfdmaBandAMCReleaseThreshold": wmanIf2mBsOfdmaBandAMCReleaseThreshold,
       "wmanIf2mBsOfdmaBandAMCAllocTimer": wmanIf2mBsOfdmaBandAMCAllocTimer,
       "wmanIf2mBsOfdmaBandAMCReleaseTimer": wmanIf2mBsOfdmaBandAMCReleaseTimer,
       "wmanIf2mBsOfdmaBandStatRepMAXPeriod": wmanIf2mBsOfdmaBandStatRepMAXPeriod,
       "wmanIf2mBsOfdmaBandAMCRetryTimer": wmanIf2mBsOfdmaBandAMCRetryTimer,
       "wmanIf2mBsOfdmaHandoverRangingStart": wmanIf2mBsOfdmaHandoverRangingStart,
       "wmanIf2mBsOfdmaHandoverRangingEnd": wmanIf2mBsOfdmaHandoverRangingEnd,
       "wmanIf2mBsOfdmaHARQAackDelayDLBurst": wmanIf2mBsOfdmaHARQAackDelayDLBurst,
       "wmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap": wmanIf2mBsOfdmaUlAmcAlloPhyBandsBitmap,
       "wmanIf2mBsOfdmaMaxRetransmission": wmanIf2mBsOfdmaMaxRetransmission,
       "wmanIf2mBsOfdmaNormalizedCnOverride": wmanIf2mBsOfdmaNormalizedCnOverride,
       "wmanIf2mBsOfdmaSizeOfCqichId": wmanIf2mBsOfdmaSizeOfCqichId,
       "wmanIf2mBsOfdmaNormalizedCnValue": wmanIf2mBsOfdmaNormalizedCnValue,
       "wmanIf2mBsOfdmaNormalizedCnOverride2": wmanIf2mBsOfdmaNormalizedCnOverride2,
       "wmanIf2mBsOfdmaBandAmcEntryAvgCinr": wmanIf2mBsOfdmaBandAmcEntryAvgCinr,
       "wmanIf2mBsOfdmaAasPreambleUpperBond": wmanIf2mBsOfdmaAasPreambleUpperBond,
       "wmanIf2mBsOfdmaAasPreambleLowerBond": wmanIf2mBsOfdmaAasPreambleLowerBond,
       "wmanIf2mBsOfdmaAasBeamSelectAllowed": wmanIf2mBsOfdmaAasBeamSelectAllowed,
       "wmanIf2mBsOfdmaCqichIndicationFlag": wmanIf2mBsOfdmaCqichIndicationFlag,
       "wmanIf2mBsOfdmaUpPowerAdjStep": wmanIf2mBsOfdmaUpPowerAdjStep,
       "wmanIf2mBsOfdmaDownPowerAdjStep": wmanIf2mBsOfdmaDownPowerAdjStep,
       "wmanIf2mBsOfdmaMinPowerOffsetAdj": wmanIf2mBsOfdmaMinPowerOffsetAdj,
       "wmanIf2mBsOfdmaMaxPowerOffsetAdj": wmanIf2mBsOfdmaMaxPowerOffsetAdj,
       "wmanIf2mBsOfdmaHandoverRngCodes": wmanIf2mBsOfdmaHandoverRngCodes,
       "wmanIf2mBsOfdmaInitialRngInterval": wmanIf2mBsOfdmaInitialRngInterval,
       "wmanIf2mBsOfdmaTxPwrRepThreshold": wmanIf2mBsOfdmaTxPwrRepThreshold,
       "wmanIf2mBsOfdmaTprPower": wmanIf2mBsOfdmaTprPower,
       "wmanIf2mBsOfdmaAlphaPavg": wmanIf2mBsOfdmaAlphaPavg,
       "wmanIf2mBsOfdmaCqichTxPwrRepThreshold": wmanIf2mBsOfdmaCqichTxPwrRepThreshold,
       "wmanIf2mBsOfdmaCqichTprPower": wmanIf2mBsOfdmaCqichTprPower,
       "wmanIf2mBsOfdmaCqichAlphaPavg": wmanIf2mBsOfdmaCqichAlphaPavg,
       "wmanIf2mBsOfdmaNormalizedCnChSounding": wmanIf2mBsOfdmaNormalizedCnChSounding,
       "wmanIf2mBsOfdmaInitialRngBackoffStart": wmanIf2mBsOfdmaInitialRngBackoffStart,
       "wmanIf2mBsOfdmaInitialRngBackoffEnd": wmanIf2mBsOfdmaInitialRngBackoffEnd,
       "wmanIf2mBsOfdmaBwRequestBackoffStart": wmanIf2mBsOfdmaBwRequestBackoffStart,
       "wmanIf2mBsOfdmaBwRequestBackoffEnd": wmanIf2mBsOfdmaBwRequestBackoffEnd,
       "wmanIf2mBsNeighborBsOfdmaDcdTable": wmanIf2mBsNeighborBsOfdmaDcdTable,
       "wmanIf2mBsNeighborBsOfdmaDcdEntry": wmanIf2mBsNeighborBsOfdmaDcdEntry,
       "wmanIf2mBsOfdmaBsEIRP": wmanIf2mBsOfdmaBsEIRP,
       "wmanIf2mBsOfdmaChannelNumber": wmanIf2mBsOfdmaChannelNumber,
       "wmanIf2mBsOfdmaTTG": wmanIf2mBsOfdmaTTG,
       "wmanIf2mBsOfdmaRTG": wmanIf2mBsOfdmaRTG,
       "wmanIf2mBsOfdmaInitRngMaxRSS": wmanIf2mBsOfdmaInitRngMaxRSS,
       "wmanIf2mBsOfdmaDownlinkCenterFreq": wmanIf2mBsOfdmaDownlinkCenterFreq,
       "wmanIf2mBsOfdmaBsId": wmanIf2mBsOfdmaBsId,
       "wmanIf2mBsOfdmaMacVersion": wmanIf2mBsOfdmaMacVersion,
       "wmanIf2mBsOfdmaFrameDurationCode": wmanIf2mBsOfdmaFrameDurationCode,
       "wmanIf2mBsOfdmaHARQAackDelayULBurst": wmanIf2mBsOfdmaHARQAackDelayULBurst,
       "wmanIf2mBsOfdmaHarqZonePermutation": wmanIf2mBsOfdmaHarqZonePermutation,
       "wmanIf2mBsOfdmaHMaxRetransmission": wmanIf2mBsOfdmaHMaxRetransmission,
       "wmanIf2mBsOfdmaCinrAlphaAvg": wmanIf2mBsOfdmaCinrAlphaAvg,
       "wmanIf2mBsOfdmaRssiAlphaAvg": wmanIf2mBsOfdmaRssiAlphaAvg,
       "wmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap": wmanIf2mBsOfdmaDlAmcAlloPhyBandsBitmap,
       "wmanIf2mBsOfdmaHandoverSupported": wmanIf2mBsOfdmaHandoverSupported,
       "wmanIf2mBsOfdmaThresholdAddBsDivSet": wmanIf2mBsOfdmaThresholdAddBsDivSet,
       "wmanIf2mBsOfdmaThresholdDelBsDivSet": wmanIf2mBsOfdmaThresholdDelBsDivSet,
       "wmanIf2mBsOfdmaAsrSlotLength": wmanIf2mBsOfdmaAsrSlotLength,
       "wmanIf2mBsOfdmaAsrSwitchingPeriod": wmanIf2mBsOfdmaAsrSwitchingPeriod,
       "wmanIf2mBsOfdmaHysteresisMargin": wmanIf2mBsOfdmaHysteresisMargin,
       "wmanIf2mBsOfdmaTimeToTrigger": wmanIf2mBsOfdmaTimeToTrigger,
       "wmanIf2mBsOfdmaRestartCount": wmanIf2mBsOfdmaRestartCount,
       "wmanIf2mBsPaging": wmanIf2mBsPaging,
       "wmanIf2mBsPagingAdvertizementTable": wmanIf2mBsPagingAdvertizementTable,
       "wmanIf2mBsPagingAdvertizementEntry": wmanIf2mBsPagingAdvertizementEntry,
       "wmanIf2mBsPagingGroupListIndex": wmanIf2mBsPagingGroupListIndex,
       "wmanIf2mBsPagingRspWindow": wmanIf2mBsPagingRspWindow,
       "wmanIf2mBsPagingAdvRowStatus": wmanIf2mBsPagingAdvRowStatus,
       "wmanIf2mBsMsPagedTable": wmanIf2mBsMsPagedTable,
       "wmanIf2mBsMsPagedEntry": wmanIf2mBsMsPagedEntry,
       "wmanIf2mBsSsMacAddrHash": wmanIf2mBsSsMacAddrHash,
       "wmanIf2mBsPagingActionCode": wmanIf2mBsPagingActionCode,
       "wmanIf2mBsCdmaCode": wmanIf2mBsCdmaCode,
       "wmanIf2mBsTransmitOpportunity": wmanIf2mBsTransmitOpportunity,
       "wmanIf2mBsPagingGroupsTable": wmanIf2mBsPagingGroupsTable,
       "wmanIf2mBsPagingGroupsEntry": wmanIf2mBsPagingGroupsEntry,
       "wmanIf2mBsPagingGroupListId": wmanIf2mBsPagingGroupListId,
       "wmanIf2mBsPagingGroupId": wmanIf2mBsPagingGroupId,
       "wmanIf2BsPagingGroupsRowStatus": wmanIf2BsPagingGroupsRowStatus,
       "wmanIf2mBsServiceFlow": wmanIf2mBsServiceFlow,
       "wmanIf2mBsServiceFlowTable": wmanIf2mBsServiceFlowTable,
       "wmanIf2mBsServiceFlowEntry": wmanIf2mBsServiceFlowEntry,
       "wmanIf2mBsSsMacAddress": wmanIf2mBsSsMacAddress,
       "wmanIf2mBsServiceFlowDirection": wmanIf2mBsServiceFlowDirection,
       "wmanIf2mBsProvisionedGlobalServiceClass": wmanIf2mBsProvisionedGlobalServiceClass,
       "wmanIf2mBsAdmittedGlobalServiceClass": wmanIf2mBsAdmittedGlobalServiceClass,
       "wmanIf2mBsActiveGlobalServiceClass": wmanIf2mBsActiveGlobalServiceClass,
       "wmanIf2mBsProvisionedQoSProfileIndex": wmanIf2mBsProvisionedQoSProfileIndex,
       "wmanIf2mBsAdmittedQoSProfileIndex": wmanIf2mBsAdmittedQoSProfileIndex,
       "wmanIf2mBsActiveQoSProfileIndex": wmanIf2mBsActiveQoSProfileIndex,
       "wmanIf2mBsArqAttributeIndex": wmanIf2mBsArqAttributeIndex,
       "wmanIf2mBsServiceFlowState": wmanIf2mBsServiceFlowState,
       "wmanIf2mBsCid": wmanIf2mBsCid,
       "wmanIf2mBsSfCsSpecification": wmanIf2mBsSfCsSpecification,
       "wmanIf2mBsSfMinTolerableTrafficRate": wmanIf2mBsSfMinTolerableTrafficRate,
       "wmanIf2mBsSfReqTxPolicy": wmanIf2mBsSfReqTxPolicy,
       "wmanIf2mBsSfTargetSaid": wmanIf2mBsSfTargetSaid,
       "wmanIf2mBsSfEstablishTime": wmanIf2mBsSfEstablishTime,
       "wmanIf2mBsSfTerminateTime": wmanIf2mBsSfTerminateTime,
       "wmanIf2mBsClassifierRuleTable": wmanIf2mBsClassifierRuleTable,
       "wmanIf2mBsClassifierRuleEntry": wmanIf2mBsClassifierRuleEntry,
       "wmanIf2mBsClassifierRuleId": wmanIf2mBsClassifierRuleId,
       "wmanIf2mBsClassifierRulePriority": wmanIf2mBsClassifierRulePriority,
       "wmanIf2mBsClassifierRuleIpTosLow": wmanIf2mBsClassifierRuleIpTosLow,
       "wmanIf2mBsClassifierRuleIpTosHigh": wmanIf2mBsClassifierRuleIpTosHigh,
       "wmanIf2mBsClassifierRuleIpTosMask": wmanIf2mBsClassifierRuleIpTosMask,
       "wmanIf2mBsClassifierRuleIpProtocol": wmanIf2mBsClassifierRuleIpProtocol,
       "wmanIf2mBsClassifierRuleIpSrcAddr": wmanIf2mBsClassifierRuleIpSrcAddr,
       "wmanIf2mBsClassifierRuleIpSrcMask": wmanIf2mBsClassifierRuleIpSrcMask,
       "wmanIf2mBsClassifierRuleIpDestAddr": wmanIf2mBsClassifierRuleIpDestAddr,
       "wmanIf2mBsClassifierRuleIpDestMask": wmanIf2mBsClassifierRuleIpDestMask,
       "wmanIf2mBsClassifierRuleSrcPortStart": wmanIf2mBsClassifierRuleSrcPortStart,
       "wmanIf2mBsClassifierRuleSrcPortEnd": wmanIf2mBsClassifierRuleSrcPortEnd,
       "wmanIf2mBsClassifierRuleDestPortStart": wmanIf2mBsClassifierRuleDestPortStart,
       "wmanIf2mBsClassifierRuleDestPortEnd": wmanIf2mBsClassifierRuleDestPortEnd,
       "wmanIf2mBsClassifierRuleDestMacAddr": wmanIf2mBsClassifierRuleDestMacAddr,
       "wmanIf2mBsClassifierRuleDestMacMask": wmanIf2mBsClassifierRuleDestMacMask,
       "wmanIf2mBsClassifierRuleSrcMacAddr": wmanIf2mBsClassifierRuleSrcMacAddr,
       "wmanIf2mBsClassifierRuleSrcMacMask": wmanIf2mBsClassifierRuleSrcMacMask,
       "wmanIf2mBsClassifierRuleEnetType": wmanIf2mBsClassifierRuleEnetType,
       "wmanIf2mBsClassifierRuleEnetProtocol": wmanIf2mBsClassifierRuleEnetProtocol,
       "wmanIf2mBsClassifierRuleUserPriLow": wmanIf2mBsClassifierRuleUserPriLow,
       "wmanIf2mBsClassifierRuleUserPriHigh": wmanIf2mBsClassifierRuleUserPriHigh,
       "wmanIf2mBsClassifierRuleVlanId": wmanIf2mBsClassifierRuleVlanId,
       "wmanIf2mBsClassifierRuleIpv6FlowLabel": wmanIf2mBsClassifierRuleIpv6FlowLabel,
       "wmanIf2mBsClassifierRulePkts": wmanIf2mBsClassifierRulePkts,
       "wmanIf2mBsClassifierRuleBitMap": wmanIf2mBsClassifierRuleBitMap,
       "wmanIf2mBsClassifierRuleAssociatedPhsi": wmanIf2mBsClassifierRuleAssociatedPhsi,
       "wmanIf2mBsPhsRuleTable": wmanIf2mBsPhsRuleTable,
       "wmanIf2mBsPhsRuleEntry": wmanIf2mBsPhsRuleEntry,
       "wmanIf2mBsPhsRuleId": wmanIf2mBsPhsRuleId,
       "wmanIf2mBsPhsRulePhsField": wmanIf2mBsPhsRulePhsField,
       "wmanIf2mBsPhsRulePhsMask": wmanIf2mBsPhsRulePhsMask,
       "wmanIf2mBsPhsRulePhsSize": wmanIf2mBsPhsRulePhsSize,
       "wmanIf2mBsPhsRulePhsVerify": wmanIf2mBsPhsRulePhsVerify,
       "wmanIf2mBsQoSProfileTable": wmanIf2mBsQoSProfileTable,
       "wmanIf2mBsQoSProfileEntry": wmanIf2mBsQoSProfileEntry,
       "wmanIf2mBsQoSProfileIndex": wmanIf2mBsQoSProfileIndex,
       "wmanIf2mBsQosServiceClassName": wmanIf2mBsQosServiceClassName,
       "wmanIf2mBsQosUlGrantScheduleType": wmanIf2mBsQosUlGrantScheduleType,
       "wmanIf2mBsQosTrafficPriority": wmanIf2mBsQosTrafficPriority,
       "wmanIf2mBsQosMaximumSustainedRate": wmanIf2mBsQosMaximumSustainedRate,
       "wmanIf2mBsQosMinimumReservedRate": wmanIf2mBsQosMinimumReservedRate,
       "wmanIf2mBsQosMaximumTrafficBurst": wmanIf2mBsQosMaximumTrafficBurst,
       "wmanIf2mBsQosToleratedJitter": wmanIf2mBsQosToleratedJitter,
       "wmanIf2mBsQosMaxLatency": wmanIf2mBsQosMaxLatency,
       "wmanIf2mBsQosUnsolicitedGrantInterval": wmanIf2mBsQosUnsolicitedGrantInterval,
       "wmanIf2mBsQosSduSize": wmanIf2mBsQosSduSize,
       "wmanIf2mBsQosUnsolicitedPollInterval": wmanIf2mBsQosUnsolicitedPollInterval,
       "wmanIf2mBsArqAttributeTable": wmanIf2mBsArqAttributeTable,
       "wmanIf2mBsArqAttributeEntry": wmanIf2mBsArqAttributeEntry,
       "wmanIf2mBsArqIndex": wmanIf2mBsArqIndex,
       "wmanIf2mBsArqEnable": wmanIf2mBsArqEnable,
       "wmanIf2mBsArqWindowSize": wmanIf2mBsArqWindowSize,
       "wmanIf2mBsArqBlockLifetime": wmanIf2mBsArqBlockLifetime,
       "wmanIf2mBsArqSyncLossTimeout": wmanIf2mBsArqSyncLossTimeout,
       "wmanIf2mBsArqDeliverInOrder": wmanIf2mBsArqDeliverInOrder,
       "wmanIf2mBsArqRxPurgeTimeout": wmanIf2mBsArqRxPurgeTimeout,
       "wmanIf2mBsArqBlockSize": wmanIf2mBsArqBlockSize,
       "wmanIf2mBsArqAckProcessingTime": wmanIf2mBsArqAckProcessingTime,
       "wmanIf2mBsPm": wmanIf2mBsPm,
       "wmanIf2mBsSsSleepModeStatisticsTable": wmanIf2mBsSsSleepModeStatisticsTable,
       "wmanIf2mBsSsSleepModeStatisticsEntry": wmanIf2mBsSsSleepModeStatisticsEntry,
       "wmanIf2mBsSsStatisticsIndex": wmanIf2mBsSsStatisticsIndex,
       "wmanIf2mBsSsSleepWindowStarted": wmanIf2mBsSsSleepWindowStarted,
       "wmanIf2mBsSsListeningWindowStarted": wmanIf2mBsSsListeningWindowStarted,
       "wmanIf2mBsSsPendingMsdu": wmanIf2mBsSsPendingMsdu,
       "wmanIf2mBsSsSleepWindowTimeStamp": wmanIf2mBsSsSleepWindowTimeStamp,
       "wmanIf2mBsMobileScanRequestTable": wmanIf2mBsMobileScanRequestTable,
       "wmanIf2mBsMobileScanRequestEntry": wmanIf2mBsMobileScanRequestEntry,
       "wmanIf2mBsScanReqDuration": wmanIf2mBsScanReqDuration,
       "wmanIf2mBsScanReqInterleavingInterval": wmanIf2mBsScanReqInterleavingInterval,
       "wmanIf2mBsScanReqIteration": wmanIf2mBsScanReqIteration,
       "wmanIf2mBsNumOfRecommendedBs": wmanIf2mBsNumOfRecommendedBs,
       "wmanIf2mBsScanConfigChangeCount": wmanIf2mBsScanConfigChangeCount,
       "wmanIf2mBsMobileScanResponseTable": wmanIf2mBsMobileScanResponseTable,
       "wmanIf2mBsMobileScanResponseEntry": wmanIf2mBsMobileScanResponseEntry,
       "wmanIf2mBsScanRspDuration": wmanIf2mBsScanRspDuration,
       "wmanIf2mBsScanRspInterleavingInterval": wmanIf2mBsScanRspInterleavingInterval,
       "wmanIf2mBsScanRspIteration": wmanIf2mBsScanRspIteration,
       "wmanIf2mBsReportMode": wmanIf2mBsReportMode,
       "wmanIf2mBsReportPeriod": wmanIf2mBsReportPeriod,
       "wmanIf2mBsReportMatric": wmanIf2mBsReportMatric,
       "wmanIf2mBsStartFrame": wmanIf2mBsStartFrame,
       "wmanIf2mBsNeighborBsInfoTable": wmanIf2mBsNeighborBsInfoTable,
       "wmanIf2mBsNeighborBsInfoEntry": wmanIf2mBsNeighborBsInfoEntry,
       "wmanIf2mBsNeighbirBsIndex": wmanIf2mBsNeighbirBsIndex,
       "wmanIf2mBsFullBsId": wmanIf2mBsFullBsId,
       "wmanIf2mBsScanningType": wmanIf2mBsScanningType,
       "wmanIf2mBsRendezvousTime": wmanIf2mBsRendezvousTime,
       "wmanIf2mBsScanCdmaCode": wmanIf2mBsScanCdmaCode,
       "wmanIf2mBsTxOpportunityOffset": wmanIf2mBsTxOpportunityOffset,
       "wmanIf2mBsCinrMean": wmanIf2mBsCinrMean,
       "wmanIf2mBsRssiMean": wmanIf2mBsRssiMean,
       "wmanIf2mBsRelativeDelay": wmanIf2mBsRelativeDelay,
       "wmanIf2mBsDiversityBsInfoTable": wmanIf2mBsDiversityBsInfoTable,
       "wmanIf2mBsDiversityBsInfoEntry": wmanIf2mBsDiversityBsInfoEntry,
       "wmanIf2mBsTempBsIndex": wmanIf2mBsTempBsIndex,
       "wmanIf2mBsFbssMdhoCinrMean": wmanIf2mBsFbssMdhoCinrMean,
       "wmanIf2mBsFbssMdhoRssiMean": wmanIf2mBsFbssMdhoRssiMean,
       "wmanIf2mBsFbssMdhoRelativeDelay": wmanIf2mBsFbssMdhoRelativeDelay,
       "wmanIf2mBsFbssMdhoRtd": wmanIf2mBsFbssMdhoRtd,
       "wmanIf2mBsFm": wmanIf2mBsFm,
       "wmanIf2mBsSm": wmanIf2mBsSm,
       "wmanIf2mBsAm": wmanIf2mBsAm}
)
