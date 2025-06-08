# SNMP MIB module (CISCO-PSBU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/broadware_28196/CISCO-PSBU-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:00:02 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

broadware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28196)
)
if mibBuilder.loadTexts:
    broadware.setRevisions(
        ("2007-01-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MediaStream_ObjectIdentity = ObjectIdentity
mediaStream = _MediaStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 2)
)
_MediaStreamNotifications_ObjectIdentity = ObjectIdentity
mediaStreamNotifications = _MediaStreamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 2, 0)
)
_MediaStreamObjects_ObjectIdentity = ObjectIdentity
mediaStreamObjects = _MediaStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 2, 1)
)
_MediaStreamName_Type = OctetString
_MediaStreamName_Object = MibScalar
mediaStreamName = _MediaStreamName_Object(
    (1, 3, 6, 1, 4, 1, 28196, 2, 1, 1),
    _MediaStreamName_Type()
)
mediaStreamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStreamName.setStatus("current")


class _MediaStreamState_Type(Integer32):
    """Custom type mediaStreamState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("start", 2),
          ("stop", 4))
    )


_MediaStreamState_Type.__name__ = "Integer32"
_MediaStreamState_Object = MibScalar
mediaStreamState = _MediaStreamState_Object(
    (1, 3, 6, 1, 4, 1, 28196, 2, 1, 2),
    _MediaStreamState_Type()
)
mediaStreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStreamState.setStatus("current")
_MediaStreamDescription_Type = OctetString
_MediaStreamDescription_Object = MibScalar
mediaStreamDescription = _MediaStreamDescription_Object(
    (1, 3, 6, 1, 4, 1, 28196, 2, 1, 3),
    _MediaStreamDescription_Type()
)
mediaStreamDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStreamDescription.setStatus("current")


class _MediaStreamConfigFailureComponent_Type(Integer32):
    """Custom type mediaStreamConfigFailureComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("stream", 2)
    )


_MediaStreamConfigFailureComponent_Type.__name__ = "Integer32"
_MediaStreamConfigFailureComponent_Object = MibScalar
mediaStreamConfigFailureComponent = _MediaStreamConfigFailureComponent_Object(
    (1, 3, 6, 1, 4, 1, 28196, 2, 1, 5),
    _MediaStreamConfigFailureComponent_Type()
)
mediaStreamConfigFailureComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStreamConfigFailureComponent.setStatus("current")
_MediaStreamConfigFailureDescription_Type = OctetString
_MediaStreamConfigFailureDescription_Object = MibScalar
mediaStreamConfigFailureDescription = _MediaStreamConfigFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 28196, 2, 1, 6),
    _MediaStreamConfigFailureDescription_Type()
)
mediaStreamConfigFailureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStreamConfigFailureDescription.setStatus("current")
_Recording_ObjectIdentity = ObjectIdentity
recording = _Recording_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 3)
)
_RecordingNotifications_ObjectIdentity = ObjectIdentity
recordingNotifications = _RecordingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 3, 0)
)
_RecordingObjects_ObjectIdentity = ObjectIdentity
recordingObjects = _RecordingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 3, 1)
)
_RecordingName_Type = OctetString
_RecordingName_Object = MibScalar
recordingName = _RecordingName_Object(
    (1, 3, 6, 1, 4, 1, 28196, 3, 1, 1),
    _RecordingName_Type()
)
recordingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordingName.setStatus("current")


class _RecordingInfo_Type(Integer32):
    """Custom type recordingInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("remove", 3),
          ("resume", 4),
          ("pause", 5),
          ("reset", 6),
          ("setevent", 7),
          ("update", 8),
          ("rename", 9))
    )


_RecordingInfo_Type.__name__ = "Integer32"
_RecordingInfo_Object = MibScalar
recordingInfo = _RecordingInfo_Object(
    (1, 3, 6, 1, 4, 1, 28196, 3, 1, 2),
    _RecordingInfo_Type()
)
recordingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordingInfo.setStatus("current")


class _RecordingFailureReason_Type(Integer32):
    """Custom type recordingFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("genErr", 6))
    )


