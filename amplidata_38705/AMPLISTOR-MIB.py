# SNMP MIB module (AMPLISTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/amplidata_38705/AMPLISTOR-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:24:29 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

amplidata = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38705)
)
if mibBuilder.loadTexts:
    amplidata.setRevisions(
        ("2012-08-01 18:25",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 1)
)
_AmountOfBackendStorageUsed_Type = OctetString
_AmountOfBackendStorageUsed_Object = MibScalar
amountOfBackendStorageUsed = _AmountOfBackendStorageUsed_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 1),
    _AmountOfBackendStorageUsed_Type()
)
amountOfBackendStorageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amountOfBackendStorageUsed.setStatus("current")
_AmountOfBackendStorageFree_Type = OctetString
_AmountOfBackendStorageFree_Object = MibScalar
amountOfBackendStorageFree = _AmountOfBackendStorageFree_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 2),
    _AmountOfBackendStorageFree_Type()
)
amountOfBackendStorageFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amountOfBackendStorageFree.setStatus("current")
_AmountOfStorageTakenSyncstoresUsed_Type = Integer32
_AmountOfStorageTakenSyncstoresUsed_Object = MibScalar
amountOfStorageTakenSyncstoresUsed = _AmountOfStorageTakenSyncstoresUsed_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 3),
    _AmountOfStorageTakenSyncstoresUsed_Type()
)
amountOfStorageTakenSyncstoresUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amountOfStorageTakenSyncstoresUsed.setStatus("current")
_AmountOfStorageTakenSyncstoresFree_Type = Integer32
_AmountOfStorageTakenSyncstoresFree_Object = MibScalar
amountOfStorageTakenSyncstoresFree = _AmountOfStorageTakenSyncstoresFree_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 4),
    _AmountOfStorageTakenSyncstoresFree_Type()
)
amountOfStorageTakenSyncstoresFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amountOfStorageTakenSyncstoresFree.setStatus("current")
_TotalNumberOfObjects_Type = OctetString
_TotalNumberOfObjects_Object = MibScalar
totalNumberOfObjects = _TotalNumberOfObjects_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 5),
    _TotalNumberOfObjects_Type()
)
totalNumberOfObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfObjects.setStatus("current")
_TotalNumberOfObjectsinStatusRepair_Type = OctetString
_TotalNumberOfObjectsinStatusRepair_Object = MibScalar
totalNumberOfObjectsinStatusRepair = _TotalNumberOfObjectsinStatusRepair_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 6),
    _TotalNumberOfObjectsinStatusRepair_Type()
)
totalNumberOfObjectsinStatusRepair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfObjectsinStatusRepair.setStatus("current")
_TotalDisksafety_Type = Integer32
_TotalDisksafety_Object = MibScalar
totalDisksafety = _TotalDisksafety_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 7),
    _TotalDisksafety_Type()
)
totalDisksafety.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDisksafety.setStatus("current")
_TotalNumberOfOnlineBlockstores_Type = Integer32
_TotalNumberOfOnlineBlockstores_Object = MibScalar
totalNumberOfOnlineBlockstores = _TotalNumberOfOnlineBlockstores_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 8),
    _TotalNumberOfOnlineBlockstores_Type()
)
totalNumberOfOnlineBlockstores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfOnlineBlockstores.setStatus("current")
_TotalNumberOfReadonlyBlockstores_Type = Integer32
_TotalNumberOfReadonlyBlockstores_Object = MibScalar
totalNumberOfReadonlyBlockstores = _TotalNumberOfReadonlyBlockstores_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 9),
    _TotalNumberOfReadonlyBlockstores_Type()
)
totalNumberOfReadonlyBlockstores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfReadonlyBlockstores.setStatus("current")
_TotalNumberOfAbandonedBlockstores_Type = Integer32
_TotalNumberOfAbandonedBlockstores_Object = MibScalar
totalNumberOfAbandonedBlockstores = _TotalNumberOfAbandonedBlockstores_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 10),
    _TotalNumberOfAbandonedBlockstores_Type()
)
totalNumberOfAbandonedBlockstores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfAbandonedBlockstores.setStatus("current")
_TotalNumberOfOfflineBlockstores_Type = Integer32
_TotalNumberOfOfflineBlockstores_Object = MibScalar
totalNumberOfOfflineBlockstores = _TotalNumberOfOfflineBlockstores_Object(
    (1, 3, 6, 1, 4, 1, 38705, 1, 11),
    _TotalNumberOfOfflineBlockstores_Type()
)
totalNumberOfOfflineBlockstores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfOfflineBlockstores.setStatus("current")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 2)
)
_TotalIngest_Type = Integer32
_TotalIngest_Object = MibScalar
totalIngest = _TotalIngest_Object(
    (1, 3, 6, 1, 4, 1, 38705, 2, 1),
    _TotalIngest_Type()
)
totalIngest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIngest.setStatus("current")
_TotalOutgest_Type = Integer32
_TotalOutgest_Object = MibScalar
totalOutgest = _TotalOutgest_Object(
    (1, 3, 6, 1, 4, 1, 38705, 2, 2),
    _TotalOutgest_Type()
)
totalOutgest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutgest.setStatus("current")
_Controller_ObjectIdentity = ObjectIdentity
controller = _Controller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 3)
)
_TotalPuts_Type = Integer32
_TotalPuts_Object = MibScalar
totalPuts = _TotalPuts_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 1),
    _TotalPuts_Type()
)
totalPuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPuts.setStatus("current")
_TotalGets_Type = Integer32
_TotalGets_Object = MibScalar
totalGets = _TotalGets_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 2),
    _TotalGets_Type()
)
totalGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalGets.setStatus("current")
_TotalInboundConnectionsOnControllers_Type = Integer32
_TotalInboundConnectionsOnControllers_Object = MibScalar
totalInboundConnectionsOnControllers = _TotalInboundConnectionsOnControllers_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 3),
    _TotalInboundConnectionsOnControllers_Type()
)
totalInboundConnectionsOnControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInboundConnectionsOnControllers.setStatus("current")
_TotalIngestTowardsPublicNetwork_Type = Integer32
_TotalIngestTowardsPublicNetwork_Object = MibScalar
totalIngestTowardsPublicNetwork = _TotalIngestTowardsPublicNetwork_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 4),
    _TotalIngestTowardsPublicNetwork_Type()
)
totalIngestTowardsPublicNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIngestTowardsPublicNetwork.setStatus("current")
_TotalOutgestTowardsPublicNetwork_Type = Integer32
_TotalOutgestTowardsPublicNetwork_Object = MibScalar
totalOutgestTowardsPublicNetwork = _TotalOutgestTowardsPublicNetwork_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 5),
    _TotalOutgestTowardsPublicNetwork_Type()
)
totalOutgestTowardsPublicNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutgestTowardsPublicNetwork.setStatus("current")
_TotalIngestTowardsStoragenodes_Type = Integer32
_TotalIngestTowardsStoragenodes_Object = MibScalar
totalIngestTowardsStoragenodes = _TotalIngestTowardsStoragenodes_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 6),
    _TotalIngestTowardsStoragenodes_Type()
)
totalIngestTowardsStoragenodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIngestTowardsStoragenodes.setStatus("current")
_TotalOutgestTowardsStoragenodes_Type = Integer32
_TotalOutgestTowardsStoragenodes_Object = MibScalar
totalOutgestTowardsStoragenodes = _TotalOutgestTowardsStoragenodes_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 7),
    _TotalOutgestTowardsStoragenodes_Type()
)
totalOutgestTowardsStoragenodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutgestTowardsStoragenodes.setStatus("current")
_TotalCpuUsagePerTotalCores_Type = OctetString
_TotalCpuUsagePerTotalCores_Object = MibScalar
totalCpuUsagePerTotalCores = _TotalCpuUsagePerTotalCores_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 8),
    _TotalCpuUsagePerTotalCores_Type()
)
totalCpuUsagePerTotalCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCpuUsagePerTotalCores.setStatus("current")
_TotalLoadPerTotalCores_Type = OctetString
_TotalLoadPerTotalCores_Object = MibScalar
totalLoadPerTotalCores = _TotalLoadPerTotalCores_Object(
    (1, 3, 6, 1, 4, 1, 38705, 3, 9),
    _TotalLoadPerTotalCores_Type()
)
totalLoadPerTotalCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalLoadPerTotalCores.setStatus("current")
_Amplidatanotifs_ObjectIdentity = ObjectIdentity
amplidatanotifs = _Amplidatanotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 1)
)
_Application_ObjectIdentity = ObjectIdentity
application = _Application_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 2)
)
_Metadatastore_ObjectIdentity = ObjectIdentity
metadatastore = _Metadatastore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 3)
)
_Blockstore_ObjectIdentity = ObjectIdentity
blockstore = _Blockstore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 4)
)
_Storagepool_ObjectIdentity = ObjectIdentity
storagepool = _Storagepool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 5)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 6)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 7)
)
_Machine_ObjectIdentity = ObjectIdentity
machine = _Machine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8)
)
_Disk_ObjectIdentity = ObjectIdentity
disk = _Disk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38705, 7, 9)
)

