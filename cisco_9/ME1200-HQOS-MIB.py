# SNMP MIB module (ME1200-HQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-HQOS-MIB.mib
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
 ME1200RowEditorState,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState",
    "ME1200Unsigned8")

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

me1200HqosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125)
)
if mibBuilder.loadTexts:
    me1200HqosMib.setRevisions(
        ("2015-01-09 00:00",
         "2014-04-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200hqosSchMode(TextualConvention, Integer32):
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
        *(("normal", 0),
          ("basic", 1),
          ("hierarchical", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200HqosMibObjects_ObjectIdentity = ObjectIdentity
me1200HqosMibObjects = _Me1200HqosMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1)
)
_Me1200HqosConfig_ObjectIdentity = ObjectIdentity
me1200HqosConfig = _Me1200HqosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2)
)
_Me1200HqosConfigInterface_ObjectIdentity = ObjectIdentity
me1200HqosConfigInterface = _Me1200HqosConfigInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2)
)
_Me1200HqosConfigInterfaceTable_Object = MibTable
me1200HqosConfigInterfaceTable = _Me1200HqosConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceTable.setStatus("current")
_Me1200HqosConfigInterfaceEntry_Object = MibTableRow
me1200HqosConfigInterfaceEntry = _Me1200HqosConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 1, 1)
)
me1200HqosConfigInterfaceEntry.setIndexNames(
    (0, "ME1200-HQOS-MIB", "me1200HqosConfigInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceEntry.setStatus("current")
_Me1200HqosConfigInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200HqosConfigInterfaceIfIndex_Object = MibTableColumn
me1200HqosConfigInterfaceIfIndex = _Me1200HqosConfigInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 1, 1, 1),
    _Me1200HqosConfigInterfaceIfIndex_Type()
)
me1200HqosConfigInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceIfIndex.setStatus("current")
_Me1200HqosConfigInterfaceSchMode_Type = ME1200hqosSchMode
_Me1200HqosConfigInterfaceSchMode_Object = MibTableColumn
me1200HqosConfigInterfaceSchMode = _Me1200HqosConfigInterfaceSchMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 1, 1, 2),
    _Me1200HqosConfigInterfaceSchMode_Type()
)
me1200HqosConfigInterfaceSchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceSchMode.setStatus("current")
_Me1200HqosConfigInterfaceHqosTable_Object = MibTable
me1200HqosConfigInterfaceHqosTable = _Me1200HqosConfigInterfaceHqosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTable.setStatus("current")
_Me1200HqosConfigInterfaceHqosEntry_Object = MibTableRow
me1200HqosConfigInterfaceHqosEntry = _Me1200HqosConfigInterfaceHqosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2, 1)
)
me1200HqosConfigInterfaceHqosEntry.setIndexNames(
    (0, "ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosIfIndex"),
    (0, "ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosHqosId"),
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosEntry.setStatus("current")
_Me1200HqosConfigInterfaceHqosIfIndex_Type = ME1200InterfaceIndex
_Me1200HqosConfigInterfaceHqosIfIndex_Object = MibTableColumn
me1200HqosConfigInterfaceHqosIfIndex = _Me1200HqosConfigInterfaceHqosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2, 1, 1),
    _Me1200HqosConfigInterfaceHqosIfIndex_Type()
)
me1200HqosConfigInterfaceHqosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosIfIndex.setStatus("current")


