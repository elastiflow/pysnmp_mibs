# SNMP MIB module (TN-SAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-SAP-MIB.mib
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(TFilterID,) = mibBuilder.importSymbols(
    "TN-FILTER-MIB",
    "TFilterID")

(BridgeId,
 L2ptProtocols,
 MstiInstanceIdOrZero,
 MvplsPruneState,
 ServObjName,
 ServType,
 StpExceptionCondition,
 StpPortRole,
 StpProtocol,
 TStpPortState,
 TlsBpduTranslation,
 TlsLimitMacMove,
 TlsLimitMacMoveLevel,
 VpnId,
 tnCustId,
 tnServNotifications,
 tnServObjs,
 tnSvcId,
 tnSvcVpnId,
 tnTstpTraps) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "BridgeId",
    "L2ptProtocols",
    "MstiInstanceIdOrZero",
    "MvplsPruneState",
    "ServObjName",
    "ServType",
    "StpExceptionCondition",
    "StpPortRole",
    "StpProtocol",
    "TStpPortState",
    "TlsBpduTranslation",
    "TlsLimitMacMove",
    "TlsLimitMacMoveLevel",
    "VpnId",
    "tnCustId",
    "tnServNotifications",
    "tnServObjs",
    "tnSvcId",
    "tnSvcVpnId",
    "tnTstpTraps")

(ServObjDesc,
 ServiceAdminStatus,
 TCpmProtPolicyID,
 TEgrHsmdaPerPacketOffsetOvr,
 TIngHsmdaPerPacketOffsetOvr,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TPortSchedulerPIR,
 TSapEgressPolicyID,
 TSapIngressPolicyID,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "ServObjDesc",
    "ServiceAdminStatus",
    "TCpmProtPolicyID",
    "TEgrHsmdaPerPacketOffsetOvr",
    "TIngHsmdaPerPacketOffsetOvr",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TPortSchedulerPIR",
    "TSapEgressPolicyID",
    "TSapIngressPolicyID",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId")

(tnSRMIBModules,) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnSvcSapMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 55)
)
if mibBuilder.loadTexts:
    tnSvcSapMIBModule.setRevisions(
        ("1912-12-05 00:00",
         "1912-09-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1907-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSapObjs_ObjectIdentity = ObjectIdentity
tnSapObjs = _TnSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3)
)
_TnSapBaseInfoTable_Object = MibTable
tnSapBaseInfoTable = _TnSapBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    tnSapBaseInfoTable.setStatus("current")
_TnSapBaseInfoEntry_Object = MibTableRow
tnSapBaseInfoEntry = _TnSapBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1)
)
tnSapBaseInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnSapBaseInfoEntry.setStatus("current")
_TnSapPortId_Type = TmnxPortID
_TnSapPortId_Object = MibTableColumn
tnSapPortId = _TnSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 1),
    _TnSapPortId_Type()
)
tnSapPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapPortId.setStatus("current")
_TnSapEncapValue_Type = TmnxEncapVal
_TnSapEncapValue_Object = MibTableColumn
tnSapEncapValue = _TnSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 2),
    _TnSapEncapValue_Type()
)
tnSapEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapEncapValue.setStatus("current")
_TnSapRowStatus_Type = RowStatus
_TnSapRowStatus_Object = MibTableColumn
tnSapRowStatus = _TnSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 3),
    _TnSapRowStatus_Type()
)
tnSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapRowStatus.setStatus("current")
_TnSapType_Type = ServType
_TnSapType_Object = MibTableColumn
tnSapType = _TnSapType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 4),
    _TnSapType_Type()
)
tnSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapType.setStatus("current")


class _TnSapDescription_Type(ServObjDesc):
    """Custom type tnSapDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_TnSapDescription_Type.__name__ = "ServObjDesc"
_TnSapDescription_Object = MibTableColumn
tnSapDescription = _TnSapDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 5),
    _TnSapDescription_Type()
)
tnSapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapDescription.setStatus("current")


class _TnSapAdminStatus_Type(ServiceAdminStatus):
    """Custom type tnSapAdminStatus based on ServiceAdminStatus"""
    defaultValue = 1


_TnSapAdminStatus_Type.__name__ = "ServiceAdminStatus"
_TnSapAdminStatus_Object = MibTableColumn
tnSapAdminStatus = _TnSapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 6),
    _TnSapAdminStatus_Type()
)
tnSapAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapAdminStatus.setStatus("current")


class _TnSapOperStatus_Type(Integer32):
    """Custom type tnSapOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("ingressQosMismatch", 3),
          ("egressQosMismatch", 4),
          ("portMtuTooSmall", 5),
          ("svcAdminDown", 6),
          ("iesIfAdminDown", 7))
    )


_TnSapOperStatus_Type.__name__ = "Integer32"
_TnSapOperStatus_Object = MibTableColumn
tnSapOperStatus = _TnSapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 7),
    _TnSapOperStatus_Type()
)
tnSapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapOperStatus.setStatus("current")


class _TnSapIngressQosPolicyId_Type(TSapIngressPolicyID):
    """Custom type tnSapIngressQosPolicyId based on TSapIngressPolicyID"""
    defaultValue = 1


_TnSapIngressQosPolicyId_Type.__name__ = "TSapIngressPolicyID"
_TnSapIngressQosPolicyId_Object = MibTableColumn
tnSapIngressQosPolicyId = _TnSapIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 8),
    _TnSapIngressQosPolicyId_Type()
)
tnSapIngressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressQosPolicyId.setStatus("current")


class _TnSapIngressMacFilterId_Type(TFilterID):
    """Custom type tnSapIngressMacFilterId based on TFilterID"""
    defaultValue = 0


_TnSapIngressMacFilterId_Type.__name__ = "TFilterID"
_TnSapIngressMacFilterId_Object = MibTableColumn
tnSapIngressMacFilterId = _TnSapIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 9),
    _TnSapIngressMacFilterId_Type()
)
tnSapIngressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMacFilterId.setStatus("current")


class _TnSapIngressIpFilterId_Type(TFilterID):
    """Custom type tnSapIngressIpFilterId based on TFilterID"""
    defaultValue = 0


_TnSapIngressIpFilterId_Type.__name__ = "TFilterID"
_TnSapIngressIpFilterId_Object = MibTableColumn
tnSapIngressIpFilterId = _TnSapIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 10),
    _TnSapIngressIpFilterId_Type()
)
tnSapIngressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIpFilterId.setStatus("current")


class _TnSapEgressQosPolicyId_Type(TSapEgressPolicyID):
    """Custom type tnSapEgressQosPolicyId based on TSapEgressPolicyID"""
    defaultValue = 1


_TnSapEgressQosPolicyId_Type.__name__ = "TSapEgressPolicyID"
_TnSapEgressQosPolicyId_Object = MibTableColumn
tnSapEgressQosPolicyId = _TnSapEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 11),
    _TnSapEgressQosPolicyId_Type()
)
tnSapEgressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressQosPolicyId.setStatus("current")


class _TnSapEgressMacFilterId_Type(TFilterID):
    """Custom type tnSapEgressMacFilterId based on TFilterID"""
    defaultValue = 0


_TnSapEgressMacFilterId_Type.__name__ = "TFilterID"
_TnSapEgressMacFilterId_Object = MibTableColumn
tnSapEgressMacFilterId = _TnSapEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 12),
    _TnSapEgressMacFilterId_Type()
)
tnSapEgressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressMacFilterId.setStatus("current")


class _TnSapEgressIpFilterId_Type(TFilterID):
    """Custom type tnSapEgressIpFilterId based on TFilterID"""
    defaultValue = 0


_TnSapEgressIpFilterId_Type.__name__ = "TFilterID"
_TnSapEgressIpFilterId_Object = MibTableColumn
tnSapEgressIpFilterId = _TnSapEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 13),
    _TnSapEgressIpFilterId_Type()
)
tnSapEgressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressIpFilterId.setStatus("current")


class _TnSapMirrorStatus_Type(Integer32):
    """Custom type tnSapMirrorStatus based on Integer32"""
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
        *(("ingress", 1),
          ("egress", 2),
          ("ingressAndEgress", 3),
          ("disabled", 4))
    )


_TnSapMirrorStatus_Type.__name__ = "Integer32"
_TnSapMirrorStatus_Object = MibTableColumn
tnSapMirrorStatus = _TnSapMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 14),
    _TnSapMirrorStatus_Type()
)
tnSapMirrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMirrorStatus.setStatus("current")
_TnSapIesIfIndex_Type = InterfaceIndexOrZero
_TnSapIesIfIndex_Object = MibTableColumn
tnSapIesIfIndex = _TnSapIesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 15),
    _TnSapIesIfIndex_Type()
)
tnSapIesIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIesIfIndex.setStatus("current")
_TnSapLastMgmtChange_Type = TimeStamp
_TnSapLastMgmtChange_Object = MibTableColumn
tnSapLastMgmtChange = _TnSapLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 16),
    _TnSapLastMgmtChange_Type()
)
tnSapLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapLastMgmtChange.setStatus("current")


class _TnSapCollectAcctStats_Type(TruthValue):
    """Custom type tnSapCollectAcctStats based on TruthValue"""
    defaultValue = 2


_TnSapCollectAcctStats_Type.__name__ = "TruthValue"
_TnSapCollectAcctStats_Object = MibTableColumn
tnSapCollectAcctStats = _TnSapCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 17),
    _TnSapCollectAcctStats_Type()
)
tnSapCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapCollectAcctStats.setStatus("current")


class _TnSapAccountingPolicyId_Type(Unsigned32):
    """Custom type tnSapAccountingPolicyId based on Unsigned32"""
    defaultValue = 0


_TnSapAccountingPolicyId_Type.__name__ = "Unsigned32"
_TnSapAccountingPolicyId_Object = MibTableColumn
tnSapAccountingPolicyId = _TnSapAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 18),
    _TnSapAccountingPolicyId_Type()
)
tnSapAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapAccountingPolicyId.setStatus("current")
_TnSapVpnId_Type = VpnId
_TnSapVpnId_Object = MibTableColumn
tnSapVpnId = _TnSapVpnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 19),
    _TnSapVpnId_Type()
)
tnSapVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapVpnId.setStatus("current")
_TnSapCustId_Type = TmnxCustId
_TnSapCustId_Object = MibTableColumn
tnSapCustId = _TnSapCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 20),
    _TnSapCustId_Type()
)
tnSapCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapCustId.setStatus("current")


class _TnSapCustMultSvcSite_Type(ServObjName):
    """Custom type tnSapCustMultSvcSite based on ServObjName"""
    defaultValue = OctetString("")


_TnSapCustMultSvcSite_Type.__name__ = "ServObjName"
_TnSapCustMultSvcSite_Object = MibTableColumn
tnSapCustMultSvcSite = _TnSapCustMultSvcSite_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 21),
    _TnSapCustMultSvcSite_Type()
)
tnSapCustMultSvcSite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapCustMultSvcSite.setStatus("current")


class _TnSapIngressQosSchedulerPolicy_Type(ServObjName):
    """Custom type tnSapIngressQosSchedulerPolicy based on ServObjName"""
    defaultValue = OctetString("")


_TnSapIngressQosSchedulerPolicy_Type.__name__ = "ServObjName"
_TnSapIngressQosSchedulerPolicy_Object = MibTableColumn
tnSapIngressQosSchedulerPolicy = _TnSapIngressQosSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 22),
    _TnSapIngressQosSchedulerPolicy_Type()
)
tnSapIngressQosSchedulerPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressQosSchedulerPolicy.setStatus("current")


class _TnSapEgressQosSchedulerPolicy_Type(ServObjName):
    """Custom type tnSapEgressQosSchedulerPolicy based on ServObjName"""
    defaultValue = OctetString("")


_TnSapEgressQosSchedulerPolicy_Type.__name__ = "ServObjName"
_TnSapEgressQosSchedulerPolicy_Object = MibTableColumn
tnSapEgressQosSchedulerPolicy = _TnSapEgressQosSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 23),
    _TnSapEgressQosSchedulerPolicy_Type()
)
tnSapEgressQosSchedulerPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressQosSchedulerPolicy.setStatus("current")


class _TnSapSplitHorizonGrp_Type(ServObjName):
    """Custom type tnSapSplitHorizonGrp based on ServObjName"""
    defaultValue = OctetString("")


_TnSapSplitHorizonGrp_Type.__name__ = "ServObjName"
_TnSapSplitHorizonGrp_Object = MibTableColumn
tnSapSplitHorizonGrp = _TnSapSplitHorizonGrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 24),
    _TnSapSplitHorizonGrp_Type()
)
tnSapSplitHorizonGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapSplitHorizonGrp.setStatus("current")


class _TnSapIngressSharedQueuePolicy_Type(ServObjName):
    """Custom type tnSapIngressSharedQueuePolicy based on ServObjName"""
    defaultValue = OctetString("")


_TnSapIngressSharedQueuePolicy_Type.__name__ = "ServObjName"
_TnSapIngressSharedQueuePolicy_Object = MibTableColumn
tnSapIngressSharedQueuePolicy = _TnSapIngressSharedQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 25),
    _TnSapIngressSharedQueuePolicy_Type()
)
tnSapIngressSharedQueuePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressSharedQueuePolicy.setStatus("current")


class _TnSapIngressMatchQinQDot1PBits_Type(Integer32):
    """Custom type tnSapIngressMatchQinQDot1PBits based on Integer32"""
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
        *(("default", 1),
          ("top", 2),
          ("bottom", 3))
    )


