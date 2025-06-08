# SNMP MIB module (F3-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-BRIDGE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:57 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(PerfCounter64,) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "PerfCounter64")

(neIndex,
 networkElementEntry,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "networkElementEntry",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortIndex,
 cmFlowEntry,
 cmFlowIndex,
 cmMPFlowIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortIndex",
    "cmFlowEntry",
    "cmFlowIndex",
    "cmMPFlowIndex")

(cmFlowHistoryEntry,
 cmFlowStatsEntry) = mibBuilder.importSymbols(
    "CM-PERFORMANCE-MIB",
    "cmFlowHistoryEntry",
    "cmFlowStatsEntry")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3BridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26)
)
if mibBuilder.loadTexts:
    f3BridgeMIB.setRevisions(
        ("2012-10-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LearningControl(TextualConvention, Integer32):
    status = "current"
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
          ("macbased", 2),
          ("flowbased", 3))
    )



class ProtectLearningControl(TextualConvention, Integer32):
    status = "current"
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
          ("discard", 2),
          ("block", 3))
    )



class LearningAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2))
    )



class LearningEntryType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )



class FlowLearningConfigAction(TextualConvention, Integer32):
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
        *(("noAction", 1),
          ("flushFwdTable", 2),
          ("clearBlock", 3),
          ("resetAgingTimer", 4))
    )



class RetrieveMacAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApllicable", 0),
          ("retrieveMac", 1))
    )



# MIB Managed Objects in the order of their OIDs

_F3BridgeConfigObjects_ObjectIdentity = ObjectIdentity
f3BridgeConfigObjects = _F3BridgeConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1)
)
_F3FlowLearningConfigTable_Object = MibTable
f3FlowLearningConfigTable = _F3FlowLearningConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1)
)
if mibBuilder.loadTexts:
    f3FlowLearningConfigTable.setStatus("current")
_F3FlowLearningConfigEntry_Object = MibTableRow
f3FlowLearningConfigEntry = _F3FlowLearningConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f3FlowLearningConfigEntry.setStatus("current")
_F3FlowLearningConfigAccIfLearningCtrl_Type = LearningControl
_F3FlowLearningConfigAccIfLearningCtrl_Object = MibTableColumn
f3FlowLearningConfigAccIfLearningCtrl = _F3FlowLearningConfigAccIfLearningCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 1),
    _F3FlowLearningConfigAccIfLearningCtrl_Type()
)
f3FlowLearningConfigAccIfLearningCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigAccIfLearningCtrl.setStatus("current")
_F3FlowLearningConfigNetIfLearningCtrl_Type = LearningControl
_F3FlowLearningConfigNetIfLearningCtrl_Object = MibTableColumn
f3FlowLearningConfigNetIfLearningCtrl = _F3FlowLearningConfigNetIfLearningCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 2),
    _F3FlowLearningConfigNetIfLearningCtrl_Type()
)
f3FlowLearningConfigNetIfLearningCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigNetIfLearningCtrl.setStatus("current")
_F3FlowLearningConfigAccMaxFwdEntries_Type = Integer32
_F3FlowLearningConfigAccMaxFwdEntries_Object = MibTableColumn
f3FlowLearningConfigAccMaxFwdEntries = _F3FlowLearningConfigAccMaxFwdEntries_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 3),
    _F3FlowLearningConfigAccMaxFwdEntries_Type()
)
f3FlowLearningConfigAccMaxFwdEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigAccMaxFwdEntries.setStatus("current")
_F3FlowLearningConfigNetMaxFwdEntries_Type = Integer32
_F3FlowLearningConfigNetMaxFwdEntries_Object = MibTableColumn
f3FlowLearningConfigNetMaxFwdEntries = _F3FlowLearningConfigNetMaxFwdEntries_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 4),
    _F3FlowLearningConfigNetMaxFwdEntries_Type()
)
f3FlowLearningConfigNetMaxFwdEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigNetMaxFwdEntries.setStatus("current")
_F3FlowLearningConfigAccIfProtectLearningCtrl_Type = ProtectLearningControl
_F3FlowLearningConfigAccIfProtectLearningCtrl_Object = MibTableColumn
f3FlowLearningConfigAccIfProtectLearningCtrl = _F3FlowLearningConfigAccIfProtectLearningCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 5),
    _F3FlowLearningConfigAccIfProtectLearningCtrl_Type()
)
f3FlowLearningConfigAccIfProtectLearningCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigAccIfProtectLearningCtrl.setStatus("current")
_F3FlowLearningConfigNetIfProtectLearningCtrl_Type = ProtectLearningControl
_F3FlowLearningConfigNetIfProtectLearningCtrl_Object = MibTableColumn
f3FlowLearningConfigNetIfProtectLearningCtrl = _F3FlowLearningConfigNetIfProtectLearningCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 6),
    _F3FlowLearningConfigNetIfProtectLearningCtrl_Type()
)
f3FlowLearningConfigNetIfProtectLearningCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigNetIfProtectLearningCtrl.setStatus("current")
_F3FlowLearningConfigAgingTimer_Type = Integer32
_F3FlowLearningConfigAgingTimer_Object = MibTableColumn
f3FlowLearningConfigAgingTimer = _F3FlowLearningConfigAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 7),
    _F3FlowLearningConfigAgingTimer_Type()
)
f3FlowLearningConfigAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigAgingTimer.setStatus("current")
_F3FlowLearningConfigTableFullAction_Type = LearningAction
_F3FlowLearningConfigTableFullAction_Object = MibTableColumn
f3FlowLearningConfigTableFullAction = _F3FlowLearningConfigTableFullAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 8),
    _F3FlowLearningConfigTableFullAction_Type()
)
f3FlowLearningConfigTableFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigTableFullAction.setStatus("current")
_F3FlowLearningConfigAction_Type = FlowLearningConfigAction
_F3FlowLearningConfigAction_Object = MibTableColumn
f3FlowLearningConfigAction = _F3FlowLearningConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 1, 1, 9),
    _F3FlowLearningConfigAction_Type()
)
f3FlowLearningConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowLearningConfigAction.setStatus("current")
_F3FlowStaticFwdEntTable_Object = MibTable
f3FlowStaticFwdEntTable = _F3FlowStaticFwdEntTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 2)
)
if mibBuilder.loadTexts:
    f3FlowStaticFwdEntTable.setStatus("current")
