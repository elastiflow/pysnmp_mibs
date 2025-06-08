# SNMP MIB module (CISCO-FIREPOWER-AP-COMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-COMM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:13 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApAaaConfigState,
 CfprApCommAdminState,
 CfprApCommChannel,
 CfprApCommCipherSuiteMode,
 CfprApCommDnsProviderAdminState,
 CfprApCommNtpProviderAdminState,
 CfprApCommProtocol,
 CfprApCommShellProto,
 CfprApCommSnmpAuth,
 CfprApCommSnmpConfigState,
 CfprApCommSnmpNotificationType,
 CfprApCommSnmpProto,
 CfprApCommSnmpV3Privilege,
 CfprApCommSnmpVersion,
 CfprApCommSshAdminState,
 CfprApCommSvcEpFsmCurrentFsm,
 CfprApCommSvcEpFsmStageName,
 CfprApCommSvcEpFsmTaskFlags,
 CfprApCommSvcEpFsmTaskItem,
 CfprApCommSyslogAdminState,
 CfprApCommSyslogClientEnum,
 CfprApCommSyslogFileSize,
 CfprApCommSyslogForwardingFacility,
 CfprApCommSyslogProto,
 CfprApCommSyslogRestrictedSeverity,
 CfprApCommSyslogSeverity,
 CfprApCommSyslogSourceAudits,
 CfprApCommSyslogSourceEvents,
 CfprApCommSyslogSourceFaults,
 CfprApCommTimeZoneConfigState,
 CfprApCommWebProto,
 CfprApConditionRemoteInvRslt,
 CfprApFsmCompletion,
 CfprApFsmFsmStageStatus,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAaaConfigState",
    "CfprApCommAdminState",
    "CfprApCommChannel",
    "CfprApCommCipherSuiteMode",
    "CfprApCommDnsProviderAdminState",
    "CfprApCommNtpProviderAdminState",
    "CfprApCommProtocol",
    "CfprApCommShellProto",
    "CfprApCommSnmpAuth",
    "CfprApCommSnmpConfigState",
    "CfprApCommSnmpNotificationType",
    "CfprApCommSnmpProto",
    "CfprApCommSnmpV3Privilege",
    "CfprApCommSnmpVersion",
    "CfprApCommSshAdminState",
    "CfprApCommSvcEpFsmCurrentFsm",
    "CfprApCommSvcEpFsmStageName",
    "CfprApCommSvcEpFsmTaskFlags",
    "CfprApCommSvcEpFsmTaskItem",
    "CfprApCommSyslogAdminState",
    "CfprApCommSyslogClientEnum",
    "CfprApCommSyslogFileSize",
    "CfprApCommSyslogForwardingFacility",
    "CfprApCommSyslogProto",
    "CfprApCommSyslogRestrictedSeverity",
    "CfprApCommSyslogSeverity",
    "CfprApCommSyslogSourceAudits",
    "CfprApCommSyslogSourceEvents",
    "CfprApCommSyslogSourceFaults",
    "CfprApCommTimeZoneConfigState",
    "CfprApCommWebProto",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFsmStageStatus",
    "CfprApPolicyPolicyOwner")

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

cfprApCommObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApCommDateTimeTable_Object = MibTable
cfprApCommDateTimeTable = _CfprApCommDateTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cfprApCommDateTimeTable.setStatus("current")
_CfprApCommDateTimeEntry_Object = MibTableRow
cfprApCommDateTimeEntry = _CfprApCommDateTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1)
)
cfprApCommDateTimeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommDateTimeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommDateTimeEntry.setStatus("current")
_CfprApCommDateTimeInstanceId_Type = CfprApManagedObjectId
_CfprApCommDateTimeInstanceId_Object = MibTableColumn
cfprApCommDateTimeInstanceId = _CfprApCommDateTimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 1),
    _CfprApCommDateTimeInstanceId_Type()
)
cfprApCommDateTimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommDateTimeInstanceId.setStatus("current")
_CfprApCommDateTimeDn_Type = CfprApManagedObjectDn
_CfprApCommDateTimeDn_Object = MibTableColumn
cfprApCommDateTimeDn = _CfprApCommDateTimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 2),
    _CfprApCommDateTimeDn_Type()
)
cfprApCommDateTimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeDn.setStatus("current")
_CfprApCommDateTimeRn_Type = SnmpAdminString
_CfprApCommDateTimeRn_Object = MibTableColumn
cfprApCommDateTimeRn = _CfprApCommDateTimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 3),
    _CfprApCommDateTimeRn_Type()
)
cfprApCommDateTimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeRn.setStatus("current")
_CfprApCommDateTimeAdminState_Type = CfprApCommAdminState
_CfprApCommDateTimeAdminState_Object = MibTableColumn
cfprApCommDateTimeAdminState = _CfprApCommDateTimeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 4),
    _CfprApCommDateTimeAdminState_Type()
)
cfprApCommDateTimeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeAdminState.setStatus("current")
_CfprApCommDateTimeConfigState_Type = CfprApCommTimeZoneConfigState
_CfprApCommDateTimeConfigState_Object = MibTableColumn
cfprApCommDateTimeConfigState = _CfprApCommDateTimeConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 5),
    _CfprApCommDateTimeConfigState_Type()
)
cfprApCommDateTimeConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeConfigState.setStatus("current")
_CfprApCommDateTimeDate_Type = DateAndTime
_CfprApCommDateTimeDate_Object = MibTableColumn
cfprApCommDateTimeDate = _CfprApCommDateTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 6),
    _CfprApCommDateTimeDate_Type()
)
cfprApCommDateTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeDate.setStatus("current")
_CfprApCommDateTimeDescr_Type = SnmpAdminString
_CfprApCommDateTimeDescr_Object = MibTableColumn
cfprApCommDateTimeDescr = _CfprApCommDateTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 7),
    _CfprApCommDateTimeDescr_Type()
)
cfprApCommDateTimeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeDescr.setStatus("current")
_CfprApCommDateTimeIntId_Type = SnmpAdminString
_CfprApCommDateTimeIntId_Object = MibTableColumn
cfprApCommDateTimeIntId = _CfprApCommDateTimeIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 8),
    _CfprApCommDateTimeIntId_Type()
)
cfprApCommDateTimeIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeIntId.setStatus("current")
_CfprApCommDateTimeName_Type = SnmpAdminString
_CfprApCommDateTimeName_Object = MibTableColumn
cfprApCommDateTimeName = _CfprApCommDateTimeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 9),
    _CfprApCommDateTimeName_Type()
)
cfprApCommDateTimeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeName.setStatus("current")
_CfprApCommDateTimeOperPort_Type = Gauge32
_CfprApCommDateTimeOperPort_Object = MibTableColumn
cfprApCommDateTimeOperPort = _CfprApCommDateTimeOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 10),
    _CfprApCommDateTimeOperPort_Type()
)
cfprApCommDateTimeOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeOperPort.setStatus("current")
_CfprApCommDateTimeOperTimezone_Type = SnmpAdminString
_CfprApCommDateTimeOperTimezone_Object = MibTableColumn
cfprApCommDateTimeOperTimezone = _CfprApCommDateTimeOperTimezone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 11),
    _CfprApCommDateTimeOperTimezone_Type()
)
cfprApCommDateTimeOperTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeOperTimezone.setStatus("current")
_CfprApCommDateTimePolicyLevel_Type = Gauge32
_CfprApCommDateTimePolicyLevel_Object = MibTableColumn
cfprApCommDateTimePolicyLevel = _CfprApCommDateTimePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 12),
    _CfprApCommDateTimePolicyLevel_Type()
)
cfprApCommDateTimePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimePolicyLevel.setStatus("current")
_CfprApCommDateTimePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommDateTimePolicyOwner_Object = MibTableColumn
cfprApCommDateTimePolicyOwner = _CfprApCommDateTimePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 13),
    _CfprApCommDateTimePolicyOwner_Type()
)
cfprApCommDateTimePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimePolicyOwner.setStatus("current")
_CfprApCommDateTimePort_Type = Gauge32
_CfprApCommDateTimePort_Object = MibTableColumn
cfprApCommDateTimePort = _CfprApCommDateTimePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 14),
    _CfprApCommDateTimePort_Type()
)
cfprApCommDateTimePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimePort.setStatus("current")
_CfprApCommDateTimeProto_Type = CfprApCommProtocol
_CfprApCommDateTimeProto_Object = MibTableColumn
cfprApCommDateTimeProto = _CfprApCommDateTimeProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 15),
    _CfprApCommDateTimeProto_Type()
)
cfprApCommDateTimeProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeProto.setStatus("current")
_CfprApCommDateTimeTimezone_Type = SnmpAdminString
_CfprApCommDateTimeTimezone_Object = MibTableColumn
cfprApCommDateTimeTimezone = _CfprApCommDateTimeTimezone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 1, 1, 16),
    _CfprApCommDateTimeTimezone_Type()
)
cfprApCommDateTimeTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDateTimeTimezone.setStatus("current")
_CfprApCommDnsTable_Object = MibTable
cfprApCommDnsTable = _CfprApCommDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    cfprApCommDnsTable.setStatus("current")
_CfprApCommDnsEntry_Object = MibTableRow
cfprApCommDnsEntry = _CfprApCommDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1)
)
cfprApCommDnsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommDnsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommDnsEntry.setStatus("current")
_CfprApCommDnsInstanceId_Type = CfprApManagedObjectId
_CfprApCommDnsInstanceId_Object = MibTableColumn
cfprApCommDnsInstanceId = _CfprApCommDnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 1),
    _CfprApCommDnsInstanceId_Type()
)
cfprApCommDnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommDnsInstanceId.setStatus("current")
_CfprApCommDnsDn_Type = CfprApManagedObjectDn
_CfprApCommDnsDn_Object = MibTableColumn
cfprApCommDnsDn = _CfprApCommDnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 2),
    _CfprApCommDnsDn_Type()
)
cfprApCommDnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsDn.setStatus("current")
_CfprApCommDnsRn_Type = SnmpAdminString
_CfprApCommDnsRn_Object = MibTableColumn
cfprApCommDnsRn = _CfprApCommDnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 3),
    _CfprApCommDnsRn_Type()
)
cfprApCommDnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsRn.setStatus("current")
_CfprApCommDnsAdminState_Type = CfprApCommAdminState
_CfprApCommDnsAdminState_Object = MibTableColumn
cfprApCommDnsAdminState = _CfprApCommDnsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 4),
    _CfprApCommDnsAdminState_Type()
)
cfprApCommDnsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsAdminState.setStatus("current")
_CfprApCommDnsDescr_Type = SnmpAdminString
_CfprApCommDnsDescr_Object = MibTableColumn
cfprApCommDnsDescr = _CfprApCommDnsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 5),
    _CfprApCommDnsDescr_Type()
)
cfprApCommDnsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsDescr.setStatus("current")
_CfprApCommDnsDomain_Type = SnmpAdminString
_CfprApCommDnsDomain_Object = MibTableColumn
cfprApCommDnsDomain = _CfprApCommDnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 6),
    _CfprApCommDnsDomain_Type()
)
cfprApCommDnsDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsDomain.setStatus("current")
_CfprApCommDnsIntId_Type = SnmpAdminString
_CfprApCommDnsIntId_Object = MibTableColumn
cfprApCommDnsIntId = _CfprApCommDnsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 7),
    _CfprApCommDnsIntId_Type()
)
cfprApCommDnsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsIntId.setStatus("current")
_CfprApCommDnsName_Type = SnmpAdminString
_CfprApCommDnsName_Object = MibTableColumn
cfprApCommDnsName = _CfprApCommDnsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 8),
    _CfprApCommDnsName_Type()
)
cfprApCommDnsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsName.setStatus("current")
_CfprApCommDnsOperPort_Type = Gauge32
_CfprApCommDnsOperPort_Object = MibTableColumn
cfprApCommDnsOperPort = _CfprApCommDnsOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 9),
    _CfprApCommDnsOperPort_Type()
)
cfprApCommDnsOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsOperPort.setStatus("current")
_CfprApCommDnsPolicyLevel_Type = Gauge32
_CfprApCommDnsPolicyLevel_Object = MibTableColumn
cfprApCommDnsPolicyLevel = _CfprApCommDnsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 10),
    _CfprApCommDnsPolicyLevel_Type()
)
cfprApCommDnsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsPolicyLevel.setStatus("current")
_CfprApCommDnsPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommDnsPolicyOwner_Object = MibTableColumn
cfprApCommDnsPolicyOwner = _CfprApCommDnsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 11),
    _CfprApCommDnsPolicyOwner_Type()
)
cfprApCommDnsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsPolicyOwner.setStatus("current")
_CfprApCommDnsPort_Type = Gauge32
_CfprApCommDnsPort_Object = MibTableColumn
cfprApCommDnsPort = _CfprApCommDnsPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 12),
    _CfprApCommDnsPort_Type()
)
cfprApCommDnsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsPort.setStatus("current")
_CfprApCommDnsProto_Type = CfprApCommProtocol
_CfprApCommDnsProto_Object = MibTableColumn
cfprApCommDnsProto = _CfprApCommDnsProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 2, 1, 13),
    _CfprApCommDnsProto_Type()
)
cfprApCommDnsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsProto.setStatus("current")
_CfprApCommDnsProviderTable_Object = MibTable
cfprApCommDnsProviderTable = _CfprApCommDnsProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3)
)
if mibBuilder.loadTexts:
    cfprApCommDnsProviderTable.setStatus("current")
_CfprApCommDnsProviderEntry_Object = MibTableRow
cfprApCommDnsProviderEntry = _CfprApCommDnsProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3, 1)
)
cfprApCommDnsProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommDnsProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommDnsProviderEntry.setStatus("current")
_CfprApCommDnsProviderInstanceId_Type = CfprApManagedObjectId
_CfprApCommDnsProviderInstanceId_Object = MibTableColumn
cfprApCommDnsProviderInstanceId = _CfprApCommDnsProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3, 1, 1),
    _CfprApCommDnsProviderInstanceId_Type()
)
cfprApCommDnsProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommDnsProviderInstanceId.setStatus("current")
_CfprApCommDnsProviderDn_Type = CfprApManagedObjectDn
_CfprApCommDnsProviderDn_Object = MibTableColumn
cfprApCommDnsProviderDn = _CfprApCommDnsProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3, 1, 2),
    _CfprApCommDnsProviderDn_Type()
)
cfprApCommDnsProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsProviderDn.setStatus("current")
_CfprApCommDnsProviderRn_Type = SnmpAdminString
_CfprApCommDnsProviderRn_Object = MibTableColumn
cfprApCommDnsProviderRn = _CfprApCommDnsProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3, 1, 3),
    _CfprApCommDnsProviderRn_Type()
)
cfprApCommDnsProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsProviderRn.setStatus("current")
_CfprApCommDnsProviderAdminState_Type = CfprApCommDnsProviderAdminState
_CfprApCommDnsProviderAdminState_Object = MibTableColumn
cfprApCommDnsProviderAdminState = _CfprApCommDnsProviderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3, 1, 4),
    _CfprApCommDnsProviderAdminState_Type()
)
cfprApCommDnsProviderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsProviderAdminState.setStatus("current")
_CfprApCommDnsProviderDescr_Type = SnmpAdminString
_CfprApCommDnsProviderDescr_Object = MibTableColumn
cfprApCommDnsProviderDescr = _CfprApCommDnsProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3, 1, 5),
    _CfprApCommDnsProviderDescr_Type()
)
cfprApCommDnsProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsProviderDescr.setStatus("current")
_CfprApCommDnsProviderHostname_Type = SnmpAdminString
_CfprApCommDnsProviderHostname_Object = MibTableColumn
cfprApCommDnsProviderHostname = _CfprApCommDnsProviderHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3, 1, 6),
    _CfprApCommDnsProviderHostname_Type()
)
cfprApCommDnsProviderHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsProviderHostname.setStatus("current")
_CfprApCommDnsProviderName_Type = SnmpAdminString
_CfprApCommDnsProviderName_Object = MibTableColumn
cfprApCommDnsProviderName = _CfprApCommDnsProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 3, 1, 7),
    _CfprApCommDnsProviderName_Type()
)
cfprApCommDnsProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommDnsProviderName.setStatus("current")
_CfprApCommEvtChannelTable_Object = MibTable
cfprApCommEvtChannelTable = _CfprApCommEvtChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4)
)
if mibBuilder.loadTexts:
    cfprApCommEvtChannelTable.setStatus("current")
