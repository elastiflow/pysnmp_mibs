# SNMP MIB module (CEM-TR08) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-TR08.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(Cn1000ConfigurationStatus,
 Cn1000ShelfRange) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "Cn1000ConfigurationStatus",
    "Cn1000ShelfRange")

(CnIfGroupIndexRange,
 CnIfGroupLinkType,
 cnTR08) = mibBuilder.importSymbols(
    "CEM-INTERFACES",
    "CnIfGroupIndexRange",
    "CnIfGroupLinkType",
    "cnTR08")

(CnSlotGroupNameType,) = mibBuilder.importSymbols(
    "CEM-TEXTUAL-CONVENTIONS",
    "CnSlotGroupNameType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cnTR08Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CnTR08ModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnTR08Mode1", 1),
          ("cnTR08Mode2", 2))
    )



class CnTR08AlarmFrameFormatType(TextualConvention, Integer32):
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
        *(("cnTR0813", 1),
          ("cnTR0816", 2),
          ("cnTR08AutoFormat", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CnTR08IfGroupConfigTable_Object = MibTable
cnTR08IfGroupConfigTable = _CnTR08IfGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cnTR08IfGroupConfigTable.setStatus("current")
_CnTR08IfGroupConfigEntry_Object = MibTableRow
cnTR08IfGroupConfigEntry = _CnTR08IfGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1)
)
cnTR08IfGroupConfigEntry.setIndexNames(
    (0, "CEM-TR08", "cnTR08IfGroupIndex"),
)
if mibBuilder.loadTexts:
    cnTR08IfGroupConfigEntry.setStatus("current")
_CnTR08IfGroupShelf_Type = Cn1000ShelfRange
_CnTR08IfGroupShelf_Object = MibTableColumn
cnTR08IfGroupShelf = _CnTR08IfGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 1),
    _CnTR08IfGroupShelf_Type()
)
cnTR08IfGroupShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupShelf.setStatus("current")
_CnTR08IfGroupSlotGroup_Type = CnSlotGroupNameType
_CnTR08IfGroupSlotGroup_Object = MibTableColumn
cnTR08IfGroupSlotGroup = _CnTR08IfGroupSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 2),
    _CnTR08IfGroupSlotGroup_Type()
)
cnTR08IfGroupSlotGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupSlotGroup.setStatus("current")
_CnTR08IfGroupIndex_Type = CnIfGroupIndexRange
_CnTR08IfGroupIndex_Object = MibTableColumn
cnTR08IfGroupIndex = _CnTR08IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 3),
    _CnTR08IfGroupIndex_Type()
)
cnTR08IfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupIndex.setStatus("current")


class _CnTR08IfGroupConnectionIndex_Type(Integer32):
    """Custom type cnTR08IfGroupConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_CnTR08IfGroupConnectionIndex_Type.__name__ = "Integer32"
_CnTR08IfGroupConnectionIndex_Object = MibTableColumn
cnTR08IfGroupConnectionIndex = _CnTR08IfGroupConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 4),
    _CnTR08IfGroupConnectionIndex_Type()
)
cnTR08IfGroupConnectionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTR08IfGroupConnectionIndex.setStatus("current")
_CnTR08IfGroupABGroupMode_Type = CnTR08ModeType
_CnTR08IfGroupABGroupMode_Object = MibTableColumn
cnTR08IfGroupABGroupMode = _CnTR08IfGroupABGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 5),
    _CnTR08IfGroupABGroupMode_Type()
)
cnTR08IfGroupABGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupABGroupMode.setStatus("current")
_CnTR08IfGroupCDGroupMode_Type = CnTR08ModeType
_CnTR08IfGroupCDGroupMode_Object = MibTableColumn
cnTR08IfGroupCDGroupMode = _CnTR08IfGroupCDGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 6),
    _CnTR08IfGroupCDGroupMode_Type()
)
cnTR08IfGroupCDGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupCDGroupMode.setStatus("current")


class _CnTR08IfGroupDefaultMetallicTestBus_Type(Integer32):
    """Custom type cnTR08IfGroupDefaultMetallicTestBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CnTR08IfGroupDefaultMetallicTestBus_Type.__name__ = "Integer32"
_CnTR08IfGroupDefaultMetallicTestBus_Object = MibTableColumn
cnTR08IfGroupDefaultMetallicTestBus = _CnTR08IfGroupDefaultMetallicTestBus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 12),
    _CnTR08IfGroupDefaultMetallicTestBus_Type()
)
cnTR08IfGroupDefaultMetallicTestBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupDefaultMetallicTestBus.setStatus("current")