class _Me1200HqosConfigInterfaceHqosHqosId_Type(Integer32):
    """Custom type me1200HqosConfigInterfaceHqosHqosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Me1200HqosConfigInterfaceHqosHqosId_Type.__name__ = "Integer32"
_Me1200HqosConfigInterfaceHqosHqosId_Object = MibTableColumn
me1200HqosConfigInterfaceHqosHqosId = _Me1200HqosConfigInterfaceHqosHqosId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2, 1, 2),
    _Me1200HqosConfigInterfaceHqosHqosId_Type()
)
me1200HqosConfigInterfaceHqosHqosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosHqosId.setStatus("current")
_Me1200HqosConfigInterfaceHqosDwrrCount_Type = ME1200Unsigned8
_Me1200HqosConfigInterfaceHqosDwrrCount_Object = MibTableColumn
me1200HqosConfigInterfaceHqosDwrrCount = _Me1200HqosConfigInterfaceHqosDwrrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2, 1, 3),
    _Me1200HqosConfigInterfaceHqosDwrrCount_Type()
)
me1200HqosConfigInterfaceHqosDwrrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosDwrrCount.setStatus("current")
_Me1200HqosConfigInterfaceHqosShaperEnable_Type = TruthValue
_Me1200HqosConfigInterfaceHqosShaperEnable_Object = MibTableColumn
me1200HqosConfigInterfaceHqosShaperEnable = _Me1200HqosConfigInterfaceHqosShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2, 1, 4),
    _Me1200HqosConfigInterfaceHqosShaperEnable_Type()
)
me1200HqosConfigInterfaceHqosShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosShaperEnable.setStatus("current")
_Me1200HqosConfigInterfaceHqosShaperRate_Type = Unsigned32
_Me1200HqosConfigInterfaceHqosShaperRate_Object = MibTableColumn
me1200HqosConfigInterfaceHqosShaperRate = _Me1200HqosConfigInterfaceHqosShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2, 1, 5),
    _Me1200HqosConfigInterfaceHqosShaperRate_Type()
)
me1200HqosConfigInterfaceHqosShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosShaperRate.setStatus("current")
_Me1200HqosConfigInterfaceHqosMinRate_Type = Unsigned32
_Me1200HqosConfigInterfaceHqosMinRate_Object = MibTableColumn
me1200HqosConfigInterfaceHqosMinRate = _Me1200HqosConfigInterfaceHqosMinRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2, 1, 6),
    _Me1200HqosConfigInterfaceHqosMinRate_Type()
)
me1200HqosConfigInterfaceHqosMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosMinRate.setStatus("current")
_Me1200HqosConfigInterfaceHqosAction_Type = ME1200RowEditorState
_Me1200HqosConfigInterfaceHqosAction_Object = MibTableColumn
me1200HqosConfigInterfaceHqosAction = _Me1200HqosConfigInterfaceHqosAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 2, 1, 10000),
    _Me1200HqosConfigInterfaceHqosAction_Type()
)
me1200HqosConfigInterfaceHqosAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosAction.setStatus("current")
_Me1200HqosConfigInterfaceHqosTableRowEditor_ObjectIdentity = ObjectIdentity
me1200HqosConfigInterfaceHqosTableRowEditor = _Me1200HqosConfigInterfaceHqosTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 3)
)
_Me1200HqosConfigInterfaceHqosTableRowEditorIfIndex_Type = ME1200InterfaceIndex
_Me1200HqosConfigInterfaceHqosTableRowEditorIfIndex_Object = MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorIfIndex = _Me1200HqosConfigInterfaceHqosTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 3, 1),
    _Me1200HqosConfigInterfaceHqosTableRowEditorIfIndex_Type()
)
me1200HqosConfigInterfaceHqosTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableRowEditorIfIndex.setStatus("current")


class _Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Type(Integer32):
    """Custom type me1200HqosConfigInterfaceHqosTableRowEditorHqosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Type.__name__ = "Integer32"
_Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Object = MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorHqosId = _Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 3, 2),
    _Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Type()
)
me1200HqosConfigInterfaceHqosTableRowEditorHqosId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableRowEditorHqosId.setStatus("current")
_Me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount_Type = ME1200Unsigned8
_Me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount_Object = MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount = _Me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 3, 3),
    _Me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount_Type()
)
me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount.setStatus("current")
_Me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable_Type = TruthValue
_Me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable_Object = MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable = _Me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 3, 4),
    _Me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable_Type()
)
me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable.setStatus("current")
_Me1200HqosConfigInterfaceHqosTableRowEditorShaperRate_Type = Unsigned32
_Me1200HqosConfigInterfaceHqosTableRowEditorShaperRate_Object = MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorShaperRate = _Me1200HqosConfigInterfaceHqosTableRowEditorShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 3, 5),
    _Me1200HqosConfigInterfaceHqosTableRowEditorShaperRate_Type()
)
me1200HqosConfigInterfaceHqosTableRowEditorShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableRowEditorShaperRate.setStatus("current")
_Me1200HqosConfigInterfaceHqosTableRowEditorMinRate_Type = Unsigned32
_Me1200HqosConfigInterfaceHqosTableRowEditorMinRate_Object = MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorMinRate = _Me1200HqosConfigInterfaceHqosTableRowEditorMinRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 3, 6),
    _Me1200HqosConfigInterfaceHqosTableRowEditorMinRate_Type()
)
me1200HqosConfigInterfaceHqosTableRowEditorMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableRowEditorMinRate.setStatus("current")
_Me1200HqosConfigInterfaceHqosTableRowEditorAction_Type = ME1200RowEditorState
_Me1200HqosConfigInterfaceHqosTableRowEditorAction_Object = MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorAction = _Me1200HqosConfigInterfaceHqosTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 3, 10000),
    _Me1200HqosConfigInterfaceHqosTableRowEditorAction_Type()
)
me1200HqosConfigInterfaceHqosTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableRowEditorAction.setStatus("current")
_Me1200HqosConfigInterfaceHqosQueueTable_Object = MibTable
me1200HqosConfigInterfaceHqosQueueTable = _Me1200HqosConfigInterfaceHqosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueTable.setStatus("current")
_Me1200HqosConfigInterfaceHqosQueueEntry_Object = MibTableRow
me1200HqosConfigInterfaceHqosQueueEntry = _Me1200HqosConfigInterfaceHqosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 4, 1)
)
me1200HqosConfigInterfaceHqosQueueEntry.setIndexNames(
    (0, "ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosQueueIfIndex"),
    (0, "ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosQueueHqosId"),
    (0, "ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosQueueQueue"),
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueEntry.setStatus("current")
_Me1200HqosConfigInterfaceHqosQueueIfIndex_Type = ME1200InterfaceIndex
_Me1200HqosConfigInterfaceHqosQueueIfIndex_Object = MibTableColumn
me1200HqosConfigInterfaceHqosQueueIfIndex = _Me1200HqosConfigInterfaceHqosQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 4, 1, 1),
    _Me1200HqosConfigInterfaceHqosQueueIfIndex_Type()
)
me1200HqosConfigInterfaceHqosQueueIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueIfIndex.setStatus("current")


class _Me1200HqosConfigInterfaceHqosQueueHqosId_Type(Integer32):
    """Custom type me1200HqosConfigInterfaceHqosQueueHqosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Me1200HqosConfigInterfaceHqosQueueHqosId_Type.__name__ = "Integer32"
_Me1200HqosConfigInterfaceHqosQueueHqosId_Object = MibTableColumn
me1200HqosConfigInterfaceHqosQueueHqosId = _Me1200HqosConfigInterfaceHqosQueueHqosId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 4, 1, 2),
    _Me1200HqosConfigInterfaceHqosQueueHqosId_Type()
)
me1200HqosConfigInterfaceHqosQueueHqosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueHqosId.setStatus("current")


class _Me1200HqosConfigInterfaceHqosQueueQueue_Type(Integer32):
    """Custom type me1200HqosConfigInterfaceHqosQueueQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200HqosConfigInterfaceHqosQueueQueue_Type.__name__ = "Integer32"