_CfprApCommEvtChannelEntry_Object = MibTableRow
cfprApCommEvtChannelEntry = _CfprApCommEvtChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1)
)
cfprApCommEvtChannelEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommEvtChannelInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommEvtChannelEntry.setStatus("current")
_CfprApCommEvtChannelInstanceId_Type = CfprApManagedObjectId
_CfprApCommEvtChannelInstanceId_Object = MibTableColumn
cfprApCommEvtChannelInstanceId = _CfprApCommEvtChannelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 1),
    _CfprApCommEvtChannelInstanceId_Type()
)
cfprApCommEvtChannelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelInstanceId.setStatus("current")
_CfprApCommEvtChannelDn_Type = CfprApManagedObjectDn
_CfprApCommEvtChannelDn_Object = MibTableColumn
cfprApCommEvtChannelDn = _CfprApCommEvtChannelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 2),
    _CfprApCommEvtChannelDn_Type()
)
cfprApCommEvtChannelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelDn.setStatus("current")
_CfprApCommEvtChannelRn_Type = SnmpAdminString
_CfprApCommEvtChannelRn_Object = MibTableColumn
cfprApCommEvtChannelRn = _CfprApCommEvtChannelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 3),
    _CfprApCommEvtChannelRn_Type()
)
cfprApCommEvtChannelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelRn.setStatus("current")
_CfprApCommEvtChannelChannelState_Type = CfprApCommChannel
_CfprApCommEvtChannelChannelState_Object = MibTableColumn
cfprApCommEvtChannelChannelState = _CfprApCommEvtChannelChannelState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 4),
    _CfprApCommEvtChannelChannelState_Type()
)
cfprApCommEvtChannelChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelChannelState.setStatus("current")
_CfprApCommEvtChannelDescr_Type = SnmpAdminString
_CfprApCommEvtChannelDescr_Object = MibTableColumn
cfprApCommEvtChannelDescr = _CfprApCommEvtChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 5),
    _CfprApCommEvtChannelDescr_Type()
)
cfprApCommEvtChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelDescr.setStatus("current")
_CfprApCommEvtChannelIntId_Type = SnmpAdminString
_CfprApCommEvtChannelIntId_Object = MibTableColumn
cfprApCommEvtChannelIntId = _CfprApCommEvtChannelIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 6),
    _CfprApCommEvtChannelIntId_Type()
)
cfprApCommEvtChannelIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelIntId.setStatus("current")
_CfprApCommEvtChannelName_Type = SnmpAdminString
_CfprApCommEvtChannelName_Object = MibTableColumn
cfprApCommEvtChannelName = _CfprApCommEvtChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 7),
    _CfprApCommEvtChannelName_Type()
)
cfprApCommEvtChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelName.setStatus("current")
_CfprApCommEvtChannelPolicyLevel_Type = Gauge32
_CfprApCommEvtChannelPolicyLevel_Object = MibTableColumn
cfprApCommEvtChannelPolicyLevel = _CfprApCommEvtChannelPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 8),
    _CfprApCommEvtChannelPolicyLevel_Type()
)
cfprApCommEvtChannelPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelPolicyLevel.setStatus("current")
_CfprApCommEvtChannelPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommEvtChannelPolicyOwner_Object = MibTableColumn
cfprApCommEvtChannelPolicyOwner = _CfprApCommEvtChannelPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 4, 1, 9),
    _CfprApCommEvtChannelPolicyOwner_Type()
)
cfprApCommEvtChannelPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommEvtChannelPolicyOwner.setStatus("current")
_CfprApCommHttpsTable_Object = MibTable
cfprApCommHttpsTable = _CfprApCommHttpsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5)
)
if mibBuilder.loadTexts:
    cfprApCommHttpsTable.setStatus("current")
_CfprApCommHttpsEntry_Object = MibTableRow
cfprApCommHttpsEntry = _CfprApCommHttpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1)
)
cfprApCommHttpsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommHttpsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommHttpsEntry.setStatus("current")
_CfprApCommHttpsInstanceId_Type = CfprApManagedObjectId
_CfprApCommHttpsInstanceId_Object = MibTableColumn
cfprApCommHttpsInstanceId = _CfprApCommHttpsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 1),
    _CfprApCommHttpsInstanceId_Type()
)
cfprApCommHttpsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommHttpsInstanceId.setStatus("current")
_CfprApCommHttpsDn_Type = CfprApManagedObjectDn
_CfprApCommHttpsDn_Object = MibTableColumn
cfprApCommHttpsDn = _CfprApCommHttpsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 2),
    _CfprApCommHttpsDn_Type()
)
cfprApCommHttpsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsDn.setStatus("current")
_CfprApCommHttpsRn_Type = SnmpAdminString
_CfprApCommHttpsRn_Object = MibTableColumn
cfprApCommHttpsRn = _CfprApCommHttpsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 3),
    _CfprApCommHttpsRn_Type()
)
cfprApCommHttpsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsRn.setStatus("current")
_CfprApCommHttpsAdminState_Type = CfprApCommAdminState
_CfprApCommHttpsAdminState_Object = MibTableColumn
cfprApCommHttpsAdminState = _CfprApCommHttpsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 4),
    _CfprApCommHttpsAdminState_Type()
)
cfprApCommHttpsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsAdminState.setStatus("current")
_CfprApCommHttpsCipherSuite_Type = SnmpAdminString
_CfprApCommHttpsCipherSuite_Object = MibTableColumn
cfprApCommHttpsCipherSuite = _CfprApCommHttpsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 5),
    _CfprApCommHttpsCipherSuite_Type()
)
cfprApCommHttpsCipherSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsCipherSuite.setStatus("current")
_CfprApCommHttpsCipherSuiteMode_Type = CfprApCommCipherSuiteMode
_CfprApCommHttpsCipherSuiteMode_Object = MibTableColumn
cfprApCommHttpsCipherSuiteMode = _CfprApCommHttpsCipherSuiteMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 6),
    _CfprApCommHttpsCipherSuiteMode_Type()
)
cfprApCommHttpsCipherSuiteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsCipherSuiteMode.setStatus("current")
_CfprApCommHttpsDescr_Type = SnmpAdminString
_CfprApCommHttpsDescr_Object = MibTableColumn
cfprApCommHttpsDescr = _CfprApCommHttpsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 7),
    _CfprApCommHttpsDescr_Type()
)
cfprApCommHttpsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsDescr.setStatus("current")
_CfprApCommHttpsIntId_Type = SnmpAdminString
_CfprApCommHttpsIntId_Object = MibTableColumn
cfprApCommHttpsIntId = _CfprApCommHttpsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 8),
    _CfprApCommHttpsIntId_Type()
)
cfprApCommHttpsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsIntId.setStatus("current")
_CfprApCommHttpsKeyRing_Type = SnmpAdminString
_CfprApCommHttpsKeyRing_Object = MibTableColumn
cfprApCommHttpsKeyRing = _CfprApCommHttpsKeyRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 9),
    _CfprApCommHttpsKeyRing_Type()
)
cfprApCommHttpsKeyRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsKeyRing.setStatus("current")
_CfprApCommHttpsName_Type = SnmpAdminString
_CfprApCommHttpsName_Object = MibTableColumn
cfprApCommHttpsName = _CfprApCommHttpsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 10),
    _CfprApCommHttpsName_Type()
)
cfprApCommHttpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsName.setStatus("current")
_CfprApCommHttpsOperPort_Type = Gauge32
_CfprApCommHttpsOperPort_Object = MibTableColumn
cfprApCommHttpsOperPort = _CfprApCommHttpsOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 11),
    _CfprApCommHttpsOperPort_Type()
)
cfprApCommHttpsOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsOperPort.setStatus("current")
_CfprApCommHttpsPolicyLevel_Type = Gauge32
_CfprApCommHttpsPolicyLevel_Object = MibTableColumn
cfprApCommHttpsPolicyLevel = _CfprApCommHttpsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 12),
    _CfprApCommHttpsPolicyLevel_Type()
)
cfprApCommHttpsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsPolicyLevel.setStatus("current")
_CfprApCommHttpsPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommHttpsPolicyOwner_Object = MibTableColumn
cfprApCommHttpsPolicyOwner = _CfprApCommHttpsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 13),
    _CfprApCommHttpsPolicyOwner_Type()
)
cfprApCommHttpsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsPolicyOwner.setStatus("current")
_CfprApCommHttpsPort_Type = Gauge32
_CfprApCommHttpsPort_Object = MibTableColumn
cfprApCommHttpsPort = _CfprApCommHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 14),
    _CfprApCommHttpsPort_Type()
)
cfprApCommHttpsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsPort.setStatus("current")
_CfprApCommHttpsProto_Type = CfprApCommWebProto
_CfprApCommHttpsProto_Object = MibTableColumn
cfprApCommHttpsProto = _CfprApCommHttpsProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 5, 1, 15),
    _CfprApCommHttpsProto_Type()
)
cfprApCommHttpsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommHttpsProto.setStatus("current")
_CfprApCommNtpProviderTable_Object = MibTable
cfprApCommNtpProviderTable = _CfprApCommNtpProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6)
)
if mibBuilder.loadTexts:
    cfprApCommNtpProviderTable.setStatus("current")
_CfprApCommNtpProviderEntry_Object = MibTableRow
cfprApCommNtpProviderEntry = _CfprApCommNtpProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6, 1)
)
cfprApCommNtpProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommNtpProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommNtpProviderEntry.setStatus("current")
_CfprApCommNtpProviderInstanceId_Type = CfprApManagedObjectId
_CfprApCommNtpProviderInstanceId_Object = MibTableColumn
cfprApCommNtpProviderInstanceId = _CfprApCommNtpProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6, 1, 1),
    _CfprApCommNtpProviderInstanceId_Type()
)
cfprApCommNtpProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommNtpProviderInstanceId.setStatus("current")
_CfprApCommNtpProviderDn_Type = CfprApManagedObjectDn
_CfprApCommNtpProviderDn_Object = MibTableColumn
cfprApCommNtpProviderDn = _CfprApCommNtpProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6, 1, 2),
    _CfprApCommNtpProviderDn_Type()
)
cfprApCommNtpProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommNtpProviderDn.setStatus("current")
_CfprApCommNtpProviderRn_Type = SnmpAdminString
_CfprApCommNtpProviderRn_Object = MibTableColumn
cfprApCommNtpProviderRn = _CfprApCommNtpProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6, 1, 3),
    _CfprApCommNtpProviderRn_Type()
)
cfprApCommNtpProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommNtpProviderRn.setStatus("current")
_CfprApCommNtpProviderAdminState_Type = CfprApCommNtpProviderAdminState
_CfprApCommNtpProviderAdminState_Object = MibTableColumn
cfprApCommNtpProviderAdminState = _CfprApCommNtpProviderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6, 1, 4),
    _CfprApCommNtpProviderAdminState_Type()
)
cfprApCommNtpProviderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommNtpProviderAdminState.setStatus("current")
_CfprApCommNtpProviderDescr_Type = SnmpAdminString
_CfprApCommNtpProviderDescr_Object = MibTableColumn
cfprApCommNtpProviderDescr = _CfprApCommNtpProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6, 1, 5),
    _CfprApCommNtpProviderDescr_Type()
)
cfprApCommNtpProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommNtpProviderDescr.setStatus("current")
_CfprApCommNtpProviderHostname_Type = SnmpAdminString
_CfprApCommNtpProviderHostname_Object = MibTableColumn
cfprApCommNtpProviderHostname = _CfprApCommNtpProviderHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6, 1, 6),
    _CfprApCommNtpProviderHostname_Type()
)
cfprApCommNtpProviderHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommNtpProviderHostname.setStatus("current")
_CfprApCommNtpProviderName_Type = SnmpAdminString
_CfprApCommNtpProviderName_Object = MibTableColumn
cfprApCommNtpProviderName = _CfprApCommNtpProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 6, 1, 7),
    _CfprApCommNtpProviderName_Type()
)
cfprApCommNtpProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommNtpProviderName.setStatus("current")
_CfprApCommShellSvcLimitsTable_Object = MibTable
cfprApCommShellSvcLimitsTable = _CfprApCommShellSvcLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7)
)
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsTable.setStatus("current")
_CfprApCommShellSvcLimitsEntry_Object = MibTableRow
cfprApCommShellSvcLimitsEntry = _CfprApCommShellSvcLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1)
)
cfprApCommShellSvcLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommShellSvcLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsEntry.setStatus("current")
_CfprApCommShellSvcLimitsInstanceId_Type = CfprApManagedObjectId
_CfprApCommShellSvcLimitsInstanceId_Object = MibTableColumn
cfprApCommShellSvcLimitsInstanceId = _CfprApCommShellSvcLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 1),
    _CfprApCommShellSvcLimitsInstanceId_Type()
)
cfprApCommShellSvcLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsInstanceId.setStatus("current")
_CfprApCommShellSvcLimitsDn_Type = CfprApManagedObjectDn
_CfprApCommShellSvcLimitsDn_Object = MibTableColumn
cfprApCommShellSvcLimitsDn = _CfprApCommShellSvcLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 2),
    _CfprApCommShellSvcLimitsDn_Type()
)
cfprApCommShellSvcLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsDn.setStatus("current")
_CfprApCommShellSvcLimitsRn_Type = SnmpAdminString
_CfprApCommShellSvcLimitsRn_Object = MibTableColumn
cfprApCommShellSvcLimitsRn = _CfprApCommShellSvcLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 3),
    _CfprApCommShellSvcLimitsRn_Type()
)
cfprApCommShellSvcLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsRn.setStatus("current")
_CfprApCommShellSvcLimitsDescr_Type = SnmpAdminString
_CfprApCommShellSvcLimitsDescr_Object = MibTableColumn
cfprApCommShellSvcLimitsDescr = _CfprApCommShellSvcLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 4),
    _CfprApCommShellSvcLimitsDescr_Type()
)
cfprApCommShellSvcLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsDescr.setStatus("current")
_CfprApCommShellSvcLimitsIntId_Type = SnmpAdminString
_CfprApCommShellSvcLimitsIntId_Object = MibTableColumn
cfprApCommShellSvcLimitsIntId = _CfprApCommShellSvcLimitsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 5),
    _CfprApCommShellSvcLimitsIntId_Type()
)
cfprApCommShellSvcLimitsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsIntId.setStatus("current")
_CfprApCommShellSvcLimitsName_Type = SnmpAdminString
_CfprApCommShellSvcLimitsName_Object = MibTableColumn
cfprApCommShellSvcLimitsName = _CfprApCommShellSvcLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 6),
    _CfprApCommShellSvcLimitsName_Type()
)
cfprApCommShellSvcLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsName.setStatus("current")
_CfprApCommShellSvcLimitsPolicyLevel_Type = Gauge32
_CfprApCommShellSvcLimitsPolicyLevel_Object = MibTableColumn
cfprApCommShellSvcLimitsPolicyLevel = _CfprApCommShellSvcLimitsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 7),
    _CfprApCommShellSvcLimitsPolicyLevel_Type()
)
cfprApCommShellSvcLimitsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsPolicyLevel.setStatus("current")
_CfprApCommShellSvcLimitsPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommShellSvcLimitsPolicyOwner_Object = MibTableColumn
cfprApCommShellSvcLimitsPolicyOwner = _CfprApCommShellSvcLimitsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 8),
    _CfprApCommShellSvcLimitsPolicyOwner_Type()
)
cfprApCommShellSvcLimitsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsPolicyOwner.setStatus("current")
_CfprApCommShellSvcLimitsSessionsPerUser_Type = Gauge32
_CfprApCommShellSvcLimitsSessionsPerUser_Object = MibTableColumn
cfprApCommShellSvcLimitsSessionsPerUser = _CfprApCommShellSvcLimitsSessionsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 9),
    _CfprApCommShellSvcLimitsSessionsPerUser_Type()
)
cfprApCommShellSvcLimitsSessionsPerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsSessionsPerUser.setStatus("current")
_CfprApCommShellSvcLimitsTotalSessions_Type = Gauge32
_CfprApCommShellSvcLimitsTotalSessions_Object = MibTableColumn
cfprApCommShellSvcLimitsTotalSessions = _CfprApCommShellSvcLimitsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 7, 1, 10),
    _CfprApCommShellSvcLimitsTotalSessions_Type()
)
cfprApCommShellSvcLimitsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommShellSvcLimitsTotalSessions.setStatus("current")
_CfprApCommSnmpTable_Object = MibTable
cfprApCommSnmpTable = _CfprApCommSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8)
)
if mibBuilder.loadTexts:
    cfprApCommSnmpTable.setStatus("current")
