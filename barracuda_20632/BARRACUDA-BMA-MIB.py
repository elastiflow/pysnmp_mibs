# SNMP MIB module (BARRACUDA-BMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/barracuda_20632/BARRACUDA-BMA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:37:18 2025
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

(barracuda,) = mibBuilder.importSymbols(
    "BARRACUDA-SMI",
    "barracuda")

(Float,) = mibBuilder.importSymbols(
    "NET-SNMP-TC",
    "Float")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bma = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QueueFiles_Type = Gauge32
_QueueFiles_Object = MibScalar
queueFiles = _QueueFiles_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 2),
    _QueueFiles_Type()
)
queueFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueFiles.setStatus("deprecated")
_UnfinishedFiles_Type = Gauge32
_UnfinishedFiles_Object = MibScalar
unfinishedFiles = _UnfinishedFiles_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 3),
    _UnfinishedFiles_Type()
)
unfinishedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unfinishedFiles.setStatus("deprecated")
_IndexCount_Type = Gauge32
_IndexCount_Object = MibScalar
indexCount = _IndexCount_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 4),
    _IndexCount_Type()
)
indexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indexCount.setStatus("deprecated")
_BmaMsgStats_ObjectIdentity = ObjectIdentity
bmaMsgStats = _BmaMsgStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5)
)
_InboundEmailsHour_Type = Gauge32
_InboundEmailsHour_Object = MibScalar
inboundEmailsHour = _InboundEmailsHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 1),
    _InboundEmailsHour_Type()
)
inboundEmailsHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundEmailsHour.setStatus("current")
_InboundEmailsDay_Type = Gauge32
_InboundEmailsDay_Object = MibScalar
inboundEmailsDay = _InboundEmailsDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 2),
    _InboundEmailsDay_Type()
)
inboundEmailsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundEmailsDay.setStatus("current")
_InboundEmailsTotal_Type = Gauge32
_InboundEmailsTotal_Object = MibScalar
inboundEmailsTotal = _InboundEmailsTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 3),
    _InboundEmailsTotal_Type()
)
inboundEmailsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundEmailsTotal.setStatus("current")
_InternalEmailsHour_Type = Gauge32
_InternalEmailsHour_Object = MibScalar
internalEmailsHour = _InternalEmailsHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 4),
    _InternalEmailsHour_Type()
)
internalEmailsHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalEmailsHour.setStatus("current")
_InternalEmailsDay_Type = Gauge32
_InternalEmailsDay_Object = MibScalar
internalEmailsDay = _InternalEmailsDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 5),
    _InternalEmailsDay_Type()
)
internalEmailsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalEmailsDay.setStatus("current")
_InternalEmailsTotal_Type = Gauge32
_InternalEmailsTotal_Object = MibScalar
internalEmailsTotal = _InternalEmailsTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 6),
    _InternalEmailsTotal_Type()
)
internalEmailsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalEmailsTotal.setStatus("current")
_OutboundEmailsHour_Type = Gauge32
_OutboundEmailsHour_Object = MibScalar
outboundEmailsHour = _OutboundEmailsHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 7),
    _OutboundEmailsHour_Type()
)
outboundEmailsHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundEmailsHour.setStatus("current")
_OutboundEmailsDay_Type = Gauge32
_OutboundEmailsDay_Object = MibScalar
outboundEmailsDay = _OutboundEmailsDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 8),
    _OutboundEmailsDay_Type()
)
outboundEmailsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundEmailsDay.setStatus("current")
_OutboundEmailsTotal_Type = Gauge32
_OutboundEmailsTotal_Object = MibScalar
outboundEmailsTotal = _OutboundEmailsTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 9),
    _OutboundEmailsTotal_Type()
)
outboundEmailsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundEmailsTotal.setStatus("current")
_AppointmentsHour_Type = Gauge32
_AppointmentsHour_Object = MibScalar
appointmentsHour = _AppointmentsHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 10),
    _AppointmentsHour_Type()
)
appointmentsHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appointmentsHour.setStatus("current")
_AppointmentsDay_Type = Gauge32
_AppointmentsDay_Object = MibScalar
appointmentsDay = _AppointmentsDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 11),
    _AppointmentsDay_Type()
)
appointmentsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appointmentsDay.setStatus("current")
_AppointmentsTotal_Type = Gauge32
_AppointmentsTotal_Object = MibScalar
appointmentsTotal = _AppointmentsTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 12),
    _AppointmentsTotal_Type()
)
appointmentsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appointmentsTotal.setStatus("current")
_ContactsHour_Type = Gauge32
_ContactsHour_Object = MibScalar
contactsHour = _ContactsHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 13),
    _ContactsHour_Type()
)
contactsHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactsHour.setStatus("current")
_ContactsDay_Type = Gauge32
_ContactsDay_Object = MibScalar
contactsDay = _ContactsDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 14),
    _ContactsDay_Type()
)
contactsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactsDay.setStatus("current")
_ContactsTotal_Type = Gauge32
_ContactsTotal_Object = MibScalar
contactsTotal = _ContactsTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 15),
    _ContactsTotal_Type()
)
contactsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactsTotal.setStatus("current")
_DistributionListHour_Type = Gauge32
_DistributionListHour_Object = MibScalar
distributionListHour = _DistributionListHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 16),
    _DistributionListHour_Type()
)
distributionListHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distributionListHour.setStatus("current")
_DistributionListDay_Type = Gauge32
_DistributionListDay_Object = MibScalar
distributionListDay = _DistributionListDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 17),
    _DistributionListDay_Type()
)
distributionListDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distributionListDay.setStatus("current")
_DistributionListTotal_Type = Gauge32
_DistributionListTotal_Object = MibScalar
distributionListTotal = _DistributionListTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 18),
    _DistributionListTotal_Type()
)
distributionListTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distributionListTotal.setStatus("current")
_NotesHour_Type = Gauge32
_NotesHour_Object = MibScalar
notesHour = _NotesHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 19),
    _NotesHour_Type()
)
notesHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notesHour.setStatus("current")
_NotesDay_Type = Gauge32
_NotesDay_Object = MibScalar
notesDay = _NotesDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 20),
    _NotesDay_Type()
)
notesDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notesDay.setStatus("current")
_NotesTotal_Type = Gauge32
_NotesTotal_Object = MibScalar
notesTotal = _NotesTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 21),
    _NotesTotal_Type()
)
notesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notesTotal.setStatus("current")
_TasksHour_Type = Gauge32
_TasksHour_Object = MibScalar
tasksHour = _TasksHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 22),
    _TasksHour_Type()
)
tasksHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tasksHour.setStatus("current")
_TasksDay_Type = Gauge32
_TasksDay_Object = MibScalar
tasksDay = _TasksDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 23),
    _TasksDay_Type()
)
tasksDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tasksDay.setStatus("current")
_TasksTotal_Type = Gauge32
_TasksTotal_Object = MibScalar
tasksTotal = _TasksTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 24),
    _TasksTotal_Type()
)
tasksTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tasksTotal.setStatus("current")
_MessagesHour_Type = Gauge32
_MessagesHour_Object = MibScalar
messagesHour = _MessagesHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 25),
    _MessagesHour_Type()
)
messagesHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesHour.setStatus("current")
_MessagesDay_Type = Gauge32
_MessagesDay_Object = MibScalar
messagesDay = _MessagesDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 26),
    _MessagesDay_Type()
)
messagesDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesDay.setStatus("current")
_MessagesTotal_Type = Gauge32
_MessagesTotal_Object = MibScalar
messagesTotal = _MessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 27),
    _MessagesTotal_Type()
)
messagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesTotal.setStatus("current")
_OtherHour_Type = Gauge32
_OtherHour_Object = MibScalar
otherHour = _OtherHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 28),
    _OtherHour_Type()
)
otherHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherHour.setStatus("current")
_OtherDay_Type = Gauge32
_OtherDay_Object = MibScalar
otherDay = _OtherDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 29),
    _OtherDay_Type()
)
otherDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDay.setStatus("current")
_OtherTotal_Type = Gauge32
_OtherTotal_Object = MibScalar
otherTotal = _OtherTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 5, 30),
    _OtherTotal_Type()
)
otherTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherTotal.setStatus("current")
_BmaPerformanceStats_ObjectIdentity = ObjectIdentity
bmaPerformanceStats = _BmaPerformanceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6)
)


