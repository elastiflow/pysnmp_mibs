# SNMP MIB module (ME1200-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-MAC-MIB.mib
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
 ME1200PortListStackable,
 ME1200RowEditorState,
 ME1200Unsigned8,
 ME1200Vlan) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200PortListStackable",
    "ME1200RowEditorState",
    "ME1200Unsigned8",
    "ME1200Vlan")

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

me1200MacMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12)
)
if mibBuilder.loadTexts:
    me1200MacMib.setRevisions(
        ("2014-03-28 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2014-01-22 00:00",
         "2013-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200MACPortLearnMode(TextualConvention, Integer32):
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
        *(("auto", 0),
          ("disable", 1),
          ("secure", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200MacMIBObjects_ObjectIdentity = ObjectIdentity
me1200MacMIBObjects = _Me1200MacMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1)
)
_Me1200MacCapabilities_ObjectIdentity = ObjectIdentity
me1200MacCapabilities = _Me1200MacCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 1)
)
_Me1200MacCapabilitiesNonVolatileMax_Type = Unsigned32
_Me1200MacCapabilitiesNonVolatileMax_Object = MibScalar
me1200MacCapabilitiesNonVolatileMax = _Me1200MacCapabilitiesNonVolatileMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 1, 1),
    _Me1200MacCapabilitiesNonVolatileMax_Type()
)
me1200MacCapabilitiesNonVolatileMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacCapabilitiesNonVolatileMax.setStatus("current")
_Me1200MacConfig_ObjectIdentity = ObjectIdentity
me1200MacConfig = _Me1200MacConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2)
)
_Me1200MacFdbGlobal_ObjectIdentity = ObjectIdentity
me1200MacFdbGlobal = _Me1200MacFdbGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 1)
)
_Me1200MacFdbGlobalAgeTime_Type = Unsigned32
_Me1200MacFdbGlobalAgeTime_Object = MibScalar
me1200MacFdbGlobalAgeTime = _Me1200MacFdbGlobalAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 1, 1),
    _Me1200MacFdbGlobalAgeTime_Type()
)
me1200MacFdbGlobalAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacFdbGlobalAgeTime.setStatus("current")
_Me1200MacFdbConfigTable_Object = MibTable
me1200MacFdbConfigTable = _Me1200MacFdbConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200MacFdbConfigTable.setStatus("current")
_Me1200MacFdbConfigEntry_Object = MibTableRow
me1200MacFdbConfigEntry = _Me1200MacFdbConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 2, 1)
)
me1200MacFdbConfigEntry.setIndexNames(
    (0, "ME1200-MAC-MIB", "me1200MacFdbConfigVlanId"),
    (0, "ME1200-MAC-MIB", "me1200MacFdbConfigMacAddress"),
)
if mibBuilder.loadTexts:
    me1200MacFdbConfigEntry.setStatus("current")