_RecordingFailureReason_Type.__name__ = "Integer32"
_RecordingFailureReason_Object = MibScalar
recordingFailureReason = _RecordingFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 28196, 3, 1, 3),
    _RecordingFailureReason_Type()
)
recordingFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordingFailureReason.setStatus("current")
_RecordingDescription_Type = OctetString
_RecordingDescription_Object = MibScalar
recordingDescription = _RecordingDescription_Object(
    (1, 3, 6, 1, 4, 1, 28196, 3, 1, 4),
    _RecordingDescription_Type()
)
recordingDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordingDescription.setStatus("current")


class _RecordingFlag_Type(Integer32):
    """Custom type recordingFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RecordingFlag_Type.__name__ = "Integer32"
_RecordingFlag_Object = MibScalar
recordingFlag = _RecordingFlag_Object(
    (1, 3, 6, 1, 4, 1, 28196, 3, 1, 5),
    _RecordingFlag_Type()
)
recordingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordingFlag.setStatus("current")
_RecordingVolumeName_Type = OctetString
_RecordingVolumeName_Object = MibScalar
recordingVolumeName = _RecordingVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 28196, 3, 1, 6),
    _RecordingVolumeName_Type()
)
recordingVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordingVolumeName.setStatus("current")
_MediaServer_ObjectIdentity = ObjectIdentity
mediaServer = _MediaServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 4)
)
_MediaServerNotifications_ObjectIdentity = ObjectIdentity
mediaServerNotifications = _MediaServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 4, 0)
)
_MediaServerObjects_ObjectIdentity = ObjectIdentity
mediaServerObjects = _MediaServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 4, 1)
)


class _MediaServerState_Type(Integer32):
    """Custom type mediaServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("partial", 3))
    )


_MediaServerState_Type.__name__ = "Integer32"
_MediaServerState_Object = MibScalar
mediaServerState = _MediaServerState_Object(
    (1, 3, 6, 1, 4, 1, 28196, 4, 1, 1),
    _MediaServerState_Type()
)
mediaServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaServerState.setStatus("current")
_MediaServerIfName_Type = OctetString
_MediaServerIfName_Object = MibScalar
mediaServerIfName = _MediaServerIfName_Object(
    (1, 3, 6, 1, 4, 1, 28196, 4, 1, 2),
    _MediaServerIfName_Type()
)
mediaServerIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaServerIfName.setStatus("current")
_MediaServerIfSpeed_Type = OctetString
_MediaServerIfSpeed_Object = MibScalar
mediaServerIfSpeed = _MediaServerIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28196, 4, 1, 3),
    _MediaServerIfSpeed_Type()
)
mediaServerIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaServerIfSpeed.setStatus("current")
_MediaServerIfThroughput_Type = OctetString
_MediaServerIfThroughput_Object = MibScalar
mediaServerIfThroughput = _MediaServerIfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 28196, 4, 1, 4),
    _MediaServerIfThroughput_Type()
)
mediaServerIfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaServerIfThroughput.setStatus("current")
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 5)
)
_GenericObjects_ObjectIdentity = ObjectIdentity
genericObjects = _GenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 5, 1)
)
_GenericTimeStamp_Type = OctetString
_GenericTimeStamp_Object = MibScalar
genericTimeStamp = _GenericTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 28196, 5, 1, 1),
    _GenericTimeStamp_Type()
)
genericTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTimeStamp.setStatus("current")
_ClockAdjustment_ObjectIdentity = ObjectIdentity
clockAdjustment = _ClockAdjustment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 6)
)
_ClockAdjustmentNotifications_ObjectIdentity = ObjectIdentity
clockAdjustmentNotifications = _ClockAdjustmentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 6, 0)
)
_ClockAdjustmentObjects_ObjectIdentity = ObjectIdentity
clockAdjustmentObjects = _ClockAdjustmentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 6, 1)
)


