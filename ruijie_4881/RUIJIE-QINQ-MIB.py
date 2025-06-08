# SNMP MIB module (RUIJIE-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-QINQ-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieQinQMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53)
)
if mibBuilder.loadTexts:
    ruijieQinQMIB.setRevisions(
        ("2009-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_RuijieQINQMIBObjects_ObjectIdentity = ObjectIdentity
ruijieQINQMIBObjects = _RuijieQINQMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1)
)
_RuijieQinQPortConfigTable_Object = MibTable
ruijieQinQPortConfigTable = _RuijieQinQPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieQinQPortConfigTable.setStatus("current")
_RuijieQinQPortConfigEntry_Object = MibTableRow
ruijieQinQPortConfigEntry = _RuijieQinQPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 1, 1)
)
ruijieQinQPortConfigEntry.setIndexNames(
    (0, "RUIJIE-QINQ-MIB", "ruijieQinQPortConfigIndex"),
)
if mibBuilder.loadTexts:
    ruijieQinQPortConfigEntry.setStatus("current")
_RuijieQinQPortConfigIndex_Type = IfIndex
_RuijieQinQPortConfigIndex_Object = MibTableColumn
ruijieQinQPortConfigIndex = _RuijieQinQPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 1, 1, 1),
    _RuijieQinQPortConfigIndex_Type()
)
ruijieQinQPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieQinQPortConfigIndex.setStatus("current")


class _RuijieQinQPortConfigMode_Type(Integer32):
    """Custom type ruijieQinQPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dot1q-tunnel", 2))
    )


_RuijieQinQPortConfigMode_Type.__name__ = "Integer32"
_RuijieQinQPortConfigMode_Object = MibTableColumn
ruijieQinQPortConfigMode = _RuijieQinQPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 1, 1, 2),
    _RuijieQinQPortConfigMode_Type()
)
ruijieQinQPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQinQPortConfigMode.setStatus("current")
_RuijieQinQPortNativeVlan_Type = VlanId
_RuijieQinQPortNativeVlan_Object = MibTableColumn
ruijieQinQPortNativeVlan = _RuijieQinQPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 1, 1, 3),
    _RuijieQinQPortNativeVlan_Type()
)
ruijieQinQPortNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQinQPortNativeVlan.setStatus("current")
_RuijieQinQPortAllowedUntagVlanList_Type = VlanList
_RuijieQinQPortAllowedUntagVlanList_Object = MibTableColumn
ruijieQinQPortAllowedUntagVlanList = _RuijieQinQPortAllowedUntagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 1, 1, 4),
    _RuijieQinQPortAllowedUntagVlanList_Type()
)
ruijieQinQPortAllowedUntagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQinQPortAllowedUntagVlanList.setStatus("current")
_RuijieQinQPortAllowedTagVlanList_Type = VlanList
_RuijieQinQPortAllowedTagVlanList_Object = MibTableColumn
ruijieQinQPortAllowedTagVlanList = _RuijieQinQPortAllowedTagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 1, 1, 5),
    _RuijieQinQPortAllowedTagVlanList_Type()
)
ruijieQinQPortAllowedTagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQinQPortAllowedTagVlanList.setStatus("current")


class _RuijieQinQServiceTPIDValue_Type(Integer32):
    """Custom type ruijieQinQServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieQinQServiceTPIDValue_Type.__name__ = "Integer32"
_RuijieQinQServiceTPIDValue_Object = MibScalar
ruijieQinQServiceTPIDValue = _RuijieQinQServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 2),
    _RuijieQinQServiceTPIDValue_Type()
)
ruijieQinQServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQinQServiceTPIDValue.setStatus("current")
_RuijieQinQIfServiceTPIDConfigTable_Object = MibTable
ruijieQinQIfServiceTPIDConfigTable = _RuijieQinQIfServiceTPIDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieQinQIfServiceTPIDConfigTable.setStatus("current")
_RuijieQinQIfServiceTPIDConfigEntry_Object = MibTableRow
ruijieQinQIfServiceTPIDConfigEntry = _RuijieQinQIfServiceTPIDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 3, 1)
)
ruijieQinQIfServiceTPIDConfigEntry.setIndexNames(
    (0, "RUIJIE-QINQ-MIB", "ruijieQinQIfServiceTPIDConfigIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieQinQIfServiceTPIDConfigEntry.setStatus("current")
_RuijieQinQIfServiceTPIDConfigIfIndex_Type = IfIndex
_RuijieQinQIfServiceTPIDConfigIfIndex_Object = MibTableColumn
ruijieQinQIfServiceTPIDConfigIfIndex = _RuijieQinQIfServiceTPIDConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 3, 1, 1),
    _RuijieQinQIfServiceTPIDConfigIfIndex_Type()
)
ruijieQinQIfServiceTPIDConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieQinQIfServiceTPIDConfigIfIndex.setStatus("current")


