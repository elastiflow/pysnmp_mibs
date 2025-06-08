# SNMP MIB module (SDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/f5_3375/SDC-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 21:18:56 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

traffix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3)
)
if mibBuilder.loadTexts:
    traffix.setRevisions(
        ("2015-04-29 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ComponentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10000,
              15000,
              20000,
              25000,
              30000,
              35000,
              40000,
              45000,
              50000,
              55000,
              60000,
              65000,
              70000,
              75000,
              80000,
              85000,
              90000,
              95000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("sdc", 10000),
          ("pool", 15000),
          ("peer", 20000),
          ("transport", 25000),
          ("files", 30000),
          ("statistics", 35000),
          ("cpf", 40000),
          ("fep", 45000),
          ("dns", 50000),
          ("tripo", 55000),
          ("slrf", 60000),
          ("splunk", 65000),
          ("ss7", 70000),
          ("nms", 75000),
          ("configManager", 80000),
          ("machine", 85000),
          ("ui", 90000),
          ("virtualServer", 95000),
          ("external", 100000))
    )



class AlarmEventCategory(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("license", 1),
          ("interSite", 2),
          ("eMSAndSDC", 3),
          ("machineResources", 4),
          ("poolStatus", 5),
          ("peerStatus", 6),
          ("virtualServers", 7),
          ("processesGeneral", 8),
          ("internalComponents", 9),
          ("notifications", 10))
    )



class AlarmEventId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10001,
              10002,
              10003,
              11001,
              11002,
              11003,
              12001,
              13001,
              13002,
              13003,
              13004,
              13005,
              13006,
              13007,
              14001,
              14002,
              14003,
              14004,
              15001,
              15002,
              15003,
              15004,
              15005,
              15006,
              15007,
              15008,
              15009,
              15010,
              16001,
              17001,
              18001,
              18002,
              18003,
              18004,
              18005,
              18006,
              18007,
              18008,
              18009,
              18010,
              18011,
              18012,
              18013,
              18014,
              18015,
              18016,
              18017,
              18018,
              18019,
              18020,
              18021,
              18022,
              18023,
              18024,
              18025,
              18026,
              18027,
              18028,
              1019001,
              1019002,
              1019003,
              1019004,
              1019005,
              1019006,
              1019007,
              1019008,
              1019009,
              1019010,
              1019011,
              1019012,
              1019013,
              1019014,
              1019015,
              1019016,
              1019017,
              1019018,
              2147483644,
              2147483645,
              2147483646,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("sdcLicenseExpiration", 10001),
          ("sdcLicenseMPS", 10002),
          ("ss7LicenseExpiration", 10003),
          ("geoSdcProxyConnection", 11001),
          ("geoSdcTripoConnection", 11002),
          ("geoSdcProxyNotMarked", 11003),
          ("cmCommunicationEmsAndSDC", 12001),
          ("machinePhysicalMemory", 13001),
          ("machineSwapMemory", 13002),
          ("machineCpuUsage", 13003),
          ("machineLoadAverage", 13004),
          ("machineDiskPartition", 13005),
          ("machineNicStatus", 13006),
          ("machineCpuStealUsage", 13007),
          ("poolHealthTimeouts", 14001),
          ("poolHealthErrorAnswers", 14002),
          ("poolStateChanged", 14003),
          ("poolRate", 14004),
          ("peerHealthIOQueue", 15001),
          ("peerHealthOosPercentage", 15002),
          ("peerHealthRTTAverage", 15003),
          ("peerHealthErrorAnswers", 15004),
          ("peerHealthTimeouts", 15005),
          ("outgoingPeerRate", 15006),
          ("incomingPeerRate", 15007),
          ("peerHealthPendingRequests", 15008),
          ("peerStateChanged", 15009),
          ("peerSctpLink", 15010),
          ("vsStateChanged", 16001),
          ("sdcComponentStatus", 17001),
          ("communicationOfCmFep", 18001),
          ("communicationOfCmCpf", 18002),
          ("communicationOfCmMateCm", 18003),
          ("communicationOfCmUi", 18004),
          ("communicationOfCmNms", 18005),
          ("communicationOfFepCpf", 18006),
          ("communicationOfCpfTripo", 18007),
          ("communicationOfNmsFep", 18008),
          ("communicationOfNmsCpf", 18009),
          ("communicationOfNmsUi", 18010),
          ("communicationOfNmsTripo", 18011),
          ("sdcComponentHealthRequestQOverload", 18012),
          ("sdcComponentHealthAnswerQOverload", 18013),
          ("sdcComponentHealthAsynchronousQOverload", 18014),
          ("sdcComponentHealthRequestQThreshold", 18015),
          ("sdcComponentHealthAnswerQThreshold", 18016),
          ("sdcComponentHealthAsynchronousQThreshold", 18017),
          ("sdcComponentTPSOverload", 18018),
          ("sdcComponentRateLimit", 18019),
          ("sdcPendingRequestsOverload", 18020),
          ("sdcPendingRequests", 18021),
          ("sdcComponentFailureRate", 18022),
          ("fepCpfCommunicationControl", 18023),
          ("communicationOfTripoMateTripo", 18024),
          ("sdcProcessStorageOverflow", 18025),
          ("sdcProcessQueueOverflow", 18026),
          ("geoSdcTripoFullReSyncStarted", 18027),
          ("geoSdcTripoSrrReSyncStarted", 18028),
          ("peerAclRejected", 1019001),
          ("peerCapacityRejected", 1019002),
          ("sdcScriptInvocationFailed", 1019003),
          ("sdcUserAuthentication", 1019004),
          ("sdcMaxTracePerDayReached", 1019005),
          ("sdcMaxTraceTPSReached", 1019006),
          ("sdcDnsResolvingFailure", 1019007),
          ("fileServerDirectory", 1019008),
          ("fileServerFile", 1019009),
          ("fileServerCloseFile", 1019010),
          ("fileServerRenameFile", 1019011),
          ("fileServerSplitFile", 1019012),
          ("sdcProcessGcLoop", 1019013),
          ("splunkLicenseUsage", 1019014),
          ("splunkLicenseViolation", 1019015),
          ("splunkLicenseLock", 1019016),
          ("sdcMonitProcessRestart", 1019017),
          ("vipAppStateChange", 1019018),
          ("allCustomEvents", 2147483644),
          ("allEvents", 2147483645),
          ("allAlarms", 2147483646),
          ("allAlarmsAndEvents", 2147483647))
    )



class AlarmSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Sdc_ObjectIdentity = ObjectIdentity
sdc = _Sdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1)
)
_SdcMgmt_ObjectIdentity = ObjectIdentity
sdcMgmt = _SdcMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4)
)
_SdcNotifObjects_ObjectIdentity = ObjectIdentity
sdcNotifObjects = _SdcNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 1)
)
_SdcAlarms_ObjectIdentity = ObjectIdentity
sdcAlarms = _SdcAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3)
)
_SdcLicenseMppbl_ObjectIdentity = ObjectIdentity
sdcLicenseMppbl = _SdcLicenseMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    sdcLicenseMppbl.setStatus("current")
_SdcLicenseEvents_ObjectIdentity = ObjectIdentity
sdcLicenseEvents = _SdcLicenseEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 1, 0)
)
if mibBuilder.loadTexts:
    sdcLicenseEvents.setStatus("current")
_SdcInterSiteMppbl_ObjectIdentity = ObjectIdentity
sdcInterSiteMppbl = _SdcInterSiteMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    sdcInterSiteMppbl.setStatus("current")
_SdcInterSiteEvents_ObjectIdentity = ObjectIdentity
sdcInterSiteEvents = _SdcInterSiteEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 2, 0)
)
if mibBuilder.loadTexts:
    sdcInterSiteEvents.setStatus("current")
_SdcEMSAndSDCMppbl_ObjectIdentity = ObjectIdentity
sdcEMSAndSDCMppbl = _SdcEMSAndSDCMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    sdcEMSAndSDCMppbl.setStatus("current")
_SdcEMSAndSDCEvents_ObjectIdentity = ObjectIdentity
sdcEMSAndSDCEvents = _SdcEMSAndSDCEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 3, 0)
)
if mibBuilder.loadTexts:
    sdcEMSAndSDCEvents.setStatus("current")
_SdcMachineResourcesMppbl_ObjectIdentity = ObjectIdentity
sdcMachineResourcesMppbl = _SdcMachineResourcesMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    sdcMachineResourcesMppbl.setStatus("current")
_SdcMachineResourcesEvents_ObjectIdentity = ObjectIdentity
sdcMachineResourcesEvents = _SdcMachineResourcesEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4, 0)
)
if mibBuilder.loadTexts:
    sdcMachineResourcesEvents.setStatus("current")
_SdcPoolStatusMppbl_ObjectIdentity = ObjectIdentity
sdcPoolStatusMppbl = _SdcPoolStatusMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 5)
)
if mibBuilder.loadTexts:
    sdcPoolStatusMppbl.setStatus("current")
_SdcPoolStatusEvents_ObjectIdentity = ObjectIdentity
sdcPoolStatusEvents = _SdcPoolStatusEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 5, 0)
)
if mibBuilder.loadTexts:
    sdcPoolStatusEvents.setStatus("current")
_SdcPeerStatusMppbl_ObjectIdentity = ObjectIdentity
sdcPeerStatusMppbl = _SdcPeerStatusMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6)
)
if mibBuilder.loadTexts:
    sdcPeerStatusMppbl.setStatus("current")
_SdcPeerStatusEvents_ObjectIdentity = ObjectIdentity
sdcPeerStatusEvents = _SdcPeerStatusEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0)
)
if mibBuilder.loadTexts:
    sdcPeerStatusEvents.setStatus("current")
_SdcVirtualServersMppbl_ObjectIdentity = ObjectIdentity
sdcVirtualServersMppbl = _SdcVirtualServersMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 7)
)
if mibBuilder.loadTexts:
    sdcVirtualServersMppbl.setStatus("current")
_SdcVirtualServersEvents_ObjectIdentity = ObjectIdentity
sdcVirtualServersEvents = _SdcVirtualServersEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 7, 0)
)
if mibBuilder.loadTexts:
    sdcVirtualServersEvents.setStatus("current")
_SdcProcessesGeneralMppbl_ObjectIdentity = ObjectIdentity
sdcProcessesGeneralMppbl = _SdcProcessesGeneralMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 8)
)
if mibBuilder.loadTexts:
    sdcProcessesGeneralMppbl.setStatus("current")
_SdcProcessesGeneralEvents_ObjectIdentity = ObjectIdentity
sdcProcessesGeneralEvents = _SdcProcessesGeneralEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 8, 0)
)
if mibBuilder.loadTexts:
    sdcProcessesGeneralEvents.setStatus("current")
_SdcInternalComponentsMppbl_ObjectIdentity = ObjectIdentity
sdcInternalComponentsMppbl = _SdcInternalComponentsMppbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9)
)
if mibBuilder.loadTexts:
    sdcInternalComponentsMppbl.setStatus("current")
