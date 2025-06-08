# SNMP MIB module (VIDYO-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vidyo_35969/VIDYO-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:06:55 2025
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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

vidyo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35969)
)
if mibBuilder.loadTexts:
    vidyo.setRevisions(
        ("2014-01-16 20:34",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VidyoMIBS_ObjectIdentity = ObjectIdentity
vidyoMIBS = _VidyoMIBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1)
)
_VidyoProducts_ObjectIdentity = ObjectIdentity
vidyoProducts = _VidyoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1)
)
_VidyoRouter_ObjectIdentity = ObjectIdentity
vidyoRouter = _VidyoRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1)
)
_VidyoRouterObjects_ObjectIdentity = ObjectIdentity
vidyoRouterObjects = _VidyoRouterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1)
)
_VidyoRouterNotificationObjects_ObjectIdentity = ObjectIdentity
vidyoRouterNotificationObjects = _VidyoRouterNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1)
)
_VidyoRouterNotificationCommonObj_ObjectIdentity = ObjectIdentity
vidyoRouterNotificationCommonObj = _VidyoRouterNotificationCommonObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1)
)
_VidyoRouterAlertTime_Type = OctetString
_VidyoRouterAlertTime_Object = MibScalar
vidyoRouterAlertTime = _VidyoRouterAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 2),
    _VidyoRouterAlertTime_Type()
)
vidyoRouterAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterAlertTime.setStatus("current")
_VidyoRouterConferenceId_Type = OctetString
_VidyoRouterConferenceId_Object = MibScalar
vidyoRouterConferenceId = _VidyoRouterConferenceId_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 3),
    _VidyoRouterConferenceId_Type()
)
vidyoRouterConferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterConferenceId.setStatus("current")
_VidyoRouterRemoteRouterId_Type = OctetString
_VidyoRouterRemoteRouterId_Object = MibScalar
vidyoRouterRemoteRouterId = _VidyoRouterRemoteRouterId_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 4),
    _VidyoRouterRemoteRouterId_Type()
)
vidyoRouterRemoteRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterRemoteRouterId.setStatus("current")
_VidyoRouterRemoteRouterUri_Type = OctetString
_VidyoRouterRemoteRouterUri_Object = MibScalar
vidyoRouterRemoteRouterUri = _VidyoRouterRemoteRouterUri_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 5),
    _VidyoRouterRemoteRouterUri_Type()
)
vidyoRouterRemoteRouterUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterRemoteRouterUri.setStatus("current")
_VidyoRouterParticipantId_Type = OctetString
_VidyoRouterParticipantId_Object = MibScalar
vidyoRouterParticipantId = _VidyoRouterParticipantId_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 6),
    _VidyoRouterParticipantId_Type()
)
vidyoRouterParticipantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterParticipantId.setStatus("current")
_VidyoRouterParticipantName_Type = OctetString
_VidyoRouterParticipantName_Object = MibScalar
vidyoRouterParticipantName = _VidyoRouterParticipantName_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 7),
    _VidyoRouterParticipantName_Type()
)
vidyoRouterParticipantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterParticipantName.setStatus("current")
_VidyoRouterParticipantUri_Type = OctetString
_VidyoRouterParticipantUri_Object = MibScalar
vidyoRouterParticipantUri = _VidyoRouterParticipantUri_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 8),
    _VidyoRouterParticipantUri_Type()
)
vidyoRouterParticipantUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterParticipantUri.setStatus("current")