_F3FlowStaticFwdEntEntry_Object = MibTableRow
f3FlowStaticFwdEntEntry = _F3FlowStaticFwdEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 2, 1)
)
f3FlowStaticFwdEntEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (1, "F3-BRIDGE-MIB", "f3FlowStaticFwdEntDestMac"),
)
if mibBuilder.loadTexts:
    f3FlowStaticFwdEntEntry.setStatus("current")
_F3FlowStaticFwdEntDestMac_Type = MacAddress
_F3FlowStaticFwdEntDestMac_Object = MibTableColumn
f3FlowStaticFwdEntDestMac = _F3FlowStaticFwdEntDestMac_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 2, 1, 1),
    _F3FlowStaticFwdEntDestMac_Type()
)
f3FlowStaticFwdEntDestMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3FlowStaticFwdEntDestMac.setStatus("current")
_F3FlowStaticFwdEntDestPort_Type = VariablePointer
_F3FlowStaticFwdEntDestPort_Object = MibTableColumn
f3FlowStaticFwdEntDestPort = _F3FlowStaticFwdEntDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 2, 1, 2),
    _F3FlowStaticFwdEntDestPort_Type()
)
f3FlowStaticFwdEntDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3FlowStaticFwdEntDestPort.setStatus("current")
_F3FlowStaticFwdEntAction_Type = LearningAction
_F3FlowStaticFwdEntAction_Object = MibTableColumn
f3FlowStaticFwdEntAction = _F3FlowStaticFwdEntAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 2, 1, 3),
    _F3FlowStaticFwdEntAction_Type()
)
f3FlowStaticFwdEntAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3FlowStaticFwdEntAction.setStatus("current")
_F3FlowStaticFwdEntStorageType_Type = StorageType
_F3FlowStaticFwdEntStorageType_Object = MibTableColumn
f3FlowStaticFwdEntStorageType = _F3FlowStaticFwdEntStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 2, 1, 4),
    _F3FlowStaticFwdEntStorageType_Type()
)
f3FlowStaticFwdEntStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3FlowStaticFwdEntStorageType.setStatus("current")
_F3FlowStaticFwdEntRowStatus_Type = RowStatus
_F3FlowStaticFwdEntRowStatus_Object = MibTableColumn
f3FlowStaticFwdEntRowStatus = _F3FlowStaticFwdEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 2, 1, 5),
    _F3FlowStaticFwdEntRowStatus_Type()
)
f3FlowStaticFwdEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3FlowStaticFwdEntRowStatus.setStatus("current")
_F3FlowStaticFwdValid_Type = TruthValue
_F3FlowStaticFwdValid_Object = MibTableColumn
f3FlowStaticFwdValid = _F3FlowStaticFwdValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 2, 1, 6),
    _F3FlowStaticFwdValid_Type()
)
f3FlowStaticFwdValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowStaticFwdValid.setStatus("current")
_F3FlowFdbTable_Object = MibTable
f3FlowFdbTable = _F3FlowFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 3)
)
if mibBuilder.loadTexts:
    f3FlowFdbTable.setStatus("current")
_F3FlowFdbEntry_Object = MibTableRow
f3FlowFdbEntry = _F3FlowFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 3, 1)
)
f3FlowFdbEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (1, "F3-BRIDGE-MIB", "f3FlowFdbDestMac"),
)
if mibBuilder.loadTexts:
    f3FlowFdbEntry.setStatus("current")