_SdcInternalComponentsEvents_ObjectIdentity = ObjectIdentity
sdcInternalComponentsEvents = _SdcInternalComponentsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0)
)
if mibBuilder.loadTexts:
    sdcInternalComponentsEvents.setStatus("current")
_SdcEvents_ObjectIdentity = ObjectIdentity
sdcEvents = _SdcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4)
)
_SdcBasicEventsMappable_ObjectIdentity = ObjectIdentity
sdcBasicEventsMappable = _SdcBasicEventsMappable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    sdcBasicEventsMappable.setStatus("current")
_SdcNotificationEvents_ObjectIdentity = ObjectIdentity
sdcNotificationEvents = _SdcNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0)
)
if mibBuilder.loadTexts:
    sdcNotificationEvents.setStatus("current")
_CpfCustomAlarms_ObjectIdentity = ObjectIdentity
cpfCustomAlarms = _CpfCustomAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 5)
)
_TrapManagement_ObjectIdentity = ObjectIdentity
trapManagement = _TrapManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6)
)
_ActiveAlarmTable_Object = MibTable
activeAlarmTable = _ActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    activeAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "SDC-MIB", "alarmSourceComponent"),
    (0, "SDC-MIB", "alarmedManagedObject"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")


class _AlarmSourceComponent_Type(DisplayString):
    """Custom type alarmSourceComponent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AlarmSourceComponent_Type.__name__ = "DisplayString"
_AlarmSourceComponent_Object = MibTableColumn
alarmSourceComponent = _AlarmSourceComponent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 1),
    _AlarmSourceComponent_Type()
)
alarmSourceComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmSourceComponent.setStatus("current")


class _AlarmedManagedObject_Type(DisplayString):
    """Custom type alarmedManagedObject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlarmedManagedObject_Type.__name__ = "DisplayString"
_AlarmedManagedObject_Object = MibTableColumn
alarmedManagedObject = _AlarmedManagedObject_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 2),
    _AlarmedManagedObject_Type()
)
alarmedManagedObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmedManagedObject.setStatus("current")
_ActiveAlarmIndex_Type = Counter64
_ActiveAlarmIndex_Object = MibTableColumn
activeAlarmIndex = _ActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 3),
    _ActiveAlarmIndex_Type()
)
activeAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    activeAlarmIndex.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 4),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_AffectedObjectType_Type = ComponentType
_AffectedObjectType_Object = MibTableColumn
affectedObjectType = _AffectedObjectType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 5),
    _AffectedObjectType_Type()
)
affectedObjectType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    affectedObjectType.setStatus("current")
_EventType_Type = AlarmEventCategory
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 7),
    _EventType_Type()
)
eventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_EventId_Type = AlarmEventId
_EventId_Object = MibTableColumn
eventId = _EventId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 8),
    _EventId_Type()
)
eventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventId.setStatus("current")


class _DetectorComponent_Type(DisplayString):
    """Custom type detectorComponent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DetectorComponent_Type.__name__ = "DisplayString"
_DetectorComponent_Object = MibTableColumn
detectorComponent = _DetectorComponent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 9),
    _DetectorComponent_Type()
)
detectorComponent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    detectorComponent.setStatus("current")


class _ManagedObjectInstance_Type(DisplayString):
    """Custom type managedObjectInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ManagedObjectInstance_Type.__name__ = "DisplayString"
_ManagedObjectInstance_Object = MibTableColumn
managedObjectInstance = _ManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 10),
    _ManagedObjectInstance_Type()
)
managedObjectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managedObjectInstance.setStatus("current")
_EventDateAndTime_Type = DateAndTime
_EventDateAndTime_Object = MibTableColumn
eventDateAndTime = _EventDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 11),
    _EventDateAndTime_Type()
)
eventDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDateAndTime.setStatus("current")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 12),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_Severity_Type = AlarmSeverity
_Severity_Object = MibTableColumn
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 13),
    _Severity_Type()
)
severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    severity.setStatus("current")


class _AdditionalText_Type(DisplayString):
    """Custom type additionalText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdditionalText_Type.__name__ = "DisplayString"
_AdditionalText_Object = MibTableColumn
additionalText = _AdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 14),
    _AdditionalText_Type()
)
additionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    additionalText.setStatus("current")


class _AlarmEventLogAutoCleared_Type(Integer32):
    """Custom type alarmEventLogAutoCleared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_AlarmEventLogAutoCleared_Type.__name__ = "Integer32"
_AlarmEventLogAutoCleared_Object = MibTableColumn
alarmEventLogAutoCleared = _AlarmEventLogAutoCleared_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 15),
    _AlarmEventLogAutoCleared_Type()
)
alarmEventLogAutoCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventLogAutoCleared.setStatus("current")


class _SiteId_Type(DisplayString):
    """Custom type siteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiteId_Type.__name__ = "DisplayString"
_SiteId_Object = MibTableColumn
siteId = _SiteId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 6, 1, 1, 16),
    _SiteId_Type()
)
siteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    siteId.setStatus("current")
_SdcStatisticsGroup_ObjectIdentity = ObjectIdentity
sdcStatisticsGroup = _SdcStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9)
)
_SdcKpis_ObjectIdentity = ObjectIdentity
sdcKpis = _SdcKpis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10)
)
_SKFamilyReasonTable_Object = MibTable
sKFamilyReasonTable = _SKFamilyReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 1)
)
if mibBuilder.loadTexts:
    sKFamilyReasonTable.setStatus("current")
_SKFamilyReasonEntry_Object = MibTableRow
sKFamilyReasonEntry = _SKFamilyReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 1, 1)
)
sKFamilyReasonEntry.setIndexNames(
    (0, "SDC-MIB", "sKFRFamily"),
    (0, "SDC-MIB", "sKFRReason"),
)
if mibBuilder.loadTexts:
    sKFamilyReasonEntry.setStatus("current")


class _SKFRFamily_Type(DisplayString):
    """Custom type sKFRFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SKFRFamily_Type.__name__ = "DisplayString"
_SKFRFamily_Object = MibTableColumn
sKFRFamily = _SKFRFamily_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 1, 1, 1),
    _SKFRFamily_Type()
)
sKFRFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sKFRFamily.setStatus("current")


class _SKFRReason_Type(DisplayString):
    """Custom type sKFRReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SKFRReason_Type.__name__ = "DisplayString"
_SKFRReason_Object = MibTableColumn
sKFRReason = _SKFRReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 1, 1, 2),
    _SKFRReason_Type()
)
sKFRReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sKFRReason.setStatus("current")
_SKNodeNameTable_Object = MibTable
sKNodeNameTable = _SKNodeNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 2)
)
if mibBuilder.loadTexts:
    sKNodeNameTable.setStatus("current")
_SKNodeNameEntry_Object = MibTableRow
sKNodeNameEntry = _SKNodeNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 2, 1)
)
sKNodeNameEntry.setIndexNames(
    (0, "SDC-MIB", "sKNNodeName"),
)
if mibBuilder.loadTexts:
    sKNodeNameEntry.setStatus("current")


class _SKNNodeName_Type(DisplayString):
    """Custom type sKNNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SKNNodeName_Type.__name__ = "DisplayString"
_SKNNodeName_Object = MibTableColumn
sKNNodeName = _SKNNodeName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 2, 1, 1),
    _SKNNodeName_Type()
)
sKNNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sKNNodeName.setStatus("current")
_SKNNAnswerLatency_Type = Gauge32
_SKNNAnswerLatency_Object = MibTableColumn
sKNNAnswerLatency = _SKNNAnswerLatency_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 2, 1, 4),
    _SKNNAnswerLatency_Type()
)
sKNNAnswerLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKNNAnswerLatency.setStatus("current")
_SKNNRequestLatency_Type = Gauge32
_SKNNRequestLatency_Object = MibTableColumn
sKNNRequestLatency = _SKNNRequestLatency_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 2, 1, 5),
    _SKNNRequestLatency_Type()
)
sKNNRequestLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKNNRequestLatency.setStatus("current")
_SKNNE2ELatency_Type = Gauge32
_SKNNE2ELatency_Object = MibTableColumn
sKNNE2ELatency = _SKNNE2ELatency_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 2, 1, 6),
    _SKNNE2ELatency_Type()
)
sKNNE2ELatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKNNE2ELatency.setStatus("current")
_SKFamilyTable_Object = MibTable
sKFamilyTable = _SKFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 3)
)
if mibBuilder.loadTexts:
    sKFamilyTable.setStatus("current")
_SKFamilyEntry_Object = MibTableRow
sKFamilyEntry = _SKFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 3, 1)
)
sKFamilyEntry.setIndexNames(
    (0, "SDC-MIB", "sdcKpisFamilyEntryFamily"),
)
if mibBuilder.loadTexts:
    sKFamilyEntry.setStatus("current")


