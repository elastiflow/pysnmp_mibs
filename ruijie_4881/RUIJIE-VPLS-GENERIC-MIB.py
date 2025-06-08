# SNMP MIB module (RUIJIE-VPLS-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VPLS-GENERIC-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(PwIndexType,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexType")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

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

ruijievplsGenericDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77)
)
if mibBuilder.loadTexts:
    ruijievplsGenericDraft01MIB.setRevisions(
        ("2010-04-28 12:00",
         "2010-06-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class RuijieVplsBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class RuijieVplsBgpRouteTargetType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("import", 1),
          ("export", 2),
          ("both", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RuijievplsNotifications_ObjectIdentity = ObjectIdentity
ruijievplsNotifications = _RuijievplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 0)
)
_RuijievplsObjects_ObjectIdentity = ObjectIdentity
ruijievplsObjects = _RuijievplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1)
)
_RuijievplsConfigIndexNext_Type = Unsigned32
_RuijievplsConfigIndexNext_Object = MibScalar
ruijievplsConfigIndexNext = _RuijievplsConfigIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 1),
    _RuijievplsConfigIndexNext_Type()
)
ruijievplsConfigIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsConfigIndexNext.setStatus("current")
_RuijievplsConfigTable_Object = MibTable
ruijievplsConfigTable = _RuijievplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2)
)
if mibBuilder.loadTexts:
    ruijievplsConfigTable.setStatus("current")
_RuijievplsConfigEntry_Object = MibTableRow
ruijievplsConfigEntry = _RuijievplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1)
)
ruijievplsConfigEntry.setIndexNames(
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndex"),
)
if mibBuilder.loadTexts:
    ruijievplsConfigEntry.setStatus("current")


class _RuijievplsConfigIndex_Type(Unsigned32):
    """Custom type ruijievplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijievplsConfigIndex_Type.__name__ = "Unsigned32"
_RuijievplsConfigIndex_Object = MibTableColumn
ruijievplsConfigIndex = _RuijievplsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 1),
    _RuijievplsConfigIndex_Type()
)
ruijievplsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijievplsConfigIndex.setStatus("current")


class _RuijievplsConfigName_Type(SnmpAdminString):
    """Custom type ruijievplsConfigName based on SnmpAdminString"""
    defaultValue = OctetString("")


_RuijievplsConfigName_Type.__name__ = "SnmpAdminString"
_RuijievplsConfigName_Object = MibTableColumn
ruijievplsConfigName = _RuijievplsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 2),
    _RuijievplsConfigName_Type()
)
ruijievplsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigName.setStatus("current")


class _RuijievplsConfigDescr_Type(SnmpAdminString):
    """Custom type ruijievplsConfigDescr based on SnmpAdminString"""
    defaultValue = OctetString("")


_RuijievplsConfigDescr_Type.__name__ = "SnmpAdminString"
_RuijievplsConfigDescr_Object = MibTableColumn
ruijievplsConfigDescr = _RuijievplsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 3),
    _RuijievplsConfigDescr_Type()
)
ruijievplsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigDescr.setStatus("current")


class _RuijievplsConfigAdminStatus_Type(Integer32):
    """Custom type ruijievplsConfigAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_RuijievplsConfigAdminStatus_Type.__name__ = "Integer32"
_RuijievplsConfigAdminStatus_Object = MibTableColumn
ruijievplsConfigAdminStatus = _RuijievplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 4),
    _RuijievplsConfigAdminStatus_Type()
)
ruijievplsConfigAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsConfigAdminStatus.setStatus("current")


class _RuijievplsConfigMacLearning_Type(TruthValue):
    """Custom type ruijievplsConfigMacLearning based on TruthValue"""
    defaultValue = 1


_RuijievplsConfigMacLearning_Type.__name__ = "TruthValue"
_RuijievplsConfigMacLearning_Object = MibTableColumn
ruijievplsConfigMacLearning = _RuijievplsConfigMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 5),
    _RuijievplsConfigMacLearning_Type()
)
ruijievplsConfigMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigMacLearning.setStatus("current")


