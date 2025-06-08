# SNMP MIB module (TIMETRA-MOBILE-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MOBILE-GATEWAY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:36 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(tmnxCardSlotNum,
 tmnxChassisIndex) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxMobGtpPriServerAddr,
 tmnxMobGtpPriServerAddrType,
 tmnxMobGtpPriServerPort,
 tmnxMobProfDiaPeerListIndex,
 tmnxMobProfDiaPeerName) = mibBuilder.importSymbols(
    "TIMETRA-MOBILE-PROFILE-MIB",
    "tmnxMobGtpPriServerAddr",
    "tmnxMobGtpPriServerAddrType",
    "tmnxMobGtpPriServerPort",
    "tmnxMobProfDiaPeerListIndex",
    "tmnxMobProfDiaPeerName")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxEnabledDisabled,
 TmnxMobDfPeerId,
 TmnxMobDiaDetailPathMgmtState,
 TmnxMobDiaPathMgmtState,
 TmnxMobGwId,
 TmnxMobGwType,
 TmnxMobLiTarget,
 TmnxMobLiTargetType,
 TmnxMobPathMgmtState,
 TmnxMobPeerType,
 TmnxMobProfName,
 TmnxOperState,
 TmnxThresholdGroupType,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxEnabledDisabled",
    "TmnxMobDfPeerId",
    "TmnxMobDiaDetailPathMgmtState",
    "TmnxMobDiaPathMgmtState",
    "TmnxMobGwId",
    "TmnxMobGwType",
    "TmnxMobLiTarget",
    "TmnxMobLiTargetType",
    "TmnxMobPathMgmtState",
    "TmnxMobPeerType",
    "TmnxMobProfName",
    "TmnxOperState",
    "TmnxThresholdGroupType",
    "TmnxVRtrID")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraMobGatewayMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 70)
)
if mibBuilder.loadTexts:
    timetraMobGatewayMIBModule.setRevisions(
        ("1909-12-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxMobGatewayConformance_ObjectIdentity = ObjectIdentity
tmnxMobGatewayConformance = _TmnxMobGatewayConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70)
)
_TmnxMobGatewayCompliances_ObjectIdentity = ObjectIdentity
tmnxMobGatewayCompliances = _TmnxMobGatewayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 1)
)
_TmnxMobGatewayGroups_ObjectIdentity = ObjectIdentity
tmnxMobGatewayGroups = _TmnxMobGatewayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2)
)
_TmnxMobGateway_ObjectIdentity = ObjectIdentity
tmnxMobGateway = _TmnxMobGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70)
)
_TmnxMobGatewayObjs_ObjectIdentity = ObjectIdentity
tmnxMobGatewayObjs = _TmnxMobGatewayObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1)
)
_TmnxMobGwTable_Object = MibTable
tmnxMobGwTable = _TmnxMobGwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxMobGwTable.setStatus("current")
_TmnxMobGwEntry_Object = MibTableRow
tmnxMobGwEntry = _TmnxMobGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 1, 1)
)
tmnxMobGwEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
)
if mibBuilder.loadTexts:
    tmnxMobGwEntry.setStatus("current")
_TmnxMobGwId_Type = TmnxMobGwId
_TmnxMobGwId_Object = MibTableColumn
tmnxMobGwId = _TmnxMobGwId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 1, 1, 1),
    _TmnxMobGwId_Type()
)
tmnxMobGwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwId.setStatus("current")
_TmnxMobGwRowStatus_Type = RowStatus
_TmnxMobGwRowStatus_Object = MibTableColumn
tmnxMobGwRowStatus = _TmnxMobGwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 1, 1, 2),
    _TmnxMobGwRowStatus_Type()
)
tmnxMobGwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwRowStatus.setStatus("current")
_TmnxMobGwLastChanged_Type = TimeStamp
_TmnxMobGwLastChanged_Object = MibTableColumn
tmnxMobGwLastChanged = _TmnxMobGwLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 1, 1, 3),
    _TmnxMobGwLastChanged_Type()
)
tmnxMobGwLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwLastChanged.setStatus("current")


class _TmnxMobGwDescription_Type(TItemDescription):
    """Custom type tmnxMobGwDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobGwDescription_Type.__name__ = "TItemDescription"
_TmnxMobGwDescription_Object = MibTableColumn
tmnxMobGwDescription = _TmnxMobGwDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 1, 1, 4),
    _TmnxMobGwDescription_Type()
)
tmnxMobGwDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwDescription.setStatus("current")
_TmnxMobGwType_Type = TmnxMobGwType
_TmnxMobGwType_Object = MibTableColumn
tmnxMobGwType = _TmnxMobGwType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 1, 1, 5),
    _TmnxMobGwType_Type()
)
tmnxMobGwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwType.setStatus("current")
_TmnxMobGwRestartCounter_Type = Unsigned32
_TmnxMobGwRestartCounter_Object = MibTableColumn
tmnxMobGwRestartCounter = _TmnxMobGwRestartCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 1, 1, 6),
    _TmnxMobGwRestartCounter_Type()
)
tmnxMobGwRestartCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRestartCounter.setStatus("current")
_TmnxMobGwSysGroupTable_Object = MibTable
tmnxMobGwSysGroupTable = _TmnxMobGwSysGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupTable.setStatus("current")
_TmnxMobGwSysGroupEntry_Object = MibTableRow
tmnxMobGwSysGroupEntry = _TmnxMobGwSysGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1)
)
tmnxMobGwSysGroupEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupId"),
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupEntry.setStatus("current")


class _TmnxMobGwSysGroupId_Type(Unsigned32):
    """Custom type tmnxMobGwSysGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMobGwSysGroupId_Type.__name__ = "Unsigned32"
_TmnxMobGwSysGroupId_Object = MibTableColumn
tmnxMobGwSysGroupId = _TmnxMobGwSysGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 1),
    _TmnxMobGwSysGroupId_Type()
)
tmnxMobGwSysGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupId.setStatus("current")
_TmnxMobGwSysGroupRowStatus_Type = RowStatus
_TmnxMobGwSysGroupRowStatus_Object = MibTableColumn
tmnxMobGwSysGroupRowStatus = _TmnxMobGwSysGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 2),
    _TmnxMobGwSysGroupRowStatus_Type()
)
tmnxMobGwSysGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupRowStatus.setStatus("current")
_TmnxMobGwSysGroupLastChanged_Type = TimeStamp
_TmnxMobGwSysGroupLastChanged_Object = MibTableColumn
tmnxMobGwSysGroupLastChanged = _TmnxMobGwSysGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 3),
    _TmnxMobGwSysGroupLastChanged_Type()
)
tmnxMobGwSysGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupLastChanged.setStatus("current")


class _TmnxMobGwSysGroupDescription_Type(TItemDescription):
    """Custom type tmnxMobGwSysGroupDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobGwSysGroupDescription_Type.__name__ = "TItemDescription"
_TmnxMobGwSysGroupDescription_Object = MibTableColumn
tmnxMobGwSysGroupDescription = _TmnxMobGwSysGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 4),
    _TmnxMobGwSysGroupDescription_Type()
)
tmnxMobGwSysGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupDescription.setStatus("current")
_TmnxMobGwSysGroupOperState_Type = TmnxOperState
_TmnxMobGwSysGroupOperState_Object = MibTableColumn
tmnxMobGwSysGroupOperState = _TmnxMobGwSysGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 5),
    _TmnxMobGwSysGroupOperState_Type()
)
tmnxMobGwSysGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupOperState.setStatus("current")
_TmnxMobGwSysGroupApp_Type = TmnxMobGwType
_TmnxMobGwSysGroupApp_Object = MibTableColumn
tmnxMobGwSysGroupApp = _TmnxMobGwSysGroupApp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 6),
    _TmnxMobGwSysGroupApp_Type()
)
tmnxMobGwSysGroupApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupApp.setStatus("current")


class _TmnxMobGwSysGroupRed_Type(Integer32):
    """Custom type tmnxMobGwSysGroupRed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("oneToOne", 1))
    )


_TmnxMobGwSysGroupRed_Type.__name__ = "Integer32"
_TmnxMobGwSysGroupRed_Object = MibTableColumn
tmnxMobGwSysGroupRed = _TmnxMobGwSysGroupRed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 7),
    _TmnxMobGwSysGroupRed_Type()
)
tmnxMobGwSysGroupRed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupRed.setStatus("current")
_TmnxMobGwSysGroupGateway_Type = TmnxMobGwId
_TmnxMobGwSysGroupGateway_Object = MibTableColumn
tmnxMobGwSysGroupGateway = _TmnxMobGwSysGroupGateway_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 8),
    _TmnxMobGwSysGroupGateway_Type()
)
tmnxMobGwSysGroupGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupGateway.setStatus("current")


class _TmnxMobGwSysGroupSysLimitName_Type(TmnxMobProfName):
    """Custom type tmnxMobGwSysGroupSysLimitName based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobGwSysGroupSysLimitName_Type.__name__ = "TmnxMobProfName"
_TmnxMobGwSysGroupSysLimitName_Object = MibTableColumn
tmnxMobGwSysGroupSysLimitName = _TmnxMobGwSysGroupSysLimitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 9),
    _TmnxMobGwSysGroupSysLimitName_Type()
)
tmnxMobGwSysGroupSysLimitName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupSysLimitName.setStatus("current")


class _TmnxMobGwSysGroupProtectDelay_Type(Unsigned32):
    """Custom type tmnxMobGwSysGroupProtectDelay based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TmnxMobGwSysGroupProtectDelay_Type.__name__ = "Unsigned32"
_TmnxMobGwSysGroupProtectDelay_Object = MibTableColumn
tmnxMobGwSysGroupProtectDelay = _TmnxMobGwSysGroupProtectDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 10),
    _TmnxMobGwSysGroupProtectDelay_Type()
)
tmnxMobGwSysGroupProtectDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupProtectDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupProtectDelay.setUnits("seconds")
_TmnxMobGwSysGroupSwitchoverCount_Type = Counter32
_TmnxMobGwSysGroupSwitchoverCount_Object = MibTableColumn
tmnxMobGwSysGroupSwitchoverCount = _TmnxMobGwSysGroupSwitchoverCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 11),
    _TmnxMobGwSysGroupSwitchoverCount_Type()
)
tmnxMobGwSysGroupSwitchoverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupSwitchoverCount.setStatus("current")
_TmnxMobGwSysGroupSwitchoverTime_Type = TimeStamp
_TmnxMobGwSysGroupSwitchoverTime_Object = MibTableColumn
tmnxMobGwSysGroupSwitchoverTime = _TmnxMobGwSysGroupSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 12),
    _TmnxMobGwSysGroupSwitchoverTime_Type()
)
tmnxMobGwSysGroupSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupSwitchoverTime.setStatus("current")


class _TmnxMobGwSysGroupRedState_Type(Integer32):
    """Custom type tmnxMobGwSysGroupRedState based on Integer32"""
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
        *(("none", 1),
          ("hot", 2),
          ("warm", 3),
          ("cold", 4))
    )


_TmnxMobGwSysGroupRedState_Type.__name__ = "Integer32"
_TmnxMobGwSysGroupRedState_Object = MibTableColumn
tmnxMobGwSysGroupRedState = _TmnxMobGwSysGroupRedState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 2, 1, 13),
    _TmnxMobGwSysGroupRedState_Type()
)
tmnxMobGwSysGroupRedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupRedState.setStatus("current")
_TmnxMobGwSysGroupCardTable_Object = MibTable
tmnxMobGwSysGroupCardTable = _TmnxMobGwSysGroupCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupCardTable.setStatus("current")
_TmnxMobGwSysGroupCardEntry_Object = MibTableRow
tmnxMobGwSysGroupCardEntry = _TmnxMobGwSysGroupCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 3, 1)
)
tmnxMobGwSysGroupCardEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupCardEntry.setStatus("current")
_TmnxMobGwSysGroupCardRowStatus_Type = RowStatus
_TmnxMobGwSysGroupCardRowStatus_Object = MibTableColumn
tmnxMobGwSysGroupCardRowStatus = _TmnxMobGwSysGroupCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 3, 1, 1),
    _TmnxMobGwSysGroupCardRowStatus_Type()
)
tmnxMobGwSysGroupCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupCardRowStatus.setStatus("current")
_TmnxMobGwSysGroupCardLastChanged_Type = TimeStamp
_TmnxMobGwSysGroupCardLastChanged_Object = MibTableColumn
tmnxMobGwSysGroupCardLastChanged = _TmnxMobGwSysGroupCardLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 3, 1, 2),
    _TmnxMobGwSysGroupCardLastChanged_Type()
)
tmnxMobGwSysGroupCardLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupCardLastChanged.setStatus("current")


class _TmnxMobGwSysGroupCardRole_Type(Integer32):
    """Custom type tmnxMobGwSysGroupCardRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protect", 2))
    )


_TmnxMobGwSysGroupCardRole_Type.__name__ = "Integer32"
_TmnxMobGwSysGroupCardRole_Object = MibTableColumn
tmnxMobGwSysGroupCardRole = _TmnxMobGwSysGroupCardRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 3, 1, 3),
    _TmnxMobGwSysGroupCardRole_Type()
)
tmnxMobGwSysGroupCardRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupCardRole.setStatus("current")


class _TmnxMobGwSysGroupCardRedState_Type(Integer32):
    """Custom type tmnxMobGwSysGroupCardRedState based on Integer32"""
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
        *(("notValid", 1),
          ("active", 2),
          ("standby", 3),
          ("standbyInProg", 4))
    )


_TmnxMobGwSysGroupCardRedState_Type.__name__ = "Integer32"
_TmnxMobGwSysGroupCardRedState_Object = MibTableColumn
tmnxMobGwSysGroupCardRedState = _TmnxMobGwSysGroupCardRedState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 3, 1, 4),
    _TmnxMobGwSysGroupCardRedState_Type()
)
tmnxMobGwSysGroupCardRedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupCardRedState.setStatus("current")
_TmnxMobGwS5PeerTable_Object = MibTable
tmnxMobGwS5PeerTable = _TmnxMobGwS5PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerTable.setStatus("current")
_TmnxMobGwS5PeerEntry_Object = MibTableRow
tmnxMobGwS5PeerEntry = _TmnxMobGwS5PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1)
)
tmnxMobGwS5PeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerAddressType"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerAddress"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerEntry.setStatus("current")
_TmnxMobGwS5PeerAddressType_Type = InetAddressType
_TmnxMobGwS5PeerAddressType_Object = MibTableColumn
tmnxMobGwS5PeerAddressType = _TmnxMobGwS5PeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1, 1),
    _TmnxMobGwS5PeerAddressType_Type()
)
tmnxMobGwS5PeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerAddressType.setStatus("current")


class _TmnxMobGwS5PeerAddress_Type(InetAddress):
    """Custom type tmnxMobGwS5PeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobGwS5PeerAddress_Type.__name__ = "InetAddress"
