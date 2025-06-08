# SNMP MIB module (F3-FPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-FPM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:57 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 CmPmBinAction,
 CmPmIntervalType,
 FlowSecState,
 OperationalState,
 PerfCounter64,
 SecondaryState,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "CmPmIntervalType",
    "FlowSecState",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState",
    "VlanId",
    "VlanPriority")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(CmActiveControlProtocolsType,
 CmControlProtocolDispType,
 FlowTagControl,
 FlowVlanActionType,
 PolicerAlgorithmType,
 PolicerColorMode,
 ShapingType,
 cmEthernetAccPortIndex,
 cmEthernetNetPortIndex,
 cmMPFlowEntry,
 cmMPFlowIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "CmActiveControlProtocolsType",
    "CmControlProtocolDispType",
    "FlowTagControl",
    "FlowVlanActionType",
    "PolicerAlgorithmType",
    "PolicerColorMode",
    "ShapingType",
    "cmEthernetAccPortIndex",
    "cmEthernetNetPortIndex",
    "cmMPFlowEntry",
    "cmMPFlowIndex")

(FlowLearningConfigAction,
 LearningAction,
 ProtectLearningControl) = mibBuilder.importSymbols(
    "F3-BRIDGE-MIB",
    "FlowLearningConfigAction",
    "LearningAction",
    "ProtectLearningControl")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3FpmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43)
)
if mibBuilder.loadTexts:
    f3FpmMIB.setRevisions(
        ("2016-07-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F3FpmConfigObjects_ObjectIdentity = ObjectIdentity
f3FpmConfigObjects = _F3FpmConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1)
)
_F3AccFlowPointTable_Object = MibTable
f3AccFlowPointTable = _F3AccFlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1)
)
if mibBuilder.loadTexts:
    f3AccFlowPointTable.setStatus("current")
_F3AccFlowPointEntry_Object = MibTableRow
f3AccFlowPointEntry = _F3AccFlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1)
)
f3AccFlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3AccFlowPointEntry.setStatus("current")


class _F3AccFlowPointIndex_Type(Integer32):
    """Custom type f3AccFlowPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFlowPointIndex_Type.__name__ = "Integer32"
_F3AccFlowPointIndex_Object = MibTableColumn
f3AccFlowPointIndex = _F3AccFlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 1),
    _F3AccFlowPointIndex_Type()
)
f3AccFlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AccFlowPointIndex.setStatus("current")


class _F3AccFlowPointAlias_Type(DisplayString):
    """Custom type f3AccFlowPointAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3AccFlowPointAlias_Type.__name__ = "DisplayString"
_F3AccFlowPointAlias_Object = MibTableColumn
f3AccFlowPointAlias = _F3AccFlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 2),
    _F3AccFlowPointAlias_Type()
)
f3AccFlowPointAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointAlias.setStatus("current")
_F3AccFlowPointAdminState_Type = AdminState
_F3AccFlowPointAdminState_Object = MibTableColumn
f3AccFlowPointAdminState = _F3AccFlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 3),
    _F3AccFlowPointAdminState_Type()
)
f3AccFlowPointAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointAdminState.setStatus("current")
_F3AccFlowPointOperationalState_Type = OperationalState
_F3AccFlowPointOperationalState_Object = MibTableColumn
f3AccFlowPointOperationalState = _F3AccFlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 4),
    _F3AccFlowPointOperationalState_Type()
)
f3AccFlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointOperationalState.setStatus("current")
_F3AccFlowPointSecondaryState_Type = SecondaryState
_F3AccFlowPointSecondaryState_Object = MibTableColumn
f3AccFlowPointSecondaryState = _F3AccFlowPointSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 5),
    _F3AccFlowPointSecondaryState_Type()
)
f3AccFlowPointSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointSecondaryState.setStatus("current")
_F3AccFlowPointAssociatedFlowId_Type = VariablePointer
_F3AccFlowPointAssociatedFlowId_Object = MibTableColumn
f3AccFlowPointAssociatedFlowId = _F3AccFlowPointAssociatedFlowId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 6),
    _F3AccFlowPointAssociatedFlowId_Type()
)
f3AccFlowPointAssociatedFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointAssociatedFlowId.setStatus("current")
_F3AccFlowPointIngressMultiCOSEnabled_Type = TruthValue
_F3AccFlowPointIngressMultiCOSEnabled_Object = MibTableColumn
f3AccFlowPointIngressMultiCOSEnabled = _F3AccFlowPointIngressMultiCOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 7),
    _F3AccFlowPointIngressMultiCOSEnabled_Type()
)
f3AccFlowPointIngressMultiCOSEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointIngressMultiCOSEnabled.setStatus("current")
_F3AccFlowPointIngressCOS_Type = Integer32
_F3AccFlowPointIngressCOS_Object = MibTableColumn
f3AccFlowPointIngressCOS = _F3AccFlowPointIngressCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 8),
    _F3AccFlowPointIngressCOS_Type()
)
f3AccFlowPointIngressCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointIngressCOS.setStatus("deprecated")
_F3AccFlowPointEgressShapingType_Type = ShapingType
_F3AccFlowPointEgressShapingType_Object = MibTableColumn
f3AccFlowPointEgressShapingType = _F3AccFlowPointEgressShapingType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 9),
    _F3AccFlowPointEgressShapingType_Type()
)
f3AccFlowPointEgressShapingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointEgressShapingType.setStatus("current")


class _F3AccFlowPointIngressVlanMemberList_Type(DisplayString):
    """Custom type f3AccFlowPointIngressVlanMemberList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_F3AccFlowPointIngressVlanMemberList_Type.__name__ = "DisplayString"
_F3AccFlowPointIngressVlanMemberList_Object = MibTableColumn
f3AccFlowPointIngressVlanMemberList = _F3AccFlowPointIngressVlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 10),
    _F3AccFlowPointIngressVlanMemberList_Type()
)
f3AccFlowPointIngressVlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointIngressVlanMemberList.setStatus("current")
_F3AccFlowPointVlanMemberAction_Type = FlowVlanActionType
_F3AccFlowPointVlanMemberAction_Object = MibTableColumn
f3AccFlowPointVlanMemberAction = _F3AccFlowPointVlanMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 11),
    _F3AccFlowPointVlanMemberAction_Type()
)
f3AccFlowPointVlanMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointVlanMemberAction.setStatus("current")


class _F3AccFlowPointVlanMemberActionVlan_Type(DisplayString):
    """Custom type f3AccFlowPointVlanMemberActionVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_F3AccFlowPointVlanMemberActionVlan_Type.__name__ = "DisplayString"
_F3AccFlowPointVlanMemberActionVlan_Object = MibTableColumn
f3AccFlowPointVlanMemberActionVlan = _F3AccFlowPointVlanMemberActionVlan_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 12),
    _F3AccFlowPointVlanMemberActionVlan_Type()
)
f3AccFlowPointVlanMemberActionVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointVlanMemberActionVlan.setStatus("current")
_F3AccFlowPointIngressUntaggedFrameEnabled_Type = TruthValue
_F3AccFlowPointIngressUntaggedFrameEnabled_Object = MibTableColumn
f3AccFlowPointIngressUntaggedFrameEnabled = _F3AccFlowPointIngressUntaggedFrameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 13),
    _F3AccFlowPointIngressUntaggedFrameEnabled_Type()
)
f3AccFlowPointIngressUntaggedFrameEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointIngressUntaggedFrameEnabled.setStatus("current")
_F3AccFlowPointCTagControl_Type = FlowTagControl
_F3AccFlowPointCTagControl_Object = MibTableColumn
f3AccFlowPointCTagControl = _F3AccFlowPointCTagControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 14),
    _F3AccFlowPointCTagControl_Type()
)
f3AccFlowPointCTagControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointCTagControl.setStatus("current")
_F3AccFlowPointCTagVlanId_Type = VlanId
_F3AccFlowPointCTagVlanId_Object = MibTableColumn
f3AccFlowPointCTagVlanId = _F3AccFlowPointCTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 15),
    _F3AccFlowPointCTagVlanId_Type()
)
f3AccFlowPointCTagVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointCTagVlanId.setStatus("current")
_F3AccFlowPointCTagVlanPriority_Type = VlanPriority
_F3AccFlowPointCTagVlanPriority_Object = MibTableColumn
f3AccFlowPointCTagVlanPriority = _F3AccFlowPointCTagVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 16),
    _F3AccFlowPointCTagVlanPriority_Type()
)
f3AccFlowPointCTagVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointCTagVlanPriority.setStatus("current")
_F3AccFlowPointSTagControl_Type = FlowTagControl
_F3AccFlowPointSTagControl_Object = MibTableColumn
f3AccFlowPointSTagControl = _F3AccFlowPointSTagControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 17),
    _F3AccFlowPointSTagControl_Type()
)
f3AccFlowPointSTagControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointSTagControl.setStatus("current")
_F3AccFlowPointSTagVlanId_Type = VlanId
_F3AccFlowPointSTagVlanId_Object = MibTableColumn
f3AccFlowPointSTagVlanId = _F3AccFlowPointSTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 18),
    _F3AccFlowPointSTagVlanId_Type()
)
f3AccFlowPointSTagVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointSTagVlanId.setStatus("current")
_F3AccFlowPointSTagVlanPriority_Type = VlanPriority
_F3AccFlowPointSTagVlanPriority_Object = MibTableColumn
f3AccFlowPointSTagVlanPriority = _F3AccFlowPointSTagVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 19),
    _F3AccFlowPointSTagVlanPriority_Type()
)
f3AccFlowPointSTagVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointSTagVlanPriority.setStatus("current")
_F3AccFlowPointEgressOuterTagPrioMapEnabled_Type = TruthValue
_F3AccFlowPointEgressOuterTagPrioMapEnabled_Object = MibTableColumn
f3AccFlowPointEgressOuterTagPrioMapEnabled = _F3AccFlowPointEgressOuterTagPrioMapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 20),
    _F3AccFlowPointEgressOuterTagPrioMapEnabled_Type()
)
f3AccFlowPointEgressOuterTagPrioMapEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointEgressOuterTagPrioMapEnabled.setStatus("current")
_F3AccFlowPointEgressInnerTagPrioMapEnabled_Type = TruthValue
_F3AccFlowPointEgressInnerTagPrioMapEnabled_Object = MibTableColumn
f3AccFlowPointEgressInnerTagPrioMapEnabled = _F3AccFlowPointEgressInnerTagPrioMapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 21),
    _F3AccFlowPointEgressInnerTagPrioMapEnabled_Type()
)
f3AccFlowPointEgressInnerTagPrioMapEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointEgressInnerTagPrioMapEnabled.setStatus("current")


class _F3AccFlowPointSESFramesLossThresholdRatio_Type(Integer32):
    """Custom type f3AccFlowPointSESFramesLossThresholdRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_F3AccFlowPointSESFramesLossThresholdRatio_Type.__name__ = "Integer32"
_F3AccFlowPointSESFramesLossThresholdRatio_Object = MibTableColumn
f3AccFlowPointSESFramesLossThresholdRatio = _F3AccFlowPointSESFramesLossThresholdRatio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 22),
    _F3AccFlowPointSESFramesLossThresholdRatio_Type()
)
f3AccFlowPointSESFramesLossThresholdRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointSESFramesLossThresholdRatio.setStatus("current")
_F3AccFlowPointDefaultMemberEnabled_Type = TruthValue
_F3AccFlowPointDefaultMemberEnabled_Object = MibTableColumn
f3AccFlowPointDefaultMemberEnabled = _F3AccFlowPointDefaultMemberEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 23),
    _F3AccFlowPointDefaultMemberEnabled_Type()
)
f3AccFlowPointDefaultMemberEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointDefaultMemberEnabled.setStatus("current")
_F3AccFlowPointMcastRateLimitEnabled_Type = TruthValue
_F3AccFlowPointMcastRateLimitEnabled_Object = MibTableColumn
f3AccFlowPointMcastRateLimitEnabled = _F3AccFlowPointMcastRateLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 24),
    _F3AccFlowPointMcastRateLimitEnabled_Type()
)
f3AccFlowPointMcastRateLimitEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointMcastRateLimitEnabled.setStatus("current")
_F3AccFlowPointMcastRateLimitSpeedLo_Type = Unsigned32
_F3AccFlowPointMcastRateLimitSpeedLo_Object = MibTableColumn
f3AccFlowPointMcastRateLimitSpeedLo = _F3AccFlowPointMcastRateLimitSpeedLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 25),
    _F3AccFlowPointMcastRateLimitSpeedLo_Type()
)
f3AccFlowPointMcastRateLimitSpeedLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointMcastRateLimitSpeedLo.setStatus("current")
_F3AccFlowPointMcastRateLimitSpeedHi_Type = Unsigned32
_F3AccFlowPointMcastRateLimitSpeedHi_Object = MibTableColumn
f3AccFlowPointMcastRateLimitSpeedHi = _F3AccFlowPointMcastRateLimitSpeedHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 26),
    _F3AccFlowPointMcastRateLimitSpeedHi_Type()
)
f3AccFlowPointMcastRateLimitSpeedHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointMcastRateLimitSpeedHi.setStatus("current")
_F3AccFlowPointBcastRateLimitEnabled_Type = TruthValue
_F3AccFlowPointBcastRateLimitEnabled_Object = MibTableColumn
f3AccFlowPointBcastRateLimitEnabled = _F3AccFlowPointBcastRateLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 27),
    _F3AccFlowPointBcastRateLimitEnabled_Type()
)
f3AccFlowPointBcastRateLimitEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointBcastRateLimitEnabled.setStatus("current")
_F3AccFlowPointBcastRateLimitSpeedLo_Type = Unsigned32
_F3AccFlowPointBcastRateLimitSpeedLo_Object = MibTableColumn
f3AccFlowPointBcastRateLimitSpeedLo = _F3AccFlowPointBcastRateLimitSpeedLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 28),
    _F3AccFlowPointBcastRateLimitSpeedLo_Type()
)
f3AccFlowPointBcastRateLimitSpeedLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointBcastRateLimitSpeedLo.setStatus("current")
_F3AccFlowPointBcastRateLimitSpeedHi_Type = Unsigned32
_F3AccFlowPointBcastRateLimitSpeedHi_Object = MibTableColumn
f3AccFlowPointBcastRateLimitSpeedHi = _F3AccFlowPointBcastRateLimitSpeedHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 29),
    _F3AccFlowPointBcastRateLimitSpeedHi_Type()
)
f3AccFlowPointBcastRateLimitSpeedHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointBcastRateLimitSpeedHi.setStatus("current")
_F3AccFlowPointCombinedRateLimitEnabled_Type = TruthValue
_F3AccFlowPointCombinedRateLimitEnabled_Object = MibTableColumn
f3AccFlowPointCombinedRateLimitEnabled = _F3AccFlowPointCombinedRateLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 30),
    _F3AccFlowPointCombinedRateLimitEnabled_Type()
)
f3AccFlowPointCombinedRateLimitEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointCombinedRateLimitEnabled.setStatus("current")
_F3AccFlowPointCombinedRateLimitSpeedLo_Type = Unsigned32
_F3AccFlowPointCombinedRateLimitSpeedLo_Object = MibTableColumn
f3AccFlowPointCombinedRateLimitSpeedLo = _F3AccFlowPointCombinedRateLimitSpeedLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 31),
    _F3AccFlowPointCombinedRateLimitSpeedLo_Type()
)
f3AccFlowPointCombinedRateLimitSpeedLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointCombinedRateLimitSpeedLo.setStatus("current")
_F3AccFlowPointCombinedRateLimitSpeedHi_Type = Unsigned32
_F3AccFlowPointCombinedRateLimitSpeedHi_Object = MibTableColumn
f3AccFlowPointCombinedRateLimitSpeedHi = _F3AccFlowPointCombinedRateLimitSpeedHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 32),
    _F3AccFlowPointCombinedRateLimitSpeedHi_Type()
)
f3AccFlowPointCombinedRateLimitSpeedHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointCombinedRateLimitSpeedHi.setStatus("current")
_F3AccFlowPointSplitHorizonGroupOID_Type = VariablePointer
_F3AccFlowPointSplitHorizonGroupOID_Object = MibTableColumn
f3AccFlowPointSplitHorizonGroupOID = _F3AccFlowPointSplitHorizonGroupOID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 33),
    _F3AccFlowPointSplitHorizonGroupOID_Type()
)
f3AccFlowPointSplitHorizonGroupOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointSplitHorizonGroupOID.setStatus("current")
_F3AccFlowPointLoopAvoidance_Type = VariablePointer
_F3AccFlowPointLoopAvoidance_Object = MibTableColumn
f3AccFlowPointLoopAvoidance = _F3AccFlowPointLoopAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 34),
    _F3AccFlowPointLoopAvoidance_Type()
)
f3AccFlowPointLoopAvoidance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointLoopAvoidance.setStatus("current")
_F3AccFlowPointHierarchicalCOSEnabled_Type = TruthValue
_F3AccFlowPointHierarchicalCOSEnabled_Object = MibTableColumn
f3AccFlowPointHierarchicalCOSEnabled = _F3AccFlowPointHierarchicalCOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 35),
    _F3AccFlowPointHierarchicalCOSEnabled_Type()
)
f3AccFlowPointHierarchicalCOSEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointHierarchicalCOSEnabled.setStatus("current")
_F3AccFlowPointMaximumBWLo_Type = Unsigned32
_F3AccFlowPointMaximumBWLo_Object = MibTableColumn
f3AccFlowPointMaximumBWLo = _F3AccFlowPointMaximumBWLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 36),
    _F3AccFlowPointMaximumBWLo_Type()
)
f3AccFlowPointMaximumBWLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointMaximumBWLo.setStatus("current")
_F3AccFlowPointMaximumBWHi_Type = Unsigned32
_F3AccFlowPointMaximumBWHi_Object = MibTableColumn
f3AccFlowPointMaximumBWHi = _F3AccFlowPointMaximumBWHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 37),
    _F3AccFlowPointMaximumBWHi_Type()
)
f3AccFlowPointMaximumBWHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointMaximumBWHi.setStatus("current")
_F3AccFlowPointGuaranteedBWLo_Type = Unsigned32
_F3AccFlowPointGuaranteedBWLo_Object = MibTableColumn
f3AccFlowPointGuaranteedBWLo = _F3AccFlowPointGuaranteedBWLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 38),
    _F3AccFlowPointGuaranteedBWLo_Type()
)
f3AccFlowPointGuaranteedBWLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointGuaranteedBWLo.setStatus("current")
_F3AccFlowPointGuaranteedBWHi_Type = Unsigned32
_F3AccFlowPointGuaranteedBWHi_Object = MibTableColumn
f3AccFlowPointGuaranteedBWHi = _F3AccFlowPointGuaranteedBWHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 39),
    _F3AccFlowPointGuaranteedBWHi_Type()
)
f3AccFlowPointGuaranteedBWHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointGuaranteedBWHi.setStatus("current")
_F3AccFlowPointAutoBandwidthConfigEnabled_Type = TruthValue
_F3AccFlowPointAutoBandwidthConfigEnabled_Object = MibTableColumn
f3AccFlowPointAutoBandwidthConfigEnabled = _F3AccFlowPointAutoBandwidthConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 40),
    _F3AccFlowPointAutoBandwidthConfigEnabled_Type()
)
f3AccFlowPointAutoBandwidthConfigEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointAutoBandwidthConfigEnabled.setStatus("current")


class _F3AccFlowPointAutoCIRPercentage_Type(Integer32):
    """Custom type f3AccFlowPointAutoCIRPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_F3AccFlowPointAutoCIRPercentage_Type.__name__ = "Integer32"
_F3AccFlowPointAutoCIRPercentage_Object = MibTableColumn
f3AccFlowPointAutoCIRPercentage = _F3AccFlowPointAutoCIRPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 41),
    _F3AccFlowPointAutoCIRPercentage_Type()
)
f3AccFlowPointAutoCIRPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointAutoCIRPercentage.setStatus("current")
_F3AccFlowPointFrameFwdEnabled_Type = TruthValue
_F3AccFlowPointFrameFwdEnabled_Object = MibTableColumn
f3AccFlowPointFrameFwdEnabled = _F3AccFlowPointFrameFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 42),
    _F3AccFlowPointFrameFwdEnabled_Type()
)
f3AccFlowPointFrameFwdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointFrameFwdEnabled.setStatus("current")
_F3AccFlowPointStorageType_Type = StorageType
_F3AccFlowPointStorageType_Object = MibTableColumn
f3AccFlowPointStorageType = _F3AccFlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 43),
    _F3AccFlowPointStorageType_Type()
)
f3AccFlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointStorageType.setStatus("current")
_F3AccFlowPointRowStatus_Type = RowStatus
_F3AccFlowPointRowStatus_Object = MibTableColumn
f3AccFlowPointRowStatus = _F3AccFlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 44),
    _F3AccFlowPointRowStatus_Type()
)
f3AccFlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFlowPointRowStatus.setStatus("current")
_F3AccFlowPointUsePortPrioMapProfile_Type = TruthValue
_F3AccFlowPointUsePortPrioMapProfile_Object = MibTableColumn
f3AccFlowPointUsePortPrioMapProfile = _F3AccFlowPointUsePortPrioMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 45),
    _F3AccFlowPointUsePortPrioMapProfile_Type()
)
f3AccFlowPointUsePortPrioMapProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointUsePortPrioMapProfile.setStatus("current")
_F3AccFlowPointRefPrioMapProfile_Type = VariablePointer
_F3AccFlowPointRefPrioMapProfile_Object = MibTableColumn
f3AccFlowPointRefPrioMapProfile = _F3AccFlowPointRefPrioMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 46),
    _F3AccFlowPointRefPrioMapProfile_Type()
)
f3AccFlowPointRefPrioMapProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointRefPrioMapProfile.setStatus("current")
_F3AccFlowpointRefConnectGuardFlowObject_Type = VariablePointer
_F3AccFlowpointRefConnectGuardFlowObject_Object = MibTableColumn
f3AccFlowpointRefConnectGuardFlowObject = _F3AccFlowpointRefConnectGuardFlowObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 47),
    _F3AccFlowpointRefConnectGuardFlowObject_Type()
)
f3AccFlowpointRefConnectGuardFlowObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowpointRefConnectGuardFlowObject.setStatus("current")
_F3AccFlowpointSecureBlockingControl_Type = TruthValue
_F3AccFlowpointSecureBlockingControl_Object = MibTableColumn
f3AccFlowpointSecureBlockingControl = _F3AccFlowpointSecureBlockingControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 48),
    _F3AccFlowpointSecureBlockingControl_Type()
)
f3AccFlowpointSecureBlockingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowpointSecureBlockingControl.setStatus("current")
_F3AccFlowpointSecureState_Type = FlowSecState
_F3AccFlowpointSecureState_Object = MibTableColumn
f3AccFlowpointSecureState = _F3AccFlowpointSecureState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 1, 1, 49),
    _F3AccFlowpointSecureState_Type()
)
f3AccFlowpointSecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowpointSecureState.setStatus("current")
_F3AccFpQosShaperTable_Object = MibTable
f3AccFpQosShaperTable = _F3AccFpQosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2)
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperTable.setStatus("current")
_F3AccFpQosShaperEntry_Object = MibTableRow
f3AccFpQosShaperEntry = _F3AccFpQosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1)
)
f3AccFpQosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperIndex"),
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperEntry.setStatus("current")


class _F3AccFpQosShaperIndex_Type(Integer32):
    """Custom type f3AccFpQosShaperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_F3AccFpQosShaperIndex_Type.__name__ = "Integer32"
_F3AccFpQosShaperIndex_Object = MibTableColumn
f3AccFpQosShaperIndex = _F3AccFpQosShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 1),
    _F3AccFpQosShaperIndex_Type()
)
f3AccFpQosShaperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AccFpQosShaperIndex.setStatus("current")
_F3AccFpQosShaperAdminState_Type = AdminState
_F3AccFpQosShaperAdminState_Object = MibTableColumn
f3AccFpQosShaperAdminState = _F3AccFpQosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 2),
    _F3AccFpQosShaperAdminState_Type()
)
f3AccFpQosShaperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperAdminState.setStatus("current")
_F3AccFpQosShaperOperationalState_Type = OperationalState
_F3AccFpQosShaperOperationalState_Object = MibTableColumn
f3AccFpQosShaperOperationalState = _F3AccFpQosShaperOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 3),
    _F3AccFpQosShaperOperationalState_Type()
)
f3AccFpQosShaperOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperOperationalState.setStatus("current")
_F3AccFpQosShaperSecondaryState_Type = SecondaryState
_F3AccFpQosShaperSecondaryState_Object = MibTableColumn
f3AccFpQosShaperSecondaryState = _F3AccFpQosShaperSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 4),
    _F3AccFpQosShaperSecondaryState_Type()
)
f3AccFpQosShaperSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperSecondaryState.setStatus("current")
_F3AccFpQosShaperCIRLo_Type = Unsigned32
_F3AccFpQosShaperCIRLo_Object = MibTableColumn
f3AccFpQosShaperCIRLo = _F3AccFpQosShaperCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 5),
    _F3AccFpQosShaperCIRLo_Type()
)
f3AccFpQosShaperCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperCIRLo.setStatus("current")
_F3AccFpQosShaperCIRHi_Type = Unsigned32
_F3AccFpQosShaperCIRHi_Object = MibTableColumn
f3AccFpQosShaperCIRHi = _F3AccFpQosShaperCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 6),
    _F3AccFpQosShaperCIRHi_Type()
)
f3AccFpQosShaperCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperCIRHi.setStatus("current")
_F3AccFpQosShaperEIRLo_Type = Unsigned32
_F3AccFpQosShaperEIRLo_Object = MibTableColumn
f3AccFpQosShaperEIRLo = _F3AccFpQosShaperEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 7),
    _F3AccFpQosShaperEIRLo_Type()
)
f3AccFpQosShaperEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperEIRLo.setStatus("current")
_F3AccFpQosShaperEIRHi_Type = Unsigned32
_F3AccFpQosShaperEIRHi_Object = MibTableColumn
f3AccFpQosShaperEIRHi = _F3AccFpQosShaperEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 8),
    _F3AccFpQosShaperEIRHi_Type()
)
f3AccFpQosShaperEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperEIRHi.setStatus("current")
_F3AccFpQosShaperCBS_Type = Unsigned32
_F3AccFpQosShaperCBS_Object = MibTableColumn
f3AccFpQosShaperCBS = _F3AccFpQosShaperCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 9),
    _F3AccFpQosShaperCBS_Type()
)
f3AccFpQosShaperCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperCBS.setStatus("current")
_F3AccFpQosShaperEBS_Type = Unsigned32
_F3AccFpQosShaperEBS_Object = MibTableColumn
f3AccFpQosShaperEBS = _F3AccFpQosShaperEBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 10),
    _F3AccFpQosShaperEBS_Type()
)
f3AccFpQosShaperEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperEBS.setStatus("current")
_F3AccFpQosShaperBufferSize_Type = Unsigned32
_F3AccFpQosShaperBufferSize_Object = MibTableColumn
f3AccFpQosShaperBufferSize = _F3AccFpQosShaperBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 11),
    _F3AccFpQosShaperBufferSize_Type()
)
f3AccFpQosShaperBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperBufferSize.setStatus("current")


class _F3AccFpQosShaperCOS_Type(Integer32):
    """Custom type f3AccFpQosShaperCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3AccFpQosShaperCOS_Type.__name__ = "Integer32"
_F3AccFpQosShaperCOS_Object = MibTableColumn
f3AccFpQosShaperCOS = _F3AccFpQosShaperCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 12),
    _F3AccFpQosShaperCOS_Type()
)
f3AccFpQosShaperCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperCOS.setStatus("current")
_F3AccFpQosShaperStorageType_Type = StorageType
_F3AccFpQosShaperStorageType_Object = MibTableColumn
f3AccFpQosShaperStorageType = _F3AccFpQosShaperStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 13),
    _F3AccFpQosShaperStorageType_Type()
)
f3AccFpQosShaperStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStorageType.setStatus("current")
_F3AccFpQosShaperRowStatus_Type = RowStatus
_F3AccFpQosShaperRowStatus_Object = MibTableColumn
f3AccFpQosShaperRowStatus = _F3AccFpQosShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 2, 1, 14),
    _F3AccFpQosShaperRowStatus_Type()
)
f3AccFpQosShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosShaperRowStatus.setStatus("current")
_F3AccFpQosPolicerTable_Object = MibTable
f3AccFpQosPolicerTable = _F3AccFpQosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3)
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerTable.setStatus("current")
_F3AccFpQosPolicerEntry_Object = MibTableRow
f3AccFpQosPolicerEntry = _F3AccFpQosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1)
)
f3AccFpQosPolicerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerIndex"),
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerEntry.setStatus("current")


