# SNMP MIB module (CEM-METALLIC-INTERFACE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-METALLIC-INTERFACE.mib
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
 cnInterfacesModule) = mibBuilder.importSymbols(
    "CEM-INTERFACES",
    "CnIfGroupIndexRange",
    "cnInterfacesModule")

(CnSlotGroupNameType,) = mibBuilder.importSymbols(
    "CEM-TEXTUAL-CONVENTIONS",
    "CnSlotGroupNameType")

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

cnMetallicInterfaceModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnMetallicInterface_ObjectIdentity = ObjectIdentity
cnMetallicInterface = _CnMetallicInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7)
)
_CnMetallicInterfaceTable_Object = MibTable
cnMetallicInterfaceTable = _CnMetallicInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    cnMetallicInterfaceTable.setStatus("current")
_CnMetallicInterfaceEntry_Object = MibTableRow
cnMetallicInterfaceEntry = _CnMetallicInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1)
)
cnMetallicInterfaceEntry.setIndexNames(
    (0, "CEM-METALLIC-INTERFACE", "cnMetallicInterfaceIfGroupIndex"),
    (0, "CEM-METALLIC-INTERFACE", "cnMetallicInterfaceBypassPair"),
    (0, "CEM-METALLIC-INTERFACE", "cnMetallicInterfaceRemoteTerminal"),
)
if mibBuilder.loadTexts:
    cnMetallicInterfaceEntry.setStatus("current")
_CnMetallicInterfaceIfGroupShelf_Type = Cn1000ShelfRange
_CnMetallicInterfaceIfGroupShelf_Object = MibTableColumn
cnMetallicInterfaceIfGroupShelf = _CnMetallicInterfaceIfGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1, 1),
    _CnMetallicInterfaceIfGroupShelf_Type()
)
cnMetallicInterfaceIfGroupShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMetallicInterfaceIfGroupShelf.setStatus("current")
_CnMetallicInterfaceIfGroupSlotGroup_Type = CnSlotGroupNameType
_CnMetallicInterfaceIfGroupSlotGroup_Object = MibTableColumn
cnMetallicInterfaceIfGroupSlotGroup = _CnMetallicInterfaceIfGroupSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1, 2),
    _CnMetallicInterfaceIfGroupSlotGroup_Type()
)
cnMetallicInterfaceIfGroupSlotGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMetallicInterfaceIfGroupSlotGroup.setStatus("current")
_CnMetallicInterfaceIfGroupIndex_Type = CnIfGroupIndexRange
_CnMetallicInterfaceIfGroupIndex_Object = MibTableColumn
cnMetallicInterfaceIfGroupIndex = _CnMetallicInterfaceIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1, 3),
    _CnMetallicInterfaceIfGroupIndex_Type()
)
cnMetallicInterfaceIfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMetallicInterfaceIfGroupIndex.setStatus("current")
_CnMetallicInterfaceRemoteTerminal_Type = IpAddress
_CnMetallicInterfaceRemoteTerminal_Object = MibTableColumn
cnMetallicInterfaceRemoteTerminal = _CnMetallicInterfaceRemoteTerminal_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1, 4),
    _CnMetallicInterfaceRemoteTerminal_Type()
)
cnMetallicInterfaceRemoteTerminal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMetallicInterfaceRemoteTerminal.setStatus("current")


class _CnMetallicInterfaceRemoteTestAccessPort_Type(Integer32):
    """Custom type cnMetallicInterfaceRemoteTestAccessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CnMetallicInterfaceRemoteTestAccessPort_Type.__name__ = "Integer32"
_CnMetallicInterfaceRemoteTestAccessPort_Object = MibTableColumn
cnMetallicInterfaceRemoteTestAccessPort = _CnMetallicInterfaceRemoteTestAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1, 5),
    _CnMetallicInterfaceRemoteTestAccessPort_Type()
)
cnMetallicInterfaceRemoteTestAccessPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMetallicInterfaceRemoteTestAccessPort.setStatus("current")


class _CnMetallicInterfaceBypassPair_Type(Integer32):
    """Custom type cnMetallicInterfaceBypassPair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 384),
    )


