# SNMP MIB module (CISCO-FIREPOWER-COMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-COMM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:10 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprAaaConfigState,
 CfprCommAdminState,
 CfprCommAuth,
 CfprCommChannel,
 CfprCommCipherSuiteMode,
 CfprCommClientItemAdminState,
 CfprCommCrlModeType,
 CfprCommDeviceState,
 CfprCommDnsProviderAdminState,
 CfprCommHostKeyEcdsa,
 CfprCommHttpsAuthType,
 CfprCommIpv4Prefix,
 CfprCommIpv6Prefix,
 CfprCommModeAdminState,
 CfprCommModeFlag,
 CfprCommNtpAuthState,
 CfprCommNtpProviderAdminState,
 CfprCommNtpSha1Id,
 CfprCommProtocol,
 CfprCommRebootState,
 CfprCommRegState,
 CfprCommServiceProtocol,
 CfprCommShellProto,
 CfprCommSnmpAdminAppSlot,
 CfprCommSnmpAuth,
 CfprCommSnmpConfigState,
 CfprCommSnmpNotificationType,
 CfprCommSnmpProto,
 CfprCommSnmpV3Privilege,
 CfprCommSnmpVersion,
 CfprCommSshAdminState,
 CfprCommSshEncryptAlgo,
 CfprCommSshKexAlgo,
 CfprCommSshMacAlgo,
 CfprCommSshcCliEncryptAlgo,
 CfprCommSshcCliKexAlgo,
 CfprCommSshcCliMacAlgo,
 CfprCommSshcStrictKeyCheck,
 CfprCommSvcEpFsmCurrentFsm,
 CfprCommSvcEpFsmStageName,
 CfprCommSvcEpFsmTaskFlags,
 CfprCommSvcEpFsmTaskItem,
 CfprCommSysTimeSyncStatus,
 CfprCommSyslogAdminState,
 CfprCommSyslogClientEnum,
 CfprCommSyslogFileSize,
 CfprCommSyslogForwardingFacility,
 CfprCommSyslogPlatformAdminState,
 CfprCommSyslogProto,
 CfprCommSyslogRestrictedSeverity,
 CfprCommSyslogSeverity,
 CfprCommSyslogSourceAudits,
 CfprCommSyslogSourceEvents,
 CfprCommSyslogSourceFaults,
 CfprCommTelemetryAdminState,
 CfprCommTelemetryFsmCurrentFsm,
 CfprCommTelemetryFsmStageName,
 CfprCommTelemetryFsmTaskItem,
 CfprCommTelemetryOperState,
 CfprCommTimeSyncStatus,
 CfprCommTimeZoneConfigState,
 CfprCommTlsVerType,
 CfprCommWebProto,
 CfprConditionRemoteInvRslt,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAaaConfigState",
    "CfprCommAdminState",
    "CfprCommAuth",
    "CfprCommChannel",
    "CfprCommCipherSuiteMode",
    "CfprCommClientItemAdminState",
    "CfprCommCrlModeType",
    "CfprCommDeviceState",
    "CfprCommDnsProviderAdminState",
    "CfprCommHostKeyEcdsa",
    "CfprCommHttpsAuthType",
    "CfprCommIpv4Prefix",
    "CfprCommIpv6Prefix",
    "CfprCommModeAdminState",
    "CfprCommModeFlag",
    "CfprCommNtpAuthState",
    "CfprCommNtpProviderAdminState",
    "CfprCommNtpSha1Id",
    "CfprCommProtocol",
    "CfprCommRebootState",
    "CfprCommRegState",
    "CfprCommServiceProtocol",
    "CfprCommShellProto",
    "CfprCommSnmpAdminAppSlot",
    "CfprCommSnmpAuth",
    "CfprCommSnmpConfigState",
    "CfprCommSnmpNotificationType",
    "CfprCommSnmpProto",
    "CfprCommSnmpV3Privilege",
    "CfprCommSnmpVersion",
    "CfprCommSshAdminState",
    "CfprCommSshEncryptAlgo",
    "CfprCommSshKexAlgo",
    "CfprCommSshMacAlgo",
    "CfprCommSshcCliEncryptAlgo",
    "CfprCommSshcCliKexAlgo",
    "CfprCommSshcCliMacAlgo",
    "CfprCommSshcStrictKeyCheck",
    "CfprCommSvcEpFsmCurrentFsm",
    "CfprCommSvcEpFsmStageName",
    "CfprCommSvcEpFsmTaskFlags",
    "CfprCommSvcEpFsmTaskItem",
    "CfprCommSysTimeSyncStatus",
    "CfprCommSyslogAdminState",
    "CfprCommSyslogClientEnum",
    "CfprCommSyslogFileSize",
    "CfprCommSyslogForwardingFacility",
    "CfprCommSyslogPlatformAdminState",
    "CfprCommSyslogProto",
    "CfprCommSyslogRestrictedSeverity",
    "CfprCommSyslogSeverity",
    "CfprCommSyslogSourceAudits",
    "CfprCommSyslogSourceEvents",
    "CfprCommSyslogSourceFaults",
    "CfprCommTelemetryAdminState",
    "CfprCommTelemetryFsmCurrentFsm",
    "CfprCommTelemetryFsmStageName",
    "CfprCommTelemetryFsmTaskItem",
    "CfprCommTelemetryOperState",
    "CfprCommTimeSyncStatus",
    "CfprCommTimeZoneConfigState",
    "CfprCommTlsVerType",
    "CfprCommWebProto",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprPolicyPolicyOwner")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprCommObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprCommDateTimeTable_Object = MibTable
cfprCommDateTimeTable = _CfprCommDateTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3)
)
if mibBuilder.loadTexts:
    cfprCommDateTimeTable.setStatus("current")
_CfprCommDateTimeEntry_Object = MibTableRow
cfprCommDateTimeEntry = _CfprCommDateTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1)
)
cfprCommDateTimeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommDateTimeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommDateTimeEntry.setStatus("current")
_CfprCommDateTimeInstanceId_Type = CfprManagedObjectId
_CfprCommDateTimeInstanceId_Object = MibTableColumn
cfprCommDateTimeInstanceId = _CfprCommDateTimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 1),
    _CfprCommDateTimeInstanceId_Type()
)
cfprCommDateTimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommDateTimeInstanceId.setStatus("current")
_CfprCommDateTimeDn_Type = CfprManagedObjectDn
_CfprCommDateTimeDn_Object = MibTableColumn
cfprCommDateTimeDn = _CfprCommDateTimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 2),
    _CfprCommDateTimeDn_Type()
)
cfprCommDateTimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeDn.setStatus("current")
_CfprCommDateTimeRn_Type = SnmpAdminString
_CfprCommDateTimeRn_Object = MibTableColumn
cfprCommDateTimeRn = _CfprCommDateTimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 3),
    _CfprCommDateTimeRn_Type()
)
cfprCommDateTimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeRn.setStatus("current")
_CfprCommDateTimeAdminState_Type = CfprCommAdminState
_CfprCommDateTimeAdminState_Object = MibTableColumn
cfprCommDateTimeAdminState = _CfprCommDateTimeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 4),
    _CfprCommDateTimeAdminState_Type()
)
cfprCommDateTimeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeAdminState.setStatus("current")
_CfprCommDateTimeConfigState_Type = CfprCommTimeZoneConfigState
_CfprCommDateTimeConfigState_Object = MibTableColumn
cfprCommDateTimeConfigState = _CfprCommDateTimeConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 5),
    _CfprCommDateTimeConfigState_Type()
)
cfprCommDateTimeConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeConfigState.setStatus("current")
_CfprCommDateTimeDate_Type = DateAndTime
_CfprCommDateTimeDate_Object = MibTableColumn
cfprCommDateTimeDate = _CfprCommDateTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 6),
    _CfprCommDateTimeDate_Type()
)
cfprCommDateTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeDate.setStatus("current")
_CfprCommDateTimeDescr_Type = SnmpAdminString
_CfprCommDateTimeDescr_Object = MibTableColumn
cfprCommDateTimeDescr = _CfprCommDateTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 7),
    _CfprCommDateTimeDescr_Type()
)
cfprCommDateTimeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeDescr.setStatus("current")
_CfprCommDateTimeIntId_Type = SnmpAdminString
_CfprCommDateTimeIntId_Object = MibTableColumn
cfprCommDateTimeIntId = _CfprCommDateTimeIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 8),
    _CfprCommDateTimeIntId_Type()
)
cfprCommDateTimeIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeIntId.setStatus("current")
_CfprCommDateTimeName_Type = SnmpAdminString
_CfprCommDateTimeName_Object = MibTableColumn
cfprCommDateTimeName = _CfprCommDateTimeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 9),
    _CfprCommDateTimeName_Type()
)
cfprCommDateTimeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeName.setStatus("current")
_CfprCommDateTimeOperPort_Type = Gauge32
_CfprCommDateTimeOperPort_Object = MibTableColumn
cfprCommDateTimeOperPort = _CfprCommDateTimeOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 10),
    _CfprCommDateTimeOperPort_Type()
)
cfprCommDateTimeOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeOperPort.setStatus("current")
_CfprCommDateTimeOperTimezone_Type = SnmpAdminString
_CfprCommDateTimeOperTimezone_Object = MibTableColumn
cfprCommDateTimeOperTimezone = _CfprCommDateTimeOperTimezone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 11),
    _CfprCommDateTimeOperTimezone_Type()
)
cfprCommDateTimeOperTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeOperTimezone.setStatus("current")
_CfprCommDateTimePolicyLevel_Type = Gauge32
_CfprCommDateTimePolicyLevel_Object = MibTableColumn
cfprCommDateTimePolicyLevel = _CfprCommDateTimePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 12),
    _CfprCommDateTimePolicyLevel_Type()
)
cfprCommDateTimePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimePolicyLevel.setStatus("current")
_CfprCommDateTimePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommDateTimePolicyOwner_Object = MibTableColumn
cfprCommDateTimePolicyOwner = _CfprCommDateTimePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 13),
    _CfprCommDateTimePolicyOwner_Type()
)
cfprCommDateTimePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimePolicyOwner.setStatus("current")
_CfprCommDateTimePort_Type = Gauge32
_CfprCommDateTimePort_Object = MibTableColumn
cfprCommDateTimePort = _CfprCommDateTimePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 14),
    _CfprCommDateTimePort_Type()
)
cfprCommDateTimePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimePort.setStatus("current")
_CfprCommDateTimeProto_Type = CfprCommProtocol
_CfprCommDateTimeProto_Object = MibTableColumn
cfprCommDateTimeProto = _CfprCommDateTimeProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 15),
    _CfprCommDateTimeProto_Type()
)
cfprCommDateTimeProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeProto.setStatus("current")
_CfprCommDateTimeTimezone_Type = SnmpAdminString
_CfprCommDateTimeTimezone_Object = MibTableColumn
cfprCommDateTimeTimezone = _CfprCommDateTimeTimezone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 16),
    _CfprCommDateTimeTimezone_Type()
)
cfprCommDateTimeTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeTimezone.setStatus("current")
_CfprCommDateTimeNtpAuthState_Type = CfprCommNtpAuthState
_CfprCommDateTimeNtpAuthState_Object = MibTableColumn
cfprCommDateTimeNtpAuthState = _CfprCommDateTimeNtpAuthState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 17),
    _CfprCommDateTimeNtpAuthState_Type()
)
cfprCommDateTimeNtpAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeNtpAuthState.setStatus("current")
_CfprCommDateTimeSysTimeSyncStatus_Type = CfprCommSysTimeSyncStatus
_CfprCommDateTimeSysTimeSyncStatus_Object = MibTableColumn
cfprCommDateTimeSysTimeSyncStatus = _CfprCommDateTimeSysTimeSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 3, 1, 18),
    _CfprCommDateTimeSysTimeSyncStatus_Type()
)
cfprCommDateTimeSysTimeSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDateTimeSysTimeSyncStatus.setStatus("current")
_CfprCommDnsTable_Object = MibTable
cfprCommDnsTable = _CfprCommDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4)
)
if mibBuilder.loadTexts:
    cfprCommDnsTable.setStatus("current")
_CfprCommDnsEntry_Object = MibTableRow
cfprCommDnsEntry = _CfprCommDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1)
)
cfprCommDnsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommDnsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommDnsEntry.setStatus("current")
_CfprCommDnsInstanceId_Type = CfprManagedObjectId
_CfprCommDnsInstanceId_Object = MibTableColumn
cfprCommDnsInstanceId = _CfprCommDnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 1),
    _CfprCommDnsInstanceId_Type()
)
cfprCommDnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommDnsInstanceId.setStatus("current")
_CfprCommDnsDn_Type = CfprManagedObjectDn
_CfprCommDnsDn_Object = MibTableColumn
cfprCommDnsDn = _CfprCommDnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 2),
    _CfprCommDnsDn_Type()
)
cfprCommDnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsDn.setStatus("current")
_CfprCommDnsRn_Type = SnmpAdminString
_CfprCommDnsRn_Object = MibTableColumn
cfprCommDnsRn = _CfprCommDnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 3),
    _CfprCommDnsRn_Type()
)
cfprCommDnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsRn.setStatus("current")
_CfprCommDnsAdminState_Type = CfprCommAdminState
_CfprCommDnsAdminState_Object = MibTableColumn
cfprCommDnsAdminState = _CfprCommDnsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 4),
    _CfprCommDnsAdminState_Type()
)
cfprCommDnsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsAdminState.setStatus("current")
_CfprCommDnsDescr_Type = SnmpAdminString
_CfprCommDnsDescr_Object = MibTableColumn
cfprCommDnsDescr = _CfprCommDnsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 5),
    _CfprCommDnsDescr_Type()
)
cfprCommDnsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsDescr.setStatus("current")
_CfprCommDnsDomain_Type = SnmpAdminString
_CfprCommDnsDomain_Object = MibTableColumn
cfprCommDnsDomain = _CfprCommDnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 6),
    _CfprCommDnsDomain_Type()
)
cfprCommDnsDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsDomain.setStatus("current")
_CfprCommDnsIntId_Type = SnmpAdminString
_CfprCommDnsIntId_Object = MibTableColumn
cfprCommDnsIntId = _CfprCommDnsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 7),
    _CfprCommDnsIntId_Type()
)
cfprCommDnsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsIntId.setStatus("current")
_CfprCommDnsName_Type = SnmpAdminString
_CfprCommDnsName_Object = MibTableColumn
cfprCommDnsName = _CfprCommDnsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 8),
    _CfprCommDnsName_Type()
)
cfprCommDnsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsName.setStatus("current")
_CfprCommDnsOperPort_Type = Gauge32
_CfprCommDnsOperPort_Object = MibTableColumn
cfprCommDnsOperPort = _CfprCommDnsOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 9),
    _CfprCommDnsOperPort_Type()
)
cfprCommDnsOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsOperPort.setStatus("current")
_CfprCommDnsPolicyLevel_Type = Gauge32
_CfprCommDnsPolicyLevel_Object = MibTableColumn
cfprCommDnsPolicyLevel = _CfprCommDnsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 10),
    _CfprCommDnsPolicyLevel_Type()
)
cfprCommDnsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsPolicyLevel.setStatus("current")
_CfprCommDnsPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommDnsPolicyOwner_Object = MibTableColumn
cfprCommDnsPolicyOwner = _CfprCommDnsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 11),
    _CfprCommDnsPolicyOwner_Type()
)
cfprCommDnsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsPolicyOwner.setStatus("current")
_CfprCommDnsPort_Type = Gauge32
_CfprCommDnsPort_Object = MibTableColumn
cfprCommDnsPort = _CfprCommDnsPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 12),
    _CfprCommDnsPort_Type()
)
cfprCommDnsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsPort.setStatus("current")
_CfprCommDnsProto_Type = CfprCommProtocol
_CfprCommDnsProto_Object = MibTableColumn
cfprCommDnsProto = _CfprCommDnsProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 4, 1, 13),
    _CfprCommDnsProto_Type()
)
cfprCommDnsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsProto.setStatus("current")
_CfprCommDnsProviderTable_Object = MibTable
cfprCommDnsProviderTable = _CfprCommDnsProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5)
)
if mibBuilder.loadTexts:
    cfprCommDnsProviderTable.setStatus("current")
_CfprCommDnsProviderEntry_Object = MibTableRow
cfprCommDnsProviderEntry = _CfprCommDnsProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5, 1)
)
cfprCommDnsProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommDnsProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommDnsProviderEntry.setStatus("current")
_CfprCommDnsProviderInstanceId_Type = CfprManagedObjectId
_CfprCommDnsProviderInstanceId_Object = MibTableColumn
cfprCommDnsProviderInstanceId = _CfprCommDnsProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5, 1, 1),
    _CfprCommDnsProviderInstanceId_Type()
)
cfprCommDnsProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommDnsProviderInstanceId.setStatus("current")
_CfprCommDnsProviderDn_Type = CfprManagedObjectDn
_CfprCommDnsProviderDn_Object = MibTableColumn
cfprCommDnsProviderDn = _CfprCommDnsProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5, 1, 2),
    _CfprCommDnsProviderDn_Type()
)
cfprCommDnsProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsProviderDn.setStatus("current")
_CfprCommDnsProviderRn_Type = SnmpAdminString
_CfprCommDnsProviderRn_Object = MibTableColumn
cfprCommDnsProviderRn = _CfprCommDnsProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5, 1, 3),
    _CfprCommDnsProviderRn_Type()
)
cfprCommDnsProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsProviderRn.setStatus("current")
_CfprCommDnsProviderAdminState_Type = CfprCommDnsProviderAdminState
_CfprCommDnsProviderAdminState_Object = MibTableColumn
cfprCommDnsProviderAdminState = _CfprCommDnsProviderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5, 1, 4),
    _CfprCommDnsProviderAdminState_Type()
)
cfprCommDnsProviderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsProviderAdminState.setStatus("current")
_CfprCommDnsProviderDescr_Type = SnmpAdminString
_CfprCommDnsProviderDescr_Object = MibTableColumn
cfprCommDnsProviderDescr = _CfprCommDnsProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5, 1, 5),
    _CfprCommDnsProviderDescr_Type()
)
cfprCommDnsProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsProviderDescr.setStatus("current")
_CfprCommDnsProviderHostname_Type = SnmpAdminString
_CfprCommDnsProviderHostname_Object = MibTableColumn
cfprCommDnsProviderHostname = _CfprCommDnsProviderHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5, 1, 6),
    _CfprCommDnsProviderHostname_Type()
)
cfprCommDnsProviderHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsProviderHostname.setStatus("current")
_CfprCommDnsProviderName_Type = SnmpAdminString
_CfprCommDnsProviderName_Object = MibTableColumn
cfprCommDnsProviderName = _CfprCommDnsProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 5, 1, 7),
    _CfprCommDnsProviderName_Type()
)
cfprCommDnsProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDnsProviderName.setStatus("current")
_CfprCommEvtChannelTable_Object = MibTable
cfprCommEvtChannelTable = _CfprCommEvtChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6)
)
if mibBuilder.loadTexts:
    cfprCommEvtChannelTable.setStatus("current")
_CfprCommEvtChannelEntry_Object = MibTableRow
cfprCommEvtChannelEntry = _CfprCommEvtChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1)
)
cfprCommEvtChannelEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommEvtChannelInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommEvtChannelEntry.setStatus("current")
_CfprCommEvtChannelInstanceId_Type = CfprManagedObjectId
_CfprCommEvtChannelInstanceId_Object = MibTableColumn
cfprCommEvtChannelInstanceId = _CfprCommEvtChannelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 1),
    _CfprCommEvtChannelInstanceId_Type()
)
cfprCommEvtChannelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommEvtChannelInstanceId.setStatus("current")
_CfprCommEvtChannelDn_Type = CfprManagedObjectDn
_CfprCommEvtChannelDn_Object = MibTableColumn
cfprCommEvtChannelDn = _CfprCommEvtChannelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 2),
    _CfprCommEvtChannelDn_Type()
)
cfprCommEvtChannelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommEvtChannelDn.setStatus("current")
_CfprCommEvtChannelRn_Type = SnmpAdminString
_CfprCommEvtChannelRn_Object = MibTableColumn
cfprCommEvtChannelRn = _CfprCommEvtChannelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 3),
    _CfprCommEvtChannelRn_Type()
)
cfprCommEvtChannelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommEvtChannelRn.setStatus("current")
_CfprCommEvtChannelChannelState_Type = CfprCommChannel
_CfprCommEvtChannelChannelState_Object = MibTableColumn
cfprCommEvtChannelChannelState = _CfprCommEvtChannelChannelState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 4),
    _CfprCommEvtChannelChannelState_Type()
)
cfprCommEvtChannelChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommEvtChannelChannelState.setStatus("current")
_CfprCommEvtChannelDescr_Type = SnmpAdminString
_CfprCommEvtChannelDescr_Object = MibTableColumn
cfprCommEvtChannelDescr = _CfprCommEvtChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 5),
    _CfprCommEvtChannelDescr_Type()
)
cfprCommEvtChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommEvtChannelDescr.setStatus("current")
_CfprCommEvtChannelIntId_Type = SnmpAdminString
_CfprCommEvtChannelIntId_Object = MibTableColumn
cfprCommEvtChannelIntId = _CfprCommEvtChannelIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 6),
    _CfprCommEvtChannelIntId_Type()
)
cfprCommEvtChannelIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommEvtChannelIntId.setStatus("current")
_CfprCommEvtChannelName_Type = SnmpAdminString
_CfprCommEvtChannelName_Object = MibTableColumn
cfprCommEvtChannelName = _CfprCommEvtChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 7),
    _CfprCommEvtChannelName_Type()
)
cfprCommEvtChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommEvtChannelName.setStatus("current")
_CfprCommEvtChannelPolicyLevel_Type = Gauge32
_CfprCommEvtChannelPolicyLevel_Object = MibTableColumn
cfprCommEvtChannelPolicyLevel = _CfprCommEvtChannelPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 8),
    _CfprCommEvtChannelPolicyLevel_Type()
)
cfprCommEvtChannelPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommEvtChannelPolicyLevel.setStatus("current")
_CfprCommEvtChannelPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommEvtChannelPolicyOwner_Object = MibTableColumn
cfprCommEvtChannelPolicyOwner = _CfprCommEvtChannelPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 6, 1, 9),
    _CfprCommEvtChannelPolicyOwner_Type()
)
cfprCommEvtChannelPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommEvtChannelPolicyOwner.setStatus("current")
_CfprCommHttpsTable_Object = MibTable
cfprCommHttpsTable = _CfprCommHttpsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8)
)
if mibBuilder.loadTexts:
    cfprCommHttpsTable.setStatus("current")
_CfprCommHttpsEntry_Object = MibTableRow
cfprCommHttpsEntry = _CfprCommHttpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1)
)
cfprCommHttpsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommHttpsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommHttpsEntry.setStatus("current")
_CfprCommHttpsInstanceId_Type = CfprManagedObjectId
_CfprCommHttpsInstanceId_Object = MibTableColumn
cfprCommHttpsInstanceId = _CfprCommHttpsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 1),
    _CfprCommHttpsInstanceId_Type()
)
cfprCommHttpsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommHttpsInstanceId.setStatus("current")
_CfprCommHttpsDn_Type = CfprManagedObjectDn
_CfprCommHttpsDn_Object = MibTableColumn
cfprCommHttpsDn = _CfprCommHttpsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 2),
    _CfprCommHttpsDn_Type()
)
cfprCommHttpsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsDn.setStatus("current")
_CfprCommHttpsRn_Type = SnmpAdminString
_CfprCommHttpsRn_Object = MibTableColumn
cfprCommHttpsRn = _CfprCommHttpsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 3),
    _CfprCommHttpsRn_Type()
)
cfprCommHttpsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsRn.setStatus("current")
_CfprCommHttpsAdminState_Type = CfprCommAdminState
_CfprCommHttpsAdminState_Object = MibTableColumn
cfprCommHttpsAdminState = _CfprCommHttpsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 4),
    _CfprCommHttpsAdminState_Type()
)
cfprCommHttpsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsAdminState.setStatus("current")
_CfprCommHttpsCipherSuite_Type = SnmpAdminString
_CfprCommHttpsCipherSuite_Object = MibTableColumn
cfprCommHttpsCipherSuite = _CfprCommHttpsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 5),
    _CfprCommHttpsCipherSuite_Type()
)
cfprCommHttpsCipherSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsCipherSuite.setStatus("current")
_CfprCommHttpsCipherSuiteMode_Type = CfprCommCipherSuiteMode
_CfprCommHttpsCipherSuiteMode_Object = MibTableColumn
cfprCommHttpsCipherSuiteMode = _CfprCommHttpsCipherSuiteMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 6),
    _CfprCommHttpsCipherSuiteMode_Type()
)
cfprCommHttpsCipherSuiteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsCipherSuiteMode.setStatus("current")
_CfprCommHttpsDescr_Type = SnmpAdminString
_CfprCommHttpsDescr_Object = MibTableColumn
cfprCommHttpsDescr = _CfprCommHttpsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 7),
    _CfprCommHttpsDescr_Type()
)
cfprCommHttpsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsDescr.setStatus("current")
_CfprCommHttpsIntId_Type = SnmpAdminString
_CfprCommHttpsIntId_Object = MibTableColumn
cfprCommHttpsIntId = _CfprCommHttpsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 8),
    _CfprCommHttpsIntId_Type()
)
cfprCommHttpsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsIntId.setStatus("current")
_CfprCommHttpsKeyRing_Type = SnmpAdminString
_CfprCommHttpsKeyRing_Object = MibTableColumn
cfprCommHttpsKeyRing = _CfprCommHttpsKeyRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 9),
    _CfprCommHttpsKeyRing_Type()
)
cfprCommHttpsKeyRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsKeyRing.setStatus("current")
_CfprCommHttpsName_Type = SnmpAdminString
_CfprCommHttpsName_Object = MibTableColumn
cfprCommHttpsName = _CfprCommHttpsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 10),
    _CfprCommHttpsName_Type()
)
cfprCommHttpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsName.setStatus("current")
_CfprCommHttpsOperPort_Type = Gauge32
_CfprCommHttpsOperPort_Object = MibTableColumn
cfprCommHttpsOperPort = _CfprCommHttpsOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 11),
    _CfprCommHttpsOperPort_Type()
)
cfprCommHttpsOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsOperPort.setStatus("current")
_CfprCommHttpsPolicyLevel_Type = Gauge32
_CfprCommHttpsPolicyLevel_Object = MibTableColumn
cfprCommHttpsPolicyLevel = _CfprCommHttpsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 12),
    _CfprCommHttpsPolicyLevel_Type()
)
cfprCommHttpsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsPolicyLevel.setStatus("current")
_CfprCommHttpsPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommHttpsPolicyOwner_Object = MibTableColumn
cfprCommHttpsPolicyOwner = _CfprCommHttpsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 13),
    _CfprCommHttpsPolicyOwner_Type()
)
cfprCommHttpsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsPolicyOwner.setStatus("current")
_CfprCommHttpsPort_Type = Gauge32
_CfprCommHttpsPort_Object = MibTableColumn
cfprCommHttpsPort = _CfprCommHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 14),
    _CfprCommHttpsPort_Type()
)
cfprCommHttpsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsPort.setStatus("current")
_CfprCommHttpsProto_Type = CfprCommWebProto
_CfprCommHttpsProto_Object = MibTableColumn
cfprCommHttpsProto = _CfprCommHttpsProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 15),
    _CfprCommHttpsProto_Type()
)
cfprCommHttpsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsProto.setStatus("current")
_CfprCommHttpsAuthType_Type = CfprCommHttpsAuthType
_CfprCommHttpsAuthType_Object = MibTableColumn
cfprCommHttpsAuthType = _CfprCommHttpsAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 16),
    _CfprCommHttpsAuthType_Type()
)
cfprCommHttpsAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsAuthType.setStatus("current")
_CfprCommHttpsCrlMode_Type = CfprCommCrlModeType
_CfprCommHttpsCrlMode_Object = MibTableColumn
cfprCommHttpsCrlMode = _CfprCommHttpsCrlMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 17),
    _CfprCommHttpsCrlMode_Type()
)
cfprCommHttpsCrlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsCrlMode.setStatus("current")
_CfprCommHttpsTlsVer_Type = CfprCommTlsVerType
_CfprCommHttpsTlsVer_Object = MibTableColumn
cfprCommHttpsTlsVer = _CfprCommHttpsTlsVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 8, 1, 18),
    _CfprCommHttpsTlsVer_Type()
)
cfprCommHttpsTlsVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommHttpsTlsVer.setStatus("current")
_CfprCommNtpProviderTable_Object = MibTable
cfprCommNtpProviderTable = _CfprCommNtpProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9)
)
if mibBuilder.loadTexts:
    cfprCommNtpProviderTable.setStatus("current")