class _F3AccFpQosPolicerIndex_Type(Integer32):
    """Custom type f3AccFpQosPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_F3AccFpQosPolicerIndex_Type.__name__ = "Integer32"
_F3AccFpQosPolicerIndex_Object = MibTableColumn
f3AccFpQosPolicerIndex = _F3AccFpQosPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 1),
    _F3AccFpQosPolicerIndex_Type()
)
f3AccFpQosPolicerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerIndex.setStatus("current")
_F3AccFpQosPolicerAdminState_Type = AdminState
_F3AccFpQosPolicerAdminState_Object = MibTableColumn
f3AccFpQosPolicerAdminState = _F3AccFpQosPolicerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 2),
    _F3AccFpQosPolicerAdminState_Type()
)
f3AccFpQosPolicerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerAdminState.setStatus("current")
_F3AccFpQosPolicerOperationalState_Type = OperationalState
_F3AccFpQosPolicerOperationalState_Object = MibTableColumn
f3AccFpQosPolicerOperationalState = _F3AccFpQosPolicerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 3),
    _F3AccFpQosPolicerOperationalState_Type()
)
f3AccFpQosPolicerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerOperationalState.setStatus("current")
_F3AccFpQosPolicerSecondaryState_Type = SecondaryState
_F3AccFpQosPolicerSecondaryState_Object = MibTableColumn
f3AccFpQosPolicerSecondaryState = _F3AccFpQosPolicerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 4),
    _F3AccFpQosPolicerSecondaryState_Type()
)
f3AccFpQosPolicerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerSecondaryState.setStatus("current")
_F3AccFpQosPolicerCIRLo_Type = Unsigned32
_F3AccFpQosPolicerCIRLo_Object = MibTableColumn
f3AccFpQosPolicerCIRLo = _F3AccFpQosPolicerCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 5),
    _F3AccFpQosPolicerCIRLo_Type()
)
f3AccFpQosPolicerCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerCIRLo.setStatus("current")
_F3AccFpQosPolicerCIRHi_Type = Unsigned32
_F3AccFpQosPolicerCIRHi_Object = MibTableColumn
f3AccFpQosPolicerCIRHi = _F3AccFpQosPolicerCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 6),
    _F3AccFpQosPolicerCIRHi_Type()
)
f3AccFpQosPolicerCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerCIRHi.setStatus("current")
_F3AccFpQosPolicerEIRLo_Type = Unsigned32
_F3AccFpQosPolicerEIRLo_Object = MibTableColumn
f3AccFpQosPolicerEIRLo = _F3AccFpQosPolicerEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 7),
    _F3AccFpQosPolicerEIRLo_Type()
)
f3AccFpQosPolicerEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerEIRLo.setStatus("current")
_F3AccFpQosPolicerEIRHi_Type = Unsigned32
_F3AccFpQosPolicerEIRHi_Object = MibTableColumn
f3AccFpQosPolicerEIRHi = _F3AccFpQosPolicerEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 8),
    _F3AccFpQosPolicerEIRHi_Type()
)
f3AccFpQosPolicerEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerEIRHi.setStatus("current")
_F3AccFpQosPolicerCBS_Type = Integer32
_F3AccFpQosPolicerCBS_Object = MibTableColumn
f3AccFpQosPolicerCBS = _F3AccFpQosPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 9),
    _F3AccFpQosPolicerCBS_Type()
)
f3AccFpQosPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerCBS.setStatus("current")
_F3AccFpQosPolicerEBS_Type = Integer32
_F3AccFpQosPolicerEBS_Object = MibTableColumn
f3AccFpQosPolicerEBS = _F3AccFpQosPolicerEBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 10),
    _F3AccFpQosPolicerEBS_Type()
)
f3AccFpQosPolicerEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerEBS.setStatus("current")
_F3AccFpQosPolicerAlgorithm_Type = PolicerAlgorithmType
_F3AccFpQosPolicerAlgorithm_Object = MibTableColumn
f3AccFpQosPolicerAlgorithm = _F3AccFpQosPolicerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 11),
    _F3AccFpQosPolicerAlgorithm_Type()
)
f3AccFpQosPolicerAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerAlgorithm.setStatus("current")
_F3AccFpQosPolicerColorMode_Type = PolicerColorMode
_F3AccFpQosPolicerColorMode_Object = MibTableColumn
f3AccFpQosPolicerColorMode = _F3AccFpQosPolicerColorMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 12),
    _F3AccFpQosPolicerColorMode_Type()
)
f3AccFpQosPolicerColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerColorMode.setStatus("current")
_F3AccFpQosPolicerCouplingFlag_Type = TruthValue
_F3AccFpQosPolicerCouplingFlag_Object = MibTableColumn
f3AccFpQosPolicerCouplingFlag = _F3AccFpQosPolicerCouplingFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 13),
    _F3AccFpQosPolicerCouplingFlag_Type()
)
f3AccFpQosPolicerCouplingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerCouplingFlag.setStatus("current")
_F3AccFpQosPolicerPolicingEnabled_Type = TruthValue
_F3AccFpQosPolicerPolicingEnabled_Object = MibTableColumn
f3AccFpQosPolicerPolicingEnabled = _F3AccFpQosPolicerPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 14),
    _F3AccFpQosPolicerPolicingEnabled_Type()
)
f3AccFpQosPolicerPolicingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerPolicingEnabled.setStatus("current")
_F3AccFpQosPolicerStorageType_Type = StorageType
_F3AccFpQosPolicerStorageType_Object = MibTableColumn
f3AccFpQosPolicerStorageType = _F3AccFpQosPolicerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 15),
    _F3AccFpQosPolicerStorageType_Type()
)
f3AccFpQosPolicerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStorageType.setStatus("current")
_F3AccFpQosPolicerRowStatus_Type = RowStatus
_F3AccFpQosPolicerRowStatus_Object = MibTableColumn
f3AccFpQosPolicerRowStatus = _F3AccFpQosPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 3, 1, 16),
    _F3AccFpQosPolicerRowStatus_Type()
)
f3AccFpQosPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerRowStatus.setStatus("current")
_F3MPFlowExtTable_Object = MibTable
f3MPFlowExtTable = _F3MPFlowExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 4)
)
if mibBuilder.loadTexts:
    f3MPFlowExtTable.setStatus("current")
_F3MPFlowExtEntry_Object = MibTableRow
f3MPFlowExtEntry = _F3MPFlowExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 4, 1)
)
if mibBuilder.loadTexts:
    f3MPFlowExtEntry.setStatus("current")
_F3MPFlowExtMaxFwdEntries_Type = Integer32
_F3MPFlowExtMaxFwdEntries_Object = MibTableColumn
f3MPFlowExtMaxFwdEntries = _F3MPFlowExtMaxFwdEntries_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 4, 1, 1),
    _F3MPFlowExtMaxFwdEntries_Type()
)
f3MPFlowExtMaxFwdEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MPFlowExtMaxFwdEntries.setStatus("current")
_F3MPFlowRefConnectGuardFlowObject_Type = VariablePointer
_F3MPFlowRefConnectGuardFlowObject_Object = MibTableColumn
f3MPFlowRefConnectGuardFlowObject = _F3MPFlowRefConnectGuardFlowObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 4, 1, 2),
    _F3MPFlowRefConnectGuardFlowObject_Type()
)
f3MPFlowRefConnectGuardFlowObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MPFlowRefConnectGuardFlowObject.setStatus("current")
_F3MPFlowSecureState_Type = FlowSecState
_F3MPFlowSecureState_Object = MibTableColumn
f3MPFlowSecureState = _F3MPFlowSecureState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 4, 1, 3),
    _F3MPFlowSecureState_Type()
)
f3MPFlowSecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowSecureState.setStatus("current")
_F3AccFlowPointCpdV2Table_Object = MibTable
f3AccFlowPointCpdV2Table = _F3AccFlowPointCpdV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5)
)
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Table.setStatus("current")
_F3AccFlowPointCpdV2Entry_Object = MibTableRow
f3AccFlowPointCpdV2Entry = _F3AccFlowPointCpdV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1)
)
f3AccFlowPointCpdV2Entry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointCpdV2Index"),
)
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Entry.setStatus("current")
_F3AccFlowPointCpdV2Index_Type = Integer32
_F3AccFlowPointCpdV2Index_Object = MibTableColumn
f3AccFlowPointCpdV2Index = _F3AccFlowPointCpdV2Index_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 1),
    _F3AccFlowPointCpdV2Index_Type()
)
f3AccFlowPointCpdV2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Index.setStatus("current")
_F3AccFlowPointCpdV2IslDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2IslDispType_Object = MibTableColumn
f3AccFlowPointCpdV2IslDispType = _F3AccFlowPointCpdV2IslDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 2),
    _F3AccFlowPointCpdV2IslDispType_Type()
)
f3AccFlowPointCpdV2IslDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2IslDispType.setStatus("current")
_F3AccFlowPointCpdV2PagpDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2PagpDispType_Object = MibTableColumn
f3AccFlowPointCpdV2PagpDispType = _F3AccFlowPointCpdV2PagpDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 3),
    _F3AccFlowPointCpdV2PagpDispType_Type()
)
f3AccFlowPointCpdV2PagpDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2PagpDispType.setStatus("current")
_F3AccFlowPointCpdV2UdldDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2UdldDispType_Object = MibTableColumn
f3AccFlowPointCpdV2UdldDispType = _F3AccFlowPointCpdV2UdldDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 4),
    _F3AccFlowPointCpdV2UdldDispType_Type()
)
f3AccFlowPointCpdV2UdldDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2UdldDispType.setStatus("current")
_F3AccFlowPointCpdV2CdpDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2CdpDispType_Object = MibTableColumn
f3AccFlowPointCpdV2CdpDispType = _F3AccFlowPointCpdV2CdpDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 5),
    _F3AccFlowPointCpdV2CdpDispType_Type()
)
f3AccFlowPointCpdV2CdpDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2CdpDispType.setStatus("current")
_F3AccFlowPointCpdV2VtpDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2VtpDispType_Object = MibTableColumn
f3AccFlowPointCpdV2VtpDispType = _F3AccFlowPointCpdV2VtpDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 6),
    _F3AccFlowPointCpdV2VtpDispType_Type()
)
f3AccFlowPointCpdV2VtpDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2VtpDispType.setStatus("current")
_F3AccFlowPointCpdV2DtpDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2DtpDispType_Object = MibTableColumn
f3AccFlowPointCpdV2DtpDispType = _F3AccFlowPointCpdV2DtpDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 7),
    _F3AccFlowPointCpdV2DtpDispType_Type()
)
f3AccFlowPointCpdV2DtpDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2DtpDispType.setStatus("current")
_F3AccFlowPointCpdV2PvstpPlusDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2PvstpPlusDispType_Object = MibTableColumn
f3AccFlowPointCpdV2PvstpPlusDispType = _F3AccFlowPointCpdV2PvstpPlusDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 8),
    _F3AccFlowPointCpdV2PvstpPlusDispType_Type()
)
f3AccFlowPointCpdV2PvstpPlusDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2PvstpPlusDispType.setStatus("current")
_F3AccFlowPointCpdV2UplinkFastDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2UplinkFastDispType_Object = MibTableColumn
f3AccFlowPointCpdV2UplinkFastDispType = _F3AccFlowPointCpdV2UplinkFastDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 9),
    _F3AccFlowPointCpdV2UplinkFastDispType_Type()
)
f3AccFlowPointCpdV2UplinkFastDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2UplinkFastDispType.setStatus("current")
_F3AccFlowPointCpdV2VlanBridgeDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2VlanBridgeDispType_Object = MibTableColumn
f3AccFlowPointCpdV2VlanBridgeDispType = _F3AccFlowPointCpdV2VlanBridgeDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 10),
    _F3AccFlowPointCpdV2VlanBridgeDispType_Type()
)
f3AccFlowPointCpdV2VlanBridgeDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2VlanBridgeDispType.setStatus("current")
_F3AccFlowPointCpdV2L2PTDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2L2PTDispType_Object = MibTableColumn
f3AccFlowPointCpdV2L2PTDispType = _F3AccFlowPointCpdV2L2PTDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 11),
    _F3AccFlowPointCpdV2L2PTDispType_Type()
)
f3AccFlowPointCpdV2L2PTDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2L2PTDispType.setStatus("current")
_F3AccFlowPointCpdV2BPDUDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2BPDUDispType_Object = MibTableColumn
f3AccFlowPointCpdV2BPDUDispType = _F3AccFlowPointCpdV2BPDUDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 12),
    _F3AccFlowPointCpdV2BPDUDispType_Type()
)
f3AccFlowPointCpdV2BPDUDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2BPDUDispType.setStatus("current")
_F3AccFlowPointCpdV2PauseDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2PauseDispType_Object = MibTableColumn
f3AccFlowPointCpdV2PauseDispType = _F3AccFlowPointCpdV2PauseDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 13),
    _F3AccFlowPointCpdV2PauseDispType_Type()
)
f3AccFlowPointCpdV2PauseDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2PauseDispType.setStatus("current")
_F3AccFlowPointCpdV2LACPDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2LACPDispType_Object = MibTableColumn
f3AccFlowPointCpdV2LACPDispType = _F3AccFlowPointCpdV2LACPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 14),
    _F3AccFlowPointCpdV2LACPDispType_Type()
)
f3AccFlowPointCpdV2LACPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2LACPDispType.setStatus("current")
_F3AccFlowPointCpdV2LACPMarkerDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2LACPMarkerDispType_Object = MibTableColumn
f3AccFlowPointCpdV2LACPMarkerDispType = _F3AccFlowPointCpdV2LACPMarkerDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 15),
    _F3AccFlowPointCpdV2LACPMarkerDispType_Type()
)
f3AccFlowPointCpdV2LACPMarkerDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2LACPMarkerDispType.setStatus("current")
_F3AccFlowPointCpdV2EfmOamDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2EfmOamDispType_Object = MibTableColumn
f3AccFlowPointCpdV2EfmOamDispType = _F3AccFlowPointCpdV2EfmOamDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 16),
    _F3AccFlowPointCpdV2EfmOamDispType_Type()
)
f3AccFlowPointCpdV2EfmOamDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2EfmOamDispType.setStatus("current")
_F3AccFlowPointCpdV2SSMDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2SSMDispType_Object = MibTableColumn
f3AccFlowPointCpdV2SSMDispType = _F3AccFlowPointCpdV2SSMDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 17),
    _F3AccFlowPointCpdV2SSMDispType_Type()
)
f3AccFlowPointCpdV2SSMDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2SSMDispType.setStatus("current")
_F3AccFlowPointCpdV2PortAuthenDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2PortAuthenDispType_Object = MibTableColumn
f3AccFlowPointCpdV2PortAuthenDispType = _F3AccFlowPointCpdV2PortAuthenDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 18),
    _F3AccFlowPointCpdV2PortAuthenDispType_Type()
)
f3AccFlowPointCpdV2PortAuthenDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2PortAuthenDispType.setStatus("current")
_F3AccFlowPointCpdV2LANBridgesDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2LANBridgesDispType_Object = MibTableColumn
f3AccFlowPointCpdV2LANBridgesDispType = _F3AccFlowPointCpdV2LANBridgesDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 19),
    _F3AccFlowPointCpdV2LANBridgesDispType_Type()
)
f3AccFlowPointCpdV2LANBridgesDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2LANBridgesDispType.setStatus("current")
_F3AccFlowPointCpdV2GMRPDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2GMRPDispType_Object = MibTableColumn
f3AccFlowPointCpdV2GMRPDispType = _F3AccFlowPointCpdV2GMRPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 20),
    _F3AccFlowPointCpdV2GMRPDispType_Type()
)
f3AccFlowPointCpdV2GMRPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2GMRPDispType.setStatus("current")
_F3AccFlowPointCpdV2GVRPDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2GVRPDispType_Object = MibTableColumn
f3AccFlowPointCpdV2GVRPDispType = _F3AccFlowPointCpdV2GVRPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 21),
    _F3AccFlowPointCpdV2GVRPDispType_Type()
)
f3AccFlowPointCpdV2GVRPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2GVRPDispType.setStatus("current")
_F3AccFlowPointCpdV2GARPDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2GARPDispType_Object = MibTableColumn
f3AccFlowPointCpdV2GARPDispType = _F3AccFlowPointCpdV2GARPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 22),
    _F3AccFlowPointCpdV2GARPDispType_Type()
)
f3AccFlowPointCpdV2GARPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2GARPDispType.setStatus("current")
_F3AccFlowPointCpdV2ActiveControlProtocols_Type = CmActiveControlProtocolsType
_F3AccFlowPointCpdV2ActiveControlProtocols_Object = MibTableColumn
f3AccFlowPointCpdV2ActiveControlProtocols = _F3AccFlowPointCpdV2ActiveControlProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 23),
    _F3AccFlowPointCpdV2ActiveControlProtocols_Type()
)
f3AccFlowPointCpdV2ActiveControlProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2ActiveControlProtocols.setStatus("current")
_F3AccFlowPointCpdV2ELMIDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2ELMIDispType_Object = MibTableColumn
f3AccFlowPointCpdV2ELMIDispType = _F3AccFlowPointCpdV2ELMIDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 24),
    _F3AccFlowPointCpdV2ELMIDispType_Type()
)
f3AccFlowPointCpdV2ELMIDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2ELMIDispType.setStatus("current")
_F3AccFlowPointCpdV2Mac00DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac00DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac00DispType = _F3AccFlowPointCpdV2Mac00DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 25),
    _F3AccFlowPointCpdV2Mac00DispType_Type()
)
f3AccFlowPointCpdV2Mac00DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac00DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac01DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac01DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac01DispType = _F3AccFlowPointCpdV2Mac01DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 26),
    _F3AccFlowPointCpdV2Mac01DispType_Type()
)
f3AccFlowPointCpdV2Mac01DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac01DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac02DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac02DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac02DispType = _F3AccFlowPointCpdV2Mac02DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 27),
    _F3AccFlowPointCpdV2Mac02DispType_Type()
)
f3AccFlowPointCpdV2Mac02DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac02DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac03DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac03DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac03DispType = _F3AccFlowPointCpdV2Mac03DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 28),
    _F3AccFlowPointCpdV2Mac03DispType_Type()
)
f3AccFlowPointCpdV2Mac03DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac03DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac04DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac04DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac04DispType = _F3AccFlowPointCpdV2Mac04DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 29),
    _F3AccFlowPointCpdV2Mac04DispType_Type()
)
f3AccFlowPointCpdV2Mac04DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac04DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac05DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac05DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac05DispType = _F3AccFlowPointCpdV2Mac05DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 30),
    _F3AccFlowPointCpdV2Mac05DispType_Type()
)
f3AccFlowPointCpdV2Mac05DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac05DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac06DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac06DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac06DispType = _F3AccFlowPointCpdV2Mac06DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 31),
    _F3AccFlowPointCpdV2Mac06DispType_Type()
)
f3AccFlowPointCpdV2Mac06DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac06DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac07DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac07DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac07DispType = _F3AccFlowPointCpdV2Mac07DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 32),
    _F3AccFlowPointCpdV2Mac07DispType_Type()
)
f3AccFlowPointCpdV2Mac07DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac07DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac08DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac08DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac08DispType = _F3AccFlowPointCpdV2Mac08DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 33),
    _F3AccFlowPointCpdV2Mac08DispType_Type()
)
f3AccFlowPointCpdV2Mac08DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac08DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac09DispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac09DispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac09DispType = _F3AccFlowPointCpdV2Mac09DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 34),
    _F3AccFlowPointCpdV2Mac09DispType_Type()
)
f3AccFlowPointCpdV2Mac09DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac09DispType.setStatus("current")
_F3AccFlowPointCpdV2Mac0ADispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac0ADispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac0ADispType = _F3AccFlowPointCpdV2Mac0ADispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 35),
    _F3AccFlowPointCpdV2Mac0ADispType_Type()
)
f3AccFlowPointCpdV2Mac0ADispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac0ADispType.setStatus("current")
_F3AccFlowPointCpdV2Mac0BDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac0BDispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac0BDispType = _F3AccFlowPointCpdV2Mac0BDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 36),
    _F3AccFlowPointCpdV2Mac0BDispType_Type()
)
f3AccFlowPointCpdV2Mac0BDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac0BDispType.setStatus("current")
_F3AccFlowPointCpdV2Mac0CDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac0CDispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac0CDispType = _F3AccFlowPointCpdV2Mac0CDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 37),
    _F3AccFlowPointCpdV2Mac0CDispType_Type()
)
f3AccFlowPointCpdV2Mac0CDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac0CDispType.setStatus("current")
_F3AccFlowPointCpdV2Mac0DDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac0DDispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac0DDispType = _F3AccFlowPointCpdV2Mac0DDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 38),
    _F3AccFlowPointCpdV2Mac0DDispType_Type()
)
f3AccFlowPointCpdV2Mac0DDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac0DDispType.setStatus("current")
_F3AccFlowPointCpdV2Mac0EDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac0EDispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac0EDispType = _F3AccFlowPointCpdV2Mac0EDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 39),
    _F3AccFlowPointCpdV2Mac0EDispType_Type()
)
f3AccFlowPointCpdV2Mac0EDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac0EDispType.setStatus("current")
_F3AccFlowPointCpdV2Mac0FDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2Mac0FDispType_Object = MibTableColumn
f3AccFlowPointCpdV2Mac0FDispType = _F3AccFlowPointCpdV2Mac0FDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 40),
    _F3AccFlowPointCpdV2Mac0FDispType_Type()
)
f3AccFlowPointCpdV2Mac0FDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Mac0FDispType.setStatus("current")
_F3AccFlowPointCpdV2NearestLLDPDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2NearestLLDPDispType_Object = MibTableColumn
f3AccFlowPointCpdV2NearestLLDPDispType = _F3AccFlowPointCpdV2NearestLLDPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 41),
    _F3AccFlowPointCpdV2NearestLLDPDispType_Type()
)
f3AccFlowPointCpdV2NearestLLDPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2NearestLLDPDispType.setStatus("current")
_F3AccFlowPointCpdV2NonTpmrLLDPDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2NonTpmrLLDPDispType_Object = MibTableColumn
f3AccFlowPointCpdV2NonTpmrLLDPDispType = _F3AccFlowPointCpdV2NonTpmrLLDPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 42),
    _F3AccFlowPointCpdV2NonTpmrLLDPDispType_Type()
)
f3AccFlowPointCpdV2NonTpmrLLDPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2NonTpmrLLDPDispType.setStatus("current")
_F3AccFlowPointCpdV2CustomerLLDPDispType_Type = CmControlProtocolDispType
_F3AccFlowPointCpdV2CustomerLLDPDispType_Object = MibTableColumn
f3AccFlowPointCpdV2CustomerLLDPDispType = _F3AccFlowPointCpdV2CustomerLLDPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 5, 1, 43),
    _F3AccFlowPointCpdV2CustomerLLDPDispType_Type()
)
f3AccFlowPointCpdV2CustomerLLDPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2CustomerLLDPDispType.setStatus("current")
_F3AccFlowPointLearningConfigTable_Object = MibTable
f3AccFlowPointLearningConfigTable = _F3AccFlowPointLearningConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 6)
)
if mibBuilder.loadTexts:
    f3AccFlowPointLearningConfigTable.setStatus("current")
_F3AccFlowPointLearningConfigEntry_Object = MibTableRow
f3AccFlowPointLearningConfigEntry = _F3AccFlowPointLearningConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 6, 1)
)
if mibBuilder.loadTexts:
    f3AccFlowPointLearningConfigEntry.setStatus("current")
_F3AccFlowPointLearningConfigLearningEnabled_Type = TruthValue
_F3AccFlowPointLearningConfigLearningEnabled_Object = MibTableColumn
f3AccFlowPointLearningConfigLearningEnabled = _F3AccFlowPointLearningConfigLearningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 6, 1, 1),
    _F3AccFlowPointLearningConfigLearningEnabled_Type()
)
f3AccFlowPointLearningConfigLearningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointLearningConfigLearningEnabled.setStatus("current")
_F3AccFlowPointLearningConfigMaxFwdEntries_Type = Integer32
_F3AccFlowPointLearningConfigMaxFwdEntries_Object = MibTableColumn
f3AccFlowPointLearningConfigMaxFwdEntries = _F3AccFlowPointLearningConfigMaxFwdEntries_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 6, 1, 2),
    _F3AccFlowPointLearningConfigMaxFwdEntries_Type()
)
f3AccFlowPointLearningConfigMaxFwdEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointLearningConfigMaxFwdEntries.setStatus("current")
_F3AccFlowPointLearningConfigProtectLearningCtrl_Type = ProtectLearningControl
_F3AccFlowPointLearningConfigProtectLearningCtrl_Object = MibTableColumn
f3AccFlowPointLearningConfigProtectLearningCtrl = _F3AccFlowPointLearningConfigProtectLearningCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 6, 1, 3),
    _F3AccFlowPointLearningConfigProtectLearningCtrl_Type()
)
f3AccFlowPointLearningConfigProtectLearningCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointLearningConfigProtectLearningCtrl.setStatus("current")
_F3AccFlowPointLearningConfigAction_Type = FlowLearningConfigAction
_F3AccFlowPointLearningConfigAction_Object = MibTableColumn
f3AccFlowPointLearningConfigAction = _F3AccFlowPointLearningConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 6, 1, 4),
    _F3AccFlowPointLearningConfigAction_Type()
)
f3AccFlowPointLearningConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointLearningConfigAction.setStatus("current")
_F3NetFlowPointTable_Object = MibTable
f3NetFlowPointTable = _F3NetFlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7)
)
if mibBuilder.loadTexts:
    f3NetFlowPointTable.setStatus("current")
_F3NetFlowPointEntry_Object = MibTableRow
f3NetFlowPointEntry = _F3NetFlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1)
)
f3NetFlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3NetFlowPointEntry.setStatus("current")


class _F3NetFlowPointIndex_Type(Integer32):
    """Custom type f3NetFlowPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFlowPointIndex_Type.__name__ = "Integer32"
_F3NetFlowPointIndex_Object = MibTableColumn
f3NetFlowPointIndex = _F3NetFlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 1),
    _F3NetFlowPointIndex_Type()
)
f3NetFlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NetFlowPointIndex.setStatus("current")


class _F3NetFlowPointAlias_Type(DisplayString):
    """Custom type f3NetFlowPointAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3NetFlowPointAlias_Type.__name__ = "DisplayString"
_F3NetFlowPointAlias_Object = MibTableColumn
f3NetFlowPointAlias = _F3NetFlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 2),
    _F3NetFlowPointAlias_Type()
)
f3NetFlowPointAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointAlias.setStatus("current")
_F3NetFlowPointAdminState_Type = AdminState
_F3NetFlowPointAdminState_Object = MibTableColumn
f3NetFlowPointAdminState = _F3NetFlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 3),
    _F3NetFlowPointAdminState_Type()
)
f3NetFlowPointAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointAdminState.setStatus("current")
_F3NetFlowPointOperationalState_Type = OperationalState
_F3NetFlowPointOperationalState_Object = MibTableColumn
f3NetFlowPointOperationalState = _F3NetFlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 4),
    _F3NetFlowPointOperationalState_Type()
)
f3NetFlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointOperationalState.setStatus("current")
_F3NetFlowPointSecondaryState_Type = SecondaryState
_F3NetFlowPointSecondaryState_Object = MibTableColumn
f3NetFlowPointSecondaryState = _F3NetFlowPointSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 5),
    _F3NetFlowPointSecondaryState_Type()
)
f3NetFlowPointSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointSecondaryState.setStatus("current")
_F3NetFlowPointAssociatedFlowId_Type = VariablePointer
_F3NetFlowPointAssociatedFlowId_Object = MibTableColumn
f3NetFlowPointAssociatedFlowId = _F3NetFlowPointAssociatedFlowId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 6),
    _F3NetFlowPointAssociatedFlowId_Type()
)
f3NetFlowPointAssociatedFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointAssociatedFlowId.setStatus("current")
_F3NetFlowPointIngressMultiCOSEnabled_Type = TruthValue
_F3NetFlowPointIngressMultiCOSEnabled_Object = MibTableColumn
f3NetFlowPointIngressMultiCOSEnabled = _F3NetFlowPointIngressMultiCOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 7),
    _F3NetFlowPointIngressMultiCOSEnabled_Type()
)
f3NetFlowPointIngressMultiCOSEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointIngressMultiCOSEnabled.setStatus("current")
_F3NetFlowPointIngressCOS_Type = Integer32
_F3NetFlowPointIngressCOS_Object = MibTableColumn
f3NetFlowPointIngressCOS = _F3NetFlowPointIngressCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 8),
    _F3NetFlowPointIngressCOS_Type()
)
f3NetFlowPointIngressCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointIngressCOS.setStatus("deprecated")
_F3NetFlowPointEgressShapingType_Type = ShapingType
_F3NetFlowPointEgressShapingType_Object = MibTableColumn
f3NetFlowPointEgressShapingType = _F3NetFlowPointEgressShapingType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 9),
    _F3NetFlowPointEgressShapingType_Type()
)
f3NetFlowPointEgressShapingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointEgressShapingType.setStatus("current")


class _F3NetFlowPointIngressVlanMemberList_Type(DisplayString):
    """Custom type f3NetFlowPointIngressVlanMemberList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_F3NetFlowPointIngressVlanMemberList_Type.__name__ = "DisplayString"
_F3NetFlowPointIngressVlanMemberList_Object = MibTableColumn
f3NetFlowPointIngressVlanMemberList = _F3NetFlowPointIngressVlanMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 10),
    _F3NetFlowPointIngressVlanMemberList_Type()
)
f3NetFlowPointIngressVlanMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointIngressVlanMemberList.setStatus("current")
_F3NetFlowPointVlanMemberAction_Type = FlowVlanActionType
_F3NetFlowPointVlanMemberAction_Object = MibTableColumn
f3NetFlowPointVlanMemberAction = _F3NetFlowPointVlanMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 11),
    _F3NetFlowPointVlanMemberAction_Type()
)
f3NetFlowPointVlanMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointVlanMemberAction.setStatus("current")


class _F3NetFlowPointVlanMemberActionVlan_Type(DisplayString):
    """Custom type f3NetFlowPointVlanMemberActionVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_F3NetFlowPointVlanMemberActionVlan_Type.__name__ = "DisplayString"
_F3NetFlowPointVlanMemberActionVlan_Object = MibTableColumn
f3NetFlowPointVlanMemberActionVlan = _F3NetFlowPointVlanMemberActionVlan_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 12),
    _F3NetFlowPointVlanMemberActionVlan_Type()
)
f3NetFlowPointVlanMemberActionVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointVlanMemberActionVlan.setStatus("current")
_F3NetFlowPointIngressUntaggedFrameEnabled_Type = TruthValue
_F3NetFlowPointIngressUntaggedFrameEnabled_Object = MibTableColumn
f3NetFlowPointIngressUntaggedFrameEnabled = _F3NetFlowPointIngressUntaggedFrameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 13),
    _F3NetFlowPointIngressUntaggedFrameEnabled_Type()
)
f3NetFlowPointIngressUntaggedFrameEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointIngressUntaggedFrameEnabled.setStatus("current")
_F3NetFlowPointCTagControl_Type = FlowTagControl
_F3NetFlowPointCTagControl_Object = MibTableColumn
f3NetFlowPointCTagControl = _F3NetFlowPointCTagControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 14),
    _F3NetFlowPointCTagControl_Type()
)
f3NetFlowPointCTagControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointCTagControl.setStatus("current")
_F3NetFlowPointCTagVlanId_Type = VlanId
_F3NetFlowPointCTagVlanId_Object = MibTableColumn
f3NetFlowPointCTagVlanId = _F3NetFlowPointCTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 15),
    _F3NetFlowPointCTagVlanId_Type()
)
f3NetFlowPointCTagVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointCTagVlanId.setStatus("current")
_F3NetFlowPointCTagVlanPriority_Type = VlanPriority
_F3NetFlowPointCTagVlanPriority_Object = MibTableColumn
f3NetFlowPointCTagVlanPriority = _F3NetFlowPointCTagVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 16),
    _F3NetFlowPointCTagVlanPriority_Type()
)
f3NetFlowPointCTagVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointCTagVlanPriority.setStatus("current")
_F3NetFlowPointSTagControl_Type = FlowTagControl
_F3NetFlowPointSTagControl_Object = MibTableColumn
f3NetFlowPointSTagControl = _F3NetFlowPointSTagControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 17),
    _F3NetFlowPointSTagControl_Type()
)
f3NetFlowPointSTagControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointSTagControl.setStatus("current")
_F3NetFlowPointSTagVlanId_Type = VlanId
_F3NetFlowPointSTagVlanId_Object = MibTableColumn
f3NetFlowPointSTagVlanId = _F3NetFlowPointSTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 18),
    _F3NetFlowPointSTagVlanId_Type()
)
f3NetFlowPointSTagVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointSTagVlanId.setStatus("current")
_F3NetFlowPointSTagVlanPriority_Type = VlanPriority
_F3NetFlowPointSTagVlanPriority_Object = MibTableColumn
f3NetFlowPointSTagVlanPriority = _F3NetFlowPointSTagVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 19),
    _F3NetFlowPointSTagVlanPriority_Type()
)
f3NetFlowPointSTagVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointSTagVlanPriority.setStatus("current")
_F3NetFlowPointEgressOuterTagPrioMapEnabled_Type = TruthValue
_F3NetFlowPointEgressOuterTagPrioMapEnabled_Object = MibTableColumn
f3NetFlowPointEgressOuterTagPrioMapEnabled = _F3NetFlowPointEgressOuterTagPrioMapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 20),
    _F3NetFlowPointEgressOuterTagPrioMapEnabled_Type()
)
f3NetFlowPointEgressOuterTagPrioMapEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointEgressOuterTagPrioMapEnabled.setStatus("current")
_F3NetFlowPointEgressInnerTagPrioMapEnabled_Type = TruthValue
_F3NetFlowPointEgressInnerTagPrioMapEnabled_Object = MibTableColumn
f3NetFlowPointEgressInnerTagPrioMapEnabled = _F3NetFlowPointEgressInnerTagPrioMapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 21),
    _F3NetFlowPointEgressInnerTagPrioMapEnabled_Type()
)
f3NetFlowPointEgressInnerTagPrioMapEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointEgressInnerTagPrioMapEnabled.setStatus("current")


class _F3NetFlowPointSESFramesLossThresholdRatio_Type(Integer32):
    """Custom type f3NetFlowPointSESFramesLossThresholdRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_F3NetFlowPointSESFramesLossThresholdRatio_Type.__name__ = "Integer32"
_F3NetFlowPointSESFramesLossThresholdRatio_Object = MibTableColumn
f3NetFlowPointSESFramesLossThresholdRatio = _F3NetFlowPointSESFramesLossThresholdRatio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 22),
    _F3NetFlowPointSESFramesLossThresholdRatio_Type()
)
f3NetFlowPointSESFramesLossThresholdRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointSESFramesLossThresholdRatio.setStatus("current")
_F3NetFlowPointDefaultMemberEnabled_Type = TruthValue
_F3NetFlowPointDefaultMemberEnabled_Object = MibTableColumn
f3NetFlowPointDefaultMemberEnabled = _F3NetFlowPointDefaultMemberEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 23),
    _F3NetFlowPointDefaultMemberEnabled_Type()
)
f3NetFlowPointDefaultMemberEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointDefaultMemberEnabled.setStatus("current")
_F3NetFlowPointMcastRateLimitEnabled_Type = TruthValue
_F3NetFlowPointMcastRateLimitEnabled_Object = MibTableColumn
f3NetFlowPointMcastRateLimitEnabled = _F3NetFlowPointMcastRateLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 24),
    _F3NetFlowPointMcastRateLimitEnabled_Type()
)
f3NetFlowPointMcastRateLimitEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointMcastRateLimitEnabled.setStatus("current")
_F3NetFlowPointMcastRateLimitSpeedLo_Type = Unsigned32
_F3NetFlowPointMcastRateLimitSpeedLo_Object = MibTableColumn
f3NetFlowPointMcastRateLimitSpeedLo = _F3NetFlowPointMcastRateLimitSpeedLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 25),
    _F3NetFlowPointMcastRateLimitSpeedLo_Type()
)
f3NetFlowPointMcastRateLimitSpeedLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointMcastRateLimitSpeedLo.setStatus("current")
_F3NetFlowPointMcastRateLimitSpeedHi_Type = Unsigned32
_F3NetFlowPointMcastRateLimitSpeedHi_Object = MibTableColumn
f3NetFlowPointMcastRateLimitSpeedHi = _F3NetFlowPointMcastRateLimitSpeedHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 26),
    _F3NetFlowPointMcastRateLimitSpeedHi_Type()
)
f3NetFlowPointMcastRateLimitSpeedHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointMcastRateLimitSpeedHi.setStatus("current")
_F3NetFlowPointBcastRateLimitEnabled_Type = TruthValue
_F3NetFlowPointBcastRateLimitEnabled_Object = MibTableColumn
f3NetFlowPointBcastRateLimitEnabled = _F3NetFlowPointBcastRateLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 27),
    _F3NetFlowPointBcastRateLimitEnabled_Type()
)
f3NetFlowPointBcastRateLimitEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointBcastRateLimitEnabled.setStatus("current")
_F3NetFlowPointBcastRateLimitSpeedLo_Type = Unsigned32
_F3NetFlowPointBcastRateLimitSpeedLo_Object = MibTableColumn
f3NetFlowPointBcastRateLimitSpeedLo = _F3NetFlowPointBcastRateLimitSpeedLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 28),
    _F3NetFlowPointBcastRateLimitSpeedLo_Type()
)
f3NetFlowPointBcastRateLimitSpeedLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointBcastRateLimitSpeedLo.setStatus("current")
_F3NetFlowPointBcastRateLimitSpeedHi_Type = Unsigned32
_F3NetFlowPointBcastRateLimitSpeedHi_Object = MibTableColumn
f3NetFlowPointBcastRateLimitSpeedHi = _F3NetFlowPointBcastRateLimitSpeedHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 29),
    _F3NetFlowPointBcastRateLimitSpeedHi_Type()
)
f3NetFlowPointBcastRateLimitSpeedHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointBcastRateLimitSpeedHi.setStatus("current")
_F3NetFlowPointCombinedRateLimitEnabled_Type = TruthValue
_F3NetFlowPointCombinedRateLimitEnabled_Object = MibTableColumn
f3NetFlowPointCombinedRateLimitEnabled = _F3NetFlowPointCombinedRateLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 30),
    _F3NetFlowPointCombinedRateLimitEnabled_Type()
)
f3NetFlowPointCombinedRateLimitEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointCombinedRateLimitEnabled.setStatus("current")
_F3NetFlowPointCombinedRateLimitSpeedLo_Type = Unsigned32
_F3NetFlowPointCombinedRateLimitSpeedLo_Object = MibTableColumn
f3NetFlowPointCombinedRateLimitSpeedLo = _F3NetFlowPointCombinedRateLimitSpeedLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 31),
    _F3NetFlowPointCombinedRateLimitSpeedLo_Type()
)
f3NetFlowPointCombinedRateLimitSpeedLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointCombinedRateLimitSpeedLo.setStatus("current")
_F3NetFlowPointCombinedRateLimitSpeedHi_Type = Unsigned32
_F3NetFlowPointCombinedRateLimitSpeedHi_Object = MibTableColumn
f3NetFlowPointCombinedRateLimitSpeedHi = _F3NetFlowPointCombinedRateLimitSpeedHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 32),
    _F3NetFlowPointCombinedRateLimitSpeedHi_Type()
)
f3NetFlowPointCombinedRateLimitSpeedHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointCombinedRateLimitSpeedHi.setStatus("current")
_F3NetFlowPointSplitHorizonGroupOID_Type = VariablePointer
_F3NetFlowPointSplitHorizonGroupOID_Object = MibTableColumn
f3NetFlowPointSplitHorizonGroupOID = _F3NetFlowPointSplitHorizonGroupOID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 33),
    _F3NetFlowPointSplitHorizonGroupOID_Type()
)
f3NetFlowPointSplitHorizonGroupOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointSplitHorizonGroupOID.setStatus("current")
_F3NetFlowPointLoopAvoidance_Type = VariablePointer
_F3NetFlowPointLoopAvoidance_Object = MibTableColumn
f3NetFlowPointLoopAvoidance = _F3NetFlowPointLoopAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 34),
    _F3NetFlowPointLoopAvoidance_Type()
)
f3NetFlowPointLoopAvoidance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointLoopAvoidance.setStatus("current")
_F3NetFlowPointHierarchicalCOSEnabled_Type = TruthValue
_F3NetFlowPointHierarchicalCOSEnabled_Object = MibTableColumn
f3NetFlowPointHierarchicalCOSEnabled = _F3NetFlowPointHierarchicalCOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 35),
    _F3NetFlowPointHierarchicalCOSEnabled_Type()
)
f3NetFlowPointHierarchicalCOSEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointHierarchicalCOSEnabled.setStatus("current")
_F3NetFlowPointMaximumBWLo_Type = Unsigned32
_F3NetFlowPointMaximumBWLo_Object = MibTableColumn
f3NetFlowPointMaximumBWLo = _F3NetFlowPointMaximumBWLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 36),
    _F3NetFlowPointMaximumBWLo_Type()
)
f3NetFlowPointMaximumBWLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointMaximumBWLo.setStatus("current")
_F3NetFlowPointMaximumBWHi_Type = Unsigned32
_F3NetFlowPointMaximumBWHi_Object = MibTableColumn
f3NetFlowPointMaximumBWHi = _F3NetFlowPointMaximumBWHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 37),
    _F3NetFlowPointMaximumBWHi_Type()
)
f3NetFlowPointMaximumBWHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointMaximumBWHi.setStatus("current")
_F3NetFlowPointGuaranteedBWLo_Type = Unsigned32
_F3NetFlowPointGuaranteedBWLo_Object = MibTableColumn
f3NetFlowPointGuaranteedBWLo = _F3NetFlowPointGuaranteedBWLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 38),
    _F3NetFlowPointGuaranteedBWLo_Type()
)
f3NetFlowPointGuaranteedBWLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointGuaranteedBWLo.setStatus("current")
_F3NetFlowPointGuaranteedBWHi_Type = Unsigned32
_F3NetFlowPointGuaranteedBWHi_Object = MibTableColumn
f3NetFlowPointGuaranteedBWHi = _F3NetFlowPointGuaranteedBWHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 39),
    _F3NetFlowPointGuaranteedBWHi_Type()
)
f3NetFlowPointGuaranteedBWHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointGuaranteedBWHi.setStatus("current")
_F3NetFlowPointAutoBandwidthConfigEnabled_Type = TruthValue
_F3NetFlowPointAutoBandwidthConfigEnabled_Object = MibTableColumn
f3NetFlowPointAutoBandwidthConfigEnabled = _F3NetFlowPointAutoBandwidthConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 40),
    _F3NetFlowPointAutoBandwidthConfigEnabled_Type()
)
f3NetFlowPointAutoBandwidthConfigEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointAutoBandwidthConfigEnabled.setStatus("current")


