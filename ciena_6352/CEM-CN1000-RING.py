# SNMP MIB module (CEM-CN1000-RING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-RING.mib
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnCN1000RingModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RxDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("west", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Cn1000RingTable_Object = MibTable
cn1000RingTable = _Cn1000RingTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 1)
)
if mibBuilder.loadTexts:
    cn1000RingTable.setStatus("current")
_Cn1000RingEntry_Object = MibTableRow
cn1000RingEntry = _Cn1000RingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 1, 1)
)
cn1000RingEntry.setIndexNames(
    (0, "CEM-CN1000-RING", "cn1000RingID"),
)
if mibBuilder.loadTexts:
    cn1000RingEntry.setStatus("current")


class _Cn1000RingID_Type(Integer32):
    """Custom type cn1000RingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Cn1000RingID_Type.__name__ = "Integer32"
_Cn1000RingID_Object = MibTableColumn
cn1000RingID = _Cn1000RingID_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 1, 1, 1),
    _Cn1000RingID_Type()
)
cn1000RingID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000RingID.setStatus("current")


class _Cn1000RingMaster_Type(Integer32):
    """Custom type cn1000RingMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Cn1000RingMaster_Type.__name__ = "Integer32"
_Cn1000RingMaster_Object = MibTableColumn
cn1000RingMaster = _Cn1000RingMaster_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 1, 1, 2),
    _Cn1000RingMaster_Type()
)
cn1000RingMaster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000RingMaster.setStatus("current")


