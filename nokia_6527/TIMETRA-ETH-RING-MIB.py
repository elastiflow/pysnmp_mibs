# SNMP MIB module (TIMETRA-ETH-RING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-ETH-RING-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:31 2025
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(TItemDescription,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxOperState")


# MODULE-IDENTITY

timetraEthRingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 72)
)
if mibBuilder.loadTexts:
    timetraEthRingMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1910-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxEthRingIndex(TextualConvention, Unsigned32):
    status = "current"


class TmnxEthRingPathIndex(TextualConvention, Integer32):
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



class TmnxEthRingRplNodeType(TextualConvention, Integer32):
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



class TmnxEthRingApsInfoType(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x-1x [1x:1x:1x:1x:1x:1x] 24x-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 32),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxEthRingConformance_ObjectIdentity = ObjectIdentity
tmnxEthRingConformance = _TmnxEthRingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72)
)
_TmnxEthRingCompliances_ObjectIdentity = ObjectIdentity
tmnxEthRingCompliances = _TmnxEthRingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 1)
)
_TmnxEthRingGroups_ObjectIdentity = ObjectIdentity
tmnxEthRingGroups = _TmnxEthRingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2)
)
_TmnxEthRingTSGroups_ObjectIdentity = ObjectIdentity
tmnxEthRingTSGroups = _TmnxEthRingTSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 0)
)
_TmnxEthRingConfigGroups_ObjectIdentity = ObjectIdentity
tmnxEthRingConfigGroups = _TmnxEthRingConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 1)
)
_TmnxEthRingOperGroups_ObjectIdentity = ObjectIdentity
tmnxEthRingOperGroups = _TmnxEthRingOperGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 2)
)
_TmnxEthRingMemberGroups_ObjectIdentity = ObjectIdentity
tmnxEthRingMemberGroups = _TmnxEthRingMemberGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 3)
)
_TmnxEthRingAPSGroups_ObjectIdentity = ObjectIdentity
tmnxEthRingAPSGroups = _TmnxEthRingAPSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 4)
)
_TmnxEthRingNotifyGroups_ObjectIdentity = ObjectIdentity
tmnxEthRingNotifyGroups = _TmnxEthRingNotifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 5)
)
_TmnxEthRingSAPGroups_ObjectIdentity = ObjectIdentity
tmnxEthRingSAPGroups = _TmnxEthRingSAPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 6)
)
_TmnxEthRingV9v0Groups_ObjectIdentity = ObjectIdentity
tmnxEthRingV9v0Groups = _TmnxEthRingV9v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 7)
)
_TmnxEthRingObjs_ObjectIdentity = ObjectIdentity
tmnxEthRingObjs = _TmnxEthRingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72)
)
_TmnxEthRingConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxEthRingConfigTimeStamps = _TmnxEthRingConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 0)
)
_TmnxEthRingCfgTblLastChanged_Type = TimeStamp
_TmnxEthRingCfgTblLastChanged_Object = MibScalar
tmnxEthRingCfgTblLastChanged = _TmnxEthRingCfgTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 0, 1),
    _TmnxEthRingCfgTblLastChanged_Type()
)
tmnxEthRingCfgTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingCfgTblLastChanged.setStatus("current")
_TmnxEthRingPathTblLastChanged_Type = TimeStamp
_TmnxEthRingPathTblLastChanged_Object = MibScalar
tmnxEthRingPathTblLastChanged = _TmnxEthRingPathTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 0, 2),
    _TmnxEthRingPathTblLastChanged_Type()
)
tmnxEthRingPathTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingPathTblLastChanged.setStatus("current")
_TmnxEthRingSAPPathTblChanged_Type = TimeStamp
_TmnxEthRingSAPPathTblChanged_Object = MibScalar
tmnxEthRingSAPPathTblChanged = _TmnxEthRingSAPPathTblChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 0, 4),
    _TmnxEthRingSAPPathTblChanged_Type()
)
tmnxEthRingSAPPathTblChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingSAPPathTblChanged.setStatus("current")
_TmnxEthRingConfigurations_ObjectIdentity = ObjectIdentity
tmnxEthRingConfigurations = _TmnxEthRingConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1)
)
_TmnxEthRingConfigTable_Object = MibTable
tmnxEthRingConfigTable = _TmnxEthRingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxEthRingConfigTable.setStatus("current")
_TmnxEthRingConfigEntry_Object = MibTableRow
tmnxEthRingConfigEntry = _TmnxEthRingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1)
)
tmnxEthRingConfigEntry.setIndexNames(
    (0, "TIMETRA-ETH-RING-MIB", "tmnxEthRingIndex"),
)
if mibBuilder.loadTexts:
    tmnxEthRingConfigEntry.setStatus("current")