_CfprApCommSnmpEntry_Object = MibTableRow
cfprApCommSnmpEntry = _CfprApCommSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1)
)
cfprApCommSnmpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSnmpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSnmpEntry.setStatus("current")
_CfprApCommSnmpInstanceId_Type = CfprApManagedObjectId
_CfprApCommSnmpInstanceId_Object = MibTableColumn
cfprApCommSnmpInstanceId = _CfprApCommSnmpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 1),
    _CfprApCommSnmpInstanceId_Type()
)
cfprApCommSnmpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSnmpInstanceId.setStatus("current")
_CfprApCommSnmpDn_Type = CfprApManagedObjectDn
_CfprApCommSnmpDn_Object = MibTableColumn
cfprApCommSnmpDn = _CfprApCommSnmpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 2),
    _CfprApCommSnmpDn_Type()
)
cfprApCommSnmpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpDn.setStatus("current")
_CfprApCommSnmpRn_Type = SnmpAdminString
_CfprApCommSnmpRn_Object = MibTableColumn
cfprApCommSnmpRn = _CfprApCommSnmpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 3),
    _CfprApCommSnmpRn_Type()
)
cfprApCommSnmpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpRn.setStatus("current")
_CfprApCommSnmpAdminState_Type = CfprApCommAdminState
_CfprApCommSnmpAdminState_Object = MibTableColumn
cfprApCommSnmpAdminState = _CfprApCommSnmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 4),
    _CfprApCommSnmpAdminState_Type()
)
cfprApCommSnmpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpAdminState.setStatus("current")
_CfprApCommSnmpCommunity_Type = SnmpAdminString
_CfprApCommSnmpCommunity_Object = MibTableColumn
cfprApCommSnmpCommunity = _CfprApCommSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 5),
    _CfprApCommSnmpCommunity_Type()
)
cfprApCommSnmpCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpCommunity.setStatus("current")
_CfprApCommSnmpConfigState_Type = CfprApCommSnmpConfigState
_CfprApCommSnmpConfigState_Object = MibTableColumn
cfprApCommSnmpConfigState = _CfprApCommSnmpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 6),
    _CfprApCommSnmpConfigState_Type()
)
cfprApCommSnmpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpConfigState.setStatus("current")
_CfprApCommSnmpDescr_Type = SnmpAdminString
_CfprApCommSnmpDescr_Object = MibTableColumn
cfprApCommSnmpDescr = _CfprApCommSnmpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 7),
    _CfprApCommSnmpDescr_Type()
)
cfprApCommSnmpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpDescr.setStatus("current")
_CfprApCommSnmpIntId_Type = SnmpAdminString
_CfprApCommSnmpIntId_Object = MibTableColumn
cfprApCommSnmpIntId = _CfprApCommSnmpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 8),
    _CfprApCommSnmpIntId_Type()
)
cfprApCommSnmpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpIntId.setStatus("current")
_CfprApCommSnmpIsSetSnmpSecure_Type = TruthValue
_CfprApCommSnmpIsSetSnmpSecure_Object = MibTableColumn
cfprApCommSnmpIsSetSnmpSecure = _CfprApCommSnmpIsSetSnmpSecure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 9),
    _CfprApCommSnmpIsSetSnmpSecure_Type()
)
cfprApCommSnmpIsSetSnmpSecure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpIsSetSnmpSecure.setStatus("current")
_CfprApCommSnmpName_Type = SnmpAdminString
_CfprApCommSnmpName_Object = MibTableColumn
cfprApCommSnmpName = _CfprApCommSnmpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 10),
    _CfprApCommSnmpName_Type()
)
cfprApCommSnmpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpName.setStatus("current")
_CfprApCommSnmpOperPort_Type = Gauge32
_CfprApCommSnmpOperPort_Object = MibTableColumn
cfprApCommSnmpOperPort = _CfprApCommSnmpOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 11),
    _CfprApCommSnmpOperPort_Type()
)
cfprApCommSnmpOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpOperPort.setStatus("current")
_CfprApCommSnmpPolicyLevel_Type = Gauge32
_CfprApCommSnmpPolicyLevel_Object = MibTableColumn
cfprApCommSnmpPolicyLevel = _CfprApCommSnmpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 12),
    _CfprApCommSnmpPolicyLevel_Type()
)
cfprApCommSnmpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpPolicyLevel.setStatus("current")
_CfprApCommSnmpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommSnmpPolicyOwner_Object = MibTableColumn
cfprApCommSnmpPolicyOwner = _CfprApCommSnmpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 13),
    _CfprApCommSnmpPolicyOwner_Type()
)
cfprApCommSnmpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpPolicyOwner.setStatus("current")
_CfprApCommSnmpPort_Type = Gauge32
_CfprApCommSnmpPort_Object = MibTableColumn
cfprApCommSnmpPort = _CfprApCommSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 14),
    _CfprApCommSnmpPort_Type()
)
cfprApCommSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpPort.setStatus("current")
_CfprApCommSnmpProto_Type = CfprApCommSnmpProto
_CfprApCommSnmpProto_Object = MibTableColumn
cfprApCommSnmpProto = _CfprApCommSnmpProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 15),
    _CfprApCommSnmpProto_Type()
)
cfprApCommSnmpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpProto.setStatus("current")
_CfprApCommSnmpSysContact_Type = SnmpAdminString
_CfprApCommSnmpSysContact_Object = MibTableColumn
cfprApCommSnmpSysContact = _CfprApCommSnmpSysContact_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 16),
    _CfprApCommSnmpSysContact_Type()
)
cfprApCommSnmpSysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpSysContact.setStatus("current")
_CfprApCommSnmpSysLocation_Type = SnmpAdminString
_CfprApCommSnmpSysLocation_Object = MibTableColumn
cfprApCommSnmpSysLocation = _CfprApCommSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 8, 1, 17),
    _CfprApCommSnmpSysLocation_Type()
)
cfprApCommSnmpSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpSysLocation.setStatus("current")
_CfprApCommSnmpTrapTable_Object = MibTable
cfprApCommSnmpTrapTable = _CfprApCommSnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9)
)
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapTable.setStatus("current")
_CfprApCommSnmpTrapEntry_Object = MibTableRow
cfprApCommSnmpTrapEntry = _CfprApCommSnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1)
)
cfprApCommSnmpTrapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSnmpTrapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapEntry.setStatus("current")
_CfprApCommSnmpTrapInstanceId_Type = CfprApManagedObjectId
_CfprApCommSnmpTrapInstanceId_Object = MibTableColumn
cfprApCommSnmpTrapInstanceId = _CfprApCommSnmpTrapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 1),
    _CfprApCommSnmpTrapInstanceId_Type()
)
cfprApCommSnmpTrapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapInstanceId.setStatus("current")
_CfprApCommSnmpTrapDn_Type = CfprApManagedObjectDn
_CfprApCommSnmpTrapDn_Object = MibTableColumn
cfprApCommSnmpTrapDn = _CfprApCommSnmpTrapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 2),
    _CfprApCommSnmpTrapDn_Type()
)
cfprApCommSnmpTrapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapDn.setStatus("current")
_CfprApCommSnmpTrapRn_Type = SnmpAdminString
_CfprApCommSnmpTrapRn_Object = MibTableColumn
cfprApCommSnmpTrapRn = _CfprApCommSnmpTrapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 3),
    _CfprApCommSnmpTrapRn_Type()
)
cfprApCommSnmpTrapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapRn.setStatus("current")
_CfprApCommSnmpTrapCommunity_Type = SnmpAdminString
_CfprApCommSnmpTrapCommunity_Object = MibTableColumn
cfprApCommSnmpTrapCommunity = _CfprApCommSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 4),
    _CfprApCommSnmpTrapCommunity_Type()
)
cfprApCommSnmpTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapCommunity.setStatus("current")
_CfprApCommSnmpTrapHostname_Type = SnmpAdminString
_CfprApCommSnmpTrapHostname_Object = MibTableColumn
cfprApCommSnmpTrapHostname = _CfprApCommSnmpTrapHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 5),
    _CfprApCommSnmpTrapHostname_Type()
)
cfprApCommSnmpTrapHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapHostname.setStatus("current")
_CfprApCommSnmpTrapNotificationType_Type = CfprApCommSnmpNotificationType
_CfprApCommSnmpTrapNotificationType_Object = MibTableColumn
cfprApCommSnmpTrapNotificationType = _CfprApCommSnmpTrapNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 6),
    _CfprApCommSnmpTrapNotificationType_Type()
)
cfprApCommSnmpTrapNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapNotificationType.setStatus("current")
_CfprApCommSnmpTrapPort_Type = Gauge32
_CfprApCommSnmpTrapPort_Object = MibTableColumn
cfprApCommSnmpTrapPort = _CfprApCommSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 7),
    _CfprApCommSnmpTrapPort_Type()
)
cfprApCommSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapPort.setStatus("current")
_CfprApCommSnmpTrapV3Privilege_Type = CfprApCommSnmpV3Privilege
_CfprApCommSnmpTrapV3Privilege_Object = MibTableColumn
cfprApCommSnmpTrapV3Privilege = _CfprApCommSnmpTrapV3Privilege_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 8),
    _CfprApCommSnmpTrapV3Privilege_Type()
)
cfprApCommSnmpTrapV3Privilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapV3Privilege.setStatus("current")
_CfprApCommSnmpTrapVersion_Type = CfprApCommSnmpVersion
_CfprApCommSnmpTrapVersion_Object = MibTableColumn
cfprApCommSnmpTrapVersion = _CfprApCommSnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 9, 1, 9),
    _CfprApCommSnmpTrapVersion_Type()
)
cfprApCommSnmpTrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpTrapVersion.setStatus("current")
_CfprApCommSnmpUserTable_Object = MibTable
cfprApCommSnmpUserTable = _CfprApCommSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10)
)
if mibBuilder.loadTexts:
    cfprApCommSnmpUserTable.setStatus("current")
_CfprApCommSnmpUserEntry_Object = MibTableRow
cfprApCommSnmpUserEntry = _CfprApCommSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1)
)
cfprApCommSnmpUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSnmpUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSnmpUserEntry.setStatus("current")
_CfprApCommSnmpUserInstanceId_Type = CfprApManagedObjectId
_CfprApCommSnmpUserInstanceId_Object = MibTableColumn
cfprApCommSnmpUserInstanceId = _CfprApCommSnmpUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 1),
    _CfprApCommSnmpUserInstanceId_Type()
)
cfprApCommSnmpUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserInstanceId.setStatus("current")
_CfprApCommSnmpUserDn_Type = CfprApManagedObjectDn
_CfprApCommSnmpUserDn_Object = MibTableColumn
cfprApCommSnmpUserDn = _CfprApCommSnmpUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 2),
    _CfprApCommSnmpUserDn_Type()
)
cfprApCommSnmpUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserDn.setStatus("current")
_CfprApCommSnmpUserRn_Type = SnmpAdminString
_CfprApCommSnmpUserRn_Object = MibTableColumn
cfprApCommSnmpUserRn = _CfprApCommSnmpUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 3),
    _CfprApCommSnmpUserRn_Type()
)
cfprApCommSnmpUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserRn.setStatus("current")
_CfprApCommSnmpUserAuth_Type = CfprApCommSnmpAuth
_CfprApCommSnmpUserAuth_Object = MibTableColumn
cfprApCommSnmpUserAuth = _CfprApCommSnmpUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 4),
    _CfprApCommSnmpUserAuth_Type()
)
cfprApCommSnmpUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserAuth.setStatus("current")
_CfprApCommSnmpUserConfigState_Type = CfprApAaaConfigState
_CfprApCommSnmpUserConfigState_Object = MibTableColumn
cfprApCommSnmpUserConfigState = _CfprApCommSnmpUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 5),
    _CfprApCommSnmpUserConfigState_Type()
)
cfprApCommSnmpUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserConfigState.setStatus("current")
_CfprApCommSnmpUserConfigStatusMessage_Type = SnmpAdminString
_CfprApCommSnmpUserConfigStatusMessage_Object = MibTableColumn
cfprApCommSnmpUserConfigStatusMessage = _CfprApCommSnmpUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 6),
    _CfprApCommSnmpUserConfigStatusMessage_Type()
)
cfprApCommSnmpUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserConfigStatusMessage.setStatus("current")
_CfprApCommSnmpUserDescr_Type = SnmpAdminString
_CfprApCommSnmpUserDescr_Object = MibTableColumn
cfprApCommSnmpUserDescr = _CfprApCommSnmpUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 7),
    _CfprApCommSnmpUserDescr_Type()
)
cfprApCommSnmpUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserDescr.setStatus("current")
_CfprApCommSnmpUserName_Type = SnmpAdminString
_CfprApCommSnmpUserName_Object = MibTableColumn
cfprApCommSnmpUserName = _CfprApCommSnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 8),
    _CfprApCommSnmpUserName_Type()
)
cfprApCommSnmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserName.setStatus("current")
_CfprApCommSnmpUserPrivPwdSet_Type = TruthValue
_CfprApCommSnmpUserPrivPwdSet_Object = MibTableColumn
cfprApCommSnmpUserPrivPwdSet = _CfprApCommSnmpUserPrivPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 9),
    _CfprApCommSnmpUserPrivPwdSet_Type()
)
cfprApCommSnmpUserPrivPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserPrivPwdSet.setStatus("current")
_CfprApCommSnmpUserPrivpwd_Type = SnmpAdminString
_CfprApCommSnmpUserPrivpwd_Object = MibTableColumn
cfprApCommSnmpUserPrivpwd = _CfprApCommSnmpUserPrivpwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 10),
    _CfprApCommSnmpUserPrivpwd_Type()
)
cfprApCommSnmpUserPrivpwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserPrivpwd.setStatus("current")
_CfprApCommSnmpUserPwd_Type = SnmpAdminString
_CfprApCommSnmpUserPwd_Object = MibTableColumn
cfprApCommSnmpUserPwd = _CfprApCommSnmpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 11),
    _CfprApCommSnmpUserPwd_Type()
)
cfprApCommSnmpUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserPwd.setStatus("current")
_CfprApCommSnmpUserPwdSet_Type = TruthValue
_CfprApCommSnmpUserPwdSet_Object = MibTableColumn
cfprApCommSnmpUserPwdSet = _CfprApCommSnmpUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 12),
    _CfprApCommSnmpUserPwdSet_Type()
)
cfprApCommSnmpUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserPwdSet.setStatus("current")
_CfprApCommSnmpUserUseAes_Type = TruthValue
_CfprApCommSnmpUserUseAes_Object = MibTableColumn
cfprApCommSnmpUserUseAes = _CfprApCommSnmpUserUseAes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 10, 1, 13),
    _CfprApCommSnmpUserUseAes_Type()
)
cfprApCommSnmpUserUseAes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSnmpUserUseAes.setStatus("current")
_CfprApCommSshTable_Object = MibTable
cfprApCommSshTable = _CfprApCommSshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11)
)
if mibBuilder.loadTexts:
    cfprApCommSshTable.setStatus("current")
_CfprApCommSshEntry_Object = MibTableRow
cfprApCommSshEntry = _CfprApCommSshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1)
)
cfprApCommSshEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSshInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSshEntry.setStatus("current")
_CfprApCommSshInstanceId_Type = CfprApManagedObjectId
_CfprApCommSshInstanceId_Object = MibTableColumn
cfprApCommSshInstanceId = _CfprApCommSshInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 1),
    _CfprApCommSshInstanceId_Type()
)
cfprApCommSshInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSshInstanceId.setStatus("current")
_CfprApCommSshDn_Type = CfprApManagedObjectDn
_CfprApCommSshDn_Object = MibTableColumn
cfprApCommSshDn = _CfprApCommSshDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 2),
    _CfprApCommSshDn_Type()
)
cfprApCommSshDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshDn.setStatus("current")
_CfprApCommSshRn_Type = SnmpAdminString
_CfprApCommSshRn_Object = MibTableColumn
cfprApCommSshRn = _CfprApCommSshRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 3),
    _CfprApCommSshRn_Type()
)
cfprApCommSshRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshRn.setStatus("current")
_CfprApCommSshAdminState_Type = CfprApCommSshAdminState
_CfprApCommSshAdminState_Object = MibTableColumn
cfprApCommSshAdminState = _CfprApCommSshAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 4),
    _CfprApCommSshAdminState_Type()
)
cfprApCommSshAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshAdminState.setStatus("current")
_CfprApCommSshDescr_Type = SnmpAdminString
_CfprApCommSshDescr_Object = MibTableColumn
cfprApCommSshDescr = _CfprApCommSshDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 5),
    _CfprApCommSshDescr_Type()
)
cfprApCommSshDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshDescr.setStatus("current")
_CfprApCommSshIntId_Type = SnmpAdminString
_CfprApCommSshIntId_Object = MibTableColumn
cfprApCommSshIntId = _CfprApCommSshIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 6),
    _CfprApCommSshIntId_Type()
)
cfprApCommSshIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshIntId.setStatus("current")
_CfprApCommSshName_Type = SnmpAdminString
_CfprApCommSshName_Object = MibTableColumn
cfprApCommSshName = _CfprApCommSshName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 7),
    _CfprApCommSshName_Type()
)
cfprApCommSshName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshName.setStatus("current")
_CfprApCommSshOperPort_Type = Gauge32
_CfprApCommSshOperPort_Object = MibTableColumn
cfprApCommSshOperPort = _CfprApCommSshOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 8),
    _CfprApCommSshOperPort_Type()
)
cfprApCommSshOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshOperPort.setStatus("current")
_CfprApCommSshPolicyLevel_Type = Gauge32
_CfprApCommSshPolicyLevel_Object = MibTableColumn
cfprApCommSshPolicyLevel = _CfprApCommSshPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 9),
    _CfprApCommSshPolicyLevel_Type()
)
cfprApCommSshPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshPolicyLevel.setStatus("current")
_CfprApCommSshPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommSshPolicyOwner_Object = MibTableColumn
cfprApCommSshPolicyOwner = _CfprApCommSshPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 10),
    _CfprApCommSshPolicyOwner_Type()
)
cfprApCommSshPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshPolicyOwner.setStatus("current")
_CfprApCommSshPort_Type = Gauge32
_CfprApCommSshPort_Object = MibTableColumn
cfprApCommSshPort = _CfprApCommSshPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 11),
    _CfprApCommSshPort_Type()
)
cfprApCommSshPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshPort.setStatus("current")
_CfprApCommSshProto_Type = CfprApCommShellProto
_CfprApCommSshProto_Object = MibTableColumn
cfprApCommSshProto = _CfprApCommSshProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 11, 1, 12),
    _CfprApCommSshProto_Type()
)
cfprApCommSshProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSshProto.setStatus("current")
_CfprApCommSvcEpTable_Object = MibTable
cfprApCommSvcEpTable = _CfprApCommSvcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12)
)
if mibBuilder.loadTexts:
    cfprApCommSvcEpTable.setStatus("current")
