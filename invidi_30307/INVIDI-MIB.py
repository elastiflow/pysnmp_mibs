# SNMP MIB module (INVIDI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/invidi_30307/INVIDI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:37 2025
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

invidiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30307)
)
if mibBuilder.loadTexts:
    invidiMIB.setRevisions(
        ("2017-03-10 00:00",
         "2008-01-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class StatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("notApplicablei", 4))
    )



class InterfaceType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("breakWindows", 1),
          ("adrs", 2),
          ("adoAloCreationAdrs", 3),
          ("prioritizerAdrs", 4),
          ("assets", 5),
          ("guideData", 6),
          ("stbData", 7),
          ("avProfileCategoryData", 8),
          ("breakStatus", 9),
          ("verificationLogs", 10),
          ("viewlistReportLogs", 11),
          ("impressions", 12),
          ("stbResponderList", 13),
          ("unknownSTBList", 14),
          ("requiredAssets", 15),
          ("assetStates", 16),
          ("airedBreaks", 17))
    )



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1)
)
_Advatar_ObjectIdentity = ObjectIdentity
advatar = _Advatar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1)
)
if mibBuilder.loadTexts:
    advatar.setStatus("current")
_NotificationPrefix_ObjectIdentity = ObjectIdentity
notificationPrefix = _NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0)
)
if mibBuilder.loadTexts:
    notificationPrefix.setStatus("current")
_MibNotifications_ObjectIdentity = ObjectIdentity
mibNotifications = _MibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0)
)
if mibBuilder.loadTexts:
    mibNotifications.setStatus("current")
_NotificationObjects_ObjectIdentity = ObjectIdentity
notificationObjects = _NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    notificationObjects.setStatus("current")
_IpAddress_Type = DisplayString
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 1, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_HostName_Type = DisplayString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_ErrorString_Type = DisplayString
_ErrorString_Object = MibScalar
errorString = _ErrorString_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 1, 3),
    _ErrorString_Type()
)
errorString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorString.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 1)
)
if mibBuilder.loadTexts:
    status.setStatus("current")
_BdmsInterfaceStatus_Type = StatusType
_BdmsInterfaceStatus_Object = MibScalar
bdmsInterfaceStatus = _BdmsInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 1, 1),
    _BdmsInterfaceStatus_Type()
)
bdmsInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdmsInterfaceStatus.setStatus("current")
_InBandDataMonitorStatus_Type = StatusType
_InBandDataMonitorStatus_Object = MibScalar
inBandDataMonitorStatus = _InBandDataMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 1, 2),
    _InBandDataMonitorStatus_Type()
)
inBandDataMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBandDataMonitorStatus.setStatus("current")
_PlantInterfaceStatus_Type = StatusType
_PlantInterfaceStatus_Object = MibScalar
plantInterfaceStatus = _PlantInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 1, 3),
    _PlantInterfaceStatus_Type()
)
plantInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plantInterfaceStatus.setStatus("current")
_OutBandDataMonitorStatus_Type = StatusType
_OutBandDataMonitorStatus_Object = MibScalar
outBandDataMonitorStatus = _OutBandDataMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 1, 4),
    _OutBandDataMonitorStatus_Type()
)
outBandDataMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBandDataMonitorStatus.setStatus("current")
_RcsInterfaceStatus_Type = StatusType
_RcsInterfaceStatus_Object = MibScalar
rcsInterfaceStatus = _RcsInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 1, 5),
    _RcsInterfaceStatus_Type()
)
rcsInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcsInterfaceStatus.setStatus("current")
_BdmsInterface_ObjectIdentity = ObjectIdentity
bdmsInterface = _BdmsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2)
)
if mibBuilder.loadTexts:
    bdmsInterface.setStatus("current")
_StatisticsTable_Object = MibTable
statisticsTable = _StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    statisticsTable.setStatus("current")
_StatisticsEntry_Object = MibTableRow
statisticsEntry = _StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1)
)
statisticsEntry.setIndexNames(
    (0, "INVIDI-MIB", "statisticsIndex"),
)
if mibBuilder.loadTexts:
    statisticsEntry.setStatus("current")
_StatisticsIndex_Type = InterfaceType
_StatisticsIndex_Object = MibTableColumn
statisticsIndex = _StatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 1),
    _StatisticsIndex_Type()
)
statisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statisticsIndex.setStatus("current")
_BizStatus_Type = DisplayString
_BizStatus_Object = MibTableColumn
bizStatus = _BizStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 2),
    _BizStatus_Type()
)
bizStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bizStatus.setStatus("current")
_LastStartTime_Type = DisplayString
_LastStartTime_Object = MibTableColumn
lastStartTime = _LastStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 3),
    _LastStartTime_Type()
)
lastStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastStartTime.setStatus("current")
_LastCompletedTime_Type = DisplayString
_LastCompletedTime_Object = MibTableColumn
lastCompletedTime = _LastCompletedTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 4),
    _LastCompletedTime_Type()
)
lastCompletedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCompletedTime.setStatus("current")
_EstimatedNextRequest_Type = DisplayString
_EstimatedNextRequest_Object = MibTableColumn
estimatedNextRequest = _EstimatedNextRequest_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 5),
    _EstimatedNextRequest_Type()
)
estimatedNextRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estimatedNextRequest.setStatus("current")
_CompletedRequests_Type = DisplayString
_CompletedRequests_Object = MibTableColumn
completedRequests = _CompletedRequests_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 6),
    _CompletedRequests_Type()
)
completedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    completedRequests.setStatus("current")
_CompletedReqSinceReset_Type = DisplayString
_CompletedReqSinceReset_Object = MibTableColumn
completedReqSinceReset = _CompletedReqSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 7),
    _CompletedReqSinceReset_Type()
)
completedReqSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    completedReqSinceReset.setStatus("current")
_AcceptedRecords_Type = Integer32
_AcceptedRecords_Object = MibTableColumn
acceptedRecords = _AcceptedRecords_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 8),
    _AcceptedRecords_Type()
)
acceptedRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptedRecords.setStatus("current")
_RejectedRecords_Type = Integer32
_RejectedRecords_Object = MibTableColumn
rejectedRecords = _RejectedRecords_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 9),
    _RejectedRecords_Type()
)
rejectedRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rejectedRecords.setStatus("current")
_LastErrorTime_Type = DisplayString
_LastErrorTime_Object = MibTableColumn
lastErrorTime = _LastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 10),
    _LastErrorTime_Type()
)
lastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastErrorTime.setStatus("current")
_LastError_Type = DisplayString
_LastError_Object = MibTableColumn
lastError = _LastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 2, 1, 1, 11),
    _LastError_Type()
)
lastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastError.setStatus("current")
_InBandDataMonitor_ObjectIdentity = ObjectIdentity
inBandDataMonitor = _InBandDataMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3)
)
if mibBuilder.loadTexts:
    inBandDataMonitor.setStatus("current")
_ViewlistTable_Object = MibTable
viewlistTable = _ViewlistTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    viewlistTable.setStatus("current")
_ViewlistStatisticsEntry_Object = MibTableRow
viewlistStatisticsEntry = _ViewlistStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1)
)
viewlistStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "vlNetwork"),
)
if mibBuilder.loadTexts:
    viewlistStatisticsEntry.setStatus("current")


class _VlNetwork_Type(DisplayString):
    """Custom type vlNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_VlNetwork_Type.__name__ = "DisplayString"
_VlNetwork_Object = MibTableColumn
vlNetwork = _VlNetwork_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 1),
    _VlNetwork_Type()
)
vlNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlNetwork.setStatus("current")
_VlZone_Type = DisplayString
_VlZone_Object = MibTableColumn
vlZone = _VlZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 2),
    _VlZone_Type()
)
vlZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlZone.setStatus("current")
_VlSourceId_Type = Integer32
_VlSourceId_Object = MibTableColumn
vlSourceId = _VlSourceId_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 3),
    _VlSourceId_Type()
)
vlSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlSourceId.setStatus("current")
_VlAVProfileName_Type = DisplayString
_VlAVProfileName_Object = MibTableColumn
vlAVProfileName = _VlAVProfileName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 4),
    _VlAVProfileName_Type()
)
vlAVProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlAVProfileName.setStatus("current")
_VlID_Type = Integer32
_VlID_Object = MibTableColumn
vlID = _VlID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 5),
    _VlID_Type()
)
vlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlID.setStatus("current")
_VlType_Type = DisplayString
_VlType_Object = MibTableColumn
vlType = _VlType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 6),
    _VlType_Type()
)
vlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlType.setStatus("current")
_VlUniqueProgID_Type = Integer32
_VlUniqueProgID_Object = MibTableColumn
vlUniqueProgID = _VlUniqueProgID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 7),
    _VlUniqueProgID_Type()
)
vlUniqueProgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlUniqueProgID.setStatus("current")
_VlAvailNumber_Type = Integer32
_VlAvailNumber_Object = MibTableColumn
vlAvailNumber = _VlAvailNumber_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 8),
    _VlAvailNumber_Type()
)
vlAvailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlAvailNumber.setStatus("current")
_VlWindowID_Type = Integer32
_VlWindowID_Object = MibTableColumn
vlWindowID = _VlWindowID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 9),
    _VlWindowID_Type()
)
vlWindowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlWindowID.setStatus("current")
_VlLength_Type = Integer32
_VlLength_Object = MibTableColumn
vlLength = _VlLength_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 10),
    _VlLength_Type()
)
vlLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlLength.setStatus("current")
_VlNumEntries_Type = Integer32
_VlNumEntries_Object = MibTableColumn
vlNumEntries = _VlNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 11),
    _VlNumEntries_Type()
)
vlNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlNumEntries.setStatus("current")
_VlStartTime_Type = DisplayString
_VlStartTime_Object = MibTableColumn
vlStartTime = _VlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 12),
    _VlStartTime_Type()
)
vlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlStartTime.setStatus("current")
_VlEndTime_Type = DisplayString
_VlEndTime_Object = MibTableColumn
vlEndTime = _VlEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 13),
    _VlEndTime_Type()
)
vlEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlEndTime.setStatus("current")
_VlBreakPos_Type = Integer32
_VlBreakPos_Object = MibTableColumn
vlBreakPos = _VlBreakPos_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 14),
    _VlBreakPos_Type()
)
vlBreakPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBreakPos.setStatus("current")
_VlCueTime_Type = DisplayString
_VlCueTime_Object = MibTableColumn
vlCueTime = _VlCueTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 15),
    _VlCueTime_Type()
)
vlCueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlCueTime.setStatus("current")
_VlCueReceived_Type = DisplayString
_VlCueReceived_Object = MibTableColumn
vlCueReceived = _VlCueReceived_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 16),
    _VlCueReceived_Type()
)
vlCueReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlCueReceived.setStatus("current")
_VlAirTime_Type = DisplayString
_VlAirTime_Object = MibTableColumn
vlAirTime = _VlAirTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 17),
    _VlAirTime_Type()
)
vlAirTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlAirTime.setStatus("current")
_VlExpectedEndTime_Type = DisplayString
_VlExpectedEndTime_Object = MibTableColumn
vlExpectedEndTime = _VlExpectedEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 18),
    _VlExpectedEndTime_Type()
)
vlExpectedEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlExpectedEndTime.setStatus("current")
_VlStatus_Type = DisplayString
_VlStatus_Object = MibTableColumn
vlStatus = _VlStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 19),
    _VlStatus_Type()
)
vlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlStatus.setStatus("current")
_VlReqTimingMsgs_Type = DisplayString
_VlReqTimingMsgs_Object = MibTableColumn
vlReqTimingMsgs = _VlReqTimingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 20),
    _VlReqTimingMsgs_Type()
)
vlReqTimingMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlReqTimingMsgs.setStatus("current")
_VlLastMsgSent_Type = DisplayString
_VlLastMsgSent_Object = MibTableColumn
vlLastMsgSent = _VlLastMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 1, 1, 21),
    _VlLastMsgSent_Type()
)
vlLastMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlLastMsgSent.setStatus("current")
_CueStatisticsTable_Object = MibTable
cueStatisticsTable = _CueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cueStatisticsTable.setStatus("current")
_CueStatisticsEntry_Object = MibTableRow
cueStatisticsEntry = _CueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1)
)
cueStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "qtReceived"),
)
if mibBuilder.loadTexts:
    cueStatisticsEntry.setStatus("current")


class _QtReceived_Type(DisplayString):
    """Custom type qtReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_QtReceived_Type.__name__ = "DisplayString"
_QtReceived_Object = MibTableColumn
qtReceived = _QtReceived_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 1),
    _QtReceived_Type()
)
qtReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtReceived.setStatus("current")
_QtCueTime_Type = DisplayString
_QtCueTime_Object = MibTableColumn
qtCueTime = _QtCueTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 2),
    _QtCueTime_Type()
)
qtCueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtCueTime.setStatus("current")
_QtPtsTime_Type = DisplayString
_QtPtsTime_Object = MibTableColumn
qtPtsTime = _QtPtsTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 3),
    _QtPtsTime_Type()
)
qtPtsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtPtsTime.setStatus("current")
_QtTimeToInsert_Type = DisplayString
_QtTimeToInsert_Object = MibTableColumn
qtTimeToInsert = _QtTimeToInsert_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 4),
    _QtTimeToInsert_Type()
)
qtTimeToInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtTimeToInsert.setStatus("current")
_QtHost_Type = DisplayString
_QtHost_Object = MibTableColumn
qtHost = _QtHost_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 5),
    _QtHost_Type()
)
qtHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtHost.setStatus("current")
_QtNetwork_Type = DisplayString
_QtNetwork_Object = MibTableColumn
qtNetwork = _QtNetwork_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 6),
    _QtNetwork_Type()
)
qtNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtNetwork.setStatus("current")
_QtZone_Type = DisplayString
_QtZone_Object = MibTableColumn
qtZone = _QtZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 7),
    _QtZone_Type()
)
qtZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtZone.setStatus("current")
_QtPid_Type = Integer32
_QtPid_Object = MibTableColumn
qtPid = _QtPid_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 8),
    _QtPid_Type()
)
qtPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtPid.setStatus("current")
_QtSourceId_Type = Integer32
_QtSourceId_Object = MibTableColumn
qtSourceId = _QtSourceId_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 9),
    _QtSourceId_Type()
)
qtSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtSourceId.setStatus("current")
_QtBreakId_Type = Integer32
_QtBreakId_Object = MibTableColumn
qtBreakId = _QtBreakId_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 10),
    _QtBreakId_Type()
)
qtBreakId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtBreakId.setStatus("current")
_QtUniqueProgID_Type = Integer32
_QtUniqueProgID_Object = MibTableColumn
qtUniqueProgID = _QtUniqueProgID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 11),
    _QtUniqueProgID_Type()
)
qtUniqueProgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtUniqueProgID.setStatus("current")
_QtAvailNumber_Type = Integer32
_QtAvailNumber_Object = MibTableColumn
qtAvailNumber = _QtAvailNumber_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 12),
    _QtAvailNumber_Type()
)
qtAvailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtAvailNumber.setStatus("current")
_QtStartTime_Type = DisplayString
_QtStartTime_Object = MibTableColumn
qtStartTime = _QtStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 13),
    _QtStartTime_Type()
)
qtStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtStartTime.setStatus("current")
_QtEndTime_Type = DisplayString
_QtEndTime_Object = MibTableColumn
qtEndTime = _QtEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 14),
    _QtEndTime_Type()
)
qtEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtEndTime.setStatus("current")
_QtBreakPos_Type = Integer32
_QtBreakPos_Object = MibTableColumn
qtBreakPos = _QtBreakPos_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 15),
    _QtBreakPos_Type()
)
qtBreakPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtBreakPos.setStatus("current")
_QtStatus_Type = DisplayString
_QtStatus_Object = MibTableColumn
qtStatus = _QtStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 2, 1, 16),
    _QtStatus_Type()
)
qtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtStatus.setStatus("current")
_InbandStbTable_Object = MibTable
inbandStbTable = _InbandStbTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    inbandStbTable.setStatus("current")
_InbandStbStatisticsEntry_Object = MibTableRow
inbandStbStatisticsEntry = _InbandStbStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 3, 1)
)
inbandStbStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "inMessageType"),
)
if mibBuilder.loadTexts:
    inbandStbStatisticsEntry.setStatus("current")


class _InMessageType_Type(DisplayString):
    """Custom type inMessageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_InMessageType_Type.__name__ = "DisplayString"
_InMessageType_Object = MibTableColumn
inMessageType = _InMessageType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 3, 1, 1),
    _InMessageType_Type()
)
inMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inMessageType.setStatus("current")
_InBytesTransfered_Type = DisplayString
_InBytesTransfered_Object = MibTableColumn
inBytesTransfered = _InBytesTransfered_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 3, 1, 2),
    _InBytesTransfered_Type()
)
inBytesTransfered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBytesTransfered.setStatus("current")
_InMessages_Type = Integer32
_InMessages_Object = MibTableColumn
inMessages = _InMessages_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 3, 1, 3),
    _InMessages_Type()
)
inMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inMessages.setStatus("current")
_InStartTime_Type = DisplayString
_InStartTime_Object = MibTableColumn
inStartTime = _InStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 3, 1, 4),
    _InStartTime_Type()
)
inStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inStartTime.setStatus("current")
_InAverageRate_Type = DisplayString
_InAverageRate_Object = MibTableColumn
inAverageRate = _InAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 3, 1, 5),
    _InAverageRate_Type()
)
inAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAverageRate.setStatus("current")
_InLastMessageTimeAndSize_Type = DisplayString
_InLastMessageTimeAndSize_Object = MibTableColumn
inLastMessageTimeAndSize = _InLastMessageTimeAndSize_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 3, 1, 6),
    _InLastMessageTimeAndSize_Type()
)
inLastMessageTimeAndSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLastMessageTimeAndSize.setStatus("current")
_UnViewlistTable_Object = MibTable
unViewlistTable = _UnViewlistTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    unViewlistTable.setStatus("current")
_UnViewlistStatisticsEntry_Object = MibTableRow
unViewlistStatisticsEntry = _UnViewlistStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1)
)
unViewlistStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "unvlNetwork"),
)
if mibBuilder.loadTexts:
    unViewlistStatisticsEntry.setStatus("current")


class _UnvlNetwork_Type(DisplayString):
    """Custom type unvlNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_UnvlNetwork_Type.__name__ = "DisplayString"
_UnvlNetwork_Object = MibTableColumn
unvlNetwork = _UnvlNetwork_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 1),
    _UnvlNetwork_Type()
)
unvlNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlNetwork.setStatus("current")
_UnvlZone_Type = DisplayString
_UnvlZone_Object = MibTableColumn
unvlZone = _UnvlZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 2),
    _UnvlZone_Type()
)
unvlZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlZone.setStatus("current")
_UnvlSourceId_Type = Integer32
_UnvlSourceId_Object = MibTableColumn
unvlSourceId = _UnvlSourceId_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 3),
    _UnvlSourceId_Type()
)
unvlSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlSourceId.setStatus("current")
_UnvlAVProfileName_Type = DisplayString
_UnvlAVProfileName_Object = MibTableColumn
unvlAVProfileName = _UnvlAVProfileName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 4),
    _UnvlAVProfileName_Type()
)
unvlAVProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlAVProfileName.setStatus("current")
_UnvlID_Type = Integer32
_UnvlID_Object = MibTableColumn
unvlID = _UnvlID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 5),
    _UnvlID_Type()
)
unvlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlID.setStatus("current")
_UnvlType_Type = DisplayString
_UnvlType_Object = MibTableColumn
unvlType = _UnvlType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 6),
    _UnvlType_Type()
)
unvlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlType.setStatus("current")
_UnvlUniqueProgID_Type = Integer32
_UnvlUniqueProgID_Object = MibTableColumn
unvlUniqueProgID = _UnvlUniqueProgID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 7),
    _UnvlUniqueProgID_Type()
)
unvlUniqueProgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlUniqueProgID.setStatus("current")
_UnvlAvailNumber_Type = Integer32
_UnvlAvailNumber_Object = MibTableColumn
unvlAvailNumber = _UnvlAvailNumber_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 8),
    _UnvlAvailNumber_Type()
)
unvlAvailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlAvailNumber.setStatus("current")
_UnvlWindowID_Type = Integer32
_UnvlWindowID_Object = MibTableColumn
unvlWindowID = _UnvlWindowID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 9),
    _UnvlWindowID_Type()
)
unvlWindowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlWindowID.setStatus("current")
_UnvlLength_Type = Integer32
_UnvlLength_Object = MibTableColumn
unvlLength = _UnvlLength_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 10),
    _UnvlLength_Type()
)
unvlLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlLength.setStatus("current")
_UnvlNumEntries_Type = Integer32
_UnvlNumEntries_Object = MibTableColumn
unvlNumEntries = _UnvlNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 11),
    _UnvlNumEntries_Type()
)
unvlNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlNumEntries.setStatus("current")
_UnvlStartTime_Type = DisplayString
_UnvlStartTime_Object = MibTableColumn
unvlStartTime = _UnvlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 12),
    _UnvlStartTime_Type()
)
unvlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlStartTime.setStatus("current")
_UnvlEndTime_Type = DisplayString
_UnvlEndTime_Object = MibTableColumn
unvlEndTime = _UnvlEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 13),
    _UnvlEndTime_Type()
)
unvlEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlEndTime.setStatus("current")
_UnvlBreakPos_Type = Integer32
_UnvlBreakPos_Object = MibTableColumn
unvlBreakPos = _UnvlBreakPos_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 14),
    _UnvlBreakPos_Type()
)
unvlBreakPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlBreakPos.setStatus("current")
_UnvlCueTime_Type = DisplayString
_UnvlCueTime_Object = MibTableColumn
unvlCueTime = _UnvlCueTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 15),
    _UnvlCueTime_Type()
)
unvlCueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlCueTime.setStatus("current")
_UnvlCueReceived_Type = DisplayString
_UnvlCueReceived_Object = MibTableColumn
unvlCueReceived = _UnvlCueReceived_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 16),
    _UnvlCueReceived_Type()
)
unvlCueReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlCueReceived.setStatus("current")
_UnvlAirTime_Type = DisplayString
_UnvlAirTime_Object = MibTableColumn
unvlAirTime = _UnvlAirTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 17),
    _UnvlAirTime_Type()
)
unvlAirTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlAirTime.setStatus("current")
_UnvlExpectedEndTime_Type = DisplayString
_UnvlExpectedEndTime_Object = MibTableColumn
unvlExpectedEndTime = _UnvlExpectedEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 18),
    _UnvlExpectedEndTime_Type()
)
unvlExpectedEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlExpectedEndTime.setStatus("current")
_UnvlStatus_Type = DisplayString
_UnvlStatus_Object = MibTableColumn
unvlStatus = _UnvlStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 19),
    _UnvlStatus_Type()
)
unvlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlStatus.setStatus("current")
_UnvlReqTimingMsgs_Type = DisplayString
_UnvlReqTimingMsgs_Object = MibTableColumn
unvlReqTimingMsgs = _UnvlReqTimingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 20),
    _UnvlReqTimingMsgs_Type()
)
unvlReqTimingMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlReqTimingMsgs.setStatus("current")
_UnvlLastMsgSent_Type = DisplayString
_UnvlLastMsgSent_Object = MibTableColumn
unvlLastMsgSent = _UnvlLastMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 4, 1, 21),
    _UnvlLastMsgSent_Type()
)
unvlLastMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unvlLastMsgSent.setStatus("current")
_DiscardedTable_Object = MibTable
discardedTable = _DiscardedTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    discardedTable.setStatus("current")
_DiscardedEntry_Object = MibTableRow
discardedEntry = _DiscardedEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1)
)
discardedEntry.setIndexNames(
    (1, "INVIDI-MIB", "disNetwork"),
)
if mibBuilder.loadTexts:
    discardedEntry.setStatus("current")


