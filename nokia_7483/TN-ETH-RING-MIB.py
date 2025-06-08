# SNMP MIB module (TN-ETH-RING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-ETH-RING-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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

(tnSapEncapValue,
 tnSapPortId) = mibBuilder.importSymbols(
    "TN-SAP-MIB",
    "tnSapEncapValue",
    "tnSapPortId")

(tnSvcId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "tnSvcId")

(TItemDescription,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxOperState) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemDescription",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxOperState")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnEthRingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 72)
)
if mibBuilder.loadTexts:
    tnEthRingMIBModule.setRevisions(
        ("1913-06-28 00:00",
         "1910-01-01 00:00",
         "1912-12-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnEthRingIndex(TextualConvention, Unsigned32):
    status = "current"


class TnEthRingPathIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pathA", 0),
          ("pathB", 1))
    )



class TnEthRingRplNodeType(TextualConvention, Integer32):
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
        *(("rplNone", 0),
          ("rplOwner", 1),
          ("rplNeighbor", 2))
    )



class TnEthRingApsInfoType(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x-1x [1x:1x:1x:1x:1x:1x] 24x-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 32),
    )



# MIB Managed Objects in the order of their OIDs

_TnEthRingObjs_ObjectIdentity = ObjectIdentity
tnEthRingObjs = _TnEthRingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72)
)
_TnEthRingConfigurations_ObjectIdentity = ObjectIdentity
tnEthRingConfigurations = _TnEthRingConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1)
)
_TnEthRingConfigTable_Object = MibTable
tnEthRingConfigTable = _TnEthRingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1)
)
if mibBuilder.loadTexts:
    tnEthRingConfigTable.setStatus("current")
_TnEthRingConfigEntry_Object = MibTableRow
tnEthRingConfigEntry = _TnEthRingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1)
)
tnEthRingConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-ETH-RING-MIB", "tnEthRingIndex"),
)
if mibBuilder.loadTexts:
    tnEthRingConfigEntry.setStatus("current")


class _TnEthRingIndex_Type(TnEthRingIndex):
    """Custom type tnEthRingIndex based on TnEthRingIndex"""
    subtypeSpec = TnEthRingIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnEthRingIndex_Type.__name__ = "TnEthRingIndex"
_TnEthRingIndex_Object = MibTableColumn
tnEthRingIndex = _TnEthRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 1),
    _TnEthRingIndex_Type()
)
tnEthRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthRingIndex.setStatus("current")
_TnEthRingRowStatus_Type = RowStatus
_TnEthRingRowStatus_Object = MibTableColumn
tnEthRingRowStatus = _TnEthRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 2),
    _TnEthRingRowStatus_Type()
)
tnEthRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingRowStatus.setStatus("current")
_TnEthRingTimeStamp_Type = TimeStamp
_TnEthRingTimeStamp_Object = MibTableColumn
tnEthRingTimeStamp = _TnEthRingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 3),
    _TnEthRingTimeStamp_Type()
)
tnEthRingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingTimeStamp.setStatus("current")


class _TnEthRingDescription_Type(TItemDescription):
    """Custom type tnEthRingDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TnEthRingDescription_Type.__name__ = "TItemDescription"
_TnEthRingDescription_Object = MibTableColumn
tnEthRingDescription = _TnEthRingDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 4),
    _TnEthRingDescription_Type()
)
tnEthRingDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingDescription.setStatus("current")


class _TnEthRingAdminState_Type(TmnxAdminState):
    """Custom type tnEthRingAdminState based on TmnxAdminState"""
    defaultValue = 3


_TnEthRingAdminState_Type.__name__ = "TmnxAdminState"
_TnEthRingAdminState_Object = MibTableColumn
tnEthRingAdminState = _TnEthRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 5),
    _TnEthRingAdminState_Type()
)
tnEthRingAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingAdminState.setStatus("current")
_TnEthRingOperState_Type = TmnxOperState
_TnEthRingOperState_Object = MibTableColumn
tnEthRingOperState = _TnEthRingOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 6),
    _TnEthRingOperState_Type()
)
tnEthRingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingOperState.setStatus("current")


class _TnEthRingGuardTime_Type(Unsigned32):
    """Custom type tnEthRingGuardTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TnEthRingGuardTime_Type.__name__ = "Unsigned32"
