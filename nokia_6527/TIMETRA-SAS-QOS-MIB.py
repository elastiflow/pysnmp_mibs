# SNMP MIB module (TIMETRA-SAS-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-QOS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:16 2025
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

(AtmServiceCategory,
 AtmTrafficDescrParamIndex) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory",
    "AtmTrafficDescrParamIndex")

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tNetworkEgressFCEntry,
 tNetworkPolicyEntry,
 tNetworkPolicyIndex,
 tNetworkQueueEntry,
 tNetworkQueuePolicyEntry,
 tPortSchedulerPlcyEntry,
 tSapEgressEntry,
 tSapEgressQueueEntry,
 tSapIngressEntry,
 tSapIngressFCEntry,
 tSapIngressIPCriteriaEntry,
 tSapIngressIPv6CriteriaEntry,
 tSapIngressIndex,
 tSapIngressMacCriteriaEntry,
 tSapIngressQueueEntry,
 tSlopePolicy,
 tSlopePolicyEntry) = mibBuilder.importSymbols(
    "TIMETRA-QOS-MIB",
    "tNetworkEgressFCEntry",
    "tNetworkPolicyEntry",
    "tNetworkPolicyIndex",
    "tNetworkQueueEntry",
    "tNetworkQueuePolicyEntry",
    "tPortSchedulerPlcyEntry",
    "tSapEgressEntry",
    "tSapEgressQueueEntry",
    "tSapIngressEntry",
    "tSapIngressFCEntry",
    "tSapIngressIPCriteriaEntry",
    "tSapIngressIPv6CriteriaEntry",
    "tSapIngressIndex",
    "tSapIngressMacCriteriaEntry",
    "tSapIngressQueueEntry",
    "tSlopePolicy",
    "tSlopePolicyEntry")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(Dot1PPriority,
 IpAddressPrefixLength,
 ServiceAccessPoint,
 TDEValue,
 TDSCPName,
 TDSCPNameOrEmpty,
 TDSCPValue,
 TDSCPValueOrNone,
 TEgressQueueId,
 TFCName,
 TFCType,
 TFrameType,
 TIngressMeterId,
 TIngressQueueId,
 TIpProtocol,
 TItemDescription,
 TLspExpValue,
 TMplsLspExpProfMapID,
 TNamedItem,
 TNamedItemOrEmpty,
 TNetworkIngressMeterId,
 TPortSchedulerCIR,
 TPortSchedulerPIR,
 TQueueId,
 TSapIngressMeterId,
 TTcpUdpPort,
 TTcpUdpPortOperator) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "ServiceAccessPoint",
    "TDEValue",
    "TDSCPName",
    "TDSCPNameOrEmpty",
    "TDSCPValue",
    "TDSCPValueOrNone",
    "TEgressQueueId",
    "TFCName",
    "TFCType",
    "TFrameType",
    "TIngressMeterId",
    "TIngressQueueId",
    "TIpProtocol",
    "TItemDescription",
    "TLspExpValue",
    "TMplsLspExpProfMapID",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TNetworkIngressMeterId",
    "TPortSchedulerCIR",
    "TPortSchedulerPIR",
    "TQueueId",
    "TSapIngressMeterId",
    "TTcpUdpPort",
    "TTcpUdpPortOperator")


# MODULE-IDENTITY

timetraSASQosMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    timetraSASQosMIBModule.setRevisions(
        ("1908-01-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TSapIngressPolicyID(TPolicyID):
    status = "current"


class TSapEgressPolicyID(TPolicyID):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TAccessEgressPolicyID(TPolicyID):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TNetworkPolicyID(TPolicyID):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TRemarkPolicyID(TPolicyID):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TItemScope(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 1),
          ("template", 2))
    )



class TItemMatch(TextualConvention, Integer32):
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
        *(("off", 1),
          ("false", 2),
          ("true", 3))
    )



class TPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )



class TPriorityOrDefault(TextualConvention, Integer32):
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
        *(("low", 1),
          ("high", 2),
          ("default", 3))
    )



class TProfile(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )



class TProfileOrDei(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              13)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("use-dei", 13))
    )



class TProfileOrNone(TextualConvention, Integer32):
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
          ("in", 1),
          ("out", 2))
    )



class TAdaptationRule(TextualConvention, Integer32):
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
        *(("max", 1),
          ("min", 2),
          ("closest", 3))
    )



class TRemarkType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("dscp", 2),
          ("precedence", 3))
    )



class TPrecValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TPrecValueOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TIngressCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 20000000),
    )



class TIngressPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 20000000),
    )



class TCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class TPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TPIRRateOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class TIngressBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(4, 2146959),
    )



class TBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 131072),
    )



class TBurstPercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TBurstHundredthsOfPercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class TBurstPercentOrDefault(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



class TRatePercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TLevelOrDefault(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TQWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )



class TMeterMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priority", 1),
          ("profile", 2))
    )



class TPlcyMode(TextualConvention, Integer32):
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
        *(("strict", 0),
          ("roundRobin", 1),
          ("weightedRoundRobin", 2),
          ("weightedDeficitRoundRobin", 3))
    )



class TMeterRateMode(TextualConvention, Integer32):
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
        *(("trtcm", 1),
          ("srtcm", 2),
          ("trtcm1", 3),
          ("trtcm2", 4))
    )



class TPlcyQuanta(TextualConvention, Integer32):
    status = "current"


class TQueueMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priority", 1),
          ("profile", 2))
    )



class TEntryIndicator(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TEntryId(TEntryIndicator):
    status = "current"
    subtypeSpec = TEntryIndicator.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TMatchCriteria(TextualConvention, Integer32):
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
        *(("ip", 1),
          ("mac", 2),
          ("none", 3),
          ("dscp", 4),
          ("dot1p", 5),
          ("prec", 6))
    )



class TAtmTdpDescrType(TextualConvention, Integer32):
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
        *(("clp0And1pcr", 0),
          ("clp0And1pcrPlusClp0And1scr", 1),
          ("clp0And1pcrPlusClp0scr", 2),
          ("clp0And1pcrPlusClp0scrTag", 3))
    )



class TSlopeDropRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TSlopeThreshold(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TMaxProbability(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(100, 100),
    )



class TNetworkPolicyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipInterface", 1),
          ("port", 2))
    )



class TDot1PLspExpValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TMplsLspExpProfileValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSASQosConformance_ObjectIdentity = ObjectIdentity
tmnxSASQosConformance = _TmnxSASQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1)
)
_TmnxSASQosCompliances_ObjectIdentity = ObjectIdentity
tmnxSASQosCompliances = _TmnxSASQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 1)
)
_TmnxSASQosGroups_ObjectIdentity = ObjectIdentity
tmnxSASQosGroups = _TmnxSASQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 2)
)
_TSASQosObjects_ObjectIdentity = ObjectIdentity
tSASQosObjects = _TSASQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1)
)
_TAccessEgressObjects_ObjectIdentity = ObjectIdentity
tAccessEgressObjects = _TAccessEgressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1)
)
_TAccessEgressTable_Object = MibTable
tAccessEgressTable = _TAccessEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tAccessEgressTable.setStatus("current")
_TAccessEgressEntry_Object = MibTableRow
tAccessEgressEntry = _TAccessEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1)
)
tAccessEgressEntry.setIndexNames(
    (0, "TIMETRA-SAS-QOS-MIB", "tAccessEgressIndex"),
)
if mibBuilder.loadTexts:
    tAccessEgressEntry.setStatus("current")
_TAccessEgressIndex_Type = TAccessEgressPolicyID
_TAccessEgressIndex_Object = MibTableColumn
tAccessEgressIndex = _TAccessEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1, 1),
    _TAccessEgressIndex_Type()
)
tAccessEgressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAccessEgressIndex.setStatus("current")
_TAccessEgressRowStatus_Type = RowStatus
_TAccessEgressRowStatus_Object = MibTableColumn
tAccessEgressRowStatus = _TAccessEgressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1, 2),
    _TAccessEgressRowStatus_Type()
)
tAccessEgressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressRowStatus.setStatus("current")


class _TAccessEgressScope_Type(TItemScope):
    """Custom type tAccessEgressScope based on TItemScope"""
    defaultValue = 2


_TAccessEgressScope_Type.__name__ = "TItemScope"
_TAccessEgressScope_Object = MibTableColumn
tAccessEgressScope = _TAccessEgressScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1, 3),
    _TAccessEgressScope_Type()
)
tAccessEgressScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressScope.setStatus("current")


class _TAccessEgressDescription_Type(TItemDescription):
    """Custom type tAccessEgressDescription based on TItemDescription"""
    defaultHexValue = ""


_TAccessEgressDescription_Type.__name__ = "TItemDescription"
_TAccessEgressDescription_Object = MibTableColumn
tAccessEgressDescription = _TAccessEgressDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1, 4),
    _TAccessEgressDescription_Type()
)
tAccessEgressDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressDescription.setStatus("current")
_TAccessEgressLastChanged_Type = TimeStamp
_TAccessEgressLastChanged_Object = MibTableColumn
tAccessEgressLastChanged = _TAccessEgressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1, 5),
    _TAccessEgressLastChanged_Type()
)
tAccessEgressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAccessEgressLastChanged.setStatus("current")


class _TAccessEgressRemark_Type(TruthValue):
    """Custom type tAccessEgressRemark based on TruthValue"""
    defaultValue = 2


_TAccessEgressRemark_Type.__name__ = "TruthValue"
_TAccessEgressRemark_Object = MibTableColumn
tAccessEgressRemark = _TAccessEgressRemark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1, 6),
    _TAccessEgressRemark_Type()
)
tAccessEgressRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressRemark.setStatus("current")


class _TAccessEgressRemarkPolicyId_Type(TRemarkPolicyID):
    """Custom type tAccessEgressRemarkPolicyId based on TRemarkPolicyID"""
    defaultValue = 1


_TAccessEgressRemarkPolicyId_Type.__name__ = "TRemarkPolicyID"
_TAccessEgressRemarkPolicyId_Object = MibTableColumn
tAccessEgressRemarkPolicyId = _TAccessEgressRemarkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1, 7),
    _TAccessEgressRemarkPolicyId_Type()
)
tAccessEgressRemarkPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressRemarkPolicyId.setStatus("current")


class _TAccessEgressRemarkType_Type(Integer32):
    """Custom type tAccessEgressRemarkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("use-dot1p", 1),
          ("use-dscp", 2),
          ("all", 3))
    )


_TAccessEgressRemarkType_Type.__name__ = "Integer32"
_TAccessEgressRemarkType_Object = MibTableColumn
tAccessEgressRemarkType = _TAccessEgressRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 1, 1, 8),
    _TAccessEgressRemarkType_Type()
)
tAccessEgressRemarkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressRemarkType.setStatus("current")
_TAccessEgressQueueTable_Object = MibTable
tAccessEgressQueueTable = _TAccessEgressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tAccessEgressQueueTable.setStatus("current")
_TAccessEgressQueueEntry_Object = MibTableRow
tAccessEgressQueueEntry = _TAccessEgressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1)
)
tAccessEgressQueueEntry.setIndexNames(
    (0, "TIMETRA-SAS-QOS-MIB", "tAccessEgressIndex"),
    (0, "TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueIndex"),
)
if mibBuilder.loadTexts:
    tAccessEgressQueueEntry.setStatus("current")


class _TAccessEgressQueueIndex_Type(TEgressQueueId):
    """Custom type tAccessEgressQueueIndex based on TEgressQueueId"""
    subtypeSpec = TEgressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TAccessEgressQueueIndex_Type.__name__ = "TEgressQueueId"
_TAccessEgressQueueIndex_Object = MibTableColumn
tAccessEgressQueueIndex = _TAccessEgressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 1),
    _TAccessEgressQueueIndex_Type()
)
tAccessEgressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAccessEgressQueueIndex.setStatus("current")
_TAccessEgressQueueRowStatus_Type = RowStatus
_TAccessEgressQueueRowStatus_Object = MibTableColumn
tAccessEgressQueueRowStatus = _TAccessEgressQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 2),
    _TAccessEgressQueueRowStatus_Type()
)
tAccessEgressQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueueRowStatus.setStatus("current")


class _TAccessEgressQueueCBS_Type(TBurstSize):
    """Custom type tAccessEgressQueueCBS based on TBurstSize"""
    defaultValue = -1


_TAccessEgressQueueCBS_Type.__name__ = "TBurstSize"
_TAccessEgressQueueCBS_Object = MibTableColumn
tAccessEgressQueueCBS = _TAccessEgressQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 3),
    _TAccessEgressQueueCBS_Type()
)
tAccessEgressQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueueCBS.setStatus("current")


class _TAccessEgressQueueMBS_Type(TBurstSize):
    """Custom type tAccessEgressQueueMBS based on TBurstSize"""
    defaultValue = -1


_TAccessEgressQueueMBS_Type.__name__ = "TBurstSize"
_TAccessEgressQueueMBS_Object = MibTableColumn
tAccessEgressQueueMBS = _TAccessEgressQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 4),
    _TAccessEgressQueueMBS_Type()
)
tAccessEgressQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueueMBS.setStatus("current")


class _TAccessEgressQueuePIRAdaptation_Type(TAdaptationRule):
    """Custom type tAccessEgressQueuePIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TAccessEgressQueuePIRAdaptation_Type.__name__ = "TAdaptationRule"
_TAccessEgressQueuePIRAdaptation_Object = MibTableColumn
tAccessEgressQueuePIRAdaptation = _TAccessEgressQueuePIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 5),
    _TAccessEgressQueuePIRAdaptation_Type()
)
tAccessEgressQueuePIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueuePIRAdaptation.setStatus("current")


class _TAccessEgressQueueCIRAdaptation_Type(TAdaptationRule):
    """Custom type tAccessEgressQueueCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TAccessEgressQueueCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TAccessEgressQueueCIRAdaptation_Object = MibTableColumn
tAccessEgressQueueCIRAdaptation = _TAccessEgressQueueCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 6),
    _TAccessEgressQueueCIRAdaptation_Type()
)
tAccessEgressQueueCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueueCIRAdaptation.setStatus("current")


class _TAccessEgressQueueAdminPIR_Type(TPIRRate):
    """Custom type tAccessEgressQueueAdminPIR based on TPIRRate"""
    defaultValue = -1


_TAccessEgressQueueAdminPIR_Type.__name__ = "TPIRRate"
_TAccessEgressQueueAdminPIR_Object = MibTableColumn
tAccessEgressQueueAdminPIR = _TAccessEgressQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 7),
    _TAccessEgressQueueAdminPIR_Type()
)
tAccessEgressQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueueAdminPIR.setStatus("current")


class _TAccessEgressQueueAdminCIR_Type(TCIRRate):
    """Custom type tAccessEgressQueueAdminCIR based on TCIRRate"""
    defaultValue = 0


_TAccessEgressQueueAdminCIR_Type.__name__ = "TCIRRate"
_TAccessEgressQueueAdminCIR_Object = MibTableColumn
tAccessEgressQueueAdminCIR = _TAccessEgressQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 8),
    _TAccessEgressQueueAdminCIR_Type()
)
tAccessEgressQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueueAdminCIR.setStatus("current")
_TAccessEgressQueueOperPIR_Type = TPIRRate
_TAccessEgressQueueOperPIR_Object = MibTableColumn
tAccessEgressQueueOperPIR = _TAccessEgressQueueOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 9),
    _TAccessEgressQueueOperPIR_Type()
)
tAccessEgressQueueOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAccessEgressQueueOperPIR.setStatus("current")
_TAccessEgressQueueOperCIR_Type = TCIRRate
_TAccessEgressQueueOperCIR_Object = MibTableColumn
tAccessEgressQueueOperCIR = _TAccessEgressQueueOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 10),
    _TAccessEgressQueueOperCIR_Type()
)
tAccessEgressQueueOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAccessEgressQueueOperCIR.setStatus("current")
_TAccessEgressQueueLastChanged_Type = TimeStamp
_TAccessEgressQueueLastChanged_Object = MibTableColumn
tAccessEgressQueueLastChanged = _TAccessEgressQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 11),
    _TAccessEgressQueueLastChanged_Type()
)
tAccessEgressQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAccessEgressQueueLastChanged.setStatus("current")


class _TAccessEgressQueuePolicyName_Type(TNamedItem):
    """Custom type tAccessEgressQueuePolicyName based on TNamedItem"""
    defaultValue = OctetString("default")


_TAccessEgressQueuePolicyName_Type.__name__ = "TNamedItem"
_TAccessEgressQueuePolicyName_Object = MibTableColumn
tAccessEgressQueuePolicyName = _TAccessEgressQueuePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 12),
    _TAccessEgressQueuePolicyName_Type()
)
tAccessEgressQueuePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueuePolicyName.setStatus("current")


class _TAccessEgressQueuePolicyQueueMode_Type(Integer32):
    """Custom type tAccessEgressQueuePolicyQueueMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("strict-ef", 1),
          ("strict", 2),
          ("weighted", 3))
    )


_TAccessEgressQueuePolicyQueueMode_Type.__name__ = "Integer32"
_TAccessEgressQueuePolicyQueueMode_Object = MibTableColumn
tAccessEgressQueuePolicyQueueMode = _TAccessEgressQueuePolicyQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 13),
    _TAccessEgressQueuePolicyQueueMode_Type()
)
tAccessEgressQueuePolicyQueueMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueuePolicyQueueMode.setStatus("current")


class _TAccessEgressQueuePolicyWeight_Type(Integer32):
    """Custom type tAccessEgressQueuePolicyWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TAccessEgressQueuePolicyWeight_Type.__name__ = "Integer32"
_TAccessEgressQueuePolicyWeight_Object = MibTableColumn
tAccessEgressQueuePolicyWeight = _TAccessEgressQueuePolicyWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 2, 1, 14),
    _TAccessEgressQueuePolicyWeight_Type()
)
tAccessEgressQueuePolicyWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressQueuePolicyWeight.setStatus("current")
_TAccessEgressFCTable_Object = MibTable
tAccessEgressFCTable = _TAccessEgressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tAccessEgressFCTable.setStatus("current")
_TAccessEgressFCEntry_Object = MibTableRow
tAccessEgressFCEntry = _TAccessEgressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1)
)
tAccessEgressFCEntry.setIndexNames(
    (0, "TIMETRA-SAS-QOS-MIB", "tAccessEgressIndex"),
    (0, "TIMETRA-SAS-QOS-MIB", "tAccessEgressFCName"),
)
if mibBuilder.loadTexts:
    tAccessEgressFCEntry.setStatus("current")
_TAccessEgressFCName_Type = TFCName
_TAccessEgressFCName_Object = MibTableColumn
tAccessEgressFCName = _TAccessEgressFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 1),
    _TAccessEgressFCName_Type()
)
tAccessEgressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAccessEgressFCName.setStatus("current")
_TAccessEgressFCRowStatus_Type = RowStatus
_TAccessEgressFCRowStatus_Object = MibTableColumn
tAccessEgressFCRowStatus = _TAccessEgressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 2),
    _TAccessEgressFCRowStatus_Type()
)
tAccessEgressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressFCRowStatus.setStatus("current")
_TAccessEgressFCQueue_Type = TEgressQueueId
_TAccessEgressFCQueue_Object = MibTableColumn
tAccessEgressFCQueue = _TAccessEgressFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 3),
    _TAccessEgressFCQueue_Type()
)
tAccessEgressFCQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressFCQueue.setStatus("current")


class _TAccessEgressFCDot1PInProfile_Type(Dot1PPriority):
    """Custom type tAccessEgressFCDot1PInProfile based on Dot1PPriority"""
    defaultValue = -1


_TAccessEgressFCDot1PInProfile_Type.__name__ = "Dot1PPriority"
_TAccessEgressFCDot1PInProfile_Object = MibTableColumn
tAccessEgressFCDot1PInProfile = _TAccessEgressFCDot1PInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 4),
    _TAccessEgressFCDot1PInProfile_Type()
)
tAccessEgressFCDot1PInProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressFCDot1PInProfile.setStatus("current")


class _TAccessEgressFCDot1POutProfile_Type(Dot1PPriority):
    """Custom type tAccessEgressFCDot1POutProfile based on Dot1PPriority"""
    defaultValue = -1


_TAccessEgressFCDot1POutProfile_Type.__name__ = "Dot1PPriority"
_TAccessEgressFCDot1POutProfile_Object = MibTableColumn
tAccessEgressFCDot1POutProfile = _TAccessEgressFCDot1POutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 5),
    _TAccessEgressFCDot1POutProfile_Type()
)
tAccessEgressFCDot1POutProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressFCDot1POutProfile.setStatus("current")
_TAccessEgressFCLastChanged_Type = TimeStamp
_TAccessEgressFCLastChanged_Object = MibTableColumn
tAccessEgressFCLastChanged = _TAccessEgressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 6),
    _TAccessEgressFCLastChanged_Type()
)
tAccessEgressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAccessEgressFCLastChanged.setStatus("current")


class _TAccessEgressFCDscpInProfile_Type(TDSCPNameOrEmpty):
    """Custom type tAccessEgressFCDscpInProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TAccessEgressFCDscpInProfile_Type.__name__ = "TDSCPNameOrEmpty"
