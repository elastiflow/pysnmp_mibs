# SNMP MIB module (CIENA-CES-PBT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-CES-PBT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:46 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesPbtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cienaCesPbtMIB.setRevisions(
        ("2010-12-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesPbtMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesPbtMIBObjects = _CienaCesPbtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1)
)
_CienaCesPbt_ObjectIdentity = ObjectIdentity
cienaCesPbt = _CienaCesPbt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1)
)
_CienaCesPbtGlobalAttrs_ObjectIdentity = ObjectIdentity
cienaCesPbtGlobalAttrs = _CienaCesPbtGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 1)
)
_CienaCesPbtBridgeMac_Type = MacAddress
_CienaCesPbtBridgeMac_Object = MibScalar
cienaCesPbtBridgeMac = _CienaCesPbtBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 1, 1),
    _CienaCesPbtBridgeMac_Type()
)
cienaCesPbtBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtBridgeMac.setStatus("current")
_CienaCesPbtServiceTagEtype_Type = OctetString
_CienaCesPbtServiceTagEtype_Object = MibScalar
cienaCesPbtServiceTagEtype = _CienaCesPbtServiceTagEtype_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 1, 2),
    _CienaCesPbtServiceTagEtype_Type()
)
cienaCesPbtServiceTagEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceTagEtype.setStatus("current")
_CienaCesPbtTunnelTagEtype_Type = OctetString
_CienaCesPbtTunnelTagEtype_Object = MibScalar
cienaCesPbtTunnelTagEtype = _CienaCesPbtTunnelTagEtype_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 1, 3),
    _CienaCesPbtTunnelTagEtype_Type()
)
cienaCesPbtTunnelTagEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTunnelTagEtype.setStatus("current")


class _CienaCesPbtTunnelReversionState_Type(CienaGlobalState):
    """Custom type cienaCesPbtTunnelReversionState based on CienaGlobalState"""
    defaultValue = 2


_CienaCesPbtTunnelReversionState_Type.__name__ = "CienaGlobalState"
_CienaCesPbtTunnelReversionState_Object = MibScalar
cienaCesPbtTunnelReversionState = _CienaCesPbtTunnelReversionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 1, 4),
    _CienaCesPbtTunnelReversionState_Type()
)
cienaCesPbtTunnelReversionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTunnelReversionState.setStatus("current")


class _CienaCesPbtTunnelReversionHoldTime_Type(Unsigned32):
    """Custom type cienaCesPbtTunnelReversionHoldTime based on Unsigned32"""
    defaultValue = 3000


_CienaCesPbtTunnelReversionHoldTime_Type.__name__ = "Unsigned32"
_CienaCesPbtTunnelReversionHoldTime_Object = MibScalar
cienaCesPbtTunnelReversionHoldTime = _CienaCesPbtTunnelReversionHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 1, 5),
    _CienaCesPbtTunnelReversionHoldTime_Type()
)
cienaCesPbtTunnelReversionHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTunnelReversionHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPbtTunnelReversionHoldTime.setUnits("milliseconds")


class _CienaCesPbtTunnelSwitchOverHoldTime_Type(Unsigned32):
    """Custom type cienaCesPbtTunnelSwitchOverHoldTime based on Unsigned32"""
    defaultValue = 0


_CienaCesPbtTunnelSwitchOverHoldTime_Type.__name__ = "Unsigned32"
_CienaCesPbtTunnelSwitchOverHoldTime_Object = MibScalar
cienaCesPbtTunnelSwitchOverHoldTime = _CienaCesPbtTunnelSwitchOverHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 1, 6),
    _CienaCesPbtTunnelSwitchOverHoldTime_Type()
)
cienaCesPbtTunnelSwitchOverHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTunnelSwitchOverHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPbtTunnelSwitchOverHoldTime.setUnits("milliseconds")
_CienaCesPbtTnlGroupTable_Object = MibTable
cienaCesPbtTnlGroupTable = _CienaCesPbtTnlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupTable.setStatus("current")
_CienaCesPbtTnlGroupEntry_Object = MibTableRow
cienaCesPbtTnlGroupEntry = _CienaCesPbtTnlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2, 1)
)
cienaCesPbtTnlGroupEntry.setIndexNames(
    (0, "CIENA-CES-PBT-MIB", "cienaCesPbtTnlGroupIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupEntry.setStatus("current")
_CienaCesPbtTnlGroupIndex_Type = Unsigned32
_CienaCesPbtTnlGroupIndex_Object = MibTableColumn
cienaCesPbtTnlGroupIndex = _CienaCesPbtTnlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2, 1, 1),
    _CienaCesPbtTnlGroupIndex_Type()
)
cienaCesPbtTnlGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupIndex.setStatus("current")
_CienaCesPbtTnlGroupName_Type = DisplayString
_CienaCesPbtTnlGroupName_Object = MibTableColumn
cienaCesPbtTnlGroupName = _CienaCesPbtTnlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2, 1, 2),
    _CienaCesPbtTnlGroupName_Type()
)
cienaCesPbtTnlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupName.setStatus("current")
_CienaCesPbtTnlGroupOperState_Type = CienaGlobalState
_CienaCesPbtTnlGroupOperState_Object = MibTableColumn
cienaCesPbtTnlGroupOperState = _CienaCesPbtTnlGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2, 1, 3),
    _CienaCesPbtTnlGroupOperState_Type()
)
cienaCesPbtTnlGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupOperState.setStatus("current")
_CienaCesPbtTnlGroupActivePair_Type = Unsigned32
_CienaCesPbtTnlGroupActivePair_Object = MibTableColumn
cienaCesPbtTnlGroupActivePair = _CienaCesPbtTnlGroupActivePair_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2, 1, 4),
    _CienaCesPbtTnlGroupActivePair_Type()
)
cienaCesPbtTnlGroupActivePair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupActivePair.setStatus("current")


class _CienaCesPbtTnlGroupSyncEnabled_Type(CienaGlobalState):
    """Custom type cienaCesPbtTnlGroupSyncEnabled based on CienaGlobalState"""
    defaultValue = 2


_CienaCesPbtTnlGroupSyncEnabled_Type.__name__ = "CienaGlobalState"
_CienaCesPbtTnlGroupSyncEnabled_Object = MibTableColumn
cienaCesPbtTnlGroupSyncEnabled = _CienaCesPbtTnlGroupSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2, 1, 5),
    _CienaCesPbtTnlGroupSyncEnabled_Type()
)
cienaCesPbtTnlGroupSyncEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupSyncEnabled.setStatus("current")
_CienaCesPbtTnlGroupUseCount_Type = Unsigned32
_CienaCesPbtTnlGroupUseCount_Object = MibTableColumn
cienaCesPbtTnlGroupUseCount = _CienaCesPbtTnlGroupUseCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2, 1, 6),
    _CienaCesPbtTnlGroupUseCount_Type()
)
cienaCesPbtTnlGroupUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupUseCount.setStatus("current")
_CienaCesPbtTnlGroupReverting_Type = TruthValue
_CienaCesPbtTnlGroupReverting_Object = MibTableColumn
cienaCesPbtTnlGroupReverting = _CienaCesPbtTnlGroupReverting_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 2, 1, 7),
    _CienaCesPbtTnlGroupReverting_Type()
)
cienaCesPbtTnlGroupReverting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtTnlGroupReverting.setStatus("current")
_CienaCesPbtEncapTnlTable_Object = MibTable
cienaCesPbtEncapTnlTable = _CienaCesPbtEncapTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlTable.setStatus("current")
_CienaCesPbtEncapTnlEntry_Object = MibTableRow
cienaCesPbtEncapTnlEntry = _CienaCesPbtEncapTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1)
)
cienaCesPbtEncapTnlEntry.setIndexNames(
    (0, "CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlEntry.setStatus("current")
_CienaCesPbtEncapTnlIndex_Type = Unsigned32
_CienaCesPbtEncapTnlIndex_Object = MibTableColumn
cienaCesPbtEncapTnlIndex = _CienaCesPbtEncapTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 1),
    _CienaCesPbtEncapTnlIndex_Type()
)
cienaCesPbtEncapTnlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlIndex.setStatus("current")
_CienaCesPbtEncapTnlName_Type = DisplayString
_CienaCesPbtEncapTnlName_Object = MibTableColumn
cienaCesPbtEncapTnlName = _CienaCesPbtEncapTnlName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 2),
    _CienaCesPbtEncapTnlName_Type()
)
cienaCesPbtEncapTnlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlName.setStatus("current")
_CienaCesPbtEncapTnlGroupIndex_Type = Unsigned32
_CienaCesPbtEncapTnlGroupIndex_Object = MibTableColumn
cienaCesPbtEncapTnlGroupIndex = _CienaCesPbtEncapTnlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 3),
    _CienaCesPbtEncapTnlGroupIndex_Type()
)
cienaCesPbtEncapTnlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlGroupIndex.setStatus("current")


