# SNMP MIB module (RUBRIK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/rubrik_49929/RUBRIK-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 16:09:22 2025
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

rubrik = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 49929)
)
if mibBuilder.loadTexts:
    rubrik.setRevisions(
        ("2020-11-03 00:00",
         "2020-01-31 00:00",
         "2019-07-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrikSystemMibs_ObjectIdentity = ObjectIdentity
brikSystemMibs = _BrikSystemMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 1)
)
_Cluster_ObjectIdentity = ObjectIdentity
cluster = _Cluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 1)
)
_UsedInBytes_Type = Counter64
_UsedInBytes_Object = MibScalar
usedInBytes = _UsedInBytes_Object(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 1, 1),
    _UsedInBytes_Type()
)
usedInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedInBytes.setStatus("current")
_AvailableInBytes_Type = Counter64
_AvailableInBytes_Object = MibScalar
availableInBytes = _AvailableInBytes_Object(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 1, 2),
    _AvailableInBytes_Type()
)
availableInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableInBytes.setStatus("current")
_TotalInBytes_Type = Counter64
_TotalInBytes_Object = MibScalar
totalInBytes = _TotalInBytes_Object(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 1, 3),
    _TotalInBytes_Type()
)
totalInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInBytes.setStatus("current")
_RunwayRemaining_Type = Gauge32
_RunwayRemaining_Object = MibScalar
runwayRemaining = _RunwayRemaining_Object(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 1, 4),
    _RunwayRemaining_Type()
)
runwayRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runwayRemaining.setStatus("current")
_Bandwidth_ObjectIdentity = ObjectIdentity
bandwidth = _Bandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 2)
)
_ArchiveAvgBytesPerSecondLastHour_Type = Counter64
_ArchiveAvgBytesPerSecondLastHour_Object = MibScalar
archiveAvgBytesPerSecondLastHour = _ArchiveAvgBytesPerSecondLastHour_Object(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 2, 3),
    _ArchiveAvgBytesPerSecondLastHour_Type()
)
archiveAvgBytesPerSecondLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveAvgBytesPerSecondLastHour.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 3)
)
_TotalNodes_Type = Gauge32
_TotalNodes_Object = MibScalar
totalNodes = _TotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 3, 1),
    _TotalNodes_Type()
)
totalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNodes.setStatus("current")
_ActiveNodes_Type = Gauge32
_ActiveNodes_Object = MibScalar
activeNodes = _ActiveNodes_Object(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 3, 2),
    _ActiveNodes_Type()
)
activeNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeNodes.setStatus("current")
_StreamsCount_Type = Gauge32
_StreamsCount_Object = MibScalar
streamsCount = _StreamsCount_Object(
    (1, 3, 6, 1, 4, 1, 49929, 1, 1, 3, 3),
    _StreamsCount_Type()
)
streamsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamsCount.setStatus("current")
_BrikSystemTraps_ObjectIdentity = ObjectIdentity
brikSystemTraps = _BrikSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 2)
)
_HardwareTrapsPrefix_ObjectIdentity = ObjectIdentity
hardwareTrapsPrefix = _HardwareTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1)
)
_HardwareTraps_ObjectIdentity = ObjectIdentity
hardwareTraps = _HardwareTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0)
)
_DiskTrapsPrefix_ObjectIdentity = ObjectIdentity
diskTrapsPrefix = _DiskTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2)
)
_DiskTraps_ObjectIdentity = ObjectIdentity
diskTraps = _DiskTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0)
)
_NodeTrapsPrefix_ObjectIdentity = ObjectIdentity
nodeTrapsPrefix = _NodeTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3)
)
_NodeTraps_ObjectIdentity = ObjectIdentity
nodeTraps = _NodeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0)
)
_BrikBackupTrapsPrefix_ObjectIdentity = ObjectIdentity
brikBackupTrapsPrefix = _BrikBackupTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 4)
)
_BrikBackupTraps_ObjectIdentity = ObjectIdentity
brikBackupTraps = _BrikBackupTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 4, 0)
)
_BrikNotificationObjects_ObjectIdentity = ObjectIdentity
brikNotificationObjects = _BrikNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 8)
)