class _DisNetwork_Type(DisplayString):
    """Custom type disNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_DisNetwork_Type.__name__ = "DisplayString"
_DisNetwork_Object = MibTableColumn
disNetwork = _DisNetwork_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 1),
    _DisNetwork_Type()
)
disNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disNetwork.setStatus("current")
_DisZone_Type = DisplayString
_DisZone_Object = MibTableColumn
disZone = _DisZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 2),
    _DisZone_Type()
)
disZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disZone.setStatus("current")
_DisSourceId_Type = Integer32
_DisSourceId_Object = MibTableColumn
disSourceId = _DisSourceId_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 3),
    _DisSourceId_Type()
)
disSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disSourceId.setStatus("current")
_DisAVProfileName_Type = DisplayString
_DisAVProfileName_Object = MibTableColumn
disAVProfileName = _DisAVProfileName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 4),
    _DisAVProfileName_Type()
)
disAVProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disAVProfileName.setStatus("current")
_DisID_Type = Integer32
_DisID_Object = MibTableColumn
disID = _DisID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 5),
    _DisID_Type()
)
disID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disID.setStatus("current")
_DisType_Type = DisplayString
_DisType_Object = MibTableColumn
disType = _DisType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 6),
    _DisType_Type()
)
disType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disType.setStatus("current")
_DisUniqueProgID_Type = Integer32
_DisUniqueProgID_Object = MibTableColumn
disUniqueProgID = _DisUniqueProgID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 7),
    _DisUniqueProgID_Type()
)
disUniqueProgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disUniqueProgID.setStatus("current")
_DisAvailNumber_Type = Integer32
_DisAvailNumber_Object = MibTableColumn
disAvailNumber = _DisAvailNumber_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 8),
    _DisAvailNumber_Type()
)
disAvailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disAvailNumber.setStatus("current")
_DisWindowID_Type = Integer32
_DisWindowID_Object = MibTableColumn
disWindowID = _DisWindowID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 9),
    _DisWindowID_Type()
)
disWindowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disWindowID.setStatus("current")
_DisLength_Type = Integer32
_DisLength_Object = MibTableColumn
disLength = _DisLength_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 10),
    _DisLength_Type()
)
disLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disLength.setStatus("current")
_DisNumEntries_Type = Integer32
_DisNumEntries_Object = MibTableColumn
disNumEntries = _DisNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 11),
    _DisNumEntries_Type()
)
disNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disNumEntries.setStatus("current")
_DisStartTime_Type = DisplayString
_DisStartTime_Object = MibTableColumn
disStartTime = _DisStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 12),
    _DisStartTime_Type()
)
disStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disStartTime.setStatus("current")
_DisEndTime_Type = DisplayString
_DisEndTime_Object = MibTableColumn
disEndTime = _DisEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 13),
    _DisEndTime_Type()
)
disEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disEndTime.setStatus("current")
_DisBreakPos_Type = Integer32
_DisBreakPos_Object = MibTableColumn
disBreakPos = _DisBreakPos_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 14),
    _DisBreakPos_Type()
)
disBreakPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disBreakPos.setStatus("current")
_DisCueTime_Type = DisplayString
_DisCueTime_Object = MibTableColumn
disCueTime = _DisCueTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 15),
    _DisCueTime_Type()
)
disCueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disCueTime.setStatus("current")
_DisCueReceived_Type = DisplayString
_DisCueReceived_Object = MibTableColumn
disCueReceived = _DisCueReceived_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 16),
    _DisCueReceived_Type()
)
disCueReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disCueReceived.setStatus("current")
_DisAirTime_Type = DisplayString
_DisAirTime_Object = MibTableColumn
disAirTime = _DisAirTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 17),
    _DisAirTime_Type()
)
disAirTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disAirTime.setStatus("current")
_DisExpectedEndTime_Type = DisplayString
_DisExpectedEndTime_Object = MibTableColumn
disExpectedEndTime = _DisExpectedEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 18),
    _DisExpectedEndTime_Type()
)
disExpectedEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disExpectedEndTime.setStatus("current")
_DisStatus_Type = DisplayString
_DisStatus_Object = MibTableColumn
disStatus = _DisStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 19),
    _DisStatus_Type()
)
disStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disStatus.setStatus("current")
_DisReqTimingMsgs_Type = DisplayString
_DisReqTimingMsgs_Object = MibTableColumn
disReqTimingMsgs = _DisReqTimingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 20),
    _DisReqTimingMsgs_Type()
)
disReqTimingMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disReqTimingMsgs.setStatus("current")
_DisLastMsgSent_Type = DisplayString
_DisLastMsgSent_Object = MibTableColumn
disLastMsgSent = _DisLastMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 5, 1, 21),
    _DisLastMsgSent_Type()
)
disLastMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disLastMsgSent.setStatus("current")
_AssetErrorTable_Object = MibTable
assetErrorTable = _AssetErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    assetErrorTable.setStatus("current")
_AssetErrorEntry_Object = MibTableRow
assetErrorEntry = _AssetErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 6, 1)
)
assetErrorEntry.setIndexNames(
    (1, "INVIDI-MIB", "aeTime"),
)
if mibBuilder.loadTexts:
    assetErrorEntry.setStatus("current")


class _AeTime_Type(DisplayString):
    """Custom type aeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_AeTime_Type.__name__ = "DisplayString"
_AeTime_Object = MibTableColumn
aeTime = _AeTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 6, 1, 1),
    _AeTime_Type()
)
aeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeTime.setStatus("current")
_AeDescription_Type = DisplayString
_AeDescription_Object = MibTableColumn
aeDescription = _AeDescription_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 3, 6, 1, 2),
    _AeDescription_Type()
)
aeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeDescription.setStatus("current")
_PlantInterface_ObjectIdentity = ObjectIdentity
plantInterface = _PlantInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4)
)
if mibBuilder.loadTexts:
    plantInterface.setStatus("current")
_AdInserterTable_Object = MibTable
adInserterTable = _AdInserterTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adInserterTable.setStatus("current")
_AdInserterStatisticsEntry_Object = MibTableRow
adInserterStatisticsEntry = _AdInserterStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1)
)
adInserterStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "adinsName"),
)
if mibBuilder.loadTexts:
    adInserterStatisticsEntry.setStatus("current")


class _AdinsName_Type(DisplayString):
    """Custom type adinsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_AdinsName_Type.__name__ = "DisplayString"
_AdinsName_Object = MibTableColumn
adinsName = _AdinsName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1, 1),
    _AdinsName_Type()
)
adinsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adinsName.setStatus("current")
_AdinsIndex_Type = DisplayString
_AdinsIndex_Object = MibTableColumn
adinsIndex = _AdinsIndex_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1, 2),
    _AdinsIndex_Type()
)
adinsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adinsIndex.setStatus("current")
_AdinsStatus_Type = DisplayString
_AdinsStatus_Object = MibTableColumn
adinsStatus = _AdinsStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1, 3),
    _AdinsStatus_Type()
)
adinsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adinsStatus.setStatus("current")
_AdinsSuccesses_Type = Integer32
_AdinsSuccesses_Object = MibTableColumn
adinsSuccesses = _AdinsSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1, 4),
    _AdinsSuccesses_Type()
)
adinsSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adinsSuccesses.setStatus("current")
_AdinsSuccessTime_Type = DisplayString
_AdinsSuccessTime_Object = MibTableColumn
adinsSuccessTime = _AdinsSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1, 5),
    _AdinsSuccessTime_Type()
)
adinsSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adinsSuccessTime.setStatus("current")
_AdinsFailures_Type = Integer32
_AdinsFailures_Object = MibTableColumn
adinsFailures = _AdinsFailures_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1, 6),
    _AdinsFailures_Type()
)
adinsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adinsFailures.setStatus("current")
_AdinsFailTime_Type = DisplayString
_AdinsFailTime_Object = MibTableColumn
adinsFailTime = _AdinsFailTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1, 7),
    _AdinsFailTime_Type()
)
adinsFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adinsFailTime.setStatus("current")
_AdinsError_Type = DisplayString
_AdinsError_Object = MibTableColumn
adinsError = _AdinsError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 1, 1, 8),
    _AdinsError_Type()
)
adinsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adinsError.setStatus("current")
_InsStreamConfigStatisticsTable_Object = MibTable
insStreamConfigStatisticsTable = _InsStreamConfigStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    insStreamConfigStatisticsTable.setStatus("current")
_InsStreamConfigStatisticsEntry_Object = MibTableRow
insStreamConfigStatisticsEntry = _InsStreamConfigStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1)
)
insStreamConfigStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "insStreamAdInsName"),
)
if mibBuilder.loadTexts:
    insStreamConfigStatisticsEntry.setStatus("current")


class _InsStreamAdInsName_Type(DisplayString):
    """Custom type insStreamAdInsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_InsStreamAdInsName_Type.__name__ = "DisplayString"
_InsStreamAdInsName_Object = MibTableColumn
insStreamAdInsName = _InsStreamAdInsName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 1),
    _InsStreamAdInsName_Type()
)
insStreamAdInsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamAdInsName.setStatus("current")
_InsStreamAdInsType_Type = DisplayString
_InsStreamAdInsType_Object = MibTableColumn
insStreamAdInsType = _InsStreamAdInsType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 2),
    _InsStreamAdInsType_Type()
)
insStreamAdInsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamAdInsType.setStatus("current")
_InsStreamAdChEIA_Type = Integer32
_InsStreamAdChEIA_Object = MibTableColumn
insStreamAdChEIA = _InsStreamAdChEIA_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 3),
    _InsStreamAdChEIA_Type()
)
insStreamAdChEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamAdChEIA.setStatus("current")
_InsStreamAdChFreq_Type = DisplayString
_InsStreamAdChFreq_Object = MibTableColumn
insStreamAdChFreq = _InsStreamAdChFreq_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 4),
    _InsStreamAdChFreq_Type()
)
insStreamAdChFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamAdChFreq.setStatus("current")
_InsStreamAdChMod_Type = DisplayString
_InsStreamAdChMod_Object = MibTableColumn
insStreamAdChMod = _InsStreamAdChMod_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 5),
    _InsStreamAdChMod_Type()
)
insStreamAdChMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamAdChMod.setStatus("current")
_InsStreamTBID_Type = Integer32
_InsStreamTBID_Object = MibTableColumn
insStreamTBID = _InsStreamTBID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 6),
    _InsStreamTBID_Type()
)
insStreamTBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamTBID.setStatus("current")
_InsStreamTBZone_Type = DisplayString
_InsStreamTBZone_Object = MibTableColumn
insStreamTBZone = _InsStreamTBZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 7),
    _InsStreamTBZone_Type()
)
insStreamTBZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamTBZone.setStatus("current")
_InsStreamIUID_Type = Integer32
_InsStreamIUID_Object = MibTableColumn
insStreamIUID = _InsStreamIUID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 8),
    _InsStreamIUID_Type()
)
insStreamIUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamIUID.setStatus("current")
_InsStreamTCID_Type = Integer32
_InsStreamTCID_Object = MibTableColumn
insStreamTCID = _InsStreamTCID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 9),
    _InsStreamTCID_Type()
)
insStreamTCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamTCID.setStatus("current")
_InsStreamChName_Type = DisplayString
_InsStreamChName_Object = MibTableColumn
insStreamChName = _InsStreamChName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 10),
    _InsStreamChName_Type()
)
insStreamChName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamChName.setStatus("current")
_InsStreamChZone_Type = DisplayString
_InsStreamChZone_Object = MibTableColumn
insStreamChZone = _InsStreamChZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 11),
    _InsStreamChZone_Type()
)
insStreamChZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamChZone.setStatus("current")
_InsStreamHiddenCh_Type = Integer32
_InsStreamHiddenCh_Object = MibTableColumn
insStreamHiddenCh = _InsStreamHiddenCh_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 12),
    _InsStreamHiddenCh_Type()
)
insStreamHiddenCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamHiddenCh.setStatus("current")
_InsStreamAvProCat_Type = DisplayString
_InsStreamAvProCat_Object = MibTableColumn
insStreamAvProCat = _InsStreamAvProCat_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 13),
    _InsStreamAvProCat_Type()
)
insStreamAvProCat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamAvProCat.setStatus("current")
_InsStreamProgramNum_Type = Integer32
_InsStreamProgramNum_Object = MibTableColumn
insStreamProgramNum = _InsStreamProgramNum_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 14),
    _InsStreamProgramNum_Type()
)
insStreamProgramNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamProgramNum.setStatus("current")
_InsStreamPreroll_Type = Integer32
_InsStreamPreroll_Object = MibTableColumn
insStreamPreroll = _InsStreamPreroll_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 2, 1, 15),
    _InsStreamPreroll_Type()
)
insStreamPreroll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insStreamPreroll.setStatus("current")
_VirtualStreamConfigTable_Object = MibTable
virtualStreamConfigTable = _VirtualStreamConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    virtualStreamConfigTable.setStatus("current")
_VirtualStreamConfigEntry_Object = MibTableRow
virtualStreamConfigEntry = _VirtualStreamConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 3, 1)
)
virtualStreamConfigEntry.setIndexNames(
    (1, "INVIDI-MIB", "virtualStreamIUID"),
)
if mibBuilder.loadTexts:
    virtualStreamConfigEntry.setStatus("current")
_VirtualStreamIUID_Type = ObjectIdentifier
_VirtualStreamIUID_Object = MibTableColumn
virtualStreamIUID = _VirtualStreamIUID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 3, 1, 1),
    _VirtualStreamIUID_Type()
)
virtualStreamIUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualStreamIUID.setStatus("current")
_VirtualStreamTCID_Type = Integer32
_VirtualStreamTCID_Object = MibTableColumn
virtualStreamTCID = _VirtualStreamTCID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 3, 1, 2),
    _VirtualStreamTCID_Type()
)
virtualStreamTCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualStreamTCID.setStatus("current")
_VirtualStreamZONE_Type = DisplayString
_VirtualStreamZONE_Object = MibTableColumn
virtualStreamZONE = _VirtualStreamZONE_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 3, 1, 3),
    _VirtualStreamZONE_Type()
)
virtualStreamZONE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualStreamZONE.setStatus("current")
_AssetManagementTable_Object = MibTable
assetManagementTable = _AssetManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    assetManagementTable.setStatus("current")
_AssetManagementStatisticsEntry_Object = MibTableRow
assetManagementStatisticsEntry = _AssetManagementStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4, 1)
)
assetManagementStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "amsName"),
)
if mibBuilder.loadTexts:
    assetManagementStatisticsEntry.setStatus("current")
_AmsName_Type = DisplayString
_AmsName_Object = MibTableColumn
amsName = _AmsName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4, 1, 1),
    _AmsName_Type()
)
amsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsName.setStatus("current")
_AmsStatus_Type = DisplayString
_AmsStatus_Object = MibTableColumn
amsStatus = _AmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4, 1, 2),
    _AmsStatus_Type()
)
amsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsStatus.setStatus("current")
_AmsSuccesses_Type = Counter32
_AmsSuccesses_Object = MibTableColumn
amsSuccesses = _AmsSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4, 1, 3),
    _AmsSuccesses_Type()
)
amsSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsSuccesses.setStatus("current")
_AmsSuccessTime_Type = DisplayString
_AmsSuccessTime_Object = MibTableColumn
amsSuccessTime = _AmsSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4, 1, 4),
    _AmsSuccessTime_Type()
)
amsSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsSuccessTime.setStatus("current")
_AmsFailures_Type = Counter32
_AmsFailures_Object = MibTableColumn
amsFailures = _AmsFailures_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4, 1, 5),
    _AmsFailures_Type()
)
amsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsFailures.setStatus("current")
_AmsFailTime_Type = DisplayString
_AmsFailTime_Object = MibTableColumn
amsFailTime = _AmsFailTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4, 1, 6),
    _AmsFailTime_Type()
)
amsFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsFailTime.setStatus("current")
_AmsError_Type = DisplayString
_AmsError_Object = MibTableColumn
amsError = _AmsError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 4, 1, 7),
    _AmsError_Type()
)
amsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsError.setStatus("current")
_AdConnTable_Object = MibTable
adConnTable = _AdConnTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    adConnTable.setStatus("current")
_AdConnectionEntry_Object = MibTableRow
adConnectionEntry = _AdConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5, 1)
)
adConnectionEntry.setIndexNames(
    (1, "INVIDI-MIB", "advName"),
)
if mibBuilder.loadTexts:
    adConnectionEntry.setStatus("current")


class _AdvName_Type(DisplayString):
    """Custom type advName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_AdvName_Type.__name__ = "DisplayString"
_AdvName_Object = MibTableColumn
advName = _AdvName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5, 1, 1),
    _AdvName_Type()
)
advName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advName.setStatus("current")
_AdvAddress_Type = DisplayString
_AdvAddress_Object = MibTableColumn
advAddress = _AdvAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5, 1, 2),
    _AdvAddress_Type()
)
advAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advAddress.setStatus("current")
_AdvPort_Type = DisplayString
_AdvPort_Object = MibTableColumn
advPort = _AdvPort_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5, 1, 3),
    _AdvPort_Type()
)
advPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advPort.setStatus("current")
_AdvStatus_Type = DisplayString
_AdvStatus_Object = MibTableColumn
advStatus = _AdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5, 1, 4),
    _AdvStatus_Type()
)
advStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advStatus.setStatus("current")
_AdvLastSuccess_Type = DisplayString
_AdvLastSuccess_Object = MibTableColumn
advLastSuccess = _AdvLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5, 1, 5),
    _AdvLastSuccess_Type()
)
advLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advLastSuccess.setStatus("current")
_AdvLastFail_Type = DisplayString
_AdvLastFail_Object = MibTableColumn
advLastFail = _AdvLastFail_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5, 1, 6),
    _AdvLastFail_Type()
)
advLastFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advLastFail.setStatus("current")
_AdvLastError_Type = DisplayString
_AdvLastError_Object = MibTableColumn
advLastError = _AdvLastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 5, 1, 7),
    _AdvLastError_Type()
)
advLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advLastError.setStatus("current")
_MuxSvcTable_Object = MibTable
muxSvcTable = _MuxSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    muxSvcTable.setStatus("current")
_MuxServiceEntry_Object = MibTableRow
muxServiceEntry = _MuxServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6, 1)
)
muxServiceEntry.setIndexNames(
    (1, "INVIDI-MIB", "muxID"),
)
if mibBuilder.loadTexts:
    muxServiceEntry.setStatus("current")
_MuxID_Type = ObjectIdentifier
_MuxID_Object = MibTableColumn
muxID = _MuxID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6, 1, 1),
    _MuxID_Type()
)
muxID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxID.setStatus("current")
_MuxDescription_Type = DisplayString
_MuxDescription_Object = MibTableColumn
muxDescription = _MuxDescription_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6, 1, 2),
    _MuxDescription_Type()
)
muxDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxDescription.setStatus("current")
_MuxVersion_Type = DisplayString
_MuxVersion_Object = MibTableColumn
muxVersion = _MuxVersion_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6, 1, 3),
    _MuxVersion_Type()
)
muxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxVersion.setStatus("current")
_MuxSequence_Type = Integer32
_MuxSequence_Object = MibTableColumn
muxSequence = _MuxSequence_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6, 1, 4),
    _MuxSequence_Type()
)
muxSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxSequence.setStatus("current")
_MuxAddress_Type = DisplayString
_MuxAddress_Object = MibTableColumn
muxAddress = _MuxAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6, 1, 5),
    _MuxAddress_Type()
)
muxAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxAddress.setStatus("current")
_MuxPreferred_Type = DisplayString
_MuxPreferred_Object = MibTableColumn
muxPreferred = _MuxPreferred_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6, 1, 6),
    _MuxPreferred_Type()
)
muxPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxPreferred.setStatus("current")
_MuxSvcList_Type = DisplayString
_MuxSvcList_Object = MibTableColumn
muxSvcList = _MuxSvcList_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 6, 1, 7),
    _MuxSvcList_Type()
)
muxSvcList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxSvcList.setStatus("current")
_Scte35Table_Object = MibTable
scte35Table = _Scte35Table_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    scte35Table.setStatus("current")
_Scte35ReceiverEntry_Object = MibTableRow
scte35ReceiverEntry = _Scte35ReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 7, 1)
)
scte35ReceiverEntry.setIndexNames(
    (1, "INVIDI-MIB", "scte35Name"),
)
if mibBuilder.loadTexts:
    scte35ReceiverEntry.setStatus("current")


class _Scte35Name_Type(DisplayString):
    """Custom type scte35Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_Scte35Name_Type.__name__ = "DisplayString"