_TmnxMobGwS5PeerAddress_Object = MibTableColumn
tmnxMobGwS5PeerAddress = _TmnxMobGwS5PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1, 2),
    _TmnxMobGwS5PeerAddress_Type()
)
tmnxMobGwS5PeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerAddress.setStatus("current")
_TmnxMobGwS5PeerPort_Type = InetPortNumber
_TmnxMobGwS5PeerPort_Object = MibTableColumn
tmnxMobGwS5PeerPort = _TmnxMobGwS5PeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1, 3),
    _TmnxMobGwS5PeerPort_Type()
)
tmnxMobGwS5PeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerPort.setStatus("current")
_TmnxMobGwS5PeerLastChanged_Type = TimeStamp
_TmnxMobGwS5PeerLastChanged_Object = MibTableColumn
tmnxMobGwS5PeerLastChanged = _TmnxMobGwS5PeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1, 4),
    _TmnxMobGwS5PeerLastChanged_Type()
)
tmnxMobGwS5PeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerLastChanged.setStatus("current")
_TmnxMobGwS5PeerCreateTime_Type = TimeStamp
_TmnxMobGwS5PeerCreateTime_Object = MibTableColumn
tmnxMobGwS5PeerCreateTime = _TmnxMobGwS5PeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1, 5),
    _TmnxMobGwS5PeerCreateTime_Type()
)
tmnxMobGwS5PeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerCreateTime.setStatus("current")
_TmnxMobGwS5PeerPathMgmtState_Type = TmnxMobPathMgmtState
_TmnxMobGwS5PeerPathMgmtState_Object = MibTableColumn
tmnxMobGwS5PeerPathMgmtState = _TmnxMobGwS5PeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1, 6),
    _TmnxMobGwS5PeerPathMgmtState_Type()
)
tmnxMobGwS5PeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerPathMgmtState.setStatus("current")
_TmnxMobGwS5PeerGatewayId_Type = TmnxMobGwId
_TmnxMobGwS5PeerGatewayId_Object = MibTableColumn
tmnxMobGwS5PeerGatewayId = _TmnxMobGwS5PeerGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1, 7),
    _TmnxMobGwS5PeerGatewayId_Type()
)
tmnxMobGwS5PeerGatewayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerGatewayId.setStatus("current")
_TmnxMobGwS5PeerType_Type = TmnxMobPeerType
_TmnxMobGwS5PeerType_Object = MibTableColumn
tmnxMobGwS5PeerType = _TmnxMobGwS5PeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 4, 1, 8),
    _TmnxMobGwS5PeerType_Type()
)
tmnxMobGwS5PeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerType.setStatus("current")
_TmnxMobGwS5StatTable_Object = MibTable
tmnxMobGwS5StatTable = _TmnxMobGwS5StatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxMobGwS5StatTable.setStatus("current")
_TmnxMobGwS5StatEntry_Object = MibTableRow
tmnxMobGwS5StatEntry = _TmnxMobGwS5StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1)
)
tmnxMobGwS5StatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerAddressType"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerAddress"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobGwS5StatEntry.setStatus("current")
_TmnxMobGwS5StatCreateSessnReq_Type = Counter32
_TmnxMobGwS5StatCreateSessnReq_Object = MibTableColumn
tmnxMobGwS5StatCreateSessnReq = _TmnxMobGwS5StatCreateSessnReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 1),
    _TmnxMobGwS5StatCreateSessnReq_Type()
)
tmnxMobGwS5StatCreateSessnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatCreateSessnReq.setStatus("current")
_TmnxMobGwS5StatCreateSessnResp_Type = Counter32
_TmnxMobGwS5StatCreateSessnResp_Object = MibTableColumn
tmnxMobGwS5StatCreateSessnResp = _TmnxMobGwS5StatCreateSessnResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 2),
    _TmnxMobGwS5StatCreateSessnResp_Type()
)
tmnxMobGwS5StatCreateSessnResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatCreateSessnResp.setStatus("current")
_TmnxMobGwS5StatDeleteSessnReq_Type = Counter32
_TmnxMobGwS5StatDeleteSessnReq_Object = MibTableColumn
tmnxMobGwS5StatDeleteSessnReq = _TmnxMobGwS5StatDeleteSessnReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 3),
    _TmnxMobGwS5StatDeleteSessnReq_Type()
)
tmnxMobGwS5StatDeleteSessnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeleteSessnReq.setStatus("current")
_TmnxMobGwS5StatDeleteSessnResp_Type = Counter32
_TmnxMobGwS5StatDeleteSessnResp_Object = MibTableColumn
tmnxMobGwS5StatDeleteSessnResp = _TmnxMobGwS5StatDeleteSessnResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 4),
    _TmnxMobGwS5StatDeleteSessnResp_Type()
)
tmnxMobGwS5StatDeleteSessnResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeleteSessnResp.setStatus("current")
_TmnxMobGwS5StatCreateBearerReq_Type = Counter32
_TmnxMobGwS5StatCreateBearerReq_Object = MibTableColumn
tmnxMobGwS5StatCreateBearerReq = _TmnxMobGwS5StatCreateBearerReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 5),
    _TmnxMobGwS5StatCreateBearerReq_Type()
)
tmnxMobGwS5StatCreateBearerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatCreateBearerReq.setStatus("current")
_TmnxMobGwS5StatCreateBearerRsp_Type = Counter32
_TmnxMobGwS5StatCreateBearerRsp_Object = MibTableColumn
tmnxMobGwS5StatCreateBearerRsp = _TmnxMobGwS5StatCreateBearerRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 6),
    _TmnxMobGwS5StatCreateBearerRsp_Type()
)
tmnxMobGwS5StatCreateBearerRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatCreateBearerRsp.setStatus("current")
_TmnxMobGwS5StatDeleteBearerReq_Type = Counter32
_TmnxMobGwS5StatDeleteBearerReq_Object = MibTableColumn
tmnxMobGwS5StatDeleteBearerReq = _TmnxMobGwS5StatDeleteBearerReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 7),
    _TmnxMobGwS5StatDeleteBearerReq_Type()
)
tmnxMobGwS5StatDeleteBearerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeleteBearerReq.setStatus("current")
_TmnxMobGwS5StatDeleteBearerRsp_Type = Counter32
_TmnxMobGwS5StatDeleteBearerRsp_Object = MibTableColumn
tmnxMobGwS5StatDeleteBearerRsp = _TmnxMobGwS5StatDeleteBearerRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 8),
    _TmnxMobGwS5StatDeleteBearerRsp_Type()
)
tmnxMobGwS5StatDeleteBearerRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeleteBearerRsp.setStatus("current")
_TmnxMobGwS5StatModifyBearerReq_Type = Counter32
_TmnxMobGwS5StatModifyBearerReq_Object = MibTableColumn
tmnxMobGwS5StatModifyBearerReq = _TmnxMobGwS5StatModifyBearerReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 9),
    _TmnxMobGwS5StatModifyBearerReq_Type()
)
tmnxMobGwS5StatModifyBearerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatModifyBearerReq.setStatus("current")
_TmnxMobGwS5StatModifyBearerRsp_Type = Counter32
_TmnxMobGwS5StatModifyBearerRsp_Object = MibTableColumn
tmnxMobGwS5StatModifyBearerRsp = _TmnxMobGwS5StatModifyBearerRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 10),
    _TmnxMobGwS5StatModifyBearerRsp_Type()
)
tmnxMobGwS5StatModifyBearerRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatModifyBearerRsp.setStatus("current")
_TmnxMobGwS5StatRxEchoRequests_Type = Counter32
_TmnxMobGwS5StatRxEchoRequests_Object = MibTableColumn
tmnxMobGwS5StatRxEchoRequests = _TmnxMobGwS5StatRxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 11),
    _TmnxMobGwS5StatRxEchoRequests_Type()
)
tmnxMobGwS5StatRxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatRxEchoRequests.setStatus("current")
_TmnxMobGwS5StatTxEchoResponses_Type = Counter32
_TmnxMobGwS5StatTxEchoResponses_Object = MibTableColumn
tmnxMobGwS5StatTxEchoResponses = _TmnxMobGwS5StatTxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 12),
    _TmnxMobGwS5StatTxEchoResponses_Type()
)
tmnxMobGwS5StatTxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatTxEchoResponses.setStatus("current")
_TmnxMobGwS5StatTxEchoRequests_Type = Counter32
_TmnxMobGwS5StatTxEchoRequests_Object = MibTableColumn
tmnxMobGwS5StatTxEchoRequests = _TmnxMobGwS5StatTxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 13),
    _TmnxMobGwS5StatTxEchoRequests_Type()
)
tmnxMobGwS5StatTxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatTxEchoRequests.setStatus("current")
_TmnxMobGwS5StatRxEchoResponses_Type = Counter32
_TmnxMobGwS5StatRxEchoResponses_Object = MibTableColumn
tmnxMobGwS5StatRxEchoResponses = _TmnxMobGwS5StatRxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 14),
    _TmnxMobGwS5StatRxEchoResponses_Type()
)
tmnxMobGwS5StatRxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatRxEchoResponses.setStatus("current")
_TmnxMobGwS5StatRxMalformedPkts_Type = Counter32
_TmnxMobGwS5StatRxMalformedPkts_Object = MibTableColumn
tmnxMobGwS5StatRxMalformedPkts = _TmnxMobGwS5StatRxMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 15),
    _TmnxMobGwS5StatRxMalformedPkts_Type()
)
tmnxMobGwS5StatRxMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatRxMalformedPkts.setStatus("current")
_TmnxMobGwS5StatRxUnknownPkts_Type = Counter32
_TmnxMobGwS5StatRxUnknownPkts_Object = MibTableColumn
tmnxMobGwS5StatRxUnknownPkts = _TmnxMobGwS5StatRxUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 16),
    _TmnxMobGwS5StatRxUnknownPkts_Type()
)
tmnxMobGwS5StatRxUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatRxUnknownPkts.setStatus("current")
_TmnxMobGwS5StatRxMissingIePkts_Type = Counter32
_TmnxMobGwS5StatRxMissingIePkts_Object = MibTableColumn
tmnxMobGwS5StatRxMissingIePkts = _TmnxMobGwS5StatRxMissingIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 17),
    _TmnxMobGwS5StatRxMissingIePkts_Type()
)
tmnxMobGwS5StatRxMissingIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatRxMissingIePkts.setStatus("current")
_TmnxMobGwS5StatCreatePbu_Type = Counter32
_TmnxMobGwS5StatCreatePbu_Object = MibTableColumn
tmnxMobGwS5StatCreatePbu = _TmnxMobGwS5StatCreatePbu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 18),
    _TmnxMobGwS5StatCreatePbu_Type()
)
tmnxMobGwS5StatCreatePbu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatCreatePbu.setStatus("current")
_TmnxMobGwS5StatCreatePba_Type = Counter32
_TmnxMobGwS5StatCreatePba_Object = MibTableColumn
tmnxMobGwS5StatCreatePba = _TmnxMobGwS5StatCreatePba_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 19),
    _TmnxMobGwS5StatCreatePba_Type()
)
tmnxMobGwS5StatCreatePba.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatCreatePba.setStatus("current")
_TmnxMobGwS5StatDeletePbu_Type = Counter32
_TmnxMobGwS5StatDeletePbu_Object = MibTableColumn
tmnxMobGwS5StatDeletePbu = _TmnxMobGwS5StatDeletePbu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 20),
    _TmnxMobGwS5StatDeletePbu_Type()
)
tmnxMobGwS5StatDeletePbu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeletePbu.setStatus("current")
_TmnxMobGwS5StatDeletePba_Type = Counter32
_TmnxMobGwS5StatDeletePba_Object = MibTableColumn
tmnxMobGwS5StatDeletePba = _TmnxMobGwS5StatDeletePba_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 21),
    _TmnxMobGwS5StatDeletePba_Type()
)
tmnxMobGwS5StatDeletePba.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeletePba.setStatus("current")
_TmnxMobGwS5StatBri_Type = Counter32
_TmnxMobGwS5StatBri_Object = MibTableColumn
tmnxMobGwS5StatBri = _TmnxMobGwS5StatBri_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 22),
    _TmnxMobGwS5StatBri_Type()
)
tmnxMobGwS5StatBri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatBri.setStatus("current")
_TmnxMobGwS5StatBra_Type = Counter32
_TmnxMobGwS5StatBra_Object = MibTableColumn
tmnxMobGwS5StatBra = _TmnxMobGwS5StatBra_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 23),
    _TmnxMobGwS5StatBra_Type()
)
tmnxMobGwS5StatBra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatBra.setStatus("current")
_TmnxMobGwS5StatPeerRestarts_Type = Counter32
_TmnxMobGwS5StatPeerRestarts_Object = MibTableColumn
tmnxMobGwS5StatPeerRestarts = _TmnxMobGwS5StatPeerRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 24),
    _TmnxMobGwS5StatPeerRestarts_Type()
)
tmnxMobGwS5StatPeerRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatPeerRestarts.setStatus("current")
_TmnxMobGwS5StatPeerRestrtCount_Type = Counter32
_TmnxMobGwS5StatPeerRestrtCount_Object = MibTableColumn
tmnxMobGwS5StatPeerRestrtCount = _TmnxMobGwS5StatPeerRestrtCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 25),
    _TmnxMobGwS5StatPeerRestrtCount_Type()
)
tmnxMobGwS5StatPeerRestrtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatPeerRestrtCount.setStatus("current")
_TmnxMobGwS5StatPathMgmtFails_Type = Counter32
_TmnxMobGwS5StatPathMgmtFails_Object = MibTableColumn
tmnxMobGwS5StatPathMgmtFails = _TmnxMobGwS5StatPathMgmtFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 26),
    _TmnxMobGwS5StatPathMgmtFails_Type()
)
tmnxMobGwS5StatPathMgmtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatPathMgmtFails.setStatus("current")
_TmnxMobGwS5StatUpdateBearerReq_Type = Counter32
_TmnxMobGwS5StatUpdateBearerReq_Object = MibTableColumn
tmnxMobGwS5StatUpdateBearerReq = _TmnxMobGwS5StatUpdateBearerReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 27),
    _TmnxMobGwS5StatUpdateBearerReq_Type()
)
tmnxMobGwS5StatUpdateBearerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatUpdateBearerReq.setStatus("current")
_TmnxMobGwS5StatUpdateBearerRsp_Type = Counter32
_TmnxMobGwS5StatUpdateBearerRsp_Object = MibTableColumn
tmnxMobGwS5StatUpdateBearerRsp = _TmnxMobGwS5StatUpdateBearerRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 28),
    _TmnxMobGwS5StatUpdateBearerRsp_Type()
)
tmnxMobGwS5StatUpdateBearerRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatUpdateBearerRsp.setStatus("current")
_TmnxMobGwS5StatBearersIpv4_Type = Gauge32
_TmnxMobGwS5StatBearersIpv4_Object = MibTableColumn
tmnxMobGwS5StatBearersIpv4 = _TmnxMobGwS5StatBearersIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 29),
    _TmnxMobGwS5StatBearersIpv4_Type()
)
tmnxMobGwS5StatBearersIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatBearersIpv4.setStatus("obsolete")
_TmnxMobGwS5StatBearersIpv6_Type = Gauge32
_TmnxMobGwS5StatBearersIpv6_Object = MibTableColumn
tmnxMobGwS5StatBearersIpv6 = _TmnxMobGwS5StatBearersIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 30),
    _TmnxMobGwS5StatBearersIpv6_Type()
)
tmnxMobGwS5StatBearersIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatBearersIpv6.setStatus("obsolete")
_TmnxMobGwS5StatBearerIpv4v6_Type = Gauge32
_TmnxMobGwS5StatBearerIpv4v6_Object = MibTableColumn
tmnxMobGwS5StatBearerIpv4v6 = _TmnxMobGwS5StatBearerIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 31),
    _TmnxMobGwS5StatBearerIpv4v6_Type()
)
tmnxMobGwS5StatBearerIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatBearerIpv4v6.setStatus("obsolete")
_TmnxMobGwS5StatDedctdBearers_Type = Gauge32
_TmnxMobGwS5StatDedctdBearers_Object = MibTableColumn
tmnxMobGwS5StatDedctdBearers = _TmnxMobGwS5StatDedctdBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 32),
    _TmnxMobGwS5StatDedctdBearers_Type()
)
tmnxMobGwS5StatDedctdBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDedctdBearers.setStatus("obsolete")
_TmnxMobGwS5StatUlBytes_Type = Counter32
_TmnxMobGwS5StatUlBytes_Object = MibTableColumn
tmnxMobGwS5StatUlBytes = _TmnxMobGwS5StatUlBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 33),
    _TmnxMobGwS5StatUlBytes_Type()
)
tmnxMobGwS5StatUlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatUlBytes.setStatus("current")
_TmnxMobGwS5StatDlBytes_Type = Counter32
_TmnxMobGwS5StatDlBytes_Object = MibTableColumn
tmnxMobGwS5StatDlBytes = _TmnxMobGwS5StatDlBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 34),
    _TmnxMobGwS5StatDlBytes_Type()
)
tmnxMobGwS5StatDlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDlBytes.setStatus("current")
_TmnxMobGwS5StatUlPackets_Type = Counter32
_TmnxMobGwS5StatUlPackets_Object = MibTableColumn
tmnxMobGwS5StatUlPackets = _TmnxMobGwS5StatUlPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 35),
    _TmnxMobGwS5StatUlPackets_Type()
)
tmnxMobGwS5StatUlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatUlPackets.setStatus("current")
_TmnxMobGwS5StatDlPackets_Type = Counter32
_TmnxMobGwS5StatDlPackets_Object = MibTableColumn
tmnxMobGwS5StatDlPackets = _TmnxMobGwS5StatDlPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 36),
    _TmnxMobGwS5StatDlPackets_Type()
)
tmnxMobGwS5StatDlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDlPackets.setStatus("current")
_TmnxMobGwS5StatBearers_Type = Gauge32
_TmnxMobGwS5StatBearers_Object = MibTableColumn
tmnxMobGwS5StatBearers = _TmnxMobGwS5StatBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 37),
    _TmnxMobGwS5StatBearers_Type()
)
tmnxMobGwS5StatBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatBearers.setStatus("current")
_TmnxMobGwS5StatDefBearers_Type = Gauge32
_TmnxMobGwS5StatDefBearers_Object = MibTableColumn
tmnxMobGwS5StatDefBearers = _TmnxMobGwS5StatDefBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 38),
    _TmnxMobGwS5StatDefBearers_Type()
)
tmnxMobGwS5StatDefBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDefBearers.setStatus("obsolete")
_TmnxMobGwS5StatRoamers_Type = Gauge32
_TmnxMobGwS5StatRoamers_Object = MibTableColumn
tmnxMobGwS5StatRoamers = _TmnxMobGwS5StatRoamers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 39),
    _TmnxMobGwS5StatRoamers_Type()
)
tmnxMobGwS5StatRoamers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatRoamers.setStatus("obsolete")
_TmnxMobGwS5StatActiveBearers_Type = Gauge32
_TmnxMobGwS5StatActiveBearers_Object = MibTableColumn
tmnxMobGwS5StatActiveBearers = _TmnxMobGwS5StatActiveBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 40),
    _TmnxMobGwS5StatActiveBearers_Type()
)
tmnxMobGwS5StatActiveBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatActiveBearers.setStatus("obsolete")
_TmnxMobGwS5StatIdleBearers_Type = Gauge32
_TmnxMobGwS5StatIdleBearers_Object = MibTableColumn
tmnxMobGwS5StatIdleBearers = _TmnxMobGwS5StatIdleBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 41),
    _TmnxMobGwS5StatIdleBearers_Type()
)
tmnxMobGwS5StatIdleBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatIdleBearers.setStatus("obsolete")
_TmnxMobGwS5StatModifyBearrCmd_Type = Counter32
_TmnxMobGwS5StatModifyBearrCmd_Object = MibTableColumn
tmnxMobGwS5StatModifyBearrCmd = _TmnxMobGwS5StatModifyBearrCmd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 42),
    _TmnxMobGwS5StatModifyBearrCmd_Type()
)
tmnxMobGwS5StatModifyBearrCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatModifyBearrCmd.setStatus("current")
_TmnxMobGwS5StatModifyBearrFlr_Type = Counter32
_TmnxMobGwS5StatModifyBearrFlr_Object = MibTableColumn
tmnxMobGwS5StatModifyBearrFlr = _TmnxMobGwS5StatModifyBearrFlr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 43),
    _TmnxMobGwS5StatModifyBearrFlr_Type()
)
tmnxMobGwS5StatModifyBearrFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatModifyBearrFlr.setStatus("current")
_TmnxMobGwS5StatDeleteBearrCmd_Type = Counter32
_TmnxMobGwS5StatDeleteBearrCmd_Object = MibTableColumn
tmnxMobGwS5StatDeleteBearrCmd = _TmnxMobGwS5StatDeleteBearrCmd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 44),
    _TmnxMobGwS5StatDeleteBearrCmd_Type()
)
tmnxMobGwS5StatDeleteBearrCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeleteBearrCmd.setStatus("current")
_TmnxMobGwS5StatDeleteBearrFlr_Type = Counter32
_TmnxMobGwS5StatDeleteBearrFlr_Object = MibTableColumn
tmnxMobGwS5StatDeleteBearrFlr = _TmnxMobGwS5StatDeleteBearrFlr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 45),
    _TmnxMobGwS5StatDeleteBearrFlr_Type()
)
tmnxMobGwS5StatDeleteBearrFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeleteBearrFlr.setStatus("current")
_TmnxMobGwS5StatBearrResCmd_Type = Counter32
_TmnxMobGwS5StatBearrResCmd_Object = MibTableColumn
tmnxMobGwS5StatBearrResCmd = _TmnxMobGwS5StatBearrResCmd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 46),
    _TmnxMobGwS5StatBearrResCmd_Type()
)
tmnxMobGwS5StatBearrResCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatBearrResCmd.setStatus("current")
_TmnxMobGwS5StatBearrResFailInd_Type = Counter32
_TmnxMobGwS5StatBearrResFailInd_Object = MibTableColumn
tmnxMobGwS5StatBearrResFailInd = _TmnxMobGwS5StatBearrResFailInd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 47),
    _TmnxMobGwS5StatBearrResFailInd_Type()
)
tmnxMobGwS5StatBearrResFailInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatBearrResFailInd.setStatus("current")
_TmnxMobGwS5StatSuspNoticeReq_Type = Counter32
_TmnxMobGwS5StatSuspNoticeReq_Object = MibTableColumn
tmnxMobGwS5StatSuspNoticeReq = _TmnxMobGwS5StatSuspNoticeReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 48),
    _TmnxMobGwS5StatSuspNoticeReq_Type()
)
tmnxMobGwS5StatSuspNoticeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatSuspNoticeReq.setStatus("current")
_TmnxMobGwS5StatSuspNoticeAck_Type = Counter32
_TmnxMobGwS5StatSuspNoticeAck_Object = MibTableColumn
tmnxMobGwS5StatSuspNoticeAck = _TmnxMobGwS5StatSuspNoticeAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 49),
    _TmnxMobGwS5StatSuspNoticeAck_Type()
)
tmnxMobGwS5StatSuspNoticeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatSuspNoticeAck.setStatus("current")
_TmnxMobGwS5StatResumeNoticeReq_Type = Counter32
_TmnxMobGwS5StatResumeNoticeReq_Object = MibTableColumn
tmnxMobGwS5StatResumeNoticeReq = _TmnxMobGwS5StatResumeNoticeReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 50),
    _TmnxMobGwS5StatResumeNoticeReq_Type()
)
tmnxMobGwS5StatResumeNoticeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatResumeNoticeReq.setStatus("current")
_TmnxMobGwS5StatResumeNoticeAck_Type = Counter32
_TmnxMobGwS5StatResumeNoticeAck_Object = MibTableColumn
tmnxMobGwS5StatResumeNoticeAck = _TmnxMobGwS5StatResumeNoticeAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 51),
    _TmnxMobGwS5StatResumeNoticeAck_Type()
)
tmnxMobGwS5StatResumeNoticeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatResumeNoticeAck.setStatus("current")
_TmnxMobGwS5StatCreateSessnRespFl_Type = Counter32
_TmnxMobGwS5StatCreateSessnRespFl_Object = MibTableColumn
tmnxMobGwS5StatCreateSessnRespFl = _TmnxMobGwS5StatCreateSessnRespFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 52),
    _TmnxMobGwS5StatCreateSessnRespFl_Type()
)
tmnxMobGwS5StatCreateSessnRespFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatCreateSessnRespFl.setStatus("current")
_TmnxMobGwS5StatDeleteSessnRespFl_Type = Counter32
_TmnxMobGwS5StatDeleteSessnRespFl_Object = MibTableColumn
tmnxMobGwS5StatDeleteSessnRespFl = _TmnxMobGwS5StatDeleteSessnRespFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 53),
    _TmnxMobGwS5StatDeleteSessnRespFl_Type()
)
tmnxMobGwS5StatDeleteSessnRespFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeleteSessnRespFl.setStatus("current")
_TmnxMobGwS5StatCreateBearerRspFl_Type = Counter32
_TmnxMobGwS5StatCreateBearerRspFl_Object = MibTableColumn
tmnxMobGwS5StatCreateBearerRspFl = _TmnxMobGwS5StatCreateBearerRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 54),
    _TmnxMobGwS5StatCreateBearerRspFl_Type()
)
tmnxMobGwS5StatCreateBearerRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatCreateBearerRspFl.setStatus("current")
_TmnxMobGwS5StatDeleteBearerRspFl_Type = Counter32
_TmnxMobGwS5StatDeleteBearerRspFl_Object = MibTableColumn
tmnxMobGwS5StatDeleteBearerRspFl = _TmnxMobGwS5StatDeleteBearerRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 55),
    _TmnxMobGwS5StatDeleteBearerRspFl_Type()
)
tmnxMobGwS5StatDeleteBearerRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatDeleteBearerRspFl.setStatus("current")
_TmnxMobGwS5StatModifyBearerRspFl_Type = Counter32
_TmnxMobGwS5StatModifyBearerRspFl_Object = MibTableColumn
tmnxMobGwS5StatModifyBearerRspFl = _TmnxMobGwS5StatModifyBearerRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 56),
    _TmnxMobGwS5StatModifyBearerRspFl_Type()
)
tmnxMobGwS5StatModifyBearerRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatModifyBearerRspFl.setStatus("current")
_TmnxMobGwS5StatUpdateBearerRspFl_Type = Counter32
_TmnxMobGwS5StatUpdateBearerRspFl_Object = MibTableColumn
tmnxMobGwS5StatUpdateBearerRspFl = _TmnxMobGwS5StatUpdateBearerRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 5, 1, 57),
    _TmnxMobGwS5StatUpdateBearerRspFl_Type()
)
tmnxMobGwS5StatUpdateBearerRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5StatUpdateBearerRspFl.setStatus("current")
_TmnxMobGwS8PeerTable_Object = MibTable
tmnxMobGwS8PeerTable = _TmnxMobGwS8PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerTable.setStatus("current")
_TmnxMobGwS8PeerEntry_Object = MibTableRow
tmnxMobGwS8PeerEntry = _TmnxMobGwS8PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1)
)
tmnxMobGwS8PeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerAddressType"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerAddress"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerEntry.setStatus("current")
_TmnxMobGwS8PeerAddressType_Type = InetAddressType
_TmnxMobGwS8PeerAddressType_Object = MibTableColumn
tmnxMobGwS8PeerAddressType = _TmnxMobGwS8PeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1, 1),
    _TmnxMobGwS8PeerAddressType_Type()
)
tmnxMobGwS8PeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerAddressType.setStatus("current")


