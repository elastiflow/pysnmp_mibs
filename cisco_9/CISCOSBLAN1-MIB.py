# SNMP MIB module (CISCOSBLAN1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSBLAN1-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:13:48 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlLan1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224)
)
if mibBuilder.loadTexts:
    rlLan1.setRevisions(
        ("2015-06-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class GroupId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1279),
    )



class GroupIdList(TextualConvention, OctetString):
    status = "current"


class VlanIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



# MIB Managed Objects in the order of their OIDs



class _RlLan1STagEtherType_Type(OctetString):
    """Custom type rlLan1STagEtherType based on OctetString"""
    defaultHexValue = "88A8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_RlLan1STagEtherType_Type.__name__ = "OctetString"
_RlLan1STagEtherType_Object = MibScalar
rlLan1STagEtherType = _RlLan1STagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 1),
    _RlLan1STagEtherType_Type()
)
rlLan1STagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1STagEtherType.setStatus("current")


class _RlLan1CPVlanId_Type(VlanIdOrNone):
    """Custom type rlLan1CPVlanId based on VlanIdOrNone"""
    defaultValue = 0


_RlLan1CPVlanId_Type.__name__ = "VlanIdOrNone"
_RlLan1CPVlanId_Object = MibScalar
rlLan1CPVlanId = _RlLan1CPVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 2),
    _RlLan1CPVlanId_Type()
)
rlLan1CPVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1CPVlanId.setStatus("current")


class _RlLan1CPVlanCos_Type(Integer32):
    """Custom type rlLan1CPVlanCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlLan1CPVlanCos_Type.__name__ = "Integer32"
_RlLan1CPVlanCos_Object = MibScalar
rlLan1CPVlanCos = _RlLan1CPVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 3),
    _RlLan1CPVlanCos_Type()
)
rlLan1CPVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1CPVlanCos.setStatus("current")


class _RlLan1x86Port_Type(Integer32):
    """Custom type rlLan1x86Port based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RlLan1x86Port_Type.__name__ = "Integer32"
_RlLan1x86Port_Object = MibScalar
rlLan1x86Port = _RlLan1x86Port_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 4),
    _RlLan1x86Port_Type()
)
rlLan1x86Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86Port.setStatus("current")


class _RlLan1CPVlanMulticastMappingVlanId_Type(VlanIdOrNone):
    """Custom type rlLan1CPVlanMulticastMappingVlanId based on VlanIdOrNone"""
    defaultValue = 0


_RlLan1CPVlanMulticastMappingVlanId_Type.__name__ = "VlanIdOrNone"
_RlLan1CPVlanMulticastMappingVlanId_Object = MibScalar
rlLan1CPVlanMulticastMappingVlanId = _RlLan1CPVlanMulticastMappingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 5),
    _RlLan1CPVlanMulticastMappingVlanId_Type()
)
rlLan1CPVlanMulticastMappingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1CPVlanMulticastMappingVlanId.setStatus("current")


class _RlLan1NonCPVlanMulticastMappingVlanId_Type(VlanIdOrNone):
    """Custom type rlLan1NonCPVlanMulticastMappingVlanId based on VlanIdOrNone"""
    defaultValue = 0


_RlLan1NonCPVlanMulticastMappingVlanId_Type.__name__ = "VlanIdOrNone"
_RlLan1NonCPVlanMulticastMappingVlanId_Object = MibScalar
rlLan1NonCPVlanMulticastMappingVlanId = _RlLan1NonCPVlanMulticastMappingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 6),
    _RlLan1NonCPVlanMulticastMappingVlanId_Type()
)
rlLan1NonCPVlanMulticastMappingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1NonCPVlanMulticastMappingVlanId.setStatus("current")
_RlLan1x86VlanMappingTable_Object = MibTable
rlLan1x86VlanMappingTable = _RlLan1x86VlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7)
)
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingTable.setStatus("current")
_RlLan1x86VlanMappingEntry_Object = MibTableRow
rlLan1x86VlanMappingEntry = _RlLan1x86VlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1)
)
rlLan1x86VlanMappingEntry.setIndexNames(
    (0, "CISCOSBLAN1-MIB", "rlLan1x86VlanMappingVlanId"),
)
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingEntry.setStatus("current")
_RlLan1x86VlanMappingVlanId_Type = VlanId
_RlLan1x86VlanMappingVlanId_Object = MibTableColumn
rlLan1x86VlanMappingVlanId = _RlLan1x86VlanMappingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 1),
    _RlLan1x86VlanMappingVlanId_Type()
)
rlLan1x86VlanMappingVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingVlanId.setStatus("current")
_RlLan1x86VlanMappingGroupId_Type = GroupId
_RlLan1x86VlanMappingGroupId_Object = MibTableColumn
rlLan1x86VlanMappingGroupId = _RlLan1x86VlanMappingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 2),
    _RlLan1x86VlanMappingGroupId_Type()
)
rlLan1x86VlanMappingGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingGroupId.setStatus("current")
_RlLan1x86VlanMappingRowStatus_Type = RowStatus
_RlLan1x86VlanMappingRowStatus_Object = MibTableColumn
rlLan1x86VlanMappingRowStatus = _RlLan1x86VlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 7, 1, 3),
    _RlLan1x86VlanMappingRowStatus_Type()
)
rlLan1x86VlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlLan1x86VlanMappingRowStatus.setStatus("current")
_RlLan1x86MacMappingTable_Object = MibTable
rlLan1x86MacMappingTable = _RlLan1x86MacMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8)
)
if mibBuilder.loadTexts:
    rlLan1x86MacMappingTable.setStatus("current")
