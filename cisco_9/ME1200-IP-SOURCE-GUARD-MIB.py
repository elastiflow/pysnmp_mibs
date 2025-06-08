# SNMP MIB module (ME1200-IP-SOURCE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-IP-SOURCE-GUARD-MIB.mib
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

me1200IpSourceGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64)
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardMIB.setRevisions(
        ("2014-03-28 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2013-10-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200IpSourceGuardMIBObjects_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardMIBObjects = _Me1200IpSourceGuardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1)
)
_Me1200IpSourceGuardConfig_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardConfig = _Me1200IpSourceGuardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2)
)
_Me1200IpSourceGuardGlobals_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardGlobals = _Me1200IpSourceGuardGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 1)
)
_Me1200IpSourceGuardGlobalsMode_Type = TruthValue
_Me1200IpSourceGuardGlobalsMode_Object = MibScalar
me1200IpSourceGuardGlobalsMode = _Me1200IpSourceGuardGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 1, 1),
    _Me1200IpSourceGuardGlobalsMode_Type()
)
me1200IpSourceGuardGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardGlobalsMode.setStatus("current")
_Me1200IpSourceGuardInterfaceTable_Object = MibTable
me1200IpSourceGuardInterfaceTable = _Me1200IpSourceGuardInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardInterfaceTable.setStatus("current")
_Me1200IpSourceGuardInterfaceEntry_Object = MibTableRow
me1200IpSourceGuardInterfaceEntry = _Me1200IpSourceGuardInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 2, 1)
)
me1200IpSourceGuardInterfaceEntry.setIndexNames(
    (0, "ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardInterfaceEntry.setStatus("current")
_Me1200IpSourceGuardInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200IpSourceGuardInterfaceIfIndex_Object = MibTableColumn
me1200IpSourceGuardInterfaceIfIndex = _Me1200IpSourceGuardInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 2, 1, 1),
    _Me1200IpSourceGuardInterfaceIfIndex_Type()
)
me1200IpSourceGuardInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpSourceGuardInterfaceIfIndex.setStatus("current")
_Me1200IpSourceGuardInterfaceMode_Type = TruthValue
_Me1200IpSourceGuardInterfaceMode_Object = MibTableColumn
me1200IpSourceGuardInterfaceMode = _Me1200IpSourceGuardInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 2, 1, 2),
    _Me1200IpSourceGuardInterfaceMode_Type()
)
me1200IpSourceGuardInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardInterfaceMode.setStatus("current")
_Me1200IpSourceGuardInterfaceDynamicEntryCount_Type = Unsigned32
_Me1200IpSourceGuardInterfaceDynamicEntryCount_Object = MibTableColumn
me1200IpSourceGuardInterfaceDynamicEntryCount = _Me1200IpSourceGuardInterfaceDynamicEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 2, 1, 3),
    _Me1200IpSourceGuardInterfaceDynamicEntryCount_Type()
)
me1200IpSourceGuardInterfaceDynamicEntryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardInterfaceDynamicEntryCount.setStatus("current")
_Me1200IpSourceGuardStaticConfigTable_Object = MibTable
me1200IpSourceGuardStaticConfigTable = _Me1200IpSourceGuardStaticConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigTable.setStatus("current")
_Me1200IpSourceGuardStaticConfigEntry_Object = MibTableRow
me1200IpSourceGuardStaticConfigEntry = _Me1200IpSourceGuardStaticConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 3, 1)
)
me1200IpSourceGuardStaticConfigEntry.setIndexNames(
    (0, "ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigIfIndex"),
    (0, "ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigVlanId"),
    (0, "ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigIpAddress"),
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigEntry.setStatus("current")
_Me1200IpSourceGuardStaticConfigIfIndex_Type = ME1200InterfaceIndex
_Me1200IpSourceGuardStaticConfigIfIndex_Object = MibTableColumn
me1200IpSourceGuardStaticConfigIfIndex = _Me1200IpSourceGuardStaticConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 3, 1, 1),
    _Me1200IpSourceGuardStaticConfigIfIndex_Type()
)
me1200IpSourceGuardStaticConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigIfIndex.setStatus("current")


