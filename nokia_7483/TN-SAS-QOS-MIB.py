# SNMP MIB module (TN-SAS-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-SAS-QOS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:36 2025
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnNetworkPolicyEntry,
 tnNetworkPolicyIndex,
 tnNetworkQueueEntry,
 tnPortSchedulerPlcyEntry,
 tnSapIngressEntry,
 tnSapIngressFCEntry,
 tnSapIngressIndex,
 tnSlopePolicy,
 tnSlopePolicyEntry) = mibBuilder.importSymbols(
    "TN-QOS-MIB",
    "tnNetworkPolicyEntry",
    "tnNetworkPolicyIndex",
    "tnNetworkQueueEntry",
    "tnPortSchedulerPlcyEntry",
    "tnSapIngressEntry",
    "tnSapIngressFCEntry",
    "tnSapIngressIndex",
    "tnSlopePolicy",
    "tnSlopePolicyEntry")

(tnSapEncapValue,
 tnSapPortId) = mibBuilder.importSymbols(
    "TN-SAP-MIB",
    "tnSapEncapValue",
    "tnSapPortId")

(tnSvcId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "tnSvcId")

(Dot1PPriority,
 TAdaptationRule,
 TBurstSize,
 TCIRRate,
 TDSCPNameOrEmpty,
 TEgressQueueId,
 TFCName,
 TItemDescription,
 TItemScope,
 TLspExpValue,
 TMeterMode,
 TMplsLspExpProfMapID,
 TNamedItem,
 TNetworkIngressMeterId,
 TPIRRate,
 TPlcyMode,
 TPolicyID,
 TQWeight,
 TQueueId,
 TSapIngressMeterId) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "Dot1PPriority",
    "TAdaptationRule",
    "TBurstSize",
    "TCIRRate",
    "TDSCPNameOrEmpty",
    "TEgressQueueId",
    "TFCName",
    "TItemDescription",
    "TItemScope",
    "TLspExpValue",
    "TMeterMode",
    "TMplsLspExpProfMapID",
    "TNamedItem",
    "TNetworkIngressMeterId",
    "TPIRRate",
    "TPlcyMode",
    "TPolicyID",
    "TQWeight",
    "TQueueId",
    "TSapIngressMeterId")

(tnSASModules,
 tnSASObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSASModules",
    "tnSASObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnSASQosMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tnSASQosMIBModule.setRevisions(
        ("1913-08-22 00:00",
         "1913-08-16 00:00",
         "1912-12-05 00:00",
         "1912-09-01 00:00",
         "1908-01-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TAccessEgressPolicyID(TPolicyID):
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



class TIngressBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(4, 2146959),
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

_TnSASQosObjects_ObjectIdentity = ObjectIdentity
tnSASQosObjects = _TnSASQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1)
)
_TnAccessEgressObjects_ObjectIdentity = ObjectIdentity
tnAccessEgressObjects = _TnAccessEgressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1)
)
_TnAccessEgressTable_Object = MibTable
tnAccessEgressTable = _TnAccessEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnAccessEgressTable.setStatus("current")
_TnAccessEgressEntry_Object = MibTableRow
tnAccessEgressEntry = _TnAccessEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1)
)
tnAccessEgressEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SAS-QOS-MIB", "tnAccessEgressIndex"),
)
if mibBuilder.loadTexts:
    tnAccessEgressEntry.setStatus("current")
_TnAccessEgressIndex_Type = TAccessEgressPolicyID
_TnAccessEgressIndex_Object = MibTableColumn
tnAccessEgressIndex = _TnAccessEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1, 1),
    _TnAccessEgressIndex_Type()
)
tnAccessEgressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAccessEgressIndex.setStatus("current")
_TnAccessEgressRowStatus_Type = RowStatus
_TnAccessEgressRowStatus_Object = MibTableColumn
tnAccessEgressRowStatus = _TnAccessEgressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1, 2),
    _TnAccessEgressRowStatus_Type()
)
tnAccessEgressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressRowStatus.setStatus("current")


class _TnAccessEgressScope_Type(TItemScope):
    """Custom type tnAccessEgressScope based on TItemScope"""
    defaultValue = 2


_TnAccessEgressScope_Type.__name__ = "TItemScope"
_TnAccessEgressScope_Object = MibTableColumn
tnAccessEgressScope = _TnAccessEgressScope_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1, 3),
    _TnAccessEgressScope_Type()
)
tnAccessEgressScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressScope.setStatus("current")


class _TnAccessEgressDescription_Type(TItemDescription):
    """Custom type tnAccessEgressDescription based on TItemDescription"""
    defaultHexValue = ""


_TnAccessEgressDescription_Type.__name__ = "TItemDescription"
_TnAccessEgressDescription_Object = MibTableColumn
tnAccessEgressDescription = _TnAccessEgressDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1, 4),
    _TnAccessEgressDescription_Type()
)
tnAccessEgressDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressDescription.setStatus("current")
_TnAccessEgressLastChanged_Type = TimeStamp
_TnAccessEgressLastChanged_Object = MibTableColumn
tnAccessEgressLastChanged = _TnAccessEgressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1, 5),
    _TnAccessEgressLastChanged_Type()
)
tnAccessEgressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessEgressLastChanged.setStatus("current")


class _TnAccessEgressRemark_Type(TruthValue):
    """Custom type tnAccessEgressRemark based on TruthValue"""
    defaultValue = 2


_TnAccessEgressRemark_Type.__name__ = "TruthValue"
_TnAccessEgressRemark_Object = MibTableColumn
tnAccessEgressRemark = _TnAccessEgressRemark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1, 6),
    _TnAccessEgressRemark_Type()
)
tnAccessEgressRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressRemark.setStatus("current")


class _TnAccessEgressRemarkPolicyId_Type(TRemarkPolicyID):
    """Custom type tnAccessEgressRemarkPolicyId based on TRemarkPolicyID"""
    defaultValue = 1


_TnAccessEgressRemarkPolicyId_Type.__name__ = "TRemarkPolicyID"
_TnAccessEgressRemarkPolicyId_Object = MibTableColumn
tnAccessEgressRemarkPolicyId = _TnAccessEgressRemarkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1, 7),
    _TnAccessEgressRemarkPolicyId_Type()
)
tnAccessEgressRemarkPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressRemarkPolicyId.setStatus("current")


class _TnAccessEgressRemarkType_Type(Integer32):
    """Custom type tnAccessEgressRemarkType based on Integer32"""
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


_TnAccessEgressRemarkType_Type.__name__ = "Integer32"
_TnAccessEgressRemarkType_Object = MibTableColumn
tnAccessEgressRemarkType = _TnAccessEgressRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 1, 1, 8),
    _TnAccessEgressRemarkType_Type()
)
tnAccessEgressRemarkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressRemarkType.setStatus("current")
_TnAccessEgressQueueTable_Object = MibTable
tnAccessEgressQueueTable = _TnAccessEgressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnAccessEgressQueueTable.setStatus("current")
_TnAccessEgressQueueEntry_Object = MibTableRow
tnAccessEgressQueueEntry = _TnAccessEgressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1)
)
tnAccessEgressQueueEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SAS-QOS-MIB", "tnAccessEgressIndex"),
    (0, "TN-SAS-QOS-MIB", "tnAccessEgressQueueIndex"),
)
if mibBuilder.loadTexts:
    tnAccessEgressQueueEntry.setStatus("current")


class _TnAccessEgressQueueIndex_Type(TEgressQueueId):
    """Custom type tnAccessEgressQueueIndex based on TEgressQueueId"""
    subtypeSpec = TEgressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnAccessEgressQueueIndex_Type.__name__ = "TEgressQueueId"
_TnAccessEgressQueueIndex_Object = MibTableColumn
tnAccessEgressQueueIndex = _TnAccessEgressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 1),
    _TnAccessEgressQueueIndex_Type()
)
tnAccessEgressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAccessEgressQueueIndex.setStatus("current")
_TnAccessEgressQueueRowStatus_Type = RowStatus
_TnAccessEgressQueueRowStatus_Object = MibTableColumn
tnAccessEgressQueueRowStatus = _TnAccessEgressQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 2),
    _TnAccessEgressQueueRowStatus_Type()
)
tnAccessEgressQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressQueueRowStatus.setStatus("current")


class _TnAccessEgressQueueCBS_Type(TBurstSize):
    """Custom type tnAccessEgressQueueCBS based on TBurstSize"""
    defaultValue = -1


_TnAccessEgressQueueCBS_Type.__name__ = "TBurstSize"
_TnAccessEgressQueueCBS_Object = MibTableColumn
tnAccessEgressQueueCBS = _TnAccessEgressQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 3),
    _TnAccessEgressQueueCBS_Type()
)
tnAccessEgressQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressQueueCBS.setStatus("current")


class _TnAccessEgressQueueMBS_Type(TBurstSize):
    """Custom type tnAccessEgressQueueMBS based on TBurstSize"""
    defaultValue = -1


_TnAccessEgressQueueMBS_Type.__name__ = "TBurstSize"
_TnAccessEgressQueueMBS_Object = MibTableColumn
tnAccessEgressQueueMBS = _TnAccessEgressQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 4),
    _TnAccessEgressQueueMBS_Type()
)
tnAccessEgressQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressQueueMBS.setStatus("current")


class _TnAccessEgressQueuePIRAdaptation_Type(TAdaptationRule):
    """Custom type tnAccessEgressQueuePIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TnAccessEgressQueuePIRAdaptation_Type.__name__ = "TAdaptationRule"
_TnAccessEgressQueuePIRAdaptation_Object = MibTableColumn
tnAccessEgressQueuePIRAdaptation = _TnAccessEgressQueuePIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 5),
    _TnAccessEgressQueuePIRAdaptation_Type()
)
tnAccessEgressQueuePIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressQueuePIRAdaptation.setStatus("current")


class _TnAccessEgressQueueCIRAdaptation_Type(TAdaptationRule):
    """Custom type tnAccessEgressQueueCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TnAccessEgressQueueCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TnAccessEgressQueueCIRAdaptation_Object = MibTableColumn
tnAccessEgressQueueCIRAdaptation = _TnAccessEgressQueueCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 6),
    _TnAccessEgressQueueCIRAdaptation_Type()
)
tnAccessEgressQueueCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressQueueCIRAdaptation.setStatus("current")


class _TnAccessEgressQueueAdminPIR_Type(TPIRRate):
    """Custom type tnAccessEgressQueueAdminPIR based on TPIRRate"""
    defaultValue = -1


_TnAccessEgressQueueAdminPIR_Type.__name__ = "TPIRRate"
_TnAccessEgressQueueAdminPIR_Object = MibTableColumn
tnAccessEgressQueueAdminPIR = _TnAccessEgressQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 7),
    _TnAccessEgressQueueAdminPIR_Type()
)
tnAccessEgressQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressQueueAdminPIR.setStatus("current")


class _TnAccessEgressQueueAdminCIR_Type(TCIRRate):
    """Custom type tnAccessEgressQueueAdminCIR based on TCIRRate"""
    defaultValue = 0


_TnAccessEgressQueueAdminCIR_Type.__name__ = "TCIRRate"
_TnAccessEgressQueueAdminCIR_Object = MibTableColumn
tnAccessEgressQueueAdminCIR = _TnAccessEgressQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 8),
    _TnAccessEgressQueueAdminCIR_Type()
)
tnAccessEgressQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressQueueAdminCIR.setStatus("current")
_TnAccessEgressQueueOperPIR_Type = TPIRRate
_TnAccessEgressQueueOperPIR_Object = MibTableColumn
tnAccessEgressQueueOperPIR = _TnAccessEgressQueueOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 9),
    _TnAccessEgressQueueOperPIR_Type()
)
tnAccessEgressQueueOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessEgressQueueOperPIR.setStatus("current")
_TnAccessEgressQueueOperCIR_Type = TCIRRate
_TnAccessEgressQueueOperCIR_Object = MibTableColumn
tnAccessEgressQueueOperCIR = _TnAccessEgressQueueOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 10),
    _TnAccessEgressQueueOperCIR_Type()
)
tnAccessEgressQueueOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessEgressQueueOperCIR.setStatus("current")
_TnAccessEgressQueueLastChanged_Type = TimeStamp
_TnAccessEgressQueueLastChanged_Object = MibTableColumn
tnAccessEgressQueueLastChanged = _TnAccessEgressQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 2, 1, 11),
    _TnAccessEgressQueueLastChanged_Type()
)
tnAccessEgressQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessEgressQueueLastChanged.setStatus("current")
_TnAccessEgressFCTable_Object = MibTable
tnAccessEgressFCTable = _TnAccessEgressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnAccessEgressFCTable.setStatus("current")
_TnAccessEgressFCEntry_Object = MibTableRow
tnAccessEgressFCEntry = _TnAccessEgressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1)
)
tnAccessEgressFCEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SAS-QOS-MIB", "tnAccessEgressIndex"),
    (0, "TN-SAS-QOS-MIB", "tnAccessEgressFCName"),
)
if mibBuilder.loadTexts:
    tnAccessEgressFCEntry.setStatus("current")
_TnAccessEgressFCName_Type = TFCName
_TnAccessEgressFCName_Object = MibTableColumn
tnAccessEgressFCName = _TnAccessEgressFCName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1, 1),
    _TnAccessEgressFCName_Type()
)
tnAccessEgressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAccessEgressFCName.setStatus("current")
_TnAccessEgressFCRowStatus_Type = RowStatus
_TnAccessEgressFCRowStatus_Object = MibTableColumn
tnAccessEgressFCRowStatus = _TnAccessEgressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1, 2),
    _TnAccessEgressFCRowStatus_Type()
)
tnAccessEgressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressFCRowStatus.setStatus("current")
_TnAccessEgressFCQueue_Type = TEgressQueueId
_TnAccessEgressFCQueue_Object = MibTableColumn
tnAccessEgressFCQueue = _TnAccessEgressFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1, 3),
    _TnAccessEgressFCQueue_Type()
)
tnAccessEgressFCQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressFCQueue.setStatus("current")