_Me1200MacFdbConfigVlanId_Type = ME1200Vlan
_Me1200MacFdbConfigVlanId_Object = MibTableColumn
me1200MacFdbConfigVlanId = _Me1200MacFdbConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 2, 1, 1),
    _Me1200MacFdbConfigVlanId_Type()
)
me1200MacFdbConfigVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacFdbConfigVlanId.setStatus("current")
_Me1200MacFdbConfigMacAddress_Type = MacAddress
_Me1200MacFdbConfigMacAddress_Object = MibTableColumn
me1200MacFdbConfigMacAddress = _Me1200MacFdbConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 2, 1, 2),
    _Me1200MacFdbConfigMacAddress_Type()
)
me1200MacFdbConfigMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacFdbConfigMacAddress.setStatus("current")
_Me1200MacFdbConfigPortList_Type = ME1200PortListStackable
_Me1200MacFdbConfigPortList_Object = MibTableColumn
me1200MacFdbConfigPortList = _Me1200MacFdbConfigPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 2, 1, 3),
    _Me1200MacFdbConfigPortList_Type()
)
me1200MacFdbConfigPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacFdbConfigPortList.setStatus("current")
_Me1200MacFdbConfigAction_Type = ME1200RowEditorState
_Me1200MacFdbConfigAction_Object = MibTableColumn
me1200MacFdbConfigAction = _Me1200MacFdbConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 2, 1, 100),
    _Me1200MacFdbConfigAction_Type()
)
me1200MacFdbConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacFdbConfigAction.setStatus("current")
_Me1200MacFdbConfigTableRowEditor_ObjectIdentity = ObjectIdentity
me1200MacFdbConfigTableRowEditor = _Me1200MacFdbConfigTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 3)
)
_Me1200MacFdbConfigTableRowEditorVlanId_Type = ME1200Vlan
_Me1200MacFdbConfigTableRowEditorVlanId_Object = MibScalar
me1200MacFdbConfigTableRowEditorVlanId = _Me1200MacFdbConfigTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 3, 1),
    _Me1200MacFdbConfigTableRowEditorVlanId_Type()
)
me1200MacFdbConfigTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacFdbConfigTableRowEditorVlanId.setStatus("current")
_Me1200MacFdbConfigTableRowEditorMacAddress_Type = MacAddress
_Me1200MacFdbConfigTableRowEditorMacAddress_Object = MibScalar
me1200MacFdbConfigTableRowEditorMacAddress = _Me1200MacFdbConfigTableRowEditorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 3, 2),
    _Me1200MacFdbConfigTableRowEditorMacAddress_Type()
)
me1200MacFdbConfigTableRowEditorMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacFdbConfigTableRowEditorMacAddress.setStatus("current")
_Me1200MacFdbConfigTableRowEditorPortList_Type = ME1200PortListStackable
_Me1200MacFdbConfigTableRowEditorPortList_Object = MibScalar
me1200MacFdbConfigTableRowEditorPortList = _Me1200MacFdbConfigTableRowEditorPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 3, 3),
    _Me1200MacFdbConfigTableRowEditorPortList_Type()
)
me1200MacFdbConfigTableRowEditorPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacFdbConfigTableRowEditorPortList.setStatus("current")
_Me1200MacFdbConfigTableRowEditorAction_Type = ME1200RowEditorState
_Me1200MacFdbConfigTableRowEditorAction_Object = MibScalar
me1200MacFdbConfigTableRowEditorAction = _Me1200MacFdbConfigTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 3, 100),
    _Me1200MacFdbConfigTableRowEditorAction_Type()
)
me1200MacFdbConfigTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacFdbConfigTableRowEditorAction.setStatus("current")
_Me1200MacConfigPortLearnTable_Object = MibTable
me1200MacConfigPortLearnTable = _Me1200MacConfigPortLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 4)
)
if mibBuilder.loadTexts:
    me1200MacConfigPortLearnTable.setStatus("current")
_Me1200MacConfigPortLearnEntry_Object = MibTableRow
me1200MacConfigPortLearnEntry = _Me1200MacConfigPortLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 4, 1)
)
me1200MacConfigPortLearnEntry.setIndexNames(
    (0, "ME1200-MAC-MIB", "me1200MacConfigPortLearnIfIndex"),
)
if mibBuilder.loadTexts:
    me1200MacConfigPortLearnEntry.setStatus("current")
_Me1200MacConfigPortLearnIfIndex_Type = ME1200InterfaceIndex
_Me1200MacConfigPortLearnIfIndex_Object = MibTableColumn
me1200MacConfigPortLearnIfIndex = _Me1200MacConfigPortLearnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 4, 1, 1),
    _Me1200MacConfigPortLearnIfIndex_Type()
)
me1200MacConfigPortLearnIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacConfigPortLearnIfIndex.setStatus("current")
_Me1200MacConfigPortLearnLearnMode_Type = ME1200MACPortLearnMode
_Me1200MacConfigPortLearnLearnMode_Object = MibTableColumn
me1200MacConfigPortLearnLearnMode = _Me1200MacConfigPortLearnLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 4, 1, 2),
    _Me1200MacConfigPortLearnLearnMode_Type()
)
me1200MacConfigPortLearnLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacConfigPortLearnLearnMode.setStatus("current")
_Me1200MacConfigPortLearnChangeAllowed_Type = TruthValue
_Me1200MacConfigPortLearnChangeAllowed_Object = MibTableColumn
me1200MacConfigPortLearnChangeAllowed = _Me1200MacConfigPortLearnChangeAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 4, 1, 3),
    _Me1200MacConfigPortLearnChangeAllowed_Type()
)
me1200MacConfigPortLearnChangeAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacConfigPortLearnChangeAllowed.setStatus("current")
_Me1200MacConfigVlanLearnTable_Object = MibTable
me1200MacConfigVlanLearnTable = _Me1200MacConfigVlanLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 5)
)
if mibBuilder.loadTexts:
    me1200MacConfigVlanLearnTable.setStatus("current")
