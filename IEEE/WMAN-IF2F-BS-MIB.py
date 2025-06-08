# SNMP MIB module (WMAN-IF2F-BS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-IF2F-BS-MIB.mib
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

(WmanIf2TcActionRule,
 WmanIf2TcArqBlockSize,
 WmanIf2TcCidDescriptor,
 WmanIf2TcCidType,
 WmanIf2TcClassifierMap,
 WmanIf2TcCsType,
 WmanIf2TcEthernetType,
 WmanIf2TcFsnType,
 WmanIf2TcIpTypOfServ,
 WmanIf2TcIpv6FlowLabel,
 WmanIf2TcMbsType,
 WmanIf2TcPhsRuleVerify,
 WmanIf2TcReqTxPolicy,
 WmanIf2TcSchedulingType,
 WmanIf2TcSduType,
 WmanIf2TcSfDirection,
 WmanIf2TcSfState) = mibBuilder.importSymbols(
    "WMAN-IF2-TC-MIB",
    "WmanIf2TcActionRule",
    "WmanIf2TcArqBlockSize",
    "WmanIf2TcCidDescriptor",
    "WmanIf2TcCidType",
    "WmanIf2TcClassifierMap",
    "WmanIf2TcCsType",
    "WmanIf2TcEthernetType",
    "WmanIf2TcFsnType",
    "WmanIf2TcIpTypOfServ",
    "WmanIf2TcIpv6FlowLabel",
    "WmanIf2TcMbsType",
    "WmanIf2TcPhsRuleVerify",
    "WmanIf2TcReqTxPolicy",
    "WmanIf2TcSchedulingType",
    "WmanIf2TcSduType",
    "WmanIf2TcSfDirection",
    "WmanIf2TcSfState")


# MODULE-IDENTITY

wmanIf2fBsMib = ModuleIdentity(
    (1, 0, 8802, 16, 4)
)
if mibBuilder.loadTexts:
    wmanIf2fBsMib.setRevisions(
        ("2009-01-28 00:00",
         "2008-10-01 00:00",
         "2008-07-22 00:00",
         "2008-05-27 00:00",
         "2008-03-31 00:00",
         "2008-02-11 00:00",
         "2007-11-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class WmanIf2fServClassName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )



# MIB Managed Objects in the order of their OIDs

_WmanIf2fBsProvServiceFlowTable_Object = MibTable
wmanIf2fBsProvServiceFlowTable = _WmanIf2fBsProvServiceFlowTable_Object(
    (1, 0, 8802, 16, 4, 1)
)
if mibBuilder.loadTexts:
    wmanIf2fBsProvServiceFlowTable.setStatus("current")
_WmanIf2fBsProvServiceFlowEntry_Object = MibTableRow
wmanIf2fBsProvServiceFlowEntry = _WmanIf2fBsProvServiceFlowEntry_Object(
    (1, 0, 8802, 16, 4, 1, 1)
)
wmanIf2fBsProvServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSsProvMacAddress"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfId"),
)
if mibBuilder.loadTexts:
    wmanIf2fBsProvServiceFlowEntry.setStatus("current")
_WmanIf2fBsSsProvMacAddress_Type = MacAddress
_WmanIf2fBsSsProvMacAddress_Object = MibTableColumn
wmanIf2fBsSsProvMacAddress = _WmanIf2fBsSsProvMacAddress_Object(
    (1, 0, 8802, 16, 4, 1, 1, 1),
    _WmanIf2fBsSsProvMacAddress_Type()
)
wmanIf2fBsSsProvMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsSsProvMacAddress.setStatus("current")


class _WmanIf2fBsSfId_Type(Unsigned32):
    """Custom type wmanIf2fBsSfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIf2fBsSfId_Type.__name__ = "Unsigned32"
_WmanIf2fBsSfId_Object = MibTableColumn
wmanIf2fBsSfId = _WmanIf2fBsSfId_Object(
    (1, 0, 8802, 16, 4, 1, 1, 2),
    _WmanIf2fBsSfId_Type()
)
wmanIf2fBsSfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsSfId.setStatus("current")
_WmanIf2fBsSfDirection_Type = WmanIf2TcSfDirection
_WmanIf2fBsSfDirection_Object = MibTableColumn
wmanIf2fBsSfDirection = _WmanIf2fBsSfDirection_Object(
    (1, 0, 8802, 16, 4, 1, 1, 3),
    _WmanIf2fBsSfDirection_Type()
)
wmanIf2fBsSfDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsSfDirection.setStatus("current")


class _WmanIf2fBsServiceClassIndex_Type(Integer32):
    """Custom type wmanIf2fBsServiceClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2fBsServiceClassIndex_Type.__name__ = "Integer32"
_WmanIf2fBsServiceClassIndex_Object = MibTableColumn
wmanIf2fBsServiceClassIndex = _WmanIf2fBsServiceClassIndex_Object(
    (1, 0, 8802, 16, 4, 1, 1, 4),
    _WmanIf2fBsServiceClassIndex_Type()
)
wmanIf2fBsServiceClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsServiceClassIndex.setStatus("current")
_WmanIf2fBsSfState_Type = WmanIf2TcSfState
_WmanIf2fBsSfState_Object = MibTableColumn
wmanIf2fBsSfState = _WmanIf2fBsSfState_Object(
    (1, 0, 8802, 16, 4, 1, 1, 5),
    _WmanIf2fBsSfState_Type()
)
wmanIf2fBsSfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsSfState.setStatus("current")
_WmanIf2fBsSfProvisionedTime_Type = TimeStamp
_WmanIf2fBsSfProvisionedTime_Object = MibTableColumn
wmanIf2fBsSfProvisionedTime = _WmanIf2fBsSfProvisionedTime_Object(
    (1, 0, 8802, 16, 4, 1, 1, 6),
    _WmanIf2fBsSfProvisionedTime_Type()
)
wmanIf2fBsSfProvisionedTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsSfProvisionedTime.setStatus("current")
_WmanIf2fBsSfCsSpecification_Type = WmanIf2TcCsType
_WmanIf2fBsSfCsSpecification_Object = MibTableColumn
wmanIf2fBsSfCsSpecification = _WmanIf2fBsSfCsSpecification_Object(
    (1, 0, 8802, 16, 4, 1, 1, 7),
    _WmanIf2fBsSfCsSpecification_Type()
)
wmanIf2fBsSfCsSpecification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsSfCsSpecification.setStatus("current")
_WmanIf2fBsProvisionedSfRowStatus_Type = RowStatus
_WmanIf2fBsProvisionedSfRowStatus_Object = MibTableColumn
wmanIf2fBsProvisionedSfRowStatus = _WmanIf2fBsProvisionedSfRowStatus_Object(
    (1, 0, 8802, 16, 4, 1, 1, 8),
    _WmanIf2fBsProvisionedSfRowStatus_Type()
)
wmanIf2fBsProvisionedSfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvisionedSfRowStatus.setStatus("current")
_WmanIf2fBsProvServiceClassTable_Object = MibTable
wmanIf2fBsProvServiceClassTable = _WmanIf2fBsProvServiceClassTable_Object(
    (1, 0, 8802, 16, 4, 2)
)
if mibBuilder.loadTexts:
    wmanIf2fBsProvServiceClassTable.setStatus("current")
_WmanIf2fBsProvServiceClassEntry_Object = MibTableRow
wmanIf2fBsProvServiceClassEntry = _WmanIf2fBsProvServiceClassEntry_Object(
    (1, 0, 8802, 16, 4, 2, 1)
)
wmanIf2fBsProvServiceClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSProfileIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2fBsProvServiceClassEntry.setStatus("current")


class _WmanIf2fBsQoSProfileIndex_Type(Integer32):
    """Custom type wmanIf2fBsQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIf2fBsQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIf2fBsQoSProfileIndex_Object = MibTableColumn
wmanIf2fBsQoSProfileIndex = _WmanIf2fBsQoSProfileIndex_Object(
    (1, 0, 8802, 16, 4, 2, 1, 1),
    _WmanIf2fBsQoSProfileIndex_Type()
)
wmanIf2fBsQoSProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSProfileIndex.setStatus("current")
_WmanIf2fBsQosServiceClassName_Type = WmanIf2fServClassName
_WmanIf2fBsQosServiceClassName_Object = MibTableColumn
wmanIf2fBsQosServiceClassName = _WmanIf2fBsQosServiceClassName_Object(
    (1, 0, 8802, 16, 4, 2, 1, 2),
    _WmanIf2fBsQosServiceClassName_Type()
)
wmanIf2fBsQosServiceClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosServiceClassName.setStatus("current")


class _WmanIf2fBsQoSTrafficPriority_Type(Integer32):
    """Custom type wmanIf2fBsQoSTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2fBsQoSTrafficPriority_Type.__name__ = "Integer32"
_WmanIf2fBsQoSTrafficPriority_Object = MibTableColumn
wmanIf2fBsQoSTrafficPriority = _WmanIf2fBsQoSTrafficPriority_Object(
    (1, 0, 8802, 16, 4, 2, 1, 3),
    _WmanIf2fBsQoSTrafficPriority_Type()
)
wmanIf2fBsQoSTrafficPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSTrafficPriority.setStatus("current")
_WmanIf2fBsQoSMaxSustainedRate_Type = Unsigned32
_WmanIf2fBsQoSMaxSustainedRate_Object = MibTableColumn
wmanIf2fBsQoSMaxSustainedRate = _WmanIf2fBsQoSMaxSustainedRate_Object(
    (1, 0, 8802, 16, 4, 2, 1, 4),
    _WmanIf2fBsQoSMaxSustainedRate_Type()
)
wmanIf2fBsQoSMaxSustainedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSMaxSustainedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSMaxSustainedRate.setUnits("b/s")
_WmanIf2fBsQoSMaxTrafficBurst_Type = Unsigned32
_WmanIf2fBsQoSMaxTrafficBurst_Object = MibTableColumn
wmanIf2fBsQoSMaxTrafficBurst = _WmanIf2fBsQoSMaxTrafficBurst_Object(
    (1, 0, 8802, 16, 4, 2, 1, 5),
    _WmanIf2fBsQoSMaxTrafficBurst_Type()
)
wmanIf2fBsQoSMaxTrafficBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSMaxTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSMaxTrafficBurst.setUnits("byte")
_WmanIf2fBsQoSMinReservedRate_Type = Unsigned32
_WmanIf2fBsQoSMinReservedRate_Object = MibTableColumn
wmanIf2fBsQoSMinReservedRate = _WmanIf2fBsQoSMinReservedRate_Object(
    (1, 0, 8802, 16, 4, 2, 1, 6),
    _WmanIf2fBsQoSMinReservedRate_Type()
)
wmanIf2fBsQoSMinReservedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSMinReservedRate.setUnits(" b/s")
_WmanIf2fBsQoSToleratedJitter_Type = Unsigned32
_WmanIf2fBsQoSToleratedJitter_Object = MibTableColumn
wmanIf2fBsQoSToleratedJitter = _WmanIf2fBsQoSToleratedJitter_Object(
    (1, 0, 8802, 16, 4, 2, 1, 7),
    _WmanIf2fBsQoSToleratedJitter_Type()
)
wmanIf2fBsQoSToleratedJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSToleratedJitter.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSToleratedJitter.setUnits("millisecond")
_WmanIf2fBsQoSMaxLatency_Type = Unsigned32
_WmanIf2fBsQoSMaxLatency_Object = MibTableColumn
wmanIf2fBsQoSMaxLatency = _WmanIf2fBsQoSMaxLatency_Object(
    (1, 0, 8802, 16, 4, 2, 1, 8),
    _WmanIf2fBsQoSMaxLatency_Type()
)
wmanIf2fBsQoSMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSMaxLatency.setUnits("millisecond")


class _WmanIf2fBsQoSFixedVsVariableSduInd_Type(WmanIf2TcSduType):
    """Custom type wmanIf2fBsQoSFixedVsVariableSduInd based on WmanIf2TcSduType"""
    defaultValue = 0


