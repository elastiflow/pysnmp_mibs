# SNMP MIB module (RideOnTrack-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/rideontrack_49797/RideOnTrack-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:55:50 2025
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

(hrSystem,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrSystem")

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
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "mib-2",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rideOnTrack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 49797)
)
if mibBuilder.loadTexts:
    rideOnTrack.setRevisions(
        ("2017-04-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)
_SysUpTime_Type = TimeTicks
_SysUpTime_Object = MibScalar
sysUpTime = _SysUpTime_Object(
    (1, 3, 6, 1, 2, 1, 1, 3),
    _SysUpTime_Type()
)
sysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpTime.setStatus("current")
_HrSystemDate_Type = OctetString
_HrSystemDate_Object = MibScalar
hrSystemDate = _HrSystemDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 2),
    _HrSystemDate_Type()
)
hrSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemDate.setStatus("current")
_TrapVariables_ObjectIdentity = ObjectIdentity
trapVariables = _TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49797, 1)
)
_ApplicationName_Type = OctetString
_ApplicationName_Object = MibScalar
applicationName = _ApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 1),
    _ApplicationName_Type()
)
applicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationName.setStatus("current")
_ApplicationVersion_Type = OctetString
_ApplicationVersion_Object = MibScalar
applicationVersion = _ApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 2),
    _ApplicationVersion_Type()
)
applicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationVersion.setStatus("current")
_SiteName_Type = OctetString
_SiteName_Object = MibScalar
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 3),
    _SiteName_Type()
)
siteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteName.setStatus("current")
_ServerIPAddress_Type = IpAddress
_ServerIPAddress_Object = MibScalar
serverIPAddress = _ServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 4),
    _ServerIPAddress_Type()
)
serverIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIPAddress.setStatus("current")
_SwBusComponent_Type = OctetString
_SwBusComponent_Object = MibScalar
swBusComponent = _SwBusComponent_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 5),
    _SwBusComponent_Type()
)
swBusComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBusComponent.setStatus("current")
_ServerIdentity_Type = OctetString
_ServerIdentity_Object = MibScalar
serverIdentity = _ServerIdentity_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 6),
    _ServerIdentity_Type()
)
serverIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIdentity.setStatus("current")


class _AlarmPriority_Type(Integer32):
    """Custom type alarmPriority based on Integer32"""
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
        *(("critical", 1),
          ("warning", 2),
          ("informational", 3),
          ("clear", 4))
    )


_AlarmPriority_Type.__name__ = "Integer32"
_AlarmPriority_Object = MibScalar
alarmPriority = _AlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 7),
    _AlarmPriority_Type()
)
alarmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPriority.setStatus("current")
_AlarmDateTime_Type = OctetString
_AlarmDateTime_Object = MibScalar
alarmDateTime = _AlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 8),
    _AlarmDateTime_Type()
)
alarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDateTime.setStatus("current")


class _RestartReason_Type(Integer32):
    """Custom type restartReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("userRequest", 1),
          ("noAppResponse", 2),
          ("threadError", 3))
    )


_RestartReason_Type.__name__ = "Integer32"
_RestartReason_Object = MibScalar
restartReason = _RestartReason_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 9),
    _RestartReason_Type()
)
restartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartReason.setStatus("current")


class _NoAppResponseReason_Type(Integer32):
    """Custom type noAppResponseReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("notAbleToOpenProcess", 1),
          ("notAbleToTerminateProcess", 2))
    )


_NoAppResponseReason_Type.__name__ = "Integer32"
_NoAppResponseReason_Object = MibScalar
noAppResponseReason = _NoAppResponseReason_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 10),
    _NoAppResponseReason_Type()
)
noAppResponseReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noAppResponseReason.setStatus("current")
_TrapDescription_Type = OctetString
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 11),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("current")


class _LinkConnectionState_Type(Integer32):
    """Custom type linkConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disConnected", 1),
          ("startUp", 2),
          ("connected", 3),
          ("waitForSync", 4),
          ("undefined", 5))
    )


_LinkConnectionState_Type.__name__ = "Integer32"
_LinkConnectionState_Object = MibScalar
linkConnectionState = _LinkConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 12),
    _LinkConnectionState_Type()
)
linkConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkConnectionState.setStatus("current")


class _SignallingType_Type(Integer32):
    """Custom type signallingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("cas", 1),
          ("ccsIsdnEtsi", 2),
          ("ccsGsmrTs0010", 3),
          ("ccsGsmrTs102", 4),
          ("ccsQsig", 5))
    )