_TAccessEgressFCDscpInProfile_Object = MibTableColumn
tAccessEgressFCDscpInProfile = _TAccessEgressFCDscpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 7),
    _TAccessEgressFCDscpInProfile_Type()
)
tAccessEgressFCDscpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tAccessEgressFCDscpInProfile.setStatus("current")


class _TAccessEgressFCDscpOutProfile_Type(TDSCPNameOrEmpty):
    """Custom type tAccessEgressFCDscpOutProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TAccessEgressFCDscpOutProfile_Type.__name__ = "TDSCPNameOrEmpty"
_TAccessEgressFCDscpOutProfile_Object = MibTableColumn
tAccessEgressFCDscpOutProfile = _TAccessEgressFCDscpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 8),
    _TAccessEgressFCDscpOutProfile_Type()
)
tAccessEgressFCDscpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tAccessEgressFCDscpOutProfile.setStatus("current")


class _TAccessEgressFCDot1PProfile_Type(Dot1PPriority):
    """Custom type tAccessEgressFCDot1PProfile based on Dot1PPriority"""
    defaultValue = -1


_TAccessEgressFCDot1PProfile_Type.__name__ = "Dot1PPriority"
_TAccessEgressFCDot1PProfile_Object = MibTableColumn
tAccessEgressFCDot1PProfile = _TAccessEgressFCDot1PProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 9),
    _TAccessEgressFCDot1PProfile_Type()
)
tAccessEgressFCDot1PProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAccessEgressFCDot1PProfile.setStatus("current")


class _TAccessEgressFCForceDEValue_Type(TDEValue):
    """Custom type tAccessEgressFCForceDEValue based on TDEValue"""
    defaultValue = -1


_TAccessEgressFCForceDEValue_Type.__name__ = "TDEValue"
_TAccessEgressFCForceDEValue_Object = MibTableColumn
tAccessEgressFCForceDEValue = _TAccessEgressFCForceDEValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 10),
    _TAccessEgressFCForceDEValue_Type()
)
tAccessEgressFCForceDEValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tAccessEgressFCForceDEValue.setStatus("current")


class _TAccessEgressFCDEMark_Type(TruthValue):
    """Custom type tAccessEgressFCDEMark based on TruthValue"""
    defaultValue = 2


_TAccessEgressFCDEMark_Type.__name__ = "TruthValue"
_TAccessEgressFCDEMark_Object = MibTableColumn
tAccessEgressFCDEMark = _TAccessEgressFCDEMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 1, 3, 1, 11),
    _TAccessEgressFCDEMark_Type()
)
tAccessEgressFCDEMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tAccessEgressFCDEMark.setStatus("current")
_TSASSapIngressObjects_ObjectIdentity = ObjectIdentity
tSASSapIngressObjects = _TSASSapIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2)
)
_TSapIngressMeterTable_Object = MibTable
tSapIngressMeterTable = _TSapIngressMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tSapIngressMeterTable.setStatus("current")
_TSapIngressMeterEntry_Object = MibTableRow
tSapIngressMeterEntry = _TSapIngressMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1)
)
tSapIngressMeterEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-SAS-QOS-MIB", "tSapIngressMeter"),
)
if mibBuilder.loadTexts:
    tSapIngressMeterEntry.setStatus("current")
_TSapIngressMeter_Type = TSapIngressMeterId
_TSapIngressMeter_Object = MibTableColumn
tSapIngressMeter = _TSapIngressMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 1),
    _TSapIngressMeter_Type()
)
tSapIngressMeter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressMeter.setStatus("current")
_TSapIngressMeterRowStatus_Type = RowStatus
_TSapIngressMeterRowStatus_Object = MibTableColumn
tSapIngressMeterRowStatus = _TSapIngressMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 2),
    _TSapIngressMeterRowStatus_Type()
)
tSapIngressMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterRowStatus.setStatus("current")


class _TSapIngressMeterMCast_Type(TruthValue):
    """Custom type tSapIngressMeterMCast based on TruthValue"""
    defaultValue = 2


_TSapIngressMeterMCast_Type.__name__ = "TruthValue"
_TSapIngressMeterMCast_Object = MibTableColumn
tSapIngressMeterMCast = _TSapIngressMeterMCast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 8),
    _TSapIngressMeterMCast_Type()
)
tSapIngressMeterMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterMCast.setStatus("current")


class _TSapIngressMeterCBS_Type(TIngressBurstSize):
    """Custom type tSapIngressMeterCBS based on TIngressBurstSize"""
    defaultValue = -1


_TSapIngressMeterCBS_Type.__name__ = "TIngressBurstSize"
_TSapIngressMeterCBS_Object = MibTableColumn
tSapIngressMeterCBS = _TSapIngressMeterCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 10),
    _TSapIngressMeterCBS_Type()
)
tSapIngressMeterCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterCBS.setStatus("obsolete")


class _TSapIngressMeterMBS_Type(TIngressBurstSize):
    """Custom type tSapIngressMeterMBS based on TIngressBurstSize"""
    defaultValue = -1


_TSapIngressMeterMBS_Type.__name__ = "TIngressBurstSize"
_TSapIngressMeterMBS_Object = MibTableColumn
tSapIngressMeterMBS = _TSapIngressMeterMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 11),
    _TSapIngressMeterMBS_Type()
)
tSapIngressMeterMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterMBS.setStatus("obsolete")


class _TSapIngressMeterPIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapIngressMeterPIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TSapIngressMeterPIRAdaptation_Type.__name__ = "TAdaptationRule"
_TSapIngressMeterPIRAdaptation_Object = MibTableColumn
tSapIngressMeterPIRAdaptation = _TSapIngressMeterPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 13),
    _TSapIngressMeterPIRAdaptation_Type()
)
tSapIngressMeterPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterPIRAdaptation.setStatus("current")


class _TSapIngressMeterCIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapIngressMeterCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TSapIngressMeterCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TSapIngressMeterCIRAdaptation_Object = MibTableColumn
tSapIngressMeterCIRAdaptation = _TSapIngressMeterCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 14),
    _TSapIngressMeterCIRAdaptation_Type()
)
tSapIngressMeterCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterCIRAdaptation.setStatus("current")


class _TSapIngressMeterAdminPIR_Type(TIngressPIRRate):
    """Custom type tSapIngressMeterAdminPIR based on TIngressPIRRate"""
    defaultValue = -1


_TSapIngressMeterAdminPIR_Type.__name__ = "TIngressPIRRate"
_TSapIngressMeterAdminPIR_Object = MibTableColumn
tSapIngressMeterAdminPIR = _TSapIngressMeterAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 15),
    _TSapIngressMeterAdminPIR_Type()
)
tSapIngressMeterAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterAdminPIR.setStatus("current")


class _TSapIngressMeterAdminCIR_Type(TIngressCIRRate):
    """Custom type tSapIngressMeterAdminCIR based on TIngressCIRRate"""
    defaultValue = 0


_TSapIngressMeterAdminCIR_Type.__name__ = "TIngressCIRRate"
_TSapIngressMeterAdminCIR_Object = MibTableColumn
tSapIngressMeterAdminCIR = _TSapIngressMeterAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 16),
    _TSapIngressMeterAdminCIR_Type()
)
tSapIngressMeterAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterAdminCIR.setStatus("current")
_TSapIngressMeterOperPIR_Type = TPIRRate
_TSapIngressMeterOperPIR_Object = MibTableColumn
tSapIngressMeterOperPIR = _TSapIngressMeterOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 17),
    _TSapIngressMeterOperPIR_Type()
)
tSapIngressMeterOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressMeterOperPIR.setStatus("current")
_TSapIngressMeterOperCIR_Type = TCIRRate
_TSapIngressMeterOperCIR_Object = MibTableColumn
tSapIngressMeterOperCIR = _TSapIngressMeterOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 18),
    _TSapIngressMeterOperCIR_Type()
)
tSapIngressMeterOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressMeterOperCIR.setStatus("current")
_TSapIngressMeterLastChanged_Type = TimeStamp
_TSapIngressMeterLastChanged_Object = MibTableColumn
tSapIngressMeterLastChanged = _TSapIngressMeterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 19),
    _TSapIngressMeterLastChanged_Type()
)
tSapIngressMeterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressMeterLastChanged.setStatus("current")


class _TSapIngressMeterMode_Type(TMeterMode):
    """Custom type tSapIngressMeterMode based on TMeterMode"""
    defaultValue = 1


_TSapIngressMeterMode_Type.__name__ = "TMeterMode"
_TSapIngressMeterMode_Object = MibTableColumn
tSapIngressMeterMode = _TSapIngressMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 21),
    _TSapIngressMeterMode_Type()
)
tSapIngressMeterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterMode.setStatus("current")


class _TSapIngressMeterRateMode_Type(TMeterRateMode):
    """Custom type tSapIngressMeterRateMode based on TMeterRateMode"""
    defaultValue = 3


_TSapIngressMeterRateMode_Type.__name__ = "TMeterRateMode"
_TSapIngressMeterRateMode_Object = MibTableColumn
tSapIngressMeterRateMode = _TSapIngressMeterRateMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 22),
    _TSapIngressMeterRateMode_Type()
)
tSapIngressMeterRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterRateMode.setStatus("current")


class _TSapIngressMeterAdminCBS_Type(TIngressBurstSize):
    """Custom type tSapIngressMeterAdminCBS based on TIngressBurstSize"""
    defaultValue = -1


_TSapIngressMeterAdminCBS_Type.__name__ = "TIngressBurstSize"
_TSapIngressMeterAdminCBS_Object = MibTableColumn
tSapIngressMeterAdminCBS = _TSapIngressMeterAdminCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 23),
    _TSapIngressMeterAdminCBS_Type()
)
tSapIngressMeterAdminCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterAdminCBS.setStatus("current")


class _TSapIngressMeterAdminMBS_Type(TIngressBurstSize):
    """Custom type tSapIngressMeterAdminMBS based on TIngressBurstSize"""
    defaultValue = -1


_TSapIngressMeterAdminMBS_Type.__name__ = "TIngressBurstSize"
_TSapIngressMeterAdminMBS_Object = MibTableColumn
tSapIngressMeterAdminMBS = _TSapIngressMeterAdminMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 24),
    _TSapIngressMeterAdminMBS_Type()
)
tSapIngressMeterAdminMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterAdminMBS.setStatus("current")
_TSapIngressMeterOperCBS_Type = TIngressBurstSize
_TSapIngressMeterOperCBS_Object = MibTableColumn
tSapIngressMeterOperCBS = _TSapIngressMeterOperCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 25),
    _TSapIngressMeterOperCBS_Type()
)
tSapIngressMeterOperCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressMeterOperCBS.setStatus("current")
_TSapIngressMeterOperMBS_Type = TIngressBurstSize
_TSapIngressMeterOperMBS_Object = MibTableColumn
tSapIngressMeterOperMBS = _TSapIngressMeterOperMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 26),
    _TSapIngressMeterOperMBS_Type()
)
tSapIngressMeterOperMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressMeterOperMBS.setStatus("current")


class _TSapIngressMeterProfileMode_Type(TruthValue):
    """Custom type tSapIngressMeterProfileMode based on TruthValue"""
    defaultValue = 2


_TSapIngressMeterProfileMode_Type.__name__ = "TruthValue"
_TSapIngressMeterProfileMode_Object = MibTableColumn
tSapIngressMeterProfileMode = _TSapIngressMeterProfileMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 27),
    _TSapIngressMeterProfileMode_Type()
)
tSapIngressMeterProfileMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterProfileMode.setStatus("current")


class _TSapIngressMeterColorMode_Type(Integer32):
    """Custom type tSapIngressMeterColorMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 1),
          ("color-blind", 2))
    )


_TSapIngressMeterColorMode_Type.__name__ = "Integer32"
_TSapIngressMeterColorMode_Object = MibTableColumn
tSapIngressMeterColorMode = _TSapIngressMeterColorMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 1, 1, 28),
    _TSapIngressMeterColorMode_Type()
)
tSapIngressMeterColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMeterColorMode.setStatus("current")
_TSasSapIngressFCTable_Object = MibTable
tSasSapIngressFCTable = _TSasSapIngressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tSasSapIngressFCTable.setStatus("current")
_TSasSapIngressFCEntry_Object = MibTableRow
tSasSapIngressFCEntry = _TSasSapIngressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tSasSapIngressFCEntry.setStatus("current")
_TSapIngressFCMeter_Type = TSapIngressMeterId
_TSapIngressFCMeter_Object = MibTableColumn
tSapIngressFCMeter = _TSapIngressFCMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 2, 1, 1),
    _TSapIngressFCMeter_Type()
)
tSapIngressFCMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCMeter.setStatus("current")
_TSapIngressFCMCastMeter_Type = TSapIngressMeterId
_TSapIngressFCMCastMeter_Object = MibTableColumn
tSapIngressFCMCastMeter = _TSapIngressFCMCastMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 2, 1, 2),
    _TSapIngressFCMCastMeter_Type()
)
tSapIngressFCMCastMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCMCastMeter.setStatus("current")
_TSapIngressFCBCastMeter_Type = TSapIngressMeterId
_TSapIngressFCBCastMeter_Object = MibTableColumn
tSapIngressFCBCastMeter = _TSapIngressFCBCastMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 2, 1, 3),
    _TSapIngressFCBCastMeter_Type()
)
tSapIngressFCBCastMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCBCastMeter.setStatus("current")
_TSapIngressFCUnknownMeter_Type = TSapIngressMeterId
_TSapIngressFCUnknownMeter_Object = MibTableColumn
tSapIngressFCUnknownMeter = _TSapIngressFCUnknownMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 2, 1, 4),
    _TSapIngressFCUnknownMeter_Type()
)
tSapIngressFCUnknownMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCUnknownMeter.setStatus("current")
_SapIngQosMeterStatsTable_Object = MibTable
sapIngQosMeterStatsTable = _SapIngQosMeterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sapIngQosMeterStatsTable.setStatus("current")
_SapIngQosMeterStatsEntry_Object = MibTableRow
sapIngQosMeterStatsEntry = _SapIngQosMeterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1)
)
sapIngQosMeterStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-SAS-QOS-MIB", "sapIngQosMeterId"),
)
if mibBuilder.loadTexts:
    sapIngQosMeterStatsEntry.setStatus("current")
_SapIngQosMeterId_Type = TSapIngressMeterId
_SapIngQosMeterId_Object = MibTableColumn
sapIngQosMeterId = _SapIngQosMeterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 1),
    _SapIngQosMeterId_Type()
)
sapIngQosMeterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterId.setStatus("current")
_SapIngQosMeterStatsForwardedInProfPackets_Type = Counter64
_SapIngQosMeterStatsForwardedInProfPackets_Object = MibTableColumn
sapIngQosMeterStatsForwardedInProfPackets = _SapIngQosMeterStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 10),
    _SapIngQosMeterStatsForwardedInProfPackets_Type()
)
sapIngQosMeterStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterStatsForwardedInProfPackets.setStatus("current")
_SapIngQosMeterStatsForwardedOutProfPackets_Type = Counter64
_SapIngQosMeterStatsForwardedOutProfPackets_Object = MibTableColumn
sapIngQosMeterStatsForwardedOutProfPackets = _SapIngQosMeterStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 11),
    _SapIngQosMeterStatsForwardedOutProfPackets_Type()
)
sapIngQosMeterStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterStatsForwardedOutProfPackets.setStatus("current")
_SapIngQosMeterStatsForwardedInProfOctets_Type = Counter64
_SapIngQosMeterStatsForwardedInProfOctets_Object = MibTableColumn
sapIngQosMeterStatsForwardedInProfOctets = _SapIngQosMeterStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 12),
    _SapIngQosMeterStatsForwardedInProfOctets_Type()
)
sapIngQosMeterStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterStatsForwardedInProfOctets.setStatus("current")
_SapIngQosMeterStatsForwardedOutProfOctets_Type = Counter64
_SapIngQosMeterStatsForwardedOutProfOctets_Object = MibTableColumn
sapIngQosMeterStatsForwardedOutProfOctets = _SapIngQosMeterStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 13),
    _SapIngQosMeterStatsForwardedOutProfOctets_Type()
)
sapIngQosMeterStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterStatsForwardedOutProfOctets.setStatus("current")
_SapIngQosMeterStatsForwardedPackets_Type = Counter64
_SapIngQosMeterStatsForwardedPackets_Object = MibTableColumn
sapIngQosMeterStatsForwardedPackets = _SapIngQosMeterStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 14),
    _SapIngQosMeterStatsForwardedPackets_Type()
)
sapIngQosMeterStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterStatsForwardedPackets.setStatus("current")
_SapIngQosMeterStatsForwardedOctets_Type = Counter64
_SapIngQosMeterStatsForwardedOctets_Object = MibTableColumn
sapIngQosMeterStatsForwardedOctets = _SapIngQosMeterStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 15),
    _SapIngQosMeterStatsForwardedOctets_Type()
)
sapIngQosMeterStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterStatsForwardedOctets.setStatus("current")
_SapIngQosMeterStatsDroppedPackets_Type = Counter64
_SapIngQosMeterStatsDroppedPackets_Object = MibTableColumn
sapIngQosMeterStatsDroppedPackets = _SapIngQosMeterStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 16),
    _SapIngQosMeterStatsDroppedPackets_Type()
)
sapIngQosMeterStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterStatsDroppedPackets.setStatus("current")
_SapIngQosMeterStatsDroppedOctets_Type = Counter64
_SapIngQosMeterStatsDroppedOctets_Object = MibTableColumn
sapIngQosMeterStatsDroppedOctets = _SapIngQosMeterStatsDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 3, 1, 17),
    _SapIngQosMeterStatsDroppedOctets_Type()
)
sapIngQosMeterStatsDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterStatsDroppedOctets.setStatus("current")
_TSapIngressExtnTable_Object = MibTable
tSapIngressExtnTable = _TSapIngressExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tSapIngressExtnTable.setStatus("current")
_TSapIngressExtnEntry_Object = MibTableRow
tSapIngressExtnEntry = _TSapIngressExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tSapIngressExtnEntry.setStatus("current")