class _ClockAdjustmentState_Type(Integer32):
    """Custom type clockAdjustmentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("hcAdjToSc", 2)
    )


_ClockAdjustmentState_Type.__name__ = "Integer32"
_ClockAdjustmentState_Object = MibScalar
clockAdjustmentState = _ClockAdjustmentState_Object(
    (1, 3, 6, 1, 4, 1, 28196, 6, 1, 1),
    _ClockAdjustmentState_Type()
)
clockAdjustmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockAdjustmentState.setStatus("current")
_PsbuEventMIBConformance_ObjectIdentity = ObjectIdentity
psbuEventMIBConformance = _PsbuEventMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 16)
)
_PsbuEventMIBCompliances_ObjectIdentity = ObjectIdentity
psbuEventMIBCompliances = _PsbuEventMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 16, 1)
)
_PsbuEventMIBGroups_ObjectIdentity = ObjectIdentity
psbuEventMIBGroups = _PsbuEventMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2)
)

# Managed Objects groups

mediaStreamObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 1)
)
mediaStreamObjectGroup.setObjects(
      *(("CISCO-PSBU-MIB", "mediaStreamName"),
        ("CISCO-PSBU-MIB", "mediaStreamState"),
        ("CISCO-PSBU-MIB", "mediaStreamDescription"),
        ("CISCO-PSBU-MIB", "mediaStreamConfigFailureComponent"),
        ("CISCO-PSBU-MIB", "mediaStreamConfigFailureDescription"))
)
if mibBuilder.loadTexts:
    mediaStreamObjectGroup.setStatus("current")

recordingObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 2)
)
recordingObjectGroup.setObjects(
      *(("CISCO-PSBU-MIB", "recordingName"),
        ("CISCO-PSBU-MIB", "recordingInfo"),
        ("CISCO-PSBU-MIB", "recordingFailureReason"),
        ("CISCO-PSBU-MIB", "recordingDescription"),
        ("CISCO-PSBU-MIB", "recordingFlag"),
        ("CISCO-PSBU-MIB", "recordingVolumeName"))
)
if mibBuilder.loadTexts:
    recordingObjectGroup.setStatus("current")

mediaServerObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 3)
)
mediaServerObjectGroup.setObjects(
      *(("CISCO-PSBU-MIB", "mediaServerState"),
        ("CISCO-PSBU-MIB", "mediaServerIfName"),
        ("CISCO-PSBU-MIB", "mediaServerIfSpeed"),
        ("CISCO-PSBU-MIB", "mediaServerIfThroughput"))
)
if mibBuilder.loadTexts:
    mediaServerObjectGroup.setStatus("current")

genericObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 4)
)
genericObjectGroup.setObjects(
    ("CISCO-PSBU-MIB", "genericTimeStamp")
)
if mibBuilder.loadTexts:
    genericObjectGroup.setStatus("current")

clockAdjustmentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 8)
)
clockAdjustmentObjectGroup.setObjects(
    ("CISCO-PSBU-MIB", "clockAdjustmentState")
)
if mibBuilder.loadTexts:
    clockAdjustmentObjectGroup.setStatus("current")


# Notification objects

mediaStreamStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 2, 0, 1)
)
mediaStreamStateChange.setObjects(
      *(("CISCO-PSBU-MIB", "mediaStreamName"),
        ("CISCO-PSBU-MIB", "mediaStreamState"),
        ("CISCO-PSBU-MIB", "mediaStreamDescription"))
)
if mibBuilder.loadTexts:
    mediaStreamStateChange.setStatus(
        "current"
    )

mediaStreamDeviceUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 2, 0, 2)
)
mediaStreamDeviceUnreachable.setObjects(
    ("CISCO-PSBU-MIB", "mediaStreamName")
)
if mibBuilder.loadTexts:
    mediaStreamDeviceUnreachable.setStatus(
        "current"
    )

mediaStreamConnectionLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 2, 0, 3)
)
mediaStreamConnectionLoss.setObjects(
    ("CISCO-PSBU-MIB", "mediaStreamName")
)
if mibBuilder.loadTexts:
    mediaStreamConnectionLoss.setStatus(
        "current"
    )

mediaStreamConfigFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 2, 0, 5)
)
mediaStreamConfigFailure.setObjects(
      *(("CISCO-PSBU-MIB", "mediaStreamName"),
        ("CISCO-PSBU-MIB", "mediaStreamConfigFailureComponent"),
        ("CISCO-PSBU-MIB", "mediaStreamConfigFailureDescription"))
)
if mibBuilder.loadTexts:
    mediaStreamConfigFailure.setStatus(
        "current"
    )

recordingStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 3, 0, 1)
)
recordingStatus.setObjects(
      *(("CISCO-PSBU-MIB", "recordingName"),
        ("CISCO-PSBU-MIB", "recordingInfo"),
        ("CISCO-PSBU-MIB", "recordingFailureReason"),
        ("CISCO-PSBU-MIB", "recordingDescription"))
)
if mibBuilder.loadTexts:
    recordingStatus.setStatus(
        "current"
    )

recordingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 3, 0, 3)
)
recordingFailure.setObjects(
    ("CISCO-PSBU-MIB", "recordingName")
)
if mibBuilder.loadTexts:
    recordingFailure.setStatus(
        "current"
    )

recordingOverSubscribed = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 3, 0, 4)
)
recordingOverSubscribed.setObjects(
    ("CISCO-PSBU-MIB", "recordingVolumeName")
)
if mibBuilder.loadTexts:
    recordingOverSubscribed.setStatus(
        "current"
    )

recordingBootstrapFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 3, 0, 5)
)
recordingBootstrapFailure.setObjects(
    ("CISCO-PSBU-MIB", "recordingFlag")
)
if mibBuilder.loadTexts:
    recordingBootstrapFailure.setStatus(
        "current"
    )

mediaServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 4, 0, 1)
)
mediaServerStateChange.setObjects(
    ("CISCO-PSBU-MIB", "mediaServerState")
)
if mibBuilder.loadTexts:
    mediaServerStateChange.setStatus(
        "current"
    )

mediaServerBandwidthLimitExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 4, 0, 2)
)
mediaServerBandwidthLimitExceed.setObjects(
      *(("CISCO-PSBU-MIB", "mediaServerIfName"),
        ("CISCO-PSBU-MIB", "mediaServerIfSpeed"),
        ("CISCO-PSBU-MIB", "mediaServerIfThroughput"))
)
if mibBuilder.loadTexts:
    mediaServerBandwidthLimitExceed.setStatus(
        "current"
    )

clockAdjustmentStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28196, 6, 0, 1)
)
clockAdjustmentStatusChange.setObjects(
    ("CISCO-PSBU-MIB", "clockAdjustmentState")
)
if mibBuilder.loadTexts:
    clockAdjustmentStatusChange.setStatus(
        "current"
    )


# Notifications groups

mediaStreamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 5)
)
mediaStreamNotificationGroup.setObjects(
      *(("CISCO-PSBU-MIB", "mediaStreamStateChange"),
        ("CISCO-PSBU-MIB", "mediaStreamDeviceUnreachable"),
        ("CISCO-PSBU-MIB", "mediaStreamConnectionLoss"),
        ("CISCO-PSBU-MIB", "mediaStreamConfigFailure"))
)
if mibBuilder.loadTexts:
    mediaStreamNotificationGroup.setStatus(
        "current"
    )

recordingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 6)
)
recordingNotificationGroup.setObjects(
      *(("CISCO-PSBU-MIB", "recordingStatus"),
        ("CISCO-PSBU-MIB", "recordingFailure"),
        ("CISCO-PSBU-MIB", "recordingOverSubscribed"),
        ("CISCO-PSBU-MIB", "recordingBootstrapFailure"))
)
if mibBuilder.loadTexts:
    recordingNotificationGroup.setStatus(
        "current"
    )

mediaServerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 7)
)
mediaServerNotificationGroup.setObjects(
      *(("CISCO-PSBU-MIB", "mediaServerState"),
        ("CISCO-PSBU-MIB", "mediaServerBandwidthLimitExceed"))
)
if mibBuilder.loadTexts:
    mediaServerNotificationGroup.setStatus(
        "current"
    )

clockAdjustmentNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28196, 16, 2, 9)
)
clockAdjustmentNotificationGroup.setObjects(
    ("CISCO-PSBU-MIB", "clockAdjustmentStatusChange")
)
if mibBuilder.loadTexts:
    clockAdjustmentNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

psbuEventMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28196, 16, 1, 1)
)
psbuEventMIBFullCompliance.setObjects(
      *(("CISCO-PSBU-MIB", "mediaStreamObjectGroup"),
        ("CISCO-PSBU-MIB", "recordingObjectGroup"),
        ("CISCO-PSBU-MIB", "mediaServerObjectGroup"),
        ("CISCO-PSBU-MIB", "genericObjectGroup"),
        ("CISCO-PSBU-MIB", "mediaStreamNotificationGroup"),
        ("CISCO-PSBU-MIB", "recordingNotificationGroup"),
        ("CISCO-PSBU-MIB", "mediaServerNotificationGroup"),
        ("CISCO-PSBU-MIB", "clockAdjustmentObjectGroup"),
        ("CISCO-PSBU-MIB", "clockAdjustmentNotificationGroup"))
)
if mibBuilder.loadTexts:
    psbuEventMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PSBU-MIB",
    **{"broadware": broadware,
       "mediaStream": mediaStream,
       "mediaStreamNotifications": mediaStreamNotifications,
       "mediaStreamStateChange": mediaStreamStateChange,
       "mediaStreamDeviceUnreachable": mediaStreamDeviceUnreachable,
       "mediaStreamConnectionLoss": mediaStreamConnectionLoss,
       "mediaStreamConfigFailure": mediaStreamConfigFailure,
       "mediaStreamObjects": mediaStreamObjects,
       "mediaStreamName": mediaStreamName,
       "mediaStreamState": mediaStreamState,
       "mediaStreamDescription": mediaStreamDescription,
       "mediaStreamConfigFailureComponent": mediaStreamConfigFailureComponent,
       "mediaStreamConfigFailureDescription": mediaStreamConfigFailureDescription,
       "recording": recording,
       "recordingNotifications": recordingNotifications,
       "recordingStatus": recordingStatus,
       "recordingFailure": recordingFailure,
       "recordingOverSubscribed": recordingOverSubscribed,
       "recordingBootstrapFailure": recordingBootstrapFailure,
       "recordingObjects": recordingObjects,
       "recordingName": recordingName,
       "recordingInfo": recordingInfo,
       "recordingFailureReason": recordingFailureReason,
       "recordingDescription": recordingDescription,
       "recordingFlag": recordingFlag,
       "recordingVolumeName": recordingVolumeName,
       "mediaServer": mediaServer,
       "mediaServerNotifications": mediaServerNotifications,
       "mediaServerStateChange": mediaServerStateChange,
       "mediaServerBandwidthLimitExceed": mediaServerBandwidthLimitExceed,
       "mediaServerObjects": mediaServerObjects,
       "mediaServerState": mediaServerState,
       "mediaServerIfName": mediaServerIfName,
       "mediaServerIfSpeed": mediaServerIfSpeed,
       "mediaServerIfThroughput": mediaServerIfThroughput,
       "generic": generic,
       "genericObjects": genericObjects,
       "genericTimeStamp": genericTimeStamp,
       "clockAdjustment": clockAdjustment,
       "clockAdjustmentNotifications": clockAdjustmentNotifications,
       "clockAdjustmentStatusChange": clockAdjustmentStatusChange,
       "clockAdjustmentObjects": clockAdjustmentObjects,
       "clockAdjustmentState": clockAdjustmentState,
       "psbuEventMIBConformance": psbuEventMIBConformance,
       "psbuEventMIBCompliances": psbuEventMIBCompliances,
       "psbuEventMIBFullCompliance": psbuEventMIBFullCompliance,
       "psbuEventMIBGroups": psbuEventMIBGroups,
       "mediaStreamObjectGroup": mediaStreamObjectGroup,
       "recordingObjectGroup": recordingObjectGroup,
       "mediaServerObjectGroup": mediaServerObjectGroup,
       "genericObjectGroup": genericObjectGroup,
       "mediaStreamNotificationGroup": mediaStreamNotificationGroup,
       "recordingNotificationGroup": recordingNotificationGroup,
       "mediaServerNotificationGroup": mediaServerNotificationGroup,
       "clockAdjustmentObjectGroup": clockAdjustmentObjectGroup,
       "clockAdjustmentNotificationGroup": clockAdjustmentNotificationGroup}
)