_RlLan1x86MacMappingEntry_Object = MibTableRow
rlLan1x86MacMappingEntry = _RlLan1x86MacMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1)
)
rlLan1x86MacMappingEntry.setIndexNames(
    (0, "CISCOSBLAN1-MIB", "rlLan1x86MacMappingDstMacAddress"),
)
if mibBuilder.loadTexts:
    rlLan1x86MacMappingEntry.setStatus("current")
_RlLan1x86MacMappingDstMacAddress_Type = MacAddress
_RlLan1x86MacMappingDstMacAddress_Object = MibTableColumn
rlLan1x86MacMappingDstMacAddress = _RlLan1x86MacMappingDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1, 1),
    _RlLan1x86MacMappingDstMacAddress_Type()
)
rlLan1x86MacMappingDstMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLan1x86MacMappingDstMacAddress.setStatus("current")
_RlLan1x86MacMappingVlanId_Type = VlanId
_RlLan1x86MacMappingVlanId_Object = MibTableColumn
rlLan1x86MacMappingVlanId = _RlLan1x86MacMappingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1, 2),
    _RlLan1x86MacMappingVlanId_Type()
)
rlLan1x86MacMappingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86MacMappingVlanId.setStatus("current")
_RlLan1x86MacMappingRowStatus_Type = RowStatus
_RlLan1x86MacMappingRowStatus_Object = MibTableColumn
rlLan1x86MacMappingRowStatus = _RlLan1x86MacMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 8, 1, 3),
    _RlLan1x86MacMappingRowStatus_Type()
)
rlLan1x86MacMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlLan1x86MacMappingRowStatus.setStatus("current")
_RlLan1x86ModulePortTable_Object = MibTable
rlLan1x86ModulePortTable = _RlLan1x86ModulePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 9)
)
if mibBuilder.loadTexts:
    rlLan1x86ModulePortTable.setStatus("current")
_RlLan1x86ModulePortEntry_Object = MibTableRow
rlLan1x86ModulePortEntry = _RlLan1x86ModulePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 9, 1)
)
rlLan1x86ModulePortEntry.setIndexNames(
    (0, "CISCOSBLAN1-MIB", "rlLan1x86ModulePortIfIndex"),
)
if mibBuilder.loadTexts:
    rlLan1x86ModulePortEntry.setStatus("current")