class _TmnxMobGwS8PeerAddress_Type(InetAddress):
    """Custom type tmnxMobGwS8PeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobGwS8PeerAddress_Type.__name__ = "InetAddress"
_TmnxMobGwS8PeerAddress_Object = MibTableColumn
tmnxMobGwS8PeerAddress = _TmnxMobGwS8PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1, 2),
    _TmnxMobGwS8PeerAddress_Type()
)
tmnxMobGwS8PeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerAddress.setStatus("current")
_TmnxMobGwS8PeerPort_Type = InetPortNumber
_TmnxMobGwS8PeerPort_Object = MibTableColumn
tmnxMobGwS8PeerPort = _TmnxMobGwS8PeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1, 3),
    _TmnxMobGwS8PeerPort_Type()
)
tmnxMobGwS8PeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerPort.setStatus("current")
_TmnxMobGwS8PeerLastChanged_Type = TimeStamp
_TmnxMobGwS8PeerLastChanged_Object = MibTableColumn
tmnxMobGwS8PeerLastChanged = _TmnxMobGwS8PeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1, 4),
    _TmnxMobGwS8PeerLastChanged_Type()
)
tmnxMobGwS8PeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerLastChanged.setStatus("current")
_TmnxMobGwS8PeerCreateTime_Type = TimeStamp
_TmnxMobGwS8PeerCreateTime_Object = MibTableColumn
tmnxMobGwS8PeerCreateTime = _TmnxMobGwS8PeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1, 5),
    _TmnxMobGwS8PeerCreateTime_Type()
)
tmnxMobGwS8PeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerCreateTime.setStatus("current")
_TmnxMobGwS8PeerPathMgmtState_Type = TmnxMobPathMgmtState
_TmnxMobGwS8PeerPathMgmtState_Object = MibTableColumn
tmnxMobGwS8PeerPathMgmtState = _TmnxMobGwS8PeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1, 6),
    _TmnxMobGwS8PeerPathMgmtState_Type()
)
tmnxMobGwS8PeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerPathMgmtState.setStatus("current")
_TmnxMobGwS8PeerGatewayId_Type = TmnxMobGwId
_TmnxMobGwS8PeerGatewayId_Object = MibTableColumn
tmnxMobGwS8PeerGatewayId = _TmnxMobGwS8PeerGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1, 7),
    _TmnxMobGwS8PeerGatewayId_Type()
)
tmnxMobGwS8PeerGatewayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerGatewayId.setStatus("current")
_TmnxMobGwS8PeerType_Type = TmnxMobPeerType
_TmnxMobGwS8PeerType_Object = MibTableColumn
tmnxMobGwS8PeerType = _TmnxMobGwS8PeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 6, 1, 8),
    _TmnxMobGwS8PeerType_Type()
)
tmnxMobGwS8PeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerType.setStatus("current")
_TmnxMobGwS8StatTable_Object = MibTable
tmnxMobGwS8StatTable = _TmnxMobGwS8StatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxMobGwS8StatTable.setStatus("current")
_TmnxMobGwS8StatEntry_Object = MibTableRow
tmnxMobGwS8StatEntry = _TmnxMobGwS8StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1)
)
tmnxMobGwS8StatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerAddressType"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerAddress"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobGwS8StatEntry.setStatus("current")
_TmnxMobGwS8StatCreateSessnReq_Type = Counter32
_TmnxMobGwS8StatCreateSessnReq_Object = MibTableColumn
tmnxMobGwS8StatCreateSessnReq = _TmnxMobGwS8StatCreateSessnReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 1),
    _TmnxMobGwS8StatCreateSessnReq_Type()
)
tmnxMobGwS8StatCreateSessnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatCreateSessnReq.setStatus("current")
_TmnxMobGwS8StatCreateSessnResp_Type = Counter32
_TmnxMobGwS8StatCreateSessnResp_Object = MibTableColumn
tmnxMobGwS8StatCreateSessnResp = _TmnxMobGwS8StatCreateSessnResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 2),
    _TmnxMobGwS8StatCreateSessnResp_Type()
)
tmnxMobGwS8StatCreateSessnResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatCreateSessnResp.setStatus("current")
_TmnxMobGwS8StatDeleteSessnReq_Type = Counter32
_TmnxMobGwS8StatDeleteSessnReq_Object = MibTableColumn
tmnxMobGwS8StatDeleteSessnReq = _TmnxMobGwS8StatDeleteSessnReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 3),
    _TmnxMobGwS8StatDeleteSessnReq_Type()
)
tmnxMobGwS8StatDeleteSessnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatDeleteSessnReq.setStatus("current")
_TmnxMobGwS8StatDeleteSessnResp_Type = Counter32
_TmnxMobGwS8StatDeleteSessnResp_Object = MibTableColumn
tmnxMobGwS8StatDeleteSessnResp = _TmnxMobGwS8StatDeleteSessnResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 4),
    _TmnxMobGwS8StatDeleteSessnResp_Type()
)
tmnxMobGwS8StatDeleteSessnResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatDeleteSessnResp.setStatus("current")
_TmnxMobGwS8StatCreateBearerReq_Type = Counter32
_TmnxMobGwS8StatCreateBearerReq_Object = MibTableColumn
tmnxMobGwS8StatCreateBearerReq = _TmnxMobGwS8StatCreateBearerReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 5),
    _TmnxMobGwS8StatCreateBearerReq_Type()
)
tmnxMobGwS8StatCreateBearerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatCreateBearerReq.setStatus("current")
_TmnxMobGwS8StatCreateBearerRsp_Type = Counter32
_TmnxMobGwS8StatCreateBearerRsp_Object = MibTableColumn
tmnxMobGwS8StatCreateBearerRsp = _TmnxMobGwS8StatCreateBearerRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 6),
    _TmnxMobGwS8StatCreateBearerRsp_Type()
)
tmnxMobGwS8StatCreateBearerRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatCreateBearerRsp.setStatus("current")
_TmnxMobGwS8StatDeleteBearerReq_Type = Counter32
_TmnxMobGwS8StatDeleteBearerReq_Object = MibTableColumn
tmnxMobGwS8StatDeleteBearerReq = _TmnxMobGwS8StatDeleteBearerReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 7),
    _TmnxMobGwS8StatDeleteBearerReq_Type()
)
tmnxMobGwS8StatDeleteBearerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatDeleteBearerReq.setStatus("current")
_TmnxMobGwS8StatDeleteBearerRsp_Type = Counter32
_TmnxMobGwS8StatDeleteBearerRsp_Object = MibTableColumn
tmnxMobGwS8StatDeleteBearerRsp = _TmnxMobGwS8StatDeleteBearerRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 8),
    _TmnxMobGwS8StatDeleteBearerRsp_Type()
)
tmnxMobGwS8StatDeleteBearerRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatDeleteBearerRsp.setStatus("current")
_TmnxMobGwS8StatModifyBearerReq_Type = Counter32
_TmnxMobGwS8StatModifyBearerReq_Object = MibTableColumn
tmnxMobGwS8StatModifyBearerReq = _TmnxMobGwS8StatModifyBearerReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 9),
    _TmnxMobGwS8StatModifyBearerReq_Type()
)
tmnxMobGwS8StatModifyBearerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatModifyBearerReq.setStatus("current")
_TmnxMobGwS8StatModifyBearerRsp_Type = Counter32
_TmnxMobGwS8StatModifyBearerRsp_Object = MibTableColumn
tmnxMobGwS8StatModifyBearerRsp = _TmnxMobGwS8StatModifyBearerRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 10),
    _TmnxMobGwS8StatModifyBearerRsp_Type()
)
tmnxMobGwS8StatModifyBearerRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatModifyBearerRsp.setStatus("current")
_TmnxMobGwS8StatRxEchoRequests_Type = Counter32
_TmnxMobGwS8StatRxEchoRequests_Object = MibTableColumn
tmnxMobGwS8StatRxEchoRequests = _TmnxMobGwS8StatRxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 11),
    _TmnxMobGwS8StatRxEchoRequests_Type()
)
tmnxMobGwS8StatRxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatRxEchoRequests.setStatus("current")
_TmnxMobGwS8StatTxEchoResponses_Type = Counter32
_TmnxMobGwS8StatTxEchoResponses_Object = MibTableColumn
tmnxMobGwS8StatTxEchoResponses = _TmnxMobGwS8StatTxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 12),
    _TmnxMobGwS8StatTxEchoResponses_Type()
)
tmnxMobGwS8StatTxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatTxEchoResponses.setStatus("current")
_TmnxMobGwS8StatTxEchoRequests_Type = Counter32
_TmnxMobGwS8StatTxEchoRequests_Object = MibTableColumn
tmnxMobGwS8StatTxEchoRequests = _TmnxMobGwS8StatTxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 13),
    _TmnxMobGwS8StatTxEchoRequests_Type()
)
tmnxMobGwS8StatTxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatTxEchoRequests.setStatus("current")
_TmnxMobGwS8StatRxEchoResponses_Type = Counter32
_TmnxMobGwS8StatRxEchoResponses_Object = MibTableColumn
tmnxMobGwS8StatRxEchoResponses = _TmnxMobGwS8StatRxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 14),
    _TmnxMobGwS8StatRxEchoResponses_Type()
)
tmnxMobGwS8StatRxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatRxEchoResponses.setStatus("current")
_TmnxMobGwS8StatRxMalformedPkts_Type = Counter32
_TmnxMobGwS8StatRxMalformedPkts_Object = MibTableColumn
tmnxMobGwS8StatRxMalformedPkts = _TmnxMobGwS8StatRxMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 15),
    _TmnxMobGwS8StatRxMalformedPkts_Type()
)
tmnxMobGwS8StatRxMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatRxMalformedPkts.setStatus("current")
_TmnxMobGwS8StatRxUnknownPkts_Type = Counter32
_TmnxMobGwS8StatRxUnknownPkts_Object = MibTableColumn
tmnxMobGwS8StatRxUnknownPkts = _TmnxMobGwS8StatRxUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 16),
    _TmnxMobGwS8StatRxUnknownPkts_Type()
)
tmnxMobGwS8StatRxUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatRxUnknownPkts.setStatus("current")
_TmnxMobGwS8StatRxMissingIePkts_Type = Counter32
_TmnxMobGwS8StatRxMissingIePkts_Object = MibTableColumn
tmnxMobGwS8StatRxMissingIePkts = _TmnxMobGwS8StatRxMissingIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 17),
    _TmnxMobGwS8StatRxMissingIePkts_Type()
)
tmnxMobGwS8StatRxMissingIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatRxMissingIePkts.setStatus("current")
_TmnxMobGwS8StatCreatePbu_Type = Counter32
_TmnxMobGwS8StatCreatePbu_Object = MibTableColumn
tmnxMobGwS8StatCreatePbu = _TmnxMobGwS8StatCreatePbu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 18),
    _TmnxMobGwS8StatCreatePbu_Type()
)
tmnxMobGwS8StatCreatePbu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatCreatePbu.setStatus("current")
_TmnxMobGwS8StatCreatePba_Type = Counter32
_TmnxMobGwS8StatCreatePba_Object = MibTableColumn
tmnxMobGwS8StatCreatePba = _TmnxMobGwS8StatCreatePba_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 19),
    _TmnxMobGwS8StatCreatePba_Type()
)
tmnxMobGwS8StatCreatePba.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatCreatePba.setStatus("current")
_TmnxMobGwS8StatDeletePbu_Type = Counter32
_TmnxMobGwS8StatDeletePbu_Object = MibTableColumn
tmnxMobGwS8StatDeletePbu = _TmnxMobGwS8StatDeletePbu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 20),
    _TmnxMobGwS8StatDeletePbu_Type()
)
tmnxMobGwS8StatDeletePbu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatDeletePbu.setStatus("current")
_TmnxMobGwS8StatDeletePba_Type = Counter32
_TmnxMobGwS8StatDeletePba_Object = MibTableColumn
tmnxMobGwS8StatDeletePba = _TmnxMobGwS8StatDeletePba_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 21),
    _TmnxMobGwS8StatDeletePba_Type()
)
tmnxMobGwS8StatDeletePba.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatDeletePba.setStatus("current")
_TmnxMobGwS8StatBri_Type = Counter32
_TmnxMobGwS8StatBri_Object = MibTableColumn
tmnxMobGwS8StatBri = _TmnxMobGwS8StatBri_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 22),
    _TmnxMobGwS8StatBri_Type()
)
tmnxMobGwS8StatBri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatBri.setStatus("current")
_TmnxMobGwS8StatBra_Type = Counter32
_TmnxMobGwS8StatBra_Object = MibTableColumn
tmnxMobGwS8StatBra = _TmnxMobGwS8StatBra_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 23),
    _TmnxMobGwS8StatBra_Type()
)
tmnxMobGwS8StatBra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatBra.setStatus("current")
_TmnxMobGwS8StatPeerRestarts_Type = Counter32
_TmnxMobGwS8StatPeerRestarts_Object = MibTableColumn
tmnxMobGwS8StatPeerRestarts = _TmnxMobGwS8StatPeerRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 24),
    _TmnxMobGwS8StatPeerRestarts_Type()
)
tmnxMobGwS8StatPeerRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatPeerRestarts.setStatus("current")
_TmnxMobGwS8StatPeerRestrtCount_Type = Counter32
_TmnxMobGwS8StatPeerRestrtCount_Object = MibTableColumn
tmnxMobGwS8StatPeerRestrtCount = _TmnxMobGwS8StatPeerRestrtCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 25),
    _TmnxMobGwS8StatPeerRestrtCount_Type()
)
tmnxMobGwS8StatPeerRestrtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatPeerRestrtCount.setStatus("current")
_TmnxMobGwS8StatPathMgmtFails_Type = Counter32
_TmnxMobGwS8StatPathMgmtFails_Object = MibTableColumn
tmnxMobGwS8StatPathMgmtFails = _TmnxMobGwS8StatPathMgmtFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 26),
    _TmnxMobGwS8StatPathMgmtFails_Type()
)
tmnxMobGwS8StatPathMgmtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatPathMgmtFails.setStatus("current")
_TmnxMobGwS8StatUpdateBearerReq_Type = Counter32
_TmnxMobGwS8StatUpdateBearerReq_Object = MibTableColumn
tmnxMobGwS8StatUpdateBearerReq = _TmnxMobGwS8StatUpdateBearerReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 27),
    _TmnxMobGwS8StatUpdateBearerReq_Type()
)
tmnxMobGwS8StatUpdateBearerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatUpdateBearerReq.setStatus("current")
_TmnxMobGwS8StatUpdateBearerRsp_Type = Counter32
_TmnxMobGwS8StatUpdateBearerRsp_Object = MibTableColumn
tmnxMobGwS8StatUpdateBearerRsp = _TmnxMobGwS8StatUpdateBearerRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 28),
    _TmnxMobGwS8StatUpdateBearerRsp_Type()
)
tmnxMobGwS8StatUpdateBearerRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatUpdateBearerRsp.setStatus("current")
_TmnxMobGwS8StatCreatSessnRspFl_Type = Counter32
_TmnxMobGwS8StatCreatSessnRspFl_Object = MibTableColumn
tmnxMobGwS8StatCreatSessnRspFl = _TmnxMobGwS8StatCreatSessnRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 29),
    _TmnxMobGwS8StatCreatSessnRspFl_Type()
)
tmnxMobGwS8StatCreatSessnRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatCreatSessnRspFl.setStatus("current")
_TmnxMobGwS8StatDelSessnRspFail_Type = Counter32
_TmnxMobGwS8StatDelSessnRspFail_Object = MibTableColumn
tmnxMobGwS8StatDelSessnRspFail = _TmnxMobGwS8StatDelSessnRspFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 30),
    _TmnxMobGwS8StatDelSessnRspFail_Type()
)
tmnxMobGwS8StatDelSessnRspFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatDelSessnRspFail.setStatus("current")
_TmnxMobGwS8StatCreatBearrRspFl_Type = Counter32
_TmnxMobGwS8StatCreatBearrRspFl_Object = MibTableColumn
tmnxMobGwS8StatCreatBearrRspFl = _TmnxMobGwS8StatCreatBearrRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 31),
    _TmnxMobGwS8StatCreatBearrRspFl_Type()
)
tmnxMobGwS8StatCreatBearrRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatCreatBearrRspFl.setStatus("current")
_TmnxMobGwS8StatDelBearrRspFail_Type = Counter32
_TmnxMobGwS8StatDelBearrRspFail_Object = MibTableColumn
tmnxMobGwS8StatDelBearrRspFail = _TmnxMobGwS8StatDelBearrRspFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 32),
    _TmnxMobGwS8StatDelBearrRspFail_Type()
)
tmnxMobGwS8StatDelBearrRspFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatDelBearrRspFail.setStatus("current")
_TmnxMobGwS8StatModBearrRspFail_Type = Counter32
_TmnxMobGwS8StatModBearrRspFail_Object = MibTableColumn
tmnxMobGwS8StatModBearrRspFail = _TmnxMobGwS8StatModBearrRspFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 33),
    _TmnxMobGwS8StatModBearrRspFail_Type()
)
tmnxMobGwS8StatModBearrRspFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatModBearrRspFail.setStatus("current")
_TmnxMobGwS8StatUpdatBearrRspFl_Type = Counter32
_TmnxMobGwS8StatUpdatBearrRspFl_Object = MibTableColumn
tmnxMobGwS8StatUpdatBearrRspFl = _TmnxMobGwS8StatUpdatBearrRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 7, 1, 34),
    _TmnxMobGwS8StatUpdatBearrRspFl_Type()
)
tmnxMobGwS8StatUpdatBearrRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8StatUpdatBearrRspFl.setStatus("current")
_TmnxMobGwRfPeerTable_Object = MibTable
tmnxMobGwRfPeerTable = _TmnxMobGwRfPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerTable.setStatus("current")
_TmnxMobGwRfPeerEntry_Object = MibTableRow
tmnxMobGwRfPeerEntry = _TmnxMobGwRfPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8, 1)
)
tmnxMobGwRfPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerAddressType"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerAddress"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerEntry.setStatus("current")
_TmnxMobGwRfPeerAddressType_Type = InetAddressType
_TmnxMobGwRfPeerAddressType_Object = MibTableColumn
tmnxMobGwRfPeerAddressType = _TmnxMobGwRfPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8, 1, 1),
    _TmnxMobGwRfPeerAddressType_Type()
)
tmnxMobGwRfPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerAddressType.setStatus("current")


class _TmnxMobGwRfPeerAddress_Type(InetAddress):
    """Custom type tmnxMobGwRfPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobGwRfPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobGwRfPeerAddress_Object = MibTableColumn
tmnxMobGwRfPeerAddress = _TmnxMobGwRfPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8, 1, 2),
    _TmnxMobGwRfPeerAddress_Type()
)
tmnxMobGwRfPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerAddress.setStatus("current")
_TmnxMobGwRfPeerPort_Type = InetPortNumber
_TmnxMobGwRfPeerPort_Object = MibTableColumn
tmnxMobGwRfPeerPort = _TmnxMobGwRfPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8, 1, 3),
    _TmnxMobGwRfPeerPort_Type()
)
tmnxMobGwRfPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerPort.setStatus("current")
_TmnxMobGwRfPeerLastChanged_Type = TimeStamp
_TmnxMobGwRfPeerLastChanged_Object = MibTableColumn
tmnxMobGwRfPeerLastChanged = _TmnxMobGwRfPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8, 1, 4),
    _TmnxMobGwRfPeerLastChanged_Type()
)
tmnxMobGwRfPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerLastChanged.setStatus("current")
_TmnxMobGwRfPeerCreateTime_Type = TimeStamp
_TmnxMobGwRfPeerCreateTime_Object = MibTableColumn
tmnxMobGwRfPeerCreateTime = _TmnxMobGwRfPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8, 1, 5),
    _TmnxMobGwRfPeerCreateTime_Type()
)
tmnxMobGwRfPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerCreateTime.setStatus("current")
_TmnxMobGwRfPeerPathMgmtState_Type = TmnxMobDiaPathMgmtState
_TmnxMobGwRfPeerPathMgmtState_Object = MibTableColumn
tmnxMobGwRfPeerPathMgmtState = _TmnxMobGwRfPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8, 1, 6),
    _TmnxMobGwRfPeerPathMgmtState_Type()
)
tmnxMobGwRfPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerPathMgmtState.setStatus("current")
_TmnxMobGwRfPeerDetailState_Type = TmnxMobDiaDetailPathMgmtState
_TmnxMobGwRfPeerDetailState_Object = MibTableColumn
tmnxMobGwRfPeerDetailState = _TmnxMobGwRfPeerDetailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 8, 1, 7),
    _TmnxMobGwRfPeerDetailState_Type()
)
tmnxMobGwRfPeerDetailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerDetailState.setStatus("current")
_TmnxMobGwRfStatTable_Object = MibTable
tmnxMobGwRfStatTable = _TmnxMobGwRfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTable.setStatus("current")
_TmnxMobGwRfStatEntry_Object = MibTableRow
tmnxMobGwRfStatEntry = _TmnxMobGwRfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1)
)
tmnxMobGwRfStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerAddressType"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerAddress"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobGwRfStatEntry.setStatus("current")
_TmnxMobGwRfStatTxCer_Type = Counter32
_TmnxMobGwRfStatTxCer_Object = MibTableColumn
tmnxMobGwRfStatTxCer = _TmnxMobGwRfStatTxCer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 1),
    _TmnxMobGwRfStatTxCer_Type()
)
tmnxMobGwRfStatTxCer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxCer.setStatus("current")
_TmnxMobGwRfStatRxCea_Type = Counter32
_TmnxMobGwRfStatRxCea_Object = MibTableColumn
tmnxMobGwRfStatRxCea = _TmnxMobGwRfStatRxCea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 2),
    _TmnxMobGwRfStatRxCea_Type()
)
tmnxMobGwRfStatRxCea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxCea.setStatus("current")
_TmnxMobGwRfStatRxDpr_Type = Counter32
_TmnxMobGwRfStatRxDpr_Object = MibTableColumn
tmnxMobGwRfStatRxDpr = _TmnxMobGwRfStatRxDpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 3),
    _TmnxMobGwRfStatRxDpr_Type()
)
tmnxMobGwRfStatRxDpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxDpr.setStatus("current")
_TmnxMobGwRfStatTxDpa_Type = Counter32
_TmnxMobGwRfStatTxDpa_Object = MibTableColumn
tmnxMobGwRfStatTxDpa = _TmnxMobGwRfStatTxDpa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 4),
    _TmnxMobGwRfStatTxDpa_Type()
)
tmnxMobGwRfStatTxDpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxDpa.setStatus("current")
_TmnxMobGwRfStatTxDwr_Type = Counter32
_TmnxMobGwRfStatTxDwr_Object = MibTableColumn
tmnxMobGwRfStatTxDwr = _TmnxMobGwRfStatTxDwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 5),
    _TmnxMobGwRfStatTxDwr_Type()
)
tmnxMobGwRfStatTxDwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxDwr.setStatus("current")
_TmnxMobGwRfStatRxDwa_Type = Counter32
_TmnxMobGwRfStatRxDwa_Object = MibTableColumn
tmnxMobGwRfStatRxDwa = _TmnxMobGwRfStatRxDwa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 6),
    _TmnxMobGwRfStatRxDwa_Type()
)
tmnxMobGwRfStatRxDwa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxDwa.setStatus("current")
_TmnxMobGwRfStatConnAttempts_Type = Counter32
_TmnxMobGwRfStatConnAttempts_Object = MibTableColumn
tmnxMobGwRfStatConnAttempts = _TmnxMobGwRfStatConnAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 7),
    _TmnxMobGwRfStatConnAttempts_Type()
)
tmnxMobGwRfStatConnAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatConnAttempts.setStatus("current")
_TmnxMobGwRfStatConnFailures_Type = Counter32
_TmnxMobGwRfStatConnFailures_Object = MibTableColumn
tmnxMobGwRfStatConnFailures = _TmnxMobGwRfStatConnFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 8),
    _TmnxMobGwRfStatConnFailures_Type()
)
tmnxMobGwRfStatConnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatConnFailures.setStatus("current")
_TmnxMobGwRfStatRxTransportDisc_Type = Counter32
_TmnxMobGwRfStatRxTransportDisc_Object = MibTableColumn
tmnxMobGwRfStatRxTransportDisc = _TmnxMobGwRfStatRxTransportDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 9),
    _TmnxMobGwRfStatRxTransportDisc_Type()
)
tmnxMobGwRfStatRxTransportDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxTransportDisc.setStatus("current")
_TmnxMobGwRfStatRxMsgUnexpectVer_Type = Counter32
_TmnxMobGwRfStatRxMsgUnexpectVer_Object = MibTableColumn
tmnxMobGwRfStatRxMsgUnexpectVer = _TmnxMobGwRfStatRxMsgUnexpectVer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 10),
    _TmnxMobGwRfStatRxMsgUnexpectVer_Type()
)
tmnxMobGwRfStatRxMsgUnexpectVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxMsgUnexpectVer.setStatus("current")
_TmnxMobGwRfStatRxMsgTooBig_Type = Counter32
_TmnxMobGwRfStatRxMsgTooBig_Object = MibTableColumn
tmnxMobGwRfStatRxMsgTooBig = _TmnxMobGwRfStatRxMsgTooBig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 11),
    _TmnxMobGwRfStatRxMsgTooBig_Type()
)
tmnxMobGwRfStatRxMsgTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxMsgTooBig.setStatus("current")
_TmnxMobGwRfStatRxMsgTooSmall_Type = Counter32
_TmnxMobGwRfStatRxMsgTooSmall_Object = MibTableColumn
tmnxMobGwRfStatRxMsgTooSmall = _TmnxMobGwRfStatRxMsgTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 12),
    _TmnxMobGwRfStatRxMsgTooSmall_Type()
)
tmnxMobGwRfStatRxMsgTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxMsgTooSmall.setStatus("current")
_TmnxMobGwRfStatRxInvalidCea_Type = Counter32
_TmnxMobGwRfStatRxInvalidCea_Object = MibTableColumn
tmnxMobGwRfStatRxInvalidCea = _TmnxMobGwRfStatRxInvalidCea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 13),
    _TmnxMobGwRfStatRxInvalidCea_Type()
)
tmnxMobGwRfStatRxInvalidCea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxInvalidCea.setStatus("current")
_TmnxMobGwRfStatRxMsgs_Type = Counter32
_TmnxMobGwRfStatRxMsgs_Object = MibTableColumn
tmnxMobGwRfStatRxMsgs = _TmnxMobGwRfStatRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 14),
    _TmnxMobGwRfStatRxMsgs_Type()
)
tmnxMobGwRfStatRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxMsgs.setStatus("current")
_TmnxMobGwRfStatTxMsgs_Type = Counter32
_TmnxMobGwRfStatTxMsgs_Object = MibTableColumn
tmnxMobGwRfStatTxMsgs = _TmnxMobGwRfStatTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 15),
    _TmnxMobGwRfStatTxMsgs_Type()
)
tmnxMobGwRfStatTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxMsgs.setStatus("current")
_TmnxMobGwRfStatTxRetransmitMsgs_Type = Counter32
_TmnxMobGwRfStatTxRetransmitMsgs_Object = MibTableColumn
tmnxMobGwRfStatTxRetransmitMsgs = _TmnxMobGwRfStatTxRetransmitMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 16),
    _TmnxMobGwRfStatTxRetransmitMsgs_Type()
)
tmnxMobGwRfStatTxRetransmitMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxRetransmitMsgs.setStatus("current")
_TmnxMobGwRfStatTxAcrStart_Type = Counter32
_TmnxMobGwRfStatTxAcrStart_Object = MibTableColumn
tmnxMobGwRfStatTxAcrStart = _TmnxMobGwRfStatTxAcrStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 17),
    _TmnxMobGwRfStatTxAcrStart_Type()
)
tmnxMobGwRfStatTxAcrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxAcrStart.setStatus("current")
_TmnxMobGwRfStatTxAcrInterim_Type = Counter32
_TmnxMobGwRfStatTxAcrInterim_Object = MibTableColumn
tmnxMobGwRfStatTxAcrInterim = _TmnxMobGwRfStatTxAcrInterim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 18),
    _TmnxMobGwRfStatTxAcrInterim_Type()
)
tmnxMobGwRfStatTxAcrInterim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxAcrInterim.setStatus("current")
_TmnxMobGwRfStatTxAcrStop_Type = Counter32
_TmnxMobGwRfStatTxAcrStop_Object = MibTableColumn
tmnxMobGwRfStatTxAcrStop = _TmnxMobGwRfStatTxAcrStop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 19),
    _TmnxMobGwRfStatTxAcrStop_Type()
)
tmnxMobGwRfStatTxAcrStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxAcrStop.setStatus("current")
_TmnxMobGwRfStatTxAcrStartFails_Type = Counter32
_TmnxMobGwRfStatTxAcrStartFails_Object = MibTableColumn
tmnxMobGwRfStatTxAcrStartFails = _TmnxMobGwRfStatTxAcrStartFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 20),
    _TmnxMobGwRfStatTxAcrStartFails_Type()
)
tmnxMobGwRfStatTxAcrStartFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxAcrStartFails.setStatus("current")
_TmnxMobGwRfStatTxAcrInterimFail_Type = Counter32
_TmnxMobGwRfStatTxAcrInterimFail_Object = MibTableColumn
tmnxMobGwRfStatTxAcrInterimFail = _TmnxMobGwRfStatTxAcrInterimFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 21),
    _TmnxMobGwRfStatTxAcrInterimFail_Type()
)
tmnxMobGwRfStatTxAcrInterimFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxAcrInterimFail.setStatus("current")
_TmnxMobGwRfStatTxAcrStopFails_Type = Counter32
_TmnxMobGwRfStatTxAcrStopFails_Object = MibTableColumn
tmnxMobGwRfStatTxAcrStopFails = _TmnxMobGwRfStatTxAcrStopFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 22),
    _TmnxMobGwRfStatTxAcrStopFails_Type()
)
tmnxMobGwRfStatTxAcrStopFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxAcrStopFails.setStatus("current")
_TmnxMobGwRfStatBearers_Type = Gauge32
_TmnxMobGwRfStatBearers_Object = MibTableColumn
tmnxMobGwRfStatBearers = _TmnxMobGwRfStatBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 23),
    _TmnxMobGwRfStatBearers_Type()
)
tmnxMobGwRfStatBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatBearers.setStatus("current")
_TmnxMobGwRfStatDefBearers_Type = Gauge32
_TmnxMobGwRfStatDefBearers_Object = MibTableColumn
tmnxMobGwRfStatDefBearers = _TmnxMobGwRfStatDefBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 24),
    _TmnxMobGwRfStatDefBearers_Type()
)
tmnxMobGwRfStatDefBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatDefBearers.setStatus("current")
_TmnxMobGwRfStatDedctdBearers_Type = Gauge32
_TmnxMobGwRfStatDedctdBearers_Object = MibTableColumn
tmnxMobGwRfStatDedctdBearers = _TmnxMobGwRfStatDedctdBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 25),
    _TmnxMobGwRfStatDedctdBearers_Type()
)
tmnxMobGwRfStatDedctdBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatDedctdBearers.setStatus("current")
_TmnxMobGwRfStatRoamers_Type = Gauge32
_TmnxMobGwRfStatRoamers_Object = MibTableColumn
tmnxMobGwRfStatRoamers = _TmnxMobGwRfStatRoamers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 26),
    _TmnxMobGwRfStatRoamers_Type()
)
tmnxMobGwRfStatRoamers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRoamers.setStatus("current")
_TmnxMobGwRfStatBearersIpv4_Type = Gauge32
_TmnxMobGwRfStatBearersIpv4_Object = MibTableColumn
tmnxMobGwRfStatBearersIpv4 = _TmnxMobGwRfStatBearersIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 27),
    _TmnxMobGwRfStatBearersIpv4_Type()
)
tmnxMobGwRfStatBearersIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatBearersIpv4.setStatus("current")
_TmnxMobGwRfStatBearersIpv6_Type = Gauge32
_TmnxMobGwRfStatBearersIpv6_Object = MibTableColumn
tmnxMobGwRfStatBearersIpv6 = _TmnxMobGwRfStatBearersIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 28),
    _TmnxMobGwRfStatBearersIpv6_Type()
)
tmnxMobGwRfStatBearersIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatBearersIpv6.setStatus("current")
_TmnxMobGwRfStatBearersIpv4v6_Type = Gauge32
_TmnxMobGwRfStatBearersIpv4v6_Object = MibTableColumn
tmnxMobGwRfStatBearersIpv4v6 = _TmnxMobGwRfStatBearersIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 29),
    _TmnxMobGwRfStatBearersIpv4v6_Type()
)
tmnxMobGwRfStatBearersIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatBearersIpv4v6.setStatus("current")
_TmnxMobGwRfStatActiveBearers_Type = Gauge32
_TmnxMobGwRfStatActiveBearers_Object = MibTableColumn
tmnxMobGwRfStatActiveBearers = _TmnxMobGwRfStatActiveBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 30),
    _TmnxMobGwRfStatActiveBearers_Type()
)
tmnxMobGwRfStatActiveBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatActiveBearers.setStatus("current")
_TmnxMobGwRfStatIdleBearers_Type = Gauge32
_TmnxMobGwRfStatIdleBearers_Object = MibTableColumn
tmnxMobGwRfStatIdleBearers = _TmnxMobGwRfStatIdleBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 31),
    _TmnxMobGwRfStatIdleBearers_Type()
)
tmnxMobGwRfStatIdleBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatIdleBearers.setStatus("current")
_TmnxMobGwRfStatTxDpr_Type = Counter32
_TmnxMobGwRfStatTxDpr_Object = MibTableColumn
tmnxMobGwRfStatTxDpr = _TmnxMobGwRfStatTxDpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 32),
    _TmnxMobGwRfStatTxDpr_Type()
)
tmnxMobGwRfStatTxDpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxDpr.setStatus("current")
_TmnxMobGwRfStatRxDpa_Type = Counter32
_TmnxMobGwRfStatRxDpa_Object = MibTableColumn
tmnxMobGwRfStatRxDpa = _TmnxMobGwRfStatRxDpa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 33),
    _TmnxMobGwRfStatRxDpa_Type()
)
tmnxMobGwRfStatRxDpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxDpa.setStatus("current")
_TmnxMobGwRfStatRxDwr_Type = Counter32
_TmnxMobGwRfStatRxDwr_Object = MibTableColumn
tmnxMobGwRfStatRxDwr = _TmnxMobGwRfStatRxDwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 34),
    _TmnxMobGwRfStatRxDwr_Type()
)
tmnxMobGwRfStatRxDwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatRxDwr.setStatus("current")
_TmnxMobGwRfStatTxDwa_Type = Counter32
_TmnxMobGwRfStatTxDwa_Object = MibTableColumn
tmnxMobGwRfStatTxDwa = _TmnxMobGwRfStatTxDwa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 9, 1, 35),
    _TmnxMobGwRfStatTxDwa_Type()
)
tmnxMobGwRfStatTxDwa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfStatTxDwa.setStatus("current")
_TmnxMobLiDfPeerTable_Object = MibTable
tmnxMobLiDfPeerTable = _TmnxMobLiDfPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxMobLiDfPeerTable.setStatus("current")
_TmnxMobLiDfPeerEntry_Object = MibTableRow
tmnxMobLiDfPeerEntry = _TmnxMobLiDfPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1)
)
tmnxMobLiDfPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDfPeer"),
)
if mibBuilder.loadTexts:
    tmnxMobLiDfPeerEntry.setStatus("current")