_CnMetallicInterfaceBypassPair_Type.__name__ = "Integer32"
_CnMetallicInterfaceBypassPair_Object = MibTableColumn
cnMetallicInterfaceBypassPair = _CnMetallicInterfaceBypassPair_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1, 6),
    _CnMetallicInterfaceBypassPair_Type()
)
cnMetallicInterfaceBypassPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMetallicInterfaceBypassPair.setStatus("current")
_CnMetallicInterfaceConfigStatus_Type = Cn1000ConfigurationStatus
_CnMetallicInterfaceConfigStatus_Object = MibTableColumn
cnMetallicInterfaceConfigStatus = _CnMetallicInterfaceConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1, 7),
    _CnMetallicInterfaceConfigStatus_Type()
)
cnMetallicInterfaceConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMetallicInterfaceConfigStatus.setStatus("current")
_CnMetallicInterfaceRowStatus_Type = RowStatus
_CnMetallicInterfaceRowStatus_Object = MibTableColumn
cnMetallicInterfaceRowStatus = _CnMetallicInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 1, 1, 8),
    _CnMetallicInterfaceRowStatus_Type()
)
cnMetallicInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMetallicInterfaceRowStatus.setStatus("current")

# Managed Objects groups

cnMetallicnterfaceObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7, 1, 2)
)
cnMetallicnterfaceObjectsGroup.setObjects(
      *(("CEM-METALLIC-INTERFACE", "cnMetallicInterfaceIfGroupIndex"),
        ("CEM-METALLIC-INTERFACE", "cnMetallicInterfaceRemoteTerminal"),
        ("CEM-METALLIC-INTERFACE", "cnMetallicInterfaceRemoteTestAccessPort"),
        ("CEM-METALLIC-INTERFACE", "cnMetallicInterfaceBypassPair"),
        ("CEM-METALLIC-INTERFACE", "cnMetallicInterfaceConfigStatus"),
        ("CEM-METALLIC-INTERFACE", "cnMetallicInterfaceRowStatus"),
        ("CEM-METALLIC-INTERFACE", "cnMetallicInterfaceIfGroupShelf"),
        ("CEM-METALLIC-INTERFACE", "cnMetallicInterfaceIfGroupSlotGroup"))
)
if mibBuilder.loadTexts:
    cnMetallicnterfaceObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-METALLIC-INTERFACE",
    **{"cnMetallicInterface": cnMetallicInterface,
       "cnMetallicInterfaceModule": cnMetallicInterfaceModule,
       "cnMetallicInterfaceTable": cnMetallicInterfaceTable,
       "cnMetallicInterfaceEntry": cnMetallicInterfaceEntry,
       "cnMetallicInterfaceIfGroupShelf": cnMetallicInterfaceIfGroupShelf,
       "cnMetallicInterfaceIfGroupSlotGroup": cnMetallicInterfaceIfGroupSlotGroup,
       "cnMetallicInterfaceIfGroupIndex": cnMetallicInterfaceIfGroupIndex,
       "cnMetallicInterfaceRemoteTerminal": cnMetallicInterfaceRemoteTerminal,
       "cnMetallicInterfaceRemoteTestAccessPort": cnMetallicInterfaceRemoteTestAccessPort,
       "cnMetallicInterfaceBypassPair": cnMetallicInterfaceBypassPair,
       "cnMetallicInterfaceConfigStatus": cnMetallicInterfaceConfigStatus,
       "cnMetallicInterfaceRowStatus": cnMetallicInterfaceRowStatus,
       "cnMetallicnterfaceObjectsGroup": cnMetallicnterfaceObjectsGroup}
)