_CfprApCommSvcEpEntry_Object = MibTableRow
cfprApCommSvcEpEntry = _CfprApCommSvcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1)
)
cfprApCommSvcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSvcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSvcEpEntry.setStatus("current")
_CfprApCommSvcEpInstanceId_Type = CfprApManagedObjectId
_CfprApCommSvcEpInstanceId_Object = MibTableColumn
cfprApCommSvcEpInstanceId = _CfprApCommSvcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 1),
    _CfprApCommSvcEpInstanceId_Type()
)
cfprApCommSvcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSvcEpInstanceId.setStatus("current")
_CfprApCommSvcEpDn_Type = CfprApManagedObjectDn
_CfprApCommSvcEpDn_Object = MibTableColumn
cfprApCommSvcEpDn = _CfprApCommSvcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 2),
    _CfprApCommSvcEpDn_Type()
)
cfprApCommSvcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpDn.setStatus("current")
_CfprApCommSvcEpRn_Type = SnmpAdminString
_CfprApCommSvcEpRn_Object = MibTableColumn
cfprApCommSvcEpRn = _CfprApCommSvcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 3),
    _CfprApCommSvcEpRn_Type()
)
cfprApCommSvcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpRn.setStatus("current")
_CfprApCommSvcEpConfigState_Type = CfprApAaaConfigState
_CfprApCommSvcEpConfigState_Object = MibTableColumn
cfprApCommSvcEpConfigState = _CfprApCommSvcEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 4),
    _CfprApCommSvcEpConfigState_Type()
)
cfprApCommSvcEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpConfigState.setStatus("current")
_CfprApCommSvcEpConfigStatusMessage_Type = SnmpAdminString
_CfprApCommSvcEpConfigStatusMessage_Object = MibTableColumn
cfprApCommSvcEpConfigStatusMessage = _CfprApCommSvcEpConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 5),
    _CfprApCommSvcEpConfigStatusMessage_Type()
)
cfprApCommSvcEpConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpConfigStatusMessage.setStatus("current")
_CfprApCommSvcEpDescr_Type = SnmpAdminString
_CfprApCommSvcEpDescr_Object = MibTableColumn
cfprApCommSvcEpDescr = _CfprApCommSvcEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 6),
    _CfprApCommSvcEpDescr_Type()
)
cfprApCommSvcEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpDescr.setStatus("current")
_CfprApCommSvcEpFsmDescr_Type = SnmpAdminString
_CfprApCommSvcEpFsmDescr_Object = MibTableColumn
cfprApCommSvcEpFsmDescr = _CfprApCommSvcEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 7),
    _CfprApCommSvcEpFsmDescr_Type()
)
cfprApCommSvcEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmDescr.setStatus("current")
_CfprApCommSvcEpFsmFlags_Type = SnmpAdminString
_CfprApCommSvcEpFsmFlags_Object = MibTableColumn
cfprApCommSvcEpFsmFlags = _CfprApCommSvcEpFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 8),
    _CfprApCommSvcEpFsmFlags_Type()
)
cfprApCommSvcEpFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmFlags.setStatus("current")
_CfprApCommSvcEpFsmPrev_Type = SnmpAdminString
_CfprApCommSvcEpFsmPrev_Object = MibTableColumn
cfprApCommSvcEpFsmPrev = _CfprApCommSvcEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 9),
    _CfprApCommSvcEpFsmPrev_Type()
)
cfprApCommSvcEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmPrev.setStatus("current")
_CfprApCommSvcEpFsmProgr_Type = Gauge32
_CfprApCommSvcEpFsmProgr_Object = MibTableColumn
cfprApCommSvcEpFsmProgr = _CfprApCommSvcEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 10),
    _CfprApCommSvcEpFsmProgr_Type()
)
cfprApCommSvcEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmProgr.setStatus("current")
_CfprApCommSvcEpFsmRmtInvErrCode_Type = Gauge32
_CfprApCommSvcEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApCommSvcEpFsmRmtInvErrCode = _CfprApCommSvcEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 11),
    _CfprApCommSvcEpFsmRmtInvErrCode_Type()
)
cfprApCommSvcEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmRmtInvErrCode.setStatus("current")
_CfprApCommSvcEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApCommSvcEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApCommSvcEpFsmRmtInvErrDescr = _CfprApCommSvcEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 12),
    _CfprApCommSvcEpFsmRmtInvErrDescr_Type()
)
cfprApCommSvcEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmRmtInvErrDescr.setStatus("current")
_CfprApCommSvcEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCommSvcEpFsmRmtInvRslt_Object = MibTableColumn
cfprApCommSvcEpFsmRmtInvRslt = _CfprApCommSvcEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 13),
    _CfprApCommSvcEpFsmRmtInvRslt_Type()
)
cfprApCommSvcEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmRmtInvRslt.setStatus("current")
_CfprApCommSvcEpFsmStageDescr_Type = SnmpAdminString
_CfprApCommSvcEpFsmStageDescr_Object = MibTableColumn
cfprApCommSvcEpFsmStageDescr = _CfprApCommSvcEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 14),
    _CfprApCommSvcEpFsmStageDescr_Type()
)
cfprApCommSvcEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageDescr.setStatus("current")
_CfprApCommSvcEpFsmStamp_Type = DateAndTime
_CfprApCommSvcEpFsmStamp_Object = MibTableColumn
cfprApCommSvcEpFsmStamp = _CfprApCommSvcEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 15),
    _CfprApCommSvcEpFsmStamp_Type()
)
cfprApCommSvcEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStamp.setStatus("current")
_CfprApCommSvcEpFsmStatus_Type = SnmpAdminString
_CfprApCommSvcEpFsmStatus_Object = MibTableColumn
cfprApCommSvcEpFsmStatus = _CfprApCommSvcEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 16),
    _CfprApCommSvcEpFsmStatus_Type()
)
cfprApCommSvcEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStatus.setStatus("current")
_CfprApCommSvcEpFsmTry_Type = Gauge32
_CfprApCommSvcEpFsmTry_Object = MibTableColumn
cfprApCommSvcEpFsmTry = _CfprApCommSvcEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 17),
    _CfprApCommSvcEpFsmTry_Type()
)
cfprApCommSvcEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTry.setStatus("current")
_CfprApCommSvcEpIntId_Type = SnmpAdminString
_CfprApCommSvcEpIntId_Object = MibTableColumn
cfprApCommSvcEpIntId = _CfprApCommSvcEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 18),
    _CfprApCommSvcEpIntId_Type()
)
cfprApCommSvcEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpIntId.setStatus("current")
_CfprApCommSvcEpName_Type = SnmpAdminString
_CfprApCommSvcEpName_Object = MibTableColumn
cfprApCommSvcEpName = _CfprApCommSvcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 19),
    _CfprApCommSvcEpName_Type()
)
cfprApCommSvcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpName.setStatus("current")
_CfprApCommSvcEpPolicyLevel_Type = Gauge32
_CfprApCommSvcEpPolicyLevel_Object = MibTableColumn
cfprApCommSvcEpPolicyLevel = _CfprApCommSvcEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 20),
    _CfprApCommSvcEpPolicyLevel_Type()
)
cfprApCommSvcEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpPolicyLevel.setStatus("current")
_CfprApCommSvcEpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommSvcEpPolicyOwner_Object = MibTableColumn
cfprApCommSvcEpPolicyOwner = _CfprApCommSvcEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 12, 1, 21),
    _CfprApCommSvcEpPolicyOwner_Type()
)
cfprApCommSvcEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpPolicyOwner.setStatus("current")
_CfprApCommSvcEpFsmTable_Object = MibTable
cfprApCommSvcEpFsmTable = _CfprApCommSvcEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13)
)
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTable.setStatus("current")
_CfprApCommSvcEpFsmEntry_Object = MibTableRow
cfprApCommSvcEpFsmEntry = _CfprApCommSvcEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1)
)
cfprApCommSvcEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSvcEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmEntry.setStatus("current")
_CfprApCommSvcEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApCommSvcEpFsmInstanceId_Object = MibTableColumn
cfprApCommSvcEpFsmInstanceId = _CfprApCommSvcEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 1),
    _CfprApCommSvcEpFsmInstanceId_Type()
)
cfprApCommSvcEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmInstanceId.setStatus("current")
_CfprApCommSvcEpFsmDn_Type = CfprApManagedObjectDn
_CfprApCommSvcEpFsmDn_Object = MibTableColumn
cfprApCommSvcEpFsmDn = _CfprApCommSvcEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 2),
    _CfprApCommSvcEpFsmDn_Type()
)
cfprApCommSvcEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmDn.setStatus("current")
_CfprApCommSvcEpFsmRn_Type = SnmpAdminString
_CfprApCommSvcEpFsmRn_Object = MibTableColumn
cfprApCommSvcEpFsmRn = _CfprApCommSvcEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 3),
    _CfprApCommSvcEpFsmRn_Type()
)
cfprApCommSvcEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmRn.setStatus("current")
_CfprApCommSvcEpFsmCompletionTime_Type = DateAndTime
_CfprApCommSvcEpFsmCompletionTime_Object = MibTableColumn
cfprApCommSvcEpFsmCompletionTime = _CfprApCommSvcEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 4),
    _CfprApCommSvcEpFsmCompletionTime_Type()
)
cfprApCommSvcEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmCompletionTime.setStatus("current")
_CfprApCommSvcEpFsmCurrentFsm_Type = CfprApCommSvcEpFsmCurrentFsm
_CfprApCommSvcEpFsmCurrentFsm_Object = MibTableColumn
cfprApCommSvcEpFsmCurrentFsm = _CfprApCommSvcEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 5),
    _CfprApCommSvcEpFsmCurrentFsm_Type()
)
cfprApCommSvcEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmCurrentFsm.setStatus("current")
_CfprApCommSvcEpFsmDescrData_Type = SnmpAdminString
_CfprApCommSvcEpFsmDescrData_Object = MibTableColumn
cfprApCommSvcEpFsmDescrData = _CfprApCommSvcEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 6),
    _CfprApCommSvcEpFsmDescrData_Type()
)
cfprApCommSvcEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmDescrData.setStatus("current")
_CfprApCommSvcEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApCommSvcEpFsmFsmStatus_Object = MibTableColumn
cfprApCommSvcEpFsmFsmStatus = _CfprApCommSvcEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 7),
    _CfprApCommSvcEpFsmFsmStatus_Type()
)
cfprApCommSvcEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmFsmStatus.setStatus("current")
_CfprApCommSvcEpFsmProgress_Type = Gauge32
_CfprApCommSvcEpFsmProgress_Object = MibTableColumn
cfprApCommSvcEpFsmProgress = _CfprApCommSvcEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 8),
    _CfprApCommSvcEpFsmProgress_Type()
)
cfprApCommSvcEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmProgress.setStatus("current")
_CfprApCommSvcEpFsmRmtErrCode_Type = Gauge32
_CfprApCommSvcEpFsmRmtErrCode_Object = MibTableColumn
cfprApCommSvcEpFsmRmtErrCode = _CfprApCommSvcEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 9),
    _CfprApCommSvcEpFsmRmtErrCode_Type()
)
cfprApCommSvcEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmRmtErrCode.setStatus("current")
_CfprApCommSvcEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApCommSvcEpFsmRmtErrDescr_Object = MibTableColumn
cfprApCommSvcEpFsmRmtErrDescr = _CfprApCommSvcEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 10),
    _CfprApCommSvcEpFsmRmtErrDescr_Type()
)
cfprApCommSvcEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmRmtErrDescr.setStatus("current")
_CfprApCommSvcEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCommSvcEpFsmRmtRslt_Object = MibTableColumn
cfprApCommSvcEpFsmRmtRslt = _CfprApCommSvcEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 13, 1, 11),
    _CfprApCommSvcEpFsmRmtRslt_Type()
)
cfprApCommSvcEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmRmtRslt.setStatus("current")
_CfprApCommSvcEpFsmStageTable_Object = MibTable
cfprApCommSvcEpFsmStageTable = _CfprApCommSvcEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14)
)
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageTable.setStatus("current")
_CfprApCommSvcEpFsmStageEntry_Object = MibTableRow
cfprApCommSvcEpFsmStageEntry = _CfprApCommSvcEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1)
)
cfprApCommSvcEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSvcEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageEntry.setStatus("current")
_CfprApCommSvcEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApCommSvcEpFsmStageInstanceId_Object = MibTableColumn
cfprApCommSvcEpFsmStageInstanceId = _CfprApCommSvcEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 1),
    _CfprApCommSvcEpFsmStageInstanceId_Type()
)
cfprApCommSvcEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageInstanceId.setStatus("current")
_CfprApCommSvcEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApCommSvcEpFsmStageDn_Object = MibTableColumn
cfprApCommSvcEpFsmStageDn = _CfprApCommSvcEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 2),
    _CfprApCommSvcEpFsmStageDn_Type()
)
cfprApCommSvcEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageDn.setStatus("current")
_CfprApCommSvcEpFsmStageRn_Type = SnmpAdminString
_CfprApCommSvcEpFsmStageRn_Object = MibTableColumn
cfprApCommSvcEpFsmStageRn = _CfprApCommSvcEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 3),
    _CfprApCommSvcEpFsmStageRn_Type()
)
cfprApCommSvcEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageRn.setStatus("current")
_CfprApCommSvcEpFsmStageDescrData_Type = SnmpAdminString
_CfprApCommSvcEpFsmStageDescrData_Object = MibTableColumn
cfprApCommSvcEpFsmStageDescrData = _CfprApCommSvcEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 4),
    _CfprApCommSvcEpFsmStageDescrData_Type()
)
cfprApCommSvcEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageDescrData.setStatus("current")
_CfprApCommSvcEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApCommSvcEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApCommSvcEpFsmStageLastUpdateTime = _CfprApCommSvcEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 5),
    _CfprApCommSvcEpFsmStageLastUpdateTime_Type()
)
cfprApCommSvcEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageLastUpdateTime.setStatus("current")
_CfprApCommSvcEpFsmStageName_Type = CfprApCommSvcEpFsmStageName
_CfprApCommSvcEpFsmStageName_Object = MibTableColumn
cfprApCommSvcEpFsmStageName = _CfprApCommSvcEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 6),
    _CfprApCommSvcEpFsmStageName_Type()
)
cfprApCommSvcEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageName.setStatus("current")
_CfprApCommSvcEpFsmStageOrder_Type = Gauge32
_CfprApCommSvcEpFsmStageOrder_Object = MibTableColumn
cfprApCommSvcEpFsmStageOrder = _CfprApCommSvcEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 7),
    _CfprApCommSvcEpFsmStageOrder_Type()
)
cfprApCommSvcEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageOrder.setStatus("current")
_CfprApCommSvcEpFsmStageRetry_Type = Gauge32
_CfprApCommSvcEpFsmStageRetry_Object = MibTableColumn
cfprApCommSvcEpFsmStageRetry = _CfprApCommSvcEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 8),
    _CfprApCommSvcEpFsmStageRetry_Type()
)
cfprApCommSvcEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageRetry.setStatus("current")
_CfprApCommSvcEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApCommSvcEpFsmStageStageStatus_Object = MibTableColumn
cfprApCommSvcEpFsmStageStageStatus = _CfprApCommSvcEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 14, 1, 9),
    _CfprApCommSvcEpFsmStageStageStatus_Type()
)
cfprApCommSvcEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmStageStageStatus.setStatus("current")
_CfprApCommSvcEpFsmTaskTable_Object = MibTable
cfprApCommSvcEpFsmTaskTable = _CfprApCommSvcEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15)
)
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskTable.setStatus("current")
_CfprApCommSvcEpFsmTaskEntry_Object = MibTableRow
cfprApCommSvcEpFsmTaskEntry = _CfprApCommSvcEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15, 1)
)
cfprApCommSvcEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSvcEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskEntry.setStatus("current")
_CfprApCommSvcEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApCommSvcEpFsmTaskInstanceId_Object = MibTableColumn
cfprApCommSvcEpFsmTaskInstanceId = _CfprApCommSvcEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15, 1, 1),
    _CfprApCommSvcEpFsmTaskInstanceId_Type()
)
cfprApCommSvcEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskInstanceId.setStatus("current")
_CfprApCommSvcEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApCommSvcEpFsmTaskDn_Object = MibTableColumn
cfprApCommSvcEpFsmTaskDn = _CfprApCommSvcEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15, 1, 2),
    _CfprApCommSvcEpFsmTaskDn_Type()
)
cfprApCommSvcEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskDn.setStatus("current")
_CfprApCommSvcEpFsmTaskRn_Type = SnmpAdminString
_CfprApCommSvcEpFsmTaskRn_Object = MibTableColumn
cfprApCommSvcEpFsmTaskRn = _CfprApCommSvcEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15, 1, 3),
    _CfprApCommSvcEpFsmTaskRn_Type()
)
cfprApCommSvcEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskRn.setStatus("current")
_CfprApCommSvcEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApCommSvcEpFsmTaskCompletion_Object = MibTableColumn
cfprApCommSvcEpFsmTaskCompletion = _CfprApCommSvcEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15, 1, 4),
    _CfprApCommSvcEpFsmTaskCompletion_Type()
)
cfprApCommSvcEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskCompletion.setStatus("current")
_CfprApCommSvcEpFsmTaskFlags_Type = CfprApCommSvcEpFsmTaskFlags
_CfprApCommSvcEpFsmTaskFlags_Object = MibTableColumn
cfprApCommSvcEpFsmTaskFlags = _CfprApCommSvcEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15, 1, 5),
    _CfprApCommSvcEpFsmTaskFlags_Type()
)
cfprApCommSvcEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskFlags.setStatus("current")
_CfprApCommSvcEpFsmTaskItem_Type = CfprApCommSvcEpFsmTaskItem
_CfprApCommSvcEpFsmTaskItem_Object = MibTableColumn
cfprApCommSvcEpFsmTaskItem = _CfprApCommSvcEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15, 1, 6),
    _CfprApCommSvcEpFsmTaskItem_Type()
)
cfprApCommSvcEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskItem.setStatus("current")
_CfprApCommSvcEpFsmTaskSeqId_Type = Gauge32
_CfprApCommSvcEpFsmTaskSeqId_Object = MibTableColumn
cfprApCommSvcEpFsmTaskSeqId = _CfprApCommSvcEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 15, 1, 7),
    _CfprApCommSvcEpFsmTaskSeqId_Type()
)
cfprApCommSvcEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSvcEpFsmTaskSeqId.setStatus("current")
_CfprApCommSyslogTable_Object = MibTable
cfprApCommSyslogTable = _CfprApCommSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16)
)
if mibBuilder.loadTexts:
    cfprApCommSyslogTable.setStatus("current")