_TmnxMobLiDfPeer_Type = TmnxMobDfPeerId
_TmnxMobLiDfPeer_Object = MibTableColumn
tmnxMobLiDfPeer = _TmnxMobLiDfPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 1),
    _TmnxMobLiDfPeer_Type()
)
tmnxMobLiDfPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobLiDfPeer.setStatus("current")
_TmnxMobLiDfPeerRowStatus_Type = RowStatus
_TmnxMobLiDfPeerRowStatus_Object = MibTableColumn
tmnxMobLiDfPeerRowStatus = _TmnxMobLiDfPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 2),
    _TmnxMobLiDfPeerRowStatus_Type()
)
tmnxMobLiDfPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiDfPeerRowStatus.setStatus("current")
_TmnxMobLiDfPeerLastChanged_Type = TimeStamp
_TmnxMobLiDfPeerLastChanged_Object = MibTableColumn
tmnxMobLiDfPeerLastChanged = _TmnxMobLiDfPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 3),
    _TmnxMobLiDfPeerLastChanged_Type()
)
tmnxMobLiDfPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiDfPeerLastChanged.setStatus("current")


class _TmnxMobLiDf2PeerAddressType_Type(InetAddressType):
    """Custom type tmnxMobLiDf2PeerAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxMobLiDf2PeerAddressType_Type.__name__ = "InetAddressType"
_TmnxMobLiDf2PeerAddressType_Object = MibTableColumn
tmnxMobLiDf2PeerAddressType = _TmnxMobLiDf2PeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 4),
    _TmnxMobLiDf2PeerAddressType_Type()
)
tmnxMobLiDf2PeerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiDf2PeerAddressType.setStatus("current")


class _TmnxMobLiDf2PeerAddress_Type(InetAddress):
    """Custom type tmnxMobLiDf2PeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobLiDf2PeerAddress_Type.__name__ = "InetAddress"
_TmnxMobLiDf2PeerAddress_Object = MibTableColumn
tmnxMobLiDf2PeerAddress = _TmnxMobLiDf2PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 5),
    _TmnxMobLiDf2PeerAddress_Type()
)
tmnxMobLiDf2PeerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiDf2PeerAddress.setStatus("current")
_TmnxMobLiDf2PeerPort_Type = InetPortNumber
_TmnxMobLiDf2PeerPort_Object = MibTableColumn
tmnxMobLiDf2PeerPort = _TmnxMobLiDf2PeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 6),
    _TmnxMobLiDf2PeerPort_Type()
)
tmnxMobLiDf2PeerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiDf2PeerPort.setStatus("current")


class _TmnxMobLiDf3PeerAddressType_Type(InetAddressType):
    """Custom type tmnxMobLiDf3PeerAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxMobLiDf3PeerAddressType_Type.__name__ = "InetAddressType"
_TmnxMobLiDf3PeerAddressType_Object = MibTableColumn
tmnxMobLiDf3PeerAddressType = _TmnxMobLiDf3PeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 7),
    _TmnxMobLiDf3PeerAddressType_Type()
)
tmnxMobLiDf3PeerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiDf3PeerAddressType.setStatus("current")


class _TmnxMobLiDf3PeerAddress_Type(InetAddress):
    """Custom type tmnxMobLiDf3PeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobLiDf3PeerAddress_Type.__name__ = "InetAddress"
_TmnxMobLiDf3PeerAddress_Object = MibTableColumn
tmnxMobLiDf3PeerAddress = _TmnxMobLiDf3PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 8),
    _TmnxMobLiDf3PeerAddress_Type()
)
tmnxMobLiDf3PeerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiDf3PeerAddress.setStatus("current")
_TmnxMobLiDf3PeerPort_Type = InetPortNumber
_TmnxMobLiDf3PeerPort_Object = MibTableColumn
tmnxMobLiDf3PeerPort = _TmnxMobLiDf3PeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 9),
    _TmnxMobLiDf3PeerPort_Type()
)
tmnxMobLiDf3PeerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiDf3PeerPort.setStatus("current")
_TmnxMobLiDf2OperState_Type = TmnxOperState
_TmnxMobLiDf2OperState_Object = MibTableColumn
tmnxMobLiDf2OperState = _TmnxMobLiDf2OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 10),
    _TmnxMobLiDf2OperState_Type()
)
tmnxMobLiDf2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiDf2OperState.setStatus("current")
_TmnxMobLiDf2PeerPktsTx_Type = Counter32
_TmnxMobLiDf2PeerPktsTx_Object = MibTableColumn
tmnxMobLiDf2PeerPktsTx = _TmnxMobLiDf2PeerPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 11),
    _TmnxMobLiDf2PeerPktsTx_Type()
)
tmnxMobLiDf2PeerPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiDf2PeerPktsTx.setStatus("current")
_TmnxMobLiDf3OperState_Type = TmnxOperState
_TmnxMobLiDf3OperState_Object = MibTableColumn
tmnxMobLiDf3OperState = _TmnxMobLiDf3OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 12),
    _TmnxMobLiDf3OperState_Type()
)
tmnxMobLiDf3OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiDf3OperState.setStatus("current")
_TmnxMobLiDf3PeerPktsTx_Type = Counter32
_TmnxMobLiDf3PeerPktsTx_Object = MibTableColumn
tmnxMobLiDf3PeerPktsTx = _TmnxMobLiDf3PeerPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 13),
    _TmnxMobLiDf3PeerPktsTx_Type()
)
tmnxMobLiDf3PeerPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiDf3PeerPktsTx.setStatus("current")
_TmnxMobLiTotalTargetPerPeer_Type = Counter32
_TmnxMobLiTotalTargetPerPeer_Object = MibTableColumn
tmnxMobLiTotalTargetPerPeer = _TmnxMobLiTotalTargetPerPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 10, 1, 14),
    _TmnxMobLiTotalTargetPerPeer_Type()
)
tmnxMobLiTotalTargetPerPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiTotalTargetPerPeer.setStatus("current")
_TmnxMobLiTargetTable_Object = MibTable
tmnxMobLiTargetTable = _TmnxMobLiTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxMobLiTargetTable.setStatus("current")
_TmnxMobLiTargetEntry_Object = MibTableRow
tmnxMobLiTargetEntry = _TmnxMobLiTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11, 1)
)
tmnxMobLiTargetEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTargetType"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTargetId"),
)
if mibBuilder.loadTexts:
    tmnxMobLiTargetEntry.setStatus("current")
_TmnxMobLiTargetType_Type = TmnxMobLiTargetType
_TmnxMobLiTargetType_Object = MibTableColumn
tmnxMobLiTargetType = _TmnxMobLiTargetType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11, 1, 1),
    _TmnxMobLiTargetType_Type()
)
tmnxMobLiTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobLiTargetType.setStatus("current")
_TmnxMobLiTargetId_Type = TmnxMobLiTarget
_TmnxMobLiTargetId_Object = MibTableColumn
tmnxMobLiTargetId = _TmnxMobLiTargetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11, 1, 2),
    _TmnxMobLiTargetId_Type()
)
tmnxMobLiTargetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobLiTargetId.setStatus("current")
_TmnxMobLiTargetRowStatus_Type = RowStatus
_TmnxMobLiTargetRowStatus_Object = MibTableColumn
tmnxMobLiTargetRowStatus = _TmnxMobLiTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11, 1, 3),
    _TmnxMobLiTargetRowStatus_Type()
)
tmnxMobLiTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiTargetRowStatus.setStatus("current")
_TmnxMobLiTargetLastChanged_Type = TimeStamp
_TmnxMobLiTargetLastChanged_Object = MibTableColumn
tmnxMobLiTargetLastChanged = _TmnxMobLiTargetLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11, 1, 4),
    _TmnxMobLiTargetLastChanged_Type()
)
tmnxMobLiTargetLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiTargetLastChanged.setStatus("current")


class _TmnxMobLiTargetInterceptType_Type(Integer32):
    """Custom type tmnxMobLiTargetInterceptType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iri", 1),
          ("iriCC", 2))
    )


_TmnxMobLiTargetInterceptType_Type.__name__ = "Integer32"
_TmnxMobLiTargetInterceptType_Object = MibTableColumn
tmnxMobLiTargetInterceptType = _TmnxMobLiTargetInterceptType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11, 1, 5),
    _TmnxMobLiTargetInterceptType_Type()
)
tmnxMobLiTargetInterceptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiTargetInterceptType.setStatus("current")


class _TmnxMobLiTargetDfPeer_Type(TmnxMobDfPeerId):
    """Custom type tmnxMobLiTargetDfPeer based on TmnxMobDfPeerId"""
    defaultValue = 1


_TmnxMobLiTargetDfPeer_Type.__name__ = "TmnxMobDfPeerId"
_TmnxMobLiTargetDfPeer_Object = MibTableColumn
tmnxMobLiTargetDfPeer = _TmnxMobLiTargetDfPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11, 1, 6),
    _TmnxMobLiTargetDfPeer_Type()
)
tmnxMobLiTargetDfPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiTargetDfPeer.setStatus("current")


class _TmnxMobTargetLiId_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobTargetLiId based on TNamedItemOrEmpty"""
    defaultHexValue = ""

    subtypeSpec = TNamedItemOrEmpty.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TmnxMobTargetLiId_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobTargetLiId_Object = MibTableColumn
tmnxMobTargetLiId = _TmnxMobTargetLiId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 11, 1, 7),
    _TmnxMobTargetLiId_Type()
)
tmnxMobTargetLiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobTargetLiId.setStatus("current")
_TmnxMobThresGroupTable_Object = MibTable
tmnxMobThresGroupTable = _TmnxMobThresGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxMobThresGroupTable.setStatus("current")
_TmnxMobThresGroupEntry_Object = MibTableRow
tmnxMobThresGroupEntry = _TmnxMobThresGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 12, 1)
)
tmnxMobThresGroupEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresGrpId"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresSubGrpId"),
)
if mibBuilder.loadTexts:
    tmnxMobThresGroupEntry.setStatus("current")
_TmnxMobThresGrpId_Type = TmnxThresholdGroupType
_TmnxMobThresGrpId_Object = MibTableColumn
tmnxMobThresGrpId = _TmnxMobThresGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 12, 1, 1),
    _TmnxMobThresGrpId_Type()
)
tmnxMobThresGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobThresGrpId.setStatus("current")


class _TmnxMobThresSubGrpId_Type(Unsigned32):
    """Custom type tmnxMobThresSubGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMobThresSubGrpId_Type.__name__ = "Unsigned32"
_TmnxMobThresSubGrpId_Object = MibTableColumn
tmnxMobThresSubGrpId = _TmnxMobThresSubGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 12, 1, 2),
    _TmnxMobThresSubGrpId_Type()
)
tmnxMobThresSubGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobThresSubGrpId.setStatus("current")
_TmnxMobThresGrpRowStatus_Type = RowStatus
_TmnxMobThresGrpRowStatus_Object = MibTableColumn
tmnxMobThresGrpRowStatus = _TmnxMobThresGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 12, 1, 3),
    _TmnxMobThresGrpRowStatus_Type()
)
tmnxMobThresGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobThresGrpRowStatus.setStatus("current")
_TmnxMobThresGrpLastChanged_Type = TimeStamp
_TmnxMobThresGrpLastChanged_Object = MibTableColumn
tmnxMobThresGrpLastChanged = _TmnxMobThresGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 12, 1, 4),
    _TmnxMobThresGrpLastChanged_Type()
)
tmnxMobThresGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobThresGrpLastChanged.setStatus("current")


class _TmnxMobThresGrpAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobThresGrpAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobThresGrpAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobThresGrpAdminState_Object = MibTableColumn
tmnxMobThresGrpAdminState = _TmnxMobThresGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 12, 1, 5),
    _TmnxMobThresGrpAdminState_Type()
)
tmnxMobThresGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobThresGrpAdminState.setStatus("current")


class _TmnxMobThresGrpInterval_Type(Unsigned32):
    """Custom type tmnxMobThresGrpInterval based on Unsigned32"""
    defaultValue = 5


_TmnxMobThresGrpInterval_Type.__name__ = "Unsigned32"
_TmnxMobThresGrpInterval_Object = MibTableColumn
tmnxMobThresGrpInterval = _TmnxMobThresGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 12, 1, 6),
    _TmnxMobThresGrpInterval_Type()
)
tmnxMobThresGrpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobThresGrpInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobThresGrpInterval.setUnits("minutes")
_TmnxMobThresConfigTable_Object = MibTable
tmnxMobThresConfigTable = _TmnxMobThresConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxMobThresConfigTable.setStatus("current")
_TmnxMobThresConfigEntry_Object = MibTableRow
tmnxMobThresConfigEntry = _TmnxMobThresConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1)
)
tmnxMobThresConfigEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgGroupId"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgSubGroupId"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgCounterId"),
)
if mibBuilder.loadTexts:
    tmnxMobThresConfigEntry.setStatus("current")
_TmnxMobThresCfgGroupId_Type = TmnxThresholdGroupType
_TmnxMobThresCfgGroupId_Object = MibTableColumn
tmnxMobThresCfgGroupId = _TmnxMobThresCfgGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 1),
    _TmnxMobThresCfgGroupId_Type()
)
tmnxMobThresCfgGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobThresCfgGroupId.setStatus("current")


class _TmnxMobThresCfgSubGroupId_Type(Unsigned32):
    """Custom type tmnxMobThresCfgSubGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMobThresCfgSubGroupId_Type.__name__ = "Unsigned32"
_TmnxMobThresCfgSubGroupId_Object = MibTableColumn
tmnxMobThresCfgSubGroupId = _TmnxMobThresCfgSubGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 2),
    _TmnxMobThresCfgSubGroupId_Type()
)
tmnxMobThresCfgSubGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobThresCfgSubGroupId.setStatus("current")


class _TmnxMobThresCfgCounterId_Type(Integer32):
    """Custom type tmnxMobThresCfgCounterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("brMgmtLimitUEs", 1),
          ("brMgmtLimitBrs", 2),
          ("brMgmtLimitDefBrs", 3),
          ("brMgmtLimitDedBrs", 4),
          ("brMgmtLimitActBrs", 5),
          ("brMgmtLimitUePaged", 6),
          ("brMgmtCfsAttach", 7),
          ("brMgmtCfsDedBr", 8),
          ("brMgmtCfsSvrReq", 9),
          ("brMgmtCfsIntraReloc", 10),
          ("brMgmtCfsInterReloc", 11),
          ("brMgmtCfsIdleReloc", 12),
          ("brMgmtCffAttach", 13),
          ("brMgmtCffDedBr", 14),
          ("brMgmtCffPaging", 15),
          ("brMgmtCffHandOver", 16),
          ("brMgmtCffSvrReq", 17),
          ("brMgmtCffSvrUnavl", 18),
          ("brTrafficThrouputUL", 19),
          ("brTrafficThrouputDL", 20),
          ("brTrafficAspFail", 21),
          ("brTrafficBrBdvErr", 22),
          ("pathMgmtS5Fail", 23),
          ("pathMgmtS5Restart", 24),
          ("pathMgmtS5NoResp", 25),
          ("pathMgmtS11PrPath", 26),
          ("pathMgmtS11PrRstt", 27),
          ("pathMgmtS11NoResp", 28),
          ("pathMgmtRfPeerFail", 29),
          ("pathMgmtS1UENB", 30),
          ("pathMgmtS11MME", 31),
          ("pathMgmtS5Peer", 32),
          ("pathMgmtS8Peer", 33),
          ("pathMgmtGxFail", 34),
          ("pathMgmtRfFail", 35),
          ("mgIsmCpu", 36),
          ("mgIsmMem", 37),
          ("mgIsmUplink", 38),
          ("mgIsmDownlink", 39))
    )


_TmnxMobThresCfgCounterId_Type.__name__ = "Integer32"
_TmnxMobThresCfgCounterId_Object = MibTableColumn
tmnxMobThresCfgCounterId = _TmnxMobThresCfgCounterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 3),
    _TmnxMobThresCfgCounterId_Type()
)
tmnxMobThresCfgCounterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobThresCfgCounterId.setStatus("current")
_TmnxMobThresCfgRowStatus_Type = RowStatus
_TmnxMobThresCfgRowStatus_Object = MibTableColumn
tmnxMobThresCfgRowStatus = _TmnxMobThresCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 4),
    _TmnxMobThresCfgRowStatus_Type()
)
tmnxMobThresCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobThresCfgRowStatus.setStatus("current")
_TmnxMobThresCfgLastChanged_Type = TimeStamp
_TmnxMobThresCfgLastChanged_Object = MibTableColumn
tmnxMobThresCfgLastChanged = _TmnxMobThresCfgLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 5),
    _TmnxMobThresCfgLastChanged_Type()
)
tmnxMobThresCfgLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobThresCfgLastChanged.setStatus("current")
_TmnxMobThresCfgAlarmIndex_Type = Unsigned32
_TmnxMobThresCfgAlarmIndex_Object = MibTableColumn
tmnxMobThresCfgAlarmIndex = _TmnxMobThresCfgAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 6),
    _TmnxMobThresCfgAlarmIndex_Type()
)
tmnxMobThresCfgAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobThresCfgAlarmIndex.setStatus("current")
_TmnxMobThresCfgHighThreshold_Type = Integer32
_TmnxMobThresCfgHighThreshold_Object = MibTableColumn
tmnxMobThresCfgHighThreshold = _TmnxMobThresCfgHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 7),
    _TmnxMobThresCfgHighThreshold_Type()
)
tmnxMobThresCfgHighThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobThresCfgHighThreshold.setStatus("current")
_TmnxMobThresCfgLowThreshold_Type = Integer32
_TmnxMobThresCfgLowThreshold_Object = MibTableColumn
tmnxMobThresCfgLowThreshold = _TmnxMobThresCfgLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 8),
    _TmnxMobThresCfgLowThreshold_Type()
)
tmnxMobThresCfgLowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobThresCfgLowThreshold.setStatus("current")
_TmnxMobThresCfgCtrOID_Type = ObjectIdentifier
_TmnxMobThresCfgCtrOID_Object = MibTableColumn
tmnxMobThresCfgCtrOID = _TmnxMobThresCfgCtrOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 13, 1, 9),
    _TmnxMobThresCfgCtrOID_Type()
)
tmnxMobThresCfgCtrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobThresCfgCtrOID.setStatus("current")
_TmnxMobMgIsmThresTable_Object = MibTable
tmnxMobMgIsmThresTable = _TmnxMobMgIsmThresTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresTable.setStatus("current")
_TmnxMobMgIsmThresEntry_Object = MibTableRow
tmnxMobMgIsmThresEntry = _TmnxMobMgIsmThresEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 14, 1)
)
tmnxMobMgIsmThresEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobMgIsmThresGroupId"),
)
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresEntry.setStatus("current")


class _TmnxMobMgIsmThresGroupId_Type(Unsigned32):
    """Custom type tmnxMobMgIsmThresGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMobMgIsmThresGroupId_Type.__name__ = "Unsigned32"
_TmnxMobMgIsmThresGroupId_Object = MibTableColumn
tmnxMobMgIsmThresGroupId = _TmnxMobMgIsmThresGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 14, 1, 1),
    _TmnxMobMgIsmThresGroupId_Type()
)
tmnxMobMgIsmThresGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresGroupId.setStatus("current")
_TmnxMobMgIsmThresLastChanged_Type = TimeStamp
_TmnxMobMgIsmThresLastChanged_Object = MibTableColumn
tmnxMobMgIsmThresLastChanged = _TmnxMobMgIsmThresLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 14, 1, 2),
    _TmnxMobMgIsmThresLastChanged_Type()
)
tmnxMobMgIsmThresLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresLastChanged.setStatus("current")


class _TmnxMobMgIsmThresCpu_Type(Gauge32):
    """Custom type tmnxMobMgIsmThresCpu based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobMgIsmThresCpu_Type.__name__ = "Gauge32"
_TmnxMobMgIsmThresCpu_Object = MibTableColumn
tmnxMobMgIsmThresCpu = _TmnxMobMgIsmThresCpu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 14, 1, 3),
    _TmnxMobMgIsmThresCpu_Type()
)
tmnxMobMgIsmThresCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresCpu.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresCpu.setUnits("Percent")


class _TmnxMobMgIsmThresMem_Type(Gauge32):
    """Custom type tmnxMobMgIsmThresMem based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobMgIsmThresMem_Type.__name__ = "Gauge32"
_TmnxMobMgIsmThresMem_Object = MibTableColumn
tmnxMobMgIsmThresMem = _TmnxMobMgIsmThresMem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 14, 1, 4),
    _TmnxMobMgIsmThresMem_Type()
)
tmnxMobMgIsmThresMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresMem.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresMem.setUnits("Percent")
_TmnxMobMgIsmThresThrptUL_Type = Gauge32
_TmnxMobMgIsmThresThrptUL_Object = MibTableColumn
tmnxMobMgIsmThresThrptUL = _TmnxMobMgIsmThresThrptUL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 14, 1, 5),
    _TmnxMobMgIsmThresThrptUL_Type()
)
tmnxMobMgIsmThresThrptUL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresThrptUL.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresThrptUL.setUnits("megabytes")
_TmnxMobMgIsmThresThrptDL_Type = Gauge32
_TmnxMobMgIsmThresThrptDL_Object = MibTableColumn
tmnxMobMgIsmThresThrptDL = _TmnxMobMgIsmThresThrptDL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 14, 1, 6),
    _TmnxMobMgIsmThresThrptDL_Type()
)
tmnxMobMgIsmThresThrptDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresThrptDL.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobMgIsmThresThrptDL.setUnits("megabytes")
_TmnxMobGwS5CauseCodeTable_Object = MibTable
tmnxMobGwS5CauseCodeTable = _TmnxMobGwS5CauseCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxMobGwS5CauseCodeTable.setStatus("current")
_TmnxMobGwS5CauseCodeEntry_Object = MibTableRow
tmnxMobGwS5CauseCodeEntry = _TmnxMobGwS5CauseCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1)
)
if mibBuilder.loadTexts:
    tmnxMobGwS5CauseCodeEntry.setStatus("current")
