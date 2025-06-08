# SNMP MIB module (WMAN-IF2M-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-IF2M-MIB.mib
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

wmanIf2mMib = ModuleIdentity(
    (1, 0, 8802, 16, 3)
)
if mibBuilder.loadTexts:
    wmanIf2mMib.setRevisions(
        ("2007-05-22 00:00",
         "2007-03-28 00:00",
         "2007-02-10 00:00",
         "2006-10-16 00:00")
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
        *(("psNotActive", 0),
          ("psActive", 1))
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("ieee802Dot16Of2001", 1),
          ("ieee802Dot16cOf2002", 2),
          ("ieee802Dot16aOf2003", 3),
          ("ieee802Dot16Of2004", 4),
          ("ieee802Dot16e", 5),
          ("tbd", 6))
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


class WmanIf2mHoTrigMatrix(TextualConvention, Integer32):
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
          ("reserved0", 28),
          ("reserved1", 29),
          ("reserved2", 30),
          ("reserved3", 31))
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
          ("reserved1", 1),
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("packetIpV4", 1),
          ("packetIpV6", 2),
          ("packet802dot3Ethernet", 3),
          ("packet802dot1QVlan", 4),
          ("packetIpV4Over802dot3", 5),
          ("packetIpV6Over802dot3", 6),
          ("packetIpV4Over802dot1Q", 7),
          ("packetIpV6Over802dot1Q", 8),
          ("atm", 9),
          ("packet802dot3EthernetRohcHc", 10),
          ("packet802dot3EthernetEcrtpHc", 11),
          ("packetIp2RohcHc", 12),
          ("packetIp2EcrtpHc", 13))
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


# MIB Managed Objects in the order of their OIDs

_WmanIf2mMibObjects_ObjectIdentity = ObjectIdentity
wmanIf2mMibObjects = _WmanIf2mMibObjects_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1)
)
_WmanIf2mBsObjects_ObjectIdentity = ObjectIdentity
wmanIf2mBsObjects = _WmanIf2mBsObjects_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1, 1)
)
_WmanIf2mBsCm_ObjectIdentity = ObjectIdentity
wmanIf2mBsCm = _WmanIf2mBsCm_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1, 1, 1)
)
_WmanIf2mBsCapabilities_ObjectIdentity = ObjectIdentity
wmanIf2mBsCapabilities = _WmanIf2mBsCapabilities_ObjectIdentity(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1)
)
_WmanIf2mBsBasicCapabilitiesTable_Object = MibTable
wmanIf2mBsBasicCapabilitiesTable = _WmanIf2mBsBasicCapabilitiesTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIf2mBsBasicCapabilitiesTable.setStatus("current")
_WmanIf2mBsBasicCapabilitiesEntry_Object = MibTableRow
wmanIf2mBsBasicCapabilitiesEntry = _WmanIf2mBsBasicCapabilitiesEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1)
)
wmanIf2mBsBasicCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsBasicCapabilitiesEntry.setStatus("current")
_WmanIf2mBsCapHandoverSupported_Type = WmanIf2mHandoverType
_WmanIf2mBsCapHandoverSupported_Object = MibTableColumn
wmanIf2mBsCapHandoverSupported = _WmanIf2mBsCapHandoverSupported_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 1),
    _WmanIf2mBsCapHandoverSupported_Type()
)
wmanIf2mBsCapHandoverSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHandoverSupported.setStatus("current")
_WmanIf2mBsCapRetrainTime_Type = Unsigned32
_WmanIf2mBsCapRetrainTime_Object = MibTableColumn
wmanIf2mBsCapRetrainTime = _WmanIf2mBsCapRetrainTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 2),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 3),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 4),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 5),
    _WmanIf2mBsCapMobilityFeature_Type()
)
wmanIf2mBsCapMobilityFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapMobilityFeature.setStatus("current")
_WmanIf2mBsCapIdleModeTimeout_Type = Unsigned32
_WmanIf2mBsCapIdleModeTimeout_Object = MibTableColumn
wmanIf2mBsCapIdleModeTimeout = _WmanIf2mBsCapIdleModeTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 6),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 7),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 8),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 9),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 10),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 11),
    _WmanIf2mBsCapNumOfPsClassIII_Type()
)
wmanIf2mBsCapNumOfPsClassIII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapNumOfPsClassIII.setStatus("current")
_WmanIf2mBsCapHoTrigMatrix_Type = WmanIf2mHoTrigMatrix
_WmanIf2mBsCapHoTrigMatrix_Object = MibTableColumn
wmanIf2mBsCapHoTrigMatrix = _WmanIf2mBsCapHoTrigMatrix_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 12),
    _WmanIf2mBsCapHoTrigMatrix_Type()
)
wmanIf2mBsCapHoTrigMatrix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapHoTrigMatrix.setStatus("current")
_WmanIf2mBsCapAssociationType_Type = WmanIf2mAssociationTyp
_WmanIf2mBsCapAssociationType_Object = MibTableColumn
wmanIf2mBsCapAssociationType = _WmanIf2mBsCapAssociationType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 3, 1, 13),
    _WmanIf2mBsCapAssociationType_Type()
)
wmanIf2mBsCapAssociationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapAssociationType.setStatus("current")
_WmanIf2mBsCapabilitiesConfigTable_Object = MibTable
wmanIf2mBsCapabilitiesConfigTable = _WmanIf2mBsCapabilitiesConfigTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wmanIf2mBsCapabilitiesConfigTable.setStatus("current")
_WmanIf2mBsCapabilitiesConfigEntry_Object = MibTableRow
wmanIf2mBsCapabilitiesConfigEntry = _WmanIf2mBsCapabilitiesConfigEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1)
)
wmanIf2mBsCapabilitiesConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2mBsCapabilitiesConfigEntry.setStatus("current")
_WmanIf2mBsCapCfgHandoverSupported_Type = WmanIf2mHandoverType
_WmanIf2mBsCapCfgHandoverSupported_Object = MibTableColumn
wmanIf2mBsCapCfgHandoverSupported = _WmanIf2mBsCapCfgHandoverSupported_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 1),
    _WmanIf2mBsCapCfgHandoverSupported_Type()
)
wmanIf2mBsCapCfgHandoverSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHandoverSupported.setStatus("current")