# Managed Objects groups

generalObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38705, 4)
)
generalObjectGroup.setObjects(
      *(("AMPLISTOR-MIB", "totalNumberOfObjectsinStatusRepair"),
        ("AMPLISTOR-MIB", "amountOfBackendStorageUsed"),
        ("AMPLISTOR-MIB", "totalNumberOfAbandonedBlockstores"),
        ("AMPLISTOR-MIB", "totalNumberOfObjects"),
        ("AMPLISTOR-MIB", "amountOfStorageTakenSyncstoresFree"),
        ("AMPLISTOR-MIB", "amountOfBackendStorageFree"),
        ("AMPLISTOR-MIB", "totalDisksafety"),
        ("AMPLISTOR-MIB", "amountOfStorageTakenSyncstoresUsed"),
        ("AMPLISTOR-MIB", "totalNumberOfOnlineBlockstores"),
        ("AMPLISTOR-MIB", "totalNumberOfOfflineBlockstores"),
        ("AMPLISTOR-MIB", "totalNumberOfReadonlyBlockstores"))
)
if mibBuilder.loadTexts:
    generalObjectGroup.setStatus("current")

storageObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38705, 5)
)
storageObjectGroup.setObjects(
      *(("AMPLISTOR-MIB", "totalIngest"),
        ("AMPLISTOR-MIB", "totalOutgest"))
)
if mibBuilder.loadTexts:
    storageObjectGroup.setStatus("current")

controllerObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38705, 6)
)
controllerObjectGroup.setObjects(
      *(("AMPLISTOR-MIB", "totalNumberOfAbandonedBlockstores"),
        ("AMPLISTOR-MIB", "amountOfBackendStorageFree"),
        ("AMPLISTOR-MIB", "amountOfBackendStorageUsed"),
        ("AMPLISTOR-MIB", "totalDisksafety"),
        ("AMPLISTOR-MIB", "totalIngest"),
        ("AMPLISTOR-MIB", "totalNumberOfOfflineBlockstores"),
        ("AMPLISTOR-MIB", "totalGets"),
        ("AMPLISTOR-MIB", "totalInboundConnectionsOnControllers"),
        ("AMPLISTOR-MIB", "totalIngestTowardsPublicNetwork"),
        ("AMPLISTOR-MIB", "totalNumberOfOnlineBlockstores"),
        ("AMPLISTOR-MIB", "totalLoadPerTotalCores"),
        ("AMPLISTOR-MIB", "totalNumberOfObjects"),
        ("AMPLISTOR-MIB", "totalNumberOfObjectsinStatusRepair"),
        ("AMPLISTOR-MIB", "amountOfStorageTakenSyncstoresFree"),
        ("AMPLISTOR-MIB", "totalCpuUsagePerTotalCores"),
        ("AMPLISTOR-MIB", "totalIngestTowardsStoragenodes"),
        ("AMPLISTOR-MIB", "amountOfStorageTakenSyncstoresUsed"),
        ("AMPLISTOR-MIB", "totalNumberOfReadonlyBlockstores"),
        ("AMPLISTOR-MIB", "totalOutgest"),
        ("AMPLISTOR-MIB", "totalOutgestTowardsPublicNetwork"),
        ("AMPLISTOR-MIB", "totalPuts"),
        ("AMPLISTOR-MIB", "totalOutgestTowardsStoragenodes"))
)
if mibBuilder.loadTexts:
    controllerObjectGroup.setStatus("current")


