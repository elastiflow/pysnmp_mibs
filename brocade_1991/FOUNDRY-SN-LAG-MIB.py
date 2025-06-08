# SNMP MIB module (FOUNDRY-SN-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FOUNDRY-SN-LAG-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:43 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

snLinkAggregationGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30)
)
if mibBuilder.loadTexts:
    snLinkAggregationGroup.setRevisions(
        ("2007-09-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnLinkAggregationGroupTableObjects_ObjectIdentity = ObjectIdentity
snLinkAggregationGroupTableObjects = _SnLinkAggregationGroupTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1)
)
_SnLinkAggregationGroupTable_Object = MibTable
snLinkAggregationGroupTable = _SnLinkAggregationGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1)
)
if mibBuilder.loadTexts:
    snLinkAggregationGroupTable.setStatus("current")
_SnLinkAggregationGroupEntry_Object = MibTableRow
snLinkAggregationGroupEntry = _SnLinkAggregationGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1)
)
snLinkAggregationGroupEntry.setIndexNames(
    (0, "FOUNDRY-SN-LAG-MIB", "snLinkAggregationGroupName"),
)
if mibBuilder.loadTexts:
    snLinkAggregationGroupEntry.setStatus("current")


class _SnLinkAggregationGroupName_Type(DisplayString):
    """Custom type snLinkAggregationGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnLinkAggregationGroupName_Type.__name__ = "DisplayString"
_SnLinkAggregationGroupName_Object = MibTableColumn
snLinkAggregationGroupName = _SnLinkAggregationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 1),
    _SnLinkAggregationGroupName_Type()
)
snLinkAggregationGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snLinkAggregationGroupName.setStatus("current")


class _SnLinkAggregationGroupType_Type(Integer32):
    """Custom type snLinkAggregationGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("keepalive", 3))
    )


_SnLinkAggregationGroupType_Type.__name__ = "Integer32"
_SnLinkAggregationGroupType_Object = MibTableColumn
snLinkAggregationGroupType = _SnLinkAggregationGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 2),
    _SnLinkAggregationGroupType_Type()
)
snLinkAggregationGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snLinkAggregationGroupType.setStatus("current")


class _SnLinkAggregationGroupAdminStatus_Type(Integer32):
    """Custom type snLinkAggregationGroupAdminStatus based on Integer32"""
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
        *(("deploy", 1),
          ("deployPassive", 2),
          ("undeploy", 3),
          ("undeployForced", 4))
    )


_SnLinkAggregationGroupAdminStatus_Type.__name__ = "Integer32"
_SnLinkAggregationGroupAdminStatus_Object = MibTableColumn
snLinkAggregationGroupAdminStatus = _SnLinkAggregationGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 3),
    _SnLinkAggregationGroupAdminStatus_Type()
)
snLinkAggregationGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snLinkAggregationGroupAdminStatus.setStatus("current")
_SnLinkAggregationGroupIfList_Type = OctetString
_SnLinkAggregationGroupIfList_Object = MibTableColumn
snLinkAggregationGroupIfList = _SnLinkAggregationGroupIfList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 4),
    _SnLinkAggregationGroupIfList_Type()
)
snLinkAggregationGroupIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snLinkAggregationGroupIfList.setStatus("current")
_SnLinkAggregationGroupPrimaryPort_Type = InterfaceIndex
_SnLinkAggregationGroupPrimaryPort_Object = MibTableColumn
snLinkAggregationGroupPrimaryPort = _SnLinkAggregationGroupPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 5),
    _SnLinkAggregationGroupPrimaryPort_Type()
)
snLinkAggregationGroupPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snLinkAggregationGroupPrimaryPort.setStatus("current")


class _SnLinkAggregationGroupTrunkType_Type(Integer32):
    """Custom type snLinkAggregationGroupTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hashBased", 1),
          ("perPacket", 2))
    )


_SnLinkAggregationGroupTrunkType_Type.__name__ = "Integer32"
_SnLinkAggregationGroupTrunkType_Object = MibTableColumn
snLinkAggregationGroupTrunkType = _SnLinkAggregationGroupTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 6),
    _SnLinkAggregationGroupTrunkType_Type()
)
snLinkAggregationGroupTrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snLinkAggregationGroupTrunkType.setStatus("current")
_SnLinkAggregationGroupTrunkThreshold_Type = Unsigned32
_SnLinkAggregationGroupTrunkThreshold_Object = MibTableColumn
snLinkAggregationGroupTrunkThreshold = _SnLinkAggregationGroupTrunkThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 7),
    _SnLinkAggregationGroupTrunkThreshold_Type()
)
snLinkAggregationGroupTrunkThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snLinkAggregationGroupTrunkThreshold.setStatus("current")


class _SnLinkAggregationGroupLacpTimeout_Type(Integer32):
    """Custom type snLinkAggregationGroupLacpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("long", 2),
          ("short", 3))
    )