class _WmanIf2mBsCapCfgRetrainTime_Type(Unsigned32):
    """Custom type wmanIf2mBsCapCfgRetrainTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2mBsCapCfgRetrainTime_Type.__name__ = "Unsigned32"
_WmanIf2mBsCapCfgRetrainTime_Object = MibTableColumn
wmanIf2mBsCapCfgRetrainTime = _WmanIf2mBsCapCfgRetrainTime_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 2),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 3),
    _WmanIf2mBsCapCfgHoProcessTimer_Type()
)
wmanIf2mBsCapCfgHoProcessTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoProcessTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoProcessTimer.setUnits("frames")


class _WmanIf2mBsCapCfgRetransmissionTimer_Type(Unsigned32):
    """Custom type wmanIf2mBsCapCfgRetransmissionTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2mBsCapCfgRetransmissionTimer_Type.__name__ = "Unsigned32"
_WmanIf2mBsCapCfgRetransmissionTimer_Object = MibTableColumn
wmanIf2mBsCapCfgRetransmissionTimer = _WmanIf2mBsCapCfgRetransmissionTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 4),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 5),
    _WmanIf2mBsCapCfgMobilityFeature_Type()
)
wmanIf2mBsCapCfgMobilityFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgMobilityFeature.setStatus("current")
_WmanIf2mBsCapCfgIdleModeTimeout_Type = Unsigned32
_WmanIf2mBsCapCfgIdleModeTimeout_Object = MibTableColumn
wmanIf2mBsCapCfgIdleModeTimeout = _WmanIf2mBsCapCfgIdleModeTimeout_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 6),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 7),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 8),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 9),
    _WmanIf2mBsCapCfgPowerSavingType_Type()
)
wmanIf2mBsCapCfgPowerSavingType.setMaxAccess("read-write")
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 10),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 11),
    _WmanIf2mBsCapCfgNumOfPsClassIII_Type()
)
wmanIf2mBsCapCfgNumOfPsClassIII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgNumOfPsClassIII.setStatus("current")
_WmanIf2mBsCapCfgHoTrigMatrix_Type = WmanIf2mHoTrigMatrix
_WmanIf2mBsCapCfgHoTrigMatrix_Object = MibTableColumn
wmanIf2mBsCapCfgHoTrigMatrix = _WmanIf2mBsCapCfgHoTrigMatrix_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 12),
    _WmanIf2mBsCapCfgHoTrigMatrix_Type()
)
wmanIf2mBsCapCfgHoTrigMatrix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgHoTrigMatrix.setStatus("current")
_WmanIf2mBsCapCfgAssociationType_Type = WmanIf2mAssociationTyp
_WmanIf2mBsCapCfgAssociationType_Object = MibTableColumn
wmanIf2mBsCapCfgAssociationType = _WmanIf2mBsCapCfgAssociationType_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 1, 4, 1, 13),
    _WmanIf2mBsCapCfgAssociationType_Type()
)
wmanIf2mBsCapCfgAssociationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsCapCfgAssociationType.setStatus("current")
_WmanIf2mBsConfigurationTable_Object = MibTable
wmanIf2mBsConfigurationTable = _WmanIf2mBsConfigurationTable_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wmanIf2mBsConfigurationTable.setStatus("current")
_WmanIf2mBsConfigurationEntry_Object = MibTableRow
wmanIf2mBsConfigurationEntry = _WmanIf2mBsConfigurationEntry_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1)
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 1),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 2),
    _WmanIf2mBsAscAgingTimer_Type()
)
wmanIf2mBsAscAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsAscAgingTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsAscAgingTimer.setUnits("milliseconds")