_WmanIf2fBsQoSFixedVsVariableSduInd_Type.__name__ = "WmanIf2TcSduType"
_WmanIf2fBsQoSFixedVsVariableSduInd_Object = MibTableColumn
wmanIf2fBsQoSFixedVsVariableSduInd = _WmanIf2fBsQoSFixedVsVariableSduInd_Object(
    (1, 0, 8802, 16, 4, 2, 1, 9),
    _WmanIf2fBsQoSFixedVsVariableSduInd_Type()
)
wmanIf2fBsQoSFixedVsVariableSduInd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSFixedVsVariableSduInd.setStatus("current")


class _WmanIf2fBsQoSSduSize_Type(Unsigned32):
    """Custom type wmanIf2fBsQoSSduSize based on Unsigned32"""
    defaultValue = 49


_WmanIf2fBsQoSSduSize_Type.__name__ = "Unsigned32"
_WmanIf2fBsQoSSduSize_Object = MibTableColumn
wmanIf2fBsQoSSduSize = _WmanIf2fBsQoSSduSize_Object(
    (1, 0, 8802, 16, 4, 2, 1, 10),
    _WmanIf2fBsQoSSduSize_Type()
)
wmanIf2fBsQoSSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSSduSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQoSSduSize.setUnits("byte")


class _WmanIf2fBsQosScSchedulingType_Type(WmanIf2TcSchedulingType):
    """Custom type wmanIf2fBsQosScSchedulingType based on WmanIf2TcSchedulingType"""
    defaultValue = 2


_WmanIf2fBsQosScSchedulingType_Type.__name__ = "WmanIf2TcSchedulingType"
_WmanIf2fBsQosScSchedulingType_Object = MibTableColumn
wmanIf2fBsQosScSchedulingType = _WmanIf2fBsQosScSchedulingType_Object(
    (1, 0, 8802, 16, 4, 2, 1, 11),
    _WmanIf2fBsQosScSchedulingType_Type()
)
wmanIf2fBsQosScSchedulingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScSchedulingType.setStatus("current")
_WmanIf2fBsQosScArqEnable_Type = TruthValue
_WmanIf2fBsQosScArqEnable_Object = MibTableColumn
wmanIf2fBsQosScArqEnable = _WmanIf2fBsQosScArqEnable_Object(
    (1, 0, 8802, 16, 4, 2, 1, 12),
    _WmanIf2fBsQosScArqEnable_Type()
)
wmanIf2fBsQosScArqEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqEnable.setStatus("current")


class _WmanIf2fBsQosScArqWindowSize_Type(Integer32):
    """Custom type wmanIf2fBsQosScArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIf2fBsQosScArqWindowSize_Type.__name__ = "Integer32"
_WmanIf2fBsQosScArqWindowSize_Object = MibTableColumn
wmanIf2fBsQosScArqWindowSize = _WmanIf2fBsQosScArqWindowSize_Object(
    (1, 0, 8802, 16, 4, 2, 1, 13),
    _WmanIf2fBsQosScArqWindowSize_Type()
)
wmanIf2fBsQosScArqWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqWindowSize.setStatus("current")


class _WmanIf2fBsQosArqTxRetryTimeout_Type(Integer32):
    """Custom type wmanIf2fBsQosArqTxRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsQosArqTxRetryTimeout_Type.__name__ = "Integer32"
_WmanIf2fBsQosArqTxRetryTimeout_Object = MibTableColumn
wmanIf2fBsQosArqTxRetryTimeout = _WmanIf2fBsQosArqTxRetryTimeout_Object(
    (1, 0, 8802, 16, 4, 2, 1, 14),
    _WmanIf2fBsQosArqTxRetryTimeout_Type()
)
wmanIf2fBsQosArqTxRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosArqTxRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQosArqTxRetryTimeout.setUnits("100 us")


class _WmanIf2fBsQosArqRxRetryTimeout_Type(Integer32):
    """Custom type wmanIf2fBsQosArqRxRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsQosArqRxRetryTimeout_Type.__name__ = "Integer32"
_WmanIf2fBsQosArqRxRetryTimeout_Object = MibTableColumn
wmanIf2fBsQosArqRxRetryTimeout = _WmanIf2fBsQosArqRxRetryTimeout_Object(
    (1, 0, 8802, 16, 4, 2, 1, 15),
    _WmanIf2fBsQosArqRxRetryTimeout_Type()
)
wmanIf2fBsQosArqRxRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosArqRxRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQosArqRxRetryTimeout.setUnits("100 us")


class _WmanIf2fBsQosScArqBlockLifetime_Type(Integer32):
    """Custom type wmanIf2fBsQosScArqBlockLifetime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsQosScArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIf2fBsQosScArqBlockLifetime_Object = MibTableColumn
wmanIf2fBsQosScArqBlockLifetime = _WmanIf2fBsQosScArqBlockLifetime_Object(
    (1, 0, 8802, 16, 4, 2, 1, 16),
    _WmanIf2fBsQosScArqBlockLifetime_Type()
)
wmanIf2fBsQosScArqBlockLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqBlockLifetime.setUnits("100 us")


class _WmanIf2fBsQosScArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIf2fBsQosScArqSyncLossTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsQosScArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIf2fBsQosScArqSyncLossTimeout_Object = MibTableColumn
wmanIf2fBsQosScArqSyncLossTimeout = _WmanIf2fBsQosScArqSyncLossTimeout_Object(
    (1, 0, 8802, 16, 4, 2, 1, 17),
    _WmanIf2fBsQosScArqSyncLossTimeout_Type()
)
wmanIf2fBsQosScArqSyncLossTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqSyncLossTimeout.setUnits("100 us")
_WmanIf2fBsQosScArqDeliverInOrder_Type = TruthValue
_WmanIf2fBsQosScArqDeliverInOrder_Object = MibTableColumn
wmanIf2fBsQosScArqDeliverInOrder = _WmanIf2fBsQosScArqDeliverInOrder_Object(
    (1, 0, 8802, 16, 4, 2, 1, 18),
    _WmanIf2fBsQosScArqDeliverInOrder_Type()
)
wmanIf2fBsQosScArqDeliverInOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqDeliverInOrder.setStatus("current")


class _WmanIf2fBsQosScArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIf2fBsQosScArqRxPurgeTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsQosScArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIf2fBsQosScArqRxPurgeTimeout_Object = MibTableColumn
wmanIf2fBsQosScArqRxPurgeTimeout = _WmanIf2fBsQosScArqRxPurgeTimeout_Object(
    (1, 0, 8802, 16, 4, 2, 1, 19),
    _WmanIf2fBsQosScArqRxPurgeTimeout_Type()
)
wmanIf2fBsQosScArqRxPurgeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqRxPurgeTimeout.setUnits("100 us")
_WmanIf2fBsQosScArqBlockSizeReq_Type = WmanIf2TcArqBlockSize
_WmanIf2fBsQosScArqBlockSizeReq_Object = MibTableColumn
wmanIf2fBsQosScArqBlockSizeReq = _WmanIf2fBsQosScArqBlockSizeReq_Object(
    (1, 0, 8802, 16, 4, 2, 1, 20),
    _WmanIf2fBsQosScArqBlockSizeReq_Type()
)
wmanIf2fBsQosScArqBlockSizeReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqBlockSizeReq.setStatus("current")


class _WmanIf2fBsQosScArqBlockSizeRsp_Type(Integer32):
    """Custom type wmanIf2fBsQosScArqBlockSizeRsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2fBsQosScArqBlockSizeRsp_Type.__name__ = "Integer32"
_WmanIf2fBsQosScArqBlockSizeRsp_Object = MibTableColumn
wmanIf2fBsQosScArqBlockSizeRsp = _WmanIf2fBsQosScArqBlockSizeRsp_Object(
    (1, 0, 8802, 16, 4, 2, 1, 21),
    _WmanIf2fBsQosScArqBlockSizeRsp_Type()
)
wmanIf2fBsQosScArqBlockSizeRsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosScArqBlockSizeRsp.setStatus("current")
_WmanIf2fBsQosReqTxPolicy_Type = WmanIf2TcReqTxPolicy
_WmanIf2fBsQosReqTxPolicy_Object = MibTableColumn
wmanIf2fBsQosReqTxPolicy = _WmanIf2fBsQosReqTxPolicy_Object(
    (1, 0, 8802, 16, 4, 2, 1, 22),
    _WmanIf2fBsQosReqTxPolicy_Type()
)
wmanIf2fBsQosReqTxPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosReqTxPolicy.setStatus("current")


class _WmanIf2fBsQosFragmentSeqNumType_Type(WmanIf2TcFsnType):
    """Custom type wmanIf2fBsQosFragmentSeqNumType based on WmanIf2TcFsnType"""
    defaultValue = 1


_WmanIf2fBsQosFragmentSeqNumType_Type.__name__ = "WmanIf2TcFsnType"
_WmanIf2fBsQosFragmentSeqNumType_Object = MibTableColumn
wmanIf2fBsQosFragmentSeqNumType = _WmanIf2fBsQosFragmentSeqNumType_Object(
    (1, 0, 8802, 16, 4, 2, 1, 23),
    _WmanIf2fBsQosFragmentSeqNumType_Type()
)
wmanIf2fBsQosFragmentSeqNumType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosFragmentSeqNumType.setStatus("current")
_WmanIf2fBsQosMbsService_Type = WmanIf2TcMbsType
_WmanIf2fBsQosMbsService_Object = MibTableColumn
wmanIf2fBsQosMbsService = _WmanIf2fBsQosMbsService_Object(
    (1, 0, 8802, 16, 4, 2, 1, 24),
    _WmanIf2fBsQosMbsService_Type()
)
wmanIf2fBsQosMbsService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosMbsService.setStatus("current")
_WmanIf2fBsQosServiceClassRowStatus_Type = RowStatus
_WmanIf2fBsQosServiceClassRowStatus_Object = MibTableColumn
wmanIf2fBsQosServiceClassRowStatus = _WmanIf2fBsQosServiceClassRowStatus_Object(
    (1, 0, 8802, 16, 4, 2, 1, 25),
    _WmanIf2fBsQosServiceClassRowStatus_Type()
)
wmanIf2fBsQosServiceClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsQosServiceClassRowStatus.setStatus("current")
_WmanIf2fBsServiceFlowTable_Object = MibTable
wmanIf2fBsServiceFlowTable = _WmanIf2fBsServiceFlowTable_Object(
    (1, 0, 8802, 16, 4, 3)
)
if mibBuilder.loadTexts:
    wmanIf2fBsServiceFlowTable.setStatus("current")
_WmanIf2fBsServiceFlowEntry_Object = MibTableRow
wmanIf2fBsServiceFlowEntry = _WmanIf2fBsServiceFlowEntry_Object(
    (1, 0, 8802, 16, 4, 3, 1)
)
wmanIf2fBsServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfMacAddress"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfId"),
)
if mibBuilder.loadTexts:
    wmanIf2fBsServiceFlowEntry.setStatus("current")
_WmanIf2fBsSfMacAddress_Type = MacAddress
_WmanIf2fBsSfMacAddress_Object = MibTableColumn
wmanIf2fBsSfMacAddress = _WmanIf2fBsSfMacAddress_Object(
    (1, 0, 8802, 16, 4, 3, 1, 1),
    _WmanIf2fBsSfMacAddress_Type()
)
wmanIf2fBsSfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsSfMacAddress.setStatus("current")
_WmanIf2fBsSfCid_Type = WmanIf2TcCidType
_WmanIf2fBsSfCid_Object = MibTableColumn
wmanIf2fBsSfCid = _WmanIf2fBsSfCid_Object(
    (1, 0, 8802, 16, 4, 3, 1, 2),
    _WmanIf2fBsSfCid_Type()
)
wmanIf2fBsSfCid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsSfCid.setStatus("current")
_WmanIf2fBsServiceFlowDirection_Type = WmanIf2TcSfDirection
_WmanIf2fBsServiceFlowDirection_Object = MibTableColumn
wmanIf2fBsServiceFlowDirection = _WmanIf2fBsServiceFlowDirection_Object(
    (1, 0, 8802, 16, 4, 3, 1, 3),
    _WmanIf2fBsServiceFlowDirection_Type()
)
wmanIf2fBsServiceFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsServiceFlowDirection.setStatus("current")
_WmanIf2fBsServiceFlowState_Type = WmanIf2TcSfState
_WmanIf2fBsServiceFlowState_Object = MibTableColumn
wmanIf2fBsServiceFlowState = _WmanIf2fBsServiceFlowState_Object(
    (1, 0, 8802, 16, 4, 3, 1, 4),
    _WmanIf2fBsServiceFlowState_Type()
)
wmanIf2fBsServiceFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsServiceFlowState.setStatus("current")


class _WmanIf2fBsTrafficPriority_Type(Integer32):
    """Custom type wmanIf2fBsTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2fBsTrafficPriority_Type.__name__ = "Integer32"