class _Cn1000RingName_Type(OctetString):
    """Custom type cn1000RingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000RingName_Type.__name__ = "OctetString"
_Cn1000RingName_Object = MibTableColumn
cn1000RingName = _Cn1000RingName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 1, 1, 3),
    _Cn1000RingName_Type()
)
cn1000RingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000RingName.setStatus("current")
_Cn1000RingRowStatus_Type = RowStatus
_Cn1000RingRowStatus_Object = MibTableColumn
cn1000RingRowStatus = _Cn1000RingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 1, 1, 4),
    _Cn1000RingRowStatus_Type()
)
cn1000RingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000RingRowStatus.setStatus("current")
_Cn1000RingPortTable_Object = MibTable
cn1000RingPortTable = _Cn1000RingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2)
)
if mibBuilder.loadTexts:
    cn1000RingPortTable.setStatus("current")
_Cn1000RingPortEntry_Object = MibTableRow
cn1000RingPortEntry = _Cn1000RingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2, 1)
)
cn1000RingPortEntry.setIndexNames(
    (0, "CEM-CN1000-RING", "cn1000RingPortIfIndex"),
)
if mibBuilder.loadTexts:
    cn1000RingPortEntry.setStatus("current")
_Cn1000RingPortIfIndex_Type = InterfaceIndex
_Cn1000RingPortIfIndex_Object = MibTableColumn
cn1000RingPortIfIndex = _Cn1000RingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2, 1, 1),
    _Cn1000RingPortIfIndex_Type()
)
cn1000RingPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000RingPortIfIndex.setStatus("current")
_Cn1000RingPortShelf_Type = Integer32
_Cn1000RingPortShelf_Object = MibTableColumn
cn1000RingPortShelf = _Cn1000RingPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2, 1, 2),
    _Cn1000RingPortShelf_Type()
)
cn1000RingPortShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPortShelf.setStatus("current")
_Cn1000RingPortSlotGroup_Type = Integer32
_Cn1000RingPortSlotGroup_Object = MibTableColumn
cn1000RingPortSlotGroup = _Cn1000RingPortSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2, 1, 3),
    _Cn1000RingPortSlotGroup_Type()
)
cn1000RingPortSlotGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPortSlotGroup.setStatus("current")
_Cn1000RingPortPort_Type = Integer32
_Cn1000RingPortPort_Object = MibTableColumn
cn1000RingPortPort = _Cn1000RingPortPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2, 1, 4),
    _Cn1000RingPortPort_Type()
)
cn1000RingPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPortPort.setStatus("current")
_Cn1000RingPortRingId_Type = Integer32
_Cn1000RingPortRingId_Object = MibTableColumn
cn1000RingPortRingId = _Cn1000RingPortRingId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2, 1, 5),
    _Cn1000RingPortRingId_Type()
)
cn1000RingPortRingId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000RingPortRingId.setStatus("current")
_Cn1000RingPortRingMaster_Type = TruthValue
_Cn1000RingPortRingMaster_Object = MibTableColumn
cn1000RingPortRingMaster = _Cn1000RingPortRingMaster_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2, 1, 6),
    _Cn1000RingPortRingMaster_Type()
)
cn1000RingPortRingMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPortRingMaster.setStatus("current")
_Cn1000RingPortRowStatus_Type = RowStatus
_Cn1000RingPortRowStatus_Object = MibTableColumn
cn1000RingPortRowStatus = _Cn1000RingPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 2, 1, 7),
    _Cn1000RingPortRowStatus_Type()
)
cn1000RingPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000RingPortRowStatus.setStatus("current")
_Cn1000RingPortPathTable_Object = MibTable
cn1000RingPortPathTable = _Cn1000RingPortPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3)
)
if mibBuilder.loadTexts:
    cn1000RingPortPathTable.setStatus("current")
_Cn1000RingPortPathEntry_Object = MibTableRow
cn1000RingPortPathEntry = _Cn1000RingPortPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1)
)
cn1000RingPortPathEntry.setIndexNames(
    (0, "CEM-CN1000-RING", "cn1000RingPortPathIfindex"),
    (0, "CEM-CN1000-RING", "cn1000RingPortPathVpi"),
)
if mibBuilder.loadTexts:
    cn1000RingPortPathEntry.setStatus("current")
_Cn1000RingPortPathIfindex_Type = InterfaceIndex
_Cn1000RingPortPathIfindex_Object = MibTableColumn
cn1000RingPortPathIfindex = _Cn1000RingPortPathIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1, 1),
    _Cn1000RingPortPathIfindex_Type()
)
cn1000RingPortPathIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000RingPortPathIfindex.setStatus("current")
_Cn1000RingPortPathShelf_Type = Integer32
_Cn1000RingPortPathShelf_Object = MibTableColumn
cn1000RingPortPathShelf = _Cn1000RingPortPathShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1, 2),
    _Cn1000RingPortPathShelf_Type()
)
cn1000RingPortPathShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPortPathShelf.setStatus("current")
_Cn1000RingPortPathSlotGroup_Type = Integer32
_Cn1000RingPortPathSlotGroup_Object = MibTableColumn
cn1000RingPortPathSlotGroup = _Cn1000RingPortPathSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1, 3),
    _Cn1000RingPortPathSlotGroup_Type()
)
cn1000RingPortPathSlotGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPortPathSlotGroup.setStatus("current")
_Cn1000RingPortPathPort_Type = Integer32
_Cn1000RingPortPathPort_Object = MibTableColumn
cn1000RingPortPathPort = _Cn1000RingPortPathPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1, 4),
    _Cn1000RingPortPathPort_Type()
)
cn1000RingPortPathPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPortPathPort.setStatus("current")


class _Cn1000RingPortPathVpi_Type(Integer32):
    """Custom type cn1000RingPortPathVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000RingPortPathVpi_Type.__name__ = "Integer32"
_Cn1000RingPortPathVpi_Object = MibTableColumn
cn1000RingPortPathVpi = _Cn1000RingPortPathVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1, 5),
    _Cn1000RingPortPathVpi_Type()
)
cn1000RingPortPathVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000RingPortPathVpi.setStatus("current")
_Cn1000RingPortPathRxDir_Type = RxDirection
_Cn1000RingPortPathRxDir_Object = MibTableColumn
cn1000RingPortPathRxDir = _Cn1000RingPortPathRxDir_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1, 6),
    _Cn1000RingPortPathRxDir_Type()
)
cn1000RingPortPathRxDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000RingPortPathRxDir.setStatus("current")


