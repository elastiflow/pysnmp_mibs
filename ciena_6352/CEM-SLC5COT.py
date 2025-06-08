# SNMP MIB module (CEM-SLC5COT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-SLC5COT.mib
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
 cnInterfacesModule) = mibBuilder.importSymbols(
    "CEM-INTERFACES",
    "CnIfGroupIndexRange",
    "CnIfGroupLinkType",
    "cnInterfacesModule")

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

cnSLC5COTModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnSLC5COT_ObjectIdentity = ObjectIdentity
cnSLC5COT = _CnSLC5COT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6)
)
_CnSLC5COTIfGroupConfigTable_Object = MibTable
cnSLC5COTIfGroupConfigTable = _CnSLC5COTIfGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupConfigTable.setStatus("current")
_CnSLC5COTIfGroupConfigEntry_Object = MibTableRow
cnSLC5COTIfGroupConfigEntry = _CnSLC5COTIfGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1)
)
cnSLC5COTIfGroupConfigEntry.setIndexNames(
    (0, "CEM-SLC5COT", "cnSLC5COTIfGroupIndex"),
)
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupConfigEntry.setStatus("current")
_CnSLC5COTIfGroupShelf_Type = Cn1000ShelfRange
_CnSLC5COTIfGroupShelf_Object = MibTableColumn
cnSLC5COTIfGroupShelf = _CnSLC5COTIfGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 1),
    _CnSLC5COTIfGroupShelf_Type()
)
cnSLC5COTIfGroupShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupShelf.setStatus("current")
_CnSLC5COTIfGroupSlotGroup_Type = CnSlotGroupNameType
_CnSLC5COTIfGroupSlotGroup_Object = MibTableColumn
cnSLC5COTIfGroupSlotGroup = _CnSLC5COTIfGroupSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 2),
    _CnSLC5COTIfGroupSlotGroup_Type()
)
cnSLC5COTIfGroupSlotGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupSlotGroup.setStatus("current")
_CnSLC5COTIfGroupIndex_Type = CnIfGroupIndexRange
_CnSLC5COTIfGroupIndex_Object = MibTableColumn
cnSLC5COTIfGroupIndex = _CnSLC5COTIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 3),
    _CnSLC5COTIfGroupIndex_Type()
)
cnSLC5COTIfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupIndex.setStatus("current")


class _CnSLC5COTIfGroupConnectionIndex_Type(Integer32):
    """Custom type cnSLC5COTIfGroupConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_CnSLC5COTIfGroupConnectionIndex_Type.__name__ = "Integer32"
_CnSLC5COTIfGroupConnectionIndex_Object = MibTableColumn
cnSLC5COTIfGroupConnectionIndex = _CnSLC5COTIfGroupConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 4),
    _CnSLC5COTIfGroupConnectionIndex_Type()
)
cnSLC5COTIfGroupConnectionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupConnectionIndex.setStatus("current")


class _CnSLC5COTIfGroupAdminState_Type(Integer32):
    """Custom type cnSLC5COTIfGroupAdminState based on Integer32"""
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


_CnSLC5COTIfGroupAdminState_Type.__name__ = "Integer32"
_CnSLC5COTIfGroupAdminState_Object = MibTableColumn
cnSLC5COTIfGroupAdminState = _CnSLC5COTIfGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 5),
    _CnSLC5COTIfGroupAdminState_Type()
)
cnSLC5COTIfGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupAdminState.setStatus("current")


class _CnSLC5COTIfGroupDescription_Type(OctetString):
    """Custom type cnSLC5COTIfGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CnSLC5COTIfGroupDescription_Type.__name__ = "OctetString"
_CnSLC5COTIfGroupDescription_Object = MibTableColumn
cnSLC5COTIfGroupDescription = _CnSLC5COTIfGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 6),
    _CnSLC5COTIfGroupDescription_Type()
)
cnSLC5COTIfGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupDescription.setStatus("current")
_CnSLC5COTIfGroupConfigStatus_Type = Cn1000ConfigurationStatus
_CnSLC5COTIfGroupConfigStatus_Object = MibTableColumn
cnSLC5COTIfGroupConfigStatus = _CnSLC5COTIfGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 7),
    _CnSLC5COTIfGroupConfigStatus_Type()
)
cnSLC5COTIfGroupConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupConfigStatus.setStatus("current")