class _RuijievplsConfigDiscardUnknownDest_Type(TruthValue):
    """Custom type ruijievplsConfigDiscardUnknownDest based on TruthValue"""
    defaultValue = 2


_RuijievplsConfigDiscardUnknownDest_Type.__name__ = "TruthValue"
_RuijievplsConfigDiscardUnknownDest_Object = MibTableColumn
ruijievplsConfigDiscardUnknownDest = _RuijievplsConfigDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 6),
    _RuijievplsConfigDiscardUnknownDest_Type()
)
ruijievplsConfigDiscardUnknownDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigDiscardUnknownDest.setStatus("current")


class _RuijievplsConfigMacAging_Type(TruthValue):
    """Custom type ruijievplsConfigMacAging based on TruthValue"""
    defaultValue = 1


_RuijievplsConfigMacAging_Type.__name__ = "TruthValue"
_RuijievplsConfigMacAging_Object = MibTableColumn
ruijievplsConfigMacAging = _RuijievplsConfigMacAging_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 7),
    _RuijievplsConfigMacAging_Type()
)
ruijievplsConfigMacAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsConfigMacAging.setStatus("current")


class _RuijievplsConfigFwdFullHighWatermark_Type(Unsigned32):
    """Custom type ruijievplsConfigFwdFullHighWatermark based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijievplsConfigFwdFullHighWatermark_Type.__name__ = "Unsigned32"
_RuijievplsConfigFwdFullHighWatermark_Object = MibTableColumn
ruijievplsConfigFwdFullHighWatermark = _RuijievplsConfigFwdFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 8),
    _RuijievplsConfigFwdFullHighWatermark_Type()
)
ruijievplsConfigFwdFullHighWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigFwdFullHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    ruijievplsConfigFwdFullHighWatermark.setUnits("percentage")


class _RuijievplsConfigFwdFullLowWatermark_Type(Unsigned32):
    """Custom type ruijievplsConfigFwdFullLowWatermark based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijievplsConfigFwdFullLowWatermark_Type.__name__ = "Unsigned32"
_RuijievplsConfigFwdFullLowWatermark_Object = MibTableColumn
ruijievplsConfigFwdFullLowWatermark = _RuijievplsConfigFwdFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 9),
    _RuijievplsConfigFwdFullLowWatermark_Type()
)
ruijievplsConfigFwdFullLowWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigFwdFullLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    ruijievplsConfigFwdFullLowWatermark.setUnits("percentage")
_RuijievplsConfigRowStatus_Type = RowStatus
_RuijievplsConfigRowStatus_Object = MibTableColumn
ruijievplsConfigRowStatus = _RuijievplsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 10),
    _RuijievplsConfigRowStatus_Type()
)
ruijievplsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigRowStatus.setStatus("current")