class _VidyoRouterRtpRecvPacketLoss_Type(Unsigned32):
    """Custom type vidyoRouterRtpRecvPacketLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VidyoRouterRtpRecvPacketLoss_Type.__name__ = "Unsigned32"
_VidyoRouterRtpRecvPacketLoss_Object = MibScalar
vidyoRouterRtpRecvPacketLoss = _VidyoRouterRtpRecvPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 9),
    _VidyoRouterRtpRecvPacketLoss_Type()
)
vidyoRouterRtpRecvPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterRtpRecvPacketLoss.setStatus("current")
_VidyoRouterRtpRecvJitter_Type = Unsigned32
_VidyoRouterRtpRecvJitter_Object = MibScalar
vidyoRouterRtpRecvJitter = _VidyoRouterRtpRecvJitter_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 10),
    _VidyoRouterRtpRecvJitter_Type()
)
vidyoRouterRtpRecvJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterRtpRecvJitter.setStatus("current")
_VidyoRouterEvents_ObjectIdentity = ObjectIdentity
vidyoRouterEvents = _VidyoRouterEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 2)
)
_VidyoRouterMgmnt_ObjectIdentity = ObjectIdentity
vidyoRouterMgmnt = _VidyoRouterMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3)
)
_VidyoRouterId_Type = OctetString
_VidyoRouterId_Object = MibScalar
vidyoRouterId = _VidyoRouterId_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 2),
    _VidyoRouterId_Type()
)
vidyoRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterId.setStatus("current")
_VidyoRouterName_Type = OctetString
_VidyoRouterName_Object = MibScalar
vidyoRouterName = _VidyoRouterName_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 3),
    _VidyoRouterName_Type()
)
vidyoRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterName.setStatus("current")
_VidyoRouterAppVersion_Type = OctetString
_VidyoRouterAppVersion_Object = MibScalar
vidyoRouterAppVersion = _VidyoRouterAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 4),
    _VidyoRouterAppVersion_Type()
)
vidyoRouterAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterAppVersion.setStatus("current")
_VidyoRouterOsVersion_Type = OctetString
_VidyoRouterOsVersion_Object = MibScalar
vidyoRouterOsVersion = _VidyoRouterOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 5),
    _VidyoRouterOsVersion_Type()
)
vidyoRouterOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterOsVersion.setStatus("current")
_VidyoRouterRmcpVersion_Type = OctetString
_VidyoRouterRmcpVersion_Object = MibScalar
vidyoRouterRmcpVersion = _VidyoRouterRmcpVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 6),
    _VidyoRouterRmcpVersion_Type()
)
vidyoRouterRmcpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterRmcpVersion.setStatus("current")
_VidyoRouterLogicVersion_Type = OctetString
_VidyoRouterLogicVersion_Object = MibScalar
vidyoRouterLogicVersion = _VidyoRouterLogicVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 7),
    _VidyoRouterLogicVersion_Type()
)
vidyoRouterLogicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterLogicVersion.setStatus("current")
_VidyoRouterSdkVersion_Type = OctetString
_VidyoRouterSdkVersion_Object = MibScalar
vidyoRouterSdkVersion = _VidyoRouterSdkVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 8),
    _VidyoRouterSdkVersion_Type()
)
vidyoRouterSdkVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterSdkVersion.setStatus("current")
_VidyoRouterHardwareCode_Type = Unsigned32
_VidyoRouterHardwareCode_Object = MibScalar
vidyoRouterHardwareCode = _VidyoRouterHardwareCode_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 9),
    _VidyoRouterHardwareCode_Type()
)
vidyoRouterHardwareCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterHardwareCode.setStatus("current")
_VidyoRouterHardwareName_Type = OctetString
_VidyoRouterHardwareName_Object = MibScalar
vidyoRouterHardwareName = _VidyoRouterHardwareName_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 10),
    _VidyoRouterHardwareName_Type()
)
vidyoRouterHardwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterHardwareName.setStatus("current")
_VidyoRouterCapacity_Type = Unsigned32
_VidyoRouterCapacity_Object = MibScalar
vidyoRouterCapacity = _VidyoRouterCapacity_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 11),
    _VidyoRouterCapacity_Type()
)
vidyoRouterCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterCapacity.setStatus("current")
_VidyoRouterVmId_Type = OctetString
_VidyoRouterVmId_Object = MibScalar
vidyoRouterVmId = _VidyoRouterVmId_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 12),
    _VidyoRouterVmId_Type()
)
vidyoRouterVmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterVmId.setStatus("current")
_VidyoRouterVmAddress_Type = OctetString
_VidyoRouterVmAddress_Object = MibScalar
vidyoRouterVmAddress = _VidyoRouterVmAddress_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 13),
    _VidyoRouterVmAddress_Type()
)
vidyoRouterVmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterVmAddress.setStatus("current")
_VidyoRouterVmConnIsSecure_Type = TruthValue
_VidyoRouterVmConnIsSecure_Object = MibScalar
vidyoRouterVmConnIsSecure = _VidyoRouterVmConnIsSecure_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 14),
    _VidyoRouterVmConnIsSecure_Type()
)
vidyoRouterVmConnIsSecure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterVmConnIsSecure.setStatus("current")
_VidyoRouterVmSysVersion_Type = OctetString
_VidyoRouterVmSysVersion_Object = MibScalar
vidyoRouterVmSysVersion = _VidyoRouterVmSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 15),
    _VidyoRouterVmSysVersion_Type()
)
vidyoRouterVmSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterVmSysVersion.setStatus("current")
_VidyoRouterVmConnLost_Type = TruthValue
_VidyoRouterVmConnLost_Object = MibScalar
vidyoRouterVmConnLost = _VidyoRouterVmConnLost_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 16),
    _VidyoRouterVmConnLost_Type()
)
vidyoRouterVmConnLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterVmConnLost.setStatus("current")
_VidyoRouterVmConnLostCount_Type = Counter32
_VidyoRouterVmConnLostCount_Object = MibScalar
vidyoRouterVmConnLostCount = _VidyoRouterVmConnLostCount_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 17),
    _VidyoRouterVmConnLostCount_Type()
)
vidyoRouterVmConnLostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterVmConnLostCount.setStatus("current")
_VidyoRouterState_Type = OctetString
_VidyoRouterState_Object = MibScalar
vidyoRouterState = _VidyoRouterState_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 18),
    _VidyoRouterState_Type()
)
vidyoRouterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterState.setStatus("current")
_VidyoRouterStatus_Type = OctetString
_VidyoRouterStatus_Object = MibScalar
vidyoRouterStatus = _VidyoRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 19),
    _VidyoRouterStatus_Type()
)
vidyoRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterStatus.setStatus("current")
_VidyoRouterUptime_Type = Counter32
_VidyoRouterUptime_Object = MibScalar
vidyoRouterUptime = _VidyoRouterUptime_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 20),
    _VidyoRouterUptime_Type()
)
vidyoRouterUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterUptime.setStatus("current")
_VidyoRouterConferences_Type = Unsigned32
_VidyoRouterConferences_Object = MibScalar
vidyoRouterConferences = _VidyoRouterConferences_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 21),
    _VidyoRouterConferences_Type()
)
vidyoRouterConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterConferences.setStatus("current")
_VidyoRouterParticipants_Type = Unsigned32
_VidyoRouterParticipants_Object = MibScalar
vidyoRouterParticipants = _VidyoRouterParticipants_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 22),
    _VidyoRouterParticipants_Type()
)
vidyoRouterParticipants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterParticipants.setStatus("current")
_VidyoRouterCascades_Type = Unsigned32
_VidyoRouterCascades_Object = MibScalar
vidyoRouterCascades = _VidyoRouterCascades_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 23),
    _VidyoRouterCascades_Type()
)
vidyoRouterCascades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterCascades.setStatus("current")
_VidyoRouterActiveParticipants_Type = Unsigned32
_VidyoRouterActiveParticipants_Object = MibScalar
vidyoRouterActiveParticipants = _VidyoRouterActiveParticipants_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 24),
    _VidyoRouterActiveParticipants_Type()
)
vidyoRouterActiveParticipants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterActiveParticipants.setStatus("current")
_VidyoRouterActiveCascades_Type = Unsigned32
_VidyoRouterActiveCascades_Object = MibScalar
vidyoRouterActiveCascades = _VidyoRouterActiveCascades_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 25),
    _VidyoRouterActiveCascades_Type()
)
vidyoRouterActiveCascades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterActiveCascades.setStatus("current")
_VidyoRouterBrokenCascades_Type = Unsigned32
_VidyoRouterBrokenCascades_Object = MibScalar
vidyoRouterBrokenCascades = _VidyoRouterBrokenCascades_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 26),
    _VidyoRouterBrokenCascades_Type()
)
vidyoRouterBrokenCascades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterBrokenCascades.setStatus("current")
_VidyoRouterBrokenCascadeCount_Type = Counter32
_VidyoRouterBrokenCascadeCount_Object = MibScalar
vidyoRouterBrokenCascadeCount = _VidyoRouterBrokenCascadeCount_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 27),
    _VidyoRouterBrokenCascadeCount_Type()
)
vidyoRouterBrokenCascadeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterBrokenCascadeCount.setStatus("current")
_VidyoRouterCascadeMediaAlert_Type = TruthValue
_VidyoRouterCascadeMediaAlert_Object = MibScalar
vidyoRouterCascadeMediaAlert = _VidyoRouterCascadeMediaAlert_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 28),
    _VidyoRouterCascadeMediaAlert_Type()
)
vidyoRouterCascadeMediaAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterCascadeMediaAlert.setStatus("current")
_VidyoRouterCascadeMediaAlertCount_Type = Counter32
_VidyoRouterCascadeMediaAlertCount_Object = MibScalar
vidyoRouterCascadeMediaAlertCount = _VidyoRouterCascadeMediaAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 29),
    _VidyoRouterCascadeMediaAlertCount_Type()
)
vidyoRouterCascadeMediaAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterCascadeMediaAlertCount.setStatus("current")
_VidyoRouterCascadeMediaAlertEnabled_Type = TruthValue
_VidyoRouterCascadeMediaAlertEnabled_Object = MibScalar
vidyoRouterCascadeMediaAlertEnabled = _VidyoRouterCascadeMediaAlertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 30),
    _VidyoRouterCascadeMediaAlertEnabled_Type()
)
vidyoRouterCascadeMediaAlertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoRouterCascadeMediaAlertEnabled.setStatus("current")


class _VidyoRouterCascadeMediaJitterThreshold_Type(Unsigned32):
    """Custom type vidyoRouterCascadeMediaJitterThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000000),
    )


_VidyoRouterCascadeMediaJitterThreshold_Type.__name__ = "Unsigned32"
_VidyoRouterCascadeMediaJitterThreshold_Object = MibScalar
vidyoRouterCascadeMediaJitterThreshold = _VidyoRouterCascadeMediaJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 31),
    _VidyoRouterCascadeMediaJitterThreshold_Type()
)
vidyoRouterCascadeMediaJitterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoRouterCascadeMediaJitterThreshold.setStatus("current")


class _VidyoRouterCascadeMediaLossThreshold_Type(Unsigned32):
    """Custom type vidyoRouterCascadeMediaLossThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VidyoRouterCascadeMediaLossThreshold_Type.__name__ = "Unsigned32"
_VidyoRouterCascadeMediaLossThreshold_Object = MibScalar
vidyoRouterCascadeMediaLossThreshold = _VidyoRouterCascadeMediaLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 32),
    _VidyoRouterCascadeMediaLossThreshold_Type()
)
vidyoRouterCascadeMediaLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoRouterCascadeMediaLossThreshold.setStatus("current")
_VidyoRouterParticipantMediaAlert_Type = TruthValue
_VidyoRouterParticipantMediaAlert_Object = MibScalar
vidyoRouterParticipantMediaAlert = _VidyoRouterParticipantMediaAlert_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 33),
    _VidyoRouterParticipantMediaAlert_Type()
)
vidyoRouterParticipantMediaAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterParticipantMediaAlert.setStatus("current")
_VidyoRouterParticipantMediaAlertCount_Type = Counter32
_VidyoRouterParticipantMediaAlertCount_Object = MibScalar
vidyoRouterParticipantMediaAlertCount = _VidyoRouterParticipantMediaAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 34),
    _VidyoRouterParticipantMediaAlertCount_Type()
)
vidyoRouterParticipantMediaAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoRouterParticipantMediaAlertCount.setStatus("current")
_VidyoRouterParticipantMediaAlertEnabled_Type = TruthValue
_VidyoRouterParticipantMediaAlertEnabled_Object = MibScalar
vidyoRouterParticipantMediaAlertEnabled = _VidyoRouterParticipantMediaAlertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 35),
    _VidyoRouterParticipantMediaAlertEnabled_Type()
)
vidyoRouterParticipantMediaAlertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoRouterParticipantMediaAlertEnabled.setStatus("current")


class _VidyoRouterParticipantMediaJitterThreshold_Type(Unsigned32):
    """Custom type vidyoRouterParticipantMediaJitterThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000000),
    )


_VidyoRouterParticipantMediaJitterThreshold_Type.__name__ = "Unsigned32"
_VidyoRouterParticipantMediaJitterThreshold_Object = MibScalar
vidyoRouterParticipantMediaJitterThreshold = _VidyoRouterParticipantMediaJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 36),
    _VidyoRouterParticipantMediaJitterThreshold_Type()
)
vidyoRouterParticipantMediaJitterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoRouterParticipantMediaJitterThreshold.setStatus("current")