_Me1200MacConfigVlanLearnEntry_Object = MibTableRow
me1200MacConfigVlanLearnEntry = _Me1200MacConfigVlanLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 5, 1)
)
me1200MacConfigVlanLearnEntry.setIndexNames(
    (0, "ME1200-MAC-MIB", "me1200MacConfigVlanLearnVlanId"),
)
if mibBuilder.loadTexts:
    me1200MacConfigVlanLearnEntry.setStatus("current")
_Me1200MacConfigVlanLearnVlanId_Type = ME1200Vlan
_Me1200MacConfigVlanLearnVlanId_Object = MibTableColumn
me1200MacConfigVlanLearnVlanId = _Me1200MacConfigVlanLearnVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 5, 1, 1),
    _Me1200MacConfigVlanLearnVlanId_Type()
)
me1200MacConfigVlanLearnVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacConfigVlanLearnVlanId.setStatus("current")
_Me1200MacConfigVlanLearnMode_Type = TruthValue
_Me1200MacConfigVlanLearnMode_Object = MibTableColumn
me1200MacConfigVlanLearnMode = _Me1200MacConfigVlanLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 2, 5, 1, 2),
    _Me1200MacConfigVlanLearnMode_Type()
)
me1200MacConfigVlanLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacConfigVlanLearnMode.setStatus("current")
_Me1200MacStatus_ObjectIdentity = ObjectIdentity
me1200MacStatus = _Me1200MacStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3)
)
_Me1200MacFdbTable_Object = MibTable
me1200MacFdbTable = _Me1200MacFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200MacFdbTable.setStatus("current")
_Me1200MacFdbEntry_Object = MibTableRow
me1200MacFdbEntry = _Me1200MacFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 1, 1)
)
me1200MacFdbEntry.setIndexNames(
    (0, "ME1200-MAC-MIB", "me1200MacFdbVlanId"),
    (0, "ME1200-MAC-MIB", "me1200MacFdbMacAddress"),
)
if mibBuilder.loadTexts:
    me1200MacFdbEntry.setStatus("current")
_Me1200MacFdbVlanId_Type = ME1200Vlan
_Me1200MacFdbVlanId_Object = MibTableColumn
me1200MacFdbVlanId = _Me1200MacFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 1, 1, 1),
    _Me1200MacFdbVlanId_Type()
)
me1200MacFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacFdbVlanId.setStatus("current")
_Me1200MacFdbMacAddress_Type = MacAddress
_Me1200MacFdbMacAddress_Object = MibTableColumn
me1200MacFdbMacAddress = _Me1200MacFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 1, 1, 2),
    _Me1200MacFdbMacAddress_Type()
)
me1200MacFdbMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacFdbMacAddress.setStatus("current")
_Me1200MacFdbPortList_Type = ME1200PortListStackable
_Me1200MacFdbPortList_Object = MibTableColumn
me1200MacFdbPortList = _Me1200MacFdbPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 1, 1, 3),
    _Me1200MacFdbPortList_Type()
)
me1200MacFdbPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbPortList.setStatus("current")
_Me1200MacFdbDynamic_Type = ME1200Unsigned8
_Me1200MacFdbDynamic_Object = MibTableColumn
me1200MacFdbDynamic = _Me1200MacFdbDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 1, 1, 4),
    _Me1200MacFdbDynamic_Type()
)
me1200MacFdbDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbDynamic.setStatus("current")
_Me1200MacFdbCopyToCpu_Type = ME1200Unsigned8
_Me1200MacFdbCopyToCpu_Object = MibTableColumn
me1200MacFdbCopyToCpu = _Me1200MacFdbCopyToCpu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 1, 1, 5),
    _Me1200MacFdbCopyToCpu_Type()
)
me1200MacFdbCopyToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbCopyToCpu.setStatus("current")
_Me1200MacFdbStaticTable_Object = MibTable
me1200MacFdbStaticTable = _Me1200MacFdbStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200MacFdbStaticTable.setStatus("current")
_Me1200MacFdbStaticEntry_Object = MibTableRow
me1200MacFdbStaticEntry = _Me1200MacFdbStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 2, 1)
)
me1200MacFdbStaticEntry.setIndexNames(
    (0, "ME1200-MAC-MIB", "me1200MacFdbStaticVlanId"),
    (0, "ME1200-MAC-MIB", "me1200MacFdbStaticMacAddress"),
)
if mibBuilder.loadTexts:
    me1200MacFdbStaticEntry.setStatus("current")