_WmanIf2fBsTrafficPriority_Object = MibTableColumn
wmanIf2fBsTrafficPriority = _WmanIf2fBsTrafficPriority_Object(
    (1, 0, 8802, 16, 4, 3, 1, 5),
    _WmanIf2fBsTrafficPriority_Type()
)
wmanIf2fBsTrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsTrafficPriority.setStatus("current")
_WmanIf2fBsMaxSustainedRate_Type = Unsigned32
_WmanIf2fBsMaxSustainedRate_Object = MibTableColumn
wmanIf2fBsMaxSustainedRate = _WmanIf2fBsMaxSustainedRate_Object(
    (1, 0, 8802, 16, 4, 3, 1, 6),
    _WmanIf2fBsMaxSustainedRate_Type()
)
wmanIf2fBsMaxSustainedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsMaxSustainedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsMaxSustainedRate.setUnits("b/s")
_WmanIf2fBsMaxTrafficBurst_Type = Unsigned32
_WmanIf2fBsMaxTrafficBurst_Object = MibTableColumn
wmanIf2fBsMaxTrafficBurst = _WmanIf2fBsMaxTrafficBurst_Object(
    (1, 0, 8802, 16, 4, 3, 1, 7),
    _WmanIf2fBsMaxTrafficBurst_Type()
)
wmanIf2fBsMaxTrafficBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsMaxTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsMaxTrafficBurst.setUnits("byte")
_WmanIf2fBsMinReservedRate_Type = Unsigned32
_WmanIf2fBsMinReservedRate_Object = MibTableColumn
wmanIf2fBsMinReservedRate = _WmanIf2fBsMinReservedRate_Object(
    (1, 0, 8802, 16, 4, 3, 1, 8),
    _WmanIf2fBsMinReservedRate_Type()
)
wmanIf2fBsMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsMinReservedRate.setUnits("byte")
_WmanIf2fBsToleratedJitter_Type = Unsigned32
_WmanIf2fBsToleratedJitter_Object = MibTableColumn
wmanIf2fBsToleratedJitter = _WmanIf2fBsToleratedJitter_Object(
    (1, 0, 8802, 16, 4, 3, 1, 9),
    _WmanIf2fBsToleratedJitter_Type()
)
wmanIf2fBsToleratedJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsToleratedJitter.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsToleratedJitter.setUnits("millisecond")
_WmanIf2fBsMaxLatency_Type = Unsigned32
_WmanIf2fBsMaxLatency_Object = MibTableColumn
wmanIf2fBsMaxLatency = _WmanIf2fBsMaxLatency_Object(
    (1, 0, 8802, 16, 4, 3, 1, 10),
    _WmanIf2fBsMaxLatency_Type()
)
wmanIf2fBsMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsMaxLatency.setUnits("millisecond")


class _WmanIf2fBsFixedVsVariableSduInd_Type(WmanIf2TcSduType):
    """Custom type wmanIf2fBsFixedVsVariableSduInd based on WmanIf2TcSduType"""
    defaultValue = 0


_WmanIf2fBsFixedVsVariableSduInd_Type.__name__ = "WmanIf2TcSduType"
_WmanIf2fBsFixedVsVariableSduInd_Object = MibTableColumn
wmanIf2fBsFixedVsVariableSduInd = _WmanIf2fBsFixedVsVariableSduInd_Object(
    (1, 0, 8802, 16, 4, 3, 1, 11),
    _WmanIf2fBsFixedVsVariableSduInd_Type()
)
wmanIf2fBsFixedVsVariableSduInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsFixedVsVariableSduInd.setStatus("current")


class _WmanIf2fBsSduSize_Type(Unsigned32):
    """Custom type wmanIf2fBsSduSize based on Unsigned32"""
    defaultValue = 49


_WmanIf2fBsSduSize_Type.__name__ = "Unsigned32"
_WmanIf2fBsSduSize_Object = MibTableColumn
wmanIf2fBsSduSize = _WmanIf2fBsSduSize_Object(
    (1, 0, 8802, 16, 4, 3, 1, 12),
    _WmanIf2fBsSduSize_Type()
)
wmanIf2fBsSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsSduSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsSduSize.setUnits("byte")


class _WmanIf2fBsSfSchedulingType_Type(WmanIf2TcSchedulingType):
    """Custom type wmanIf2fBsSfSchedulingType based on WmanIf2TcSchedulingType"""
    defaultValue = 2


_WmanIf2fBsSfSchedulingType_Type.__name__ = "WmanIf2TcSchedulingType"
_WmanIf2fBsSfSchedulingType_Object = MibTableColumn
wmanIf2fBsSfSchedulingType = _WmanIf2fBsSfSchedulingType_Object(
    (1, 0, 8802, 16, 4, 3, 1, 13),
    _WmanIf2fBsSfSchedulingType_Type()
)
wmanIf2fBsSfSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsSfSchedulingType.setStatus("current")
_WmanIf2fBsArqEnable_Type = TruthValue
_WmanIf2fBsArqEnable_Object = MibTableColumn
wmanIf2fBsArqEnable = _WmanIf2fBsArqEnable_Object(
    (1, 0, 8802, 16, 4, 3, 1, 14),
    _WmanIf2fBsArqEnable_Type()
)
wmanIf2fBsArqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsArqEnable.setStatus("current")


class _WmanIf2fBsArqWindowSize_Type(Integer32):
    """Custom type wmanIf2fBsArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIf2fBsArqWindowSize_Type.__name__ = "Integer32"
_WmanIf2fBsArqWindowSize_Object = MibTableColumn
wmanIf2fBsArqWindowSize = _WmanIf2fBsArqWindowSize_Object(
    (1, 0, 8802, 16, 4, 3, 1, 15),
    _WmanIf2fBsArqWindowSize_Type()
)
wmanIf2fBsArqWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsArqWindowSize.setStatus("current")


class _WmanIf2fBsArqTxRetryTimeout_Type(Integer32):
    """Custom type wmanIf2fBsArqTxRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsArqTxRetryTimeout_Type.__name__ = "Integer32"
_WmanIf2fBsArqTxRetryTimeout_Object = MibTableColumn
wmanIf2fBsArqTxRetryTimeout = _WmanIf2fBsArqTxRetryTimeout_Object(
    (1, 0, 8802, 16, 4, 3, 1, 16),
    _WmanIf2fBsArqTxRetryTimeout_Type()
)
wmanIf2fBsArqTxRetryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsArqTxRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsArqTxRetryTimeout.setUnits("100 us")


class _WmanIf2fBsArqRxRetryTimeout_Type(Integer32):
    """Custom type wmanIf2fBsArqRxRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsArqRxRetryTimeout_Type.__name__ = "Integer32"
_WmanIf2fBsArqRxRetryTimeout_Object = MibTableColumn
wmanIf2fBsArqRxRetryTimeout = _WmanIf2fBsArqRxRetryTimeout_Object(
    (1, 0, 8802, 16, 4, 3, 1, 17),
    _WmanIf2fBsArqRxRetryTimeout_Type()
)
wmanIf2fBsArqRxRetryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsArqRxRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsArqRxRetryTimeout.setUnits("100 us")


class _WmanIf2fBsArqBlockLifetime_Type(Integer32):
    """Custom type wmanIf2fBsArqBlockLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsArqBlockLifetime_Type.__name__ = "Integer32"
_WmanIf2fBsArqBlockLifetime_Object = MibTableColumn
wmanIf2fBsArqBlockLifetime = _WmanIf2fBsArqBlockLifetime_Object(
    (1, 0, 8802, 16, 4, 3, 1, 18),
    _WmanIf2fBsArqBlockLifetime_Type()
)
wmanIf2fBsArqBlockLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsArqBlockLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsArqBlockLifetime.setUnits("100 us")


class _WmanIf2fBsArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIf2fBsArqSyncLossTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIf2fBsArqSyncLossTimeout_Object = MibTableColumn
wmanIf2fBsArqSyncLossTimeout = _WmanIf2fBsArqSyncLossTimeout_Object(
    (1, 0, 8802, 16, 4, 3, 1, 19),
    _WmanIf2fBsArqSyncLossTimeout_Type()
)
wmanIf2fBsArqSyncLossTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsArqSyncLossTimeout.setUnits("100 us")
_WmanIf2fBsArqDeliverInOrder_Type = TruthValue
_WmanIf2fBsArqDeliverInOrder_Object = MibTableColumn
wmanIf2fBsArqDeliverInOrder = _WmanIf2fBsArqDeliverInOrder_Object(
    (1, 0, 8802, 16, 4, 3, 1, 20),
    _WmanIf2fBsArqDeliverInOrder_Type()
)
wmanIf2fBsArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsArqDeliverInOrder.setStatus("current")


class _WmanIf2fBsArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIf2fBsArqRxPurgeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIf2fBsArqRxPurgeTimeout_Object = MibTableColumn
wmanIf2fBsArqRxPurgeTimeout = _WmanIf2fBsArqRxPurgeTimeout_Object(
    (1, 0, 8802, 16, 4, 3, 1, 21),
    _WmanIf2fBsArqRxPurgeTimeout_Type()
)
wmanIf2fBsArqRxPurgeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsArqRxPurgeTimeout.setUnits("100 us")
_WmanIf2fBsScArqBlockSizeReq_Type = WmanIf2TcArqBlockSize
_WmanIf2fBsScArqBlockSizeReq_Object = MibTableColumn
wmanIf2fBsScArqBlockSizeReq = _WmanIf2fBsScArqBlockSizeReq_Object(
    (1, 0, 8802, 16, 4, 3, 1, 22),
    _WmanIf2fBsScArqBlockSizeReq_Type()
)
wmanIf2fBsScArqBlockSizeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsScArqBlockSizeReq.setStatus("current")


class _WmanIf2fBsScArqBlockSizeRsp_Type(Integer32):
    """Custom type wmanIf2fBsScArqBlockSizeRsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIf2fBsScArqBlockSizeRsp_Type.__name__ = "Integer32"
_WmanIf2fBsScArqBlockSizeRsp_Object = MibTableColumn
wmanIf2fBsScArqBlockSizeRsp = _WmanIf2fBsScArqBlockSizeRsp_Object(
    (1, 0, 8802, 16, 4, 3, 1, 23),
    _WmanIf2fBsScArqBlockSizeRsp_Type()
)
wmanIf2fBsScArqBlockSizeRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsScArqBlockSizeRsp.setStatus("current")
_WmanIf2fBsReqTxPolicy_Type = WmanIf2TcReqTxPolicy
_WmanIf2fBsReqTxPolicy_Object = MibTableColumn
wmanIf2fBsReqTxPolicy = _WmanIf2fBsReqTxPolicy_Object(
    (1, 0, 8802, 16, 4, 3, 1, 24),
    _WmanIf2fBsReqTxPolicy_Type()
)
wmanIf2fBsReqTxPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsReqTxPolicy.setStatus("current")
_WmanIf2fBsCsSpecification_Type = WmanIf2TcCsType
_WmanIf2fBsCsSpecification_Object = MibTableColumn
wmanIf2fBsCsSpecification = _WmanIf2fBsCsSpecification_Object(
    (1, 0, 8802, 16, 4, 3, 1, 25),
    _WmanIf2fBsCsSpecification_Type()
)
wmanIf2fBsCsSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsCsSpecification.setStatus("current")


class _WmanIf2fBsTargetSaid_Type(Integer32):
    """Custom type wmanIf2fBsTargetSaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsTargetSaid_Type.__name__ = "Integer32"
_WmanIf2fBsTargetSaid_Object = MibTableColumn
wmanIf2fBsTargetSaid = _WmanIf2fBsTargetSaid_Object(
    (1, 0, 8802, 16, 4, 3, 1, 26),
    _WmanIf2fBsTargetSaid_Type()
)
wmanIf2fBsTargetSaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsTargetSaid.setStatus("current")


