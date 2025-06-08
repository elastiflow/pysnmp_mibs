# SNMP MIB module (TIMETRA-ETH-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-ETH-TUNNEL-MIB.mib
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

(TmnxChassisIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxChassisIndex")

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

timetraEthTunnelMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 64)
)
if mibBuilder.loadTexts:
    timetraEthTunnelMIBModule.setRevisions(
        ("2014-02-01 00:00",
         "2009-02-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxEthTunnelIndex(TextualConvention, Unsigned32):
    status = "current"


class TmnxEthTunnelMemberIndex(TextualConvention, Unsigned32):
    status = "current"


class TmnxEthTunnelMemberList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("member1", 0),
          ("member2", 1),
          ("member3", 2),
          ("member4", 3),
          ("member5", 4),
          ("member6", 5),
          ("member7", 6),
          ("member8", 7),
          ("member9", 8),
          ("member10", 9),
          ("member11", 10),
          ("member12", 11),
          ("member13", 12),
          ("member14", 13),
          ("member15", 14),
          ("member16", 15))
    )


class TmnxEthTunnelApsPduType(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_TmnxEthTunnelConformance_ObjectIdentity = ObjectIdentity
tmnxEthTunnelConformance = _TmnxEthTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64)
)
_TmnxEthTunnelCompliances_ObjectIdentity = ObjectIdentity
tmnxEthTunnelCompliances = _TmnxEthTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 1)
)
_TmnxEthTunnelGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelGroups = _TmnxEthTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2)
)
_TmnxEthTunnelTSGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelTSGroups = _TmnxEthTunnelTSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 0)
)
_TmnxEthTunnelConfigGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelConfigGroups = _TmnxEthTunnelConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 1)
)
_TmnxEthTunnelOperGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelOperGroups = _TmnxEthTunnelOperGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 2)
)
_TmnxEthTunnelMemberGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelMemberGroups = _TmnxEthTunnelMemberGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 3)
)
_TmnxEthTunnelAPSGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelAPSGroups = _TmnxEthTunnelAPSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 4)
)
_TmnxEthTunnelNotifyGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelNotifyGroups = _TmnxEthTunnelNotifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 5)
)
_TmnxEthTunnelSAPGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelSAPGroups = _TmnxEthTunnelSAPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 6)
)
_TmnxEthTunnelLEGroups_ObjectIdentity = ObjectIdentity
tmnxEthTunnelLEGroups = _TmnxEthTunnelLEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 7)
)
_TmnxEthTunnelObjs_ObjectIdentity = ObjectIdentity
tmnxEthTunnelObjs = _TmnxEthTunnelObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64)
)
_TmnxEthTunnelConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxEthTunnelConfigTimeStamps = _TmnxEthTunnelConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 0)
)
_TmnxEthTunnelCfgTblLastChanged_Type = TimeStamp
_TmnxEthTunnelCfgTblLastChanged_Object = MibScalar
tmnxEthTunnelCfgTblLastChanged = _TmnxEthTunnelCfgTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 0, 1),
    _TmnxEthTunnelCfgTblLastChanged_Type()
)
tmnxEthTunnelCfgTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelCfgTblLastChanged.setStatus("current")
_TmnxEthTunnelMbrTblLastChanged_Type = TimeStamp
_TmnxEthTunnelMbrTblLastChanged_Object = MibScalar
tmnxEthTunnelMbrTblLastChanged = _TmnxEthTunnelMbrTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 0, 2),
    _TmnxEthTunnelMbrTblLastChanged_Type()
)
tmnxEthTunnelMbrTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelMbrTblLastChanged.setStatus("current")
_TmnxEthTunnelLETableChanged_Type = TimeStamp
_TmnxEthTunnelLETableChanged_Object = MibScalar
tmnxEthTunnelLETableChanged = _TmnxEthTunnelLETableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 0, 3),
    _TmnxEthTunnelLETableChanged_Type()
)
tmnxEthTunnelLETableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelLETableChanged.setStatus("current")
_TmnxEthTunnelSAPMbrTblChanged_Type = TimeStamp
_TmnxEthTunnelSAPMbrTblChanged_Object = MibScalar
tmnxEthTunnelSAPMbrTblChanged = _TmnxEthTunnelSAPMbrTblChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 0, 4),
    _TmnxEthTunnelSAPMbrTblChanged_Type()
)
tmnxEthTunnelSAPMbrTblChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelSAPMbrTblChanged.setStatus("current")
_TmnxEthTunnelConfigurations_ObjectIdentity = ObjectIdentity
tmnxEthTunnelConfigurations = _TmnxEthTunnelConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1)
)
_TmnxEthTunnelConfigTable_Object = MibTable
tmnxEthTunnelConfigTable = _TmnxEthTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelConfigTable.setStatus("current")
_TmnxEthTunnelConfigEntry_Object = MibTableRow
tmnxEthTunnelConfigEntry = _TmnxEthTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1, 1)
)
tmnxEthTunnelConfigEntry.setIndexNames(
    (0, "TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelIndex"),
)
if mibBuilder.loadTexts:
    tmnxEthTunnelConfigEntry.setStatus("current")


class _TmnxEthTunnelIndex_Type(TmnxEthTunnelIndex):
    """Custom type tmnxEthTunnelIndex based on TmnxEthTunnelIndex"""
    subtypeSpec = TmnxEthTunnelIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxEthTunnelIndex_Type.__name__ = "TmnxEthTunnelIndex"
