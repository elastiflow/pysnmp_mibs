# SNMP MIB module (CEM-CENTRALIZED-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CENTRALIZED-MANAGEMENT-MIB.mib
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

(atmTrafficDescrParamEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamEntry")

(AtmServiceCategory,
 AtmTrafficDescrParamIndex) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory",
    "AtmTrafficDescrParamIndex")

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

cnCentralizedManagementModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28)
)
if mibBuilder.loadTexts:
    cnCentralizedManagementModule.setRevisions(
        ("2003-07-03 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CnTopologyNodeId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )



class CnTopologyNodeType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("unknown", 0),
          ("rt", 1),
          ("dcm", 2),
          ("voiceHt", 3),
          ("videoHt", 4),
          ("cnx5-T1", 5),
          ("cnx5-DS3", 6),
          ("atmCloud", 7))
    )


class CnTopologyServiceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2),
          ("video", 3),
          ("management", 4),
          ("crossover", 5),
          ("ringcontrol", 6),
          ("unspecified", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CnTopology_ObjectIdentity = ObjectIdentity
cnTopology = _CnTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1)
)
if mibBuilder.loadTexts:
    cnTopology.setStatus("current")
_CnTopologyMibObjects_ObjectIdentity = ObjectIdentity
cnTopologyMibObjects = _CnTopologyMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1)
)
_CnTopologyLocalNode_ObjectIdentity = ObjectIdentity
cnTopologyLocalNode = _CnTopologyLocalNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnTopologyLocalNode.setStatus("current")
_CnTopologyLocalNodeId_Type = CnTopologyNodeId
_CnTopologyLocalNodeId_Object = MibScalar
cnTopologyLocalNodeId = _CnTopologyLocalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 1, 1),
    _CnTopologyLocalNodeId_Type()
)
cnTopologyLocalNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTopologyLocalNodeId.setStatus("current")
_CnTopologyLocalNodeType_Type = CnTopologyNodeType
_CnTopologyLocalNodeType_Object = MibScalar
cnTopologyLocalNodeType = _CnTopologyLocalNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 1, 2),
    _CnTopologyLocalNodeType_Type()
)
cnTopologyLocalNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTopologyLocalNodeType.setStatus("current")
_CnTopologyLocalMasterIp_Type = IpAddress
_CnTopologyLocalMasterIp_Object = MibScalar
cnTopologyLocalMasterIp = _CnTopologyLocalMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 1, 3),
    _CnTopologyLocalMasterIp_Type()
)
cnTopologyLocalMasterIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTopologyLocalMasterIp.setStatus("current")
_CnTopologyRemoteNodeTable_Object = MibTable
cnTopologyRemoteNodeTable = _CnTopologyRemoteNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnTopologyRemoteNodeTable.setStatus("current")
_CnTopologyRemoteNodeEntry_Object = MibTableRow
cnTopologyRemoteNodeEntry = _CnTopologyRemoteNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 2, 1)
)
cnTopologyRemoteNodeEntry.setIndexNames(
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyRemoteNodeId"),
)
if mibBuilder.loadTexts:
    cnTopologyRemoteNodeEntry.setStatus("current")
_CnTopologyRemoteNodeId_Type = CnTopologyNodeId
_CnTopologyRemoteNodeId_Object = MibTableColumn
cnTopologyRemoteNodeId = _CnTopologyRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 2, 1, 1),
    _CnTopologyRemoteNodeId_Type()
)
cnTopologyRemoteNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyRemoteNodeId.setStatus("current")
_CnTopologyRemoteNodeIpAddress_Type = IpAddress
_CnTopologyRemoteNodeIpAddress_Object = MibTableColumn
cnTopologyRemoteNodeIpAddress = _CnTopologyRemoteNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 2, 1, 5),
    _CnTopologyRemoteNodeIpAddress_Type()
)
cnTopologyRemoteNodeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTopologyRemoteNodeIpAddress.setStatus("current")
_CnTopologyRemoteNodeType_Type = CnTopologyNodeType
_CnTopologyRemoteNodeType_Object = MibTableColumn
cnTopologyRemoteNodeType = _CnTopologyRemoteNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 2, 1, 6),
    _CnTopologyRemoteNodeType_Type()
)
cnTopologyRemoteNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTopologyRemoteNodeType.setStatus("current")
_CnTopologyRemoteNodeDiscovered_Type = CnTopologyNodeType
_CnTopologyRemoteNodeDiscovered_Object = MibTableColumn
cnTopologyRemoteNodeDiscovered = _CnTopologyRemoteNodeDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 2, 1, 7),
    _CnTopologyRemoteNodeDiscovered_Type()
)
cnTopologyRemoteNodeDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTopologyRemoteNodeDiscovered.setStatus("current")