_CfprCommNtpProviderEntry_Object = MibTableRow
cfprCommNtpProviderEntry = _CfprCommNtpProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1)
)
cfprCommNtpProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommNtpProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommNtpProviderEntry.setStatus("current")
_CfprCommNtpProviderInstanceId_Type = CfprManagedObjectId
_CfprCommNtpProviderInstanceId_Object = MibTableColumn
cfprCommNtpProviderInstanceId = _CfprCommNtpProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 1),
    _CfprCommNtpProviderInstanceId_Type()
)
cfprCommNtpProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommNtpProviderInstanceId.setStatus("current")
_CfprCommNtpProviderDn_Type = CfprManagedObjectDn
_CfprCommNtpProviderDn_Object = MibTableColumn
cfprCommNtpProviderDn = _CfprCommNtpProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 2),
    _CfprCommNtpProviderDn_Type()
)
cfprCommNtpProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderDn.setStatus("current")
_CfprCommNtpProviderRn_Type = SnmpAdminString
_CfprCommNtpProviderRn_Object = MibTableColumn
cfprCommNtpProviderRn = _CfprCommNtpProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 3),
    _CfprCommNtpProviderRn_Type()
)
cfprCommNtpProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderRn.setStatus("current")
_CfprCommNtpProviderAdminState_Type = CfprCommNtpProviderAdminState
_CfprCommNtpProviderAdminState_Object = MibTableColumn
cfprCommNtpProviderAdminState = _CfprCommNtpProviderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 4),
    _CfprCommNtpProviderAdminState_Type()
)
cfprCommNtpProviderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderAdminState.setStatus("current")
_CfprCommNtpProviderDescr_Type = SnmpAdminString
_CfprCommNtpProviderDescr_Object = MibTableColumn
cfprCommNtpProviderDescr = _CfprCommNtpProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 5),
    _CfprCommNtpProviderDescr_Type()
)
cfprCommNtpProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderDescr.setStatus("current")
_CfprCommNtpProviderHostname_Type = SnmpAdminString
_CfprCommNtpProviderHostname_Object = MibTableColumn
cfprCommNtpProviderHostname = _CfprCommNtpProviderHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 6),
    _CfprCommNtpProviderHostname_Type()
)
cfprCommNtpProviderHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderHostname.setStatus("current")
_CfprCommNtpProviderName_Type = SnmpAdminString
_CfprCommNtpProviderName_Object = MibTableColumn
cfprCommNtpProviderName = _CfprCommNtpProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 7),
    _CfprCommNtpProviderName_Type()
)
cfprCommNtpProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderName.setStatus("current")
_CfprCommNtpProviderDynamicIp_Type = SnmpAdminString
_CfprCommNtpProviderDynamicIp_Object = MibTableColumn
cfprCommNtpProviderDynamicIp = _CfprCommNtpProviderDynamicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 8),
    _CfprCommNtpProviderDynamicIp_Type()
)
cfprCommNtpProviderDynamicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderDynamicIp.setStatus("current")
_CfprCommNtpProviderErrorMsg_Type = SnmpAdminString
_CfprCommNtpProviderErrorMsg_Object = MibTableColumn
cfprCommNtpProviderErrorMsg = _CfprCommNtpProviderErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 9),
    _CfprCommNtpProviderErrorMsg_Type()
)
cfprCommNtpProviderErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderErrorMsg.setStatus("current")
_CfprCommNtpProviderKeyStringSet_Type = TruthValue
_CfprCommNtpProviderKeyStringSet_Object = MibTableColumn
cfprCommNtpProviderKeyStringSet = _CfprCommNtpProviderKeyStringSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 10),
    _CfprCommNtpProviderKeyStringSet_Type()
)
cfprCommNtpProviderKeyStringSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderKeyStringSet.setStatus("current")
_CfprCommNtpProviderReachability_Type = TruthValue
_CfprCommNtpProviderReachability_Object = MibTableColumn
cfprCommNtpProviderReachability = _CfprCommNtpProviderReachability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 11),
    _CfprCommNtpProviderReachability_Type()
)
cfprCommNtpProviderReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderReachability.setStatus("current")
_CfprCommNtpProviderReceivedInvalidNtpStatusCount_Type = Gauge32
_CfprCommNtpProviderReceivedInvalidNtpStatusCount_Object = MibTableColumn
cfprCommNtpProviderReceivedInvalidNtpStatusCount = _CfprCommNtpProviderReceivedInvalidNtpStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 12),
    _CfprCommNtpProviderReceivedInvalidNtpStatusCount_Type()
)
cfprCommNtpProviderReceivedInvalidNtpStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderReceivedInvalidNtpStatusCount.setStatus("current")
_CfprCommNtpProviderSha1KeyId_Type = CfprCommNtpSha1Id
_CfprCommNtpProviderSha1KeyId_Object = MibTableColumn
cfprCommNtpProviderSha1KeyId = _CfprCommNtpProviderSha1KeyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 13),
    _CfprCommNtpProviderSha1KeyId_Type()
)
cfprCommNtpProviderSha1KeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderSha1KeyId.setStatus("current")
_CfprCommNtpProviderSha1KeyString_Type = SnmpAdminString
_CfprCommNtpProviderSha1KeyString_Object = MibTableColumn
cfprCommNtpProviderSha1KeyString = _CfprCommNtpProviderSha1KeyString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 14),
    _CfprCommNtpProviderSha1KeyString_Type()
)
cfprCommNtpProviderSha1KeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderSha1KeyString.setStatus("current")
_CfprCommNtpProviderTimeSyncStatus_Type = CfprCommTimeSyncStatus
_CfprCommNtpProviderTimeSyncStatus_Object = MibTableColumn
cfprCommNtpProviderTimeSyncStatus = _CfprCommNtpProviderTimeSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 15),
    _CfprCommNtpProviderTimeSyncStatus_Type()
)
cfprCommNtpProviderTimeSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderTimeSyncStatus.setStatus("current")
_CfprCommNtpProviderCheckStratum_Type = TruthValue
_CfprCommNtpProviderCheckStratum_Object = MibTableColumn
cfprCommNtpProviderCheckStratum = _CfprCommNtpProviderCheckStratum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 9, 1, 16),
    _CfprCommNtpProviderCheckStratum_Type()
)
cfprCommNtpProviderCheckStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommNtpProviderCheckStratum.setStatus("current")
_CfprCommShellSvcLimitsTable_Object = MibTable
cfprCommShellSvcLimitsTable = _CfprCommShellSvcLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10)
)
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsTable.setStatus("current")
_CfprCommShellSvcLimitsEntry_Object = MibTableRow
cfprCommShellSvcLimitsEntry = _CfprCommShellSvcLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1)
)
cfprCommShellSvcLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommShellSvcLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsEntry.setStatus("current")
_CfprCommShellSvcLimitsInstanceId_Type = CfprManagedObjectId
_CfprCommShellSvcLimitsInstanceId_Object = MibTableColumn
cfprCommShellSvcLimitsInstanceId = _CfprCommShellSvcLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 1),
    _CfprCommShellSvcLimitsInstanceId_Type()
)
cfprCommShellSvcLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsInstanceId.setStatus("current")
_CfprCommShellSvcLimitsDn_Type = CfprManagedObjectDn
_CfprCommShellSvcLimitsDn_Object = MibTableColumn
cfprCommShellSvcLimitsDn = _CfprCommShellSvcLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 2),
    _CfprCommShellSvcLimitsDn_Type()
)
cfprCommShellSvcLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsDn.setStatus("current")
_CfprCommShellSvcLimitsRn_Type = SnmpAdminString
_CfprCommShellSvcLimitsRn_Object = MibTableColumn
cfprCommShellSvcLimitsRn = _CfprCommShellSvcLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 3),
    _CfprCommShellSvcLimitsRn_Type()
)
cfprCommShellSvcLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsRn.setStatus("current")
_CfprCommShellSvcLimitsDescr_Type = SnmpAdminString
_CfprCommShellSvcLimitsDescr_Object = MibTableColumn
cfprCommShellSvcLimitsDescr = _CfprCommShellSvcLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 4),
    _CfprCommShellSvcLimitsDescr_Type()
)
cfprCommShellSvcLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsDescr.setStatus("current")
_CfprCommShellSvcLimitsIntId_Type = SnmpAdminString
_CfprCommShellSvcLimitsIntId_Object = MibTableColumn
cfprCommShellSvcLimitsIntId = _CfprCommShellSvcLimitsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 5),
    _CfprCommShellSvcLimitsIntId_Type()
)
cfprCommShellSvcLimitsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsIntId.setStatus("current")
_CfprCommShellSvcLimitsName_Type = SnmpAdminString
_CfprCommShellSvcLimitsName_Object = MibTableColumn
cfprCommShellSvcLimitsName = _CfprCommShellSvcLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 6),
    _CfprCommShellSvcLimitsName_Type()
)
cfprCommShellSvcLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsName.setStatus("current")
_CfprCommShellSvcLimitsPolicyLevel_Type = Gauge32
_CfprCommShellSvcLimitsPolicyLevel_Object = MibTableColumn
cfprCommShellSvcLimitsPolicyLevel = _CfprCommShellSvcLimitsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 7),
    _CfprCommShellSvcLimitsPolicyLevel_Type()
)
cfprCommShellSvcLimitsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsPolicyLevel.setStatus("current")
_CfprCommShellSvcLimitsPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommShellSvcLimitsPolicyOwner_Object = MibTableColumn
cfprCommShellSvcLimitsPolicyOwner = _CfprCommShellSvcLimitsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 8),
    _CfprCommShellSvcLimitsPolicyOwner_Type()
)
cfprCommShellSvcLimitsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsPolicyOwner.setStatus("current")
_CfprCommShellSvcLimitsSessionsPerUser_Type = Gauge32
_CfprCommShellSvcLimitsSessionsPerUser_Object = MibTableColumn
cfprCommShellSvcLimitsSessionsPerUser = _CfprCommShellSvcLimitsSessionsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 9),
    _CfprCommShellSvcLimitsSessionsPerUser_Type()
)
cfprCommShellSvcLimitsSessionsPerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsSessionsPerUser.setStatus("current")
_CfprCommShellSvcLimitsTotalSessions_Type = Gauge32
_CfprCommShellSvcLimitsTotalSessions_Object = MibTableColumn
cfprCommShellSvcLimitsTotalSessions = _CfprCommShellSvcLimitsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 10, 1, 10),
    _CfprCommShellSvcLimitsTotalSessions_Type()
)
cfprCommShellSvcLimitsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommShellSvcLimitsTotalSessions.setStatus("current")
_CfprCommSnmpTable_Object = MibTable
cfprCommSnmpTable = _CfprCommSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12)
)
if mibBuilder.loadTexts:
    cfprCommSnmpTable.setStatus("current")
_CfprCommSnmpEntry_Object = MibTableRow
cfprCommSnmpEntry = _CfprCommSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1)
)
cfprCommSnmpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSnmpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSnmpEntry.setStatus("current")
_CfprCommSnmpInstanceId_Type = CfprManagedObjectId
_CfprCommSnmpInstanceId_Object = MibTableColumn
cfprCommSnmpInstanceId = _CfprCommSnmpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 1),
    _CfprCommSnmpInstanceId_Type()
)
cfprCommSnmpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSnmpInstanceId.setStatus("current")
_CfprCommSnmpDn_Type = CfprManagedObjectDn
_CfprCommSnmpDn_Object = MibTableColumn
cfprCommSnmpDn = _CfprCommSnmpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 2),
    _CfprCommSnmpDn_Type()
)
cfprCommSnmpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpDn.setStatus("current")
_CfprCommSnmpRn_Type = SnmpAdminString
_CfprCommSnmpRn_Object = MibTableColumn
cfprCommSnmpRn = _CfprCommSnmpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 3),
    _CfprCommSnmpRn_Type()
)
cfprCommSnmpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpRn.setStatus("current")
_CfprCommSnmpAdminState_Type = CfprCommAdminState
_CfprCommSnmpAdminState_Object = MibTableColumn
cfprCommSnmpAdminState = _CfprCommSnmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 4),
    _CfprCommSnmpAdminState_Type()
)
cfprCommSnmpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpAdminState.setStatus("current")
_CfprCommSnmpCommunity_Type = SnmpAdminString
_CfprCommSnmpCommunity_Object = MibTableColumn
cfprCommSnmpCommunity = _CfprCommSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 5),
    _CfprCommSnmpCommunity_Type()
)
cfprCommSnmpCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpCommunity.setStatus("current")
_CfprCommSnmpConfigState_Type = CfprCommSnmpConfigState
_CfprCommSnmpConfigState_Object = MibTableColumn
cfprCommSnmpConfigState = _CfprCommSnmpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 6),
    _CfprCommSnmpConfigState_Type()
)
cfprCommSnmpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpConfigState.setStatus("current")
_CfprCommSnmpDescr_Type = SnmpAdminString
_CfprCommSnmpDescr_Object = MibTableColumn
cfprCommSnmpDescr = _CfprCommSnmpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 7),
    _CfprCommSnmpDescr_Type()
)
cfprCommSnmpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpDescr.setStatus("current")
_CfprCommSnmpIntId_Type = SnmpAdminString
_CfprCommSnmpIntId_Object = MibTableColumn
cfprCommSnmpIntId = _CfprCommSnmpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 8),
    _CfprCommSnmpIntId_Type()
)
cfprCommSnmpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpIntId.setStatus("current")
_CfprCommSnmpIsSetSnmpSecure_Type = TruthValue
_CfprCommSnmpIsSetSnmpSecure_Object = MibTableColumn
cfprCommSnmpIsSetSnmpSecure = _CfprCommSnmpIsSetSnmpSecure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 9),
    _CfprCommSnmpIsSetSnmpSecure_Type()
)
cfprCommSnmpIsSetSnmpSecure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpIsSetSnmpSecure.setStatus("current")
_CfprCommSnmpName_Type = SnmpAdminString
_CfprCommSnmpName_Object = MibTableColumn
cfprCommSnmpName = _CfprCommSnmpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 10),
    _CfprCommSnmpName_Type()
)
cfprCommSnmpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpName.setStatus("current")
_CfprCommSnmpOperPort_Type = Gauge32
_CfprCommSnmpOperPort_Object = MibTableColumn
cfprCommSnmpOperPort = _CfprCommSnmpOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 11),
    _CfprCommSnmpOperPort_Type()
)
cfprCommSnmpOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpOperPort.setStatus("current")
_CfprCommSnmpPolicyLevel_Type = Gauge32
_CfprCommSnmpPolicyLevel_Object = MibTableColumn
cfprCommSnmpPolicyLevel = _CfprCommSnmpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 12),
    _CfprCommSnmpPolicyLevel_Type()
)
cfprCommSnmpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpPolicyLevel.setStatus("current")
_CfprCommSnmpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommSnmpPolicyOwner_Object = MibTableColumn
cfprCommSnmpPolicyOwner = _CfprCommSnmpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 13),
    _CfprCommSnmpPolicyOwner_Type()
)
cfprCommSnmpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpPolicyOwner.setStatus("current")
_CfprCommSnmpPort_Type = Gauge32
_CfprCommSnmpPort_Object = MibTableColumn
cfprCommSnmpPort = _CfprCommSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 14),
    _CfprCommSnmpPort_Type()
)
cfprCommSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpPort.setStatus("current")
_CfprCommSnmpProto_Type = CfprCommSnmpProto
_CfprCommSnmpProto_Object = MibTableColumn
cfprCommSnmpProto = _CfprCommSnmpProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 15),
    _CfprCommSnmpProto_Type()
)
cfprCommSnmpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpProto.setStatus("current")
_CfprCommSnmpSysContact_Type = SnmpAdminString
_CfprCommSnmpSysContact_Object = MibTableColumn
cfprCommSnmpSysContact = _CfprCommSnmpSysContact_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 16),
    _CfprCommSnmpSysContact_Type()
)
cfprCommSnmpSysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpSysContact.setStatus("current")
_CfprCommSnmpSysLocation_Type = SnmpAdminString
_CfprCommSnmpSysLocation_Object = MibTableColumn
cfprCommSnmpSysLocation = _CfprCommSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 17),
    _CfprCommSnmpSysLocation_Type()
)
cfprCommSnmpSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpSysLocation.setStatus("current")
_CfprCommSnmpAdminAppEnable_Type = TruthValue
_CfprCommSnmpAdminAppEnable_Object = MibTableColumn
cfprCommSnmpAdminAppEnable = _CfprCommSnmpAdminAppEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 18),
    _CfprCommSnmpAdminAppEnable_Type()
)
cfprCommSnmpAdminAppEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpAdminAppEnable.setStatus("current")
_CfprCommSnmpAdminAppId_Type = SnmpAdminString
_CfprCommSnmpAdminAppId_Object = MibTableColumn
cfprCommSnmpAdminAppId = _CfprCommSnmpAdminAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 19),
    _CfprCommSnmpAdminAppId_Type()
)
cfprCommSnmpAdminAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpAdminAppId.setStatus("current")
_CfprCommSnmpAdminAppIp_Type = SnmpAdminString
_CfprCommSnmpAdminAppIp_Object = MibTableColumn
cfprCommSnmpAdminAppIp = _CfprCommSnmpAdminAppIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 20),
    _CfprCommSnmpAdminAppIp_Type()
)
cfprCommSnmpAdminAppIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpAdminAppIp.setStatus("current")
_CfprCommSnmpAdminAppName_Type = SnmpAdminString
_CfprCommSnmpAdminAppName_Object = MibTableColumn
cfprCommSnmpAdminAppName = _CfprCommSnmpAdminAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 21),
    _CfprCommSnmpAdminAppName_Type()
)
cfprCommSnmpAdminAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpAdminAppName.setStatus("current")
_CfprCommSnmpAdminAppSlot_Type = CfprCommSnmpAdminAppSlot
_CfprCommSnmpAdminAppSlot_Object = MibTableColumn
cfprCommSnmpAdminAppSlot = _CfprCommSnmpAdminAppSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 22),
    _CfprCommSnmpAdminAppSlot_Type()
)
cfprCommSnmpAdminAppSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpAdminAppSlot.setStatus("current")
_CfprCommSnmpUnificationDisabled_Type = TruthValue
_CfprCommSnmpUnificationDisabled_Object = MibTableColumn
cfprCommSnmpUnificationDisabled = _CfprCommSnmpUnificationDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 12, 1, 23),
    _CfprCommSnmpUnificationDisabled_Type()
)
cfprCommSnmpUnificationDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUnificationDisabled.setStatus("current")
_CfprCommSnmpTrapTable_Object = MibTable
cfprCommSnmpTrapTable = _CfprCommSnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13)
)
if mibBuilder.loadTexts:
    cfprCommSnmpTrapTable.setStatus("current")
_CfprCommSnmpTrapEntry_Object = MibTableRow
cfprCommSnmpTrapEntry = _CfprCommSnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1)
)
cfprCommSnmpTrapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSnmpTrapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSnmpTrapEntry.setStatus("current")
_CfprCommSnmpTrapInstanceId_Type = CfprManagedObjectId
_CfprCommSnmpTrapInstanceId_Object = MibTableColumn
cfprCommSnmpTrapInstanceId = _CfprCommSnmpTrapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 1),
    _CfprCommSnmpTrapInstanceId_Type()
)
cfprCommSnmpTrapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapInstanceId.setStatus("current")
_CfprCommSnmpTrapDn_Type = CfprManagedObjectDn
_CfprCommSnmpTrapDn_Object = MibTableColumn
cfprCommSnmpTrapDn = _CfprCommSnmpTrapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 2),
    _CfprCommSnmpTrapDn_Type()
)
cfprCommSnmpTrapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapDn.setStatus("current")
_CfprCommSnmpTrapRn_Type = SnmpAdminString
_CfprCommSnmpTrapRn_Object = MibTableColumn
cfprCommSnmpTrapRn = _CfprCommSnmpTrapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 3),
    _CfprCommSnmpTrapRn_Type()
)
cfprCommSnmpTrapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapRn.setStatus("current")
_CfprCommSnmpTrapCommunity_Type = SnmpAdminString
_CfprCommSnmpTrapCommunity_Object = MibTableColumn
cfprCommSnmpTrapCommunity = _CfprCommSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 4),
    _CfprCommSnmpTrapCommunity_Type()
)
cfprCommSnmpTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapCommunity.setStatus("current")
_CfprCommSnmpTrapHostname_Type = SnmpAdminString
_CfprCommSnmpTrapHostname_Object = MibTableColumn
cfprCommSnmpTrapHostname = _CfprCommSnmpTrapHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 5),
    _CfprCommSnmpTrapHostname_Type()
)
cfprCommSnmpTrapHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapHostname.setStatus("current")
_CfprCommSnmpTrapNotificationType_Type = CfprCommSnmpNotificationType
_CfprCommSnmpTrapNotificationType_Object = MibTableColumn
cfprCommSnmpTrapNotificationType = _CfprCommSnmpTrapNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 6),
    _CfprCommSnmpTrapNotificationType_Type()
)
cfprCommSnmpTrapNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapNotificationType.setStatus("current")
_CfprCommSnmpTrapPort_Type = Gauge32
_CfprCommSnmpTrapPort_Object = MibTableColumn
cfprCommSnmpTrapPort = _CfprCommSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 7),
    _CfprCommSnmpTrapPort_Type()
)
cfprCommSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapPort.setStatus("current")
_CfprCommSnmpTrapV3Privilege_Type = CfprCommSnmpV3Privilege
_CfprCommSnmpTrapV3Privilege_Object = MibTableColumn
cfprCommSnmpTrapV3Privilege = _CfprCommSnmpTrapV3Privilege_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 8),
    _CfprCommSnmpTrapV3Privilege_Type()
)
cfprCommSnmpTrapV3Privilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapV3Privilege.setStatus("current")
_CfprCommSnmpTrapVersion_Type = CfprCommSnmpVersion
_CfprCommSnmpTrapVersion_Object = MibTableColumn
cfprCommSnmpTrapVersion = _CfprCommSnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 13, 1, 9),
    _CfprCommSnmpTrapVersion_Type()
)
cfprCommSnmpTrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpTrapVersion.setStatus("current")
_CfprCommSnmpUserTable_Object = MibTable
cfprCommSnmpUserTable = _CfprCommSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14)
)
if mibBuilder.loadTexts:
    cfprCommSnmpUserTable.setStatus("current")
