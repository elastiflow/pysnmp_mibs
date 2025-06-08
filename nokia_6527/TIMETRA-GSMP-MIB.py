# SNMP MIB module (TIMETRA-GSMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-GSMP-MIB.mib
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

(custId,
 custMultSvcSiteName,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "custId",
    "custMultSvcSiteName",
    "svcId")

(tmnxSubInfoSubIdent,
 tmnxSubProfileEntry) = mibBuilder.importSymbols(
    "TIMETRA-SUBSCRIBER-MGMT-MIB",
    "tmnxSubInfoSubIdent",
    "tmnxSubProfileEntry")

(TDSCPNameOrEmpty,
 TEgrRateModType,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRAggRateLimitOverride,
 TPIRRateOverride,
 TPrecValueOrNone,
 TRemarkType,
 TmnxAdminState,
 TmnxAncpString,
 TmnxCustId,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TDSCPNameOrEmpty",
    "TEgrRateModType",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRAggRateLimitOverride",
    "TPIRRateOverride",
    "TPrecValueOrNone",
    "TRemarkType",
    "TmnxAdminState",
    "TmnxAncpString",
    "TmnxCustId",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId")


# MODULE-IDENTITY

tmnxGsmpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 39)
)
if mibBuilder.loadTexts:
    tmnxGsmpMIBModule.setRevisions(
        ("1912-06-01 00:00",
         "1909-02-28 00:00",
         "2006-07-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxGsmpCompliance_ObjectIdentity = ObjectIdentity
tmnxGsmpCompliance = _TmnxGsmpCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39)
)
_TmnxGsmpCompliances_ObjectIdentity = ObjectIdentity
tmnxGsmpCompliances = _TmnxGsmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 1)
)
_TmnxGsmpGroups_ObjectIdentity = ObjectIdentity
tmnxGsmpGroups = _TmnxGsmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 2)
)
_TmnxGsmpObjects_ObjectIdentity = ObjectIdentity
tmnxGsmpObjects = _TmnxGsmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39)
)
_TmnxGsmpNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxGsmpNotifyObjects = _TmnxGsmpNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 1)
)
_TmnxNotifAncpString_Type = TmnxAncpString
_TmnxNotifAncpString_Object = MibScalar
tmnxNotifAncpString = _TmnxNotifAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 1, 1),
    _TmnxNotifAncpString_Type()
)
tmnxNotifAncpString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifAncpString.setStatus("current")
_TmnxNotifAncpPolicyName_Type = TNamedItem
_TmnxNotifAncpPolicyName_Object = MibScalar
tmnxNotifAncpPolicyName = _TmnxNotifAncpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 1, 2),
    _TmnxNotifAncpPolicyName_Type()
)
tmnxNotifAncpPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifAncpPolicyName.setStatus("current")
_TmnxNotifAncpPlcyActualRate_Type = Unsigned32
_TmnxNotifAncpPlcyActualRate_Object = MibScalar
tmnxNotifAncpPlcyActualRate = _TmnxNotifAncpPlcyActualRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 1, 3),
    _TmnxNotifAncpPlcyActualRate_Type()
)
tmnxNotifAncpPlcyActualRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifAncpPlcyActualRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNotifAncpPlcyActualRate.setUnits("kbps")
_TmnxAncpRejectReason_Type = DisplayString
_TmnxAncpRejectReason_Object = MibScalar
tmnxAncpRejectReason = _TmnxAncpRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 1, 4),
    _TmnxAncpRejectReason_Type()
)
tmnxAncpRejectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxAncpRejectReason.setStatus("current")
_TmnxGsmpConfigTableLastChange_Type = TimeStamp
_TmnxGsmpConfigTableLastChange_Object = MibScalar
tmnxGsmpConfigTableLastChange = _TmnxGsmpConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 2),
    _TmnxGsmpConfigTableLastChange_Type()
)
tmnxGsmpConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGsmpConfigTableLastChange.setStatus("current")
_TmnxGsmpConfigTable_Object = MibTable
tmnxGsmpConfigTable = _TmnxGsmpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 3)
)
if mibBuilder.loadTexts:
    tmnxGsmpConfigTable.setStatus("current")
_TmnxGsmpConfigEntry_Object = MibTableRow
tmnxGsmpConfigEntry = _TmnxGsmpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 3, 1)
)
tmnxGsmpConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tmnxGsmpConfigEntry.setStatus("current")
_TmnxGsmpCfgLastChange_Type = TimeStamp
_TmnxGsmpCfgLastChange_Object = MibTableColumn
tmnxGsmpCfgLastChange = _TmnxGsmpCfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 3, 1, 1),
    _TmnxGsmpCfgLastChange_Type()
)
tmnxGsmpCfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGsmpCfgLastChange.setStatus("current")


class _TmnxGsmpCfgAdminState_Type(TmnxAdminState):
    """Custom type tmnxGsmpCfgAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxGsmpCfgAdminState_Type.__name__ = "TmnxAdminState"
_TmnxGsmpCfgAdminState_Object = MibTableColumn
tmnxGsmpCfgAdminState = _TmnxGsmpCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 3, 1, 2),
    _TmnxGsmpCfgAdminState_Type()
)
tmnxGsmpCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxGsmpCfgAdminState.setStatus("current")
_TmnxGsmpGroupConfigTableLastChange_Type = TimeStamp
_TmnxGsmpGroupConfigTableLastChange_Object = MibScalar
tmnxGsmpGroupConfigTableLastChange = _TmnxGsmpGroupConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 4),
    _TmnxGsmpGroupConfigTableLastChange_Type()
)
tmnxGsmpGroupConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGsmpGroupConfigTableLastChange.setStatus("current")
_TmnxGsmpGroupConfigTable_Object = MibTable
tmnxGsmpGroupConfigTable = _TmnxGsmpGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5)
)
if mibBuilder.loadTexts:
    tmnxGsmpGroupConfigTable.setStatus("current")
_TmnxGsmpGroupConfigEntry_Object = MibTableRow
tmnxGsmpGroupConfigEntry = _TmnxGsmpGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1)
)
tmnxGsmpGroupConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-GSMP-MIB", "tmnxGsmpGroupName"),
)
if mibBuilder.loadTexts:
    tmnxGsmpGroupConfigEntry.setStatus("current")
_TmnxGsmpGroupName_Type = TNamedItem
_TmnxGsmpGroupName_Object = MibTableColumn
tmnxGsmpGroupName = _TmnxGsmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 1),
    _TmnxGsmpGroupName_Type()
)
tmnxGsmpGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGsmpGroupName.setStatus("current")
_TmnxGsmpGrpCfgLastChange_Type = TimeStamp
_TmnxGsmpGrpCfgLastChange_Object = MibTableColumn
tmnxGsmpGrpCfgLastChange = _TmnxGsmpGrpCfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 2),
    _TmnxGsmpGrpCfgLastChange_Type()
)
tmnxGsmpGrpCfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgLastChange.setStatus("current")
_TmnxGsmpGrpCfgRowStatus_Type = RowStatus
_TmnxGsmpGrpCfgRowStatus_Object = MibTableColumn
tmnxGsmpGrpCfgRowStatus = _TmnxGsmpGrpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 3),
    _TmnxGsmpGrpCfgRowStatus_Type()
)
tmnxGsmpGrpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgRowStatus.setStatus("current")


class _TmnxGsmpGrpCfgAdminState_Type(TmnxAdminState):
    """Custom type tmnxGsmpGrpCfgAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxGsmpGrpCfgAdminState_Type.__name__ = "TmnxAdminState"
_TmnxGsmpGrpCfgAdminState_Object = MibTableColumn
tmnxGsmpGrpCfgAdminState = _TmnxGsmpGrpCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 4),
    _TmnxGsmpGrpCfgAdminState_Type()
)
tmnxGsmpGrpCfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgAdminState.setStatus("current")


class _TmnxGsmpGrpCfgKeepalive_Type(Unsigned32):
    """Custom type tmnxGsmpGrpCfgKeepalive based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_TmnxGsmpGrpCfgKeepalive_Type.__name__ = "Unsigned32"
_TmnxGsmpGrpCfgKeepalive_Object = MibTableColumn
tmnxGsmpGrpCfgKeepalive = _TmnxGsmpGrpCfgKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 5),
    _TmnxGsmpGrpCfgKeepalive_Type()
)
tmnxGsmpGrpCfgKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgKeepalive.setUnits("seconds")


class _TmnxGsmpGrpCfgHoldMultiplier_Type(Unsigned32):
    """Custom type tmnxGsmpGrpCfgHoldMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxGsmpGrpCfgHoldMultiplier_Type.__name__ = "Unsigned32"
_TmnxGsmpGrpCfgHoldMultiplier_Object = MibTableColumn
tmnxGsmpGrpCfgHoldMultiplier = _TmnxGsmpGrpCfgHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 6),
    _TmnxGsmpGrpCfgHoldMultiplier_Type()
)
tmnxGsmpGrpCfgHoldMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgHoldMultiplier.setStatus("current")


class _TmnxGsmpGrpCfgDescription_Type(TItemDescription):
    """Custom type tmnxGsmpGrpCfgDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxGsmpGrpCfgDescription_Type.__name__ = "TItemDescription"
_TmnxGsmpGrpCfgDescription_Object = MibTableColumn
tmnxGsmpGrpCfgDescription = _TmnxGsmpGrpCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 7),
    _TmnxGsmpGrpCfgDescription_Type()
)
tmnxGsmpGrpCfgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgDescription.setStatus("current")


class _TmnxGsmpGrpCfgAncpOamCap_Type(TmnxAdminState):
    """Custom type tmnxGsmpGrpCfgAncpOamCap based on TmnxAdminState"""
    defaultValue = 3


_TmnxGsmpGrpCfgAncpOamCap_Type.__name__ = "TmnxAdminState"
_TmnxGsmpGrpCfgAncpOamCap_Object = MibTableColumn
tmnxGsmpGrpCfgAncpOamCap = _TmnxGsmpGrpCfgAncpOamCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 8),
    _TmnxGsmpGrpCfgAncpOamCap_Type()
)
tmnxGsmpGrpCfgAncpOamCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgAncpOamCap.setStatus("current")


class _TmnxGsmpGrpCfgAncpDynTopoDiscCap_Type(TmnxAdminState):
    """Custom type tmnxGsmpGrpCfgAncpDynTopoDiscCap based on TmnxAdminState"""
    defaultValue = 2


_TmnxGsmpGrpCfgAncpDynTopoDiscCap_Type.__name__ = "TmnxAdminState"
_TmnxGsmpGrpCfgAncpDynTopoDiscCap_Object = MibTableColumn
tmnxGsmpGrpCfgAncpDynTopoDiscCap = _TmnxGsmpGrpCfgAncpDynTopoDiscCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 9),
    _TmnxGsmpGrpCfgAncpDynTopoDiscCap_Type()
)
tmnxGsmpGrpCfgAncpDynTopoDiscCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgAncpDynTopoDiscCap.setStatus("current")


class _TmnxGsmpGrpCfgPersistencyDb_Type(TmnxAdminState):
    """Custom type tmnxGsmpGrpCfgPersistencyDb based on TmnxAdminState"""
    defaultValue = 3


_TmnxGsmpGrpCfgPersistencyDb_Type.__name__ = "TmnxAdminState"
_TmnxGsmpGrpCfgPersistencyDb_Object = MibTableColumn
tmnxGsmpGrpCfgPersistencyDb = _TmnxGsmpGrpCfgPersistencyDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 10),
    _TmnxGsmpGrpCfgPersistencyDb_Type()
)
tmnxGsmpGrpCfgPersistencyDb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgPersistencyDb.setStatus("current")


class _TmnxGsmpGrpCfgIdleFilter_Type(TmnxAdminState):
    """Custom type tmnxGsmpGrpCfgIdleFilter based on TmnxAdminState"""
    defaultValue = 3


_TmnxGsmpGrpCfgIdleFilter_Type.__name__ = "TmnxAdminState"
_TmnxGsmpGrpCfgIdleFilter_Object = MibTableColumn
tmnxGsmpGrpCfgIdleFilter = _TmnxGsmpGrpCfgIdleFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 5, 1, 11),
    _TmnxGsmpGrpCfgIdleFilter_Type()
)
tmnxGsmpGrpCfgIdleFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpCfgIdleFilter.setStatus("current")
_TmnxGsmpGroupNbrTableLastChange_Type = TimeStamp
_TmnxGsmpGroupNbrTableLastChange_Object = MibScalar
tmnxGsmpGroupNbrTableLastChange = _TmnxGsmpGroupNbrTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 6),
    _TmnxGsmpGroupNbrTableLastChange_Type()
)
tmnxGsmpGroupNbrTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGsmpGroupNbrTableLastChange.setStatus("current")
_TmnxGsmpGroupNeighborTable_Object = MibTable
tmnxGsmpGroupNeighborTable = _TmnxGsmpGroupNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7)
)
if mibBuilder.loadTexts:
    tmnxGsmpGroupNeighborTable.setStatus("current")
_TmnxGsmpGroupNeighborEntry_Object = MibTableRow
tmnxGsmpGroupNeighborEntry = _TmnxGsmpGroupNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1)
)
tmnxGsmpGroupNeighborEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-GSMP-MIB", "tmnxGsmpGroupName"),
    (0, "TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrAddressType"),
    (0, "TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrAddress"),
)
if mibBuilder.loadTexts:
    tmnxGsmpGroupNeighborEntry.setStatus("current")
_TmnxGsmpGrpNbrAddressType_Type = InetAddressType
_TmnxGsmpGrpNbrAddressType_Object = MibTableColumn
tmnxGsmpGrpNbrAddressType = _TmnxGsmpGrpNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 1),
    _TmnxGsmpGrpNbrAddressType_Type()
)
tmnxGsmpGrpNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrAddressType.setStatus("current")


class _TmnxGsmpGrpNbrAddress_Type(InetAddress):
    """Custom type tmnxGsmpGrpNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxGsmpGrpNbrAddress_Type.__name__ = "InetAddress"
_TmnxGsmpGrpNbrAddress_Object = MibTableColumn
tmnxGsmpGrpNbrAddress = _TmnxGsmpGrpNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 2),
    _TmnxGsmpGrpNbrAddress_Type()
)
tmnxGsmpGrpNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrAddress.setStatus("current")
_TmnxGsmpGrpNbrLastChange_Type = TimeStamp
_TmnxGsmpGrpNbrLastChange_Object = MibTableColumn
tmnxGsmpGrpNbrLastChange = _TmnxGsmpGrpNbrLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 3),
    _TmnxGsmpGrpNbrLastChange_Type()
)
tmnxGsmpGrpNbrLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrLastChange.setStatus("current")
_TmnxGsmpGrpNbrRowStatus_Type = RowStatus
_TmnxGsmpGrpNbrRowStatus_Object = MibTableColumn
tmnxGsmpGrpNbrRowStatus = _TmnxGsmpGrpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 4),
    _TmnxGsmpGrpNbrRowStatus_Type()
)
tmnxGsmpGrpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrRowStatus.setStatus("current")