_Me1200MacFdbStaticVlanId_Type = ME1200Vlan
_Me1200MacFdbStaticVlanId_Object = MibTableColumn
me1200MacFdbStaticVlanId = _Me1200MacFdbStaticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 2, 1, 1),
    _Me1200MacFdbStaticVlanId_Type()
)
me1200MacFdbStaticVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacFdbStaticVlanId.setStatus("current")
_Me1200MacFdbStaticMacAddress_Type = MacAddress
_Me1200MacFdbStaticMacAddress_Object = MibTableColumn
me1200MacFdbStaticMacAddress = _Me1200MacFdbStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 2, 1, 2),
    _Me1200MacFdbStaticMacAddress_Type()
)
me1200MacFdbStaticMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacFdbStaticMacAddress.setStatus("current")
_Me1200MacFdbStaticPortList_Type = ME1200PortListStackable
_Me1200MacFdbStaticPortList_Object = MibTableColumn
me1200MacFdbStaticPortList = _Me1200MacFdbStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 2, 1, 3),
    _Me1200MacFdbStaticPortList_Type()
)
me1200MacFdbStaticPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbStaticPortList.setStatus("current")
_Me1200MacFdbStaticDynamic_Type = ME1200Unsigned8
_Me1200MacFdbStaticDynamic_Object = MibTableColumn
me1200MacFdbStaticDynamic = _Me1200MacFdbStaticDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 2, 1, 4),
    _Me1200MacFdbStaticDynamic_Type()
)
me1200MacFdbStaticDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbStaticDynamic.setStatus("current")
_Me1200MacFdbStaticCopyToCpu_Type = ME1200Unsigned8
_Me1200MacFdbStaticCopyToCpu_Object = MibTableColumn
me1200MacFdbStaticCopyToCpu = _Me1200MacFdbStaticCopyToCpu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 2, 1, 5),
    _Me1200MacFdbStaticCopyToCpu_Type()
)
me1200MacFdbStaticCopyToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbStaticCopyToCpu.setStatus("current")
_Me1200MacFdbPortStatisticsTable_Object = MibTable
me1200MacFdbPortStatisticsTable = _Me1200MacFdbPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200MacFdbPortStatisticsTable.setStatus("current")
_Me1200MacFdbPortStatisticsEntry_Object = MibTableRow
me1200MacFdbPortStatisticsEntry = _Me1200MacFdbPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 3, 1)
)
me1200MacFdbPortStatisticsEntry.setIndexNames(
    (0, "ME1200-MAC-MIB", "me1200MacFdbPortStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    me1200MacFdbPortStatisticsEntry.setStatus("current")
_Me1200MacFdbPortStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200MacFdbPortStatisticsIfIndex_Object = MibTableColumn
me1200MacFdbPortStatisticsIfIndex = _Me1200MacFdbPortStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 3, 1, 1),
    _Me1200MacFdbPortStatisticsIfIndex_Type()
)
me1200MacFdbPortStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MacFdbPortStatisticsIfIndex.setStatus("current")
_Me1200MacFdbPortStatisticsDynamic_Type = Unsigned32
_Me1200MacFdbPortStatisticsDynamic_Object = MibTableColumn
me1200MacFdbPortStatisticsDynamic = _Me1200MacFdbPortStatisticsDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 3, 1, 2),
    _Me1200MacFdbPortStatisticsDynamic_Type()
)
me1200MacFdbPortStatisticsDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbPortStatisticsDynamic.setStatus("current")
_Me1200MacFdbStatistics_ObjectIdentity = ObjectIdentity
me1200MacFdbStatistics = _Me1200MacFdbStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 4)
)
_Me1200MacFdbStatisticsTotalDynamic_Type = Unsigned32
_Me1200MacFdbStatisticsTotalDynamic_Object = MibScalar
me1200MacFdbStatisticsTotalDynamic = _Me1200MacFdbStatisticsTotalDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 4, 1),
    _Me1200MacFdbStatisticsTotalDynamic_Type()
)
me1200MacFdbStatisticsTotalDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbStatisticsTotalDynamic.setStatus("current")
_Me1200MacFdbStatisticsTotalStatic_Type = Unsigned32
_Me1200MacFdbStatisticsTotalStatic_Object = MibScalar
me1200MacFdbStatisticsTotalStatic = _Me1200MacFdbStatisticsTotalStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 3, 4, 2),
    _Me1200MacFdbStatisticsTotalStatic_Type()
)
me1200MacFdbStatisticsTotalStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MacFdbStatisticsTotalStatic.setStatus("current")
_Me1200MacControl_ObjectIdentity = ObjectIdentity
me1200MacControl = _Me1200MacControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 4)
)
_Me1200MacControlFlushAll_Type = TruthValue
_Me1200MacControlFlushAll_Object = MibScalar
me1200MacControlFlushAll = _Me1200MacControlFlushAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 1, 4, 1),
    _Me1200MacControlFlushAll_Type()
)
me1200MacControlFlushAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MacControlFlushAll.setStatus("current")
_Me1200MacMIBConformance_ObjectIdentity = ObjectIdentity
me1200MacMIBConformance = _Me1200MacMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2)
)
_Me1200MacMIBCompliances_ObjectIdentity = ObjectIdentity
me1200MacMIBCompliances = _Me1200MacMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 1)
)
_Me1200MacMIBGroups_ObjectIdentity = ObjectIdentity
me1200MacMIBGroups = _Me1200MacMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2)
)