class _Me1200IpSourceGuardStaticConfigVlanId_Type(Integer32):
    """Custom type me1200IpSourceGuardStaticConfigVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200IpSourceGuardStaticConfigVlanId_Type.__name__ = "Integer32"
_Me1200IpSourceGuardStaticConfigVlanId_Object = MibTableColumn
me1200IpSourceGuardStaticConfigVlanId = _Me1200IpSourceGuardStaticConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 3, 1, 2),
    _Me1200IpSourceGuardStaticConfigVlanId_Type()
)
me1200IpSourceGuardStaticConfigVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigVlanId.setStatus("current")
_Me1200IpSourceGuardStaticConfigIpAddress_Type = IpAddress
_Me1200IpSourceGuardStaticConfigIpAddress_Object = MibTableColumn
me1200IpSourceGuardStaticConfigIpAddress = _Me1200IpSourceGuardStaticConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 3, 1, 3),
    _Me1200IpSourceGuardStaticConfigIpAddress_Type()
)
me1200IpSourceGuardStaticConfigIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigIpAddress.setStatus("current")
_Me1200IpSourceGuardStaticConfigMacAddress_Type = MacAddress
_Me1200IpSourceGuardStaticConfigMacAddress_Object = MibTableColumn
me1200IpSourceGuardStaticConfigMacAddress = _Me1200IpSourceGuardStaticConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 3, 1, 4),
    _Me1200IpSourceGuardStaticConfigMacAddress_Type()
)
me1200IpSourceGuardStaticConfigMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigMacAddress.setStatus("current")
_Me1200IpSourceGuardStaticConfigAction_Type = ME1200RowEditorState
_Me1200IpSourceGuardStaticConfigAction_Object = MibTableColumn
me1200IpSourceGuardStaticConfigAction = _Me1200IpSourceGuardStaticConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 3, 1, 100),
    _Me1200IpSourceGuardStaticConfigAction_Type()
)
me1200IpSourceGuardStaticConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigAction.setStatus("current")
_Me1200IpSourceGuardStaticConfigTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardStaticConfigTableRowEditor = _Me1200IpSourceGuardStaticConfigTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 4)
)
_Me1200IpSourceGuardStaticConfigTableRowEditorIfIndex_Type = ME1200InterfaceIndex
_Me1200IpSourceGuardStaticConfigTableRowEditorIfIndex_Object = MibScalar
me1200IpSourceGuardStaticConfigTableRowEditorIfIndex = _Me1200IpSourceGuardStaticConfigTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 4, 1),
    _Me1200IpSourceGuardStaticConfigTableRowEditorIfIndex_Type()
)
me1200IpSourceGuardStaticConfigTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigTableRowEditorIfIndex.setStatus("current")


class _Me1200IpSourceGuardStaticConfigTableRowEditorVlanId_Type(Integer32):
    """Custom type me1200IpSourceGuardStaticConfigTableRowEditorVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200IpSourceGuardStaticConfigTableRowEditorVlanId_Type.__name__ = "Integer32"