class _SdcKpisFamilyEntryFamily_Type(DisplayString):
    """Custom type sdcKpisFamilyEntryFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SdcKpisFamilyEntryFamily_Type.__name__ = "DisplayString"
_SdcKpisFamilyEntryFamily_Object = MibTableColumn
sdcKpisFamilyEntryFamily = _SdcKpisFamilyEntryFamily_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 3, 1, 1),
    _SdcKpisFamilyEntryFamily_Type()
)
sdcKpisFamilyEntryFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdcKpisFamilyEntryFamily.setStatus("current")
_SKFDiscardedMps_Type = Gauge32
_SKFDiscardedMps_Object = MibTableColumn
sKFDiscardedMps = _SKFDiscardedMps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 3, 1, 5),
    _SKFDiscardedMps_Type()
)
sKFDiscardedMps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKFDiscardedMps.setStatus("current")
_SKNewMasterSessions_Type = Gauge32
_SKNewMasterSessions_Object = MibScalar
sKNewMasterSessions = _SKNewMasterSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 51),
    _SKNewMasterSessions_Type()
)
sKNewMasterSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKNewMasterSessions.setStatus("current")
_SKNewSlaveSessions_Type = Gauge32
_SKNewSlaveSessions_Object = MibScalar
sKNewSlaveSessions = _SKNewSlaveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 52),
    _SKNewSlaveSessions_Type()
)
sKNewSlaveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKNewSlaveSessions.setStatus("current")
_SKNumberOfSessionRepositoryEntries_Type = Gauge32
_SKNumberOfSessionRepositoryEntries_Object = MibScalar
sKNumberOfSessionRepositoryEntries = _SKNumberOfSessionRepositoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 54),
    _SKNumberOfSessionRepositoryEntries_Type()
)
sKNumberOfSessionRepositoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKNumberOfSessionRepositoryEntries.setStatus("current")
_SKLicenseMps_Type = Gauge32
_SKLicenseMps_Object = MibScalar
sKLicenseMps = _SKLicenseMps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 55),
    _SKLicenseMps_Type()
)
sKLicenseMps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKLicenseMps.setStatus("current")
_SKSlrfMaxRoundtripTime_Type = Gauge32
_SKSlrfMaxRoundtripTime_Object = MibScalar
sKSlrfMaxRoundtripTime = _SKSlrfMaxRoundtripTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 56),
    _SKSlrfMaxRoundtripTime_Type()
)
sKSlrfMaxRoundtripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKSlrfMaxRoundtripTime.setStatus("current")
_SKSlrfAverageRoundtripTime_Type = Gauge32
_SKSlrfAverageRoundtripTime_Object = MibScalar
sKSlrfAverageRoundtripTime = _SKSlrfAverageRoundtripTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 57),
    _SKSlrfAverageRoundtripTime_Type()
)
sKSlrfAverageRoundtripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKSlrfAverageRoundtripTime.setStatus("current")
_SKSlrfQueries_Type = Gauge32
_SKSlrfQueries_Object = MibScalar
sKSlrfQueries = _SKSlrfQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 10, 58),
    _SKSlrfQueries_Type()
)
sKSlrfQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKSlrfQueries.setStatus("current")
_PeersAndPoolsKpis_ObjectIdentity = ObjectIdentity
peersAndPoolsKpis = _PeersAndPoolsKpis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20)
)
_PAPKMessageTypePeerNameTable_Object = MibTable
pAPKMessageTypePeerNameTable = _PAPKMessageTypePeerNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 1)
)
if mibBuilder.loadTexts:
    pAPKMessageTypePeerNameTable.setStatus("current")
_PAPKMessageTypePeerNameEntry_Object = MibTableRow
pAPKMessageTypePeerNameEntry = _PAPKMessageTypePeerNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 1, 1)
)
pAPKMessageTypePeerNameEntry.setIndexNames(
    (0, "SDC-MIB", "pAPKMTPNMessageType"),
    (0, "SDC-MIB", "pAPKMTPNPeerName"),
)
if mibBuilder.loadTexts:
    pAPKMessageTypePeerNameEntry.setStatus("current")


class _PAPKMTPNMessageType_Type(DisplayString):
    """Custom type pAPKMTPNMessageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PAPKMTPNMessageType_Type.__name__ = "DisplayString"
_PAPKMTPNMessageType_Object = MibTableColumn
pAPKMTPNMessageType = _PAPKMTPNMessageType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 1, 1, 1),
    _PAPKMTPNMessageType_Type()
)
pAPKMTPNMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pAPKMTPNMessageType.setStatus("current")


class _PAPKMTPNPeerName_Type(DisplayString):
    """Custom type pAPKMTPNPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PAPKMTPNPeerName_Type.__name__ = "DisplayString"
_PAPKMTPNPeerName_Object = MibTableColumn
pAPKMTPNPeerName = _PAPKMTPNPeerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 1, 1, 2),
    _PAPKMTPNPeerName_Type()
)
pAPKMTPNPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pAPKMTPNPeerName.setStatus("current")
_PeerMessagesEntrySent_Type = Gauge32
_PeerMessagesEntrySent_Object = MibTableColumn
peerMessagesEntrySent = _PeerMessagesEntrySent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 1, 1, 4),
    _PeerMessagesEntrySent_Type()
)
peerMessagesEntrySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerMessagesEntrySent.setStatus("current")
_PAPKMTPNRequestsReceivedFromPeer_Type = Gauge32
_PAPKMTPNRequestsReceivedFromPeer_Object = MibTableColumn
pAPKMTPNRequestsReceivedFromPeer = _PAPKMTPNRequestsReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 1, 1, 5),
    _PAPKMTPNRequestsReceivedFromPeer_Type()
)
pAPKMTPNRequestsReceivedFromPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKMTPNRequestsReceivedFromPeer.setStatus("current")
_PAPKMTPNDestinationPeerAvgLatency_Type = Gauge32
_PAPKMTPNDestinationPeerAvgLatency_Object = MibTableColumn
pAPKMTPNDestinationPeerAvgLatency = _PAPKMTPNDestinationPeerAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 1, 1, 10),
    _PAPKMTPNDestinationPeerAvgLatency_Type()
)
pAPKMTPNDestinationPeerAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKMTPNDestinationPeerAvgLatency.setStatus("current")
_PAPKPoolNameTable_Object = MibTable
pAPKPoolNameTable = _PAPKPoolNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 2)
)
if mibBuilder.loadTexts:
    pAPKPoolNameTable.setStatus("current")
_PAPKPoolNameEntry_Object = MibTableRow
pAPKPoolNameEntry = _PAPKPoolNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 2, 1)
)
pAPKPoolNameEntry.setIndexNames(
    (0, "SDC-MIB", "pAPKPNPoolName"),
)
if mibBuilder.loadTexts:
    pAPKPoolNameEntry.setStatus("current")


class _PAPKPNPoolName_Type(DisplayString):
    """Custom type pAPKPNPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PAPKPNPoolName_Type.__name__ = "DisplayString"
_PAPKPNPoolName_Object = MibTableColumn
pAPKPNPoolName = _PAPKPNPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 2, 1, 1),
    _PAPKPNPoolName_Type()
)
pAPKPNPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pAPKPNPoolName.setStatus("current")
_PAPKPNRequestsSentToDestinationPool_Type = Gauge32
_PAPKPNRequestsSentToDestinationPool_Object = MibTableColumn
pAPKPNRequestsSentToDestinationPool = _PAPKPNRequestsSentToDestinationPool_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 2, 1, 4),
    _PAPKPNRequestsSentToDestinationPool_Type()
)
pAPKPNRequestsSentToDestinationPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNRequestsSentToDestinationPool.setStatus("current")
_PAPKPNPoolSentMessagesTotal_Type = Gauge32
_PAPKPNPoolSentMessagesTotal_Object = MibTableColumn
pAPKPNPoolSentMessagesTotal = _PAPKPNPoolSentMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 2, 1, 5),
    _PAPKPNPoolSentMessagesTotal_Type()
)
pAPKPNPoolSentMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNPoolSentMessagesTotal.setStatus("current")
_PAPKPNDestinationPool99PercentileLatency_Type = Gauge32
_PAPKPNDestinationPool99PercentileLatency_Object = MibTableColumn
pAPKPNDestinationPool99PercentileLatency = _PAPKPNDestinationPool99PercentileLatency_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 2, 1, 6),
    _PAPKPNDestinationPool99PercentileLatency_Type()
)
pAPKPNDestinationPool99PercentileLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNDestinationPool99PercentileLatency.setStatus("current")
_PAPKPNDestinationPoolAvgLatency_Type = Gauge32
_PAPKPNDestinationPoolAvgLatency_Object = MibTableColumn
pAPKPNDestinationPoolAvgLatency = _PAPKPNDestinationPoolAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 2, 1, 7),
    _PAPKPNDestinationPoolAvgLatency_Type()
)
pAPKPNDestinationPoolAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNDestinationPoolAvgLatency.setStatus("current")
_PAPKPeerNameTable_Object = MibTable
pAPKPeerNameTable = _PAPKPeerNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 3)
)
if mibBuilder.loadTexts:
    pAPKPeerNameTable.setStatus("current")
_PAPKPeerNameEntry_Object = MibTableRow
pAPKPeerNameEntry = _PAPKPeerNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 3, 1)
)
pAPKPeerNameEntry.setIndexNames(
    (0, "SDC-MIB", "pAPKPNPeerName"),
)
if mibBuilder.loadTexts:
    pAPKPeerNameEntry.setStatus("current")


class _PAPKPNPeerName_Type(DisplayString):
    """Custom type pAPKPNPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PAPKPNPeerName_Type.__name__ = "DisplayString"
_PAPKPNPeerName_Object = MibTableColumn
pAPKPNPeerName = _PAPKPNPeerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 3, 1, 1),
    _PAPKPNPeerName_Type()
)
pAPKPNPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pAPKPNPeerName.setStatus("current")
_PAPKPNRequestsBytesReceivedFromPeer_Type = Gauge32
_PAPKPNRequestsBytesReceivedFromPeer_Object = MibTableColumn
pAPKPNRequestsBytesReceivedFromPeer = _PAPKPNRequestsBytesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 3, 1, 4),
    _PAPKPNRequestsBytesReceivedFromPeer_Type()
)
pAPKPNRequestsBytesReceivedFromPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNRequestsBytesReceivedFromPeer.setStatus("current")
_PAPKPNAnswersBytesReceivedFromPeer_Type = Gauge32
_PAPKPNAnswersBytesReceivedFromPeer_Object = MibTableColumn
pAPKPNAnswersBytesReceivedFromPeer = _PAPKPNAnswersBytesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 3, 1, 5),
    _PAPKPNAnswersBytesReceivedFromPeer_Type()
)
pAPKPNAnswersBytesReceivedFromPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNAnswersBytesReceivedFromPeer.setStatus("current")
_PAPKPNDestinationPeer99PercentilLatency_Type = Gauge32
_PAPKPNDestinationPeer99PercentilLatency_Object = MibTableColumn
pAPKPNDestinationPeer99PercentilLatency = _PAPKPNDestinationPeer99PercentilLatency_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 3, 1, 6),
    _PAPKPNDestinationPeer99PercentilLatency_Type()
)
pAPKPNDestinationPeer99PercentilLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNDestinationPeer99PercentilLatency.setStatus("current")
_PAPKPNPeerSentRequestsTotal_Type = Gauge32
_PAPKPNPeerSentRequestsTotal_Object = MibTableColumn
pAPKPNPeerSentRequestsTotal = _PAPKPNPeerSentRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 3, 1, 7),
    _PAPKPNPeerSentRequestsTotal_Type()
)
pAPKPNPeerSentRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNPeerSentRequestsTotal.setStatus("current")
_PAPKPeerNameFamilyReasonTable_Object = MibTable
pAPKPeerNameFamilyReasonTable = _PAPKPeerNameFamilyReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 4)
)
if mibBuilder.loadTexts:
    pAPKPeerNameFamilyReasonTable.setStatus("current")
_PAPKPeerNameFamilyReasonEntry_Object = MibTableRow
pAPKPeerNameFamilyReasonEntry = _PAPKPeerNameFamilyReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 4, 1)
)
pAPKPeerNameFamilyReasonEntry.setIndexNames(
    (0, "SDC-MIB", "peerRneReasonEntryPeerName"),
    (0, "SDC-MIB", "peerRneReasonEntryFamily"),
    (0, "SDC-MIB", "peerRneReasonEntryReason"),
)
if mibBuilder.loadTexts:
    pAPKPeerNameFamilyReasonEntry.setStatus("current")


class _PeerRneReasonEntryPeerName_Type(DisplayString):
    """Custom type peerRneReasonEntryPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PeerRneReasonEntryPeerName_Type.__name__ = "DisplayString"