# Managed Objects groups

me1200MacCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 1)
)
me1200MacCapabilitiesInfoGroup.setObjects(
    ("ME1200-MAC-MIB", "me1200MacCapabilitiesNonVolatileMax")
)
if mibBuilder.loadTexts:
    me1200MacCapabilitiesInfoGroup.setStatus("current")

me1200MacFdbGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 2)
)
me1200MacFdbGlobalInfoGroup.setObjects(
    ("ME1200-MAC-MIB", "me1200MacFdbGlobalAgeTime")
)
if mibBuilder.loadTexts:
    me1200MacFdbGlobalInfoGroup.setStatus("current")

me1200MacFdbConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 3)
)
me1200MacFdbConfigTableInfoGroup.setObjects(
      *(("ME1200-MAC-MIB", "me1200MacFdbConfigPortList"),
        ("ME1200-MAC-MIB", "me1200MacFdbConfigAction"))
)
if mibBuilder.loadTexts:
    me1200MacFdbConfigTableInfoGroup.setStatus("current")

me1200MacFdbConfigTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 4)
)
me1200MacFdbConfigTableRowEditorInfoGroup.setObjects(
      *(("ME1200-MAC-MIB", "me1200MacFdbConfigTableRowEditorVlanId"),
        ("ME1200-MAC-MIB", "me1200MacFdbConfigTableRowEditorMacAddress"),
        ("ME1200-MAC-MIB", "me1200MacFdbConfigTableRowEditorPortList"),
        ("ME1200-MAC-MIB", "me1200MacFdbConfigTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200MacFdbConfigTableRowEditorInfoGroup.setStatus("current")

me1200MacConfigPortLearnInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 5)
)
me1200MacConfigPortLearnInfoGroup.setObjects(
      *(("ME1200-MAC-MIB", "me1200MacConfigPortLearnLearnMode"),
        ("ME1200-MAC-MIB", "me1200MacConfigPortLearnChangeAllowed"))
)
if mibBuilder.loadTexts:
    me1200MacConfigPortLearnInfoGroup.setStatus("current")

me1200MacConfigVlanLearnInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 6)
)
me1200MacConfigVlanLearnInfoGroup.setObjects(
    ("ME1200-MAC-MIB", "me1200MacConfigVlanLearnMode")
)
if mibBuilder.loadTexts:
    me1200MacConfigVlanLearnInfoGroup.setStatus("current")