class _CnTopologyRemoteNodeStatus_Type(Integer32):
    """Custom type cnTopologyRemoteNodeStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("configMismatch", 3),
          ("synchronizing", 4),
          ("conflict", 5))
    )


_CnTopologyRemoteNodeStatus_Type.__name__ = "Integer32"
_CnTopologyRemoteNodeStatus_Object = MibTableColumn
cnTopologyRemoteNodeStatus = _CnTopologyRemoteNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 2, 1, 8),
    _CnTopologyRemoteNodeStatus_Type()
)
cnTopologyRemoteNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTopologyRemoteNodeStatus.setStatus("current")
_CnTopologyRemoteNodeRowStatus_Type = RowStatus
_CnTopologyRemoteNodeRowStatus_Object = MibTableColumn
cnTopologyRemoteNodeRowStatus = _CnTopologyRemoteNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 2, 1, 30),
    _CnTopologyRemoteNodeRowStatus_Type()
)
cnTopologyRemoteNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTopologyRemoteNodeRowStatus.setStatus("current")
_CnTopologyPhyConnTable_Object = MibTable
cnTopologyPhyConnTable = _CnTopologyPhyConnTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cnTopologyPhyConnTable.setStatus("current")
_CnTopologyPhyConnEntry_Object = MibTableRow
cnTopologyPhyConnEntry = _CnTopologyPhyConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3, 1)
)
cnTopologyPhyConnEntry.setIndexNames(
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPhyConnNodeIdA"),
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPhyConnIfIndexA"),
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPhyConnNodeIdB"),
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPhyConnIfIndexB"),
)
if mibBuilder.loadTexts:
    cnTopologyPhyConnEntry.setStatus("current")
_CnTopologyPhyConnNodeIdA_Type = CnTopologyNodeId
_CnTopologyPhyConnNodeIdA_Object = MibTableColumn
cnTopologyPhyConnNodeIdA = _CnTopologyPhyConnNodeIdA_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3, 1, 1),
    _CnTopologyPhyConnNodeIdA_Type()
)
cnTopologyPhyConnNodeIdA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPhyConnNodeIdA.setStatus("current")
_CnTopologyPhyConnIfIndexA_Type = InterfaceIndex
_CnTopologyPhyConnIfIndexA_Object = MibTableColumn
cnTopologyPhyConnIfIndexA = _CnTopologyPhyConnIfIndexA_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3, 1, 2),
    _CnTopologyPhyConnIfIndexA_Type()
)
cnTopologyPhyConnIfIndexA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPhyConnIfIndexA.setStatus("current")
_CnTopologyPhyConnNodeIdB_Type = CnTopologyNodeId
_CnTopologyPhyConnNodeIdB_Object = MibTableColumn
cnTopologyPhyConnNodeIdB = _CnTopologyPhyConnNodeIdB_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3, 1, 3),
    _CnTopologyPhyConnNodeIdB_Type()
)
cnTopologyPhyConnNodeIdB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPhyConnNodeIdB.setStatus("current")
_CnTopologyPhyConnIfIndexB_Type = InterfaceIndex
_CnTopologyPhyConnIfIndexB_Object = MibTableColumn
cnTopologyPhyConnIfIndexB = _CnTopologyPhyConnIfIndexB_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3, 1, 4),
    _CnTopologyPhyConnIfIndexB_Type()
)
cnTopologyPhyConnIfIndexB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPhyConnIfIndexB.setStatus("current")


class _CnTopologyPhyConnRingId_Type(Unsigned32):
    """Custom type cnTopologyPhyConnRingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CnTopologyPhyConnRingId_Type.__name__ = "Unsigned32"
_CnTopologyPhyConnRingId_Object = MibTableColumn
cnTopologyPhyConnRingId = _CnTopologyPhyConnRingId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3, 1, 10),
    _CnTopologyPhyConnRingId_Type()
)
cnTopologyPhyConnRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTopologyPhyConnRingId.setStatus("current")