class _TnAccessEgressFCDot1PInProfile_Type(Dot1PPriority):
    """Custom type tnAccessEgressFCDot1PInProfile based on Dot1PPriority"""
    defaultValue = -1


_TnAccessEgressFCDot1PInProfile_Type.__name__ = "Dot1PPriority"
_TnAccessEgressFCDot1PInProfile_Object = MibTableColumn
tnAccessEgressFCDot1PInProfile = _TnAccessEgressFCDot1PInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1, 4),
    _TnAccessEgressFCDot1PInProfile_Type()
)
tnAccessEgressFCDot1PInProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressFCDot1PInProfile.setStatus("current")


class _TnAccessEgressFCDot1POutProfile_Type(Dot1PPriority):
    """Custom type tnAccessEgressFCDot1POutProfile based on Dot1PPriority"""
    defaultValue = -1


_TnAccessEgressFCDot1POutProfile_Type.__name__ = "Dot1PPriority"
_TnAccessEgressFCDot1POutProfile_Object = MibTableColumn
tnAccessEgressFCDot1POutProfile = _TnAccessEgressFCDot1POutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1, 5),
    _TnAccessEgressFCDot1POutProfile_Type()
)
tnAccessEgressFCDot1POutProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessEgressFCDot1POutProfile.setStatus("current")
_TnAccessEgressFCLastChanged_Type = TimeStamp
_TnAccessEgressFCLastChanged_Object = MibTableColumn
tnAccessEgressFCLastChanged = _TnAccessEgressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1, 6),
    _TnAccessEgressFCLastChanged_Type()
)
tnAccessEgressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessEgressFCLastChanged.setStatus("current")


class _TnAccessEgressFCDscpInProfile_Type(TDSCPNameOrEmpty):
    """Custom type tnAccessEgressFCDscpInProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TnAccessEgressFCDscpInProfile_Type.__name__ = "TDSCPNameOrEmpty"
_TnAccessEgressFCDscpInProfile_Object = MibTableColumn
tnAccessEgressFCDscpInProfile = _TnAccessEgressFCDscpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1, 7),
    _TnAccessEgressFCDscpInProfile_Type()
)
tnAccessEgressFCDscpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAccessEgressFCDscpInProfile.setStatus("current")


class _TnAccessEgressFCDscpOutProfile_Type(TDSCPNameOrEmpty):
    """Custom type tnAccessEgressFCDscpOutProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TnAccessEgressFCDscpOutProfile_Type.__name__ = "TDSCPNameOrEmpty"
_TnAccessEgressFCDscpOutProfile_Object = MibTableColumn
tnAccessEgressFCDscpOutProfile = _TnAccessEgressFCDscpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 3, 1, 8),
    _TnAccessEgressFCDscpOutProfile_Type()
)
tnAccessEgressFCDscpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAccessEgressFCDscpOutProfile.setStatus("current")
_TnAccessEgressScalar1_Type = Unsigned32
_TnAccessEgressScalar1_Object = MibScalar
tnAccessEgressScalar1 = _TnAccessEgressScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 101),
    _TnAccessEgressScalar1_Type()
)
tnAccessEgressScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessEgressScalar1.setStatus("current")
_TnAccessEgressScalar2_Type = Unsigned32
_TnAccessEgressScalar2_Object = MibScalar
tnAccessEgressScalar2 = _TnAccessEgressScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 1, 102),
    _TnAccessEgressScalar2_Type()
)
tnAccessEgressScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessEgressScalar2.setStatus("current")
_TnSASSapIngressObjects_ObjectIdentity = ObjectIdentity
tnSASSapIngressObjects = _TnSASSapIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2)
)
_TnSapIngressMeterTable_Object = MibTable
tnSapIngressMeterTable = _TnSapIngressMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnSapIngressMeterTable.setStatus("current")
_TnSapIngressMeterEntry_Object = MibTableRow
tnSapIngressMeterEntry = _TnSapIngressMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1)
)
tnSapIngressMeterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnSapIngressIndex"),
    (0, "TN-SAS-QOS-MIB", "tnSapIngressMeter"),
)
if mibBuilder.loadTexts:
    tnSapIngressMeterEntry.setStatus("current")
_TnSapIngressMeter_Type = TSapIngressMeterId
_TnSapIngressMeter_Object = MibTableColumn
tnSapIngressMeter = _TnSapIngressMeter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 1),
    _TnSapIngressMeter_Type()
)
tnSapIngressMeter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIngressMeter.setStatus("current")
_TnSapIngressMeterRowStatus_Type = RowStatus
_TnSapIngressMeterRowStatus_Object = MibTableColumn
tnSapIngressMeterRowStatus = _TnSapIngressMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 2),
    _TnSapIngressMeterRowStatus_Type()
)
tnSapIngressMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterRowStatus.setStatus("current")


class _TnSapIngressMeterMCast_Type(TruthValue):
    """Custom type tnSapIngressMeterMCast based on TruthValue"""
    defaultValue = 2


_TnSapIngressMeterMCast_Type.__name__ = "TruthValue"
_TnSapIngressMeterMCast_Object = MibTableColumn
tnSapIngressMeterMCast = _TnSapIngressMeterMCast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 8),
    _TnSapIngressMeterMCast_Type()
)
tnSapIngressMeterMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterMCast.setStatus("current")


class _TnSapIngressMeterPIRAdaptation_Type(TAdaptationRule):
    """Custom type tnSapIngressMeterPIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TnSapIngressMeterPIRAdaptation_Type.__name__ = "TAdaptationRule"
_TnSapIngressMeterPIRAdaptation_Object = MibTableColumn
tnSapIngressMeterPIRAdaptation = _TnSapIngressMeterPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 13),
    _TnSapIngressMeterPIRAdaptation_Type()
)
tnSapIngressMeterPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterPIRAdaptation.setStatus("current")


class _TnSapIngressMeterCIRAdaptation_Type(TAdaptationRule):
    """Custom type tnSapIngressMeterCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TnSapIngressMeterCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TnSapIngressMeterCIRAdaptation_Object = MibTableColumn
tnSapIngressMeterCIRAdaptation = _TnSapIngressMeterCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 14),
    _TnSapIngressMeterCIRAdaptation_Type()
)
tnSapIngressMeterCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterCIRAdaptation.setStatus("current")


class _TnSapIngressMeterAdminPIR_Type(TIngressPIRRate):
    """Custom type tnSapIngressMeterAdminPIR based on TIngressPIRRate"""
    defaultValue = -1


_TnSapIngressMeterAdminPIR_Type.__name__ = "TIngressPIRRate"
_TnSapIngressMeterAdminPIR_Object = MibTableColumn
tnSapIngressMeterAdminPIR = _TnSapIngressMeterAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 15),
    _TnSapIngressMeterAdminPIR_Type()
)
tnSapIngressMeterAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterAdminPIR.setStatus("current")


class _TnSapIngressMeterAdminCIR_Type(TIngressCIRRate):
    """Custom type tnSapIngressMeterAdminCIR based on TIngressCIRRate"""
    defaultValue = 0


_TnSapIngressMeterAdminCIR_Type.__name__ = "TIngressCIRRate"
_TnSapIngressMeterAdminCIR_Object = MibTableColumn
tnSapIngressMeterAdminCIR = _TnSapIngressMeterAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 16),
    _TnSapIngressMeterAdminCIR_Type()
)
tnSapIngressMeterAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterAdminCIR.setStatus("current")
_TnSapIngressMeterOperPIR_Type = TPIRRate
_TnSapIngressMeterOperPIR_Object = MibTableColumn
tnSapIngressMeterOperPIR = _TnSapIngressMeterOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 17),
    _TnSapIngressMeterOperPIR_Type()
)
tnSapIngressMeterOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressMeterOperPIR.setStatus("current")
_TnSapIngressMeterOperCIR_Type = TCIRRate
_TnSapIngressMeterOperCIR_Object = MibTableColumn
tnSapIngressMeterOperCIR = _TnSapIngressMeterOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 18),
    _TnSapIngressMeterOperCIR_Type()
)
tnSapIngressMeterOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressMeterOperCIR.setStatus("current")
_TnSapIngressMeterLastChanged_Type = TimeStamp
_TnSapIngressMeterLastChanged_Object = MibTableColumn
tnSapIngressMeterLastChanged = _TnSapIngressMeterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 19),
    _TnSapIngressMeterLastChanged_Type()
)
tnSapIngressMeterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressMeterLastChanged.setStatus("current")


class _TnSapIngressMeterMode_Type(TMeterMode):
    """Custom type tnSapIngressMeterMode based on TMeterMode"""
    defaultValue = 1


_TnSapIngressMeterMode_Type.__name__ = "TMeterMode"
_TnSapIngressMeterMode_Object = MibTableColumn
tnSapIngressMeterMode = _TnSapIngressMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 21),
    _TnSapIngressMeterMode_Type()
)
tnSapIngressMeterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterMode.setStatus("current")


class _TnSapIngressMeterRateMode_Type(TMeterRateMode):
    """Custom type tnSapIngressMeterRateMode based on TMeterRateMode"""
    defaultValue = 3


_TnSapIngressMeterRateMode_Type.__name__ = "TMeterRateMode"
_TnSapIngressMeterRateMode_Object = MibTableColumn
tnSapIngressMeterRateMode = _TnSapIngressMeterRateMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 22),
    _TnSapIngressMeterRateMode_Type()
)
tnSapIngressMeterRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterRateMode.setStatus("current")


class _TnSapIngressMeterAdminCBS_Type(TIngressBurstSize):
    """Custom type tnSapIngressMeterAdminCBS based on TIngressBurstSize"""
    defaultValue = -1


_TnSapIngressMeterAdminCBS_Type.__name__ = "TIngressBurstSize"
_TnSapIngressMeterAdminCBS_Object = MibTableColumn
tnSapIngressMeterAdminCBS = _TnSapIngressMeterAdminCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 23),
    _TnSapIngressMeterAdminCBS_Type()
)
tnSapIngressMeterAdminCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterAdminCBS.setStatus("current")


class _TnSapIngressMeterAdminMBS_Type(TIngressBurstSize):
    """Custom type tnSapIngressMeterAdminMBS based on TIngressBurstSize"""
    defaultValue = -1