# Notification objects

internalDatabaseBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 2, 25)
)
if mibBuilder.loadTexts:
    internalDatabaseBackupFailed.setStatus(
        "current"
    )

manyFileDescriptors = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 2, 47)
)
if mibBuilder.loadTexts:
    manyFileDescriptors.setStatus(
        "current"
    )

noProgressForClusters = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 2, 49)
)
if mibBuilder.loadTexts:
    noProgressForClusters.setStatus(
        "current"
    )

duplicateAgentSessionsFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 2, 51)
)
if mibBuilder.loadTexts:
    duplicateAgentSessionsFound.setStatus(
        "current"
    )

metaStoreMaintenanceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 3, 4)
)
if mibBuilder.loadTexts:
    metaStoreMaintenanceFailed.setStatus(
        "current"
    )

numberOfKeysInMetaStoreHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 3, 5)
)
if mibBuilder.loadTexts:
    numberOfKeysInMetaStoreHigh.setStatus(
        "current"
    )

MetaStoreNotEnoughServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 3, 7)
)
if mibBuilder.loadTexts:
    MetaStoreNotEnoughServers.setStatus(
        "current"
    )

MetaStoreHasLaggingNodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 3, 8)
)
if mibBuilder.loadTexts:
    MetaStoreHasLaggingNodes.setStatus(
        "current"
    )

blockstoreReadonly = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 4, 26)
)
if mibBuilder.loadTexts:
    blockstoreReadonly.setStatus(
        "current"
    )

blockstoreHighCheckblocks = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 4, 28)
)
if mibBuilder.loadTexts:
    blockstoreHighCheckblocks.setStatus(
        "current"
    )

blockstoreMaxCheckblocks = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 4, 29)
)
if mibBuilder.loadTexts:
    blockstoreMaxCheckblocks.setStatus(
        "current"
    )

blockstoreMonitor = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 4, 30)
)
if mibBuilder.loadTexts:
    blockstoreMonitor.setStatus(
        "current"
    )

storagepoolDataOutdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 5, 1)
)
if mibBuilder.loadTexts:
    storagepoolDataOutdated.setStatus(
        "current"
    )

usedSpaceExceeds70Percent = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 5, 25)
)
if mibBuilder.loadTexts:
    usedSpaceExceeds70Percent.setStatus(
        "current"
    )

usedSpaceExceeds80Percent = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 5, 26)
)
if mibBuilder.loadTexts:
    usedSpaceExceeds80Percent.setStatus(
        "current"
    )

usedSpaceExceeds90Percent = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 5, 27)
)
if mibBuilder.loadTexts:
    usedSpaceExceeds90Percent.setStatus(
        "current"
    )

machineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 6, 1)
)
if mibBuilder.loadTexts:
    machineDown.setStatus(
        "current"
    )

coreDumpsFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 6, 71)
)
if mibBuilder.loadTexts:
    coreDumpsFound.setStatus(
        "current"
    )

nicHalfDuplex = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 7, 3)
)
if mibBuilder.loadTexts:
    nicHalfDuplex.setStatus(
        "current"
    )

nicSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 7, 4)
)
if mibBuilder.loadTexts:
    nicSpeed.setStatus(
        "current"
    )

mountpointFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 1)
)
if mibBuilder.loadTexts:
    mountpointFull.setStatus(
        "current"
    )

swapUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 2)
)
if mibBuilder.loadTexts:
    swapUsage.setStatus(
        "current"
    )

cpuOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 4)
)
if mibBuilder.loadTexts:
    cpuOverloaded.setStatus(
        "current"
    )

memoryOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 5)
)
if mibBuilder.loadTexts:
    memoryOverloaded.setStatus(
        "current"
    )

tooManyErrorPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 6)
)
if mibBuilder.loadTexts:
    tooManyErrorPackets.setStatus(
        "current"
    )

bandwidthUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 7)
)
if mibBuilder.loadTexts:
    bandwidthUsageHigh.setStatus(
        "current"
    )

cpuTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 8)
)
if mibBuilder.loadTexts:
    cpuTemperatureHigh.setStatus(
        "current"
    )

caseTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 9)
)
if mibBuilder.loadTexts:
    caseTemperatureHigh.setStatus(
        "current"
    )

cpuFanNotWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 10)
)
if mibBuilder.loadTexts:
    cpuFanNotWorking.setStatus(
        "current"
    )

smartFailuresDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 12)
)
if mibBuilder.loadTexts:
    smartFailuresDetected.setStatus(
        "current"
    )

partitionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 13)
)
if mibBuilder.loadTexts:
    partitionFailure.setStatus(
        "current"
    )

mirrorDeviceNonCleanState = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 17)
)
if mibBuilder.loadTexts:
    mirrorDeviceNonCleanState.setStatus(
        "current"
    )

dmesgError = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 19)
)
if mibBuilder.loadTexts:
    dmesgError.setStatus(
        "current"
    )

filesystemReadOnly = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 20)
)
if mibBuilder.loadTexts:
    filesystemReadOnly.setStatus(
        "current"
    )

applicationStartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 42)
)
if mibBuilder.loadTexts:
    applicationStartFailed.setStatus(
        "current"
    )

agentRestartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 47)
)
if mibBuilder.loadTexts:
    agentRestartFailed.setStatus(
        "current"
    )

networkInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 54)
)
if mibBuilder.loadTexts:
    networkInterfaceDown.setStatus(
        "current"
    )

cpuLoadHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 104)
)
if mibBuilder.loadTexts:
    cpuLoadHigh.setStatus(
        "current"
    )

smartControlNotEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 105)
)
if mibBuilder.loadTexts:
    smartControlNotEnabled.setStatus(
        "current"
    )

machineRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 8, 106)
)
if mibBuilder.loadTexts:
    machineRebooted.setStatus(
        "current"
    )

diskNotDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 9, 2)
)
if mibBuilder.loadTexts:
    diskNotDetected.setStatus(
        "current"
    )

diskBusLocationNotDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 38705, 7, 9, 11)
)
if mibBuilder.loadTexts:
    diskBusLocationNotDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AMPLISTOR-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "amplidata": amplidata,
       "general": general,
       "amountOfBackendStorageUsed": amountOfBackendStorageUsed,
       "amountOfBackendStorageFree": amountOfBackendStorageFree,
       "amountOfStorageTakenSyncstoresUsed": amountOfStorageTakenSyncstoresUsed,
       "amountOfStorageTakenSyncstoresFree": amountOfStorageTakenSyncstoresFree,
       "totalNumberOfObjects": totalNumberOfObjects,
       "totalNumberOfObjectsinStatusRepair": totalNumberOfObjectsinStatusRepair,
       "totalDisksafety": totalDisksafety,
       "totalNumberOfOnlineBlockstores": totalNumberOfOnlineBlockstores,
       "totalNumberOfReadonlyBlockstores": totalNumberOfReadonlyBlockstores,
       "totalNumberOfAbandonedBlockstores": totalNumberOfAbandonedBlockstores,
       "totalNumberOfOfflineBlockstores": totalNumberOfOfflineBlockstores,
       "storage": storage,
       "totalIngest": totalIngest,
       "totalOutgest": totalOutgest,
       "controller": controller,
       "totalPuts": totalPuts,
       "totalGets": totalGets,
       "totalInboundConnectionsOnControllers": totalInboundConnectionsOnControllers,
       "totalIngestTowardsPublicNetwork": totalIngestTowardsPublicNetwork,
       "totalOutgestTowardsPublicNetwork": totalOutgestTowardsPublicNetwork,
       "totalIngestTowardsStoragenodes": totalIngestTowardsStoragenodes,
       "totalOutgestTowardsStoragenodes": totalOutgestTowardsStoragenodes,
       "totalCpuUsagePerTotalCores": totalCpuUsagePerTotalCores,
       "totalLoadPerTotalCores": totalLoadPerTotalCores,
       "generalObjectGroup": generalObjectGroup,
       "storageObjectGroup": storageObjectGroup,
       "controllerObjectGroup": controllerObjectGroup,
       "amplidatanotifs": amplidatanotifs,
       "agent": agent,
       "application": application,
       "internalDatabaseBackupFailed": internalDatabaseBackupFailed,
       "manyFileDescriptors": manyFileDescriptors,
       "noProgressForClusters": noProgressForClusters,
       "duplicateAgentSessionsFound": duplicateAgentSessionsFound,
       "metadatastore": metadatastore,
       "metaStoreMaintenanceFailed": metaStoreMaintenanceFailed,
       "numberOfKeysInMetaStoreHigh": numberOfKeysInMetaStoreHigh,
       "MetaStoreNotEnoughServers": MetaStoreNotEnoughServers,
       "MetaStoreHasLaggingNodes": MetaStoreHasLaggingNodes,
       "blockstore": blockstore,
       "blockstoreReadonly": blockstoreReadonly,
       "blockstoreHighCheckblocks": blockstoreHighCheckblocks,
       "blockstoreMaxCheckblocks": blockstoreMaxCheckblocks,
       "blockstoreMonitor": blockstoreMonitor,
       "storagepool": storagepool,
       "storagepoolDataOutdated": storagepoolDataOutdated,
       "usedSpaceExceeds70Percent": usedSpaceExceeds70Percent,
       "usedSpaceExceeds80Percent": usedSpaceExceeds80Percent,
       "usedSpaceExceeds90Percent": usedSpaceExceeds90Percent,
       "generic": generic,
       "machineDown": machineDown,
       "coreDumpsFound": coreDumpsFound,
       "network": network,
       "nicHalfDuplex": nicHalfDuplex,
       "nicSpeed": nicSpeed,
       "machine": machine,
       "mountpointFull": mountpointFull,
       "swapUsage": swapUsage,
       "cpuOverloaded": cpuOverloaded,
       "memoryOverloaded": memoryOverloaded,
       "tooManyErrorPackets": tooManyErrorPackets,
       "bandwidthUsageHigh": bandwidthUsageHigh,
       "cpuTemperatureHigh": cpuTemperatureHigh,
       "caseTemperatureHigh": caseTemperatureHigh,
       "cpuFanNotWorking": cpuFanNotWorking,
       "smartFailuresDetected": smartFailuresDetected,
       "partitionFailure": partitionFailure,
       "mirrorDeviceNonCleanState": mirrorDeviceNonCleanState,
       "dmesgError": dmesgError,
       "filesystemReadOnly": filesystemReadOnly,
       "applicationStartFailed": applicationStartFailed,
       "agentRestartFailed": agentRestartFailed,
       "networkInterfaceDown": networkInterfaceDown,
       "cpuLoadHigh": cpuLoadHigh,
       "smartControlNotEnabled": smartControlNotEnabled,
       "machineRebooted": machineRebooted,
       "disk": disk,
       "diskNotDetected": diskNotDetected,
       "diskBusLocationNotDetected": diskBusLocationNotDetected}
)
