# SNMP MIB module (CIE1000-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-MAC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(CIE1000InterfaceIndex,
 CIE1000PortList,
 CIE1000RowEditorState,
 CIE1000Unsigned8,
 CIE1000Vlan) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000InterfaceIndex",
    "CIE1000PortList",
    "CIE1000RowEditorState",
    "CIE1000Unsigned8",
    "CIE1000Vlan")

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

cie1000MacMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12)
)
if mibBuilder.loadTexts:
    cie1000MacMib.setRevisions(
        ("2014-08-20 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000MACPortLearnMode(TextualConvention, Integer32):
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

_Cie1000MacMibObjects_ObjectIdentity = ObjectIdentity
cie1000MacMibObjects = _Cie1000MacMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1)
)
_Cie1000MacCapabilities_ObjectIdentity = ObjectIdentity
cie1000MacCapabilities = _Cie1000MacCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 1)
)
_Cie1000MacCapabilitiesNonVolatileMax_Type = Unsigned32
_Cie1000MacCapabilitiesNonVolatileMax_Object = MibScalar
cie1000MacCapabilitiesNonVolatileMax = _Cie1000MacCapabilitiesNonVolatileMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 1, 1),
    _Cie1000MacCapabilitiesNonVolatileMax_Type()
)
cie1000MacCapabilitiesNonVolatileMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacCapabilitiesNonVolatileMax.setStatus("current")
_Cie1000MacConfig_ObjectIdentity = ObjectIdentity
cie1000MacConfig = _Cie1000MacConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2)
)
_Cie1000MacConfigFdbGlobal_ObjectIdentity = ObjectIdentity
cie1000MacConfigFdbGlobal = _Cie1000MacConfigFdbGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 1)
)
_Cie1000MacConfigFdbGlobalAgeTime_Type = Unsigned32
_Cie1000MacConfigFdbGlobalAgeTime_Object = MibScalar
cie1000MacConfigFdbGlobalAgeTime = _Cie1000MacConfigFdbGlobalAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 1, 1),
    _Cie1000MacConfigFdbGlobalAgeTime_Type()
)
cie1000MacConfigFdbGlobalAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbGlobalAgeTime.setStatus("current")
_Cie1000MacConfigFdbTable_Object = MibTable
cie1000MacConfigFdbTable = _Cie1000MacConfigFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000MacConfigFdbTable.setStatus("current")
_Cie1000MacConfigFdbEntry_Object = MibTableRow
cie1000MacConfigFdbEntry = _Cie1000MacConfigFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 2, 1)
)
cie1000MacConfigFdbEntry.setIndexNames(
    (0, "CIE1000-MAC-MIB", "cie1000MacConfigFdbVlanId"),
    (0, "CIE1000-MAC-MIB", "cie1000MacConfigFdbMacAddress"),
)
if mibBuilder.loadTexts:
    cie1000MacConfigFdbEntry.setStatus("current")
