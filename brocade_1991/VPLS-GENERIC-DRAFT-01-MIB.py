# SNMP MIB module (VPLS-GENERIC-DRAFT-01-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/VPLS-GENERIC-DRAFT-01-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:33 2025
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

(vplsRoot,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "vplsRoot")

(PwIndexType,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(VPNIdOrZero,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNIdOrZero")


# MODULE-IDENTITY

vplsGenericDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1)
)
if mibBuilder.loadTexts:
    vplsGenericDraft01MIB.setRevisions(
        ("2006-08-30 12:00",
         "2006-06-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VplsNotifications_ObjectIdentity = ObjectIdentity
vplsNotifications = _VplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 0)
)
_VplsObjects_ObjectIdentity = ObjectIdentity
vplsObjects = _VplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1)
)
_VplsConfigIndexNext_Type = Unsigned32
_VplsConfigIndexNext_Object = MibScalar
vplsConfigIndexNext = _VplsConfigIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 1),
    _VplsConfigIndexNext_Type()
)
vplsConfigIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsConfigIndexNext.setStatus("current")
_VplsConfigTable_Object = MibTable
vplsConfigTable = _VplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vplsConfigTable.setStatus("current")
_VplsConfigEntry_Object = MibTableRow
vplsConfigEntry = _VplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1)
)
vplsConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsConfigEntry.setStatus("current")


class _VplsConfigIndex_Type(Unsigned32):
    """Custom type vplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VplsConfigIndex_Type.__name__ = "Unsigned32"
_VplsConfigIndex_Object = MibTableColumn
vplsConfigIndex = _VplsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 1),
    _VplsConfigIndex_Type()
)
vplsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsConfigIndex.setStatus("current")


class _VplsConfigName_Type(SnmpAdminString):
    """Custom type vplsConfigName based on SnmpAdminString"""
    defaultValue = OctetString("")


_VplsConfigName_Type.__name__ = "SnmpAdminString"
_VplsConfigName_Object = MibTableColumn
vplsConfigName = _VplsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 2),
    _VplsConfigName_Type()
)
vplsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigName.setStatus("current")


class _VplsConfigDescr_Type(SnmpAdminString):
    """Custom type vplsConfigDescr based on SnmpAdminString"""
    defaultValue = OctetString("")


_VplsConfigDescr_Type.__name__ = "SnmpAdminString"
_VplsConfigDescr_Object = MibTableColumn
vplsConfigDescr = _VplsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 3),
    _VplsConfigDescr_Type()
)
vplsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigDescr.setStatus("current")


class _VplsConfigAdminStatus_Type(Integer32):
    """Custom type vplsConfigAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_VplsConfigAdminStatus_Type.__name__ = "Integer32"
_VplsConfigAdminStatus_Object = MibTableColumn
vplsConfigAdminStatus = _VplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 4),
    _VplsConfigAdminStatus_Type()
)
vplsConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigAdminStatus.setStatus("current")


class _VplsConfigMacLearning_Type(TruthValue):
    """Custom type vplsConfigMacLearning based on TruthValue"""
    defaultValue = 1


_VplsConfigMacLearning_Type.__name__ = "TruthValue"
_VplsConfigMacLearning_Object = MibTableColumn
vplsConfigMacLearning = _VplsConfigMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 6),
    _VplsConfigMacLearning_Type()
)
vplsConfigMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMacLearning.setStatus("current")


class _VplsConfigDiscardUnknownDest_Type(TruthValue):
    """Custom type vplsConfigDiscardUnknownDest based on TruthValue"""
    defaultValue = 2


_VplsConfigDiscardUnknownDest_Type.__name__ = "TruthValue"
_VplsConfigDiscardUnknownDest_Object = MibTableColumn
vplsConfigDiscardUnknownDest = _VplsConfigDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 7),
    _VplsConfigDiscardUnknownDest_Type()
)
vplsConfigDiscardUnknownDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigDiscardUnknownDest.setStatus("current")


class _VplsConfigMacAging_Type(TruthValue):
    """Custom type vplsConfigMacAging based on TruthValue"""
    defaultValue = 1