_TmnxMobGwS5CcRxReqAccepted_Type = Counter32
_TmnxMobGwS5CcRxReqAccepted_Object = MibTableColumn
tmnxMobGwS5CcRxReqAccepted = _TmnxMobGwS5CcRxReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 1),
    _TmnxMobGwS5CcRxReqAccepted_Type()
)
tmnxMobGwS5CcRxReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxReqAccepted.setStatus("current")
_TmnxMobGwS5CcRxCtxNotFound_Type = Counter32
_TmnxMobGwS5CcRxCtxNotFound_Object = MibTableColumn
tmnxMobGwS5CcRxCtxNotFound = _TmnxMobGwS5CcRxCtxNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 2),
    _TmnxMobGwS5CcRxCtxNotFound_Type()
)
tmnxMobGwS5CcRxCtxNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxCtxNotFound.setStatus("current")
_TmnxMobGwS5CcRxInvalidLength_Type = Counter32
_TmnxMobGwS5CcRxInvalidLength_Object = MibTableColumn
tmnxMobGwS5CcRxInvalidLength = _TmnxMobGwS5CcRxInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 3),
    _TmnxMobGwS5CcRxInvalidLength_Type()
)
tmnxMobGwS5CcRxInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxInvalidLength.setStatus("current")
_TmnxMobGwS5CcRxMndIeIncorrect_Type = Counter32
_TmnxMobGwS5CcRxMndIeIncorrect_Object = MibTableColumn
tmnxMobGwS5CcRxMndIeIncorrect = _TmnxMobGwS5CcRxMndIeIncorrect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 4),
    _TmnxMobGwS5CcRxMndIeIncorrect_Type()
)
tmnxMobGwS5CcRxMndIeIncorrect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxMndIeIncorrect.setStatus("current")
_TmnxMobGwS5CcRxMandIeMissing_Type = Counter32
_TmnxMobGwS5CcRxMandIeMissing_Object = MibTableColumn
tmnxMobGwS5CcRxMandIeMissing = _TmnxMobGwS5CcRxMandIeMissing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 5),
    _TmnxMobGwS5CcRxMandIeMissing_Type()
)
tmnxMobGwS5CcRxMandIeMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxMandIeMissing.setStatus("current")
_TmnxMobGwS5CcRxReqRejected_Type = Counter32
_TmnxMobGwS5CcRxReqRejected_Object = MibTableColumn
tmnxMobGwS5CcRxReqRejected = _TmnxMobGwS5CcRxReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 6),
    _TmnxMobGwS5CcRxReqRejected_Type()
)
tmnxMobGwS5CcRxReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxReqRejected.setStatus("current")
_TmnxMobGwS5CcRxRemPeerNoResp_Type = Counter32
_TmnxMobGwS5CcRxRemPeerNoResp_Object = MibTableColumn
tmnxMobGwS5CcRxRemPeerNoResp = _TmnxMobGwS5CcRxRemPeerNoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 7),
    _TmnxMobGwS5CcRxRemPeerNoResp_Type()
)
tmnxMobGwS5CcRxRemPeerNoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxRemPeerNoResp.setStatus("current")
_TmnxMobGwS5CcRxNoResAvailable_Type = Counter32
_TmnxMobGwS5CcRxNoResAvailable_Object = MibTableColumn
tmnxMobGwS5CcRxNoResAvailable = _TmnxMobGwS5CcRxNoResAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 8),
    _TmnxMobGwS5CcRxNoResAvailable_Type()
)
tmnxMobGwS5CcRxNoResAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxNoResAvailable.setStatus("current")
_TmnxMobGwS5CcRxUsrAuthFailure_Type = Counter32
_TmnxMobGwS5CcRxUsrAuthFailure_Object = MibTableColumn
tmnxMobGwS5CcRxUsrAuthFailure = _TmnxMobGwS5CcRxUsrAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 9),
    _TmnxMobGwS5CcRxUsrAuthFailure_Type()
)
tmnxMobGwS5CcRxUsrAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxUsrAuthFailure.setStatus("current")
_TmnxMobGwS5CcRxOthers_Type = Counter32
_TmnxMobGwS5CcRxOthers_Object = MibTableColumn
tmnxMobGwS5CcRxOthers = _TmnxMobGwS5CcRxOthers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 10),
    _TmnxMobGwS5CcRxOthers_Type()
)
tmnxMobGwS5CcRxOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcRxOthers.setStatus("current")
_TmnxMobGwS5CcTxReqAccepted_Type = Counter32
_TmnxMobGwS5CcTxReqAccepted_Object = MibTableColumn
tmnxMobGwS5CcTxReqAccepted = _TmnxMobGwS5CcTxReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 11),
    _TmnxMobGwS5CcTxReqAccepted_Type()
)
tmnxMobGwS5CcTxReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxReqAccepted.setStatus("current")
_TmnxMobGwS5CcTxCtxNotFound_Type = Counter32
_TmnxMobGwS5CcTxCtxNotFound_Object = MibTableColumn
tmnxMobGwS5CcTxCtxNotFound = _TmnxMobGwS5CcTxCtxNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 12),
    _TmnxMobGwS5CcTxCtxNotFound_Type()
)
tmnxMobGwS5CcTxCtxNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxCtxNotFound.setStatus("current")
_TmnxMobGwS5CcTxInvalidLength_Type = Counter32
_TmnxMobGwS5CcTxInvalidLength_Object = MibTableColumn
tmnxMobGwS5CcTxInvalidLength = _TmnxMobGwS5CcTxInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 13),
    _TmnxMobGwS5CcTxInvalidLength_Type()
)
tmnxMobGwS5CcTxInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxInvalidLength.setStatus("current")
_TmnxMobGwS5CcTxMndIeIncorrect_Type = Counter32
_TmnxMobGwS5CcTxMndIeIncorrect_Object = MibTableColumn
tmnxMobGwS5CcTxMndIeIncorrect = _TmnxMobGwS5CcTxMndIeIncorrect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 14),
    _TmnxMobGwS5CcTxMndIeIncorrect_Type()
)
tmnxMobGwS5CcTxMndIeIncorrect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxMndIeIncorrect.setStatus("current")
_TmnxMobGwS5CcTxMandIeMissing_Type = Counter32
_TmnxMobGwS5CcTxMandIeMissing_Object = MibTableColumn
tmnxMobGwS5CcTxMandIeMissing = _TmnxMobGwS5CcTxMandIeMissing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 15),
    _TmnxMobGwS5CcTxMandIeMissing_Type()
)
tmnxMobGwS5CcTxMandIeMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxMandIeMissing.setStatus("current")
_TmnxMobGwS5CcTxReqRejected_Type = Counter32
_TmnxMobGwS5CcTxReqRejected_Object = MibTableColumn
tmnxMobGwS5CcTxReqRejected = _TmnxMobGwS5CcTxReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 16),
    _TmnxMobGwS5CcTxReqRejected_Type()
)
tmnxMobGwS5CcTxReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxReqRejected.setStatus("current")
_TmnxMobGwS5CcTxRemPeerNoResp_Type = Counter32
_TmnxMobGwS5CcTxRemPeerNoResp_Object = MibTableColumn
tmnxMobGwS5CcTxRemPeerNoResp = _TmnxMobGwS5CcTxRemPeerNoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 17),
    _TmnxMobGwS5CcTxRemPeerNoResp_Type()
)
tmnxMobGwS5CcTxRemPeerNoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxRemPeerNoResp.setStatus("current")
_TmnxMobGwS5CcTxNoResAvailable_Type = Counter32
_TmnxMobGwS5CcTxNoResAvailable_Object = MibTableColumn
tmnxMobGwS5CcTxNoResAvailable = _TmnxMobGwS5CcTxNoResAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 18),
    _TmnxMobGwS5CcTxNoResAvailable_Type()
)
tmnxMobGwS5CcTxNoResAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxNoResAvailable.setStatus("current")
_TmnxMobGwS5CcTxUsrAuthFailure_Type = Counter32
_TmnxMobGwS5CcTxUsrAuthFailure_Object = MibTableColumn
tmnxMobGwS5CcTxUsrAuthFailure = _TmnxMobGwS5CcTxUsrAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 19),
    _TmnxMobGwS5CcTxUsrAuthFailure_Type()
)
tmnxMobGwS5CcTxUsrAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxUsrAuthFailure.setStatus("current")
_TmnxMobGwS5CcTxOthers_Type = Counter32
_TmnxMobGwS5CcTxOthers_Object = MibTableColumn
tmnxMobGwS5CcTxOthers = _TmnxMobGwS5CcTxOthers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 1, 15, 1, 20),
    _TmnxMobGwS5CcTxOthers_Type()
)
tmnxMobGwS5CcTxOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5CcTxOthers.setStatus("current")
_TmnxMobGatewayGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxMobGatewayGlobalObjs = _TmnxMobGatewayGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2)
)
_TmnxMobGwTableLastChanged_Type = TimeStamp
_TmnxMobGwTableLastChanged_Object = MibScalar
tmnxMobGwTableLastChanged = _TmnxMobGwTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 1),
    _TmnxMobGwTableLastChanged_Type()
)
tmnxMobGwTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwTableLastChanged.setStatus("current")
_TmnxMobGwSysGroupTblLstChgd_Type = TimeStamp
_TmnxMobGwSysGroupTblLstChgd_Object = MibScalar
tmnxMobGwSysGroupTblLstChgd = _TmnxMobGwSysGroupTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 2),
    _TmnxMobGwSysGroupTblLstChgd_Type()
)
tmnxMobGwSysGroupTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupTblLstChgd.setStatus("current")
_TmnxMobGwSysGroupCardTblLstChgd_Type = TimeStamp
_TmnxMobGwSysGroupCardTblLstChgd_Object = MibScalar
tmnxMobGwSysGroupCardTblLstChgd = _TmnxMobGwSysGroupCardTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 3),
    _TmnxMobGwSysGroupCardTblLstChgd_Type()
)
tmnxMobGwSysGroupCardTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwSysGroupCardTblLstChgd.setStatus("current")


class _TmnxMobGwSysLimitName_Type(TmnxMobProfName):
    """Custom type tmnxMobGwSysLimitName based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobGwSysLimitName_Type.__name__ = "TmnxMobProfName"
_TmnxMobGwSysLimitName_Object = MibScalar
tmnxMobGwSysLimitName = _TmnxMobGwSysLimitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 4),
    _TmnxMobGwSysLimitName_Type()
)
tmnxMobGwSysLimitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobGwSysLimitName.setStatus("current")
_TmnxMobGwS5PeerTableLastChanged_Type = TimeStamp
_TmnxMobGwS5PeerTableLastChanged_Object = MibScalar
tmnxMobGwS5PeerTableLastChanged = _TmnxMobGwS5PeerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 5),
    _TmnxMobGwS5PeerTableLastChanged_Type()
)
tmnxMobGwS5PeerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS5PeerTableLastChanged.setStatus("current")
_TmnxMobGwS8PeerTableLastChanged_Type = TimeStamp
_TmnxMobGwS8PeerTableLastChanged_Object = MibScalar
tmnxMobGwS8PeerTableLastChanged = _TmnxMobGwS8PeerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 6),
    _TmnxMobGwS8PeerTableLastChanged_Type()
)
tmnxMobGwS8PeerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwS8PeerTableLastChanged.setStatus("current")
_TmnxMobGwRfPeerTableLastChngd_Type = TimeStamp
_TmnxMobGwRfPeerTableLastChngd_Object = MibScalar
tmnxMobGwRfPeerTableLastChngd = _TmnxMobGwRfPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 7),
    _TmnxMobGwRfPeerTableLastChngd_Type()
)
tmnxMobGwRfPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobGwRfPeerTableLastChngd.setStatus("current")
_TmnxMobLiDfPeerTableLastChanged_Type = TimeStamp
_TmnxMobLiDfPeerTableLastChanged_Object = MibScalar
tmnxMobLiDfPeerTableLastChanged = _TmnxMobLiDfPeerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 8),
    _TmnxMobLiDfPeerTableLastChanged_Type()
)
tmnxMobLiDfPeerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiDfPeerTableLastChanged.setStatus("current")
_TmnxMobLiTargetTableLastChanged_Type = TimeStamp
_TmnxMobLiTargetTableLastChanged_Object = MibScalar
tmnxMobLiTargetTableLastChanged = _TmnxMobLiTargetTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 9),
    _TmnxMobLiTargetTableLastChanged_Type()
)
tmnxMobLiTargetTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiTargetTableLastChanged.setStatus("current")
_TmnxMobThresGroupLastChgd_Type = TimeStamp
_TmnxMobThresGroupLastChgd_Object = MibScalar
tmnxMobThresGroupLastChgd = _TmnxMobThresGroupLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 10),
    _TmnxMobThresGroupLastChgd_Type()
)
tmnxMobThresGroupLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobThresGroupLastChgd.setStatus("current")
_TmnxMobGatewayGlobalLiObjs_ObjectIdentity = ObjectIdentity
tmnxMobGatewayGlobalLiObjs = _TmnxMobGatewayGlobalLiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11)
)


class _TmnxMobLiX3Transport_Type(Integer32):
    """Custom type tmnxMobLiX3Transport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_TmnxMobLiX3Transport_Type.__name__ = "Integer32"
_TmnxMobLiX3Transport_Object = MibScalar
tmnxMobLiX3Transport = _TmnxMobLiX3Transport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 1),
    _TmnxMobLiX3Transport_Type()
)
tmnxMobLiX3Transport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiX3Transport.setStatus("current")


class _TmnxMobLiLocalInterfaceType_Type(InetAddressType):
    """Custom type tmnxMobLiLocalInterfaceType based on InetAddressType"""
    defaultValue = 0


_TmnxMobLiLocalInterfaceType_Type.__name__ = "InetAddressType"
_TmnxMobLiLocalInterfaceType_Object = MibScalar
tmnxMobLiLocalInterfaceType = _TmnxMobLiLocalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 2),
    _TmnxMobLiLocalInterfaceType_Type()
)
tmnxMobLiLocalInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiLocalInterfaceType.setStatus("current")


class _TmnxMobLiLocalInterface_Type(InetAddress):
    """Custom type tmnxMobLiLocalInterface based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobLiLocalInterface_Type.__name__ = "InetAddress"
_TmnxMobLiLocalInterface_Object = MibScalar
tmnxMobLiLocalInterface = _TmnxMobLiLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 3),
    _TmnxMobLiLocalInterface_Type()
)
tmnxMobLiLocalInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiLocalInterface.setStatus("current")
_TmnxMobLiTotalTargets_Type = Counter32
_TmnxMobLiTotalTargets_Object = MibScalar
tmnxMobLiTotalTargets = _TmnxMobLiTotalTargets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 4),
    _TmnxMobLiTotalTargets_Type()
)
tmnxMobLiTotalTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiTotalTargets.setStatus("current")
_TmnxMobLiTotalPeers_Type = Counter32
_TmnxMobLiTotalPeers_Object = MibScalar
tmnxMobLiTotalPeers = _TmnxMobLiTotalPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 5),
    _TmnxMobLiTotalPeers_Type()
)
tmnxMobLiTotalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiTotalPeers.setStatus("current")
_TmnxMobLiTotalIRITargets_Type = Counter32
_TmnxMobLiTotalIRITargets_Object = MibScalar
tmnxMobLiTotalIRITargets = _TmnxMobLiTotalIRITargets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 6),
    _TmnxMobLiTotalIRITargets_Type()
)
tmnxMobLiTotalIRITargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiTotalIRITargets.setStatus("current")
_TmnxMobLiTotalIRICCTargets_Type = Counter32
_TmnxMobLiTotalIRICCTargets_Object = MibScalar
tmnxMobLiTotalIRICCTargets = _TmnxMobLiTotalIRICCTargets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 7),
    _TmnxMobLiTotalIRICCTargets_Type()
)
tmnxMobLiTotalIRICCTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobLiTotalIRICCTargets.setStatus("current")


class _TmnxMobLiVprnId_Type(TmnxVRtrID):
    """Custom type tmnxMobLiVprnId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobLiVprnId_Type.__name__ = "TmnxVRtrID"
_TmnxMobLiVprnId_Object = MibScalar
tmnxMobLiVprnId = _TmnxMobLiVprnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 8),
    _TmnxMobLiVprnId_Type()
)
tmnxMobLiVprnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiVprnId.setStatus("current")


class _TmnxMobLiULICVersion_Type(Integer32):
    """Custom type tmnxMobLiULICVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v0", 0),
          ("v1", 1))
    )


_TmnxMobLiULICVersion_Type.__name__ = "Integer32"
_TmnxMobLiULICVersion_Object = MibScalar
tmnxMobLiULICVersion = _TmnxMobLiULICVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 9),
    _TmnxMobLiULICVersion_Type()
)
tmnxMobLiULICVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiULICVersion.setStatus("current")


class _TmnxMobLiULIChangeReporting_Type(Integer32):
    """Custom type tmnxMobLiULIChangeReporting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_TmnxMobLiULIChangeReporting_Type.__name__ = "Integer32"
_TmnxMobLiULIChangeReporting_Object = MibScalar
tmnxMobLiULIChangeReporting = _TmnxMobLiULIChangeReporting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 10),
    _TmnxMobLiULIChangeReporting_Type()
)
tmnxMobLiULIChangeReporting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiULIChangeReporting.setStatus("current")


class _TmnxMobLiOperatorId_Type(TNamedItem):
    """Custom type tmnxMobLiOperatorId based on TNamedItem"""
    defaultValue = OctetString("op_id")

    subtypeSpec = TNamedItem.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_TmnxMobLiOperatorId_Type.__name__ = "TNamedItem"
_TmnxMobLiOperatorId_Object = MibScalar
tmnxMobLiOperatorId = _TmnxMobLiOperatorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 11, 11),
    _TmnxMobLiOperatorId_Type()
)
tmnxMobLiOperatorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobLiOperatorId.setStatus("current")
_TmnxMobThresConfigLastChanged_Type = TimeStamp
_TmnxMobThresConfigLastChanged_Object = MibScalar
tmnxMobThresConfigLastChanged = _TmnxMobThresConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 2, 12),
    _TmnxMobThresConfigLastChanged_Type()
)
tmnxMobThresConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobThresConfigLastChanged.setStatus("current")
_TmnxMobGatewayNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxMobGatewayNotificationObjs = _TmnxMobGatewayNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3)
)
_TmnxMobGwNtfyGatewayId_Type = TmnxMobGwId
_TmnxMobGwNtfyGatewayId_Object = MibScalar
tmnxMobGwNtfyGatewayId = _TmnxMobGwNtfyGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 1),
    _TmnxMobGwNtfyGatewayId_Type()
)
tmnxMobGwNtfyGatewayId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGatewayId.setStatus("current")
_TmnxMobGwNtfyVrtrId_Type = TmnxVRtrID
_TmnxMobGwNtfyVrtrId_Object = MibScalar
tmnxMobGwNtfyVrtrId = _TmnxMobGwNtfyVrtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 2),
    _TmnxMobGwNtfyVrtrId_Type()
)
tmnxMobGwNtfyVrtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyVrtrId.setStatus("current")


class _TmnxMobGwNtfyRefPointType_Type(Integer32):
    """Custom type tmnxMobGwNtfyRefPointType based on Integer32"""
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
        *(("s1u", 1),
          ("s5", 2),
          ("s8", 3),
          ("s11", 4),
          ("gn", 5),
          ("s2a", 6))
    )


_TmnxMobGwNtfyRefPointType_Type.__name__ = "Integer32"
_TmnxMobGwNtfyRefPointType_Object = MibScalar
tmnxMobGwNtfyRefPointType = _TmnxMobGwNtfyRefPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 3),
    _TmnxMobGwNtfyRefPointType_Type()
)
tmnxMobGwNtfyRefPointType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRefPointType.setStatus("current")


class _TmnxMobGwNtfyRefPointProtocol_Type(Integer32):
    """Custom type tmnxMobGwNtfyRefPointProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gtp", 1),
          ("pmip", 2))
    )


_TmnxMobGwNtfyRefPointProtocol_Type.__name__ = "Integer32"
_TmnxMobGwNtfyRefPointProtocol_Object = MibScalar
tmnxMobGwNtfyRefPointProtocol = _TmnxMobGwNtfyRefPointProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 4),
    _TmnxMobGwNtfyRefPointProtocol_Type()
)
tmnxMobGwNtfyRefPointProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRefPointProtocol.setStatus("current")
_TmnxMobGwNtfyRfPtPeerAddrType_Type = InetAddressType
_TmnxMobGwNtfyRfPtPeerAddrType_Object = MibScalar
tmnxMobGwNtfyRfPtPeerAddrType = _TmnxMobGwNtfyRfPtPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 5),
    _TmnxMobGwNtfyRfPtPeerAddrType_Type()
)
tmnxMobGwNtfyRfPtPeerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRfPtPeerAddrType.setStatus("current")
_TmnxMobGwNtfyRfPtPeerAddr_Type = InetAddress
_TmnxMobGwNtfyRfPtPeerAddr_Object = MibScalar
tmnxMobGwNtfyRfPtPeerAddr = _TmnxMobGwNtfyRfPtPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 6),
    _TmnxMobGwNtfyRfPtPeerAddr_Type()
)
tmnxMobGwNtfyRfPtPeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRfPtPeerAddr.setStatus("current")
_TmnxMobGwNtfyRfPtPeerPort_Type = InetPortNumber
_TmnxMobGwNtfyRfPtPeerPort_Object = MibScalar
tmnxMobGwNtfyRfPtPeerPort = _TmnxMobGwNtfyRfPtPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 7),
    _TmnxMobGwNtfyRfPtPeerPort_Type()
)
tmnxMobGwNtfyRfPtPeerPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRfPtPeerPort.setStatus("current")


class _TmnxMobGwNtfyPathMgmtPeerState_Type(Integer32):
    """Custom type tmnxMobGwNtfyPathMgmtPeerState based on Integer32"""
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
        *(("added", 1),
          ("deleted", 2),
          ("pathUp", 3),
          ("pathDown", 4),
          ("pathRestart", 5),
          ("pathIdle", 6))
    )


_TmnxMobGwNtfyPathMgmtPeerState_Type.__name__ = "Integer32"
_TmnxMobGwNtfyPathMgmtPeerState_Object = MibScalar
tmnxMobGwNtfyPathMgmtPeerState = _TmnxMobGwNtfyPathMgmtPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 8),
    _TmnxMobGwNtfyPathMgmtPeerState_Type()
)
tmnxMobGwNtfyPathMgmtPeerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyPathMgmtPeerState.setStatus("current")


class _TmnxMobGwNtfyDiaRefPointType_Type(Integer32):
    """Custom type tmnxMobGwNtfyDiaRefPointType based on Integer32"""
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
        *(("gx", 1),
          ("rf", 2),
          ("gy", 3),
          ("s6b", 4))
    )


_TmnxMobGwNtfyDiaRefPointType_Type.__name__ = "Integer32"
_TmnxMobGwNtfyDiaRefPointType_Object = MibScalar
tmnxMobGwNtfyDiaRefPointType = _TmnxMobGwNtfyDiaRefPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 9),
    _TmnxMobGwNtfyDiaRefPointType_Type()
)
tmnxMobGwNtfyDiaRefPointType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyDiaRefPointType.setStatus("current")
_TmnxMobGwNtfyDiaPeerName_Type = TmnxMobProfName
_TmnxMobGwNtfyDiaPeerName_Object = MibScalar
tmnxMobGwNtfyDiaPeerName = _TmnxMobGwNtfyDiaPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 10),
    _TmnxMobGwNtfyDiaPeerName_Type()
)
tmnxMobGwNtfyDiaPeerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyDiaPeerName.setStatus("current")
_TmnxMobGwNtfyDiaPeerIndex_Type = Unsigned32
_TmnxMobGwNtfyDiaPeerIndex_Object = MibScalar
tmnxMobGwNtfyDiaPeerIndex = _TmnxMobGwNtfyDiaPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 11),
    _TmnxMobGwNtfyDiaPeerIndex_Type()
)
tmnxMobGwNtfyDiaPeerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyDiaPeerIndex.setStatus("current")
_TmnxMobGwNtfyDiaPeerAddrType_Type = InetAddressType
_TmnxMobGwNtfyDiaPeerAddrType_Object = MibScalar
tmnxMobGwNtfyDiaPeerAddrType = _TmnxMobGwNtfyDiaPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 12),
    _TmnxMobGwNtfyDiaPeerAddrType_Type()
)
tmnxMobGwNtfyDiaPeerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyDiaPeerAddrType.setStatus("current")
_TmnxMobGwNtfyDiaPeerAddr_Type = InetAddress
_TmnxMobGwNtfyDiaPeerAddr_Object = MibScalar
tmnxMobGwNtfyDiaPeerAddr = _TmnxMobGwNtfyDiaPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 13),
    _TmnxMobGwNtfyDiaPeerAddr_Type()
)
tmnxMobGwNtfyDiaPeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyDiaPeerAddr.setStatus("current")
_TmnxMobGwNtfyDiaPeerPort_Type = InetPortNumber
_TmnxMobGwNtfyDiaPeerPort_Object = MibScalar
tmnxMobGwNtfyDiaPeerPort = _TmnxMobGwNtfyDiaPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 14),
    _TmnxMobGwNtfyDiaPeerPort_Type()
)
tmnxMobGwNtfyDiaPeerPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyDiaPeerPort.setStatus("current")


class _TmnxMobGwNtfyDiameterPeerState_Type(Integer32):
    """Custom type tmnxMobGwNtfyDiameterPeerState based on Integer32"""
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
        *(("pathUp", 1),
          ("pathDown", 2),
          ("nwFailureDown", 3),
          ("added", 4),
          ("deleted", 5),
          ("pathPartialUp", 6))
    )


_TmnxMobGwNtfyDiameterPeerState_Type.__name__ = "Integer32"
_TmnxMobGwNtfyDiameterPeerState_Object = MibScalar
tmnxMobGwNtfyDiameterPeerState = _TmnxMobGwNtfyDiameterPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 15),
    _TmnxMobGwNtfyDiameterPeerState_Type()
)
tmnxMobGwNtfyDiameterPeerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyDiameterPeerState.setStatus("current")


class _TmnxMobGwNtfyDiameterReasonCode_Type(Integer32):
    """Custom type tmnxMobGwNtfyDiameterReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("adminDown", 3),
          ("dwrTimeout", 4),
          ("permFailureRecvd", 5),
          ("dnsFailure", 6),
          ("dprRecvd", 7),
          ("remoteDisconnect", 8),
          ("localDisconnect", 9),
          ("peerAdded", 10),
          ("peerDeleted", 11),
          ("peerActive", 12))
    )


