# SNMP MIB module (SCALITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scality_37489/SCALITY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:56:33 2025
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

(InetAddressIPv4,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
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

scalityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 1)
)
if mibBuilder.loadTexts:
    scalityMIB.setRevisions(
        ("2012-01-25 18:12",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Scality_ObjectIdentity = ObjectIdentity
scality = _Scality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 2)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1)
)
_Servers_ObjectIdentity = ObjectIdentity
servers = _Servers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1)
)
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1)
)
_Node_ObjectIdentity = ObjectIdentity
node = _Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1)
)
_NodeTable_Object = MibTable
nodeTable = _NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nodeTable.setStatus("current")
_NodeEntry_Object = MibTableRow
nodeEntry = _NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1)
)
nodeEntry.setIndexNames(
    (0, "SCALITY-MIB", "nodeIndex"),
)
if mibBuilder.loadTexts:
    nodeEntry.setStatus("current")
_NodeIndex_Type = Integer32
_NodeIndex_Object = MibTableColumn
nodeIndex = _NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 1),
    _NodeIndex_Type()
)
nodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeIndex.setStatus("current")
_NodeName_Type = OctetString
_NodeName_Object = MibTableColumn
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 2),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeName.setStatus("current")
_NodeAddr_Type = OctetString
_NodeAddr_Object = MibTableColumn
nodeAddr = _NodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 3),
    _NodeAddr_Type()
)
nodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeAddr.setStatus("current")
_NodeIpPort_Type = InetPortNumber
_NodeIpPort_Object = MibTableColumn
nodeIpPort = _NodeIpPort_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 4),
    _NodeIpPort_Type()
)
nodeIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIpPort.setStatus("current")
_NodeStatus_Type = OctetString
_NodeStatus_Object = MibTableColumn
nodeStatus = _NodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 5),
    _NodeStatus_Type()
)
nodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeStatus.setStatus("current")
_NodeRingName_Type = OctetString
_NodeRingName_Object = MibTableColumn
nodeRingName = _NodeRingName_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 6),
    _NodeRingName_Type()
)
nodeRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRingName.setStatus("current")
_NodeObjects_Type = Integer32
_NodeObjects_Object = MibTableColumn
nodeObjects = _NodeObjects_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 7),
    _NodeObjects_Type()
)
nodeObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeObjects.setStatus("current")
_NodeAvailable_Type = TruthValue
_NodeAvailable_Object = MibTableColumn
nodeAvailable = _NodeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 8),
    _NodeAvailable_Type()
)
nodeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeAvailable.setStatus("current")
_NodeNeedReload_Type = TruthValue
_NodeNeedReload_Object = MibTableColumn
nodeNeedReload = _NodeNeedReload_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 9),
    _NodeNeedReload_Type()
)
nodeNeedReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNeedReload.setStatus("current")
_NodeTaskBlocked_Type = TruthValue
_NodeTaskBlocked_Object = MibTableColumn
nodeTaskBlocked = _NodeTaskBlocked_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 1, 1, 10),
    _NodeTaskBlocked_Type()
)
nodeTaskBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTaskBlocked.setStatus("current")
_Iod_ObjectIdentity = ObjectIdentity
iod = _Iod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2)
)
_IodTable_Object = MibTable
iodTable = _IodTable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    iodTable.setStatus("current")
_IodEntry_Object = MibTableRow
iodEntry = _IodEntry_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1)
)
iodEntry.setIndexNames(
    (0, "SCALITY-MIB", "iodIndex"),
)
if mibBuilder.loadTexts:
    iodEntry.setStatus("current")