_TnEthRingGuardTime_Object = MibTableColumn
tnEthRingGuardTime = _TnEthRingGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 7),
    _TnEthRingGuardTime_Type()
)
tnEthRingGuardTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingGuardTime.setStatus("current")
if mibBuilder.loadTexts:
    tnEthRingGuardTime.setUnits("deciseconds")


class _TnEthRingRevertTime_Type(Unsigned32):
    """Custom type tnEthRingRevertTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_TnEthRingRevertTime_Type.__name__ = "Unsigned32"
_TnEthRingRevertTime_Object = MibTableColumn
tnEthRingRevertTime = _TnEthRingRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 8),
    _TnEthRingRevertTime_Type()
)
tnEthRingRevertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingRevertTime.setStatus("current")
if mibBuilder.loadTexts:
    tnEthRingRevertTime.setUnits("seconds")


class _TnEthRingRevertTimeCountDn_Type(Unsigned32):
    """Custom type tnEthRingRevertTimeCountDn based on Unsigned32"""
    defaultValue = 0


_TnEthRingRevertTimeCountDn_Type.__name__ = "Unsigned32"
_TnEthRingRevertTimeCountDn_Object = MibTableColumn
tnEthRingRevertTimeCountDn = _TnEthRingRevertTimeCountDn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 9),
    _TnEthRingRevertTimeCountDn_Type()
)
tnEthRingRevertTimeCountDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingRevertTimeCountDn.setStatus("current")
if mibBuilder.loadTexts:
    tnEthRingRevertTimeCountDn.setUnits("seconds")


class _TnEthRingCcmHoldDownTime_Type(Unsigned32):
    """Custom type tnEthRingCcmHoldDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TnEthRingCcmHoldDownTime_Type.__name__ = "Unsigned32"
_TnEthRingCcmHoldDownTime_Object = MibTableColumn
tnEthRingCcmHoldDownTime = _TnEthRingCcmHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 10),
    _TnEthRingCcmHoldDownTime_Type()
)
tnEthRingCcmHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingCcmHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    tnEthRingCcmHoldDownTime.setUnits("deciseconds")


class _TnEthRingCcmHoldUpTime_Type(Unsigned32):
    """Custom type tnEthRingCcmHoldUpTime based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TnEthRingCcmHoldUpTime_Type.__name__ = "Unsigned32"
_TnEthRingCcmHoldUpTime_Object = MibTableColumn
tnEthRingCcmHoldUpTime = _TnEthRingCcmHoldUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 11),
    _TnEthRingCcmHoldUpTime_Type()
)
tnEthRingCcmHoldUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingCcmHoldUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tnEthRingCcmHoldUpTime.setUnits("deciseconds")


class _TnEthRingRplNode_Type(TnEthRingRplNodeType):
    """Custom type tnEthRingRplNode based on TnEthRingRplNodeType"""
    defaultValue = 0


_TnEthRingRplNode_Type.__name__ = "TnEthRingRplNodeType"
_TnEthRingRplNode_Object = MibTableColumn
tnEthRingRplNode = _TnEthRingRplNode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 12),
    _TnEthRingRplNode_Type()
)
tnEthRingRplNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingRplNode.setStatus("current")
_TnEthRingNodeId_Type = MacAddress
_TnEthRingNodeId_Object = MibTableColumn
tnEthRingNodeId = _TnEthRingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 13),
    _TnEthRingNodeId_Type()
)
tnEthRingNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingNodeId.setStatus("current")
_TnEthRingTxApsPdu_Type = TnEthRingApsInfoType
_TnEthRingTxApsPdu_Object = MibTableColumn
tnEthRingTxApsPdu = _TnEthRingTxApsPdu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 14),
    _TnEthRingTxApsPdu_Type()
)
tnEthRingTxApsPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingTxApsPdu.setStatus("current")


class _TnEthRingDefectStatus_Type(Bits):
    """Custom type tnEthRingDefectStatus based on Bits"""
    namedValues = NamedValues(
        ("dFopPM", 0)
    )

_TnEthRingDefectStatus_Type.__name__ = "Bits"
_TnEthRingDefectStatus_Object = MibTableColumn
tnEthRingDefectStatus = _TnEthRingDefectStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 15),
    _TnEthRingDefectStatus_Type()
)
tnEthRingDefectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingDefectStatus.setStatus("current")


class _TnEthRingSubRingType_Type(Integer32):
    """Custom type tnEthRingSubRingType based on Integer32"""
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
          ("virtualLink", 1),
          ("nonVirtualLink", 2))
    )


_TnEthRingSubRingType_Type.__name__ = "Integer32"
_TnEthRingSubRingType_Object = MibTableColumn
tnEthRingSubRingType = _TnEthRingSubRingType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 16),
    _TnEthRingSubRingType_Type()
)
tnEthRingSubRingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingSubRingType.setStatus("current")


class _TnEthRingSubRingInterconnectId_Type(Unsigned32):
    """Custom type tnEthRingSubRingInterconnectId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TnEthRingSubRingInterconnectId_Type.__name__ = "Unsigned32"
