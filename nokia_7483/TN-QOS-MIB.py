# SNMP MIB module (TN-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-QOS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:44 2025
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

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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

(Dot1PPriority,
 IpAddressPrefixLength,
 ServiceAccessPoint,
 TAdaptationRule,
 TBurstHundredthsOfPercent,
 TBurstPercentOrDefault,
 TDEProfile,
 TDEValue,
 TDSCPNameOrEmpty,
 TEgressQueueId,
 TEntryId,
 TFCName,
 TFrameType,
 TIngressHsmdaCounterIdOrZero,
 TIngressHsmdaPerPacketOffset,
 TIngressHsmdaQueueId,
 TIngressQueueId,
 TIpProtocol,
 TItemDescription,
 TItemMatch,
 TItemScope,
 TLNamedItemOrEmpty,
 TLevel,
 TLevelOrDefault,
 TLspExpValue,
 TMacFilterType,
 TMatchCriteria,
 TNamedItem,
 TNamedItemOrEmpty,
 TNetworkPolicyID,
 TPIRRatePercent,
 TPortSchedulerCIR,
 TPortSchedulerPIR,
 TPrecValueOrNone,
 TPriority,
 TPriorityOrDefault,
 TProfile,
 TProfileOrNone,
 TQueueId,
 TRatePercent,
 TRemarkType,
 TSapIngressPolicyID,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TWeight) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "ServiceAccessPoint",
    "TAdaptationRule",
    "TBurstHundredthsOfPercent",
    "TBurstPercentOrDefault",
    "TDEProfile",
    "TDEValue",
    "TDSCPNameOrEmpty",
    "TEgressQueueId",
    "TEntryId",
    "TFCName",
    "TFrameType",
    "TIngressHsmdaCounterIdOrZero",
    "TIngressHsmdaPerPacketOffset",
    "TIngressHsmdaQueueId",
    "TIngressQueueId",
    "TIpProtocol",
    "TItemDescription",
    "TItemMatch",
    "TItemScope",
    "TLNamedItemOrEmpty",
    "TLevel",
    "TLevelOrDefault",
    "TLspExpValue",
    "TMacFilterType",
    "TMatchCriteria",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TNetworkPolicyID",
    "TPIRRatePercent",
    "TPortSchedulerCIR",
    "TPortSchedulerPIR",
    "TPrecValueOrNone",
    "TPriority",
    "TPriorityOrDefault",
    "TProfile",
    "TProfileOrNone",
    "TQueueId",
    "TRatePercent",
    "TRemarkType",
    "TSapIngressPolicyID",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TWeight")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnQosMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 16)
)
if mibBuilder.loadTexts:
    tnQosMIBModule.setRevisions(
        ("1913-08-22 00:00",
         "1912-12-05 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-02-28 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-05-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMcFrClassIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



# MIB Managed Objects in the order of their OIDs

_TnQosObjects_ObjectIdentity = ObjectIdentity
tnQosObjects = _TnQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16)
)
_TnSapIngressObjects_ObjectIdentity = ObjectIdentity
tnSapIngressObjects = _TnSapIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3)
)
_TnSapIngressTable_Object = MibTable
tnSapIngressTable = _TnSapIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    tnSapIngressTable.setStatus("current")
_TnSapIngressEntry_Object = MibTableRow
tnSapIngressEntry = _TnSapIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1)
)
tnSapIngressEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnSapIngressIndex"),
)
if mibBuilder.loadTexts:
    tnSapIngressEntry.setStatus("current")


class _TnSapIngressIndex_Type(TSapIngressPolicyID):
    """Custom type tnSapIngressIndex based on TSapIngressPolicyID"""
    subtypeSpec = TSapIngressPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSapIngressIndex_Type.__name__ = "TSapIngressPolicyID"
_TnSapIngressIndex_Object = MibTableColumn
tnSapIngressIndex = _TnSapIngressIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 1),
    _TnSapIngressIndex_Type()
)
tnSapIngressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIngressIndex.setStatus("current")
_TnSapIngressRowStatus_Type = RowStatus
_TnSapIngressRowStatus_Object = MibTableColumn
tnSapIngressRowStatus = _TnSapIngressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 2),
    _TnSapIngressRowStatus_Type()
)
tnSapIngressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressRowStatus.setStatus("current")


class _TnSapIngressScope_Type(TItemScope):
    """Custom type tnSapIngressScope based on TItemScope"""
    defaultValue = 2


_TnSapIngressScope_Type.__name__ = "TItemScope"
_TnSapIngressScope_Object = MibTableColumn
tnSapIngressScope = _TnSapIngressScope_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 3),
    _TnSapIngressScope_Type()
)
tnSapIngressScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressScope.setStatus("current")


class _TnSapIngressDescription_Type(TItemDescription):
    """Custom type tnSapIngressDescription based on TItemDescription"""
    defaultHexValue = ""


_TnSapIngressDescription_Type.__name__ = "TItemDescription"
_TnSapIngressDescription_Object = MibTableColumn
tnSapIngressDescription = _TnSapIngressDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 4),
    _TnSapIngressDescription_Type()
)
tnSapIngressDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressDescription.setStatus("current")


class _TnSapIngressDefaultFC_Type(TNamedItem):
    """Custom type tnSapIngressDefaultFC based on TNamedItem"""
    defaultHexValue = "be"


_TnSapIngressDefaultFC_Type.__name__ = "TNamedItem"
_TnSapIngressDefaultFC_Object = MibTableColumn
tnSapIngressDefaultFC = _TnSapIngressDefaultFC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 5),
    _TnSapIngressDefaultFC_Type()
)
tnSapIngressDefaultFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressDefaultFC.setStatus("current")


class _TnSapIngressDefaultFCPriority_Type(TPriority):
    """Custom type tnSapIngressDefaultFCPriority based on TPriority"""
    defaultValue = 1


_TnSapIngressDefaultFCPriority_Type.__name__ = "TPriority"
_TnSapIngressDefaultFCPriority_Object = MibTableColumn
tnSapIngressDefaultFCPriority = _TnSapIngressDefaultFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 6),
    _TnSapIngressDefaultFCPriority_Type()
)
tnSapIngressDefaultFCPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressDefaultFCPriority.setStatus("current")
_TnSapIngressMatchCriteria_Type = TMatchCriteria
_TnSapIngressMatchCriteria_Object = MibTableColumn
tnSapIngressMatchCriteria = _TnSapIngressMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 7),
    _TnSapIngressMatchCriteria_Type()
)
tnSapIngressMatchCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressMatchCriteria.setStatus("current")
_TnSapIngressLastChanged_Type = TimeStamp
_TnSapIngressLastChanged_Object = MibTableColumn
tnSapIngressLastChanged = _TnSapIngressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 8),
    _TnSapIngressLastChanged_Type()
)
tnSapIngressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressLastChanged.setStatus("current")


class _TnSapIngressHsmdaPacketOffset_Type(TIngressHsmdaPerPacketOffset):
    """Custom type tnSapIngressHsmdaPacketOffset based on TIngressHsmdaPerPacketOffset"""
    defaultValue = 0


_TnSapIngressHsmdaPacketOffset_Type.__name__ = "TIngressHsmdaPerPacketOffset"
_TnSapIngressHsmdaPacketOffset_Object = MibTableColumn
tnSapIngressHsmdaPacketOffset = _TnSapIngressHsmdaPacketOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 9),
    _TnSapIngressHsmdaPacketOffset_Type()
)
tnSapIngressHsmdaPacketOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressHsmdaPacketOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIngressHsmdaPacketOffset.setUnits("bytes")


class _TnSapIngressDefFCHsmdaCntrOvr_Type(TIngressHsmdaCounterIdOrZero):
    """Custom type tnSapIngressDefFCHsmdaCntrOvr based on TIngressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TnSapIngressDefFCHsmdaCntrOvr_Type.__name__ = "TIngressHsmdaCounterIdOrZero"
_TnSapIngressDefFCHsmdaCntrOvr_Object = MibTableColumn
tnSapIngressDefFCHsmdaCntrOvr = _TnSapIngressDefFCHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 10),
    _TnSapIngressDefFCHsmdaCntrOvr_Type()
)
tnSapIngressDefFCHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressDefFCHsmdaCntrOvr.setStatus("current")


class _TnSapIngressMacCritType_Type(TMacFilterType):
    """Custom type tnSapIngressMacCritType based on TMacFilterType"""
    defaultValue = 1


_TnSapIngressMacCritType_Type.__name__ = "TMacFilterType"
_TnSapIngressMacCritType_Object = MibTableColumn
tnSapIngressMacCritType = _TnSapIngressMacCritType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 11),
    _TnSapIngressMacCritType_Type()
)
tnSapIngressMacCritType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCritType.setStatus("current")


class _TnSapIngressPolicyName_Type(TLNamedItemOrEmpty):
    """Custom type tnSapIngressPolicyName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressPolicyName_Type.__name__ = "TLNamedItemOrEmpty"
_TnSapIngressPolicyName_Object = MibTableColumn
tnSapIngressPolicyName = _TnSapIngressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 1, 1, 12),
    _TnSapIngressPolicyName_Type()
)
tnSapIngressPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressPolicyName.setStatus("current")
_TnSapIngressIPCriteriaTable_Object = MibTable
tnSapIngressIPCriteriaTable = _TnSapIngressIPCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5)
)
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaTable.setStatus("current")
_TnSapIngressIPCriteriaEntry_Object = MibTableRow
tnSapIngressIPCriteriaEntry = _TnSapIngressIPCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1)
)
tnSapIngressIPCriteriaEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnSapIngressIndex"),
    (0, "TN-QOS-MIB", "tnSapIngressIPCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaEntry.setStatus("current")
_TnSapIngressIPCriteriaIndex_Type = TEntryId
_TnSapIngressIPCriteriaIndex_Object = MibTableColumn
tnSapIngressIPCriteriaIndex = _TnSapIngressIPCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 1),
    _TnSapIngressIPCriteriaIndex_Type()
)
tnSapIngressIPCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaIndex.setStatus("current")
_TnSapIngressIPCriteriaRowStatus_Type = RowStatus
_TnSapIngressIPCriteriaRowStatus_Object = MibTableColumn
tnSapIngressIPCriteriaRowStatus = _TnSapIngressIPCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 2),
    _TnSapIngressIPCriteriaRowStatus_Type()
)
tnSapIngressIPCriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaRowStatus.setStatus("current")


class _TnSapIngressIPCriteriaDescription_Type(TItemDescription):
    """Custom type tnSapIngressIPCriteriaDescription based on TItemDescription"""
    defaultHexValue = ""


_TnSapIngressIPCriteriaDescription_Type.__name__ = "TItemDescription"
_TnSapIngressIPCriteriaDescription_Object = MibTableColumn
tnSapIngressIPCriteriaDescription = _TnSapIngressIPCriteriaDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 3),
    _TnSapIngressIPCriteriaDescription_Type()
)
tnSapIngressIPCriteriaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaDescription.setStatus("current")


class _TnSapIngressIPCriteriaActionFC_Type(TNamedItemOrEmpty):
    """Custom type tnSapIngressIPCriteriaActionFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressIPCriteriaActionFC_Type.__name__ = "TNamedItemOrEmpty"
_TnSapIngressIPCriteriaActionFC_Object = MibTableColumn
tnSapIngressIPCriteriaActionFC = _TnSapIngressIPCriteriaActionFC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 4),
    _TnSapIngressIPCriteriaActionFC_Type()
)
tnSapIngressIPCriteriaActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaActionFC.setStatus("current")


class _TnSapIngressIPCriteriaActionPriority_Type(TPriorityOrDefault):
    """Custom type tnSapIngressIPCriteriaActionPriority based on TPriorityOrDefault"""
    defaultValue = 3


_TnSapIngressIPCriteriaActionPriority_Type.__name__ = "TPriorityOrDefault"
_TnSapIngressIPCriteriaActionPriority_Object = MibTableColumn
tnSapIngressIPCriteriaActionPriority = _TnSapIngressIPCriteriaActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 5),
    _TnSapIngressIPCriteriaActionPriority_Type()
)
tnSapIngressIPCriteriaActionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaActionPriority.setStatus("current")


class _TnSapIngressIPCriteriaSourceIpAddr_Type(IpAddress):
    """Custom type tnSapIngressIPCriteriaSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TnSapIngressIPCriteriaSourceIpAddr_Type.__name__ = "IpAddress"
_TnSapIngressIPCriteriaSourceIpAddr_Object = MibTableColumn
tnSapIngressIPCriteriaSourceIpAddr = _TnSapIngressIPCriteriaSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 6),
    _TnSapIngressIPCriteriaSourceIpAddr_Type()
)
tnSapIngressIPCriteriaSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaSourceIpAddr.setStatus("current")


class _TnSapIngressIPCriteriaSourceIpMask_Type(IpAddressPrefixLength):
    """Custom type tnSapIngressIPCriteriaSourceIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TnSapIngressIPCriteriaSourceIpMask_Type.__name__ = "IpAddressPrefixLength"
_TnSapIngressIPCriteriaSourceIpMask_Object = MibTableColumn
tnSapIngressIPCriteriaSourceIpMask = _TnSapIngressIPCriteriaSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 7),
    _TnSapIngressIPCriteriaSourceIpMask_Type()
)
tnSapIngressIPCriteriaSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaSourceIpMask.setStatus("current")


class _TnSapIngressIPCriteriaDestIpAddr_Type(IpAddress):
    """Custom type tnSapIngressIPCriteriaDestIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TnSapIngressIPCriteriaDestIpAddr_Type.__name__ = "IpAddress"
_TnSapIngressIPCriteriaDestIpAddr_Object = MibTableColumn
tnSapIngressIPCriteriaDestIpAddr = _TnSapIngressIPCriteriaDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 8),
    _TnSapIngressIPCriteriaDestIpAddr_Type()
)
tnSapIngressIPCriteriaDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaDestIpAddr.setStatus("current")


class _TnSapIngressIPCriteriaDestIpMask_Type(IpAddressPrefixLength):
    """Custom type tnSapIngressIPCriteriaDestIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TnSapIngressIPCriteriaDestIpMask_Type.__name__ = "IpAddressPrefixLength"
_TnSapIngressIPCriteriaDestIpMask_Object = MibTableColumn
tnSapIngressIPCriteriaDestIpMask = _TnSapIngressIPCriteriaDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 9),
    _TnSapIngressIPCriteriaDestIpMask_Type()
)
tnSapIngressIPCriteriaDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaDestIpMask.setStatus("current")


class _TnSapIngressIPCriteriaProtocol_Type(TIpProtocol):
    """Custom type tnSapIngressIPCriteriaProtocol based on TIpProtocol"""
    defaultValue = -1


_TnSapIngressIPCriteriaProtocol_Type.__name__ = "TIpProtocol"
_TnSapIngressIPCriteriaProtocol_Object = MibTableColumn
tnSapIngressIPCriteriaProtocol = _TnSapIngressIPCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 10),
    _TnSapIngressIPCriteriaProtocol_Type()
)
tnSapIngressIPCriteriaProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaProtocol.setStatus("current")


class _TnSapIngressIPCriteriaSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tnSapIngressIPCriteriaSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TnSapIngressIPCriteriaSourcePortValue1_Type.__name__ = "TTcpUdpPort"
_TnSapIngressIPCriteriaSourcePortValue1_Object = MibTableColumn
tnSapIngressIPCriteriaSourcePortValue1 = _TnSapIngressIPCriteriaSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 11),
    _TnSapIngressIPCriteriaSourcePortValue1_Type()
)
tnSapIngressIPCriteriaSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaSourcePortValue1.setStatus("current")


class _TnSapIngressIPCriteriaSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tnSapIngressIPCriteriaSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TnSapIngressIPCriteriaSourcePortValue2_Type.__name__ = "TTcpUdpPort"
_TnSapIngressIPCriteriaSourcePortValue2_Object = MibTableColumn
tnSapIngressIPCriteriaSourcePortValue2 = _TnSapIngressIPCriteriaSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 12),
    _TnSapIngressIPCriteriaSourcePortValue2_Type()
)
tnSapIngressIPCriteriaSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaSourcePortValue2.setStatus("current")


class _TnSapIngressIPCriteriaSourcePortOperator_Type(TTcpUdpPortOperator):
    """Custom type tnSapIngressIPCriteriaSourcePortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_TnSapIngressIPCriteriaSourcePortOperator_Type.__name__ = "TTcpUdpPortOperator"