_Me1200HqosConfigInterfaceHqosQueueQueue_Object = MibTableColumn
me1200HqosConfigInterfaceHqosQueueQueue = _Me1200HqosConfigInterfaceHqosQueueQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 4, 1, 3),
    _Me1200HqosConfigInterfaceHqosQueueQueue_Type()
)
me1200HqosConfigInterfaceHqosQueueQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueQueue.setStatus("current")
_Me1200HqosConfigInterfaceHqosQueueShaperEnable_Type = TruthValue
_Me1200HqosConfigInterfaceHqosQueueShaperEnable_Object = MibTableColumn
me1200HqosConfigInterfaceHqosQueueShaperEnable = _Me1200HqosConfigInterfaceHqosQueueShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 4, 1, 4),
    _Me1200HqosConfigInterfaceHqosQueueShaperEnable_Type()
)
me1200HqosConfigInterfaceHqosQueueShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueShaperEnable.setStatus("current")
_Me1200HqosConfigInterfaceHqosQueueShaperRate_Type = Unsigned32
_Me1200HqosConfigInterfaceHqosQueueShaperRate_Object = MibTableColumn
me1200HqosConfigInterfaceHqosQueueShaperRate = _Me1200HqosConfigInterfaceHqosQueueShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 4, 1, 5),
    _Me1200HqosConfigInterfaceHqosQueueShaperRate_Type()
)
me1200HqosConfigInterfaceHqosQueueShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueShaperRate.setStatus("current")
_Me1200HqosConfigInterfaceHqosQueueSchedulerWeight_Type = ME1200Unsigned8
_Me1200HqosConfigInterfaceHqosQueueSchedulerWeight_Object = MibTableColumn
me1200HqosConfigInterfaceHqosQueueSchedulerWeight = _Me1200HqosConfigInterfaceHqosQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 2, 4, 1, 6),
    _Me1200HqosConfigInterfaceHqosQueueSchedulerWeight_Type()
)
me1200HqosConfigInterfaceHqosQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueSchedulerWeight.setStatus("current")
_Me1200HqosConfigHqos_ObjectIdentity = ObjectIdentity
me1200HqosConfigHqos = _Me1200HqosConfigHqos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 1, 2, 4)
)
_Me1200HqosMibConformance_ObjectIdentity = ObjectIdentity
me1200HqosMibConformance = _Me1200HqosMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 2)
)
_Me1200HqosMibCompliances_ObjectIdentity = ObjectIdentity
me1200HqosMibCompliances = _Me1200HqosMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 2, 1)
)
_Me1200HqosMibGroups_ObjectIdentity = ObjectIdentity
me1200HqosMibGroups = _Me1200HqosMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 2, 2)
)

# Managed Objects groups