_CfprCommSnmpUserEntry_Object = MibTableRow
cfprCommSnmpUserEntry = _CfprCommSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1)
)
cfprCommSnmpUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSnmpUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSnmpUserEntry.setStatus("current")
_CfprCommSnmpUserInstanceId_Type = CfprManagedObjectId
_CfprCommSnmpUserInstanceId_Object = MibTableColumn
cfprCommSnmpUserInstanceId = _CfprCommSnmpUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 1),
    _CfprCommSnmpUserInstanceId_Type()
)
cfprCommSnmpUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSnmpUserInstanceId.setStatus("current")
_CfprCommSnmpUserDn_Type = CfprManagedObjectDn
_CfprCommSnmpUserDn_Object = MibTableColumn
cfprCommSnmpUserDn = _CfprCommSnmpUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 2),
    _CfprCommSnmpUserDn_Type()
)
cfprCommSnmpUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserDn.setStatus("current")
_CfprCommSnmpUserRn_Type = SnmpAdminString
_CfprCommSnmpUserRn_Object = MibTableColumn
cfprCommSnmpUserRn = _CfprCommSnmpUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 3),
    _CfprCommSnmpUserRn_Type()
)
cfprCommSnmpUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserRn.setStatus("current")
_CfprCommSnmpUserAuth_Type = CfprCommSnmpAuth
_CfprCommSnmpUserAuth_Object = MibTableColumn
cfprCommSnmpUserAuth = _CfprCommSnmpUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 4),
    _CfprCommSnmpUserAuth_Type()
)
cfprCommSnmpUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserAuth.setStatus("current")
_CfprCommSnmpUserConfigState_Type = CfprAaaConfigState
_CfprCommSnmpUserConfigState_Object = MibTableColumn
cfprCommSnmpUserConfigState = _CfprCommSnmpUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 5),
    _CfprCommSnmpUserConfigState_Type()
)
cfprCommSnmpUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserConfigState.setStatus("current")
_CfprCommSnmpUserConfigStatusMessage_Type = SnmpAdminString
_CfprCommSnmpUserConfigStatusMessage_Object = MibTableColumn
cfprCommSnmpUserConfigStatusMessage = _CfprCommSnmpUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 6),
    _CfprCommSnmpUserConfigStatusMessage_Type()
)
cfprCommSnmpUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserConfigStatusMessage.setStatus("current")
_CfprCommSnmpUserDescr_Type = SnmpAdminString
_CfprCommSnmpUserDescr_Object = MibTableColumn
cfprCommSnmpUserDescr = _CfprCommSnmpUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 7),
    _CfprCommSnmpUserDescr_Type()
)
cfprCommSnmpUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserDescr.setStatus("current")
_CfprCommSnmpUserName_Type = SnmpAdminString
_CfprCommSnmpUserName_Object = MibTableColumn
cfprCommSnmpUserName = _CfprCommSnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 8),
    _CfprCommSnmpUserName_Type()
)
cfprCommSnmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserName.setStatus("current")
_CfprCommSnmpUserPrivPwdSet_Type = TruthValue
_CfprCommSnmpUserPrivPwdSet_Object = MibTableColumn
cfprCommSnmpUserPrivPwdSet = _CfprCommSnmpUserPrivPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 9),
    _CfprCommSnmpUserPrivPwdSet_Type()
)
cfprCommSnmpUserPrivPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserPrivPwdSet.setStatus("current")
_CfprCommSnmpUserPrivpwd_Type = SnmpAdminString
_CfprCommSnmpUserPrivpwd_Object = MibTableColumn
cfprCommSnmpUserPrivpwd = _CfprCommSnmpUserPrivpwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 10),
    _CfprCommSnmpUserPrivpwd_Type()
)
cfprCommSnmpUserPrivpwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserPrivpwd.setStatus("current")
_CfprCommSnmpUserPwd_Type = SnmpAdminString
_CfprCommSnmpUserPwd_Object = MibTableColumn
cfprCommSnmpUserPwd = _CfprCommSnmpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 11),
    _CfprCommSnmpUserPwd_Type()
)
cfprCommSnmpUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserPwd.setStatus("current")
_CfprCommSnmpUserPwdSet_Type = TruthValue
_CfprCommSnmpUserPwdSet_Object = MibTableColumn
cfprCommSnmpUserPwdSet = _CfprCommSnmpUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 12),
    _CfprCommSnmpUserPwdSet_Type()
)
cfprCommSnmpUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserPwdSet.setStatus("current")
_CfprCommSnmpUserUseAes_Type = TruthValue
_CfprCommSnmpUserUseAes_Object = MibTableColumn
cfprCommSnmpUserUseAes = _CfprCommSnmpUserUseAes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 14, 1, 13),
    _CfprCommSnmpUserUseAes_Type()
)
cfprCommSnmpUserUseAes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSnmpUserUseAes.setStatus("current")
_CfprCommSshTable_Object = MibTable
cfprCommSshTable = _CfprCommSshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15)
)
if mibBuilder.loadTexts:
    cfprCommSshTable.setStatus("current")
_CfprCommSshEntry_Object = MibTableRow
cfprCommSshEntry = _CfprCommSshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1)
)
cfprCommSshEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSshInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSshEntry.setStatus("current")
_CfprCommSshInstanceId_Type = CfprManagedObjectId
_CfprCommSshInstanceId_Object = MibTableColumn
cfprCommSshInstanceId = _CfprCommSshInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 1),
    _CfprCommSshInstanceId_Type()
)
cfprCommSshInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSshInstanceId.setStatus("current")
_CfprCommSshDn_Type = CfprManagedObjectDn
_CfprCommSshDn_Object = MibTableColumn
cfprCommSshDn = _CfprCommSshDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 2),
    _CfprCommSshDn_Type()
)
cfprCommSshDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshDn.setStatus("current")
_CfprCommSshRn_Type = SnmpAdminString
_CfprCommSshRn_Object = MibTableColumn
cfprCommSshRn = _CfprCommSshRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 3),
    _CfprCommSshRn_Type()
)
cfprCommSshRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshRn.setStatus("current")
_CfprCommSshAdminState_Type = CfprCommSshAdminState
_CfprCommSshAdminState_Object = MibTableColumn
cfprCommSshAdminState = _CfprCommSshAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 4),
    _CfprCommSshAdminState_Type()
)
cfprCommSshAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshAdminState.setStatus("current")
_CfprCommSshDescr_Type = SnmpAdminString
_CfprCommSshDescr_Object = MibTableColumn
cfprCommSshDescr = _CfprCommSshDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 5),
    _CfprCommSshDescr_Type()
)
cfprCommSshDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshDescr.setStatus("current")
_CfprCommSshIntId_Type = SnmpAdminString
_CfprCommSshIntId_Object = MibTableColumn
cfprCommSshIntId = _CfprCommSshIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 6),
    _CfprCommSshIntId_Type()
)
cfprCommSshIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshIntId.setStatus("current")
_CfprCommSshName_Type = SnmpAdminString
_CfprCommSshName_Object = MibTableColumn
cfprCommSshName = _CfprCommSshName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 7),
    _CfprCommSshName_Type()
)
cfprCommSshName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshName.setStatus("current")
_CfprCommSshOperPort_Type = Gauge32
_CfprCommSshOperPort_Object = MibTableColumn
cfprCommSshOperPort = _CfprCommSshOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 8),
    _CfprCommSshOperPort_Type()
)
cfprCommSshOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshOperPort.setStatus("current")
_CfprCommSshPolicyLevel_Type = Gauge32
_CfprCommSshPolicyLevel_Object = MibTableColumn
cfprCommSshPolicyLevel = _CfprCommSshPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 9),
    _CfprCommSshPolicyLevel_Type()
)
cfprCommSshPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPolicyLevel.setStatus("current")
_CfprCommSshPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommSshPolicyOwner_Object = MibTableColumn
cfprCommSshPolicyOwner = _CfprCommSshPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 10),
    _CfprCommSshPolicyOwner_Type()
)
cfprCommSshPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPolicyOwner.setStatus("current")
_CfprCommSshPort_Type = Gauge32
_CfprCommSshPort_Object = MibTableColumn
cfprCommSshPort = _CfprCommSshPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 11),
    _CfprCommSshPort_Type()
)
cfprCommSshPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPort.setStatus("current")
_CfprCommSshProto_Type = CfprCommShellProto
_CfprCommSshProto_Object = MibTableColumn
cfprCommSshProto = _CfprCommSshProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 12),
    _CfprCommSshProto_Type()
)
cfprCommSshProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshProto.setStatus("current")
_CfprCommSshAuthAlgo_Type = CfprCommAuth
_CfprCommSshAuthAlgo_Object = MibTableColumn
cfprCommSshAuthAlgo = _CfprCommSshAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 13),
    _CfprCommSshAuthAlgo_Type()
)
cfprCommSshAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshAuthAlgo.setStatus("current")
_CfprCommSshEncryptAlgo_Type = CfprCommSshEncryptAlgo
_CfprCommSshEncryptAlgo_Object = MibTableColumn
cfprCommSshEncryptAlgo = _CfprCommSshEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 14),
    _CfprCommSshEncryptAlgo_Type()
)
cfprCommSshEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshEncryptAlgo.setStatus("current")
_CfprCommSshHostKey_Type = Gauge32
_CfprCommSshHostKey_Object = MibTableColumn
cfprCommSshHostKey = _CfprCommSshHostKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 15),
    _CfprCommSshHostKey_Type()
)
cfprCommSshHostKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshHostKey.setStatus("current")
_CfprCommSshHostKeyDeleted_Type = TruthValue
_CfprCommSshHostKeyDeleted_Object = MibTableColumn
cfprCommSshHostKeyDeleted = _CfprCommSshHostKeyDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 16),
    _CfprCommSshHostKeyDeleted_Type()
)
cfprCommSshHostKeyDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshHostKeyDeleted.setStatus("current")
_CfprCommSshKexAlgo_Type = CfprCommSshKexAlgo
_CfprCommSshKexAlgo_Object = MibTableColumn
cfprCommSshKexAlgo = _CfprCommSshKexAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 17),
    _CfprCommSshKexAlgo_Type()
)
cfprCommSshKexAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshKexAlgo.setStatus("current")
_CfprCommSshMacAlgo_Type = CfprCommSshMacAlgo
_CfprCommSshMacAlgo_Object = MibTableColumn
cfprCommSshMacAlgo = _CfprCommSshMacAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 18),
    _CfprCommSshMacAlgo_Type()
)
cfprCommSshMacAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshMacAlgo.setStatus("current")
_CfprCommSshSshFlag_Type = Gauge32
_CfprCommSshSshFlag_Object = MibTableColumn
cfprCommSshSshFlag = _CfprCommSshSshFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 19),
    _CfprCommSshSshFlag_Type()
)
cfprCommSshSshFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshSshFlag.setStatus("current")
_CfprCommSshTime_Type = Gauge32
_CfprCommSshTime_Object = MibTableColumn
cfprCommSshTime = _CfprCommSshTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 20),
    _CfprCommSshTime_Type()
)
cfprCommSshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshTime.setStatus("current")
_CfprCommSshVolume_Type = Gauge32
_CfprCommSshVolume_Object = MibTableColumn
cfprCommSshVolume = _CfprCommSshVolume_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 21),
    _CfprCommSshVolume_Type()
)
cfprCommSshVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshVolume.setStatus("current")
_CfprCommSshHostKeyDeletedEcdsa_Type = TruthValue
_CfprCommSshHostKeyDeletedEcdsa_Object = MibTableColumn
cfprCommSshHostKeyDeletedEcdsa = _CfprCommSshHostKeyDeletedEcdsa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 22),
    _CfprCommSshHostKeyDeletedEcdsa_Type()
)
cfprCommSshHostKeyDeletedEcdsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshHostKeyDeletedEcdsa.setStatus("current")
_CfprCommSshHostKeyEcdsa_Type = CfprCommHostKeyEcdsa
_CfprCommSshHostKeyEcdsa_Object = MibTableColumn
cfprCommSshHostKeyEcdsa = _CfprCommSshHostKeyEcdsa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 15, 1, 23),
    _CfprCommSshHostKeyEcdsa_Type()
)
cfprCommSshHostKeyEcdsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshHostKeyEcdsa.setStatus("current")
_CfprCommSvcEpTable_Object = MibTable
cfprCommSvcEpTable = _CfprCommSvcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16)
)
if mibBuilder.loadTexts:
    cfprCommSvcEpTable.setStatus("current")
_CfprCommSvcEpEntry_Object = MibTableRow
cfprCommSvcEpEntry = _CfprCommSvcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1)
)
cfprCommSvcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSvcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSvcEpEntry.setStatus("current")
_CfprCommSvcEpInstanceId_Type = CfprManagedObjectId
_CfprCommSvcEpInstanceId_Object = MibTableColumn
cfprCommSvcEpInstanceId = _CfprCommSvcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 1),
    _CfprCommSvcEpInstanceId_Type()
)
cfprCommSvcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSvcEpInstanceId.setStatus("current")
_CfprCommSvcEpDn_Type = CfprManagedObjectDn
_CfprCommSvcEpDn_Object = MibTableColumn
cfprCommSvcEpDn = _CfprCommSvcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 2),
    _CfprCommSvcEpDn_Type()
)
cfprCommSvcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpDn.setStatus("current")
_CfprCommSvcEpRn_Type = SnmpAdminString
_CfprCommSvcEpRn_Object = MibTableColumn
cfprCommSvcEpRn = _CfprCommSvcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 3),
    _CfprCommSvcEpRn_Type()
)
cfprCommSvcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpRn.setStatus("current")
_CfprCommSvcEpConfigState_Type = CfprAaaConfigState
_CfprCommSvcEpConfigState_Object = MibTableColumn
cfprCommSvcEpConfigState = _CfprCommSvcEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 4),
    _CfprCommSvcEpConfigState_Type()
)
cfprCommSvcEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpConfigState.setStatus("current")
_CfprCommSvcEpConfigStatusMessage_Type = SnmpAdminString
_CfprCommSvcEpConfigStatusMessage_Object = MibTableColumn
cfprCommSvcEpConfigStatusMessage = _CfprCommSvcEpConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 5),
    _CfprCommSvcEpConfigStatusMessage_Type()
)
cfprCommSvcEpConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpConfigStatusMessage.setStatus("current")
_CfprCommSvcEpDescr_Type = SnmpAdminString
_CfprCommSvcEpDescr_Object = MibTableColumn
cfprCommSvcEpDescr = _CfprCommSvcEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 6),
    _CfprCommSvcEpDescr_Type()
)
cfprCommSvcEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpDescr.setStatus("current")
_CfprCommSvcEpFsmDescr_Type = SnmpAdminString
_CfprCommSvcEpFsmDescr_Object = MibTableColumn
cfprCommSvcEpFsmDescr = _CfprCommSvcEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 7),
    _CfprCommSvcEpFsmDescr_Type()
)
cfprCommSvcEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmDescr.setStatus("current")
_CfprCommSvcEpFsmFlags_Type = SnmpAdminString
_CfprCommSvcEpFsmFlags_Object = MibTableColumn
cfprCommSvcEpFsmFlags = _CfprCommSvcEpFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 8),
    _CfprCommSvcEpFsmFlags_Type()
)
cfprCommSvcEpFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmFlags.setStatus("current")
_CfprCommSvcEpFsmPrev_Type = SnmpAdminString
_CfprCommSvcEpFsmPrev_Object = MibTableColumn
cfprCommSvcEpFsmPrev = _CfprCommSvcEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 9),
    _CfprCommSvcEpFsmPrev_Type()
)
cfprCommSvcEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmPrev.setStatus("current")
_CfprCommSvcEpFsmProgr_Type = Gauge32
_CfprCommSvcEpFsmProgr_Object = MibTableColumn
cfprCommSvcEpFsmProgr = _CfprCommSvcEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 10),
    _CfprCommSvcEpFsmProgr_Type()
)
cfprCommSvcEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmProgr.setStatus("current")
_CfprCommSvcEpFsmRmtInvErrCode_Type = Gauge32
_CfprCommSvcEpFsmRmtInvErrCode_Object = MibTableColumn
cfprCommSvcEpFsmRmtInvErrCode = _CfprCommSvcEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 11),
    _CfprCommSvcEpFsmRmtInvErrCode_Type()
)
cfprCommSvcEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmRmtInvErrCode.setStatus("current")
_CfprCommSvcEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprCommSvcEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprCommSvcEpFsmRmtInvErrDescr = _CfprCommSvcEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 12),
    _CfprCommSvcEpFsmRmtInvErrDescr_Type()
)
cfprCommSvcEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmRmtInvErrDescr.setStatus("current")
_CfprCommSvcEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprCommSvcEpFsmRmtInvRslt_Object = MibTableColumn
cfprCommSvcEpFsmRmtInvRslt = _CfprCommSvcEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 13),
    _CfprCommSvcEpFsmRmtInvRslt_Type()
)
cfprCommSvcEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmRmtInvRslt.setStatus("current")
_CfprCommSvcEpFsmStageDescr_Type = SnmpAdminString
_CfprCommSvcEpFsmStageDescr_Object = MibTableColumn
cfprCommSvcEpFsmStageDescr = _CfprCommSvcEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 14),
    _CfprCommSvcEpFsmStageDescr_Type()
)
cfprCommSvcEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageDescr.setStatus("current")
_CfprCommSvcEpFsmStamp_Type = DateAndTime
_CfprCommSvcEpFsmStamp_Object = MibTableColumn
cfprCommSvcEpFsmStamp = _CfprCommSvcEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 15),
    _CfprCommSvcEpFsmStamp_Type()
)
cfprCommSvcEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStamp.setStatus("current")
_CfprCommSvcEpFsmStatus_Type = SnmpAdminString
_CfprCommSvcEpFsmStatus_Object = MibTableColumn
cfprCommSvcEpFsmStatus = _CfprCommSvcEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 16),
    _CfprCommSvcEpFsmStatus_Type()
)
cfprCommSvcEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStatus.setStatus("current")
_CfprCommSvcEpFsmTry_Type = Gauge32
_CfprCommSvcEpFsmTry_Object = MibTableColumn
cfprCommSvcEpFsmTry = _CfprCommSvcEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 17),
    _CfprCommSvcEpFsmTry_Type()
)
cfprCommSvcEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTry.setStatus("current")
_CfprCommSvcEpIntId_Type = SnmpAdminString
_CfprCommSvcEpIntId_Object = MibTableColumn
cfprCommSvcEpIntId = _CfprCommSvcEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 18),
    _CfprCommSvcEpIntId_Type()
)
cfprCommSvcEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpIntId.setStatus("current")
_CfprCommSvcEpName_Type = SnmpAdminString
_CfprCommSvcEpName_Object = MibTableColumn
cfprCommSvcEpName = _CfprCommSvcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 19),
    _CfprCommSvcEpName_Type()
)
cfprCommSvcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpName.setStatus("current")
_CfprCommSvcEpPolicyLevel_Type = Gauge32
_CfprCommSvcEpPolicyLevel_Object = MibTableColumn
cfprCommSvcEpPolicyLevel = _CfprCommSvcEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 20),
    _CfprCommSvcEpPolicyLevel_Type()
)
cfprCommSvcEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpPolicyLevel.setStatus("current")
_CfprCommSvcEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommSvcEpPolicyOwner_Object = MibTableColumn
cfprCommSvcEpPolicyOwner = _CfprCommSvcEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 21),
    _CfprCommSvcEpPolicyOwner_Type()
)
cfprCommSvcEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpPolicyOwner.setStatus("current")
_CfprCommSvcEpHttpsIpBlockCount_Type = Gauge32
_CfprCommSvcEpHttpsIpBlockCount_Object = MibTableColumn
cfprCommSvcEpHttpsIpBlockCount = _CfprCommSvcEpHttpsIpBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 22),
    _CfprCommSvcEpHttpsIpBlockCount_Type()
)
cfprCommSvcEpHttpsIpBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpHttpsIpBlockCount.setStatus("current")
_CfprCommSvcEpHttpsIpv6BlockCount_Type = Gauge32
_CfprCommSvcEpHttpsIpv6BlockCount_Object = MibTableColumn
cfprCommSvcEpHttpsIpv6BlockCount = _CfprCommSvcEpHttpsIpv6BlockCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 23),
    _CfprCommSvcEpHttpsIpv6BlockCount_Type()
)
cfprCommSvcEpHttpsIpv6BlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpHttpsIpv6BlockCount.setStatus("current")
_CfprCommSvcEpSnmpIpBlockCount_Type = Gauge32
_CfprCommSvcEpSnmpIpBlockCount_Object = MibTableColumn
cfprCommSvcEpSnmpIpBlockCount = _CfprCommSvcEpSnmpIpBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 24),
    _CfprCommSvcEpSnmpIpBlockCount_Type()
)
cfprCommSvcEpSnmpIpBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpSnmpIpBlockCount.setStatus("current")
_CfprCommSvcEpSnmpIpv6BlockCount_Type = Gauge32
_CfprCommSvcEpSnmpIpv6BlockCount_Object = MibTableColumn
cfprCommSvcEpSnmpIpv6BlockCount = _CfprCommSvcEpSnmpIpv6BlockCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 25),
    _CfprCommSvcEpSnmpIpv6BlockCount_Type()
)
cfprCommSvcEpSnmpIpv6BlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpSnmpIpv6BlockCount.setStatus("current")
_CfprCommSvcEpSshIpBlockCount_Type = Gauge32
_CfprCommSvcEpSshIpBlockCount_Object = MibTableColumn
cfprCommSvcEpSshIpBlockCount = _CfprCommSvcEpSshIpBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 26),
    _CfprCommSvcEpSshIpBlockCount_Type()
)
cfprCommSvcEpSshIpBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpSshIpBlockCount.setStatus("current")
_CfprCommSvcEpSshIpv6BlockCount_Type = Gauge32
_CfprCommSvcEpSshIpv6BlockCount_Object = MibTableColumn
cfprCommSvcEpSshIpv6BlockCount = _CfprCommSvcEpSshIpv6BlockCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 27),
    _CfprCommSvcEpSshIpv6BlockCount_Type()
)
cfprCommSvcEpSshIpv6BlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpSshIpv6BlockCount.setStatus("current")
_CfprCommSvcEpTlsVer_Type = CfprCommTlsVerType
_CfprCommSvcEpTlsVer_Object = MibTableColumn
cfprCommSvcEpTlsVer = _CfprCommSvcEpTlsVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 16, 1, 28),
    _CfprCommSvcEpTlsVer_Type()
)
cfprCommSvcEpTlsVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpTlsVer.setStatus("current")
_CfprCommSvcEpFsmTable_Object = MibTable
cfprCommSvcEpFsmTable = _CfprCommSvcEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17)
)
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTable.setStatus("current")
_CfprCommSvcEpFsmEntry_Object = MibTableRow
cfprCommSvcEpFsmEntry = _CfprCommSvcEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1)
)
cfprCommSvcEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSvcEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmEntry.setStatus("current")
_CfprCommSvcEpFsmInstanceId_Type = CfprManagedObjectId
_CfprCommSvcEpFsmInstanceId_Object = MibTableColumn
cfprCommSvcEpFsmInstanceId = _CfprCommSvcEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 1),
    _CfprCommSvcEpFsmInstanceId_Type()
)
cfprCommSvcEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmInstanceId.setStatus("current")
_CfprCommSvcEpFsmDn_Type = CfprManagedObjectDn
_CfprCommSvcEpFsmDn_Object = MibTableColumn
cfprCommSvcEpFsmDn = _CfprCommSvcEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 2),
    _CfprCommSvcEpFsmDn_Type()
)
cfprCommSvcEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmDn.setStatus("current")
_CfprCommSvcEpFsmRn_Type = SnmpAdminString
_CfprCommSvcEpFsmRn_Object = MibTableColumn
cfprCommSvcEpFsmRn = _CfprCommSvcEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 3),
    _CfprCommSvcEpFsmRn_Type()
)
cfprCommSvcEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmRn.setStatus("current")
_CfprCommSvcEpFsmCompletionTime_Type = DateAndTime
_CfprCommSvcEpFsmCompletionTime_Object = MibTableColumn
cfprCommSvcEpFsmCompletionTime = _CfprCommSvcEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 4),
    _CfprCommSvcEpFsmCompletionTime_Type()
)
cfprCommSvcEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmCompletionTime.setStatus("current")
_CfprCommSvcEpFsmCurrentFsm_Type = CfprCommSvcEpFsmCurrentFsm
_CfprCommSvcEpFsmCurrentFsm_Object = MibTableColumn
cfprCommSvcEpFsmCurrentFsm = _CfprCommSvcEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 5),
    _CfprCommSvcEpFsmCurrentFsm_Type()
)
cfprCommSvcEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmCurrentFsm.setStatus("current")
_CfprCommSvcEpFsmDescrData_Type = SnmpAdminString
_CfprCommSvcEpFsmDescrData_Object = MibTableColumn
cfprCommSvcEpFsmDescrData = _CfprCommSvcEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 6),
    _CfprCommSvcEpFsmDescrData_Type()
)
cfprCommSvcEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmDescrData.setStatus("current")
_CfprCommSvcEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprCommSvcEpFsmFsmStatus_Object = MibTableColumn
cfprCommSvcEpFsmFsmStatus = _CfprCommSvcEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 7),
    _CfprCommSvcEpFsmFsmStatus_Type()
)
cfprCommSvcEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmFsmStatus.setStatus("current")
_CfprCommSvcEpFsmProgress_Type = Gauge32
_CfprCommSvcEpFsmProgress_Object = MibTableColumn
cfprCommSvcEpFsmProgress = _CfprCommSvcEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 8),
    _CfprCommSvcEpFsmProgress_Type()
)
cfprCommSvcEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmProgress.setStatus("current")
_CfprCommSvcEpFsmRmtErrCode_Type = Gauge32
_CfprCommSvcEpFsmRmtErrCode_Object = MibTableColumn
cfprCommSvcEpFsmRmtErrCode = _CfprCommSvcEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 9),
    _CfprCommSvcEpFsmRmtErrCode_Type()
)
cfprCommSvcEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmRmtErrCode.setStatus("current")
_CfprCommSvcEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprCommSvcEpFsmRmtErrDescr_Object = MibTableColumn
cfprCommSvcEpFsmRmtErrDescr = _CfprCommSvcEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 10),
    _CfprCommSvcEpFsmRmtErrDescr_Type()
)
cfprCommSvcEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmRmtErrDescr.setStatus("current")
_CfprCommSvcEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprCommSvcEpFsmRmtRslt_Object = MibTableColumn
cfprCommSvcEpFsmRmtRslt = _CfprCommSvcEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 17, 1, 11),
    _CfprCommSvcEpFsmRmtRslt_Type()
)
cfprCommSvcEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmRmtRslt.setStatus("current")
_CfprCommSvcEpFsmStageTable_Object = MibTable
cfprCommSvcEpFsmStageTable = _CfprCommSvcEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18)
)
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageTable.setStatus("current")
_CfprCommSvcEpFsmStageEntry_Object = MibTableRow
cfprCommSvcEpFsmStageEntry = _CfprCommSvcEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1)
)
cfprCommSvcEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSvcEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageEntry.setStatus("current")
_CfprCommSvcEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprCommSvcEpFsmStageInstanceId_Object = MibTableColumn
cfprCommSvcEpFsmStageInstanceId = _CfprCommSvcEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 1),
    _CfprCommSvcEpFsmStageInstanceId_Type()
)
cfprCommSvcEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageInstanceId.setStatus("current")
_CfprCommSvcEpFsmStageDn_Type = CfprManagedObjectDn
_CfprCommSvcEpFsmStageDn_Object = MibTableColumn
cfprCommSvcEpFsmStageDn = _CfprCommSvcEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 2),
    _CfprCommSvcEpFsmStageDn_Type()
)
cfprCommSvcEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageDn.setStatus("current")
_CfprCommSvcEpFsmStageRn_Type = SnmpAdminString
_CfprCommSvcEpFsmStageRn_Object = MibTableColumn
cfprCommSvcEpFsmStageRn = _CfprCommSvcEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 3),
    _CfprCommSvcEpFsmStageRn_Type()
)
cfprCommSvcEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageRn.setStatus("current")
_CfprCommSvcEpFsmStageDescrData_Type = SnmpAdminString
_CfprCommSvcEpFsmStageDescrData_Object = MibTableColumn
cfprCommSvcEpFsmStageDescrData = _CfprCommSvcEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 4),
    _CfprCommSvcEpFsmStageDescrData_Type()
)
cfprCommSvcEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageDescrData.setStatus("current")
_CfprCommSvcEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprCommSvcEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprCommSvcEpFsmStageLastUpdateTime = _CfprCommSvcEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 5),
    _CfprCommSvcEpFsmStageLastUpdateTime_Type()
)
cfprCommSvcEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageLastUpdateTime.setStatus("current")
_CfprCommSvcEpFsmStageName_Type = CfprCommSvcEpFsmStageName
_CfprCommSvcEpFsmStageName_Object = MibTableColumn
cfprCommSvcEpFsmStageName = _CfprCommSvcEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 6),
    _CfprCommSvcEpFsmStageName_Type()
)
cfprCommSvcEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageName.setStatus("current")
_CfprCommSvcEpFsmStageOrder_Type = Gauge32
_CfprCommSvcEpFsmStageOrder_Object = MibTableColumn
cfprCommSvcEpFsmStageOrder = _CfprCommSvcEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 7),
    _CfprCommSvcEpFsmStageOrder_Type()
)
cfprCommSvcEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageOrder.setStatus("current")
_CfprCommSvcEpFsmStageRetry_Type = Gauge32
_CfprCommSvcEpFsmStageRetry_Object = MibTableColumn
cfprCommSvcEpFsmStageRetry = _CfprCommSvcEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 8),
    _CfprCommSvcEpFsmStageRetry_Type()
)
cfprCommSvcEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageRetry.setStatus("current")
_CfprCommSvcEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprCommSvcEpFsmStageStageStatus_Object = MibTableColumn
cfprCommSvcEpFsmStageStageStatus = _CfprCommSvcEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 18, 1, 9),
    _CfprCommSvcEpFsmStageStageStatus_Type()
)
cfprCommSvcEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmStageStageStatus.setStatus("current")
_CfprCommSvcEpFsmTaskTable_Object = MibTable
cfprCommSvcEpFsmTaskTable = _CfprCommSvcEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19)
)
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskTable.setStatus("current")
_CfprCommSvcEpFsmTaskEntry_Object = MibTableRow
cfprCommSvcEpFsmTaskEntry = _CfprCommSvcEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19, 1)
)
cfprCommSvcEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSvcEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskEntry.setStatus("current")
_CfprCommSvcEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprCommSvcEpFsmTaskInstanceId_Object = MibTableColumn
cfprCommSvcEpFsmTaskInstanceId = _CfprCommSvcEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19, 1, 1),
    _CfprCommSvcEpFsmTaskInstanceId_Type()
)
cfprCommSvcEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskInstanceId.setStatus("current")
_CfprCommSvcEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprCommSvcEpFsmTaskDn_Object = MibTableColumn
cfprCommSvcEpFsmTaskDn = _CfprCommSvcEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19, 1, 2),
    _CfprCommSvcEpFsmTaskDn_Type()
)
cfprCommSvcEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskDn.setStatus("current")
_CfprCommSvcEpFsmTaskRn_Type = SnmpAdminString
_CfprCommSvcEpFsmTaskRn_Object = MibTableColumn
cfprCommSvcEpFsmTaskRn = _CfprCommSvcEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19, 1, 3),
    _CfprCommSvcEpFsmTaskRn_Type()
)
cfprCommSvcEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskRn.setStatus("current")
_CfprCommSvcEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprCommSvcEpFsmTaskCompletion_Object = MibTableColumn
cfprCommSvcEpFsmTaskCompletion = _CfprCommSvcEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19, 1, 4),
    _CfprCommSvcEpFsmTaskCompletion_Type()
)
cfprCommSvcEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskCompletion.setStatus("current")
_CfprCommSvcEpFsmTaskFlags_Type = CfprCommSvcEpFsmTaskFlags
_CfprCommSvcEpFsmTaskFlags_Object = MibTableColumn
cfprCommSvcEpFsmTaskFlags = _CfprCommSvcEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19, 1, 5),
    _CfprCommSvcEpFsmTaskFlags_Type()
)
cfprCommSvcEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskFlags.setStatus("current")
_CfprCommSvcEpFsmTaskItem_Type = CfprCommSvcEpFsmTaskItem
_CfprCommSvcEpFsmTaskItem_Object = MibTableColumn
cfprCommSvcEpFsmTaskItem = _CfprCommSvcEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19, 1, 6),
    _CfprCommSvcEpFsmTaskItem_Type()
)
cfprCommSvcEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskItem.setStatus("current")
_CfprCommSvcEpFsmTaskSeqId_Type = Gauge32
_CfprCommSvcEpFsmTaskSeqId_Object = MibTableColumn
cfprCommSvcEpFsmTaskSeqId = _CfprCommSvcEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 19, 1, 7),
    _CfprCommSvcEpFsmTaskSeqId_Type()
)
cfprCommSvcEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSvcEpFsmTaskSeqId.setStatus("current")
_CfprCommSyslogTable_Object = MibTable
cfprCommSyslogTable = _CfprCommSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20)
)
if mibBuilder.loadTexts:
    cfprCommSyslogTable.setStatus("current")