_TnSapIngressIPCriteriaSourcePortOperator_Object = MibTableColumn
tnSapIngressIPCriteriaSourcePortOperator = _TnSapIngressIPCriteriaSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 13),
    _TnSapIngressIPCriteriaSourcePortOperator_Type()
)
tnSapIngressIPCriteriaSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaSourcePortOperator.setStatus("current")


class _TnSapIngressIPCriteriaDestPortValue1_Type(TTcpUdpPort):
    """Custom type tnSapIngressIPCriteriaDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TnSapIngressIPCriteriaDestPortValue1_Type.__name__ = "TTcpUdpPort"
_TnSapIngressIPCriteriaDestPortValue1_Object = MibTableColumn
tnSapIngressIPCriteriaDestPortValue1 = _TnSapIngressIPCriteriaDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 14),
    _TnSapIngressIPCriteriaDestPortValue1_Type()
)
tnSapIngressIPCriteriaDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaDestPortValue1.setStatus("current")


class _TnSapIngressIPCriteriaDestPortValue2_Type(TTcpUdpPort):
    """Custom type tnSapIngressIPCriteriaDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TnSapIngressIPCriteriaDestPortValue2_Type.__name__ = "TTcpUdpPort"
_TnSapIngressIPCriteriaDestPortValue2_Object = MibTableColumn
tnSapIngressIPCriteriaDestPortValue2 = _TnSapIngressIPCriteriaDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 15),
    _TnSapIngressIPCriteriaDestPortValue2_Type()
)
tnSapIngressIPCriteriaDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaDestPortValue2.setStatus("current")


class _TnSapIngressIPCriteriaDestPortOperator_Type(TTcpUdpPortOperator):
    """Custom type tnSapIngressIPCriteriaDestPortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_TnSapIngressIPCriteriaDestPortOperator_Type.__name__ = "TTcpUdpPortOperator"
_TnSapIngressIPCriteriaDestPortOperator_Object = MibTableColumn
tnSapIngressIPCriteriaDestPortOperator = _TnSapIngressIPCriteriaDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 16),
    _TnSapIngressIPCriteriaDestPortOperator_Type()
)
tnSapIngressIPCriteriaDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaDestPortOperator.setStatus("current")


class _TnSapIngressIPCriteriaDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tnSapIngressIPCriteriaDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TnSapIngressIPCriteriaDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TnSapIngressIPCriteriaDSCP_Object = MibTableColumn
tnSapIngressIPCriteriaDSCP = _TnSapIngressIPCriteriaDSCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 17),
    _TnSapIngressIPCriteriaDSCP_Type()
)
tnSapIngressIPCriteriaDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaDSCP.setStatus("current")


class _TnSapIngressIPCriteriaFragment_Type(TItemMatch):
    """Custom type tnSapIngressIPCriteriaFragment based on TItemMatch"""
    defaultValue = 1


_TnSapIngressIPCriteriaFragment_Type.__name__ = "TItemMatch"
_TnSapIngressIPCriteriaFragment_Object = MibTableColumn
tnSapIngressIPCriteriaFragment = _TnSapIngressIPCriteriaFragment_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 19),
    _TnSapIngressIPCriteriaFragment_Type()
)
tnSapIngressIPCriteriaFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaFragment.setStatus("current")
_TnSapIngressIPCriteriaLastChanged_Type = TimeStamp
_TnSapIngressIPCriteriaLastChanged_Object = MibTableColumn
tnSapIngressIPCriteriaLastChanged = _TnSapIngressIPCriteriaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 20),
    _TnSapIngressIPCriteriaLastChanged_Type()
)
tnSapIngressIPCriteriaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaLastChanged.setStatus("current")


class _TnSapIngressIPCritHsmdaCntrOvr_Type(TIngressHsmdaCounterIdOrZero):
    """Custom type tnSapIngressIPCritHsmdaCntrOvr based on TIngressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TnSapIngressIPCritHsmdaCntrOvr_Type.__name__ = "TIngressHsmdaCounterIdOrZero"
_TnSapIngressIPCritHsmdaCntrOvr_Object = MibTableColumn
tnSapIngressIPCritHsmdaCntrOvr = _TnSapIngressIPCritHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 5, 1, 21),
    _TnSapIngressIPCritHsmdaCntrOvr_Type()
)
tnSapIngressIPCritHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCritHsmdaCntrOvr.setStatus("current")
_TnSapIngressMacCriteriaTable_Object = MibTable
tnSapIngressMacCriteriaTable = _TnSapIngressMacCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6)
)
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaTable.setStatus("current")
_TnSapIngressMacCriteriaEntry_Object = MibTableRow
tnSapIngressMacCriteriaEntry = _TnSapIngressMacCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1)
)
tnSapIngressMacCriteriaEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnSapIngressIndex"),
    (0, "TN-QOS-MIB", "tnSapIngressMacCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaEntry.setStatus("current")
_TnSapIngressMacCriteriaIndex_Type = TEntryId
_TnSapIngressMacCriteriaIndex_Object = MibTableColumn
tnSapIngressMacCriteriaIndex = _TnSapIngressMacCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 1),
    _TnSapIngressMacCriteriaIndex_Type()
)
tnSapIngressMacCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaIndex.setStatus("current")
_TnSapIngressMacCriteriaRowStatus_Type = RowStatus
_TnSapIngressMacCriteriaRowStatus_Object = MibTableColumn
tnSapIngressMacCriteriaRowStatus = _TnSapIngressMacCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 2),
    _TnSapIngressMacCriteriaRowStatus_Type()
)
tnSapIngressMacCriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaRowStatus.setStatus("current")


class _TnSapIngressMacCriteriaDescription_Type(TItemDescription):
    """Custom type tnSapIngressMacCriteriaDescription based on TItemDescription"""
    defaultHexValue = ""


_TnSapIngressMacCriteriaDescription_Type.__name__ = "TItemDescription"
_TnSapIngressMacCriteriaDescription_Object = MibTableColumn
tnSapIngressMacCriteriaDescription = _TnSapIngressMacCriteriaDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 3),
    _TnSapIngressMacCriteriaDescription_Type()
)
tnSapIngressMacCriteriaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaDescription.setStatus("current")
_TnSapIngressMacCriteriaActionFC_Type = TNamedItemOrEmpty
_TnSapIngressMacCriteriaActionFC_Object = MibTableColumn
tnSapIngressMacCriteriaActionFC = _TnSapIngressMacCriteriaActionFC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 4),
    _TnSapIngressMacCriteriaActionFC_Type()
)
tnSapIngressMacCriteriaActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaActionFC.setStatus("current")


class _TnSapIngressMacCriteriaActionPriority_Type(TPriorityOrDefault):
    """Custom type tnSapIngressMacCriteriaActionPriority based on TPriorityOrDefault"""
    defaultValue = 3


_TnSapIngressMacCriteriaActionPriority_Type.__name__ = "TPriorityOrDefault"
_TnSapIngressMacCriteriaActionPriority_Object = MibTableColumn
tnSapIngressMacCriteriaActionPriority = _TnSapIngressMacCriteriaActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 5),
    _TnSapIngressMacCriteriaActionPriority_Type()
)
tnSapIngressMacCriteriaActionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaActionPriority.setStatus("current")


class _TnSapIngressMacCriteriaFrameType_Type(TFrameType):
    """Custom type tnSapIngressMacCriteriaFrameType based on TFrameType"""
    defaultValue = 0


_TnSapIngressMacCriteriaFrameType_Type.__name__ = "TFrameType"
_TnSapIngressMacCriteriaFrameType_Object = MibTableColumn
tnSapIngressMacCriteriaFrameType = _TnSapIngressMacCriteriaFrameType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 6),
    _TnSapIngressMacCriteriaFrameType_Type()
)
tnSapIngressMacCriteriaFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaFrameType.setStatus("current")


class _TnSapIngressMacCriteriaSrcMacAddr_Type(MacAddress):
    """Custom type tnSapIngressMacCriteriaSrcMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TnSapIngressMacCriteriaSrcMacAddr_Type.__name__ = "MacAddress"
_TnSapIngressMacCriteriaSrcMacAddr_Object = MibTableColumn
tnSapIngressMacCriteriaSrcMacAddr = _TnSapIngressMacCriteriaSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 8),
    _TnSapIngressMacCriteriaSrcMacAddr_Type()
)
tnSapIngressMacCriteriaSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaSrcMacAddr.setStatus("current")


class _TnSapIngressMacCriteriaSrcMacMask_Type(MacAddress):
    """Custom type tnSapIngressMacCriteriaSrcMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TnSapIngressMacCriteriaSrcMacMask_Type.__name__ = "MacAddress"
_TnSapIngressMacCriteriaSrcMacMask_Object = MibTableColumn
tnSapIngressMacCriteriaSrcMacMask = _TnSapIngressMacCriteriaSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 9),
    _TnSapIngressMacCriteriaSrcMacMask_Type()
)
tnSapIngressMacCriteriaSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaSrcMacMask.setStatus("current")


class _TnSapIngressMacCriteriaDstMacAddr_Type(MacAddress):
    """Custom type tnSapIngressMacCriteriaDstMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TnSapIngressMacCriteriaDstMacAddr_Type.__name__ = "MacAddress"
_TnSapIngressMacCriteriaDstMacAddr_Object = MibTableColumn
tnSapIngressMacCriteriaDstMacAddr = _TnSapIngressMacCriteriaDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 10),
    _TnSapIngressMacCriteriaDstMacAddr_Type()
)
tnSapIngressMacCriteriaDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaDstMacAddr.setStatus("current")


class _TnSapIngressMacCriteriaDstMacMask_Type(MacAddress):
    """Custom type tnSapIngressMacCriteriaDstMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TnSapIngressMacCriteriaDstMacMask_Type.__name__ = "MacAddress"
_TnSapIngressMacCriteriaDstMacMask_Object = MibTableColumn
tnSapIngressMacCriteriaDstMacMask = _TnSapIngressMacCriteriaDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 11),
    _TnSapIngressMacCriteriaDstMacMask_Type()
)
tnSapIngressMacCriteriaDstMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaDstMacMask.setStatus("current")


class _TnSapIngressMacCriteriaDot1PValue_Type(Dot1PPriority):
    """Custom type tnSapIngressMacCriteriaDot1PValue based on Dot1PPriority"""
    defaultValue = -1


_TnSapIngressMacCriteriaDot1PValue_Type.__name__ = "Dot1PPriority"
_TnSapIngressMacCriteriaDot1PValue_Object = MibTableColumn
tnSapIngressMacCriteriaDot1PValue = _TnSapIngressMacCriteriaDot1PValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 12),
    _TnSapIngressMacCriteriaDot1PValue_Type()
)
tnSapIngressMacCriteriaDot1PValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaDot1PValue.setStatus("current")


class _TnSapIngressMacCriteriaDot1PMask_Type(Dot1PPriority):
    """Custom type tnSapIngressMacCriteriaDot1PMask based on Dot1PPriority"""
    defaultValue = 0

    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnSapIngressMacCriteriaDot1PMask_Type.__name__ = "Dot1PPriority"
_TnSapIngressMacCriteriaDot1PMask_Object = MibTableColumn
tnSapIngressMacCriteriaDot1PMask = _TnSapIngressMacCriteriaDot1PMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 13),
    _TnSapIngressMacCriteriaDot1PMask_Type()
)
tnSapIngressMacCriteriaDot1PMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaDot1PMask.setStatus("current")


class _TnSapIngressMacCriteriaEthernetType_Type(Integer32):
    """Custom type tnSapIngressMacCriteriaEthernetType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1536, 65535),
    )


_TnSapIngressMacCriteriaEthernetType_Type.__name__ = "Integer32"
_TnSapIngressMacCriteriaEthernetType_Object = MibTableColumn
tnSapIngressMacCriteriaEthernetType = _TnSapIngressMacCriteriaEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 14),
    _TnSapIngressMacCriteriaEthernetType_Type()
)
tnSapIngressMacCriteriaEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaEthernetType.setStatus("current")


class _TnSapIngressMacCriteriaDSAP_Type(ServiceAccessPoint):
    """Custom type tnSapIngressMacCriteriaDSAP based on ServiceAccessPoint"""
    defaultValue = -1


_TnSapIngressMacCriteriaDSAP_Type.__name__ = "ServiceAccessPoint"
_TnSapIngressMacCriteriaDSAP_Object = MibTableColumn
tnSapIngressMacCriteriaDSAP = _TnSapIngressMacCriteriaDSAP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 15),
    _TnSapIngressMacCriteriaDSAP_Type()
)
tnSapIngressMacCriteriaDSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaDSAP.setStatus("current")


class _TnSapIngressMacCriteriaDSAPMask_Type(ServiceAccessPoint):
    """Custom type tnSapIngressMacCriteriaDSAPMask based on ServiceAccessPoint"""
    defaultValue = -1


_TnSapIngressMacCriteriaDSAPMask_Type.__name__ = "ServiceAccessPoint"
_TnSapIngressMacCriteriaDSAPMask_Object = MibTableColumn
tnSapIngressMacCriteriaDSAPMask = _TnSapIngressMacCriteriaDSAPMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 16),
    _TnSapIngressMacCriteriaDSAPMask_Type()
)
tnSapIngressMacCriteriaDSAPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaDSAPMask.setStatus("current")


class _TnSapIngressMacCriteriaSSAP_Type(ServiceAccessPoint):
    """Custom type tnSapIngressMacCriteriaSSAP based on ServiceAccessPoint"""
    defaultValue = -1


_TnSapIngressMacCriteriaSSAP_Type.__name__ = "ServiceAccessPoint"
_TnSapIngressMacCriteriaSSAP_Object = MibTableColumn
tnSapIngressMacCriteriaSSAP = _TnSapIngressMacCriteriaSSAP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 17),
    _TnSapIngressMacCriteriaSSAP_Type()
)
tnSapIngressMacCriteriaSSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaSSAP.setStatus("current")


class _TnSapIngressMacCriteriaSSAPMask_Type(ServiceAccessPoint):
    """Custom type tnSapIngressMacCriteriaSSAPMask based on ServiceAccessPoint"""
    defaultValue = -1


_TnSapIngressMacCriteriaSSAPMask_Type.__name__ = "ServiceAccessPoint"
_TnSapIngressMacCriteriaSSAPMask_Object = MibTableColumn
tnSapIngressMacCriteriaSSAPMask = _TnSapIngressMacCriteriaSSAPMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 18),
    _TnSapIngressMacCriteriaSSAPMask_Type()
)
tnSapIngressMacCriteriaSSAPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaSSAPMask.setStatus("current")


class _TnSapIngressMacCriteriaSnapPid_Type(Integer32):
    """Custom type tnSapIngressMacCriteriaSnapPid based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TnSapIngressMacCriteriaSnapPid_Type.__name__ = "Integer32"