class _CienaCesPbtEncapTnlGroupName_Type(DisplayString):
    """Custom type cienaCesPbtEncapTnlGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesPbtEncapTnlGroupName_Type.__name__ = "DisplayString"
_CienaCesPbtEncapTnlGroupName_Object = MibTableColumn
cienaCesPbtEncapTnlGroupName = _CienaCesPbtEncapTnlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 4),
    _CienaCesPbtEncapTnlGroupName_Type()
)
cienaCesPbtEncapTnlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlGroupName.setStatus("current")


class _CienaCesPbtEncapTnlFwdState_Type(Integer32):
    """Custom type cienaCesPbtEncapTnlFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_CienaCesPbtEncapTnlFwdState_Type.__name__ = "Integer32"
_CienaCesPbtEncapTnlFwdState_Object = MibTableColumn
cienaCesPbtEncapTnlFwdState = _CienaCesPbtEncapTnlFwdState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 5),
    _CienaCesPbtEncapTnlFwdState_Type()
)
cienaCesPbtEncapTnlFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlFwdState.setStatus("current")
_CienaCesPbtEncapTnlNotifIndex_Type = Unsigned32
_CienaCesPbtEncapTnlNotifIndex_Object = MibTableColumn
cienaCesPbtEncapTnlNotifIndex = _CienaCesPbtEncapTnlNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 6),
    _CienaCesPbtEncapTnlNotifIndex_Type()
)
cienaCesPbtEncapTnlNotifIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlNotifIndex.setStatus("current")
_CienaCesPbtEncapTnlBvid_Type = Unsigned32
_CienaCesPbtEncapTnlBvid_Object = MibTableColumn
cienaCesPbtEncapTnlBvid = _CienaCesPbtEncapTnlBvid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 7),
    _CienaCesPbtEncapTnlBvid_Type()
)
cienaCesPbtEncapTnlBvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlBvid.setStatus("current")
_CienaCesPbtEncapTnlRemoteBridgeIndex_Type = Unsigned32
_CienaCesPbtEncapTnlRemoteBridgeIndex_Object = MibTableColumn
cienaCesPbtEncapTnlRemoteBridgeIndex = _CienaCesPbtEncapTnlRemoteBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 8),
    _CienaCesPbtEncapTnlRemoteBridgeIndex_Type()
)
cienaCesPbtEncapTnlRemoteBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlRemoteBridgeIndex.setStatus("current")
_CienaCesPbtEncapTnlRemoteBridgeName_Type = DisplayString
_CienaCesPbtEncapTnlRemoteBridgeName_Object = MibTableColumn
cienaCesPbtEncapTnlRemoteBridgeName = _CienaCesPbtEncapTnlRemoteBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 9),
    _CienaCesPbtEncapTnlRemoteBridgeName_Type()
)
cienaCesPbtEncapTnlRemoteBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlRemoteBridgeName.setStatus("current")
_CienaCesPbtEncapTnlPgId_Type = Unsigned32
_CienaCesPbtEncapTnlPgId_Object = MibTableColumn
cienaCesPbtEncapTnlPgId = _CienaCesPbtEncapTnlPgId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 10),
    _CienaCesPbtEncapTnlPgId_Type()
)
cienaCesPbtEncapTnlPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlPgId.setStatus("current")
_CienaCesPbtEncapTnlPortName_Type = DisplayString
_CienaCesPbtEncapTnlPortName_Object = MibTableColumn
cienaCesPbtEncapTnlPortName = _CienaCesPbtEncapTnlPortName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 11),
    _CienaCesPbtEncapTnlPortName_Type()
)
cienaCesPbtEncapTnlPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlPortName.setStatus("current")
_CienaCesPbtEncapTnlFaults_Type = Unsigned32
_CienaCesPbtEncapTnlFaults_Object = MibTableColumn
cienaCesPbtEncapTnlFaults = _CienaCesPbtEncapTnlFaults_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 12),
    _CienaCesPbtEncapTnlFaults_Type()
)
cienaCesPbtEncapTnlFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlFaults.setStatus("current")


class _CienaCesPbtEncapTnlAdminState_Type(CienaGlobalState):
    """Custom type cienaCesPbtEncapTnlAdminState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesPbtEncapTnlAdminState_Type.__name__ = "CienaGlobalState"
_CienaCesPbtEncapTnlAdminState_Object = MibTableColumn
cienaCesPbtEncapTnlAdminState = _CienaCesPbtEncapTnlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 13),
    _CienaCesPbtEncapTnlAdminState_Type()
)
cienaCesPbtEncapTnlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlAdminState.setStatus("current")
_CienaCesPbtEncapTnlOperState_Type = CienaGlobalState
_CienaCesPbtEncapTnlOperState_Object = MibTableColumn
cienaCesPbtEncapTnlOperState = _CienaCesPbtEncapTnlOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 14),
    _CienaCesPbtEncapTnlOperState_Type()
)
cienaCesPbtEncapTnlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlOperState.setStatus("current")
_CienaCesPbtEncapTnlPaired_Type = TruthValue
_CienaCesPbtEncapTnlPaired_Object = MibTableColumn
cienaCesPbtEncapTnlPaired = _CienaCesPbtEncapTnlPaired_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 15),
    _CienaCesPbtEncapTnlPaired_Type()
)
cienaCesPbtEncapTnlPaired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlPaired.setStatus("current")
_CienaCesPbtEncapTnlPairIndex_Type = Integer32
_CienaCesPbtEncapTnlPairIndex_Object = MibTableColumn
cienaCesPbtEncapTnlPairIndex = _CienaCesPbtEncapTnlPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 16),
    _CienaCesPbtEncapTnlPairIndex_Type()
)
cienaCesPbtEncapTnlPairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlPairIndex.setStatus("current")
_CienaCesPbtEncapTnlPairOperState_Type = CienaGlobalState
_CienaCesPbtEncapTnlPairOperState_Object = MibTableColumn
cienaCesPbtEncapTnlPairOperState = _CienaCesPbtEncapTnlPairOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 17),
    _CienaCesPbtEncapTnlPairOperState_Type()
)
cienaCesPbtEncapTnlPairOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlPairOperState.setStatus("current")


class _CienaCesPbtEncapTnlFrameCosPolicy_Type(Integer32):
    """Custom type cienaCesPbtEncapTnlFrameCosPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("bvidPcPMap", 2))
    )