_TmnxEthTunnelIndex_Object = MibTableColumn
tmnxEthTunnelIndex = _TmnxEthTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1, 1, 1),
    _TmnxEthTunnelIndex_Type()
)
tmnxEthTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEthTunnelIndex.setStatus("current")
_TmnxEthTunnelRowStatus_Type = RowStatus
_TmnxEthTunnelRowStatus_Object = MibTableColumn
tmnxEthTunnelRowStatus = _TmnxEthTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1, 1, 2),
    _TmnxEthTunnelRowStatus_Type()
)
tmnxEthTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelRowStatus.setStatus("current")
_TmnxEthTunnelTimeStamp_Type = TimeStamp
_TmnxEthTunnelTimeStamp_Object = MibTableColumn
tmnxEthTunnelTimeStamp = _TmnxEthTunnelTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1, 1, 3),
    _TmnxEthTunnelTimeStamp_Type()
)
tmnxEthTunnelTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelTimeStamp.setStatus("current")


class _TmnxEthTunnelHoldDownTimeMember_Type(Unsigned32):
    """Custom type tmnxEthTunnelHoldDownTimeMember based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxEthTunnelHoldDownTimeMember_Type.__name__ = "Unsigned32"
_TmnxEthTunnelHoldDownTimeMember_Object = MibTableColumn
tmnxEthTunnelHoldDownTimeMember = _TmnxEthTunnelHoldDownTimeMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1, 1, 4),
    _TmnxEthTunnelHoldDownTimeMember_Type()
)
tmnxEthTunnelHoldDownTimeMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelHoldDownTimeMember.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthTunnelHoldDownTimeMember.setUnits("centiseconds")


class _TmnxEthTunnelProtectionType_Type(Integer32):
    """Custom type tmnxEthTunnelProtectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g8031-1to1", 1),
          ("loadsharing", 2))
    )


_TmnxEthTunnelProtectionType_Type.__name__ = "Integer32"
_TmnxEthTunnelProtectionType_Object = MibTableColumn
tmnxEthTunnelProtectionType = _TmnxEthTunnelProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1, 1, 5),
    _TmnxEthTunnelProtectionType_Type()
)
tmnxEthTunnelProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelProtectionType.setStatus("current")


class _TmnxEthTunnelRevertTime_Type(Unsigned32):
    """Custom type tmnxEthTunnelRevertTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 720),
    )


_TmnxEthTunnelRevertTime_Type.__name__ = "Unsigned32"
_TmnxEthTunnelRevertTime_Object = MibTableColumn
tmnxEthTunnelRevertTime = _TmnxEthTunnelRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1, 1, 6),
    _TmnxEthTunnelRevertTime_Type()
)
tmnxEthTunnelRevertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelRevertTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthTunnelRevertTime.setUnits("seconds")


class _TmnxEthTunnelHoldUpTimeMember_Type(Unsigned32):
    """Custom type tmnxEthTunnelHoldUpTimeMember based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxEthTunnelHoldUpTimeMember_Type.__name__ = "Unsigned32"
_TmnxEthTunnelHoldUpTimeMember_Object = MibTableColumn
tmnxEthTunnelHoldUpTimeMember = _TmnxEthTunnelHoldUpTimeMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 1, 1, 7),
    _TmnxEthTunnelHoldUpTimeMember_Type()
)
tmnxEthTunnelHoldUpTimeMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelHoldUpTimeMember.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthTunnelHoldUpTimeMember.setUnits("deciseconds")
_TmnxEthTunnelOperTable_Object = MibTable
tmnxEthTunnelOperTable = _TmnxEthTunnelOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelOperTable.setStatus("current")
_TmnxEthTunnelOperEntry_Object = MibTableRow
tmnxEthTunnelOperEntry = _TmnxEthTunnelOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelOperEntry.setStatus("current")
_TmnxEthTunnelChassisIndex_Type = TmnxChassisIndex
_TmnxEthTunnelChassisIndex_Object = MibTableColumn
tmnxEthTunnelChassisIndex = _TmnxEthTunnelChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 2, 1, 1),
    _TmnxEthTunnelChassisIndex_Type()
)
tmnxEthTunnelChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelChassisIndex.setStatus("current")
_TmnxEthTunnelIfIndex_Type = InterfaceIndexOrZero
_TmnxEthTunnelIfIndex_Object = MibTableColumn
tmnxEthTunnelIfIndex = _TmnxEthTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 2, 1, 2),
    _TmnxEthTunnelIfIndex_Type()
)
tmnxEthTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelIfIndex.setStatus("current")
_TmnxEthTunnelMgmtMemberIfIndex_Type = InterfaceIndexOrZero
_TmnxEthTunnelMgmtMemberIfIndex_Object = MibTableColumn
tmnxEthTunnelMgmtMemberIfIndex = _TmnxEthTunnelMgmtMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 2, 1, 3),
    _TmnxEthTunnelMgmtMemberIfIndex_Type()
)
tmnxEthTunnelMgmtMemberIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelMgmtMemberIfIndex.setStatus("current")


class _TmnxEthTunnelActiveMembers_Type(TmnxEthTunnelMemberList):
    """Custom type tmnxEthTunnelActiveMembers based on TmnxEthTunnelMemberList"""
    defaultBinValue = "0"


