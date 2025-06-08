# SNMP MIB module (RUIJIE-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-PRIVATE-VLAN-MIB.mib
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijiePrivateVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44)
)
if mibBuilder.loadTexts:
    ruijiePrivateVlanMIB.setRevisions(
        ("2009-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrivateVlanType(TextualConvention, Integer32):
    status = "current"
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
        *(("normal", 1),
          ("primary", 2),
          ("isolated", 3),
          ("community", 4))
    )



class VlanIndexOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_RuijiepvlanMIBObjects_ObjectIdentity = ObjectIdentity
ruijiepvlanMIBObjects = _RuijiepvlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1)
)
_RuijiepvlanVlanObjects_ObjectIdentity = ObjectIdentity
ruijiepvlanVlanObjects = _RuijiepvlanVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 1)
)
_RuijiepvlanVlanTable_Object = MibTable
ruijiepvlanVlanTable = _RuijiepvlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiepvlanVlanTable.setStatus("current")
_RuijiepvlanVlanEntry_Object = MibTableRow
ruijiepvlanVlanEntry = _RuijiepvlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 1, 1, 1)
)
ruijiepvlanVlanEntry.setIndexNames(
    (0, "RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanVlanIndex"),
)
if mibBuilder.loadTexts:
    ruijiepvlanVlanEntry.setStatus("current")
_RuijiepvlanVlanIndex_Type = VlanIndexOrZero
_RuijiepvlanVlanIndex_Object = MibTableColumn
ruijiepvlanVlanIndex = _RuijiepvlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 1, 1, 1, 1),
    _RuijiepvlanVlanIndex_Type()
)
ruijiepvlanVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiepvlanVlanIndex.setStatus("current")
_RuijiepvlanVlanPrivateVlanType_Type = PrivateVlanType
_RuijiepvlanVlanPrivateVlanType_Object = MibTableColumn
ruijiepvlanVlanPrivateVlanType = _RuijiepvlanVlanPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 1, 1, 1, 2),
    _RuijiepvlanVlanPrivateVlanType_Type()
)
ruijiepvlanVlanPrivateVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiepvlanVlanPrivateVlanType.setStatus("current")
_RuijiepvlanVlanAssociatedPrimaryVlan_Type = VlanIndexOrZero
_RuijiepvlanVlanAssociatedPrimaryVlan_Object = MibTableColumn
ruijiepvlanVlanAssociatedPrimaryVlan = _RuijiepvlanVlanAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 1, 1, 1, 3),
    _RuijiepvlanVlanAssociatedPrimaryVlan_Type()
)
ruijiepvlanVlanAssociatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiepvlanVlanAssociatedPrimaryVlan.setStatus("current")
_RuijiepvlanIfAssociatedPrimaryVlan_Type = TruthValue
_RuijiepvlanIfAssociatedPrimaryVlan_Object = MibTableColumn
ruijiepvlanIfAssociatedPrimaryVlan = _RuijiepvlanIfAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 1, 1, 1, 4),
    _RuijiepvlanIfAssociatedPrimaryVlan_Type()
)
ruijiepvlanIfAssociatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiepvlanIfAssociatedPrimaryVlan.setStatus("current")
_RuijiepvlanPortObjects_ObjectIdentity = ObjectIdentity
ruijiepvlanPortObjects = _RuijiepvlanPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2)
)
_RuijiepvlanPrivatePortTable_Object = MibTable
ruijiepvlanPrivatePortTable = _RuijiepvlanPrivatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijiepvlanPrivatePortTable.setStatus("current")
_RuijiepvlanPrivatePortEntry_Object = MibTableRow
ruijiepvlanPrivatePortEntry = _RuijiepvlanPrivatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 1, 1)
)
ruijiepvlanPrivatePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruijiepvlanPrivatePortEntry.setStatus("current")
_RuijiepvlanPrivatePortPrimaryVlan_Type = VlanIndexOrZero
_RuijiepvlanPrivatePortPrimaryVlan_Object = MibTableColumn
ruijiepvlanPrivatePortPrimaryVlan = _RuijiepvlanPrivatePortPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 1, 1, 1),
    _RuijiepvlanPrivatePortPrimaryVlan_Type()
)
ruijiepvlanPrivatePortPrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanPrivatePortPrimaryVlan.setStatus("current")
_RuijiepvlanPrivatePortSecondaryVlan_Type = VlanIndexOrZero
_RuijiepvlanPrivatePortSecondaryVlan_Object = MibTableColumn
ruijiepvlanPrivatePortSecondaryVlan = _RuijiepvlanPrivatePortSecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 1, 1, 2),
    _RuijiepvlanPrivatePortSecondaryVlan_Type()
)
ruijiepvlanPrivatePortSecondaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanPrivatePortSecondaryVlan.setStatus("current")
_RuijiepvlanPromPortTable_Object = MibTable
ruijiepvlanPromPortTable = _RuijiepvlanPromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijiepvlanPromPortTable.setStatus("current")
_RuijiepvlanPromPortEntry_Object = MibTableRow
ruijiepvlanPromPortEntry = _RuijiepvlanPromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 2, 1)
)
ruijiepvlanPromPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruijiepvlanPromPortEntry.setStatus("current")
_RuijiepvlanPrivatePortPrimaryVlanId_Type = VlanIndexOrZero
_RuijiepvlanPrivatePortPrimaryVlanId_Object = MibTableColumn
ruijiepvlanPrivatePortPrimaryVlanId = _RuijiepvlanPrivatePortPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 2, 1, 1),
    _RuijiepvlanPrivatePortPrimaryVlanId_Type()
)
ruijiepvlanPrivatePortPrimaryVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanPrivatePortPrimaryVlanId.setStatus("current")