class _WmanIf2fBsFragmentSeqNumType_Type(WmanIf2TcFsnType):
    """Custom type wmanIf2fBsFragmentSeqNumType based on WmanIf2TcFsnType"""
    defaultValue = 1


_WmanIf2fBsFragmentSeqNumType_Type.__name__ = "WmanIf2TcFsnType"
_WmanIf2fBsFragmentSeqNumType_Object = MibTableColumn
wmanIf2fBsFragmentSeqNumType = _WmanIf2fBsFragmentSeqNumType_Object(
    (1, 0, 8802, 16, 4, 3, 1, 27),
    _WmanIf2fBsFragmentSeqNumType_Type()
)
wmanIf2fBsFragmentSeqNumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsFragmentSeqNumType.setStatus("current")
_WmanIf2fBsMbsService_Type = WmanIf2TcMbsType
_WmanIf2fBsMbsService_Object = MibTableColumn
wmanIf2fBsMbsService = _WmanIf2fBsMbsService_Object(
    (1, 0, 8802, 16, 4, 3, 1, 28),
    _WmanIf2fBsMbsService_Type()
)
wmanIf2fBsMbsService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsMbsService.setStatus("current")
_WmanIf2fBsProvClassifierRuleTable_Object = MibTable
wmanIf2fBsProvClassifierRuleTable = _WmanIf2fBsProvClassifierRuleTable_Object(
    (1, 0, 8802, 16, 4, 4)
)
if mibBuilder.loadTexts:
    wmanIf2fBsProvClassifierRuleTable.setStatus("current")
_WmanIf2fBsProvClassifierRuleEntry_Object = MibTableRow
wmanIf2fBsProvClassifierRuleEntry = _WmanIf2fBsProvClassifierRuleEntry_Object(
    (1, 0, 8802, 16, 4, 4, 1)
)
wmanIf2fBsProvClassifierRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSsProvMacAddress"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfId"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2fBsProvClassifierRuleEntry.setStatus("current")


class _WmanIf2fBsProvClsfRuleIndex_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsProvClsfRuleIndex_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleIndex_Object = MibTableColumn
wmanIf2fBsProvClsfRuleIndex = _WmanIf2fBsProvClsfRuleIndex_Object(
    (1, 0, 8802, 16, 4, 4, 1, 1),
    _WmanIf2fBsProvClsfRuleIndex_Type()
)
wmanIf2fBsProvClsfRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleIndex.setStatus("current")


class _WmanIf2fBsProvClsfRulePriority_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRulePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2fBsProvClsfRulePriority_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRulePriority_Object = MibTableColumn
wmanIf2fBsProvClsfRulePriority = _WmanIf2fBsProvClsfRulePriority_Object(
    (1, 0, 8802, 16, 4, 4, 1, 2),
    _WmanIf2fBsProvClsfRulePriority_Type()
)
wmanIf2fBsProvClsfRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRulePriority.setStatus("current")


class _WmanIf2fBsProvClsfRuleIpProtocol_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2fBsProvClsfRuleIpProtocol_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleIpProtocol_Object = MibTableColumn
wmanIf2fBsProvClsfRuleIpProtocol = _WmanIf2fBsProvClsfRuleIpProtocol_Object(
    (1, 0, 8802, 16, 4, 4, 1, 3),
    _WmanIf2fBsProvClsfRuleIpProtocol_Type()
)
wmanIf2fBsProvClsfRuleIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleIpProtocol.setStatus("current")
_WmanIf2fBsProvClsfRuleIpSrcAddr_Type = InetAddress
_WmanIf2fBsProvClsfRuleIpSrcAddr_Object = MibTableColumn
wmanIf2fBsProvClsfRuleIpSrcAddr = _WmanIf2fBsProvClsfRuleIpSrcAddr_Object(
    (1, 0, 8802, 16, 4, 4, 1, 4),
    _WmanIf2fBsProvClsfRuleIpSrcAddr_Type()
)
wmanIf2fBsProvClsfRuleIpSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleIpSrcAddr.setStatus("current")
_WmanIf2fBsProvClsfRuleIpSrcMask_Type = InetAddress
_WmanIf2fBsProvClsfRuleIpSrcMask_Object = MibTableColumn
wmanIf2fBsProvClsfRuleIpSrcMask = _WmanIf2fBsProvClsfRuleIpSrcMask_Object(
    (1, 0, 8802, 16, 4, 4, 1, 5),
    _WmanIf2fBsProvClsfRuleIpSrcMask_Type()
)
wmanIf2fBsProvClsfRuleIpSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleIpSrcMask.setStatus("current")
_WmanIf2fBsProvClsfRuleIpDestAddr_Type = InetAddress
_WmanIf2fBsProvClsfRuleIpDestAddr_Object = MibTableColumn
wmanIf2fBsProvClsfRuleIpDestAddr = _WmanIf2fBsProvClsfRuleIpDestAddr_Object(
    (1, 0, 8802, 16, 4, 4, 1, 6),
    _WmanIf2fBsProvClsfRuleIpDestAddr_Type()
)
wmanIf2fBsProvClsfRuleIpDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleIpDestAddr.setStatus("current")
_WmanIf2fBsProvClsfRuleIpDestMask_Type = InetAddress
_WmanIf2fBsProvClsfRuleIpDestMask_Object = MibTableColumn
wmanIf2fBsProvClsfRuleIpDestMask = _WmanIf2fBsProvClsfRuleIpDestMask_Object(
    (1, 0, 8802, 16, 4, 4, 1, 7),
    _WmanIf2fBsProvClsfRuleIpDestMask_Type()
)
wmanIf2fBsProvClsfRuleIpDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleIpDestMask.setStatus("current")


class _WmanIf2fBsProvClsfRuleSrcPortStart_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleSrcPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsProvClsfRuleSrcPortStart_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleSrcPortStart_Object = MibTableColumn
wmanIf2fBsProvClsfRuleSrcPortStart = _WmanIf2fBsProvClsfRuleSrcPortStart_Object(
    (1, 0, 8802, 16, 4, 4, 1, 8),
    _WmanIf2fBsProvClsfRuleSrcPortStart_Type()
)
wmanIf2fBsProvClsfRuleSrcPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleSrcPortStart.setStatus("current")


class _WmanIf2fBsProvClsfRuleSrcPortEnd_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleSrcPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsProvClsfRuleSrcPortEnd_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleSrcPortEnd_Object = MibTableColumn
wmanIf2fBsProvClsfRuleSrcPortEnd = _WmanIf2fBsProvClsfRuleSrcPortEnd_Object(
    (1, 0, 8802, 16, 4, 4, 1, 9),
    _WmanIf2fBsProvClsfRuleSrcPortEnd_Type()
)
wmanIf2fBsProvClsfRuleSrcPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleSrcPortEnd.setStatus("current")


class _WmanIf2fBsProvClsfRuleDestPortStart_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsProvClsfRuleDestPortStart_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleDestPortStart_Object = MibTableColumn
wmanIf2fBsProvClsfRuleDestPortStart = _WmanIf2fBsProvClsfRuleDestPortStart_Object(
    (1, 0, 8802, 16, 4, 4, 1, 10),
    _WmanIf2fBsProvClsfRuleDestPortStart_Type()
)
wmanIf2fBsProvClsfRuleDestPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleDestPortStart.setStatus("current")


class _WmanIf2fBsProvClsfRuleDestPortEnd_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsProvClsfRuleDestPortEnd_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleDestPortEnd_Object = MibTableColumn
wmanIf2fBsProvClsfRuleDestPortEnd = _WmanIf2fBsProvClsfRuleDestPortEnd_Object(
    (1, 0, 8802, 16, 4, 4, 1, 11),
    _WmanIf2fBsProvClsfRuleDestPortEnd_Type()
)
wmanIf2fBsProvClsfRuleDestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleDestPortEnd.setStatus("current")
_WmanIf2fBsProvClsfRuleDestMacAddr_Type = MacAddress
_WmanIf2fBsProvClsfRuleDestMacAddr_Object = MibTableColumn
wmanIf2fBsProvClsfRuleDestMacAddr = _WmanIf2fBsProvClsfRuleDestMacAddr_Object(
    (1, 0, 8802, 16, 4, 4, 1, 12),
    _WmanIf2fBsProvClsfRuleDestMacAddr_Type()
)
wmanIf2fBsProvClsfRuleDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleDestMacAddr.setStatus("current")
_WmanIf2fBsProvClsfRuleDestMacMask_Type = MacAddress
_WmanIf2fBsProvClsfRuleDestMacMask_Object = MibTableColumn
wmanIf2fBsProvClsfRuleDestMacMask = _WmanIf2fBsProvClsfRuleDestMacMask_Object(
    (1, 0, 8802, 16, 4, 4, 1, 13),
    _WmanIf2fBsProvClsfRuleDestMacMask_Type()
)
wmanIf2fBsProvClsfRuleDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleDestMacMask.setStatus("current")
_WmanIf2fBsProvClsfRuleSrcMacAddr_Type = MacAddress
_WmanIf2fBsProvClsfRuleSrcMacAddr_Object = MibTableColumn
wmanIf2fBsProvClsfRuleSrcMacAddr = _WmanIf2fBsProvClsfRuleSrcMacAddr_Object(
    (1, 0, 8802, 16, 4, 4, 1, 14),
    _WmanIf2fBsProvClsfRuleSrcMacAddr_Type()
)
wmanIf2fBsProvClsfRuleSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleSrcMacAddr.setStatus("current")
_WmanIf2fBsProvClsfRuleSrcMacMask_Type = MacAddress
_WmanIf2fBsProvClsfRuleSrcMacMask_Object = MibTableColumn
wmanIf2fBsProvClsfRuleSrcMacMask = _WmanIf2fBsProvClsfRuleSrcMacMask_Object(
    (1, 0, 8802, 16, 4, 4, 1, 15),
    _WmanIf2fBsProvClsfRuleSrcMacMask_Type()
)
wmanIf2fBsProvClsfRuleSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleSrcMacMask.setStatus("current")
_WmanIf2fBsProvClsfRuleEnetProtType_Type = WmanIf2TcEthernetType
_WmanIf2fBsProvClsfRuleEnetProtType_Object = MibTableColumn
wmanIf2fBsProvClsfRuleEnetProtType = _WmanIf2fBsProvClsfRuleEnetProtType_Object(
    (1, 0, 8802, 16, 4, 4, 1, 16),
    _WmanIf2fBsProvClsfRuleEnetProtType_Type()
)
wmanIf2fBsProvClsfRuleEnetProtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleEnetProtType.setStatus("current")


class _WmanIf2fBsProvClsfRuleEnetProtocol_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsProvClsfRuleEnetProtocol_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleEnetProtocol_Object = MibTableColumn
wmanIf2fBsProvClsfRuleEnetProtocol = _WmanIf2fBsProvClsfRuleEnetProtocol_Object(
    (1, 0, 8802, 16, 4, 4, 1, 17),
    _WmanIf2fBsProvClsfRuleEnetProtocol_Type()
)
wmanIf2fBsProvClsfRuleEnetProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleEnetProtocol.setStatus("current")


class _WmanIf2fBsProvClsfRuleUserPriLow_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2fBsProvClsfRuleUserPriLow_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleUserPriLow_Object = MibTableColumn
wmanIf2fBsProvClsfRuleUserPriLow = _WmanIf2fBsProvClsfRuleUserPriLow_Object(
    (1, 0, 8802, 16, 4, 4, 1, 18),
    _WmanIf2fBsProvClsfRuleUserPriLow_Type()
)
wmanIf2fBsProvClsfRuleUserPriLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleUserPriLow.setStatus("current")


class _WmanIf2fBsProvClsfRuleUserPriHigh_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2fBsProvClsfRuleUserPriHigh_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleUserPriHigh_Object = MibTableColumn
wmanIf2fBsProvClsfRuleUserPriHigh = _WmanIf2fBsProvClsfRuleUserPriHigh_Object(
    (1, 0, 8802, 16, 4, 4, 1, 19),
    _WmanIf2fBsProvClsfRuleUserPriHigh_Type()
)
wmanIf2fBsProvClsfRuleUserPriHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleUserPriHigh.setStatus("current")