class _F3NetFlowPointAutoCIRPercentage_Type(Integer32):
    """Custom type f3NetFlowPointAutoCIRPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_F3NetFlowPointAutoCIRPercentage_Type.__name__ = "Integer32"
_F3NetFlowPointAutoCIRPercentage_Object = MibTableColumn
f3NetFlowPointAutoCIRPercentage = _F3NetFlowPointAutoCIRPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 41),
    _F3NetFlowPointAutoCIRPercentage_Type()
)
f3NetFlowPointAutoCIRPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointAutoCIRPercentage.setStatus("current")
_F3NetFlowPointFrameFwdEnabled_Type = TruthValue
_F3NetFlowPointFrameFwdEnabled_Object = MibTableColumn
f3NetFlowPointFrameFwdEnabled = _F3NetFlowPointFrameFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 42),
    _F3NetFlowPointFrameFwdEnabled_Type()
)
f3NetFlowPointFrameFwdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointFrameFwdEnabled.setStatus("current")
_F3NetFlowPointStorageType_Type = StorageType
_F3NetFlowPointStorageType_Object = MibTableColumn
f3NetFlowPointStorageType = _F3NetFlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 43),
    _F3NetFlowPointStorageType_Type()
)
f3NetFlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointStorageType.setStatus("current")
_F3NetFlowPointRowStatus_Type = RowStatus
_F3NetFlowPointRowStatus_Object = MibTableColumn
f3NetFlowPointRowStatus = _F3NetFlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 44),
    _F3NetFlowPointRowStatus_Type()
)
f3NetFlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFlowPointRowStatus.setStatus("current")
_F3NetFlowPointUsePortPrioMapProfile_Type = TruthValue
_F3NetFlowPointUsePortPrioMapProfile_Object = MibTableColumn
f3NetFlowPointUsePortPrioMapProfile = _F3NetFlowPointUsePortPrioMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 45),
    _F3NetFlowPointUsePortPrioMapProfile_Type()
)
f3NetFlowPointUsePortPrioMapProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointUsePortPrioMapProfile.setStatus("current")
_F3NetFlowPointRefPrioMapProfile_Type = VariablePointer
_F3NetFlowPointRefPrioMapProfile_Object = MibTableColumn
f3NetFlowPointRefPrioMapProfile = _F3NetFlowPointRefPrioMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 46),
    _F3NetFlowPointRefPrioMapProfile_Type()
)
f3NetFlowPointRefPrioMapProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointRefPrioMapProfile.setStatus("current")
_F3NetFlowpointRefConnectGuardFlowObject_Type = VariablePointer
_F3NetFlowpointRefConnectGuardFlowObject_Object = MibTableColumn
f3NetFlowpointRefConnectGuardFlowObject = _F3NetFlowpointRefConnectGuardFlowObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 47),
    _F3NetFlowpointRefConnectGuardFlowObject_Type()
)
f3NetFlowpointRefConnectGuardFlowObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowpointRefConnectGuardFlowObject.setStatus("current")
_F3NetFlowpointSecureBlockingControl_Type = TruthValue
_F3NetFlowpointSecureBlockingControl_Object = MibTableColumn
f3NetFlowpointSecureBlockingControl = _F3NetFlowpointSecureBlockingControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 48),
    _F3NetFlowpointSecureBlockingControl_Type()
)
f3NetFlowpointSecureBlockingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowpointSecureBlockingControl.setStatus("current")
_F3NetFlowpointSecureState_Type = FlowSecState
_F3NetFlowpointSecureState_Object = MibTableColumn
f3NetFlowpointSecureState = _F3NetFlowpointSecureState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 7, 1, 49),
    _F3NetFlowpointSecureState_Type()
)
f3NetFlowpointSecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowpointSecureState.setStatus("current")
_F3NetFpQosShaperTable_Object = MibTable
f3NetFpQosShaperTable = _F3NetFpQosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8)
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperTable.setStatus("current")
_F3NetFpQosShaperEntry_Object = MibTableRow
f3NetFpQosShaperEntry = _F3NetFpQosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1)
)
f3NetFpQosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperIndex"),
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperEntry.setStatus("current")


class _F3NetFpQosShaperIndex_Type(Integer32):
    """Custom type f3NetFpQosShaperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_F3NetFpQosShaperIndex_Type.__name__ = "Integer32"
_F3NetFpQosShaperIndex_Object = MibTableColumn
f3NetFpQosShaperIndex = _F3NetFpQosShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 1),
    _F3NetFpQosShaperIndex_Type()
)
f3NetFpQosShaperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NetFpQosShaperIndex.setStatus("current")
_F3NetFpQosShaperAdminState_Type = AdminState
_F3NetFpQosShaperAdminState_Object = MibTableColumn
f3NetFpQosShaperAdminState = _F3NetFpQosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 2),
    _F3NetFpQosShaperAdminState_Type()
)
f3NetFpQosShaperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperAdminState.setStatus("current")
_F3NetFpQosShaperOperationalState_Type = OperationalState
_F3NetFpQosShaperOperationalState_Object = MibTableColumn
f3NetFpQosShaperOperationalState = _F3NetFpQosShaperOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 3),
    _F3NetFpQosShaperOperationalState_Type()
)
f3NetFpQosShaperOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperOperationalState.setStatus("current")
_F3NetFpQosShaperSecondaryState_Type = SecondaryState
_F3NetFpQosShaperSecondaryState_Object = MibTableColumn
f3NetFpQosShaperSecondaryState = _F3NetFpQosShaperSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 4),
    _F3NetFpQosShaperSecondaryState_Type()
)
f3NetFpQosShaperSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperSecondaryState.setStatus("current")
_F3NetFpQosShaperCIRLo_Type = Unsigned32
_F3NetFpQosShaperCIRLo_Object = MibTableColumn
f3NetFpQosShaperCIRLo = _F3NetFpQosShaperCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 5),
    _F3NetFpQosShaperCIRLo_Type()
)
f3NetFpQosShaperCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperCIRLo.setStatus("current")
_F3NetFpQosShaperCIRHi_Type = Unsigned32
_F3NetFpQosShaperCIRHi_Object = MibTableColumn
f3NetFpQosShaperCIRHi = _F3NetFpQosShaperCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 6),
    _F3NetFpQosShaperCIRHi_Type()
)
f3NetFpQosShaperCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperCIRHi.setStatus("current")
_F3NetFpQosShaperEIRLo_Type = Unsigned32
_F3NetFpQosShaperEIRLo_Object = MibTableColumn
f3NetFpQosShaperEIRLo = _F3NetFpQosShaperEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 7),
    _F3NetFpQosShaperEIRLo_Type()
)
f3NetFpQosShaperEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperEIRLo.setStatus("current")
_F3NetFpQosShaperEIRHi_Type = Unsigned32
_F3NetFpQosShaperEIRHi_Object = MibTableColumn
f3NetFpQosShaperEIRHi = _F3NetFpQosShaperEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 8),
    _F3NetFpQosShaperEIRHi_Type()
)
f3NetFpQosShaperEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperEIRHi.setStatus("current")
_F3NetFpQosShaperCBS_Type = Unsigned32
_F3NetFpQosShaperCBS_Object = MibTableColumn
f3NetFpQosShaperCBS = _F3NetFpQosShaperCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 9),
    _F3NetFpQosShaperCBS_Type()
)
f3NetFpQosShaperCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperCBS.setStatus("current")
_F3NetFpQosShaperEBS_Type = Unsigned32
_F3NetFpQosShaperEBS_Object = MibTableColumn
f3NetFpQosShaperEBS = _F3NetFpQosShaperEBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 10),
    _F3NetFpQosShaperEBS_Type()
)
f3NetFpQosShaperEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperEBS.setStatus("current")
_F3NetFpQosShaperBufferSize_Type = Unsigned32
_F3NetFpQosShaperBufferSize_Object = MibTableColumn
f3NetFpQosShaperBufferSize = _F3NetFpQosShaperBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 11),
    _F3NetFpQosShaperBufferSize_Type()
)
f3NetFpQosShaperBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperBufferSize.setStatus("current")


class _F3NetFpQosShaperCOS_Type(Integer32):
    """Custom type f3NetFpQosShaperCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3NetFpQosShaperCOS_Type.__name__ = "Integer32"
_F3NetFpQosShaperCOS_Object = MibTableColumn
f3NetFpQosShaperCOS = _F3NetFpQosShaperCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 12),
    _F3NetFpQosShaperCOS_Type()
)
f3NetFpQosShaperCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperCOS.setStatus("current")
_F3NetFpQosShaperStorageType_Type = StorageType
_F3NetFpQosShaperStorageType_Object = MibTableColumn
f3NetFpQosShaperStorageType = _F3NetFpQosShaperStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 13),
    _F3NetFpQosShaperStorageType_Type()
)
f3NetFpQosShaperStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStorageType.setStatus("current")
_F3NetFpQosShaperRowStatus_Type = RowStatus
_F3NetFpQosShaperRowStatus_Object = MibTableColumn
f3NetFpQosShaperRowStatus = _F3NetFpQosShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 8, 1, 14),
    _F3NetFpQosShaperRowStatus_Type()
)
f3NetFpQosShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosShaperRowStatus.setStatus("current")
_F3NetFpQosPolicerTable_Object = MibTable
f3NetFpQosPolicerTable = _F3NetFpQosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9)
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerTable.setStatus("current")
_F3NetFpQosPolicerEntry_Object = MibTableRow
f3NetFpQosPolicerEntry = _F3NetFpQosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1)
)
f3NetFpQosPolicerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerIndex"),
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerEntry.setStatus("current")


class _F3NetFpQosPolicerIndex_Type(Integer32):
    """Custom type f3NetFpQosPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_F3NetFpQosPolicerIndex_Type.__name__ = "Integer32"
_F3NetFpQosPolicerIndex_Object = MibTableColumn
f3NetFpQosPolicerIndex = _F3NetFpQosPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 1),
    _F3NetFpQosPolicerIndex_Type()
)
f3NetFpQosPolicerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerIndex.setStatus("current")
_F3NetFpQosPolicerAdminState_Type = AdminState
_F3NetFpQosPolicerAdminState_Object = MibTableColumn
f3NetFpQosPolicerAdminState = _F3NetFpQosPolicerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 2),
    _F3NetFpQosPolicerAdminState_Type()
)
f3NetFpQosPolicerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerAdminState.setStatus("current")
_F3NetFpQosPolicerOperationalState_Type = OperationalState
_F3NetFpQosPolicerOperationalState_Object = MibTableColumn
f3NetFpQosPolicerOperationalState = _F3NetFpQosPolicerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 3),
    _F3NetFpQosPolicerOperationalState_Type()
)
f3NetFpQosPolicerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerOperationalState.setStatus("current")
_F3NetFpQosPolicerSecondaryState_Type = SecondaryState
_F3NetFpQosPolicerSecondaryState_Object = MibTableColumn
f3NetFpQosPolicerSecondaryState = _F3NetFpQosPolicerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 4),
    _F3NetFpQosPolicerSecondaryState_Type()
)
f3NetFpQosPolicerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerSecondaryState.setStatus("current")
_F3NetFpQosPolicerCIRLo_Type = Unsigned32
_F3NetFpQosPolicerCIRLo_Object = MibTableColumn
f3NetFpQosPolicerCIRLo = _F3NetFpQosPolicerCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 5),
    _F3NetFpQosPolicerCIRLo_Type()
)
f3NetFpQosPolicerCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerCIRLo.setStatus("current")
_F3NetFpQosPolicerCIRHi_Type = Unsigned32
_F3NetFpQosPolicerCIRHi_Object = MibTableColumn
f3NetFpQosPolicerCIRHi = _F3NetFpQosPolicerCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 6),
    _F3NetFpQosPolicerCIRHi_Type()
)
f3NetFpQosPolicerCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerCIRHi.setStatus("current")
_F3NetFpQosPolicerEIRLo_Type = Unsigned32
_F3NetFpQosPolicerEIRLo_Object = MibTableColumn
f3NetFpQosPolicerEIRLo = _F3NetFpQosPolicerEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 7),
    _F3NetFpQosPolicerEIRLo_Type()
)
f3NetFpQosPolicerEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerEIRLo.setStatus("current")
_F3NetFpQosPolicerEIRHi_Type = Unsigned32
_F3NetFpQosPolicerEIRHi_Object = MibTableColumn
f3NetFpQosPolicerEIRHi = _F3NetFpQosPolicerEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 8),
    _F3NetFpQosPolicerEIRHi_Type()
)
f3NetFpQosPolicerEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerEIRHi.setStatus("current")
_F3NetFpQosPolicerCBS_Type = Integer32
_F3NetFpQosPolicerCBS_Object = MibTableColumn
f3NetFpQosPolicerCBS = _F3NetFpQosPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 9),
    _F3NetFpQosPolicerCBS_Type()
)
f3NetFpQosPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerCBS.setStatus("current")
_F3NetFpQosPolicerEBS_Type = Integer32
_F3NetFpQosPolicerEBS_Object = MibTableColumn
f3NetFpQosPolicerEBS = _F3NetFpQosPolicerEBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 10),
    _F3NetFpQosPolicerEBS_Type()
)
f3NetFpQosPolicerEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerEBS.setStatus("current")
_F3NetFpQosPolicerAlgorithm_Type = PolicerAlgorithmType
_F3NetFpQosPolicerAlgorithm_Object = MibTableColumn
f3NetFpQosPolicerAlgorithm = _F3NetFpQosPolicerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 11),
    _F3NetFpQosPolicerAlgorithm_Type()
)
f3NetFpQosPolicerAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerAlgorithm.setStatus("current")
_F3NetFpQosPolicerColorMode_Type = PolicerColorMode
_F3NetFpQosPolicerColorMode_Object = MibTableColumn
f3NetFpQosPolicerColorMode = _F3NetFpQosPolicerColorMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 12),
    _F3NetFpQosPolicerColorMode_Type()
)
f3NetFpQosPolicerColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerColorMode.setStatus("current")
_F3NetFpQosPolicerCouplingFlag_Type = TruthValue
_F3NetFpQosPolicerCouplingFlag_Object = MibTableColumn
f3NetFpQosPolicerCouplingFlag = _F3NetFpQosPolicerCouplingFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 13),
    _F3NetFpQosPolicerCouplingFlag_Type()
)
f3NetFpQosPolicerCouplingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerCouplingFlag.setStatus("current")
_F3NetFpQosPolicerPolicingEnabled_Type = TruthValue
_F3NetFpQosPolicerPolicingEnabled_Object = MibTableColumn
f3NetFpQosPolicerPolicingEnabled = _F3NetFpQosPolicerPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 14),
    _F3NetFpQosPolicerPolicingEnabled_Type()
)
f3NetFpQosPolicerPolicingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerPolicingEnabled.setStatus("current")
_F3NetFpQosPolicerStorageType_Type = StorageType
_F3NetFpQosPolicerStorageType_Object = MibTableColumn
f3NetFpQosPolicerStorageType = _F3NetFpQosPolicerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 15),
    _F3NetFpQosPolicerStorageType_Type()
)
f3NetFpQosPolicerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStorageType.setStatus("current")
_F3NetFpQosPolicerRowStatus_Type = RowStatus
_F3NetFpQosPolicerRowStatus_Object = MibTableColumn
f3NetFpQosPolicerRowStatus = _F3NetFpQosPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 9, 1, 16),
    _F3NetFpQosPolicerRowStatus_Type()
)
f3NetFpQosPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerRowStatus.setStatus("current")
_F3NetFlowPointCpdV2Table_Object = MibTable
f3NetFlowPointCpdV2Table = _F3NetFlowPointCpdV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10)
)
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Table.setStatus("current")
_F3NetFlowPointCpdV2Entry_Object = MibTableRow
f3NetFlowPointCpdV2Entry = _F3NetFlowPointCpdV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1)
)
f3NetFlowPointCpdV2Entry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointCpdV2Index"),
)
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Entry.setStatus("current")
_F3NetFlowPointCpdV2Index_Type = Integer32
_F3NetFlowPointCpdV2Index_Object = MibTableColumn
f3NetFlowPointCpdV2Index = _F3NetFlowPointCpdV2Index_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 1),
    _F3NetFlowPointCpdV2Index_Type()
)
f3NetFlowPointCpdV2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Index.setStatus("current")
_F3NetFlowPointCpdV2IslDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2IslDispType_Object = MibTableColumn
f3NetFlowPointCpdV2IslDispType = _F3NetFlowPointCpdV2IslDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 2),
    _F3NetFlowPointCpdV2IslDispType_Type()
)
f3NetFlowPointCpdV2IslDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2IslDispType.setStatus("current")
_F3NetFlowPointCpdV2PagpDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2PagpDispType_Object = MibTableColumn
f3NetFlowPointCpdV2PagpDispType = _F3NetFlowPointCpdV2PagpDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 3),
    _F3NetFlowPointCpdV2PagpDispType_Type()
)
f3NetFlowPointCpdV2PagpDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2PagpDispType.setStatus("current")
_F3NetFlowPointCpdV2UdldDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2UdldDispType_Object = MibTableColumn
f3NetFlowPointCpdV2UdldDispType = _F3NetFlowPointCpdV2UdldDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 4),
    _F3NetFlowPointCpdV2UdldDispType_Type()
)
f3NetFlowPointCpdV2UdldDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2UdldDispType.setStatus("current")
_F3NetFlowPointCpdV2CdpDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2CdpDispType_Object = MibTableColumn
f3NetFlowPointCpdV2CdpDispType = _F3NetFlowPointCpdV2CdpDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 5),
    _F3NetFlowPointCpdV2CdpDispType_Type()
)
f3NetFlowPointCpdV2CdpDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2CdpDispType.setStatus("current")
_F3NetFlowPointCpdV2VtpDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2VtpDispType_Object = MibTableColumn
f3NetFlowPointCpdV2VtpDispType = _F3NetFlowPointCpdV2VtpDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 6),
    _F3NetFlowPointCpdV2VtpDispType_Type()
)
f3NetFlowPointCpdV2VtpDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2VtpDispType.setStatus("current")
_F3NetFlowPointCpdV2DtpDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2DtpDispType_Object = MibTableColumn
f3NetFlowPointCpdV2DtpDispType = _F3NetFlowPointCpdV2DtpDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 7),
    _F3NetFlowPointCpdV2DtpDispType_Type()
)
f3NetFlowPointCpdV2DtpDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2DtpDispType.setStatus("current")
_F3NetFlowPointCpdV2PvstpPlusDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2PvstpPlusDispType_Object = MibTableColumn
f3NetFlowPointCpdV2PvstpPlusDispType = _F3NetFlowPointCpdV2PvstpPlusDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 8),
    _F3NetFlowPointCpdV2PvstpPlusDispType_Type()
)
f3NetFlowPointCpdV2PvstpPlusDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2PvstpPlusDispType.setStatus("current")
_F3NetFlowPointCpdV2UplinkFastDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2UplinkFastDispType_Object = MibTableColumn
f3NetFlowPointCpdV2UplinkFastDispType = _F3NetFlowPointCpdV2UplinkFastDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 9),
    _F3NetFlowPointCpdV2UplinkFastDispType_Type()
)
f3NetFlowPointCpdV2UplinkFastDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2UplinkFastDispType.setStatus("current")
_F3NetFlowPointCpdV2VlanBridgeDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2VlanBridgeDispType_Object = MibTableColumn
f3NetFlowPointCpdV2VlanBridgeDispType = _F3NetFlowPointCpdV2VlanBridgeDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 10),
    _F3NetFlowPointCpdV2VlanBridgeDispType_Type()
)
f3NetFlowPointCpdV2VlanBridgeDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2VlanBridgeDispType.setStatus("current")
_F3NetFlowPointCpdV2L2PTDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2L2PTDispType_Object = MibTableColumn
f3NetFlowPointCpdV2L2PTDispType = _F3NetFlowPointCpdV2L2PTDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 11),
    _F3NetFlowPointCpdV2L2PTDispType_Type()
)
f3NetFlowPointCpdV2L2PTDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2L2PTDispType.setStatus("current")
_F3NetFlowPointCpdV2BPDUDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2BPDUDispType_Object = MibTableColumn
f3NetFlowPointCpdV2BPDUDispType = _F3NetFlowPointCpdV2BPDUDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 12),
    _F3NetFlowPointCpdV2BPDUDispType_Type()
)
f3NetFlowPointCpdV2BPDUDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2BPDUDispType.setStatus("current")
_F3NetFlowPointCpdV2PauseDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2PauseDispType_Object = MibTableColumn
f3NetFlowPointCpdV2PauseDispType = _F3NetFlowPointCpdV2PauseDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 13),
    _F3NetFlowPointCpdV2PauseDispType_Type()
)
f3NetFlowPointCpdV2PauseDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2PauseDispType.setStatus("current")
_F3NetFlowPointCpdV2LACPDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2LACPDispType_Object = MibTableColumn
f3NetFlowPointCpdV2LACPDispType = _F3NetFlowPointCpdV2LACPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 14),
    _F3NetFlowPointCpdV2LACPDispType_Type()
)
f3NetFlowPointCpdV2LACPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2LACPDispType.setStatus("current")
_F3NetFlowPointCpdV2LACPMarkerDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2LACPMarkerDispType_Object = MibTableColumn
f3NetFlowPointCpdV2LACPMarkerDispType = _F3NetFlowPointCpdV2LACPMarkerDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 15),
    _F3NetFlowPointCpdV2LACPMarkerDispType_Type()
)
f3NetFlowPointCpdV2LACPMarkerDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2LACPMarkerDispType.setStatus("current")
_F3NetFlowPointCpdV2EfmOamDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2EfmOamDispType_Object = MibTableColumn
f3NetFlowPointCpdV2EfmOamDispType = _F3NetFlowPointCpdV2EfmOamDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 16),
    _F3NetFlowPointCpdV2EfmOamDispType_Type()
)
f3NetFlowPointCpdV2EfmOamDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2EfmOamDispType.setStatus("current")
_F3NetFlowPointCpdV2SSMDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2SSMDispType_Object = MibTableColumn
f3NetFlowPointCpdV2SSMDispType = _F3NetFlowPointCpdV2SSMDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 17),
    _F3NetFlowPointCpdV2SSMDispType_Type()
)
f3NetFlowPointCpdV2SSMDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2SSMDispType.setStatus("current")
_F3NetFlowPointCpdV2PortAuthenDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2PortAuthenDispType_Object = MibTableColumn
f3NetFlowPointCpdV2PortAuthenDispType = _F3NetFlowPointCpdV2PortAuthenDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 18),
    _F3NetFlowPointCpdV2PortAuthenDispType_Type()
)
f3NetFlowPointCpdV2PortAuthenDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2PortAuthenDispType.setStatus("current")
_F3NetFlowPointCpdV2LANBridgesDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2LANBridgesDispType_Object = MibTableColumn
f3NetFlowPointCpdV2LANBridgesDispType = _F3NetFlowPointCpdV2LANBridgesDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 19),
    _F3NetFlowPointCpdV2LANBridgesDispType_Type()
)
f3NetFlowPointCpdV2LANBridgesDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2LANBridgesDispType.setStatus("current")
_F3NetFlowPointCpdV2GMRPDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2GMRPDispType_Object = MibTableColumn
f3NetFlowPointCpdV2GMRPDispType = _F3NetFlowPointCpdV2GMRPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 20),
    _F3NetFlowPointCpdV2GMRPDispType_Type()
)
f3NetFlowPointCpdV2GMRPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2GMRPDispType.setStatus("current")
_F3NetFlowPointCpdV2GVRPDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2GVRPDispType_Object = MibTableColumn
f3NetFlowPointCpdV2GVRPDispType = _F3NetFlowPointCpdV2GVRPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 21),
    _F3NetFlowPointCpdV2GVRPDispType_Type()
)
f3NetFlowPointCpdV2GVRPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2GVRPDispType.setStatus("current")
_F3NetFlowPointCpdV2GARPDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2GARPDispType_Object = MibTableColumn
f3NetFlowPointCpdV2GARPDispType = _F3NetFlowPointCpdV2GARPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 22),
    _F3NetFlowPointCpdV2GARPDispType_Type()
)
f3NetFlowPointCpdV2GARPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2GARPDispType.setStatus("current")
_F3NetFlowPointCpdV2ActiveControlProtocols_Type = CmActiveControlProtocolsType
_F3NetFlowPointCpdV2ActiveControlProtocols_Object = MibTableColumn
f3NetFlowPointCpdV2ActiveControlProtocols = _F3NetFlowPointCpdV2ActiveControlProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 23),
    _F3NetFlowPointCpdV2ActiveControlProtocols_Type()
)
f3NetFlowPointCpdV2ActiveControlProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2ActiveControlProtocols.setStatus("current")
_F3NetFlowPointCpdV2ELMIDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2ELMIDispType_Object = MibTableColumn
f3NetFlowPointCpdV2ELMIDispType = _F3NetFlowPointCpdV2ELMIDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 24),
    _F3NetFlowPointCpdV2ELMIDispType_Type()
)
f3NetFlowPointCpdV2ELMIDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2ELMIDispType.setStatus("current")
_F3NetFlowPointCpdV2Mac00DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac00DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac00DispType = _F3NetFlowPointCpdV2Mac00DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 25),
    _F3NetFlowPointCpdV2Mac00DispType_Type()
)
f3NetFlowPointCpdV2Mac00DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac00DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac01DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac01DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac01DispType = _F3NetFlowPointCpdV2Mac01DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 26),
    _F3NetFlowPointCpdV2Mac01DispType_Type()
)
f3NetFlowPointCpdV2Mac01DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac01DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac02DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac02DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac02DispType = _F3NetFlowPointCpdV2Mac02DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 27),
    _F3NetFlowPointCpdV2Mac02DispType_Type()
)
f3NetFlowPointCpdV2Mac02DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac02DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac03DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac03DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac03DispType = _F3NetFlowPointCpdV2Mac03DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 28),
    _F3NetFlowPointCpdV2Mac03DispType_Type()
)
f3NetFlowPointCpdV2Mac03DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac03DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac04DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac04DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac04DispType = _F3NetFlowPointCpdV2Mac04DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 29),
    _F3NetFlowPointCpdV2Mac04DispType_Type()
)
f3NetFlowPointCpdV2Mac04DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac04DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac05DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac05DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac05DispType = _F3NetFlowPointCpdV2Mac05DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 30),
    _F3NetFlowPointCpdV2Mac05DispType_Type()
)
f3NetFlowPointCpdV2Mac05DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac05DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac06DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac06DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac06DispType = _F3NetFlowPointCpdV2Mac06DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 31),
    _F3NetFlowPointCpdV2Mac06DispType_Type()
)
f3NetFlowPointCpdV2Mac06DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac06DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac07DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac07DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac07DispType = _F3NetFlowPointCpdV2Mac07DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 32),
    _F3NetFlowPointCpdV2Mac07DispType_Type()
)
f3NetFlowPointCpdV2Mac07DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac07DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac08DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac08DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac08DispType = _F3NetFlowPointCpdV2Mac08DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 33),
    _F3NetFlowPointCpdV2Mac08DispType_Type()
)
f3NetFlowPointCpdV2Mac08DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac08DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac09DispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac09DispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac09DispType = _F3NetFlowPointCpdV2Mac09DispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 34),
    _F3NetFlowPointCpdV2Mac09DispType_Type()
)
f3NetFlowPointCpdV2Mac09DispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac09DispType.setStatus("current")
_F3NetFlowPointCpdV2Mac0ADispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac0ADispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac0ADispType = _F3NetFlowPointCpdV2Mac0ADispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 35),
    _F3NetFlowPointCpdV2Mac0ADispType_Type()
)
f3NetFlowPointCpdV2Mac0ADispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac0ADispType.setStatus("current")
_F3NetFlowPointCpdV2Mac0BDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac0BDispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac0BDispType = _F3NetFlowPointCpdV2Mac0BDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 36),
    _F3NetFlowPointCpdV2Mac0BDispType_Type()
)
f3NetFlowPointCpdV2Mac0BDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac0BDispType.setStatus("current")
_F3NetFlowPointCpdV2Mac0CDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac0CDispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac0CDispType = _F3NetFlowPointCpdV2Mac0CDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 37),
    _F3NetFlowPointCpdV2Mac0CDispType_Type()
)
f3NetFlowPointCpdV2Mac0CDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac0CDispType.setStatus("current")
_F3NetFlowPointCpdV2Mac0DDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac0DDispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac0DDispType = _F3NetFlowPointCpdV2Mac0DDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 38),
    _F3NetFlowPointCpdV2Mac0DDispType_Type()
)
f3NetFlowPointCpdV2Mac0DDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac0DDispType.setStatus("current")
_F3NetFlowPointCpdV2Mac0EDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac0EDispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac0EDispType = _F3NetFlowPointCpdV2Mac0EDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 39),
    _F3NetFlowPointCpdV2Mac0EDispType_Type()
)
f3NetFlowPointCpdV2Mac0EDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac0EDispType.setStatus("current")
_F3NetFlowPointCpdV2Mac0FDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2Mac0FDispType_Object = MibTableColumn
f3NetFlowPointCpdV2Mac0FDispType = _F3NetFlowPointCpdV2Mac0FDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 40),
    _F3NetFlowPointCpdV2Mac0FDispType_Type()
)
f3NetFlowPointCpdV2Mac0FDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Mac0FDispType.setStatus("current")
_F3NetFlowPointCpdV2NearestLLDPDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2NearestLLDPDispType_Object = MibTableColumn
f3NetFlowPointCpdV2NearestLLDPDispType = _F3NetFlowPointCpdV2NearestLLDPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 41),
    _F3NetFlowPointCpdV2NearestLLDPDispType_Type()
)
f3NetFlowPointCpdV2NearestLLDPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2NearestLLDPDispType.setStatus("current")
_F3NetFlowPointCpdV2NonTpmrLLDPDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2NonTpmrLLDPDispType_Object = MibTableColumn
f3NetFlowPointCpdV2NonTpmrLLDPDispType = _F3NetFlowPointCpdV2NonTpmrLLDPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 42),
    _F3NetFlowPointCpdV2NonTpmrLLDPDispType_Type()
)
f3NetFlowPointCpdV2NonTpmrLLDPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2NonTpmrLLDPDispType.setStatus("current")
_F3NetFlowPointCpdV2CustomerLLDPDispType_Type = CmControlProtocolDispType
_F3NetFlowPointCpdV2CustomerLLDPDispType_Object = MibTableColumn
f3NetFlowPointCpdV2CustomerLLDPDispType = _F3NetFlowPointCpdV2CustomerLLDPDispType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 10, 1, 43),
    _F3NetFlowPointCpdV2CustomerLLDPDispType_Type()
)
f3NetFlowPointCpdV2CustomerLLDPDispType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2CustomerLLDPDispType.setStatus("current")
_F3NetFlowPointLearningConfigTable_Object = MibTable
f3NetFlowPointLearningConfigTable = _F3NetFlowPointLearningConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 11)
)
if mibBuilder.loadTexts:
    f3NetFlowPointLearningConfigTable.setStatus("current")
_F3NetFlowPointLearningConfigEntry_Object = MibTableRow
f3NetFlowPointLearningConfigEntry = _F3NetFlowPointLearningConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 11, 1)
)
if mibBuilder.loadTexts:
    f3NetFlowPointLearningConfigEntry.setStatus("current")
_F3NetFlowPointLearningConfigLearningEnabled_Type = TruthValue
_F3NetFlowPointLearningConfigLearningEnabled_Object = MibTableColumn
f3NetFlowPointLearningConfigLearningEnabled = _F3NetFlowPointLearningConfigLearningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 11, 1, 1),
    _F3NetFlowPointLearningConfigLearningEnabled_Type()
)
f3NetFlowPointLearningConfigLearningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointLearningConfigLearningEnabled.setStatus("current")
_F3NetFlowPointLearningConfigMaxFwdEntries_Type = Integer32
_F3NetFlowPointLearningConfigMaxFwdEntries_Object = MibTableColumn
f3NetFlowPointLearningConfigMaxFwdEntries = _F3NetFlowPointLearningConfigMaxFwdEntries_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 11, 1, 2),
    _F3NetFlowPointLearningConfigMaxFwdEntries_Type()
)
f3NetFlowPointLearningConfigMaxFwdEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointLearningConfigMaxFwdEntries.setStatus("current")
_F3NetFlowPointLearningConfigProtectLearningCtrl_Type = ProtectLearningControl
_F3NetFlowPointLearningConfigProtectLearningCtrl_Object = MibTableColumn
f3NetFlowPointLearningConfigProtectLearningCtrl = _F3NetFlowPointLearningConfigProtectLearningCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 11, 1, 3),
    _F3NetFlowPointLearningConfigProtectLearningCtrl_Type()
)
f3NetFlowPointLearningConfigProtectLearningCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointLearningConfigProtectLearningCtrl.setStatus("current")
_F3NetFlowPointLearningConfigAction_Type = FlowLearningConfigAction
_F3NetFlowPointLearningConfigAction_Object = MibTableColumn
f3NetFlowPointLearningConfigAction = _F3NetFlowPointLearningConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 1, 11, 1, 4),
    _F3NetFlowPointLearningConfigAction_Type()
)
f3NetFlowPointLearningConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointLearningConfigAction.setStatus("current")
_F3FpmPerfObjects_ObjectIdentity = ObjectIdentity
f3FpmPerfObjects = _F3FpmPerfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2)
)
_F3AccFlowPointStatsTable_Object = MibTable
f3AccFlowPointStatsTable = _F3AccFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1)
)
if mibBuilder.loadTexts:
    f3AccFlowPointStatsTable.setStatus("current")
_F3AccFlowPointStatsEntry_Object = MibTableRow
f3AccFlowPointStatsEntry = _F3AccFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1)
)
f3AccFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3AccFlowPointStatsEntry.setStatus("current")