_TnEthRingSubRingInterconnectId_Object = MibTableColumn
tnEthRingSubRingInterconnectId = _TnEthRingSubRingInterconnectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 17),
    _TnEthRingSubRingInterconnectId_Type()
)
tnEthRingSubRingInterconnectId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingSubRingInterconnectId.setStatus("current")


class _TnEthRingSubRingPropTopChange_Type(TruthValue):
    """Custom type tnEthRingSubRingPropTopChange based on TruthValue"""
    defaultValue = 2


_TnEthRingSubRingPropTopChange_Type.__name__ = "TruthValue"
_TnEthRingSubRingPropTopChange_Object = MibTableColumn
tnEthRingSubRingPropTopChange = _TnEthRingSubRingPropTopChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 18),
    _TnEthRingSubRingPropTopChange_Type()
)
tnEthRingSubRingPropTopChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingSubRingPropTopChange.setStatus("current")


class _TnEthRingCompatibleVersion_Type(Integer32):
    """Custom type tnEthRingCompatibleVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_TnEthRingCompatibleVersion_Type.__name__ = "Integer32"
_TnEthRingCompatibleVersion_Object = MibTableColumn
tnEthRingCompatibleVersion = _TnEthRingCompatibleVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 1, 1, 19),
    _TnEthRingCompatibleVersion_Type()
)
tnEthRingCompatibleVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingCompatibleVersion.setStatus("current")
_TnEthRingPathTable_Object = MibTable
tnEthRingPathTable = _TnEthRingPathTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3)
)
if mibBuilder.loadTexts:
    tnEthRingPathTable.setStatus("current")
_TnEthRingPathEntry_Object = MibTableRow
tnEthRingPathEntry = _TnEthRingPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1)
)
tnEthRingPathEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-ETH-RING-MIB", "tnEthRingIndex"),
    (0, "TN-ETH-RING-MIB", "tnEthRingPathIndex"),
)
if mibBuilder.loadTexts:
    tnEthRingPathEntry.setStatus("current")
_TnEthRingPathIndex_Type = TnEthRingPathIndex
_TnEthRingPathIndex_Object = MibTableColumn
tnEthRingPathIndex = _TnEthRingPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 1),
    _TnEthRingPathIndex_Type()
)
tnEthRingPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthRingPathIndex.setStatus("current")
_TnEthRingPathRowStatus_Type = RowStatus
_TnEthRingPathRowStatus_Object = MibTableColumn
tnEthRingPathRowStatus = _TnEthRingPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 2),
    _TnEthRingPathRowStatus_Type()
)
tnEthRingPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingPathRowStatus.setStatus("current")
_TnEthRingPathTimeStamp_Type = TimeStamp
_TnEthRingPathTimeStamp_Object = MibTableColumn
tnEthRingPathTimeStamp = _TnEthRingPathTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 3),
    _TnEthRingPathTimeStamp_Type()
)
tnEthRingPathTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingPathTimeStamp.setStatus("current")
_TnEthRingPathIfIndex_Type = InterfaceIndexOrZero
_TnEthRingPathIfIndex_Object = MibTableColumn
tnEthRingPathIfIndex = _TnEthRingPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 4),
    _TnEthRingPathIfIndex_Type()
)
tnEthRingPathIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingPathIfIndex.setStatus("current")
_TnEthRingPathIfRapsCcTag_Type = TmnxEncapVal
_TnEthRingPathIfRapsCcTag_Object = MibTableColumn
tnEthRingPathIfRapsCcTag = _TnEthRingPathIfRapsCcTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 5),
    _TnEthRingPathIfRapsCcTag_Type()
)
tnEthRingPathIfRapsCcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingPathIfRapsCcTag.setStatus("current")
_TnEthRingPathDescription_Type = TItemDescription
_TnEthRingPathDescription_Object = MibTableColumn
tnEthRingPathDescription = _TnEthRingPathDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 6),
    _TnEthRingPathDescription_Type()
)
tnEthRingPathDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingPathDescription.setStatus("current")


class _TnEthRingPathAdminStatus_Type(TmnxAdminState):
    """Custom type tnEthRingPathAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TnEthRingPathAdminStatus_Type.__name__ = "TmnxAdminState"