class _RuijievplsConfigMtu_Type(Unsigned32):
    """Custom type ruijievplsConfigMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(46, 1530),
    )


_RuijievplsConfigMtu_Type.__name__ = "Unsigned32"
_RuijievplsConfigMtu_Object = MibTableColumn
ruijievplsConfigMtu = _RuijievplsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 11),
    _RuijievplsConfigMtu_Type()
)
ruijievplsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigMtu.setStatus("current")
_RuijievplsConfigVpnId_Type = VPNIdOrZero
_RuijievplsConfigVpnId_Object = MibTableColumn
ruijievplsConfigVpnId = _RuijievplsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 12),
    _RuijievplsConfigVpnId_Type()
)
ruijievplsConfigVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigVpnId.setStatus("current")


class _RuijievplsConfigServiceType_Type(Integer32):
    """Custom type ruijievplsConfigServiceType based on Integer32"""
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


_RuijievplsConfigServiceType_Type.__name__ = "Integer32"
_RuijievplsConfigServiceType_Object = MibTableColumn
ruijievplsConfigServiceType = _RuijievplsConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 13),
    _RuijievplsConfigServiceType_Type()
)
ruijievplsConfigServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigServiceType.setStatus("current")


class _RuijievplsConfigServiceSignal_Type(Integer32):
    """Custom type ruijievplsConfigServiceSignal based on Integer32"""
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


_RuijievplsConfigServiceSignal_Type.__name__ = "Integer32"
_RuijievplsConfigServiceSignal_Object = MibTableColumn
ruijievplsConfigServiceSignal = _RuijievplsConfigServiceSignal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 2, 1, 14),
    _RuijievplsConfigServiceSignal_Type()
)
ruijievplsConfigServiceSignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsConfigServiceSignal.setStatus("current")
_RuijievplsStatusTable_Object = MibTable
ruijievplsStatusTable = _RuijievplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 3)
)
if mibBuilder.loadTexts:
    ruijievplsStatusTable.setStatus("current")
_RuijievplsStatusEntry_Object = MibTableRow
ruijievplsStatusEntry = _RuijievplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 3, 1)
)
ruijievplsStatusEntry.setIndexNames(
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndex"),
)
if mibBuilder.loadTexts:
    ruijievplsStatusEntry.setStatus("current")


class _RuijievplsStatusOperStatus_Type(Integer32):
    """Custom type ruijievplsStatusOperStatus based on Integer32"""
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


_RuijievplsStatusOperStatus_Type.__name__ = "Integer32"
_RuijievplsStatusOperStatus_Object = MibTableColumn
ruijievplsStatusOperStatus = _RuijievplsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 3, 1, 1),
    _RuijievplsStatusOperStatus_Type()
)
ruijievplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsStatusOperStatus.setStatus("current")
_RuijievplsStatusPeerCount_Type = Counter32
_RuijievplsStatusPeerCount_Object = MibTableColumn
ruijievplsStatusPeerCount = _RuijievplsStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 3, 1, 2),
    _RuijievplsStatusPeerCount_Type()
)
ruijievplsStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsStatusPeerCount.setStatus("current")
_RuijievplsPwBindTable_Object = MibTable
ruijievplsPwBindTable = _RuijievplsPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 4)
)
if mibBuilder.loadTexts:
    ruijievplsPwBindTable.setStatus("current")
_RuijievplsPwBindEntry_Object = MibTableRow
ruijievplsPwBindEntry = _RuijievplsPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 4, 1)
)
ruijievplsPwBindEntry.setIndexNames(
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndex"),
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    ruijievplsPwBindEntry.setStatus("current")
_RuijievplsPwBindIndex_Type = Unsigned32
_RuijievplsPwBindIndex_Object = MibTableColumn
ruijievplsPwBindIndex = _RuijievplsPwBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 4, 1, 1),
    _RuijievplsPwBindIndex_Type()
)
ruijievplsPwBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijievplsPwBindIndex.setStatus("current")


class _RuijievplsPwBindConfigType_Type(Integer32):
    """Custom type ruijievplsPwBindConfigType based on Integer32"""
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


_RuijievplsPwBindConfigType_Type.__name__ = "Integer32"
_RuijievplsPwBindConfigType_Object = MibTableColumn
ruijievplsPwBindConfigType = _RuijievplsPwBindConfigType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 4, 1, 2),
    _RuijievplsPwBindConfigType_Type()
)
ruijievplsPwBindConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsPwBindConfigType.setStatus("current")


class _RuijievplsPwBindType_Type(Integer32):
    """Custom type ruijievplsPwBindType based on Integer32"""
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


_RuijievplsPwBindType_Type.__name__ = "Integer32"
_RuijievplsPwBindType_Object = MibTableColumn
ruijievplsPwBindType = _RuijievplsPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 4, 1, 3),
    _RuijievplsPwBindType_Type()
)
ruijievplsPwBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsPwBindType.setStatus("current")
_RuijievplsBgpADConfigTable_Object = MibTable
ruijievplsBgpADConfigTable = _RuijievplsBgpADConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 5)
)
if mibBuilder.loadTexts:
    ruijievplsBgpADConfigTable.setStatus("current")
_RuijievplsBgpADConfigEntry_Object = MibTableRow
ruijievplsBgpADConfigEntry = _RuijievplsBgpADConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 5, 1)
)
ruijievplsBgpADConfigEntry.setIndexNames(
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndex"),
)
if mibBuilder.loadTexts:
    ruijievplsBgpADConfigEntry.setStatus("current")
_RuijievplsBgpADConfigRouteDistinguisher_Type = RuijieVplsBgpRouteDistinguisher
_RuijievplsBgpADConfigRouteDistinguisher_Object = MibTableColumn
ruijievplsBgpADConfigRouteDistinguisher = _RuijievplsBgpADConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 5, 1, 1),
    _RuijievplsBgpADConfigRouteDistinguisher_Type()
)
ruijievplsBgpADConfigRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsBgpADConfigRouteDistinguisher.setStatus("current")
_RuijievplsBgpADConfigRowStatus_Type = RowStatus
_RuijievplsBgpADConfigRowStatus_Object = MibTableColumn
ruijievplsBgpADConfigRowStatus = _RuijievplsBgpADConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 5, 1, 2),
    _RuijievplsBgpADConfigRowStatus_Type()
)
ruijievplsBgpADConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsBgpADConfigRowStatus.setStatus("current")
_RuijievplsBgpRteTargetTable_Object = MibTable
ruijievplsBgpRteTargetTable = _RuijievplsBgpRteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 6)
)
if mibBuilder.loadTexts:
    ruijievplsBgpRteTargetTable.setStatus("current")
_RuijievplsBgpRteTargetEntry_Object = MibTableRow
ruijievplsBgpRteTargetEntry = _RuijievplsBgpRteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 6, 1)
)
ruijievplsBgpRteTargetEntry.setIndexNames(
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndex"),
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsBgpRteTargetIndex"),
)
if mibBuilder.loadTexts:
    ruijievplsBgpRteTargetEntry.setStatus("current")
_RuijievplsBgpRteTargetIndex_Type = Unsigned32
_RuijievplsBgpRteTargetIndex_Object = MibTableColumn
ruijievplsBgpRteTargetIndex = _RuijievplsBgpRteTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 6, 1, 1),
    _RuijievplsBgpRteTargetIndex_Type()
)
ruijievplsBgpRteTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijievplsBgpRteTargetIndex.setStatus("current")
_RuijievplsBgpRteTargetRTType_Type = RuijieVplsBgpRouteTargetType
_RuijievplsBgpRteTargetRTType_Object = MibTableColumn
ruijievplsBgpRteTargetRTType = _RuijievplsBgpRteTargetRTType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 6, 1, 2),
    _RuijievplsBgpRteTargetRTType_Type()
)
ruijievplsBgpRteTargetRTType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsBgpRteTargetRTType.setStatus("current")
_RuijievplsBgpRteTargetRT_Type = RuijieVplsBgpRouteTarget
_RuijievplsBgpRteTargetRT_Object = MibTableColumn
ruijievplsBgpRteTargetRT = _RuijievplsBgpRteTargetRT_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 6, 1, 3),
    _RuijievplsBgpRteTargetRT_Type()
)
ruijievplsBgpRteTargetRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsBgpRteTargetRT.setStatus("current")
_RuijievplsBgpRteTargetRTRowStatus_Type = RowStatus
_RuijievplsBgpRteTargetRTRowStatus_Object = MibTableColumn
ruijievplsBgpRteTargetRTRowStatus = _RuijievplsBgpRteTargetRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 6, 1, 4),
    _RuijievplsBgpRteTargetRTRowStatus_Type()
)
ruijievplsBgpRteTargetRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsBgpRteTargetRTRowStatus.setStatus("current")
_RuijievplsIfBindTable_Object = MibTable
ruijievplsIfBindTable = _RuijievplsIfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 7)
)
if mibBuilder.loadTexts:
    ruijievplsIfBindTable.setStatus("current")
_RuijieVplsIfBindEntry_Object = MibTableRow
ruijieVplsIfBindEntry = _RuijieVplsIfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 7, 1)
)
ruijieVplsIfBindEntry.setIndexNames(
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndex"),
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsIfBindIndex"),
)
if mibBuilder.loadTexts:
    ruijieVplsIfBindEntry.setStatus("current")
_RuijievplsIfBindIndex_Type = InterfaceIndexOrZero
_RuijievplsIfBindIndex_Object = MibTableColumn
ruijievplsIfBindIndex = _RuijievplsIfBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 7, 1, 1),
    _RuijievplsIfBindIndex_Type()
)
ruijievplsIfBindIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsIfBindIndex.setStatus("current")
_RuijievplsSiteId_Type = Unsigned32
_RuijievplsSiteId_Object = MibTableColumn
ruijievplsSiteId = _RuijievplsSiteId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 7, 1, 2),
    _RuijievplsSiteId_Type()
)
ruijievplsSiteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsSiteId.setStatus("current")
_RuijievplsIfRowStatus_Type = RowStatus
_RuijievplsIfRowStatus_Object = MibTableColumn
ruijievplsIfRowStatus = _RuijievplsIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 1, 7, 1, 3),
    _RuijievplsIfRowStatus_Type()
)
ruijievplsIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsIfRowStatus.setStatus("current")
_RuijievplsConformance_ObjectIdentity = ObjectIdentity
ruijievplsConformance = _RuijievplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 2)
)
_RuijievplsCompliances_ObjectIdentity = ObjectIdentity
ruijievplsCompliances = _RuijievplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 2, 1)
)
_RuijievplsGroups_ObjectIdentity = ObjectIdentity
ruijievplsGroups = _RuijievplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 2, 2)
)

# Managed Objects groups

ruijievplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 2, 2, 1)
)
ruijievplsGroup.setObjects(
      *(("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigName"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigDescr"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigAdminStatus"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigMacLearning"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigDiscardUnknownDest"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigMacAging"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigVpnId"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigFwdFullHighWatermark"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigFwdFullLowWatermark"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigRowStatus"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndexNext"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigMtu"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigServiceType"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsStatusOperStatus"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsStatusPeerCount"))
)
if mibBuilder.loadTexts:
    ruijievplsGroup.setStatus("current")

ruijievplsPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 2, 2, 2)
)
ruijievplsPwBindGroup.setObjects(
      *(("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsPwBindConfigType"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsPwBindType"))
)
if mibBuilder.loadTexts:
    ruijievplsPwBindGroup.setStatus("current")


# Notification objects

ruijievplsFwdFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 0, 1)
)
ruijievplsFwdFullAlarmRaised.setObjects(
      *(("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigVpnId"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigFwdFullHighWatermark"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    ruijievplsFwdFullAlarmRaised.setStatus(
        "current"
    )

ruijievplsFwdFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 0, 2)
)
ruijievplsFwdFullAlarmCleared.setObjects(
      *(("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigVpnId"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigFwdFullHighWatermark"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    ruijievplsFwdFullAlarmCleared.setStatus(
        "current"
    )


# Notifications groups

ruijievplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 2, 2, 3)
)
ruijievplsNotificationGroup.setObjects(
      *(("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsFwdFullAlarmRaised"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsFwdFullAlarmCleared"))
)
if mibBuilder.loadTexts:
    ruijievplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijievplsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 2, 1, 1)
)
ruijievplsModuleFullCompliance.setObjects(
      *(("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsGroup"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsPwBindGroup"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    ruijievplsModuleFullCompliance.setStatus(
        "current"
    )

ruijievplsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 77, 2, 1, 2)
)
ruijievplsModuleReadOnlyCompliance.setObjects(
      *(("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsGroup"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsPwBindGroup"),
        ("RUIJIE-VPLS-GENERIC-MIB", "ruijievplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    ruijievplsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VPLS-GENERIC-MIB",
    **{"RuijieVplsBgpRouteDistinguisher": RuijieVplsBgpRouteDistinguisher,
       "RuijieVplsBgpRouteTarget": RuijieVplsBgpRouteTarget,
       "RuijieVplsBgpRouteTargetType": RuijieVplsBgpRouteTargetType,
       "ruijievplsGenericDraft01MIB": ruijievplsGenericDraft01MIB,
       "ruijievplsNotifications": ruijievplsNotifications,
       "ruijievplsFwdFullAlarmRaised": ruijievplsFwdFullAlarmRaised,
       "ruijievplsFwdFullAlarmCleared": ruijievplsFwdFullAlarmCleared,
       "ruijievplsObjects": ruijievplsObjects,
       "ruijievplsConfigIndexNext": ruijievplsConfigIndexNext,
       "ruijievplsConfigTable": ruijievplsConfigTable,
       "ruijievplsConfigEntry": ruijievplsConfigEntry,
       "ruijievplsConfigIndex": ruijievplsConfigIndex,
       "ruijievplsConfigName": ruijievplsConfigName,
       "ruijievplsConfigDescr": ruijievplsConfigDescr,
       "ruijievplsConfigAdminStatus": ruijievplsConfigAdminStatus,
       "ruijievplsConfigMacLearning": ruijievplsConfigMacLearning,
       "ruijievplsConfigDiscardUnknownDest": ruijievplsConfigDiscardUnknownDest,
       "ruijievplsConfigMacAging": ruijievplsConfigMacAging,
       "ruijievplsConfigFwdFullHighWatermark": ruijievplsConfigFwdFullHighWatermark,
       "ruijievplsConfigFwdFullLowWatermark": ruijievplsConfigFwdFullLowWatermark,
       "ruijievplsConfigRowStatus": ruijievplsConfigRowStatus,
       "ruijievplsConfigMtu": ruijievplsConfigMtu,
       "ruijievplsConfigVpnId": ruijievplsConfigVpnId,
       "ruijievplsConfigServiceType": ruijievplsConfigServiceType,
       "ruijievplsConfigServiceSignal": ruijievplsConfigServiceSignal,
       "ruijievplsStatusTable": ruijievplsStatusTable,
       "ruijievplsStatusEntry": ruijievplsStatusEntry,
       "ruijievplsStatusOperStatus": ruijievplsStatusOperStatus,
       "ruijievplsStatusPeerCount": ruijievplsStatusPeerCount,
       "ruijievplsPwBindTable": ruijievplsPwBindTable,
       "ruijievplsPwBindEntry": ruijievplsPwBindEntry,
       "ruijievplsPwBindIndex": ruijievplsPwBindIndex,
       "ruijievplsPwBindConfigType": ruijievplsPwBindConfigType,
       "ruijievplsPwBindType": ruijievplsPwBindType,
       "ruijievplsBgpADConfigTable": ruijievplsBgpADConfigTable,
       "ruijievplsBgpADConfigEntry": ruijievplsBgpADConfigEntry,
       "ruijievplsBgpADConfigRouteDistinguisher": ruijievplsBgpADConfigRouteDistinguisher,
       "ruijievplsBgpADConfigRowStatus": ruijievplsBgpADConfigRowStatus,
       "ruijievplsBgpRteTargetTable": ruijievplsBgpRteTargetTable,
       "ruijievplsBgpRteTargetEntry": ruijievplsBgpRteTargetEntry,
       "ruijievplsBgpRteTargetIndex": ruijievplsBgpRteTargetIndex,
       "ruijievplsBgpRteTargetRTType": ruijievplsBgpRteTargetRTType,
       "ruijievplsBgpRteTargetRT": ruijievplsBgpRteTargetRT,
       "ruijievplsBgpRteTargetRTRowStatus": ruijievplsBgpRteTargetRTRowStatus,
       "ruijievplsIfBindTable": ruijievplsIfBindTable,
       "ruijieVplsIfBindEntry": ruijieVplsIfBindEntry,
       "ruijievplsIfBindIndex": ruijievplsIfBindIndex,
       "ruijievplsSiteId": ruijievplsSiteId,
       "ruijievplsIfRowStatus": ruijievplsIfRowStatus,
       "ruijievplsConformance": ruijievplsConformance,
       "ruijievplsCompliances": ruijievplsCompliances,
       "ruijievplsModuleFullCompliance": ruijievplsModuleFullCompliance,
       "ruijievplsModuleReadOnlyCompliance": ruijievplsModuleReadOnlyCompliance,
       "ruijievplsGroups": ruijievplsGroups,
       "ruijievplsGroup": ruijievplsGroup,
       "ruijievplsPwBindGroup": ruijievplsPwBindGroup,
       "ruijievplsNotificationGroup": ruijievplsNotificationGroup}
)