_CienaCesPbtEncapTnlFrameCosPolicy_Type.__name__ = "Integer32"
_CienaCesPbtEncapTnlFrameCosPolicy_Object = MibTableColumn
cienaCesPbtEncapTnlFrameCosPolicy = _CienaCesPbtEncapTnlFrameCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 18),
    _CienaCesPbtEncapTnlFrameCosPolicy_Type()
)
cienaCesPbtEncapTnlFrameCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlFrameCosPolicy.setStatus("current")
_CienaCesPbtEncapTnlFrameCosMapIndex_Type = Unsigned32
_CienaCesPbtEncapTnlFrameCosMapIndex_Object = MibTableColumn
cienaCesPbtEncapTnlFrameCosMapIndex = _CienaCesPbtEncapTnlFrameCosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 19),
    _CienaCesPbtEncapTnlFrameCosMapIndex_Type()
)
cienaCesPbtEncapTnlFrameCosMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlFrameCosMapIndex.setStatus("current")
_CienaCesPbtEncapTnlFrameCosMapName_Type = DisplayString
_CienaCesPbtEncapTnlFrameCosMapName_Object = MibTableColumn
cienaCesPbtEncapTnlFrameCosMapName = _CienaCesPbtEncapTnlFrameCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 20),
    _CienaCesPbtEncapTnlFrameCosMapName_Type()
)
cienaCesPbtEncapTnlFrameCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlFrameCosMapName.setStatus("current")


class _CienaCesPbtEncapTnlFixedPcp_Type(Integer32):
    """Custom type cienaCesPbtEncapTnlFixedPcp based on Integer32"""
    defaultValue = 2


_CienaCesPbtEncapTnlFixedPcp_Type.__name__ = "Integer32"
_CienaCesPbtEncapTnlFixedPcp_Object = MibTableColumn
cienaCesPbtEncapTnlFixedPcp = _CienaCesPbtEncapTnlFixedPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 21),
    _CienaCesPbtEncapTnlFixedPcp_Type()
)
cienaCesPbtEncapTnlFixedPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlFixedPcp.setStatus("current")
_CienaCesPbtEncapTnlCfmConfigured_Type = TruthValue
_CienaCesPbtEncapTnlCfmConfigured_Object = MibTableColumn
cienaCesPbtEncapTnlCfmConfigured = _CienaCesPbtEncapTnlCfmConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 22),
    _CienaCesPbtEncapTnlCfmConfigured_Type()
)
cienaCesPbtEncapTnlCfmConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlCfmConfigured.setStatus("current")
_CienaCesPbtEncapTnlPairedDecapIndex_Type = Unsigned32
_CienaCesPbtEncapTnlPairedDecapIndex_Object = MibTableColumn
cienaCesPbtEncapTnlPairedDecapIndex = _CienaCesPbtEncapTnlPairedDecapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 23),
    _CienaCesPbtEncapTnlPairedDecapIndex_Type()
)
cienaCesPbtEncapTnlPairedDecapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlPairedDecapIndex.setStatus("current")
_CienaCesPbtEncapTnlPairedDecapName_Type = DisplayString
_CienaCesPbtEncapTnlPairedDecapName_Object = MibTableColumn
cienaCesPbtEncapTnlPairedDecapName = _CienaCesPbtEncapTnlPairedDecapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 24),
    _CienaCesPbtEncapTnlPairedDecapName_Type()
)
cienaCesPbtEncapTnlPairedDecapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlPairedDecapName.setStatus("current")
_CienaCesPbtEncapTnlWeight_Type = Unsigned32
_CienaCesPbtEncapTnlWeight_Object = MibTableColumn
cienaCesPbtEncapTnlWeight = _CienaCesPbtEncapTnlWeight_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 25),
    _CienaCesPbtEncapTnlWeight_Type()
)
cienaCesPbtEncapTnlWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlWeight.setStatus("current")
_CienaCesPbtEncapTnlLocalBridgeIndex_Type = Unsigned32
_CienaCesPbtEncapTnlLocalBridgeIndex_Object = MibTableColumn
cienaCesPbtEncapTnlLocalBridgeIndex = _CienaCesPbtEncapTnlLocalBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 26),
    _CienaCesPbtEncapTnlLocalBridgeIndex_Type()
)
cienaCesPbtEncapTnlLocalBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlLocalBridgeIndex.setStatus("current")
_CienaCesPbtEncapTnlLocalBridgeName_Type = DisplayString
_CienaCesPbtEncapTnlLocalBridgeName_Object = MibTableColumn
cienaCesPbtEncapTnlLocalBridgeName = _CienaCesPbtEncapTnlLocalBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 27),
    _CienaCesPbtEncapTnlLocalBridgeName_Type()
)
cienaCesPbtEncapTnlLocalBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlLocalBridgeName.setStatus("current")
_CienaCesPbtEncapTnlReversionToPairIndex_Type = Unsigned32
_CienaCesPbtEncapTnlReversionToPairIndex_Object = MibTableColumn
cienaCesPbtEncapTnlReversionToPairIndex = _CienaCesPbtEncapTnlReversionToPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 28),
    _CienaCesPbtEncapTnlReversionToPairIndex_Type()
)
cienaCesPbtEncapTnlReversionToPairIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlReversionToPairIndex.setStatus("current")
_CienaCesPbtEncapTnlReversionFromPairIndex_Type = Unsigned32
_CienaCesPbtEncapTnlReversionFromPairIndex_Object = MibTableColumn
cienaCesPbtEncapTnlReversionFromPairIndex = _CienaCesPbtEncapTnlReversionFromPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 3, 1, 29),
    _CienaCesPbtEncapTnlReversionFromPairIndex_Type()
)
cienaCesPbtEncapTnlReversionFromPairIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPbtEncapTnlReversionFromPairIndex.setStatus("current")
_CienaCesPbtDecapTnlTable_Object = MibTable
cienaCesPbtDecapTnlTable = _CienaCesPbtDecapTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlTable.setStatus("current")
_CienaCesPbtDecapTnlEntry_Object = MibTableRow
cienaCesPbtDecapTnlEntry = _CienaCesPbtDecapTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1)
)
cienaCesPbtDecapTnlEntry.setIndexNames(
    (0, "CIENA-CES-PBT-MIB", "cienaCesPbtDecapTnlIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlEntry.setStatus("current")
_CienaCesPbtDecapTnlIndex_Type = Unsigned32
_CienaCesPbtDecapTnlIndex_Object = MibTableColumn
cienaCesPbtDecapTnlIndex = _CienaCesPbtDecapTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 1),
    _CienaCesPbtDecapTnlIndex_Type()
)
cienaCesPbtDecapTnlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlIndex.setStatus("current")
_CienaCesPbtDecapTnlName_Type = DisplayString
_CienaCesPbtDecapTnlName_Object = MibTableColumn
cienaCesPbtDecapTnlName = _CienaCesPbtDecapTnlName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 2),
    _CienaCesPbtDecapTnlName_Type()
)
cienaCesPbtDecapTnlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlName.setStatus("current")
_CienaCesPbtDecapTnlSourceBridgeIndex_Type = Unsigned32
_CienaCesPbtDecapTnlSourceBridgeIndex_Object = MibTableColumn
cienaCesPbtDecapTnlSourceBridgeIndex = _CienaCesPbtDecapTnlSourceBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 3),
    _CienaCesPbtDecapTnlSourceBridgeIndex_Type()
)
cienaCesPbtDecapTnlSourceBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlSourceBridgeIndex.setStatus("current")
_CienaCesPbtDecapTnlSourceBridgeName_Type = DisplayString
_CienaCesPbtDecapTnlSourceBridgeName_Object = MibTableColumn
cienaCesPbtDecapTnlSourceBridgeName = _CienaCesPbtDecapTnlSourceBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 4),
    _CienaCesPbtDecapTnlSourceBridgeName_Type()
)
cienaCesPbtDecapTnlSourceBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlSourceBridgeName.setStatus("current")
_CienaCesPbtDecapTnlGroupIndex_Type = Unsigned32
_CienaCesPbtDecapTnlGroupIndex_Object = MibTableColumn
cienaCesPbtDecapTnlGroupIndex = _CienaCesPbtDecapTnlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 5),
    _CienaCesPbtDecapTnlGroupIndex_Type()
)
cienaCesPbtDecapTnlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlGroupIndex.setStatus("current")
_CienaCesPbtDecapTnlGroupName_Type = DisplayString
_CienaCesPbtDecapTnlGroupName_Object = MibTableColumn
cienaCesPbtDecapTnlGroupName = _CienaCesPbtDecapTnlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 6),
    _CienaCesPbtDecapTnlGroupName_Type()
)
cienaCesPbtDecapTnlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlGroupName.setStatus("current")
_CienaCesPbtDecapTnlBvid_Type = Unsigned32
_CienaCesPbtDecapTnlBvid_Object = MibTableColumn
cienaCesPbtDecapTnlBvid = _CienaCesPbtDecapTnlBvid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 7),
    _CienaCesPbtDecapTnlBvid_Type()
)
cienaCesPbtDecapTnlBvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlBvid.setStatus("current")
_CienaCesPbtDecapTnlPgId_Type = Unsigned32
_CienaCesPbtDecapTnlPgId_Object = MibTableColumn
cienaCesPbtDecapTnlPgId = _CienaCesPbtDecapTnlPgId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 8),
    _CienaCesPbtDecapTnlPgId_Type()
)
cienaCesPbtDecapTnlPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlPgId.setStatus("current")
_CienaCesPbtDecapTnlPortName_Type = DisplayString
_CienaCesPbtDecapTnlPortName_Object = MibTableColumn
cienaCesPbtDecapTnlPortName = _CienaCesPbtDecapTnlPortName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 9),
    _CienaCesPbtDecapTnlPortName_Type()
)
cienaCesPbtDecapTnlPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlPortName.setStatus("current")
_CienaCesPbtDecapTnlFaults_Type = Unsigned32
_CienaCesPbtDecapTnlFaults_Object = MibTableColumn
cienaCesPbtDecapTnlFaults = _CienaCesPbtDecapTnlFaults_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 10),
    _CienaCesPbtDecapTnlFaults_Type()
)
cienaCesPbtDecapTnlFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlFaults.setStatus("current")
_CienaCesPbtDecapTnlOperState_Type = CienaGlobalState
_CienaCesPbtDecapTnlOperState_Object = MibTableColumn
cienaCesPbtDecapTnlOperState = _CienaCesPbtDecapTnlOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 11),
    _CienaCesPbtDecapTnlOperState_Type()
)
cienaCesPbtDecapTnlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlOperState.setStatus("current")