_TnSapIngressMatchQinQDot1PBits_Type.__name__ = "Integer32"
_TnSapIngressMatchQinQDot1PBits_Object = MibTableColumn
tnSapIngressMatchQinQDot1PBits = _TnSapIngressMatchQinQDot1PBits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 26),
    _TnSapIngressMatchQinQDot1PBits_Type()
)
tnSapIngressMatchQinQDot1PBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressMatchQinQDot1PBits.setStatus("current")


class _TnSapOperFlags_Type(Bits):
    """Custom type tnSapOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sapAdminDown", 0),
          ("svcAdminDown", 1),
          ("iesIfAdminDown", 2),
          ("portOperDown", 3),
          ("portMtuTooSmall", 4),
          ("l2OperDown", 5),
          ("ingressQosMismatch", 6),
          ("egressQosMismatch", 7),
          ("relearnLimitExceeded", 8),
          ("recProtSrcMac", 9),
          ("subIfAdminDown", 10),
          ("sapIpipeNoCeIpAddr", 11),
          ("sapTodResourceUnavail", 12),
          ("sapTodMssResourceUnavail", 13),
          ("sapParamMismatch", 14),
          ("sapCemNoEcidOrMacAddr", 15),
          ("sapStandbyForMcRing", 16),
          ("sapSvcMtuTooSmall", 17),
          ("ingressNamedPoolMismatch", 18),
          ("egressNamedPoolMismatch", 19),
          ("ipMirrorNoMacAddr", 20),
          ("sapEpipeNoRingNode", 21),
          ("mcStandby", 22),
          ("mhStandby", 23),
          ("oamDownMepFault", 24),
          ("oamUpMepFault", 25),
          ("ethTunTagMisconfig", 26),
          ("ingressPolicerMismatch", 27),
          ("egressPolicerMismatch", 28),
          ("sapTlsNoRingNode", 29),
          ("ethRingPathBlocked", 30),
          ("oamTunnelMepFault", 31),
          ("operGrpDown", 32))
    )

_TnSapOperFlags_Type.__name__ = "Bits"
_TnSapOperFlags_Object = MibTableColumn
tnSapOperFlags = _TnSapOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 27),
    _TnSapOperFlags_Type()
)
tnSapOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapOperFlags.setStatus("current")
_TnSapLastStatusChange_Type = TimeStamp
_TnSapLastStatusChange_Object = MibTableColumn
tnSapLastStatusChange = _TnSapLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 28),
    _TnSapLastStatusChange_Type()
)
tnSapLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapLastStatusChange.setStatus("current")


class _TnSapAntiSpoofing_Type(Integer32):
    """Custom type tnSapAntiSpoofing based on Integer32"""
    defaultValue = 0

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
        *(("disabled", 0),
          ("sourceIpAddr", 1),
          ("sourceMacAddr", 2),
          ("sourceIpAndMacAddr", 3),
          ("nextHopIpAndMacAddr", 4))
    )


_TnSapAntiSpoofing_Type.__name__ = "Integer32"
_TnSapAntiSpoofing_Object = MibTableColumn
tnSapAntiSpoofing = _TnSapAntiSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 29),
    _TnSapAntiSpoofing_Type()
)
tnSapAntiSpoofing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapAntiSpoofing.setStatus("current")


class _TnSapIngressIpv6FilterId_Type(TFilterID):
    """Custom type tnSapIngressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_TnSapIngressIpv6FilterId_Type.__name__ = "TFilterID"
_TnSapIngressIpv6FilterId_Object = MibTableColumn
tnSapIngressIpv6FilterId = _TnSapIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 30),
    _TnSapIngressIpv6FilterId_Type()
)
tnSapIngressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressIpv6FilterId.setStatus("current")


class _TnSapEgressIpv6FilterId_Type(TFilterID):
    """Custom type tnSapEgressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_TnSapEgressIpv6FilterId_Type.__name__ = "TFilterID"
_TnSapEgressIpv6FilterId_Object = MibTableColumn
tnSapEgressIpv6FilterId = _TnSapEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 31),
    _TnSapEgressIpv6FilterId_Type()
)
tnSapEgressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressIpv6FilterId.setStatus("current")


class _TnSapTodSuite_Type(TNamedItemOrEmpty):
    """Custom type tnSapTodSuite based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnSapTodSuite_Type.__name__ = "TNamedItemOrEmpty"
_TnSapTodSuite_Object = MibTableColumn
tnSapTodSuite = _TnSapTodSuite_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 32),
    _TnSapTodSuite_Type()
)
tnSapTodSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapTodSuite.setStatus("current")


class _TnSapIngUseMultipointShared_Type(TruthValue):
    """Custom type tnSapIngUseMultipointShared based on TruthValue"""
    defaultValue = 2


_TnSapIngUseMultipointShared_Type.__name__ = "TruthValue"
_TnSapIngUseMultipointShared_Object = MibTableColumn
tnSapIngUseMultipointShared = _TnSapIngUseMultipointShared_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 33),
    _TnSapIngUseMultipointShared_Type()
)
tnSapIngUseMultipointShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngUseMultipointShared.setStatus("current")


class _TnSapEgressQinQMarkTopOnly_Type(TruthValue):
    """Custom type tnSapEgressQinQMarkTopOnly based on TruthValue"""
    defaultValue = 2


_TnSapEgressQinQMarkTopOnly_Type.__name__ = "TruthValue"
_TnSapEgressQinQMarkTopOnly_Object = MibTableColumn
tnSapEgressQinQMarkTopOnly = _TnSapEgressQinQMarkTopOnly_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 34),
    _TnSapEgressQinQMarkTopOnly_Type()
)
tnSapEgressQinQMarkTopOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressQinQMarkTopOnly.setStatus("current")


class _TnSapEgressAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type tnSapEgressAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_TnSapEgressAggRateLimit_Type.__name__ = "TPortSchedulerPIR"
_TnSapEgressAggRateLimit_Object = MibTableColumn
tnSapEgressAggRateLimit = _TnSapEgressAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 35),
    _TnSapEgressAggRateLimit_Type()
)
tnSapEgressAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tnSapEgressAggRateLimit.setUnits("kbps")


class _TnSapEndPoint_Type(ServObjName):
    """Custom type tnSapEndPoint based on ServObjName"""
    defaultValue = OctetString("")


_TnSapEndPoint_Type.__name__ = "ServObjName"
_TnSapEndPoint_Object = MibTableColumn
tnSapEndPoint = _TnSapEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 36),
    _TnSapEndPoint_Type()
)
tnSapEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEndPoint.setStatus("current")


class _TnSapIngressVlanTranslation_Type(Integer32):
    """Custom type tnSapIngressVlanTranslation based on Integer32"""
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
        *(("none", 1),
          ("vlanId", 2),
          ("copyOuter", 3))
    )


_TnSapIngressVlanTranslation_Type.__name__ = "Integer32"
_TnSapIngressVlanTranslation_Object = MibTableColumn
tnSapIngressVlanTranslation = _TnSapIngressVlanTranslation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 37),
    _TnSapIngressVlanTranslation_Type()
)
tnSapIngressVlanTranslation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressVlanTranslation.setStatus("current")


class _TnSapIngressVlanTranslationId_Type(Integer32):
    """Custom type tnSapIngressVlanTranslationId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4094),
    )


_TnSapIngressVlanTranslationId_Type.__name__ = "Integer32"
_TnSapIngressVlanTranslationId_Object = MibTableColumn
tnSapIngressVlanTranslationId = _TnSapIngressVlanTranslationId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 38),
    _TnSapIngressVlanTranslationId_Type()
)
tnSapIngressVlanTranslationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressVlanTranslationId.setStatus("current")


class _TnSapSubType_Type(Integer32):
    """Custom type tnSapSubType based on Integer32"""
    defaultValue = 0

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
        *(("regular", 0),
          ("capture", 1),
          ("managed", 2),
          ("video", 3))
    )


_TnSapSubType_Type.__name__ = "Integer32"
_TnSapSubType_Object = MibTableColumn
tnSapSubType = _TnSapSubType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 39),
    _TnSapSubType_Type()
)
tnSapSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapSubType.setStatus("current")
_TnSapCpmProtPolicyId_Type = TCpmProtPolicyID
_TnSapCpmProtPolicyId_Object = MibTableColumn
tnSapCpmProtPolicyId = _TnSapCpmProtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 40),
    _TnSapCpmProtPolicyId_Type()
)
tnSapCpmProtPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapCpmProtPolicyId.setStatus("current")


class _TnSapCpmProtMonitorMac_Type(TruthValue):
    """Custom type tnSapCpmProtMonitorMac based on TruthValue"""
    defaultValue = 2


_TnSapCpmProtMonitorMac_Type.__name__ = "TruthValue"
_TnSapCpmProtMonitorMac_Object = MibTableColumn
tnSapCpmProtMonitorMac = _TnSapCpmProtMonitorMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 41),
    _TnSapCpmProtMonitorMac_Type()
)
tnSapCpmProtMonitorMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapCpmProtMonitorMac.setStatus("current")


class _TnSapEgressFrameBasedAccounting_Type(TruthValue):
    """Custom type tnSapEgressFrameBasedAccounting based on TruthValue"""
    defaultValue = 2


_TnSapEgressFrameBasedAccounting_Type.__name__ = "TruthValue"
_TnSapEgressFrameBasedAccounting_Object = MibTableColumn
tnSapEgressFrameBasedAccounting = _TnSapEgressFrameBasedAccounting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 42),
    _TnSapEgressFrameBasedAccounting_Type()
)
tnSapEgressFrameBasedAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressFrameBasedAccounting.setStatus("current")


class _TnSapIngressAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type tnSapIngressAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_TnSapIngressAggRateLimit_Type.__name__ = "TPortSchedulerPIR"
_TnSapIngressAggRateLimit_Object = MibTableColumn
tnSapIngressAggRateLimit = _TnSapIngressAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 43),
    _TnSapIngressAggRateLimit_Type()
)
tnSapIngressAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIngressAggRateLimit.setUnits("kbps")


class _TnSapEgressHsmdaShaperOverride_Type(TNamedItemOrEmpty):
    """Custom type tnSapEgressHsmdaShaperOverride based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TnSapEgressHsmdaShaperOverride_Type.__name__ = "TNamedItemOrEmpty"
_TnSapEgressHsmdaShaperOverride_Object = MibTableColumn
tnSapEgressHsmdaShaperOverride = _TnSapEgressHsmdaShaperOverride_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 44),
    _TnSapEgressHsmdaShaperOverride_Type()
)
tnSapEgressHsmdaShaperOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressHsmdaShaperOverride.setStatus("current")


class _TnSapIngressHsmdaPacketOffOvr_Type(TIngHsmdaPerPacketOffsetOvr):
    """Custom type tnSapIngressHsmdaPacketOffOvr based on TIngHsmdaPerPacketOffsetOvr"""
    defaultValue = -128


_TnSapIngressHsmdaPacketOffOvr_Type.__name__ = "TIngHsmdaPerPacketOffsetOvr"
_TnSapIngressHsmdaPacketOffOvr_Object = MibTableColumn
tnSapIngressHsmdaPacketOffOvr = _TnSapIngressHsmdaPacketOffOvr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 45),
    _TnSapIngressHsmdaPacketOffOvr_Type()
)
tnSapIngressHsmdaPacketOffOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIngressHsmdaPacketOffOvr.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIngressHsmdaPacketOffOvr.setUnits("bytes")


class _TnSapEgressHsmdaPacketOffOverride_Type(TEgrHsmdaPerPacketOffsetOvr):
    """Custom type tnSapEgressHsmdaPacketOffOverride based on TEgrHsmdaPerPacketOffsetOvr"""
    defaultValue = -128


_TnSapEgressHsmdaPacketOffOverride_Type.__name__ = "TEgrHsmdaPerPacketOffsetOvr"
_TnSapEgressHsmdaPacketOffOverride_Object = MibTableColumn
tnSapEgressHsmdaPacketOffOverride = _TnSapEgressHsmdaPacketOffOverride_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 46),
    _TnSapEgressHsmdaPacketOffOverride_Type()
)
tnSapEgressHsmdaPacketOffOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEgressHsmdaPacketOffOverride.setStatus("current")
if mibBuilder.loadTexts:
    tnSapEgressHsmdaPacketOffOverride.setUnits("bytes")


class _TnSapCallingStationId_Type(DisplayString):
    """Custom type tnSapCallingStationId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSapCallingStationId_Type.__name__ = "DisplayString"
_TnSapCallingStationId_Object = MibTableColumn
tnSapCallingStationId = _TnSapCallingStationId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 47),
    _TnSapCallingStationId_Type()
)
tnSapCallingStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapCallingStationId.setStatus("current")


class _TnSapIsaAaApplicationProfile_Type(ServObjName):
    """Custom type tnSapIsaAaApplicationProfile based on ServObjName"""
    defaultValue = OctetString("")


_TnSapIsaAaApplicationProfile_Type.__name__ = "ServObjName"
_TnSapIsaAaApplicationProfile_Object = MibTableColumn
tnSapIsaAaApplicationProfile = _TnSapIsaAaApplicationProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 48),
    _TnSapIsaAaApplicationProfile_Type()
)
tnSapIsaAaApplicationProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIsaAaApplicationProfile.setStatus("current")


class _TnSapEthRingIndex_Type(Unsigned32):
    """Custom type tnSapEthRingIndex based on Unsigned32"""
    defaultValue = 0


_TnSapEthRingIndex_Type.__name__ = "Unsigned32"
_TnSapEthRingIndex_Object = MibTableColumn
tnSapEthRingIndex = _TnSapEthRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 2, 1, 52),
    _TnSapEthRingIndex_Type()
)
tnSapEthRingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEthRingIndex.setStatus("current")
_TnSapTlsInfoTable_Object = MibTable
tnSapTlsInfoTable = _TnSapTlsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3)
)
if mibBuilder.loadTexts:
    tnSapTlsInfoTable.setStatus("current")
_TnSapTlsInfoEntry_Object = MibTableRow
tnSapTlsInfoEntry = _TnSapTlsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1)
)
tnSapTlsInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnSapTlsInfoEntry.setStatus("current")


class _TnSapTlsStpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tnSapTlsStpAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 1


_TnSapTlsStpAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TnSapTlsStpAdminStatus_Object = MibTableColumn
tnSapTlsStpAdminStatus = _TnSapTlsStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 1),
    _TnSapTlsStpAdminStatus_Type()
)
tnSapTlsStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpAdminStatus.setStatus("current")


class _TnSapTlsStpPriority_Type(Integer32):
    """Custom type tnSapTlsStpPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSapTlsStpPriority_Type.__name__ = "Integer32"