_PeerRneReasonEntryPeerName_Object = MibTableColumn
peerRneReasonEntryPeerName = _PeerRneReasonEntryPeerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 4, 1, 1),
    _PeerRneReasonEntryPeerName_Type()
)
peerRneReasonEntryPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peerRneReasonEntryPeerName.setStatus("current")


class _PeerRneReasonEntryFamily_Type(DisplayString):
    """Custom type peerRneReasonEntryFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PeerRneReasonEntryFamily_Type.__name__ = "DisplayString"
_PeerRneReasonEntryFamily_Object = MibTableColumn
peerRneReasonEntryFamily = _PeerRneReasonEntryFamily_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 4, 1, 2),
    _PeerRneReasonEntryFamily_Type()
)
peerRneReasonEntryFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peerRneReasonEntryFamily.setStatus("current")


class _PeerRneReasonEntryReason_Type(DisplayString):
    """Custom type peerRneReasonEntryReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PeerRneReasonEntryReason_Type.__name__ = "DisplayString"
_PeerRneReasonEntryReason_Object = MibTableColumn
peerRneReasonEntryReason = _PeerRneReasonEntryReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 4, 1, 3),
    _PeerRneReasonEntryReason_Type()
)
peerRneReasonEntryReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peerRneReasonEntryReason.setStatus("current")
_PAPKPNFRPeerRequestsRejectsByIncomingRateLimit_Type = Gauge32
_PAPKPNFRPeerRequestsRejectsByIncomingRateLimit_Object = MibTableColumn
pAPKPNFRPeerRequestsRejectsByIncomingRateLimit = _PAPKPNFRPeerRequestsRejectsByIncomingRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 20, 4, 1, 5),
    _PAPKPNFRPeerRequestsRejectsByIncomingRateLimit_Type()
)
pAPKPNFRPeerRequestsRejectsByIncomingRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPKPNFRPeerRequestsRejectsByIncomingRateLimit.setStatus("current")
_TransactionsKpis_ObjectIdentity = ObjectIdentity
transactionsKpis = _TransactionsKpis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 30)
)
_TKPeerNameFamilyMessageTypeTable_Object = MibTable
tKPeerNameFamilyMessageTypeTable = _TKPeerNameFamilyMessageTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 30, 1)
)
if mibBuilder.loadTexts:
    tKPeerNameFamilyMessageTypeTable.setStatus("current")
_TKPeerNameFamilyMessageTypeEntry_Object = MibTableRow
tKPeerNameFamilyMessageTypeEntry = _TKPeerNameFamilyMessageTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 30, 1, 1)
)
tKPeerNameFamilyMessageTypeEntry.setIndexNames(
    (0, "SDC-MIB", "tKPNFMTPeerName"),
    (0, "SDC-MIB", "tKPNFMTFamily"),
    (0, "SDC-MIB", "tKPNFMTMessageType"),
)
if mibBuilder.loadTexts:
    tKPeerNameFamilyMessageTypeEntry.setStatus("current")


class _TKPNFMTPeerName_Type(DisplayString):
    """Custom type tKPNFMTPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TKPNFMTPeerName_Type.__name__ = "DisplayString"
_TKPNFMTPeerName_Object = MibTableColumn
tKPNFMTPeerName = _TKPNFMTPeerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 30, 1, 1, 1),
    _TKPNFMTPeerName_Type()
)
tKPNFMTPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tKPNFMTPeerName.setStatus("current")


class _TKPNFMTFamily_Type(DisplayString):
    """Custom type tKPNFMTFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TKPNFMTFamily_Type.__name__ = "DisplayString"
_TKPNFMTFamily_Object = MibTableColumn
tKPNFMTFamily = _TKPNFMTFamily_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 30, 1, 1, 2),
    _TKPNFMTFamily_Type()
)
tKPNFMTFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tKPNFMTFamily.setStatus("current")


class _TKPNFMTMessageType_Type(DisplayString):
    """Custom type tKPNFMTMessageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TKPNFMTMessageType_Type.__name__ = "DisplayString"
_TKPNFMTMessageType_Object = MibTableColumn
tKPNFMTMessageType = _TKPNFMTMessageType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 30, 1, 1, 3),
    _TKPNFMTMessageType_Type()
)
tKPNFMTMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tKPNFMTMessageType.setStatus("current")
_TKPNFMTOriginPeerRemoteNodeEvents_Type = Gauge32
_TKPNFMTOriginPeerRemoteNodeEvents_Object = MibTableColumn
tKPNFMTOriginPeerRemoteNodeEvents = _TKPNFMTOriginPeerRemoteNodeEvents_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 30, 1, 1, 5),
    _TKPNFMTOriginPeerRemoteNodeEvents_Type()
)
tKPNFMTOriginPeerRemoteNodeEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tKPNFMTOriginPeerRemoteNodeEvents.setStatus("current")
_ResourcesKpis_ObjectIdentity = ObjectIdentity
resourcesKpis = _ResourcesKpis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40)
)
_RKNodeNameTable_Object = MibTable
rKNodeNameTable = _RKNodeNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 1)
)
if mibBuilder.loadTexts:
    rKNodeNameTable.setStatus("current")
_RKNodeNameEntry_Object = MibTableRow
rKNodeNameEntry = _RKNodeNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 1, 1)
)
rKNodeNameEntry.setIndexNames(
    (0, "SDC-MIB", "rKNNNodeName"),
)
if mibBuilder.loadTexts:
    rKNodeNameEntry.setStatus("current")


class _RKNNNodeName_Type(DisplayString):
    """Custom type rKNNNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RKNNNodeName_Type.__name__ = "DisplayString"
_RKNNNodeName_Object = MibTableColumn
rKNNNodeName = _RKNNNodeName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 1, 1, 1),
    _RKNNNodeName_Type()
)
rKNNNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rKNNNodeName.setStatus("current")
_RKNNUsedMemory_Type = Gauge32
_RKNNUsedMemory_Object = MibTableColumn
rKNNUsedMemory = _RKNNUsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 1, 1, 5),
    _RKNNUsedMemory_Type()
)
rKNNUsedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKNNUsedMemory.setStatus("current")
_RKNNCpuUsage_Type = Gauge32
_RKNNCpuUsage_Object = MibTableColumn
rKNNCpuUsage = _RKNNCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 1, 1, 6),
    _RKNNCpuUsage_Type()
)
rKNNCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKNNCpuUsage.setStatus("current")
_RKMachineNameTable_Object = MibTable
rKMachineNameTable = _RKMachineNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 2)
)
if mibBuilder.loadTexts:
    rKMachineNameTable.setStatus("current")
_RKMachineNameEntry_Object = MibTableRow
rKMachineNameEntry = _RKMachineNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 2, 1)
)
rKMachineNameEntry.setIndexNames(
    (0, "SDC-MIB", "rKMNMachineName"),
)
if mibBuilder.loadTexts:
    rKMachineNameEntry.setStatus("current")


class _RKMNMachineName_Type(DisplayString):
    """Custom type rKMNMachineName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RKMNMachineName_Type.__name__ = "DisplayString"
_RKMNMachineName_Object = MibTableColumn
rKMNMachineName = _RKMNMachineName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 2, 1, 1),
    _RKMNMachineName_Type()
)
rKMNMachineName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rKMNMachineName.setStatus("current")
_RKMNMachineFreeMemory_Type = Gauge32
_RKMNMachineFreeMemory_Object = MibTableColumn
rKMNMachineFreeMemory = _RKMNMachineFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 2, 1, 5),
    _RKMNMachineFreeMemory_Type()
)
rKMNMachineFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNMachineFreeMemory.setStatus("current")
_RKMNMachineAvailableSwap_Type = Gauge32
_RKMNMachineAvailableSwap_Object = MibTableColumn
rKMNMachineAvailableSwap = _RKMNMachineAvailableSwap_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 2, 1, 6),
    _RKMNMachineAvailableSwap_Type()
)
rKMNMachineAvailableSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNMachineAvailableSwap.setStatus("current")
_RKMNMachineCpuUsage_Type = Gauge32
_RKMNMachineCpuUsage_Object = MibTableColumn
rKMNMachineCpuUsage = _RKMNMachineCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 2, 1, 7),
    _RKMNMachineCpuUsage_Type()
)
rKMNMachineCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNMachineCpuUsage.setStatus("current")
_RKMNMachineLoadAverage_Type = Gauge32
_RKMNMachineLoadAverage_Object = MibTableColumn
rKMNMachineLoadAverage = _RKMNMachineLoadAverage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 2, 1, 8),
    _RKMNMachineLoadAverage_Type()
)
rKMNMachineLoadAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNMachineLoadAverage.setStatus("current")
_RKMachineNamePartitionNameTable_Object = MibTable
rKMachineNamePartitionNameTable = _RKMachineNamePartitionNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 3)
)
if mibBuilder.loadTexts:
    rKMachineNamePartitionNameTable.setStatus("current")
_RKMachineNamePartitionNameEntry_Object = MibTableRow
rKMachineNamePartitionNameEntry = _RKMachineNamePartitionNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 3, 1)
)
rKMachineNamePartitionNameEntry.setIndexNames(
    (0, "SDC-MIB", "rKMNPNMachineName"),
    (0, "SDC-MIB", "rKMNPNPartitionName"),
)
if mibBuilder.loadTexts:
    rKMachineNamePartitionNameEntry.setStatus("current")


class _RKMNPNMachineName_Type(DisplayString):
    """Custom type rKMNPNMachineName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RKMNPNMachineName_Type.__name__ = "DisplayString"
_RKMNPNMachineName_Object = MibTableColumn
rKMNPNMachineName = _RKMNPNMachineName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 3, 1, 1),
    _RKMNPNMachineName_Type()
)
rKMNPNMachineName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rKMNPNMachineName.setStatus("current")


class _RKMNPNPartitionName_Type(DisplayString):
    """Custom type rKMNPNPartitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RKMNPNPartitionName_Type.__name__ = "DisplayString"
_RKMNPNPartitionName_Object = MibTableColumn
rKMNPNPartitionName = _RKMNPNPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 3, 1, 2),
    _RKMNPNPartitionName_Type()
)
rKMNPNPartitionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rKMNPNPartitionName.setStatus("current")
_RKMNPNMachinePartitionUsage_Type = Gauge32
_RKMNPNMachinePartitionUsage_Object = MibTableColumn
rKMNPNMachinePartitionUsage = _RKMNPNMachinePartitionUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 3, 1, 5),
    _RKMNPNMachinePartitionUsage_Type()
)
rKMNPNMachinePartitionUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNPNMachinePartitionUsage.setStatus("current")
_RKMachineNameDiskNameTable_Object = MibTable
rKMachineNameDiskNameTable = _RKMachineNameDiskNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 4)
)
if mibBuilder.loadTexts:
    rKMachineNameDiskNameTable.setStatus("current")
_RKMachineNameDiskNameEntry_Object = MibTableRow
rKMachineNameDiskNameEntry = _RKMachineNameDiskNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 4, 1)
)
rKMachineNameDiskNameEntry.setIndexNames(
    (0, "SDC-MIB", "rKMNDNMachineName"),
    (0, "SDC-MIB", "rKMNDNDiskName"),
)
if mibBuilder.loadTexts:
    rKMachineNameDiskNameEntry.setStatus("current")


class _RKMNDNMachineName_Type(DisplayString):
    """Custom type rKMNDNMachineName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RKMNDNMachineName_Type.__name__ = "DisplayString"