class _CnSLC5COTIfGroupF1Cable_Type(Integer32):
    """Custom type cnSLC5COTIfGroupF1Cable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnSLC5COTIfGroupF1Cable_Type.__name__ = "Integer32"
_CnSLC5COTIfGroupF1Cable_Object = MibTableColumn
cnSLC5COTIfGroupF1Cable = _CnSLC5COTIfGroupF1Cable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 8),
    _CnSLC5COTIfGroupF1Cable_Type()
)
cnSLC5COTIfGroupF1Cable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupF1Cable.setStatus("current")


class _CnSLC5COTIfGroupF1PairRangeStart_Type(Integer32):
    """Custom type cnSLC5COTIfGroupF1PairRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnSLC5COTIfGroupF1PairRangeStart_Type.__name__ = "Integer32"
_CnSLC5COTIfGroupF1PairRangeStart_Object = MibTableColumn
cnSLC5COTIfGroupF1PairRangeStart = _CnSLC5COTIfGroupF1PairRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 9),
    _CnSLC5COTIfGroupF1PairRangeStart_Type()
)
cnSLC5COTIfGroupF1PairRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupF1PairRangeStart.setStatus("current")


class _CnSLC5COTIfGroupF1PairRangeEnd_Type(Integer32):
    """Custom type cnSLC5COTIfGroupF1PairRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnSLC5COTIfGroupF1PairRangeEnd_Type.__name__ = "Integer32"
_CnSLC5COTIfGroupF1PairRangeEnd_Object = MibTableColumn
cnSLC5COTIfGroupF1PairRangeEnd = _CnSLC5COTIfGroupF1PairRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 10),
    _CnSLC5COTIfGroupF1PairRangeEnd_Type()
)
cnSLC5COTIfGroupF1PairRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupF1PairRangeEnd.setStatus("current")
_CnSLC5COTIfGroupRowStatus_Type = RowStatus
_CnSLC5COTIfGroupRowStatus_Object = MibTableColumn
cnSLC5COTIfGroupRowStatus = _CnSLC5COTIfGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 1, 1, 11),
    _CnSLC5COTIfGroupRowStatus_Type()
)
cnSLC5COTIfGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTIfGroupRowStatus.setStatus("current")
_CnSLC5COTLinkTable_Object = MibTable
cnSLC5COTLinkTable = _CnSLC5COTLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    cnSLC5COTLinkTable.setStatus("current")
_CnSLC5COTLinkEntry_Object = MibTableRow
cnSLC5COTLinkEntry = _CnSLC5COTLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 2, 1)
)
cnSLC5COTLinkEntry.setIndexNames(
    (0, "CEM-SLC5COT", "cnSLC5COTLinkIfGroupIndex"),
    (0, "CEM-SLC5COT", "cnSLC5COTLinkIfIndex"),
)
if mibBuilder.loadTexts:
    cnSLC5COTLinkEntry.setStatus("current")
_CnSLC5COTLinkIfGroupIndex_Type = CnIfGroupIndexRange
_CnSLC5COTLinkIfGroupIndex_Object = MibTableColumn
cnSLC5COTLinkIfGroupIndex = _CnSLC5COTLinkIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 2, 1, 1),
    _CnSLC5COTLinkIfGroupIndex_Type()
)
cnSLC5COTLinkIfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTLinkIfGroupIndex.setStatus("current")
_CnSLC5COTLinkIfIndex_Type = InterfaceIndex
_CnSLC5COTLinkIfIndex_Object = MibTableColumn
cnSLC5COTLinkIfIndex = _CnSLC5COTLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 2, 1, 2),
    _CnSLC5COTLinkIfIndex_Type()
)
cnSLC5COTLinkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTLinkIfIndex.setStatus("current")
_CnSLC5COTLinkType_Type = CnIfGroupLinkType
_CnSLC5COTLinkType_Object = MibTableColumn
cnSLC5COTLinkType = _CnSLC5COTLinkType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 2, 1, 3),
    _CnSLC5COTLinkType_Type()
)
cnSLC5COTLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTLinkType.setStatus("current")
_CnSLC5COTLinkConfigStatus_Type = Cn1000ConfigurationStatus
_CnSLC5COTLinkConfigStatus_Object = MibTableColumn
cnSLC5COTLinkConfigStatus = _CnSLC5COTLinkConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 2, 1, 4),
    _CnSLC5COTLinkConfigStatus_Type()
)
cnSLC5COTLinkConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnSLC5COTLinkConfigStatus.setStatus("current")
_CnSLC5COTLinkRowStatus_Type = RowStatus
_CnSLC5COTLinkRowStatus_Object = MibTableColumn
cnSLC5COTLinkRowStatus = _CnSLC5COTLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 2, 1, 5),
    _CnSLC5COTLinkRowStatus_Type()
)
cnSLC5COTLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSLC5COTLinkRowStatus.setStatus("current")

# Managed Objects groups

cnSLC5COTObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6, 1, 3)
)
cnSLC5COTObjectsGroup.setObjects(
      *(("CEM-SLC5COT", "cnSLC5COTIfGroupShelf"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupSlotGroup"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupIndex"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupConnectionIndex"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupDescription"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupConfigStatus"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupF1Cable"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupF1PairRangeStart"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupF1PairRangeEnd"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupRowStatus"),
        ("CEM-SLC5COT", "cnSLC5COTLinkIfGroupIndex"),
        ("CEM-SLC5COT", "cnSLC5COTLinkIfIndex"),
        ("CEM-SLC5COT", "cnSLC5COTLinkType"),
        ("CEM-SLC5COT", "cnSLC5COTLinkConfigStatus"),
        ("CEM-SLC5COT", "cnSLC5COTLinkRowStatus"),
        ("CEM-SLC5COT", "cnSLC5COTIfGroupAdminState"))
)
if mibBuilder.loadTexts:
    cnSLC5COTObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-SLC5COT",
    **{"cnSLC5COT": cnSLC5COT,
       "cnSLC5COTModule": cnSLC5COTModule,
       "cnSLC5COTIfGroupConfigTable": cnSLC5COTIfGroupConfigTable,
       "cnSLC5COTIfGroupConfigEntry": cnSLC5COTIfGroupConfigEntry,
       "cnSLC5COTIfGroupShelf": cnSLC5COTIfGroupShelf,
       "cnSLC5COTIfGroupSlotGroup": cnSLC5COTIfGroupSlotGroup,
       "cnSLC5COTIfGroupIndex": cnSLC5COTIfGroupIndex,
       "cnSLC5COTIfGroupConnectionIndex": cnSLC5COTIfGroupConnectionIndex,
       "cnSLC5COTIfGroupAdminState": cnSLC5COTIfGroupAdminState,
       "cnSLC5COTIfGroupDescription": cnSLC5COTIfGroupDescription,
       "cnSLC5COTIfGroupConfigStatus": cnSLC5COTIfGroupConfigStatus,
       "cnSLC5COTIfGroupF1Cable": cnSLC5COTIfGroupF1Cable,
       "cnSLC5COTIfGroupF1PairRangeStart": cnSLC5COTIfGroupF1PairRangeStart,
       "cnSLC5COTIfGroupF1PairRangeEnd": cnSLC5COTIfGroupF1PairRangeEnd,
       "cnSLC5COTIfGroupRowStatus": cnSLC5COTIfGroupRowStatus,
       "cnSLC5COTLinkTable": cnSLC5COTLinkTable,
       "cnSLC5COTLinkEntry": cnSLC5COTLinkEntry,
       "cnSLC5COTLinkIfGroupIndex": cnSLC5COTLinkIfGroupIndex,
       "cnSLC5COTLinkIfIndex": cnSLC5COTLinkIfIndex,
       "cnSLC5COTLinkType": cnSLC5COTLinkType,
       "cnSLC5COTLinkConfigStatus": cnSLC5COTLinkConfigStatus,
       "cnSLC5COTLinkRowStatus": cnSLC5COTLinkRowStatus,
       "cnSLC5COTObjectsGroup": cnSLC5COTObjectsGroup}
)