_TnSapIngressMeterAdminMBS_Type.__name__ = "TIngressBurstSize"
_TnSapIngressMeterAdminMBS_Object = MibTableColumn
tnSapIngressMeterAdminMBS = _TnSapIngressMeterAdminMBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 24),
    _TnSapIngressMeterAdminMBS_Type()
)
tnSapIngressMeterAdminMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMeterAdminMBS.setStatus("current")
_TnSapIngressMeterOperCBS_Type = TIngressBurstSize
_TnSapIngressMeterOperCBS_Object = MibTableColumn
tnSapIngressMeterOperCBS = _TnSapIngressMeterOperCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 25),
    _TnSapIngressMeterOperCBS_Type()
)
tnSapIngressMeterOperCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressMeterOperCBS.setStatus("current")
_TnSapIngressMeterOperMBS_Type = TIngressBurstSize
_TnSapIngressMeterOperMBS_Object = MibTableColumn
tnSapIngressMeterOperMBS = _TnSapIngressMeterOperMBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 1, 1, 26),
    _TnSapIngressMeterOperMBS_Type()
)
tnSapIngressMeterOperMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressMeterOperMBS.setStatus("current")
_TnSASSapIngressFCTable_Object = MibTable
tnSASSapIngressFCTable = _TnSASSapIngressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnSASSapIngressFCTable.setStatus("current")
_TnSASSapIngressFCEntry_Object = MibTableRow
tnSASSapIngressFCEntry = _TnSASSapIngressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSASSapIngressFCEntry.setStatus("current")
_TnSapIngressFCMeter_Type = TSapIngressMeterId
_TnSapIngressFCMeter_Object = MibTableColumn
tnSapIngressFCMeter = _TnSapIngressFCMeter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 2, 1, 1),
    _TnSapIngressFCMeter_Type()
)
tnSapIngressFCMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCMeter.setStatus("current")
_TnSapIngressFCMCastMeter_Type = TSapIngressMeterId
_TnSapIngressFCMCastMeter_Object = MibTableColumn
tnSapIngressFCMCastMeter = _TnSapIngressFCMCastMeter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 2, 1, 2),
    _TnSapIngressFCMCastMeter_Type()
)
tnSapIngressFCMCastMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCMCastMeter.setStatus("current")
_TnSapIngressFCBCastMeter_Type = TSapIngressMeterId
_TnSapIngressFCBCastMeter_Object = MibTableColumn
tnSapIngressFCBCastMeter = _TnSapIngressFCBCastMeter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 2, 1, 3),
    _TnSapIngressFCBCastMeter_Type()
)
tnSapIngressFCBCastMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCBCastMeter.setStatus("current")
_TnSapIngressFCUnknownMeter_Type = TSapIngressMeterId
_TnSapIngressFCUnknownMeter_Object = MibTableColumn
tnSapIngressFCUnknownMeter = _TnSapIngressFCUnknownMeter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 2, 1, 4),
    _TnSapIngressFCUnknownMeter_Type()
)
tnSapIngressFCUnknownMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressFCUnknownMeter.setStatus("current")
_TnSapIngQosMeterStatsTable_Object = MibTable
tnSapIngQosMeterStatsTable = _TnSapIngQosMeterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsTable.setStatus("current")
_TnSapIngQosMeterStatsEntry_Object = MibTableRow
tnSapIngQosMeterStatsEntry = _TnSapIngQosMeterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1)
)
tnSapIngQosMeterStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
    (0, "TN-SAS-QOS-MIB", "tnSapIngQosMeterId"),
)
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsEntry.setStatus("current")
_TnSapIngQosMeterId_Type = TSapIngressMeterId
_TnSapIngQosMeterId_Object = MibTableColumn
tnSapIngQosMeterId = _TnSapIngQosMeterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 1),
    _TnSapIngQosMeterId_Type()
)
tnSapIngQosMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIngQosMeterId.setStatus("current")
_TnSapIngQosMeterStatsForwardedInProfPackets_Type = Counter64
_TnSapIngQosMeterStatsForwardedInProfPackets_Object = MibTableColumn
tnSapIngQosMeterStatsForwardedInProfPackets = _TnSapIngQosMeterStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 10),
    _TnSapIngQosMeterStatsForwardedInProfPackets_Type()
)
tnSapIngQosMeterStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsForwardedInProfPackets.setStatus("current")
_TnSapIngQosMeterStatsForwardedOutProfPackets_Type = Counter64
_TnSapIngQosMeterStatsForwardedOutProfPackets_Object = MibTableColumn
tnSapIngQosMeterStatsForwardedOutProfPackets = _TnSapIngQosMeterStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 11),
    _TnSapIngQosMeterStatsForwardedOutProfPackets_Type()
)
tnSapIngQosMeterStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsForwardedOutProfPackets.setStatus("current")
_TnSapIngQosMeterStatsForwardedInProfOctets_Type = Counter64
_TnSapIngQosMeterStatsForwardedInProfOctets_Object = MibTableColumn
tnSapIngQosMeterStatsForwardedInProfOctets = _TnSapIngQosMeterStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 12),
    _TnSapIngQosMeterStatsForwardedInProfOctets_Type()
)
tnSapIngQosMeterStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsForwardedInProfOctets.setStatus("current")
_TnSapIngQosMeterStatsForwardedOutProfOctets_Type = Counter64
_TnSapIngQosMeterStatsForwardedOutProfOctets_Object = MibTableColumn
tnSapIngQosMeterStatsForwardedOutProfOctets = _TnSapIngQosMeterStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 13),
    _TnSapIngQosMeterStatsForwardedOutProfOctets_Type()
)
tnSapIngQosMeterStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsForwardedOutProfOctets.setStatus("current")
_TnSapIngQosMeterStatsForwardedPackets_Type = Counter64
_TnSapIngQosMeterStatsForwardedPackets_Object = MibTableColumn
tnSapIngQosMeterStatsForwardedPackets = _TnSapIngQosMeterStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 14),
    _TnSapIngQosMeterStatsForwardedPackets_Type()
)
tnSapIngQosMeterStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsForwardedPackets.setStatus("current")
_TnSapIngQosMeterStatsForwardedOctets_Type = Counter64
_TnSapIngQosMeterStatsForwardedOctets_Object = MibTableColumn
tnSapIngQosMeterStatsForwardedOctets = _TnSapIngQosMeterStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 15),
    _TnSapIngQosMeterStatsForwardedOctets_Type()
)
tnSapIngQosMeterStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsForwardedOctets.setStatus("current")
_TnSapIngQosMeterStatsDroppedPackets_Type = Counter64
_TnSapIngQosMeterStatsDroppedPackets_Object = MibTableColumn
tnSapIngQosMeterStatsDroppedPackets = _TnSapIngQosMeterStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 16),
    _TnSapIngQosMeterStatsDroppedPackets_Type()
)
tnSapIngQosMeterStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsDroppedPackets.setStatus("current")
_TnSapIngQosMeterStatsDroppedOctets_Type = Counter64
_TnSapIngQosMeterStatsDroppedOctets_Object = MibTableColumn
tnSapIngQosMeterStatsDroppedOctets = _TnSapIngQosMeterStatsDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 3, 1, 17),
    _TnSapIngQosMeterStatsDroppedOctets_Type()
)
tnSapIngQosMeterStatsDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngQosMeterStatsDroppedOctets.setStatus("current")
_TnSapIngressExtnTable_Object = MibTable
tnSapIngressExtnTable = _TnSapIngressExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tnSapIngressExtnTable.setStatus("current")
_TnSapIngressExtnEntry_Object = MibTableRow
tnSapIngressExtnEntry = _TnSapIngressExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnSapIngressExtnEntry.setStatus("current")


class _TnSapIngressNumQosClassifiers_Type(Unsigned32):
    """Custom type tnSapIngressNumQosClassifiers based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_TnSapIngressNumQosClassifiers_Type.__name__ = "Unsigned32"
_TnSapIngressNumQosClassifiers_Object = MibTableColumn
tnSapIngressNumQosClassifiers = _TnSapIngressNumQosClassifiers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 1),
    _TnSapIngressNumQosClassifiers_Type()
)
tnSapIngressNumQosClassifiers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressNumQosClassifiers.setStatus("current")
_TnSapIngressQosClassifiersRequiredInVpls_Type = Unsigned32
_TnSapIngressQosClassifiersRequiredInVpls_Object = MibTableColumn
tnSapIngressQosClassifiersRequiredInVpls = _TnSapIngressQosClassifiersRequiredInVpls_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 4),
    _TnSapIngressQosClassifiersRequiredInVpls_Type()
)
tnSapIngressQosClassifiersRequiredInVpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressQosClassifiersRequiredInVpls.setStatus("current")
_TnSapIngressQosClassifiersRequiredInEpipe_Type = Unsigned32
_TnSapIngressQosClassifiersRequiredInEpipe_Object = MibTableColumn
tnSapIngressQosClassifiersRequiredInEpipe = _TnSapIngressQosClassifiersRequiredInEpipe_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 5),
    _TnSapIngressQosClassifiersRequiredInEpipe_Type()
)
tnSapIngressQosClassifiersRequiredInEpipe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressQosClassifiersRequiredInEpipe.setStatus("current")
_TnSapIngressQosMetersRequiredInVpls_Type = Unsigned32
_TnSapIngressQosMetersRequiredInVpls_Object = MibTableColumn
tnSapIngressQosMetersRequiredInVpls = _TnSapIngressQosMetersRequiredInVpls_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 6),
    _TnSapIngressQosMetersRequiredInVpls_Type()
)
tnSapIngressQosMetersRequiredInVpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressQosMetersRequiredInVpls.setStatus("current")
_TnSapIngressQosMetersRequiredInEpipe_Type = Unsigned32
_TnSapIngressQosMetersRequiredInEpipe_Object = MibTableColumn
tnSapIngressQosMetersRequiredInEpipe = _TnSapIngressQosMetersRequiredInEpipe_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 7),
    _TnSapIngressQosMetersRequiredInEpipe_Type()
)
tnSapIngressQosMetersRequiredInEpipe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIngressQosMetersRequiredInEpipe.setStatus("current")


class _TnSapIngressIPCriteriaMatch_Type(Integer32):
    """Custom type tnSapIngressIPCriteriaMatch based on Integer32"""
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


_TnSapIngressIPCriteriaMatch_Type.__name__ = "Integer32"
_TnSapIngressIPCriteriaMatch_Object = MibTableColumn
tnSapIngressIPCriteriaMatch = _TnSapIngressIPCriteriaMatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 8),
    _TnSapIngressIPCriteriaMatch_Type()
)
tnSapIngressIPCriteriaMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPCriteriaMatch.setStatus("current")


class _TnSapIngressMacCriteriaMatch_Type(Integer32):
    """Custom type tnSapIngressMacCriteriaMatch based on Integer32"""
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


_TnSapIngressMacCriteriaMatch_Type.__name__ = "Integer32"
_TnSapIngressMacCriteriaMatch_Object = MibTableColumn
tnSapIngressMacCriteriaMatch = _TnSapIngressMacCriteriaMatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 9),
    _TnSapIngressMacCriteriaMatch_Type()
)
tnSapIngressMacCriteriaMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacCriteriaMatch.setStatus("current")


class _TnSapIngressIPv6CriteriaEnable_Type(TruthValue):
    """Custom type tnSapIngressIPv6CriteriaEnable based on TruthValue"""
    defaultValue = 2


_TnSapIngressIPv6CriteriaEnable_Type.__name__ = "TruthValue"
_TnSapIngressIPv6CriteriaEnable_Object = MibTableColumn
tnSapIngressIPv6CriteriaEnable = _TnSapIngressIPv6CriteriaEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 10),
    _TnSapIngressIPv6CriteriaEnable_Type()
)
tnSapIngressIPv6CriteriaEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaEnable.setStatus("current")


class _TnSapIngressIPv6CriteriaMatch_Type(Integer32):
    """Custom type tnSapIngressIPv6CriteriaMatch based on Integer32"""
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


_TnSapIngressIPv6CriteriaMatch_Type.__name__ = "Integer32"
_TnSapIngressIPv6CriteriaMatch_Object = MibTableColumn
tnSapIngressIPv6CriteriaMatch = _TnSapIngressIPv6CriteriaMatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 4, 1, 11),
    _TnSapIngressIPv6CriteriaMatch_Type()
)
tnSapIngressIPv6CriteriaMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIPv6CriteriaMatch.setStatus("current")
_TnSASSapIngressScalar1_Type = Unsigned32
_TnSASSapIngressScalar1_Object = MibScalar
tnSASSapIngressScalar1 = _TnSASSapIngressScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 101),
    _TnSASSapIngressScalar1_Type()
)
tnSASSapIngressScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASSapIngressScalar1.setStatus("current")
_TnSASSapIngressScalar2_Type = Unsigned32
_TnSASSapIngressScalar2_Object = MibScalar
tnSASSapIngressScalar2 = _TnSASSapIngressScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 2, 102),
    _TnSASSapIngressScalar2_Type()
)
tnSASSapIngressScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASSapIngressScalar2.setStatus("current")
_TnSASNetworkIngressObjects_ObjectIdentity = ObjectIdentity
tnSASNetworkIngressObjects = _TnSASNetworkIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3)
)
_TnNetworkIngressFCTable_Object = MibTable
tnNetworkIngressFCTable = _TnNetworkIngressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnNetworkIngressFCTable.setStatus("current")
_TnNetworkIngressFCEntry_Object = MibTableRow
tnNetworkIngressFCEntry = _TnNetworkIngressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 1, 1)
)
tnNetworkIngressFCEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnNetworkPolicyIndex"),
    (0, "TN-SAS-QOS-MIB", "tnNetworkIngressFCName"),
)
if mibBuilder.loadTexts:
    tnNetworkIngressFCEntry.setStatus("current")
_TnNetworkIngressFCName_Type = TNamedItem
_TnNetworkIngressFCName_Object = MibTableColumn
tnNetworkIngressFCName = _TnNetworkIngressFCName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 1, 1, 1),
    _TnNetworkIngressFCName_Type()
)
tnNetworkIngressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetworkIngressFCName.setStatus("current")
_TnNetworkIngressFCRowStatus_Type = RowStatus
_TnNetworkIngressFCRowStatus_Object = MibTableColumn
tnNetworkIngressFCRowStatus = _TnNetworkIngressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 1, 1, 2),
    _TnNetworkIngressFCRowStatus_Type()
)
tnNetworkIngressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressFCRowStatus.setStatus("current")
_TnNetworkIngressFCMeter_Type = TNetworkIngressMeterId
_TnNetworkIngressFCMeter_Object = MibTableColumn
tnNetworkIngressFCMeter = _TnNetworkIngressFCMeter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 1, 1, 3),
    _TnNetworkIngressFCMeter_Type()
)
tnNetworkIngressFCMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressFCMeter.setStatus("current")
_TnNetworkIngressFCMCastMeter_Type = TNetworkIngressMeterId
_TnNetworkIngressFCMCastMeter_Object = MibTableColumn
tnNetworkIngressFCMCastMeter = _TnNetworkIngressFCMCastMeter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 1, 1, 4),
    _TnNetworkIngressFCMCastMeter_Type()
)
tnNetworkIngressFCMCastMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressFCMCastMeter.setStatus("current")
_TnNetworkIngressFCLastChanged_Type = TimeStamp
_TnNetworkIngressFCLastChanged_Object = MibTableColumn
tnNetworkIngressFCLastChanged = _TnNetworkIngressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 1, 1, 5),
    _TnNetworkIngressFCLastChanged_Type()
)
tnNetworkIngressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkIngressFCLastChanged.setStatus("current")
_TnNetworkIngressMeterTable_Object = MibTable
tnNetworkIngressMeterTable = _TnNetworkIngressMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnNetworkIngressMeterTable.setStatus("current")
_TnNetworkIngressMeterEntry_Object = MibTableRow
tnNetworkIngressMeterEntry = _TnNetworkIngressMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1)
)
tnNetworkIngressMeterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnNetworkPolicyIndex"),
    (0, "TN-SAS-QOS-MIB", "tnNetworkIngressMeterIndex"),
)
if mibBuilder.loadTexts:
    tnNetworkIngressMeterEntry.setStatus("current")
_TnNetworkIngressMeterIndex_Type = TNetworkIngressMeterId
_TnNetworkIngressMeterIndex_Object = MibTableColumn
tnNetworkIngressMeterIndex = _TnNetworkIngressMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 1),
    _TnNetworkIngressMeterIndex_Type()
)
tnNetworkIngressMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterIndex.setStatus("current")
_TnNetworkIngressMeterRowStatus_Type = RowStatus
_TnNetworkIngressMeterRowStatus_Object = MibTableColumn
tnNetworkIngressMeterRowStatus = _TnNetworkIngressMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 2),
    _TnNetworkIngressMeterRowStatus_Type()
)
tnNetworkIngressMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterRowStatus.setStatus("current")


class _TnNetworkIngressMeterCIRAdaptation_Type(TAdaptationRule):
    """Custom type tnNetworkIngressMeterCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TnNetworkIngressMeterCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TnNetworkIngressMeterCIRAdaptation_Object = MibTableColumn