class _CnTopologyPhyConnStatus_Type(Integer32):
    """Custom type cnTopologyPhyConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_CnTopologyPhyConnStatus_Type.__name__ = "Integer32"
_CnTopologyPhyConnStatus_Object = MibTableColumn
cnTopologyPhyConnStatus = _CnTopologyPhyConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3, 1, 11),
    _CnTopologyPhyConnStatus_Type()
)
cnTopologyPhyConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTopologyPhyConnStatus.setStatus("current")
_CnTopologyPhyConnRowStatus_Type = RowStatus
_CnTopologyPhyConnRowStatus_Object = MibTableColumn
cnTopologyPhyConnRowStatus = _CnTopologyPhyConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 3, 1, 30),
    _CnTopologyPhyConnRowStatus_Type()
)
cnTopologyPhyConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTopologyPhyConnRowStatus.setStatus("current")
_CnTopologyPathTable_Object = MibTable
cnTopologyPathTable = _CnTopologyPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cnTopologyPathTable.setStatus("current")
_CnTopologyPathEntry_Object = MibTableRow
cnTopologyPathEntry = _CnTopologyPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1)
)
cnTopologyPathEntry.setIndexNames(
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPathSrcNodeId"),
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPathSrcIfIndex"),
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPathSrcVpi"),
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPathDestNodeId"),
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPathDestIfIndex"),
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopologyPathDestVpi"),
)
if mibBuilder.loadTexts:
    cnTopologyPathEntry.setStatus("current")
_CnTopologyPathSrcNodeId_Type = CnTopologyNodeId
_CnTopologyPathSrcNodeId_Object = MibTableColumn
cnTopologyPathSrcNodeId = _CnTopologyPathSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 1),
    _CnTopologyPathSrcNodeId_Type()
)
cnTopologyPathSrcNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPathSrcNodeId.setStatus("current")
_CnTopologyPathSrcIfIndex_Type = InterfaceIndex
_CnTopologyPathSrcIfIndex_Object = MibTableColumn
cnTopologyPathSrcIfIndex = _CnTopologyPathSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 2),
    _CnTopologyPathSrcIfIndex_Type()
)
cnTopologyPathSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPathSrcIfIndex.setStatus("current")


class _CnTopologyPathSrcVpi_Type(Integer32):
    """Custom type cnTopologyPathSrcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CnTopologyPathSrcVpi_Type.__name__ = "Integer32"
_CnTopologyPathSrcVpi_Object = MibTableColumn
cnTopologyPathSrcVpi = _CnTopologyPathSrcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 3),
    _CnTopologyPathSrcVpi_Type()
)
cnTopologyPathSrcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPathSrcVpi.setStatus("current")
_CnTopologyPathDestNodeId_Type = CnTopologyNodeId
_CnTopologyPathDestNodeId_Object = MibTableColumn
cnTopologyPathDestNodeId = _CnTopologyPathDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 5),
    _CnTopologyPathDestNodeId_Type()
)
cnTopologyPathDestNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPathDestNodeId.setStatus("current")
_CnTopologyPathDestIfIndex_Type = InterfaceIndex
_CnTopologyPathDestIfIndex_Object = MibTableColumn
cnTopologyPathDestIfIndex = _CnTopologyPathDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 6),
    _CnTopologyPathDestIfIndex_Type()
)
cnTopologyPathDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPathDestIfIndex.setStatus("current")


class _CnTopologyPathDestVpi_Type(Integer32):
    """Custom type cnTopologyPathDestVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CnTopologyPathDestVpi_Type.__name__ = "Integer32"
_CnTopologyPathDestVpi_Object = MibTableColumn
cnTopologyPathDestVpi = _CnTopologyPathDestVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 7),
    _CnTopologyPathDestVpi_Type()
)
cnTopologyPathDestVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTopologyPathDestVpi.setStatus("current")


class _CnTopologyPathServiceType_Type(CnTopologyServiceType):
    """Custom type cnTopologyPathServiceType based on CnTopologyServiceType"""
    defaultValue = 1


_CnTopologyPathServiceType_Type.__name__ = "CnTopologyServiceType"
_CnTopologyPathServiceType_Object = MibTableColumn
cnTopologyPathServiceType = _CnTopologyPathServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 10),
    _CnTopologyPathServiceType_Type()
)
cnTopologyPathServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTopologyPathServiceType.setStatus("current")


class _CnTopologyPathServiceCategory_Type(AtmServiceCategory):
    """Custom type cnTopologyPathServiceCategory based on AtmServiceCategory"""
    defaultValue = 6


_CnTopologyPathServiceCategory_Type.__name__ = "AtmServiceCategory"
_CnTopologyPathServiceCategory_Object = MibTableColumn
cnTopologyPathServiceCategory = _CnTopologyPathServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 11),
    _CnTopologyPathServiceCategory_Type()
)
cnTopologyPathServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTopologyPathServiceCategory.setStatus("current")


class _CnTopologyPathReceiveTrafficDescrIndex_Type(Integer32):
    """Custom type cnTopologyPathReceiveTrafficDescrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CnTopologyPathReceiveTrafficDescrIndex_Type.__name__ = "Integer32"