class _BrikNotificationMessage_Type(OctetString):
    """Custom type brikNotificationMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_BrikNotificationMessage_Type.__name__ = "OctetString"
_BrikNotificationMessage_Object = MibScalar
brikNotificationMessage = _BrikNotificationMessage_Object(
    (1, 3, 6, 1, 4, 1, 49929, 8, 1),
    _BrikNotificationMessage_Type()
)
brikNotificationMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    brikNotificationMessage.setStatus("current")
_RubrikConformance_ObjectIdentity = ObjectIdentity
rubrikConformance = _RubrikConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 11)
)
_RubrikCompliances_ObjectIdentity = ObjectIdentity
rubrikCompliances = _RubrikCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 11, 1)
)
_RubrikGroups_ObjectIdentity = ObjectIdentity
rubrikGroups = _RubrikGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49929, 11, 2)
)

# Managed Objects groups

rubrikObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 49929, 11, 2, 2)
)
rubrikObjects.setObjects(
      *(("RUBRIK-MIB", "brikNotificationMessage"),
        ("RUBRIK-MIB", "usedInBytes"),
        ("RUBRIK-MIB", "availableInBytes"),
        ("RUBRIK-MIB", "totalInBytes"),
        ("RUBRIK-MIB", "runwayRemaining"),
        ("RUBRIK-MIB", "archiveAvgBytesPerSecondLastHour"),
        ("RUBRIK-MIB", "totalNodes"),
        ("RUBRIK-MIB", "activeNodes"),
        ("RUBRIK-MIB", "streamsCount"))
)
if mibBuilder.loadTexts:
    rubrikObjects.setStatus("current")


# Notification objects

networkInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 1)
)
networkInterfaceDown.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    networkInterfaceDown.setStatus(
        "current"
    )

networkInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 2)
)
networkInterfaceUp.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    networkInterfaceUp.setStatus(
        "current"
    )

ntpOutofSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 3)
)
ntpOutofSync.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    ntpOutofSync.setStatus(
        "current"
    )

chassisNeedsReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 4)
)
chassisNeedsReplacement.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    chassisNeedsReplacement.setStatus(
        "current"
    )

dimmError = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 5)
)
dimmError.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    dimmError.setStatus(
        "current"
    )

biosError = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 6)
)
biosError.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    biosError.setStatus(
        "current"
    )

nodeNeedsReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 7)
)
nodeNeedsReplacement.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeNeedsReplacement.setStatus(
        "current"
    )

powerSupplyNeedsReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 8)
)
powerSupplyNeedsReplacement.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    powerSupplyNeedsReplacement.setStatus(
        "current"
    )

chassisRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 9)
)
chassisRecovered.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    chassisRecovered.setStatus(
        "current"
    )

dimmRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 10)
)
dimmRecovered.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    dimmRecovered.setStatus(
        "current"
    )

biosRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 11)
)
biosRecovered.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    biosRecovered.setStatus(
        "current"
    )

powerSupplyRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 12)
)
powerSupplyRecovered.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    powerSupplyRecovered.setStatus(
        "current"
    )

powerSupplyNeedsCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 13)
)
powerSupplyNeedsCheck.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    powerSupplyNeedsCheck.setStatus(
        "current"
    )

cmosNeedsReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 1, 0, 14)
)
cmosNeedsReplacement.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    cmosNeedsReplacement.setStatus(
        "current"
    )

diskLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 1)
)
diskLocked.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskLocked.setStatus(
        "current"
    )

diskLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 2)
)
diskLost.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskLost.setStatus(
        "current"
    )

diskRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 3)
)
diskRecovered.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskRecovered.setStatus(
        "current"
    )

diskRemovedFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 4)
)
diskRemovedFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskRemovedFailure.setStatus(
        "current"
    )

diskRemovedSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 5)
)
diskRemovedSuccess.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskRemovedSuccess.setStatus(
        "current"
    )

diskSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 6)
)
diskSetupFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskSetupFailure.setStatus(
        "current"
    )

diskSetupSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 7)
)
diskSetupSuccess.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskSetupSuccess.setStatus(
        "current"
    )

diskUnformatted = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 8)
)
diskUnformatted.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskUnformatted.setStatus(
        "current"
    )

diskUnhealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 2, 0, 9)
)
diskUnhealthy.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    diskUnhealthy.setStatus(
        "current"
    )

nodeAddFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 1)
)
nodeAddFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeAddFailure.setStatus(
        "current"
    )

nodeAddSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 2)
)
nodeAddSuccess.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeAddSuccess.setStatus(
        "current"
    )

nodeAutoRemoveSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 3)
)
nodeAutoRemoveSuccess.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeAutoRemoveSuccess.setStatus(
        "current"
    )

nodeAutoRemoveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 4)
)
nodeAutoRemoveFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeAutoRemoveFailure.setStatus(
        "current"
    )

nodeAutoRemoveDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 5)
)
nodeAutoRemoveDetected.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeAutoRemoveDetected.setStatus(
        "current"
    )

nodeDecommissionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 6)
)
nodeDecommissionFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeDecommissionFailure.setStatus(
        "current"
    )

nodeDecommissionSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 7)
)
nodeDecommissionSuccess.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeDecommissionSuccess.setStatus(
        "current"
    )

nodeDownInRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 8)
)
nodeDownInRecovery.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeDownInRecovery.setStatus(
        "current"
    )

nodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 9)
)
nodeDown.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeDown.setStatus(
        "current"
    )

nodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 10)
)
nodeUp.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeUp.setStatus(
        "current"
    )

nodeRecommissionSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 11)
)
nodeRecommissionSuccess.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeRecommissionSuccess.setStatus(
        "current"
    )

nodeRecommissionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 12)
)
nodeRecommissionFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeRecommissionFailure.setStatus(
        "current"
    )

nodeRemoveSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 13)
)
nodeRemoveSuccess.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeRemoveSuccess.setStatus(
        "current"
    )

nodeRemoveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 14)
)
nodeRemoveFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeRemoveFailure.setStatus(
        "current"
    )

nodeTpmNeedsUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 15)
)
nodeTpmNeedsUpgrade.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeTpmNeedsUpgrade.setStatus(
        "current"
    )

nodePeriodicTaskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 16)
)
nodePeriodicTaskFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodePeriodicTaskFailure.setStatus(
        "current"
    )

nodeNtpConfigCheckFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 17)
)
nodeNtpConfigCheckFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeNtpConfigCheckFailure.setStatus(
        "current"
    )

nodeDecommissionInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 18)
)
nodeDecommissionInProgress.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeDecommissionInProgress.setStatus(
        "current"
    )

nodeDecommissionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 19)
)
nodeDecommissionStarted.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    nodeDecommissionStarted.setStatus(
        "current"
    )

healthMonitorPolicyCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 20)
)
healthMonitorPolicyCritical.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    healthMonitorPolicyCritical.setStatus(
        "current"
    )

healthMonitorPolicyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 2, 3, 0, 21)
)
healthMonitorPolicyWarning.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    healthMonitorPolicyWarning.setStatus(
        "current"
    )

backupJobFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 49929, 4, 0, 1)
)
backupJobFailure.setObjects(
    ("RUBRIK-MIB", "brikNotificationMessage")
)
if mibBuilder.loadTexts:
    backupJobFailure.setStatus(
        "current"
    )


# Notifications groups

rubrikNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 49929, 11, 2, 1)
)
rubrikNotifications.setObjects(
      *(("RUBRIK-MIB", "networkInterfaceDown"),
        ("RUBRIK-MIB", "networkInterfaceUp"),
        ("RUBRIK-MIB", "ntpOutofSync"),
        ("RUBRIK-MIB", "chassisNeedsReplacement"),
        ("RUBRIK-MIB", "dimmError"),
        ("RUBRIK-MIB", "biosError"),
        ("RUBRIK-MIB", "nodeNeedsReplacement"),
        ("RUBRIK-MIB", "powerSupplyNeedsReplacement"),
        ("RUBRIK-MIB", "chassisRecovered"),
        ("RUBRIK-MIB", "dimmRecovered"),
        ("RUBRIK-MIB", "biosRecovered"),
        ("RUBRIK-MIB", "powerSupplyRecovered"),
        ("RUBRIK-MIB", "powerSupplyNeedsCheck"),
        ("RUBRIK-MIB", "diskLocked"),
        ("RUBRIK-MIB", "diskLost"),
        ("RUBRIK-MIB", "diskRecovered"),
        ("RUBRIK-MIB", "diskRemovedFailure"),
        ("RUBRIK-MIB", "diskRemovedSuccess"),
        ("RUBRIK-MIB", "diskSetupFailure"),
        ("RUBRIK-MIB", "diskSetupSuccess"),
        ("RUBRIK-MIB", "diskUnformatted"),
        ("RUBRIK-MIB", "diskUnhealthy"),
        ("RUBRIK-MIB", "nodeAddFailure"),
        ("RUBRIK-MIB", "nodeAddSuccess"),
        ("RUBRIK-MIB", "nodeAutoRemoveSuccess"),
        ("RUBRIK-MIB", "nodeAutoRemoveFailure"),
        ("RUBRIK-MIB", "nodeAutoRemoveDetected"),
        ("RUBRIK-MIB", "nodeDecommissionStarted"),
        ("RUBRIK-MIB", "nodeDecommissionFailure"),
        ("RUBRIK-MIB", "nodeDecommissionSuccess"),
        ("RUBRIK-MIB", "nodeDecommissionInProgress"),
        ("RUBRIK-MIB", "nodeDownInRecovery"),
        ("RUBRIK-MIB", "nodeDown"),
        ("RUBRIK-MIB", "nodeUp"),
        ("RUBRIK-MIB", "nodeRecommissionSuccess"),
        ("RUBRIK-MIB", "nodeRecommissionFailure"),
        ("RUBRIK-MIB", "nodeRemoveSuccess"),
        ("RUBRIK-MIB", "nodeRemoveFailure"),
        ("RUBRIK-MIB", "nodeTpmNeedsUpgrade"),
        ("RUBRIK-MIB", "nodePeriodicTaskFailure"),
        ("RUBRIK-MIB", "nodeNtpConfigCheckFailure"),
        ("RUBRIK-MIB", "healthMonitorPolicyCritical"),
        ("RUBRIK-MIB", "healthMonitorPolicyWarning"),
        ("RUBRIK-MIB", "backupJobFailure"),
        ("RUBRIK-MIB", "cmosNeedsReplacement"))
)
if mibBuilder.loadTexts:
    rubrikNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rubrikCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 49929, 11, 1, 1)
)
rubrikCompliance1.setObjects(
      *(("RUBRIK-MIB", "rubrikNotifications"),
        ("RUBRIK-MIB", "rubrikObjects"))
)
if mibBuilder.loadTexts:
    rubrikCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUBRIK-MIB",
    **{"rubrik": rubrik,
       "brikSystemMibs": brikSystemMibs,
       "cluster": cluster,
       "storage": storage,
       "usedInBytes": usedInBytes,
       "availableInBytes": availableInBytes,
       "totalInBytes": totalInBytes,
       "runwayRemaining": runwayRemaining,
       "bandwidth": bandwidth,
       "archiveAvgBytesPerSecondLastHour": archiveAvgBytesPerSecondLastHour,
       "system": system,
       "totalNodes": totalNodes,
       "activeNodes": activeNodes,
       "streamsCount": streamsCount,
       "brikSystemTraps": brikSystemTraps,
       "hardwareTrapsPrefix": hardwareTrapsPrefix,
       "hardwareTraps": hardwareTraps,
       "networkInterfaceDown": networkInterfaceDown,
       "networkInterfaceUp": networkInterfaceUp,
       "ntpOutofSync": ntpOutofSync,
       "chassisNeedsReplacement": chassisNeedsReplacement,
       "dimmError": dimmError,
       "biosError": biosError,
       "nodeNeedsReplacement": nodeNeedsReplacement,
       "powerSupplyNeedsReplacement": powerSupplyNeedsReplacement,
       "chassisRecovered": chassisRecovered,
       "dimmRecovered": dimmRecovered,
       "biosRecovered": biosRecovered,
       "powerSupplyRecovered": powerSupplyRecovered,
       "powerSupplyNeedsCheck": powerSupplyNeedsCheck,
       "cmosNeedsReplacement": cmosNeedsReplacement,
       "diskTrapsPrefix": diskTrapsPrefix,
       "diskTraps": diskTraps,
       "diskLocked": diskLocked,
       "diskLost": diskLost,
       "diskRecovered": diskRecovered,
       "diskRemovedFailure": diskRemovedFailure,
       "diskRemovedSuccess": diskRemovedSuccess,
       "diskSetupFailure": diskSetupFailure,
       "diskSetupSuccess": diskSetupSuccess,
       "diskUnformatted": diskUnformatted,
       "diskUnhealthy": diskUnhealthy,
       "nodeTrapsPrefix": nodeTrapsPrefix,
       "nodeTraps": nodeTraps,
       "nodeAddFailure": nodeAddFailure,
       "nodeAddSuccess": nodeAddSuccess,
       "nodeAutoRemoveSuccess": nodeAutoRemoveSuccess,
       "nodeAutoRemoveFailure": nodeAutoRemoveFailure,
       "nodeAutoRemoveDetected": nodeAutoRemoveDetected,
       "nodeDecommissionFailure": nodeDecommissionFailure,
       "nodeDecommissionSuccess": nodeDecommissionSuccess,
       "nodeDownInRecovery": nodeDownInRecovery,
       "nodeDown": nodeDown,
       "nodeUp": nodeUp,
       "nodeRecommissionSuccess": nodeRecommissionSuccess,
       "nodeRecommissionFailure": nodeRecommissionFailure,
       "nodeRemoveSuccess": nodeRemoveSuccess,
       "nodeRemoveFailure": nodeRemoveFailure,
       "nodeTpmNeedsUpgrade": nodeTpmNeedsUpgrade,
       "nodePeriodicTaskFailure": nodePeriodicTaskFailure,
       "nodeNtpConfigCheckFailure": nodeNtpConfigCheckFailure,
       "nodeDecommissionInProgress": nodeDecommissionInProgress,
       "nodeDecommissionStarted": nodeDecommissionStarted,
       "healthMonitorPolicyCritical": healthMonitorPolicyCritical,
       "healthMonitorPolicyWarning": healthMonitorPolicyWarning,
       "brikBackupTrapsPrefix": brikBackupTrapsPrefix,
       "brikBackupTraps": brikBackupTraps,
       "backupJobFailure": backupJobFailure,
       "brikNotificationObjects": brikNotificationObjects,
       "brikNotificationMessage": brikNotificationMessage,
       "rubrikConformance": rubrikConformance,
       "rubrikCompliances": rubrikCompliances,
       "rubrikCompliance1": rubrikCompliance1,
       "rubrikGroups": rubrikGroups,
       "rubrikNotifications": rubrikNotifications,
       "rubrikObjects": rubrikObjects}
)