class _RuijieQinQIfServiceTPIDValue_Type(Integer32):
    """Custom type ruijieQinQIfServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieQinQIfServiceTPIDValue_Type.__name__ = "Integer32"
_RuijieQinQIfServiceTPIDValue_Object = MibTableColumn
ruijieQinQIfServiceTPIDValue = _RuijieQinQIfServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 3, 1, 2),
    _RuijieQinQIfServiceTPIDValue_Type()
)
ruijieQinQIfServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQinQIfServiceTPIDValue.setStatus("current")
_RuijieQinQPriorityCopyTable_Object = MibTable
ruijieQinQPriorityCopyTable = _RuijieQinQPriorityCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieQinQPriorityCopyTable.setStatus("current")
_RuijieQinQPriorityCopyEntry_Object = MibTableRow
ruijieQinQPriorityCopyEntry = _RuijieQinQPriorityCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 4, 1)
)
ruijieQinQPriorityCopyEntry.setIndexNames(
    (0, "RUIJIE-QINQ-MIB", "ruijieQinQPriorityCopyIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieQinQPriorityCopyEntry.setStatus("current")
_RuijieQinQPriorityCopyIfIndex_Type = IfIndex
_RuijieQinQPriorityCopyIfIndex_Object = MibTableColumn
ruijieQinQPriorityCopyIfIndex = _RuijieQinQPriorityCopyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 4, 1, 1),
    _RuijieQinQPriorityCopyIfIndex_Type()
)
ruijieQinQPriorityCopyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieQinQPriorityCopyIfIndex.setStatus("current")
_RuijieQinQPriorityCopyPortStatus_Type = EnabledStatus
_RuijieQinQPriorityCopyPortStatus_Object = MibTableColumn
ruijieQinQPriorityCopyPortStatus = _RuijieQinQPriorityCopyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 4, 1, 2),
    _RuijieQinQPriorityCopyPortStatus_Type()
)
ruijieQinQPriorityCopyPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQinQPriorityCopyPortStatus.setStatus("current")
_RuijieQinQPriorityRemarkTable_Object = MibTable
ruijieQinQPriorityRemarkTable = _RuijieQinQPriorityRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieQinQPriorityRemarkTable.setStatus("current")
_RuijieQinQPriorityRemarkEntry_Object = MibTableRow
ruijieQinQPriorityRemarkEntry = _RuijieQinQPriorityRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 5, 1)
)
ruijieQinQPriorityRemarkEntry.setIndexNames(
    (0, "RUIJIE-QINQ-MIB", "ruijieQinQPriorityRemarkIfIndex"),
    (0, "RUIJIE-QINQ-MIB", "ruijieQinQPriorityValue"),
)
if mibBuilder.loadTexts:
    ruijieQinQPriorityRemarkEntry.setStatus("current")
_RuijieQinQPriorityRemarkIfIndex_Type = IfIndex
_RuijieQinQPriorityRemarkIfIndex_Object = MibTableColumn
ruijieQinQPriorityRemarkIfIndex = _RuijieQinQPriorityRemarkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 5, 1, 1),
    _RuijieQinQPriorityRemarkIfIndex_Type()
)
ruijieQinQPriorityRemarkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieQinQPriorityRemarkIfIndex.setStatus("current")


class _RuijieQinQPriorityValue_Type(Integer32):
    """Custom type ruijieQinQPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieQinQPriorityValue_Type.__name__ = "Integer32"
_RuijieQinQPriorityValue_Object = MibTableColumn
ruijieQinQPriorityValue = _RuijieQinQPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 5, 1, 2),
    _RuijieQinQPriorityValue_Type()
)
ruijieQinQPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQinQPriorityValue.setStatus("current")