_F3FlowFdbDestMac_Type = MacAddress
_F3FlowFdbDestMac_Object = MibTableColumn
f3FlowFdbDestMac = _F3FlowFdbDestMac_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 3, 1, 1),
    _F3FlowFdbDestMac_Type()
)
f3FlowFdbDestMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3FlowFdbDestMac.setStatus("current")
_F3FlowFdbDestPort_Type = VariablePointer
_F3FlowFdbDestPort_Object = MibTableColumn
f3FlowFdbDestPort = _F3FlowFdbDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 3, 1, 2),
    _F3FlowFdbDestPort_Type()
)
f3FlowFdbDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowFdbDestPort.setStatus("current")
_F3FlowFdbAction_Type = LearningAction
_F3FlowFdbAction_Object = MibTableColumn
f3FlowFdbAction = _F3FlowFdbAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 3, 1, 3),
    _F3FlowFdbAction_Type()
)
f3FlowFdbAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowFdbAction.setStatus("current")
_F3FlowFdbEntryType_Type = LearningEntryType
_F3FlowFdbEntryType_Object = MibTableColumn
f3FlowFdbEntryType = _F3FlowFdbEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 3, 1, 4),
    _F3FlowFdbEntryType_Type()
)
f3FlowFdbEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowFdbEntryType.setStatus("current")
_F3MPFlowStaticFwdTable_Object = MibTable
f3MPFlowStaticFwdTable = _F3MPFlowStaticFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 4)
)
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdTable.setStatus("current")
_F3MPFlowStaticFwdEntry_Object = MibTableRow
f3MPFlowStaticFwdEntry = _F3MPFlowStaticFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 4, 1)
)
f3MPFlowStaticFwdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-FACILITY-MIB", "cmMPFlowIndex"),
    (0, "F3-BRIDGE-MIB", "f3MPFlowStaticFwdMacAddress"),
)
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdEntry.setStatus("current")
_F3MPFlowStaticFwdMacAddress_Type = MacAddress
_F3MPFlowStaticFwdMacAddress_Object = MibTableColumn
f3MPFlowStaticFwdMacAddress = _F3MPFlowStaticFwdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 4, 1, 1),
    _F3MPFlowStaticFwdMacAddress_Type()
)
f3MPFlowStaticFwdMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdMacAddress.setStatus("current")
_F3MPFlowStaticFwdFP_Type = VariablePointer
_F3MPFlowStaticFwdFP_Object = MibTableColumn
f3MPFlowStaticFwdFP = _F3MPFlowStaticFwdFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 4, 1, 2),
    _F3MPFlowStaticFwdFP_Type()
)
f3MPFlowStaticFwdFP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdFP.setStatus("current")
_F3MPFlowStaticFwdControlAction_Type = LearningAction
_F3MPFlowStaticFwdControlAction_Object = MibTableColumn
f3MPFlowStaticFwdControlAction = _F3MPFlowStaticFwdControlAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 4, 1, 3),
    _F3MPFlowStaticFwdControlAction_Type()
)
f3MPFlowStaticFwdControlAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdControlAction.setStatus("current")
_F3MPFlowStaticFwdValid_Type = TruthValue
_F3MPFlowStaticFwdValid_Object = MibTableColumn
f3MPFlowStaticFwdValid = _F3MPFlowStaticFwdValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 4, 1, 4),
    _F3MPFlowStaticFwdValid_Type()
)
f3MPFlowStaticFwdValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdValid.setStatus("current")
_F3MPFlowStaticFwdStorageType_Type = StorageType
_F3MPFlowStaticFwdStorageType_Object = MibTableColumn
f3MPFlowStaticFwdStorageType = _F3MPFlowStaticFwdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 4, 1, 5),
    _F3MPFlowStaticFwdStorageType_Type()
)
f3MPFlowStaticFwdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdStorageType.setStatus("current")
_F3MPFlowStaticFwdRowStatus_Type = RowStatus
_F3MPFlowStaticFwdRowStatus_Object = MibTableColumn
f3MPFlowStaticFwdRowStatus = _F3MPFlowStaticFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 4, 1, 6),
    _F3MPFlowStaticFwdRowStatus_Type()
)
f3MPFlowStaticFwdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdRowStatus.setStatus("current")
_F3MPFlowFDBTable_Object = MibTable
f3MPFlowFDBTable = _F3MPFlowFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 5)
)
if mibBuilder.loadTexts:
    f3MPFlowFDBTable.setStatus("current")
_F3MPFlowFDBEntry_Object = MibTableRow
f3MPFlowFDBEntry = _F3MPFlowFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 5, 1)
)
f3MPFlowFDBEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-FACILITY-MIB", "cmMPFlowIndex"),
    (0, "F3-BRIDGE-MIB", "f3MPFlowFDBMacAddress"),
)
if mibBuilder.loadTexts:
    f3MPFlowFDBEntry.setStatus("current")
_F3MPFlowFDBMacAddress_Type = MacAddress
_F3MPFlowFDBMacAddress_Object = MibTableColumn
f3MPFlowFDBMacAddress = _F3MPFlowFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 5, 1, 1),
    _F3MPFlowFDBMacAddress_Type()
)
f3MPFlowFDBMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MPFlowFDBMacAddress.setStatus("current")
_F3MPFlowFDBFP_Type = VariablePointer
_F3MPFlowFDBFP_Object = MibTableColumn
f3MPFlowFDBFP = _F3MPFlowFDBFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 5, 1, 2),
    _F3MPFlowFDBFP_Type()
)
f3MPFlowFDBFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowFDBFP.setStatus("current")
_F3MPFlowFDBType_Type = LearningEntryType
_F3MPFlowFDBType_Object = MibTableColumn
f3MPFlowFDBType = _F3MPFlowFDBType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 5, 1, 3),
    _F3MPFlowFDBType_Type()
)
f3MPFlowFDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowFDBType.setStatus("current")
_F3MPFlowFDBControlAction_Type = LearningAction
_F3MPFlowFDBControlAction_Object = MibTableColumn
f3MPFlowFDBControlAction = _F3MPFlowFDBControlAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 5, 1, 4),
    _F3MPFlowFDBControlAction_Type()
)
f3MPFlowFDBControlAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MPFlowFDBControlAction.setStatus("current")
_F3FwdTSizeProfileTable_Object = MibTable
f3FwdTSizeProfileTable = _F3FwdTSizeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 6)
)
if mibBuilder.loadTexts:
    f3FwdTSizeProfileTable.setStatus("current")
_F3FwdTSizeProfileEntry_Object = MibTableRow
f3FwdTSizeProfileEntry = _F3FwdTSizeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 6, 1)
)
f3FwdTSizeProfileEntry.setIndexNames(
    (0, "F3-BRIDGE-MIB", "f3FwdTSizeProfileIndex"),
)
if mibBuilder.loadTexts:
    f3FwdTSizeProfileEntry.setStatus("current")