class _CienaCesPbtDecapTnlFwdState_Type(Integer32):
    """Custom type cienaCesPbtDecapTnlFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_CienaCesPbtDecapTnlFwdState_Type.__name__ = "Integer32"
_CienaCesPbtDecapTnlFwdState_Object = MibTableColumn
cienaCesPbtDecapTnlFwdState = _CienaCesPbtDecapTnlFwdState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 12),
    _CienaCesPbtDecapTnlFwdState_Type()
)
cienaCesPbtDecapTnlFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlFwdState.setStatus("current")
_CienaCesPbtDecapTnlPaired_Type = TruthValue
_CienaCesPbtDecapTnlPaired_Object = MibTableColumn
cienaCesPbtDecapTnlPaired = _CienaCesPbtDecapTnlPaired_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 13),
    _CienaCesPbtDecapTnlPaired_Type()
)
cienaCesPbtDecapTnlPaired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlPaired.setStatus("current")
_CienaCesPbtDecapTnlPairIndex_Type = Integer32
_CienaCesPbtDecapTnlPairIndex_Object = MibTableColumn
cienaCesPbtDecapTnlPairIndex = _CienaCesPbtDecapTnlPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 14),
    _CienaCesPbtDecapTnlPairIndex_Type()
)
cienaCesPbtDecapTnlPairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlPairIndex.setStatus("current")
_CienaCesPbtDecapTnlPairOperState_Type = CienaGlobalState
_CienaCesPbtDecapTnlPairOperState_Object = MibTableColumn
cienaCesPbtDecapTnlPairOperState = _CienaCesPbtDecapTnlPairOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 15),
    _CienaCesPbtDecapTnlPairOperState_Type()
)
cienaCesPbtDecapTnlPairOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlPairOperState.setStatus("current")


class _CienaCesPbtDecapTnlResolvedCosPolicy_Type(Integer32):
    """Custom type cienaCesPbtDecapTnlResolvedCosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("fixed", 2),
          ("bvidPcpMap", 3))
    )