_CfprApCommSyslogEntry_Object = MibTableRow
cfprApCommSyslogEntry = _CfprApCommSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1)
)
cfprApCommSyslogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSyslogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSyslogEntry.setStatus("current")
_CfprApCommSyslogInstanceId_Type = CfprApManagedObjectId
_CfprApCommSyslogInstanceId_Object = MibTableColumn
cfprApCommSyslogInstanceId = _CfprApCommSyslogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 1),
    _CfprApCommSyslogInstanceId_Type()
)
cfprApCommSyslogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSyslogInstanceId.setStatus("current")
_CfprApCommSyslogDn_Type = CfprApManagedObjectDn
_CfprApCommSyslogDn_Object = MibTableColumn
cfprApCommSyslogDn = _CfprApCommSyslogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 2),
    _CfprApCommSyslogDn_Type()
)
cfprApCommSyslogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogDn.setStatus("current")
_CfprApCommSyslogRn_Type = SnmpAdminString
_CfprApCommSyslogRn_Object = MibTableColumn
cfprApCommSyslogRn = _CfprApCommSyslogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 3),
    _CfprApCommSyslogRn_Type()
)
cfprApCommSyslogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogRn.setStatus("current")
_CfprApCommSyslogAdminState_Type = CfprApCommAdminState
_CfprApCommSyslogAdminState_Object = MibTableColumn
cfprApCommSyslogAdminState = _CfprApCommSyslogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 4),
    _CfprApCommSyslogAdminState_Type()
)
cfprApCommSyslogAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogAdminState.setStatus("current")
_CfprApCommSyslogDescr_Type = SnmpAdminString
_CfprApCommSyslogDescr_Object = MibTableColumn
cfprApCommSyslogDescr = _CfprApCommSyslogDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 5),
    _CfprApCommSyslogDescr_Type()
)
cfprApCommSyslogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogDescr.setStatus("current")
_CfprApCommSyslogIntId_Type = SnmpAdminString
_CfprApCommSyslogIntId_Object = MibTableColumn
cfprApCommSyslogIntId = _CfprApCommSyslogIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 6),
    _CfprApCommSyslogIntId_Type()
)
cfprApCommSyslogIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogIntId.setStatus("current")
_CfprApCommSyslogName_Type = SnmpAdminString
_CfprApCommSyslogName_Object = MibTableColumn
cfprApCommSyslogName = _CfprApCommSyslogName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 7),
    _CfprApCommSyslogName_Type()
)
cfprApCommSyslogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogName.setStatus("current")
_CfprApCommSyslogOperPort_Type = Gauge32
_CfprApCommSyslogOperPort_Object = MibTableColumn
cfprApCommSyslogOperPort = _CfprApCommSyslogOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 8),
    _CfprApCommSyslogOperPort_Type()
)
cfprApCommSyslogOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogOperPort.setStatus("current")
_CfprApCommSyslogPolicyLevel_Type = Gauge32
_CfprApCommSyslogPolicyLevel_Object = MibTableColumn
cfprApCommSyslogPolicyLevel = _CfprApCommSyslogPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 9),
    _CfprApCommSyslogPolicyLevel_Type()
)
cfprApCommSyslogPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogPolicyLevel.setStatus("current")
_CfprApCommSyslogPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommSyslogPolicyOwner_Object = MibTableColumn
cfprApCommSyslogPolicyOwner = _CfprApCommSyslogPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 10),
    _CfprApCommSyslogPolicyOwner_Type()
)
cfprApCommSyslogPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogPolicyOwner.setStatus("current")
_CfprApCommSyslogPort_Type = Gauge32
_CfprApCommSyslogPort_Object = MibTableColumn
cfprApCommSyslogPort = _CfprApCommSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 11),
    _CfprApCommSyslogPort_Type()
)
cfprApCommSyslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogPort.setStatus("current")
_CfprApCommSyslogProto_Type = CfprApCommSyslogProto
_CfprApCommSyslogProto_Object = MibTableColumn
cfprApCommSyslogProto = _CfprApCommSyslogProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 12),
    _CfprApCommSyslogProto_Type()
)
cfprApCommSyslogProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogProto.setStatus("current")
_CfprApCommSyslogSeverity_Type = CfprApCommSyslogSeverity
_CfprApCommSyslogSeverity_Object = MibTableColumn
cfprApCommSyslogSeverity = _CfprApCommSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 16, 1, 13),
    _CfprApCommSyslogSeverity_Type()
)
cfprApCommSyslogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogSeverity.setStatus("current")
_CfprApCommSyslogClientTable_Object = MibTable
cfprApCommSyslogClientTable = _CfprApCommSyslogClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17)
)
if mibBuilder.loadTexts:
    cfprApCommSyslogClientTable.setStatus("current")
_CfprApCommSyslogClientEntry_Object = MibTableRow
cfprApCommSyslogClientEntry = _CfprApCommSyslogClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1)
)
cfprApCommSyslogClientEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSyslogClientInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSyslogClientEntry.setStatus("current")
_CfprApCommSyslogClientInstanceId_Type = CfprApManagedObjectId
_CfprApCommSyslogClientInstanceId_Object = MibTableColumn
cfprApCommSyslogClientInstanceId = _CfprApCommSyslogClientInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1, 1),
    _CfprApCommSyslogClientInstanceId_Type()
)
cfprApCommSyslogClientInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSyslogClientInstanceId.setStatus("current")
_CfprApCommSyslogClientDn_Type = CfprApManagedObjectDn
_CfprApCommSyslogClientDn_Object = MibTableColumn
cfprApCommSyslogClientDn = _CfprApCommSyslogClientDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1, 2),
    _CfprApCommSyslogClientDn_Type()
)
cfprApCommSyslogClientDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogClientDn.setStatus("current")
_CfprApCommSyslogClientRn_Type = SnmpAdminString
_CfprApCommSyslogClientRn_Object = MibTableColumn
cfprApCommSyslogClientRn = _CfprApCommSyslogClientRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1, 3),
    _CfprApCommSyslogClientRn_Type()
)
cfprApCommSyslogClientRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogClientRn.setStatus("current")
_CfprApCommSyslogClientAdminState_Type = CfprApCommSyslogAdminState
_CfprApCommSyslogClientAdminState_Object = MibTableColumn
cfprApCommSyslogClientAdminState = _CfprApCommSyslogClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1, 4),
    _CfprApCommSyslogClientAdminState_Type()
)
cfprApCommSyslogClientAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogClientAdminState.setStatus("current")
_CfprApCommSyslogClientForwardingFacility_Type = CfprApCommSyslogForwardingFacility
_CfprApCommSyslogClientForwardingFacility_Object = MibTableColumn
cfprApCommSyslogClientForwardingFacility = _CfprApCommSyslogClientForwardingFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1, 5),
    _CfprApCommSyslogClientForwardingFacility_Type()
)
cfprApCommSyslogClientForwardingFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogClientForwardingFacility.setStatus("current")
_CfprApCommSyslogClientHostname_Type = SnmpAdminString
_CfprApCommSyslogClientHostname_Object = MibTableColumn
cfprApCommSyslogClientHostname = _CfprApCommSyslogClientHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1, 6),
    _CfprApCommSyslogClientHostname_Type()
)
cfprApCommSyslogClientHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogClientHostname.setStatus("current")
_CfprApCommSyslogClientName_Type = CfprApCommSyslogClientEnum
_CfprApCommSyslogClientName_Object = MibTableColumn
cfprApCommSyslogClientName = _CfprApCommSyslogClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1, 7),
    _CfprApCommSyslogClientName_Type()
)
cfprApCommSyslogClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogClientName.setStatus("current")
_CfprApCommSyslogClientSeverity_Type = CfprApCommSyslogSeverity
_CfprApCommSyslogClientSeverity_Object = MibTableColumn
cfprApCommSyslogClientSeverity = _CfprApCommSyslogClientSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 17, 1, 8),
    _CfprApCommSyslogClientSeverity_Type()
)
cfprApCommSyslogClientSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogClientSeverity.setStatus("current")
_CfprApCommSyslogConsoleTable_Object = MibTable
cfprApCommSyslogConsoleTable = _CfprApCommSyslogConsoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18)
)
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleTable.setStatus("current")
_CfprApCommSyslogConsoleEntry_Object = MibTableRow
cfprApCommSyslogConsoleEntry = _CfprApCommSyslogConsoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18, 1)
)
cfprApCommSyslogConsoleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSyslogConsoleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleEntry.setStatus("current")
_CfprApCommSyslogConsoleInstanceId_Type = CfprApManagedObjectId
_CfprApCommSyslogConsoleInstanceId_Object = MibTableColumn
cfprApCommSyslogConsoleInstanceId = _CfprApCommSyslogConsoleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18, 1, 1),
    _CfprApCommSyslogConsoleInstanceId_Type()
)
cfprApCommSyslogConsoleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleInstanceId.setStatus("current")
_CfprApCommSyslogConsoleDn_Type = CfprApManagedObjectDn
_CfprApCommSyslogConsoleDn_Object = MibTableColumn
cfprApCommSyslogConsoleDn = _CfprApCommSyslogConsoleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18, 1, 2),
    _CfprApCommSyslogConsoleDn_Type()
)
cfprApCommSyslogConsoleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleDn.setStatus("current")
_CfprApCommSyslogConsoleRn_Type = SnmpAdminString
_CfprApCommSyslogConsoleRn_Object = MibTableColumn
cfprApCommSyslogConsoleRn = _CfprApCommSyslogConsoleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18, 1, 3),
    _CfprApCommSyslogConsoleRn_Type()
)
cfprApCommSyslogConsoleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleRn.setStatus("current")
_CfprApCommSyslogConsoleAdminState_Type = CfprApCommSyslogAdminState
_CfprApCommSyslogConsoleAdminState_Object = MibTableColumn
cfprApCommSyslogConsoleAdminState = _CfprApCommSyslogConsoleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18, 1, 4),
    _CfprApCommSyslogConsoleAdminState_Type()
)
cfprApCommSyslogConsoleAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleAdminState.setStatus("current")
_CfprApCommSyslogConsoleDescr_Type = SnmpAdminString
_CfprApCommSyslogConsoleDescr_Object = MibTableColumn
cfprApCommSyslogConsoleDescr = _CfprApCommSyslogConsoleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18, 1, 5),
    _CfprApCommSyslogConsoleDescr_Type()
)
cfprApCommSyslogConsoleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleDescr.setStatus("current")
_CfprApCommSyslogConsoleName_Type = SnmpAdminString
_CfprApCommSyslogConsoleName_Object = MibTableColumn
cfprApCommSyslogConsoleName = _CfprApCommSyslogConsoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18, 1, 6),
    _CfprApCommSyslogConsoleName_Type()
)
cfprApCommSyslogConsoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleName.setStatus("current")
_CfprApCommSyslogConsoleSeverity_Type = CfprApCommSyslogRestrictedSeverity
_CfprApCommSyslogConsoleSeverity_Object = MibTableColumn
cfprApCommSyslogConsoleSeverity = _CfprApCommSyslogConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 18, 1, 7),
    _CfprApCommSyslogConsoleSeverity_Type()
)
cfprApCommSyslogConsoleSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogConsoleSeverity.setStatus("current")
_CfprApCommSyslogFileTable_Object = MibTable
cfprApCommSyslogFileTable = _CfprApCommSyslogFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19)
)
if mibBuilder.loadTexts:
    cfprApCommSyslogFileTable.setStatus("current")