_F3FwdTSizeProfileIndex_Type = Integer32
_F3FwdTSizeProfileIndex_Object = MibTableColumn
f3FwdTSizeProfileIndex = _F3FwdTSizeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 6, 1, 1),
    _F3FwdTSizeProfileIndex_Type()
)
f3FwdTSizeProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3FwdTSizeProfileIndex.setStatus("current")
_F3FwdTSizeProfileName_Type = DisplayString
_F3FwdTSizeProfileName_Object = MibTableColumn
f3FwdTSizeProfileName = _F3FwdTSizeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 6, 1, 2),
    _F3FwdTSizeProfileName_Type()
)
f3FwdTSizeProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FwdTSizeProfileName.setStatus("current")
_F3FwdTSizeProfileTableSize_Type = Integer32
_F3FwdTSizeProfileTableSize_Object = MibTableColumn
f3FwdTSizeProfileTableSize = _F3FwdTSizeProfileTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 6, 1, 3),
    _F3FwdTSizeProfileTableSize_Type()
)
f3FwdTSizeProfileTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FwdTSizeProfileTableSize.setStatus("current")
_F3MultiGroupRegistrationTable_Object = MibTable
f3MultiGroupRegistrationTable = _F3MultiGroupRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7)
)
if mibBuilder.loadTexts:
    f3MultiGroupRegistrationTable.setStatus("current")
_F3MultiGroupRegistrationEntry_Object = MibTableRow
f3MultiGroupRegistrationEntry = _F3MultiGroupRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7, 1)
)
f3MultiGroupRegistrationEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-FACILITY-MIB", "cmMPFlowIndex"),
    (0, "F3-BRIDGE-MIB", "f3MGRMulticastAddress"),
)
if mibBuilder.loadTexts:
    f3MultiGroupRegistrationEntry.setStatus("current")
_F3MGRMulticastAddress_Type = MacAddress
_F3MGRMulticastAddress_Object = MibTableColumn
f3MGRMulticastAddress = _F3MGRMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7, 1, 1),
    _F3MGRMulticastAddress_Type()
)
f3MGRMulticastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MGRMulticastAddress.setStatus("current")
_F3MGRFPList_Type = DisplayString
_F3MGRFPList_Object = MibTableColumn
f3MGRFPList = _F3MGRFPList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7, 1, 2),
    _F3MGRFPList_Type()
)
f3MGRFPList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MGRFPList.setStatus("current")
_F3MGRGroupAction_Type = LearningAction
_F3MGRGroupAction_Object = MibTableColumn
f3MGRGroupAction = _F3MGRGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7, 1, 3),
    _F3MGRGroupAction_Type()
)
f3MGRGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MGRGroupAction.setStatus("current")
_F3MGRGroupType_Type = LearningEntryType
_F3MGRGroupType_Object = MibTableColumn
f3MGRGroupType = _F3MGRGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7, 1, 4),
    _F3MGRGroupType_Type()
)
f3MGRGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MGRGroupType.setStatus("current")
_F3MGRGroupValid_Type = TruthValue
_F3MGRGroupValid_Object = MibTableColumn
f3MGRGroupValid = _F3MGRGroupValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7, 1, 5),
    _F3MGRGroupValid_Type()
)
f3MGRGroupValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MGRGroupValid.setStatus("current")
_F3MGRGroupStorageType_Type = StorageType
_F3MGRGroupStorageType_Object = MibTableColumn
f3MGRGroupStorageType = _F3MGRGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7, 1, 6),
    _F3MGRGroupStorageType_Type()
)
f3MGRGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MGRGroupStorageType.setStatus("current")
_F3MGRGroupRowStatus_Type = RowStatus
_F3MGRGroupRowStatus_Object = MibTableColumn
f3MGRGroupRowStatus = _F3MGRGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 7, 1, 7),
    _F3MGRGroupRowStatus_Type()
)
f3MGRGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MGRGroupRowStatus.setStatus("current")
_F3MGRFPMemberTable_Object = MibTable
f3MGRFPMemberTable = _F3MGRFPMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 8)
)
if mibBuilder.loadTexts:
    f3MGRFPMemberTable.setStatus("current")
_F3MGRFPMemberEntry_Object = MibTableRow
f3MGRFPMemberEntry = _F3MGRFPMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 8, 1)
)
f3MGRFPMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-FACILITY-MIB", "cmMPFlowIndex"),
    (0, "F3-BRIDGE-MIB", "f3MGRMulticastAddress"),
    (0, "F3-BRIDGE-MIB", "f3MGRFPIndex"),
)
if mibBuilder.loadTexts:
    f3MGRFPMemberEntry.setStatus("current")
_F3MGRFPIndex_Type = VariablePointer
_F3MGRFPIndex_Object = MibTableColumn
f3MGRFPIndex = _F3MGRFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 8, 1, 1),
    _F3MGRFPIndex_Type()
)
f3MGRFPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MGRFPIndex.setStatus("current")
_F3MGRFPIndexRowStatus_Type = RowStatus
_F3MGRFPIndexRowStatus_Object = MibTableColumn
f3MGRFPIndexRowStatus = _F3MGRFPIndexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 8, 1, 2),
    _F3MGRFPIndexRowStatus_Type()
)
f3MGRFPIndexRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MGRFPIndexRowStatus.setStatus("current")
_NetworkElementBridgeParamsTable_Object = MibTable
networkElementBridgeParamsTable = _NetworkElementBridgeParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 9)
)
if mibBuilder.loadTexts:
    networkElementBridgeParamsTable.setStatus("current")
_NetworkElementBridgeParamsEntry_Object = MibTableRow
networkElementBridgeParamsEntry = _NetworkElementBridgeParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 9, 1)
)
if mibBuilder.loadTexts:
    networkElementBridgeParamsEntry.setStatus("current")