_Scte35Name_Object = MibTableColumn
scte35Name = _Scte35Name_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 7, 1, 1),
    _Scte35Name_Type()
)
scte35Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35Name.setStatus("current")
_Scte35CueRecvTime_Type = DisplayString
_Scte35CueRecvTime_Object = MibTableColumn
scte35CueRecvTime = _Scte35CueRecvTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 7, 1, 2),
    _Scte35CueRecvTime_Type()
)
scte35CueRecvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35CueRecvTime.setStatus("current")
_Scte35Status_Type = DisplayString
_Scte35Status_Object = MibTableColumn
scte35Status = _Scte35Status_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 7, 1, 3),
    _Scte35Status_Type()
)
scte35Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35Status.setStatus("current")
_Scte35SuccessTime_Type = DisplayString
_Scte35SuccessTime_Object = MibTableColumn
scte35SuccessTime = _Scte35SuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 7, 1, 4),
    _Scte35SuccessTime_Type()
)
scte35SuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35SuccessTime.setStatus("current")
_Scte35FailTime_Type = DisplayString
_Scte35FailTime_Object = MibTableColumn
scte35FailTime = _Scte35FailTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 7, 1, 5),
    _Scte35FailTime_Type()
)
scte35FailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35FailTime.setStatus("current")
_Scte35Error_Type = DisplayString
_Scte35Error_Object = MibTableColumn
scte35Error = _Scte35Error_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 7, 1, 6),
    _Scte35Error_Type()
)
scte35Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35Error.setStatus("current")
_ServiceSCTE35CueReceiverMapTable_Object = MibTable
serviceSCTE35CueReceiverMapTable = _ServiceSCTE35CueReceiverMapTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    serviceSCTE35CueReceiverMapTable.setStatus("current")
_ServiceSCTE35CueReceiverMapEntry_Object = MibTableRow
serviceSCTE35CueReceiverMapEntry = _ServiceSCTE35CueReceiverMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 8, 1)
)
serviceSCTE35CueReceiverMapEntry.setIndexNames(
    (1, "INVIDI-MIB", "scte35CueSvcID"),
)
if mibBuilder.loadTexts:
    serviceSCTE35CueReceiverMapEntry.setStatus("current")
_Scte35CueSvcID_Type = ObjectIdentifier
_Scte35CueSvcID_Object = MibTableColumn
scte35CueSvcID = _Scte35CueSvcID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 8, 1, 1),
    _Scte35CueSvcID_Type()
)
scte35CueSvcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35CueSvcID.setStatus("current")
_Scte35CueSvcName_Type = DisplayString
_Scte35CueSvcName_Object = MibTableColumn
scte35CueSvcName = _Scte35CueSvcName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 8, 1, 2),
    _Scte35CueSvcName_Type()
)
scte35CueSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35CueSvcName.setStatus("current")
_Scte35CueSvcZone_Type = DisplayString
_Scte35CueSvcZone_Object = MibTableColumn
scte35CueSvcZone = _Scte35CueSvcZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 8, 1, 3),
    _Scte35CueSvcZone_Type()
)
scte35CueSvcZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35CueSvcZone.setStatus("current")
_Scte35CueSvcPID_Type = DisplayString
_Scte35CueSvcPID_Object = MibTableColumn
scte35CueSvcPID = _Scte35CueSvcPID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 8, 1, 4),
    _Scte35CueSvcPID_Type()
)
scte35CueSvcPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35CueSvcPID.setStatus("current")
_Scte35CueReceiverAddr_Type = DisplayString
_Scte35CueReceiverAddr_Object = MibTableColumn
scte35CueReceiverAddr = _Scte35CueReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 8, 1, 5),
    _Scte35CueReceiverAddr_Type()
)
scte35CueReceiverAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scte35CueReceiverAddr.setStatus("current")
_CueConnectTable_Object = MibTable
cueConnectTable = _CueConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9)
)
if mibBuilder.loadTexts:
    cueConnectTable.setStatus("current")
_CueConnectEntry_Object = MibTableRow
cueConnectEntry = _CueConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1)
)
cueConnectEntry.setIndexNames(
    (1, "INVIDI-MIB", "cueSvcID"),
)
if mibBuilder.loadTexts:
    cueConnectEntry.setStatus("current")
_CueSvcID_Type = ObjectIdentifier
_CueSvcID_Object = MibTableColumn
cueSvcID = _CueSvcID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 1),
    _CueSvcID_Type()
)
cueSvcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcID.setStatus("current")
_CueSvcName_Type = DisplayString
_CueSvcName_Object = MibTableColumn
cueSvcName = _CueSvcName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 2),
    _CueSvcName_Type()
)
cueSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcName.setStatus("current")
_CueSvcZone_Type = DisplayString
_CueSvcZone_Object = MibTableColumn
cueSvcZone = _CueSvcZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 3),
    _CueSvcZone_Type()
)
cueSvcZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcZone.setStatus("current")
_CueSvcMuxID_Type = Integer32
_CueSvcMuxID_Object = MibTableColumn
cueSvcMuxID = _CueSvcMuxID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 4),
    _CueSvcMuxID_Type()
)
cueSvcMuxID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcMuxID.setStatus("current")
_CueSvcLastRecvTime_Type = DisplayString
_CueSvcLastRecvTime_Object = MibTableColumn
cueSvcLastRecvTime = _CueSvcLastRecvTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 5),
    _CueSvcLastRecvTime_Type()
)
cueSvcLastRecvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcLastRecvTime.setStatus("current")
_CueSvcStatus_Type = DisplayString
_CueSvcStatus_Object = MibTableColumn
cueSvcStatus = _CueSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 6),
    _CueSvcStatus_Type()
)
cueSvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcStatus.setStatus("current")
_CueSvcLastSuccess_Type = DisplayString
_CueSvcLastSuccess_Object = MibTableColumn
cueSvcLastSuccess = _CueSvcLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 7),
    _CueSvcLastSuccess_Type()
)
cueSvcLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcLastSuccess.setStatus("current")
_CueSvcLastFail_Type = DisplayString
_CueSvcLastFail_Object = MibTableColumn
cueSvcLastFail = _CueSvcLastFail_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 8),
    _CueSvcLastFail_Type()
)
cueSvcLastFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcLastFail.setStatus("current")
_CueSvcLastErr_Type = DisplayString
_CueSvcLastErr_Object = MibTableColumn
cueSvcLastErr = _CueSvcLastErr_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 9, 1, 9),
    _CueSvcLastErr_Type()
)
cueSvcLastErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSvcLastErr.setStatus("current")
_InbandConnectTable_Object = MibTable
inbandConnectTable = _InbandConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    inbandConnectTable.setStatus("current")
_InbandConnectEntry_Object = MibTableRow
inbandConnectEntry = _InbandConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1)
)
inbandConnectEntry.setIndexNames(
    (1, "INVIDI-MIB", "inSvcID"),
)
if mibBuilder.loadTexts:
    inbandConnectEntry.setStatus("current")
_InSvcID_Type = ObjectIdentifier
_InSvcID_Object = MibTableColumn
inSvcID = _InSvcID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 1),
    _InSvcID_Type()
)
inSvcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcID.setStatus("current")
_InSvcName_Type = DisplayString
_InSvcName_Object = MibTableColumn
inSvcName = _InSvcName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 2),
    _InSvcName_Type()
)
inSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcName.setStatus("current")
_InSvcZone_Type = DisplayString
_InSvcZone_Object = MibTableColumn
inSvcZone = _InSvcZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 3),
    _InSvcZone_Type()
)
inSvcZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcZone.setStatus("current")
_InSvcPriAddress_Type = DisplayString
_InSvcPriAddress_Object = MibTableColumn
inSvcPriAddress = _InSvcPriAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 4),
    _InSvcPriAddress_Type()
)
inSvcPriAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcPriAddress.setStatus("current")
_InSvcSecAddress_Type = DisplayString
_InSvcSecAddress_Object = MibTableColumn
inSvcSecAddress = _InSvcSecAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 5),
    _InSvcSecAddress_Type()
)
inSvcSecAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcSecAddress.setStatus("current")
_InSvcTerAddress_Type = DisplayString
_InSvcTerAddress_Object = MibTableColumn
inSvcTerAddress = _InSvcTerAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 6),
    _InSvcTerAddress_Type()
)
inSvcTerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcTerAddress.setStatus("current")
_InSvcQuaAddress_Type = DisplayString
_InSvcQuaAddress_Object = MibTableColumn
inSvcQuaAddress = _InSvcQuaAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 7),
    _InSvcQuaAddress_Type()
)
inSvcQuaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcQuaAddress.setStatus("current")
_InSvcVoteLastSendTime_Type = DisplayString
_InSvcVoteLastSendTime_Object = MibTableColumn
inSvcVoteLastSendTime = _InSvcVoteLastSendTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 8),
    _InSvcVoteLastSendTime_Type()
)
inSvcVoteLastSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcVoteLastSendTime.setStatus("current")
_InSvcVlLastSendTime_Type = DisplayString
_InSvcVlLastSendTime_Object = MibTableColumn
inSvcVlLastSendTime = _InSvcVlLastSendTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 9),
    _InSvcVlLastSendTime_Type()
)
inSvcVlLastSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcVlLastSendTime.setStatus("current")
_InSvcBdLastSendTime_Type = DisplayString
_InSvcBdLastSendTime_Object = MibTableColumn
inSvcBdLastSendTime = _InSvcBdLastSendTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 10),
    _InSvcBdLastSendTime_Type()
)
inSvcBdLastSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcBdLastSendTime.setStatus("current")
_InSvcRTMLastSendTime_Type = DisplayString
_InSvcRTMLastSendTime_Object = MibTableColumn
inSvcRTMLastSendTime = _InSvcRTMLastSendTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 11),
    _InSvcRTMLastSendTime_Type()
)
inSvcRTMLastSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcRTMLastSendTime.setStatus("current")
_InSvcCueLastSendTime_Type = DisplayString
_InSvcCueLastSendTime_Object = MibTableColumn
inSvcCueLastSendTime = _InSvcCueLastSendTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 12),
    _InSvcCueLastSendTime_Type()
)
inSvcCueLastSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcCueLastSendTime.setStatus("current")
_InSvcStatus_Type = DisplayString
_InSvcStatus_Object = MibTableColumn
inSvcStatus = _InSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 13),
    _InSvcStatus_Type()
)
inSvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcStatus.setStatus("current")
_InSvcLastSuccess_Type = DisplayString
_InSvcLastSuccess_Object = MibTableColumn
inSvcLastSuccess = _InSvcLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 14),
    _InSvcLastSuccess_Type()
)
inSvcLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcLastSuccess.setStatus("current")
_InSvcLastFail_Type = DisplayString
_InSvcLastFail_Object = MibTableColumn
inSvcLastFail = _InSvcLastFail_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 15),
    _InSvcLastFail_Type()
)
inSvcLastFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcLastFail.setStatus("current")
_InSvcLastErr_Type = DisplayString
_InSvcLastErr_Object = MibTableColumn
inSvcLastErr = _InSvcLastErr_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 10, 1, 16),
    _InSvcLastErr_Type()
)
inSvcLastErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvcLastErr.setStatus("current")
_AssetStateCheckTable_Object = MibTable
assetStateCheckTable = _AssetStateCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11)
)
if mibBuilder.loadTexts:
    assetStateCheckTable.setStatus("current")
_AssetStateCheckStatisticsEntry_Object = MibTableRow
assetStateCheckStatisticsEntry = _AssetStateCheckStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11, 1)
)
assetStateCheckStatisticsEntry.setIndexNames(
    (0, "INVIDI-MIB", "ascName"),
)
if mibBuilder.loadTexts:
    assetStateCheckStatisticsEntry.setStatus("current")


class _AscName_Type(DisplayString):
    """Custom type ascName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_AscName_Type.__name__ = "DisplayString"
_AscName_Object = MibTableColumn
ascName = _AscName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11, 1, 1),
    _AscName_Type()
)
ascName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascName.setStatus("current")
_AscStatus_Type = DisplayString
_AscStatus_Object = MibTableColumn
ascStatus = _AscStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11, 1, 2),
    _AscStatus_Type()
)
ascStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascStatus.setStatus("current")
_AscSuccesses_Type = Integer32
_AscSuccesses_Object = MibTableColumn
ascSuccesses = _AscSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11, 1, 3),
    _AscSuccesses_Type()
)
ascSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascSuccesses.setStatus("current")
_AscSuccessTime_Type = DisplayString
_AscSuccessTime_Object = MibTableColumn
ascSuccessTime = _AscSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11, 1, 4),
    _AscSuccessTime_Type()
)
ascSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascSuccessTime.setStatus("current")
_AscFailures_Type = Integer32
_AscFailures_Object = MibTableColumn
ascFailures = _AscFailures_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11, 1, 5),
    _AscFailures_Type()
)
ascFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascFailures.setStatus("current")
_AscFailTime_Type = DisplayString
_AscFailTime_Object = MibTableColumn
ascFailTime = _AscFailTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11, 1, 6),
    _AscFailTime_Type()
)
ascFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascFailTime.setStatus("current")
_AscError_Type = DisplayString
_AscError_Object = MibTableColumn
ascError = _AscError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 11, 1, 7),
    _AscError_Type()
)
ascError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascError.setStatus("current")
_BdsErrorTable_Object = MibTable
bdsErrorTable = _BdsErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 12)
)
if mibBuilder.loadTexts:
    bdsErrorTable.setStatus("current")
_BdsErrorEntry_Object = MibTableRow
bdsErrorEntry = _BdsErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 12, 1)
)
bdsErrorEntry.setIndexNames(
    (1, "INVIDI-MIB", "bdsErrorTime"),
)
if mibBuilder.loadTexts:
    bdsErrorEntry.setStatus("current")


class _BdsErrorTime_Type(DisplayString):
    """Custom type bdsErrorTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_BdsErrorTime_Type.__name__ = "DisplayString"
_BdsErrorTime_Object = MibTableColumn
bdsErrorTime = _BdsErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 12, 1, 1),
    _BdsErrorTime_Type()
)
bdsErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdsErrorTime.setStatus("current")
_BdsErrorDescription_Type = DisplayString
_BdsErrorDescription_Object = MibTableColumn
bdsErrorDescription = _BdsErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 12, 1, 2),
    _BdsErrorDescription_Type()
)
bdsErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdsErrorDescription.setStatus("current")
_SvcWithNoUsableInsStreamsTable_Object = MibTable
svcWithNoUsableInsStreamsTable = _SvcWithNoUsableInsStreamsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13)
)
if mibBuilder.loadTexts:
    svcWithNoUsableInsStreamsTable.setStatus("current")
_SvcWithNoUsableInsStreamsEntry_Object = MibTableRow
svcWithNoUsableInsStreamsEntry = _SvcWithNoUsableInsStreamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13, 1)
)
svcWithNoUsableInsStreamsEntry.setIndexNames(
    (1, "INVIDI-MIB", "noUsableInsStreamsSvcID"),
)
if mibBuilder.loadTexts:
    svcWithNoUsableInsStreamsEntry.setStatus("current")
_NoUsableInsStreamsSvcID_Type = ObjectIdentifier
_NoUsableInsStreamsSvcID_Object = MibTableColumn
noUsableInsStreamsSvcID = _NoUsableInsStreamsSvcID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13, 1, 1),
    _NoUsableInsStreamsSvcID_Type()
)
noUsableInsStreamsSvcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noUsableInsStreamsSvcID.setStatus("current")
_NoUsableInsStreamsSvcName_Type = DisplayString
_NoUsableInsStreamsSvcName_Object = MibTableColumn
noUsableInsStreamsSvcName = _NoUsableInsStreamsSvcName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13, 1, 2),
    _NoUsableInsStreamsSvcName_Type()
)
noUsableInsStreamsSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noUsableInsStreamsSvcName.setStatus("current")
_NoUsableInsStreamsSvcZone_Type = DisplayString
_NoUsableInsStreamsSvcZone_Object = MibTableColumn
noUsableInsStreamsSvcZone = _NoUsableInsStreamsSvcZone_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13, 1, 3),
    _NoUsableInsStreamsSvcZone_Type()
)
noUsableInsStreamsSvcZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noUsableInsStreamsSvcZone.setStatus("current")
_NoUsableInsStreamsAvPID_Type = Integer32
_NoUsableInsStreamsAvPID_Object = MibTableColumn
noUsableInsStreamsAvPID = _NoUsableInsStreamsAvPID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13, 1, 4),
    _NoUsableInsStreamsAvPID_Type()
)
noUsableInsStreamsAvPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noUsableInsStreamsAvPID.setStatus("current")
_NoUsableInsStreamsAvPName_Type = DisplayString
_NoUsableInsStreamsAvPName_Object = MibTableColumn
noUsableInsStreamsAvPName = _NoUsableInsStreamsAvPName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13, 1, 5),
    _NoUsableInsStreamsAvPName_Type()
)
noUsableInsStreamsAvPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noUsableInsStreamsAvPName.setStatus("current")
_NoUsableInsStreamsAVPCatID_Type = Integer32
_NoUsableInsStreamsAVPCatID_Object = MibTableColumn
noUsableInsStreamsAVPCatID = _NoUsableInsStreamsAVPCatID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13, 1, 6),
    _NoUsableInsStreamsAVPCatID_Type()
)
noUsableInsStreamsAVPCatID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noUsableInsStreamsAVPCatID.setStatus("current")
_NoUsableInsStreamsAVPCatName_Type = DisplayString
_NoUsableInsStreamsAVPCatName_Object = MibTableColumn
noUsableInsStreamsAVPCatName = _NoUsableInsStreamsAVPCatName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 13, 1, 7),
    _NoUsableInsStreamsAVPCatName_Type()
)
noUsableInsStreamsAVPCatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noUsableInsStreamsAVPCatName.setStatus("current")
_AvProfCatMapTable_Object = MibTable
avProfCatMapTable = _AvProfCatMapTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 14)
)
if mibBuilder.loadTexts:
    avProfCatMapTable.setStatus("current")
_AvProfCatMapEntry_Object = MibTableRow
avProfCatMapEntry = _AvProfCatMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 14, 1)
)
avProfCatMapEntry.setIndexNames(
    (1, "INVIDI-MIB", "avProfCatID"),
)
if mibBuilder.loadTexts:
    avProfCatMapEntry.setStatus("current")
_AvProfCatID_Type = ObjectIdentifier
_AvProfCatID_Object = MibTableColumn
avProfCatID = _AvProfCatID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 14, 1, 1),
    _AvProfCatID_Type()
)
avProfCatID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avProfCatID.setStatus("current")
_AvProfCatName_Type = DisplayString
_AvProfCatName_Object = MibTableColumn
avProfCatName = _AvProfCatName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 14, 1, 2),
    _AvProfCatName_Type()
)
avProfCatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avProfCatName.setStatus("current")
_AvProfCatFiller_Type = DisplayString
_AvProfCatFiller_Object = MibTableColumn
avProfCatFiller = _AvProfCatFiller_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 14, 1, 3),
    _AvProfCatFiller_Type()
)
avProfCatFiller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avProfCatFiller.setStatus("current")
_AvProfCatAVProfID_Type = Integer32
_AvProfCatAVProfID_Object = MibTableColumn
avProfCatAVProfID = _AvProfCatAVProfID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 14, 1, 4),
    _AvProfCatAVProfID_Type()
)
avProfCatAVProfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avProfCatAVProfID.setStatus("current")
_AvProfCatAVProfName_Type = DisplayString
_AvProfCatAVProfName_Object = MibTableColumn
avProfCatAVProfName = _AvProfCatAVProfName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 14, 1, 5),
    _AvProfCatAVProfName_Type()
)
avProfCatAVProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avProfCatAVProfName.setStatus("current")
_AvProfCatStreams_Type = Integer32
_AvProfCatStreams_Object = MibTableColumn
avProfCatStreams = _AvProfCatStreams_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 4, 14, 1, 6),
    _AvProfCatStreams_Type()
)
avProfCatStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avProfCatStreams.setStatus("current")
_OutBandDataMonitor_ObjectIdentity = ObjectIdentity
outBandDataMonitor = _OutBandDataMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5)
)
if mibBuilder.loadTexts:
    outBandDataMonitor.setStatus("current")
_CarouselMonitorTable_Object = MibTable
carouselMonitorTable = _CarouselMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    carouselMonitorTable.setStatus("current")
_CarouselMonitorEntry_Object = MibTableRow
carouselMonitorEntry = _CarouselMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 1, 1)
)
carouselMonitorEntry.setIndexNames(
    (1, "INVIDI-MIB", "messageType"),
)
if mibBuilder.loadTexts:
    carouselMonitorEntry.setStatus("current")


class _MessageType_Type(DisplayString):
    """Custom type messageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_MessageType_Type.__name__ = "DisplayString"
_MessageType_Object = MibTableColumn
messageType = _MessageType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 1, 1, 1),
    _MessageType_Type()
)
messageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageType.setStatus("current")
_BytesTransfered_Type = Counter32
_BytesTransfered_Object = MibTableColumn
bytesTransfered = _BytesTransfered_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 1, 1, 2),
    _BytesTransfered_Type()
)
bytesTransfered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesTransfered.setStatus("current")
_Messages_Type = Integer32
_Messages_Object = MibTableColumn
messages = _Messages_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 1, 1, 3),
    _Messages_Type()
)
messages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messages.setStatus("current")
_StartTime_Type = DisplayString
_StartTime_Object = MibTableColumn
startTime = _StartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 1, 1, 4),
    _StartTime_Type()
)
startTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startTime.setStatus("current")
_AverageRate_Type = DisplayString
_AverageRate_Object = MibTableColumn
averageRate = _AverageRate_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 1, 1, 5),
    _AverageRate_Type()
)
averageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageRate.setStatus("current")
_LastMessageTimeAndSize_Type = DisplayString
_LastMessageTimeAndSize_Object = MibTableColumn
lastMessageTimeAndSize = _LastMessageTimeAndSize_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 1, 1, 6),
    _LastMessageTimeAndSize_Type()
)
lastMessageTimeAndSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastMessageTimeAndSize.setStatus("current")
_FileDropStatusTable_Object = MibTable
fileDropStatusTable = _FileDropStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    fileDropStatusTable.setStatus("current")
_FileDropStatusEntry_Object = MibTableRow
fileDropStatusEntry = _FileDropStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1)
)
fileDropStatusEntry.setIndexNames(
    (1, "INVIDI-MIB", "fileType"),
)
if mibBuilder.loadTexts:
    fileDropStatusEntry.setStatus("current")


class _FileType_Type(DisplayString):
    """Custom type fileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_FileType_Type.__name__ = "DisplayString"