_CienaCesPbtDecapTnlResolvedCosPolicy_Type.__name__ = "Integer32"
_CienaCesPbtDecapTnlResolvedCosPolicy_Object = MibTableColumn
cienaCesPbtDecapTnlResolvedCosPolicy = _CienaCesPbtDecapTnlResolvedCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 16),
    _CienaCesPbtDecapTnlResolvedCosPolicy_Type()
)
cienaCesPbtDecapTnlResolvedCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlResolvedCosPolicy.setStatus("current")
_CienaCesPbtDecapTnlResolvedCosMapIndex_Type = Unsigned32
_CienaCesPbtDecapTnlResolvedCosMapIndex_Object = MibTableColumn
cienaCesPbtDecapTnlResolvedCosMapIndex = _CienaCesPbtDecapTnlResolvedCosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 17),
    _CienaCesPbtDecapTnlResolvedCosMapIndex_Type()
)
cienaCesPbtDecapTnlResolvedCosMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlResolvedCosMapIndex.setStatus("current")
_CienaCesPbtDecapTnlResolvedCosMapName_Type = DisplayString
_CienaCesPbtDecapTnlResolvedCosMapName_Object = MibTableColumn
cienaCesPbtDecapTnlResolvedCosMapName = _CienaCesPbtDecapTnlResolvedCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 18),
    _CienaCesPbtDecapTnlResolvedCosMapName_Type()
)
cienaCesPbtDecapTnlResolvedCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlResolvedCosMapName.setStatus("current")
_CienaCesPbtDecapTnlCfmConfigured_Type = TruthValue
_CienaCesPbtDecapTnlCfmConfigured_Object = MibTableColumn
cienaCesPbtDecapTnlCfmConfigured = _CienaCesPbtDecapTnlCfmConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 19),
    _CienaCesPbtDecapTnlCfmConfigured_Type()
)
cienaCesPbtDecapTnlCfmConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlCfmConfigured.setStatus("current")
_CienaCesPbtDecapTnlPairedEncapIndex_Type = Unsigned32
_CienaCesPbtDecapTnlPairedEncapIndex_Object = MibTableColumn
cienaCesPbtDecapTnlPairedEncapIndex = _CienaCesPbtDecapTnlPairedEncapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 20),
    _CienaCesPbtDecapTnlPairedEncapIndex_Type()
)
cienaCesPbtDecapTnlPairedEncapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlPairedEncapIndex.setStatus("current")
_CienaCesPbtDecapTnlPairedEncapName_Type = DisplayString
_CienaCesPbtDecapTnlPairedEncapName_Object = MibTableColumn
cienaCesPbtDecapTnlPairedEncapName = _CienaCesPbtDecapTnlPairedEncapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 4, 1, 21),
    _CienaCesPbtDecapTnlPairedEncapName_Type()
)
cienaCesPbtDecapTnlPairedEncapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtDecapTnlPairedEncapName.setStatus("current")
_CienaCesPbtRemoteBridgeNameMacMapTable_Object = MibTable
cienaCesPbtRemoteBridgeNameMacMapTable = _CienaCesPbtRemoteBridgeNameMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesPbtRemoteBridgeNameMacMapTable.setStatus("current")
_CienaCesPbtRemoteBridgeNameMacMapEntry_Object = MibTableRow
cienaCesPbtRemoteBridgeNameMacMapEntry = _CienaCesPbtRemoteBridgeNameMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 5, 1)
)
cienaCesPbtRemoteBridgeNameMacMapEntry.setIndexNames(
    (0, "CIENA-CES-PBT-MIB", "cienaCesPbtRemoteBridgeNameMacMapIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPbtRemoteBridgeNameMacMapEntry.setStatus("current")
_CienaCesPbtRemoteBridgeNameMacMapIndex_Type = Integer32
_CienaCesPbtRemoteBridgeNameMacMapIndex_Object = MibTableColumn
cienaCesPbtRemoteBridgeNameMacMapIndex = _CienaCesPbtRemoteBridgeNameMacMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 5, 1, 1),
    _CienaCesPbtRemoteBridgeNameMacMapIndex_Type()
)
cienaCesPbtRemoteBridgeNameMacMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtRemoteBridgeNameMacMapIndex.setStatus("current")
_CienaCesPbtRemoteBridgeNameMacMapBridgeName_Type = DisplayString
_CienaCesPbtRemoteBridgeNameMacMapBridgeName_Object = MibTableColumn
cienaCesPbtRemoteBridgeNameMacMapBridgeName = _CienaCesPbtRemoteBridgeNameMacMapBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 5, 1, 2),
    _CienaCesPbtRemoteBridgeNameMacMapBridgeName_Type()
)
cienaCesPbtRemoteBridgeNameMacMapBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtRemoteBridgeNameMacMapBridgeName.setStatus("current")
_CienaCesPbtRemoteBridgeNameMacMapMacAddr_Type = MacAddress
_CienaCesPbtRemoteBridgeNameMacMapMacAddr_Object = MibTableColumn
cienaCesPbtRemoteBridgeNameMacMapMacAddr = _CienaCesPbtRemoteBridgeNameMacMapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 5, 1, 3),
    _CienaCesPbtRemoteBridgeNameMacMapMacAddr_Type()
)
cienaCesPbtRemoteBridgeNameMacMapMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtRemoteBridgeNameMacMapMacAddr.setStatus("current")
_CienaCesPbtRemoteBridgeNameMacMapUseCount_Type = Counter32
_CienaCesPbtRemoteBridgeNameMacMapUseCount_Object = MibTableColumn
cienaCesPbtRemoteBridgeNameMacMapUseCount = _CienaCesPbtRemoteBridgeNameMacMapUseCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 5, 1, 4),
    _CienaCesPbtRemoteBridgeNameMacMapUseCount_Type()
)
cienaCesPbtRemoteBridgeNameMacMapUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtRemoteBridgeNameMacMapUseCount.setStatus("current")
_CienaCesPbtLocalBridgeNameMacMapTable_Object = MibTable
cienaCesPbtLocalBridgeNameMacMapTable = _CienaCesPbtLocalBridgeNameMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesPbtLocalBridgeNameMacMapTable.setStatus("current")
_CienaCesPbtLocalBridgeNameMacMapEntry_Object = MibTableRow
cienaCesPbtLocalBridgeNameMacMapEntry = _CienaCesPbtLocalBridgeNameMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 7, 1)
)
cienaCesPbtLocalBridgeNameMacMapEntry.setIndexNames(
    (0, "CIENA-CES-PBT-MIB", "cienaCesPbtLocalBridgeNameMacMapIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPbtLocalBridgeNameMacMapEntry.setStatus("current")
_CienaCesPbtLocalBridgeNameMacMapIndex_Type = Integer32
_CienaCesPbtLocalBridgeNameMacMapIndex_Object = MibTableColumn
cienaCesPbtLocalBridgeNameMacMapIndex = _CienaCesPbtLocalBridgeNameMacMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 7, 1, 1),
    _CienaCesPbtLocalBridgeNameMacMapIndex_Type()
)
cienaCesPbtLocalBridgeNameMacMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtLocalBridgeNameMacMapIndex.setStatus("current")
_CienaCesPbtLocalBridgeNameMacMapBridgeName_Type = DisplayString
_CienaCesPbtLocalBridgeNameMacMapBridgeName_Object = MibTableColumn
cienaCesPbtLocalBridgeNameMacMapBridgeName = _CienaCesPbtLocalBridgeNameMacMapBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 7, 1, 2),
    _CienaCesPbtLocalBridgeNameMacMapBridgeName_Type()
)
cienaCesPbtLocalBridgeNameMacMapBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtLocalBridgeNameMacMapBridgeName.setStatus("current")
_CienaCesPbtLocalBridgeNameMacMapMacAddr_Type = MacAddress
_CienaCesPbtLocalBridgeNameMacMapMacAddr_Object = MibTableColumn
cienaCesPbtLocalBridgeNameMacMapMacAddr = _CienaCesPbtLocalBridgeNameMacMapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 7, 1, 3),
    _CienaCesPbtLocalBridgeNameMacMapMacAddr_Type()
)
cienaCesPbtLocalBridgeNameMacMapMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtLocalBridgeNameMacMapMacAddr.setStatus("current")
_CienaCesPbtLocalBridgeNameMacMapUseCount_Type = Counter32
_CienaCesPbtLocalBridgeNameMacMapUseCount_Object = MibTableColumn
cienaCesPbtLocalBridgeNameMacMapUseCount = _CienaCesPbtLocalBridgeNameMacMapUseCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 7, 1, 4),
    _CienaCesPbtLocalBridgeNameMacMapUseCount_Type()
)
cienaCesPbtLocalBridgeNameMacMapUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtLocalBridgeNameMacMapUseCount.setStatus("current")
_CienaCesPbtServiceTable_Object = MibTable
cienaCesPbtServiceTable = _CienaCesPbtServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cienaCesPbtServiceTable.setStatus("current")
_CienaCesPbtServiceEntry_Object = MibTableRow
cienaCesPbtServiceEntry = _CienaCesPbtServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1)
)
cienaCesPbtServiceEntry.setIndexNames(
    (0, "CIENA-CES-PBT-MIB", "cienaCesPbtServiceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPbtServiceEntry.setStatus("current")
_CienaCesPbtServiceIndex_Type = Unsigned32
_CienaCesPbtServiceIndex_Object = MibTableColumn
cienaCesPbtServiceIndex = _CienaCesPbtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 1),
    _CienaCesPbtServiceIndex_Type()
)
cienaCesPbtServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPbtServiceIndex.setStatus("current")
_CienaCesPbtServiceName_Type = DisplayString
_CienaCesPbtServiceName_Object = MibTableColumn
cienaCesPbtServiceName = _CienaCesPbtServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 2),
    _CienaCesPbtServiceName_Type()
)
cienaCesPbtServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceName.setStatus("current")
_CienaCesPbtServiceOperStatus_Type = CienaGlobalState
_CienaCesPbtServiceOperStatus_Object = MibTableColumn
cienaCesPbtServiceOperStatus = _CienaCesPbtServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 3),
    _CienaCesPbtServiceOperStatus_Type()
)
cienaCesPbtServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceOperStatus.setStatus("current")
_CienaCesPbtServiceFloodContProfileId_Type = Integer32
_CienaCesPbtServiceFloodContProfileId_Object = MibTableColumn
cienaCesPbtServiceFloodContProfileId = _CienaCesPbtServiceFloodContProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 4),
    _CienaCesPbtServiceFloodContProfileId_Type()
)
cienaCesPbtServiceFloodContProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceFloodContProfileId.setStatus("current")
_CienaCesPbtServiceFloodContProfileName_Type = DisplayString
_CienaCesPbtServiceFloodContProfileName_Object = MibTableColumn
cienaCesPbtServiceFloodContProfileName = _CienaCesPbtServiceFloodContProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 5),
    _CienaCesPbtServiceFloodContProfileName_Type()
)
cienaCesPbtServiceFloodContProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceFloodContProfileName.setStatus("current")
_CienaCesPbtServiceVsIndex_Type = Unsigned32
_CienaCesPbtServiceVsIndex_Object = MibTableColumn
cienaCesPbtServiceVsIndex = _CienaCesPbtServiceVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 6),
    _CienaCesPbtServiceVsIndex_Type()
)
cienaCesPbtServiceVsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceVsIndex.setStatus("current")
_CienaCesPbtServiceVsName_Type = DisplayString
_CienaCesPbtServiceVsName_Object = MibTableColumn
cienaCesPbtServiceVsName = _CienaCesPbtServiceVsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 7),
    _CienaCesPbtServiceVsName_Type()
)
cienaCesPbtServiceVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceVsName.setStatus("current")
_CienaCesPbtServiceTnlGroupIndex_Type = Unsigned32
_CienaCesPbtServiceTnlGroupIndex_Object = MibTableColumn
cienaCesPbtServiceTnlGroupIndex = _CienaCesPbtServiceTnlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 8),
    _CienaCesPbtServiceTnlGroupIndex_Type()
)
cienaCesPbtServiceTnlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceTnlGroupIndex.setStatus("current")
_CienaCesPbtServiceTnlGroupName_Type = DisplayString
_CienaCesPbtServiceTnlGroupName_Object = MibTableColumn
cienaCesPbtServiceTnlGroupName = _CienaCesPbtServiceTnlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 9),
    _CienaCesPbtServiceTnlGroupName_Type()
)
cienaCesPbtServiceTnlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceTnlGroupName.setStatus("current")
_CienaCesPbtServiceIngressIsId_Type = Unsigned32
_CienaCesPbtServiceIngressIsId_Object = MibTableColumn
cienaCesPbtServiceIngressIsId = _CienaCesPbtServiceIngressIsId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 10),
    _CienaCesPbtServiceIngressIsId_Type()
)
cienaCesPbtServiceIngressIsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceIngressIsId.setStatus("current")
_CienaCesPbtServiceEgressIsId_Type = Unsigned32
_CienaCesPbtServiceEgressIsId_Object = MibTableColumn
cienaCesPbtServiceEgressIsId = _CienaCesPbtServiceEgressIsId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 11),
    _CienaCesPbtServiceEgressIsId_Type()
)
cienaCesPbtServiceEgressIsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceEgressIsId.setStatus("current")


