# SNMP MIB module (CEM-CARD-REDUNDANCY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CARD-REDUNDANCY.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(CnSlotGroupNameType,) = mibBuilder.importSymbols(
    "CEM-TEXTUAL-CONVENTIONS",
    "CnSlotGroupNameType")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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

cnCardRedundancyModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 6)
)
if mibBuilder.loadTexts:
    cnCardRedundancyModule.setRevisions(
        ("2001-09-14 14:12",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnRedundantCardGroupTable_Object = MibTable
cnRedundantCardGroupTable = _CnRedundantCardGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1)
)
if mibBuilder.loadTexts:
    cnRedundantCardGroupTable.setStatus("current")
_CnRedundantCardGroupEntry_Object = MibTableRow
cnRedundantCardGroupEntry = _CnRedundantCardGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1)
)
cnRedundantCardGroupEntry.setIndexNames(
    (0, "CEM-CARD-REDUNDANCY", "cnRCShelf"),
    (0, "CEM-CARD-REDUNDANCY", "cnRCSlotGroup"),
)
if mibBuilder.loadTexts:
    cnRedundantCardGroupEntry.setStatus("current")


class _CnRCShelf_Type(Integer32):
    """Custom type cnRCShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CnRCShelf_Type.__name__ = "Integer32"
_CnRCShelf_Object = MibTableColumn
cnRCShelf = _CnRCShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 1),
    _CnRCShelf_Type()
)
cnRCShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRCShelf.setStatus("current")
_CnRCSlotGroup_Type = CnSlotGroupNameType
_CnRCSlotGroup_Object = MibTableColumn
cnRCSlotGroup = _CnRCSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 2),
    _CnRCSlotGroup_Type()
)
cnRCSlotGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRCSlotGroup.setStatus("current")


class _CnRCRedundantCardType_Type(Integer32):
    """Custom type cnRCRedundantCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cnRCcn1000CECard", 0),
          ("cnRCcn1000T1Card", 1),
          ("cnRCcn1000WANShortHaulEnhancedCard", 2),
          ("cnRCcn1000WANLongHaulEnhancedCard", 3),
          ("cnRCcn1000WANShortHaulCard", 4),
          ("cnRCcn1000WANLongHaulCard", 5),
          ("cnRCcn1000Ds3Card", 6),
          ("cnRCcn1000E1Card", 7),
          ("cnRCcn1000WANOC12", 8))
    )


_CnRCRedundantCardType_Type.__name__ = "Integer32"
_CnRCRedundantCardType_Object = MibTableColumn
cnRCRedundantCardType = _CnRCRedundantCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 3),
    _CnRCRedundantCardType_Type()
)
cnRCRedundantCardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnRCRedundantCardType.setStatus("current")


class _CnCardGrouping_Type(Integer32):
    """Custom type cnCardGrouping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnRCUnspared", 1),
          ("cnRConeToOneSpared", 2))
    )


_CnCardGrouping_Type.__name__ = "Integer32"
_CnCardGrouping_Object = MibTableColumn
cnCardGrouping = _CnCardGrouping_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 4),
    _CnCardGrouping_Type()
)
cnCardGrouping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnCardGrouping.setStatus("current")


class _CnRCAlias_Type(OctetString):
    """Custom type cnRCAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnRCAlias_Type.__name__ = "OctetString"
_CnRCAlias_Object = MibTableColumn
cnRCAlias = _CnRCAlias_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 5),
    _CnRCAlias_Type()
)
cnRCAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnRCAlias.setStatus("current")


class _CnRedundancyAdminState_Type(Integer32):
    """Custom type cnRedundancyAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnRCJoined", 1),
          ("cnRCPartitioned", 2))
    )


_CnRedundancyAdminState_Type.__name__ = "Integer32"
_CnRedundancyAdminState_Object = MibTableColumn
cnRedundancyAdminState = _CnRedundancyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 6),
    _CnRedundancyAdminState_Type()
)
cnRedundancyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnRedundancyAdminState.setStatus("current")


class _CnSwitchOverPolicy_Type(Integer32):
    """Custom type cnSwitchOverPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cnRCOnlyManualAllowed", 1),
          ("cnRCManualOrAutomaticAllowed", 2),
          ("cnRCSwitchoverNotAllowed", 3))
    )