class _WmanIf2fBsProvClsfRuleVlanId_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WmanIf2fBsProvClsfRuleVlanId_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleVlanId_Object = MibTableColumn
wmanIf2fBsProvClsfRuleVlanId = _WmanIf2fBsProvClsfRuleVlanId_Object(
    (1, 0, 8802, 16, 4, 4, 1, 20),
    _WmanIf2fBsProvClsfRuleVlanId_Type()
)
wmanIf2fBsProvClsfRuleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleVlanId.setStatus("current")


class _WmanIf2fBsProvClsfRuleAssociatedPhsi_Type(Integer32):
    """Custom type wmanIf2fBsProvClsfRuleAssociatedPhsi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2fBsProvClsfRuleAssociatedPhsi_Type.__name__ = "Integer32"
_WmanIf2fBsProvClsfRuleAssociatedPhsi_Object = MibTableColumn
wmanIf2fBsProvClsfRuleAssociatedPhsi = _WmanIf2fBsProvClsfRuleAssociatedPhsi_Object(
    (1, 0, 8802, 16, 4, 4, 1, 21),
    _WmanIf2fBsProvClsfRuleAssociatedPhsi_Type()
)
wmanIf2fBsProvClsfRuleAssociatedPhsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleAssociatedPhsi.setStatus("current")
_WmanIf2fBsProvClsfRuleIpv6FlowLabel_Type = WmanIf2TcIpv6FlowLabel
_WmanIf2fBsProvClsfRuleIpv6FlowLabel_Object = MibTableColumn
wmanIf2fBsProvClsfRuleIpv6FlowLabel = _WmanIf2fBsProvClsfRuleIpv6FlowLabel_Object(
    (1, 0, 8802, 16, 4, 4, 1, 22),
    _WmanIf2fBsProvClsfRuleIpv6FlowLabel_Type()
)
wmanIf2fBsProvClsfRuleIpv6FlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleIpv6FlowLabel.setStatus("current")
_WmanIf2fBsProvClsfRuleActionRule_Type = WmanIf2TcActionRule
_WmanIf2fBsProvClsfRuleActionRule_Object = MibTableColumn
wmanIf2fBsProvClsfRuleActionRule = _WmanIf2fBsProvClsfRuleActionRule_Object(
    (1, 0, 8802, 16, 4, 4, 1, 23),
    _WmanIf2fBsProvClsfRuleActionRule_Type()
)
wmanIf2fBsProvClsfRuleActionRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleActionRule.setStatus("current")
_WmanIf2fBsProvClsfRuleIpTypeOfService_Type = WmanIf2TcIpTypOfServ
_WmanIf2fBsProvClsfRuleIpTypeOfService_Object = MibTableColumn
wmanIf2fBsProvClsfRuleIpTypeOfService = _WmanIf2fBsProvClsfRuleIpTypeOfService_Object(
    (1, 0, 8802, 16, 4, 4, 1, 24),
    _WmanIf2fBsProvClsfRuleIpTypeOfService_Type()
)
wmanIf2fBsProvClsfRuleIpTypeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleIpTypeOfService.setStatus("current")
_WmanIf2fBsProvClsfRuleBitMap_Type = WmanIf2TcClassifierMap
_WmanIf2fBsProvClsfRuleBitMap_Object = MibTableColumn
wmanIf2fBsProvClsfRuleBitMap = _WmanIf2fBsProvClsfRuleBitMap_Object(
    (1, 0, 8802, 16, 4, 4, 1, 25),
    _WmanIf2fBsProvClsfRuleBitMap_Type()
)
wmanIf2fBsProvClsfRuleBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleBitMap.setStatus("current")
_WmanIf2fBsProvClsfRuleRowStatus_Type = RowStatus
_WmanIf2fBsProvClsfRuleRowStatus_Object = MibTableColumn
wmanIf2fBsProvClsfRuleRowStatus = _WmanIf2fBsProvClsfRuleRowStatus_Object(
    (1, 0, 8802, 16, 4, 4, 1, 26),
    _WmanIf2fBsProvClsfRuleRowStatus_Type()
)
wmanIf2fBsProvClsfRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvClsfRuleRowStatus.setStatus("current")
_WmanIf2fBsProvPhsRuleTable_Object = MibTable
wmanIf2fBsProvPhsRuleTable = _WmanIf2fBsProvPhsRuleTable_Object(
    (1, 0, 8802, 16, 4, 5)
)
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRuleTable.setStatus("current")
_WmanIf2fBsProvPhsRuleEntry_Object = MibTableRow
wmanIf2fBsProvPhsRuleEntry = _WmanIf2fBsProvPhsRuleEntry_Object(
    (1, 0, 8802, 16, 4, 5, 1)
)
wmanIf2fBsProvPhsRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSsProvMacAddress"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfId"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsProvPhsRulePhsIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRuleEntry.setStatus("current")


class _WmanIf2fBsProvPhsRulePhsIndex_Type(Integer32):
    """Custom type wmanIf2fBsProvPhsRulePhsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2fBsProvPhsRulePhsIndex_Type.__name__ = "Integer32"
_WmanIf2fBsProvPhsRulePhsIndex_Object = MibTableColumn
wmanIf2fBsProvPhsRulePhsIndex = _WmanIf2fBsProvPhsRulePhsIndex_Object(
    (1, 0, 8802, 16, 4, 5, 1, 1),
    _WmanIf2fBsProvPhsRulePhsIndex_Type()
)
wmanIf2fBsProvPhsRulePhsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRulePhsIndex.setStatus("current")


class _WmanIf2fBsProvPhsRulePhsField_Type(OctetString):
    """Custom type wmanIf2fBsProvPhsRulePhsField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2fBsProvPhsRulePhsField_Type.__name__ = "OctetString"
_WmanIf2fBsProvPhsRulePhsField_Object = MibTableColumn
wmanIf2fBsProvPhsRulePhsField = _WmanIf2fBsProvPhsRulePhsField_Object(
    (1, 0, 8802, 16, 4, 5, 1, 2),
    _WmanIf2fBsProvPhsRulePhsField_Type()
)
wmanIf2fBsProvPhsRulePhsField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRulePhsField.setStatus("current")


class _WmanIf2fBsProvPhsRulePhsMask_Type(OctetString):
    """Custom type wmanIf2fBsProvPhsRulePhsMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2fBsProvPhsRulePhsMask_Type.__name__ = "OctetString"
_WmanIf2fBsProvPhsRulePhsMask_Object = MibTableColumn
wmanIf2fBsProvPhsRulePhsMask = _WmanIf2fBsProvPhsRulePhsMask_Object(
    (1, 0, 8802, 16, 4, 5, 1, 3),
    _WmanIf2fBsProvPhsRulePhsMask_Type()
)
wmanIf2fBsProvPhsRulePhsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRulePhsMask.setStatus("current")