_CfprCommSyslogEntry_Object = MibTableRow
cfprCommSyslogEntry = _CfprCommSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1)
)
cfprCommSyslogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSyslogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSyslogEntry.setStatus("current")
_CfprCommSyslogInstanceId_Type = CfprManagedObjectId
_CfprCommSyslogInstanceId_Object = MibTableColumn
cfprCommSyslogInstanceId = _CfprCommSyslogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 1),
    _CfprCommSyslogInstanceId_Type()
)
cfprCommSyslogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSyslogInstanceId.setStatus("current")
_CfprCommSyslogDn_Type = CfprManagedObjectDn
_CfprCommSyslogDn_Object = MibTableColumn
cfprCommSyslogDn = _CfprCommSyslogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 2),
    _CfprCommSyslogDn_Type()
)
cfprCommSyslogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogDn.setStatus("current")
_CfprCommSyslogRn_Type = SnmpAdminString
_CfprCommSyslogRn_Object = MibTableColumn
cfprCommSyslogRn = _CfprCommSyslogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 3),
    _CfprCommSyslogRn_Type()
)
cfprCommSyslogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogRn.setStatus("current")
_CfprCommSyslogAdminState_Type = CfprCommAdminState
_CfprCommSyslogAdminState_Object = MibTableColumn
cfprCommSyslogAdminState = _CfprCommSyslogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 4),
    _CfprCommSyslogAdminState_Type()
)
cfprCommSyslogAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogAdminState.setStatus("current")
_CfprCommSyslogDescr_Type = SnmpAdminString
_CfprCommSyslogDescr_Object = MibTableColumn
cfprCommSyslogDescr = _CfprCommSyslogDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 5),
    _CfprCommSyslogDescr_Type()
)
cfprCommSyslogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogDescr.setStatus("current")
_CfprCommSyslogIntId_Type = SnmpAdminString
_CfprCommSyslogIntId_Object = MibTableColumn
cfprCommSyslogIntId = _CfprCommSyslogIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 6),
    _CfprCommSyslogIntId_Type()
)
cfprCommSyslogIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogIntId.setStatus("current")
_CfprCommSyslogName_Type = SnmpAdminString
_CfprCommSyslogName_Object = MibTableColumn
cfprCommSyslogName = _CfprCommSyslogName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 7),
    _CfprCommSyslogName_Type()
)
cfprCommSyslogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogName.setStatus("current")
_CfprCommSyslogOperPort_Type = Gauge32
_CfprCommSyslogOperPort_Object = MibTableColumn
cfprCommSyslogOperPort = _CfprCommSyslogOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 8),
    _CfprCommSyslogOperPort_Type()
)
cfprCommSyslogOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogOperPort.setStatus("current")
_CfprCommSyslogPolicyLevel_Type = Gauge32
_CfprCommSyslogPolicyLevel_Object = MibTableColumn
cfprCommSyslogPolicyLevel = _CfprCommSyslogPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 9),
    _CfprCommSyslogPolicyLevel_Type()
)
cfprCommSyslogPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPolicyLevel.setStatus("current")
_CfprCommSyslogPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommSyslogPolicyOwner_Object = MibTableColumn
cfprCommSyslogPolicyOwner = _CfprCommSyslogPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 10),
    _CfprCommSyslogPolicyOwner_Type()
)
cfprCommSyslogPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPolicyOwner.setStatus("current")
_CfprCommSyslogPort_Type = Gauge32
_CfprCommSyslogPort_Object = MibTableColumn
cfprCommSyslogPort = _CfprCommSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 11),
    _CfprCommSyslogPort_Type()
)
cfprCommSyslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPort.setStatus("current")
_CfprCommSyslogProto_Type = CfprCommSyslogProto
_CfprCommSyslogProto_Object = MibTableColumn
cfprCommSyslogProto = _CfprCommSyslogProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 12),
    _CfprCommSyslogProto_Type()
)
cfprCommSyslogProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogProto.setStatus("current")
_CfprCommSyslogSeverity_Type = CfprCommSyslogSeverity
_CfprCommSyslogSeverity_Object = MibTableColumn
cfprCommSyslogSeverity = _CfprCommSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 20, 1, 13),
    _CfprCommSyslogSeverity_Type()
)
cfprCommSyslogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogSeverity.setStatus("current")
_CfprCommSyslogClientTable_Object = MibTable
cfprCommSyslogClientTable = _CfprCommSyslogClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21)
)
if mibBuilder.loadTexts:
    cfprCommSyslogClientTable.setStatus("current")
_CfprCommSyslogClientEntry_Object = MibTableRow
cfprCommSyslogClientEntry = _CfprCommSyslogClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1)
)
cfprCommSyslogClientEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSyslogClientInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSyslogClientEntry.setStatus("current")
_CfprCommSyslogClientInstanceId_Type = CfprManagedObjectId
_CfprCommSyslogClientInstanceId_Object = MibTableColumn
cfprCommSyslogClientInstanceId = _CfprCommSyslogClientInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1, 1),
    _CfprCommSyslogClientInstanceId_Type()
)
cfprCommSyslogClientInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSyslogClientInstanceId.setStatus("current")
_CfprCommSyslogClientDn_Type = CfprManagedObjectDn
_CfprCommSyslogClientDn_Object = MibTableColumn
cfprCommSyslogClientDn = _CfprCommSyslogClientDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1, 2),
    _CfprCommSyslogClientDn_Type()
)
cfprCommSyslogClientDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogClientDn.setStatus("current")
_CfprCommSyslogClientRn_Type = SnmpAdminString
_CfprCommSyslogClientRn_Object = MibTableColumn
cfprCommSyslogClientRn = _CfprCommSyslogClientRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1, 3),
    _CfprCommSyslogClientRn_Type()
)
cfprCommSyslogClientRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogClientRn.setStatus("current")
_CfprCommSyslogClientAdminState_Type = CfprCommSyslogAdminState
_CfprCommSyslogClientAdminState_Object = MibTableColumn
cfprCommSyslogClientAdminState = _CfprCommSyslogClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1, 4),
    _CfprCommSyslogClientAdminState_Type()
)
cfprCommSyslogClientAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogClientAdminState.setStatus("current")
_CfprCommSyslogClientForwardingFacility_Type = CfprCommSyslogForwardingFacility
_CfprCommSyslogClientForwardingFacility_Object = MibTableColumn
cfprCommSyslogClientForwardingFacility = _CfprCommSyslogClientForwardingFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1, 5),
    _CfprCommSyslogClientForwardingFacility_Type()
)
cfprCommSyslogClientForwardingFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogClientForwardingFacility.setStatus("current")
_CfprCommSyslogClientHostname_Type = SnmpAdminString
_CfprCommSyslogClientHostname_Object = MibTableColumn
cfprCommSyslogClientHostname = _CfprCommSyslogClientHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1, 6),
    _CfprCommSyslogClientHostname_Type()
)
cfprCommSyslogClientHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogClientHostname.setStatus("current")
_CfprCommSyslogClientName_Type = CfprCommSyslogClientEnum
_CfprCommSyslogClientName_Object = MibTableColumn
cfprCommSyslogClientName = _CfprCommSyslogClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1, 7),
    _CfprCommSyslogClientName_Type()
)
cfprCommSyslogClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogClientName.setStatus("current")
_CfprCommSyslogClientSeverity_Type = CfprCommSyslogSeverity
_CfprCommSyslogClientSeverity_Object = MibTableColumn
cfprCommSyslogClientSeverity = _CfprCommSyslogClientSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 21, 1, 8),
    _CfprCommSyslogClientSeverity_Type()
)
cfprCommSyslogClientSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogClientSeverity.setStatus("current")
_CfprCommSyslogConsoleTable_Object = MibTable
cfprCommSyslogConsoleTable = _CfprCommSyslogConsoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22)
)
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleTable.setStatus("current")
_CfprCommSyslogConsoleEntry_Object = MibTableRow
cfprCommSyslogConsoleEntry = _CfprCommSyslogConsoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22, 1)
)
cfprCommSyslogConsoleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSyslogConsoleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleEntry.setStatus("current")
_CfprCommSyslogConsoleInstanceId_Type = CfprManagedObjectId
_CfprCommSyslogConsoleInstanceId_Object = MibTableColumn
cfprCommSyslogConsoleInstanceId = _CfprCommSyslogConsoleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22, 1, 1),
    _CfprCommSyslogConsoleInstanceId_Type()
)
cfprCommSyslogConsoleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleInstanceId.setStatus("current")
_CfprCommSyslogConsoleDn_Type = CfprManagedObjectDn
_CfprCommSyslogConsoleDn_Object = MibTableColumn
cfprCommSyslogConsoleDn = _CfprCommSyslogConsoleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22, 1, 2),
    _CfprCommSyslogConsoleDn_Type()
)
cfprCommSyslogConsoleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleDn.setStatus("current")
_CfprCommSyslogConsoleRn_Type = SnmpAdminString
_CfprCommSyslogConsoleRn_Object = MibTableColumn
cfprCommSyslogConsoleRn = _CfprCommSyslogConsoleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22, 1, 3),
    _CfprCommSyslogConsoleRn_Type()
)
cfprCommSyslogConsoleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleRn.setStatus("current")
_CfprCommSyslogConsoleAdminState_Type = CfprCommSyslogAdminState
_CfprCommSyslogConsoleAdminState_Object = MibTableColumn
cfprCommSyslogConsoleAdminState = _CfprCommSyslogConsoleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22, 1, 4),
    _CfprCommSyslogConsoleAdminState_Type()
)
cfprCommSyslogConsoleAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleAdminState.setStatus("current")
_CfprCommSyslogConsoleDescr_Type = SnmpAdminString
_CfprCommSyslogConsoleDescr_Object = MibTableColumn
cfprCommSyslogConsoleDescr = _CfprCommSyslogConsoleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22, 1, 5),
    _CfprCommSyslogConsoleDescr_Type()
)
cfprCommSyslogConsoleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleDescr.setStatus("current")
_CfprCommSyslogConsoleName_Type = SnmpAdminString
_CfprCommSyslogConsoleName_Object = MibTableColumn
cfprCommSyslogConsoleName = _CfprCommSyslogConsoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22, 1, 6),
    _CfprCommSyslogConsoleName_Type()
)
cfprCommSyslogConsoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleName.setStatus("current")
_CfprCommSyslogConsoleSeverity_Type = CfprCommSyslogRestrictedSeverity
_CfprCommSyslogConsoleSeverity_Object = MibTableColumn
cfprCommSyslogConsoleSeverity = _CfprCommSyslogConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 22, 1, 7),
    _CfprCommSyslogConsoleSeverity_Type()
)
cfprCommSyslogConsoleSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogConsoleSeverity.setStatus("current")
_CfprCommSyslogFileTable_Object = MibTable
cfprCommSyslogFileTable = _CfprCommSyslogFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23)
)
if mibBuilder.loadTexts:
    cfprCommSyslogFileTable.setStatus("current")
_CfprCommSyslogFileEntry_Object = MibTableRow
cfprCommSyslogFileEntry = _CfprCommSyslogFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1)
)
cfprCommSyslogFileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSyslogFileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSyslogFileEntry.setStatus("current")
_CfprCommSyslogFileInstanceId_Type = CfprManagedObjectId
_CfprCommSyslogFileInstanceId_Object = MibTableColumn
cfprCommSyslogFileInstanceId = _CfprCommSyslogFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1, 1),
    _CfprCommSyslogFileInstanceId_Type()
)
cfprCommSyslogFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSyslogFileInstanceId.setStatus("current")
_CfprCommSyslogFileDn_Type = CfprManagedObjectDn
_CfprCommSyslogFileDn_Object = MibTableColumn
cfprCommSyslogFileDn = _CfprCommSyslogFileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1, 2),
    _CfprCommSyslogFileDn_Type()
)
cfprCommSyslogFileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogFileDn.setStatus("current")
_CfprCommSyslogFileRn_Type = SnmpAdminString
_CfprCommSyslogFileRn_Object = MibTableColumn
cfprCommSyslogFileRn = _CfprCommSyslogFileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1, 3),
    _CfprCommSyslogFileRn_Type()
)
cfprCommSyslogFileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogFileRn.setStatus("current")
_CfprCommSyslogFileAdminState_Type = CfprCommSyslogAdminState
_CfprCommSyslogFileAdminState_Object = MibTableColumn
cfprCommSyslogFileAdminState = _CfprCommSyslogFileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1, 4),
    _CfprCommSyslogFileAdminState_Type()
)
cfprCommSyslogFileAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogFileAdminState.setStatus("current")
_CfprCommSyslogFileDescr_Type = SnmpAdminString
_CfprCommSyslogFileDescr_Object = MibTableColumn
cfprCommSyslogFileDescr = _CfprCommSyslogFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1, 5),
    _CfprCommSyslogFileDescr_Type()
)
cfprCommSyslogFileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogFileDescr.setStatus("current")
_CfprCommSyslogFileName_Type = SnmpAdminString
_CfprCommSyslogFileName_Object = MibTableColumn
cfprCommSyslogFileName = _CfprCommSyslogFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1, 6),
    _CfprCommSyslogFileName_Type()
)
cfprCommSyslogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogFileName.setStatus("current")
_CfprCommSyslogFileSeverity_Type = CfprCommSyslogSeverity
_CfprCommSyslogFileSeverity_Object = MibTableColumn
cfprCommSyslogFileSeverity = _CfprCommSyslogFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1, 7),
    _CfprCommSyslogFileSeverity_Type()
)
cfprCommSyslogFileSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogFileSeverity.setStatus("current")
_CfprCommSyslogFileSize_Type = CfprCommSyslogFileSize
_CfprCommSyslogFileSize_Object = MibTableColumn
cfprCommSyslogFileSize = _CfprCommSyslogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 23, 1, 8),
    _CfprCommSyslogFileSize_Type()
)
cfprCommSyslogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogFileSize.setStatus("current")
_CfprCommSyslogMonitorTable_Object = MibTable
cfprCommSyslogMonitorTable = _CfprCommSyslogMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24)
)
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorTable.setStatus("current")
_CfprCommSyslogMonitorEntry_Object = MibTableRow
cfprCommSyslogMonitorEntry = _CfprCommSyslogMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24, 1)
)
cfprCommSyslogMonitorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSyslogMonitorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorEntry.setStatus("current")
_CfprCommSyslogMonitorInstanceId_Type = CfprManagedObjectId
_CfprCommSyslogMonitorInstanceId_Object = MibTableColumn
cfprCommSyslogMonitorInstanceId = _CfprCommSyslogMonitorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24, 1, 1),
    _CfprCommSyslogMonitorInstanceId_Type()
)
cfprCommSyslogMonitorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorInstanceId.setStatus("current")
_CfprCommSyslogMonitorDn_Type = CfprManagedObjectDn
_CfprCommSyslogMonitorDn_Object = MibTableColumn
cfprCommSyslogMonitorDn = _CfprCommSyslogMonitorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24, 1, 2),
    _CfprCommSyslogMonitorDn_Type()
)
cfprCommSyslogMonitorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorDn.setStatus("current")
_CfprCommSyslogMonitorRn_Type = SnmpAdminString
_CfprCommSyslogMonitorRn_Object = MibTableColumn
cfprCommSyslogMonitorRn = _CfprCommSyslogMonitorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24, 1, 3),
    _CfprCommSyslogMonitorRn_Type()
)
cfprCommSyslogMonitorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorRn.setStatus("current")
_CfprCommSyslogMonitorAdminState_Type = CfprCommSyslogAdminState
_CfprCommSyslogMonitorAdminState_Object = MibTableColumn
cfprCommSyslogMonitorAdminState = _CfprCommSyslogMonitorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24, 1, 4),
    _CfprCommSyslogMonitorAdminState_Type()
)
cfprCommSyslogMonitorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorAdminState.setStatus("current")
_CfprCommSyslogMonitorDescr_Type = SnmpAdminString
_CfprCommSyslogMonitorDescr_Object = MibTableColumn
cfprCommSyslogMonitorDescr = _CfprCommSyslogMonitorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24, 1, 5),
    _CfprCommSyslogMonitorDescr_Type()
)
cfprCommSyslogMonitorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorDescr.setStatus("current")
_CfprCommSyslogMonitorName_Type = SnmpAdminString
_CfprCommSyslogMonitorName_Object = MibTableColumn
cfprCommSyslogMonitorName = _CfprCommSyslogMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24, 1, 6),
    _CfprCommSyslogMonitorName_Type()
)
cfprCommSyslogMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorName.setStatus("current")
_CfprCommSyslogMonitorSeverity_Type = CfprCommSyslogSeverity
_CfprCommSyslogMonitorSeverity_Object = MibTableColumn
cfprCommSyslogMonitorSeverity = _CfprCommSyslogMonitorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 24, 1, 7),
    _CfprCommSyslogMonitorSeverity_Type()
)
cfprCommSyslogMonitorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogMonitorSeverity.setStatus("current")
_CfprCommSyslogSourceTable_Object = MibTable
cfprCommSyslogSourceTable = _CfprCommSyslogSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25)
)
if mibBuilder.loadTexts:
    cfprCommSyslogSourceTable.setStatus("current")
_CfprCommSyslogSourceEntry_Object = MibTableRow
cfprCommSyslogSourceEntry = _CfprCommSyslogSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1)
)
cfprCommSyslogSourceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSyslogSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSyslogSourceEntry.setStatus("current")
_CfprCommSyslogSourceInstanceId_Type = CfprManagedObjectId
_CfprCommSyslogSourceInstanceId_Object = MibTableColumn
cfprCommSyslogSourceInstanceId = _CfprCommSyslogSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1, 1),
    _CfprCommSyslogSourceInstanceId_Type()
)
cfprCommSyslogSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSyslogSourceInstanceId.setStatus("current")
_CfprCommSyslogSourceDn_Type = CfprManagedObjectDn
_CfprCommSyslogSourceDn_Object = MibTableColumn
cfprCommSyslogSourceDn = _CfprCommSyslogSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1, 2),
    _CfprCommSyslogSourceDn_Type()
)
cfprCommSyslogSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogSourceDn.setStatus("current")
_CfprCommSyslogSourceRn_Type = SnmpAdminString
_CfprCommSyslogSourceRn_Object = MibTableColumn
cfprCommSyslogSourceRn = _CfprCommSyslogSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1, 3),
    _CfprCommSyslogSourceRn_Type()
)
cfprCommSyslogSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogSourceRn.setStatus("current")
_CfprCommSyslogSourceAudits_Type = CfprCommSyslogSourceAudits
_CfprCommSyslogSourceAudits_Object = MibTableColumn
cfprCommSyslogSourceAudits = _CfprCommSyslogSourceAudits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1, 4),
    _CfprCommSyslogSourceAudits_Type()
)
cfprCommSyslogSourceAudits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogSourceAudits.setStatus("current")
_CfprCommSyslogSourceDescr_Type = SnmpAdminString
_CfprCommSyslogSourceDescr_Object = MibTableColumn
cfprCommSyslogSourceDescr = _CfprCommSyslogSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1, 5),
    _CfprCommSyslogSourceDescr_Type()
)
cfprCommSyslogSourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogSourceDescr.setStatus("current")
_CfprCommSyslogSourceEvents_Type = CfprCommSyslogSourceEvents
_CfprCommSyslogSourceEvents_Object = MibTableColumn
cfprCommSyslogSourceEvents = _CfprCommSyslogSourceEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1, 6),
    _CfprCommSyslogSourceEvents_Type()
)
cfprCommSyslogSourceEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogSourceEvents.setStatus("current")
_CfprCommSyslogSourceFaults_Type = CfprCommSyslogSourceFaults
_CfprCommSyslogSourceFaults_Object = MibTableColumn
cfprCommSyslogSourceFaults = _CfprCommSyslogSourceFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1, 7),
    _CfprCommSyslogSourceFaults_Type()
)
cfprCommSyslogSourceFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogSourceFaults.setStatus("current")
_CfprCommSyslogSourceName_Type = SnmpAdminString
_CfprCommSyslogSourceName_Object = MibTableColumn
cfprCommSyslogSourceName = _CfprCommSyslogSourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 25, 1, 8),
    _CfprCommSyslogSourceName_Type()
)
cfprCommSyslogSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogSourceName.setStatus("current")
_CfprCommTelnetTable_Object = MibTable
cfprCommTelnetTable = _CfprCommTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26)
)
if mibBuilder.loadTexts:
    cfprCommTelnetTable.setStatus("current")