class _RuijieQinQPriorityRemarkValue_Type(Integer32):
    """Custom type ruijieQinQPriorityRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieQinQPriorityRemarkValue_Type.__name__ = "Integer32"
_RuijieQinQPriorityRemarkValue_Object = MibTableColumn
ruijieQinQPriorityRemarkValue = _RuijieQinQPriorityRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 5, 1, 3),
    _RuijieQinQPriorityRemarkValue_Type()
)
ruijieQinQPriorityRemarkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQinQPriorityRemarkValue.setStatus("current")
_RuijieselectiveQinQBasedOnVlanTable_Object = MibTable
ruijieselectiveQinQBasedOnVlanTable = _RuijieselectiveQinQBasedOnVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnVlanTable.setStatus("current")
_RuijieselectiveQinQBasedOnVlanEntry_Object = MibTableRow
ruijieselectiveQinQBasedOnVlanEntry = _RuijieselectiveQinQBasedOnVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 6, 1)
)
ruijieselectiveQinQBasedOnVlanEntry.setIndexNames(
    (0, "RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnVlanIfIndex"),
    (0, "RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnVlanType"),
    (0, "RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnVlanOuterVlanID"),
    (0, "RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnVlanOldOuterVlanID"),
)
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnVlanEntry.setStatus("current")
_RuijieselectiveQinQBasedOnVlanIfIndex_Type = IfIndex
_RuijieselectiveQinQBasedOnVlanIfIndex_Object = MibTableColumn
ruijieselectiveQinQBasedOnVlanIfIndex = _RuijieselectiveQinQBasedOnVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 6, 1, 1),
    _RuijieselectiveQinQBasedOnVlanIfIndex_Type()
)
ruijieselectiveQinQBasedOnVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnVlanIfIndex.setStatus("current")


class _RuijieselectiveQinQBasedOnVlanType_Type(Integer32):
    """Custom type ruijieselectiveQinQBasedOnVlanType based on Integer32"""
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
        *(("addOuterTag", 1),
          ("modifyOuterTagBaseInnerTag", 2),
          ("modifyOuterTagBaseOuterTag", 3),
          ("modifyOuterTagBaseInnerAndOuterTag", 4))
    )


_RuijieselectiveQinQBasedOnVlanType_Type.__name__ = "Integer32"
_RuijieselectiveQinQBasedOnVlanType_Object = MibTableColumn
ruijieselectiveQinQBasedOnVlanType = _RuijieselectiveQinQBasedOnVlanType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 6, 1, 2),
    _RuijieselectiveQinQBasedOnVlanType_Type()
)
ruijieselectiveQinQBasedOnVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnVlanType.setStatus("current")


class _RuijieselectiveQinQBasedOnVlanOuterVlanID_Type(Integer32):
    """Custom type ruijieselectiveQinQBasedOnVlanOuterVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieselectiveQinQBasedOnVlanOuterVlanID_Type.__name__ = "Integer32"
_RuijieselectiveQinQBasedOnVlanOuterVlanID_Object = MibTableColumn
ruijieselectiveQinQBasedOnVlanOuterVlanID = _RuijieselectiveQinQBasedOnVlanOuterVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 6, 1, 3),
    _RuijieselectiveQinQBasedOnVlanOuterVlanID_Type()
)
ruijieselectiveQinQBasedOnVlanOuterVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnVlanOuterVlanID.setStatus("current")


