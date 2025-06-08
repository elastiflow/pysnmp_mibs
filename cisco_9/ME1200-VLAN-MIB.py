# SNMP MIB module (ME1200-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-VLAN-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,
 ME1200EtherType,
 ME1200InterfaceIndex,
 ME1200PortListStackable,
 ME1200RowEditorState,
 ME1200Unsigned16,
 ME1200Vlan,
 ME1200VlanListQuarter) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200EtherType",
    "ME1200InterfaceIndex",
    "ME1200PortListStackable",
    "ME1200RowEditorState",
    "ME1200Unsigned16",
    "ME1200Vlan",
    "ME1200VlanListQuarter")

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

me1200VlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13)
)
if mibBuilder.loadTexts:
    me1200VlanMIB.setRevisions(
        ("2015-01-16 00:00",
         "2014-03-11 00:00",
         "2014-02-12 00:00",
         "2014-01-29 00:00",
         "2014-01-23 00:00",
         "2014-01-22 00:00",
         "2013-12-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200VlanEgressTagging(TextualConvention, Integer32):
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



class ME1200VlanIngressAcceptance(TextualConvention, Integer32):
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



class ME1200VlanPortMode(TextualConvention, Integer32):
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



class ME1200VlanPortType(TextualConvention, Integer32):
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



class ME1200VlanUserType(TextualConvention, Integer32):
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

_Me1200VlanMIBObjects_ObjectIdentity = ObjectIdentity
me1200VlanMIBObjects = _Me1200VlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1)
)
_Me1200VlanCapabilities_ObjectIdentity = ObjectIdentity
me1200VlanCapabilities = _Me1200VlanCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 1)
)
_Me1200VlanCapabilitiesVlanIdMin_Type = ME1200Vlan
_Me1200VlanCapabilitiesVlanIdMin_Object = MibScalar
me1200VlanCapabilitiesVlanIdMin = _Me1200VlanCapabilitiesVlanIdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 1, 1),
    _Me1200VlanCapabilitiesVlanIdMin_Type()
)
me1200VlanCapabilitiesVlanIdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanCapabilitiesVlanIdMin.setStatus("current")
_Me1200VlanCapabilitiesVlanIdMax_Type = ME1200Vlan
_Me1200VlanCapabilitiesVlanIdMax_Object = MibScalar
me1200VlanCapabilitiesVlanIdMax = _Me1200VlanCapabilitiesVlanIdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 1, 2),
    _Me1200VlanCapabilitiesVlanIdMax_Type()
)
me1200VlanCapabilitiesVlanIdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanCapabilitiesVlanIdMax.setStatus("current")
_Me1200VlanCapabilitiesFidCnt_Type = ME1200Unsigned16
_Me1200VlanCapabilitiesFidCnt_Object = MibScalar
me1200VlanCapabilitiesFidCnt = _Me1200VlanCapabilitiesFidCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 1, 3),
    _Me1200VlanCapabilitiesFidCnt_Type()
)
me1200VlanCapabilitiesFidCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanCapabilitiesFidCnt.setStatus("current")
_Me1200VlanConfig_ObjectIdentity = ObjectIdentity
me1200VlanConfig = _Me1200VlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2)
)
_Me1200VlanConfigGlobals_ObjectIdentity = ObjectIdentity
me1200VlanConfigGlobals = _Me1200VlanConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1)
)
_Me1200VlanConfigGlobalsMain_ObjectIdentity = ObjectIdentity
me1200VlanConfigGlobalsMain = _Me1200VlanConfigGlobalsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 1)
)


class _Me1200VlanConfigGlobalsMainCustomSPortEtherType_Type(ME1200EtherType):
    """Custom type me1200VlanConfigGlobalsMainCustomSPortEtherType based on ME1200EtherType"""
    subtypeSpec = ME1200EtherType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_Me1200VlanConfigGlobalsMainCustomSPortEtherType_Type.__name__ = "ME1200EtherType"