_TnSapIngressMacCriteriaSnapPid_Object = MibTableColumn
tnSapIngressMacCriteriaSnapPid = _TnSapIngressMacCriteriaSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 19),
    _TnSapIngressMacCriteriaSnapPid_Type()
)
tnSapIngressMacCriteriaSnapPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaSnapPid.setStatus("current")


class _TnSapIngressMacCriteriaSnapOui_Type(Integer32):
    """Custom type tnSapIngressMacCriteriaSnapOui based on Integer32"""
    defaultValue = 1

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
          ("zero", 2),
          ("nonZero", 3))
    )


_TnSapIngressMacCriteriaSnapOui_Type.__name__ = "Integer32"
_TnSapIngressMacCriteriaSnapOui_Object = MibTableColumn
tnSapIngressMacCriteriaSnapOui = _TnSapIngressMacCriteriaSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 20),
    _TnSapIngressMacCriteriaSnapOui_Type()
)
tnSapIngressMacCriteriaSnapOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaSnapOui.setStatus("current")
_TnSapIngressMacCriteriaLastChanged_Type = TimeStamp
_TnSapIngressMacCriteriaLastChanged_Object = MibTableColumn
tnSapIngressMacCriteriaLastChanged = _TnSapIngressMacCriteriaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 6, 1, 21),
    _TnSapIngressMacCriteriaLastChanged_Type()
)
tnSapIngressMacCriteriaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaLastChanged.setStatus("current")
_TnSapIngressFCTable_Object = MibTable
tnSapIngressFCTable = _TnSapIngressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7)
)
if mibBuilder.loadTexts:
    tnSapIngressFCTable.setStatus("current")
_TnSapIngressFCEntry_Object = MibTableRow
tnSapIngressFCEntry = _TnSapIngressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1)
)
tnSapIngressFCEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnSapIngressIndex"),
    (0, "TN-QOS-MIB", "tnSapIngressFCName"),
)
if mibBuilder.loadTexts:
    tnSapIngressFCEntry.setStatus("current")
_TnSapIngressFCName_Type = TNamedItem
_TnSapIngressFCName_Object = MibTableColumn
tnSapIngressFCName = _TnSapIngressFCName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 1),
    _TnSapIngressFCName_Type()
)
tnSapIngressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIngressFCName.setStatus("current")
_TnSapIngressFCRowStatus_Type = RowStatus
_TnSapIngressFCRowStatus_Object = MibTableColumn
tnSapIngressFCRowStatus = _TnSapIngressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 2),
    _TnSapIngressFCRowStatus_Type()
)
tnSapIngressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCRowStatus.setStatus("current")


class _TnSapIngressFCQueue_Type(TIngressQueueId):
    """Custom type tnSapIngressFCQueue based on TIngressQueueId"""
    defaultValue = 0


_TnSapIngressFCQueue_Type.__name__ = "TIngressQueueId"
_TnSapIngressFCQueue_Object = MibTableColumn
tnSapIngressFCQueue = _TnSapIngressFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 3),
    _TnSapIngressFCQueue_Type()
)
tnSapIngressFCQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCQueue.setStatus("current")


class _TnSapIngressFCMCastQueue_Type(TIngressQueueId):
    """Custom type tnSapIngressFCMCastQueue based on TIngressQueueId"""
    defaultValue = 0


_TnSapIngressFCMCastQueue_Type.__name__ = "TIngressQueueId"
_TnSapIngressFCMCastQueue_Object = MibTableColumn
tnSapIngressFCMCastQueue = _TnSapIngressFCMCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 4),
    _TnSapIngressFCMCastQueue_Type()
)
tnSapIngressFCMCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCMCastQueue.setStatus("current")


class _TnSapIngressFCBCastQueue_Type(TIngressQueueId):
    """Custom type tnSapIngressFCBCastQueue based on TIngressQueueId"""
    defaultValue = 0


_TnSapIngressFCBCastQueue_Type.__name__ = "TIngressQueueId"
_TnSapIngressFCBCastQueue_Object = MibTableColumn
tnSapIngressFCBCastQueue = _TnSapIngressFCBCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 5),
    _TnSapIngressFCBCastQueue_Type()
)
tnSapIngressFCBCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCBCastQueue.setStatus("current")


class _TnSapIngressFCUnknownQueue_Type(TIngressQueueId):
    """Custom type tnSapIngressFCUnknownQueue based on TIngressQueueId"""
    defaultValue = 0


_TnSapIngressFCUnknownQueue_Type.__name__ = "TIngressQueueId"
_TnSapIngressFCUnknownQueue_Object = MibTableColumn
tnSapIngressFCUnknownQueue = _TnSapIngressFCUnknownQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 6),
    _TnSapIngressFCUnknownQueue_Type()
)
tnSapIngressFCUnknownQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCUnknownQueue.setStatus("current")
_TnSapIngressFCLastChanged_Type = TimeStamp
_TnSapIngressFCLastChanged_Object = MibTableColumn
tnSapIngressFCLastChanged = _TnSapIngressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 7),
    _TnSapIngressFCLastChanged_Type()
)
tnSapIngressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressFCLastChanged.setStatus("current")


class _TnSapIngressFCInProfRemark_Type(TRemarkType):
    """Custom type tnSapIngressFCInProfRemark based on TRemarkType"""
    defaultValue = 1


_TnSapIngressFCInProfRemark_Type.__name__ = "TRemarkType"
_TnSapIngressFCInProfRemark_Object = MibTableColumn
tnSapIngressFCInProfRemark = _TnSapIngressFCInProfRemark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 8),
    _TnSapIngressFCInProfRemark_Type()
)
tnSapIngressFCInProfRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCInProfRemark.setStatus("current")


class _TnSapIngressFCInProfDscp_Type(TNamedItemOrEmpty):
    """Custom type tnSapIngressFCInProfDscp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressFCInProfDscp_Type.__name__ = "TNamedItemOrEmpty"
_TnSapIngressFCInProfDscp_Object = MibTableColumn
tnSapIngressFCInProfDscp = _TnSapIngressFCInProfDscp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 9),
    _TnSapIngressFCInProfDscp_Type()
)
tnSapIngressFCInProfDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCInProfDscp.setStatus("current")


class _TnSapIngressFCInProfPrec_Type(TPrecValueOrNone):
    """Custom type tnSapIngressFCInProfPrec based on TPrecValueOrNone"""
    defaultValue = -1


_TnSapIngressFCInProfPrec_Type.__name__ = "TPrecValueOrNone"
_TnSapIngressFCInProfPrec_Object = MibTableColumn
tnSapIngressFCInProfPrec = _TnSapIngressFCInProfPrec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 10),
    _TnSapIngressFCInProfPrec_Type()
)
tnSapIngressFCInProfPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCInProfPrec.setStatus("current")


class _TnSapIngressFCOutProfRemark_Type(TRemarkType):
    """Custom type tnSapIngressFCOutProfRemark based on TRemarkType"""
    defaultValue = 1


_TnSapIngressFCOutProfRemark_Type.__name__ = "TRemarkType"
_TnSapIngressFCOutProfRemark_Object = MibTableColumn
tnSapIngressFCOutProfRemark = _TnSapIngressFCOutProfRemark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 11),
    _TnSapIngressFCOutProfRemark_Type()
)
tnSapIngressFCOutProfRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCOutProfRemark.setStatus("current")


class _TnSapIngressFCOutProfDscp_Type(TNamedItemOrEmpty):
    """Custom type tnSapIngressFCOutProfDscp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressFCOutProfDscp_Type.__name__ = "TNamedItemOrEmpty"
_TnSapIngressFCOutProfDscp_Object = MibTableColumn
tnSapIngressFCOutProfDscp = _TnSapIngressFCOutProfDscp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 12),
    _TnSapIngressFCOutProfDscp_Type()
)
tnSapIngressFCOutProfDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCOutProfDscp.setStatus("current")


class _TnSapIngressFCOutProfPrec_Type(TPrecValueOrNone):
    """Custom type tnSapIngressFCOutProfPrec based on TPrecValueOrNone"""
    defaultValue = -1


_TnSapIngressFCOutProfPrec_Type.__name__ = "TPrecValueOrNone"
_TnSapIngressFCOutProfPrec_Object = MibTableColumn
tnSapIngressFCOutProfPrec = _TnSapIngressFCOutProfPrec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 13),
    _TnSapIngressFCOutProfPrec_Type()
)
tnSapIngressFCOutProfPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCOutProfPrec.setStatus("current")


class _TnSapIngressFCProfile_Type(TProfileOrNone):
    """Custom type tnSapIngressFCProfile based on TProfileOrNone"""
    defaultValue = 0


_TnSapIngressFCProfile_Type.__name__ = "TProfileOrNone"
_TnSapIngressFCProfile_Object = MibTableColumn
tnSapIngressFCProfile = _TnSapIngressFCProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 14),
    _TnSapIngressFCProfile_Type()
)
tnSapIngressFCProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCProfile.setStatus("current")


class _TnSapIngressFCHsmdaQueue_Type(TIngressHsmdaQueueId):
    """Custom type tnSapIngressFCHsmdaQueue based on TIngressHsmdaQueueId"""
    defaultValue = 0


_TnSapIngressFCHsmdaQueue_Type.__name__ = "TIngressHsmdaQueueId"
_TnSapIngressFCHsmdaQueue_Object = MibTableColumn
tnSapIngressFCHsmdaQueue = _TnSapIngressFCHsmdaQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 15),
    _TnSapIngressFCHsmdaQueue_Type()
)
tnSapIngressFCHsmdaQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCHsmdaQueue.setStatus("current")


class _TnSapIngressFCHsmdaMCastQueue_Type(TIngressHsmdaQueueId):
    """Custom type tnSapIngressFCHsmdaMCastQueue based on TIngressHsmdaQueueId"""
    defaultValue = 0


_TnSapIngressFCHsmdaMCastQueue_Type.__name__ = "TIngressHsmdaQueueId"
_TnSapIngressFCHsmdaMCastQueue_Object = MibTableColumn
tnSapIngressFCHsmdaMCastQueue = _TnSapIngressFCHsmdaMCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 16),
    _TnSapIngressFCHsmdaMCastQueue_Type()
)
tnSapIngressFCHsmdaMCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCHsmdaMCastQueue.setStatus("current")


class _TnSapIngressFCHsmdaBCastQueue_Type(TIngressHsmdaQueueId):
    """Custom type tnSapIngressFCHsmdaBCastQueue based on TIngressHsmdaQueueId"""
    defaultValue = 0


_TnSapIngressFCHsmdaBCastQueue_Type.__name__ = "TIngressHsmdaQueueId"
_TnSapIngressFCHsmdaBCastQueue_Object = MibTableColumn
tnSapIngressFCHsmdaBCastQueue = _TnSapIngressFCHsmdaBCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 17),
    _TnSapIngressFCHsmdaBCastQueue_Type()
)
tnSapIngressFCHsmdaBCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCHsmdaBCastQueue.setStatus("current")


class _TnSapIngressFCDE1OutOfProfile_Type(TruthValue):
    """Custom type tnSapIngressFCDE1OutOfProfile based on TruthValue"""
    defaultValue = 2


_TnSapIngressFCDE1OutOfProfile_Type.__name__ = "TruthValue"
_TnSapIngressFCDE1OutOfProfile_Object = MibTableColumn
tnSapIngressFCDE1OutOfProfile = _TnSapIngressFCDE1OutOfProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 18),
    _TnSapIngressFCDE1OutOfProfile_Type()
)
tnSapIngressFCDE1OutOfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCDE1OutOfProfile.setStatus("current")


class _TnSapIngressFCQGrp_Type(TNamedItemOrEmpty):
    """Custom type tnSapIngressFCQGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressFCQGrp_Type.__name__ = "TNamedItemOrEmpty"
_TnSapIngressFCQGrp_Object = MibTableColumn
tnSapIngressFCQGrp = _TnSapIngressFCQGrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 19),
    _TnSapIngressFCQGrp_Type()
)
tnSapIngressFCQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCQGrp.setStatus("current")


class _TnSapIngressFCQGrpMCast_Type(TNamedItemOrEmpty):
    """Custom type tnSapIngressFCQGrpMCast based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressFCQGrpMCast_Type.__name__ = "TNamedItemOrEmpty"
_TnSapIngressFCQGrpMCast_Object = MibTableColumn
tnSapIngressFCQGrpMCast = _TnSapIngressFCQGrpMCast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 20),
    _TnSapIngressFCQGrpMCast_Type()
)
tnSapIngressFCQGrpMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCQGrpMCast.setStatus("current")


class _TnSapIngressFCQGrpBCast_Type(TNamedItemOrEmpty):
    """Custom type tnSapIngressFCQGrpBCast based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressFCQGrpBCast_Type.__name__ = "TNamedItemOrEmpty"
_TnSapIngressFCQGrpBCast_Object = MibTableColumn
tnSapIngressFCQGrpBCast = _TnSapIngressFCQGrpBCast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 21),
    _TnSapIngressFCQGrpBCast_Type()
)
tnSapIngressFCQGrpBCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCQGrpBCast.setStatus("current")


class _TnSapIngressFCQGrpUnknown_Type(TNamedItemOrEmpty):
    """Custom type tnSapIngressFCQGrpUnknown based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressFCQGrpUnknown_Type.__name__ = "TNamedItemOrEmpty"
_TnSapIngressFCQGrpUnknown_Object = MibTableColumn
tnSapIngressFCQGrpUnknown = _TnSapIngressFCQGrpUnknown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 7, 1, 22),
    _TnSapIngressFCQGrpUnknown_Type()
)
tnSapIngressFCQGrpUnknown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCQGrpUnknown.setStatus("current")
_TnSapIngressIPv6CriteriaTable_Object = MibTable
tnSapIngressIPv6CriteriaTable = _TnSapIngressIPv6CriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9)
)
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaTable.setStatus("current")
_TnSapIngressIPv6CriteriaEntry_Object = MibTableRow
tnSapIngressIPv6CriteriaEntry = _TnSapIngressIPv6CriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1)
)
tnSapIngressIPv6CriteriaEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnSapIngressIndex"),
    (0, "TN-QOS-MIB", "tnSapIngressIPv6CriteriaIndex"),
)
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaEntry.setStatus("current")
_TnSapIngressIPv6CriteriaIndex_Type = TEntryId
_TnSapIngressIPv6CriteriaIndex_Object = MibTableColumn
tnSapIngressIPv6CriteriaIndex = _TnSapIngressIPv6CriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 1),
    _TnSapIngressIPv6CriteriaIndex_Type()
)
tnSapIngressIPv6CriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaIndex.setStatus("current")
_TnSapIngressIPv6CriteriaRowStatus_Type = RowStatus
_TnSapIngressIPv6CriteriaRowStatus_Object = MibTableColumn
tnSapIngressIPv6CriteriaRowStatus = _TnSapIngressIPv6CriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 2),
    _TnSapIngressIPv6CriteriaRowStatus_Type()
)
tnSapIngressIPv6CriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaRowStatus.setStatus("current")


class _TnSapIngressIPv6CriteriaDescription_Type(TItemDescription):
    """Custom type tnSapIngressIPv6CriteriaDescription based on TItemDescription"""
    defaultHexValue = ""


_TnSapIngressIPv6CriteriaDescription_Type.__name__ = "TItemDescription"
_TnSapIngressIPv6CriteriaDescription_Object = MibTableColumn
tnSapIngressIPv6CriteriaDescription = _TnSapIngressIPv6CriteriaDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 3),
    _TnSapIngressIPv6CriteriaDescription_Type()
)
tnSapIngressIPv6CriteriaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaDescription.setStatus("current")