_Cie1000MacConfigFdbVlanId_Type = CIE1000Vlan
_Cie1000MacConfigFdbVlanId_Object = MibTableColumn
cie1000MacConfigFdbVlanId = _Cie1000MacConfigFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 2, 1, 1),
    _Cie1000MacConfigFdbVlanId_Type()
)
cie1000MacConfigFdbVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbVlanId.setStatus("current")
_Cie1000MacConfigFdbMacAddress_Type = MacAddress
_Cie1000MacConfigFdbMacAddress_Object = MibTableColumn
cie1000MacConfigFdbMacAddress = _Cie1000MacConfigFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 2, 1, 2),
    _Cie1000MacConfigFdbMacAddress_Type()
)
cie1000MacConfigFdbMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbMacAddress.setStatus("current")
_Cie1000MacConfigFdbPortList_Type = CIE1000PortList
_Cie1000MacConfigFdbPortList_Object = MibTableColumn
cie1000MacConfigFdbPortList = _Cie1000MacConfigFdbPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 2, 1, 3),
    _Cie1000MacConfigFdbPortList_Type()
)
cie1000MacConfigFdbPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbPortList.setStatus("current")
_Cie1000MacConfigFdbAction_Type = CIE1000RowEditorState
_Cie1000MacConfigFdbAction_Object = MibTableColumn
cie1000MacConfigFdbAction = _Cie1000MacConfigFdbAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 2, 1, 100),
    _Cie1000MacConfigFdbAction_Type()
)
cie1000MacConfigFdbAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbAction.setStatus("current")
_Cie1000MacConfigFdbTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000MacConfigFdbTableRowEditor = _Cie1000MacConfigFdbTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 3)
)
_Cie1000MacConfigFdbTableRowEditorVlanId_Type = CIE1000Vlan
_Cie1000MacConfigFdbTableRowEditorVlanId_Object = MibScalar
cie1000MacConfigFdbTableRowEditorVlanId = _Cie1000MacConfigFdbTableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 3, 1),
    _Cie1000MacConfigFdbTableRowEditorVlanId_Type()
)
cie1000MacConfigFdbTableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbTableRowEditorVlanId.setStatus("current")
_Cie1000MacConfigFdbTableRowEditorMacAddress_Type = MacAddress
_Cie1000MacConfigFdbTableRowEditorMacAddress_Object = MibScalar
cie1000MacConfigFdbTableRowEditorMacAddress = _Cie1000MacConfigFdbTableRowEditorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 3, 2),
    _Cie1000MacConfigFdbTableRowEditorMacAddress_Type()
)
cie1000MacConfigFdbTableRowEditorMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbTableRowEditorMacAddress.setStatus("current")
_Cie1000MacConfigFdbTableRowEditorPortList_Type = CIE1000PortList
_Cie1000MacConfigFdbTableRowEditorPortList_Object = MibScalar
cie1000MacConfigFdbTableRowEditorPortList = _Cie1000MacConfigFdbTableRowEditorPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 3, 3),
    _Cie1000MacConfigFdbTableRowEditorPortList_Type()
)
cie1000MacConfigFdbTableRowEditorPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbTableRowEditorPortList.setStatus("current")
_Cie1000MacConfigFdbTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000MacConfigFdbTableRowEditorAction_Object = MibScalar
cie1000MacConfigFdbTableRowEditorAction = _Cie1000MacConfigFdbTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 3, 100),
    _Cie1000MacConfigFdbTableRowEditorAction_Type()
)
cie1000MacConfigFdbTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigFdbTableRowEditorAction.setStatus("current")
_Cie1000MacConfigPortLearnTable_Object = MibTable
cie1000MacConfigPortLearnTable = _Cie1000MacConfigPortLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cie1000MacConfigPortLearnTable.setStatus("current")
_Cie1000MacConfigPortLearnEntry_Object = MibTableRow
cie1000MacConfigPortLearnEntry = _Cie1000MacConfigPortLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 4, 1)
)
cie1000MacConfigPortLearnEntry.setIndexNames(
    (0, "CIE1000-MAC-MIB", "cie1000MacConfigPortLearnIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000MacConfigPortLearnEntry.setStatus("current")
_Cie1000MacConfigPortLearnIfIndex_Type = CIE1000InterfaceIndex
_Cie1000MacConfigPortLearnIfIndex_Object = MibTableColumn
cie1000MacConfigPortLearnIfIndex = _Cie1000MacConfigPortLearnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 4, 1, 1),
    _Cie1000MacConfigPortLearnIfIndex_Type()
)
cie1000MacConfigPortLearnIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacConfigPortLearnIfIndex.setStatus("current")
_Cie1000MacConfigPortLearnLearnMode_Type = CIE1000MACPortLearnMode
_Cie1000MacConfigPortLearnLearnMode_Object = MibTableColumn
cie1000MacConfigPortLearnLearnMode = _Cie1000MacConfigPortLearnLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 4, 1, 2),
    _Cie1000MacConfigPortLearnLearnMode_Type()
)
cie1000MacConfigPortLearnLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigPortLearnLearnMode.setStatus("current")
_Cie1000MacConfigPortLearnChangeAllowed_Type = TruthValue
_Cie1000MacConfigPortLearnChangeAllowed_Object = MibTableColumn
cie1000MacConfigPortLearnChangeAllowed = _Cie1000MacConfigPortLearnChangeAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 4, 1, 3),
    _Cie1000MacConfigPortLearnChangeAllowed_Type()
)
cie1000MacConfigPortLearnChangeAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigPortLearnChangeAllowed.setStatus("current")
_Cie1000MacConfigVlanLearnTable_Object = MibTable
cie1000MacConfigVlanLearnTable = _Cie1000MacConfigVlanLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cie1000MacConfigVlanLearnTable.setStatus("current")
_Cie1000MacConfigVlanLearnEntry_Object = MibTableRow
cie1000MacConfigVlanLearnEntry = _Cie1000MacConfigVlanLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 5, 1)
)
cie1000MacConfigVlanLearnEntry.setIndexNames(
    (0, "CIE1000-MAC-MIB", "cie1000MacConfigVlanLearnVlanId"),
)
if mibBuilder.loadTexts:
    cie1000MacConfigVlanLearnEntry.setStatus("current")