class _TSapIngressNumQosClassifiers_Type(Unsigned32):
    """Custom type tSapIngressNumQosClassifiers based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_TSapIngressNumQosClassifiers_Type.__name__ = "Unsigned32"
_TSapIngressNumQosClassifiers_Object = MibTableColumn
tSapIngressNumQosClassifiers = _TSapIngressNumQosClassifiers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 1),
    _TSapIngressNumQosClassifiers_Type()
)
tSapIngressNumQosClassifiers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressNumQosClassifiers.setStatus("current")
_TSapIngressQosClassifiersUsed_Type = Unsigned32
_TSapIngressQosClassifiersUsed_Object = MibTableColumn
tSapIngressQosClassifiersUsed = _TSapIngressQosClassifiersUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 2),
    _TSapIngressQosClassifiersUsed_Type()
)
tSapIngressQosClassifiersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQosClassifiersUsed.setStatus("obsolete")
_TSapIngressQosMetersUsed_Type = Unsigned32
_TSapIngressQosMetersUsed_Object = MibTableColumn
tSapIngressQosMetersUsed = _TSapIngressQosMetersUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 3),
    _TSapIngressQosMetersUsed_Type()
)
tSapIngressQosMetersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQosMetersUsed.setStatus("obsolete")
_TSapIngressQosClassifiersRequiredInVpls_Type = Unsigned32
_TSapIngressQosClassifiersRequiredInVpls_Object = MibTableColumn
tSapIngressQosClassifiersRequiredInVpls = _TSapIngressQosClassifiersRequiredInVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 4),
    _TSapIngressQosClassifiersRequiredInVpls_Type()
)
tSapIngressQosClassifiersRequiredInVpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQosClassifiersRequiredInVpls.setStatus("current")
_TSapIngressQosClassifiersRequiredInEpipe_Type = Unsigned32
_TSapIngressQosClassifiersRequiredInEpipe_Object = MibTableColumn
tSapIngressQosClassifiersRequiredInEpipe = _TSapIngressQosClassifiersRequiredInEpipe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 5),
    _TSapIngressQosClassifiersRequiredInEpipe_Type()
)
tSapIngressQosClassifiersRequiredInEpipe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQosClassifiersRequiredInEpipe.setStatus("current")
_TSapIngressQosMetersRequiredInVpls_Type = Unsigned32
_TSapIngressQosMetersRequiredInVpls_Object = MibTableColumn
tSapIngressQosMetersRequiredInVpls = _TSapIngressQosMetersRequiredInVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 6),
    _TSapIngressQosMetersRequiredInVpls_Type()
)
tSapIngressQosMetersRequiredInVpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQosMetersRequiredInVpls.setStatus("current")
_TSapIngressQosMetersRequiredInEpipe_Type = Unsigned32
_TSapIngressQosMetersRequiredInEpipe_Object = MibTableColumn
tSapIngressQosMetersRequiredInEpipe = _TSapIngressQosMetersRequiredInEpipe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 7),
    _TSapIngressQosMetersRequiredInEpipe_Type()
)
tSapIngressQosMetersRequiredInEpipe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQosMetersRequiredInEpipe.setStatus("current")


class _TSapIngressIPCriteriaMatch_Type(Integer32):
    """Custom type tSapIngressIPCriteriaMatch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dscp-only", 2))
    )


_TSapIngressIPCriteriaMatch_Type.__name__ = "Integer32"
_TSapIngressIPCriteriaMatch_Object = MibTableColumn
tSapIngressIPCriteriaMatch = _TSapIngressIPCriteriaMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 8),
    _TSapIngressIPCriteriaMatch_Type()
)
tSapIngressIPCriteriaMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaMatch.setStatus("current")


class _TSapIngressMacCriteriaMatch_Type(Integer32):
    """Custom type tSapIngressMacCriteriaMatch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dot1p-only", 2))
    )


_TSapIngressMacCriteriaMatch_Type.__name__ = "Integer32"
_TSapIngressMacCriteriaMatch_Object = MibTableColumn
tSapIngressMacCriteriaMatch = _TSapIngressMacCriteriaMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 9),
    _TSapIngressMacCriteriaMatch_Type()
)
tSapIngressMacCriteriaMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaMatch.setStatus("current")


class _TSapIngressDefaultFCProfile_Type(TProfileOrDei):
    """Custom type tSapIngressDefaultFCProfile based on TProfileOrDei"""
    defaultValue = 2


_TSapIngressDefaultFCProfile_Type.__name__ = "TProfileOrDei"
_TSapIngressDefaultFCProfile_Object = MibTableColumn
tSapIngressDefaultFCProfile = _TSapIngressDefaultFCProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 10),
    _TSapIngressDefaultFCProfile_Type()
)
tSapIngressDefaultFCProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDefaultFCProfile.setStatus("current")


class _TSapIngressIPv6CriteriaEnable_Type(TruthValue):
    """Custom type tSapIngressIPv6CriteriaEnable based on TruthValue"""
    defaultValue = 2


_TSapIngressIPv6CriteriaEnable_Type.__name__ = "TruthValue"
_TSapIngressIPv6CriteriaEnable_Object = MibTableColumn
tSapIngressIPv6CriteriaEnable = _TSapIngressIPv6CriteriaEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 11),
    _TSapIngressIPv6CriteriaEnable_Type()
)
tSapIngressIPv6CriteriaEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaEnable.setStatus("current")


class _TSapIngressIPv6CriteriaMatch_Type(Integer32):
    """Custom type tSapIngressIPv6CriteriaMatch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dscp-only", 2))
    )


_TSapIngressIPv6CriteriaMatch_Type.__name__ = "Integer32"
_TSapIngressIPv6CriteriaMatch_Object = MibTableColumn
tSapIngressIPv6CriteriaMatch = _TSapIngressIPv6CriteriaMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 12),
    _TSapIngressIPv6CriteriaMatch_Type()
)
tSapIngressIPv6CriteriaMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaMatch.setStatus("current")


class _TSapIngressIPMacMatch_Type(Integer32):
    """Custom type tSapIngressIPMacMatch based on Integer32"""
    defaultValue = 0

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
          ("ip-first", 1),
          ("mac-first", 2))
    )


_TSapIngressIPMacMatch_Type.__name__ = "Integer32"
_TSapIngressIPMacMatch_Object = MibTableColumn
tSapIngressIPMacMatch = _TSapIngressIPMacMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 13),
    _TSapIngressIPMacMatch_Type()
)
tSapIngressIPMacMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPMacMatch.setStatus("current")
_TSapIngressQosClassifiersRequiredInIes_Type = Unsigned32
_TSapIngressQosClassifiersRequiredInIes_Object = MibTableColumn
tSapIngressQosClassifiersRequiredInIes = _TSapIngressQosClassifiersRequiredInIes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 14),
    _TSapIngressQosClassifiersRequiredInIes_Type()
)
tSapIngressQosClassifiersRequiredInIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQosClassifiersRequiredInIes.setStatus("current")
_TSapIngressQosMetersRequiredInIes_Type = Unsigned32
_TSapIngressQosMetersRequiredInIes_Object = MibTableColumn
tSapIngressQosMetersRequiredInIes = _TSapIngressQosMetersRequiredInIes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 4, 1, 15),
    _TSapIngressQosMetersRequiredInIes_Type()
)
tSapIngressQosMetersRequiredInIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQosMetersRequiredInIes.setStatus("current")
_TSapIngressQueueExtnTable_Object = MibTable
tSapIngressQueueExtnTable = _TSapIngressQueueExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tSapIngressQueueExtnTable.setStatus("current")
_TSapIngressQueueExtnEntry_Object = MibTableRow
tSapIngressQueueExtnEntry = _TSapIngressQueueExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tSapIngressQueueExtnEntry.setStatus("current")


class _TSapIngressQueuePolicyName_Type(TNamedItem):
    """Custom type tSapIngressQueuePolicyName based on TNamedItem"""
    defaultValue = OctetString("default")


_TSapIngressQueuePolicyName_Type.__name__ = "TNamedItem"
_TSapIngressQueuePolicyName_Object = MibTableColumn
tSapIngressQueuePolicyName = _TSapIngressQueuePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 5, 1, 1),
    _TSapIngressQueuePolicyName_Type()
)
tSapIngressQueuePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueuePolicyName.setStatus("current")
_TSapIngressIPCriteriaExtnTable_Object = MibTable
tSapIngressIPCriteriaExtnTable = _TSapIngressIPCriteriaExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaExtnTable.setStatus("current")
_TSapIngressIPCriteriaExtnEntry_Object = MibTableRow
tSapIngressIPCriteriaExtnEntry = _TSapIngressIPCriteriaExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaExtnEntry.setStatus("current")


class _TSapIngressIPCriteriaActionProfile_Type(TProfileOrDei):
    """Custom type tSapIngressIPCriteriaActionProfile based on TProfileOrDei"""
    defaultValue = 2


_TSapIngressIPCriteriaActionProfile_Type.__name__ = "TProfileOrDei"
_TSapIngressIPCriteriaActionProfile_Object = MibTableColumn
tSapIngressIPCriteriaActionProfile = _TSapIngressIPCriteriaActionProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 6, 1, 1),
    _TSapIngressIPCriteriaActionProfile_Type()
)
tSapIngressIPCriteriaActionProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaActionProfile.setStatus("current")
_TSapIngressMacCriteriaExtnTable_Object = MibTable
tSapIngressMacCriteriaExtnTable = _TSapIngressMacCriteriaExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaExtnTable.setStatus("current")
_TSapIngressMacCriteriaExtnEntry_Object = MibTableRow
tSapIngressMacCriteriaExtnEntry = _TSapIngressMacCriteriaExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaExtnEntry.setStatus("current")


class _TSapIngressMacCriteriaActionProfile_Type(TProfileOrDei):
    """Custom type tSapIngressMacCriteriaActionProfile based on TProfileOrDei"""
    defaultValue = 2


_TSapIngressMacCriteriaActionProfile_Type.__name__ = "TProfileOrDei"
_TSapIngressMacCriteriaActionProfile_Object = MibTableColumn
tSapIngressMacCriteriaActionProfile = _TSapIngressMacCriteriaActionProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 7, 1, 1),
    _TSapIngressMacCriteriaActionProfile_Type()
)
tSapIngressMacCriteriaActionProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaActionProfile.setStatus("current")
_TSapIngressIPv6CriteriaExtnTable_Object = MibTable
tSapIngressIPv6CriteriaExtnTable = _TSapIngressIPv6CriteriaExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaExtnTable.setStatus("current")
_TSapIngressIPv6CriteriaExtnEntry_Object = MibTableRow
tSapIngressIPv6CriteriaExtnEntry = _TSapIngressIPv6CriteriaExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaExtnEntry.setStatus("current")


class _TSapIngressIPv6CriteriaActionProfile_Type(TProfileOrDei):
    """Custom type tSapIngressIPv6CriteriaActionProfile based on TProfileOrDei"""
    defaultValue = 2


_TSapIngressIPv6CriteriaActionProfile_Type.__name__ = "TProfileOrDei"
_TSapIngressIPv6CriteriaActionProfile_Object = MibTableColumn
tSapIngressIPv6CriteriaActionProfile = _TSapIngressIPv6CriteriaActionProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 2, 8, 1, 1),
    _TSapIngressIPv6CriteriaActionProfile_Type()
)
tSapIngressIPv6CriteriaActionProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaActionProfile.setStatus("current")
_TSASNetworkIngressObjects_ObjectIdentity = ObjectIdentity
tSASNetworkIngressObjects = _TSASNetworkIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3)
)
_TNetworkIngressFCExtnTable_Object = MibTable
tNetworkIngressFCExtnTable = _TNetworkIngressFCExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tNetworkIngressFCExtnTable.setStatus("current")
_TNetworkIngressFCExtnEntry_Object = MibTableRow
tNetworkIngressFCExtnEntry = _TNetworkIngressFCExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 1, 1)
)
tNetworkIngressFCExtnEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnName"),
)
if mibBuilder.loadTexts:
    tNetworkIngressFCExtnEntry.setStatus("current")
_TNetworkIngressFCExtnName_Type = TNamedItem
_TNetworkIngressFCExtnName_Object = MibTableColumn
tNetworkIngressFCExtnName = _TNetworkIngressFCExtnName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 1, 1, 1),
    _TNetworkIngressFCExtnName_Type()
)
tNetworkIngressFCExtnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkIngressFCExtnName.setStatus("current")
_TNetworkIngressFCExtnRowStatus_Type = RowStatus
_TNetworkIngressFCExtnRowStatus_Object = MibTableColumn
tNetworkIngressFCExtnRowStatus = _TNetworkIngressFCExtnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 1, 1, 2),
    _TNetworkIngressFCExtnRowStatus_Type()
)
tNetworkIngressFCExtnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressFCExtnRowStatus.setStatus("current")
_TNetworkIngressFCExtnMeter_Type = TNetworkIngressMeterId
_TNetworkIngressFCExtnMeter_Object = MibTableColumn
tNetworkIngressFCExtnMeter = _TNetworkIngressFCExtnMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 1, 1, 3),
    _TNetworkIngressFCExtnMeter_Type()
)
tNetworkIngressFCExtnMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressFCExtnMeter.setStatus("current")
_TNetworkIngressFCExtnMCastMeter_Type = TNetworkIngressMeterId
_TNetworkIngressFCExtnMCastMeter_Object = MibTableColumn
tNetworkIngressFCExtnMCastMeter = _TNetworkIngressFCExtnMCastMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 1, 1, 4),
    _TNetworkIngressFCExtnMCastMeter_Type()
)
tNetworkIngressFCExtnMCastMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressFCExtnMCastMeter.setStatus("current")
_TNetworkIngressFCExtnLastChanged_Type = TimeStamp
_TNetworkIngressFCExtnLastChanged_Object = MibTableColumn
tNetworkIngressFCExtnLastChanged = _TNetworkIngressFCExtnLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 1, 1, 5),
    _TNetworkIngressFCExtnLastChanged_Type()
)
tNetworkIngressFCExtnLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressFCExtnLastChanged.setStatus("current")
_TNetworkIngressMeterTable_Object = MibTable
tNetworkIngressMeterTable = _TNetworkIngressMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tNetworkIngressMeterTable.setStatus("current")
_TNetworkIngressMeterEntry_Object = MibTableRow
tNetworkIngressMeterEntry = _TNetworkIngressMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1)
)
tNetworkIngressMeterEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterIndex"),
)
if mibBuilder.loadTexts:
    tNetworkIngressMeterEntry.setStatus("current")
_TNetworkIngressMeterIndex_Type = TNetworkIngressMeterId
_TNetworkIngressMeterIndex_Object = MibTableColumn
tNetworkIngressMeterIndex = _TNetworkIngressMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 1),
    _TNetworkIngressMeterIndex_Type()
)
tNetworkIngressMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkIngressMeterIndex.setStatus("current")
_TNetworkIngressMeterRowStatus_Type = RowStatus
_TNetworkIngressMeterRowStatus_Object = MibTableColumn
tNetworkIngressMeterRowStatus = _TNetworkIngressMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 2),
    _TNetworkIngressMeterRowStatus_Type()
)
tNetworkIngressMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterRowStatus.setStatus("current")


class _TNetworkIngressMeterCBS_Type(TIngressBurstSize):
    """Custom type tNetworkIngressMeterCBS based on TIngressBurstSize"""
    defaultValue = -1


_TNetworkIngressMeterCBS_Type.__name__ = "TIngressBurstSize"
_TNetworkIngressMeterCBS_Object = MibTableColumn
tNetworkIngressMeterCBS = _TNetworkIngressMeterCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 3),
    _TNetworkIngressMeterCBS_Type()
)
tNetworkIngressMeterCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterCBS.setStatus("obsolete")


class _TNetworkIngressMeterMBS_Type(TIngressBurstSize):
    """Custom type tNetworkIngressMeterMBS based on TIngressBurstSize"""
    defaultValue = -1


_TNetworkIngressMeterMBS_Type.__name__ = "TIngressBurstSize"
_TNetworkIngressMeterMBS_Object = MibTableColumn
tNetworkIngressMeterMBS = _TNetworkIngressMeterMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 4),
    _TNetworkIngressMeterMBS_Type()
)
tNetworkIngressMeterMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterMBS.setStatus("obsolete")


class _TNetworkIngressMeterCIRAdaptation_Type(TAdaptationRule):
    """Custom type tNetworkIngressMeterCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TNetworkIngressMeterCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TNetworkIngressMeterCIRAdaptation_Object = MibTableColumn
tNetworkIngressMeterCIRAdaptation = _TNetworkIngressMeterCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 5),
    _TNetworkIngressMeterCIRAdaptation_Type()
)
tNetworkIngressMeterCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterCIRAdaptation.setStatus("current")


class _TNetworkIngressMeterPIRAdaptation_Type(TAdaptationRule):
    """Custom type tNetworkIngressMeterPIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TNetworkIngressMeterPIRAdaptation_Type.__name__ = "TAdaptationRule"
_TNetworkIngressMeterPIRAdaptation_Object = MibTableColumn
tNetworkIngressMeterPIRAdaptation = _TNetworkIngressMeterPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 6),
    _TNetworkIngressMeterPIRAdaptation_Type()
)
tNetworkIngressMeterPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterPIRAdaptation.setStatus("current")


class _TNetworkIngressMeterAdminPIR_Type(TIngressPIRRate):
    """Custom type tNetworkIngressMeterAdminPIR based on TIngressPIRRate"""
    defaultValue = -1


_TNetworkIngressMeterAdminPIR_Type.__name__ = "TIngressPIRRate"
_TNetworkIngressMeterAdminPIR_Object = MibTableColumn
tNetworkIngressMeterAdminPIR = _TNetworkIngressMeterAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 7),
    _TNetworkIngressMeterAdminPIR_Type()
)
tNetworkIngressMeterAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterAdminPIR.setStatus("current")


class _TNetworkIngressMeterAdminCIR_Type(TIngressCIRRate):
    """Custom type tNetworkIngressMeterAdminCIR based on TIngressCIRRate"""
    defaultValue = 0


_TNetworkIngressMeterAdminCIR_Type.__name__ = "TIngressCIRRate"
_TNetworkIngressMeterAdminCIR_Object = MibTableColumn
tNetworkIngressMeterAdminCIR = _TNetworkIngressMeterAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 8),
    _TNetworkIngressMeterAdminCIR_Type()
)
tNetworkIngressMeterAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterAdminCIR.setStatus("current")
_TNetworkIngressMeterOperPIR_Type = TPIRRate
_TNetworkIngressMeterOperPIR_Object = MibTableColumn
tNetworkIngressMeterOperPIR = _TNetworkIngressMeterOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 9),
    _TNetworkIngressMeterOperPIR_Type()
)
tNetworkIngressMeterOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressMeterOperPIR.setStatus("current")
_TNetworkIngressMeterOperCIR_Type = TCIRRate
_TNetworkIngressMeterOperCIR_Object = MibTableColumn
tNetworkIngressMeterOperCIR = _TNetworkIngressMeterOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 10),
    _TNetworkIngressMeterOperCIR_Type()
)
tNetworkIngressMeterOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressMeterOperCIR.setStatus("current")
_TNetworkIngressMeterLastChanged_Type = TimeStamp
_TNetworkIngressMeterLastChanged_Object = MibTableColumn
tNetworkIngressMeterLastChanged = _TNetworkIngressMeterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 11),
    _TNetworkIngressMeterLastChanged_Type()
)
tNetworkIngressMeterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressMeterLastChanged.setStatus("current")


class _TNetworkIngressMeterMode_Type(TMeterMode):
    """Custom type tNetworkIngressMeterMode based on TMeterMode"""
    defaultValue = 1


_TNetworkIngressMeterMode_Type.__name__ = "TMeterMode"
_TNetworkIngressMeterMode_Object = MibTableColumn
tNetworkIngressMeterMode = _TNetworkIngressMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 12),
    _TNetworkIngressMeterMode_Type()
)
tNetworkIngressMeterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterMode.setStatus("current")


class _TNetworkIngressMeterMCast_Type(TruthValue):
    """Custom type tNetworkIngressMeterMCast based on TruthValue"""
    defaultValue = 2


_TNetworkIngressMeterMCast_Type.__name__ = "TruthValue"
_TNetworkIngressMeterMCast_Object = MibTableColumn
tNetworkIngressMeterMCast = _TNetworkIngressMeterMCast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 13),
    _TNetworkIngressMeterMCast_Type()
)
tNetworkIngressMeterMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterMCast.setStatus("current")


class _TNetworkIngressMeterRateMode_Type(TMeterRateMode):
    """Custom type tNetworkIngressMeterRateMode based on TMeterRateMode"""
    defaultValue = 3


_TNetworkIngressMeterRateMode_Type.__name__ = "TMeterRateMode"
_TNetworkIngressMeterRateMode_Object = MibTableColumn
tNetworkIngressMeterRateMode = _TNetworkIngressMeterRateMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 14),
    _TNetworkIngressMeterRateMode_Type()
)
tNetworkIngressMeterRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterRateMode.setStatus("current")


class _TNetworkIngressMeterAdminCBS_Type(TIngressBurstSize):
    """Custom type tNetworkIngressMeterAdminCBS based on TIngressBurstSize"""
    defaultValue = -1