me1200HqosConfigInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 2, 2, 1)
)
me1200HqosConfigInterfaceTableInfoGroup.setObjects(
    ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceSchMode")
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceTableInfoGroup.setStatus("current")

me1200HqosConfigInterfaceHqosTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 2, 2, 2)
)
me1200HqosConfigInterfaceHqosTableInfoGroup.setObjects(
      *(("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosDwrrCount"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosShaperEnable"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosShaperRate"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosMinRate"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosAction"))
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableInfoGroup.setStatus("current")

me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 2, 2, 3)
)
me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup.setObjects(
      *(("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableRowEditorIfIndex"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableRowEditorHqosId"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableRowEditorShaperRate"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableRowEditorMinRate"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup.setStatus("current")

me1200HqosConfigInterfaceHqosQueueTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 2, 2, 4)
)
me1200HqosConfigInterfaceHqosQueueTableInfoGroup.setObjects(
      *(("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosQueueShaperEnable"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosQueueShaperRate"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosQueueSchedulerWeight"))
)
if mibBuilder.loadTexts:
    me1200HqosConfigInterfaceHqosQueueTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200HqosMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 125, 2, 1, 1)
)
me1200HqosMibCompliance.setObjects(
      *(("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceTableInfoGroup"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableInfoGroup"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup"),
        ("ME1200-HQOS-MIB", "me1200HqosConfigInterfaceHqosQueueTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200HqosMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-HQOS-MIB",
    **{"ME1200hqosSchMode": ME1200hqosSchMode,
       "me1200HqosMib": me1200HqosMib,
       "me1200HqosMibObjects": me1200HqosMibObjects,
       "me1200HqosConfig": me1200HqosConfig,
       "me1200HqosConfigInterface": me1200HqosConfigInterface,
       "me1200HqosConfigInterfaceTable": me1200HqosConfigInterfaceTable,
       "me1200HqosConfigInterfaceEntry": me1200HqosConfigInterfaceEntry,
       "me1200HqosConfigInterfaceIfIndex": me1200HqosConfigInterfaceIfIndex,
       "me1200HqosConfigInterfaceSchMode": me1200HqosConfigInterfaceSchMode,
       "me1200HqosConfigInterfaceHqosTable": me1200HqosConfigInterfaceHqosTable,
       "me1200HqosConfigInterfaceHqosEntry": me1200HqosConfigInterfaceHqosEntry,
       "me1200HqosConfigInterfaceHqosIfIndex": me1200HqosConfigInterfaceHqosIfIndex,
       "me1200HqosConfigInterfaceHqosHqosId": me1200HqosConfigInterfaceHqosHqosId,
       "me1200HqosConfigInterfaceHqosDwrrCount": me1200HqosConfigInterfaceHqosDwrrCount,
       "me1200HqosConfigInterfaceHqosShaperEnable": me1200HqosConfigInterfaceHqosShaperEnable,
       "me1200HqosConfigInterfaceHqosShaperRate": me1200HqosConfigInterfaceHqosShaperRate,
       "me1200HqosConfigInterfaceHqosMinRate": me1200HqosConfigInterfaceHqosMinRate,
       "me1200HqosConfigInterfaceHqosAction": me1200HqosConfigInterfaceHqosAction,
       "me1200HqosConfigInterfaceHqosTableRowEditor": me1200HqosConfigInterfaceHqosTableRowEditor,
       "me1200HqosConfigInterfaceHqosTableRowEditorIfIndex": me1200HqosConfigInterfaceHqosTableRowEditorIfIndex,
       "me1200HqosConfigInterfaceHqosTableRowEditorHqosId": me1200HqosConfigInterfaceHqosTableRowEditorHqosId,
       "me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount": me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount,
       "me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable": me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable,
       "me1200HqosConfigInterfaceHqosTableRowEditorShaperRate": me1200HqosConfigInterfaceHqosTableRowEditorShaperRate,
       "me1200HqosConfigInterfaceHqosTableRowEditorMinRate": me1200HqosConfigInterfaceHqosTableRowEditorMinRate,
       "me1200HqosConfigInterfaceHqosTableRowEditorAction": me1200HqosConfigInterfaceHqosTableRowEditorAction,
       "me1200HqosConfigInterfaceHqosQueueTable": me1200HqosConfigInterfaceHqosQueueTable,
       "me1200HqosConfigInterfaceHqosQueueEntry": me1200HqosConfigInterfaceHqosQueueEntry,
       "me1200HqosConfigInterfaceHqosQueueIfIndex": me1200HqosConfigInterfaceHqosQueueIfIndex,
       "me1200HqosConfigInterfaceHqosQueueHqosId": me1200HqosConfigInterfaceHqosQueueHqosId,
       "me1200HqosConfigInterfaceHqosQueueQueue": me1200HqosConfigInterfaceHqosQueueQueue,
       "me1200HqosConfigInterfaceHqosQueueShaperEnable": me1200HqosConfigInterfaceHqosQueueShaperEnable,
       "me1200HqosConfigInterfaceHqosQueueShaperRate": me1200HqosConfigInterfaceHqosQueueShaperRate,
       "me1200HqosConfigInterfaceHqosQueueSchedulerWeight": me1200HqosConfigInterfaceHqosQueueSchedulerWeight,
       "me1200HqosConfigHqos": me1200HqosConfigHqos,
       "me1200HqosMibConformance": me1200HqosMibConformance,
       "me1200HqosMibCompliances": me1200HqosMibCompliances,
       "me1200HqosMibCompliance": me1200HqosMibCompliance,
       "me1200HqosMibGroups": me1200HqosMibGroups,
       "me1200HqosConfigInterfaceTableInfoGroup": me1200HqosConfigInterfaceTableInfoGroup,
       "me1200HqosConfigInterfaceHqosTableInfoGroup": me1200HqosConfigInterfaceHqosTableInfoGroup,
       "me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup": me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup,
       "me1200HqosConfigInterfaceHqosQueueTableInfoGroup": me1200HqosConfigInterfaceHqosQueueTableInfoGroup}
)