class _VidyoRouterParticipantMediaLossThreshold_Type(Unsigned32):
    """Custom type vidyoRouterParticipantMediaLossThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_VidyoRouterParticipantMediaLossThreshold_Type.__name__ = "Unsigned32"
_VidyoRouterParticipantMediaLossThreshold_Object = MibScalar
vidyoRouterParticipantMediaLossThreshold = _VidyoRouterParticipantMediaLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 37),
    _VidyoRouterParticipantMediaLossThreshold_Type()
)
vidyoRouterParticipantMediaLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoRouterParticipantMediaLossThreshold.setStatus("current")
_VidyoPortal_ObjectIdentity = ObjectIdentity
vidyoPortal = _VidyoPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2)
)
_VidyoPortalObjects_ObjectIdentity = ObjectIdentity
vidyoPortalObjects = _VidyoPortalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 1)
)
_VidyoPortalNotificationObjects_ObjectIdentity = ObjectIdentity
vidyoPortalNotificationObjects = _VidyoPortalNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 1, 1)
)
_VidyoPortalNotificationCommonObj_ObjectIdentity = ObjectIdentity
vidyoPortalNotificationCommonObj = _VidyoPortalNotificationCommonObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 1, 1, 1)
)
_VidyoPortalTrapTime_Type = OctetString
_VidyoPortalTrapTime_Object = MibScalar
vidyoPortalTrapTime = _VidyoPortalTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 1, 1, 1, 2),
    _VidyoPortalTrapTime_Type()
)
vidyoPortalTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalTrapTime.setStatus("current")
_VidyoPortalLocation_Type = OctetString
_VidyoPortalLocation_Object = MibScalar
vidyoPortalLocation = _VidyoPortalLocation_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 1, 1, 1, 3),
    _VidyoPortalLocation_Type()
)
vidyoPortalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalLocation.setStatus("current")
_VidyoPortalLocalName_Type = OctetString
_VidyoPortalLocalName_Object = MibScalar
vidyoPortalLocalName = _VidyoPortalLocalName_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 1, 1, 1, 4),
    _VidyoPortalLocalName_Type()
)
vidyoPortalLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalLocalName.setStatus("current")
_VidyoPortalStatusReportString_Type = OctetString
_VidyoPortalStatusReportString_Object = MibScalar
vidyoPortalStatusReportString = _VidyoPortalStatusReportString_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 1, 1, 1, 5),
    _VidyoPortalStatusReportString_Type()
)
vidyoPortalStatusReportString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalStatusReportString.setStatus("current")
_VidyoPortalEvents_ObjectIdentity = ObjectIdentity
vidyoPortalEvents = _VidyoPortalEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2)
)
_VidyoPortalMgmnt_ObjectIdentity = ObjectIdentity
vidyoPortalMgmnt = _VidyoPortalMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3)
)
_VidyoPortalSwVersion_Type = OctetString
_VidyoPortalSwVersion_Object = MibScalar
vidyoPortalSwVersion = _VidyoPortalSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 2),
    _VidyoPortalSwVersion_Type()
)
vidyoPortalSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalSwVersion.setStatus("current")
_VidyoPortalHwVersion_Type = OctetString
_VidyoPortalHwVersion_Object = MibScalar
vidyoPortalHwVersion = _VidyoPortalHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 3),
    _VidyoPortalHwVersion_Type()
)
vidyoPortalHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalHwVersion.setStatus("current")
_VidyoPortalTenantsCount_Type = Unsigned32
_VidyoPortalTenantsCount_Object = MibScalar
vidyoPortalTenantsCount = _VidyoPortalTenantsCount_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 4),
    _VidyoPortalTenantsCount_Type()
)
vidyoPortalTenantsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalTenantsCount.setStatus("current")
_VidyoPortalOnlineUsers_Type = Unsigned32
_VidyoPortalOnlineUsers_Object = MibScalar
vidyoPortalOnlineUsers = _VidyoPortalOnlineUsers_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 5),
    _VidyoPortalOnlineUsers_Type()
)
vidyoPortalOnlineUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalOnlineUsers.setStatus("current")
_VidyoPortalActiveConferences_Type = Unsigned32
_VidyoPortalActiveConferences_Object = MibScalar
vidyoPortalActiveConferences = _VidyoPortalActiveConferences_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 6),
    _VidyoPortalActiveConferences_Type()
)
vidyoPortalActiveConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalActiveConferences.setStatus("current")
_VidyoPortalConnectedVidyoGateways_Type = Unsigned32
_VidyoPortalConnectedVidyoGateways_Object = MibScalar
vidyoPortalConnectedVidyoGateways = _VidyoPortalConnectedVidyoGateways_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 7),
    _VidyoPortalConnectedVidyoGateways_Type()
)
vidyoPortalConnectedVidyoGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalConnectedVidyoGateways.setStatus("current")
_VidyoPortalConnectedVidyoRouters_Type = Unsigned32
_VidyoPortalConnectedVidyoRouters_Object = MibScalar
vidyoPortalConnectedVidyoRouters = _VidyoPortalConnectedVidyoRouters_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 8),
    _VidyoPortalConnectedVidyoRouters_Type()
)
vidyoPortalConnectedVidyoRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalConnectedVidyoRouters.setStatus("current")
_VidyoPortalConnectedVidyoReplays_Type = Unsigned32
_VidyoPortalConnectedVidyoReplays_Object = MibScalar
vidyoPortalConnectedVidyoReplays = _VidyoPortalConnectedVidyoReplays_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 9),
    _VidyoPortalConnectedVidyoReplays_Type()
)
vidyoPortalConnectedVidyoReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalConnectedVidyoReplays.setStatus("current")
_VidyoPortalClusterLocalIp_Type = OctetString
_VidyoPortalClusterLocalIp_Object = MibScalar
vidyoPortalClusterLocalIp = _VidyoPortalClusterLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 10),
    _VidyoPortalClusterLocalIp_Type()
)
vidyoPortalClusterLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalClusterLocalIp.setStatus("current")
_VidyoPortalClusterClusterIp_Type = OctetString
_VidyoPortalClusterClusterIp_Object = MibScalar
vidyoPortalClusterClusterIp = _VidyoPortalClusterClusterIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 11),
    _VidyoPortalClusterClusterIp_Type()
)
vidyoPortalClusterClusterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalClusterClusterIp.setStatus("current")
_VidyoPortalClusterPeerIp_Type = OctetString
_VidyoPortalClusterPeerIp_Object = MibScalar
vidyoPortalClusterPeerIp = _VidyoPortalClusterPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 12),
    _VidyoPortalClusterPeerIp_Type()
)
vidyoPortalClusterPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalClusterPeerIp.setStatus("current")
_VidyoPortalClusterHeartbeatPort_Type = Integer32
_VidyoPortalClusterHeartbeatPort_Object = MibScalar
vidyoPortalClusterHeartbeatPort = _VidyoPortalClusterHeartbeatPort_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 13),
    _VidyoPortalClusterHeartbeatPort_Type()
)
vidyoPortalClusterHeartbeatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalClusterHeartbeatPort.setStatus("current")
_VidyoPortalClusterFQDN_Type = OctetString
_VidyoPortalClusterFQDN_Object = MibScalar
vidyoPortalClusterFQDN = _VidyoPortalClusterFQDN_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 14),
    _VidyoPortalClusterFQDN_Type()
)
vidyoPortalClusterFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalClusterFQDN.setStatus("current")
_VidyoPortalClusterClusterIPNetmask_Type = Unsigned32
_VidyoPortalClusterClusterIPNetmask_Object = MibScalar
vidyoPortalClusterClusterIPNetmask = _VidyoPortalClusterClusterIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 15),
    _VidyoPortalClusterClusterIPNetmask_Type()
)
vidyoPortalClusterClusterIPNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalClusterClusterIPNetmask.setStatus("current")
_VidyoPortalClusterTestIp_Type = OctetString
_VidyoPortalClusterTestIp_Object = MibScalar
vidyoPortalClusterTestIp = _VidyoPortalClusterTestIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 16),
    _VidyoPortalClusterTestIp_Type()
)
vidyoPortalClusterTestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalClusterTestIp.setStatus("current")
_VidyoPortalClusterPreferredNode_Type = TruthValue
_VidyoPortalClusterPreferredNode_Object = MibScalar
vidyoPortalClusterPreferredNode = _VidyoPortalClusterPreferredNode_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 17),
    _VidyoPortalClusterPreferredNode_Type()
)
vidyoPortalClusterPreferredNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalClusterPreferredNode.setStatus("current")
_VidyoPortalHotStandbyStatus_Type = OctetString
_VidyoPortalHotStandbyStatus_Object = MibScalar
vidyoPortalHotStandbyStatus = _VidyoPortalHotStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 18),
    _VidyoPortalHotStandbyStatus_Type()
)
vidyoPortalHotStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalHotStandbyStatus.setStatus("current")
_VidyoPortalHotStandbyDBSnapshot_Type = OctetString
_VidyoPortalHotStandbyDBSnapshot_Object = MibScalar
vidyoPortalHotStandbyDBSnapshot = _VidyoPortalHotStandbyDBSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 19),
    _VidyoPortalHotStandbyDBSnapshot_Type()
)
vidyoPortalHotStandbyDBSnapshot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoPortalHotStandbyDBSnapshot.setStatus("current")


class _VidyoPortalLinesLicenseThreshold_Type(Unsigned32):
    """Custom type vidyoPortalLinesLicenseThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VidyoPortalLinesLicenseThreshold_Type.__name__ = "Unsigned32"
