# SNMP MIB module (ME1200-ARP-INSPECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-ARP-INSPECTION-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(ME1200InterfaceIndex,
 ME1200RowEditorState) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState")

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

me1200ArpInspectionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63)
)
if mibBuilder.loadTexts:
    me1200ArpInspectionMib.setRevisions(
        ("2014-03-28 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2013-10-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200ArpInspectionLogType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("deny", 1),
          ("permit", 2),
          ("all", 3))
    )



class ME1200ArpInspectionRegisterStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200ArpInspectionMIBObjects_ObjectIdentity = ObjectIdentity
me1200ArpInspectionMIBObjects = _Me1200ArpInspectionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1)
)
_Me1200ArpInspectionConfig_ObjectIdentity = ObjectIdentity
me1200ArpInspectionConfig = _Me1200ArpInspectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2)
)
_Me1200ArpInspectionGlobals_ObjectIdentity = ObjectIdentity
me1200ArpInspectionGlobals = _Me1200ArpInspectionGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 1)
)
_Me1200ArpInspectionGlobalsAdminState_Type = TruthValue
_Me1200ArpInspectionGlobalsAdminState_Object = MibScalar
me1200ArpInspectionGlobalsAdminState = _Me1200ArpInspectionGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 1, 1),
    _Me1200ArpInspectionGlobalsAdminState_Type()
)
me1200ArpInspectionGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionGlobalsAdminState.setStatus("current")
_Me1200ArpInspectionPortConfigTable_Object = MibTable
me1200ArpInspectionPortConfigTable = _Me1200ArpInspectionPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200ArpInspectionPortConfigTable.setStatus("current")
_Me1200ArpInspectionPortConfigEntry_Object = MibTableRow
me1200ArpInspectionPortConfigEntry = _Me1200ArpInspectionPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 2, 1)
)
me1200ArpInspectionPortConfigEntry.setIndexNames(
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    me1200ArpInspectionPortConfigEntry.setStatus("current")
_Me1200ArpInspectionPortConfigIfIndex_Type = ME1200InterfaceIndex
_Me1200ArpInspectionPortConfigIfIndex_Object = MibTableColumn
me1200ArpInspectionPortConfigIfIndex = _Me1200ArpInspectionPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 2, 1, 1),
    _Me1200ArpInspectionPortConfigIfIndex_Type()
)
me1200ArpInspectionPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionPortConfigIfIndex.setStatus("current")
_Me1200ArpInspectionPortConfigMode_Type = TruthValue
_Me1200ArpInspectionPortConfigMode_Object = MibTableColumn
me1200ArpInspectionPortConfigMode = _Me1200ArpInspectionPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 2, 1, 2),
    _Me1200ArpInspectionPortConfigMode_Type()
)
me1200ArpInspectionPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionPortConfigMode.setStatus("current")
_Me1200ArpInspectionPortConfigCheckVlan_Type = TruthValue
_Me1200ArpInspectionPortConfigCheckVlan_Object = MibTableColumn
me1200ArpInspectionPortConfigCheckVlan = _Me1200ArpInspectionPortConfigCheckVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 2, 1, 3),
    _Me1200ArpInspectionPortConfigCheckVlan_Type()
)
me1200ArpInspectionPortConfigCheckVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionPortConfigCheckVlan.setStatus("current")
_Me1200ArpInspectionPortConfigLogType_Type = ME1200ArpInspectionLogType
_Me1200ArpInspectionPortConfigLogType_Object = MibTableColumn
me1200ArpInspectionPortConfigLogType = _Me1200ArpInspectionPortConfigLogType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 2, 1, 4),
    _Me1200ArpInspectionPortConfigLogType_Type()
)
me1200ArpInspectionPortConfigLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionPortConfigLogType.setStatus("current")
_Me1200ArpInspectionVlanConfigTable_Object = MibTable
me1200ArpInspectionVlanConfigTable = _Me1200ArpInspectionVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigTable.setStatus("current")
_Me1200ArpInspectionVlanConfigEntry_Object = MibTableRow
me1200ArpInspectionVlanConfigEntry = _Me1200ArpInspectionVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 3, 1)
)
me1200ArpInspectionVlanConfigEntry.setIndexNames(
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionVlanConfigVlanId"),
)
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigEntry.setStatus("current")