_Cie1000MacConfigVlanLearnVlanId_Type = CIE1000Vlan
_Cie1000MacConfigVlanLearnVlanId_Object = MibTableColumn
cie1000MacConfigVlanLearnVlanId = _Cie1000MacConfigVlanLearnVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 5, 1, 1),
    _Cie1000MacConfigVlanLearnVlanId_Type()
)
cie1000MacConfigVlanLearnVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacConfigVlanLearnVlanId.setStatus("current")
_Cie1000MacConfigVlanLearnMode_Type = TruthValue
_Cie1000MacConfigVlanLearnMode_Object = MibTableColumn
cie1000MacConfigVlanLearnMode = _Cie1000MacConfigVlanLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 2, 5, 1, 2),
    _Cie1000MacConfigVlanLearnMode_Type()
)
cie1000MacConfigVlanLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacConfigVlanLearnMode.setStatus("current")
_Cie1000MacStatus_ObjectIdentity = ObjectIdentity
cie1000MacStatus = _Cie1000MacStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3)
)
_Cie1000MacStatusFdbTable_Object = MibTable
cie1000MacStatusFdbTable = _Cie1000MacStatusFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbTable.setStatus("current")
_Cie1000MacStatusFdbEntry_Object = MibTableRow
cie1000MacStatusFdbEntry = _Cie1000MacStatusFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 1, 1)
)
cie1000MacStatusFdbEntry.setIndexNames(
    (0, "CIE1000-MAC-MIB", "cie1000MacStatusFdbVlanId"),
    (0, "CIE1000-MAC-MIB", "cie1000MacStatusFdbMacAddress"),
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbEntry.setStatus("current")
_Cie1000MacStatusFdbVlanId_Type = CIE1000Vlan
_Cie1000MacStatusFdbVlanId_Object = MibTableColumn
cie1000MacStatusFdbVlanId = _Cie1000MacStatusFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 1, 1, 1),
    _Cie1000MacStatusFdbVlanId_Type()
)
cie1000MacStatusFdbVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbVlanId.setStatus("current")
_Cie1000MacStatusFdbMacAddress_Type = MacAddress
_Cie1000MacStatusFdbMacAddress_Object = MibTableColumn
cie1000MacStatusFdbMacAddress = _Cie1000MacStatusFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 1, 1, 2),
    _Cie1000MacStatusFdbMacAddress_Type()
)
cie1000MacStatusFdbMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbMacAddress.setStatus("current")
_Cie1000MacStatusFdbPortList_Type = CIE1000PortList
_Cie1000MacStatusFdbPortList_Object = MibTableColumn
cie1000MacStatusFdbPortList = _Cie1000MacStatusFdbPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 1, 1, 3),
    _Cie1000MacStatusFdbPortList_Type()
)
cie1000MacStatusFdbPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbPortList.setStatus("current")
_Cie1000MacStatusFdbDynamic_Type = CIE1000Unsigned8
_Cie1000MacStatusFdbDynamic_Object = MibTableColumn
cie1000MacStatusFdbDynamic = _Cie1000MacStatusFdbDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 1, 1, 4),
    _Cie1000MacStatusFdbDynamic_Type()
)
cie1000MacStatusFdbDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbDynamic.setStatus("current")
_Cie1000MacStatusFdbCopyToCpu_Type = CIE1000Unsigned8
_Cie1000MacStatusFdbCopyToCpu_Object = MibTableColumn
cie1000MacStatusFdbCopyToCpu = _Cie1000MacStatusFdbCopyToCpu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 1, 1, 5),
    _Cie1000MacStatusFdbCopyToCpu_Type()
)
cie1000MacStatusFdbCopyToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbCopyToCpu.setStatus("current")
_Cie1000MacStatusFdbStaticTable_Object = MibTable
cie1000MacStatusFdbStaticTable = _Cie1000MacStatusFdbStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStaticTable.setStatus("current")
_Cie1000MacStatusFdbStaticEntry_Object = MibTableRow
cie1000MacStatusFdbStaticEntry = _Cie1000MacStatusFdbStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 2, 1)
)
cie1000MacStatusFdbStaticEntry.setIndexNames(
    (0, "CIE1000-MAC-MIB", "cie1000MacStatusFdbStaticVlanId"),
    (0, "CIE1000-MAC-MIB", "cie1000MacStatusFdbStaticMacAddress"),
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStaticEntry.setStatus("current")
_Cie1000MacStatusFdbStaticVlanId_Type = CIE1000Vlan
_Cie1000MacStatusFdbStaticVlanId_Object = MibTableColumn
cie1000MacStatusFdbStaticVlanId = _Cie1000MacStatusFdbStaticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 2, 1, 1),
    _Cie1000MacStatusFdbStaticVlanId_Type()
)
cie1000MacStatusFdbStaticVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStaticVlanId.setStatus("current")
_Cie1000MacStatusFdbStaticMacAddress_Type = MacAddress
_Cie1000MacStatusFdbStaticMacAddress_Object = MibTableColumn
cie1000MacStatusFdbStaticMacAddress = _Cie1000MacStatusFdbStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 2, 1, 2),
    _Cie1000MacStatusFdbStaticMacAddress_Type()
)
cie1000MacStatusFdbStaticMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStaticMacAddress.setStatus("current")
_Cie1000MacStatusFdbStaticPortList_Type = CIE1000PortList
_Cie1000MacStatusFdbStaticPortList_Object = MibTableColumn
cie1000MacStatusFdbStaticPortList = _Cie1000MacStatusFdbStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 2, 1, 3),
    _Cie1000MacStatusFdbStaticPortList_Type()
)
cie1000MacStatusFdbStaticPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStaticPortList.setStatus("current")
_Cie1000MacStatusFdbStaticDynamic_Type = CIE1000Unsigned8
_Cie1000MacStatusFdbStaticDynamic_Object = MibTableColumn
cie1000MacStatusFdbStaticDynamic = _Cie1000MacStatusFdbStaticDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 2, 1, 4),
    _Cie1000MacStatusFdbStaticDynamic_Type()
)
cie1000MacStatusFdbStaticDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStaticDynamic.setStatus("current")
_Cie1000MacStatusFdbStaticCopyToCpu_Type = CIE1000Unsigned8
_Cie1000MacStatusFdbStaticCopyToCpu_Object = MibTableColumn
cie1000MacStatusFdbStaticCopyToCpu = _Cie1000MacStatusFdbStaticCopyToCpu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 2, 1, 5),
    _Cie1000MacStatusFdbStaticCopyToCpu_Type()
)
cie1000MacStatusFdbStaticCopyToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStaticCopyToCpu.setStatus("current")
_Cie1000MacStatusFdbPortStatisticsTable_Object = MibTable
cie1000MacStatusFdbPortStatisticsTable = _Cie1000MacStatusFdbPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbPortStatisticsTable.setStatus("current")
_Cie1000MacStatusFdbPortStatisticsEntry_Object = MibTableRow
cie1000MacStatusFdbPortStatisticsEntry = _Cie1000MacStatusFdbPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 3, 1)
)
cie1000MacStatusFdbPortStatisticsEntry.setIndexNames(
    (0, "CIE1000-MAC-MIB", "cie1000MacStatusFdbPortStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbPortStatisticsEntry.setStatus("current")
_Cie1000MacStatusFdbPortStatisticsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000MacStatusFdbPortStatisticsIfIndex_Object = MibTableColumn
cie1000MacStatusFdbPortStatisticsIfIndex = _Cie1000MacStatusFdbPortStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 3, 1, 1),
    _Cie1000MacStatusFdbPortStatisticsIfIndex_Type()
)
cie1000MacStatusFdbPortStatisticsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbPortStatisticsIfIndex.setStatus("current")
_Cie1000MacStatusFdbPortStatisticsDynamic_Type = Unsigned32
_Cie1000MacStatusFdbPortStatisticsDynamic_Object = MibTableColumn
cie1000MacStatusFdbPortStatisticsDynamic = _Cie1000MacStatusFdbPortStatisticsDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 3, 1, 2),
    _Cie1000MacStatusFdbPortStatisticsDynamic_Type()
)
cie1000MacStatusFdbPortStatisticsDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbPortStatisticsDynamic.setStatus("current")
_Cie1000MacStatusFdbStatistics_ObjectIdentity = ObjectIdentity
cie1000MacStatusFdbStatistics = _Cie1000MacStatusFdbStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 4)
)
_Cie1000MacStatusFdbStatisticsTotalDynamic_Type = Unsigned32
_Cie1000MacStatusFdbStatisticsTotalDynamic_Object = MibScalar
cie1000MacStatusFdbStatisticsTotalDynamic = _Cie1000MacStatusFdbStatisticsTotalDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 4, 1),
    _Cie1000MacStatusFdbStatisticsTotalDynamic_Type()
)
cie1000MacStatusFdbStatisticsTotalDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStatisticsTotalDynamic.setStatus("current")
_Cie1000MacStatusFdbStatisticsTotalStatic_Type = Unsigned32
_Cie1000MacStatusFdbStatisticsTotalStatic_Object = MibScalar
cie1000MacStatusFdbStatisticsTotalStatic = _Cie1000MacStatusFdbStatisticsTotalStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 3, 4, 2),
    _Cie1000MacStatusFdbStatisticsTotalStatic_Type()
)
cie1000MacStatusFdbStatisticsTotalStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStatisticsTotalStatic.setStatus("current")
_Cie1000MacControl_ObjectIdentity = ObjectIdentity
cie1000MacControl = _Cie1000MacControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 4)
)
_Cie1000MacControlFlushAll_Type = TruthValue
_Cie1000MacControlFlushAll_Object = MibScalar
cie1000MacControlFlushAll = _Cie1000MacControlFlushAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 1, 4, 1),
    _Cie1000MacControlFlushAll_Type()
)
cie1000MacControlFlushAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MacControlFlushAll.setStatus("current")
_Cie1000MacMibConformance_ObjectIdentity = ObjectIdentity
cie1000MacMibConformance = _Cie1000MacMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2)
)
_Cie1000MacMibCompliances_ObjectIdentity = ObjectIdentity
cie1000MacMibCompliances = _Cie1000MacMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 1)
)
_Cie1000MacMibGroups_ObjectIdentity = ObjectIdentity
cie1000MacMibGroups = _Cie1000MacMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2)
)