_CfprCommTelnetEntry_Object = MibTableRow
cfprCommTelnetEntry = _CfprCommTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1)
)
cfprCommTelnetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommTelnetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommTelnetEntry.setStatus("current")
_CfprCommTelnetInstanceId_Type = CfprManagedObjectId
_CfprCommTelnetInstanceId_Object = MibTableColumn
cfprCommTelnetInstanceId = _CfprCommTelnetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 1),
    _CfprCommTelnetInstanceId_Type()
)
cfprCommTelnetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommTelnetInstanceId.setStatus("current")
_CfprCommTelnetDn_Type = CfprManagedObjectDn
_CfprCommTelnetDn_Object = MibTableColumn
cfprCommTelnetDn = _CfprCommTelnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 2),
    _CfprCommTelnetDn_Type()
)
cfprCommTelnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetDn.setStatus("current")
_CfprCommTelnetRn_Type = SnmpAdminString
_CfprCommTelnetRn_Object = MibTableColumn
cfprCommTelnetRn = _CfprCommTelnetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 3),
    _CfprCommTelnetRn_Type()
)
cfprCommTelnetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetRn.setStatus("current")
_CfprCommTelnetAdminState_Type = CfprCommAdminState
_CfprCommTelnetAdminState_Object = MibTableColumn
cfprCommTelnetAdminState = _CfprCommTelnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 4),
    _CfprCommTelnetAdminState_Type()
)
cfprCommTelnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetAdminState.setStatus("current")
_CfprCommTelnetDescr_Type = SnmpAdminString
_CfprCommTelnetDescr_Object = MibTableColumn
cfprCommTelnetDescr = _CfprCommTelnetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 5),
    _CfprCommTelnetDescr_Type()
)
cfprCommTelnetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetDescr.setStatus("current")
_CfprCommTelnetIntId_Type = SnmpAdminString
_CfprCommTelnetIntId_Object = MibTableColumn
cfprCommTelnetIntId = _CfprCommTelnetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 6),
    _CfprCommTelnetIntId_Type()
)
cfprCommTelnetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetIntId.setStatus("current")
_CfprCommTelnetName_Type = SnmpAdminString
_CfprCommTelnetName_Object = MibTableColumn
cfprCommTelnetName = _CfprCommTelnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 7),
    _CfprCommTelnetName_Type()
)
cfprCommTelnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetName.setStatus("current")
_CfprCommTelnetOperPort_Type = Gauge32
_CfprCommTelnetOperPort_Object = MibTableColumn
cfprCommTelnetOperPort = _CfprCommTelnetOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 8),
    _CfprCommTelnetOperPort_Type()
)
cfprCommTelnetOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetOperPort.setStatus("current")
_CfprCommTelnetPolicyLevel_Type = Gauge32
_CfprCommTelnetPolicyLevel_Object = MibTableColumn
cfprCommTelnetPolicyLevel = _CfprCommTelnetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 9),
    _CfprCommTelnetPolicyLevel_Type()
)
cfprCommTelnetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetPolicyLevel.setStatus("current")
_CfprCommTelnetPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommTelnetPolicyOwner_Object = MibTableColumn
cfprCommTelnetPolicyOwner = _CfprCommTelnetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 10),
    _CfprCommTelnetPolicyOwner_Type()
)
cfprCommTelnetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetPolicyOwner.setStatus("current")
_CfprCommTelnetPort_Type = Gauge32
_CfprCommTelnetPort_Object = MibTableColumn
cfprCommTelnetPort = _CfprCommTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 11),
    _CfprCommTelnetPort_Type()
)
cfprCommTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetPort.setStatus("current")
_CfprCommTelnetProto_Type = CfprCommShellProto
_CfprCommTelnetProto_Object = MibTableColumn
cfprCommTelnetProto = _CfprCommTelnetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 26, 1, 12),
    _CfprCommTelnetProto_Type()
)
cfprCommTelnetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelnetProto.setStatus("current")
_CfprCommWebChannelTable_Object = MibTable
cfprCommWebChannelTable = _CfprCommWebChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27)
)
if mibBuilder.loadTexts:
    cfprCommWebChannelTable.setStatus("current")
_CfprCommWebChannelEntry_Object = MibTableRow
cfprCommWebChannelEntry = _CfprCommWebChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1)
)
cfprCommWebChannelEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommWebChannelInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommWebChannelEntry.setStatus("current")
_CfprCommWebChannelInstanceId_Type = CfprManagedObjectId
_CfprCommWebChannelInstanceId_Object = MibTableColumn
cfprCommWebChannelInstanceId = _CfprCommWebChannelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 1),
    _CfprCommWebChannelInstanceId_Type()
)
cfprCommWebChannelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommWebChannelInstanceId.setStatus("current")
_CfprCommWebChannelDn_Type = CfprManagedObjectDn
_CfprCommWebChannelDn_Object = MibTableColumn
cfprCommWebChannelDn = _CfprCommWebChannelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 2),
    _CfprCommWebChannelDn_Type()
)
cfprCommWebChannelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebChannelDn.setStatus("current")
_CfprCommWebChannelRn_Type = SnmpAdminString
_CfprCommWebChannelRn_Object = MibTableColumn
cfprCommWebChannelRn = _CfprCommWebChannelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 3),
    _CfprCommWebChannelRn_Type()
)
cfprCommWebChannelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebChannelRn.setStatus("current")
_CfprCommWebChannelChannelState_Type = CfprCommChannel
_CfprCommWebChannelChannelState_Object = MibTableColumn
cfprCommWebChannelChannelState = _CfprCommWebChannelChannelState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 4),
    _CfprCommWebChannelChannelState_Type()
)
cfprCommWebChannelChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebChannelChannelState.setStatus("current")
_CfprCommWebChannelDescr_Type = SnmpAdminString
_CfprCommWebChannelDescr_Object = MibTableColumn
cfprCommWebChannelDescr = _CfprCommWebChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 5),
    _CfprCommWebChannelDescr_Type()
)
cfprCommWebChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebChannelDescr.setStatus("current")
_CfprCommWebChannelIntId_Type = SnmpAdminString
_CfprCommWebChannelIntId_Object = MibTableColumn
cfprCommWebChannelIntId = _CfprCommWebChannelIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 6),
    _CfprCommWebChannelIntId_Type()
)
cfprCommWebChannelIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebChannelIntId.setStatus("current")
_CfprCommWebChannelName_Type = SnmpAdminString
_CfprCommWebChannelName_Object = MibTableColumn
cfprCommWebChannelName = _CfprCommWebChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 7),
    _CfprCommWebChannelName_Type()
)
cfprCommWebChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebChannelName.setStatus("current")
_CfprCommWebChannelPolicyLevel_Type = Gauge32
_CfprCommWebChannelPolicyLevel_Object = MibTableColumn
cfprCommWebChannelPolicyLevel = _CfprCommWebChannelPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 8),
    _CfprCommWebChannelPolicyLevel_Type()
)
cfprCommWebChannelPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebChannelPolicyLevel.setStatus("current")
_CfprCommWebChannelPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommWebChannelPolicyOwner_Object = MibTableColumn
cfprCommWebChannelPolicyOwner = _CfprCommWebChannelPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 27, 1, 9),
    _CfprCommWebChannelPolicyOwner_Type()
)
cfprCommWebChannelPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebChannelPolicyOwner.setStatus("current")
_CfprCommWebSvcLimitsTable_Object = MibTable
cfprCommWebSvcLimitsTable = _CfprCommWebSvcLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28)
)
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsTable.setStatus("current")
_CfprCommWebSvcLimitsEntry_Object = MibTableRow
cfprCommWebSvcLimitsEntry = _CfprCommWebSvcLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1)
)
cfprCommWebSvcLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommWebSvcLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsEntry.setStatus("current")
_CfprCommWebSvcLimitsInstanceId_Type = CfprManagedObjectId
_CfprCommWebSvcLimitsInstanceId_Object = MibTableColumn
cfprCommWebSvcLimitsInstanceId = _CfprCommWebSvcLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 1),
    _CfprCommWebSvcLimitsInstanceId_Type()
)
cfprCommWebSvcLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsInstanceId.setStatus("current")
_CfprCommWebSvcLimitsDn_Type = CfprManagedObjectDn
_CfprCommWebSvcLimitsDn_Object = MibTableColumn
cfprCommWebSvcLimitsDn = _CfprCommWebSvcLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 2),
    _CfprCommWebSvcLimitsDn_Type()
)
cfprCommWebSvcLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsDn.setStatus("current")
_CfprCommWebSvcLimitsRn_Type = SnmpAdminString
_CfprCommWebSvcLimitsRn_Object = MibTableColumn
cfprCommWebSvcLimitsRn = _CfprCommWebSvcLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 3),
    _CfprCommWebSvcLimitsRn_Type()
)
cfprCommWebSvcLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsRn.setStatus("current")
_CfprCommWebSvcLimitsDescr_Type = SnmpAdminString
_CfprCommWebSvcLimitsDescr_Object = MibTableColumn
cfprCommWebSvcLimitsDescr = _CfprCommWebSvcLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 4),
    _CfprCommWebSvcLimitsDescr_Type()
)
cfprCommWebSvcLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsDescr.setStatus("current")
_CfprCommWebSvcLimitsIntId_Type = SnmpAdminString
_CfprCommWebSvcLimitsIntId_Object = MibTableColumn
cfprCommWebSvcLimitsIntId = _CfprCommWebSvcLimitsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 5),
    _CfprCommWebSvcLimitsIntId_Type()
)
cfprCommWebSvcLimitsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsIntId.setStatus("current")
_CfprCommWebSvcLimitsName_Type = SnmpAdminString
_CfprCommWebSvcLimitsName_Object = MibTableColumn
cfprCommWebSvcLimitsName = _CfprCommWebSvcLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 6),
    _CfprCommWebSvcLimitsName_Type()
)
cfprCommWebSvcLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsName.setStatus("current")
_CfprCommWebSvcLimitsPolicyLevel_Type = Gauge32
_CfprCommWebSvcLimitsPolicyLevel_Object = MibTableColumn
cfprCommWebSvcLimitsPolicyLevel = _CfprCommWebSvcLimitsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 7),
    _CfprCommWebSvcLimitsPolicyLevel_Type()
)
cfprCommWebSvcLimitsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsPolicyLevel.setStatus("current")
_CfprCommWebSvcLimitsPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommWebSvcLimitsPolicyOwner_Object = MibTableColumn
cfprCommWebSvcLimitsPolicyOwner = _CfprCommWebSvcLimitsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 8),
    _CfprCommWebSvcLimitsPolicyOwner_Type()
)
cfprCommWebSvcLimitsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsPolicyOwner.setStatus("current")
_CfprCommWebSvcLimitsSessionsPerUser_Type = Gauge32
_CfprCommWebSvcLimitsSessionsPerUser_Object = MibTableColumn
cfprCommWebSvcLimitsSessionsPerUser = _CfprCommWebSvcLimitsSessionsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 9),
    _CfprCommWebSvcLimitsSessionsPerUser_Type()
)
cfprCommWebSvcLimitsSessionsPerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsSessionsPerUser.setStatus("current")
_CfprCommWebSvcLimitsTotalSessions_Type = Gauge32
_CfprCommWebSvcLimitsTotalSessions_Object = MibTableColumn
cfprCommWebSvcLimitsTotalSessions = _CfprCommWebSvcLimitsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 28, 1, 10),
    _CfprCommWebSvcLimitsTotalSessions_Type()
)
cfprCommWebSvcLimitsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWebSvcLimitsTotalSessions.setStatus("current")
_CfprCommWsmanTable_Object = MibTable
cfprCommWsmanTable = _CfprCommWsmanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29)
)
if mibBuilder.loadTexts:
    cfprCommWsmanTable.setStatus("current")
_CfprCommWsmanEntry_Object = MibTableRow
cfprCommWsmanEntry = _CfprCommWsmanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1)
)
cfprCommWsmanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommWsmanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommWsmanEntry.setStatus("current")
_CfprCommWsmanInstanceId_Type = CfprManagedObjectId
_CfprCommWsmanInstanceId_Object = MibTableColumn
cfprCommWsmanInstanceId = _CfprCommWsmanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 1),
    _CfprCommWsmanInstanceId_Type()
)
cfprCommWsmanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommWsmanInstanceId.setStatus("current")
_CfprCommWsmanDn_Type = CfprManagedObjectDn
_CfprCommWsmanDn_Object = MibTableColumn
cfprCommWsmanDn = _CfprCommWsmanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 2),
    _CfprCommWsmanDn_Type()
)
cfprCommWsmanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanDn.setStatus("current")
_CfprCommWsmanRn_Type = SnmpAdminString
_CfprCommWsmanRn_Object = MibTableColumn
cfprCommWsmanRn = _CfprCommWsmanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 3),
    _CfprCommWsmanRn_Type()
)
cfprCommWsmanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanRn.setStatus("current")
_CfprCommWsmanAdminState_Type = CfprCommAdminState
_CfprCommWsmanAdminState_Object = MibTableColumn
cfprCommWsmanAdminState = _CfprCommWsmanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 4),
    _CfprCommWsmanAdminState_Type()
)
cfprCommWsmanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanAdminState.setStatus("current")
_CfprCommWsmanDescr_Type = SnmpAdminString
_CfprCommWsmanDescr_Object = MibTableColumn
cfprCommWsmanDescr = _CfprCommWsmanDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 5),
    _CfprCommWsmanDescr_Type()
)
cfprCommWsmanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanDescr.setStatus("current")
_CfprCommWsmanIntId_Type = SnmpAdminString
_CfprCommWsmanIntId_Object = MibTableColumn
cfprCommWsmanIntId = _CfprCommWsmanIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 6),
    _CfprCommWsmanIntId_Type()
)
cfprCommWsmanIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanIntId.setStatus("current")
_CfprCommWsmanName_Type = SnmpAdminString
_CfprCommWsmanName_Object = MibTableColumn
cfprCommWsmanName = _CfprCommWsmanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 7),
    _CfprCommWsmanName_Type()
)
cfprCommWsmanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanName.setStatus("current")
_CfprCommWsmanOperPort_Type = Gauge32
_CfprCommWsmanOperPort_Object = MibTableColumn
cfprCommWsmanOperPort = _CfprCommWsmanOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 8),
    _CfprCommWsmanOperPort_Type()
)
cfprCommWsmanOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanOperPort.setStatus("current")
_CfprCommWsmanPolicyLevel_Type = Gauge32
_CfprCommWsmanPolicyLevel_Object = MibTableColumn
cfprCommWsmanPolicyLevel = _CfprCommWsmanPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 9),
    _CfprCommWsmanPolicyLevel_Type()
)
cfprCommWsmanPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanPolicyLevel.setStatus("current")
_CfprCommWsmanPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommWsmanPolicyOwner_Object = MibTableColumn
cfprCommWsmanPolicyOwner = _CfprCommWsmanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 10),
    _CfprCommWsmanPolicyOwner_Type()
)
cfprCommWsmanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanPolicyOwner.setStatus("current")
_CfprCommWsmanPort_Type = Gauge32
_CfprCommWsmanPort_Object = MibTableColumn
cfprCommWsmanPort = _CfprCommWsmanPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 11),
    _CfprCommWsmanPort_Type()
)
cfprCommWsmanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanPort.setStatus("current")
_CfprCommWsmanProto_Type = CfprCommWebProto
_CfprCommWsmanProto_Object = MibTableColumn
cfprCommWsmanProto = _CfprCommWsmanProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 29, 1, 12),
    _CfprCommWsmanProto_Type()
)
cfprCommWsmanProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommWsmanProto.setStatus("current")
_CfprCommFipsConfigTable_Object = MibTable
cfprCommFipsConfigTable = _CfprCommFipsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31)
)
if mibBuilder.loadTexts:
    cfprCommFipsConfigTable.setStatus("current")
_CfprCommFipsConfigEntry_Object = MibTableRow
cfprCommFipsConfigEntry = _CfprCommFipsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1)
)
cfprCommFipsConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommFipsConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommFipsConfigEntry.setStatus("current")
_CfprCommFipsConfigInstanceId_Type = CfprManagedObjectId
_CfprCommFipsConfigInstanceId_Object = MibTableColumn
cfprCommFipsConfigInstanceId = _CfprCommFipsConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 1),
    _CfprCommFipsConfigInstanceId_Type()
)
cfprCommFipsConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommFipsConfigInstanceId.setStatus("current")
_CfprCommFipsConfigDn_Type = CfprManagedObjectDn
_CfprCommFipsConfigDn_Object = MibTableColumn
cfprCommFipsConfigDn = _CfprCommFipsConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 2),
    _CfprCommFipsConfigDn_Type()
)
cfprCommFipsConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigDn.setStatus("current")
_CfprCommFipsConfigRn_Type = SnmpAdminString
_CfprCommFipsConfigRn_Object = MibTableColumn
cfprCommFipsConfigRn = _CfprCommFipsConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 3),
    _CfprCommFipsConfigRn_Type()
)
cfprCommFipsConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigRn.setStatus("current")
_CfprCommFipsConfigCcAdminState_Type = CfprCommModeAdminState
_CfprCommFipsConfigCcAdminState_Object = MibTableColumn
cfprCommFipsConfigCcAdminState = _CfprCommFipsConfigCcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 4),
    _CfprCommFipsConfigCcAdminState_Type()
)
cfprCommFipsConfigCcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigCcAdminState.setStatus("current")
_CfprCommFipsConfigCcOperState_Type = CfprCommModeAdminState
_CfprCommFipsConfigCcOperState_Object = MibTableColumn
cfprCommFipsConfigCcOperState = _CfprCommFipsConfigCcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 5),
    _CfprCommFipsConfigCcOperState_Type()
)
cfprCommFipsConfigCcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigCcOperState.setStatus("current")
_CfprCommFipsConfigDescr_Type = SnmpAdminString
_CfprCommFipsConfigDescr_Object = MibTableColumn
cfprCommFipsConfigDescr = _CfprCommFipsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 6),
    _CfprCommFipsConfigDescr_Type()
)
cfprCommFipsConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigDescr.setStatus("current")
_CfprCommFipsConfigFipsAdminState_Type = CfprCommModeAdminState
_CfprCommFipsConfigFipsAdminState_Object = MibTableColumn
cfprCommFipsConfigFipsAdminState = _CfprCommFipsConfigFipsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 7),
    _CfprCommFipsConfigFipsAdminState_Type()
)
cfprCommFipsConfigFipsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigFipsAdminState.setStatus("current")
_CfprCommFipsConfigFipsOperState_Type = CfprCommModeAdminState
_CfprCommFipsConfigFipsOperState_Object = MibTableColumn
cfprCommFipsConfigFipsOperState = _CfprCommFipsConfigFipsOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 8),
    _CfprCommFipsConfigFipsOperState_Type()
)
cfprCommFipsConfigFipsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigFipsOperState.setStatus("current")
_CfprCommFipsConfigModeFlag_Type = CfprCommModeFlag
_CfprCommFipsConfigModeFlag_Object = MibTableColumn
cfprCommFipsConfigModeFlag = _CfprCommFipsConfigModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 9),
    _CfprCommFipsConfigModeFlag_Type()
)
cfprCommFipsConfigModeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigModeFlag.setStatus("current")
_CfprCommFipsConfigName_Type = SnmpAdminString
_CfprCommFipsConfigName_Object = MibTableColumn
cfprCommFipsConfigName = _CfprCommFipsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 10),
    _CfprCommFipsConfigName_Type()
)
cfprCommFipsConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigName.setStatus("current")
_CfprCommFipsConfigRebootState_Type = CfprCommRebootState
_CfprCommFipsConfigRebootState_Object = MibTableColumn
cfprCommFipsConfigRebootState = _CfprCommFipsConfigRebootState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 31, 1, 11),
    _CfprCommFipsConfigRebootState_Type()
)
cfprCommFipsConfigRebootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommFipsConfigRebootState.setStatus("current")
_CfprCommIPv6BlockTable_Object = MibTable
cfprCommIPv6BlockTable = _CfprCommIPv6BlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 32)
)
if mibBuilder.loadTexts:
    cfprCommIPv6BlockTable.setStatus("current")
_CfprCommIPv6BlockEntry_Object = MibTableRow
cfprCommIPv6BlockEntry = _CfprCommIPv6BlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 32, 1)
)
cfprCommIPv6BlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommIPv6BlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommIPv6BlockEntry.setStatus("current")
_CfprCommIPv6BlockInstanceId_Type = CfprManagedObjectId
_CfprCommIPv6BlockInstanceId_Object = MibTableColumn
cfprCommIPv6BlockInstanceId = _CfprCommIPv6BlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 32, 1, 1),
    _CfprCommIPv6BlockInstanceId_Type()
)
cfprCommIPv6BlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommIPv6BlockInstanceId.setStatus("current")
_CfprCommIPv6BlockDn_Type = CfprManagedObjectDn
_CfprCommIPv6BlockDn_Object = MibTableColumn
cfprCommIPv6BlockDn = _CfprCommIPv6BlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 32, 1, 2),
    _CfprCommIPv6BlockDn_Type()
)
cfprCommIPv6BlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIPv6BlockDn.setStatus("current")
_CfprCommIPv6BlockRn_Type = SnmpAdminString
_CfprCommIPv6BlockRn_Object = MibTableColumn
cfprCommIPv6BlockRn = _CfprCommIPv6BlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 32, 1, 3),
    _CfprCommIPv6BlockRn_Type()
)
cfprCommIPv6BlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIPv6BlockRn.setStatus("current")
_CfprCommIPv6BlockIpAddress_Type = InetAddressIPv6
_CfprCommIPv6BlockIpAddress_Object = MibTableColumn
cfprCommIPv6BlockIpAddress = _CfprCommIPv6BlockIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 32, 1, 4),
    _CfprCommIPv6BlockIpAddress_Type()
)
cfprCommIPv6BlockIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIPv6BlockIpAddress.setStatus("current")
_CfprCommIPv6BlockPrefixLength_Type = CfprCommIpv6Prefix
_CfprCommIPv6BlockPrefixLength_Object = MibTableColumn
cfprCommIPv6BlockPrefixLength = _CfprCommIPv6BlockPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 32, 1, 5),
    _CfprCommIPv6BlockPrefixLength_Type()
)
cfprCommIPv6BlockPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIPv6BlockPrefixLength.setStatus("current")
_CfprCommIPv6BlockProtocol_Type = CfprCommServiceProtocol
_CfprCommIPv6BlockProtocol_Object = MibTableColumn
cfprCommIPv6BlockProtocol = _CfprCommIPv6BlockProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 32, 1, 6),
    _CfprCommIPv6BlockProtocol_Type()
)
cfprCommIPv6BlockProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIPv6BlockProtocol.setStatus("current")
_CfprCommIpBlockTable_Object = MibTable
cfprCommIpBlockTable = _CfprCommIpBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 33)
)
if mibBuilder.loadTexts:
    cfprCommIpBlockTable.setStatus("current")
_CfprCommIpBlockEntry_Object = MibTableRow
cfprCommIpBlockEntry = _CfprCommIpBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 33, 1)
)
cfprCommIpBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommIpBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommIpBlockEntry.setStatus("current")
_CfprCommIpBlockInstanceId_Type = CfprManagedObjectId
_CfprCommIpBlockInstanceId_Object = MibTableColumn
cfprCommIpBlockInstanceId = _CfprCommIpBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 33, 1, 1),
    _CfprCommIpBlockInstanceId_Type()
)
cfprCommIpBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommIpBlockInstanceId.setStatus("current")
_CfprCommIpBlockDn_Type = CfprManagedObjectDn
_CfprCommIpBlockDn_Object = MibTableColumn
cfprCommIpBlockDn = _CfprCommIpBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 33, 1, 2),
    _CfprCommIpBlockDn_Type()
)
cfprCommIpBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIpBlockDn.setStatus("current")
_CfprCommIpBlockRn_Type = SnmpAdminString
_CfprCommIpBlockRn_Object = MibTableColumn
cfprCommIpBlockRn = _CfprCommIpBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 33, 1, 3),
    _CfprCommIpBlockRn_Type()
)
cfprCommIpBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIpBlockRn.setStatus("current")
_CfprCommIpBlockIpAddress_Type = InetAddressIPv4
_CfprCommIpBlockIpAddress_Object = MibTableColumn
cfprCommIpBlockIpAddress = _CfprCommIpBlockIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 33, 1, 4),
    _CfprCommIpBlockIpAddress_Type()
)
cfprCommIpBlockIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIpBlockIpAddress.setStatus("current")
_CfprCommIpBlockPrefixLength_Type = CfprCommIpv4Prefix
_CfprCommIpBlockPrefixLength_Object = MibTableColumn
cfprCommIpBlockPrefixLength = _CfprCommIpBlockPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 33, 1, 5),
    _CfprCommIpBlockPrefixLength_Type()
)
cfprCommIpBlockPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIpBlockPrefixLength.setStatus("current")
_CfprCommIpBlockProtocol_Type = CfprCommServiceProtocol
_CfprCommIpBlockProtocol_Object = MibTableColumn
cfprCommIpBlockProtocol = _CfprCommIpBlockProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 33, 1, 6),
    _CfprCommIpBlockProtocol_Type()
)
cfprCommIpBlockProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommIpBlockProtocol.setStatus("current")
_CfprCommSshPubkeyTable_Object = MibTable
cfprCommSshPubkeyTable = _CfprCommSshPubkeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34)
)
if mibBuilder.loadTexts:
    cfprCommSshPubkeyTable.setStatus("current")