_NeBridgeParamsRtrvMacAction_Type = RetrieveMacAction
_NeBridgeParamsRtrvMacAction_Object = MibTableColumn
neBridgeParamsRtrvMacAction = _NeBridgeParamsRtrvMacAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 1, 9, 1, 1),
    _NeBridgeParamsRtrvMacAction_Type()
)
neBridgeParamsRtrvMacAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neBridgeParamsRtrvMacAction.setStatus("current")
_F3BridgeStatsObjects_ObjectIdentity = ObjectIdentity
f3BridgeStatsObjects = _F3BridgeStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2)
)
_F3FlowLearningStatsTable_Object = MibTable
f3FlowLearningStatsTable = _F3FlowLearningStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 1)
)
if mibBuilder.loadTexts:
    f3FlowLearningStatsTable.setStatus("current")
_F3FlowLearningStatsEntry_Object = MibTableRow
f3FlowLearningStatsEntry = _F3FlowLearningStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f3FlowLearningStatsEntry.setStatus("current")
_F3FlowLearningStatsMacTableFlushes_Type = PerfCounter64
_F3FlowLearningStatsMacTableFlushes_Object = MibTableColumn
f3FlowLearningStatsMacTableFlushes = _F3FlowLearningStatsMacTableFlushes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 1, 1, 1),
    _F3FlowLearningStatsMacTableFlushes_Type()
)
f3FlowLearningStatsMacTableFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningStatsMacTableFlushes.setStatus("current")
_F3FlowLearningStatsFDStaticBlock_Type = PerfCounter64
_F3FlowLearningStatsFDStaticBlock_Object = MibTableColumn
f3FlowLearningStatsFDStaticBlock = _F3FlowLearningStatsFDStaticBlock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 1, 1, 2),
    _F3FlowLearningStatsFDStaticBlock_Type()
)
f3FlowLearningStatsFDStaticBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningStatsFDStaticBlock.setStatus("current")
_F3FlowLearningStatsFDHairPin_Type = PerfCounter64
_F3FlowLearningStatsFDHairPin_Object = MibTableColumn
f3FlowLearningStatsFDHairPin = _F3FlowLearningStatsFDHairPin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 1, 1, 3),
    _F3FlowLearningStatsFDHairPin_Type()
)
f3FlowLearningStatsFDHairPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningStatsFDHairPin.setStatus("current")
_F3FlowLearningStatsFDNoDest_Type = PerfCounter64
_F3FlowLearningStatsFDNoDest_Object = MibTableColumn
f3FlowLearningStatsFDNoDest = _F3FlowLearningStatsFDNoDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 1, 1, 4),
    _F3FlowLearningStatsFDNoDest_Type()
)
f3FlowLearningStatsFDNoDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningStatsFDNoDest.setStatus("current")
_F3FlowLearningStatsMacTableDiscards_Type = PerfCounter64
_F3FlowLearningStatsMacTableDiscards_Object = MibTableColumn
f3FlowLearningStatsMacTableDiscards = _F3FlowLearningStatsMacTableDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 1, 1, 5),
    _F3FlowLearningStatsMacTableDiscards_Type()
)
f3FlowLearningStatsMacTableDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningStatsMacTableDiscards.setStatus("current")
_F3FlowLearningHistoryTable_Object = MibTable
f3FlowLearningHistoryTable = _F3FlowLearningHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 2)
)
if mibBuilder.loadTexts:
    f3FlowLearningHistoryTable.setStatus("current")
_F3FlowLearningHistoryEntry_Object = MibTableRow
f3FlowLearningHistoryEntry = _F3FlowLearningHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 2, 1)
)
if mibBuilder.loadTexts:
    f3FlowLearningHistoryEntry.setStatus("current")
_F3FlowLearningHistoryMacTableFlushes_Type = PerfCounter64
_F3FlowLearningHistoryMacTableFlushes_Object = MibTableColumn
f3FlowLearningHistoryMacTableFlushes = _F3FlowLearningHistoryMacTableFlushes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 2, 1, 1),
    _F3FlowLearningHistoryMacTableFlushes_Type()
)
f3FlowLearningHistoryMacTableFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningHistoryMacTableFlushes.setStatus("current")
_F3FlowLearningHistoryFDStaticBlock_Type = PerfCounter64
_F3FlowLearningHistoryFDStaticBlock_Object = MibTableColumn
f3FlowLearningHistoryFDStaticBlock = _F3FlowLearningHistoryFDStaticBlock_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 2, 1, 2),
    _F3FlowLearningHistoryFDStaticBlock_Type()
)
f3FlowLearningHistoryFDStaticBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningHistoryFDStaticBlock.setStatus("current")
_F3FlowLearningHistoryFDHairPin_Type = PerfCounter64
_F3FlowLearningHistoryFDHairPin_Object = MibTableColumn
f3FlowLearningHistoryFDHairPin = _F3FlowLearningHistoryFDHairPin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 2, 1, 3),
    _F3FlowLearningHistoryFDHairPin_Type()
)
f3FlowLearningHistoryFDHairPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningHistoryFDHairPin.setStatus("current")
_F3FlowLearningHistoryFDNoDest_Type = PerfCounter64
_F3FlowLearningHistoryFDNoDest_Object = MibTableColumn
f3FlowLearningHistoryFDNoDest = _F3FlowLearningHistoryFDNoDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 2, 1, 4),
    _F3FlowLearningHistoryFDNoDest_Type()
)
f3FlowLearningHistoryFDNoDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningHistoryFDNoDest.setStatus("current")
_F3FlowLearningHistoryMacTableDiscards_Type = PerfCounter64
_F3FlowLearningHistoryMacTableDiscards_Object = MibTableColumn
f3FlowLearningHistoryMacTableDiscards = _F3FlowLearningHistoryMacTableDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 2, 2, 1, 5),
    _F3FlowLearningHistoryMacTableDiscards_Type()
)
f3FlowLearningHistoryMacTableDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowLearningHistoryMacTableDiscards.setStatus("current")
_F3BridgeConformance_ObjectIdentity = ObjectIdentity
f3BridgeConformance = _F3BridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3)
)
_F3BridgeCompliances_ObjectIdentity = ObjectIdentity
f3BridgeCompliances = _F3BridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 1)
)
_F3BridgeGroups_ObjectIdentity = ObjectIdentity
f3BridgeGroups = _F3BridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2)
)
cmFlowEntry.registerAugmentions(
    ("F3-BRIDGE-MIB",
     "f3FlowLearningConfigEntry")
)
f3FlowLearningConfigEntry.setIndexNames(*cmFlowEntry.getIndexNames())
networkElementEntry.registerAugmentions(
    ("F3-BRIDGE-MIB",
     "networkElementBridgeParamsEntry")
)
networkElementBridgeParamsEntry.setIndexNames(*networkElementEntry.getIndexNames())
cmFlowStatsEntry.registerAugmentions(
    ("F3-BRIDGE-MIB",
     "f3FlowLearningStatsEntry")
)
f3FlowLearningStatsEntry.setIndexNames(*cmFlowStatsEntry.getIndexNames())
cmFlowHistoryEntry.registerAugmentions(
    ("F3-BRIDGE-MIB",
     "f3FlowLearningHistoryEntry")
)
f3FlowLearningHistoryEntry.setIndexNames(*cmFlowHistoryEntry.getIndexNames())