tnNetworkIngressMeterCIRAdaptation = _TnNetworkIngressMeterCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 5),
    _TnNetworkIngressMeterCIRAdaptation_Type()
)
tnNetworkIngressMeterCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterCIRAdaptation.setStatus("current")


class _TnNetworkIngressMeterPIRAdaptation_Type(TAdaptationRule):
    """Custom type tnNetworkIngressMeterPIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TnNetworkIngressMeterPIRAdaptation_Type.__name__ = "TAdaptationRule"
_TnNetworkIngressMeterPIRAdaptation_Object = MibTableColumn
tnNetworkIngressMeterPIRAdaptation = _TnNetworkIngressMeterPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 6),
    _TnNetworkIngressMeterPIRAdaptation_Type()
)
tnNetworkIngressMeterPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterPIRAdaptation.setStatus("current")


class _TnNetworkIngressMeterAdminPIR_Type(TIngressPIRRate):
    """Custom type tnNetworkIngressMeterAdminPIR based on TIngressPIRRate"""
    defaultValue = -1


_TnNetworkIngressMeterAdminPIR_Type.__name__ = "TIngressPIRRate"
_TnNetworkIngressMeterAdminPIR_Object = MibTableColumn
tnNetworkIngressMeterAdminPIR = _TnNetworkIngressMeterAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 7),
    _TnNetworkIngressMeterAdminPIR_Type()
)
tnNetworkIngressMeterAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterAdminPIR.setStatus("current")


class _TnNetworkIngressMeterAdminCIR_Type(TIngressCIRRate):
    """Custom type tnNetworkIngressMeterAdminCIR based on TIngressCIRRate"""
    defaultValue = 0


_TnNetworkIngressMeterAdminCIR_Type.__name__ = "TIngressCIRRate"
_TnNetworkIngressMeterAdminCIR_Object = MibTableColumn
tnNetworkIngressMeterAdminCIR = _TnNetworkIngressMeterAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 8),
    _TnNetworkIngressMeterAdminCIR_Type()
)
tnNetworkIngressMeterAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterAdminCIR.setStatus("current")
_TnNetworkIngressMeterOperPIR_Type = TPIRRate
_TnNetworkIngressMeterOperPIR_Object = MibTableColumn
tnNetworkIngressMeterOperPIR = _TnNetworkIngressMeterOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 9),
    _TnNetworkIngressMeterOperPIR_Type()
)
tnNetworkIngressMeterOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterOperPIR.setStatus("current")
_TnNetworkIngressMeterOperCIR_Type = TCIRRate
_TnNetworkIngressMeterOperCIR_Object = MibTableColumn
tnNetworkIngressMeterOperCIR = _TnNetworkIngressMeterOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 10),
    _TnNetworkIngressMeterOperCIR_Type()
)
tnNetworkIngressMeterOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterOperCIR.setStatus("current")
_TnNetworkIngressMeterLastChanged_Type = TimeStamp
_TnNetworkIngressMeterLastChanged_Object = MibTableColumn
tnNetworkIngressMeterLastChanged = _TnNetworkIngressMeterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 11),
    _TnNetworkIngressMeterLastChanged_Type()
)
tnNetworkIngressMeterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterLastChanged.setStatus("current")


class _TnNetworkIngressMeterMode_Type(TMeterMode):
    """Custom type tnNetworkIngressMeterMode based on TMeterMode"""
    defaultValue = 1


_TnNetworkIngressMeterMode_Type.__name__ = "TMeterMode"
_TnNetworkIngressMeterMode_Object = MibTableColumn
tnNetworkIngressMeterMode = _TnNetworkIngressMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 12),
    _TnNetworkIngressMeterMode_Type()
)
tnNetworkIngressMeterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterMode.setStatus("current")


class _TnNetworkIngressMeterMCast_Type(TruthValue):
    """Custom type tnNetworkIngressMeterMCast based on TruthValue"""
    defaultValue = 2


_TnNetworkIngressMeterMCast_Type.__name__ = "TruthValue"
_TnNetworkIngressMeterMCast_Object = MibTableColumn
tnNetworkIngressMeterMCast = _TnNetworkIngressMeterMCast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 13),
    _TnNetworkIngressMeterMCast_Type()
)
tnNetworkIngressMeterMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterMCast.setStatus("current")


class _TnNetworkIngressMeterRateMode_Type(TMeterRateMode):
    """Custom type tnNetworkIngressMeterRateMode based on TMeterRateMode"""
    defaultValue = 3


_TnNetworkIngressMeterRateMode_Type.__name__ = "TMeterRateMode"
_TnNetworkIngressMeterRateMode_Object = MibTableColumn
tnNetworkIngressMeterRateMode = _TnNetworkIngressMeterRateMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 14),
    _TnNetworkIngressMeterRateMode_Type()
)
tnNetworkIngressMeterRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterRateMode.setStatus("current")


class _TnNetworkIngressMeterAdminCBS_Type(TIngressBurstSize):
    """Custom type tnNetworkIngressMeterAdminCBS based on TIngressBurstSize"""
    defaultValue = -1


_TnNetworkIngressMeterAdminCBS_Type.__name__ = "TIngressBurstSize"
_TnNetworkIngressMeterAdminCBS_Object = MibTableColumn
tnNetworkIngressMeterAdminCBS = _TnNetworkIngressMeterAdminCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 15),
    _TnNetworkIngressMeterAdminCBS_Type()
)
tnNetworkIngressMeterAdminCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterAdminCBS.setStatus("current")


class _TnNetworkIngressMeterAdminMBS_Type(TIngressBurstSize):
    """Custom type tnNetworkIngressMeterAdminMBS based on TIngressBurstSize"""
    defaultValue = -1


_TnNetworkIngressMeterAdminMBS_Type.__name__ = "TIngressBurstSize"
_TnNetworkIngressMeterAdminMBS_Object = MibTableColumn
tnNetworkIngressMeterAdminMBS = _TnNetworkIngressMeterAdminMBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 16),
    _TnNetworkIngressMeterAdminMBS_Type()
)
tnNetworkIngressMeterAdminMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterAdminMBS.setStatus("current")
_TnNetworkIngressMeterOperCBS_Type = TIngressBurstSize
_TnNetworkIngressMeterOperCBS_Object = MibTableColumn
tnNetworkIngressMeterOperCBS = _TnNetworkIngressMeterOperCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 17),
    _TnNetworkIngressMeterOperCBS_Type()
)
tnNetworkIngressMeterOperCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterOperCBS.setStatus("current")
_TnNetworkIngressMeterOperMBS_Type = TIngressBurstSize
_TnNetworkIngressMeterOperMBS_Object = MibTableColumn
tnNetworkIngressMeterOperMBS = _TnNetworkIngressMeterOperMBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 2, 1, 26),
    _TnNetworkIngressMeterOperMBS_Type()
)
tnNetworkIngressMeterOperMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterOperMBS.setStatus("current")
_TnSASNetworkIngressScalar1_Type = Unsigned32
_TnSASNetworkIngressScalar1_Object = MibScalar
tnSASNetworkIngressScalar1 = _TnSASNetworkIngressScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 101),
    _TnSASNetworkIngressScalar1_Type()
)
tnSASNetworkIngressScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASNetworkIngressScalar1.setStatus("current")
_TnSASNetworkIngressScalar2_Type = Unsigned32
_TnSASNetworkIngressScalar2_Object = MibScalar
tnSASNetworkIngressScalar2 = _TnSASNetworkIngressScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 3, 102),
    _TnSASNetworkIngressScalar2_Type()
)
tnSASNetworkIngressScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASNetworkIngressScalar2.setStatus("current")
_TnSASSlopeObjects_ObjectIdentity = ObjectIdentity
tnSASSlopeObjects = _TnSASSlopeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4)
)
_TnSASSlopePolicyExtnTable_Object = MibTable
tnSASSlopePolicyExtnTable = _TnSASSlopePolicyExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnSASSlopePolicyExtnTable.setStatus("current")
_TnSASSlopePolicyExtnEntry_Object = MibTableRow
tnSASSlopePolicyExtnEntry = _TnSASSlopePolicyExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tnSASSlopePolicyExtnEntry.setStatus("current")


class _TnSlopeHiQueue1DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeHiQueue1DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TnSlopeHiQueue1DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeHiQueue1DropRate_Object = MibTableColumn
tnSlopeHiQueue1DropRate = _TnSlopeHiQueue1DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 1),
    _TnSlopeHiQueue1DropRate_Type()
)
tnSlopeHiQueue1DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiQueue1DropRate.setStatus("current")


class _TnSlopeHiQueue2DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeHiQueue2DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TnSlopeHiQueue2DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeHiQueue2DropRate_Object = MibTableColumn
tnSlopeHiQueue2DropRate = _TnSlopeHiQueue2DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 2),
    _TnSlopeHiQueue2DropRate_Type()
)
tnSlopeHiQueue2DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiQueue2DropRate.setStatus("current")


class _TnSlopeHiQueue3DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeHiQueue3DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TnSlopeHiQueue3DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeHiQueue3DropRate_Object = MibTableColumn
tnSlopeHiQueue3DropRate = _TnSlopeHiQueue3DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 3),
    _TnSlopeHiQueue3DropRate_Type()
)
tnSlopeHiQueue3DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiQueue3DropRate.setStatus("current")


class _TnSlopeHiQueue4DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeHiQueue4DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TnSlopeHiQueue4DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeHiQueue4DropRate_Object = MibTableColumn
tnSlopeHiQueue4DropRate = _TnSlopeHiQueue4DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 4),
    _TnSlopeHiQueue4DropRate_Type()
)
tnSlopeHiQueue4DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiQueue4DropRate.setStatus("current")


class _TnSlopeHiQueue5DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeHiQueue5DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TnSlopeHiQueue5DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeHiQueue5DropRate_Object = MibTableColumn
tnSlopeHiQueue5DropRate = _TnSlopeHiQueue5DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 5),
    _TnSlopeHiQueue5DropRate_Type()
)
tnSlopeHiQueue5DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiQueue5DropRate.setStatus("current")


class _TnSlopeHiQueue6DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeHiQueue6DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TnSlopeHiQueue6DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeHiQueue6DropRate_Object = MibTableColumn
tnSlopeHiQueue6DropRate = _TnSlopeHiQueue6DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 6),
    _TnSlopeHiQueue6DropRate_Type()
)
tnSlopeHiQueue6DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiQueue6DropRate.setStatus("current")


class _TnSlopeHiQueue7DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeHiQueue7DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TnSlopeHiQueue7DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeHiQueue7DropRate_Object = MibTableColumn
tnSlopeHiQueue7DropRate = _TnSlopeHiQueue7DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 7),
    _TnSlopeHiQueue7DropRate_Type()
)
tnSlopeHiQueue7DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiQueue7DropRate.setStatus("current")


class _TnSlopeHiQueue8DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeHiQueue8DropRate based on TSlopeDropRate"""
    defaultValue = 1


_TnSlopeHiQueue8DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeHiQueue8DropRate_Object = MibTableColumn
tnSlopeHiQueue8DropRate = _TnSlopeHiQueue8DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 8),
    _TnSlopeHiQueue8DropRate_Type()
)
tnSlopeHiQueue8DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiQueue8DropRate.setStatus("current")


class _TnSlopeLoQueue1DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeLoQueue1DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TnSlopeLoQueue1DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeLoQueue1DropRate_Object = MibTableColumn
tnSlopeLoQueue1DropRate = _TnSlopeLoQueue1DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 9),
    _TnSlopeLoQueue1DropRate_Type()
)
tnSlopeLoQueue1DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoQueue1DropRate.setStatus("current")


class _TnSlopeLoQueue2DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeLoQueue2DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TnSlopeLoQueue2DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeLoQueue2DropRate_Object = MibTableColumn
tnSlopeLoQueue2DropRate = _TnSlopeLoQueue2DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 10),
    _TnSlopeLoQueue2DropRate_Type()
)
tnSlopeLoQueue2DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoQueue2DropRate.setStatus("current")


class _TnSlopeLoQueue3DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeLoQueue3DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TnSlopeLoQueue3DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeLoQueue3DropRate_Object = MibTableColumn
tnSlopeLoQueue3DropRate = _TnSlopeLoQueue3DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 11),
    _TnSlopeLoQueue3DropRate_Type()
)
tnSlopeLoQueue3DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoQueue3DropRate.setStatus("current")


class _TnSlopeLoQueue4DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeLoQueue4DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TnSlopeLoQueue4DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeLoQueue4DropRate_Object = MibTableColumn
tnSlopeLoQueue4DropRate = _TnSlopeLoQueue4DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 12),
    _TnSlopeLoQueue4DropRate_Type()
)
tnSlopeLoQueue4DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoQueue4DropRate.setStatus("current")


class _TnSlopeLoQueue5DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeLoQueue5DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TnSlopeLoQueue5DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeLoQueue5DropRate_Object = MibTableColumn
tnSlopeLoQueue5DropRate = _TnSlopeLoQueue5DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 13),
    _TnSlopeLoQueue5DropRate_Type()
)
tnSlopeLoQueue5DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoQueue5DropRate.setStatus("current")


class _TnSlopeLoQueue6DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeLoQueue6DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TnSlopeLoQueue6DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeLoQueue6DropRate_Object = MibTableColumn
tnSlopeLoQueue6DropRate = _TnSlopeLoQueue6DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 14),
    _TnSlopeLoQueue6DropRate_Type()
)
tnSlopeLoQueue6DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoQueue6DropRate.setStatus("current")


class _TnSlopeLoQueue7DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeLoQueue7DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TnSlopeLoQueue7DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeLoQueue7DropRate_Object = MibTableColumn
tnSlopeLoQueue7DropRate = _TnSlopeLoQueue7DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 15),
    _TnSlopeLoQueue7DropRate_Type()
)
tnSlopeLoQueue7DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoQueue7DropRate.setStatus("current")


class _TnSlopeLoQueue8DropRate_Type(TSlopeDropRate):
    """Custom type tnSlopeLoQueue8DropRate based on TSlopeDropRate"""
    defaultValue = 0