_TNetworkIngressMeterAdminCBS_Type.__name__ = "TIngressBurstSize"
_TNetworkIngressMeterAdminCBS_Object = MibTableColumn
tNetworkIngressMeterAdminCBS = _TNetworkIngressMeterAdminCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 15),
    _TNetworkIngressMeterAdminCBS_Type()
)
tNetworkIngressMeterAdminCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterAdminCBS.setStatus("current")


class _TNetworkIngressMeterAdminMBS_Type(TIngressBurstSize):
    """Custom type tNetworkIngressMeterAdminMBS based on TIngressBurstSize"""
    defaultValue = -1


_TNetworkIngressMeterAdminMBS_Type.__name__ = "TIngressBurstSize"
_TNetworkIngressMeterAdminMBS_Object = MibTableColumn
tNetworkIngressMeterAdminMBS = _TNetworkIngressMeterAdminMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 16),
    _TNetworkIngressMeterAdminMBS_Type()
)
tNetworkIngressMeterAdminMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterAdminMBS.setStatus("current")
_TNetworkIngressMeterOperCBS_Type = TIngressBurstSize
_TNetworkIngressMeterOperCBS_Object = MibTableColumn
tNetworkIngressMeterOperCBS = _TNetworkIngressMeterOperCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 17),
    _TNetworkIngressMeterOperCBS_Type()
)
tNetworkIngressMeterOperCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressMeterOperCBS.setStatus("current")
_TNetworkIngressMeterOperMBS_Type = TIngressBurstSize
_TNetworkIngressMeterOperMBS_Object = MibTableColumn
tNetworkIngressMeterOperMBS = _TNetworkIngressMeterOperMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 3, 2, 1, 26),
    _TNetworkIngressMeterOperMBS_Type()
)
tNetworkIngressMeterOperMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressMeterOperMBS.setStatus("current")
_TSASSlopeObjects_ObjectIdentity = ObjectIdentity
tSASSlopeObjects = _TSASSlopeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4)
)
_TSasSlopePolicyExtnTable_Object = MibTable
tSasSlopePolicyExtnTable = _TSasSlopePolicyExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tSasSlopePolicyExtnTable.setStatus("current")
_TSasSlopePolicyExtnEntry_Object = MibTableRow
tSasSlopePolicyExtnEntry = _TSasSlopePolicyExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tSasSlopePolicyExtnEntry.setStatus("current")


class _TSlopeHiQueue1DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeHiQueue1DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TSlopeHiQueue1DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeHiQueue1DropRate_Object = MibTableColumn
tSlopeHiQueue1DropRate = _TSlopeHiQueue1DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 1),
    _TSlopeHiQueue1DropRate_Type()
)
tSlopeHiQueue1DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiQueue1DropRate.setStatus("current")


class _TSlopeHiQueue2DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeHiQueue2DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TSlopeHiQueue2DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeHiQueue2DropRate_Object = MibTableColumn
tSlopeHiQueue2DropRate = _TSlopeHiQueue2DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 2),
    _TSlopeHiQueue2DropRate_Type()
)
tSlopeHiQueue2DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiQueue2DropRate.setStatus("current")


class _TSlopeHiQueue3DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeHiQueue3DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TSlopeHiQueue3DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeHiQueue3DropRate_Object = MibTableColumn
tSlopeHiQueue3DropRate = _TSlopeHiQueue3DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 3),
    _TSlopeHiQueue3DropRate_Type()
)
tSlopeHiQueue3DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiQueue3DropRate.setStatus("current")


class _TSlopeHiQueue4DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeHiQueue4DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TSlopeHiQueue4DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeHiQueue4DropRate_Object = MibTableColumn
tSlopeHiQueue4DropRate = _TSlopeHiQueue4DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 4),
    _TSlopeHiQueue4DropRate_Type()
)
tSlopeHiQueue4DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiQueue4DropRate.setStatus("current")


class _TSlopeHiQueue5DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeHiQueue5DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TSlopeHiQueue5DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeHiQueue5DropRate_Object = MibTableColumn
tSlopeHiQueue5DropRate = _TSlopeHiQueue5DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 5),
    _TSlopeHiQueue5DropRate_Type()
)
tSlopeHiQueue5DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiQueue5DropRate.setStatus("current")


class _TSlopeHiQueue6DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeHiQueue6DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TSlopeHiQueue6DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeHiQueue6DropRate_Object = MibTableColumn
tSlopeHiQueue6DropRate = _TSlopeHiQueue6DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 6),
    _TSlopeHiQueue6DropRate_Type()
)
tSlopeHiQueue6DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiQueue6DropRate.setStatus("current")


class _TSlopeHiQueue7DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeHiQueue7DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TSlopeHiQueue7DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeHiQueue7DropRate_Object = MibTableColumn
tSlopeHiQueue7DropRate = _TSlopeHiQueue7DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 7),
    _TSlopeHiQueue7DropRate_Type()
)
tSlopeHiQueue7DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiQueue7DropRate.setStatus("current")


class _TSlopeHiQueue8DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeHiQueue8DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TSlopeHiQueue8DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeHiQueue8DropRate_Object = MibTableColumn
tSlopeHiQueue8DropRate = _TSlopeHiQueue8DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 8),
    _TSlopeHiQueue8DropRate_Type()
)
tSlopeHiQueue8DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiQueue8DropRate.setStatus("current")


class _TSlopeLoQueue1DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeLoQueue1DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TSlopeLoQueue1DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeLoQueue1DropRate_Object = MibTableColumn
tSlopeLoQueue1DropRate = _TSlopeLoQueue1DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 9),
    _TSlopeLoQueue1DropRate_Type()
)
tSlopeLoQueue1DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoQueue1DropRate.setStatus("current")


class _TSlopeLoQueue2DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeLoQueue2DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TSlopeLoQueue2DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeLoQueue2DropRate_Object = MibTableColumn
tSlopeLoQueue2DropRate = _TSlopeLoQueue2DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 10),
    _TSlopeLoQueue2DropRate_Type()
)
tSlopeLoQueue2DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoQueue2DropRate.setStatus("current")


class _TSlopeLoQueue3DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeLoQueue3DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TSlopeLoQueue3DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeLoQueue3DropRate_Object = MibTableColumn
tSlopeLoQueue3DropRate = _TSlopeLoQueue3DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 11),
    _TSlopeLoQueue3DropRate_Type()
)
tSlopeLoQueue3DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoQueue3DropRate.setStatus("current")


class _TSlopeLoQueue4DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeLoQueue4DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TSlopeLoQueue4DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeLoQueue4DropRate_Object = MibTableColumn
tSlopeLoQueue4DropRate = _TSlopeLoQueue4DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 12),
    _TSlopeLoQueue4DropRate_Type()
)
tSlopeLoQueue4DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoQueue4DropRate.setStatus("current")


class _TSlopeLoQueue5DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeLoQueue5DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TSlopeLoQueue5DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeLoQueue5DropRate_Object = MibTableColumn
tSlopeLoQueue5DropRate = _TSlopeLoQueue5DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 13),
    _TSlopeLoQueue5DropRate_Type()
)
tSlopeLoQueue5DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoQueue5DropRate.setStatus("current")


class _TSlopeLoQueue6DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeLoQueue6DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TSlopeLoQueue6DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeLoQueue6DropRate_Object = MibTableColumn
tSlopeLoQueue6DropRate = _TSlopeLoQueue6DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 14),
    _TSlopeLoQueue6DropRate_Type()
)
tSlopeLoQueue6DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoQueue6DropRate.setStatus("current")


class _TSlopeLoQueue7DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeLoQueue7DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TSlopeLoQueue7DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeLoQueue7DropRate_Object = MibTableColumn
tSlopeLoQueue7DropRate = _TSlopeLoQueue7DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 15),
    _TSlopeLoQueue7DropRate_Type()
)
tSlopeLoQueue7DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoQueue7DropRate.setStatus("current")


class _TSlopeLoQueue8DropRate_Type(TSlopeDropRate):
    """Custom type tSlopeLoQueue8DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TSlopeLoQueue8DropRate_Type.__name__ = "TSlopeDropRate"
_TSlopeLoQueue8DropRate_Object = MibTableColumn
tSlopeLoQueue8DropRate = _TSlopeLoQueue8DropRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 16),
    _TSlopeLoQueue8DropRate_Type()
)
tSlopeLoQueue8DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoQueue8DropRate.setStatus("current")


class _TSlopeHiStartThreshold_Type(TSlopeThreshold):
    """Custom type tSlopeHiStartThreshold based on TSlopeThreshold"""
    defaultValue = 75


_TSlopeHiStartThreshold_Type.__name__ = "TSlopeThreshold"
_TSlopeHiStartThreshold_Object = MibTableColumn
tSlopeHiStartThreshold = _TSlopeHiStartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 17),
    _TSlopeHiStartThreshold_Type()
)
tSlopeHiStartThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiStartThreshold.setStatus("current")


class _TSlopeLoStartThreshold_Type(TSlopeThreshold):
    """Custom type tSlopeLoStartThreshold based on TSlopeThreshold"""
    defaultValue = 50


_TSlopeLoStartThreshold_Type.__name__ = "TSlopeThreshold"
_TSlopeLoStartThreshold_Object = MibTableColumn
tSlopeLoStartThreshold = _TSlopeLoStartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 1, 1, 18),
    _TSlopeLoStartThreshold_Type()
)
tSlopeLoStartThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoStartThreshold.setStatus("current")
_TSlopePolicyQueueTable_Object = MibTable
tSlopePolicyQueueTable = _TSlopePolicyQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tSlopePolicyQueueTable.setStatus("current")
_TSlopePolicyQueueEntry_Object = MibTableRow
tSlopePolicyQueueEntry = _TSlopePolicyQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1)
)
tSlopePolicyQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSlopePolicy"),
    (0, "TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueId"),
)
if mibBuilder.loadTexts:
    tSlopePolicyQueueEntry.setStatus("current")


class _TSlopePolicyQueueId_Type(TQueueId):
    """Custom type tSlopePolicyQueueId based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TSlopePolicyQueueId_Type.__name__ = "TQueueId"
_TSlopePolicyQueueId_Object = MibTableColumn
tSlopePolicyQueueId = _TSlopePolicyQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 1),
    _TSlopePolicyQueueId_Type()
)
tSlopePolicyQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSlopePolicyQueueId.setStatus("current")
_TSlopePolicyQueueRowStatus_Type = RowStatus
_TSlopePolicyQueueRowStatus_Object = MibTableColumn
tSlopePolicyQueueRowStatus = _TSlopePolicyQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 2),
    _TSlopePolicyQueueRowStatus_Type()
)
tSlopePolicyQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueRowStatus.setStatus("current")
_TSlopePolicyQueueLastChanged_Type = TimeStamp
_TSlopePolicyQueueLastChanged_Object = MibTableColumn
tSlopePolicyQueueLastChanged = _TSlopePolicyQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 3),
    _TSlopePolicyQueueLastChanged_Type()
)
tSlopePolicyQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSlopePolicyQueueLastChanged.setStatus("current")


class _TSlopePolicyQueueHiAdminStatus_Type(Integer32):
    """Custom type tSlopePolicyQueueHiAdminStatus based on Integer32"""
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


_TSlopePolicyQueueHiAdminStatus_Type.__name__ = "Integer32"
_TSlopePolicyQueueHiAdminStatus_Object = MibTableColumn
tSlopePolicyQueueHiAdminStatus = _TSlopePolicyQueueHiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 4),
    _TSlopePolicyQueueHiAdminStatus_Type()
)
tSlopePolicyQueueHiAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueHiAdminStatus.setStatus("current")


class _TSlopePolicyQueueHiStartAverage_Type(Unsigned32):
    """Custom type tSlopePolicyQueueHiStartAverage based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopePolicyQueueHiStartAverage_Type.__name__ = "Unsigned32"
_TSlopePolicyQueueHiStartAverage_Object = MibTableColumn
tSlopePolicyQueueHiStartAverage = _TSlopePolicyQueueHiStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 5),
    _TSlopePolicyQueueHiStartAverage_Type()
)
tSlopePolicyQueueHiStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueHiStartAverage.setStatus("current")


class _TSlopePolicyQueueHiMaxAverage_Type(Unsigned32):
    """Custom type tSlopePolicyQueueHiMaxAverage based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopePolicyQueueHiMaxAverage_Type.__name__ = "Unsigned32"
_TSlopePolicyQueueHiMaxAverage_Object = MibTableColumn
tSlopePolicyQueueHiMaxAverage = _TSlopePolicyQueueHiMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 6),
    _TSlopePolicyQueueHiMaxAverage_Type()
)
tSlopePolicyQueueHiMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueHiMaxAverage.setStatus("current")


class _TSlopePolicyQueueHiMaxProbability_Type(TMaxProbability):
    """Custom type tSlopePolicyQueueHiMaxProbability based on TMaxProbability"""
    defaultValue = 75


_TSlopePolicyQueueHiMaxProbability_Type.__name__ = "TMaxProbability"
_TSlopePolicyQueueHiMaxProbability_Object = MibTableColumn
tSlopePolicyQueueHiMaxProbability = _TSlopePolicyQueueHiMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 7),
    _TSlopePolicyQueueHiMaxProbability_Type()
)
tSlopePolicyQueueHiMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueHiMaxProbability.setStatus("current")


class _TSlopePolicyQueueLoAdminStatus_Type(Integer32):
    """Custom type tSlopePolicyQueueLoAdminStatus based on Integer32"""
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


_TSlopePolicyQueueLoAdminStatus_Type.__name__ = "Integer32"
_TSlopePolicyQueueLoAdminStatus_Object = MibTableColumn
tSlopePolicyQueueLoAdminStatus = _TSlopePolicyQueueLoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 8),
    _TSlopePolicyQueueLoAdminStatus_Type()
)
tSlopePolicyQueueLoAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueLoAdminStatus.setStatus("current")


class _TSlopePolicyQueueLoStartAverage_Type(Unsigned32):
    """Custom type tSlopePolicyQueueLoStartAverage based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopePolicyQueueLoStartAverage_Type.__name__ = "Unsigned32"
_TSlopePolicyQueueLoStartAverage_Object = MibTableColumn
tSlopePolicyQueueLoStartAverage = _TSlopePolicyQueueLoStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 9),
    _TSlopePolicyQueueLoStartAverage_Type()
)
tSlopePolicyQueueLoStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueLoStartAverage.setStatus("current")


class _TSlopePolicyQueueLoMaxAverage_Type(Unsigned32):
    """Custom type tSlopePolicyQueueLoMaxAverage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopePolicyQueueLoMaxAverage_Type.__name__ = "Unsigned32"
_TSlopePolicyQueueLoMaxAverage_Object = MibTableColumn
tSlopePolicyQueueLoMaxAverage = _TSlopePolicyQueueLoMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 10),
    _TSlopePolicyQueueLoMaxAverage_Type()
)
tSlopePolicyQueueLoMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueLoMaxAverage.setStatus("current")


class _TSlopePolicyQueueLoMaxProbability_Type(TMaxProbability):
    """Custom type tSlopePolicyQueueLoMaxProbability based on TMaxProbability"""
    defaultValue = 75


_TSlopePolicyQueueLoMaxProbability_Type.__name__ = "TMaxProbability"
_TSlopePolicyQueueLoMaxProbability_Object = MibTableColumn
tSlopePolicyQueueLoMaxProbability = _TSlopePolicyQueueLoMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 11),
    _TSlopePolicyQueueLoMaxProbability_Type()
)
tSlopePolicyQueueLoMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueLoMaxProbability.setStatus("current")


class _TSlopePolicyQueueNonTcpAdminStatus_Type(Integer32):
    """Custom type tSlopePolicyQueueNonTcpAdminStatus based on Integer32"""
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


_TSlopePolicyQueueNonTcpAdminStatus_Type.__name__ = "Integer32"
_TSlopePolicyQueueNonTcpAdminStatus_Object = MibTableColumn
tSlopePolicyQueueNonTcpAdminStatus = _TSlopePolicyQueueNonTcpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 12),
    _TSlopePolicyQueueNonTcpAdminStatus_Type()
)
tSlopePolicyQueueNonTcpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueNonTcpAdminStatus.setStatus("current")


class _TSlopePolicyQueueNonTcpStartAverage_Type(Unsigned32):
    """Custom type tSlopePolicyQueueNonTcpStartAverage based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopePolicyQueueNonTcpStartAverage_Type.__name__ = "Unsigned32"
_TSlopePolicyQueueNonTcpStartAverage_Object = MibTableColumn
tSlopePolicyQueueNonTcpStartAverage = _TSlopePolicyQueueNonTcpStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 13),
    _TSlopePolicyQueueNonTcpStartAverage_Type()
)
tSlopePolicyQueueNonTcpStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueNonTcpStartAverage.setStatus("current")


class _TSlopePolicyQueueNonTcpMaxAverage_Type(Unsigned32):
    """Custom type tSlopePolicyQueueNonTcpMaxAverage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopePolicyQueueNonTcpMaxAverage_Type.__name__ = "Unsigned32"
_TSlopePolicyQueueNonTcpMaxAverage_Object = MibTableColumn
tSlopePolicyQueueNonTcpMaxAverage = _TSlopePolicyQueueNonTcpMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 14),
    _TSlopePolicyQueueNonTcpMaxAverage_Type()
)
tSlopePolicyQueueNonTcpMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueNonTcpMaxAverage.setStatus("current")


class _TSlopePolicyQueueNonTcpMaxProbability_Type(TMaxProbability):
    """Custom type tSlopePolicyQueueNonTcpMaxProbability based on TMaxProbability"""
    defaultValue = 75


_TSlopePolicyQueueNonTcpMaxProbability_Type.__name__ = "TMaxProbability"
_TSlopePolicyQueueNonTcpMaxProbability_Object = MibTableColumn
tSlopePolicyQueueNonTcpMaxProbability = _TSlopePolicyQueueNonTcpMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 15),
    _TSlopePolicyQueueNonTcpMaxProbability_Type()
)
tSlopePolicyQueueNonTcpMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueNonTcpMaxProbability.setStatus("current")