_TmnxMobGwNtfyDiameterReasonCode_Type.__name__ = "Integer32"
_TmnxMobGwNtfyDiameterReasonCode_Object = MibScalar
tmnxMobGwNtfyDiameterReasonCode = _TmnxMobGwNtfyDiameterReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 16),
    _TmnxMobGwNtfyDiameterReasonCode_Type()
)
tmnxMobGwNtfyDiameterReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyDiameterReasonCode.setStatus("current")


class _TmnxMobGwNtfyChrgRefPointType_Type(Integer32):
    """Custom type tmnxMobGwNtfyChrgRefPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rf", 1),
          ("ga", 2))
    )


_TmnxMobGwNtfyChrgRefPointType_Type.__name__ = "Integer32"
_TmnxMobGwNtfyChrgRefPointType_Object = MibScalar
tmnxMobGwNtfyChrgRefPointType = _TmnxMobGwNtfyChrgRefPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 17),
    _TmnxMobGwNtfyChrgRefPointType_Type()
)
tmnxMobGwNtfyChrgRefPointType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyChrgRefPointType.setStatus("current")
_TmnxMobGwNtfyPriCdfDiaPeer_Type = TmnxMobProfName
_TmnxMobGwNtfyPriCdfDiaPeer_Object = MibScalar
tmnxMobGwNtfyPriCdfDiaPeer = _TmnxMobGwNtfyPriCdfDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 18),
    _TmnxMobGwNtfyPriCdfDiaPeer_Type()
)
tmnxMobGwNtfyPriCdfDiaPeer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyPriCdfDiaPeer.setStatus("current")
_TmnxMobGwNtfySecCdfDiaPeer_Type = TmnxMobProfName
_TmnxMobGwNtfySecCdfDiaPeer_Object = MibScalar
tmnxMobGwNtfySecCdfDiaPeer = _TmnxMobGwNtfySecCdfDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 19),
    _TmnxMobGwNtfySecCdfDiaPeer_Type()
)
tmnxMobGwNtfySecCdfDiaPeer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfySecCdfDiaPeer.setStatus("current")
_TmnxMobGwNtfyCdfDiaPeer_Type = TmnxMobProfName
_TmnxMobGwNtfyCdfDiaPeer_Object = MibScalar
tmnxMobGwNtfyCdfDiaPeer = _TmnxMobGwNtfyCdfDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 20),
    _TmnxMobGwNtfyCdfDiaPeer_Type()
)
tmnxMobGwNtfyCdfDiaPeer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyCdfDiaPeer.setStatus("current")


class _TmnxMobGwNtfyFlashId_Type(Integer32):
    """Custom type tmnxMobGwNtfyFlashId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cf1", 1),
          ("cf2", 2))
    )


_TmnxMobGwNtfyFlashId_Type.__name__ = "Integer32"
_TmnxMobGwNtfyFlashId_Object = MibScalar
tmnxMobGwNtfyFlashId = _TmnxMobGwNtfyFlashId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 21),
    _TmnxMobGwNtfyFlashId_Type()
)
tmnxMobGwNtfyFlashId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyFlashId.setStatus("current")
_TmnxMobGwNtfyCfLimit_Type = Unsigned32
_TmnxMobGwNtfyCfLimit_Object = MibScalar
tmnxMobGwNtfyCfLimit = _TmnxMobGwNtfyCfLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 22),
    _TmnxMobGwNtfyCfLimit_Type()
)
tmnxMobGwNtfyCfLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyCfLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyCfLimit.setUnits("megabytes")


class _TmnxMobGwNtfyAcrFailureType_Type(Integer32):
    """Custom type tmnxMobGwNtfyAcrFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail2In10Sec", 1),
          ("fail5In60Sec", 2))
    )


_TmnxMobGwNtfyAcrFailureType_Type.__name__ = "Integer32"
_TmnxMobGwNtfyAcrFailureType_Object = MibScalar
tmnxMobGwNtfyAcrFailureType = _TmnxMobGwNtfyAcrFailureType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 23),
    _TmnxMobGwNtfyAcrFailureType_Type()
)
tmnxMobGwNtfyAcrFailureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyAcrFailureType.setStatus("current")
_TmnxMobGwNtfyGtpPriGrpName_Type = TmnxMobProfName
_TmnxMobGwNtfyGtpPriGrpName_Object = MibScalar
tmnxMobGwNtfyGtpPriGrpName = _TmnxMobGwNtfyGtpPriGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 24),
    _TmnxMobGwNtfyGtpPriGrpName_Type()
)
tmnxMobGwNtfyGtpPriGrpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriGrpName.setStatus("current")
_TmnxMobGwNtfyGtpPriServIndex_Type = Unsigned32
_TmnxMobGwNtfyGtpPriServIndex_Object = MibScalar
tmnxMobGwNtfyGtpPriServIndex = _TmnxMobGwNtfyGtpPriServIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 25),
    _TmnxMobGwNtfyGtpPriServIndex_Type()
)
tmnxMobGwNtfyGtpPriServIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriServIndex.setStatus("current")
_TmnxMobGwNtfyGtpPriServAddrType_Type = InetAddressType
_TmnxMobGwNtfyGtpPriServAddrType_Object = MibScalar
tmnxMobGwNtfyGtpPriServAddrType = _TmnxMobGwNtfyGtpPriServAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 26),
    _TmnxMobGwNtfyGtpPriServAddrType_Type()
)
tmnxMobGwNtfyGtpPriServAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriServAddrType.setStatus("current")


class _TmnxMobGwNtfyGtpPriServAddr_Type(InetAddress):
    """Custom type tmnxMobGwNtfyGtpPriServAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxMobGwNtfyGtpPriServAddr_Type.__name__ = "InetAddress"
_TmnxMobGwNtfyGtpPriServAddr_Object = MibScalar
tmnxMobGwNtfyGtpPriServAddr = _TmnxMobGwNtfyGtpPriServAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 27),
    _TmnxMobGwNtfyGtpPriServAddr_Type()
)
tmnxMobGwNtfyGtpPriServAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriServAddr.setStatus("current")
_TmnxMobGwNtfyGtpPriServPort_Type = InetPortNumber
_TmnxMobGwNtfyGtpPriServPort_Object = MibScalar
tmnxMobGwNtfyGtpPriServPort = _TmnxMobGwNtfyGtpPriServPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 28),
    _TmnxMobGwNtfyGtpPriServPort_Type()
)
tmnxMobGwNtfyGtpPriServPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriServPort.setStatus("current")
_TmnxMobGwNtfyNewGtpPriServIndex_Type = Unsigned32
_TmnxMobGwNtfyNewGtpPriServIndex_Object = MibScalar
tmnxMobGwNtfyNewGtpPriServIndex = _TmnxMobGwNtfyNewGtpPriServIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 29),
    _TmnxMobGwNtfyNewGtpPriServIndex_Type()
)
tmnxMobGwNtfyNewGtpPriServIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyNewGtpPriServIndex.setStatus("current")
_TmnxMobGwNtfyNewGtpPriSrvAdrType_Type = InetAddressType
_TmnxMobGwNtfyNewGtpPriSrvAdrType_Object = MibScalar
tmnxMobGwNtfyNewGtpPriSrvAdrType = _TmnxMobGwNtfyNewGtpPriSrvAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 30),
    _TmnxMobGwNtfyNewGtpPriSrvAdrType_Type()
)
tmnxMobGwNtfyNewGtpPriSrvAdrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyNewGtpPriSrvAdrType.setStatus("current")


class _TmnxMobGwNtfyNewGtpPriServAddr_Type(InetAddress):
    """Custom type tmnxMobGwNtfyNewGtpPriServAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxMobGwNtfyNewGtpPriServAddr_Type.__name__ = "InetAddress"
_TmnxMobGwNtfyNewGtpPriServAddr_Object = MibScalar
tmnxMobGwNtfyNewGtpPriServAddr = _TmnxMobGwNtfyNewGtpPriServAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 31),
    _TmnxMobGwNtfyNewGtpPriServAddr_Type()
)
tmnxMobGwNtfyNewGtpPriServAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyNewGtpPriServAddr.setStatus("current")
_TmnxMobGwNtfyNewGtpPriServPort_Type = InetPortNumber
_TmnxMobGwNtfyNewGtpPriServPort_Object = MibScalar
tmnxMobGwNtfyNewGtpPriServPort = _TmnxMobGwNtfyNewGtpPriServPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 32),
    _TmnxMobGwNtfyNewGtpPriServPort_Type()
)
tmnxMobGwNtfyNewGtpPriServPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyNewGtpPriServPort.setStatus("current")
_TmnxMobGwNtfyRadGrpName_Type = TmnxMobProfName
_TmnxMobGwNtfyRadGrpName_Object = MibScalar
tmnxMobGwNtfyRadGrpName = _TmnxMobGwNtfyRadGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 33),
    _TmnxMobGwNtfyRadGrpName_Type()
)
tmnxMobGwNtfyRadGrpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRadGrpName.setStatus("current")
_TmnxMobGwNtfyRadPeerIndex_Type = Unsigned32
_TmnxMobGwNtfyRadPeerIndex_Object = MibScalar
tmnxMobGwNtfyRadPeerIndex = _TmnxMobGwNtfyRadPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 34),
    _TmnxMobGwNtfyRadPeerIndex_Type()
)
tmnxMobGwNtfyRadPeerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRadPeerIndex.setStatus("current")
_TmnxMobGwNtfyRadPeerAddrType_Type = InetAddressType
_TmnxMobGwNtfyRadPeerAddrType_Object = MibScalar
tmnxMobGwNtfyRadPeerAddrType = _TmnxMobGwNtfyRadPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 35),
    _TmnxMobGwNtfyRadPeerAddrType_Type()
)
tmnxMobGwNtfyRadPeerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRadPeerAddrType.setStatus("current")


class _TmnxMobGwNtfyRadPeerAddr_Type(InetAddress):
    """Custom type tmnxMobGwNtfyRadPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxMobGwNtfyRadPeerAddr_Type.__name__ = "InetAddress"
_TmnxMobGwNtfyRadPeerAddr_Object = MibScalar
tmnxMobGwNtfyRadPeerAddr = _TmnxMobGwNtfyRadPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 36),
    _TmnxMobGwNtfyRadPeerAddr_Type()
)
tmnxMobGwNtfyRadPeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRadPeerAddr.setStatus("current")
_TmnxMobGwNtfyRadPeerAuthPort_Type = InetPortNumber
_TmnxMobGwNtfyRadPeerAuthPort_Object = MibScalar
tmnxMobGwNtfyRadPeerAuthPort = _TmnxMobGwNtfyRadPeerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 37),
    _TmnxMobGwNtfyRadPeerAuthPort_Type()
)
tmnxMobGwNtfyRadPeerAuthPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRadPeerAuthPort.setStatus("current")


class _TmnxMobGwNtfyGtpPriServerState_Type(Integer32):
    """Custom type tmnxMobGwNtfyGtpPriServerState based on Integer32"""
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
        *(("pathUp", 1),
          ("pathDown", 2),
          ("added", 3),
          ("deleted", 4))
    )


_TmnxMobGwNtfyGtpPriServerState_Type.__name__ = "Integer32"
_TmnxMobGwNtfyGtpPriServerState_Object = MibScalar
tmnxMobGwNtfyGtpPriServerState = _TmnxMobGwNtfyGtpPriServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 38),
    _TmnxMobGwNtfyGtpPriServerState_Type()
)
tmnxMobGwNtfyGtpPriServerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriServerState.setStatus("current")


class _TmnxMobGwNtfyGtpPriSvrReasonCode_Type(Integer32):
    """Custom type tmnxMobGwNtfyGtpPriSvrReasonCode based on Integer32"""
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
        *(("none", 1),
          ("unknown", 2),
          ("shutdown", 3),
          ("remoteDisc", 4),
          ("localDisc", 5),
          ("peerActive", 6),
          ("peerIdle", 7))
    )


_TmnxMobGwNtfyGtpPriSvrReasonCode_Type.__name__ = "Integer32"
_TmnxMobGwNtfyGtpPriSvrReasonCode_Object = MibScalar
tmnxMobGwNtfyGtpPriSvrReasonCode = _TmnxMobGwNtfyGtpPriSvrReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 39),
    _TmnxMobGwNtfyGtpPriSvrReasonCode_Type()
)
tmnxMobGwNtfyGtpPriSvrReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriSvrReasonCode.setStatus("current")


class _TmnxMobGwNtfyGtpPriGrpState_Type(Integer32):
    """Custom type tmnxMobGwNtfyGtpPriGrpState based on Integer32"""
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


_TmnxMobGwNtfyGtpPriGrpState_Type.__name__ = "Integer32"
_TmnxMobGwNtfyGtpPriGrpState_Object = MibScalar
tmnxMobGwNtfyGtpPriGrpState = _TmnxMobGwNtfyGtpPriGrpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 40),
    _TmnxMobGwNtfyGtpPriGrpState_Type()
)
tmnxMobGwNtfyGtpPriGrpState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriGrpState.setStatus("current")


class _TmnxMobGwNtfyGtpPriGrpReasonCode_Type(Integer32):
    """Custom type tmnxMobGwNtfyGtpPriGrpReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteDisc", 1),
          ("localDisc", 2))
    )


_TmnxMobGwNtfyGtpPriGrpReasonCode_Type.__name__ = "Integer32"
_TmnxMobGwNtfyGtpPriGrpReasonCode_Object = MibScalar
tmnxMobGwNtfyGtpPriGrpReasonCode = _TmnxMobGwNtfyGtpPriGrpReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 41),
    _TmnxMobGwNtfyGtpPriGrpReasonCode_Type()
)
tmnxMobGwNtfyGtpPriGrpReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyGtpPriGrpReasonCode.setStatus("current")


class _TmnxMobGwNtfySysGroupId_Type(Unsigned32):
    """Custom type tmnxMobGwNtfySysGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMobGwNtfySysGroupId_Type.__name__ = "Unsigned32"
_TmnxMobGwNtfySysGroupId_Object = MibScalar
tmnxMobGwNtfySysGroupId = _TmnxMobGwNtfySysGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 42),
    _TmnxMobGwNtfySysGroupId_Type()
)
tmnxMobGwNtfySysGroupId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfySysGroupId.setStatus("current")