_TnSlopeLoQueue8DropRate_Type.__name__ = "TSlopeDropRate"
_TnSlopeLoQueue8DropRate_Object = MibTableColumn
tnSlopeLoQueue8DropRate = _TnSlopeLoQueue8DropRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 16),
    _TnSlopeLoQueue8DropRate_Type()
)
tnSlopeLoQueue8DropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoQueue8DropRate.setStatus("current")


class _TnSlopeHiStartThreshold_Type(TSlopeThreshold):
    """Custom type tnSlopeHiStartThreshold based on TSlopeThreshold"""
    defaultValue = 75


_TnSlopeHiStartThreshold_Type.__name__ = "TSlopeThreshold"
_TnSlopeHiStartThreshold_Object = MibTableColumn
tnSlopeHiStartThreshold = _TnSlopeHiStartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 17),
    _TnSlopeHiStartThreshold_Type()
)
tnSlopeHiStartThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeHiStartThreshold.setStatus("current")


class _TnSlopeLoStartThreshold_Type(TSlopeThreshold):
    """Custom type tnSlopeLoStartThreshold based on TSlopeThreshold"""
    defaultValue = 50


_TnSlopeLoStartThreshold_Type.__name__ = "TSlopeThreshold"
_TnSlopeLoStartThreshold_Object = MibTableColumn
tnSlopeLoStartThreshold = _TnSlopeLoStartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 1, 1, 18),
    _TnSlopeLoStartThreshold_Type()
)
tnSlopeLoStartThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopeLoStartThreshold.setStatus("current")
_TnSlopePolicyQueueTable_Object = MibTable
tnSlopePolicyQueueTable = _TnSlopePolicyQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tnSlopePolicyQueueTable.setStatus("current")
_TnSlopePolicyQueueEntry_Object = MibTableRow
tnSlopePolicyQueueEntry = _TnSlopePolicyQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1)
)
tnSlopePolicyQueueEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-QOS-MIB", "tnSlopePolicy"),
    (0, "TN-SAS-QOS-MIB", "tnSlopePolicyQueueId"),
)
if mibBuilder.loadTexts:
    tnSlopePolicyQueueEntry.setStatus("current")


class _TnSlopePolicyQueueId_Type(TQueueId):
    """Custom type tnSlopePolicyQueueId based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnSlopePolicyQueueId_Type.__name__ = "TQueueId"
_TnSlopePolicyQueueId_Object = MibTableColumn
tnSlopePolicyQueueId = _TnSlopePolicyQueueId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 1),
    _TnSlopePolicyQueueId_Type()
)
tnSlopePolicyQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueId.setStatus("current")
_TnSlopePolicyQueueRowStatus_Type = RowStatus
_TnSlopePolicyQueueRowStatus_Object = MibTableColumn
tnSlopePolicyQueueRowStatus = _TnSlopePolicyQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 2),
    _TnSlopePolicyQueueRowStatus_Type()
)
tnSlopePolicyQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueRowStatus.setStatus("current")
_TnSlopePolicyQueueLastChanged_Type = TimeStamp
_TnSlopePolicyQueueLastChanged_Object = MibTableColumn
tnSlopePolicyQueueLastChanged = _TnSlopePolicyQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 3),
    _TnSlopePolicyQueueLastChanged_Type()
)
tnSlopePolicyQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueLastChanged.setStatus("current")


class _TnSlopePolicyQueueHiAdminStatus_Type(Integer32):
    """Custom type tnSlopePolicyQueueHiAdminStatus based on Integer32"""
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


_TnSlopePolicyQueueHiAdminStatus_Type.__name__ = "Integer32"
_TnSlopePolicyQueueHiAdminStatus_Object = MibTableColumn
tnSlopePolicyQueueHiAdminStatus = _TnSlopePolicyQueueHiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 4),
    _TnSlopePolicyQueueHiAdminStatus_Type()
)
tnSlopePolicyQueueHiAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueHiAdminStatus.setStatus("current")


class _TnSlopePolicyQueueHiStartAverage_Type(Unsigned32):
    """Custom type tnSlopePolicyQueueHiStartAverage based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopePolicyQueueHiStartAverage_Type.__name__ = "Unsigned32"
_TnSlopePolicyQueueHiStartAverage_Object = MibTableColumn
tnSlopePolicyQueueHiStartAverage = _TnSlopePolicyQueueHiStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 5),
    _TnSlopePolicyQueueHiStartAverage_Type()
)
tnSlopePolicyQueueHiStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueHiStartAverage.setStatus("current")


class _TnSlopePolicyQueueHiMaxAverage_Type(Unsigned32):
    """Custom type tnSlopePolicyQueueHiMaxAverage based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopePolicyQueueHiMaxAverage_Type.__name__ = "Unsigned32"
_TnSlopePolicyQueueHiMaxAverage_Object = MibTableColumn
tnSlopePolicyQueueHiMaxAverage = _TnSlopePolicyQueueHiMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 6),
    _TnSlopePolicyQueueHiMaxAverage_Type()
)
tnSlopePolicyQueueHiMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueHiMaxAverage.setStatus("current")


class _TnSlopePolicyQueueHiMaxProbability_Type(TMaxProbability):
    """Custom type tnSlopePolicyQueueHiMaxProbability based on TMaxProbability"""
    defaultValue = 75


_TnSlopePolicyQueueHiMaxProbability_Type.__name__ = "TMaxProbability"
_TnSlopePolicyQueueHiMaxProbability_Object = MibTableColumn
tnSlopePolicyQueueHiMaxProbability = _TnSlopePolicyQueueHiMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 7),
    _TnSlopePolicyQueueHiMaxProbability_Type()
)
tnSlopePolicyQueueHiMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueHiMaxProbability.setStatus("current")


class _TnSlopePolicyQueueLoAdminStatus_Type(Integer32):
    """Custom type tnSlopePolicyQueueLoAdminStatus based on Integer32"""
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


_TnSlopePolicyQueueLoAdminStatus_Type.__name__ = "Integer32"
_TnSlopePolicyQueueLoAdminStatus_Object = MibTableColumn
tnSlopePolicyQueueLoAdminStatus = _TnSlopePolicyQueueLoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 8),
    _TnSlopePolicyQueueLoAdminStatus_Type()
)
tnSlopePolicyQueueLoAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueLoAdminStatus.setStatus("current")


class _TnSlopePolicyQueueLoStartAverage_Type(Unsigned32):
    """Custom type tnSlopePolicyQueueLoStartAverage based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopePolicyQueueLoStartAverage_Type.__name__ = "Unsigned32"
_TnSlopePolicyQueueLoStartAverage_Object = MibTableColumn
tnSlopePolicyQueueLoStartAverage = _TnSlopePolicyQueueLoStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 9),
    _TnSlopePolicyQueueLoStartAverage_Type()
)
tnSlopePolicyQueueLoStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueLoStartAverage.setStatus("current")


class _TnSlopePolicyQueueLoMaxAverage_Type(Unsigned32):
    """Custom type tnSlopePolicyQueueLoMaxAverage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopePolicyQueueLoMaxAverage_Type.__name__ = "Unsigned32"
_TnSlopePolicyQueueLoMaxAverage_Object = MibTableColumn
tnSlopePolicyQueueLoMaxAverage = _TnSlopePolicyQueueLoMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 10),
    _TnSlopePolicyQueueLoMaxAverage_Type()
)
tnSlopePolicyQueueLoMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueLoMaxAverage.setStatus("current")


class _TnSlopePolicyQueueLoMaxProbability_Type(TMaxProbability):
    """Custom type tnSlopePolicyQueueLoMaxProbability based on TMaxProbability"""
    defaultValue = 75


_TnSlopePolicyQueueLoMaxProbability_Type.__name__ = "TMaxProbability"
_TnSlopePolicyQueueLoMaxProbability_Object = MibTableColumn
tnSlopePolicyQueueLoMaxProbability = _TnSlopePolicyQueueLoMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 11),
    _TnSlopePolicyQueueLoMaxProbability_Type()
)
tnSlopePolicyQueueLoMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueLoMaxProbability.setStatus("current")


class _TnSlopePolicyQueueNonTcpAdminStatus_Type(Integer32):
    """Custom type tnSlopePolicyQueueNonTcpAdminStatus based on Integer32"""
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


_TnSlopePolicyQueueNonTcpAdminStatus_Type.__name__ = "Integer32"
_TnSlopePolicyQueueNonTcpAdminStatus_Object = MibTableColumn
tnSlopePolicyQueueNonTcpAdminStatus = _TnSlopePolicyQueueNonTcpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 12),
    _TnSlopePolicyQueueNonTcpAdminStatus_Type()
)
tnSlopePolicyQueueNonTcpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueNonTcpAdminStatus.setStatus("current")


class _TnSlopePolicyQueueNonTcpStartAverage_Type(Unsigned32):
    """Custom type tnSlopePolicyQueueNonTcpStartAverage based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopePolicyQueueNonTcpStartAverage_Type.__name__ = "Unsigned32"
_TnSlopePolicyQueueNonTcpStartAverage_Object = MibTableColumn
tnSlopePolicyQueueNonTcpStartAverage = _TnSlopePolicyQueueNonTcpStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 13),
    _TnSlopePolicyQueueNonTcpStartAverage_Type()
)
tnSlopePolicyQueueNonTcpStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueNonTcpStartAverage.setStatus("current")


class _TnSlopePolicyQueueNonTcpMaxAverage_Type(Unsigned32):
    """Custom type tnSlopePolicyQueueNonTcpMaxAverage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSlopePolicyQueueNonTcpMaxAverage_Type.__name__ = "Unsigned32"
_TnSlopePolicyQueueNonTcpMaxAverage_Object = MibTableColumn
tnSlopePolicyQueueNonTcpMaxAverage = _TnSlopePolicyQueueNonTcpMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 14),
    _TnSlopePolicyQueueNonTcpMaxAverage_Type()
)
tnSlopePolicyQueueNonTcpMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueNonTcpMaxAverage.setStatus("current")


class _TnSlopePolicyQueueNonTcpMaxProbability_Type(TMaxProbability):
    """Custom type tnSlopePolicyQueueNonTcpMaxProbability based on TMaxProbability"""
    defaultValue = 75


_TnSlopePolicyQueueNonTcpMaxProbability_Type.__name__ = "TMaxProbability"
_TnSlopePolicyQueueNonTcpMaxProbability_Object = MibTableColumn
tnSlopePolicyQueueNonTcpMaxProbability = _TnSlopePolicyQueueNonTcpMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 15),
    _TnSlopePolicyQueueNonTcpMaxProbability_Type()
)
tnSlopePolicyQueueNonTcpMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueNonTcpMaxProbability.setStatus("current")


class _TnSlopePolicyQueueTimeAvgFactor_Type(Unsigned32):
    """Custom type tnSlopePolicyQueueTimeAvgFactor based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TnSlopePolicyQueueTimeAvgFactor_Type.__name__ = "Unsigned32"
_TnSlopePolicyQueueTimeAvgFactor_Object = MibTableColumn
tnSlopePolicyQueueTimeAvgFactor = _TnSlopePolicyQueueTimeAvgFactor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 2, 1, 16),
    _TnSlopePolicyQueueTimeAvgFactor_Type()
)
tnSlopePolicyQueueTimeAvgFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlopePolicyQueueTimeAvgFactor.setStatus("current")
_TnSASSlopeScalar1_Type = Unsigned32
_TnSASSlopeScalar1_Object = MibScalar
tnSASSlopeScalar1 = _TnSASSlopeScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 101),
    _TnSASSlopeScalar1_Type()
)
tnSASSlopeScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASSlopeScalar1.setStatus("current")
_TnSASSlopeScalar2_Type = Unsigned32
_TnSASSlopeScalar2_Object = MibScalar
tnSASSlopeScalar2 = _TnSASSlopeScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 4, 102),
    _TnSASSlopeScalar2_Type()
)
tnSASSlopeScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASSlopeScalar2.setStatus("current")
_TnSASSchedulerObjects_ObjectIdentity = ObjectIdentity
tnSASSchedulerObjects = _TnSASSchedulerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5)
)
_TnSASPortSchedulerPlcyTable_Object = MibTable
tnSASPortSchedulerPlcyTable = _TnSASPortSchedulerPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnSASPortSchedulerPlcyTable.setStatus("current")
_TnSASPortSchedulerPlcyEntry_Object = MibTableRow
tnSASPortSchedulerPlcyEntry = _TnSASPortSchedulerPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tnSASPortSchedulerPlcyEntry.setStatus("current")
_TnPortSchedulerPlcyMode_Type = TPlcyMode
_TnPortSchedulerPlcyMode_Object = MibTableColumn
tnPortSchedulerPlcyMode = _TnPortSchedulerPlcyMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 1),
    _TnPortSchedulerPlcyMode_Type()
)
tnPortSchedulerPlcyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyMode.setStatus("current")


class _TnPortSchedulerPlcyQuanta_Type(TPlcyQuanta):
    """Custom type tnPortSchedulerPlcyQuanta based on TPlcyQuanta"""
    defaultValue = 0


_TnPortSchedulerPlcyQuanta_Type.__name__ = "TPlcyQuanta"
_TnPortSchedulerPlcyQuanta_Object = MibTableColumn
tnPortSchedulerPlcyQuanta = _TnPortSchedulerPlcyQuanta_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 2),
    _TnPortSchedulerPlcyQuanta_Type()
)
tnPortSchedulerPlcyQuanta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQuanta.setStatus("current")


class _TnPortSchedulerPlcyQueue1Weight_Type(TQWeight):
    """Custom type tnPortSchedulerPlcyQueue1Weight based on TQWeight"""
    defaultValue = 1