class _TnSapIngressIPv6CriteriaActionFC_Type(TNamedItemOrEmpty):
    """Custom type tnSapIngressIPv6CriteriaActionFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapIngressIPv6CriteriaActionFC_Type.__name__ = "TNamedItemOrEmpty"
_TnSapIngressIPv6CriteriaActionFC_Object = MibTableColumn
tnSapIngressIPv6CriteriaActionFC = _TnSapIngressIPv6CriteriaActionFC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 4),
    _TnSapIngressIPv6CriteriaActionFC_Type()
)
tnSapIngressIPv6CriteriaActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaActionFC.setStatus("current")


class _TnSapIngressIPv6CriteriaActionPriority_Type(TPriorityOrDefault):
    """Custom type tnSapIngressIPv6CriteriaActionPriority based on TPriorityOrDefault"""
    defaultValue = 3


_TnSapIngressIPv6CriteriaActionPriority_Type.__name__ = "TPriorityOrDefault"
_TnSapIngressIPv6CriteriaActionPriority_Object = MibTableColumn
tnSapIngressIPv6CriteriaActionPriority = _TnSapIngressIPv6CriteriaActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 5),
    _TnSapIngressIPv6CriteriaActionPriority_Type()
)
tnSapIngressIPv6CriteriaActionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaActionPriority.setStatus("current")


class _TnSapIngressIPv6CriteriaSourceIpAddr_Type(InetAddressIPv6):
    """Custom type tnSapIngressIPv6CriteriaSourceIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TnSapIngressIPv6CriteriaSourceIpAddr_Type.__name__ = "InetAddressIPv6"
_TnSapIngressIPv6CriteriaSourceIpAddr_Object = MibTableColumn
tnSapIngressIPv6CriteriaSourceIpAddr = _TnSapIngressIPv6CriteriaSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 6),
    _TnSapIngressIPv6CriteriaSourceIpAddr_Type()
)
tnSapIngressIPv6CriteriaSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaSourceIpAddr.setStatus("current")


class _TnSapIngressIPv6CriteriaSourceIpMask_Type(InetAddressPrefixLength):
    """Custom type tnSapIngressIPv6CriteriaSourceIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TnSapIngressIPv6CriteriaSourceIpMask_Type.__name__ = "InetAddressPrefixLength"
_TnSapIngressIPv6CriteriaSourceIpMask_Object = MibTableColumn
tnSapIngressIPv6CriteriaSourceIpMask = _TnSapIngressIPv6CriteriaSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 7),
    _TnSapIngressIPv6CriteriaSourceIpMask_Type()
)
tnSapIngressIPv6CriteriaSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaSourceIpMask.setStatus("current")


class _TnSapIngressIPv6CriteriaDestIpAddr_Type(InetAddressIPv6):
    """Custom type tnSapIngressIPv6CriteriaDestIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TnSapIngressIPv6CriteriaDestIpAddr_Type.__name__ = "InetAddressIPv6"
_TnSapIngressIPv6CriteriaDestIpAddr_Object = MibTableColumn
tnSapIngressIPv6CriteriaDestIpAddr = _TnSapIngressIPv6CriteriaDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 8),
    _TnSapIngressIPv6CriteriaDestIpAddr_Type()
)
tnSapIngressIPv6CriteriaDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaDestIpAddr.setStatus("current")


class _TnSapIngressIPv6CriteriaDestIpMask_Type(InetAddressPrefixLength):
    """Custom type tnSapIngressIPv6CriteriaDestIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TnSapIngressIPv6CriteriaDestIpMask_Type.__name__ = "InetAddressPrefixLength"
_TnSapIngressIPv6CriteriaDestIpMask_Object = MibTableColumn
tnSapIngressIPv6CriteriaDestIpMask = _TnSapIngressIPv6CriteriaDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 9),
    _TnSapIngressIPv6CriteriaDestIpMask_Type()
)
tnSapIngressIPv6CriteriaDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaDestIpMask.setStatus("current")


class _TnSapIngressIPv6CriteriaNextHeader_Type(TIpProtocol):
    """Custom type tnSapIngressIPv6CriteriaNextHeader based on TIpProtocol"""
    defaultValue = -1


_TnSapIngressIPv6CriteriaNextHeader_Type.__name__ = "TIpProtocol"
_TnSapIngressIPv6CriteriaNextHeader_Object = MibTableColumn
tnSapIngressIPv6CriteriaNextHeader = _TnSapIngressIPv6CriteriaNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 10),
    _TnSapIngressIPv6CriteriaNextHeader_Type()
)
tnSapIngressIPv6CriteriaNextHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaNextHeader.setStatus("current")


class _TnSapIngressIPv6CriteriaSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tnSapIngressIPv6CriteriaSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TnSapIngressIPv6CriteriaSourcePortValue1_Type.__name__ = "TTcpUdpPort"
_TnSapIngressIPv6CriteriaSourcePortValue1_Object = MibTableColumn
tnSapIngressIPv6CriteriaSourcePortValue1 = _TnSapIngressIPv6CriteriaSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 11),
    _TnSapIngressIPv6CriteriaSourcePortValue1_Type()
)
tnSapIngressIPv6CriteriaSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaSourcePortValue1.setStatus("current")


class _TnSapIngressIPv6CriteriaSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tnSapIngressIPv6CriteriaSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TnSapIngressIPv6CriteriaSourcePortValue2_Type.__name__ = "TTcpUdpPort"
_TnSapIngressIPv6CriteriaSourcePortValue2_Object = MibTableColumn
tnSapIngressIPv6CriteriaSourcePortValue2 = _TnSapIngressIPv6CriteriaSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 12),
    _TnSapIngressIPv6CriteriaSourcePortValue2_Type()
)
tnSapIngressIPv6CriteriaSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaSourcePortValue2.setStatus("current")


class _TnSapIngressIPv6CriteriaSourcePortOperator_Type(TTcpUdpPortOperator):
    """Custom type tnSapIngressIPv6CriteriaSourcePortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_TnSapIngressIPv6CriteriaSourcePortOperator_Type.__name__ = "TTcpUdpPortOperator"
_TnSapIngressIPv6CriteriaSourcePortOperator_Object = MibTableColumn
tnSapIngressIPv6CriteriaSourcePortOperator = _TnSapIngressIPv6CriteriaSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 13),
    _TnSapIngressIPv6CriteriaSourcePortOperator_Type()
)
tnSapIngressIPv6CriteriaSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaSourcePortOperator.setStatus("current")


class _TnSapIngressIPv6CriteriaDestPortValue1_Type(TTcpUdpPort):
    """Custom type tnSapIngressIPv6CriteriaDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TnSapIngressIPv6CriteriaDestPortValue1_Type.__name__ = "TTcpUdpPort"
_TnSapIngressIPv6CriteriaDestPortValue1_Object = MibTableColumn
tnSapIngressIPv6CriteriaDestPortValue1 = _TnSapIngressIPv6CriteriaDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 14),
    _TnSapIngressIPv6CriteriaDestPortValue1_Type()
)
tnSapIngressIPv6CriteriaDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaDestPortValue1.setStatus("current")


class _TnSapIngressIPv6CriteriaDestPortValue2_Type(TTcpUdpPort):
    """Custom type tnSapIngressIPv6CriteriaDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TnSapIngressIPv6CriteriaDestPortValue2_Type.__name__ = "TTcpUdpPort"
_TnSapIngressIPv6CriteriaDestPortValue2_Object = MibTableColumn
tnSapIngressIPv6CriteriaDestPortValue2 = _TnSapIngressIPv6CriteriaDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 15),
    _TnSapIngressIPv6CriteriaDestPortValue2_Type()
)
tnSapIngressIPv6CriteriaDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaDestPortValue2.setStatus("current")


class _TnSapIngressIPv6CriteriaDestPortOperator_Type(TTcpUdpPortOperator):
    """Custom type tnSapIngressIPv6CriteriaDestPortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_TnSapIngressIPv6CriteriaDestPortOperator_Type.__name__ = "TTcpUdpPortOperator"
_TnSapIngressIPv6CriteriaDestPortOperator_Object = MibTableColumn
tnSapIngressIPv6CriteriaDestPortOperator = _TnSapIngressIPv6CriteriaDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 16),
    _TnSapIngressIPv6CriteriaDestPortOperator_Type()
)
tnSapIngressIPv6CriteriaDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaDestPortOperator.setStatus("current")


class _TnSapIngressIPv6CriteriaDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tnSapIngressIPv6CriteriaDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TnSapIngressIPv6CriteriaDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TnSapIngressIPv6CriteriaDSCP_Object = MibTableColumn
tnSapIngressIPv6CriteriaDSCP = _TnSapIngressIPv6CriteriaDSCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 17),
    _TnSapIngressIPv6CriteriaDSCP_Type()
)
tnSapIngressIPv6CriteriaDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaDSCP.setStatus("current")
_TnSapIngressIPv6CriteriaLastChanged_Type = TimeStamp
_TnSapIngressIPv6CriteriaLastChanged_Object = MibTableColumn
tnSapIngressIPv6CriteriaLastChanged = _TnSapIngressIPv6CriteriaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 9, 1, 20),
    _TnSapIngressIPv6CriteriaLastChanged_Type()
)
tnSapIngressIPv6CriteriaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaLastChanged.setStatus("current")
_TnSapIngressScalar1_Type = Unsigned32
_TnSapIngressScalar1_Object = MibScalar
tnSapIngressScalar1 = _TnSapIngressScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 101),
    _TnSapIngressScalar1_Type()
)
tnSapIngressScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressScalar1.setStatus("current")
_TnSapIngressScalar2_Type = Unsigned32
_TnSapIngressScalar2_Object = MibScalar
tnSapIngressScalar2 = _TnSapIngressScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 3, 102),
    _TnSapIngressScalar2_Type()
)
tnSapIngressScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressScalar2.setStatus("current")
_TnNetworkObjects_ObjectIdentity = ObjectIdentity
tnNetworkObjects = _TnNetworkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5)
)
_TnNetworkPolicyTable_Object = MibTable
tnNetworkPolicyTable = _TnNetworkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1)
)
if mibBuilder.loadTexts:
    tnNetworkPolicyTable.setStatus("current")
_TnNetworkPolicyEntry_Object = MibTableRow
tnNetworkPolicyEntry = _TnNetworkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1)
)
tnNetworkPolicyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnNetworkPolicyIndex"),
)
if mibBuilder.loadTexts:
    tnNetworkPolicyEntry.setStatus("current")
_TnNetworkPolicyIndex_Type = TNetworkPolicyID
_TnNetworkPolicyIndex_Object = MibTableColumn
tnNetworkPolicyIndex = _TnNetworkPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 1),
    _TnNetworkPolicyIndex_Type()
)
tnNetworkPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetworkPolicyIndex.setStatus("current")
_TnNetworkPolicyRowStatus_Type = RowStatus
_TnNetworkPolicyRowStatus_Object = MibTableColumn
tnNetworkPolicyRowStatus = _TnNetworkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 2),
    _TnNetworkPolicyRowStatus_Type()
)
tnNetworkPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyRowStatus.setStatus("current")


class _TnNetworkPolicyScope_Type(TItemScope):
    """Custom type tnNetworkPolicyScope based on TItemScope"""
    defaultValue = 2


_TnNetworkPolicyScope_Type.__name__ = "TItemScope"
_TnNetworkPolicyScope_Object = MibTableColumn
tnNetworkPolicyScope = _TnNetworkPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 5),
    _TnNetworkPolicyScope_Type()
)
tnNetworkPolicyScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyScope.setStatus("current")


class _TnNetworkPolicyDescription_Type(TItemDescription):
    """Custom type tnNetworkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TnNetworkPolicyDescription_Type.__name__ = "TItemDescription"
_TnNetworkPolicyDescription_Object = MibTableColumn
tnNetworkPolicyDescription = _TnNetworkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 6),
    _TnNetworkPolicyDescription_Type()
)
tnNetworkPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyDescription.setStatus("current")


class _TnNetworkPolicyIngressDefaultActionFC_Type(TFCName):
    """Custom type tnNetworkPolicyIngressDefaultActionFC based on TFCName"""
    defaultHexValue = "be"


_TnNetworkPolicyIngressDefaultActionFC_Type.__name__ = "TFCName"
_TnNetworkPolicyIngressDefaultActionFC_Object = MibTableColumn
tnNetworkPolicyIngressDefaultActionFC = _TnNetworkPolicyIngressDefaultActionFC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 7),
    _TnNetworkPolicyIngressDefaultActionFC_Type()
)
tnNetworkPolicyIngressDefaultActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyIngressDefaultActionFC.setStatus("current")


class _TnNetworkPolicyIngressDefaultActionProfile_Type(TProfile):
    """Custom type tnNetworkPolicyIngressDefaultActionProfile based on TProfile"""
    defaultValue = 2


_TnNetworkPolicyIngressDefaultActionProfile_Type.__name__ = "TProfile"
_TnNetworkPolicyIngressDefaultActionProfile_Object = MibTableColumn
tnNetworkPolicyIngressDefaultActionProfile = _TnNetworkPolicyIngressDefaultActionProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 8),
    _TnNetworkPolicyIngressDefaultActionProfile_Type()
)
tnNetworkPolicyIngressDefaultActionProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyIngressDefaultActionProfile.setStatus("current")


class _TnNetworkPolicyEgressRemark_Type(TruthValue):
    """Custom type tnNetworkPolicyEgressRemark based on TruthValue"""
    defaultValue = 2


_TnNetworkPolicyEgressRemark_Type.__name__ = "TruthValue"
_TnNetworkPolicyEgressRemark_Object = MibTableColumn
tnNetworkPolicyEgressRemark = _TnNetworkPolicyEgressRemark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 9),
    _TnNetworkPolicyEgressRemark_Type()
)
tnNetworkPolicyEgressRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyEgressRemark.setStatus("current")
_TnNetworkPolicyLastChanged_Type = TimeStamp
_TnNetworkPolicyLastChanged_Object = MibTableColumn
tnNetworkPolicyLastChanged = _TnNetworkPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 10),
    _TnNetworkPolicyLastChanged_Type()
)
tnNetworkPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkPolicyLastChanged.setStatus("current")


class _TnNetworkPolicyIngressLerUseDscp_Type(TruthValue):
    """Custom type tnNetworkPolicyIngressLerUseDscp based on TruthValue"""
    defaultValue = 2


_TnNetworkPolicyIngressLerUseDscp_Type.__name__ = "TruthValue"
_TnNetworkPolicyIngressLerUseDscp_Object = MibTableColumn
tnNetworkPolicyIngressLerUseDscp = _TnNetworkPolicyIngressLerUseDscp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 11),
    _TnNetworkPolicyIngressLerUseDscp_Type()
)
tnNetworkPolicyIngressLerUseDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyIngressLerUseDscp.setStatus("current")


class _TnNetworkPolicyEgressRemarkDscp_Type(TruthValue):
    """Custom type tnNetworkPolicyEgressRemarkDscp based on TruthValue"""
    defaultValue = 2


_TnNetworkPolicyEgressRemarkDscp_Type.__name__ = "TruthValue"
_TnNetworkPolicyEgressRemarkDscp_Object = MibTableColumn
tnNetworkPolicyEgressRemarkDscp = _TnNetworkPolicyEgressRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 1, 1, 12),
    _TnNetworkPolicyEgressRemarkDscp_Type()
)
tnNetworkPolicyEgressRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyEgressRemarkDscp.setStatus("current")
_TnNetworkIngressDot1pTable_Object = MibTable
tnNetworkIngressDot1pTable = _TnNetworkIngressDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 3)
)
if mibBuilder.loadTexts:
    tnNetworkIngressDot1pTable.setStatus("current")