_SignallingType_Type.__name__ = "Integer32"
_SignallingType_Object = MibScalar
signallingType = _SignallingType_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 13),
    _SignallingType_Type()
)
signallingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallingType.setStatus("current")


class _PrimaryRateState_Type(Integer32):
    """Custom type primaryRateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("unknown", 3))
    )


_PrimaryRateState_Type.__name__ = "Integer32"
_PrimaryRateState_Object = MibScalar
primaryRateState = _PrimaryRateState_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 14),
    _PrimaryRateState_Type()
)
primaryRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryRateState.setStatus("current")


class _SignallingState_Type(Integer32):
    """Custom type signallingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("down", 1),
          ("suspended", 2),
          ("up", 3),
          ("downInv", 4))
    )


_SignallingState_Type.__name__ = "Integer32"
_SignallingState_Object = MibScalar
signallingState = _SignallingState_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 15),
    _SignallingState_Type()
)
signallingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallingState.setStatus("current")


class _ResourceType_Type(Integer32):
    """Custom type resourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("cpu", 1),
          ("memory", 2),
          ("disk", 3),
          ("reserved", 4))
    )


_ResourceType_Type.__name__ = "Integer32"
_ResourceType_Object = MibScalar
resourceType = _ResourceType_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 16),
    _ResourceType_Type()
)
resourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceType.setStatus("current")
_ThresholdValue_Type = Integer32
_ThresholdValue_Object = MibScalar
thresholdValue = _ThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 17),
    _ThresholdValue_Type()
)
thresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdValue.setStatus("current")


class _ThresholdWatermark_Type(Integer32):
    """Custom type thresholdWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("aboveThreshold", 1),
          ("belowThreshold", 2))
    )


_ThresholdWatermark_Type.__name__ = "Integer32"
_ThresholdWatermark_Object = MibScalar
thresholdWatermark = _ThresholdWatermark_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 18),
    _ThresholdWatermark_Type()
)
thresholdWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdWatermark.setStatus("current")
_SupervisedApplicationName_Type = OctetString
_SupervisedApplicationName_Object = MibScalar
supervisedApplicationName = _SupervisedApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 19),
    _SupervisedApplicationName_Type()
)
supervisedApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supervisedApplicationName.setStatus("current")
_AlarmCode_Type = Integer32
_AlarmCode_Object = MibScalar
alarmCode = _AlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 20),
    _AlarmCode_Type()
)
alarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCode.setStatus("current")


class _ConnectionType_Type(Integer32):
    """Custom type connectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("server", 0),
          ("dica", 1),
          ("voiceRecorder", 2),
          ("gateway", 3),
          ("playback", 4),
          ("simulator", 5),
          ("mailoffice", 6),
          ("remoteCmdExec", 7),
          ("mediationDevice", 8))
    )


_ConnectionType_Type.__name__ = "Integer32"
_ConnectionType_Object = MibScalar
connectionType = _ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 21),
    _ConnectionType_Type()
)
connectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionType.setStatus("current")


class _LinkNumber_Type(Integer32):
    """Custom type linkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LinkNumber_Type.__name__ = "Integer32"
_LinkNumber_Object = MibScalar
linkNumber = _LinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 22),
    _LinkNumber_Type()
)
linkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumber.setStatus("current")
_RemoteIdentity_Type = OctetString
_RemoteIdentity_Object = MibScalar
remoteIdentity = _RemoteIdentity_Object(
    (1, 3, 6, 1, 4, 1, 49797, 1, 23),
    _RemoteIdentity_Type()
)
remoteIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIdentity.setStatus("current")
_SnmpAlarmNextIndex_ObjectIdentity = ObjectIdentity
snmpAlarmNextIndex = _SnmpAlarmNextIndex_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 1)
)
_SnmpMIBObjects_ObjectIdentity = ObjectIdentity
snmpMIBObjects = _SnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 1, 1)
)
_SnmpTrap_ObjectIdentity = ObjectIdentity
snmpTrap = _SnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 1, 1, 4)
)
_SnmpTrapOID_Type = ObjectIdentifier
_SnmpTrapOID_Object = MibScalar
snmpTrapOID = _SnmpTrapOID_Object(
    (1, 3, 6, 1, 6, 3, 1, 1, 4, 1),
    _SnmpTrapOID_Type()
)
snmpTrapOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snmpTrapOID.setStatus("current")

# Managed Objects groups

trapVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 49797, 8)
)
trapVariablesGroup.setObjects(
      *(("RideOnTrack-MIB", "applicationName"),
        ("RideOnTrack-MIB", "applicationVersion"),
        ("RideOnTrack-MIB", "siteName"),
        ("RideOnTrack-MIB", "serverIPAddress"),
        ("RideOnTrack-MIB", "swBusComponent"),
        ("RideOnTrack-MIB", "serverIdentity"),
        ("RideOnTrack-MIB", "alarmPriority"),
        ("RideOnTrack-MIB", "alarmDateTime"),
        ("RideOnTrack-MIB", "restartReason"),
        ("RideOnTrack-MIB", "noAppResponseReason"),
        ("RideOnTrack-MIB", "trapDescription"),
        ("RideOnTrack-MIB", "linkConnectionState"),
        ("RideOnTrack-MIB", "signallingType"),
        ("RideOnTrack-MIB", "primaryRateState"),
        ("RideOnTrack-MIB", "signallingState"),
        ("RideOnTrack-MIB", "resourceType"),
        ("RideOnTrack-MIB", "thresholdValue"),
        ("RideOnTrack-MIB", "thresholdWatermark"),
        ("RideOnTrack-MIB", "supervisedApplicationName"),
        ("RideOnTrack-MIB", "alarmCode"),
        ("RideOnTrack-MIB", "connectionType"),
        ("RideOnTrack-MIB", "linkNumber"),
        ("RideOnTrack-MIB", "remoteIdentity"),
        ("RideOnTrack-MIB", "sysUpTime"),
        ("RideOnTrack-MIB", "snmpTrapOID"),
        ("RideOnTrack-MIB", "hrSystemDate"))
)
if mibBuilder.loadTexts:
    trapVariablesGroup.setStatus("current")


# Notification objects

appSupervisorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 49797, 2)
)
appSupervisorTrap.setObjects(
      *(("RideOnTrack-MIB", "sysUpTime"),
        ("RideOnTrack-MIB", "snmpTrapOID"),
        ("RideOnTrack-MIB", "applicationName"),
        ("RideOnTrack-MIB", "applicationVersion"),
        ("RideOnTrack-MIB", "hrSystemDate"),
        ("RideOnTrack-MIB", "serverIdentity"),
        ("RideOnTrack-MIB", "alarmPriority"),
        ("RideOnTrack-MIB", "supervisedApplicationName"),
        ("RideOnTrack-MIB", "restartReason"),
        ("RideOnTrack-MIB", "noAppResponseReason"),
        ("RideOnTrack-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    appSupervisorTrap.setStatus(
        "current"
    )

appSupervisorHeartBeatNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 49797, 3)
)
appSupervisorHeartBeatNotification.setObjects(
      *(("RideOnTrack-MIB", "sysUpTime"),
        ("RideOnTrack-MIB", "snmpTrapOID"),
        ("RideOnTrack-MIB", "applicationName"),
        ("RideOnTrack-MIB", "applicationVersion"),
        ("RideOnTrack-MIB", "hrSystemDate"),
        ("RideOnTrack-MIB", "serverIdentity"),
        ("RideOnTrack-MIB", "alarmPriority"),
        ("RideOnTrack-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    appSupervisorHeartBeatNotification.setStatus(
        "current"
    )

applicationConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 49797, 4)
)
applicationConnectionTrap.setObjects(
      *(("RideOnTrack-MIB", "sysUpTime"),
        ("RideOnTrack-MIB", "snmpTrapOID"),
        ("RideOnTrack-MIB", "applicationName"),
        ("RideOnTrack-MIB", "applicationVersion"),
        ("RideOnTrack-MIB", "hrSystemDate"),
        ("RideOnTrack-MIB", "serverIdentity"),
        ("RideOnTrack-MIB", "alarmPriority"),
        ("RideOnTrack-MIB", "connectionType"),
        ("RideOnTrack-MIB", "linkConnectionState"),
        ("RideOnTrack-MIB", "remoteIdentity"),
        ("RideOnTrack-MIB", "swBusComponent"),
        ("RideOnTrack-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    applicationConnectionTrap.setStatus(
        "current"
    )

gatewayLinkConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 49797, 5)
)
gatewayLinkConnectionTrap.setObjects(
      *(("RideOnTrack-MIB", "sysUpTime"),
        ("RideOnTrack-MIB", "snmpTrapOID"),
        ("RideOnTrack-MIB", "applicationName"),
        ("RideOnTrack-MIB", "applicationVersion"),
        ("RideOnTrack-MIB", "hrSystemDate"),
        ("RideOnTrack-MIB", "serverIdentity"),
        ("RideOnTrack-MIB", "alarmPriority"),
        ("RideOnTrack-MIB", "linkNumber"),
        ("RideOnTrack-MIB", "signallingType"),
        ("RideOnTrack-MIB", "primaryRateState"),
        ("RideOnTrack-MIB", "signallingState"),
        ("RideOnTrack-MIB", "swBusComponent"),
        ("RideOnTrack-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    gatewayLinkConnectionTrap.setStatus(
        "current"
    )

resourceThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 49797, 6)
)
resourceThresholdTrap.setObjects(
      *(("RideOnTrack-MIB", "sysUpTime"),
        ("RideOnTrack-MIB", "snmpTrapOID"),
        ("RideOnTrack-MIB", "applicationName"),
        ("RideOnTrack-MIB", "applicationVersion"),
        ("RideOnTrack-MIB", "hrSystemDate"),
        ("RideOnTrack-MIB", "serverIdentity"),
        ("RideOnTrack-MIB", "alarmPriority"),
        ("RideOnTrack-MIB", "resourceType"),
        ("RideOnTrack-MIB", "thresholdValue"),
        ("RideOnTrack-MIB", "thresholdWatermark"),
        ("RideOnTrack-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    resourceThresholdTrap.setStatus(
        "current"
    )

sipConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 49797, 7)
)
sipConnectionTrap.setObjects(
      *(("RideOnTrack-MIB", "sysUpTime"),
        ("RideOnTrack-MIB", "snmpTrapOID"),
        ("RideOnTrack-MIB", "applicationName"),
        ("RideOnTrack-MIB", "applicationVersion"),
        ("RideOnTrack-MIB", "hrSystemDate"),
        ("RideOnTrack-MIB", "serverIdentity"),
        ("RideOnTrack-MIB", "alarmPriority"),
        ("RideOnTrack-MIB", "serverIPAddress"),
        ("RideOnTrack-MIB", "swBusComponent"),
        ("RideOnTrack-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    sipConnectionTrap.setStatus(
        "current"
    )


# Notifications groups

trapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 49797, 9)
)
trapGroup.setObjects(
      *(("RideOnTrack-MIB", "appSupervisorTrap"),
        ("RideOnTrack-MIB", "appSupervisorHeartBeatNotification"),
        ("RideOnTrack-MIB", "applicationConnectionTrap"),
        ("RideOnTrack-MIB", "gatewayLinkConnectionTrap"),
        ("RideOnTrack-MIB", "resourceThresholdTrap"),
        ("RideOnTrack-MIB", "sipConnectionTrap"))
)
if mibBuilder.loadTexts:
    trapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RideOnTrack-MIB",
    **{"system": system,
       "sysUpTime": sysUpTime,
       "hrSystemDate": hrSystemDate,
       "rideOnTrack": rideOnTrack,
       "trapVariables": trapVariables,
       "applicationName": applicationName,
       "applicationVersion": applicationVersion,
       "siteName": siteName,
       "serverIPAddress": serverIPAddress,
       "swBusComponent": swBusComponent,
       "serverIdentity": serverIdentity,
       "alarmPriority": alarmPriority,
       "alarmDateTime": alarmDateTime,
       "restartReason": restartReason,
       "noAppResponseReason": noAppResponseReason,
       "trapDescription": trapDescription,
       "linkConnectionState": linkConnectionState,
       "signallingType": signallingType,
       "primaryRateState": primaryRateState,
       "signallingState": signallingState,
       "resourceType": resourceType,
       "thresholdValue": thresholdValue,
       "thresholdWatermark": thresholdWatermark,
       "supervisedApplicationName": supervisedApplicationName,
       "alarmCode": alarmCode,
       "connectionType": connectionType,
       "linkNumber": linkNumber,
       "remoteIdentity": remoteIdentity,
       "appSupervisorTrap": appSupervisorTrap,
       "appSupervisorHeartBeatNotification": appSupervisorHeartBeatNotification,
       "applicationConnectionTrap": applicationConnectionTrap,
       "gatewayLinkConnectionTrap": gatewayLinkConnectionTrap,
       "resourceThresholdTrap": resourceThresholdTrap,
       "sipConnectionTrap": sipConnectionTrap,
       "trapVariablesGroup": trapVariablesGroup,
       "trapGroup": trapGroup,
       "snmpAlarmNextIndex": snmpAlarmNextIndex,
       "snmpMIBObjects": snmpMIBObjects,
       "snmpTrap": snmpTrap,
       "snmpTrapOID": snmpTrapOID}
)
