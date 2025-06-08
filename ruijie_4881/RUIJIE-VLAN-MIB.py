# SNMP MIB module (RUIJIE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VLAN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

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

ruijieVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9)
)
if mibBuilder.loadTexts:
    ruijieVlanMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_RuijieVlanMIBObjects_ObjectIdentity = ObjectIdentity
ruijieVlanMIBObjects = _RuijieVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1)
)
_RuijieVlanMaxNumber_Type = Integer32
_RuijieVlanMaxNumber_Object = MibScalar
ruijieVlanMaxNumber = _RuijieVlanMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 1),
    _RuijieVlanMaxNumber_Type()
)
ruijieVlanMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVlanMaxNumber.setStatus("current")
_RuijieVlanCurrentNumber_Type = Integer32
_RuijieVlanCurrentNumber_Object = MibScalar
ruijieVlanCurrentNumber = _RuijieVlanCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 2),
    _RuijieVlanCurrentNumber_Type()
)
ruijieVlanCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVlanCurrentNumber.setStatus("current")
_RuijieSystemMaxVID_Type = Integer32
_RuijieSystemMaxVID_Object = MibScalar
ruijieSystemMaxVID = _RuijieSystemMaxVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 3),
    _RuijieSystemMaxVID_Type()
)
ruijieSystemMaxVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMaxVID.setStatus("current")
_RuijieVlanIfConfigTable_Object = MibTable
ruijieVlanIfConfigTable = _RuijieVlanIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieVlanIfConfigTable.setStatus("obsolete")
_RuijieVlanIfConfigEntry_Object = MibTableRow
ruijieVlanIfConfigEntry = _RuijieVlanIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1)
)
ruijieVlanIfConfigEntry.setIndexNames(
    (0, "RUIJIE-VLAN-MIB", "ruijieVlanIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieVlanIfConfigEntry.setStatus("obsolete")
_RuijieVlanIfConfigIfIndex_Type = IfIndex
_RuijieVlanIfConfigIfIndex_Object = MibTableColumn
ruijieVlanIfConfigIfIndex = _RuijieVlanIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1, 1),
    _RuijieVlanIfConfigIfIndex_Type()
)
ruijieVlanIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVlanIfConfigIfIndex.setStatus("obsolete")
_RuijieVlanIfAccessVlan_Type = VlanId
_RuijieVlanIfAccessVlan_Object = MibTableColumn
ruijieVlanIfAccessVlan = _RuijieVlanIfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1, 2),
    _RuijieVlanIfAccessVlan_Type()
)
ruijieVlanIfAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVlanIfAccessVlan.setStatus("obsolete")
_RuijieVlanIfNativeVlan_Type = VlanId
_RuijieVlanIfNativeVlan_Object = MibTableColumn
ruijieVlanIfNativeVlan = _RuijieVlanIfNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1, 3),
    _RuijieVlanIfNativeVlan_Type()
)
ruijieVlanIfNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVlanIfNativeVlan.setStatus("obsolete")


class _RuijieVlanIfAllowedVlanList_Type(OctetString):
    """Custom type ruijieVlanIfAllowedVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_RuijieVlanIfAllowedVlanList_Type.__name__ = "OctetString"
_RuijieVlanIfAllowedVlanList_Object = MibTableColumn
ruijieVlanIfAllowedVlanList = _RuijieVlanIfAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1, 4),
    _RuijieVlanIfAllowedVlanList_Type()
)
ruijieVlanIfAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVlanIfAllowedVlanList.setStatus("obsolete")
_RuijieVlanTable_Object = MibTable
ruijieVlanTable = _RuijieVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieVlanTable.setStatus("obsolete")
_RuijieVlanEntry_Object = MibTableRow
ruijieVlanEntry = _RuijieVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1)
)
ruijieVlanEntry.setIndexNames(
    (0, "RUIJIE-VLAN-MIB", "ruijieVlanVID"),
)
if mibBuilder.loadTexts:
    ruijieVlanEntry.setStatus("obsolete")
_RuijieVlanVID_Type = VlanId
_RuijieVlanVID_Object = MibTableColumn
ruijieVlanVID = _RuijieVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 1),
    _RuijieVlanVID_Type()
)
ruijieVlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVlanVID.setStatus("obsolete")
_RuijieVlanPortMemberAction_Type = MemberMap
_RuijieVlanPortMemberAction_Object = MibTableColumn
ruijieVlanPortMemberAction = _RuijieVlanPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 2),
    _RuijieVlanPortMemberAction_Type()
)
ruijieVlanPortMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVlanPortMemberAction.setStatus("obsolete")
_RuijieVlanApMemberAction_Type = MemberMap
_RuijieVlanApMemberAction_Object = MibTableColumn
ruijieVlanApMemberAction = _RuijieVlanApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 3),
    _RuijieVlanApMemberAction_Type()
)
ruijieVlanApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVlanApMemberAction.setStatus("obsolete")


class _RuijieVlanAlias_Type(DisplayString):
    """Custom type ruijieVlanAlias based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieVlanAlias_Type.__name__ = "DisplayString"