class _SystemLoad_Type(Gauge32):
    """Custom type systemLoad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SystemLoad_Type.__name__ = "Gauge32"
_SystemLoad_Object = MibScalar
systemLoad = _SystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 1),
    _SystemLoad_Type()
)
systemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLoad.setStatus("current")
if mibBuilder.loadTexts:
    systemLoad.setUnits("%")
_BmaCPUFanStats_ObjectIdentity = ObjectIdentity
bmaCPUFanStats = _BmaCPUFanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 2)
)
_Cpu1FanSpeed_Type = Gauge32
_Cpu1FanSpeed_Object = MibScalar
cpu1FanSpeed = _Cpu1FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 2, 1),
    _Cpu1FanSpeed_Type()
)
cpu1FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu1FanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cpu1FanSpeed.setUnits("RPM")
_Cpu2FanSpeed_Type = Gauge32
_Cpu2FanSpeed_Object = MibScalar
cpu2FanSpeed = _Cpu2FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 2, 2),
    _Cpu2FanSpeed_Type()
)
cpu2FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu2FanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cpu2FanSpeed.setUnits("RPM")
_BmaSystemTempStats_ObjectIdentity = ObjectIdentity
bmaSystemTempStats = _BmaSystemTempStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 3)
)
_SystemTemperature1_Type = Gauge32
_SystemTemperature1_Object = MibScalar
systemTemperature1 = _SystemTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 3, 1),
    _SystemTemperature1_Type()
)
systemTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature1.setStatus("current")
if mibBuilder.loadTexts:
    systemTemperature1.setUnits("C")
_BmaCPUTempStats_ObjectIdentity = ObjectIdentity
bmaCPUTempStats = _BmaCPUTempStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 4)
)
_Cpu1Temperature_Type = Gauge32
_Cpu1Temperature_Object = MibScalar
cpu1Temperature = _Cpu1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 4, 1),
    _Cpu1Temperature_Type()
)
cpu1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    cpu1Temperature.setUnits("C")
_Cpu2Temperature_Type = Gauge32
_Cpu2Temperature_Object = MibScalar
cpu2Temperature = _Cpu2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 4, 2),
    _Cpu2Temperature_Type()
)
cpu2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    cpu2Temperature.setUnits("C")


class _FirmwareStorage_Type(Gauge32):
    """Custom type firmwareStorage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FirmwareStorage_Type.__name__ = "Gauge32"