class _Me1200ArpInspectionVlanConfigVlanId_Type(Integer32):
    """Custom type me1200ArpInspectionVlanConfigVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200ArpInspectionVlanConfigVlanId_Type.__name__ = "Integer32"
_Me1200ArpInspectionVlanConfigVlanId_Object = MibTableColumn
me1200ArpInspectionVlanConfigVlanId = _Me1200ArpInspectionVlanConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 3, 1, 1),
    _Me1200ArpInspectionVlanConfigVlanId_Type()
)
me1200ArpInspectionVlanConfigVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigVlanId.setStatus("current")
_Me1200ArpInspectionVlanConfigLogType_Type = ME1200ArpInspectionLogType
_Me1200ArpInspectionVlanConfigLogType_Object = MibTableColumn
me1200ArpInspectionVlanConfigLogType = _Me1200ArpInspectionVlanConfigLogType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 3, 1, 2),
    _Me1200ArpInspectionVlanConfigLogType_Type()
)
me1200ArpInspectionVlanConfigLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigLogType.setStatus("current")
_Me1200ArpInspectionVlanConfigAction_Type = ME1200RowEditorState
_Me1200ArpInspectionVlanConfigAction_Object = MibTableColumn
me1200ArpInspectionVlanConfigAction = _Me1200ArpInspectionVlanConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 3, 1, 100),
    _Me1200ArpInspectionVlanConfigAction_Type()
)
me1200ArpInspectionVlanConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigAction.setStatus("current")
_Me1200ArpInspectionVlanConfigTableRowEditor_ObjectIdentity = ObjectIdentity
me1200ArpInspectionVlanConfigTableRowEditor = _Me1200ArpInspectionVlanConfigTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 4)
)


class _Me1200ArpInspectionVlanConfigTableRowEditorVlanId_Type(Integer32):
    """Custom type me1200ArpInspectionVlanConfigTableRowEditorVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200ArpInspectionVlanConfigTableRowEditorVlanId_Type.__name__ = "Integer32"
_Me1200ArpInspectionVlanConfigTableRowEditorVlanId_Object = MibScalar
me1200ArpInspectionVlanConfigTableRowEditorVlanId = _Me1200ArpInspectionVlanConfigTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 4, 1),
    _Me1200ArpInspectionVlanConfigTableRowEditorVlanId_Type()
)
me1200ArpInspectionVlanConfigTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigTableRowEditorVlanId.setStatus("current")
_Me1200ArpInspectionVlanConfigTableRowEditorLogType_Type = ME1200ArpInspectionLogType
_Me1200ArpInspectionVlanConfigTableRowEditorLogType_Object = MibScalar
me1200ArpInspectionVlanConfigTableRowEditorLogType = _Me1200ArpInspectionVlanConfigTableRowEditorLogType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 4, 2),
    _Me1200ArpInspectionVlanConfigTableRowEditorLogType_Type()
)
me1200ArpInspectionVlanConfigTableRowEditorLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigTableRowEditorLogType.setStatus("current")
_Me1200ArpInspectionVlanConfigTableRowEditorAction_Type = ME1200RowEditorState
_Me1200ArpInspectionVlanConfigTableRowEditorAction_Object = MibScalar
me1200ArpInspectionVlanConfigTableRowEditorAction = _Me1200ArpInspectionVlanConfigTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 4, 100),
    _Me1200ArpInspectionVlanConfigTableRowEditorAction_Type()
)
me1200ArpInspectionVlanConfigTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigTableRowEditorAction.setStatus("current")
_Me1200ArpInspectionStaticConfigTable_Object = MibTable
me1200ArpInspectionStaticConfigTable = _Me1200ArpInspectionStaticConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 5)
)
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigTable.setStatus("current")
_Me1200ArpInspectionStaticConfigEntry_Object = MibTableRow
me1200ArpInspectionStaticConfigEntry = _Me1200ArpInspectionStaticConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 5, 1)
)
me1200ArpInspectionStaticConfigEntry.setIndexNames(
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigIfIndex"),
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigVlanId"),
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigMacAddress"),
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigIpAddress"),
)
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigEntry.setStatus("current")
_Me1200ArpInspectionStaticConfigIfIndex_Type = ME1200InterfaceIndex
_Me1200ArpInspectionStaticConfigIfIndex_Object = MibTableColumn
me1200ArpInspectionStaticConfigIfIndex = _Me1200ArpInspectionStaticConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 5, 1, 1),
    _Me1200ArpInspectionStaticConfigIfIndex_Type()
)
me1200ArpInspectionStaticConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigIfIndex.setStatus("current")