_CfprCommSshPubkeyEntry_Object = MibTableRow
cfprCommSshPubkeyEntry = _CfprCommSshPubkeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1)
)
cfprCommSshPubkeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSshPubkeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSshPubkeyEntry.setStatus("current")
_CfprCommSshPubkeyInstanceId_Type = CfprManagedObjectId
_CfprCommSshPubkeyInstanceId_Object = MibTableColumn
cfprCommSshPubkeyInstanceId = _CfprCommSshPubkeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 1),
    _CfprCommSshPubkeyInstanceId_Type()
)
cfprCommSshPubkeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyInstanceId.setStatus("current")
_CfprCommSshPubkeyDn_Type = CfprManagedObjectDn
_CfprCommSshPubkeyDn_Object = MibTableColumn
cfprCommSshPubkeyDn = _CfprCommSshPubkeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 2),
    _CfprCommSshPubkeyDn_Type()
)
cfprCommSshPubkeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyDn.setStatus("current")
_CfprCommSshPubkeyRn_Type = SnmpAdminString
_CfprCommSshPubkeyRn_Object = MibTableColumn
cfprCommSshPubkeyRn = _CfprCommSshPubkeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 3),
    _CfprCommSshPubkeyRn_Type()
)
cfprCommSshPubkeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyRn.setStatus("current")
_CfprCommSshPubkeyAdminState_Type = CfprCommAdminState
_CfprCommSshPubkeyAdminState_Object = MibTableColumn
cfprCommSshPubkeyAdminState = _CfprCommSshPubkeyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 4),
    _CfprCommSshPubkeyAdminState_Type()
)
cfprCommSshPubkeyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyAdminState.setStatus("current")
_CfprCommSshPubkeyDescr_Type = SnmpAdminString
_CfprCommSshPubkeyDescr_Object = MibTableColumn
cfprCommSshPubkeyDescr = _CfprCommSshPubkeyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 5),
    _CfprCommSshPubkeyDescr_Type()
)
cfprCommSshPubkeyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyDescr.setStatus("current")
_CfprCommSshPubkeyIntId_Type = SnmpAdminString
_CfprCommSshPubkeyIntId_Object = MibTableColumn
cfprCommSshPubkeyIntId = _CfprCommSshPubkeyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 6),
    _CfprCommSshPubkeyIntId_Type()
)
cfprCommSshPubkeyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyIntId.setStatus("current")
_CfprCommSshPubkeyName_Type = SnmpAdminString
_CfprCommSshPubkeyName_Object = MibTableColumn
cfprCommSshPubkeyName = _CfprCommSshPubkeyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 7),
    _CfprCommSshPubkeyName_Type()
)
cfprCommSshPubkeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyName.setStatus("current")
_CfprCommSshPubkeyOperPort_Type = Gauge32
_CfprCommSshPubkeyOperPort_Object = MibTableColumn
cfprCommSshPubkeyOperPort = _CfprCommSshPubkeyOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 8),
    _CfprCommSshPubkeyOperPort_Type()
)
cfprCommSshPubkeyOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyOperPort.setStatus("current")
_CfprCommSshPubkeyPolicyLevel_Type = Gauge32
_CfprCommSshPubkeyPolicyLevel_Object = MibTableColumn
cfprCommSshPubkeyPolicyLevel = _CfprCommSshPubkeyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 9),
    _CfprCommSshPubkeyPolicyLevel_Type()
)
cfprCommSshPubkeyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyPolicyLevel.setStatus("current")
_CfprCommSshPubkeyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCommSshPubkeyPolicyOwner_Object = MibTableColumn
cfprCommSshPubkeyPolicyOwner = _CfprCommSshPubkeyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 10),
    _CfprCommSshPubkeyPolicyOwner_Type()
)
cfprCommSshPubkeyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyPolicyOwner.setStatus("current")
_CfprCommSshPubkeyPort_Type = Gauge32
_CfprCommSshPubkeyPort_Object = MibTableColumn
cfprCommSshPubkeyPort = _CfprCommSshPubkeyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 11),
    _CfprCommSshPubkeyPort_Type()
)
cfprCommSshPubkeyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyPort.setStatus("current")
_CfprCommSshPubkeyProto_Type = CfprCommProtocol
_CfprCommSshPubkeyProto_Object = MibTableColumn
cfprCommSshPubkeyProto = _CfprCommSshPubkeyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 34, 1, 12),
    _CfprCommSshPubkeyProto_Type()
)
cfprCommSshPubkeyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyProto.setStatus("current")
_CfprCommSshPubkeyChainTable_Object = MibTable
cfprCommSshPubkeyChainTable = _CfprCommSshPubkeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35)
)
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainTable.setStatus("current")
_CfprCommSshPubkeyChainEntry_Object = MibTableRow
cfprCommSshPubkeyChainEntry = _CfprCommSshPubkeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1)
)
cfprCommSshPubkeyChainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSshPubkeyChainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainEntry.setStatus("current")
_CfprCommSshPubkeyChainInstanceId_Type = CfprManagedObjectId
_CfprCommSshPubkeyChainInstanceId_Object = MibTableColumn
cfprCommSshPubkeyChainInstanceId = _CfprCommSshPubkeyChainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 1),
    _CfprCommSshPubkeyChainInstanceId_Type()
)
cfprCommSshPubkeyChainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainInstanceId.setStatus("current")
_CfprCommSshPubkeyChainDn_Type = CfprManagedObjectDn
_CfprCommSshPubkeyChainDn_Object = MibTableColumn
cfprCommSshPubkeyChainDn = _CfprCommSshPubkeyChainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 2),
    _CfprCommSshPubkeyChainDn_Type()
)
cfprCommSshPubkeyChainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainDn.setStatus("current")
_CfprCommSshPubkeyChainRn_Type = SnmpAdminString
_CfprCommSshPubkeyChainRn_Object = MibTableColumn
cfprCommSshPubkeyChainRn = _CfprCommSshPubkeyChainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 3),
    _CfprCommSshPubkeyChainRn_Type()
)
cfprCommSshPubkeyChainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainRn.setStatus("current")
_CfprCommSshPubkeyChainAdminState_Type = CfprCommClientItemAdminState
_CfprCommSshPubkeyChainAdminState_Object = MibTableColumn
cfprCommSshPubkeyChainAdminState = _CfprCommSshPubkeyChainAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 4),
    _CfprCommSshPubkeyChainAdminState_Type()
)
cfprCommSshPubkeyChainAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainAdminState.setStatus("current")
_CfprCommSshPubkeyChainDescr_Type = SnmpAdminString
_CfprCommSshPubkeyChainDescr_Object = MibTableColumn
cfprCommSshPubkeyChainDescr = _CfprCommSshPubkeyChainDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 5),
    _CfprCommSshPubkeyChainDescr_Type()
)
cfprCommSshPubkeyChainDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainDescr.setStatus("current")
_CfprCommSshPubkeyChainHostname_Type = SnmpAdminString
_CfprCommSshPubkeyChainHostname_Object = MibTableColumn
cfprCommSshPubkeyChainHostname = _CfprCommSshPubkeyChainHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 6),
    _CfprCommSshPubkeyChainHostname_Type()
)
cfprCommSshPubkeyChainHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainHostname.setStatus("current")
_CfprCommSshPubkeyChainKeyString_Type = SnmpAdminString
_CfprCommSshPubkeyChainKeyString_Object = MibTableColumn
cfprCommSshPubkeyChainKeyString = _CfprCommSshPubkeyChainKeyString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 7),
    _CfprCommSshPubkeyChainKeyString_Type()
)
cfprCommSshPubkeyChainKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainKeyString.setStatus("current")
_CfprCommSshPubkeyChainName_Type = SnmpAdminString
_CfprCommSshPubkeyChainName_Object = MibTableColumn
cfprCommSshPubkeyChainName = _CfprCommSshPubkeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 8),
    _CfprCommSshPubkeyChainName_Type()
)
cfprCommSshPubkeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainName.setStatus("current")
_CfprCommSshPubkeyChainServer_Type = SnmpAdminString
_CfprCommSshPubkeyChainServer_Object = MibTableColumn
cfprCommSshPubkeyChainServer = _CfprCommSshPubkeyChainServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 35, 1, 9),
    _CfprCommSshPubkeyChainServer_Type()
)
cfprCommSshPubkeyChainServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshPubkeyChainServer.setStatus("current")
_CfprCommSshcTable_Object = MibTable
cfprCommSshcTable = _CfprCommSshcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36)
)
if mibBuilder.loadTexts:
    cfprCommSshcTable.setStatus("current")
_CfprCommSshcEntry_Object = MibTableRow
cfprCommSshcEntry = _CfprCommSshcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1)
)
cfprCommSshcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSshcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSshcEntry.setStatus("current")
_CfprCommSshcInstanceId_Type = CfprManagedObjectId
_CfprCommSshcInstanceId_Object = MibTableColumn
cfprCommSshcInstanceId = _CfprCommSshcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 1),
    _CfprCommSshcInstanceId_Type()
)
cfprCommSshcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSshcInstanceId.setStatus("current")
_CfprCommSshcDn_Type = CfprManagedObjectDn
_CfprCommSshcDn_Object = MibTableColumn
cfprCommSshcDn = _CfprCommSshcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 2),
    _CfprCommSshcDn_Type()
)
cfprCommSshcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcDn.setStatus("current")
_CfprCommSshcRn_Type = SnmpAdminString
_CfprCommSshcRn_Object = MibTableColumn
cfprCommSshcRn = _CfprCommSshcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 3),
    _CfprCommSshcRn_Type()
)
cfprCommSshcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcRn.setStatus("current")
_CfprCommSshcAdminState_Type = CfprCommClientItemAdminState
_CfprCommSshcAdminState_Object = MibTableColumn
cfprCommSshcAdminState = _CfprCommSshcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 4),
    _CfprCommSshcAdminState_Type()
)
cfprCommSshcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcAdminState.setStatus("current")
_CfprCommSshcCliEncryptAlgo_Type = CfprCommSshcCliEncryptAlgo
_CfprCommSshcCliEncryptAlgo_Object = MibTableColumn
cfprCommSshcCliEncryptAlgo = _CfprCommSshcCliEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 5),
    _CfprCommSshcCliEncryptAlgo_Type()
)
cfprCommSshcCliEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcCliEncryptAlgo.setStatus("current")
_CfprCommSshcCliKexAlgo_Type = CfprCommSshcCliKexAlgo
_CfprCommSshcCliKexAlgo_Object = MibTableColumn
cfprCommSshcCliKexAlgo = _CfprCommSshcCliKexAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 6),
    _CfprCommSshcCliKexAlgo_Type()
)
cfprCommSshcCliKexAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcCliKexAlgo.setStatus("current")
_CfprCommSshcCliMacAlgo_Type = CfprCommSshcCliMacAlgo
_CfprCommSshcCliMacAlgo_Object = MibTableColumn
cfprCommSshcCliMacAlgo = _CfprCommSshcCliMacAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 7),
    _CfprCommSshcCliMacAlgo_Type()
)
cfprCommSshcCliMacAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcCliMacAlgo.setStatus("current")
_CfprCommSshcDescr_Type = SnmpAdminString
_CfprCommSshcDescr_Object = MibTableColumn
cfprCommSshcDescr = _CfprCommSshcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 8),
    _CfprCommSshcDescr_Type()
)
cfprCommSshcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcDescr.setStatus("current")
_CfprCommSshcHostname_Type = SnmpAdminString
_CfprCommSshcHostname_Object = MibTableColumn
cfprCommSshcHostname = _CfprCommSshcHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 9),
    _CfprCommSshcHostname_Type()
)
cfprCommSshcHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcHostname.setStatus("current")
_CfprCommSshcName_Type = SnmpAdminString
_CfprCommSshcName_Object = MibTableColumn
cfprCommSshcName = _CfprCommSshcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 10),
    _CfprCommSshcName_Type()
)
cfprCommSshcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcName.setStatus("current")
_CfprCommSshcStrictKeyCheck_Type = CfprCommSshcStrictKeyCheck
_CfprCommSshcStrictKeyCheck_Object = MibTableColumn
cfprCommSshcStrictKeyCheck = _CfprCommSshcStrictKeyCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 11),
    _CfprCommSshcStrictKeyCheck_Type()
)
cfprCommSshcStrictKeyCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcStrictKeyCheck.setStatus("current")
_CfprCommSshcTime_Type = Gauge32
_CfprCommSshcTime_Object = MibTableColumn
cfprCommSshcTime = _CfprCommSshcTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 12),
    _CfprCommSshcTime_Type()
)
cfprCommSshcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcTime.setStatus("current")
_CfprCommSshcVolume_Type = Gauge32
_CfprCommSshcVolume_Object = MibTableColumn
cfprCommSshcVolume = _CfprCommSshcVolume_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 36, 1, 13),
    _CfprCommSshcVolume_Type()
)
cfprCommSshcVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSshcVolume.setStatus("current")
_CfprCommSyslogPlatformTable_Object = MibTable
cfprCommSyslogPlatformTable = _CfprCommSyslogPlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37)
)
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformTable.setStatus("current")
_CfprCommSyslogPlatformEntry_Object = MibTableRow
cfprCommSyslogPlatformEntry = _CfprCommSyslogPlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37, 1)
)
cfprCommSyslogPlatformEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommSyslogPlatformInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformEntry.setStatus("current")
_CfprCommSyslogPlatformInstanceId_Type = CfprManagedObjectId
_CfprCommSyslogPlatformInstanceId_Object = MibTableColumn
cfprCommSyslogPlatformInstanceId = _CfprCommSyslogPlatformInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37, 1, 1),
    _CfprCommSyslogPlatformInstanceId_Type()
)
cfprCommSyslogPlatformInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformInstanceId.setStatus("current")
_CfprCommSyslogPlatformDn_Type = CfprManagedObjectDn
_CfprCommSyslogPlatformDn_Object = MibTableColumn
cfprCommSyslogPlatformDn = _CfprCommSyslogPlatformDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37, 1, 2),
    _CfprCommSyslogPlatformDn_Type()
)
cfprCommSyslogPlatformDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformDn.setStatus("current")
_CfprCommSyslogPlatformRn_Type = SnmpAdminString
_CfprCommSyslogPlatformRn_Object = MibTableColumn
cfprCommSyslogPlatformRn = _CfprCommSyslogPlatformRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37, 1, 3),
    _CfprCommSyslogPlatformRn_Type()
)
cfprCommSyslogPlatformRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformRn.setStatus("current")
_CfprCommSyslogPlatformAdminState_Type = CfprCommSyslogPlatformAdminState
_CfprCommSyslogPlatformAdminState_Object = MibTableColumn
cfprCommSyslogPlatformAdminState = _CfprCommSyslogPlatformAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37, 1, 4),
    _CfprCommSyslogPlatformAdminState_Type()
)
cfprCommSyslogPlatformAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformAdminState.setStatus("current")
_CfprCommSyslogPlatformDescr_Type = SnmpAdminString
_CfprCommSyslogPlatformDescr_Object = MibTableColumn
cfprCommSyslogPlatformDescr = _CfprCommSyslogPlatformDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37, 1, 5),
    _CfprCommSyslogPlatformDescr_Type()
)
cfprCommSyslogPlatformDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformDescr.setStatus("current")
_CfprCommSyslogPlatformName_Type = SnmpAdminString
_CfprCommSyslogPlatformName_Object = MibTableColumn
cfprCommSyslogPlatformName = _CfprCommSyslogPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37, 1, 6),
    _CfprCommSyslogPlatformName_Type()
)
cfprCommSyslogPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformName.setStatus("current")
_CfprCommSyslogPlatformSeverity_Type = CfprCommSyslogSeverity
_CfprCommSyslogPlatformSeverity_Object = MibTableColumn
cfprCommSyslogPlatformSeverity = _CfprCommSyslogPlatformSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 37, 1, 7),
    _CfprCommSyslogPlatformSeverity_Type()
)
cfprCommSyslogPlatformSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommSyslogPlatformSeverity.setStatus("current")
_CfprCommDeviceManagerTable_Object = MibTable
cfprCommDeviceManagerTable = _CfprCommDeviceManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38)
)
if mibBuilder.loadTexts:
    cfprCommDeviceManagerTable.setStatus("current")
_CfprCommDeviceManagerEntry_Object = MibTableRow
cfprCommDeviceManagerEntry = _CfprCommDeviceManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1)
)
cfprCommDeviceManagerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommDeviceManagerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommDeviceManagerEntry.setStatus("current")
_CfprCommDeviceManagerInstanceId_Type = CfprManagedObjectId
_CfprCommDeviceManagerInstanceId_Object = MibTableColumn
cfprCommDeviceManagerInstanceId = _CfprCommDeviceManagerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 1),
    _CfprCommDeviceManagerInstanceId_Type()
)
cfprCommDeviceManagerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerInstanceId.setStatus("current")
_CfprCommDeviceManagerDn_Type = CfprManagedObjectDn
_CfprCommDeviceManagerDn_Object = MibTableColumn
cfprCommDeviceManagerDn = _CfprCommDeviceManagerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 2),
    _CfprCommDeviceManagerDn_Type()
)
cfprCommDeviceManagerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerDn.setStatus("current")
_CfprCommDeviceManagerRn_Type = SnmpAdminString
_CfprCommDeviceManagerRn_Object = MibTableColumn
cfprCommDeviceManagerRn = _CfprCommDeviceManagerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 3),
    _CfprCommDeviceManagerRn_Type()
)
cfprCommDeviceManagerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerRn.setStatus("current")
_CfprCommDeviceManagerDescr_Type = SnmpAdminString
_CfprCommDeviceManagerDescr_Object = MibTableColumn
cfprCommDeviceManagerDescr = _CfprCommDeviceManagerDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 4),
    _CfprCommDeviceManagerDescr_Type()
)
cfprCommDeviceManagerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerDescr.setStatus("current")
_CfprCommDeviceManagerDeviceState_Type = CfprCommDeviceState
_CfprCommDeviceManagerDeviceState_Object = MibTableColumn
cfprCommDeviceManagerDeviceState = _CfprCommDeviceManagerDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 5),
    _CfprCommDeviceManagerDeviceState_Type()
)
cfprCommDeviceManagerDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerDeviceState.setStatus("current")
_CfprCommDeviceManagerErrorMsg_Type = SnmpAdminString
_CfprCommDeviceManagerErrorMsg_Object = MibTableColumn
cfprCommDeviceManagerErrorMsg = _CfprCommDeviceManagerErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 6),
    _CfprCommDeviceManagerErrorMsg_Type()
)
cfprCommDeviceManagerErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerErrorMsg.setStatus("current")
_CfprCommDeviceManagerHostname_Type = SnmpAdminString
_CfprCommDeviceManagerHostname_Object = MibTableColumn
cfprCommDeviceManagerHostname = _CfprCommDeviceManagerHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 7),
    _CfprCommDeviceManagerHostname_Type()
)
cfprCommDeviceManagerHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerHostname.setStatus("current")
_CfprCommDeviceManagerName_Type = SnmpAdminString
_CfprCommDeviceManagerName_Object = MibTableColumn
cfprCommDeviceManagerName = _CfprCommDeviceManagerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 8),
    _CfprCommDeviceManagerName_Type()
)
cfprCommDeviceManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerName.setStatus("current")
_CfprCommDeviceManagerNatId_Type = SnmpAdminString
_CfprCommDeviceManagerNatId_Object = MibTableColumn
cfprCommDeviceManagerNatId = _CfprCommDeviceManagerNatId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 9),
    _CfprCommDeviceManagerNatId_Type()
)
cfprCommDeviceManagerNatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerNatId.setStatus("current")
_CfprCommDeviceManagerRegKey_Type = SnmpAdminString
_CfprCommDeviceManagerRegKey_Object = MibTableColumn
cfprCommDeviceManagerRegKey = _CfprCommDeviceManagerRegKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 10),
    _CfprCommDeviceManagerRegKey_Type()
)
cfprCommDeviceManagerRegKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerRegKey.setStatus("current")
_CfprCommDeviceManagerRegState_Type = CfprCommRegState
_CfprCommDeviceManagerRegState_Object = MibTableColumn
cfprCommDeviceManagerRegState = _CfprCommDeviceManagerRegState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 38, 1, 11),
    _CfprCommDeviceManagerRegState_Type()
)
cfprCommDeviceManagerRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommDeviceManagerRegState.setStatus("current")
_CfprCommTelemetryTable_Object = MibTable
cfprCommTelemetryTable = _CfprCommTelemetryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39)
)
if mibBuilder.loadTexts:
    cfprCommTelemetryTable.setStatus("current")
