# SNMP MIB module (CIE1000-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-VLAN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000DisplayString,
 CIE1000EtherType,
 CIE1000InterfaceIndex,
 CIE1000PortList,
 CIE1000RowEditorState,
 CIE1000Unsigned16,
 CIE1000Vlan,
 CIE1000VlanListQuarter) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000EtherType",
    "CIE1000InterfaceIndex",
    "CIE1000PortList",
    "CIE1000RowEditorState",
    "CIE1000Unsigned16",
    "CIE1000Vlan",
    "CIE1000VlanListQuarter")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

cie1000VlanMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13)
)
if mibBuilder.loadTexts:
    cie1000VlanMib.setRevisions(
        ("2015-01-16 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000VlanEgressTagging(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("untagThis", 0),
          ("tagThis", 1),
          ("tagAll", 2),
          ("untagAll", 3))
    )



class CIE1000VlanIngressAcceptance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("tagged", 1),
          ("untagged", 2))
    )



class CIE1000VlanPortMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("trunk", 1),
          ("hybrid", 2))
    )



class CIE1000VlanPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unaware", 0),
          ("c", 1),
          ("s", 2),
          ("sCustom", 3))
    )



class CIE1000VlanUserType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("combined", 0),
          ("admin", 1),
          ("dot1x", 3),
          ("mvrp", 4),
          ("gvrp", 5),
          ("mvr", 6),
          ("voiceVlan", 7),
          ("mstp", 8),
          ("erps", 9),
          ("mep", 10),
          ("evc", 11),
          ("vcl", 12),
          ("rmirror", 13))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000VlanMibObjects_ObjectIdentity = ObjectIdentity
cie1000VlanMibObjects = _Cie1000VlanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1)
)
_Cie1000VlanCapabilities_ObjectIdentity = ObjectIdentity
cie1000VlanCapabilities = _Cie1000VlanCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 1)
)
_Cie1000VlanCapabilitiesVlanIdMin_Type = CIE1000Vlan
_Cie1000VlanCapabilitiesVlanIdMin_Object = MibScalar
cie1000VlanCapabilitiesVlanIdMin = _Cie1000VlanCapabilitiesVlanIdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 1, 1),
    _Cie1000VlanCapabilitiesVlanIdMin_Type()
)
cie1000VlanCapabilitiesVlanIdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanCapabilitiesVlanIdMin.setStatus("current")
_Cie1000VlanCapabilitiesVlanIdMax_Type = CIE1000Vlan
_Cie1000VlanCapabilitiesVlanIdMax_Object = MibScalar
cie1000VlanCapabilitiesVlanIdMax = _Cie1000VlanCapabilitiesVlanIdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 1, 2),
    _Cie1000VlanCapabilitiesVlanIdMax_Type()
)
cie1000VlanCapabilitiesVlanIdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanCapabilitiesVlanIdMax.setStatus("current")
_Cie1000VlanCapabilitiesFidCnt_Type = CIE1000Unsigned16
_Cie1000VlanCapabilitiesFidCnt_Object = MibScalar
cie1000VlanCapabilitiesFidCnt = _Cie1000VlanCapabilitiesFidCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 1, 3),
    _Cie1000VlanCapabilitiesFidCnt_Type()
)
cie1000VlanCapabilitiesFidCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanCapabilitiesFidCnt.setStatus("current")
_Cie1000VlanConfig_ObjectIdentity = ObjectIdentity
cie1000VlanConfig = _Cie1000VlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2)
)
_Cie1000VlanConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000VlanConfigGlobals = _Cie1000VlanConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1)
)
_Cie1000VlanConfigGlobalsMain_ObjectIdentity = ObjectIdentity
cie1000VlanConfigGlobalsMain = _Cie1000VlanConfigGlobalsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 1)
)


class _Cie1000VlanConfigGlobalsMainCustomSPortEtherType_Type(CIE1000EtherType):
    """Custom type cie1000VlanConfigGlobalsMainCustomSPortEtherType based on CIE1000EtherType"""
    subtypeSpec = CIE1000EtherType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_Cie1000VlanConfigGlobalsMainCustomSPortEtherType_Type.__name__ = "CIE1000EtherType"