_TnNetworkIngressDot1pEntry_Object = MibTableRow
tnNetworkIngressDot1pEntry = _TnNetworkIngressDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 3, 1)
)
tnNetworkIngressDot1pEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnNetworkPolicyIndex"),
    (0, "TN-QOS-MIB", "tnNetworkIngressDot1pValue"),
)
if mibBuilder.loadTexts:
    tnNetworkIngressDot1pEntry.setStatus("current")


class _TnNetworkIngressDot1pValue_Type(Dot1PPriority):
    """Custom type tnNetworkIngressDot1pValue based on Dot1PPriority"""
    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnNetworkIngressDot1pValue_Type.__name__ = "Dot1PPriority"
_TnNetworkIngressDot1pValue_Object = MibTableColumn
tnNetworkIngressDot1pValue = _TnNetworkIngressDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 3, 1, 1),
    _TnNetworkIngressDot1pValue_Type()
)
tnNetworkIngressDot1pValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetworkIngressDot1pValue.setStatus("current")
_TnNetworkIngressDot1pRowStatus_Type = RowStatus
_TnNetworkIngressDot1pRowStatus_Object = MibTableColumn
tnNetworkIngressDot1pRowStatus = _TnNetworkIngressDot1pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 3, 1, 2),
    _TnNetworkIngressDot1pRowStatus_Type()
)
tnNetworkIngressDot1pRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressDot1pRowStatus.setStatus("current")
_TnNetworkIngressDot1pFC_Type = TFCName
_TnNetworkIngressDot1pFC_Object = MibTableColumn
tnNetworkIngressDot1pFC = _TnNetworkIngressDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 3, 1, 3),
    _TnNetworkIngressDot1pFC_Type()
)
tnNetworkIngressDot1pFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressDot1pFC.setStatus("current")
_TnNetworkIngressDot1pProfile_Type = TDEProfile
_TnNetworkIngressDot1pProfile_Object = MibTableColumn
tnNetworkIngressDot1pProfile = _TnNetworkIngressDot1pProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 3, 1, 4),
    _TnNetworkIngressDot1pProfile_Type()
)
tnNetworkIngressDot1pProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressDot1pProfile.setStatus("current")
_TnNetworkIngressDot1pLastChanged_Type = TimeStamp
_TnNetworkIngressDot1pLastChanged_Object = MibTableColumn
tnNetworkIngressDot1pLastChanged = _TnNetworkIngressDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 3, 1, 5),
    _TnNetworkIngressDot1pLastChanged_Type()
)
tnNetworkIngressDot1pLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkIngressDot1pLastChanged.setStatus("current")
_TnNetworkEgressFCTable_Object = MibTable
tnNetworkEgressFCTable = _TnNetworkEgressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7)
)
if mibBuilder.loadTexts:
    tnNetworkEgressFCTable.setStatus("current")
_TnNetworkEgressFCEntry_Object = MibTableRow
tnNetworkEgressFCEntry = _TnNetworkEgressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1)
)
tnNetworkEgressFCEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnNetworkPolicyIndex"),
    (0, "TN-QOS-MIB", "tnNetworkEgressFCName"),
)
if mibBuilder.loadTexts:
    tnNetworkEgressFCEntry.setStatus("current")
_TnNetworkEgressFCName_Type = TFCName
_TnNetworkEgressFCName_Object = MibTableColumn
tnNetworkEgressFCName = _TnNetworkEgressFCName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 1),
    _TnNetworkEgressFCName_Type()
)
tnNetworkEgressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetworkEgressFCName.setStatus("current")
_TnNetworkEgressFCDSCPInProfile_Type = TDSCPNameOrEmpty
_TnNetworkEgressFCDSCPInProfile_Object = MibTableColumn
tnNetworkEgressFCDSCPInProfile = _TnNetworkEgressFCDSCPInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 2),
    _TnNetworkEgressFCDSCPInProfile_Type()
)
tnNetworkEgressFCDSCPInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCDSCPInProfile.setStatus("current")
_TnNetworkEgressFCDSCPOutProfile_Type = TDSCPNameOrEmpty
_TnNetworkEgressFCDSCPOutProfile_Object = MibTableColumn
tnNetworkEgressFCDSCPOutProfile = _TnNetworkEgressFCDSCPOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 3),
    _TnNetworkEgressFCDSCPOutProfile_Type()
)
tnNetworkEgressFCDSCPOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCDSCPOutProfile.setStatus("current")
_TnNetworkEgressFCLspExpInProfile_Type = TLspExpValue
_TnNetworkEgressFCLspExpInProfile_Object = MibTableColumn
tnNetworkEgressFCLspExpInProfile = _TnNetworkEgressFCLspExpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 4),
    _TnNetworkEgressFCLspExpInProfile_Type()
)
tnNetworkEgressFCLspExpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCLspExpInProfile.setStatus("current")
_TnNetworkEgressFCLspExpOutProfile_Type = TLspExpValue
_TnNetworkEgressFCLspExpOutProfile_Object = MibTableColumn
tnNetworkEgressFCLspExpOutProfile = _TnNetworkEgressFCLspExpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 5),
    _TnNetworkEgressFCLspExpOutProfile_Type()
)
tnNetworkEgressFCLspExpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCLspExpOutProfile.setStatus("current")
_TnNetworkEgressFCDot1pInProfile_Type = Dot1PPriority
_TnNetworkEgressFCDot1pInProfile_Object = MibTableColumn
tnNetworkEgressFCDot1pInProfile = _TnNetworkEgressFCDot1pInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 6),
    _TnNetworkEgressFCDot1pInProfile_Type()
)
tnNetworkEgressFCDot1pInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCDot1pInProfile.setStatus("current")
_TnNetworkEgressFCDot1pOutProfile_Type = Dot1PPriority
_TnNetworkEgressFCDot1pOutProfile_Object = MibTableColumn
tnNetworkEgressFCDot1pOutProfile = _TnNetworkEgressFCDot1pOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 7),
    _TnNetworkEgressFCDot1pOutProfile_Type()
)
tnNetworkEgressFCDot1pOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCDot1pOutProfile.setStatus("current")
_TnNetworkEgressFCLastChanged_Type = TimeStamp
_TnNetworkEgressFCLastChanged_Object = MibTableColumn
tnNetworkEgressFCLastChanged = _TnNetworkEgressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 8),
    _TnNetworkEgressFCLastChanged_Type()
)
tnNetworkEgressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkEgressFCLastChanged.setStatus("current")


class _TnNetworkEgressFCForceDEValue_Type(TDEValue):
    """Custom type tnNetworkEgressFCForceDEValue based on TDEValue"""
    defaultValue = -1


_TnNetworkEgressFCForceDEValue_Type.__name__ = "TDEValue"
_TnNetworkEgressFCForceDEValue_Object = MibTableColumn
tnNetworkEgressFCForceDEValue = _TnNetworkEgressFCForceDEValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 9),
    _TnNetworkEgressFCForceDEValue_Type()
)
tnNetworkEgressFCForceDEValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCForceDEValue.setStatus("current")


class _TnNetworkEgressFCDEMark_Type(TruthValue):
    """Custom type tnNetworkEgressFCDEMark based on TruthValue"""
    defaultValue = 2


_TnNetworkEgressFCDEMark_Type.__name__ = "TruthValue"
_TnNetworkEgressFCDEMark_Object = MibTableColumn
tnNetworkEgressFCDEMark = _TnNetworkEgressFCDEMark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 10),
    _TnNetworkEgressFCDEMark_Type()
)
tnNetworkEgressFCDEMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCDEMark.setStatus("current")


class _TnNetworkEgressFCQGrpQueue_Type(TEgressQueueId):
    """Custom type tnNetworkEgressFCQGrpQueue based on TEgressQueueId"""
    defaultValue = 0


_TnNetworkEgressFCQGrpQueue_Type.__name__ = "TEgressQueueId"
_TnNetworkEgressFCQGrpQueue_Object = MibTableColumn
tnNetworkEgressFCQGrpQueue = _TnNetworkEgressFCQGrpQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 7, 1, 11),
    _TnNetworkEgressFCQGrpQueue_Type()
)
tnNetworkEgressFCQGrpQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkEgressFCQGrpQueue.setStatus("current")
_TnNetworkScalar1_Type = Unsigned32
_TnNetworkScalar1_Object = MibScalar
tnNetworkScalar1 = _TnNetworkScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 101),
    _TnNetworkScalar1_Type()
)
tnNetworkScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkScalar1.setStatus("current")
_TnNetworkScalar2_Type = Unsigned32
_TnNetworkScalar2_Object = MibScalar
tnNetworkScalar2 = _TnNetworkScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 5, 102),
    _TnNetworkScalar2_Type()
)
tnNetworkScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkScalar2.setStatus("current")
_TnNetworkQueueObjects_ObjectIdentity = ObjectIdentity
tnNetworkQueueObjects = _TnNetworkQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6)
)
_TnNetworkQueuePolicyTable_Object = MibTable
tnNetworkQueuePolicyTable = _TnNetworkQueuePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 1)
)
if mibBuilder.loadTexts:
    tnNetworkQueuePolicyTable.setStatus("current")
_TnNetworkQueuePolicyEntry_Object = MibTableRow
tnNetworkQueuePolicyEntry = _TnNetworkQueuePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 1, 1)
)
tnNetworkQueuePolicyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnNetworkQueuePolicy"),
)
if mibBuilder.loadTexts:
    tnNetworkQueuePolicyEntry.setStatus("current")
_TnNetworkQueuePolicy_Type = TNamedItem
_TnNetworkQueuePolicy_Object = MibTableColumn
tnNetworkQueuePolicy = _TnNetworkQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 1, 1, 1),
    _TnNetworkQueuePolicy_Type()
)
tnNetworkQueuePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetworkQueuePolicy.setStatus("current")
_TnNetworkQueuePolicyRowStatus_Type = RowStatus
_TnNetworkQueuePolicyRowStatus_Object = MibTableColumn
tnNetworkQueuePolicyRowStatus = _TnNetworkQueuePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 1, 1, 2),
    _TnNetworkQueuePolicyRowStatus_Type()
)
tnNetworkQueuePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePolicyRowStatus.setStatus("current")


class _TnNetworkQueuePolicyDescription_Type(TItemDescription):
    """Custom type tnNetworkQueuePolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TnNetworkQueuePolicyDescription_Type.__name__ = "TItemDescription"
_TnNetworkQueuePolicyDescription_Object = MibTableColumn
tnNetworkQueuePolicyDescription = _TnNetworkQueuePolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 1, 1, 3),
    _TnNetworkQueuePolicyDescription_Type()
)
tnNetworkQueuePolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePolicyDescription.setStatus("current")
_TnNetworkQueuePolicyLastChanged_Type = TimeStamp
_TnNetworkQueuePolicyLastChanged_Object = MibTableColumn
tnNetworkQueuePolicyLastChanged = _TnNetworkQueuePolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 1, 1, 8),
    _TnNetworkQueuePolicyLastChanged_Type()
)
tnNetworkQueuePolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkQueuePolicyLastChanged.setStatus("current")
_TnNetworkQueueTable_Object = MibTable
tnNetworkQueueTable = _TnNetworkQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2)
)
if mibBuilder.loadTexts:
    tnNetworkQueueTable.setStatus("current")
_TnNetworkQueueEntry_Object = MibTableRow
tnNetworkQueueEntry = _TnNetworkQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1)
)
tnNetworkQueueEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnNetworkQueuePolicy"),
    (0, "TN-QOS-MIB", "tnNetworkQueue"),
)
if mibBuilder.loadTexts:
    tnNetworkQueueEntry.setStatus("current")


class _TnNetworkQueue_Type(TQueueId):
    """Custom type tnNetworkQueue based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TnNetworkQueue_Type.__name__ = "TQueueId"
_TnNetworkQueue_Object = MibTableColumn
tnNetworkQueue = _TnNetworkQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 1),
    _TnNetworkQueue_Type()
)
tnNetworkQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetworkQueue.setStatus("current")
_TnNetworkQueueRowStatus_Type = RowStatus
_TnNetworkQueueRowStatus_Object = MibTableColumn
tnNetworkQueueRowStatus = _TnNetworkQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 2),
    _TnNetworkQueueRowStatus_Type()
)
tnNetworkQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueRowStatus.setStatus("current")


class _TnNetworkQueuePoolName_Type(TNamedItemOrEmpty):
    """Custom type tnNetworkQueuePoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnNetworkQueuePoolName_Type.__name__ = "TNamedItemOrEmpty"
_TnNetworkQueuePoolName_Object = MibTableColumn
tnNetworkQueuePoolName = _TnNetworkQueuePoolName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 3),
    _TnNetworkQueuePoolName_Type()
)
tnNetworkQueuePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePoolName.setStatus("current")


class _TnNetworkQueueParent_Type(TNamedItemOrEmpty):
    """Custom type tnNetworkQueueParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnNetworkQueueParent_Type.__name__ = "TNamedItemOrEmpty"
_TnNetworkQueueParent_Object = MibTableColumn
tnNetworkQueueParent = _TnNetworkQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 4),
    _TnNetworkQueueParent_Type()
)
tnNetworkQueueParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueParent.setStatus("current")


class _TnNetworkQueueLevel_Type(TLevel):
    """Custom type tnNetworkQueueLevel based on TLevel"""
    defaultValue = 1


_TnNetworkQueueLevel_Type.__name__ = "TLevel"
_TnNetworkQueueLevel_Object = MibTableColumn
tnNetworkQueueLevel = _TnNetworkQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 5),
    _TnNetworkQueueLevel_Type()
)
tnNetworkQueueLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueLevel.setStatus("current")


class _TnNetworkQueueWeight_Type(TWeight):
    """Custom type tnNetworkQueueWeight based on TWeight"""
    defaultValue = 1


_TnNetworkQueueWeight_Type.__name__ = "TWeight"
_TnNetworkQueueWeight_Object = MibTableColumn
tnNetworkQueueWeight = _TnNetworkQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 6),
    _TnNetworkQueueWeight_Type()
)
tnNetworkQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueWeight.setStatus("current")


class _TnNetworkQueueCIRLevel_Type(TLevelOrDefault):
    """Custom type tnNetworkQueueCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_TnNetworkQueueCIRLevel_Type.__name__ = "TLevelOrDefault"
_TnNetworkQueueCIRLevel_Object = MibTableColumn
tnNetworkQueueCIRLevel = _TnNetworkQueueCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 7),
    _TnNetworkQueueCIRLevel_Type()
)
tnNetworkQueueCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueCIRLevel.setStatus("current")


class _TnNetworkQueueCIRWeight_Type(TWeight):
    """Custom type tnNetworkQueueCIRWeight based on TWeight"""
    defaultValue = 1


_TnNetworkQueueCIRWeight_Type.__name__ = "TWeight"
_TnNetworkQueueCIRWeight_Object = MibTableColumn
tnNetworkQueueCIRWeight = _TnNetworkQueueCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 8),
    _TnNetworkQueueCIRWeight_Type()
)
tnNetworkQueueCIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueCIRWeight.setStatus("current")


class _TnNetworkQueueMCast_Type(TruthValue):
    """Custom type tnNetworkQueueMCast based on TruthValue"""
    defaultValue = 2


_TnNetworkQueueMCast_Type.__name__ = "TruthValue"
_TnNetworkQueueMCast_Object = MibTableColumn
tnNetworkQueueMCast = _TnNetworkQueueMCast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 9),
    _TnNetworkQueueMCast_Type()
)
tnNetworkQueueMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueMCast.setStatus("current")


class _TnNetworkQueueExpedite_Type(Integer32):
    """Custom type tnNetworkQueueExpedite based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expedited", 1),
          ("auto-expedited", 2),
          ("non-expedited", 3))
    )