# Managed Objects groups

cie1000MacCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 1)
)
cie1000MacCapabilitiesInfoGroup.setObjects(
    ("CIE1000-MAC-MIB", "cie1000MacCapabilitiesNonVolatileMax")
)
if mibBuilder.loadTexts:
    cie1000MacCapabilitiesInfoGroup.setStatus("current")

cie1000MacConfigFdbGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 2)
)
cie1000MacConfigFdbGlobalInfoGroup.setObjects(
    ("CIE1000-MAC-MIB", "cie1000MacConfigFdbGlobalAgeTime")
)
if mibBuilder.loadTexts:
    cie1000MacConfigFdbGlobalInfoGroup.setStatus("current")

cie1000MacConfigFdbTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 3)
)
cie1000MacConfigFdbTableInfoGroup.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacConfigFdbVlanId"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbMacAddress"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbPortList"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbAction"))
)
if mibBuilder.loadTexts:
    cie1000MacConfigFdbTableInfoGroup.setStatus("current")

cie1000MacConfigFdbTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 4)
)
cie1000MacConfigFdbTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacConfigFdbTableRowEditorVlanId"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbTableRowEditorMacAddress"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbTableRowEditorPortList"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000MacConfigFdbTableRowEditorInfoGroup.setStatus("current")

cie1000MacConfigPortLearnInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 5)
)
cie1000MacConfigPortLearnInfoGroup.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacConfigPortLearnIfIndex"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigPortLearnLearnMode"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigPortLearnChangeAllowed"))
)
if mibBuilder.loadTexts:
    cie1000MacConfigPortLearnInfoGroup.setStatus("current")