_FirmwareStorage_Object = MibScalar
firmwareStorage = _FirmwareStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 5),
    _FirmwareStorage_Type()
)
firmwareStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStorage.setStatus("current")
if mibBuilder.loadTexts:
    firmwareStorage.setUnits("%")


class _MailLogStorage_Type(Gauge32):
    """Custom type mailLogStorage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MailLogStorage_Type.__name__ = "Gauge32"
_MailLogStorage_Object = MibScalar
mailLogStorage = _MailLogStorage_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 6),
    _MailLogStorage_Type()
)
mailLogStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailLogStorage.setStatus("current")
if mibBuilder.loadTexts:
    mailLogStorage.setUnits("%")
_IndexQueueLength_Type = Gauge32
_IndexQueueLength_Object = MibScalar
indexQueueLength = _IndexQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 8),
    _IndexQueueLength_Type()
)
indexQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indexQueueLength.setStatus("current")
_LastMessageArchived_Type = DisplayString
_LastMessageArchived_Object = MibScalar
lastMessageArchived = _LastMessageArchived_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 9),
    _LastMessageArchived_Type()
)
lastMessageArchived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastMessageArchived.setStatus("current")
_MessagesDeduplicated_Type = Gauge32
_MessagesDeduplicated_Object = MibScalar
messagesDeduplicated = _MessagesDeduplicated_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 10),
    _MessagesDeduplicated_Type()
)
messagesDeduplicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesDeduplicated.setStatus("current")
_StorageSaved_Type = Gauge32
_StorageSaved_Object = MibScalar
storageSaved = _StorageSaved_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 11),
    _StorageSaved_Type()
)
storageSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageSaved.setStatus("current")
if mibBuilder.loadTexts:
    storageSaved.setUnits("bytes")


class _CloudControlStatus_Type(Integer32):
    """Custom type cloudControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2),
          ("notConfigured", 3))
    )