_TnSapTlsStpPriority_Object = MibTableColumn
tnSapTlsStpPriority = _TnSapTlsStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 2),
    _TnSapTlsStpPriority_Type()
)
tnSapTlsStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpPriority.setStatus("current")


class _TnSapTlsStpPortNum_Type(Integer32):
    """Custom type tnSapTlsStpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TnSapTlsStpPortNum_Type.__name__ = "Integer32"
_TnSapTlsStpPortNum_Object = MibTableColumn
tnSapTlsStpPortNum = _TnSapTlsStpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 3),
    _TnSapTlsStpPortNum_Type()
)
tnSapTlsStpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpPortNum.setStatus("current")


class _TnSapTlsStpPathCost_Type(Integer32):
    """Custom type tnSapTlsStpPathCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_TnSapTlsStpPathCost_Type.__name__ = "Integer32"
_TnSapTlsStpPathCost_Object = MibTableColumn
tnSapTlsStpPathCost = _TnSapTlsStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 4),
    _TnSapTlsStpPathCost_Type()
)
tnSapTlsStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpPathCost.setStatus("current")


class _TnSapTlsStpRapidStart_Type(TmnxEnabledDisabled):
    """Custom type tnSapTlsStpRapidStart based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSapTlsStpRapidStart_Type.__name__ = "TmnxEnabledDisabled"
_TnSapTlsStpRapidStart_Object = MibTableColumn
tnSapTlsStpRapidStart = _TnSapTlsStpRapidStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 5),
    _TnSapTlsStpRapidStart_Type()
)
tnSapTlsStpRapidStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpRapidStart.setStatus("current")


class _TnSapTlsStpBpduEncap_Type(Integer32):
    """Custom type tnSapTlsStpBpduEncap based on Integer32"""
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
        *(("dynamic", 1),
          ("dot1d", 2),
          ("pvst", 3))
    )


_TnSapTlsStpBpduEncap_Type.__name__ = "Integer32"
_TnSapTlsStpBpduEncap_Object = MibTableColumn
tnSapTlsStpBpduEncap = _TnSapTlsStpBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 6),
    _TnSapTlsStpBpduEncap_Type()
)
tnSapTlsStpBpduEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpBpduEncap.setStatus("current")
_TnSapTlsStpPortState_Type = TStpPortState
_TnSapTlsStpPortState_Object = MibTableColumn
tnSapTlsStpPortState = _TnSapTlsStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 7),
    _TnSapTlsStpPortState_Type()
)
tnSapTlsStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpPortState.setStatus("current")
_TnSapTlsStpDesignatedBridge_Type = BridgeId
_TnSapTlsStpDesignatedBridge_Object = MibTableColumn
tnSapTlsStpDesignatedBridge = _TnSapTlsStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 8),
    _TnSapTlsStpDesignatedBridge_Type()
)
tnSapTlsStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpDesignatedBridge.setStatus("current")
_TnSapTlsStpDesignatedPort_Type = Integer32
_TnSapTlsStpDesignatedPort_Object = MibTableColumn
tnSapTlsStpDesignatedPort = _TnSapTlsStpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 9),
    _TnSapTlsStpDesignatedPort_Type()
)
tnSapTlsStpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpDesignatedPort.setStatus("current")
_TnSapTlsStpForwardTransitions_Type = Gauge32
_TnSapTlsStpForwardTransitions_Object = MibTableColumn
tnSapTlsStpForwardTransitions = _TnSapTlsStpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 10),
    _TnSapTlsStpForwardTransitions_Type()
)
tnSapTlsStpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpForwardTransitions.setStatus("current")
_TnSapTlsStpInConfigBpdus_Type = Gauge32
_TnSapTlsStpInConfigBpdus_Object = MibTableColumn
tnSapTlsStpInConfigBpdus = _TnSapTlsStpInConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 11),
    _TnSapTlsStpInConfigBpdus_Type()
)
tnSapTlsStpInConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpInConfigBpdus.setStatus("current")
_TnSapTlsStpInTcnBpdus_Type = Gauge32
_TnSapTlsStpInTcnBpdus_Object = MibTableColumn
tnSapTlsStpInTcnBpdus = _TnSapTlsStpInTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 12),
    _TnSapTlsStpInTcnBpdus_Type()
)
tnSapTlsStpInTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpInTcnBpdus.setStatus("current")
_TnSapTlsStpInBadBpdus_Type = Gauge32
_TnSapTlsStpInBadBpdus_Object = MibTableColumn
tnSapTlsStpInBadBpdus = _TnSapTlsStpInBadBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 13),
    _TnSapTlsStpInBadBpdus_Type()
)
tnSapTlsStpInBadBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpInBadBpdus.setStatus("current")
_TnSapTlsStpOutConfigBpdus_Type = Gauge32
_TnSapTlsStpOutConfigBpdus_Object = MibTableColumn
tnSapTlsStpOutConfigBpdus = _TnSapTlsStpOutConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 14),
    _TnSapTlsStpOutConfigBpdus_Type()
)
tnSapTlsStpOutConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpOutConfigBpdus.setStatus("current")
_TnSapTlsStpOutTcnBpdus_Type = Gauge32
_TnSapTlsStpOutTcnBpdus_Object = MibTableColumn
tnSapTlsStpOutTcnBpdus = _TnSapTlsStpOutTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 15),
    _TnSapTlsStpOutTcnBpdus_Type()
)
tnSapTlsStpOutTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpOutTcnBpdus.setStatus("current")


class _TnSapTlsStpOperBpduEncap_Type(Integer32):
    """Custom type tnSapTlsStpOperBpduEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("dot1d", 2),
          ("pvst", 3))
    )


_TnSapTlsStpOperBpduEncap_Type.__name__ = "Integer32"
_TnSapTlsStpOperBpduEncap_Object = MibTableColumn
tnSapTlsStpOperBpduEncap = _TnSapTlsStpOperBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 16),
    _TnSapTlsStpOperBpduEncap_Type()
)
tnSapTlsStpOperBpduEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpOperBpduEncap.setStatus("current")
_TnSapTlsVpnId_Type = VpnId
_TnSapTlsVpnId_Object = MibTableColumn
tnSapTlsVpnId = _TnSapTlsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 17),
    _TnSapTlsVpnId_Type()
)
tnSapTlsVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsVpnId.setStatus("current")
_TnSapTlsCustId_Type = TmnxCustId
_TnSapTlsCustId_Object = MibTableColumn
tnSapTlsCustId = _TnSapTlsCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 18),
    _TnSapTlsCustId_Type()
)
tnSapTlsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsCustId.setStatus("current")


class _TnSapTlsMacAddressLimit_Type(Integer32):
    """Custom type tnSapTlsMacAddressLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511999),
    )


_TnSapTlsMacAddressLimit_Type.__name__ = "Integer32"
_TnSapTlsMacAddressLimit_Object = MibTableColumn
tnSapTlsMacAddressLimit = _TnSapTlsMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 19),
    _TnSapTlsMacAddressLimit_Type()
)
tnSapTlsMacAddressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMacAddressLimit.setStatus("current")
_TnSapTlsNumMacAddresses_Type = Integer32
_TnSapTlsNumMacAddresses_Object = MibTableColumn
tnSapTlsNumMacAddresses = _TnSapTlsNumMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 20),
    _TnSapTlsNumMacAddresses_Type()
)
tnSapTlsNumMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsNumMacAddresses.setStatus("current")
_TnSapTlsNumStaticMacAddresses_Type = Integer32
_TnSapTlsNumStaticMacAddresses_Object = MibTableColumn
tnSapTlsNumStaticMacAddresses = _TnSapTlsNumStaticMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 21),
    _TnSapTlsNumStaticMacAddresses_Type()
)
tnSapTlsNumStaticMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsNumStaticMacAddresses.setStatus("current")


class _TnSapTlsMacLearning_Type(TmnxEnabledDisabled):
    """Custom type tnSapTlsMacLearning based on TmnxEnabledDisabled"""
    defaultValue = 1


_TnSapTlsMacLearning_Type.__name__ = "TmnxEnabledDisabled"
_TnSapTlsMacLearning_Object = MibTableColumn
tnSapTlsMacLearning = _TnSapTlsMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 22),
    _TnSapTlsMacLearning_Type()
)
tnSapTlsMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMacLearning.setStatus("current")


class _TnSapTlsMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type tnSapTlsMacAgeing based on TmnxEnabledDisabled"""
    defaultValue = 1


_TnSapTlsMacAgeing_Type.__name__ = "TmnxEnabledDisabled"
_TnSapTlsMacAgeing_Object = MibTableColumn
tnSapTlsMacAgeing = _TnSapTlsMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 23),
    _TnSapTlsMacAgeing_Type()
)
tnSapTlsMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMacAgeing.setStatus("current")
_TnSapTlsStpOperEdge_Type = TruthValue
_TnSapTlsStpOperEdge_Object = MibTableColumn
tnSapTlsStpOperEdge = _TnSapTlsStpOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 24),
    _TnSapTlsStpOperEdge_Type()
)
tnSapTlsStpOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpOperEdge.setStatus("current")


class _TnSapTlsStpAdminPointToPoint_Type(Integer32):
    """Custom type tnSapTlsStpAdminPointToPoint based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1))
    )


_TnSapTlsStpAdminPointToPoint_Type.__name__ = "Integer32"
_TnSapTlsStpAdminPointToPoint_Object = MibTableColumn
tnSapTlsStpAdminPointToPoint = _TnSapTlsStpAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 25),
    _TnSapTlsStpAdminPointToPoint_Type()
)
tnSapTlsStpAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpAdminPointToPoint.setStatus("current")
_TnSapTlsStpPortRole_Type = StpPortRole
_TnSapTlsStpPortRole_Object = MibTableColumn
tnSapTlsStpPortRole = _TnSapTlsStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 26),
    _TnSapTlsStpPortRole_Type()
)
tnSapTlsStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpPortRole.setStatus("current")


class _TnSapTlsStpAutoEdge_Type(TmnxEnabledDisabled):
    """Custom type tnSapTlsStpAutoEdge based on TmnxEnabledDisabled"""
    defaultValue = 1


_TnSapTlsStpAutoEdge_Type.__name__ = "TmnxEnabledDisabled"
_TnSapTlsStpAutoEdge_Object = MibTableColumn
tnSapTlsStpAutoEdge = _TnSapTlsStpAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 27),
    _TnSapTlsStpAutoEdge_Type()
)
tnSapTlsStpAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpAutoEdge.setStatus("current")
_TnSapTlsStpOperProtocol_Type = StpProtocol
_TnSapTlsStpOperProtocol_Object = MibTableColumn
tnSapTlsStpOperProtocol = _TnSapTlsStpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 28),
    _TnSapTlsStpOperProtocol_Type()
)
tnSapTlsStpOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpOperProtocol.setStatus("current")
_TnSapTlsStpInRstBpdus_Type = Gauge32
_TnSapTlsStpInRstBpdus_Object = MibTableColumn
tnSapTlsStpInRstBpdus = _TnSapTlsStpInRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 29),
    _TnSapTlsStpInRstBpdus_Type()
)
tnSapTlsStpInRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpInRstBpdus.setStatus("current")
_TnSapTlsStpOutRstBpdus_Type = Gauge32
_TnSapTlsStpOutRstBpdus_Object = MibTableColumn
tnSapTlsStpOutRstBpdus = _TnSapTlsStpOutRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 30),
    _TnSapTlsStpOutRstBpdus_Type()
)
tnSapTlsStpOutRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpOutRstBpdus.setStatus("current")


class _TnSapTlsLimitMacMove_Type(TlsLimitMacMove):
    """Custom type tnSapTlsLimitMacMove based on TlsLimitMacMove"""
    defaultValue = 1


_TnSapTlsLimitMacMove_Type.__name__ = "TlsLimitMacMove"
_TnSapTlsLimitMacMove_Object = MibTableColumn
tnSapTlsLimitMacMove = _TnSapTlsLimitMacMove_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 31),
    _TnSapTlsLimitMacMove_Type()
)
tnSapTlsLimitMacMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsLimitMacMove.setStatus("current")
_TnSapTlsMacPinning_Type = TmnxEnabledDisabled
_TnSapTlsMacPinning_Object = MibTableColumn
tnSapTlsMacPinning = _TnSapTlsMacPinning_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 33),
    _TnSapTlsMacPinning_Type()
)
tnSapTlsMacPinning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMacPinning.setStatus("current")


class _TnSapTlsDiscardUnknownSource_Type(TmnxEnabledDisabled):
    """Custom type tnSapTlsDiscardUnknownSource based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSapTlsDiscardUnknownSource_Type.__name__ = "TmnxEnabledDisabled"