class _Cn1000RingPortPathStatus_Type(Integer32):
    """Custom type cn1000RingPortPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_Cn1000RingPortPathStatus_Type.__name__ = "Integer32"
_Cn1000RingPortPathStatus_Object = MibTableColumn
cn1000RingPortPathStatus = _Cn1000RingPortPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1, 7),
    _Cn1000RingPortPathStatus_Type()
)
cn1000RingPortPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPortPathStatus.setStatus("current")
_Cn1000RingPortPathRowStatus_Type = RowStatus
_Cn1000RingPortPathRowStatus_Object = MibTableColumn
cn1000RingPortPathRowStatus = _Cn1000RingPortPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 3, 1, 8),
    _Cn1000RingPortPathRowStatus_Type()
)
cn1000RingPortPathRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000RingPortPathRowStatus.setStatus("current")
_Cn1000RingPathTable_Object = MibTable
cn1000RingPathTable = _Cn1000RingPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 4)
)
if mibBuilder.loadTexts:
    cn1000RingPathTable.setStatus("current")
_Cn1000RingPathEntry_Object = MibTableRow
cn1000RingPathEntry = _Cn1000RingPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 4, 1)
)
cn1000RingPathEntry.setIndexNames(
    (0, "CEM-CN1000-RING", "cn1000RingPathRingId"),
    (0, "CEM-CN1000-RING", "cn1000RingPathVpi"),
)
if mibBuilder.loadTexts:
    cn1000RingPathEntry.setStatus("current")


class _Cn1000RingPathRingId_Type(Integer32):
    """Custom type cn1000RingPathRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Cn1000RingPathRingId_Type.__name__ = "Integer32"
_Cn1000RingPathRingId_Object = MibTableColumn
cn1000RingPathRingId = _Cn1000RingPathRingId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 4, 1, 1),
    _Cn1000RingPathRingId_Type()
)
cn1000RingPathRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000RingPathRingId.setStatus("current")