_CnSwitchOverPolicy_Type.__name__ = "Integer32"
_CnSwitchOverPolicy_Object = MibTableColumn
cnSwitchOverPolicy = _CnSwitchOverPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 7),
    _CnSwitchOverPolicy_Type()
)
cnSwitchOverPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnSwitchOverPolicy.setStatus("current")


class _CnActivityControl_Type(Integer32):
    """Custom type cnActivityControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("cnRCCheckedSwitchover", 1),
          ("cnRCForcedSwitchover", 2),
          ("cnRCForcedSwitchoverFailed", 3),
          ("cnRCForcedSwitchoverPassed", 4),
          ("cnRCCheckedSwitchoverFailed", 5),
          ("cnRCCheckedSwitchoverPassed", 6),
          ("cnNoSwitchoversYet", 7),
          ("cnRCAutoSwitchoverFailed", 9),
          ("cnRCCheckedSwitchoverPreemptedByAutoPassed", 10),
          ("cnRCCheckedSwitchoverPreemptedByAutoFailed", 11),
          ("cnRcSwitchoverOperationAborted", 12))
    )


_CnActivityControl_Type.__name__ = "Integer32"
_CnActivityControl_Object = MibTableColumn
cnActivityControl = _CnActivityControl_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 8),
    _CnActivityControl_Type()
)
cnActivityControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnActivityControl.setStatus("current")


class _CnGroupServiceState_Type(Integer32):
    """Custom type cnGroupServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnRCRedundantServiceUp", 1),
          ("cnRCRedundantServiceDown", 2))
    )


_CnGroupServiceState_Type.__name__ = "Integer32"
_CnGroupServiceState_Object = MibTableColumn
cnGroupServiceState = _CnGroupServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 9),
    _CnGroupServiceState_Type()
)
cnGroupServiceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGroupServiceState.setStatus("current")


class _CnFaultTolerant_Type(Integer32):
    """Custom type cnFaultTolerant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnRCFaultTolerant", 1),
          ("cnRCNotFaultTolerant", 2))
    )


_CnFaultTolerant_Type.__name__ = "Integer32"
_CnFaultTolerant_Object = MibTableColumn
cnFaultTolerant = _CnFaultTolerant_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 10),
    _CnFaultTolerant_Type()
)
cnFaultTolerant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnFaultTolerant.setStatus("current")


class _CnGroupDataSyncState_Type(Integer32):
    """Custom type cnGroupDataSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cnRCNoDataSyncDone", 1),
          ("cnRCConfigCheckpointDone", 2),
          ("cnRCJournaling", 3))
    )


_CnGroupDataSyncState_Type.__name__ = "Integer32"
_CnGroupDataSyncState_Object = MibTableColumn
cnGroupDataSyncState = _CnGroupDataSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 11),
    _CnGroupDataSyncState_Type()
)
cnGroupDataSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGroupDataSyncState.setStatus("current")
_CnCardRedundancyConfigLastChange_Type = TimeTicks
_CnCardRedundancyConfigLastChange_Object = MibTableColumn
cnCardRedundancyConfigLastChange = _CnCardRedundancyConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 12),
    _CnCardRedundancyConfigLastChange_Type()
)
cnCardRedundancyConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCardRedundancyConfigLastChange.setStatus("current")
_CnCardRedundancyActivityLastChange_Type = TimeTicks
_CnCardRedundancyActivityLastChange_Object = MibTableColumn
cnCardRedundancyActivityLastChange = _CnCardRedundancyActivityLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 13),
    _CnCardRedundancyActivityLastChange_Type()
)
cnCardRedundancyActivityLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCardRedundancyActivityLastChange.setStatus("current")
_CnRedundantCardGroupRowStatus_Type = RowStatus
_CnRedundantCardGroupRowStatus_Object = MibTableColumn
cnRedundantCardGroupRowStatus = _CnRedundantCardGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 14),
    _CnRedundantCardGroupRowStatus_Type()
)
cnRedundantCardGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnRedundantCardGroupRowStatus.setStatus("current")