_CnTopologyPathReceiveTrafficDescrIndex_Object = MibTableColumn
cnTopologyPathReceiveTrafficDescrIndex = _CnTopologyPathReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 15),
    _CnTopologyPathReceiveTrafficDescrIndex_Type()
)
cnTopologyPathReceiveTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTopologyPathReceiveTrafficDescrIndex.setStatus("current")


class _CnTopologyPathTransmitTrafficDescrIndex_Type(Integer32):
    """Custom type cnTopologyPathTransmitTrafficDescrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CnTopologyPathTransmitTrafficDescrIndex_Type.__name__ = "Integer32"
_CnTopologyPathTransmitTrafficDescrIndex_Object = MibTableColumn
cnTopologyPathTransmitTrafficDescrIndex = _CnTopologyPathTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 16),
    _CnTopologyPathTransmitTrafficDescrIndex_Type()
)
cnTopologyPathTransmitTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnTopologyPathTransmitTrafficDescrIndex.setStatus("current")


class _CnTopologyPathStatus_Type(Integer32):
    """Custom type cnTopologyPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_CnTopologyPathStatus_Type.__name__ = "Integer32"
_CnTopologyPathStatus_Object = MibTableColumn
cnTopologyPathStatus = _CnTopologyPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 17),
    _CnTopologyPathStatus_Type()
)
cnTopologyPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTopologyPathStatus.setStatus("current")
_CnTopologyPathRowStatus_Type = RowStatus
_CnTopologyPathRowStatus_Object = MibTableColumn
cnTopologyPathRowStatus = _CnTopologyPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 1, 4, 1, 30),
    _CnTopologyPathRowStatus_Type()
)
cnTopologyPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTopologyPathRowStatus.setStatus("current")
_CnTopologyNotifications_ObjectIdentity = ObjectIdentity
cnTopologyNotifications = _CnTopologyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 2)
)
_CnTopologyConformance_ObjectIdentity = ObjectIdentity
cnTopologyConformance = _CnTopologyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 3)
)
_CnTopologyGroups_ObjectIdentity = ObjectIdentity
cnTopologyGroups = _CnTopologyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 3, 1)
)
_CnTopologyCompliances_ObjectIdentity = ObjectIdentity
cnTopologyCompliances = _CnTopologyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 3, 2)
)
_CnATMServiceConnection_ObjectIdentity = ObjectIdentity
cnATMServiceConnection = _CnATMServiceConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2)
)
if mibBuilder.loadTexts:
    cnATMServiceConnection.setStatus("current")


class _CnAtmSCIndexNext_Type(Integer32):
    """Custom type cnAtmSCIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnAtmSCIndexNext_Type.__name__ = "Integer32"
_CnAtmSCIndexNext_Object = MibScalar
cnAtmSCIndexNext = _CnAtmSCIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 1),
    _CnAtmSCIndexNext_Type()
)
cnAtmSCIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmSCIndexNext.setStatus("current")
_CnAtmSCResultTables_ObjectIdentity = ObjectIdentity
cnAtmSCResultTables = _CnAtmSCResultTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 2)
)
_CnAtmSCResultTable_Object = MibTable
cnAtmSCResultTable = _CnAtmSCResultTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cnAtmSCResultTable.setStatus("current")
_CnAtmSCResultEntry_Object = MibTableRow
cnAtmSCResultEntry = _CnAtmSCResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 2, 1, 1)
)
cnAtmSCResultEntry.setIndexNames(
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCResultIndex"),
)
if mibBuilder.loadTexts:
    cnAtmSCResultEntry.setStatus("current")


class _CnAtmSCResultIndex_Type(Integer32):
    """Custom type cnAtmSCResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnAtmSCResultIndex_Type.__name__ = "Integer32"
_CnAtmSCResultIndex_Object = MibTableColumn
cnAtmSCResultIndex = _CnAtmSCResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 2, 1, 1, 1),
    _CnAtmSCResultIndex_Type()
)
cnAtmSCResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAtmSCResultIndex.setStatus("current")


class _CnAtmSCResultCode_Type(Integer32):
    """Custom type cnAtmSCResultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnAtmSCResultCode_Type.__name__ = "Integer32"
_CnAtmSCResultCode_Object = MibTableColumn
cnAtmSCResultCode = _CnAtmSCResultCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 2, 1, 1, 2),
    _CnAtmSCResultCode_Type()
)
cnAtmSCResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmSCResultCode.setStatus("current")
_CnAtmSCResultText_Type = DisplayString
_CnAtmSCResultText_Object = MibTableColumn
cnAtmSCResultText = _CnAtmSCResultText_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 2, 1, 1, 3),
    _CnAtmSCResultText_Type()
)
cnAtmSCResultText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmSCResultText.setStatus("current")
_CnAtmSCTables_ObjectIdentity = ObjectIdentity
cnAtmSCTables = _CnAtmSCTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3)
)
_CnAtmSCTable_Object = MibTable
cnAtmSCTable = _CnAtmSCTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cnAtmSCTable.setStatus("current")
_CnAtmSCEntry_Object = MibTableRow
cnAtmSCEntry = _CnAtmSCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1)
)
cnAtmSCEntry.setIndexNames(
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCIndex"),
)
if mibBuilder.loadTexts:
    cnAtmSCEntry.setStatus("current")


class _CnAtmSCIndex_Type(Integer32):
    """Custom type cnAtmSCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnAtmSCIndex_Type.__name__ = "Integer32"
