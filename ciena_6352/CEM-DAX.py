# SNMP MIB module (CEM-DAX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-DAX.mib
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

(Cn1000ConfigurationStatus,) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "Cn1000ConfigurationStatus")

(CnIfGroupIndexRange,
 cnDAX) = mibBuilder.importSymbols(
    "CEM-INTERFACES",
    "CnIfGroupIndexRange",
    "cnDAX")

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

cnDAXModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnDAXIfGroupConfigTable_Object = MibTable
cnDAXIfGroupConfigTable = _CnDAXIfGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    cnDAXIfGroupConfigTable.setStatus("current")
_CnDAXIfGroupConfigEntry_Object = MibTableRow
cnDAXIfGroupConfigEntry = _CnDAXIfGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1)
)
cnDAXIfGroupConfigEntry.setIndexNames(
    (0, "CEM-DAX", "cnDAXIfGroupIndex"),
)
if mibBuilder.loadTexts:
    cnDAXIfGroupConfigEntry.setStatus("current")
_CnDAXIfGroupShelf_Type = InterfaceIndex
_CnDAXIfGroupShelf_Object = MibTableColumn
cnDAXIfGroupShelf = _CnDAXIfGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1, 1),
    _CnDAXIfGroupShelf_Type()
)
cnDAXIfGroupShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXIfGroupShelf.setStatus("current")
_CnDAXIfGroupSlotGroup_Type = CnSlotGroupNameType
_CnDAXIfGroupSlotGroup_Object = MibTableColumn
cnDAXIfGroupSlotGroup = _CnDAXIfGroupSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1, 2),
    _CnDAXIfGroupSlotGroup_Type()
)
cnDAXIfGroupSlotGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXIfGroupSlotGroup.setStatus("current")
_CnDAXIfGroupIndex_Type = CnIfGroupIndexRange
_CnDAXIfGroupIndex_Object = MibTableColumn
cnDAXIfGroupIndex = _CnDAXIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1, 3),
    _CnDAXIfGroupIndex_Type()
)
cnDAXIfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXIfGroupIndex.setStatus("current")


class _CnDAXIfGroupConnectionIndex_Type(Integer32):
    """Custom type cnDAXIfGroupConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_CnDAXIfGroupConnectionIndex_Type.__name__ = "Integer32"
_CnDAXIfGroupConnectionIndex_Object = MibTableColumn
cnDAXIfGroupConnectionIndex = _CnDAXIfGroupConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1, 4),
    _CnDAXIfGroupConnectionIndex_Type()
)
cnDAXIfGroupConnectionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXIfGroupConnectionIndex.setStatus("current")


class _CnDAXIfGroupDescription_Type(OctetString):
    """Custom type cnDAXIfGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CnDAXIfGroupDescription_Type.__name__ = "OctetString"
_CnDAXIfGroupDescription_Object = MibTableColumn
cnDAXIfGroupDescription = _CnDAXIfGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1, 5),
    _CnDAXIfGroupDescription_Type()
)
cnDAXIfGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXIfGroupDescription.setStatus("current")


class _CnDAXIfGroupAdminState_Type(Integer32):
    """Custom type cnDAXIfGroupAdminState based on Integer32"""
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


_CnDAXIfGroupAdminState_Type.__name__ = "Integer32"
_CnDAXIfGroupAdminState_Object = MibTableColumn
cnDAXIfGroupAdminState = _CnDAXIfGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1, 6),
    _CnDAXIfGroupAdminState_Type()
)
cnDAXIfGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXIfGroupAdminState.setStatus("current")
_CnDAXIfGroupConfigStatus_Type = Cn1000ConfigurationStatus
_CnDAXIfGroupConfigStatus_Object = MibTableColumn
cnDAXIfGroupConfigStatus = _CnDAXIfGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1, 7),
    _CnDAXIfGroupConfigStatus_Type()
)
cnDAXIfGroupConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDAXIfGroupConfigStatus.setStatus("current")
_CnDAXIfGroupRowStatus_Type = RowStatus
_CnDAXIfGroupRowStatus_Object = MibTableColumn
cnDAXIfGroupRowStatus = _CnDAXIfGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 1, 1, 8),
    _CnDAXIfGroupRowStatus_Type()
)
cnDAXIfGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXIfGroupRowStatus.setStatus("current")
_CnDAXLinkTable_Object = MibTable
cnDAXLinkTable = _CnDAXLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    cnDAXLinkTable.setStatus("current")
_CnDAXLinkEntry_Object = MibTableRow
cnDAXLinkEntry = _CnDAXLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 2, 1)
)
cnDAXLinkEntry.setIndexNames(
    (0, "CEM-DAX", "cnDAXLinkIfGroupIndex"),
    (0, "CEM-DAX", "cnDAXLinkIfIndex"),
)
if mibBuilder.loadTexts:
    cnDAXLinkEntry.setStatus("current")