class _TmnxEthRingIndex_Type(TmnxEthRingIndex):
    """Custom type tmnxEthRingIndex based on TmnxEthRingIndex"""
    subtypeSpec = TmnxEthRingIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_TmnxEthRingIndex_Type.__name__ = "TmnxEthRingIndex"
_TmnxEthRingIndex_Object = MibTableColumn
tmnxEthRingIndex = _TmnxEthRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 1),
    _TmnxEthRingIndex_Type()
)
tmnxEthRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEthRingIndex.setStatus("current")
_TmnxEthRingRowStatus_Type = RowStatus
_TmnxEthRingRowStatus_Object = MibTableColumn
tmnxEthRingRowStatus = _TmnxEthRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 2),
    _TmnxEthRingRowStatus_Type()
)
tmnxEthRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingRowStatus.setStatus("current")
_TmnxEthRingTimeStamp_Type = TimeStamp
_TmnxEthRingTimeStamp_Object = MibTableColumn
tmnxEthRingTimeStamp = _TmnxEthRingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 3),
    _TmnxEthRingTimeStamp_Type()
)
tmnxEthRingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingTimeStamp.setStatus("current")


class _TmnxEthRingDescription_Type(TItemDescription):
    """Custom type tmnxEthRingDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxEthRingDescription_Type.__name__ = "TItemDescription"
_TmnxEthRingDescription_Object = MibTableColumn
tmnxEthRingDescription = _TmnxEthRingDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 4),
    _TmnxEthRingDescription_Type()
)
tmnxEthRingDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingDescription.setStatus("current")


class _TmnxEthRingAdminState_Type(TmnxAdminState):
    """Custom type tmnxEthRingAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxEthRingAdminState_Type.__name__ = "TmnxAdminState"
_TmnxEthRingAdminState_Object = MibTableColumn
tmnxEthRingAdminState = _TmnxEthRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 5),
    _TmnxEthRingAdminState_Type()
)
tmnxEthRingAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingAdminState.setStatus("current")
_TmnxEthRingOperState_Type = TmnxOperState
_TmnxEthRingOperState_Object = MibTableColumn
tmnxEthRingOperState = _TmnxEthRingOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 6),
    _TmnxEthRingOperState_Type()
)
tmnxEthRingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingOperState.setStatus("current")


class _TmnxEthRingGuardTime_Type(Unsigned32):
    """Custom type tmnxEthRingGuardTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TmnxEthRingGuardTime_Type.__name__ = "Unsigned32"
_TmnxEthRingGuardTime_Object = MibTableColumn
tmnxEthRingGuardTime = _TmnxEthRingGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 7),
    _TmnxEthRingGuardTime_Type()
)
tmnxEthRingGuardTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingGuardTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthRingGuardTime.setUnits("deciseconds")


class _TmnxEthRingRevertTime_Type(Unsigned32):
    """Custom type tmnxEthRingRevertTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 720),
    )


_TmnxEthRingRevertTime_Type.__name__ = "Unsigned32"
_TmnxEthRingRevertTime_Object = MibTableColumn
tmnxEthRingRevertTime = _TmnxEthRingRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 8),
    _TmnxEthRingRevertTime_Type()
)
tmnxEthRingRevertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingRevertTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthRingRevertTime.setUnits("seconds")


class _TmnxEthRingRevertTimeCountDn_Type(Unsigned32):
    """Custom type tmnxEthRingRevertTimeCountDn based on Unsigned32"""
    defaultValue = 0


_TmnxEthRingRevertTimeCountDn_Type.__name__ = "Unsigned32"
_TmnxEthRingRevertTimeCountDn_Object = MibTableColumn
tmnxEthRingRevertTimeCountDn = _TmnxEthRingRevertTimeCountDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 9),
    _TmnxEthRingRevertTimeCountDn_Type()
)
tmnxEthRingRevertTimeCountDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingRevertTimeCountDn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthRingRevertTimeCountDn.setUnits("seconds")