class _Me1200ArpInspectionStaticConfigVlanId_Type(Integer32):
    """Custom type me1200ArpInspectionStaticConfigVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200ArpInspectionStaticConfigVlanId_Type.__name__ = "Integer32"
_Me1200ArpInspectionStaticConfigVlanId_Object = MibTableColumn
me1200ArpInspectionStaticConfigVlanId = _Me1200ArpInspectionStaticConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 5, 1, 2),
    _Me1200ArpInspectionStaticConfigVlanId_Type()
)
me1200ArpInspectionStaticConfigVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigVlanId.setStatus("current")
_Me1200ArpInspectionStaticConfigMacAddress_Type = MacAddress
_Me1200ArpInspectionStaticConfigMacAddress_Object = MibTableColumn
me1200ArpInspectionStaticConfigMacAddress = _Me1200ArpInspectionStaticConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 5, 1, 3),
    _Me1200ArpInspectionStaticConfigMacAddress_Type()
)
me1200ArpInspectionStaticConfigMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigMacAddress.setStatus("current")
_Me1200ArpInspectionStaticConfigIpAddress_Type = IpAddress
_Me1200ArpInspectionStaticConfigIpAddress_Object = MibTableColumn
me1200ArpInspectionStaticConfigIpAddress = _Me1200ArpInspectionStaticConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 5, 1, 4),
    _Me1200ArpInspectionStaticConfigIpAddress_Type()
)
me1200ArpInspectionStaticConfigIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigIpAddress.setStatus("current")
_Me1200ArpInspectionStaticConfigAction_Type = ME1200RowEditorState
_Me1200ArpInspectionStaticConfigAction_Object = MibTableColumn
me1200ArpInspectionStaticConfigAction = _Me1200ArpInspectionStaticConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 5, 1, 100),
    _Me1200ArpInspectionStaticConfigAction_Type()
)
me1200ArpInspectionStaticConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigAction.setStatus("current")
_Me1200ArpInspectionStaticConfigTableRowEditor_ObjectIdentity = ObjectIdentity
me1200ArpInspectionStaticConfigTableRowEditor = _Me1200ArpInspectionStaticConfigTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 6)
)
_Me1200ArpInspectionStaticConfigTableRowEditorIfIndex_Type = ME1200InterfaceIndex
_Me1200ArpInspectionStaticConfigTableRowEditorIfIndex_Object = MibScalar
me1200ArpInspectionStaticConfigTableRowEditorIfIndex = _Me1200ArpInspectionStaticConfigTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 6, 1),
    _Me1200ArpInspectionStaticConfigTableRowEditorIfIndex_Type()
)
me1200ArpInspectionStaticConfigTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigTableRowEditorIfIndex.setStatus("current")


class _Me1200ArpInspectionStaticConfigTableRowEditorVlanId_Type(Integer32):
    """Custom type me1200ArpInspectionStaticConfigTableRowEditorVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200ArpInspectionStaticConfigTableRowEditorVlanId_Type.__name__ = "Integer32"