class _RuijieselectiveQinQBasedOnVlanOldOuterVlanID_Type(Integer32):
    """Custom type ruijieselectiveQinQBasedOnVlanOldOuterVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieselectiveQinQBasedOnVlanOldOuterVlanID_Type.__name__ = "Integer32"
_RuijieselectiveQinQBasedOnVlanOldOuterVlanID_Object = MibTableColumn
ruijieselectiveQinQBasedOnVlanOldOuterVlanID = _RuijieselectiveQinQBasedOnVlanOldOuterVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 6, 1, 4),
    _RuijieselectiveQinQBasedOnVlanOldOuterVlanID_Type()
)
ruijieselectiveQinQBasedOnVlanOldOuterVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnVlanOldOuterVlanID.setStatus("current")
_RuijieselectiveQinQBasedOnVlanVlanList_Type = VlanList
_RuijieselectiveQinQBasedOnVlanVlanList_Object = MibTableColumn
ruijieselectiveQinQBasedOnVlanVlanList = _RuijieselectiveQinQBasedOnVlanVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 6, 1, 5),
    _RuijieselectiveQinQBasedOnVlanVlanList_Type()
)
ruijieselectiveQinQBasedOnVlanVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnVlanVlanList.setStatus("current")
_RuijieselectiveQinQBasedOnAclTable_Object = MibTable
ruijieselectiveQinQBasedOnAclTable = _RuijieselectiveQinQBasedOnAclTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnAclTable.setStatus("current")
_RuijieselectiveQinQBasedOnAclEntry_Object = MibTableRow
ruijieselectiveQinQBasedOnAclEntry = _RuijieselectiveQinQBasedOnAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 7, 1)
)
ruijieselectiveQinQBasedOnAclEntry.setIndexNames(
    (0, "RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnAclIfIndex"),
    (0, "RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnAclType"),
    (0, "RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnAclAclID"),
)
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnAclEntry.setStatus("current")
_RuijieselectiveQinQBasedOnAclIfIndex_Type = IfIndex
_RuijieselectiveQinQBasedOnAclIfIndex_Object = MibTableColumn
ruijieselectiveQinQBasedOnAclIfIndex = _RuijieselectiveQinQBasedOnAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 7, 1, 1),
    _RuijieselectiveQinQBasedOnAclIfIndex_Type()
)
ruijieselectiveQinQBasedOnAclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnAclIfIndex.setStatus("current")


class _RuijieselectiveQinQBasedOnAclType_Type(Integer32):
    """Custom type ruijieselectiveQinQBasedOnAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addOuterTag", 1),
          ("modifyOuterTag", 2),
          ("modifyInnerTag", 3))
    )


_RuijieselectiveQinQBasedOnAclType_Type.__name__ = "Integer32"
_RuijieselectiveQinQBasedOnAclType_Object = MibTableColumn
ruijieselectiveQinQBasedOnAclType = _RuijieselectiveQinQBasedOnAclType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 7, 1, 2),
    _RuijieselectiveQinQBasedOnAclType_Type()
)
ruijieselectiveQinQBasedOnAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnAclType.setStatus("current")
_RuijieselectiveQinQBasedOnAclAclID_Type = Integer32
_RuijieselectiveQinQBasedOnAclAclID_Object = MibTableColumn
ruijieselectiveQinQBasedOnAclAclID = _RuijieselectiveQinQBasedOnAclAclID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 7, 1, 3),
    _RuijieselectiveQinQBasedOnAclAclID_Type()
)
ruijieselectiveQinQBasedOnAclAclID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnAclAclID.setStatus("current")


class _RuijieselectiveQinQBasedOnAclVlanID_Type(Integer32):
    """Custom type ruijieselectiveQinQBasedOnAclVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieselectiveQinQBasedOnAclVlanID_Type.__name__ = "Integer32"
_RuijieselectiveQinQBasedOnAclVlanID_Object = MibTableColumn
ruijieselectiveQinQBasedOnAclVlanID = _RuijieselectiveQinQBasedOnAclVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 7, 1, 4),
    _RuijieselectiveQinQBasedOnAclVlanID_Type()
)
ruijieselectiveQinQBasedOnAclVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieselectiveQinQBasedOnAclVlanID.setStatus("current")
_RuijieQinQVlanMappingTable_Object = MibTable
ruijieQinQVlanMappingTable = _RuijieQinQVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieQinQVlanMappingTable.setStatus("current")
_RuijieQinQVlanMappingEntry_Object = MibTableRow
ruijieQinQVlanMappingEntry = _RuijieQinQVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 8, 1)
)
ruijieQinQVlanMappingEntry.setIndexNames(
    (0, "RUIJIE-QINQ-MIB", "ruijieQinQVlanMappingIfIndex"),
    (0, "RUIJIE-QINQ-MIB", "ruijieQinQVlanMappingType"),
    (0, "RUIJIE-QINQ-MIB", "ruijieQinQVlanMappingNewVlanID"),
)
if mibBuilder.loadTexts:
    ruijieQinQVlanMappingEntry.setStatus("current")
_RuijieQinQVlanMappingIfIndex_Type = IfIndex
_RuijieQinQVlanMappingIfIndex_Object = MibTableColumn
ruijieQinQVlanMappingIfIndex = _RuijieQinQVlanMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 8, 1, 1),
    _RuijieQinQVlanMappingIfIndex_Type()
)
ruijieQinQVlanMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieQinQVlanMappingIfIndex.setStatus("current")


class _RuijieQinQVlanMappingType_Type(Integer32):
    """Custom type ruijieQinQVlanMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanMappingIn", 1),
          ("vlanMappingOut", 2))
    )