_TnEthRingPathAdminStatus_Object = MibTableColumn
tnEthRingPathAdminStatus = _TnEthRingPathAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 7),
    _TnEthRingPathAdminStatus_Type()
)
tnEthRingPathAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingPathAdminStatus.setStatus("current")
_TnEthRingPathOperStatus_Type = TmnxOperState
_TnEthRingPathOperStatus_Object = MibTableColumn
tnEthRingPathOperStatus = _TnEthRingPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 8),
    _TnEthRingPathOperStatus_Type()
)
tnEthRingPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingPathOperStatus.setStatus("current")


class _TnEthRingPathType_Type(Integer32):
    """Custom type tnEthRingPathType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("rplEnd", 1))
    )


_TnEthRingPathType_Type.__name__ = "Integer32"
_TnEthRingPathType_Object = MibTableColumn
tnEthRingPathType = _TnEthRingPathType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 9),
    _TnEthRingPathType_Type()
)
tnEthRingPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingPathType.setStatus("current")


class _TnEthRingPathFwdState_Type(Integer32):
    """Custom type tnEthRingPathFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unblocked", 0),
          ("blocked", 1))
    )


_TnEthRingPathFwdState_Type.__name__ = "Integer32"
_TnEthRingPathFwdState_Object = MibTableColumn
tnEthRingPathFwdState = _TnEthRingPathFwdState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 10),
    _TnEthRingPathFwdState_Type()
)
tnEthRingPathFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingPathFwdState.setStatus("current")
_TnEthRingPathFwdStateChgTime_Type = TimeStamp
_TnEthRingPathFwdStateChgTime_Object = MibTableColumn
tnEthRingPathFwdStateChgTime = _TnEthRingPathFwdStateChgTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 11),
    _TnEthRingPathFwdStateChgTime_Type()
)
tnEthRingPathFwdStateChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingPathFwdStateChgTime.setStatus("current")
_TnEthRingPathRxApsPdu_Type = TnEthRingApsInfoType
_TnEthRingPathRxApsPdu_Object = MibTableColumn
tnEthRingPathRxApsPdu = _TnEthRingPathRxApsPdu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 3, 1, 12),
    _TnEthRingPathRxApsPdu_Type()
)
tnEthRingPathRxApsPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingPathRxApsPdu.setStatus("current")
_TnEthRingSAPConfigs_ObjectIdentity = ObjectIdentity
tnEthRingSAPConfigs = _TnEthRingSAPConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 4)
)
_TnEthRingSAPPathTable_Object = MibTable
tnEthRingSAPPathTable = _TnEthRingSAPPathTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnEthRingSAPPathTable.setStatus("current")
_TnEthRingSAPPathEntry_Object = MibTableRow
tnEthRingSAPPathEntry = _TnEthRingSAPPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 4, 1, 1)
)
tnEthRingSAPPathEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnEthRingSAPPathEntry.setStatus("current")
_TnEthRingSAPPathIndex_Type = Unsigned32
_TnEthRingSAPPathIndex_Object = MibTableColumn
tnEthRingSAPPathIndex = _TnEthRingSAPPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 4, 1, 1, 1),
    _TnEthRingSAPPathIndex_Type()
)
tnEthRingSAPPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingSAPPathIndex.setStatus("current")
_TnEthRingSAPPathControlFlag_Type = TruthValue
_TnEthRingSAPPathControlFlag_Object = MibTableColumn
tnEthRingSAPPathControlFlag = _TnEthRingSAPPathControlFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 4, 1, 1, 2),
    _TnEthRingSAPPathControlFlag_Type()
)
tnEthRingSAPPathControlFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingSAPPathControlFlag.setStatus("current")
_TnEthRingCommandTable_Object = MibTable
tnEthRingCommandTable = _TnEthRingCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 5)
)
if mibBuilder.loadTexts:
    tnEthRingCommandTable.setStatus("current")