_Me1200ArpInspectionStaticConfigTableRowEditorVlanId_Object = MibScalar
me1200ArpInspectionStaticConfigTableRowEditorVlanId = _Me1200ArpInspectionStaticConfigTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 6, 2),
    _Me1200ArpInspectionStaticConfigTableRowEditorVlanId_Type()
)
me1200ArpInspectionStaticConfigTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigTableRowEditorVlanId.setStatus("current")
_Me1200ArpInspectionStaticConfigTableRowEditorMacAddress_Type = MacAddress
_Me1200ArpInspectionStaticConfigTableRowEditorMacAddress_Object = MibScalar
me1200ArpInspectionStaticConfigTableRowEditorMacAddress = _Me1200ArpInspectionStaticConfigTableRowEditorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 6, 3),
    _Me1200ArpInspectionStaticConfigTableRowEditorMacAddress_Type()
)
me1200ArpInspectionStaticConfigTableRowEditorMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigTableRowEditorMacAddress.setStatus("current")
_Me1200ArpInspectionStaticConfigTableRowEditorIpAddress_Type = IpAddress
_Me1200ArpInspectionStaticConfigTableRowEditorIpAddress_Object = MibScalar
me1200ArpInspectionStaticConfigTableRowEditorIpAddress = _Me1200ArpInspectionStaticConfigTableRowEditorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 6, 4),
    _Me1200ArpInspectionStaticConfigTableRowEditorIpAddress_Type()
)
me1200ArpInspectionStaticConfigTableRowEditorIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigTableRowEditorIpAddress.setStatus("current")
_Me1200ArpInspectionStaticConfigTableRowEditorAction_Type = ME1200RowEditorState
_Me1200ArpInspectionStaticConfigTableRowEditorAction_Object = MibScalar
me1200ArpInspectionStaticConfigTableRowEditorAction = _Me1200ArpInspectionStaticConfigTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 2, 6, 100),
    _Me1200ArpInspectionStaticConfigTableRowEditorAction_Type()
)
me1200ArpInspectionStaticConfigTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigTableRowEditorAction.setStatus("current")
_Me1200ArpInspectionStatus_ObjectIdentity = ObjectIdentity
me1200ArpInspectionStatus = _Me1200ArpInspectionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 3)
)
_Me1200ArpInspectionDynamicAddressTable_Object = MibTable
me1200ArpInspectionDynamicAddressTable = _Me1200ArpInspectionDynamicAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200ArpInspectionDynamicAddressTable.setStatus("current")
_Me1200ArpInspectionDynamicAddressEntry_Object = MibTableRow
me1200ArpInspectionDynamicAddressEntry = _Me1200ArpInspectionDynamicAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 3, 1, 1)
)
me1200ArpInspectionDynamicAddressEntry.setIndexNames(
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionDynamicAddressIfIndex"),
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionDynamicAddressVlanId"),
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionDynamicAddressMacAddress"),
    (0, "ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionDynamicAddressIpAddress"),
)
if mibBuilder.loadTexts:
    me1200ArpInspectionDynamicAddressEntry.setStatus("current")
_Me1200ArpInspectionDynamicAddressIfIndex_Type = ME1200InterfaceIndex
_Me1200ArpInspectionDynamicAddressIfIndex_Object = MibTableColumn
me1200ArpInspectionDynamicAddressIfIndex = _Me1200ArpInspectionDynamicAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 3, 1, 1, 1),
    _Me1200ArpInspectionDynamicAddressIfIndex_Type()
)
me1200ArpInspectionDynamicAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionDynamicAddressIfIndex.setStatus("current")