_FileType_Object = MibTableColumn
fileType = _FileType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 1),
    _FileType_Type()
)
fileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileType.setStatus("current")
_FileDropSegment_Type = Integer32
_FileDropSegment_Object = MibTableColumn
fileDropSegment = _FileDropSegment_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 2),
    _FileDropSegment_Type()
)
fileDropSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileDropSegment.setStatus("current")
_FileDropCreationTime_Type = DisplayString
_FileDropCreationTime_Object = MibTableColumn
fileDropCreationTime = _FileDropCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 3),
    _FileDropCreationTime_Type()
)
fileDropCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileDropCreationTime.setStatus("current")
_TransferStatus_Type = DisplayString
_TransferStatus_Object = MibTableColumn
transferStatus = _TransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 4),
    _TransferStatus_Type()
)
transferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatus.setStatus("current")
_TransferSuccesses_Type = Integer32
_TransferSuccesses_Object = MibTableColumn
transferSuccesses = _TransferSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 5),
    _TransferSuccesses_Type()
)
transferSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSuccesses.setStatus("current")
_TransferSuccessTime_Type = DisplayString
_TransferSuccessTime_Object = MibTableColumn
transferSuccessTime = _TransferSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 6),
    _TransferSuccessTime_Type()
)
transferSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSuccessTime.setStatus("current")
_TransferFailures_Type = Integer32
_TransferFailures_Object = MibTableColumn
transferFailures = _TransferFailures_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 7),
    _TransferFailures_Type()
)
transferFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferFailures.setStatus("current")
_TransferFailTime_Type = DisplayString
_TransferFailTime_Object = MibTableColumn
transferFailTime = _TransferFailTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 8),
    _TransferFailTime_Type()
)
transferFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferFailTime.setStatus("current")
_TransferError_Type = DisplayString
_TransferError_Object = MibTableColumn
transferError = _TransferError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 2, 1, 9),
    _TransferError_Type()
)
transferError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferError.setStatus("current")
_DssStatusStatisticsTable_Object = MibTable
dssStatusStatisticsTable = _DssStatusStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    dssStatusStatisticsTable.setStatus("current")
_DssStatusStatisticsEntry_Object = MibTableRow
dssStatusStatisticsEntry = _DssStatusStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 3, 1)
)
dssStatusStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "dssStatus"),
)
if mibBuilder.loadTexts:
    dssStatusStatisticsEntry.setStatus("current")


class _DssStatus_Type(DisplayString):
    """Custom type dssStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_DssStatus_Type.__name__ = "DisplayString"
_DssStatus_Object = MibTableColumn
dssStatus = _DssStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 3, 1, 1),
    _DssStatus_Type()
)
dssStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dssStatus.setStatus("current")
_TargetUpdateStatusTable_Object = MibTable
targetUpdateStatusTable = _TargetUpdateStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    targetUpdateStatusTable.setStatus("current")
_TargetUpdateStatusEntry_Object = MibTableRow
targetUpdateStatusEntry = _TargetUpdateStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4, 1)
)
targetUpdateStatusEntry.setIndexNames(
    (1, "INVIDI-MIB", "targetUpdateName"),
)
if mibBuilder.loadTexts:
    targetUpdateStatusEntry.setStatus("current")


class _TargetUpdateName_Type(DisplayString):
    """Custom type targetUpdateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_TargetUpdateName_Type.__name__ = "DisplayString"
_TargetUpdateName_Object = MibTableColumn
targetUpdateName = _TargetUpdateName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4, 1, 1),
    _TargetUpdateName_Type()
)
targetUpdateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetUpdateName.setStatus("current")
_TargetUpdateStatus_Type = DisplayString
_TargetUpdateStatus_Object = MibTableColumn
targetUpdateStatus = _TargetUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4, 1, 2),
    _TargetUpdateStatus_Type()
)
targetUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetUpdateStatus.setStatus("current")
_TargetUpdateSuccesses_Type = Integer32
_TargetUpdateSuccesses_Object = MibTableColumn
targetUpdateSuccesses = _TargetUpdateSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4, 1, 3),
    _TargetUpdateSuccesses_Type()
)
targetUpdateSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetUpdateSuccesses.setStatus("current")
_TargetUpdateSuccessTime_Type = DisplayString
_TargetUpdateSuccessTime_Object = MibTableColumn
targetUpdateSuccessTime = _TargetUpdateSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4, 1, 4),
    _TargetUpdateSuccessTime_Type()
)
targetUpdateSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetUpdateSuccessTime.setStatus("current")
_TargetUpdateFailures_Type = Integer32
_TargetUpdateFailures_Object = MibTableColumn
targetUpdateFailures = _TargetUpdateFailures_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4, 1, 5),
    _TargetUpdateFailures_Type()
)
targetUpdateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetUpdateFailures.setStatus("current")
_TargetUpdateFailTime_Type = DisplayString
_TargetUpdateFailTime_Object = MibTableColumn
targetUpdateFailTime = _TargetUpdateFailTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4, 1, 6),
    _TargetUpdateFailTime_Type()
)
targetUpdateFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetUpdateFailTime.setStatus("current")
_TargetUpdateError_Type = DisplayString
_TargetUpdateError_Object = MibTableColumn
targetUpdateError = _TargetUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 4, 1, 7),
    _TargetUpdateError_Type()
)
targetUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetUpdateError.setStatus("current")
_AdoAloCreationStatusTable_Object = MibTable
adoAloCreationStatusTable = _AdoAloCreationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    adoAloCreationStatusTable.setStatus("current")
_AdoAloCreationStatusEntry_Object = MibTableRow
adoAloCreationStatusEntry = _AdoAloCreationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5, 1)
)
adoAloCreationStatusEntry.setIndexNames(
    (1, "INVIDI-MIB", "adoAloCreationName"),
)
if mibBuilder.loadTexts:
    adoAloCreationStatusEntry.setStatus("current")


class _AdoAloCreationName_Type(DisplayString):
    """Custom type adoAloCreationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_AdoAloCreationName_Type.__name__ = "DisplayString"
_AdoAloCreationName_Object = MibTableColumn
adoAloCreationName = _AdoAloCreationName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5, 1, 1),
    _AdoAloCreationName_Type()
)
adoAloCreationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adoAloCreationName.setStatus("current")
_AdoAloCreationStatus_Type = DisplayString
_AdoAloCreationStatus_Object = MibTableColumn
adoAloCreationStatus = _AdoAloCreationStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5, 1, 2),
    _AdoAloCreationStatus_Type()
)
adoAloCreationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adoAloCreationStatus.setStatus("current")
_AdoAloCreationSuccesses_Type = Integer32
_AdoAloCreationSuccesses_Object = MibTableColumn
adoAloCreationSuccesses = _AdoAloCreationSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5, 1, 3),
    _AdoAloCreationSuccesses_Type()
)
adoAloCreationSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adoAloCreationSuccesses.setStatus("current")
_AdoAloCreationSuccessTime_Type = DisplayString
_AdoAloCreationSuccessTime_Object = MibTableColumn
adoAloCreationSuccessTime = _AdoAloCreationSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5, 1, 4),
    _AdoAloCreationSuccessTime_Type()
)
adoAloCreationSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adoAloCreationSuccessTime.setStatus("current")
_AdoAloCreationFailures_Type = Integer32
_AdoAloCreationFailures_Object = MibTableColumn
adoAloCreationFailures = _AdoAloCreationFailures_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5, 1, 5),
    _AdoAloCreationFailures_Type()
)
adoAloCreationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adoAloCreationFailures.setStatus("current")
_AdoAloCreationFailTime_Type = DisplayString
_AdoAloCreationFailTime_Object = MibTableColumn
adoAloCreationFailTime = _AdoAloCreationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5, 1, 6),
    _AdoAloCreationFailTime_Type()
)
adoAloCreationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adoAloCreationFailTime.setStatus("current")
_AdoAloCreationError_Type = DisplayString
_AdoAloCreationError_Object = MibTableColumn
adoAloCreationError = _AdoAloCreationError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 5, 1, 7),
    _AdoAloCreationError_Type()
)
adoAloCreationError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adoAloCreationError.setStatus("current")
_PrioritizerAssetPushStatusTable_Object = MibTable
prioritizerAssetPushStatusTable = _PrioritizerAssetPushStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    prioritizerAssetPushStatusTable.setStatus("current")
_PrioritizerAssetPushStatusEntry_Object = MibTableRow
prioritizerAssetPushStatusEntry = _PrioritizerAssetPushStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6, 1)
)
prioritizerAssetPushStatusEntry.setIndexNames(
    (1, "INVIDI-MIB", "prioritizerAssetPushName"),
)
if mibBuilder.loadTexts:
    prioritizerAssetPushStatusEntry.setStatus("current")


class _PrioritizerAssetPushName_Type(DisplayString):
    """Custom type prioritizerAssetPushName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_PrioritizerAssetPushName_Type.__name__ = "DisplayString"
_PrioritizerAssetPushName_Object = MibTableColumn
prioritizerAssetPushName = _PrioritizerAssetPushName_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6, 1, 1),
    _PrioritizerAssetPushName_Type()
)
prioritizerAssetPushName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioritizerAssetPushName.setStatus("current")
_PrioritizerAssetPushStatus_Type = DisplayString
_PrioritizerAssetPushStatus_Object = MibTableColumn
prioritizerAssetPushStatus = _PrioritizerAssetPushStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6, 1, 2),
    _PrioritizerAssetPushStatus_Type()
)
prioritizerAssetPushStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioritizerAssetPushStatus.setStatus("current")
_PrioritizerAssetPushSuccesses_Type = Integer32
_PrioritizerAssetPushSuccesses_Object = MibTableColumn
prioritizerAssetPushSuccesses = _PrioritizerAssetPushSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6, 1, 3),
    _PrioritizerAssetPushSuccesses_Type()
)
prioritizerAssetPushSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioritizerAssetPushSuccesses.setStatus("current")
_PrioritizerAssetPushSuccessTime_Type = DisplayString
_PrioritizerAssetPushSuccessTime_Object = MibTableColumn
prioritizerAssetPushSuccessTime = _PrioritizerAssetPushSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6, 1, 4),
    _PrioritizerAssetPushSuccessTime_Type()
)
prioritizerAssetPushSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioritizerAssetPushSuccessTime.setStatus("current")
_PrioritizerAssetPushFailures_Type = Integer32
_PrioritizerAssetPushFailures_Object = MibTableColumn
prioritizerAssetPushFailures = _PrioritizerAssetPushFailures_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6, 1, 5),
    _PrioritizerAssetPushFailures_Type()
)
prioritizerAssetPushFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioritizerAssetPushFailures.setStatus("current")
_PrioritizerAssetPushFailTime_Type = DisplayString
_PrioritizerAssetPushFailTime_Object = MibTableColumn
prioritizerAssetPushFailTime = _PrioritizerAssetPushFailTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6, 1, 6),
    _PrioritizerAssetPushFailTime_Type()
)
prioritizerAssetPushFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioritizerAssetPushFailTime.setStatus("current")
_PrioritizerAssetPushError_Type = DisplayString
_PrioritizerAssetPushError_Object = MibTableColumn
prioritizerAssetPushError = _PrioritizerAssetPushError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 6, 1, 7),
    _PrioritizerAssetPushError_Type()
)
prioritizerAssetPushError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioritizerAssetPushError.setStatus("current")
_DssErrorTable_Object = MibTable
dssErrorTable = _DssErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    dssErrorTable.setStatus("current")
_DssErrorEntry_Object = MibTableRow
dssErrorEntry = _DssErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 7, 1)
)
dssErrorEntry.setIndexNames(
    (1, "INVIDI-MIB", "dssErrorTime"),
)
if mibBuilder.loadTexts:
    dssErrorEntry.setStatus("current")


class _DssErrorTime_Type(DisplayString):
    """Custom type dssErrorTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_DssErrorTime_Type.__name__ = "DisplayString"
_DssErrorTime_Object = MibTableColumn
dssErrorTime = _DssErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 7, 1, 1),
    _DssErrorTime_Type()
)
dssErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dssErrorTime.setStatus("current")
_DssErrorDescription_Type = DisplayString
_DssErrorDescription_Object = MibTableColumn
dssErrorDescription = _DssErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 5, 7, 1, 2),
    _DssErrorDescription_Type()
)
dssErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dssErrorDescription.setStatus("current")
_RcsInterface_ObjectIdentity = ObjectIdentity
rcsInterface = _RcsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rcsInterface.setStatus("current")
_ProcessingStatusStatisticsTable_Object = MibTable
processingStatusStatisticsTable = _ProcessingStatusStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    processingStatusStatisticsTable.setStatus("current")
_ProcessingStatusStatisticsEntry_Object = MibTableRow
processingStatusStatisticsEntry = _ProcessingStatusStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 1, 1)
)
processingStatusStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "eventTime"),
)
if mibBuilder.loadTexts:
    processingStatusStatisticsEntry.setStatus("current")


class _EventTime_Type(DisplayString):
    """Custom type eventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_EventTime_Type.__name__ = "DisplayString"
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 1, 1, 1),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_EventDescription_Type = DisplayString
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 1, 1, 2),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_InteractiveFromTable_Object = MibTable
interactiveFromTable = _InteractiveFromTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    interactiveFromTable.setStatus("current")
_InteractiveFromStatisticsEntry_Object = MibTableRow
interactiveFromStatisticsEntry = _InteractiveFromStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 2, 1)
)
interactiveFromStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "fromMessageType"),
)
if mibBuilder.loadTexts:
    interactiveFromStatisticsEntry.setStatus("current")


class _FromMessageType_Type(DisplayString):
    """Custom type fromMessageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_FromMessageType_Type.__name__ = "DisplayString"
_FromMessageType_Object = MibTableColumn
fromMessageType = _FromMessageType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 2, 1, 1),
    _FromMessageType_Type()
)
fromMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fromMessageType.setStatus("current")
_FromBytesTransfered_Type = DisplayString
_FromBytesTransfered_Object = MibTableColumn
fromBytesTransfered = _FromBytesTransfered_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 2, 1, 2),
    _FromBytesTransfered_Type()
)
fromBytesTransfered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fromBytesTransfered.setStatus("current")
_FromMessages_Type = Integer32
_FromMessages_Object = MibTableColumn
fromMessages = _FromMessages_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 2, 1, 3),
    _FromMessages_Type()
)
fromMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fromMessages.setStatus("current")
_FromStartTime_Type = DisplayString
_FromStartTime_Object = MibTableColumn
fromStartTime = _FromStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 2, 1, 4),
    _FromStartTime_Type()
)
fromStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fromStartTime.setStatus("current")
_FromAverageRate_Type = DisplayString
_FromAverageRate_Object = MibTableColumn
fromAverageRate = _FromAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 2, 1, 5),
    _FromAverageRate_Type()
)
fromAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fromAverageRate.setStatus("current")
_FromLastMessageTimeAndSize_Type = DisplayString
_FromLastMessageTimeAndSize_Object = MibTableColumn
fromLastMessageTimeAndSize = _FromLastMessageTimeAndSize_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 2, 1, 6),
    _FromLastMessageTimeAndSize_Type()
)
fromLastMessageTimeAndSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fromLastMessageTimeAndSize.setStatus("current")
_InteractiveToTable_Object = MibTable
interactiveToTable = _InteractiveToTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    interactiveToTable.setStatus("current")
_InteractiveToStatisticsEntry_Object = MibTableRow
interactiveToStatisticsEntry = _InteractiveToStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 3, 1)
)
interactiveToStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "toMessageType"),
)
if mibBuilder.loadTexts:
    interactiveToStatisticsEntry.setStatus("current")


class _ToMessageType_Type(DisplayString):
    """Custom type toMessageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_ToMessageType_Type.__name__ = "DisplayString"
_ToMessageType_Object = MibTableColumn
toMessageType = _ToMessageType_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 3, 1, 1),
    _ToMessageType_Type()
)
toMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toMessageType.setStatus("current")
_ToBytesTransfered_Type = Counter32
_ToBytesTransfered_Object = MibTableColumn
toBytesTransfered = _ToBytesTransfered_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 3, 1, 2),
    _ToBytesTransfered_Type()
)
toBytesTransfered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toBytesTransfered.setStatus("current")
_ToMessages_Type = Integer32
_ToMessages_Object = MibTableColumn
toMessages = _ToMessages_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 3, 1, 3),
    _ToMessages_Type()
)
toMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toMessages.setStatus("current")
_ToStartTime_Type = DisplayString
_ToStartTime_Object = MibTableColumn
toStartTime = _ToStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 3, 1, 4),
    _ToStartTime_Type()
)
toStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toStartTime.setStatus("current")
_ToAverageRate_Type = DisplayString
_ToAverageRate_Object = MibTableColumn
toAverageRate = _ToAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 3, 1, 5),
    _ToAverageRate_Type()
)
toAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toAverageRate.setStatus("current")
_ToLastMessageTimeAndSize_Type = DisplayString
_ToLastMessageTimeAndSize_Object = MibTableColumn
toLastMessageTimeAndSize = _ToLastMessageTimeAndSize_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 3, 1, 6),
    _ToLastMessageTimeAndSize_Type()
)
toLastMessageTimeAndSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toLastMessageTimeAndSize.setStatus("current")
_StbReturnTable_Object = MibTable
stbReturnTable = _StbReturnTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    stbReturnTable.setStatus("current")
_StbReturnEntry_Object = MibTableRow
stbReturnEntry = _StbReturnEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 4, 1)
)
stbReturnEntry.setIndexNames(
    (1, "INVIDI-MIB", "numberOfConnectRetries"),
)
if mibBuilder.loadTexts:
    stbReturnEntry.setStatus("current")
_NumberOfConnectRetries_Type = ObjectIdentifier
_NumberOfConnectRetries_Object = MibTableColumn
numberOfConnectRetries = _NumberOfConnectRetries_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 4, 1, 1),
    _NumberOfConnectRetries_Type()
)
numberOfConnectRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfConnectRetries.setStatus("current")
_NumberOfResends_Type = Integer32
_NumberOfResends_Object = MibTableColumn
numberOfResends = _NumberOfResends_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 4, 1, 2),
    _NumberOfResends_Type()
)
numberOfResends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfResends.setStatus("current")
_NumberOfV1AliveMessages_Type = Integer32
_NumberOfV1AliveMessages_Object = MibTableColumn
numberOfV1AliveMessages = _NumberOfV1AliveMessages_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 4, 1, 3),
    _NumberOfV1AliveMessages_Type()
)
numberOfV1AliveMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfV1AliveMessages.setStatus("current")
_PercentageOfV1AliveMessages_Type = Integer32
_PercentageOfV1AliveMessages_Object = MibTableColumn
percentageOfV1AliveMessages = _PercentageOfV1AliveMessages_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 4, 1, 4),
    _PercentageOfV1AliveMessages_Type()
)
percentageOfV1AliveMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    percentageOfV1AliveMessages.setStatus("current")
_SetTopStatisticsTable_Object = MibTable
setTopStatisticsTable = _SetTopStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    setTopStatisticsTable.setStatus("current")
_SetTopStatisticsEntry_Object = MibTableRow
setTopStatisticsEntry = _SetTopStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5, 1)
)
setTopStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "boxID"),
)
if mibBuilder.loadTexts:
    setTopStatisticsEntry.setStatus("current")


class _BoxID_Type(DisplayString):
    """Custom type boxID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_BoxID_Type.__name__ = "DisplayString"
_BoxID_Object = MibTableColumn
boxID = _BoxID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5, 1, 1),
    _BoxID_Type()
)
boxID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxID.setStatus("current")
_MessagesCount_Type = Integer32
_MessagesCount_Object = MibTableColumn
messagesCount = _MessagesCount_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5, 1, 2),
    _MessagesCount_Type()
)
messagesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesCount.setStatus("current")
_ExposedDateTime_Type = DisplayString
_ExposedDateTime_Object = MibTableColumn
exposedDateTime = _ExposedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5, 1, 3),
    _ExposedDateTime_Type()
)
exposedDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exposedDateTime.setStatus("current")
_DateRequestAndTime_Type = DisplayString
_DateRequestAndTime_Object = MibTableColumn
dateRequestAndTime = _DateRequestAndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5, 1, 4),
    _DateRequestAndTime_Type()
)
dateRequestAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateRequestAndTime.setStatus("current")
_LastAdPlayed_Type = DisplayString
_LastAdPlayed_Object = MibTableColumn
lastAdPlayed = _LastAdPlayed_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5, 1, 5),
    _LastAdPlayed_Type()
)
lastAdPlayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastAdPlayed.setStatus("current")
_ReturnStats_Type = DisplayString
_ReturnStats_Object = MibTableColumn
returnStats = _ReturnStats_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5, 1, 6),
    _ReturnStats_Type()
)
returnStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnStats.setStatus("current")
_LastMessage_Type = DisplayString
_LastMessage_Object = MibTableColumn
lastMessage = _LastMessage_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 5, 1, 7),
    _LastMessage_Type()
)
lastMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastMessage.setStatus("current")
_UnknownSetTopsTable_Object = MibTable
unknownSetTopsTable = _UnknownSetTopsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    unknownSetTopsTable.setStatus("current")
_UnknownSetTopsEntry_Object = MibTableRow
unknownSetTopsEntry = _UnknownSetTopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 6, 1)
)
unknownSetTopsEntry.setIndexNames(
    (1, "INVIDI-MIB", "boxIDUnknown"),
)
if mibBuilder.loadTexts:
    unknownSetTopsEntry.setStatus("current")


class _BoxIDUnknown_Type(DisplayString):
    """Custom type boxIDUnknown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_BoxIDUnknown_Type.__name__ = "DisplayString"