class _TSlopePolicyQueueTimeAvgFactor_Type(Unsigned32):
    """Custom type tSlopePolicyQueueTimeAvgFactor based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TSlopePolicyQueueTimeAvgFactor_Type.__name__ = "Unsigned32"
_TSlopePolicyQueueTimeAvgFactor_Object = MibTableColumn
tSlopePolicyQueueTimeAvgFactor = _TSlopePolicyQueueTimeAvgFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 4, 2, 1, 16),
    _TSlopePolicyQueueTimeAvgFactor_Type()
)
tSlopePolicyQueueTimeAvgFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopePolicyQueueTimeAvgFactor.setStatus("current")
_TSasSchedulerObjects_ObjectIdentity = ObjectIdentity
tSasSchedulerObjects = _TSasSchedulerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5)
)
_TSasPortSchedulerPlcyTable_Object = MibTable
tSasPortSchedulerPlcyTable = _TSasPortSchedulerPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tSasPortSchedulerPlcyTable.setStatus("current")
_TSasPortSchedulerPlcyEntry_Object = MibTableRow
tSasPortSchedulerPlcyEntry = _TSasPortSchedulerPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tSasPortSchedulerPlcyEntry.setStatus("current")


class _TPortSchedulerPlcyMode_Type(TPlcyMode):
    """Custom type tPortSchedulerPlcyMode based on TPlcyMode"""
    defaultValue = 0


_TPortSchedulerPlcyMode_Type.__name__ = "TPlcyMode"
_TPortSchedulerPlcyMode_Object = MibTableColumn
tPortSchedulerPlcyMode = _TPortSchedulerPlcyMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 1),
    _TPortSchedulerPlcyMode_Type()
)
tPortSchedulerPlcyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyMode.setStatus("current")


class _TPortSchedulerPlcyQuanta_Type(TPlcyQuanta):
    """Custom type tPortSchedulerPlcyQuanta based on TPlcyQuanta"""
    defaultValue = 0


_TPortSchedulerPlcyQuanta_Type.__name__ = "TPlcyQuanta"
_TPortSchedulerPlcyQuanta_Object = MibTableColumn
tPortSchedulerPlcyQuanta = _TPortSchedulerPlcyQuanta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 2),
    _TPortSchedulerPlcyQuanta_Type()
)
tPortSchedulerPlcyQuanta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQuanta.setStatus("current")


class _TPortSchedulerPlcyQueue1Weight_Type(TQWeight):
    """Custom type tPortSchedulerPlcyQueue1Weight based on TQWeight"""
    defaultValue = 1


_TPortSchedulerPlcyQueue1Weight_Type.__name__ = "TQWeight"
_TPortSchedulerPlcyQueue1Weight_Object = MibTableColumn
tPortSchedulerPlcyQueue1Weight = _TPortSchedulerPlcyQueue1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 3),
    _TPortSchedulerPlcyQueue1Weight_Type()
)
tPortSchedulerPlcyQueue1Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQueue1Weight.setStatus("current")


class _TPortSchedulerPlcyQueue2Weight_Type(TQWeight):
    """Custom type tPortSchedulerPlcyQueue2Weight based on TQWeight"""
    defaultValue = 1


_TPortSchedulerPlcyQueue2Weight_Type.__name__ = "TQWeight"
_TPortSchedulerPlcyQueue2Weight_Object = MibTableColumn
tPortSchedulerPlcyQueue2Weight = _TPortSchedulerPlcyQueue2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 4),
    _TPortSchedulerPlcyQueue2Weight_Type()
)
tPortSchedulerPlcyQueue2Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQueue2Weight.setStatus("current")


class _TPortSchedulerPlcyQueue3Weight_Type(TQWeight):
    """Custom type tPortSchedulerPlcyQueue3Weight based on TQWeight"""
    defaultValue = 1


_TPortSchedulerPlcyQueue3Weight_Type.__name__ = "TQWeight"
_TPortSchedulerPlcyQueue3Weight_Object = MibTableColumn
tPortSchedulerPlcyQueue3Weight = _TPortSchedulerPlcyQueue3Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 5),
    _TPortSchedulerPlcyQueue3Weight_Type()
)
tPortSchedulerPlcyQueue3Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQueue3Weight.setStatus("current")


class _TPortSchedulerPlcyQueue4Weight_Type(TQWeight):
    """Custom type tPortSchedulerPlcyQueue4Weight based on TQWeight"""
    defaultValue = 1


_TPortSchedulerPlcyQueue4Weight_Type.__name__ = "TQWeight"
_TPortSchedulerPlcyQueue4Weight_Object = MibTableColumn
tPortSchedulerPlcyQueue4Weight = _TPortSchedulerPlcyQueue4Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 6),
    _TPortSchedulerPlcyQueue4Weight_Type()
)
tPortSchedulerPlcyQueue4Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQueue4Weight.setStatus("current")


class _TPortSchedulerPlcyQueue5Weight_Type(TQWeight):
    """Custom type tPortSchedulerPlcyQueue5Weight based on TQWeight"""
    defaultValue = 1


_TPortSchedulerPlcyQueue5Weight_Type.__name__ = "TQWeight"
_TPortSchedulerPlcyQueue5Weight_Object = MibTableColumn
tPortSchedulerPlcyQueue5Weight = _TPortSchedulerPlcyQueue5Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 7),
    _TPortSchedulerPlcyQueue5Weight_Type()
)
tPortSchedulerPlcyQueue5Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQueue5Weight.setStatus("current")


class _TPortSchedulerPlcyQueue6Weight_Type(TQWeight):
    """Custom type tPortSchedulerPlcyQueue6Weight based on TQWeight"""
    defaultValue = 1


_TPortSchedulerPlcyQueue6Weight_Type.__name__ = "TQWeight"
_TPortSchedulerPlcyQueue6Weight_Object = MibTableColumn
tPortSchedulerPlcyQueue6Weight = _TPortSchedulerPlcyQueue6Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 8),
    _TPortSchedulerPlcyQueue6Weight_Type()
)
tPortSchedulerPlcyQueue6Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQueue6Weight.setStatus("current")


class _TPortSchedulerPlcyQueue7Weight_Type(TQWeight):
    """Custom type tPortSchedulerPlcyQueue7Weight based on TQWeight"""
    defaultValue = 1


_TPortSchedulerPlcyQueue7Weight_Type.__name__ = "TQWeight"
_TPortSchedulerPlcyQueue7Weight_Object = MibTableColumn
tPortSchedulerPlcyQueue7Weight = _TPortSchedulerPlcyQueue7Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 9),
    _TPortSchedulerPlcyQueue7Weight_Type()
)
tPortSchedulerPlcyQueue7Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQueue7Weight.setStatus("current")


class _TPortSchedulerPlcyQueue8Weight_Type(TQWeight):
    """Custom type tPortSchedulerPlcyQueue8Weight based on TQWeight"""
    defaultValue = 1


_TPortSchedulerPlcyQueue8Weight_Type.__name__ = "TQWeight"
_TPortSchedulerPlcyQueue8Weight_Object = MibTableColumn
tPortSchedulerPlcyQueue8Weight = _TPortSchedulerPlcyQueue8Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 5, 1, 1, 10),
    _TPortSchedulerPlcyQueue8Weight_Type()
)
tPortSchedulerPlcyQueue8Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyQueue8Weight.setStatus("current")
_TQosFrameBasedAccntObjects_ObjectIdentity = ObjectIdentity
tQosFrameBasedAccntObjects = _TQosFrameBasedAccntObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 6)
)


class _TQosIngressFrameBasedAccnt_Type(TruthValue):
    """Custom type tQosIngressFrameBasedAccnt based on TruthValue"""
    defaultValue = 2


_TQosIngressFrameBasedAccnt_Type.__name__ = "TruthValue"
_TQosIngressFrameBasedAccnt_Object = MibScalar
tQosIngressFrameBasedAccnt = _TQosIngressFrameBasedAccnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 6, 1),
    _TQosIngressFrameBasedAccnt_Type()
)
tQosIngressFrameBasedAccnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngressFrameBasedAccnt.setStatus("current")


class _TQosEgressFrameBasedAccnt_Type(TruthValue):
    """Custom type tQosEgressFrameBasedAccnt based on TruthValue"""
    defaultValue = 2


_TQosEgressFrameBasedAccnt_Type.__name__ = "TruthValue"
_TQosEgressFrameBasedAccnt_Object = MibScalar
tQosEgressFrameBasedAccnt = _TQosEgressFrameBasedAccnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 6, 2),
    _TQosEgressFrameBasedAccnt_Type()
)
tQosEgressFrameBasedAccnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgressFrameBasedAccnt.setStatus("current")
_TSASNetworkObjects_ObjectIdentity = ObjectIdentity
tSASNetworkObjects = _TSASNetworkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7)
)
_TNetworkPolicyExtnTable_Object = MibTable
tNetworkPolicyExtnTable = _TNetworkPolicyExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tNetworkPolicyExtnTable.setStatus("current")
_TNetworkPolicyExtnEntry_Object = MibTableRow
tNetworkPolicyExtnEntry = _TNetworkPolicyExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    tNetworkPolicyExtnEntry.setStatus("current")


class _TNetworkPolicyType_Type(TNetworkPolicyType):
    """Custom type tNetworkPolicyType based on TNetworkPolicyType"""
    defaultValue = 1


_TNetworkPolicyType_Type.__name__ = "TNetworkPolicyType"
_TNetworkPolicyType_Object = MibTableColumn
tNetworkPolicyType = _TNetworkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 1, 1, 1),
    _TNetworkPolicyType_Type()
)
tNetworkPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyType.setStatus("current")


class _TNetworkPolicyRemarkPolicyId_Type(TRemarkPolicyID):
    """Custom type tNetworkPolicyRemarkPolicyId based on TRemarkPolicyID"""
    defaultValue = 2


_TNetworkPolicyRemarkPolicyId_Type.__name__ = "TRemarkPolicyID"
_TNetworkPolicyRemarkPolicyId_Object = MibTableColumn
tNetworkPolicyRemarkPolicyId = _TNetworkPolicyRemarkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 1, 1, 2),
    _TNetworkPolicyRemarkPolicyId_Type()
)
tNetworkPolicyRemarkPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyRemarkPolicyId.setStatus("current")


class _TNetworkIngressMeterColorMode_Type(Integer32):
    """Custom type tNetworkIngressMeterColorMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 1),
          ("color-blind", 2))
    )


_TNetworkIngressMeterColorMode_Type.__name__ = "Integer32"
_TNetworkIngressMeterColorMode_Object = MibTableColumn
tNetworkIngressMeterColorMode = _TNetworkIngressMeterColorMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 1, 1, 3),
    _TNetworkIngressMeterColorMode_Type()
)
tNetworkIngressMeterColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressMeterColorMode.setStatus("current")


class _TNetworkIngressMplsLspExpProfile_Type(TMplsLspExpProfMapID):
    """Custom type tNetworkIngressMplsLspExpProfile based on TMplsLspExpProfMapID"""
    defaultValue = 1


_TNetworkIngressMplsLspExpProfile_Type.__name__ = "TMplsLspExpProfMapID"
_TNetworkIngressMplsLspExpProfile_Object = MibTableColumn
tNetworkIngressMplsLspExpProfile = _TNetworkIngressMplsLspExpProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 1, 1, 4),
    _TNetworkIngressMplsLspExpProfile_Type()
)
tNetworkIngressMplsLspExpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkIngressMplsLspExpProfile.setStatus("current")


class _TNetworkEgressRemarkType_Type(Integer32):
    """Custom type tNetworkEgressRemarkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("use-dot1p", 1),
          ("use-dscp", 2),
          ("all", 3))
    )


_TNetworkEgressRemarkType_Type.__name__ = "Integer32"
_TNetworkEgressRemarkType_Object = MibTableColumn
tNetworkEgressRemarkType = _TNetworkEgressRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 1, 1, 5),
    _TNetworkEgressRemarkType_Type()
)
tNetworkEgressRemarkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkEgressRemarkType.setStatus("current")
_TNetworkQueueExtnTable_Object = MibTable
tNetworkQueueExtnTable = _TNetworkQueueExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    tNetworkQueueExtnTable.setStatus("current")
_TNetworkQueueExtnEntry_Object = MibTableRow
tNetworkQueueExtnEntry = _TNetworkQueueExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    tNetworkQueueExtnEntry.setStatus("current")


class _TNetworkQueuePolicyName_Type(TNamedItem):
    """Custom type tNetworkQueuePolicyName based on TNamedItem"""
    defaultValue = OctetString("default")


_TNetworkQueuePolicyName_Type.__name__ = "TNamedItem"
_TNetworkQueuePolicyName_Object = MibTableColumn
tNetworkQueuePolicyName = _TNetworkQueuePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 2, 1, 1),
    _TNetworkQueuePolicyName_Type()
)
tNetworkQueuePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyName.setStatus("current")


class _TNetworkQueuePolicyQueueMode_Type(Integer32):
    """Custom type tNetworkQueuePolicyQueueMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("strict-ef", 1),
          ("strict", 2),
          ("weighted", 3))
    )


_TNetworkQueuePolicyQueueMode_Type.__name__ = "Integer32"
_TNetworkQueuePolicyQueueMode_Object = MibTableColumn
tNetworkQueuePolicyQueueMode = _TNetworkQueuePolicyQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 2, 1, 2),
    _TNetworkQueuePolicyQueueMode_Type()
)
tNetworkQueuePolicyQueueMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyQueueMode.setStatus("current")


class _TNetworkQueuePolicyWeight_Type(Integer32):
    """Custom type tNetworkQueuePolicyWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TNetworkQueuePolicyWeight_Type.__name__ = "Integer32"
_TNetworkQueuePolicyWeight_Object = MibTableColumn
tNetworkQueuePolicyWeight = _TNetworkQueuePolicyWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 2, 1, 3),
    _TNetworkQueuePolicyWeight_Type()
)
tNetworkQueuePolicyWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyWeight.setStatus("current")
_TNetworkEgressFCExtnTable_Object = MibTable
tNetworkEgressFCExtnTable = _TNetworkEgressFCExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    tNetworkEgressFCExtnTable.setStatus("current")
_TNetworkEgressFCExtnEntry_Object = MibTableRow
tNetworkEgressFCExtnEntry = _TNetworkEgressFCExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    tNetworkEgressFCExtnEntry.setStatus("current")
_TNetworkEgressFCDot1pProfile_Type = Dot1PPriority
_TNetworkEgressFCDot1pProfile_Object = MibTableColumn
tNetworkEgressFCDot1pProfile = _TNetworkEgressFCDot1pProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 7, 3, 1, 1),
    _TNetworkEgressFCDot1pProfile_Type()
)
tNetworkEgressFCDot1pProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCDot1pProfile.setStatus("current")
_TSASQueueMgmtObjects_ObjectIdentity = ObjectIdentity
tSASQueueMgmtObjects = _TSASQueueMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8)
)
_TQueueMgmtPolicyTable_Object = MibTable
tQueueMgmtPolicyTable = _TQueueMgmtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tQueueMgmtPolicyTable.setStatus("current")
_TQueueMgmtPolicyEntry_Object = MibTableRow
tQueueMgmtPolicyEntry = _TQueueMgmtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1)
)
tQueueMgmtPolicyEntry.setIndexNames(
    (0, "TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyName"),
)
if mibBuilder.loadTexts:
    tQueueMgmtPolicyEntry.setStatus("current")
_TQueueMgmtPolicyName_Type = TNamedItem
_TQueueMgmtPolicyName_Object = MibTableColumn
tQueueMgmtPolicyName = _TQueueMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 1),
    _TQueueMgmtPolicyName_Type()
)
tQueueMgmtPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyName.setStatus("current")
_TQueueMgmtPolicyRowStatus_Type = RowStatus
_TQueueMgmtPolicyRowStatus_Object = MibTableColumn
tQueueMgmtPolicyRowStatus = _TQueueMgmtPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 2),
    _TQueueMgmtPolicyRowStatus_Type()
)
tQueueMgmtPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyRowStatus.setStatus("current")
_TQueueMgmtPolicyLastChanged_Type = TimeStamp
_TQueueMgmtPolicyLastChanged_Object = MibTableColumn
tQueueMgmtPolicyLastChanged = _TQueueMgmtPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 3),
    _TQueueMgmtPolicyLastChanged_Type()
)
tQueueMgmtPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyLastChanged.setStatus("current")


class _TQueueMgmtPolicyDescription_Type(TItemDescription):
    """Custom type tQueueMgmtPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TQueueMgmtPolicyDescription_Type.__name__ = "TItemDescription"
_TQueueMgmtPolicyDescription_Object = MibTableColumn
tQueueMgmtPolicyDescription = _TQueueMgmtPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 4),
    _TQueueMgmtPolicyDescription_Type()
)
tQueueMgmtPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyDescription.setStatus("current")


class _TQueueMgmtPolicyHiAdminStatus_Type(Integer32):
    """Custom type tQueueMgmtPolicyHiAdminStatus based on Integer32"""
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


_TQueueMgmtPolicyHiAdminStatus_Type.__name__ = "Integer32"
_TQueueMgmtPolicyHiAdminStatus_Object = MibTableColumn
tQueueMgmtPolicyHiAdminStatus = _TQueueMgmtPolicyHiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 5),
    _TQueueMgmtPolicyHiAdminStatus_Type()
)
tQueueMgmtPolicyHiAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyHiAdminStatus.setStatus("current")


class _TQueueMgmtPolicyHiStartAverage_Type(Unsigned32):
    """Custom type tQueueMgmtPolicyHiStartAverage based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQueueMgmtPolicyHiStartAverage_Type.__name__ = "Unsigned32"
_TQueueMgmtPolicyHiStartAverage_Object = MibTableColumn
tQueueMgmtPolicyHiStartAverage = _TQueueMgmtPolicyHiStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 6),
    _TQueueMgmtPolicyHiStartAverage_Type()
)
tQueueMgmtPolicyHiStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyHiStartAverage.setStatus("current")


class _TQueueMgmtPolicyHiMaxAverage_Type(Unsigned32):
    """Custom type tQueueMgmtPolicyHiMaxAverage based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQueueMgmtPolicyHiMaxAverage_Type.__name__ = "Unsigned32"
_TQueueMgmtPolicyHiMaxAverage_Object = MibTableColumn
tQueueMgmtPolicyHiMaxAverage = _TQueueMgmtPolicyHiMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 7),
    _TQueueMgmtPolicyHiMaxAverage_Type()
)
tQueueMgmtPolicyHiMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyHiMaxAverage.setStatus("current")


class _TQueueMgmtPolicyHiMaxProbability_Type(Unsigned32):
    """Custom type tQueueMgmtPolicyHiMaxProbability based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TQueueMgmtPolicyHiMaxProbability_Type.__name__ = "Unsigned32"
_TQueueMgmtPolicyHiMaxProbability_Object = MibTableColumn
tQueueMgmtPolicyHiMaxProbability = _TQueueMgmtPolicyHiMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 8),
    _TQueueMgmtPolicyHiMaxProbability_Type()
)
tQueueMgmtPolicyHiMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyHiMaxProbability.setStatus("current")


class _TQueueMgmtPolicyLoAdminStatus_Type(Integer32):
    """Custom type tQueueMgmtPolicyLoAdminStatus based on Integer32"""
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


_TQueueMgmtPolicyLoAdminStatus_Type.__name__ = "Integer32"
_TQueueMgmtPolicyLoAdminStatus_Object = MibTableColumn
tQueueMgmtPolicyLoAdminStatus = _TQueueMgmtPolicyLoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 9),
    _TQueueMgmtPolicyLoAdminStatus_Type()
)
tQueueMgmtPolicyLoAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyLoAdminStatus.setStatus("current")


class _TQueueMgmtPolicyLoStartAverage_Type(Unsigned32):
    """Custom type tQueueMgmtPolicyLoStartAverage based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQueueMgmtPolicyLoStartAverage_Type.__name__ = "Unsigned32"
_TQueueMgmtPolicyLoStartAverage_Object = MibTableColumn
tQueueMgmtPolicyLoStartAverage = _TQueueMgmtPolicyLoStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 10),
    _TQueueMgmtPolicyLoStartAverage_Type()
)
tQueueMgmtPolicyLoStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyLoStartAverage.setStatus("current")


class _TQueueMgmtPolicyLoMaxAverage_Type(Unsigned32):
    """Custom type tQueueMgmtPolicyLoMaxAverage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQueueMgmtPolicyLoMaxAverage_Type.__name__ = "Unsigned32"
_TQueueMgmtPolicyLoMaxAverage_Object = MibTableColumn
tQueueMgmtPolicyLoMaxAverage = _TQueueMgmtPolicyLoMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 11),
    _TQueueMgmtPolicyLoMaxAverage_Type()
)
tQueueMgmtPolicyLoMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyLoMaxAverage.setStatus("current")


class _TQueueMgmtPolicyLoMaxProbability_Type(Unsigned32):
    """Custom type tQueueMgmtPolicyLoMaxProbability based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TQueueMgmtPolicyLoMaxProbability_Type.__name__ = "Unsigned32"
_TQueueMgmtPolicyLoMaxProbability_Object = MibTableColumn
tQueueMgmtPolicyLoMaxProbability = _TQueueMgmtPolicyLoMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 12),
    _TQueueMgmtPolicyLoMaxProbability_Type()
)
tQueueMgmtPolicyLoMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyLoMaxProbability.setStatus("current")


class _TQueueMgmtPolicyCBS_Type(Integer32):
    """Custom type tQueueMgmtPolicyCBS based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 800000),
    )


_TQueueMgmtPolicyCBS_Type.__name__ = "Integer32"
_TQueueMgmtPolicyCBS_Object = MibTableColumn
tQueueMgmtPolicyCBS = _TQueueMgmtPolicyCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 13),
    _TQueueMgmtPolicyCBS_Type()
)
tQueueMgmtPolicyCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyCBS.setStatus("current")


class _TQueueMgmtPolicyMBS_Type(Integer32):
    """Custom type tQueueMgmtPolicyMBS based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 800000),
    )