class _CnGroupDataSyncProgressStatus_Type(Integer32):
    """Custom type cnGroupDataSyncProgressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cnRCNoSync", 1),
          ("cnRCCheckpointing", 2),
          ("cnRCSyncing", 3),
          ("cnRCInSync", 4),
          ("cnRCSparing", 5))
    )


_CnGroupDataSyncProgressStatus_Type.__name__ = "Integer32"
_CnGroupDataSyncProgressStatus_Object = MibTableColumn
cnGroupDataSyncProgressStatus = _CnGroupDataSyncProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 15),
    _CnGroupDataSyncProgressStatus_Type()
)
cnGroupDataSyncProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGroupDataSyncProgressStatus.setStatus("current")


class _CnRebootControl_Type(Integer32):
    """Custom type cnRebootControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cnRebootActive", 1),
          ("cnRebootInactive", 2),
          ("cnRebootBoth", 3),
          ("cnRebootPassed", 4),
          ("cnRebootFailed", 5))
    )


_CnRebootControl_Type.__name__ = "Integer32"
_CnRebootControl_Object = MibTableColumn
cnRebootControl = _CnRebootControl_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 1, 1, 16),
    _CnRebootControl_Type()
)
cnRebootControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnRebootControl.setStatus("current")
_CnRedundantCardMappingTable_Object = MibTable
cnRedundantCardMappingTable = _CnRedundantCardMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 2)
)
if mibBuilder.loadTexts:
    cnRedundantCardMappingTable.setStatus("current")
_CnRedundantCardMappingEntry_Object = MibTableRow
cnRedundantCardMappingEntry = _CnRedundantCardMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 2, 1)
)
cnRedundantCardMappingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CEM-CARD-REDUNDANCY", "cnRCSlotGroup"),
    (0, "CEM-CARD-REDUNDANCY", "cnRCRedundantCardType"),
)
if mibBuilder.loadTexts:
    cnRedundantCardMappingEntry.setStatus("current")


class _CnRedundantCardActivityState_Type(Integer32):
    """Custom type cnRedundantCardActivityState based on Integer32"""
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
        *(("cnRCActive", 1),
          ("cnRCInactive", 2),
          ("cnRCInitializing", 3),
          ("cnRCFaulted", 4))
    )


_CnRedundantCardActivityState_Type.__name__ = "Integer32"
_CnRedundantCardActivityState_Object = MibTableColumn
cnRedundantCardActivityState = _CnRedundantCardActivityState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 2, 1, 1),
    _CnRedundantCardActivityState_Type()
)
cnRedundantCardActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRedundantCardActivityState.setStatus("current")