_RuijieVlanAlias_Object = MibTableColumn
ruijieVlanAlias = _RuijieVlanAlias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 4),
    _RuijieVlanAlias_Type()
)
ruijieVlanAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVlanAlias.setStatus("obsolete")
_RuijieVlanEntryStatus_Type = ConfigStatus
_RuijieVlanEntryStatus_Object = MibTableColumn
ruijieVlanEntryStatus = _RuijieVlanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 5),
    _RuijieVlanEntryStatus_Type()
)
ruijieVlanEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVlanEntryStatus.setStatus("obsolete")
_RuijieVlanPortConfigTable_Object = MibTable
ruijieVlanPortConfigTable = _RuijieVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieVlanPortConfigTable.setStatus("current")
_RuijieVlanPortConfigEntry_Object = MibTableRow
ruijieVlanPortConfigEntry = _RuijieVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1)
)
ruijieVlanPortConfigEntry.setIndexNames(
    (0, "RUIJIE-VLAN-MIB", "ruijieVlanPortConfigIndex"),
)
if mibBuilder.loadTexts:
    ruijieVlanPortConfigEntry.setStatus("current")
_RuijieVlanPortConfigIndex_Type = IfIndex
_RuijieVlanPortConfigIndex_Object = MibTableColumn
ruijieVlanPortConfigIndex = _RuijieVlanPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 1),
    _RuijieVlanPortConfigIndex_Type()
)
ruijieVlanPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVlanPortConfigIndex.setStatus("current")