class _CienaCesPbtServiceFixedEgressPcp_Type(Integer32):
    """Custom type cienaCesPbtServiceFixedEgressPcp based on Integer32"""
    defaultValue = 2


_CienaCesPbtServiceFixedEgressPcp_Type.__name__ = "Integer32"
_CienaCesPbtServiceFixedEgressPcp_Object = MibTableColumn
cienaCesPbtServiceFixedEgressPcp = _CienaCesPbtServiceFixedEgressPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 12),
    _CienaCesPbtServiceFixedEgressPcp_Type()
)
cienaCesPbtServiceFixedEgressPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceFixedEgressPcp.setStatus("current")


class _CienaCesPbtServiceFrameCosPolicy_Type(Integer32):
    """Custom type cienaCesPbtServiceFrameCosPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("isidPcPMap", 2))
    )


_CienaCesPbtServiceFrameCosPolicy_Type.__name__ = "Integer32"
_CienaCesPbtServiceFrameCosPolicy_Object = MibTableColumn
cienaCesPbtServiceFrameCosPolicy = _CienaCesPbtServiceFrameCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 13),
    _CienaCesPbtServiceFrameCosPolicy_Type()
)
cienaCesPbtServiceFrameCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceFrameCosPolicy.setStatus("current")


class _CienaCesPbtServiceFrameCosMapIndex_Type(Integer32):
    """Custom type cienaCesPbtServiceFrameCosMapIndex based on Integer32"""
    defaultValue = 1


_CienaCesPbtServiceFrameCosMapIndex_Type.__name__ = "Integer32"
_CienaCesPbtServiceFrameCosMapIndex_Object = MibTableColumn
cienaCesPbtServiceFrameCosMapIndex = _CienaCesPbtServiceFrameCosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 14),
    _CienaCesPbtServiceFrameCosMapIndex_Type()
)
cienaCesPbtServiceFrameCosMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceFrameCosMapIndex.setStatus("current")
_CienaCesPbtServiceFrameCosMapName_Type = DisplayString
_CienaCesPbtServiceFrameCosMapName_Object = MibTableColumn
cienaCesPbtServiceFrameCosMapName = _CienaCesPbtServiceFrameCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 15),
    _CienaCesPbtServiceFrameCosMapName_Type()
)
cienaCesPbtServiceFrameCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceFrameCosMapName.setStatus("current")


class _CienaCesPbtServiceResolvedCosPolicy_Type(Integer32):
    """Custom type cienaCesPbtServiceResolvedCosPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("fixed", 2),
          ("isidPcpMap", 3))
    )


_CienaCesPbtServiceResolvedCosPolicy_Type.__name__ = "Integer32"
_CienaCesPbtServiceResolvedCosPolicy_Object = MibTableColumn
cienaCesPbtServiceResolvedCosPolicy = _CienaCesPbtServiceResolvedCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 16),
    _CienaCesPbtServiceResolvedCosPolicy_Type()
)
cienaCesPbtServiceResolvedCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceResolvedCosPolicy.setStatus("current")


class _CienaCesPbtServiceResolvedCosProfileIndex_Type(Integer32):
    """Custom type cienaCesPbtServiceResolvedCosProfileIndex based on Integer32"""
    defaultValue = 1


_CienaCesPbtServiceResolvedCosProfileIndex_Type.__name__ = "Integer32"
_CienaCesPbtServiceResolvedCosProfileIndex_Object = MibTableColumn
cienaCesPbtServiceResolvedCosProfileIndex = _CienaCesPbtServiceResolvedCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 17),
    _CienaCesPbtServiceResolvedCosProfileIndex_Type()
)
cienaCesPbtServiceResolvedCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceResolvedCosProfileIndex.setStatus("current")
_CienaCesPbtServiceResolvedCosProfileName_Type = DisplayString
_CienaCesPbtServiceResolvedCosProfileName_Object = MibTableColumn
cienaCesPbtServiceResolvedCosProfileName = _CienaCesPbtServiceResolvedCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 18),
    _CienaCesPbtServiceResolvedCosProfileName_Type()
)
cienaCesPbtServiceResolvedCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceResolvedCosProfileName.setStatus("current")
_CienaCesPbtServiceIngressMeterProfileId_Type = Integer32
_CienaCesPbtServiceIngressMeterProfileId_Object = MibTableColumn
cienaCesPbtServiceIngressMeterProfileId = _CienaCesPbtServiceIngressMeterProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 19),
    _CienaCesPbtServiceIngressMeterProfileId_Type()
)
cienaCesPbtServiceIngressMeterProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceIngressMeterProfileId.setStatus("current")
_CienaCesPbtServiceIngressMeterProfileName_Type = DisplayString
_CienaCesPbtServiceIngressMeterProfileName_Object = MibTableColumn
cienaCesPbtServiceIngressMeterProfileName = _CienaCesPbtServiceIngressMeterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 20),
    _CienaCesPbtServiceIngressMeterProfileName_Type()
)
cienaCesPbtServiceIngressMeterProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceIngressMeterProfileName.setStatus("current")