class _F3AccFlowPointStatsIndex_Type(Integer32):
    """Custom type f3AccFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFlowPointStatsIndex_Type.__name__ = "Integer32"
_F3AccFlowPointStatsIndex_Object = MibTableColumn
f3AccFlowPointStatsIndex = _F3AccFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 1),
    _F3AccFlowPointStatsIndex_Type()
)
f3AccFlowPointStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsIndex.setStatus("current")
_F3AccFlowPointStatsIntervalType_Type = CmPmIntervalType
_F3AccFlowPointStatsIntervalType_Object = MibTableColumn
f3AccFlowPointStatsIntervalType = _F3AccFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 2),
    _F3AccFlowPointStatsIntervalType_Type()
)
f3AccFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsIntervalType.setStatus("current")
_F3AccFlowPointStatsValid_Type = TruthValue
_F3AccFlowPointStatsValid_Object = MibTableColumn
f3AccFlowPointStatsValid = _F3AccFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 3),
    _F3AccFlowPointStatsValid_Type()
)
f3AccFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsValid.setStatus("current")
_F3AccFlowPointStatsAction_Type = CmPmBinAction
_F3AccFlowPointStatsAction_Object = MibTableColumn
f3AccFlowPointStatsAction = _F3AccFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 4),
    _F3AccFlowPointStatsAction_Type()
)
f3AccFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsAction.setStatus("current")
_F3AccFlowPointStatsL2CPFD_Type = PerfCounter64
_F3AccFlowPointStatsL2CPFD_Object = MibTableColumn
f3AccFlowPointStatsL2CPFD = _F3AccFlowPointStatsL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 5),
    _F3AccFlowPointStatsL2CPFD_Type()
)
f3AccFlowPointStatsL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsL2CPFD.setStatus("current")
_F3AccFlowPointStatsABRRx_Type = PerfCounter64
_F3AccFlowPointStatsABRRx_Object = MibTableColumn
f3AccFlowPointStatsABRRx = _F3AccFlowPointStatsABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 6),
    _F3AccFlowPointStatsABRRx_Type()
)
f3AccFlowPointStatsABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsABRRx.setStatus("current")
_F3AccFlowPointStatsABRRLRx_Type = PerfCounter64
_F3AccFlowPointStatsABRRLRx_Object = MibTableColumn
f3AccFlowPointStatsABRRLRx = _F3AccFlowPointStatsABRRLRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 7),
    _F3AccFlowPointStatsABRRLRx_Type()
)
f3AccFlowPointStatsABRRLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsABRRLRx.setStatus("current")
_F3AccFlowPointStatsUAS_Type = PerfCounter64
_F3AccFlowPointStatsUAS_Object = MibTableColumn
f3AccFlowPointStatsUAS = _F3AccFlowPointStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 8),
    _F3AccFlowPointStatsUAS_Type()
)
f3AccFlowPointStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsUAS.setStatus("current")
_F3AccFlowPointStatsSES_Type = PerfCounter64
_F3AccFlowPointStatsSES_Object = MibTableColumn
f3AccFlowPointStatsSES = _F3AccFlowPointStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 9),
    _F3AccFlowPointStatsSES_Type()
)
f3AccFlowPointStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsSES.setStatus("current")
_F3AccFlowPointStatsFMG_Type = PerfCounter64
_F3AccFlowPointStatsFMG_Object = MibTableColumn
f3AccFlowPointStatsFMG = _F3AccFlowPointStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 10),
    _F3AccFlowPointStatsFMG_Type()
)
f3AccFlowPointStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFMG.setStatus("current")
_F3AccFlowPointStatsFMY_Type = PerfCounter64
_F3AccFlowPointStatsFMY_Object = MibTableColumn
f3AccFlowPointStatsFMY = _F3AccFlowPointStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 11),
    _F3AccFlowPointStatsFMY_Type()
)
f3AccFlowPointStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFMY.setStatus("current")
_F3AccFlowPointStatsFMRD_Type = PerfCounter64
_F3AccFlowPointStatsFMRD_Object = MibTableColumn
f3AccFlowPointStatsFMRD = _F3AccFlowPointStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 12),
    _F3AccFlowPointStatsFMRD_Type()
)
f3AccFlowPointStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFMRD.setStatus("current")
_F3AccFlowPointStatsFTD_Type = PerfCounter64
_F3AccFlowPointStatsFTD_Object = MibTableColumn
f3AccFlowPointStatsFTD = _F3AccFlowPointStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 13),
    _F3AccFlowPointStatsFTD_Type()
)
f3AccFlowPointStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFTD.setStatus("current")
_F3AccFlowPointStatsBytesIn_Type = PerfCounter64
_F3AccFlowPointStatsBytesIn_Object = MibTableColumn
f3AccFlowPointStatsBytesIn = _F3AccFlowPointStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 14),
    _F3AccFlowPointStatsBytesIn_Type()
)
f3AccFlowPointStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsBytesIn.setStatus("current")
_F3AccFlowPointStatsBytesOut_Type = PerfCounter64
_F3AccFlowPointStatsBytesOut_Object = MibTableColumn
f3AccFlowPointStatsBytesOut = _F3AccFlowPointStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 15),
    _F3AccFlowPointStatsBytesOut_Type()
)
f3AccFlowPointStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsBytesOut.setStatus("current")
_F3AccFlowPointStatsIBRMax_Type = PerfCounter64
_F3AccFlowPointStatsIBRMax_Object = MibTableColumn
f3AccFlowPointStatsIBRMax = _F3AccFlowPointStatsIBRMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 16),
    _F3AccFlowPointStatsIBRMax_Type()
)
f3AccFlowPointStatsIBRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsIBRMax.setStatus("current")
_F3AccFlowPointStatsIBRRlMax_Type = PerfCounter64
_F3AccFlowPointStatsIBRRlMax_Object = MibTableColumn
f3AccFlowPointStatsIBRRlMax = _F3AccFlowPointStatsIBRRlMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 17),
    _F3AccFlowPointStatsIBRRlMax_Type()
)
f3AccFlowPointStatsIBRRlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsIBRRlMax.setStatus("current")
_F3AccFlowPointStatsIBRMin_Type = PerfCounter64
_F3AccFlowPointStatsIBRMin_Object = MibTableColumn
f3AccFlowPointStatsIBRMin = _F3AccFlowPointStatsIBRMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 18),
    _F3AccFlowPointStatsIBRMin_Type()
)
f3AccFlowPointStatsIBRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsIBRMin.setStatus("current")
_F3AccFlowPointStatsIBRRlMin_Type = PerfCounter64
_F3AccFlowPointStatsIBRRlMin_Object = MibTableColumn
f3AccFlowPointStatsIBRRlMin = _F3AccFlowPointStatsIBRRlMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 19),
    _F3AccFlowPointStatsIBRRlMin_Type()
)
f3AccFlowPointStatsIBRRlMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsIBRRlMin.setStatus("current")
_F3AccFlowPointStatsIBR_Type = PerfCounter64
_F3AccFlowPointStatsIBR_Object = MibTableColumn
f3AccFlowPointStatsIBR = _F3AccFlowPointStatsIBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 20),
    _F3AccFlowPointStatsIBR_Type()
)
f3AccFlowPointStatsIBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsIBR.setStatus("current")
_F3AccFlowPointStatsIBRRl_Type = PerfCounter64
_F3AccFlowPointStatsIBRRl_Object = MibTableColumn
f3AccFlowPointStatsIBRRl = _F3AccFlowPointStatsIBRRl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 21),
    _F3AccFlowPointStatsIBRRl_Type()
)
f3AccFlowPointStatsIBRRl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsIBRRl.setStatus("current")
_F3AccFlowPointStatsFBCD_Type = PerfCounter64
_F3AccFlowPointStatsFBCD_Object = MibTableColumn
f3AccFlowPointStatsFBCD = _F3AccFlowPointStatsFBCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 22),
    _F3AccFlowPointStatsFBCD_Type()
)
f3AccFlowPointStatsFBCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFBCD.setStatus("current")
_F3AccFlowPointStatsFMCD_Type = PerfCounter64
_F3AccFlowPointStatsFMCD_Object = MibTableColumn
f3AccFlowPointStatsFMCD = _F3AccFlowPointStatsFMCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 23),
    _F3AccFlowPointStatsFMCD_Type()
)
f3AccFlowPointStatsFMCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFMCD.setStatus("current")
_F3AccFlowPointStatsFdRxFb_Type = PerfCounter64
_F3AccFlowPointStatsFdRxFb_Object = MibTableColumn
f3AccFlowPointStatsFdRxFb = _F3AccFlowPointStatsFdRxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 24),
    _F3AccFlowPointStatsFdRxFb_Type()
)
f3AccFlowPointStatsFdRxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFdRxFb.setStatus("current")
_F3AccFlowPointStatsFdTxFb_Type = PerfCounter64
_F3AccFlowPointStatsFdTxFb_Object = MibTableColumn
f3AccFlowPointStatsFdTxFb = _F3AccFlowPointStatsFdTxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 25),
    _F3AccFlowPointStatsFdTxFb_Type()
)
f3AccFlowPointStatsFdTxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFdTxFb.setStatus("current")
_F3AccFlowPointStatsFdicd_Type = PerfCounter64
_F3AccFlowPointStatsFdicd_Object = MibTableColumn
f3AccFlowPointStatsFdicd = _F3AccFlowPointStatsFdicd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 26),
    _F3AccFlowPointStatsFdicd_Type()
)
f3AccFlowPointStatsFdicd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsFdicd.setStatus("current")
_F3AccFlowPointStatsNumLearnTableFlushes_Type = PerfCounter64
_F3AccFlowPointStatsNumLearnTableFlushes_Object = MibTableColumn
f3AccFlowPointStatsNumLearnTableFlushes = _F3AccFlowPointStatsNumLearnTableFlushes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 1, 1, 27),
    _F3AccFlowPointStatsNumLearnTableFlushes_Type()
)
f3AccFlowPointStatsNumLearnTableFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointStatsNumLearnTableFlushes.setStatus("current")
_F3NetFlowPointStatsTable_Object = MibTable
f3NetFlowPointStatsTable = _F3NetFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2)
)
if mibBuilder.loadTexts:
    f3NetFlowPointStatsTable.setStatus("current")
_F3NetFlowPointStatsEntry_Object = MibTableRow
f3NetFlowPointStatsEntry = _F3NetFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1)
)
f3NetFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NetFlowPointStatsEntry.setStatus("current")


class _F3NetFlowPointStatsIndex_Type(Integer32):
    """Custom type f3NetFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFlowPointStatsIndex_Type.__name__ = "Integer32"
_F3NetFlowPointStatsIndex_Object = MibTableColumn
f3NetFlowPointStatsIndex = _F3NetFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 1),
    _F3NetFlowPointStatsIndex_Type()
)
f3NetFlowPointStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsIndex.setStatus("current")
_F3NetFlowPointStatsIntervalType_Type = CmPmIntervalType
_F3NetFlowPointStatsIntervalType_Object = MibTableColumn
f3NetFlowPointStatsIntervalType = _F3NetFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 2),
    _F3NetFlowPointStatsIntervalType_Type()
)
f3NetFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsIntervalType.setStatus("current")
_F3NetFlowPointStatsValid_Type = TruthValue
_F3NetFlowPointStatsValid_Object = MibTableColumn
f3NetFlowPointStatsValid = _F3NetFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 3),
    _F3NetFlowPointStatsValid_Type()
)
f3NetFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsValid.setStatus("current")
_F3NetFlowPointStatsAction_Type = CmPmBinAction
_F3NetFlowPointStatsAction_Object = MibTableColumn
f3NetFlowPointStatsAction = _F3NetFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 4),
    _F3NetFlowPointStatsAction_Type()
)
f3NetFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsAction.setStatus("current")
_F3NetFlowPointStatsL2CPFD_Type = PerfCounter64
_F3NetFlowPointStatsL2CPFD_Object = MibTableColumn
f3NetFlowPointStatsL2CPFD = _F3NetFlowPointStatsL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 5),
    _F3NetFlowPointStatsL2CPFD_Type()
)
f3NetFlowPointStatsL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsL2CPFD.setStatus("current")
_F3NetFlowPointStatsABRRx_Type = PerfCounter64
_F3NetFlowPointStatsABRRx_Object = MibTableColumn
f3NetFlowPointStatsABRRx = _F3NetFlowPointStatsABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 6),
    _F3NetFlowPointStatsABRRx_Type()
)
f3NetFlowPointStatsABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsABRRx.setStatus("current")
_F3NetFlowPointStatsABRRLRx_Type = PerfCounter64
_F3NetFlowPointStatsABRRLRx_Object = MibTableColumn
f3NetFlowPointStatsABRRLRx = _F3NetFlowPointStatsABRRLRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 7),
    _F3NetFlowPointStatsABRRLRx_Type()
)
f3NetFlowPointStatsABRRLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsABRRLRx.setStatus("current")
_F3NetFlowPointStatsUAS_Type = PerfCounter64
_F3NetFlowPointStatsUAS_Object = MibTableColumn
f3NetFlowPointStatsUAS = _F3NetFlowPointStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 8),
    _F3NetFlowPointStatsUAS_Type()
)
f3NetFlowPointStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsUAS.setStatus("current")
_F3NetFlowPointStatsSES_Type = PerfCounter64
_F3NetFlowPointStatsSES_Object = MibTableColumn
f3NetFlowPointStatsSES = _F3NetFlowPointStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 9),
    _F3NetFlowPointStatsSES_Type()
)
f3NetFlowPointStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsSES.setStatus("current")
_F3NetFlowPointStatsFMG_Type = PerfCounter64
_F3NetFlowPointStatsFMG_Object = MibTableColumn
f3NetFlowPointStatsFMG = _F3NetFlowPointStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 10),
    _F3NetFlowPointStatsFMG_Type()
)
f3NetFlowPointStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFMG.setStatus("current")
_F3NetFlowPointStatsFMY_Type = PerfCounter64
_F3NetFlowPointStatsFMY_Object = MibTableColumn
f3NetFlowPointStatsFMY = _F3NetFlowPointStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 11),
    _F3NetFlowPointStatsFMY_Type()
)
f3NetFlowPointStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFMY.setStatus("current")
_F3NetFlowPointStatsFMRD_Type = PerfCounter64
_F3NetFlowPointStatsFMRD_Object = MibTableColumn
f3NetFlowPointStatsFMRD = _F3NetFlowPointStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 12),
    _F3NetFlowPointStatsFMRD_Type()
)
f3NetFlowPointStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFMRD.setStatus("current")
_F3NetFlowPointStatsFTD_Type = PerfCounter64
_F3NetFlowPointStatsFTD_Object = MibTableColumn
f3NetFlowPointStatsFTD = _F3NetFlowPointStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 13),
    _F3NetFlowPointStatsFTD_Type()
)
f3NetFlowPointStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFTD.setStatus("current")
_F3NetFlowPointStatsBytesIn_Type = PerfCounter64
_F3NetFlowPointStatsBytesIn_Object = MibTableColumn
f3NetFlowPointStatsBytesIn = _F3NetFlowPointStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 14),
    _F3NetFlowPointStatsBytesIn_Type()
)
f3NetFlowPointStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsBytesIn.setStatus("current")
_F3NetFlowPointStatsBytesOut_Type = PerfCounter64
_F3NetFlowPointStatsBytesOut_Object = MibTableColumn
f3NetFlowPointStatsBytesOut = _F3NetFlowPointStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 15),
    _F3NetFlowPointStatsBytesOut_Type()
)
f3NetFlowPointStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsBytesOut.setStatus("current")
_F3NetFlowPointStatsIBRMax_Type = PerfCounter64
_F3NetFlowPointStatsIBRMax_Object = MibTableColumn
f3NetFlowPointStatsIBRMax = _F3NetFlowPointStatsIBRMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 16),
    _F3NetFlowPointStatsIBRMax_Type()
)
f3NetFlowPointStatsIBRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsIBRMax.setStatus("current")
_F3NetFlowPointStatsIBRRlMax_Type = PerfCounter64
_F3NetFlowPointStatsIBRRlMax_Object = MibTableColumn
f3NetFlowPointStatsIBRRlMax = _F3NetFlowPointStatsIBRRlMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 17),
    _F3NetFlowPointStatsIBRRlMax_Type()
)
f3NetFlowPointStatsIBRRlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsIBRRlMax.setStatus("current")
_F3NetFlowPointStatsIBRMin_Type = PerfCounter64
_F3NetFlowPointStatsIBRMin_Object = MibTableColumn
f3NetFlowPointStatsIBRMin = _F3NetFlowPointStatsIBRMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 18),
    _F3NetFlowPointStatsIBRMin_Type()
)
f3NetFlowPointStatsIBRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsIBRMin.setStatus("current")
_F3NetFlowPointStatsIBRRlMin_Type = PerfCounter64
_F3NetFlowPointStatsIBRRlMin_Object = MibTableColumn
f3NetFlowPointStatsIBRRlMin = _F3NetFlowPointStatsIBRRlMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 19),
    _F3NetFlowPointStatsIBRRlMin_Type()
)
f3NetFlowPointStatsIBRRlMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsIBRRlMin.setStatus("current")
_F3NetFlowPointStatsIBR_Type = PerfCounter64
_F3NetFlowPointStatsIBR_Object = MibTableColumn
f3NetFlowPointStatsIBR = _F3NetFlowPointStatsIBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 20),
    _F3NetFlowPointStatsIBR_Type()
)
f3NetFlowPointStatsIBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsIBR.setStatus("current")
_F3NetFlowPointStatsIBRRl_Type = PerfCounter64
_F3NetFlowPointStatsIBRRl_Object = MibTableColumn
f3NetFlowPointStatsIBRRl = _F3NetFlowPointStatsIBRRl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 21),
    _F3NetFlowPointStatsIBRRl_Type()
)
f3NetFlowPointStatsIBRRl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsIBRRl.setStatus("current")
_F3NetFlowPointStatsFBCD_Type = PerfCounter64
_F3NetFlowPointStatsFBCD_Object = MibTableColumn
f3NetFlowPointStatsFBCD = _F3NetFlowPointStatsFBCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 22),
    _F3NetFlowPointStatsFBCD_Type()
)
f3NetFlowPointStatsFBCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFBCD.setStatus("current")
_F3NetFlowPointStatsFMCD_Type = PerfCounter64
_F3NetFlowPointStatsFMCD_Object = MibTableColumn
f3NetFlowPointStatsFMCD = _F3NetFlowPointStatsFMCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 23),
    _F3NetFlowPointStatsFMCD_Type()
)
f3NetFlowPointStatsFMCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFMCD.setStatus("current")
_F3NetFlowPointStatsFdRxFb_Type = PerfCounter64
_F3NetFlowPointStatsFdRxFb_Object = MibTableColumn
f3NetFlowPointStatsFdRxFb = _F3NetFlowPointStatsFdRxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 24),
    _F3NetFlowPointStatsFdRxFb_Type()
)
f3NetFlowPointStatsFdRxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFdRxFb.setStatus("current")
_F3NetFlowPointStatsFdTxFb_Type = PerfCounter64
_F3NetFlowPointStatsFdTxFb_Object = MibTableColumn
f3NetFlowPointStatsFdTxFb = _F3NetFlowPointStatsFdTxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 25),
    _F3NetFlowPointStatsFdTxFb_Type()
)
f3NetFlowPointStatsFdTxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFdTxFb.setStatus("current")
_F3NetFlowPointStatsFdicd_Type = PerfCounter64
_F3NetFlowPointStatsFdicd_Object = MibTableColumn
f3NetFlowPointStatsFdicd = _F3NetFlowPointStatsFdicd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 26),
    _F3NetFlowPointStatsFdicd_Type()
)
f3NetFlowPointStatsFdicd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsFdicd.setStatus("current")
_F3NetFlowPointStatsNumLearnTableFlushes_Type = PerfCounter64
_F3NetFlowPointStatsNumLearnTableFlushes_Object = MibTableColumn
f3NetFlowPointStatsNumLearnTableFlushes = _F3NetFlowPointStatsNumLearnTableFlushes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 2, 1, 27),
    _F3NetFlowPointStatsNumLearnTableFlushes_Type()
)
f3NetFlowPointStatsNumLearnTableFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointStatsNumLearnTableFlushes.setStatus("current")
_F3AccFlowPointHistoryTable_Object = MibTable
f3AccFlowPointHistoryTable = _F3AccFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3)
)
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryTable.setStatus("current")
_F3AccFlowPointHistoryEntry_Object = MibTableRow
f3AccFlowPointHistoryEntry = _F3AccFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1)
)
f3AccFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointStatsIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryEntry.setStatus("current")


class _F3AccFlowPointHistoryIndex_Type(Integer32):
    """Custom type f3AccFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3AccFlowPointHistoryIndex_Object = MibTableColumn
f3AccFlowPointHistoryIndex = _F3AccFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 1),
    _F3AccFlowPointHistoryIndex_Type()
)
f3AccFlowPointHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryIndex.setStatus("current")
_F3AccFlowPointHistoryTime_Type = DateAndTime
_F3AccFlowPointHistoryTime_Object = MibTableColumn
f3AccFlowPointHistoryTime = _F3AccFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 2),
    _F3AccFlowPointHistoryTime_Type()
)
f3AccFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryTime.setStatus("current")
_F3AccFlowPointHistoryValid_Type = TruthValue
_F3AccFlowPointHistoryValid_Object = MibTableColumn
f3AccFlowPointHistoryValid = _F3AccFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 3),
    _F3AccFlowPointHistoryValid_Type()
)
f3AccFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryValid.setStatus("current")
_F3AccFlowPointHistoryAction_Type = CmPmBinAction
_F3AccFlowPointHistoryAction_Object = MibTableColumn
f3AccFlowPointHistoryAction = _F3AccFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 4),
    _F3AccFlowPointHistoryAction_Type()
)
f3AccFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryAction.setStatus("current")
_F3AccFlowPointHistoryL2CPFD_Type = PerfCounter64
_F3AccFlowPointHistoryL2CPFD_Object = MibTableColumn
f3AccFlowPointHistoryL2CPFD = _F3AccFlowPointHistoryL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 5),
    _F3AccFlowPointHistoryL2CPFD_Type()
)
f3AccFlowPointHistoryL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryL2CPFD.setStatus("current")
_F3AccFlowPointHistoryABRRx_Type = PerfCounter64
_F3AccFlowPointHistoryABRRx_Object = MibTableColumn
f3AccFlowPointHistoryABRRx = _F3AccFlowPointHistoryABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 6),
    _F3AccFlowPointHistoryABRRx_Type()
)
f3AccFlowPointHistoryABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryABRRx.setStatus("current")
_F3AccFlowPointHistoryABRRLRx_Type = PerfCounter64
_F3AccFlowPointHistoryABRRLRx_Object = MibTableColumn
f3AccFlowPointHistoryABRRLRx = _F3AccFlowPointHistoryABRRLRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 7),
    _F3AccFlowPointHistoryABRRLRx_Type()
)
f3AccFlowPointHistoryABRRLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryABRRLRx.setStatus("current")
_F3AccFlowPointHistoryUAS_Type = PerfCounter64
_F3AccFlowPointHistoryUAS_Object = MibTableColumn
f3AccFlowPointHistoryUAS = _F3AccFlowPointHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 8),
    _F3AccFlowPointHistoryUAS_Type()
)
f3AccFlowPointHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryUAS.setStatus("current")
_F3AccFlowPointHistorySES_Type = PerfCounter64
_F3AccFlowPointHistorySES_Object = MibTableColumn
f3AccFlowPointHistorySES = _F3AccFlowPointHistorySES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 9),
    _F3AccFlowPointHistorySES_Type()
)
f3AccFlowPointHistorySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistorySES.setStatus("current")
_F3AccFlowPointHistoryFMG_Type = PerfCounter64
_F3AccFlowPointHistoryFMG_Object = MibTableColumn
f3AccFlowPointHistoryFMG = _F3AccFlowPointHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 10),
    _F3AccFlowPointHistoryFMG_Type()
)
f3AccFlowPointHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFMG.setStatus("current")
_F3AccFlowPointHistoryFMY_Type = PerfCounter64
_F3AccFlowPointHistoryFMY_Object = MibTableColumn
f3AccFlowPointHistoryFMY = _F3AccFlowPointHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 11),
    _F3AccFlowPointHistoryFMY_Type()
)
f3AccFlowPointHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFMY.setStatus("current")
_F3AccFlowPointHistoryFMRD_Type = PerfCounter64
_F3AccFlowPointHistoryFMRD_Object = MibTableColumn
f3AccFlowPointHistoryFMRD = _F3AccFlowPointHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 12),
    _F3AccFlowPointHistoryFMRD_Type()
)
f3AccFlowPointHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFMRD.setStatus("current")
_F3AccFlowPointHistoryFTD_Type = PerfCounter64
_F3AccFlowPointHistoryFTD_Object = MibTableColumn
f3AccFlowPointHistoryFTD = _F3AccFlowPointHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 13),
    _F3AccFlowPointHistoryFTD_Type()
)
f3AccFlowPointHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFTD.setStatus("current")
_F3AccFlowPointHistoryBytesIn_Type = PerfCounter64
_F3AccFlowPointHistoryBytesIn_Object = MibTableColumn
f3AccFlowPointHistoryBytesIn = _F3AccFlowPointHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 14),
    _F3AccFlowPointHistoryBytesIn_Type()
)
f3AccFlowPointHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryBytesIn.setStatus("current")
_F3AccFlowPointHistoryBytesOut_Type = PerfCounter64
_F3AccFlowPointHistoryBytesOut_Object = MibTableColumn
f3AccFlowPointHistoryBytesOut = _F3AccFlowPointHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 15),
    _F3AccFlowPointHistoryBytesOut_Type()
)
f3AccFlowPointHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryBytesOut.setStatus("current")
_F3AccFlowPointHistoryIBRMax_Type = PerfCounter64
_F3AccFlowPointHistoryIBRMax_Object = MibTableColumn
f3AccFlowPointHistoryIBRMax = _F3AccFlowPointHistoryIBRMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 16),
    _F3AccFlowPointHistoryIBRMax_Type()
)
f3AccFlowPointHistoryIBRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryIBRMax.setStatus("current")
_F3AccFlowPointHistoryIBRRlMax_Type = PerfCounter64
_F3AccFlowPointHistoryIBRRlMax_Object = MibTableColumn
f3AccFlowPointHistoryIBRRlMax = _F3AccFlowPointHistoryIBRRlMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 17),
    _F3AccFlowPointHistoryIBRRlMax_Type()
)
f3AccFlowPointHistoryIBRRlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryIBRRlMax.setStatus("current")
_F3AccFlowPointHistoryIBRMin_Type = PerfCounter64
_F3AccFlowPointHistoryIBRMin_Object = MibTableColumn
f3AccFlowPointHistoryIBRMin = _F3AccFlowPointHistoryIBRMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 18),
    _F3AccFlowPointHistoryIBRMin_Type()
)
f3AccFlowPointHistoryIBRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryIBRMin.setStatus("current")
_F3AccFlowPointHistoryIBRRlMin_Type = PerfCounter64
_F3AccFlowPointHistoryIBRRlMin_Object = MibTableColumn
f3AccFlowPointHistoryIBRRlMin = _F3AccFlowPointHistoryIBRRlMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 19),
    _F3AccFlowPointHistoryIBRRlMin_Type()
)
f3AccFlowPointHistoryIBRRlMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryIBRRlMin.setStatus("current")
_F3AccFlowPointHistoryIBR_Type = PerfCounter64
_F3AccFlowPointHistoryIBR_Object = MibTableColumn
f3AccFlowPointHistoryIBR = _F3AccFlowPointHistoryIBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 20),
    _F3AccFlowPointHistoryIBR_Type()
)
f3AccFlowPointHistoryIBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryIBR.setStatus("current")
_F3AccFlowPointHistoryIBRRl_Type = PerfCounter64
_F3AccFlowPointHistoryIBRRl_Object = MibTableColumn
f3AccFlowPointHistoryIBRRl = _F3AccFlowPointHistoryIBRRl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 21),
    _F3AccFlowPointHistoryIBRRl_Type()
)
f3AccFlowPointHistoryIBRRl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryIBRRl.setStatus("current")
_F3AccFlowPointHistoryFBCD_Type = PerfCounter64
_F3AccFlowPointHistoryFBCD_Object = MibTableColumn
f3AccFlowPointHistoryFBCD = _F3AccFlowPointHistoryFBCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 22),
    _F3AccFlowPointHistoryFBCD_Type()
)
f3AccFlowPointHistoryFBCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFBCD.setStatus("current")
_F3AccFlowPointHistoryFMCD_Type = PerfCounter64
_F3AccFlowPointHistoryFMCD_Object = MibTableColumn
f3AccFlowPointHistoryFMCD = _F3AccFlowPointHistoryFMCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 23),
    _F3AccFlowPointHistoryFMCD_Type()
)
f3AccFlowPointHistoryFMCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFMCD.setStatus("current")
_F3AccFlowPointHistoryFdRxFb_Type = PerfCounter64
_F3AccFlowPointHistoryFdRxFb_Object = MibTableColumn
f3AccFlowPointHistoryFdRxFb = _F3AccFlowPointHistoryFdRxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 24),
    _F3AccFlowPointHistoryFdRxFb_Type()
)
f3AccFlowPointHistoryFdRxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFdRxFb.setStatus("current")
_F3AccFlowPointHistoryFdTxFb_Type = PerfCounter64
_F3AccFlowPointHistoryFdTxFb_Object = MibTableColumn
f3AccFlowPointHistoryFdTxFb = _F3AccFlowPointHistoryFdTxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 25),
    _F3AccFlowPointHistoryFdTxFb_Type()
)
f3AccFlowPointHistoryFdTxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFdTxFb.setStatus("current")
_F3AccFlowPointHistoryFdicd_Type = PerfCounter64
_F3AccFlowPointHistoryFdicd_Object = MibTableColumn
f3AccFlowPointHistoryFdicd = _F3AccFlowPointHistoryFdicd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 26),
    _F3AccFlowPointHistoryFdicd_Type()
)
f3AccFlowPointHistoryFdicd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryFdicd.setStatus("current")
_F3AccFlowPointHistoryNumLearnTableFlushes_Type = PerfCounter64
_F3AccFlowPointHistoryNumLearnTableFlushes_Object = MibTableColumn
f3AccFlowPointHistoryNumLearnTableFlushes = _F3AccFlowPointHistoryNumLearnTableFlushes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 3, 1, 27),
    _F3AccFlowPointHistoryNumLearnTableFlushes_Type()
)
f3AccFlowPointHistoryNumLearnTableFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointHistoryNumLearnTableFlushes.setStatus("current")
_F3NetFlowPointHistoryTable_Object = MibTable
f3NetFlowPointHistoryTable = _F3NetFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4)
)
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryTable.setStatus("current")
_F3NetFlowPointHistoryEntry_Object = MibTableRow
f3NetFlowPointHistoryEntry = _F3NetFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1)
)
f3NetFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointStatsIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryEntry.setStatus("current")


class _F3NetFlowPointHistoryIndex_Type(Integer32):
    """Custom type f3NetFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3NetFlowPointHistoryIndex_Object = MibTableColumn
f3NetFlowPointHistoryIndex = _F3NetFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 1),
    _F3NetFlowPointHistoryIndex_Type()
)
f3NetFlowPointHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryIndex.setStatus("current")
_F3NetFlowPointHistoryTime_Type = DateAndTime
_F3NetFlowPointHistoryTime_Object = MibTableColumn
f3NetFlowPointHistoryTime = _F3NetFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 2),
    _F3NetFlowPointHistoryTime_Type()
)
f3NetFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryTime.setStatus("current")
_F3NetFlowPointHistoryValid_Type = TruthValue
_F3NetFlowPointHistoryValid_Object = MibTableColumn
f3NetFlowPointHistoryValid = _F3NetFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 3),
    _F3NetFlowPointHistoryValid_Type()
)
f3NetFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryValid.setStatus("current")
_F3NetFlowPointHistoryAction_Type = CmPmBinAction
_F3NetFlowPointHistoryAction_Object = MibTableColumn
f3NetFlowPointHistoryAction = _F3NetFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 4),
    _F3NetFlowPointHistoryAction_Type()
)
f3NetFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryAction.setStatus("current")
_F3NetFlowPointHistoryL2CPFD_Type = PerfCounter64
_F3NetFlowPointHistoryL2CPFD_Object = MibTableColumn
f3NetFlowPointHistoryL2CPFD = _F3NetFlowPointHistoryL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 5),
    _F3NetFlowPointHistoryL2CPFD_Type()
)
f3NetFlowPointHistoryL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryL2CPFD.setStatus("current")
_F3NetFlowPointHistoryABRRx_Type = PerfCounter64
_F3NetFlowPointHistoryABRRx_Object = MibTableColumn
f3NetFlowPointHistoryABRRx = _F3NetFlowPointHistoryABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 6),
    _F3NetFlowPointHistoryABRRx_Type()
)
f3NetFlowPointHistoryABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryABRRx.setStatus("current")
_F3NetFlowPointHistoryABRRLRx_Type = PerfCounter64
_F3NetFlowPointHistoryABRRLRx_Object = MibTableColumn
f3NetFlowPointHistoryABRRLRx = _F3NetFlowPointHistoryABRRLRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 7),
    _F3NetFlowPointHistoryABRRLRx_Type()
)
f3NetFlowPointHistoryABRRLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryABRRLRx.setStatus("current")
_F3NetFlowPointHistoryUAS_Type = PerfCounter64
_F3NetFlowPointHistoryUAS_Object = MibTableColumn
f3NetFlowPointHistoryUAS = _F3NetFlowPointHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 8),
    _F3NetFlowPointHistoryUAS_Type()
)
f3NetFlowPointHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryUAS.setStatus("current")
_F3NetFlowPointHistorySES_Type = PerfCounter64
_F3NetFlowPointHistorySES_Object = MibTableColumn
f3NetFlowPointHistorySES = _F3NetFlowPointHistorySES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 9),
    _F3NetFlowPointHistorySES_Type()
)
f3NetFlowPointHistorySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistorySES.setStatus("current")
_F3NetFlowPointHistoryFMG_Type = PerfCounter64
_F3NetFlowPointHistoryFMG_Object = MibTableColumn
f3NetFlowPointHistoryFMG = _F3NetFlowPointHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 10),
    _F3NetFlowPointHistoryFMG_Type()
)
f3NetFlowPointHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFMG.setStatus("current")
_F3NetFlowPointHistoryFMY_Type = PerfCounter64
_F3NetFlowPointHistoryFMY_Object = MibTableColumn
f3NetFlowPointHistoryFMY = _F3NetFlowPointHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 11),
    _F3NetFlowPointHistoryFMY_Type()
)
f3NetFlowPointHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFMY.setStatus("current")
_F3NetFlowPointHistoryFMRD_Type = PerfCounter64
_F3NetFlowPointHistoryFMRD_Object = MibTableColumn
f3NetFlowPointHistoryFMRD = _F3NetFlowPointHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 12),
    _F3NetFlowPointHistoryFMRD_Type()
)
f3NetFlowPointHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFMRD.setStatus("current")
_F3NetFlowPointHistoryFTD_Type = PerfCounter64
_F3NetFlowPointHistoryFTD_Object = MibTableColumn
f3NetFlowPointHistoryFTD = _F3NetFlowPointHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 13),
    _F3NetFlowPointHistoryFTD_Type()
)
f3NetFlowPointHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFTD.setStatus("current")
_F3NetFlowPointHistoryBytesIn_Type = PerfCounter64
_F3NetFlowPointHistoryBytesIn_Object = MibTableColumn
f3NetFlowPointHistoryBytesIn = _F3NetFlowPointHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 14),
    _F3NetFlowPointHistoryBytesIn_Type()
)
f3NetFlowPointHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryBytesIn.setStatus("current")
_F3NetFlowPointHistoryBytesOut_Type = PerfCounter64
_F3NetFlowPointHistoryBytesOut_Object = MibTableColumn
f3NetFlowPointHistoryBytesOut = _F3NetFlowPointHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 15),
    _F3NetFlowPointHistoryBytesOut_Type()
)
f3NetFlowPointHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryBytesOut.setStatus("current")
_F3NetFlowPointHistoryIBRMax_Type = PerfCounter64
_F3NetFlowPointHistoryIBRMax_Object = MibTableColumn
f3NetFlowPointHistoryIBRMax = _F3NetFlowPointHistoryIBRMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 16),
    _F3NetFlowPointHistoryIBRMax_Type()
)
f3NetFlowPointHistoryIBRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryIBRMax.setStatus("current")
_F3NetFlowPointHistoryIBRRlMax_Type = PerfCounter64
_F3NetFlowPointHistoryIBRRlMax_Object = MibTableColumn
f3NetFlowPointHistoryIBRRlMax = _F3NetFlowPointHistoryIBRRlMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 17),
    _F3NetFlowPointHistoryIBRRlMax_Type()
)
f3NetFlowPointHistoryIBRRlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryIBRRlMax.setStatus("current")
_F3NetFlowPointHistoryIBRMin_Type = PerfCounter64
_F3NetFlowPointHistoryIBRMin_Object = MibTableColumn
f3NetFlowPointHistoryIBRMin = _F3NetFlowPointHistoryIBRMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 18),
    _F3NetFlowPointHistoryIBRMin_Type()
)
f3NetFlowPointHistoryIBRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryIBRMin.setStatus("current")
_F3NetFlowPointHistoryIBRRlMin_Type = PerfCounter64
_F3NetFlowPointHistoryIBRRlMin_Object = MibTableColumn
f3NetFlowPointHistoryIBRRlMin = _F3NetFlowPointHistoryIBRRlMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 19),
    _F3NetFlowPointHistoryIBRRlMin_Type()
)
f3NetFlowPointHistoryIBRRlMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryIBRRlMin.setStatus("current")
_F3NetFlowPointHistoryIBR_Type = PerfCounter64
_F3NetFlowPointHistoryIBR_Object = MibTableColumn
f3NetFlowPointHistoryIBR = _F3NetFlowPointHistoryIBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 20),
    _F3NetFlowPointHistoryIBR_Type()
)
f3NetFlowPointHistoryIBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryIBR.setStatus("current")
_F3NetFlowPointHistoryIBRRl_Type = PerfCounter64
_F3NetFlowPointHistoryIBRRl_Object = MibTableColumn
f3NetFlowPointHistoryIBRRl = _F3NetFlowPointHistoryIBRRl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 21),
    _F3NetFlowPointHistoryIBRRl_Type()
)
f3NetFlowPointHistoryIBRRl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryIBRRl.setStatus("current")
_F3NetFlowPointHistoryFBCD_Type = PerfCounter64
_F3NetFlowPointHistoryFBCD_Object = MibTableColumn
f3NetFlowPointHistoryFBCD = _F3NetFlowPointHistoryFBCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 22),
    _F3NetFlowPointHistoryFBCD_Type()
)
f3NetFlowPointHistoryFBCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFBCD.setStatus("current")
_F3NetFlowPointHistoryFMCD_Type = PerfCounter64
_F3NetFlowPointHistoryFMCD_Object = MibTableColumn
f3NetFlowPointHistoryFMCD = _F3NetFlowPointHistoryFMCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 23),
    _F3NetFlowPointHistoryFMCD_Type()
)
f3NetFlowPointHistoryFMCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFMCD.setStatus("current")
_F3NetFlowPointHistoryFdRxFb_Type = PerfCounter64
_F3NetFlowPointHistoryFdRxFb_Object = MibTableColumn
f3NetFlowPointHistoryFdRxFb = _F3NetFlowPointHistoryFdRxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 24),
    _F3NetFlowPointHistoryFdRxFb_Type()
)
f3NetFlowPointHistoryFdRxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFdRxFb.setStatus("current")
_F3NetFlowPointHistoryFdTxFb_Type = PerfCounter64
_F3NetFlowPointHistoryFdTxFb_Object = MibTableColumn
f3NetFlowPointHistoryFdTxFb = _F3NetFlowPointHistoryFdTxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 25),
    _F3NetFlowPointHistoryFdTxFb_Type()
)
f3NetFlowPointHistoryFdTxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFdTxFb.setStatus("current")
_F3NetFlowPointHistoryFdicd_Type = PerfCounter64
_F3NetFlowPointHistoryFdicd_Object = MibTableColumn
f3NetFlowPointHistoryFdicd = _F3NetFlowPointHistoryFdicd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 26),
    _F3NetFlowPointHistoryFdicd_Type()
)
f3NetFlowPointHistoryFdicd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryFdicd.setStatus("current")
_F3NetFlowPointHistoryNumLearnTableFlushes_Type = PerfCounter64
_F3NetFlowPointHistoryNumLearnTableFlushes_Object = MibTableColumn
f3NetFlowPointHistoryNumLearnTableFlushes = _F3NetFlowPointHistoryNumLearnTableFlushes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 4, 1, 27),
    _F3NetFlowPointHistoryNumLearnTableFlushes_Type()
)
f3NetFlowPointHistoryNumLearnTableFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointHistoryNumLearnTableFlushes.setStatus("current")
_F3AccFlowPointThresholdTable_Object = MibTable
f3AccFlowPointThresholdTable = _F3AccFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 5)
)
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdTable.setStatus("current")
_F3AccFlowPointThresholdEntry_Object = MibTableRow
f3AccFlowPointThresholdEntry = _F3AccFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 5, 1)
)
f3AccFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointStatsIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdEntry.setStatus("current")