_CnAtmSCIndex_Object = MibTableColumn
cnAtmSCIndex = _CnAtmSCIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 1),
    _CnAtmSCIndex_Type()
)
cnAtmSCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAtmSCIndex.setStatus("current")


class _CnAtmSCUSNodeId_Type(Integer32):
    """Custom type cnAtmSCUSNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CnAtmSCUSNodeId_Type.__name__ = "Integer32"
_CnAtmSCUSNodeId_Object = MibTableColumn
cnAtmSCUSNodeId = _CnAtmSCUSNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 2),
    _CnAtmSCUSNodeId_Type()
)
cnAtmSCUSNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCUSNodeId.setStatus("current")
_CnAtmSCUSIfIndex_Type = Integer32
_CnAtmSCUSIfIndex_Object = MibTableColumn
cnAtmSCUSIfIndex = _CnAtmSCUSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 3),
    _CnAtmSCUSIfIndex_Type()
)
cnAtmSCUSIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCUSIfIndex.setStatus("current")


class _CnAtmSCDSNodeId_Type(Integer32):
    """Custom type cnAtmSCDSNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CnAtmSCDSNodeId_Type.__name__ = "Integer32"
_CnAtmSCDSNodeId_Object = MibTableColumn
cnAtmSCDSNodeId = _CnAtmSCDSNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 4),
    _CnAtmSCDSNodeId_Type()
)
cnAtmSCDSNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCDSNodeId.setStatus("current")
_CnAtmSCDSIfIndex_Type = Integer32
_CnAtmSCDSIfIndex_Object = MibTableColumn
cnAtmSCDSIfIndex = _CnAtmSCDSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 5),
    _CnAtmSCDSIfIndex_Type()
)
cnAtmSCDSIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCDSIfIndex.setStatus("current")


class _CnAtmSCUSVclVpi_Type(Integer32):
    """Custom type cnAtmSCUSVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_CnAtmSCUSVclVpi_Type.__name__ = "Integer32"
_CnAtmSCUSVclVpi_Object = MibTableColumn
cnAtmSCUSVclVpi = _CnAtmSCUSVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 6),
    _CnAtmSCUSVclVpi_Type()
)
cnAtmSCUSVclVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCUSVclVpi.setStatus("current")


class _CnAtmSCUSVclVci_Type(Integer32):
    """Custom type cnAtmSCUSVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CnAtmSCUSVclVci_Type.__name__ = "Integer32"
_CnAtmSCUSVclVci_Object = MibTableColumn
cnAtmSCUSVclVci = _CnAtmSCUSVclVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 7),
    _CnAtmSCUSVclVci_Type()
)
cnAtmSCUSVclVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCUSVclVci.setStatus("current")


class _CnAtmSCUSVccAalType_Type(Integer32):
    """Custom type cnAtmSCUSVccAalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("aal34", 2),
          ("aal5", 3),
          ("other", 4),
          ("unknown", 5),
          ("aal2", 6))
    )


_CnAtmSCUSVccAalType_Type.__name__ = "Integer32"
_CnAtmSCUSVccAalType_Object = MibTableColumn
cnAtmSCUSVccAalType = _CnAtmSCUSVccAalType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 8),
    _CnAtmSCUSVccAalType_Type()
)
cnAtmSCUSVccAalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCUSVccAalType.setStatus("current")


class _CnAtmSCDSVclVpi_Type(Integer32):
    """Custom type cnAtmSCDSVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CnAtmSCDSVclVpi_Type.__name__ = "Integer32"
_CnAtmSCDSVclVpi_Object = MibTableColumn
cnAtmSCDSVclVpi = _CnAtmSCDSVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 9),
    _CnAtmSCDSVclVpi_Type()
)
cnAtmSCDSVclVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCDSVclVpi.setStatus("current")