class _TmnxEthRingCcmHoldDownTime_Type(Unsigned32):
    """Custom type tmnxEthRingCcmHoldDownTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxEthRingCcmHoldDownTime_Type.__name__ = "Unsigned32"
_TmnxEthRingCcmHoldDownTime_Object = MibTableColumn
tmnxEthRingCcmHoldDownTime = _TmnxEthRingCcmHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 10),
    _TmnxEthRingCcmHoldDownTime_Type()
)
tmnxEthRingCcmHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingCcmHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthRingCcmHoldDownTime.setUnits("centiseconds")


class _TmnxEthRingCcmHoldUpTime_Type(Unsigned32):
    """Custom type tmnxEthRingCcmHoldUpTime based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxEthRingCcmHoldUpTime_Type.__name__ = "Unsigned32"
_TmnxEthRingCcmHoldUpTime_Object = MibTableColumn
tmnxEthRingCcmHoldUpTime = _TmnxEthRingCcmHoldUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 11),
    _TmnxEthRingCcmHoldUpTime_Type()
)
tmnxEthRingCcmHoldUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingCcmHoldUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthRingCcmHoldUpTime.setUnits("deciseconds")


class _TmnxEthRingRplNode_Type(TmnxEthRingRplNodeType):
    """Custom type tmnxEthRingRplNode based on TmnxEthRingRplNodeType"""
    defaultValue = 0


_TmnxEthRingRplNode_Type.__name__ = "TmnxEthRingRplNodeType"
_TmnxEthRingRplNode_Object = MibTableColumn
tmnxEthRingRplNode = _TmnxEthRingRplNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 12),
    _TmnxEthRingRplNode_Type()
)
tmnxEthRingRplNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingRplNode.setStatus("current")
_TmnxEthRingNodeId_Type = MacAddress
_TmnxEthRingNodeId_Object = MibTableColumn
tmnxEthRingNodeId = _TmnxEthRingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 13),
    _TmnxEthRingNodeId_Type()
)
tmnxEthRingNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingNodeId.setStatus("current")
_TmnxEthRingTxApsPdu_Type = TmnxEthRingApsInfoType
_TmnxEthRingTxApsPdu_Object = MibTableColumn
tmnxEthRingTxApsPdu = _TmnxEthRingTxApsPdu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 14),
    _TmnxEthRingTxApsPdu_Type()
)
tmnxEthRingTxApsPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingTxApsPdu.setStatus("current")


class _TmnxEthRingDefectStatus_Type(Bits):
    """Custom type tmnxEthRingDefectStatus based on Bits"""
    namedValues = NamedValues(
        ("dFopPM", 0)
    )

_TmnxEthRingDefectStatus_Type.__name__ = "Bits"
_TmnxEthRingDefectStatus_Object = MibTableColumn
tmnxEthRingDefectStatus = _TmnxEthRingDefectStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 15),
    _TmnxEthRingDefectStatus_Type()
)
tmnxEthRingDefectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingDefectStatus.setStatus("current")


class _TmnxEthRingSubRingType_Type(Integer32):
    """Custom type tmnxEthRingSubRingType based on Integer32"""
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


_TmnxEthRingSubRingType_Type.__name__ = "Integer32"
_TmnxEthRingSubRingType_Object = MibTableColumn
tmnxEthRingSubRingType = _TmnxEthRingSubRingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 16),
    _TmnxEthRingSubRingType_Type()
)
tmnxEthRingSubRingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingSubRingType.setStatus("current")