class _RlLan1x86ModulePortIfIndex_Type(Integer32):
    """Custom type rlLan1x86ModulePortIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RlLan1x86ModulePortIfIndex_Type.__name__ = "Integer32"
_RlLan1x86ModulePortIfIndex_Object = MibTableColumn
rlLan1x86ModulePortIfIndex = _RlLan1x86ModulePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 9, 1, 1),
    _RlLan1x86ModulePortIfIndex_Type()
)
rlLan1x86ModulePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLan1x86ModulePortIfIndex.setStatus("current")


class _RlLan1x86ModulePortCPAllowed_Type(TruthValue):
    """Custom type rlLan1x86ModulePortCPAllowed based on TruthValue"""
    defaultValue = 2


_RlLan1x86ModulePortCPAllowed_Type.__name__ = "TruthValue"
_RlLan1x86ModulePortCPAllowed_Object = MibTableColumn
rlLan1x86ModulePortCPAllowed = _RlLan1x86ModulePortCPAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 9, 1, 2),
    _RlLan1x86ModulePortCPAllowed_Type()
)
rlLan1x86ModulePortCPAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86ModulePortCPAllowed.setStatus("current")


class _RlLan1x86ModulePortCPUntaggedAllowed_Type(TruthValue):
    """Custom type rlLan1x86ModulePortCPUntaggedAllowed based on TruthValue"""
    defaultValue = 2


_RlLan1x86ModulePortCPUntaggedAllowed_Type.__name__ = "TruthValue"
_RlLan1x86ModulePortCPUntaggedAllowed_Object = MibTableColumn
rlLan1x86ModulePortCPUntaggedAllowed = _RlLan1x86ModulePortCPUntaggedAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 9, 1, 3),
    _RlLan1x86ModulePortCPUntaggedAllowed_Type()
)
rlLan1x86ModulePortCPUntaggedAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86ModulePortCPUntaggedAllowed.setStatus("current")


class _RlLan1x86ModulePortMulticastBroadcastAllowedVlan_Type(Integer32):
    """Custom type rlLan1x86ModulePortMulticastBroadcastAllowedVlan based on Integer32"""
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
        *(("none", 1),
          ("cp", 2),
          ("noncp", 3))
    )


_RlLan1x86ModulePortMulticastBroadcastAllowedVlan_Type.__name__ = "Integer32"
_RlLan1x86ModulePortMulticastBroadcastAllowedVlan_Object = MibTableColumn
rlLan1x86ModulePortMulticastBroadcastAllowedVlan = _RlLan1x86ModulePortMulticastBroadcastAllowedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 9, 1, 4),
    _RlLan1x86ModulePortMulticastBroadcastAllowedVlan_Type()
)
rlLan1x86ModulePortMulticastBroadcastAllowedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86ModulePortMulticastBroadcastAllowedVlan.setStatus("current")


class _RlLan1x86ModulePortIngressGroupId_Type(GroupId):
    """Custom type rlLan1x86ModulePortIngressGroupId based on GroupId"""
    defaultValue = 0


_RlLan1x86ModulePortIngressGroupId_Type.__name__ = "GroupId"
_RlLan1x86ModulePortIngressGroupId_Object = MibTableColumn
rlLan1x86ModulePortIngressGroupId = _RlLan1x86ModulePortIngressGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 9, 1, 5),
    _RlLan1x86ModulePortIngressGroupId_Type()
)
rlLan1x86ModulePortIngressGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86ModulePortIngressGroupId.setStatus("current")


class _RlLan1x86ModulePortEgressGroupIdList_Type(GroupIdList):
    """Custom type rlLan1x86ModulePortEgressGroupIdList based on GroupIdList"""
    defaultHexValue = ""


_RlLan1x86ModulePortEgressGroupIdList_Type.__name__ = "GroupIdList"
_RlLan1x86ModulePortEgressGroupIdList_Object = MibTableColumn
rlLan1x86ModulePortEgressGroupIdList = _RlLan1x86ModulePortEgressGroupIdList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 224, 9, 1, 6),
    _RlLan1x86ModulePortEgressGroupIdList_Type()
)
rlLan1x86ModulePortEgressGroupIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLan1x86ModulePortEgressGroupIdList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSBLAN1-MIB",
    **{"GroupId": GroupId,
       "GroupIdList": GroupIdList,
       "VlanIdOrNone": VlanIdOrNone,
       "rlLan1": rlLan1,
       "rlLan1STagEtherType": rlLan1STagEtherType,
       "rlLan1CPVlanId": rlLan1CPVlanId,
       "rlLan1CPVlanCos": rlLan1CPVlanCos,
       "rlLan1x86Port": rlLan1x86Port,
       "rlLan1CPVlanMulticastMappingVlanId": rlLan1CPVlanMulticastMappingVlanId,
       "rlLan1NonCPVlanMulticastMappingVlanId": rlLan1NonCPVlanMulticastMappingVlanId,
       "rlLan1x86VlanMappingTable": rlLan1x86VlanMappingTable,
       "rlLan1x86VlanMappingEntry": rlLan1x86VlanMappingEntry,
       "rlLan1x86VlanMappingVlanId": rlLan1x86VlanMappingVlanId,
       "rlLan1x86VlanMappingGroupId": rlLan1x86VlanMappingGroupId,
       "rlLan1x86VlanMappingRowStatus": rlLan1x86VlanMappingRowStatus,
       "rlLan1x86MacMappingTable": rlLan1x86MacMappingTable,
       "rlLan1x86MacMappingEntry": rlLan1x86MacMappingEntry,
       "rlLan1x86MacMappingDstMacAddress": rlLan1x86MacMappingDstMacAddress,
       "rlLan1x86MacMappingVlanId": rlLan1x86MacMappingVlanId,
       "rlLan1x86MacMappingRowStatus": rlLan1x86MacMappingRowStatus,
       "rlLan1x86ModulePortTable": rlLan1x86ModulePortTable,
       "rlLan1x86ModulePortEntry": rlLan1x86ModulePortEntry,
       "rlLan1x86ModulePortIfIndex": rlLan1x86ModulePortIfIndex,
       "rlLan1x86ModulePortCPAllowed": rlLan1x86ModulePortCPAllowed,
       "rlLan1x86ModulePortCPUntaggedAllowed": rlLan1x86ModulePortCPUntaggedAllowed,
       "rlLan1x86ModulePortMulticastBroadcastAllowedVlan": rlLan1x86ModulePortMulticastBroadcastAllowedVlan,
       "rlLan1x86ModulePortIngressGroupId": rlLan1x86ModulePortIngressGroupId,
       "rlLan1x86ModulePortEgressGroupIdList": rlLan1x86ModulePortEgressGroupIdList}
)