# Managed Objects groups

f3FlowLearningConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 1)
)
f3FlowLearningConfigGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3FlowLearningConfigAccIfLearningCtrl"),
        ("F3-BRIDGE-MIB", "f3FlowLearningConfigNetIfLearningCtrl"),
        ("F3-BRIDGE-MIB", "f3FlowLearningConfigAccMaxFwdEntries"),
        ("F3-BRIDGE-MIB", "f3FlowLearningConfigNetMaxFwdEntries"),
        ("F3-BRIDGE-MIB", "f3FlowLearningConfigAccIfProtectLearningCtrl"),
        ("F3-BRIDGE-MIB", "f3FlowLearningConfigNetIfProtectLearningCtrl"),
        ("F3-BRIDGE-MIB", "f3FlowLearningConfigAgingTimer"),
        ("F3-BRIDGE-MIB", "f3FlowLearningConfigTableFullAction"),
        ("F3-BRIDGE-MIB", "f3FlowLearningConfigAction"))
)
if mibBuilder.loadTexts:
    f3FlowLearningConfigGroup.setStatus("current")

f3FlowStaticFwdEntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 2)
)
f3FlowStaticFwdEntGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3FlowStaticFwdEntDestPort"),
        ("F3-BRIDGE-MIB", "f3FlowStaticFwdEntAction"),
        ("F3-BRIDGE-MIB", "f3FlowStaticFwdEntStorageType"),
        ("F3-BRIDGE-MIB", "f3FlowStaticFwdEntRowStatus"),
        ("F3-BRIDGE-MIB", "f3FlowStaticFwdValid"))
)
if mibBuilder.loadTexts:
    f3FlowStaticFwdEntGroup.setStatus("current")

f3FlowLearningStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 3)
)
f3FlowLearningStatsGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3FlowLearningStatsMacTableFlushes"),
        ("F3-BRIDGE-MIB", "f3FlowLearningStatsFDStaticBlock"),
        ("F3-BRIDGE-MIB", "f3FlowLearningStatsFDHairPin"),
        ("F3-BRIDGE-MIB", "f3FlowLearningStatsFDNoDest"),
        ("F3-BRIDGE-MIB", "f3FlowLearningStatsMacTableDiscards"))
)
if mibBuilder.loadTexts:
    f3FlowLearningStatsGroup.setStatus("current")

f3FlowLearningHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 4)
)
f3FlowLearningHistoryGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3FlowLearningHistoryMacTableFlushes"),
        ("F3-BRIDGE-MIB", "f3FlowLearningHistoryFDStaticBlock"),
        ("F3-BRIDGE-MIB", "f3FlowLearningHistoryFDHairPin"),
        ("F3-BRIDGE-MIB", "f3FlowLearningHistoryFDNoDest"),
        ("F3-BRIDGE-MIB", "f3FlowLearningHistoryMacTableDiscards"))
)
if mibBuilder.loadTexts:
    f3FlowLearningHistoryGroup.setStatus("current")

f3FlowFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 5)
)
f3FlowFdbGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3FlowFdbDestPort"),
        ("F3-BRIDGE-MIB", "f3FlowFdbAction"),
        ("F3-BRIDGE-MIB", "f3FlowFdbEntryType"))
)
if mibBuilder.loadTexts:
    f3FlowFdbGroup.setStatus("current")

f3MPFlowStaticFwdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 6)
)
f3MPFlowStaticFwdGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3MPFlowStaticFwdMacAddress"),
        ("F3-BRIDGE-MIB", "f3MPFlowStaticFwdFP"),
        ("F3-BRIDGE-MIB", "f3MPFlowStaticFwdControlAction"),
        ("F3-BRIDGE-MIB", "f3MPFlowStaticFwdValid"),
        ("F3-BRIDGE-MIB", "f3MPFlowStaticFwdStorageType"),
        ("F3-BRIDGE-MIB", "f3MPFlowStaticFwdRowStatus"))
)
if mibBuilder.loadTexts:
    f3MPFlowStaticFwdGroup.setStatus("current")