_Me1200VlanConfigGlobalsMainCustomSPortEtherType_Object = MibScalar
me1200VlanConfigGlobalsMainCustomSPortEtherType = _Me1200VlanConfigGlobalsMainCustomSPortEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 1, 1),
    _Me1200VlanConfigGlobalsMainCustomSPortEtherType_Type()
)
me1200VlanConfigGlobalsMainCustomSPortEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsMainCustomSPortEtherType.setStatus("current")
_Me1200VlanConfigGlobalsMainAccessVlans0To1K_Type = ME1200VlanListQuarter
_Me1200VlanConfigGlobalsMainAccessVlans0To1K_Object = MibScalar
me1200VlanConfigGlobalsMainAccessVlans0To1K = _Me1200VlanConfigGlobalsMainAccessVlans0To1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 1, 2),
    _Me1200VlanConfigGlobalsMainAccessVlans0To1K_Type()
)
me1200VlanConfigGlobalsMainAccessVlans0To1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsMainAccessVlans0To1K.setStatus("current")
_Me1200VlanConfigGlobalsMainAccessVlans1KTo2K_Type = ME1200VlanListQuarter
_Me1200VlanConfigGlobalsMainAccessVlans1KTo2K_Object = MibScalar
me1200VlanConfigGlobalsMainAccessVlans1KTo2K = _Me1200VlanConfigGlobalsMainAccessVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 1, 3),
    _Me1200VlanConfigGlobalsMainAccessVlans1KTo2K_Type()
)
me1200VlanConfigGlobalsMainAccessVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsMainAccessVlans1KTo2K.setStatus("current")
_Me1200VlanConfigGlobalsMainAccessVlans2KTo3K_Type = ME1200VlanListQuarter
_Me1200VlanConfigGlobalsMainAccessVlans2KTo3K_Object = MibScalar
me1200VlanConfigGlobalsMainAccessVlans2KTo3K = _Me1200VlanConfigGlobalsMainAccessVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 1, 4),
    _Me1200VlanConfigGlobalsMainAccessVlans2KTo3K_Type()
)
me1200VlanConfigGlobalsMainAccessVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsMainAccessVlans2KTo3K.setStatus("current")
_Me1200VlanConfigGlobalsMainAccessVlans3KTo4K_Type = ME1200VlanListQuarter
_Me1200VlanConfigGlobalsMainAccessVlans3KTo4K_Object = MibScalar
me1200VlanConfigGlobalsMainAccessVlans3KTo4K = _Me1200VlanConfigGlobalsMainAccessVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 1, 5),
    _Me1200VlanConfigGlobalsMainAccessVlans3KTo4K_Type()
)
me1200VlanConfigGlobalsMainAccessVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsMainAccessVlans3KTo4K.setStatus("current")
_Me1200VlanConfigGlobalsNameTable_Object = MibTable
me1200VlanConfigGlobalsNameTable = _Me1200VlanConfigGlobalsNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsNameTable.setStatus("current")
_Me1200VlanConfigGlobalsNameEntry_Object = MibTableRow
me1200VlanConfigGlobalsNameEntry = _Me1200VlanConfigGlobalsNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 2, 1)
)
me1200VlanConfigGlobalsNameEntry.setIndexNames(
    (0, "ME1200-VLAN-MIB", "me1200VlanConfigGlobalsNameVlanId"),
)
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsNameEntry.setStatus("current")
_Me1200VlanConfigGlobalsNameVlanId_Type = ME1200Vlan
_Me1200VlanConfigGlobalsNameVlanId_Object = MibTableColumn
me1200VlanConfigGlobalsNameVlanId = _Me1200VlanConfigGlobalsNameVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 2, 1, 1),
    _Me1200VlanConfigGlobalsNameVlanId_Type()
)
me1200VlanConfigGlobalsNameVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsNameVlanId.setStatus("current")