_Me1200IpSourceGuardStaticConfigTableRowEditorVlanId_Object = MibScalar
me1200IpSourceGuardStaticConfigTableRowEditorVlanId = _Me1200IpSourceGuardStaticConfigTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 4, 2),
    _Me1200IpSourceGuardStaticConfigTableRowEditorVlanId_Type()
)
me1200IpSourceGuardStaticConfigTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigTableRowEditorVlanId.setStatus("current")
_Me1200IpSourceGuardStaticConfigTableRowEditorIpAddress_Type = IpAddress
_Me1200IpSourceGuardStaticConfigTableRowEditorIpAddress_Object = MibScalar
me1200IpSourceGuardStaticConfigTableRowEditorIpAddress = _Me1200IpSourceGuardStaticConfigTableRowEditorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 4, 3),
    _Me1200IpSourceGuardStaticConfigTableRowEditorIpAddress_Type()
)
me1200IpSourceGuardStaticConfigTableRowEditorIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigTableRowEditorIpAddress.setStatus("current")
_Me1200IpSourceGuardStaticConfigTableRowEditorMacAddress_Type = MacAddress
_Me1200IpSourceGuardStaticConfigTableRowEditorMacAddress_Object = MibScalar
me1200IpSourceGuardStaticConfigTableRowEditorMacAddress = _Me1200IpSourceGuardStaticConfigTableRowEditorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 4, 4),
    _Me1200IpSourceGuardStaticConfigTableRowEditorMacAddress_Type()
)
me1200IpSourceGuardStaticConfigTableRowEditorMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigTableRowEditorMacAddress.setStatus("current")
_Me1200IpSourceGuardStaticConfigTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpSourceGuardStaticConfigTableRowEditorAction_Object = MibScalar
me1200IpSourceGuardStaticConfigTableRowEditorAction = _Me1200IpSourceGuardStaticConfigTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 2, 4, 100),
    _Me1200IpSourceGuardStaticConfigTableRowEditorAction_Type()
)
me1200IpSourceGuardStaticConfigTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigTableRowEditorAction.setStatus("current")
_Me1200IpSourceGuardStatus_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardStatus = _Me1200IpSourceGuardStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 3)
)
_Me1200IpSourceGuardDynamicStatusTable_Object = MibTable
me1200IpSourceGuardDynamicStatusTable = _Me1200IpSourceGuardDynamicStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardDynamicStatusTable.setStatus("current")
_Me1200IpSourceGuardDynamicStatusEntry_Object = MibTableRow
me1200IpSourceGuardDynamicStatusEntry = _Me1200IpSourceGuardDynamicStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 3, 2, 1)
)
me1200IpSourceGuardDynamicStatusEntry.setIndexNames(
    (0, "ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardDynamicStatusIfIndex"),
    (0, "ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardDynamicStatusVlanId"),
    (0, "ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardDynamicStatusIpAddress"),
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardDynamicStatusEntry.setStatus("current")
_Me1200IpSourceGuardDynamicStatusIfIndex_Type = ME1200InterfaceIndex
_Me1200IpSourceGuardDynamicStatusIfIndex_Object = MibTableColumn
me1200IpSourceGuardDynamicStatusIfIndex = _Me1200IpSourceGuardDynamicStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 3, 2, 1, 1),
    _Me1200IpSourceGuardDynamicStatusIfIndex_Type()
)
me1200IpSourceGuardDynamicStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpSourceGuardDynamicStatusIfIndex.setStatus("current")


