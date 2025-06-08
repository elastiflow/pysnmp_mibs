# SNMP MIB module (COHESITY-APPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cohesity_47421/COHESITY-APPLIANCE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:50:28 2025
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

caMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47421)
)
if mibBuilder.loadTexts:
    caMIB.setRevisions(
        ("2016-07-13 04:16",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NotifsGroup_ObjectIdentity = ObjectIdentity
notifsGroup = _NotifsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47421, 0)
)
_CaEventVariables_ObjectIdentity = ObjectIdentity
caEventVariables = _CaEventVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47421, 1)
)
_DiskIsBadEvent_Type = DisplayString
_DiskIsBadEvent_Object = MibScalar
diskIsBadEvent = _DiskIsBadEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 1),
    _DiskIsBadEvent_Type()
)
diskIsBadEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIsBadEvent.setStatus("current")
_NodeIsDownEvent_Type = DisplayString
_NodeIsDownEvent_Object = MibScalar
nodeIsDownEvent = _NodeIsDownEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 2),
    _NodeIsDownEvent_Type()
)
nodeIsDownEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIsDownEvent.setStatus("current")
_DiskOfflineEvent_Type = DisplayString
_DiskOfflineEvent_Object = MibScalar
diskOfflineEvent = _DiskOfflineEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 3),
    _DiskOfflineEvent_Type()
)
diskOfflineEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskOfflineEvent.setStatus("current")
_UpgradeFailedEvent_Type = DisplayString
_UpgradeFailedEvent_Object = MibScalar
upgradeFailedEvent = _UpgradeFailedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 4),
    _UpgradeFailedEvent_Type()
)
upgradeFailedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFailedEvent.setStatus("current")
_NewDiskFoundEvent_Type = DisplayString
_NewDiskFoundEvent_Object = MibScalar
newDiskFoundEvent = _NewDiskFoundEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 5),
    _NewDiskFoundEvent_Type()
)
newDiskFoundEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newDiskFoundEvent.setStatus("current")
_LogsDiskSpaceLowEvent_Type = DisplayString
_LogsDiskSpaceLowEvent_Object = MibScalar
logsDiskSpaceLowEvent = _LogsDiskSpaceLowEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 6),
    _LogsDiskSpaceLowEvent_Type()
)
logsDiskSpaceLowEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logsDiskSpaceLowEvent.setStatus("current")
_TimeServiceEvent_Type = DisplayString
_TimeServiceEvent_Object = MibScalar
timeServiceEvent = _TimeServiceEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 7),
    _TimeServiceEvent_Type()
)
timeServiceEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServiceEvent.setStatus("current")
_MissingDiskEvent_Type = DisplayString
_MissingDiskEvent_Object = MibScalar
missingDiskEvent = _MissingDiskEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 8),
    _MissingDiskEvent_Type()
)
missingDiskEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    missingDiskEvent.setStatus("current")
_WriteLimitEvent_Type = DisplayString
_WriteLimitEvent_Object = MibScalar
writeLimitEvent = _WriteLimitEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 9),
    _WriteLimitEvent_Type()
)
writeLimitEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeLimitEvent.setStatus("current")
_MemUncorrectableEccEvent_Type = DisplayString
_MemUncorrectableEccEvent_Object = MibScalar
memUncorrectableEccEvent = _MemUncorrectableEccEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 10),
    _MemUncorrectableEccEvent_Type()
)
memUncorrectableEccEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUncorrectableEccEvent.setStatus("current")
_MemCorrectableEccEvent_Type = DisplayString
_MemCorrectableEccEvent_Object = MibScalar
memCorrectableEccEvent = _MemCorrectableEccEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 11),
    _MemCorrectableEccEvent_Type()
)
memCorrectableEccEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCorrectableEccEvent.setStatus("current")
_WatchdogTriggeredEvent_Type = DisplayString
_WatchdogTriggeredEvent_Object = MibScalar
watchdogTriggeredEvent = _WatchdogTriggeredEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 12),
    _WatchdogTriggeredEvent_Type()
)
watchdogTriggeredEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogTriggeredEvent.setStatus("current")
_TempOutOfHighRangeEvent_Type = DisplayString
_TempOutOfHighRangeEvent_Object = MibScalar
tempOutOfHighRangeEvent = _TempOutOfHighRangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 13),
    _TempOutOfHighRangeEvent_Type()
)
tempOutOfHighRangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempOutOfHighRangeEvent.setStatus("current")
_TempOutOfLowRangeEvent_Type = DisplayString
_TempOutOfLowRangeEvent_Object = MibScalar
tempOutOfLowRangeEvent = _TempOutOfLowRangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 14),
    _TempOutOfLowRangeEvent_Type()
)
tempOutOfLowRangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempOutOfLowRangeEvent.setStatus("current")
_VoltOutOfHighRangeEvent_Type = DisplayString
_VoltOutOfHighRangeEvent_Object = MibScalar
voltOutOfHighRangeEvent = _VoltOutOfHighRangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 15),
    _VoltOutOfHighRangeEvent_Type()
)
voltOutOfHighRangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltOutOfHighRangeEvent.setStatus("current")
_VoltOutOfLowRangeEvent_Type = DisplayString
_VoltOutOfLowRangeEvent_Object = MibScalar
voltOutOfLowRangeEvent = _VoltOutOfLowRangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 16),
    _VoltOutOfLowRangeEvent_Type()
)
voltOutOfLowRangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltOutOfLowRangeEvent.setStatus("current")
_HddDriveRemovedEvent_Type = DisplayString
_HddDriveRemovedEvent_Object = MibScalar
hddDriveRemovedEvent = _HddDriveRemovedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 17),
    _HddDriveRemovedEvent_Type()
)
hddDriveRemovedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddDriveRemovedEvent.setStatus("current")
_HddDriveInsertedEvent_Type = DisplayString
_HddDriveInsertedEvent_Object = MibScalar
hddDriveInsertedEvent = _HddDriveInsertedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 18),
    _HddDriveInsertedEvent_Type()
)
hddDriveInsertedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddDriveInsertedEvent.setStatus("current")
_HddDriveFaultEvent_Type = DisplayString
_HddDriveFaultEvent_Object = MibScalar
hddDriveFaultEvent = _HddDriveFaultEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 19),
    _HddDriveFaultEvent_Type()
)
hddDriveFaultEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddDriveFaultEvent.setStatus("current")
_PowerSupplyRemovedEvent_Type = DisplayString
_PowerSupplyRemovedEvent_Object = MibScalar
powerSupplyRemovedEvent = _PowerSupplyRemovedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 20),
    _PowerSupplyRemovedEvent_Type()
)
powerSupplyRemovedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRemovedEvent.setStatus("current")
_PowerSupplyInsertedEvent_Type = DisplayString
_PowerSupplyInsertedEvent_Object = MibScalar
powerSupplyInsertedEvent = _PowerSupplyInsertedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 21),
    _PowerSupplyInsertedEvent_Type()
)
powerSupplyInsertedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyInsertedEvent.setStatus("current")
_LanCableRemovedEvent_Type = DisplayString
_LanCableRemovedEvent_Object = MibScalar
lanCableRemovedEvent = _LanCableRemovedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 22),
    _LanCableRemovedEvent_Type()
)
lanCableRemovedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCableRemovedEvent.setStatus("current")
_LanCableInsertedEvent_Type = DisplayString
_LanCableInsertedEvent_Object = MibScalar
lanCableInsertedEvent = _LanCableInsertedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 23),
    _LanCableInsertedEvent_Type()
)
lanCableInsertedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCableInsertedEvent.setStatus("current")
_IpmiSelClearedEvent_Type = DisplayString
_IpmiSelClearedEvent_Object = MibScalar
ipmiSelClearedEvent = _IpmiSelClearedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 24),
    _IpmiSelClearedEvent_Type()
)
ipmiSelClearedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiSelClearedEvent.setStatus("current")
_NodeRebootedEvent_Type = DisplayString
_NodeRebootedEvent_Object = MibScalar
nodeRebootedEvent = _NodeRebootedEvent_Object(
    (1, 3, 6, 1, 4, 1, 47421, 1, 25),
    _NodeRebootedEvent_Type()
)
nodeRebootedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRebootedEvent.setStatus("current")
_CaMIBConformance_ObjectIdentity = ObjectIdentity
caMIBConformance = _CaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47421, 2)
)
_CaMIBCompliances_ObjectIdentity = ObjectIdentity
caMIBCompliances = _CaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47421, 2, 1)
)
_CaMIBGroups_ObjectIdentity = ObjectIdentity
caMIBGroups = _CaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47421, 2, 2)
)
_BasicGroup_ObjectIdentity = ObjectIdentity
basicGroup = _BasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47421, 3)
)
_StatsGroup_ObjectIdentity = ObjectIdentity
statsGroup = _StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47421, 4)
)