class _CnTR08IfGroupDescription_Type(OctetString):
    """Custom type cnTR08IfGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CnTR08IfGroupDescription_Type.__name__ = "OctetString"
_CnTR08IfGroupDescription_Object = MibTableColumn
cnTR08IfGroupDescription = _CnTR08IfGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 13),
    _CnTR08IfGroupDescription_Type()
)
cnTR08IfGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupDescription.setStatus("current")
_CnTR08IfGroupAlarmFrameFormat_Type = CnTR08AlarmFrameFormatType
_CnTR08IfGroupAlarmFrameFormat_Object = MibTableColumn
cnTR08IfGroupAlarmFrameFormat = _CnTR08IfGroupAlarmFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 14),
    _CnTR08IfGroupAlarmFrameFormat_Type()
)
cnTR08IfGroupAlarmFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupAlarmFrameFormat.setStatus("current")


class _CnTR08IfGroupF1Cable_Type(Integer32):
    """Custom type cnTR08IfGroupF1Cable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnTR08IfGroupF1Cable_Type.__name__ = "Integer32"
_CnTR08IfGroupF1Cable_Object = MibTableColumn
cnTR08IfGroupF1Cable = _CnTR08IfGroupF1Cable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 20),
    _CnTR08IfGroupF1Cable_Type()
)
cnTR08IfGroupF1Cable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupF1Cable.setStatus("current")


class _CnTR08IfGroupF1PairRangeStart_Type(Integer32):
    """Custom type cnTR08IfGroupF1PairRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnTR08IfGroupF1PairRangeStart_Type.__name__ = "Integer32"
_CnTR08IfGroupF1PairRangeStart_Object = MibTableColumn
cnTR08IfGroupF1PairRangeStart = _CnTR08IfGroupF1PairRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 21),
    _CnTR08IfGroupF1PairRangeStart_Type()
)
cnTR08IfGroupF1PairRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupF1PairRangeStart.setStatus("current")


class _CnTR08IfGroupF1PairRangeEnd_Type(Integer32):
    """Custom type cnTR08IfGroupF1PairRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnTR08IfGroupF1PairRangeEnd_Type.__name__ = "Integer32"
_CnTR08IfGroupF1PairRangeEnd_Object = MibTableColumn
cnTR08IfGroupF1PairRangeEnd = _CnTR08IfGroupF1PairRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 22),
    _CnTR08IfGroupF1PairRangeEnd_Type()
)
cnTR08IfGroupF1PairRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupF1PairRangeEnd.setStatus("current")