_TmnxEthTunnelActiveMembers_Type.__name__ = "TmnxEthTunnelMemberList"
_TmnxEthTunnelActiveMembers_Object = MibTableColumn
tmnxEthTunnelActiveMembers = _TmnxEthTunnelActiveMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 2, 1, 4),
    _TmnxEthTunnelActiveMembers_Type()
)
tmnxEthTunnelActiveMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelActiveMembers.setStatus("current")
_TmnxEthTunnelRevertTimeCountDn_Type = Unsigned32
_TmnxEthTunnelRevertTimeCountDn_Object = MibTableColumn
tmnxEthTunnelRevertTimeCountDn = _TmnxEthTunnelRevertTimeCountDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 2, 1, 5),
    _TmnxEthTunnelRevertTimeCountDn_Type()
)
tmnxEthTunnelRevertTimeCountDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelRevertTimeCountDn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthTunnelRevertTimeCountDn.setUnits("seconds")
_TmnxEthTunnelMemberTable_Object = MibTable
tmnxEthTunnelMemberTable = _TmnxEthTunnelMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberTable.setStatus("current")
_TmnxEthTunnelMemberEntry_Object = MibTableRow
tmnxEthTunnelMemberEntry = _TmnxEthTunnelMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1)
)
tmnxEthTunnelMemberEntry.setIndexNames(
    (0, "TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelIndex"),
    (0, "TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberIndex"),
)
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberEntry.setStatus("current")


class _TmnxEthTunnelMemberIndex_Type(TmnxEthTunnelMemberIndex):
    """Custom type tmnxEthTunnelMemberIndex based on TmnxEthTunnelMemberIndex"""
    subtypeSpec = TmnxEthTunnelMemberIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxEthTunnelMemberIndex_Type.__name__ = "TmnxEthTunnelMemberIndex"
_TmnxEthTunnelMemberIndex_Object = MibTableColumn
tmnxEthTunnelMemberIndex = _TmnxEthTunnelMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 1),
    _TmnxEthTunnelMemberIndex_Type()
)
tmnxEthTunnelMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberIndex.setStatus("current")
_TmnxEthTunnelMemberRowStatus_Type = RowStatus
_TmnxEthTunnelMemberRowStatus_Object = MibTableColumn
tmnxEthTunnelMemberRowStatus = _TmnxEthTunnelMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 2),
    _TmnxEthTunnelMemberRowStatus_Type()
)
tmnxEthTunnelMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberRowStatus.setStatus("current")
_TmnxEthTunnelMemberTimeStamp_Type = TimeStamp
_TmnxEthTunnelMemberTimeStamp_Object = MibTableColumn
tmnxEthTunnelMemberTimeStamp = _TmnxEthTunnelMemberTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 3),
    _TmnxEthTunnelMemberTimeStamp_Type()
)
tmnxEthTunnelMemberTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberTimeStamp.setStatus("current")


class _TmnxEthTunnelMemberIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxEthTunnelMemberIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxEthTunnelMemberIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxEthTunnelMemberIfIndex_Object = MibTableColumn
tmnxEthTunnelMemberIfIndex = _TmnxEthTunnelMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 4),
    _TmnxEthTunnelMemberIfIndex_Type()
)
tmnxEthTunnelMemberIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberIfIndex.setStatus("current")


class _TmnxEthTunnelMemberIfCtlTag_Type(TmnxEncapVal):
    """Custom type tmnxEthTunnelMemberIfCtlTag based on TmnxEncapVal"""
    defaultValue = 4294967295


_TmnxEthTunnelMemberIfCtlTag_Type.__name__ = "TmnxEncapVal"
_TmnxEthTunnelMemberIfCtlTag_Object = MibTableColumn
tmnxEthTunnelMemberIfCtlTag = _TmnxEthTunnelMemberIfCtlTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 5),
    _TmnxEthTunnelMemberIfCtlTag_Type()
)
tmnxEthTunnelMemberIfCtlTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberIfCtlTag.setStatus("current")
_TmnxEthTunnelMemberDescription_Type = TItemDescription
_TmnxEthTunnelMemberDescription_Object = MibTableColumn
tmnxEthTunnelMemberDescription = _TmnxEthTunnelMemberDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 6),
    _TmnxEthTunnelMemberDescription_Type()
)
tmnxEthTunnelMemberDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberDescription.setStatus("current")


class _TmnxEthTunnelMemberAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxEthTunnelMemberAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxEthTunnelMemberAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxEthTunnelMemberAdminStatus_Object = MibTableColumn
tmnxEthTunnelMemberAdminStatus = _TmnxEthTunnelMemberAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 7),
    _TmnxEthTunnelMemberAdminStatus_Type()
)
tmnxEthTunnelMemberAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberAdminStatus.setStatus("current")
_TmnxEthTunnelMemberOperStatus_Type = TmnxOperState
_TmnxEthTunnelMemberOperStatus_Object = MibTableColumn
tmnxEthTunnelMemberOperStatus = _TmnxEthTunnelMemberOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 8),
    _TmnxEthTunnelMemberOperStatus_Type()
)
tmnxEthTunnelMemberOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberOperStatus.setStatus("current")