# Managed Objects groups

caObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47421, 2, 2, 1)
)
caObjectGroup.setObjects(
      *(("COHESITY-APPLIANCE-MIB", "diskIsBadEvent"),
        ("COHESITY-APPLIANCE-MIB", "nodeIsDownEvent"),
        ("COHESITY-APPLIANCE-MIB", "diskOfflineEvent"),
        ("COHESITY-APPLIANCE-MIB", "upgradeFailedEvent"),
        ("COHESITY-APPLIANCE-MIB", "newDiskFoundEvent"),
        ("COHESITY-APPLIANCE-MIB", "logsDiskSpaceLowEvent"),
        ("COHESITY-APPLIANCE-MIB", "timeServiceEvent"),
        ("COHESITY-APPLIANCE-MIB", "missingDiskEvent"),
        ("COHESITY-APPLIANCE-MIB", "writeLimitEvent"),
        ("COHESITY-APPLIANCE-MIB", "memUncorrectableEccEvent"),
        ("COHESITY-APPLIANCE-MIB", "memCorrectableEccEvent"),
        ("COHESITY-APPLIANCE-MIB", "watchdogTriggeredEvent"),
        ("COHESITY-APPLIANCE-MIB", "tempOutOfHighRangeEvent"),
        ("COHESITY-APPLIANCE-MIB", "tempOutOfLowRangeEvent"),
        ("COHESITY-APPLIANCE-MIB", "voltOutOfHighRangeEvent"),
        ("COHESITY-APPLIANCE-MIB", "voltOutOfLowRangeEvent"),
        ("COHESITY-APPLIANCE-MIB", "hddDriveRemovedEvent"),
        ("COHESITY-APPLIANCE-MIB", "hddDriveInsertedEvent"),
        ("COHESITY-APPLIANCE-MIB", "hddDriveFaultEvent"),
        ("COHESITY-APPLIANCE-MIB", "powerSupplyRemovedEvent"),
        ("COHESITY-APPLIANCE-MIB", "powerSupplyInsertedEvent"),
        ("COHESITY-APPLIANCE-MIB", "lanCableRemovedEvent"),
        ("COHESITY-APPLIANCE-MIB", "lanCableInsertedEvent"),
        ("COHESITY-APPLIANCE-MIB", "ipmiSelClearedEvent"),
        ("COHESITY-APPLIANCE-MIB", "nodeRebootedEvent"))
)
if mibBuilder.loadTexts:
    caObjectGroup.setStatus("current")