_TnSapTlsDiscardUnknownSource_Object = MibTableColumn
tnSapTlsDiscardUnknownSource = _TnSapTlsDiscardUnknownSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 34),
    _TnSapTlsDiscardUnknownSource_Type()
)
tnSapTlsDiscardUnknownSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsDiscardUnknownSource.setStatus("current")
_TnSapTlsMvplsPruneState_Type = MvplsPruneState
_TnSapTlsMvplsPruneState_Object = MibTableColumn
tnSapTlsMvplsPruneState = _TnSapTlsMvplsPruneState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 35),
    _TnSapTlsMvplsPruneState_Type()
)
tnSapTlsMvplsPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMvplsPruneState.setStatus("current")
_TnSapTlsMvplsMgmtService_Type = TmnxServId
_TnSapTlsMvplsMgmtService_Object = MibTableColumn
tnSapTlsMvplsMgmtService = _TnSapTlsMvplsMgmtService_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 36),
    _TnSapTlsMvplsMgmtService_Type()
)
tnSapTlsMvplsMgmtService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMvplsMgmtService.setStatus("current")
_TnSapTlsMvplsMgmtPortId_Type = TmnxPortID
_TnSapTlsMvplsMgmtPortId_Object = MibTableColumn
tnSapTlsMvplsMgmtPortId = _TnSapTlsMvplsMgmtPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 37),
    _TnSapTlsMvplsMgmtPortId_Type()
)
tnSapTlsMvplsMgmtPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMvplsMgmtPortId.setStatus("current")
_TnSapTlsMvplsMgmtEncapValue_Type = TmnxEncapVal
_TnSapTlsMvplsMgmtEncapValue_Object = MibTableColumn
tnSapTlsMvplsMgmtEncapValue = _TnSapTlsMvplsMgmtEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 38),
    _TnSapTlsMvplsMgmtEncapValue_Type()
)
tnSapTlsMvplsMgmtEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMvplsMgmtEncapValue.setStatus("current")


class _TnSapTlsArpReplyAgent_Type(Integer32):
    """Custom type tnSapTlsArpReplyAgent based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledWithSubscrIdent", 3))
    )


_TnSapTlsArpReplyAgent_Type.__name__ = "Integer32"
_TnSapTlsArpReplyAgent_Object = MibTableColumn
tnSapTlsArpReplyAgent = _TnSapTlsArpReplyAgent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 39),
    _TnSapTlsArpReplyAgent_Type()
)
tnSapTlsArpReplyAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsArpReplyAgent.setStatus("current")
_TnSapTlsStpException_Type = StpExceptionCondition
_TnSapTlsStpException_Object = MibTableColumn
tnSapTlsStpException = _TnSapTlsStpException_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 40),
    _TnSapTlsStpException_Type()
)
tnSapTlsStpException.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpException.setStatus("current")


class _TnSapTlsAuthenticationPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tnSapTlsAuthenticationPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TnSapTlsAuthenticationPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TnSapTlsAuthenticationPolicy_Object = MibTableColumn
tnSapTlsAuthenticationPolicy = _TnSapTlsAuthenticationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 41),
    _TnSapTlsAuthenticationPolicy_Type()
)
tnSapTlsAuthenticationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsAuthenticationPolicy.setStatus("current")


class _TnSapTlsL2ptTermination_Type(TmnxEnabledDisabled):
    """Custom type tnSapTlsL2ptTermination based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSapTlsL2ptTermination_Type.__name__ = "TmnxEnabledDisabled"
_TnSapTlsL2ptTermination_Object = MibTableColumn
tnSapTlsL2ptTermination = _TnSapTlsL2ptTermination_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 42),
    _TnSapTlsL2ptTermination_Type()
)
tnSapTlsL2ptTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsL2ptTermination.setStatus("current")


class _TnSapTlsBpduTranslation_Type(TlsBpduTranslation):
    """Custom type tnSapTlsBpduTranslation based on TlsBpduTranslation"""
    defaultValue = 2


_TnSapTlsBpduTranslation_Type.__name__ = "TlsBpduTranslation"
_TnSapTlsBpduTranslation_Object = MibTableColumn
tnSapTlsBpduTranslation = _TnSapTlsBpduTranslation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 43),
    _TnSapTlsBpduTranslation_Type()
)
tnSapTlsBpduTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsBpduTranslation.setStatus("current")


class _TnSapTlsStpRootGuard_Type(TruthValue):
    """Custom type tnSapTlsStpRootGuard based on TruthValue"""
    defaultValue = 2


_TnSapTlsStpRootGuard_Type.__name__ = "TruthValue"
_TnSapTlsStpRootGuard_Object = MibTableColumn
tnSapTlsStpRootGuard = _TnSapTlsStpRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 44),
    _TnSapTlsStpRootGuard_Type()
)
tnSapTlsStpRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsStpRootGuard.setStatus("current")
_TnSapTlsStpInsideRegion_Type = TruthValue
_TnSapTlsStpInsideRegion_Object = MibTableColumn
tnSapTlsStpInsideRegion = _TnSapTlsStpInsideRegion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 45),
    _TnSapTlsStpInsideRegion_Type()
)
tnSapTlsStpInsideRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpInsideRegion.setStatus("current")


class _TnSapTlsEgressMcastGroup_Type(TNamedItemOrEmpty):
    """Custom type tnSapTlsEgressMcastGroup based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TnSapTlsEgressMcastGroup_Type.__name__ = "TNamedItemOrEmpty"
_TnSapTlsEgressMcastGroup_Object = MibTableColumn
tnSapTlsEgressMcastGroup = _TnSapTlsEgressMcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 46),
    _TnSapTlsEgressMcastGroup_Type()
)
tnSapTlsEgressMcastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsEgressMcastGroup.setStatus("current")
_TnSapTlsStpInMstBpdus_Type = Gauge32
_TnSapTlsStpInMstBpdus_Object = MibTableColumn
tnSapTlsStpInMstBpdus = _TnSapTlsStpInMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 47),
    _TnSapTlsStpInMstBpdus_Type()
)
tnSapTlsStpInMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpInMstBpdus.setStatus("current")
_TnSapTlsStpOutMstBpdus_Type = Gauge32
_TnSapTlsStpOutMstBpdus_Object = MibTableColumn
tnSapTlsStpOutMstBpdus = _TnSapTlsStpOutMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 48),
    _TnSapTlsStpOutMstBpdus_Type()
)
tnSapTlsStpOutMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpOutMstBpdus.setStatus("current")


class _TnSapTlsRestProtSrcMac_Type(TruthValue):
    """Custom type tnSapTlsRestProtSrcMac based on TruthValue"""
    defaultValue = 2


_TnSapTlsRestProtSrcMac_Type.__name__ = "TruthValue"
_TnSapTlsRestProtSrcMac_Object = MibTableColumn
tnSapTlsRestProtSrcMac = _TnSapTlsRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 49),
    _TnSapTlsRestProtSrcMac_Type()
)
tnSapTlsRestProtSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsRestProtSrcMac.setStatus("current")


class _TnSapTlsRestUnprotDstMac_Type(TruthValue):
    """Custom type tnSapTlsRestUnprotDstMac based on TruthValue"""
    defaultValue = 2


_TnSapTlsRestUnprotDstMac_Type.__name__ = "TruthValue"
_TnSapTlsRestUnprotDstMac_Object = MibTableColumn
tnSapTlsRestUnprotDstMac = _TnSapTlsRestUnprotDstMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 50),
    _TnSapTlsRestUnprotDstMac_Type()
)
tnSapTlsRestUnprotDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsRestUnprotDstMac.setStatus("current")
_TnSapTlsStpRxdDesigBridge_Type = BridgeId
_TnSapTlsStpRxdDesigBridge_Object = MibTableColumn
tnSapTlsStpRxdDesigBridge = _TnSapTlsStpRxdDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 51),
    _TnSapTlsStpRxdDesigBridge_Type()
)
tnSapTlsStpRxdDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpRxdDesigBridge.setStatus("current")
_TnSapTlsStpRootGuardViolation_Type = TruthValue
_TnSapTlsStpRootGuardViolation_Object = MibTableColumn
tnSapTlsStpRootGuardViolation = _TnSapTlsStpRootGuardViolation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 52),
    _TnSapTlsStpRootGuardViolation_Type()
)
tnSapTlsStpRootGuardViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsStpRootGuardViolation.setStatus("current")


class _TnSapTlsShcvAction_Type(Integer32):
    """Custom type tnSapTlsShcvAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("remove", 2))
    )


_TnSapTlsShcvAction_Type.__name__ = "Integer32"
_TnSapTlsShcvAction_Object = MibTableColumn
tnSapTlsShcvAction = _TnSapTlsShcvAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 53),
    _TnSapTlsShcvAction_Type()
)
tnSapTlsShcvAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsShcvAction.setStatus("current")
_TnSapTlsShcvSrcIp_Type = IpAddress
_TnSapTlsShcvSrcIp_Object = MibTableColumn
tnSapTlsShcvSrcIp = _TnSapTlsShcvSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 54),
    _TnSapTlsShcvSrcIp_Type()
)
tnSapTlsShcvSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsShcvSrcIp.setStatus("current")
_TnSapTlsShcvSrcMac_Type = MacAddress
_TnSapTlsShcvSrcMac_Object = MibTableColumn
tnSapTlsShcvSrcMac = _TnSapTlsShcvSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 55),
    _TnSapTlsShcvSrcMac_Type()
)
tnSapTlsShcvSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsShcvSrcMac.setStatus("current")


class _TnSapTlsShcvInterval_Type(Unsigned32):
    """Custom type tnSapTlsShcvInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_TnSapTlsShcvInterval_Type.__name__ = "Unsigned32"
_TnSapTlsShcvInterval_Object = MibTableColumn
tnSapTlsShcvInterval = _TnSapTlsShcvInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 56),
    _TnSapTlsShcvInterval_Type()
)
tnSapTlsShcvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsShcvInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnSapTlsShcvInterval.setUnits("minutes")
_TnSapTlsMvplsMgmtMsti_Type = MstiInstanceIdOrZero
_TnSapTlsMvplsMgmtMsti_Object = MibTableColumn
tnSapTlsMvplsMgmtMsti = _TnSapTlsMvplsMgmtMsti_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 57),
    _TnSapTlsMvplsMgmtMsti_Type()
)
tnSapTlsMvplsMgmtMsti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMvplsMgmtMsti.setStatus("current")
_TnSapTlsMacMoveNextUpTime_Type = Unsigned32
_TnSapTlsMacMoveNextUpTime_Object = MibTableColumn
tnSapTlsMacMoveNextUpTime = _TnSapTlsMacMoveNextUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 58),
    _TnSapTlsMacMoveNextUpTime_Type()
)
tnSapTlsMacMoveNextUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMacMoveNextUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapTlsMacMoveNextUpTime.setUnits("seconds")
_TnSapTlsMacMoveRateExcdLeft_Type = Unsigned32
_TnSapTlsMacMoveRateExcdLeft_Object = MibTableColumn
tnSapTlsMacMoveRateExcdLeft = _TnSapTlsMacMoveRateExcdLeft_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 59),
    _TnSapTlsMacMoveRateExcdLeft_Type()
)
tnSapTlsMacMoveRateExcdLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMacMoveRateExcdLeft.setStatus("current")


class _TnSapTlsRestProtSrcMacAction_Type(Integer32):
    """Custom type tnSapTlsRestProtSrcMacAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("alarm-only", 2))
    )


_TnSapTlsRestProtSrcMacAction_Type.__name__ = "Integer32"
_TnSapTlsRestProtSrcMacAction_Object = MibTableColumn
tnSapTlsRestProtSrcMacAction = _TnSapTlsRestProtSrcMacAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 60),
    _TnSapTlsRestProtSrcMacAction_Type()
)
tnSapTlsRestProtSrcMacAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsRestProtSrcMacAction.setStatus("current")


class _TnSapTlsL2ptForceBoundary_Type(TruthValue):
    """Custom type tnSapTlsL2ptForceBoundary based on TruthValue"""
    defaultValue = 2


_TnSapTlsL2ptForceBoundary_Type.__name__ = "TruthValue"
_TnSapTlsL2ptForceBoundary_Object = MibTableColumn
tnSapTlsL2ptForceBoundary = _TnSapTlsL2ptForceBoundary_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 61),
    _TnSapTlsL2ptForceBoundary_Type()
)
tnSapTlsL2ptForceBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsL2ptForceBoundary.setStatus("current")


class _TnSapTlsLimitMacMoveLevel_Type(TlsLimitMacMoveLevel):
    """Custom type tnSapTlsLimitMacMoveLevel based on TlsLimitMacMoveLevel"""
    defaultValue = 3


_TnSapTlsLimitMacMoveLevel_Type.__name__ = "TlsLimitMacMoveLevel"
_TnSapTlsLimitMacMoveLevel_Object = MibTableColumn
tnSapTlsLimitMacMoveLevel = _TnSapTlsLimitMacMoveLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 62),
    _TnSapTlsLimitMacMoveLevel_Type()
)
tnSapTlsLimitMacMoveLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsLimitMacMoveLevel.setStatus("current")


class _TnSapTlsBpduTransOper_Type(Integer32):
    """Custom type tnSapTlsBpduTransOper based on Integer32"""
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
        *(("undefined", 1),
          ("disabled", 2),
          ("pvst", 3),
          ("stp", 4),
          ("pvst-rw", 5))
    )