_TnPortSchedulerPlcyQueue1Weight_Type.__name__ = "TQWeight"
_TnPortSchedulerPlcyQueue1Weight_Object = MibTableColumn
tnPortSchedulerPlcyQueue1Weight = _TnPortSchedulerPlcyQueue1Weight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 3),
    _TnPortSchedulerPlcyQueue1Weight_Type()
)
tnPortSchedulerPlcyQueue1Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQueue1Weight.setStatus("current")


class _TnPortSchedulerPlcyQueue2Weight_Type(TQWeight):
    """Custom type tnPortSchedulerPlcyQueue2Weight based on TQWeight"""
    defaultValue = 1


_TnPortSchedulerPlcyQueue2Weight_Type.__name__ = "TQWeight"
_TnPortSchedulerPlcyQueue2Weight_Object = MibTableColumn
tnPortSchedulerPlcyQueue2Weight = _TnPortSchedulerPlcyQueue2Weight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 4),
    _TnPortSchedulerPlcyQueue2Weight_Type()
)
tnPortSchedulerPlcyQueue2Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQueue2Weight.setStatus("current")


class _TnPortSchedulerPlcyQueue3Weight_Type(TQWeight):
    """Custom type tnPortSchedulerPlcyQueue3Weight based on TQWeight"""
    defaultValue = 1


_TnPortSchedulerPlcyQueue3Weight_Type.__name__ = "TQWeight"
_TnPortSchedulerPlcyQueue3Weight_Object = MibTableColumn
tnPortSchedulerPlcyQueue3Weight = _TnPortSchedulerPlcyQueue3Weight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 5),
    _TnPortSchedulerPlcyQueue3Weight_Type()
)
tnPortSchedulerPlcyQueue3Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQueue3Weight.setStatus("current")


class _TnPortSchedulerPlcyQueue4Weight_Type(TQWeight):
    """Custom type tnPortSchedulerPlcyQueue4Weight based on TQWeight"""
    defaultValue = 1


_TnPortSchedulerPlcyQueue4Weight_Type.__name__ = "TQWeight"
_TnPortSchedulerPlcyQueue4Weight_Object = MibTableColumn
tnPortSchedulerPlcyQueue4Weight = _TnPortSchedulerPlcyQueue4Weight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 6),
    _TnPortSchedulerPlcyQueue4Weight_Type()
)
tnPortSchedulerPlcyQueue4Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQueue4Weight.setStatus("current")


class _TnPortSchedulerPlcyQueue5Weight_Type(TQWeight):
    """Custom type tnPortSchedulerPlcyQueue5Weight based on TQWeight"""
    defaultValue = 1


_TnPortSchedulerPlcyQueue5Weight_Type.__name__ = "TQWeight"
_TnPortSchedulerPlcyQueue5Weight_Object = MibTableColumn
tnPortSchedulerPlcyQueue5Weight = _TnPortSchedulerPlcyQueue5Weight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 7),
    _TnPortSchedulerPlcyQueue5Weight_Type()
)
tnPortSchedulerPlcyQueue5Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQueue5Weight.setStatus("current")


class _TnPortSchedulerPlcyQueue6Weight_Type(TQWeight):
    """Custom type tnPortSchedulerPlcyQueue6Weight based on TQWeight"""
    defaultValue = 1


_TnPortSchedulerPlcyQueue6Weight_Type.__name__ = "TQWeight"
_TnPortSchedulerPlcyQueue6Weight_Object = MibTableColumn
tnPortSchedulerPlcyQueue6Weight = _TnPortSchedulerPlcyQueue6Weight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 8),
    _TnPortSchedulerPlcyQueue6Weight_Type()
)
tnPortSchedulerPlcyQueue6Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQueue6Weight.setStatus("current")


class _TnPortSchedulerPlcyQueue7Weight_Type(TQWeight):
    """Custom type tnPortSchedulerPlcyQueue7Weight based on TQWeight"""
    defaultValue = 1


_TnPortSchedulerPlcyQueue7Weight_Type.__name__ = "TQWeight"
_TnPortSchedulerPlcyQueue7Weight_Object = MibTableColumn
tnPortSchedulerPlcyQueue7Weight = _TnPortSchedulerPlcyQueue7Weight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 9),
    _TnPortSchedulerPlcyQueue7Weight_Type()
)
tnPortSchedulerPlcyQueue7Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQueue7Weight.setStatus("current")


class _TnPortSchedulerPlcyQueue8Weight_Type(TQWeight):
    """Custom type tnPortSchedulerPlcyQueue8Weight based on TQWeight"""
    defaultValue = 1


_TnPortSchedulerPlcyQueue8Weight_Type.__name__ = "TQWeight"
_TnPortSchedulerPlcyQueue8Weight_Object = MibTableColumn
tnPortSchedulerPlcyQueue8Weight = _TnPortSchedulerPlcyQueue8Weight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 5, 1, 1, 10),
    _TnPortSchedulerPlcyQueue8Weight_Type()
)
tnPortSchedulerPlcyQueue8Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortSchedulerPlcyQueue8Weight.setStatus("current")
_TnQosFrameBasedAccntObjects_ObjectIdentity = ObjectIdentity
tnQosFrameBasedAccntObjects = _TnQosFrameBasedAccntObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 6)
)
_TnQosFrameBasedAccntTable_Object = MibTable
tnQosFrameBasedAccntTable = _TnQosFrameBasedAccntTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tnQosFrameBasedAccntTable.setStatus("current")
_TnQosFrameBasedAccntEntry_Object = MibTableRow
tnQosFrameBasedAccntEntry = _TnQosFrameBasedAccntEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 6, 3, 1)
)
tnQosFrameBasedAccntEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnQosFrameBasedAccntEntry.setStatus("current")


class _TnQosIngressFrameBasedAccnt_Type(TruthValue):
    """Custom type tnQosIngressFrameBasedAccnt based on TruthValue"""
    defaultValue = 2


_TnQosIngressFrameBasedAccnt_Type.__name__ = "TruthValue"
_TnQosIngressFrameBasedAccnt_Object = MibTableColumn
tnQosIngressFrameBasedAccnt = _TnQosIngressFrameBasedAccnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 6, 3, 1, 1),
    _TnQosIngressFrameBasedAccnt_Type()
)
tnQosIngressFrameBasedAccnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosIngressFrameBasedAccnt.setStatus("current")


class _TnQosEgressFrameBasedAccnt_Type(TruthValue):
    """Custom type tnQosEgressFrameBasedAccnt based on TruthValue"""
    defaultValue = 2


_TnQosEgressFrameBasedAccnt_Type.__name__ = "TruthValue"
_TnQosEgressFrameBasedAccnt_Object = MibTableColumn
tnQosEgressFrameBasedAccnt = _TnQosEgressFrameBasedAccnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 6, 3, 1, 2),
    _TnQosEgressFrameBasedAccnt_Type()
)
tnQosEgressFrameBasedAccnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosEgressFrameBasedAccnt.setStatus("current")
_TnSASNetworkObjects_ObjectIdentity = ObjectIdentity
tnSASNetworkObjects = _TnSASNetworkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7)
)
_TnNetworkPolicyExtnTable_Object = MibTable
tnNetworkPolicyExtnTable = _TnNetworkPolicyExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tnNetworkPolicyExtnTable.setStatus("current")
_TnNetworkPolicyExtnEntry_Object = MibTableRow
tnNetworkPolicyExtnEntry = _TnNetworkPolicyExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    tnNetworkPolicyExtnEntry.setStatus("current")


class _TnNetworkPolicyType_Type(TNetworkPolicyType):
    """Custom type tnNetworkPolicyType based on TNetworkPolicyType"""
    defaultValue = 1


_TnNetworkPolicyType_Type.__name__ = "TNetworkPolicyType"
_TnNetworkPolicyType_Object = MibTableColumn
tnNetworkPolicyType = _TnNetworkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 1, 1, 1),
    _TnNetworkPolicyType_Type()
)
tnNetworkPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyType.setStatus("current")


class _TnNetworkPolicyRemarkPolicyId_Type(TRemarkPolicyID):
    """Custom type tnNetworkPolicyRemarkPolicyId based on TRemarkPolicyID"""
    defaultValue = 2


_TnNetworkPolicyRemarkPolicyId_Type.__name__ = "TRemarkPolicyID"
_TnNetworkPolicyRemarkPolicyId_Object = MibTableColumn
tnNetworkPolicyRemarkPolicyId = _TnNetworkPolicyRemarkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 1, 1, 2),
    _TnNetworkPolicyRemarkPolicyId_Type()
)
tnNetworkPolicyRemarkPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkPolicyRemarkPolicyId.setStatus("current")


class _TnNetworkIngressMeterColorMode_Type(Integer32):
    """Custom type tnNetworkIngressMeterColorMode based on Integer32"""
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


_TnNetworkIngressMeterColorMode_Type.__name__ = "Integer32"
_TnNetworkIngressMeterColorMode_Object = MibTableColumn
tnNetworkIngressMeterColorMode = _TnNetworkIngressMeterColorMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 1, 1, 3),
    _TnNetworkIngressMeterColorMode_Type()
)
tnNetworkIngressMeterColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkIngressMeterColorMode.setStatus("current")


class _TnNetworkIngressMplsLspExpProfile_Type(TMplsLspExpProfMapID):
    """Custom type tnNetworkIngressMplsLspExpProfile based on TMplsLspExpProfMapID"""
    defaultValue = 1


_TnNetworkIngressMplsLspExpProfile_Type.__name__ = "TMplsLspExpProfMapID"
_TnNetworkIngressMplsLspExpProfile_Object = MibTableColumn
tnNetworkIngressMplsLspExpProfile = _TnNetworkIngressMplsLspExpProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 1, 1, 4),
    _TnNetworkIngressMplsLspExpProfile_Type()
)
tnNetworkIngressMplsLspExpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNetworkIngressMplsLspExpProfile.setStatus("current")


class _TnNetworkEgressRemarkType_Type(Integer32):
    """Custom type tnNetworkEgressRemarkType based on Integer32"""
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


_TnNetworkEgressRemarkType_Type.__name__ = "Integer32"
_TnNetworkEgressRemarkType_Object = MibTableColumn
tnNetworkEgressRemarkType = _TnNetworkEgressRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 1, 1, 5),
    _TnNetworkEgressRemarkType_Type()
)
tnNetworkEgressRemarkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkEgressRemarkType.setStatus("current")
_TnNetworkQueueExtnTable_Object = MibTable
tnNetworkQueueExtnTable = _TnNetworkQueueExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    tnNetworkQueueExtnTable.setStatus("current")
_TnNetworkQueueExtnEntry_Object = MibTableRow
tnNetworkQueueExtnEntry = _TnNetworkQueueExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    tnNetworkQueueExtnEntry.setStatus("current")


class _TnNetworkQueuePolicyName_Type(TNamedItem):
    """Custom type tnNetworkQueuePolicyName based on TNamedItem"""
    defaultValue = OctetString("default")


_TnNetworkQueuePolicyName_Type.__name__ = "TNamedItem"
_TnNetworkQueuePolicyName_Object = MibTableColumn
tnNetworkQueuePolicyName = _TnNetworkQueuePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 7, 2, 1, 1),
    _TnNetworkQueuePolicyName_Type()
)
tnNetworkQueuePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetworkQueuePolicyName.setStatus("current")
_TnSASGeneralQosObjects_ObjectIdentity = ObjectIdentity
tnSASGeneralQosObjects = _TnSASGeneralQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21)
)
_TnSASRemarkPolicyTable_Object = MibTable
tnSASRemarkPolicyTable = _TnSASRemarkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    tnSASRemarkPolicyTable.setStatus("current")
_TnSASRemarkPolicyEntry_Object = MibTableRow
tnSASRemarkPolicyEntry = _TnSASRemarkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 1, 1)
)
tnSASRemarkPolicyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SAS-QOS-MIB", "tnSASRemarkPolicyId"),
)
if mibBuilder.loadTexts:
    tnSASRemarkPolicyEntry.setStatus("current")
_TnSASRemarkPolicyId_Type = TRemarkPolicyID
_TnSASRemarkPolicyId_Object = MibTableColumn
tnSASRemarkPolicyId = _TnSASRemarkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 1, 1, 1),
    _TnSASRemarkPolicyId_Type()
)
tnSASRemarkPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyId.setStatus("current")
_TnSASRemarkPolicyRowStatus_Type = RowStatus
_TnSASRemarkPolicyRowStatus_Object = MibTableColumn
tnSASRemarkPolicyRowStatus = _TnSASRemarkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 1, 1, 2),
    _TnSASRemarkPolicyRowStatus_Type()
)
tnSASRemarkPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyRowStatus.setStatus("current")