_CfprApCommSyslogFileEntry_Object = MibTableRow
cfprApCommSyslogFileEntry = _CfprApCommSyslogFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1)
)
cfprApCommSyslogFileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSyslogFileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSyslogFileEntry.setStatus("current")
_CfprApCommSyslogFileInstanceId_Type = CfprApManagedObjectId
_CfprApCommSyslogFileInstanceId_Object = MibTableColumn
cfprApCommSyslogFileInstanceId = _CfprApCommSyslogFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1, 1),
    _CfprApCommSyslogFileInstanceId_Type()
)
cfprApCommSyslogFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSyslogFileInstanceId.setStatus("current")
_CfprApCommSyslogFileDn_Type = CfprApManagedObjectDn
_CfprApCommSyslogFileDn_Object = MibTableColumn
cfprApCommSyslogFileDn = _CfprApCommSyslogFileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1, 2),
    _CfprApCommSyslogFileDn_Type()
)
cfprApCommSyslogFileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogFileDn.setStatus("current")
_CfprApCommSyslogFileRn_Type = SnmpAdminString
_CfprApCommSyslogFileRn_Object = MibTableColumn
cfprApCommSyslogFileRn = _CfprApCommSyslogFileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1, 3),
    _CfprApCommSyslogFileRn_Type()
)
cfprApCommSyslogFileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogFileRn.setStatus("current")
_CfprApCommSyslogFileAdminState_Type = CfprApCommSyslogAdminState
_CfprApCommSyslogFileAdminState_Object = MibTableColumn
cfprApCommSyslogFileAdminState = _CfprApCommSyslogFileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1, 4),
    _CfprApCommSyslogFileAdminState_Type()
)
cfprApCommSyslogFileAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogFileAdminState.setStatus("current")
_CfprApCommSyslogFileDescr_Type = SnmpAdminString
_CfprApCommSyslogFileDescr_Object = MibTableColumn
cfprApCommSyslogFileDescr = _CfprApCommSyslogFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1, 5),
    _CfprApCommSyslogFileDescr_Type()
)
cfprApCommSyslogFileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogFileDescr.setStatus("current")
_CfprApCommSyslogFileName_Type = SnmpAdminString
_CfprApCommSyslogFileName_Object = MibTableColumn
cfprApCommSyslogFileName = _CfprApCommSyslogFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1, 6),
    _CfprApCommSyslogFileName_Type()
)
cfprApCommSyslogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogFileName.setStatus("current")
_CfprApCommSyslogFileSeverity_Type = CfprApCommSyslogSeverity
_CfprApCommSyslogFileSeverity_Object = MibTableColumn
cfprApCommSyslogFileSeverity = _CfprApCommSyslogFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1, 7),
    _CfprApCommSyslogFileSeverity_Type()
)
cfprApCommSyslogFileSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogFileSeverity.setStatus("current")
_CfprApCommSyslogFileSize_Type = CfprApCommSyslogFileSize
_CfprApCommSyslogFileSize_Object = MibTableColumn
cfprApCommSyslogFileSize = _CfprApCommSyslogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 19, 1, 8),
    _CfprApCommSyslogFileSize_Type()
)
cfprApCommSyslogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogFileSize.setStatus("current")
_CfprApCommSyslogMonitorTable_Object = MibTable
cfprApCommSyslogMonitorTable = _CfprApCommSyslogMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20)
)
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorTable.setStatus("current")
_CfprApCommSyslogMonitorEntry_Object = MibTableRow
cfprApCommSyslogMonitorEntry = _CfprApCommSyslogMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20, 1)
)
cfprApCommSyslogMonitorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSyslogMonitorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorEntry.setStatus("current")
_CfprApCommSyslogMonitorInstanceId_Type = CfprApManagedObjectId
_CfprApCommSyslogMonitorInstanceId_Object = MibTableColumn
cfprApCommSyslogMonitorInstanceId = _CfprApCommSyslogMonitorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20, 1, 1),
    _CfprApCommSyslogMonitorInstanceId_Type()
)
cfprApCommSyslogMonitorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorInstanceId.setStatus("current")
_CfprApCommSyslogMonitorDn_Type = CfprApManagedObjectDn
_CfprApCommSyslogMonitorDn_Object = MibTableColumn
cfprApCommSyslogMonitorDn = _CfprApCommSyslogMonitorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20, 1, 2),
    _CfprApCommSyslogMonitorDn_Type()
)
cfprApCommSyslogMonitorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorDn.setStatus("current")
_CfprApCommSyslogMonitorRn_Type = SnmpAdminString
_CfprApCommSyslogMonitorRn_Object = MibTableColumn
cfprApCommSyslogMonitorRn = _CfprApCommSyslogMonitorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20, 1, 3),
    _CfprApCommSyslogMonitorRn_Type()
)
cfprApCommSyslogMonitorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorRn.setStatus("current")
_CfprApCommSyslogMonitorAdminState_Type = CfprApCommSyslogAdminState
_CfprApCommSyslogMonitorAdminState_Object = MibTableColumn
cfprApCommSyslogMonitorAdminState = _CfprApCommSyslogMonitorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20, 1, 4),
    _CfprApCommSyslogMonitorAdminState_Type()
)
cfprApCommSyslogMonitorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorAdminState.setStatus("current")
_CfprApCommSyslogMonitorDescr_Type = SnmpAdminString
_CfprApCommSyslogMonitorDescr_Object = MibTableColumn
cfprApCommSyslogMonitorDescr = _CfprApCommSyslogMonitorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20, 1, 5),
    _CfprApCommSyslogMonitorDescr_Type()
)
cfprApCommSyslogMonitorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorDescr.setStatus("current")
_CfprApCommSyslogMonitorName_Type = SnmpAdminString
_CfprApCommSyslogMonitorName_Object = MibTableColumn
cfprApCommSyslogMonitorName = _CfprApCommSyslogMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20, 1, 6),
    _CfprApCommSyslogMonitorName_Type()
)
cfprApCommSyslogMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorName.setStatus("current")
_CfprApCommSyslogMonitorSeverity_Type = CfprApCommSyslogSeverity
_CfprApCommSyslogMonitorSeverity_Object = MibTableColumn
cfprApCommSyslogMonitorSeverity = _CfprApCommSyslogMonitorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 20, 1, 7),
    _CfprApCommSyslogMonitorSeverity_Type()
)
cfprApCommSyslogMonitorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogMonitorSeverity.setStatus("current")
_CfprApCommSyslogSourceTable_Object = MibTable
cfprApCommSyslogSourceTable = _CfprApCommSyslogSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21)
)
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceTable.setStatus("current")
_CfprApCommSyslogSourceEntry_Object = MibTableRow
cfprApCommSyslogSourceEntry = _CfprApCommSyslogSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1)
)
cfprApCommSyslogSourceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommSyslogSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceEntry.setStatus("current")
_CfprApCommSyslogSourceInstanceId_Type = CfprApManagedObjectId
_CfprApCommSyslogSourceInstanceId_Object = MibTableColumn
cfprApCommSyslogSourceInstanceId = _CfprApCommSyslogSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1, 1),
    _CfprApCommSyslogSourceInstanceId_Type()
)
cfprApCommSyslogSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceInstanceId.setStatus("current")
_CfprApCommSyslogSourceDn_Type = CfprApManagedObjectDn
_CfprApCommSyslogSourceDn_Object = MibTableColumn
cfprApCommSyslogSourceDn = _CfprApCommSyslogSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1, 2),
    _CfprApCommSyslogSourceDn_Type()
)
cfprApCommSyslogSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceDn.setStatus("current")
_CfprApCommSyslogSourceRn_Type = SnmpAdminString
_CfprApCommSyslogSourceRn_Object = MibTableColumn
cfprApCommSyslogSourceRn = _CfprApCommSyslogSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1, 3),
    _CfprApCommSyslogSourceRn_Type()
)
cfprApCommSyslogSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceRn.setStatus("current")
_CfprApCommSyslogSourceAudits_Type = CfprApCommSyslogSourceAudits
_CfprApCommSyslogSourceAudits_Object = MibTableColumn
cfprApCommSyslogSourceAudits = _CfprApCommSyslogSourceAudits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1, 4),
    _CfprApCommSyslogSourceAudits_Type()
)
cfprApCommSyslogSourceAudits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceAudits.setStatus("current")
_CfprApCommSyslogSourceDescr_Type = SnmpAdminString
_CfprApCommSyslogSourceDescr_Object = MibTableColumn
cfprApCommSyslogSourceDescr = _CfprApCommSyslogSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1, 5),
    _CfprApCommSyslogSourceDescr_Type()
)
cfprApCommSyslogSourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceDescr.setStatus("current")
_CfprApCommSyslogSourceEvents_Type = CfprApCommSyslogSourceEvents
_CfprApCommSyslogSourceEvents_Object = MibTableColumn
cfprApCommSyslogSourceEvents = _CfprApCommSyslogSourceEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1, 6),
    _CfprApCommSyslogSourceEvents_Type()
)
cfprApCommSyslogSourceEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceEvents.setStatus("current")
_CfprApCommSyslogSourceFaults_Type = CfprApCommSyslogSourceFaults
_CfprApCommSyslogSourceFaults_Object = MibTableColumn
cfprApCommSyslogSourceFaults = _CfprApCommSyslogSourceFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1, 7),
    _CfprApCommSyslogSourceFaults_Type()
)
cfprApCommSyslogSourceFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceFaults.setStatus("current")
_CfprApCommSyslogSourceName_Type = SnmpAdminString
_CfprApCommSyslogSourceName_Object = MibTableColumn
cfprApCommSyslogSourceName = _CfprApCommSyslogSourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 21, 1, 8),
    _CfprApCommSyslogSourceName_Type()
)
cfprApCommSyslogSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommSyslogSourceName.setStatus("current")
_CfprApCommTelnetTable_Object = MibTable
cfprApCommTelnetTable = _CfprApCommTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22)
)
if mibBuilder.loadTexts:
    cfprApCommTelnetTable.setStatus("current")
_CfprApCommTelnetEntry_Object = MibTableRow
cfprApCommTelnetEntry = _CfprApCommTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1)
)
cfprApCommTelnetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommTelnetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommTelnetEntry.setStatus("current")
_CfprApCommTelnetInstanceId_Type = CfprApManagedObjectId
_CfprApCommTelnetInstanceId_Object = MibTableColumn
cfprApCommTelnetInstanceId = _CfprApCommTelnetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 1),
    _CfprApCommTelnetInstanceId_Type()
)
cfprApCommTelnetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommTelnetInstanceId.setStatus("current")
_CfprApCommTelnetDn_Type = CfprApManagedObjectDn
_CfprApCommTelnetDn_Object = MibTableColumn
cfprApCommTelnetDn = _CfprApCommTelnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 2),
    _CfprApCommTelnetDn_Type()
)
cfprApCommTelnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetDn.setStatus("current")
_CfprApCommTelnetRn_Type = SnmpAdminString
_CfprApCommTelnetRn_Object = MibTableColumn
cfprApCommTelnetRn = _CfprApCommTelnetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 3),
    _CfprApCommTelnetRn_Type()
)
cfprApCommTelnetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetRn.setStatus("current")
_CfprApCommTelnetAdminState_Type = CfprApCommAdminState
_CfprApCommTelnetAdminState_Object = MibTableColumn
cfprApCommTelnetAdminState = _CfprApCommTelnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 4),
    _CfprApCommTelnetAdminState_Type()
)
cfprApCommTelnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetAdminState.setStatus("current")
_CfprApCommTelnetDescr_Type = SnmpAdminString
_CfprApCommTelnetDescr_Object = MibTableColumn
cfprApCommTelnetDescr = _CfprApCommTelnetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 5),
    _CfprApCommTelnetDescr_Type()
)
cfprApCommTelnetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetDescr.setStatus("current")
_CfprApCommTelnetIntId_Type = SnmpAdminString
_CfprApCommTelnetIntId_Object = MibTableColumn
cfprApCommTelnetIntId = _CfprApCommTelnetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 6),
    _CfprApCommTelnetIntId_Type()
)
cfprApCommTelnetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetIntId.setStatus("current")
_CfprApCommTelnetName_Type = SnmpAdminString
_CfprApCommTelnetName_Object = MibTableColumn
cfprApCommTelnetName = _CfprApCommTelnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 7),
    _CfprApCommTelnetName_Type()
)
cfprApCommTelnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetName.setStatus("current")
_CfprApCommTelnetOperPort_Type = Gauge32
_CfprApCommTelnetOperPort_Object = MibTableColumn
cfprApCommTelnetOperPort = _CfprApCommTelnetOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 8),
    _CfprApCommTelnetOperPort_Type()
)
cfprApCommTelnetOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetOperPort.setStatus("current")
_CfprApCommTelnetPolicyLevel_Type = Gauge32
_CfprApCommTelnetPolicyLevel_Object = MibTableColumn
cfprApCommTelnetPolicyLevel = _CfprApCommTelnetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 9),
    _CfprApCommTelnetPolicyLevel_Type()
)
cfprApCommTelnetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetPolicyLevel.setStatus("current")
_CfprApCommTelnetPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommTelnetPolicyOwner_Object = MibTableColumn
cfprApCommTelnetPolicyOwner = _CfprApCommTelnetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 10),
    _CfprApCommTelnetPolicyOwner_Type()
)
cfprApCommTelnetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetPolicyOwner.setStatus("current")
_CfprApCommTelnetPort_Type = Gauge32
_CfprApCommTelnetPort_Object = MibTableColumn
cfprApCommTelnetPort = _CfprApCommTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 11),
    _CfprApCommTelnetPort_Type()
)
cfprApCommTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetPort.setStatus("current")
_CfprApCommTelnetProto_Type = CfprApCommShellProto
_CfprApCommTelnetProto_Object = MibTableColumn
cfprApCommTelnetProto = _CfprApCommTelnetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 22, 1, 12),
    _CfprApCommTelnetProto_Type()
)
cfprApCommTelnetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommTelnetProto.setStatus("current")
_CfprApCommWebChannelTable_Object = MibTable
cfprApCommWebChannelTable = _CfprApCommWebChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23)
)
if mibBuilder.loadTexts:
    cfprApCommWebChannelTable.setStatus("current")
_CfprApCommWebChannelEntry_Object = MibTableRow
cfprApCommWebChannelEntry = _CfprApCommWebChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1)
)
cfprApCommWebChannelEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommWebChannelInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommWebChannelEntry.setStatus("current")
_CfprApCommWebChannelInstanceId_Type = CfprApManagedObjectId
_CfprApCommWebChannelInstanceId_Object = MibTableColumn
cfprApCommWebChannelInstanceId = _CfprApCommWebChannelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 1),
    _CfprApCommWebChannelInstanceId_Type()
)
cfprApCommWebChannelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommWebChannelInstanceId.setStatus("current")
_CfprApCommWebChannelDn_Type = CfprApManagedObjectDn
_CfprApCommWebChannelDn_Object = MibTableColumn
cfprApCommWebChannelDn = _CfprApCommWebChannelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 2),
    _CfprApCommWebChannelDn_Type()
)
cfprApCommWebChannelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebChannelDn.setStatus("current")
_CfprApCommWebChannelRn_Type = SnmpAdminString
_CfprApCommWebChannelRn_Object = MibTableColumn
cfprApCommWebChannelRn = _CfprApCommWebChannelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 3),
    _CfprApCommWebChannelRn_Type()
)
cfprApCommWebChannelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebChannelRn.setStatus("current")
_CfprApCommWebChannelChannelState_Type = CfprApCommChannel
_CfprApCommWebChannelChannelState_Object = MibTableColumn
cfprApCommWebChannelChannelState = _CfprApCommWebChannelChannelState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 4),
    _CfprApCommWebChannelChannelState_Type()
)
cfprApCommWebChannelChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebChannelChannelState.setStatus("current")
_CfprApCommWebChannelDescr_Type = SnmpAdminString
_CfprApCommWebChannelDescr_Object = MibTableColumn
cfprApCommWebChannelDescr = _CfprApCommWebChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 5),
    _CfprApCommWebChannelDescr_Type()
)
cfprApCommWebChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebChannelDescr.setStatus("current")
_CfprApCommWebChannelIntId_Type = SnmpAdminString
_CfprApCommWebChannelIntId_Object = MibTableColumn
cfprApCommWebChannelIntId = _CfprApCommWebChannelIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 6),
    _CfprApCommWebChannelIntId_Type()
)
cfprApCommWebChannelIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebChannelIntId.setStatus("current")
_CfprApCommWebChannelName_Type = SnmpAdminString
_CfprApCommWebChannelName_Object = MibTableColumn
cfprApCommWebChannelName = _CfprApCommWebChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 7),
    _CfprApCommWebChannelName_Type()
)
cfprApCommWebChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebChannelName.setStatus("current")
_CfprApCommWebChannelPolicyLevel_Type = Gauge32
_CfprApCommWebChannelPolicyLevel_Object = MibTableColumn
cfprApCommWebChannelPolicyLevel = _CfprApCommWebChannelPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 8),
    _CfprApCommWebChannelPolicyLevel_Type()
)
cfprApCommWebChannelPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebChannelPolicyLevel.setStatus("current")
_CfprApCommWebChannelPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommWebChannelPolicyOwner_Object = MibTableColumn
cfprApCommWebChannelPolicyOwner = _CfprApCommWebChannelPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 23, 1, 9),
    _CfprApCommWebChannelPolicyOwner_Type()
)
cfprApCommWebChannelPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebChannelPolicyOwner.setStatus("current")
_CfprApCommWebSvcLimitsTable_Object = MibTable
cfprApCommWebSvcLimitsTable = _CfprApCommWebSvcLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24)
)
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsTable.setStatus("current")
_CfprApCommWebSvcLimitsEntry_Object = MibTableRow
cfprApCommWebSvcLimitsEntry = _CfprApCommWebSvcLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1)
)
cfprApCommWebSvcLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommWebSvcLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsEntry.setStatus("current")
_CfprApCommWebSvcLimitsInstanceId_Type = CfprApManagedObjectId
_CfprApCommWebSvcLimitsInstanceId_Object = MibTableColumn
cfprApCommWebSvcLimitsInstanceId = _CfprApCommWebSvcLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 1),
    _CfprApCommWebSvcLimitsInstanceId_Type()
)
cfprApCommWebSvcLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsInstanceId.setStatus("current")
_CfprApCommWebSvcLimitsDn_Type = CfprApManagedObjectDn
_CfprApCommWebSvcLimitsDn_Object = MibTableColumn
cfprApCommWebSvcLimitsDn = _CfprApCommWebSvcLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 2),
    _CfprApCommWebSvcLimitsDn_Type()
)
cfprApCommWebSvcLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsDn.setStatus("current")
_CfprApCommWebSvcLimitsRn_Type = SnmpAdminString
_CfprApCommWebSvcLimitsRn_Object = MibTableColumn
cfprApCommWebSvcLimitsRn = _CfprApCommWebSvcLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 3),
    _CfprApCommWebSvcLimitsRn_Type()
)
cfprApCommWebSvcLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsRn.setStatus("current")
_CfprApCommWebSvcLimitsDescr_Type = SnmpAdminString
_CfprApCommWebSvcLimitsDescr_Object = MibTableColumn
cfprApCommWebSvcLimitsDescr = _CfprApCommWebSvcLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 4),
    _CfprApCommWebSvcLimitsDescr_Type()
)
cfprApCommWebSvcLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsDescr.setStatus("current")
_CfprApCommWebSvcLimitsIntId_Type = SnmpAdminString
_CfprApCommWebSvcLimitsIntId_Object = MibTableColumn
cfprApCommWebSvcLimitsIntId = _CfprApCommWebSvcLimitsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 5),
    _CfprApCommWebSvcLimitsIntId_Type()
)
cfprApCommWebSvcLimitsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsIntId.setStatus("current")
_CfprApCommWebSvcLimitsName_Type = SnmpAdminString
_CfprApCommWebSvcLimitsName_Object = MibTableColumn
cfprApCommWebSvcLimitsName = _CfprApCommWebSvcLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 6),
    _CfprApCommWebSvcLimitsName_Type()
)
cfprApCommWebSvcLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsName.setStatus("current")
_CfprApCommWebSvcLimitsPolicyLevel_Type = Gauge32
_CfprApCommWebSvcLimitsPolicyLevel_Object = MibTableColumn
cfprApCommWebSvcLimitsPolicyLevel = _CfprApCommWebSvcLimitsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 7),
    _CfprApCommWebSvcLimitsPolicyLevel_Type()
)
cfprApCommWebSvcLimitsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsPolicyLevel.setStatus("current")
_CfprApCommWebSvcLimitsPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommWebSvcLimitsPolicyOwner_Object = MibTableColumn
cfprApCommWebSvcLimitsPolicyOwner = _CfprApCommWebSvcLimitsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 8),
    _CfprApCommWebSvcLimitsPolicyOwner_Type()
)
cfprApCommWebSvcLimitsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsPolicyOwner.setStatus("current")
_CfprApCommWebSvcLimitsSessionsPerUser_Type = Gauge32
_CfprApCommWebSvcLimitsSessionsPerUser_Object = MibTableColumn
cfprApCommWebSvcLimitsSessionsPerUser = _CfprApCommWebSvcLimitsSessionsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 9),
    _CfprApCommWebSvcLimitsSessionsPerUser_Type()
)
cfprApCommWebSvcLimitsSessionsPerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsSessionsPerUser.setStatus("current")
_CfprApCommWebSvcLimitsTotalSessions_Type = Gauge32
_CfprApCommWebSvcLimitsTotalSessions_Object = MibTableColumn
cfprApCommWebSvcLimitsTotalSessions = _CfprApCommWebSvcLimitsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 24, 1, 10),
    _CfprApCommWebSvcLimitsTotalSessions_Type()
)
cfprApCommWebSvcLimitsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWebSvcLimitsTotalSessions.setStatus("current")
_CfprApCommWsmanTable_Object = MibTable
cfprApCommWsmanTable = _CfprApCommWsmanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25)
)
if mibBuilder.loadTexts:
    cfprApCommWsmanTable.setStatus("current")