_CloudControlStatus_Type.__name__ = "Integer32"
_CloudControlStatus_Object = MibScalar
cloudControlStatus = _CloudControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 6, 12),
    _CloudControlStatus_Type()
)
cloudControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudControlStatus.setStatus("current")
_BmaPolicyStats_ObjectIdentity = ObjectIdentity
bmaPolicyStats = _BmaPolicyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7)
)
_PersonalInfoHour_Type = Gauge32
_PersonalInfoHour_Object = MibScalar
personalInfoHour = _PersonalInfoHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 1),
    _PersonalInfoHour_Type()
)
personalInfoHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    personalInfoHour.setStatus("current")
_PersonalInfoDay_Type = Gauge32
_PersonalInfoDay_Object = MibScalar
personalInfoDay = _PersonalInfoDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 2),
    _PersonalInfoDay_Type()
)
personalInfoDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    personalInfoDay.setStatus("current")
_PersonalInfoTotal_Type = Gauge32
_PersonalInfoTotal_Object = MibScalar
personalInfoTotal = _PersonalInfoTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 3),
    _PersonalInfoTotal_Type()
)
personalInfoTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    personalInfoTotal.setStatus("current")
_FoulLanguageHour_Type = Gauge32
_FoulLanguageHour_Object = MibScalar
foulLanguageHour = _FoulLanguageHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 4),
    _FoulLanguageHour_Type()
)
foulLanguageHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foulLanguageHour.setStatus("current")
_FoulLanguageDay_Type = Gauge32
_FoulLanguageDay_Object = MibScalar
foulLanguageDay = _FoulLanguageDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 5),
    _FoulLanguageDay_Type()
)
foulLanguageDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foulLanguageDay.setStatus("current")
_FoulLanguageTotal_Type = Gauge32
_FoulLanguageTotal_Object = MibScalar
foulLanguageTotal = _FoulLanguageTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 6),
    _FoulLanguageTotal_Type()
)
foulLanguageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foulLanguageTotal.setStatus("current")
_PersonalEmailHour_Type = Gauge32
_PersonalEmailHour_Object = MibScalar
personalEmailHour = _PersonalEmailHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 7),
    _PersonalEmailHour_Type()
)
personalEmailHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    personalEmailHour.setStatus("current")
_PersonalEmailDay_Type = Gauge32
_PersonalEmailDay_Object = MibScalar
personalEmailDay = _PersonalEmailDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 8),
    _PersonalEmailDay_Type()
)
personalEmailDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    personalEmailDay.setStatus("current")
_PersonalEmailTotal_Type = Gauge32
_PersonalEmailTotal_Object = MibScalar
personalEmailTotal = _PersonalEmailTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 9),
    _PersonalEmailTotal_Type()
)
personalEmailTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    personalEmailTotal.setStatus("current")
_PolicyHour_Type = Gauge32
_PolicyHour_Object = MibScalar
policyHour = _PolicyHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 10),
    _PolicyHour_Type()
)
policyHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyHour.setStatus("current")
_PolicyDay_Type = Gauge32
_PolicyDay_Object = MibScalar
policyDay = _PolicyDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 11),
    _PolicyDay_Type()
)
policyDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDay.setStatus("current")
_PolicyTotal_Type = Gauge32
_PolicyTotal_Object = MibScalar
policyTotal = _PolicyTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 12),
    _PolicyTotal_Type()
)
policyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyTotal.setStatus("current")
_CustomPolicyTable_Object = MibTable
customPolicyTable = _CustomPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 13)
)
if mibBuilder.loadTexts:
    customPolicyTable.setStatus("current")
_CustomPolicyEntry_Object = MibTableRow
customPolicyEntry = _CustomPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 13, 1)
)
customPolicyEntry.setIndexNames(
    (0, "BARRACUDA-BMA-MIB", "customPolicyIndex"),
)
if mibBuilder.loadTexts:
    customPolicyEntry.setStatus("current")