_VplsConfigMacAging_Type.__name__ = "TruthValue"
_VplsConfigMacAging_Object = MibTableColumn
vplsConfigMacAging = _VplsConfigMacAging_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 8),
    _VplsConfigMacAging_Type()
)
vplsConfigMacAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMacAging.setStatus("current")


class _VplsConfigFwdFullHighWatermark_Type(Unsigned32):
    """Custom type vplsConfigFwdFullHighWatermark based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VplsConfigFwdFullHighWatermark_Type.__name__ = "Unsigned32"
_VplsConfigFwdFullHighWatermark_Object = MibTableColumn
vplsConfigFwdFullHighWatermark = _VplsConfigFwdFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 10),
    _VplsConfigFwdFullHighWatermark_Type()
)
vplsConfigFwdFullHighWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigFwdFullHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    vplsConfigFwdFullHighWatermark.setUnits("percentage")


class _VplsConfigFwdFullLowWatermark_Type(Unsigned32):
    """Custom type vplsConfigFwdFullLowWatermark based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VplsConfigFwdFullLowWatermark_Type.__name__ = "Unsigned32"
_VplsConfigFwdFullLowWatermark_Object = MibTableColumn
vplsConfigFwdFullLowWatermark = _VplsConfigFwdFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 11),
    _VplsConfigFwdFullLowWatermark_Type()
)
vplsConfigFwdFullLowWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigFwdFullLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    vplsConfigFwdFullLowWatermark.setUnits("percentage")
_VplsConfigRowStatus_Type = RowStatus
_VplsConfigRowStatus_Object = MibTableColumn
vplsConfigRowStatus = _VplsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 12),
    _VplsConfigRowStatus_Type()
)
vplsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigRowStatus.setStatus("current")


class _VplsConfigMtu_Type(Unsigned32):
    """Custom type vplsConfigMtu based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_VplsConfigMtu_Type.__name__ = "Unsigned32"
_VplsConfigMtu_Object = MibTableColumn
vplsConfigMtu = _VplsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 13),
    _VplsConfigMtu_Type()
)
vplsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMtu.setStatus("current")
_VplsConfigVpnId_Type = VPNIdOrZero
_VplsConfigVpnId_Object = MibTableColumn
vplsConfigVpnId = _VplsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 14),
    _VplsConfigVpnId_Type()
)
vplsConfigVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsConfigVpnId.setStatus("current")


class _VplsConfigServiceType_Type(Integer32):
    """Custom type vplsConfigServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ethernet", 2))
    )


_VplsConfigServiceType_Type.__name__ = "Integer32"
_VplsConfigServiceType_Object = MibTableColumn
vplsConfigServiceType = _VplsConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 15),
    _VplsConfigServiceType_Type()
)
vplsConfigServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigServiceType.setStatus("current")


class _VplsConfigStorageType_Type(StorageType):
    """Custom type vplsConfigStorageType based on StorageType"""
    defaultValue = 2


_VplsConfigStorageType_Type.__name__ = "StorageType"
_VplsConfigStorageType_Object = MibTableColumn
vplsConfigStorageType = _VplsConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 2, 1, 16),
    _VplsConfigStorageType_Type()
)
vplsConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigStorageType.setStatus("current")
_VplsStatusTable_Object = MibTable
vplsStatusTable = _VplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vplsStatusTable.setStatus("current")
_VplsStatusEntry_Object = MibTableRow
vplsStatusEntry = _VplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 3, 1)
)
vplsStatusEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsStatusEntry.setStatus("current")


class _VplsStatusOperStatus_Type(Integer32):
    """Custom type vplsStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("up", 1),
          ("down", 2))
    )


_VplsStatusOperStatus_Type.__name__ = "Integer32"
_VplsStatusOperStatus_Object = MibTableColumn
vplsStatusOperStatus = _VplsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 3, 1, 1),
    _VplsStatusOperStatus_Type()
)
vplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusOperStatus.setStatus("current")
_VplsStatusPeerCount_Type = Counter32
_VplsStatusPeerCount_Object = MibTableColumn
vplsStatusPeerCount = _VplsStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 3, 1, 2),
    _VplsStatusPeerCount_Type()
)
vplsStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusPeerCount.setStatus("current")
_VplsPwBindTable_Object = MibTable
vplsPwBindTable = _VplsPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vplsPwBindTable.setStatus("current")
_VplsPwBindEntry_Object = MibTableRow
vplsPwBindEntry = _VplsPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 4, 1)
)
vplsPwBindEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigIndex"),
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "vplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    vplsPwBindEntry.setStatus("current")
_VplsPwBindIndex_Type = PwIndexType
_VplsPwBindIndex_Object = MibTableColumn
vplsPwBindIndex = _VplsPwBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 4, 1, 1),
    _VplsPwBindIndex_Type()
)
vplsPwBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsPwBindIndex.setStatus("current")


class _VplsPwBindConfigType_Type(Integer32):
    """Custom type vplsPwBindConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("autodiscovery", 2))
    )