_CfprCommTelemetryEntry_Object = MibTableRow
cfprCommTelemetryEntry = _CfprCommTelemetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1)
)
cfprCommTelemetryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommTelemetryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommTelemetryEntry.setStatus("current")
_CfprCommTelemetryInstanceId_Type = CfprManagedObjectId
_CfprCommTelemetryInstanceId_Object = MibTableColumn
cfprCommTelemetryInstanceId = _CfprCommTelemetryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 1),
    _CfprCommTelemetryInstanceId_Type()
)
cfprCommTelemetryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommTelemetryInstanceId.setStatus("current")
_CfprCommTelemetryDn_Type = CfprManagedObjectDn
_CfprCommTelemetryDn_Object = MibTableColumn
cfprCommTelemetryDn = _CfprCommTelemetryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 2),
    _CfprCommTelemetryDn_Type()
)
cfprCommTelemetryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryDn.setStatus("current")
_CfprCommTelemetryRn_Type = SnmpAdminString
_CfprCommTelemetryRn_Object = MibTableColumn
cfprCommTelemetryRn = _CfprCommTelemetryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 3),
    _CfprCommTelemetryRn_Type()
)
cfprCommTelemetryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryRn.setStatus("current")
_CfprCommTelemetryAdminState_Type = CfprCommTelemetryAdminState
_CfprCommTelemetryAdminState_Object = MibTableColumn
cfprCommTelemetryAdminState = _CfprCommTelemetryAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 4),
    _CfprCommTelemetryAdminState_Type()
)
cfprCommTelemetryAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryAdminState.setStatus("current")
_CfprCommTelemetryEnableFlag_Type = TruthValue
_CfprCommTelemetryEnableFlag_Object = MibTableColumn
cfprCommTelemetryEnableFlag = _CfprCommTelemetryEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 5),
    _CfprCommTelemetryEnableFlag_Type()
)
cfprCommTelemetryEnableFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryEnableFlag.setStatus("current")
_CfprCommTelemetryErrorMessage_Type = SnmpAdminString
_CfprCommTelemetryErrorMessage_Object = MibTableColumn
cfprCommTelemetryErrorMessage = _CfprCommTelemetryErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 6),
    _CfprCommTelemetryErrorMessage_Type()
)
cfprCommTelemetryErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryErrorMessage.setStatus("current")
_CfprCommTelemetryFltAggr_Type = Unsigned64
_CfprCommTelemetryFltAggr_Object = MibTableColumn
cfprCommTelemetryFltAggr = _CfprCommTelemetryFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 7),
    _CfprCommTelemetryFltAggr_Type()
)
cfprCommTelemetryFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFltAggr.setStatus("current")
_CfprCommTelemetryFsmDescr_Type = SnmpAdminString
_CfprCommTelemetryFsmDescr_Object = MibTableColumn
cfprCommTelemetryFsmDescr = _CfprCommTelemetryFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 8),
    _CfprCommTelemetryFsmDescr_Type()
)
cfprCommTelemetryFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmDescr.setStatus("current")
_CfprCommTelemetryFsmPrev_Type = SnmpAdminString
_CfprCommTelemetryFsmPrev_Object = MibTableColumn
cfprCommTelemetryFsmPrev = _CfprCommTelemetryFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 9),
    _CfprCommTelemetryFsmPrev_Type()
)
cfprCommTelemetryFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmPrev.setStatus("current")
_CfprCommTelemetryFsmProgr_Type = Gauge32
_CfprCommTelemetryFsmProgr_Object = MibTableColumn
cfprCommTelemetryFsmProgr = _CfprCommTelemetryFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 10),
    _CfprCommTelemetryFsmProgr_Type()
)
cfprCommTelemetryFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmProgr.setStatus("current")
_CfprCommTelemetryFsmRmtInvErrCode_Type = Gauge32
_CfprCommTelemetryFsmRmtInvErrCode_Object = MibTableColumn
cfprCommTelemetryFsmRmtInvErrCode = _CfprCommTelemetryFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 11),
    _CfprCommTelemetryFsmRmtInvErrCode_Type()
)
cfprCommTelemetryFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmRmtInvErrCode.setStatus("current")
_CfprCommTelemetryFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprCommTelemetryFsmRmtInvErrDescr_Object = MibTableColumn
cfprCommTelemetryFsmRmtInvErrDescr = _CfprCommTelemetryFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 12),
    _CfprCommTelemetryFsmRmtInvErrDescr_Type()
)
cfprCommTelemetryFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmRmtInvErrDescr.setStatus("current")
_CfprCommTelemetryFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprCommTelemetryFsmRmtInvRslt_Object = MibTableColumn
cfprCommTelemetryFsmRmtInvRslt = _CfprCommTelemetryFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 13),
    _CfprCommTelemetryFsmRmtInvRslt_Type()
)
cfprCommTelemetryFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmRmtInvRslt.setStatus("current")
_CfprCommTelemetryFsmStageDescr_Type = SnmpAdminString
_CfprCommTelemetryFsmStageDescr_Object = MibTableColumn
cfprCommTelemetryFsmStageDescr = _CfprCommTelemetryFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 14),
    _CfprCommTelemetryFsmStageDescr_Type()
)
cfprCommTelemetryFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageDescr.setStatus("current")
_CfprCommTelemetryFsmStamp_Type = DateAndTime
_CfprCommTelemetryFsmStamp_Object = MibTableColumn
cfprCommTelemetryFsmStamp = _CfprCommTelemetryFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 15),
    _CfprCommTelemetryFsmStamp_Type()
)
cfprCommTelemetryFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStamp.setStatus("current")
_CfprCommTelemetryFsmStatus_Type = SnmpAdminString
_CfprCommTelemetryFsmStatus_Object = MibTableColumn
cfprCommTelemetryFsmStatus = _CfprCommTelemetryFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 16),
    _CfprCommTelemetryFsmStatus_Type()
)
cfprCommTelemetryFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStatus.setStatus("current")
_CfprCommTelemetryFsmTry_Type = Gauge32
_CfprCommTelemetryFsmTry_Object = MibTableColumn
cfprCommTelemetryFsmTry = _CfprCommTelemetryFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 17),
    _CfprCommTelemetryFsmTry_Type()
)
cfprCommTelemetryFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTry.setStatus("current")
_CfprCommTelemetryOperState_Type = CfprCommTelemetryOperState
_CfprCommTelemetryOperState_Object = MibTableColumn
cfprCommTelemetryOperState = _CfprCommTelemetryOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 18),
    _CfprCommTelemetryOperState_Type()
)
cfprCommTelemetryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryOperState.setStatus("current")
_CfprCommTelemetryPeriod_Type = Gauge32
_CfprCommTelemetryPeriod_Object = MibTableColumn
cfprCommTelemetryPeriod = _CfprCommTelemetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 39, 1, 19),
    _CfprCommTelemetryPeriod_Type()
)
cfprCommTelemetryPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryPeriod.setStatus("current")
_CfprCommTelemetryFsmTable_Object = MibTable
cfprCommTelemetryFsmTable = _CfprCommTelemetryFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40)
)
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTable.setStatus("current")
_CfprCommTelemetryFsmEntry_Object = MibTableRow
cfprCommTelemetryFsmEntry = _CfprCommTelemetryFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1)
)
cfprCommTelemetryFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommTelemetryFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmEntry.setStatus("current")
_CfprCommTelemetryFsmInstanceId_Type = CfprManagedObjectId
_CfprCommTelemetryFsmInstanceId_Object = MibTableColumn
cfprCommTelemetryFsmInstanceId = _CfprCommTelemetryFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 1),
    _CfprCommTelemetryFsmInstanceId_Type()
)
cfprCommTelemetryFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmInstanceId.setStatus("current")
_CfprCommTelemetryFsmDn_Type = CfprManagedObjectDn
_CfprCommTelemetryFsmDn_Object = MibTableColumn
cfprCommTelemetryFsmDn = _CfprCommTelemetryFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 2),
    _CfprCommTelemetryFsmDn_Type()
)
cfprCommTelemetryFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmDn.setStatus("current")
_CfprCommTelemetryFsmRn_Type = SnmpAdminString
_CfprCommTelemetryFsmRn_Object = MibTableColumn
cfprCommTelemetryFsmRn = _CfprCommTelemetryFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 3),
    _CfprCommTelemetryFsmRn_Type()
)
cfprCommTelemetryFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmRn.setStatus("current")
_CfprCommTelemetryFsmCompletionTime_Type = DateAndTime
_CfprCommTelemetryFsmCompletionTime_Object = MibTableColumn
cfprCommTelemetryFsmCompletionTime = _CfprCommTelemetryFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 4),
    _CfprCommTelemetryFsmCompletionTime_Type()
)
cfprCommTelemetryFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmCompletionTime.setStatus("current")
_CfprCommTelemetryFsmCurrentFsm_Type = CfprCommTelemetryFsmCurrentFsm
_CfprCommTelemetryFsmCurrentFsm_Object = MibTableColumn
cfprCommTelemetryFsmCurrentFsm = _CfprCommTelemetryFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 5),
    _CfprCommTelemetryFsmCurrentFsm_Type()
)
cfprCommTelemetryFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmCurrentFsm.setStatus("current")
_CfprCommTelemetryFsmDescrData_Type = SnmpAdminString
_CfprCommTelemetryFsmDescrData_Object = MibTableColumn
cfprCommTelemetryFsmDescrData = _CfprCommTelemetryFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 6),
    _CfprCommTelemetryFsmDescrData_Type()
)
cfprCommTelemetryFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmDescrData.setStatus("current")
_CfprCommTelemetryFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprCommTelemetryFsmFsmStatus_Object = MibTableColumn
cfprCommTelemetryFsmFsmStatus = _CfprCommTelemetryFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 7),
    _CfprCommTelemetryFsmFsmStatus_Type()
)
cfprCommTelemetryFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmFsmStatus.setStatus("current")
_CfprCommTelemetryFsmProgress_Type = Gauge32
_CfprCommTelemetryFsmProgress_Object = MibTableColumn
cfprCommTelemetryFsmProgress = _CfprCommTelemetryFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 8),
    _CfprCommTelemetryFsmProgress_Type()
)
cfprCommTelemetryFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmProgress.setStatus("current")
_CfprCommTelemetryFsmRmtErrCode_Type = Gauge32
_CfprCommTelemetryFsmRmtErrCode_Object = MibTableColumn
cfprCommTelemetryFsmRmtErrCode = _CfprCommTelemetryFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 9),
    _CfprCommTelemetryFsmRmtErrCode_Type()
)
cfprCommTelemetryFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmRmtErrCode.setStatus("current")
_CfprCommTelemetryFsmRmtErrDescr_Type = SnmpAdminString
_CfprCommTelemetryFsmRmtErrDescr_Object = MibTableColumn
cfprCommTelemetryFsmRmtErrDescr = _CfprCommTelemetryFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 10),
    _CfprCommTelemetryFsmRmtErrDescr_Type()
)
cfprCommTelemetryFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmRmtErrDescr.setStatus("current")
_CfprCommTelemetryFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprCommTelemetryFsmRmtRslt_Object = MibTableColumn
cfprCommTelemetryFsmRmtRslt = _CfprCommTelemetryFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 40, 1, 11),
    _CfprCommTelemetryFsmRmtRslt_Type()
)
cfprCommTelemetryFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmRmtRslt.setStatus("current")
_CfprCommTelemetryFsmStageTable_Object = MibTable
cfprCommTelemetryFsmStageTable = _CfprCommTelemetryFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41)
)
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageTable.setStatus("current")
_CfprCommTelemetryFsmStageEntry_Object = MibTableRow
cfprCommTelemetryFsmStageEntry = _CfprCommTelemetryFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1)
)
cfprCommTelemetryFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommTelemetryFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageEntry.setStatus("current")
_CfprCommTelemetryFsmStageInstanceId_Type = CfprManagedObjectId
_CfprCommTelemetryFsmStageInstanceId_Object = MibTableColumn
cfprCommTelemetryFsmStageInstanceId = _CfprCommTelemetryFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 1),
    _CfprCommTelemetryFsmStageInstanceId_Type()
)
cfprCommTelemetryFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageInstanceId.setStatus("current")
_CfprCommTelemetryFsmStageDn_Type = CfprManagedObjectDn
_CfprCommTelemetryFsmStageDn_Object = MibTableColumn
cfprCommTelemetryFsmStageDn = _CfprCommTelemetryFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 2),
    _CfprCommTelemetryFsmStageDn_Type()
)
cfprCommTelemetryFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageDn.setStatus("current")
_CfprCommTelemetryFsmStageRn_Type = SnmpAdminString
_CfprCommTelemetryFsmStageRn_Object = MibTableColumn
cfprCommTelemetryFsmStageRn = _CfprCommTelemetryFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 3),
    _CfprCommTelemetryFsmStageRn_Type()
)
cfprCommTelemetryFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageRn.setStatus("current")
_CfprCommTelemetryFsmStageDescrData_Type = SnmpAdminString
_CfprCommTelemetryFsmStageDescrData_Object = MibTableColumn
cfprCommTelemetryFsmStageDescrData = _CfprCommTelemetryFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 4),
    _CfprCommTelemetryFsmStageDescrData_Type()
)
cfprCommTelemetryFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageDescrData.setStatus("current")
_CfprCommTelemetryFsmStageLastUpdateTime_Type = DateAndTime
_CfprCommTelemetryFsmStageLastUpdateTime_Object = MibTableColumn
cfprCommTelemetryFsmStageLastUpdateTime = _CfprCommTelemetryFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 5),
    _CfprCommTelemetryFsmStageLastUpdateTime_Type()
)
cfprCommTelemetryFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageLastUpdateTime.setStatus("current")
_CfprCommTelemetryFsmStageName_Type = CfprCommTelemetryFsmStageName
_CfprCommTelemetryFsmStageName_Object = MibTableColumn
cfprCommTelemetryFsmStageName = _CfprCommTelemetryFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 6),
    _CfprCommTelemetryFsmStageName_Type()
)
cfprCommTelemetryFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageName.setStatus("current")
_CfprCommTelemetryFsmStageOrder_Type = Gauge32
_CfprCommTelemetryFsmStageOrder_Object = MibTableColumn
cfprCommTelemetryFsmStageOrder = _CfprCommTelemetryFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 7),
    _CfprCommTelemetryFsmStageOrder_Type()
)
cfprCommTelemetryFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageOrder.setStatus("current")
_CfprCommTelemetryFsmStageRetry_Type = Gauge32
_CfprCommTelemetryFsmStageRetry_Object = MibTableColumn
cfprCommTelemetryFsmStageRetry = _CfprCommTelemetryFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 8),
    _CfprCommTelemetryFsmStageRetry_Type()
)
cfprCommTelemetryFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageRetry.setStatus("current")
_CfprCommTelemetryFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprCommTelemetryFsmStageStageStatus_Object = MibTableColumn
cfprCommTelemetryFsmStageStageStatus = _CfprCommTelemetryFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 41, 1, 9),
    _CfprCommTelemetryFsmStageStageStatus_Type()
)
cfprCommTelemetryFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmStageStageStatus.setStatus("current")
_CfprCommTelemetryFsmTaskTable_Object = MibTable
cfprCommTelemetryFsmTaskTable = _CfprCommTelemetryFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42)
)
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskTable.setStatus("current")
_CfprCommTelemetryFsmTaskEntry_Object = MibTableRow
cfprCommTelemetryFsmTaskEntry = _CfprCommTelemetryFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42, 1)
)
cfprCommTelemetryFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMM-MIB", "cfprCommTelemetryFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskEntry.setStatus("current")
_CfprCommTelemetryFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprCommTelemetryFsmTaskInstanceId_Object = MibTableColumn
cfprCommTelemetryFsmTaskInstanceId = _CfprCommTelemetryFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42, 1, 1),
    _CfprCommTelemetryFsmTaskInstanceId_Type()
)
cfprCommTelemetryFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskInstanceId.setStatus("current")
_CfprCommTelemetryFsmTaskDn_Type = CfprManagedObjectDn
_CfprCommTelemetryFsmTaskDn_Object = MibTableColumn
cfprCommTelemetryFsmTaskDn = _CfprCommTelemetryFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42, 1, 2),
    _CfprCommTelemetryFsmTaskDn_Type()
)
cfprCommTelemetryFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskDn.setStatus("current")
_CfprCommTelemetryFsmTaskRn_Type = SnmpAdminString
_CfprCommTelemetryFsmTaskRn_Object = MibTableColumn
cfprCommTelemetryFsmTaskRn = _CfprCommTelemetryFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42, 1, 3),
    _CfprCommTelemetryFsmTaskRn_Type()
)
cfprCommTelemetryFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskRn.setStatus("current")
_CfprCommTelemetryFsmTaskCompletion_Type = CfprFsmCompletion
_CfprCommTelemetryFsmTaskCompletion_Object = MibTableColumn
cfprCommTelemetryFsmTaskCompletion = _CfprCommTelemetryFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42, 1, 4),
    _CfprCommTelemetryFsmTaskCompletion_Type()
)
cfprCommTelemetryFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskCompletion.setStatus("current")
_CfprCommTelemetryFsmTaskFlags_Type = CfprFsmFlags
_CfprCommTelemetryFsmTaskFlags_Object = MibTableColumn
cfprCommTelemetryFsmTaskFlags = _CfprCommTelemetryFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42, 1, 5),
    _CfprCommTelemetryFsmTaskFlags_Type()
)
cfprCommTelemetryFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskFlags.setStatus("current")
_CfprCommTelemetryFsmTaskItem_Type = CfprCommTelemetryFsmTaskItem
_CfprCommTelemetryFsmTaskItem_Object = MibTableColumn
cfprCommTelemetryFsmTaskItem = _CfprCommTelemetryFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42, 1, 6),
    _CfprCommTelemetryFsmTaskItem_Type()
)
cfprCommTelemetryFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskItem.setStatus("current")
_CfprCommTelemetryFsmTaskSeqId_Type = Gauge32
_CfprCommTelemetryFsmTaskSeqId_Object = MibTableColumn
cfprCommTelemetryFsmTaskSeqId = _CfprCommTelemetryFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 11, 42, 1, 7),
    _CfprCommTelemetryFsmTaskSeqId_Type()
)
cfprCommTelemetryFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCommTelemetryFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-COMM-MIB",
    **{"cfprCommObjects": cfprCommObjects,
       "cfprCommDateTimeTable": cfprCommDateTimeTable,
       "cfprCommDateTimeEntry": cfprCommDateTimeEntry,
       "cfprCommDateTimeInstanceId": cfprCommDateTimeInstanceId,
       "cfprCommDateTimeDn": cfprCommDateTimeDn,
       "cfprCommDateTimeRn": cfprCommDateTimeRn,
       "cfprCommDateTimeAdminState": cfprCommDateTimeAdminState,
       "cfprCommDateTimeConfigState": cfprCommDateTimeConfigState,
       "cfprCommDateTimeDate": cfprCommDateTimeDate,
       "cfprCommDateTimeDescr": cfprCommDateTimeDescr,
       "cfprCommDateTimeIntId": cfprCommDateTimeIntId,
       "cfprCommDateTimeName": cfprCommDateTimeName,
       "cfprCommDateTimeOperPort": cfprCommDateTimeOperPort,
       "cfprCommDateTimeOperTimezone": cfprCommDateTimeOperTimezone,
       "cfprCommDateTimePolicyLevel": cfprCommDateTimePolicyLevel,
       "cfprCommDateTimePolicyOwner": cfprCommDateTimePolicyOwner,
       "cfprCommDateTimePort": cfprCommDateTimePort,
       "cfprCommDateTimeProto": cfprCommDateTimeProto,
       "cfprCommDateTimeTimezone": cfprCommDateTimeTimezone,
       "cfprCommDateTimeNtpAuthState": cfprCommDateTimeNtpAuthState,
       "cfprCommDateTimeSysTimeSyncStatus": cfprCommDateTimeSysTimeSyncStatus,
       "cfprCommDnsTable": cfprCommDnsTable,
       "cfprCommDnsEntry": cfprCommDnsEntry,
       "cfprCommDnsInstanceId": cfprCommDnsInstanceId,
       "cfprCommDnsDn": cfprCommDnsDn,
       "cfprCommDnsRn": cfprCommDnsRn,
       "cfprCommDnsAdminState": cfprCommDnsAdminState,
       "cfprCommDnsDescr": cfprCommDnsDescr,
       "cfprCommDnsDomain": cfprCommDnsDomain,
       "cfprCommDnsIntId": cfprCommDnsIntId,
       "cfprCommDnsName": cfprCommDnsName,
       "cfprCommDnsOperPort": cfprCommDnsOperPort,
       "cfprCommDnsPolicyLevel": cfprCommDnsPolicyLevel,
       "cfprCommDnsPolicyOwner": cfprCommDnsPolicyOwner,
       "cfprCommDnsPort": cfprCommDnsPort,
       "cfprCommDnsProto": cfprCommDnsProto,
       "cfprCommDnsProviderTable": cfprCommDnsProviderTable,
       "cfprCommDnsProviderEntry": cfprCommDnsProviderEntry,
       "cfprCommDnsProviderInstanceId": cfprCommDnsProviderInstanceId,
       "cfprCommDnsProviderDn": cfprCommDnsProviderDn,
       "cfprCommDnsProviderRn": cfprCommDnsProviderRn,
       "cfprCommDnsProviderAdminState": cfprCommDnsProviderAdminState,
       "cfprCommDnsProviderDescr": cfprCommDnsProviderDescr,
       "cfprCommDnsProviderHostname": cfprCommDnsProviderHostname,
       "cfprCommDnsProviderName": cfprCommDnsProviderName,
       "cfprCommEvtChannelTable": cfprCommEvtChannelTable,
       "cfprCommEvtChannelEntry": cfprCommEvtChannelEntry,
       "cfprCommEvtChannelInstanceId": cfprCommEvtChannelInstanceId,
       "cfprCommEvtChannelDn": cfprCommEvtChannelDn,
       "cfprCommEvtChannelRn": cfprCommEvtChannelRn,
       "cfprCommEvtChannelChannelState": cfprCommEvtChannelChannelState,
       "cfprCommEvtChannelDescr": cfprCommEvtChannelDescr,
       "cfprCommEvtChannelIntId": cfprCommEvtChannelIntId,
       "cfprCommEvtChannelName": cfprCommEvtChannelName,
       "cfprCommEvtChannelPolicyLevel": cfprCommEvtChannelPolicyLevel,
       "cfprCommEvtChannelPolicyOwner": cfprCommEvtChannelPolicyOwner,
       "cfprCommHttpsTable": cfprCommHttpsTable,
       "cfprCommHttpsEntry": cfprCommHttpsEntry,
       "cfprCommHttpsInstanceId": cfprCommHttpsInstanceId,
       "cfprCommHttpsDn": cfprCommHttpsDn,
       "cfprCommHttpsRn": cfprCommHttpsRn,
       "cfprCommHttpsAdminState": cfprCommHttpsAdminState,
       "cfprCommHttpsCipherSuite": cfprCommHttpsCipherSuite,
       "cfprCommHttpsCipherSuiteMode": cfprCommHttpsCipherSuiteMode,
       "cfprCommHttpsDescr": cfprCommHttpsDescr,
       "cfprCommHttpsIntId": cfprCommHttpsIntId,
       "cfprCommHttpsKeyRing": cfprCommHttpsKeyRing,
       "cfprCommHttpsName": cfprCommHttpsName,
       "cfprCommHttpsOperPort": cfprCommHttpsOperPort,
       "cfprCommHttpsPolicyLevel": cfprCommHttpsPolicyLevel,
       "cfprCommHttpsPolicyOwner": cfprCommHttpsPolicyOwner,
       "cfprCommHttpsPort": cfprCommHttpsPort,
       "cfprCommHttpsProto": cfprCommHttpsProto,
       "cfprCommHttpsAuthType": cfprCommHttpsAuthType,
       "cfprCommHttpsCrlMode": cfprCommHttpsCrlMode,
       "cfprCommHttpsTlsVer": cfprCommHttpsTlsVer,
       "cfprCommNtpProviderTable": cfprCommNtpProviderTable,
       "cfprCommNtpProviderEntry": cfprCommNtpProviderEntry,
       "cfprCommNtpProviderInstanceId": cfprCommNtpProviderInstanceId,
       "cfprCommNtpProviderDn": cfprCommNtpProviderDn,
       "cfprCommNtpProviderRn": cfprCommNtpProviderRn,
       "cfprCommNtpProviderAdminState": cfprCommNtpProviderAdminState,
       "cfprCommNtpProviderDescr": cfprCommNtpProviderDescr,
       "cfprCommNtpProviderHostname": cfprCommNtpProviderHostname,
       "cfprCommNtpProviderName": cfprCommNtpProviderName,
       "cfprCommNtpProviderDynamicIp": cfprCommNtpProviderDynamicIp,
       "cfprCommNtpProviderErrorMsg": cfprCommNtpProviderErrorMsg,
       "cfprCommNtpProviderKeyStringSet": cfprCommNtpProviderKeyStringSet,
       "cfprCommNtpProviderReachability": cfprCommNtpProviderReachability,
       "cfprCommNtpProviderReceivedInvalidNtpStatusCount": cfprCommNtpProviderReceivedInvalidNtpStatusCount,
       "cfprCommNtpProviderSha1KeyId": cfprCommNtpProviderSha1KeyId,
       "cfprCommNtpProviderSha1KeyString": cfprCommNtpProviderSha1KeyString,
       "cfprCommNtpProviderTimeSyncStatus": cfprCommNtpProviderTimeSyncStatus,
       "cfprCommNtpProviderCheckStratum": cfprCommNtpProviderCheckStratum,
       "cfprCommShellSvcLimitsTable": cfprCommShellSvcLimitsTable,
       "cfprCommShellSvcLimitsEntry": cfprCommShellSvcLimitsEntry,
       "cfprCommShellSvcLimitsInstanceId": cfprCommShellSvcLimitsInstanceId,
       "cfprCommShellSvcLimitsDn": cfprCommShellSvcLimitsDn,
       "cfprCommShellSvcLimitsRn": cfprCommShellSvcLimitsRn,
       "cfprCommShellSvcLimitsDescr": cfprCommShellSvcLimitsDescr,
       "cfprCommShellSvcLimitsIntId": cfprCommShellSvcLimitsIntId,
       "cfprCommShellSvcLimitsName": cfprCommShellSvcLimitsName,
       "cfprCommShellSvcLimitsPolicyLevel": cfprCommShellSvcLimitsPolicyLevel,
       "cfprCommShellSvcLimitsPolicyOwner": cfprCommShellSvcLimitsPolicyOwner,
       "cfprCommShellSvcLimitsSessionsPerUser": cfprCommShellSvcLimitsSessionsPerUser,
       "cfprCommShellSvcLimitsTotalSessions": cfprCommShellSvcLimitsTotalSessions,
       "cfprCommSnmpTable": cfprCommSnmpTable,
       "cfprCommSnmpEntry": cfprCommSnmpEntry,
       "cfprCommSnmpInstanceId": cfprCommSnmpInstanceId,
       "cfprCommSnmpDn": cfprCommSnmpDn,
       "cfprCommSnmpRn": cfprCommSnmpRn,
       "cfprCommSnmpAdminState": cfprCommSnmpAdminState,
       "cfprCommSnmpCommunity": cfprCommSnmpCommunity,
       "cfprCommSnmpConfigState": cfprCommSnmpConfigState,
       "cfprCommSnmpDescr": cfprCommSnmpDescr,
       "cfprCommSnmpIntId": cfprCommSnmpIntId,
       "cfprCommSnmpIsSetSnmpSecure": cfprCommSnmpIsSetSnmpSecure,
       "cfprCommSnmpName": cfprCommSnmpName,
       "cfprCommSnmpOperPort": cfprCommSnmpOperPort,
       "cfprCommSnmpPolicyLevel": cfprCommSnmpPolicyLevel,
       "cfprCommSnmpPolicyOwner": cfprCommSnmpPolicyOwner,
       "cfprCommSnmpPort": cfprCommSnmpPort,
       "cfprCommSnmpProto": cfprCommSnmpProto,
       "cfprCommSnmpSysContact": cfprCommSnmpSysContact,
       "cfprCommSnmpSysLocation": cfprCommSnmpSysLocation,
       "cfprCommSnmpAdminAppEnable": cfprCommSnmpAdminAppEnable,
       "cfprCommSnmpAdminAppId": cfprCommSnmpAdminAppId,
       "cfprCommSnmpAdminAppIp": cfprCommSnmpAdminAppIp,
       "cfprCommSnmpAdminAppName": cfprCommSnmpAdminAppName,
       "cfprCommSnmpAdminAppSlot": cfprCommSnmpAdminAppSlot,
       "cfprCommSnmpUnificationDisabled": cfprCommSnmpUnificationDisabled,
       "cfprCommSnmpTrapTable": cfprCommSnmpTrapTable,
       "cfprCommSnmpTrapEntry": cfprCommSnmpTrapEntry,
       "cfprCommSnmpTrapInstanceId": cfprCommSnmpTrapInstanceId,
       "cfprCommSnmpTrapDn": cfprCommSnmpTrapDn,
       "cfprCommSnmpTrapRn": cfprCommSnmpTrapRn,
       "cfprCommSnmpTrapCommunity": cfprCommSnmpTrapCommunity,
       "cfprCommSnmpTrapHostname": cfprCommSnmpTrapHostname,
       "cfprCommSnmpTrapNotificationType": cfprCommSnmpTrapNotificationType,
       "cfprCommSnmpTrapPort": cfprCommSnmpTrapPort,
       "cfprCommSnmpTrapV3Privilege": cfprCommSnmpTrapV3Privilege,
       "cfprCommSnmpTrapVersion": cfprCommSnmpTrapVersion,
       "cfprCommSnmpUserTable": cfprCommSnmpUserTable,
       "cfprCommSnmpUserEntry": cfprCommSnmpUserEntry,
       "cfprCommSnmpUserInstanceId": cfprCommSnmpUserInstanceId,
       "cfprCommSnmpUserDn": cfprCommSnmpUserDn,
       "cfprCommSnmpUserRn": cfprCommSnmpUserRn,
       "cfprCommSnmpUserAuth": cfprCommSnmpUserAuth,
       "cfprCommSnmpUserConfigState": cfprCommSnmpUserConfigState,
       "cfprCommSnmpUserConfigStatusMessage": cfprCommSnmpUserConfigStatusMessage,
       "cfprCommSnmpUserDescr": cfprCommSnmpUserDescr,
       "cfprCommSnmpUserName": cfprCommSnmpUserName,
       "cfprCommSnmpUserPrivPwdSet": cfprCommSnmpUserPrivPwdSet,
       "cfprCommSnmpUserPrivpwd": cfprCommSnmpUserPrivpwd,
       "cfprCommSnmpUserPwd": cfprCommSnmpUserPwd,
       "cfprCommSnmpUserPwdSet": cfprCommSnmpUserPwdSet,
       "cfprCommSnmpUserUseAes": cfprCommSnmpUserUseAes,
       "cfprCommSshTable": cfprCommSshTable,
       "cfprCommSshEntry": cfprCommSshEntry,
       "cfprCommSshInstanceId": cfprCommSshInstanceId,
       "cfprCommSshDn": cfprCommSshDn,
       "cfprCommSshRn": cfprCommSshRn,
       "cfprCommSshAdminState": cfprCommSshAdminState,
       "cfprCommSshDescr": cfprCommSshDescr,
       "cfprCommSshIntId": cfprCommSshIntId,
       "cfprCommSshName": cfprCommSshName,
       "cfprCommSshOperPort": cfprCommSshOperPort,
       "cfprCommSshPolicyLevel": cfprCommSshPolicyLevel,
       "cfprCommSshPolicyOwner": cfprCommSshPolicyOwner,
       "cfprCommSshPort": cfprCommSshPort,
       "cfprCommSshProto": cfprCommSshProto,
       "cfprCommSshAuthAlgo": cfprCommSshAuthAlgo,
       "cfprCommSshEncryptAlgo": cfprCommSshEncryptAlgo,
       "cfprCommSshHostKey": cfprCommSshHostKey,
       "cfprCommSshHostKeyDeleted": cfprCommSshHostKeyDeleted,
       "cfprCommSshKexAlgo": cfprCommSshKexAlgo,
       "cfprCommSshMacAlgo": cfprCommSshMacAlgo,
       "cfprCommSshSshFlag": cfprCommSshSshFlag,
       "cfprCommSshTime": cfprCommSshTime,
       "cfprCommSshVolume": cfprCommSshVolume,
       "cfprCommSshHostKeyDeletedEcdsa": cfprCommSshHostKeyDeletedEcdsa,
       "cfprCommSshHostKeyEcdsa": cfprCommSshHostKeyEcdsa,
       "cfprCommSvcEpTable": cfprCommSvcEpTable,
       "cfprCommSvcEpEntry": cfprCommSvcEpEntry,
       "cfprCommSvcEpInstanceId": cfprCommSvcEpInstanceId,
       "cfprCommSvcEpDn": cfprCommSvcEpDn,
       "cfprCommSvcEpRn": cfprCommSvcEpRn,
       "cfprCommSvcEpConfigState": cfprCommSvcEpConfigState,
       "cfprCommSvcEpConfigStatusMessage": cfprCommSvcEpConfigStatusMessage,
       "cfprCommSvcEpDescr": cfprCommSvcEpDescr,
       "cfprCommSvcEpFsmDescr": cfprCommSvcEpFsmDescr,
       "cfprCommSvcEpFsmFlags": cfprCommSvcEpFsmFlags,
       "cfprCommSvcEpFsmPrev": cfprCommSvcEpFsmPrev,
       "cfprCommSvcEpFsmProgr": cfprCommSvcEpFsmProgr,
       "cfprCommSvcEpFsmRmtInvErrCode": cfprCommSvcEpFsmRmtInvErrCode,
       "cfprCommSvcEpFsmRmtInvErrDescr": cfprCommSvcEpFsmRmtInvErrDescr,
       "cfprCommSvcEpFsmRmtInvRslt": cfprCommSvcEpFsmRmtInvRslt,
       "cfprCommSvcEpFsmStageDescr": cfprCommSvcEpFsmStageDescr,
       "cfprCommSvcEpFsmStamp": cfprCommSvcEpFsmStamp,
       "cfprCommSvcEpFsmStatus": cfprCommSvcEpFsmStatus,
       "cfprCommSvcEpFsmTry": cfprCommSvcEpFsmTry,
       "cfprCommSvcEpIntId": cfprCommSvcEpIntId,
       "cfprCommSvcEpName": cfprCommSvcEpName,
       "cfprCommSvcEpPolicyLevel": cfprCommSvcEpPolicyLevel,
       "cfprCommSvcEpPolicyOwner": cfprCommSvcEpPolicyOwner,
       "cfprCommSvcEpHttpsIpBlockCount": cfprCommSvcEpHttpsIpBlockCount,
       "cfprCommSvcEpHttpsIpv6BlockCount": cfprCommSvcEpHttpsIpv6BlockCount,
       "cfprCommSvcEpSnmpIpBlockCount": cfprCommSvcEpSnmpIpBlockCount,
       "cfprCommSvcEpSnmpIpv6BlockCount": cfprCommSvcEpSnmpIpv6BlockCount,
       "cfprCommSvcEpSshIpBlockCount": cfprCommSvcEpSshIpBlockCount,
       "cfprCommSvcEpSshIpv6BlockCount": cfprCommSvcEpSshIpv6BlockCount,
       "cfprCommSvcEpTlsVer": cfprCommSvcEpTlsVer,
       "cfprCommSvcEpFsmTable": cfprCommSvcEpFsmTable,
       "cfprCommSvcEpFsmEntry": cfprCommSvcEpFsmEntry,
       "cfprCommSvcEpFsmInstanceId": cfprCommSvcEpFsmInstanceId,
       "cfprCommSvcEpFsmDn": cfprCommSvcEpFsmDn,
       "cfprCommSvcEpFsmRn": cfprCommSvcEpFsmRn,
       "cfprCommSvcEpFsmCompletionTime": cfprCommSvcEpFsmCompletionTime,
       "cfprCommSvcEpFsmCurrentFsm": cfprCommSvcEpFsmCurrentFsm,
       "cfprCommSvcEpFsmDescrData": cfprCommSvcEpFsmDescrData,
       "cfprCommSvcEpFsmFsmStatus": cfprCommSvcEpFsmFsmStatus,
       "cfprCommSvcEpFsmProgress": cfprCommSvcEpFsmProgress,
       "cfprCommSvcEpFsmRmtErrCode": cfprCommSvcEpFsmRmtErrCode,
       "cfprCommSvcEpFsmRmtErrDescr": cfprCommSvcEpFsmRmtErrDescr,
       "cfprCommSvcEpFsmRmtRslt": cfprCommSvcEpFsmRmtRslt,
       "cfprCommSvcEpFsmStageTable": cfprCommSvcEpFsmStageTable,
       "cfprCommSvcEpFsmStageEntry": cfprCommSvcEpFsmStageEntry,
       "cfprCommSvcEpFsmStageInstanceId": cfprCommSvcEpFsmStageInstanceId,
       "cfprCommSvcEpFsmStageDn": cfprCommSvcEpFsmStageDn,
       "cfprCommSvcEpFsmStageRn": cfprCommSvcEpFsmStageRn,
       "cfprCommSvcEpFsmStageDescrData": cfprCommSvcEpFsmStageDescrData,
       "cfprCommSvcEpFsmStageLastUpdateTime": cfprCommSvcEpFsmStageLastUpdateTime,
       "cfprCommSvcEpFsmStageName": cfprCommSvcEpFsmStageName,
       "cfprCommSvcEpFsmStageOrder": cfprCommSvcEpFsmStageOrder,
       "cfprCommSvcEpFsmStageRetry": cfprCommSvcEpFsmStageRetry,
       "cfprCommSvcEpFsmStageStageStatus": cfprCommSvcEpFsmStageStageStatus,
       "cfprCommSvcEpFsmTaskTable": cfprCommSvcEpFsmTaskTable,
       "cfprCommSvcEpFsmTaskEntry": cfprCommSvcEpFsmTaskEntry,
       "cfprCommSvcEpFsmTaskInstanceId": cfprCommSvcEpFsmTaskInstanceId,
       "cfprCommSvcEpFsmTaskDn": cfprCommSvcEpFsmTaskDn,
       "cfprCommSvcEpFsmTaskRn": cfprCommSvcEpFsmTaskRn,
       "cfprCommSvcEpFsmTaskCompletion": cfprCommSvcEpFsmTaskCompletion,
       "cfprCommSvcEpFsmTaskFlags": cfprCommSvcEpFsmTaskFlags,
       "cfprCommSvcEpFsmTaskItem": cfprCommSvcEpFsmTaskItem,
       "cfprCommSvcEpFsmTaskSeqId": cfprCommSvcEpFsmTaskSeqId,
       "cfprCommSyslogTable": cfprCommSyslogTable,
       "cfprCommSyslogEntry": cfprCommSyslogEntry,
       "cfprCommSyslogInstanceId": cfprCommSyslogInstanceId,
       "cfprCommSyslogDn": cfprCommSyslogDn,
       "cfprCommSyslogRn": cfprCommSyslogRn,
       "cfprCommSyslogAdminState": cfprCommSyslogAdminState,
       "cfprCommSyslogDescr": cfprCommSyslogDescr,
       "cfprCommSyslogIntId": cfprCommSyslogIntId,
       "cfprCommSyslogName": cfprCommSyslogName,
       "cfprCommSyslogOperPort": cfprCommSyslogOperPort,
       "cfprCommSyslogPolicyLevel": cfprCommSyslogPolicyLevel,
       "cfprCommSyslogPolicyOwner": cfprCommSyslogPolicyOwner,
       "cfprCommSyslogPort": cfprCommSyslogPort,
       "cfprCommSyslogProto": cfprCommSyslogProto,
       "cfprCommSyslogSeverity": cfprCommSyslogSeverity,
       "cfprCommSyslogClientTable": cfprCommSyslogClientTable,
       "cfprCommSyslogClientEntry": cfprCommSyslogClientEntry,
       "cfprCommSyslogClientInstanceId": cfprCommSyslogClientInstanceId,
       "cfprCommSyslogClientDn": cfprCommSyslogClientDn,
       "cfprCommSyslogClientRn": cfprCommSyslogClientRn,
       "cfprCommSyslogClientAdminState": cfprCommSyslogClientAdminState,
       "cfprCommSyslogClientForwardingFacility": cfprCommSyslogClientForwardingFacility,
       "cfprCommSyslogClientHostname": cfprCommSyslogClientHostname,
       "cfprCommSyslogClientName": cfprCommSyslogClientName,
       "cfprCommSyslogClientSeverity": cfprCommSyslogClientSeverity,
       "cfprCommSyslogConsoleTable": cfprCommSyslogConsoleTable,
       "cfprCommSyslogConsoleEntry": cfprCommSyslogConsoleEntry,
       "cfprCommSyslogConsoleInstanceId": cfprCommSyslogConsoleInstanceId,
       "cfprCommSyslogConsoleDn": cfprCommSyslogConsoleDn,
       "cfprCommSyslogConsoleRn": cfprCommSyslogConsoleRn,
       "cfprCommSyslogConsoleAdminState": cfprCommSyslogConsoleAdminState,
       "cfprCommSyslogConsoleDescr": cfprCommSyslogConsoleDescr,
       "cfprCommSyslogConsoleName": cfprCommSyslogConsoleName,
       "cfprCommSyslogConsoleSeverity": cfprCommSyslogConsoleSeverity,
       "cfprCommSyslogFileTable": cfprCommSyslogFileTable,
       "cfprCommSyslogFileEntry": cfprCommSyslogFileEntry,
       "cfprCommSyslogFileInstanceId": cfprCommSyslogFileInstanceId,
       "cfprCommSyslogFileDn": cfprCommSyslogFileDn,
       "cfprCommSyslogFileRn": cfprCommSyslogFileRn,
       "cfprCommSyslogFileAdminState": cfprCommSyslogFileAdminState,
       "cfprCommSyslogFileDescr": cfprCommSyslogFileDescr,
       "cfprCommSyslogFileName": cfprCommSyslogFileName,
       "cfprCommSyslogFileSeverity": cfprCommSyslogFileSeverity,
       "cfprCommSyslogFileSize": cfprCommSyslogFileSize,
       "cfprCommSyslogMonitorTable": cfprCommSyslogMonitorTable,
       "cfprCommSyslogMonitorEntry": cfprCommSyslogMonitorEntry,
       "cfprCommSyslogMonitorInstanceId": cfprCommSyslogMonitorInstanceId,
       "cfprCommSyslogMonitorDn": cfprCommSyslogMonitorDn,
       "cfprCommSyslogMonitorRn": cfprCommSyslogMonitorRn,
       "cfprCommSyslogMonitorAdminState": cfprCommSyslogMonitorAdminState,
       "cfprCommSyslogMonitorDescr": cfprCommSyslogMonitorDescr,
       "cfprCommSyslogMonitorName": cfprCommSyslogMonitorName,
       "cfprCommSyslogMonitorSeverity": cfprCommSyslogMonitorSeverity,
       "cfprCommSyslogSourceTable": cfprCommSyslogSourceTable,
       "cfprCommSyslogSourceEntry": cfprCommSyslogSourceEntry,
       "cfprCommSyslogSourceInstanceId": cfprCommSyslogSourceInstanceId,
       "cfprCommSyslogSourceDn": cfprCommSyslogSourceDn,
       "cfprCommSyslogSourceRn": cfprCommSyslogSourceRn,
       "cfprCommSyslogSourceAudits": cfprCommSyslogSourceAudits,
       "cfprCommSyslogSourceDescr": cfprCommSyslogSourceDescr,
       "cfprCommSyslogSourceEvents": cfprCommSyslogSourceEvents,
       "cfprCommSyslogSourceFaults": cfprCommSyslogSourceFaults,
       "cfprCommSyslogSourceName": cfprCommSyslogSourceName,
       "cfprCommTelnetTable": cfprCommTelnetTable,
       "cfprCommTelnetEntry": cfprCommTelnetEntry,
       "cfprCommTelnetInstanceId": cfprCommTelnetInstanceId,
       "cfprCommTelnetDn": cfprCommTelnetDn,
       "cfprCommTelnetRn": cfprCommTelnetRn,
       "cfprCommTelnetAdminState": cfprCommTelnetAdminState,
       "cfprCommTelnetDescr": cfprCommTelnetDescr,
       "cfprCommTelnetIntId": cfprCommTelnetIntId,
       "cfprCommTelnetName": cfprCommTelnetName,
       "cfprCommTelnetOperPort": cfprCommTelnetOperPort,
       "cfprCommTelnetPolicyLevel": cfprCommTelnetPolicyLevel,
       "cfprCommTelnetPolicyOwner": cfprCommTelnetPolicyOwner,
       "cfprCommTelnetPort": cfprCommTelnetPort,
       "cfprCommTelnetProto": cfprCommTelnetProto,
       "cfprCommWebChannelTable": cfprCommWebChannelTable,
       "cfprCommWebChannelEntry": cfprCommWebChannelEntry,
       "cfprCommWebChannelInstanceId": cfprCommWebChannelInstanceId,
       "cfprCommWebChannelDn": cfprCommWebChannelDn,
       "cfprCommWebChannelRn": cfprCommWebChannelRn,
       "cfprCommWebChannelChannelState": cfprCommWebChannelChannelState,
       "cfprCommWebChannelDescr": cfprCommWebChannelDescr,
       "cfprCommWebChannelIntId": cfprCommWebChannelIntId,
       "cfprCommWebChannelName": cfprCommWebChannelName,
       "cfprCommWebChannelPolicyLevel": cfprCommWebChannelPolicyLevel,
       "cfprCommWebChannelPolicyOwner": cfprCommWebChannelPolicyOwner,
       "cfprCommWebSvcLimitsTable": cfprCommWebSvcLimitsTable,
       "cfprCommWebSvcLimitsEntry": cfprCommWebSvcLimitsEntry,
       "cfprCommWebSvcLimitsInstanceId": cfprCommWebSvcLimitsInstanceId,
       "cfprCommWebSvcLimitsDn": cfprCommWebSvcLimitsDn,
       "cfprCommWebSvcLimitsRn": cfprCommWebSvcLimitsRn,
       "cfprCommWebSvcLimitsDescr": cfprCommWebSvcLimitsDescr,
       "cfprCommWebSvcLimitsIntId": cfprCommWebSvcLimitsIntId,
       "cfprCommWebSvcLimitsName": cfprCommWebSvcLimitsName,
       "cfprCommWebSvcLimitsPolicyLevel": cfprCommWebSvcLimitsPolicyLevel,
       "cfprCommWebSvcLimitsPolicyOwner": cfprCommWebSvcLimitsPolicyOwner,
       "cfprCommWebSvcLimitsSessionsPerUser": cfprCommWebSvcLimitsSessionsPerUser,
       "cfprCommWebSvcLimitsTotalSessions": cfprCommWebSvcLimitsTotalSessions,
       "cfprCommWsmanTable": cfprCommWsmanTable,
       "cfprCommWsmanEntry": cfprCommWsmanEntry,
       "cfprCommWsmanInstanceId": cfprCommWsmanInstanceId,
       "cfprCommWsmanDn": cfprCommWsmanDn,
       "cfprCommWsmanRn": cfprCommWsmanRn,
       "cfprCommWsmanAdminState": cfprCommWsmanAdminState,
       "cfprCommWsmanDescr": cfprCommWsmanDescr,
       "cfprCommWsmanIntId": cfprCommWsmanIntId,
       "cfprCommWsmanName": cfprCommWsmanName,
       "cfprCommWsmanOperPort": cfprCommWsmanOperPort,
       "cfprCommWsmanPolicyLevel": cfprCommWsmanPolicyLevel,
       "cfprCommWsmanPolicyOwner": cfprCommWsmanPolicyOwner,
       "cfprCommWsmanPort": cfprCommWsmanPort,
       "cfprCommWsmanProto": cfprCommWsmanProto,
       "cfprCommFipsConfigTable": cfprCommFipsConfigTable,
       "cfprCommFipsConfigEntry": cfprCommFipsConfigEntry,
       "cfprCommFipsConfigInstanceId": cfprCommFipsConfigInstanceId,
       "cfprCommFipsConfigDn": cfprCommFipsConfigDn,
       "cfprCommFipsConfigRn": cfprCommFipsConfigRn,
       "cfprCommFipsConfigCcAdminState": cfprCommFipsConfigCcAdminState,
       "cfprCommFipsConfigCcOperState": cfprCommFipsConfigCcOperState,
       "cfprCommFipsConfigDescr": cfprCommFipsConfigDescr,
       "cfprCommFipsConfigFipsAdminState": cfprCommFipsConfigFipsAdminState,
       "cfprCommFipsConfigFipsOperState": cfprCommFipsConfigFipsOperState,
       "cfprCommFipsConfigModeFlag": cfprCommFipsConfigModeFlag,
       "cfprCommFipsConfigName": cfprCommFipsConfigName,
       "cfprCommFipsConfigRebootState": cfprCommFipsConfigRebootState,
       "cfprCommIPv6BlockTable": cfprCommIPv6BlockTable,
       "cfprCommIPv6BlockEntry": cfprCommIPv6BlockEntry,
       "cfprCommIPv6BlockInstanceId": cfprCommIPv6BlockInstanceId,
       "cfprCommIPv6BlockDn": cfprCommIPv6BlockDn,
       "cfprCommIPv6BlockRn": cfprCommIPv6BlockRn,
       "cfprCommIPv6BlockIpAddress": cfprCommIPv6BlockIpAddress,
       "cfprCommIPv6BlockPrefixLength": cfprCommIPv6BlockPrefixLength,
       "cfprCommIPv6BlockProtocol": cfprCommIPv6BlockProtocol,
       "cfprCommIpBlockTable": cfprCommIpBlockTable,
       "cfprCommIpBlockEntry": cfprCommIpBlockEntry,
       "cfprCommIpBlockInstanceId": cfprCommIpBlockInstanceId,
       "cfprCommIpBlockDn": cfprCommIpBlockDn,
       "cfprCommIpBlockRn": cfprCommIpBlockRn,
       "cfprCommIpBlockIpAddress": cfprCommIpBlockIpAddress,
       "cfprCommIpBlockPrefixLength": cfprCommIpBlockPrefixLength,
       "cfprCommIpBlockProtocol": cfprCommIpBlockProtocol,
       "cfprCommSshPubkeyTable": cfprCommSshPubkeyTable,
       "cfprCommSshPubkeyEntry": cfprCommSshPubkeyEntry,
       "cfprCommSshPubkeyInstanceId": cfprCommSshPubkeyInstanceId,
       "cfprCommSshPubkeyDn": cfprCommSshPubkeyDn,
       "cfprCommSshPubkeyRn": cfprCommSshPubkeyRn,
       "cfprCommSshPubkeyAdminState": cfprCommSshPubkeyAdminState,
       "cfprCommSshPubkeyDescr": cfprCommSshPubkeyDescr,
       "cfprCommSshPubkeyIntId": cfprCommSshPubkeyIntId,
       "cfprCommSshPubkeyName": cfprCommSshPubkeyName,
       "cfprCommSshPubkeyOperPort": cfprCommSshPubkeyOperPort,
       "cfprCommSshPubkeyPolicyLevel": cfprCommSshPubkeyPolicyLevel,
       "cfprCommSshPubkeyPolicyOwner": cfprCommSshPubkeyPolicyOwner,
       "cfprCommSshPubkeyPort": cfprCommSshPubkeyPort,
       "cfprCommSshPubkeyProto": cfprCommSshPubkeyProto,
       "cfprCommSshPubkeyChainTable": cfprCommSshPubkeyChainTable,
       "cfprCommSshPubkeyChainEntry": cfprCommSshPubkeyChainEntry,
       "cfprCommSshPubkeyChainInstanceId": cfprCommSshPubkeyChainInstanceId,
       "cfprCommSshPubkeyChainDn": cfprCommSshPubkeyChainDn,
       "cfprCommSshPubkeyChainRn": cfprCommSshPubkeyChainRn,
       "cfprCommSshPubkeyChainAdminState": cfprCommSshPubkeyChainAdminState,
       "cfprCommSshPubkeyChainDescr": cfprCommSshPubkeyChainDescr,
       "cfprCommSshPubkeyChainHostname": cfprCommSshPubkeyChainHostname,
       "cfprCommSshPubkeyChainKeyString": cfprCommSshPubkeyChainKeyString,
       "cfprCommSshPubkeyChainName": cfprCommSshPubkeyChainName,
       "cfprCommSshPubkeyChainServer": cfprCommSshPubkeyChainServer,
       "cfprCommSshcTable": cfprCommSshcTable,
       "cfprCommSshcEntry": cfprCommSshcEntry,
       "cfprCommSshcInstanceId": cfprCommSshcInstanceId,
       "cfprCommSshcDn": cfprCommSshcDn,
       "cfprCommSshcRn": cfprCommSshcRn,
       "cfprCommSshcAdminState": cfprCommSshcAdminState,
       "cfprCommSshcCliEncryptAlgo": cfprCommSshcCliEncryptAlgo,
       "cfprCommSshcCliKexAlgo": cfprCommSshcCliKexAlgo,
       "cfprCommSshcCliMacAlgo": cfprCommSshcCliMacAlgo,
       "cfprCommSshcDescr": cfprCommSshcDescr,
       "cfprCommSshcHostname": cfprCommSshcHostname,
       "cfprCommSshcName": cfprCommSshcName,
       "cfprCommSshcStrictKeyCheck": cfprCommSshcStrictKeyCheck,
       "cfprCommSshcTime": cfprCommSshcTime,
       "cfprCommSshcVolume": cfprCommSshcVolume,
       "cfprCommSyslogPlatformTable": cfprCommSyslogPlatformTable,
       "cfprCommSyslogPlatformEntry": cfprCommSyslogPlatformEntry,
       "cfprCommSyslogPlatformInstanceId": cfprCommSyslogPlatformInstanceId,
       "cfprCommSyslogPlatformDn": cfprCommSyslogPlatformDn,
       "cfprCommSyslogPlatformRn": cfprCommSyslogPlatformRn,
       "cfprCommSyslogPlatformAdminState": cfprCommSyslogPlatformAdminState,
       "cfprCommSyslogPlatformDescr": cfprCommSyslogPlatformDescr,
       "cfprCommSyslogPlatformName": cfprCommSyslogPlatformName,
       "cfprCommSyslogPlatformSeverity": cfprCommSyslogPlatformSeverity,
       "cfprCommDeviceManagerTable": cfprCommDeviceManagerTable,
       "cfprCommDeviceManagerEntry": cfprCommDeviceManagerEntry,
       "cfprCommDeviceManagerInstanceId": cfprCommDeviceManagerInstanceId,
       "cfprCommDeviceManagerDn": cfprCommDeviceManagerDn,
       "cfprCommDeviceManagerRn": cfprCommDeviceManagerRn,
       "cfprCommDeviceManagerDescr": cfprCommDeviceManagerDescr,
       "cfprCommDeviceManagerDeviceState": cfprCommDeviceManagerDeviceState,
       "cfprCommDeviceManagerErrorMsg": cfprCommDeviceManagerErrorMsg,
       "cfprCommDeviceManagerHostname": cfprCommDeviceManagerHostname,
       "cfprCommDeviceManagerName": cfprCommDeviceManagerName,
       "cfprCommDeviceManagerNatId": cfprCommDeviceManagerNatId,
       "cfprCommDeviceManagerRegKey": cfprCommDeviceManagerRegKey,
       "cfprCommDeviceManagerRegState": cfprCommDeviceManagerRegState,
       "cfprCommTelemetryTable": cfprCommTelemetryTable,
       "cfprCommTelemetryEntry": cfprCommTelemetryEntry,
       "cfprCommTelemetryInstanceId": cfprCommTelemetryInstanceId,
       "cfprCommTelemetryDn": cfprCommTelemetryDn,
       "cfprCommTelemetryRn": cfprCommTelemetryRn,
       "cfprCommTelemetryAdminState": cfprCommTelemetryAdminState,
       "cfprCommTelemetryEnableFlag": cfprCommTelemetryEnableFlag,
       "cfprCommTelemetryErrorMessage": cfprCommTelemetryErrorMessage,
       "cfprCommTelemetryFltAggr": cfprCommTelemetryFltAggr,
       "cfprCommTelemetryFsmDescr": cfprCommTelemetryFsmDescr,
       "cfprCommTelemetryFsmPrev": cfprCommTelemetryFsmPrev,
       "cfprCommTelemetryFsmProgr": cfprCommTelemetryFsmProgr,
       "cfprCommTelemetryFsmRmtInvErrCode": cfprCommTelemetryFsmRmtInvErrCode,
       "cfprCommTelemetryFsmRmtInvErrDescr": cfprCommTelemetryFsmRmtInvErrDescr,
       "cfprCommTelemetryFsmRmtInvRslt": cfprCommTelemetryFsmRmtInvRslt,
       "cfprCommTelemetryFsmStageDescr": cfprCommTelemetryFsmStageDescr,
       "cfprCommTelemetryFsmStamp": cfprCommTelemetryFsmStamp,
       "cfprCommTelemetryFsmStatus": cfprCommTelemetryFsmStatus,
       "cfprCommTelemetryFsmTry": cfprCommTelemetryFsmTry,
       "cfprCommTelemetryOperState": cfprCommTelemetryOperState,
       "cfprCommTelemetryPeriod": cfprCommTelemetryPeriod,
       "cfprCommTelemetryFsmTable": cfprCommTelemetryFsmTable,
       "cfprCommTelemetryFsmEntry": cfprCommTelemetryFsmEntry,
       "cfprCommTelemetryFsmInstanceId": cfprCommTelemetryFsmInstanceId,
       "cfprCommTelemetryFsmDn": cfprCommTelemetryFsmDn,
       "cfprCommTelemetryFsmRn": cfprCommTelemetryFsmRn,
       "cfprCommTelemetryFsmCompletionTime": cfprCommTelemetryFsmCompletionTime,
       "cfprCommTelemetryFsmCurrentFsm": cfprCommTelemetryFsmCurrentFsm,
       "cfprCommTelemetryFsmDescrData": cfprCommTelemetryFsmDescrData,
       "cfprCommTelemetryFsmFsmStatus": cfprCommTelemetryFsmFsmStatus,
       "cfprCommTelemetryFsmProgress": cfprCommTelemetryFsmProgress,
       "cfprCommTelemetryFsmRmtErrCode": cfprCommTelemetryFsmRmtErrCode,
       "cfprCommTelemetryFsmRmtErrDescr": cfprCommTelemetryFsmRmtErrDescr,
       "cfprCommTelemetryFsmRmtRslt": cfprCommTelemetryFsmRmtRslt,
       "cfprCommTelemetryFsmStageTable": cfprCommTelemetryFsmStageTable,
       "cfprCommTelemetryFsmStageEntry": cfprCommTelemetryFsmStageEntry,
       "cfprCommTelemetryFsmStageInstanceId": cfprCommTelemetryFsmStageInstanceId,
       "cfprCommTelemetryFsmStageDn": cfprCommTelemetryFsmStageDn,
       "cfprCommTelemetryFsmStageRn": cfprCommTelemetryFsmStageRn,
       "cfprCommTelemetryFsmStageDescrData": cfprCommTelemetryFsmStageDescrData,
       "cfprCommTelemetryFsmStageLastUpdateTime": cfprCommTelemetryFsmStageLastUpdateTime,
       "cfprCommTelemetryFsmStageName": cfprCommTelemetryFsmStageName,
       "cfprCommTelemetryFsmStageOrder": cfprCommTelemetryFsmStageOrder,
       "cfprCommTelemetryFsmStageRetry": cfprCommTelemetryFsmStageRetry,
       "cfprCommTelemetryFsmStageStageStatus": cfprCommTelemetryFsmStageStageStatus,
       "cfprCommTelemetryFsmTaskTable": cfprCommTelemetryFsmTaskTable,
       "cfprCommTelemetryFsmTaskEntry": cfprCommTelemetryFsmTaskEntry,
       "cfprCommTelemetryFsmTaskInstanceId": cfprCommTelemetryFsmTaskInstanceId,
       "cfprCommTelemetryFsmTaskDn": cfprCommTelemetryFsmTaskDn,
       "cfprCommTelemetryFsmTaskRn": cfprCommTelemetryFsmTaskRn,
       "cfprCommTelemetryFsmTaskCompletion": cfprCommTelemetryFsmTaskCompletion,
       "cfprCommTelemetryFsmTaskFlags": cfprCommTelemetryFsmTaskFlags,
       "cfprCommTelemetryFsmTaskItem": cfprCommTelemetryFsmTaskItem,
       "cfprCommTelemetryFsmTaskSeqId": cfprCommTelemetryFsmTaskSeqId}
)