class _WmanIf2fBsProvPhsRulePhsSize_Type(Integer32):
    """Custom type wmanIf2fBsProvPhsRulePhsSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2fBsProvPhsRulePhsSize_Type.__name__ = "Integer32"
_WmanIf2fBsProvPhsRulePhsSize_Object = MibTableColumn
wmanIf2fBsProvPhsRulePhsSize = _WmanIf2fBsProvPhsRulePhsSize_Object(
    (1, 0, 8802, 16, 4, 5, 1, 4),
    _WmanIf2fBsProvPhsRulePhsSize_Type()
)
wmanIf2fBsProvPhsRulePhsSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRulePhsSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRulePhsSize.setUnits("byte")


class _WmanIf2fBsProvPhsRulePhsVerify_Type(WmanIf2TcPhsRuleVerify):
    """Custom type wmanIf2fBsProvPhsRulePhsVerify based on WmanIf2TcPhsRuleVerify"""
    defaultValue = 0


_WmanIf2fBsProvPhsRulePhsVerify_Type.__name__ = "WmanIf2TcPhsRuleVerify"
_WmanIf2fBsProvPhsRulePhsVerify_Object = MibTableColumn
wmanIf2fBsProvPhsRulePhsVerify = _WmanIf2fBsProvPhsRulePhsVerify_Object(
    (1, 0, 8802, 16, 4, 5, 1, 5),
    _WmanIf2fBsProvPhsRulePhsVerify_Type()
)
wmanIf2fBsProvPhsRulePhsVerify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRulePhsVerify.setStatus("current")
_WmanIf2fBsProvPhsRuleRowStatus_Type = RowStatus
_WmanIf2fBsProvPhsRuleRowStatus_Object = MibTableColumn
wmanIf2fBsProvPhsRuleRowStatus = _WmanIf2fBsProvPhsRuleRowStatus_Object(
    (1, 0, 8802, 16, 4, 5, 1, 6),
    _WmanIf2fBsProvPhsRuleRowStatus_Type()
)
wmanIf2fBsProvPhsRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIf2fBsProvPhsRuleRowStatus.setStatus("current")
_WmanIf2fBsClassifierRuleTable_Object = MibTable
wmanIf2fBsClassifierRuleTable = _WmanIf2fBsClassifierRuleTable_Object(
    (1, 0, 8802, 16, 4, 6)
)
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleTable.setStatus("current")
_WmanIf2fBsClassifierRuleEntry_Object = MibTableRow
wmanIf2fBsClassifierRuleEntry = _WmanIf2fBsClassifierRuleEntry_Object(
    (1, 0, 8802, 16, 4, 6, 1)
)
wmanIf2fBsClassifierRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfMacAddress"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfId"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleEntry.setStatus("current")


class _WmanIf2fBsClassifierRuleIndex_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsClassifierRuleIndex_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleIndex_Object = MibTableColumn
wmanIf2fBsClassifierRuleIndex = _WmanIf2fBsClassifierRuleIndex_Object(
    (1, 0, 8802, 16, 4, 6, 1, 1),
    _WmanIf2fBsClassifierRuleIndex_Type()
)
wmanIf2fBsClassifierRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleIndex.setStatus("current")


class _WmanIf2fBsClassifierRulePriority_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRulePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2fBsClassifierRulePriority_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRulePriority_Object = MibTableColumn
wmanIf2fBsClassifierRulePriority = _WmanIf2fBsClassifierRulePriority_Object(
    (1, 0, 8802, 16, 4, 6, 1, 2),
    _WmanIf2fBsClassifierRulePriority_Type()
)
wmanIf2fBsClassifierRulePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRulePriority.setStatus("current")


class _WmanIf2fBsClassifierRuleIpProtocol_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2fBsClassifierRuleIpProtocol_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleIpProtocol_Object = MibTableColumn
wmanIf2fBsClassifierRuleIpProtocol = _WmanIf2fBsClassifierRuleIpProtocol_Object(
    (1, 0, 8802, 16, 4, 6, 1, 3),
    _WmanIf2fBsClassifierRuleIpProtocol_Type()
)
wmanIf2fBsClassifierRuleIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleIpProtocol.setStatus("current")
_WmanIf2fBsClassifierRuleIpSourceAddr_Type = InetAddress
_WmanIf2fBsClassifierRuleIpSourceAddr_Object = MibTableColumn
wmanIf2fBsClassifierRuleIpSourceAddr = _WmanIf2fBsClassifierRuleIpSourceAddr_Object(
    (1, 0, 8802, 16, 4, 6, 1, 4),
    _WmanIf2fBsClassifierRuleIpSourceAddr_Type()
)
wmanIf2fBsClassifierRuleIpSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleIpSourceAddr.setStatus("current")
_WmanIf2fBsClassifierRuleIpSourceMask_Type = InetAddress
_WmanIf2fBsClassifierRuleIpSourceMask_Object = MibTableColumn
wmanIf2fBsClassifierRuleIpSourceMask = _WmanIf2fBsClassifierRuleIpSourceMask_Object(
    (1, 0, 8802, 16, 4, 6, 1, 5),
    _WmanIf2fBsClassifierRuleIpSourceMask_Type()
)
wmanIf2fBsClassifierRuleIpSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleIpSourceMask.setStatus("current")
_WmanIf2fBsClassifierRuleIpDestAddr_Type = InetAddress
_WmanIf2fBsClassifierRuleIpDestAddr_Object = MibTableColumn
wmanIf2fBsClassifierRuleIpDestAddr = _WmanIf2fBsClassifierRuleIpDestAddr_Object(
    (1, 0, 8802, 16, 4, 6, 1, 6),
    _WmanIf2fBsClassifierRuleIpDestAddr_Type()
)
wmanIf2fBsClassifierRuleIpDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleIpDestAddr.setStatus("current")
_WmanIf2fBsClassifierRuleIpDestMask_Type = InetAddress
_WmanIf2fBsClassifierRuleIpDestMask_Object = MibTableColumn
wmanIf2fBsClassifierRuleIpDestMask = _WmanIf2fBsClassifierRuleIpDestMask_Object(
    (1, 0, 8802, 16, 4, 6, 1, 7),
    _WmanIf2fBsClassifierRuleIpDestMask_Type()
)
wmanIf2fBsClassifierRuleIpDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleIpDestMask.setStatus("current")


class _WmanIf2fBsClassifierRuleSourcePortStart_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleSourcePortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsClassifierRuleSourcePortStart_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleSourcePortStart_Object = MibTableColumn
wmanIf2fBsClassifierRuleSourcePortStart = _WmanIf2fBsClassifierRuleSourcePortStart_Object(
    (1, 0, 8802, 16, 4, 6, 1, 8),
    _WmanIf2fBsClassifierRuleSourcePortStart_Type()
)
wmanIf2fBsClassifierRuleSourcePortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleSourcePortStart.setStatus("current")


class _WmanIf2fBsClassifierRuleSourcePortEnd_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsClassifierRuleSourcePortEnd_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleSourcePortEnd_Object = MibTableColumn
wmanIf2fBsClassifierRuleSourcePortEnd = _WmanIf2fBsClassifierRuleSourcePortEnd_Object(
    (1, 0, 8802, 16, 4, 6, 1, 9),
    _WmanIf2fBsClassifierRuleSourcePortEnd_Type()
)
wmanIf2fBsClassifierRuleSourcePortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleSourcePortEnd.setStatus("current")


class _WmanIf2fBsClassifierRuleDestPortStart_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsClassifierRuleDestPortStart_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleDestPortStart_Object = MibTableColumn
wmanIf2fBsClassifierRuleDestPortStart = _WmanIf2fBsClassifierRuleDestPortStart_Object(
    (1, 0, 8802, 16, 4, 6, 1, 10),
    _WmanIf2fBsClassifierRuleDestPortStart_Type()
)
wmanIf2fBsClassifierRuleDestPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleDestPortStart.setStatus("current")


class _WmanIf2fBsClassifierRuleDestPortEnd_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsClassifierRuleDestPortEnd_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleDestPortEnd_Object = MibTableColumn
wmanIf2fBsClassifierRuleDestPortEnd = _WmanIf2fBsClassifierRuleDestPortEnd_Object(
    (1, 0, 8802, 16, 4, 6, 1, 11),
    _WmanIf2fBsClassifierRuleDestPortEnd_Type()
)
wmanIf2fBsClassifierRuleDestPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleDestPortEnd.setStatus("current")
_WmanIf2fBsClassifierRuleDestMacAddr_Type = MacAddress
_WmanIf2fBsClassifierRuleDestMacAddr_Object = MibTableColumn
wmanIf2fBsClassifierRuleDestMacAddr = _WmanIf2fBsClassifierRuleDestMacAddr_Object(
    (1, 0, 8802, 16, 4, 6, 1, 12),
    _WmanIf2fBsClassifierRuleDestMacAddr_Type()
)
wmanIf2fBsClassifierRuleDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleDestMacAddr.setStatus("current")
_WmanIf2fBsClassifierRuleDestMacMask_Type = MacAddress
_WmanIf2fBsClassifierRuleDestMacMask_Object = MibTableColumn
wmanIf2fBsClassifierRuleDestMacMask = _WmanIf2fBsClassifierRuleDestMacMask_Object(
    (1, 0, 8802, 16, 4, 6, 1, 13),
    _WmanIf2fBsClassifierRuleDestMacMask_Type()
)
wmanIf2fBsClassifierRuleDestMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleDestMacMask.setStatus("current")
_WmanIf2fBsClassifierRuleSourceMacAddr_Type = MacAddress
_WmanIf2fBsClassifierRuleSourceMacAddr_Object = MibTableColumn
wmanIf2fBsClassifierRuleSourceMacAddr = _WmanIf2fBsClassifierRuleSourceMacAddr_Object(
    (1, 0, 8802, 16, 4, 6, 1, 14),
    _WmanIf2fBsClassifierRuleSourceMacAddr_Type()
)
wmanIf2fBsClassifierRuleSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleSourceMacAddr.setStatus("current")
_WmanIf2fBsClassifierRuleSourceMacMask_Type = MacAddress
_WmanIf2fBsClassifierRuleSourceMacMask_Object = MibTableColumn
wmanIf2fBsClassifierRuleSourceMacMask = _WmanIf2fBsClassifierRuleSourceMacMask_Object(
    (1, 0, 8802, 16, 4, 6, 1, 15),
    _WmanIf2fBsClassifierRuleSourceMacMask_Type()
)
wmanIf2fBsClassifierRuleSourceMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleSourceMacMask.setStatus("current")
_WmanIf2fBsClassifierRuleEnetProtocolTyp_Type = WmanIf2TcEthernetType
_WmanIf2fBsClassifierRuleEnetProtocolTyp_Object = MibTableColumn
wmanIf2fBsClassifierRuleEnetProtocolTyp = _WmanIf2fBsClassifierRuleEnetProtocolTyp_Object(
    (1, 0, 8802, 16, 4, 6, 1, 16),
    _WmanIf2fBsClassifierRuleEnetProtocolTyp_Type()
)
wmanIf2fBsClassifierRuleEnetProtocolTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleEnetProtocolTyp.setStatus("current")


class _WmanIf2fBsClassifierRuleEnetProtocol_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIf2fBsClassifierRuleEnetProtocol_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleEnetProtocol_Object = MibTableColumn
wmanIf2fBsClassifierRuleEnetProtocol = _WmanIf2fBsClassifierRuleEnetProtocol_Object(
    (1, 0, 8802, 16, 4, 6, 1, 17),
    _WmanIf2fBsClassifierRuleEnetProtocol_Type()
)
wmanIf2fBsClassifierRuleEnetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleEnetProtocol.setStatus("current")


class _WmanIf2fBsClassifierRuleUserPriLow_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2fBsClassifierRuleUserPriLow_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleUserPriLow_Object = MibTableColumn
wmanIf2fBsClassifierRuleUserPriLow = _WmanIf2fBsClassifierRuleUserPriLow_Object(
    (1, 0, 8802, 16, 4, 6, 1, 18),
    _WmanIf2fBsClassifierRuleUserPriLow_Type()
)
wmanIf2fBsClassifierRuleUserPriLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleUserPriLow.setStatus("current")


class _WmanIf2fBsClassifierRuleUserPriHigh_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIf2fBsClassifierRuleUserPriHigh_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleUserPriHigh_Object = MibTableColumn
wmanIf2fBsClassifierRuleUserPriHigh = _WmanIf2fBsClassifierRuleUserPriHigh_Object(
    (1, 0, 8802, 16, 4, 6, 1, 19),
    _WmanIf2fBsClassifierRuleUserPriHigh_Type()
)
wmanIf2fBsClassifierRuleUserPriHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleUserPriHigh.setStatus("current")


class _WmanIf2fBsClassifierRuleVlanId_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WmanIf2fBsClassifierRuleVlanId_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleVlanId_Object = MibTableColumn
wmanIf2fBsClassifierRuleVlanId = _WmanIf2fBsClassifierRuleVlanId_Object(
    (1, 0, 8802, 16, 4, 6, 1, 20),
    _WmanIf2fBsClassifierRuleVlanId_Type()
)
wmanIf2fBsClassifierRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleVlanId.setStatus("current")


class _WmanIf2fBsClassifierRuleAssociatedPhsi_Type(Integer32):
    """Custom type wmanIf2fBsClassifierRuleAssociatedPhsi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2fBsClassifierRuleAssociatedPhsi_Type.__name__ = "Integer32"
_WmanIf2fBsClassifierRuleAssociatedPhsi_Object = MibTableColumn
wmanIf2fBsClassifierRuleAssociatedPhsi = _WmanIf2fBsClassifierRuleAssociatedPhsi_Object(
    (1, 0, 8802, 16, 4, 6, 1, 21),
    _WmanIf2fBsClassifierRuleAssociatedPhsi_Type()
)
wmanIf2fBsClassifierRuleAssociatedPhsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleAssociatedPhsi.setStatus("current")
_WmanIf2fBsClassifierRuleIpv6FlowLabel_Type = WmanIf2TcIpv6FlowLabel
_WmanIf2fBsClassifierRuleIpv6FlowLabel_Object = MibTableColumn
wmanIf2fBsClassifierRuleIpv6FlowLabel = _WmanIf2fBsClassifierRuleIpv6FlowLabel_Object(
    (1, 0, 8802, 16, 4, 6, 1, 22),
    _WmanIf2fBsClassifierRuleIpv6FlowLabel_Type()
)
wmanIf2fBsClassifierRuleIpv6FlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleIpv6FlowLabel.setStatus("current")
_WmanIf2fBsClassifierRuleActionRule_Type = WmanIf2TcActionRule
_WmanIf2fBsClassifierRuleActionRule_Object = MibTableColumn
wmanIf2fBsClassifierRuleActionRule = _WmanIf2fBsClassifierRuleActionRule_Object(
    (1, 0, 8802, 16, 4, 6, 1, 23),
    _WmanIf2fBsClassifierRuleActionRule_Type()
)
wmanIf2fBsClassifierRuleActionRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleActionRule.setStatus("current")
_WmanIf2fBsClassifierRuleIpTypeOfService_Type = WmanIf2TcIpTypOfServ
_WmanIf2fBsClassifierRuleIpTypeOfService_Object = MibTableColumn
wmanIf2fBsClassifierRuleIpTypeOfService = _WmanIf2fBsClassifierRuleIpTypeOfService_Object(
    (1, 0, 8802, 16, 4, 6, 1, 24),
    _WmanIf2fBsClassifierRuleIpTypeOfService_Type()
)
wmanIf2fBsClassifierRuleIpTypeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleIpTypeOfService.setStatus("current")
_WmanIf2fBsClassifierRuleBitMap_Type = WmanIf2TcClassifierMap
_WmanIf2fBsClassifierRuleBitMap_Object = MibTableColumn
wmanIf2fBsClassifierRuleBitMap = _WmanIf2fBsClassifierRuleBitMap_Object(
    (1, 0, 8802, 16, 4, 6, 1, 25),
    _WmanIf2fBsClassifierRuleBitMap_Type()
)
wmanIf2fBsClassifierRuleBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRuleBitMap.setStatus("current")
_WmanIf2fBsClassifierRulePkts_Type = Counter64
_WmanIf2fBsClassifierRulePkts_Object = MibTableColumn
wmanIf2fBsClassifierRulePkts = _WmanIf2fBsClassifierRulePkts_Object(
    (1, 0, 8802, 16, 4, 6, 1, 26),
    _WmanIf2fBsClassifierRulePkts_Type()
)
wmanIf2fBsClassifierRulePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsClassifierRulePkts.setStatus("current")
_WmanIf2fBsPhsRuleTable_Object = MibTable
wmanIf2fBsPhsRuleTable = _WmanIf2fBsPhsRuleTable_Object(
    (1, 0, 8802, 16, 4, 7)
)
if mibBuilder.loadTexts:
    wmanIf2fBsPhsRuleTable.setStatus("current")
_WmanIf2fBsPhsRuleEntry_Object = MibTableRow
wmanIf2fBsPhsRuleEntry = _WmanIf2fBsPhsRuleEntry_Object(
    (1, 0, 8802, 16, 4, 7, 1)
)
wmanIf2fBsPhsRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfMacAddress"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsSfCid"),
    (0, "WMAN-IF2F-BS-MIB", "wmanIf2fBsPhsRulePhsIndex"),
)
if mibBuilder.loadTexts:
    wmanIf2fBsPhsRuleEntry.setStatus("current")