_TnSapTlsBpduTransOper_Type.__name__ = "Integer32"
_TnSapTlsBpduTransOper_Object = MibTableColumn
tnSapTlsBpduTransOper = _TnSapTlsBpduTransOper_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 63),
    _TnSapTlsBpduTransOper_Type()
)
tnSapTlsBpduTransOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsBpduTransOper.setStatus("current")


class _TnSapTlsDefMtnSapPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tnSapTlsDefMtnSapPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TnSapTlsDefMtnSapPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TnSapTlsDefMtnSapPolicy_Object = MibTableColumn
tnSapTlsDefMtnSapPolicy = _TnSapTlsDefMtnSapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 64),
    _TnSapTlsDefMtnSapPolicy_Type()
)
tnSapTlsDefMtnSapPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsDefMtnSapPolicy.setStatus("current")


class _TnSapTlsL2ptProtocols_Type(L2ptProtocols):
    """Custom type tnSapTlsL2ptProtocols based on L2ptProtocols"""
    defaultBinValue = "1"


_TnSapTlsL2ptProtocols_Type.__name__ = "L2ptProtocols"
_TnSapTlsL2ptProtocols_Object = MibTableColumn
tnSapTlsL2ptProtocols = _TnSapTlsL2ptProtocols_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 65),
    _TnSapTlsL2ptProtocols_Type()
)
tnSapTlsL2ptProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsL2ptProtocols.setStatus("current")


class _TnSapTlsL2ptForceProtocols_Type(L2ptProtocols):
    """Custom type tnSapTlsL2ptForceProtocols based on L2ptProtocols"""
    defaultBinValue = "1"


_TnSapTlsL2ptForceProtocols_Type.__name__ = "L2ptProtocols"
_TnSapTlsL2ptForceProtocols_Object = MibTableColumn
tnSapTlsL2ptForceProtocols = _TnSapTlsL2ptForceProtocols_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 66),
    _TnSapTlsL2ptForceProtocols_Type()
)
tnSapTlsL2ptForceProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsL2ptForceProtocols.setStatus("current")


class _TnSapTlsPppoeMtnSapTrigger_Type(TruthValue):
    """Custom type tnSapTlsPppoeMtnSapTrigger based on TruthValue"""
    defaultValue = 2


_TnSapTlsPppoeMtnSapTrigger_Type.__name__ = "TruthValue"
_TnSapTlsPppoeMtnSapTrigger_Object = MibTableColumn
tnSapTlsPppoeMtnSapTrigger = _TnSapTlsPppoeMtnSapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 67),
    _TnSapTlsPppoeMtnSapTrigger_Type()
)
tnSapTlsPppoeMtnSapTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsPppoeMtnSapTrigger.setStatus("current")


class _TnSapTlsDhcpMtnSapTrigger_Type(TruthValue):
    """Custom type tnSapTlsDhcpMtnSapTrigger based on TruthValue"""
    defaultValue = 2


_TnSapTlsDhcpMtnSapTrigger_Type.__name__ = "TruthValue"
_TnSapTlsDhcpMtnSapTrigger_Object = MibTableColumn
tnSapTlsDhcpMtnSapTrigger = _TnSapTlsDhcpMtnSapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 68),
    _TnSapTlsDhcpMtnSapTrigger_Type()
)
tnSapTlsDhcpMtnSapTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsDhcpMtnSapTrigger.setStatus("current")


class _TnSapTlsMrpJoinTime_Type(Unsigned32):
    """Custom type tnSapTlsMrpJoinTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnSapTlsMrpJoinTime_Type.__name__ = "Unsigned32"
_TnSapTlsMrpJoinTime_Object = MibTableColumn
tnSapTlsMrpJoinTime = _TnSapTlsMrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 69),
    _TnSapTlsMrpJoinTime_Type()
)
tnSapTlsMrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMrpJoinTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapTlsMrpJoinTime.setUnits("deci-seconds")


class _TnSapTlsMrpLeaveTime_Type(Unsigned32):
    """Custom type tnSapTlsMrpLeaveTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_TnSapTlsMrpLeaveTime_Type.__name__ = "Unsigned32"
_TnSapTlsMrpLeaveTime_Object = MibTableColumn
tnSapTlsMrpLeaveTime = _TnSapTlsMrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 70),
    _TnSapTlsMrpLeaveTime_Type()
)
tnSapTlsMrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMrpLeaveTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapTlsMrpLeaveTime.setUnits("deci-seconds")


class _TnSapTlsMrpLeaveAllTime_Type(Unsigned32):
    """Custom type tnSapTlsMrpLeaveAllTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_TnSapTlsMrpLeaveAllTime_Type.__name__ = "Unsigned32"
_TnSapTlsMrpLeaveAllTime_Object = MibTableColumn
tnSapTlsMrpLeaveAllTime = _TnSapTlsMrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 71),
    _TnSapTlsMrpLeaveAllTime_Type()
)
tnSapTlsMrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMrpLeaveAllTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapTlsMrpLeaveAllTime.setUnits("deci-seconds")


class _TnSapTlsMrpPeriodicTime_Type(Unsigned32):
    """Custom type tnSapTlsMrpPeriodicTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_TnSapTlsMrpPeriodicTime_Type.__name__ = "Unsigned32"
_TnSapTlsMrpPeriodicTime_Object = MibTableColumn
tnSapTlsMrpPeriodicTime = _TnSapTlsMrpPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 72),
    _TnSapTlsMrpPeriodicTime_Type()
)
tnSapTlsMrpPeriodicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMrpPeriodicTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapTlsMrpPeriodicTime.setUnits("deci-seconds")


class _TnSapTlsMrpPeriodicEnabled_Type(TruthValue):
    """Custom type tnSapTlsMrpPeriodicEnabled based on TruthValue"""
    defaultValue = 2


_TnSapTlsMrpPeriodicEnabled_Type.__name__ = "TruthValue"
_TnSapTlsMrpPeriodicEnabled_Object = MibTableColumn
tnSapTlsMrpPeriodicEnabled = _TnSapTlsMrpPeriodicEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 73),
    _TnSapTlsMrpPeriodicEnabled_Type()
)
tnSapTlsMrpPeriodicEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsMrpPeriodicEnabled.setStatus("current")


class _TnSapTlsPppoePolicy_Type(TNamedItemOrEmpty):
    """Custom type tnSapTlsPppoePolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TnSapTlsPppoePolicy_Type.__name__ = "TNamedItemOrEmpty"
_TnSapTlsPppoePolicy_Object = MibTableColumn
tnSapTlsPppoePolicy = _TnSapTlsPppoePolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 74),
    _TnSapTlsPppoePolicy_Type()
)
tnSapTlsPppoePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsPppoePolicy.setStatus("current")


class _TnSapTlsArpMsapTrigger_Type(TruthValue):
    """Custom type tnSapTlsArpMsapTrigger based on TruthValue"""
    defaultValue = 2


_TnSapTlsArpMsapTrigger_Type.__name__ = "TruthValue"
_TnSapTlsArpMsapTrigger_Object = MibTableColumn
tnSapTlsArpMsapTrigger = _TnSapTlsArpMsapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 75),
    _TnSapTlsArpMsapTrigger_Type()
)
tnSapTlsArpMsapTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsArpMsapTrigger.setStatus("current")
_TnSapTlsInTcBitBpdus_Type = Counter32
_TnSapTlsInTcBitBpdus_Object = MibTableColumn
tnSapTlsInTcBitBpdus = _TnSapTlsInTcBitBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 76),
    _TnSapTlsInTcBitBpdus_Type()
)
tnSapTlsInTcBitBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsInTcBitBpdus.setStatus("current")
_TnSapTlsOutTcBitBpdus_Type = Counter32
_TnSapTlsOutTcBitBpdus_Object = MibTableColumn
tnSapTlsOutTcBitBpdus = _TnSapTlsOutTcBitBpdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 77),
    _TnSapTlsOutTcBitBpdus_Type()
)
tnSapTlsOutTcBitBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsOutTcBitBpdus.setStatus("current")


class _TnSapTlsShcvRetryTimeout_Type(Unsigned32):
    """Custom type tnSapTlsShcvRetryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_TnSapTlsShcvRetryTimeout_Type.__name__ = "Unsigned32"
_TnSapTlsShcvRetryTimeout_Object = MibTableColumn
tnSapTlsShcvRetryTimeout = _TnSapTlsShcvRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 81),
    _TnSapTlsShcvRetryTimeout_Type()
)
tnSapTlsShcvRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsShcvRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tnSapTlsShcvRetryTimeout.setUnits("seconds")