class _TmnxEthTunnelMemberPrecedence_Type(Unsigned32):
    """Custom type tmnxEthTunnelMemberPrecedence based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxEthTunnelMemberPrecedence_Type.__name__ = "Unsigned32"
_TmnxEthTunnelMemberPrecedence_Object = MibTableColumn
tmnxEthTunnelMemberPrecedence = _TmnxEthTunnelMemberPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 3, 1, 9),
    _TmnxEthTunnelMemberPrecedence_Type()
)
tmnxEthTunnelMemberPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelMemberPrecedence.setStatus("current")
_TmnxEthTunnelAPSConfigs_ObjectIdentity = ObjectIdentity
tmnxEthTunnelAPSConfigs = _TmnxEthTunnelAPSConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4)
)
_TmnxEthTunnelApsTable_Object = MibTable
tmnxEthTunnelApsTable = _TmnxEthTunnelApsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsTable.setStatus("current")
_TmnxEthTunnelApsEntry_Object = MibTableRow
tmnxEthTunnelApsEntry = _TmnxEthTunnelApsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 1, 1)
)
tmnxEthTunnelApsEntry.setIndexNames(
    (0, "TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelIndex"),
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsEntry.setStatus("current")
_TmnxEthTunnelApsRxPdu_Type = TmnxEthTunnelApsPduType
_TmnxEthTunnelApsRxPdu_Object = MibTableColumn
tmnxEthTunnelApsRxPdu = _TmnxEthTunnelApsRxPdu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 1, 1, 1),
    _TmnxEthTunnelApsRxPdu_Type()
)
tmnxEthTunnelApsRxPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsRxPdu.setStatus("current")
_TmnxEthTunnelApsTxPdu_Type = TmnxEthTunnelApsPduType
_TmnxEthTunnelApsTxPdu_Object = MibTableColumn
tmnxEthTunnelApsTxPdu = _TmnxEthTunnelApsTxPdu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 1, 1, 2),
    _TmnxEthTunnelApsTxPdu_Type()
)
tmnxEthTunnelApsTxPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsTxPdu.setStatus("current")


class _TmnxEthTunnelApsDefectStatus_Type(Bits):
    """Custom type tmnxEthTunnelApsDefectStatus based on Bits"""
    namedValues = NamedValues(
        *(("dFopCM", 0),
          ("dFopPM", 1),
          ("dFopNR", 2))
    )

_TmnxEthTunnelApsDefectStatus_Type.__name__ = "Bits"
_TmnxEthTunnelApsDefectStatus_Object = MibTableColumn
tmnxEthTunnelApsDefectStatus = _TmnxEthTunnelApsDefectStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 1, 1, 3),
    _TmnxEthTunnelApsDefectStatus_Type()
)
tmnxEthTunnelApsDefectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsDefectStatus.setStatus("current")
_TmnxEthTunnelApsSwitchoverTime_Type = TimeStamp
_TmnxEthTunnelApsSwitchoverTime_Object = MibTableColumn
tmnxEthTunnelApsSwitchoverTime = _TmnxEthTunnelApsSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 1, 1, 4),
    _TmnxEthTunnelApsSwitchoverTime_Type()
)
tmnxEthTunnelApsSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsSwitchoverTime.setStatus("current")
_TmnxEthTunnelApsMemberTable_Object = MibTable
tmnxEthTunnelApsMemberTable = _TmnxEthTunnelApsMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsMemberTable.setStatus("current")
_TmnxEthTunnelApsMemberEntry_Object = MibTableRow
tmnxEthTunnelApsMemberEntry = _TmnxEthTunnelApsMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 2, 1)
)
tmnxEthTunnelApsMemberEntry.setIndexNames(
    (0, "TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelIndex"),
    (0, "TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberIndex"),
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsMemberEntry.setStatus("current")
_TmnxEthTunnelApsMemberActCount_Type = Counter32
_TmnxEthTunnelApsMemberActCount_Object = MibTableColumn
tmnxEthTunnelApsMemberActCount = _TmnxEthTunnelApsMemberActCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 2, 1, 1),
    _TmnxEthTunnelApsMemberActCount_Type()
)
tmnxEthTunnelApsMemberActCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsMemberActCount.setStatus("current")
_TmnxEthTunnelApsMemberActTime_Type = Counter32
_TmnxEthTunnelApsMemberActTime_Object = MibTableColumn
tmnxEthTunnelApsMemberActTime = _TmnxEthTunnelApsMemberActTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 2, 1, 2),
    _TmnxEthTunnelApsMemberActTime_Type()
)
tmnxEthTunnelApsMemberActTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsMemberActTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsMemberActTime.setUnits("seconds")
_TmnxEthTunnelApsCommandTable_Object = MibTable
tmnxEthTunnelApsCommandTable = _TmnxEthTunnelApsCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsCommandTable.setStatus("current")
_TmnxEthTunnelApsCommandEntry_Object = MibTableRow
tmnxEthTunnelApsCommandEntry = _TmnxEthTunnelApsCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsCommandEntry.setStatus("current")


class _TmnxEthTunnelApsCommandSwitch_Type(Integer32):
    """Custom type tmnxEthTunnelApsCommandSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 0),
          ("clear", 1),
          ("lockoutOfSecondary", 2),
          ("forceSwitchPrimaryToSecondary", 3),
          ("manualSwitchPrimaryToSecondary", 4),
          ("exercise", 5))
    )


_TmnxEthTunnelApsCommandSwitch_Type.__name__ = "Integer32"
_TmnxEthTunnelApsCommandSwitch_Object = MibTableColumn
tmnxEthTunnelApsCommandSwitch = _TmnxEthTunnelApsCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 3, 1, 1),
    _TmnxEthTunnelApsCommandSwitch_Type()
)
tmnxEthTunnelApsCommandSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsCommandSwitch.setStatus("current")


class _TmnxEthTunnelApsCommandExsResult_Type(Integer32):
    """Custom type tmnxEthTunnelApsCommandExsResult based on Integer32"""
    defaultValue = 4

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
        *(("passed", 1),
          ("failed", 2),
          ("preempted", 3),
          ("unknown", 4))
    )