class _Me1200ArpInspectionDynamicAddressVlanId_Type(Integer32):
    """Custom type me1200ArpInspectionDynamicAddressVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200ArpInspectionDynamicAddressVlanId_Type.__name__ = "Integer32"
_Me1200ArpInspectionDynamicAddressVlanId_Object = MibTableColumn
me1200ArpInspectionDynamicAddressVlanId = _Me1200ArpInspectionDynamicAddressVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 3, 1, 1, 2),
    _Me1200ArpInspectionDynamicAddressVlanId_Type()
)
me1200ArpInspectionDynamicAddressVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionDynamicAddressVlanId.setStatus("current")
_Me1200ArpInspectionDynamicAddressMacAddress_Type = MacAddress
_Me1200ArpInspectionDynamicAddressMacAddress_Object = MibTableColumn
me1200ArpInspectionDynamicAddressMacAddress = _Me1200ArpInspectionDynamicAddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 3, 1, 1, 3),
    _Me1200ArpInspectionDynamicAddressMacAddress_Type()
)
me1200ArpInspectionDynamicAddressMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionDynamicAddressMacAddress.setStatus("current")
_Me1200ArpInspectionDynamicAddressIpAddress_Type = IpAddress
_Me1200ArpInspectionDynamicAddressIpAddress_Object = MibTableColumn
me1200ArpInspectionDynamicAddressIpAddress = _Me1200ArpInspectionDynamicAddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 3, 1, 1, 4),
    _Me1200ArpInspectionDynamicAddressIpAddress_Type()
)
me1200ArpInspectionDynamicAddressIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ArpInspectionDynamicAddressIpAddress.setStatus("current")
_Me1200ArpInspectionDynamicAddressType_Type = ME1200ArpInspectionRegisterStatus
_Me1200ArpInspectionDynamicAddressType_Object = MibTableColumn
me1200ArpInspectionDynamicAddressType = _Me1200ArpInspectionDynamicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 3, 1, 1, 5),
    _Me1200ArpInspectionDynamicAddressType_Type()
)
me1200ArpInspectionDynamicAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ArpInspectionDynamicAddressType.setStatus("current")
_Me1200ArpInspectionControl_ObjectIdentity = ObjectIdentity
me1200ArpInspectionControl = _Me1200ArpInspectionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 4)
)
_Me1200ArpInspectionControlGlobals_ObjectIdentity = ObjectIdentity
me1200ArpInspectionControlGlobals = _Me1200ArpInspectionControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 4, 1)
)
_Me1200ArpInspectionControlGlobalsTranslateDynamicToStatic_Type = TruthValue
_Me1200ArpInspectionControlGlobalsTranslateDynamicToStatic_Object = MibScalar
me1200ArpInspectionControlGlobalsTranslateDynamicToStatic = _Me1200ArpInspectionControlGlobalsTranslateDynamicToStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 1, 4, 1, 1),
    _Me1200ArpInspectionControlGlobalsTranslateDynamicToStatic_Type()
)
me1200ArpInspectionControlGlobalsTranslateDynamicToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ArpInspectionControlGlobalsTranslateDynamicToStatic.setStatus("current")
_Me1200ArpInspectionMIBConformance_ObjectIdentity = ObjectIdentity
me1200ArpInspectionMIBConformance = _Me1200ArpInspectionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2)
)
_Me1200ArpInspectionMIBCompliances_ObjectIdentity = ObjectIdentity
me1200ArpInspectionMIBCompliances = _Me1200ArpInspectionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 1)
)
_Me1200ArpInspectionMIBGroups_ObjectIdentity = ObjectIdentity
me1200ArpInspectionMIBGroups = _Me1200ArpInspectionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2)
)

# Managed Objects groups

me1200ArpInspectionGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2, 1)
)
me1200ArpInspectionGlobalsInfoGroup.setObjects(
    ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionGlobalsAdminState")
)
if mibBuilder.loadTexts:
    me1200ArpInspectionGlobalsInfoGroup.setStatus("current")

me1200ArpInspectionPortConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2, 2)
)
me1200ArpInspectionPortConfigTableInfoGroup.setObjects(
      *(("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionPortConfigMode"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionPortConfigCheckVlan"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionPortConfigLogType"))
)
if mibBuilder.loadTexts:
    me1200ArpInspectionPortConfigTableInfoGroup.setStatus("current")

me1200ArpInspectionVlanConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2, 3)
)
me1200ArpInspectionVlanConfigTableInfoGroup.setObjects(
      *(("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionVlanConfigLogType"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionVlanConfigAction"))
)
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigTableInfoGroup.setStatus("current")

me1200ArpInspectionVlanConfigTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2, 4)
)
me1200ArpInspectionVlanConfigTableRowEditorInfoGroup.setObjects(
      *(("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionVlanConfigTableRowEditorVlanId"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionVlanConfigTableRowEditorLogType"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionVlanConfigTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ArpInspectionVlanConfigTableRowEditorInfoGroup.setStatus("current")

me1200ArpInspectionStaticConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2, 5)
)
me1200ArpInspectionStaticConfigTableInfoGroup.setObjects(
    ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigAction")
)
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigTableInfoGroup.setStatus("current")

me1200ArpInspectionStaticConfigTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2, 6)
)
me1200ArpInspectionStaticConfigTableRowEditorInfoGroup.setObjects(
      *(("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigTableRowEditorIfIndex"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigTableRowEditorVlanId"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigTableRowEditorMacAddress"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigTableRowEditorIpAddress"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ArpInspectionStaticConfigTableRowEditorInfoGroup.setStatus("current")

me1200ArpInspectionDynamicAddressTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2, 7)
)
me1200ArpInspectionDynamicAddressTableInfoGroup.setObjects(
    ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionDynamicAddressType")
)
if mibBuilder.loadTexts:
    me1200ArpInspectionDynamicAddressTableInfoGroup.setStatus("current")

me1200ArpInspectionControlGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 2, 8)
)
me1200ArpInspectionControlGlobalsInfoGroup.setObjects(
    ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionControlGlobalsTranslateDynamicToStatic")
)
if mibBuilder.loadTexts:
    me1200ArpInspectionControlGlobalsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200ArpInspectionMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 63, 2, 1, 1)
)
me1200ArpInspectionMibCompliance.setObjects(
      *(("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionGlobalsInfoGroup"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionPortConfigTableInfoGroup"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionVlanConfigTableInfoGroup"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionVlanConfigTableRowEditorInfoGroup"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigTableInfoGroup"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionStaticConfigTableRowEditorInfoGroup"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionDynamicAddressTableInfoGroup"),
        ("ME1200-ARP-INSPECTION-MIB", "me1200ArpInspectionControlGlobalsInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200ArpInspectionMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-ARP-INSPECTION-MIB",
    **{"ME1200ArpInspectionLogType": ME1200ArpInspectionLogType,
       "ME1200ArpInspectionRegisterStatus": ME1200ArpInspectionRegisterStatus,
       "me1200ArpInspectionMib": me1200ArpInspectionMib,
       "me1200ArpInspectionMIBObjects": me1200ArpInspectionMIBObjects,
       "me1200ArpInspectionConfig": me1200ArpInspectionConfig,
       "me1200ArpInspectionGlobals": me1200ArpInspectionGlobals,
       "me1200ArpInspectionGlobalsAdminState": me1200ArpInspectionGlobalsAdminState,
       "me1200ArpInspectionPortConfigTable": me1200ArpInspectionPortConfigTable,
       "me1200ArpInspectionPortConfigEntry": me1200ArpInspectionPortConfigEntry,
       "me1200ArpInspectionPortConfigIfIndex": me1200ArpInspectionPortConfigIfIndex,
       "me1200ArpInspectionPortConfigMode": me1200ArpInspectionPortConfigMode,
       "me1200ArpInspectionPortConfigCheckVlan": me1200ArpInspectionPortConfigCheckVlan,
       "me1200ArpInspectionPortConfigLogType": me1200ArpInspectionPortConfigLogType,
       "me1200ArpInspectionVlanConfigTable": me1200ArpInspectionVlanConfigTable,
       "me1200ArpInspectionVlanConfigEntry": me1200ArpInspectionVlanConfigEntry,
       "me1200ArpInspectionVlanConfigVlanId": me1200ArpInspectionVlanConfigVlanId,
       "me1200ArpInspectionVlanConfigLogType": me1200ArpInspectionVlanConfigLogType,
       "me1200ArpInspectionVlanConfigAction": me1200ArpInspectionVlanConfigAction,
       "me1200ArpInspectionVlanConfigTableRowEditor": me1200ArpInspectionVlanConfigTableRowEditor,
       "me1200ArpInspectionVlanConfigTableRowEditorVlanId": me1200ArpInspectionVlanConfigTableRowEditorVlanId,
       "me1200ArpInspectionVlanConfigTableRowEditorLogType": me1200ArpInspectionVlanConfigTableRowEditorLogType,
       "me1200ArpInspectionVlanConfigTableRowEditorAction": me1200ArpInspectionVlanConfigTableRowEditorAction,
       "me1200ArpInspectionStaticConfigTable": me1200ArpInspectionStaticConfigTable,
       "me1200ArpInspectionStaticConfigEntry": me1200ArpInspectionStaticConfigEntry,
       "me1200ArpInspectionStaticConfigIfIndex": me1200ArpInspectionStaticConfigIfIndex,
       "me1200ArpInspectionStaticConfigVlanId": me1200ArpInspectionStaticConfigVlanId,
       "me1200ArpInspectionStaticConfigMacAddress": me1200ArpInspectionStaticConfigMacAddress,
       "me1200ArpInspectionStaticConfigIpAddress": me1200ArpInspectionStaticConfigIpAddress,
       "me1200ArpInspectionStaticConfigAction": me1200ArpInspectionStaticConfigAction,
       "me1200ArpInspectionStaticConfigTableRowEditor": me1200ArpInspectionStaticConfigTableRowEditor,
       "me1200ArpInspectionStaticConfigTableRowEditorIfIndex": me1200ArpInspectionStaticConfigTableRowEditorIfIndex,
       "me1200ArpInspectionStaticConfigTableRowEditorVlanId": me1200ArpInspectionStaticConfigTableRowEditorVlanId,
       "me1200ArpInspectionStaticConfigTableRowEditorMacAddress": me1200ArpInspectionStaticConfigTableRowEditorMacAddress,
       "me1200ArpInspectionStaticConfigTableRowEditorIpAddress": me1200ArpInspectionStaticConfigTableRowEditorIpAddress,
       "me1200ArpInspectionStaticConfigTableRowEditorAction": me1200ArpInspectionStaticConfigTableRowEditorAction,
       "me1200ArpInspectionStatus": me1200ArpInspectionStatus,
       "me1200ArpInspectionDynamicAddressTable": me1200ArpInspectionDynamicAddressTable,
       "me1200ArpInspectionDynamicAddressEntry": me1200ArpInspectionDynamicAddressEntry,
       "me1200ArpInspectionDynamicAddressIfIndex": me1200ArpInspectionDynamicAddressIfIndex,
       "me1200ArpInspectionDynamicAddressVlanId": me1200ArpInspectionDynamicAddressVlanId,
       "me1200ArpInspectionDynamicAddressMacAddress": me1200ArpInspectionDynamicAddressMacAddress,
       "me1200ArpInspectionDynamicAddressIpAddress": me1200ArpInspectionDynamicAddressIpAddress,
       "me1200ArpInspectionDynamicAddressType": me1200ArpInspectionDynamicAddressType,
       "me1200ArpInspectionControl": me1200ArpInspectionControl,
       "me1200ArpInspectionControlGlobals": me1200ArpInspectionControlGlobals,
       "me1200ArpInspectionControlGlobalsTranslateDynamicToStatic": me1200ArpInspectionControlGlobalsTranslateDynamicToStatic,
       "me1200ArpInspectionMIBConformance": me1200ArpInspectionMIBConformance,
       "me1200ArpInspectionMIBCompliances": me1200ArpInspectionMIBCompliances,
       "me1200ArpInspectionMibCompliance": me1200ArpInspectionMibCompliance,
       "me1200ArpInspectionMIBGroups": me1200ArpInspectionMIBGroups,
       "me1200ArpInspectionGlobalsInfoGroup": me1200ArpInspectionGlobalsInfoGroup,
       "me1200ArpInspectionPortConfigTableInfoGroup": me1200ArpInspectionPortConfigTableInfoGroup,
       "me1200ArpInspectionVlanConfigTableInfoGroup": me1200ArpInspectionVlanConfigTableInfoGroup,
       "me1200ArpInspectionVlanConfigTableRowEditorInfoGroup": me1200ArpInspectionVlanConfigTableRowEditorInfoGroup,
       "me1200ArpInspectionStaticConfigTableInfoGroup": me1200ArpInspectionStaticConfigTableInfoGroup,
       "me1200ArpInspectionStaticConfigTableRowEditorInfoGroup": me1200ArpInspectionStaticConfigTableRowEditorInfoGroup,
       "me1200ArpInspectionDynamicAddressTableInfoGroup": me1200ArpInspectionDynamicAddressTableInfoGroup,
       "me1200ArpInspectionControlGlobalsInfoGroup": me1200ArpInspectionControlGlobalsInfoGroup}
)