class _IodIndex_Type(Integer32):
    """Custom type iodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000),
    )


_IodIndex_Type.__name__ = "Integer32"
_IodIndex_Object = MibTableColumn
iodIndex = _IodIndex_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 1),
    _IodIndex_Type()
)
iodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iodIndex.setStatus("current")
_IodName_Type = OctetString
_IodName_Object = MibTableColumn
iodName = _IodName_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 2),
    _IodName_Type()
)
iodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodName.setStatus("current")
_IodType_Type = OctetString
_IodType_Object = MibTableColumn
iodType = _IodType_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 3),
    _IodType_Type()
)
iodType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodType.setStatus("current")
_IodStored_Type = Counter64
_IodStored_Object = MibTableColumn
iodStored = _IodStored_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 4),
    _IodStored_Type()
)
iodStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodStored.setStatus("current")
_IodAvail_Type = Counter64
_IodAvail_Object = MibTableColumn
iodAvail = _IodAvail_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 5),
    _IodAvail_Type()
)
iodAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodAvail.setStatus("current")
_IodTotal_Type = Counter64
_IodTotal_Object = MibTableColumn
iodTotal = _IodTotal_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 6),
    _IodTotal_Type()
)
iodTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodTotal.setStatus("current")
_IodStatus_Type = OctetString
_IodStatus_Object = MibTableColumn
iodStatus = _IodStatus_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 7),
    _IodStatus_Type()
)
iodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodStatus.setStatus("current")
_IodFull_Type = Integer32
_IodFull_Object = MibTableColumn
iodFull = _IodFull_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 8),
    _IodFull_Type()
)
iodFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodFull.setStatus("current")
_IodFsid_Type = OctetString
_IodFsid_Object = MibTableColumn
iodFsid = _IodFsid_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 9),
    _IodFsid_Type()
)
iodFsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodFsid.setStatus("current")
_IodAvailable_Type = TruthValue
_IodAvailable_Object = MibTableColumn
iodAvailable = _IodAvailable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 10),
    _IodAvailable_Type()
)
iodAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iodAvailable.setStatus("current")
_IodRing_Type = OctetString
_IodRing_Object = MibTableColumn
iodRing = _IodRing_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 1, 1, 11),
    _IodRing_Type()
)
iodRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iodRing.setStatus("current")
_RestConnector_ObjectIdentity = ObjectIdentity
restConnector = _RestConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3)
)
_RestConnectorTable_Object = MibTable
restConnectorTable = _RestConnectorTable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    restConnectorTable.setStatus("current")
_RestConnectorEntry_Object = MibTableRow
restConnectorEntry = _RestConnectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 1, 1)
)
restConnectorEntry.setIndexNames(
    (0, "SCALITY-MIB", "restConnectorIndex"),
)
if mibBuilder.loadTexts:
    restConnectorEntry.setStatus("current")
_RestConnectorIndex_Type = Integer32
_RestConnectorIndex_Object = MibTableColumn
restConnectorIndex = _RestConnectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 1, 1, 1),
    _RestConnectorIndex_Type()
)
restConnectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    restConnectorIndex.setStatus("current")
_RestConnectorName_Type = OctetString
_RestConnectorName_Object = MibTableColumn
restConnectorName = _RestConnectorName_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 1, 1, 2),
    _RestConnectorName_Type()
)
restConnectorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restConnectorName.setStatus("current")
_RestConnectorAddr_Type = OctetString
_RestConnectorAddr_Object = MibTableColumn
restConnectorAddr = _RestConnectorAddr_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 1, 1, 3),
    _RestConnectorAddr_Type()
)
restConnectorAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restConnectorAddr.setStatus("current")
_RestConnectorStatus_Type = OctetString
_RestConnectorStatus_Object = MibTableColumn
restConnectorStatus = _RestConnectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 1, 1, 4),
    _RestConnectorStatus_Type()
)
restConnectorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restConnectorStatus.setStatus("current")
_RestConnectorBootstrap_Type = OctetString
_RestConnectorBootstrap_Object = MibTableColumn
restConnectorBootstrap = _RestConnectorBootstrap_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 1, 1, 5),
    _RestConnectorBootstrap_Type()
)
restConnectorBootstrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restConnectorBootstrap.setStatus("current")
_RestConnectorAvailable_Type = TruthValue
_RestConnectorAvailable_Object = MibTableColumn
restConnectorAvailable = _RestConnectorAvailable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 1, 1, 6),
    _RestConnectorAvailable_Type()
)
restConnectorAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restConnectorAvailable.setStatus("current")
_Supervisor_ObjectIdentity = ObjectIdentity
supervisor = _Supervisor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4)
)
_RingTable_Object = MibTable
ringTable = _RingTable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ringTable.setStatus("current")
_RingEntry_Object = MibTableRow
ringEntry = _RingEntry_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1)
)
ringEntry.setIndexNames(
    (0, "SCALITY-MIB", "ringIndex"),
)
if mibBuilder.loadTexts:
    ringEntry.setStatus("current")
_RingIndex_Type = Integer32
_RingIndex_Object = MibTableColumn
ringIndex = _RingIndex_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 1),
    _RingIndex_Type()
)
ringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ringIndex.setStatus("current")
_RingName_Type = OctetString
_RingName_Object = MibTableColumn
ringName = _RingName_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 2),
    _RingName_Type()
)
ringName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringName.setStatus("current")
_RingStateRun_Type = TruthValue
_RingStateRun_Object = MibTableColumn
ringStateRun = _RingStateRun_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 3),
    _RingStateRun_Type()
)
ringStateRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStateRun.setStatus("current")
_RingStateOOS_Type = TruthValue
_RingStateOOS_Object = MibTableColumn
ringStateOOS = _RingStateOOS_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 4),
    _RingStateOOS_Type()
)
ringStateOOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStateOOS.setStatus("current")
_RingNodeTotal_Type = Integer32
_RingNodeTotal_Object = MibTableColumn
ringNodeTotal = _RingNodeTotal_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 5),
    _RingNodeTotal_Type()
)
ringNodeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringNodeTotal.setStatus("current")
_RingNodeRun_Type = Integer32
_RingNodeRun_Object = MibTableColumn
ringNodeRun = _RingNodeRun_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 6),
    _RingNodeRun_Type()
)
ringNodeRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringNodeRun.setStatus("current")
_RingNodeOOS_Type = Integer32
_RingNodeOOS_Object = MibTableColumn
ringNodeOOS = _RingNodeOOS_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 7),
    _RingNodeOOS_Type()
)
ringNodeOOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringNodeOOS.setStatus("current")
_RingState_Type = OctetString
_RingState_Object = MibTableColumn
ringState = _RingState_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 8),
    _RingState_Type()
)
ringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringState.setStatus("current")
_RingDiskTotal_Type = Integer32
_RingDiskTotal_Object = MibTableColumn
ringDiskTotal = _RingDiskTotal_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 9),
    _RingDiskTotal_Type()
)
ringDiskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringDiskTotal.setStatus("current")
_RingObjectsTotal_Type = Counter64
_RingObjectsTotal_Object = MibTableColumn
ringObjectsTotal = _RingObjectsTotal_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 10),
    _RingObjectsTotal_Type()
)
ringObjectsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringObjectsTotal.setStatus("current")
_RingStorageAvg_Type = Integer32
_RingStorageAvg_Object = MibTableColumn
ringStorageAvg = _RingStorageAvg_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 11),
    _RingStorageAvg_Type()
)
ringStorageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStorageAvg.setStatus("current")
_RingStorageStored_Type = Counter64
_RingStorageStored_Object = MibTableColumn
ringStorageStored = _RingStorageStored_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 12),
    _RingStorageStored_Type()
)
ringStorageStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStorageStored.setStatus("current")
_RingStorageUsed_Type = Integer32
_RingStorageUsed_Object = MibTableColumn
ringStorageUsed = _RingStorageUsed_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 13),
    _RingStorageUsed_Type()
)
ringStorageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStorageUsed.setStatus("current")
_RingStorageAvailable_Type = Integer32
_RingStorageAvailable_Object = MibTableColumn
ringStorageAvailable = _RingStorageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 14),
    _RingStorageAvailable_Type()
)
ringStorageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStorageAvailable.setStatus("current")
_RingStorageTotal_Type = Integer32
_RingStorageTotal_Object = MibTableColumn
ringStorageTotal = _RingStorageTotal_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 1, 1, 15),
    _RingStorageTotal_Type()
)
ringStorageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStorageTotal.setStatus("current")
_SupTable_Object = MibTable
supTable = _SupTable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    supTable.setStatus("current")
_SupEntry_Object = MibTableRow
supEntry = _SupEntry_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1)
)
supEntry.setIndexNames(
    (0, "SCALITY-MIB", "supIndex"),
)
if mibBuilder.loadTexts:
    supEntry.setStatus("current")
_SupIndex_Type = Integer32
_SupIndex_Object = MibTableColumn
supIndex = _SupIndex_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1, 1),
    _SupIndex_Type()
)
supIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    supIndex.setStatus("current")
_SupName_Type = OctetString
_SupName_Object = MibTableColumn
supName = _SupName_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1, 2),
    _SupName_Type()
)
supName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supName.setStatus("current")
_SupIpPort_Type = InetPortNumber
_SupIpPort_Object = MibTableColumn
supIpPort = _SupIpPort_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1, 3),
    _SupIpPort_Type()
)
supIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supIpPort.setStatus("current")
_SupAddr_Type = InetAddressIPv4
_SupAddr_Object = MibTableColumn
supAddr = _SupAddr_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1, 4),
    _SupAddr_Type()
)
supAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supAddr.setStatus("current")
_SupNbSrvTotal_Type = Integer32
_SupNbSrvTotal_Object = MibTableColumn
supNbSrvTotal = _SupNbSrvTotal_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1, 5),
    _SupNbSrvTotal_Type()
)
supNbSrvTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supNbSrvTotal.setStatus("current")
_SupNbSrvOk_Type = Integer32
_SupNbSrvOk_Object = MibTableColumn
supNbSrvOk = _SupNbSrvOk_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1, 6),
    _SupNbSrvOk_Type()
)
supNbSrvOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supNbSrvOk.setStatus("current")
_SupNbSrvNok_Type = Integer32
_SupNbSrvNok_Object = MibTableColumn
supNbSrvNok = _SupNbSrvNok_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1, 7),
    _SupNbSrvNok_Type()
)
supNbSrvNok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supNbSrvNok.setStatus("current")
_SupAvailable_Type = TruthValue
_SupAvailable_Object = MibTableColumn
supAvailable = _SupAvailable_Object(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 2, 1, 8),
    _SupAvailable_Type()
)
supAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supAvailable.setStatus("current")

# Managed Objects groups


# Notification objects

trapNodeStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 3)
)
trapNodeStatusChanged.setObjects(
      *(("SCALITY-MIB", "nodeName"),
        ("SCALITY-MIB", "nodeStatus"))
)
if mibBuilder.loadTexts:
    trapNodeStatusChanged.setStatus(
        "current"
    )

trapNodeNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 4)
)
trapNodeNotAvailable.setObjects(
      *(("SCALITY-MIB", "nodeName"),
        ("SCALITY-MIB", "nodeAvailable"))
)
if mibBuilder.loadTexts:
    trapNodeNotAvailable.setStatus(
        "current"
    )

trapNodeNeedsReload = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 5)
)
trapNodeNeedsReload.setObjects(
      *(("SCALITY-MIB", "nodeName"),
        ("SCALITY-MIB", "nodeNeedReload"))
)
if mibBuilder.loadTexts:
    trapNodeNeedsReload.setStatus(
        "current"
    )

trapNodeTaskBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 6)
)
trapNodeTaskBlocked.setObjects(
      *(("SCALITY-MIB", "nodeName"),
        ("SCALITY-MIB", "nodeTaskBlocked"))
)
if mibBuilder.loadTexts:
    trapNodeTaskBlocked.setStatus(
        "current"
    )

trapIodNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 3)
)
trapIodNotAvailable.setObjects(
    ("SCALITY-MIB", "iodFull")
)
if mibBuilder.loadTexts:
    trapIodNotAvailable.setStatus(
        "current"
    )

trapIodDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 4)
)
trapIodDiskFull.setObjects(
      *(("SCALITY-MIB", "iodName"),
        ("SCALITY-MIB", "iodFull"))
)
if mibBuilder.loadTexts:
    trapIodDiskFull.setStatus(
        "current"
    )

trapIodStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 5)
)
trapIodStatusChanged.setObjects(
      *(("SCALITY-MIB", "iodName"),
        ("SCALITY-MIB", "ringState"))
)
if mibBuilder.loadTexts:
    trapIodStatusChanged.setStatus(
        "current"
    )

trapRestConnStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 3)
)
trapRestConnStatusChanged.setObjects(
      *(("SCALITY-MIB", "restConnectorName"),
        ("SCALITY-MIB", "restConnectorStatus"))
)
if mibBuilder.loadTexts:
    trapRestConnStatusChanged.setStatus(
        "current"
    )

trapRestConnectorNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 4)
)
trapRestConnectorNotAvailable.setObjects(
      *(("SCALITY-MIB", "restConnectorName"),
        ("SCALITY-MIB", "restConnectorAvailable"))
)
if mibBuilder.loadTexts:
    trapRestConnectorNotAvailable.setStatus(
        "current"
    )

trapRingRunChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 4)
)
trapRingRunChanged.setObjects(
      *(("SCALITY-MIB", "ringName"),
        ("SCALITY-MIB", "ringNodeRun"))
)
if mibBuilder.loadTexts:
    trapRingRunChanged.setStatus(
        "current"
    )

trapRingStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 6)
)
trapRingStatusChanged.setObjects(
      *(("SCALITY-MIB", "ringName"),
        ("SCALITY-MIB", "ringState"))
)
if mibBuilder.loadTexts:
    trapRingStatusChanged.setStatus(
        "current"
    )

trapSupNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 7)
)
trapSupNotAvailable.setObjects(
      *(("SCALITY-MIB", "supName"),
        ("SCALITY-MIB", "supAvailable"))
)
if mibBuilder.loadTexts:
    trapSupNotAvailable.setStatus(
        "current"
    )

trapSupSrvOKChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 8)
)
trapSupSrvOKChanged.setObjects(
      *(("SCALITY-MIB", "supName"),
        ("SCALITY-MIB", "supNbSrvOk"))
)
if mibBuilder.loadTexts:
    trapSupSrvOKChanged.setStatus(
        "current"
    )


# Notifications groups

trapGrpNode = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 1, 2)
)
trapGrpNode.setObjects(
      *(("SCALITY-MIB", "trapNodeNotAvailable"),
        ("SCALITY-MIB", "trapNodeStatusChanged"))
)
if mibBuilder.loadTexts:
    trapGrpNode.setStatus(
        "current"
    )

trapGrpIod = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 2, 2)
)
trapGrpIod.setObjects(
      *(("SCALITY-MIB", "trapIodDiskFull"),
        ("SCALITY-MIB", "trapIodNotAvailable"),
        ("SCALITY-MIB", "trapIodStatusChanged"))
)
if mibBuilder.loadTexts:
    trapGrpIod.setStatus(
        "current"
    )

trapGrpRestConnectior = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 3, 2)
)
trapGrpRestConnectior.setObjects(
      *(("SCALITY-MIB", "trapRestConnectorNotAvailable"),
        ("SCALITY-MIB", "trapRestConnStatusChanged"))
)
if mibBuilder.loadTexts:
    trapGrpRestConnectior.setStatus(
        "current"
    )

trapGrpSupervisor = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 37489, 2, 1, 1, 1, 4, 3)
)
trapGrpSupervisor.setObjects(
      *(("SCALITY-MIB", "trapRingRunChanged"),
        ("SCALITY-MIB", "trapRingStatusChanged"),
        ("SCALITY-MIB", "trapSupNotAvailable"),
        ("SCALITY-MIB", "trapSupSrvOKChanged"))
)
if mibBuilder.loadTexts:
    trapGrpSupervisor.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCALITY-MIB",
    **{"scality": scality,
       "scalityMIB": scalityMIB,
       "products": products,
       "storage": storage,
       "servers": servers,
       "version": version,
       "node": node,
       "nodeTable": nodeTable,
       "nodeEntry": nodeEntry,
       "nodeIndex": nodeIndex,
       "nodeName": nodeName,
       "nodeAddr": nodeAddr,
       "nodeIpPort": nodeIpPort,
       "nodeStatus": nodeStatus,
       "nodeRingName": nodeRingName,
       "nodeObjects": nodeObjects,
       "nodeAvailable": nodeAvailable,
       "nodeNeedReload": nodeNeedReload,
       "nodeTaskBlocked": nodeTaskBlocked,
       "trapGrpNode": trapGrpNode,
       "trapNodeStatusChanged": trapNodeStatusChanged,
       "trapNodeNotAvailable": trapNodeNotAvailable,
       "trapNodeNeedsReload": trapNodeNeedsReload,
       "trapNodeTaskBlocked": trapNodeTaskBlocked,
       "iod": iod,
       "iodTable": iodTable,
       "iodEntry": iodEntry,
       "iodIndex": iodIndex,
       "iodName": iodName,
       "iodType": iodType,
       "iodStored": iodStored,
       "iodAvail": iodAvail,
       "iodTotal": iodTotal,
       "iodStatus": iodStatus,
       "iodFull": iodFull,
       "iodFsid": iodFsid,
       "iodAvailable": iodAvailable,
       "iodRing": iodRing,
       "trapGrpIod": trapGrpIod,
       "trapIodNotAvailable": trapIodNotAvailable,
       "trapIodDiskFull": trapIodDiskFull,
       "trapIodStatusChanged": trapIodStatusChanged,
       "restConnector": restConnector,
       "restConnectorTable": restConnectorTable,
       "restConnectorEntry": restConnectorEntry,
       "restConnectorIndex": restConnectorIndex,
       "restConnectorName": restConnectorName,
       "restConnectorAddr": restConnectorAddr,
       "restConnectorStatus": restConnectorStatus,
       "restConnectorBootstrap": restConnectorBootstrap,
       "restConnectorAvailable": restConnectorAvailable,
       "trapGrpRestConnectior": trapGrpRestConnectior,
       "trapRestConnStatusChanged": trapRestConnStatusChanged,
       "trapRestConnectorNotAvailable": trapRestConnectorNotAvailable,
       "supervisor": supervisor,
       "ringTable": ringTable,
       "ringEntry": ringEntry,
       "ringIndex": ringIndex,
       "ringName": ringName,
       "ringStateRun": ringStateRun,
       "ringStateOOS": ringStateOOS,
       "ringNodeTotal": ringNodeTotal,
       "ringNodeRun": ringNodeRun,
       "ringNodeOOS": ringNodeOOS,
       "ringState": ringState,
       "ringDiskTotal": ringDiskTotal,
       "ringObjectsTotal": ringObjectsTotal,
       "ringStorageAvg": ringStorageAvg,
       "ringStorageStored": ringStorageStored,
       "ringStorageUsed": ringStorageUsed,
       "ringStorageAvailable": ringStorageAvailable,
       "ringStorageTotal": ringStorageTotal,
       "supTable": supTable,
       "supEntry": supEntry,
       "supIndex": supIndex,
       "supName": supName,
       "supIpPort": supIpPort,
       "supAddr": supAddr,
       "supNbSrvTotal": supNbSrvTotal,
       "supNbSrvOk": supNbSrvOk,
       "supNbSrvNok": supNbSrvNok,
       "supAvailable": supAvailable,
       "trapGrpSupervisor": trapGrpSupervisor,
       "trapRingRunChanged": trapRingRunChanged,
       "trapRingStatusChanged": trapRingStatusChanged,
       "trapSupNotAvailable": trapSupNotAvailable,
       "trapSupSrvOKChanged": trapSupSrvOKChanged}
)