_TmnxEthTunnelApsCommandExsResult_Type.__name__ = "Integer32"
_TmnxEthTunnelApsCommandExsResult_Object = MibTableColumn
tmnxEthTunnelApsCommandExsResult = _TmnxEthTunnelApsCommandExsResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 4, 3, 1, 2),
    _TmnxEthTunnelApsCommandExsResult_Type()
)
tmnxEthTunnelApsCommandExsResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEthTunnelApsCommandExsResult.setStatus("current")
_TmnxEthTunnelLEConfigs_ObjectIdentity = ObjectIdentity
tmnxEthTunnelLEConfigs = _TmnxEthTunnelLEConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 5)
)
_TmnxEthTunnelLETable_Object = MibTable
tmnxEthTunnelLETable = _TmnxEthTunnelLETable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelLETable.setStatus("current")
_TmnxEthTunnelLEEntry_Object = MibTableRow
tmnxEthTunnelLEEntry = _TmnxEthTunnelLEEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 5, 1, 1)
)
tmnxEthTunnelLEEntry.setIndexNames(
    (0, "TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelIndex"),
)
if mibBuilder.loadTexts:
    tmnxEthTunnelLEEntry.setStatus("current")


class _TmnxEthTunnelLEAccessAdaptQos_Type(Integer32):
    """Custom type tmnxEthTunnelLEAccessAdaptQos based on Integer32"""
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
        *(("link", 1),
          ("distribute", 2),
          ("portFair", 3))
    )


_TmnxEthTunnelLEAccessAdaptQos_Type.__name__ = "Integer32"
_TmnxEthTunnelLEAccessAdaptQos_Object = MibTableColumn
tmnxEthTunnelLEAccessAdaptQos = _TmnxEthTunnelLEAccessAdaptQos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 5, 1, 1, 1),
    _TmnxEthTunnelLEAccessAdaptQos_Type()
)
tmnxEthTunnelLEAccessAdaptQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEthTunnelLEAccessAdaptQos.setStatus("current")


class _TmnxEthTunnelLEPerFpIngQueueing_Type(TruthValue):
    """Custom type tmnxEthTunnelLEPerFpIngQueueing based on TruthValue"""
    defaultValue = 2


_TmnxEthTunnelLEPerFpIngQueueing_Type.__name__ = "TruthValue"
_TmnxEthTunnelLEPerFpIngQueueing_Object = MibTableColumn
tmnxEthTunnelLEPerFpIngQueueing = _TmnxEthTunnelLEPerFpIngQueueing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 5, 1, 1, 2),
    _TmnxEthTunnelLEPerFpIngQueueing_Type()
)
tmnxEthTunnelLEPerFpIngQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEthTunnelLEPerFpIngQueueing.setStatus("current")


class _TmnxEthTunnelLEMbrThreshold_Type(Unsigned32):
    """Custom type tmnxEthTunnelLEMbrThreshold based on Unsigned32"""
    defaultValue = 0


_TmnxEthTunnelLEMbrThreshold_Type.__name__ = "Unsigned32"
_TmnxEthTunnelLEMbrThreshold_Object = MibTableColumn
tmnxEthTunnelLEMbrThreshold = _TmnxEthTunnelLEMbrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 5, 1, 1, 3),
    _TmnxEthTunnelLEMbrThreshold_Type()
)
tmnxEthTunnelLEMbrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEthTunnelLEMbrThreshold.setStatus("current")
_TmnxEthTunnelSAPConfigs_ObjectIdentity = ObjectIdentity
tmnxEthTunnelSAPConfigs = _TmnxEthTunnelSAPConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 6)
)
_TmnxEthTunnelSAPMemberTable_Object = MibTable
tmnxEthTunnelSAPMemberTable = _TmnxEthTunnelSAPMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxEthTunnelSAPMemberTable.setStatus("current")
_TmnxEthTunnelSAPMemberEntry_Object = MibTableRow
tmnxEthTunnelSAPMemberEntry = _TmnxEthTunnelSAPMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 6, 1, 1)
)
tmnxEthTunnelSAPMemberEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberIndex"),
)
if mibBuilder.loadTexts:
    tmnxEthTunnelSAPMemberEntry.setStatus("current")
_TmnxEthTunnelSAPMemberRowStatus_Type = RowStatus
_TmnxEthTunnelSAPMemberRowStatus_Object = MibTableColumn
tmnxEthTunnelSAPMemberRowStatus = _TmnxEthTunnelSAPMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 6, 1, 1, 1),
    _TmnxEthTunnelSAPMemberRowStatus_Type()
)
tmnxEthTunnelSAPMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelSAPMemberRowStatus.setStatus("current")


class _TmnxEthTunnelSAPMemberTagValue_Type(TmnxEncapVal):
    """Custom type tmnxEthTunnelSAPMemberTagValue based on TmnxEncapVal"""
    defaultValue = 4294967295