_SnLinkAggregationGroupLacpTimeout_Type.__name__ = "Integer32"
_SnLinkAggregationGroupLacpTimeout_Object = MibTableColumn
snLinkAggregationGroupLacpTimeout = _SnLinkAggregationGroupLacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 8),
    _SnLinkAggregationGroupLacpTimeout_Type()
)
snLinkAggregationGroupLacpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snLinkAggregationGroupLacpTimeout.setStatus("current")
_SnLinkAggregationGroupIfIndex_Type = InterfaceIndexOrZero
_SnLinkAggregationGroupIfIndex_Object = MibTableColumn
snLinkAggregationGroupIfIndex = _SnLinkAggregationGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 9),
    _SnLinkAggregationGroupIfIndex_Type()
)
snLinkAggregationGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snLinkAggregationGroupIfIndex.setStatus("current")
_SnLinkAggregationGroupPortCount_Type = Unsigned32
_SnLinkAggregationGroupPortCount_Object = MibTableColumn
snLinkAggregationGroupPortCount = _SnLinkAggregationGroupPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 10),
    _SnLinkAggregationGroupPortCount_Type()
)
snLinkAggregationGroupPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snLinkAggregationGroupPortCount.setStatus("current")
_SnLinkAggregationGroupRowStatus_Type = RowStatus
_SnLinkAggregationGroupRowStatus_Object = MibTableColumn
snLinkAggregationGroupRowStatus = _SnLinkAggregationGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 11),
    _SnLinkAggregationGroupRowStatus_Type()
)
snLinkAggregationGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snLinkAggregationGroupRowStatus.setStatus("current")
_SnLinkAggregationGroupId_Type = Unsigned32
_SnLinkAggregationGroupId_Object = MibTableColumn
snLinkAggregationGroupId = _SnLinkAggregationGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1, 1, 12),
    _SnLinkAggregationGroupId_Type()
)
snLinkAggregationGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snLinkAggregationGroupId.setStatus("current")
_SnLinkAggregationGroupPortTableObjects_ObjectIdentity = ObjectIdentity
snLinkAggregationGroupPortTableObjects = _SnLinkAggregationGroupPortTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2)
)
_SnLinkAggregationGroupPortTable_Object = MibTable
snLinkAggregationGroupPortTable = _SnLinkAggregationGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1)
)
if mibBuilder.loadTexts:
    snLinkAggregationGroupPortTable.setStatus("current")
_SnLinkAggregationGroupPortEntry_Object = MibTableRow
snLinkAggregationGroupPortEntry = _SnLinkAggregationGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1)
)
snLinkAggregationGroupPortEntry.setIndexNames(
    (0, "FOUNDRY-SN-LAG-MIB", "snLinkAggregationGroupName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snLinkAggregationGroupPortEntry.setStatus("current")


class _SnLinkAggregationGroupPortLacpPriority_Type(Integer32):
    """Custom type snLinkAggregationGroupPortLacpPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnLinkAggregationGroupPortLacpPriority_Type.__name__ = "Integer32"
_SnLinkAggregationGroupPortLacpPriority_Object = MibTableColumn
snLinkAggregationGroupPortLacpPriority = _SnLinkAggregationGroupPortLacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 1),
    _SnLinkAggregationGroupPortLacpPriority_Type()
)
snLinkAggregationGroupPortLacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snLinkAggregationGroupPortLacpPriority.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-LAG-MIB",
    **{"snLinkAggregationGroup": snLinkAggregationGroup,
       "snLinkAggregationGroupTableObjects": snLinkAggregationGroupTableObjects,
       "snLinkAggregationGroupTable": snLinkAggregationGroupTable,
       "snLinkAggregationGroupEntry": snLinkAggregationGroupEntry,
       "snLinkAggregationGroupName": snLinkAggregationGroupName,
       "snLinkAggregationGroupType": snLinkAggregationGroupType,
       "snLinkAggregationGroupAdminStatus": snLinkAggregationGroupAdminStatus,
       "snLinkAggregationGroupIfList": snLinkAggregationGroupIfList,
       "snLinkAggregationGroupPrimaryPort": snLinkAggregationGroupPrimaryPort,
       "snLinkAggregationGroupTrunkType": snLinkAggregationGroupTrunkType,
       "snLinkAggregationGroupTrunkThreshold": snLinkAggregationGroupTrunkThreshold,
       "snLinkAggregationGroupLacpTimeout": snLinkAggregationGroupLacpTimeout,
       "snLinkAggregationGroupIfIndex": snLinkAggregationGroupIfIndex,
       "snLinkAggregationGroupPortCount": snLinkAggregationGroupPortCount,
       "snLinkAggregationGroupRowStatus": snLinkAggregationGroupRowStatus,
       "snLinkAggregationGroupId": snLinkAggregationGroupId,
       "snLinkAggregationGroupPortTableObjects": snLinkAggregationGroupPortTableObjects,
       "snLinkAggregationGroupPortTable": snLinkAggregationGroupPortTable,
       "snLinkAggregationGroupPortEntry": snLinkAggregationGroupPortEntry,
       "snLinkAggregationGroupPortLacpPriority": snLinkAggregationGroupPortLacpPriority}
)