me1200MacFdbTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 7)
)
me1200MacFdbTableInfoGroup.setObjects(
      *(("ME1200-MAC-MIB", "me1200MacFdbPortList"),
        ("ME1200-MAC-MIB", "me1200MacFdbDynamic"),
        ("ME1200-MAC-MIB", "me1200MacFdbCopyToCpu"))
)
if mibBuilder.loadTexts:
    me1200MacFdbTableInfoGroup.setStatus("current")

me1200MacFdbStaticTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 8)
)
me1200MacFdbStaticTableInfoGroup.setObjects(
      *(("ME1200-MAC-MIB", "me1200MacFdbStaticPortList"),
        ("ME1200-MAC-MIB", "me1200MacFdbStaticDynamic"),
        ("ME1200-MAC-MIB", "me1200MacFdbStaticCopyToCpu"))
)
if mibBuilder.loadTexts:
    me1200MacFdbStaticTableInfoGroup.setStatus("current")

me1200MacFdbPortStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 9)
)
me1200MacFdbPortStatisticsInfoGroup.setObjects(
    ("ME1200-MAC-MIB", "me1200MacFdbPortStatisticsDynamic")
)
if mibBuilder.loadTexts:
    me1200MacFdbPortStatisticsInfoGroup.setStatus("current")

me1200MacFdbStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 10)
)
me1200MacFdbStatisticsInfoGroup.setObjects(
      *(("ME1200-MAC-MIB", "me1200MacFdbStatisticsTotalDynamic"),
        ("ME1200-MAC-MIB", "me1200MacFdbStatisticsTotalStatic"))
)
if mibBuilder.loadTexts:
    me1200MacFdbStatisticsInfoGroup.setStatus("current")