class _F3AccFlowPointThresholdIndex_Type(Integer32):
    """Custom type f3AccFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3AccFlowPointThresholdIndex_Object = MibTableColumn
f3AccFlowPointThresholdIndex = _F3AccFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 5, 1, 1),
    _F3AccFlowPointThresholdIndex_Type()
)
f3AccFlowPointThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdIndex.setStatus("current")
_F3AccFlowPointThresholdInterval_Type = CmPmIntervalType
_F3AccFlowPointThresholdInterval_Object = MibTableColumn
f3AccFlowPointThresholdInterval = _F3AccFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 5, 1, 2),
    _F3AccFlowPointThresholdInterval_Type()
)
f3AccFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdInterval.setStatus("current")
_F3AccFlowPointThresholdVariable_Type = VariablePointer
_F3AccFlowPointThresholdVariable_Object = MibTableColumn
f3AccFlowPointThresholdVariable = _F3AccFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 5, 1, 3),
    _F3AccFlowPointThresholdVariable_Type()
)
f3AccFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdVariable.setStatus("current")
_F3AccFlowPointThresholdValueLo_Type = Unsigned32
_F3AccFlowPointThresholdValueLo_Object = MibTableColumn
f3AccFlowPointThresholdValueLo = _F3AccFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 5, 1, 4),
    _F3AccFlowPointThresholdValueLo_Type()
)
f3AccFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdValueLo.setStatus("current")
_F3AccFlowPointThresholdValueHi_Type = Unsigned32
_F3AccFlowPointThresholdValueHi_Object = MibTableColumn
f3AccFlowPointThresholdValueHi = _F3AccFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 5, 1, 5),
    _F3AccFlowPointThresholdValueHi_Type()
)
f3AccFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdValueHi.setStatus("current")
_F3AccFlowPointThresholdMonValue_Type = Counter64
_F3AccFlowPointThresholdMonValue_Object = MibTableColumn
f3AccFlowPointThresholdMonValue = _F3AccFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 5, 1, 6),
    _F3AccFlowPointThresholdMonValue_Type()
)
f3AccFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdMonValue.setStatus("current")
_F3NetFlowPointThresholdTable_Object = MibTable
f3NetFlowPointThresholdTable = _F3NetFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 6)
)
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdTable.setStatus("current")
_F3NetFlowPointThresholdEntry_Object = MibTableRow
f3NetFlowPointThresholdEntry = _F3NetFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 6, 1)
)
f3NetFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointStatsIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdEntry.setStatus("current")


class _F3NetFlowPointThresholdIndex_Type(Integer32):
    """Custom type f3NetFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3NetFlowPointThresholdIndex_Object = MibTableColumn
f3NetFlowPointThresholdIndex = _F3NetFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 6, 1, 1),
    _F3NetFlowPointThresholdIndex_Type()
)
f3NetFlowPointThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdIndex.setStatus("current")
_F3NetFlowPointThresholdInterval_Type = CmPmIntervalType
_F3NetFlowPointThresholdInterval_Object = MibTableColumn
f3NetFlowPointThresholdInterval = _F3NetFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 6, 1, 2),
    _F3NetFlowPointThresholdInterval_Type()
)
f3NetFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdInterval.setStatus("current")
_F3NetFlowPointThresholdVariable_Type = VariablePointer
_F3NetFlowPointThresholdVariable_Object = MibTableColumn
f3NetFlowPointThresholdVariable = _F3NetFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 6, 1, 3),
    _F3NetFlowPointThresholdVariable_Type()
)
f3NetFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdVariable.setStatus("current")
_F3NetFlowPointThresholdValueLo_Type = Unsigned32
_F3NetFlowPointThresholdValueLo_Object = MibTableColumn
f3NetFlowPointThresholdValueLo = _F3NetFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 6, 1, 4),
    _F3NetFlowPointThresholdValueLo_Type()
)
f3NetFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdValueLo.setStatus("current")
_F3NetFlowPointThresholdValueHi_Type = Unsigned32
_F3NetFlowPointThresholdValueHi_Object = MibTableColumn
f3NetFlowPointThresholdValueHi = _F3NetFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 6, 1, 5),
    _F3NetFlowPointThresholdValueHi_Type()
)
f3NetFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdValueHi.setStatus("current")
_F3NetFlowPointThresholdMonValue_Type = Counter64
_F3NetFlowPointThresholdMonValue_Object = MibTableColumn
f3NetFlowPointThresholdMonValue = _F3NetFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 6, 1, 6),
    _F3NetFlowPointThresholdMonValue_Type()
)
f3NetFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdMonValue.setStatus("current")
_F3MPFlowStatsTable_Object = MibTable
f3MPFlowStatsTable = _F3MPFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7)
)
if mibBuilder.loadTexts:
    f3MPFlowStatsTable.setStatus("current")
_F3MPFlowStatsEntry_Object = MibTableRow
f3MPFlowStatsEntry = _F3MPFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1)
)
f3MPFlowStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-FACILITY-MIB", "cmMPFlowIndex"),
    (0, "F3-FPM-MIB", "f3MPFlowStatsIndex"),
)
if mibBuilder.loadTexts:
    f3MPFlowStatsEntry.setStatus("current")


class _F3MPFlowStatsIndex_Type(Integer32):
    """Custom type f3MPFlowStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3MPFlowStatsIndex_Type.__name__ = "Integer32"
_F3MPFlowStatsIndex_Object = MibTableColumn
f3MPFlowStatsIndex = _F3MPFlowStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1, 1),
    _F3MPFlowStatsIndex_Type()
)
f3MPFlowStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStatsIndex.setStatus("current")
_F3MPFlowStatsIntervalType_Type = CmPmIntervalType
_F3MPFlowStatsIntervalType_Object = MibTableColumn
f3MPFlowStatsIntervalType = _F3MPFlowStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1, 2),
    _F3MPFlowStatsIntervalType_Type()
)
f3MPFlowStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStatsIntervalType.setStatus("current")
_F3MPFlowStatsValid_Type = TruthValue
_F3MPFlowStatsValid_Object = MibTableColumn
f3MPFlowStatsValid = _F3MPFlowStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1, 3),
    _F3MPFlowStatsValid_Type()
)
f3MPFlowStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStatsValid.setStatus("current")
_F3MPFlowStatsAction_Type = CmPmBinAction
_F3MPFlowStatsAction_Object = MibTableColumn
f3MPFlowStatsAction = _F3MPFlowStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1, 4),
    _F3MPFlowStatsAction_Type()
)
f3MPFlowStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MPFlowStatsAction.setStatus("current")
_F3MPFlowStatsFDStaticBlock_Type = PerfCounter64
_F3MPFlowStatsFDStaticBlock_Object = MibTableColumn
f3MPFlowStatsFDStaticBlock = _F3MPFlowStatsFDStaticBlock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1, 5),
    _F3MPFlowStatsFDStaticBlock_Type()
)
f3MPFlowStatsFDStaticBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStatsFDStaticBlock.setStatus("current")
_F3MPFlowStatsFDHairPin_Type = PerfCounter64
_F3MPFlowStatsFDHairPin_Object = MibTableColumn
f3MPFlowStatsFDHairPin = _F3MPFlowStatsFDHairPin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1, 6),
    _F3MPFlowStatsFDHairPin_Type()
)
f3MPFlowStatsFDHairPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStatsFDHairPin.setStatus("current")
_F3MPFlowStatsMacTableDiscards_Type = PerfCounter64
_F3MPFlowStatsMacTableDiscards_Object = MibTableColumn
f3MPFlowStatsMacTableDiscards = _F3MPFlowStatsMacTableDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1, 7),
    _F3MPFlowStatsMacTableDiscards_Type()
)
f3MPFlowStatsMacTableDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStatsMacTableDiscards.setStatus("current")
_F3MPFlowStatsFDProtLearn_Type = PerfCounter64
_F3MPFlowStatsFDProtLearn_Object = MibTableColumn
f3MPFlowStatsFDProtLearn = _F3MPFlowStatsFDProtLearn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 7, 1, 8),
    _F3MPFlowStatsFDProtLearn_Type()
)
f3MPFlowStatsFDProtLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStatsFDProtLearn.setStatus("current")
_F3MPFlowHistoryTable_Object = MibTable
f3MPFlowHistoryTable = _F3MPFlowHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8)
)
if mibBuilder.loadTexts:
    f3MPFlowHistoryTable.setStatus("current")
_F3MPFlowHistoryEntry_Object = MibTableRow
f3MPFlowHistoryEntry = _F3MPFlowHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1)
)
f3MPFlowHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-FACILITY-MIB", "cmMPFlowIndex"),
    (0, "F3-FPM-MIB", "f3MPFlowStatsIndex"),
    (0, "F3-FPM-MIB", "f3MPFlowHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3MPFlowHistoryEntry.setStatus("current")


class _F3MPFlowHistoryIndex_Type(Integer32):
    """Custom type f3MPFlowHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3MPFlowHistoryIndex_Type.__name__ = "Integer32"
_F3MPFlowHistoryIndex_Object = MibTableColumn
f3MPFlowHistoryIndex = _F3MPFlowHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1, 1),
    _F3MPFlowHistoryIndex_Type()
)
f3MPFlowHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowHistoryIndex.setStatus("current")
_F3MPFlowHistoryTime_Type = DateAndTime
_F3MPFlowHistoryTime_Object = MibTableColumn
f3MPFlowHistoryTime = _F3MPFlowHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1, 2),
    _F3MPFlowHistoryTime_Type()
)
f3MPFlowHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowHistoryTime.setStatus("current")
_F3MPFlowHistoryValid_Type = TruthValue
_F3MPFlowHistoryValid_Object = MibTableColumn
f3MPFlowHistoryValid = _F3MPFlowHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1, 3),
    _F3MPFlowHistoryValid_Type()
)
f3MPFlowHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowHistoryValid.setStatus("current")
_F3MPFlowHistoryAction_Type = CmPmBinAction
_F3MPFlowHistoryAction_Object = MibTableColumn
f3MPFlowHistoryAction = _F3MPFlowHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1, 4),
    _F3MPFlowHistoryAction_Type()
)
f3MPFlowHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MPFlowHistoryAction.setStatus("current")
_F3MPFlowHistoryFDStaticBlock_Type = PerfCounter64
_F3MPFlowHistoryFDStaticBlock_Object = MibTableColumn
f3MPFlowHistoryFDStaticBlock = _F3MPFlowHistoryFDStaticBlock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1, 5),
    _F3MPFlowHistoryFDStaticBlock_Type()
)
f3MPFlowHistoryFDStaticBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowHistoryFDStaticBlock.setStatus("current")
_F3MPFlowHistoryFDHairPin_Type = PerfCounter64
_F3MPFlowHistoryFDHairPin_Object = MibTableColumn
f3MPFlowHistoryFDHairPin = _F3MPFlowHistoryFDHairPin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1, 6),
    _F3MPFlowHistoryFDHairPin_Type()
)
f3MPFlowHistoryFDHairPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowHistoryFDHairPin.setStatus("current")
_F3MPFlowHistoryMacTableDiscards_Type = PerfCounter64
_F3MPFlowHistoryMacTableDiscards_Object = MibTableColumn
f3MPFlowHistoryMacTableDiscards = _F3MPFlowHistoryMacTableDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1, 7),
    _F3MPFlowHistoryMacTableDiscards_Type()
)
f3MPFlowHistoryMacTableDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowHistoryMacTableDiscards.setStatus("current")
_F3MPFlowHistoryFDProtLearn_Type = PerfCounter64
_F3MPFlowHistoryFDProtLearn_Object = MibTableColumn
f3MPFlowHistoryFDProtLearn = _F3MPFlowHistoryFDProtLearn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 8, 1, 8),
    _F3MPFlowHistoryFDProtLearn_Type()
)
f3MPFlowHistoryFDProtLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowHistoryFDProtLearn.setStatus("current")
_F3MPFlowThresholdTable_Object = MibTable
f3MPFlowThresholdTable = _F3MPFlowThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 9)
)
if mibBuilder.loadTexts:
    f3MPFlowThresholdTable.setStatus("current")
_F3MPFlowThresholdEntry_Object = MibTableRow
f3MPFlowThresholdEntry = _F3MPFlowThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 9, 1)
)
f3MPFlowThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-FACILITY-MIB", "cmMPFlowIndex"),
    (0, "F3-FPM-MIB", "f3MPFlowStatsIndex"),
    (0, "F3-FPM-MIB", "f3MPFlowThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3MPFlowThresholdEntry.setStatus("current")


class _F3MPFlowThresholdIndex_Type(Integer32):
    """Custom type f3MPFlowThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3MPFlowThresholdIndex_Type.__name__ = "Integer32"
_F3MPFlowThresholdIndex_Object = MibTableColumn
f3MPFlowThresholdIndex = _F3MPFlowThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 9, 1, 1),
    _F3MPFlowThresholdIndex_Type()
)
f3MPFlowThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowThresholdIndex.setStatus("current")
_F3MPFlowThresholdInterval_Type = CmPmIntervalType
_F3MPFlowThresholdInterval_Object = MibTableColumn
f3MPFlowThresholdInterval = _F3MPFlowThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 9, 1, 2),
    _F3MPFlowThresholdInterval_Type()
)
f3MPFlowThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowThresholdInterval.setStatus("current")
_F3MPFlowThresholdVariable_Type = VariablePointer
_F3MPFlowThresholdVariable_Object = MibTableColumn
f3MPFlowThresholdVariable = _F3MPFlowThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 9, 1, 3),
    _F3MPFlowThresholdVariable_Type()
)
f3MPFlowThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowThresholdVariable.setStatus("current")
_F3MPFlowThresholdValueLo_Type = Unsigned32
_F3MPFlowThresholdValueLo_Object = MibTableColumn
f3MPFlowThresholdValueLo = _F3MPFlowThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 9, 1, 4),
    _F3MPFlowThresholdValueLo_Type()
)
f3MPFlowThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MPFlowThresholdValueLo.setStatus("current")
_F3MPFlowThresholdValueHi_Type = Unsigned32
_F3MPFlowThresholdValueHi_Object = MibTableColumn
f3MPFlowThresholdValueHi = _F3MPFlowThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 9, 1, 5),
    _F3MPFlowThresholdValueHi_Type()
)
f3MPFlowThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MPFlowThresholdValueHi.setStatus("current")
_F3MPFlowThresholdMonValue_Type = Counter64
_F3MPFlowThresholdMonValue_Object = MibTableColumn
f3MPFlowThresholdMonValue = _F3MPFlowThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 9, 1, 6),
    _F3MPFlowThresholdMonValue_Type()
)
f3MPFlowThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowThresholdMonValue.setStatus("current")
_F3AccFpQosShaperStatsTable_Object = MibTable
f3AccFpQosShaperStatsTable = _F3AccFpQosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10)
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsTable.setStatus("current")
_F3AccFpQosShaperStatsEntry_Object = MibTableRow
f3AccFpQosShaperStatsEntry = _F3AccFpQosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1)
)
f3AccFpQosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsEntry.setStatus("current")


class _F3AccFpQosShaperStatsIndex_Type(Integer32):
    """Custom type f3AccFpQosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFpQosShaperStatsIndex_Type.__name__ = "Integer32"
_F3AccFpQosShaperStatsIndex_Object = MibTableColumn
f3AccFpQosShaperStatsIndex = _F3AccFpQosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 1),
    _F3AccFpQosShaperStatsIndex_Type()
)
f3AccFpQosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsIndex.setStatus("current")
_F3AccFpQosShaperStatsIntervalType_Type = CmPmIntervalType
_F3AccFpQosShaperStatsIntervalType_Object = MibTableColumn
f3AccFpQosShaperStatsIntervalType = _F3AccFpQosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 2),
    _F3AccFpQosShaperStatsIntervalType_Type()
)
f3AccFpQosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsIntervalType.setStatus("current")
_F3AccFpQosShaperStatsValid_Type = TruthValue
_F3AccFpQosShaperStatsValid_Object = MibTableColumn
f3AccFpQosShaperStatsValid = _F3AccFpQosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 3),
    _F3AccFpQosShaperStatsValid_Type()
)
f3AccFpQosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsValid.setStatus("current")
_F3AccFpQosShaperStatsAction_Type = CmPmBinAction
_F3AccFpQosShaperStatsAction_Object = MibTableColumn
f3AccFpQosShaperStatsAction = _F3AccFpQosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 4),
    _F3AccFpQosShaperStatsAction_Type()
)
f3AccFpQosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsAction.setStatus("current")
_F3AccFpQosShaperStatsBT_Type = PerfCounter64
_F3AccFpQosShaperStatsBT_Object = MibTableColumn
f3AccFpQosShaperStatsBT = _F3AccFpQosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 5),
    _F3AccFpQosShaperStatsBT_Type()
)
f3AccFpQosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsBT.setStatus("current")
_F3AccFpQosShaperStatsBTD_Type = PerfCounter64
_F3AccFpQosShaperStatsBTD_Object = MibTableColumn
f3AccFpQosShaperStatsBTD = _F3AccFpQosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 6),
    _F3AccFpQosShaperStatsBTD_Type()
)
f3AccFpQosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsBTD.setStatus("current")
_F3AccFpQosShaperStatsFD_Type = PerfCounter64
_F3AccFpQosShaperStatsFD_Object = MibTableColumn
f3AccFpQosShaperStatsFD = _F3AccFpQosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 7),
    _F3AccFpQosShaperStatsFD_Type()
)
f3AccFpQosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsFD.setStatus("current")
_F3AccFpQosShaperStatsFTD_Type = PerfCounter64
_F3AccFpQosShaperStatsFTD_Object = MibTableColumn
f3AccFpQosShaperStatsFTD = _F3AccFpQosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 8),
    _F3AccFpQosShaperStatsFTD_Type()
)
f3AccFpQosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsFTD.setStatus("current")
_F3AccFpQosShaperStatsABRRL_Type = PerfCounter64
_F3AccFpQosShaperStatsABRRL_Object = MibTableColumn
f3AccFpQosShaperStatsABRRL = _F3AccFpQosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 9),
    _F3AccFpQosShaperStatsABRRL_Type()
)
f3AccFpQosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsABRRL.setStatus("current")
_F3AccFpQosShaperStatsBREDD_Type = PerfCounter64
_F3AccFpQosShaperStatsBREDD_Object = MibTableColumn
f3AccFpQosShaperStatsBREDD = _F3AccFpQosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 10),
    _F3AccFpQosShaperStatsBREDD_Type()
)
f3AccFpQosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsBREDD.setStatus("current")
_F3AccFpQosShaperStatsFREDD_Type = PerfCounter64
_F3AccFpQosShaperStatsFREDD_Object = MibTableColumn
f3AccFpQosShaperStatsFREDD = _F3AccFpQosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 10, 1, 11),
    _F3AccFpQosShaperStatsFREDD_Type()
)
f3AccFpQosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperStatsFREDD.setStatus("current")
_F3AccFpQosShaperHistoryTable_Object = MibTable
f3AccFpQosShaperHistoryTable = _F3AccFpQosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11)
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryTable.setStatus("current")
_F3AccFpQosShaperHistoryEntry_Object = MibTableRow
f3AccFpQosShaperHistoryEntry = _F3AccFpQosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1)
)
f3AccFpQosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperStatsIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryEntry.setStatus("current")


class _F3AccFpQosShaperHistoryIndex_Type(Integer32):
    """Custom type f3AccFpQosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFpQosShaperHistoryIndex_Type.__name__ = "Integer32"
_F3AccFpQosShaperHistoryIndex_Object = MibTableColumn
f3AccFpQosShaperHistoryIndex = _F3AccFpQosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 1),
    _F3AccFpQosShaperHistoryIndex_Type()
)
f3AccFpQosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryIndex.setStatus("current")
_F3AccFpQosShaperHistoryTime_Type = DateAndTime
_F3AccFpQosShaperHistoryTime_Object = MibTableColumn
f3AccFpQosShaperHistoryTime = _F3AccFpQosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 2),
    _F3AccFpQosShaperHistoryTime_Type()
)
f3AccFpQosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryTime.setStatus("current")
_F3AccFpQosShaperHistoryValid_Type = TruthValue
_F3AccFpQosShaperHistoryValid_Object = MibTableColumn
f3AccFpQosShaperHistoryValid = _F3AccFpQosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 3),
    _F3AccFpQosShaperHistoryValid_Type()
)
f3AccFpQosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryValid.setStatus("current")
_F3AccFpQosShaperHistoryAction_Type = CmPmBinAction
_F3AccFpQosShaperHistoryAction_Object = MibTableColumn
f3AccFpQosShaperHistoryAction = _F3AccFpQosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 4),
    _F3AccFpQosShaperHistoryAction_Type()
)
f3AccFpQosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryAction.setStatus("current")
_F3AccFpQosShaperHistoryBT_Type = PerfCounter64
_F3AccFpQosShaperHistoryBT_Object = MibTableColumn
f3AccFpQosShaperHistoryBT = _F3AccFpQosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 5),
    _F3AccFpQosShaperHistoryBT_Type()
)
f3AccFpQosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryBT.setStatus("current")
_F3AccFpQosShaperHistoryBTD_Type = PerfCounter64
_F3AccFpQosShaperHistoryBTD_Object = MibTableColumn
f3AccFpQosShaperHistoryBTD = _F3AccFpQosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 6),
    _F3AccFpQosShaperHistoryBTD_Type()
)
f3AccFpQosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryBTD.setStatus("current")
_F3AccFpQosShaperHistoryFD_Type = PerfCounter64
_F3AccFpQosShaperHistoryFD_Object = MibTableColumn
f3AccFpQosShaperHistoryFD = _F3AccFpQosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 7),
    _F3AccFpQosShaperHistoryFD_Type()
)
f3AccFpQosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryFD.setStatus("current")
_F3AccFpQosShaperHistoryFTD_Type = PerfCounter64
_F3AccFpQosShaperHistoryFTD_Object = MibTableColumn
f3AccFpQosShaperHistoryFTD = _F3AccFpQosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 8),
    _F3AccFpQosShaperHistoryFTD_Type()
)
f3AccFpQosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryFTD.setStatus("current")
_F3AccFpQosShaperHistoryABRRL_Type = PerfCounter64
_F3AccFpQosShaperHistoryABRRL_Object = MibTableColumn
f3AccFpQosShaperHistoryABRRL = _F3AccFpQosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 9),
    _F3AccFpQosShaperHistoryABRRL_Type()
)
f3AccFpQosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryABRRL.setStatus("current")
_F3AccFpQosShaperHistoryBREDD_Type = PerfCounter64
_F3AccFpQosShaperHistoryBREDD_Object = MibTableColumn
f3AccFpQosShaperHistoryBREDD = _F3AccFpQosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 10),
    _F3AccFpQosShaperHistoryBREDD_Type()
)
f3AccFpQosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryBREDD.setStatus("current")
_F3AccFpQosShaperHistoryFREDD_Type = PerfCounter64
_F3AccFpQosShaperHistoryFREDD_Object = MibTableColumn
f3AccFpQosShaperHistoryFREDD = _F3AccFpQosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 11, 1, 11),
    _F3AccFpQosShaperHistoryFREDD_Type()
)
f3AccFpQosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperHistoryFREDD.setStatus("current")
_F3AccFpQosShaperThresholdTable_Object = MibTable
f3AccFpQosShaperThresholdTable = _F3AccFpQosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 12)
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdTable.setStatus("current")
_F3AccFpQosShaperThresholdEntry_Object = MibTableRow
f3AccFpQosShaperThresholdEntry = _F3AccFpQosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 12, 1)
)
f3AccFpQosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperStatsIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdEntry.setStatus("current")


class _F3AccFpQosShaperThresholdIndex_Type(Integer32):
    """Custom type f3AccFpQosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFpQosShaperThresholdIndex_Type.__name__ = "Integer32"
_F3AccFpQosShaperThresholdIndex_Object = MibTableColumn
f3AccFpQosShaperThresholdIndex = _F3AccFpQosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 12, 1, 1),
    _F3AccFpQosShaperThresholdIndex_Type()
)
f3AccFpQosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdIndex.setStatus("current")
_F3AccFpQosShaperThresholdInterval_Type = CmPmIntervalType
_F3AccFpQosShaperThresholdInterval_Object = MibTableColumn
f3AccFpQosShaperThresholdInterval = _F3AccFpQosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 12, 1, 2),
    _F3AccFpQosShaperThresholdInterval_Type()
)
f3AccFpQosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdInterval.setStatus("current")
_F3AccFpQosShaperThresholdVariable_Type = VariablePointer
_F3AccFpQosShaperThresholdVariable_Object = MibTableColumn
f3AccFpQosShaperThresholdVariable = _F3AccFpQosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 12, 1, 3),
    _F3AccFpQosShaperThresholdVariable_Type()
)
f3AccFpQosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdVariable.setStatus("current")
_F3AccFpQosShaperThresholdValueLo_Type = Unsigned32
_F3AccFpQosShaperThresholdValueLo_Object = MibTableColumn
f3AccFpQosShaperThresholdValueLo = _F3AccFpQosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 12, 1, 4),
    _F3AccFpQosShaperThresholdValueLo_Type()
)
f3AccFpQosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdValueLo.setStatus("current")
_F3AccFpQosShaperThresholdValueHi_Type = Unsigned32
_F3AccFpQosShaperThresholdValueHi_Object = MibTableColumn
f3AccFpQosShaperThresholdValueHi = _F3AccFpQosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 12, 1, 5),
    _F3AccFpQosShaperThresholdValueHi_Type()
)
f3AccFpQosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdValueHi.setStatus("current")
_F3AccFpQosShaperThresholdMonValue_Type = Counter64
_F3AccFpQosShaperThresholdMonValue_Object = MibTableColumn
f3AccFpQosShaperThresholdMonValue = _F3AccFpQosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 12, 1, 6),
    _F3AccFpQosShaperThresholdMonValue_Type()
)
f3AccFpQosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdMonValue.setStatus("current")
_F3NetFpQosShaperStatsTable_Object = MibTable
f3NetFpQosShaperStatsTable = _F3NetFpQosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13)
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsTable.setStatus("current")
_F3NetFpQosShaperStatsEntry_Object = MibTableRow
f3NetFpQosShaperStatsEntry = _F3NetFpQosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1)
)
f3NetFpQosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsEntry.setStatus("current")


class _F3NetFpQosShaperStatsIndex_Type(Integer32):
    """Custom type f3NetFpQosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFpQosShaperStatsIndex_Type.__name__ = "Integer32"
_F3NetFpQosShaperStatsIndex_Object = MibTableColumn
f3NetFpQosShaperStatsIndex = _F3NetFpQosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 1),
    _F3NetFpQosShaperStatsIndex_Type()
)
f3NetFpQosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsIndex.setStatus("current")
_F3NetFpQosShaperStatsIntervalType_Type = CmPmIntervalType
_F3NetFpQosShaperStatsIntervalType_Object = MibTableColumn
f3NetFpQosShaperStatsIntervalType = _F3NetFpQosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 2),
    _F3NetFpQosShaperStatsIntervalType_Type()
)
f3NetFpQosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsIntervalType.setStatus("current")
_F3NetFpQosShaperStatsValid_Type = TruthValue
_F3NetFpQosShaperStatsValid_Object = MibTableColumn
f3NetFpQosShaperStatsValid = _F3NetFpQosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 3),
    _F3NetFpQosShaperStatsValid_Type()
)
f3NetFpQosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsValid.setStatus("current")
_F3NetFpQosShaperStatsAction_Type = CmPmBinAction
_F3NetFpQosShaperStatsAction_Object = MibTableColumn
f3NetFpQosShaperStatsAction = _F3NetFpQosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 4),
    _F3NetFpQosShaperStatsAction_Type()
)
f3NetFpQosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsAction.setStatus("current")
_F3NetFpQosShaperStatsBT_Type = PerfCounter64
_F3NetFpQosShaperStatsBT_Object = MibTableColumn
f3NetFpQosShaperStatsBT = _F3NetFpQosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 5),
    _F3NetFpQosShaperStatsBT_Type()
)
f3NetFpQosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsBT.setStatus("current")
_F3NetFpQosShaperStatsBTD_Type = PerfCounter64
_F3NetFpQosShaperStatsBTD_Object = MibTableColumn
f3NetFpQosShaperStatsBTD = _F3NetFpQosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 6),
    _F3NetFpQosShaperStatsBTD_Type()
)
f3NetFpQosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsBTD.setStatus("current")
_F3NetFpQosShaperStatsFD_Type = PerfCounter64
_F3NetFpQosShaperStatsFD_Object = MibTableColumn
f3NetFpQosShaperStatsFD = _F3NetFpQosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 7),
    _F3NetFpQosShaperStatsFD_Type()
)
f3NetFpQosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsFD.setStatus("current")
_F3NetFpQosShaperStatsFTD_Type = PerfCounter64
_F3NetFpQosShaperStatsFTD_Object = MibTableColumn
f3NetFpQosShaperStatsFTD = _F3NetFpQosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 8),
    _F3NetFpQosShaperStatsFTD_Type()
)
f3NetFpQosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsFTD.setStatus("current")
_F3NetFpQosShaperStatsABRRL_Type = PerfCounter64
_F3NetFpQosShaperStatsABRRL_Object = MibTableColumn
f3NetFpQosShaperStatsABRRL = _F3NetFpQosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 9),
    _F3NetFpQosShaperStatsABRRL_Type()
)
f3NetFpQosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsABRRL.setStatus("current")
_F3NetFpQosShaperStatsBREDD_Type = PerfCounter64
_F3NetFpQosShaperStatsBREDD_Object = MibTableColumn
f3NetFpQosShaperStatsBREDD = _F3NetFpQosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 10),
    _F3NetFpQosShaperStatsBREDD_Type()
)
f3NetFpQosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsBREDD.setStatus("current")
_F3NetFpQosShaperStatsFREDD_Type = PerfCounter64
_F3NetFpQosShaperStatsFREDD_Object = MibTableColumn
f3NetFpQosShaperStatsFREDD = _F3NetFpQosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 13, 1, 11),
    _F3NetFpQosShaperStatsFREDD_Type()
)
f3NetFpQosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperStatsFREDD.setStatus("current")
_F3NetFpQosShaperHistoryTable_Object = MibTable
f3NetFpQosShaperHistoryTable = _F3NetFpQosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14)
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryTable.setStatus("current")
_F3NetFpQosShaperHistoryEntry_Object = MibTableRow
f3NetFpQosShaperHistoryEntry = _F3NetFpQosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1)
)
f3NetFpQosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperStatsIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryEntry.setStatus("current")


class _F3NetFpQosShaperHistoryIndex_Type(Integer32):
    """Custom type f3NetFpQosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFpQosShaperHistoryIndex_Type.__name__ = "Integer32"
_F3NetFpQosShaperHistoryIndex_Object = MibTableColumn
f3NetFpQosShaperHistoryIndex = _F3NetFpQosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 1),
    _F3NetFpQosShaperHistoryIndex_Type()
)
f3NetFpQosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryIndex.setStatus("current")
_F3NetFpQosShaperHistoryTime_Type = DateAndTime
_F3NetFpQosShaperHistoryTime_Object = MibTableColumn
f3NetFpQosShaperHistoryTime = _F3NetFpQosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 2),
    _F3NetFpQosShaperHistoryTime_Type()
)
f3NetFpQosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryTime.setStatus("current")
_F3NetFpQosShaperHistoryValid_Type = TruthValue
_F3NetFpQosShaperHistoryValid_Object = MibTableColumn
f3NetFpQosShaperHistoryValid = _F3NetFpQosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 3),
    _F3NetFpQosShaperHistoryValid_Type()
)
f3NetFpQosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryValid.setStatus("current")
_F3NetFpQosShaperHistoryAction_Type = CmPmBinAction
_F3NetFpQosShaperHistoryAction_Object = MibTableColumn
f3NetFpQosShaperHistoryAction = _F3NetFpQosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 4),
    _F3NetFpQosShaperHistoryAction_Type()
)
f3NetFpQosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryAction.setStatus("current")
_F3NetFpQosShaperHistoryBT_Type = PerfCounter64
_F3NetFpQosShaperHistoryBT_Object = MibTableColumn
f3NetFpQosShaperHistoryBT = _F3NetFpQosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 5),
    _F3NetFpQosShaperHistoryBT_Type()
)
f3NetFpQosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryBT.setStatus("current")
_F3NetFpQosShaperHistoryBTD_Type = PerfCounter64
_F3NetFpQosShaperHistoryBTD_Object = MibTableColumn
f3NetFpQosShaperHistoryBTD = _F3NetFpQosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 6),
    _F3NetFpQosShaperHistoryBTD_Type()
)
f3NetFpQosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryBTD.setStatus("current")
_F3NetFpQosShaperHistoryFD_Type = PerfCounter64
_F3NetFpQosShaperHistoryFD_Object = MibTableColumn
f3NetFpQosShaperHistoryFD = _F3NetFpQosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 7),
    _F3NetFpQosShaperHistoryFD_Type()
)
f3NetFpQosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryFD.setStatus("current")
_F3NetFpQosShaperHistoryFTD_Type = PerfCounter64
_F3NetFpQosShaperHistoryFTD_Object = MibTableColumn
f3NetFpQosShaperHistoryFTD = _F3NetFpQosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 8),
    _F3NetFpQosShaperHistoryFTD_Type()
)
f3NetFpQosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryFTD.setStatus("current")
_F3NetFpQosShaperHistoryABRRL_Type = PerfCounter64
_F3NetFpQosShaperHistoryABRRL_Object = MibTableColumn
f3NetFpQosShaperHistoryABRRL = _F3NetFpQosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 9),
    _F3NetFpQosShaperHistoryABRRL_Type()
)
f3NetFpQosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryABRRL.setStatus("current")
_F3NetFpQosShaperHistoryBREDD_Type = PerfCounter64
_F3NetFpQosShaperHistoryBREDD_Object = MibTableColumn
f3NetFpQosShaperHistoryBREDD = _F3NetFpQosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 10),
    _F3NetFpQosShaperHistoryBREDD_Type()
)
f3NetFpQosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryBREDD.setStatus("current")
_F3NetFpQosShaperHistoryFREDD_Type = PerfCounter64
_F3NetFpQosShaperHistoryFREDD_Object = MibTableColumn
f3NetFpQosShaperHistoryFREDD = _F3NetFpQosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 14, 1, 11),
    _F3NetFpQosShaperHistoryFREDD_Type()
)
f3NetFpQosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperHistoryFREDD.setStatus("current")
_F3NetFpQosShaperThresholdTable_Object = MibTable
f3NetFpQosShaperThresholdTable = _F3NetFpQosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 15)
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdTable.setStatus("current")
_F3NetFpQosShaperThresholdEntry_Object = MibTableRow
f3NetFpQosShaperThresholdEntry = _F3NetFpQosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 15, 1)
)
f3NetFpQosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperStatsIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdEntry.setStatus("current")


class _F3NetFpQosShaperThresholdIndex_Type(Integer32):
    """Custom type f3NetFpQosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFpQosShaperThresholdIndex_Type.__name__ = "Integer32"
_F3NetFpQosShaperThresholdIndex_Object = MibTableColumn
f3NetFpQosShaperThresholdIndex = _F3NetFpQosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 15, 1, 1),
    _F3NetFpQosShaperThresholdIndex_Type()
)
f3NetFpQosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdIndex.setStatus("current")
_F3NetFpQosShaperThresholdInterval_Type = CmPmIntervalType
_F3NetFpQosShaperThresholdInterval_Object = MibTableColumn
f3NetFpQosShaperThresholdInterval = _F3NetFpQosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 15, 1, 2),
    _F3NetFpQosShaperThresholdInterval_Type()
)
f3NetFpQosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdInterval.setStatus("current")
_F3NetFpQosShaperThresholdVariable_Type = VariablePointer
_F3NetFpQosShaperThresholdVariable_Object = MibTableColumn
f3NetFpQosShaperThresholdVariable = _F3NetFpQosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 15, 1, 3),
    _F3NetFpQosShaperThresholdVariable_Type()
)
f3NetFpQosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdVariable.setStatus("current")
_F3NetFpQosShaperThresholdValueLo_Type = Unsigned32
_F3NetFpQosShaperThresholdValueLo_Object = MibTableColumn
f3NetFpQosShaperThresholdValueLo = _F3NetFpQosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 15, 1, 4),
    _F3NetFpQosShaperThresholdValueLo_Type()
)
f3NetFpQosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdValueLo.setStatus("current")
_F3NetFpQosShaperThresholdValueHi_Type = Unsigned32
_F3NetFpQosShaperThresholdValueHi_Object = MibTableColumn
f3NetFpQosShaperThresholdValueHi = _F3NetFpQosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 15, 1, 5),
    _F3NetFpQosShaperThresholdValueHi_Type()
)
f3NetFpQosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdValueHi.setStatus("current")
_F3NetFpQosShaperThresholdMonValue_Type = Counter64
_F3NetFpQosShaperThresholdMonValue_Object = MibTableColumn
f3NetFpQosShaperThresholdMonValue = _F3NetFpQosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 15, 1, 6),
    _F3NetFpQosShaperThresholdMonValue_Type()
)
f3NetFpQosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdMonValue.setStatus("current")
_F3AccFpQosPolicerStatsTable_Object = MibTable
f3AccFpQosPolicerStatsTable = _F3AccFpQosPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16)
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsTable.setStatus("current")
_F3AccFpQosPolicerStatsEntry_Object = MibTableRow
f3AccFpQosPolicerStatsEntry = _F3AccFpQosPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1)
)
f3AccFpQosPolicerStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerStatsIndex"),
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsEntry.setStatus("current")


class _F3AccFpQosPolicerStatsIndex_Type(Integer32):
    """Custom type f3AccFpQosPolicerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFpQosPolicerStatsIndex_Type.__name__ = "Integer32"