_RKMNDNMachineName_Object = MibTableColumn
rKMNDNMachineName = _RKMNDNMachineName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 4, 1, 1),
    _RKMNDNMachineName_Type()
)
rKMNDNMachineName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rKMNDNMachineName.setStatus("current")


class _RKMNDNDiskName_Type(DisplayString):
    """Custom type rKMNDNDiskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RKMNDNDiskName_Type.__name__ = "DisplayString"
_RKMNDNDiskName_Object = MibTableColumn
rKMNDNDiskName = _RKMNDNDiskName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 4, 1, 2),
    _RKMNDNDiskName_Type()
)
rKMNDNDiskName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rKMNDNDiskName.setStatus("current")
_RKMNDNMachineDiskIoBytesIn_Type = Gauge32
_RKMNDNMachineDiskIoBytesIn_Object = MibTableColumn
rKMNDNMachineDiskIoBytesIn = _RKMNDNMachineDiskIoBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 4, 1, 5),
    _RKMNDNMachineDiskIoBytesIn_Type()
)
rKMNDNMachineDiskIoBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNDNMachineDiskIoBytesIn.setStatus("current")
_RKMNDNMachineDiskIoBytesOut_Type = Gauge32
_RKMNDNMachineDiskIoBytesOut_Object = MibTableColumn
rKMNDNMachineDiskIoBytesOut = _RKMNDNMachineDiskIoBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 4, 1, 6),
    _RKMNDNMachineDiskIoBytesOut_Type()
)
rKMNDNMachineDiskIoBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNDNMachineDiskIoBytesOut.setStatus("current")
_RKMachineNameNetworkNameTable_Object = MibTable
rKMachineNameNetworkNameTable = _RKMachineNameNetworkNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 5)
)
if mibBuilder.loadTexts:
    rKMachineNameNetworkNameTable.setStatus("current")
_RKMachineNameNetworkNameEntry_Object = MibTableRow
rKMachineNameNetworkNameEntry = _RKMachineNameNetworkNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 5, 1)
)
rKMachineNameNetworkNameEntry.setIndexNames(
    (0, "SDC-MIB", "rKMNNNMachineName"),
    (0, "SDC-MIB", "rKMNNNNetworkName"),
)
if mibBuilder.loadTexts:
    rKMachineNameNetworkNameEntry.setStatus("current")


class _RKMNNNMachineName_Type(DisplayString):
    """Custom type rKMNNNMachineName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RKMNNNMachineName_Type.__name__ = "DisplayString"
_RKMNNNMachineName_Object = MibTableColumn
rKMNNNMachineName = _RKMNNNMachineName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 5, 1, 1),
    _RKMNNNMachineName_Type()
)
rKMNNNMachineName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rKMNNNMachineName.setStatus("current")