class _CnRedundantCardDemeritPoints_Type(Integer32):
    """Custom type cnRedundantCardDemeritPoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CnRedundantCardDemeritPoints_Type.__name__ = "Integer32"
_CnRedundantCardDemeritPoints_Object = MibTableColumn
cnRedundantCardDemeritPoints = _CnRedundantCardDemeritPoints_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 2, 1, 2),
    _CnRedundantCardDemeritPoints_Type()
)
cnRedundantCardDemeritPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRedundantCardDemeritPoints.setStatus("current")
_CnRedundantCardMappingRowStatus_Type = RowStatus
_CnRedundantCardMappingRowStatus_Object = MibTableColumn
cnRedundantCardMappingRowStatus = _CnRedundantCardMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 6, 2, 1, 3),
    _CnRedundantCardMappingRowStatus_Type()
)
cnRedundantCardMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnRedundantCardMappingRowStatus.setStatus("current")
_CnRedundantCardServiceStateChangeNotification_ObjectIdentity = ObjectIdentity
cnRedundantCardServiceStateChangeNotification = _CnRedundantCardServiceStateChangeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 6, 3)
)
_CnCardRedundancyGroups_ObjectIdentity = ObjectIdentity
cnCardRedundancyGroups = _CnCardRedundancyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 6, 4)
)

# Managed Objects groups

cnCardRedundancyModuleObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 6, 4, 1)
)
cnCardRedundancyModuleObjectGroup.setObjects(
      *(("CEM-CARD-REDUNDANCY", "cnRCShelf"),
        ("CEM-CARD-REDUNDANCY", "cnRCSlotGroup"),
        ("CEM-CARD-REDUNDANCY", "cnRCRedundantCardType"),
        ("CEM-CARD-REDUNDANCY", "cnCardGrouping"),
        ("CEM-CARD-REDUNDANCY", "cnRedundancyAdminState"),
        ("CEM-CARD-REDUNDANCY", "cnSwitchOverPolicy"),
        ("CEM-CARD-REDUNDANCY", "cnActivityControl"),
        ("CEM-CARD-REDUNDANCY", "cnGroupServiceState"),
        ("CEM-CARD-REDUNDANCY", "cnFaultTolerant"),
        ("CEM-CARD-REDUNDANCY", "cnGroupDataSyncState"),
        ("CEM-CARD-REDUNDANCY", "cnCardRedundancyConfigLastChange"),
        ("CEM-CARD-REDUNDANCY", "cnCardRedundancyActivityLastChange"),
        ("CEM-CARD-REDUNDANCY", "cnRedundantCardGroupRowStatus"),
        ("CEM-CARD-REDUNDANCY", "cnRedundantCardActivityState"),
        ("CEM-CARD-REDUNDANCY", "cnRedundantCardDemeritPoints"),
        ("CEM-CARD-REDUNDANCY", "cnGroupDataSyncProgressStatus"),
        ("CEM-CARD-REDUNDANCY", "cnRebootControl"),
        ("CEM-CARD-REDUNDANCY", "cnRedundantCardMappingRowStatus"),
        ("CEM-CARD-REDUNDANCY", "cnRCAlias"))
)
if mibBuilder.loadTexts:
    cnCardRedundancyModuleObjectGroup.setStatus("current")


# Notification objects

cnRedundantCardServiceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 6, 3, 1)
)
cnRedundantCardServiceStateChange.setObjects(
    ("CEM-CARD-REDUNDANCY", "cnGroupServiceState")
)
if mibBuilder.loadTexts:
    cnRedundantCardServiceStateChange.setStatus(
        "current"
    )


# Notifications groups

cnCardRedundancyNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 6, 4, 2)
)
cnCardRedundancyNotificationsGroup.setObjects(
    ("CEM-CARD-REDUNDANCY", "cnRedundantCardServiceStateChange")
)
if mibBuilder.loadTexts:
    cnCardRedundancyNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CARD-REDUNDANCY",
    **{"cnCardRedundancyModule": cnCardRedundancyModule,
       "cnRedundantCardGroupTable": cnRedundantCardGroupTable,
       "cnRedundantCardGroupEntry": cnRedundantCardGroupEntry,
       "cnRCShelf": cnRCShelf,
       "cnRCSlotGroup": cnRCSlotGroup,
       "cnRCRedundantCardType": cnRCRedundantCardType,
       "cnCardGrouping": cnCardGrouping,
       "cnRCAlias": cnRCAlias,
       "cnRedundancyAdminState": cnRedundancyAdminState,
       "cnSwitchOverPolicy": cnSwitchOverPolicy,
       "cnActivityControl": cnActivityControl,
       "cnGroupServiceState": cnGroupServiceState,
       "cnFaultTolerant": cnFaultTolerant,
       "cnGroupDataSyncState": cnGroupDataSyncState,
       "cnCardRedundancyConfigLastChange": cnCardRedundancyConfigLastChange,
       "cnCardRedundancyActivityLastChange": cnCardRedundancyActivityLastChange,
       "cnRedundantCardGroupRowStatus": cnRedundantCardGroupRowStatus,
       "cnGroupDataSyncProgressStatus": cnGroupDataSyncProgressStatus,
       "cnRebootControl": cnRebootControl,
       "cnRedundantCardMappingTable": cnRedundantCardMappingTable,
       "cnRedundantCardMappingEntry": cnRedundantCardMappingEntry,
       "cnRedundantCardActivityState": cnRedundantCardActivityState,
       "cnRedundantCardDemeritPoints": cnRedundantCardDemeritPoints,
       "cnRedundantCardMappingRowStatus": cnRedundantCardMappingRowStatus,
       "cnRedundantCardServiceStateChangeNotification": cnRedundantCardServiceStateChangeNotification,
       "cnRedundantCardServiceStateChange": cnRedundantCardServiceStateChange,
       "cnCardRedundancyGroups": cnCardRedundancyGroups,
       "cnCardRedundancyModuleObjectGroup": cnCardRedundancyModuleObjectGroup,
       "cnCardRedundancyNotificationsGroup": cnCardRedundancyNotificationsGroup}
)