_F3AccFpQosPolicerStatsIndex_Object = MibTableColumn
f3AccFpQosPolicerStatsIndex = _F3AccFpQosPolicerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 1),
    _F3AccFpQosPolicerStatsIndex_Type()
)
f3AccFpQosPolicerStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsIndex.setStatus("current")
_F3AccFpQosPolicerStatsIntervalType_Type = CmPmIntervalType
_F3AccFpQosPolicerStatsIntervalType_Object = MibTableColumn
f3AccFpQosPolicerStatsIntervalType = _F3AccFpQosPolicerStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 2),
    _F3AccFpQosPolicerStatsIntervalType_Type()
)
f3AccFpQosPolicerStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsIntervalType.setStatus("current")
_F3AccFpQosPolicerStatsValid_Type = TruthValue
_F3AccFpQosPolicerStatsValid_Object = MibTableColumn
f3AccFpQosPolicerStatsValid = _F3AccFpQosPolicerStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 3),
    _F3AccFpQosPolicerStatsValid_Type()
)
f3AccFpQosPolicerStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsValid.setStatus("current")
_F3AccFpQosPolicerStatsAction_Type = CmPmBinAction
_F3AccFpQosPolicerStatsAction_Object = MibTableColumn
f3AccFpQosPolicerStatsAction = _F3AccFpQosPolicerStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 4),
    _F3AccFpQosPolicerStatsAction_Type()
)
f3AccFpQosPolicerStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsAction.setStatus("current")
_F3AccFpQosPolicerStatsFMG_Type = PerfCounter64
_F3AccFpQosPolicerStatsFMG_Object = MibTableColumn
f3AccFpQosPolicerStatsFMG = _F3AccFpQosPolicerStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 5),
    _F3AccFpQosPolicerStatsFMG_Type()
)
f3AccFpQosPolicerStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsFMG.setStatus("current")
_F3AccFpQosPolicerStatsFMY_Type = PerfCounter64
_F3AccFpQosPolicerStatsFMY_Object = MibTableColumn
f3AccFpQosPolicerStatsFMY = _F3AccFpQosPolicerStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 6),
    _F3AccFpQosPolicerStatsFMY_Type()
)
f3AccFpQosPolicerStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsFMY.setStatus("current")
_F3AccFpQosPolicerStatsFMRD_Type = PerfCounter64
_F3AccFpQosPolicerStatsFMRD_Object = MibTableColumn
f3AccFpQosPolicerStatsFMRD = _F3AccFpQosPolicerStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 7),
    _F3AccFpQosPolicerStatsFMRD_Type()
)
f3AccFpQosPolicerStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsFMRD.setStatus("current")
_F3AccFpQosPolicerStatsBytesIn_Type = PerfCounter64
_F3AccFpQosPolicerStatsBytesIn_Object = MibTableColumn
f3AccFpQosPolicerStatsBytesIn = _F3AccFpQosPolicerStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 8),
    _F3AccFpQosPolicerStatsBytesIn_Type()
)
f3AccFpQosPolicerStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsBytesIn.setStatus("current")
_F3AccFpQosPolicerStatsBytesOut_Type = PerfCounter64
_F3AccFpQosPolicerStatsBytesOut_Object = MibTableColumn
f3AccFpQosPolicerStatsBytesOut = _F3AccFpQosPolicerStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 9),
    _F3AccFpQosPolicerStatsBytesOut_Type()
)
f3AccFpQosPolicerStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsBytesOut.setStatus("current")
_F3AccFpQosPolicerStatsABR_Type = PerfCounter64
_F3AccFpQosPolicerStatsABR_Object = MibTableColumn
f3AccFpQosPolicerStatsABR = _F3AccFpQosPolicerStatsABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 16, 1, 10),
    _F3AccFpQosPolicerStatsABR_Type()
)
f3AccFpQosPolicerStatsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerStatsABR.setStatus("current")
_F3AccFpQosPolicerHistoryTable_Object = MibTable
f3AccFpQosPolicerHistoryTable = _F3AccFpQosPolicerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17)
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryTable.setStatus("current")
_F3AccFpQosPolicerHistoryEntry_Object = MibTableRow
f3AccFpQosPolicerHistoryEntry = _F3AccFpQosPolicerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1)
)
f3AccFpQosPolicerHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerStatsIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryEntry.setStatus("current")


class _F3AccFpQosPolicerHistoryIndex_Type(Integer32):
    """Custom type f3AccFpQosPolicerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFpQosPolicerHistoryIndex_Type.__name__ = "Integer32"
_F3AccFpQosPolicerHistoryIndex_Object = MibTableColumn
f3AccFpQosPolicerHistoryIndex = _F3AccFpQosPolicerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 1),
    _F3AccFpQosPolicerHistoryIndex_Type()
)
f3AccFpQosPolicerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryIndex.setStatus("current")
_F3AccFpQosPolicerHistoryTime_Type = DateAndTime
_F3AccFpQosPolicerHistoryTime_Object = MibTableColumn
f3AccFpQosPolicerHistoryTime = _F3AccFpQosPolicerHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 2),
    _F3AccFpQosPolicerHistoryTime_Type()
)
f3AccFpQosPolicerHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryTime.setStatus("current")
_F3AccFpQosPolicerHistoryValid_Type = TruthValue
_F3AccFpQosPolicerHistoryValid_Object = MibTableColumn
f3AccFpQosPolicerHistoryValid = _F3AccFpQosPolicerHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 3),
    _F3AccFpQosPolicerHistoryValid_Type()
)
f3AccFpQosPolicerHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryValid.setStatus("current")
_F3AccFpQosPolicerHistoryAction_Type = CmPmBinAction
_F3AccFpQosPolicerHistoryAction_Object = MibTableColumn
f3AccFpQosPolicerHistoryAction = _F3AccFpQosPolicerHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 4),
    _F3AccFpQosPolicerHistoryAction_Type()
)
f3AccFpQosPolicerHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryAction.setStatus("current")
_F3AccFpQosPolicerHistoryFMG_Type = PerfCounter64
_F3AccFpQosPolicerHistoryFMG_Object = MibTableColumn
f3AccFpQosPolicerHistoryFMG = _F3AccFpQosPolicerHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 5),
    _F3AccFpQosPolicerHistoryFMG_Type()
)
f3AccFpQosPolicerHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryFMG.setStatus("current")
_F3AccFpQosPolicerHistoryFMY_Type = PerfCounter64
_F3AccFpQosPolicerHistoryFMY_Object = MibTableColumn
f3AccFpQosPolicerHistoryFMY = _F3AccFpQosPolicerHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 6),
    _F3AccFpQosPolicerHistoryFMY_Type()
)
f3AccFpQosPolicerHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryFMY.setStatus("current")
_F3AccFpQosPolicerHistoryFMRD_Type = PerfCounter64
_F3AccFpQosPolicerHistoryFMRD_Object = MibTableColumn
f3AccFpQosPolicerHistoryFMRD = _F3AccFpQosPolicerHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 7),
    _F3AccFpQosPolicerHistoryFMRD_Type()
)
f3AccFpQosPolicerHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryFMRD.setStatus("current")
_F3AccFpQosPolicerHistoryBytesIn_Type = PerfCounter64
_F3AccFpQosPolicerHistoryBytesIn_Object = MibTableColumn
f3AccFpQosPolicerHistoryBytesIn = _F3AccFpQosPolicerHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 8),
    _F3AccFpQosPolicerHistoryBytesIn_Type()
)
f3AccFpQosPolicerHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryBytesIn.setStatus("current")
_F3AccFpQosPolicerHistoryBytesOut_Type = PerfCounter64
_F3AccFpQosPolicerHistoryBytesOut_Object = MibTableColumn
f3AccFpQosPolicerHistoryBytesOut = _F3AccFpQosPolicerHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 9),
    _F3AccFpQosPolicerHistoryBytesOut_Type()
)
f3AccFpQosPolicerHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryBytesOut.setStatus("current")
_F3AccFpQosPolicerHistoryABR_Type = PerfCounter64
_F3AccFpQosPolicerHistoryABR_Object = MibTableColumn
f3AccFpQosPolicerHistoryABR = _F3AccFpQosPolicerHistoryABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 17, 1, 10),
    _F3AccFpQosPolicerHistoryABR_Type()
)
f3AccFpQosPolicerHistoryABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerHistoryABR.setStatus("current")
_F3AccFpQosPolicerThresholdTable_Object = MibTable
f3AccFpQosPolicerThresholdTable = _F3AccFpQosPolicerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 18)
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdTable.setStatus("current")
_F3AccFpQosPolicerThresholdEntry_Object = MibTableRow
f3AccFpQosPolicerThresholdEntry = _F3AccFpQosPolicerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 18, 1)
)
f3AccFpQosPolicerThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-FPM-MIB", "f3AccFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerStatsIndex"),
    (0, "F3-FPM-MIB", "f3AccFpQosPolicerThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdEntry.setStatus("current")


class _F3AccFpQosPolicerThresholdIndex_Type(Integer32):
    """Custom type f3AccFpQosPolicerThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AccFpQosPolicerThresholdIndex_Type.__name__ = "Integer32"
_F3AccFpQosPolicerThresholdIndex_Object = MibTableColumn
f3AccFpQosPolicerThresholdIndex = _F3AccFpQosPolicerThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 18, 1, 1),
    _F3AccFpQosPolicerThresholdIndex_Type()
)
f3AccFpQosPolicerThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdIndex.setStatus("current")
_F3AccFpQosPolicerThresholdInterval_Type = CmPmIntervalType
_F3AccFpQosPolicerThresholdInterval_Object = MibTableColumn
f3AccFpQosPolicerThresholdInterval = _F3AccFpQosPolicerThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 18, 1, 2),
    _F3AccFpQosPolicerThresholdInterval_Type()
)
f3AccFpQosPolicerThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdInterval.setStatus("current")
_F3AccFpQosPolicerThresholdVariable_Type = VariablePointer
_F3AccFpQosPolicerThresholdVariable_Object = MibTableColumn
f3AccFpQosPolicerThresholdVariable = _F3AccFpQosPolicerThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 18, 1, 3),
    _F3AccFpQosPolicerThresholdVariable_Type()
)
f3AccFpQosPolicerThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdVariable.setStatus("current")
_F3AccFpQosPolicerThresholdValueLo_Type = Unsigned32
_F3AccFpQosPolicerThresholdValueLo_Object = MibTableColumn
f3AccFpQosPolicerThresholdValueLo = _F3AccFpQosPolicerThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 18, 1, 4),
    _F3AccFpQosPolicerThresholdValueLo_Type()
)
f3AccFpQosPolicerThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdValueLo.setStatus("current")
_F3AccFpQosPolicerThresholdValueHi_Type = Unsigned32
_F3AccFpQosPolicerThresholdValueHi_Object = MibTableColumn
f3AccFpQosPolicerThresholdValueHi = _F3AccFpQosPolicerThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 18, 1, 5),
    _F3AccFpQosPolicerThresholdValueHi_Type()
)
f3AccFpQosPolicerThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdValueHi.setStatus("current")
_F3AccFpQosPolicerThresholdMonValue_Type = Counter64
_F3AccFpQosPolicerThresholdMonValue_Object = MibTableColumn
f3AccFpQosPolicerThresholdMonValue = _F3AccFpQosPolicerThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 18, 1, 6),
    _F3AccFpQosPolicerThresholdMonValue_Type()
)
f3AccFpQosPolicerThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdMonValue.setStatus("current")
_F3NetFpQosPolicerStatsTable_Object = MibTable
f3NetFpQosPolicerStatsTable = _F3NetFpQosPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19)
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsTable.setStatus("current")
_F3NetFpQosPolicerStatsEntry_Object = MibTableRow
f3NetFpQosPolicerStatsEntry = _F3NetFpQosPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1)
)
f3NetFpQosPolicerStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsEntry.setStatus("current")


class _F3NetFpQosPolicerStatsIndex_Type(Integer32):
    """Custom type f3NetFpQosPolicerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFpQosPolicerStatsIndex_Type.__name__ = "Integer32"
_F3NetFpQosPolicerStatsIndex_Object = MibTableColumn
f3NetFpQosPolicerStatsIndex = _F3NetFpQosPolicerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 1),
    _F3NetFpQosPolicerStatsIndex_Type()
)
f3NetFpQosPolicerStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsIndex.setStatus("current")
_F3NetFpQosPolicerStatsIntervalType_Type = CmPmIntervalType
_F3NetFpQosPolicerStatsIntervalType_Object = MibTableColumn
f3NetFpQosPolicerStatsIntervalType = _F3NetFpQosPolicerStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 2),
    _F3NetFpQosPolicerStatsIntervalType_Type()
)
f3NetFpQosPolicerStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsIntervalType.setStatus("current")
_F3NetFpQosPolicerStatsValid_Type = TruthValue
_F3NetFpQosPolicerStatsValid_Object = MibTableColumn
f3NetFpQosPolicerStatsValid = _F3NetFpQosPolicerStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 3),
    _F3NetFpQosPolicerStatsValid_Type()
)
f3NetFpQosPolicerStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsValid.setStatus("current")
_F3NetFpQosPolicerStatsAction_Type = CmPmBinAction
_F3NetFpQosPolicerStatsAction_Object = MibTableColumn
f3NetFpQosPolicerStatsAction = _F3NetFpQosPolicerStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 4),
    _F3NetFpQosPolicerStatsAction_Type()
)
f3NetFpQosPolicerStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsAction.setStatus("current")
_F3NetFpQosPolicerStatsFMG_Type = PerfCounter64
_F3NetFpQosPolicerStatsFMG_Object = MibTableColumn
f3NetFpQosPolicerStatsFMG = _F3NetFpQosPolicerStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 5),
    _F3NetFpQosPolicerStatsFMG_Type()
)
f3NetFpQosPolicerStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsFMG.setStatus("current")
_F3NetFpQosPolicerStatsFMY_Type = PerfCounter64
_F3NetFpQosPolicerStatsFMY_Object = MibTableColumn
f3NetFpQosPolicerStatsFMY = _F3NetFpQosPolicerStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 6),
    _F3NetFpQosPolicerStatsFMY_Type()
)
f3NetFpQosPolicerStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsFMY.setStatus("current")
_F3NetFpQosPolicerStatsFMRD_Type = PerfCounter64
_F3NetFpQosPolicerStatsFMRD_Object = MibTableColumn
f3NetFpQosPolicerStatsFMRD = _F3NetFpQosPolicerStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 7),
    _F3NetFpQosPolicerStatsFMRD_Type()
)
f3NetFpQosPolicerStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsFMRD.setStatus("current")
_F3NetFpQosPolicerStatsBytesIn_Type = PerfCounter64
_F3NetFpQosPolicerStatsBytesIn_Object = MibTableColumn
f3NetFpQosPolicerStatsBytesIn = _F3NetFpQosPolicerStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 8),
    _F3NetFpQosPolicerStatsBytesIn_Type()
)
f3NetFpQosPolicerStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsBytesIn.setStatus("current")
_F3NetFpQosPolicerStatsBytesOut_Type = PerfCounter64
_F3NetFpQosPolicerStatsBytesOut_Object = MibTableColumn
f3NetFpQosPolicerStatsBytesOut = _F3NetFpQosPolicerStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 9),
    _F3NetFpQosPolicerStatsBytesOut_Type()
)
f3NetFpQosPolicerStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsBytesOut.setStatus("current")
_F3NetFpQosPolicerStatsABR_Type = PerfCounter64
_F3NetFpQosPolicerStatsABR_Object = MibTableColumn
f3NetFpQosPolicerStatsABR = _F3NetFpQosPolicerStatsABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 19, 1, 10),
    _F3NetFpQosPolicerStatsABR_Type()
)
f3NetFpQosPolicerStatsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerStatsABR.setStatus("current")
_F3NetFpQosPolicerHistoryTable_Object = MibTable
f3NetFpQosPolicerHistoryTable = _F3NetFpQosPolicerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20)
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryTable.setStatus("current")
_F3NetFpQosPolicerHistoryEntry_Object = MibTableRow
f3NetFpQosPolicerHistoryEntry = _F3NetFpQosPolicerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1)
)
f3NetFpQosPolicerHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerStatsIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryEntry.setStatus("current")


class _F3NetFpQosPolicerHistoryIndex_Type(Integer32):
    """Custom type f3NetFpQosPolicerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFpQosPolicerHistoryIndex_Type.__name__ = "Integer32"