_TQueueMgmtPolicyMBS_Type.__name__ = "Integer32"
_TQueueMgmtPolicyMBS_Object = MibTableColumn
tQueueMgmtPolicyMBS = _TQueueMgmtPolicyMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 14),
    _TQueueMgmtPolicyMBS_Type()
)
tQueueMgmtPolicyMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyMBS.setStatus("current")


class _TQueueMgmtPolicyTimeAvgFactor_Type(Unsigned32):
    """Custom type tQueueMgmtPolicyTimeAvgFactor based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TQueueMgmtPolicyTimeAvgFactor_Type.__name__ = "Unsigned32"
_TQueueMgmtPolicyTimeAvgFactor_Object = MibTableColumn
tQueueMgmtPolicyTimeAvgFactor = _TQueueMgmtPolicyTimeAvgFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 15),
    _TQueueMgmtPolicyTimeAvgFactor_Type()
)
tQueueMgmtPolicyTimeAvgFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyTimeAvgFactor.setStatus("current")


class _TQueueMgmtPolicyScope_Type(TItemScope):
    """Custom type tQueueMgmtPolicyScope based on TItemScope"""
    defaultValue = 2


_TQueueMgmtPolicyScope_Type.__name__ = "TItemScope"
_TQueueMgmtPolicyScope_Object = MibTableColumn
tQueueMgmtPolicyScope = _TQueueMgmtPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 8, 1, 1, 16),
    _TQueueMgmtPolicyScope_Type()
)
tQueueMgmtPolicyScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQueueMgmtPolicyScope.setStatus("current")
_TSASSapEgressObjects_ObjectIdentity = ObjectIdentity
tSASSapEgressObjects = _TSASSapEgressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9)
)
_TSapEgressExtnTable_Object = MibTable
tSapEgressExtnTable = _TSapEgressExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tSapEgressExtnTable.setStatus("current")
_TSapEgressExtnEntry_Object = MibTableRow
tSapEgressExtnEntry = _TSapEgressExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tSapEgressExtnEntry.setStatus("current")


class _TSapEgressRemark_Type(TruthValue):
    """Custom type tSapEgressRemark based on TruthValue"""
    defaultValue = 2


_TSapEgressRemark_Type.__name__ = "TruthValue"
_TSapEgressRemark_Object = MibTableColumn
tSapEgressRemark = _TSapEgressRemark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 1, 1, 1),
    _TSapEgressRemark_Type()
)
tSapEgressRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressRemark.setStatus("current")


class _TSapEgressRemarkPolicyId_Type(TRemarkPolicyID):
    """Custom type tSapEgressRemarkPolicyId based on TRemarkPolicyID"""
    defaultValue = 1


_TSapEgressRemarkPolicyId_Type.__name__ = "TRemarkPolicyID"
_TSapEgressRemarkPolicyId_Object = MibTableColumn
tSapEgressRemarkPolicyId = _TSapEgressRemarkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 1, 1, 2),
    _TSapEgressRemarkPolicyId_Type()
)
tSapEgressRemarkPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressRemarkPolicyId.setStatus("current")
_TSapEgressQueueExtnTable_Object = MibTable
tSapEgressQueueExtnTable = _TSapEgressQueueExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tSapEgressQueueExtnTable.setStatus("current")
_TSapEgressQueueExtnEntry_Object = MibTableRow
tSapEgressQueueExtnEntry = _TSapEgressQueueExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    tSapEgressQueueExtnEntry.setStatus("current")


class _TSapEgressQueuePolicyName_Type(TNamedItem):
    """Custom type tSapEgressQueuePolicyName based on TNamedItem"""
    defaultValue = OctetString("default")


_TSapEgressQueuePolicyName_Type.__name__ = "TNamedItem"
_TSapEgressQueuePolicyName_Object = MibTableColumn
tSapEgressQueuePolicyName = _TSapEgressQueuePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 2, 1, 1),
    _TSapEgressQueuePolicyName_Type()
)
tSapEgressQueuePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePolicyName.setStatus("current")


class _TSapEgressQueuePolicyQueueMode_Type(Integer32):
    """Custom type tSapEgressQueuePolicyQueueMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("strict-ef", 1),
          ("strict", 2),
          ("weighted", 3))
    )


_TSapEgressQueuePolicyQueueMode_Type.__name__ = "Integer32"
_TSapEgressQueuePolicyQueueMode_Object = MibTableColumn
tSapEgressQueuePolicyQueueMode = _TSapEgressQueuePolicyQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 2, 1, 2),
    _TSapEgressQueuePolicyQueueMode_Type()
)
tSapEgressQueuePolicyQueueMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePolicyQueueMode.setStatus("current")


class _TSapEgressQueuePolicyWeight_Type(Integer32):
    """Custom type tSapEgressQueuePolicyWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TSapEgressQueuePolicyWeight_Type.__name__ = "Integer32"
_TSapEgressQueuePolicyWeight_Object = MibTableColumn
tSapEgressQueuePolicyWeight = _TSapEgressQueuePolicyWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 9, 2, 1, 3),
    _TSapEgressQueuePolicyWeight_Type()
)
tSapEgressQueuePolicyWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePolicyWeight.setStatus("current")
_TMplsQosObjects_ObjectIdentity = ObjectIdentity
tMplsQosObjects = _TMplsQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10)
)
_TMplsLspExpProfMapTable_Object = MibTable
tMplsLspExpProfMapTable = _TMplsLspExpProfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tMplsLspExpProfMapTable.setStatus("current")
_TMplsLspExpProfMapEntry_Object = MibTableRow
tMplsLspExpProfMapEntry = _TMplsLspExpProfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 1, 1)
)
tMplsLspExpProfMapEntry.setIndexNames(
    (0, "TIMETRA-SAS-QOS-MIB", "tMplsLspExpProfMapIndex"),
)
if mibBuilder.loadTexts:
    tMplsLspExpProfMapEntry.setStatus("current")
_TMplsLspExpProfMapIndex_Type = TMplsLspExpProfMapID
_TMplsLspExpProfMapIndex_Object = MibTableColumn
tMplsLspExpProfMapIndex = _TMplsLspExpProfMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 1, 1, 1),
    _TMplsLspExpProfMapIndex_Type()
)
tMplsLspExpProfMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMplsLspExpProfMapIndex.setStatus("current")
_TMplsLspExpProfMapRowStatus_Type = RowStatus
_TMplsLspExpProfMapRowStatus_Object = MibTableColumn
tMplsLspExpProfMapRowStatus = _TMplsLspExpProfMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 1, 1, 2),
    _TMplsLspExpProfMapRowStatus_Type()
)
tMplsLspExpProfMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMplsLspExpProfMapRowStatus.setStatus("current")


class _TMplsLspExpProfMapDescription_Type(TItemDescription):
    """Custom type tMplsLspExpProfMapDescription based on TItemDescription"""
    defaultHexValue = ""


_TMplsLspExpProfMapDescription_Type.__name__ = "TItemDescription"
_TMplsLspExpProfMapDescription_Object = MibTableColumn
tMplsLspExpProfMapDescription = _TMplsLspExpProfMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 1, 1, 3),
    _TMplsLspExpProfMapDescription_Type()
)
tMplsLspExpProfMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMplsLspExpProfMapDescription.setStatus("current")
_TMplsLspExpProfMapLastChanged_Type = TimeStamp
_TMplsLspExpProfMapLastChanged_Object = MibTableColumn
tMplsLspExpProfMapLastChanged = _TMplsLspExpProfMapLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 1, 1, 4),
    _TMplsLspExpProfMapLastChanged_Type()
)
tMplsLspExpProfMapLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMplsLspExpProfMapLastChanged.setStatus("current")


class _TGlobalMplsLspExpProfile_Type(TMplsLspExpProfMapID):
    """Custom type tGlobalMplsLspExpProfile based on TMplsLspExpProfMapID"""
    defaultValue = 1


_TGlobalMplsLspExpProfile_Type.__name__ = "TMplsLspExpProfMapID"
_TGlobalMplsLspExpProfile_Object = MibScalar
tGlobalMplsLspExpProfile = _TGlobalMplsLspExpProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 3),
    _TGlobalMplsLspExpProfile_Type()
)
tGlobalMplsLspExpProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tGlobalMplsLspExpProfile.setStatus("current")
_TMplsLspExpProfileTable_Object = MibTable
tMplsLspExpProfileTable = _TMplsLspExpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 4)
)
if mibBuilder.loadTexts:
    tMplsLspExpProfileTable.setStatus("current")
_TMplsLspExpProfileEntry_Object = MibTableRow
tMplsLspExpProfileEntry = _TMplsLspExpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 4, 1)
)
tMplsLspExpProfileEntry.setIndexNames(
    (0, "TIMETRA-SAS-QOS-MIB", "tMplsLspExpProfMapIndex"),
    (0, "TIMETRA-SAS-QOS-MIB", "tMplsLspExpProfileBits"),
)
if mibBuilder.loadTexts:
    tMplsLspExpProfileEntry.setStatus("current")


class _TMplsLspExpProfileBits_Type(TMplsLspExpProfileValue):
    """Custom type tMplsLspExpProfileBits based on TMplsLspExpProfileValue"""
    defaultValue = -1


_TMplsLspExpProfileBits_Type.__name__ = "TMplsLspExpProfileValue"
_TMplsLspExpProfileBits_Object = MibTableColumn
tMplsLspExpProfileBits = _TMplsLspExpProfileBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 4, 1, 1),
    _TMplsLspExpProfileBits_Type()
)
tMplsLspExpProfileBits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMplsLspExpProfileBits.setStatus("current")
_TMplsLspExpProfileRowStatus_Type = RowStatus
_TMplsLspExpProfileRowStatus_Object = MibTableColumn
tMplsLspExpProfileRowStatus = _TMplsLspExpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 4, 1, 2),
    _TMplsLspExpProfileRowStatus_Type()
)
tMplsLspExpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMplsLspExpProfileRowStatus.setStatus("current")


class _TMplsLspExpProfile_Type(TProfile):
    """Custom type tMplsLspExpProfile based on TProfile"""
    defaultValue = 2


_TMplsLspExpProfile_Type.__name__ = "TProfile"
_TMplsLspExpProfile_Object = MibTableColumn
tMplsLspExpProfile = _TMplsLspExpProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 4, 1, 3),
    _TMplsLspExpProfile_Type()
)
tMplsLspExpProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMplsLspExpProfile.setStatus("current")
_TMplsLspExpProfileLastChanged_Type = TimeStamp
_TMplsLspExpProfileLastChanged_Object = MibTableColumn
tMplsLspExpProfileLastChanged = _TMplsLspExpProfileLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 4, 1, 4),
    _TMplsLspExpProfileLastChanged_Type()
)
tMplsLspExpProfileLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMplsLspExpProfileLastChanged.setStatus("current")


class _TLdpLocalFcEnableAdminStatus_Type(TruthValue):
    """Custom type tLdpLocalFcEnableAdminStatus based on TruthValue"""
    defaultValue = 2


_TLdpLocalFcEnableAdminStatus_Type.__name__ = "TruthValue"
_TLdpLocalFcEnableAdminStatus_Object = MibScalar
tLdpLocalFcEnableAdminStatus = _TLdpLocalFcEnableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 5),
    _TLdpLocalFcEnableAdminStatus_Type()
)
tLdpLocalFcEnableAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLdpLocalFcEnableAdminStatus.setStatus("current")
_TLdpLocalFcEnableOperStatus_Type = TruthValue
_TLdpLocalFcEnableOperStatus_Object = MibScalar
tLdpLocalFcEnableOperStatus = _TLdpLocalFcEnableOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 10, 6),
    _TLdpLocalFcEnableOperStatus_Type()
)
tLdpLocalFcEnableOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLdpLocalFcEnableOperStatus.setStatus("current")
_TSASGeneralQosObjects_ObjectIdentity = ObjectIdentity
tSASGeneralQosObjects = _TSASGeneralQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21)
)
_TSASRemarkPolicyTable_Object = MibTable
tSASRemarkPolicyTable = _TSASRemarkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    tSASRemarkPolicyTable.setStatus("current")
_TSASRemarkPolicyEntry_Object = MibTableRow
tSASRemarkPolicyEntry = _TSASRemarkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 1, 1)
)
tSASRemarkPolicyEntry.setIndexNames(
    (0, "TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyId"),
)
if mibBuilder.loadTexts:
    tSASRemarkPolicyEntry.setStatus("current")
_TSASRemarkPolicyId_Type = TRemarkPolicyID
_TSASRemarkPolicyId_Object = MibTableColumn
tSASRemarkPolicyId = _TSASRemarkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 1, 1, 1),
    _TSASRemarkPolicyId_Type()
)
tSASRemarkPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSASRemarkPolicyId.setStatus("current")
_TSASRemarkPolicyRowStatus_Type = RowStatus
_TSASRemarkPolicyRowStatus_Object = MibTableColumn
tSASRemarkPolicyRowStatus = _TSASRemarkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 1, 1, 2),
    _TSASRemarkPolicyRowStatus_Type()
)
tSASRemarkPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASRemarkPolicyRowStatus.setStatus("current")


class _TSASRemarkPolicyDescription_Type(TItemDescription):
    """Custom type tSASRemarkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TSASRemarkPolicyDescription_Type.__name__ = "TItemDescription"
_TSASRemarkPolicyDescription_Object = MibTableColumn
tSASRemarkPolicyDescription = _TSASRemarkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 1, 1, 3),
    _TSASRemarkPolicyDescription_Type()
)
tSASRemarkPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASRemarkPolicyDescription.setStatus("current")


class _TSASRemarkPolicyType_Type(Integer32):
    """Custom type tSASRemarkPolicyType based on Integer32"""
    defaultValue = 5

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
        *(("dot1p", 1),
          ("dscp", 2),
          ("lsp-exp", 3),
          ("dot1p-dscp", 4),
          ("dot1p-lsp-exp-shared", 5))
    )


_TSASRemarkPolicyType_Type.__name__ = "Integer32"
_TSASRemarkPolicyType_Object = MibTableColumn
tSASRemarkPolicyType = _TSASRemarkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 1, 1, 4),
    _TSASRemarkPolicyType_Type()
)
tSASRemarkPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASRemarkPolicyType.setStatus("current")
_TSASRemarkPolicyLastChanged_Type = TimeStamp
_TSASRemarkPolicyLastChanged_Object = MibTableColumn
tSASRemarkPolicyLastChanged = _TSASRemarkPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 1, 1, 5),
    _TSASRemarkPolicyLastChanged_Type()
)
tSASRemarkPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSASRemarkPolicyLastChanged.setStatus("current")
_TSASRemarkPolicyFCTable_Object = MibTable
tSASRemarkPolicyFCTable = _TSASRemarkPolicyFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2)
)
if mibBuilder.loadTexts:
    tSASRemarkPolicyFCTable.setStatus("current")
_TSASRemarkPolicyFCEntry_Object = MibTableRow
tSASRemarkPolicyFCEntry = _TSASRemarkPolicyFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1)
)
tSASRemarkPolicyFCEntry.setIndexNames(
    (0, "TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyId"),
    (0, "TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyFCName"),
)
if mibBuilder.loadTexts:
    tSASRemarkPolicyFCEntry.setStatus("current")
_TSASRemarkPolicyFCName_Type = TFCName
_TSASRemarkPolicyFCName_Object = MibTableColumn
tSASRemarkPolicyFCName = _TSASRemarkPolicyFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 1),
    _TSASRemarkPolicyFCName_Type()
)
tSASRemarkPolicyFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSASRemarkPolicyFCName.setStatus("current")


class _TSASRemarkPolicyDot1PInProfile_Type(Dot1PPriority):
    """Custom type tSASRemarkPolicyDot1PInProfile based on Dot1PPriority"""
    defaultValue = -1


_TSASRemarkPolicyDot1PInProfile_Type.__name__ = "Dot1PPriority"
_TSASRemarkPolicyDot1PInProfile_Object = MibTableColumn
tSASRemarkPolicyDot1PInProfile = _TSASRemarkPolicyDot1PInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 2),
    _TSASRemarkPolicyDot1PInProfile_Type()
)
tSASRemarkPolicyDot1PInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyDot1PInProfile.setStatus("current")


class _TSASRemarkPolicyDot1POutProfile_Type(Dot1PPriority):
    """Custom type tSASRemarkPolicyDot1POutProfile based on Dot1PPriority"""
    defaultValue = -1


_TSASRemarkPolicyDot1POutProfile_Type.__name__ = "Dot1PPriority"
_TSASRemarkPolicyDot1POutProfile_Object = MibTableColumn
tSASRemarkPolicyDot1POutProfile = _TSASRemarkPolicyDot1POutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 3),
    _TSASRemarkPolicyDot1POutProfile_Type()
)
tSASRemarkPolicyDot1POutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyDot1POutProfile.setStatus("current")


class _TSASRemarkPolicyDSCPInProfile_Type(TDSCPNameOrEmpty):
    """Custom type tSASRemarkPolicyDSCPInProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TSASRemarkPolicyDSCPInProfile_Type.__name__ = "TDSCPNameOrEmpty"
_TSASRemarkPolicyDSCPInProfile_Object = MibTableColumn
tSASRemarkPolicyDSCPInProfile = _TSASRemarkPolicyDSCPInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 4),
    _TSASRemarkPolicyDSCPInProfile_Type()
)
tSASRemarkPolicyDSCPInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyDSCPInProfile.setStatus("current")


class _TSASRemarkPolicyDSCPOutProfile_Type(TDSCPNameOrEmpty):
    """Custom type tSASRemarkPolicyDSCPOutProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TSASRemarkPolicyDSCPOutProfile_Type.__name__ = "TDSCPNameOrEmpty"
_TSASRemarkPolicyDSCPOutProfile_Object = MibTableColumn
tSASRemarkPolicyDSCPOutProfile = _TSASRemarkPolicyDSCPOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 5),
    _TSASRemarkPolicyDSCPOutProfile_Type()
)
tSASRemarkPolicyDSCPOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyDSCPOutProfile.setStatus("current")


class _TSASRemarkPolicyLspExpInProfile_Type(TLspExpValue):
    """Custom type tSASRemarkPolicyLspExpInProfile based on TLspExpValue"""
    defaultValue = -1


_TSASRemarkPolicyLspExpInProfile_Type.__name__ = "TLspExpValue"
_TSASRemarkPolicyLspExpInProfile_Object = MibTableColumn
tSASRemarkPolicyLspExpInProfile = _TSASRemarkPolicyLspExpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 6),
    _TSASRemarkPolicyLspExpInProfile_Type()
)
tSASRemarkPolicyLspExpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyLspExpInProfile.setStatus("current")


class _TSASRemarkPolicyLspExpOutProfile_Type(TLspExpValue):
    """Custom type tSASRemarkPolicyLspExpOutProfile based on TLspExpValue"""
    defaultValue = -1


_TSASRemarkPolicyLspExpOutProfile_Type.__name__ = "TLspExpValue"
_TSASRemarkPolicyLspExpOutProfile_Object = MibTableColumn
tSASRemarkPolicyLspExpOutProfile = _TSASRemarkPolicyLspExpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 7),
    _TSASRemarkPolicyLspExpOutProfile_Type()
)
tSASRemarkPolicyLspExpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyLspExpOutProfile.setStatus("current")


class _TSASRemarkPolicyDot1PLspExpInProfile_Type(TDot1PLspExpValue):
    """Custom type tSASRemarkPolicyDot1PLspExpInProfile based on TDot1PLspExpValue"""
    defaultValue = -1


_TSASRemarkPolicyDot1PLspExpInProfile_Type.__name__ = "TDot1PLspExpValue"
_TSASRemarkPolicyDot1PLspExpInProfile_Object = MibTableColumn
tSASRemarkPolicyDot1PLspExpInProfile = _TSASRemarkPolicyDot1PLspExpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 8),
    _TSASRemarkPolicyDot1PLspExpInProfile_Type()
)
tSASRemarkPolicyDot1PLspExpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyDot1PLspExpInProfile.setStatus("current")


class _TSASRemarkPolicyDot1PLspExpOutProfile_Type(TDot1PLspExpValue):
    """Custom type tSASRemarkPolicyDot1PLspExpOutProfile based on TDot1PLspExpValue"""
    defaultValue = -1