class _WmanIf2fBsPhsRulePhsIndex_Type(Integer32):
    """Custom type wmanIf2fBsPhsRulePhsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIf2fBsPhsRulePhsIndex_Type.__name__ = "Integer32"
_WmanIf2fBsPhsRulePhsIndex_Object = MibTableColumn
wmanIf2fBsPhsRulePhsIndex = _WmanIf2fBsPhsRulePhsIndex_Object(
    (1, 0, 8802, 16, 4, 7, 1, 1),
    _WmanIf2fBsPhsRulePhsIndex_Type()
)
wmanIf2fBsPhsRulePhsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIf2fBsPhsRulePhsIndex.setStatus("current")


class _WmanIf2fBsPhsRulePhsField_Type(OctetString):
    """Custom type wmanIf2fBsPhsRulePhsField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2fBsPhsRulePhsField_Type.__name__ = "OctetString"
_WmanIf2fBsPhsRulePhsField_Object = MibTableColumn
wmanIf2fBsPhsRulePhsField = _WmanIf2fBsPhsRulePhsField_Object(
    (1, 0, 8802, 16, 4, 7, 1, 2),
    _WmanIf2fBsPhsRulePhsField_Type()
)
wmanIf2fBsPhsRulePhsField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsPhsRulePhsField.setStatus("current")


class _WmanIf2fBsPhsRulePhsMask_Type(OctetString):
    """Custom type wmanIf2fBsPhsRulePhsMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_WmanIf2fBsPhsRulePhsMask_Type.__name__ = "OctetString"
_WmanIf2fBsPhsRulePhsMask_Object = MibTableColumn
wmanIf2fBsPhsRulePhsMask = _WmanIf2fBsPhsRulePhsMask_Object(
    (1, 0, 8802, 16, 4, 7, 1, 3),
    _WmanIf2fBsPhsRulePhsMask_Type()
)
wmanIf2fBsPhsRulePhsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsPhsRulePhsMask.setStatus("current")


class _WmanIf2fBsPhsRulePhsSize_Type(Integer32):
    """Custom type wmanIf2fBsPhsRulePhsSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIf2fBsPhsRulePhsSize_Type.__name__ = "Integer32"
_WmanIf2fBsPhsRulePhsSize_Object = MibTableColumn
wmanIf2fBsPhsRulePhsSize = _WmanIf2fBsPhsRulePhsSize_Object(
    (1, 0, 8802, 16, 4, 7, 1, 4),
    _WmanIf2fBsPhsRulePhsSize_Type()
)
wmanIf2fBsPhsRulePhsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsPhsRulePhsSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIf2fBsPhsRulePhsSize.setUnits("byte")


class _WmanIf2fBsPhsRulePhsVerify_Type(WmanIf2TcPhsRuleVerify):
    """Custom type wmanIf2fBsPhsRulePhsVerify based on WmanIf2TcPhsRuleVerify"""
    defaultValue = 0


_WmanIf2fBsPhsRulePhsVerify_Type.__name__ = "WmanIf2TcPhsRuleVerify"
_WmanIf2fBsPhsRulePhsVerify_Object = MibTableColumn
wmanIf2fBsPhsRulePhsVerify = _WmanIf2fBsPhsRulePhsVerify_Object(
    (1, 0, 8802, 16, 4, 7, 1, 5),
    _WmanIf2fBsPhsRulePhsVerify_Type()
)
wmanIf2fBsPhsRulePhsVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIf2fBsPhsRulePhsVerify.setStatus("current")
_WmanIf2fBsConformance_ObjectIdentity = ObjectIdentity
wmanIf2fBsConformance = _WmanIf2fBsConformance_ObjectIdentity(
    (1, 0, 8802, 16, 4, 8)
)
_WmanIf2fBsMibGroups_ObjectIdentity = ObjectIdentity
wmanIf2fBsMibGroups = _WmanIf2fBsMibGroups_ObjectIdentity(
    (1, 0, 8802, 16, 4, 8, 1)
)
_WmanIf2fBsMibCompliances_ObjectIdentity = ObjectIdentity
wmanIf2fBsMibCompliances = _WmanIf2fBsMibCompliances_ObjectIdentity(
    (1, 0, 8802, 16, 4, 8, 2)
)

# Managed Objects groups

wmanIf2fBsMibProvSfGroup = ObjectGroup(
    (1, 0, 8802, 16, 4, 8, 1, 1)
)
wmanIf2fBsMibProvSfGroup.setObjects(
      *(("WMAN-IF2F-BS-MIB", "wmanIf2fBsSfDirection"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsServiceClassIndex"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsSfState"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsSfProvisionedTime"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsSfCsSpecification"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvisionedSfRowStatus"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosServiceClassName"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSTrafficPriority"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSMaxSustainedRate"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSMaxTrafficBurst"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSMinReservedRate"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSToleratedJitter"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSMaxLatency"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSFixedVsVariableSduInd"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQoSSduSize"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScSchedulingType"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScArqEnable"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScArqWindowSize"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosArqTxRetryTimeout"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosArqRxRetryTimeout"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScArqBlockLifetime"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScArqSyncLossTimeout"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScArqDeliverInOrder"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScArqRxPurgeTimeout"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScArqBlockSizeReq"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosScArqBlockSizeRsp"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosReqTxPolicy"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosFragmentSeqNumType"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosMbsService"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsQosServiceClassRowStatus"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRulePriority"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleIpProtocol"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleIpSrcAddr"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleIpSrcMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleIpDestAddr"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleIpDestMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleSrcPortStart"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleSrcPortEnd"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleDestPortStart"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleDestPortEnd"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleDestMacAddr"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleDestMacMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleSrcMacAddr"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleSrcMacMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleEnetProtType"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleEnetProtocol"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleUserPriLow"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleUserPriHigh"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleVlanId"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleIpv6FlowLabel"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleActionRule"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleIpTypeOfService"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleBitMap"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleAssociatedPhsi"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvClsfRuleRowStatus"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvPhsRulePhsField"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvPhsRulePhsMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvPhsRulePhsSize"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvPhsRulePhsVerify"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsProvPhsRuleRowStatus"))
)
if mibBuilder.loadTexts:
    wmanIf2fBsMibProvSfGroup.setStatus("current")