me1200MacControlInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 2, 11)
)
me1200MacControlInfoGroup.setObjects(
    ("ME1200-MAC-MIB", "me1200MacControlFlushAll")
)
if mibBuilder.loadTexts:
    me1200MacControlInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200MacMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 12, 2, 1, 1)
)
me1200MacMibCompliance.setObjects(
      *(("ME1200-MAC-MIB", "me1200MacCapabilitiesInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacFdbGlobalInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacFdbConfigTableInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacFdbConfigTableRowEditorInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacConfigPortLearnInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacConfigVlanLearnInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacFdbTableInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacFdbStaticTableInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacFdbPortStatisticsInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacFdbStatisticsInfoGroup"),
        ("ME1200-MAC-MIB", "me1200MacControlInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200MacMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-MAC-MIB",
    **{"ME1200MACPortLearnMode": ME1200MACPortLearnMode,
       "me1200MacMib": me1200MacMib,
       "me1200MacMIBObjects": me1200MacMIBObjects,
       "me1200MacCapabilities": me1200MacCapabilities,
       "me1200MacCapabilitiesNonVolatileMax": me1200MacCapabilitiesNonVolatileMax,
       "me1200MacConfig": me1200MacConfig,
       "me1200MacFdbGlobal": me1200MacFdbGlobal,
       "me1200MacFdbGlobalAgeTime": me1200MacFdbGlobalAgeTime,
       "me1200MacFdbConfigTable": me1200MacFdbConfigTable,
       "me1200MacFdbConfigEntry": me1200MacFdbConfigEntry,
       "me1200MacFdbConfigVlanId": me1200MacFdbConfigVlanId,
       "me1200MacFdbConfigMacAddress": me1200MacFdbConfigMacAddress,
       "me1200MacFdbConfigPortList": me1200MacFdbConfigPortList,
       "me1200MacFdbConfigAction": me1200MacFdbConfigAction,
       "me1200MacFdbConfigTableRowEditor": me1200MacFdbConfigTableRowEditor,
       "me1200MacFdbConfigTableRowEditorVlanId": me1200MacFdbConfigTableRowEditorVlanId,
       "me1200MacFdbConfigTableRowEditorMacAddress": me1200MacFdbConfigTableRowEditorMacAddress,
       "me1200MacFdbConfigTableRowEditorPortList": me1200MacFdbConfigTableRowEditorPortList,
       "me1200MacFdbConfigTableRowEditorAction": me1200MacFdbConfigTableRowEditorAction,
       "me1200MacConfigPortLearnTable": me1200MacConfigPortLearnTable,
       "me1200MacConfigPortLearnEntry": me1200MacConfigPortLearnEntry,
       "me1200MacConfigPortLearnIfIndex": me1200MacConfigPortLearnIfIndex,
       "me1200MacConfigPortLearnLearnMode": me1200MacConfigPortLearnLearnMode,
       "me1200MacConfigPortLearnChangeAllowed": me1200MacConfigPortLearnChangeAllowed,
       "me1200MacConfigVlanLearnTable": me1200MacConfigVlanLearnTable,
       "me1200MacConfigVlanLearnEntry": me1200MacConfigVlanLearnEntry,
       "me1200MacConfigVlanLearnVlanId": me1200MacConfigVlanLearnVlanId,
       "me1200MacConfigVlanLearnMode": me1200MacConfigVlanLearnMode,
       "me1200MacStatus": me1200MacStatus,
       "me1200MacFdbTable": me1200MacFdbTable,
       "me1200MacFdbEntry": me1200MacFdbEntry,
       "me1200MacFdbVlanId": me1200MacFdbVlanId,
       "me1200MacFdbMacAddress": me1200MacFdbMacAddress,
       "me1200MacFdbPortList": me1200MacFdbPortList,
       "me1200MacFdbDynamic": me1200MacFdbDynamic,
       "me1200MacFdbCopyToCpu": me1200MacFdbCopyToCpu,
       "me1200MacFdbStaticTable": me1200MacFdbStaticTable,
       "me1200MacFdbStaticEntry": me1200MacFdbStaticEntry,
       "me1200MacFdbStaticVlanId": me1200MacFdbStaticVlanId,
       "me1200MacFdbStaticMacAddress": me1200MacFdbStaticMacAddress,
       "me1200MacFdbStaticPortList": me1200MacFdbStaticPortList,
       "me1200MacFdbStaticDynamic": me1200MacFdbStaticDynamic,
       "me1200MacFdbStaticCopyToCpu": me1200MacFdbStaticCopyToCpu,
       "me1200MacFdbPortStatisticsTable": me1200MacFdbPortStatisticsTable,
       "me1200MacFdbPortStatisticsEntry": me1200MacFdbPortStatisticsEntry,
       "me1200MacFdbPortStatisticsIfIndex": me1200MacFdbPortStatisticsIfIndex,
       "me1200MacFdbPortStatisticsDynamic": me1200MacFdbPortStatisticsDynamic,
       "me1200MacFdbStatistics": me1200MacFdbStatistics,
       "me1200MacFdbStatisticsTotalDynamic": me1200MacFdbStatisticsTotalDynamic,
       "me1200MacFdbStatisticsTotalStatic": me1200MacFdbStatisticsTotalStatic,
       "me1200MacControl": me1200MacControl,
       "me1200MacControlFlushAll": me1200MacControlFlushAll,
       "me1200MacMIBConformance": me1200MacMIBConformance,
       "me1200MacMIBCompliances": me1200MacMIBCompliances,
       "me1200MacMibCompliance": me1200MacMibCompliance,
       "me1200MacMIBGroups": me1200MacMIBGroups,
       "me1200MacCapabilitiesInfoGroup": me1200MacCapabilitiesInfoGroup,
       "me1200MacFdbGlobalInfoGroup": me1200MacFdbGlobalInfoGroup,
       "me1200MacFdbConfigTableInfoGroup": me1200MacFdbConfigTableInfoGroup,
       "me1200MacFdbConfigTableRowEditorInfoGroup": me1200MacFdbConfigTableRowEditorInfoGroup,
       "me1200MacConfigPortLearnInfoGroup": me1200MacConfigPortLearnInfoGroup,
       "me1200MacConfigVlanLearnInfoGroup": me1200MacConfigVlanLearnInfoGroup,
       "me1200MacFdbTableInfoGroup": me1200MacFdbTableInfoGroup,
       "me1200MacFdbStaticTableInfoGroup": me1200MacFdbStaticTableInfoGroup,
       "me1200MacFdbPortStatisticsInfoGroup": me1200MacFdbPortStatisticsInfoGroup,
       "me1200MacFdbStatisticsInfoGroup": me1200MacFdbStatisticsInfoGroup,
       "me1200MacControlInfoGroup": me1200MacControlInfoGroup}
)