_TnNetworkQueueExpedite_Type.__name__ = "Integer32"
_TnNetworkQueueExpedite_Object = MibTableColumn
tnNetworkQueueExpedite = _TnNetworkQueueExpedite_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 10),
    _TnNetworkQueueExpedite_Type()
)
tnNetworkQueueExpedite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueExpedite.setStatus("current")


class _TnNetworkQueueCIR_Type(TRatePercent):
    """Custom type tnNetworkQueueCIR based on TRatePercent"""
    defaultValue = 0


_TnNetworkQueueCIR_Type.__name__ = "TRatePercent"
_TnNetworkQueueCIR_Object = MibTableColumn
tnNetworkQueueCIR = _TnNetworkQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 11),
    _TnNetworkQueueCIR_Type()
)
tnNetworkQueueCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueCIR.setStatus("current")


class _TnNetworkQueuePIR_Type(TPIRRatePercent):
    """Custom type tnNetworkQueuePIR based on TPIRRatePercent"""
    defaultValue = 100


_TnNetworkQueuePIR_Type.__name__ = "TPIRRatePercent"
_TnNetworkQueuePIR_Object = MibTableColumn
tnNetworkQueuePIR = _TnNetworkQueuePIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 12),
    _TnNetworkQueuePIR_Type()
)
tnNetworkQueuePIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePIR.setStatus("current")


class _TnNetworkQueueCBS_Type(TBurstHundredthsOfPercent):
    """Custom type tnNetworkQueueCBS based on TBurstHundredthsOfPercent"""
    defaultValue = 100


_TnNetworkQueueCBS_Type.__name__ = "TBurstHundredthsOfPercent"
_TnNetworkQueueCBS_Object = MibTableColumn
tnNetworkQueueCBS = _TnNetworkQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 13),
    _TnNetworkQueueCBS_Type()
)
tnNetworkQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueCBS.setStatus("current")
if mibBuilder.loadTexts:
    tnNetworkQueueCBS.setUnits("Hundredths of a percent")


class _TnNetworkQueueMBS_Type(TBurstHundredthsOfPercent):
    """Custom type tnNetworkQueueMBS based on TBurstHundredthsOfPercent"""
    defaultValue = 10000


_TnNetworkQueueMBS_Type.__name__ = "TBurstHundredthsOfPercent"
_TnNetworkQueueMBS_Object = MibTableColumn
tnNetworkQueueMBS = _TnNetworkQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 14),
    _TnNetworkQueueMBS_Type()
)
tnNetworkQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueMBS.setStatus("current")
if mibBuilder.loadTexts:
    tnNetworkQueueMBS.setUnits("Hundredths of a percent")


class _TnNetworkQueueHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tnNetworkQueueHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TnNetworkQueueHiPrioOnly_Type.__name__ = "TBurstPercentOrDefault"
_TnNetworkQueueHiPrioOnly_Object = MibTableColumn
tnNetworkQueueHiPrioOnly = _TnNetworkQueueHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 15),
    _TnNetworkQueueHiPrioOnly_Type()
)
tnNetworkQueueHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueHiPrioOnly.setStatus("current")
_TnNetworkQueueLastChanged_Type = TimeStamp
_TnNetworkQueueLastChanged_Object = MibTableColumn
tnNetworkQueueLastChanged = _TnNetworkQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 16),
    _TnNetworkQueueLastChanged_Type()
)
tnNetworkQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkQueueLastChanged.setStatus("current")


class _TnNetworkQueueUsePortParent_Type(TruthValue):
    """Custom type tnNetworkQueueUsePortParent based on TruthValue"""
    defaultValue = 2


_TnNetworkQueueUsePortParent_Type.__name__ = "TruthValue"
_TnNetworkQueueUsePortParent_Object = MibTableColumn
tnNetworkQueueUsePortParent = _TnNetworkQueueUsePortParent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 17),
    _TnNetworkQueueUsePortParent_Type()
)
tnNetworkQueueUsePortParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueUsePortParent.setStatus("current")


class _TnNetworkQueuePortLvl_Type(TLevel):
    """Custom type tnNetworkQueuePortLvl based on TLevel"""
    defaultValue = 1


_TnNetworkQueuePortLvl_Type.__name__ = "TLevel"
_TnNetworkQueuePortLvl_Object = MibTableColumn
tnNetworkQueuePortLvl = _TnNetworkQueuePortLvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 18),
    _TnNetworkQueuePortLvl_Type()
)
tnNetworkQueuePortLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePortLvl.setStatus("current")


class _TnNetworkQueuePortWght_Type(TWeight):
    """Custom type tnNetworkQueuePortWght based on TWeight"""
    defaultValue = 1


_TnNetworkQueuePortWght_Type.__name__ = "TWeight"
_TnNetworkQueuePortWght_Object = MibTableColumn
tnNetworkQueuePortWght = _TnNetworkQueuePortWght_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 19),
    _TnNetworkQueuePortWght_Type()
)
tnNetworkQueuePortWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePortWght.setStatus("current")


class _TnNetworkQueuePortCIRLvl_Type(TLevelOrDefault):
    """Custom type tnNetworkQueuePortCIRLvl based on TLevelOrDefault"""
    defaultValue = 0


_TnNetworkQueuePortCIRLvl_Type.__name__ = "TLevelOrDefault"
_TnNetworkQueuePortCIRLvl_Object = MibTableColumn
tnNetworkQueuePortCIRLvl = _TnNetworkQueuePortCIRLvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 20),
    _TnNetworkQueuePortCIRLvl_Type()
)
tnNetworkQueuePortCIRLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePortCIRLvl.setStatus("current")


class _TnNetworkQueuePortCIRWght_Type(TWeight):
    """Custom type tnNetworkQueuePortCIRWght based on TWeight"""
    defaultValue = 0


_TnNetworkQueuePortCIRWght_Type.__name__ = "TWeight"
_TnNetworkQueuePortCIRWght_Object = MibTableColumn
tnNetworkQueuePortCIRWght = _TnNetworkQueuePortCIRWght_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 21),
    _TnNetworkQueuePortCIRWght_Type()
)
tnNetworkQueuePortCIRWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePortCIRWght.setStatus("current")


class _TnNetworkQueuePortAvgOverhead_Type(Unsigned32):
    """Custom type tnNetworkQueuePortAvgOverhead based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnNetworkQueuePortAvgOverhead_Type.__name__ = "Unsigned32"
_TnNetworkQueuePortAvgOverhead_Object = MibTableColumn
tnNetworkQueuePortAvgOverhead = _TnNetworkQueuePortAvgOverhead_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 22),
    _TnNetworkQueuePortAvgOverhead_Type()
)
tnNetworkQueuePortAvgOverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePortAvgOverhead.setStatus("current")
if mibBuilder.loadTexts:
    tnNetworkQueuePortAvgOverhead.setUnits("Hundredths of a percent")


class _TnNetworkQueueCIRAdaptation_Type(TAdaptationRule):
    """Custom type tnNetworkQueueCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TnNetworkQueueCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TnNetworkQueueCIRAdaptation_Object = MibTableColumn
tnNetworkQueueCIRAdaptation = _TnNetworkQueueCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 23),
    _TnNetworkQueueCIRAdaptation_Type()
)
tnNetworkQueueCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueueCIRAdaptation.setStatus("current")


class _TnNetworkQueuePIRAdaptation_Type(TAdaptationRule):
    """Custom type tnNetworkQueuePIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TnNetworkQueuePIRAdaptation_Type.__name__ = "TAdaptationRule"
_TnNetworkQueuePIRAdaptation_Object = MibTableColumn
tnNetworkQueuePIRAdaptation = _TnNetworkQueuePIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 6, 2, 1, 24),
    _TnNetworkQueuePIRAdaptation_Type()
)
tnNetworkQueuePIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePIRAdaptation.setStatus("current")
_TnSlopeObjects_ObjectIdentity = ObjectIdentity
tnSlopeObjects = _TnSlopeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10)
)
_TnSlopePolicyTable_Object = MibTable
tnSlopePolicyTable = _TnSlopePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1)
)
if mibBuilder.loadTexts:
    tnSlopePolicyTable.setStatus("current")
_TnSlopePolicyEntry_Object = MibTableRow
tnSlopePolicyEntry = _TnSlopePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1)
)
tnSlopePolicyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnSlopePolicy"),
)
if mibBuilder.loadTexts:
    tnSlopePolicyEntry.setStatus("current")
_TnSlopePolicy_Type = TNamedItem
_TnSlopePolicy_Object = MibTableColumn
tnSlopePolicy = _TnSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 1),
    _TnSlopePolicy_Type()
)
tnSlopePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSlopePolicy.setStatus("current")
_TnSlopeRowStatus_Type = RowStatus
_TnSlopeRowStatus_Object = MibTableColumn
tnSlopeRowStatus = _TnSlopeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 2),
    _TnSlopeRowStatus_Type()
)
tnSlopeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeRowStatus.setStatus("current")


class _TnSlopeDescription_Type(TItemDescription):
    """Custom type tnSlopeDescription based on TItemDescription"""
    defaultHexValue = ""


_TnSlopeDescription_Type.__name__ = "TItemDescription"
_TnSlopeDescription_Object = MibTableColumn
tnSlopeDescription = _TnSlopeDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 3),
    _TnSlopeDescription_Type()
)
tnSlopeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeDescription.setStatus("current")


class _TnSlopeHiAdminStatus_Type(Integer32):
    """Custom type tnSlopeHiAdminStatus based on Integer32"""
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


_TnSlopeHiAdminStatus_Type.__name__ = "Integer32"
_TnSlopeHiAdminStatus_Object = MibTableColumn
tnSlopeHiAdminStatus = _TnSlopeHiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 4),
    _TnSlopeHiAdminStatus_Type()
)
tnSlopeHiAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiAdminStatus.setStatus("current")


class _TnSlopeHiStartAverage_Type(Unsigned32):
    """Custom type tnSlopeHiStartAverage based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopeHiStartAverage_Type.__name__ = "Unsigned32"
_TnSlopeHiStartAverage_Object = MibTableColumn
tnSlopeHiStartAverage = _TnSlopeHiStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 5),
    _TnSlopeHiStartAverage_Type()
)
tnSlopeHiStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiStartAverage.setStatus("current")


class _TnSlopeHiMaxAverage_Type(Unsigned32):
    """Custom type tnSlopeHiMaxAverage based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopeHiMaxAverage_Type.__name__ = "Unsigned32"
_TnSlopeHiMaxAverage_Object = MibTableColumn
tnSlopeHiMaxAverage = _TnSlopeHiMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 6),
    _TnSlopeHiMaxAverage_Type()
)
tnSlopeHiMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiMaxAverage.setStatus("current")


class _TnSlopeHiMaxProbability_Type(Unsigned32):
    """Custom type tnSlopeHiMaxProbability based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopeHiMaxProbability_Type.__name__ = "Unsigned32"
_TnSlopeHiMaxProbability_Object = MibTableColumn
tnSlopeHiMaxProbability = _TnSlopeHiMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 7),
    _TnSlopeHiMaxProbability_Type()
)
tnSlopeHiMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiMaxProbability.setStatus("current")


class _TnSlopeLoAdminStatus_Type(Integer32):
    """Custom type tnSlopeLoAdminStatus based on Integer32"""
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


_TnSlopeLoAdminStatus_Type.__name__ = "Integer32"
_TnSlopeLoAdminStatus_Object = MibTableColumn
tnSlopeLoAdminStatus = _TnSlopeLoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 8),
    _TnSlopeLoAdminStatus_Type()
)
tnSlopeLoAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoAdminStatus.setStatus("current")


class _TnSlopeLoStartAverage_Type(Unsigned32):
    """Custom type tnSlopeLoStartAverage based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopeLoStartAverage_Type.__name__ = "Unsigned32"
_TnSlopeLoStartAverage_Object = MibTableColumn
tnSlopeLoStartAverage = _TnSlopeLoStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 9),
    _TnSlopeLoStartAverage_Type()
)
tnSlopeLoStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoStartAverage.setStatus("current")


class _TnSlopeLoMaxAverage_Type(Unsigned32):
    """Custom type tnSlopeLoMaxAverage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopeLoMaxAverage_Type.__name__ = "Unsigned32"
_TnSlopeLoMaxAverage_Object = MibTableColumn
tnSlopeLoMaxAverage = _TnSlopeLoMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 10),
    _TnSlopeLoMaxAverage_Type()
)
tnSlopeLoMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoMaxAverage.setStatus("current")


class _TnSlopeLoMaxProbability_Type(Unsigned32):
    """Custom type tnSlopeLoMaxProbability based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopeLoMaxProbability_Type.__name__ = "Unsigned32"
_TnSlopeLoMaxProbability_Object = MibTableColumn
tnSlopeLoMaxProbability = _TnSlopeLoMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 11),
    _TnSlopeLoMaxProbability_Type()
)
tnSlopeLoMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoMaxProbability.setStatus("current")


class _TnSlopeTimeAvgFactor_Type(Unsigned32):
    """Custom type tnSlopeTimeAvgFactor based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TnSlopeTimeAvgFactor_Type.__name__ = "Unsigned32"
_TnSlopeTimeAvgFactor_Object = MibTableColumn
tnSlopeTimeAvgFactor = _TnSlopeTimeAvgFactor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 12),
    _TnSlopeTimeAvgFactor_Type()
)
tnSlopeTimeAvgFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeTimeAvgFactor.setStatus("current")
_TnSlopeLastChanged_Type = TimeStamp
_TnSlopeLastChanged_Object = MibTableColumn
tnSlopeLastChanged = _TnSlopeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 10, 1, 1, 13),
    _TnSlopeLastChanged_Type()
)
tnSlopeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlopeLastChanged.setStatus("current")
_TnSchedulerObjects_ObjectIdentity = ObjectIdentity
tnSchedulerObjects = _TnSchedulerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12)
)
_TnPortSchedulerPlcyTable_Object = MibTable
tnPortSchedulerPlcyTable = _TnPortSchedulerPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3)
)
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyTable.setStatus("current")
_TnPortSchedulerPlcyEntry_Object = MibTableRow
tnPortSchedulerPlcyEntry = _TnPortSchedulerPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1)
)
tnPortSchedulerPlcyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (1, "TN-QOS-MIB", "tnPortSchedulerPlcyName"),
)
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyEntry.setStatus("current")
_TnPortSchedulerPlcyName_Type = TNamedItem
_TnPortSchedulerPlcyName_Object = MibTableColumn
tnPortSchedulerPlcyName = _TnPortSchedulerPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 1),
    _TnPortSchedulerPlcyName_Type()
)
tnPortSchedulerPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyName.setStatus("current")
_TnPortSchedulerPlcyRowStatus_Type = RowStatus
_TnPortSchedulerPlcyRowStatus_Object = MibTableColumn
tnPortSchedulerPlcyRowStatus = _TnPortSchedulerPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 2),
    _TnPortSchedulerPlcyRowStatus_Type()
)
tnPortSchedulerPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyRowStatus.setStatus("current")