class _TmnxGsmpGrpNbrAdminState_Type(TmnxAdminState):
    """Custom type tmnxGsmpGrpNbrAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxGsmpGrpNbrAdminState_Type.__name__ = "TmnxAdminState"
_TmnxGsmpGrpNbrAdminState_Object = MibTableColumn
tmnxGsmpGrpNbrAdminState = _TmnxGsmpGrpNbrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 5),
    _TmnxGsmpGrpNbrAdminState_Type()
)
tmnxGsmpGrpNbrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrAdminState.setStatus("current")


class _TmnxGsmpGrpNbrLocalAddrType_Type(InetAddressType):
    """Custom type tmnxGsmpGrpNbrLocalAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxGsmpGrpNbrLocalAddrType_Type.__name__ = "InetAddressType"
_TmnxGsmpGrpNbrLocalAddrType_Object = MibTableColumn
tmnxGsmpGrpNbrLocalAddrType = _TmnxGsmpGrpNbrLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 6),
    _TmnxGsmpGrpNbrLocalAddrType_Type()
)
tmnxGsmpGrpNbrLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrLocalAddrType.setStatus("current")


class _TmnxGsmpGrpNbrLocalAddr_Type(InetAddress):
    """Custom type tmnxGsmpGrpNbrLocalAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxGsmpGrpNbrLocalAddr_Type.__name__ = "InetAddress"
_TmnxGsmpGrpNbrLocalAddr_Object = MibTableColumn
tmnxGsmpGrpNbrLocalAddr = _TmnxGsmpGrpNbrLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 7),
    _TmnxGsmpGrpNbrLocalAddr_Type()
)
tmnxGsmpGrpNbrLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrLocalAddr.setStatus("current")


class _TmnxGsmpGrpNbrDescription_Type(TItemDescription):
    """Custom type tmnxGsmpGrpNbrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxGsmpGrpNbrDescription_Type.__name__ = "TItemDescription"
_TmnxGsmpGrpNbrDescription_Object = MibTableColumn
tmnxGsmpGrpNbrDescription = _TmnxGsmpGrpNbrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 8),
    _TmnxGsmpGrpNbrDescription_Type()
)
tmnxGsmpGrpNbrDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrDescription.setStatus("current")


class _TmnxGsmpGrpNbrPrioMarkType_Type(TRemarkType):
    """Custom type tmnxGsmpGrpNbrPrioMarkType based on TRemarkType"""
    defaultValue = 1


_TmnxGsmpGrpNbrPrioMarkType_Type.__name__ = "TRemarkType"
_TmnxGsmpGrpNbrPrioMarkType_Object = MibTableColumn
tmnxGsmpGrpNbrPrioMarkType = _TmnxGsmpGrpNbrPrioMarkType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 9),
    _TmnxGsmpGrpNbrPrioMarkType_Type()
)
tmnxGsmpGrpNbrPrioMarkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrPrioMarkType.setStatus("current")


class _TmnxGsmpGrpNbrPrioMarkPrec_Type(TPrecValueOrNone):
    """Custom type tmnxGsmpGrpNbrPrioMarkPrec based on TPrecValueOrNone"""
    defaultValue = -1


_TmnxGsmpGrpNbrPrioMarkPrec_Type.__name__ = "TPrecValueOrNone"
_TmnxGsmpGrpNbrPrioMarkPrec_Object = MibTableColumn
tmnxGsmpGrpNbrPrioMarkPrec = _TmnxGsmpGrpNbrPrioMarkPrec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 10),
    _TmnxGsmpGrpNbrPrioMarkPrec_Type()
)
tmnxGsmpGrpNbrPrioMarkPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrPrioMarkPrec.setStatus("current")


class _TmnxGsmpGrpNbrPrioMarkDscp_Type(TDSCPNameOrEmpty):
    """Custom type tmnxGsmpGrpNbrPrioMarkDscp based on TDSCPNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxGsmpGrpNbrPrioMarkDscp_Type.__name__ = "TDSCPNameOrEmpty"
_TmnxGsmpGrpNbrPrioMarkDscp_Object = MibTableColumn
tmnxGsmpGrpNbrPrioMarkDscp = _TmnxGsmpGrpNbrPrioMarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 7, 1, 11),
    _TmnxGsmpGrpNbrPrioMarkDscp_Type()
)
tmnxGsmpGrpNbrPrioMarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGsmpGrpNbrPrioMarkDscp.setStatus("current")
_TmnxAncpStaticMapSapTblLastChg_Type = TimeStamp
_TmnxAncpStaticMapSapTblLastChg_Object = MibScalar
tmnxAncpStaticMapSapTblLastChg = _TmnxAncpStaticMapSapTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 8),
    _TmnxAncpStaticMapSapTblLastChg_Type()
)
tmnxAncpStaticMapSapTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapSapTblLastChg.setStatus("current")
_TmnxAncpStaticMapSapTable_Object = MibTable
tmnxAncpStaticMapSapTable = _TmnxAncpStaticMapSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 9)
)
if mibBuilder.loadTexts:
    tmnxAncpStaticMapSapTable.setStatus("current")
_TmnxAncpStaticMapSapEntry_Object = MibTableRow
tmnxAncpStaticMapSapEntry = _TmnxAncpStaticMapSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 9, 1)
)
tmnxAncpStaticMapSapEntry.setIndexNames(
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapString"),
)
if mibBuilder.loadTexts:
    tmnxAncpStaticMapSapEntry.setStatus("current")
_TmnxAncpStaticMapSapString_Type = TmnxAncpString
_TmnxAncpStaticMapSapString_Object = MibTableColumn
tmnxAncpStaticMapSapString = _TmnxAncpStaticMapSapString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 9, 1, 1),
    _TmnxAncpStaticMapSapString_Type()
)
tmnxAncpStaticMapSapString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapSapString.setStatus("current")
_TmnxAncpStaticMapSapLastChange_Type = TimeStamp
_TmnxAncpStaticMapSapLastChange_Object = MibTableColumn
tmnxAncpStaticMapSapLastChange = _TmnxAncpStaticMapSapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 9, 1, 2),
    _TmnxAncpStaticMapSapLastChange_Type()
)
tmnxAncpStaticMapSapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapSapLastChange.setStatus("current")
_TmnxAncpStaticMapSapRowStatus_Type = RowStatus
_TmnxAncpStaticMapSapRowStatus_Object = MibTableColumn
tmnxAncpStaticMapSapRowStatus = _TmnxAncpStaticMapSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 9, 1, 3),
    _TmnxAncpStaticMapSapRowStatus_Type()
)
tmnxAncpStaticMapSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapSapRowStatus.setStatus("current")
_TmnxAncpStaticMapSapAncpPolName_Type = TNamedItem
_TmnxAncpStaticMapSapAncpPolName_Object = MibTableColumn
tmnxAncpStaticMapSapAncpPolName = _TmnxAncpStaticMapSapAncpPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 9, 1, 4),
    _TmnxAncpStaticMapSapAncpPolName_Type()
)
tmnxAncpStaticMapSapAncpPolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapSapAncpPolName.setStatus("current")
_TmnxAncpStaticMapMssTblLastChg_Type = TimeStamp
_TmnxAncpStaticMapMssTblLastChg_Object = MibScalar
tmnxAncpStaticMapMssTblLastChg = _TmnxAncpStaticMapMssTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 10),
    _TmnxAncpStaticMapMssTblLastChg_Type()
)
tmnxAncpStaticMapMssTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapMssTblLastChg.setStatus("current")
_TmnxAncpStaticMapMssTable_Object = MibTable
tmnxAncpStaticMapMssTable = _TmnxAncpStaticMapMssTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 11)
)
if mibBuilder.loadTexts:
    tmnxAncpStaticMapMssTable.setStatus("current")
_TmnxAncpStaticMapMssEntry_Object = MibTableRow
tmnxAncpStaticMapMssEntry = _TmnxAncpStaticMapMssEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 11, 1)
)
tmnxAncpStaticMapMssEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssString"),
)
if mibBuilder.loadTexts:
    tmnxAncpStaticMapMssEntry.setStatus("current")
_TmnxAncpStaticMapMssString_Type = TmnxAncpString
_TmnxAncpStaticMapMssString_Object = MibTableColumn
tmnxAncpStaticMapMssString = _TmnxAncpStaticMapMssString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 11, 1, 1),
    _TmnxAncpStaticMapMssString_Type()
)
tmnxAncpStaticMapMssString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapMssString.setStatus("current")
_TmnxAncpStaticMapMssLastChange_Type = TimeStamp
_TmnxAncpStaticMapMssLastChange_Object = MibTableColumn
tmnxAncpStaticMapMssLastChange = _TmnxAncpStaticMapMssLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 11, 1, 2),
    _TmnxAncpStaticMapMssLastChange_Type()
)
tmnxAncpStaticMapMssLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapMssLastChange.setStatus("current")
_TmnxAncpStaticMapMssRowStatus_Type = RowStatus
_TmnxAncpStaticMapMssRowStatus_Object = MibTableColumn
tmnxAncpStaticMapMssRowStatus = _TmnxAncpStaticMapMssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 11, 1, 3),
    _TmnxAncpStaticMapMssRowStatus_Type()
)
tmnxAncpStaticMapMssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapMssRowStatus.setStatus("current")
_TmnxAncpStaticMapMssAncpPolName_Type = TNamedItem
_TmnxAncpStaticMapMssAncpPolName_Object = MibTableColumn
tmnxAncpStaticMapMssAncpPolName = _TmnxAncpStaticMapMssAncpPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 11, 1, 4),
    _TmnxAncpStaticMapMssAncpPolName_Type()
)
tmnxAncpStaticMapMssAncpPolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpStaticMapMssAncpPolName.setStatus("current")
_TmnxAncpSubProfileTblLastChange_Type = TimeStamp
_TmnxAncpSubProfileTblLastChange_Object = MibScalar
tmnxAncpSubProfileTblLastChange = _TmnxAncpSubProfileTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 12),
    _TmnxAncpSubProfileTblLastChange_Type()
)
tmnxAncpSubProfileTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubProfileTblLastChange.setStatus("current")
_TmnxAncpSubProfileTable_Object = MibTable
tmnxAncpSubProfileTable = _TmnxAncpSubProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 13)
)
if mibBuilder.loadTexts:
    tmnxAncpSubProfileTable.setStatus("current")
_TmnxAncpSubProfileEntry_Object = MibTableRow
tmnxAncpSubProfileEntry = _TmnxAncpSubProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 13, 1)
)
if mibBuilder.loadTexts:
    tmnxAncpSubProfileEntry.setStatus("current")


class _TmnxAncpSubProfileAncpPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxAncpSubProfileAncpPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxAncpSubProfileAncpPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxAncpSubProfileAncpPolicy_Object = MibTableColumn
tmnxAncpSubProfileAncpPolicy = _TmnxAncpSubProfileAncpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 13, 1, 1),
    _TmnxAncpSubProfileAncpPolicy_Type()
)
tmnxAncpSubProfileAncpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpSubProfileAncpPolicy.setStatus("current")
_TmnxAncpPolicyTableLastChange_Type = TimeStamp
_TmnxAncpPolicyTableLastChange_Object = MibScalar
tmnxAncpPolicyTableLastChange = _TmnxAncpPolicyTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 14),
    _TmnxAncpPolicyTableLastChange_Type()
)
tmnxAncpPolicyTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpPolicyTableLastChange.setStatus("current")
_TmnxAncpPolicyTable_Object = MibTable
tmnxAncpPolicyTable = _TmnxAncpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15)
)
if mibBuilder.loadTexts:
    tmnxAncpPolicyTable.setStatus("current")
_TmnxAncpPolicyEntry_Object = MibTableRow
tmnxAncpPolicyEntry = _TmnxAncpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1)
)
tmnxAncpPolicyEntry.setIndexNames(
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpPolicyName"),
)
if mibBuilder.loadTexts:
    tmnxAncpPolicyEntry.setStatus("current")
_TmnxAncpPolicyName_Type = TNamedItem
_TmnxAncpPolicyName_Object = MibTableColumn
tmnxAncpPolicyName = _TmnxAncpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 1),
    _TmnxAncpPolicyName_Type()
)
tmnxAncpPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpPolicyName.setStatus("current")
_TmnxAncpPlcyLastChange_Type = TimeStamp
_TmnxAncpPlcyLastChange_Object = MibTableColumn
tmnxAncpPlcyLastChange = _TmnxAncpPlcyLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 2),
    _TmnxAncpPlcyLastChange_Type()
)
tmnxAncpPlcyLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpPlcyLastChange.setStatus("current")
_TmnxAncpPlcyRowStatus_Type = RowStatus
_TmnxAncpPlcyRowStatus_Object = MibTableColumn
tmnxAncpPlcyRowStatus = _TmnxAncpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 3),
    _TmnxAncpPlcyRowStatus_Type()
)
tmnxAncpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyRowStatus.setStatus("current")


class _TmnxAncpPlcyIngRateAdjustment_Type(Unsigned32):
    """Custom type tmnxAncpPlcyIngRateAdjustment based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_TmnxAncpPlcyIngRateAdjustment_Type.__name__ = "Unsigned32"
_TmnxAncpPlcyIngRateAdjustment_Object = MibTableColumn
tmnxAncpPlcyIngRateAdjustment = _TmnxAncpPlcyIngRateAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 4),
    _TmnxAncpPlcyIngRateAdjustment_Type()
)
tmnxAncpPlcyIngRateAdjustment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyIngRateAdjustment.setStatus("current")


class _TmnxAncpPlcyIngRateReduction_Type(Unsigned32):
    """Custom type tmnxAncpPlcyIngRateReduction based on Unsigned32"""
    defaultValue = 0


_TmnxAncpPlcyIngRateReduction_Type.__name__ = "Unsigned32"
_TmnxAncpPlcyIngRateReduction_Object = MibTableColumn
tmnxAncpPlcyIngRateReduction = _TmnxAncpPlcyIngRateReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 5),
    _TmnxAncpPlcyIngRateReduction_Type()
)
tmnxAncpPlcyIngRateReduction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyIngRateReduction.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpPlcyIngRateReduction.setUnits("kbps")


class _TmnxAncpPlcyIngRateMonitor_Type(Unsigned32):
    """Custom type tmnxAncpPlcyIngRateMonitor based on Unsigned32"""
    defaultValue = 0


_TmnxAncpPlcyIngRateMonitor_Type.__name__ = "Unsigned32"
_TmnxAncpPlcyIngRateMonitor_Object = MibTableColumn
tmnxAncpPlcyIngRateMonitor = _TmnxAncpPlcyIngRateMonitor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 6),
    _TmnxAncpPlcyIngRateMonitor_Type()
)
tmnxAncpPlcyIngRateMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyIngRateMonitor.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpPlcyIngRateMonitor.setUnits("kbps")