class _TnSapTlsShcvRetryCount_Type(Unsigned32):
    """Custom type tnSapTlsShcvRetryCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 29),
    )


_TnSapTlsShcvRetryCount_Type.__name__ = "Unsigned32"
_TnSapTlsShcvRetryCount_Object = MibTableColumn
tnSapTlsShcvRetryCount = _TnSapTlsShcvRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 3, 1, 82),
    _TnSapTlsShcvRetryCount_Type()
)
tnSapTlsShcvRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapTlsShcvRetryCount.setStatus("current")
_TnSapScalar1_Type = Unsigned32
_TnSapScalar1_Object = MibScalar
tnSapScalar1 = _TnSapScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 5),
    _TnSapScalar1_Type()
)
tnSapScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapScalar1.setStatus("current")
_TnSapBaseStatsTable_Object = MibTable
tnSapBaseStatsTable = _TnSapBaseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6)
)
if mibBuilder.loadTexts:
    tnSapBaseStatsTable.setStatus("current")
_TnSapBaseStatsEntry_Object = MibTableRow
tnSapBaseStatsEntry = _TnSapBaseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1)
)
tnSapBaseStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnSapBaseStatsEntry.setStatus("current")
_TnSapBaseStatsIngressPchipDroppedPackets_Type = Counter64
_TnSapBaseStatsIngressPchipDroppedPackets_Object = MibTableColumn
tnSapBaseStatsIngressPchipDroppedPackets = _TnSapBaseStatsIngressPchipDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 1),
    _TnSapBaseStatsIngressPchipDroppedPackets_Type()
)
tnSapBaseStatsIngressPchipDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressPchipDroppedPackets.setStatus("current")
_TnSapBaseStatsIngressPchipDroppedOctets_Type = Counter64
_TnSapBaseStatsIngressPchipDroppedOctets_Object = MibTableColumn
tnSapBaseStatsIngressPchipDroppedOctets = _TnSapBaseStatsIngressPchipDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 2),
    _TnSapBaseStatsIngressPchipDroppedOctets_Type()
)
tnSapBaseStatsIngressPchipDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressPchipDroppedOctets.setStatus("current")
_TnSapBaseStatsIngressPchipOfferedHiPrioPackets_Type = Counter64
_TnSapBaseStatsIngressPchipOfferedHiPrioPackets_Object = MibTableColumn
tnSapBaseStatsIngressPchipOfferedHiPrioPackets = _TnSapBaseStatsIngressPchipOfferedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 3),
    _TnSapBaseStatsIngressPchipOfferedHiPrioPackets_Type()
)
tnSapBaseStatsIngressPchipOfferedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressPchipOfferedHiPrioPackets.setStatus("current")
_TnSapBaseStatsIngressPchipOfferedHiPrioOctets_Type = Counter64
_TnSapBaseStatsIngressPchipOfferedHiPrioOctets_Object = MibTableColumn
tnSapBaseStatsIngressPchipOfferedHiPrioOctets = _TnSapBaseStatsIngressPchipOfferedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 4),
    _TnSapBaseStatsIngressPchipOfferedHiPrioOctets_Type()
)
tnSapBaseStatsIngressPchipOfferedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressPchipOfferedHiPrioOctets.setStatus("current")
_TnSapBaseStatsIngressPchipOfferedLoPrioPackets_Type = Counter64
_TnSapBaseStatsIngressPchipOfferedLoPrioPackets_Object = MibTableColumn
tnSapBaseStatsIngressPchipOfferedLoPrioPackets = _TnSapBaseStatsIngressPchipOfferedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 5),
    _TnSapBaseStatsIngressPchipOfferedLoPrioPackets_Type()
)
tnSapBaseStatsIngressPchipOfferedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressPchipOfferedLoPrioPackets.setStatus("current")
_TnSapBaseStatsIngressPchipOfferedLoPrioOctets_Type = Counter64
_TnSapBaseStatsIngressPchipOfferedLoPrioOctets_Object = MibTableColumn
tnSapBaseStatsIngressPchipOfferedLoPrioOctets = _TnSapBaseStatsIngressPchipOfferedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 6),
    _TnSapBaseStatsIngressPchipOfferedLoPrioOctets_Type()
)
tnSapBaseStatsIngressPchipOfferedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressPchipOfferedLoPrioOctets.setStatus("current")
_TnSapBaseStatsIngressQchipDroppedHiPrioPackets_Type = Counter64
_TnSapBaseStatsIngressQchipDroppedHiPrioPackets_Object = MibTableColumn
tnSapBaseStatsIngressQchipDroppedHiPrioPackets = _TnSapBaseStatsIngressQchipDroppedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 7),
    _TnSapBaseStatsIngressQchipDroppedHiPrioPackets_Type()
)
tnSapBaseStatsIngressQchipDroppedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressQchipDroppedHiPrioPackets.setStatus("current")
_TnSapBaseStatsIngressQchipDroppedHiPrioOctets_Type = Counter64
_TnSapBaseStatsIngressQchipDroppedHiPrioOctets_Object = MibTableColumn
tnSapBaseStatsIngressQchipDroppedHiPrioOctets = _TnSapBaseStatsIngressQchipDroppedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 8),
    _TnSapBaseStatsIngressQchipDroppedHiPrioOctets_Type()
)
tnSapBaseStatsIngressQchipDroppedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressQchipDroppedHiPrioOctets.setStatus("current")
_TnSapBaseStatsIngressQchipDroppedLoPrioPackets_Type = Counter64
_TnSapBaseStatsIngressQchipDroppedLoPrioPackets_Object = MibTableColumn
tnSapBaseStatsIngressQchipDroppedLoPrioPackets = _TnSapBaseStatsIngressQchipDroppedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 9),
    _TnSapBaseStatsIngressQchipDroppedLoPrioPackets_Type()
)
tnSapBaseStatsIngressQchipDroppedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressQchipDroppedLoPrioPackets.setStatus("current")
_TnSapBaseStatsIngressQchipDroppedLoPrioOctets_Type = Counter64
_TnSapBaseStatsIngressQchipDroppedLoPrioOctets_Object = MibTableColumn
tnSapBaseStatsIngressQchipDroppedLoPrioOctets = _TnSapBaseStatsIngressQchipDroppedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 10),
    _TnSapBaseStatsIngressQchipDroppedLoPrioOctets_Type()
)
tnSapBaseStatsIngressQchipDroppedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressQchipDroppedLoPrioOctets.setStatus("current")
_TnSapBaseStatsIngressQchipForwardedInProfPackets_Type = Counter64
_TnSapBaseStatsIngressQchipForwardedInProfPackets_Object = MibTableColumn
tnSapBaseStatsIngressQchipForwardedInProfPackets = _TnSapBaseStatsIngressQchipForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 11),
    _TnSapBaseStatsIngressQchipForwardedInProfPackets_Type()
)
tnSapBaseStatsIngressQchipForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressQchipForwardedInProfPackets.setStatus("current")
_TnSapBaseStatsIngressQchipForwardedInProfOctets_Type = Counter64
_TnSapBaseStatsIngressQchipForwardedInProfOctets_Object = MibTableColumn
tnSapBaseStatsIngressQchipForwardedInProfOctets = _TnSapBaseStatsIngressQchipForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 12),
    _TnSapBaseStatsIngressQchipForwardedInProfOctets_Type()
)
tnSapBaseStatsIngressQchipForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressQchipForwardedInProfOctets.setStatus("current")
_TnSapBaseStatsIngressQchipForwardedOutProfPackets_Type = Counter64
_TnSapBaseStatsIngressQchipForwardedOutProfPackets_Object = MibTableColumn
tnSapBaseStatsIngressQchipForwardedOutProfPackets = _TnSapBaseStatsIngressQchipForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 13),
    _TnSapBaseStatsIngressQchipForwardedOutProfPackets_Type()
)
tnSapBaseStatsIngressQchipForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressQchipForwardedOutProfPackets.setStatus("current")
_TnSapBaseStatsIngressQchipForwardedOutProfOctets_Type = Counter64
_TnSapBaseStatsIngressQchipForwardedOutProfOctets_Object = MibTableColumn
tnSapBaseStatsIngressQchipForwardedOutProfOctets = _TnSapBaseStatsIngressQchipForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 14),
    _TnSapBaseStatsIngressQchipForwardedOutProfOctets_Type()
)
tnSapBaseStatsIngressQchipForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressQchipForwardedOutProfOctets.setStatus("current")
_TnSapBaseStatsEgressQchipDroppedInProfPackets_Type = Counter64
_TnSapBaseStatsEgressQchipDroppedInProfPackets_Object = MibTableColumn
tnSapBaseStatsEgressQchipDroppedInProfPackets = _TnSapBaseStatsEgressQchipDroppedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 15),
    _TnSapBaseStatsEgressQchipDroppedInProfPackets_Type()
)
tnSapBaseStatsEgressQchipDroppedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressQchipDroppedInProfPackets.setStatus("current")
_TnSapBaseStatsEgressQchipDroppedInProfOctets_Type = Counter64
_TnSapBaseStatsEgressQchipDroppedInProfOctets_Object = MibTableColumn
tnSapBaseStatsEgressQchipDroppedInProfOctets = _TnSapBaseStatsEgressQchipDroppedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 16),
    _TnSapBaseStatsEgressQchipDroppedInProfOctets_Type()
)
tnSapBaseStatsEgressQchipDroppedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressQchipDroppedInProfOctets.setStatus("current")
_TnSapBaseStatsEgressQchipDroppedOutProfPackets_Type = Counter64
_TnSapBaseStatsEgressQchipDroppedOutProfPackets_Object = MibTableColumn
tnSapBaseStatsEgressQchipDroppedOutProfPackets = _TnSapBaseStatsEgressQchipDroppedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 17),
    _TnSapBaseStatsEgressQchipDroppedOutProfPackets_Type()
)
tnSapBaseStatsEgressQchipDroppedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressQchipDroppedOutProfPackets.setStatus("current")
_TnSapBaseStatsEgressQchipDroppedOutProfOctets_Type = Counter64
_TnSapBaseStatsEgressQchipDroppedOutProfOctets_Object = MibTableColumn
tnSapBaseStatsEgressQchipDroppedOutProfOctets = _TnSapBaseStatsEgressQchipDroppedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 18),
    _TnSapBaseStatsEgressQchipDroppedOutProfOctets_Type()
)
tnSapBaseStatsEgressQchipDroppedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressQchipDroppedOutProfOctets.setStatus("current")
_TnSapBaseStatsEgressQchipForwardedInProfPackets_Type = Counter64
_TnSapBaseStatsEgressQchipForwardedInProfPackets_Object = MibTableColumn
tnSapBaseStatsEgressQchipForwardedInProfPackets = _TnSapBaseStatsEgressQchipForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 19),
    _TnSapBaseStatsEgressQchipForwardedInProfPackets_Type()
)
tnSapBaseStatsEgressQchipForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressQchipForwardedInProfPackets.setStatus("current")
_TnSapBaseStatsEgressQchipForwardedInProfOctets_Type = Counter64
_TnSapBaseStatsEgressQchipForwardedInProfOctets_Object = MibTableColumn
tnSapBaseStatsEgressQchipForwardedInProfOctets = _TnSapBaseStatsEgressQchipForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 20),
    _TnSapBaseStatsEgressQchipForwardedInProfOctets_Type()
)
tnSapBaseStatsEgressQchipForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressQchipForwardedInProfOctets.setStatus("current")
_TnSapBaseStatsEgressQchipForwardedOutProfPackets_Type = Counter64
_TnSapBaseStatsEgressQchipForwardedOutProfPackets_Object = MibTableColumn
tnSapBaseStatsEgressQchipForwardedOutProfPackets = _TnSapBaseStatsEgressQchipForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 21),
    _TnSapBaseStatsEgressQchipForwardedOutProfPackets_Type()
)
tnSapBaseStatsEgressQchipForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressQchipForwardedOutProfPackets.setStatus("current")
_TnSapBaseStatsEgressQchipForwardedOutProfOctets_Type = Counter64
_TnSapBaseStatsEgressQchipForwardedOutProfOctets_Object = MibTableColumn
tnSapBaseStatsEgressQchipForwardedOutProfOctets = _TnSapBaseStatsEgressQchipForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 22),
    _TnSapBaseStatsEgressQchipForwardedOutProfOctets_Type()
)
tnSapBaseStatsEgressQchipForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressQchipForwardedOutProfOctets.setStatus("current")
_TnSapBaseStatsCustId_Type = TmnxCustId
_TnSapBaseStatsCustId_Object = MibTableColumn
tnSapBaseStatsCustId = _TnSapBaseStatsCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 23),
    _TnSapBaseStatsCustId_Type()
)
tnSapBaseStatsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsCustId.setStatus("current")
_TnSapBaseStatsIngressPchipOfferedUncoloredPackets_Type = Counter64
_TnSapBaseStatsIngressPchipOfferedUncoloredPackets_Object = MibTableColumn
tnSapBaseStatsIngressPchipOfferedUncoloredPackets = _TnSapBaseStatsIngressPchipOfferedUncoloredPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 24),
    _TnSapBaseStatsIngressPchipOfferedUncoloredPackets_Type()
)
tnSapBaseStatsIngressPchipOfferedUncoloredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressPchipOfferedUncoloredPackets.setStatus("current")
_TnSapBaseStatsIngressPchipOfferedUncoloredOctets_Type = Counter64
_TnSapBaseStatsIngressPchipOfferedUncoloredOctets_Object = MibTableColumn
tnSapBaseStatsIngressPchipOfferedUncoloredOctets = _TnSapBaseStatsIngressPchipOfferedUncoloredOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 25),
    _TnSapBaseStatsIngressPchipOfferedUncoloredOctets_Type()
)
tnSapBaseStatsIngressPchipOfferedUncoloredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressPchipOfferedUncoloredOctets.setStatus("current")
_TnSapBaseStatsAuthenticationPktsDiscarded_Type = Counter32
_TnSapBaseStatsAuthenticationPktsDiscarded_Object = MibTableColumn
tnSapBaseStatsAuthenticationPktsDiscarded = _TnSapBaseStatsAuthenticationPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 26),
    _TnSapBaseStatsAuthenticationPktsDiscarded_Type()
)
tnSapBaseStatsAuthenticationPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsAuthenticationPktsDiscarded.setStatus("current")
_TnSapBaseStatsAuthenticationPktsSuccess_Type = Counter32
_TnSapBaseStatsAuthenticationPktsSuccess_Object = MibTableColumn
tnSapBaseStatsAuthenticationPktsSuccess = _TnSapBaseStatsAuthenticationPktsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 27),
    _TnSapBaseStatsAuthenticationPktsSuccess_Type()
)
tnSapBaseStatsAuthenticationPktsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsAuthenticationPktsSuccess.setStatus("current")
_TnSapBaseStatsLastClearedTime_Type = TimeStamp
_TnSapBaseStatsLastClearedTime_Object = MibTableColumn
tnSapBaseStatsLastClearedTime = _TnSapBaseStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 6, 1, 28),
    _TnSapBaseStatsLastClearedTime_Type()
)
tnSapBaseStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsLastClearedTime.setStatus("current")
_TnSapEthernetInfoTable_Object = MibTable
tnSapEthernetInfoTable = _TnSapEthernetInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 43)
)
if mibBuilder.loadTexts:
    tnSapEthernetInfoTable.setStatus("current")
_TnSapEthernetInfoEntry_Object = MibTableRow
tnSapEthernetInfoEntry = _TnSapEthernetInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 43, 1)
)
tnSapEthernetInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnSapEthernetInfoEntry.setStatus("current")


class _TnSapEthernetLLFAdminStatus_Type(ServiceAdminStatus):
    """Custom type tnSapEthernetLLFAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_TnSapEthernetLLFAdminStatus_Type.__name__ = "ServiceAdminStatus"
_TnSapEthernetLLFAdminStatus_Object = MibTableColumn
tnSapEthernetLLFAdminStatus = _TnSapEthernetLLFAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 43, 1, 1),
    _TnSapEthernetLLFAdminStatus_Type()
)
tnSapEthernetLLFAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEthernetLLFAdminStatus.setStatus("current")


class _TnSapEthernetLLFOperStatus_Type(Integer32):
    """Custom type tnSapEthernetLLFOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("clear", 2))
    )


_TnSapEthernetLLFOperStatus_Type.__name__ = "Integer32"
_TnSapEthernetLLFOperStatus_Object = MibTableColumn
tnSapEthernetLLFOperStatus = _TnSapEthernetLLFOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 43, 1, 2),
    _TnSapEthernetLLFOperStatus_Type()
)
tnSapEthernetLLFOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapEthernetLLFOperStatus.setStatus("current")


class _TnSapEthernetLLFId_Type(Unsigned32):
    """Custom type tnSapEthernetLLFId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TnSapEthernetLLFId_Type.__name__ = "Unsigned32"
_TnSapEthernetLLFId_Object = MibTableColumn
tnSapEthernetLLFId = _TnSapEthernetLLFId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 43, 1, 3),
    _TnSapEthernetLLFId_Type()
)
tnSapEthernetLLFId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapEthernetLLFId.setStatus("current")
_TnSapTlsMrpTable_Object = MibTable
tnSapTlsMrpTable = _TnSapTlsMrpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50)
)
if mibBuilder.loadTexts:
    tnSapTlsMrpTable.setStatus("current")
_TnSapTlsMrpEntry_Object = MibTableRow
tnSapTlsMrpEntry = _TnSapTlsMrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1)
)
if mibBuilder.loadTexts:
    tnSapTlsMrpEntry.setStatus("current")