class _Me1200IpSourceGuardDynamicStatusVlanId_Type(Integer32):
    """Custom type me1200IpSourceGuardDynamicStatusVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200IpSourceGuardDynamicStatusVlanId_Type.__name__ = "Integer32"
_Me1200IpSourceGuardDynamicStatusVlanId_Object = MibTableColumn
me1200IpSourceGuardDynamicStatusVlanId = _Me1200IpSourceGuardDynamicStatusVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 3, 2, 1, 2),
    _Me1200IpSourceGuardDynamicStatusVlanId_Type()
)
me1200IpSourceGuardDynamicStatusVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpSourceGuardDynamicStatusVlanId.setStatus("current")
_Me1200IpSourceGuardDynamicStatusIpAddress_Type = IpAddress
_Me1200IpSourceGuardDynamicStatusIpAddress_Object = MibTableColumn
me1200IpSourceGuardDynamicStatusIpAddress = _Me1200IpSourceGuardDynamicStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 3, 2, 1, 3),
    _Me1200IpSourceGuardDynamicStatusIpAddress_Type()
)
me1200IpSourceGuardDynamicStatusIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpSourceGuardDynamicStatusIpAddress.setStatus("current")
_Me1200IpSourceGuardDynamicStatusMacAddress_Type = MacAddress
_Me1200IpSourceGuardDynamicStatusMacAddress_Object = MibTableColumn
me1200IpSourceGuardDynamicStatusMacAddress = _Me1200IpSourceGuardDynamicStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 3, 2, 1, 4),
    _Me1200IpSourceGuardDynamicStatusMacAddress_Type()
)
me1200IpSourceGuardDynamicStatusMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpSourceGuardDynamicStatusMacAddress.setStatus("current")
_Me1200IpSourceGuardControl_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardControl = _Me1200IpSourceGuardControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 4)
)
_Me1200IpSourceGuardControlTranslateDynamicToStatic_Type = TruthValue
_Me1200IpSourceGuardControlTranslateDynamicToStatic_Object = MibScalar
me1200IpSourceGuardControlTranslateDynamicToStatic = _Me1200IpSourceGuardControlTranslateDynamicToStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 1, 4, 1),
    _Me1200IpSourceGuardControlTranslateDynamicToStatic_Type()
)
me1200IpSourceGuardControlTranslateDynamicToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpSourceGuardControlTranslateDynamicToStatic.setStatus("current")
_Me1200IpSourceGuardMIBConformance_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardMIBConformance = _Me1200IpSourceGuardMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2)
)
_Me1200IpSourceGuardMIBCompliances_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardMIBCompliances = _Me1200IpSourceGuardMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 1)
)
_Me1200IpSourceGuardMIBGroups_ObjectIdentity = ObjectIdentity
me1200IpSourceGuardMIBGroups = _Me1200IpSourceGuardMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 2)
)

# Managed Objects groups

me1200IpSourceGuardGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 2, 1)
)
me1200IpSourceGuardGlobalsInfoGroup.setObjects(
    ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardGlobalsMode")
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardGlobalsInfoGroup.setStatus("current")

me1200IpSourceGuardInterfaceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 2, 2)
)
me1200IpSourceGuardInterfaceInfoGroup.setObjects(
      *(("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardInterfaceMode"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardInterfaceDynamicEntryCount"))
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardInterfaceInfoGroup.setStatus("current")

me1200IpSourceGuardStaticConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 2, 3)
)
me1200IpSourceGuardStaticConfigTableInfoGroup.setObjects(
      *(("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigMacAddress"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigAction"))
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigTableInfoGroup.setStatus("current")

me1200IpSourceGuardStaticConfigTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 2, 4)
)
me1200IpSourceGuardStaticConfigTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigTableRowEditorIfIndex"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigTableRowEditorVlanId"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigTableRowEditorIpAddress"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigTableRowEditorMacAddress"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardStaticConfigTableRowEditorInfoGroup.setStatus("current")

me1200IpSourceGuardDynamicStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 2, 5)
)
me1200IpSourceGuardDynamicStatusTableInfoGroup.setObjects(
    ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardDynamicStatusMacAddress")
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardDynamicStatusTableInfoGroup.setStatus("current")

me1200IpSourceGuardControlInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 2, 6)
)
me1200IpSourceGuardControlInfoGroup.setObjects(
    ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardControlTranslateDynamicToStatic")
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardControlInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200IpSourceGuardMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 64, 2, 1, 1)
)
me1200IpSourceGuardMIBCompliance.setObjects(
      *(("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardGlobalsInfoGroup"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardInterfaceInfoGroup"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigTableInfoGroup"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardStaticConfigTableRowEditorInfoGroup"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardDynamicStatusTableInfoGroup"),
        ("ME1200-IP-SOURCE-GUARD-MIB", "me1200IpSourceGuardControlInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200IpSourceGuardMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-IP-SOURCE-GUARD-MIB",
    **{"me1200IpSourceGuardMIB": me1200IpSourceGuardMIB,
       "me1200IpSourceGuardMIBObjects": me1200IpSourceGuardMIBObjects,
       "me1200IpSourceGuardConfig": me1200IpSourceGuardConfig,
       "me1200IpSourceGuardGlobals": me1200IpSourceGuardGlobals,
       "me1200IpSourceGuardGlobalsMode": me1200IpSourceGuardGlobalsMode,
       "me1200IpSourceGuardInterfaceTable": me1200IpSourceGuardInterfaceTable,
       "me1200IpSourceGuardInterfaceEntry": me1200IpSourceGuardInterfaceEntry,
       "me1200IpSourceGuardInterfaceIfIndex": me1200IpSourceGuardInterfaceIfIndex,
       "me1200IpSourceGuardInterfaceMode": me1200IpSourceGuardInterfaceMode,
       "me1200IpSourceGuardInterfaceDynamicEntryCount": me1200IpSourceGuardInterfaceDynamicEntryCount,
       "me1200IpSourceGuardStaticConfigTable": me1200IpSourceGuardStaticConfigTable,
       "me1200IpSourceGuardStaticConfigEntry": me1200IpSourceGuardStaticConfigEntry,
       "me1200IpSourceGuardStaticConfigIfIndex": me1200IpSourceGuardStaticConfigIfIndex,
       "me1200IpSourceGuardStaticConfigVlanId": me1200IpSourceGuardStaticConfigVlanId,
       "me1200IpSourceGuardStaticConfigIpAddress": me1200IpSourceGuardStaticConfigIpAddress,
       "me1200IpSourceGuardStaticConfigMacAddress": me1200IpSourceGuardStaticConfigMacAddress,
       "me1200IpSourceGuardStaticConfigAction": me1200IpSourceGuardStaticConfigAction,
       "me1200IpSourceGuardStaticConfigTableRowEditor": me1200IpSourceGuardStaticConfigTableRowEditor,
       "me1200IpSourceGuardStaticConfigTableRowEditorIfIndex": me1200IpSourceGuardStaticConfigTableRowEditorIfIndex,
       "me1200IpSourceGuardStaticConfigTableRowEditorVlanId": me1200IpSourceGuardStaticConfigTableRowEditorVlanId,
       "me1200IpSourceGuardStaticConfigTableRowEditorIpAddress": me1200IpSourceGuardStaticConfigTableRowEditorIpAddress,
       "me1200IpSourceGuardStaticConfigTableRowEditorMacAddress": me1200IpSourceGuardStaticConfigTableRowEditorMacAddress,
       "me1200IpSourceGuardStaticConfigTableRowEditorAction": me1200IpSourceGuardStaticConfigTableRowEditorAction,
       "me1200IpSourceGuardStatus": me1200IpSourceGuardStatus,
       "me1200IpSourceGuardDynamicStatusTable": me1200IpSourceGuardDynamicStatusTable,
       "me1200IpSourceGuardDynamicStatusEntry": me1200IpSourceGuardDynamicStatusEntry,
       "me1200IpSourceGuardDynamicStatusIfIndex": me1200IpSourceGuardDynamicStatusIfIndex,
       "me1200IpSourceGuardDynamicStatusVlanId": me1200IpSourceGuardDynamicStatusVlanId,
       "me1200IpSourceGuardDynamicStatusIpAddress": me1200IpSourceGuardDynamicStatusIpAddress,
       "me1200IpSourceGuardDynamicStatusMacAddress": me1200IpSourceGuardDynamicStatusMacAddress,
       "me1200IpSourceGuardControl": me1200IpSourceGuardControl,
       "me1200IpSourceGuardControlTranslateDynamicToStatic": me1200IpSourceGuardControlTranslateDynamicToStatic,
       "me1200IpSourceGuardMIBConformance": me1200IpSourceGuardMIBConformance,
       "me1200IpSourceGuardMIBCompliances": me1200IpSourceGuardMIBCompliances,
       "me1200IpSourceGuardMIBCompliance": me1200IpSourceGuardMIBCompliance,
       "me1200IpSourceGuardMIBGroups": me1200IpSourceGuardMIBGroups,
       "me1200IpSourceGuardGlobalsInfoGroup": me1200IpSourceGuardGlobalsInfoGroup,
       "me1200IpSourceGuardInterfaceInfoGroup": me1200IpSourceGuardInterfaceInfoGroup,
       "me1200IpSourceGuardStaticConfigTableInfoGroup": me1200IpSourceGuardStaticConfigTableInfoGroup,
       "me1200IpSourceGuardStaticConfigTableRowEditorInfoGroup": me1200IpSourceGuardStaticConfigTableRowEditorInfoGroup,
       "me1200IpSourceGuardDynamicStatusTableInfoGroup": me1200IpSourceGuardDynamicStatusTableInfoGroup,
       "me1200IpSourceGuardControlInfoGroup": me1200IpSourceGuardControlInfoGroup}
)