class _TnPortSchedulerPlcyDescription_Type(TItemDescription):
    """Custom type tnPortSchedulerPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TnPortSchedulerPlcyDescription_Type.__name__ = "TItemDescription"
_TnPortSchedulerPlcyDescription_Object = MibTableColumn
tnPortSchedulerPlcyDescription = _TnPortSchedulerPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 3),
    _TnPortSchedulerPlcyDescription_Type()
)
tnPortSchedulerPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyDescription.setStatus("current")
_TnPortSchedulerPlcyLastChanged_Type = TimeStamp
_TnPortSchedulerPlcyLastChanged_Object = MibTableColumn
tnPortSchedulerPlcyLastChanged = _TnPortSchedulerPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 4),
    _TnPortSchedulerPlcyLastChanged_Type()
)
tnPortSchedulerPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLastChanged.setStatus("current")


class _TnPortSchedulerPlcyMaxRate_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyMaxRate based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyMaxRate_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyMaxRate_Object = MibTableColumn
tnPortSchedulerPlcyMaxRate = _TnPortSchedulerPlcyMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 5),
    _TnPortSchedulerPlcyMaxRate_Type()
)
tnPortSchedulerPlcyMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyMaxRate.setUnits("kbps")


class _TnPortSchedulerPlcyLvl1PIR_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyLvl1PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl1PIR_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyLvl1PIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl1PIR = _TnPortSchedulerPlcyLvl1PIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 6),
    _TnPortSchedulerPlcyLvl1PIR_Type()
)
tnPortSchedulerPlcyLvl1PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl1PIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl1PIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl1CIR_Type(TPortSchedulerCIR):
    """Custom type tnPortSchedulerPlcyLvl1CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl1CIR_Type.__name__ = "TPortSchedulerCIR"
_TnPortSchedulerPlcyLvl1CIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl1CIR = _TnPortSchedulerPlcyLvl1CIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 7),
    _TnPortSchedulerPlcyLvl1CIR_Type()
)
tnPortSchedulerPlcyLvl1CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl1CIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl1CIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl2PIR_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyLvl2PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl2PIR_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyLvl2PIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl2PIR = _TnPortSchedulerPlcyLvl2PIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 8),
    _TnPortSchedulerPlcyLvl2PIR_Type()
)
tnPortSchedulerPlcyLvl2PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl2PIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl2PIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl2CIR_Type(TPortSchedulerCIR):
    """Custom type tnPortSchedulerPlcyLvl2CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl2CIR_Type.__name__ = "TPortSchedulerCIR"
_TnPortSchedulerPlcyLvl2CIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl2CIR = _TnPortSchedulerPlcyLvl2CIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 9),
    _TnPortSchedulerPlcyLvl2CIR_Type()
)
tnPortSchedulerPlcyLvl2CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl2CIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl2CIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl3PIR_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyLvl3PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl3PIR_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyLvl3PIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl3PIR = _TnPortSchedulerPlcyLvl3PIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 10),
    _TnPortSchedulerPlcyLvl3PIR_Type()
)
tnPortSchedulerPlcyLvl3PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl3PIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl3PIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl3CIR_Type(TPortSchedulerCIR):
    """Custom type tnPortSchedulerPlcyLvl3CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl3CIR_Type.__name__ = "TPortSchedulerCIR"
_TnPortSchedulerPlcyLvl3CIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl3CIR = _TnPortSchedulerPlcyLvl3CIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 11),
    _TnPortSchedulerPlcyLvl3CIR_Type()
)
tnPortSchedulerPlcyLvl3CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl3CIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl3CIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl4PIR_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyLvl4PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl4PIR_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyLvl4PIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl4PIR = _TnPortSchedulerPlcyLvl4PIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 12),
    _TnPortSchedulerPlcyLvl4PIR_Type()
)
tnPortSchedulerPlcyLvl4PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl4PIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl4PIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl4CIR_Type(TPortSchedulerCIR):
    """Custom type tnPortSchedulerPlcyLvl4CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl4CIR_Type.__name__ = "TPortSchedulerCIR"
_TnPortSchedulerPlcyLvl4CIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl4CIR = _TnPortSchedulerPlcyLvl4CIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 13),
    _TnPortSchedulerPlcyLvl4CIR_Type()
)
tnPortSchedulerPlcyLvl4CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl4CIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl4CIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl5PIR_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyLvl5PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl5PIR_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyLvl5PIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl5PIR = _TnPortSchedulerPlcyLvl5PIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 14),
    _TnPortSchedulerPlcyLvl5PIR_Type()
)
tnPortSchedulerPlcyLvl5PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl5PIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl5PIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl5CIR_Type(TPortSchedulerCIR):
    """Custom type tnPortSchedulerPlcyLvl5CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl5CIR_Type.__name__ = "TPortSchedulerCIR"
_TnPortSchedulerPlcyLvl5CIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl5CIR = _TnPortSchedulerPlcyLvl5CIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 15),
    _TnPortSchedulerPlcyLvl5CIR_Type()
)
tnPortSchedulerPlcyLvl5CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl5CIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl5CIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl6PIR_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyLvl6PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl6PIR_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyLvl6PIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl6PIR = _TnPortSchedulerPlcyLvl6PIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 16),
    _TnPortSchedulerPlcyLvl6PIR_Type()
)
tnPortSchedulerPlcyLvl6PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl6PIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl6PIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl6CIR_Type(TPortSchedulerCIR):
    """Custom type tnPortSchedulerPlcyLvl6CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl6CIR_Type.__name__ = "TPortSchedulerCIR"
_TnPortSchedulerPlcyLvl6CIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl6CIR = _TnPortSchedulerPlcyLvl6CIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 17),
    _TnPortSchedulerPlcyLvl6CIR_Type()
)
tnPortSchedulerPlcyLvl6CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl6CIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl6CIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl7PIR_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyLvl7PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl7PIR_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyLvl7PIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl7PIR = _TnPortSchedulerPlcyLvl7PIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 18),
    _TnPortSchedulerPlcyLvl7PIR_Type()
)
tnPortSchedulerPlcyLvl7PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl7PIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl7PIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl7CIR_Type(TPortSchedulerCIR):
    """Custom type tnPortSchedulerPlcyLvl7CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl7CIR_Type.__name__ = "TPortSchedulerCIR"
_TnPortSchedulerPlcyLvl7CIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl7CIR = _TnPortSchedulerPlcyLvl7CIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 19),
    _TnPortSchedulerPlcyLvl7CIR_Type()
)
tnPortSchedulerPlcyLvl7CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl7CIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl7CIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl8PIR_Type(TPortSchedulerPIR):
    """Custom type tnPortSchedulerPlcyLvl8PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl8PIR_Type.__name__ = "TPortSchedulerPIR"
_TnPortSchedulerPlcyLvl8PIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl8PIR = _TnPortSchedulerPlcyLvl8PIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 20),
    _TnPortSchedulerPlcyLvl8PIR_Type()
)
tnPortSchedulerPlcyLvl8PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl8PIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl8PIR.setUnits("kbps")


class _TnPortSchedulerPlcyLvl8CIR_Type(TPortSchedulerCIR):
    """Custom type tnPortSchedulerPlcyLvl8CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TnPortSchedulerPlcyLvl8CIR_Type.__name__ = "TPortSchedulerCIR"
_TnPortSchedulerPlcyLvl8CIR_Object = MibTableColumn
tnPortSchedulerPlcyLvl8CIR = _TnPortSchedulerPlcyLvl8CIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 21),
    _TnPortSchedulerPlcyLvl8CIR_Type()
)
tnPortSchedulerPlcyLvl8CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl8CIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyLvl8CIR.setUnits("kbps")


class _TnPortSchedulerPlcyOrphanLvl_Type(TLevel):
    """Custom type tnPortSchedulerPlcyOrphanLvl based on TLevel"""
    defaultValue = 1


_TnPortSchedulerPlcyOrphanLvl_Type.__name__ = "TLevel"
_TnPortSchedulerPlcyOrphanLvl_Object = MibTableColumn
tnPortSchedulerPlcyOrphanLvl = _TnPortSchedulerPlcyOrphanLvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 22),
    _TnPortSchedulerPlcyOrphanLvl_Type()
)
tnPortSchedulerPlcyOrphanLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyOrphanLvl.setStatus("current")


class _TnPortSchedulerPlcyOrphanWeight_Type(TWeight):
    """Custom type tnPortSchedulerPlcyOrphanWeight based on TWeight"""
    defaultValue = 0


_TnPortSchedulerPlcyOrphanWeight_Type.__name__ = "TWeight"
_TnPortSchedulerPlcyOrphanWeight_Object = MibTableColumn
tnPortSchedulerPlcyOrphanWeight = _TnPortSchedulerPlcyOrphanWeight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 23),
    _TnPortSchedulerPlcyOrphanWeight_Type()
)
tnPortSchedulerPlcyOrphanWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyOrphanWeight.setStatus("current")


class _TnPortSchedulerPlcyOrphanCIRLvl_Type(TLevelOrDefault):
    """Custom type tnPortSchedulerPlcyOrphanCIRLvl based on TLevelOrDefault"""
    defaultValue = 0


_TnPortSchedulerPlcyOrphanCIRLvl_Type.__name__ = "TLevelOrDefault"
_TnPortSchedulerPlcyOrphanCIRLvl_Object = MibTableColumn
tnPortSchedulerPlcyOrphanCIRLvl = _TnPortSchedulerPlcyOrphanCIRLvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 24),
    _TnPortSchedulerPlcyOrphanCIRLvl_Type()
)
tnPortSchedulerPlcyOrphanCIRLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyOrphanCIRLvl.setStatus("current")


class _TnPortSchedulerPlcyOrphanCIRWght_Type(TWeight):
    """Custom type tnPortSchedulerPlcyOrphanCIRWght based on TWeight"""
    defaultValue = 0