class _Me1200VlanConfigGlobalsNameName_Type(ME1200DisplayString):
    """Custom type me1200VlanConfigGlobalsNameName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200VlanConfigGlobalsNameName_Type.__name__ = "ME1200DisplayString"
_Me1200VlanConfigGlobalsNameName_Object = MibTableColumn
me1200VlanConfigGlobalsNameName = _Me1200VlanConfigGlobalsNameName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 1, 2, 1, 2),
    _Me1200VlanConfigGlobalsNameName_Type()
)
me1200VlanConfigGlobalsNameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsNameName.setStatus("current")
_Me1200VlanConfigInterfaces_ObjectIdentity = ObjectIdentity
me1200VlanConfigInterfaces = _Me1200VlanConfigInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2)
)
_Me1200VlanConfigInterfaceTable_Object = MibTable
me1200VlanConfigInterfaceTable = _Me1200VlanConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceTable.setStatus("current")
_Me1200VlanConfigInterfaceEntry_Object = MibTableRow
me1200VlanConfigInterfaceEntry = _Me1200VlanConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1)
)
me1200VlanConfigInterfaceEntry.setIndexNames(
    (0, "ME1200-VLAN-MIB", "me1200VlanConfigInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceEntry.setStatus("current")
_Me1200VlanConfigInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200VlanConfigInterfaceIfIndex_Object = MibTableColumn
me1200VlanConfigInterfaceIfIndex = _Me1200VlanConfigInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 1),
    _Me1200VlanConfigInterfaceIfIndex_Type()
)
me1200VlanConfigInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceIfIndex.setStatus("current")
_Me1200VlanConfigInterfaceMode_Type = ME1200VlanPortMode
_Me1200VlanConfigInterfaceMode_Object = MibTableColumn
me1200VlanConfigInterfaceMode = _Me1200VlanConfigInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 2),
    _Me1200VlanConfigInterfaceMode_Type()
)
me1200VlanConfigInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceMode.setStatus("current")
_Me1200VlanConfigInterfaceAccessVlan_Type = ME1200Vlan
_Me1200VlanConfigInterfaceAccessVlan_Object = MibTableColumn
me1200VlanConfigInterfaceAccessVlan = _Me1200VlanConfigInterfaceAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 3),
    _Me1200VlanConfigInterfaceAccessVlan_Type()
)
me1200VlanConfigInterfaceAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceAccessVlan.setStatus("current")
_Me1200VlanConfigInterfaceTrunkNativeVlan_Type = ME1200Vlan
_Me1200VlanConfigInterfaceTrunkNativeVlan_Object = MibTableColumn
me1200VlanConfigInterfaceTrunkNativeVlan = _Me1200VlanConfigInterfaceTrunkNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 4),
    _Me1200VlanConfigInterfaceTrunkNativeVlan_Type()
)
me1200VlanConfigInterfaceTrunkNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceTrunkNativeVlan.setStatus("current")
_Me1200VlanConfigInterfaceTrunkTagNativeVlan_Type = TruthValue
_Me1200VlanConfigInterfaceTrunkTagNativeVlan_Object = MibTableColumn
me1200VlanConfigInterfaceTrunkTagNativeVlan = _Me1200VlanConfigInterfaceTrunkTagNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 5),
    _Me1200VlanConfigInterfaceTrunkTagNativeVlan_Type()
)
me1200VlanConfigInterfaceTrunkTagNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceTrunkTagNativeVlan.setStatus("current")
_Me1200VlanConfigInterfaceTrunkVlans0KTo1K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceTrunkVlans0KTo1K_Object = MibTableColumn
me1200VlanConfigInterfaceTrunkVlans0KTo1K = _Me1200VlanConfigInterfaceTrunkVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 6),
    _Me1200VlanConfigInterfaceTrunkVlans0KTo1K_Type()
)
me1200VlanConfigInterfaceTrunkVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceTrunkVlans0KTo1K.setStatus("current")
_Me1200VlanConfigInterfaceTrunkVlans1KTo2K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceTrunkVlans1KTo2K_Object = MibTableColumn
me1200VlanConfigInterfaceTrunkVlans1KTo2K = _Me1200VlanConfigInterfaceTrunkVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 7),
    _Me1200VlanConfigInterfaceTrunkVlans1KTo2K_Type()
)
me1200VlanConfigInterfaceTrunkVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceTrunkVlans1KTo2K.setStatus("current")
_Me1200VlanConfigInterfaceTrunkVlans2KTo3K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceTrunkVlans2KTo3K_Object = MibTableColumn
me1200VlanConfigInterfaceTrunkVlans2KTo3K = _Me1200VlanConfigInterfaceTrunkVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 8),
    _Me1200VlanConfigInterfaceTrunkVlans2KTo3K_Type()
)
me1200VlanConfigInterfaceTrunkVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceTrunkVlans2KTo3K.setStatus("current")
_Me1200VlanConfigInterfaceTrunkVlans3KTo4K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceTrunkVlans3KTo4K_Object = MibTableColumn
me1200VlanConfigInterfaceTrunkVlans3KTo4K = _Me1200VlanConfigInterfaceTrunkVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 9),
    _Me1200VlanConfigInterfaceTrunkVlans3KTo4K_Type()
)
me1200VlanConfigInterfaceTrunkVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceTrunkVlans3KTo4K.setStatus("current")
_Me1200VlanConfigInterfaceHybridNativeVlan_Type = ME1200Vlan
_Me1200VlanConfigInterfaceHybridNativeVlan_Object = MibTableColumn
me1200VlanConfigInterfaceHybridNativeVlan = _Me1200VlanConfigInterfaceHybridNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 10),
    _Me1200VlanConfigInterfaceHybridNativeVlan_Type()
)
me1200VlanConfigInterfaceHybridNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridNativeVlan.setStatus("current")
_Me1200VlanConfigInterfaceHybridPortType_Type = ME1200VlanPortType
_Me1200VlanConfigInterfaceHybridPortType_Object = MibTableColumn
me1200VlanConfigInterfaceHybridPortType = _Me1200VlanConfigInterfaceHybridPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 11),
    _Me1200VlanConfigInterfaceHybridPortType_Type()
)
me1200VlanConfigInterfaceHybridPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridPortType.setStatus("current")
_Me1200VlanConfigInterfaceHybridIngressFiltering_Type = TruthValue
_Me1200VlanConfigInterfaceHybridIngressFiltering_Object = MibTableColumn
me1200VlanConfigInterfaceHybridIngressFiltering = _Me1200VlanConfigInterfaceHybridIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 12),
    _Me1200VlanConfigInterfaceHybridIngressFiltering_Type()
)
me1200VlanConfigInterfaceHybridIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridIngressFiltering.setStatus("current")
_Me1200VlanConfigInterfaceHybridIngressAcceptance_Type = ME1200VlanIngressAcceptance
_Me1200VlanConfigInterfaceHybridIngressAcceptance_Object = MibTableColumn
me1200VlanConfigInterfaceHybridIngressAcceptance = _Me1200VlanConfigInterfaceHybridIngressAcceptance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 13),
    _Me1200VlanConfigInterfaceHybridIngressAcceptance_Type()
)
me1200VlanConfigInterfaceHybridIngressAcceptance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridIngressAcceptance.setStatus("current")
_Me1200VlanConfigInterfaceHybridEgressTagging_Type = ME1200VlanEgressTagging
_Me1200VlanConfigInterfaceHybridEgressTagging_Object = MibTableColumn
me1200VlanConfigInterfaceHybridEgressTagging = _Me1200VlanConfigInterfaceHybridEgressTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 14),
    _Me1200VlanConfigInterfaceHybridEgressTagging_Type()
)
me1200VlanConfigInterfaceHybridEgressTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridEgressTagging.setStatus("current")
_Me1200VlanConfigInterfaceHybridVlans0KTo1K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceHybridVlans0KTo1K_Object = MibTableColumn
me1200VlanConfigInterfaceHybridVlans0KTo1K = _Me1200VlanConfigInterfaceHybridVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 15),
    _Me1200VlanConfigInterfaceHybridVlans0KTo1K_Type()
)
me1200VlanConfigInterfaceHybridVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridVlans0KTo1K.setStatus("current")
_Me1200VlanConfigInterfaceHybridVlans1KTo2K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceHybridVlans1KTo2K_Object = MibTableColumn
me1200VlanConfigInterfaceHybridVlans1KTo2K = _Me1200VlanConfigInterfaceHybridVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 16),
    _Me1200VlanConfigInterfaceHybridVlans1KTo2K_Type()
)
me1200VlanConfigInterfaceHybridVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridVlans1KTo2K.setStatus("current")
_Me1200VlanConfigInterfaceHybridVlans2KTo3K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceHybridVlans2KTo3K_Object = MibTableColumn
me1200VlanConfigInterfaceHybridVlans2KTo3K = _Me1200VlanConfigInterfaceHybridVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 17),
    _Me1200VlanConfigInterfaceHybridVlans2KTo3K_Type()
)
me1200VlanConfigInterfaceHybridVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridVlans2KTo3K.setStatus("current")
_Me1200VlanConfigInterfaceHybridVlans3KTo4K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceHybridVlans3KTo4K_Object = MibTableColumn
me1200VlanConfigInterfaceHybridVlans3KTo4K = _Me1200VlanConfigInterfaceHybridVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 18),
    _Me1200VlanConfigInterfaceHybridVlans3KTo4K_Type()
)
me1200VlanConfigInterfaceHybridVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceHybridVlans3KTo4K.setStatus("current")
_Me1200VlanConfigInterfaceForbiddenVlans0KTo1K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceForbiddenVlans0KTo1K_Object = MibTableColumn
me1200VlanConfigInterfaceForbiddenVlans0KTo1K = _Me1200VlanConfigInterfaceForbiddenVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 19),
    _Me1200VlanConfigInterfaceForbiddenVlans0KTo1K_Type()
)
me1200VlanConfigInterfaceForbiddenVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceForbiddenVlans0KTo1K.setStatus("current")
_Me1200VlanConfigInterfaceForbiddenVlans1KTo2K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceForbiddenVlans1KTo2K_Object = MibTableColumn
me1200VlanConfigInterfaceForbiddenVlans1KTo2K = _Me1200VlanConfigInterfaceForbiddenVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 20),
    _Me1200VlanConfigInterfaceForbiddenVlans1KTo2K_Type()
)
me1200VlanConfigInterfaceForbiddenVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceForbiddenVlans1KTo2K.setStatus("current")
_Me1200VlanConfigInterfaceForbiddenVlans2KTo3K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceForbiddenVlans2KTo3K_Object = MibTableColumn
me1200VlanConfigInterfaceForbiddenVlans2KTo3K = _Me1200VlanConfigInterfaceForbiddenVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 21),
    _Me1200VlanConfigInterfaceForbiddenVlans2KTo3K_Type()
)
me1200VlanConfigInterfaceForbiddenVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceForbiddenVlans2KTo3K.setStatus("current")
_Me1200VlanConfigInterfaceForbiddenVlans3KTo4K_Type = ME1200VlanListQuarter
_Me1200VlanConfigInterfaceForbiddenVlans3KTo4K_Object = MibTableColumn
me1200VlanConfigInterfaceForbiddenVlans3KTo4K = _Me1200VlanConfigInterfaceForbiddenVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 1, 1, 22),
    _Me1200VlanConfigInterfaceForbiddenVlans3KTo4K_Type()
)
me1200VlanConfigInterfaceForbiddenVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceForbiddenVlans3KTo4K.setStatus("current")
_Me1200VlanConfigInterfacesSvlTable_Object = MibTable
me1200VlanConfigInterfacesSvlTable = _Me1200VlanConfigInterfacesSvlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlTable.setStatus("current")
_Me1200VlanConfigInterfacesSvlEntry_Object = MibTableRow
me1200VlanConfigInterfacesSvlEntry = _Me1200VlanConfigInterfacesSvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 2, 1)
)
me1200VlanConfigInterfacesSvlEntry.setIndexNames(
    (0, "ME1200-VLAN-MIB", "me1200VlanConfigInterfacesSvlVlanId"),
)
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlEntry.setStatus("current")
_Me1200VlanConfigInterfacesSvlVlanId_Type = ME1200Vlan
_Me1200VlanConfigInterfacesSvlVlanId_Object = MibTableColumn
me1200VlanConfigInterfacesSvlVlanId = _Me1200VlanConfigInterfacesSvlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 2, 1, 1),
    _Me1200VlanConfigInterfacesSvlVlanId_Type()
)
me1200VlanConfigInterfacesSvlVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlVlanId.setStatus("current")
_Me1200VlanConfigInterfacesSvlFilterId_Type = ME1200Unsigned16
_Me1200VlanConfigInterfacesSvlFilterId_Object = MibTableColumn
me1200VlanConfigInterfacesSvlFilterId = _Me1200VlanConfigInterfacesSvlFilterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 2, 1, 2),
    _Me1200VlanConfigInterfacesSvlFilterId_Type()
)
me1200VlanConfigInterfacesSvlFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlFilterId.setStatus("current")
_Me1200VlanConfigInterfacesSvlAction_Type = ME1200RowEditorState
_Me1200VlanConfigInterfacesSvlAction_Object = MibTableColumn
me1200VlanConfigInterfacesSvlAction = _Me1200VlanConfigInterfacesSvlAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 2, 1, 100),
    _Me1200VlanConfigInterfacesSvlAction_Type()
)
me1200VlanConfigInterfacesSvlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlAction.setStatus("current")
_Me1200VlanConfigInterfacesSvlTableRowEditor_ObjectIdentity = ObjectIdentity
me1200VlanConfigInterfacesSvlTableRowEditor = _Me1200VlanConfigInterfacesSvlTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 3)
)
_Me1200VlanConfigInterfacesSvlTableRowEditorVlanId_Type = ME1200Vlan
_Me1200VlanConfigInterfacesSvlTableRowEditorVlanId_Object = MibScalar
me1200VlanConfigInterfacesSvlTableRowEditorVlanId = _Me1200VlanConfigInterfacesSvlTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 3, 1),
    _Me1200VlanConfigInterfacesSvlTableRowEditorVlanId_Type()
)
me1200VlanConfigInterfacesSvlTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlTableRowEditorVlanId.setStatus("current")
_Me1200VlanConfigInterfacesSvlTableRowEditorFilterId_Type = ME1200Unsigned16
_Me1200VlanConfigInterfacesSvlTableRowEditorFilterId_Object = MibScalar
me1200VlanConfigInterfacesSvlTableRowEditorFilterId = _Me1200VlanConfigInterfacesSvlTableRowEditorFilterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 3, 2),
    _Me1200VlanConfigInterfacesSvlTableRowEditorFilterId_Type()
)
me1200VlanConfigInterfacesSvlTableRowEditorFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlTableRowEditorFilterId.setStatus("current")
_Me1200VlanConfigInterfacesSvlTableRowEditorAction_Type = ME1200RowEditorState
_Me1200VlanConfigInterfacesSvlTableRowEditorAction_Object = MibScalar
me1200VlanConfigInterfacesSvlTableRowEditorAction = _Me1200VlanConfigInterfacesSvlTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 2, 2, 3, 100),
    _Me1200VlanConfigInterfacesSvlTableRowEditorAction_Type()
)
me1200VlanConfigInterfacesSvlTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlTableRowEditorAction.setStatus("current")
_Me1200VlanStatus_ObjectIdentity = ObjectIdentity
me1200VlanStatus = _Me1200VlanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3)
)
_Me1200VlanStatusInterfaces_ObjectIdentity = ObjectIdentity
me1200VlanStatusInterfaces = _Me1200VlanStatusInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1)
)
_Me1200VlanStatusInterfaceTable_Object = MibTable
me1200VlanStatusInterfaceTable = _Me1200VlanStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceTable.setStatus("current")
_Me1200VlanStatusInterfaceEntry_Object = MibTableRow
me1200VlanStatusInterfaceEntry = _Me1200VlanStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1)
)
me1200VlanStatusInterfaceEntry.setIndexNames(
    (0, "ME1200-VLAN-MIB", "me1200VlanStatusInterfaceIfIndex"),
    (0, "ME1200-VLAN-MIB", "me1200VlanStatusInterfaceVlanUser"),
)
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceEntry.setStatus("current")
_Me1200VlanStatusInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200VlanStatusInterfaceIfIndex_Object = MibTableColumn
me1200VlanStatusInterfaceIfIndex = _Me1200VlanStatusInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1, 1),
    _Me1200VlanStatusInterfaceIfIndex_Type()
)
me1200VlanStatusInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceIfIndex.setStatus("current")
_Me1200VlanStatusInterfaceVlanUser_Type = ME1200VlanUserType
_Me1200VlanStatusInterfaceVlanUser_Object = MibTableColumn
me1200VlanStatusInterfaceVlanUser = _Me1200VlanStatusInterfaceVlanUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1, 2),
    _Me1200VlanStatusInterfaceVlanUser_Type()
)
me1200VlanStatusInterfaceVlanUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceVlanUser.setStatus("current")
_Me1200VlanStatusInterfacePvid_Type = ME1200Vlan
_Me1200VlanStatusInterfacePvid_Object = MibTableColumn
me1200VlanStatusInterfacePvid = _Me1200VlanStatusInterfacePvid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1, 3),
    _Me1200VlanStatusInterfacePvid_Type()
)
me1200VlanStatusInterfacePvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanStatusInterfacePvid.setStatus("current")
_Me1200VlanStatusInterfaceUvid_Type = ME1200Vlan
_Me1200VlanStatusInterfaceUvid_Object = MibTableColumn
me1200VlanStatusInterfaceUvid = _Me1200VlanStatusInterfaceUvid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1, 4),
    _Me1200VlanStatusInterfaceUvid_Type()
)
me1200VlanStatusInterfaceUvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceUvid.setStatus("current")
_Me1200VlanStatusInterfacePortType_Type = ME1200VlanPortType
_Me1200VlanStatusInterfacePortType_Object = MibTableColumn
me1200VlanStatusInterfacePortType = _Me1200VlanStatusInterfacePortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1, 5),
    _Me1200VlanStatusInterfacePortType_Type()
)
me1200VlanStatusInterfacePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanStatusInterfacePortType.setStatus("current")
_Me1200VlanStatusInterfaceIngressFiltering_Type = TruthValue
_Me1200VlanStatusInterfaceIngressFiltering_Object = MibTableColumn
me1200VlanStatusInterfaceIngressFiltering = _Me1200VlanStatusInterfaceIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1, 6),
    _Me1200VlanStatusInterfaceIngressFiltering_Type()
)
me1200VlanStatusInterfaceIngressFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceIngressFiltering.setStatus("current")
_Me1200VlanStatusInterfaceIngressAcceptance_Type = ME1200VlanIngressAcceptance
_Me1200VlanStatusInterfaceIngressAcceptance_Object = MibTableColumn
me1200VlanStatusInterfaceIngressAcceptance = _Me1200VlanStatusInterfaceIngressAcceptance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1, 7),
    _Me1200VlanStatusInterfaceIngressAcceptance_Type()
)
me1200VlanStatusInterfaceIngressAcceptance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceIngressAcceptance.setStatus("current")
_Me1200VlanStatusInterfaceEgressTagging_Type = ME1200VlanEgressTagging
_Me1200VlanStatusInterfaceEgressTagging_Object = MibTableColumn
me1200VlanStatusInterfaceEgressTagging = _Me1200VlanStatusInterfaceEgressTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 1, 1, 1, 8),
    _Me1200VlanStatusInterfaceEgressTagging_Type()
)
me1200VlanStatusInterfaceEgressTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceEgressTagging.setStatus("current")
_Me1200VlanStatusMemberships_ObjectIdentity = ObjectIdentity
me1200VlanStatusMemberships = _Me1200VlanStatusMemberships_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 2)
)
_Me1200VlanStatusMembershipVlanTable_Object = MibTable
me1200VlanStatusMembershipVlanTable = _Me1200VlanStatusMembershipVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    me1200VlanStatusMembershipVlanTable.setStatus("current")
_Me1200VlanStatusMembershipVlanEntry_Object = MibTableRow
me1200VlanStatusMembershipVlanEntry = _Me1200VlanStatusMembershipVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 2, 1, 1)
)
me1200VlanStatusMembershipVlanEntry.setIndexNames(
    (0, "ME1200-VLAN-MIB", "me1200VlanStatusMembershipVlanVlanId"),
    (0, "ME1200-VLAN-MIB", "me1200VlanStatusMembershipVlanVlanUser"),
)
if mibBuilder.loadTexts:
    me1200VlanStatusMembershipVlanEntry.setStatus("current")
_Me1200VlanStatusMembershipVlanVlanId_Type = ME1200Vlan
_Me1200VlanStatusMembershipVlanVlanId_Object = MibTableColumn
me1200VlanStatusMembershipVlanVlanId = _Me1200VlanStatusMembershipVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 2, 1, 1, 1),
    _Me1200VlanStatusMembershipVlanVlanId_Type()
)
me1200VlanStatusMembershipVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200VlanStatusMembershipVlanVlanId.setStatus("current")
_Me1200VlanStatusMembershipVlanVlanUser_Type = ME1200VlanUserType
_Me1200VlanStatusMembershipVlanVlanUser_Object = MibTableColumn
me1200VlanStatusMembershipVlanVlanUser = _Me1200VlanStatusMembershipVlanVlanUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 2, 1, 1, 2),
    _Me1200VlanStatusMembershipVlanVlanUser_Type()
)
me1200VlanStatusMembershipVlanVlanUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200VlanStatusMembershipVlanVlanUser.setStatus("current")
_Me1200VlanStatusMembershipVlanPortList_Type = ME1200PortListStackable
_Me1200VlanStatusMembershipVlanPortList_Object = MibTableColumn
me1200VlanStatusMembershipVlanPortList = _Me1200VlanStatusMembershipVlanPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 1, 3, 2, 1, 1, 3),
    _Me1200VlanStatusMembershipVlanPortList_Type()
)
me1200VlanStatusMembershipVlanPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200VlanStatusMembershipVlanPortList.setStatus("current")
_Me1200VlanMIBConformance_ObjectIdentity = ObjectIdentity
me1200VlanMIBConformance = _Me1200VlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3)
)
_Me1200VlanMIBCompliances_ObjectIdentity = ObjectIdentity
me1200VlanMIBCompliances = _Me1200VlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 1)
)
_Me1200VlanMIBGroups_ObjectIdentity = ObjectIdentity
me1200VlanMIBGroups = _Me1200VlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2)
)

# Managed Objects groups

me1200VlanCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2, 1)
)
me1200VlanCapabilitiesInfoGroup.setObjects(
      *(("ME1200-VLAN-MIB", "me1200VlanCapabilitiesVlanIdMin"),
        ("ME1200-VLAN-MIB", "me1200VlanCapabilitiesVlanIdMax"),
        ("ME1200-VLAN-MIB", "me1200VlanCapabilitiesFidCnt"))
)
if mibBuilder.loadTexts:
    me1200VlanCapabilitiesInfoGroup.setStatus("current")

me1200VlanConfigGlobalsMainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2, 2)
)
me1200VlanConfigGlobalsMainInfoGroup.setObjects(
      *(("ME1200-VLAN-MIB", "me1200VlanConfigGlobalsMainCustomSPortEtherType"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigGlobalsMainAccessVlans0To1K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigGlobalsMainAccessVlans1KTo2K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigGlobalsMainAccessVlans2KTo3K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigGlobalsMainAccessVlans3KTo4K"))
)
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsMainInfoGroup.setStatus("current")

me1200VlanConfigGlobalsNameTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2, 3)
)
me1200VlanConfigGlobalsNameTableInfoGroup.setObjects(
    ("ME1200-VLAN-MIB", "me1200VlanConfigGlobalsNameName")
)
if mibBuilder.loadTexts:
    me1200VlanConfigGlobalsNameTableInfoGroup.setStatus("current")

me1200VlanConfigInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2, 4)
)
me1200VlanConfigInterfaceTableInfoGroup.setObjects(
      *(("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceMode"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceAccessVlan"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceTrunkNativeVlan"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceTrunkTagNativeVlan"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceTrunkVlans0KTo1K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceTrunkVlans1KTo2K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceTrunkVlans2KTo3K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceTrunkVlans3KTo4K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridNativeVlan"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridPortType"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridIngressFiltering"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridIngressAcceptance"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridEgressTagging"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridVlans0KTo1K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridVlans1KTo2K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridVlans2KTo3K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceHybridVlans3KTo4K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceForbiddenVlans0KTo1K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceForbiddenVlans1KTo2K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceForbiddenVlans2KTo3K"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceForbiddenVlans3KTo4K"))
)
if mibBuilder.loadTexts:
    me1200VlanConfigInterfaceTableInfoGroup.setStatus("current")

me1200VlanConfigInterfacesSvlTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2, 5)
)
me1200VlanConfigInterfacesSvlTableInfoGroup.setObjects(
      *(("ME1200-VLAN-MIB", "me1200VlanConfigInterfacesSvlFilterId"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfacesSvlAction"))
)
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlTableInfoGroup.setStatus("current")

me1200VlanConfigInterfacesSvlTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2, 6)
)
me1200VlanConfigInterfacesSvlTableRowEditorInfoGroup.setObjects(
      *(("ME1200-VLAN-MIB", "me1200VlanConfigInterfacesSvlTableRowEditorVlanId"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfacesSvlTableRowEditorFilterId"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfacesSvlTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200VlanConfigInterfacesSvlTableRowEditorInfoGroup.setStatus("current")

me1200VlanStatusInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2, 7)
)
me1200VlanStatusInterfaceTableInfoGroup.setObjects(
      *(("ME1200-VLAN-MIB", "me1200VlanStatusInterfacePvid"),
        ("ME1200-VLAN-MIB", "me1200VlanStatusInterfaceUvid"),
        ("ME1200-VLAN-MIB", "me1200VlanStatusInterfacePortType"),
        ("ME1200-VLAN-MIB", "me1200VlanStatusInterfaceIngressFiltering"),
        ("ME1200-VLAN-MIB", "me1200VlanStatusInterfaceIngressAcceptance"),
        ("ME1200-VLAN-MIB", "me1200VlanStatusInterfaceEgressTagging"))
)
if mibBuilder.loadTexts:
    me1200VlanStatusInterfaceTableInfoGroup.setStatus("current")

me1200VlanStatusMembershipVlanTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 2, 8)
)
me1200VlanStatusMembershipVlanTableInfoGroup.setObjects(
    ("ME1200-VLAN-MIB", "me1200VlanStatusMembershipVlanPortList")
)
if mibBuilder.loadTexts:
    me1200VlanStatusMembershipVlanTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200VlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 13, 3, 1, 1)
)
me1200VlanMIBCompliance.setObjects(
      *(("ME1200-VLAN-MIB", "me1200VlanCapabilitiesInfoGroup"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigGlobalsMainInfoGroup"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigGlobalsNameTableInfoGroup"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfaceTableInfoGroup"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfacesSvlTableInfoGroup"),
        ("ME1200-VLAN-MIB", "me1200VlanConfigInterfacesSvlTableRowEditorInfoGroup"),
        ("ME1200-VLAN-MIB", "me1200VlanStatusInterfaceTableInfoGroup"),
        ("ME1200-VLAN-MIB", "me1200VlanStatusMembershipVlanTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200VlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-VLAN-MIB",
    **{"ME1200VlanEgressTagging": ME1200VlanEgressTagging,
       "ME1200VlanIngressAcceptance": ME1200VlanIngressAcceptance,
       "ME1200VlanPortMode": ME1200VlanPortMode,
       "ME1200VlanPortType": ME1200VlanPortType,
       "ME1200VlanUserType": ME1200VlanUserType,
       "me1200VlanMIB": me1200VlanMIB,
       "me1200VlanMIBObjects": me1200VlanMIBObjects,
       "me1200VlanCapabilities": me1200VlanCapabilities,
       "me1200VlanCapabilitiesVlanIdMin": me1200VlanCapabilitiesVlanIdMin,
       "me1200VlanCapabilitiesVlanIdMax": me1200VlanCapabilitiesVlanIdMax,
       "me1200VlanCapabilitiesFidCnt": me1200VlanCapabilitiesFidCnt,
       "me1200VlanConfig": me1200VlanConfig,
       "me1200VlanConfigGlobals": me1200VlanConfigGlobals,
       "me1200VlanConfigGlobalsMain": me1200VlanConfigGlobalsMain,
       "me1200VlanConfigGlobalsMainCustomSPortEtherType": me1200VlanConfigGlobalsMainCustomSPortEtherType,
       "me1200VlanConfigGlobalsMainAccessVlans0To1K": me1200VlanConfigGlobalsMainAccessVlans0To1K,
       "me1200VlanConfigGlobalsMainAccessVlans1KTo2K": me1200VlanConfigGlobalsMainAccessVlans1KTo2K,
       "me1200VlanConfigGlobalsMainAccessVlans2KTo3K": me1200VlanConfigGlobalsMainAccessVlans2KTo3K,
       "me1200VlanConfigGlobalsMainAccessVlans3KTo4K": me1200VlanConfigGlobalsMainAccessVlans3KTo4K,
       "me1200VlanConfigGlobalsNameTable": me1200VlanConfigGlobalsNameTable,
       "me1200VlanConfigGlobalsNameEntry": me1200VlanConfigGlobalsNameEntry,
       "me1200VlanConfigGlobalsNameVlanId": me1200VlanConfigGlobalsNameVlanId,
       "me1200VlanConfigGlobalsNameName": me1200VlanConfigGlobalsNameName,
       "me1200VlanConfigInterfaces": me1200VlanConfigInterfaces,
       "me1200VlanConfigInterfaceTable": me1200VlanConfigInterfaceTable,
       "me1200VlanConfigInterfaceEntry": me1200VlanConfigInterfaceEntry,
       "me1200VlanConfigInterfaceIfIndex": me1200VlanConfigInterfaceIfIndex,
       "me1200VlanConfigInterfaceMode": me1200VlanConfigInterfaceMode,
       "me1200VlanConfigInterfaceAccessVlan": me1200VlanConfigInterfaceAccessVlan,
       "me1200VlanConfigInterfaceTrunkNativeVlan": me1200VlanConfigInterfaceTrunkNativeVlan,
       "me1200VlanConfigInterfaceTrunkTagNativeVlan": me1200VlanConfigInterfaceTrunkTagNativeVlan,
       "me1200VlanConfigInterfaceTrunkVlans0KTo1K": me1200VlanConfigInterfaceTrunkVlans0KTo1K,
       "me1200VlanConfigInterfaceTrunkVlans1KTo2K": me1200VlanConfigInterfaceTrunkVlans1KTo2K,
       "me1200VlanConfigInterfaceTrunkVlans2KTo3K": me1200VlanConfigInterfaceTrunkVlans2KTo3K,
       "me1200VlanConfigInterfaceTrunkVlans3KTo4K": me1200VlanConfigInterfaceTrunkVlans3KTo4K,
       "me1200VlanConfigInterfaceHybridNativeVlan": me1200VlanConfigInterfaceHybridNativeVlan,
       "me1200VlanConfigInterfaceHybridPortType": me1200VlanConfigInterfaceHybridPortType,
       "me1200VlanConfigInterfaceHybridIngressFiltering": me1200VlanConfigInterfaceHybridIngressFiltering,
       "me1200VlanConfigInterfaceHybridIngressAcceptance": me1200VlanConfigInterfaceHybridIngressAcceptance,
       "me1200VlanConfigInterfaceHybridEgressTagging": me1200VlanConfigInterfaceHybridEgressTagging,
       "me1200VlanConfigInterfaceHybridVlans0KTo1K": me1200VlanConfigInterfaceHybridVlans0KTo1K,
       "me1200VlanConfigInterfaceHybridVlans1KTo2K": me1200VlanConfigInterfaceHybridVlans1KTo2K,
       "me1200VlanConfigInterfaceHybridVlans2KTo3K": me1200VlanConfigInterfaceHybridVlans2KTo3K,
       "me1200VlanConfigInterfaceHybridVlans3KTo4K": me1200VlanConfigInterfaceHybridVlans3KTo4K,
       "me1200VlanConfigInterfaceForbiddenVlans0KTo1K": me1200VlanConfigInterfaceForbiddenVlans0KTo1K,
       "me1200VlanConfigInterfaceForbiddenVlans1KTo2K": me1200VlanConfigInterfaceForbiddenVlans1KTo2K,
       "me1200VlanConfigInterfaceForbiddenVlans2KTo3K": me1200VlanConfigInterfaceForbiddenVlans2KTo3K,
       "me1200VlanConfigInterfaceForbiddenVlans3KTo4K": me1200VlanConfigInterfaceForbiddenVlans3KTo4K,
       "me1200VlanConfigInterfacesSvlTable": me1200VlanConfigInterfacesSvlTable,
       "me1200VlanConfigInterfacesSvlEntry": me1200VlanConfigInterfacesSvlEntry,
       "me1200VlanConfigInterfacesSvlVlanId": me1200VlanConfigInterfacesSvlVlanId,
       "me1200VlanConfigInterfacesSvlFilterId": me1200VlanConfigInterfacesSvlFilterId,
       "me1200VlanConfigInterfacesSvlAction": me1200VlanConfigInterfacesSvlAction,
       "me1200VlanConfigInterfacesSvlTableRowEditor": me1200VlanConfigInterfacesSvlTableRowEditor,
       "me1200VlanConfigInterfacesSvlTableRowEditorVlanId": me1200VlanConfigInterfacesSvlTableRowEditorVlanId,
       "me1200VlanConfigInterfacesSvlTableRowEditorFilterId": me1200VlanConfigInterfacesSvlTableRowEditorFilterId,
       "me1200VlanConfigInterfacesSvlTableRowEditorAction": me1200VlanConfigInterfacesSvlTableRowEditorAction,
       "me1200VlanStatus": me1200VlanStatus,
       "me1200VlanStatusInterfaces": me1200VlanStatusInterfaces,
       "me1200VlanStatusInterfaceTable": me1200VlanStatusInterfaceTable,
       "me1200VlanStatusInterfaceEntry": me1200VlanStatusInterfaceEntry,
       "me1200VlanStatusInterfaceIfIndex": me1200VlanStatusInterfaceIfIndex,
       "me1200VlanStatusInterfaceVlanUser": me1200VlanStatusInterfaceVlanUser,
       "me1200VlanStatusInterfacePvid": me1200VlanStatusInterfacePvid,
       "me1200VlanStatusInterfaceUvid": me1200VlanStatusInterfaceUvid,
       "me1200VlanStatusInterfacePortType": me1200VlanStatusInterfacePortType,
       "me1200VlanStatusInterfaceIngressFiltering": me1200VlanStatusInterfaceIngressFiltering,
       "me1200VlanStatusInterfaceIngressAcceptance": me1200VlanStatusInterfaceIngressAcceptance,
       "me1200VlanStatusInterfaceEgressTagging": me1200VlanStatusInterfaceEgressTagging,
       "me1200VlanStatusMemberships": me1200VlanStatusMemberships,
       "me1200VlanStatusMembershipVlanTable": me1200VlanStatusMembershipVlanTable,
       "me1200VlanStatusMembershipVlanEntry": me1200VlanStatusMembershipVlanEntry,
       "me1200VlanStatusMembershipVlanVlanId": me1200VlanStatusMembershipVlanVlanId,
       "me1200VlanStatusMembershipVlanVlanUser": me1200VlanStatusMembershipVlanVlanUser,
       "me1200VlanStatusMembershipVlanPortList": me1200VlanStatusMembershipVlanPortList,
       "me1200VlanMIBConformance": me1200VlanMIBConformance,
       "me1200VlanMIBCompliances": me1200VlanMIBCompliances,
       "me1200VlanMIBCompliance": me1200VlanMIBCompliance,
       "me1200VlanMIBGroups": me1200VlanMIBGroups,
       "me1200VlanCapabilitiesInfoGroup": me1200VlanCapabilitiesInfoGroup,
       "me1200VlanConfigGlobalsMainInfoGroup": me1200VlanConfigGlobalsMainInfoGroup,
       "me1200VlanConfigGlobalsNameTableInfoGroup": me1200VlanConfigGlobalsNameTableInfoGroup,
       "me1200VlanConfigInterfaceTableInfoGroup": me1200VlanConfigInterfaceTableInfoGroup,
       "me1200VlanConfigInterfacesSvlTableInfoGroup": me1200VlanConfigInterfacesSvlTableInfoGroup,
       "me1200VlanConfigInterfacesSvlTableRowEditorInfoGroup": me1200VlanConfigInterfacesSvlTableRowEditorInfoGroup,
       "me1200VlanStatusInterfaceTableInfoGroup": me1200VlanStatusInterfaceTableInfoGroup,
       "me1200VlanStatusMembershipVlanTableInfoGroup": me1200VlanStatusMembershipVlanTableInfoGroup}
)