class _TnSASRemarkPolicyDescription_Type(TItemDescription):
    """Custom type tnSASRemarkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TnSASRemarkPolicyDescription_Type.__name__ = "TItemDescription"
_TnSASRemarkPolicyDescription_Object = MibTableColumn
tnSASRemarkPolicyDescription = _TnSASRemarkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 1, 1, 3),
    _TnSASRemarkPolicyDescription_Type()
)
tnSASRemarkPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyDescription.setStatus("current")


class _TnSASRemarkPolicyType_Type(Integer32):
    """Custom type tnSASRemarkPolicyType based on Integer32"""
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


_TnSASRemarkPolicyType_Type.__name__ = "Integer32"
_TnSASRemarkPolicyType_Object = MibTableColumn
tnSASRemarkPolicyType = _TnSASRemarkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 1, 1, 4),
    _TnSASRemarkPolicyType_Type()
)
tnSASRemarkPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyType.setStatus("current")
_TnSASRemarkPolicyLastChanged_Type = TimeStamp
_TnSASRemarkPolicyLastChanged_Object = MibTableColumn
tnSASRemarkPolicyLastChanged = _TnSASRemarkPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 1, 1, 5),
    _TnSASRemarkPolicyLastChanged_Type()
)
tnSASRemarkPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyLastChanged.setStatus("current")
_TnSASRemarkPolicyFCTable_Object = MibTable
tnSASRemarkPolicyFCTable = _TnSASRemarkPolicyFCTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2)
)
if mibBuilder.loadTexts:
    tnSASRemarkPolicyFCTable.setStatus("current")
_TnSASRemarkPolicyFCEntry_Object = MibTableRow
tnSASRemarkPolicyFCEntry = _TnSASRemarkPolicyFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1)
)
tnSASRemarkPolicyFCEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SAS-QOS-MIB", "tnSASRemarkPolicyId"),
    (0, "TN-SAS-QOS-MIB", "tnSASRemarkPolicyFCName"),
)
if mibBuilder.loadTexts:
    tnSASRemarkPolicyFCEntry.setStatus("current")
_TnSASRemarkPolicyFCName_Type = TFCName
_TnSASRemarkPolicyFCName_Object = MibTableColumn
tnSASRemarkPolicyFCName = _TnSASRemarkPolicyFCName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 1),
    _TnSASRemarkPolicyFCName_Type()
)
tnSASRemarkPolicyFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyFCName.setStatus("current")


class _TnSASRemarkPolicyDot1PInProfile_Type(Dot1PPriority):
    """Custom type tnSASRemarkPolicyDot1PInProfile based on Dot1PPriority"""
    defaultValue = -1


_TnSASRemarkPolicyDot1PInProfile_Type.__name__ = "Dot1PPriority"
_TnSASRemarkPolicyDot1PInProfile_Object = MibTableColumn
tnSASRemarkPolicyDot1PInProfile = _TnSASRemarkPolicyDot1PInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 2),
    _TnSASRemarkPolicyDot1PInProfile_Type()
)
tnSASRemarkPolicyDot1PInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyDot1PInProfile.setStatus("current")


class _TnSASRemarkPolicyDot1POutProfile_Type(Dot1PPriority):
    """Custom type tnSASRemarkPolicyDot1POutProfile based on Dot1PPriority"""
    defaultValue = -1


_TnSASRemarkPolicyDot1POutProfile_Type.__name__ = "Dot1PPriority"
_TnSASRemarkPolicyDot1POutProfile_Object = MibTableColumn
tnSASRemarkPolicyDot1POutProfile = _TnSASRemarkPolicyDot1POutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 3),
    _TnSASRemarkPolicyDot1POutProfile_Type()
)
tnSASRemarkPolicyDot1POutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyDot1POutProfile.setStatus("current")


class _TnSASRemarkPolicyDSCPInProfile_Type(TDSCPNameOrEmpty):
    """Custom type tnSASRemarkPolicyDSCPInProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TnSASRemarkPolicyDSCPInProfile_Type.__name__ = "TDSCPNameOrEmpty"
_TnSASRemarkPolicyDSCPInProfile_Object = MibTableColumn
tnSASRemarkPolicyDSCPInProfile = _TnSASRemarkPolicyDSCPInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 4),
    _TnSASRemarkPolicyDSCPInProfile_Type()
)
tnSASRemarkPolicyDSCPInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyDSCPInProfile.setStatus("current")