class _RuijiepvlanPromPortSecondaryRemap_Type(OctetString):
    """Custom type ruijiepvlanPromPortSecondaryRemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RuijiepvlanPromPortSecondaryRemap_Type.__name__ = "OctetString"
_RuijiepvlanPromPortSecondaryRemap_Object = MibTableColumn
ruijiepvlanPromPortSecondaryRemap = _RuijiepvlanPromPortSecondaryRemap_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 2, 1, 2),
    _RuijiepvlanPromPortSecondaryRemap_Type()
)
ruijiepvlanPromPortSecondaryRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanPromPortSecondaryRemap.setStatus("current")


class _RuijiepvlanPromPortSecondaryRemap2k_Type(OctetString):
    """Custom type ruijiepvlanPromPortSecondaryRemap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RuijiepvlanPromPortSecondaryRemap2k_Type.__name__ = "OctetString"
_RuijiepvlanPromPortSecondaryRemap2k_Object = MibTableColumn
ruijiepvlanPromPortSecondaryRemap2k = _RuijiepvlanPromPortSecondaryRemap2k_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 2, 1, 3),
    _RuijiepvlanPromPortSecondaryRemap2k_Type()
)
ruijiepvlanPromPortSecondaryRemap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanPromPortSecondaryRemap2k.setStatus("current")


class _RuijiepvlanPromPortSecondaryRemap3k_Type(OctetString):
    """Custom type ruijiepvlanPromPortSecondaryRemap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RuijiepvlanPromPortSecondaryRemap3k_Type.__name__ = "OctetString"
_RuijiepvlanPromPortSecondaryRemap3k_Object = MibTableColumn
ruijiepvlanPromPortSecondaryRemap3k = _RuijiepvlanPromPortSecondaryRemap3k_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 2, 1, 4),
    _RuijiepvlanPromPortSecondaryRemap3k_Type()
)
ruijiepvlanPromPortSecondaryRemap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanPromPortSecondaryRemap3k.setStatus("current")


class _RuijiepvlanPromPortSecondaryRemap4k_Type(OctetString):
    """Custom type ruijiepvlanPromPortSecondaryRemap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RuijiepvlanPromPortSecondaryRemap4k_Type.__name__ = "OctetString"
_RuijiepvlanPromPortSecondaryRemap4k_Object = MibTableColumn
ruijiepvlanPromPortSecondaryRemap4k = _RuijiepvlanPromPortSecondaryRemap4k_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 2, 1, 5),
    _RuijiepvlanPromPortSecondaryRemap4k_Type()
)
ruijiepvlanPromPortSecondaryRemap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanPromPortSecondaryRemap4k.setStatus("current")
_RuijiepvlanPortModeTable_Object = MibTable
ruijiepvlanPortModeTable = _RuijiepvlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruijiepvlanPortModeTable.setStatus("current")
_RuijiepvlanPortModeEntry_Object = MibTableRow
ruijiepvlanPortModeEntry = _RuijiepvlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 3, 1)
)
ruijiepvlanPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruijiepvlanPortModeEntry.setStatus("current")