_CfprApCommWsmanEntry_Object = MibTableRow
cfprApCommWsmanEntry = _CfprApCommWsmanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1)
)
cfprApCommWsmanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMM-MIB", "cfprApCommWsmanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCommWsmanEntry.setStatus("current")
_CfprApCommWsmanInstanceId_Type = CfprApManagedObjectId
_CfprApCommWsmanInstanceId_Object = MibTableColumn
cfprApCommWsmanInstanceId = _CfprApCommWsmanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 1),
    _CfprApCommWsmanInstanceId_Type()
)
cfprApCommWsmanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCommWsmanInstanceId.setStatus("current")
_CfprApCommWsmanDn_Type = CfprApManagedObjectDn
_CfprApCommWsmanDn_Object = MibTableColumn
cfprApCommWsmanDn = _CfprApCommWsmanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 2),
    _CfprApCommWsmanDn_Type()
)
cfprApCommWsmanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanDn.setStatus("current")
_CfprApCommWsmanRn_Type = SnmpAdminString
_CfprApCommWsmanRn_Object = MibTableColumn
cfprApCommWsmanRn = _CfprApCommWsmanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 3),
    _CfprApCommWsmanRn_Type()
)
cfprApCommWsmanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanRn.setStatus("current")
_CfprApCommWsmanAdminState_Type = CfprApCommAdminState
_CfprApCommWsmanAdminState_Object = MibTableColumn
cfprApCommWsmanAdminState = _CfprApCommWsmanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 4),
    _CfprApCommWsmanAdminState_Type()
)
cfprApCommWsmanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanAdminState.setStatus("current")
_CfprApCommWsmanDescr_Type = SnmpAdminString
_CfprApCommWsmanDescr_Object = MibTableColumn
cfprApCommWsmanDescr = _CfprApCommWsmanDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 5),
    _CfprApCommWsmanDescr_Type()
)
cfprApCommWsmanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanDescr.setStatus("current")
_CfprApCommWsmanIntId_Type = SnmpAdminString
_CfprApCommWsmanIntId_Object = MibTableColumn
cfprApCommWsmanIntId = _CfprApCommWsmanIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 6),
    _CfprApCommWsmanIntId_Type()
)
cfprApCommWsmanIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanIntId.setStatus("current")
_CfprApCommWsmanName_Type = SnmpAdminString
_CfprApCommWsmanName_Object = MibTableColumn
cfprApCommWsmanName = _CfprApCommWsmanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 7),
    _CfprApCommWsmanName_Type()
)
cfprApCommWsmanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanName.setStatus("current")
_CfprApCommWsmanOperPort_Type = Gauge32
_CfprApCommWsmanOperPort_Object = MibTableColumn
cfprApCommWsmanOperPort = _CfprApCommWsmanOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 8),
    _CfprApCommWsmanOperPort_Type()
)
cfprApCommWsmanOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanOperPort.setStatus("current")
_CfprApCommWsmanPolicyLevel_Type = Gauge32
_CfprApCommWsmanPolicyLevel_Object = MibTableColumn
cfprApCommWsmanPolicyLevel = _CfprApCommWsmanPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 9),
    _CfprApCommWsmanPolicyLevel_Type()
)
cfprApCommWsmanPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanPolicyLevel.setStatus("current")
_CfprApCommWsmanPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApCommWsmanPolicyOwner_Object = MibTableColumn
cfprApCommWsmanPolicyOwner = _CfprApCommWsmanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 10),
    _CfprApCommWsmanPolicyOwner_Type()
)
cfprApCommWsmanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanPolicyOwner.setStatus("current")
_CfprApCommWsmanPort_Type = Gauge32
_CfprApCommWsmanPort_Object = MibTableColumn
cfprApCommWsmanPort = _CfprApCommWsmanPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 11),
    _CfprApCommWsmanPort_Type()
)
cfprApCommWsmanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanPort.setStatus("current")
_CfprApCommWsmanProto_Type = CfprApCommWebProto
_CfprApCommWsmanProto_Object = MibTableColumn
cfprApCommWsmanProto = _CfprApCommWsmanProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 11, 25, 1, 12),
    _CfprApCommWsmanProto_Type()
)
cfprApCommWsmanProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCommWsmanProto.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-COMM-MIB",
    **{"cfprApCommObjects": cfprApCommObjects,
       "cfprApCommDateTimeTable": cfprApCommDateTimeTable,
       "cfprApCommDateTimeEntry": cfprApCommDateTimeEntry,
       "cfprApCommDateTimeInstanceId": cfprApCommDateTimeInstanceId,
       "cfprApCommDateTimeDn": cfprApCommDateTimeDn,
       "cfprApCommDateTimeRn": cfprApCommDateTimeRn,
       "cfprApCommDateTimeAdminState": cfprApCommDateTimeAdminState,
       "cfprApCommDateTimeConfigState": cfprApCommDateTimeConfigState,
       "cfprApCommDateTimeDate": cfprApCommDateTimeDate,
       "cfprApCommDateTimeDescr": cfprApCommDateTimeDescr,
       "cfprApCommDateTimeIntId": cfprApCommDateTimeIntId,
       "cfprApCommDateTimeName": cfprApCommDateTimeName,
       "cfprApCommDateTimeOperPort": cfprApCommDateTimeOperPort,
       "cfprApCommDateTimeOperTimezone": cfprApCommDateTimeOperTimezone,
       "cfprApCommDateTimePolicyLevel": cfprApCommDateTimePolicyLevel,
       "cfprApCommDateTimePolicyOwner": cfprApCommDateTimePolicyOwner,
       "cfprApCommDateTimePort": cfprApCommDateTimePort,
       "cfprApCommDateTimeProto": cfprApCommDateTimeProto,
       "cfprApCommDateTimeTimezone": cfprApCommDateTimeTimezone,
       "cfprApCommDnsTable": cfprApCommDnsTable,
       "cfprApCommDnsEntry": cfprApCommDnsEntry,
       "cfprApCommDnsInstanceId": cfprApCommDnsInstanceId,
       "cfprApCommDnsDn": cfprApCommDnsDn,
       "cfprApCommDnsRn": cfprApCommDnsRn,
       "cfprApCommDnsAdminState": cfprApCommDnsAdminState,
       "cfprApCommDnsDescr": cfprApCommDnsDescr,
       "cfprApCommDnsDomain": cfprApCommDnsDomain,
       "cfprApCommDnsIntId": cfprApCommDnsIntId,
       "cfprApCommDnsName": cfprApCommDnsName,
       "cfprApCommDnsOperPort": cfprApCommDnsOperPort,
       "cfprApCommDnsPolicyLevel": cfprApCommDnsPolicyLevel,
       "cfprApCommDnsPolicyOwner": cfprApCommDnsPolicyOwner,
       "cfprApCommDnsPort": cfprApCommDnsPort,
       "cfprApCommDnsProto": cfprApCommDnsProto,
       "cfprApCommDnsProviderTable": cfprApCommDnsProviderTable,
       "cfprApCommDnsProviderEntry": cfprApCommDnsProviderEntry,
       "cfprApCommDnsProviderInstanceId": cfprApCommDnsProviderInstanceId,
       "cfprApCommDnsProviderDn": cfprApCommDnsProviderDn,
       "cfprApCommDnsProviderRn": cfprApCommDnsProviderRn,
       "cfprApCommDnsProviderAdminState": cfprApCommDnsProviderAdminState,
       "cfprApCommDnsProviderDescr": cfprApCommDnsProviderDescr,
       "cfprApCommDnsProviderHostname": cfprApCommDnsProviderHostname,
       "cfprApCommDnsProviderName": cfprApCommDnsProviderName,
       "cfprApCommEvtChannelTable": cfprApCommEvtChannelTable,
       "cfprApCommEvtChannelEntry": cfprApCommEvtChannelEntry,
       "cfprApCommEvtChannelInstanceId": cfprApCommEvtChannelInstanceId,
       "cfprApCommEvtChannelDn": cfprApCommEvtChannelDn,
       "cfprApCommEvtChannelRn": cfprApCommEvtChannelRn,
       "cfprApCommEvtChannelChannelState": cfprApCommEvtChannelChannelState,
       "cfprApCommEvtChannelDescr": cfprApCommEvtChannelDescr,
       "cfprApCommEvtChannelIntId": cfprApCommEvtChannelIntId,
       "cfprApCommEvtChannelName": cfprApCommEvtChannelName,
       "cfprApCommEvtChannelPolicyLevel": cfprApCommEvtChannelPolicyLevel,
       "cfprApCommEvtChannelPolicyOwner": cfprApCommEvtChannelPolicyOwner,
       "cfprApCommHttpsTable": cfprApCommHttpsTable,
       "cfprApCommHttpsEntry": cfprApCommHttpsEntry,
       "cfprApCommHttpsInstanceId": cfprApCommHttpsInstanceId,
       "cfprApCommHttpsDn": cfprApCommHttpsDn,
       "cfprApCommHttpsRn": cfprApCommHttpsRn,
       "cfprApCommHttpsAdminState": cfprApCommHttpsAdminState,
       "cfprApCommHttpsCipherSuite": cfprApCommHttpsCipherSuite,
       "cfprApCommHttpsCipherSuiteMode": cfprApCommHttpsCipherSuiteMode,
       "cfprApCommHttpsDescr": cfprApCommHttpsDescr,
       "cfprApCommHttpsIntId": cfprApCommHttpsIntId,
       "cfprApCommHttpsKeyRing": cfprApCommHttpsKeyRing,
       "cfprApCommHttpsName": cfprApCommHttpsName,
       "cfprApCommHttpsOperPort": cfprApCommHttpsOperPort,
       "cfprApCommHttpsPolicyLevel": cfprApCommHttpsPolicyLevel,
       "cfprApCommHttpsPolicyOwner": cfprApCommHttpsPolicyOwner,
       "cfprApCommHttpsPort": cfprApCommHttpsPort,
       "cfprApCommHttpsProto": cfprApCommHttpsProto,
       "cfprApCommNtpProviderTable": cfprApCommNtpProviderTable,
       "cfprApCommNtpProviderEntry": cfprApCommNtpProviderEntry,
       "cfprApCommNtpProviderInstanceId": cfprApCommNtpProviderInstanceId,
       "cfprApCommNtpProviderDn": cfprApCommNtpProviderDn,
       "cfprApCommNtpProviderRn": cfprApCommNtpProviderRn,
       "cfprApCommNtpProviderAdminState": cfprApCommNtpProviderAdminState,
       "cfprApCommNtpProviderDescr": cfprApCommNtpProviderDescr,
       "cfprApCommNtpProviderHostname": cfprApCommNtpProviderHostname,
       "cfprApCommNtpProviderName": cfprApCommNtpProviderName,
       "cfprApCommShellSvcLimitsTable": cfprApCommShellSvcLimitsTable,
       "cfprApCommShellSvcLimitsEntry": cfprApCommShellSvcLimitsEntry,
       "cfprApCommShellSvcLimitsInstanceId": cfprApCommShellSvcLimitsInstanceId,
       "cfprApCommShellSvcLimitsDn": cfprApCommShellSvcLimitsDn,
       "cfprApCommShellSvcLimitsRn": cfprApCommShellSvcLimitsRn,
       "cfprApCommShellSvcLimitsDescr": cfprApCommShellSvcLimitsDescr,
       "cfprApCommShellSvcLimitsIntId": cfprApCommShellSvcLimitsIntId,
       "cfprApCommShellSvcLimitsName": cfprApCommShellSvcLimitsName,
       "cfprApCommShellSvcLimitsPolicyLevel": cfprApCommShellSvcLimitsPolicyLevel,
       "cfprApCommShellSvcLimitsPolicyOwner": cfprApCommShellSvcLimitsPolicyOwner,
       "cfprApCommShellSvcLimitsSessionsPerUser": cfprApCommShellSvcLimitsSessionsPerUser,
       "cfprApCommShellSvcLimitsTotalSessions": cfprApCommShellSvcLimitsTotalSessions,
       "cfprApCommSnmpTable": cfprApCommSnmpTable,
       "cfprApCommSnmpEntry": cfprApCommSnmpEntry,
       "cfprApCommSnmpInstanceId": cfprApCommSnmpInstanceId,
       "cfprApCommSnmpDn": cfprApCommSnmpDn,
       "cfprApCommSnmpRn": cfprApCommSnmpRn,
       "cfprApCommSnmpAdminState": cfprApCommSnmpAdminState,
       "cfprApCommSnmpCommunity": cfprApCommSnmpCommunity,
       "cfprApCommSnmpConfigState": cfprApCommSnmpConfigState,
       "cfprApCommSnmpDescr": cfprApCommSnmpDescr,
       "cfprApCommSnmpIntId": cfprApCommSnmpIntId,
       "cfprApCommSnmpIsSetSnmpSecure": cfprApCommSnmpIsSetSnmpSecure,
       "cfprApCommSnmpName": cfprApCommSnmpName,
       "cfprApCommSnmpOperPort": cfprApCommSnmpOperPort,
       "cfprApCommSnmpPolicyLevel": cfprApCommSnmpPolicyLevel,
       "cfprApCommSnmpPolicyOwner": cfprApCommSnmpPolicyOwner,
       "cfprApCommSnmpPort": cfprApCommSnmpPort,
       "cfprApCommSnmpProto": cfprApCommSnmpProto,
       "cfprApCommSnmpSysContact": cfprApCommSnmpSysContact,
       "cfprApCommSnmpSysLocation": cfprApCommSnmpSysLocation,
       "cfprApCommSnmpTrapTable": cfprApCommSnmpTrapTable,
       "cfprApCommSnmpTrapEntry": cfprApCommSnmpTrapEntry,
       "cfprApCommSnmpTrapInstanceId": cfprApCommSnmpTrapInstanceId,
       "cfprApCommSnmpTrapDn": cfprApCommSnmpTrapDn,
       "cfprApCommSnmpTrapRn": cfprApCommSnmpTrapRn,
       "cfprApCommSnmpTrapCommunity": cfprApCommSnmpTrapCommunity,
       "cfprApCommSnmpTrapHostname": cfprApCommSnmpTrapHostname,
       "cfprApCommSnmpTrapNotificationType": cfprApCommSnmpTrapNotificationType,
       "cfprApCommSnmpTrapPort": cfprApCommSnmpTrapPort,
       "cfprApCommSnmpTrapV3Privilege": cfprApCommSnmpTrapV3Privilege,
       "cfprApCommSnmpTrapVersion": cfprApCommSnmpTrapVersion,
       "cfprApCommSnmpUserTable": cfprApCommSnmpUserTable,
       "cfprApCommSnmpUserEntry": cfprApCommSnmpUserEntry,
       "cfprApCommSnmpUserInstanceId": cfprApCommSnmpUserInstanceId,
       "cfprApCommSnmpUserDn": cfprApCommSnmpUserDn,
       "cfprApCommSnmpUserRn": cfprApCommSnmpUserRn,
       "cfprApCommSnmpUserAuth": cfprApCommSnmpUserAuth,
       "cfprApCommSnmpUserConfigState": cfprApCommSnmpUserConfigState,
       "cfprApCommSnmpUserConfigStatusMessage": cfprApCommSnmpUserConfigStatusMessage,
       "cfprApCommSnmpUserDescr": cfprApCommSnmpUserDescr,
       "cfprApCommSnmpUserName": cfprApCommSnmpUserName,
       "cfprApCommSnmpUserPrivPwdSet": cfprApCommSnmpUserPrivPwdSet,
       "cfprApCommSnmpUserPrivpwd": cfprApCommSnmpUserPrivpwd,
       "cfprApCommSnmpUserPwd": cfprApCommSnmpUserPwd,
       "cfprApCommSnmpUserPwdSet": cfprApCommSnmpUserPwdSet,
       "cfprApCommSnmpUserUseAes": cfprApCommSnmpUserUseAes,
       "cfprApCommSshTable": cfprApCommSshTable,
       "cfprApCommSshEntry": cfprApCommSshEntry,
       "cfprApCommSshInstanceId": cfprApCommSshInstanceId,
       "cfprApCommSshDn": cfprApCommSshDn,
       "cfprApCommSshRn": cfprApCommSshRn,
       "cfprApCommSshAdminState": cfprApCommSshAdminState,
       "cfprApCommSshDescr": cfprApCommSshDescr,
       "cfprApCommSshIntId": cfprApCommSshIntId,
       "cfprApCommSshName": cfprApCommSshName,
       "cfprApCommSshOperPort": cfprApCommSshOperPort,
       "cfprApCommSshPolicyLevel": cfprApCommSshPolicyLevel,
       "cfprApCommSshPolicyOwner": cfprApCommSshPolicyOwner,
       "cfprApCommSshPort": cfprApCommSshPort,
       "cfprApCommSshProto": cfprApCommSshProto,
       "cfprApCommSvcEpTable": cfprApCommSvcEpTable,
       "cfprApCommSvcEpEntry": cfprApCommSvcEpEntry,
       "cfprApCommSvcEpInstanceId": cfprApCommSvcEpInstanceId,
       "cfprApCommSvcEpDn": cfprApCommSvcEpDn,
       "cfprApCommSvcEpRn": cfprApCommSvcEpRn,
       "cfprApCommSvcEpConfigState": cfprApCommSvcEpConfigState,
       "cfprApCommSvcEpConfigStatusMessage": cfprApCommSvcEpConfigStatusMessage,
       "cfprApCommSvcEpDescr": cfprApCommSvcEpDescr,
       "cfprApCommSvcEpFsmDescr": cfprApCommSvcEpFsmDescr,
       "cfprApCommSvcEpFsmFlags": cfprApCommSvcEpFsmFlags,
       "cfprApCommSvcEpFsmPrev": cfprApCommSvcEpFsmPrev,
       "cfprApCommSvcEpFsmProgr": cfprApCommSvcEpFsmProgr,
       "cfprApCommSvcEpFsmRmtInvErrCode": cfprApCommSvcEpFsmRmtInvErrCode,
       "cfprApCommSvcEpFsmRmtInvErrDescr": cfprApCommSvcEpFsmRmtInvErrDescr,
       "cfprApCommSvcEpFsmRmtInvRslt": cfprApCommSvcEpFsmRmtInvRslt,
       "cfprApCommSvcEpFsmStageDescr": cfprApCommSvcEpFsmStageDescr,
       "cfprApCommSvcEpFsmStamp": cfprApCommSvcEpFsmStamp,
       "cfprApCommSvcEpFsmStatus": cfprApCommSvcEpFsmStatus,
       "cfprApCommSvcEpFsmTry": cfprApCommSvcEpFsmTry,
       "cfprApCommSvcEpIntId": cfprApCommSvcEpIntId,
       "cfprApCommSvcEpName": cfprApCommSvcEpName,
       "cfprApCommSvcEpPolicyLevel": cfprApCommSvcEpPolicyLevel,
       "cfprApCommSvcEpPolicyOwner": cfprApCommSvcEpPolicyOwner,
       "cfprApCommSvcEpFsmTable": cfprApCommSvcEpFsmTable,
       "cfprApCommSvcEpFsmEntry": cfprApCommSvcEpFsmEntry,
       "cfprApCommSvcEpFsmInstanceId": cfprApCommSvcEpFsmInstanceId,
       "cfprApCommSvcEpFsmDn": cfprApCommSvcEpFsmDn,
       "cfprApCommSvcEpFsmRn": cfprApCommSvcEpFsmRn,
       "cfprApCommSvcEpFsmCompletionTime": cfprApCommSvcEpFsmCompletionTime,
       "cfprApCommSvcEpFsmCurrentFsm": cfprApCommSvcEpFsmCurrentFsm,
       "cfprApCommSvcEpFsmDescrData": cfprApCommSvcEpFsmDescrData,
       "cfprApCommSvcEpFsmFsmStatus": cfprApCommSvcEpFsmFsmStatus,
       "cfprApCommSvcEpFsmProgress": cfprApCommSvcEpFsmProgress,
       "cfprApCommSvcEpFsmRmtErrCode": cfprApCommSvcEpFsmRmtErrCode,
       "cfprApCommSvcEpFsmRmtErrDescr": cfprApCommSvcEpFsmRmtErrDescr,
       "cfprApCommSvcEpFsmRmtRslt": cfprApCommSvcEpFsmRmtRslt,
       "cfprApCommSvcEpFsmStageTable": cfprApCommSvcEpFsmStageTable,
       "cfprApCommSvcEpFsmStageEntry": cfprApCommSvcEpFsmStageEntry,
       "cfprApCommSvcEpFsmStageInstanceId": cfprApCommSvcEpFsmStageInstanceId,
       "cfprApCommSvcEpFsmStageDn": cfprApCommSvcEpFsmStageDn,
       "cfprApCommSvcEpFsmStageRn": cfprApCommSvcEpFsmStageRn,
       "cfprApCommSvcEpFsmStageDescrData": cfprApCommSvcEpFsmStageDescrData,
       "cfprApCommSvcEpFsmStageLastUpdateTime": cfprApCommSvcEpFsmStageLastUpdateTime,
       "cfprApCommSvcEpFsmStageName": cfprApCommSvcEpFsmStageName,
       "cfprApCommSvcEpFsmStageOrder": cfprApCommSvcEpFsmStageOrder,
       "cfprApCommSvcEpFsmStageRetry": cfprApCommSvcEpFsmStageRetry,
       "cfprApCommSvcEpFsmStageStageStatus": cfprApCommSvcEpFsmStageStageStatus,
       "cfprApCommSvcEpFsmTaskTable": cfprApCommSvcEpFsmTaskTable,
       "cfprApCommSvcEpFsmTaskEntry": cfprApCommSvcEpFsmTaskEntry,
       "cfprApCommSvcEpFsmTaskInstanceId": cfprApCommSvcEpFsmTaskInstanceId,
       "cfprApCommSvcEpFsmTaskDn": cfprApCommSvcEpFsmTaskDn,
       "cfprApCommSvcEpFsmTaskRn": cfprApCommSvcEpFsmTaskRn,
       "cfprApCommSvcEpFsmTaskCompletion": cfprApCommSvcEpFsmTaskCompletion,
       "cfprApCommSvcEpFsmTaskFlags": cfprApCommSvcEpFsmTaskFlags,
       "cfprApCommSvcEpFsmTaskItem": cfprApCommSvcEpFsmTaskItem,
       "cfprApCommSvcEpFsmTaskSeqId": cfprApCommSvcEpFsmTaskSeqId,
       "cfprApCommSyslogTable": cfprApCommSyslogTable,
       "cfprApCommSyslogEntry": cfprApCommSyslogEntry,
       "cfprApCommSyslogInstanceId": cfprApCommSyslogInstanceId,
       "cfprApCommSyslogDn": cfprApCommSyslogDn,
       "cfprApCommSyslogRn": cfprApCommSyslogRn,
       "cfprApCommSyslogAdminState": cfprApCommSyslogAdminState,
       "cfprApCommSyslogDescr": cfprApCommSyslogDescr,
       "cfprApCommSyslogIntId": cfprApCommSyslogIntId,
       "cfprApCommSyslogName": cfprApCommSyslogName,
       "cfprApCommSyslogOperPort": cfprApCommSyslogOperPort,
       "cfprApCommSyslogPolicyLevel": cfprApCommSyslogPolicyLevel,
       "cfprApCommSyslogPolicyOwner": cfprApCommSyslogPolicyOwner,
       "cfprApCommSyslogPort": cfprApCommSyslogPort,
       "cfprApCommSyslogProto": cfprApCommSyslogProto,
       "cfprApCommSyslogSeverity": cfprApCommSyslogSeverity,
       "cfprApCommSyslogClientTable": cfprApCommSyslogClientTable,
       "cfprApCommSyslogClientEntry": cfprApCommSyslogClientEntry,
       "cfprApCommSyslogClientInstanceId": cfprApCommSyslogClientInstanceId,
       "cfprApCommSyslogClientDn": cfprApCommSyslogClientDn,
       "cfprApCommSyslogClientRn": cfprApCommSyslogClientRn,
       "cfprApCommSyslogClientAdminState": cfprApCommSyslogClientAdminState,
       "cfprApCommSyslogClientForwardingFacility": cfprApCommSyslogClientForwardingFacility,
       "cfprApCommSyslogClientHostname": cfprApCommSyslogClientHostname,
       "cfprApCommSyslogClientName": cfprApCommSyslogClientName,
       "cfprApCommSyslogClientSeverity": cfprApCommSyslogClientSeverity,
       "cfprApCommSyslogConsoleTable": cfprApCommSyslogConsoleTable,
       "cfprApCommSyslogConsoleEntry": cfprApCommSyslogConsoleEntry,
       "cfprApCommSyslogConsoleInstanceId": cfprApCommSyslogConsoleInstanceId,
       "cfprApCommSyslogConsoleDn": cfprApCommSyslogConsoleDn,
       "cfprApCommSyslogConsoleRn": cfprApCommSyslogConsoleRn,
       "cfprApCommSyslogConsoleAdminState": cfprApCommSyslogConsoleAdminState,
       "cfprApCommSyslogConsoleDescr": cfprApCommSyslogConsoleDescr,
       "cfprApCommSyslogConsoleName": cfprApCommSyslogConsoleName,
       "cfprApCommSyslogConsoleSeverity": cfprApCommSyslogConsoleSeverity,
       "cfprApCommSyslogFileTable": cfprApCommSyslogFileTable,
       "cfprApCommSyslogFileEntry": cfprApCommSyslogFileEntry,
       "cfprApCommSyslogFileInstanceId": cfprApCommSyslogFileInstanceId,
       "cfprApCommSyslogFileDn": cfprApCommSyslogFileDn,
       "cfprApCommSyslogFileRn": cfprApCommSyslogFileRn,
       "cfprApCommSyslogFileAdminState": cfprApCommSyslogFileAdminState,
       "cfprApCommSyslogFileDescr": cfprApCommSyslogFileDescr,
       "cfprApCommSyslogFileName": cfprApCommSyslogFileName,
       "cfprApCommSyslogFileSeverity": cfprApCommSyslogFileSeverity,
       "cfprApCommSyslogFileSize": cfprApCommSyslogFileSize,
       "cfprApCommSyslogMonitorTable": cfprApCommSyslogMonitorTable,
       "cfprApCommSyslogMonitorEntry": cfprApCommSyslogMonitorEntry,
       "cfprApCommSyslogMonitorInstanceId": cfprApCommSyslogMonitorInstanceId,
       "cfprApCommSyslogMonitorDn": cfprApCommSyslogMonitorDn,
       "cfprApCommSyslogMonitorRn": cfprApCommSyslogMonitorRn,
       "cfprApCommSyslogMonitorAdminState": cfprApCommSyslogMonitorAdminState,
       "cfprApCommSyslogMonitorDescr": cfprApCommSyslogMonitorDescr,
       "cfprApCommSyslogMonitorName": cfprApCommSyslogMonitorName,
       "cfprApCommSyslogMonitorSeverity": cfprApCommSyslogMonitorSeverity,
       "cfprApCommSyslogSourceTable": cfprApCommSyslogSourceTable,
       "cfprApCommSyslogSourceEntry": cfprApCommSyslogSourceEntry,
       "cfprApCommSyslogSourceInstanceId": cfprApCommSyslogSourceInstanceId,
       "cfprApCommSyslogSourceDn": cfprApCommSyslogSourceDn,
       "cfprApCommSyslogSourceRn": cfprApCommSyslogSourceRn,
       "cfprApCommSyslogSourceAudits": cfprApCommSyslogSourceAudits,
       "cfprApCommSyslogSourceDescr": cfprApCommSyslogSourceDescr,
       "cfprApCommSyslogSourceEvents": cfprApCommSyslogSourceEvents,
       "cfprApCommSyslogSourceFaults": cfprApCommSyslogSourceFaults,
       "cfprApCommSyslogSourceName": cfprApCommSyslogSourceName,
       "cfprApCommTelnetTable": cfprApCommTelnetTable,
       "cfprApCommTelnetEntry": cfprApCommTelnetEntry,
       "cfprApCommTelnetInstanceId": cfprApCommTelnetInstanceId,
       "cfprApCommTelnetDn": cfprApCommTelnetDn,
       "cfprApCommTelnetRn": cfprApCommTelnetRn,
       "cfprApCommTelnetAdminState": cfprApCommTelnetAdminState,
       "cfprApCommTelnetDescr": cfprApCommTelnetDescr,
       "cfprApCommTelnetIntId": cfprApCommTelnetIntId,
       "cfprApCommTelnetName": cfprApCommTelnetName,
       "cfprApCommTelnetOperPort": cfprApCommTelnetOperPort,
       "cfprApCommTelnetPolicyLevel": cfprApCommTelnetPolicyLevel,
       "cfprApCommTelnetPolicyOwner": cfprApCommTelnetPolicyOwner,
       "cfprApCommTelnetPort": cfprApCommTelnetPort,
       "cfprApCommTelnetProto": cfprApCommTelnetProto,
       "cfprApCommWebChannelTable": cfprApCommWebChannelTable,
       "cfprApCommWebChannelEntry": cfprApCommWebChannelEntry,
       "cfprApCommWebChannelInstanceId": cfprApCommWebChannelInstanceId,
       "cfprApCommWebChannelDn": cfprApCommWebChannelDn,
       "cfprApCommWebChannelRn": cfprApCommWebChannelRn,
       "cfprApCommWebChannelChannelState": cfprApCommWebChannelChannelState,
       "cfprApCommWebChannelDescr": cfprApCommWebChannelDescr,
       "cfprApCommWebChannelIntId": cfprApCommWebChannelIntId,
       "cfprApCommWebChannelName": cfprApCommWebChannelName,
       "cfprApCommWebChannelPolicyLevel": cfprApCommWebChannelPolicyLevel,
       "cfprApCommWebChannelPolicyOwner": cfprApCommWebChannelPolicyOwner,
       "cfprApCommWebSvcLimitsTable": cfprApCommWebSvcLimitsTable,
       "cfprApCommWebSvcLimitsEntry": cfprApCommWebSvcLimitsEntry,
       "cfprApCommWebSvcLimitsInstanceId": cfprApCommWebSvcLimitsInstanceId,
       "cfprApCommWebSvcLimitsDn": cfprApCommWebSvcLimitsDn,
       "cfprApCommWebSvcLimitsRn": cfprApCommWebSvcLimitsRn,
       "cfprApCommWebSvcLimitsDescr": cfprApCommWebSvcLimitsDescr,
       "cfprApCommWebSvcLimitsIntId": cfprApCommWebSvcLimitsIntId,
       "cfprApCommWebSvcLimitsName": cfprApCommWebSvcLimitsName,
       "cfprApCommWebSvcLimitsPolicyLevel": cfprApCommWebSvcLimitsPolicyLevel,
       "cfprApCommWebSvcLimitsPolicyOwner": cfprApCommWebSvcLimitsPolicyOwner,
       "cfprApCommWebSvcLimitsSessionsPerUser": cfprApCommWebSvcLimitsSessionsPerUser,
       "cfprApCommWebSvcLimitsTotalSessions": cfprApCommWebSvcLimitsTotalSessions,
       "cfprApCommWsmanTable": cfprApCommWsmanTable,
       "cfprApCommWsmanEntry": cfprApCommWsmanEntry,
       "cfprApCommWsmanInstanceId": cfprApCommWsmanInstanceId,
       "cfprApCommWsmanDn": cfprApCommWsmanDn,
       "cfprApCommWsmanRn": cfprApCommWsmanRn,
       "cfprApCommWsmanAdminState": cfprApCommWsmanAdminState,
       "cfprApCommWsmanDescr": cfprApCommWsmanDescr,
       "cfprApCommWsmanIntId": cfprApCommWsmanIntId,
       "cfprApCommWsmanName": cfprApCommWsmanName,
       "cfprApCommWsmanOperPort": cfprApCommWsmanOperPort,
       "cfprApCommWsmanPolicyLevel": cfprApCommWsmanPolicyLevel,
       "cfprApCommWsmanPolicyOwner": cfprApCommWsmanPolicyOwner,
       "cfprApCommWsmanPort": cfprApCommWsmanPort,
       "cfprApCommWsmanProto": cfprApCommWsmanProto}
)