class _CnAtmSCDSVclVci_Type(Integer32):
    """Custom type cnAtmSCDSVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CnAtmSCDSVclVci_Type.__name__ = "Integer32"
_CnAtmSCDSVclVci_Object = MibTableColumn
cnAtmSCDSVclVci = _CnAtmSCDSVclVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 10),
    _CnAtmSCDSVclVci_Type()
)
cnAtmSCDSVclVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCDSVclVci.setStatus("current")


class _CnAtmSCDSVccAalType_Type(Integer32):
    """Custom type cnAtmSCDSVccAalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 1),
          ("aal34", 2),
          ("aal5", 3),
          ("other", 4),
          ("unknown", 5),
          ("aal2", 6))
    )


_CnAtmSCDSVccAalType_Type.__name__ = "Integer32"
_CnAtmSCDSVccAalType_Object = MibTableColumn
cnAtmSCDSVccAalType = _CnAtmSCDSVccAalType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 11),
    _CnAtmSCDSVccAalType_Type()
)
cnAtmSCDSVccAalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCDSVccAalType.setStatus("current")


class _CnAtmSCVclReceiveTrafficDescrIndex_Type(Integer32):
    """Custom type cnAtmSCVclReceiveTrafficDescrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CnAtmSCVclReceiveTrafficDescrIndex_Type.__name__ = "Integer32"
_CnAtmSCVclReceiveTrafficDescrIndex_Object = MibTableColumn
cnAtmSCVclReceiveTrafficDescrIndex = _CnAtmSCVclReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 12),
    _CnAtmSCVclReceiveTrafficDescrIndex_Type()
)
cnAtmSCVclReceiveTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCVclReceiveTrafficDescrIndex.setStatus("current")


class _CnAtmSCVclTransmitTrafficDescrIndex_Type(Integer32):
    """Custom type cnAtmSCVclTransmitTrafficDescrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CnAtmSCVclTransmitTrafficDescrIndex_Type.__name__ = "Integer32"
_CnAtmSCVclTransmitTrafficDescrIndex_Object = MibTableColumn
cnAtmSCVclTransmitTrafficDescrIndex = _CnAtmSCVclTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 13),
    _CnAtmSCVclTransmitTrafficDescrIndex_Type()
)
cnAtmSCVclTransmitTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCVclTransmitTrafficDescrIndex.setStatus("current")


class _CnAtmSCConnectionState_Type(Integer32):
    """Custom type cnAtmSCConnectionState based on Integer32"""
    defaultValue = 0


_CnAtmSCConnectionState_Type.__name__ = "Integer32"
_CnAtmSCConnectionState_Object = MibTableColumn
cnAtmSCConnectionState = _CnAtmSCConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 14),
    _CnAtmSCConnectionState_Type()
)
cnAtmSCConnectionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCConnectionState.setStatus("current")


class _CnAtmSCPvcUpstreamPolicing_Type(Integer32):
    """Custom type cnAtmSCPvcUpstreamPolicing based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAtmSCPvcUpstreamPolicing_Type.__name__ = "Integer32"
_CnAtmSCPvcUpstreamPolicing_Object = MibTableColumn
cnAtmSCPvcUpstreamPolicing = _CnAtmSCPvcUpstreamPolicing_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 15),
    _CnAtmSCPvcUpstreamPolicing_Type()
)
cnAtmSCPvcUpstreamPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCPvcUpstreamPolicing.setStatus("current")


class _CnAtmSCConnectionServiceType_Type(CnTopologyServiceType):
    """Custom type cnAtmSCConnectionServiceType based on CnTopologyServiceType"""
    defaultValue = 1


_CnAtmSCConnectionServiceType_Type.__name__ = "CnTopologyServiceType"
_CnAtmSCConnectionServiceType_Object = MibTableColumn
cnAtmSCConnectionServiceType = _CnAtmSCConnectionServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 16),
    _CnAtmSCConnectionServiceType_Type()
)
cnAtmSCConnectionServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCConnectionServiceType.setStatus("current")
_CnAtmSCRowStatus_Type = RowStatus
_CnAtmSCRowStatus_Object = MibTableColumn
cnAtmSCRowStatus = _CnAtmSCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 3, 1, 1, 17),
    _CnAtmSCRowStatus_Type()
)
cnAtmSCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmSCRowStatus.setStatus("current")
_CnAtmSCConformance_ObjectIdentity = ObjectIdentity
cnAtmSCConformance = _CnAtmSCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 7)
)
_CnAtmSCGroups_ObjectIdentity = ObjectIdentity
cnAtmSCGroups = _CnAtmSCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 7, 1)
)
_CnAtmSCCompliances_ObjectIdentity = ObjectIdentity
cnAtmSCCompliances = _CnAtmSCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 7, 2)
)
_CnDistListTable_Object = MibTable
cnDistListTable = _CnDistListTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 4)
)
if mibBuilder.loadTexts:
    cnDistListTable.setStatus("current")
_CnDistListEntry_Object = MibTableRow
cnDistListEntry = _CnDistListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 4, 1)
)
cnDistListEntry.setIndexNames(
    (0, "CEM-CENTRALIZED-MANAGEMENT-MIB", "cnDistListIndex"),
)
if mibBuilder.loadTexts:
    cnDistListEntry.setStatus("current")


class _CnDistListIndex_Type(Integer32):
    """Custom type cnDistListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnDistListIndex_Type.__name__ = "Integer32"