f3MPFlowFDBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 7)
)
f3MPFlowFDBGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3MPFlowFDBMacAddress"),
        ("F3-BRIDGE-MIB", "f3MPFlowFDBFP"),
        ("F3-BRIDGE-MIB", "f3MPFlowFDBType"),
        ("F3-BRIDGE-MIB", "f3MPFlowFDBControlAction"))
)
if mibBuilder.loadTexts:
    f3MPFlowFDBGroup.setStatus("current")

f3FwdTSizeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 8)
)
f3FwdTSizeProfileGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3FwdTSizeProfileIndex"),
        ("F3-BRIDGE-MIB", "f3FwdTSizeProfileName"),
        ("F3-BRIDGE-MIB", "f3FwdTSizeProfileTableSize"))
)
if mibBuilder.loadTexts:
    f3FwdTSizeProfileGroup.setStatus("current")

f3MGGroupFPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 9)
)
f3MGGroupFPGroup.setObjects(
      *(("F3-BRIDGE-MIB", "f3MGRMulticastAddress"),
        ("F3-BRIDGE-MIB", "f3MGRFPList"),
        ("F3-BRIDGE-MIB", "f3MGRGroupAction"),
        ("F3-BRIDGE-MIB", "f3MGRGroupType"),
        ("F3-BRIDGE-MIB", "f3MGRGroupValid"),
        ("F3-BRIDGE-MIB", "f3MGRGroupRowStatus"),
        ("F3-BRIDGE-MIB", "f3MGRFPIndex"),
        ("F3-BRIDGE-MIB", "f3MGRFPIndexRowStatus"),
        ("F3-BRIDGE-MIB", "f3MGRGroupStorageType"))
)
if mibBuilder.loadTexts:
    f3MGGroupFPGroup.setStatus("current")