class _TmnxAncpPlcyIngRateMonitorNtf_Type(TruthValue):
    """Custom type tmnxAncpPlcyIngRateMonitorNtf based on TruthValue"""
    defaultValue = 2


_TmnxAncpPlcyIngRateMonitorNtf_Type.__name__ = "TruthValue"
_TmnxAncpPlcyIngRateMonitorNtf_Object = MibTableColumn
tmnxAncpPlcyIngRateMonitorNtf = _TmnxAncpPlcyIngRateMonitorNtf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 7),
    _TmnxAncpPlcyIngRateMonitorNtf_Type()
)
tmnxAncpPlcyIngRateMonitorNtf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyIngRateMonitorNtf.setStatus("current")


class _TmnxAncpPlcyIngRateModType_Type(Integer32):
    """Custom type tmnxAncpPlcyIngRateModType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("namedScheduler", 2))
    )


_TmnxAncpPlcyIngRateModType_Type.__name__ = "Integer32"
_TmnxAncpPlcyIngRateModType_Object = MibTableColumn
tmnxAncpPlcyIngRateModType = _TmnxAncpPlcyIngRateModType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 8),
    _TmnxAncpPlcyIngRateModType_Type()
)
tmnxAncpPlcyIngRateModType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyIngRateModType.setStatus("current")


class _TmnxAncpPlcyIngRateModSched_Type(TNamedItemOrEmpty):
    """Custom type tmnxAncpPlcyIngRateModSched based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxAncpPlcyIngRateModSched_Type.__name__ = "TNamedItemOrEmpty"
_TmnxAncpPlcyIngRateModSched_Object = MibTableColumn
tmnxAncpPlcyIngRateModSched = _TmnxAncpPlcyIngRateModSched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 9),
    _TmnxAncpPlcyIngRateModSched_Type()
)
tmnxAncpPlcyIngRateModSched.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyIngRateModSched.setStatus("current")


class _TmnxAncpPlcyEgrRateAdjustment_Type(Unsigned32):
    """Custom type tmnxAncpPlcyEgrRateAdjustment based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_TmnxAncpPlcyEgrRateAdjustment_Type.__name__ = "Unsigned32"
_TmnxAncpPlcyEgrRateAdjustment_Object = MibTableColumn
tmnxAncpPlcyEgrRateAdjustment = _TmnxAncpPlcyEgrRateAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 10),
    _TmnxAncpPlcyEgrRateAdjustment_Type()
)
tmnxAncpPlcyEgrRateAdjustment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyEgrRateAdjustment.setStatus("current")


class _TmnxAncpPlcyEgrRateReduction_Type(Unsigned32):
    """Custom type tmnxAncpPlcyEgrRateReduction based on Unsigned32"""
    defaultValue = 0


_TmnxAncpPlcyEgrRateReduction_Type.__name__ = "Unsigned32"
_TmnxAncpPlcyEgrRateReduction_Object = MibTableColumn
tmnxAncpPlcyEgrRateReduction = _TmnxAncpPlcyEgrRateReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 11),
    _TmnxAncpPlcyEgrRateReduction_Type()
)
tmnxAncpPlcyEgrRateReduction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyEgrRateReduction.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpPlcyEgrRateReduction.setUnits("kbps")


class _TmnxAncpPlcyEgrRateMonitor_Type(Unsigned32):
    """Custom type tmnxAncpPlcyEgrRateMonitor based on Unsigned32"""
    defaultValue = 0


_TmnxAncpPlcyEgrRateMonitor_Type.__name__ = "Unsigned32"
_TmnxAncpPlcyEgrRateMonitor_Object = MibTableColumn
tmnxAncpPlcyEgrRateMonitor = _TmnxAncpPlcyEgrRateMonitor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 12),
    _TmnxAncpPlcyEgrRateMonitor_Type()
)
tmnxAncpPlcyEgrRateMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyEgrRateMonitor.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpPlcyEgrRateMonitor.setUnits("kbps")


class _TmnxAncpPlcyEgrRateMonitorNtf_Type(TruthValue):
    """Custom type tmnxAncpPlcyEgrRateMonitorNtf based on TruthValue"""
    defaultValue = 2


_TmnxAncpPlcyEgrRateMonitorNtf_Type.__name__ = "TruthValue"
_TmnxAncpPlcyEgrRateMonitorNtf_Object = MibTableColumn
tmnxAncpPlcyEgrRateMonitorNtf = _TmnxAncpPlcyEgrRateMonitorNtf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 13),
    _TmnxAncpPlcyEgrRateMonitorNtf_Type()
)
tmnxAncpPlcyEgrRateMonitorNtf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyEgrRateMonitorNtf.setStatus("current")


class _TmnxAncpPlcyEgrRateModType_Type(TEgrRateModType):
    """Custom type tmnxAncpPlcyEgrRateModType based on TEgrRateModType"""
    defaultValue = 1


_TmnxAncpPlcyEgrRateModType_Type.__name__ = "TEgrRateModType"
_TmnxAncpPlcyEgrRateModType_Object = MibTableColumn
tmnxAncpPlcyEgrRateModType = _TmnxAncpPlcyEgrRateModType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 14),
    _TmnxAncpPlcyEgrRateModType_Type()
)
tmnxAncpPlcyEgrRateModType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyEgrRateModType.setStatus("current")


class _TmnxAncpPlcyEgrRateModSched_Type(TNamedItemOrEmpty):
    """Custom type tmnxAncpPlcyEgrRateModSched based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxAncpPlcyEgrRateModSched_Type.__name__ = "TNamedItemOrEmpty"
_TmnxAncpPlcyEgrRateModSched_Object = MibTableColumn
tmnxAncpPlcyEgrRateModSched = _TmnxAncpPlcyEgrRateModSched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 15),
    _TmnxAncpPlcyEgrRateModSched_Type()
)
tmnxAncpPlcyEgrRateModSched.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyEgrRateModSched.setStatus("current")


class _TmnxAncpPlcyDisableShcv_Type(TruthValue):
    """Custom type tmnxAncpPlcyDisableShcv based on TruthValue"""
    defaultValue = 2


_TmnxAncpPlcyDisableShcv_Type.__name__ = "TruthValue"
_TmnxAncpPlcyDisableShcv_Object = MibTableColumn
tmnxAncpPlcyDisableShcv = _TmnxAncpPlcyDisableShcv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 16),
    _TmnxAncpPlcyDisableShcv_Type()
)
tmnxAncpPlcyDisableShcv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyDisableShcv.setStatus("current")


class _TmnxAncpPlcyDisableShcvHldTime_Type(Unsigned32):
    """Custom type tmnxAncpPlcyDisableShcvHldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_TmnxAncpPlcyDisableShcvHldTime_Type.__name__ = "Unsigned32"
_TmnxAncpPlcyDisableShcvHldTime_Object = MibTableColumn
tmnxAncpPlcyDisableShcvHldTime = _TmnxAncpPlcyDisableShcvHldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 17),
    _TmnxAncpPlcyDisableShcvHldTime_Type()
)
tmnxAncpPlcyDisableShcvHldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyDisableShcvHldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpPlcyDisableShcvHldTime.setUnits("seconds")


class _TmnxAncpPlcyDisableShcvNtf_Type(TruthValue):
    """Custom type tmnxAncpPlcyDisableShcvNtf based on TruthValue"""
    defaultValue = 2


_TmnxAncpPlcyDisableShcvNtf_Type.__name__ = "TruthValue"
_TmnxAncpPlcyDisableShcvNtf_Object = MibTableColumn
tmnxAncpPlcyDisableShcvNtf = _TmnxAncpPlcyDisableShcvNtf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 15, 1, 18),
    _TmnxAncpPlcyDisableShcvNtf_Type()
)
tmnxAncpPlcyDisableShcvNtf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxAncpPlcyDisableShcvNtf.setStatus("current")
_TmnxAncpStringInfoTable_Object = MibTable
tmnxAncpStringInfoTable = _TmnxAncpStringInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16)
)
if mibBuilder.loadTexts:
    tmnxAncpStringInfoTable.setStatus("current")
_TmnxAncpStringInfoEntry_Object = MibTableRow
tmnxAncpStringInfoEntry = _TmnxAncpStringInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1)
)
tmnxAncpStringInfoEntry.setIndexNames(
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpStrInfAncpString"),
)
if mibBuilder.loadTexts:
    tmnxAncpStringInfoEntry.setStatus("current")
_TmnxAncpStrInfAncpString_Type = TmnxAncpString
_TmnxAncpStrInfAncpString_Object = MibTableColumn
tmnxAncpStrInfAncpString = _TmnxAncpStrInfAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 1),
    _TmnxAncpStrInfAncpString_Type()
)
tmnxAncpStrInfAncpString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpStrInfAncpString.setStatus("current")


class _TmnxAncpStrInfAssociation_Type(Integer32):
    """Custom type tmnxAncpStrInfAssociation based on Integer32"""
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
          ("sap", 2),
          ("multiServSite", 3),
          ("subscriberId", 4))
    )


_TmnxAncpStrInfAssociation_Type.__name__ = "Integer32"
_TmnxAncpStrInfAssociation_Object = MibTableColumn
tmnxAncpStrInfAssociation = _TmnxAncpStrInfAssociation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 2),
    _TmnxAncpStrInfAssociation_Type()
)
tmnxAncpStrInfAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfAssociation.setStatus("current")
_TmnxAncpStrInfSapPortId_Type = TmnxPortID
_TmnxAncpStrInfSapPortId_Object = MibTableColumn
tmnxAncpStrInfSapPortId = _TmnxAncpStrInfSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 3),
    _TmnxAncpStrInfSapPortId_Type()
)
tmnxAncpStrInfSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfSapPortId.setStatus("current")
_TmnxAncpStrInfSapEncapValue_Type = TmnxEncapVal
_TmnxAncpStrInfSapEncapValue_Object = MibTableColumn
tmnxAncpStrInfSapEncapValue = _TmnxAncpStrInfSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 4),
    _TmnxAncpStrInfSapEncapValue_Type()
)
tmnxAncpStrInfSapEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfSapEncapValue.setStatus("current")
_TmnxAncpStrInfMultSvcSiteName_Type = TNamedItemOrEmpty
_TmnxAncpStrInfMultSvcSiteName_Object = MibTableColumn
tmnxAncpStrInfMultSvcSiteName = _TmnxAncpStrInfMultSvcSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 5),
    _TmnxAncpStrInfMultSvcSiteName_Type()
)
tmnxAncpStrInfMultSvcSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfMultSvcSiteName.setStatus("current")
_TmnxAncpStrInfMultSvcSiteCust_Type = TmnxCustId
_TmnxAncpStrInfMultSvcSiteCust_Object = MibTableColumn
tmnxAncpStrInfMultSvcSiteCust = _TmnxAncpStrInfMultSvcSiteCust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 6),
    _TmnxAncpStrInfMultSvcSiteCust_Type()
)
tmnxAncpStrInfMultSvcSiteCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfMultSvcSiteCust.setStatus("current")
_TmnxAncpStrInfSubscrIdent_Type = DisplayString
_TmnxAncpStrInfSubscrIdent_Object = MibTableColumn
tmnxAncpStrInfSubscrIdent = _TmnxAncpStrInfSubscrIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 7),
    _TmnxAncpStrInfSubscrIdent_Type()
)
tmnxAncpStrInfSubscrIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfSubscrIdent.setStatus("current")


class _TmnxAncpStrInfLineState_Type(Integer32):
    """Custom type tmnxAncpStrInfLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("down", 2),
          ("up", 3))
    )


_TmnxAncpStrInfLineState_Type.__name__ = "Integer32"
_TmnxAncpStrInfLineState_Object = MibTableColumn
tmnxAncpStrInfLineState = _TmnxAncpStrInfLineState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 8),
    _TmnxAncpStrInfLineState_Type()
)
tmnxAncpStrInfLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfLineState.setStatus("current")
_TmnxAncpStrInfAncpPolicyName_Type = TNamedItemOrEmpty
_TmnxAncpStrInfAncpPolicyName_Object = MibTableColumn
tmnxAncpStrInfAncpPolicyName = _TmnxAncpStrInfAncpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 9),
    _TmnxAncpStrInfAncpPolicyName_Type()
)
tmnxAncpStrInfAncpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfAncpPolicyName.setStatus("current")
_TmnxAncpStrInfIngrRate_Type = TPIRRateOverride
_TmnxAncpStrInfIngrRate_Object = MibTableColumn
tmnxAncpStrInfIngrRate = _TmnxAncpStrInfIngrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 10),
    _TmnxAncpStrInfIngrRate_Type()
)
tmnxAncpStrInfIngrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfIngrRate.setStatus("current")
_TmnxAncpStrInfAdjustedIngrRate_Type = TPIRRateOverride
_TmnxAncpStrInfAdjustedIngrRate_Object = MibTableColumn
tmnxAncpStrInfAdjustedIngrRate = _TmnxAncpStrInfAdjustedIngrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 11),
    _TmnxAncpStrInfAdjustedIngrRate_Type()
)
tmnxAncpStrInfAdjustedIngrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfAdjustedIngrRate.setStatus("current")
_TmnxAncpStrInfEgrRate_Type = TPIRRateOverride
_TmnxAncpStrInfEgrRate_Object = MibTableColumn
tmnxAncpStrInfEgrRate = _TmnxAncpStrInfEgrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 12),
    _TmnxAncpStrInfEgrRate_Type()
)
tmnxAncpStrInfEgrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfEgrRate.setStatus("current")
_TmnxAncpStrInfAdjustedEgrRate_Type = TPIRRateOverride
_TmnxAncpStrInfAdjustedEgrRate_Object = MibTableColumn
tmnxAncpStrInfAdjustedEgrRate = _TmnxAncpStrInfAdjustedEgrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 13),
    _TmnxAncpStrInfAdjustedEgrRate_Type()
)
tmnxAncpStrInfAdjustedEgrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfAdjustedEgrRate.setStatus("current")
_TmnxAncpStrInfServId_Type = TmnxServId
_TmnxAncpStrInfServId_Object = MibTableColumn
tmnxAncpStrInfServId = _TmnxAncpStrInfServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 14),
    _TmnxAncpStrInfServId_Type()
)
tmnxAncpStrInfServId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfServId.setStatus("current")
_TmnxAncpStrInfNeighborAddrType_Type = InetAddressType
_TmnxAncpStrInfNeighborAddrType_Object = MibTableColumn
tmnxAncpStrInfNeighborAddrType = _TmnxAncpStrInfNeighborAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 15),
    _TmnxAncpStrInfNeighborAddrType_Type()
)
tmnxAncpStrInfNeighborAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfNeighborAddrType.setStatus("current")
_TmnxAncpStrInfNeighborAddr_Type = InetAddress
_TmnxAncpStrInfNeighborAddr_Object = MibTableColumn
tmnxAncpStrInfNeighborAddr = _TmnxAncpStrInfNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 16),
    _TmnxAncpStrInfNeighborAddr_Type()
)
tmnxAncpStrInfNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfNeighborAddr.setStatus("current")
_TmnxAncpStrInfTcpPort_Type = Unsigned32
_TmnxAncpStrInfTcpPort_Object = MibTableColumn
tmnxAncpStrInfTcpPort = _TmnxAncpStrInfTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 17),
    _TmnxAncpStrInfTcpPort_Type()
)
tmnxAncpStrInfTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfTcpPort.setStatus("current")
_TmnxAncpStrInfGroupName_Type = TNamedItemOrEmpty
_TmnxAncpStrInfGroupName_Object = MibTableColumn
tmnxAncpStrInfGroupName = _TmnxAncpStrInfGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 18),
    _TmnxAncpStrInfGroupName_Type()
)
tmnxAncpStrInfGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfGroupName.setStatus("current")
_TmnxAncpStrInfPersistKey_Type = Unsigned32
_TmnxAncpStrInfPersistKey_Object = MibTableColumn
tmnxAncpStrInfPersistKey = _TmnxAncpStrInfPersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 16, 1, 19),
    _TmnxAncpStrInfPersistKey_Type()
)
tmnxAncpStrInfPersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStrInfPersistKey.setStatus("current")
_TmnxAncpSessionTable_Object = MibTable
tmnxAncpSessionTable = _TmnxAncpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17)
)
if mibBuilder.loadTexts:
    tmnxAncpSessionTable.setStatus("current")