wmanIf2fBsMibActSfGroup = ObjectGroup(
    (1, 0, 8802, 16, 4, 8, 1, 2)
)
wmanIf2fBsMibActSfGroup.setObjects(
      *(("WMAN-IF2F-BS-MIB", "wmanIf2fBsServiceFlowDirection"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsServiceFlowState"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsTrafficPriority"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsMaxSustainedRate"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsMaxTrafficBurst"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsMinReservedRate"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsToleratedJitter"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsMaxLatency"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsFixedVsVariableSduInd"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsSduSize"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsSfSchedulingType"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsArqEnable"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsArqWindowSize"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsArqTxRetryTimeout"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsArqRxRetryTimeout"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsArqBlockLifetime"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsArqSyncLossTimeout"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsArqDeliverInOrder"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsArqRxPurgeTimeout"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsScArqBlockSizeReq"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsScArqBlockSizeRsp"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsReqTxPolicy"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsCsSpecification"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsTargetSaid"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsFragmentSeqNumType"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsMbsService"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRulePriority"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleIpProtocol"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleIpSourceAddr"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleIpSourceMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleIpDestAddr"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleIpDestMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleSourcePortStart"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleSourcePortEnd"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleDestPortStart"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleDestPortEnd"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleDestMacAddr"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleDestMacMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleSourceMacAddr"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleSourceMacMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleEnetProtocolTyp"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleEnetProtocol"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleUserPriLow"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleUserPriHigh"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleVlanId"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRulePkts"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleIpv6FlowLabel"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleActionRule"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleIpTypeOfService"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleBitMap"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsClassifierRuleAssociatedPhsi"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsPhsRulePhsField"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsPhsRulePhsMask"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsPhsRulePhsSize"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsPhsRulePhsVerify"))
)
if mibBuilder.loadTexts:
    wmanIf2fBsMibActSfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wmanIf2fBsMibCompliance = ModuleCompliance(
    (1, 0, 8802, 16, 4, 8, 2, 1)
)
wmanIf2fBsMibCompliance.setObjects(
      *(("WMAN-IF2F-BS-MIB", "wmanIf2fBsMibProvSfGroup"),
        ("WMAN-IF2F-BS-MIB", "wmanIf2fBsMibActSfGroup"))
)
if mibBuilder.loadTexts:
    wmanIf2fBsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-IF2F-BS-MIB",
    **{"WmanIf2fServClassName": WmanIf2fServClassName,
       "wmanIf2fBsMib": wmanIf2fBsMib,
       "wmanIf2fBsProvServiceFlowTable": wmanIf2fBsProvServiceFlowTable,
       "wmanIf2fBsProvServiceFlowEntry": wmanIf2fBsProvServiceFlowEntry,
       "wmanIf2fBsSsProvMacAddress": wmanIf2fBsSsProvMacAddress,
       "wmanIf2fBsSfId": wmanIf2fBsSfId,
       "wmanIf2fBsSfDirection": wmanIf2fBsSfDirection,
       "wmanIf2fBsServiceClassIndex": wmanIf2fBsServiceClassIndex,
       "wmanIf2fBsSfState": wmanIf2fBsSfState,
       "wmanIf2fBsSfProvisionedTime": wmanIf2fBsSfProvisionedTime,
       "wmanIf2fBsSfCsSpecification": wmanIf2fBsSfCsSpecification,
       "wmanIf2fBsProvisionedSfRowStatus": wmanIf2fBsProvisionedSfRowStatus,
       "wmanIf2fBsProvServiceClassTable": wmanIf2fBsProvServiceClassTable,
       "wmanIf2fBsProvServiceClassEntry": wmanIf2fBsProvServiceClassEntry,
       "wmanIf2fBsQoSProfileIndex": wmanIf2fBsQoSProfileIndex,
       "wmanIf2fBsQosServiceClassName": wmanIf2fBsQosServiceClassName,
       "wmanIf2fBsQoSTrafficPriority": wmanIf2fBsQoSTrafficPriority,
       "wmanIf2fBsQoSMaxSustainedRate": wmanIf2fBsQoSMaxSustainedRate,
       "wmanIf2fBsQoSMaxTrafficBurst": wmanIf2fBsQoSMaxTrafficBurst,
       "wmanIf2fBsQoSMinReservedRate": wmanIf2fBsQoSMinReservedRate,
       "wmanIf2fBsQoSToleratedJitter": wmanIf2fBsQoSToleratedJitter,
       "wmanIf2fBsQoSMaxLatency": wmanIf2fBsQoSMaxLatency,
       "wmanIf2fBsQoSFixedVsVariableSduInd": wmanIf2fBsQoSFixedVsVariableSduInd,
       "wmanIf2fBsQoSSduSize": wmanIf2fBsQoSSduSize,
       "wmanIf2fBsQosScSchedulingType": wmanIf2fBsQosScSchedulingType,
       "wmanIf2fBsQosScArqEnable": wmanIf2fBsQosScArqEnable,
       "wmanIf2fBsQosScArqWindowSize": wmanIf2fBsQosScArqWindowSize,
       "wmanIf2fBsQosArqTxRetryTimeout": wmanIf2fBsQosArqTxRetryTimeout,
       "wmanIf2fBsQosArqRxRetryTimeout": wmanIf2fBsQosArqRxRetryTimeout,
       "wmanIf2fBsQosScArqBlockLifetime": wmanIf2fBsQosScArqBlockLifetime,
       "wmanIf2fBsQosScArqSyncLossTimeout": wmanIf2fBsQosScArqSyncLossTimeout,
       "wmanIf2fBsQosScArqDeliverInOrder": wmanIf2fBsQosScArqDeliverInOrder,
       "wmanIf2fBsQosScArqRxPurgeTimeout": wmanIf2fBsQosScArqRxPurgeTimeout,
       "wmanIf2fBsQosScArqBlockSizeReq": wmanIf2fBsQosScArqBlockSizeReq,
       "wmanIf2fBsQosScArqBlockSizeRsp": wmanIf2fBsQosScArqBlockSizeRsp,
       "wmanIf2fBsQosReqTxPolicy": wmanIf2fBsQosReqTxPolicy,
       "wmanIf2fBsQosFragmentSeqNumType": wmanIf2fBsQosFragmentSeqNumType,
       "wmanIf2fBsQosMbsService": wmanIf2fBsQosMbsService,
       "wmanIf2fBsQosServiceClassRowStatus": wmanIf2fBsQosServiceClassRowStatus,
       "wmanIf2fBsServiceFlowTable": wmanIf2fBsServiceFlowTable,
       "wmanIf2fBsServiceFlowEntry": wmanIf2fBsServiceFlowEntry,
       "wmanIf2fBsSfMacAddress": wmanIf2fBsSfMacAddress,
       "wmanIf2fBsSfCid": wmanIf2fBsSfCid,
       "wmanIf2fBsServiceFlowDirection": wmanIf2fBsServiceFlowDirection,
       "wmanIf2fBsServiceFlowState": wmanIf2fBsServiceFlowState,
       "wmanIf2fBsTrafficPriority": wmanIf2fBsTrafficPriority,
       "wmanIf2fBsMaxSustainedRate": wmanIf2fBsMaxSustainedRate,
       "wmanIf2fBsMaxTrafficBurst": wmanIf2fBsMaxTrafficBurst,
       "wmanIf2fBsMinReservedRate": wmanIf2fBsMinReservedRate,
       "wmanIf2fBsToleratedJitter": wmanIf2fBsToleratedJitter,
       "wmanIf2fBsMaxLatency": wmanIf2fBsMaxLatency,
       "wmanIf2fBsFixedVsVariableSduInd": wmanIf2fBsFixedVsVariableSduInd,
       "wmanIf2fBsSduSize": wmanIf2fBsSduSize,
       "wmanIf2fBsSfSchedulingType": wmanIf2fBsSfSchedulingType,
       "wmanIf2fBsArqEnable": wmanIf2fBsArqEnable,
       "wmanIf2fBsArqWindowSize": wmanIf2fBsArqWindowSize,
       "wmanIf2fBsArqTxRetryTimeout": wmanIf2fBsArqTxRetryTimeout,
       "wmanIf2fBsArqRxRetryTimeout": wmanIf2fBsArqRxRetryTimeout,
       "wmanIf2fBsArqBlockLifetime": wmanIf2fBsArqBlockLifetime,
       "wmanIf2fBsArqSyncLossTimeout": wmanIf2fBsArqSyncLossTimeout,
       "wmanIf2fBsArqDeliverInOrder": wmanIf2fBsArqDeliverInOrder,
       "wmanIf2fBsArqRxPurgeTimeout": wmanIf2fBsArqRxPurgeTimeout,
       "wmanIf2fBsScArqBlockSizeReq": wmanIf2fBsScArqBlockSizeReq,
       "wmanIf2fBsScArqBlockSizeRsp": wmanIf2fBsScArqBlockSizeRsp,
       "wmanIf2fBsReqTxPolicy": wmanIf2fBsReqTxPolicy,
       "wmanIf2fBsCsSpecification": wmanIf2fBsCsSpecification,
       "wmanIf2fBsTargetSaid": wmanIf2fBsTargetSaid,
       "wmanIf2fBsFragmentSeqNumType": wmanIf2fBsFragmentSeqNumType,
       "wmanIf2fBsMbsService": wmanIf2fBsMbsService,
       "wmanIf2fBsProvClassifierRuleTable": wmanIf2fBsProvClassifierRuleTable,
       "wmanIf2fBsProvClassifierRuleEntry": wmanIf2fBsProvClassifierRuleEntry,
       "wmanIf2fBsProvClsfRuleIndex": wmanIf2fBsProvClsfRuleIndex,
       "wmanIf2fBsProvClsfRulePriority": wmanIf2fBsProvClsfRulePriority,
       "wmanIf2fBsProvClsfRuleIpProtocol": wmanIf2fBsProvClsfRuleIpProtocol,
       "wmanIf2fBsProvClsfRuleIpSrcAddr": wmanIf2fBsProvClsfRuleIpSrcAddr,
       "wmanIf2fBsProvClsfRuleIpSrcMask": wmanIf2fBsProvClsfRuleIpSrcMask,
       "wmanIf2fBsProvClsfRuleIpDestAddr": wmanIf2fBsProvClsfRuleIpDestAddr,
       "wmanIf2fBsProvClsfRuleIpDestMask": wmanIf2fBsProvClsfRuleIpDestMask,
       "wmanIf2fBsProvClsfRuleSrcPortStart": wmanIf2fBsProvClsfRuleSrcPortStart,
       "wmanIf2fBsProvClsfRuleSrcPortEnd": wmanIf2fBsProvClsfRuleSrcPortEnd,
       "wmanIf2fBsProvClsfRuleDestPortStart": wmanIf2fBsProvClsfRuleDestPortStart,
       "wmanIf2fBsProvClsfRuleDestPortEnd": wmanIf2fBsProvClsfRuleDestPortEnd,
       "wmanIf2fBsProvClsfRuleDestMacAddr": wmanIf2fBsProvClsfRuleDestMacAddr,
       "wmanIf2fBsProvClsfRuleDestMacMask": wmanIf2fBsProvClsfRuleDestMacMask,
       "wmanIf2fBsProvClsfRuleSrcMacAddr": wmanIf2fBsProvClsfRuleSrcMacAddr,
       "wmanIf2fBsProvClsfRuleSrcMacMask": wmanIf2fBsProvClsfRuleSrcMacMask,
       "wmanIf2fBsProvClsfRuleEnetProtType": wmanIf2fBsProvClsfRuleEnetProtType,
       "wmanIf2fBsProvClsfRuleEnetProtocol": wmanIf2fBsProvClsfRuleEnetProtocol,
       "wmanIf2fBsProvClsfRuleUserPriLow": wmanIf2fBsProvClsfRuleUserPriLow,
       "wmanIf2fBsProvClsfRuleUserPriHigh": wmanIf2fBsProvClsfRuleUserPriHigh,
       "wmanIf2fBsProvClsfRuleVlanId": wmanIf2fBsProvClsfRuleVlanId,
       "wmanIf2fBsProvClsfRuleAssociatedPhsi": wmanIf2fBsProvClsfRuleAssociatedPhsi,
       "wmanIf2fBsProvClsfRuleIpv6FlowLabel": wmanIf2fBsProvClsfRuleIpv6FlowLabel,
       "wmanIf2fBsProvClsfRuleActionRule": wmanIf2fBsProvClsfRuleActionRule,
       "wmanIf2fBsProvClsfRuleIpTypeOfService": wmanIf2fBsProvClsfRuleIpTypeOfService,
       "wmanIf2fBsProvClsfRuleBitMap": wmanIf2fBsProvClsfRuleBitMap,
       "wmanIf2fBsProvClsfRuleRowStatus": wmanIf2fBsProvClsfRuleRowStatus,
       "wmanIf2fBsProvPhsRuleTable": wmanIf2fBsProvPhsRuleTable,
       "wmanIf2fBsProvPhsRuleEntry": wmanIf2fBsProvPhsRuleEntry,
       "wmanIf2fBsProvPhsRulePhsIndex": wmanIf2fBsProvPhsRulePhsIndex,
       "wmanIf2fBsProvPhsRulePhsField": wmanIf2fBsProvPhsRulePhsField,
       "wmanIf2fBsProvPhsRulePhsMask": wmanIf2fBsProvPhsRulePhsMask,
       "wmanIf2fBsProvPhsRulePhsSize": wmanIf2fBsProvPhsRulePhsSize,
       "wmanIf2fBsProvPhsRulePhsVerify": wmanIf2fBsProvPhsRulePhsVerify,
       "wmanIf2fBsProvPhsRuleRowStatus": wmanIf2fBsProvPhsRuleRowStatus,
       "wmanIf2fBsClassifierRuleTable": wmanIf2fBsClassifierRuleTable,
       "wmanIf2fBsClassifierRuleEntry": wmanIf2fBsClassifierRuleEntry,
       "wmanIf2fBsClassifierRuleIndex": wmanIf2fBsClassifierRuleIndex,
       "wmanIf2fBsClassifierRulePriority": wmanIf2fBsClassifierRulePriority,
       "wmanIf2fBsClassifierRuleIpProtocol": wmanIf2fBsClassifierRuleIpProtocol,
       "wmanIf2fBsClassifierRuleIpSourceAddr": wmanIf2fBsClassifierRuleIpSourceAddr,
       "wmanIf2fBsClassifierRuleIpSourceMask": wmanIf2fBsClassifierRuleIpSourceMask,
       "wmanIf2fBsClassifierRuleIpDestAddr": wmanIf2fBsClassifierRuleIpDestAddr,
       "wmanIf2fBsClassifierRuleIpDestMask": wmanIf2fBsClassifierRuleIpDestMask,
       "wmanIf2fBsClassifierRuleSourcePortStart": wmanIf2fBsClassifierRuleSourcePortStart,
       "wmanIf2fBsClassifierRuleSourcePortEnd": wmanIf2fBsClassifierRuleSourcePortEnd,
       "wmanIf2fBsClassifierRuleDestPortStart": wmanIf2fBsClassifierRuleDestPortStart,
       "wmanIf2fBsClassifierRuleDestPortEnd": wmanIf2fBsClassifierRuleDestPortEnd,
       "wmanIf2fBsClassifierRuleDestMacAddr": wmanIf2fBsClassifierRuleDestMacAddr,
       "wmanIf2fBsClassifierRuleDestMacMask": wmanIf2fBsClassifierRuleDestMacMask,
       "wmanIf2fBsClassifierRuleSourceMacAddr": wmanIf2fBsClassifierRuleSourceMacAddr,
       "wmanIf2fBsClassifierRuleSourceMacMask": wmanIf2fBsClassifierRuleSourceMacMask,
       "wmanIf2fBsClassifierRuleEnetProtocolTyp": wmanIf2fBsClassifierRuleEnetProtocolTyp,
       "wmanIf2fBsClassifierRuleEnetProtocol": wmanIf2fBsClassifierRuleEnetProtocol,
       "wmanIf2fBsClassifierRuleUserPriLow": wmanIf2fBsClassifierRuleUserPriLow,
       "wmanIf2fBsClassifierRuleUserPriHigh": wmanIf2fBsClassifierRuleUserPriHigh,
       "wmanIf2fBsClassifierRuleVlanId": wmanIf2fBsClassifierRuleVlanId,
       "wmanIf2fBsClassifierRuleAssociatedPhsi": wmanIf2fBsClassifierRuleAssociatedPhsi,
       "wmanIf2fBsClassifierRuleIpv6FlowLabel": wmanIf2fBsClassifierRuleIpv6FlowLabel,
       "wmanIf2fBsClassifierRuleActionRule": wmanIf2fBsClassifierRuleActionRule,
       "wmanIf2fBsClassifierRuleIpTypeOfService": wmanIf2fBsClassifierRuleIpTypeOfService,
       "wmanIf2fBsClassifierRuleBitMap": wmanIf2fBsClassifierRuleBitMap,
       "wmanIf2fBsClassifierRulePkts": wmanIf2fBsClassifierRulePkts,
       "wmanIf2fBsPhsRuleTable": wmanIf2fBsPhsRuleTable,
       "wmanIf2fBsPhsRuleEntry": wmanIf2fBsPhsRuleEntry,
       "wmanIf2fBsPhsRulePhsIndex": wmanIf2fBsPhsRulePhsIndex,
       "wmanIf2fBsPhsRulePhsField": wmanIf2fBsPhsRulePhsField,
       "wmanIf2fBsPhsRulePhsMask": wmanIf2fBsPhsRulePhsMask,
       "wmanIf2fBsPhsRulePhsSize": wmanIf2fBsPhsRulePhsSize,
       "wmanIf2fBsPhsRulePhsVerify": wmanIf2fBsPhsRulePhsVerify,
       "wmanIf2fBsConformance": wmanIf2fBsConformance,
       "wmanIf2fBsMibGroups": wmanIf2fBsMibGroups,
       "wmanIf2fBsMibProvSfGroup": wmanIf2fBsMibProvSfGroup,
       "wmanIf2fBsMibActSfGroup": wmanIf2fBsMibActSfGroup,
       "wmanIf2fBsMibCompliances": wmanIf2fBsMibCompliances,
       "wmanIf2fBsMibCompliance": wmanIf2fBsMibCompliance}
)