_Cie1000VlanConfigGlobalsMainCustomSPortEtherType_Object = MibScalar
cie1000VlanConfigGlobalsMainCustomSPortEtherType = _Cie1000VlanConfigGlobalsMainCustomSPortEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 1, 1),
    _Cie1000VlanConfigGlobalsMainCustomSPortEtherType_Type()
)
cie1000VlanConfigGlobalsMainCustomSPortEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsMainCustomSPortEtherType.setStatus("current")
_Cie1000VlanConfigGlobalsMainAccessVlans0To1K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigGlobalsMainAccessVlans0To1K_Object = MibScalar
cie1000VlanConfigGlobalsMainAccessVlans0To1K = _Cie1000VlanConfigGlobalsMainAccessVlans0To1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 1, 2),
    _Cie1000VlanConfigGlobalsMainAccessVlans0To1K_Type()
)
cie1000VlanConfigGlobalsMainAccessVlans0To1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsMainAccessVlans0To1K.setStatus("current")
_Cie1000VlanConfigGlobalsMainAccessVlans1KTo2K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigGlobalsMainAccessVlans1KTo2K_Object = MibScalar
cie1000VlanConfigGlobalsMainAccessVlans1KTo2K = _Cie1000VlanConfigGlobalsMainAccessVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 1, 3),
    _Cie1000VlanConfigGlobalsMainAccessVlans1KTo2K_Type()
)
cie1000VlanConfigGlobalsMainAccessVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsMainAccessVlans1KTo2K.setStatus("current")
_Cie1000VlanConfigGlobalsMainAccessVlans2KTo3K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigGlobalsMainAccessVlans2KTo3K_Object = MibScalar
cie1000VlanConfigGlobalsMainAccessVlans2KTo3K = _Cie1000VlanConfigGlobalsMainAccessVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 1, 4),
    _Cie1000VlanConfigGlobalsMainAccessVlans2KTo3K_Type()
)
cie1000VlanConfigGlobalsMainAccessVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsMainAccessVlans2KTo3K.setStatus("current")
_Cie1000VlanConfigGlobalsMainAccessVlans3KTo4K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigGlobalsMainAccessVlans3KTo4K_Object = MibScalar
cie1000VlanConfigGlobalsMainAccessVlans3KTo4K = _Cie1000VlanConfigGlobalsMainAccessVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 1, 5),
    _Cie1000VlanConfigGlobalsMainAccessVlans3KTo4K_Type()
)
cie1000VlanConfigGlobalsMainAccessVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsMainAccessVlans3KTo4K.setStatus("current")
_Cie1000VlanConfigGlobalsNameTable_Object = MibTable
cie1000VlanConfigGlobalsNameTable = _Cie1000VlanConfigGlobalsNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsNameTable.setStatus("current")
_Cie1000VlanConfigGlobalsNameEntry_Object = MibTableRow
cie1000VlanConfigGlobalsNameEntry = _Cie1000VlanConfigGlobalsNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 2, 1)
)
cie1000VlanConfigGlobalsNameEntry.setIndexNames(
    (0, "CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsNameVlanId"),
)
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsNameEntry.setStatus("current")
_Cie1000VlanConfigGlobalsNameVlanId_Type = CIE1000Vlan
_Cie1000VlanConfigGlobalsNameVlanId_Object = MibTableColumn
cie1000VlanConfigGlobalsNameVlanId = _Cie1000VlanConfigGlobalsNameVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 2, 1, 1),
    _Cie1000VlanConfigGlobalsNameVlanId_Type()
)
cie1000VlanConfigGlobalsNameVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsNameVlanId.setStatus("current")