class _TnSASRemarkPolicyDSCPOutProfile_Type(TDSCPNameOrEmpty):
    """Custom type tnSASRemarkPolicyDSCPOutProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TnSASRemarkPolicyDSCPOutProfile_Type.__name__ = "TDSCPNameOrEmpty"
_TnSASRemarkPolicyDSCPOutProfile_Object = MibTableColumn
tnSASRemarkPolicyDSCPOutProfile = _TnSASRemarkPolicyDSCPOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 5),
    _TnSASRemarkPolicyDSCPOutProfile_Type()
)
tnSASRemarkPolicyDSCPOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyDSCPOutProfile.setStatus("current")


class _TnSASRemarkPolicyLspExpInProfile_Type(TLspExpValue):
    """Custom type tnSASRemarkPolicyLspExpInProfile based on TLspExpValue"""
    defaultValue = -1


_TnSASRemarkPolicyLspExpInProfile_Type.__name__ = "TLspExpValue"
_TnSASRemarkPolicyLspExpInProfile_Object = MibTableColumn
tnSASRemarkPolicyLspExpInProfile = _TnSASRemarkPolicyLspExpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 6),
    _TnSASRemarkPolicyLspExpInProfile_Type()
)
tnSASRemarkPolicyLspExpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyLspExpInProfile.setStatus("current")


class _TnSASRemarkPolicyLspExpOutProfile_Type(TLspExpValue):
    """Custom type tnSASRemarkPolicyLspExpOutProfile based on TLspExpValue"""
    defaultValue = -1


_TnSASRemarkPolicyLspExpOutProfile_Type.__name__ = "TLspExpValue"
_TnSASRemarkPolicyLspExpOutProfile_Object = MibTableColumn
tnSASRemarkPolicyLspExpOutProfile = _TnSASRemarkPolicyLspExpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 7),
    _TnSASRemarkPolicyLspExpOutProfile_Type()
)
tnSASRemarkPolicyLspExpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyLspExpOutProfile.setStatus("current")


class _TnSASRemarkPolicyDot1PLspExpInProfile_Type(TDot1PLspExpValue):
    """Custom type tnSASRemarkPolicyDot1PLspExpInProfile based on TDot1PLspExpValue"""
    defaultValue = -1


_TnSASRemarkPolicyDot1PLspExpInProfile_Type.__name__ = "TDot1PLspExpValue"
_TnSASRemarkPolicyDot1PLspExpInProfile_Object = MibTableColumn
tnSASRemarkPolicyDot1PLspExpInProfile = _TnSASRemarkPolicyDot1PLspExpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 8),
    _TnSASRemarkPolicyDot1PLspExpInProfile_Type()
)
tnSASRemarkPolicyDot1PLspExpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyDot1PLspExpInProfile.setStatus("current")


class _TnSASRemarkPolicyDot1PLspExpOutProfile_Type(TDot1PLspExpValue):
    """Custom type tnSASRemarkPolicyDot1PLspExpOutProfile based on TDot1PLspExpValue"""
    defaultValue = -1


_TnSASRemarkPolicyDot1PLspExpOutProfile_Type.__name__ = "TDot1PLspExpValue"
_TnSASRemarkPolicyDot1PLspExpOutProfile_Object = MibTableColumn
tnSASRemarkPolicyDot1PLspExpOutProfile = _TnSASRemarkPolicyDot1PLspExpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 1, 21, 2, 1, 9),
    _TnSASRemarkPolicyDot1PLspExpOutProfile_Type()
)
tnSASRemarkPolicyDot1PLspExpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSASRemarkPolicyDot1PLspExpOutProfile.setStatus("current")
tnSapIngressFCEntry.registerAugmentions(
    ("TN-SAS-QOS-MIB",
     "tnSASSapIngressFCEntry")
)
tnSASSapIngressFCEntry.setIndexNames(*tnSapIngressFCEntry.getIndexNames())
tnSapIngressEntry.registerAugmentions(
    ("TN-SAS-QOS-MIB",
     "tnSapIngressExtnEntry")
)
tnSapIngressExtnEntry.setIndexNames(*tnSapIngressEntry.getIndexNames())
tnSlopePolicyEntry.registerAugmentions(
    ("TN-SAS-QOS-MIB",
     "tnSASSlopePolicyExtnEntry")
)
tnSASSlopePolicyExtnEntry.setIndexNames(*tnSlopePolicyEntry.getIndexNames())
tnPortSchedulerPlcyEntry.registerAugmentions(
    ("TN-SAS-QOS-MIB",
     "tnSASPortSchedulerPlcyEntry")
)
tnSASPortSchedulerPlcyEntry.setIndexNames(*tnPortSchedulerPlcyEntry.getIndexNames())
tnNetworkPolicyEntry.registerAugmentions(
    ("TN-SAS-QOS-MIB",
     "tnNetworkPolicyExtnEntry")
)
tnNetworkPolicyExtnEntry.setIndexNames(*tnNetworkPolicyEntry.getIndexNames())
tnNetworkQueueEntry.registerAugmentions(
    ("TN-SAS-QOS-MIB",
     "tnNetworkQueueExtnEntry")
)
tnNetworkQueueExtnEntry.setIndexNames(*tnNetworkQueueEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAS-QOS-MIB",
    **{"TAccessEgressPolicyID": TAccessEgressPolicyID,
       "TRemarkPolicyID": TRemarkPolicyID,
       "TIngressCIRRate": TIngressCIRRate,
       "TIngressPIRRate": TIngressPIRRate,
       "TIngressBurstSize": TIngressBurstSize,
       "TMeterRateMode": TMeterRateMode,
       "TPlcyQuanta": TPlcyQuanta,
       "TMatchCriteria": TMatchCriteria,
       "TAtmTdpDescrType": TAtmTdpDescrType,
       "TSlopeDropRate": TSlopeDropRate,
       "TSlopeThreshold": TSlopeThreshold,
       "TMaxProbability": TMaxProbability,
       "TNetworkPolicyType": TNetworkPolicyType,
       "TDot1PLspExpValue": TDot1PLspExpValue,
       "TMplsLspExpProfileValue": TMplsLspExpProfileValue,
       "tnSASQosMIBModule": tnSASQosMIBModule,
       "tnSASQosObjects": tnSASQosObjects,
       "tnAccessEgressObjects": tnAccessEgressObjects,
       "tnAccessEgressTable": tnAccessEgressTable,
       "tnAccessEgressEntry": tnAccessEgressEntry,
       "tnAccessEgressIndex": tnAccessEgressIndex,
       "tnAccessEgressRowStatus": tnAccessEgressRowStatus,
       "tnAccessEgressScope": tnAccessEgressScope,
       "tnAccessEgressDescription": tnAccessEgressDescription,
       "tnAccessEgressLastChanged": tnAccessEgressLastChanged,
       "tnAccessEgressRemark": tnAccessEgressRemark,
       "tnAccessEgressRemarkPolicyId": tnAccessEgressRemarkPolicyId,
       "tnAccessEgressRemarkType": tnAccessEgressRemarkType,
       "tnAccessEgressQueueTable": tnAccessEgressQueueTable,
       "tnAccessEgressQueueEntry": tnAccessEgressQueueEntry,
       "tnAccessEgressQueueIndex": tnAccessEgressQueueIndex,
       "tnAccessEgressQueueRowStatus": tnAccessEgressQueueRowStatus,
       "tnAccessEgressQueueCBS": tnAccessEgressQueueCBS,
       "tnAccessEgressQueueMBS": tnAccessEgressQueueMBS,
       "tnAccessEgressQueuePIRAdaptation": tnAccessEgressQueuePIRAdaptation,
       "tnAccessEgressQueueCIRAdaptation": tnAccessEgressQueueCIRAdaptation,
       "tnAccessEgressQueueAdminPIR": tnAccessEgressQueueAdminPIR,
       "tnAccessEgressQueueAdminCIR": tnAccessEgressQueueAdminCIR,
       "tnAccessEgressQueueOperPIR": tnAccessEgressQueueOperPIR,
       "tnAccessEgressQueueOperCIR": tnAccessEgressQueueOperCIR,
       "tnAccessEgressQueueLastChanged": tnAccessEgressQueueLastChanged,
       "tnAccessEgressFCTable": tnAccessEgressFCTable,
       "tnAccessEgressFCEntry": tnAccessEgressFCEntry,
       "tnAccessEgressFCName": tnAccessEgressFCName,
       "tnAccessEgressFCRowStatus": tnAccessEgressFCRowStatus,
       "tnAccessEgressFCQueue": tnAccessEgressFCQueue,
       "tnAccessEgressFCDot1PInProfile": tnAccessEgressFCDot1PInProfile,
       "tnAccessEgressFCDot1POutProfile": tnAccessEgressFCDot1POutProfile,
       "tnAccessEgressFCLastChanged": tnAccessEgressFCLastChanged,
       "tnAccessEgressFCDscpInProfile": tnAccessEgressFCDscpInProfile,
       "tnAccessEgressFCDscpOutProfile": tnAccessEgressFCDscpOutProfile,
       "tnAccessEgressScalar1": tnAccessEgressScalar1,
       "tnAccessEgressScalar2": tnAccessEgressScalar2,
       "tnSASSapIngressObjects": tnSASSapIngressObjects,
       "tnSapIngressMeterTable": tnSapIngressMeterTable,
       "tnSapIngressMeterEntry": tnSapIngressMeterEntry,
       "tnSapIngressMeter": tnSapIngressMeter,
       "tnSapIngressMeterRowStatus": tnSapIngressMeterRowStatus,
       "tnSapIngressMeterMCast": tnSapIngressMeterMCast,
       "tnSapIngressMeterPIRAdaptation": tnSapIngressMeterPIRAdaptation,
       "tnSapIngressMeterCIRAdaptation": tnSapIngressMeterCIRAdaptation,
       "tnSapIngressMeterAdminPIR": tnSapIngressMeterAdminPIR,
       "tnSapIngressMeterAdminCIR": tnSapIngressMeterAdminCIR,
       "tnSapIngressMeterOperPIR": tnSapIngressMeterOperPIR,
       "tnSapIngressMeterOperCIR": tnSapIngressMeterOperCIR,
       "tnSapIngressMeterLastChanged": tnSapIngressMeterLastChanged,
       "tnSapIngressMeterMode": tnSapIngressMeterMode,
       "tnSapIngressMeterRateMode": tnSapIngressMeterRateMode,
       "tnSapIngressMeterAdminCBS": tnSapIngressMeterAdminCBS,
       "tnSapIngressMeterAdminMBS": tnSapIngressMeterAdminMBS,
       "tnSapIngressMeterOperCBS": tnSapIngressMeterOperCBS,
       "tnSapIngressMeterOperMBS": tnSapIngressMeterOperMBS,
       "tnSASSapIngressFCTable": tnSASSapIngressFCTable,
       "tnSASSapIngressFCEntry": tnSASSapIngressFCEntry,
       "tnSapIngressFCMeter": tnSapIngressFCMeter,
       "tnSapIngressFCMCastMeter": tnSapIngressFCMCastMeter,
       "tnSapIngressFCBCastMeter": tnSapIngressFCBCastMeter,
       "tnSapIngressFCUnknownMeter": tnSapIngressFCUnknownMeter,
       "tnSapIngQosMeterStatsTable": tnSapIngQosMeterStatsTable,
       "tnSapIngQosMeterStatsEntry": tnSapIngQosMeterStatsEntry,
       "tnSapIngQosMeterId": tnSapIngQosMeterId,
       "tnSapIngQosMeterStatsForwardedInProfPackets": tnSapIngQosMeterStatsForwardedInProfPackets,
       "tnSapIngQosMeterStatsForwardedOutProfPackets": tnSapIngQosMeterStatsForwardedOutProfPackets,
       "tnSapIngQosMeterStatsForwardedInProfOctets": tnSapIngQosMeterStatsForwardedInProfOctets,
       "tnSapIngQosMeterStatsForwardedOutProfOctets": tnSapIngQosMeterStatsForwardedOutProfOctets,
       "tnSapIngQosMeterStatsForwardedPackets": tnSapIngQosMeterStatsForwardedPackets,
       "tnSapIngQosMeterStatsForwardedOctets": tnSapIngQosMeterStatsForwardedOctets,
       "tnSapIngQosMeterStatsDroppedPackets": tnSapIngQosMeterStatsDroppedPackets,
       "tnSapIngQosMeterStatsDroppedOctets": tnSapIngQosMeterStatsDroppedOctets,
       "tnSapIngressExtnTable": tnSapIngressExtnTable,
       "tnSapIngressExtnEntry": tnSapIngressExtnEntry,
       "tnSapIngressNumQosClassifiers": tnSapIngressNumQosClassifiers,
       "tnSapIngressQosClassifiersRequiredInVpls": tnSapIngressQosClassifiersRequiredInVpls,
       "tnSapIngressQosClassifiersRequiredInEpipe": tnSapIngressQosClassifiersRequiredInEpipe,
       "tnSapIngressQosMetersRequiredInVpls": tnSapIngressQosMetersRequiredInVpls,
       "tnSapIngressQosMetersRequiredInEpipe": tnSapIngressQosMetersRequiredInEpipe,
       "tnSapIngressIPCriteriaMatch": tnSapIngressIPCriteriaMatch,
       "tnSapIngressMacCriteriaMatch": tnSapIngressMacCriteriaMatch,
       "tnSapIngressIPv6CriteriaEnable": tnSapIngressIPv6CriteriaEnable,
       "tnSapIngressIPv6CriteriaMatch": tnSapIngressIPv6CriteriaMatch,
       "tnSASSapIngressScalar1": tnSASSapIngressScalar1,
       "tnSASSapIngressScalar2": tnSASSapIngressScalar2,
       "tnSASNetworkIngressObjects": tnSASNetworkIngressObjects,
       "tnNetworkIngressFCTable": tnNetworkIngressFCTable,
       "tnNetworkIngressFCEntry": tnNetworkIngressFCEntry,
       "tnNetworkIngressFCName": tnNetworkIngressFCName,
       "tnNetworkIngressFCRowStatus": tnNetworkIngressFCRowStatus,
       "tnNetworkIngressFCMeter": tnNetworkIngressFCMeter,
       "tnNetworkIngressFCMCastMeter": tnNetworkIngressFCMCastMeter,
       "tnNetworkIngressFCLastChanged": tnNetworkIngressFCLastChanged,
       "tnNetworkIngressMeterTable": tnNetworkIngressMeterTable,
       "tnNetworkIngressMeterEntry": tnNetworkIngressMeterEntry,
       "tnNetworkIngressMeterIndex": tnNetworkIngressMeterIndex,
       "tnNetworkIngressMeterRowStatus": tnNetworkIngressMeterRowStatus,
       "tnNetworkIngressMeterCIRAdaptation": tnNetworkIngressMeterCIRAdaptation,
       "tnNetworkIngressMeterPIRAdaptation": tnNetworkIngressMeterPIRAdaptation,
       "tnNetworkIngressMeterAdminPIR": tnNetworkIngressMeterAdminPIR,
       "tnNetworkIngressMeterAdminCIR": tnNetworkIngressMeterAdminCIR,
       "tnNetworkIngressMeterOperPIR": tnNetworkIngressMeterOperPIR,
       "tnNetworkIngressMeterOperCIR": tnNetworkIngressMeterOperCIR,
       "tnNetworkIngressMeterLastChanged": tnNetworkIngressMeterLastChanged,
       "tnNetworkIngressMeterMode": tnNetworkIngressMeterMode,
       "tnNetworkIngressMeterMCast": tnNetworkIngressMeterMCast,
       "tnNetworkIngressMeterRateMode": tnNetworkIngressMeterRateMode,
       "tnNetworkIngressMeterAdminCBS": tnNetworkIngressMeterAdminCBS,
       "tnNetworkIngressMeterAdminMBS": tnNetworkIngressMeterAdminMBS,
       "tnNetworkIngressMeterOperCBS": tnNetworkIngressMeterOperCBS,
       "tnNetworkIngressMeterOperMBS": tnNetworkIngressMeterOperMBS,
       "tnSASNetworkIngressScalar1": tnSASNetworkIngressScalar1,
       "tnSASNetworkIngressScalar2": tnSASNetworkIngressScalar2,
       "tnSASSlopeObjects": tnSASSlopeObjects,
       "tnSASSlopePolicyExtnTable": tnSASSlopePolicyExtnTable,
       "tnSASSlopePolicyExtnEntry": tnSASSlopePolicyExtnEntry,
       "tnSlopeHiQueue1DropRate": tnSlopeHiQueue1DropRate,
       "tnSlopeHiQueue2DropRate": tnSlopeHiQueue2DropRate,
       "tnSlopeHiQueue3DropRate": tnSlopeHiQueue3DropRate,
       "tnSlopeHiQueue4DropRate": tnSlopeHiQueue4DropRate,
       "tnSlopeHiQueue5DropRate": tnSlopeHiQueue5DropRate,
       "tnSlopeHiQueue6DropRate": tnSlopeHiQueue6DropRate,
       "tnSlopeHiQueue7DropRate": tnSlopeHiQueue7DropRate,
       "tnSlopeHiQueue8DropRate": tnSlopeHiQueue8DropRate,
       "tnSlopeLoQueue1DropRate": tnSlopeLoQueue1DropRate,
       "tnSlopeLoQueue2DropRate": tnSlopeLoQueue2DropRate,
       "tnSlopeLoQueue3DropRate": tnSlopeLoQueue3DropRate,
       "tnSlopeLoQueue4DropRate": tnSlopeLoQueue4DropRate,
       "tnSlopeLoQueue5DropRate": tnSlopeLoQueue5DropRate,
       "tnSlopeLoQueue6DropRate": tnSlopeLoQueue6DropRate,
       "tnSlopeLoQueue7DropRate": tnSlopeLoQueue7DropRate,
       "tnSlopeLoQueue8DropRate": tnSlopeLoQueue8DropRate,
       "tnSlopeHiStartThreshold": tnSlopeHiStartThreshold,
       "tnSlopeLoStartThreshold": tnSlopeLoStartThreshold,
       "tnSlopePolicyQueueTable": tnSlopePolicyQueueTable,
       "tnSlopePolicyQueueEntry": tnSlopePolicyQueueEntry,
       "tnSlopePolicyQueueId": tnSlopePolicyQueueId,
       "tnSlopePolicyQueueRowStatus": tnSlopePolicyQueueRowStatus,
       "tnSlopePolicyQueueLastChanged": tnSlopePolicyQueueLastChanged,
       "tnSlopePolicyQueueHiAdminStatus": tnSlopePolicyQueueHiAdminStatus,
       "tnSlopePolicyQueueHiStartAverage": tnSlopePolicyQueueHiStartAverage,
       "tnSlopePolicyQueueHiMaxAverage": tnSlopePolicyQueueHiMaxAverage,
       "tnSlopePolicyQueueHiMaxProbability": tnSlopePolicyQueueHiMaxProbability,
       "tnSlopePolicyQueueLoAdminStatus": tnSlopePolicyQueueLoAdminStatus,
       "tnSlopePolicyQueueLoStartAverage": tnSlopePolicyQueueLoStartAverage,
       "tnSlopePolicyQueueLoMaxAverage": tnSlopePolicyQueueLoMaxAverage,
       "tnSlopePolicyQueueLoMaxProbability": tnSlopePolicyQueueLoMaxProbability,
       "tnSlopePolicyQueueNonTcpAdminStatus": tnSlopePolicyQueueNonTcpAdminStatus,
       "tnSlopePolicyQueueNonTcpStartAverage": tnSlopePolicyQueueNonTcpStartAverage,
       "tnSlopePolicyQueueNonTcpMaxAverage": tnSlopePolicyQueueNonTcpMaxAverage,
       "tnSlopePolicyQueueNonTcpMaxProbability": tnSlopePolicyQueueNonTcpMaxProbability,
       "tnSlopePolicyQueueTimeAvgFactor": tnSlopePolicyQueueTimeAvgFactor,
       "tnSASSlopeScalar1": tnSASSlopeScalar1,
       "tnSASSlopeScalar2": tnSASSlopeScalar2,
       "tnSASSchedulerObjects": tnSASSchedulerObjects,
       "tnSASPortSchedulerPlcyTable": tnSASPortSchedulerPlcyTable,
       "tnSASPortSchedulerPlcyEntry": tnSASPortSchedulerPlcyEntry,
       "tnPortSchedulerPlcyMode": tnPortSchedulerPlcyMode,
       "tnPortSchedulerPlcyQuanta": tnPortSchedulerPlcyQuanta,
       "tnPortSchedulerPlcyQueue1Weight": tnPortSchedulerPlcyQueue1Weight,
       "tnPortSchedulerPlcyQueue2Weight": tnPortSchedulerPlcyQueue2Weight,
       "tnPortSchedulerPlcyQueue3Weight": tnPortSchedulerPlcyQueue3Weight,
       "tnPortSchedulerPlcyQueue4Weight": tnPortSchedulerPlcyQueue4Weight,
       "tnPortSchedulerPlcyQueue5Weight": tnPortSchedulerPlcyQueue5Weight,
       "tnPortSchedulerPlcyQueue6Weight": tnPortSchedulerPlcyQueue6Weight,
       "tnPortSchedulerPlcyQueue7Weight": tnPortSchedulerPlcyQueue7Weight,
       "tnPortSchedulerPlcyQueue8Weight": tnPortSchedulerPlcyQueue8Weight,
       "tnQosFrameBasedAccntObjects": tnQosFrameBasedAccntObjects,
       "tnQosFrameBasedAccntTable": tnQosFrameBasedAccntTable,
       "tnQosFrameBasedAccntEntry": tnQosFrameBasedAccntEntry,
       "tnQosIngressFrameBasedAccnt": tnQosIngressFrameBasedAccnt,
       "tnQosEgressFrameBasedAccnt": tnQosEgressFrameBasedAccnt,
       "tnSASNetworkObjects": tnSASNetworkObjects,
       "tnNetworkPolicyExtnTable": tnNetworkPolicyExtnTable,
       "tnNetworkPolicyExtnEntry": tnNetworkPolicyExtnEntry,
       "tnNetworkPolicyType": tnNetworkPolicyType,
       "tnNetworkPolicyRemarkPolicyId": tnNetworkPolicyRemarkPolicyId,
       "tnNetworkIngressMeterColorMode": tnNetworkIngressMeterColorMode,
       "tnNetworkIngressMplsLspExpProfile": tnNetworkIngressMplsLspExpProfile,
       "tnNetworkEgressRemarkType": tnNetworkEgressRemarkType,
       "tnNetworkQueueExtnTable": tnNetworkQueueExtnTable,
       "tnNetworkQueueExtnEntry": tnNetworkQueueExtnEntry,
       "tnNetworkQueuePolicyName": tnNetworkQueuePolicyName,
       "tnSASGeneralQosObjects": tnSASGeneralQosObjects,
       "tnSASRemarkPolicyTable": tnSASRemarkPolicyTable,
       "tnSASRemarkPolicyEntry": tnSASRemarkPolicyEntry,
       "tnSASRemarkPolicyId": tnSASRemarkPolicyId,
       "tnSASRemarkPolicyRowStatus": tnSASRemarkPolicyRowStatus,
       "tnSASRemarkPolicyDescription": tnSASRemarkPolicyDescription,
       "tnSASRemarkPolicyType": tnSASRemarkPolicyType,
       "tnSASRemarkPolicyLastChanged": tnSASRemarkPolicyLastChanged,
       "tnSASRemarkPolicyFCTable": tnSASRemarkPolicyFCTable,
       "tnSASRemarkPolicyFCEntry": tnSASRemarkPolicyFCEntry,
       "tnSASRemarkPolicyFCName": tnSASRemarkPolicyFCName,
       "tnSASRemarkPolicyDot1PInProfile": tnSASRemarkPolicyDot1PInProfile,
       "tnSASRemarkPolicyDot1POutProfile": tnSASRemarkPolicyDot1POutProfile,
       "tnSASRemarkPolicyDSCPInProfile": tnSASRemarkPolicyDSCPInProfile,
       "tnSASRemarkPolicyDSCPOutProfile": tnSASRemarkPolicyDSCPOutProfile,
       "tnSASRemarkPolicyLspExpInProfile": tnSASRemarkPolicyLspExpInProfile,
       "tnSASRemarkPolicyLspExpOutProfile": tnSASRemarkPolicyLspExpOutProfile,
       "tnSASRemarkPolicyDot1PLspExpInProfile": tnSASRemarkPolicyDot1PLspExpInProfile,
       "tnSASRemarkPolicyDot1PLspExpOutProfile": tnSASRemarkPolicyDot1PLspExpOutProfile}
)