_VplsPwBindConfigType_Type.__name__ = "Integer32"
_VplsPwBindConfigType_Object = MibTableColumn
vplsPwBindConfigType = _VplsPwBindConfigType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 4, 1, 2),
    _VplsPwBindConfigType_Type()
)
vplsPwBindConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindConfigType.setStatus("current")


class _VplsPwBindType_Type(Integer32):
    """Custom type vplsPwBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mesh", 1),
          ("spoke", 2))
    )


_VplsPwBindType_Type.__name__ = "Integer32"
_VplsPwBindType_Object = MibTableColumn
vplsPwBindType = _VplsPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 4, 1, 3),
    _VplsPwBindType_Type()
)
vplsPwBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindType.setStatus("current")
_VplsPwBindRowStatus_Type = RowStatus
_VplsPwBindRowStatus_Object = MibTableColumn
vplsPwBindRowStatus = _VplsPwBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 4, 1, 4),
    _VplsPwBindRowStatus_Type()
)
vplsPwBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindRowStatus.setStatus("current")


class _VplsPwBindStorageType_Type(StorageType):
    """Custom type vplsPwBindStorageType based on StorageType"""
    defaultValue = 2


_VplsPwBindStorageType_Type.__name__ = "StorageType"
_VplsPwBindStorageType_Object = MibTableColumn
vplsPwBindStorageType = _VplsPwBindStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 4, 1, 5),
    _VplsPwBindStorageType_Type()
)
vplsPwBindStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindStorageType.setStatus("current")


class _VplsStatusNotifEnable_Type(TruthValue):
    """Custom type vplsStatusNotifEnable based on TruthValue"""
    defaultValue = 2


_VplsStatusNotifEnable_Type.__name__ = "TruthValue"
_VplsStatusNotifEnable_Object = MibScalar
vplsStatusNotifEnable = _VplsStatusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 5),
    _VplsStatusNotifEnable_Type()
)
vplsStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsStatusNotifEnable.setStatus("current")


class _VplsNotificationMaxRate_Type(Unsigned32):
    """Custom type vplsNotificationMaxRate based on Unsigned32"""
    defaultValue = 0


_VplsNotificationMaxRate_Type.__name__ = "Unsigned32"
_VplsNotificationMaxRate_Object = MibScalar
vplsNotificationMaxRate = _VplsNotificationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 1, 6),
    _VplsNotificationMaxRate_Type()
)
vplsNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsNotificationMaxRate.setStatus("current")
_VplsConformance_ObjectIdentity = ObjectIdentity
vplsConformance = _VplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 2)
)
_VplsCompliances_ObjectIdentity = ObjectIdentity
vplsCompliances = _VplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 2, 1)
)
_VplsGroups_ObjectIdentity = ObjectIdentity
vplsGroups = _VplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 2, 2)
)

# Managed Objects groups

vplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 2, 2, 1)
)
vplsGroup.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigName"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigDescr"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigAdminStatus"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigMacLearning"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigDiscardUnknownDest"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigMacAging"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigVpnId"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigFwdFullHighWatermark"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigFwdFullLowWatermark"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigRowStatus"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigIndexNext"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigMtu"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigServiceType"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigStorageType"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsStatusOperStatus"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsStatusPeerCount"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsStatusNotifEnable"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    vplsGroup.setStatus("current")

vplsPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 2, 2, 2)
)
vplsPwBindGroup.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsPwBindConfigType"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsPwBindType"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsPwBindRowStatus"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsPwBindStorageType"))
)
if mibBuilder.loadTexts:
    vplsPwBindGroup.setStatus("current")


# Notification objects

vplsStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 0, 1)
)
vplsStatusChanged.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigVpnId"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigAdminStatus"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsStatusOperStatus"))
)
if mibBuilder.loadTexts:
    vplsStatusChanged.setStatus(
        "current"
    )

vplsFwdFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 0, 2)
)
vplsFwdFullAlarmRaised.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigVpnId"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigFwdFullHighWatermark"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    vplsFwdFullAlarmRaised.setStatus(
        "current"
    )

vplsFwdFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 0, 3)
)
vplsFwdFullAlarmCleared.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigVpnId"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigFwdFullHighWatermark"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    vplsFwdFullAlarmCleared.setStatus(
        "current"
    )


# Notifications groups

vplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 2, 2, 3)
)
vplsNotificationGroup.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsStatusChanged"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsFwdFullAlarmRaised"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsFwdFullAlarmCleared"))
)
if mibBuilder.loadTexts:
    vplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vplsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 2, 1, 1)
)
vplsModuleFullCompliance.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsGroup"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsPwBindGroup"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    vplsModuleFullCompliance.setStatus(
        "current"
    )

vplsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4, 1, 2, 1, 2)
)
vplsModuleReadOnlyCompliance.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsGroup"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsPwBindGroup"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "vplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    vplsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPLS-GENERIC-DRAFT-01-MIB",
    **{"vplsGenericDraft01MIB": vplsGenericDraft01MIB,
       "vplsNotifications": vplsNotifications,
       "vplsStatusChanged": vplsStatusChanged,
       "vplsFwdFullAlarmRaised": vplsFwdFullAlarmRaised,
       "vplsFwdFullAlarmCleared": vplsFwdFullAlarmCleared,
       "vplsObjects": vplsObjects,
       "vplsConfigIndexNext": vplsConfigIndexNext,
       "vplsConfigTable": vplsConfigTable,
       "vplsConfigEntry": vplsConfigEntry,
       "vplsConfigIndex": vplsConfigIndex,
       "vplsConfigName": vplsConfigName,
       "vplsConfigDescr": vplsConfigDescr,
       "vplsConfigAdminStatus": vplsConfigAdminStatus,
       "vplsConfigMacLearning": vplsConfigMacLearning,
       "vplsConfigDiscardUnknownDest": vplsConfigDiscardUnknownDest,
       "vplsConfigMacAging": vplsConfigMacAging,
       "vplsConfigFwdFullHighWatermark": vplsConfigFwdFullHighWatermark,
       "vplsConfigFwdFullLowWatermark": vplsConfigFwdFullLowWatermark,
       "vplsConfigRowStatus": vplsConfigRowStatus,
       "vplsConfigMtu": vplsConfigMtu,
       "vplsConfigVpnId": vplsConfigVpnId,
       "vplsConfigServiceType": vplsConfigServiceType,
       "vplsConfigStorageType": vplsConfigStorageType,
       "vplsStatusTable": vplsStatusTable,
       "vplsStatusEntry": vplsStatusEntry,
       "vplsStatusOperStatus": vplsStatusOperStatus,
       "vplsStatusPeerCount": vplsStatusPeerCount,
       "vplsPwBindTable": vplsPwBindTable,
       "vplsPwBindEntry": vplsPwBindEntry,
       "vplsPwBindIndex": vplsPwBindIndex,
       "vplsPwBindConfigType": vplsPwBindConfigType,
       "vplsPwBindType": vplsPwBindType,
       "vplsPwBindRowStatus": vplsPwBindRowStatus,
       "vplsPwBindStorageType": vplsPwBindStorageType,
       "vplsStatusNotifEnable": vplsStatusNotifEnable,
       "vplsNotificationMaxRate": vplsNotificationMaxRate,
       "vplsConformance": vplsConformance,
       "vplsCompliances": vplsCompliances,
       "vplsModuleFullCompliance": vplsModuleFullCompliance,
       "vplsModuleReadOnlyCompliance": vplsModuleReadOnlyCompliance,
       "vplsGroups": vplsGroups,
       "vplsGroup": vplsGroup,
       "vplsPwBindGroup": vplsPwBindGroup,
       "vplsNotificationGroup": vplsNotificationGroup}
)