class _Cie1000VlanConfigGlobalsNameName_Type(CIE1000DisplayString):
    """Custom type cie1000VlanConfigGlobalsNameName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000VlanConfigGlobalsNameName_Type.__name__ = "CIE1000DisplayString"
_Cie1000VlanConfigGlobalsNameName_Object = MibTableColumn
cie1000VlanConfigGlobalsNameName = _Cie1000VlanConfigGlobalsNameName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 1, 2, 1, 2),
    _Cie1000VlanConfigGlobalsNameName_Type()
)
cie1000VlanConfigGlobalsNameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsNameName.setStatus("current")
_Cie1000VlanConfigInterfaces_ObjectIdentity = ObjectIdentity
cie1000VlanConfigInterfaces = _Cie1000VlanConfigInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2)
)
_Cie1000VlanConfigInterfacesTable_Object = MibTable
cie1000VlanConfigInterfacesTable = _Cie1000VlanConfigInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesTable.setStatus("current")
_Cie1000VlanConfigInterfacesEntry_Object = MibTableRow
cie1000VlanConfigInterfacesEntry = _Cie1000VlanConfigInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1)
)
cie1000VlanConfigInterfacesEntry.setIndexNames(
    (0, "CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesEntry.setStatus("current")
_Cie1000VlanConfigInterfacesIfIndex_Type = CIE1000InterfaceIndex
_Cie1000VlanConfigInterfacesIfIndex_Object = MibTableColumn
cie1000VlanConfigInterfacesIfIndex = _Cie1000VlanConfigInterfacesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 1),
    _Cie1000VlanConfigInterfacesIfIndex_Type()
)
cie1000VlanConfigInterfacesIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesIfIndex.setStatus("current")
_Cie1000VlanConfigInterfacesMode_Type = CIE1000VlanPortMode
_Cie1000VlanConfigInterfacesMode_Object = MibTableColumn
cie1000VlanConfigInterfacesMode = _Cie1000VlanConfigInterfacesMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 2),
    _Cie1000VlanConfigInterfacesMode_Type()
)
cie1000VlanConfigInterfacesMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesMode.setStatus("current")
_Cie1000VlanConfigInterfacesAccessVlan_Type = CIE1000Vlan
_Cie1000VlanConfigInterfacesAccessVlan_Object = MibTableColumn
cie1000VlanConfigInterfacesAccessVlan = _Cie1000VlanConfigInterfacesAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 3),
    _Cie1000VlanConfigInterfacesAccessVlan_Type()
)
cie1000VlanConfigInterfacesAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesAccessVlan.setStatus("current")
_Cie1000VlanConfigInterfacesTrunkNativeVlan_Type = CIE1000Vlan
_Cie1000VlanConfigInterfacesTrunkNativeVlan_Object = MibTableColumn
cie1000VlanConfigInterfacesTrunkNativeVlan = _Cie1000VlanConfigInterfacesTrunkNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 4),
    _Cie1000VlanConfigInterfacesTrunkNativeVlan_Type()
)
cie1000VlanConfigInterfacesTrunkNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesTrunkNativeVlan.setStatus("current")
_Cie1000VlanConfigInterfacesTrunkTagNativeVlan_Type = TruthValue
_Cie1000VlanConfigInterfacesTrunkTagNativeVlan_Object = MibTableColumn
cie1000VlanConfigInterfacesTrunkTagNativeVlan = _Cie1000VlanConfigInterfacesTrunkTagNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 5),
    _Cie1000VlanConfigInterfacesTrunkTagNativeVlan_Type()
)
cie1000VlanConfigInterfacesTrunkTagNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesTrunkTagNativeVlan.setStatus("current")
_Cie1000VlanConfigInterfacesTrunkVlans0KTo1K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesTrunkVlans0KTo1K_Object = MibTableColumn
cie1000VlanConfigInterfacesTrunkVlans0KTo1K = _Cie1000VlanConfigInterfacesTrunkVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 6),
    _Cie1000VlanConfigInterfacesTrunkVlans0KTo1K_Type()
)
cie1000VlanConfigInterfacesTrunkVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesTrunkVlans0KTo1K.setStatus("current")
_Cie1000VlanConfigInterfacesTrunkVlans1KTo2K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesTrunkVlans1KTo2K_Object = MibTableColumn
cie1000VlanConfigInterfacesTrunkVlans1KTo2K = _Cie1000VlanConfigInterfacesTrunkVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 7),
    _Cie1000VlanConfigInterfacesTrunkVlans1KTo2K_Type()
)
cie1000VlanConfigInterfacesTrunkVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesTrunkVlans1KTo2K.setStatus("current")
_Cie1000VlanConfigInterfacesTrunkVlans2KTo3K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesTrunkVlans2KTo3K_Object = MibTableColumn
cie1000VlanConfigInterfacesTrunkVlans2KTo3K = _Cie1000VlanConfigInterfacesTrunkVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 8),
    _Cie1000VlanConfigInterfacesTrunkVlans2KTo3K_Type()
)
cie1000VlanConfigInterfacesTrunkVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesTrunkVlans2KTo3K.setStatus("current")
_Cie1000VlanConfigInterfacesTrunkVlans3KTo4K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesTrunkVlans3KTo4K_Object = MibTableColumn
cie1000VlanConfigInterfacesTrunkVlans3KTo4K = _Cie1000VlanConfigInterfacesTrunkVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 9),
    _Cie1000VlanConfigInterfacesTrunkVlans3KTo4K_Type()
)
cie1000VlanConfigInterfacesTrunkVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesTrunkVlans3KTo4K.setStatus("current")
_Cie1000VlanConfigInterfacesHybridNativeVlan_Type = CIE1000Vlan
_Cie1000VlanConfigInterfacesHybridNativeVlan_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridNativeVlan = _Cie1000VlanConfigInterfacesHybridNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 10),
    _Cie1000VlanConfigInterfacesHybridNativeVlan_Type()
)
cie1000VlanConfigInterfacesHybridNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridNativeVlan.setStatus("current")
_Cie1000VlanConfigInterfacesHybridPortType_Type = CIE1000VlanPortType
_Cie1000VlanConfigInterfacesHybridPortType_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridPortType = _Cie1000VlanConfigInterfacesHybridPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 11),
    _Cie1000VlanConfigInterfacesHybridPortType_Type()
)
cie1000VlanConfigInterfacesHybridPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridPortType.setStatus("current")
_Cie1000VlanConfigInterfacesHybridIngressFiltering_Type = TruthValue
_Cie1000VlanConfigInterfacesHybridIngressFiltering_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridIngressFiltering = _Cie1000VlanConfigInterfacesHybridIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 12),
    _Cie1000VlanConfigInterfacesHybridIngressFiltering_Type()
)
cie1000VlanConfigInterfacesHybridIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridIngressFiltering.setStatus("current")
_Cie1000VlanConfigInterfacesHybridIngressAcceptance_Type = CIE1000VlanIngressAcceptance
_Cie1000VlanConfigInterfacesHybridIngressAcceptance_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridIngressAcceptance = _Cie1000VlanConfigInterfacesHybridIngressAcceptance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 13),
    _Cie1000VlanConfigInterfacesHybridIngressAcceptance_Type()
)
cie1000VlanConfigInterfacesHybridIngressAcceptance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridIngressAcceptance.setStatus("current")
_Cie1000VlanConfigInterfacesHybridEgressTagging_Type = CIE1000VlanEgressTagging
_Cie1000VlanConfigInterfacesHybridEgressTagging_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridEgressTagging = _Cie1000VlanConfigInterfacesHybridEgressTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 14),
    _Cie1000VlanConfigInterfacesHybridEgressTagging_Type()
)
cie1000VlanConfigInterfacesHybridEgressTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridEgressTagging.setStatus("current")
_Cie1000VlanConfigInterfacesHybridVlans0KTo1K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesHybridVlans0KTo1K_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridVlans0KTo1K = _Cie1000VlanConfigInterfacesHybridVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 15),
    _Cie1000VlanConfigInterfacesHybridVlans0KTo1K_Type()
)
cie1000VlanConfigInterfacesHybridVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridVlans0KTo1K.setStatus("current")
_Cie1000VlanConfigInterfacesHybridVlans1KTo2K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesHybridVlans1KTo2K_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridVlans1KTo2K = _Cie1000VlanConfigInterfacesHybridVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 16),
    _Cie1000VlanConfigInterfacesHybridVlans1KTo2K_Type()
)
cie1000VlanConfigInterfacesHybridVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridVlans1KTo2K.setStatus("current")
_Cie1000VlanConfigInterfacesHybridVlans2KTo3K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesHybridVlans2KTo3K_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridVlans2KTo3K = _Cie1000VlanConfigInterfacesHybridVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 17),
    _Cie1000VlanConfigInterfacesHybridVlans2KTo3K_Type()
)
cie1000VlanConfigInterfacesHybridVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridVlans2KTo3K.setStatus("current")
_Cie1000VlanConfigInterfacesHybridVlans3KTo4K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesHybridVlans3KTo4K_Object = MibTableColumn
cie1000VlanConfigInterfacesHybridVlans3KTo4K = _Cie1000VlanConfigInterfacesHybridVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 18),
    _Cie1000VlanConfigInterfacesHybridVlans3KTo4K_Type()
)
cie1000VlanConfigInterfacesHybridVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesHybridVlans3KTo4K.setStatus("current")
_Cie1000VlanConfigInterfacesForbiddenVlans0KTo1K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesForbiddenVlans0KTo1K_Object = MibTableColumn
cie1000VlanConfigInterfacesForbiddenVlans0KTo1K = _Cie1000VlanConfigInterfacesForbiddenVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 19),
    _Cie1000VlanConfigInterfacesForbiddenVlans0KTo1K_Type()
)
cie1000VlanConfigInterfacesForbiddenVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesForbiddenVlans0KTo1K.setStatus("current")
_Cie1000VlanConfigInterfacesForbiddenVlans1KTo2K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesForbiddenVlans1KTo2K_Object = MibTableColumn
cie1000VlanConfigInterfacesForbiddenVlans1KTo2K = _Cie1000VlanConfigInterfacesForbiddenVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 20),
    _Cie1000VlanConfigInterfacesForbiddenVlans1KTo2K_Type()
)
cie1000VlanConfigInterfacesForbiddenVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesForbiddenVlans1KTo2K.setStatus("current")
_Cie1000VlanConfigInterfacesForbiddenVlans2KTo3K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesForbiddenVlans2KTo3K_Object = MibTableColumn
cie1000VlanConfigInterfacesForbiddenVlans2KTo3K = _Cie1000VlanConfigInterfacesForbiddenVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 21),
    _Cie1000VlanConfigInterfacesForbiddenVlans2KTo3K_Type()
)
cie1000VlanConfigInterfacesForbiddenVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesForbiddenVlans2KTo3K.setStatus("current")
_Cie1000VlanConfigInterfacesForbiddenVlans3KTo4K_Type = CIE1000VlanListQuarter
_Cie1000VlanConfigInterfacesForbiddenVlans3KTo4K_Object = MibTableColumn
cie1000VlanConfigInterfacesForbiddenVlans3KTo4K = _Cie1000VlanConfigInterfacesForbiddenVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 1, 1, 22),
    _Cie1000VlanConfigInterfacesForbiddenVlans3KTo4K_Type()
)
cie1000VlanConfigInterfacesForbiddenVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesForbiddenVlans3KTo4K.setStatus("current")
_Cie1000VlanConfigInterfacesSvlTable_Object = MibTable
cie1000VlanConfigInterfacesSvlTable = _Cie1000VlanConfigInterfacesSvlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlTable.setStatus("current")
_Cie1000VlanConfigInterfacesSvlEntry_Object = MibTableRow
cie1000VlanConfigInterfacesSvlEntry = _Cie1000VlanConfigInterfacesSvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 2, 1)
)
cie1000VlanConfigInterfacesSvlEntry.setIndexNames(
    (0, "CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlVlanId"),
)
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlEntry.setStatus("current")
_Cie1000VlanConfigInterfacesSvlVlanId_Type = CIE1000Vlan
_Cie1000VlanConfigInterfacesSvlVlanId_Object = MibTableColumn
cie1000VlanConfigInterfacesSvlVlanId = _Cie1000VlanConfigInterfacesSvlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 2, 1, 1),
    _Cie1000VlanConfigInterfacesSvlVlanId_Type()
)
cie1000VlanConfigInterfacesSvlVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlVlanId.setStatus("current")
_Cie1000VlanConfigInterfacesSvlFilterId_Type = CIE1000Unsigned16
_Cie1000VlanConfigInterfacesSvlFilterId_Object = MibTableColumn
cie1000VlanConfigInterfacesSvlFilterId = _Cie1000VlanConfigInterfacesSvlFilterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 2, 1, 2),
    _Cie1000VlanConfigInterfacesSvlFilterId_Type()
)
cie1000VlanConfigInterfacesSvlFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlFilterId.setStatus("current")
_Cie1000VlanConfigInterfacesSvlAction_Type = CIE1000RowEditorState
_Cie1000VlanConfigInterfacesSvlAction_Object = MibTableColumn
cie1000VlanConfigInterfacesSvlAction = _Cie1000VlanConfigInterfacesSvlAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 2, 1, 100),
    _Cie1000VlanConfigInterfacesSvlAction_Type()
)
cie1000VlanConfigInterfacesSvlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlAction.setStatus("current")
_Cie1000VlanConfigInterfacesSvlTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000VlanConfigInterfacesSvlTableRowEditor = _Cie1000VlanConfigInterfacesSvlTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 3)
)
_Cie1000VlanConfigInterfacesSvlTableRowEditorVlanId_Type = CIE1000Vlan
_Cie1000VlanConfigInterfacesSvlTableRowEditorVlanId_Object = MibScalar
cie1000VlanConfigInterfacesSvlTableRowEditorVlanId = _Cie1000VlanConfigInterfacesSvlTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 3, 1),
    _Cie1000VlanConfigInterfacesSvlTableRowEditorVlanId_Type()
)
cie1000VlanConfigInterfacesSvlTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlTableRowEditorVlanId.setStatus("current")
_Cie1000VlanConfigInterfacesSvlTableRowEditorFilterId_Type = CIE1000Unsigned16
_Cie1000VlanConfigInterfacesSvlTableRowEditorFilterId_Object = MibScalar
cie1000VlanConfigInterfacesSvlTableRowEditorFilterId = _Cie1000VlanConfigInterfacesSvlTableRowEditorFilterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 3, 2),
    _Cie1000VlanConfigInterfacesSvlTableRowEditorFilterId_Type()
)
cie1000VlanConfigInterfacesSvlTableRowEditorFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlTableRowEditorFilterId.setStatus("current")
_Cie1000VlanConfigInterfacesSvlTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000VlanConfigInterfacesSvlTableRowEditorAction_Object = MibScalar
cie1000VlanConfigInterfacesSvlTableRowEditorAction = _Cie1000VlanConfigInterfacesSvlTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 2, 2, 3, 100),
    _Cie1000VlanConfigInterfacesSvlTableRowEditorAction_Type()
)
cie1000VlanConfigInterfacesSvlTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlTableRowEditorAction.setStatus("current")
_Cie1000VlanStatus_ObjectIdentity = ObjectIdentity
cie1000VlanStatus = _Cie1000VlanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3)
)
_Cie1000VlanStatusInterfaces_ObjectIdentity = ObjectIdentity
cie1000VlanStatusInterfaces = _Cie1000VlanStatusInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1)
)
_Cie1000VlanStatusInterfacesTable_Object = MibTable
cie1000VlanStatusInterfacesTable = _Cie1000VlanStatusInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesTable.setStatus("current")
_Cie1000VlanStatusInterfacesEntry_Object = MibTableRow
cie1000VlanStatusInterfacesEntry = _Cie1000VlanStatusInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1)
)
cie1000VlanStatusInterfacesEntry.setIndexNames(
    (0, "CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesIfIndex"),
    (0, "CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesVlanUser"),
)
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesEntry.setStatus("current")
_Cie1000VlanStatusInterfacesIfIndex_Type = CIE1000InterfaceIndex
_Cie1000VlanStatusInterfacesIfIndex_Object = MibTableColumn
cie1000VlanStatusInterfacesIfIndex = _Cie1000VlanStatusInterfacesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1, 1),
    _Cie1000VlanStatusInterfacesIfIndex_Type()
)
cie1000VlanStatusInterfacesIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesIfIndex.setStatus("current")
_Cie1000VlanStatusInterfacesVlanUser_Type = CIE1000VlanUserType
_Cie1000VlanStatusInterfacesVlanUser_Object = MibTableColumn
cie1000VlanStatusInterfacesVlanUser = _Cie1000VlanStatusInterfacesVlanUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1, 2),
    _Cie1000VlanStatusInterfacesVlanUser_Type()
)
cie1000VlanStatusInterfacesVlanUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesVlanUser.setStatus("current")
_Cie1000VlanStatusInterfacesPvid_Type = CIE1000Vlan
_Cie1000VlanStatusInterfacesPvid_Object = MibTableColumn
cie1000VlanStatusInterfacesPvid = _Cie1000VlanStatusInterfacesPvid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1, 3),
    _Cie1000VlanStatusInterfacesPvid_Type()
)
cie1000VlanStatusInterfacesPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesPvid.setStatus("current")
_Cie1000VlanStatusInterfacesUvid_Type = CIE1000Vlan
_Cie1000VlanStatusInterfacesUvid_Object = MibTableColumn
cie1000VlanStatusInterfacesUvid = _Cie1000VlanStatusInterfacesUvid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1, 4),
    _Cie1000VlanStatusInterfacesUvid_Type()
)
cie1000VlanStatusInterfacesUvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesUvid.setStatus("current")
_Cie1000VlanStatusInterfacesPortType_Type = CIE1000VlanPortType
_Cie1000VlanStatusInterfacesPortType_Object = MibTableColumn
cie1000VlanStatusInterfacesPortType = _Cie1000VlanStatusInterfacesPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1, 5),
    _Cie1000VlanStatusInterfacesPortType_Type()
)
cie1000VlanStatusInterfacesPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesPortType.setStatus("current")
_Cie1000VlanStatusInterfacesIngressFiltering_Type = TruthValue
_Cie1000VlanStatusInterfacesIngressFiltering_Object = MibTableColumn
cie1000VlanStatusInterfacesIngressFiltering = _Cie1000VlanStatusInterfacesIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1, 6),
    _Cie1000VlanStatusInterfacesIngressFiltering_Type()
)
cie1000VlanStatusInterfacesIngressFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesIngressFiltering.setStatus("current")
_Cie1000VlanStatusInterfacesIngressAcceptance_Type = CIE1000VlanIngressAcceptance
_Cie1000VlanStatusInterfacesIngressAcceptance_Object = MibTableColumn
cie1000VlanStatusInterfacesIngressAcceptance = _Cie1000VlanStatusInterfacesIngressAcceptance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1, 7),
    _Cie1000VlanStatusInterfacesIngressAcceptance_Type()
)
cie1000VlanStatusInterfacesIngressAcceptance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesIngressAcceptance.setStatus("current")
_Cie1000VlanStatusInterfacesEgressTagging_Type = CIE1000VlanEgressTagging
_Cie1000VlanStatusInterfacesEgressTagging_Object = MibTableColumn
cie1000VlanStatusInterfacesEgressTagging = _Cie1000VlanStatusInterfacesEgressTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 1, 1, 1, 8),
    _Cie1000VlanStatusInterfacesEgressTagging_Type()
)
cie1000VlanStatusInterfacesEgressTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesEgressTagging.setStatus("current")
_Cie1000VlanStatusMemberships_ObjectIdentity = ObjectIdentity
cie1000VlanStatusMemberships = _Cie1000VlanStatusMemberships_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 2)
)
_Cie1000VlanStatusMembershipsVlanTable_Object = MibTable
cie1000VlanStatusMembershipsVlanTable = _Cie1000VlanStatusMembershipsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000VlanStatusMembershipsVlanTable.setStatus("current")
_Cie1000VlanStatusMembershipsVlanEntry_Object = MibTableRow
cie1000VlanStatusMembershipsVlanEntry = _Cie1000VlanStatusMembershipsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 2, 1, 1)
)
cie1000VlanStatusMembershipsVlanEntry.setIndexNames(
    (0, "CIE1000-VLAN-MIB", "cie1000VlanStatusMembershipsVlanVlanId"),
    (0, "CIE1000-VLAN-MIB", "cie1000VlanStatusMembershipsVlanVlanUser"),
)
if mibBuilder.loadTexts:
    cie1000VlanStatusMembershipsVlanEntry.setStatus("current")
_Cie1000VlanStatusMembershipsVlanVlanId_Type = CIE1000Vlan
_Cie1000VlanStatusMembershipsVlanVlanId_Object = MibTableColumn
cie1000VlanStatusMembershipsVlanVlanId = _Cie1000VlanStatusMembershipsVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 2, 1, 1, 1),
    _Cie1000VlanStatusMembershipsVlanVlanId_Type()
)
cie1000VlanStatusMembershipsVlanVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000VlanStatusMembershipsVlanVlanId.setStatus("current")
_Cie1000VlanStatusMembershipsVlanVlanUser_Type = CIE1000VlanUserType
_Cie1000VlanStatusMembershipsVlanVlanUser_Object = MibTableColumn
cie1000VlanStatusMembershipsVlanVlanUser = _Cie1000VlanStatusMembershipsVlanVlanUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 2, 1, 1, 2),
    _Cie1000VlanStatusMembershipsVlanVlanUser_Type()
)
cie1000VlanStatusMembershipsVlanVlanUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000VlanStatusMembershipsVlanVlanUser.setStatus("current")
_Cie1000VlanStatusMembershipsVlanPortList_Type = CIE1000PortList
_Cie1000VlanStatusMembershipsVlanPortList_Object = MibTableColumn
cie1000VlanStatusMembershipsVlanPortList = _Cie1000VlanStatusMembershipsVlanPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 1, 3, 2, 1, 1, 3),
    _Cie1000VlanStatusMembershipsVlanPortList_Type()
)
cie1000VlanStatusMembershipsVlanPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000VlanStatusMembershipsVlanPortList.setStatus("current")
_Cie1000VlanMibConformance_ObjectIdentity = ObjectIdentity
cie1000VlanMibConformance = _Cie1000VlanMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2)
)
_Cie1000VlanMibCompliances_ObjectIdentity = ObjectIdentity
cie1000VlanMibCompliances = _Cie1000VlanMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 1)
)
_Cie1000VlanMibGroups_ObjectIdentity = ObjectIdentity
cie1000VlanMibGroups = _Cie1000VlanMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2)
)

# Managed Objects groups

cie1000VlanCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2, 1)
)
cie1000VlanCapabilitiesInfoGroup.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanCapabilitiesVlanIdMin"),
        ("CIE1000-VLAN-MIB", "cie1000VlanCapabilitiesVlanIdMax"),
        ("CIE1000-VLAN-MIB", "cie1000VlanCapabilitiesFidCnt"))
)
if mibBuilder.loadTexts:
    cie1000VlanCapabilitiesInfoGroup.setStatus("current")

cie1000VlanConfigGlobalsMainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2, 2)
)
cie1000VlanConfigGlobalsMainInfoGroup.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsMainCustomSPortEtherType"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsMainAccessVlans0To1K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsMainAccessVlans1KTo2K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsMainAccessVlans2KTo3K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsMainAccessVlans3KTo4K"))
)
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsMainInfoGroup.setStatus("current")

cie1000VlanConfigGlobalsNameTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2, 3)
)
cie1000VlanConfigGlobalsNameTableInfoGroup.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsNameVlanId"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsNameName"))
)
if mibBuilder.loadTexts:
    cie1000VlanConfigGlobalsNameTableInfoGroup.setStatus("current")

cie1000VlanConfigInterfacesTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2, 4)
)
cie1000VlanConfigInterfacesTableInfoGroup.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesIfIndex"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesMode"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesAccessVlan"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesTrunkNativeVlan"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesTrunkTagNativeVlan"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesTrunkVlans0KTo1K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesTrunkVlans1KTo2K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesTrunkVlans2KTo3K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesTrunkVlans3KTo4K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridNativeVlan"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridPortType"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridIngressFiltering"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridIngressAcceptance"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridEgressTagging"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridVlans0KTo1K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridVlans1KTo2K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridVlans2KTo3K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesHybridVlans3KTo4K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesForbiddenVlans0KTo1K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesForbiddenVlans1KTo2K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesForbiddenVlans2KTo3K"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesForbiddenVlans3KTo4K"))
)
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesTableInfoGroup.setStatus("current")

cie1000VlanConfigInterfacesSvlTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2, 5)
)
cie1000VlanConfigInterfacesSvlTableInfoGroup.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlVlanId"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlFilterId"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlAction"))
)
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlTableInfoGroup.setStatus("current")

cie1000VlanConfigInterfacesSvlTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2, 6)
)
cie1000VlanConfigInterfacesSvlTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlTableRowEditorVlanId"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlTableRowEditorFilterId"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000VlanConfigInterfacesSvlTableRowEditorInfoGroup.setStatus("current")

cie1000VlanStatusInterfacesTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2, 7)
)
cie1000VlanStatusInterfacesTableInfoGroup.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesIfIndex"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesVlanUser"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesPvid"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesUvid"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesPortType"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesIngressFiltering"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesIngressAcceptance"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesEgressTagging"))
)
if mibBuilder.loadTexts:
    cie1000VlanStatusInterfacesTableInfoGroup.setStatus("current")

cie1000VlanStatusMembershipsVlanTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 2, 8)
)
cie1000VlanStatusMembershipsVlanTableInfoGroup.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanStatusMembershipsVlanVlanId"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusMembershipsVlanVlanUser"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusMembershipsVlanPortList"))
)
if mibBuilder.loadTexts:
    cie1000VlanStatusMembershipsVlanTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000VlanMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 13, 2, 1, 1)
)
cie1000VlanMibCompliance.setObjects(
      *(("CIE1000-VLAN-MIB", "cie1000VlanCapabilitiesInfoGroup"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsMainInfoGroup"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigGlobalsNameTableInfoGroup"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesTableInfoGroup"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlTableInfoGroup"),
        ("CIE1000-VLAN-MIB", "cie1000VlanConfigInterfacesSvlTableRowEditorInfoGroup"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusInterfacesTableInfoGroup"),
        ("CIE1000-VLAN-MIB", "cie1000VlanStatusMembershipsVlanTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000VlanMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-VLAN-MIB",
    **{"CIE1000VlanEgressTagging": CIE1000VlanEgressTagging,
       "CIE1000VlanIngressAcceptance": CIE1000VlanIngressAcceptance,
       "CIE1000VlanPortMode": CIE1000VlanPortMode,
       "CIE1000VlanPortType": CIE1000VlanPortType,
       "CIE1000VlanUserType": CIE1000VlanUserType,
       "cie1000VlanMib": cie1000VlanMib,
       "cie1000VlanMibObjects": cie1000VlanMibObjects,
       "cie1000VlanCapabilities": cie1000VlanCapabilities,
       "cie1000VlanCapabilitiesVlanIdMin": cie1000VlanCapabilitiesVlanIdMin,
       "cie1000VlanCapabilitiesVlanIdMax": cie1000VlanCapabilitiesVlanIdMax,
       "cie1000VlanCapabilitiesFidCnt": cie1000VlanCapabilitiesFidCnt,
       "cie1000VlanConfig": cie1000VlanConfig,
       "cie1000VlanConfigGlobals": cie1000VlanConfigGlobals,
       "cie1000VlanConfigGlobalsMain": cie1000VlanConfigGlobalsMain,
       "cie1000VlanConfigGlobalsMainCustomSPortEtherType": cie1000VlanConfigGlobalsMainCustomSPortEtherType,
       "cie1000VlanConfigGlobalsMainAccessVlans0To1K": cie1000VlanConfigGlobalsMainAccessVlans0To1K,
       "cie1000VlanConfigGlobalsMainAccessVlans1KTo2K": cie1000VlanConfigGlobalsMainAccessVlans1KTo2K,
       "cie1000VlanConfigGlobalsMainAccessVlans2KTo3K": cie1000VlanConfigGlobalsMainAccessVlans2KTo3K,
       "cie1000VlanConfigGlobalsMainAccessVlans3KTo4K": cie1000VlanConfigGlobalsMainAccessVlans3KTo4K,
       "cie1000VlanConfigGlobalsNameTable": cie1000VlanConfigGlobalsNameTable,
       "cie1000VlanConfigGlobalsNameEntry": cie1000VlanConfigGlobalsNameEntry,
       "cie1000VlanConfigGlobalsNameVlanId": cie1000VlanConfigGlobalsNameVlanId,
       "cie1000VlanConfigGlobalsNameName": cie1000VlanConfigGlobalsNameName,
       "cie1000VlanConfigInterfaces": cie1000VlanConfigInterfaces,
       "cie1000VlanConfigInterfacesTable": cie1000VlanConfigInterfacesTable,
       "cie1000VlanConfigInterfacesEntry": cie1000VlanConfigInterfacesEntry,
       "cie1000VlanConfigInterfacesIfIndex": cie1000VlanConfigInterfacesIfIndex,
       "cie1000VlanConfigInterfacesMode": cie1000VlanConfigInterfacesMode,
       "cie1000VlanConfigInterfacesAccessVlan": cie1000VlanConfigInterfacesAccessVlan,
       "cie1000VlanConfigInterfacesTrunkNativeVlan": cie1000VlanConfigInterfacesTrunkNativeVlan,
       "cie1000VlanConfigInterfacesTrunkTagNativeVlan": cie1000VlanConfigInterfacesTrunkTagNativeVlan,
       "cie1000VlanConfigInterfacesTrunkVlans0KTo1K": cie1000VlanConfigInterfacesTrunkVlans0KTo1K,
       "cie1000VlanConfigInterfacesTrunkVlans1KTo2K": cie1000VlanConfigInterfacesTrunkVlans1KTo2K,
       "cie1000VlanConfigInterfacesTrunkVlans2KTo3K": cie1000VlanConfigInterfacesTrunkVlans2KTo3K,
       "cie1000VlanConfigInterfacesTrunkVlans3KTo4K": cie1000VlanConfigInterfacesTrunkVlans3KTo4K,
       "cie1000VlanConfigInterfacesHybridNativeVlan": cie1000VlanConfigInterfacesHybridNativeVlan,
       "cie1000VlanConfigInterfacesHybridPortType": cie1000VlanConfigInterfacesHybridPortType,
       "cie1000VlanConfigInterfacesHybridIngressFiltering": cie1000VlanConfigInterfacesHybridIngressFiltering,
       "cie1000VlanConfigInterfacesHybridIngressAcceptance": cie1000VlanConfigInterfacesHybridIngressAcceptance,
       "cie1000VlanConfigInterfacesHybridEgressTagging": cie1000VlanConfigInterfacesHybridEgressTagging,
       "cie1000VlanConfigInterfacesHybridVlans0KTo1K": cie1000VlanConfigInterfacesHybridVlans0KTo1K,
       "cie1000VlanConfigInterfacesHybridVlans1KTo2K": cie1000VlanConfigInterfacesHybridVlans1KTo2K,
       "cie1000VlanConfigInterfacesHybridVlans2KTo3K": cie1000VlanConfigInterfacesHybridVlans2KTo3K,
       "cie1000VlanConfigInterfacesHybridVlans3KTo4K": cie1000VlanConfigInterfacesHybridVlans3KTo4K,
       "cie1000VlanConfigInterfacesForbiddenVlans0KTo1K": cie1000VlanConfigInterfacesForbiddenVlans0KTo1K,
       "cie1000VlanConfigInterfacesForbiddenVlans1KTo2K": cie1000VlanConfigInterfacesForbiddenVlans1KTo2K,
       "cie1000VlanConfigInterfacesForbiddenVlans2KTo3K": cie1000VlanConfigInterfacesForbiddenVlans2KTo3K,
       "cie1000VlanConfigInterfacesForbiddenVlans3KTo4K": cie1000VlanConfigInterfacesForbiddenVlans3KTo4K,
       "cie1000VlanConfigInterfacesSvlTable": cie1000VlanConfigInterfacesSvlTable,
       "cie1000VlanConfigInterfacesSvlEntry": cie1000VlanConfigInterfacesSvlEntry,
       "cie1000VlanConfigInterfacesSvlVlanId": cie1000VlanConfigInterfacesSvlVlanId,
       "cie1000VlanConfigInterfacesSvlFilterId": cie1000VlanConfigInterfacesSvlFilterId,
       "cie1000VlanConfigInterfacesSvlAction": cie1000VlanConfigInterfacesSvlAction,
       "cie1000VlanConfigInterfacesSvlTableRowEditor": cie1000VlanConfigInterfacesSvlTableRowEditor,
       "cie1000VlanConfigInterfacesSvlTableRowEditorVlanId": cie1000VlanConfigInterfacesSvlTableRowEditorVlanId,
       "cie1000VlanConfigInterfacesSvlTableRowEditorFilterId": cie1000VlanConfigInterfacesSvlTableRowEditorFilterId,
       "cie1000VlanConfigInterfacesSvlTableRowEditorAction": cie1000VlanConfigInterfacesSvlTableRowEditorAction,
       "cie1000VlanStatus": cie1000VlanStatus,
       "cie1000VlanStatusInterfaces": cie1000VlanStatusInterfaces,
       "cie1000VlanStatusInterfacesTable": cie1000VlanStatusInterfacesTable,
       "cie1000VlanStatusInterfacesEntry": cie1000VlanStatusInterfacesEntry,
       "cie1000VlanStatusInterfacesIfIndex": cie1000VlanStatusInterfacesIfIndex,
       "cie1000VlanStatusInterfacesVlanUser": cie1000VlanStatusInterfacesVlanUser,
       "cie1000VlanStatusInterfacesPvid": cie1000VlanStatusInterfacesPvid,
       "cie1000VlanStatusInterfacesUvid": cie1000VlanStatusInterfacesUvid,
       "cie1000VlanStatusInterfacesPortType": cie1000VlanStatusInterfacesPortType,
       "cie1000VlanStatusInterfacesIngressFiltering": cie1000VlanStatusInterfacesIngressFiltering,
       "cie1000VlanStatusInterfacesIngressAcceptance": cie1000VlanStatusInterfacesIngressAcceptance,
       "cie1000VlanStatusInterfacesEgressTagging": cie1000VlanStatusInterfacesEgressTagging,
       "cie1000VlanStatusMemberships": cie1000VlanStatusMemberships,
       "cie1000VlanStatusMembershipsVlanTable": cie1000VlanStatusMembershipsVlanTable,
       "cie1000VlanStatusMembershipsVlanEntry": cie1000VlanStatusMembershipsVlanEntry,
       "cie1000VlanStatusMembershipsVlanVlanId": cie1000VlanStatusMembershipsVlanVlanId,
       "cie1000VlanStatusMembershipsVlanVlanUser": cie1000VlanStatusMembershipsVlanVlanUser,
       "cie1000VlanStatusMembershipsVlanPortList": cie1000VlanStatusMembershipsVlanPortList,
       "cie1000VlanMibConformance": cie1000VlanMibConformance,
       "cie1000VlanMibCompliances": cie1000VlanMibCompliances,
       "cie1000VlanMibCompliance": cie1000VlanMibCompliance,
       "cie1000VlanMibGroups": cie1000VlanMibGroups,
       "cie1000VlanCapabilitiesInfoGroup": cie1000VlanCapabilitiesInfoGroup,
       "cie1000VlanConfigGlobalsMainInfoGroup": cie1000VlanConfigGlobalsMainInfoGroup,
       "cie1000VlanConfigGlobalsNameTableInfoGroup": cie1000VlanConfigGlobalsNameTableInfoGroup,
       "cie1000VlanConfigInterfacesTableInfoGroup": cie1000VlanConfigInterfacesTableInfoGroup,
       "cie1000VlanConfigInterfacesSvlTableInfoGroup": cie1000VlanConfigInterfacesSvlTableInfoGroup,
       "cie1000VlanConfigInterfacesSvlTableRowEditorInfoGroup": cie1000VlanConfigInterfacesSvlTableRowEditorInfoGroup,
       "cie1000VlanStatusInterfacesTableInfoGroup": cie1000VlanStatusInterfacesTableInfoGroup,
       "cie1000VlanStatusMembershipsVlanTableInfoGroup": cie1000VlanStatusMembershipsVlanTableInfoGroup}
)