_CnDistListIndex_Object = MibTableColumn
cnDistListIndex = _CnDistListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 4, 1, 1),
    _CnDistListIndex_Type()
)
cnDistListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnDistListIndex.setStatus("current")


class _CnDistListName_Type(OctetString):
    """Custom type cnDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnDistListName_Type.__name__ = "OctetString"
_CnDistListName_Object = MibTableColumn
cnDistListName = _CnDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 4, 1, 2),
    _CnDistListName_Type()
)
cnDistListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnDistListName.setStatus("current")


class _CnDistListNodes_Type(OctetString):
    """Custom type cnDistListNodes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_CnDistListNodes_Type.__name__ = "OctetString"
_CnDistListNodes_Object = MibTableColumn
cnDistListNodes = _CnDistListNodes_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 4, 1, 3),
    _CnDistListNodes_Type()
)
cnDistListNodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnDistListNodes.setStatus("current")
_CnDistListRowStatus_Type = RowStatus
_CnDistListRowStatus_Object = MibTableColumn
cnDistListRowStatus = _CnDistListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 28, 4, 1, 4),
    _CnDistListRowStatus_Type()
)
cnDistListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnDistListRowStatus.setStatus("current")

# Managed Objects groups

cnAtmSCGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 28, 2, 7, 1, 1)
)
cnAtmSCGeneralGroup.setObjects(
      *(("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCUSVclVpi"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCUSVclVci"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCIndexNext"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCUSVccAalType"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCDSVclVpi"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCDSVccAalType"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCConnectionState"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCPvcUpstreamPolicing"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCResultText"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCResultCode"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCRowStatus"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCUSIfIndex"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCDSIfIndex"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCDSVclVci"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCVclReceiveTrafficDescrIndex"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCVclTransmitTrafficDescrIndex"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCUSNodeId"),
        ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnAtmSCDSNodeId"))
)
if mibBuilder.loadTexts:
    cnAtmSCGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cnTopologyMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 28, 1, 3, 2, 1)
)
cnTopologyMibCompliance.setObjects(
    ("CEM-CENTRALIZED-MANAGEMENT-MIB", "cnTopology")
)
if mibBuilder.loadTexts:
    cnTopologyMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CENTRALIZED-MANAGEMENT-MIB",
    **{"CnTopologyNodeId": CnTopologyNodeId,
       "CnTopologyNodeType": CnTopologyNodeType,
       "CnTopologyServiceType": CnTopologyServiceType,
       "cnCentralizedManagementModule": cnCentralizedManagementModule,
       "cnTopology": cnTopology,
       "cnTopologyMibObjects": cnTopologyMibObjects,
       "cnTopologyLocalNode": cnTopologyLocalNode,
       "cnTopologyLocalNodeId": cnTopologyLocalNodeId,
       "cnTopologyLocalNodeType": cnTopologyLocalNodeType,
       "cnTopologyLocalMasterIp": cnTopologyLocalMasterIp,
       "cnTopologyRemoteNodeTable": cnTopologyRemoteNodeTable,
       "cnTopologyRemoteNodeEntry": cnTopologyRemoteNodeEntry,
       "cnTopologyRemoteNodeId": cnTopologyRemoteNodeId,
       "cnTopologyRemoteNodeIpAddress": cnTopologyRemoteNodeIpAddress,
       "cnTopologyRemoteNodeType": cnTopologyRemoteNodeType,
       "cnTopologyRemoteNodeDiscovered": cnTopologyRemoteNodeDiscovered,
       "cnTopologyRemoteNodeStatus": cnTopologyRemoteNodeStatus,
       "cnTopologyRemoteNodeRowStatus": cnTopologyRemoteNodeRowStatus,
       "cnTopologyPhyConnTable": cnTopologyPhyConnTable,
       "cnTopologyPhyConnEntry": cnTopologyPhyConnEntry,
       "cnTopologyPhyConnNodeIdA": cnTopologyPhyConnNodeIdA,
       "cnTopologyPhyConnIfIndexA": cnTopologyPhyConnIfIndexA,
       "cnTopologyPhyConnNodeIdB": cnTopologyPhyConnNodeIdB,
       "cnTopologyPhyConnIfIndexB": cnTopologyPhyConnIfIndexB,
       "cnTopologyPhyConnRingId": cnTopologyPhyConnRingId,
       "cnTopologyPhyConnStatus": cnTopologyPhyConnStatus,
       "cnTopologyPhyConnRowStatus": cnTopologyPhyConnRowStatus,
       "cnTopologyPathTable": cnTopologyPathTable,
       "cnTopologyPathEntry": cnTopologyPathEntry,
       "cnTopologyPathSrcNodeId": cnTopologyPathSrcNodeId,
       "cnTopologyPathSrcIfIndex": cnTopologyPathSrcIfIndex,
       "cnTopologyPathSrcVpi": cnTopologyPathSrcVpi,
       "cnTopologyPathDestNodeId": cnTopologyPathDestNodeId,
       "cnTopologyPathDestIfIndex": cnTopologyPathDestIfIndex,
       "cnTopologyPathDestVpi": cnTopologyPathDestVpi,
       "cnTopologyPathServiceType": cnTopologyPathServiceType,
       "cnTopologyPathServiceCategory": cnTopologyPathServiceCategory,
       "cnTopologyPathReceiveTrafficDescrIndex": cnTopologyPathReceiveTrafficDescrIndex,
       "cnTopologyPathTransmitTrafficDescrIndex": cnTopologyPathTransmitTrafficDescrIndex,
       "cnTopologyPathStatus": cnTopologyPathStatus,
       "cnTopologyPathRowStatus": cnTopologyPathRowStatus,
       "cnTopologyNotifications": cnTopologyNotifications,
       "cnTopologyConformance": cnTopologyConformance,
       "cnTopologyGroups": cnTopologyGroups,
       "cnTopologyCompliances": cnTopologyCompliances,
       "cnTopologyMibCompliance": cnTopologyMibCompliance,
       "cnATMServiceConnection": cnATMServiceConnection,
       "cnAtmSCIndexNext": cnAtmSCIndexNext,
       "cnAtmSCResultTables": cnAtmSCResultTables,
       "cnAtmSCResultTable": cnAtmSCResultTable,
       "cnAtmSCResultEntry": cnAtmSCResultEntry,
       "cnAtmSCResultIndex": cnAtmSCResultIndex,
       "cnAtmSCResultCode": cnAtmSCResultCode,
       "cnAtmSCResultText": cnAtmSCResultText,
       "cnAtmSCTables": cnAtmSCTables,
       "cnAtmSCTable": cnAtmSCTable,
       "cnAtmSCEntry": cnAtmSCEntry,
       "cnAtmSCIndex": cnAtmSCIndex,
       "cnAtmSCUSNodeId": cnAtmSCUSNodeId,
       "cnAtmSCUSIfIndex": cnAtmSCUSIfIndex,
       "cnAtmSCDSNodeId": cnAtmSCDSNodeId,
       "cnAtmSCDSIfIndex": cnAtmSCDSIfIndex,
       "cnAtmSCUSVclVpi": cnAtmSCUSVclVpi,
       "cnAtmSCUSVclVci": cnAtmSCUSVclVci,
       "cnAtmSCUSVccAalType": cnAtmSCUSVccAalType,
       "cnAtmSCDSVclVpi": cnAtmSCDSVclVpi,
       "cnAtmSCDSVclVci": cnAtmSCDSVclVci,
       "cnAtmSCDSVccAalType": cnAtmSCDSVccAalType,
       "cnAtmSCVclReceiveTrafficDescrIndex": cnAtmSCVclReceiveTrafficDescrIndex,
       "cnAtmSCVclTransmitTrafficDescrIndex": cnAtmSCVclTransmitTrafficDescrIndex,
       "cnAtmSCConnectionState": cnAtmSCConnectionState,
       "cnAtmSCPvcUpstreamPolicing": cnAtmSCPvcUpstreamPolicing,
       "cnAtmSCConnectionServiceType": cnAtmSCConnectionServiceType,
       "cnAtmSCRowStatus": cnAtmSCRowStatus,
       "cnAtmSCConformance": cnAtmSCConformance,
       "cnAtmSCGroups": cnAtmSCGroups,
       "cnAtmSCGeneralGroup": cnAtmSCGeneralGroup,
       "cnAtmSCCompliances": cnAtmSCCompliances,
       "cnDistListTable": cnDistListTable,
       "cnDistListEntry": cnDistListEntry,
       "cnDistListIndex": cnDistListIndex,
       "cnDistListName": cnDistListName,
       "cnDistListNodes": cnDistListNodes,
       "cnDistListRowStatus": cnDistListRowStatus}
)