_TmnxEthTunnelSAPMemberTagValue_Type.__name__ = "TmnxEncapVal"
_TmnxEthTunnelSAPMemberTagValue_Object = MibTableColumn
tmnxEthTunnelSAPMemberTagValue = _TmnxEthTunnelSAPMemberTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 1, 6, 1, 1, 2),
    _TmnxEthTunnelSAPMemberTagValue_Type()
)
tmnxEthTunnelSAPMemberTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEthTunnelSAPMemberTagValue.setStatus("current")
_TmnxEthTunnelStatistics_ObjectIdentity = ObjectIdentity
tmnxEthTunnelStatistics = _TmnxEthTunnelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 64, 2)
)
_TmnxEthTunnelNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxEthTunnelNotifyPrefix = _TmnxEthTunnelNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64)
)
_TmnxEthTunnelNotifications_ObjectIdentity = ObjectIdentity
tmnxEthTunnelNotifications = _TmnxEthTunnelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0)
)
_TmnxEthTunnelApsNotifications_ObjectIdentity = ObjectIdentity
tmnxEthTunnelApsNotifications = _TmnxEthTunnelApsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0, 2)
)
tmnxEthTunnelConfigEntry.registerAugmentions(
    ("TIMETRA-ETH-TUNNEL-MIB",
     "tmnxEthTunnelOperEntry")
)
tmnxEthTunnelOperEntry.setIndexNames(*tmnxEthTunnelConfigEntry.getIndexNames())
tmnxEthTunnelApsMemberEntry.registerAugmentions(
    ("TIMETRA-ETH-TUNNEL-MIB",
     "tmnxEthTunnelApsCommandEntry")
)
tmnxEthTunnelApsCommandEntry.setIndexNames(*tmnxEthTunnelApsMemberEntry.getIndexNames())

# Managed Objects groups

tmnxEthTunnelTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 0, 1)
)
tmnxEthTunnelTimeStampGroup.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelCfgTblLastChanged"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelTimeStamp"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMbrTblLastChanged"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberTimeStamp"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelTimeStampGroup.setStatus("current")

tmnxEthTunnelTimeStampV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 0, 2)
)
tmnxEthTunnelTimeStampV8v0Group.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelSAPMbrTblChanged"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelLETableChanged"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelTimeStampV8v0Group.setStatus("current")

tmnxEthTunnelBaseConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 1, 1)
)
tmnxEthTunnelBaseConfigGroup.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelChassisIndex"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelRowStatus"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelHoldDownTimeMember"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelProtectionType"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelRevertTime"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelBaseConfigGroup.setStatus("current")

tmnxEthTunnelBaseConfigV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 1, 2)
)
tmnxEthTunnelBaseConfigV8v0Group.setObjects(
    ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelHoldUpTimeMember")
)
if mibBuilder.loadTexts:
    tmnxEthTunnelBaseConfigV8v0Group.setStatus("current")

tmnxEthTunnelBaseOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 2, 1)
)
tmnxEthTunnelBaseOperGroup.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelIfIndex"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMgmtMemberIfIndex"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelActiveMembers"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelRevertTimeCountDn"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelBaseOperGroup.setStatus("current")

tmnxEthTunnelBaseMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 3, 1)
)
tmnxEthTunnelBaseMemberGroup.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberRowStatus"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberIfIndex"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberIfCtlTag"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberDescription"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberAdminStatus"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberOperStatus"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberPrecedence"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelBaseMemberGroup.setStatus("current")

tmnxEthTunnelBaseAPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 4, 1)
)
tmnxEthTunnelBaseAPSGroup.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsRxPdu"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsTxPdu"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsDefectStatus"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsSwitchoverTime"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsMemberActCount"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsMemberActTime"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelBaseAPSGroup.setStatus("current")

tmnxEthTunnelBaseAPSV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 4, 2)
)
tmnxEthTunnelBaseAPSV8v0Group.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsCommandSwitch"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsCommandExsResult"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelBaseAPSV8v0Group.setStatus("current")

tmnxEthTunnelSAPMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 6, 1)
)
tmnxEthTunnelSAPMemberGroup.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelSAPMemberRowStatus"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelSAPMemberTagValue"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelSAPMemberGroup.setStatus("current")

tmnxEthTunnelLEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 7, 1)
)
tmnxEthTunnelLEGroup.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelLEAccessAdaptQos"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelLEPerFpIngQueueing"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelLEMbrThreshold"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelLEGroup.setStatus("current")


# Notification objects

tmnxEthTunnelApsCfgRaiseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0, 2, 1)
)
tmnxEthTunnelApsCfgRaiseAlarm.setObjects(
    ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsDefectStatus")
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsCfgRaiseAlarm.setStatus(
        "current"
    )

tmnxEthTunnelApsCfgClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0, 2, 2)
)
tmnxEthTunnelApsCfgClearAlarm.setObjects(
    ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsDefectStatus")
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsCfgClearAlarm.setStatus(
        "current"
    )

tmnxEthTunnelApsPrvsnRaiseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0, 2, 3)
)
tmnxEthTunnelApsPrvsnRaiseAlarm.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsDefectStatus"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsRxPdu"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsTxPdu"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsPrvsnRaiseAlarm.setStatus(
        "current"
    )

tmnxEthTunnelApsPrvsnClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0, 2, 4)
)
tmnxEthTunnelApsPrvsnClearAlarm.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsDefectStatus"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsRxPdu"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsTxPdu"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsPrvsnClearAlarm.setStatus(
        "current"
    )

tmnxEthTunnelApsNoRspRaiseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0, 2, 5)
)
tmnxEthTunnelApsNoRspRaiseAlarm.setObjects(
    ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsDefectStatus")
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsNoRspRaiseAlarm.setStatus(
        "current"
    )

tmnxEthTunnelApsNoRspClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0, 2, 6)
)
tmnxEthTunnelApsNoRspClearAlarm.setObjects(
    ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsDefectStatus")
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsNoRspClearAlarm.setStatus(
        "current"
    )

tmnxEthTunnelApsSwitchoverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 64, 0, 2, 7)
)
tmnxEthTunnelApsSwitchoverAlarm.setObjects(
    ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelMemberPrecedence")
)
if mibBuilder.loadTexts:
    tmnxEthTunnelApsSwitchoverAlarm.setStatus(
        "current"
    )


# Notifications groups

tmnxEthTunnelAPSNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 2, 5, 1)
)
tmnxEthTunnelAPSNotifyGroup.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsCfgRaiseAlarm"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsCfgClearAlarm"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsPrvsnRaiseAlarm"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsPrvsnClearAlarm"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsNoRspRaiseAlarm"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsNoRspClearAlarm"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelApsSwitchoverAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelAPSNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxEthTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 1, 1)
)
tmnxEthTunnelCompliance.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelTimeStampGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseConfigGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseOperGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseMemberGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseAPSGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelAPSNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelCompliance.setStatus(
        "obsolete"
    )

tmnxEthTunnelV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 64, 1, 2)
)
tmnxEthTunnelV8v0Compliance.setObjects(
      *(("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelTimeStampGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelTimeStampV8v0Group"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseConfigGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseConfigV8v0Group"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseOperGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseMemberGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseAPSGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelBaseAPSV8v0Group"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelAPSNotifyGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelLEGroup"),
        ("TIMETRA-ETH-TUNNEL-MIB", "tmnxEthTunnelSAPMemberGroup"))
)
if mibBuilder.loadTexts:
    tmnxEthTunnelV8v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ETH-TUNNEL-MIB",
    **{"TmnxEthTunnelIndex": TmnxEthTunnelIndex,
       "TmnxEthTunnelMemberIndex": TmnxEthTunnelMemberIndex,
       "TmnxEthTunnelMemberList": TmnxEthTunnelMemberList,
       "TmnxEthTunnelApsPduType": TmnxEthTunnelApsPduType,
       "timetraEthTunnelMIBModule": timetraEthTunnelMIBModule,
       "tmnxEthTunnelConformance": tmnxEthTunnelConformance,
       "tmnxEthTunnelCompliances": tmnxEthTunnelCompliances,
       "tmnxEthTunnelCompliance": tmnxEthTunnelCompliance,
       "tmnxEthTunnelV8v0Compliance": tmnxEthTunnelV8v0Compliance,
       "tmnxEthTunnelGroups": tmnxEthTunnelGroups,
       "tmnxEthTunnelTSGroups": tmnxEthTunnelTSGroups,
       "tmnxEthTunnelTimeStampGroup": tmnxEthTunnelTimeStampGroup,
       "tmnxEthTunnelTimeStampV8v0Group": tmnxEthTunnelTimeStampV8v0Group,
       "tmnxEthTunnelConfigGroups": tmnxEthTunnelConfigGroups,
       "tmnxEthTunnelBaseConfigGroup": tmnxEthTunnelBaseConfigGroup,
       "tmnxEthTunnelBaseConfigV8v0Group": tmnxEthTunnelBaseConfigV8v0Group,
       "tmnxEthTunnelOperGroups": tmnxEthTunnelOperGroups,
       "tmnxEthTunnelBaseOperGroup": tmnxEthTunnelBaseOperGroup,
       "tmnxEthTunnelMemberGroups": tmnxEthTunnelMemberGroups,
       "tmnxEthTunnelBaseMemberGroup": tmnxEthTunnelBaseMemberGroup,
       "tmnxEthTunnelAPSGroups": tmnxEthTunnelAPSGroups,
       "tmnxEthTunnelBaseAPSGroup": tmnxEthTunnelBaseAPSGroup,
       "tmnxEthTunnelBaseAPSV8v0Group": tmnxEthTunnelBaseAPSV8v0Group,
       "tmnxEthTunnelNotifyGroups": tmnxEthTunnelNotifyGroups,
       "tmnxEthTunnelAPSNotifyGroup": tmnxEthTunnelAPSNotifyGroup,
       "tmnxEthTunnelSAPGroups": tmnxEthTunnelSAPGroups,
       "tmnxEthTunnelSAPMemberGroup": tmnxEthTunnelSAPMemberGroup,
       "tmnxEthTunnelLEGroups": tmnxEthTunnelLEGroups,
       "tmnxEthTunnelLEGroup": tmnxEthTunnelLEGroup,
       "tmnxEthTunnelObjs": tmnxEthTunnelObjs,
       "tmnxEthTunnelConfigTimeStamps": tmnxEthTunnelConfigTimeStamps,
       "tmnxEthTunnelCfgTblLastChanged": tmnxEthTunnelCfgTblLastChanged,
       "tmnxEthTunnelMbrTblLastChanged": tmnxEthTunnelMbrTblLastChanged,
       "tmnxEthTunnelLETableChanged": tmnxEthTunnelLETableChanged,
       "tmnxEthTunnelSAPMbrTblChanged": tmnxEthTunnelSAPMbrTblChanged,
       "tmnxEthTunnelConfigurations": tmnxEthTunnelConfigurations,
       "tmnxEthTunnelConfigTable": tmnxEthTunnelConfigTable,
       "tmnxEthTunnelConfigEntry": tmnxEthTunnelConfigEntry,
       "tmnxEthTunnelIndex": tmnxEthTunnelIndex,
       "tmnxEthTunnelRowStatus": tmnxEthTunnelRowStatus,
       "tmnxEthTunnelTimeStamp": tmnxEthTunnelTimeStamp,
       "tmnxEthTunnelHoldDownTimeMember": tmnxEthTunnelHoldDownTimeMember,
       "tmnxEthTunnelProtectionType": tmnxEthTunnelProtectionType,
       "tmnxEthTunnelRevertTime": tmnxEthTunnelRevertTime,
       "tmnxEthTunnelHoldUpTimeMember": tmnxEthTunnelHoldUpTimeMember,
       "tmnxEthTunnelOperTable": tmnxEthTunnelOperTable,
       "tmnxEthTunnelOperEntry": tmnxEthTunnelOperEntry,
       "tmnxEthTunnelChassisIndex": tmnxEthTunnelChassisIndex,
       "tmnxEthTunnelIfIndex": tmnxEthTunnelIfIndex,
       "tmnxEthTunnelMgmtMemberIfIndex": tmnxEthTunnelMgmtMemberIfIndex,
       "tmnxEthTunnelActiveMembers": tmnxEthTunnelActiveMembers,
       "tmnxEthTunnelRevertTimeCountDn": tmnxEthTunnelRevertTimeCountDn,
       "tmnxEthTunnelMemberTable": tmnxEthTunnelMemberTable,
       "tmnxEthTunnelMemberEntry": tmnxEthTunnelMemberEntry,
       "tmnxEthTunnelMemberIndex": tmnxEthTunnelMemberIndex,
       "tmnxEthTunnelMemberRowStatus": tmnxEthTunnelMemberRowStatus,
       "tmnxEthTunnelMemberTimeStamp": tmnxEthTunnelMemberTimeStamp,
       "tmnxEthTunnelMemberIfIndex": tmnxEthTunnelMemberIfIndex,
       "tmnxEthTunnelMemberIfCtlTag": tmnxEthTunnelMemberIfCtlTag,
       "tmnxEthTunnelMemberDescription": tmnxEthTunnelMemberDescription,
       "tmnxEthTunnelMemberAdminStatus": tmnxEthTunnelMemberAdminStatus,
       "tmnxEthTunnelMemberOperStatus": tmnxEthTunnelMemberOperStatus,
       "tmnxEthTunnelMemberPrecedence": tmnxEthTunnelMemberPrecedence,
       "tmnxEthTunnelAPSConfigs": tmnxEthTunnelAPSConfigs,
       "tmnxEthTunnelApsTable": tmnxEthTunnelApsTable,
       "tmnxEthTunnelApsEntry": tmnxEthTunnelApsEntry,
       "tmnxEthTunnelApsRxPdu": tmnxEthTunnelApsRxPdu,
       "tmnxEthTunnelApsTxPdu": tmnxEthTunnelApsTxPdu,
       "tmnxEthTunnelApsDefectStatus": tmnxEthTunnelApsDefectStatus,
       "tmnxEthTunnelApsSwitchoverTime": tmnxEthTunnelApsSwitchoverTime,
       "tmnxEthTunnelApsMemberTable": tmnxEthTunnelApsMemberTable,
       "tmnxEthTunnelApsMemberEntry": tmnxEthTunnelApsMemberEntry,
       "tmnxEthTunnelApsMemberActCount": tmnxEthTunnelApsMemberActCount,
       "tmnxEthTunnelApsMemberActTime": tmnxEthTunnelApsMemberActTime,
       "tmnxEthTunnelApsCommandTable": tmnxEthTunnelApsCommandTable,
       "tmnxEthTunnelApsCommandEntry": tmnxEthTunnelApsCommandEntry,
       "tmnxEthTunnelApsCommandSwitch": tmnxEthTunnelApsCommandSwitch,
       "tmnxEthTunnelApsCommandExsResult": tmnxEthTunnelApsCommandExsResult,
       "tmnxEthTunnelLEConfigs": tmnxEthTunnelLEConfigs,
       "tmnxEthTunnelLETable": tmnxEthTunnelLETable,
       "tmnxEthTunnelLEEntry": tmnxEthTunnelLEEntry,
       "tmnxEthTunnelLEAccessAdaptQos": tmnxEthTunnelLEAccessAdaptQos,
       "tmnxEthTunnelLEPerFpIngQueueing": tmnxEthTunnelLEPerFpIngQueueing,
       "tmnxEthTunnelLEMbrThreshold": tmnxEthTunnelLEMbrThreshold,
       "tmnxEthTunnelSAPConfigs": tmnxEthTunnelSAPConfigs,
       "tmnxEthTunnelSAPMemberTable": tmnxEthTunnelSAPMemberTable,
       "tmnxEthTunnelSAPMemberEntry": tmnxEthTunnelSAPMemberEntry,
       "tmnxEthTunnelSAPMemberRowStatus": tmnxEthTunnelSAPMemberRowStatus,
       "tmnxEthTunnelSAPMemberTagValue": tmnxEthTunnelSAPMemberTagValue,
       "tmnxEthTunnelStatistics": tmnxEthTunnelStatistics,
       "tmnxEthTunnelNotifyPrefix": tmnxEthTunnelNotifyPrefix,
       "tmnxEthTunnelNotifications": tmnxEthTunnelNotifications,
       "tmnxEthTunnelApsNotifications": tmnxEthTunnelApsNotifications,
       "tmnxEthTunnelApsCfgRaiseAlarm": tmnxEthTunnelApsCfgRaiseAlarm,
       "tmnxEthTunnelApsCfgClearAlarm": tmnxEthTunnelApsCfgClearAlarm,
       "tmnxEthTunnelApsPrvsnRaiseAlarm": tmnxEthTunnelApsPrvsnRaiseAlarm,
       "tmnxEthTunnelApsPrvsnClearAlarm": tmnxEthTunnelApsPrvsnClearAlarm,
       "tmnxEthTunnelApsNoRspRaiseAlarm": tmnxEthTunnelApsNoRspRaiseAlarm,
       "tmnxEthTunnelApsNoRspClearAlarm": tmnxEthTunnelApsNoRspClearAlarm,
       "tmnxEthTunnelApsSwitchoverAlarm": tmnxEthTunnelApsSwitchoverAlarm}
)