_TmnxAncpSessionEntry_Object = MibTableRow
tmnxAncpSessionEntry = _TmnxAncpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1)
)
tmnxAncpSessionEntry.setIndexNames(
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSesServiceId"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSesNbrAddressType"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSesNbrAddress"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSesNbrTcpPort"),
)
if mibBuilder.loadTexts:
    tmnxAncpSessionEntry.setStatus("current")
_TmnxAncpSesServiceId_Type = TmnxServId
_TmnxAncpSesServiceId_Object = MibTableColumn
tmnxAncpSesServiceId = _TmnxAncpSesServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 1),
    _TmnxAncpSesServiceId_Type()
)
tmnxAncpSesServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpSesServiceId.setStatus("current")
_TmnxAncpSesNbrAddressType_Type = InetAddressType
_TmnxAncpSesNbrAddressType_Object = MibTableColumn
tmnxAncpSesNbrAddressType = _TmnxAncpSesNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 2),
    _TmnxAncpSesNbrAddressType_Type()
)
tmnxAncpSesNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrAddressType.setStatus("current")
_TmnxAncpSesNbrAddress_Type = InetAddress
_TmnxAncpSesNbrAddress_Object = MibTableColumn
tmnxAncpSesNbrAddress = _TmnxAncpSesNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 3),
    _TmnxAncpSesNbrAddress_Type()
)
tmnxAncpSesNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrAddress.setStatus("current")
_TmnxAncpSesNbrTcpPort_Type = Unsigned32
_TmnxAncpSesNbrTcpPort_Object = MibTableColumn
tmnxAncpSesNbrTcpPort = _TmnxAncpSesNbrTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 4),
    _TmnxAncpSesNbrTcpPort_Type()
)
tmnxAncpSesNbrTcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrTcpPort.setStatus("current")
_TmnxAncpSesNbrPeerInstance_Type = Unsigned32
_TmnxAncpSesNbrPeerInstance_Object = MibTableColumn
tmnxAncpSesNbrPeerInstance = _TmnxAncpSesNbrPeerInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 5),
    _TmnxAncpSesNbrPeerInstance_Type()
)
tmnxAncpSesNbrPeerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrPeerInstance.setStatus("current")
_TmnxAncpSesNbrPeerPort_Type = Unsigned32
_TmnxAncpSesNbrPeerPort_Object = MibTableColumn
tmnxAncpSesNbrPeerPort = _TmnxAncpSesNbrPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 6),
    _TmnxAncpSesNbrPeerPort_Type()
)
tmnxAncpSesNbrPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrPeerPort.setStatus("current")


class _TmnxAncpSesNbrPeerName_Type(OctetString):
    """Custom type tmnxAncpSesNbrPeerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TmnxAncpSesNbrPeerName_Type.__name__ = "OctetString"
_TmnxAncpSesNbrPeerName_Object = MibTableColumn
tmnxAncpSesNbrPeerName = _TmnxAncpSesNbrPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 7),
    _TmnxAncpSesNbrPeerName_Type()
)
tmnxAncpSesNbrPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrPeerName.setStatus("current")
_TmnxAncpSesSenderInstance_Type = Unsigned32
_TmnxAncpSesSenderInstance_Object = MibTableColumn
tmnxAncpSesSenderInstance = _TmnxAncpSesSenderInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 8),
    _TmnxAncpSesSenderInstance_Type()
)
tmnxAncpSesSenderInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesSenderInstance.setStatus("current")
_TmnxAncpSesSenderPort_Type = Unsigned32
_TmnxAncpSesSenderPort_Object = MibTableColumn
tmnxAncpSesSenderPort = _TmnxAncpSesSenderPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 9),
    _TmnxAncpSesSenderPort_Type()
)
tmnxAncpSesSenderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesSenderPort.setStatus("current")


class _TmnxAncpSesSenderName_Type(OctetString):
    """Custom type tmnxAncpSesSenderName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TmnxAncpSesSenderName_Type.__name__ = "OctetString"
_TmnxAncpSesSenderName_Object = MibTableColumn
tmnxAncpSesSenderName = _TmnxAncpSesSenderName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 10),
    _TmnxAncpSesSenderName_Type()
)
tmnxAncpSesSenderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesSenderName.setStatus("current")
_TmnxAncpSesNbrTimeouts_Type = Unsigned32
_TmnxAncpSesNbrTimeouts_Object = MibTableColumn
tmnxAncpSesNbrTimeouts = _TmnxAncpSesNbrTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 11),
    _TmnxAncpSesNbrTimeouts_Type()
)
tmnxAncpSesNbrTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrTimeouts.setStatus("current")
_TmnxAncpSesNbrMaxNbrOfTimeouts_Type = Unsigned32
_TmnxAncpSesNbrMaxNbrOfTimeouts_Object = MibTableColumn
tmnxAncpSesNbrMaxNbrOfTimeouts = _TmnxAncpSesNbrMaxNbrOfTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 12),
    _TmnxAncpSesNbrMaxNbrOfTimeouts_Type()
)
tmnxAncpSesNbrMaxNbrOfTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrMaxNbrOfTimeouts.setStatus("current")
_TmnxAncpSesNbrTimer_Type = Unsigned32
_TmnxAncpSesNbrTimer_Object = MibTableColumn
tmnxAncpSesNbrTimer = _TmnxAncpSesNbrTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 13),
    _TmnxAncpSesNbrTimer_Type()
)
tmnxAncpSesNbrTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesNbrTimer.setStatus("current")
_TmnxAncpSesSenderTimer_Type = Unsigned32
_TmnxAncpSesSenderTimer_Object = MibTableColumn
tmnxAncpSesSenderTimer = _TmnxAncpSesSenderTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 14),
    _TmnxAncpSesSenderTimer_Type()
)
tmnxAncpSesSenderTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesSenderTimer.setStatus("current")


class _TmnxAncpSesNegotiatedCaps_Type(Bits):
    """Custom type tmnxAncpSesNegotiatedCaps based on Bits"""
    namedValues = NamedValues(
        *(("oamCap", 0),
          ("dynTopoDiscCap", 1))
    )

_TmnxAncpSesNegotiatedCaps_Type.__name__ = "Bits"
_TmnxAncpSesNegotiatedCaps_Object = MibTableColumn
tmnxAncpSesNegotiatedCaps = _TmnxAncpSesNegotiatedCaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 15),
    _TmnxAncpSesNegotiatedCaps_Type()
)
tmnxAncpSesNegotiatedCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesNegotiatedCaps.setStatus("current")


class _TmnxAncpSesConfiguredCaps_Type(Bits):
    """Custom type tmnxAncpSesConfiguredCaps based on Bits"""
    namedValues = NamedValues(
        *(("oamCap", 0),
          ("dynTopoDiscCap", 1))
    )

_TmnxAncpSesConfiguredCaps_Type.__name__ = "Bits"
_TmnxAncpSesConfiguredCaps_Object = MibTableColumn
tmnxAncpSesConfiguredCaps = _TmnxAncpSesConfiguredCaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 16),
    _TmnxAncpSesConfiguredCaps_Type()
)
tmnxAncpSesConfiguredCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesConfiguredCaps.setStatus("current")
_TmnxAncpSesGroupName_Type = TNamedItem
_TmnxAncpSesGroupName_Object = MibTableColumn
tmnxAncpSesGroupName = _TmnxAncpSesGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 17),
    _TmnxAncpSesGroupName_Type()
)
tmnxAncpSesGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesGroupName.setStatus("current")


class _TmnxAncpSesState_Type(Integer32):
    """Custom type tmnxAncpSesState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("synSent", 1),
          ("synReceived", 2),
          ("established", 3))
    )


_TmnxAncpSesState_Type.__name__ = "Integer32"
_TmnxAncpSesState_Object = MibTableColumn
tmnxAncpSesState = _TmnxAncpSesState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 18),
    _TmnxAncpSesState_Type()
)
tmnxAncpSesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesState.setStatus("current")
_TmnxAncpSesLocalAddrType_Type = InetAddressType
_TmnxAncpSesLocalAddrType_Object = MibTableColumn
tmnxAncpSesLocalAddrType = _TmnxAncpSesLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 19),
    _TmnxAncpSesLocalAddrType_Type()
)
tmnxAncpSesLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesLocalAddrType.setStatus("current")
_TmnxAncpSesLocalAddr_Type = InetAddress
_TmnxAncpSesLocalAddr_Object = MibTableColumn
tmnxAncpSesLocalAddr = _TmnxAncpSesLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 20),
    _TmnxAncpSesLocalAddr_Type()
)
tmnxAncpSesLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesLocalAddr.setStatus("current")


class _TmnxAncpSesVersion_Type(Integer32):
    """Custom type tmnxAncpSesVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gsmp", 1),
          ("ancp", 2))
    )


_TmnxAncpSesVersion_Type.__name__ = "Integer32"
_TmnxAncpSesVersion_Object = MibTableColumn
tmnxAncpSesVersion = _TmnxAncpSesVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 21),
    _TmnxAncpSesVersion_Type()
)
tmnxAncpSesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesVersion.setStatus("current")