class _Cn1000RingPathVpi_Type(Integer32):
    """Custom type cn1000RingPathVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000RingPathVpi_Type.__name__ = "Integer32"
_Cn1000RingPathVpi_Object = MibTableColumn
cn1000RingPathVpi = _Cn1000RingPathVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 4, 1, 2),
    _Cn1000RingPathVpi_Type()
)
cn1000RingPathVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000RingPathVpi.setStatus("current")
_Cn1000RingPathNodeA_Type = Integer32
_Cn1000RingPathNodeA_Object = MibTableColumn
cn1000RingPathNodeA = _Cn1000RingPathNodeA_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 4, 1, 3),
    _Cn1000RingPathNodeA_Type()
)
cn1000RingPathNodeA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPathNodeA.setStatus("current")
_Cn1000RingPathLocationA_Type = Integer32
_Cn1000RingPathLocationA_Object = MibTableColumn
cn1000RingPathLocationA = _Cn1000RingPathLocationA_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 4, 1, 4),
    _Cn1000RingPathLocationA_Type()
)
cn1000RingPathLocationA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPathLocationA.setStatus("current")
_Cn1000RingPathNodeB_Type = Integer32
_Cn1000RingPathNodeB_Object = MibTableColumn
cn1000RingPathNodeB = _Cn1000RingPathNodeB_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 4, 1, 5),
    _Cn1000RingPathNodeB_Type()
)
cn1000RingPathNodeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPathNodeB.setStatus("current")
_Cn1000RingPathLocationB_Type = Integer32
_Cn1000RingPathLocationB_Object = MibTableColumn
cn1000RingPathLocationB = _Cn1000RingPathLocationB_Object(
    (1, 3, 6, 1, 4, 1, 6352, 27, 4, 1, 6),
    _Cn1000RingPathLocationB_Type()
)
cn1000RingPathLocationB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000RingPathLocationB.setStatus("current")

# Managed Objects groups

cn100010RingObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 27, 5)
)
cn100010RingObjectGroup.setObjects(
      *(("CEM-CN1000-RING", "cn1000RingPortShelf"),
        ("CEM-CN1000-RING", "cn1000RingPortSlotGroup"),
        ("CEM-CN1000-RING", "cn1000RingPortPort"),
        ("CEM-CN1000-RING", "cn1000RingPortRingId"),
        ("CEM-CN1000-RING", "cn1000RingPortPathPort"),
        ("CEM-CN1000-RING", "cn1000RingPortPathSlotGroup"),
        ("CEM-CN1000-RING", "cn1000RingPortPathShelf"),
        ("CEM-CN1000-RING", "cn1000RingPortPathRowStatus"),
        ("CEM-CN1000-RING", "cn1000RingPathLocationB"),
        ("CEM-CN1000-RING", "cn1000RingPathNodeB"),
        ("CEM-CN1000-RING", "cn1000RingPathLocationA"),
        ("CEM-CN1000-RING", "cn1000RingPathNodeA"),
        ("CEM-CN1000-RING", "cn1000RingPortPathStatus"),
        ("CEM-CN1000-RING", "cn1000RingPortRowStatus"),
        ("CEM-CN1000-RING", "cn1000RingMaster"),
        ("CEM-CN1000-RING", "cn1000RingName"),
        ("CEM-CN1000-RING", "cn1000RingRowStatus"),
        ("CEM-CN1000-RING", "cn1000RingPortRingMaster"),
        ("CEM-CN1000-RING", "cn1000RingPortPathRxDir"))
)
if mibBuilder.loadTexts:
    cn100010RingObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-RING",
    **{"RxDirection": RxDirection,
       "cnCN1000RingModule": cnCN1000RingModule,
       "cn1000RingTable": cn1000RingTable,
       "cn1000RingEntry": cn1000RingEntry,
       "cn1000RingID": cn1000RingID,
       "cn1000RingMaster": cn1000RingMaster,
       "cn1000RingName": cn1000RingName,
       "cn1000RingRowStatus": cn1000RingRowStatus,
       "cn1000RingPortTable": cn1000RingPortTable,
       "cn1000RingPortEntry": cn1000RingPortEntry,
       "cn1000RingPortIfIndex": cn1000RingPortIfIndex,
       "cn1000RingPortShelf": cn1000RingPortShelf,
       "cn1000RingPortSlotGroup": cn1000RingPortSlotGroup,
       "cn1000RingPortPort": cn1000RingPortPort,
       "cn1000RingPortRingId": cn1000RingPortRingId,
       "cn1000RingPortRingMaster": cn1000RingPortRingMaster,
       "cn1000RingPortRowStatus": cn1000RingPortRowStatus,
       "cn1000RingPortPathTable": cn1000RingPortPathTable,
       "cn1000RingPortPathEntry": cn1000RingPortPathEntry,
       "cn1000RingPortPathIfindex": cn1000RingPortPathIfindex,
       "cn1000RingPortPathShelf": cn1000RingPortPathShelf,
       "cn1000RingPortPathSlotGroup": cn1000RingPortPathSlotGroup,
       "cn1000RingPortPathPort": cn1000RingPortPathPort,
       "cn1000RingPortPathVpi": cn1000RingPortPathVpi,
       "cn1000RingPortPathRxDir": cn1000RingPortPathRxDir,
       "cn1000RingPortPathStatus": cn1000RingPortPathStatus,
       "cn1000RingPortPathRowStatus": cn1000RingPortPathRowStatus,
       "cn1000RingPathTable": cn1000RingPathTable,
       "cn1000RingPathEntry": cn1000RingPathEntry,
       "cn1000RingPathRingId": cn1000RingPathRingId,
       "cn1000RingPathVpi": cn1000RingPathVpi,
       "cn1000RingPathNodeA": cn1000RingPathNodeA,
       "cn1000RingPathLocationA": cn1000RingPathLocationA,
       "cn1000RingPathNodeB": cn1000RingPathNodeB,
       "cn1000RingPathLocationB": cn1000RingPathLocationB,
       "cn100010RingObjectGroup": cn100010RingObjectGroup}
)