_RuijieQinQVlanMappingType_Type.__name__ = "Integer32"
_RuijieQinQVlanMappingType_Object = MibTableColumn
ruijieQinQVlanMappingType = _RuijieQinQVlanMappingType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 8, 1, 2),
    _RuijieQinQVlanMappingType_Type()
)
ruijieQinQVlanMappingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQinQVlanMappingType.setStatus("current")


class _RuijieQinQVlanMappingNewVlanID_Type(Integer32):
    """Custom type ruijieQinQVlanMappingNewVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieQinQVlanMappingNewVlanID_Type.__name__ = "Integer32"
_RuijieQinQVlanMappingNewVlanID_Object = MibTableColumn
ruijieQinQVlanMappingNewVlanID = _RuijieQinQVlanMappingNewVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 8, 1, 3),
    _RuijieQinQVlanMappingNewVlanID_Type()
)
ruijieQinQVlanMappingNewVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQinQVlanMappingNewVlanID.setStatus("current")
_RuijieQinQVlanMappingOldVlanList_Type = VlanList
_RuijieQinQVlanMappingOldVlanList_Object = MibTableColumn
ruijieQinQVlanMappingOldVlanList = _RuijieQinQVlanMappingOldVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 8, 1, 4),
    _RuijieQinQVlanMappingOldVlanList_Type()
)
ruijieQinQVlanMappingOldVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQinQVlanMappingOldVlanList.setStatus("current")


class _RuijieQinQVlanMappingOldVlanID_Type(Integer32):
    """Custom type ruijieQinQVlanMappingOldVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieQinQVlanMappingOldVlanID_Type.__name__ = "Integer32"
_RuijieQinQVlanMappingOldVlanID_Object = MibTableColumn
ruijieQinQVlanMappingOldVlanID = _RuijieQinQVlanMappingOldVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 1, 8, 1, 5),
    _RuijieQinQVlanMappingOldVlanID_Type()
)
ruijieQinQVlanMappingOldVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQinQVlanMappingOldVlanID.setStatus("current")
_RuijieQinQMIBConformance_ObjectIdentity = ObjectIdentity
ruijieQinQMIBConformance = _RuijieQinQMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 2)
)
_RuijieQinQMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieQinQMIBCompliances = _RuijieQinQMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 2, 1)
)
_RuijieQinQMIBGroups_ObjectIdentity = ObjectIdentity
ruijieQinQMIBGroups = _RuijieQinQMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 2, 2)
)

# Managed Objects groups

ruijieQinQMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 2, 2, 1)
)
ruijieQinQMIBGroup.setObjects(
      *(("RUIJIE-QINQ-MIB", "ruijieQinQPortConfigMode"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQPortNativeVlan"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQPortAllowedUntagVlanList"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQPortAllowedTagVlanList"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQServiceTPIDValue"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQIfServiceTPIDValue"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQPriorityCopyPortStatus"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQPriorityValue"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQPriorityRemarkValue"),
        ("RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnVlanType"),
        ("RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnVlanOuterVlanID"),
        ("RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnVlanOldOuterVlanID"),
        ("RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnVlanVlanList"),
        ("RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnAclType"),
        ("RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnAclAclID"),
        ("RUIJIE-QINQ-MIB", "ruijieselectiveQinQBasedOnAclVlanID"),
        ("RUIJIE-QINQ-MIB", "ruijieQinQVlanMappingNewVlanID"))
)
if mibBuilder.loadTexts:
    ruijieQinQMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieQinQMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 53, 2, 1, 1)
)
ruijieQinQMIBCompliance.setObjects(
    ("RUIJIE-QINQ-MIB", "ruijieQinQMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieQinQMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-QINQ-MIB",
    **{"VlanList": VlanList,
       "ruijieQinQMIB": ruijieQinQMIB,
       "ruijieQINQMIBObjects": ruijieQINQMIBObjects,
       "ruijieQinQPortConfigTable": ruijieQinQPortConfigTable,
       "ruijieQinQPortConfigEntry": ruijieQinQPortConfigEntry,
       "ruijieQinQPortConfigIndex": ruijieQinQPortConfigIndex,
       "ruijieQinQPortConfigMode": ruijieQinQPortConfigMode,
       "ruijieQinQPortNativeVlan": ruijieQinQPortNativeVlan,
       "ruijieQinQPortAllowedUntagVlanList": ruijieQinQPortAllowedUntagVlanList,
       "ruijieQinQPortAllowedTagVlanList": ruijieQinQPortAllowedTagVlanList,
       "ruijieQinQServiceTPIDValue": ruijieQinQServiceTPIDValue,
       "ruijieQinQIfServiceTPIDConfigTable": ruijieQinQIfServiceTPIDConfigTable,
       "ruijieQinQIfServiceTPIDConfigEntry": ruijieQinQIfServiceTPIDConfigEntry,
       "ruijieQinQIfServiceTPIDConfigIfIndex": ruijieQinQIfServiceTPIDConfigIfIndex,
       "ruijieQinQIfServiceTPIDValue": ruijieQinQIfServiceTPIDValue,
       "ruijieQinQPriorityCopyTable": ruijieQinQPriorityCopyTable,
       "ruijieQinQPriorityCopyEntry": ruijieQinQPriorityCopyEntry,
       "ruijieQinQPriorityCopyIfIndex": ruijieQinQPriorityCopyIfIndex,
       "ruijieQinQPriorityCopyPortStatus": ruijieQinQPriorityCopyPortStatus,
       "ruijieQinQPriorityRemarkTable": ruijieQinQPriorityRemarkTable,
       "ruijieQinQPriorityRemarkEntry": ruijieQinQPriorityRemarkEntry,
       "ruijieQinQPriorityRemarkIfIndex": ruijieQinQPriorityRemarkIfIndex,
       "ruijieQinQPriorityValue": ruijieQinQPriorityValue,
       "ruijieQinQPriorityRemarkValue": ruijieQinQPriorityRemarkValue,
       "ruijieselectiveQinQBasedOnVlanTable": ruijieselectiveQinQBasedOnVlanTable,
       "ruijieselectiveQinQBasedOnVlanEntry": ruijieselectiveQinQBasedOnVlanEntry,
       "ruijieselectiveQinQBasedOnVlanIfIndex": ruijieselectiveQinQBasedOnVlanIfIndex,
       "ruijieselectiveQinQBasedOnVlanType": ruijieselectiveQinQBasedOnVlanType,
       "ruijieselectiveQinQBasedOnVlanOuterVlanID": ruijieselectiveQinQBasedOnVlanOuterVlanID,
       "ruijieselectiveQinQBasedOnVlanOldOuterVlanID": ruijieselectiveQinQBasedOnVlanOldOuterVlanID,
       "ruijieselectiveQinQBasedOnVlanVlanList": ruijieselectiveQinQBasedOnVlanVlanList,
       "ruijieselectiveQinQBasedOnAclTable": ruijieselectiveQinQBasedOnAclTable,
       "ruijieselectiveQinQBasedOnAclEntry": ruijieselectiveQinQBasedOnAclEntry,
       "ruijieselectiveQinQBasedOnAclIfIndex": ruijieselectiveQinQBasedOnAclIfIndex,
       "ruijieselectiveQinQBasedOnAclType": ruijieselectiveQinQBasedOnAclType,
       "ruijieselectiveQinQBasedOnAclAclID": ruijieselectiveQinQBasedOnAclAclID,
       "ruijieselectiveQinQBasedOnAclVlanID": ruijieselectiveQinQBasedOnAclVlanID,
       "ruijieQinQVlanMappingTable": ruijieQinQVlanMappingTable,
       "ruijieQinQVlanMappingEntry": ruijieQinQVlanMappingEntry,
       "ruijieQinQVlanMappingIfIndex": ruijieQinQVlanMappingIfIndex,
       "ruijieQinQVlanMappingType": ruijieQinQVlanMappingType,
       "ruijieQinQVlanMappingNewVlanID": ruijieQinQVlanMappingNewVlanID,
       "ruijieQinQVlanMappingOldVlanList": ruijieQinQVlanMappingOldVlanList,
       "ruijieQinQVlanMappingOldVlanID": ruijieQinQVlanMappingOldVlanID,
       "ruijieQinQMIBConformance": ruijieQinQMIBConformance,
       "ruijieQinQMIBCompliances": ruijieQinQMIBCompliances,
       "ruijieQinQMIBCompliance": ruijieQinQMIBCompliance,
       "ruijieQinQMIBGroups": ruijieQinQMIBGroups,
       "ruijieQinQMIBGroup": ruijieQinQMIBGroup}
)