_TnPortSchedulerPlcyOrphanCIRWght_Type.__name__ = "TWeight"
_TnPortSchedulerPlcyOrphanCIRWght_Object = MibTableColumn
tnPortSchedulerPlcyOrphanCIRWght = _TnPortSchedulerPlcyOrphanCIRWght_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 3, 1, 25),
    _TnPortSchedulerPlcyOrphanCIRWght_Type()
)
tnPortSchedulerPlcyOrphanCIRWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyOrphanCIRWght.setStatus("current")
_TnSchedulerScalar1_Type = Unsigned32
_TnSchedulerScalar1_Object = MibScalar
tnSchedulerScalar1 = _TnSchedulerScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 101),
    _TnSchedulerScalar1_Type()
)
tnSchedulerScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSchedulerScalar1.setStatus("current")
_TnSchedulerScalar2_Type = Unsigned32
_TnSchedulerScalar2_Object = MibScalar
tnSchedulerScalar2 = _TnSchedulerScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 16, 12, 102),
    _TnSchedulerScalar2_Type()
)
tnSchedulerScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSchedulerScalar2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-QOS-MIB",
    **{"TmnxMcFrClassIndex": TmnxMcFrClassIndex,
       "tnQosMIBModule": tnQosMIBModule,
       "tnQosObjects": tnQosObjects,
       "tnSapIngressObjects": tnSapIngressObjects,
       "tnSapIngressTable": tnSapIngressTable,
       "tnSapIngressEntry": tnSapIngressEntry,
       "tnSapIngressIndex": tnSapIngressIndex,
       "tnSapIngressRowStatus": tnSapIngressRowStatus,
       "tnSapIngressScope": tnSapIngressScope,
       "tnSapIngressDescription": tnSapIngressDescription,
       "tnSapIngressDefaultFC": tnSapIngressDefaultFC,
       "tnSapIngressDefaultFCPriority": tnSapIngressDefaultFCPriority,
       "tnSapIngressMatchCriteria": tnSapIngressMatchCriteria,
       "tnSapIngressLastChanged": tnSapIngressLastChanged,
       "tnSapIngressHsmdaPacketOffset": tnSapIngressHsmdaPacketOffset,
       "tnSapIngressDefFCHsmdaCntrOvr": tnSapIngressDefFCHsmdaCntrOvr,
       "tnSapIngressMacCritType": tnSapIngressMacCritType,
       "tnSapIngressPolicyName": tnSapIngressPolicyName,
       "tnSapIngressIPCriteriaTable": tnSapIngressIPCriteriaTable,
       "tnSapIngressIPCriteriaEntry": tnSapIngressIPCriteriaEntry,
       "tnSapIngressIPCriteriaIndex": tnSapIngressIPCriteriaIndex,
       "tnSapIngressIPCriteriaRowStatus": tnSapIngressIPCriteriaRowStatus,
       "tnSapIngressIPCriteriaDescription": tnSapIngressIPCriteriaDescription,
       "tnSapIngressIPCriteriaActionFC": tnSapIngressIPCriteriaActionFC,
       "tnSapIngressIPCriteriaActionPriority": tnSapIngressIPCriteriaActionPriority,
       "tnSapIngressIPCriteriaSourceIpAddr": tnSapIngressIPCriteriaSourceIpAddr,
       "tnSapIngressIPCriteriaSourceIpMask": tnSapIngressIPCriteriaSourceIpMask,
       "tnSapIngressIPCriteriaDestIpAddr": tnSapIngressIPCriteriaDestIpAddr,
       "tnSapIngressIPCriteriaDestIpMask": tnSapIngressIPCriteriaDestIpMask,
       "tnSapIngressIPCriteriaProtocol": tnSapIngressIPCriteriaProtocol,
       "tnSapIngressIPCriteriaSourcePortValue1": tnSapIngressIPCriteriaSourcePortValue1,
       "tnSapIngressIPCriteriaSourcePortValue2": tnSapIngressIPCriteriaSourcePortValue2,
       "tnSapIngressIPCriteriaSourcePortOperator": tnSapIngressIPCriteriaSourcePortOperator,
       "tnSapIngressIPCriteriaDestPortValue1": tnSapIngressIPCriteriaDestPortValue1,
       "tnSapIngressIPCriteriaDestPortValue2": tnSapIngressIPCriteriaDestPortValue2,
       "tnSapIngressIPCriteriaDestPortOperator": tnSapIngressIPCriteriaDestPortOperator,
       "tnSapIngressIPCriteriaDSCP": tnSapIngressIPCriteriaDSCP,
       "tnSapIngressIPCriteriaFragment": tnSapIngressIPCriteriaFragment,
       "tnSapIngressIPCriteriaLastChanged": tnSapIngressIPCriteriaLastChanged,
       "tnSapIngressIPCritHsmdaCntrOvr": tnSapIngressIPCritHsmdaCntrOvr,
       "tnSapIngressMacCriteriaTable": tnSapIngressMacCriteriaTable,
       "tnSapIngressMacCriteriaEntry": tnSapIngressMacCriteriaEntry,
       "tnSapIngressMacCriteriaIndex": tnSapIngressMacCriteriaIndex,
       "tnSapIngressMacCriteriaRowStatus": tnSapIngressMacCriteriaRowStatus,
       "tnSapIngressMacCriteriaDescription": tnSapIngressMacCriteriaDescription,
       "tnSapIngressMacCriteriaActionFC": tnSapIngressMacCriteriaActionFC,
       "tnSapIngressMacCriteriaActionPriority": tnSapIngressMacCriteriaActionPriority,
       "tnSapIngressMacCriteriaFrameType": tnSapIngressMacCriteriaFrameType,
       "tnSapIngressMacCriteriaSrcMacAddr": tnSapIngressMacCriteriaSrcMacAddr,
       "tnSapIngressMacCriteriaSrcMacMask": tnSapIngressMacCriteriaSrcMacMask,
       "tnSapIngressMacCriteriaDstMacAddr": tnSapIngressMacCriteriaDstMacAddr,
       "tnSapIngressMacCriteriaDstMacMask": tnSapIngressMacCriteriaDstMacMask,
       "tnSapIngressMacCriteriaDot1PValue": tnSapIngressMacCriteriaDot1PValue,
       "tnSapIngressMacCriteriaDot1PMask": tnSapIngressMacCriteriaDot1PMask,
       "tnSapIngressMacCriteriaEthernetType": tnSapIngressMacCriteriaEthernetType,
       "tnSapIngressMacCriteriaDSAP": tnSapIngressMacCriteriaDSAP,
       "tnSapIngressMacCriteriaDSAPMask": tnSapIngressMacCriteriaDSAPMask,
       "tnSapIngressMacCriteriaSSAP": tnSapIngressMacCriteriaSSAP,
       "tnSapIngressMacCriteriaSSAPMask": tnSapIngressMacCriteriaSSAPMask,
       "tnSapIngressMacCriteriaSnapPid": tnSapIngressMacCriteriaSnapPid,
       "tnSapIngressMacCriteriaSnapOui": tnSapIngressMacCriteriaSnapOui,
       "tnSapIngressMacCriteriaLastChanged": tnSapIngressMacCriteriaLastChanged,
       "tnSapIngressFCTable": tnSapIngressFCTable,
       "tnSapIngressFCEntry": tnSapIngressFCEntry,
       "tnSapIngressFCName": tnSapIngressFCName,
       "tnSapIngressFCRowStatus": tnSapIngressFCRowStatus,
       "tnSapIngressFCQueue": tnSapIngressFCQueue,
       "tnSapIngressFCMCastQueue": tnSapIngressFCMCastQueue,
       "tnSapIngressFCBCastQueue": tnSapIngressFCBCastQueue,
       "tnSapIngressFCUnknownQueue": tnSapIngressFCUnknownQueue,
       "tnSapIngressFCLastChanged": tnSapIngressFCLastChanged,
       "tnSapIngressFCInProfRemark": tnSapIngressFCInProfRemark,
       "tnSapIngressFCInProfDscp": tnSapIngressFCInProfDscp,
       "tnSapIngressFCInProfPrec": tnSapIngressFCInProfPrec,
       "tnSapIngressFCOutProfRemark": tnSapIngressFCOutProfRemark,
       "tnSapIngressFCOutProfDscp": tnSapIngressFCOutProfDscp,
       "tnSapIngressFCOutProfPrec": tnSapIngressFCOutProfPrec,
       "tnSapIngressFCProfile": tnSapIngressFCProfile,
       "tnSapIngressFCHsmdaQueue": tnSapIngressFCHsmdaQueue,
       "tnSapIngressFCHsmdaMCastQueue": tnSapIngressFCHsmdaMCastQueue,
       "tnSapIngressFCHsmdaBCastQueue": tnSapIngressFCHsmdaBCastQueue,
       "tnSapIngressFCDE1OutOfProfile": tnSapIngressFCDE1OutOfProfile,
       "tnSapIngressFCQGrp": tnSapIngressFCQGrp,
       "tnSapIngressFCQGrpMCast": tnSapIngressFCQGrpMCast,
       "tnSapIngressFCQGrpBCast": tnSapIngressFCQGrpBCast,
       "tnSapIngressFCQGrpUnknown": tnSapIngressFCQGrpUnknown,
       "tnSapIngressIPv6CriteriaTable": tnSapIngressIPv6CriteriaTable,
       "tnSapIngressIPv6CriteriaEntry": tnSapIngressIPv6CriteriaEntry,
       "tnSapIngressIPv6CriteriaIndex": tnSapIngressIPv6CriteriaIndex,
       "tnSapIngressIPv6CriteriaRowStatus": tnSapIngressIPv6CriteriaRowStatus,
       "tnSapIngressIPv6CriteriaDescription": tnSapIngressIPv6CriteriaDescription,
       "tnSapIngressIPv6CriteriaActionFC": tnSapIngressIPv6CriteriaActionFC,
       "tnSapIngressIPv6CriteriaActionPriority": tnSapIngressIPv6CriteriaActionPriority,
       "tnSapIngressIPv6CriteriaSourceIpAddr": tnSapIngressIPv6CriteriaSourceIpAddr,
       "tnSapIngressIPv6CriteriaSourceIpMask": tnSapIngressIPv6CriteriaSourceIpMask,
       "tnSapIngressIPv6CriteriaDestIpAddr": tnSapIngressIPv6CriteriaDestIpAddr,
       "tnSapIngressIPv6CriteriaDestIpMask": tnSapIngressIPv6CriteriaDestIpMask,
       "tnSapIngressIPv6CriteriaNextHeader": tnSapIngressIPv6CriteriaNextHeader,
       "tnSapIngressIPv6CriteriaSourcePortValue1": tnSapIngressIPv6CriteriaSourcePortValue1,
       "tnSapIngressIPv6CriteriaSourcePortValue2": tnSapIngressIPv6CriteriaSourcePortValue2,
       "tnSapIngressIPv6CriteriaSourcePortOperator": tnSapIngressIPv6CriteriaSourcePortOperator,
       "tnSapIngressIPv6CriteriaDestPortValue1": tnSapIngressIPv6CriteriaDestPortValue1,
       "tnSapIngressIPv6CriteriaDestPortValue2": tnSapIngressIPv6CriteriaDestPortValue2,
       "tnSapIngressIPv6CriteriaDestPortOperator": tnSapIngressIPv6CriteriaDestPortOperator,
       "tnSapIngressIPv6CriteriaDSCP": tnSapIngressIPv6CriteriaDSCP,
       "tnSapIngressIPv6CriteriaLastChanged": tnSapIngressIPv6CriteriaLastChanged,
       "tnSapIngressScalar1": tnSapIngressScalar1,
       "tnSapIngressScalar2": tnSapIngressScalar2,
       "tnNetworkObjects": tnNetworkObjects,
       "tnNetworkPolicyTable": tnNetworkPolicyTable,
       "tnNetworkPolicyEntry": tnNetworkPolicyEntry,
       "tnNetworkPolicyIndex": tnNetworkPolicyIndex,
       "tnNetworkPolicyRowStatus": tnNetworkPolicyRowStatus,
       "tnNetworkPolicyScope": tnNetworkPolicyScope,
       "tnNetworkPolicyDescription": tnNetworkPolicyDescription,
       "tnNetworkPolicyIngressDefaultActionFC": tnNetworkPolicyIngressDefaultActionFC,
       "tnNetworkPolicyIngressDefaultActionProfile": tnNetworkPolicyIngressDefaultActionProfile,
       "tnNetworkPolicyEgressRemark": tnNetworkPolicyEgressRemark,
       "tnNetworkPolicyLastChanged": tnNetworkPolicyLastChanged,
       "tnNetworkPolicyIngressLerUseDscp": tnNetworkPolicyIngressLerUseDscp,
       "tnNetworkPolicyEgressRemarkDscp": tnNetworkPolicyEgressRemarkDscp,
       "tnNetworkIngressDot1pTable": tnNetworkIngressDot1pTable,
       "tnNetworkIngressDot1pEntry": tnNetworkIngressDot1pEntry,
       "tnNetworkIngressDot1pValue": tnNetworkIngressDot1pValue,
       "tnNetworkIngressDot1pRowStatus": tnNetworkIngressDot1pRowStatus,
       "tnNetworkIngressDot1pFC": tnNetworkIngressDot1pFC,
       "tnNetworkIngressDot1pProfile": tnNetworkIngressDot1pProfile,
       "tnNetworkIngressDot1pLastChanged": tnNetworkIngressDot1pLastChanged,
       "tnNetworkEgressFCTable": tnNetworkEgressFCTable,
       "tnNetworkEgressFCEntry": tnNetworkEgressFCEntry,
       "tnNetworkEgressFCName": tnNetworkEgressFCName,
       "tnNetworkEgressFCDSCPInProfile": tnNetworkEgressFCDSCPInProfile,
       "tnNetworkEgressFCDSCPOutProfile": tnNetworkEgressFCDSCPOutProfile,
       "tnNetworkEgressFCLspExpInProfile": tnNetworkEgressFCLspExpInProfile,
       "tnNetworkEgressFCLspExpOutProfile": tnNetworkEgressFCLspExpOutProfile,
       "tnNetworkEgressFCDot1pInProfile": tnNetworkEgressFCDot1pInProfile,
       "tnNetworkEgressFCDot1pOutProfile": tnNetworkEgressFCDot1pOutProfile,
       "tnNetworkEgressFCLastChanged": tnNetworkEgressFCLastChanged,
       "tnNetworkEgressFCForceDEValue": tnNetworkEgressFCForceDEValue,
       "tnNetworkEgressFCDEMark": tnNetworkEgressFCDEMark,
       "tnNetworkEgressFCQGrpQueue": tnNetworkEgressFCQGrpQueue,
       "tnNetworkScalar1": tnNetworkScalar1,
       "tnNetworkScalar2": tnNetworkScalar2,
       "tnNetworkQueueObjects": tnNetworkQueueObjects,
       "tnNetworkQueuePolicyTable": tnNetworkQueuePolicyTable,
       "tnNetworkQueuePolicyEntry": tnNetworkQueuePolicyEntry,
       "tnNetworkQueuePolicy": tnNetworkQueuePolicy,
       "tnNetworkQueuePolicyRowStatus": tnNetworkQueuePolicyRowStatus,
       "tnNetworkQueuePolicyDescription": tnNetworkQueuePolicyDescription,
       "tnNetworkQueuePolicyLastChanged": tnNetworkQueuePolicyLastChanged,
       "tnNetworkQueueTable": tnNetworkQueueTable,
       "tnNetworkQueueEntry": tnNetworkQueueEntry,
       "tnNetworkQueue": tnNetworkQueue,
       "tnNetworkQueueRowStatus": tnNetworkQueueRowStatus,
       "tnNetworkQueuePoolName": tnNetworkQueuePoolName,
       "tnNetworkQueueParent": tnNetworkQueueParent,
       "tnNetworkQueueLevel": tnNetworkQueueLevel,
       "tnNetworkQueueWeight": tnNetworkQueueWeight,
       "tnNetworkQueueCIRLevel": tnNetworkQueueCIRLevel,
       "tnNetworkQueueCIRWeight": tnNetworkQueueCIRWeight,
       "tnNetworkQueueMCast": tnNetworkQueueMCast,
       "tnNetworkQueueExpedite": tnNetworkQueueExpedite,
       "tnNetworkQueueCIR": tnNetworkQueueCIR,
       "tnNetworkQueuePIR": tnNetworkQueuePIR,
       "tnNetworkQueueCBS": tnNetworkQueueCBS,
       "tnNetworkQueueMBS": tnNetworkQueueMBS,
       "tnNetworkQueueHiPrioOnly": tnNetworkQueueHiPrioOnly,
       "tnNetworkQueueLastChanged": tnNetworkQueueLastChanged,
       "tnNetworkQueueUsePortParent": tnNetworkQueueUsePortParent,
       "tnNetworkQueuePortLvl": tnNetworkQueuePortLvl,
       "tnNetworkQueuePortWght": tnNetworkQueuePortWght,
       "tnNetworkQueuePortCIRLvl": tnNetworkQueuePortCIRLvl,
       "tnNetworkQueuePortCIRWght": tnNetworkQueuePortCIRWght,
       "tnNetworkQueuePortAvgOverhead": tnNetworkQueuePortAvgOverhead,
       "tnNetworkQueueCIRAdaptation": tnNetworkQueueCIRAdaptation,
       "tnNetworkQueuePIRAdaptation": tnNetworkQueuePIRAdaptation,
       "tnSlopeObjects": tnSlopeObjects,
       "tnSlopePolicyTable": tnSlopePolicyTable,
       "tnSlopePolicyEntry": tnSlopePolicyEntry,
       "tnSlopePolicy": tnSlopePolicy,
       "tnSlopeRowStatus": tnSlopeRowStatus,
       "tnSlopeDescription": tnSlopeDescription,
       "tnSlopeHiAdminStatus": tnSlopeHiAdminStatus,
       "tnSlopeHiStartAverage": tnSlopeHiStartAverage,
       "tnSlopeHiMaxAverage": tnSlopeHiMaxAverage,
       "tnSlopeHiMaxProbability": tnSlopeHiMaxProbability,
       "tnSlopeLoAdminStatus": tnSlopeLoAdminStatus,
       "tnSlopeLoStartAverage": tnSlopeLoStartAverage,
       "tnSlopeLoMaxAverage": tnSlopeLoMaxAverage,
       "tnSlopeLoMaxProbability": tnSlopeLoMaxProbability,
       "tnSlopeTimeAvgFactor": tnSlopeTimeAvgFactor,
       "tnSlopeLastChanged": tnSlopeLastChanged,
       "tnSchedulerObjects": tnSchedulerObjects,
       "tnPortSchedulerPlcyTable": tnPortSchedulerPlcyTable,
       "tnPortSchedulerPlcyEntry": tnPortSchedulerPlcyEntry,
       "tnPortSchedulerPlcyName": tnPortSchedulerPlcyName,
       "tnPortSchedulerPlcyRowStatus": tnPortSchedulerPlcyRowStatus,
       "tnPortSchedulerPlcyDescription": tnPortSchedulerPlcyDescription,
       "tnPortSchedulerPlcyLastChanged": tnPortSchedulerPlcyLastChanged,
       "tnPortSchedulerPlcyMaxRate": tnPortSchedulerPlcyMaxRate,
       "tnPortSchedulerPlcyLvl1PIR": tnPortSchedulerPlcyLvl1PIR,
       "tnPortSchedulerPlcyLvl1CIR": tnPortSchedulerPlcyLvl1CIR,
       "tnPortSchedulerPlcyLvl2PIR": tnPortSchedulerPlcyLvl2PIR,
       "tnPortSchedulerPlcyLvl2CIR": tnPortSchedulerPlcyLvl2CIR,
       "tnPortSchedulerPlcyLvl3PIR": tnPortSchedulerPlcyLvl3PIR,
       "tnPortSchedulerPlcyLvl3CIR": tnPortSchedulerPlcyLvl3CIR,
       "tnPortSchedulerPlcyLvl4PIR": tnPortSchedulerPlcyLvl4PIR,
       "tnPortSchedulerPlcyLvl4CIR": tnPortSchedulerPlcyLvl4CIR,
       "tnPortSchedulerPlcyLvl5PIR": tnPortSchedulerPlcyLvl5PIR,
       "tnPortSchedulerPlcyLvl5CIR": tnPortSchedulerPlcyLvl5CIR,
       "tnPortSchedulerPlcyLvl6PIR": tnPortSchedulerPlcyLvl6PIR,
       "tnPortSchedulerPlcyLvl6CIR": tnPortSchedulerPlcyLvl6CIR,
       "tnPortSchedulerPlcyLvl7PIR": tnPortSchedulerPlcyLvl7PIR,
       "tnPortSchedulerPlcyLvl7CIR": tnPortSchedulerPlcyLvl7CIR,
       "tnPortSchedulerPlcyLvl8PIR": tnPortSchedulerPlcyLvl8PIR,
       "tnPortSchedulerPlcyLvl8CIR": tnPortSchedulerPlcyLvl8CIR,
       "tnPortSchedulerPlcyOrphanLvl": tnPortSchedulerPlcyOrphanLvl,
       "tnPortSchedulerPlcyOrphanWeight": tnPortSchedulerPlcyOrphanWeight,
       "tnPortSchedulerPlcyOrphanCIRLvl": tnPortSchedulerPlcyOrphanCIRLvl,
       "tnPortSchedulerPlcyOrphanCIRWght": tnPortSchedulerPlcyOrphanCIRWght,
       "tnSchedulerScalar1": tnSchedulerScalar1,
       "tnSchedulerScalar2": tnSchedulerScalar2}
)