cie1000MacConfigVlanLearnInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 6)
)
cie1000MacConfigVlanLearnInfoGroup.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacConfigVlanLearnVlanId"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigVlanLearnMode"))
)
if mibBuilder.loadTexts:
    cie1000MacConfigVlanLearnInfoGroup.setStatus("current")

cie1000MacStatusFdbTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 7)
)
cie1000MacStatusFdbTableInfoGroup.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacStatusFdbVlanId"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbMacAddress"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbPortList"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbDynamic"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbCopyToCpu"))
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbTableInfoGroup.setStatus("current")

cie1000MacStatusFdbStaticTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 8)
)
cie1000MacStatusFdbStaticTableInfoGroup.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacStatusFdbStaticVlanId"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbStaticMacAddress"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbStaticPortList"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbStaticDynamic"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbStaticCopyToCpu"))
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStaticTableInfoGroup.setStatus("current")

cie1000MacStatusFdbPortStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 9)
)
cie1000MacStatusFdbPortStatisticsInfoGroup.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacStatusFdbPortStatisticsIfIndex"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbPortStatisticsDynamic"))
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbPortStatisticsInfoGroup.setStatus("current")

cie1000MacStatusFdbStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 10)
)
cie1000MacStatusFdbStatisticsInfoGroup.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacStatusFdbStatisticsTotalDynamic"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbStatisticsTotalStatic"))
)
if mibBuilder.loadTexts:
    cie1000MacStatusFdbStatisticsInfoGroup.setStatus("current")