class _RuijieVlanPortConfigMode_Type(Integer32):
    """Custom type ruijieVlanPortConfigMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2),
          ("dot1q-tunnel", 3),
          ("hybrid", 4),
          ("other", 5),
          ("uplink", 6),
          ("host", 7),
          ("promiscuous", 8))
    )


_RuijieVlanPortConfigMode_Type.__name__ = "Integer32"
_RuijieVlanPortConfigMode_Object = MibTableColumn
ruijieVlanPortConfigMode = _RuijieVlanPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 2),
    _RuijieVlanPortConfigMode_Type()
)
ruijieVlanPortConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVlanPortConfigMode.setStatus("current")
_RuijieVlanPortAccessVlan_Type = VlanId
_RuijieVlanPortAccessVlan_Object = MibTableColumn
ruijieVlanPortAccessVlan = _RuijieVlanPortAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 3),
    _RuijieVlanPortAccessVlan_Type()
)
ruijieVlanPortAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVlanPortAccessVlan.setStatus("current")
_RuijieVlanPortNativeVlan_Type = VlanId
_RuijieVlanPortNativeVlan_Object = MibTableColumn
ruijieVlanPortNativeVlan = _RuijieVlanPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 4),
    _RuijieVlanPortNativeVlan_Type()
)
ruijieVlanPortNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVlanPortNativeVlan.setStatus("current")
_RuijieVlanPortAllowedVlanList_Type = VlanList
_RuijieVlanPortAllowedVlanList_Object = MibTableColumn
ruijieVlanPortAllowedVlanList = _RuijieVlanPortAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 5),
    _RuijieVlanPortAllowedVlanList_Type()
)
ruijieVlanPortAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVlanPortAllowedVlanList.setStatus("current")
_RuijieIfVlanID_Type = Integer32
_RuijieIfVlanID_Object = MibTableColumn
ruijieIfVlanID = _RuijieIfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 6, 1, 6),
    _RuijieIfVlanID_Type()
)
ruijieIfVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfVlanID.setStatus("current")
_RuijieVlanConfigTable_Object = MibTable
ruijieVlanConfigTable = _RuijieVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieVlanConfigTable.setStatus("current")
_RuijieVlanConfigEntry_Object = MibTableRow
ruijieVlanConfigEntry = _RuijieVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1)
)
ruijieVlanConfigEntry.setIndexNames(
    (0, "RUIJIE-VLAN-MIB", "ruijieVlanConfigVID"),
)
if mibBuilder.loadTexts:
    ruijieVlanConfigEntry.setStatus("current")
_RuijieVlanConfigVID_Type = VlanId
_RuijieVlanConfigVID_Object = MibTableColumn
ruijieVlanConfigVID = _RuijieVlanConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 1),
    _RuijieVlanConfigVID_Type()
)
ruijieVlanConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVlanConfigVID.setStatus("current")
_RuijieVlanConfigAction_Type = Integer32
_RuijieVlanConfigAction_Object = MibTableColumn
ruijieVlanConfigAction = _RuijieVlanConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 2),
    _RuijieVlanConfigAction_Type()
)
ruijieVlanConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVlanConfigAction.setStatus("current")
_RuijieVlanConfigName_Type = DisplayString
_RuijieVlanConfigName_Object = MibTableColumn
ruijieVlanConfigName = _RuijieVlanConfigName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 3),
    _RuijieVlanConfigName_Type()
)
ruijieVlanConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVlanConfigName.setStatus("current")
_RuijieVlanConfigPortMember_Type = PortList
_RuijieVlanConfigPortMember_Object = MibTableColumn
ruijieVlanConfigPortMember = _RuijieVlanConfigPortMember_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 7, 1, 4),
    _RuijieVlanConfigPortMember_Type()
)
ruijieVlanConfigPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVlanConfigPortMember.setStatus("current")
_RuijieVlanMIBConformance_ObjectIdentity = ObjectIdentity
ruijieVlanMIBConformance = _RuijieVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2)
)
_RuijieVlanMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieVlanMIBCompliances = _RuijieVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2, 1)
)
_RuijieVlanMIBGroups_ObjectIdentity = ObjectIdentity
ruijieVlanMIBGroups = _RuijieVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2, 2)
)

# Managed Objects groups

ruijieVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2, 2, 1)
)
ruijieVlanMIBGroup.setObjects(
      *(("RUIJIE-VLAN-MIB", "ruijieVlanMaxNumber"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanCurrentNumber"),
        ("RUIJIE-VLAN-MIB", "ruijieSystemMaxVID"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanIfAccessVlan"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanIfNativeVlan"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanIfAllowedVlanList"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanVID"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanApMemberAction"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanPortMemberAction"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanAlias"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanEntryStatus"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanPortConfigMode"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanPortAccessVlan"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanPortNativeVlan"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanPortAllowedVlanList"),
        ("RUIJIE-VLAN-MIB", "ruijieIfVlanID"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanConfigVID"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanConfigAction"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanConfigName"),
        ("RUIJIE-VLAN-MIB", "ruijieVlanConfigPortMember"))
)
if mibBuilder.loadTexts:
    ruijieVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2, 1, 1)
)
ruijieVlanMIBCompliance.setObjects(
    ("RUIJIE-VLAN-MIB", "ruijieVlanMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VLAN-MIB",
    **{"VlanList": VlanList,
       "ruijieVlanMIB": ruijieVlanMIB,
       "ruijieVlanMIBObjects": ruijieVlanMIBObjects,
       "ruijieVlanMaxNumber": ruijieVlanMaxNumber,
       "ruijieVlanCurrentNumber": ruijieVlanCurrentNumber,
       "ruijieSystemMaxVID": ruijieSystemMaxVID,
       "ruijieVlanIfConfigTable": ruijieVlanIfConfigTable,
       "ruijieVlanIfConfigEntry": ruijieVlanIfConfigEntry,
       "ruijieVlanIfConfigIfIndex": ruijieVlanIfConfigIfIndex,
       "ruijieVlanIfAccessVlan": ruijieVlanIfAccessVlan,
       "ruijieVlanIfNativeVlan": ruijieVlanIfNativeVlan,
       "ruijieVlanIfAllowedVlanList": ruijieVlanIfAllowedVlanList,
       "ruijieVlanTable": ruijieVlanTable,
       "ruijieVlanEntry": ruijieVlanEntry,
       "ruijieVlanVID": ruijieVlanVID,
       "ruijieVlanPortMemberAction": ruijieVlanPortMemberAction,
       "ruijieVlanApMemberAction": ruijieVlanApMemberAction,
       "ruijieVlanAlias": ruijieVlanAlias,
       "ruijieVlanEntryStatus": ruijieVlanEntryStatus,
       "ruijieVlanPortConfigTable": ruijieVlanPortConfigTable,
       "ruijieVlanPortConfigEntry": ruijieVlanPortConfigEntry,
       "ruijieVlanPortConfigIndex": ruijieVlanPortConfigIndex,
       "ruijieVlanPortConfigMode": ruijieVlanPortConfigMode,
       "ruijieVlanPortAccessVlan": ruijieVlanPortAccessVlan,
       "ruijieVlanPortNativeVlan": ruijieVlanPortNativeVlan,
       "ruijieVlanPortAllowedVlanList": ruijieVlanPortAllowedVlanList,
       "ruijieIfVlanID": ruijieIfVlanID,
       "ruijieVlanConfigTable": ruijieVlanConfigTable,
       "ruijieVlanConfigEntry": ruijieVlanConfigEntry,
       "ruijieVlanConfigVID": ruijieVlanConfigVID,
       "ruijieVlanConfigAction": ruijieVlanConfigAction,
       "ruijieVlanConfigName": ruijieVlanConfigName,
       "ruijieVlanConfigPortMember": ruijieVlanConfigPortMember,
       "ruijieVlanMIBConformance": ruijieVlanMIBConformance,
       "ruijieVlanMIBCompliances": ruijieVlanMIBCompliances,
       "ruijieVlanMIBCompliance": ruijieVlanMIBCompliance,
       "ruijieVlanMIBGroups": ruijieVlanMIBGroups,
       "ruijieVlanMIBGroup": ruijieVlanMIBGroup}
)