class _RKMNNNNetworkName_Type(DisplayString):
    """Custom type rKMNNNNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RKMNNNNetworkName_Type.__name__ = "DisplayString"
_RKMNNNNetworkName_Object = MibTableColumn
rKMNNNNetworkName = _RKMNNNNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 5, 1, 2),
    _RKMNNNNetworkName_Type()
)
rKMNNNNetworkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rKMNNNNetworkName.setStatus("current")
_RKMNNNMachineNetworkInterfaceBytesReceived_Type = Gauge32
_RKMNNNMachineNetworkInterfaceBytesReceived_Object = MibTableColumn
rKMNNNMachineNetworkInterfaceBytesReceived = _RKMNNNMachineNetworkInterfaceBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 5, 1, 5),
    _RKMNNNMachineNetworkInterfaceBytesReceived_Type()
)
rKMNNNMachineNetworkInterfaceBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNNNMachineNetworkInterfaceBytesReceived.setStatus("current")
_RKMNNNMachineNetworkInterfaceBytesSent_Type = Gauge32
_RKMNNNMachineNetworkInterfaceBytesSent_Object = MibTableColumn
rKMNNNMachineNetworkInterfaceBytesSent = _RKMNNNMachineNetworkInterfaceBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 5, 1, 6),
    _RKMNNNMachineNetworkInterfaceBytesSent_Type()
)
rKMNNNMachineNetworkInterfaceBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNNNMachineNetworkInterfaceBytesSent.setStatus("current")
_RKMNNNMachineNetworkInterfaceInErrors_Type = Gauge32
_RKMNNNMachineNetworkInterfaceInErrors_Object = MibTableColumn
rKMNNNMachineNetworkInterfaceInErrors = _RKMNNNMachineNetworkInterfaceInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 5, 1, 7),
    _RKMNNNMachineNetworkInterfaceInErrors_Type()
)
rKMNNNMachineNetworkInterfaceInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNNNMachineNetworkInterfaceInErrors.setStatus("current")
_RKMNNNMachineNetworkInterfaceOutErrors_Type = Gauge32
_RKMNNNMachineNetworkInterfaceOutErrors_Object = MibTableColumn
rKMNNNMachineNetworkInterfaceOutErrors = _RKMNNNMachineNetworkInterfaceOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 9, 40, 5, 1, 8),
    _RKMNNNMachineNetworkInterfaceOutErrors_Type()
)
rKMNNNMachineNetworkInterfaceOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rKMNNNMachineNetworkInterfaceOutErrors.setStatus("current")

# Managed Objects groups

sdcObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 8)
)
sdcObjectGroup.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"),
        ("SDC-MIB", "activeAlarmIndex"))
)
if mibBuilder.loadTexts:
    sdcObjectGroup.setStatus("current")

sdcKpiObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 10)
)
sdcKpiObjectGroup.setObjects(
      *(("SDC-MIB", "sKNNE2ELatency"),
        ("SDC-MIB", "rKNNCpuUsage"),
        ("SDC-MIB", "rKMNMachineFreeMemory"),
        ("SDC-MIB", "rKMNMachineAvailableSwap"),
        ("SDC-MIB", "rKMNMachineCpuUsage"),
        ("SDC-MIB", "rKMNMachineLoadAverage"),
        ("SDC-MIB", "rKMNPNMachinePartitionUsage"),
        ("SDC-MIB", "rKMNDNMachineDiskIoBytesIn"),
        ("SDC-MIB", "rKMNDNMachineDiskIoBytesOut"),
        ("SDC-MIB", "rKMNNNMachineNetworkInterfaceBytesReceived"),
        ("SDC-MIB", "rKMNNNMachineNetworkInterfaceBytesSent"),
        ("SDC-MIB", "rKMNNNMachineNetworkInterfaceInErrors"),
        ("SDC-MIB", "rKMNNNMachineNetworkInterfaceOutErrors"),
        ("SDC-MIB", "pAPKPNFRPeerRequestsRejectsByIncomingRateLimit"),
        ("SDC-MIB", "rKNNUsedMemory"),
        ("SDC-MIB", "sKNewMasterSessions"),
        ("SDC-MIB", "sKNewSlaveSessions"),
        ("SDC-MIB", "pAPKPNRequestsBytesReceivedFromPeer"),
        ("SDC-MIB", "pAPKPNAnswersBytesReceivedFromPeer"),
        ("SDC-MIB", "pAPKMTPNRequestsReceivedFromPeer"),
        ("SDC-MIB", "tKPNFMTOriginPeerRemoteNodeEvents"),
        ("SDC-MIB", "pAPKMTPNDestinationPeerAvgLatency"),
        ("SDC-MIB", "pAPKPNDestinationPeer99PercentilLatency"),
        ("SDC-MIB", "pAPKPNDestinationPool99PercentileLatency"),
        ("SDC-MIB", "pAPKPNDestinationPoolAvgLatency"),
        ("SDC-MIB", "pAPKPNRequestsSentToDestinationPool"),
        ("SDC-MIB", "sKNNAnswerLatency"),
        ("SDC-MIB", "sKNNRequestLatency"),
        ("SDC-MIB", "sKNumberOfSessionRepositoryEntries"),
        ("SDC-MIB", "sKLicenseMps"),
        ("SDC-MIB", "sKSlrfMaxRoundtripTime"),
        ("SDC-MIB", "sKSlrfAverageRoundtripTime"),
        ("SDC-MIB", "sKSlrfQueries"),
        ("SDC-MIB", "sKFDiscardedMps"),
        ("SDC-MIB", "peerMessagesEntrySent"),
        ("SDC-MIB", "pAPKPNPeerSentRequestsTotal"),
        ("SDC-MIB", "pAPKPNPoolSentMessagesTotal"))
)
if mibBuilder.loadTexts:
    sdcKpiObjectGroup.setStatus("current")


# Notification objects

sdcLicenseExpirationViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 1, 0, 1)
)
sdcLicenseExpirationViolation.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcLicenseExpirationViolation.setStatus(
        "current"
    )

sdcLicenseMpsViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 1, 0, 2)
)
sdcLicenseMpsViolation.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcLicenseMpsViolation.setStatus(
        "current"
    )

sdcSS7LicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 1, 0, 3)
)
sdcSS7LicenseViolation.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcSS7LicenseViolation.setStatus(
        "current"
    )

sdcProxyConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 2, 0, 1)
)
sdcProxyConnection.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcProxyConnection.setStatus(
        "current"
    )

sdcTripoGeoLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 2, 0, 3)
)
sdcTripoGeoLink.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcTripoGeoLink.setStatus(
        "current"
    )

geoSdcProxyNotMarked = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 2, 0, 4)
)
geoSdcProxyNotMarked.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    geoSdcProxyNotMarked.setStatus(
        "current"
    )

sdcCmEmsConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 3, 0, 3)
)
sdcCmEmsConnection.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCmEmsConnection.setStatus(
        "current"
    )

sdcMachinePhysicalMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4, 0, 1)
)
sdcMachinePhysicalMemory.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMachinePhysicalMemory.setStatus(
        "current"
    )

sdcMachineSwapMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4, 0, 2)
)
sdcMachineSwapMemory.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMachineSwapMemory.setStatus(
        "current"
    )

sdcMachineCpuUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4, 0, 3)
)
sdcMachineCpuUsage.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMachineCpuUsage.setStatus(
        "current"
    )

sdcMachineLoadAverage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4, 0, 4)
)
sdcMachineLoadAverage.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMachineLoadAverage.setStatus(
        "current"
    )

sdcMachineDiskPartitionUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4, 0, 5)
)
sdcMachineDiskPartitionUsage.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMachineDiskPartitionUsage.setStatus(
        "current"
    )

sdcMachineNIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4, 0, 6)
)
sdcMachineNIC.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMachineNIC.setStatus(
        "current"
    )

sdcMachineCpuStealUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 4, 0, 7)
)
sdcMachineCpuStealUsage.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMachineCpuStealUsage.setStatus(
        "current"
    )

sdcTimeoutPoolHealthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 5, 0, 1)
)
sdcTimeoutPoolHealthChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcTimeoutPoolHealthChanged.setStatus(
        "current"
    )

sdcErrorsPoolHealthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 5, 0, 2)
)
sdcErrorsPoolHealthChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcErrorsPoolHealthChanged.setStatus(
        "current"
    )

sdcPoolStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 5, 0, 3)
)
sdcPoolStateChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPoolStateChanged.setStatus(
        "current"
    )

sdcPoolRateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 5, 0, 4)
)
sdcPoolRateChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPoolRateChanged.setStatus(
        "current"
    )

sdcIOQueuePeerHealthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 1)
)
sdcIOQueuePeerHealthChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcIOQueuePeerHealthChanged.setStatus(
        "current"
    )

sdcOOSPeerHealthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 2)
)
sdcOOSPeerHealthChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcOOSPeerHealthChanged.setStatus(
        "current"
    )

sdcRTTPeerHealthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 3)
)
sdcRTTPeerHealthChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcRTTPeerHealthChanged.setStatus(
        "current"
    )

sdcErrorsPeerHealthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 4)
)
sdcErrorsPeerHealthChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcErrorsPeerHealthChanged.setStatus(
        "current"
    )

sdcTimeoutsPeerHealthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 5)
)
sdcTimeoutsPeerHealthChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcTimeoutsPeerHealthChanged.setStatus(
        "current"
    )

sdcPeerOutgoingRateLimitChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 6)
)
sdcPeerOutgoingRateLimitChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPeerOutgoingRateLimitChanged.setStatus(
        "current"
    )

sdcPeerIncomingRateLimitChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 7)
)
sdcPeerIncomingRateLimitChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPeerIncomingRateLimitChanged.setStatus(
        "current"
    )

sdcPendingRequestsPeerHealthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 8)
)
sdcPendingRequestsPeerHealthChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPendingRequestsPeerHealthChanged.setStatus(
        "current"
    )

sdcPeerStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 9)
)
sdcPeerStateChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPeerStateChanged.setStatus(
        "current"
    )

sdcSctpPeerLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 6, 0, 10)
)
sdcSctpPeerLink.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcSctpPeerLink.setStatus(
        "current"
    )

sdcVirtualServerStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 7, 0, 1)
)
sdcVirtualServerStateChanged.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcVirtualServerStateChanged.setStatus(
        "current"
    )

sdcComponentStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 8, 0, 1)
)
sdcComponentStatus.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentStatus.setStatus(
        "current"
    )

sdcCommunicationOfCmFep = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 1)
)
sdcCommunicationOfCmFep.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfCmFep.setStatus(
        "current"
    )

sdcCommunicationOfCmCpf = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 2)
)
sdcCommunicationOfCmCpf.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfCmCpf.setStatus(
        "current"
    )

sdcCommunicationOfCmMateCm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 3)
)
sdcCommunicationOfCmMateCm.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfCmMateCm.setStatus(
        "current"
    )

sdcCommunicationOfCmUi = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 4)
)
sdcCommunicationOfCmUi.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfCmUi.setStatus(
        "current"
    )

sdcCommunicationOfCmNms = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 5)
)
sdcCommunicationOfCmNms.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfCmNms.setStatus(
        "current"
    )

sdcCommunicationOfFepCpf = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 6)
)
sdcCommunicationOfFepCpf.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfFepCpf.setStatus(
        "current"
    )

sdcCommunicationOfCpfTripo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 7)
)
sdcCommunicationOfCpfTripo.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfCpfTripo.setStatus(
        "current"
    )

sdcCommunicationOfNmsFep = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 9)
)
sdcCommunicationOfNmsFep.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfNmsFep.setStatus(
        "current"
    )

sdcCommunicationOfNmsCpf = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 10)
)
sdcCommunicationOfNmsCpf.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfNmsCpf.setStatus(
        "current"
    )

sdcCommunicationOfNmsUi = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 11)
)
sdcCommunicationOfNmsUi.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfNmsUi.setStatus(
        "current"
    )

sdcCommunicationOfNmsTripo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 13)
)
sdcCommunicationOfNmsTripo.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcCommunicationOfNmsTripo.setStatus(
        "current"
    )

sdcComponentHealthRequestQOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 16)
)
sdcComponentHealthRequestQOverload.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentHealthRequestQOverload.setStatus(
        "current"
    )

sdcComponentHealthAnswerQOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 17)
)
sdcComponentHealthAnswerQOverload.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentHealthAnswerQOverload.setStatus(
        "current"
    )

sdcComponentHealthAsynchronousQOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 18)
)
sdcComponentHealthAsynchronousQOverload.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentHealthAsynchronousQOverload.setStatus(
        "current"
    )

sdcComponentHealthRequestQThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 19)
)
sdcComponentHealthRequestQThreshold.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentHealthRequestQThreshold.setStatus(
        "current"
    )

sdcComponentHealthAnswerQThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 20)
)
sdcComponentHealthAnswerQThreshold.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentHealthAnswerQThreshold.setStatus(
        "current"
    )

sdcComponentHealthAsynchronousQThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 21)
)
sdcComponentHealthAsynchronousQThreshold.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentHealthAsynchronousQThreshold.setStatus(
        "current"
    )

sdcComponentTPSOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 22)
)
sdcComponentTPSOverload.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentTPSOverload.setStatus(
        "current"
    )

sdcComponentRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 23)
)
sdcComponentRateLimit.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentRateLimit.setStatus(
        "current"
    )

sdcPendingRequestsOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 24)
)
sdcPendingRequestsOverload.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPendingRequestsOverload.setStatus(
        "current"
    )

sdcPendingRequests = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 25)
)
sdcPendingRequests.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPendingRequests.setStatus(
        "current"
    )

sdcComponentFailureRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 26)
)
sdcComponentFailureRate.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentFailureRate.setStatus(
        "current"
    )

fepCpfCommunicationControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 27)
)
fepCpfCommunicationControl.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    fepCpfCommunicationControl.setStatus(
        "current"
    )

sdcInternalTripoConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 28)
)
sdcInternalTripoConnection.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcInternalTripoConnection.setStatus(
        "current"
    )

sdcTripoHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 29)
)
sdcTripoHealth.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcTripoHealth.setStatus(
        "current"
    )

sdcTripoQueueOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 30)
)
sdcTripoQueueOverflow.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcTripoQueueOverflow.setStatus(
        "current"
    )

geoSdcTripoFullReSyncStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 31)
)
geoSdcTripoFullReSyncStarted.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    geoSdcTripoFullReSyncStarted.setStatus(
        "current"
    )

geoSdcTripoSrrReSyncStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 3, 9, 0, 32)
)
geoSdcTripoSrrReSyncStarted.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    geoSdcTripoSrrReSyncStarted.setStatus(
        "current"
    )

sdcPeerAclRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 1)
)
sdcPeerAclRejected.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPeerAclRejected.setStatus(
        "current"
    )

sdcPeerCapacityRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 2)
)
sdcPeerCapacityRejected.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcPeerCapacityRejected.setStatus(
        "current"
    )

sdcScriptInvocationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 4)
)
sdcScriptInvocationFailed.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcScriptInvocationFailed.setStatus(
        "current"
    )

sdcUserAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 6)
)
sdcUserAuthenticationFailure.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcUserAuthenticationFailure.setStatus(
        "current"
    )

sdcMaxTracePerDayReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 7)
)
sdcMaxTracePerDayReached.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMaxTracePerDayReached.setStatus(
        "current"
    )

sdcMaxTraceTPSReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 8)
)
sdcMaxTraceTPSReached.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcMaxTraceTPSReached.setStatus(
        "current"
    )

sdcDnsResolvingSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 9)
)
sdcDnsResolvingSuccess.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcDnsResolvingSuccess.setStatus(
        "current"
    )

sdcFileServerDirectory = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 15)
)
sdcFileServerDirectory.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcFileServerDirectory.setStatus(
        "current"
    )

sdcFileServerFileCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 16)
)
sdcFileServerFileCreate.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcFileServerFileCreate.setStatus(
        "current"
    )

sdcFileServerCloseFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 17)
)
sdcFileServerCloseFile.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcFileServerCloseFile.setStatus(
        "current"
    )

sdcFileServerRenameFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 18)
)
sdcFileServerRenameFile.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcFileServerRenameFile.setStatus(
        "current"
    )

sdcFileServerSplitFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 19)
)
sdcFileServerSplitFile.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcFileServerSplitFile.setStatus(
        "current"
    )

sdcComponentGcLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 20)
)
sdcComponentGcLoop.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcComponentGcLoop.setStatus(
        "current"
    )

sdcSplunkLicenseUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 22)
)
sdcSplunkLicenseUsage.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcSplunkLicenseUsage.setStatus(
        "current"
    )

sdcSplunkLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 23)
)
sdcSplunkLicenseViolation.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcSplunkLicenseViolation.setStatus(
        "current"
    )

sdcSplunkLicenseLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 24)
)
sdcSplunkLicenseLock.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcSplunkLicenseLock.setStatus(
        "current"
    )

sdcProcessRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 25)
)
sdcProcessRestart.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    sdcProcessRestart.setStatus(
        "current"
    )

vipAppStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 4, 1, 0, 26)
)
vipAppStateChange.setObjects(
      *(("SDC-MIB", "siteId"),
        ("SDC-MIB", "hostName"),
        ("SDC-MIB", "affectedObjectType"),
        ("SDC-MIB", "eventType"),
        ("SDC-MIB", "eventId"),
        ("SDC-MIB", "detectorComponent"),
        ("SDC-MIB", "managedObjectInstance"),
        ("SDC-MIB", "eventDateAndTime"),
        ("SDC-MIB", "eventDescription"),
        ("SDC-MIB", "severity"),
        ("SDC-MIB", "additionalText"),
        ("SDC-MIB", "alarmEventLogAutoCleared"))
)
if mibBuilder.loadTexts:
    vipAppStateChange.setStatus(
        "current"
    )


# Notifications groups

sdcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 7)
)
sdcNotificationGroup.setObjects(
      *(("SDC-MIB", "sdcLicenseExpirationViolation"),
        ("SDC-MIB", "sdcLicenseMpsViolation"),
        ("SDC-MIB", "sdcSS7LicenseViolation"),
        ("SDC-MIB", "sdcProxyConnection"),
        ("SDC-MIB", "sdcTripoGeoLink"),
        ("SDC-MIB", "geoSdcProxyNotMarked"),
        ("SDC-MIB", "sdcCmEmsConnection"),
        ("SDC-MIB", "sdcMachinePhysicalMemory"),
        ("SDC-MIB", "sdcMachineSwapMemory"),
        ("SDC-MIB", "sdcMachineCpuUsage"),
        ("SDC-MIB", "sdcMachineLoadAverage"),
        ("SDC-MIB", "sdcMachineDiskPartitionUsage"),
        ("SDC-MIB", "sdcMachineNIC"),
        ("SDC-MIB", "sdcMachineCpuStealUsage"),
        ("SDC-MIB", "sdcTimeoutPoolHealthChanged"),
        ("SDC-MIB", "sdcErrorsPoolHealthChanged"),
        ("SDC-MIB", "sdcPoolStateChanged"),
        ("SDC-MIB", "sdcPoolRateChanged"),
        ("SDC-MIB", "sdcIOQueuePeerHealthChanged"),
        ("SDC-MIB", "sdcOOSPeerHealthChanged"),
        ("SDC-MIB", "sdcRTTPeerHealthChanged"),
        ("SDC-MIB", "sdcErrorsPeerHealthChanged"),
        ("SDC-MIB", "sdcTimeoutsPeerHealthChanged"),
        ("SDC-MIB", "sdcPeerOutgoingRateLimitChanged"),
        ("SDC-MIB", "sdcPeerIncomingRateLimitChanged"),
        ("SDC-MIB", "sdcPendingRequestsPeerHealthChanged"),
        ("SDC-MIB", "sdcPeerStateChanged"),
        ("SDC-MIB", "sdcSctpPeerLink"),
        ("SDC-MIB", "sdcVirtualServerStateChanged"),
        ("SDC-MIB", "sdcComponentStatus"),
        ("SDC-MIB", "sdcCommunicationOfCmFep"),
        ("SDC-MIB", "sdcCommunicationOfCmCpf"),
        ("SDC-MIB", "sdcCommunicationOfCmMateCm"),
        ("SDC-MIB", "sdcCommunicationOfCmUi"),
        ("SDC-MIB", "sdcCommunicationOfCmNms"),
        ("SDC-MIB", "sdcCommunicationOfFepCpf"),
        ("SDC-MIB", "sdcCommunicationOfCpfTripo"),
        ("SDC-MIB", "sdcCommunicationOfNmsFep"),
        ("SDC-MIB", "sdcCommunicationOfNmsCpf"),
        ("SDC-MIB", "sdcCommunicationOfNmsUi"),
        ("SDC-MIB", "sdcCommunicationOfNmsTripo"),
        ("SDC-MIB", "sdcComponentHealthRequestQOverload"),
        ("SDC-MIB", "sdcComponentHealthAnswerQOverload"),
        ("SDC-MIB", "sdcComponentHealthAsynchronousQOverload"),
        ("SDC-MIB", "sdcComponentHealthRequestQThreshold"),
        ("SDC-MIB", "sdcComponentHealthAnswerQThreshold"),
        ("SDC-MIB", "sdcComponentHealthAsynchronousQThreshold"),
        ("SDC-MIB", "sdcComponentTPSOverload"),
        ("SDC-MIB", "sdcComponentRateLimit"),
        ("SDC-MIB", "sdcPendingRequestsOverload"),
        ("SDC-MIB", "sdcPendingRequests"),
        ("SDC-MIB", "sdcComponentFailureRate"),
        ("SDC-MIB", "fepCpfCommunicationControl"),
        ("SDC-MIB", "sdcInternalTripoConnection"),
        ("SDC-MIB", "sdcTripoHealth"),
        ("SDC-MIB", "sdcTripoQueueOverflow"),
        ("SDC-MIB", "geoSdcTripoFullReSyncStarted"),
        ("SDC-MIB", "geoSdcTripoSrrReSyncStarted"),
        ("SDC-MIB", "sdcPeerAclRejected"),
        ("SDC-MIB", "sdcPeerCapacityRejected"),
        ("SDC-MIB", "sdcScriptInvocationFailed"),
        ("SDC-MIB", "sdcUserAuthenticationFailure"),
        ("SDC-MIB", "sdcMaxTracePerDayReached"),
        ("SDC-MIB", "sdcMaxTraceTPSReached"),
        ("SDC-MIB", "sdcDnsResolvingSuccess"),
        ("SDC-MIB", "sdcFileServerDirectory"),
        ("SDC-MIB", "sdcFileServerFileCreate"),
        ("SDC-MIB", "sdcFileServerCloseFile"),
        ("SDC-MIB", "sdcFileServerRenameFile"),
        ("SDC-MIB", "sdcFileServerSplitFile"),
        ("SDC-MIB", "sdcComponentGcLoop"),
        ("SDC-MIB", "sdcSplunkLicenseUsage"),
        ("SDC-MIB", "sdcSplunkLicenseViolation"),
        ("SDC-MIB", "sdcSplunkLicenseLock"),
        ("SDC-MIB", "sdcProcessRestart"),
        ("SDC-MIB", "vipAppStateChange"))
)
if mibBuilder.loadTexts:
    sdcNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sdcModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 4, 2)
)
sdcModuleCompliance.setObjects(
      *(("SDC-MIB", "sdcObjectGroup"),
        ("SDC-MIB", "sdcNotificationGroup"),
        ("SDC-MIB", "sdcKpiObjectGroup"))
)
if mibBuilder.loadTexts:
    sdcModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SDC-MIB",
    **{"ComponentType": ComponentType,
       "AlarmEventCategory": AlarmEventCategory,
       "AlarmEventId": AlarmEventId,
       "AlarmSeverity": AlarmSeverity,
       "traffix": traffix,
       "sdc": sdc,
       "sdcMgmt": sdcMgmt,
       "sdcNotifObjects": sdcNotifObjects,
       "sdcModuleCompliance": sdcModuleCompliance,
       "sdcAlarms": sdcAlarms,
       "sdcLicenseMppbl": sdcLicenseMppbl,
       "sdcLicenseEvents": sdcLicenseEvents,
       "sdcLicenseExpirationViolation": sdcLicenseExpirationViolation,
       "sdcLicenseMpsViolation": sdcLicenseMpsViolation,
       "sdcSS7LicenseViolation": sdcSS7LicenseViolation,
       "sdcInterSiteMppbl": sdcInterSiteMppbl,
       "sdcInterSiteEvents": sdcInterSiteEvents,
       "sdcProxyConnection": sdcProxyConnection,
       "sdcTripoGeoLink": sdcTripoGeoLink,
       "geoSdcProxyNotMarked": geoSdcProxyNotMarked,
       "sdcEMSAndSDCMppbl": sdcEMSAndSDCMppbl,
       "sdcEMSAndSDCEvents": sdcEMSAndSDCEvents,
       "sdcCmEmsConnection": sdcCmEmsConnection,
       "sdcMachineResourcesMppbl": sdcMachineResourcesMppbl,
       "sdcMachineResourcesEvents": sdcMachineResourcesEvents,
       "sdcMachinePhysicalMemory": sdcMachinePhysicalMemory,
       "sdcMachineSwapMemory": sdcMachineSwapMemory,
       "sdcMachineCpuUsage": sdcMachineCpuUsage,
       "sdcMachineLoadAverage": sdcMachineLoadAverage,
       "sdcMachineDiskPartitionUsage": sdcMachineDiskPartitionUsage,
       "sdcMachineNIC": sdcMachineNIC,
       "sdcMachineCpuStealUsage": sdcMachineCpuStealUsage,
       "sdcPoolStatusMppbl": sdcPoolStatusMppbl,
       "sdcPoolStatusEvents": sdcPoolStatusEvents,
       "sdcTimeoutPoolHealthChanged": sdcTimeoutPoolHealthChanged,
       "sdcErrorsPoolHealthChanged": sdcErrorsPoolHealthChanged,
       "sdcPoolStateChanged": sdcPoolStateChanged,
       "sdcPoolRateChanged": sdcPoolRateChanged,
       "sdcPeerStatusMppbl": sdcPeerStatusMppbl,
       "sdcPeerStatusEvents": sdcPeerStatusEvents,
       "sdcIOQueuePeerHealthChanged": sdcIOQueuePeerHealthChanged,
       "sdcOOSPeerHealthChanged": sdcOOSPeerHealthChanged,
       "sdcRTTPeerHealthChanged": sdcRTTPeerHealthChanged,
       "sdcErrorsPeerHealthChanged": sdcErrorsPeerHealthChanged,
       "sdcTimeoutsPeerHealthChanged": sdcTimeoutsPeerHealthChanged,
       "sdcPeerOutgoingRateLimitChanged": sdcPeerOutgoingRateLimitChanged,
       "sdcPeerIncomingRateLimitChanged": sdcPeerIncomingRateLimitChanged,
       "sdcPendingRequestsPeerHealthChanged": sdcPendingRequestsPeerHealthChanged,
       "sdcPeerStateChanged": sdcPeerStateChanged,
       "sdcSctpPeerLink": sdcSctpPeerLink,
       "sdcVirtualServersMppbl": sdcVirtualServersMppbl,
       "sdcVirtualServersEvents": sdcVirtualServersEvents,
       "sdcVirtualServerStateChanged": sdcVirtualServerStateChanged,
       "sdcProcessesGeneralMppbl": sdcProcessesGeneralMppbl,
       "sdcProcessesGeneralEvents": sdcProcessesGeneralEvents,
       "sdcComponentStatus": sdcComponentStatus,
       "sdcInternalComponentsMppbl": sdcInternalComponentsMppbl,
       "sdcInternalComponentsEvents": sdcInternalComponentsEvents,
       "sdcCommunicationOfCmFep": sdcCommunicationOfCmFep,
       "sdcCommunicationOfCmCpf": sdcCommunicationOfCmCpf,
       "sdcCommunicationOfCmMateCm": sdcCommunicationOfCmMateCm,
       "sdcCommunicationOfCmUi": sdcCommunicationOfCmUi,
       "sdcCommunicationOfCmNms": sdcCommunicationOfCmNms,
       "sdcCommunicationOfFepCpf": sdcCommunicationOfFepCpf,
       "sdcCommunicationOfCpfTripo": sdcCommunicationOfCpfTripo,
       "sdcCommunicationOfNmsFep": sdcCommunicationOfNmsFep,
       "sdcCommunicationOfNmsCpf": sdcCommunicationOfNmsCpf,
       "sdcCommunicationOfNmsUi": sdcCommunicationOfNmsUi,
       "sdcCommunicationOfNmsTripo": sdcCommunicationOfNmsTripo,
       "sdcComponentHealthRequestQOverload": sdcComponentHealthRequestQOverload,
       "sdcComponentHealthAnswerQOverload": sdcComponentHealthAnswerQOverload,
       "sdcComponentHealthAsynchronousQOverload": sdcComponentHealthAsynchronousQOverload,
       "sdcComponentHealthRequestQThreshold": sdcComponentHealthRequestQThreshold,
       "sdcComponentHealthAnswerQThreshold": sdcComponentHealthAnswerQThreshold,
       "sdcComponentHealthAsynchronousQThreshold": sdcComponentHealthAsynchronousQThreshold,
       "sdcComponentTPSOverload": sdcComponentTPSOverload,
       "sdcComponentRateLimit": sdcComponentRateLimit,
       "sdcPendingRequestsOverload": sdcPendingRequestsOverload,
       "sdcPendingRequests": sdcPendingRequests,
       "sdcComponentFailureRate": sdcComponentFailureRate,
       "fepCpfCommunicationControl": fepCpfCommunicationControl,
       "sdcInternalTripoConnection": sdcInternalTripoConnection,
       "sdcTripoHealth": sdcTripoHealth,
       "sdcTripoQueueOverflow": sdcTripoQueueOverflow,
       "geoSdcTripoFullReSyncStarted": geoSdcTripoFullReSyncStarted,
       "geoSdcTripoSrrReSyncStarted": geoSdcTripoSrrReSyncStarted,
       "sdcEvents": sdcEvents,
       "sdcBasicEventsMappable": sdcBasicEventsMappable,
       "sdcNotificationEvents": sdcNotificationEvents,
       "sdcPeerAclRejected": sdcPeerAclRejected,
       "sdcPeerCapacityRejected": sdcPeerCapacityRejected,
       "sdcScriptInvocationFailed": sdcScriptInvocationFailed,
       "sdcUserAuthenticationFailure": sdcUserAuthenticationFailure,
       "sdcMaxTracePerDayReached": sdcMaxTracePerDayReached,
       "sdcMaxTraceTPSReached": sdcMaxTraceTPSReached,
       "sdcDnsResolvingSuccess": sdcDnsResolvingSuccess,
       "sdcFileServerDirectory": sdcFileServerDirectory,
       "sdcFileServerFileCreate": sdcFileServerFileCreate,
       "sdcFileServerCloseFile": sdcFileServerCloseFile,
       "sdcFileServerRenameFile": sdcFileServerRenameFile,
       "sdcFileServerSplitFile": sdcFileServerSplitFile,
       "sdcComponentGcLoop": sdcComponentGcLoop,
       "sdcSplunkLicenseUsage": sdcSplunkLicenseUsage,
       "sdcSplunkLicenseViolation": sdcSplunkLicenseViolation,
       "sdcSplunkLicenseLock": sdcSplunkLicenseLock,
       "sdcProcessRestart": sdcProcessRestart,
       "vipAppStateChange": vipAppStateChange,
       "cpfCustomAlarms": cpfCustomAlarms,
       "trapManagement": trapManagement,
       "activeAlarmTable": activeAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "alarmSourceComponent": alarmSourceComponent,
       "alarmedManagedObject": alarmedManagedObject,
       "activeAlarmIndex": activeAlarmIndex,
       "hostName": hostName,
       "affectedObjectType": affectedObjectType,
       "eventType": eventType,
       "eventId": eventId,
       "detectorComponent": detectorComponent,
       "managedObjectInstance": managedObjectInstance,
       "eventDateAndTime": eventDateAndTime,
       "eventDescription": eventDescription,
       "severity": severity,
       "additionalText": additionalText,
       "alarmEventLogAutoCleared": alarmEventLogAutoCleared,
       "siteId": siteId,
       "sdcNotificationGroup": sdcNotificationGroup,
       "sdcObjectGroup": sdcObjectGroup,
       "sdcStatisticsGroup": sdcStatisticsGroup,
       "sdcKpis": sdcKpis,
       "sKFamilyReasonTable": sKFamilyReasonTable,
       "sKFamilyReasonEntry": sKFamilyReasonEntry,
       "sKFRFamily": sKFRFamily,
       "sKFRReason": sKFRReason,
       "sKNodeNameTable": sKNodeNameTable,
       "sKNodeNameEntry": sKNodeNameEntry,
       "sKNNodeName": sKNNodeName,
       "sKNNAnswerLatency": sKNNAnswerLatency,
       "sKNNRequestLatency": sKNNRequestLatency,
       "sKNNE2ELatency": sKNNE2ELatency,
       "sKFamilyTable": sKFamilyTable,
       "sKFamilyEntry": sKFamilyEntry,
       "sdcKpisFamilyEntryFamily": sdcKpisFamilyEntryFamily,
       "sKFDiscardedMps": sKFDiscardedMps,
       "sKNewMasterSessions": sKNewMasterSessions,
       "sKNewSlaveSessions": sKNewSlaveSessions,
       "sKNumberOfSessionRepositoryEntries": sKNumberOfSessionRepositoryEntries,
       "sKLicenseMps": sKLicenseMps,
       "sKSlrfMaxRoundtripTime": sKSlrfMaxRoundtripTime,
       "sKSlrfAverageRoundtripTime": sKSlrfAverageRoundtripTime,
       "sKSlrfQueries": sKSlrfQueries,
       "peersAndPoolsKpis": peersAndPoolsKpis,
       "pAPKMessageTypePeerNameTable": pAPKMessageTypePeerNameTable,
       "pAPKMessageTypePeerNameEntry": pAPKMessageTypePeerNameEntry,
       "pAPKMTPNMessageType": pAPKMTPNMessageType,
       "pAPKMTPNPeerName": pAPKMTPNPeerName,
       "peerMessagesEntrySent": peerMessagesEntrySent,
       "pAPKMTPNRequestsReceivedFromPeer": pAPKMTPNRequestsReceivedFromPeer,
       "pAPKMTPNDestinationPeerAvgLatency": pAPKMTPNDestinationPeerAvgLatency,
       "pAPKPoolNameTable": pAPKPoolNameTable,
       "pAPKPoolNameEntry": pAPKPoolNameEntry,
       "pAPKPNPoolName": pAPKPNPoolName,
       "pAPKPNRequestsSentToDestinationPool": pAPKPNRequestsSentToDestinationPool,
       "pAPKPNPoolSentMessagesTotal": pAPKPNPoolSentMessagesTotal,
       "pAPKPNDestinationPool99PercentileLatency": pAPKPNDestinationPool99PercentileLatency,
       "pAPKPNDestinationPoolAvgLatency": pAPKPNDestinationPoolAvgLatency,
       "pAPKPeerNameTable": pAPKPeerNameTable,
       "pAPKPeerNameEntry": pAPKPeerNameEntry,
       "pAPKPNPeerName": pAPKPNPeerName,
       "pAPKPNRequestsBytesReceivedFromPeer": pAPKPNRequestsBytesReceivedFromPeer,
       "pAPKPNAnswersBytesReceivedFromPeer": pAPKPNAnswersBytesReceivedFromPeer,
       "pAPKPNDestinationPeer99PercentilLatency": pAPKPNDestinationPeer99PercentilLatency,
       "pAPKPNPeerSentRequestsTotal": pAPKPNPeerSentRequestsTotal,
       "pAPKPeerNameFamilyReasonTable": pAPKPeerNameFamilyReasonTable,
       "pAPKPeerNameFamilyReasonEntry": pAPKPeerNameFamilyReasonEntry,
       "peerRneReasonEntryPeerName": peerRneReasonEntryPeerName,
       "peerRneReasonEntryFamily": peerRneReasonEntryFamily,
       "peerRneReasonEntryReason": peerRneReasonEntryReason,
       "pAPKPNFRPeerRequestsRejectsByIncomingRateLimit": pAPKPNFRPeerRequestsRejectsByIncomingRateLimit,
       "transactionsKpis": transactionsKpis,
       "tKPeerNameFamilyMessageTypeTable": tKPeerNameFamilyMessageTypeTable,
       "tKPeerNameFamilyMessageTypeEntry": tKPeerNameFamilyMessageTypeEntry,
       "tKPNFMTPeerName": tKPNFMTPeerName,
       "tKPNFMTFamily": tKPNFMTFamily,
       "tKPNFMTMessageType": tKPNFMTMessageType,
       "tKPNFMTOriginPeerRemoteNodeEvents": tKPNFMTOriginPeerRemoteNodeEvents,
       "resourcesKpis": resourcesKpis,
       "rKNodeNameTable": rKNodeNameTable,
       "rKNodeNameEntry": rKNodeNameEntry,
       "rKNNNodeName": rKNNNodeName,
       "rKNNUsedMemory": rKNNUsedMemory,
       "rKNNCpuUsage": rKNNCpuUsage,
       "rKMachineNameTable": rKMachineNameTable,
       "rKMachineNameEntry": rKMachineNameEntry,
       "rKMNMachineName": rKMNMachineName,
       "rKMNMachineFreeMemory": rKMNMachineFreeMemory,
       "rKMNMachineAvailableSwap": rKMNMachineAvailableSwap,
       "rKMNMachineCpuUsage": rKMNMachineCpuUsage,
       "rKMNMachineLoadAverage": rKMNMachineLoadAverage,
       "rKMachineNamePartitionNameTable": rKMachineNamePartitionNameTable,
       "rKMachineNamePartitionNameEntry": rKMachineNamePartitionNameEntry,
       "rKMNPNMachineName": rKMNPNMachineName,
       "rKMNPNPartitionName": rKMNPNPartitionName,
       "rKMNPNMachinePartitionUsage": rKMNPNMachinePartitionUsage,
       "rKMachineNameDiskNameTable": rKMachineNameDiskNameTable,
       "rKMachineNameDiskNameEntry": rKMachineNameDiskNameEntry,
       "rKMNDNMachineName": rKMNDNMachineName,
       "rKMNDNDiskName": rKMNDNDiskName,
       "rKMNDNMachineDiskIoBytesIn": rKMNDNMachineDiskIoBytesIn,
       "rKMNDNMachineDiskIoBytesOut": rKMNDNMachineDiskIoBytesOut,
       "rKMachineNameNetworkNameTable": rKMachineNameNetworkNameTable,
       "rKMachineNameNetworkNameEntry": rKMachineNameNetworkNameEntry,
       "rKMNNNMachineName": rKMNNNMachineName,
       "rKMNNNNetworkName": rKMNNNNetworkName,
       "rKMNNNMachineNetworkInterfaceBytesReceived": rKMNNNMachineNetworkInterfaceBytesReceived,
       "rKMNNNMachineNetworkInterfaceBytesSent": rKMNNNMachineNetworkInterfaceBytesSent,
       "rKMNNNMachineNetworkInterfaceInErrors": rKMNNNMachineNetworkInterfaceInErrors,
       "rKMNNNMachineNetworkInterfaceOutErrors": rKMNNNMachineNetworkInterfaceOutErrors,
       "sdcKpiObjectGroup": sdcKpiObjectGroup}
)