_TSASRemarkPolicyDot1PLspExpOutProfile_Type.__name__ = "TDot1PLspExpValue"
_TSASRemarkPolicyDot1PLspExpOutProfile_Object = MibTableColumn
tSASRemarkPolicyDot1PLspExpOutProfile = _TSASRemarkPolicyDot1PLspExpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 9),
    _TSASRemarkPolicyDot1PLspExpOutProfile_Type()
)
tSASRemarkPolicyDot1PLspExpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyDot1PLspExpOutProfile.setStatus("current")


class _TSASRemarkPolicyDot1PProfile_Type(Dot1PPriority):
    """Custom type tSASRemarkPolicyDot1PProfile based on Dot1PPriority"""
    defaultValue = -1


_TSASRemarkPolicyDot1PProfile_Type.__name__ = "Dot1PPriority"
_TSASRemarkPolicyDot1PProfile_Object = MibTableColumn
tSASRemarkPolicyDot1PProfile = _TSASRemarkPolicyDot1PProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 10),
    _TSASRemarkPolicyDot1PProfile_Type()
)
tSASRemarkPolicyDot1PProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyDot1PProfile.setStatus("current")


class _TSASRemarkPolicyForceDEValue_Type(TDEValue):
    """Custom type tSASRemarkPolicyForceDEValue based on TDEValue"""
    defaultValue = -1


_TSASRemarkPolicyForceDEValue_Type.__name__ = "TDEValue"
_TSASRemarkPolicyForceDEValue_Object = MibTableColumn
tSASRemarkPolicyForceDEValue = _TSASRemarkPolicyForceDEValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 11),
    _TSASRemarkPolicyForceDEValue_Type()
)
tSASRemarkPolicyForceDEValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyForceDEValue.setStatus("current")


class _TSASRemarkPolicyFCDEMark_Type(TruthValue):
    """Custom type tSASRemarkPolicyFCDEMark based on TruthValue"""
    defaultValue = 2


_TSASRemarkPolicyFCDEMark_Type.__name__ = "TruthValue"
_TSASRemarkPolicyFCDEMark_Object = MibTableColumn
tSASRemarkPolicyFCDEMark = _TSASRemarkPolicyFCDEMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 1, 21, 2, 1, 12),
    _TSASRemarkPolicyFCDEMark_Type()
)
tSASRemarkPolicyFCDEMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSASRemarkPolicyFCDEMark.setStatus("current")
tSapIngressFCEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSasSapIngressFCEntry")
)
tSasSapIngressFCEntry.setIndexNames(*tSapIngressFCEntry.getIndexNames())
tSapIngressEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSapIngressExtnEntry")
)
tSapIngressExtnEntry.setIndexNames(*tSapIngressEntry.getIndexNames())
tSapIngressQueueEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSapIngressQueueExtnEntry")
)
tSapIngressQueueExtnEntry.setIndexNames(*tSapIngressQueueEntry.getIndexNames())
tSapIngressIPCriteriaEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSapIngressIPCriteriaExtnEntry")
)
tSapIngressIPCriteriaExtnEntry.setIndexNames(*tSapIngressIPCriteriaEntry.getIndexNames())
tSapIngressMacCriteriaEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSapIngressMacCriteriaExtnEntry")
)
tSapIngressMacCriteriaExtnEntry.setIndexNames(*tSapIngressMacCriteriaEntry.getIndexNames())
tSapIngressIPv6CriteriaEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSapIngressIPv6CriteriaExtnEntry")
)
tSapIngressIPv6CriteriaExtnEntry.setIndexNames(*tSapIngressIPv6CriteriaEntry.getIndexNames())
tSlopePolicyEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSasSlopePolicyExtnEntry")
)
tSasSlopePolicyExtnEntry.setIndexNames(*tSlopePolicyEntry.getIndexNames())
tPortSchedulerPlcyEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSasPortSchedulerPlcyEntry")
)
tSasPortSchedulerPlcyEntry.setIndexNames(*tPortSchedulerPlcyEntry.getIndexNames())
tNetworkPolicyEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tNetworkPolicyExtnEntry")
)
tNetworkPolicyExtnEntry.setIndexNames(*tNetworkPolicyEntry.getIndexNames())
tNetworkQueueEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tNetworkQueueExtnEntry")
)
tNetworkQueueExtnEntry.setIndexNames(*tNetworkQueueEntry.getIndexNames())
tNetworkEgressFCEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tNetworkEgressFCExtnEntry")
)
tNetworkEgressFCExtnEntry.setIndexNames(*tNetworkEgressFCEntry.getIndexNames())
tSapEgressEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSapEgressExtnEntry")
)
tSapEgressExtnEntry.setIndexNames(*tSapEgressEntry.getIndexNames())
tSapEgressQueueEntry.registerAugmentions(
    ("TIMETRA-SAS-QOS-MIB",
     "tSapEgressQueueExtnEntry")
)
tSapEgressQueueExtnEntry.setIndexNames(*tSapEgressQueueEntry.getIndexNames())

# Managed Objects groups

tmnxSASQoSV1v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 2, 1)
)
tmnxSASQoSV1v0Group.setObjects(
      *(("TIMETRA-SAS-QOS-MIB", "tAccessEgressRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressScope"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressDescription"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressRemark"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueuePIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueCIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueAdminPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueAdminCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueOperPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueOperCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCQueue"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCDot1PInProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCDot1POutProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterMCast"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterAdminCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterAdminMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterOperCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterOperMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterCIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterPIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterAdminPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterAdminCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterOperPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterOperCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterMode"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterRateMode"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnMCastMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterAdminCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterAdminMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterOperCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterOperMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterCIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterPIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterAdminPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterAdminCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterOperPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterOperCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterMode"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterMCast"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterRateMode"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue1DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue2DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue3DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue4DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue5DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue6DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue7DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue8DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue1DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue2DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue3DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue4DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue5DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue6DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue7DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue8DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiStartThreshold"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoStartThreshold"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyMode"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQuanta"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue1Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue2Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue3Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue4Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue5Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue6Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue7Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue8Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressFCMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressFCMCastMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressFCBCastMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressFCUnknownMeter"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterId"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedInProfPackets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedOutProfPackets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedInProfOctets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedOutProfOctets"),
        ("TIMETRA-SAS-QOS-MIB", "tQosIngressFrameBasedAccnt"),
        ("TIMETRA-SAS-QOS-MIB", "tQosEgressFrameBasedAccnt"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressNumQosClassifiers"))
)
if mibBuilder.loadTexts:
    tmnxSASQoSV1v0Group.setStatus("current")

tmnxSASMQoSV1v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 2, 2)
)
tmnxSASMQoSV1v0Group.setObjects(
      *(("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueHiAdminStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueHiStartAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueHiMaxAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueHiMaxProbability"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueLoAdminStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueLoStartAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueLoMaxAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueLoMaxProbability"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueNonTcpAdminStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueNonTcpStartAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueNonTcpMaxAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueNonTcpMaxProbability"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopePolicyQueueTimeAvgFactor"))
)
if mibBuilder.loadTexts:
    tmnxSASMQoSV1v0Group.setStatus("current")

tmnxSASQoSV2v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 2, 3)
)
tmnxSASQoSV2v0Group.setObjects(
      *(("TIMETRA-SAS-QOS-MIB", "tNetworkQueuePolicyName"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkPolicyRemarkPolicyId"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkPolicyType"),
        ("TIMETRA-SAS-QOS-MIB", "tSapEgressQueuePolicyName"),
        ("TIMETRA-SAS-QOS-MIB", "tSapEgressRemarkPolicyId"),
        ("TIMETRA-SAS-QOS-MIB", "tSapEgressRemark"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressRemarkPolicyId"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyDescription"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyType"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyDot1PInProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyDot1POutProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyDSCPInProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyDSCPOutProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyLspExpInProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyLspExpOutProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyDot1PLspExpInProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyDot1PLspExpOutProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSASRemarkPolicyLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyDescription"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyHiAdminStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyHiStartAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyHiMaxAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyHiMaxProbability"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyLoAdminStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyLoStartAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyLoMaxAverage"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyLoMaxProbability"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyTimeAvgFactor"),
        ("TIMETRA-SAS-QOS-MIB", "tQueueMgmtPolicyScope"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressScope"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressDescription"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressRemark"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueuePIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueCIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueAdminPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueAdminCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueOperPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueOperCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressQueueLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCQueue"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCDot1PInProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCDot1POutProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterMCast"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterAdminCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterAdminMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterOperCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterOperMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterCIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterPIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterAdminPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterAdminCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterOperPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterOperCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterMode"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterRateMode"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnMCastMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressFCExtnLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterAdminCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterAdminMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterOperCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterOperMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterCIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterPIRAdaptation"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterAdminPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterAdminCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterOperPIR"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterOperCIR"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterLastChanged"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterMode"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterMCast"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterRateMode"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue1DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue2DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue3DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue4DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue5DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue6DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue7DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiQueue8DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue1DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue2DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue3DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue4DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue5DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue6DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue7DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoQueue8DropRate"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeHiStartThreshold"),
        ("TIMETRA-SAS-QOS-MIB", "tSlopeLoStartThreshold"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyMode"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQuanta"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue1Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue2Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue3Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue4Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue5Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue6Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue7Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tPortSchedulerPlcyQueue8Weight"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressFCMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressFCMCastMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressFCBCastMeter"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressFCUnknownMeter"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterId"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedInProfPackets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedOutProfPackets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedInProfOctets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedOutProfOctets"),
        ("TIMETRA-SAS-QOS-MIB", "tQosIngressFrameBasedAccnt"),
        ("TIMETRA-SAS-QOS-MIB", "tQosEgressFrameBasedAccnt"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressNumQosClassifiers"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressQosClassifiersRequiredInVpls"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressQosClassifiersRequiredInEpipe"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressQosMetersRequiredInVpls"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressQosMetersRequiredInEpipe"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressIPCriteriaMatch"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMacCriteriaMatch"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressIPv6CriteriaEnable"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressIPv6CriteriaMatch"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkEgressRemarkType"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressIPMacMatch"))
)
if mibBuilder.loadTexts:
    tmnxSASQoSV2v0Group.setStatus("current")

tmnxSASQosObsolete7210V2v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 2, 4)
)
tmnxSASQosObsolete7210V2v0Group.setObjects(
      *(("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tNetworkIngressMeterMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterCBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMeterMBS"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressQosClassifiersUsed"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressQosMetersUsed"))
)
if mibBuilder.loadTexts:
    tmnxSASQosObsolete7210V2v0Group.setStatus("current")

tmnxSASQos7210V4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 2, 5)
)
tmnxSASQos7210V4v0Group.setObjects(
      *(("TIMETRA-SAS-QOS-MIB", "tGlobalMplsLspExpProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tLdpLocalFcEnableAdminStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tLdpLocalFcEnableOperStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tMplsLspExpProfMapRowStatus"),
        ("TIMETRA-SAS-QOS-MIB", "tMplsLspExpProfMapDescription"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressRemarkType"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCDscpInProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tAccessEgressFCDscpOutProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressQueuePolicyName"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressIPCriteriaActionProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressMacCriteriaActionProfile"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressIPv6CriteriaActionProfile"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedPackets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsForwardedOctets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsDroppedPackets"),
        ("TIMETRA-SAS-QOS-MIB", "sapIngQosMeterStatsDroppedOctets"))
)
if mibBuilder.loadTexts:
    tmnxSASQos7210V4v0Group.setStatus("current")

tmnxSASQoSV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 2, 6)
)
tmnxSASQoSV10v0Group.setObjects(
      *(("TIMETRA-SAS-QOS-MIB", "tSapIngressQosClassifiersRequiredInIes"),
        ("TIMETRA-SAS-QOS-MIB", "tSapIngressQosMetersRequiredInIes"))
)
if mibBuilder.loadTexts:
    tmnxSASQoSV10v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxSASQoSComp7210V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 1, 1)
)
tmnxSASQoSComp7210V1v0.setObjects(
    ("TIMETRA-SAS-QOS-MIB", "tmnxSASQoSV1v0Group")
)
if mibBuilder.loadTexts:
    tmnxSASQoSComp7210V1v0.setStatus(
        "current"
    )