class _CienaCesPbtServiceIngressMeterPolicy_Type(Integer32):
    """Custom type cienaCesPbtServiceIngressMeterPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("nonhierarchical", 1),
          ("hierarchical", 2))
    )


_CienaCesPbtServiceIngressMeterPolicy_Type.__name__ = "Integer32"
_CienaCesPbtServiceIngressMeterPolicy_Object = MibTableColumn
cienaCesPbtServiceIngressMeterPolicy = _CienaCesPbtServiceIngressMeterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 21),
    _CienaCesPbtServiceIngressMeterPolicy_Type()
)
cienaCesPbtServiceIngressMeterPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceIngressMeterPolicy.setStatus("current")
_CienaCesPbtServiceEgressL2UserFrameTransform_Type = OctetString
_CienaCesPbtServiceEgressL2UserFrameTransform_Object = MibTableColumn
cienaCesPbtServiceEgressL2UserFrameTransform = _CienaCesPbtServiceEgressL2UserFrameTransform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 22),
    _CienaCesPbtServiceEgressL2UserFrameTransform_Type()
)
cienaCesPbtServiceEgressL2UserFrameTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceEgressL2UserFrameTransform.setStatus("current")
_CienaCesPbtServiceIngressL2UserFrameTransform_Type = OctetString
_CienaCesPbtServiceIngressL2UserFrameTransform_Object = MibTableColumn
cienaCesPbtServiceIngressL2UserFrameTransform = _CienaCesPbtServiceIngressL2UserFrameTransform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 1, 1, 8, 1, 23),
    _CienaCesPbtServiceIngressL2UserFrameTransform_Type()
)
cienaCesPbtServiceIngressL2UserFrameTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPbtServiceIngressL2UserFrameTransform.setStatus("current")
_CienaCesPbtMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesPbtMIBConformance = _CienaCesPbtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 3)
)
_CienaCesPbtMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesPbtMIBCompliances = _CienaCesPbtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 3, 1)
)
_CienaCesPbtMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesPbtMIBGroups = _CienaCesPbtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 3, 2)
)
_CienaCesPbtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesPbtMIBNotificationPrefix = _CienaCesPbtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 6)
)
_CienaCesPbtMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesPbtMIBNotifications = _CienaCesPbtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 6, 0)
)

# Managed Objects groups

pbtGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 3, 2, 1)
)
pbtGlobalConfigGroup.setObjects(
      *(("CIENA-CES-PBT-MIB", "cienaCesPbtBridgeMac"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtServiceTagEtype"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTunnelTagEtype"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTunnelReversionState"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTunnelReversionHoldTime"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTunnelSwitchOverHoldTime"))
)
if mibBuilder.loadTexts:
    pbtGlobalConfigGroup.setStatus("current")


# Notification objects

cienaCesPbtTunnelActivateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 6, 0, 1)
)
cienaCesPbtTunnelActivateNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlNotifIndex"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlName"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTnlGroupIndex"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTnlGroupName"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlFwdState"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlBvid"))
)
if mibBuilder.loadTexts:
    cienaCesPbtTunnelActivateNotification.setStatus(
        "current"
    )

cienaCesPbtTunnelDeactivateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 6, 0, 2)
)
cienaCesPbtTunnelDeactivateNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlNotifIndex"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlName"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTnlGroupIndex"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTnlGroupName"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlFwdState"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlBvid"))
)
if mibBuilder.loadTexts:
    cienaCesPbtTunnelDeactivateNotification.setStatus(
        "current"
    )

cienaCesPbtTunnelReversionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 6, 0, 3)
)
cienaCesPbtTunnelReversionNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTnlGroupIndex"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTnlGroupName"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlReversionToPairIndex"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtEncapTnlReversionFromPairIndex"))
)
if mibBuilder.loadTexts:
    cienaCesPbtTunnelReversionNotification.setStatus(
        "current"
    )


# Notifications groups

pbtNotificationGroups = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 6, 3, 2, 2)
)
pbtNotificationGroups.setObjects(
      *(("CIENA-CES-PBT-MIB", "cienaCesPbtTunnelActivateNotification"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTunnelDeactivateNotification"),
        ("CIENA-CES-PBT-MIB", "cienaCesPbtTunnelReversionNotification"))
)
if mibBuilder.loadTexts:
    pbtNotificationGroups.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-PBT-MIB",
    **{"cienaCesPbtMIB": cienaCesPbtMIB,
       "cienaCesPbtMIBObjects": cienaCesPbtMIBObjects,
       "cienaCesPbt": cienaCesPbt,
       "cienaCesPbtGlobalAttrs": cienaCesPbtGlobalAttrs,
       "cienaCesPbtBridgeMac": cienaCesPbtBridgeMac,
       "cienaCesPbtServiceTagEtype": cienaCesPbtServiceTagEtype,
       "cienaCesPbtTunnelTagEtype": cienaCesPbtTunnelTagEtype,
       "cienaCesPbtTunnelReversionState": cienaCesPbtTunnelReversionState,
       "cienaCesPbtTunnelReversionHoldTime": cienaCesPbtTunnelReversionHoldTime,
       "cienaCesPbtTunnelSwitchOverHoldTime": cienaCesPbtTunnelSwitchOverHoldTime,
       "cienaCesPbtTnlGroupTable": cienaCesPbtTnlGroupTable,
       "cienaCesPbtTnlGroupEntry": cienaCesPbtTnlGroupEntry,
       "cienaCesPbtTnlGroupIndex": cienaCesPbtTnlGroupIndex,
       "cienaCesPbtTnlGroupName": cienaCesPbtTnlGroupName,
       "cienaCesPbtTnlGroupOperState": cienaCesPbtTnlGroupOperState,
       "cienaCesPbtTnlGroupActivePair": cienaCesPbtTnlGroupActivePair,
       "cienaCesPbtTnlGroupSyncEnabled": cienaCesPbtTnlGroupSyncEnabled,
       "cienaCesPbtTnlGroupUseCount": cienaCesPbtTnlGroupUseCount,
       "cienaCesPbtTnlGroupReverting": cienaCesPbtTnlGroupReverting,
       "cienaCesPbtEncapTnlTable": cienaCesPbtEncapTnlTable,
       "cienaCesPbtEncapTnlEntry": cienaCesPbtEncapTnlEntry,
       "cienaCesPbtEncapTnlIndex": cienaCesPbtEncapTnlIndex,
       "cienaCesPbtEncapTnlName": cienaCesPbtEncapTnlName,
       "cienaCesPbtEncapTnlGroupIndex": cienaCesPbtEncapTnlGroupIndex,
       "cienaCesPbtEncapTnlGroupName": cienaCesPbtEncapTnlGroupName,
       "cienaCesPbtEncapTnlFwdState": cienaCesPbtEncapTnlFwdState,
       "cienaCesPbtEncapTnlNotifIndex": cienaCesPbtEncapTnlNotifIndex,
       "cienaCesPbtEncapTnlBvid": cienaCesPbtEncapTnlBvid,
       "cienaCesPbtEncapTnlRemoteBridgeIndex": cienaCesPbtEncapTnlRemoteBridgeIndex,
       "cienaCesPbtEncapTnlRemoteBridgeName": cienaCesPbtEncapTnlRemoteBridgeName,
       "cienaCesPbtEncapTnlPgId": cienaCesPbtEncapTnlPgId,
       "cienaCesPbtEncapTnlPortName": cienaCesPbtEncapTnlPortName,
       "cienaCesPbtEncapTnlFaults": cienaCesPbtEncapTnlFaults,
       "cienaCesPbtEncapTnlAdminState": cienaCesPbtEncapTnlAdminState,
       "cienaCesPbtEncapTnlOperState": cienaCesPbtEncapTnlOperState,
       "cienaCesPbtEncapTnlPaired": cienaCesPbtEncapTnlPaired,
       "cienaCesPbtEncapTnlPairIndex": cienaCesPbtEncapTnlPairIndex,
       "cienaCesPbtEncapTnlPairOperState": cienaCesPbtEncapTnlPairOperState,
       "cienaCesPbtEncapTnlFrameCosPolicy": cienaCesPbtEncapTnlFrameCosPolicy,
       "cienaCesPbtEncapTnlFrameCosMapIndex": cienaCesPbtEncapTnlFrameCosMapIndex,
       "cienaCesPbtEncapTnlFrameCosMapName": cienaCesPbtEncapTnlFrameCosMapName,
       "cienaCesPbtEncapTnlFixedPcp": cienaCesPbtEncapTnlFixedPcp,
       "cienaCesPbtEncapTnlCfmConfigured": cienaCesPbtEncapTnlCfmConfigured,
       "cienaCesPbtEncapTnlPairedDecapIndex": cienaCesPbtEncapTnlPairedDecapIndex,
       "cienaCesPbtEncapTnlPairedDecapName": cienaCesPbtEncapTnlPairedDecapName,
       "cienaCesPbtEncapTnlWeight": cienaCesPbtEncapTnlWeight,
       "cienaCesPbtEncapTnlLocalBridgeIndex": cienaCesPbtEncapTnlLocalBridgeIndex,
       "cienaCesPbtEncapTnlLocalBridgeName": cienaCesPbtEncapTnlLocalBridgeName,
       "cienaCesPbtEncapTnlReversionToPairIndex": cienaCesPbtEncapTnlReversionToPairIndex,
       "cienaCesPbtEncapTnlReversionFromPairIndex": cienaCesPbtEncapTnlReversionFromPairIndex,
       "cienaCesPbtDecapTnlTable": cienaCesPbtDecapTnlTable,
       "cienaCesPbtDecapTnlEntry": cienaCesPbtDecapTnlEntry,
       "cienaCesPbtDecapTnlIndex": cienaCesPbtDecapTnlIndex,
       "cienaCesPbtDecapTnlName": cienaCesPbtDecapTnlName,
       "cienaCesPbtDecapTnlSourceBridgeIndex": cienaCesPbtDecapTnlSourceBridgeIndex,
       "cienaCesPbtDecapTnlSourceBridgeName": cienaCesPbtDecapTnlSourceBridgeName,
       "cienaCesPbtDecapTnlGroupIndex": cienaCesPbtDecapTnlGroupIndex,
       "cienaCesPbtDecapTnlGroupName": cienaCesPbtDecapTnlGroupName,
       "cienaCesPbtDecapTnlBvid": cienaCesPbtDecapTnlBvid,
       "cienaCesPbtDecapTnlPgId": cienaCesPbtDecapTnlPgId,
       "cienaCesPbtDecapTnlPortName": cienaCesPbtDecapTnlPortName,
       "cienaCesPbtDecapTnlFaults": cienaCesPbtDecapTnlFaults,
       "cienaCesPbtDecapTnlOperState": cienaCesPbtDecapTnlOperState,
       "cienaCesPbtDecapTnlFwdState": cienaCesPbtDecapTnlFwdState,
       "cienaCesPbtDecapTnlPaired": cienaCesPbtDecapTnlPaired,
       "cienaCesPbtDecapTnlPairIndex": cienaCesPbtDecapTnlPairIndex,
       "cienaCesPbtDecapTnlPairOperState": cienaCesPbtDecapTnlPairOperState,
       "cienaCesPbtDecapTnlResolvedCosPolicy": cienaCesPbtDecapTnlResolvedCosPolicy,
       "cienaCesPbtDecapTnlResolvedCosMapIndex": cienaCesPbtDecapTnlResolvedCosMapIndex,
       "cienaCesPbtDecapTnlResolvedCosMapName": cienaCesPbtDecapTnlResolvedCosMapName,
       "cienaCesPbtDecapTnlCfmConfigured": cienaCesPbtDecapTnlCfmConfigured,
       "cienaCesPbtDecapTnlPairedEncapIndex": cienaCesPbtDecapTnlPairedEncapIndex,
       "cienaCesPbtDecapTnlPairedEncapName": cienaCesPbtDecapTnlPairedEncapName,
       "cienaCesPbtRemoteBridgeNameMacMapTable": cienaCesPbtRemoteBridgeNameMacMapTable,
       "cienaCesPbtRemoteBridgeNameMacMapEntry": cienaCesPbtRemoteBridgeNameMacMapEntry,
       "cienaCesPbtRemoteBridgeNameMacMapIndex": cienaCesPbtRemoteBridgeNameMacMapIndex,
       "cienaCesPbtRemoteBridgeNameMacMapBridgeName": cienaCesPbtRemoteBridgeNameMacMapBridgeName,
       "cienaCesPbtRemoteBridgeNameMacMapMacAddr": cienaCesPbtRemoteBridgeNameMacMapMacAddr,
       "cienaCesPbtRemoteBridgeNameMacMapUseCount": cienaCesPbtRemoteBridgeNameMacMapUseCount,
       "cienaCesPbtLocalBridgeNameMacMapTable": cienaCesPbtLocalBridgeNameMacMapTable,
       "cienaCesPbtLocalBridgeNameMacMapEntry": cienaCesPbtLocalBridgeNameMacMapEntry,
       "cienaCesPbtLocalBridgeNameMacMapIndex": cienaCesPbtLocalBridgeNameMacMapIndex,
       "cienaCesPbtLocalBridgeNameMacMapBridgeName": cienaCesPbtLocalBridgeNameMacMapBridgeName,
       "cienaCesPbtLocalBridgeNameMacMapMacAddr": cienaCesPbtLocalBridgeNameMacMapMacAddr,
       "cienaCesPbtLocalBridgeNameMacMapUseCount": cienaCesPbtLocalBridgeNameMacMapUseCount,
       "cienaCesPbtServiceTable": cienaCesPbtServiceTable,
       "cienaCesPbtServiceEntry": cienaCesPbtServiceEntry,
       "cienaCesPbtServiceIndex": cienaCesPbtServiceIndex,
       "cienaCesPbtServiceName": cienaCesPbtServiceName,
       "cienaCesPbtServiceOperStatus": cienaCesPbtServiceOperStatus,
       "cienaCesPbtServiceFloodContProfileId": cienaCesPbtServiceFloodContProfileId,
       "cienaCesPbtServiceFloodContProfileName": cienaCesPbtServiceFloodContProfileName,
       "cienaCesPbtServiceVsIndex": cienaCesPbtServiceVsIndex,
       "cienaCesPbtServiceVsName": cienaCesPbtServiceVsName,
       "cienaCesPbtServiceTnlGroupIndex": cienaCesPbtServiceTnlGroupIndex,
       "cienaCesPbtServiceTnlGroupName": cienaCesPbtServiceTnlGroupName,
       "cienaCesPbtServiceIngressIsId": cienaCesPbtServiceIngressIsId,
       "cienaCesPbtServiceEgressIsId": cienaCesPbtServiceEgressIsId,
       "cienaCesPbtServiceFixedEgressPcp": cienaCesPbtServiceFixedEgressPcp,
       "cienaCesPbtServiceFrameCosPolicy": cienaCesPbtServiceFrameCosPolicy,
       "cienaCesPbtServiceFrameCosMapIndex": cienaCesPbtServiceFrameCosMapIndex,
       "cienaCesPbtServiceFrameCosMapName": cienaCesPbtServiceFrameCosMapName,
       "cienaCesPbtServiceResolvedCosPolicy": cienaCesPbtServiceResolvedCosPolicy,
       "cienaCesPbtServiceResolvedCosProfileIndex": cienaCesPbtServiceResolvedCosProfileIndex,
       "cienaCesPbtServiceResolvedCosProfileName": cienaCesPbtServiceResolvedCosProfileName,
       "cienaCesPbtServiceIngressMeterProfileId": cienaCesPbtServiceIngressMeterProfileId,
       "cienaCesPbtServiceIngressMeterProfileName": cienaCesPbtServiceIngressMeterProfileName,
       "cienaCesPbtServiceIngressMeterPolicy": cienaCesPbtServiceIngressMeterPolicy,
       "cienaCesPbtServiceEgressL2UserFrameTransform": cienaCesPbtServiceEgressL2UserFrameTransform,
       "cienaCesPbtServiceIngressL2UserFrameTransform": cienaCesPbtServiceIngressL2UserFrameTransform,
       "cienaCesPbtMIBConformance": cienaCesPbtMIBConformance,
       "cienaCesPbtMIBCompliances": cienaCesPbtMIBCompliances,
       "cienaCesPbtMIBGroups": cienaCesPbtMIBGroups,
       "pbtGlobalConfigGroup": pbtGlobalConfigGroup,
       "pbtNotificationGroups": pbtNotificationGroups,
       "cienaCesPbtMIBNotificationPrefix": cienaCesPbtMIBNotificationPrefix,
       "cienaCesPbtMIBNotifications": cienaCesPbtMIBNotifications,
       "cienaCesPbtTunnelActivateNotification": cienaCesPbtTunnelActivateNotification,
       "cienaCesPbtTunnelDeactivateNotification": cienaCesPbtTunnelDeactivateNotification,
       "cienaCesPbtTunnelReversionNotification": cienaCesPbtTunnelReversionNotification}
)