class _TmnxEthRingSubRingInterconnectId_Type(Unsigned32):
    """Custom type tmnxEthRingSubRingInterconnectId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxEthRingSubRingInterconnectId_Type.__name__ = "Unsigned32"
_TmnxEthRingSubRingInterconnectId_Object = MibTableColumn
tmnxEthRingSubRingInterconnectId = _TmnxEthRingSubRingInterconnectId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 17),
    _TmnxEthRingSubRingInterconnectId_Type()
)
tmnxEthRingSubRingInterconnectId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingSubRingInterconnectId.setStatus("current")


class _TmnxEthRingSubRingPropTopChange_Type(TruthValue):
    """Custom type tmnxEthRingSubRingPropTopChange based on TruthValue"""
    defaultValue = 2


_TmnxEthRingSubRingPropTopChange_Type.__name__ = "TruthValue"
_TmnxEthRingSubRingPropTopChange_Object = MibTableColumn
tmnxEthRingSubRingPropTopChange = _TmnxEthRingSubRingPropTopChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 18),
    _TmnxEthRingSubRingPropTopChange_Type()
)
tmnxEthRingSubRingPropTopChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingSubRingPropTopChange.setStatus("current")


class _TmnxEthRingCompatibleVersion_Type(Integer32):
    """Custom type tmnxEthRingCompatibleVersion based on Integer32"""
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


_TmnxEthRingCompatibleVersion_Type.__name__ = "Integer32"
_TmnxEthRingCompatibleVersion_Object = MibTableColumn
tmnxEthRingCompatibleVersion = _TmnxEthRingCompatibleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 1, 1, 19),
    _TmnxEthRingCompatibleVersion_Type()
)
tmnxEthRingCompatibleVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingCompatibleVersion.setStatus("current")
_TmnxEthRingPathTable_Object = MibTable
tmnxEthRingPathTable = _TmnxEthRingPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxEthRingPathTable.setStatus("current")
_TmnxEthRingPathEntry_Object = MibTableRow
tmnxEthRingPathEntry = _TmnxEthRingPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1)
)
tmnxEthRingPathEntry.setIndexNames(
    (0, "TIMETRA-ETH-RING-MIB", "tmnxEthRingIndex"),
    (0, "TIMETRA-ETH-RING-MIB", "tmnxEthRingPathIndex"),
)
if mibBuilder.loadTexts:
    tmnxEthRingPathEntry.setStatus("current")
_TmnxEthRingPathIndex_Type = TmnxEthRingPathIndex
_TmnxEthRingPathIndex_Object = MibTableColumn
tmnxEthRingPathIndex = _TmnxEthRingPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 1),
    _TmnxEthRingPathIndex_Type()
)
tmnxEthRingPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEthRingPathIndex.setStatus("current")
_TmnxEthRingPathRowStatus_Type = RowStatus
_TmnxEthRingPathRowStatus_Object = MibTableColumn
tmnxEthRingPathRowStatus = _TmnxEthRingPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 2),
    _TmnxEthRingPathRowStatus_Type()
)
tmnxEthRingPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingPathRowStatus.setStatus("current")
_TmnxEthRingPathTimeStamp_Type = TimeStamp
_TmnxEthRingPathTimeStamp_Object = MibTableColumn
tmnxEthRingPathTimeStamp = _TmnxEthRingPathTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 3),
    _TmnxEthRingPathTimeStamp_Type()
)
tmnxEthRingPathTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingPathTimeStamp.setStatus("current")
_TmnxEthRingPathIfIndex_Type = InterfaceIndexOrZero
_TmnxEthRingPathIfIndex_Object = MibTableColumn
tmnxEthRingPathIfIndex = _TmnxEthRingPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 4),
    _TmnxEthRingPathIfIndex_Type()
)
tmnxEthRingPathIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingPathIfIndex.setStatus("current")
_TmnxEthRingPathIfRapsCcTag_Type = TmnxEncapVal
_TmnxEthRingPathIfRapsCcTag_Object = MibTableColumn
tmnxEthRingPathIfRapsCcTag = _TmnxEthRingPathIfRapsCcTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 5),
    _TmnxEthRingPathIfRapsCcTag_Type()
)
tmnxEthRingPathIfRapsCcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingPathIfRapsCcTag.setStatus("current")
_TmnxEthRingPathDescription_Type = TItemDescription
_TmnxEthRingPathDescription_Object = MibTableColumn
tmnxEthRingPathDescription = _TmnxEthRingPathDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 6),
    _TmnxEthRingPathDescription_Type()
)
tmnxEthRingPathDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingPathDescription.setStatus("current")


class _TmnxEthRingPathAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxEthRingPathAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxEthRingPathAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxEthRingPathAdminStatus_Object = MibTableColumn
tmnxEthRingPathAdminStatus = _TmnxEthRingPathAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 7),
    _TmnxEthRingPathAdminStatus_Type()
)
tmnxEthRingPathAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingPathAdminStatus.setStatus("current")
_TmnxEthRingPathOperStatus_Type = TmnxOperState
_TmnxEthRingPathOperStatus_Object = MibTableColumn
tmnxEthRingPathOperStatus = _TmnxEthRingPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 8),
    _TmnxEthRingPathOperStatus_Type()
)
tmnxEthRingPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingPathOperStatus.setStatus("current")


class _TmnxEthRingPathType_Type(Integer32):
    """Custom type tmnxEthRingPathType based on Integer32"""
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


_TmnxEthRingPathType_Type.__name__ = "Integer32"
_TmnxEthRingPathType_Object = MibTableColumn
tmnxEthRingPathType = _TmnxEthRingPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 9),
    _TmnxEthRingPathType_Type()
)
tmnxEthRingPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingPathType.setStatus("current")


class _TmnxEthRingPathFwdState_Type(Integer32):
    """Custom type tmnxEthRingPathFwdState based on Integer32"""
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


_TmnxEthRingPathFwdState_Type.__name__ = "Integer32"
_TmnxEthRingPathFwdState_Object = MibTableColumn
tmnxEthRingPathFwdState = _TmnxEthRingPathFwdState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 10),
    _TmnxEthRingPathFwdState_Type()
)
tmnxEthRingPathFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingPathFwdState.setStatus("current")
_TmnxEthRingPathFwdStateChgTime_Type = TimeStamp
_TmnxEthRingPathFwdStateChgTime_Object = MibTableColumn
tmnxEthRingPathFwdStateChgTime = _TmnxEthRingPathFwdStateChgTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 11),
    _TmnxEthRingPathFwdStateChgTime_Type()
)
tmnxEthRingPathFwdStateChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingPathFwdStateChgTime.setStatus("current")
_TmnxEthRingPathRxApsPdu_Type = TmnxEthRingApsInfoType
_TmnxEthRingPathRxApsPdu_Object = MibTableColumn
tmnxEthRingPathRxApsPdu = _TmnxEthRingPathRxApsPdu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 3, 1, 12),
    _TmnxEthRingPathRxApsPdu_Type()
)
tmnxEthRingPathRxApsPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingPathRxApsPdu.setStatus("current")
_TmnxEthRingSAPConfigs_ObjectIdentity = ObjectIdentity
tmnxEthRingSAPConfigs = _TmnxEthRingSAPConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 4)
)
_TmnxEthRingSAPPathTable_Object = MibTable
tmnxEthRingSAPPathTable = _TmnxEthRingSAPPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxEthRingSAPPathTable.setStatus("current")
_TmnxEthRingSAPPathEntry_Object = MibTableRow
tmnxEthRingSAPPathEntry = _TmnxEthRingSAPPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 4, 1, 1)
)
tmnxEthRingSAPPathEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxEthRingSAPPathEntry.setStatus("current")
_TmnxEthRingSAPPathIndex_Type = Unsigned32
_TmnxEthRingSAPPathIndex_Object = MibTableColumn
tmnxEthRingSAPPathIndex = _TmnxEthRingSAPPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 4, 1, 1, 1),
    _TmnxEthRingSAPPathIndex_Type()
)
tmnxEthRingSAPPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingSAPPathIndex.setStatus("current")
_TmnxEthRingSAPPathControlFlag_Type = TruthValue
_TmnxEthRingSAPPathControlFlag_Object = MibTableColumn
tmnxEthRingSAPPathControlFlag = _TmnxEthRingSAPPathControlFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 4, 1, 1, 2),
    _TmnxEthRingSAPPathControlFlag_Type()
)
tmnxEthRingSAPPathControlFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthRingSAPPathControlFlag.setStatus("current")
_TmnxEthRingCommandTable_Object = MibTable
tmnxEthRingCommandTable = _TmnxEthRingCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxEthRingCommandTable.setStatus("current")
_TmnxEthRingCommandEntry_Object = MibTableRow
tmnxEthRingCommandEntry = _TmnxEthRingCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxEthRingCommandEntry.setStatus("current")


class _TmnxEthRingCommandSwitch_Type(Integer32):
    """Custom type tmnxEthRingCommandSwitch based on Integer32"""
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


_TmnxEthRingCommandSwitch_Type.__name__ = "Integer32"
_TmnxEthRingCommandSwitch_Object = MibTableColumn
tmnxEthRingCommandSwitch = _TmnxEthRingCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 1, 5, 1, 1),
    _TmnxEthRingCommandSwitch_Type()
)
tmnxEthRingCommandSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthRingCommandSwitch.setStatus("current")
_TmnxEthRingStatistics_ObjectIdentity = ObjectIdentity
tmnxEthRingStatistics = _TmnxEthRingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 72, 2)
)
_TmnxEthRingNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxEthRingNotifyPrefix = _TmnxEthRingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 72)
)
_TmnxEthRingNotifications_ObjectIdentity = ObjectIdentity
tmnxEthRingNotifications = _TmnxEthRingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 72, 0)
)
_TmnxEthRingOprNotifications_ObjectIdentity = ObjectIdentity
tmnxEthRingOprNotifications = _TmnxEthRingOprNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 72, 0, 1)
)
_TmnxEthRingApsNotifications_ObjectIdentity = ObjectIdentity
tmnxEthRingApsNotifications = _TmnxEthRingApsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 72, 0, 2)
)
tmnxEthRingPathEntry.registerAugmentions(
    ("TIMETRA-ETH-RING-MIB",
     "tmnxEthRingCommandEntry")
)
tmnxEthRingCommandEntry.setIndexNames(*tmnxEthRingPathEntry.getIndexNames())

# Managed Objects groups

tmnxEthRingTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 0, 1)
)
tmnxEthRingTimeStampGroup.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingCfgTblLastChanged"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingTimeStamp"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathTblLastChanged"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathTimeStamp"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingSAPPathTblChanged"))
)
if mibBuilder.loadTexts:
    tmnxEthRingTimeStampGroup.setStatus("current")

tmnxEthRingBaseConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 1, 1)
)
tmnxEthRingBaseConfigGroup.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingRowStatus"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingDescription"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingAdminState"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingOperState"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingGuardTime"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingCcmHoldDownTime"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingCcmHoldUpTime"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingRevertTime"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingRevertTimeCountDn"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingRplNode"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingNodeId"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingTxApsPdu"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingDefectStatus"))
)
if mibBuilder.loadTexts:
    tmnxEthRingBaseConfigGroup.setStatus("current")

tmnxEthRingBasePathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 3, 1)
)
tmnxEthRingBasePathGroup.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathRowStatus"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathIfIndex"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathIfRapsCcTag"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathDescription"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathAdminStatus"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathOperStatus"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathType"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathFwdState"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathFwdStateChgTime"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathRxApsPdu"))
)
if mibBuilder.loadTexts:
    tmnxEthRingBasePathGroup.setStatus("current")

tmnxEthRingSAPPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 6, 1)
)
tmnxEthRingSAPPathGroup.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingSAPPathIndex"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingSAPPathControlFlag"))
)
if mibBuilder.loadTexts:
    tmnxEthRingSAPPathGroup.setStatus("current")

tmnxEthRingBaseConfigV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 7, 1)
)
tmnxEthRingBaseConfigV9v0Group.setObjects(
    ("TIMETRA-ETH-RING-MIB", "tmnxEthRingCompatibleVersion")
)
if mibBuilder.loadTexts:
    tmnxEthRingBaseConfigV9v0Group.setStatus("current")

tmnxEthRingSubRingV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 7, 2)
)
tmnxEthRingSubRingV9v0Group.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingSubRingType"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingSubRingInterconnectId"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingSubRingPropTopChange"))
)
if mibBuilder.loadTexts:
    tmnxEthRingSubRingV9v0Group.setStatus("current")

tmnxEthRingCommandV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 7, 3)
)
tmnxEthRingCommandV9v0Group.setObjects(
    ("TIMETRA-ETH-RING-MIB", "tmnxEthRingCommandSwitch")
)
if mibBuilder.loadTexts:
    tmnxEthRingCommandV9v0Group.setStatus("current")


# Notification objects

tmnxEthRingPathFwdStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 72, 0, 1, 1)
)
tmnxEthRingPathFwdStateChange.setObjects(
    ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathFwdState")
)
if mibBuilder.loadTexts:
    tmnxEthRingPathFwdStateChange.setStatus(
        "current"
    )

tmnxEthRingApsPrvsnRaiseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 72, 0, 2, 1)
)
tmnxEthRingApsPrvsnRaiseAlarm.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingTxApsPdu"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathRxApsPdu"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingDefectStatus"))
)
if mibBuilder.loadTexts:
    tmnxEthRingApsPrvsnRaiseAlarm.setStatus(
        "current"
    )

tmnxEthRingApsPrvsnClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 72, 0, 2, 2)
)
tmnxEthRingApsPrvsnClearAlarm.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingTxApsPdu"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathRxApsPdu"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingDefectStatus"))
)
if mibBuilder.loadTexts:
    tmnxEthRingApsPrvsnClearAlarm.setStatus(
        "current"
    )


# Notifications groups

tmnxEthRingOperNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 5, 1)
)
tmnxEthRingOperNotifyGroup.setObjects(
    ("TIMETRA-ETH-RING-MIB", "tmnxEthRingPathFwdStateChange")
)
if mibBuilder.loadTexts:
    tmnxEthRingOperNotifyGroup.setStatus(
        "current"
    )

tmnxEthRingApsNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 2, 5, 2)
)
tmnxEthRingApsNotifyGroup.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingApsPrvsnRaiseAlarm"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingApsPrvsnClearAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEthRingApsNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxEthRingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 1, 1)
)
tmnxEthRingCompliance.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingTimeStampGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingBaseConfigGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingBasePathGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingSAPPathGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingOperNotifyGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingApsNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxEthRingCompliance.setStatus(
        "obsolete"
    )

tmnxEthRingV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 72, 1, 2)
)
tmnxEthRingV9v0Compliance.setObjects(
      *(("TIMETRA-ETH-RING-MIB", "tmnxEthRingTimeStampGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingBaseConfigGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingBasePathGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingSAPPathGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingOperNotifyGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingApsNotifyGroup"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingBaseConfigV9v0Group"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingSubRingV9v0Group"),
        ("TIMETRA-ETH-RING-MIB", "tmnxEthRingCommandV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxEthRingV9v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ETH-RING-MIB",
    **{"TmnxEthRingIndex": TmnxEthRingIndex,
       "TmnxEthRingPathIndex": TmnxEthRingPathIndex,
       "TmnxEthRingRplNodeType": TmnxEthRingRplNodeType,
       "TmnxEthRingApsInfoType": TmnxEthRingApsInfoType,
       "timetraEthRingMIBModule": timetraEthRingMIBModule,
       "tmnxEthRingConformance": tmnxEthRingConformance,
       "tmnxEthRingCompliances": tmnxEthRingCompliances,
       "tmnxEthRingCompliance": tmnxEthRingCompliance,
       "tmnxEthRingV9v0Compliance": tmnxEthRingV9v0Compliance,
       "tmnxEthRingGroups": tmnxEthRingGroups,
       "tmnxEthRingTSGroups": tmnxEthRingTSGroups,
       "tmnxEthRingTimeStampGroup": tmnxEthRingTimeStampGroup,
       "tmnxEthRingConfigGroups": tmnxEthRingConfigGroups,
       "tmnxEthRingBaseConfigGroup": tmnxEthRingBaseConfigGroup,
       "tmnxEthRingOperGroups": tmnxEthRingOperGroups,
       "tmnxEthRingMemberGroups": tmnxEthRingMemberGroups,
       "tmnxEthRingBasePathGroup": tmnxEthRingBasePathGroup,
       "tmnxEthRingAPSGroups": tmnxEthRingAPSGroups,
       "tmnxEthRingNotifyGroups": tmnxEthRingNotifyGroups,
       "tmnxEthRingOperNotifyGroup": tmnxEthRingOperNotifyGroup,
       "tmnxEthRingApsNotifyGroup": tmnxEthRingApsNotifyGroup,
       "tmnxEthRingSAPGroups": tmnxEthRingSAPGroups,
       "tmnxEthRingSAPPathGroup": tmnxEthRingSAPPathGroup,
       "tmnxEthRingV9v0Groups": tmnxEthRingV9v0Groups,
       "tmnxEthRingBaseConfigV9v0Group": tmnxEthRingBaseConfigV9v0Group,
       "tmnxEthRingSubRingV9v0Group": tmnxEthRingSubRingV9v0Group,
       "tmnxEthRingCommandV9v0Group": tmnxEthRingCommandV9v0Group,
       "tmnxEthRingObjs": tmnxEthRingObjs,
       "tmnxEthRingConfigTimeStamps": tmnxEthRingConfigTimeStamps,
       "tmnxEthRingCfgTblLastChanged": tmnxEthRingCfgTblLastChanged,
       "tmnxEthRingPathTblLastChanged": tmnxEthRingPathTblLastChanged,
       "tmnxEthRingSAPPathTblChanged": tmnxEthRingSAPPathTblChanged,
       "tmnxEthRingConfigurations": tmnxEthRingConfigurations,
       "tmnxEthRingConfigTable": tmnxEthRingConfigTable,
       "tmnxEthRingConfigEntry": tmnxEthRingConfigEntry,
       "tmnxEthRingIndex": tmnxEthRingIndex,
       "tmnxEthRingRowStatus": tmnxEthRingRowStatus,
       "tmnxEthRingTimeStamp": tmnxEthRingTimeStamp,
       "tmnxEthRingDescription": tmnxEthRingDescription,
       "tmnxEthRingAdminState": tmnxEthRingAdminState,
       "tmnxEthRingOperState": tmnxEthRingOperState,
       "tmnxEthRingGuardTime": tmnxEthRingGuardTime,
       "tmnxEthRingRevertTime": tmnxEthRingRevertTime,
       "tmnxEthRingRevertTimeCountDn": tmnxEthRingRevertTimeCountDn,
       "tmnxEthRingCcmHoldDownTime": tmnxEthRingCcmHoldDownTime,
       "tmnxEthRingCcmHoldUpTime": tmnxEthRingCcmHoldUpTime,
       "tmnxEthRingRplNode": tmnxEthRingRplNode,
       "tmnxEthRingNodeId": tmnxEthRingNodeId,
       "tmnxEthRingTxApsPdu": tmnxEthRingTxApsPdu,
       "tmnxEthRingDefectStatus": tmnxEthRingDefectStatus,
       "tmnxEthRingSubRingType": tmnxEthRingSubRingType,
       "tmnxEthRingSubRingInterconnectId": tmnxEthRingSubRingInterconnectId,
       "tmnxEthRingSubRingPropTopChange": tmnxEthRingSubRingPropTopChange,
       "tmnxEthRingCompatibleVersion": tmnxEthRingCompatibleVersion,
       "tmnxEthRingPathTable": tmnxEthRingPathTable,
       "tmnxEthRingPathEntry": tmnxEthRingPathEntry,
       "tmnxEthRingPathIndex": tmnxEthRingPathIndex,
       "tmnxEthRingPathRowStatus": tmnxEthRingPathRowStatus,
       "tmnxEthRingPathTimeStamp": tmnxEthRingPathTimeStamp,
       "tmnxEthRingPathIfIndex": tmnxEthRingPathIfIndex,
       "tmnxEthRingPathIfRapsCcTag": tmnxEthRingPathIfRapsCcTag,
       "tmnxEthRingPathDescription": tmnxEthRingPathDescription,
       "tmnxEthRingPathAdminStatus": tmnxEthRingPathAdminStatus,
       "tmnxEthRingPathOperStatus": tmnxEthRingPathOperStatus,
       "tmnxEthRingPathType": tmnxEthRingPathType,
       "tmnxEthRingPathFwdState": tmnxEthRingPathFwdState,
       "tmnxEthRingPathFwdStateChgTime": tmnxEthRingPathFwdStateChgTime,
       "tmnxEthRingPathRxApsPdu": tmnxEthRingPathRxApsPdu,
       "tmnxEthRingSAPConfigs": tmnxEthRingSAPConfigs,
       "tmnxEthRingSAPPathTable": tmnxEthRingSAPPathTable,
       "tmnxEthRingSAPPathEntry": tmnxEthRingSAPPathEntry,
       "tmnxEthRingSAPPathIndex": tmnxEthRingSAPPathIndex,
       "tmnxEthRingSAPPathControlFlag": tmnxEthRingSAPPathControlFlag,
       "tmnxEthRingCommandTable": tmnxEthRingCommandTable,
       "tmnxEthRingCommandEntry": tmnxEthRingCommandEntry,
       "tmnxEthRingCommandSwitch": tmnxEthRingCommandSwitch,
       "tmnxEthRingStatistics": tmnxEthRingStatistics,
       "tmnxEthRingNotifyPrefix": tmnxEthRingNotifyPrefix,
       "tmnxEthRingNotifications": tmnxEthRingNotifications,
       "tmnxEthRingOprNotifications": tmnxEthRingOprNotifications,
       "tmnxEthRingPathFwdStateChange": tmnxEthRingPathFwdStateChange,
       "tmnxEthRingApsNotifications": tmnxEthRingApsNotifications,
       "tmnxEthRingApsPrvsnRaiseAlarm": tmnxEthRingApsPrvsnRaiseAlarm,
       "tmnxEthRingApsPrvsnClearAlarm": tmnxEthRingApsPrvsnClearAlarm}
)