class _WmanIf2mBsPagingRetryCount_Type(Integer32):
    """Custom type wmanIf2mBsPagingRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WmanIf2mBsPagingRetryCount_Type.__name__ = "Integer32"
_WmanIf2mBsPagingRetryCount_Object = MibTableColumn
wmanIf2mBsPagingRetryCount = _WmanIf2mBsPagingRetryCount_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 3),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 4),
    _WmanIf2mBsModeSelectFeedbackProcTime_Type()
)
wmanIf2mBsModeSelectFeedbackProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsModeSelectFeedbackProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsModeSelectFeedbackProcTime.setUnits("microseconds")


class _WmanIf2mBsIdleModeSystemTimer_Type(Unsigned32):
    """Custom type wmanIf2mBsIdleModeSystemTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 65536),
    )


_WmanIf2mBsIdleModeSystemTimer_Type.__name__ = "Unsigned32"
_WmanIf2mBsIdleModeSystemTimer_Object = MibTableColumn
wmanIf2mBsIdleModeSystemTimer = _WmanIf2mBsIdleModeSystemTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 5),
    _WmanIf2mBsIdleModeSystemTimer_Type()
)
wmanIf2mBsIdleModeSystemTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsIdleModeSystemTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsIdleModeSystemTimer.setUnits("seconds")


class _WmanIf2mBsMgmtResourceHoldingTimer_Type(Integer32):
    """Custom type wmanIf2mBsMgmtResourceHoldingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WmanIf2mBsMgmtResourceHoldingTimer_Type.__name__ = "Integer32"
_WmanIf2mBsMgmtResourceHoldingTimer_Object = MibTableColumn
wmanIf2mBsMgmtResourceHoldingTimer = _WmanIf2mBsMgmtResourceHoldingTimer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 6),
    _WmanIf2mBsMgmtResourceHoldingTimer_Type()
)
wmanIf2mBsMgmtResourceHoldingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsMgmtResourceHoldingTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsMgmtResourceHoldingTimer.setUnits("milliseconds")


class _WmanIf2mBsDregCommandRetryCount_Type(Integer32):
    """Custom type wmanIf2mBsDregCommandRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_WmanIf2mBsDregCommandRetryCount_Type.__name__ = "Integer32"
_WmanIf2mBsDregCommandRetryCount_Object = MibTableColumn
wmanIf2mBsDregCommandRetryCount = _WmanIf2mBsDregCommandRetryCount_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 7),
    _WmanIf2mBsDregCommandRetryCount_Type()
)
wmanIf2mBsDregCommandRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsDregCommandRetryCount.setStatus("current")


class _WmanIf2mBsT46Timer_Type(Integer32):
    """Custom type wmanIf2mBsT46Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_WmanIf2mBsT46Timer_Type.__name__ = "Integer32"
_WmanIf2mBsT46Timer_Object = MibTableColumn
wmanIf2mBsT46Timer = _WmanIf2mBsT46Timer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 8),
    _WmanIf2mBsT46Timer_Type()
)
wmanIf2mBsT46Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsT46Timer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsT46Timer.setUnits("milliseconds")


class _WmanIf2mBsT47Timer_Type(Integer32):
    """Custom type wmanIf2mBsT47Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1024),
    )