_CnDAXLinkIfGroupIndex_Type = CnIfGroupIndexRange
_CnDAXLinkIfGroupIndex_Object = MibTableColumn
cnDAXLinkIfGroupIndex = _CnDAXLinkIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 2, 1, 1),
    _CnDAXLinkIfGroupIndex_Type()
)
cnDAXLinkIfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXLinkIfGroupIndex.setStatus("current")
_CnDAXLinkIfIndex_Type = InterfaceIndex
_CnDAXLinkIfIndex_Object = MibTableColumn
cnDAXLinkIfIndex = _CnDAXLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 2, 1, 2),
    _CnDAXLinkIfIndex_Type()
)
cnDAXLinkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXLinkIfIndex.setStatus("current")


class _CnDAXLinkLogicalNumber_Type(Integer32):
    """Custom type cnDAXLinkLogicalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CnDAXLinkLogicalNumber_Type.__name__ = "Integer32"
_CnDAXLinkLogicalNumber_Object = MibTableColumn
cnDAXLinkLogicalNumber = _CnDAXLinkLogicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 2, 1, 3),
    _CnDAXLinkLogicalNumber_Type()
)
cnDAXLinkLogicalNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXLinkLogicalNumber.setStatus("current")
_CnDAXLinkConfigStatus_Type = Cn1000ConfigurationStatus
_CnDAXLinkConfigStatus_Object = MibTableColumn
cnDAXLinkConfigStatus = _CnDAXLinkConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 2, 1, 4),
    _CnDAXLinkConfigStatus_Type()
)
cnDAXLinkConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDAXLinkConfigStatus.setStatus("current")
_CnDAXLinkRowStatus_Type = RowStatus
_CnDAXLinkRowStatus_Object = MibTableColumn
cnDAXLinkRowStatus = _CnDAXLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 2, 1, 5),
    _CnDAXLinkRowStatus_Type()
)
cnDAXLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDAXLinkRowStatus.setStatus("current")

# Managed Objects groups

cnDAXObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8, 1, 3)
)
cnDAXObjectsGroup.setObjects(
      *(("CEM-DAX", "cnDAXIfGroupShelf"),
        ("CEM-DAX", "cnDAXIfGroupSlotGroup"),
        ("CEM-DAX", "cnDAXIfGroupIndex"),
        ("CEM-DAX", "cnDAXIfGroupConnectionIndex"),
        ("CEM-DAX", "cnDAXIfGroupDescription"),
        ("CEM-DAX", "cnDAXIfGroupConfigStatus"),
        ("CEM-DAX", "cnDAXIfGroupRowStatus"),
        ("CEM-DAX", "cnDAXLinkIfGroupIndex"),
        ("CEM-DAX", "cnDAXLinkIfIndex"),
        ("CEM-DAX", "cnDAXLinkLogicalNumber"),
        ("CEM-DAX", "cnDAXLinkConfigStatus"),
        ("CEM-DAX", "cnDAXLinkRowStatus"),
        ("CEM-DAX", "cnDAXIfGroupAdminState"))
)
if mibBuilder.loadTexts:
    cnDAXObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-DAX",
    **{"cnDAXModule": cnDAXModule,
       "cnDAXIfGroupConfigTable": cnDAXIfGroupConfigTable,
       "cnDAXIfGroupConfigEntry": cnDAXIfGroupConfigEntry,
       "cnDAXIfGroupShelf": cnDAXIfGroupShelf,
       "cnDAXIfGroupSlotGroup": cnDAXIfGroupSlotGroup,
       "cnDAXIfGroupIndex": cnDAXIfGroupIndex,
       "cnDAXIfGroupConnectionIndex": cnDAXIfGroupConnectionIndex,
       "cnDAXIfGroupDescription": cnDAXIfGroupDescription,
       "cnDAXIfGroupAdminState": cnDAXIfGroupAdminState,
       "cnDAXIfGroupConfigStatus": cnDAXIfGroupConfigStatus,
       "cnDAXIfGroupRowStatus": cnDAXIfGroupRowStatus,
       "cnDAXLinkTable": cnDAXLinkTable,
       "cnDAXLinkEntry": cnDAXLinkEntry,
       "cnDAXLinkIfGroupIndex": cnDAXLinkIfGroupIndex,
       "cnDAXLinkIfIndex": cnDAXLinkIfIndex,
       "cnDAXLinkLogicalNumber": cnDAXLinkLogicalNumber,
       "cnDAXLinkConfigStatus": cnDAXLinkConfigStatus,
       "cnDAXLinkRowStatus": cnDAXLinkRowStatus,
       "cnDAXObjectsGroup": cnDAXObjectsGroup}
)