class _TmnxAncpSesPartitionID_Type(Integer32):
    """Custom type tmnxAncpSesPartitionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxAncpSesPartitionID_Type.__name__ = "Integer32"
_TmnxAncpSesPartitionID_Object = MibTableColumn
tmnxAncpSesPartitionID = _TmnxAncpSesPartitionID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 17, 1, 22),
    _TmnxAncpSesPartitionID_Type()
)
tmnxAncpSesPartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesPartitionID.setStatus("current")
_TmnxAncpSessionStatsTable_Object = MibTable
tmnxAncpSessionStatsTable = _TmnxAncpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18)
)
if mibBuilder.loadTexts:
    tmnxAncpSessionStatsTable.setStatus("current")
_TmnxAncpSessionStatsEntry_Object = MibTableRow
tmnxAncpSessionStatsEntry = _TmnxAncpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1)
)
tmnxAncpSessionStatsEntry.setIndexNames(
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSesServiceId"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSesNbrAddressType"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSesNbrAddress"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSesNbrTcpPort"),
)
if mibBuilder.loadTexts:
    tmnxAncpSessionStatsEntry.setStatus("current")
_TmnxAncpSesStatLastChanged_Type = TimeStamp
_TmnxAncpSesStatLastChanged_Object = MibTableColumn
tmnxAncpSesStatLastChanged = _TmnxAncpSesStatLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 1),
    _TmnxAncpSesStatLastChanged_Type()
)
tmnxAncpSesStatLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatLastChanged.setStatus("current")
_TmnxAncpSesStatRxDrop_Type = Counter32
_TmnxAncpSesStatRxDrop_Object = MibTableColumn
tmnxAncpSesStatRxDrop = _TmnxAncpSesStatRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 2),
    _TmnxAncpSesStatRxDrop_Type()
)
tmnxAncpSesStatRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatRxDrop.setStatus("current")
_TmnxAncpSesStatTxDrop_Type = Counter32
_TmnxAncpSesStatTxDrop_Object = MibTableColumn
tmnxAncpSesStatTxDrop = _TmnxAncpSesStatTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 3),
    _TmnxAncpSesStatTxDrop_Type()
)
tmnxAncpSesStatTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatTxDrop.setStatus("current")
_TmnxAncpSesStatRxSyn_Type = Counter32
_TmnxAncpSesStatRxSyn_Object = MibTableColumn
tmnxAncpSesStatRxSyn = _TmnxAncpSesStatRxSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 4),
    _TmnxAncpSesStatRxSyn_Type()
)
tmnxAncpSesStatRxSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatRxSyn.setStatus("current")
_TmnxAncpSesStatTxSyn_Type = Counter32
_TmnxAncpSesStatTxSyn_Object = MibTableColumn
tmnxAncpSesStatTxSyn = _TmnxAncpSesStatTxSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 5),
    _TmnxAncpSesStatTxSyn_Type()
)
tmnxAncpSesStatTxSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatTxSyn.setStatus("current")
_TmnxAncpSesStatRxSynAck_Type = Counter32
_TmnxAncpSesStatRxSynAck_Object = MibTableColumn
tmnxAncpSesStatRxSynAck = _TmnxAncpSesStatRxSynAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 6),
    _TmnxAncpSesStatRxSynAck_Type()
)
tmnxAncpSesStatRxSynAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatRxSynAck.setStatus("current")
_TmnxAncpSesStatTxSynAck_Type = Counter32
_TmnxAncpSesStatTxSynAck_Object = MibTableColumn
tmnxAncpSesStatTxSynAck = _TmnxAncpSesStatTxSynAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 7),
    _TmnxAncpSesStatTxSynAck_Type()
)
tmnxAncpSesStatTxSynAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatTxSynAck.setStatus("current")
_TmnxAncpSesStatRxAck_Type = Counter32
_TmnxAncpSesStatRxAck_Object = MibTableColumn
tmnxAncpSesStatRxAck = _TmnxAncpSesStatRxAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 8),
    _TmnxAncpSesStatRxAck_Type()
)
tmnxAncpSesStatRxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatRxAck.setStatus("current")
_TmnxAncpSesStatTxAck_Type = Counter32
_TmnxAncpSesStatTxAck_Object = MibTableColumn
tmnxAncpSesStatTxAck = _TmnxAncpSesStatTxAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 9),
    _TmnxAncpSesStatTxAck_Type()
)
tmnxAncpSesStatTxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatTxAck.setStatus("current")
_TmnxAncpSesStatRxRstAck_Type = Counter32
_TmnxAncpSesStatRxRstAck_Object = MibTableColumn
tmnxAncpSesStatRxRstAck = _TmnxAncpSesStatRxRstAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 10),
    _TmnxAncpSesStatRxRstAck_Type()
)
tmnxAncpSesStatRxRstAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatRxRstAck.setStatus("current")
_TmnxAncpSesStatTxRstAck_Type = Counter32
_TmnxAncpSesStatTxRstAck_Object = MibTableColumn
tmnxAncpSesStatTxRstAck = _TmnxAncpSesStatTxRstAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 11),
    _TmnxAncpSesStatTxRstAck_Type()
)
tmnxAncpSesStatTxRstAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatTxRstAck.setStatus("current")
_TmnxAncpSesStatRxPortUp_Type = Counter32
_TmnxAncpSesStatRxPortUp_Object = MibTableColumn
tmnxAncpSesStatRxPortUp = _TmnxAncpSesStatRxPortUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 12),
    _TmnxAncpSesStatRxPortUp_Type()
)
tmnxAncpSesStatRxPortUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatRxPortUp.setStatus("current")
_TmnxAncpSesStatTxPortUp_Type = Counter32
_TmnxAncpSesStatTxPortUp_Object = MibTableColumn
tmnxAncpSesStatTxPortUp = _TmnxAncpSesStatTxPortUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 13),
    _TmnxAncpSesStatTxPortUp_Type()
)
tmnxAncpSesStatTxPortUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatTxPortUp.setStatus("current")
_TmnxAncpSesStatRxPortDown_Type = Counter32
_TmnxAncpSesStatRxPortDown_Object = MibTableColumn
tmnxAncpSesStatRxPortDown = _TmnxAncpSesStatRxPortDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 14),
    _TmnxAncpSesStatRxPortDown_Type()
)
tmnxAncpSesStatRxPortDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatRxPortDown.setStatus("current")
_TmnxAncpSesStatTxPortDown_Type = Counter32
_TmnxAncpSesStatTxPortDown_Object = MibTableColumn
tmnxAncpSesStatTxPortDown = _TmnxAncpSesStatTxPortDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 15),
    _TmnxAncpSesStatTxPortDown_Type()
)
tmnxAncpSesStatTxPortDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatTxPortDown.setStatus("current")
_TmnxAncpSesStatRxLoopback_Type = Counter32
_TmnxAncpSesStatRxLoopback_Object = MibTableColumn
tmnxAncpSesStatRxLoopback = _TmnxAncpSesStatRxLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 16),
    _TmnxAncpSesStatRxLoopback_Type()
)
tmnxAncpSesStatRxLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatRxLoopback.setStatus("current")
_TmnxAncpSesStatTxLoopback_Type = Counter32
_TmnxAncpSesStatTxLoopback_Object = MibTableColumn
tmnxAncpSesStatTxLoopback = _TmnxAncpSesStatTxLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 18, 1, 17),
    _TmnxAncpSesStatTxLoopback_Type()
)
tmnxAncpSesStatTxLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSesStatTxLoopback.setStatus("current")
_TmnxAncpSapMonitorTable_Object = MibTable
tmnxAncpSapMonitorTable = _TmnxAncpSapMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 19)
)
if mibBuilder.loadTexts:
    tmnxAncpSapMonitorTable.setStatus("current")
_TmnxAncpSapMonitorEntry_Object = MibTableRow
tmnxAncpSapMonitorEntry = _TmnxAncpSapMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 19, 1)
)
tmnxAncpSapMonitorEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxAncpSapMonitorEntry.setStatus("current")
_TmnxAncpSapMntrEgrAggRateLimit_Type = TPIRAggRateLimitOverride
_TmnxAncpSapMntrEgrAggRateLimit_Object = MibTableColumn
tmnxAncpSapMntrEgrAggRateLimit = _TmnxAncpSapMntrEgrAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 19, 1, 1),
    _TmnxAncpSapMntrEgrAggRateLimit_Type()
)
tmnxAncpSapMntrEgrAggRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapMntrEgrAggRateLimit.setStatus("current")
_TmnxAncpSapMntrAncpString_Type = TmnxAncpString
_TmnxAncpSapMntrAncpString_Object = MibTableColumn
tmnxAncpSapMntrAncpString = _TmnxAncpSapMntrAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 19, 1, 2),
    _TmnxAncpSapMntrAncpString_Type()
)
tmnxAncpSapMntrAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapMntrAncpString.setStatus("current")
_TmnxAncpSapIngSchedMonitorTable_Object = MibTable
tmnxAncpSapIngSchedMonitorTable = _TmnxAncpSapIngSchedMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 20)
)
if mibBuilder.loadTexts:
    tmnxAncpSapIngSchedMonitorTable.setStatus("current")
_TmnxAncpSapIngSchedMonitorEntry_Object = MibTableRow
tmnxAncpSapIngSchedMonitorEntry = _TmnxAncpSapIngSchedMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 20, 1)
)
tmnxAncpSapIngSchedMonitorEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSapIngMntrQosShedName"),
)
if mibBuilder.loadTexts:
    tmnxAncpSapIngSchedMonitorEntry.setStatus("current")
_TmnxAncpSapIngMntrQosShedName_Type = TNamedItem
_TmnxAncpSapIngMntrQosShedName_Object = MibTableColumn
tmnxAncpSapIngMntrQosShedName = _TmnxAncpSapIngMntrQosShedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 20, 1, 1),
    _TmnxAncpSapIngMntrQosShedName_Type()
)
tmnxAncpSapIngMntrQosShedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpSapIngMntrQosShedName.setStatus("current")
_TmnxAncpSapIngMntrQosShedPIR_Type = TPIRRateOverride
_TmnxAncpSapIngMntrQosShedPIR_Object = MibTableColumn
tmnxAncpSapIngMntrQosShedPIR = _TmnxAncpSapIngMntrQosShedPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 20, 1, 2),
    _TmnxAncpSapIngMntrQosShedPIR_Type()
)
tmnxAncpSapIngMntrQosShedPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapIngMntrQosShedPIR.setStatus("obsolete")
_TmnxAncpSapIngMntrAncpString_Type = TmnxAncpString
_TmnxAncpSapIngMntrAncpString_Object = MibTableColumn
tmnxAncpSapIngMntrAncpString = _TmnxAncpSapIngMntrAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 20, 1, 3),
    _TmnxAncpSapIngMntrAncpString_Type()
)
tmnxAncpSapIngMntrAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapIngMntrAncpString.setStatus("current")


class _TmnxAncpSapIngMntrQosShedPIRHi_Type(Unsigned32):
    """Custom type tmnxAncpSapIngMntrQosShedPIRHi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpSapIngMntrQosShedPIRHi_Type.__name__ = "Unsigned32"
_TmnxAncpSapIngMntrQosShedPIRHi_Object = MibTableColumn
tmnxAncpSapIngMntrQosShedPIRHi = _TmnxAncpSapIngMntrQosShedPIRHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 20, 1, 4),
    _TmnxAncpSapIngMntrQosShedPIRHi_Type()
)
tmnxAncpSapIngMntrQosShedPIRHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapIngMntrQosShedPIRHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpSapIngMntrQosShedPIRHi.setUnits("kbps")


class _TmnxAncpSapIngMntrQosShedPIRLo_Type(Unsigned32):
    """Custom type tmnxAncpSapIngMntrQosShedPIRLo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200000000),
        ValueRangeConstraint(4294967294, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpSapIngMntrQosShedPIRLo_Type.__name__ = "Unsigned32"
_TmnxAncpSapIngMntrQosShedPIRLo_Object = MibTableColumn
tmnxAncpSapIngMntrQosShedPIRLo = _TmnxAncpSapIngMntrQosShedPIRLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 20, 1, 5),
    _TmnxAncpSapIngMntrQosShedPIRLo_Type()
)
tmnxAncpSapIngMntrQosShedPIRLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapIngMntrQosShedPIRLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpSapIngMntrQosShedPIRLo.setUnits("kbps")
_TmnxAncpSapEgrSchedMonitorTable_Object = MibTable
tmnxAncpSapEgrSchedMonitorTable = _TmnxAncpSapEgrSchedMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 21)
)
if mibBuilder.loadTexts:
    tmnxAncpSapEgrSchedMonitorTable.setStatus("current")
_TmnxAncpSapEgrSchedMonitorEntry_Object = MibTableRow
tmnxAncpSapEgrSchedMonitorEntry = _TmnxAncpSapEgrSchedMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 21, 1)
)
tmnxAncpSapEgrSchedMonitorEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpSapEgrMntrQosShedName"),
)
if mibBuilder.loadTexts:
    tmnxAncpSapEgrSchedMonitorEntry.setStatus("current")
_TmnxAncpSapEgrMntrQosShedName_Type = TNamedItem
_TmnxAncpSapEgrMntrQosShedName_Object = MibTableColumn
tmnxAncpSapEgrMntrQosShedName = _TmnxAncpSapEgrMntrQosShedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 21, 1, 1),
    _TmnxAncpSapEgrMntrQosShedName_Type()
)
tmnxAncpSapEgrMntrQosShedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpSapEgrMntrQosShedName.setStatus("current")
_TmnxAncpSapEgrMntrQosShedPIR_Type = TPIRRateOverride
_TmnxAncpSapEgrMntrQosShedPIR_Object = MibTableColumn
tmnxAncpSapEgrMntrQosShedPIR = _TmnxAncpSapEgrMntrQosShedPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 21, 1, 2),
    _TmnxAncpSapEgrMntrQosShedPIR_Type()
)
tmnxAncpSapEgrMntrQosShedPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapEgrMntrQosShedPIR.setStatus("obsolete")
_TmnxAncpSapEgrMntrAncpString_Type = TmnxAncpString
_TmnxAncpSapEgrMntrAncpString_Object = MibTableColumn
tmnxAncpSapEgrMntrAncpString = _TmnxAncpSapEgrMntrAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 21, 1, 3),
    _TmnxAncpSapEgrMntrAncpString_Type()
)
tmnxAncpSapEgrMntrAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapEgrMntrAncpString.setStatus("current")


class _TmnxAncpSapEgrMntrQosShedPIRHi_Type(Unsigned32):
    """Custom type tmnxAncpSapEgrMntrQosShedPIRHi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpSapEgrMntrQosShedPIRHi_Type.__name__ = "Unsigned32"
_TmnxAncpSapEgrMntrQosShedPIRHi_Object = MibTableColumn
tmnxAncpSapEgrMntrQosShedPIRHi = _TmnxAncpSapEgrMntrQosShedPIRHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 21, 1, 4),
    _TmnxAncpSapEgrMntrQosShedPIRHi_Type()
)
tmnxAncpSapEgrMntrQosShedPIRHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapEgrMntrQosShedPIRHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpSapEgrMntrQosShedPIRHi.setUnits("kbps")


class _TmnxAncpSapEgrMntrQosShedPIRLo_Type(Unsigned32):
    """Custom type tmnxAncpSapEgrMntrQosShedPIRLo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200000000),
        ValueRangeConstraint(4294967294, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpSapEgrMntrQosShedPIRLo_Type.__name__ = "Unsigned32"
_TmnxAncpSapEgrMntrQosShedPIRLo_Object = MibTableColumn
tmnxAncpSapEgrMntrQosShedPIRLo = _TmnxAncpSapEgrMntrQosShedPIRLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 21, 1, 5),
    _TmnxAncpSapEgrMntrQosShedPIRLo_Type()
)
tmnxAncpSapEgrMntrQosShedPIRLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSapEgrMntrQosShedPIRLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpSapEgrMntrQosShedPIRLo.setUnits("kbps")
_TmnxAncpMssMonitorTable_Object = MibTable
tmnxAncpMssMonitorTable = _TmnxAncpMssMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 22)
)
if mibBuilder.loadTexts:
    tmnxAncpMssMonitorTable.setStatus("current")
_TmnxAncpMssMonitorEntry_Object = MibTableRow
tmnxAncpMssMonitorEntry = _TmnxAncpMssMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 22, 1)
)
tmnxAncpMssMonitorEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
)
if mibBuilder.loadTexts:
    tmnxAncpMssMonitorEntry.setStatus("current")
_TmnxAncpMssMntrEgrAggRateLimit_Type = TPIRAggRateLimitOverride
_TmnxAncpMssMntrEgrAggRateLimit_Object = MibTableColumn
tmnxAncpMssMntrEgrAggRateLimit = _TmnxAncpMssMntrEgrAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 22, 1, 1),
    _TmnxAncpMssMntrEgrAggRateLimit_Type()
)
tmnxAncpMssMntrEgrAggRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssMntrEgrAggRateLimit.setStatus("current")
_TmnxAncpMssMntrAncpString_Type = TmnxAncpString
_TmnxAncpMssMntrAncpString_Object = MibTableColumn
tmnxAncpMssMntrAncpString = _TmnxAncpMssMntrAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 22, 1, 2),
    _TmnxAncpMssMntrAncpString_Type()
)
tmnxAncpMssMntrAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssMntrAncpString.setStatus("current")
_TmnxAncpMssIngMonitorTable_Object = MibTable
tmnxAncpMssIngMonitorTable = _TmnxAncpMssIngMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 23)
)
if mibBuilder.loadTexts:
    tmnxAncpMssIngMonitorTable.setStatus("current")
_TmnxAncpMssIngMonitorEntry_Object = MibTableRow
tmnxAncpMssIngMonitorEntry = _TmnxAncpMssIngMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 23, 1)
)
tmnxAncpMssIngMonitorEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpMssIngMntrQosShedName"),
)
if mibBuilder.loadTexts:
    tmnxAncpMssIngMonitorEntry.setStatus("current")
_TmnxAncpMssIngMntrQosShedName_Type = TNamedItem
_TmnxAncpMssIngMntrQosShedName_Object = MibTableColumn
tmnxAncpMssIngMntrQosShedName = _TmnxAncpMssIngMntrQosShedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 23, 1, 1),
    _TmnxAncpMssIngMntrQosShedName_Type()
)
tmnxAncpMssIngMntrQosShedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpMssIngMntrQosShedName.setStatus("current")
_TmnxAncpMssIngMntrQosShedPIR_Type = TPIRRateOverride
_TmnxAncpMssIngMntrQosShedPIR_Object = MibTableColumn
tmnxAncpMssIngMntrQosShedPIR = _TmnxAncpMssIngMntrQosShedPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 23, 1, 2),
    _TmnxAncpMssIngMntrQosShedPIR_Type()
)
tmnxAncpMssIngMntrQosShedPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssIngMntrQosShedPIR.setStatus("obsolete")
_TmnxAncpMssIngMntrAncpString_Type = TmnxAncpString
_TmnxAncpMssIngMntrAncpString_Object = MibTableColumn
tmnxAncpMssIngMntrAncpString = _TmnxAncpMssIngMntrAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 23, 1, 3),
    _TmnxAncpMssIngMntrAncpString_Type()
)
tmnxAncpMssIngMntrAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssIngMntrAncpString.setStatus("current")


class _TmnxAncpMssIngMntrQosShedPIRHi_Type(Unsigned32):
    """Custom type tmnxAncpMssIngMntrQosShedPIRHi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpMssIngMntrQosShedPIRHi_Type.__name__ = "Unsigned32"