class _CnTR08IfGroupAdminState_Type(Integer32):
    """Custom type cnTR08IfGroupAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undetermined", 0),
          ("up", 1),
          ("down", 2))
    )


_CnTR08IfGroupAdminState_Type.__name__ = "Integer32"
_CnTR08IfGroupAdminState_Object = MibTableColumn
cnTR08IfGroupAdminState = _CnTR08IfGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 23),
    _CnTR08IfGroupAdminState_Type()
)
cnTR08IfGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupAdminState.setStatus("current")
_CnTR08IfGroupConfigStatus_Type = Cn1000ConfigurationStatus
_CnTR08IfGroupConfigStatus_Object = MibTableColumn
cnTR08IfGroupConfigStatus = _CnTR08IfGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 24),
    _CnTR08IfGroupConfigStatus_Type()
)
cnTR08IfGroupConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTR08IfGroupConfigStatus.setStatus("current")
_CnTR08IfGroupRowStatus_Type = RowStatus
_CnTR08IfGroupRowStatus_Object = MibTableColumn
cnTR08IfGroupRowStatus = _CnTR08IfGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 1, 1, 25),
    _CnTR08IfGroupRowStatus_Type()
)
cnTR08IfGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08IfGroupRowStatus.setStatus("current")
_CnTR08LinkTable_Object = MibTable
cnTR08LinkTable = _CnTR08LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cnTR08LinkTable.setStatus("current")
_CnTR08LinkEntry_Object = MibTableRow
cnTR08LinkEntry = _CnTR08LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 2, 1)
)
cnTR08LinkEntry.setIndexNames(
    (0, "CEM-TR08", "cnTR08LinkIfGroupIndex"),
    (0, "CEM-TR08", "cnTR08LinkIfIndex"),
)
if mibBuilder.loadTexts:
    cnTR08LinkEntry.setStatus("current")
_CnTR08LinkIfGroupIndex_Type = CnIfGroupIndexRange
_CnTR08LinkIfGroupIndex_Object = MibTableColumn
cnTR08LinkIfGroupIndex = _CnTR08LinkIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 2, 1, 1),
    _CnTR08LinkIfGroupIndex_Type()
)
cnTR08LinkIfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08LinkIfGroupIndex.setStatus("current")
_CnTR08LinkIfIndex_Type = InterfaceIndex
_CnTR08LinkIfIndex_Object = MibTableColumn
cnTR08LinkIfIndex = _CnTR08LinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 2, 1, 2),
    _CnTR08LinkIfIndex_Type()
)
cnTR08LinkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08LinkIfIndex.setStatus("current")
_CnTR08LinkType_Type = CnIfGroupLinkType
_CnTR08LinkType_Object = MibTableColumn
cnTR08LinkType = _CnTR08LinkType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 2, 1, 3),
    _CnTR08LinkType_Type()
)
cnTR08LinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08LinkType.setStatus("current")
_CnTR08LinkConfigStatus_Type = Cn1000ConfigurationStatus
_CnTR08LinkConfigStatus_Object = MibTableColumn
cnTR08LinkConfigStatus = _CnTR08LinkConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 2, 1, 4),
    _CnTR08LinkConfigStatus_Type()
)
cnTR08LinkConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTR08LinkConfigStatus.setStatus("current")
_CnTR08LinkRowStatus_Type = RowStatus
_CnTR08LinkRowStatus_Object = MibTableColumn
cnTR08LinkRowStatus = _CnTR08LinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 2, 1, 5),
    _CnTR08LinkRowStatus_Type()
)
cnTR08LinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTR08LinkRowStatus.setStatus("current")

# Managed Objects groups

cnTR08ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2, 1, 10)
)
cnTR08ObjectsGroup.setObjects(
      *(("CEM-TR08", "cnTR08IfGroupShelf"),
        ("CEM-TR08", "cnTR08IfGroupSlotGroup"),
        ("CEM-TR08", "cnTR08IfGroupIndex"),
        ("CEM-TR08", "cnTR08IfGroupConnectionIndex"),
        ("CEM-TR08", "cnTR08IfGroupABGroupMode"),
        ("CEM-TR08", "cnTR08IfGroupCDGroupMode"),
        ("CEM-TR08", "cnTR08IfGroupDefaultMetallicTestBus"),
        ("CEM-TR08", "cnTR08IfGroupDescription"),
        ("CEM-TR08", "cnTR08IfGroupAlarmFrameFormat"),
        ("CEM-TR08", "cnTR08IfGroupF1Cable"),
        ("CEM-TR08", "cnTR08IfGroupF1PairRangeStart"),
        ("CEM-TR08", "cnTR08IfGroupF1PairRangeEnd"),
        ("CEM-TR08", "cnTR08IfGroupAdminState"),
        ("CEM-TR08", "cnTR08IfGroupConfigStatus"),
        ("CEM-TR08", "cnTR08IfGroupRowStatus"),
        ("CEM-TR08", "cnTR08LinkIfGroupIndex"),
        ("CEM-TR08", "cnTR08LinkIfIndex"),
        ("CEM-TR08", "cnTR08LinkType"),
        ("CEM-TR08", "cnTR08LinkConfigStatus"),
        ("CEM-TR08", "cnTR08LinkRowStatus"))
)
if mibBuilder.loadTexts:
    cnTR08ObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-TR08",
    **{"CnTR08ModeType": CnTR08ModeType,
       "CnTR08AlarmFrameFormatType": CnTR08AlarmFrameFormatType,
       "cnTR08Module": cnTR08Module,
       "cnTR08IfGroupConfigTable": cnTR08IfGroupConfigTable,
       "cnTR08IfGroupConfigEntry": cnTR08IfGroupConfigEntry,
       "cnTR08IfGroupShelf": cnTR08IfGroupShelf,
       "cnTR08IfGroupSlotGroup": cnTR08IfGroupSlotGroup,
       "cnTR08IfGroupIndex": cnTR08IfGroupIndex,
       "cnTR08IfGroupConnectionIndex": cnTR08IfGroupConnectionIndex,
       "cnTR08IfGroupABGroupMode": cnTR08IfGroupABGroupMode,
       "cnTR08IfGroupCDGroupMode": cnTR08IfGroupCDGroupMode,
       "cnTR08IfGroupDefaultMetallicTestBus": cnTR08IfGroupDefaultMetallicTestBus,
       "cnTR08IfGroupDescription": cnTR08IfGroupDescription,
       "cnTR08IfGroupAlarmFrameFormat": cnTR08IfGroupAlarmFrameFormat,
       "cnTR08IfGroupF1Cable": cnTR08IfGroupF1Cable,
       "cnTR08IfGroupF1PairRangeStart": cnTR08IfGroupF1PairRangeStart,
       "cnTR08IfGroupF1PairRangeEnd": cnTR08IfGroupF1PairRangeEnd,
       "cnTR08IfGroupAdminState": cnTR08IfGroupAdminState,
       "cnTR08IfGroupConfigStatus": cnTR08IfGroupConfigStatus,
       "cnTR08IfGroupRowStatus": cnTR08IfGroupRowStatus,
       "cnTR08LinkTable": cnTR08LinkTable,
       "cnTR08LinkEntry": cnTR08LinkEntry,
       "cnTR08LinkIfGroupIndex": cnTR08LinkIfGroupIndex,
       "cnTR08LinkIfIndex": cnTR08LinkIfIndex,
       "cnTR08LinkType": cnTR08LinkType,
       "cnTR08LinkConfigStatus": cnTR08LinkConfigStatus,
       "cnTR08LinkRowStatus": cnTR08LinkRowStatus,
       "cnTR08ObjectsGroup": cnTR08ObjectsGroup}
)