_TnSapTlsMrpRxPdus_Type = Counter32
_TnSapTlsMrpRxPdus_Object = MibTableColumn
tnSapTlsMrpRxPdus = _TnSapTlsMrpRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 1),
    _TnSapTlsMrpRxPdus_Type()
)
tnSapTlsMrpRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpRxPdus.setStatus("current")
_TnSapTlsMrpDroppedPdus_Type = Counter32
_TnSapTlsMrpDroppedPdus_Object = MibTableColumn
tnSapTlsMrpDroppedPdus = _TnSapTlsMrpDroppedPdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 2),
    _TnSapTlsMrpDroppedPdus_Type()
)
tnSapTlsMrpDroppedPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpDroppedPdus.setStatus("current")
_TnSapTlsMrpTxPdus_Type = Counter32
_TnSapTlsMrpTxPdus_Object = MibTableColumn
tnSapTlsMrpTxPdus = _TnSapTlsMrpTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 3),
    _TnSapTlsMrpTxPdus_Type()
)
tnSapTlsMrpTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpTxPdus.setStatus("current")
_TnSapTlsMrpRxNewEvent_Type = Counter32
_TnSapTlsMrpRxNewEvent_Object = MibTableColumn
tnSapTlsMrpRxNewEvent = _TnSapTlsMrpRxNewEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 4),
    _TnSapTlsMrpRxNewEvent_Type()
)
tnSapTlsMrpRxNewEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpRxNewEvent.setStatus("current")
_TnSapTlsMrpRxJoinInEvent_Type = Counter32
_TnSapTlsMrpRxJoinInEvent_Object = MibTableColumn
tnSapTlsMrpRxJoinInEvent = _TnSapTlsMrpRxJoinInEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 5),
    _TnSapTlsMrpRxJoinInEvent_Type()
)
tnSapTlsMrpRxJoinInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpRxJoinInEvent.setStatus("current")
_TnSapTlsMrpRxInEvent_Type = Counter32
_TnSapTlsMrpRxInEvent_Object = MibTableColumn
tnSapTlsMrpRxInEvent = _TnSapTlsMrpRxInEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 6),
    _TnSapTlsMrpRxInEvent_Type()
)
tnSapTlsMrpRxInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpRxInEvent.setStatus("current")
_TnSapTlsMrpRxJoinEmptyEvent_Type = Counter32
_TnSapTlsMrpRxJoinEmptyEvent_Object = MibTableColumn
tnSapTlsMrpRxJoinEmptyEvent = _TnSapTlsMrpRxJoinEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 7),
    _TnSapTlsMrpRxJoinEmptyEvent_Type()
)
tnSapTlsMrpRxJoinEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpRxJoinEmptyEvent.setStatus("current")
_TnSapTlsMrpRxEmptyEvent_Type = Counter32
_TnSapTlsMrpRxEmptyEvent_Object = MibTableColumn
tnSapTlsMrpRxEmptyEvent = _TnSapTlsMrpRxEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 8),
    _TnSapTlsMrpRxEmptyEvent_Type()
)
tnSapTlsMrpRxEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpRxEmptyEvent.setStatus("current")
_TnSapTlsMrpRxLeaveEvent_Type = Counter32
_TnSapTlsMrpRxLeaveEvent_Object = MibTableColumn
tnSapTlsMrpRxLeaveEvent = _TnSapTlsMrpRxLeaveEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 9),
    _TnSapTlsMrpRxLeaveEvent_Type()
)
tnSapTlsMrpRxLeaveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpRxLeaveEvent.setStatus("current")
_TnSapTlsMrpTxNewEvent_Type = Counter32
_TnSapTlsMrpTxNewEvent_Object = MibTableColumn
tnSapTlsMrpTxNewEvent = _TnSapTlsMrpTxNewEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 10),
    _TnSapTlsMrpTxNewEvent_Type()
)
tnSapTlsMrpTxNewEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpTxNewEvent.setStatus("current")
_TnSapTlsMrpTxJoinInEvent_Type = Counter32
_TnSapTlsMrpTxJoinInEvent_Object = MibTableColumn
tnSapTlsMrpTxJoinInEvent = _TnSapTlsMrpTxJoinInEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 11),
    _TnSapTlsMrpTxJoinInEvent_Type()
)
tnSapTlsMrpTxJoinInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpTxJoinInEvent.setStatus("current")
_TnSapTlsMrpTxInEvent_Type = Counter32
_TnSapTlsMrpTxInEvent_Object = MibTableColumn
tnSapTlsMrpTxInEvent = _TnSapTlsMrpTxInEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 12),
    _TnSapTlsMrpTxInEvent_Type()
)
tnSapTlsMrpTxInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpTxInEvent.setStatus("current")
_TnSapTlsMrpTxJoinEmptyEvent_Type = Counter32
_TnSapTlsMrpTxJoinEmptyEvent_Object = MibTableColumn
tnSapTlsMrpTxJoinEmptyEvent = _TnSapTlsMrpTxJoinEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 13),
    _TnSapTlsMrpTxJoinEmptyEvent_Type()
)
tnSapTlsMrpTxJoinEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpTxJoinEmptyEvent.setStatus("current")
_TnSapTlsMrpTxEmptyEvent_Type = Counter32
_TnSapTlsMrpTxEmptyEvent_Object = MibTableColumn
tnSapTlsMrpTxEmptyEvent = _TnSapTlsMrpTxEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 14),
    _TnSapTlsMrpTxEmptyEvent_Type()
)
tnSapTlsMrpTxEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpTxEmptyEvent.setStatus("current")
_TnSapTlsMrpTxLeaveEvent_Type = Counter32
_TnSapTlsMrpTxLeaveEvent_Object = MibTableColumn
tnSapTlsMrpTxLeaveEvent = _TnSapTlsMrpTxLeaveEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 3, 50, 1, 15),
    _TnSapTlsMrpTxLeaveEvent_Type()
)
tnSapTlsMrpTxLeaveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapTlsMrpTxLeaveEvent.setStatus("current")
_TnSapTrapsPrefix_ObjectIdentity = ObjectIdentity
tnSapTrapsPrefix = _TnSapTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 3)
)
_TnSapTraps_ObjectIdentity = ObjectIdentity
tnSapTraps = _TnSapTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 3, 0)
)
tnSapTlsInfoEntry.registerAugmentions(
    ("TN-SAP-MIB",
     "tnSapTlsMrpEntry")
)
tnSapTlsMrpEntry.setIndexNames(*tnSapTlsInfoEntry.getIndexNames())

# Managed Objects groups


# Notification objects

tnSapStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 3, 0, 3)
)
tnSapStatusChanged.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SERV-MIB", "tnSvcVpnId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"),
        ("TN-SAP-MIB", "tnSapAdminStatus"),
        ("TN-SAP-MIB", "tnSapOperStatus"),
        ("TN-SAP-MIB", "tnSapOperFlags"))
)
if mibBuilder.loadTexts:
    tnSapStatusChanged.setStatus(
        "current"
    )

tnSapTlsMacAddrLimitAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 3, 0, 4)
)
tnSapTlsMacAddrLimitAlarmRaised.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SERV-MIB", "tnSvcVpnId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"))
)
if mibBuilder.loadTexts:
    tnSapTlsMacAddrLimitAlarmRaised.setStatus(
        "current"
    )

tnSapTlsMacAddrLimitAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 3, 0, 5)
)
tnSapTlsMacAddrLimitAlarmCleared.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SERV-MIB", "tnSvcVpnId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"))
)
if mibBuilder.loadTexts:
    tnSapTlsMacAddrLimitAlarmCleared.setStatus(
        "current"
    )

tnSapDHCPLseStateMobilityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 3, 0, 22)
)
tnSapDHCPLseStateMobilityError.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SERV-MIB", "tnSvcVpnId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"))
)
if mibBuilder.loadTexts:
    tnSapDHCPLseStateMobilityError.setStatus(
        "current"
    )

tnTopologyChangeSapMajorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5, 0, 1)
)
tnTopologyChangeSapMajorState.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"))
)
if mibBuilder.loadTexts:
    tnTopologyChangeSapMajorState.setStatus(
        "current"
    )

tnNewRootSap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5, 0, 2)
)
tnNewRootSap.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"))
)
if mibBuilder.loadTexts:
    tnNewRootSap.setStatus(
        "current"
    )

tnTopologyChangeSapState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5, 0, 5)
)
tnTopologyChangeSapState.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"))
)
if mibBuilder.loadTexts:
    tnTopologyChangeSapState.setStatus(
        "current"
    )

tnReceivedTCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5, 0, 6)
)
tnReceivedTCN.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"))
)
if mibBuilder.loadTexts:
    tnReceivedTCN.setStatus(
        "current"
    )

tnSapActiveProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5, 0, 30)
)
tnSapActiveProtocolChange.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"),
        ("TN-SAP-MIB", "tnSapTlsStpOperProtocol"))
)
if mibBuilder.loadTexts:
    tnSapActiveProtocolChange.setStatus(
        "current"
    )

tnStpRootGuardViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5, 0, 35)
)
tnStpRootGuardViolation.setObjects(
      *(("TN-SERV-MIB", "tnSvcId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"),
        ("TN-SAP-MIB", "tnSapTlsStpRootGuardViolation"))
)
if mibBuilder.loadTexts:
    tnStpRootGuardViolation.setStatus(
        "current"
    )

tnSapStpExcepCondStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 4, 5, 0, 37)
)
tnSapStpExcepCondStateChng.setObjects(
      *(("TN-SERV-MIB", "tnCustId"),
        ("TN-SERV-MIB", "tnSvcId"),
        ("TN-SAP-MIB", "tnSapPortId"),
        ("TN-SAP-MIB", "tnSapEncapValue"),
        ("TN-SAP-MIB", "tnSapTlsStpException"))
)
if mibBuilder.loadTexts:
    tnSapStpExcepCondStateChng.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAP-MIB",
    **{"tnSvcSapMIBModule": tnSvcSapMIBModule,
       "tnSapObjs": tnSapObjs,
       "tnSapBaseInfoTable": tnSapBaseInfoTable,
       "tnSapBaseInfoEntry": tnSapBaseInfoEntry,
       "tnSapPortId": tnSapPortId,
       "tnSapEncapValue": tnSapEncapValue,
       "tnSapRowStatus": tnSapRowStatus,
       "tnSapType": tnSapType,
       "tnSapDescription": tnSapDescription,
       "tnSapAdminStatus": tnSapAdminStatus,
       "tnSapOperStatus": tnSapOperStatus,
       "tnSapIngressQosPolicyId": tnSapIngressQosPolicyId,
       "tnSapIngressMacFilterId": tnSapIngressMacFilterId,
       "tnSapIngressIpFilterId": tnSapIngressIpFilterId,
       "tnSapEgressQosPolicyId": tnSapEgressQosPolicyId,
       "tnSapEgressMacFilterId": tnSapEgressMacFilterId,
       "tnSapEgressIpFilterId": tnSapEgressIpFilterId,
       "tnSapMirrorStatus": tnSapMirrorStatus,
       "tnSapIesIfIndex": tnSapIesIfIndex,
       "tnSapLastMgmtChange": tnSapLastMgmtChange,
       "tnSapCollectAcctStats": tnSapCollectAcctStats,
       "tnSapAccountingPolicyId": tnSapAccountingPolicyId,
       "tnSapVpnId": tnSapVpnId,
       "tnSapCustId": tnSapCustId,
       "tnSapCustMultSvcSite": tnSapCustMultSvcSite,
       "tnSapIngressQosSchedulerPolicy": tnSapIngressQosSchedulerPolicy,
       "tnSapEgressQosSchedulerPolicy": tnSapEgressQosSchedulerPolicy,
       "tnSapSplitHorizonGrp": tnSapSplitHorizonGrp,
       "tnSapIngressSharedQueuePolicy": tnSapIngressSharedQueuePolicy,
       "tnSapIngressMatchQinQDot1PBits": tnSapIngressMatchQinQDot1PBits,
       "tnSapOperFlags": tnSapOperFlags,
       "tnSapLastStatusChange": tnSapLastStatusChange,
       "tnSapAntiSpoofing": tnSapAntiSpoofing,
       "tnSapIngressIpv6FilterId": tnSapIngressIpv6FilterId,
       "tnSapEgressIpv6FilterId": tnSapEgressIpv6FilterId,
       "tnSapTodSuite": tnSapTodSuite,
       "tnSapIngUseMultipointShared": tnSapIngUseMultipointShared,
       "tnSapEgressQinQMarkTopOnly": tnSapEgressQinQMarkTopOnly,
       "tnSapEgressAggRateLimit": tnSapEgressAggRateLimit,
       "tnSapEndPoint": tnSapEndPoint,
       "tnSapIngressVlanTranslation": tnSapIngressVlanTranslation,
       "tnSapIngressVlanTranslationId": tnSapIngressVlanTranslationId,
       "tnSapSubType": tnSapSubType,
       "tnSapCpmProtPolicyId": tnSapCpmProtPolicyId,
       "tnSapCpmProtMonitorMac": tnSapCpmProtMonitorMac,
       "tnSapEgressFrameBasedAccounting": tnSapEgressFrameBasedAccounting,
       "tnSapIngressAggRateLimit": tnSapIngressAggRateLimit,
       "tnSapEgressHsmdaShaperOverride": tnSapEgressHsmdaShaperOverride,
       "tnSapIngressHsmdaPacketOffOvr": tnSapIngressHsmdaPacketOffOvr,
       "tnSapEgressHsmdaPacketOffOverride": tnSapEgressHsmdaPacketOffOverride,
       "tnSapCallingStationId": tnSapCallingStationId,
       "tnSapIsaAaApplicationProfile": tnSapIsaAaApplicationProfile,
       "tnSapEthRingIndex": tnSapEthRingIndex,
       "tnSapTlsInfoTable": tnSapTlsInfoTable,
       "tnSapTlsInfoEntry": tnSapTlsInfoEntry,
       "tnSapTlsStpAdminStatus": tnSapTlsStpAdminStatus,
       "tnSapTlsStpPriority": tnSapTlsStpPriority,
       "tnSapTlsStpPortNum": tnSapTlsStpPortNum,
       "tnSapTlsStpPathCost": tnSapTlsStpPathCost,
       "tnSapTlsStpRapidStart": tnSapTlsStpRapidStart,
       "tnSapTlsStpBpduEncap": tnSapTlsStpBpduEncap,
       "tnSapTlsStpPortState": tnSapTlsStpPortState,
       "tnSapTlsStpDesignatedBridge": tnSapTlsStpDesignatedBridge,
       "tnSapTlsStpDesignatedPort": tnSapTlsStpDesignatedPort,
       "tnSapTlsStpForwardTransitions": tnSapTlsStpForwardTransitions,
       "tnSapTlsStpInConfigBpdus": tnSapTlsStpInConfigBpdus,
       "tnSapTlsStpInTcnBpdus": tnSapTlsStpInTcnBpdus,
       "tnSapTlsStpInBadBpdus": tnSapTlsStpInBadBpdus,
       "tnSapTlsStpOutConfigBpdus": tnSapTlsStpOutConfigBpdus,
       "tnSapTlsStpOutTcnBpdus": tnSapTlsStpOutTcnBpdus,
       "tnSapTlsStpOperBpduEncap": tnSapTlsStpOperBpduEncap,
       "tnSapTlsVpnId": tnSapTlsVpnId,
       "tnSapTlsCustId": tnSapTlsCustId,
       "tnSapTlsMacAddressLimit": tnSapTlsMacAddressLimit,
       "tnSapTlsNumMacAddresses": tnSapTlsNumMacAddresses,
       "tnSapTlsNumStaticMacAddresses": tnSapTlsNumStaticMacAddresses,
       "tnSapTlsMacLearning": tnSapTlsMacLearning,
       "tnSapTlsMacAgeing": tnSapTlsMacAgeing,
       "tnSapTlsStpOperEdge": tnSapTlsStpOperEdge,
       "tnSapTlsStpAdminPointToPoint": tnSapTlsStpAdminPointToPoint,
       "tnSapTlsStpPortRole": tnSapTlsStpPortRole,
       "tnSapTlsStpAutoEdge": tnSapTlsStpAutoEdge,
       "tnSapTlsStpOperProtocol": tnSapTlsStpOperProtocol,
       "tnSapTlsStpInRstBpdus": tnSapTlsStpInRstBpdus,
       "tnSapTlsStpOutRstBpdus": tnSapTlsStpOutRstBpdus,
       "tnSapTlsLimitMacMove": tnSapTlsLimitMacMove,
       "tnSapTlsMacPinning": tnSapTlsMacPinning,
       "tnSapTlsDiscardUnknownSource": tnSapTlsDiscardUnknownSource,
       "tnSapTlsMvplsPruneState": tnSapTlsMvplsPruneState,
       "tnSapTlsMvplsMgmtService": tnSapTlsMvplsMgmtService,
       "tnSapTlsMvplsMgmtPortId": tnSapTlsMvplsMgmtPortId,
       "tnSapTlsMvplsMgmtEncapValue": tnSapTlsMvplsMgmtEncapValue,
       "tnSapTlsArpReplyAgent": tnSapTlsArpReplyAgent,
       "tnSapTlsStpException": tnSapTlsStpException,
       "tnSapTlsAuthenticationPolicy": tnSapTlsAuthenticationPolicy,
       "tnSapTlsL2ptTermination": tnSapTlsL2ptTermination,
       "tnSapTlsBpduTranslation": tnSapTlsBpduTranslation,
       "tnSapTlsStpRootGuard": tnSapTlsStpRootGuard,
       "tnSapTlsStpInsideRegion": tnSapTlsStpInsideRegion,
       "tnSapTlsEgressMcastGroup": tnSapTlsEgressMcastGroup,
       "tnSapTlsStpInMstBpdus": tnSapTlsStpInMstBpdus,
       "tnSapTlsStpOutMstBpdus": tnSapTlsStpOutMstBpdus,
       "tnSapTlsRestProtSrcMac": tnSapTlsRestProtSrcMac,
       "tnSapTlsRestUnprotDstMac": tnSapTlsRestUnprotDstMac,
       "tnSapTlsStpRxdDesigBridge": tnSapTlsStpRxdDesigBridge,
       "tnSapTlsStpRootGuardViolation": tnSapTlsStpRootGuardViolation,
       "tnSapTlsShcvAction": tnSapTlsShcvAction,
       "tnSapTlsShcvSrcIp": tnSapTlsShcvSrcIp,
       "tnSapTlsShcvSrcMac": tnSapTlsShcvSrcMac,
       "tnSapTlsShcvInterval": tnSapTlsShcvInterval,
       "tnSapTlsMvplsMgmtMsti": tnSapTlsMvplsMgmtMsti,
       "tnSapTlsMacMoveNextUpTime": tnSapTlsMacMoveNextUpTime,
       "tnSapTlsMacMoveRateExcdLeft": tnSapTlsMacMoveRateExcdLeft,
       "tnSapTlsRestProtSrcMacAction": tnSapTlsRestProtSrcMacAction,
       "tnSapTlsL2ptForceBoundary": tnSapTlsL2ptForceBoundary,
       "tnSapTlsLimitMacMoveLevel": tnSapTlsLimitMacMoveLevel,
       "tnSapTlsBpduTransOper": tnSapTlsBpduTransOper,
       "tnSapTlsDefMtnSapPolicy": tnSapTlsDefMtnSapPolicy,
       "tnSapTlsL2ptProtocols": tnSapTlsL2ptProtocols,
       "tnSapTlsL2ptForceProtocols": tnSapTlsL2ptForceProtocols,
       "tnSapTlsPppoeMtnSapTrigger": tnSapTlsPppoeMtnSapTrigger,
       "tnSapTlsDhcpMtnSapTrigger": tnSapTlsDhcpMtnSapTrigger,
       "tnSapTlsMrpJoinTime": tnSapTlsMrpJoinTime,
       "tnSapTlsMrpLeaveTime": tnSapTlsMrpLeaveTime,
       "tnSapTlsMrpLeaveAllTime": tnSapTlsMrpLeaveAllTime,
       "tnSapTlsMrpPeriodicTime": tnSapTlsMrpPeriodicTime,
       "tnSapTlsMrpPeriodicEnabled": tnSapTlsMrpPeriodicEnabled,
       "tnSapTlsPppoePolicy": tnSapTlsPppoePolicy,
       "tnSapTlsArpMsapTrigger": tnSapTlsArpMsapTrigger,
       "tnSapTlsInTcBitBpdus": tnSapTlsInTcBitBpdus,
       "tnSapTlsOutTcBitBpdus": tnSapTlsOutTcBitBpdus,
       "tnSapTlsShcvRetryTimeout": tnSapTlsShcvRetryTimeout,
       "tnSapTlsShcvRetryCount": tnSapTlsShcvRetryCount,
       "tnSapScalar1": tnSapScalar1,
       "tnSapBaseStatsTable": tnSapBaseStatsTable,
       "tnSapBaseStatsEntry": tnSapBaseStatsEntry,
       "tnSapBaseStatsIngressPchipDroppedPackets": tnSapBaseStatsIngressPchipDroppedPackets,
       "tnSapBaseStatsIngressPchipDroppedOctets": tnSapBaseStatsIngressPchipDroppedOctets,
       "tnSapBaseStatsIngressPchipOfferedHiPrioPackets": tnSapBaseStatsIngressPchipOfferedHiPrioPackets,
       "tnSapBaseStatsIngressPchipOfferedHiPrioOctets": tnSapBaseStatsIngressPchipOfferedHiPrioOctets,
       "tnSapBaseStatsIngressPchipOfferedLoPrioPackets": tnSapBaseStatsIngressPchipOfferedLoPrioPackets,
       "tnSapBaseStatsIngressPchipOfferedLoPrioOctets": tnSapBaseStatsIngressPchipOfferedLoPrioOctets,
       "tnSapBaseStatsIngressQchipDroppedHiPrioPackets": tnSapBaseStatsIngressQchipDroppedHiPrioPackets,
       "tnSapBaseStatsIngressQchipDroppedHiPrioOctets": tnSapBaseStatsIngressQchipDroppedHiPrioOctets,
       "tnSapBaseStatsIngressQchipDroppedLoPrioPackets": tnSapBaseStatsIngressQchipDroppedLoPrioPackets,
       "tnSapBaseStatsIngressQchipDroppedLoPrioOctets": tnSapBaseStatsIngressQchipDroppedLoPrioOctets,
       "tnSapBaseStatsIngressQchipForwardedInProfPackets": tnSapBaseStatsIngressQchipForwardedInProfPackets,
       "tnSapBaseStatsIngressQchipForwardedInProfOctets": tnSapBaseStatsIngressQchipForwardedInProfOctets,
       "tnSapBaseStatsIngressQchipForwardedOutProfPackets": tnSapBaseStatsIngressQchipForwardedOutProfPackets,
       "tnSapBaseStatsIngressQchipForwardedOutProfOctets": tnSapBaseStatsIngressQchipForwardedOutProfOctets,
       "tnSapBaseStatsEgressQchipDroppedInProfPackets": tnSapBaseStatsEgressQchipDroppedInProfPackets,
       "tnSapBaseStatsEgressQchipDroppedInProfOctets": tnSapBaseStatsEgressQchipDroppedInProfOctets,
       "tnSapBaseStatsEgressQchipDroppedOutProfPackets": tnSapBaseStatsEgressQchipDroppedOutProfPackets,
       "tnSapBaseStatsEgressQchipDroppedOutProfOctets": tnSapBaseStatsEgressQchipDroppedOutProfOctets,
       "tnSapBaseStatsEgressQchipForwardedInProfPackets": tnSapBaseStatsEgressQchipForwardedInProfPackets,
       "tnSapBaseStatsEgressQchipForwardedInProfOctets": tnSapBaseStatsEgressQchipForwardedInProfOctets,
       "tnSapBaseStatsEgressQchipForwardedOutProfPackets": tnSapBaseStatsEgressQchipForwardedOutProfPackets,
       "tnSapBaseStatsEgressQchipForwardedOutProfOctets": tnSapBaseStatsEgressQchipForwardedOutProfOctets,
       "tnSapBaseStatsCustId": tnSapBaseStatsCustId,
       "tnSapBaseStatsIngressPchipOfferedUncoloredPackets": tnSapBaseStatsIngressPchipOfferedUncoloredPackets,
       "tnSapBaseStatsIngressPchipOfferedUncoloredOctets": tnSapBaseStatsIngressPchipOfferedUncoloredOctets,
       "tnSapBaseStatsAuthenticationPktsDiscarded": tnSapBaseStatsAuthenticationPktsDiscarded,
       "tnSapBaseStatsAuthenticationPktsSuccess": tnSapBaseStatsAuthenticationPktsSuccess,
       "tnSapBaseStatsLastClearedTime": tnSapBaseStatsLastClearedTime,
       "tnSapEthernetInfoTable": tnSapEthernetInfoTable,
       "tnSapEthernetInfoEntry": tnSapEthernetInfoEntry,
       "tnSapEthernetLLFAdminStatus": tnSapEthernetLLFAdminStatus,
       "tnSapEthernetLLFOperStatus": tnSapEthernetLLFOperStatus,
       "tnSapEthernetLLFId": tnSapEthernetLLFId,
       "tnSapTlsMrpTable": tnSapTlsMrpTable,
       "tnSapTlsMrpEntry": tnSapTlsMrpEntry,
       "tnSapTlsMrpRxPdus": tnSapTlsMrpRxPdus,
       "tnSapTlsMrpDroppedPdus": tnSapTlsMrpDroppedPdus,
       "tnSapTlsMrpTxPdus": tnSapTlsMrpTxPdus,
       "tnSapTlsMrpRxNewEvent": tnSapTlsMrpRxNewEvent,
       "tnSapTlsMrpRxJoinInEvent": tnSapTlsMrpRxJoinInEvent,
       "tnSapTlsMrpRxInEvent": tnSapTlsMrpRxInEvent,
       "tnSapTlsMrpRxJoinEmptyEvent": tnSapTlsMrpRxJoinEmptyEvent,
       "tnSapTlsMrpRxEmptyEvent": tnSapTlsMrpRxEmptyEvent,
       "tnSapTlsMrpRxLeaveEvent": tnSapTlsMrpRxLeaveEvent,
       "tnSapTlsMrpTxNewEvent": tnSapTlsMrpTxNewEvent,
       "tnSapTlsMrpTxJoinInEvent": tnSapTlsMrpTxJoinInEvent,
       "tnSapTlsMrpTxInEvent": tnSapTlsMrpTxInEvent,
       "tnSapTlsMrpTxJoinEmptyEvent": tnSapTlsMrpTxJoinEmptyEvent,
       "tnSapTlsMrpTxEmptyEvent": tnSapTlsMrpTxEmptyEvent,
       "tnSapTlsMrpTxLeaveEvent": tnSapTlsMrpTxLeaveEvent,
       "tnSapTrapsPrefix": tnSapTrapsPrefix,
       "tnSapTraps": tnSapTraps,
       "tnSapStatusChanged": tnSapStatusChanged,
       "tnSapTlsMacAddrLimitAlarmRaised": tnSapTlsMacAddrLimitAlarmRaised,
       "tnSapTlsMacAddrLimitAlarmCleared": tnSapTlsMacAddrLimitAlarmCleared,
       "tnSapDHCPLseStateMobilityError": tnSapDHCPLseStateMobilityError,
       "tnTopologyChangeSapMajorState": tnTopologyChangeSapMajorState,
       "tnNewRootSap": tnNewRootSap,
       "tnTopologyChangeSapState": tnTopologyChangeSapState,
       "tnReceivedTCN": tnReceivedTCN,
       "tnSapActiveProtocolChange": tnSapActiveProtocolChange,
       "tnStpRootGuardViolation": tnStpRootGuardViolation,
       "tnSapStpExcepCondStateChng": tnSapStpExcepCondStateChng}
)