_CustomPolicyIndex_Type = Integer32
_CustomPolicyIndex_Object = MibTableColumn
customPolicyIndex = _CustomPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 13, 1, 1),
    _CustomPolicyIndex_Type()
)
customPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    customPolicyIndex.setStatus("current")
_CustomPolicyName_Type = DisplayString
_CustomPolicyName_Object = MibTableColumn
customPolicyName = _CustomPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 13, 1, 2),
    _CustomPolicyName_Type()
)
customPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customPolicyName.setStatus("current")
_CustomPolicyStatsHour_Type = Gauge32
_CustomPolicyStatsHour_Object = MibTableColumn
customPolicyStatsHour = _CustomPolicyStatsHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 13, 1, 3),
    _CustomPolicyStatsHour_Type()
)
customPolicyStatsHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customPolicyStatsHour.setStatus("current")
_CustomPolicyStatsDay_Type = Gauge32
_CustomPolicyStatsDay_Object = MibTableColumn
customPolicyStatsDay = _CustomPolicyStatsDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 13, 1, 4),
    _CustomPolicyStatsDay_Type()
)
customPolicyStatsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customPolicyStatsDay.setStatus("current")
_CustomPolicyStatsTotal_Type = Gauge32
_CustomPolicyStatsTotal_Object = MibTableColumn
customPolicyStatsTotal = _CustomPolicyStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 7, 13, 1, 5),
    _CustomPolicyStatsTotal_Type()
)
customPolicyStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customPolicyStatsTotal.setStatus("current")
_BmaStorageStats_ObjectIdentity = ObjectIdentity
bmaStorageStats = _BmaStorageStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8)
)
_EffectiveHour_Type = Gauge32
_EffectiveHour_Object = MibScalar
effectiveHour = _EffectiveHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 1),
    _EffectiveHour_Type()
)
effectiveHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    effectiveHour.setStatus("current")
if mibBuilder.loadTexts:
    effectiveHour.setUnits("MB")
_EffectiveDay_Type = Gauge32
_EffectiveDay_Object = MibScalar
effectiveDay = _EffectiveDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 2),
    _EffectiveDay_Type()
)
effectiveDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    effectiveDay.setStatus("current")
if mibBuilder.loadTexts:
    effectiveDay.setUnits("MB")
_EffectiveTotal_Type = Gauge32
_EffectiveTotal_Object = MibScalar
effectiveTotal = _EffectiveTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 3),
    _EffectiveTotal_Type()
)
effectiveTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    effectiveTotal.setStatus("current")
if mibBuilder.loadTexts:
    effectiveTotal.setUnits("MB")
_OnDiskSizeHour_Type = Gauge32
_OnDiskSizeHour_Object = MibScalar
onDiskSizeHour = _OnDiskSizeHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 4),
    _OnDiskSizeHour_Type()
)
onDiskSizeHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onDiskSizeHour.setStatus("current")
if mibBuilder.loadTexts:
    onDiskSizeHour.setUnits("MB")
_OnDiskSizeDay_Type = Gauge32
_OnDiskSizeDay_Object = MibScalar
onDiskSizeDay = _OnDiskSizeDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 5),
    _OnDiskSizeDay_Type()
)
onDiskSizeDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onDiskSizeDay.setStatus("current")
if mibBuilder.loadTexts:
    onDiskSizeDay.setUnits("MB")
_OnDiskSizeTotal_Type = Gauge32
_OnDiskSizeTotal_Object = MibScalar
onDiskSizeTotal = _OnDiskSizeTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 6),
    _OnDiskSizeTotal_Type()
)
onDiskSizeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onDiskSizeTotal.setStatus("current")
if mibBuilder.loadTexts:
    onDiskSizeTotal.setUnits("MB")


class _ReductionHour_Type(Integer32):
    """Custom type reductionHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_ReductionHour_Type.__name__ = "Integer32"
_ReductionHour_Object = MibScalar
reductionHour = _ReductionHour_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 7),
    _ReductionHour_Type()
)
reductionHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reductionHour.setStatus("current")
if mibBuilder.loadTexts:
    reductionHour.setUnits("%")


class _ReductionDay_Type(Integer32):
    """Custom type reductionDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_ReductionDay_Type.__name__ = "Integer32"
_ReductionDay_Object = MibScalar
reductionDay = _ReductionDay_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 8),
    _ReductionDay_Type()
)
reductionDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reductionDay.setStatus("current")
if mibBuilder.loadTexts:
    reductionDay.setUnits("%")