f3NetworkElementBridgeParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 2, 10)
)
f3NetworkElementBridgeParamsGroup.setObjects(
    ("F3-BRIDGE-MIB", "neBridgeParamsRtrvMacAction")
)
if mibBuilder.loadTexts:
    f3NetworkElementBridgeParamsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3BridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 26, 3, 1, 1)
)
f3BridgeCompliance.setObjects(
      *(("F3-BRIDGE-MIB", "f3FlowLearningConfigGroup"),
        ("F3-BRIDGE-MIB", "f3FlowStaticFwdEntGroup"),
        ("F3-BRIDGE-MIB", "f3FlowLearningStatsGroup"),
        ("F3-BRIDGE-MIB", "f3FlowLearningHistoryGroup"),
        ("F3-BRIDGE-MIB", "f3FlowFdbGroup"),
        ("F3-BRIDGE-MIB", "f3MPFlowStaticFwdGroup"),
        ("F3-BRIDGE-MIB", "f3MPFlowFDBGroup"),
        ("F3-BRIDGE-MIB", "f3FwdTSizeProfileGroup"),
        ("F3-BRIDGE-MIB", "f3MGGroupFPGroup"),
        ("F3-BRIDGE-MIB", "f3NetworkElementBridgeParamsGroup"))
)
if mibBuilder.loadTexts:
    f3BridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-BRIDGE-MIB",
    **{"LearningControl": LearningControl,
       "ProtectLearningControl": ProtectLearningControl,
       "LearningAction": LearningAction,
       "LearningEntryType": LearningEntryType,
       "FlowLearningConfigAction": FlowLearningConfigAction,
       "RetrieveMacAction": RetrieveMacAction,
       "f3BridgeMIB": f3BridgeMIB,
       "f3BridgeConfigObjects": f3BridgeConfigObjects,
       "f3FlowLearningConfigTable": f3FlowLearningConfigTable,
       "f3FlowLearningConfigEntry": f3FlowLearningConfigEntry,
       "f3FlowLearningConfigAccIfLearningCtrl": f3FlowLearningConfigAccIfLearningCtrl,
       "f3FlowLearningConfigNetIfLearningCtrl": f3FlowLearningConfigNetIfLearningCtrl,
       "f3FlowLearningConfigAccMaxFwdEntries": f3FlowLearningConfigAccMaxFwdEntries,
       "f3FlowLearningConfigNetMaxFwdEntries": f3FlowLearningConfigNetMaxFwdEntries,
       "f3FlowLearningConfigAccIfProtectLearningCtrl": f3FlowLearningConfigAccIfProtectLearningCtrl,
       "f3FlowLearningConfigNetIfProtectLearningCtrl": f3FlowLearningConfigNetIfProtectLearningCtrl,
       "f3FlowLearningConfigAgingTimer": f3FlowLearningConfigAgingTimer,
       "f3FlowLearningConfigTableFullAction": f3FlowLearningConfigTableFullAction,
       "f3FlowLearningConfigAction": f3FlowLearningConfigAction,
       "f3FlowStaticFwdEntTable": f3FlowStaticFwdEntTable,
       "f3FlowStaticFwdEntEntry": f3FlowStaticFwdEntEntry,
       "f3FlowStaticFwdEntDestMac": f3FlowStaticFwdEntDestMac,
       "f3FlowStaticFwdEntDestPort": f3FlowStaticFwdEntDestPort,
       "f3FlowStaticFwdEntAction": f3FlowStaticFwdEntAction,
       "f3FlowStaticFwdEntStorageType": f3FlowStaticFwdEntStorageType,
       "f3FlowStaticFwdEntRowStatus": f3FlowStaticFwdEntRowStatus,
       "f3FlowStaticFwdValid": f3FlowStaticFwdValid,
       "f3FlowFdbTable": f3FlowFdbTable,
       "f3FlowFdbEntry": f3FlowFdbEntry,
       "f3FlowFdbDestMac": f3FlowFdbDestMac,
       "f3FlowFdbDestPort": f3FlowFdbDestPort,
       "f3FlowFdbAction": f3FlowFdbAction,
       "f3FlowFdbEntryType": f3FlowFdbEntryType,
       "f3MPFlowStaticFwdTable": f3MPFlowStaticFwdTable,
       "f3MPFlowStaticFwdEntry": f3MPFlowStaticFwdEntry,
       "f3MPFlowStaticFwdMacAddress": f3MPFlowStaticFwdMacAddress,
       "f3MPFlowStaticFwdFP": f3MPFlowStaticFwdFP,
       "f3MPFlowStaticFwdControlAction": f3MPFlowStaticFwdControlAction,
       "f3MPFlowStaticFwdValid": f3MPFlowStaticFwdValid,
       "f3MPFlowStaticFwdStorageType": f3MPFlowStaticFwdStorageType,
       "f3MPFlowStaticFwdRowStatus": f3MPFlowStaticFwdRowStatus,
       "f3MPFlowFDBTable": f3MPFlowFDBTable,
       "f3MPFlowFDBEntry": f3MPFlowFDBEntry,
       "f3MPFlowFDBMacAddress": f3MPFlowFDBMacAddress,
       "f3MPFlowFDBFP": f3MPFlowFDBFP,
       "f3MPFlowFDBType": f3MPFlowFDBType,
       "f3MPFlowFDBControlAction": f3MPFlowFDBControlAction,
       "f3FwdTSizeProfileTable": f3FwdTSizeProfileTable,
       "f3FwdTSizeProfileEntry": f3FwdTSizeProfileEntry,
       "f3FwdTSizeProfileIndex": f3FwdTSizeProfileIndex,
       "f3FwdTSizeProfileName": f3FwdTSizeProfileName,
       "f3FwdTSizeProfileTableSize": f3FwdTSizeProfileTableSize,
       "f3MultiGroupRegistrationTable": f3MultiGroupRegistrationTable,
       "f3MultiGroupRegistrationEntry": f3MultiGroupRegistrationEntry,
       "f3MGRMulticastAddress": f3MGRMulticastAddress,
       "f3MGRFPList": f3MGRFPList,
       "f3MGRGroupAction": f3MGRGroupAction,
       "f3MGRGroupType": f3MGRGroupType,
       "f3MGRGroupValid": f3MGRGroupValid,
       "f3MGRGroupStorageType": f3MGRGroupStorageType,
       "f3MGRGroupRowStatus": f3MGRGroupRowStatus,
       "f3MGRFPMemberTable": f3MGRFPMemberTable,
       "f3MGRFPMemberEntry": f3MGRFPMemberEntry,
       "f3MGRFPIndex": f3MGRFPIndex,
       "f3MGRFPIndexRowStatus": f3MGRFPIndexRowStatus,
       "networkElementBridgeParamsTable": networkElementBridgeParamsTable,
       "networkElementBridgeParamsEntry": networkElementBridgeParamsEntry,
       "neBridgeParamsRtrvMacAction": neBridgeParamsRtrvMacAction,
       "f3BridgeStatsObjects": f3BridgeStatsObjects,
       "f3FlowLearningStatsTable": f3FlowLearningStatsTable,
       "f3FlowLearningStatsEntry": f3FlowLearningStatsEntry,
       "f3FlowLearningStatsMacTableFlushes": f3FlowLearningStatsMacTableFlushes,
       "f3FlowLearningStatsFDStaticBlock": f3FlowLearningStatsFDStaticBlock,
       "f3FlowLearningStatsFDHairPin": f3FlowLearningStatsFDHairPin,
       "f3FlowLearningStatsFDNoDest": f3FlowLearningStatsFDNoDest,
       "f3FlowLearningStatsMacTableDiscards": f3FlowLearningStatsMacTableDiscards,
       "f3FlowLearningHistoryTable": f3FlowLearningHistoryTable,
       "f3FlowLearningHistoryEntry": f3FlowLearningHistoryEntry,
       "f3FlowLearningHistoryMacTableFlushes": f3FlowLearningHistoryMacTableFlushes,
       "f3FlowLearningHistoryFDStaticBlock": f3FlowLearningHistoryFDStaticBlock,
       "f3FlowLearningHistoryFDHairPin": f3FlowLearningHistoryFDHairPin,
       "f3FlowLearningHistoryFDNoDest": f3FlowLearningHistoryFDNoDest,
       "f3FlowLearningHistoryMacTableDiscards": f3FlowLearningHistoryMacTableDiscards,
       "f3BridgeConformance": f3BridgeConformance,
       "f3BridgeCompliances": f3BridgeCompliances,
       "f3BridgeCompliance": f3BridgeCompliance,
       "f3BridgeGroups": f3BridgeGroups,
       "f3FlowLearningConfigGroup": f3FlowLearningConfigGroup,
       "f3FlowStaticFwdEntGroup": f3FlowStaticFwdEntGroup,
       "f3FlowLearningStatsGroup": f3FlowLearningStatsGroup,
       "f3FlowLearningHistoryGroup": f3FlowLearningHistoryGroup,
       "f3FlowFdbGroup": f3FlowFdbGroup,
       "f3MPFlowStaticFwdGroup": f3MPFlowStaticFwdGroup,
       "f3MPFlowFDBGroup": f3MPFlowFDBGroup,
       "f3FwdTSizeProfileGroup": f3FwdTSizeProfileGroup,
       "f3MGGroupFPGroup": f3MGGroupFPGroup,
       "f3NetworkElementBridgeParamsGroup": f3NetworkElementBridgeParamsGroup}
)