_F3NetFpQosPolicerHistoryIndex_Object = MibTableColumn
f3NetFpQosPolicerHistoryIndex = _F3NetFpQosPolicerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 1),
    _F3NetFpQosPolicerHistoryIndex_Type()
)
f3NetFpQosPolicerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryIndex.setStatus("current")
_F3NetFpQosPolicerHistoryTime_Type = DateAndTime
_F3NetFpQosPolicerHistoryTime_Object = MibTableColumn
f3NetFpQosPolicerHistoryTime = _F3NetFpQosPolicerHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 2),
    _F3NetFpQosPolicerHistoryTime_Type()
)
f3NetFpQosPolicerHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryTime.setStatus("current")
_F3NetFpQosPolicerHistoryValid_Type = TruthValue
_F3NetFpQosPolicerHistoryValid_Object = MibTableColumn
f3NetFpQosPolicerHistoryValid = _F3NetFpQosPolicerHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 3),
    _F3NetFpQosPolicerHistoryValid_Type()
)
f3NetFpQosPolicerHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryValid.setStatus("current")
_F3NetFpQosPolicerHistoryAction_Type = CmPmBinAction
_F3NetFpQosPolicerHistoryAction_Object = MibTableColumn
f3NetFpQosPolicerHistoryAction = _F3NetFpQosPolicerHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 4),
    _F3NetFpQosPolicerHistoryAction_Type()
)
f3NetFpQosPolicerHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryAction.setStatus("current")
_F3NetFpQosPolicerHistoryFMG_Type = PerfCounter64
_F3NetFpQosPolicerHistoryFMG_Object = MibTableColumn
f3NetFpQosPolicerHistoryFMG = _F3NetFpQosPolicerHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 5),
    _F3NetFpQosPolicerHistoryFMG_Type()
)
f3NetFpQosPolicerHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryFMG.setStatus("current")
_F3NetFpQosPolicerHistoryFMY_Type = PerfCounter64
_F3NetFpQosPolicerHistoryFMY_Object = MibTableColumn
f3NetFpQosPolicerHistoryFMY = _F3NetFpQosPolicerHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 6),
    _F3NetFpQosPolicerHistoryFMY_Type()
)
f3NetFpQosPolicerHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryFMY.setStatus("current")
_F3NetFpQosPolicerHistoryFMRD_Type = PerfCounter64
_F3NetFpQosPolicerHistoryFMRD_Object = MibTableColumn
f3NetFpQosPolicerHistoryFMRD = _F3NetFpQosPolicerHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 7),
    _F3NetFpQosPolicerHistoryFMRD_Type()
)
f3NetFpQosPolicerHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryFMRD.setStatus("current")
_F3NetFpQosPolicerHistoryBytesIn_Type = PerfCounter64
_F3NetFpQosPolicerHistoryBytesIn_Object = MibTableColumn
f3NetFpQosPolicerHistoryBytesIn = _F3NetFpQosPolicerHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 8),
    _F3NetFpQosPolicerHistoryBytesIn_Type()
)
f3NetFpQosPolicerHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryBytesIn.setStatus("current")
_F3NetFpQosPolicerHistoryBytesOut_Type = PerfCounter64
_F3NetFpQosPolicerHistoryBytesOut_Object = MibTableColumn
f3NetFpQosPolicerHistoryBytesOut = _F3NetFpQosPolicerHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 9),
    _F3NetFpQosPolicerHistoryBytesOut_Type()
)
f3NetFpQosPolicerHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryBytesOut.setStatus("current")
_F3NetFpQosPolicerHistoryABR_Type = PerfCounter64
_F3NetFpQosPolicerHistoryABR_Object = MibTableColumn
f3NetFpQosPolicerHistoryABR = _F3NetFpQosPolicerHistoryABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 20, 1, 10),
    _F3NetFpQosPolicerHistoryABR_Type()
)
f3NetFpQosPolicerHistoryABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerHistoryABR.setStatus("current")
_F3NetFpQosPolicerThresholdTable_Object = MibTable
f3NetFpQosPolicerThresholdTable = _F3NetFpQosPolicerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 21)
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdTable.setStatus("current")
_F3NetFpQosPolicerThresholdEntry_Object = MibTableRow
f3NetFpQosPolicerThresholdEntry = _F3NetFpQosPolicerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 21, 1)
)
f3NetFpQosPolicerThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-FPM-MIB", "f3NetFlowPointIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerStatsIndex"),
    (0, "F3-FPM-MIB", "f3NetFpQosPolicerThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdEntry.setStatus("current")


class _F3NetFpQosPolicerThresholdIndex_Type(Integer32):
    """Custom type f3NetFpQosPolicerThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetFpQosPolicerThresholdIndex_Type.__name__ = "Integer32"
_F3NetFpQosPolicerThresholdIndex_Object = MibTableColumn
f3NetFpQosPolicerThresholdIndex = _F3NetFpQosPolicerThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 21, 1, 1),
    _F3NetFpQosPolicerThresholdIndex_Type()
)
f3NetFpQosPolicerThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdIndex.setStatus("current")
_F3NetFpQosPolicerThresholdInterval_Type = CmPmIntervalType
_F3NetFpQosPolicerThresholdInterval_Object = MibTableColumn
f3NetFpQosPolicerThresholdInterval = _F3NetFpQosPolicerThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 21, 1, 2),
    _F3NetFpQosPolicerThresholdInterval_Type()
)
f3NetFpQosPolicerThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdInterval.setStatus("current")
_F3NetFpQosPolicerThresholdVariable_Type = VariablePointer
_F3NetFpQosPolicerThresholdVariable_Object = MibTableColumn
f3NetFpQosPolicerThresholdVariable = _F3NetFpQosPolicerThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 21, 1, 3),
    _F3NetFpQosPolicerThresholdVariable_Type()
)
f3NetFpQosPolicerThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdVariable.setStatus("current")
_F3NetFpQosPolicerThresholdValueLo_Type = Unsigned32
_F3NetFpQosPolicerThresholdValueLo_Object = MibTableColumn
f3NetFpQosPolicerThresholdValueLo = _F3NetFpQosPolicerThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 21, 1, 4),
    _F3NetFpQosPolicerThresholdValueLo_Type()
)
f3NetFpQosPolicerThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdValueLo.setStatus("current")
_F3NetFpQosPolicerThresholdValueHi_Type = Unsigned32
_F3NetFpQosPolicerThresholdValueHi_Object = MibTableColumn
f3NetFpQosPolicerThresholdValueHi = _F3NetFpQosPolicerThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 21, 1, 5),
    _F3NetFpQosPolicerThresholdValueHi_Type()
)
f3NetFpQosPolicerThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdValueHi.setStatus("current")
_F3NetFpQosPolicerThresholdMonValue_Type = Counter64
_F3NetFpQosPolicerThresholdMonValue_Object = MibTableColumn
f3NetFpQosPolicerThresholdMonValue = _F3NetFpQosPolicerThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 2, 21, 1, 6),
    _F3NetFpQosPolicerThresholdMonValue_Type()
)
f3NetFpQosPolicerThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdMonValue.setStatus("current")
_F3FpmPerfNotifications_ObjectIdentity = ObjectIdentity
f3FpmPerfNotifications = _F3FpmPerfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 3)
)
_F3FpmConformance_ObjectIdentity = ObjectIdentity
f3FpmConformance = _F3FpmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4)
)
_F3FpmCompliances_ObjectIdentity = ObjectIdentity
f3FpmCompliances = _F3FpmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 1)
)
_F3FpmGroups_ObjectIdentity = ObjectIdentity
f3FpmGroups = _F3FpmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2)
)
cmMPFlowEntry.registerAugmentions(
    ("F3-FPM-MIB",
     "f3MPFlowExtEntry")
)
f3MPFlowExtEntry.setIndexNames(*cmMPFlowEntry.getIndexNames())
f3AccFlowPointEntry.registerAugmentions(
    ("F3-FPM-MIB",
     "f3AccFlowPointLearningConfigEntry")
)
f3AccFlowPointLearningConfigEntry.setIndexNames(*f3AccFlowPointEntry.getIndexNames())
f3NetFlowPointEntry.registerAugmentions(
    ("F3-FPM-MIB",
     "f3NetFlowPointLearningConfigEntry")
)
f3NetFlowPointLearningConfigEntry.setIndexNames(*f3NetFlowPointEntry.getIndexNames())

# Managed Objects groups

f3AccFlowPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 1)
)
f3AccFlowPointGroup.setObjects(
      *(("F3-FPM-MIB", "f3AccFlowPointAlias"),
        ("F3-FPM-MIB", "f3AccFlowPointAdminState"),
        ("F3-FPM-MIB", "f3AccFlowPointOperationalState"),
        ("F3-FPM-MIB", "f3AccFlowPointSecondaryState"),
        ("F3-FPM-MIB", "f3AccFlowPointAssociatedFlowId"),
        ("F3-FPM-MIB", "f3AccFlowPointIngressMultiCOSEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointIngressCOS"),
        ("F3-FPM-MIB", "f3AccFlowPointEgressShapingType"),
        ("F3-FPM-MIB", "f3AccFlowPointIngressVlanMemberList"),
        ("F3-FPM-MIB", "f3AccFlowPointVlanMemberAction"),
        ("F3-FPM-MIB", "f3AccFlowPointVlanMemberActionVlan"),
        ("F3-FPM-MIB", "f3AccFlowPointIngressUntaggedFrameEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointCTagControl"),
        ("F3-FPM-MIB", "f3AccFlowPointCTagVlanId"),
        ("F3-FPM-MIB", "f3AccFlowPointCTagVlanPriority"),
        ("F3-FPM-MIB", "f3AccFlowPointSTagControl"),
        ("F3-FPM-MIB", "f3AccFlowPointSTagVlanId"),
        ("F3-FPM-MIB", "f3AccFlowPointSTagVlanPriority"),
        ("F3-FPM-MIB", "f3AccFlowPointEgressOuterTagPrioMapEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointEgressInnerTagPrioMapEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointSESFramesLossThresholdRatio"),
        ("F3-FPM-MIB", "f3AccFlowPointDefaultMemberEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointMcastRateLimitEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointMcastRateLimitSpeedLo"),
        ("F3-FPM-MIB", "f3AccFlowPointMcastRateLimitSpeedHi"),
        ("F3-FPM-MIB", "f3AccFlowPointBcastRateLimitEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointBcastRateLimitSpeedLo"),
        ("F3-FPM-MIB", "f3AccFlowPointBcastRateLimitSpeedHi"),
        ("F3-FPM-MIB", "f3AccFlowPointCombinedRateLimitEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointCombinedRateLimitSpeedLo"),
        ("F3-FPM-MIB", "f3AccFlowPointCombinedRateLimitSpeedHi"),
        ("F3-FPM-MIB", "f3AccFlowPointSplitHorizonGroupOID"),
        ("F3-FPM-MIB", "f3AccFlowPointLoopAvoidance"),
        ("F3-FPM-MIB", "f3AccFlowPointHierarchicalCOSEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointMaximumBWLo"),
        ("F3-FPM-MIB", "f3AccFlowPointMaximumBWHi"),
        ("F3-FPM-MIB", "f3AccFlowPointGuaranteedBWLo"),
        ("F3-FPM-MIB", "f3AccFlowPointGuaranteedBWHi"),
        ("F3-FPM-MIB", "f3AccFlowPointAutoBandwidthConfigEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointAutoCIRPercentage"),
        ("F3-FPM-MIB", "f3AccFlowPointFrameFwdEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointStorageType"),
        ("F3-FPM-MIB", "f3AccFlowPointRowStatus"),
        ("F3-FPM-MIB", "f3AccFlowPointUsePortPrioMapProfile"),
        ("F3-FPM-MIB", "f3AccFlowPointRefPrioMapProfile"),
        ("F3-FPM-MIB", "f3AccFlowpointRefConnectGuardFlowObject"),
        ("F3-FPM-MIB", "f3AccFlowpointSecureBlockingControl"),
        ("F3-FPM-MIB", "f3AccFlowpointSecureState"))
)
if mibBuilder.loadTexts:
    f3AccFlowPointGroup.setStatus("current")

f3AccFpQosShaperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 2)
)
f3AccFpQosShaperGroup.setObjects(
      *(("F3-FPM-MIB", "f3AccFpQosShaperIndex"),
        ("F3-FPM-MIB", "f3AccFpQosShaperAdminState"),
        ("F3-FPM-MIB", "f3AccFpQosShaperOperationalState"),
        ("F3-FPM-MIB", "f3AccFpQosShaperSecondaryState"),
        ("F3-FPM-MIB", "f3AccFpQosShaperCIRLo"),
        ("F3-FPM-MIB", "f3AccFpQosShaperCIRHi"),
        ("F3-FPM-MIB", "f3AccFpQosShaperCBS"),
        ("F3-FPM-MIB", "f3AccFpQosShaperEIRLo"),
        ("F3-FPM-MIB", "f3AccFpQosShaperEIRHi"),
        ("F3-FPM-MIB", "f3AccFpQosShaperEBS"),
        ("F3-FPM-MIB", "f3AccFpQosShaperBufferSize"),
        ("F3-FPM-MIB", "f3AccFpQosShaperCOS"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStorageType"),
        ("F3-FPM-MIB", "f3AccFpQosShaperRowStatus"))
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperGroup.setStatus("current")

f3AccFpQosPolicerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 3)
)
f3AccFpQosPolicerGroup.setObjects(
      *(("F3-FPM-MIB", "f3AccFpQosPolicerAdminState"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerOperationalState"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerSecondaryState"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerCIRLo"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerCIRHi"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerEIRLo"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerEIRHi"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerCBS"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerEBS"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerAlgorithm"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerColorMode"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerCouplingFlag"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStorageType"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerRowStatus"))
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerGroup.setStatus("current")

f3MPFlowExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 4)
)
f3MPFlowExtGroup.setObjects(
      *(("F3-FPM-MIB", "f3MPFlowExtMaxFwdEntries"),
        ("F3-FPM-MIB", "f3MPFlowRefConnectGuardFlowObject"),
        ("F3-FPM-MIB", "f3MPFlowSecureState"))
)
if mibBuilder.loadTexts:
    f3MPFlowExtGroup.setStatus("current")

f3AccFlowPointCpdV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 5)
)
f3AccFlowPointCpdV2Group.setObjects(
      *(("F3-FPM-MIB", "f3AccFlowPointCpdV2IslDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2PagpDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2UdldDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2CdpDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2VtpDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2DtpDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2PvstpPlusDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2UplinkFastDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2VlanBridgeDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2L2PTDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2BPDUDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2PauseDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2LACPDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2LACPMarkerDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2EfmOamDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2SSMDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2PortAuthenDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2LANBridgesDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2GMRPDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2GVRPDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2GARPDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2ActiveControlProtocols"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2ELMIDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac00DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac01DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac02DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac03DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac04DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac05DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac06DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac07DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac08DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac09DispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac0ADispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac0BDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac0CDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac0DDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac0EDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Mac0FDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2NearestLLDPDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2NonTpmrLLDPDispType"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2CustomerLLDPDispType"))
)
if mibBuilder.loadTexts:
    f3AccFlowPointCpdV2Group.setStatus("current")

f3AccFlowPointLearningConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 6)
)
f3AccFlowPointLearningConfigGroup.setObjects(
      *(("F3-FPM-MIB", "f3AccFlowPointLearningConfigLearningEnabled"),
        ("F3-FPM-MIB", "f3AccFlowPointLearningConfigMaxFwdEntries"),
        ("F3-FPM-MIB", "f3AccFlowPointLearningConfigProtectLearningCtrl"),
        ("F3-FPM-MIB", "f3AccFlowPointLearningConfigAction"))
)
if mibBuilder.loadTexts:
    f3AccFlowPointLearningConfigGroup.setStatus("current")

f3NetFlowPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 7)
)
f3NetFlowPointGroup.setObjects(
      *(("F3-FPM-MIB", "f3NetFlowPointAlias"),
        ("F3-FPM-MIB", "f3NetFlowPointAdminState"),
        ("F3-FPM-MIB", "f3NetFlowPointOperationalState"),
        ("F3-FPM-MIB", "f3NetFlowPointSecondaryState"),
        ("F3-FPM-MIB", "f3NetFlowPointAssociatedFlowId"),
        ("F3-FPM-MIB", "f3NetFlowPointIngressMultiCOSEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointIngressCOS"),
        ("F3-FPM-MIB", "f3NetFlowPointEgressShapingType"),
        ("F3-FPM-MIB", "f3NetFlowPointIngressVlanMemberList"),
        ("F3-FPM-MIB", "f3NetFlowPointVlanMemberAction"),
        ("F3-FPM-MIB", "f3NetFlowPointVlanMemberActionVlan"),
        ("F3-FPM-MIB", "f3NetFlowPointIngressUntaggedFrameEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointCTagControl"),
        ("F3-FPM-MIB", "f3NetFlowPointCTagVlanId"),
        ("F3-FPM-MIB", "f3NetFlowPointCTagVlanPriority"),
        ("F3-FPM-MIB", "f3NetFlowPointSTagControl"),
        ("F3-FPM-MIB", "f3NetFlowPointSTagVlanId"),
        ("F3-FPM-MIB", "f3NetFlowPointSTagVlanPriority"),
        ("F3-FPM-MIB", "f3NetFlowPointEgressOuterTagPrioMapEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointEgressInnerTagPrioMapEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointSESFramesLossThresholdRatio"),
        ("F3-FPM-MIB", "f3NetFlowPointDefaultMemberEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointMcastRateLimitEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointMcastRateLimitSpeedLo"),
        ("F3-FPM-MIB", "f3NetFlowPointMcastRateLimitSpeedHi"),
        ("F3-FPM-MIB", "f3NetFlowPointBcastRateLimitEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointBcastRateLimitSpeedLo"),
        ("F3-FPM-MIB", "f3NetFlowPointBcastRateLimitSpeedHi"),
        ("F3-FPM-MIB", "f3NetFlowPointCombinedRateLimitEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointCombinedRateLimitSpeedLo"),
        ("F3-FPM-MIB", "f3NetFlowPointCombinedRateLimitSpeedHi"),
        ("F3-FPM-MIB", "f3NetFlowPointSplitHorizonGroupOID"),
        ("F3-FPM-MIB", "f3NetFlowPointLoopAvoidance"),
        ("F3-FPM-MIB", "f3NetFlowPointHierarchicalCOSEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointMaximumBWLo"),
        ("F3-FPM-MIB", "f3NetFlowPointMaximumBWHi"),
        ("F3-FPM-MIB", "f3NetFlowPointGuaranteedBWLo"),
        ("F3-FPM-MIB", "f3NetFlowPointGuaranteedBWHi"),
        ("F3-FPM-MIB", "f3NetFlowPointAutoBandwidthConfigEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointAutoCIRPercentage"),
        ("F3-FPM-MIB", "f3NetFlowPointFrameFwdEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointStorageType"),
        ("F3-FPM-MIB", "f3NetFlowPointRowStatus"),
        ("F3-FPM-MIB", "f3NetFlowPointUsePortPrioMapProfile"),
        ("F3-FPM-MIB", "f3NetFlowPointRefPrioMapProfile"),
        ("F3-FPM-MIB", "f3NetFlowpointRefConnectGuardFlowObject"),
        ("F3-FPM-MIB", "f3NetFlowpointSecureBlockingControl"),
        ("F3-FPM-MIB", "f3NetFlowpointSecureState"))
)
if mibBuilder.loadTexts:
    f3NetFlowPointGroup.setStatus("current")

f3NetFpQosShaperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 8)
)
f3NetFpQosShaperGroup.setObjects(
      *(("F3-FPM-MIB", "f3NetFpQosShaperIndex"),
        ("F3-FPM-MIB", "f3NetFpQosShaperAdminState"),
        ("F3-FPM-MIB", "f3NetFpQosShaperOperationalState"),
        ("F3-FPM-MIB", "f3NetFpQosShaperSecondaryState"),
        ("F3-FPM-MIB", "f3NetFpQosShaperCIRLo"),
        ("F3-FPM-MIB", "f3NetFpQosShaperCIRHi"),
        ("F3-FPM-MIB", "f3NetFpQosShaperCBS"),
        ("F3-FPM-MIB", "f3NetFpQosShaperEIRLo"),
        ("F3-FPM-MIB", "f3NetFpQosShaperEIRHi"),
        ("F3-FPM-MIB", "f3NetFpQosShaperEBS"),
        ("F3-FPM-MIB", "f3NetFpQosShaperBufferSize"),
        ("F3-FPM-MIB", "f3NetFpQosShaperCOS"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStorageType"),
        ("F3-FPM-MIB", "f3NetFpQosShaperRowStatus"))
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperGroup.setStatus("current")

f3NetFpQosPolicerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 9)
)
f3NetFpQosPolicerGroup.setObjects(
      *(("F3-FPM-MIB", "f3NetFpQosPolicerAdminState"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerOperationalState"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerSecondaryState"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerCIRLo"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerCIRHi"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerEIRLo"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerEIRHi"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerCBS"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerEBS"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerAlgorithm"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerColorMode"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerCouplingFlag"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStorageType"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerRowStatus"))
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerGroup.setStatus("current")

f3NetFlowPointCpdV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 10)
)
f3NetFlowPointCpdV2Group.setObjects(
      *(("F3-FPM-MIB", "f3NetFlowPointCpdV2IslDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2PagpDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2UdldDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2CdpDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2VtpDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2DtpDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2PvstpPlusDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2UplinkFastDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2VlanBridgeDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2L2PTDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2BPDUDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2PauseDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2LACPDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2LACPMarkerDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2EfmOamDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2SSMDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2PortAuthenDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2LANBridgesDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2GMRPDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2GVRPDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2GARPDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2ActiveControlProtocols"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2ELMIDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac00DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac01DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac02DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac03DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac04DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac05DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac06DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac07DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac08DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac09DispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac0ADispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac0BDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac0CDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac0DDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac0EDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Mac0FDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2NearestLLDPDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2NonTpmrLLDPDispType"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2CustomerLLDPDispType"))
)
if mibBuilder.loadTexts:
    f3NetFlowPointCpdV2Group.setStatus("current")

f3NetFlowPointLearningConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 11)
)
f3NetFlowPointLearningConfigGroup.setObjects(
      *(("F3-FPM-MIB", "f3NetFlowPointLearningConfigLearningEnabled"),
        ("F3-FPM-MIB", "f3NetFlowPointLearningConfigMaxFwdEntries"),
        ("F3-FPM-MIB", "f3NetFlowPointLearningConfigProtectLearningCtrl"),
        ("F3-FPM-MIB", "f3NetFlowPointLearningConfigAction"))
)
if mibBuilder.loadTexts:
    f3NetFlowPointLearningConfigGroup.setStatus("current")

f3AccFlowPointPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 12)
)
f3AccFlowPointPerfGroup.setObjects(
      *(("F3-FPM-MIB", "f3AccFlowPointStatsIndex"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsIntervalType"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsValid"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsAction"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsL2CPFD"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsABRRx"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsABRRLRx"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsUAS"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsSES"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFMG"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFMY"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFMRD"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFTD"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsBytesIn"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsBytesOut"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsIBRMax"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsIBRRlMax"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsIBRMin"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsIBRRlMin"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsIBR"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsIBRRl"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFBCD"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFMCD"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFdRxFb"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFdTxFb"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsFdicd"),
        ("F3-FPM-MIB", "f3AccFlowPointStatsNumLearnTableFlushes"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryIndex"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryTime"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryValid"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryAction"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryL2CPFD"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryABRRx"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryABRRLRx"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryUAS"),
        ("F3-FPM-MIB", "f3AccFlowPointHistorySES"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFMG"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFMY"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFMRD"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFTD"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryBytesIn"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryBytesOut"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryIBRMax"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryIBRRlMax"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryIBRMin"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryIBRRlMin"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryIBR"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryIBRRl"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFBCD"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFMCD"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFdRxFb"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFdTxFb"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryFdicd"),
        ("F3-FPM-MIB", "f3AccFlowPointHistoryNumLearnTableFlushes"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdIndex"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdInterval"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdVariable"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdValueLo"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdValueHi"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3AccFlowPointPerfGroup.setStatus("current")

f3NetFlowPointPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 13)
)
f3NetFlowPointPerfGroup.setObjects(
      *(("F3-FPM-MIB", "f3NetFlowPointStatsIndex"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsIntervalType"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsValid"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsAction"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsL2CPFD"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsABRRx"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsABRRLRx"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsUAS"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsSES"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFMG"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFMY"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFMRD"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFTD"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsBytesIn"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsBytesOut"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsIBRMax"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsIBRRlMax"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsIBRMin"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsIBRRlMin"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsIBR"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsIBRRl"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFBCD"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFMCD"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFdRxFb"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFdTxFb"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsFdicd"),
        ("F3-FPM-MIB", "f3NetFlowPointStatsNumLearnTableFlushes"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryIndex"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryTime"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryValid"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryAction"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryL2CPFD"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryABRRx"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryABRRLRx"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryUAS"),
        ("F3-FPM-MIB", "f3NetFlowPointHistorySES"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFMG"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFMY"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFMRD"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFTD"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryBytesIn"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryBytesOut"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryIBRMax"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryIBRRlMax"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryIBRMin"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryIBRRlMin"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryIBR"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryIBRRl"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFBCD"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFMCD"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFdRxFb"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFdTxFb"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryFdicd"),
        ("F3-FPM-MIB", "f3NetFlowPointHistoryNumLearnTableFlushes"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdIndex"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdInterval"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdVariable"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdValueLo"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdValueHi"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NetFlowPointPerfGroup.setStatus("current")

f3MPFlowPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 14)
)
f3MPFlowPerfGroup.setObjects(
      *(("F3-FPM-MIB", "f3MPFlowStatsIndex"),
        ("F3-FPM-MIB", "f3MPFlowStatsIntervalType"),
        ("F3-FPM-MIB", "f3MPFlowStatsValid"),
        ("F3-FPM-MIB", "f3MPFlowStatsAction"),
        ("F3-FPM-MIB", "f3MPFlowStatsFDStaticBlock"),
        ("F3-FPM-MIB", "f3MPFlowStatsFDHairPin"),
        ("F3-FPM-MIB", "f3MPFlowStatsMacTableDiscards"),
        ("F3-FPM-MIB", "f3MPFlowStatsFDProtLearn"),
        ("F3-FPM-MIB", "f3MPFlowHistoryIndex"),
        ("F3-FPM-MIB", "f3MPFlowHistoryTime"),
        ("F3-FPM-MIB", "f3MPFlowHistoryValid"),
        ("F3-FPM-MIB", "f3MPFlowHistoryAction"),
        ("F3-FPM-MIB", "f3MPFlowHistoryFDStaticBlock"),
        ("F3-FPM-MIB", "f3MPFlowHistoryFDHairPin"),
        ("F3-FPM-MIB", "f3MPFlowHistoryMacTableDiscards"),
        ("F3-FPM-MIB", "f3MPFlowHistoryFDProtLearn"),
        ("F3-FPM-MIB", "f3MPFlowThresholdIndex"),
        ("F3-FPM-MIB", "f3MPFlowThresholdInterval"),
        ("F3-FPM-MIB", "f3MPFlowThresholdVariable"),
        ("F3-FPM-MIB", "f3MPFlowThresholdValueLo"),
        ("F3-FPM-MIB", "f3MPFlowThresholdValueHi"),
        ("F3-FPM-MIB", "f3MPFlowThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3MPFlowPerfGroup.setStatus("current")

f3AccFpQosShaperPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 15)
)
f3AccFpQosShaperPerfGroup.setObjects(
      *(("F3-FPM-MIB", "f3AccFpQosShaperStatsIndex"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsIntervalType"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsValid"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsAction"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsBT"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsBTD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsFD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsFTD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsABRRL"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsBREDD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperStatsFREDD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryIndex"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryTime"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryValid"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryAction"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryBT"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryBTD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryFD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryFTD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryABRRL"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryBREDD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperHistoryFREDD"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdIndex"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdInterval"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdVariable"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdValueLo"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdValueHi"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperPerfGroup.setStatus("current")

f3NetFpQosShaperPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 16)
)
f3NetFpQosShaperPerfGroup.setObjects(
      *(("F3-FPM-MIB", "f3NetFpQosShaperStatsIndex"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsIntervalType"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsValid"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsAction"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsBT"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsBTD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsFD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsFTD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsABRRL"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsBREDD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperStatsFREDD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryIndex"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryTime"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryValid"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryAction"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryBT"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryBTD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryFD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryFTD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryABRRL"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryBREDD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperHistoryFREDD"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdIndex"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdInterval"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdVariable"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdValueLo"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdValueHi"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperPerfGroup.setStatus("current")

f3AccFpQosPolicerPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 17)
)
f3AccFpQosPolicerPerfGroup.setObjects(
      *(("F3-FPM-MIB", "f3AccFpQosPolicerStatsIndex"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsIntervalType"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsValid"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsAction"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsFMG"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsFMY"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsFMRD"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsBytesIn"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsBytesOut"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerStatsABR"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryIndex"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryTime"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryValid"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryAction"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryFMG"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryFMY"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryFMRD"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryBytesIn"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryBytesOut"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerHistoryABR"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdIndex"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdInterval"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdVariable"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdValueLo"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdValueHi"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerPerfGroup.setStatus("current")

f3NetFpQosPolicerPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 18)
)
f3NetFpQosPolicerPerfGroup.setObjects(
      *(("F3-FPM-MIB", "f3NetFpQosPolicerStatsIndex"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsIntervalType"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsValid"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsAction"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsFMG"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsFMY"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsFMRD"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsBytesIn"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsBytesOut"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerStatsABR"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryIndex"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryTime"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryValid"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryAction"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryFMG"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryFMY"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryFMRD"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryBytesIn"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryBytesOut"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerHistoryABR"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdIndex"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdInterval"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdVariable"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdValueLo"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdValueHi"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerPerfGroup.setStatus("current")


# Notification objects

f3AccFlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 3, 1)
)
f3AccFlowPointThresholdCrossingAlert.setObjects(
      *(("F3-FPM-MIB", "f3AccFlowPointThresholdIndex"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdInterval"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdVariable"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdValueLo"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdValueHi"),
        ("F3-FPM-MIB", "f3AccFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3AccFlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

f3NetFlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 3, 2)
)
f3NetFlowPointThresholdCrossingAlert.setObjects(
      *(("F3-FPM-MIB", "f3NetFlowPointThresholdIndex"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdInterval"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdVariable"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdValueLo"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdValueHi"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NetFlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

f3MPFlowThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 3, 3)
)
f3MPFlowThresholdCrossingAlert.setObjects(
      *(("F3-FPM-MIB", "f3MPFlowThresholdIndex"),
        ("F3-FPM-MIB", "f3MPFlowThresholdInterval"),
        ("F3-FPM-MIB", "f3MPFlowThresholdVariable"),
        ("F3-FPM-MIB", "f3MPFlowThresholdValueLo"),
        ("F3-FPM-MIB", "f3MPFlowThresholdValueHi"),
        ("F3-FPM-MIB", "f3MPFlowThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3MPFlowThresholdCrossingAlert.setStatus(
        "current"
    )

f3AccFpQosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 3, 4)
)
f3AccFpQosShaperThresholdCrossingAlert.setObjects(
      *(("F3-FPM-MIB", "f3AccFpQosShaperThresholdIndex"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdInterval"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdVariable"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdValueLo"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdValueHi"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3AccFpQosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

f3NetFpQosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 3, 5)
)
f3NetFpQosShaperThresholdCrossingAlert.setObjects(
      *(("F3-FPM-MIB", "f3NetFpQosShaperThresholdIndex"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdInterval"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdVariable"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdValueLo"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdValueHi"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NetFpQosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

f3AccFpQosPolicerThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 3, 6)
)
f3AccFpQosPolicerThresholdCrossingAlert.setObjects(
      *(("F3-FPM-MIB", "f3AccFpQosPolicerThresholdIndex"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdInterval"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdVariable"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdValueLo"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdValueHi"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3AccFpQosPolicerThresholdCrossingAlert.setStatus(
        "current"
    )

f3NetFpQosPolicerThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 3, 7)
)
f3NetFpQosPolicerThresholdCrossingAlert.setObjects(
      *(("F3-FPM-MIB", "f3NetFpQosPolicerThresholdIndex"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdInterval"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdVariable"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdValueLo"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdValueHi"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NetFpQosPolicerThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups

f3FpmPerfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 2, 19)
)
f3FpmPerfNotifGroup.setObjects(
      *(("F3-FPM-MIB", "f3AccFlowPointThresholdCrossingAlert"),
        ("F3-FPM-MIB", "f3NetFlowPointThresholdCrossingAlert"),
        ("F3-FPM-MIB", "f3MPFlowThresholdCrossingAlert"),
        ("F3-FPM-MIB", "f3AccFpQosShaperThresholdCrossingAlert"),
        ("F3-FPM-MIB", "f3NetFpQosShaperThresholdCrossingAlert"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerThresholdCrossingAlert"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerThresholdCrossingAlert"))
)
if mibBuilder.loadTexts:
    f3FpmPerfNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f3FpmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 43, 4, 1, 1)
)
f3FpmCompliance.setObjects(
      *(("F3-FPM-MIB", "f3AccFlowPointGroup"),
        ("F3-FPM-MIB", "f3AccFpQosShaperGroup"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerGroup"),
        ("F3-FPM-MIB", "f3MPFlowExtGroup"),
        ("F3-FPM-MIB", "f3AccFlowPointCpdV2Group"),
        ("F3-FPM-MIB", "f3AccFlowPointLearningConfigGroup"),
        ("F3-FPM-MIB", "f3NetFlowPointGroup"),
        ("F3-FPM-MIB", "f3NetFpQosShaperGroup"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerGroup"),
        ("F3-FPM-MIB", "f3NetFlowPointCpdV2Group"),
        ("F3-FPM-MIB", "f3NetFlowPointLearningConfigGroup"),
        ("F3-FPM-MIB", "f3AccFlowPointPerfGroup"),
        ("F3-FPM-MIB", "f3NetFlowPointPerfGroup"),
        ("F3-FPM-MIB", "f3MPFlowPerfGroup"),
        ("F3-FPM-MIB", "f3AccFpQosShaperPerfGroup"),
        ("F3-FPM-MIB", "f3NetFpQosShaperPerfGroup"),
        ("F3-FPM-MIB", "f3AccFpQosPolicerPerfGroup"),
        ("F3-FPM-MIB", "f3NetFpQosPolicerPerfGroup"),
        ("F3-FPM-MIB", "f3FpmPerfNotifGroup"))
)
if mibBuilder.loadTexts:
    f3FpmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-FPM-MIB",
    **{"f3FpmMIB": f3FpmMIB,
       "f3FpmConfigObjects": f3FpmConfigObjects,
       "f3AccFlowPointTable": f3AccFlowPointTable,
       "f3AccFlowPointEntry": f3AccFlowPointEntry,
       "f3AccFlowPointIndex": f3AccFlowPointIndex,
       "f3AccFlowPointAlias": f3AccFlowPointAlias,
       "f3AccFlowPointAdminState": f3AccFlowPointAdminState,
       "f3AccFlowPointOperationalState": f3AccFlowPointOperationalState,
       "f3AccFlowPointSecondaryState": f3AccFlowPointSecondaryState,
       "f3AccFlowPointAssociatedFlowId": f3AccFlowPointAssociatedFlowId,
       "f3AccFlowPointIngressMultiCOSEnabled": f3AccFlowPointIngressMultiCOSEnabled,
       "f3AccFlowPointIngressCOS": f3AccFlowPointIngressCOS,
       "f3AccFlowPointEgressShapingType": f3AccFlowPointEgressShapingType,
       "f3AccFlowPointIngressVlanMemberList": f3AccFlowPointIngressVlanMemberList,
       "f3AccFlowPointVlanMemberAction": f3AccFlowPointVlanMemberAction,
       "f3AccFlowPointVlanMemberActionVlan": f3AccFlowPointVlanMemberActionVlan,
       "f3AccFlowPointIngressUntaggedFrameEnabled": f3AccFlowPointIngressUntaggedFrameEnabled,
       "f3AccFlowPointCTagControl": f3AccFlowPointCTagControl,
       "f3AccFlowPointCTagVlanId": f3AccFlowPointCTagVlanId,
       "f3AccFlowPointCTagVlanPriority": f3AccFlowPointCTagVlanPriority,
       "f3AccFlowPointSTagControl": f3AccFlowPointSTagControl,
       "f3AccFlowPointSTagVlanId": f3AccFlowPointSTagVlanId,
       "f3AccFlowPointSTagVlanPriority": f3AccFlowPointSTagVlanPriority,
       "f3AccFlowPointEgressOuterTagPrioMapEnabled": f3AccFlowPointEgressOuterTagPrioMapEnabled,
       "f3AccFlowPointEgressInnerTagPrioMapEnabled": f3AccFlowPointEgressInnerTagPrioMapEnabled,
       "f3AccFlowPointSESFramesLossThresholdRatio": f3AccFlowPointSESFramesLossThresholdRatio,
       "f3AccFlowPointDefaultMemberEnabled": f3AccFlowPointDefaultMemberEnabled,
       "f3AccFlowPointMcastRateLimitEnabled": f3AccFlowPointMcastRateLimitEnabled,
       "f3AccFlowPointMcastRateLimitSpeedLo": f3AccFlowPointMcastRateLimitSpeedLo,
       "f3AccFlowPointMcastRateLimitSpeedHi": f3AccFlowPointMcastRateLimitSpeedHi,
       "f3AccFlowPointBcastRateLimitEnabled": f3AccFlowPointBcastRateLimitEnabled,
       "f3AccFlowPointBcastRateLimitSpeedLo": f3AccFlowPointBcastRateLimitSpeedLo,
       "f3AccFlowPointBcastRateLimitSpeedHi": f3AccFlowPointBcastRateLimitSpeedHi,
       "f3AccFlowPointCombinedRateLimitEnabled": f3AccFlowPointCombinedRateLimitEnabled,
       "f3AccFlowPointCombinedRateLimitSpeedLo": f3AccFlowPointCombinedRateLimitSpeedLo,
       "f3AccFlowPointCombinedRateLimitSpeedHi": f3AccFlowPointCombinedRateLimitSpeedHi,
       "f3AccFlowPointSplitHorizonGroupOID": f3AccFlowPointSplitHorizonGroupOID,
       "f3AccFlowPointLoopAvoidance": f3AccFlowPointLoopAvoidance,
       "f3AccFlowPointHierarchicalCOSEnabled": f3AccFlowPointHierarchicalCOSEnabled,
       "f3AccFlowPointMaximumBWLo": f3AccFlowPointMaximumBWLo,
       "f3AccFlowPointMaximumBWHi": f3AccFlowPointMaximumBWHi,
       "f3AccFlowPointGuaranteedBWLo": f3AccFlowPointGuaranteedBWLo,
       "f3AccFlowPointGuaranteedBWHi": f3AccFlowPointGuaranteedBWHi,
       "f3AccFlowPointAutoBandwidthConfigEnabled": f3AccFlowPointAutoBandwidthConfigEnabled,
       "f3AccFlowPointAutoCIRPercentage": f3AccFlowPointAutoCIRPercentage,
       "f3AccFlowPointFrameFwdEnabled": f3AccFlowPointFrameFwdEnabled,
       "f3AccFlowPointStorageType": f3AccFlowPointStorageType,
       "f3AccFlowPointRowStatus": f3AccFlowPointRowStatus,
       "f3AccFlowPointUsePortPrioMapProfile": f3AccFlowPointUsePortPrioMapProfile,
       "f3AccFlowPointRefPrioMapProfile": f3AccFlowPointRefPrioMapProfile,
       "f3AccFlowpointRefConnectGuardFlowObject": f3AccFlowpointRefConnectGuardFlowObject,
       "f3AccFlowpointSecureBlockingControl": f3AccFlowpointSecureBlockingControl,
       "f3AccFlowpointSecureState": f3AccFlowpointSecureState,
       "f3AccFpQosShaperTable": f3AccFpQosShaperTable,
       "f3AccFpQosShaperEntry": f3AccFpQosShaperEntry,
       "f3AccFpQosShaperIndex": f3AccFpQosShaperIndex,
       "f3AccFpQosShaperAdminState": f3AccFpQosShaperAdminState,
       "f3AccFpQosShaperOperationalState": f3AccFpQosShaperOperationalState,
       "f3AccFpQosShaperSecondaryState": f3AccFpQosShaperSecondaryState,
       "f3AccFpQosShaperCIRLo": f3AccFpQosShaperCIRLo,
       "f3AccFpQosShaperCIRHi": f3AccFpQosShaperCIRHi,
       "f3AccFpQosShaperEIRLo": f3AccFpQosShaperEIRLo,
       "f3AccFpQosShaperEIRHi": f3AccFpQosShaperEIRHi,
       "f3AccFpQosShaperCBS": f3AccFpQosShaperCBS,
       "f3AccFpQosShaperEBS": f3AccFpQosShaperEBS,
       "f3AccFpQosShaperBufferSize": f3AccFpQosShaperBufferSize,
       "f3AccFpQosShaperCOS": f3AccFpQosShaperCOS,
       "f3AccFpQosShaperStorageType": f3AccFpQosShaperStorageType,
       "f3AccFpQosShaperRowStatus": f3AccFpQosShaperRowStatus,
       "f3AccFpQosPolicerTable": f3AccFpQosPolicerTable,
       "f3AccFpQosPolicerEntry": f3AccFpQosPolicerEntry,
       "f3AccFpQosPolicerIndex": f3AccFpQosPolicerIndex,
       "f3AccFpQosPolicerAdminState": f3AccFpQosPolicerAdminState,
       "f3AccFpQosPolicerOperationalState": f3AccFpQosPolicerOperationalState,
       "f3AccFpQosPolicerSecondaryState": f3AccFpQosPolicerSecondaryState,
       "f3AccFpQosPolicerCIRLo": f3AccFpQosPolicerCIRLo,
       "f3AccFpQosPolicerCIRHi": f3AccFpQosPolicerCIRHi,
       "f3AccFpQosPolicerEIRLo": f3AccFpQosPolicerEIRLo,
       "f3AccFpQosPolicerEIRHi": f3AccFpQosPolicerEIRHi,
       "f3AccFpQosPolicerCBS": f3AccFpQosPolicerCBS,
       "f3AccFpQosPolicerEBS": f3AccFpQosPolicerEBS,
       "f3AccFpQosPolicerAlgorithm": f3AccFpQosPolicerAlgorithm,
       "f3AccFpQosPolicerColorMode": f3AccFpQosPolicerColorMode,
       "f3AccFpQosPolicerCouplingFlag": f3AccFpQosPolicerCouplingFlag,
       "f3AccFpQosPolicerPolicingEnabled": f3AccFpQosPolicerPolicingEnabled,
       "f3AccFpQosPolicerStorageType": f3AccFpQosPolicerStorageType,
       "f3AccFpQosPolicerRowStatus": f3AccFpQosPolicerRowStatus,
       "f3MPFlowExtTable": f3MPFlowExtTable,
       "f3MPFlowExtEntry": f3MPFlowExtEntry,
       "f3MPFlowExtMaxFwdEntries": f3MPFlowExtMaxFwdEntries,
       "f3MPFlowRefConnectGuardFlowObject": f3MPFlowRefConnectGuardFlowObject,
       "f3MPFlowSecureState": f3MPFlowSecureState,
       "f3AccFlowPointCpdV2Table": f3AccFlowPointCpdV2Table,
       "f3AccFlowPointCpdV2Entry": f3AccFlowPointCpdV2Entry,
       "f3AccFlowPointCpdV2Index": f3AccFlowPointCpdV2Index,
       "f3AccFlowPointCpdV2IslDispType": f3AccFlowPointCpdV2IslDispType,
       "f3AccFlowPointCpdV2PagpDispType": f3AccFlowPointCpdV2PagpDispType,
       "f3AccFlowPointCpdV2UdldDispType": f3AccFlowPointCpdV2UdldDispType,
       "f3AccFlowPointCpdV2CdpDispType": f3AccFlowPointCpdV2CdpDispType,
       "f3AccFlowPointCpdV2VtpDispType": f3AccFlowPointCpdV2VtpDispType,
       "f3AccFlowPointCpdV2DtpDispType": f3AccFlowPointCpdV2DtpDispType,
       "f3AccFlowPointCpdV2PvstpPlusDispType": f3AccFlowPointCpdV2PvstpPlusDispType,
       "f3AccFlowPointCpdV2UplinkFastDispType": f3AccFlowPointCpdV2UplinkFastDispType,
       "f3AccFlowPointCpdV2VlanBridgeDispType": f3AccFlowPointCpdV2VlanBridgeDispType,
       "f3AccFlowPointCpdV2L2PTDispType": f3AccFlowPointCpdV2L2PTDispType,
       "f3AccFlowPointCpdV2BPDUDispType": f3AccFlowPointCpdV2BPDUDispType,
       "f3AccFlowPointCpdV2PauseDispType": f3AccFlowPointCpdV2PauseDispType,
       "f3AccFlowPointCpdV2LACPDispType": f3AccFlowPointCpdV2LACPDispType,
       "f3AccFlowPointCpdV2LACPMarkerDispType": f3AccFlowPointCpdV2LACPMarkerDispType,
       "f3AccFlowPointCpdV2EfmOamDispType": f3AccFlowPointCpdV2EfmOamDispType,
       "f3AccFlowPointCpdV2SSMDispType": f3AccFlowPointCpdV2SSMDispType,
       "f3AccFlowPointCpdV2PortAuthenDispType": f3AccFlowPointCpdV2PortAuthenDispType,
       "f3AccFlowPointCpdV2LANBridgesDispType": f3AccFlowPointCpdV2LANBridgesDispType,
       "f3AccFlowPointCpdV2GMRPDispType": f3AccFlowPointCpdV2GMRPDispType,
       "f3AccFlowPointCpdV2GVRPDispType": f3AccFlowPointCpdV2GVRPDispType,
       "f3AccFlowPointCpdV2GARPDispType": f3AccFlowPointCpdV2GARPDispType,
       "f3AccFlowPointCpdV2ActiveControlProtocols": f3AccFlowPointCpdV2ActiveControlProtocols,
       "f3AccFlowPointCpdV2ELMIDispType": f3AccFlowPointCpdV2ELMIDispType,
       "f3AccFlowPointCpdV2Mac00DispType": f3AccFlowPointCpdV2Mac00DispType,
       "f3AccFlowPointCpdV2Mac01DispType": f3AccFlowPointCpdV2Mac01DispType,
       "f3AccFlowPointCpdV2Mac02DispType": f3AccFlowPointCpdV2Mac02DispType,
       "f3AccFlowPointCpdV2Mac03DispType": f3AccFlowPointCpdV2Mac03DispType,
       "f3AccFlowPointCpdV2Mac04DispType": f3AccFlowPointCpdV2Mac04DispType,
       "f3AccFlowPointCpdV2Mac05DispType": f3AccFlowPointCpdV2Mac05DispType,
       "f3AccFlowPointCpdV2Mac06DispType": f3AccFlowPointCpdV2Mac06DispType,
       "f3AccFlowPointCpdV2Mac07DispType": f3AccFlowPointCpdV2Mac07DispType,
       "f3AccFlowPointCpdV2Mac08DispType": f3AccFlowPointCpdV2Mac08DispType,
       "f3AccFlowPointCpdV2Mac09DispType": f3AccFlowPointCpdV2Mac09DispType,
       "f3AccFlowPointCpdV2Mac0ADispType": f3AccFlowPointCpdV2Mac0ADispType,
       "f3AccFlowPointCpdV2Mac0BDispType": f3AccFlowPointCpdV2Mac0BDispType,
       "f3AccFlowPointCpdV2Mac0CDispType": f3AccFlowPointCpdV2Mac0CDispType,
       "f3AccFlowPointCpdV2Mac0DDispType": f3AccFlowPointCpdV2Mac0DDispType,
       "f3AccFlowPointCpdV2Mac0EDispType": f3AccFlowPointCpdV2Mac0EDispType,
       "f3AccFlowPointCpdV2Mac0FDispType": f3AccFlowPointCpdV2Mac0FDispType,
       "f3AccFlowPointCpdV2NearestLLDPDispType": f3AccFlowPointCpdV2NearestLLDPDispType,
       "f3AccFlowPointCpdV2NonTpmrLLDPDispType": f3AccFlowPointCpdV2NonTpmrLLDPDispType,
       "f3AccFlowPointCpdV2CustomerLLDPDispType": f3AccFlowPointCpdV2CustomerLLDPDispType,
       "f3AccFlowPointLearningConfigTable": f3AccFlowPointLearningConfigTable,
       "f3AccFlowPointLearningConfigEntry": f3AccFlowPointLearningConfigEntry,
       "f3AccFlowPointLearningConfigLearningEnabled": f3AccFlowPointLearningConfigLearningEnabled,
       "f3AccFlowPointLearningConfigMaxFwdEntries": f3AccFlowPointLearningConfigMaxFwdEntries,
       "f3AccFlowPointLearningConfigProtectLearningCtrl": f3AccFlowPointLearningConfigProtectLearningCtrl,
       "f3AccFlowPointLearningConfigAction": f3AccFlowPointLearningConfigAction,
       "f3NetFlowPointTable": f3NetFlowPointTable,
       "f3NetFlowPointEntry": f3NetFlowPointEntry,
       "f3NetFlowPointIndex": f3NetFlowPointIndex,
       "f3NetFlowPointAlias": f3NetFlowPointAlias,
       "f3NetFlowPointAdminState": f3NetFlowPointAdminState,
       "f3NetFlowPointOperationalState": f3NetFlowPointOperationalState,
       "f3NetFlowPointSecondaryState": f3NetFlowPointSecondaryState,
       "f3NetFlowPointAssociatedFlowId": f3NetFlowPointAssociatedFlowId,
       "f3NetFlowPointIngressMultiCOSEnabled": f3NetFlowPointIngressMultiCOSEnabled,
       "f3NetFlowPointIngressCOS": f3NetFlowPointIngressCOS,
       "f3NetFlowPointEgressShapingType": f3NetFlowPointEgressShapingType,
       "f3NetFlowPointIngressVlanMemberList": f3NetFlowPointIngressVlanMemberList,
       "f3NetFlowPointVlanMemberAction": f3NetFlowPointVlanMemberAction,
       "f3NetFlowPointVlanMemberActionVlan": f3NetFlowPointVlanMemberActionVlan,
       "f3NetFlowPointIngressUntaggedFrameEnabled": f3NetFlowPointIngressUntaggedFrameEnabled,
       "f3NetFlowPointCTagControl": f3NetFlowPointCTagControl,
       "f3NetFlowPointCTagVlanId": f3NetFlowPointCTagVlanId,
       "f3NetFlowPointCTagVlanPriority": f3NetFlowPointCTagVlanPriority,
       "f3NetFlowPointSTagControl": f3NetFlowPointSTagControl,
       "f3NetFlowPointSTagVlanId": f3NetFlowPointSTagVlanId,
       "f3NetFlowPointSTagVlanPriority": f3NetFlowPointSTagVlanPriority,
       "f3NetFlowPointEgressOuterTagPrioMapEnabled": f3NetFlowPointEgressOuterTagPrioMapEnabled,
       "f3NetFlowPointEgressInnerTagPrioMapEnabled": f3NetFlowPointEgressInnerTagPrioMapEnabled,
       "f3NetFlowPointSESFramesLossThresholdRatio": f3NetFlowPointSESFramesLossThresholdRatio,
       "f3NetFlowPointDefaultMemberEnabled": f3NetFlowPointDefaultMemberEnabled,
       "f3NetFlowPointMcastRateLimitEnabled": f3NetFlowPointMcastRateLimitEnabled,
       "f3NetFlowPointMcastRateLimitSpeedLo": f3NetFlowPointMcastRateLimitSpeedLo,
       "f3NetFlowPointMcastRateLimitSpeedHi": f3NetFlowPointMcastRateLimitSpeedHi,
       "f3NetFlowPointBcastRateLimitEnabled": f3NetFlowPointBcastRateLimitEnabled,
       "f3NetFlowPointBcastRateLimitSpeedLo": f3NetFlowPointBcastRateLimitSpeedLo,
       "f3NetFlowPointBcastRateLimitSpeedHi": f3NetFlowPointBcastRateLimitSpeedHi,
       "f3NetFlowPointCombinedRateLimitEnabled": f3NetFlowPointCombinedRateLimitEnabled,
       "f3NetFlowPointCombinedRateLimitSpeedLo": f3NetFlowPointCombinedRateLimitSpeedLo,
       "f3NetFlowPointCombinedRateLimitSpeedHi": f3NetFlowPointCombinedRateLimitSpeedHi,
       "f3NetFlowPointSplitHorizonGroupOID": f3NetFlowPointSplitHorizonGroupOID,
       "f3NetFlowPointLoopAvoidance": f3NetFlowPointLoopAvoidance,
       "f3NetFlowPointHierarchicalCOSEnabled": f3NetFlowPointHierarchicalCOSEnabled,
       "f3NetFlowPointMaximumBWLo": f3NetFlowPointMaximumBWLo,
       "f3NetFlowPointMaximumBWHi": f3NetFlowPointMaximumBWHi,
       "f3NetFlowPointGuaranteedBWLo": f3NetFlowPointGuaranteedBWLo,
       "f3NetFlowPointGuaranteedBWHi": f3NetFlowPointGuaranteedBWHi,
       "f3NetFlowPointAutoBandwidthConfigEnabled": f3NetFlowPointAutoBandwidthConfigEnabled,
       "f3NetFlowPointAutoCIRPercentage": f3NetFlowPointAutoCIRPercentage,
       "f3NetFlowPointFrameFwdEnabled": f3NetFlowPointFrameFwdEnabled,
       "f3NetFlowPointStorageType": f3NetFlowPointStorageType,
       "f3NetFlowPointRowStatus": f3NetFlowPointRowStatus,
       "f3NetFlowPointUsePortPrioMapProfile": f3NetFlowPointUsePortPrioMapProfile,
       "f3NetFlowPointRefPrioMapProfile": f3NetFlowPointRefPrioMapProfile,
       "f3NetFlowpointRefConnectGuardFlowObject": f3NetFlowpointRefConnectGuardFlowObject,
       "f3NetFlowpointSecureBlockingControl": f3NetFlowpointSecureBlockingControl,
       "f3NetFlowpointSecureState": f3NetFlowpointSecureState,
       "f3NetFpQosShaperTable": f3NetFpQosShaperTable,
       "f3NetFpQosShaperEntry": f3NetFpQosShaperEntry,
       "f3NetFpQosShaperIndex": f3NetFpQosShaperIndex,
       "f3NetFpQosShaperAdminState": f3NetFpQosShaperAdminState,
       "f3NetFpQosShaperOperationalState": f3NetFpQosShaperOperationalState,
       "f3NetFpQosShaperSecondaryState": f3NetFpQosShaperSecondaryState,
       "f3NetFpQosShaperCIRLo": f3NetFpQosShaperCIRLo,
       "f3NetFpQosShaperCIRHi": f3NetFpQosShaperCIRHi,
       "f3NetFpQosShaperEIRLo": f3NetFpQosShaperEIRLo,
       "f3NetFpQosShaperEIRHi": f3NetFpQosShaperEIRHi,
       "f3NetFpQosShaperCBS": f3NetFpQosShaperCBS,
       "f3NetFpQosShaperEBS": f3NetFpQosShaperEBS,
       "f3NetFpQosShaperBufferSize": f3NetFpQosShaperBufferSize,
       "f3NetFpQosShaperCOS": f3NetFpQosShaperCOS,
       "f3NetFpQosShaperStorageType": f3NetFpQosShaperStorageType,
       "f3NetFpQosShaperRowStatus": f3NetFpQosShaperRowStatus,
       "f3NetFpQosPolicerTable": f3NetFpQosPolicerTable,
       "f3NetFpQosPolicerEntry": f3NetFpQosPolicerEntry,
       "f3NetFpQosPolicerIndex": f3NetFpQosPolicerIndex,
       "f3NetFpQosPolicerAdminState": f3NetFpQosPolicerAdminState,
       "f3NetFpQosPolicerOperationalState": f3NetFpQosPolicerOperationalState,
       "f3NetFpQosPolicerSecondaryState": f3NetFpQosPolicerSecondaryState,
       "f3NetFpQosPolicerCIRLo": f3NetFpQosPolicerCIRLo,
       "f3NetFpQosPolicerCIRHi": f3NetFpQosPolicerCIRHi,
       "f3NetFpQosPolicerEIRLo": f3NetFpQosPolicerEIRLo,
       "f3NetFpQosPolicerEIRHi": f3NetFpQosPolicerEIRHi,
       "f3NetFpQosPolicerCBS": f3NetFpQosPolicerCBS,
       "f3NetFpQosPolicerEBS": f3NetFpQosPolicerEBS,
       "f3NetFpQosPolicerAlgorithm": f3NetFpQosPolicerAlgorithm,
       "f3NetFpQosPolicerColorMode": f3NetFpQosPolicerColorMode,
       "f3NetFpQosPolicerCouplingFlag": f3NetFpQosPolicerCouplingFlag,
       "f3NetFpQosPolicerPolicingEnabled": f3NetFpQosPolicerPolicingEnabled,
       "f3NetFpQosPolicerStorageType": f3NetFpQosPolicerStorageType,
       "f3NetFpQosPolicerRowStatus": f3NetFpQosPolicerRowStatus,
       "f3NetFlowPointCpdV2Table": f3NetFlowPointCpdV2Table,
       "f3NetFlowPointCpdV2Entry": f3NetFlowPointCpdV2Entry,
       "f3NetFlowPointCpdV2Index": f3NetFlowPointCpdV2Index,
       "f3NetFlowPointCpdV2IslDispType": f3NetFlowPointCpdV2IslDispType,
       "f3NetFlowPointCpdV2PagpDispType": f3NetFlowPointCpdV2PagpDispType,
       "f3NetFlowPointCpdV2UdldDispType": f3NetFlowPointCpdV2UdldDispType,
       "f3NetFlowPointCpdV2CdpDispType": f3NetFlowPointCpdV2CdpDispType,
       "f3NetFlowPointCpdV2VtpDispType": f3NetFlowPointCpdV2VtpDispType,
       "f3NetFlowPointCpdV2DtpDispType": f3NetFlowPointCpdV2DtpDispType,
       "f3NetFlowPointCpdV2PvstpPlusDispType": f3NetFlowPointCpdV2PvstpPlusDispType,
       "f3NetFlowPointCpdV2UplinkFastDispType": f3NetFlowPointCpdV2UplinkFastDispType,
       "f3NetFlowPointCpdV2VlanBridgeDispType": f3NetFlowPointCpdV2VlanBridgeDispType,
       "f3NetFlowPointCpdV2L2PTDispType": f3NetFlowPointCpdV2L2PTDispType,
       "f3NetFlowPointCpdV2BPDUDispType": f3NetFlowPointCpdV2BPDUDispType,
       "f3NetFlowPointCpdV2PauseDispType": f3NetFlowPointCpdV2PauseDispType,
       "f3NetFlowPointCpdV2LACPDispType": f3NetFlowPointCpdV2LACPDispType,
       "f3NetFlowPointCpdV2LACPMarkerDispType": f3NetFlowPointCpdV2LACPMarkerDispType,
       "f3NetFlowPointCpdV2EfmOamDispType": f3NetFlowPointCpdV2EfmOamDispType,
       "f3NetFlowPointCpdV2SSMDispType": f3NetFlowPointCpdV2SSMDispType,
       "f3NetFlowPointCpdV2PortAuthenDispType": f3NetFlowPointCpdV2PortAuthenDispType,
       "f3NetFlowPointCpdV2LANBridgesDispType": f3NetFlowPointCpdV2LANBridgesDispType,
       "f3NetFlowPointCpdV2GMRPDispType": f3NetFlowPointCpdV2GMRPDispType,
       "f3NetFlowPointCpdV2GVRPDispType": f3NetFlowPointCpdV2GVRPDispType,
       "f3NetFlowPointCpdV2GARPDispType": f3NetFlowPointCpdV2GARPDispType,
       "f3NetFlowPointCpdV2ActiveControlProtocols": f3NetFlowPointCpdV2ActiveControlProtocols,
       "f3NetFlowPointCpdV2ELMIDispType": f3NetFlowPointCpdV2ELMIDispType,
       "f3NetFlowPointCpdV2Mac00DispType": f3NetFlowPointCpdV2Mac00DispType,
       "f3NetFlowPointCpdV2Mac01DispType": f3NetFlowPointCpdV2Mac01DispType,
       "f3NetFlowPointCpdV2Mac02DispType": f3NetFlowPointCpdV2Mac02DispType,
       "f3NetFlowPointCpdV2Mac03DispType": f3NetFlowPointCpdV2Mac03DispType,
       "f3NetFlowPointCpdV2Mac04DispType": f3NetFlowPointCpdV2Mac04DispType,
       "f3NetFlowPointCpdV2Mac05DispType": f3NetFlowPointCpdV2Mac05DispType,
       "f3NetFlowPointCpdV2Mac06DispType": f3NetFlowPointCpdV2Mac06DispType,
       "f3NetFlowPointCpdV2Mac07DispType": f3NetFlowPointCpdV2Mac07DispType,
       "f3NetFlowPointCpdV2Mac08DispType": f3NetFlowPointCpdV2Mac08DispType,
       "f3NetFlowPointCpdV2Mac09DispType": f3NetFlowPointCpdV2Mac09DispType,
       "f3NetFlowPointCpdV2Mac0ADispType": f3NetFlowPointCpdV2Mac0ADispType,
       "f3NetFlowPointCpdV2Mac0BDispType": f3NetFlowPointCpdV2Mac0BDispType,
       "f3NetFlowPointCpdV2Mac0CDispType": f3NetFlowPointCpdV2Mac0CDispType,
       "f3NetFlowPointCpdV2Mac0DDispType": f3NetFlowPointCpdV2Mac0DDispType,
       "f3NetFlowPointCpdV2Mac0EDispType": f3NetFlowPointCpdV2Mac0EDispType,
       "f3NetFlowPointCpdV2Mac0FDispType": f3NetFlowPointCpdV2Mac0FDispType,
       "f3NetFlowPointCpdV2NearestLLDPDispType": f3NetFlowPointCpdV2NearestLLDPDispType,
       "f3NetFlowPointCpdV2NonTpmrLLDPDispType": f3NetFlowPointCpdV2NonTpmrLLDPDispType,
       "f3NetFlowPointCpdV2CustomerLLDPDispType": f3NetFlowPointCpdV2CustomerLLDPDispType,
       "f3NetFlowPointLearningConfigTable": f3NetFlowPointLearningConfigTable,
       "f3NetFlowPointLearningConfigEntry": f3NetFlowPointLearningConfigEntry,
       "f3NetFlowPointLearningConfigLearningEnabled": f3NetFlowPointLearningConfigLearningEnabled,
       "f3NetFlowPointLearningConfigMaxFwdEntries": f3NetFlowPointLearningConfigMaxFwdEntries,
       "f3NetFlowPointLearningConfigProtectLearningCtrl": f3NetFlowPointLearningConfigProtectLearningCtrl,
       "f3NetFlowPointLearningConfigAction": f3NetFlowPointLearningConfigAction,
       "f3FpmPerfObjects": f3FpmPerfObjects,
       "f3AccFlowPointStatsTable": f3AccFlowPointStatsTable,
       "f3AccFlowPointStatsEntry": f3AccFlowPointStatsEntry,
       "f3AccFlowPointStatsIndex": f3AccFlowPointStatsIndex,
       "f3AccFlowPointStatsIntervalType": f3AccFlowPointStatsIntervalType,
       "f3AccFlowPointStatsValid": f3AccFlowPointStatsValid,
       "f3AccFlowPointStatsAction": f3AccFlowPointStatsAction,
       "f3AccFlowPointStatsL2CPFD": f3AccFlowPointStatsL2CPFD,
       "f3AccFlowPointStatsABRRx": f3AccFlowPointStatsABRRx,
       "f3AccFlowPointStatsABRRLRx": f3AccFlowPointStatsABRRLRx,
       "f3AccFlowPointStatsUAS": f3AccFlowPointStatsUAS,
       "f3AccFlowPointStatsSES": f3AccFlowPointStatsSES,
       "f3AccFlowPointStatsFMG": f3AccFlowPointStatsFMG,
       "f3AccFlowPointStatsFMY": f3AccFlowPointStatsFMY,
       "f3AccFlowPointStatsFMRD": f3AccFlowPointStatsFMRD,
       "f3AccFlowPointStatsFTD": f3AccFlowPointStatsFTD,
       "f3AccFlowPointStatsBytesIn": f3AccFlowPointStatsBytesIn,
       "f3AccFlowPointStatsBytesOut": f3AccFlowPointStatsBytesOut,
       "f3AccFlowPointStatsIBRMax": f3AccFlowPointStatsIBRMax,
       "f3AccFlowPointStatsIBRRlMax": f3AccFlowPointStatsIBRRlMax,
       "f3AccFlowPointStatsIBRMin": f3AccFlowPointStatsIBRMin,
       "f3AccFlowPointStatsIBRRlMin": f3AccFlowPointStatsIBRRlMin,
       "f3AccFlowPointStatsIBR": f3AccFlowPointStatsIBR,
       "f3AccFlowPointStatsIBRRl": f3AccFlowPointStatsIBRRl,
       "f3AccFlowPointStatsFBCD": f3AccFlowPointStatsFBCD,
       "f3AccFlowPointStatsFMCD": f3AccFlowPointStatsFMCD,
       "f3AccFlowPointStatsFdRxFb": f3AccFlowPointStatsFdRxFb,
       "f3AccFlowPointStatsFdTxFb": f3AccFlowPointStatsFdTxFb,
       "f3AccFlowPointStatsFdicd": f3AccFlowPointStatsFdicd,
       "f3AccFlowPointStatsNumLearnTableFlushes": f3AccFlowPointStatsNumLearnTableFlushes,
       "f3NetFlowPointStatsTable": f3NetFlowPointStatsTable,
       "f3NetFlowPointStatsEntry": f3NetFlowPointStatsEntry,
       "f3NetFlowPointStatsIndex": f3NetFlowPointStatsIndex,
       "f3NetFlowPointStatsIntervalType": f3NetFlowPointStatsIntervalType,
       "f3NetFlowPointStatsValid": f3NetFlowPointStatsValid,
       "f3NetFlowPointStatsAction": f3NetFlowPointStatsAction,
       "f3NetFlowPointStatsL2CPFD": f3NetFlowPointStatsL2CPFD,
       "f3NetFlowPointStatsABRRx": f3NetFlowPointStatsABRRx,
       "f3NetFlowPointStatsABRRLRx": f3NetFlowPointStatsABRRLRx,
       "f3NetFlowPointStatsUAS": f3NetFlowPointStatsUAS,
       "f3NetFlowPointStatsSES": f3NetFlowPointStatsSES,
       "f3NetFlowPointStatsFMG": f3NetFlowPointStatsFMG,
       "f3NetFlowPointStatsFMY": f3NetFlowPointStatsFMY,
       "f3NetFlowPointStatsFMRD": f3NetFlowPointStatsFMRD,
       "f3NetFlowPointStatsFTD": f3NetFlowPointStatsFTD,
       "f3NetFlowPointStatsBytesIn": f3NetFlowPointStatsBytesIn,
       "f3NetFlowPointStatsBytesOut": f3NetFlowPointStatsBytesOut,
       "f3NetFlowPointStatsIBRMax": f3NetFlowPointStatsIBRMax,
       "f3NetFlowPointStatsIBRRlMax": f3NetFlowPointStatsIBRRlMax,
       "f3NetFlowPointStatsIBRMin": f3NetFlowPointStatsIBRMin,
       "f3NetFlowPointStatsIBRRlMin": f3NetFlowPointStatsIBRRlMin,
       "f3NetFlowPointStatsIBR": f3NetFlowPointStatsIBR,
       "f3NetFlowPointStatsIBRRl": f3NetFlowPointStatsIBRRl,
       "f3NetFlowPointStatsFBCD": f3NetFlowPointStatsFBCD,
       "f3NetFlowPointStatsFMCD": f3NetFlowPointStatsFMCD,
       "f3NetFlowPointStatsFdRxFb": f3NetFlowPointStatsFdRxFb,
       "f3NetFlowPointStatsFdTxFb": f3NetFlowPointStatsFdTxFb,
       "f3NetFlowPointStatsFdicd": f3NetFlowPointStatsFdicd,
       "f3NetFlowPointStatsNumLearnTableFlushes": f3NetFlowPointStatsNumLearnTableFlushes,
       "f3AccFlowPointHistoryTable": f3AccFlowPointHistoryTable,
       "f3AccFlowPointHistoryEntry": f3AccFlowPointHistoryEntry,
       "f3AccFlowPointHistoryIndex": f3AccFlowPointHistoryIndex,
       "f3AccFlowPointHistoryTime": f3AccFlowPointHistoryTime,
       "f3AccFlowPointHistoryValid": f3AccFlowPointHistoryValid,
       "f3AccFlowPointHistoryAction": f3AccFlowPointHistoryAction,
       "f3AccFlowPointHistoryL2CPFD": f3AccFlowPointHistoryL2CPFD,
       "f3AccFlowPointHistoryABRRx": f3AccFlowPointHistoryABRRx,
       "f3AccFlowPointHistoryABRRLRx": f3AccFlowPointHistoryABRRLRx,
       "f3AccFlowPointHistoryUAS": f3AccFlowPointHistoryUAS,
       "f3AccFlowPointHistorySES": f3AccFlowPointHistorySES,
       "f3AccFlowPointHistoryFMG": f3AccFlowPointHistoryFMG,
       "f3AccFlowPointHistoryFMY": f3AccFlowPointHistoryFMY,
       "f3AccFlowPointHistoryFMRD": f3AccFlowPointHistoryFMRD,
       "f3AccFlowPointHistoryFTD": f3AccFlowPointHistoryFTD,
       "f3AccFlowPointHistoryBytesIn": f3AccFlowPointHistoryBytesIn,
       "f3AccFlowPointHistoryBytesOut": f3AccFlowPointHistoryBytesOut,
       "f3AccFlowPointHistoryIBRMax": f3AccFlowPointHistoryIBRMax,
       "f3AccFlowPointHistoryIBRRlMax": f3AccFlowPointHistoryIBRRlMax,
       "f3AccFlowPointHistoryIBRMin": f3AccFlowPointHistoryIBRMin,
       "f3AccFlowPointHistoryIBRRlMin": f3AccFlowPointHistoryIBRRlMin,
       "f3AccFlowPointHistoryIBR": f3AccFlowPointHistoryIBR,
       "f3AccFlowPointHistoryIBRRl": f3AccFlowPointHistoryIBRRl,
       "f3AccFlowPointHistoryFBCD": f3AccFlowPointHistoryFBCD,
       "f3AccFlowPointHistoryFMCD": f3AccFlowPointHistoryFMCD,
       "f3AccFlowPointHistoryFdRxFb": f3AccFlowPointHistoryFdRxFb,
       "f3AccFlowPointHistoryFdTxFb": f3AccFlowPointHistoryFdTxFb,
       "f3AccFlowPointHistoryFdicd": f3AccFlowPointHistoryFdicd,
       "f3AccFlowPointHistoryNumLearnTableFlushes": f3AccFlowPointHistoryNumLearnTableFlushes,
       "f3NetFlowPointHistoryTable": f3NetFlowPointHistoryTable,
       "f3NetFlowPointHistoryEntry": f3NetFlowPointHistoryEntry,
       "f3NetFlowPointHistoryIndex": f3NetFlowPointHistoryIndex,
       "f3NetFlowPointHistoryTime": f3NetFlowPointHistoryTime,
       "f3NetFlowPointHistoryValid": f3NetFlowPointHistoryValid,
       "f3NetFlowPointHistoryAction": f3NetFlowPointHistoryAction,
       "f3NetFlowPointHistoryL2CPFD": f3NetFlowPointHistoryL2CPFD,
       "f3NetFlowPointHistoryABRRx": f3NetFlowPointHistoryABRRx,
       "f3NetFlowPointHistoryABRRLRx": f3NetFlowPointHistoryABRRLRx,
       "f3NetFlowPointHistoryUAS": f3NetFlowPointHistoryUAS,
       "f3NetFlowPointHistorySES": f3NetFlowPointHistorySES,
       "f3NetFlowPointHistoryFMG": f3NetFlowPointHistoryFMG,
       "f3NetFlowPointHistoryFMY": f3NetFlowPointHistoryFMY,
       "f3NetFlowPointHistoryFMRD": f3NetFlowPointHistoryFMRD,
       "f3NetFlowPointHistoryFTD": f3NetFlowPointHistoryFTD,
       "f3NetFlowPointHistoryBytesIn": f3NetFlowPointHistoryBytesIn,
       "f3NetFlowPointHistoryBytesOut": f3NetFlowPointHistoryBytesOut,
       "f3NetFlowPointHistoryIBRMax": f3NetFlowPointHistoryIBRMax,
       "f3NetFlowPointHistoryIBRRlMax": f3NetFlowPointHistoryIBRRlMax,
       "f3NetFlowPointHistoryIBRMin": f3NetFlowPointHistoryIBRMin,
       "f3NetFlowPointHistoryIBRRlMin": f3NetFlowPointHistoryIBRRlMin,
       "f3NetFlowPointHistoryIBR": f3NetFlowPointHistoryIBR,
       "f3NetFlowPointHistoryIBRRl": f3NetFlowPointHistoryIBRRl,
       "f3NetFlowPointHistoryFBCD": f3NetFlowPointHistoryFBCD,
       "f3NetFlowPointHistoryFMCD": f3NetFlowPointHistoryFMCD,
       "f3NetFlowPointHistoryFdRxFb": f3NetFlowPointHistoryFdRxFb,
       "f3NetFlowPointHistoryFdTxFb": f3NetFlowPointHistoryFdTxFb,
       "f3NetFlowPointHistoryFdicd": f3NetFlowPointHistoryFdicd,
       "f3NetFlowPointHistoryNumLearnTableFlushes": f3NetFlowPointHistoryNumLearnTableFlushes,
       "f3AccFlowPointThresholdTable": f3AccFlowPointThresholdTable,
       "f3AccFlowPointThresholdEntry": f3AccFlowPointThresholdEntry,
       "f3AccFlowPointThresholdIndex": f3AccFlowPointThresholdIndex,
       "f3AccFlowPointThresholdInterval": f3AccFlowPointThresholdInterval,
       "f3AccFlowPointThresholdVariable": f3AccFlowPointThresholdVariable,
       "f3AccFlowPointThresholdValueLo": f3AccFlowPointThresholdValueLo,
       "f3AccFlowPointThresholdValueHi": f3AccFlowPointThresholdValueHi,
       "f3AccFlowPointThresholdMonValue": f3AccFlowPointThresholdMonValue,
       "f3NetFlowPointThresholdTable": f3NetFlowPointThresholdTable,
       "f3NetFlowPointThresholdEntry": f3NetFlowPointThresholdEntry,
       "f3NetFlowPointThresholdIndex": f3NetFlowPointThresholdIndex,
       "f3NetFlowPointThresholdInterval": f3NetFlowPointThresholdInterval,
       "f3NetFlowPointThresholdVariable": f3NetFlowPointThresholdVariable,
       "f3NetFlowPointThresholdValueLo": f3NetFlowPointThresholdValueLo,
       "f3NetFlowPointThresholdValueHi": f3NetFlowPointThresholdValueHi,
       "f3NetFlowPointThresholdMonValue": f3NetFlowPointThresholdMonValue,
       "f3MPFlowStatsTable": f3MPFlowStatsTable,
       "f3MPFlowStatsEntry": f3MPFlowStatsEntry,
       "f3MPFlowStatsIndex": f3MPFlowStatsIndex,
       "f3MPFlowStatsIntervalType": f3MPFlowStatsIntervalType,
       "f3MPFlowStatsValid": f3MPFlowStatsValid,
       "f3MPFlowStatsAction": f3MPFlowStatsAction,
       "f3MPFlowStatsFDStaticBlock": f3MPFlowStatsFDStaticBlock,
       "f3MPFlowStatsFDHairPin": f3MPFlowStatsFDHairPin,
       "f3MPFlowStatsMacTableDiscards": f3MPFlowStatsMacTableDiscards,
       "f3MPFlowStatsFDProtLearn": f3MPFlowStatsFDProtLearn,
       "f3MPFlowHistoryTable": f3MPFlowHistoryTable,
       "f3MPFlowHistoryEntry": f3MPFlowHistoryEntry,
       "f3MPFlowHistoryIndex": f3MPFlowHistoryIndex,
       "f3MPFlowHistoryTime": f3MPFlowHistoryTime,
       "f3MPFlowHistoryValid": f3MPFlowHistoryValid,
       "f3MPFlowHistoryAction": f3MPFlowHistoryAction,
       "f3MPFlowHistoryFDStaticBlock": f3MPFlowHistoryFDStaticBlock,
       "f3MPFlowHistoryFDHairPin": f3MPFlowHistoryFDHairPin,
       "f3MPFlowHistoryMacTableDiscards": f3MPFlowHistoryMacTableDiscards,
       "f3MPFlowHistoryFDProtLearn": f3MPFlowHistoryFDProtLearn,
       "f3MPFlowThresholdTable": f3MPFlowThresholdTable,
       "f3MPFlowThresholdEntry": f3MPFlowThresholdEntry,
       "f3MPFlowThresholdIndex": f3MPFlowThresholdIndex,
       "f3MPFlowThresholdInterval": f3MPFlowThresholdInterval,
       "f3MPFlowThresholdVariable": f3MPFlowThresholdVariable,
       "f3MPFlowThresholdValueLo": f3MPFlowThresholdValueLo,
       "f3MPFlowThresholdValueHi": f3MPFlowThresholdValueHi,
       "f3MPFlowThresholdMonValue": f3MPFlowThresholdMonValue,
       "f3AccFpQosShaperStatsTable": f3AccFpQosShaperStatsTable,
       "f3AccFpQosShaperStatsEntry": f3AccFpQosShaperStatsEntry,
       "f3AccFpQosShaperStatsIndex": f3AccFpQosShaperStatsIndex,
       "f3AccFpQosShaperStatsIntervalType": f3AccFpQosShaperStatsIntervalType,
       "f3AccFpQosShaperStatsValid": f3AccFpQosShaperStatsValid,
       "f3AccFpQosShaperStatsAction": f3AccFpQosShaperStatsAction,
       "f3AccFpQosShaperStatsBT": f3AccFpQosShaperStatsBT,
       "f3AccFpQosShaperStatsBTD": f3AccFpQosShaperStatsBTD,
       "f3AccFpQosShaperStatsFD": f3AccFpQosShaperStatsFD,
       "f3AccFpQosShaperStatsFTD": f3AccFpQosShaperStatsFTD,
       "f3AccFpQosShaperStatsABRRL": f3AccFpQosShaperStatsABRRL,
       "f3AccFpQosShaperStatsBREDD": f3AccFpQosShaperStatsBREDD,
       "f3AccFpQosShaperStatsFREDD": f3AccFpQosShaperStatsFREDD,
       "f3AccFpQosShaperHistoryTable": f3AccFpQosShaperHistoryTable,
       "f3AccFpQosShaperHistoryEntry": f3AccFpQosShaperHistoryEntry,
       "f3AccFpQosShaperHistoryIndex": f3AccFpQosShaperHistoryIndex,
       "f3AccFpQosShaperHistoryTime": f3AccFpQosShaperHistoryTime,
       "f3AccFpQosShaperHistoryValid": f3AccFpQosShaperHistoryValid,
       "f3AccFpQosShaperHistoryAction": f3AccFpQosShaperHistoryAction,
       "f3AccFpQosShaperHistoryBT": f3AccFpQosShaperHistoryBT,
       "f3AccFpQosShaperHistoryBTD": f3AccFpQosShaperHistoryBTD,
       "f3AccFpQosShaperHistoryFD": f3AccFpQosShaperHistoryFD,
       "f3AccFpQosShaperHistoryFTD": f3AccFpQosShaperHistoryFTD,
       "f3AccFpQosShaperHistoryABRRL": f3AccFpQosShaperHistoryABRRL,
       "f3AccFpQosShaperHistoryBREDD": f3AccFpQosShaperHistoryBREDD,
       "f3AccFpQosShaperHistoryFREDD": f3AccFpQosShaperHistoryFREDD,
       "f3AccFpQosShaperThresholdTable": f3AccFpQosShaperThresholdTable,
       "f3AccFpQosShaperThresholdEntry": f3AccFpQosShaperThresholdEntry,
       "f3AccFpQosShaperThresholdIndex": f3AccFpQosShaperThresholdIndex,
       "f3AccFpQosShaperThresholdInterval": f3AccFpQosShaperThresholdInterval,
       "f3AccFpQosShaperThresholdVariable": f3AccFpQosShaperThresholdVariable,
       "f3AccFpQosShaperThresholdValueLo": f3AccFpQosShaperThresholdValueLo,
       "f3AccFpQosShaperThresholdValueHi": f3AccFpQosShaperThresholdValueHi,
       "f3AccFpQosShaperThresholdMonValue": f3AccFpQosShaperThresholdMonValue,
       "f3NetFpQosShaperStatsTable": f3NetFpQosShaperStatsTable,
       "f3NetFpQosShaperStatsEntry": f3NetFpQosShaperStatsEntry,
       "f3NetFpQosShaperStatsIndex": f3NetFpQosShaperStatsIndex,
       "f3NetFpQosShaperStatsIntervalType": f3NetFpQosShaperStatsIntervalType,
       "f3NetFpQosShaperStatsValid": f3NetFpQosShaperStatsValid,
       "f3NetFpQosShaperStatsAction": f3NetFpQosShaperStatsAction,
       "f3NetFpQosShaperStatsBT": f3NetFpQosShaperStatsBT,
       "f3NetFpQosShaperStatsBTD": f3NetFpQosShaperStatsBTD,
       "f3NetFpQosShaperStatsFD": f3NetFpQosShaperStatsFD,
       "f3NetFpQosShaperStatsFTD": f3NetFpQosShaperStatsFTD,
       "f3NetFpQosShaperStatsABRRL": f3NetFpQosShaperStatsABRRL,
       "f3NetFpQosShaperStatsBREDD": f3NetFpQosShaperStatsBREDD,
       "f3NetFpQosShaperStatsFREDD": f3NetFpQosShaperStatsFREDD,
       "f3NetFpQosShaperHistoryTable": f3NetFpQosShaperHistoryTable,
       "f3NetFpQosShaperHistoryEntry": f3NetFpQosShaperHistoryEntry,
       "f3NetFpQosShaperHistoryIndex": f3NetFpQosShaperHistoryIndex,
       "f3NetFpQosShaperHistoryTime": f3NetFpQosShaperHistoryTime,
       "f3NetFpQosShaperHistoryValid": f3NetFpQosShaperHistoryValid,
       "f3NetFpQosShaperHistoryAction": f3NetFpQosShaperHistoryAction,
       "f3NetFpQosShaperHistoryBT": f3NetFpQosShaperHistoryBT,
       "f3NetFpQosShaperHistoryBTD": f3NetFpQosShaperHistoryBTD,
       "f3NetFpQosShaperHistoryFD": f3NetFpQosShaperHistoryFD,
       "f3NetFpQosShaperHistoryFTD": f3NetFpQosShaperHistoryFTD,
       "f3NetFpQosShaperHistoryABRRL": f3NetFpQosShaperHistoryABRRL,
       "f3NetFpQosShaperHistoryBREDD": f3NetFpQosShaperHistoryBREDD,
       "f3NetFpQosShaperHistoryFREDD": f3NetFpQosShaperHistoryFREDD,
       "f3NetFpQosShaperThresholdTable": f3NetFpQosShaperThresholdTable,
       "f3NetFpQosShaperThresholdEntry": f3NetFpQosShaperThresholdEntry,
       "f3NetFpQosShaperThresholdIndex": f3NetFpQosShaperThresholdIndex,
       "f3NetFpQosShaperThresholdInterval": f3NetFpQosShaperThresholdInterval,
       "f3NetFpQosShaperThresholdVariable": f3NetFpQosShaperThresholdVariable,
       "f3NetFpQosShaperThresholdValueLo": f3NetFpQosShaperThresholdValueLo,
       "f3NetFpQosShaperThresholdValueHi": f3NetFpQosShaperThresholdValueHi,
       "f3NetFpQosShaperThresholdMonValue": f3NetFpQosShaperThresholdMonValue,
       "f3AccFpQosPolicerStatsTable": f3AccFpQosPolicerStatsTable,
       "f3AccFpQosPolicerStatsEntry": f3AccFpQosPolicerStatsEntry,
       "f3AccFpQosPolicerStatsIndex": f3AccFpQosPolicerStatsIndex,
       "f3AccFpQosPolicerStatsIntervalType": f3AccFpQosPolicerStatsIntervalType,
       "f3AccFpQosPolicerStatsValid": f3AccFpQosPolicerStatsValid,
       "f3AccFpQosPolicerStatsAction": f3AccFpQosPolicerStatsAction,
       "f3AccFpQosPolicerStatsFMG": f3AccFpQosPolicerStatsFMG,
       "f3AccFpQosPolicerStatsFMY": f3AccFpQosPolicerStatsFMY,
       "f3AccFpQosPolicerStatsFMRD": f3AccFpQosPolicerStatsFMRD,
       "f3AccFpQosPolicerStatsBytesIn": f3AccFpQosPolicerStatsBytesIn,
       "f3AccFpQosPolicerStatsBytesOut": f3AccFpQosPolicerStatsBytesOut,
       "f3AccFpQosPolicerStatsABR": f3AccFpQosPolicerStatsABR,
       "f3AccFpQosPolicerHistoryTable": f3AccFpQosPolicerHistoryTable,
       "f3AccFpQosPolicerHistoryEntry": f3AccFpQosPolicerHistoryEntry,
       "f3AccFpQosPolicerHistoryIndex": f3AccFpQosPolicerHistoryIndex,
       "f3AccFpQosPolicerHistoryTime": f3AccFpQosPolicerHistoryTime,
       "f3AccFpQosPolicerHistoryValid": f3AccFpQosPolicerHistoryValid,
       "f3AccFpQosPolicerHistoryAction": f3AccFpQosPolicerHistoryAction,
       "f3AccFpQosPolicerHistoryFMG": f3AccFpQosPolicerHistoryFMG,
       "f3AccFpQosPolicerHistoryFMY": f3AccFpQosPolicerHistoryFMY,
       "f3AccFpQosPolicerHistoryFMRD": f3AccFpQosPolicerHistoryFMRD,
       "f3AccFpQosPolicerHistoryBytesIn": f3AccFpQosPolicerHistoryBytesIn,
       "f3AccFpQosPolicerHistoryBytesOut": f3AccFpQosPolicerHistoryBytesOut,
       "f3AccFpQosPolicerHistoryABR": f3AccFpQosPolicerHistoryABR,
       "f3AccFpQosPolicerThresholdTable": f3AccFpQosPolicerThresholdTable,
       "f3AccFpQosPolicerThresholdEntry": f3AccFpQosPolicerThresholdEntry,
       "f3AccFpQosPolicerThresholdIndex": f3AccFpQosPolicerThresholdIndex,
       "f3AccFpQosPolicerThresholdInterval": f3AccFpQosPolicerThresholdInterval,
       "f3AccFpQosPolicerThresholdVariable": f3AccFpQosPolicerThresholdVariable,
       "f3AccFpQosPolicerThresholdValueLo": f3AccFpQosPolicerThresholdValueLo,
       "f3AccFpQosPolicerThresholdValueHi": f3AccFpQosPolicerThresholdValueHi,
       "f3AccFpQosPolicerThresholdMonValue": f3AccFpQosPolicerThresholdMonValue,
       "f3NetFpQosPolicerStatsTable": f3NetFpQosPolicerStatsTable,
       "f3NetFpQosPolicerStatsEntry": f3NetFpQosPolicerStatsEntry,
       "f3NetFpQosPolicerStatsIndex": f3NetFpQosPolicerStatsIndex,
       "f3NetFpQosPolicerStatsIntervalType": f3NetFpQosPolicerStatsIntervalType,
       "f3NetFpQosPolicerStatsValid": f3NetFpQosPolicerStatsValid,
       "f3NetFpQosPolicerStatsAction": f3NetFpQosPolicerStatsAction,
       "f3NetFpQosPolicerStatsFMG": f3NetFpQosPolicerStatsFMG,
       "f3NetFpQosPolicerStatsFMY": f3NetFpQosPolicerStatsFMY,
       "f3NetFpQosPolicerStatsFMRD": f3NetFpQosPolicerStatsFMRD,
       "f3NetFpQosPolicerStatsBytesIn": f3NetFpQosPolicerStatsBytesIn,
       "f3NetFpQosPolicerStatsBytesOut": f3NetFpQosPolicerStatsBytesOut,
       "f3NetFpQosPolicerStatsABR": f3NetFpQosPolicerStatsABR,
       "f3NetFpQosPolicerHistoryTable": f3NetFpQosPolicerHistoryTable,
       "f3NetFpQosPolicerHistoryEntry": f3NetFpQosPolicerHistoryEntry,
       "f3NetFpQosPolicerHistoryIndex": f3NetFpQosPolicerHistoryIndex,
       "f3NetFpQosPolicerHistoryTime": f3NetFpQosPolicerHistoryTime,
       "f3NetFpQosPolicerHistoryValid": f3NetFpQosPolicerHistoryValid,
       "f3NetFpQosPolicerHistoryAction": f3NetFpQosPolicerHistoryAction,
       "f3NetFpQosPolicerHistoryFMG": f3NetFpQosPolicerHistoryFMG,
       "f3NetFpQosPolicerHistoryFMY": f3NetFpQosPolicerHistoryFMY,
       "f3NetFpQosPolicerHistoryFMRD": f3NetFpQosPolicerHistoryFMRD,
       "f3NetFpQosPolicerHistoryBytesIn": f3NetFpQosPolicerHistoryBytesIn,
       "f3NetFpQosPolicerHistoryBytesOut": f3NetFpQosPolicerHistoryBytesOut,
       "f3NetFpQosPolicerHistoryABR": f3NetFpQosPolicerHistoryABR,
       "f3NetFpQosPolicerThresholdTable": f3NetFpQosPolicerThresholdTable,
       "f3NetFpQosPolicerThresholdEntry": f3NetFpQosPolicerThresholdEntry,
       "f3NetFpQosPolicerThresholdIndex": f3NetFpQosPolicerThresholdIndex,
       "f3NetFpQosPolicerThresholdInterval": f3NetFpQosPolicerThresholdInterval,
       "f3NetFpQosPolicerThresholdVariable": f3NetFpQosPolicerThresholdVariable,
       "f3NetFpQosPolicerThresholdValueLo": f3NetFpQosPolicerThresholdValueLo,
       "f3NetFpQosPolicerThresholdValueHi": f3NetFpQosPolicerThresholdValueHi,
       "f3NetFpQosPolicerThresholdMonValue": f3NetFpQosPolicerThresholdMonValue,
       "f3FpmPerfNotifications": f3FpmPerfNotifications,
       "f3AccFlowPointThresholdCrossingAlert": f3AccFlowPointThresholdCrossingAlert,
       "f3NetFlowPointThresholdCrossingAlert": f3NetFlowPointThresholdCrossingAlert,
       "f3MPFlowThresholdCrossingAlert": f3MPFlowThresholdCrossingAlert,
       "f3AccFpQosShaperThresholdCrossingAlert": f3AccFpQosShaperThresholdCrossingAlert,
       "f3NetFpQosShaperThresholdCrossingAlert": f3NetFpQosShaperThresholdCrossingAlert,
       "f3AccFpQosPolicerThresholdCrossingAlert": f3AccFpQosPolicerThresholdCrossingAlert,
       "f3NetFpQosPolicerThresholdCrossingAlert": f3NetFpQosPolicerThresholdCrossingAlert,
       "f3FpmConformance": f3FpmConformance,
       "f3FpmCompliances": f3FpmCompliances,
       "f3FpmCompliance": f3FpmCompliance,
       "f3FpmGroups": f3FpmGroups,
       "f3AccFlowPointGroup": f3AccFlowPointGroup,
       "f3AccFpQosShaperGroup": f3AccFpQosShaperGroup,
       "f3AccFpQosPolicerGroup": f3AccFpQosPolicerGroup,
       "f3MPFlowExtGroup": f3MPFlowExtGroup,
       "f3AccFlowPointCpdV2Group": f3AccFlowPointCpdV2Group,
       "f3AccFlowPointLearningConfigGroup": f3AccFlowPointLearningConfigGroup,
       "f3NetFlowPointGroup": f3NetFlowPointGroup,
       "f3NetFpQosShaperGroup": f3NetFpQosShaperGroup,
       "f3NetFpQosPolicerGroup": f3NetFpQosPolicerGroup,
       "f3NetFlowPointCpdV2Group": f3NetFlowPointCpdV2Group,
       "f3NetFlowPointLearningConfigGroup": f3NetFlowPointLearningConfigGroup,
       "f3AccFlowPointPerfGroup": f3AccFlowPointPerfGroup,
       "f3NetFlowPointPerfGroup": f3NetFlowPointPerfGroup,
       "f3MPFlowPerfGroup": f3MPFlowPerfGroup,
       "f3AccFpQosShaperPerfGroup": f3AccFpQosShaperPerfGroup,
       "f3NetFpQosShaperPerfGroup": f3NetFpQosShaperPerfGroup,
       "f3AccFpQosPolicerPerfGroup": f3AccFpQosPolicerPerfGroup,
       "f3NetFpQosPolicerPerfGroup": f3NetFpQosPolicerPerfGroup,
       "f3FpmPerfNotifGroup": f3FpmPerfNotifGroup}
)