_TmnxAncpMssIngMntrQosShedPIRHi_Object = MibTableColumn
tmnxAncpMssIngMntrQosShedPIRHi = _TmnxAncpMssIngMntrQosShedPIRHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 23, 1, 4),
    _TmnxAncpMssIngMntrQosShedPIRHi_Type()
)
tmnxAncpMssIngMntrQosShedPIRHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssIngMntrQosShedPIRHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpMssIngMntrQosShedPIRHi.setUnits("kbps")


class _TmnxAncpMssIngMntrQosShedPIRLo_Type(Unsigned32):
    """Custom type tmnxAncpMssIngMntrQosShedPIRLo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200000000),
        ValueRangeConstraint(4294967294, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpMssIngMntrQosShedPIRLo_Type.__name__ = "Unsigned32"
_TmnxAncpMssIngMntrQosShedPIRLo_Object = MibTableColumn
tmnxAncpMssIngMntrQosShedPIRLo = _TmnxAncpMssIngMntrQosShedPIRLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 23, 1, 5),
    _TmnxAncpMssIngMntrQosShedPIRLo_Type()
)
tmnxAncpMssIngMntrQosShedPIRLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssIngMntrQosShedPIRLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpMssIngMntrQosShedPIRLo.setUnits("kbps")
_TmnxAncpMssEgrMonitorTable_Object = MibTable
tmnxAncpMssEgrMonitorTable = _TmnxAncpMssEgrMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 24)
)
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMonitorTable.setStatus("current")
_TmnxAncpMssEgrMonitorEntry_Object = MibTableRow
tmnxAncpMssEgrMonitorEntry = _TmnxAncpMssEgrMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 24, 1)
)
tmnxAncpMssEgrMonitorEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpMssEgrMntrQosShedName"),
)
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMonitorEntry.setStatus("current")
_TmnxAncpMssEgrMntrQosShedName_Type = TNamedItem
_TmnxAncpMssEgrMntrQosShedName_Object = MibTableColumn
tmnxAncpMssEgrMntrQosShedName = _TmnxAncpMssEgrMntrQosShedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 24, 1, 1),
    _TmnxAncpMssEgrMntrQosShedName_Type()
)
tmnxAncpMssEgrMntrQosShedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMntrQosShedName.setStatus("current")
_TmnxAncpMssEgrMntrQosShedPIR_Type = TPIRRateOverride
_TmnxAncpMssEgrMntrQosShedPIR_Object = MibTableColumn
tmnxAncpMssEgrMntrQosShedPIR = _TmnxAncpMssEgrMntrQosShedPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 24, 1, 2),
    _TmnxAncpMssEgrMntrQosShedPIR_Type()
)
tmnxAncpMssEgrMntrQosShedPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMntrQosShedPIR.setStatus("obsolete")
_TmnxAncpMssEgrMntrAncpString_Type = TmnxAncpString
_TmnxAncpMssEgrMntrAncpString_Object = MibTableColumn
tmnxAncpMssEgrMntrAncpString = _TmnxAncpMssEgrMntrAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 24, 1, 3),
    _TmnxAncpMssEgrMntrAncpString_Type()
)
tmnxAncpMssEgrMntrAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMntrAncpString.setStatus("current")


class _TmnxAncpMssEgrMntrQosShedPIRHi_Type(Unsigned32):
    """Custom type tmnxAncpMssEgrMntrQosShedPIRHi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpMssEgrMntrQosShedPIRHi_Type.__name__ = "Unsigned32"
_TmnxAncpMssEgrMntrQosShedPIRHi_Object = MibTableColumn
tmnxAncpMssEgrMntrQosShedPIRHi = _TmnxAncpMssEgrMntrQosShedPIRHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 24, 1, 4),
    _TmnxAncpMssEgrMntrQosShedPIRHi_Type()
)
tmnxAncpMssEgrMntrQosShedPIRHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMntrQosShedPIRHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMntrQosShedPIRHi.setUnits("kbps")


class _TmnxAncpMssEgrMntrQosShedPIRLo_Type(Unsigned32):
    """Custom type tmnxAncpMssEgrMntrQosShedPIRLo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200000000),
        ValueRangeConstraint(4294967294, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpMssEgrMntrQosShedPIRLo_Type.__name__ = "Unsigned32"
_TmnxAncpMssEgrMntrQosShedPIRLo_Object = MibTableColumn
tmnxAncpMssEgrMntrQosShedPIRLo = _TmnxAncpMssEgrMntrQosShedPIRLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 24, 1, 5),
    _TmnxAncpMssEgrMntrQosShedPIRLo_Type()
)
tmnxAncpMssEgrMntrQosShedPIRLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMntrQosShedPIRLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpMssEgrMntrQosShedPIRLo.setUnits("kbps")
_TmnxAncpSubMonitorTable_Object = MibTable
tmnxAncpSubMonitorTable = _TmnxAncpSubMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25)
)
if mibBuilder.loadTexts:
    tmnxAncpSubMonitorTable.setStatus("current")
_TmnxAncpSubMonitorEntry_Object = MibTableRow
tmnxAncpSubMonitorEntry = _TmnxAncpSubMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1)
)
tmnxAncpSubMonitorEntry.setIndexNames(
    (1, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
)
if mibBuilder.loadTexts:
    tmnxAncpSubMonitorEntry.setStatus("current")
_TmnxAncpSubMntrIngQosShedName_Type = TNamedItem
_TmnxAncpSubMntrIngQosShedName_Object = MibTableColumn
tmnxAncpSubMntrIngQosShedName = _TmnxAncpSubMntrIngQosShedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 1),
    _TmnxAncpSubMntrIngQosShedName_Type()
)
tmnxAncpSubMntrIngQosShedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrIngQosShedName.setStatus("current")
_TmnxAncpSubMntrIngQosShedPIR_Type = TPIRRateOverride
_TmnxAncpSubMntrIngQosShedPIR_Object = MibTableColumn
tmnxAncpSubMntrIngQosShedPIR = _TmnxAncpSubMntrIngQosShedPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 2),
    _TmnxAncpSubMntrIngQosShedPIR_Type()
)
tmnxAncpSubMntrIngQosShedPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrIngQosShedPIR.setStatus("obsolete")
_TmnxAncpSubMntrEgrQosShedName_Type = TNamedItem
_TmnxAncpSubMntrEgrQosShedName_Object = MibTableColumn
tmnxAncpSubMntrEgrQosShedName = _TmnxAncpSubMntrEgrQosShedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 3),
    _TmnxAncpSubMntrEgrQosShedName_Type()
)
tmnxAncpSubMntrEgrQosShedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrEgrQosShedName.setStatus("current")
_TmnxAncpSubMntrEgrQosShedPIR_Type = TPIRRateOverride
_TmnxAncpSubMntrEgrQosShedPIR_Object = MibTableColumn
tmnxAncpSubMntrEgrQosShedPIR = _TmnxAncpSubMntrEgrQosShedPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 4),
    _TmnxAncpSubMntrEgrQosShedPIR_Type()
)
tmnxAncpSubMntrEgrQosShedPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrEgrQosShedPIR.setStatus("obsolete")
_TmnxAncpSubMntrEgrAggRateLimit_Type = TPIRAggRateLimitOverride
_TmnxAncpSubMntrEgrAggRateLimit_Object = MibTableColumn
tmnxAncpSubMntrEgrAggRateLimit = _TmnxAncpSubMntrEgrAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 5),
    _TmnxAncpSubMntrEgrAggRateLimit_Type()
)
tmnxAncpSubMntrEgrAggRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrEgrAggRateLimit.setStatus("current")


class _TmnxAncpSubMntrIngQosShedPIRHi_Type(Unsigned32):
    """Custom type tmnxAncpSubMntrIngQosShedPIRHi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpSubMntrIngQosShedPIRHi_Type.__name__ = "Unsigned32"
_TmnxAncpSubMntrIngQosShedPIRHi_Object = MibTableColumn
tmnxAncpSubMntrIngQosShedPIRHi = _TmnxAncpSubMntrIngQosShedPIRHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 6),
    _TmnxAncpSubMntrIngQosShedPIRHi_Type()
)
tmnxAncpSubMntrIngQosShedPIRHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrIngQosShedPIRHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrIngQosShedPIRHi.setUnits("kbps")


class _TmnxAncpSubMntrIngQosShedPIRLo_Type(Unsigned32):
    """Custom type tmnxAncpSubMntrIngQosShedPIRLo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200000000),
        ValueRangeConstraint(4294967294, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpSubMntrIngQosShedPIRLo_Type.__name__ = "Unsigned32"
_TmnxAncpSubMntrIngQosShedPIRLo_Object = MibTableColumn
tmnxAncpSubMntrIngQosShedPIRLo = _TmnxAncpSubMntrIngQosShedPIRLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 7),
    _TmnxAncpSubMntrIngQosShedPIRLo_Type()
)
tmnxAncpSubMntrIngQosShedPIRLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrIngQosShedPIRLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrIngQosShedPIRLo.setUnits("kbps")


class _TmnxAncpSubMntrEgrQosShedPIRHi_Type(Unsigned32):
    """Custom type tmnxAncpSubMntrEgrQosShedPIRHi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpSubMntrEgrQosShedPIRHi_Type.__name__ = "Unsigned32"
_TmnxAncpSubMntrEgrQosShedPIRHi_Object = MibTableColumn
tmnxAncpSubMntrEgrQosShedPIRHi = _TmnxAncpSubMntrEgrQosShedPIRHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 8),
    _TmnxAncpSubMntrEgrQosShedPIRHi_Type()
)
tmnxAncpSubMntrEgrQosShedPIRHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrEgrQosShedPIRHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrEgrQosShedPIRHi.setUnits("kbps")


class _TmnxAncpSubMntrEgrQosShedPIRLo_Type(Unsigned32):
    """Custom type tmnxAncpSubMntrEgrQosShedPIRLo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3200000000),
        ValueRangeConstraint(4294967294, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxAncpSubMntrEgrQosShedPIRLo_Type.__name__ = "Unsigned32"
_TmnxAncpSubMntrEgrQosShedPIRLo_Object = MibTableColumn
tmnxAncpSubMntrEgrQosShedPIRLo = _TmnxAncpSubMntrEgrQosShedPIRLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 25, 1, 9),
    _TmnxAncpSubMntrEgrQosShedPIRLo_Type()
)
tmnxAncpSubMntrEgrQosShedPIRLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrEgrQosShedPIRLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxAncpSubMntrEgrQosShedPIRLo.setUnits("kbps")
_TmnxAncpStringDslLineInfoTable_Object = MibTable
tmnxAncpStringDslLineInfoTable = _TmnxAncpStringDslLineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 26)
)
if mibBuilder.loadTexts:
    tmnxAncpStringDslLineInfoTable.setStatus("current")
_TmnxAncpStringDslLineInfoEntry_Object = MibTableRow
tmnxAncpStringDslLineInfoEntry = _TmnxAncpStringDslLineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 26, 1)
)
tmnxAncpStringDslLineInfoEntry.setIndexNames(
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpStringLineInfoAncpString"),
    (0, "TIMETRA-GSMP-MIB", "tmnxAncpStringLineInfoType"),
)
if mibBuilder.loadTexts:
    tmnxAncpStringDslLineInfoEntry.setStatus("current")
_TmnxAncpStringLineInfoAncpString_Type = TmnxAncpString
_TmnxAncpStringLineInfoAncpString_Object = MibTableColumn
tmnxAncpStringLineInfoAncpString = _TmnxAncpStringLineInfoAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 26, 1, 1),
    _TmnxAncpStringLineInfoAncpString_Type()
)
tmnxAncpStringLineInfoAncpString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpStringLineInfoAncpString.setStatus("current")


class _TmnxAncpStringLineInfoType_Type(Integer32):
    """Custom type tmnxAncpStringLineInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145)
        )
    )
    namedValues = NamedValues(
        *(("actualNetDataRateUpstream", 129),
          ("actualNetDataRateDownstream", 130),
          ("minimumNetDataRateUpstream", 131),
          ("minimumNetDataRateDownstream", 132),
          ("attainableNetDataRateUpstream", 133),
          ("attainableNetDataRateDownstream", 134),
          ("maximumNetDataRateUpstream", 135),
          ("maximumNetDataRateDownstream", 136),
          ("minimumNetLowPowerDataRateUpstream", 137),
          ("minimumNetLowPowerDataRateDownstream", 138),
          ("maximumInterleavingDelayUpstream", 139),
          ("actualInterleavingDelayUpstream", 140),
          ("maximumInterleavingDelayDownstream", 141),
          ("actualInterleavingDelayDownstream", 142),
          ("dslLineState", 143),
          ("accessLoopEncapsulation", 144),
          ("dslType", 145))
    )


_TmnxAncpStringLineInfoType_Type.__name__ = "Integer32"
_TmnxAncpStringLineInfoType_Object = MibTableColumn
tmnxAncpStringLineInfoType = _TmnxAncpStringLineInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 26, 1, 2),
    _TmnxAncpStringLineInfoType_Type()
)
tmnxAncpStringLineInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxAncpStringLineInfoType.setStatus("current")
_TmnxAncpStringLineInfoValue_Type = Unsigned32
_TmnxAncpStringLineInfoValue_Object = MibTableColumn
tmnxAncpStringLineInfoValue = _TmnxAncpStringLineInfoValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 39, 26, 1, 3),
    _TmnxAncpStringLineInfoValue_Type()
)
tmnxAncpStringLineInfoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxAncpStringLineInfoValue.setStatus("current")
_TmnxGsmpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxGsmpNotifyPrefix = _TmnxGsmpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 39)
)
_TmnxGsmpNotifications_ObjectIdentity = ObjectIdentity
tmnxGsmpNotifications = _TmnxGsmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 39, 0)
)
tmnxSubProfileEntry.registerAugmentions(
    ("TIMETRA-GSMP-MIB",
     "tmnxAncpSubProfileEntry")
)
tmnxAncpSubProfileEntry.setIndexNames(*tmnxSubProfileEntry.getIndexNames())

# Managed Objects groups