_WmanIf2mBsT47Timer_Type.__name__ = "Integer32"
_WmanIf2mBsT47Timer_Object = MibTableColumn
wmanIf2mBsT47Timer = _WmanIf2mBsT47Timer_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 9),
    _WmanIf2mBsT47Timer_Type()
)
wmanIf2mBsT47Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsT47Timer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2mBsT47Timer.setUnits("frames")


class _WmanIf2mBsPagingInterval_Type(Integer32):
    """Custom type wmanIf2mBsPagingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_WmanIf2mBsPagingInterval_Type.__name__ = "Integer32"
_WmanIf2mBsPagingInterval_Object = MibTableColumn
wmanIf2mBsPagingInterval = _WmanIf2mBsPagingInterval_Object(
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 10),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 11),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 12),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 13),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 14),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 15),
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
    (1, 0, 8802, 16, 3, 1, 1, 1, 5, 1, 16),
    _WmanIf2mBsPrimaryCidUlQosProfileIndex_Type()
)
wmanIf2mBsPrimaryCidUlQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIf2mBsPrimaryCidUlQosProfileIndex.setStatus("current")
_WmanIf2mMibConformance_ObjectIdentity = ObjectIdentity
wmanIf2mMibConformance = _WmanIf2mMibConformance_ObjectIdentity(
    (1, 0, 8802, 16, 3, 2)
)
_WmanIf2mMibGroups_ObjectIdentity = ObjectIdentity
wmanIf2mMibGroups = _WmanIf2mMibGroups_ObjectIdentity(
    (1, 0, 8802, 16, 3, 2, 1)
)

# Managed Objects groups

wmanIf2mMibAllObjects = ObjectGroup(
    (1, 0, 8802, 16, 3, 2, 1, 1)
)
wmanIf2mMibAllObjects.setObjects(
      *(("WMAN-IF2M-MIB", "wmanIf2mBsCapHandoverSupported"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapRetrainTime"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapHoProcessTimer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapRetransmissionTimer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapMobilityFeature"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapIdleModeTimeout"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapHoConnProcessTime"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapHoTekProcessTime"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapPowerSavingType"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapNumOfPsClassIandII"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapNumOfPsClassIII"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapHoTrigMatrix"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapAssociationType"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgHandoverSupported"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgRetrainTime"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgHoProcessTimer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgRetransmissionTimer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgMobilityFeature"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgIdleModeTimeout"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgHoConnProcessTime"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgHoTekProcessTime"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgPowerSavingType"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgNumOfPsClassIandII"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgNumOfPsClassIII"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgHoTrigMatrix"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsCapCfgAssociationType"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsMobNbrAdvInterval"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsAscAgingTimer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsPagingRetryCount"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsModeSelectFeedbackProcTime"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsIdleModeSystemTimer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsMgmtResourceHoldingTimer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsDregCommandRetryCount"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsT46Timer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsT47Timer"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsPagingInterval"),
        ("WMAN-IF2M-MIB", "wmanIf2mBs2ndMgmtDlQoSProfileIndex"),
        ("WMAN-IF2M-MIB", "wmanIf2mBs2ndMgmtUlQoSProfileIndex"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsBasicCidDlQosProfileIndex"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsBasicCidUlQosProfileIndex"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsPrimaryCidDlQosProfileIndex"),
        ("WMAN-IF2M-MIB", "wmanIf2mBsPrimaryCidUlQosProfileIndex"))
)
if mibBuilder.loadTexts:
    wmanIf2mMibAllObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-IF2M-MIB",
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
       "wmanIf2mMib": wmanIf2mMib,
       "wmanIf2mMibObjects": wmanIf2mMibObjects,
       "wmanIf2mBsObjects": wmanIf2mBsObjects,
       "wmanIf2mBsCm": wmanIf2mBsCm,
       "wmanIf2mBsCapabilities": wmanIf2mBsCapabilities,
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
       "wmanIf2mMibConformance": wmanIf2mMibConformance,
       "wmanIf2mMibGroups": wmanIf2mMibGroups,
       "wmanIf2mMibAllObjects": wmanIf2mMibAllObjects}
)