# Notification objects

diskIsBadNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 1)
)
diskIsBadNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "diskIsBadEvent")
)
if mibBuilder.loadTexts:
    diskIsBadNotif.setStatus(
        "current"
    )

nodeIsDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 2)
)
nodeIsDownNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "nodeIsDownEvent")
)
if mibBuilder.loadTexts:
    nodeIsDownNotif.setStatus(
        "current"
    )

diskOfflineNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 3)
)
diskOfflineNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "diskOfflineEvent")
)
if mibBuilder.loadTexts:
    diskOfflineNotif.setStatus(
        "current"
    )

upgradeFailedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 4)
)
upgradeFailedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "upgradeFailedEvent")
)
if mibBuilder.loadTexts:
    upgradeFailedNotif.setStatus(
        "current"
    )

newDiskFoundNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 5)
)
newDiskFoundNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "newDiskFoundEvent")
)
if mibBuilder.loadTexts:
    newDiskFoundNotif.setStatus(
        "current"
    )

logsDiskSpaceLowNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 6)
)
logsDiskSpaceLowNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "logsDiskSpaceLowEvent")
)
if mibBuilder.loadTexts:
    logsDiskSpaceLowNotif.setStatus(
        "current"
    )

timeServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 7)
)
timeServiceNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "timeServiceEvent")
)
if mibBuilder.loadTexts:
    timeServiceNotif.setStatus(
        "current"
    )

missingDiskNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 8)
)
missingDiskNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "missingDiskEvent")
)
if mibBuilder.loadTexts:
    missingDiskNotif.setStatus(
        "current"
    )

writeLimitNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 9)
)
writeLimitNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "writeLimitEvent")
)
if mibBuilder.loadTexts:
    writeLimitNotif.setStatus(
        "current"
    )

memUncorrectableEccNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 10)
)
memUncorrectableEccNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "memUncorrectableEccEvent")
)
if mibBuilder.loadTexts:
    memUncorrectableEccNotif.setStatus(
        "current"
    )

memCorrectableEccNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 11)
)
memCorrectableEccNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "memCorrectableEccEvent")
)
if mibBuilder.loadTexts:
    memCorrectableEccNotif.setStatus(
        "current"
    )

watchdogTriggeredNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 12)
)
watchdogTriggeredNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "watchdogTriggeredEvent")
)
if mibBuilder.loadTexts:
    watchdogTriggeredNotif.setStatus(
        "current"
    )

tempOutOfHighRangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 13)
)
tempOutOfHighRangeNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "tempOutOfHighRangeEvent")
)
if mibBuilder.loadTexts:
    tempOutOfHighRangeNotif.setStatus(
        "current"
    )

tempOutOfLowRangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 14)
)
tempOutOfLowRangeNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "tempOutOfLowRangeEvent")
)
if mibBuilder.loadTexts:
    tempOutOfLowRangeNotif.setStatus(
        "current"
    )

voltOutOfHighRangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 15)
)
voltOutOfHighRangeNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "voltOutOfHighRangeEvent")
)
if mibBuilder.loadTexts:
    voltOutOfHighRangeNotif.setStatus(
        "current"
    )

voltOutOfLowRangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 16)
)
voltOutOfLowRangeNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "voltOutOfLowRangeEvent")
)
if mibBuilder.loadTexts:
    voltOutOfLowRangeNotif.setStatus(
        "current"
    )

hddDriveRemovedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 17)
)
hddDriveRemovedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "hddDriveRemovedEvent")
)
if mibBuilder.loadTexts:
    hddDriveRemovedNotif.setStatus(
        "current"
    )

hddDriveInsertedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 18)
)
hddDriveInsertedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "hddDriveInsertedEvent")
)
if mibBuilder.loadTexts:
    hddDriveInsertedNotif.setStatus(
        "current"
    )

hddDriveFaultNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 19)
)
hddDriveFaultNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "hddDriveFaultEvent")
)
if mibBuilder.loadTexts:
    hddDriveFaultNotif.setStatus(
        "current"
    )

powerSupplyRemovedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 20)
)
powerSupplyRemovedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "powerSupplyRemovedEvent")
)
if mibBuilder.loadTexts:
    powerSupplyRemovedNotif.setStatus(
        "current"
    )

powerSupplyInsertedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 21)
)
powerSupplyInsertedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "powerSupplyInsertedEvent")
)
if mibBuilder.loadTexts:
    powerSupplyInsertedNotif.setStatus(
        "current"
    )

lanCableRemovedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 22)
)
lanCableRemovedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "lanCableRemovedEvent")
)
if mibBuilder.loadTexts:
    lanCableRemovedNotif.setStatus(
        "current"
    )

lanCableInsertedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 23)
)
lanCableInsertedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "lanCableInsertedEvent")
)
if mibBuilder.loadTexts:
    lanCableInsertedNotif.setStatus(
        "current"
    )

ipmiSelClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 24)
)
ipmiSelClearedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "ipmiSelClearedEvent")
)
if mibBuilder.loadTexts:
    ipmiSelClearedNotif.setStatus(
        "current"
    )

nodeRebootedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 47421, 0, 25)
)
nodeRebootedNotif.setObjects(
    ("COHESITY-APPLIANCE-MIB", "nodeRebootedEvent")
)
if mibBuilder.loadTexts:
    nodeRebootedNotif.setStatus(
        "current"
    )


# Notifications groups

caNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47421, 2, 2, 2)
)
caNotificationGroup.setObjects(
      *(("COHESITY-APPLIANCE-MIB", "diskIsBadNotif"),
        ("COHESITY-APPLIANCE-MIB", "nodeIsDownNotif"),
        ("COHESITY-APPLIANCE-MIB", "diskOfflineNotif"),
        ("COHESITY-APPLIANCE-MIB", "upgradeFailedNotif"),
        ("COHESITY-APPLIANCE-MIB", "newDiskFoundNotif"),
        ("COHESITY-APPLIANCE-MIB", "logsDiskSpaceLowNotif"),
        ("COHESITY-APPLIANCE-MIB", "timeServiceNotif"),
        ("COHESITY-APPLIANCE-MIB", "missingDiskNotif"),
        ("COHESITY-APPLIANCE-MIB", "writeLimitNotif"),
        ("COHESITY-APPLIANCE-MIB", "memUncorrectableEccNotif"),
        ("COHESITY-APPLIANCE-MIB", "memCorrectableEccNotif"),
        ("COHESITY-APPLIANCE-MIB", "watchdogTriggeredNotif"),
        ("COHESITY-APPLIANCE-MIB", "tempOutOfHighRangeNotif"),
        ("COHESITY-APPLIANCE-MIB", "tempOutOfLowRangeNotif"),
        ("COHESITY-APPLIANCE-MIB", "voltOutOfHighRangeNotif"),
        ("COHESITY-APPLIANCE-MIB", "voltOutOfLowRangeNotif"),
        ("COHESITY-APPLIANCE-MIB", "hddDriveRemovedNotif"),
        ("COHESITY-APPLIANCE-MIB", "hddDriveInsertedNotif"),
        ("COHESITY-APPLIANCE-MIB", "hddDriveFaultNotif"),
        ("COHESITY-APPLIANCE-MIB", "powerSupplyRemovedNotif"),
        ("COHESITY-APPLIANCE-MIB", "powerSupplyInsertedNotif"),
        ("COHESITY-APPLIANCE-MIB", "lanCableRemovedNotif"),
        ("COHESITY-APPLIANCE-MIB", "lanCableInsertedNotif"),
        ("COHESITY-APPLIANCE-MIB", "ipmiSelClearedNotif"),
        ("COHESITY-APPLIANCE-MIB", "nodeRebootedNotif"))
)
if mibBuilder.loadTexts:
    caNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

caMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47421, 2, 1, 1)
)
caMIBCompliance.setObjects(
      *(("COHESITY-APPLIANCE-MIB", "caObjectGroup"),
        ("COHESITY-APPLIANCE-MIB", "caNotificationGroup"))
)
if mibBuilder.loadTexts:
    caMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COHESITY-APPLIANCE-MIB",
    **{"caMIB": caMIB,
       "notifsGroup": notifsGroup,
       "diskIsBadNotif": diskIsBadNotif,
       "nodeIsDownNotif": nodeIsDownNotif,
       "diskOfflineNotif": diskOfflineNotif,
       "upgradeFailedNotif": upgradeFailedNotif,
       "newDiskFoundNotif": newDiskFoundNotif,
       "logsDiskSpaceLowNotif": logsDiskSpaceLowNotif,
       "timeServiceNotif": timeServiceNotif,
       "missingDiskNotif": missingDiskNotif,
       "writeLimitNotif": writeLimitNotif,
       "memUncorrectableEccNotif": memUncorrectableEccNotif,
       "memCorrectableEccNotif": memCorrectableEccNotif,
       "watchdogTriggeredNotif": watchdogTriggeredNotif,
       "tempOutOfHighRangeNotif": tempOutOfHighRangeNotif,
       "tempOutOfLowRangeNotif": tempOutOfLowRangeNotif,
       "voltOutOfHighRangeNotif": voltOutOfHighRangeNotif,
       "voltOutOfLowRangeNotif": voltOutOfLowRangeNotif,
       "hddDriveRemovedNotif": hddDriveRemovedNotif,
       "hddDriveInsertedNotif": hddDriveInsertedNotif,
       "hddDriveFaultNotif": hddDriveFaultNotif,
       "powerSupplyRemovedNotif": powerSupplyRemovedNotif,
       "powerSupplyInsertedNotif": powerSupplyInsertedNotif,
       "lanCableRemovedNotif": lanCableRemovedNotif,
       "lanCableInsertedNotif": lanCableInsertedNotif,
       "ipmiSelClearedNotif": ipmiSelClearedNotif,
       "nodeRebootedNotif": nodeRebootedNotif,
       "caEventVariables": caEventVariables,
       "diskIsBadEvent": diskIsBadEvent,
       "nodeIsDownEvent": nodeIsDownEvent,
       "diskOfflineEvent": diskOfflineEvent,
       "upgradeFailedEvent": upgradeFailedEvent,
       "newDiskFoundEvent": newDiskFoundEvent,
       "logsDiskSpaceLowEvent": logsDiskSpaceLowEvent,
       "timeServiceEvent": timeServiceEvent,
       "missingDiskEvent": missingDiskEvent,
       "writeLimitEvent": writeLimitEvent,
       "memUncorrectableEccEvent": memUncorrectableEccEvent,
       "memCorrectableEccEvent": memCorrectableEccEvent,
       "watchdogTriggeredEvent": watchdogTriggeredEvent,
       "tempOutOfHighRangeEvent": tempOutOfHighRangeEvent,
       "tempOutOfLowRangeEvent": tempOutOfLowRangeEvent,
       "voltOutOfHighRangeEvent": voltOutOfHighRangeEvent,
       "voltOutOfLowRangeEvent": voltOutOfLowRangeEvent,
       "hddDriveRemovedEvent": hddDriveRemovedEvent,
       "hddDriveInsertedEvent": hddDriveInsertedEvent,
       "hddDriveFaultEvent": hddDriveFaultEvent,
       "powerSupplyRemovedEvent": powerSupplyRemovedEvent,
       "powerSupplyInsertedEvent": powerSupplyInsertedEvent,
       "lanCableRemovedEvent": lanCableRemovedEvent,
       "lanCableInsertedEvent": lanCableInsertedEvent,
       "ipmiSelClearedEvent": ipmiSelClearedEvent,
       "nodeRebootedEvent": nodeRebootedEvent,
       "caMIBConformance": caMIBConformance,
       "caMIBCompliances": caMIBCompliances,
       "caMIBCompliance": caMIBCompliance,
       "caMIBGroups": caMIBGroups,
       "caObjectGroup": caObjectGroup,
       "caNotificationGroup": caNotificationGroup,
       "basicGroup": basicGroup,
       "statsGroup": statsGroup}
)