tmnxSASQoSComp7210V2v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 1, 1, 2)
)
tmnxSASQoSComp7210V2v0.setObjects(
    ("TIMETRA-SAS-QOS-MIB", "tmnxSASQoSV2v0Group")
)
if mibBuilder.loadTexts:
    tmnxSASQoSComp7210V2v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-QOS-MIB",
    **{"TPolicyID": TPolicyID,
       "TSapIngressPolicyID": TSapIngressPolicyID,
       "TSapEgressPolicyID": TSapEgressPolicyID,
       "TAccessEgressPolicyID": TAccessEgressPolicyID,
       "TNetworkPolicyID": TNetworkPolicyID,
       "TRemarkPolicyID": TRemarkPolicyID,
       "TItemScope": TItemScope,
       "TItemMatch": TItemMatch,
       "TPriority": TPriority,
       "TPriorityOrDefault": TPriorityOrDefault,
       "TProfile": TProfile,
       "TProfileOrDei": TProfileOrDei,
       "TProfileOrNone": TProfileOrNone,
       "TAdaptationRule": TAdaptationRule,
       "TRemarkType": TRemarkType,
       "TPrecValue": TPrecValue,
       "TPrecValueOrNone": TPrecValueOrNone,
       "TIngressCIRRate": TIngressCIRRate,
       "TIngressPIRRate": TIngressPIRRate,
       "TCIRRate": TCIRRate,
       "TPIRRate": TPIRRate,
       "TPIRRateOrZero": TPIRRateOrZero,
       "TIngressBurstSize": TIngressBurstSize,
       "TBurstSize": TBurstSize,
       "TBurstPercent": TBurstPercent,
       "TBurstHundredthsOfPercent": TBurstHundredthsOfPercent,
       "TBurstPercentOrDefault": TBurstPercentOrDefault,
       "TRatePercent": TRatePercent,
       "TLevel": TLevel,
       "TLevelOrDefault": TLevelOrDefault,
       "TWeight": TWeight,
       "TQWeight": TQWeight,
       "TMeterMode": TMeterMode,
       "TPlcyMode": TPlcyMode,
       "TMeterRateMode": TMeterRateMode,
       "TPlcyQuanta": TPlcyQuanta,
       "TQueueMode": TQueueMode,
       "TEntryIndicator": TEntryIndicator,
       "TEntryId": TEntryId,
       "TMatchCriteria": TMatchCriteria,
       "TAtmTdpDescrType": TAtmTdpDescrType,
       "TSlopeDropRate": TSlopeDropRate,
       "TSlopeThreshold": TSlopeThreshold,
       "TMaxProbability": TMaxProbability,
       "TNetworkPolicyType": TNetworkPolicyType,
       "TDot1PLspExpValue": TDot1PLspExpValue,
       "TMplsLspExpProfileValue": TMplsLspExpProfileValue,
       "timetraSASQosMIBModule": timetraSASQosMIBModule,
       "tmnxSASQosConformance": tmnxSASQosConformance,
       "tmnxSASQosCompliances": tmnxSASQosCompliances,
       "tmnxSASQoSComp7210V1v0": tmnxSASQoSComp7210V1v0,
       "tmnxSASQoSComp7210V2v0": tmnxSASQoSComp7210V2v0,
       "tmnxSASQosGroups": tmnxSASQosGroups,
       "tmnxSASQoSV1v0Group": tmnxSASQoSV1v0Group,
       "tmnxSASMQoSV1v0Group": tmnxSASMQoSV1v0Group,
       "tmnxSASQoSV2v0Group": tmnxSASQoSV2v0Group,
       "tmnxSASQosObsolete7210V2v0Group": tmnxSASQosObsolete7210V2v0Group,
       "tmnxSASQos7210V4v0Group": tmnxSASQos7210V4v0Group,
       "tmnxSASQoSV10v0Group": tmnxSASQoSV10v0Group,
       "tSASQosObjects": tSASQosObjects,
       "tAccessEgressObjects": tAccessEgressObjects,
       "tAccessEgressTable": tAccessEgressTable,
       "tAccessEgressEntry": tAccessEgressEntry,
       "tAccessEgressIndex": tAccessEgressIndex,
       "tAccessEgressRowStatus": tAccessEgressRowStatus,
       "tAccessEgressScope": tAccessEgressScope,
       "tAccessEgressDescription": tAccessEgressDescription,
       "tAccessEgressLastChanged": tAccessEgressLastChanged,
       "tAccessEgressRemark": tAccessEgressRemark,
       "tAccessEgressRemarkPolicyId": tAccessEgressRemarkPolicyId,
       "tAccessEgressRemarkType": tAccessEgressRemarkType,
       "tAccessEgressQueueTable": tAccessEgressQueueTable,
       "tAccessEgressQueueEntry": tAccessEgressQueueEntry,
       "tAccessEgressQueueIndex": tAccessEgressQueueIndex,
       "tAccessEgressQueueRowStatus": tAccessEgressQueueRowStatus,
       "tAccessEgressQueueCBS": tAccessEgressQueueCBS,
       "tAccessEgressQueueMBS": tAccessEgressQueueMBS,
       "tAccessEgressQueuePIRAdaptation": tAccessEgressQueuePIRAdaptation,
       "tAccessEgressQueueCIRAdaptation": tAccessEgressQueueCIRAdaptation,
       "tAccessEgressQueueAdminPIR": tAccessEgressQueueAdminPIR,
       "tAccessEgressQueueAdminCIR": tAccessEgressQueueAdminCIR,
       "tAccessEgressQueueOperPIR": tAccessEgressQueueOperPIR,
       "tAccessEgressQueueOperCIR": tAccessEgressQueueOperCIR,
       "tAccessEgressQueueLastChanged": tAccessEgressQueueLastChanged,
       "tAccessEgressQueuePolicyName": tAccessEgressQueuePolicyName,
       "tAccessEgressQueuePolicyQueueMode": tAccessEgressQueuePolicyQueueMode,
       "tAccessEgressQueuePolicyWeight": tAccessEgressQueuePolicyWeight,
       "tAccessEgressFCTable": tAccessEgressFCTable,
       "tAccessEgressFCEntry": tAccessEgressFCEntry,
       "tAccessEgressFCName": tAccessEgressFCName,
       "tAccessEgressFCRowStatus": tAccessEgressFCRowStatus,
       "tAccessEgressFCQueue": tAccessEgressFCQueue,
       "tAccessEgressFCDot1PInProfile": tAccessEgressFCDot1PInProfile,
       "tAccessEgressFCDot1POutProfile": tAccessEgressFCDot1POutProfile,
       "tAccessEgressFCLastChanged": tAccessEgressFCLastChanged,
       "tAccessEgressFCDscpInProfile": tAccessEgressFCDscpInProfile,
       "tAccessEgressFCDscpOutProfile": tAccessEgressFCDscpOutProfile,
       "tAccessEgressFCDot1PProfile": tAccessEgressFCDot1PProfile,
       "tAccessEgressFCForceDEValue": tAccessEgressFCForceDEValue,
       "tAccessEgressFCDEMark": tAccessEgressFCDEMark,
       "tSASSapIngressObjects": tSASSapIngressObjects,
       "tSapIngressMeterTable": tSapIngressMeterTable,
       "tSapIngressMeterEntry": tSapIngressMeterEntry,
       "tSapIngressMeter": tSapIngressMeter,
       "tSapIngressMeterRowStatus": tSapIngressMeterRowStatus,
       "tSapIngressMeterMCast": tSapIngressMeterMCast,
       "tSapIngressMeterCBS": tSapIngressMeterCBS,
       "tSapIngressMeterMBS": tSapIngressMeterMBS,
       "tSapIngressMeterPIRAdaptation": tSapIngressMeterPIRAdaptation,
       "tSapIngressMeterCIRAdaptation": tSapIngressMeterCIRAdaptation,
       "tSapIngressMeterAdminPIR": tSapIngressMeterAdminPIR,
       "tSapIngressMeterAdminCIR": tSapIngressMeterAdminCIR,
       "tSapIngressMeterOperPIR": tSapIngressMeterOperPIR,
       "tSapIngressMeterOperCIR": tSapIngressMeterOperCIR,
       "tSapIngressMeterLastChanged": tSapIngressMeterLastChanged,
       "tSapIngressMeterMode": tSapIngressMeterMode,
       "tSapIngressMeterRateMode": tSapIngressMeterRateMode,
       "tSapIngressMeterAdminCBS": tSapIngressMeterAdminCBS,
       "tSapIngressMeterAdminMBS": tSapIngressMeterAdminMBS,
       "tSapIngressMeterOperCBS": tSapIngressMeterOperCBS,
       "tSapIngressMeterOperMBS": tSapIngressMeterOperMBS,
       "tSapIngressMeterProfileMode": tSapIngressMeterProfileMode,
       "tSapIngressMeterColorMode": tSapIngressMeterColorMode,
       "tSasSapIngressFCTable": tSasSapIngressFCTable,
       "tSasSapIngressFCEntry": tSasSapIngressFCEntry,
       "tSapIngressFCMeter": tSapIngressFCMeter,
       "tSapIngressFCMCastMeter": tSapIngressFCMCastMeter,
       "tSapIngressFCBCastMeter": tSapIngressFCBCastMeter,
       "tSapIngressFCUnknownMeter": tSapIngressFCUnknownMeter,
       "sapIngQosMeterStatsTable": sapIngQosMeterStatsTable,
       "sapIngQosMeterStatsEntry": sapIngQosMeterStatsEntry,
       "sapIngQosMeterId": sapIngQosMeterId,
       "sapIngQosMeterStatsForwardedInProfPackets": sapIngQosMeterStatsForwardedInProfPackets,
       "sapIngQosMeterStatsForwardedOutProfPackets": sapIngQosMeterStatsForwardedOutProfPackets,
       "sapIngQosMeterStatsForwardedInProfOctets": sapIngQosMeterStatsForwardedInProfOctets,
       "sapIngQosMeterStatsForwardedOutProfOctets": sapIngQosMeterStatsForwardedOutProfOctets,
       "sapIngQosMeterStatsForwardedPackets": sapIngQosMeterStatsForwardedPackets,
       "sapIngQosMeterStatsForwardedOctets": sapIngQosMeterStatsForwardedOctets,
       "sapIngQosMeterStatsDroppedPackets": sapIngQosMeterStatsDroppedPackets,
       "sapIngQosMeterStatsDroppedOctets": sapIngQosMeterStatsDroppedOctets,
       "tSapIngressExtnTable": tSapIngressExtnTable,
       "tSapIngressExtnEntry": tSapIngressExtnEntry,
       "tSapIngressNumQosClassifiers": tSapIngressNumQosClassifiers,
       "tSapIngressQosClassifiersUsed": tSapIngressQosClassifiersUsed,
       "tSapIngressQosMetersUsed": tSapIngressQosMetersUsed,
       "tSapIngressQosClassifiersRequiredInVpls": tSapIngressQosClassifiersRequiredInVpls,
       "tSapIngressQosClassifiersRequiredInEpipe": tSapIngressQosClassifiersRequiredInEpipe,
       "tSapIngressQosMetersRequiredInVpls": tSapIngressQosMetersRequiredInVpls,
       "tSapIngressQosMetersRequiredInEpipe": tSapIngressQosMetersRequiredInEpipe,
       "tSapIngressIPCriteriaMatch": tSapIngressIPCriteriaMatch,
       "tSapIngressMacCriteriaMatch": tSapIngressMacCriteriaMatch,
       "tSapIngressDefaultFCProfile": tSapIngressDefaultFCProfile,
       "tSapIngressIPv6CriteriaEnable": tSapIngressIPv6CriteriaEnable,
       "tSapIngressIPv6CriteriaMatch": tSapIngressIPv6CriteriaMatch,
       "tSapIngressIPMacMatch": tSapIngressIPMacMatch,
       "tSapIngressQosClassifiersRequiredInIes": tSapIngressQosClassifiersRequiredInIes,
       "tSapIngressQosMetersRequiredInIes": tSapIngressQosMetersRequiredInIes,
       "tSapIngressQueueExtnTable": tSapIngressQueueExtnTable,
       "tSapIngressQueueExtnEntry": tSapIngressQueueExtnEntry,
       "tSapIngressQueuePolicyName": tSapIngressQueuePolicyName,
       "tSapIngressIPCriteriaExtnTable": tSapIngressIPCriteriaExtnTable,
       "tSapIngressIPCriteriaExtnEntry": tSapIngressIPCriteriaExtnEntry,
       "tSapIngressIPCriteriaActionProfile": tSapIngressIPCriteriaActionProfile,
       "tSapIngressMacCriteriaExtnTable": tSapIngressMacCriteriaExtnTable,
       "tSapIngressMacCriteriaExtnEntry": tSapIngressMacCriteriaExtnEntry,
       "tSapIngressMacCriteriaActionProfile": tSapIngressMacCriteriaActionProfile,
       "tSapIngressIPv6CriteriaExtnTable": tSapIngressIPv6CriteriaExtnTable,
       "tSapIngressIPv6CriteriaExtnEntry": tSapIngressIPv6CriteriaExtnEntry,
       "tSapIngressIPv6CriteriaActionProfile": tSapIngressIPv6CriteriaActionProfile,
       "tSASNetworkIngressObjects": tSASNetworkIngressObjects,
       "tNetworkIngressFCExtnTable": tNetworkIngressFCExtnTable,
       "tNetworkIngressFCExtnEntry": tNetworkIngressFCExtnEntry,
       "tNetworkIngressFCExtnName": tNetworkIngressFCExtnName,
       "tNetworkIngressFCExtnRowStatus": tNetworkIngressFCExtnRowStatus,
       "tNetworkIngressFCExtnMeter": tNetworkIngressFCExtnMeter,
       "tNetworkIngressFCExtnMCastMeter": tNetworkIngressFCExtnMCastMeter,
       "tNetworkIngressFCExtnLastChanged": tNetworkIngressFCExtnLastChanged,
       "tNetworkIngressMeterTable": tNetworkIngressMeterTable,
       "tNetworkIngressMeterEntry": tNetworkIngressMeterEntry,
       "tNetworkIngressMeterIndex": tNetworkIngressMeterIndex,
       "tNetworkIngressMeterRowStatus": tNetworkIngressMeterRowStatus,
       "tNetworkIngressMeterCBS": tNetworkIngressMeterCBS,
       "tNetworkIngressMeterMBS": tNetworkIngressMeterMBS,
       "tNetworkIngressMeterCIRAdaptation": tNetworkIngressMeterCIRAdaptation,
       "tNetworkIngressMeterPIRAdaptation": tNetworkIngressMeterPIRAdaptation,
       "tNetworkIngressMeterAdminPIR": tNetworkIngressMeterAdminPIR,
       "tNetworkIngressMeterAdminCIR": tNetworkIngressMeterAdminCIR,
       "tNetworkIngressMeterOperPIR": tNetworkIngressMeterOperPIR,
       "tNetworkIngressMeterOperCIR": tNetworkIngressMeterOperCIR,
       "tNetworkIngressMeterLastChanged": tNetworkIngressMeterLastChanged,
       "tNetworkIngressMeterMode": tNetworkIngressMeterMode,
       "tNetworkIngressMeterMCast": tNetworkIngressMeterMCast,
       "tNetworkIngressMeterRateMode": tNetworkIngressMeterRateMode,
       "tNetworkIngressMeterAdminCBS": tNetworkIngressMeterAdminCBS,
       "tNetworkIngressMeterAdminMBS": tNetworkIngressMeterAdminMBS,
       "tNetworkIngressMeterOperCBS": tNetworkIngressMeterOperCBS,
       "tNetworkIngressMeterOperMBS": tNetworkIngressMeterOperMBS,
       "tSASSlopeObjects": tSASSlopeObjects,
       "tSasSlopePolicyExtnTable": tSasSlopePolicyExtnTable,
       "tSasSlopePolicyExtnEntry": tSasSlopePolicyExtnEntry,
       "tSlopeHiQueue1DropRate": tSlopeHiQueue1DropRate,
       "tSlopeHiQueue2DropRate": tSlopeHiQueue2DropRate,
       "tSlopeHiQueue3DropRate": tSlopeHiQueue3DropRate,
       "tSlopeHiQueue4DropRate": tSlopeHiQueue4DropRate,
       "tSlopeHiQueue5DropRate": tSlopeHiQueue5DropRate,
       "tSlopeHiQueue6DropRate": tSlopeHiQueue6DropRate,
       "tSlopeHiQueue7DropRate": tSlopeHiQueue7DropRate,
       "tSlopeHiQueue8DropRate": tSlopeHiQueue8DropRate,
       "tSlopeLoQueue1DropRate": tSlopeLoQueue1DropRate,
       "tSlopeLoQueue2DropRate": tSlopeLoQueue2DropRate,
       "tSlopeLoQueue3DropRate": tSlopeLoQueue3DropRate,
       "tSlopeLoQueue4DropRate": tSlopeLoQueue4DropRate,
       "tSlopeLoQueue5DropRate": tSlopeLoQueue5DropRate,
       "tSlopeLoQueue6DropRate": tSlopeLoQueue6DropRate,
       "tSlopeLoQueue7DropRate": tSlopeLoQueue7DropRate,
       "tSlopeLoQueue8DropRate": tSlopeLoQueue8DropRate,
       "tSlopeHiStartThreshold": tSlopeHiStartThreshold,
       "tSlopeLoStartThreshold": tSlopeLoStartThreshold,
       "tSlopePolicyQueueTable": tSlopePolicyQueueTable,
       "tSlopePolicyQueueEntry": tSlopePolicyQueueEntry,
       "tSlopePolicyQueueId": tSlopePolicyQueueId,
       "tSlopePolicyQueueRowStatus": tSlopePolicyQueueRowStatus,
       "tSlopePolicyQueueLastChanged": tSlopePolicyQueueLastChanged,
       "tSlopePolicyQueueHiAdminStatus": tSlopePolicyQueueHiAdminStatus,
       "tSlopePolicyQueueHiStartAverage": tSlopePolicyQueueHiStartAverage,
       "tSlopePolicyQueueHiMaxAverage": tSlopePolicyQueueHiMaxAverage,
       "tSlopePolicyQueueHiMaxProbability": tSlopePolicyQueueHiMaxProbability,
       "tSlopePolicyQueueLoAdminStatus": tSlopePolicyQueueLoAdminStatus,
       "tSlopePolicyQueueLoStartAverage": tSlopePolicyQueueLoStartAverage,
       "tSlopePolicyQueueLoMaxAverage": tSlopePolicyQueueLoMaxAverage,
       "tSlopePolicyQueueLoMaxProbability": tSlopePolicyQueueLoMaxProbability,
       "tSlopePolicyQueueNonTcpAdminStatus": tSlopePolicyQueueNonTcpAdminStatus,
       "tSlopePolicyQueueNonTcpStartAverage": tSlopePolicyQueueNonTcpStartAverage,
       "tSlopePolicyQueueNonTcpMaxAverage": tSlopePolicyQueueNonTcpMaxAverage,
       "tSlopePolicyQueueNonTcpMaxProbability": tSlopePolicyQueueNonTcpMaxProbability,
       "tSlopePolicyQueueTimeAvgFactor": tSlopePolicyQueueTimeAvgFactor,
       "tSasSchedulerObjects": tSasSchedulerObjects,
       "tSasPortSchedulerPlcyTable": tSasPortSchedulerPlcyTable,
       "tSasPortSchedulerPlcyEntry": tSasPortSchedulerPlcyEntry,
       "tPortSchedulerPlcyMode": tPortSchedulerPlcyMode,
       "tPortSchedulerPlcyQuanta": tPortSchedulerPlcyQuanta,
       "tPortSchedulerPlcyQueue1Weight": tPortSchedulerPlcyQueue1Weight,
       "tPortSchedulerPlcyQueue2Weight": tPortSchedulerPlcyQueue2Weight,
       "tPortSchedulerPlcyQueue3Weight": tPortSchedulerPlcyQueue3Weight,
       "tPortSchedulerPlcyQueue4Weight": tPortSchedulerPlcyQueue4Weight,
       "tPortSchedulerPlcyQueue5Weight": tPortSchedulerPlcyQueue5Weight,
       "tPortSchedulerPlcyQueue6Weight": tPortSchedulerPlcyQueue6Weight,
       "tPortSchedulerPlcyQueue7Weight": tPortSchedulerPlcyQueue7Weight,
       "tPortSchedulerPlcyQueue8Weight": tPortSchedulerPlcyQueue8Weight,
       "tQosFrameBasedAccntObjects": tQosFrameBasedAccntObjects,
       "tQosIngressFrameBasedAccnt": tQosIngressFrameBasedAccnt,
       "tQosEgressFrameBasedAccnt": tQosEgressFrameBasedAccnt,
       "tSASNetworkObjects": tSASNetworkObjects,
       "tNetworkPolicyExtnTable": tNetworkPolicyExtnTable,
       "tNetworkPolicyExtnEntry": tNetworkPolicyExtnEntry,
       "tNetworkPolicyType": tNetworkPolicyType,
       "tNetworkPolicyRemarkPolicyId": tNetworkPolicyRemarkPolicyId,
       "tNetworkIngressMeterColorMode": tNetworkIngressMeterColorMode,
       "tNetworkIngressMplsLspExpProfile": tNetworkIngressMplsLspExpProfile,
       "tNetworkEgressRemarkType": tNetworkEgressRemarkType,
       "tNetworkQueueExtnTable": tNetworkQueueExtnTable,
       "tNetworkQueueExtnEntry": tNetworkQueueExtnEntry,
       "tNetworkQueuePolicyName": tNetworkQueuePolicyName,
       "tNetworkQueuePolicyQueueMode": tNetworkQueuePolicyQueueMode,
       "tNetworkQueuePolicyWeight": tNetworkQueuePolicyWeight,
       "tNetworkEgressFCExtnTable": tNetworkEgressFCExtnTable,
       "tNetworkEgressFCExtnEntry": tNetworkEgressFCExtnEntry,
       "tNetworkEgressFCDot1pProfile": tNetworkEgressFCDot1pProfile,
       "tSASQueueMgmtObjects": tSASQueueMgmtObjects,
       "tQueueMgmtPolicyTable": tQueueMgmtPolicyTable,
       "tQueueMgmtPolicyEntry": tQueueMgmtPolicyEntry,
       "tQueueMgmtPolicyName": tQueueMgmtPolicyName,
       "tQueueMgmtPolicyRowStatus": tQueueMgmtPolicyRowStatus,
       "tQueueMgmtPolicyLastChanged": tQueueMgmtPolicyLastChanged,
       "tQueueMgmtPolicyDescription": tQueueMgmtPolicyDescription,
       "tQueueMgmtPolicyHiAdminStatus": tQueueMgmtPolicyHiAdminStatus,
       "tQueueMgmtPolicyHiStartAverage": tQueueMgmtPolicyHiStartAverage,
       "tQueueMgmtPolicyHiMaxAverage": tQueueMgmtPolicyHiMaxAverage,
       "tQueueMgmtPolicyHiMaxProbability": tQueueMgmtPolicyHiMaxProbability,
       "tQueueMgmtPolicyLoAdminStatus": tQueueMgmtPolicyLoAdminStatus,
       "tQueueMgmtPolicyLoStartAverage": tQueueMgmtPolicyLoStartAverage,
       "tQueueMgmtPolicyLoMaxAverage": tQueueMgmtPolicyLoMaxAverage,
       "tQueueMgmtPolicyLoMaxProbability": tQueueMgmtPolicyLoMaxProbability,
       "tQueueMgmtPolicyCBS": tQueueMgmtPolicyCBS,
       "tQueueMgmtPolicyMBS": tQueueMgmtPolicyMBS,
       "tQueueMgmtPolicyTimeAvgFactor": tQueueMgmtPolicyTimeAvgFactor,
       "tQueueMgmtPolicyScope": tQueueMgmtPolicyScope,
       "tSASSapEgressObjects": tSASSapEgressObjects,
       "tSapEgressExtnTable": tSapEgressExtnTable,
       "tSapEgressExtnEntry": tSapEgressExtnEntry,
       "tSapEgressRemark": tSapEgressRemark,
       "tSapEgressRemarkPolicyId": tSapEgressRemarkPolicyId,
       "tSapEgressQueueExtnTable": tSapEgressQueueExtnTable,
       "tSapEgressQueueExtnEntry": tSapEgressQueueExtnEntry,
       "tSapEgressQueuePolicyName": tSapEgressQueuePolicyName,
       "tSapEgressQueuePolicyQueueMode": tSapEgressQueuePolicyQueueMode,
       "tSapEgressQueuePolicyWeight": tSapEgressQueuePolicyWeight,
       "tMplsQosObjects": tMplsQosObjects,
       "tMplsLspExpProfMapTable": tMplsLspExpProfMapTable,
       "tMplsLspExpProfMapEntry": tMplsLspExpProfMapEntry,
       "tMplsLspExpProfMapIndex": tMplsLspExpProfMapIndex,
       "tMplsLspExpProfMapRowStatus": tMplsLspExpProfMapRowStatus,
       "tMplsLspExpProfMapDescription": tMplsLspExpProfMapDescription,
       "tMplsLspExpProfMapLastChanged": tMplsLspExpProfMapLastChanged,
       "tGlobalMplsLspExpProfile": tGlobalMplsLspExpProfile,
       "tMplsLspExpProfileTable": tMplsLspExpProfileTable,
       "tMplsLspExpProfileEntry": tMplsLspExpProfileEntry,
       "tMplsLspExpProfileBits": tMplsLspExpProfileBits,
       "tMplsLspExpProfileRowStatus": tMplsLspExpProfileRowStatus,
       "tMplsLspExpProfile": tMplsLspExpProfile,
       "tMplsLspExpProfileLastChanged": tMplsLspExpProfileLastChanged,
       "tLdpLocalFcEnableAdminStatus": tLdpLocalFcEnableAdminStatus,
       "tLdpLocalFcEnableOperStatus": tLdpLocalFcEnableOperStatus,
       "tSASGeneralQosObjects": tSASGeneralQosObjects,
       "tSASRemarkPolicyTable": tSASRemarkPolicyTable,
       "tSASRemarkPolicyEntry": tSASRemarkPolicyEntry,
       "tSASRemarkPolicyId": tSASRemarkPolicyId,
       "tSASRemarkPolicyRowStatus": tSASRemarkPolicyRowStatus,
       "tSASRemarkPolicyDescription": tSASRemarkPolicyDescription,
       "tSASRemarkPolicyType": tSASRemarkPolicyType,
       "tSASRemarkPolicyLastChanged": tSASRemarkPolicyLastChanged,
       "tSASRemarkPolicyFCTable": tSASRemarkPolicyFCTable,
       "tSASRemarkPolicyFCEntry": tSASRemarkPolicyFCEntry,
       "tSASRemarkPolicyFCName": tSASRemarkPolicyFCName,
       "tSASRemarkPolicyDot1PInProfile": tSASRemarkPolicyDot1PInProfile,
       "tSASRemarkPolicyDot1POutProfile": tSASRemarkPolicyDot1POutProfile,
       "tSASRemarkPolicyDSCPInProfile": tSASRemarkPolicyDSCPInProfile,
       "tSASRemarkPolicyDSCPOutProfile": tSASRemarkPolicyDSCPOutProfile,
       "tSASRemarkPolicyLspExpInProfile": tSASRemarkPolicyLspExpInProfile,
       "tSASRemarkPolicyLspExpOutProfile": tSASRemarkPolicyLspExpOutProfile,
       "tSASRemarkPolicyDot1PLspExpInProfile": tSASRemarkPolicyDot1PLspExpInProfile,
       "tSASRemarkPolicyDot1PLspExpOutProfile": tSASRemarkPolicyDot1PLspExpOutProfile,
       "tSASRemarkPolicyDot1PProfile": tSASRemarkPolicyDot1PProfile,
       "tSASRemarkPolicyForceDEValue": tSASRemarkPolicyForceDEValue,
       "tSASRemarkPolicyFCDEMark": tSASRemarkPolicyFCDEMark}
)