tmnxGsmpV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 2, 1)
)
tmnxGsmpV5v0Group.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxGsmpConfigTableLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGroupConfigTableLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGroupNbrTableLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapTblLastChg"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssTblLastChg"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubProfileTblLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPolicyTableLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpCfgLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpCfgAdminState"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgAdminState"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgKeepalive"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgHoldMultiplier"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgDescription"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgAncpOamCap"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgAncpDynTopoDiscCap"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrAdminState"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrLocalAddrType"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrLocalAddr"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrDescription"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrPrioMarkType"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrPrioMarkPrec"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrPrioMarkDscp"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapAncpPolName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssAncpPolName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubProfileAncpPolicy"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateAdjustment"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateReduction"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateMonitor"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateMonitorNtf"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateModType"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateModSched"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateAdjustment"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateReduction"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateMonitor"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateMonitorNtf"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateModType"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateModSched"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyDisableShcv"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyDisableShcvHldTime"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyDisableShcvNtf"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfAssociation"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfSapPortId"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfSapEncapValue"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfMultSvcSiteName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfMultSvcSiteCust"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfSubscrIdent"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfLineState"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfAncpPolicyName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfIngrRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfAdjustedIngrRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfEgrRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfAdjustedEgrRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfServId"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfNeighborAddrType"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfNeighborAddr"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfTcpPort"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfGroupName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrPeerInstance"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrPeerPort"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrPeerName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesSenderInstance"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesSenderPort"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesSenderName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrTimeouts"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrMaxNbrOfTimeouts"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrTimer"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesSenderTimer"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNegotiatedCaps"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesConfiguredCaps"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesGroupName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesState"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesLocalAddrType"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesLocalAddr"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatLastChanged"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxDrop"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxDrop"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxSyn"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxSyn"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxSynAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxSynAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxRstAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxRstAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxPortUp"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxPortUp"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxPortDown"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxPortDown"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxLoopback"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxLoopback"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapMntrEgrAggRateLimit"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapIngMntrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapIngMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapEgrMntrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapEgrMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssMntrEgrAggRateLimit"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssIngMntrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssIngMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssEgrMntrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssEgrMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrIngQosShedName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrIngQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrEgrQosShedName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrEgrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrEgrAggRateLimit"))
)
if mibBuilder.loadTexts:
    tmnxGsmpV5v0Group.setStatus("obsolete")

tmnxGsmpNotificationObjV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 2, 3)
)
tmnxGsmpNotificationObjV5v0Group.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxNotifAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxNotifAncpPolicyName"),
        ("TIMETRA-GSMP-MIB", "tmnxNotifAncpPlcyActualRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpRejectReason"))
)
if mibBuilder.loadTexts:
    tmnxGsmpNotificationObjV5v0Group.setStatus("current")

tmnxGsmpV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 2, 4)
)
tmnxGsmpV11v0Group.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxGsmpConfigTableLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGroupConfigTableLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGroupNbrTableLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapTblLastChg"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssTblLastChg"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubProfileTblLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPolicyTableLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpCfgLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpCfgAdminState"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgAdminState"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgKeepalive"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgHoldMultiplier"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgDescription"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgAncpOamCap"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgAncpDynTopoDiscCap"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrAdminState"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrLocalAddrType"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrLocalAddr"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrDescription"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrPrioMarkType"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrPrioMarkPrec"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpNbrPrioMarkDscp"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapSapAncpPolName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStaticMapMssAncpPolName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubProfileAncpPolicy"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyLastChange"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyRowStatus"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateAdjustment"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateReduction"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateMonitor"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateMonitorNtf"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateModType"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyIngRateModSched"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateAdjustment"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateReduction"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateMonitor"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateMonitorNtf"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateModType"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyEgrRateModSched"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyDisableShcv"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyDisableShcvHldTime"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpPlcyDisableShcvNtf"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfAssociation"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfSapPortId"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfSapEncapValue"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfMultSvcSiteName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfMultSvcSiteCust"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfSubscrIdent"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfLineState"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfAncpPolicyName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfIngrRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfAdjustedIngrRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfEgrRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfAdjustedEgrRate"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfServId"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfNeighborAddrType"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfNeighborAddr"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfTcpPort"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfGroupName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrPeerInstance"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrPeerPort"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrPeerName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesSenderInstance"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesSenderPort"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesSenderName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrTimeouts"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrMaxNbrOfTimeouts"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNbrTimer"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesSenderTimer"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesNegotiatedCaps"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesConfiguredCaps"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesGroupName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesState"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesLocalAddrType"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesLocalAddr"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatLastChanged"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxDrop"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxDrop"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxSyn"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxSyn"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxSynAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxSynAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxRstAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxRstAck"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxPortUp"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxPortUp"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxPortDown"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxPortDown"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatRxLoopback"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesStatTxLoopback"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapMntrEgrAggRateLimit"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapIngMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapEgrMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssMntrEgrAggRateLimit"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssIngMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssEgrMntrAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrIngQosShedName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrEgrQosShedName"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrEgrAggRateLimit"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesVersion"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesPartitionID"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgPersistencyDb"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpGrpCfgIdleFilter"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStringLineInfoValue"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStrInfPersistKey"))
)
if mibBuilder.loadTexts:
    tmnxGsmpV11v0Group.setStatus("current")

tmnxGsmpSchedulerRateV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 2, 5)
)
tmnxGsmpSchedulerRateV11v0Group.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxAncpSapIngMntrQosShedPIRHi"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapIngMntrQosShedPIRLo"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapEgrMntrQosShedPIRHi"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapEgrMntrQosShedPIRLo"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssIngMntrQosShedPIRHi"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssIngMntrQosShedPIRLo"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssEgrMntrQosShedPIRHi"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssEgrMntrQosShedPIRLo"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrIngQosShedPIRHi"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrIngQosShedPIRLo"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrEgrQosShedPIRHi"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrEgrQosShedPIRLo"))
)
if mibBuilder.loadTexts:
    tmnxGsmpSchedulerRateV11v0Group.setStatus("current")

tmnxGsmpObsoletedV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 2, 6)
)
tmnxGsmpObsoletedV11v0Group.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxAncpMssIngMntrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpMssEgrMntrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapIngMntrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSapEgrMntrQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrIngQosShedPIR"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSubMntrEgrQosShedPIR"))
)
if mibBuilder.loadTexts:
    tmnxGsmpObsoletedV11v0Group.setStatus("current")


# Notification objects

tmnxAncpIngRateMonitorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 39, 0, 1)
)
tmnxAncpIngRateMonitorEvent.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxNotifAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxNotifAncpPolicyName"),
        ("TIMETRA-GSMP-MIB", "tmnxNotifAncpPlcyActualRate"))
)
if mibBuilder.loadTexts:
    tmnxAncpIngRateMonitorEvent.setStatus(
        "current"
    )

tmnxAncpEgrRateMonitorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 39, 0, 2)
)
tmnxAncpEgrRateMonitorEvent.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxNotifAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxNotifAncpPolicyName"),
        ("TIMETRA-GSMP-MIB", "tmnxNotifAncpPlcyActualRate"))
)
if mibBuilder.loadTexts:
    tmnxAncpEgrRateMonitorEvent.setStatus(
        "current"
    )

tmnxAncpShcvDisabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 39, 0, 3)
)
tmnxAncpShcvDisabledEvent.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxNotifAncpString"),
        ("TIMETRA-GSMP-MIB", "tmnxNotifAncpPolicyName"))
)
if mibBuilder.loadTexts:
    tmnxAncpShcvDisabledEvent.setStatus(
        "current"
    )

tmnxAncpSesRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 39, 0, 4)
)
tmnxAncpSesRejected.setObjects(
    ("TIMETRA-GSMP-MIB", "tmnxAncpRejectReason")
)
if mibBuilder.loadTexts:
    tmnxAncpSesRejected.setStatus(
        "current"
    )

tmnxAncpStringRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 39, 0, 5)
)
tmnxAncpStringRejected.setObjects(
    ("TIMETRA-GSMP-MIB", "tmnxAncpRejectReason")
)
if mibBuilder.loadTexts:
    tmnxAncpStringRejected.setStatus(
        "current"
    )


# Notifications groups