class _ReductionTotal_Type(Integer32):
    """Custom type reductionTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_ReductionTotal_Type.__name__ = "Integer32"
_ReductionTotal_Object = MibScalar
reductionTotal = _ReductionTotal_Object(
    (1, 3, 6, 1, 4, 1, 20632, 6, 8, 9),
    _ReductionTotal_Type()
)
reductionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reductionTotal.setStatus("current")
if mibBuilder.loadTexts:
    reductionTotal.setUnits("%")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BARRACUDA-BMA-MIB",
    **{"bma": bma,
       "queueFiles": queueFiles,
       "unfinishedFiles": unfinishedFiles,
       "indexCount": indexCount,
       "bmaMsgStats": bmaMsgStats,
       "inboundEmailsHour": inboundEmailsHour,
       "inboundEmailsDay": inboundEmailsDay,
       "inboundEmailsTotal": inboundEmailsTotal,
       "internalEmailsHour": internalEmailsHour,
       "internalEmailsDay": internalEmailsDay,
       "internalEmailsTotal": internalEmailsTotal,
       "outboundEmailsHour": outboundEmailsHour,
       "outboundEmailsDay": outboundEmailsDay,
       "outboundEmailsTotal": outboundEmailsTotal,
       "appointmentsHour": appointmentsHour,
       "appointmentsDay": appointmentsDay,
       "appointmentsTotal": appointmentsTotal,
       "contactsHour": contactsHour,
       "contactsDay": contactsDay,
       "contactsTotal": contactsTotal,
       "distributionListHour": distributionListHour,
       "distributionListDay": distributionListDay,
       "distributionListTotal": distributionListTotal,
       "notesHour": notesHour,
       "notesDay": notesDay,
       "notesTotal": notesTotal,
       "tasksHour": tasksHour,
       "tasksDay": tasksDay,
       "tasksTotal": tasksTotal,
       "messagesHour": messagesHour,
       "messagesDay": messagesDay,
       "messagesTotal": messagesTotal,
       "otherHour": otherHour,
       "otherDay": otherDay,
       "otherTotal": otherTotal,
       "bmaPerformanceStats": bmaPerformanceStats,
       "systemLoad": systemLoad,
       "bmaCPUFanStats": bmaCPUFanStats,
       "cpu1FanSpeed": cpu1FanSpeed,
       "cpu2FanSpeed": cpu2FanSpeed,
       "bmaSystemTempStats": bmaSystemTempStats,
       "systemTemperature1": systemTemperature1,
       "bmaCPUTempStats": bmaCPUTempStats,
       "cpu1Temperature": cpu1Temperature,
       "cpu2Temperature": cpu2Temperature,
       "firmwareStorage": firmwareStorage,
       "mailLogStorage": mailLogStorage,
       "indexQueueLength": indexQueueLength,
       "lastMessageArchived": lastMessageArchived,
       "messagesDeduplicated": messagesDeduplicated,
       "storageSaved": storageSaved,
       "cloudControlStatus": cloudControlStatus,
       "bmaPolicyStats": bmaPolicyStats,
       "personalInfoHour": personalInfoHour,
       "personalInfoDay": personalInfoDay,
       "personalInfoTotal": personalInfoTotal,
       "foulLanguageHour": foulLanguageHour,
       "foulLanguageDay": foulLanguageDay,
       "foulLanguageTotal": foulLanguageTotal,
       "personalEmailHour": personalEmailHour,
       "personalEmailDay": personalEmailDay,
       "personalEmailTotal": personalEmailTotal,
       "policyHour": policyHour,
       "policyDay": policyDay,
       "policyTotal": policyTotal,
       "customPolicyTable": customPolicyTable,
       "customPolicyEntry": customPolicyEntry,
       "customPolicyIndex": customPolicyIndex,
       "customPolicyName": customPolicyName,
       "customPolicyStatsHour": customPolicyStatsHour,
       "customPolicyStatsDay": customPolicyStatsDay,
       "customPolicyStatsTotal": customPolicyStatsTotal,
       "bmaStorageStats": bmaStorageStats,
       "effectiveHour": effectiveHour,
       "effectiveDay": effectiveDay,
       "effectiveTotal": effectiveTotal,
       "onDiskSizeHour": onDiskSizeHour,
       "onDiskSizeDay": onDiskSizeDay,
       "onDiskSizeTotal": onDiskSizeTotal,
       "reductionHour": reductionHour,
       "reductionDay": reductionDay,
       "reductionTotal": reductionTotal}
)