_TnEthRingCommandEntry_Object = MibTableRow
tnEthRingCommandEntry = _TnEthRingCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnEthRingCommandEntry.setStatus("current")


class _TnEthRingCommandSwitch_Type(Integer32):
    """Custom type tnEthRingCommandSwitch based on Integer32"""
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
        *(("noCmd", 0),
          ("clear", 1),
          ("forceSwitch", 2),
          ("manualSwitch", 3))
    )


_TnEthRingCommandSwitch_Type.__name__ = "Integer32"
_TnEthRingCommandSwitch_Object = MibTableColumn
tnEthRingCommandSwitch = _TnEthRingCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 5, 1, 1),
    _TnEthRingCommandSwitch_Type()
)
tnEthRingCommandSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthRingCommandSwitch.setStatus("current")
_TnEthRingConfigurationsScalar1_Type = Unsigned32
_TnEthRingConfigurationsScalar1_Object = MibScalar
tnEthRingConfigurationsScalar1 = _TnEthRingConfigurationsScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 101),
    _TnEthRingConfigurationsScalar1_Type()
)
tnEthRingConfigurationsScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingConfigurationsScalar1.setStatus("current")
_TnEthRingConfigurationsScalar2_Type = Unsigned32
_TnEthRingConfigurationsScalar2_Object = MibScalar
tnEthRingConfigurationsScalar2 = _TnEthRingConfigurationsScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 72, 1, 102),
    _TnEthRingConfigurationsScalar2_Type()
)
tnEthRingConfigurationsScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthRingConfigurationsScalar2.setStatus("current")
_TnEthRingNotifyPrefix_ObjectIdentity = ObjectIdentity
tnEthRingNotifyPrefix = _TnEthRingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 72)
)
_TnEthRingNotifications_ObjectIdentity = ObjectIdentity
tnEthRingNotifications = _TnEthRingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 72, 0)
)
_TnEthRingOprNotifications_ObjectIdentity = ObjectIdentity
tnEthRingOprNotifications = _TnEthRingOprNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 72, 0, 1)
)
_TnEthRingApsNotifications_ObjectIdentity = ObjectIdentity
tnEthRingApsNotifications = _TnEthRingApsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 72, 0, 2)
)
tnEthRingPathEntry.registerAugmentions(
    ("TN-ETH-RING-MIB",
     "tnEthRingCommandEntry")
)
tnEthRingCommandEntry.setIndexNames(*tnEthRingPathEntry.getIndexNames())

# Managed Objects groups


# Notification objects

tnEthRingPathFwdStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 72, 0, 1, 1)
)
tnEthRingPathFwdStateChange.setObjects(
    ("TN-ETH-RING-MIB", "tnEthRingPathFwdState")
)
if mibBuilder.loadTexts:
    tnEthRingPathFwdStateChange.setStatus(
        "current"
    )

tnEthRingApsPrvsnRaiseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 72, 0, 2, 1)
)
tnEthRingApsPrvsnRaiseAlarm.setObjects(
      *(("TN-ETH-RING-MIB", "tnEthRingTxApsPdu"),
        ("TN-ETH-RING-MIB", "tnEthRingPathRxApsPdu"),
        ("TN-ETH-RING-MIB", "tnEthRingDefectStatus"))
)
if mibBuilder.loadTexts:
    tnEthRingApsPrvsnRaiseAlarm.setStatus(
        "current"
    )

tnEthRingApsPrvsnClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 72, 0, 2, 2)
)
tnEthRingApsPrvsnClearAlarm.setObjects(
      *(("TN-ETH-RING-MIB", "tnEthRingTxApsPdu"),
        ("TN-ETH-RING-MIB", "tnEthRingPathRxApsPdu"),
        ("TN-ETH-RING-MIB", "tnEthRingDefectStatus"))
)
if mibBuilder.loadTexts:
    tnEthRingApsPrvsnClearAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ETH-RING-MIB",
    **{"TnEthRingIndex": TnEthRingIndex,
       "TnEthRingPathIndex": TnEthRingPathIndex,
       "TnEthRingRplNodeType": TnEthRingRplNodeType,
       "TnEthRingApsInfoType": TnEthRingApsInfoType,
       "tnEthRingMIBModule": tnEthRingMIBModule,
       "tnEthRingObjs": tnEthRingObjs,
       "tnEthRingConfigurations": tnEthRingConfigurations,
       "tnEthRingConfigTable": tnEthRingConfigTable,
       "tnEthRingConfigEntry": tnEthRingConfigEntry,
       "tnEthRingIndex": tnEthRingIndex,
       "tnEthRingRowStatus": tnEthRingRowStatus,
       "tnEthRingTimeStamp": tnEthRingTimeStamp,
       "tnEthRingDescription": tnEthRingDescription,
       "tnEthRingAdminState": tnEthRingAdminState,
       "tnEthRingOperState": tnEthRingOperState,
       "tnEthRingGuardTime": tnEthRingGuardTime,
       "tnEthRingRevertTime": tnEthRingRevertTime,
       "tnEthRingRevertTimeCountDn": tnEthRingRevertTimeCountDn,
       "tnEthRingCcmHoldDownTime": tnEthRingCcmHoldDownTime,
       "tnEthRingCcmHoldUpTime": tnEthRingCcmHoldUpTime,
       "tnEthRingRplNode": tnEthRingRplNode,
       "tnEthRingNodeId": tnEthRingNodeId,
       "tnEthRingTxApsPdu": tnEthRingTxApsPdu,
       "tnEthRingDefectStatus": tnEthRingDefectStatus,
       "tnEthRingSubRingType": tnEthRingSubRingType,
       "tnEthRingSubRingInterconnectId": tnEthRingSubRingInterconnectId,
       "tnEthRingSubRingPropTopChange": tnEthRingSubRingPropTopChange,
       "tnEthRingCompatibleVersion": tnEthRingCompatibleVersion,
       "tnEthRingPathTable": tnEthRingPathTable,
       "tnEthRingPathEntry": tnEthRingPathEntry,
       "tnEthRingPathIndex": tnEthRingPathIndex,
       "tnEthRingPathRowStatus": tnEthRingPathRowStatus,
       "tnEthRingPathTimeStamp": tnEthRingPathTimeStamp,
       "tnEthRingPathIfIndex": tnEthRingPathIfIndex,
       "tnEthRingPathIfRapsCcTag": tnEthRingPathIfRapsCcTag,
       "tnEthRingPathDescription": tnEthRingPathDescription,
       "tnEthRingPathAdminStatus": tnEthRingPathAdminStatus,
       "tnEthRingPathOperStatus": tnEthRingPathOperStatus,
       "tnEthRingPathType": tnEthRingPathType,
       "tnEthRingPathFwdState": tnEthRingPathFwdState,
       "tnEthRingPathFwdStateChgTime": tnEthRingPathFwdStateChgTime,
       "tnEthRingPathRxApsPdu": tnEthRingPathRxApsPdu,
       "tnEthRingSAPConfigs": tnEthRingSAPConfigs,
       "tnEthRingSAPPathTable": tnEthRingSAPPathTable,
       "tnEthRingSAPPathEntry": tnEthRingSAPPathEntry,
       "tnEthRingSAPPathIndex": tnEthRingSAPPathIndex,
       "tnEthRingSAPPathControlFlag": tnEthRingSAPPathControlFlag,
       "tnEthRingCommandTable": tnEthRingCommandTable,
       "tnEthRingCommandEntry": tnEthRingCommandEntry,
       "tnEthRingCommandSwitch": tnEthRingCommandSwitch,
       "tnEthRingConfigurationsScalar1": tnEthRingConfigurationsScalar1,
       "tnEthRingConfigurationsScalar2": tnEthRingConfigurationsScalar2,
       "tnEthRingNotifyPrefix": tnEthRingNotifyPrefix,
       "tnEthRingNotifications": tnEthRingNotifications,
       "tnEthRingOprNotifications": tnEthRingOprNotifications,
       "tnEthRingPathFwdStateChange": tnEthRingPathFwdStateChange,
       "tnEthRingApsNotifications": tnEthRingApsNotifications,
       "tnEthRingApsPrvsnRaiseAlarm": tnEthRingApsPrvsnRaiseAlarm,
       "tnEthRingApsPrvsnClearAlarm": tnEthRingApsPrvsnClearAlarm}
)