_VidyoPortalLinesLicenseThreshold_Object = MibScalar
vidyoPortalLinesLicenseThreshold = _VidyoPortalLinesLicenseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 20),
    _VidyoPortalLinesLicenseThreshold_Type()
)
vidyoPortalLinesLicenseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoPortalLinesLicenseThreshold.setStatus("current")


class _VidyoPortalInstallLicenseThreshold_Type(Unsigned32):
    """Custom type vidyoPortalInstallLicenseThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VidyoPortalInstallLicenseThreshold_Type.__name__ = "Unsigned32"
_VidyoPortalInstallLicenseThreshold_Object = MibScalar
vidyoPortalInstallLicenseThreshold = _VidyoPortalInstallLicenseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 21),
    _VidyoPortalInstallLicenseThreshold_Type()
)
vidyoPortalInstallLicenseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoPortalInstallLicenseThreshold.setStatus("current")
_VidyoGateway_ObjectIdentity = ObjectIdentity
vidyoGateway = _VidyoGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3)
)
_VidyoGatewayNode_ObjectIdentity = ObjectIdentity
vidyoGatewayNode = _VidyoGatewayNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1)
)
_VidyoGatewayNodeObjects_ObjectIdentity = ObjectIdentity
vidyoGatewayNodeObjects = _VidyoGatewayNodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1)
)
_VidyoGatewayNodeNotificationObjects_ObjectIdentity = ObjectIdentity
vidyoGatewayNodeNotificationObjects = _VidyoGatewayNodeNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1)
)
_VidyoGatewayNodeNotificationCommonObj_ObjectIdentity = ObjectIdentity
vidyoGatewayNodeNotificationCommonObj = _VidyoGatewayNodeNotificationCommonObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1)
)
_VidyoGatewayNodeGwIp_Type = OctetString
_VidyoGatewayNodeGwIp_Object = MibScalar
vidyoGatewayNodeGwIp = _VidyoGatewayNodeGwIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1, 2),
    _VidyoGatewayNodeGwIp_Type()
)
vidyoGatewayNodeGwIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeGwIp.setStatus("current")
_VidyoGatewayNodeMediaQualityValue_Type = Integer32
_VidyoGatewayNodeMediaQualityValue_Object = MibScalar
vidyoGatewayNodeMediaQualityValue = _VidyoGatewayNodeMediaQualityValue_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1, 3),
    _VidyoGatewayNodeMediaQualityValue_Type()
)
vidyoGatewayNodeMediaQualityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeMediaQualityValue.setStatus("current")
_VidyoGatewayNodePacketLossValue_Type = Integer32
_VidyoGatewayNodePacketLossValue_Object = MibScalar
vidyoGatewayNodePacketLossValue = _VidyoGatewayNodePacketLossValue_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1, 4),
    _VidyoGatewayNodePacketLossValue_Type()
)
vidyoGatewayNodePacketLossValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodePacketLossValue.setStatus("current")
_VidyoGatewayNodeCallId_Type = Integer32
_VidyoGatewayNodeCallId_Object = MibScalar
vidyoGatewayNodeCallId = _VidyoGatewayNodeCallId_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1, 5),
    _VidyoGatewayNodeCallId_Type()
)
vidyoGatewayNodeCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeCallId.setStatus("current")
_VidyoGatewayNodeChannelType_Type = OctetString
_VidyoGatewayNodeChannelType_Object = MibScalar
vidyoGatewayNodeChannelType = _VidyoGatewayNodeChannelType_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1, 6),
    _VidyoGatewayNodeChannelType_Type()
)
vidyoGatewayNodeChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeChannelType.setStatus("current")
_VidyoGatewayNodeLegacyIp_Type = OctetString
_VidyoGatewayNodeLegacyIp_Object = MibScalar
vidyoGatewayNodeLegacyIp = _VidyoGatewayNodeLegacyIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1, 7),
    _VidyoGatewayNodeLegacyIp_Type()
)
vidyoGatewayNodeLegacyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeLegacyIp.setStatus("current")
_VidyoGatewayNodeLegacyName_Type = OctetString
_VidyoGatewayNodeLegacyName_Object = MibScalar
vidyoGatewayNodeLegacyName = _VidyoGatewayNodeLegacyName_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1, 8),
    _VidyoGatewayNodeLegacyName_Type()
)
vidyoGatewayNodeLegacyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeLegacyName.setStatus("current")
_VidyoGatewayNodeEvents_ObjectIdentity = ObjectIdentity
vidyoGatewayNodeEvents = _VidyoGatewayNodeEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 2)
)
_VidyoGatewayNodeMgmnt_ObjectIdentity = ObjectIdentity
vidyoGatewayNodeMgmnt = _VidyoGatewayNodeMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 3)
)
_VidyoGatewayNodeSwVersion_Type = OctetString
_VidyoGatewayNodeSwVersion_Object = MibScalar
vidyoGatewayNodeSwVersion = _VidyoGatewayNodeSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 3, 2),
    _VidyoGatewayNodeSwVersion_Type()
)
vidyoGatewayNodeSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeSwVersion.setStatus("current")
_VidyoGatewayNodeHwVersion_Type = OctetString
_VidyoGatewayNodeHwVersion_Object = MibScalar
vidyoGatewayNodeHwVersion = _VidyoGatewayNodeHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 3, 3),
    _VidyoGatewayNodeHwVersion_Type()
)
vidyoGatewayNodeHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeHwVersion.setStatus("current")
_VidyoGatewayNodeGwccIp_Type = OctetString
_VidyoGatewayNodeGwccIp_Object = MibScalar
vidyoGatewayNodeGwccIp = _VidyoGatewayNodeGwccIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 3, 4),
    _VidyoGatewayNodeGwccIp_Type()
)
vidyoGatewayNodeGwccIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayNodeGwccIp.setStatus("current")
_VidyoGatewayNodeThresholdCheckFrequency_Type = Unsigned32
_VidyoGatewayNodeThresholdCheckFrequency_Object = MibScalar
vidyoGatewayNodeThresholdCheckFrequency = _VidyoGatewayNodeThresholdCheckFrequency_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 3, 5),
    _VidyoGatewayNodeThresholdCheckFrequency_Type()
)
vidyoGatewayNodeThresholdCheckFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoGatewayNodeThresholdCheckFrequency.setStatus("current")
_VidyoGatewayNodeMediaQualityThreshold_Type = Unsigned32
_VidyoGatewayNodeMediaQualityThreshold_Object = MibScalar
vidyoGatewayNodeMediaQualityThreshold = _VidyoGatewayNodeMediaQualityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 3, 6),
    _VidyoGatewayNodeMediaQualityThreshold_Type()
)
vidyoGatewayNodeMediaQualityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoGatewayNodeMediaQualityThreshold.setStatus("current")
_VidyoGatewayNodePacketLossThreshold_Type = Unsigned32
_VidyoGatewayNodePacketLossThreshold_Object = MibScalar
vidyoGatewayNodePacketLossThreshold = _VidyoGatewayNodePacketLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 3, 7),
    _VidyoGatewayNodePacketLossThreshold_Type()
)
vidyoGatewayNodePacketLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidyoGatewayNodePacketLossThreshold.setStatus("current")
_VidyoGatewayController_ObjectIdentity = ObjectIdentity
vidyoGatewayController = _VidyoGatewayController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2)
)
_VidyoGatewayControllerObjects_ObjectIdentity = ObjectIdentity
vidyoGatewayControllerObjects = _VidyoGatewayControllerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1)
)
_VidyoGatewayControllerNotificationObjects_ObjectIdentity = ObjectIdentity
vidyoGatewayControllerNotificationObjects = _VidyoGatewayControllerNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1)
)
_VidyoGatewayControllerNotificationCommonObj_ObjectIdentity = ObjectIdentity
vidyoGatewayControllerNotificationCommonObj = _VidyoGatewayControllerNotificationCommonObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1)
)
_VidyoGatewayControllerGwIp_Type = OctetString
_VidyoGatewayControllerGwIp_Object = MibScalar
vidyoGatewayControllerGwIp = _VidyoGatewayControllerGwIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 2),
    _VidyoGatewayControllerGwIp_Type()
)
vidyoGatewayControllerGwIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerGwIp.setStatus("current")
_VidyoGatewayControllerGwccIp_Type = OctetString
_VidyoGatewayControllerGwccIp_Object = MibScalar
vidyoGatewayControllerGwccIp = _VidyoGatewayControllerGwccIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 3),
    _VidyoGatewayControllerGwccIp_Type()
)
vidyoGatewayControllerGwccIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerGwccIp.setStatus("current")
_VidyoGatewayControllerVmId_Type = OctetString
_VidyoGatewayControllerVmId_Object = MibScalar
vidyoGatewayControllerVmId = _VidyoGatewayControllerVmId_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 4),
    _VidyoGatewayControllerVmId_Type()
)
vidyoGatewayControllerVmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerVmId.setStatus("current")
_VidyoGatewayControllerVmAddress_Type = OctetString
_VidyoGatewayControllerVmAddress_Object = MibScalar
vidyoGatewayControllerVmAddress = _VidyoGatewayControllerVmAddress_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 5),
    _VidyoGatewayControllerVmAddress_Type()
)
vidyoGatewayControllerVmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerVmAddress.setStatus("current")
_VidyoGatewayControllerClusterRole_Type = OctetString
_VidyoGatewayControllerClusterRole_Object = MibScalar
vidyoGatewayControllerClusterRole = _VidyoGatewayControllerClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 6),
    _VidyoGatewayControllerClusterRole_Type()
)
vidyoGatewayControllerClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerClusterRole.setStatus("current")
_VidyoGatewayControllerCallType_Type = OctetString
_VidyoGatewayControllerCallType_Object = MibScalar
vidyoGatewayControllerCallType = _VidyoGatewayControllerCallType_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 7),
    _VidyoGatewayControllerCallType_Type()
)
vidyoGatewayControllerCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerCallType.setStatus("current")
_VidyoGatewayControllerCallDirection_Type = OctetString
_VidyoGatewayControllerCallDirection_Object = MibScalar
vidyoGatewayControllerCallDirection = _VidyoGatewayControllerCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 8),
    _VidyoGatewayControllerCallDirection_Type()
)
vidyoGatewayControllerCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerCallDirection.setStatus("current")
_VidyoGatewayControllerCaller_Type = OctetString
_VidyoGatewayControllerCaller_Object = MibScalar
vidyoGatewayControllerCaller = _VidyoGatewayControllerCaller_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 9),
    _VidyoGatewayControllerCaller_Type()
)
vidyoGatewayControllerCaller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerCaller.setStatus("current")
_VidyoGatewayControllerCallee_Type = OctetString
_VidyoGatewayControllerCallee_Object = MibScalar
vidyoGatewayControllerCallee = _VidyoGatewayControllerCallee_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 10),
    _VidyoGatewayControllerCallee_Type()
)
vidyoGatewayControllerCallee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerCallee.setStatus("current")
_VidyoGatewayControllerAlertTime_Type = OctetString
_VidyoGatewayControllerAlertTime_Object = MibScalar
vidyoGatewayControllerAlertTime = _VidyoGatewayControllerAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 11),
    _VidyoGatewayControllerAlertTime_Type()
)
vidyoGatewayControllerAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerAlertTime.setStatus("current")
_VidyoGatewayControllerRemoteIp_Type = OctetString
_VidyoGatewayControllerRemoteIp_Object = MibScalar
vidyoGatewayControllerRemoteIp = _VidyoGatewayControllerRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 12),
    _VidyoGatewayControllerRemoteIp_Type()
)
vidyoGatewayControllerRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidyoGatewayControllerRemoteIp.setStatus("current")
_VidyoGatewayControllerEvents_ObjectIdentity = ObjectIdentity
vidyoGatewayControllerEvents = _VidyoGatewayControllerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2)
)

# Managed Objects groups

vidyoRouterNotificationCommonObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 1, 1, 1, 1)
)
vidyoRouterNotificationCommonObjGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterAlertTime"),
        ("VIDYO-SNMP-MIB", "vidyoRouterConferenceId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRemoteRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRemoteRouterUri"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantName"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantUri"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRtpRecvPacketLoss"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRtpRecvJitter"))
)
if mibBuilder.loadTexts:
    vidyoRouterNotificationCommonObjGroup.setStatus("current")

vidyoRouterMgmntObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 3, 1)
)
vidyoRouterMgmntObjGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterName"),
        ("VIDYO-SNMP-MIB", "vidyoRouterAppVersion"),
        ("VIDYO-SNMP-MIB", "vidyoRouterOsVersion"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRmcpVersion"),
        ("VIDYO-SNMP-MIB", "vidyoRouterLogicVersion"),
        ("VIDYO-SNMP-MIB", "vidyoRouterSdkVersion"),
        ("VIDYO-SNMP-MIB", "vidyoRouterHardwareCode"),
        ("VIDYO-SNMP-MIB", "vidyoRouterHardwareName"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCapacity"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmAddress"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmConnIsSecure"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmSysVersion"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmConnLost"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmConnLostCount"),
        ("VIDYO-SNMP-MIB", "vidyoRouterState"),
        ("VIDYO-SNMP-MIB", "vidyoRouterStatus"),
        ("VIDYO-SNMP-MIB", "vidyoRouterUptime"),
        ("VIDYO-SNMP-MIB", "vidyoRouterConferences"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipants"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascades"),
        ("VIDYO-SNMP-MIB", "vidyoRouterActiveParticipants"),
        ("VIDYO-SNMP-MIB", "vidyoRouterActiveCascades"),
        ("VIDYO-SNMP-MIB", "vidyoRouterBrokenCascades"),
        ("VIDYO-SNMP-MIB", "vidyoRouterBrokenCascadeCount"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascadeMediaAlert"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascadeMediaAlertCount"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascadeMediaAlertEnabled"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascadeMediaJitterThreshold"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascadeMediaLossThreshold"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantMediaAlert"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantMediaAlertCount"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantMediaAlertEnabled"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantMediaJitterThreshold"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantMediaLossThreshold"))
)
if mibBuilder.loadTexts:
    vidyoRouterMgmntObjGroup.setStatus("current")

vidyoPortalNotificationCommonObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 1, 1, 1, 1)
)
vidyoPortalNotificationCommonObjGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalNotificationCommonObjGroup.setStatus("current")

vidyoPortalMgmntObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 3, 1)
)
vidyoPortalMgmntObjGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalSwVersion"),
        ("VIDYO-SNMP-MIB", "vidyoPortalHwVersion"),
        ("VIDYO-SNMP-MIB", "vidyoPortalTenantsCount"),
        ("VIDYO-SNMP-MIB", "vidyoPortalOnlineUsers"),
        ("VIDYO-SNMP-MIB", "vidyoPortalActiveConferences"),
        ("VIDYO-SNMP-MIB", "vidyoPortalConnectedVidyoGateways"),
        ("VIDYO-SNMP-MIB", "vidyoPortalConnectedVidyoRouters"),
        ("VIDYO-SNMP-MIB", "vidyoPortalConnectedVidyoReplays"),
        ("VIDYO-SNMP-MIB", "vidyoPortalClusterLocalIp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalClusterClusterIp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalClusterPeerIp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalClusterHeartbeatPort"),
        ("VIDYO-SNMP-MIB", "vidyoPortalClusterFQDN"),
        ("VIDYO-SNMP-MIB", "vidyoPortalClusterClusterIPNetmask"),
        ("VIDYO-SNMP-MIB", "vidyoPortalClusterTestIp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalClusterPreferredNode"),
        ("VIDYO-SNMP-MIB", "vidyoPortalHotStandbyStatus"),
        ("VIDYO-SNMP-MIB", "vidyoPortalHotStandbyDBSnapshot"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLinesLicenseThreshold"),
        ("VIDYO-SNMP-MIB", "vidyoPortalInstallLicenseThreshold"))
)
if mibBuilder.loadTexts:
    vidyoPortalMgmntObjGroup.setStatus("current")

vidyoGatewayNodeNotificationCommonObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 1, 1, 1, 1)
)
vidyoGatewayNodeNotificationCommonObjGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayNodeGwIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeMediaQualityValue"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodePacketLossValue"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeCallId"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeChannelType"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeLegacyIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeLegacyName"))
)
if mibBuilder.loadTexts:
    vidyoGatewayNodeNotificationCommonObjGroup.setStatus("current")

vidyoGatewayNodeMgmntObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 3, 1)
)
vidyoGatewayNodeMgmntObjGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayNodeSwVersion"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeHwVersion"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeGwccIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeThresholdCheckFrequency"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeMediaQualityThreshold"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodePacketLossThreshold"))
)
if mibBuilder.loadTexts:
    vidyoGatewayNodeMgmntObjGroup.setStatus("current")

vidyoGatewayControllerNotificationCommonObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 1, 1, 1, 1)
)
vidyoGatewayControllerNotificationCommonObjGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwccIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerVmId"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerVmAddress"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerClusterRole"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCallType"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCallDirection"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCaller"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCallee"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerAlertTime"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerRemoteIp"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerNotificationCommonObjGroup.setStatus("current")


# Notification objects

vidyoRouterVmConnLostAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 2, 2)
)
vidyoRouterVmConnLostAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterStatus"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmAddress"),
        ("VIDYO-SNMP-MIB", "vidyoRouterAlertTime"))
)
if mibBuilder.loadTexts:
    vidyoRouterVmConnLostAlert.setStatus(
        "current"
    )

vidyoRouterVmConnEstablishedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 2, 3)
)
vidyoRouterVmConnEstablishedAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterStatus"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmAddress"),
        ("VIDYO-SNMP-MIB", "vidyoRouterAlertTime"))
)
if mibBuilder.loadTexts:
    vidyoRouterVmConnEstablishedAlert.setStatus(
        "current"
    )

vidyoRouterCascadeBrokenAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 2, 4)
)
vidyoRouterCascadeBrokenAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterConferenceId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRemoteRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRemoteRouterUri"),
        ("VIDYO-SNMP-MIB", "vidyoRouterAlertTime"))
)
if mibBuilder.loadTexts:
    vidyoRouterCascadeBrokenAlert.setStatus(
        "current"
    )

vidyoRouterCascadeFixedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 2, 5)
)
vidyoRouterCascadeFixedAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterConferenceId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRemoteRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRemoteRouterUri"),
        ("VIDYO-SNMP-MIB", "vidyoRouterAlertTime"))
)
if mibBuilder.loadTexts:
    vidyoRouterCascadeFixedAlert.setStatus(
        "current"
    )

vidyoRouterCascadeMediaQualityAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 2, 6)
)
vidyoRouterCascadeMediaQualityAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterConferenceId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRemoteRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRemoteRouterUri"),
        ("VIDYO-SNMP-MIB", "vidyoRouterAlertTime"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRtpRecvPacketLoss"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRtpRecvJitter"))
)
if mibBuilder.loadTexts:
    vidyoRouterCascadeMediaQualityAlert.setStatus(
        "current"
    )

vidyoRouterParticipantMediaQualityAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 2, 7)
)
vidyoRouterParticipantMediaQualityAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterConferenceId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantId"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantName"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantUri"),
        ("VIDYO-SNMP-MIB", "vidyoRouterAlertTime"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRtpRecvPacketLoss"),
        ("VIDYO-SNMP-MIB", "vidyoRouterRtpRecvJitter"))
)
if mibBuilder.loadTexts:
    vidyoRouterParticipantMediaQualityAlert.setStatus(
        "current"
    )

vidyoPortalVidyoManagerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 2)
)
vidyoPortalVidyoManagerUp.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoManagerUp.setStatus(
        "current"
    )

vidyoPortalVidyoManagerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 3)
)
vidyoPortalVidyoManagerDown.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoManagerDown.setStatus(
        "current"
    )

vidyoPortalVidyoRouterUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 4)
)
vidyoPortalVidyoRouterUp.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoRouterUp.setStatus(
        "current"
    )

vidyoPortalVidyoRouterDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 5)
)
vidyoPortalVidyoRouterDown.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoRouterDown.setStatus(
        "current"
    )

vidyoPortalVidyoGatewayUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 6)
)
vidyoPortalVidyoGatewayUp.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoGatewayUp.setStatus(
        "current"
    )

vidyoPortalVidyoGatewayDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 7)
)
vidyoPortalVidyoGatewayDown.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoGatewayDown.setStatus(
        "current"
    )

vidyoPortalUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 8)
)
vidyoPortalUp.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalUp.setStatus(
        "current"
    )

vidyoPortalDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 9)
)
vidyoPortalDown.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalDown.setStatus(
        "current"
    )

vidyoPortalFailoverOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 10)
)
vidyoPortalFailoverOccurred.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalFailoverOccurred.setStatus(
        "current"
    )

vidyoPortalLineConsumptionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 11)
)
vidyoPortalLineConsumptionThresholdExceeded.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalLineConsumptionThresholdExceeded.setStatus(
        "current"
    )

vidyoPortalInstallConsumptionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 12)
)
vidyoPortalInstallConsumptionThresholdExceeded.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalInstallConsumptionThresholdExceeded.setStatus(
        "current"
    )

vidyoPortalInstallConsumptionNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 13)
)
vidyoPortalInstallConsumptionNormal.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalInstallConsumptionNormal.setStatus(
        "current"
    )

vidyoPortalLineConsumptionNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 14)
)
vidyoPortalLineConsumptionNormal.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalLineConsumptionNormal.setStatus(
        "current"
    )

vidyoPortalVidyoProxyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 15)
)
vidyoPortalVidyoProxyUp.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoProxyUp.setStatus(
        "current"
    )

vidyoPortalVidyoProxyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 16)
)
vidyoPortalVidyoProxyDown.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoProxyDown.setStatus(
        "current"
    )

vidyoPortalVidyoReplayUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 17)
)
vidyoPortalVidyoReplayUp.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoReplayUp.setStatus(
        "current"
    )

vidyoPortalVidyoReplayDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 18)
)
vidyoPortalVidyoReplayDown.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalTrapTime"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocation"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLocalName"),
        ("VIDYO-SNMP-MIB", "vidyoPortalStatusReportString"))
)
if mibBuilder.loadTexts:
    vidyoPortalVidyoReplayDown.setStatus(
        "current"
    )

vidyoGatewayNodeLegacyMediaQualityThresholdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 2, 2)
)
vidyoGatewayNodeLegacyMediaQualityThresholdAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayNodeMediaQualityValue"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeGwIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeCallId"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeChannelType"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeLegacyIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeLegacyName"))
)
if mibBuilder.loadTexts:
    vidyoGatewayNodeLegacyMediaQualityThresholdAlert.setStatus(
        "current"
    )

vidyoGatewayNodeLegacyPacketLossThresholdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 2, 3)
)
vidyoGatewayNodeLegacyPacketLossThresholdAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayNodePacketLossValue"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeGwIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeCallId"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeChannelType"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeLegacyIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeLegacyName"))
)
if mibBuilder.loadTexts:
    vidyoGatewayNodeLegacyPacketLossThresholdAlert.setStatus(
        "current"
    )

vidyoGatewayControllerJoinedClusterAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2, 2)
)
vidyoGatewayControllerJoinedClusterAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwccIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwIp"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerJoinedClusterAlert.setStatus(
        "current"
    )

vidyoGatewayControllerLeftClusterAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2, 3)
)
vidyoGatewayControllerLeftClusterAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwccIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwIp"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerLeftClusterAlert.setStatus(
        "current"
    )

vidyoGatewayControllerVmConnLostAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2, 4)
)
vidyoGatewayControllerVmConnLostAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwccIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerVmId"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerVmAddress"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerVmConnLostAlert.setStatus(
        "current"
    )

vidyoGatewayControllerVmConnEstablishedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2, 5)
)
vidyoGatewayControllerVmConnEstablishedAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwccIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerVmId"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerVmAddress"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerVmConnEstablishedAlert.setStatus(
        "current"
    )

vidyoGatewayControllerCallRejectedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2, 6)
)
vidyoGatewayControllerCallRejectedAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerAlertTime"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCallType"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCallDirection"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCaller"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCallee"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerCallRejectedAlert.setStatus(
        "current"
    )

vidyoGatewayControllerClusterRoleAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2, 7)
)
vidyoGatewayControllerClusterRoleAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerAlertTime"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwccIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerClusterRole"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerClusterRoleAlert.setStatus(
        "current"
    )

vidyoGatewayControllerIPAddedToBlackListAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2, 8)
)
vidyoGatewayControllerIPAddedToBlackListAlert.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerAlertTime"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerGwccIp"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerRemoteIp"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerIPAddedToBlackListAlert.setStatus(
        "current"
    )


# Notifications groups

vidyoRouterEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 1, 2, 1)
)
vidyoRouterEventsGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoRouterVmConnLostAlert"),
        ("VIDYO-SNMP-MIB", "vidyoRouterVmConnEstablishedAlert"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascadeBrokenAlert"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascadeFixedAlert"),
        ("VIDYO-SNMP-MIB", "vidyoRouterCascadeMediaQualityAlert"),
        ("VIDYO-SNMP-MIB", "vidyoRouterParticipantMediaQualityAlert"))
)
if mibBuilder.loadTexts:
    vidyoRouterEventsGroup.setStatus(
        "current"
    )

vidyoPortalEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 2, 2, 1)
)
vidyoPortalEventsGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoPortalVidyoManagerUp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoManagerDown"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoRouterUp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoRouterDown"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoGatewayUp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoGatewayDown"),
        ("VIDYO-SNMP-MIB", "vidyoPortalUp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalDown"),
        ("VIDYO-SNMP-MIB", "vidyoPortalFailoverOccurred"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLineConsumptionThresholdExceeded"),
        ("VIDYO-SNMP-MIB", "vidyoPortalInstallConsumptionThresholdExceeded"),
        ("VIDYO-SNMP-MIB", "vidyoPortalInstallConsumptionNormal"),
        ("VIDYO-SNMP-MIB", "vidyoPortalLineConsumptionNormal"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoProxyUp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoProxyDown"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoReplayUp"),
        ("VIDYO-SNMP-MIB", "vidyoPortalVidyoReplayDown"))
)
if mibBuilder.loadTexts:
    vidyoPortalEventsGroup.setStatus(
        "current"
    )

vidyoGatewayNodeEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 1, 2, 1)
)
vidyoGatewayNodeEventGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayNodeLegacyMediaQualityThresholdAlert"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayNodeLegacyPacketLossThresholdAlert"))
)
if mibBuilder.loadTexts:
    vidyoGatewayNodeEventGroup.setStatus(
        "current"
    )

vidyoGatewayControllerEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35969, 1, 1, 3, 2, 2, 1)
)
vidyoGatewayControllerEventGroup.setObjects(
      *(("VIDYO-SNMP-MIB", "vidyoGatewayControllerJoinedClusterAlert"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerLeftClusterAlert"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerVmConnLostAlert"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerVmConnEstablishedAlert"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerCallRejectedAlert"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerClusterRoleAlert"),
        ("VIDYO-SNMP-MIB", "vidyoGatewayControllerIPAddedToBlackListAlert"))
)
if mibBuilder.loadTexts:
    vidyoGatewayControllerEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDYO-SNMP-MIB",
    **{"vidyo": vidyo,
       "vidyoMIBS": vidyoMIBS,
       "vidyoProducts": vidyoProducts,
       "vidyoRouter": vidyoRouter,
       "vidyoRouterObjects": vidyoRouterObjects,
       "vidyoRouterNotificationObjects": vidyoRouterNotificationObjects,
       "vidyoRouterNotificationCommonObj": vidyoRouterNotificationCommonObj,
       "vidyoRouterNotificationCommonObjGroup": vidyoRouterNotificationCommonObjGroup,
       "vidyoRouterAlertTime": vidyoRouterAlertTime,
       "vidyoRouterConferenceId": vidyoRouterConferenceId,
       "vidyoRouterRemoteRouterId": vidyoRouterRemoteRouterId,
       "vidyoRouterRemoteRouterUri": vidyoRouterRemoteRouterUri,
       "vidyoRouterParticipantId": vidyoRouterParticipantId,
       "vidyoRouterParticipantName": vidyoRouterParticipantName,
       "vidyoRouterParticipantUri": vidyoRouterParticipantUri,
       "vidyoRouterRtpRecvPacketLoss": vidyoRouterRtpRecvPacketLoss,
       "vidyoRouterRtpRecvJitter": vidyoRouterRtpRecvJitter,
       "vidyoRouterEvents": vidyoRouterEvents,
       "vidyoRouterEventsGroup": vidyoRouterEventsGroup,
       "vidyoRouterVmConnLostAlert": vidyoRouterVmConnLostAlert,
       "vidyoRouterVmConnEstablishedAlert": vidyoRouterVmConnEstablishedAlert,
       "vidyoRouterCascadeBrokenAlert": vidyoRouterCascadeBrokenAlert,
       "vidyoRouterCascadeFixedAlert": vidyoRouterCascadeFixedAlert,
       "vidyoRouterCascadeMediaQualityAlert": vidyoRouterCascadeMediaQualityAlert,
       "vidyoRouterParticipantMediaQualityAlert": vidyoRouterParticipantMediaQualityAlert,
       "vidyoRouterMgmnt": vidyoRouterMgmnt,
       "vidyoRouterMgmntObjGroup": vidyoRouterMgmntObjGroup,
       "vidyoRouterId": vidyoRouterId,
       "vidyoRouterName": vidyoRouterName,
       "vidyoRouterAppVersion": vidyoRouterAppVersion,
       "vidyoRouterOsVersion": vidyoRouterOsVersion,
       "vidyoRouterRmcpVersion": vidyoRouterRmcpVersion,
       "vidyoRouterLogicVersion": vidyoRouterLogicVersion,
       "vidyoRouterSdkVersion": vidyoRouterSdkVersion,
       "vidyoRouterHardwareCode": vidyoRouterHardwareCode,
       "vidyoRouterHardwareName": vidyoRouterHardwareName,
       "vidyoRouterCapacity": vidyoRouterCapacity,
       "vidyoRouterVmId": vidyoRouterVmId,
       "vidyoRouterVmAddress": vidyoRouterVmAddress,
       "vidyoRouterVmConnIsSecure": vidyoRouterVmConnIsSecure,
       "vidyoRouterVmSysVersion": vidyoRouterVmSysVersion,
       "vidyoRouterVmConnLost": vidyoRouterVmConnLost,
       "vidyoRouterVmConnLostCount": vidyoRouterVmConnLostCount,
       "vidyoRouterState": vidyoRouterState,
       "vidyoRouterStatus": vidyoRouterStatus,
       "vidyoRouterUptime": vidyoRouterUptime,
       "vidyoRouterConferences": vidyoRouterConferences,
       "vidyoRouterParticipants": vidyoRouterParticipants,
       "vidyoRouterCascades": vidyoRouterCascades,
       "vidyoRouterActiveParticipants": vidyoRouterActiveParticipants,
       "vidyoRouterActiveCascades": vidyoRouterActiveCascades,
       "vidyoRouterBrokenCascades": vidyoRouterBrokenCascades,
       "vidyoRouterBrokenCascadeCount": vidyoRouterBrokenCascadeCount,
       "vidyoRouterCascadeMediaAlert": vidyoRouterCascadeMediaAlert,
       "vidyoRouterCascadeMediaAlertCount": vidyoRouterCascadeMediaAlertCount,
       "vidyoRouterCascadeMediaAlertEnabled": vidyoRouterCascadeMediaAlertEnabled,
       "vidyoRouterCascadeMediaJitterThreshold": vidyoRouterCascadeMediaJitterThreshold,
       "vidyoRouterCascadeMediaLossThreshold": vidyoRouterCascadeMediaLossThreshold,
       "vidyoRouterParticipantMediaAlert": vidyoRouterParticipantMediaAlert,
       "vidyoRouterParticipantMediaAlertCount": vidyoRouterParticipantMediaAlertCount,
       "vidyoRouterParticipantMediaAlertEnabled": vidyoRouterParticipantMediaAlertEnabled,
       "vidyoRouterParticipantMediaJitterThreshold": vidyoRouterParticipantMediaJitterThreshold,
       "vidyoRouterParticipantMediaLossThreshold": vidyoRouterParticipantMediaLossThreshold,
       "vidyoPortal": vidyoPortal,
       "vidyoPortalObjects": vidyoPortalObjects,
       "vidyoPortalNotificationObjects": vidyoPortalNotificationObjects,
       "vidyoPortalNotificationCommonObj": vidyoPortalNotificationCommonObj,
       "vidyoPortalNotificationCommonObjGroup": vidyoPortalNotificationCommonObjGroup,
       "vidyoPortalTrapTime": vidyoPortalTrapTime,
       "vidyoPortalLocation": vidyoPortalLocation,
       "vidyoPortalLocalName": vidyoPortalLocalName,
       "vidyoPortalStatusReportString": vidyoPortalStatusReportString,
       "vidyoPortalEvents": vidyoPortalEvents,
       "vidyoPortalEventsGroup": vidyoPortalEventsGroup,
       "vidyoPortalVidyoManagerUp": vidyoPortalVidyoManagerUp,
       "vidyoPortalVidyoManagerDown": vidyoPortalVidyoManagerDown,
       "vidyoPortalVidyoRouterUp": vidyoPortalVidyoRouterUp,
       "vidyoPortalVidyoRouterDown": vidyoPortalVidyoRouterDown,
       "vidyoPortalVidyoGatewayUp": vidyoPortalVidyoGatewayUp,
       "vidyoPortalVidyoGatewayDown": vidyoPortalVidyoGatewayDown,
       "vidyoPortalUp": vidyoPortalUp,
       "vidyoPortalDown": vidyoPortalDown,
       "vidyoPortalFailoverOccurred": vidyoPortalFailoverOccurred,
       "vidyoPortalLineConsumptionThresholdExceeded": vidyoPortalLineConsumptionThresholdExceeded,
       "vidyoPortalInstallConsumptionThresholdExceeded": vidyoPortalInstallConsumptionThresholdExceeded,
       "vidyoPortalInstallConsumptionNormal": vidyoPortalInstallConsumptionNormal,
       "vidyoPortalLineConsumptionNormal": vidyoPortalLineConsumptionNormal,
       "vidyoPortalVidyoProxyUp": vidyoPortalVidyoProxyUp,
       "vidyoPortalVidyoProxyDown": vidyoPortalVidyoProxyDown,
       "vidyoPortalVidyoReplayUp": vidyoPortalVidyoReplayUp,
       "vidyoPortalVidyoReplayDown": vidyoPortalVidyoReplayDown,
       "vidyoPortalMgmnt": vidyoPortalMgmnt,
       "vidyoPortalMgmntObjGroup": vidyoPortalMgmntObjGroup,
       "vidyoPortalSwVersion": vidyoPortalSwVersion,
       "vidyoPortalHwVersion": vidyoPortalHwVersion,
       "vidyoPortalTenantsCount": vidyoPortalTenantsCount,
       "vidyoPortalOnlineUsers": vidyoPortalOnlineUsers,
       "vidyoPortalActiveConferences": vidyoPortalActiveConferences,
       "vidyoPortalConnectedVidyoGateways": vidyoPortalConnectedVidyoGateways,
       "vidyoPortalConnectedVidyoRouters": vidyoPortalConnectedVidyoRouters,
       "vidyoPortalConnectedVidyoReplays": vidyoPortalConnectedVidyoReplays,
       "vidyoPortalClusterLocalIp": vidyoPortalClusterLocalIp,
       "vidyoPortalClusterClusterIp": vidyoPortalClusterClusterIp,
       "vidyoPortalClusterPeerIp": vidyoPortalClusterPeerIp,
       "vidyoPortalClusterHeartbeatPort": vidyoPortalClusterHeartbeatPort,
       "vidyoPortalClusterFQDN": vidyoPortalClusterFQDN,
       "vidyoPortalClusterClusterIPNetmask": vidyoPortalClusterClusterIPNetmask,
       "vidyoPortalClusterTestIp": vidyoPortalClusterTestIp,
       "vidyoPortalClusterPreferredNode": vidyoPortalClusterPreferredNode,
       "vidyoPortalHotStandbyStatus": vidyoPortalHotStandbyStatus,
       "vidyoPortalHotStandbyDBSnapshot": vidyoPortalHotStandbyDBSnapshot,
       "vidyoPortalLinesLicenseThreshold": vidyoPortalLinesLicenseThreshold,
       "vidyoPortalInstallLicenseThreshold": vidyoPortalInstallLicenseThreshold,
       "vidyoGateway": vidyoGateway,
       "vidyoGatewayNode": vidyoGatewayNode,
       "vidyoGatewayNodeObjects": vidyoGatewayNodeObjects,
       "vidyoGatewayNodeNotificationObjects": vidyoGatewayNodeNotificationObjects,
       "vidyoGatewayNodeNotificationCommonObj": vidyoGatewayNodeNotificationCommonObj,
       "vidyoGatewayNodeNotificationCommonObjGroup": vidyoGatewayNodeNotificationCommonObjGroup,
       "vidyoGatewayNodeGwIp": vidyoGatewayNodeGwIp,
       "vidyoGatewayNodeMediaQualityValue": vidyoGatewayNodeMediaQualityValue,
       "vidyoGatewayNodePacketLossValue": vidyoGatewayNodePacketLossValue,
       "vidyoGatewayNodeCallId": vidyoGatewayNodeCallId,
       "vidyoGatewayNodeChannelType": vidyoGatewayNodeChannelType,
       "vidyoGatewayNodeLegacyIp": vidyoGatewayNodeLegacyIp,
       "vidyoGatewayNodeLegacyName": vidyoGatewayNodeLegacyName,
       "vidyoGatewayNodeEvents": vidyoGatewayNodeEvents,
       "vidyoGatewayNodeEventGroup": vidyoGatewayNodeEventGroup,
       "vidyoGatewayNodeLegacyMediaQualityThresholdAlert": vidyoGatewayNodeLegacyMediaQualityThresholdAlert,
       "vidyoGatewayNodeLegacyPacketLossThresholdAlert": vidyoGatewayNodeLegacyPacketLossThresholdAlert,
       "vidyoGatewayNodeMgmnt": vidyoGatewayNodeMgmnt,
       "vidyoGatewayNodeMgmntObjGroup": vidyoGatewayNodeMgmntObjGroup,
       "vidyoGatewayNodeSwVersion": vidyoGatewayNodeSwVersion,
       "vidyoGatewayNodeHwVersion": vidyoGatewayNodeHwVersion,
       "vidyoGatewayNodeGwccIp": vidyoGatewayNodeGwccIp,
       "vidyoGatewayNodeThresholdCheckFrequency": vidyoGatewayNodeThresholdCheckFrequency,
       "vidyoGatewayNodeMediaQualityThreshold": vidyoGatewayNodeMediaQualityThreshold,
       "vidyoGatewayNodePacketLossThreshold": vidyoGatewayNodePacketLossThreshold,
       "vidyoGatewayController": vidyoGatewayController,
       "vidyoGatewayControllerObjects": vidyoGatewayControllerObjects,
       "vidyoGatewayControllerNotificationObjects": vidyoGatewayControllerNotificationObjects,
       "vidyoGatewayControllerNotificationCommonObj": vidyoGatewayControllerNotificationCommonObj,
       "vidyoGatewayControllerNotificationCommonObjGroup": vidyoGatewayControllerNotificationCommonObjGroup,
       "vidyoGatewayControllerGwIp": vidyoGatewayControllerGwIp,
       "vidyoGatewayControllerGwccIp": vidyoGatewayControllerGwccIp,
       "vidyoGatewayControllerVmId": vidyoGatewayControllerVmId,
       "vidyoGatewayControllerVmAddress": vidyoGatewayControllerVmAddress,
       "vidyoGatewayControllerClusterRole": vidyoGatewayControllerClusterRole,
       "vidyoGatewayControllerCallType": vidyoGatewayControllerCallType,
       "vidyoGatewayControllerCallDirection": vidyoGatewayControllerCallDirection,
       "vidyoGatewayControllerCaller": vidyoGatewayControllerCaller,
       "vidyoGatewayControllerCallee": vidyoGatewayControllerCallee,
       "vidyoGatewayControllerAlertTime": vidyoGatewayControllerAlertTime,
       "vidyoGatewayControllerRemoteIp": vidyoGatewayControllerRemoteIp,
       "vidyoGatewayControllerEvents": vidyoGatewayControllerEvents,
       "vidyoGatewayControllerEventGroup": vidyoGatewayControllerEventGroup,
       "vidyoGatewayControllerJoinedClusterAlert": vidyoGatewayControllerJoinedClusterAlert,
       "vidyoGatewayControllerLeftClusterAlert": vidyoGatewayControllerLeftClusterAlert,
       "vidyoGatewayControllerVmConnLostAlert": vidyoGatewayControllerVmConnLostAlert,
       "vidyoGatewayControllerVmConnEstablishedAlert": vidyoGatewayControllerVmConnEstablishedAlert,
       "vidyoGatewayControllerCallRejectedAlert": vidyoGatewayControllerCallRejectedAlert,
       "vidyoGatewayControllerClusterRoleAlert": vidyoGatewayControllerClusterRoleAlert,
       "vidyoGatewayControllerIPAddedToBlackListAlert": vidyoGatewayControllerIPAddedToBlackListAlert}
)