_BoxIDUnknown_Object = MibTableColumn
boxIDUnknown = _BoxIDUnknown_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 6, 1, 1),
    _BoxIDUnknown_Type()
)
boxIDUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxIDUnknown.setStatus("current")
_RequestTime_Type = DisplayString
_RequestTime_Object = MibTableColumn
requestTime = _RequestTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 6, 1, 2),
    _RequestTime_Type()
)
requestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requestTime.setStatus("current")
_ClickStatisticsTable_Object = MibTable
clickStatisticsTable = _ClickStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    clickStatisticsTable.setStatus("current")
_ClickStatisticsEntry_Object = MibTableRow
clickStatisticsEntry = _ClickStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 7, 1)
)
clickStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "clickStatus"),
)
if mibBuilder.loadTexts:
    clickStatisticsEntry.setStatus("current")


class _ClickStatus_Type(DisplayString):
    """Custom type clickStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_ClickStatus_Type.__name__ = "DisplayString"
_ClickStatus_Object = MibTableColumn
clickStatus = _ClickStatus_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 7, 1, 1),
    _ClickStatus_Type()
)
clickStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clickStatus.setStatus("current")
_ClickSuccesses_Type = Integer32
_ClickSuccesses_Object = MibTableColumn
clickSuccesses = _ClickSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 7, 1, 2),
    _ClickSuccesses_Type()
)
clickSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clickSuccesses.setStatus("current")
_ClickLastSuccessTime_Type = DisplayString
_ClickLastSuccessTime_Object = MibTableColumn
clickLastSuccessTime = _ClickLastSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 7, 1, 3),
    _ClickLastSuccessTime_Type()
)
clickLastSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clickLastSuccessTime.setStatus("current")
_ClickFailures_Type = Integer32
_ClickFailures_Object = MibTableColumn
clickFailures = _ClickFailures_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 7, 1, 4),
    _ClickFailures_Type()
)
clickFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clickFailures.setStatus("current")
_ClickLastFailureTime_Type = DisplayString
_ClickLastFailureTime_Object = MibTableColumn
clickLastFailureTime = _ClickLastFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 7, 1, 5),
    _ClickLastFailureTime_Type()
)
clickLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clickLastFailureTime.setStatus("current")
_ClickLastError_Type = DisplayString
_ClickLastError_Object = MibTableColumn
clickLastError = _ClickLastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 7, 1, 6),
    _ClickLastError_Type()
)
clickLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clickLastError.setStatus("current")
_RawAdnFileCreationTable_Object = MibTable
rawAdnFileCreationTable = _RawAdnFileCreationTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8)
)
if mibBuilder.loadTexts:
    rawAdnFileCreationTable.setStatus("current")
_RawAdnFileCreationEntry_Object = MibTableRow
rawAdnFileCreationEntry = _RawAdnFileCreationEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8, 1)
)
rawAdnFileCreationEntry.setIndexNames(
    (1, "INVIDI-MIB", "rawAdnFileCreationFileshare"),
)
if mibBuilder.loadTexts:
    rawAdnFileCreationEntry.setStatus("current")


class _RawAdnFileCreationFileshare_Type(DisplayString):
    """Custom type rawAdnFileCreationFileshare based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RawAdnFileCreationFileshare_Type.__name__ = "DisplayString"
_RawAdnFileCreationFileshare_Object = MibTableColumn
rawAdnFileCreationFileshare = _RawAdnFileCreationFileshare_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8, 1, 1),
    _RawAdnFileCreationFileshare_Type()
)
rawAdnFileCreationFileshare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileCreationFileshare.setStatus("current")
_RawAdnFileCreationRetrieval_Type = Integer32
_RawAdnFileCreationRetrieval_Object = MibTableColumn
rawAdnFileCreationRetrieval = _RawAdnFileCreationRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8, 1, 2),
    _RawAdnFileCreationRetrieval_Type()
)
rawAdnFileCreationRetrieval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileCreationRetrieval.setStatus("current")
_RawAdnFileCreationSuccess_Type = Integer32
_RawAdnFileCreationSuccess_Object = MibTableColumn
rawAdnFileCreationSuccess = _RawAdnFileCreationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8, 1, 3),
    _RawAdnFileCreationSuccess_Type()
)
rawAdnFileCreationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileCreationSuccess.setStatus("current")
_RawAdnFileCreationLastSuccess_Type = DisplayString
_RawAdnFileCreationLastSuccess_Object = MibTableColumn
rawAdnFileCreationLastSuccess = _RawAdnFileCreationLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8, 1, 4),
    _RawAdnFileCreationLastSuccess_Type()
)
rawAdnFileCreationLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileCreationLastSuccess.setStatus("current")
_RawAdnFileCreationFailure_Type = Integer32
_RawAdnFileCreationFailure_Object = MibTableColumn
rawAdnFileCreationFailure = _RawAdnFileCreationFailure_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8, 1, 5),
    _RawAdnFileCreationFailure_Type()
)
rawAdnFileCreationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileCreationFailure.setStatus("current")
_RawAdnFileCreationLastFailure_Type = DisplayString
_RawAdnFileCreationLastFailure_Object = MibTableColumn
rawAdnFileCreationLastFailure = _RawAdnFileCreationLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8, 1, 6),
    _RawAdnFileCreationLastFailure_Type()
)
rawAdnFileCreationLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileCreationLastFailure.setStatus("current")
_RawAdnFileCreationLastError_Type = DisplayString
_RawAdnFileCreationLastError_Object = MibTableColumn
rawAdnFileCreationLastError = _RawAdnFileCreationLastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 8, 1, 7),
    _RawAdnFileCreationLastError_Type()
)
rawAdnFileCreationLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileCreationLastError.setStatus("current")
_RawAdnFileTransferTable_Object = MibTable
rawAdnFileTransferTable = _RawAdnFileTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9)
)
if mibBuilder.loadTexts:
    rawAdnFileTransferTable.setStatus("current")
_RawAdnFileTransferEntry_Object = MibTableRow
rawAdnFileTransferEntry = _RawAdnFileTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9, 1)
)
rawAdnFileTransferEntry.setIndexNames(
    (1, "INVIDI-MIB", "rawAdnFileTransferFileshare"),
)
if mibBuilder.loadTexts:
    rawAdnFileTransferEntry.setStatus("current")


class _RawAdnFileTransferFileshare_Type(DisplayString):
    """Custom type rawAdnFileTransferFileshare based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RawAdnFileTransferFileshare_Type.__name__ = "DisplayString"
_RawAdnFileTransferFileshare_Object = MibTableColumn
rawAdnFileTransferFileshare = _RawAdnFileTransferFileshare_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9, 1, 1),
    _RawAdnFileTransferFileshare_Type()
)
rawAdnFileTransferFileshare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileTransferFileshare.setStatus("current")
_RawAdnFileTransferRetrieval_Type = Integer32
_RawAdnFileTransferRetrieval_Object = MibTableColumn
rawAdnFileTransferRetrieval = _RawAdnFileTransferRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9, 1, 2),
    _RawAdnFileTransferRetrieval_Type()
)
rawAdnFileTransferRetrieval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileTransferRetrieval.setStatus("current")
_RawAdnFileTransferSuccess_Type = Integer32
_RawAdnFileTransferSuccess_Object = MibTableColumn
rawAdnFileTransferSuccess = _RawAdnFileTransferSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9, 1, 3),
    _RawAdnFileTransferSuccess_Type()
)
rawAdnFileTransferSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileTransferSuccess.setStatus("current")
_RawAdnFileTransferLastSuccess_Type = DisplayString
_RawAdnFileTransferLastSuccess_Object = MibTableColumn
rawAdnFileTransferLastSuccess = _RawAdnFileTransferLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9, 1, 4),
    _RawAdnFileTransferLastSuccess_Type()
)
rawAdnFileTransferLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileTransferLastSuccess.setStatus("current")
_RawAdnFileTransferFailure_Type = Integer32
_RawAdnFileTransferFailure_Object = MibTableColumn
rawAdnFileTransferFailure = _RawAdnFileTransferFailure_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9, 1, 5),
    _RawAdnFileTransferFailure_Type()
)
rawAdnFileTransferFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileTransferFailure.setStatus("current")
_RawAdnFileTransferLastFailure_Type = DisplayString
_RawAdnFileTransferLastFailure_Object = MibTableColumn
rawAdnFileTransferLastFailure = _RawAdnFileTransferLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9, 1, 6),
    _RawAdnFileTransferLastFailure_Type()
)
rawAdnFileTransferLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileTransferLastFailure.setStatus("current")
_RawAdnFileTransferLastError_Type = DisplayString
_RawAdnFileTransferLastError_Object = MibTableColumn
rawAdnFileTransferLastError = _RawAdnFileTransferLastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 9, 1, 7),
    _RawAdnFileTransferLastError_Type()
)
rawAdnFileTransferLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawAdnFileTransferLastError.setStatus("current")
_VmStatisticsTable_Object = MibTable
vmStatisticsTable = _VmStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10)
)
if mibBuilder.loadTexts:
    vmStatisticsTable.setStatus("current")
_VmStatisticsEntry_Object = MibTableRow
vmStatisticsEntry = _VmStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10, 1)
)
vmStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "vmIP"),
)
if mibBuilder.loadTexts:
    vmStatisticsEntry.setStatus("current")


class _VmIP_Type(DisplayString):
    """Custom type vmIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_VmIP_Type.__name__ = "DisplayString"
_VmIP_Object = MibTableColumn
vmIP = _VmIP_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10, 1, 1),
    _VmIP_Type()
)
vmIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIP.setStatus("current")
_VmRetrieval_Type = Integer32
_VmRetrieval_Object = MibTableColumn
vmRetrieval = _VmRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10, 1, 2),
    _VmRetrieval_Type()
)
vmRetrieval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmRetrieval.setStatus("current")
_VmSuccess_Type = Integer32
_VmSuccess_Object = MibTableColumn
vmSuccess = _VmSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10, 1, 3),
    _VmSuccess_Type()
)
vmSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmSuccess.setStatus("current")
_VmLastSuccess_Type = DisplayString
_VmLastSuccess_Object = MibTableColumn
vmLastSuccess = _VmLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10, 1, 4),
    _VmLastSuccess_Type()
)
vmLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmLastSuccess.setStatus("current")
_VmFailure_Type = Integer32
_VmFailure_Object = MibTableColumn
vmFailure = _VmFailure_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10, 1, 5),
    _VmFailure_Type()
)
vmFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmFailure.setStatus("current")
_VmLastFailure_Type = DisplayString
_VmLastFailure_Object = MibTableColumn
vmLastFailure = _VmLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10, 1, 6),
    _VmLastFailure_Type()
)
vmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmLastFailure.setStatus("current")
_VmLastError_Type = DisplayString
_VmLastError_Object = MibTableColumn
vmLastError = _VmLastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 10, 1, 7),
    _VmLastError_Type()
)
vmLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmLastError.setStatus("current")
_AmsStatisticsTable_Object = MibTable
amsStatisticsTable = _AmsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11)
)
if mibBuilder.loadTexts:
    amsStatisticsTable.setStatus("current")
_AmsStatisticsEntry_Object = MibTableRow
amsStatisticsEntry = _AmsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11, 1)
)
amsStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "amsFileshare"),
)
if mibBuilder.loadTexts:
    amsStatisticsEntry.setStatus("current")


class _AmsFileshare_Type(DisplayString):
    """Custom type amsFileshare based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_AmsFileshare_Type.__name__ = "DisplayString"
_AmsFileshare_Object = MibTableColumn
amsFileshare = _AmsFileshare_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11, 1, 1),
    _AmsFileshare_Type()
)
amsFileshare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsFileshare.setStatus("current")
_AmsRetrieval_Type = Integer32
_AmsRetrieval_Object = MibTableColumn
amsRetrieval = _AmsRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11, 1, 2),
    _AmsRetrieval_Type()
)
amsRetrieval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRetrieval.setStatus("current")
_AmsSuccess_Type = Integer32
_AmsSuccess_Object = MibTableColumn
amsSuccess = _AmsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11, 1, 3),
    _AmsSuccess_Type()
)
amsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsSuccess.setStatus("current")
_AmsLastSuccess_Type = DisplayString
_AmsLastSuccess_Object = MibTableColumn
amsLastSuccess = _AmsLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11, 1, 4),
    _AmsLastSuccess_Type()
)
amsLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLastSuccess.setStatus("current")
_AmsFailure_Type = Integer32
_AmsFailure_Object = MibTableColumn
amsFailure = _AmsFailure_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11, 1, 5),
    _AmsFailure_Type()
)
amsFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsFailure.setStatus("current")
_AmsLastFailure_Type = DisplayString
_AmsLastFailure_Object = MibTableColumn
amsLastFailure = _AmsLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11, 1, 6),
    _AmsLastFailure_Type()
)
amsLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLastFailure.setStatus("current")
_AmsLastError_Type = DisplayString
_AmsLastError_Object = MibTableColumn
amsLastError = _AmsLastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 11, 1, 7),
    _AmsLastError_Type()
)
amsLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLastError.setStatus("current")
_RcsErrorTable_Object = MibTable
rcsErrorTable = _RcsErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 12)
)
if mibBuilder.loadTexts:
    rcsErrorTable.setStatus("current")
_RcsErrorEntry_Object = MibTableRow
rcsErrorEntry = _RcsErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 12, 1)
)
rcsErrorEntry.setIndexNames(
    (1, "INVIDI-MIB", "rcsErrorTime"),
)
if mibBuilder.loadTexts:
    rcsErrorEntry.setStatus("current")


class _RcsErrorTime_Type(DisplayString):
    """Custom type rcsErrorTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_RcsErrorTime_Type.__name__ = "DisplayString"
_RcsErrorTime_Object = MibTableColumn
rcsErrorTime = _RcsErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 12, 1, 1),
    _RcsErrorTime_Type()
)
rcsErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcsErrorTime.setStatus("current")
_RcsErrorDescription_Type = DisplayString
_RcsErrorDescription_Object = MibTableColumn
rcsErrorDescription = _RcsErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 12, 1, 2),
    _RcsErrorDescription_Type()
)
rcsErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcsErrorDescription.setStatus("current")
_InboundVotesStatisticsTable_Object = MibTable
inboundVotesStatisticsTable = _InboundVotesStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 13)
)
if mibBuilder.loadTexts:
    inboundVotesStatisticsTable.setStatus("current")
_InboundVotesStatisticsEntry_Object = MibTableRow
inboundVotesStatisticsEntry = _InboundVotesStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 13, 1)
)
inboundVotesStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "inboundVotesRcsAddress"),
)
if mibBuilder.loadTexts:
    inboundVotesStatisticsEntry.setStatus("current")


class _InboundVotesRcsAddress_Type(DisplayString):
    """Custom type inboundVotesRcsAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_InboundVotesRcsAddress_Type.__name__ = "DisplayString"
_InboundVotesRcsAddress_Object = MibTableColumn
inboundVotesRcsAddress = _InboundVotesRcsAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 13, 1, 1),
    _InboundVotesRcsAddress_Type()
)
inboundVotesRcsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundVotesRcsAddress.setStatus("current")
_InboundVoteMsgReceivedCount_Type = Integer32
_InboundVoteMsgReceivedCount_Object = MibTableColumn
inboundVoteMsgReceivedCount = _InboundVoteMsgReceivedCount_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 13, 1, 2),
    _InboundVoteMsgReceivedCount_Type()
)
inboundVoteMsgReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundVoteMsgReceivedCount.setStatus("current")
_InboundVoteMsgLastRecevied_Type = DisplayString
_InboundVoteMsgLastRecevied_Object = MibTableColumn
inboundVoteMsgLastRecevied = _InboundVoteMsgLastRecevied_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 13, 1, 3),
    _InboundVoteMsgLastRecevied_Type()
)
inboundVoteMsgLastRecevied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundVoteMsgLastRecevied.setStatus("current")
_InboundVoteMsgFailureCount_Type = Integer32
_InboundVoteMsgFailureCount_Object = MibTableColumn
inboundVoteMsgFailureCount = _InboundVoteMsgFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 13, 1, 4),
    _InboundVoteMsgFailureCount_Type()
)
inboundVoteMsgFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundVoteMsgFailureCount.setStatus("current")
_InboundVoteMsgLastFailureTime_Type = DisplayString
_InboundVoteMsgLastFailureTime_Object = MibTableColumn
inboundVoteMsgLastFailureTime = _InboundVoteMsgLastFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 13, 1, 5),
    _InboundVoteMsgLastFailureTime_Type()
)
inboundVoteMsgLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundVoteMsgLastFailureTime.setStatus("current")
_InboundVotesLastError_Type = DisplayString
_InboundVotesLastError_Object = MibTableColumn
inboundVotesLastError = _InboundVotesLastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 13, 1, 6),
    _InboundVotesLastError_Type()
)
inboundVotesLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundVotesLastError.setStatus("current")
_OutboundVotesStatisticsTable_Object = MibTable
outboundVotesStatisticsTable = _OutboundVotesStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14)
)
if mibBuilder.loadTexts:
    outboundVotesStatisticsTable.setStatus("current")
_OutboundVotesStatisticsEntry_Object = MibTableRow
outboundVotesStatisticsEntry = _OutboundVotesStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1)
)
outboundVotesStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "outboundVotesBdsAddress"),
)
if mibBuilder.loadTexts:
    outboundVotesStatisticsEntry.setStatus("current")


class _OutboundVotesBdsAddress_Type(DisplayString):
    """Custom type outboundVotesBdsAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 120),
    )


_OutboundVotesBdsAddress_Type.__name__ = "DisplayString"
_OutboundVotesBdsAddress_Object = MibTableColumn
outboundVotesBdsAddress = _OutboundVotesBdsAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1, 1),
    _OutboundVotesBdsAddress_Type()
)
outboundVotesBdsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundVotesBdsAddress.setStatus("current")
_OutboundVoteMsgSentCount_Type = Integer32
_OutboundVoteMsgSentCount_Object = MibTableColumn
outboundVoteMsgSentCount = _OutboundVoteMsgSentCount_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1, 2),
    _OutboundVoteMsgSentCount_Type()
)
outboundVoteMsgSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundVoteMsgSentCount.setStatus("current")
_OutboundVoteMsgLastSent_Type = DisplayString
_OutboundVoteMsgLastSent_Object = MibTableColumn
outboundVoteMsgLastSent = _OutboundVoteMsgLastSent_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1, 3),
    _OutboundVoteMsgLastSent_Type()
)
outboundVoteMsgLastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundVoteMsgLastSent.setStatus("current")
_OutboundVoteMsgDropCount_Type = Integer32
_OutboundVoteMsgDropCount_Object = MibTableColumn
outboundVoteMsgDropCount = _OutboundVoteMsgDropCount_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1, 4),
    _OutboundVoteMsgDropCount_Type()
)
outboundVoteMsgDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundVoteMsgDropCount.setStatus("current")
_OutboundVoteMsgLastDrop_Type = DisplayString
_OutboundVoteMsgLastDrop_Object = MibTableColumn
outboundVoteMsgLastDrop = _OutboundVoteMsgLastDrop_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1, 5),
    _OutboundVoteMsgLastDrop_Type()
)
outboundVoteMsgLastDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundVoteMsgLastDrop.setStatus("current")
_OutboundVoteMsgFailureCount_Type = Integer32
_OutboundVoteMsgFailureCount_Object = MibTableColumn
outboundVoteMsgFailureCount = _OutboundVoteMsgFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1, 6),
    _OutboundVoteMsgFailureCount_Type()
)
outboundVoteMsgFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundVoteMsgFailureCount.setStatus("current")
_OutboundVoteMsgLastFailureTime_Type = DisplayString
_OutboundVoteMsgLastFailureTime_Object = MibTableColumn
outboundVoteMsgLastFailureTime = _OutboundVoteMsgLastFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1, 7),
    _OutboundVoteMsgLastFailureTime_Type()
)
outboundVoteMsgLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundVoteMsgLastFailureTime.setStatus("current")
_OutboundVotesLastError_Type = DisplayString
_OutboundVotesLastError_Object = MibTableColumn
outboundVotesLastError = _OutboundVotesLastError_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 14, 1, 8),
    _OutboundVotesLastError_Type()
)
outboundVotesLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundVotesLastError.setStatus("current")
_VotingSessionsStatisticsTable_Object = MibTable
votingSessionsStatisticsTable = _VotingSessionsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 15)
)
if mibBuilder.loadTexts:
    votingSessionsStatisticsTable.setStatus("current")
_VotingSessionsStatisticsEntry_Object = MibTableRow
votingSessionsStatisticsEntry = _VotingSessionsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 15, 1)
)
votingSessionsStatisticsEntry.setIndexNames(
    (1, "INVIDI-MIB", "votingSessionSessionID"),
)
if mibBuilder.loadTexts:
    votingSessionsStatisticsEntry.setStatus("current")
_VotingSessionSessionID_Type = ObjectIdentifier
_VotingSessionSessionID_Object = MibTableColumn
votingSessionSessionID = _VotingSessionSessionID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 15, 1, 1),
    _VotingSessionSessionID_Type()
)
votingSessionSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    votingSessionSessionID.setStatus("current")
_VotingSessionBreakID_Type = Integer32
_VotingSessionBreakID_Object = MibTableColumn
votingSessionBreakID = _VotingSessionBreakID_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 15, 1, 2),
    _VotingSessionBreakID_Type()
)
votingSessionBreakID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    votingSessionBreakID.setStatus("current")
_VotingSessionBdsAddress_Type = DisplayString
_VotingSessionBdsAddress_Object = MibTableColumn
votingSessionBdsAddress = _VotingSessionBdsAddress_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 15, 1, 3),
    _VotingSessionBdsAddress_Type()
)
votingSessionBdsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    votingSessionBdsAddress.setStatus("current")
_VotingSessionVoteEndTime_Type = DisplayString
_VotingSessionVoteEndTime_Object = MibTableColumn
votingSessionVoteEndTime = _VotingSessionVoteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 6, 15, 1, 4),
    _VotingSessionVoteEndTime_Type()
)
votingSessionVoteEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    votingSessionVoteEndTime.setStatus("current")
_InvidiConformance_ObjectIdentity = ObjectIdentity
invidiConformance = _InvidiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 2)
)
_InvidiMIBGroups_ObjectIdentity = ObjectIdentity
invidiMIBGroups = _InvidiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1)
)
_InvidiMIBCompliances_ObjectIdentity = ObjectIdentity
invidiMIBCompliances = _InvidiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30307, 2, 2)
)

# Managed Objects groups

pageStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 1)
)
pageStatusGroup.setObjects(
      *(("INVIDI-MIB", "bdmsInterfaceStatus"),
        ("INVIDI-MIB", "inBandDataMonitorStatus"),
        ("INVIDI-MIB", "plantInterfaceStatus"),
        ("INVIDI-MIB", "outBandDataMonitorStatus"),
        ("INVIDI-MIB", "rcsInterfaceStatus"))
)
if mibBuilder.loadTexts:
    pageStatusGroup.setStatus("current")

bdmsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 2)
)
bdmsInterfaceGroup.setObjects(
      *(("INVIDI-MIB", "bizStatus"),
        ("INVIDI-MIB", "lastStartTime"),
        ("INVIDI-MIB", "lastCompletedTime"),
        ("INVIDI-MIB", "estimatedNextRequest"),
        ("INVIDI-MIB", "completedRequests"),
        ("INVIDI-MIB", "completedReqSinceReset"),
        ("INVIDI-MIB", "acceptedRecords"),
        ("INVIDI-MIB", "rejectedRecords"),
        ("INVIDI-MIB", "lastErrorTime"),
        ("INVIDI-MIB", "lastError"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceGroup.setStatus("current")

inbandDataMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 3)
)
inbandDataMonitorGroup.setObjects(
      *(("INVIDI-MIB", "vlNetwork"),
        ("INVIDI-MIB", "vlZone"),
        ("INVIDI-MIB", "vlSourceId"),
        ("INVIDI-MIB", "vlAVProfileName"),
        ("INVIDI-MIB", "vlID"),
        ("INVIDI-MIB", "vlType"),
        ("INVIDI-MIB", "vlUniqueProgID"),
        ("INVIDI-MIB", "vlAvailNumber"),
        ("INVIDI-MIB", "vlWindowID"),
        ("INVIDI-MIB", "vlLength"),
        ("INVIDI-MIB", "vlNumEntries"),
        ("INVIDI-MIB", "vlStartTime"),
        ("INVIDI-MIB", "vlEndTime"),
        ("INVIDI-MIB", "vlBreakPos"),
        ("INVIDI-MIB", "vlCueTime"),
        ("INVIDI-MIB", "vlCueReceived"),
        ("INVIDI-MIB", "vlAirTime"),
        ("INVIDI-MIB", "vlExpectedEndTime"),
        ("INVIDI-MIB", "vlStatus"),
        ("INVIDI-MIB", "vlReqTimingMsgs"),
        ("INVIDI-MIB", "vlLastMsgSent"))
)
if mibBuilder.loadTexts:
    inbandDataMonitorGroup.setStatus("current")

cueToneStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 4)
)
cueToneStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "qtReceived"),
        ("INVIDI-MIB", "qtCueTime"),
        ("INVIDI-MIB", "qtPtsTime"),
        ("INVIDI-MIB", "qtTimeToInsert"),
        ("INVIDI-MIB", "qtHost"),
        ("INVIDI-MIB", "qtNetwork"),
        ("INVIDI-MIB", "qtZone"),
        ("INVIDI-MIB", "qtPid"),
        ("INVIDI-MIB", "qtSourceId"),
        ("INVIDI-MIB", "qtBreakId"),
        ("INVIDI-MIB", "qtUniqueProgID"),
        ("INVIDI-MIB", "qtAvailNumber"),
        ("INVIDI-MIB", "qtStartTime"),
        ("INVIDI-MIB", "qtEndTime"),
        ("INVIDI-MIB", "qtBreakPos"),
        ("INVIDI-MIB", "qtStatus"))
)
if mibBuilder.loadTexts:
    cueToneStatisticsGroup.setStatus("current")

inbandDataStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 5)
)
inbandDataStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "inMessageType"),
        ("INVIDI-MIB", "inBytesTransfered"),
        ("INVIDI-MIB", "inMessages"),
        ("INVIDI-MIB", "inStartTime"),
        ("INVIDI-MIB", "inAverageRate"),
        ("INVIDI-MIB", "inLastMessageTimeAndSize"))
)
if mibBuilder.loadTexts:
    inbandDataStatisticsGroup.setStatus("current")

unplayedBreakGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 6)
)
unplayedBreakGroup.setObjects(
      *(("INVIDI-MIB", "unvlNetwork"),
        ("INVIDI-MIB", "unvlZone"),
        ("INVIDI-MIB", "unvlSourceId"),
        ("INVIDI-MIB", "unvlAVProfileName"),
        ("INVIDI-MIB", "unvlID"),
        ("INVIDI-MIB", "unvlType"),
        ("INVIDI-MIB", "unvlUniqueProgID"),
        ("INVIDI-MIB", "unvlAvailNumber"),
        ("INVIDI-MIB", "unvlWindowID"),
        ("INVIDI-MIB", "unvlLength"),
        ("INVIDI-MIB", "unvlNumEntries"),
        ("INVIDI-MIB", "unvlStartTime"),
        ("INVIDI-MIB", "unvlEndTime"),
        ("INVIDI-MIB", "unvlBreakPos"),
        ("INVIDI-MIB", "unvlCueTime"),
        ("INVIDI-MIB", "unvlCueReceived"),
        ("INVIDI-MIB", "unvlAirTime"),
        ("INVIDI-MIB", "unvlExpectedEndTime"),
        ("INVIDI-MIB", "unvlStatus"),
        ("INVIDI-MIB", "unvlReqTimingMsgs"),
        ("INVIDI-MIB", "unvlLastMsgSent"))
)
if mibBuilder.loadTexts:
    unplayedBreakGroup.setStatus("current")

discardedBreakGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 7)
)
discardedBreakGroup.setObjects(
      *(("INVIDI-MIB", "disNetwork"),
        ("INVIDI-MIB", "disZone"),
        ("INVIDI-MIB", "disSourceId"),
        ("INVIDI-MIB", "disAVProfileName"),
        ("INVIDI-MIB", "disID"),
        ("INVIDI-MIB", "disType"),
        ("INVIDI-MIB", "disUniqueProgID"),
        ("INVIDI-MIB", "disAvailNumber"),
        ("INVIDI-MIB", "disWindowID"),
        ("INVIDI-MIB", "disLength"),
        ("INVIDI-MIB", "disNumEntries"),
        ("INVIDI-MIB", "disStartTime"),
        ("INVIDI-MIB", "disEndTime"),
        ("INVIDI-MIB", "disBreakPos"),
        ("INVIDI-MIB", "disCueTime"),
        ("INVIDI-MIB", "disCueReceived"),
        ("INVIDI-MIB", "disAirTime"),
        ("INVIDI-MIB", "disExpectedEndTime"),
        ("INVIDI-MIB", "disStatus"),
        ("INVIDI-MIB", "disReqTimingMsgs"),
        ("INVIDI-MIB", "disLastMsgSent"))
)
if mibBuilder.loadTexts:
    discardedBreakGroup.setStatus("current")

assetErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 8)
)
assetErrorGroup.setObjects(
      *(("INVIDI-MIB", "aeTime"),
        ("INVIDI-MIB", "aeDescription"))
)
if mibBuilder.loadTexts:
    assetErrorGroup.setStatus("current")

adInserterStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 9)
)
adInserterStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "adinsName"),
        ("INVIDI-MIB", "adinsIndex"),
        ("INVIDI-MIB", "adinsStatus"),
        ("INVIDI-MIB", "adinsSuccesses"),
        ("INVIDI-MIB", "adinsSuccessTime"),
        ("INVIDI-MIB", "adinsFailures"),
        ("INVIDI-MIB", "adinsFailTime"),
        ("INVIDI-MIB", "adinsError"))
)
if mibBuilder.loadTexts:
    adInserterStatisticsGroup.setStatus("current")

insertionStreamConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 10)
)
insertionStreamConfigGroup.setObjects(
      *(("INVIDI-MIB", "insStreamAdInsName"),
        ("INVIDI-MIB", "insStreamAdInsType"),
        ("INVIDI-MIB", "insStreamAdChEIA"),
        ("INVIDI-MIB", "insStreamAdChFreq"),
        ("INVIDI-MIB", "insStreamAdChMod"),
        ("INVIDI-MIB", "insStreamTBID"),
        ("INVIDI-MIB", "insStreamTBZone"),
        ("INVIDI-MIB", "insStreamIUID"),
        ("INVIDI-MIB", "insStreamTCID"),
        ("INVIDI-MIB", "insStreamChName"),
        ("INVIDI-MIB", "insStreamChZone"),
        ("INVIDI-MIB", "insStreamHiddenCh"),
        ("INVIDI-MIB", "insStreamAvProCat"),
        ("INVIDI-MIB", "insStreamProgramNum"),
        ("INVIDI-MIB", "insStreamPreroll"))
)
if mibBuilder.loadTexts:
    insertionStreamConfigGroup.setStatus("current")

virtualStreamConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 11)
)
virtualStreamConfigGroup.setObjects(
      *(("INVIDI-MIB", "virtualStreamIUID"),
        ("INVIDI-MIB", "virtualStreamTCID"),
        ("INVIDI-MIB", "virtualStreamZONE"))
)
if mibBuilder.loadTexts:
    virtualStreamConfigGroup.setStatus("current")

amsStatisticsPlantIFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 12)
)
amsStatisticsPlantIFGroup.setObjects(
      *(("INVIDI-MIB", "amsName"),
        ("INVIDI-MIB", "amsStatus"),
        ("INVIDI-MIB", "amsSuccesses"),
        ("INVIDI-MIB", "amsSuccessTime"),
        ("INVIDI-MIB", "amsFailures"),
        ("INVIDI-MIB", "amsFailTime"),
        ("INVIDI-MIB", "amsError"))
)
if mibBuilder.loadTexts:
    amsStatisticsPlantIFGroup.setStatus("current")

svcAdvertisementConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 13)
)
svcAdvertisementConnectionGroup.setObjects(
      *(("INVIDI-MIB", "advName"),
        ("INVIDI-MIB", "advAddress"),
        ("INVIDI-MIB", "advPort"),
        ("INVIDI-MIB", "advStatus"),
        ("INVIDI-MIB", "advLastSuccess"),
        ("INVIDI-MIB", "advLastFail"),
        ("INVIDI-MIB", "advLastError"))
)
if mibBuilder.loadTexts:
    svcAdvertisementConnectionGroup.setStatus("current")

serviceMuxListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 14)
)
serviceMuxListGroup.setObjects(
      *(("INVIDI-MIB", "muxID"),
        ("INVIDI-MIB", "muxDescription"),
        ("INVIDI-MIB", "muxVersion"),
        ("INVIDI-MIB", "muxSequence"),
        ("INVIDI-MIB", "muxAddress"),
        ("INVIDI-MIB", "muxPreferred"),
        ("INVIDI-MIB", "muxSvcList"))
)
if mibBuilder.loadTexts:
    serviceMuxListGroup.setStatus("current")

scte35ReceiverConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 15)
)
scte35ReceiverConnectionGroup.setObjects(
      *(("INVIDI-MIB", "scte35Name"),
        ("INVIDI-MIB", "scte35CueRecvTime"),
        ("INVIDI-MIB", "scte35Status"),
        ("INVIDI-MIB", "scte35SuccessTime"),
        ("INVIDI-MIB", "scte35FailTime"),
        ("INVIDI-MIB", "scte35Error"))
)
if mibBuilder.loadTexts:
    scte35ReceiverConnectionGroup.setStatus("current")

serviceCueConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 16)
)
serviceCueConnectionGroup.setObjects(
      *(("INVIDI-MIB", "cueSvcID"),
        ("INVIDI-MIB", "cueSvcName"),
        ("INVIDI-MIB", "cueSvcZone"),
        ("INVIDI-MIB", "cueSvcMuxID"),
        ("INVIDI-MIB", "cueSvcLastRecvTime"),
        ("INVIDI-MIB", "cueSvcStatus"),
        ("INVIDI-MIB", "cueSvcLastSuccess"),
        ("INVIDI-MIB", "cueSvcLastFail"),
        ("INVIDI-MIB", "cueSvcLastErr"))
)
if mibBuilder.loadTexts:
    serviceCueConnectionGroup.setStatus("current")

serviceInbandConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 17)
)
serviceInbandConnectionGroup.setObjects(
      *(("INVIDI-MIB", "inSvcID"),
        ("INVIDI-MIB", "inSvcName"),
        ("INVIDI-MIB", "inSvcZone"),
        ("INVIDI-MIB", "inSvcPriAddress"),
        ("INVIDI-MIB", "inSvcSecAddress"),
        ("INVIDI-MIB", "inSvcTerAddress"),
        ("INVIDI-MIB", "inSvcQuaAddress"),
        ("INVIDI-MIB", "inSvcVoteLastSendTime"),
        ("INVIDI-MIB", "inSvcVlLastSendTime"),
        ("INVIDI-MIB", "inSvcBdLastSendTime"),
        ("INVIDI-MIB", "inSvcRTMLastSendTime"),
        ("INVIDI-MIB", "inSvcCueLastSendTime"),
        ("INVIDI-MIB", "inSvcStatus"),
        ("INVIDI-MIB", "inSvcLastSuccess"),
        ("INVIDI-MIB", "inSvcLastFail"),
        ("INVIDI-MIB", "inSvcLastErr"))
)
if mibBuilder.loadTexts:
    serviceInbandConnectionGroup.setStatus("current")

assetStateCheckStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 18)
)
assetStateCheckStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "ascName"),
        ("INVIDI-MIB", "ascStatus"),
        ("INVIDI-MIB", "ascSuccesses"),
        ("INVIDI-MIB", "ascSuccessTime"),
        ("INVIDI-MIB", "ascFailures"),
        ("INVIDI-MIB", "ascFailTime"),
        ("INVIDI-MIB", "ascError"))
)
if mibBuilder.loadTexts:
    assetStateCheckStatisticsGroup.setStatus("current")

bdsErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 19)
)
bdsErrorGroup.setObjects(
      *(("INVIDI-MIB", "bdsErrorTime"),
        ("INVIDI-MIB", "bdsErrorDescription"))
)
if mibBuilder.loadTexts:
    bdsErrorGroup.setStatus("current")

svcWithNoUsableInsertStreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 20)
)
svcWithNoUsableInsertStreamGroup.setObjects(
      *(("INVIDI-MIB", "noUsableInsStreamsSvcID"),
        ("INVIDI-MIB", "noUsableInsStreamsSvcName"),
        ("INVIDI-MIB", "noUsableInsStreamsSvcZone"),
        ("INVIDI-MIB", "noUsableInsStreamsAvPID"),
        ("INVIDI-MIB", "noUsableInsStreamsAvPName"),
        ("INVIDI-MIB", "noUsableInsStreamsAVPCatID"),
        ("INVIDI-MIB", "noUsableInsStreamsAVPCatName"))
)
if mibBuilder.loadTexts:
    svcWithNoUsableInsertStreamGroup.setStatus("current")

avProfileCategoryMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 21)
)
avProfileCategoryMappingGroup.setObjects(
      *(("INVIDI-MIB", "avProfCatID"),
        ("INVIDI-MIB", "avProfCatName"),
        ("INVIDI-MIB", "avProfCatFiller"),
        ("INVIDI-MIB", "avProfCatAVProfID"),
        ("INVIDI-MIB", "avProfCatAVProfName"),
        ("INVIDI-MIB", "avProfCatStreams"))
)
if mibBuilder.loadTexts:
    avProfileCategoryMappingGroup.setStatus("current")

carouselMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 22)
)
carouselMonitorGroup.setObjects(
      *(("INVIDI-MIB", "messageType"),
        ("INVIDI-MIB", "bytesTransfered"),
        ("INVIDI-MIB", "messages"),
        ("INVIDI-MIB", "startTime"),
        ("INVIDI-MIB", "averageRate"),
        ("INVIDI-MIB", "lastMessageTimeAndSize"))
)
if mibBuilder.loadTexts:
    carouselMonitorGroup.setStatus("current")

fileDropStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 23)
)
fileDropStatusGroup.setObjects(
      *(("INVIDI-MIB", "fileType"),
        ("INVIDI-MIB", "fileDropSegment"),
        ("INVIDI-MIB", "fileDropCreationTime"),
        ("INVIDI-MIB", "transferStatus"),
        ("INVIDI-MIB", "transferSuccesses"),
        ("INVIDI-MIB", "transferSuccessTime"),
        ("INVIDI-MIB", "transferFailures"),
        ("INVIDI-MIB", "transferFailTime"),
        ("INVIDI-MIB", "transferError"))
)
if mibBuilder.loadTexts:
    fileDropStatusGroup.setStatus("current")

dssStatusStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 24)
)
dssStatusStatisticsGroup.setObjects(
    ("INVIDI-MIB", "dssStatus")
)
if mibBuilder.loadTexts:
    dssStatusStatisticsGroup.setStatus("current")

targetUpdateStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 25)
)
targetUpdateStatusGroup.setObjects(
      *(("INVIDI-MIB", "targetUpdateName"),
        ("INVIDI-MIB", "targetUpdateStatus"),
        ("INVIDI-MIB", "targetUpdateSuccesses"),
        ("INVIDI-MIB", "targetUpdateSuccessTime"),
        ("INVIDI-MIB", "targetUpdateFailures"),
        ("INVIDI-MIB", "targetUpdateFailTime"),
        ("INVIDI-MIB", "targetUpdateError"))
)
if mibBuilder.loadTexts:
    targetUpdateStatusGroup.setStatus("current")

serviceSCTE35CueReceiverMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 26)
)
serviceSCTE35CueReceiverMapGroup.setObjects(
      *(("INVIDI-MIB", "scte35CueSvcID"),
        ("INVIDI-MIB", "scte35CueSvcName"),
        ("INVIDI-MIB", "scte35CueSvcZone"),
        ("INVIDI-MIB", "scte35CueSvcPID"),
        ("INVIDI-MIB", "scte35CueReceiverAddr"))
)
if mibBuilder.loadTexts:
    serviceSCTE35CueReceiverMapGroup.setStatus("current")

adoAloCreationStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 27)
)
adoAloCreationStatusGroup.setObjects(
      *(("INVIDI-MIB", "adoAloCreationName"),
        ("INVIDI-MIB", "adoAloCreationStatus"),
        ("INVIDI-MIB", "adoAloCreationSuccesses"),
        ("INVIDI-MIB", "adoAloCreationSuccessTime"),
        ("INVIDI-MIB", "adoAloCreationFailures"),
        ("INVIDI-MIB", "adoAloCreationFailTime"),
        ("INVIDI-MIB", "adoAloCreationError"))
)
if mibBuilder.loadTexts:
    adoAloCreationStatusGroup.setStatus("current")

prioritizerAssetPushStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 28)
)
prioritizerAssetPushStatusGroup.setObjects(
      *(("INVIDI-MIB", "prioritizerAssetPushName"),
        ("INVIDI-MIB", "prioritizerAssetPushStatus"),
        ("INVIDI-MIB", "prioritizerAssetPushSuccesses"),
        ("INVIDI-MIB", "prioritizerAssetPushSuccessTime"),
        ("INVIDI-MIB", "prioritizerAssetPushFailures"),
        ("INVIDI-MIB", "prioritizerAssetPushFailTime"),
        ("INVIDI-MIB", "prioritizerAssetPushError"))
)
if mibBuilder.loadTexts:
    prioritizerAssetPushStatusGroup.setStatus("current")

dssErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 29)
)
dssErrorGroup.setObjects(
      *(("INVIDI-MIB", "dssErrorTime"),
        ("INVIDI-MIB", "dssErrorDescription"))
)
if mibBuilder.loadTexts:
    dssErrorGroup.setStatus("current")

processingStatusStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 30)
)
processingStatusStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "eventTime"),
        ("INVIDI-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    processingStatusStatisticsGroup.setStatus("current")

interactiveFromStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 31)
)
interactiveFromStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "fromMessageType"),
        ("INVIDI-MIB", "fromBytesTransfered"),
        ("INVIDI-MIB", "fromMessages"),
        ("INVIDI-MIB", "fromStartTime"),
        ("INVIDI-MIB", "fromAverageRate"),
        ("INVIDI-MIB", "fromLastMessageTimeAndSize"))
)
if mibBuilder.loadTexts:
    interactiveFromStatisticsGroup.setStatus("current")

interactiveToStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 32)
)
interactiveToStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "toMessageType"),
        ("INVIDI-MIB", "toBytesTransfered"),
        ("INVIDI-MIB", "toMessages"),
        ("INVIDI-MIB", "toStartTime"),
        ("INVIDI-MIB", "toAverageRate"),
        ("INVIDI-MIB", "toLastMessageTimeAndSize"))
)
if mibBuilder.loadTexts:
    interactiveToStatisticsGroup.setStatus("current")

stbReturnStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 33)
)
stbReturnStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "numberOfConnectRetries"),
        ("INVIDI-MIB", "numberOfResends"),
        ("INVIDI-MIB", "numberOfV1AliveMessages"),
        ("INVIDI-MIB", "percentageOfV1AliveMessages"))
)
if mibBuilder.loadTexts:
    stbReturnStatisticsGroup.setStatus("current")

stbStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 34)
)
stbStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "boxID"),
        ("INVIDI-MIB", "messagesCount"),
        ("INVIDI-MIB", "exposedDateTime"),
        ("INVIDI-MIB", "dateRequestAndTime"),
        ("INVIDI-MIB", "lastAdPlayed"),
        ("INVIDI-MIB", "returnStats"),
        ("INVIDI-MIB", "lastMessage"))
)
if mibBuilder.loadTexts:
    stbStatisticsGroup.setStatus("current")

unknownSetTopsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 35)
)
unknownSetTopsGroup.setObjects(
      *(("INVIDI-MIB", "boxIDUnknown"),
        ("INVIDI-MIB", "requestTime"))
)
if mibBuilder.loadTexts:
    unknownSetTopsGroup.setStatus("current")

clickStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 36)
)
clickStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "clickStatus"),
        ("INVIDI-MIB", "clickSuccesses"),
        ("INVIDI-MIB", "clickLastSuccessTime"),
        ("INVIDI-MIB", "clickFailures"),
        ("INVIDI-MIB", "clickLastFailureTime"),
        ("INVIDI-MIB", "clickLastError"))
)
if mibBuilder.loadTexts:
    clickStatisticsGroup.setStatus("current")

rawAdnFileCreationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 37)
)
rawAdnFileCreationGroup.setObjects(
      *(("INVIDI-MIB", "rawAdnFileCreationFileshare"),
        ("INVIDI-MIB", "rawAdnFileCreationRetrieval"),
        ("INVIDI-MIB", "rawAdnFileCreationSuccess"),
        ("INVIDI-MIB", "rawAdnFileCreationLastSuccess"),
        ("INVIDI-MIB", "rawAdnFileCreationFailure"),
        ("INVIDI-MIB", "rawAdnFileCreationLastFailure"),
        ("INVIDI-MIB", "rawAdnFileCreationLastError"))
)
if mibBuilder.loadTexts:
    rawAdnFileCreationGroup.setStatus("current")

rawAdnFileTransferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 38)
)
rawAdnFileTransferGroup.setObjects(
      *(("INVIDI-MIB", "rawAdnFileTransferFileshare"),
        ("INVIDI-MIB", "rawAdnFileTransferRetrieval"),
        ("INVIDI-MIB", "rawAdnFileTransferSuccess"),
        ("INVIDI-MIB", "rawAdnFileTransferLastSuccess"),
        ("INVIDI-MIB", "rawAdnFileTransferFailure"),
        ("INVIDI-MIB", "rawAdnFileTransferLastFailure"),
        ("INVIDI-MIB", "rawAdnFileTransferLastError"))
)
if mibBuilder.loadTexts:
    rawAdnFileTransferGroup.setStatus("current")

viewerMeasurementStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 39)
)
viewerMeasurementStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "vmIP"),
        ("INVIDI-MIB", "vmRetrieval"),
        ("INVIDI-MIB", "vmSuccess"),
        ("INVIDI-MIB", "vmLastSuccess"),
        ("INVIDI-MIB", "vmFailure"),
        ("INVIDI-MIB", "vmLastFailure"),
        ("INVIDI-MIB", "vmLastError"))
)
if mibBuilder.loadTexts:
    viewerMeasurementStatisticsGroup.setStatus("current")

amsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 40)
)
amsStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "amsFileshare"),
        ("INVIDI-MIB", "amsRetrieval"),
        ("INVIDI-MIB", "amsSuccess"),
        ("INVIDI-MIB", "amsLastSuccess"),
        ("INVIDI-MIB", "amsFailure"),
        ("INVIDI-MIB", "amsLastFailure"),
        ("INVIDI-MIB", "amsLastError"))
)
if mibBuilder.loadTexts:
    amsStatisticsGroup.setStatus("current")

rcsErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 41)
)
rcsErrorGroup.setObjects(
      *(("INVIDI-MIB", "rcsErrorTime"),
        ("INVIDI-MIB", "rcsErrorDescription"))
)
if mibBuilder.loadTexts:
    rcsErrorGroup.setStatus("current")

inboundVotesStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 42)
)
inboundVotesStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "inboundVotesRcsAddress"),
        ("INVIDI-MIB", "inboundVoteMsgReceivedCount"),
        ("INVIDI-MIB", "inboundVoteMsgLastRecevied"),
        ("INVIDI-MIB", "inboundVoteMsgFailureCount"),
        ("INVIDI-MIB", "inboundVoteMsgLastFailureTime"),
        ("INVIDI-MIB", "inboundVotesLastError"))
)
if mibBuilder.loadTexts:
    inboundVotesStatisticsGroup.setStatus("current")

outboundVotesStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 43)
)
outboundVotesStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "outboundVotesBdsAddress"),
        ("INVIDI-MIB", "outboundVoteMsgSentCount"),
        ("INVIDI-MIB", "outboundVoteMsgLastSent"),
        ("INVIDI-MIB", "outboundVoteMsgDropCount"),
        ("INVIDI-MIB", "outboundVoteMsgLastDrop"),
        ("INVIDI-MIB", "outboundVoteMsgFailureCount"),
        ("INVIDI-MIB", "outboundVoteMsgLastFailureTime"),
        ("INVIDI-MIB", "outboundVotesLastError"))
)
if mibBuilder.loadTexts:
    outboundVotesStatisticsGroup.setStatus("current")

votingSessionsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 44)
)
votingSessionsStatisticsGroup.setObjects(
      *(("INVIDI-MIB", "votingSessionSessionID"),
        ("INVIDI-MIB", "votingSessionBreakID"),
        ("INVIDI-MIB", "votingSessionBdsAddress"),
        ("INVIDI-MIB", "votingSessionVoteEndTime"))
)
if mibBuilder.loadTexts:
    votingSessionsStatisticsGroup.setStatus("current")

notificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 45)
)
notificationObjectsGroup.setObjects(
      *(("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    notificationObjectsGroup.setStatus("current")


# Notification objects

advatarSystemFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 1)
)
advatarSystemFailure.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    advatarSystemFailure.setStatus(
        "current"
    )

transferOfClickStreamFileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 2)
)
transferOfClickStreamFileFailed.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    transferOfClickStreamFileFailed.setStatus(
        "current"
    )

bdmsInterfaceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 3)
)
bdmsInterfaceError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceError.setStatus(
        "current"
    )

adInserterErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 4)
)
adInserterErrors.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    adInserterErrors.setStatus(
        "current"
    )

cueProcessingErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 5)
)
cueProcessingErrors.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    cueProcessingErrors.setStatus(
        "current"
    )

viewListErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 6)
)
viewListErrors.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    viewListErrors.setStatus(
        "current"
    )

advatarError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 7)
)
advatarError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    advatarError.setStatus(
        "current"
    )

assetError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 8)
)
assetError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    assetError.setStatus(
        "current"
    )

breakWindowDiscarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 9)
)
breakWindowDiscarded.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    breakWindowDiscarded.setStatus(
        "current"
    )

advatarSystemAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 10)
)
advatarSystemAlert.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    advatarSystemAlert.setStatus(
        "current"
    )

bdmsInterfaceErrorBreakWindows = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 11)
)
bdmsInterfaceErrorBreakWindows.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorBreakWindows.setStatus(
        "current"
    )

bdmsInterfaceErrorAssets = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 12)
)
bdmsInterfaceErrorAssets.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorAssets.setStatus(
        "current"
    )

bdmsInterfaceErrorAdrs = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 13)
)
bdmsInterfaceErrorAdrs.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorAdrs.setStatus(
        "current"
    )

bdmsInterfaceErrorVerificatLogs = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 14)
)
bdmsInterfaceErrorVerificatLogs.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorVerificatLogs.setStatus(
        "current"
    )

bdmsInterfaceErrorVlReportLogs = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 16)
)
bdmsInterfaceErrorVlReportLogs.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorVlReportLogs.setStatus(
        "current"
    )

bdmsInterfaceErrorGuideData = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 17)
)
bdmsInterfaceErrorGuideData.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorGuideData.setStatus(
        "current"
    )

bdmsInterfaceErrorImpressions = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 18)
)
bdmsInterfaceErrorImpressions.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorImpressions.setStatus(
        "current"
    )

bdmsInterfaceErrorStbData = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 19)
)
bdmsInterfaceErrorStbData.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorStbData.setStatus(
        "current"
    )

bdmsInterfaceErrorStbRespondList = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 20)
)
bdmsInterfaceErrorStbRespondList.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorStbRespondList.setStatus(
        "current"
    )

bdmsInterfaceErrorUnknownSTBList = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 21)
)
bdmsInterfaceErrorUnknownSTBList.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorUnknownSTBList.setStatus(
        "current"
    )

adInserterErrorSchedulesWritten = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 23)
)
adInserterErrorSchedulesWritten.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    adInserterErrorSchedulesWritten.setStatus(
        "current"
    )

cueReceiverConnectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 24)
)
cueReceiverConnectionError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    cueReceiverConnectionError.setStatus(
        "current"
    )

adInserterErrorCueTonesSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 25)
)
adInserterErrorCueTonesSent.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    adInserterErrorCueTonesSent.setStatus(
        "current"
    )

adInserterErrorSnmpStatistics = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 26)
)
adInserterErrorSnmpStatistics.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    adInserterErrorSnmpStatistics.setStatus(
        "current"
    )

adnProcessingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 30)
)
adnProcessingError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    adnProcessingError.setStatus(
        "current"
    )

noBreaksReceivedFromBDMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 33)
)
noBreaksReceivedFromBDMS.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    noBreaksReceivedFromBDMS.setStatus(
        "current"
    )

advatarStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 34)
)
advatarStarted.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    advatarStarted.setStatus(
        "current"
    )

advatarStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 35)
)
advatarStopped.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    advatarStopped.setStatus(
        "current"
    )

noCueReceivedForWindow = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 36)
)
noCueReceivedForWindow.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    noCueReceivedForWindow.setStatus(
        "current"
    )

bdmsInterfaceErrorBreakStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 38)
)
bdmsInterfaceErrorBreakStatus.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorBreakStatus.setStatus(
        "current"
    )

outOfBandErrorOnDemandInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 39)
)
outOfBandErrorOnDemandInterface.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    outOfBandErrorOnDemandInterface.setStatus(
        "current"
    )

cueInactivityOnNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 40)
)
cueInactivityOnNetwork.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    cueInactivityOnNetwork.setStatus(
        "current"
    )

unplayedBreak = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 41)
)
unplayedBreak.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    unplayedBreak.setStatus(
        "current"
    )

bdsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 42)
)
bdsError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdsError.setStatus(
        "current"
    )

dssError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 43)
)
dssError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    dssError.setStatus(
        "current"
    )

rcsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 44)
)
rcsError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    rcsError.setStatus(
        "current"
    )

bdmsInterfaceErrorReqAssetsList = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 46)
)
bdmsInterfaceErrorReqAssetsList.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorReqAssetsList.setStatus(
        "current"
    )

bdmsInterfaceErrorAssetStateList = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 47)
)
bdmsInterfaceErrorAssetStateList.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorAssetStateList.setStatus(
        "current"
    )

gcsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 48)
)
gcsError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    gcsError.setStatus(
        "current"
    )

configurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 49)
)
configurationError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    configurationError.setStatus(
        "current"
    )

assetsPresentListStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 50)
)
assetsPresentListStatus.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    assetsPresentListStatus.setStatus(
        "current"
    )

requiredAssetsListStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 51)
)
requiredAssetsListStatus.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    requiredAssetsListStatus.setStatus(
        "current"
    )

voteRoutingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 52)
)
voteRoutingError.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    voteRoutingError.setStatus(
        "current"
    )

outOfBandErrorFileDropInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 53)
)
outOfBandErrorFileDropInterface.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    outOfBandErrorFileDropInterface.setStatus(
        "current"
    )

voteDroppedReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 54)
)
voteDroppedReport.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    voteDroppedReport.setStatus(
        "current"
    )

bdmsInterfaceErrorAvProfCatData = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 55)
)
bdmsInterfaceErrorAvProfCatData.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorAvProfCatData.setStatus(
        "current"
    )

bdmsInterfaceErrorAiredBreaks = NotificationType(
    (1, 3, 6, 1, 4, 1, 30307, 1, 1, 0, 0, 56)
)
bdmsInterfaceErrorAiredBreaks.setObjects(
      *(("INVIDI-MIB", "hostName"),
        ("INVIDI-MIB", "ipAddress"),
        ("INVIDI-MIB", "errorString"))
)
if mibBuilder.loadTexts:
    bdmsInterfaceErrorAiredBreaks.setStatus(
        "current"
    )


# Notifications groups

trapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30307, 2, 1, 46)
)
trapNotificationGroup.setObjects(
      *(("INVIDI-MIB", "advatarSystemFailure"),
        ("INVIDI-MIB", "transferOfClickStreamFileFailed"),
        ("INVIDI-MIB", "bdmsInterfaceError"),
        ("INVIDI-MIB", "adInserterErrors"),
        ("INVIDI-MIB", "cueProcessingErrors"),
        ("INVIDI-MIB", "viewListErrors"),
        ("INVIDI-MIB", "advatarError"),
        ("INVIDI-MIB", "assetError"),
        ("INVIDI-MIB", "breakWindowDiscarded"),
        ("INVIDI-MIB", "advatarSystemAlert"),
        ("INVIDI-MIB", "bdmsInterfaceErrorBreakWindows"),
        ("INVIDI-MIB", "bdmsInterfaceErrorAssets"),
        ("INVIDI-MIB", "bdmsInterfaceErrorAdrs"),
        ("INVIDI-MIB", "bdmsInterfaceErrorVerificatLogs"),
        ("INVIDI-MIB", "bdmsInterfaceErrorVlReportLogs"),
        ("INVIDI-MIB", "bdmsInterfaceErrorGuideData"),
        ("INVIDI-MIB", "bdmsInterfaceErrorImpressions"),
        ("INVIDI-MIB", "bdmsInterfaceErrorStbData"),
        ("INVIDI-MIB", "bdmsInterfaceErrorStbRespondList"),
        ("INVIDI-MIB", "bdmsInterfaceErrorUnknownSTBList"),
        ("INVIDI-MIB", "adInserterErrorSchedulesWritten"),
        ("INVIDI-MIB", "cueReceiverConnectionError"),
        ("INVIDI-MIB", "adInserterErrorCueTonesSent"),
        ("INVIDI-MIB", "adInserterErrorSnmpStatistics"),
        ("INVIDI-MIB", "adnProcessingError"),
        ("INVIDI-MIB", "noBreaksReceivedFromBDMS"),
        ("INVIDI-MIB", "advatarStarted"),
        ("INVIDI-MIB", "advatarStopped"),
        ("INVIDI-MIB", "noCueReceivedForWindow"),
        ("INVIDI-MIB", "bdmsInterfaceErrorBreakStatus"),
        ("INVIDI-MIB", "outOfBandErrorOnDemandInterface"),
        ("INVIDI-MIB", "cueInactivityOnNetwork"),
        ("INVIDI-MIB", "unplayedBreak"),
        ("INVIDI-MIB", "bdsError"),
        ("INVIDI-MIB", "dssError"),
        ("INVIDI-MIB", "rcsError"),
        ("INVIDI-MIB", "bdmsInterfaceErrorReqAssetsList"),
        ("INVIDI-MIB", "bdmsInterfaceErrorAssetStateList"),
        ("INVIDI-MIB", "gcsError"),
        ("INVIDI-MIB", "configurationError"),
        ("INVIDI-MIB", "assetsPresentListStatus"),
        ("INVIDI-MIB", "requiredAssetsListStatus"),
        ("INVIDI-MIB", "voteRoutingError"),
        ("INVIDI-MIB", "outOfBandErrorFileDropInterface"),
        ("INVIDI-MIB", "voteDroppedReport"),
        ("INVIDI-MIB", "bdmsInterfaceErrorAvProfCatData"),
        ("INVIDI-MIB", "bdmsInterfaceErrorAiredBreaks"))
)
if mibBuilder.loadTexts:
    trapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

invidiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30307, 2, 2, 1)
)
invidiMIBCompliance.setObjects(
      *(("INVIDI-MIB", "pageStatusGroup"),
        ("INVIDI-MIB", "bdmsInterfaceGroup"))
)
if mibBuilder.loadTexts:
    invidiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INVIDI-MIB",
    **{"StatusType": StatusType,
       "InterfaceType": InterfaceType,
       "invidiMIB": invidiMIB,
       "products": products,
       "advatar": advatar,
       "notificationPrefix": notificationPrefix,
       "mibNotifications": mibNotifications,
       "advatarSystemFailure": advatarSystemFailure,
       "transferOfClickStreamFileFailed": transferOfClickStreamFileFailed,
       "bdmsInterfaceError": bdmsInterfaceError,
       "adInserterErrors": adInserterErrors,
       "cueProcessingErrors": cueProcessingErrors,
       "viewListErrors": viewListErrors,
       "advatarError": advatarError,
       "assetError": assetError,
       "breakWindowDiscarded": breakWindowDiscarded,
       "advatarSystemAlert": advatarSystemAlert,
       "bdmsInterfaceErrorBreakWindows": bdmsInterfaceErrorBreakWindows,
       "bdmsInterfaceErrorAssets": bdmsInterfaceErrorAssets,
       "bdmsInterfaceErrorAdrs": bdmsInterfaceErrorAdrs,
       "bdmsInterfaceErrorVerificatLogs": bdmsInterfaceErrorVerificatLogs,
       "bdmsInterfaceErrorVlReportLogs": bdmsInterfaceErrorVlReportLogs,
       "bdmsInterfaceErrorGuideData": bdmsInterfaceErrorGuideData,
       "bdmsInterfaceErrorImpressions": bdmsInterfaceErrorImpressions,
       "bdmsInterfaceErrorStbData": bdmsInterfaceErrorStbData,
       "bdmsInterfaceErrorStbRespondList": bdmsInterfaceErrorStbRespondList,
       "bdmsInterfaceErrorUnknownSTBList": bdmsInterfaceErrorUnknownSTBList,
       "adInserterErrorSchedulesWritten": adInserterErrorSchedulesWritten,
       "cueReceiverConnectionError": cueReceiverConnectionError,
       "adInserterErrorCueTonesSent": adInserterErrorCueTonesSent,
       "adInserterErrorSnmpStatistics": adInserterErrorSnmpStatistics,
       "adnProcessingError": adnProcessingError,
       "noBreaksReceivedFromBDMS": noBreaksReceivedFromBDMS,
       "advatarStarted": advatarStarted,
       "advatarStopped": advatarStopped,
       "noCueReceivedForWindow": noCueReceivedForWindow,
       "bdmsInterfaceErrorBreakStatus": bdmsInterfaceErrorBreakStatus,
       "outOfBandErrorOnDemandInterface": outOfBandErrorOnDemandInterface,
       "cueInactivityOnNetwork": cueInactivityOnNetwork,
       "unplayedBreak": unplayedBreak,
       "bdsError": bdsError,
       "dssError": dssError,
       "rcsError": rcsError,
       "bdmsInterfaceErrorReqAssetsList": bdmsInterfaceErrorReqAssetsList,
       "bdmsInterfaceErrorAssetStateList": bdmsInterfaceErrorAssetStateList,
       "gcsError": gcsError,
       "configurationError": configurationError,
       "assetsPresentListStatus": assetsPresentListStatus,
       "requiredAssetsListStatus": requiredAssetsListStatus,
       "voteRoutingError": voteRoutingError,
       "outOfBandErrorFileDropInterface": outOfBandErrorFileDropInterface,
       "voteDroppedReport": voteDroppedReport,
       "bdmsInterfaceErrorAvProfCatData": bdmsInterfaceErrorAvProfCatData,
       "bdmsInterfaceErrorAiredBreaks": bdmsInterfaceErrorAiredBreaks,
       "notificationObjects": notificationObjects,
       "ipAddress": ipAddress,
       "hostName": hostName,
       "errorString": errorString,
       "status": status,
       "bdmsInterfaceStatus": bdmsInterfaceStatus,
       "inBandDataMonitorStatus": inBandDataMonitorStatus,
       "plantInterfaceStatus": plantInterfaceStatus,
       "outBandDataMonitorStatus": outBandDataMonitorStatus,
       "rcsInterfaceStatus": rcsInterfaceStatus,
       "bdmsInterface": bdmsInterface,
       "statisticsTable": statisticsTable,
       "statisticsEntry": statisticsEntry,
       "statisticsIndex": statisticsIndex,
       "bizStatus": bizStatus,
       "lastStartTime": lastStartTime,
       "lastCompletedTime": lastCompletedTime,
       "estimatedNextRequest": estimatedNextRequest,
       "completedRequests": completedRequests,
       "completedReqSinceReset": completedReqSinceReset,
       "acceptedRecords": acceptedRecords,
       "rejectedRecords": rejectedRecords,
       "lastErrorTime": lastErrorTime,
       "lastError": lastError,
       "inBandDataMonitor": inBandDataMonitor,
       "viewlistTable": viewlistTable,
       "viewlistStatisticsEntry": viewlistStatisticsEntry,
       "vlNetwork": vlNetwork,
       "vlZone": vlZone,
       "vlSourceId": vlSourceId,
       "vlAVProfileName": vlAVProfileName,
       "vlID": vlID,
       "vlType": vlType,
       "vlUniqueProgID": vlUniqueProgID,
       "vlAvailNumber": vlAvailNumber,
       "vlWindowID": vlWindowID,
       "vlLength": vlLength,
       "vlNumEntries": vlNumEntries,
       "vlStartTime": vlStartTime,
       "vlEndTime": vlEndTime,
       "vlBreakPos": vlBreakPos,
       "vlCueTime": vlCueTime,
       "vlCueReceived": vlCueReceived,
       "vlAirTime": vlAirTime,
       "vlExpectedEndTime": vlExpectedEndTime,
       "vlStatus": vlStatus,
       "vlReqTimingMsgs": vlReqTimingMsgs,
       "vlLastMsgSent": vlLastMsgSent,
       "cueStatisticsTable": cueStatisticsTable,
       "cueStatisticsEntry": cueStatisticsEntry,
       "qtReceived": qtReceived,
       "qtCueTime": qtCueTime,
       "qtPtsTime": qtPtsTime,
       "qtTimeToInsert": qtTimeToInsert,
       "qtHost": qtHost,
       "qtNetwork": qtNetwork,
       "qtZone": qtZone,
       "qtPid": qtPid,
       "qtSourceId": qtSourceId,
       "qtBreakId": qtBreakId,
       "qtUniqueProgID": qtUniqueProgID,
       "qtAvailNumber": qtAvailNumber,
       "qtStartTime": qtStartTime,
       "qtEndTime": qtEndTime,
       "qtBreakPos": qtBreakPos,
       "qtStatus": qtStatus,
       "inbandStbTable": inbandStbTable,
       "inbandStbStatisticsEntry": inbandStbStatisticsEntry,
       "inMessageType": inMessageType,
       "inBytesTransfered": inBytesTransfered,
       "inMessages": inMessages,
       "inStartTime": inStartTime,
       "inAverageRate": inAverageRate,
       "inLastMessageTimeAndSize": inLastMessageTimeAndSize,
       "unViewlistTable": unViewlistTable,
       "unViewlistStatisticsEntry": unViewlistStatisticsEntry,
       "unvlNetwork": unvlNetwork,
       "unvlZone": unvlZone,
       "unvlSourceId": unvlSourceId,
       "unvlAVProfileName": unvlAVProfileName,
       "unvlID": unvlID,
       "unvlType": unvlType,
       "unvlUniqueProgID": unvlUniqueProgID,
       "unvlAvailNumber": unvlAvailNumber,
       "unvlWindowID": unvlWindowID,
       "unvlLength": unvlLength,
       "unvlNumEntries": unvlNumEntries,
       "unvlStartTime": unvlStartTime,
       "unvlEndTime": unvlEndTime,
       "unvlBreakPos": unvlBreakPos,
       "unvlCueTime": unvlCueTime,
       "unvlCueReceived": unvlCueReceived,
       "unvlAirTime": unvlAirTime,
       "unvlExpectedEndTime": unvlExpectedEndTime,
       "unvlStatus": unvlStatus,
       "unvlReqTimingMsgs": unvlReqTimingMsgs,
       "unvlLastMsgSent": unvlLastMsgSent,
       "discardedTable": discardedTable,
       "discardedEntry": discardedEntry,
       "disNetwork": disNetwork,
       "disZone": disZone,
       "disSourceId": disSourceId,
       "disAVProfileName": disAVProfileName,
       "disID": disID,
       "disType": disType,
       "disUniqueProgID": disUniqueProgID,
       "disAvailNumber": disAvailNumber,
       "disWindowID": disWindowID,
       "disLength": disLength,
       "disNumEntries": disNumEntries,
       "disStartTime": disStartTime,
       "disEndTime": disEndTime,
       "disBreakPos": disBreakPos,
       "disCueTime": disCueTime,
       "disCueReceived": disCueReceived,
       "disAirTime": disAirTime,
       "disExpectedEndTime": disExpectedEndTime,
       "disStatus": disStatus,
       "disReqTimingMsgs": disReqTimingMsgs,
       "disLastMsgSent": disLastMsgSent,
       "assetErrorTable": assetErrorTable,
       "assetErrorEntry": assetErrorEntry,
       "aeTime": aeTime,
       "aeDescription": aeDescription,
       "plantInterface": plantInterface,
       "adInserterTable": adInserterTable,
       "adInserterStatisticsEntry": adInserterStatisticsEntry,
       "adinsName": adinsName,
       "adinsIndex": adinsIndex,
       "adinsStatus": adinsStatus,
       "adinsSuccesses": adinsSuccesses,
       "adinsSuccessTime": adinsSuccessTime,
       "adinsFailures": adinsFailures,
       "adinsFailTime": adinsFailTime,
       "adinsError": adinsError,
       "insStreamConfigStatisticsTable": insStreamConfigStatisticsTable,
       "insStreamConfigStatisticsEntry": insStreamConfigStatisticsEntry,
       "insStreamAdInsName": insStreamAdInsName,
       "insStreamAdInsType": insStreamAdInsType,
       "insStreamAdChEIA": insStreamAdChEIA,
       "insStreamAdChFreq": insStreamAdChFreq,
       "insStreamAdChMod": insStreamAdChMod,
       "insStreamTBID": insStreamTBID,
       "insStreamTBZone": insStreamTBZone,
       "insStreamIUID": insStreamIUID,
       "insStreamTCID": insStreamTCID,
       "insStreamChName": insStreamChName,
       "insStreamChZone": insStreamChZone,
       "insStreamHiddenCh": insStreamHiddenCh,
       "insStreamAvProCat": insStreamAvProCat,
       "insStreamProgramNum": insStreamProgramNum,
       "insStreamPreroll": insStreamPreroll,
       "virtualStreamConfigTable": virtualStreamConfigTable,
       "virtualStreamConfigEntry": virtualStreamConfigEntry,
       "virtualStreamIUID": virtualStreamIUID,
       "virtualStreamTCID": virtualStreamTCID,
       "virtualStreamZONE": virtualStreamZONE,
       "assetManagementTable": assetManagementTable,
       "assetManagementStatisticsEntry": assetManagementStatisticsEntry,
       "amsName": amsName,
       "amsStatus": amsStatus,
       "amsSuccesses": amsSuccesses,
       "amsSuccessTime": amsSuccessTime,
       "amsFailures": amsFailures,
       "amsFailTime": amsFailTime,
       "amsError": amsError,
       "adConnTable": adConnTable,
       "adConnectionEntry": adConnectionEntry,
       "advName": advName,
       "advAddress": advAddress,
       "advPort": advPort,
       "advStatus": advStatus,
       "advLastSuccess": advLastSuccess,
       "advLastFail": advLastFail,
       "advLastError": advLastError,
       "muxSvcTable": muxSvcTable,
       "muxServiceEntry": muxServiceEntry,
       "muxID": muxID,
       "muxDescription": muxDescription,
       "muxVersion": muxVersion,
       "muxSequence": muxSequence,
       "muxAddress": muxAddress,
       "muxPreferred": muxPreferred,
       "muxSvcList": muxSvcList,
       "scte35Table": scte35Table,
       "scte35ReceiverEntry": scte35ReceiverEntry,
       "scte35Name": scte35Name,
       "scte35CueRecvTime": scte35CueRecvTime,
       "scte35Status": scte35Status,
       "scte35SuccessTime": scte35SuccessTime,
       "scte35FailTime": scte35FailTime,
       "scte35Error": scte35Error,
       "serviceSCTE35CueReceiverMapTable": serviceSCTE35CueReceiverMapTable,
       "serviceSCTE35CueReceiverMapEntry": serviceSCTE35CueReceiverMapEntry,
       "scte35CueSvcID": scte35CueSvcID,
       "scte35CueSvcName": scte35CueSvcName,
       "scte35CueSvcZone": scte35CueSvcZone,
       "scte35CueSvcPID": scte35CueSvcPID,
       "scte35CueReceiverAddr": scte35CueReceiverAddr,
       "cueConnectTable": cueConnectTable,
       "cueConnectEntry": cueConnectEntry,
       "cueSvcID": cueSvcID,
       "cueSvcName": cueSvcName,
       "cueSvcZone": cueSvcZone,
       "cueSvcMuxID": cueSvcMuxID,
       "cueSvcLastRecvTime": cueSvcLastRecvTime,
       "cueSvcStatus": cueSvcStatus,
       "cueSvcLastSuccess": cueSvcLastSuccess,
       "cueSvcLastFail": cueSvcLastFail,
       "cueSvcLastErr": cueSvcLastErr,
       "inbandConnectTable": inbandConnectTable,
       "inbandConnectEntry": inbandConnectEntry,
       "inSvcID": inSvcID,
       "inSvcName": inSvcName,
       "inSvcZone": inSvcZone,
       "inSvcPriAddress": inSvcPriAddress,
       "inSvcSecAddress": inSvcSecAddress,
       "inSvcTerAddress": inSvcTerAddress,
       "inSvcQuaAddress": inSvcQuaAddress,
       "inSvcVoteLastSendTime": inSvcVoteLastSendTime,
       "inSvcVlLastSendTime": inSvcVlLastSendTime,
       "inSvcBdLastSendTime": inSvcBdLastSendTime,
       "inSvcRTMLastSendTime": inSvcRTMLastSendTime,
       "inSvcCueLastSendTime": inSvcCueLastSendTime,
       "inSvcStatus": inSvcStatus,
       "inSvcLastSuccess": inSvcLastSuccess,
       "inSvcLastFail": inSvcLastFail,
       "inSvcLastErr": inSvcLastErr,
       "assetStateCheckTable": assetStateCheckTable,
       "assetStateCheckStatisticsEntry": assetStateCheckStatisticsEntry,
       "ascName": ascName,
       "ascStatus": ascStatus,
       "ascSuccesses": ascSuccesses,
       "ascSuccessTime": ascSuccessTime,
       "ascFailures": ascFailures,
       "ascFailTime": ascFailTime,
       "ascError": ascError,
       "bdsErrorTable": bdsErrorTable,
       "bdsErrorEntry": bdsErrorEntry,
       "bdsErrorTime": bdsErrorTime,
       "bdsErrorDescription": bdsErrorDescription,
       "svcWithNoUsableInsStreamsTable": svcWithNoUsableInsStreamsTable,
       "svcWithNoUsableInsStreamsEntry": svcWithNoUsableInsStreamsEntry,
       "noUsableInsStreamsSvcID": noUsableInsStreamsSvcID,
       "noUsableInsStreamsSvcName": noUsableInsStreamsSvcName,
       "noUsableInsStreamsSvcZone": noUsableInsStreamsSvcZone,
       "noUsableInsStreamsAvPID": noUsableInsStreamsAvPID,
       "noUsableInsStreamsAvPName": noUsableInsStreamsAvPName,
       "noUsableInsStreamsAVPCatID": noUsableInsStreamsAVPCatID,
       "noUsableInsStreamsAVPCatName": noUsableInsStreamsAVPCatName,
       "avProfCatMapTable": avProfCatMapTable,
       "avProfCatMapEntry": avProfCatMapEntry,
       "avProfCatID": avProfCatID,
       "avProfCatName": avProfCatName,
       "avProfCatFiller": avProfCatFiller,
       "avProfCatAVProfID": avProfCatAVProfID,
       "avProfCatAVProfName": avProfCatAVProfName,
       "avProfCatStreams": avProfCatStreams,
       "outBandDataMonitor": outBandDataMonitor,
       "carouselMonitorTable": carouselMonitorTable,
       "carouselMonitorEntry": carouselMonitorEntry,
       "messageType": messageType,
       "bytesTransfered": bytesTransfered,
       "messages": messages,
       "startTime": startTime,
       "averageRate": averageRate,
       "lastMessageTimeAndSize": lastMessageTimeAndSize,
       "fileDropStatusTable": fileDropStatusTable,
       "fileDropStatusEntry": fileDropStatusEntry,
       "fileType": fileType,
       "fileDropSegment": fileDropSegment,
       "fileDropCreationTime": fileDropCreationTime,
       "transferStatus": transferStatus,
       "transferSuccesses": transferSuccesses,
       "transferSuccessTime": transferSuccessTime,
       "transferFailures": transferFailures,
       "transferFailTime": transferFailTime,
       "transferError": transferError,
       "dssStatusStatisticsTable": dssStatusStatisticsTable,
       "dssStatusStatisticsEntry": dssStatusStatisticsEntry,
       "dssStatus": dssStatus,
       "targetUpdateStatusTable": targetUpdateStatusTable,
       "targetUpdateStatusEntry": targetUpdateStatusEntry,
       "targetUpdateName": targetUpdateName,
       "targetUpdateStatus": targetUpdateStatus,
       "targetUpdateSuccesses": targetUpdateSuccesses,
       "targetUpdateSuccessTime": targetUpdateSuccessTime,
       "targetUpdateFailures": targetUpdateFailures,
       "targetUpdateFailTime": targetUpdateFailTime,
       "targetUpdateError": targetUpdateError,
       "adoAloCreationStatusTable": adoAloCreationStatusTable,
       "adoAloCreationStatusEntry": adoAloCreationStatusEntry,
       "adoAloCreationName": adoAloCreationName,
       "adoAloCreationStatus": adoAloCreationStatus,
       "adoAloCreationSuccesses": adoAloCreationSuccesses,
       "adoAloCreationSuccessTime": adoAloCreationSuccessTime,
       "adoAloCreationFailures": adoAloCreationFailures,
       "adoAloCreationFailTime": adoAloCreationFailTime,
       "adoAloCreationError": adoAloCreationError,
       "prioritizerAssetPushStatusTable": prioritizerAssetPushStatusTable,
       "prioritizerAssetPushStatusEntry": prioritizerAssetPushStatusEntry,
       "prioritizerAssetPushName": prioritizerAssetPushName,
       "prioritizerAssetPushStatus": prioritizerAssetPushStatus,
       "prioritizerAssetPushSuccesses": prioritizerAssetPushSuccesses,
       "prioritizerAssetPushSuccessTime": prioritizerAssetPushSuccessTime,
       "prioritizerAssetPushFailures": prioritizerAssetPushFailures,
       "prioritizerAssetPushFailTime": prioritizerAssetPushFailTime,
       "prioritizerAssetPushError": prioritizerAssetPushError,
       "dssErrorTable": dssErrorTable,
       "dssErrorEntry": dssErrorEntry,
       "dssErrorTime": dssErrorTime,
       "dssErrorDescription": dssErrorDescription,
       "rcsInterface": rcsInterface,
       "processingStatusStatisticsTable": processingStatusStatisticsTable,
       "processingStatusStatisticsEntry": processingStatusStatisticsEntry,
       "eventTime": eventTime,
       "eventDescription": eventDescription,
       "interactiveFromTable": interactiveFromTable,
       "interactiveFromStatisticsEntry": interactiveFromStatisticsEntry,
       "fromMessageType": fromMessageType,
       "fromBytesTransfered": fromBytesTransfered,
       "fromMessages": fromMessages,
       "fromStartTime": fromStartTime,
       "fromAverageRate": fromAverageRate,
       "fromLastMessageTimeAndSize": fromLastMessageTimeAndSize,
       "interactiveToTable": interactiveToTable,
       "interactiveToStatisticsEntry": interactiveToStatisticsEntry,
       "toMessageType": toMessageType,
       "toBytesTransfered": toBytesTransfered,
       "toMessages": toMessages,
       "toStartTime": toStartTime,
       "toAverageRate": toAverageRate,
       "toLastMessageTimeAndSize": toLastMessageTimeAndSize,
       "stbReturnTable": stbReturnTable,
       "stbReturnEntry": stbReturnEntry,
       "numberOfConnectRetries": numberOfConnectRetries,
       "numberOfResends": numberOfResends,
       "numberOfV1AliveMessages": numberOfV1AliveMessages,
       "percentageOfV1AliveMessages": percentageOfV1AliveMessages,
       "setTopStatisticsTable": setTopStatisticsTable,
       "setTopStatisticsEntry": setTopStatisticsEntry,
       "boxID": boxID,
       "messagesCount": messagesCount,
       "exposedDateTime": exposedDateTime,
       "dateRequestAndTime": dateRequestAndTime,
       "lastAdPlayed": lastAdPlayed,
       "returnStats": returnStats,
       "lastMessage": lastMessage,
       "unknownSetTopsTable": unknownSetTopsTable,
       "unknownSetTopsEntry": unknownSetTopsEntry,
       "boxIDUnknown": boxIDUnknown,
       "requestTime": requestTime,
       "clickStatisticsTable": clickStatisticsTable,
       "clickStatisticsEntry": clickStatisticsEntry,
       "clickStatus": clickStatus,
       "clickSuccesses": clickSuccesses,
       "clickLastSuccessTime": clickLastSuccessTime,
       "clickFailures": clickFailures,
       "clickLastFailureTime": clickLastFailureTime,
       "clickLastError": clickLastError,
       "rawAdnFileCreationTable": rawAdnFileCreationTable,
       "rawAdnFileCreationEntry": rawAdnFileCreationEntry,
       "rawAdnFileCreationFileshare": rawAdnFileCreationFileshare,
       "rawAdnFileCreationRetrieval": rawAdnFileCreationRetrieval,
       "rawAdnFileCreationSuccess": rawAdnFileCreationSuccess,
       "rawAdnFileCreationLastSuccess": rawAdnFileCreationLastSuccess,
       "rawAdnFileCreationFailure": rawAdnFileCreationFailure,
       "rawAdnFileCreationLastFailure": rawAdnFileCreationLastFailure,
       "rawAdnFileCreationLastError": rawAdnFileCreationLastError,
       "rawAdnFileTransferTable": rawAdnFileTransferTable,
       "rawAdnFileTransferEntry": rawAdnFileTransferEntry,
       "rawAdnFileTransferFileshare": rawAdnFileTransferFileshare,
       "rawAdnFileTransferRetrieval": rawAdnFileTransferRetrieval,
       "rawAdnFileTransferSuccess": rawAdnFileTransferSuccess,
       "rawAdnFileTransferLastSuccess": rawAdnFileTransferLastSuccess,
       "rawAdnFileTransferFailure": rawAdnFileTransferFailure,
       "rawAdnFileTransferLastFailure": rawAdnFileTransferLastFailure,
       "rawAdnFileTransferLastError": rawAdnFileTransferLastError,
       "vmStatisticsTable": vmStatisticsTable,
       "vmStatisticsEntry": vmStatisticsEntry,
       "vmIP": vmIP,
       "vmRetrieval": vmRetrieval,
       "vmSuccess": vmSuccess,
       "vmLastSuccess": vmLastSuccess,
       "vmFailure": vmFailure,
       "vmLastFailure": vmLastFailure,
       "vmLastError": vmLastError,
       "amsStatisticsTable": amsStatisticsTable,
       "amsStatisticsEntry": amsStatisticsEntry,
       "amsFileshare": amsFileshare,
       "amsRetrieval": amsRetrieval,
       "amsSuccess": amsSuccess,
       "amsLastSuccess": amsLastSuccess,
       "amsFailure": amsFailure,
       "amsLastFailure": amsLastFailure,
       "amsLastError": amsLastError,
       "rcsErrorTable": rcsErrorTable,
       "rcsErrorEntry": rcsErrorEntry,
       "rcsErrorTime": rcsErrorTime,
       "rcsErrorDescription": rcsErrorDescription,
       "inboundVotesStatisticsTable": inboundVotesStatisticsTable,
       "inboundVotesStatisticsEntry": inboundVotesStatisticsEntry,
       "inboundVotesRcsAddress": inboundVotesRcsAddress,
       "inboundVoteMsgReceivedCount": inboundVoteMsgReceivedCount,
       "inboundVoteMsgLastRecevied": inboundVoteMsgLastRecevied,
       "inboundVoteMsgFailureCount": inboundVoteMsgFailureCount,
       "inboundVoteMsgLastFailureTime": inboundVoteMsgLastFailureTime,
       "inboundVotesLastError": inboundVotesLastError,
       "outboundVotesStatisticsTable": outboundVotesStatisticsTable,
       "outboundVotesStatisticsEntry": outboundVotesStatisticsEntry,
       "outboundVotesBdsAddress": outboundVotesBdsAddress,
       "outboundVoteMsgSentCount": outboundVoteMsgSentCount,
       "outboundVoteMsgLastSent": outboundVoteMsgLastSent,
       "outboundVoteMsgDropCount": outboundVoteMsgDropCount,
       "outboundVoteMsgLastDrop": outboundVoteMsgLastDrop,
       "outboundVoteMsgFailureCount": outboundVoteMsgFailureCount,
       "outboundVoteMsgLastFailureTime": outboundVoteMsgLastFailureTime,
       "outboundVotesLastError": outboundVotesLastError,
       "votingSessionsStatisticsTable": votingSessionsStatisticsTable,
       "votingSessionsStatisticsEntry": votingSessionsStatisticsEntry,
       "votingSessionSessionID": votingSessionSessionID,
       "votingSessionBreakID": votingSessionBreakID,
       "votingSessionBdsAddress": votingSessionBdsAddress,
       "votingSessionVoteEndTime": votingSessionVoteEndTime,
       "invidiConformance": invidiConformance,
       "invidiMIBGroups": invidiMIBGroups,
       "pageStatusGroup": pageStatusGroup,
       "bdmsInterfaceGroup": bdmsInterfaceGroup,
       "inbandDataMonitorGroup": inbandDataMonitorGroup,
       "cueToneStatisticsGroup": cueToneStatisticsGroup,
       "inbandDataStatisticsGroup": inbandDataStatisticsGroup,
       "unplayedBreakGroup": unplayedBreakGroup,
       "discardedBreakGroup": discardedBreakGroup,
       "assetErrorGroup": assetErrorGroup,
       "adInserterStatisticsGroup": adInserterStatisticsGroup,
       "insertionStreamConfigGroup": insertionStreamConfigGroup,
       "virtualStreamConfigGroup": virtualStreamConfigGroup,
       "amsStatisticsPlantIFGroup": amsStatisticsPlantIFGroup,
       "svcAdvertisementConnectionGroup": svcAdvertisementConnectionGroup,
       "serviceMuxListGroup": serviceMuxListGroup,
       "scte35ReceiverConnectionGroup": scte35ReceiverConnectionGroup,
       "serviceCueConnectionGroup": serviceCueConnectionGroup,
       "serviceInbandConnectionGroup": serviceInbandConnectionGroup,
       "assetStateCheckStatisticsGroup": assetStateCheckStatisticsGroup,
       "bdsErrorGroup": bdsErrorGroup,
       "svcWithNoUsableInsertStreamGroup": svcWithNoUsableInsertStreamGroup,
       "avProfileCategoryMappingGroup": avProfileCategoryMappingGroup,
       "carouselMonitorGroup": carouselMonitorGroup,
       "fileDropStatusGroup": fileDropStatusGroup,
       "dssStatusStatisticsGroup": dssStatusStatisticsGroup,
       "targetUpdateStatusGroup": targetUpdateStatusGroup,
       "serviceSCTE35CueReceiverMapGroup": serviceSCTE35CueReceiverMapGroup,
       "adoAloCreationStatusGroup": adoAloCreationStatusGroup,
       "prioritizerAssetPushStatusGroup": prioritizerAssetPushStatusGroup,
       "dssErrorGroup": dssErrorGroup,
       "processingStatusStatisticsGroup": processingStatusStatisticsGroup,
       "interactiveFromStatisticsGroup": interactiveFromStatisticsGroup,
       "interactiveToStatisticsGroup": interactiveToStatisticsGroup,
       "stbReturnStatisticsGroup": stbReturnStatisticsGroup,
       "stbStatisticsGroup": stbStatisticsGroup,
       "unknownSetTopsGroup": unknownSetTopsGroup,
       "clickStatisticsGroup": clickStatisticsGroup,
       "rawAdnFileCreationGroup": rawAdnFileCreationGroup,
       "rawAdnFileTransferGroup": rawAdnFileTransferGroup,
       "viewerMeasurementStatisticsGroup": viewerMeasurementStatisticsGroup,
       "amsStatisticsGroup": amsStatisticsGroup,
       "rcsErrorGroup": rcsErrorGroup,
       "inboundVotesStatisticsGroup": inboundVotesStatisticsGroup,
       "outboundVotesStatisticsGroup": outboundVotesStatisticsGroup,
       "votingSessionsStatisticsGroup": votingSessionsStatisticsGroup,
       "notificationObjectsGroup": notificationObjectsGroup,
       "trapNotificationGroup": trapNotificationGroup,
       "invidiMIBCompliances": invidiMIBCompliances,
       "invidiMIBCompliance": invidiMIBCompliance}
)