class _RuijiepvlanPortMode_Type(Integer32):
    """Custom type ruijiepvlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonPrivateVlan", 1),
          ("host", 2),
          ("promiscuous", 3))
    )


_RuijiepvlanPortMode_Type.__name__ = "Integer32"
_RuijiepvlanPortMode_Object = MibTableColumn
ruijiepvlanPortMode = _RuijiepvlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 2, 3, 1, 1),
    _RuijiepvlanPortMode_Type()
)
ruijiepvlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanPortMode.setStatus("current")
_RuijiepvlanSVIObjects_ObjectIdentity = ObjectIdentity
ruijiepvlanSVIObjects = _RuijiepvlanSVIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 3)
)
_RuijiepvlanSVIMappingTable_Object = MibTable
ruijiepvlanSVIMappingTable = _RuijiepvlanSVIMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijiepvlanSVIMappingTable.setStatus("current")
_RuijiepvlanSVIMappingEntry_Object = MibTableRow
ruijiepvlanSVIMappingEntry = _RuijiepvlanSVIMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 3, 1, 1)
)
ruijiepvlanSVIMappingEntry.setIndexNames(
    (0, "RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanSVIMappingVlanIndex"),
)
if mibBuilder.loadTexts:
    ruijiepvlanSVIMappingEntry.setStatus("current")
_RuijiepvlanSVIMappingVlanIndex_Type = VlanIndexOrZero
_RuijiepvlanSVIMappingVlanIndex_Object = MibTableColumn
ruijiepvlanSVIMappingVlanIndex = _RuijiepvlanSVIMappingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 3, 1, 1, 1),
    _RuijiepvlanSVIMappingVlanIndex_Type()
)
ruijiepvlanSVIMappingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiepvlanSVIMappingVlanIndex.setStatus("current")
_RuijiepvlanSVIMappingPrimarySVI_Type = VlanIndexOrZero
_RuijiepvlanSVIMappingPrimarySVI_Object = MibTableColumn
ruijiepvlanSVIMappingPrimarySVI = _RuijiepvlanSVIMappingPrimarySVI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 1, 3, 1, 1, 2),
    _RuijiepvlanSVIMappingPrimarySVI_Type()
)
ruijiepvlanSVIMappingPrimarySVI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiepvlanSVIMappingPrimarySVI.setStatus("current")
_RuijiepvlanMIBConformance_ObjectIdentity = ObjectIdentity
ruijiepvlanMIBConformance = _RuijiepvlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2)
)
_RuijiepvlanMIBCompliances_ObjectIdentity = ObjectIdentity
ruijiepvlanMIBCompliances = _RuijiepvlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2, 1)
)
_RuijiepvlanMIBGroups_ObjectIdentity = ObjectIdentity
ruijiepvlanMIBGroups = _RuijiepvlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2, 2)
)

# Managed Objects groups

ruijiepvlanVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2, 2, 1)
)
ruijiepvlanVlanGroup.setObjects(
      *(("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanVlanIndex"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanVlanPrivateVlanType"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanVlanAssociatedPrimaryVlan"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanIfAssociatedPrimaryVlan"))
)
if mibBuilder.loadTexts:
    ruijiepvlanVlanGroup.setStatus("current")

ruijiepvlanPrivatePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2, 2, 2)
)
ruijiepvlanPrivatePortGroup.setObjects(
      *(("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPrivatePortPrimaryVlan"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPrivatePortSecondaryVlan"))
)
if mibBuilder.loadTexts:
    ruijiepvlanPrivatePortGroup.setStatus("current")

ruijiepvlanPromPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2, 2, 3)
)
ruijiepvlanPromPortGroup.setObjects(
      *(("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPrivatePortPrimaryVlan"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPromPortSecondaryRemap"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPromPortSecondaryRemap2k"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPromPortSecondaryRemap3k"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPromPortSecondaryRemap4k"))
)
if mibBuilder.loadTexts:
    ruijiepvlanPromPortGroup.setStatus("current")

ruijiepvlanPortModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2, 2, 4)
)
ruijiepvlanPortModeGroup.setObjects(
    ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPortMode")
)
if mibBuilder.loadTexts:
    ruijiepvlanPortModeGroup.setStatus("current")

ruijiepvlanSVIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2, 2, 5)
)
ruijiepvlanSVIGroup.setObjects(
    ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanSVIMappingPrimarySVI")
)
if mibBuilder.loadTexts:
    ruijiepvlanSVIGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijiepvlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 44, 2, 1, 1)
)
ruijiepvlanMIBCompliance.setObjects(
      *(("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanVlanGroup"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPrivatePortGroup"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPromPortGroup"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanPortModeGroup"),
        ("RUIJIE-PRIVATE-VLAN-MIB", "ruijiepvlanSVIGroup"))
)
if mibBuilder.loadTexts:
    ruijiepvlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PRIVATE-VLAN-MIB",
    **{"PrivateVlanType": PrivateVlanType,
       "VlanIndexOrZero": VlanIndexOrZero,
       "ruijiePrivateVlanMIB": ruijiePrivateVlanMIB,
       "ruijiepvlanMIBObjects": ruijiepvlanMIBObjects,
       "ruijiepvlanVlanObjects": ruijiepvlanVlanObjects,
       "ruijiepvlanVlanTable": ruijiepvlanVlanTable,
       "ruijiepvlanVlanEntry": ruijiepvlanVlanEntry,
       "ruijiepvlanVlanIndex": ruijiepvlanVlanIndex,
       "ruijiepvlanVlanPrivateVlanType": ruijiepvlanVlanPrivateVlanType,
       "ruijiepvlanVlanAssociatedPrimaryVlan": ruijiepvlanVlanAssociatedPrimaryVlan,
       "ruijiepvlanIfAssociatedPrimaryVlan": ruijiepvlanIfAssociatedPrimaryVlan,
       "ruijiepvlanPortObjects": ruijiepvlanPortObjects,
       "ruijiepvlanPrivatePortTable": ruijiepvlanPrivatePortTable,
       "ruijiepvlanPrivatePortEntry": ruijiepvlanPrivatePortEntry,
       "ruijiepvlanPrivatePortPrimaryVlan": ruijiepvlanPrivatePortPrimaryVlan,
       "ruijiepvlanPrivatePortSecondaryVlan": ruijiepvlanPrivatePortSecondaryVlan,
       "ruijiepvlanPromPortTable": ruijiepvlanPromPortTable,
       "ruijiepvlanPromPortEntry": ruijiepvlanPromPortEntry,
       "ruijiepvlanPrivatePortPrimaryVlanId": ruijiepvlanPrivatePortPrimaryVlanId,
       "ruijiepvlanPromPortSecondaryRemap": ruijiepvlanPromPortSecondaryRemap,
       "ruijiepvlanPromPortSecondaryRemap2k": ruijiepvlanPromPortSecondaryRemap2k,
       "ruijiepvlanPromPortSecondaryRemap3k": ruijiepvlanPromPortSecondaryRemap3k,
       "ruijiepvlanPromPortSecondaryRemap4k": ruijiepvlanPromPortSecondaryRemap4k,
       "ruijiepvlanPortModeTable": ruijiepvlanPortModeTable,
       "ruijiepvlanPortModeEntry": ruijiepvlanPortModeEntry,
       "ruijiepvlanPortMode": ruijiepvlanPortMode,
       "ruijiepvlanSVIObjects": ruijiepvlanSVIObjects,
       "ruijiepvlanSVIMappingTable": ruijiepvlanSVIMappingTable,
       "ruijiepvlanSVIMappingEntry": ruijiepvlanSVIMappingEntry,
       "ruijiepvlanSVIMappingVlanIndex": ruijiepvlanSVIMappingVlanIndex,
       "ruijiepvlanSVIMappingPrimarySVI": ruijiepvlanSVIMappingPrimarySVI,
       "ruijiepvlanMIBConformance": ruijiepvlanMIBConformance,
       "ruijiepvlanMIBCompliances": ruijiepvlanMIBCompliances,
       "ruijiepvlanMIBCompliance": ruijiepvlanMIBCompliance,
       "ruijiepvlanMIBGroups": ruijiepvlanMIBGroups,
       "ruijiepvlanVlanGroup": ruijiepvlanVlanGroup,
       "ruijiepvlanPrivatePortGroup": ruijiepvlanPrivatePortGroup,
       "ruijiepvlanPromPortGroup": ruijiepvlanPromPortGroup,
       "ruijiepvlanPortModeGroup": ruijiepvlanPortModeGroup,
       "ruijiepvlanSVIGroup": ruijiepvlanSVIGroup}
)