cie1000MacControlInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 2, 11)
)
cie1000MacControlInfoGroup.setObjects(
    ("CIE1000-MAC-MIB", "cie1000MacControlFlushAll")
)
if mibBuilder.loadTexts:
    cie1000MacControlInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000MacMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 12, 2, 1, 1)
)
cie1000MacMibCompliance.setObjects(
      *(("CIE1000-MAC-MIB", "cie1000MacCapabilitiesInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbGlobalInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbTableInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigFdbTableRowEditorInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigPortLearnInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacConfigVlanLearnInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbTableInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbStaticTableInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbPortStatisticsInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacStatusFdbStatisticsInfoGroup"),
        ("CIE1000-MAC-MIB", "cie1000MacControlInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000MacMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-MAC-MIB",
    **{"CIE1000MACPortLearnMode": CIE1000MACPortLearnMode,
       "cie1000MacMib": cie1000MacMib,
       "cie1000MacMibObjects": cie1000MacMibObjects,
       "cie1000MacCapabilities": cie1000MacCapabilities,
       "cie1000MacCapabilitiesNonVolatileMax": cie1000MacCapabilitiesNonVolatileMax,
       "cie1000MacConfig": cie1000MacConfig,
       "cie1000MacConfigFdbGlobal": cie1000MacConfigFdbGlobal,
       "cie1000MacConfigFdbGlobalAgeTime": cie1000MacConfigFdbGlobalAgeTime,
       "cie1000MacConfigFdbTable": cie1000MacConfigFdbTable,
       "cie1000MacConfigFdbEntry": cie1000MacConfigFdbEntry,
       "cie1000MacConfigFdbVlanId": cie1000MacConfigFdbVlanId,
       "cie1000MacConfigFdbMacAddress": cie1000MacConfigFdbMacAddress,
       "cie1000MacConfigFdbPortList": cie1000MacConfigFdbPortList,
       "cie1000MacConfigFdbAction": cie1000MacConfigFdbAction,
       "cie1000MacConfigFdbTableRowEditor": cie1000MacConfigFdbTableRowEditor,
       "cie1000MacConfigFdbTableRowEditorVlanId": cie1000MacConfigFdbTableRowEditorVlanId,
       "cie1000MacConfigFdbTableRowEditorMacAddress": cie1000MacConfigFdbTableRowEditorMacAddress,
       "cie1000MacConfigFdbTableRowEditorPortList": cie1000MacConfigFdbTableRowEditorPortList,
       "cie1000MacConfigFdbTableRowEditorAction": cie1000MacConfigFdbTableRowEditorAction,
       "cie1000MacConfigPortLearnTable": cie1000MacConfigPortLearnTable,
       "cie1000MacConfigPortLearnEntry": cie1000MacConfigPortLearnEntry,
       "cie1000MacConfigPortLearnIfIndex": cie1000MacConfigPortLearnIfIndex,
       "cie1000MacConfigPortLearnLearnMode": cie1000MacConfigPortLearnLearnMode,
       "cie1000MacConfigPortLearnChangeAllowed": cie1000MacConfigPortLearnChangeAllowed,
       "cie1000MacConfigVlanLearnTable": cie1000MacConfigVlanLearnTable,
       "cie1000MacConfigVlanLearnEntry": cie1000MacConfigVlanLearnEntry,
       "cie1000MacConfigVlanLearnVlanId": cie1000MacConfigVlanLearnVlanId,
       "cie1000MacConfigVlanLearnMode": cie1000MacConfigVlanLearnMode,
       "cie1000MacStatus": cie1000MacStatus,
       "cie1000MacStatusFdbTable": cie1000MacStatusFdbTable,
       "cie1000MacStatusFdbEntry": cie1000MacStatusFdbEntry,
       "cie1000MacStatusFdbVlanId": cie1000MacStatusFdbVlanId,
       "cie1000MacStatusFdbMacAddress": cie1000MacStatusFdbMacAddress,
       "cie1000MacStatusFdbPortList": cie1000MacStatusFdbPortList,
       "cie1000MacStatusFdbDynamic": cie1000MacStatusFdbDynamic,
       "cie1000MacStatusFdbCopyToCpu": cie1000MacStatusFdbCopyToCpu,
       "cie1000MacStatusFdbStaticTable": cie1000MacStatusFdbStaticTable,
       "cie1000MacStatusFdbStaticEntry": cie1000MacStatusFdbStaticEntry,
       "cie1000MacStatusFdbStaticVlanId": cie1000MacStatusFdbStaticVlanId,
       "cie1000MacStatusFdbStaticMacAddress": cie1000MacStatusFdbStaticMacAddress,
       "cie1000MacStatusFdbStaticPortList": cie1000MacStatusFdbStaticPortList,
       "cie1000MacStatusFdbStaticDynamic": cie1000MacStatusFdbStaticDynamic,
       "cie1000MacStatusFdbStaticCopyToCpu": cie1000MacStatusFdbStaticCopyToCpu,
       "cie1000MacStatusFdbPortStatisticsTable": cie1000MacStatusFdbPortStatisticsTable,
       "cie1000MacStatusFdbPortStatisticsEntry": cie1000MacStatusFdbPortStatisticsEntry,
       "cie1000MacStatusFdbPortStatisticsIfIndex": cie1000MacStatusFdbPortStatisticsIfIndex,
       "cie1000MacStatusFdbPortStatisticsDynamic": cie1000MacStatusFdbPortStatisticsDynamic,
       "cie1000MacStatusFdbStatistics": cie1000MacStatusFdbStatistics,
       "cie1000MacStatusFdbStatisticsTotalDynamic": cie1000MacStatusFdbStatisticsTotalDynamic,
       "cie1000MacStatusFdbStatisticsTotalStatic": cie1000MacStatusFdbStatisticsTotalStatic,
       "cie1000MacControl": cie1000MacControl,
       "cie1000MacControlFlushAll": cie1000MacControlFlushAll,
       "cie1000MacMibConformance": cie1000MacMibConformance,
       "cie1000MacMibCompliances": cie1000MacMibCompliances,
       "cie1000MacMibCompliance": cie1000MacMibCompliance,
       "cie1000MacMibGroups": cie1000MacMibGroups,
       "cie1000MacCapabilitiesInfoGroup": cie1000MacCapabilitiesInfoGroup,
       "cie1000MacConfigFdbGlobalInfoGroup": cie1000MacConfigFdbGlobalInfoGroup,
       "cie1000MacConfigFdbTableInfoGroup": cie1000MacConfigFdbTableInfoGroup,
       "cie1000MacConfigFdbTableRowEditorInfoGroup": cie1000MacConfigFdbTableRowEditorInfoGroup,
       "cie1000MacConfigPortLearnInfoGroup": cie1000MacConfigPortLearnInfoGroup,
       "cie1000MacConfigVlanLearnInfoGroup": cie1000MacConfigVlanLearnInfoGroup,
       "cie1000MacStatusFdbTableInfoGroup": cie1000MacStatusFdbTableInfoGroup,
       "cie1000MacStatusFdbStaticTableInfoGroup": cie1000MacStatusFdbStaticTableInfoGroup,
       "cie1000MacStatusFdbPortStatisticsInfoGroup": cie1000MacStatusFdbPortStatisticsInfoGroup,
       "cie1000MacStatusFdbStatisticsInfoGroup": cie1000MacStatusFdbStatisticsInfoGroup,
       "cie1000MacControlInfoGroup": cie1000MacControlInfoGroup}
)