class _TmnxMobGwNtfyWriteCdrAction_Type(Integer32):
    """Custom type tmnxMobGwNtfyWriteCdrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_TmnxMobGwNtfyWriteCdrAction_Type.__name__ = "Integer32"
_TmnxMobGwNtfyWriteCdrAction_Object = MibScalar
tmnxMobGwNtfyWriteCdrAction = _TmnxMobGwNtfyWriteCdrAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 43),
    _TmnxMobGwNtfyWriteCdrAction_Type()
)
tmnxMobGwNtfyWriteCdrAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyWriteCdrAction.setStatus("current")
_TmnxMobGwNtfyRadPeerAcctPort_Type = InetPortNumber
_TmnxMobGwNtfyRadPeerAcctPort_Object = MibScalar
tmnxMobGwNtfyRadPeerAcctPort = _TmnxMobGwNtfyRadPeerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 44),
    _TmnxMobGwNtfyRadPeerAcctPort_Type()
)
tmnxMobGwNtfyRadPeerAcctPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRadPeerAcctPort.setStatus("current")


class _TmnxMobGwNtfyRadPeerState_Type(Integer32):
    """Custom type tmnxMobGwNtfyRadPeerState based on Integer32"""
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


_TmnxMobGwNtfyRadPeerState_Type.__name__ = "Integer32"
_TmnxMobGwNtfyRadPeerState_Object = MibScalar
tmnxMobGwNtfyRadPeerState = _TmnxMobGwNtfyRadPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 45),
    _TmnxMobGwNtfyRadPeerState_Type()
)
tmnxMobGwNtfyRadPeerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRadPeerState.setStatus("current")


class _TmnxMobGwNtfyRadGrpState_Type(Integer32):
    """Custom type tmnxMobGwNtfyRadGrpState based on Integer32"""
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


_TmnxMobGwNtfyRadGrpState_Type.__name__ = "Integer32"
_TmnxMobGwNtfyRadGrpState_Object = MibScalar
tmnxMobGwNtfyRadGrpState = _TmnxMobGwNtfyRadGrpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 3, 46),
    _TmnxMobGwNtfyRadGrpState_Type()
)
tmnxMobGwNtfyRadGrpState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMobGwNtfyRadGrpState.setStatus("current")
_TmnxMobGatewayChargingRecObjs_ObjectIdentity = ObjectIdentity
tmnxMobGatewayChargingRecObjs = _TmnxMobGatewayChargingRecObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 70, 4)
)
_TmnxMobGatewayNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMobGatewayNotifyPrefix = _TmnxMobGatewayNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70)
)
_TmnxMobGatewayNotifications_ObjectIdentity = ObjectIdentity
tmnxMobGatewayNotifications = _TmnxMobGatewayNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0)
)
tmnxMobGwS5StatEntry.registerAugmentions(
    ("TIMETRA-MOBILE-GATEWAY-MIB",
     "tmnxMobGwS5CauseCodeEntry")
)
tmnxMobGwS5CauseCodeEntry.setIndexNames(*tmnxMobGwS5StatEntry.getIndexNames())

# Managed Objects groups

tmnxMobGatewayGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 1)
)
tmnxMobGatewayGlobalGroup.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwTableLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupTblLstChgd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupCardTblLstChgd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerTableLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerTableLastChngd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDfPeerTableLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTargetTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayGlobalGroup.setStatus("current")

tmnxMobGatewayCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 2)
)
tmnxMobGatewayCommonGroup.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRowStatus"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRestartCounter"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayCommonGroup.setStatus("current")

tmnxMobGatewaySystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 3)
)
tmnxMobGatewaySystemGroup.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupRowStatus"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupOperState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupApp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupRed"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupSysLimitName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupGateway"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupCardRowStatus"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupCardLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupCardRole"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysLimitName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupSwitchoverCount"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupSwitchoverTime"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupProtectDelay"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupCardRedState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupRedState"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewaySystemGroup.setStatus("current")

tmnxMobGatewayRefPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 4)
)
tmnxMobGatewayRefPointGroup.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerCreateTime"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerPathMgmtState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateSessnReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateSessnResp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteSessnReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteSessnResp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxEchoRequests"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatTxEchoResponses"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatTxEchoRequests"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxEchoResponses"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxMalformedPkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxUnknownPkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxMissingIePkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatPeerRestarts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatPeerRestrtCount"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatPathMgmtFails"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUpdateBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUpdateBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerCreateTime"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerPathMgmtState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerDetailState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxCer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxCea"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxDpr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxDpa"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxDwr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxDwa"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatConnAttempts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatConnFailures"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxTransportDisc"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxMsgUnexpectVer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxMsgTooBig"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxMsgTooSmall"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxInvalidCea"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxMsgs"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxMsgs"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxRetransmitMsgs"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrStart"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrInterim"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrStop"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrStartFails"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrInterimFail"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrStopFails"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatDefBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatDedctdBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRoamers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatBearersIpv4"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatBearersIpv6"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatBearersIpv4v6"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatActiveBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatIdleBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearersIpv4"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearersIpv6"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearerIpv4v6"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDedctdBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUlBytes"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDlBytes"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUlPackets"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDlPackets"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDefBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRoamers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatActiveBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatIdleBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearrCmd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearrFlr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearrCmd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearrFlr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearrResCmd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearrResFailInd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatSuspNoticeReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatSuspNoticeAck"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatResumeNoticeReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatResumeNoticeAck"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxDpr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxDpa"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxDwr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxDwa"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayRefPointGroup.setStatus("obsolete")

tmnxMobGatewayNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 5)
)
tmnxMobGatewayNotifyObjsGroup.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRefPointProtocol"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRfPtPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRfPtPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRfPtPeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyPathMgmtPeerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiameterPeerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiameterReasonCode"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyChrgRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyPriCdfDiaPeer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfySecCdfDiaPeer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyCdfDiaPeer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyFlashId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyCfLimit"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyAcrFailureType"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayNotifyObjsGroup.setStatus("current")

tmnxMobGatewayUnsupportedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 7)
)
tmnxMobGatewayUnsupportedGroup.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwDescription"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupDescription"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreatePbu"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreatePba"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeletePbu"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeletePba"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBri"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBra"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayUnsupportedGroup.setStatus("current")

tmnxMobGatewayLiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 8)
)
tmnxMobGatewayLiGroup.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDfPeerRowStatus"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDfPeerLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf2PeerAddressType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf2PeerAddress"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf2PeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf3PeerAddressType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf3PeerAddress"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf3PeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf2OperState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf2PeerPktsTx"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTargetRowStatus"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTargetLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTargetInterceptType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTargetDfPeer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiX3Transport"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiLocalInterfaceType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiLocalInterface"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTotalTargets"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTotalPeers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTotalIRITargets"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTotalIRICCTargets"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf3OperState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf3PeerPktsTx"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiTotalTargetPerPeer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiVprnId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobTargetLiId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiULICVersion"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiULIChangeReporting"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiOperatorId"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayLiGroup.setStatus("current")

tmnxMobGatewayNotifyObjsV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 10)
)
tmnxMobGatewayNotifyObjsV3Group.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyNewGtpPriServAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyNewGtpPriServIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyNewGtpPriServPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyNewGtpPriSrvAdrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAuthPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAcctPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadGrpState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpReasonCode"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriSvrReasonCode"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfySysGroupId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyWriteCdrAction"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayNotifyObjsV3Group.setStatus("current")

tmnxMobGatewayGlobalV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 11)
)
tmnxMobGatewayGlobalV3Group.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresGroupLastChgd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresConfigLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayGlobalV3Group.setStatus("current")

tmnxMobGatewayThresV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 12)
)
tmnxMobGatewayThresV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresGrpRowStatus"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresGrpLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresGrpAdminState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresGrpInterval"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgRowStatus"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgGroupId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgSubGroupId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgAlarmIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgHighThreshold"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgLowThreshold"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobThresCfgCtrOID"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobMgIsmThresLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobMgIsmThresCpu"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobMgIsmThresMem"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobMgIsmThresThrptUL"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobMgIsmThresThrptDL"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayThresV3v0Group.setStatus("current")

tmnxMobGatewayRefPointV3v5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 13)
)
tmnxMobGatewayRefPointV3v5Group.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerTableLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerCreateTime"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerPathMgmtState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8PeerType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatCreateSessnReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatCreateSessnResp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatDeleteSessnReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatDeleteSessnResp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatCreateBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatCreateBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatDeleteBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatDeleteBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatModifyBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatModifyBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatRxEchoRequests"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatTxEchoResponses"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatTxEchoRequests"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatRxEchoResponses"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatRxMalformedPkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatRxUnknownPkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatRxMissingIePkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatCreatePbu"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatCreatePba"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatDeletePbu"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatDeletePba"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatBri"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatBra"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatPeerRestarts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatPeerRestrtCount"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatPathMgmtFails"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatUpdateBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatUpdateBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatCreatSessnRspFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatDelSessnRspFail"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatCreatBearrRspFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatDelBearrRspFail"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatModBearrRspFail"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS8StatUpdatBearrRspFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateSessnRespFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteSessnRespFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateBearerRspFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearerRspFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearerRspFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUpdateBearerRspFl"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxReqAccepted"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxCtxNotFound"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxInvalidLength"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxMndIeIncorrect"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxMandIeMissing"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxReqRejected"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxRemPeerNoResp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxNoResAvailable"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxUsrAuthFailure"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcRxOthers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxReqAccepted"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxCtxNotFound"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxInvalidLength"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxMndIeIncorrect"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxMandIeMissing"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxReqRejected"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxRemPeerNoResp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxNoResAvailable"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxUsrAuthFailure"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5CcTxOthers"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayRefPointV3v5Group.setStatus("current")

tmnxMobGatewayObsoletedGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 14)
)
tmnxMobGatewayObsoletedGroups.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearersIpv4"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearersIpv6"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearerIpv4v6"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDedctdBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDefBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRoamers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatActiveBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatIdleBearers"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayObsoletedGroups.setStatus("current")

tmnxMobGatewayRefPointGroupV31v2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 15)
)
tmnxMobGatewayRefPointGroupV31v2.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerCreateTime"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerPathMgmtState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5PeerType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateSessnReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateSessnResp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteSessnReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteSessnResp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatCreateBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxEchoRequests"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatTxEchoResponses"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatTxEchoRequests"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxEchoResponses"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxMalformedPkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxUnknownPkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatRxMissingIePkts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatPeerRestarts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatPeerRestrtCount"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatPathMgmtFails"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUpdateBearerReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUpdateBearerRsp"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerLastChanged"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerCreateTime"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerPathMgmtState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfPeerDetailState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxCer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxCea"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxDpr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxDpa"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxDwr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxDwa"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatConnAttempts"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatConnFailures"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxTransportDisc"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxMsgUnexpectVer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxMsgTooBig"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxMsgTooSmall"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxInvalidCea"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxMsgs"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxMsgs"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxRetransmitMsgs"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrStart"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrInterim"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrStop"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrStartFails"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrInterimFail"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxAcrStopFails"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatDefBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatDedctdBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRoamers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatBearersIpv4"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatBearersIpv6"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatBearersIpv4v6"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatActiveBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatIdleBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUlBytes"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDlBytes"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatUlPackets"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDlPackets"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearers"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearrCmd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatModifyBearrFlr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearrCmd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatDeleteBearrFlr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearrResCmd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatBearrResFailInd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatSuspNoticeReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatSuspNoticeAck"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatResumeNoticeReq"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwS5StatResumeNoticeAck"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxDpr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxDpa"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatRxDwr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRfStatTxDwa"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayRefPointGroupV31v2.setStatus("current")


# Notification objects

tmnxMobGwPathMgmtPeerState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 1)
)
tmnxMobGwPathMgmtPeerState.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRefPointProtocol"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRfPtPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRfPtPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRfPtPeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyPathMgmtPeerState"))
)
if mibBuilder.loadTexts:
    tmnxMobGwPathMgmtPeerState.setStatus(
        "current"
    )

tmnxMobGwDiameterPeerState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 2)
)
tmnxMobGwDiameterPeerState.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiameterPeerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiameterReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxMobGwDiameterPeerState.setStatus(
        "current"
    )

tmnxMobGwAcrFailuresAlarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 3)
)
tmnxMobGwAcrFailuresAlarmMajor.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyChrgRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyAcrFailureType"))
)
if mibBuilder.loadTexts:
    tmnxMobGwAcrFailuresAlarmMajor.setStatus(
        "current"
    )

tmnxMobGwCdfDownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 4)
)
tmnxMobGwCdfDownAlarm.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyPriCdfDiaPeer"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfySecCdfDiaPeer"))
)
if mibBuilder.loadTexts:
    tmnxMobGwCdfDownAlarm.setStatus(
        "current"
    )

tmnxMobGwCdfDownAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 5)
)
tmnxMobGwCdfDownAlarmCleared.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyCdfDiaPeer"))
)
if mibBuilder.loadTexts:
    tmnxMobGwCdfDownAlarmCleared.setStatus(
        "current"
    )

tmnxMobGwAcrFailuresAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 6)
)
tmnxMobGwAcrFailuresAlarmClear.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyChrgRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyAcrFailureType"))
)
if mibBuilder.loadTexts:
    tmnxMobGwAcrFailuresAlarmClear.setStatus(
        "current"
    )

tmnxMobGwCfCapacityAlarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 7)
)
tmnxMobGwCfCapacityAlarmMinor.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyChrgRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyFlashId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyCfLimit"))
)
if mibBuilder.loadTexts:
    tmnxMobGwCfCapacityAlarmMinor.setStatus(
        "current"
    )

tmnxMobGwCfCapacityAlmMnrClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 8)
)
tmnxMobGwCfCapacityAlmMnrClear.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyChrgRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyFlashId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyCfLimit"))
)
if mibBuilder.loadTexts:
    tmnxMobGwCfCapacityAlmMnrClear.setStatus(
        "current"
    )

tmnxMobGwCfCapacityAlarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 9)
)
tmnxMobGwCfCapacityAlarmMajor.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyChrgRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyFlashId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyCfLimit"))
)
if mibBuilder.loadTexts:
    tmnxMobGwCfCapacityAlarmMajor.setStatus(
        "current"
    )

tmnxMobGwCfCapacityAlmMjrClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 10)
)
tmnxMobGwCfCapacityAlmMjrClear.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyChrgRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyFlashId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyCfLimit"))
)
if mibBuilder.loadTexts:
    tmnxMobGwCfCapacityAlmMjrClear.setStatus(
        "current"
    )

tmnxMobGwSysGrpRedStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 11)
)
tmnxMobGwSysGrpRedStateChange.setObjects(
    ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupRedState")
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGrpRedStateChange.setStatus(
        "current"
    )

tmnxMobGwSysGrpCardRedStChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 12)
)
tmnxMobGwSysGrpCardRedStChange.setObjects(
    ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGroupCardRedState")
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGrpCardRedStChange.setStatus(
        "current"
    )

tmnxMobGwGtpPriServFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 13)
)
tmnxMobGwGtpPriServFailAlarm.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServPort"))
)
if mibBuilder.loadTexts:
    tmnxMobGwGtpPriServFailAlarm.setStatus(
        "current"
    )

tmnxMobGwGtpPriServFailAlarmClrd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 14)
)
tmnxMobGwGtpPriServFailAlarmClrd.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServPort"))
)
if mibBuilder.loadTexts:
    tmnxMobGwGtpPriServFailAlarmClrd.setStatus(
        "current"
    )

tmnxMobGwGtpPriSrvSwitchoverSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 15)
)
tmnxMobGwGtpPriSrvSwitchoverSucc.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyNewGtpPriServIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyNewGtpPriSrvAdrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyNewGtpPriServAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyNewGtpPriServPort"))
)
if mibBuilder.loadTexts:
    tmnxMobGwGtpPriSrvSwitchoverSucc.setStatus(
        "current"
    )

tmnxMobGwGtpPriGrpFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 16)
)
tmnxMobGwGtpPriGrpFailAlarm.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpName"))
)
if mibBuilder.loadTexts:
    tmnxMobGwGtpPriGrpFailAlarm.setStatus(
        "current"
    )

tmnxMobGwGtpPriGrpFailAlarmClrd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 17)
)
tmnxMobGwGtpPriGrpFailAlarmClrd.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpName"))
)
if mibBuilder.loadTexts:
    tmnxMobGwGtpPriGrpFailAlarmClrd.setStatus(
        "current"
    )

tmnxMobGwRadPeerFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 18)
)
tmnxMobGwRadPeerFailAlarm.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAuthPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAcctPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerState"))
)
if mibBuilder.loadTexts:
    tmnxMobGwRadPeerFailAlarm.setStatus(
        "current"
    )

tmnxMobGwRadPeerFailAlarmClrd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 19)
)
tmnxMobGwRadPeerFailAlarmClrd.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAuthPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerAcctPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadPeerState"))
)
if mibBuilder.loadTexts:
    tmnxMobGwRadPeerFailAlarmClrd.setStatus(
        "current"
    )

tmnxMobGwRadGrpFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 20)
)
tmnxMobGwRadGrpFailAlarm.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadGrpState"))
)
if mibBuilder.loadTexts:
    tmnxMobGwRadGrpFailAlarm.setStatus(
        "current"
    )

tmnxMobGwRadGrpFailAlarmClrd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 21)
)
tmnxMobGwRadGrpFailAlarmClrd.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyVrtrId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyRadGrpState"))
)
if mibBuilder.loadTexts:
    tmnxMobGwRadGrpFailAlarmClrd.setStatus(
        "current"
    )

tmnxMobLiDf2OperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 22)
)
tmnxMobLiDf2OperStateChange.setObjects(
    ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf2OperState")
)
if mibBuilder.loadTexts:
    tmnxMobLiDf2OperStateChange.setStatus(
        "current"
    )

tmnxMobGwGtpPriServerState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 23)
)
tmnxMobGwGtpPriServerState.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerAddrType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerAddr"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriSvrReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxMobGwGtpPriServerState.setStatus(
        "current"
    )

tmnxMobGwSysGrpGtpPriServerState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 24)
)
tmnxMobGwSysGrpGtpPriServerState.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfySysGroupId"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerAddrType"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerAddr"),
        ("TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriServerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriSvrReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGrpGtpPriServerState.setStatus(
        "current"
    )

tmnxMobGwGtpPriSrvGrpState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 25)
)
tmnxMobGwGtpPriSrvGrpState.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxMobGwGtpPriSrvGrpState.setStatus(
        "current"
    )

tmnxMobGwSysGrpGtpPriSrvGrpState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 26)
)
tmnxMobGwSysGrpGtpPriSrvGrpState.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfySysGroupId"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGtpPriGrpReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGrpGtpPriSrvGrpState.setStatus(
        "current"
    )

tmnxMobGwSysGrpWriteCdrToCfAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 27)
)
tmnxMobGwSysGrpWriteCdrToCfAlarm.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfySysGroupId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyWriteCdrAction"))
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGrpWriteCdrToCfAlarm.setStatus(
        "current"
    )

tmnxMobGwSysGrpDiameterPeerState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 70, 0, 28)
)
tmnxMobGwSysGrpDiameterPeerState.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyGatewayId"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaRefPointType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfySysGroupId"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerName"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerIndex"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddrType"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerAddr"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiaPeerPort"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiameterPeerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwNtfyDiameterReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxMobGwSysGrpDiameterPeerState.setStatus(
        "current"
    )


# Notifications groups

tmnxMobGatewayNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 6)
)
tmnxMobGatewayNotificationsGroup.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwPathMgmtPeerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwDiameterPeerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwAcrFailuresAlarmMajor"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwCdfDownAlarm"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwCdfDownAlarmCleared"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwAcrFailuresAlarmClear"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwCfCapacityAlarmMinor"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwCfCapacityAlmMnrClear"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwCfCapacityAlarmMajor"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwCfCapacityAlmMjrClear"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGrpRedStateChange"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGrpCardRedStChange"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayNotificationsGroup.setStatus(
        "current"
    )

tmnxMobGatewayNotifyV3Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 2, 9)
)
tmnxMobGatewayNotifyV3Group.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwGtpPriServFailAlarm"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwGtpPriServFailAlarmClrd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwGtpPriSrvSwitchoverSucc"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwGtpPriGrpFailAlarm"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwGtpPriGrpFailAlarmClrd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRadGrpFailAlarm"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRadGrpFailAlarmClrd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRadPeerFailAlarm"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwRadPeerFailAlarmClrd"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobLiDf2OperStateChange"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwGtpPriServerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwGtpPriSrvGrpState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGrpGtpPriServerState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGrpGtpPriSrvGrpState"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGrpWriteCdrToCfAlarm"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwSysGrpDiameterPeerState"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayNotifyV3Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMobGatewayV1v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 1, 1)
)
tmnxMobGatewayV1v0Compliance.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayGlobalGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayCommonGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewaySystemGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayRefPointGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotifyObjsGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotificationsGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayLiGroup"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayV1v0Compliance.setStatus(
        "obsolete"
    )

tmnxMobGatewayV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 1, 2)
)
tmnxMobGatewayV3v0Compliance.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayGlobalGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayCommonGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewaySystemGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayRefPointGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotifyObjsGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotificationsGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayLiGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotifyV3Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotifyObjsV3Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayGlobalV3Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayThresV3v0Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayRefPointV3v5Group"))
)
if mibBuilder.loadTexts:
    tmnxMobGatewayV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxMobGateway7xxxV10v0Compl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 70, 1, 3)
)
tmnxMobGateway7xxxV10v0Compl.setObjects(
      *(("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayCommonGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayGlobalGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayGlobalV3Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayLiGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayRefPointGroupV31v2"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayRefPointV3v5Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewaySystemGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayThresV3v0Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotificationsGroup"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotifyV3Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayNotifyObjsV3Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayGlobalV3Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayThresV3v0Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayRefPointV3v5Group"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayRefPointGroupV31v2"),
        ("TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGatewayUnsupportedGroup"))
)
if mibBuilder.loadTexts:
    tmnxMobGateway7xxxV10v0Compl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MOBILE-GATEWAY-MIB",
    **{"timetraMobGatewayMIBModule": timetraMobGatewayMIBModule,
       "tmnxMobGatewayConformance": tmnxMobGatewayConformance,
       "tmnxMobGatewayCompliances": tmnxMobGatewayCompliances,
       "tmnxMobGatewayV1v0Compliance": tmnxMobGatewayV1v0Compliance,
       "tmnxMobGatewayV3v0Compliance": tmnxMobGatewayV3v0Compliance,
       "tmnxMobGateway7xxxV10v0Compl": tmnxMobGateway7xxxV10v0Compl,
       "tmnxMobGatewayGroups": tmnxMobGatewayGroups,
       "tmnxMobGatewayGlobalGroup": tmnxMobGatewayGlobalGroup,
       "tmnxMobGatewayCommonGroup": tmnxMobGatewayCommonGroup,
       "tmnxMobGatewaySystemGroup": tmnxMobGatewaySystemGroup,
       "tmnxMobGatewayRefPointGroup": tmnxMobGatewayRefPointGroup,
       "tmnxMobGatewayNotifyObjsGroup": tmnxMobGatewayNotifyObjsGroup,
       "tmnxMobGatewayNotificationsGroup": tmnxMobGatewayNotificationsGroup,
       "tmnxMobGatewayUnsupportedGroup": tmnxMobGatewayUnsupportedGroup,
       "tmnxMobGatewayLiGroup": tmnxMobGatewayLiGroup,
       "tmnxMobGatewayNotifyV3Group": tmnxMobGatewayNotifyV3Group,
       "tmnxMobGatewayNotifyObjsV3Group": tmnxMobGatewayNotifyObjsV3Group,
       "tmnxMobGatewayGlobalV3Group": tmnxMobGatewayGlobalV3Group,
       "tmnxMobGatewayThresV3v0Group": tmnxMobGatewayThresV3v0Group,
       "tmnxMobGatewayRefPointV3v5Group": tmnxMobGatewayRefPointV3v5Group,
       "tmnxMobGatewayObsoletedGroups": tmnxMobGatewayObsoletedGroups,
       "tmnxMobGatewayRefPointGroupV31v2": tmnxMobGatewayRefPointGroupV31v2,
       "tmnxMobGateway": tmnxMobGateway,
       "tmnxMobGatewayObjs": tmnxMobGatewayObjs,
       "tmnxMobGwTable": tmnxMobGwTable,
       "tmnxMobGwEntry": tmnxMobGwEntry,
       "tmnxMobGwId": tmnxMobGwId,
       "tmnxMobGwRowStatus": tmnxMobGwRowStatus,
       "tmnxMobGwLastChanged": tmnxMobGwLastChanged,
       "tmnxMobGwDescription": tmnxMobGwDescription,
       "tmnxMobGwType": tmnxMobGwType,
       "tmnxMobGwRestartCounter": tmnxMobGwRestartCounter,
       "tmnxMobGwSysGroupTable": tmnxMobGwSysGroupTable,
       "tmnxMobGwSysGroupEntry": tmnxMobGwSysGroupEntry,
       "tmnxMobGwSysGroupId": tmnxMobGwSysGroupId,
       "tmnxMobGwSysGroupRowStatus": tmnxMobGwSysGroupRowStatus,
       "tmnxMobGwSysGroupLastChanged": tmnxMobGwSysGroupLastChanged,
       "tmnxMobGwSysGroupDescription": tmnxMobGwSysGroupDescription,
       "tmnxMobGwSysGroupOperState": tmnxMobGwSysGroupOperState,
       "tmnxMobGwSysGroupApp": tmnxMobGwSysGroupApp,
       "tmnxMobGwSysGroupRed": tmnxMobGwSysGroupRed,
       "tmnxMobGwSysGroupGateway": tmnxMobGwSysGroupGateway,
       "tmnxMobGwSysGroupSysLimitName": tmnxMobGwSysGroupSysLimitName,
       "tmnxMobGwSysGroupProtectDelay": tmnxMobGwSysGroupProtectDelay,
       "tmnxMobGwSysGroupSwitchoverCount": tmnxMobGwSysGroupSwitchoverCount,
       "tmnxMobGwSysGroupSwitchoverTime": tmnxMobGwSysGroupSwitchoverTime,
       "tmnxMobGwSysGroupRedState": tmnxMobGwSysGroupRedState,
       "tmnxMobGwSysGroupCardTable": tmnxMobGwSysGroupCardTable,
       "tmnxMobGwSysGroupCardEntry": tmnxMobGwSysGroupCardEntry,
       "tmnxMobGwSysGroupCardRowStatus": tmnxMobGwSysGroupCardRowStatus,
       "tmnxMobGwSysGroupCardLastChanged": tmnxMobGwSysGroupCardLastChanged,
       "tmnxMobGwSysGroupCardRole": tmnxMobGwSysGroupCardRole,
       "tmnxMobGwSysGroupCardRedState": tmnxMobGwSysGroupCardRedState,
       "tmnxMobGwS5PeerTable": tmnxMobGwS5PeerTable,
       "tmnxMobGwS5PeerEntry": tmnxMobGwS5PeerEntry,
       "tmnxMobGwS5PeerAddressType": tmnxMobGwS5PeerAddressType,
       "tmnxMobGwS5PeerAddress": tmnxMobGwS5PeerAddress,
       "tmnxMobGwS5PeerPort": tmnxMobGwS5PeerPort,
       "tmnxMobGwS5PeerLastChanged": tmnxMobGwS5PeerLastChanged,
       "tmnxMobGwS5PeerCreateTime": tmnxMobGwS5PeerCreateTime,
       "tmnxMobGwS5PeerPathMgmtState": tmnxMobGwS5PeerPathMgmtState,
       "tmnxMobGwS5PeerGatewayId": tmnxMobGwS5PeerGatewayId,
       "tmnxMobGwS5PeerType": tmnxMobGwS5PeerType,
       "tmnxMobGwS5StatTable": tmnxMobGwS5StatTable,
       "tmnxMobGwS5StatEntry": tmnxMobGwS5StatEntry,
       "tmnxMobGwS5StatCreateSessnReq": tmnxMobGwS5StatCreateSessnReq,
       "tmnxMobGwS5StatCreateSessnResp": tmnxMobGwS5StatCreateSessnResp,
       "tmnxMobGwS5StatDeleteSessnReq": tmnxMobGwS5StatDeleteSessnReq,
       "tmnxMobGwS5StatDeleteSessnResp": tmnxMobGwS5StatDeleteSessnResp,
       "tmnxMobGwS5StatCreateBearerReq": tmnxMobGwS5StatCreateBearerReq,
       "tmnxMobGwS5StatCreateBearerRsp": tmnxMobGwS5StatCreateBearerRsp,
       "tmnxMobGwS5StatDeleteBearerReq": tmnxMobGwS5StatDeleteBearerReq,
       "tmnxMobGwS5StatDeleteBearerRsp": tmnxMobGwS5StatDeleteBearerRsp,
       "tmnxMobGwS5StatModifyBearerReq": tmnxMobGwS5StatModifyBearerReq,
       "tmnxMobGwS5StatModifyBearerRsp": tmnxMobGwS5StatModifyBearerRsp,
       "tmnxMobGwS5StatRxEchoRequests": tmnxMobGwS5StatRxEchoRequests,
       "tmnxMobGwS5StatTxEchoResponses": tmnxMobGwS5StatTxEchoResponses,
       "tmnxMobGwS5StatTxEchoRequests": tmnxMobGwS5StatTxEchoRequests,
       "tmnxMobGwS5StatRxEchoResponses": tmnxMobGwS5StatRxEchoResponses,
       "tmnxMobGwS5StatRxMalformedPkts": tmnxMobGwS5StatRxMalformedPkts,
       "tmnxMobGwS5StatRxUnknownPkts": tmnxMobGwS5StatRxUnknownPkts,
       "tmnxMobGwS5StatRxMissingIePkts": tmnxMobGwS5StatRxMissingIePkts,
       "tmnxMobGwS5StatCreatePbu": tmnxMobGwS5StatCreatePbu,
       "tmnxMobGwS5StatCreatePba": tmnxMobGwS5StatCreatePba,
       "tmnxMobGwS5StatDeletePbu": tmnxMobGwS5StatDeletePbu,
       "tmnxMobGwS5StatDeletePba": tmnxMobGwS5StatDeletePba,
       "tmnxMobGwS5StatBri": tmnxMobGwS5StatBri,
       "tmnxMobGwS5StatBra": tmnxMobGwS5StatBra,
       "tmnxMobGwS5StatPeerRestarts": tmnxMobGwS5StatPeerRestarts,
       "tmnxMobGwS5StatPeerRestrtCount": tmnxMobGwS5StatPeerRestrtCount,
       "tmnxMobGwS5StatPathMgmtFails": tmnxMobGwS5StatPathMgmtFails,
       "tmnxMobGwS5StatUpdateBearerReq": tmnxMobGwS5StatUpdateBearerReq,
       "tmnxMobGwS5StatUpdateBearerRsp": tmnxMobGwS5StatUpdateBearerRsp,
       "tmnxMobGwS5StatBearersIpv4": tmnxMobGwS5StatBearersIpv4,
       "tmnxMobGwS5StatBearersIpv6": tmnxMobGwS5StatBearersIpv6,
       "tmnxMobGwS5StatBearerIpv4v6": tmnxMobGwS5StatBearerIpv4v6,
       "tmnxMobGwS5StatDedctdBearers": tmnxMobGwS5StatDedctdBearers,
       "tmnxMobGwS5StatUlBytes": tmnxMobGwS5StatUlBytes,
       "tmnxMobGwS5StatDlBytes": tmnxMobGwS5StatDlBytes,
       "tmnxMobGwS5StatUlPackets": tmnxMobGwS5StatUlPackets,
       "tmnxMobGwS5StatDlPackets": tmnxMobGwS5StatDlPackets,
       "tmnxMobGwS5StatBearers": tmnxMobGwS5StatBearers,
       "tmnxMobGwS5StatDefBearers": tmnxMobGwS5StatDefBearers,
       "tmnxMobGwS5StatRoamers": tmnxMobGwS5StatRoamers,
       "tmnxMobGwS5StatActiveBearers": tmnxMobGwS5StatActiveBearers,
       "tmnxMobGwS5StatIdleBearers": tmnxMobGwS5StatIdleBearers,
       "tmnxMobGwS5StatModifyBearrCmd": tmnxMobGwS5StatModifyBearrCmd,
       "tmnxMobGwS5StatModifyBearrFlr": tmnxMobGwS5StatModifyBearrFlr,
       "tmnxMobGwS5StatDeleteBearrCmd": tmnxMobGwS5StatDeleteBearrCmd,
       "tmnxMobGwS5StatDeleteBearrFlr": tmnxMobGwS5StatDeleteBearrFlr,
       "tmnxMobGwS5StatBearrResCmd": tmnxMobGwS5StatBearrResCmd,
       "tmnxMobGwS5StatBearrResFailInd": tmnxMobGwS5StatBearrResFailInd,
       "tmnxMobGwS5StatSuspNoticeReq": tmnxMobGwS5StatSuspNoticeReq,
       "tmnxMobGwS5StatSuspNoticeAck": tmnxMobGwS5StatSuspNoticeAck,
       "tmnxMobGwS5StatResumeNoticeReq": tmnxMobGwS5StatResumeNoticeReq,
       "tmnxMobGwS5StatResumeNoticeAck": tmnxMobGwS5StatResumeNoticeAck,
       "tmnxMobGwS5StatCreateSessnRespFl": tmnxMobGwS5StatCreateSessnRespFl,
       "tmnxMobGwS5StatDeleteSessnRespFl": tmnxMobGwS5StatDeleteSessnRespFl,
       "tmnxMobGwS5StatCreateBearerRspFl": tmnxMobGwS5StatCreateBearerRspFl,
       "tmnxMobGwS5StatDeleteBearerRspFl": tmnxMobGwS5StatDeleteBearerRspFl,
       "tmnxMobGwS5StatModifyBearerRspFl": tmnxMobGwS5StatModifyBearerRspFl,
       "tmnxMobGwS5StatUpdateBearerRspFl": tmnxMobGwS5StatUpdateBearerRspFl,
       "tmnxMobGwS8PeerTable": tmnxMobGwS8PeerTable,
       "tmnxMobGwS8PeerEntry": tmnxMobGwS8PeerEntry,
       "tmnxMobGwS8PeerAddressType": tmnxMobGwS8PeerAddressType,
       "tmnxMobGwS8PeerAddress": tmnxMobGwS8PeerAddress,
       "tmnxMobGwS8PeerPort": tmnxMobGwS8PeerPort,
       "tmnxMobGwS8PeerLastChanged": tmnxMobGwS8PeerLastChanged,
       "tmnxMobGwS8PeerCreateTime": tmnxMobGwS8PeerCreateTime,
       "tmnxMobGwS8PeerPathMgmtState": tmnxMobGwS8PeerPathMgmtState,
       "tmnxMobGwS8PeerGatewayId": tmnxMobGwS8PeerGatewayId,
       "tmnxMobGwS8PeerType": tmnxMobGwS8PeerType,
       "tmnxMobGwS8StatTable": tmnxMobGwS8StatTable,
       "tmnxMobGwS8StatEntry": tmnxMobGwS8StatEntry,
       "tmnxMobGwS8StatCreateSessnReq": tmnxMobGwS8StatCreateSessnReq,
       "tmnxMobGwS8StatCreateSessnResp": tmnxMobGwS8StatCreateSessnResp,
       "tmnxMobGwS8StatDeleteSessnReq": tmnxMobGwS8StatDeleteSessnReq,
       "tmnxMobGwS8StatDeleteSessnResp": tmnxMobGwS8StatDeleteSessnResp,
       "tmnxMobGwS8StatCreateBearerReq": tmnxMobGwS8StatCreateBearerReq,
       "tmnxMobGwS8StatCreateBearerRsp": tmnxMobGwS8StatCreateBearerRsp,
       "tmnxMobGwS8StatDeleteBearerReq": tmnxMobGwS8StatDeleteBearerReq,
       "tmnxMobGwS8StatDeleteBearerRsp": tmnxMobGwS8StatDeleteBearerRsp,
       "tmnxMobGwS8StatModifyBearerReq": tmnxMobGwS8StatModifyBearerReq,
       "tmnxMobGwS8StatModifyBearerRsp": tmnxMobGwS8StatModifyBearerRsp,
       "tmnxMobGwS8StatRxEchoRequests": tmnxMobGwS8StatRxEchoRequests,
       "tmnxMobGwS8StatTxEchoResponses": tmnxMobGwS8StatTxEchoResponses,
       "tmnxMobGwS8StatTxEchoRequests": tmnxMobGwS8StatTxEchoRequests,
       "tmnxMobGwS8StatRxEchoResponses": tmnxMobGwS8StatRxEchoResponses,
       "tmnxMobGwS8StatRxMalformedPkts": tmnxMobGwS8StatRxMalformedPkts,
       "tmnxMobGwS8StatRxUnknownPkts": tmnxMobGwS8StatRxUnknownPkts,
       "tmnxMobGwS8StatRxMissingIePkts": tmnxMobGwS8StatRxMissingIePkts,
       "tmnxMobGwS8StatCreatePbu": tmnxMobGwS8StatCreatePbu,
       "tmnxMobGwS8StatCreatePba": tmnxMobGwS8StatCreatePba,
       "tmnxMobGwS8StatDeletePbu": tmnxMobGwS8StatDeletePbu,
       "tmnxMobGwS8StatDeletePba": tmnxMobGwS8StatDeletePba,
       "tmnxMobGwS8StatBri": tmnxMobGwS8StatBri,
       "tmnxMobGwS8StatBra": tmnxMobGwS8StatBra,
       "tmnxMobGwS8StatPeerRestarts": tmnxMobGwS8StatPeerRestarts,
       "tmnxMobGwS8StatPeerRestrtCount": tmnxMobGwS8StatPeerRestrtCount,
       "tmnxMobGwS8StatPathMgmtFails": tmnxMobGwS8StatPathMgmtFails,
       "tmnxMobGwS8StatUpdateBearerReq": tmnxMobGwS8StatUpdateBearerReq,
       "tmnxMobGwS8StatUpdateBearerRsp": tmnxMobGwS8StatUpdateBearerRsp,
       "tmnxMobGwS8StatCreatSessnRspFl": tmnxMobGwS8StatCreatSessnRspFl,
       "tmnxMobGwS8StatDelSessnRspFail": tmnxMobGwS8StatDelSessnRspFail,
       "tmnxMobGwS8StatCreatBearrRspFl": tmnxMobGwS8StatCreatBearrRspFl,
       "tmnxMobGwS8StatDelBearrRspFail": tmnxMobGwS8StatDelBearrRspFail,
       "tmnxMobGwS8StatModBearrRspFail": tmnxMobGwS8StatModBearrRspFail,
       "tmnxMobGwS8StatUpdatBearrRspFl": tmnxMobGwS8StatUpdatBearrRspFl,
       "tmnxMobGwRfPeerTable": tmnxMobGwRfPeerTable,
       "tmnxMobGwRfPeerEntry": tmnxMobGwRfPeerEntry,
       "tmnxMobGwRfPeerAddressType": tmnxMobGwRfPeerAddressType,
       "tmnxMobGwRfPeerAddress": tmnxMobGwRfPeerAddress,
       "tmnxMobGwRfPeerPort": tmnxMobGwRfPeerPort,
       "tmnxMobGwRfPeerLastChanged": tmnxMobGwRfPeerLastChanged,
       "tmnxMobGwRfPeerCreateTime": tmnxMobGwRfPeerCreateTime,
       "tmnxMobGwRfPeerPathMgmtState": tmnxMobGwRfPeerPathMgmtState,
       "tmnxMobGwRfPeerDetailState": tmnxMobGwRfPeerDetailState,
       "tmnxMobGwRfStatTable": tmnxMobGwRfStatTable,
       "tmnxMobGwRfStatEntry": tmnxMobGwRfStatEntry,
       "tmnxMobGwRfStatTxCer": tmnxMobGwRfStatTxCer,
       "tmnxMobGwRfStatRxCea": tmnxMobGwRfStatRxCea,
       "tmnxMobGwRfStatRxDpr": tmnxMobGwRfStatRxDpr,
       "tmnxMobGwRfStatTxDpa": tmnxMobGwRfStatTxDpa,
       "tmnxMobGwRfStatTxDwr": tmnxMobGwRfStatTxDwr,
       "tmnxMobGwRfStatRxDwa": tmnxMobGwRfStatRxDwa,
       "tmnxMobGwRfStatConnAttempts": tmnxMobGwRfStatConnAttempts,
       "tmnxMobGwRfStatConnFailures": tmnxMobGwRfStatConnFailures,
       "tmnxMobGwRfStatRxTransportDisc": tmnxMobGwRfStatRxTransportDisc,
       "tmnxMobGwRfStatRxMsgUnexpectVer": tmnxMobGwRfStatRxMsgUnexpectVer,
       "tmnxMobGwRfStatRxMsgTooBig": tmnxMobGwRfStatRxMsgTooBig,
       "tmnxMobGwRfStatRxMsgTooSmall": tmnxMobGwRfStatRxMsgTooSmall,
       "tmnxMobGwRfStatRxInvalidCea": tmnxMobGwRfStatRxInvalidCea,
       "tmnxMobGwRfStatRxMsgs": tmnxMobGwRfStatRxMsgs,
       "tmnxMobGwRfStatTxMsgs": tmnxMobGwRfStatTxMsgs,
       "tmnxMobGwRfStatTxRetransmitMsgs": tmnxMobGwRfStatTxRetransmitMsgs,
       "tmnxMobGwRfStatTxAcrStart": tmnxMobGwRfStatTxAcrStart,
       "tmnxMobGwRfStatTxAcrInterim": tmnxMobGwRfStatTxAcrInterim,
       "tmnxMobGwRfStatTxAcrStop": tmnxMobGwRfStatTxAcrStop,
       "tmnxMobGwRfStatTxAcrStartFails": tmnxMobGwRfStatTxAcrStartFails,
       "tmnxMobGwRfStatTxAcrInterimFail": tmnxMobGwRfStatTxAcrInterimFail,
       "tmnxMobGwRfStatTxAcrStopFails": tmnxMobGwRfStatTxAcrStopFails,
       "tmnxMobGwRfStatBearers": tmnxMobGwRfStatBearers,
       "tmnxMobGwRfStatDefBearers": tmnxMobGwRfStatDefBearers,
       "tmnxMobGwRfStatDedctdBearers": tmnxMobGwRfStatDedctdBearers,
       "tmnxMobGwRfStatRoamers": tmnxMobGwRfStatRoamers,
       "tmnxMobGwRfStatBearersIpv4": tmnxMobGwRfStatBearersIpv4,
       "tmnxMobGwRfStatBearersIpv6": tmnxMobGwRfStatBearersIpv6,
       "tmnxMobGwRfStatBearersIpv4v6": tmnxMobGwRfStatBearersIpv4v6,
       "tmnxMobGwRfStatActiveBearers": tmnxMobGwRfStatActiveBearers,
       "tmnxMobGwRfStatIdleBearers": tmnxMobGwRfStatIdleBearers,
       "tmnxMobGwRfStatTxDpr": tmnxMobGwRfStatTxDpr,
       "tmnxMobGwRfStatRxDpa": tmnxMobGwRfStatRxDpa,
       "tmnxMobGwRfStatRxDwr": tmnxMobGwRfStatRxDwr,
       "tmnxMobGwRfStatTxDwa": tmnxMobGwRfStatTxDwa,
       "tmnxMobLiDfPeerTable": tmnxMobLiDfPeerTable,
       "tmnxMobLiDfPeerEntry": tmnxMobLiDfPeerEntry,
       "tmnxMobLiDfPeer": tmnxMobLiDfPeer,
       "tmnxMobLiDfPeerRowStatus": tmnxMobLiDfPeerRowStatus,
       "tmnxMobLiDfPeerLastChanged": tmnxMobLiDfPeerLastChanged,
       "tmnxMobLiDf2PeerAddressType": tmnxMobLiDf2PeerAddressType,
       "tmnxMobLiDf2PeerAddress": tmnxMobLiDf2PeerAddress,
       "tmnxMobLiDf2PeerPort": tmnxMobLiDf2PeerPort,
       "tmnxMobLiDf3PeerAddressType": tmnxMobLiDf3PeerAddressType,
       "tmnxMobLiDf3PeerAddress": tmnxMobLiDf3PeerAddress,
       "tmnxMobLiDf3PeerPort": tmnxMobLiDf3PeerPort,
       "tmnxMobLiDf2OperState": tmnxMobLiDf2OperState,
       "tmnxMobLiDf2PeerPktsTx": tmnxMobLiDf2PeerPktsTx,
       "tmnxMobLiDf3OperState": tmnxMobLiDf3OperState,
       "tmnxMobLiDf3PeerPktsTx": tmnxMobLiDf3PeerPktsTx,
       "tmnxMobLiTotalTargetPerPeer": tmnxMobLiTotalTargetPerPeer,
       "tmnxMobLiTargetTable": tmnxMobLiTargetTable,
       "tmnxMobLiTargetEntry": tmnxMobLiTargetEntry,
       "tmnxMobLiTargetType": tmnxMobLiTargetType,
       "tmnxMobLiTargetId": tmnxMobLiTargetId,
       "tmnxMobLiTargetRowStatus": tmnxMobLiTargetRowStatus,
       "tmnxMobLiTargetLastChanged": tmnxMobLiTargetLastChanged,
       "tmnxMobLiTargetInterceptType": tmnxMobLiTargetInterceptType,
       "tmnxMobLiTargetDfPeer": tmnxMobLiTargetDfPeer,
       "tmnxMobTargetLiId": tmnxMobTargetLiId,
       "tmnxMobThresGroupTable": tmnxMobThresGroupTable,
       "tmnxMobThresGroupEntry": tmnxMobThresGroupEntry,
       "tmnxMobThresGrpId": tmnxMobThresGrpId,
       "tmnxMobThresSubGrpId": tmnxMobThresSubGrpId,
       "tmnxMobThresGrpRowStatus": tmnxMobThresGrpRowStatus,
       "tmnxMobThresGrpLastChanged": tmnxMobThresGrpLastChanged,
       "tmnxMobThresGrpAdminState": tmnxMobThresGrpAdminState,
       "tmnxMobThresGrpInterval": tmnxMobThresGrpInterval,
       "tmnxMobThresConfigTable": tmnxMobThresConfigTable,
       "tmnxMobThresConfigEntry": tmnxMobThresConfigEntry,
       "tmnxMobThresCfgGroupId": tmnxMobThresCfgGroupId,
       "tmnxMobThresCfgSubGroupId": tmnxMobThresCfgSubGroupId,
       "tmnxMobThresCfgCounterId": tmnxMobThresCfgCounterId,
       "tmnxMobThresCfgRowStatus": tmnxMobThresCfgRowStatus,
       "tmnxMobThresCfgLastChanged": tmnxMobThresCfgLastChanged,
       "tmnxMobThresCfgAlarmIndex": tmnxMobThresCfgAlarmIndex,
       "tmnxMobThresCfgHighThreshold": tmnxMobThresCfgHighThreshold,
       "tmnxMobThresCfgLowThreshold": tmnxMobThresCfgLowThreshold,
       "tmnxMobThresCfgCtrOID": tmnxMobThresCfgCtrOID,
       "tmnxMobMgIsmThresTable": tmnxMobMgIsmThresTable,
       "tmnxMobMgIsmThresEntry": tmnxMobMgIsmThresEntry,
       "tmnxMobMgIsmThresGroupId": tmnxMobMgIsmThresGroupId,
       "tmnxMobMgIsmThresLastChanged": tmnxMobMgIsmThresLastChanged,
       "tmnxMobMgIsmThresCpu": tmnxMobMgIsmThresCpu,
       "tmnxMobMgIsmThresMem": tmnxMobMgIsmThresMem,
       "tmnxMobMgIsmThresThrptUL": tmnxMobMgIsmThresThrptUL,
       "tmnxMobMgIsmThresThrptDL": tmnxMobMgIsmThresThrptDL,
       "tmnxMobGwS5CauseCodeTable": tmnxMobGwS5CauseCodeTable,
       "tmnxMobGwS5CauseCodeEntry": tmnxMobGwS5CauseCodeEntry,
       "tmnxMobGwS5CcRxReqAccepted": tmnxMobGwS5CcRxReqAccepted,
       "tmnxMobGwS5CcRxCtxNotFound": tmnxMobGwS5CcRxCtxNotFound,
       "tmnxMobGwS5CcRxInvalidLength": tmnxMobGwS5CcRxInvalidLength,
       "tmnxMobGwS5CcRxMndIeIncorrect": tmnxMobGwS5CcRxMndIeIncorrect,
       "tmnxMobGwS5CcRxMandIeMissing": tmnxMobGwS5CcRxMandIeMissing,
       "tmnxMobGwS5CcRxReqRejected": tmnxMobGwS5CcRxReqRejected,
       "tmnxMobGwS5CcRxRemPeerNoResp": tmnxMobGwS5CcRxRemPeerNoResp,
       "tmnxMobGwS5CcRxNoResAvailable": tmnxMobGwS5CcRxNoResAvailable,
       "tmnxMobGwS5CcRxUsrAuthFailure": tmnxMobGwS5CcRxUsrAuthFailure,
       "tmnxMobGwS5CcRxOthers": tmnxMobGwS5CcRxOthers,
       "tmnxMobGwS5CcTxReqAccepted": tmnxMobGwS5CcTxReqAccepted,
       "tmnxMobGwS5CcTxCtxNotFound": tmnxMobGwS5CcTxCtxNotFound,
       "tmnxMobGwS5CcTxInvalidLength": tmnxMobGwS5CcTxInvalidLength,
       "tmnxMobGwS5CcTxMndIeIncorrect": tmnxMobGwS5CcTxMndIeIncorrect,
       "tmnxMobGwS5CcTxMandIeMissing": tmnxMobGwS5CcTxMandIeMissing,
       "tmnxMobGwS5CcTxReqRejected": tmnxMobGwS5CcTxReqRejected,
       "tmnxMobGwS5CcTxRemPeerNoResp": tmnxMobGwS5CcTxRemPeerNoResp,
       "tmnxMobGwS5CcTxNoResAvailable": tmnxMobGwS5CcTxNoResAvailable,
       "tmnxMobGwS5CcTxUsrAuthFailure": tmnxMobGwS5CcTxUsrAuthFailure,
       "tmnxMobGwS5CcTxOthers": tmnxMobGwS5CcTxOthers,
       "tmnxMobGatewayGlobalObjs": tmnxMobGatewayGlobalObjs,
       "tmnxMobGwTableLastChanged": tmnxMobGwTableLastChanged,
       "tmnxMobGwSysGroupTblLstChgd": tmnxMobGwSysGroupTblLstChgd,
       "tmnxMobGwSysGroupCardTblLstChgd": tmnxMobGwSysGroupCardTblLstChgd,
       "tmnxMobGwSysLimitName": tmnxMobGwSysLimitName,
       "tmnxMobGwS5PeerTableLastChanged": tmnxMobGwS5PeerTableLastChanged,
       "tmnxMobGwS8PeerTableLastChanged": tmnxMobGwS8PeerTableLastChanged,
       "tmnxMobGwRfPeerTableLastChngd": tmnxMobGwRfPeerTableLastChngd,
       "tmnxMobLiDfPeerTableLastChanged": tmnxMobLiDfPeerTableLastChanged,
       "tmnxMobLiTargetTableLastChanged": tmnxMobLiTargetTableLastChanged,
       "tmnxMobThresGroupLastChgd": tmnxMobThresGroupLastChgd,
       "tmnxMobGatewayGlobalLiObjs": tmnxMobGatewayGlobalLiObjs,
       "tmnxMobLiX3Transport": tmnxMobLiX3Transport,
       "tmnxMobLiLocalInterfaceType": tmnxMobLiLocalInterfaceType,
       "tmnxMobLiLocalInterface": tmnxMobLiLocalInterface,
       "tmnxMobLiTotalTargets": tmnxMobLiTotalTargets,
       "tmnxMobLiTotalPeers": tmnxMobLiTotalPeers,
       "tmnxMobLiTotalIRITargets": tmnxMobLiTotalIRITargets,
       "tmnxMobLiTotalIRICCTargets": tmnxMobLiTotalIRICCTargets,
       "tmnxMobLiVprnId": tmnxMobLiVprnId,
       "tmnxMobLiULICVersion": tmnxMobLiULICVersion,
       "tmnxMobLiULIChangeReporting": tmnxMobLiULIChangeReporting,
       "tmnxMobLiOperatorId": tmnxMobLiOperatorId,
       "tmnxMobThresConfigLastChanged": tmnxMobThresConfigLastChanged,
       "tmnxMobGatewayNotificationObjs": tmnxMobGatewayNotificationObjs,
       "tmnxMobGwNtfyGatewayId": tmnxMobGwNtfyGatewayId,
       "tmnxMobGwNtfyVrtrId": tmnxMobGwNtfyVrtrId,
       "tmnxMobGwNtfyRefPointType": tmnxMobGwNtfyRefPointType,
       "tmnxMobGwNtfyRefPointProtocol": tmnxMobGwNtfyRefPointProtocol,
       "tmnxMobGwNtfyRfPtPeerAddrType": tmnxMobGwNtfyRfPtPeerAddrType,
       "tmnxMobGwNtfyRfPtPeerAddr": tmnxMobGwNtfyRfPtPeerAddr,
       "tmnxMobGwNtfyRfPtPeerPort": tmnxMobGwNtfyRfPtPeerPort,
       "tmnxMobGwNtfyPathMgmtPeerState": tmnxMobGwNtfyPathMgmtPeerState,
       "tmnxMobGwNtfyDiaRefPointType": tmnxMobGwNtfyDiaRefPointType,
       "tmnxMobGwNtfyDiaPeerName": tmnxMobGwNtfyDiaPeerName,
       "tmnxMobGwNtfyDiaPeerIndex": tmnxMobGwNtfyDiaPeerIndex,
       "tmnxMobGwNtfyDiaPeerAddrType": tmnxMobGwNtfyDiaPeerAddrType,
       "tmnxMobGwNtfyDiaPeerAddr": tmnxMobGwNtfyDiaPeerAddr,
       "tmnxMobGwNtfyDiaPeerPort": tmnxMobGwNtfyDiaPeerPort,
       "tmnxMobGwNtfyDiameterPeerState": tmnxMobGwNtfyDiameterPeerState,
       "tmnxMobGwNtfyDiameterReasonCode": tmnxMobGwNtfyDiameterReasonCode,
       "tmnxMobGwNtfyChrgRefPointType": tmnxMobGwNtfyChrgRefPointType,
       "tmnxMobGwNtfyPriCdfDiaPeer": tmnxMobGwNtfyPriCdfDiaPeer,
       "tmnxMobGwNtfySecCdfDiaPeer": tmnxMobGwNtfySecCdfDiaPeer,
       "tmnxMobGwNtfyCdfDiaPeer": tmnxMobGwNtfyCdfDiaPeer,
       "tmnxMobGwNtfyFlashId": tmnxMobGwNtfyFlashId,
       "tmnxMobGwNtfyCfLimit": tmnxMobGwNtfyCfLimit,
       "tmnxMobGwNtfyAcrFailureType": tmnxMobGwNtfyAcrFailureType,
       "tmnxMobGwNtfyGtpPriGrpName": tmnxMobGwNtfyGtpPriGrpName,
       "tmnxMobGwNtfyGtpPriServIndex": tmnxMobGwNtfyGtpPriServIndex,
       "tmnxMobGwNtfyGtpPriServAddrType": tmnxMobGwNtfyGtpPriServAddrType,
       "tmnxMobGwNtfyGtpPriServAddr": tmnxMobGwNtfyGtpPriServAddr,
       "tmnxMobGwNtfyGtpPriServPort": tmnxMobGwNtfyGtpPriServPort,
       "tmnxMobGwNtfyNewGtpPriServIndex": tmnxMobGwNtfyNewGtpPriServIndex,
       "tmnxMobGwNtfyNewGtpPriSrvAdrType": tmnxMobGwNtfyNewGtpPriSrvAdrType,
       "tmnxMobGwNtfyNewGtpPriServAddr": tmnxMobGwNtfyNewGtpPriServAddr,
       "tmnxMobGwNtfyNewGtpPriServPort": tmnxMobGwNtfyNewGtpPriServPort,
       "tmnxMobGwNtfyRadGrpName": tmnxMobGwNtfyRadGrpName,
       "tmnxMobGwNtfyRadPeerIndex": tmnxMobGwNtfyRadPeerIndex,
       "tmnxMobGwNtfyRadPeerAddrType": tmnxMobGwNtfyRadPeerAddrType,
       "tmnxMobGwNtfyRadPeerAddr": tmnxMobGwNtfyRadPeerAddr,
       "tmnxMobGwNtfyRadPeerAuthPort": tmnxMobGwNtfyRadPeerAuthPort,
       "tmnxMobGwNtfyGtpPriServerState": tmnxMobGwNtfyGtpPriServerState,
       "tmnxMobGwNtfyGtpPriSvrReasonCode": tmnxMobGwNtfyGtpPriSvrReasonCode,
       "tmnxMobGwNtfyGtpPriGrpState": tmnxMobGwNtfyGtpPriGrpState,
       "tmnxMobGwNtfyGtpPriGrpReasonCode": tmnxMobGwNtfyGtpPriGrpReasonCode,
       "tmnxMobGwNtfySysGroupId": tmnxMobGwNtfySysGroupId,
       "tmnxMobGwNtfyWriteCdrAction": tmnxMobGwNtfyWriteCdrAction,
       "tmnxMobGwNtfyRadPeerAcctPort": tmnxMobGwNtfyRadPeerAcctPort,
       "tmnxMobGwNtfyRadPeerState": tmnxMobGwNtfyRadPeerState,
       "tmnxMobGwNtfyRadGrpState": tmnxMobGwNtfyRadGrpState,
       "tmnxMobGatewayChargingRecObjs": tmnxMobGatewayChargingRecObjs,
       "tmnxMobGatewayNotifyPrefix": tmnxMobGatewayNotifyPrefix,
       "tmnxMobGatewayNotifications": tmnxMobGatewayNotifications,
       "tmnxMobGwPathMgmtPeerState": tmnxMobGwPathMgmtPeerState,
       "tmnxMobGwDiameterPeerState": tmnxMobGwDiameterPeerState,
       "tmnxMobGwAcrFailuresAlarmMajor": tmnxMobGwAcrFailuresAlarmMajor,
       "tmnxMobGwCdfDownAlarm": tmnxMobGwCdfDownAlarm,
       "tmnxMobGwCdfDownAlarmCleared": tmnxMobGwCdfDownAlarmCleared,
       "tmnxMobGwAcrFailuresAlarmClear": tmnxMobGwAcrFailuresAlarmClear,
       "tmnxMobGwCfCapacityAlarmMinor": tmnxMobGwCfCapacityAlarmMinor,
       "tmnxMobGwCfCapacityAlmMnrClear": tmnxMobGwCfCapacityAlmMnrClear,
       "tmnxMobGwCfCapacityAlarmMajor": tmnxMobGwCfCapacityAlarmMajor,
       "tmnxMobGwCfCapacityAlmMjrClear": tmnxMobGwCfCapacityAlmMjrClear,
       "tmnxMobGwSysGrpRedStateChange": tmnxMobGwSysGrpRedStateChange,
       "tmnxMobGwSysGrpCardRedStChange": tmnxMobGwSysGrpCardRedStChange,
       "tmnxMobGwGtpPriServFailAlarm": tmnxMobGwGtpPriServFailAlarm,
       "tmnxMobGwGtpPriServFailAlarmClrd": tmnxMobGwGtpPriServFailAlarmClrd,
       "tmnxMobGwGtpPriSrvSwitchoverSucc": tmnxMobGwGtpPriSrvSwitchoverSucc,
       "tmnxMobGwGtpPriGrpFailAlarm": tmnxMobGwGtpPriGrpFailAlarm,
       "tmnxMobGwGtpPriGrpFailAlarmClrd": tmnxMobGwGtpPriGrpFailAlarmClrd,
       "tmnxMobGwRadPeerFailAlarm": tmnxMobGwRadPeerFailAlarm,
       "tmnxMobGwRadPeerFailAlarmClrd": tmnxMobGwRadPeerFailAlarmClrd,
       "tmnxMobGwRadGrpFailAlarm": tmnxMobGwRadGrpFailAlarm,
       "tmnxMobGwRadGrpFailAlarmClrd": tmnxMobGwRadGrpFailAlarmClrd,
       "tmnxMobLiDf2OperStateChange": tmnxMobLiDf2OperStateChange,
       "tmnxMobGwGtpPriServerState": tmnxMobGwGtpPriServerState,
       "tmnxMobGwSysGrpGtpPriServerState": tmnxMobGwSysGrpGtpPriServerState,
       "tmnxMobGwGtpPriSrvGrpState": tmnxMobGwGtpPriSrvGrpState,
       "tmnxMobGwSysGrpGtpPriSrvGrpState": tmnxMobGwSysGrpGtpPriSrvGrpState,
       "tmnxMobGwSysGrpWriteCdrToCfAlarm": tmnxMobGwSysGrpWriteCdrToCfAlarm,
       "tmnxMobGwSysGrpDiameterPeerState": tmnxMobGwSysGrpDiameterPeerState}
)