tmnxGsmpV5v0GNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 2, 2)
)
tmnxGsmpV5v0GNotificationGroup.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxAncpIngRateMonitorEvent"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpEgrRateMonitorEvent"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpShcvDisabledEvent"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpSesRejected"),
        ("TIMETRA-GSMP-MIB", "tmnxAncpStringRejected"))
)
if mibBuilder.loadTexts:
    tmnxGsmpV5v0GNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxGsmpV5v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 1, 1)
)
tmnxGsmpV5v0MIBCompliance.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxGsmpV5v0Group"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpV5v0GNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxGsmpV5v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxGsmpV11v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 39, 1, 2)
)
tmnxGsmpV11v0MIBCompliance.setObjects(
      *(("TIMETRA-GSMP-MIB", "tmnxGsmpV11v0Group"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpV5v0GNotificationGroup"),
        ("TIMETRA-GSMP-MIB", "tmnxGsmpSchedulerRateV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxGsmpV11v0MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-GSMP-MIB",
    **{"tmnxGsmpMIBModule": tmnxGsmpMIBModule,
       "tmnxGsmpCompliance": tmnxGsmpCompliance,
       "tmnxGsmpCompliances": tmnxGsmpCompliances,
       "tmnxGsmpV5v0MIBCompliance": tmnxGsmpV5v0MIBCompliance,
       "tmnxGsmpV11v0MIBCompliance": tmnxGsmpV11v0MIBCompliance,
       "tmnxGsmpGroups": tmnxGsmpGroups,
       "tmnxGsmpV5v0Group": tmnxGsmpV5v0Group,
       "tmnxGsmpV5v0GNotificationGroup": tmnxGsmpV5v0GNotificationGroup,
       "tmnxGsmpNotificationObjV5v0Group": tmnxGsmpNotificationObjV5v0Group,
       "tmnxGsmpV11v0Group": tmnxGsmpV11v0Group,
       "tmnxGsmpSchedulerRateV11v0Group": tmnxGsmpSchedulerRateV11v0Group,
       "tmnxGsmpObsoletedV11v0Group": tmnxGsmpObsoletedV11v0Group,
       "tmnxGsmpObjects": tmnxGsmpObjects,
       "tmnxGsmpNotifyObjects": tmnxGsmpNotifyObjects,
       "tmnxNotifAncpString": tmnxNotifAncpString,
       "tmnxNotifAncpPolicyName": tmnxNotifAncpPolicyName,
       "tmnxNotifAncpPlcyActualRate": tmnxNotifAncpPlcyActualRate,
       "tmnxAncpRejectReason": tmnxAncpRejectReason,
       "tmnxGsmpConfigTableLastChange": tmnxGsmpConfigTableLastChange,
       "tmnxGsmpConfigTable": tmnxGsmpConfigTable,
       "tmnxGsmpConfigEntry": tmnxGsmpConfigEntry,
       "tmnxGsmpCfgLastChange": tmnxGsmpCfgLastChange,
       "tmnxGsmpCfgAdminState": tmnxGsmpCfgAdminState,
       "tmnxGsmpGroupConfigTableLastChange": tmnxGsmpGroupConfigTableLastChange,
       "tmnxGsmpGroupConfigTable": tmnxGsmpGroupConfigTable,
       "tmnxGsmpGroupConfigEntry": tmnxGsmpGroupConfigEntry,
       "tmnxGsmpGroupName": tmnxGsmpGroupName,
       "tmnxGsmpGrpCfgLastChange": tmnxGsmpGrpCfgLastChange,
       "tmnxGsmpGrpCfgRowStatus": tmnxGsmpGrpCfgRowStatus,
       "tmnxGsmpGrpCfgAdminState": tmnxGsmpGrpCfgAdminState,
       "tmnxGsmpGrpCfgKeepalive": tmnxGsmpGrpCfgKeepalive,
       "tmnxGsmpGrpCfgHoldMultiplier": tmnxGsmpGrpCfgHoldMultiplier,
       "tmnxGsmpGrpCfgDescription": tmnxGsmpGrpCfgDescription,
       "tmnxGsmpGrpCfgAncpOamCap": tmnxGsmpGrpCfgAncpOamCap,
       "tmnxGsmpGrpCfgAncpDynTopoDiscCap": tmnxGsmpGrpCfgAncpDynTopoDiscCap,
       "tmnxGsmpGrpCfgPersistencyDb": tmnxGsmpGrpCfgPersistencyDb,
       "tmnxGsmpGrpCfgIdleFilter": tmnxGsmpGrpCfgIdleFilter,
       "tmnxGsmpGroupNbrTableLastChange": tmnxGsmpGroupNbrTableLastChange,
       "tmnxGsmpGroupNeighborTable": tmnxGsmpGroupNeighborTable,
       "tmnxGsmpGroupNeighborEntry": tmnxGsmpGroupNeighborEntry,
       "tmnxGsmpGrpNbrAddressType": tmnxGsmpGrpNbrAddressType,
       "tmnxGsmpGrpNbrAddress": tmnxGsmpGrpNbrAddress,
       "tmnxGsmpGrpNbrLastChange": tmnxGsmpGrpNbrLastChange,
       "tmnxGsmpGrpNbrRowStatus": tmnxGsmpGrpNbrRowStatus,
       "tmnxGsmpGrpNbrAdminState": tmnxGsmpGrpNbrAdminState,
       "tmnxGsmpGrpNbrLocalAddrType": tmnxGsmpGrpNbrLocalAddrType,
       "tmnxGsmpGrpNbrLocalAddr": tmnxGsmpGrpNbrLocalAddr,
       "tmnxGsmpGrpNbrDescription": tmnxGsmpGrpNbrDescription,
       "tmnxGsmpGrpNbrPrioMarkType": tmnxGsmpGrpNbrPrioMarkType,
       "tmnxGsmpGrpNbrPrioMarkPrec": tmnxGsmpGrpNbrPrioMarkPrec,
       "tmnxGsmpGrpNbrPrioMarkDscp": tmnxGsmpGrpNbrPrioMarkDscp,
       "tmnxAncpStaticMapSapTblLastChg": tmnxAncpStaticMapSapTblLastChg,
       "tmnxAncpStaticMapSapTable": tmnxAncpStaticMapSapTable,
       "tmnxAncpStaticMapSapEntry": tmnxAncpStaticMapSapEntry,
       "tmnxAncpStaticMapSapString": tmnxAncpStaticMapSapString,
       "tmnxAncpStaticMapSapLastChange": tmnxAncpStaticMapSapLastChange,
       "tmnxAncpStaticMapSapRowStatus": tmnxAncpStaticMapSapRowStatus,
       "tmnxAncpStaticMapSapAncpPolName": tmnxAncpStaticMapSapAncpPolName,
       "tmnxAncpStaticMapMssTblLastChg": tmnxAncpStaticMapMssTblLastChg,
       "tmnxAncpStaticMapMssTable": tmnxAncpStaticMapMssTable,
       "tmnxAncpStaticMapMssEntry": tmnxAncpStaticMapMssEntry,
       "tmnxAncpStaticMapMssString": tmnxAncpStaticMapMssString,
       "tmnxAncpStaticMapMssLastChange": tmnxAncpStaticMapMssLastChange,
       "tmnxAncpStaticMapMssRowStatus": tmnxAncpStaticMapMssRowStatus,
       "tmnxAncpStaticMapMssAncpPolName": tmnxAncpStaticMapMssAncpPolName,
       "tmnxAncpSubProfileTblLastChange": tmnxAncpSubProfileTblLastChange,
       "tmnxAncpSubProfileTable": tmnxAncpSubProfileTable,
       "tmnxAncpSubProfileEntry": tmnxAncpSubProfileEntry,
       "tmnxAncpSubProfileAncpPolicy": tmnxAncpSubProfileAncpPolicy,
       "tmnxAncpPolicyTableLastChange": tmnxAncpPolicyTableLastChange,
       "tmnxAncpPolicyTable": tmnxAncpPolicyTable,
       "tmnxAncpPolicyEntry": tmnxAncpPolicyEntry,
       "tmnxAncpPolicyName": tmnxAncpPolicyName,
       "tmnxAncpPlcyLastChange": tmnxAncpPlcyLastChange,
       "tmnxAncpPlcyRowStatus": tmnxAncpPlcyRowStatus,
       "tmnxAncpPlcyIngRateAdjustment": tmnxAncpPlcyIngRateAdjustment,
       "tmnxAncpPlcyIngRateReduction": tmnxAncpPlcyIngRateReduction,
       "tmnxAncpPlcyIngRateMonitor": tmnxAncpPlcyIngRateMonitor,
       "tmnxAncpPlcyIngRateMonitorNtf": tmnxAncpPlcyIngRateMonitorNtf,
       "tmnxAncpPlcyIngRateModType": tmnxAncpPlcyIngRateModType,
       "tmnxAncpPlcyIngRateModSched": tmnxAncpPlcyIngRateModSched,
       "tmnxAncpPlcyEgrRateAdjustment": tmnxAncpPlcyEgrRateAdjustment,
       "tmnxAncpPlcyEgrRateReduction": tmnxAncpPlcyEgrRateReduction,
       "tmnxAncpPlcyEgrRateMonitor": tmnxAncpPlcyEgrRateMonitor,
       "tmnxAncpPlcyEgrRateMonitorNtf": tmnxAncpPlcyEgrRateMonitorNtf,
       "tmnxAncpPlcyEgrRateModType": tmnxAncpPlcyEgrRateModType,
       "tmnxAncpPlcyEgrRateModSched": tmnxAncpPlcyEgrRateModSched,
       "tmnxAncpPlcyDisableShcv": tmnxAncpPlcyDisableShcv,
       "tmnxAncpPlcyDisableShcvHldTime": tmnxAncpPlcyDisableShcvHldTime,
       "tmnxAncpPlcyDisableShcvNtf": tmnxAncpPlcyDisableShcvNtf,
       "tmnxAncpStringInfoTable": tmnxAncpStringInfoTable,
       "tmnxAncpStringInfoEntry": tmnxAncpStringInfoEntry,
       "tmnxAncpStrInfAncpString": tmnxAncpStrInfAncpString,
       "tmnxAncpStrInfAssociation": tmnxAncpStrInfAssociation,
       "tmnxAncpStrInfSapPortId": tmnxAncpStrInfSapPortId,
       "tmnxAncpStrInfSapEncapValue": tmnxAncpStrInfSapEncapValue,
       "tmnxAncpStrInfMultSvcSiteName": tmnxAncpStrInfMultSvcSiteName,
       "tmnxAncpStrInfMultSvcSiteCust": tmnxAncpStrInfMultSvcSiteCust,
       "tmnxAncpStrInfSubscrIdent": tmnxAncpStrInfSubscrIdent,
       "tmnxAncpStrInfLineState": tmnxAncpStrInfLineState,
       "tmnxAncpStrInfAncpPolicyName": tmnxAncpStrInfAncpPolicyName,
       "tmnxAncpStrInfIngrRate": tmnxAncpStrInfIngrRate,
       "tmnxAncpStrInfAdjustedIngrRate": tmnxAncpStrInfAdjustedIngrRate,
       "tmnxAncpStrInfEgrRate": tmnxAncpStrInfEgrRate,
       "tmnxAncpStrInfAdjustedEgrRate": tmnxAncpStrInfAdjustedEgrRate,
       "tmnxAncpStrInfServId": tmnxAncpStrInfServId,
       "tmnxAncpStrInfNeighborAddrType": tmnxAncpStrInfNeighborAddrType,
       "tmnxAncpStrInfNeighborAddr": tmnxAncpStrInfNeighborAddr,
       "tmnxAncpStrInfTcpPort": tmnxAncpStrInfTcpPort,
       "tmnxAncpStrInfGroupName": tmnxAncpStrInfGroupName,
       "tmnxAncpStrInfPersistKey": tmnxAncpStrInfPersistKey,
       "tmnxAncpSessionTable": tmnxAncpSessionTable,
       "tmnxAncpSessionEntry": tmnxAncpSessionEntry,
       "tmnxAncpSesServiceId": tmnxAncpSesServiceId,
       "tmnxAncpSesNbrAddressType": tmnxAncpSesNbrAddressType,
       "tmnxAncpSesNbrAddress": tmnxAncpSesNbrAddress,
       "tmnxAncpSesNbrTcpPort": tmnxAncpSesNbrTcpPort,
       "tmnxAncpSesNbrPeerInstance": tmnxAncpSesNbrPeerInstance,
       "tmnxAncpSesNbrPeerPort": tmnxAncpSesNbrPeerPort,
       "tmnxAncpSesNbrPeerName": tmnxAncpSesNbrPeerName,
       "tmnxAncpSesSenderInstance": tmnxAncpSesSenderInstance,
       "tmnxAncpSesSenderPort": tmnxAncpSesSenderPort,
       "tmnxAncpSesSenderName": tmnxAncpSesSenderName,
       "tmnxAncpSesNbrTimeouts": tmnxAncpSesNbrTimeouts,
       "tmnxAncpSesNbrMaxNbrOfTimeouts": tmnxAncpSesNbrMaxNbrOfTimeouts,
       "tmnxAncpSesNbrTimer": tmnxAncpSesNbrTimer,
       "tmnxAncpSesSenderTimer": tmnxAncpSesSenderTimer,
       "tmnxAncpSesNegotiatedCaps": tmnxAncpSesNegotiatedCaps,
       "tmnxAncpSesConfiguredCaps": tmnxAncpSesConfiguredCaps,
       "tmnxAncpSesGroupName": tmnxAncpSesGroupName,
       "tmnxAncpSesState": tmnxAncpSesState,
       "tmnxAncpSesLocalAddrType": tmnxAncpSesLocalAddrType,
       "tmnxAncpSesLocalAddr": tmnxAncpSesLocalAddr,
       "tmnxAncpSesVersion": tmnxAncpSesVersion,
       "tmnxAncpSesPartitionID": tmnxAncpSesPartitionID,
       "tmnxAncpSessionStatsTable": tmnxAncpSessionStatsTable,
       "tmnxAncpSessionStatsEntry": tmnxAncpSessionStatsEntry,
       "tmnxAncpSesStatLastChanged": tmnxAncpSesStatLastChanged,
       "tmnxAncpSesStatRxDrop": tmnxAncpSesStatRxDrop,
       "tmnxAncpSesStatTxDrop": tmnxAncpSesStatTxDrop,
       "tmnxAncpSesStatRxSyn": tmnxAncpSesStatRxSyn,
       "tmnxAncpSesStatTxSyn": tmnxAncpSesStatTxSyn,
       "tmnxAncpSesStatRxSynAck": tmnxAncpSesStatRxSynAck,
       "tmnxAncpSesStatTxSynAck": tmnxAncpSesStatTxSynAck,
       "tmnxAncpSesStatRxAck": tmnxAncpSesStatRxAck,
       "tmnxAncpSesStatTxAck": tmnxAncpSesStatTxAck,
       "tmnxAncpSesStatRxRstAck": tmnxAncpSesStatRxRstAck,
       "tmnxAncpSesStatTxRstAck": tmnxAncpSesStatTxRstAck,
       "tmnxAncpSesStatRxPortUp": tmnxAncpSesStatRxPortUp,
       "tmnxAncpSesStatTxPortUp": tmnxAncpSesStatTxPortUp,
       "tmnxAncpSesStatRxPortDown": tmnxAncpSesStatRxPortDown,
       "tmnxAncpSesStatTxPortDown": tmnxAncpSesStatTxPortDown,
       "tmnxAncpSesStatRxLoopback": tmnxAncpSesStatRxLoopback,
       "tmnxAncpSesStatTxLoopback": tmnxAncpSesStatTxLoopback,
       "tmnxAncpSapMonitorTable": tmnxAncpSapMonitorTable,
       "tmnxAncpSapMonitorEntry": tmnxAncpSapMonitorEntry,
       "tmnxAncpSapMntrEgrAggRateLimit": tmnxAncpSapMntrEgrAggRateLimit,
       "tmnxAncpSapMntrAncpString": tmnxAncpSapMntrAncpString,
       "tmnxAncpSapIngSchedMonitorTable": tmnxAncpSapIngSchedMonitorTable,
       "tmnxAncpSapIngSchedMonitorEntry": tmnxAncpSapIngSchedMonitorEntry,
       "tmnxAncpSapIngMntrQosShedName": tmnxAncpSapIngMntrQosShedName,
       "tmnxAncpSapIngMntrQosShedPIR": tmnxAncpSapIngMntrQosShedPIR,
       "tmnxAncpSapIngMntrAncpString": tmnxAncpSapIngMntrAncpString,
       "tmnxAncpSapIngMntrQosShedPIRHi": tmnxAncpSapIngMntrQosShedPIRHi,
       "tmnxAncpSapIngMntrQosShedPIRLo": tmnxAncpSapIngMntrQosShedPIRLo,
       "tmnxAncpSapEgrSchedMonitorTable": tmnxAncpSapEgrSchedMonitorTable,
       "tmnxAncpSapEgrSchedMonitorEntry": tmnxAncpSapEgrSchedMonitorEntry,
       "tmnxAncpSapEgrMntrQosShedName": tmnxAncpSapEgrMntrQosShedName,
       "tmnxAncpSapEgrMntrQosShedPIR": tmnxAncpSapEgrMntrQosShedPIR,
       "tmnxAncpSapEgrMntrAncpString": tmnxAncpSapEgrMntrAncpString,
       "tmnxAncpSapEgrMntrQosShedPIRHi": tmnxAncpSapEgrMntrQosShedPIRHi,
       "tmnxAncpSapEgrMntrQosShedPIRLo": tmnxAncpSapEgrMntrQosShedPIRLo,
       "tmnxAncpMssMonitorTable": tmnxAncpMssMonitorTable,
       "tmnxAncpMssMonitorEntry": tmnxAncpMssMonitorEntry,
       "tmnxAncpMssMntrEgrAggRateLimit": tmnxAncpMssMntrEgrAggRateLimit,
       "tmnxAncpMssMntrAncpString": tmnxAncpMssMntrAncpString,
       "tmnxAncpMssIngMonitorTable": tmnxAncpMssIngMonitorTable,
       "tmnxAncpMssIngMonitorEntry": tmnxAncpMssIngMonitorEntry,
       "tmnxAncpMssIngMntrQosShedName": tmnxAncpMssIngMntrQosShedName,
       "tmnxAncpMssIngMntrQosShedPIR": tmnxAncpMssIngMntrQosShedPIR,
       "tmnxAncpMssIngMntrAncpString": tmnxAncpMssIngMntrAncpString,
       "tmnxAncpMssIngMntrQosShedPIRHi": tmnxAncpMssIngMntrQosShedPIRHi,
       "tmnxAncpMssIngMntrQosShedPIRLo": tmnxAncpMssIngMntrQosShedPIRLo,
       "tmnxAncpMssEgrMonitorTable": tmnxAncpMssEgrMonitorTable,
       "tmnxAncpMssEgrMonitorEntry": tmnxAncpMssEgrMonitorEntry,
       "tmnxAncpMssEgrMntrQosShedName": tmnxAncpMssEgrMntrQosShedName,
       "tmnxAncpMssEgrMntrQosShedPIR": tmnxAncpMssEgrMntrQosShedPIR,
       "tmnxAncpMssEgrMntrAncpString": tmnxAncpMssEgrMntrAncpString,
       "tmnxAncpMssEgrMntrQosShedPIRHi": tmnxAncpMssEgrMntrQosShedPIRHi,
       "tmnxAncpMssEgrMntrQosShedPIRLo": tmnxAncpMssEgrMntrQosShedPIRLo,
       "tmnxAncpSubMonitorTable": tmnxAncpSubMonitorTable,
       "tmnxAncpSubMonitorEntry": tmnxAncpSubMonitorEntry,
       "tmnxAncpSubMntrIngQosShedName": tmnxAncpSubMntrIngQosShedName,
       "tmnxAncpSubMntrIngQosShedPIR": tmnxAncpSubMntrIngQosShedPIR,
       "tmnxAncpSubMntrEgrQosShedName": tmnxAncpSubMntrEgrQosShedName,
       "tmnxAncpSubMntrEgrQosShedPIR": tmnxAncpSubMntrEgrQosShedPIR,
       "tmnxAncpSubMntrEgrAggRateLimit": tmnxAncpSubMntrEgrAggRateLimit,
       "tmnxAncpSubMntrIngQosShedPIRHi": tmnxAncpSubMntrIngQosShedPIRHi,
       "tmnxAncpSubMntrIngQosShedPIRLo": tmnxAncpSubMntrIngQosShedPIRLo,
       "tmnxAncpSubMntrEgrQosShedPIRHi": tmnxAncpSubMntrEgrQosShedPIRHi,
       "tmnxAncpSubMntrEgrQosShedPIRLo": tmnxAncpSubMntrEgrQosShedPIRLo,
       "tmnxAncpStringDslLineInfoTable": tmnxAncpStringDslLineInfoTable,
       "tmnxAncpStringDslLineInfoEntry": tmnxAncpStringDslLineInfoEntry,
       "tmnxAncpStringLineInfoAncpString": tmnxAncpStringLineInfoAncpString,
       "tmnxAncpStringLineInfoType": tmnxAncpStringLineInfoType,
       "tmnxAncpStringLineInfoValue": tmnxAncpStringLineInfoValue,
       "tmnxGsmpNotifyPrefix": tmnxGsmpNotifyPrefix,
       "tmnxGsmpNotifications": tmnxGsmpNotifications,
       "tmnxAncpIngRateMonitorEvent": tmnxAncpIngRateMonitorEvent,
       "tmnxAncpEgrRateMonitorEvent": tmnxAncpEgrRateMonitorEvent,
       "tmnxAncpShcvDisabledEvent": tmnxAncpShcvDisabledEvent,
       "tmnxAncpSesRejected": tmnxAncpSesRejected,
       "tmnxAncpStringRejected": tmnxAncpStringRejected}
)
