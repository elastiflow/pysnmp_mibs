# SNMP MIB module (CISCO-FIREPOWER-AP-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-AAA-MIB.mib
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

(CfprApAaaAccess,
 CfprApAaaAccountStatus,
 CfprApAaaAuthRealmFsmCurrentFsm,
 CfprApAaaAuthRealmFsmStageName,
 CfprApAaaCimcSessionType,
 CfprApAaaClear,
 CfprApAaaConfigState,
 CfprApAaaDomainAuthRealm,
 CfprApAaaEpAccess,
 CfprApAaaEpFsmCurrentFsm,
 CfprApAaaEpFsmStageName,
 CfprApAaaEpFsmTaskItem,
 CfprApAaaExtMgmtAccess,
 CfprApAaaIpmiOverLan,
 CfprApAaaLdapEpFsmCurrentFsm,
 CfprApAaaLdapEpFsmStageName,
 CfprApAaaLdapGroupRuleAuthorization,
 CfprApAaaLdapGroupRuleTraversal,
 CfprApAaaLdapVendor,
 CfprApAaaNoRolePolicy,
 CfprApAaaPwdPolicy,
 CfprApAaaRadiusEpFsmCurrentFsm,
 CfprApAaaRadiusEpFsmStageName,
 CfprApAaaRadiusService,
 CfprApAaaRealm,
 CfprApAaaRealmFsmCurrentFsm,
 CfprApAaaRealmFsmStageName,
 CfprApAaaRealmFsmTaskItem,
 CfprApAaaSession,
 CfprApAaaSessionState,
 CfprApAaaSshStr,
 CfprApAaaTacacsPlusEpFsmCurrentFsm,
 CfprApAaaTacacsPlusEpFsmStageName,
 CfprApAaaUserEpFsmCurrentFsm,
 CfprApAaaUserEpFsmStageName,
 CfprApAaaUserEpFsmTaskItem,
 CfprApAaaUserInterface,
 CfprApConditionActionIndicator,
 CfprApConditionCause,
 CfprApConditionCode,
 CfprApConditionRemoteInvRslt,
 CfprApConditionSeverity,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApNetworkSwitchId,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAaaAccess",
    "CfprApAaaAccountStatus",
    "CfprApAaaAuthRealmFsmCurrentFsm",
    "CfprApAaaAuthRealmFsmStageName",
    "CfprApAaaCimcSessionType",
    "CfprApAaaClear",
    "CfprApAaaConfigState",
    "CfprApAaaDomainAuthRealm",
    "CfprApAaaEpAccess",
    "CfprApAaaEpFsmCurrentFsm",
    "CfprApAaaEpFsmStageName",
    "CfprApAaaEpFsmTaskItem",
    "CfprApAaaExtMgmtAccess",
    "CfprApAaaIpmiOverLan",
    "CfprApAaaLdapEpFsmCurrentFsm",
    "CfprApAaaLdapEpFsmStageName",
    "CfprApAaaLdapGroupRuleAuthorization",
    "CfprApAaaLdapGroupRuleTraversal",
    "CfprApAaaLdapVendor",
    "CfprApAaaNoRolePolicy",
    "CfprApAaaPwdPolicy",
    "CfprApAaaRadiusEpFsmCurrentFsm",
    "CfprApAaaRadiusEpFsmStageName",
    "CfprApAaaRadiusService",
    "CfprApAaaRealm",
    "CfprApAaaRealmFsmCurrentFsm",
    "CfprApAaaRealmFsmStageName",
    "CfprApAaaRealmFsmTaskItem",
    "CfprApAaaSession",
    "CfprApAaaSessionState",
    "CfprApAaaSshStr",
    "CfprApAaaTacacsPlusEpFsmCurrentFsm",
    "CfprApAaaTacacsPlusEpFsmStageName",
    "CfprApAaaUserEpFsmCurrentFsm",
    "CfprApAaaUserEpFsmStageName",
    "CfprApAaaUserEpFsmTaskItem",
    "CfprApAaaUserInterface",
    "CfprApConditionActionIndicator",
    "CfprApConditionCause",
    "CfprApConditionCode",
    "CfprApConditionRemoteInvRslt",
    "CfprApConditionSeverity",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApNetworkSwitchId",
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

cfprApAaaObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApAaaAuthRealmTable_Object = MibTable
cfprApAaaAuthRealmTable = _CfprApAaaAuthRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmTable.setStatus("current")
_CfprApAaaAuthRealmEntry_Object = MibTableRow
cfprApAaaAuthRealmEntry = _CfprApAaaAuthRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1)
)
cfprApAaaAuthRealmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaAuthRealmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmEntry.setStatus("current")
_CfprApAaaAuthRealmInstanceId_Type = CfprApManagedObjectId
_CfprApAaaAuthRealmInstanceId_Object = MibTableColumn
cfprApAaaAuthRealmInstanceId = _CfprApAaaAuthRealmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 1),
    _CfprApAaaAuthRealmInstanceId_Type()
)
cfprApAaaAuthRealmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmInstanceId.setStatus("current")
_CfprApAaaAuthRealmDn_Type = CfprApManagedObjectDn
_CfprApAaaAuthRealmDn_Object = MibTableColumn
cfprApAaaAuthRealmDn = _CfprApAaaAuthRealmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 2),
    _CfprApAaaAuthRealmDn_Type()
)
cfprApAaaAuthRealmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmDn.setStatus("current")
_CfprApAaaAuthRealmRn_Type = SnmpAdminString
_CfprApAaaAuthRealmRn_Object = MibTableColumn
cfprApAaaAuthRealmRn = _CfprApAaaAuthRealmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 3),
    _CfprApAaaAuthRealmRn_Type()
)
cfprApAaaAuthRealmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmRn.setStatus("current")
_CfprApAaaAuthRealmConLogin_Type = CfprApAaaRealm
_CfprApAaaAuthRealmConLogin_Object = MibTableColumn
cfprApAaaAuthRealmConLogin = _CfprApAaaAuthRealmConLogin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 4),
    _CfprApAaaAuthRealmConLogin_Type()
)
cfprApAaaAuthRealmConLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmConLogin.setStatus("current")
_CfprApAaaAuthRealmDefLogin_Type = CfprApAaaRealm
_CfprApAaaAuthRealmDefLogin_Object = MibTableColumn
cfprApAaaAuthRealmDefLogin = _CfprApAaaAuthRealmDefLogin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 5),
    _CfprApAaaAuthRealmDefLogin_Type()
)
cfprApAaaAuthRealmDefLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmDefLogin.setStatus("current")
_CfprApAaaAuthRealmDefRolePolicy_Type = CfprApAaaNoRolePolicy
_CfprApAaaAuthRealmDefRolePolicy_Object = MibTableColumn
cfprApAaaAuthRealmDefRolePolicy = _CfprApAaaAuthRealmDefRolePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 6),
    _CfprApAaaAuthRealmDefRolePolicy_Type()
)
cfprApAaaAuthRealmDefRolePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmDefRolePolicy.setStatus("current")
_CfprApAaaAuthRealmDescr_Type = SnmpAdminString
_CfprApAaaAuthRealmDescr_Object = MibTableColumn
cfprApAaaAuthRealmDescr = _CfprApAaaAuthRealmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 7),
    _CfprApAaaAuthRealmDescr_Type()
)
cfprApAaaAuthRealmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmDescr.setStatus("current")
_CfprApAaaAuthRealmFsmDescr_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmDescr_Object = MibTableColumn
cfprApAaaAuthRealmFsmDescr = _CfprApAaaAuthRealmFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 8),
    _CfprApAaaAuthRealmFsmDescr_Type()
)
cfprApAaaAuthRealmFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmDescr.setStatus("current")
_CfprApAaaAuthRealmFsmPrev_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmPrev_Object = MibTableColumn
cfprApAaaAuthRealmFsmPrev = _CfprApAaaAuthRealmFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 9),
    _CfprApAaaAuthRealmFsmPrev_Type()
)
cfprApAaaAuthRealmFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmPrev.setStatus("current")
_CfprApAaaAuthRealmFsmProgr_Type = Gauge32
_CfprApAaaAuthRealmFsmProgr_Object = MibTableColumn
cfprApAaaAuthRealmFsmProgr = _CfprApAaaAuthRealmFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 10),
    _CfprApAaaAuthRealmFsmProgr_Type()
)
cfprApAaaAuthRealmFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmProgr.setStatus("current")
_CfprApAaaAuthRealmFsmRmtInvErrCode_Type = Gauge32
_CfprApAaaAuthRealmFsmRmtInvErrCode_Object = MibTableColumn
cfprApAaaAuthRealmFsmRmtInvErrCode = _CfprApAaaAuthRealmFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 11),
    _CfprApAaaAuthRealmFsmRmtInvErrCode_Type()
)
cfprApAaaAuthRealmFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmRmtInvErrCode.setStatus("current")
_CfprApAaaAuthRealmFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmRmtInvErrDescr_Object = MibTableColumn
cfprApAaaAuthRealmFsmRmtInvErrDescr = _CfprApAaaAuthRealmFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 12),
    _CfprApAaaAuthRealmFsmRmtInvErrDescr_Type()
)
cfprApAaaAuthRealmFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmRmtInvErrDescr.setStatus("current")
_CfprApAaaAuthRealmFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaAuthRealmFsmRmtInvRslt_Object = MibTableColumn
cfprApAaaAuthRealmFsmRmtInvRslt = _CfprApAaaAuthRealmFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 13),
    _CfprApAaaAuthRealmFsmRmtInvRslt_Type()
)
cfprApAaaAuthRealmFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmRmtInvRslt.setStatus("current")
_CfprApAaaAuthRealmFsmStageDescr_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmStageDescr_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageDescr = _CfprApAaaAuthRealmFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 14),
    _CfprApAaaAuthRealmFsmStageDescr_Type()
)
cfprApAaaAuthRealmFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageDescr.setStatus("current")
_CfprApAaaAuthRealmFsmStamp_Type = DateAndTime
_CfprApAaaAuthRealmFsmStamp_Object = MibTableColumn
cfprApAaaAuthRealmFsmStamp = _CfprApAaaAuthRealmFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 15),
    _CfprApAaaAuthRealmFsmStamp_Type()
)
cfprApAaaAuthRealmFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStamp.setStatus("current")
_CfprApAaaAuthRealmFsmStatus_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmStatus_Object = MibTableColumn
cfprApAaaAuthRealmFsmStatus = _CfprApAaaAuthRealmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 16),
    _CfprApAaaAuthRealmFsmStatus_Type()
)
cfprApAaaAuthRealmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStatus.setStatus("current")
_CfprApAaaAuthRealmFsmTry_Type = Gauge32
_CfprApAaaAuthRealmFsmTry_Object = MibTableColumn
cfprApAaaAuthRealmFsmTry = _CfprApAaaAuthRealmFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 17),
    _CfprApAaaAuthRealmFsmTry_Type()
)
cfprApAaaAuthRealmFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmTry.setStatus("current")
_CfprApAaaAuthRealmIntId_Type = SnmpAdminString
_CfprApAaaAuthRealmIntId_Object = MibTableColumn
cfprApAaaAuthRealmIntId = _CfprApAaaAuthRealmIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 18),
    _CfprApAaaAuthRealmIntId_Type()
)
cfprApAaaAuthRealmIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmIntId.setStatus("current")
_CfprApAaaAuthRealmName_Type = SnmpAdminString
_CfprApAaaAuthRealmName_Object = MibTableColumn
cfprApAaaAuthRealmName = _CfprApAaaAuthRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 19),
    _CfprApAaaAuthRealmName_Type()
)
cfprApAaaAuthRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmName.setStatus("current")
_CfprApAaaAuthRealmPolicyLevel_Type = Gauge32
_CfprApAaaAuthRealmPolicyLevel_Object = MibTableColumn
cfprApAaaAuthRealmPolicyLevel = _CfprApAaaAuthRealmPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 20),
    _CfprApAaaAuthRealmPolicyLevel_Type()
)
cfprApAaaAuthRealmPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmPolicyLevel.setStatus("current")
_CfprApAaaAuthRealmPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaAuthRealmPolicyOwner_Object = MibTableColumn
cfprApAaaAuthRealmPolicyOwner = _CfprApAaaAuthRealmPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 1, 1, 21),
    _CfprApAaaAuthRealmPolicyOwner_Type()
)
cfprApAaaAuthRealmPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmPolicyOwner.setStatus("current")
_CfprApAaaAuthRealmFsmTable_Object = MibTable
cfprApAaaAuthRealmFsmTable = _CfprApAaaAuthRealmFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmTable.setStatus("current")
_CfprApAaaAuthRealmFsmEntry_Object = MibTableRow
cfprApAaaAuthRealmFsmEntry = _CfprApAaaAuthRealmFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1)
)
cfprApAaaAuthRealmFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaAuthRealmFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmEntry.setStatus("current")
_CfprApAaaAuthRealmFsmInstanceId_Type = CfprApManagedObjectId
_CfprApAaaAuthRealmFsmInstanceId_Object = MibTableColumn
cfprApAaaAuthRealmFsmInstanceId = _CfprApAaaAuthRealmFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 1),
    _CfprApAaaAuthRealmFsmInstanceId_Type()
)
cfprApAaaAuthRealmFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmInstanceId.setStatus("current")
_CfprApAaaAuthRealmFsmDn_Type = CfprApManagedObjectDn
_CfprApAaaAuthRealmFsmDn_Object = MibTableColumn
cfprApAaaAuthRealmFsmDn = _CfprApAaaAuthRealmFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 2),
    _CfprApAaaAuthRealmFsmDn_Type()
)
cfprApAaaAuthRealmFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmDn.setStatus("current")
_CfprApAaaAuthRealmFsmRn_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmRn_Object = MibTableColumn
cfprApAaaAuthRealmFsmRn = _CfprApAaaAuthRealmFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 3),
    _CfprApAaaAuthRealmFsmRn_Type()
)
cfprApAaaAuthRealmFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmRn.setStatus("current")
_CfprApAaaAuthRealmFsmCompletionTime_Type = DateAndTime
_CfprApAaaAuthRealmFsmCompletionTime_Object = MibTableColumn
cfprApAaaAuthRealmFsmCompletionTime = _CfprApAaaAuthRealmFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 4),
    _CfprApAaaAuthRealmFsmCompletionTime_Type()
)
cfprApAaaAuthRealmFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmCompletionTime.setStatus("current")
_CfprApAaaAuthRealmFsmCurrentFsm_Type = CfprApAaaAuthRealmFsmCurrentFsm
_CfprApAaaAuthRealmFsmCurrentFsm_Object = MibTableColumn
cfprApAaaAuthRealmFsmCurrentFsm = _CfprApAaaAuthRealmFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 5),
    _CfprApAaaAuthRealmFsmCurrentFsm_Type()
)
cfprApAaaAuthRealmFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmCurrentFsm.setStatus("current")
_CfprApAaaAuthRealmFsmDescrData_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmDescrData_Object = MibTableColumn
cfprApAaaAuthRealmFsmDescrData = _CfprApAaaAuthRealmFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 6),
    _CfprApAaaAuthRealmFsmDescrData_Type()
)
cfprApAaaAuthRealmFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmDescrData.setStatus("current")
_CfprApAaaAuthRealmFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaAuthRealmFsmFsmStatus_Object = MibTableColumn
cfprApAaaAuthRealmFsmFsmStatus = _CfprApAaaAuthRealmFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 7),
    _CfprApAaaAuthRealmFsmFsmStatus_Type()
)
cfprApAaaAuthRealmFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmFsmStatus.setStatus("current")
_CfprApAaaAuthRealmFsmProgress_Type = Gauge32
_CfprApAaaAuthRealmFsmProgress_Object = MibTableColumn
cfprApAaaAuthRealmFsmProgress = _CfprApAaaAuthRealmFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 8),
    _CfprApAaaAuthRealmFsmProgress_Type()
)
cfprApAaaAuthRealmFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmProgress.setStatus("current")
_CfprApAaaAuthRealmFsmRmtErrCode_Type = Gauge32
_CfprApAaaAuthRealmFsmRmtErrCode_Object = MibTableColumn
cfprApAaaAuthRealmFsmRmtErrCode = _CfprApAaaAuthRealmFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 9),
    _CfprApAaaAuthRealmFsmRmtErrCode_Type()
)
cfprApAaaAuthRealmFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmRmtErrCode.setStatus("current")
_CfprApAaaAuthRealmFsmRmtErrDescr_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmRmtErrDescr_Object = MibTableColumn
cfprApAaaAuthRealmFsmRmtErrDescr = _CfprApAaaAuthRealmFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 10),
    _CfprApAaaAuthRealmFsmRmtErrDescr_Type()
)
cfprApAaaAuthRealmFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmRmtErrDescr.setStatus("current")
_CfprApAaaAuthRealmFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaAuthRealmFsmRmtRslt_Object = MibTableColumn
cfprApAaaAuthRealmFsmRmtRslt = _CfprApAaaAuthRealmFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 2, 1, 11),
    _CfprApAaaAuthRealmFsmRmtRslt_Type()
)
cfprApAaaAuthRealmFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmRmtRslt.setStatus("current")
_CfprApAaaAuthRealmFsmStageTable_Object = MibTable
cfprApAaaAuthRealmFsmStageTable = _CfprApAaaAuthRealmFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageTable.setStatus("current")
_CfprApAaaAuthRealmFsmStageEntry_Object = MibTableRow
cfprApAaaAuthRealmFsmStageEntry = _CfprApAaaAuthRealmFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1)
)
cfprApAaaAuthRealmFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaAuthRealmFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageEntry.setStatus("current")
_CfprApAaaAuthRealmFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApAaaAuthRealmFsmStageInstanceId_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageInstanceId = _CfprApAaaAuthRealmFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 1),
    _CfprApAaaAuthRealmFsmStageInstanceId_Type()
)
cfprApAaaAuthRealmFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageInstanceId.setStatus("current")
_CfprApAaaAuthRealmFsmStageDn_Type = CfprApManagedObjectDn
_CfprApAaaAuthRealmFsmStageDn_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageDn = _CfprApAaaAuthRealmFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 2),
    _CfprApAaaAuthRealmFsmStageDn_Type()
)
cfprApAaaAuthRealmFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageDn.setStatus("current")
_CfprApAaaAuthRealmFsmStageRn_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmStageRn_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageRn = _CfprApAaaAuthRealmFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 3),
    _CfprApAaaAuthRealmFsmStageRn_Type()
)
cfprApAaaAuthRealmFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageRn.setStatus("current")
_CfprApAaaAuthRealmFsmStageDescrData_Type = SnmpAdminString
_CfprApAaaAuthRealmFsmStageDescrData_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageDescrData = _CfprApAaaAuthRealmFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 4),
    _CfprApAaaAuthRealmFsmStageDescrData_Type()
)
cfprApAaaAuthRealmFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageDescrData.setStatus("current")
_CfprApAaaAuthRealmFsmStageLastUpdateTime_Type = DateAndTime
_CfprApAaaAuthRealmFsmStageLastUpdateTime_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageLastUpdateTime = _CfprApAaaAuthRealmFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 5),
    _CfprApAaaAuthRealmFsmStageLastUpdateTime_Type()
)
cfprApAaaAuthRealmFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageLastUpdateTime.setStatus("current")
_CfprApAaaAuthRealmFsmStageName_Type = CfprApAaaAuthRealmFsmStageName
_CfprApAaaAuthRealmFsmStageName_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageName = _CfprApAaaAuthRealmFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 6),
    _CfprApAaaAuthRealmFsmStageName_Type()
)
cfprApAaaAuthRealmFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageName.setStatus("current")
_CfprApAaaAuthRealmFsmStageOrder_Type = Gauge32
_CfprApAaaAuthRealmFsmStageOrder_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageOrder = _CfprApAaaAuthRealmFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 7),
    _CfprApAaaAuthRealmFsmStageOrder_Type()
)
cfprApAaaAuthRealmFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageOrder.setStatus("current")
_CfprApAaaAuthRealmFsmStageRetry_Type = Gauge32
_CfprApAaaAuthRealmFsmStageRetry_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageRetry = _CfprApAaaAuthRealmFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 8),
    _CfprApAaaAuthRealmFsmStageRetry_Type()
)
cfprApAaaAuthRealmFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageRetry.setStatus("current")
_CfprApAaaAuthRealmFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaAuthRealmFsmStageStageStatus_Object = MibTableColumn
cfprApAaaAuthRealmFsmStageStageStatus = _CfprApAaaAuthRealmFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 3, 1, 9),
    _CfprApAaaAuthRealmFsmStageStageStatus_Type()
)
cfprApAaaAuthRealmFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaAuthRealmFsmStageStageStatus.setStatus("current")
_CfprApAaaCimcSessionTable_Object = MibTable
cfprApAaaCimcSessionTable = _CfprApAaaCimcSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionTable.setStatus("current")
_CfprApAaaCimcSessionEntry_Object = MibTableRow
cfprApAaaCimcSessionEntry = _CfprApAaaCimcSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1)
)
cfprApAaaCimcSessionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaCimcSessionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionEntry.setStatus("current")
_CfprApAaaCimcSessionInstanceId_Type = CfprApManagedObjectId
_CfprApAaaCimcSessionInstanceId_Object = MibTableColumn
cfprApAaaCimcSessionInstanceId = _CfprApAaaCimcSessionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 1),
    _CfprApAaaCimcSessionInstanceId_Type()
)
cfprApAaaCimcSessionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionInstanceId.setStatus("current")
_CfprApAaaCimcSessionDn_Type = CfprApManagedObjectDn
_CfprApAaaCimcSessionDn_Object = MibTableColumn
cfprApAaaCimcSessionDn = _CfprApAaaCimcSessionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 2),
    _CfprApAaaCimcSessionDn_Type()
)
cfprApAaaCimcSessionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionDn.setStatus("current")
_CfprApAaaCimcSessionRn_Type = SnmpAdminString
_CfprApAaaCimcSessionRn_Object = MibTableColumn
cfprApAaaCimcSessionRn = _CfprApAaaCimcSessionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 3),
    _CfprApAaaCimcSessionRn_Type()
)
cfprApAaaCimcSessionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionRn.setStatus("current")
_CfprApAaaCimcSessionAdminState_Type = CfprApAaaSessionState
_CfprApAaaCimcSessionAdminState_Object = MibTableColumn
cfprApAaaCimcSessionAdminState = _CfprApAaaCimcSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 4),
    _CfprApAaaCimcSessionAdminState_Type()
)
cfprApAaaCimcSessionAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionAdminState.setStatus("current")
_CfprApAaaCimcSessionCimcAddr_Type = SnmpAdminString
_CfprApAaaCimcSessionCimcAddr_Object = MibTableColumn
cfprApAaaCimcSessionCimcAddr = _CfprApAaaCimcSessionCimcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 5),
    _CfprApAaaCimcSessionCimcAddr_Type()
)
cfprApAaaCimcSessionCimcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionCimcAddr.setStatus("current")
_CfprApAaaCimcSessionId_Type = SnmpAdminString
_CfprApAaaCimcSessionId_Object = MibTableColumn
cfprApAaaCimcSessionId = _CfprApAaaCimcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 6),
    _CfprApAaaCimcSessionId_Type()
)
cfprApAaaCimcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionId.setStatus("current")
_CfprApAaaCimcSessionIntDel_Type = TruthValue
_CfprApAaaCimcSessionIntDel_Object = MibTableColumn
cfprApAaaCimcSessionIntDel = _CfprApAaaCimcSessionIntDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 7),
    _CfprApAaaCimcSessionIntDel_Type()
)
cfprApAaaCimcSessionIntDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionIntDel.setStatus("current")
_CfprApAaaCimcSessionIsDelete_Type = CfprApAaaClear
_CfprApAaaCimcSessionIsDelete_Object = MibTableColumn
cfprApAaaCimcSessionIsDelete = _CfprApAaaCimcSessionIsDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 8),
    _CfprApAaaCimcSessionIsDelete_Type()
)
cfprApAaaCimcSessionIsDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionIsDelete.setStatus("current")
_CfprApAaaCimcSessionLastUpdatedTime_Type = DateAndTime
_CfprApAaaCimcSessionLastUpdatedTime_Object = MibTableColumn
cfprApAaaCimcSessionLastUpdatedTime = _CfprApAaaCimcSessionLastUpdatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 9),
    _CfprApAaaCimcSessionLastUpdatedTime_Type()
)
cfprApAaaCimcSessionLastUpdatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionLastUpdatedTime.setStatus("current")
_CfprApAaaCimcSessionLoginTime_Type = DateAndTime
_CfprApAaaCimcSessionLoginTime_Object = MibTableColumn
cfprApAaaCimcSessionLoginTime = _CfprApAaaCimcSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 10),
    _CfprApAaaCimcSessionLoginTime_Type()
)
cfprApAaaCimcSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionLoginTime.setStatus("current")
_CfprApAaaCimcSessionLsDn_Type = SnmpAdminString
_CfprApAaaCimcSessionLsDn_Object = MibTableColumn
cfprApAaaCimcSessionLsDn = _CfprApAaaCimcSessionLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 11),
    _CfprApAaaCimcSessionLsDn_Type()
)
cfprApAaaCimcSessionLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionLsDn.setStatus("current")
_CfprApAaaCimcSessionPid_Type = Gauge32
_CfprApAaaCimcSessionPid_Object = MibTableColumn
cfprApAaaCimcSessionPid = _CfprApAaaCimcSessionPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 12),
    _CfprApAaaCimcSessionPid_Type()
)
cfprApAaaCimcSessionPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionPid.setStatus("current")
_CfprApAaaCimcSessionPnDn_Type = SnmpAdminString
_CfprApAaaCimcSessionPnDn_Object = MibTableColumn
cfprApAaaCimcSessionPnDn = _CfprApAaaCimcSessionPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 13),
    _CfprApAaaCimcSessionPnDn_Type()
)
cfprApAaaCimcSessionPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionPnDn.setStatus("current")
_CfprApAaaCimcSessionPriv_Type = SnmpAdminString
_CfprApAaaCimcSessionPriv_Object = MibTableColumn
cfprApAaaCimcSessionPriv = _CfprApAaaCimcSessionPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 14),
    _CfprApAaaCimcSessionPriv_Type()
)
cfprApAaaCimcSessionPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionPriv.setStatus("current")
_CfprApAaaCimcSessionSourceAddr_Type = SnmpAdminString
_CfprApAaaCimcSessionSourceAddr_Object = MibTableColumn
cfprApAaaCimcSessionSourceAddr = _CfprApAaaCimcSessionSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 15),
    _CfprApAaaCimcSessionSourceAddr_Type()
)
cfprApAaaCimcSessionSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionSourceAddr.setStatus("current")
_CfprApAaaCimcSessionType_Type = CfprApAaaCimcSessionType
_CfprApAaaCimcSessionType_Object = MibTableColumn
cfprApAaaCimcSessionType = _CfprApAaaCimcSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 16),
    _CfprApAaaCimcSessionType_Type()
)
cfprApAaaCimcSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionType.setStatus("current")
_CfprApAaaCimcSessionUser_Type = SnmpAdminString
_CfprApAaaCimcSessionUser_Object = MibTableColumn
cfprApAaaCimcSessionUser = _CfprApAaaCimcSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 4, 1, 17),
    _CfprApAaaCimcSessionUser_Type()
)
cfprApAaaCimcSessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaCimcSessionUser.setStatus("current")
_CfprApAaaConsoleAuthTable_Object = MibTable
cfprApAaaConsoleAuthTable = _CfprApAaaConsoleAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthTable.setStatus("current")
_CfprApAaaConsoleAuthEntry_Object = MibTableRow
cfprApAaaConsoleAuthEntry = _CfprApAaaConsoleAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1)
)
cfprApAaaConsoleAuthEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaConsoleAuthInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthEntry.setStatus("current")
_CfprApAaaConsoleAuthInstanceId_Type = CfprApManagedObjectId
_CfprApAaaConsoleAuthInstanceId_Object = MibTableColumn
cfprApAaaConsoleAuthInstanceId = _CfprApAaaConsoleAuthInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 1),
    _CfprApAaaConsoleAuthInstanceId_Type()
)
cfprApAaaConsoleAuthInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthInstanceId.setStatus("current")
_CfprApAaaConsoleAuthDn_Type = CfprApManagedObjectDn
_CfprApAaaConsoleAuthDn_Object = MibTableColumn
cfprApAaaConsoleAuthDn = _CfprApAaaConsoleAuthDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 2),
    _CfprApAaaConsoleAuthDn_Type()
)
cfprApAaaConsoleAuthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthDn.setStatus("current")
_CfprApAaaConsoleAuthRn_Type = SnmpAdminString
_CfprApAaaConsoleAuthRn_Object = MibTableColumn
cfprApAaaConsoleAuthRn = _CfprApAaaConsoleAuthRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 3),
    _CfprApAaaConsoleAuthRn_Type()
)
cfprApAaaConsoleAuthRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthRn.setStatus("current")
_CfprApAaaConsoleAuthDescr_Type = SnmpAdminString
_CfprApAaaConsoleAuthDescr_Object = MibTableColumn
cfprApAaaConsoleAuthDescr = _CfprApAaaConsoleAuthDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 4),
    _CfprApAaaConsoleAuthDescr_Type()
)
cfprApAaaConsoleAuthDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthDescr.setStatus("current")
_CfprApAaaConsoleAuthName_Type = SnmpAdminString
_CfprApAaaConsoleAuthName_Object = MibTableColumn
cfprApAaaConsoleAuthName = _CfprApAaaConsoleAuthName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 5),
    _CfprApAaaConsoleAuthName_Type()
)
cfprApAaaConsoleAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthName.setStatus("current")
_CfprApAaaConsoleAuthOperProviderGroup_Type = SnmpAdminString
_CfprApAaaConsoleAuthOperProviderGroup_Object = MibTableColumn
cfprApAaaConsoleAuthOperProviderGroup = _CfprApAaaConsoleAuthOperProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 6),
    _CfprApAaaConsoleAuthOperProviderGroup_Type()
)
cfprApAaaConsoleAuthOperProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthOperProviderGroup.setStatus("current")
_CfprApAaaConsoleAuthOperRealm_Type = CfprApAaaRealm
_CfprApAaaConsoleAuthOperRealm_Object = MibTableColumn
cfprApAaaConsoleAuthOperRealm = _CfprApAaaConsoleAuthOperRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 7),
    _CfprApAaaConsoleAuthOperRealm_Type()
)
cfprApAaaConsoleAuthOperRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthOperRealm.setStatus("current")
_CfprApAaaConsoleAuthProviderGroup_Type = SnmpAdminString
_CfprApAaaConsoleAuthProviderGroup_Object = MibTableColumn
cfprApAaaConsoleAuthProviderGroup = _CfprApAaaConsoleAuthProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 8),
    _CfprApAaaConsoleAuthProviderGroup_Type()
)
cfprApAaaConsoleAuthProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthProviderGroup.setStatus("current")
_CfprApAaaConsoleAuthRealm_Type = CfprApAaaRealm
_CfprApAaaConsoleAuthRealm_Object = MibTableColumn
cfprApAaaConsoleAuthRealm = _CfprApAaaConsoleAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 9),
    _CfprApAaaConsoleAuthRealm_Type()
)
cfprApAaaConsoleAuthRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthRealm.setStatus("current")
_CfprApAaaConsoleAuthUse2Factor_Type = TruthValue
_CfprApAaaConsoleAuthUse2Factor_Object = MibTableColumn
cfprApAaaConsoleAuthUse2Factor = _CfprApAaaConsoleAuthUse2Factor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 5, 1, 10),
    _CfprApAaaConsoleAuthUse2Factor_Type()
)
cfprApAaaConsoleAuthUse2Factor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaConsoleAuthUse2Factor.setStatus("current")
_CfprApAaaDefaultAuthTable_Object = MibTable
cfprApAaaDefaultAuthTable = _CfprApAaaDefaultAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthTable.setStatus("current")
_CfprApAaaDefaultAuthEntry_Object = MibTableRow
cfprApAaaDefaultAuthEntry = _CfprApAaaDefaultAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1)
)
cfprApAaaDefaultAuthEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaDefaultAuthInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthEntry.setStatus("current")
_CfprApAaaDefaultAuthInstanceId_Type = CfprApManagedObjectId
_CfprApAaaDefaultAuthInstanceId_Object = MibTableColumn
cfprApAaaDefaultAuthInstanceId = _CfprApAaaDefaultAuthInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 1),
    _CfprApAaaDefaultAuthInstanceId_Type()
)
cfprApAaaDefaultAuthInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthInstanceId.setStatus("current")
_CfprApAaaDefaultAuthDn_Type = CfprApManagedObjectDn
_CfprApAaaDefaultAuthDn_Object = MibTableColumn
cfprApAaaDefaultAuthDn = _CfprApAaaDefaultAuthDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 2),
    _CfprApAaaDefaultAuthDn_Type()
)
cfprApAaaDefaultAuthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthDn.setStatus("current")
_CfprApAaaDefaultAuthRn_Type = SnmpAdminString
_CfprApAaaDefaultAuthRn_Object = MibTableColumn
cfprApAaaDefaultAuthRn = _CfprApAaaDefaultAuthRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 3),
    _CfprApAaaDefaultAuthRn_Type()
)
cfprApAaaDefaultAuthRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthRn.setStatus("current")
_CfprApAaaDefaultAuthDescr_Type = SnmpAdminString
_CfprApAaaDefaultAuthDescr_Object = MibTableColumn
cfprApAaaDefaultAuthDescr = _CfprApAaaDefaultAuthDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 4),
    _CfprApAaaDefaultAuthDescr_Type()
)
cfprApAaaDefaultAuthDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthDescr.setStatus("current")
_CfprApAaaDefaultAuthName_Type = SnmpAdminString
_CfprApAaaDefaultAuthName_Object = MibTableColumn
cfprApAaaDefaultAuthName = _CfprApAaaDefaultAuthName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 5),
    _CfprApAaaDefaultAuthName_Type()
)
cfprApAaaDefaultAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthName.setStatus("current")
_CfprApAaaDefaultAuthOperProviderGroup_Type = SnmpAdminString
_CfprApAaaDefaultAuthOperProviderGroup_Object = MibTableColumn
cfprApAaaDefaultAuthOperProviderGroup = _CfprApAaaDefaultAuthOperProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 6),
    _CfprApAaaDefaultAuthOperProviderGroup_Type()
)
cfprApAaaDefaultAuthOperProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthOperProviderGroup.setStatus("current")
_CfprApAaaDefaultAuthOperRealm_Type = CfprApAaaRealm
_CfprApAaaDefaultAuthOperRealm_Object = MibTableColumn
cfprApAaaDefaultAuthOperRealm = _CfprApAaaDefaultAuthOperRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 7),
    _CfprApAaaDefaultAuthOperRealm_Type()
)
cfprApAaaDefaultAuthOperRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthOperRealm.setStatus("current")
_CfprApAaaDefaultAuthProviderGroup_Type = SnmpAdminString
_CfprApAaaDefaultAuthProviderGroup_Object = MibTableColumn
cfprApAaaDefaultAuthProviderGroup = _CfprApAaaDefaultAuthProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 8),
    _CfprApAaaDefaultAuthProviderGroup_Type()
)
cfprApAaaDefaultAuthProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthProviderGroup.setStatus("current")
_CfprApAaaDefaultAuthRealm_Type = CfprApAaaRealm
_CfprApAaaDefaultAuthRealm_Object = MibTableColumn
cfprApAaaDefaultAuthRealm = _CfprApAaaDefaultAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 9),
    _CfprApAaaDefaultAuthRealm_Type()
)
cfprApAaaDefaultAuthRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthRealm.setStatus("current")
_CfprApAaaDefaultAuthRefreshPeriod_Type = Gauge32
_CfprApAaaDefaultAuthRefreshPeriod_Object = MibTableColumn
cfprApAaaDefaultAuthRefreshPeriod = _CfprApAaaDefaultAuthRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 10),
    _CfprApAaaDefaultAuthRefreshPeriod_Type()
)
cfprApAaaDefaultAuthRefreshPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthRefreshPeriod.setStatus("current")
_CfprApAaaDefaultAuthSessionTimeout_Type = Gauge32
_CfprApAaaDefaultAuthSessionTimeout_Object = MibTableColumn
cfprApAaaDefaultAuthSessionTimeout = _CfprApAaaDefaultAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 11),
    _CfprApAaaDefaultAuthSessionTimeout_Type()
)
cfprApAaaDefaultAuthSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthSessionTimeout.setStatus("current")
_CfprApAaaDefaultAuthUse2Factor_Type = TruthValue
_CfprApAaaDefaultAuthUse2Factor_Object = MibTableColumn
cfprApAaaDefaultAuthUse2Factor = _CfprApAaaDefaultAuthUse2Factor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 6, 1, 12),
    _CfprApAaaDefaultAuthUse2Factor_Type()
)
cfprApAaaDefaultAuthUse2Factor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDefaultAuthUse2Factor.setStatus("current")
_CfprApAaaDomainTable_Object = MibTable
cfprApAaaDomainTable = _CfprApAaaDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cfprApAaaDomainTable.setStatus("current")
_CfprApAaaDomainEntry_Object = MibTableRow
cfprApAaaDomainEntry = _CfprApAaaDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7, 1)
)
cfprApAaaDomainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaDomainEntry.setStatus("current")
_CfprApAaaDomainInstanceId_Type = CfprApManagedObjectId
_CfprApAaaDomainInstanceId_Object = MibTableColumn
cfprApAaaDomainInstanceId = _CfprApAaaDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7, 1, 1),
    _CfprApAaaDomainInstanceId_Type()
)
cfprApAaaDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaDomainInstanceId.setStatus("current")
_CfprApAaaDomainDn_Type = CfprApManagedObjectDn
_CfprApAaaDomainDn_Object = MibTableColumn
cfprApAaaDomainDn = _CfprApAaaDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7, 1, 2),
    _CfprApAaaDomainDn_Type()
)
cfprApAaaDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainDn.setStatus("current")
_CfprApAaaDomainRn_Type = SnmpAdminString
_CfprApAaaDomainRn_Object = MibTableColumn
cfprApAaaDomainRn = _CfprApAaaDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7, 1, 3),
    _CfprApAaaDomainRn_Type()
)
cfprApAaaDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainRn.setStatus("current")
_CfprApAaaDomainDescr_Type = SnmpAdminString
_CfprApAaaDomainDescr_Object = MibTableColumn
cfprApAaaDomainDescr = _CfprApAaaDomainDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7, 1, 4),
    _CfprApAaaDomainDescr_Type()
)
cfprApAaaDomainDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainDescr.setStatus("current")
_CfprApAaaDomainName_Type = SnmpAdminString
_CfprApAaaDomainName_Object = MibTableColumn
cfprApAaaDomainName = _CfprApAaaDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7, 1, 5),
    _CfprApAaaDomainName_Type()
)
cfprApAaaDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainName.setStatus("current")
_CfprApAaaDomainRefreshPeriod_Type = Gauge32
_CfprApAaaDomainRefreshPeriod_Object = MibTableColumn
cfprApAaaDomainRefreshPeriod = _CfprApAaaDomainRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7, 1, 6),
    _CfprApAaaDomainRefreshPeriod_Type()
)
cfprApAaaDomainRefreshPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainRefreshPeriod.setStatus("current")
_CfprApAaaDomainSessionTimeout_Type = Gauge32
_CfprApAaaDomainSessionTimeout_Object = MibTableColumn
cfprApAaaDomainSessionTimeout = _CfprApAaaDomainSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 7, 1, 7),
    _CfprApAaaDomainSessionTimeout_Type()
)
cfprApAaaDomainSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainSessionTimeout.setStatus("current")
_CfprApAaaDomainAuthTable_Object = MibTable
cfprApAaaDomainAuthTable = _CfprApAaaDomainAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthTable.setStatus("current")
_CfprApAaaDomainAuthEntry_Object = MibTableRow
cfprApAaaDomainAuthEntry = _CfprApAaaDomainAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1)
)
cfprApAaaDomainAuthEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaDomainAuthInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthEntry.setStatus("current")
_CfprApAaaDomainAuthInstanceId_Type = CfprApManagedObjectId
_CfprApAaaDomainAuthInstanceId_Object = MibTableColumn
cfprApAaaDomainAuthInstanceId = _CfprApAaaDomainAuthInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 1),
    _CfprApAaaDomainAuthInstanceId_Type()
)
cfprApAaaDomainAuthInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthInstanceId.setStatus("current")
_CfprApAaaDomainAuthDn_Type = CfprApManagedObjectDn
_CfprApAaaDomainAuthDn_Object = MibTableColumn
cfprApAaaDomainAuthDn = _CfprApAaaDomainAuthDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 2),
    _CfprApAaaDomainAuthDn_Type()
)
cfprApAaaDomainAuthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthDn.setStatus("current")
_CfprApAaaDomainAuthRn_Type = SnmpAdminString
_CfprApAaaDomainAuthRn_Object = MibTableColumn
cfprApAaaDomainAuthRn = _CfprApAaaDomainAuthRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 3),
    _CfprApAaaDomainAuthRn_Type()
)
cfprApAaaDomainAuthRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthRn.setStatus("current")
_CfprApAaaDomainAuthDescr_Type = SnmpAdminString
_CfprApAaaDomainAuthDescr_Object = MibTableColumn
cfprApAaaDomainAuthDescr = _CfprApAaaDomainAuthDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 4),
    _CfprApAaaDomainAuthDescr_Type()
)
cfprApAaaDomainAuthDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthDescr.setStatus("current")
_CfprApAaaDomainAuthName_Type = SnmpAdminString
_CfprApAaaDomainAuthName_Object = MibTableColumn
cfprApAaaDomainAuthName = _CfprApAaaDomainAuthName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 5),
    _CfprApAaaDomainAuthName_Type()
)
cfprApAaaDomainAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthName.setStatus("current")
_CfprApAaaDomainAuthOperProviderGroup_Type = SnmpAdminString
_CfprApAaaDomainAuthOperProviderGroup_Object = MibTableColumn
cfprApAaaDomainAuthOperProviderGroup = _CfprApAaaDomainAuthOperProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 6),
    _CfprApAaaDomainAuthOperProviderGroup_Type()
)
cfprApAaaDomainAuthOperProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthOperProviderGroup.setStatus("current")
_CfprApAaaDomainAuthOperRealm_Type = CfprApAaaRealm
_CfprApAaaDomainAuthOperRealm_Object = MibTableColumn
cfprApAaaDomainAuthOperRealm = _CfprApAaaDomainAuthOperRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 7),
    _CfprApAaaDomainAuthOperRealm_Type()
)
cfprApAaaDomainAuthOperRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthOperRealm.setStatus("current")
_CfprApAaaDomainAuthProviderGroup_Type = SnmpAdminString
_CfprApAaaDomainAuthProviderGroup_Object = MibTableColumn
cfprApAaaDomainAuthProviderGroup = _CfprApAaaDomainAuthProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 8),
    _CfprApAaaDomainAuthProviderGroup_Type()
)
cfprApAaaDomainAuthProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthProviderGroup.setStatus("current")
_CfprApAaaDomainAuthRealm_Type = CfprApAaaDomainAuthRealm
_CfprApAaaDomainAuthRealm_Object = MibTableColumn
cfprApAaaDomainAuthRealm = _CfprApAaaDomainAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 9),
    _CfprApAaaDomainAuthRealm_Type()
)
cfprApAaaDomainAuthRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthRealm.setStatus("current")
_CfprApAaaDomainAuthUse2Factor_Type = TruthValue
_CfprApAaaDomainAuthUse2Factor_Object = MibTableColumn
cfprApAaaDomainAuthUse2Factor = _CfprApAaaDomainAuthUse2Factor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 8, 1, 10),
    _CfprApAaaDomainAuthUse2Factor_Type()
)
cfprApAaaDomainAuthUse2Factor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaDomainAuthUse2Factor.setStatus("current")
_CfprApAaaEpAuthProfileTable_Object = MibTable
cfprApAaaEpAuthProfileTable = _CfprApAaaEpAuthProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileTable.setStatus("current")
_CfprApAaaEpAuthProfileEntry_Object = MibTableRow
cfprApAaaEpAuthProfileEntry = _CfprApAaaEpAuthProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1)
)
cfprApAaaEpAuthProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaEpAuthProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileEntry.setStatus("current")
_CfprApAaaEpAuthProfileInstanceId_Type = CfprApManagedObjectId
_CfprApAaaEpAuthProfileInstanceId_Object = MibTableColumn
cfprApAaaEpAuthProfileInstanceId = _CfprApAaaEpAuthProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 1),
    _CfprApAaaEpAuthProfileInstanceId_Type()
)
cfprApAaaEpAuthProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileInstanceId.setStatus("current")
_CfprApAaaEpAuthProfileDn_Type = CfprApManagedObjectDn
_CfprApAaaEpAuthProfileDn_Object = MibTableColumn
cfprApAaaEpAuthProfileDn = _CfprApAaaEpAuthProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 2),
    _CfprApAaaEpAuthProfileDn_Type()
)
cfprApAaaEpAuthProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileDn.setStatus("current")
_CfprApAaaEpAuthProfileRn_Type = SnmpAdminString
_CfprApAaaEpAuthProfileRn_Object = MibTableColumn
cfprApAaaEpAuthProfileRn = _CfprApAaaEpAuthProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 3),
    _CfprApAaaEpAuthProfileRn_Type()
)
cfprApAaaEpAuthProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileRn.setStatus("current")
_CfprApAaaEpAuthProfileDescr_Type = SnmpAdminString
_CfprApAaaEpAuthProfileDescr_Object = MibTableColumn
cfprApAaaEpAuthProfileDescr = _CfprApAaaEpAuthProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 4),
    _CfprApAaaEpAuthProfileDescr_Type()
)
cfprApAaaEpAuthProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileDescr.setStatus("current")
_CfprApAaaEpAuthProfileIntId_Type = SnmpAdminString
_CfprApAaaEpAuthProfileIntId_Object = MibTableColumn
cfprApAaaEpAuthProfileIntId = _CfprApAaaEpAuthProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 5),
    _CfprApAaaEpAuthProfileIntId_Type()
)
cfprApAaaEpAuthProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileIntId.setStatus("current")
_CfprApAaaEpAuthProfileIpmiOverLan_Type = CfprApAaaIpmiOverLan
_CfprApAaaEpAuthProfileIpmiOverLan_Object = MibTableColumn
cfprApAaaEpAuthProfileIpmiOverLan = _CfprApAaaEpAuthProfileIpmiOverLan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 6),
    _CfprApAaaEpAuthProfileIpmiOverLan_Type()
)
cfprApAaaEpAuthProfileIpmiOverLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileIpmiOverLan.setStatus("current")
_CfprApAaaEpAuthProfileName_Type = SnmpAdminString
_CfprApAaaEpAuthProfileName_Object = MibTableColumn
cfprApAaaEpAuthProfileName = _CfprApAaaEpAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 7),
    _CfprApAaaEpAuthProfileName_Type()
)
cfprApAaaEpAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfileName.setStatus("current")
_CfprApAaaEpAuthProfilePolicyLevel_Type = Gauge32
_CfprApAaaEpAuthProfilePolicyLevel_Object = MibTableColumn
cfprApAaaEpAuthProfilePolicyLevel = _CfprApAaaEpAuthProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 8),
    _CfprApAaaEpAuthProfilePolicyLevel_Type()
)
cfprApAaaEpAuthProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfilePolicyLevel.setStatus("current")
_CfprApAaaEpAuthProfilePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaEpAuthProfilePolicyOwner_Object = MibTableColumn
cfprApAaaEpAuthProfilePolicyOwner = _CfprApAaaEpAuthProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 9, 1, 9),
    _CfprApAaaEpAuthProfilePolicyOwner_Type()
)
cfprApAaaEpAuthProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpAuthProfilePolicyOwner.setStatus("current")
_CfprApAaaEpFsmTable_Object = MibTable
cfprApAaaEpFsmTable = _CfprApAaaEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTable.setStatus("current")
_CfprApAaaEpFsmEntry_Object = MibTableRow
cfprApAaaEpFsmEntry = _CfprApAaaEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1)
)
cfprApAaaEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaEpFsmEntry.setStatus("current")
_CfprApAaaEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApAaaEpFsmInstanceId_Object = MibTableColumn
cfprApAaaEpFsmInstanceId = _CfprApAaaEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 1),
    _CfprApAaaEpFsmInstanceId_Type()
)
cfprApAaaEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmInstanceId.setStatus("current")
_CfprApAaaEpFsmDn_Type = CfprApManagedObjectDn
_CfprApAaaEpFsmDn_Object = MibTableColumn
cfprApAaaEpFsmDn = _CfprApAaaEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 2),
    _CfprApAaaEpFsmDn_Type()
)
cfprApAaaEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmDn.setStatus("current")
_CfprApAaaEpFsmRn_Type = SnmpAdminString
_CfprApAaaEpFsmRn_Object = MibTableColumn
cfprApAaaEpFsmRn = _CfprApAaaEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 3),
    _CfprApAaaEpFsmRn_Type()
)
cfprApAaaEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmRn.setStatus("current")
_CfprApAaaEpFsmCompletionTime_Type = DateAndTime
_CfprApAaaEpFsmCompletionTime_Object = MibTableColumn
cfprApAaaEpFsmCompletionTime = _CfprApAaaEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 4),
    _CfprApAaaEpFsmCompletionTime_Type()
)
cfprApAaaEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmCompletionTime.setStatus("current")
_CfprApAaaEpFsmCurrentFsm_Type = CfprApAaaEpFsmCurrentFsm
_CfprApAaaEpFsmCurrentFsm_Object = MibTableColumn
cfprApAaaEpFsmCurrentFsm = _CfprApAaaEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 5),
    _CfprApAaaEpFsmCurrentFsm_Type()
)
cfprApAaaEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmCurrentFsm.setStatus("current")
_CfprApAaaEpFsmDescr_Type = SnmpAdminString
_CfprApAaaEpFsmDescr_Object = MibTableColumn
cfprApAaaEpFsmDescr = _CfprApAaaEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 6),
    _CfprApAaaEpFsmDescr_Type()
)
cfprApAaaEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmDescr.setStatus("current")
_CfprApAaaEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaEpFsmFsmStatus_Object = MibTableColumn
cfprApAaaEpFsmFsmStatus = _CfprApAaaEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 7),
    _CfprApAaaEpFsmFsmStatus_Type()
)
cfprApAaaEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmFsmStatus.setStatus("current")
_CfprApAaaEpFsmProgress_Type = Gauge32
_CfprApAaaEpFsmProgress_Object = MibTableColumn
cfprApAaaEpFsmProgress = _CfprApAaaEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 8),
    _CfprApAaaEpFsmProgress_Type()
)
cfprApAaaEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmProgress.setStatus("current")
_CfprApAaaEpFsmRmtErrCode_Type = Gauge32
_CfprApAaaEpFsmRmtErrCode_Object = MibTableColumn
cfprApAaaEpFsmRmtErrCode = _CfprApAaaEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 9),
    _CfprApAaaEpFsmRmtErrCode_Type()
)
cfprApAaaEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmRmtErrCode.setStatus("current")
_CfprApAaaEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApAaaEpFsmRmtErrDescr_Object = MibTableColumn
cfprApAaaEpFsmRmtErrDescr = _CfprApAaaEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 10),
    _CfprApAaaEpFsmRmtErrDescr_Type()
)
cfprApAaaEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmRmtErrDescr.setStatus("current")
_CfprApAaaEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaEpFsmRmtRslt_Object = MibTableColumn
cfprApAaaEpFsmRmtRslt = _CfprApAaaEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 10, 1, 11),
    _CfprApAaaEpFsmRmtRslt_Type()
)
cfprApAaaEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmRmtRslt.setStatus("current")
_CfprApAaaEpFsmStageTable_Object = MibTable
cfprApAaaEpFsmStageTable = _CfprApAaaEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageTable.setStatus("current")
_CfprApAaaEpFsmStageEntry_Object = MibTableRow
cfprApAaaEpFsmStageEntry = _CfprApAaaEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1)
)
cfprApAaaEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageEntry.setStatus("current")
_CfprApAaaEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApAaaEpFsmStageInstanceId_Object = MibTableColumn
cfprApAaaEpFsmStageInstanceId = _CfprApAaaEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 1),
    _CfprApAaaEpFsmStageInstanceId_Type()
)
cfprApAaaEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageInstanceId.setStatus("current")
_CfprApAaaEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApAaaEpFsmStageDn_Object = MibTableColumn
cfprApAaaEpFsmStageDn = _CfprApAaaEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 2),
    _CfprApAaaEpFsmStageDn_Type()
)
cfprApAaaEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageDn.setStatus("current")
_CfprApAaaEpFsmStageRn_Type = SnmpAdminString
_CfprApAaaEpFsmStageRn_Object = MibTableColumn
cfprApAaaEpFsmStageRn = _CfprApAaaEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 3),
    _CfprApAaaEpFsmStageRn_Type()
)
cfprApAaaEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageRn.setStatus("current")
_CfprApAaaEpFsmStageDescr_Type = SnmpAdminString
_CfprApAaaEpFsmStageDescr_Object = MibTableColumn
cfprApAaaEpFsmStageDescr = _CfprApAaaEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 4),
    _CfprApAaaEpFsmStageDescr_Type()
)
cfprApAaaEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageDescr.setStatus("current")
_CfprApAaaEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApAaaEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApAaaEpFsmStageLastUpdateTime = _CfprApAaaEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 5),
    _CfprApAaaEpFsmStageLastUpdateTime_Type()
)
cfprApAaaEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageLastUpdateTime.setStatus("current")
_CfprApAaaEpFsmStageName_Type = CfprApAaaEpFsmStageName
_CfprApAaaEpFsmStageName_Object = MibTableColumn
cfprApAaaEpFsmStageName = _CfprApAaaEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 6),
    _CfprApAaaEpFsmStageName_Type()
)
cfprApAaaEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageName.setStatus("current")
_CfprApAaaEpFsmStageOrder_Type = Gauge32
_CfprApAaaEpFsmStageOrder_Object = MibTableColumn
cfprApAaaEpFsmStageOrder = _CfprApAaaEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 7),
    _CfprApAaaEpFsmStageOrder_Type()
)
cfprApAaaEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageOrder.setStatus("current")
_CfprApAaaEpFsmStageRetry_Type = Gauge32
_CfprApAaaEpFsmStageRetry_Object = MibTableColumn
cfprApAaaEpFsmStageRetry = _CfprApAaaEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 8),
    _CfprApAaaEpFsmStageRetry_Type()
)
cfprApAaaEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageRetry.setStatus("current")
_CfprApAaaEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaEpFsmStageStageStatus_Object = MibTableColumn
cfprApAaaEpFsmStageStageStatus = _CfprApAaaEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 11, 1, 9),
    _CfprApAaaEpFsmStageStageStatus_Type()
)
cfprApAaaEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmStageStageStatus.setStatus("current")
_CfprApAaaEpFsmTaskTable_Object = MibTable
cfprApAaaEpFsmTaskTable = _CfprApAaaEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskTable.setStatus("current")
_CfprApAaaEpFsmTaskEntry_Object = MibTableRow
cfprApAaaEpFsmTaskEntry = _CfprApAaaEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12, 1)
)
cfprApAaaEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskEntry.setStatus("current")
_CfprApAaaEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApAaaEpFsmTaskInstanceId_Object = MibTableColumn
cfprApAaaEpFsmTaskInstanceId = _CfprApAaaEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12, 1, 1),
    _CfprApAaaEpFsmTaskInstanceId_Type()
)
cfprApAaaEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskInstanceId.setStatus("current")
_CfprApAaaEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApAaaEpFsmTaskDn_Object = MibTableColumn
cfprApAaaEpFsmTaskDn = _CfprApAaaEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12, 1, 2),
    _CfprApAaaEpFsmTaskDn_Type()
)
cfprApAaaEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskDn.setStatus("current")
_CfprApAaaEpFsmTaskRn_Type = SnmpAdminString
_CfprApAaaEpFsmTaskRn_Object = MibTableColumn
cfprApAaaEpFsmTaskRn = _CfprApAaaEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12, 1, 3),
    _CfprApAaaEpFsmTaskRn_Type()
)
cfprApAaaEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskRn.setStatus("current")
_CfprApAaaEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApAaaEpFsmTaskCompletion_Object = MibTableColumn
cfprApAaaEpFsmTaskCompletion = _CfprApAaaEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12, 1, 4),
    _CfprApAaaEpFsmTaskCompletion_Type()
)
cfprApAaaEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskCompletion.setStatus("current")
_CfprApAaaEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApAaaEpFsmTaskFlags_Object = MibTableColumn
cfprApAaaEpFsmTaskFlags = _CfprApAaaEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12, 1, 5),
    _CfprApAaaEpFsmTaskFlags_Type()
)
cfprApAaaEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskFlags.setStatus("current")
_CfprApAaaEpFsmTaskItem_Type = CfprApAaaEpFsmTaskItem
_CfprApAaaEpFsmTaskItem_Object = MibTableColumn
cfprApAaaEpFsmTaskItem = _CfprApAaaEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12, 1, 6),
    _CfprApAaaEpFsmTaskItem_Type()
)
cfprApAaaEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskItem.setStatus("current")
_CfprApAaaEpFsmTaskSeqId_Type = Gauge32
_CfprApAaaEpFsmTaskSeqId_Object = MibTableColumn
cfprApAaaEpFsmTaskSeqId = _CfprApAaaEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 12, 1, 7),
    _CfprApAaaEpFsmTaskSeqId_Type()
)
cfprApAaaEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpFsmTaskSeqId.setStatus("current")
_CfprApAaaEpLoginTable_Object = MibTable
cfprApAaaEpLoginTable = _CfprApAaaEpLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cfprApAaaEpLoginTable.setStatus("current")
_CfprApAaaEpLoginEntry_Object = MibTableRow
cfprApAaaEpLoginEntry = _CfprApAaaEpLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1)
)
cfprApAaaEpLoginEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaEpLoginInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaEpLoginEntry.setStatus("current")
_CfprApAaaEpLoginInstanceId_Type = CfprApManagedObjectId
_CfprApAaaEpLoginInstanceId_Object = MibTableColumn
cfprApAaaEpLoginInstanceId = _CfprApAaaEpLoginInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 1),
    _CfprApAaaEpLoginInstanceId_Type()
)
cfprApAaaEpLoginInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginInstanceId.setStatus("current")
_CfprApAaaEpLoginDn_Type = CfprApManagedObjectDn
_CfprApAaaEpLoginDn_Object = MibTableColumn
cfprApAaaEpLoginDn = _CfprApAaaEpLoginDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 2),
    _CfprApAaaEpLoginDn_Type()
)
cfprApAaaEpLoginDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginDn.setStatus("current")
_CfprApAaaEpLoginRn_Type = SnmpAdminString
_CfprApAaaEpLoginRn_Object = MibTableColumn
cfprApAaaEpLoginRn = _CfprApAaaEpLoginRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 3),
    _CfprApAaaEpLoginRn_Type()
)
cfprApAaaEpLoginRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginRn.setStatus("current")
_CfprApAaaEpLoginDescr_Type = SnmpAdminString
_CfprApAaaEpLoginDescr_Object = MibTableColumn
cfprApAaaEpLoginDescr = _CfprApAaaEpLoginDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 4),
    _CfprApAaaEpLoginDescr_Type()
)
cfprApAaaEpLoginDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginDescr.setStatus("current")
_CfprApAaaEpLoginId_Type = SnmpAdminString
_CfprApAaaEpLoginId_Object = MibTableColumn
cfprApAaaEpLoginId = _CfprApAaaEpLoginId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 5),
    _CfprApAaaEpLoginId_Type()
)
cfprApAaaEpLoginId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginId.setStatus("current")
_CfprApAaaEpLoginIntId_Type = SnmpAdminString
_CfprApAaaEpLoginIntId_Object = MibTableColumn
cfprApAaaEpLoginIntId = _CfprApAaaEpLoginIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 6),
    _CfprApAaaEpLoginIntId_Type()
)
cfprApAaaEpLoginIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginIntId.setStatus("current")
_CfprApAaaEpLoginLocalHost_Type = SnmpAdminString
_CfprApAaaEpLoginLocalHost_Object = MibTableColumn
cfprApAaaEpLoginLocalHost = _CfprApAaaEpLoginLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 7),
    _CfprApAaaEpLoginLocalHost_Type()
)
cfprApAaaEpLoginLocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginLocalHost.setStatus("current")
_CfprApAaaEpLoginName_Type = SnmpAdminString
_CfprApAaaEpLoginName_Object = MibTableColumn
cfprApAaaEpLoginName = _CfprApAaaEpLoginName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 8),
    _CfprApAaaEpLoginName_Type()
)
cfprApAaaEpLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginName.setStatus("current")
_CfprApAaaEpLoginPolicyLevel_Type = Gauge32
_CfprApAaaEpLoginPolicyLevel_Object = MibTableColumn
cfprApAaaEpLoginPolicyLevel = _CfprApAaaEpLoginPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 9),
    _CfprApAaaEpLoginPolicyLevel_Type()
)
cfprApAaaEpLoginPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginPolicyLevel.setStatus("current")
_CfprApAaaEpLoginPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaEpLoginPolicyOwner_Object = MibTableColumn
cfprApAaaEpLoginPolicyOwner = _CfprApAaaEpLoginPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 10),
    _CfprApAaaEpLoginPolicyOwner_Type()
)
cfprApAaaEpLoginPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginPolicyOwner.setStatus("current")
_CfprApAaaEpLoginRemoteHost_Type = SnmpAdminString
_CfprApAaaEpLoginRemoteHost_Object = MibTableColumn
cfprApAaaEpLoginRemoteHost = _CfprApAaaEpLoginRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 11),
    _CfprApAaaEpLoginRemoteHost_Type()
)
cfprApAaaEpLoginRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginRemoteHost.setStatus("current")
_CfprApAaaEpLoginSession_Type = CfprApAaaSession
_CfprApAaaEpLoginSession_Object = MibTableColumn
cfprApAaaEpLoginSession = _CfprApAaaEpLoginSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 12),
    _CfprApAaaEpLoginSession_Type()
)
cfprApAaaEpLoginSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginSession.setStatus("current")
_CfprApAaaEpLoginSwitchId_Type = CfprApNetworkSwitchId
_CfprApAaaEpLoginSwitchId_Object = MibTableColumn
cfprApAaaEpLoginSwitchId = _CfprApAaaEpLoginSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 13, 1, 13),
    _CfprApAaaEpLoginSwitchId_Type()
)
cfprApAaaEpLoginSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpLoginSwitchId.setStatus("current")
_CfprApAaaEpUserTable_Object = MibTable
cfprApAaaEpUserTable = _CfprApAaaEpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cfprApAaaEpUserTable.setStatus("current")
_CfprApAaaEpUserEntry_Object = MibTableRow
cfprApAaaEpUserEntry = _CfprApAaaEpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1)
)
cfprApAaaEpUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaEpUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaEpUserEntry.setStatus("current")
_CfprApAaaEpUserInstanceId_Type = CfprApManagedObjectId
_CfprApAaaEpUserInstanceId_Object = MibTableColumn
cfprApAaaEpUserInstanceId = _CfprApAaaEpUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 1),
    _CfprApAaaEpUserInstanceId_Type()
)
cfprApAaaEpUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaEpUserInstanceId.setStatus("current")
_CfprApAaaEpUserDn_Type = CfprApManagedObjectDn
_CfprApAaaEpUserDn_Object = MibTableColumn
cfprApAaaEpUserDn = _CfprApAaaEpUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 2),
    _CfprApAaaEpUserDn_Type()
)
cfprApAaaEpUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserDn.setStatus("current")
_CfprApAaaEpUserRn_Type = SnmpAdminString
_CfprApAaaEpUserRn_Object = MibTableColumn
cfprApAaaEpUserRn = _CfprApAaaEpUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 3),
    _CfprApAaaEpUserRn_Type()
)
cfprApAaaEpUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserRn.setStatus("current")
_CfprApAaaEpUserConfigState_Type = CfprApAaaConfigState
_CfprApAaaEpUserConfigState_Object = MibTableColumn
cfprApAaaEpUserConfigState = _CfprApAaaEpUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 4),
    _CfprApAaaEpUserConfigState_Type()
)
cfprApAaaEpUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserConfigState.setStatus("current")
_CfprApAaaEpUserConfigStatusMessage_Type = SnmpAdminString
_CfprApAaaEpUserConfigStatusMessage_Object = MibTableColumn
cfprApAaaEpUserConfigStatusMessage = _CfprApAaaEpUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 5),
    _CfprApAaaEpUserConfigStatusMessage_Type()
)
cfprApAaaEpUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserConfigStatusMessage.setStatus("current")
_CfprApAaaEpUserDescr_Type = SnmpAdminString
_CfprApAaaEpUserDescr_Object = MibTableColumn
cfprApAaaEpUserDescr = _CfprApAaaEpUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 6),
    _CfprApAaaEpUserDescr_Type()
)
cfprApAaaEpUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserDescr.setStatus("current")
_CfprApAaaEpUserName_Type = SnmpAdminString
_CfprApAaaEpUserName_Object = MibTableColumn
cfprApAaaEpUserName = _CfprApAaaEpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 7),
    _CfprApAaaEpUserName_Type()
)
cfprApAaaEpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserName.setStatus("current")
_CfprApAaaEpUserPriv_Type = CfprApAaaEpAccess
_CfprApAaaEpUserPriv_Object = MibTableColumn
cfprApAaaEpUserPriv = _CfprApAaaEpUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 8),
    _CfprApAaaEpUserPriv_Type()
)
cfprApAaaEpUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserPriv.setStatus("current")
_CfprApAaaEpUserPwd_Type = SnmpAdminString
_CfprApAaaEpUserPwd_Object = MibTableColumn
cfprApAaaEpUserPwd = _CfprApAaaEpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 9),
    _CfprApAaaEpUserPwd_Type()
)
cfprApAaaEpUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserPwd.setStatus("current")
_CfprApAaaEpUserPwdSet_Type = TruthValue
_CfprApAaaEpUserPwdSet_Object = MibTableColumn
cfprApAaaEpUserPwdSet = _CfprApAaaEpUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 14, 1, 10),
    _CfprApAaaEpUserPwdSet_Type()
)
cfprApAaaEpUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaEpUserPwdSet.setStatus("current")
_CfprApAaaExtMgmtCutThruTknTable_Object = MibTable
cfprApAaaExtMgmtCutThruTknTable = _CfprApAaaExtMgmtCutThruTknTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknTable.setStatus("current")
_CfprApAaaExtMgmtCutThruTknEntry_Object = MibTableRow
cfprApAaaExtMgmtCutThruTknEntry = _CfprApAaaExtMgmtCutThruTknEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1)
)
cfprApAaaExtMgmtCutThruTknEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaExtMgmtCutThruTknInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknEntry.setStatus("current")
_CfprApAaaExtMgmtCutThruTknInstanceId_Type = CfprApManagedObjectId
_CfprApAaaExtMgmtCutThruTknInstanceId_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknInstanceId = _CfprApAaaExtMgmtCutThruTknInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 1),
    _CfprApAaaExtMgmtCutThruTknInstanceId_Type()
)
cfprApAaaExtMgmtCutThruTknInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknInstanceId.setStatus("current")
_CfprApAaaExtMgmtCutThruTknDn_Type = CfprApManagedObjectDn
_CfprApAaaExtMgmtCutThruTknDn_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknDn = _CfprApAaaExtMgmtCutThruTknDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 2),
    _CfprApAaaExtMgmtCutThruTknDn_Type()
)
cfprApAaaExtMgmtCutThruTknDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknDn.setStatus("current")
_CfprApAaaExtMgmtCutThruTknRn_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknRn_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknRn = _CfprApAaaExtMgmtCutThruTknRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 3),
    _CfprApAaaExtMgmtCutThruTknRn_Type()
)
cfprApAaaExtMgmtCutThruTknRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknRn.setStatus("current")
_CfprApAaaExtMgmtCutThruTknAuthDomain_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknAuthDomain_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknAuthDomain = _CfprApAaaExtMgmtCutThruTknAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 4),
    _CfprApAaaExtMgmtCutThruTknAuthDomain_Type()
)
cfprApAaaExtMgmtCutThruTknAuthDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknAuthDomain.setStatus("current")
_CfprApAaaExtMgmtCutThruTknAuthUser_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknAuthUser_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknAuthUser = _CfprApAaaExtMgmtCutThruTknAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 5),
    _CfprApAaaExtMgmtCutThruTknAuthUser_Type()
)
cfprApAaaExtMgmtCutThruTknAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknAuthUser.setStatus("current")
_CfprApAaaExtMgmtCutThruTknCreationTime_Type = DateAndTime
_CfprApAaaExtMgmtCutThruTknCreationTime_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknCreationTime = _CfprApAaaExtMgmtCutThruTknCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 6),
    _CfprApAaaExtMgmtCutThruTknCreationTime_Type()
)
cfprApAaaExtMgmtCutThruTknCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknCreationTime.setStatus("current")
_CfprApAaaExtMgmtCutThruTknDescr_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknDescr_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknDescr = _CfprApAaaExtMgmtCutThruTknDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 7),
    _CfprApAaaExtMgmtCutThruTknDescr_Type()
)
cfprApAaaExtMgmtCutThruTknDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknDescr.setStatus("current")
_CfprApAaaExtMgmtCutThruTknIntId_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknIntId_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknIntId = _CfprApAaaExtMgmtCutThruTknIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 8),
    _CfprApAaaExtMgmtCutThruTknIntId_Type()
)
cfprApAaaExtMgmtCutThruTknIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknIntId.setStatus("current")
_CfprApAaaExtMgmtCutThruTknLocales_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknLocales_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknLocales = _CfprApAaaExtMgmtCutThruTknLocales_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 9),
    _CfprApAaaExtMgmtCutThruTknLocales_Type()
)
cfprApAaaExtMgmtCutThruTknLocales.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknLocales.setStatus("current")
_CfprApAaaExtMgmtCutThruTknName_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknName_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknName = _CfprApAaaExtMgmtCutThruTknName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 10),
    _CfprApAaaExtMgmtCutThruTknName_Type()
)
cfprApAaaExtMgmtCutThruTknName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknName.setStatus("current")
_CfprApAaaExtMgmtCutThruTknPnDn_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknPnDn_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknPnDn = _CfprApAaaExtMgmtCutThruTknPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 11),
    _CfprApAaaExtMgmtCutThruTknPnDn_Type()
)
cfprApAaaExtMgmtCutThruTknPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknPnDn.setStatus("current")
_CfprApAaaExtMgmtCutThruTknPolicyLevel_Type = Gauge32
_CfprApAaaExtMgmtCutThruTknPolicyLevel_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknPolicyLevel = _CfprApAaaExtMgmtCutThruTknPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 12),
    _CfprApAaaExtMgmtCutThruTknPolicyLevel_Type()
)
cfprApAaaExtMgmtCutThruTknPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknPolicyLevel.setStatus("current")
_CfprApAaaExtMgmtCutThruTknPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaExtMgmtCutThruTknPolicyOwner_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknPolicyOwner = _CfprApAaaExtMgmtCutThruTknPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 13),
    _CfprApAaaExtMgmtCutThruTknPolicyOwner_Type()
)
cfprApAaaExtMgmtCutThruTknPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknPolicyOwner.setStatus("current")
_CfprApAaaExtMgmtCutThruTknPriv_Type = CfprApAaaAccess
_CfprApAaaExtMgmtCutThruTknPriv_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknPriv = _CfprApAaaExtMgmtCutThruTknPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 14),
    _CfprApAaaExtMgmtCutThruTknPriv_Type()
)
cfprApAaaExtMgmtCutThruTknPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknPriv.setStatus("current")
_CfprApAaaExtMgmtCutThruTknRemote_Type = TruthValue
_CfprApAaaExtMgmtCutThruTknRemote_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknRemote = _CfprApAaaExtMgmtCutThruTknRemote_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 15),
    _CfprApAaaExtMgmtCutThruTknRemote_Type()
)
cfprApAaaExtMgmtCutThruTknRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknRemote.setStatus("current")
_CfprApAaaExtMgmtCutThruTknToken_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknToken_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknToken = _CfprApAaaExtMgmtCutThruTknToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 16),
    _CfprApAaaExtMgmtCutThruTknToken_Type()
)
cfprApAaaExtMgmtCutThruTknToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknToken.setStatus("current")
_CfprApAaaExtMgmtCutThruTknType_Type = CfprApAaaExtMgmtAccess
_CfprApAaaExtMgmtCutThruTknType_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknType = _CfprApAaaExtMgmtCutThruTknType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 17),
    _CfprApAaaExtMgmtCutThruTknType_Type()
)
cfprApAaaExtMgmtCutThruTknType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknType.setStatus("current")
_CfprApAaaExtMgmtCutThruTknUser_Type = SnmpAdminString
_CfprApAaaExtMgmtCutThruTknUser_Object = MibTableColumn
cfprApAaaExtMgmtCutThruTknUser = _CfprApAaaExtMgmtCutThruTknUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 15, 1, 18),
    _CfprApAaaExtMgmtCutThruTknUser_Type()
)
cfprApAaaExtMgmtCutThruTknUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaExtMgmtCutThruTknUser.setStatus("current")
_CfprApAaaLdapEpTable_Object = MibTable
cfprApAaaLdapEpTable = _CfprApAaaLdapEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16)
)
if mibBuilder.loadTexts:
    cfprApAaaLdapEpTable.setStatus("current")
_CfprApAaaLdapEpEntry_Object = MibTableRow
cfprApAaaLdapEpEntry = _CfprApAaaLdapEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1)
)
cfprApAaaLdapEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaLdapEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaLdapEpEntry.setStatus("current")
_CfprApAaaLdapEpInstanceId_Type = CfprApManagedObjectId
_CfprApAaaLdapEpInstanceId_Object = MibTableColumn
cfprApAaaLdapEpInstanceId = _CfprApAaaLdapEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 1),
    _CfprApAaaLdapEpInstanceId_Type()
)
cfprApAaaLdapEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpInstanceId.setStatus("current")
_CfprApAaaLdapEpDn_Type = CfprApManagedObjectDn
_CfprApAaaLdapEpDn_Object = MibTableColumn
cfprApAaaLdapEpDn = _CfprApAaaLdapEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 2),
    _CfprApAaaLdapEpDn_Type()
)
cfprApAaaLdapEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpDn.setStatus("current")
_CfprApAaaLdapEpRn_Type = SnmpAdminString
_CfprApAaaLdapEpRn_Object = MibTableColumn
cfprApAaaLdapEpRn = _CfprApAaaLdapEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 3),
    _CfprApAaaLdapEpRn_Type()
)
cfprApAaaLdapEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpRn.setStatus("current")
_CfprApAaaLdapEpAttribute_Type = SnmpAdminString
_CfprApAaaLdapEpAttribute_Object = MibTableColumn
cfprApAaaLdapEpAttribute = _CfprApAaaLdapEpAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 4),
    _CfprApAaaLdapEpAttribute_Type()
)
cfprApAaaLdapEpAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpAttribute.setStatus("current")
_CfprApAaaLdapEpBasedn_Type = SnmpAdminString
_CfprApAaaLdapEpBasedn_Object = MibTableColumn
cfprApAaaLdapEpBasedn = _CfprApAaaLdapEpBasedn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 5),
    _CfprApAaaLdapEpBasedn_Type()
)
cfprApAaaLdapEpBasedn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpBasedn.setStatus("current")
_CfprApAaaLdapEpDescr_Type = SnmpAdminString
_CfprApAaaLdapEpDescr_Object = MibTableColumn
cfprApAaaLdapEpDescr = _CfprApAaaLdapEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 6),
    _CfprApAaaLdapEpDescr_Type()
)
cfprApAaaLdapEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpDescr.setStatus("current")
_CfprApAaaLdapEpFilter_Type = SnmpAdminString
_CfprApAaaLdapEpFilter_Object = MibTableColumn
cfprApAaaLdapEpFilter = _CfprApAaaLdapEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 7),
    _CfprApAaaLdapEpFilter_Type()
)
cfprApAaaLdapEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFilter.setStatus("current")
_CfprApAaaLdapEpFsmDescr_Type = SnmpAdminString
_CfprApAaaLdapEpFsmDescr_Object = MibTableColumn
cfprApAaaLdapEpFsmDescr = _CfprApAaaLdapEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 8),
    _CfprApAaaLdapEpFsmDescr_Type()
)
cfprApAaaLdapEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmDescr.setStatus("current")
_CfprApAaaLdapEpFsmPrev_Type = SnmpAdminString
_CfprApAaaLdapEpFsmPrev_Object = MibTableColumn
cfprApAaaLdapEpFsmPrev = _CfprApAaaLdapEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 9),
    _CfprApAaaLdapEpFsmPrev_Type()
)
cfprApAaaLdapEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmPrev.setStatus("current")
_CfprApAaaLdapEpFsmProgr_Type = Gauge32
_CfprApAaaLdapEpFsmProgr_Object = MibTableColumn
cfprApAaaLdapEpFsmProgr = _CfprApAaaLdapEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 10),
    _CfprApAaaLdapEpFsmProgr_Type()
)
cfprApAaaLdapEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmProgr.setStatus("current")
_CfprApAaaLdapEpFsmRmtInvErrCode_Type = Gauge32
_CfprApAaaLdapEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApAaaLdapEpFsmRmtInvErrCode = _CfprApAaaLdapEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 11),
    _CfprApAaaLdapEpFsmRmtInvErrCode_Type()
)
cfprApAaaLdapEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmRmtInvErrCode.setStatus("current")
_CfprApAaaLdapEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApAaaLdapEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApAaaLdapEpFsmRmtInvErrDescr = _CfprApAaaLdapEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 12),
    _CfprApAaaLdapEpFsmRmtInvErrDescr_Type()
)
cfprApAaaLdapEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmRmtInvErrDescr.setStatus("current")
_CfprApAaaLdapEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaLdapEpFsmRmtInvRslt_Object = MibTableColumn
cfprApAaaLdapEpFsmRmtInvRslt = _CfprApAaaLdapEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 13),
    _CfprApAaaLdapEpFsmRmtInvRslt_Type()
)
cfprApAaaLdapEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmRmtInvRslt.setStatus("current")
_CfprApAaaLdapEpFsmStageDescr_Type = SnmpAdminString
_CfprApAaaLdapEpFsmStageDescr_Object = MibTableColumn
cfprApAaaLdapEpFsmStageDescr = _CfprApAaaLdapEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 14),
    _CfprApAaaLdapEpFsmStageDescr_Type()
)
cfprApAaaLdapEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageDescr.setStatus("current")
_CfprApAaaLdapEpFsmStamp_Type = DateAndTime
_CfprApAaaLdapEpFsmStamp_Object = MibTableColumn
cfprApAaaLdapEpFsmStamp = _CfprApAaaLdapEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 15),
    _CfprApAaaLdapEpFsmStamp_Type()
)
cfprApAaaLdapEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStamp.setStatus("current")
_CfprApAaaLdapEpFsmStatus_Type = SnmpAdminString
_CfprApAaaLdapEpFsmStatus_Object = MibTableColumn
cfprApAaaLdapEpFsmStatus = _CfprApAaaLdapEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 16),
    _CfprApAaaLdapEpFsmStatus_Type()
)
cfprApAaaLdapEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStatus.setStatus("current")
_CfprApAaaLdapEpFsmTry_Type = Gauge32
_CfprApAaaLdapEpFsmTry_Object = MibTableColumn
cfprApAaaLdapEpFsmTry = _CfprApAaaLdapEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 17),
    _CfprApAaaLdapEpFsmTry_Type()
)
cfprApAaaLdapEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmTry.setStatus("current")
_CfprApAaaLdapEpIntId_Type = SnmpAdminString
_CfprApAaaLdapEpIntId_Object = MibTableColumn
cfprApAaaLdapEpIntId = _CfprApAaaLdapEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 18),
    _CfprApAaaLdapEpIntId_Type()
)
cfprApAaaLdapEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpIntId.setStatus("current")
_CfprApAaaLdapEpName_Type = SnmpAdminString
_CfprApAaaLdapEpName_Object = MibTableColumn
cfprApAaaLdapEpName = _CfprApAaaLdapEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 19),
    _CfprApAaaLdapEpName_Type()
)
cfprApAaaLdapEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpName.setStatus("current")
_CfprApAaaLdapEpPolicyLevel_Type = Gauge32
_CfprApAaaLdapEpPolicyLevel_Object = MibTableColumn
cfprApAaaLdapEpPolicyLevel = _CfprApAaaLdapEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 20),
    _CfprApAaaLdapEpPolicyLevel_Type()
)
cfprApAaaLdapEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpPolicyLevel.setStatus("current")
_CfprApAaaLdapEpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaLdapEpPolicyOwner_Object = MibTableColumn
cfprApAaaLdapEpPolicyOwner = _CfprApAaaLdapEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 21),
    _CfprApAaaLdapEpPolicyOwner_Type()
)
cfprApAaaLdapEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpPolicyOwner.setStatus("current")
_CfprApAaaLdapEpRetries_Type = Gauge32
_CfprApAaaLdapEpRetries_Object = MibTableColumn
cfprApAaaLdapEpRetries = _CfprApAaaLdapEpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 22),
    _CfprApAaaLdapEpRetries_Type()
)
cfprApAaaLdapEpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpRetries.setStatus("current")
_CfprApAaaLdapEpTimeout_Type = Gauge32
_CfprApAaaLdapEpTimeout_Object = MibTableColumn
cfprApAaaLdapEpTimeout = _CfprApAaaLdapEpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 16, 1, 23),
    _CfprApAaaLdapEpTimeout_Type()
)
cfprApAaaLdapEpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpTimeout.setStatus("current")
_CfprApAaaLdapEpFsmTable_Object = MibTable
cfprApAaaLdapEpFsmTable = _CfprApAaaLdapEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17)
)
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmTable.setStatus("current")
_CfprApAaaLdapEpFsmEntry_Object = MibTableRow
cfprApAaaLdapEpFsmEntry = _CfprApAaaLdapEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1)
)
cfprApAaaLdapEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaLdapEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmEntry.setStatus("current")
_CfprApAaaLdapEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApAaaLdapEpFsmInstanceId_Object = MibTableColumn
cfprApAaaLdapEpFsmInstanceId = _CfprApAaaLdapEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 1),
    _CfprApAaaLdapEpFsmInstanceId_Type()
)
cfprApAaaLdapEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmInstanceId.setStatus("current")
_CfprApAaaLdapEpFsmDn_Type = CfprApManagedObjectDn
_CfprApAaaLdapEpFsmDn_Object = MibTableColumn
cfprApAaaLdapEpFsmDn = _CfprApAaaLdapEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 2),
    _CfprApAaaLdapEpFsmDn_Type()
)
cfprApAaaLdapEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmDn.setStatus("current")
_CfprApAaaLdapEpFsmRn_Type = SnmpAdminString
_CfprApAaaLdapEpFsmRn_Object = MibTableColumn
cfprApAaaLdapEpFsmRn = _CfprApAaaLdapEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 3),
    _CfprApAaaLdapEpFsmRn_Type()
)
cfprApAaaLdapEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmRn.setStatus("current")
_CfprApAaaLdapEpFsmCompletionTime_Type = DateAndTime
_CfprApAaaLdapEpFsmCompletionTime_Object = MibTableColumn
cfprApAaaLdapEpFsmCompletionTime = _CfprApAaaLdapEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 4),
    _CfprApAaaLdapEpFsmCompletionTime_Type()
)
cfprApAaaLdapEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmCompletionTime.setStatus("current")
_CfprApAaaLdapEpFsmCurrentFsm_Type = CfprApAaaLdapEpFsmCurrentFsm
_CfprApAaaLdapEpFsmCurrentFsm_Object = MibTableColumn
cfprApAaaLdapEpFsmCurrentFsm = _CfprApAaaLdapEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 5),
    _CfprApAaaLdapEpFsmCurrentFsm_Type()
)
cfprApAaaLdapEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmCurrentFsm.setStatus("current")
_CfprApAaaLdapEpFsmDescrData_Type = SnmpAdminString
_CfprApAaaLdapEpFsmDescrData_Object = MibTableColumn
cfprApAaaLdapEpFsmDescrData = _CfprApAaaLdapEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 6),
    _CfprApAaaLdapEpFsmDescrData_Type()
)
cfprApAaaLdapEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmDescrData.setStatus("current")
_CfprApAaaLdapEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaLdapEpFsmFsmStatus_Object = MibTableColumn
cfprApAaaLdapEpFsmFsmStatus = _CfprApAaaLdapEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 7),
    _CfprApAaaLdapEpFsmFsmStatus_Type()
)
cfprApAaaLdapEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmFsmStatus.setStatus("current")
_CfprApAaaLdapEpFsmProgress_Type = Gauge32
_CfprApAaaLdapEpFsmProgress_Object = MibTableColumn
cfprApAaaLdapEpFsmProgress = _CfprApAaaLdapEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 8),
    _CfprApAaaLdapEpFsmProgress_Type()
)
cfprApAaaLdapEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmProgress.setStatus("current")
_CfprApAaaLdapEpFsmRmtErrCode_Type = Gauge32
_CfprApAaaLdapEpFsmRmtErrCode_Object = MibTableColumn
cfprApAaaLdapEpFsmRmtErrCode = _CfprApAaaLdapEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 9),
    _CfprApAaaLdapEpFsmRmtErrCode_Type()
)
cfprApAaaLdapEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmRmtErrCode.setStatus("current")
_CfprApAaaLdapEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApAaaLdapEpFsmRmtErrDescr_Object = MibTableColumn
cfprApAaaLdapEpFsmRmtErrDescr = _CfprApAaaLdapEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 10),
    _CfprApAaaLdapEpFsmRmtErrDescr_Type()
)
cfprApAaaLdapEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmRmtErrDescr.setStatus("current")
_CfprApAaaLdapEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaLdapEpFsmRmtRslt_Object = MibTableColumn
cfprApAaaLdapEpFsmRmtRslt = _CfprApAaaLdapEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 17, 1, 11),
    _CfprApAaaLdapEpFsmRmtRslt_Type()
)
cfprApAaaLdapEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmRmtRslt.setStatus("current")
_CfprApAaaLdapEpFsmStageTable_Object = MibTable
cfprApAaaLdapEpFsmStageTable = _CfprApAaaLdapEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18)
)
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageTable.setStatus("current")
_CfprApAaaLdapEpFsmStageEntry_Object = MibTableRow
cfprApAaaLdapEpFsmStageEntry = _CfprApAaaLdapEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1)
)
cfprApAaaLdapEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaLdapEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageEntry.setStatus("current")
_CfprApAaaLdapEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApAaaLdapEpFsmStageInstanceId_Object = MibTableColumn
cfprApAaaLdapEpFsmStageInstanceId = _CfprApAaaLdapEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 1),
    _CfprApAaaLdapEpFsmStageInstanceId_Type()
)
cfprApAaaLdapEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageInstanceId.setStatus("current")
_CfprApAaaLdapEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApAaaLdapEpFsmStageDn_Object = MibTableColumn
cfprApAaaLdapEpFsmStageDn = _CfprApAaaLdapEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 2),
    _CfprApAaaLdapEpFsmStageDn_Type()
)
cfprApAaaLdapEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageDn.setStatus("current")
_CfprApAaaLdapEpFsmStageRn_Type = SnmpAdminString
_CfprApAaaLdapEpFsmStageRn_Object = MibTableColumn
cfprApAaaLdapEpFsmStageRn = _CfprApAaaLdapEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 3),
    _CfprApAaaLdapEpFsmStageRn_Type()
)
cfprApAaaLdapEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageRn.setStatus("current")
_CfprApAaaLdapEpFsmStageDescrData_Type = SnmpAdminString
_CfprApAaaLdapEpFsmStageDescrData_Object = MibTableColumn
cfprApAaaLdapEpFsmStageDescrData = _CfprApAaaLdapEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 4),
    _CfprApAaaLdapEpFsmStageDescrData_Type()
)
cfprApAaaLdapEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageDescrData.setStatus("current")
_CfprApAaaLdapEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApAaaLdapEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApAaaLdapEpFsmStageLastUpdateTime = _CfprApAaaLdapEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 5),
    _CfprApAaaLdapEpFsmStageLastUpdateTime_Type()
)
cfprApAaaLdapEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageLastUpdateTime.setStatus("current")
_CfprApAaaLdapEpFsmStageName_Type = CfprApAaaLdapEpFsmStageName
_CfprApAaaLdapEpFsmStageName_Object = MibTableColumn
cfprApAaaLdapEpFsmStageName = _CfprApAaaLdapEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 6),
    _CfprApAaaLdapEpFsmStageName_Type()
)
cfprApAaaLdapEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageName.setStatus("current")
_CfprApAaaLdapEpFsmStageOrder_Type = Gauge32
_CfprApAaaLdapEpFsmStageOrder_Object = MibTableColumn
cfprApAaaLdapEpFsmStageOrder = _CfprApAaaLdapEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 7),
    _CfprApAaaLdapEpFsmStageOrder_Type()
)
cfprApAaaLdapEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageOrder.setStatus("current")
_CfprApAaaLdapEpFsmStageRetry_Type = Gauge32
_CfprApAaaLdapEpFsmStageRetry_Object = MibTableColumn
cfprApAaaLdapEpFsmStageRetry = _CfprApAaaLdapEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 8),
    _CfprApAaaLdapEpFsmStageRetry_Type()
)
cfprApAaaLdapEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageRetry.setStatus("current")
_CfprApAaaLdapEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaLdapEpFsmStageStageStatus_Object = MibTableColumn
cfprApAaaLdapEpFsmStageStageStatus = _CfprApAaaLdapEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 18, 1, 9),
    _CfprApAaaLdapEpFsmStageStageStatus_Type()
)
cfprApAaaLdapEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapEpFsmStageStageStatus.setStatus("current")
_CfprApAaaLdapGroupTable_Object = MibTable
cfprApAaaLdapGroupTable = _CfprApAaaLdapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 19)
)
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupTable.setStatus("current")
_CfprApAaaLdapGroupEntry_Object = MibTableRow
cfprApAaaLdapGroupEntry = _CfprApAaaLdapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 19, 1)
)
cfprApAaaLdapGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaLdapGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupEntry.setStatus("current")
_CfprApAaaLdapGroupInstanceId_Type = CfprApManagedObjectId
_CfprApAaaLdapGroupInstanceId_Object = MibTableColumn
cfprApAaaLdapGroupInstanceId = _CfprApAaaLdapGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 19, 1, 1),
    _CfprApAaaLdapGroupInstanceId_Type()
)
cfprApAaaLdapGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupInstanceId.setStatus("current")
_CfprApAaaLdapGroupDn_Type = CfprApManagedObjectDn
_CfprApAaaLdapGroupDn_Object = MibTableColumn
cfprApAaaLdapGroupDn = _CfprApAaaLdapGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 19, 1, 2),
    _CfprApAaaLdapGroupDn_Type()
)
cfprApAaaLdapGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupDn.setStatus("current")
_CfprApAaaLdapGroupRn_Type = SnmpAdminString
_CfprApAaaLdapGroupRn_Object = MibTableColumn
cfprApAaaLdapGroupRn = _CfprApAaaLdapGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 19, 1, 3),
    _CfprApAaaLdapGroupRn_Type()
)
cfprApAaaLdapGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRn.setStatus("current")
_CfprApAaaLdapGroupDescr_Type = SnmpAdminString
_CfprApAaaLdapGroupDescr_Object = MibTableColumn
cfprApAaaLdapGroupDescr = _CfprApAaaLdapGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 19, 1, 4),
    _CfprApAaaLdapGroupDescr_Type()
)
cfprApAaaLdapGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupDescr.setStatus("current")
_CfprApAaaLdapGroupName_Type = SnmpAdminString
_CfprApAaaLdapGroupName_Object = MibTableColumn
cfprApAaaLdapGroupName = _CfprApAaaLdapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 19, 1, 5),
    _CfprApAaaLdapGroupName_Type()
)
cfprApAaaLdapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupName.setStatus("current")
_CfprApAaaLdapGroupRuleTable_Object = MibTable
cfprApAaaLdapGroupRuleTable = _CfprApAaaLdapGroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20)
)
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleTable.setStatus("current")
_CfprApAaaLdapGroupRuleEntry_Object = MibTableRow
cfprApAaaLdapGroupRuleEntry = _CfprApAaaLdapGroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1)
)
cfprApAaaLdapGroupRuleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaLdapGroupRuleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleEntry.setStatus("current")
_CfprApAaaLdapGroupRuleInstanceId_Type = CfprApManagedObjectId
_CfprApAaaLdapGroupRuleInstanceId_Object = MibTableColumn
cfprApAaaLdapGroupRuleInstanceId = _CfprApAaaLdapGroupRuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 1),
    _CfprApAaaLdapGroupRuleInstanceId_Type()
)
cfprApAaaLdapGroupRuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleInstanceId.setStatus("current")
_CfprApAaaLdapGroupRuleDn_Type = CfprApManagedObjectDn
_CfprApAaaLdapGroupRuleDn_Object = MibTableColumn
cfprApAaaLdapGroupRuleDn = _CfprApAaaLdapGroupRuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 2),
    _CfprApAaaLdapGroupRuleDn_Type()
)
cfprApAaaLdapGroupRuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleDn.setStatus("current")
_CfprApAaaLdapGroupRuleRn_Type = SnmpAdminString
_CfprApAaaLdapGroupRuleRn_Object = MibTableColumn
cfprApAaaLdapGroupRuleRn = _CfprApAaaLdapGroupRuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 3),
    _CfprApAaaLdapGroupRuleRn_Type()
)
cfprApAaaLdapGroupRuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleRn.setStatus("current")
_CfprApAaaLdapGroupRuleAuthorization_Type = CfprApAaaLdapGroupRuleAuthorization
_CfprApAaaLdapGroupRuleAuthorization_Object = MibTableColumn
cfprApAaaLdapGroupRuleAuthorization = _CfprApAaaLdapGroupRuleAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 4),
    _CfprApAaaLdapGroupRuleAuthorization_Type()
)
cfprApAaaLdapGroupRuleAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleAuthorization.setStatus("current")
_CfprApAaaLdapGroupRuleDescr_Type = SnmpAdminString
_CfprApAaaLdapGroupRuleDescr_Object = MibTableColumn
cfprApAaaLdapGroupRuleDescr = _CfprApAaaLdapGroupRuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 5),
    _CfprApAaaLdapGroupRuleDescr_Type()
)
cfprApAaaLdapGroupRuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleDescr.setStatus("current")
_CfprApAaaLdapGroupRuleName_Type = SnmpAdminString
_CfprApAaaLdapGroupRuleName_Object = MibTableColumn
cfprApAaaLdapGroupRuleName = _CfprApAaaLdapGroupRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 6),
    _CfprApAaaLdapGroupRuleName_Type()
)
cfprApAaaLdapGroupRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleName.setStatus("current")
_CfprApAaaLdapGroupRuleTargetAttr_Type = SnmpAdminString
_CfprApAaaLdapGroupRuleTargetAttr_Object = MibTableColumn
cfprApAaaLdapGroupRuleTargetAttr = _CfprApAaaLdapGroupRuleTargetAttr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 7),
    _CfprApAaaLdapGroupRuleTargetAttr_Type()
)
cfprApAaaLdapGroupRuleTargetAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleTargetAttr.setStatus("current")
_CfprApAaaLdapGroupRuleTraversal_Type = CfprApAaaLdapGroupRuleTraversal
_CfprApAaaLdapGroupRuleTraversal_Object = MibTableColumn
cfprApAaaLdapGroupRuleTraversal = _CfprApAaaLdapGroupRuleTraversal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 8),
    _CfprApAaaLdapGroupRuleTraversal_Type()
)
cfprApAaaLdapGroupRuleTraversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleTraversal.setStatus("current")
_CfprApAaaLdapGroupRuleUsePrimaryGroup_Type = TruthValue
_CfprApAaaLdapGroupRuleUsePrimaryGroup_Object = MibTableColumn
cfprApAaaLdapGroupRuleUsePrimaryGroup = _CfprApAaaLdapGroupRuleUsePrimaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 20, 1, 9),
    _CfprApAaaLdapGroupRuleUsePrimaryGroup_Type()
)
cfprApAaaLdapGroupRuleUsePrimaryGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapGroupRuleUsePrimaryGroup.setStatus("current")
_CfprApAaaLdapProviderTable_Object = MibTable
cfprApAaaLdapProviderTable = _CfprApAaaLdapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21)
)
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderTable.setStatus("current")
_CfprApAaaLdapProviderEntry_Object = MibTableRow
cfprApAaaLdapProviderEntry = _CfprApAaaLdapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1)
)
cfprApAaaLdapProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaLdapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderEntry.setStatus("current")
_CfprApAaaLdapProviderInstanceId_Type = CfprApManagedObjectId
_CfprApAaaLdapProviderInstanceId_Object = MibTableColumn
cfprApAaaLdapProviderInstanceId = _CfprApAaaLdapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 1),
    _CfprApAaaLdapProviderInstanceId_Type()
)
cfprApAaaLdapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderInstanceId.setStatus("current")
_CfprApAaaLdapProviderDn_Type = CfprApManagedObjectDn
_CfprApAaaLdapProviderDn_Object = MibTableColumn
cfprApAaaLdapProviderDn = _CfprApAaaLdapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 2),
    _CfprApAaaLdapProviderDn_Type()
)
cfprApAaaLdapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderDn.setStatus("current")
_CfprApAaaLdapProviderRn_Type = SnmpAdminString
_CfprApAaaLdapProviderRn_Object = MibTableColumn
cfprApAaaLdapProviderRn = _CfprApAaaLdapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 3),
    _CfprApAaaLdapProviderRn_Type()
)
cfprApAaaLdapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderRn.setStatus("current")
_CfprApAaaLdapProviderAttribute_Type = SnmpAdminString
_CfprApAaaLdapProviderAttribute_Object = MibTableColumn
cfprApAaaLdapProviderAttribute = _CfprApAaaLdapProviderAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 4),
    _CfprApAaaLdapProviderAttribute_Type()
)
cfprApAaaLdapProviderAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderAttribute.setStatus("current")
_CfprApAaaLdapProviderBasedn_Type = SnmpAdminString
_CfprApAaaLdapProviderBasedn_Object = MibTableColumn
cfprApAaaLdapProviderBasedn = _CfprApAaaLdapProviderBasedn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 5),
    _CfprApAaaLdapProviderBasedn_Type()
)
cfprApAaaLdapProviderBasedn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderBasedn.setStatus("current")
_CfprApAaaLdapProviderDescr_Type = SnmpAdminString
_CfprApAaaLdapProviderDescr_Object = MibTableColumn
cfprApAaaLdapProviderDescr = _CfprApAaaLdapProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 6),
    _CfprApAaaLdapProviderDescr_Type()
)
cfprApAaaLdapProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderDescr.setStatus("current")
_CfprApAaaLdapProviderEnableSSL_Type = TruthValue
_CfprApAaaLdapProviderEnableSSL_Object = MibTableColumn
cfprApAaaLdapProviderEnableSSL = _CfprApAaaLdapProviderEnableSSL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 7),
    _CfprApAaaLdapProviderEnableSSL_Type()
)
cfprApAaaLdapProviderEnableSSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderEnableSSL.setStatus("current")
_CfprApAaaLdapProviderEncKey_Type = SnmpAdminString
_CfprApAaaLdapProviderEncKey_Object = MibTableColumn
cfprApAaaLdapProviderEncKey = _CfprApAaaLdapProviderEncKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 8),
    _CfprApAaaLdapProviderEncKey_Type()
)
cfprApAaaLdapProviderEncKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderEncKey.setStatus("current")
_CfprApAaaLdapProviderFilter_Type = SnmpAdminString
_CfprApAaaLdapProviderFilter_Object = MibTableColumn
cfprApAaaLdapProviderFilter = _CfprApAaaLdapProviderFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 9),
    _CfprApAaaLdapProviderFilter_Type()
)
cfprApAaaLdapProviderFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderFilter.setStatus("current")
_CfprApAaaLdapProviderKey_Type = SnmpAdminString
_CfprApAaaLdapProviderKey_Object = MibTableColumn
cfprApAaaLdapProviderKey = _CfprApAaaLdapProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 10),
    _CfprApAaaLdapProviderKey_Type()
)
cfprApAaaLdapProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderKey.setStatus("current")
_CfprApAaaLdapProviderKeySet_Type = TruthValue
_CfprApAaaLdapProviderKeySet_Object = MibTableColumn
cfprApAaaLdapProviderKeySet = _CfprApAaaLdapProviderKeySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 11),
    _CfprApAaaLdapProviderKeySet_Type()
)
cfprApAaaLdapProviderKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderKeySet.setStatus("current")
_CfprApAaaLdapProviderName_Type = SnmpAdminString
_CfprApAaaLdapProviderName_Object = MibTableColumn
cfprApAaaLdapProviderName = _CfprApAaaLdapProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 12),
    _CfprApAaaLdapProviderName_Type()
)
cfprApAaaLdapProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderName.setStatus("current")
_CfprApAaaLdapProviderOrder_Type = Gauge32
_CfprApAaaLdapProviderOrder_Object = MibTableColumn
cfprApAaaLdapProviderOrder = _CfprApAaaLdapProviderOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 13),
    _CfprApAaaLdapProviderOrder_Type()
)
cfprApAaaLdapProviderOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderOrder.setStatus("current")
_CfprApAaaLdapProviderPort_Type = Gauge32
_CfprApAaaLdapProviderPort_Object = MibTableColumn
cfprApAaaLdapProviderPort = _CfprApAaaLdapProviderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 14),
    _CfprApAaaLdapProviderPort_Type()
)
cfprApAaaLdapProviderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderPort.setStatus("current")
_CfprApAaaLdapProviderRetries_Type = Gauge32
_CfprApAaaLdapProviderRetries_Object = MibTableColumn
cfprApAaaLdapProviderRetries = _CfprApAaaLdapProviderRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 15),
    _CfprApAaaLdapProviderRetries_Type()
)
cfprApAaaLdapProviderRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderRetries.setStatus("current")
_CfprApAaaLdapProviderRootdn_Type = SnmpAdminString
_CfprApAaaLdapProviderRootdn_Object = MibTableColumn
cfprApAaaLdapProviderRootdn = _CfprApAaaLdapProviderRootdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 16),
    _CfprApAaaLdapProviderRootdn_Type()
)
cfprApAaaLdapProviderRootdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderRootdn.setStatus("current")
_CfprApAaaLdapProviderTimeout_Type = Gauge32
_CfprApAaaLdapProviderTimeout_Object = MibTableColumn
cfprApAaaLdapProviderTimeout = _CfprApAaaLdapProviderTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 17),
    _CfprApAaaLdapProviderTimeout_Type()
)
cfprApAaaLdapProviderTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderTimeout.setStatus("current")
_CfprApAaaLdapProviderVendor_Type = CfprApAaaLdapVendor
_CfprApAaaLdapProviderVendor_Object = MibTableColumn
cfprApAaaLdapProviderVendor = _CfprApAaaLdapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 21, 1, 18),
    _CfprApAaaLdapProviderVendor_Type()
)
cfprApAaaLdapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLdapProviderVendor.setStatus("current")
_CfprApAaaLocaleTable_Object = MibTable
cfprApAaaLocaleTable = _CfprApAaaLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22)
)
if mibBuilder.loadTexts:
    cfprApAaaLocaleTable.setStatus("current")
_CfprApAaaLocaleEntry_Object = MibTableRow
cfprApAaaLocaleEntry = _CfprApAaaLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1)
)
cfprApAaaLocaleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaLocaleEntry.setStatus("current")
_CfprApAaaLocaleInstanceId_Type = CfprApManagedObjectId
_CfprApAaaLocaleInstanceId_Object = MibTableColumn
cfprApAaaLocaleInstanceId = _CfprApAaaLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 1),
    _CfprApAaaLocaleInstanceId_Type()
)
cfprApAaaLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaLocaleInstanceId.setStatus("current")
_CfprApAaaLocaleDn_Type = CfprApManagedObjectDn
_CfprApAaaLocaleDn_Object = MibTableColumn
cfprApAaaLocaleDn = _CfprApAaaLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 2),
    _CfprApAaaLocaleDn_Type()
)
cfprApAaaLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocaleDn.setStatus("current")
_CfprApAaaLocaleRn_Type = SnmpAdminString
_CfprApAaaLocaleRn_Object = MibTableColumn
cfprApAaaLocaleRn = _CfprApAaaLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 3),
    _CfprApAaaLocaleRn_Type()
)
cfprApAaaLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocaleRn.setStatus("current")
_CfprApAaaLocaleConfigState_Type = CfprApAaaConfigState
_CfprApAaaLocaleConfigState_Object = MibTableColumn
cfprApAaaLocaleConfigState = _CfprApAaaLocaleConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 4),
    _CfprApAaaLocaleConfigState_Type()
)
cfprApAaaLocaleConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocaleConfigState.setStatus("current")
_CfprApAaaLocaleConfigStatusMessage_Type = SnmpAdminString
_CfprApAaaLocaleConfigStatusMessage_Object = MibTableColumn
cfprApAaaLocaleConfigStatusMessage = _CfprApAaaLocaleConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 5),
    _CfprApAaaLocaleConfigStatusMessage_Type()
)
cfprApAaaLocaleConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocaleConfigStatusMessage.setStatus("current")
_CfprApAaaLocaleDescr_Type = SnmpAdminString
_CfprApAaaLocaleDescr_Object = MibTableColumn
cfprApAaaLocaleDescr = _CfprApAaaLocaleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 6),
    _CfprApAaaLocaleDescr_Type()
)
cfprApAaaLocaleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocaleDescr.setStatus("current")
_CfprApAaaLocaleIntId_Type = SnmpAdminString
_CfprApAaaLocaleIntId_Object = MibTableColumn
cfprApAaaLocaleIntId = _CfprApAaaLocaleIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 7),
    _CfprApAaaLocaleIntId_Type()
)
cfprApAaaLocaleIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocaleIntId.setStatus("current")
_CfprApAaaLocaleName_Type = SnmpAdminString
_CfprApAaaLocaleName_Object = MibTableColumn
cfprApAaaLocaleName = _CfprApAaaLocaleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 8),
    _CfprApAaaLocaleName_Type()
)
cfprApAaaLocaleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocaleName.setStatus("current")
_CfprApAaaLocalePolicyLevel_Type = Gauge32
_CfprApAaaLocalePolicyLevel_Object = MibTableColumn
cfprApAaaLocalePolicyLevel = _CfprApAaaLocalePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 9),
    _CfprApAaaLocalePolicyLevel_Type()
)
cfprApAaaLocalePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocalePolicyLevel.setStatus("current")
_CfprApAaaLocalePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaLocalePolicyOwner_Object = MibTableColumn
cfprApAaaLocalePolicyOwner = _CfprApAaaLocalePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 22, 1, 10),
    _CfprApAaaLocalePolicyOwner_Type()
)
cfprApAaaLocalePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLocalePolicyOwner.setStatus("current")
_CfprApAaaLogTable_Object = MibTable
cfprApAaaLogTable = _CfprApAaaLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 23)
)
if mibBuilder.loadTexts:
    cfprApAaaLogTable.setStatus("current")
_CfprApAaaLogEntry_Object = MibTableRow
cfprApAaaLogEntry = _CfprApAaaLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 23, 1)
)
cfprApAaaLogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaLogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaLogEntry.setStatus("current")
_CfprApAaaLogInstanceId_Type = CfprApManagedObjectId
_CfprApAaaLogInstanceId_Object = MibTableColumn
cfprApAaaLogInstanceId = _CfprApAaaLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 23, 1, 1),
    _CfprApAaaLogInstanceId_Type()
)
cfprApAaaLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaLogInstanceId.setStatus("current")
_CfprApAaaLogDn_Type = CfprApManagedObjectDn
_CfprApAaaLogDn_Object = MibTableColumn
cfprApAaaLogDn = _CfprApAaaLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 23, 1, 2),
    _CfprApAaaLogDn_Type()
)
cfprApAaaLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLogDn.setStatus("current")
_CfprApAaaLogRn_Type = SnmpAdminString
_CfprApAaaLogRn_Object = MibTableColumn
cfprApAaaLogRn = _CfprApAaaLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 23, 1, 3),
    _CfprApAaaLogRn_Type()
)
cfprApAaaLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLogRn.setStatus("current")
_CfprApAaaLogMaxSize_Type = Gauge32
_CfprApAaaLogMaxSize_Object = MibTableColumn
cfprApAaaLogMaxSize = _CfprApAaaLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 23, 1, 4),
    _CfprApAaaLogMaxSize_Type()
)
cfprApAaaLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLogMaxSize.setStatus("current")
_CfprApAaaLogPurgeWindow_Type = Gauge32
_CfprApAaaLogPurgeWindow_Object = MibTableColumn
cfprApAaaLogPurgeWindow = _CfprApAaaLogPurgeWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 23, 1, 5),
    _CfprApAaaLogPurgeWindow_Type()
)
cfprApAaaLogPurgeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLogPurgeWindow.setStatus("current")
_CfprApAaaLogSize_Type = Gauge32
_CfprApAaaLogSize_Object = MibTableColumn
cfprApAaaLogSize = _CfprApAaaLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 23, 1, 6),
    _CfprApAaaLogSize_Type()
)
cfprApAaaLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaLogSize.setStatus("current")
_CfprApAaaModLRTable_Object = MibTable
cfprApAaaModLRTable = _CfprApAaaModLRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24)
)
if mibBuilder.loadTexts:
    cfprApAaaModLRTable.setStatus("current")
_CfprApAaaModLREntry_Object = MibTableRow
cfprApAaaModLREntry = _CfprApAaaModLREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1)
)
cfprApAaaModLREntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaModLRInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaModLREntry.setStatus("current")
_CfprApAaaModLRInstanceId_Type = CfprApManagedObjectId
_CfprApAaaModLRInstanceId_Object = MibTableColumn
cfprApAaaModLRInstanceId = _CfprApAaaModLRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 1),
    _CfprApAaaModLRInstanceId_Type()
)
cfprApAaaModLRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaModLRInstanceId.setStatus("current")
_CfprApAaaModLRDn_Type = CfprApManagedObjectDn
_CfprApAaaModLRDn_Object = MibTableColumn
cfprApAaaModLRDn = _CfprApAaaModLRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 2),
    _CfprApAaaModLRDn_Type()
)
cfprApAaaModLRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRDn.setStatus("current")
_CfprApAaaModLRRn_Type = SnmpAdminString
_CfprApAaaModLRRn_Object = MibTableColumn
cfprApAaaModLRRn = _CfprApAaaModLRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 3),
    _CfprApAaaModLRRn_Type()
)
cfprApAaaModLRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRRn.setStatus("current")
_CfprApAaaModLRAffected_Type = SnmpAdminString
_CfprApAaaModLRAffected_Object = MibTableColumn
cfprApAaaModLRAffected = _CfprApAaaModLRAffected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 4),
    _CfprApAaaModLRAffected_Type()
)
cfprApAaaModLRAffected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRAffected.setStatus("current")
_CfprApAaaModLRCause_Type = CfprApConditionCause
_CfprApAaaModLRCause_Object = MibTableColumn
cfprApAaaModLRCause = _CfprApAaaModLRCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 5),
    _CfprApAaaModLRCause_Type()
)
cfprApAaaModLRCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRCause.setStatus("current")
_CfprApAaaModLRChangeSet_Type = SnmpAdminString
_CfprApAaaModLRChangeSet_Object = MibTableColumn
cfprApAaaModLRChangeSet = _CfprApAaaModLRChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 6),
    _CfprApAaaModLRChangeSet_Type()
)
cfprApAaaModLRChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRChangeSet.setStatus("current")
_CfprApAaaModLRCode_Type = CfprApConditionCode
_CfprApAaaModLRCode_Object = MibTableColumn
cfprApAaaModLRCode = _CfprApAaaModLRCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 7),
    _CfprApAaaModLRCode_Type()
)
cfprApAaaModLRCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRCode.setStatus("current")
_CfprApAaaModLRCreated_Type = DateAndTime
_CfprApAaaModLRCreated_Object = MibTableColumn
cfprApAaaModLRCreated = _CfprApAaaModLRCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 8),
    _CfprApAaaModLRCreated_Type()
)
cfprApAaaModLRCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRCreated.setStatus("current")
_CfprApAaaModLRDescr_Type = SnmpAdminString
_CfprApAaaModLRDescr_Object = MibTableColumn
cfprApAaaModLRDescr = _CfprApAaaModLRDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 9),
    _CfprApAaaModLRDescr_Type()
)
cfprApAaaModLRDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRDescr.setStatus("current")
_CfprApAaaModLRId_Type = Gauge32
_CfprApAaaModLRId_Object = MibTableColumn
cfprApAaaModLRId = _CfprApAaaModLRId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 10),
    _CfprApAaaModLRId_Type()
)
cfprApAaaModLRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRId.setStatus("current")
_CfprApAaaModLRInd_Type = CfprApConditionActionIndicator
_CfprApAaaModLRInd_Object = MibTableColumn
cfprApAaaModLRInd = _CfprApAaaModLRInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 11),
    _CfprApAaaModLRInd_Type()
)
cfprApAaaModLRInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRInd.setStatus("current")
_CfprApAaaModLRSessionId_Type = SnmpAdminString
_CfprApAaaModLRSessionId_Object = MibTableColumn
cfprApAaaModLRSessionId = _CfprApAaaModLRSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 12),
    _CfprApAaaModLRSessionId_Type()
)
cfprApAaaModLRSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRSessionId.setStatus("current")
_CfprApAaaModLRSeverity_Type = CfprApConditionSeverity
_CfprApAaaModLRSeverity_Object = MibTableColumn
cfprApAaaModLRSeverity = _CfprApAaaModLRSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 13),
    _CfprApAaaModLRSeverity_Type()
)
cfprApAaaModLRSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRSeverity.setStatus("current")
_CfprApAaaModLRTrig_Type = Gauge32
_CfprApAaaModLRTrig_Object = MibTableColumn
cfprApAaaModLRTrig = _CfprApAaaModLRTrig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 14),
    _CfprApAaaModLRTrig_Type()
)
cfprApAaaModLRTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRTrig.setStatus("current")
_CfprApAaaModLRTxId_Type = Unsigned64
_CfprApAaaModLRTxId_Object = MibTableColumn
cfprApAaaModLRTxId = _CfprApAaaModLRTxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 15),
    _CfprApAaaModLRTxId_Type()
)
cfprApAaaModLRTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRTxId.setStatus("current")
_CfprApAaaModLRUser_Type = SnmpAdminString
_CfprApAaaModLRUser_Object = MibTableColumn
cfprApAaaModLRUser = _CfprApAaaModLRUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 24, 1, 16),
    _CfprApAaaModLRUser_Type()
)
cfprApAaaModLRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaModLRUser.setStatus("current")
_CfprApAaaOrgTable_Object = MibTable
cfprApAaaOrgTable = _CfprApAaaOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25)
)
if mibBuilder.loadTexts:
    cfprApAaaOrgTable.setStatus("current")
_CfprApAaaOrgEntry_Object = MibTableRow
cfprApAaaOrgEntry = _CfprApAaaOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1)
)
cfprApAaaOrgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaOrgEntry.setStatus("current")
_CfprApAaaOrgInstanceId_Type = CfprApManagedObjectId
_CfprApAaaOrgInstanceId_Object = MibTableColumn
cfprApAaaOrgInstanceId = _CfprApAaaOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1, 1),
    _CfprApAaaOrgInstanceId_Type()
)
cfprApAaaOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaOrgInstanceId.setStatus("current")
_CfprApAaaOrgDn_Type = CfprApManagedObjectDn
_CfprApAaaOrgDn_Object = MibTableColumn
cfprApAaaOrgDn = _CfprApAaaOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1, 2),
    _CfprApAaaOrgDn_Type()
)
cfprApAaaOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaOrgDn.setStatus("current")
_CfprApAaaOrgRn_Type = SnmpAdminString
_CfprApAaaOrgRn_Object = MibTableColumn
cfprApAaaOrgRn = _CfprApAaaOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1, 3),
    _CfprApAaaOrgRn_Type()
)
cfprApAaaOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaOrgRn.setStatus("current")
_CfprApAaaOrgConfigState_Type = CfprApAaaConfigState
_CfprApAaaOrgConfigState_Object = MibTableColumn
cfprApAaaOrgConfigState = _CfprApAaaOrgConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1, 4),
    _CfprApAaaOrgConfigState_Type()
)
cfprApAaaOrgConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaOrgConfigState.setStatus("current")
_CfprApAaaOrgConfigStatusMessage_Type = SnmpAdminString
_CfprApAaaOrgConfigStatusMessage_Object = MibTableColumn
cfprApAaaOrgConfigStatusMessage = _CfprApAaaOrgConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1, 5),
    _CfprApAaaOrgConfigStatusMessage_Type()
)
cfprApAaaOrgConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaOrgConfigStatusMessage.setStatus("current")
_CfprApAaaOrgDescr_Type = SnmpAdminString
_CfprApAaaOrgDescr_Object = MibTableColumn
cfprApAaaOrgDescr = _CfprApAaaOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1, 6),
    _CfprApAaaOrgDescr_Type()
)
cfprApAaaOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaOrgDescr.setStatus("current")
_CfprApAaaOrgName_Type = SnmpAdminString
_CfprApAaaOrgName_Object = MibTableColumn
cfprApAaaOrgName = _CfprApAaaOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1, 7),
    _CfprApAaaOrgName_Type()
)
cfprApAaaOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaOrgName.setStatus("current")
_CfprApAaaOrgOrgDn_Type = SnmpAdminString
_CfprApAaaOrgOrgDn_Object = MibTableColumn
cfprApAaaOrgOrgDn = _CfprApAaaOrgOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 25, 1, 8),
    _CfprApAaaOrgOrgDn_Type()
)
cfprApAaaOrgOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaOrgOrgDn.setStatus("current")
_CfprApAaaPreLoginBannerTable_Object = MibTable
cfprApAaaPreLoginBannerTable = _CfprApAaaPreLoginBannerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26)
)
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerTable.setStatus("current")
_CfprApAaaPreLoginBannerEntry_Object = MibTableRow
cfprApAaaPreLoginBannerEntry = _CfprApAaaPreLoginBannerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1)
)
cfprApAaaPreLoginBannerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaPreLoginBannerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerEntry.setStatus("current")
_CfprApAaaPreLoginBannerInstanceId_Type = CfprApManagedObjectId
_CfprApAaaPreLoginBannerInstanceId_Object = MibTableColumn
cfprApAaaPreLoginBannerInstanceId = _CfprApAaaPreLoginBannerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 1),
    _CfprApAaaPreLoginBannerInstanceId_Type()
)
cfprApAaaPreLoginBannerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerInstanceId.setStatus("current")
_CfprApAaaPreLoginBannerDn_Type = CfprApManagedObjectDn
_CfprApAaaPreLoginBannerDn_Object = MibTableColumn
cfprApAaaPreLoginBannerDn = _CfprApAaaPreLoginBannerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 2),
    _CfprApAaaPreLoginBannerDn_Type()
)
cfprApAaaPreLoginBannerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerDn.setStatus("current")
_CfprApAaaPreLoginBannerRn_Type = SnmpAdminString
_CfprApAaaPreLoginBannerRn_Object = MibTableColumn
cfprApAaaPreLoginBannerRn = _CfprApAaaPreLoginBannerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 3),
    _CfprApAaaPreLoginBannerRn_Type()
)
cfprApAaaPreLoginBannerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerRn.setStatus("current")
_CfprApAaaPreLoginBannerDescr_Type = SnmpAdminString
_CfprApAaaPreLoginBannerDescr_Object = MibTableColumn
cfprApAaaPreLoginBannerDescr = _CfprApAaaPreLoginBannerDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 4),
    _CfprApAaaPreLoginBannerDescr_Type()
)
cfprApAaaPreLoginBannerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerDescr.setStatus("current")
_CfprApAaaPreLoginBannerIntId_Type = SnmpAdminString
_CfprApAaaPreLoginBannerIntId_Object = MibTableColumn
cfprApAaaPreLoginBannerIntId = _CfprApAaaPreLoginBannerIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 5),
    _CfprApAaaPreLoginBannerIntId_Type()
)
cfprApAaaPreLoginBannerIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerIntId.setStatus("current")
_CfprApAaaPreLoginBannerMessage_Type = SnmpAdminString
_CfprApAaaPreLoginBannerMessage_Object = MibTableColumn
cfprApAaaPreLoginBannerMessage = _CfprApAaaPreLoginBannerMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 6),
    _CfprApAaaPreLoginBannerMessage_Type()
)
cfprApAaaPreLoginBannerMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerMessage.setStatus("current")
_CfprApAaaPreLoginBannerName_Type = SnmpAdminString
_CfprApAaaPreLoginBannerName_Object = MibTableColumn
cfprApAaaPreLoginBannerName = _CfprApAaaPreLoginBannerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 7),
    _CfprApAaaPreLoginBannerName_Type()
)
cfprApAaaPreLoginBannerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerName.setStatus("current")
_CfprApAaaPreLoginBannerPolicyLevel_Type = Gauge32
_CfprApAaaPreLoginBannerPolicyLevel_Object = MibTableColumn
cfprApAaaPreLoginBannerPolicyLevel = _CfprApAaaPreLoginBannerPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 8),
    _CfprApAaaPreLoginBannerPolicyLevel_Type()
)
cfprApAaaPreLoginBannerPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerPolicyLevel.setStatus("current")
_CfprApAaaPreLoginBannerPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaPreLoginBannerPolicyOwner_Object = MibTableColumn
cfprApAaaPreLoginBannerPolicyOwner = _CfprApAaaPreLoginBannerPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 26, 1, 9),
    _CfprApAaaPreLoginBannerPolicyOwner_Type()
)
cfprApAaaPreLoginBannerPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPreLoginBannerPolicyOwner.setStatus("current")
_CfprApAaaProviderGroupTable_Object = MibTable
cfprApAaaProviderGroupTable = _CfprApAaaProviderGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27)
)
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupTable.setStatus("current")
_CfprApAaaProviderGroupEntry_Object = MibTableRow
cfprApAaaProviderGroupEntry = _CfprApAaaProviderGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27, 1)
)
cfprApAaaProviderGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaProviderGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupEntry.setStatus("current")
_CfprApAaaProviderGroupInstanceId_Type = CfprApManagedObjectId
_CfprApAaaProviderGroupInstanceId_Object = MibTableColumn
cfprApAaaProviderGroupInstanceId = _CfprApAaaProviderGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27, 1, 1),
    _CfprApAaaProviderGroupInstanceId_Type()
)
cfprApAaaProviderGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupInstanceId.setStatus("current")
_CfprApAaaProviderGroupDn_Type = CfprApManagedObjectDn
_CfprApAaaProviderGroupDn_Object = MibTableColumn
cfprApAaaProviderGroupDn = _CfprApAaaProviderGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27, 1, 2),
    _CfprApAaaProviderGroupDn_Type()
)
cfprApAaaProviderGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupDn.setStatus("current")
_CfprApAaaProviderGroupRn_Type = SnmpAdminString
_CfprApAaaProviderGroupRn_Object = MibTableColumn
cfprApAaaProviderGroupRn = _CfprApAaaProviderGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27, 1, 3),
    _CfprApAaaProviderGroupRn_Type()
)
cfprApAaaProviderGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupRn.setStatus("current")
_CfprApAaaProviderGroupConfigState_Type = CfprApAaaConfigState
_CfprApAaaProviderGroupConfigState_Object = MibTableColumn
cfprApAaaProviderGroupConfigState = _CfprApAaaProviderGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27, 1, 4),
    _CfprApAaaProviderGroupConfigState_Type()
)
cfprApAaaProviderGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupConfigState.setStatus("current")
_CfprApAaaProviderGroupDescr_Type = SnmpAdminString
_CfprApAaaProviderGroupDescr_Object = MibTableColumn
cfprApAaaProviderGroupDescr = _CfprApAaaProviderGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27, 1, 5),
    _CfprApAaaProviderGroupDescr_Type()
)
cfprApAaaProviderGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupDescr.setStatus("current")
_CfprApAaaProviderGroupName_Type = SnmpAdminString
_CfprApAaaProviderGroupName_Object = MibTableColumn
cfprApAaaProviderGroupName = _CfprApAaaProviderGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27, 1, 6),
    _CfprApAaaProviderGroupName_Type()
)
cfprApAaaProviderGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupName.setStatus("current")
_CfprApAaaProviderGroupSize_Type = Gauge32
_CfprApAaaProviderGroupSize_Object = MibTableColumn
cfprApAaaProviderGroupSize = _CfprApAaaProviderGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 27, 1, 7),
    _CfprApAaaProviderGroupSize_Type()
)
cfprApAaaProviderGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderGroupSize.setStatus("current")
_CfprApAaaProviderRefTable_Object = MibTable
cfprApAaaProviderRefTable = _CfprApAaaProviderRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 28)
)
if mibBuilder.loadTexts:
    cfprApAaaProviderRefTable.setStatus("current")
_CfprApAaaProviderRefEntry_Object = MibTableRow
cfprApAaaProviderRefEntry = _CfprApAaaProviderRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 28, 1)
)
cfprApAaaProviderRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaProviderRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaProviderRefEntry.setStatus("current")
_CfprApAaaProviderRefInstanceId_Type = CfprApManagedObjectId
_CfprApAaaProviderRefInstanceId_Object = MibTableColumn
cfprApAaaProviderRefInstanceId = _CfprApAaaProviderRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 28, 1, 1),
    _CfprApAaaProviderRefInstanceId_Type()
)
cfprApAaaProviderRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaProviderRefInstanceId.setStatus("current")
_CfprApAaaProviderRefDn_Type = CfprApManagedObjectDn
_CfprApAaaProviderRefDn_Object = MibTableColumn
cfprApAaaProviderRefDn = _CfprApAaaProviderRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 28, 1, 2),
    _CfprApAaaProviderRefDn_Type()
)
cfprApAaaProviderRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderRefDn.setStatus("current")
_CfprApAaaProviderRefRn_Type = SnmpAdminString
_CfprApAaaProviderRefRn_Object = MibTableColumn
cfprApAaaProviderRefRn = _CfprApAaaProviderRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 28, 1, 3),
    _CfprApAaaProviderRefRn_Type()
)
cfprApAaaProviderRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderRefRn.setStatus("current")
_CfprApAaaProviderRefDescr_Type = SnmpAdminString
_CfprApAaaProviderRefDescr_Object = MibTableColumn
cfprApAaaProviderRefDescr = _CfprApAaaProviderRefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 28, 1, 4),
    _CfprApAaaProviderRefDescr_Type()
)
cfprApAaaProviderRefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderRefDescr.setStatus("current")
_CfprApAaaProviderRefName_Type = SnmpAdminString
_CfprApAaaProviderRefName_Object = MibTableColumn
cfprApAaaProviderRefName = _CfprApAaaProviderRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 28, 1, 5),
    _CfprApAaaProviderRefName_Type()
)
cfprApAaaProviderRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderRefName.setStatus("current")
_CfprApAaaProviderRefOrder_Type = Gauge32
_CfprApAaaProviderRefOrder_Object = MibTableColumn
cfprApAaaProviderRefOrder = _CfprApAaaProviderRefOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 28, 1, 6),
    _CfprApAaaProviderRefOrder_Type()
)
cfprApAaaProviderRefOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaProviderRefOrder.setStatus("current")
_CfprApAaaPwdProfileTable_Object = MibTable
cfprApAaaPwdProfileTable = _CfprApAaaPwdProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29)
)
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileTable.setStatus("current")
_CfprApAaaPwdProfileEntry_Object = MibTableRow
cfprApAaaPwdProfileEntry = _CfprApAaaPwdProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1)
)
cfprApAaaPwdProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaPwdProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileEntry.setStatus("current")
_CfprApAaaPwdProfileInstanceId_Type = CfprApManagedObjectId
_CfprApAaaPwdProfileInstanceId_Object = MibTableColumn
cfprApAaaPwdProfileInstanceId = _CfprApAaaPwdProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 1),
    _CfprApAaaPwdProfileInstanceId_Type()
)
cfprApAaaPwdProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileInstanceId.setStatus("current")
_CfprApAaaPwdProfileDn_Type = CfprApManagedObjectDn
_CfprApAaaPwdProfileDn_Object = MibTableColumn
cfprApAaaPwdProfileDn = _CfprApAaaPwdProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 2),
    _CfprApAaaPwdProfileDn_Type()
)
cfprApAaaPwdProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileDn.setStatus("current")
_CfprApAaaPwdProfileRn_Type = SnmpAdminString
_CfprApAaaPwdProfileRn_Object = MibTableColumn
cfprApAaaPwdProfileRn = _CfprApAaaPwdProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 3),
    _CfprApAaaPwdProfileRn_Type()
)
cfprApAaaPwdProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileRn.setStatus("current")
_CfprApAaaPwdProfileChangeCount_Type = Gauge32
_CfprApAaaPwdProfileChangeCount_Object = MibTableColumn
cfprApAaaPwdProfileChangeCount = _CfprApAaaPwdProfileChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 4),
    _CfprApAaaPwdProfileChangeCount_Type()
)
cfprApAaaPwdProfileChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileChangeCount.setStatus("current")
_CfprApAaaPwdProfileChangeDuringInterval_Type = CfprApAaaPwdPolicy
_CfprApAaaPwdProfileChangeDuringInterval_Object = MibTableColumn
cfprApAaaPwdProfileChangeDuringInterval = _CfprApAaaPwdProfileChangeDuringInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 5),
    _CfprApAaaPwdProfileChangeDuringInterval_Type()
)
cfprApAaaPwdProfileChangeDuringInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileChangeDuringInterval.setStatus("current")
_CfprApAaaPwdProfileChangeInterval_Type = Gauge32
_CfprApAaaPwdProfileChangeInterval_Object = MibTableColumn
cfprApAaaPwdProfileChangeInterval = _CfprApAaaPwdProfileChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 6),
    _CfprApAaaPwdProfileChangeInterval_Type()
)
cfprApAaaPwdProfileChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileChangeInterval.setStatus("current")
_CfprApAaaPwdProfileExpirationWarnTime_Type = Gauge32
_CfprApAaaPwdProfileExpirationWarnTime_Object = MibTableColumn
cfprApAaaPwdProfileExpirationWarnTime = _CfprApAaaPwdProfileExpirationWarnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 8),
    _CfprApAaaPwdProfileExpirationWarnTime_Type()
)
cfprApAaaPwdProfileExpirationWarnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileExpirationWarnTime.setStatus("current")
_CfprApAaaPwdProfileHistoryCount_Type = Gauge32
_CfprApAaaPwdProfileHistoryCount_Object = MibTableColumn
cfprApAaaPwdProfileHistoryCount = _CfprApAaaPwdProfileHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 9),
    _CfprApAaaPwdProfileHistoryCount_Type()
)
cfprApAaaPwdProfileHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileHistoryCount.setStatus("current")
_CfprApAaaPwdProfileNoChangeInterval_Type = Gauge32
_CfprApAaaPwdProfileNoChangeInterval_Object = MibTableColumn
cfprApAaaPwdProfileNoChangeInterval = _CfprApAaaPwdProfileNoChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 29, 1, 12),
    _CfprApAaaPwdProfileNoChangeInterval_Type()
)
cfprApAaaPwdProfileNoChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaPwdProfileNoChangeInterval.setStatus("current")
_CfprApAaaRadiusEpTable_Object = MibTable
cfprApAaaRadiusEpTable = _CfprApAaaRadiusEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30)
)
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpTable.setStatus("current")
_CfprApAaaRadiusEpEntry_Object = MibTableRow
cfprApAaaRadiusEpEntry = _CfprApAaaRadiusEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1)
)
cfprApAaaRadiusEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRadiusEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpEntry.setStatus("current")
_CfprApAaaRadiusEpInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRadiusEpInstanceId_Object = MibTableColumn
cfprApAaaRadiusEpInstanceId = _CfprApAaaRadiusEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 1),
    _CfprApAaaRadiusEpInstanceId_Type()
)
cfprApAaaRadiusEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpInstanceId.setStatus("current")
_CfprApAaaRadiusEpDn_Type = CfprApManagedObjectDn
_CfprApAaaRadiusEpDn_Object = MibTableColumn
cfprApAaaRadiusEpDn = _CfprApAaaRadiusEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 2),
    _CfprApAaaRadiusEpDn_Type()
)
cfprApAaaRadiusEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpDn.setStatus("current")
_CfprApAaaRadiusEpRn_Type = SnmpAdminString
_CfprApAaaRadiusEpRn_Object = MibTableColumn
cfprApAaaRadiusEpRn = _CfprApAaaRadiusEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 3),
    _CfprApAaaRadiusEpRn_Type()
)
cfprApAaaRadiusEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpRn.setStatus("current")
_CfprApAaaRadiusEpDescr_Type = SnmpAdminString
_CfprApAaaRadiusEpDescr_Object = MibTableColumn
cfprApAaaRadiusEpDescr = _CfprApAaaRadiusEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 4),
    _CfprApAaaRadiusEpDescr_Type()
)
cfprApAaaRadiusEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpDescr.setStatus("current")
_CfprApAaaRadiusEpFsmDescr_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmDescr_Object = MibTableColumn
cfprApAaaRadiusEpFsmDescr = _CfprApAaaRadiusEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 5),
    _CfprApAaaRadiusEpFsmDescr_Type()
)
cfprApAaaRadiusEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmDescr.setStatus("current")
_CfprApAaaRadiusEpFsmPrev_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmPrev_Object = MibTableColumn
cfprApAaaRadiusEpFsmPrev = _CfprApAaaRadiusEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 6),
    _CfprApAaaRadiusEpFsmPrev_Type()
)
cfprApAaaRadiusEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmPrev.setStatus("current")
_CfprApAaaRadiusEpFsmProgr_Type = Gauge32
_CfprApAaaRadiusEpFsmProgr_Object = MibTableColumn
cfprApAaaRadiusEpFsmProgr = _CfprApAaaRadiusEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 7),
    _CfprApAaaRadiusEpFsmProgr_Type()
)
cfprApAaaRadiusEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmProgr.setStatus("current")
_CfprApAaaRadiusEpFsmRmtInvErrCode_Type = Gauge32
_CfprApAaaRadiusEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApAaaRadiusEpFsmRmtInvErrCode = _CfprApAaaRadiusEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 8),
    _CfprApAaaRadiusEpFsmRmtInvErrCode_Type()
)
cfprApAaaRadiusEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmRmtInvErrCode.setStatus("current")
_CfprApAaaRadiusEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApAaaRadiusEpFsmRmtInvErrDescr = _CfprApAaaRadiusEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 9),
    _CfprApAaaRadiusEpFsmRmtInvErrDescr_Type()
)
cfprApAaaRadiusEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmRmtInvErrDescr.setStatus("current")
_CfprApAaaRadiusEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaRadiusEpFsmRmtInvRslt_Object = MibTableColumn
cfprApAaaRadiusEpFsmRmtInvRslt = _CfprApAaaRadiusEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 10),
    _CfprApAaaRadiusEpFsmRmtInvRslt_Type()
)
cfprApAaaRadiusEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmRmtInvRslt.setStatus("current")
_CfprApAaaRadiusEpFsmStageDescr_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmStageDescr_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageDescr = _CfprApAaaRadiusEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 11),
    _CfprApAaaRadiusEpFsmStageDescr_Type()
)
cfprApAaaRadiusEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageDescr.setStatus("current")
_CfprApAaaRadiusEpFsmStamp_Type = DateAndTime
_CfprApAaaRadiusEpFsmStamp_Object = MibTableColumn
cfprApAaaRadiusEpFsmStamp = _CfprApAaaRadiusEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 12),
    _CfprApAaaRadiusEpFsmStamp_Type()
)
cfprApAaaRadiusEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStamp.setStatus("current")
_CfprApAaaRadiusEpFsmStatus_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmStatus_Object = MibTableColumn
cfprApAaaRadiusEpFsmStatus = _CfprApAaaRadiusEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 13),
    _CfprApAaaRadiusEpFsmStatus_Type()
)
cfprApAaaRadiusEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStatus.setStatus("current")
_CfprApAaaRadiusEpFsmTry_Type = Gauge32
_CfprApAaaRadiusEpFsmTry_Object = MibTableColumn
cfprApAaaRadiusEpFsmTry = _CfprApAaaRadiusEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 14),
    _CfprApAaaRadiusEpFsmTry_Type()
)
cfprApAaaRadiusEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmTry.setStatus("current")
_CfprApAaaRadiusEpIntId_Type = SnmpAdminString
_CfprApAaaRadiusEpIntId_Object = MibTableColumn
cfprApAaaRadiusEpIntId = _CfprApAaaRadiusEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 15),
    _CfprApAaaRadiusEpIntId_Type()
)
cfprApAaaRadiusEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpIntId.setStatus("current")
_CfprApAaaRadiusEpName_Type = SnmpAdminString
_CfprApAaaRadiusEpName_Object = MibTableColumn
cfprApAaaRadiusEpName = _CfprApAaaRadiusEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 16),
    _CfprApAaaRadiusEpName_Type()
)
cfprApAaaRadiusEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpName.setStatus("current")
_CfprApAaaRadiusEpPolicyLevel_Type = Gauge32
_CfprApAaaRadiusEpPolicyLevel_Object = MibTableColumn
cfprApAaaRadiusEpPolicyLevel = _CfprApAaaRadiusEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 17),
    _CfprApAaaRadiusEpPolicyLevel_Type()
)
cfprApAaaRadiusEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpPolicyLevel.setStatus("current")
_CfprApAaaRadiusEpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaRadiusEpPolicyOwner_Object = MibTableColumn
cfprApAaaRadiusEpPolicyOwner = _CfprApAaaRadiusEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 18),
    _CfprApAaaRadiusEpPolicyOwner_Type()
)
cfprApAaaRadiusEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpPolicyOwner.setStatus("current")
_CfprApAaaRadiusEpRetries_Type = Gauge32
_CfprApAaaRadiusEpRetries_Object = MibTableColumn
cfprApAaaRadiusEpRetries = _CfprApAaaRadiusEpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 19),
    _CfprApAaaRadiusEpRetries_Type()
)
cfprApAaaRadiusEpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpRetries.setStatus("current")
_CfprApAaaRadiusEpTimeout_Type = Gauge32
_CfprApAaaRadiusEpTimeout_Object = MibTableColumn
cfprApAaaRadiusEpTimeout = _CfprApAaaRadiusEpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 30, 1, 20),
    _CfprApAaaRadiusEpTimeout_Type()
)
cfprApAaaRadiusEpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpTimeout.setStatus("current")
_CfprApAaaRadiusEpFsmTable_Object = MibTable
cfprApAaaRadiusEpFsmTable = _CfprApAaaRadiusEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31)
)
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmTable.setStatus("current")
_CfprApAaaRadiusEpFsmEntry_Object = MibTableRow
cfprApAaaRadiusEpFsmEntry = _CfprApAaaRadiusEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1)
)
cfprApAaaRadiusEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRadiusEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmEntry.setStatus("current")
_CfprApAaaRadiusEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRadiusEpFsmInstanceId_Object = MibTableColumn
cfprApAaaRadiusEpFsmInstanceId = _CfprApAaaRadiusEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 1),
    _CfprApAaaRadiusEpFsmInstanceId_Type()
)
cfprApAaaRadiusEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmInstanceId.setStatus("current")
_CfprApAaaRadiusEpFsmDn_Type = CfprApManagedObjectDn
_CfprApAaaRadiusEpFsmDn_Object = MibTableColumn
cfprApAaaRadiusEpFsmDn = _CfprApAaaRadiusEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 2),
    _CfprApAaaRadiusEpFsmDn_Type()
)
cfprApAaaRadiusEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmDn.setStatus("current")
_CfprApAaaRadiusEpFsmRn_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmRn_Object = MibTableColumn
cfprApAaaRadiusEpFsmRn = _CfprApAaaRadiusEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 3),
    _CfprApAaaRadiusEpFsmRn_Type()
)
cfprApAaaRadiusEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmRn.setStatus("current")
_CfprApAaaRadiusEpFsmCompletionTime_Type = DateAndTime
_CfprApAaaRadiusEpFsmCompletionTime_Object = MibTableColumn
cfprApAaaRadiusEpFsmCompletionTime = _CfprApAaaRadiusEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 4),
    _CfprApAaaRadiusEpFsmCompletionTime_Type()
)
cfprApAaaRadiusEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmCompletionTime.setStatus("current")
_CfprApAaaRadiusEpFsmCurrentFsm_Type = CfprApAaaRadiusEpFsmCurrentFsm
_CfprApAaaRadiusEpFsmCurrentFsm_Object = MibTableColumn
cfprApAaaRadiusEpFsmCurrentFsm = _CfprApAaaRadiusEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 5),
    _CfprApAaaRadiusEpFsmCurrentFsm_Type()
)
cfprApAaaRadiusEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmCurrentFsm.setStatus("current")
_CfprApAaaRadiusEpFsmDescrData_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmDescrData_Object = MibTableColumn
cfprApAaaRadiusEpFsmDescrData = _CfprApAaaRadiusEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 6),
    _CfprApAaaRadiusEpFsmDescrData_Type()
)
cfprApAaaRadiusEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmDescrData.setStatus("current")
_CfprApAaaRadiusEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaRadiusEpFsmFsmStatus_Object = MibTableColumn
cfprApAaaRadiusEpFsmFsmStatus = _CfprApAaaRadiusEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 7),
    _CfprApAaaRadiusEpFsmFsmStatus_Type()
)
cfprApAaaRadiusEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmFsmStatus.setStatus("current")
_CfprApAaaRadiusEpFsmProgress_Type = Gauge32
_CfprApAaaRadiusEpFsmProgress_Object = MibTableColumn
cfprApAaaRadiusEpFsmProgress = _CfprApAaaRadiusEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 8),
    _CfprApAaaRadiusEpFsmProgress_Type()
)
cfprApAaaRadiusEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmProgress.setStatus("current")
_CfprApAaaRadiusEpFsmRmtErrCode_Type = Gauge32
_CfprApAaaRadiusEpFsmRmtErrCode_Object = MibTableColumn
cfprApAaaRadiusEpFsmRmtErrCode = _CfprApAaaRadiusEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 9),
    _CfprApAaaRadiusEpFsmRmtErrCode_Type()
)
cfprApAaaRadiusEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmRmtErrCode.setStatus("current")
_CfprApAaaRadiusEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmRmtErrDescr_Object = MibTableColumn
cfprApAaaRadiusEpFsmRmtErrDescr = _CfprApAaaRadiusEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 10),
    _CfprApAaaRadiusEpFsmRmtErrDescr_Type()
)
cfprApAaaRadiusEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmRmtErrDescr.setStatus("current")
_CfprApAaaRadiusEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaRadiusEpFsmRmtRslt_Object = MibTableColumn
cfprApAaaRadiusEpFsmRmtRslt = _CfprApAaaRadiusEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 31, 1, 11),
    _CfprApAaaRadiusEpFsmRmtRslt_Type()
)
cfprApAaaRadiusEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmRmtRslt.setStatus("current")
_CfprApAaaRadiusEpFsmStageTable_Object = MibTable
cfprApAaaRadiusEpFsmStageTable = _CfprApAaaRadiusEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32)
)
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageTable.setStatus("current")
_CfprApAaaRadiusEpFsmStageEntry_Object = MibTableRow
cfprApAaaRadiusEpFsmStageEntry = _CfprApAaaRadiusEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1)
)
cfprApAaaRadiusEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRadiusEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageEntry.setStatus("current")
_CfprApAaaRadiusEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRadiusEpFsmStageInstanceId_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageInstanceId = _CfprApAaaRadiusEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 1),
    _CfprApAaaRadiusEpFsmStageInstanceId_Type()
)
cfprApAaaRadiusEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageInstanceId.setStatus("current")
_CfprApAaaRadiusEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApAaaRadiusEpFsmStageDn_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageDn = _CfprApAaaRadiusEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 2),
    _CfprApAaaRadiusEpFsmStageDn_Type()
)
cfprApAaaRadiusEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageDn.setStatus("current")
_CfprApAaaRadiusEpFsmStageRn_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmStageRn_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageRn = _CfprApAaaRadiusEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 3),
    _CfprApAaaRadiusEpFsmStageRn_Type()
)
cfprApAaaRadiusEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageRn.setStatus("current")
_CfprApAaaRadiusEpFsmStageDescrData_Type = SnmpAdminString
_CfprApAaaRadiusEpFsmStageDescrData_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageDescrData = _CfprApAaaRadiusEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 4),
    _CfprApAaaRadiusEpFsmStageDescrData_Type()
)
cfprApAaaRadiusEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageDescrData.setStatus("current")
_CfprApAaaRadiusEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApAaaRadiusEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageLastUpdateTime = _CfprApAaaRadiusEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 5),
    _CfprApAaaRadiusEpFsmStageLastUpdateTime_Type()
)
cfprApAaaRadiusEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageLastUpdateTime.setStatus("current")
_CfprApAaaRadiusEpFsmStageName_Type = CfprApAaaRadiusEpFsmStageName
_CfprApAaaRadiusEpFsmStageName_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageName = _CfprApAaaRadiusEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 6),
    _CfprApAaaRadiusEpFsmStageName_Type()
)
cfprApAaaRadiusEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageName.setStatus("current")
_CfprApAaaRadiusEpFsmStageOrder_Type = Gauge32
_CfprApAaaRadiusEpFsmStageOrder_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageOrder = _CfprApAaaRadiusEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 7),
    _CfprApAaaRadiusEpFsmStageOrder_Type()
)
cfprApAaaRadiusEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageOrder.setStatus("current")
_CfprApAaaRadiusEpFsmStageRetry_Type = Gauge32
_CfprApAaaRadiusEpFsmStageRetry_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageRetry = _CfprApAaaRadiusEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 8),
    _CfprApAaaRadiusEpFsmStageRetry_Type()
)
cfprApAaaRadiusEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageRetry.setStatus("current")
_CfprApAaaRadiusEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaRadiusEpFsmStageStageStatus_Object = MibTableColumn
cfprApAaaRadiusEpFsmStageStageStatus = _CfprApAaaRadiusEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 32, 1, 9),
    _CfprApAaaRadiusEpFsmStageStageStatus_Type()
)
cfprApAaaRadiusEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusEpFsmStageStageStatus.setStatus("current")
_CfprApAaaRadiusProviderTable_Object = MibTable
cfprApAaaRadiusProviderTable = _CfprApAaaRadiusProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33)
)
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderTable.setStatus("current")
_CfprApAaaRadiusProviderEntry_Object = MibTableRow
cfprApAaaRadiusProviderEntry = _CfprApAaaRadiusProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1)
)
cfprApAaaRadiusProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRadiusProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderEntry.setStatus("current")
_CfprApAaaRadiusProviderInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRadiusProviderInstanceId_Object = MibTableColumn
cfprApAaaRadiusProviderInstanceId = _CfprApAaaRadiusProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 1),
    _CfprApAaaRadiusProviderInstanceId_Type()
)
cfprApAaaRadiusProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderInstanceId.setStatus("current")
_CfprApAaaRadiusProviderDn_Type = CfprApManagedObjectDn
_CfprApAaaRadiusProviderDn_Object = MibTableColumn
cfprApAaaRadiusProviderDn = _CfprApAaaRadiusProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 2),
    _CfprApAaaRadiusProviderDn_Type()
)
cfprApAaaRadiusProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderDn.setStatus("current")
_CfprApAaaRadiusProviderRn_Type = SnmpAdminString
_CfprApAaaRadiusProviderRn_Object = MibTableColumn
cfprApAaaRadiusProviderRn = _CfprApAaaRadiusProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 3),
    _CfprApAaaRadiusProviderRn_Type()
)
cfprApAaaRadiusProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderRn.setStatus("current")
_CfprApAaaRadiusProviderAuthPort_Type = Gauge32
_CfprApAaaRadiusProviderAuthPort_Object = MibTableColumn
cfprApAaaRadiusProviderAuthPort = _CfprApAaaRadiusProviderAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 4),
    _CfprApAaaRadiusProviderAuthPort_Type()
)
cfprApAaaRadiusProviderAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderAuthPort.setStatus("current")
_CfprApAaaRadiusProviderDescr_Type = SnmpAdminString
_CfprApAaaRadiusProviderDescr_Object = MibTableColumn
cfprApAaaRadiusProviderDescr = _CfprApAaaRadiusProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 5),
    _CfprApAaaRadiusProviderDescr_Type()
)
cfprApAaaRadiusProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderDescr.setStatus("current")
_CfprApAaaRadiusProviderEncKey_Type = SnmpAdminString
_CfprApAaaRadiusProviderEncKey_Object = MibTableColumn
cfprApAaaRadiusProviderEncKey = _CfprApAaaRadiusProviderEncKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 6),
    _CfprApAaaRadiusProviderEncKey_Type()
)
cfprApAaaRadiusProviderEncKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderEncKey.setStatus("current")
_CfprApAaaRadiusProviderKey_Type = SnmpAdminString
_CfprApAaaRadiusProviderKey_Object = MibTableColumn
cfprApAaaRadiusProviderKey = _CfprApAaaRadiusProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 7),
    _CfprApAaaRadiusProviderKey_Type()
)
cfprApAaaRadiusProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderKey.setStatus("current")
_CfprApAaaRadiusProviderKeySet_Type = TruthValue
_CfprApAaaRadiusProviderKeySet_Object = MibTableColumn
cfprApAaaRadiusProviderKeySet = _CfprApAaaRadiusProviderKeySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 8),
    _CfprApAaaRadiusProviderKeySet_Type()
)
cfprApAaaRadiusProviderKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderKeySet.setStatus("current")
_CfprApAaaRadiusProviderName_Type = SnmpAdminString
_CfprApAaaRadiusProviderName_Object = MibTableColumn
cfprApAaaRadiusProviderName = _CfprApAaaRadiusProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 9),
    _CfprApAaaRadiusProviderName_Type()
)
cfprApAaaRadiusProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderName.setStatus("current")
_CfprApAaaRadiusProviderOrder_Type = Gauge32
_CfprApAaaRadiusProviderOrder_Object = MibTableColumn
cfprApAaaRadiusProviderOrder = _CfprApAaaRadiusProviderOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 10),
    _CfprApAaaRadiusProviderOrder_Type()
)
cfprApAaaRadiusProviderOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderOrder.setStatus("current")
_CfprApAaaRadiusProviderRetries_Type = Gauge32
_CfprApAaaRadiusProviderRetries_Object = MibTableColumn
cfprApAaaRadiusProviderRetries = _CfprApAaaRadiusProviderRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 11),
    _CfprApAaaRadiusProviderRetries_Type()
)
cfprApAaaRadiusProviderRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderRetries.setStatus("current")
_CfprApAaaRadiusProviderService_Type = CfprApAaaRadiusService
_CfprApAaaRadiusProviderService_Object = MibTableColumn
cfprApAaaRadiusProviderService = _CfprApAaaRadiusProviderService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 12),
    _CfprApAaaRadiusProviderService_Type()
)
cfprApAaaRadiusProviderService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderService.setStatus("current")
_CfprApAaaRadiusProviderTimeout_Type = Gauge32
_CfprApAaaRadiusProviderTimeout_Object = MibTableColumn
cfprApAaaRadiusProviderTimeout = _CfprApAaaRadiusProviderTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 33, 1, 13),
    _CfprApAaaRadiusProviderTimeout_Type()
)
cfprApAaaRadiusProviderTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRadiusProviderTimeout.setStatus("current")
_CfprApAaaRealmFsmTable_Object = MibTable
cfprApAaaRealmFsmTable = _CfprApAaaRealmFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34)
)
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTable.setStatus("current")
_CfprApAaaRealmFsmEntry_Object = MibTableRow
cfprApAaaRealmFsmEntry = _CfprApAaaRealmFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1)
)
cfprApAaaRealmFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRealmFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmEntry.setStatus("current")
_CfprApAaaRealmFsmInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRealmFsmInstanceId_Object = MibTableColumn
cfprApAaaRealmFsmInstanceId = _CfprApAaaRealmFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 1),
    _CfprApAaaRealmFsmInstanceId_Type()
)
cfprApAaaRealmFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmInstanceId.setStatus("current")
_CfprApAaaRealmFsmDn_Type = CfprApManagedObjectDn
_CfprApAaaRealmFsmDn_Object = MibTableColumn
cfprApAaaRealmFsmDn = _CfprApAaaRealmFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 2),
    _CfprApAaaRealmFsmDn_Type()
)
cfprApAaaRealmFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmDn.setStatus("current")
_CfprApAaaRealmFsmRn_Type = SnmpAdminString
_CfprApAaaRealmFsmRn_Object = MibTableColumn
cfprApAaaRealmFsmRn = _CfprApAaaRealmFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 3),
    _CfprApAaaRealmFsmRn_Type()
)
cfprApAaaRealmFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmRn.setStatus("current")
_CfprApAaaRealmFsmCompletionTime_Type = DateAndTime
_CfprApAaaRealmFsmCompletionTime_Object = MibTableColumn
cfprApAaaRealmFsmCompletionTime = _CfprApAaaRealmFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 4),
    _CfprApAaaRealmFsmCompletionTime_Type()
)
cfprApAaaRealmFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmCompletionTime.setStatus("current")
_CfprApAaaRealmFsmCurrentFsm_Type = CfprApAaaRealmFsmCurrentFsm
_CfprApAaaRealmFsmCurrentFsm_Object = MibTableColumn
cfprApAaaRealmFsmCurrentFsm = _CfprApAaaRealmFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 5),
    _CfprApAaaRealmFsmCurrentFsm_Type()
)
cfprApAaaRealmFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmCurrentFsm.setStatus("current")
_CfprApAaaRealmFsmDescr_Type = SnmpAdminString
_CfprApAaaRealmFsmDescr_Object = MibTableColumn
cfprApAaaRealmFsmDescr = _CfprApAaaRealmFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 6),
    _CfprApAaaRealmFsmDescr_Type()
)
cfprApAaaRealmFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmDescr.setStatus("current")
_CfprApAaaRealmFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaRealmFsmFsmStatus_Object = MibTableColumn
cfprApAaaRealmFsmFsmStatus = _CfprApAaaRealmFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 7),
    _CfprApAaaRealmFsmFsmStatus_Type()
)
cfprApAaaRealmFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmFsmStatus.setStatus("current")
_CfprApAaaRealmFsmProgress_Type = Gauge32
_CfprApAaaRealmFsmProgress_Object = MibTableColumn
cfprApAaaRealmFsmProgress = _CfprApAaaRealmFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 8),
    _CfprApAaaRealmFsmProgress_Type()
)
cfprApAaaRealmFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmProgress.setStatus("current")
_CfprApAaaRealmFsmRmtErrCode_Type = Gauge32
_CfprApAaaRealmFsmRmtErrCode_Object = MibTableColumn
cfprApAaaRealmFsmRmtErrCode = _CfprApAaaRealmFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 9),
    _CfprApAaaRealmFsmRmtErrCode_Type()
)
cfprApAaaRealmFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmRmtErrCode.setStatus("current")
_CfprApAaaRealmFsmRmtErrDescr_Type = SnmpAdminString
_CfprApAaaRealmFsmRmtErrDescr_Object = MibTableColumn
cfprApAaaRealmFsmRmtErrDescr = _CfprApAaaRealmFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 10),
    _CfprApAaaRealmFsmRmtErrDescr_Type()
)
cfprApAaaRealmFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmRmtErrDescr.setStatus("current")
_CfprApAaaRealmFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaRealmFsmRmtRslt_Object = MibTableColumn
cfprApAaaRealmFsmRmtRslt = _CfprApAaaRealmFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 34, 1, 11),
    _CfprApAaaRealmFsmRmtRslt_Type()
)
cfprApAaaRealmFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmRmtRslt.setStatus("current")
_CfprApAaaRealmFsmStageTable_Object = MibTable
cfprApAaaRealmFsmStageTable = _CfprApAaaRealmFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35)
)
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageTable.setStatus("current")
_CfprApAaaRealmFsmStageEntry_Object = MibTableRow
cfprApAaaRealmFsmStageEntry = _CfprApAaaRealmFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1)
)
cfprApAaaRealmFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRealmFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageEntry.setStatus("current")
_CfprApAaaRealmFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRealmFsmStageInstanceId_Object = MibTableColumn
cfprApAaaRealmFsmStageInstanceId = _CfprApAaaRealmFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 1),
    _CfprApAaaRealmFsmStageInstanceId_Type()
)
cfprApAaaRealmFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageInstanceId.setStatus("current")
_CfprApAaaRealmFsmStageDn_Type = CfprApManagedObjectDn
_CfprApAaaRealmFsmStageDn_Object = MibTableColumn
cfprApAaaRealmFsmStageDn = _CfprApAaaRealmFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 2),
    _CfprApAaaRealmFsmStageDn_Type()
)
cfprApAaaRealmFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageDn.setStatus("current")
_CfprApAaaRealmFsmStageRn_Type = SnmpAdminString
_CfprApAaaRealmFsmStageRn_Object = MibTableColumn
cfprApAaaRealmFsmStageRn = _CfprApAaaRealmFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 3),
    _CfprApAaaRealmFsmStageRn_Type()
)
cfprApAaaRealmFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageRn.setStatus("current")
_CfprApAaaRealmFsmStageDescr_Type = SnmpAdminString
_CfprApAaaRealmFsmStageDescr_Object = MibTableColumn
cfprApAaaRealmFsmStageDescr = _CfprApAaaRealmFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 4),
    _CfprApAaaRealmFsmStageDescr_Type()
)
cfprApAaaRealmFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageDescr.setStatus("current")
_CfprApAaaRealmFsmStageLastUpdateTime_Type = DateAndTime
_CfprApAaaRealmFsmStageLastUpdateTime_Object = MibTableColumn
cfprApAaaRealmFsmStageLastUpdateTime = _CfprApAaaRealmFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 5),
    _CfprApAaaRealmFsmStageLastUpdateTime_Type()
)
cfprApAaaRealmFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageLastUpdateTime.setStatus("current")
_CfprApAaaRealmFsmStageName_Type = CfprApAaaRealmFsmStageName
_CfprApAaaRealmFsmStageName_Object = MibTableColumn
cfprApAaaRealmFsmStageName = _CfprApAaaRealmFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 6),
    _CfprApAaaRealmFsmStageName_Type()
)
cfprApAaaRealmFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageName.setStatus("current")
_CfprApAaaRealmFsmStageOrder_Type = Gauge32
_CfprApAaaRealmFsmStageOrder_Object = MibTableColumn
cfprApAaaRealmFsmStageOrder = _CfprApAaaRealmFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 7),
    _CfprApAaaRealmFsmStageOrder_Type()
)
cfprApAaaRealmFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageOrder.setStatus("current")
_CfprApAaaRealmFsmStageRetry_Type = Gauge32
_CfprApAaaRealmFsmStageRetry_Object = MibTableColumn
cfprApAaaRealmFsmStageRetry = _CfprApAaaRealmFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 8),
    _CfprApAaaRealmFsmStageRetry_Type()
)
cfprApAaaRealmFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageRetry.setStatus("current")
_CfprApAaaRealmFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaRealmFsmStageStageStatus_Object = MibTableColumn
cfprApAaaRealmFsmStageStageStatus = _CfprApAaaRealmFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 35, 1, 9),
    _CfprApAaaRealmFsmStageStageStatus_Type()
)
cfprApAaaRealmFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmStageStageStatus.setStatus("current")
_CfprApAaaRealmFsmTaskTable_Object = MibTable
cfprApAaaRealmFsmTaskTable = _CfprApAaaRealmFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36)
)
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskTable.setStatus("current")
_CfprApAaaRealmFsmTaskEntry_Object = MibTableRow
cfprApAaaRealmFsmTaskEntry = _CfprApAaaRealmFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36, 1)
)
cfprApAaaRealmFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRealmFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskEntry.setStatus("current")
_CfprApAaaRealmFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRealmFsmTaskInstanceId_Object = MibTableColumn
cfprApAaaRealmFsmTaskInstanceId = _CfprApAaaRealmFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36, 1, 1),
    _CfprApAaaRealmFsmTaskInstanceId_Type()
)
cfprApAaaRealmFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskInstanceId.setStatus("current")
_CfprApAaaRealmFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApAaaRealmFsmTaskDn_Object = MibTableColumn
cfprApAaaRealmFsmTaskDn = _CfprApAaaRealmFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36, 1, 2),
    _CfprApAaaRealmFsmTaskDn_Type()
)
cfprApAaaRealmFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskDn.setStatus("current")
_CfprApAaaRealmFsmTaskRn_Type = SnmpAdminString
_CfprApAaaRealmFsmTaskRn_Object = MibTableColumn
cfprApAaaRealmFsmTaskRn = _CfprApAaaRealmFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36, 1, 3),
    _CfprApAaaRealmFsmTaskRn_Type()
)
cfprApAaaRealmFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskRn.setStatus("current")
_CfprApAaaRealmFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApAaaRealmFsmTaskCompletion_Object = MibTableColumn
cfprApAaaRealmFsmTaskCompletion = _CfprApAaaRealmFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36, 1, 4),
    _CfprApAaaRealmFsmTaskCompletion_Type()
)
cfprApAaaRealmFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskCompletion.setStatus("current")
_CfprApAaaRealmFsmTaskFlags_Type = CfprApFsmFlags
_CfprApAaaRealmFsmTaskFlags_Object = MibTableColumn
cfprApAaaRealmFsmTaskFlags = _CfprApAaaRealmFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36, 1, 5),
    _CfprApAaaRealmFsmTaskFlags_Type()
)
cfprApAaaRealmFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskFlags.setStatus("current")
_CfprApAaaRealmFsmTaskItem_Type = CfprApAaaRealmFsmTaskItem
_CfprApAaaRealmFsmTaskItem_Object = MibTableColumn
cfprApAaaRealmFsmTaskItem = _CfprApAaaRealmFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36, 1, 6),
    _CfprApAaaRealmFsmTaskItem_Type()
)
cfprApAaaRealmFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskItem.setStatus("current")
_CfprApAaaRealmFsmTaskSeqId_Type = Gauge32
_CfprApAaaRealmFsmTaskSeqId_Object = MibTableColumn
cfprApAaaRealmFsmTaskSeqId = _CfprApAaaRealmFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 36, 1, 7),
    _CfprApAaaRealmFsmTaskSeqId_Type()
)
cfprApAaaRealmFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRealmFsmTaskSeqId.setStatus("current")
_CfprApAaaRemoteUserTable_Object = MibTable
cfprApAaaRemoteUserTable = _CfprApAaaRemoteUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37)
)
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserTable.setStatus("current")
_CfprApAaaRemoteUserEntry_Object = MibTableRow
cfprApAaaRemoteUserEntry = _CfprApAaaRemoteUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1)
)
cfprApAaaRemoteUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRemoteUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserEntry.setStatus("current")
_CfprApAaaRemoteUserInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRemoteUserInstanceId_Object = MibTableColumn
cfprApAaaRemoteUserInstanceId = _CfprApAaaRemoteUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 1),
    _CfprApAaaRemoteUserInstanceId_Type()
)
cfprApAaaRemoteUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserInstanceId.setStatus("current")
_CfprApAaaRemoteUserDn_Type = CfprApManagedObjectDn
_CfprApAaaRemoteUserDn_Object = MibTableColumn
cfprApAaaRemoteUserDn = _CfprApAaaRemoteUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 2),
    _CfprApAaaRemoteUserDn_Type()
)
cfprApAaaRemoteUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserDn.setStatus("current")
_CfprApAaaRemoteUserRn_Type = SnmpAdminString
_CfprApAaaRemoteUserRn_Object = MibTableColumn
cfprApAaaRemoteUserRn = _CfprApAaaRemoteUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 3),
    _CfprApAaaRemoteUserRn_Type()
)
cfprApAaaRemoteUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserRn.setStatus("current")
_CfprApAaaRemoteUserConfigState_Type = CfprApAaaConfigState
_CfprApAaaRemoteUserConfigState_Object = MibTableColumn
cfprApAaaRemoteUserConfigState = _CfprApAaaRemoteUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 4),
    _CfprApAaaRemoteUserConfigState_Type()
)
cfprApAaaRemoteUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserConfigState.setStatus("current")
_CfprApAaaRemoteUserConfigStatusMessage_Type = SnmpAdminString
_CfprApAaaRemoteUserConfigStatusMessage_Object = MibTableColumn
cfprApAaaRemoteUserConfigStatusMessage = _CfprApAaaRemoteUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 5),
    _CfprApAaaRemoteUserConfigStatusMessage_Type()
)
cfprApAaaRemoteUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserConfigStatusMessage.setStatus("current")
_CfprApAaaRemoteUserDescr_Type = SnmpAdminString
_CfprApAaaRemoteUserDescr_Object = MibTableColumn
cfprApAaaRemoteUserDescr = _CfprApAaaRemoteUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 6),
    _CfprApAaaRemoteUserDescr_Type()
)
cfprApAaaRemoteUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserDescr.setStatus("current")
_CfprApAaaRemoteUserName_Type = SnmpAdminString
_CfprApAaaRemoteUserName_Object = MibTableColumn
cfprApAaaRemoteUserName = _CfprApAaaRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 7),
    _CfprApAaaRemoteUserName_Type()
)
cfprApAaaRemoteUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserName.setStatus("current")
_CfprApAaaRemoteUserPwd_Type = SnmpAdminString
_CfprApAaaRemoteUserPwd_Object = MibTableColumn
cfprApAaaRemoteUserPwd = _CfprApAaaRemoteUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 8),
    _CfprApAaaRemoteUserPwd_Type()
)
cfprApAaaRemoteUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserPwd.setStatus("current")
_CfprApAaaRemoteUserPwdSet_Type = TruthValue
_CfprApAaaRemoteUserPwdSet_Object = MibTableColumn
cfprApAaaRemoteUserPwdSet = _CfprApAaaRemoteUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 37, 1, 9),
    _CfprApAaaRemoteUserPwdSet_Type()
)
cfprApAaaRemoteUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRemoteUserPwdSet.setStatus("current")
_CfprApAaaRoleTable_Object = MibTable
cfprApAaaRoleTable = _CfprApAaaRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38)
)
if mibBuilder.loadTexts:
    cfprApAaaRoleTable.setStatus("current")
_CfprApAaaRoleEntry_Object = MibTableRow
cfprApAaaRoleEntry = _CfprApAaaRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1)
)
cfprApAaaRoleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaRoleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaRoleEntry.setStatus("current")
_CfprApAaaRoleInstanceId_Type = CfprApManagedObjectId
_CfprApAaaRoleInstanceId_Object = MibTableColumn
cfprApAaaRoleInstanceId = _CfprApAaaRoleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 1),
    _CfprApAaaRoleInstanceId_Type()
)
cfprApAaaRoleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaRoleInstanceId.setStatus("current")
_CfprApAaaRoleDn_Type = CfprApManagedObjectDn
_CfprApAaaRoleDn_Object = MibTableColumn
cfprApAaaRoleDn = _CfprApAaaRoleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 2),
    _CfprApAaaRoleDn_Type()
)
cfprApAaaRoleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRoleDn.setStatus("current")
_CfprApAaaRoleRn_Type = SnmpAdminString
_CfprApAaaRoleRn_Object = MibTableColumn
cfprApAaaRoleRn = _CfprApAaaRoleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 3),
    _CfprApAaaRoleRn_Type()
)
cfprApAaaRoleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRoleRn.setStatus("current")
_CfprApAaaRoleConfigState_Type = CfprApAaaConfigState
_CfprApAaaRoleConfigState_Object = MibTableColumn
cfprApAaaRoleConfigState = _CfprApAaaRoleConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 4),
    _CfprApAaaRoleConfigState_Type()
)
cfprApAaaRoleConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRoleConfigState.setStatus("current")
_CfprApAaaRoleConfigStatusMessage_Type = SnmpAdminString
_CfprApAaaRoleConfigStatusMessage_Object = MibTableColumn
cfprApAaaRoleConfigStatusMessage = _CfprApAaaRoleConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 5),
    _CfprApAaaRoleConfigStatusMessage_Type()
)
cfprApAaaRoleConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRoleConfigStatusMessage.setStatus("current")
_CfprApAaaRoleDescr_Type = SnmpAdminString
_CfprApAaaRoleDescr_Object = MibTableColumn
cfprApAaaRoleDescr = _CfprApAaaRoleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 6),
    _CfprApAaaRoleDescr_Type()
)
cfprApAaaRoleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRoleDescr.setStatus("current")
_CfprApAaaRoleIntId_Type = SnmpAdminString
_CfprApAaaRoleIntId_Object = MibTableColumn
cfprApAaaRoleIntId = _CfprApAaaRoleIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 7),
    _CfprApAaaRoleIntId_Type()
)
cfprApAaaRoleIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRoleIntId.setStatus("current")
_CfprApAaaRoleName_Type = SnmpAdminString
_CfprApAaaRoleName_Object = MibTableColumn
cfprApAaaRoleName = _CfprApAaaRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 8),
    _CfprApAaaRoleName_Type()
)
cfprApAaaRoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRoleName.setStatus("current")
_CfprApAaaRolePolicyLevel_Type = Gauge32
_CfprApAaaRolePolicyLevel_Object = MibTableColumn
cfprApAaaRolePolicyLevel = _CfprApAaaRolePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 9),
    _CfprApAaaRolePolicyLevel_Type()
)
cfprApAaaRolePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRolePolicyLevel.setStatus("current")
_CfprApAaaRolePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaRolePolicyOwner_Object = MibTableColumn
cfprApAaaRolePolicyOwner = _CfprApAaaRolePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 10),
    _CfprApAaaRolePolicyOwner_Type()
)
cfprApAaaRolePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRolePolicyOwner.setStatus("current")
_CfprApAaaRolePriv_Type = CfprApAaaAccess
_CfprApAaaRolePriv_Object = MibTableColumn
cfprApAaaRolePriv = _CfprApAaaRolePriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 38, 1, 11),
    _CfprApAaaRolePriv_Type()
)
cfprApAaaRolePriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaRolePriv.setStatus("current")
_CfprApAaaSessionTable_Object = MibTable
cfprApAaaSessionTable = _CfprApAaaSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39)
)
if mibBuilder.loadTexts:
    cfprApAaaSessionTable.setStatus("current")
_CfprApAaaSessionEntry_Object = MibTableRow
cfprApAaaSessionEntry = _CfprApAaaSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1)
)
cfprApAaaSessionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaSessionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaSessionEntry.setStatus("current")
_CfprApAaaSessionInstanceId_Type = CfprApManagedObjectId
_CfprApAaaSessionInstanceId_Object = MibTableColumn
cfprApAaaSessionInstanceId = _CfprApAaaSessionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 1),
    _CfprApAaaSessionInstanceId_Type()
)
cfprApAaaSessionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaSessionInstanceId.setStatus("current")
_CfprApAaaSessionDn_Type = CfprApManagedObjectDn
_CfprApAaaSessionDn_Object = MibTableColumn
cfprApAaaSessionDn = _CfprApAaaSessionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 2),
    _CfprApAaaSessionDn_Type()
)
cfprApAaaSessionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionDn.setStatus("current")
_CfprApAaaSessionRn_Type = SnmpAdminString
_CfprApAaaSessionRn_Object = MibTableColumn
cfprApAaaSessionRn = _CfprApAaaSessionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 3),
    _CfprApAaaSessionRn_Type()
)
cfprApAaaSessionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionRn.setStatus("current")
_CfprApAaaSessionHost_Type = SnmpAdminString
_CfprApAaaSessionHost_Object = MibTableColumn
cfprApAaaSessionHost = _CfprApAaaSessionHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 4),
    _CfprApAaaSessionHost_Type()
)
cfprApAaaSessionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionHost.setStatus("current")
_CfprApAaaSessionId_Type = SnmpAdminString
_CfprApAaaSessionId_Object = MibTableColumn
cfprApAaaSessionId = _CfprApAaaSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 5),
    _CfprApAaaSessionId_Type()
)
cfprApAaaSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionId.setStatus("current")
_CfprApAaaSessionIntDel_Type = TruthValue
_CfprApAaaSessionIntDel_Object = MibTableColumn
cfprApAaaSessionIntDel = _CfprApAaaSessionIntDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 6),
    _CfprApAaaSessionIntDel_Type()
)
cfprApAaaSessionIntDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionIntDel.setStatus("current")
_CfprApAaaSessionLoginTime_Type = DateAndTime
_CfprApAaaSessionLoginTime_Object = MibTableColumn
cfprApAaaSessionLoginTime = _CfprApAaaSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 7),
    _CfprApAaaSessionLoginTime_Type()
)
cfprApAaaSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLoginTime.setStatus("current")
_CfprApAaaSessionPid_Type = Gauge32
_CfprApAaaSessionPid_Object = MibTableColumn
cfprApAaaSessionPid = _CfprApAaaSessionPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 8),
    _CfprApAaaSessionPid_Type()
)
cfprApAaaSessionPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionPid.setStatus("current")
_CfprApAaaSessionRefreshPeriod_Type = Gauge32
_CfprApAaaSessionRefreshPeriod_Object = MibTableColumn
cfprApAaaSessionRefreshPeriod = _CfprApAaaSessionRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 9),
    _CfprApAaaSessionRefreshPeriod_Type()
)
cfprApAaaSessionRefreshPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionRefreshPeriod.setStatus("current")
_CfprApAaaSessionSessionTimeout_Type = Gauge32
_CfprApAaaSessionSessionTimeout_Object = MibTableColumn
cfprApAaaSessionSessionTimeout = _CfprApAaaSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 10),
    _CfprApAaaSessionSessionTimeout_Type()
)
cfprApAaaSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionSessionTimeout.setStatus("current")
_CfprApAaaSessionSwitchId_Type = CfprApNetworkSwitchId
_CfprApAaaSessionSwitchId_Object = MibTableColumn
cfprApAaaSessionSwitchId = _CfprApAaaSessionSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 11),
    _CfprApAaaSessionSwitchId_Type()
)
cfprApAaaSessionSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionSwitchId.setStatus("current")
_CfprApAaaSessionTerm_Type = SnmpAdminString
_CfprApAaaSessionTerm_Object = MibTableColumn
cfprApAaaSessionTerm = _CfprApAaaSessionTerm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 12),
    _CfprApAaaSessionTerm_Type()
)
cfprApAaaSessionTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionTerm.setStatus("current")
_CfprApAaaSessionUi_Type = CfprApAaaUserInterface
_CfprApAaaSessionUi_Object = MibTableColumn
cfprApAaaSessionUi = _CfprApAaaSessionUi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 13),
    _CfprApAaaSessionUi_Type()
)
cfprApAaaSessionUi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionUi.setStatus("current")
_CfprApAaaSessionUser_Type = SnmpAdminString
_CfprApAaaSessionUser_Object = MibTableColumn
cfprApAaaSessionUser = _CfprApAaaSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 39, 1, 14),
    _CfprApAaaSessionUser_Type()
)
cfprApAaaSessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionUser.setStatus("current")
_CfprApAaaSessionInfoTable_Object = MibTable
cfprApAaaSessionInfoTable = _CfprApAaaSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40)
)
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoTable.setStatus("current")
_CfprApAaaSessionInfoEntry_Object = MibTableRow
cfprApAaaSessionInfoEntry = _CfprApAaaSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1)
)
cfprApAaaSessionInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaSessionInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoEntry.setStatus("current")
_CfprApAaaSessionInfoInstanceId_Type = CfprApManagedObjectId
_CfprApAaaSessionInfoInstanceId_Object = MibTableColumn
cfprApAaaSessionInfoInstanceId = _CfprApAaaSessionInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 1),
    _CfprApAaaSessionInfoInstanceId_Type()
)
cfprApAaaSessionInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoInstanceId.setStatus("current")
_CfprApAaaSessionInfoDn_Type = CfprApManagedObjectDn
_CfprApAaaSessionInfoDn_Object = MibTableColumn
cfprApAaaSessionInfoDn = _CfprApAaaSessionInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 2),
    _CfprApAaaSessionInfoDn_Type()
)
cfprApAaaSessionInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoDn.setStatus("current")
_CfprApAaaSessionInfoRn_Type = SnmpAdminString
_CfprApAaaSessionInfoRn_Object = MibTableColumn
cfprApAaaSessionInfoRn = _CfprApAaaSessionInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 3),
    _CfprApAaaSessionInfoRn_Type()
)
cfprApAaaSessionInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoRn.setStatus("current")
_CfprApAaaSessionInfoAddress_Type = SnmpAdminString
_CfprApAaaSessionInfoAddress_Object = MibTableColumn
cfprApAaaSessionInfoAddress = _CfprApAaaSessionInfoAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 4),
    _CfprApAaaSessionInfoAddress_Type()
)
cfprApAaaSessionInfoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoAddress.setStatus("current")
_CfprApAaaSessionInfoDestIp_Type = SnmpAdminString
_CfprApAaaSessionInfoDestIp_Object = MibTableColumn
cfprApAaaSessionInfoDestIp = _CfprApAaaSessionInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 5),
    _CfprApAaaSessionInfoDestIp_Type()
)
cfprApAaaSessionInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoDestIp.setStatus("current")
_CfprApAaaSessionInfoEtime_Type = DateAndTime
_CfprApAaaSessionInfoEtime_Object = MibTableColumn
cfprApAaaSessionInfoEtime = _CfprApAaaSessionInfoEtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 6),
    _CfprApAaaSessionInfoEtime_Type()
)
cfprApAaaSessionInfoEtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoEtime.setStatus("current")
_CfprApAaaSessionInfoId_Type = SnmpAdminString
_CfprApAaaSessionInfoId_Object = MibTableColumn
cfprApAaaSessionInfoId = _CfprApAaaSessionInfoId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 7),
    _CfprApAaaSessionInfoId_Type()
)
cfprApAaaSessionInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoId.setStatus("current")
_CfprApAaaSessionInfoPriv_Type = SnmpAdminString
_CfprApAaaSessionInfoPriv_Object = MibTableColumn
cfprApAaaSessionInfoPriv = _CfprApAaaSessionInfoPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 8),
    _CfprApAaaSessionInfoPriv_Type()
)
cfprApAaaSessionInfoPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoPriv.setStatus("current")
_CfprApAaaSessionInfoType_Type = CfprApAaaCimcSessionType
_CfprApAaaSessionInfoType_Object = MibTableColumn
cfprApAaaSessionInfoType = _CfprApAaaSessionInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 9),
    _CfprApAaaSessionInfoType_Type()
)
cfprApAaaSessionInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoType.setStatus("current")
_CfprApAaaSessionInfoUser_Type = SnmpAdminString
_CfprApAaaSessionInfoUser_Object = MibTableColumn
cfprApAaaSessionInfoUser = _CfprApAaaSessionInfoUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 10),
    _CfprApAaaSessionInfoUser_Type()
)
cfprApAaaSessionInfoUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoUser.setStatus("current")
_CfprApAaaSessionInfoUserType_Type = CfprApAaaSession
_CfprApAaaSessionInfoUserType_Object = MibTableColumn
cfprApAaaSessionInfoUserType = _CfprApAaaSessionInfoUserType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 40, 1, 11),
    _CfprApAaaSessionInfoUserType_Type()
)
cfprApAaaSessionInfoUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoUserType.setStatus("current")
_CfprApAaaSessionInfoTableTable_Object = MibTable
cfprApAaaSessionInfoTableTable = _CfprApAaaSessionInfoTableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 41)
)
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoTableTable.setStatus("current")
_CfprApAaaSessionInfoTableEntry_Object = MibTableRow
cfprApAaaSessionInfoTableEntry = _CfprApAaaSessionInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 41, 1)
)
cfprApAaaSessionInfoTableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaSessionInfoTableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoTableEntry.setStatus("current")
_CfprApAaaSessionInfoTableInstanceId_Type = CfprApManagedObjectId
_CfprApAaaSessionInfoTableInstanceId_Object = MibTableColumn
cfprApAaaSessionInfoTableInstanceId = _CfprApAaaSessionInfoTableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 41, 1, 1),
    _CfprApAaaSessionInfoTableInstanceId_Type()
)
cfprApAaaSessionInfoTableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoTableInstanceId.setStatus("current")
_CfprApAaaSessionInfoTableDn_Type = CfprApManagedObjectDn
_CfprApAaaSessionInfoTableDn_Object = MibTableColumn
cfprApAaaSessionInfoTableDn = _CfprApAaaSessionInfoTableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 41, 1, 2),
    _CfprApAaaSessionInfoTableDn_Type()
)
cfprApAaaSessionInfoTableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoTableDn.setStatus("current")
_CfprApAaaSessionInfoTableRn_Type = SnmpAdminString
_CfprApAaaSessionInfoTableRn_Object = MibTableColumn
cfprApAaaSessionInfoTableRn = _CfprApAaaSessionInfoTableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 41, 1, 3),
    _CfprApAaaSessionInfoTableRn_Type()
)
cfprApAaaSessionInfoTableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionInfoTableRn.setStatus("current")
_CfprApAaaSessionLRTable_Object = MibTable
cfprApAaaSessionLRTable = _CfprApAaaSessionLRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42)
)
if mibBuilder.loadTexts:
    cfprApAaaSessionLRTable.setStatus("current")
_CfprApAaaSessionLREntry_Object = MibTableRow
cfprApAaaSessionLREntry = _CfprApAaaSessionLREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1)
)
cfprApAaaSessionLREntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaSessionLRInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaSessionLREntry.setStatus("current")
_CfprApAaaSessionLRInstanceId_Type = CfprApManagedObjectId
_CfprApAaaSessionLRInstanceId_Object = MibTableColumn
cfprApAaaSessionLRInstanceId = _CfprApAaaSessionLRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 1),
    _CfprApAaaSessionLRInstanceId_Type()
)
cfprApAaaSessionLRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRInstanceId.setStatus("current")
_CfprApAaaSessionLRDn_Type = CfprApManagedObjectDn
_CfprApAaaSessionLRDn_Object = MibTableColumn
cfprApAaaSessionLRDn = _CfprApAaaSessionLRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 2),
    _CfprApAaaSessionLRDn_Type()
)
cfprApAaaSessionLRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRDn.setStatus("current")
_CfprApAaaSessionLRRn_Type = SnmpAdminString
_CfprApAaaSessionLRRn_Object = MibTableColumn
cfprApAaaSessionLRRn = _CfprApAaaSessionLRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 3),
    _CfprApAaaSessionLRRn_Type()
)
cfprApAaaSessionLRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRRn.setStatus("current")
_CfprApAaaSessionLRAffected_Type = SnmpAdminString
_CfprApAaaSessionLRAffected_Object = MibTableColumn
cfprApAaaSessionLRAffected = _CfprApAaaSessionLRAffected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 4),
    _CfprApAaaSessionLRAffected_Type()
)
cfprApAaaSessionLRAffected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRAffected.setStatus("current")
_CfprApAaaSessionLRCause_Type = CfprApConditionCause
_CfprApAaaSessionLRCause_Object = MibTableColumn
cfprApAaaSessionLRCause = _CfprApAaaSessionLRCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 5),
    _CfprApAaaSessionLRCause_Type()
)
cfprApAaaSessionLRCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRCause.setStatus("current")
_CfprApAaaSessionLRChangeSet_Type = SnmpAdminString
_CfprApAaaSessionLRChangeSet_Object = MibTableColumn
cfprApAaaSessionLRChangeSet = _CfprApAaaSessionLRChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 6),
    _CfprApAaaSessionLRChangeSet_Type()
)
cfprApAaaSessionLRChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRChangeSet.setStatus("current")
_CfprApAaaSessionLRCode_Type = CfprApConditionCode
_CfprApAaaSessionLRCode_Object = MibTableColumn
cfprApAaaSessionLRCode = _CfprApAaaSessionLRCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 7),
    _CfprApAaaSessionLRCode_Type()
)
cfprApAaaSessionLRCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRCode.setStatus("current")
_CfprApAaaSessionLRCreated_Type = DateAndTime
_CfprApAaaSessionLRCreated_Object = MibTableColumn
cfprApAaaSessionLRCreated = _CfprApAaaSessionLRCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 8),
    _CfprApAaaSessionLRCreated_Type()
)
cfprApAaaSessionLRCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRCreated.setStatus("current")
_CfprApAaaSessionLRDescr_Type = SnmpAdminString
_CfprApAaaSessionLRDescr_Object = MibTableColumn
cfprApAaaSessionLRDescr = _CfprApAaaSessionLRDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 9),
    _CfprApAaaSessionLRDescr_Type()
)
cfprApAaaSessionLRDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRDescr.setStatus("current")
_CfprApAaaSessionLRId_Type = Gauge32
_CfprApAaaSessionLRId_Object = MibTableColumn
cfprApAaaSessionLRId = _CfprApAaaSessionLRId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 10),
    _CfprApAaaSessionLRId_Type()
)
cfprApAaaSessionLRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRId.setStatus("current")
_CfprApAaaSessionLRInd_Type = CfprApConditionActionIndicator
_CfprApAaaSessionLRInd_Object = MibTableColumn
cfprApAaaSessionLRInd = _CfprApAaaSessionLRInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 11),
    _CfprApAaaSessionLRInd_Type()
)
cfprApAaaSessionLRInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRInd.setStatus("current")
_CfprApAaaSessionLRSessionId_Type = SnmpAdminString
_CfprApAaaSessionLRSessionId_Object = MibTableColumn
cfprApAaaSessionLRSessionId = _CfprApAaaSessionLRSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 12),
    _CfprApAaaSessionLRSessionId_Type()
)
cfprApAaaSessionLRSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRSessionId.setStatus("current")
_CfprApAaaSessionLRSeverity_Type = CfprApConditionSeverity
_CfprApAaaSessionLRSeverity_Object = MibTableColumn
cfprApAaaSessionLRSeverity = _CfprApAaaSessionLRSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 13),
    _CfprApAaaSessionLRSeverity_Type()
)
cfprApAaaSessionLRSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRSeverity.setStatus("current")
_CfprApAaaSessionLRTrig_Type = Gauge32
_CfprApAaaSessionLRTrig_Object = MibTableColumn
cfprApAaaSessionLRTrig = _CfprApAaaSessionLRTrig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 14),
    _CfprApAaaSessionLRTrig_Type()
)
cfprApAaaSessionLRTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRTrig.setStatus("current")
_CfprApAaaSessionLRTxId_Type = Unsigned64
_CfprApAaaSessionLRTxId_Object = MibTableColumn
cfprApAaaSessionLRTxId = _CfprApAaaSessionLRTxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 15),
    _CfprApAaaSessionLRTxId_Type()
)
cfprApAaaSessionLRTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRTxId.setStatus("current")
_CfprApAaaSessionLRUser_Type = SnmpAdminString
_CfprApAaaSessionLRUser_Object = MibTableColumn
cfprApAaaSessionLRUser = _CfprApAaaSessionLRUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 42, 1, 16),
    _CfprApAaaSessionLRUser_Type()
)
cfprApAaaSessionLRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSessionLRUser.setStatus("current")
_CfprApAaaShellLoginTable_Object = MibTable
cfprApAaaShellLoginTable = _CfprApAaaShellLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43)
)
if mibBuilder.loadTexts:
    cfprApAaaShellLoginTable.setStatus("current")
_CfprApAaaShellLoginEntry_Object = MibTableRow
cfprApAaaShellLoginEntry = _CfprApAaaShellLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1)
)
cfprApAaaShellLoginEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaShellLoginInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaShellLoginEntry.setStatus("current")
_CfprApAaaShellLoginInstanceId_Type = CfprApManagedObjectId
_CfprApAaaShellLoginInstanceId_Object = MibTableColumn
cfprApAaaShellLoginInstanceId = _CfprApAaaShellLoginInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 1),
    _CfprApAaaShellLoginInstanceId_Type()
)
cfprApAaaShellLoginInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginInstanceId.setStatus("current")
_CfprApAaaShellLoginDn_Type = CfprApManagedObjectDn
_CfprApAaaShellLoginDn_Object = MibTableColumn
cfprApAaaShellLoginDn = _CfprApAaaShellLoginDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 2),
    _CfprApAaaShellLoginDn_Type()
)
cfprApAaaShellLoginDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginDn.setStatus("current")
_CfprApAaaShellLoginRn_Type = SnmpAdminString
_CfprApAaaShellLoginRn_Object = MibTableColumn
cfprApAaaShellLoginRn = _CfprApAaaShellLoginRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 3),
    _CfprApAaaShellLoginRn_Type()
)
cfprApAaaShellLoginRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginRn.setStatus("current")
_CfprApAaaShellLoginDescr_Type = SnmpAdminString
_CfprApAaaShellLoginDescr_Object = MibTableColumn
cfprApAaaShellLoginDescr = _CfprApAaaShellLoginDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 4),
    _CfprApAaaShellLoginDescr_Type()
)
cfprApAaaShellLoginDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginDescr.setStatus("current")
_CfprApAaaShellLoginId_Type = SnmpAdminString
_CfprApAaaShellLoginId_Object = MibTableColumn
cfprApAaaShellLoginId = _CfprApAaaShellLoginId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 5),
    _CfprApAaaShellLoginId_Type()
)
cfprApAaaShellLoginId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginId.setStatus("current")
_CfprApAaaShellLoginIntId_Type = SnmpAdminString
_CfprApAaaShellLoginIntId_Object = MibTableColumn
cfprApAaaShellLoginIntId = _CfprApAaaShellLoginIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 6),
    _CfprApAaaShellLoginIntId_Type()
)
cfprApAaaShellLoginIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginIntId.setStatus("current")
_CfprApAaaShellLoginLocalHost_Type = SnmpAdminString
_CfprApAaaShellLoginLocalHost_Object = MibTableColumn
cfprApAaaShellLoginLocalHost = _CfprApAaaShellLoginLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 7),
    _CfprApAaaShellLoginLocalHost_Type()
)
cfprApAaaShellLoginLocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginLocalHost.setStatus("current")
_CfprApAaaShellLoginName_Type = SnmpAdminString
_CfprApAaaShellLoginName_Object = MibTableColumn
cfprApAaaShellLoginName = _CfprApAaaShellLoginName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 8),
    _CfprApAaaShellLoginName_Type()
)
cfprApAaaShellLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginName.setStatus("current")
_CfprApAaaShellLoginPolicyLevel_Type = Gauge32
_CfprApAaaShellLoginPolicyLevel_Object = MibTableColumn
cfprApAaaShellLoginPolicyLevel = _CfprApAaaShellLoginPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 9),
    _CfprApAaaShellLoginPolicyLevel_Type()
)
cfprApAaaShellLoginPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginPolicyLevel.setStatus("current")
_CfprApAaaShellLoginPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaShellLoginPolicyOwner_Object = MibTableColumn
cfprApAaaShellLoginPolicyOwner = _CfprApAaaShellLoginPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 10),
    _CfprApAaaShellLoginPolicyOwner_Type()
)
cfprApAaaShellLoginPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginPolicyOwner.setStatus("current")
_CfprApAaaShellLoginRemoteHost_Type = SnmpAdminString
_CfprApAaaShellLoginRemoteHost_Object = MibTableColumn
cfprApAaaShellLoginRemoteHost = _CfprApAaaShellLoginRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 11),
    _CfprApAaaShellLoginRemoteHost_Type()
)
cfprApAaaShellLoginRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginRemoteHost.setStatus("current")
_CfprApAaaShellLoginSession_Type = CfprApAaaSession
_CfprApAaaShellLoginSession_Object = MibTableColumn
cfprApAaaShellLoginSession = _CfprApAaaShellLoginSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 12),
    _CfprApAaaShellLoginSession_Type()
)
cfprApAaaShellLoginSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginSession.setStatus("current")
_CfprApAaaShellLoginSwitchId_Type = CfprApNetworkSwitchId
_CfprApAaaShellLoginSwitchId_Object = MibTableColumn
cfprApAaaShellLoginSwitchId = _CfprApAaaShellLoginSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 43, 1, 13),
    _CfprApAaaShellLoginSwitchId_Type()
)
cfprApAaaShellLoginSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaShellLoginSwitchId.setStatus("current")
_CfprApAaaSshAuthTable_Object = MibTable
cfprApAaaSshAuthTable = _CfprApAaaSshAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 44)
)
if mibBuilder.loadTexts:
    cfprApAaaSshAuthTable.setStatus("current")
_CfprApAaaSshAuthEntry_Object = MibTableRow
cfprApAaaSshAuthEntry = _CfprApAaaSshAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 44, 1)
)
cfprApAaaSshAuthEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaSshAuthInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaSshAuthEntry.setStatus("current")
_CfprApAaaSshAuthInstanceId_Type = CfprApManagedObjectId
_CfprApAaaSshAuthInstanceId_Object = MibTableColumn
cfprApAaaSshAuthInstanceId = _CfprApAaaSshAuthInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 44, 1, 1),
    _CfprApAaaSshAuthInstanceId_Type()
)
cfprApAaaSshAuthInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaSshAuthInstanceId.setStatus("current")
_CfprApAaaSshAuthDn_Type = CfprApManagedObjectDn
_CfprApAaaSshAuthDn_Object = MibTableColumn
cfprApAaaSshAuthDn = _CfprApAaaSshAuthDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 44, 1, 2),
    _CfprApAaaSshAuthDn_Type()
)
cfprApAaaSshAuthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSshAuthDn.setStatus("current")
_CfprApAaaSshAuthRn_Type = SnmpAdminString
_CfprApAaaSshAuthRn_Object = MibTableColumn
cfprApAaaSshAuthRn = _CfprApAaaSshAuthRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 44, 1, 3),
    _CfprApAaaSshAuthRn_Type()
)
cfprApAaaSshAuthRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSshAuthRn.setStatus("current")
_CfprApAaaSshAuthData_Type = SnmpAdminString
_CfprApAaaSshAuthData_Object = MibTableColumn
cfprApAaaSshAuthData = _CfprApAaaSshAuthData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 44, 1, 4),
    _CfprApAaaSshAuthData_Type()
)
cfprApAaaSshAuthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSshAuthData.setStatus("current")
_CfprApAaaSshAuthOldStrType_Type = CfprApAaaSshStr
_CfprApAaaSshAuthOldStrType_Object = MibTableColumn
cfprApAaaSshAuthOldStrType = _CfprApAaaSshAuthOldStrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 44, 1, 5),
    _CfprApAaaSshAuthOldStrType_Type()
)
cfprApAaaSshAuthOldStrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSshAuthOldStrType.setStatus("current")
_CfprApAaaSshAuthStrType_Type = CfprApAaaSshStr
_CfprApAaaSshAuthStrType_Object = MibTableColumn
cfprApAaaSshAuthStrType = _CfprApAaaSshAuthStrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 44, 1, 6),
    _CfprApAaaSshAuthStrType_Type()
)
cfprApAaaSshAuthStrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaSshAuthStrType.setStatus("current")
_CfprApAaaTacacsPlusEpTable_Object = MibTable
cfprApAaaTacacsPlusEpTable = _CfprApAaaTacacsPlusEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45)
)
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpTable.setStatus("current")
_CfprApAaaTacacsPlusEpEntry_Object = MibTableRow
cfprApAaaTacacsPlusEpEntry = _CfprApAaaTacacsPlusEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1)
)
cfprApAaaTacacsPlusEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaTacacsPlusEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpEntry.setStatus("current")
_CfprApAaaTacacsPlusEpInstanceId_Type = CfprApManagedObjectId
_CfprApAaaTacacsPlusEpInstanceId_Object = MibTableColumn
cfprApAaaTacacsPlusEpInstanceId = _CfprApAaaTacacsPlusEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 1),
    _CfprApAaaTacacsPlusEpInstanceId_Type()
)
cfprApAaaTacacsPlusEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpInstanceId.setStatus("current")
_CfprApAaaTacacsPlusEpDn_Type = CfprApManagedObjectDn
_CfprApAaaTacacsPlusEpDn_Object = MibTableColumn
cfprApAaaTacacsPlusEpDn = _CfprApAaaTacacsPlusEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 2),
    _CfprApAaaTacacsPlusEpDn_Type()
)
cfprApAaaTacacsPlusEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpDn.setStatus("current")
_CfprApAaaTacacsPlusEpRn_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpRn_Object = MibTableColumn
cfprApAaaTacacsPlusEpRn = _CfprApAaaTacacsPlusEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 3),
    _CfprApAaaTacacsPlusEpRn_Type()
)
cfprApAaaTacacsPlusEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpRn.setStatus("current")
_CfprApAaaTacacsPlusEpDescr_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpDescr_Object = MibTableColumn
cfprApAaaTacacsPlusEpDescr = _CfprApAaaTacacsPlusEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 4),
    _CfprApAaaTacacsPlusEpDescr_Type()
)
cfprApAaaTacacsPlusEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpDescr.setStatus("current")
_CfprApAaaTacacsPlusEpFsmDescr_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmDescr_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmDescr = _CfprApAaaTacacsPlusEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 5),
    _CfprApAaaTacacsPlusEpFsmDescr_Type()
)
cfprApAaaTacacsPlusEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmDescr.setStatus("current")
_CfprApAaaTacacsPlusEpFsmPrev_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmPrev_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmPrev = _CfprApAaaTacacsPlusEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 6),
    _CfprApAaaTacacsPlusEpFsmPrev_Type()
)
cfprApAaaTacacsPlusEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmPrev.setStatus("current")
_CfprApAaaTacacsPlusEpFsmProgr_Type = Gauge32
_CfprApAaaTacacsPlusEpFsmProgr_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmProgr = _CfprApAaaTacacsPlusEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 7),
    _CfprApAaaTacacsPlusEpFsmProgr_Type()
)
cfprApAaaTacacsPlusEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmProgr.setStatus("current")
_CfprApAaaTacacsPlusEpFsmRmtInvErrCode_Type = Gauge32
_CfprApAaaTacacsPlusEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmRmtInvErrCode = _CfprApAaaTacacsPlusEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 8),
    _CfprApAaaTacacsPlusEpFsmRmtInvErrCode_Type()
)
cfprApAaaTacacsPlusEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmRmtInvErrCode.setStatus("current")
_CfprApAaaTacacsPlusEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmRmtInvErrDescr = _CfprApAaaTacacsPlusEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 9),
    _CfprApAaaTacacsPlusEpFsmRmtInvErrDescr_Type()
)
cfprApAaaTacacsPlusEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmRmtInvErrDescr.setStatus("current")
_CfprApAaaTacacsPlusEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaTacacsPlusEpFsmRmtInvRslt_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmRmtInvRslt = _CfprApAaaTacacsPlusEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 10),
    _CfprApAaaTacacsPlusEpFsmRmtInvRslt_Type()
)
cfprApAaaTacacsPlusEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmRmtInvRslt.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageDescr_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmStageDescr_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageDescr = _CfprApAaaTacacsPlusEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 11),
    _CfprApAaaTacacsPlusEpFsmStageDescr_Type()
)
cfprApAaaTacacsPlusEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageDescr.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStamp_Type = DateAndTime
_CfprApAaaTacacsPlusEpFsmStamp_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStamp = _CfprApAaaTacacsPlusEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 12),
    _CfprApAaaTacacsPlusEpFsmStamp_Type()
)
cfprApAaaTacacsPlusEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStamp.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStatus_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmStatus_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStatus = _CfprApAaaTacacsPlusEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 13),
    _CfprApAaaTacacsPlusEpFsmStatus_Type()
)
cfprApAaaTacacsPlusEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStatus.setStatus("current")
_CfprApAaaTacacsPlusEpFsmTry_Type = Gauge32
_CfprApAaaTacacsPlusEpFsmTry_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmTry = _CfprApAaaTacacsPlusEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 14),
    _CfprApAaaTacacsPlusEpFsmTry_Type()
)
cfprApAaaTacacsPlusEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmTry.setStatus("current")
_CfprApAaaTacacsPlusEpIntId_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpIntId_Object = MibTableColumn
cfprApAaaTacacsPlusEpIntId = _CfprApAaaTacacsPlusEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 15),
    _CfprApAaaTacacsPlusEpIntId_Type()
)
cfprApAaaTacacsPlusEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpIntId.setStatus("current")
_CfprApAaaTacacsPlusEpName_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpName_Object = MibTableColumn
cfprApAaaTacacsPlusEpName = _CfprApAaaTacacsPlusEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 16),
    _CfprApAaaTacacsPlusEpName_Type()
)
cfprApAaaTacacsPlusEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpName.setStatus("current")
_CfprApAaaTacacsPlusEpPolicyLevel_Type = Gauge32
_CfprApAaaTacacsPlusEpPolicyLevel_Object = MibTableColumn
cfprApAaaTacacsPlusEpPolicyLevel = _CfprApAaaTacacsPlusEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 17),
    _CfprApAaaTacacsPlusEpPolicyLevel_Type()
)
cfprApAaaTacacsPlusEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpPolicyLevel.setStatus("current")
_CfprApAaaTacacsPlusEpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaTacacsPlusEpPolicyOwner_Object = MibTableColumn
cfprApAaaTacacsPlusEpPolicyOwner = _CfprApAaaTacacsPlusEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 18),
    _CfprApAaaTacacsPlusEpPolicyOwner_Type()
)
cfprApAaaTacacsPlusEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpPolicyOwner.setStatus("current")
_CfprApAaaTacacsPlusEpRetries_Type = Gauge32
_CfprApAaaTacacsPlusEpRetries_Object = MibTableColumn
cfprApAaaTacacsPlusEpRetries = _CfprApAaaTacacsPlusEpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 19),
    _CfprApAaaTacacsPlusEpRetries_Type()
)
cfprApAaaTacacsPlusEpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpRetries.setStatus("current")
_CfprApAaaTacacsPlusEpTimeout_Type = Gauge32
_CfprApAaaTacacsPlusEpTimeout_Object = MibTableColumn
cfprApAaaTacacsPlusEpTimeout = _CfprApAaaTacacsPlusEpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 45, 1, 20),
    _CfprApAaaTacacsPlusEpTimeout_Type()
)
cfprApAaaTacacsPlusEpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpTimeout.setStatus("current")
_CfprApAaaTacacsPlusEpFsmTable_Object = MibTable
cfprApAaaTacacsPlusEpFsmTable = _CfprApAaaTacacsPlusEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46)
)
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmTable.setStatus("current")
_CfprApAaaTacacsPlusEpFsmEntry_Object = MibTableRow
cfprApAaaTacacsPlusEpFsmEntry = _CfprApAaaTacacsPlusEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1)
)
cfprApAaaTacacsPlusEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaTacacsPlusEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmEntry.setStatus("current")
_CfprApAaaTacacsPlusEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApAaaTacacsPlusEpFsmInstanceId_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmInstanceId = _CfprApAaaTacacsPlusEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 1),
    _CfprApAaaTacacsPlusEpFsmInstanceId_Type()
)
cfprApAaaTacacsPlusEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmInstanceId.setStatus("current")
_CfprApAaaTacacsPlusEpFsmDn_Type = CfprApManagedObjectDn
_CfprApAaaTacacsPlusEpFsmDn_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmDn = _CfprApAaaTacacsPlusEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 2),
    _CfprApAaaTacacsPlusEpFsmDn_Type()
)
cfprApAaaTacacsPlusEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmDn.setStatus("current")
_CfprApAaaTacacsPlusEpFsmRn_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmRn_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmRn = _CfprApAaaTacacsPlusEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 3),
    _CfprApAaaTacacsPlusEpFsmRn_Type()
)
cfprApAaaTacacsPlusEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmRn.setStatus("current")
_CfprApAaaTacacsPlusEpFsmCompletionTime_Type = DateAndTime
_CfprApAaaTacacsPlusEpFsmCompletionTime_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmCompletionTime = _CfprApAaaTacacsPlusEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 4),
    _CfprApAaaTacacsPlusEpFsmCompletionTime_Type()
)
cfprApAaaTacacsPlusEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmCompletionTime.setStatus("current")
_CfprApAaaTacacsPlusEpFsmCurrentFsm_Type = CfprApAaaTacacsPlusEpFsmCurrentFsm
_CfprApAaaTacacsPlusEpFsmCurrentFsm_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmCurrentFsm = _CfprApAaaTacacsPlusEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 5),
    _CfprApAaaTacacsPlusEpFsmCurrentFsm_Type()
)
cfprApAaaTacacsPlusEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmCurrentFsm.setStatus("current")
_CfprApAaaTacacsPlusEpFsmDescrData_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmDescrData_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmDescrData = _CfprApAaaTacacsPlusEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 6),
    _CfprApAaaTacacsPlusEpFsmDescrData_Type()
)
cfprApAaaTacacsPlusEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmDescrData.setStatus("current")
_CfprApAaaTacacsPlusEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaTacacsPlusEpFsmFsmStatus_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmFsmStatus = _CfprApAaaTacacsPlusEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 7),
    _CfprApAaaTacacsPlusEpFsmFsmStatus_Type()
)
cfprApAaaTacacsPlusEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmFsmStatus.setStatus("current")
_CfprApAaaTacacsPlusEpFsmProgress_Type = Gauge32
_CfprApAaaTacacsPlusEpFsmProgress_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmProgress = _CfprApAaaTacacsPlusEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 8),
    _CfprApAaaTacacsPlusEpFsmProgress_Type()
)
cfprApAaaTacacsPlusEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmProgress.setStatus("current")
_CfprApAaaTacacsPlusEpFsmRmtErrCode_Type = Gauge32
_CfprApAaaTacacsPlusEpFsmRmtErrCode_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmRmtErrCode = _CfprApAaaTacacsPlusEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 9),
    _CfprApAaaTacacsPlusEpFsmRmtErrCode_Type()
)
cfprApAaaTacacsPlusEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmRmtErrCode.setStatus("current")
_CfprApAaaTacacsPlusEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmRmtErrDescr_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmRmtErrDescr = _CfprApAaaTacacsPlusEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 10),
    _CfprApAaaTacacsPlusEpFsmRmtErrDescr_Type()
)
cfprApAaaTacacsPlusEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmRmtErrDescr.setStatus("current")
_CfprApAaaTacacsPlusEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaTacacsPlusEpFsmRmtRslt_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmRmtRslt = _CfprApAaaTacacsPlusEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 46, 1, 11),
    _CfprApAaaTacacsPlusEpFsmRmtRslt_Type()
)
cfprApAaaTacacsPlusEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmRmtRslt.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageTable_Object = MibTable
cfprApAaaTacacsPlusEpFsmStageTable = _CfprApAaaTacacsPlusEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47)
)
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageTable.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageEntry_Object = MibTableRow
cfprApAaaTacacsPlusEpFsmStageEntry = _CfprApAaaTacacsPlusEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1)
)
cfprApAaaTacacsPlusEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaTacacsPlusEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageEntry.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApAaaTacacsPlusEpFsmStageInstanceId_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageInstanceId = _CfprApAaaTacacsPlusEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 1),
    _CfprApAaaTacacsPlusEpFsmStageInstanceId_Type()
)
cfprApAaaTacacsPlusEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageInstanceId.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApAaaTacacsPlusEpFsmStageDn_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageDn = _CfprApAaaTacacsPlusEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 2),
    _CfprApAaaTacacsPlusEpFsmStageDn_Type()
)
cfprApAaaTacacsPlusEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageDn.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageRn_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmStageRn_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageRn = _CfprApAaaTacacsPlusEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 3),
    _CfprApAaaTacacsPlusEpFsmStageRn_Type()
)
cfprApAaaTacacsPlusEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageRn.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageDescrData_Type = SnmpAdminString
_CfprApAaaTacacsPlusEpFsmStageDescrData_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageDescrData = _CfprApAaaTacacsPlusEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 4),
    _CfprApAaaTacacsPlusEpFsmStageDescrData_Type()
)
cfprApAaaTacacsPlusEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageDescrData.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApAaaTacacsPlusEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageLastUpdateTime = _CfprApAaaTacacsPlusEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 5),
    _CfprApAaaTacacsPlusEpFsmStageLastUpdateTime_Type()
)
cfprApAaaTacacsPlusEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageLastUpdateTime.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageName_Type = CfprApAaaTacacsPlusEpFsmStageName
_CfprApAaaTacacsPlusEpFsmStageName_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageName = _CfprApAaaTacacsPlusEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 6),
    _CfprApAaaTacacsPlusEpFsmStageName_Type()
)
cfprApAaaTacacsPlusEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageName.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageOrder_Type = Gauge32
_CfprApAaaTacacsPlusEpFsmStageOrder_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageOrder = _CfprApAaaTacacsPlusEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 7),
    _CfprApAaaTacacsPlusEpFsmStageOrder_Type()
)
cfprApAaaTacacsPlusEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageOrder.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageRetry_Type = Gauge32
_CfprApAaaTacacsPlusEpFsmStageRetry_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageRetry = _CfprApAaaTacacsPlusEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 8),
    _CfprApAaaTacacsPlusEpFsmStageRetry_Type()
)
cfprApAaaTacacsPlusEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageRetry.setStatus("current")
_CfprApAaaTacacsPlusEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaTacacsPlusEpFsmStageStageStatus_Object = MibTableColumn
cfprApAaaTacacsPlusEpFsmStageStageStatus = _CfprApAaaTacacsPlusEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 47, 1, 9),
    _CfprApAaaTacacsPlusEpFsmStageStageStatus_Type()
)
cfprApAaaTacacsPlusEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusEpFsmStageStageStatus.setStatus("current")
_CfprApAaaTacacsPlusProviderTable_Object = MibTable
cfprApAaaTacacsPlusProviderTable = _CfprApAaaTacacsPlusProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48)
)
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderTable.setStatus("current")
_CfprApAaaTacacsPlusProviderEntry_Object = MibTableRow
cfprApAaaTacacsPlusProviderEntry = _CfprApAaaTacacsPlusProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1)
)
cfprApAaaTacacsPlusProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaTacacsPlusProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderEntry.setStatus("current")
_CfprApAaaTacacsPlusProviderInstanceId_Type = CfprApManagedObjectId
_CfprApAaaTacacsPlusProviderInstanceId_Object = MibTableColumn
cfprApAaaTacacsPlusProviderInstanceId = _CfprApAaaTacacsPlusProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 1),
    _CfprApAaaTacacsPlusProviderInstanceId_Type()
)
cfprApAaaTacacsPlusProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderInstanceId.setStatus("current")
_CfprApAaaTacacsPlusProviderDn_Type = CfprApManagedObjectDn
_CfprApAaaTacacsPlusProviderDn_Object = MibTableColumn
cfprApAaaTacacsPlusProviderDn = _CfprApAaaTacacsPlusProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 2),
    _CfprApAaaTacacsPlusProviderDn_Type()
)
cfprApAaaTacacsPlusProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderDn.setStatus("current")
_CfprApAaaTacacsPlusProviderRn_Type = SnmpAdminString
_CfprApAaaTacacsPlusProviderRn_Object = MibTableColumn
cfprApAaaTacacsPlusProviderRn = _CfprApAaaTacacsPlusProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 3),
    _CfprApAaaTacacsPlusProviderRn_Type()
)
cfprApAaaTacacsPlusProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderRn.setStatus("current")
_CfprApAaaTacacsPlusProviderDescr_Type = SnmpAdminString
_CfprApAaaTacacsPlusProviderDescr_Object = MibTableColumn
cfprApAaaTacacsPlusProviderDescr = _CfprApAaaTacacsPlusProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 4),
    _CfprApAaaTacacsPlusProviderDescr_Type()
)
cfprApAaaTacacsPlusProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderDescr.setStatus("current")
_CfprApAaaTacacsPlusProviderEncKey_Type = SnmpAdminString
_CfprApAaaTacacsPlusProviderEncKey_Object = MibTableColumn
cfprApAaaTacacsPlusProviderEncKey = _CfprApAaaTacacsPlusProviderEncKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 5),
    _CfprApAaaTacacsPlusProviderEncKey_Type()
)
cfprApAaaTacacsPlusProviderEncKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderEncKey.setStatus("current")
_CfprApAaaTacacsPlusProviderKey_Type = SnmpAdminString
_CfprApAaaTacacsPlusProviderKey_Object = MibTableColumn
cfprApAaaTacacsPlusProviderKey = _CfprApAaaTacacsPlusProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 6),
    _CfprApAaaTacacsPlusProviderKey_Type()
)
cfprApAaaTacacsPlusProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderKey.setStatus("current")
_CfprApAaaTacacsPlusProviderKeySet_Type = TruthValue
_CfprApAaaTacacsPlusProviderKeySet_Object = MibTableColumn
cfprApAaaTacacsPlusProviderKeySet = _CfprApAaaTacacsPlusProviderKeySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 7),
    _CfprApAaaTacacsPlusProviderKeySet_Type()
)
cfprApAaaTacacsPlusProviderKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderKeySet.setStatus("current")
_CfprApAaaTacacsPlusProviderName_Type = SnmpAdminString
_CfprApAaaTacacsPlusProviderName_Object = MibTableColumn
cfprApAaaTacacsPlusProviderName = _CfprApAaaTacacsPlusProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 8),
    _CfprApAaaTacacsPlusProviderName_Type()
)
cfprApAaaTacacsPlusProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderName.setStatus("current")
_CfprApAaaTacacsPlusProviderOrder_Type = Gauge32
_CfprApAaaTacacsPlusProviderOrder_Object = MibTableColumn
cfprApAaaTacacsPlusProviderOrder = _CfprApAaaTacacsPlusProviderOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 9),
    _CfprApAaaTacacsPlusProviderOrder_Type()
)
cfprApAaaTacacsPlusProviderOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderOrder.setStatus("current")
_CfprApAaaTacacsPlusProviderPort_Type = Gauge32
_CfprApAaaTacacsPlusProviderPort_Object = MibTableColumn
cfprApAaaTacacsPlusProviderPort = _CfprApAaaTacacsPlusProviderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 10),
    _CfprApAaaTacacsPlusProviderPort_Type()
)
cfprApAaaTacacsPlusProviderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderPort.setStatus("current")
_CfprApAaaTacacsPlusProviderRetries_Type = Gauge32
_CfprApAaaTacacsPlusProviderRetries_Object = MibTableColumn
cfprApAaaTacacsPlusProviderRetries = _CfprApAaaTacacsPlusProviderRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 11),
    _CfprApAaaTacacsPlusProviderRetries_Type()
)
cfprApAaaTacacsPlusProviderRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderRetries.setStatus("current")
_CfprApAaaTacacsPlusProviderTimeout_Type = Gauge32
_CfprApAaaTacacsPlusProviderTimeout_Object = MibTableColumn
cfprApAaaTacacsPlusProviderTimeout = _CfprApAaaTacacsPlusProviderTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 48, 1, 12),
    _CfprApAaaTacacsPlusProviderTimeout_Type()
)
cfprApAaaTacacsPlusProviderTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaTacacsPlusProviderTimeout.setStatus("current")
_CfprApAaaUserTable_Object = MibTable
cfprApAaaUserTable = _CfprApAaaUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49)
)
if mibBuilder.loadTexts:
    cfprApAaaUserTable.setStatus("current")
_CfprApAaaUserEntry_Object = MibTableRow
cfprApAaaUserEntry = _CfprApAaaUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1)
)
cfprApAaaUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaUserEntry.setStatus("current")
_CfprApAaaUserInstanceId_Type = CfprApManagedObjectId
_CfprApAaaUserInstanceId_Object = MibTableColumn
cfprApAaaUserInstanceId = _CfprApAaaUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 1),
    _CfprApAaaUserInstanceId_Type()
)
cfprApAaaUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaUserInstanceId.setStatus("current")
_CfprApAaaUserDn_Type = CfprApManagedObjectDn
_CfprApAaaUserDn_Object = MibTableColumn
cfprApAaaUserDn = _CfprApAaaUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 2),
    _CfprApAaaUserDn_Type()
)
cfprApAaaUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDn.setStatus("current")
_CfprApAaaUserRn_Type = SnmpAdminString
_CfprApAaaUserRn_Object = MibTableColumn
cfprApAaaUserRn = _CfprApAaaUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 3),
    _CfprApAaaUserRn_Type()
)
cfprApAaaUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserRn.setStatus("current")
_CfprApAaaUserAccountStatus_Type = CfprApAaaAccountStatus
_CfprApAaaUserAccountStatus_Object = MibTableColumn
cfprApAaaUserAccountStatus = _CfprApAaaUserAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 4),
    _CfprApAaaUserAccountStatus_Type()
)
cfprApAaaUserAccountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserAccountStatus.setStatus("current")
_CfprApAaaUserClearPwdHistory_Type = CfprApAaaClear
_CfprApAaaUserClearPwdHistory_Object = MibTableColumn
cfprApAaaUserClearPwdHistory = _CfprApAaaUserClearPwdHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 5),
    _CfprApAaaUserClearPwdHistory_Type()
)
cfprApAaaUserClearPwdHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserClearPwdHistory.setStatus("current")
_CfprApAaaUserConfigState_Type = CfprApAaaConfigState
_CfprApAaaUserConfigState_Object = MibTableColumn
cfprApAaaUserConfigState = _CfprApAaaUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 6),
    _CfprApAaaUserConfigState_Type()
)
cfprApAaaUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserConfigState.setStatus("current")
_CfprApAaaUserConfigStatusMessage_Type = SnmpAdminString
_CfprApAaaUserConfigStatusMessage_Object = MibTableColumn
cfprApAaaUserConfigStatusMessage = _CfprApAaaUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 7),
    _CfprApAaaUserConfigStatusMessage_Type()
)
cfprApAaaUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserConfigStatusMessage.setStatus("current")
_CfprApAaaUserDescr_Type = SnmpAdminString
_CfprApAaaUserDescr_Object = MibTableColumn
cfprApAaaUserDescr = _CfprApAaaUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 8),
    _CfprApAaaUserDescr_Type()
)
cfprApAaaUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDescr.setStatus("current")
_CfprApAaaUserEmail_Type = SnmpAdminString
_CfprApAaaUserEmail_Object = MibTableColumn
cfprApAaaUserEmail = _CfprApAaaUserEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 9),
    _CfprApAaaUserEmail_Type()
)
cfprApAaaUserEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEmail.setStatus("current")
_CfprApAaaUserEncPwd_Type = SnmpAdminString
_CfprApAaaUserEncPwd_Object = MibTableColumn
cfprApAaaUserEncPwd = _CfprApAaaUserEncPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 10),
    _CfprApAaaUserEncPwd_Type()
)
cfprApAaaUserEncPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEncPwd.setStatus("current")
_CfprApAaaUserEncPwdSet_Type = TruthValue
_CfprApAaaUserEncPwdSet_Object = MibTableColumn
cfprApAaaUserEncPwdSet = _CfprApAaaUserEncPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 11),
    _CfprApAaaUserEncPwdSet_Type()
)
cfprApAaaUserEncPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEncPwdSet.setStatus("current")
_CfprApAaaUserExpiration_Type = DateAndTime
_CfprApAaaUserExpiration_Object = MibTableColumn
cfprApAaaUserExpiration = _CfprApAaaUserExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 12),
    _CfprApAaaUserExpiration_Type()
)
cfprApAaaUserExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserExpiration.setStatus("current")
_CfprApAaaUserExpires_Type = TruthValue
_CfprApAaaUserExpires_Object = MibTableColumn
cfprApAaaUserExpires = _CfprApAaaUserExpires_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 13),
    _CfprApAaaUserExpires_Type()
)
cfprApAaaUserExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserExpires.setStatus("current")
_CfprApAaaUserFirstName_Type = SnmpAdminString
_CfprApAaaUserFirstName_Object = MibTableColumn
cfprApAaaUserFirstName = _CfprApAaaUserFirstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 14),
    _CfprApAaaUserFirstName_Type()
)
cfprApAaaUserFirstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserFirstName.setStatus("current")
_CfprApAaaUserLastName_Type = SnmpAdminString
_CfprApAaaUserLastName_Object = MibTableColumn
cfprApAaaUserLastName = _CfprApAaaUserLastName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 15),
    _CfprApAaaUserLastName_Type()
)
cfprApAaaUserLastName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserLastName.setStatus("current")
_CfprApAaaUserName_Type = SnmpAdminString
_CfprApAaaUserName_Object = MibTableColumn
cfprApAaaUserName = _CfprApAaaUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 16),
    _CfprApAaaUserName_Type()
)
cfprApAaaUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserName.setStatus("current")
_CfprApAaaUserPhone_Type = SnmpAdminString
_CfprApAaaUserPhone_Object = MibTableColumn
cfprApAaaUserPhone = _CfprApAaaUserPhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 17),
    _CfprApAaaUserPhone_Type()
)
cfprApAaaUserPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserPhone.setStatus("current")
_CfprApAaaUserPriv_Type = CfprApAaaAccess
_CfprApAaaUserPriv_Object = MibTableColumn
cfprApAaaUserPriv = _CfprApAaaUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 18),
    _CfprApAaaUserPriv_Type()
)
cfprApAaaUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserPriv.setStatus("current")
_CfprApAaaUserPwd_Type = SnmpAdminString
_CfprApAaaUserPwd_Object = MibTableColumn
cfprApAaaUserPwd = _CfprApAaaUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 19),
    _CfprApAaaUserPwd_Type()
)
cfprApAaaUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserPwd.setStatus("current")
_CfprApAaaUserPwdSet_Type = TruthValue
_CfprApAaaUserPwdSet_Object = MibTableColumn
cfprApAaaUserPwdSet = _CfprApAaaUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 49, 1, 21),
    _CfprApAaaUserPwdSet_Type()
)
cfprApAaaUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserPwdSet.setStatus("current")
_CfprApAaaUserDataTable_Object = MibTable
cfprApAaaUserDataTable = _CfprApAaaUserDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50)
)
if mibBuilder.loadTexts:
    cfprApAaaUserDataTable.setStatus("current")
_CfprApAaaUserDataEntry_Object = MibTableRow
cfprApAaaUserDataEntry = _CfprApAaaUserDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1)
)
cfprApAaaUserDataEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaUserDataInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaUserDataEntry.setStatus("current")
_CfprApAaaUserDataInstanceId_Type = CfprApManagedObjectId
_CfprApAaaUserDataInstanceId_Object = MibTableColumn
cfprApAaaUserDataInstanceId = _CfprApAaaUserDataInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 1),
    _CfprApAaaUserDataInstanceId_Type()
)
cfprApAaaUserDataInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaUserDataInstanceId.setStatus("current")
_CfprApAaaUserDataDn_Type = CfprApManagedObjectDn
_CfprApAaaUserDataDn_Object = MibTableColumn
cfprApAaaUserDataDn = _CfprApAaaUserDataDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 2),
    _CfprApAaaUserDataDn_Type()
)
cfprApAaaUserDataDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataDn.setStatus("current")
_CfprApAaaUserDataRn_Type = SnmpAdminString
_CfprApAaaUserDataRn_Object = MibTableColumn
cfprApAaaUserDataRn = _CfprApAaaUserDataRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 3),
    _CfprApAaaUserDataRn_Type()
)
cfprApAaaUserDataRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataRn.setStatus("current")
_CfprApAaaUserDataDescr_Type = SnmpAdminString
_CfprApAaaUserDataDescr_Object = MibTableColumn
cfprApAaaUserDataDescr = _CfprApAaaUserDataDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 4),
    _CfprApAaaUserDataDescr_Type()
)
cfprApAaaUserDataDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataDescr.setStatus("current")
_CfprApAaaUserDataIntId_Type = SnmpAdminString
_CfprApAaaUserDataIntId_Object = MibTableColumn
cfprApAaaUserDataIntId = _CfprApAaaUserDataIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 5),
    _CfprApAaaUserDataIntId_Type()
)
cfprApAaaUserDataIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataIntId.setStatus("current")
_CfprApAaaUserDataName_Type = SnmpAdminString
_CfprApAaaUserDataName_Object = MibTableColumn
cfprApAaaUserDataName = _CfprApAaaUserDataName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 6),
    _CfprApAaaUserDataName_Type()
)
cfprApAaaUserDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataName.setStatus("current")
_CfprApAaaUserDataPolicyLevel_Type = Gauge32
_CfprApAaaUserDataPolicyLevel_Object = MibTableColumn
cfprApAaaUserDataPolicyLevel = _CfprApAaaUserDataPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 7),
    _CfprApAaaUserDataPolicyLevel_Type()
)
cfprApAaaUserDataPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataPolicyLevel.setStatus("current")
_CfprApAaaUserDataPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaUserDataPolicyOwner_Object = MibTableColumn
cfprApAaaUserDataPolicyOwner = _CfprApAaaUserDataPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 8),
    _CfprApAaaUserDataPolicyOwner_Type()
)
cfprApAaaUserDataPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataPolicyOwner.setStatus("current")
_CfprApAaaUserDataPwdChangeCount_Type = Gauge32
_CfprApAaaUserDataPwdChangeCount_Object = MibTableColumn
cfprApAaaUserDataPwdChangeCount = _CfprApAaaUserDataPwdChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 9),
    _CfprApAaaUserDataPwdChangeCount_Type()
)
cfprApAaaUserDataPwdChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataPwdChangeCount.setStatus("current")
_CfprApAaaUserDataPwdChangeIntervalBegin_Type = DateAndTime
_CfprApAaaUserDataPwdChangeIntervalBegin_Object = MibTableColumn
cfprApAaaUserDataPwdChangeIntervalBegin = _CfprApAaaUserDataPwdChangeIntervalBegin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 10),
    _CfprApAaaUserDataPwdChangeIntervalBegin_Type()
)
cfprApAaaUserDataPwdChangeIntervalBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataPwdChangeIntervalBegin.setStatus("current")
_CfprApAaaUserDataPwdChangedDate_Type = DateAndTime
_CfprApAaaUserDataPwdChangedDate_Object = MibTableColumn
cfprApAaaUserDataPwdChangedDate = _CfprApAaaUserDataPwdChangedDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 11),
    _CfprApAaaUserDataPwdChangedDate_Type()
)
cfprApAaaUserDataPwdChangedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataPwdChangedDate.setStatus("current")
_CfprApAaaUserDataPwdHistory_Type = SnmpAdminString
_CfprApAaaUserDataPwdHistory_Object = MibTableColumn
cfprApAaaUserDataPwdHistory = _CfprApAaaUserDataPwdHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 50, 1, 12),
    _CfprApAaaUserDataPwdHistory_Type()
)
cfprApAaaUserDataPwdHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserDataPwdHistory.setStatus("current")
_CfprApAaaUserEpTable_Object = MibTable
cfprApAaaUserEpTable = _CfprApAaaUserEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51)
)
if mibBuilder.loadTexts:
    cfprApAaaUserEpTable.setStatus("current")
_CfprApAaaUserEpEntry_Object = MibTableRow
cfprApAaaUserEpEntry = _CfprApAaaUserEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1)
)
cfprApAaaUserEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaUserEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaUserEpEntry.setStatus("current")
_CfprApAaaUserEpInstanceId_Type = CfprApManagedObjectId
_CfprApAaaUserEpInstanceId_Object = MibTableColumn
cfprApAaaUserEpInstanceId = _CfprApAaaUserEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 1),
    _CfprApAaaUserEpInstanceId_Type()
)
cfprApAaaUserEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaUserEpInstanceId.setStatus("current")
_CfprApAaaUserEpDn_Type = CfprApManagedObjectDn
_CfprApAaaUserEpDn_Object = MibTableColumn
cfprApAaaUserEpDn = _CfprApAaaUserEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 2),
    _CfprApAaaUserEpDn_Type()
)
cfprApAaaUserEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpDn.setStatus("current")
_CfprApAaaUserEpRn_Type = SnmpAdminString
_CfprApAaaUserEpRn_Object = MibTableColumn
cfprApAaaUserEpRn = _CfprApAaaUserEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 3),
    _CfprApAaaUserEpRn_Type()
)
cfprApAaaUserEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpRn.setStatus("current")
_CfprApAaaUserEpDescr_Type = SnmpAdminString
_CfprApAaaUserEpDescr_Object = MibTableColumn
cfprApAaaUserEpDescr = _CfprApAaaUserEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 4),
    _CfprApAaaUserEpDescr_Type()
)
cfprApAaaUserEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpDescr.setStatus("current")
_CfprApAaaUserEpFsmDescr_Type = SnmpAdminString
_CfprApAaaUserEpFsmDescr_Object = MibTableColumn
cfprApAaaUserEpFsmDescr = _CfprApAaaUserEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 5),
    _CfprApAaaUserEpFsmDescr_Type()
)
cfprApAaaUserEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmDescr.setStatus("current")
_CfprApAaaUserEpFsmPrev_Type = SnmpAdminString
_CfprApAaaUserEpFsmPrev_Object = MibTableColumn
cfprApAaaUserEpFsmPrev = _CfprApAaaUserEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 6),
    _CfprApAaaUserEpFsmPrev_Type()
)
cfprApAaaUserEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmPrev.setStatus("current")
_CfprApAaaUserEpFsmProgr_Type = Gauge32
_CfprApAaaUserEpFsmProgr_Object = MibTableColumn
cfprApAaaUserEpFsmProgr = _CfprApAaaUserEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 7),
    _CfprApAaaUserEpFsmProgr_Type()
)
cfprApAaaUserEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmProgr.setStatus("current")
_CfprApAaaUserEpFsmRmtInvErrCode_Type = Gauge32
_CfprApAaaUserEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApAaaUserEpFsmRmtInvErrCode = _CfprApAaaUserEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 8),
    _CfprApAaaUserEpFsmRmtInvErrCode_Type()
)
cfprApAaaUserEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmRmtInvErrCode.setStatus("current")
_CfprApAaaUserEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApAaaUserEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApAaaUserEpFsmRmtInvErrDescr = _CfprApAaaUserEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 9),
    _CfprApAaaUserEpFsmRmtInvErrDescr_Type()
)
cfprApAaaUserEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmRmtInvErrDescr.setStatus("current")
_CfprApAaaUserEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaUserEpFsmRmtInvRslt_Object = MibTableColumn
cfprApAaaUserEpFsmRmtInvRslt = _CfprApAaaUserEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 10),
    _CfprApAaaUserEpFsmRmtInvRslt_Type()
)
cfprApAaaUserEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmRmtInvRslt.setStatus("current")
_CfprApAaaUserEpFsmStageDescr_Type = SnmpAdminString
_CfprApAaaUserEpFsmStageDescr_Object = MibTableColumn
cfprApAaaUserEpFsmStageDescr = _CfprApAaaUserEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 11),
    _CfprApAaaUserEpFsmStageDescr_Type()
)
cfprApAaaUserEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageDescr.setStatus("current")
_CfprApAaaUserEpFsmStamp_Type = DateAndTime
_CfprApAaaUserEpFsmStamp_Object = MibTableColumn
cfprApAaaUserEpFsmStamp = _CfprApAaaUserEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 12),
    _CfprApAaaUserEpFsmStamp_Type()
)
cfprApAaaUserEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStamp.setStatus("current")
_CfprApAaaUserEpFsmStatus_Type = SnmpAdminString
_CfprApAaaUserEpFsmStatus_Object = MibTableColumn
cfprApAaaUserEpFsmStatus = _CfprApAaaUserEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 13),
    _CfprApAaaUserEpFsmStatus_Type()
)
cfprApAaaUserEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStatus.setStatus("current")
_CfprApAaaUserEpFsmTry_Type = Gauge32
_CfprApAaaUserEpFsmTry_Object = MibTableColumn
cfprApAaaUserEpFsmTry = _CfprApAaaUserEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 14),
    _CfprApAaaUserEpFsmTry_Type()
)
cfprApAaaUserEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTry.setStatus("current")
_CfprApAaaUserEpIntId_Type = SnmpAdminString
_CfprApAaaUserEpIntId_Object = MibTableColumn
cfprApAaaUserEpIntId = _CfprApAaaUserEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 15),
    _CfprApAaaUserEpIntId_Type()
)
cfprApAaaUserEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpIntId.setStatus("current")
_CfprApAaaUserEpMaxLoginAttempts_Type = Gauge32
_CfprApAaaUserEpMaxLoginAttempts_Object = MibTableColumn
cfprApAaaUserEpMaxLoginAttempts = _CfprApAaaUserEpMaxLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 16),
    _CfprApAaaUserEpMaxLoginAttempts_Type()
)
cfprApAaaUserEpMaxLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpMaxLoginAttempts.setStatus("current")
_CfprApAaaUserEpMinPwdLength_Type = Gauge32
_CfprApAaaUserEpMinPwdLength_Object = MibTableColumn
cfprApAaaUserEpMinPwdLength = _CfprApAaaUserEpMinPwdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 17),
    _CfprApAaaUserEpMinPwdLength_Type()
)
cfprApAaaUserEpMinPwdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpMinPwdLength.setStatus("current")
_CfprApAaaUserEpName_Type = SnmpAdminString
_CfprApAaaUserEpName_Object = MibTableColumn
cfprApAaaUserEpName = _CfprApAaaUserEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 18),
    _CfprApAaaUserEpName_Type()
)
cfprApAaaUserEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpName.setStatus("current")
_CfprApAaaUserEpPolicyLevel_Type = Gauge32
_CfprApAaaUserEpPolicyLevel_Object = MibTableColumn
cfprApAaaUserEpPolicyLevel = _CfprApAaaUserEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 19),
    _CfprApAaaUserEpPolicyLevel_Type()
)
cfprApAaaUserEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpPolicyLevel.setStatus("current")
_CfprApAaaUserEpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaUserEpPolicyOwner_Object = MibTableColumn
cfprApAaaUserEpPolicyOwner = _CfprApAaaUserEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 20),
    _CfprApAaaUserEpPolicyOwner_Type()
)
cfprApAaaUserEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpPolicyOwner.setStatus("current")
_CfprApAaaUserEpPwdStrengthCheck_Type = TruthValue
_CfprApAaaUserEpPwdStrengthCheck_Object = MibTableColumn
cfprApAaaUserEpPwdStrengthCheck = _CfprApAaaUserEpPwdStrengthCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 21),
    _CfprApAaaUserEpPwdStrengthCheck_Type()
)
cfprApAaaUserEpPwdStrengthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpPwdStrengthCheck.setStatus("current")
_CfprApAaaUserEpUserAccountUnlockTime_Type = Gauge32
_CfprApAaaUserEpUserAccountUnlockTime_Object = MibTableColumn
cfprApAaaUserEpUserAccountUnlockTime = _CfprApAaaUserEpUserAccountUnlockTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 51, 1, 22),
    _CfprApAaaUserEpUserAccountUnlockTime_Type()
)
cfprApAaaUserEpUserAccountUnlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpUserAccountUnlockTime.setStatus("current")
_CfprApAaaUserEpFsmTable_Object = MibTable
cfprApAaaUserEpFsmTable = _CfprApAaaUserEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52)
)
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTable.setStatus("current")
_CfprApAaaUserEpFsmEntry_Object = MibTableRow
cfprApAaaUserEpFsmEntry = _CfprApAaaUserEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1)
)
cfprApAaaUserEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaUserEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmEntry.setStatus("current")
_CfprApAaaUserEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApAaaUserEpFsmInstanceId_Object = MibTableColumn
cfprApAaaUserEpFsmInstanceId = _CfprApAaaUserEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 1),
    _CfprApAaaUserEpFsmInstanceId_Type()
)
cfprApAaaUserEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmInstanceId.setStatus("current")
_CfprApAaaUserEpFsmDn_Type = CfprApManagedObjectDn
_CfprApAaaUserEpFsmDn_Object = MibTableColumn
cfprApAaaUserEpFsmDn = _CfprApAaaUserEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 2),
    _CfprApAaaUserEpFsmDn_Type()
)
cfprApAaaUserEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmDn.setStatus("current")
_CfprApAaaUserEpFsmRn_Type = SnmpAdminString
_CfprApAaaUserEpFsmRn_Object = MibTableColumn
cfprApAaaUserEpFsmRn = _CfprApAaaUserEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 3),
    _CfprApAaaUserEpFsmRn_Type()
)
cfprApAaaUserEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmRn.setStatus("current")
_CfprApAaaUserEpFsmCompletionTime_Type = DateAndTime
_CfprApAaaUserEpFsmCompletionTime_Object = MibTableColumn
cfprApAaaUserEpFsmCompletionTime = _CfprApAaaUserEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 4),
    _CfprApAaaUserEpFsmCompletionTime_Type()
)
cfprApAaaUserEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmCompletionTime.setStatus("current")
_CfprApAaaUserEpFsmCurrentFsm_Type = CfprApAaaUserEpFsmCurrentFsm
_CfprApAaaUserEpFsmCurrentFsm_Object = MibTableColumn
cfprApAaaUserEpFsmCurrentFsm = _CfprApAaaUserEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 5),
    _CfprApAaaUserEpFsmCurrentFsm_Type()
)
cfprApAaaUserEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmCurrentFsm.setStatus("current")
_CfprApAaaUserEpFsmDescrData_Type = SnmpAdminString
_CfprApAaaUserEpFsmDescrData_Object = MibTableColumn
cfprApAaaUserEpFsmDescrData = _CfprApAaaUserEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 6),
    _CfprApAaaUserEpFsmDescrData_Type()
)
cfprApAaaUserEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmDescrData.setStatus("current")
_CfprApAaaUserEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaUserEpFsmFsmStatus_Object = MibTableColumn
cfprApAaaUserEpFsmFsmStatus = _CfprApAaaUserEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 7),
    _CfprApAaaUserEpFsmFsmStatus_Type()
)
cfprApAaaUserEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmFsmStatus.setStatus("current")
_CfprApAaaUserEpFsmProgress_Type = Gauge32
_CfprApAaaUserEpFsmProgress_Object = MibTableColumn
cfprApAaaUserEpFsmProgress = _CfprApAaaUserEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 8),
    _CfprApAaaUserEpFsmProgress_Type()
)
cfprApAaaUserEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmProgress.setStatus("current")
_CfprApAaaUserEpFsmRmtErrCode_Type = Gauge32
_CfprApAaaUserEpFsmRmtErrCode_Object = MibTableColumn
cfprApAaaUserEpFsmRmtErrCode = _CfprApAaaUserEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 9),
    _CfprApAaaUserEpFsmRmtErrCode_Type()
)
cfprApAaaUserEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmRmtErrCode.setStatus("current")
_CfprApAaaUserEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApAaaUserEpFsmRmtErrDescr_Object = MibTableColumn
cfprApAaaUserEpFsmRmtErrDescr = _CfprApAaaUserEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 10),
    _CfprApAaaUserEpFsmRmtErrDescr_Type()
)
cfprApAaaUserEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmRmtErrDescr.setStatus("current")
_CfprApAaaUserEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApAaaUserEpFsmRmtRslt_Object = MibTableColumn
cfprApAaaUserEpFsmRmtRslt = _CfprApAaaUserEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 52, 1, 11),
    _CfprApAaaUserEpFsmRmtRslt_Type()
)
cfprApAaaUserEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmRmtRslt.setStatus("current")
_CfprApAaaUserEpFsmStageTable_Object = MibTable
cfprApAaaUserEpFsmStageTable = _CfprApAaaUserEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53)
)
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageTable.setStatus("current")
_CfprApAaaUserEpFsmStageEntry_Object = MibTableRow
cfprApAaaUserEpFsmStageEntry = _CfprApAaaUserEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1)
)
cfprApAaaUserEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaUserEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageEntry.setStatus("current")
_CfprApAaaUserEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApAaaUserEpFsmStageInstanceId_Object = MibTableColumn
cfprApAaaUserEpFsmStageInstanceId = _CfprApAaaUserEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 1),
    _CfprApAaaUserEpFsmStageInstanceId_Type()
)
cfprApAaaUserEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageInstanceId.setStatus("current")
_CfprApAaaUserEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApAaaUserEpFsmStageDn_Object = MibTableColumn
cfprApAaaUserEpFsmStageDn = _CfprApAaaUserEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 2),
    _CfprApAaaUserEpFsmStageDn_Type()
)
cfprApAaaUserEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageDn.setStatus("current")
_CfprApAaaUserEpFsmStageRn_Type = SnmpAdminString
_CfprApAaaUserEpFsmStageRn_Object = MibTableColumn
cfprApAaaUserEpFsmStageRn = _CfprApAaaUserEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 3),
    _CfprApAaaUserEpFsmStageRn_Type()
)
cfprApAaaUserEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageRn.setStatus("current")
_CfprApAaaUserEpFsmStageDescrData_Type = SnmpAdminString
_CfprApAaaUserEpFsmStageDescrData_Object = MibTableColumn
cfprApAaaUserEpFsmStageDescrData = _CfprApAaaUserEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 4),
    _CfprApAaaUserEpFsmStageDescrData_Type()
)
cfprApAaaUserEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageDescrData.setStatus("current")
_CfprApAaaUserEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApAaaUserEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApAaaUserEpFsmStageLastUpdateTime = _CfprApAaaUserEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 5),
    _CfprApAaaUserEpFsmStageLastUpdateTime_Type()
)
cfprApAaaUserEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageLastUpdateTime.setStatus("current")
_CfprApAaaUserEpFsmStageName_Type = CfprApAaaUserEpFsmStageName
_CfprApAaaUserEpFsmStageName_Object = MibTableColumn
cfprApAaaUserEpFsmStageName = _CfprApAaaUserEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 6),
    _CfprApAaaUserEpFsmStageName_Type()
)
cfprApAaaUserEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageName.setStatus("current")
_CfprApAaaUserEpFsmStageOrder_Type = Gauge32
_CfprApAaaUserEpFsmStageOrder_Object = MibTableColumn
cfprApAaaUserEpFsmStageOrder = _CfprApAaaUserEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 7),
    _CfprApAaaUserEpFsmStageOrder_Type()
)
cfprApAaaUserEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageOrder.setStatus("current")
_CfprApAaaUserEpFsmStageRetry_Type = Gauge32
_CfprApAaaUserEpFsmStageRetry_Object = MibTableColumn
cfprApAaaUserEpFsmStageRetry = _CfprApAaaUserEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 8),
    _CfprApAaaUserEpFsmStageRetry_Type()
)
cfprApAaaUserEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageRetry.setStatus("current")
_CfprApAaaUserEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApAaaUserEpFsmStageStageStatus_Object = MibTableColumn
cfprApAaaUserEpFsmStageStageStatus = _CfprApAaaUserEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 53, 1, 9),
    _CfprApAaaUserEpFsmStageStageStatus_Type()
)
cfprApAaaUserEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmStageStageStatus.setStatus("current")
_CfprApAaaUserEpFsmTaskTable_Object = MibTable
cfprApAaaUserEpFsmTaskTable = _CfprApAaaUserEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54)
)
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskTable.setStatus("current")
_CfprApAaaUserEpFsmTaskEntry_Object = MibTableRow
cfprApAaaUserEpFsmTaskEntry = _CfprApAaaUserEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54, 1)
)
cfprApAaaUserEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaUserEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskEntry.setStatus("current")
_CfprApAaaUserEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApAaaUserEpFsmTaskInstanceId_Object = MibTableColumn
cfprApAaaUserEpFsmTaskInstanceId = _CfprApAaaUserEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54, 1, 1),
    _CfprApAaaUserEpFsmTaskInstanceId_Type()
)
cfprApAaaUserEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskInstanceId.setStatus("current")
_CfprApAaaUserEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApAaaUserEpFsmTaskDn_Object = MibTableColumn
cfprApAaaUserEpFsmTaskDn = _CfprApAaaUserEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54, 1, 2),
    _CfprApAaaUserEpFsmTaskDn_Type()
)
cfprApAaaUserEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskDn.setStatus("current")
_CfprApAaaUserEpFsmTaskRn_Type = SnmpAdminString
_CfprApAaaUserEpFsmTaskRn_Object = MibTableColumn
cfprApAaaUserEpFsmTaskRn = _CfprApAaaUserEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54, 1, 3),
    _CfprApAaaUserEpFsmTaskRn_Type()
)
cfprApAaaUserEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskRn.setStatus("current")
_CfprApAaaUserEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApAaaUserEpFsmTaskCompletion_Object = MibTableColumn
cfprApAaaUserEpFsmTaskCompletion = _CfprApAaaUserEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54, 1, 4),
    _CfprApAaaUserEpFsmTaskCompletion_Type()
)
cfprApAaaUserEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskCompletion.setStatus("current")
_CfprApAaaUserEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApAaaUserEpFsmTaskFlags_Object = MibTableColumn
cfprApAaaUserEpFsmTaskFlags = _CfprApAaaUserEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54, 1, 5),
    _CfprApAaaUserEpFsmTaskFlags_Type()
)
cfprApAaaUserEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskFlags.setStatus("current")
_CfprApAaaUserEpFsmTaskItem_Type = CfprApAaaUserEpFsmTaskItem
_CfprApAaaUserEpFsmTaskItem_Object = MibTableColumn
cfprApAaaUserEpFsmTaskItem = _CfprApAaaUserEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54, 1, 6),
    _CfprApAaaUserEpFsmTaskItem_Type()
)
cfprApAaaUserEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskItem.setStatus("current")
_CfprApAaaUserEpFsmTaskSeqId_Type = Gauge32
_CfprApAaaUserEpFsmTaskSeqId_Object = MibTableColumn
cfprApAaaUserEpFsmTaskSeqId = _CfprApAaaUserEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 54, 1, 7),
    _CfprApAaaUserEpFsmTaskSeqId_Type()
)
cfprApAaaUserEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserEpFsmTaskSeqId.setStatus("current")
_CfprApAaaUserLocaleTable_Object = MibTable
cfprApAaaUserLocaleTable = _CfprApAaaUserLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55)
)
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleTable.setStatus("current")
_CfprApAaaUserLocaleEntry_Object = MibTableRow
cfprApAaaUserLocaleEntry = _CfprApAaaUserLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55, 1)
)
cfprApAaaUserLocaleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaUserLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleEntry.setStatus("current")
_CfprApAaaUserLocaleInstanceId_Type = CfprApManagedObjectId
_CfprApAaaUserLocaleInstanceId_Object = MibTableColumn
cfprApAaaUserLocaleInstanceId = _CfprApAaaUserLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55, 1, 1),
    _CfprApAaaUserLocaleInstanceId_Type()
)
cfprApAaaUserLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleInstanceId.setStatus("current")
_CfprApAaaUserLocaleDn_Type = CfprApManagedObjectDn
_CfprApAaaUserLocaleDn_Object = MibTableColumn
cfprApAaaUserLocaleDn = _CfprApAaaUserLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55, 1, 2),
    _CfprApAaaUserLocaleDn_Type()
)
cfprApAaaUserLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleDn.setStatus("current")
_CfprApAaaUserLocaleRn_Type = SnmpAdminString
_CfprApAaaUserLocaleRn_Object = MibTableColumn
cfprApAaaUserLocaleRn = _CfprApAaaUserLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55, 1, 3),
    _CfprApAaaUserLocaleRn_Type()
)
cfprApAaaUserLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleRn.setStatus("current")
_CfprApAaaUserLocaleConfigState_Type = CfprApAaaConfigState
_CfprApAaaUserLocaleConfigState_Object = MibTableColumn
cfprApAaaUserLocaleConfigState = _CfprApAaaUserLocaleConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55, 1, 4),
    _CfprApAaaUserLocaleConfigState_Type()
)
cfprApAaaUserLocaleConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleConfigState.setStatus("current")
_CfprApAaaUserLocaleConfigStatusMessage_Type = SnmpAdminString
_CfprApAaaUserLocaleConfigStatusMessage_Object = MibTableColumn
cfprApAaaUserLocaleConfigStatusMessage = _CfprApAaaUserLocaleConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55, 1, 5),
    _CfprApAaaUserLocaleConfigStatusMessage_Type()
)
cfprApAaaUserLocaleConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleConfigStatusMessage.setStatus("current")
_CfprApAaaUserLocaleDescr_Type = SnmpAdminString
_CfprApAaaUserLocaleDescr_Object = MibTableColumn
cfprApAaaUserLocaleDescr = _CfprApAaaUserLocaleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55, 1, 6),
    _CfprApAaaUserLocaleDescr_Type()
)
cfprApAaaUserLocaleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleDescr.setStatus("current")
_CfprApAaaUserLocaleName_Type = SnmpAdminString
_CfprApAaaUserLocaleName_Object = MibTableColumn
cfprApAaaUserLocaleName = _CfprApAaaUserLocaleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 55, 1, 7),
    _CfprApAaaUserLocaleName_Type()
)
cfprApAaaUserLocaleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserLocaleName.setStatus("current")
_CfprApAaaUserRoleTable_Object = MibTable
cfprApAaaUserRoleTable = _CfprApAaaUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56)
)
if mibBuilder.loadTexts:
    cfprApAaaUserRoleTable.setStatus("current")
_CfprApAaaUserRoleEntry_Object = MibTableRow
cfprApAaaUserRoleEntry = _CfprApAaaUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56, 1)
)
cfprApAaaUserRoleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaUserRoleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaUserRoleEntry.setStatus("current")
_CfprApAaaUserRoleInstanceId_Type = CfprApManagedObjectId
_CfprApAaaUserRoleInstanceId_Object = MibTableColumn
cfprApAaaUserRoleInstanceId = _CfprApAaaUserRoleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56, 1, 1),
    _CfprApAaaUserRoleInstanceId_Type()
)
cfprApAaaUserRoleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaUserRoleInstanceId.setStatus("current")
_CfprApAaaUserRoleDn_Type = CfprApManagedObjectDn
_CfprApAaaUserRoleDn_Object = MibTableColumn
cfprApAaaUserRoleDn = _CfprApAaaUserRoleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56, 1, 2),
    _CfprApAaaUserRoleDn_Type()
)
cfprApAaaUserRoleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserRoleDn.setStatus("current")
_CfprApAaaUserRoleRn_Type = SnmpAdminString
_CfprApAaaUserRoleRn_Object = MibTableColumn
cfprApAaaUserRoleRn = _CfprApAaaUserRoleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56, 1, 3),
    _CfprApAaaUserRoleRn_Type()
)
cfprApAaaUserRoleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserRoleRn.setStatus("current")
_CfprApAaaUserRoleConfigState_Type = CfprApAaaConfigState
_CfprApAaaUserRoleConfigState_Object = MibTableColumn
cfprApAaaUserRoleConfigState = _CfprApAaaUserRoleConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56, 1, 4),
    _CfprApAaaUserRoleConfigState_Type()
)
cfprApAaaUserRoleConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserRoleConfigState.setStatus("current")
_CfprApAaaUserRoleConfigStatusMessage_Type = SnmpAdminString
_CfprApAaaUserRoleConfigStatusMessage_Object = MibTableColumn
cfprApAaaUserRoleConfigStatusMessage = _CfprApAaaUserRoleConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56, 1, 5),
    _CfprApAaaUserRoleConfigStatusMessage_Type()
)
cfprApAaaUserRoleConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserRoleConfigStatusMessage.setStatus("current")
_CfprApAaaUserRoleDescr_Type = SnmpAdminString
_CfprApAaaUserRoleDescr_Object = MibTableColumn
cfprApAaaUserRoleDescr = _CfprApAaaUserRoleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56, 1, 6),
    _CfprApAaaUserRoleDescr_Type()
)
cfprApAaaUserRoleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserRoleDescr.setStatus("current")
_CfprApAaaUserRoleName_Type = SnmpAdminString
_CfprApAaaUserRoleName_Object = MibTableColumn
cfprApAaaUserRoleName = _CfprApAaaUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 56, 1, 7),
    _CfprApAaaUserRoleName_Type()
)
cfprApAaaUserRoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaUserRoleName.setStatus("current")
_CfprApAaaWebLoginTable_Object = MibTable
cfprApAaaWebLoginTable = _CfprApAaaWebLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57)
)
if mibBuilder.loadTexts:
    cfprApAaaWebLoginTable.setStatus("current")
_CfprApAaaWebLoginEntry_Object = MibTableRow
cfprApAaaWebLoginEntry = _CfprApAaaWebLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1)
)
cfprApAaaWebLoginEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-AAA-MIB", "cfprApAaaWebLoginInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApAaaWebLoginEntry.setStatus("current")
_CfprApAaaWebLoginInstanceId_Type = CfprApManagedObjectId
_CfprApAaaWebLoginInstanceId_Object = MibTableColumn
cfprApAaaWebLoginInstanceId = _CfprApAaaWebLoginInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 1),
    _CfprApAaaWebLoginInstanceId_Type()
)
cfprApAaaWebLoginInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginInstanceId.setStatus("current")
_CfprApAaaWebLoginDn_Type = CfprApManagedObjectDn
_CfprApAaaWebLoginDn_Object = MibTableColumn
cfprApAaaWebLoginDn = _CfprApAaaWebLoginDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 2),
    _CfprApAaaWebLoginDn_Type()
)
cfprApAaaWebLoginDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginDn.setStatus("current")
_CfprApAaaWebLoginRn_Type = SnmpAdminString
_CfprApAaaWebLoginRn_Object = MibTableColumn
cfprApAaaWebLoginRn = _CfprApAaaWebLoginRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 3),
    _CfprApAaaWebLoginRn_Type()
)
cfprApAaaWebLoginRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginRn.setStatus("current")
_CfprApAaaWebLoginDescr_Type = SnmpAdminString
_CfprApAaaWebLoginDescr_Object = MibTableColumn
cfprApAaaWebLoginDescr = _CfprApAaaWebLoginDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 4),
    _CfprApAaaWebLoginDescr_Type()
)
cfprApAaaWebLoginDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginDescr.setStatus("current")
_CfprApAaaWebLoginId_Type = SnmpAdminString
_CfprApAaaWebLoginId_Object = MibTableColumn
cfprApAaaWebLoginId = _CfprApAaaWebLoginId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 5),
    _CfprApAaaWebLoginId_Type()
)
cfprApAaaWebLoginId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginId.setStatus("current")
_CfprApAaaWebLoginIntId_Type = SnmpAdminString
_CfprApAaaWebLoginIntId_Object = MibTableColumn
cfprApAaaWebLoginIntId = _CfprApAaaWebLoginIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 6),
    _CfprApAaaWebLoginIntId_Type()
)
cfprApAaaWebLoginIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginIntId.setStatus("current")
_CfprApAaaWebLoginLocalHost_Type = SnmpAdminString
_CfprApAaaWebLoginLocalHost_Object = MibTableColumn
cfprApAaaWebLoginLocalHost = _CfprApAaaWebLoginLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 7),
    _CfprApAaaWebLoginLocalHost_Type()
)
cfprApAaaWebLoginLocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginLocalHost.setStatus("current")
_CfprApAaaWebLoginName_Type = SnmpAdminString
_CfprApAaaWebLoginName_Object = MibTableColumn
cfprApAaaWebLoginName = _CfprApAaaWebLoginName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 8),
    _CfprApAaaWebLoginName_Type()
)
cfprApAaaWebLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginName.setStatus("current")
_CfprApAaaWebLoginPolicyLevel_Type = Gauge32
_CfprApAaaWebLoginPolicyLevel_Object = MibTableColumn
cfprApAaaWebLoginPolicyLevel = _CfprApAaaWebLoginPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 9),
    _CfprApAaaWebLoginPolicyLevel_Type()
)
cfprApAaaWebLoginPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginPolicyLevel.setStatus("current")
_CfprApAaaWebLoginPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApAaaWebLoginPolicyOwner_Object = MibTableColumn
cfprApAaaWebLoginPolicyOwner = _CfprApAaaWebLoginPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 10),
    _CfprApAaaWebLoginPolicyOwner_Type()
)
cfprApAaaWebLoginPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginPolicyOwner.setStatus("current")
_CfprApAaaWebLoginRemoteHost_Type = SnmpAdminString
_CfprApAaaWebLoginRemoteHost_Object = MibTableColumn
cfprApAaaWebLoginRemoteHost = _CfprApAaaWebLoginRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 11),
    _CfprApAaaWebLoginRemoteHost_Type()
)
cfprApAaaWebLoginRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginRemoteHost.setStatus("current")
_CfprApAaaWebLoginSession_Type = CfprApAaaSession
_CfprApAaaWebLoginSession_Object = MibTableColumn
cfprApAaaWebLoginSession = _CfprApAaaWebLoginSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 12),
    _CfprApAaaWebLoginSession_Type()
)
cfprApAaaWebLoginSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginSession.setStatus("current")
_CfprApAaaWebLoginSwitchId_Type = CfprApNetworkSwitchId
_CfprApAaaWebLoginSwitchId_Object = MibTableColumn
cfprApAaaWebLoginSwitchId = _CfprApAaaWebLoginSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 2, 57, 1, 13),
    _CfprApAaaWebLoginSwitchId_Type()
)
cfprApAaaWebLoginSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApAaaWebLoginSwitchId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-AAA-MIB",
    **{"cfprApAaaObjects": cfprApAaaObjects,
       "cfprApAaaAuthRealmTable": cfprApAaaAuthRealmTable,
       "cfprApAaaAuthRealmEntry": cfprApAaaAuthRealmEntry,
       "cfprApAaaAuthRealmInstanceId": cfprApAaaAuthRealmInstanceId,
       "cfprApAaaAuthRealmDn": cfprApAaaAuthRealmDn,
       "cfprApAaaAuthRealmRn": cfprApAaaAuthRealmRn,
       "cfprApAaaAuthRealmConLogin": cfprApAaaAuthRealmConLogin,
       "cfprApAaaAuthRealmDefLogin": cfprApAaaAuthRealmDefLogin,
       "cfprApAaaAuthRealmDefRolePolicy": cfprApAaaAuthRealmDefRolePolicy,
       "cfprApAaaAuthRealmDescr": cfprApAaaAuthRealmDescr,
       "cfprApAaaAuthRealmFsmDescr": cfprApAaaAuthRealmFsmDescr,
       "cfprApAaaAuthRealmFsmPrev": cfprApAaaAuthRealmFsmPrev,
       "cfprApAaaAuthRealmFsmProgr": cfprApAaaAuthRealmFsmProgr,
       "cfprApAaaAuthRealmFsmRmtInvErrCode": cfprApAaaAuthRealmFsmRmtInvErrCode,
       "cfprApAaaAuthRealmFsmRmtInvErrDescr": cfprApAaaAuthRealmFsmRmtInvErrDescr,
       "cfprApAaaAuthRealmFsmRmtInvRslt": cfprApAaaAuthRealmFsmRmtInvRslt,
       "cfprApAaaAuthRealmFsmStageDescr": cfprApAaaAuthRealmFsmStageDescr,
       "cfprApAaaAuthRealmFsmStamp": cfprApAaaAuthRealmFsmStamp,
       "cfprApAaaAuthRealmFsmStatus": cfprApAaaAuthRealmFsmStatus,
       "cfprApAaaAuthRealmFsmTry": cfprApAaaAuthRealmFsmTry,
       "cfprApAaaAuthRealmIntId": cfprApAaaAuthRealmIntId,
       "cfprApAaaAuthRealmName": cfprApAaaAuthRealmName,
       "cfprApAaaAuthRealmPolicyLevel": cfprApAaaAuthRealmPolicyLevel,
       "cfprApAaaAuthRealmPolicyOwner": cfprApAaaAuthRealmPolicyOwner,
       "cfprApAaaAuthRealmFsmTable": cfprApAaaAuthRealmFsmTable,
       "cfprApAaaAuthRealmFsmEntry": cfprApAaaAuthRealmFsmEntry,
       "cfprApAaaAuthRealmFsmInstanceId": cfprApAaaAuthRealmFsmInstanceId,
       "cfprApAaaAuthRealmFsmDn": cfprApAaaAuthRealmFsmDn,
       "cfprApAaaAuthRealmFsmRn": cfprApAaaAuthRealmFsmRn,
       "cfprApAaaAuthRealmFsmCompletionTime": cfprApAaaAuthRealmFsmCompletionTime,
       "cfprApAaaAuthRealmFsmCurrentFsm": cfprApAaaAuthRealmFsmCurrentFsm,
       "cfprApAaaAuthRealmFsmDescrData": cfprApAaaAuthRealmFsmDescrData,
       "cfprApAaaAuthRealmFsmFsmStatus": cfprApAaaAuthRealmFsmFsmStatus,
       "cfprApAaaAuthRealmFsmProgress": cfprApAaaAuthRealmFsmProgress,
       "cfprApAaaAuthRealmFsmRmtErrCode": cfprApAaaAuthRealmFsmRmtErrCode,
       "cfprApAaaAuthRealmFsmRmtErrDescr": cfprApAaaAuthRealmFsmRmtErrDescr,
       "cfprApAaaAuthRealmFsmRmtRslt": cfprApAaaAuthRealmFsmRmtRslt,
       "cfprApAaaAuthRealmFsmStageTable": cfprApAaaAuthRealmFsmStageTable,
       "cfprApAaaAuthRealmFsmStageEntry": cfprApAaaAuthRealmFsmStageEntry,
       "cfprApAaaAuthRealmFsmStageInstanceId": cfprApAaaAuthRealmFsmStageInstanceId,
       "cfprApAaaAuthRealmFsmStageDn": cfprApAaaAuthRealmFsmStageDn,
       "cfprApAaaAuthRealmFsmStageRn": cfprApAaaAuthRealmFsmStageRn,
       "cfprApAaaAuthRealmFsmStageDescrData": cfprApAaaAuthRealmFsmStageDescrData,
       "cfprApAaaAuthRealmFsmStageLastUpdateTime": cfprApAaaAuthRealmFsmStageLastUpdateTime,
       "cfprApAaaAuthRealmFsmStageName": cfprApAaaAuthRealmFsmStageName,
       "cfprApAaaAuthRealmFsmStageOrder": cfprApAaaAuthRealmFsmStageOrder,
       "cfprApAaaAuthRealmFsmStageRetry": cfprApAaaAuthRealmFsmStageRetry,
       "cfprApAaaAuthRealmFsmStageStageStatus": cfprApAaaAuthRealmFsmStageStageStatus,
       "cfprApAaaCimcSessionTable": cfprApAaaCimcSessionTable,
       "cfprApAaaCimcSessionEntry": cfprApAaaCimcSessionEntry,
       "cfprApAaaCimcSessionInstanceId": cfprApAaaCimcSessionInstanceId,
       "cfprApAaaCimcSessionDn": cfprApAaaCimcSessionDn,
       "cfprApAaaCimcSessionRn": cfprApAaaCimcSessionRn,
       "cfprApAaaCimcSessionAdminState": cfprApAaaCimcSessionAdminState,
       "cfprApAaaCimcSessionCimcAddr": cfprApAaaCimcSessionCimcAddr,
       "cfprApAaaCimcSessionId": cfprApAaaCimcSessionId,
       "cfprApAaaCimcSessionIntDel": cfprApAaaCimcSessionIntDel,
       "cfprApAaaCimcSessionIsDelete": cfprApAaaCimcSessionIsDelete,
       "cfprApAaaCimcSessionLastUpdatedTime": cfprApAaaCimcSessionLastUpdatedTime,
       "cfprApAaaCimcSessionLoginTime": cfprApAaaCimcSessionLoginTime,
       "cfprApAaaCimcSessionLsDn": cfprApAaaCimcSessionLsDn,
       "cfprApAaaCimcSessionPid": cfprApAaaCimcSessionPid,
       "cfprApAaaCimcSessionPnDn": cfprApAaaCimcSessionPnDn,
       "cfprApAaaCimcSessionPriv": cfprApAaaCimcSessionPriv,
       "cfprApAaaCimcSessionSourceAddr": cfprApAaaCimcSessionSourceAddr,
       "cfprApAaaCimcSessionType": cfprApAaaCimcSessionType,
       "cfprApAaaCimcSessionUser": cfprApAaaCimcSessionUser,
       "cfprApAaaConsoleAuthTable": cfprApAaaConsoleAuthTable,
       "cfprApAaaConsoleAuthEntry": cfprApAaaConsoleAuthEntry,
       "cfprApAaaConsoleAuthInstanceId": cfprApAaaConsoleAuthInstanceId,
       "cfprApAaaConsoleAuthDn": cfprApAaaConsoleAuthDn,
       "cfprApAaaConsoleAuthRn": cfprApAaaConsoleAuthRn,
       "cfprApAaaConsoleAuthDescr": cfprApAaaConsoleAuthDescr,
       "cfprApAaaConsoleAuthName": cfprApAaaConsoleAuthName,
       "cfprApAaaConsoleAuthOperProviderGroup": cfprApAaaConsoleAuthOperProviderGroup,
       "cfprApAaaConsoleAuthOperRealm": cfprApAaaConsoleAuthOperRealm,
       "cfprApAaaConsoleAuthProviderGroup": cfprApAaaConsoleAuthProviderGroup,
       "cfprApAaaConsoleAuthRealm": cfprApAaaConsoleAuthRealm,
       "cfprApAaaConsoleAuthUse2Factor": cfprApAaaConsoleAuthUse2Factor,
       "cfprApAaaDefaultAuthTable": cfprApAaaDefaultAuthTable,
       "cfprApAaaDefaultAuthEntry": cfprApAaaDefaultAuthEntry,
       "cfprApAaaDefaultAuthInstanceId": cfprApAaaDefaultAuthInstanceId,
       "cfprApAaaDefaultAuthDn": cfprApAaaDefaultAuthDn,
       "cfprApAaaDefaultAuthRn": cfprApAaaDefaultAuthRn,
       "cfprApAaaDefaultAuthDescr": cfprApAaaDefaultAuthDescr,
       "cfprApAaaDefaultAuthName": cfprApAaaDefaultAuthName,
       "cfprApAaaDefaultAuthOperProviderGroup": cfprApAaaDefaultAuthOperProviderGroup,
       "cfprApAaaDefaultAuthOperRealm": cfprApAaaDefaultAuthOperRealm,
       "cfprApAaaDefaultAuthProviderGroup": cfprApAaaDefaultAuthProviderGroup,
       "cfprApAaaDefaultAuthRealm": cfprApAaaDefaultAuthRealm,
       "cfprApAaaDefaultAuthRefreshPeriod": cfprApAaaDefaultAuthRefreshPeriod,
       "cfprApAaaDefaultAuthSessionTimeout": cfprApAaaDefaultAuthSessionTimeout,
       "cfprApAaaDefaultAuthUse2Factor": cfprApAaaDefaultAuthUse2Factor,
       "cfprApAaaDomainTable": cfprApAaaDomainTable,
       "cfprApAaaDomainEntry": cfprApAaaDomainEntry,
       "cfprApAaaDomainInstanceId": cfprApAaaDomainInstanceId,
       "cfprApAaaDomainDn": cfprApAaaDomainDn,
       "cfprApAaaDomainRn": cfprApAaaDomainRn,
       "cfprApAaaDomainDescr": cfprApAaaDomainDescr,
       "cfprApAaaDomainName": cfprApAaaDomainName,
       "cfprApAaaDomainRefreshPeriod": cfprApAaaDomainRefreshPeriod,
       "cfprApAaaDomainSessionTimeout": cfprApAaaDomainSessionTimeout,
       "cfprApAaaDomainAuthTable": cfprApAaaDomainAuthTable,
       "cfprApAaaDomainAuthEntry": cfprApAaaDomainAuthEntry,
       "cfprApAaaDomainAuthInstanceId": cfprApAaaDomainAuthInstanceId,
       "cfprApAaaDomainAuthDn": cfprApAaaDomainAuthDn,
       "cfprApAaaDomainAuthRn": cfprApAaaDomainAuthRn,
       "cfprApAaaDomainAuthDescr": cfprApAaaDomainAuthDescr,
       "cfprApAaaDomainAuthName": cfprApAaaDomainAuthName,
       "cfprApAaaDomainAuthOperProviderGroup": cfprApAaaDomainAuthOperProviderGroup,
       "cfprApAaaDomainAuthOperRealm": cfprApAaaDomainAuthOperRealm,
       "cfprApAaaDomainAuthProviderGroup": cfprApAaaDomainAuthProviderGroup,
       "cfprApAaaDomainAuthRealm": cfprApAaaDomainAuthRealm,
       "cfprApAaaDomainAuthUse2Factor": cfprApAaaDomainAuthUse2Factor,
       "cfprApAaaEpAuthProfileTable": cfprApAaaEpAuthProfileTable,
       "cfprApAaaEpAuthProfileEntry": cfprApAaaEpAuthProfileEntry,
       "cfprApAaaEpAuthProfileInstanceId": cfprApAaaEpAuthProfileInstanceId,
       "cfprApAaaEpAuthProfileDn": cfprApAaaEpAuthProfileDn,
       "cfprApAaaEpAuthProfileRn": cfprApAaaEpAuthProfileRn,
       "cfprApAaaEpAuthProfileDescr": cfprApAaaEpAuthProfileDescr,
       "cfprApAaaEpAuthProfileIntId": cfprApAaaEpAuthProfileIntId,
       "cfprApAaaEpAuthProfileIpmiOverLan": cfprApAaaEpAuthProfileIpmiOverLan,
       "cfprApAaaEpAuthProfileName": cfprApAaaEpAuthProfileName,
       "cfprApAaaEpAuthProfilePolicyLevel": cfprApAaaEpAuthProfilePolicyLevel,
       "cfprApAaaEpAuthProfilePolicyOwner": cfprApAaaEpAuthProfilePolicyOwner,
       "cfprApAaaEpFsmTable": cfprApAaaEpFsmTable,
       "cfprApAaaEpFsmEntry": cfprApAaaEpFsmEntry,
       "cfprApAaaEpFsmInstanceId": cfprApAaaEpFsmInstanceId,
       "cfprApAaaEpFsmDn": cfprApAaaEpFsmDn,
       "cfprApAaaEpFsmRn": cfprApAaaEpFsmRn,
       "cfprApAaaEpFsmCompletionTime": cfprApAaaEpFsmCompletionTime,
       "cfprApAaaEpFsmCurrentFsm": cfprApAaaEpFsmCurrentFsm,
       "cfprApAaaEpFsmDescr": cfprApAaaEpFsmDescr,
       "cfprApAaaEpFsmFsmStatus": cfprApAaaEpFsmFsmStatus,
       "cfprApAaaEpFsmProgress": cfprApAaaEpFsmProgress,
       "cfprApAaaEpFsmRmtErrCode": cfprApAaaEpFsmRmtErrCode,
       "cfprApAaaEpFsmRmtErrDescr": cfprApAaaEpFsmRmtErrDescr,
       "cfprApAaaEpFsmRmtRslt": cfprApAaaEpFsmRmtRslt,
       "cfprApAaaEpFsmStageTable": cfprApAaaEpFsmStageTable,
       "cfprApAaaEpFsmStageEntry": cfprApAaaEpFsmStageEntry,
       "cfprApAaaEpFsmStageInstanceId": cfprApAaaEpFsmStageInstanceId,
       "cfprApAaaEpFsmStageDn": cfprApAaaEpFsmStageDn,
       "cfprApAaaEpFsmStageRn": cfprApAaaEpFsmStageRn,
       "cfprApAaaEpFsmStageDescr": cfprApAaaEpFsmStageDescr,
       "cfprApAaaEpFsmStageLastUpdateTime": cfprApAaaEpFsmStageLastUpdateTime,
       "cfprApAaaEpFsmStageName": cfprApAaaEpFsmStageName,
       "cfprApAaaEpFsmStageOrder": cfprApAaaEpFsmStageOrder,
       "cfprApAaaEpFsmStageRetry": cfprApAaaEpFsmStageRetry,
       "cfprApAaaEpFsmStageStageStatus": cfprApAaaEpFsmStageStageStatus,
       "cfprApAaaEpFsmTaskTable": cfprApAaaEpFsmTaskTable,
       "cfprApAaaEpFsmTaskEntry": cfprApAaaEpFsmTaskEntry,
       "cfprApAaaEpFsmTaskInstanceId": cfprApAaaEpFsmTaskInstanceId,
       "cfprApAaaEpFsmTaskDn": cfprApAaaEpFsmTaskDn,
       "cfprApAaaEpFsmTaskRn": cfprApAaaEpFsmTaskRn,
       "cfprApAaaEpFsmTaskCompletion": cfprApAaaEpFsmTaskCompletion,
       "cfprApAaaEpFsmTaskFlags": cfprApAaaEpFsmTaskFlags,
       "cfprApAaaEpFsmTaskItem": cfprApAaaEpFsmTaskItem,
       "cfprApAaaEpFsmTaskSeqId": cfprApAaaEpFsmTaskSeqId,
       "cfprApAaaEpLoginTable": cfprApAaaEpLoginTable,
       "cfprApAaaEpLoginEntry": cfprApAaaEpLoginEntry,
       "cfprApAaaEpLoginInstanceId": cfprApAaaEpLoginInstanceId,
       "cfprApAaaEpLoginDn": cfprApAaaEpLoginDn,
       "cfprApAaaEpLoginRn": cfprApAaaEpLoginRn,
       "cfprApAaaEpLoginDescr": cfprApAaaEpLoginDescr,
       "cfprApAaaEpLoginId": cfprApAaaEpLoginId,
       "cfprApAaaEpLoginIntId": cfprApAaaEpLoginIntId,
       "cfprApAaaEpLoginLocalHost": cfprApAaaEpLoginLocalHost,
       "cfprApAaaEpLoginName": cfprApAaaEpLoginName,
       "cfprApAaaEpLoginPolicyLevel": cfprApAaaEpLoginPolicyLevel,
       "cfprApAaaEpLoginPolicyOwner": cfprApAaaEpLoginPolicyOwner,
       "cfprApAaaEpLoginRemoteHost": cfprApAaaEpLoginRemoteHost,
       "cfprApAaaEpLoginSession": cfprApAaaEpLoginSession,
       "cfprApAaaEpLoginSwitchId": cfprApAaaEpLoginSwitchId,
       "cfprApAaaEpUserTable": cfprApAaaEpUserTable,
       "cfprApAaaEpUserEntry": cfprApAaaEpUserEntry,
       "cfprApAaaEpUserInstanceId": cfprApAaaEpUserInstanceId,
       "cfprApAaaEpUserDn": cfprApAaaEpUserDn,
       "cfprApAaaEpUserRn": cfprApAaaEpUserRn,
       "cfprApAaaEpUserConfigState": cfprApAaaEpUserConfigState,
       "cfprApAaaEpUserConfigStatusMessage": cfprApAaaEpUserConfigStatusMessage,
       "cfprApAaaEpUserDescr": cfprApAaaEpUserDescr,
       "cfprApAaaEpUserName": cfprApAaaEpUserName,
       "cfprApAaaEpUserPriv": cfprApAaaEpUserPriv,
       "cfprApAaaEpUserPwd": cfprApAaaEpUserPwd,
       "cfprApAaaEpUserPwdSet": cfprApAaaEpUserPwdSet,
       "cfprApAaaExtMgmtCutThruTknTable": cfprApAaaExtMgmtCutThruTknTable,
       "cfprApAaaExtMgmtCutThruTknEntry": cfprApAaaExtMgmtCutThruTknEntry,
       "cfprApAaaExtMgmtCutThruTknInstanceId": cfprApAaaExtMgmtCutThruTknInstanceId,
       "cfprApAaaExtMgmtCutThruTknDn": cfprApAaaExtMgmtCutThruTknDn,
       "cfprApAaaExtMgmtCutThruTknRn": cfprApAaaExtMgmtCutThruTknRn,
       "cfprApAaaExtMgmtCutThruTknAuthDomain": cfprApAaaExtMgmtCutThruTknAuthDomain,
       "cfprApAaaExtMgmtCutThruTknAuthUser": cfprApAaaExtMgmtCutThruTknAuthUser,
       "cfprApAaaExtMgmtCutThruTknCreationTime": cfprApAaaExtMgmtCutThruTknCreationTime,
       "cfprApAaaExtMgmtCutThruTknDescr": cfprApAaaExtMgmtCutThruTknDescr,
       "cfprApAaaExtMgmtCutThruTknIntId": cfprApAaaExtMgmtCutThruTknIntId,
       "cfprApAaaExtMgmtCutThruTknLocales": cfprApAaaExtMgmtCutThruTknLocales,
       "cfprApAaaExtMgmtCutThruTknName": cfprApAaaExtMgmtCutThruTknName,
       "cfprApAaaExtMgmtCutThruTknPnDn": cfprApAaaExtMgmtCutThruTknPnDn,
       "cfprApAaaExtMgmtCutThruTknPolicyLevel": cfprApAaaExtMgmtCutThruTknPolicyLevel,
       "cfprApAaaExtMgmtCutThruTknPolicyOwner": cfprApAaaExtMgmtCutThruTknPolicyOwner,
       "cfprApAaaExtMgmtCutThruTknPriv": cfprApAaaExtMgmtCutThruTknPriv,
       "cfprApAaaExtMgmtCutThruTknRemote": cfprApAaaExtMgmtCutThruTknRemote,
       "cfprApAaaExtMgmtCutThruTknToken": cfprApAaaExtMgmtCutThruTknToken,
       "cfprApAaaExtMgmtCutThruTknType": cfprApAaaExtMgmtCutThruTknType,
       "cfprApAaaExtMgmtCutThruTknUser": cfprApAaaExtMgmtCutThruTknUser,
       "cfprApAaaLdapEpTable": cfprApAaaLdapEpTable,
       "cfprApAaaLdapEpEntry": cfprApAaaLdapEpEntry,
       "cfprApAaaLdapEpInstanceId": cfprApAaaLdapEpInstanceId,
       "cfprApAaaLdapEpDn": cfprApAaaLdapEpDn,
       "cfprApAaaLdapEpRn": cfprApAaaLdapEpRn,
       "cfprApAaaLdapEpAttribute": cfprApAaaLdapEpAttribute,
       "cfprApAaaLdapEpBasedn": cfprApAaaLdapEpBasedn,
       "cfprApAaaLdapEpDescr": cfprApAaaLdapEpDescr,
       "cfprApAaaLdapEpFilter": cfprApAaaLdapEpFilter,
       "cfprApAaaLdapEpFsmDescr": cfprApAaaLdapEpFsmDescr,
       "cfprApAaaLdapEpFsmPrev": cfprApAaaLdapEpFsmPrev,
       "cfprApAaaLdapEpFsmProgr": cfprApAaaLdapEpFsmProgr,
       "cfprApAaaLdapEpFsmRmtInvErrCode": cfprApAaaLdapEpFsmRmtInvErrCode,
       "cfprApAaaLdapEpFsmRmtInvErrDescr": cfprApAaaLdapEpFsmRmtInvErrDescr,
       "cfprApAaaLdapEpFsmRmtInvRslt": cfprApAaaLdapEpFsmRmtInvRslt,
       "cfprApAaaLdapEpFsmStageDescr": cfprApAaaLdapEpFsmStageDescr,
       "cfprApAaaLdapEpFsmStamp": cfprApAaaLdapEpFsmStamp,
       "cfprApAaaLdapEpFsmStatus": cfprApAaaLdapEpFsmStatus,
       "cfprApAaaLdapEpFsmTry": cfprApAaaLdapEpFsmTry,
       "cfprApAaaLdapEpIntId": cfprApAaaLdapEpIntId,
       "cfprApAaaLdapEpName": cfprApAaaLdapEpName,
       "cfprApAaaLdapEpPolicyLevel": cfprApAaaLdapEpPolicyLevel,
       "cfprApAaaLdapEpPolicyOwner": cfprApAaaLdapEpPolicyOwner,
       "cfprApAaaLdapEpRetries": cfprApAaaLdapEpRetries,
       "cfprApAaaLdapEpTimeout": cfprApAaaLdapEpTimeout,
       "cfprApAaaLdapEpFsmTable": cfprApAaaLdapEpFsmTable,
       "cfprApAaaLdapEpFsmEntry": cfprApAaaLdapEpFsmEntry,
       "cfprApAaaLdapEpFsmInstanceId": cfprApAaaLdapEpFsmInstanceId,
       "cfprApAaaLdapEpFsmDn": cfprApAaaLdapEpFsmDn,
       "cfprApAaaLdapEpFsmRn": cfprApAaaLdapEpFsmRn,
       "cfprApAaaLdapEpFsmCompletionTime": cfprApAaaLdapEpFsmCompletionTime,
       "cfprApAaaLdapEpFsmCurrentFsm": cfprApAaaLdapEpFsmCurrentFsm,
       "cfprApAaaLdapEpFsmDescrData": cfprApAaaLdapEpFsmDescrData,
       "cfprApAaaLdapEpFsmFsmStatus": cfprApAaaLdapEpFsmFsmStatus,
       "cfprApAaaLdapEpFsmProgress": cfprApAaaLdapEpFsmProgress,
       "cfprApAaaLdapEpFsmRmtErrCode": cfprApAaaLdapEpFsmRmtErrCode,
       "cfprApAaaLdapEpFsmRmtErrDescr": cfprApAaaLdapEpFsmRmtErrDescr,
       "cfprApAaaLdapEpFsmRmtRslt": cfprApAaaLdapEpFsmRmtRslt,
       "cfprApAaaLdapEpFsmStageTable": cfprApAaaLdapEpFsmStageTable,
       "cfprApAaaLdapEpFsmStageEntry": cfprApAaaLdapEpFsmStageEntry,
       "cfprApAaaLdapEpFsmStageInstanceId": cfprApAaaLdapEpFsmStageInstanceId,
       "cfprApAaaLdapEpFsmStageDn": cfprApAaaLdapEpFsmStageDn,
       "cfprApAaaLdapEpFsmStageRn": cfprApAaaLdapEpFsmStageRn,
       "cfprApAaaLdapEpFsmStageDescrData": cfprApAaaLdapEpFsmStageDescrData,
       "cfprApAaaLdapEpFsmStageLastUpdateTime": cfprApAaaLdapEpFsmStageLastUpdateTime,
       "cfprApAaaLdapEpFsmStageName": cfprApAaaLdapEpFsmStageName,
       "cfprApAaaLdapEpFsmStageOrder": cfprApAaaLdapEpFsmStageOrder,
       "cfprApAaaLdapEpFsmStageRetry": cfprApAaaLdapEpFsmStageRetry,
       "cfprApAaaLdapEpFsmStageStageStatus": cfprApAaaLdapEpFsmStageStageStatus,
       "cfprApAaaLdapGroupTable": cfprApAaaLdapGroupTable,
       "cfprApAaaLdapGroupEntry": cfprApAaaLdapGroupEntry,
       "cfprApAaaLdapGroupInstanceId": cfprApAaaLdapGroupInstanceId,
       "cfprApAaaLdapGroupDn": cfprApAaaLdapGroupDn,
       "cfprApAaaLdapGroupRn": cfprApAaaLdapGroupRn,
       "cfprApAaaLdapGroupDescr": cfprApAaaLdapGroupDescr,
       "cfprApAaaLdapGroupName": cfprApAaaLdapGroupName,
       "cfprApAaaLdapGroupRuleTable": cfprApAaaLdapGroupRuleTable,
       "cfprApAaaLdapGroupRuleEntry": cfprApAaaLdapGroupRuleEntry,
       "cfprApAaaLdapGroupRuleInstanceId": cfprApAaaLdapGroupRuleInstanceId,
       "cfprApAaaLdapGroupRuleDn": cfprApAaaLdapGroupRuleDn,
       "cfprApAaaLdapGroupRuleRn": cfprApAaaLdapGroupRuleRn,
       "cfprApAaaLdapGroupRuleAuthorization": cfprApAaaLdapGroupRuleAuthorization,
       "cfprApAaaLdapGroupRuleDescr": cfprApAaaLdapGroupRuleDescr,
       "cfprApAaaLdapGroupRuleName": cfprApAaaLdapGroupRuleName,
       "cfprApAaaLdapGroupRuleTargetAttr": cfprApAaaLdapGroupRuleTargetAttr,
       "cfprApAaaLdapGroupRuleTraversal": cfprApAaaLdapGroupRuleTraversal,
       "cfprApAaaLdapGroupRuleUsePrimaryGroup": cfprApAaaLdapGroupRuleUsePrimaryGroup,
       "cfprApAaaLdapProviderTable": cfprApAaaLdapProviderTable,
       "cfprApAaaLdapProviderEntry": cfprApAaaLdapProviderEntry,
       "cfprApAaaLdapProviderInstanceId": cfprApAaaLdapProviderInstanceId,
       "cfprApAaaLdapProviderDn": cfprApAaaLdapProviderDn,
       "cfprApAaaLdapProviderRn": cfprApAaaLdapProviderRn,
       "cfprApAaaLdapProviderAttribute": cfprApAaaLdapProviderAttribute,
       "cfprApAaaLdapProviderBasedn": cfprApAaaLdapProviderBasedn,
       "cfprApAaaLdapProviderDescr": cfprApAaaLdapProviderDescr,
       "cfprApAaaLdapProviderEnableSSL": cfprApAaaLdapProviderEnableSSL,
       "cfprApAaaLdapProviderEncKey": cfprApAaaLdapProviderEncKey,
       "cfprApAaaLdapProviderFilter": cfprApAaaLdapProviderFilter,
       "cfprApAaaLdapProviderKey": cfprApAaaLdapProviderKey,
       "cfprApAaaLdapProviderKeySet": cfprApAaaLdapProviderKeySet,
       "cfprApAaaLdapProviderName": cfprApAaaLdapProviderName,
       "cfprApAaaLdapProviderOrder": cfprApAaaLdapProviderOrder,
       "cfprApAaaLdapProviderPort": cfprApAaaLdapProviderPort,
       "cfprApAaaLdapProviderRetries": cfprApAaaLdapProviderRetries,
       "cfprApAaaLdapProviderRootdn": cfprApAaaLdapProviderRootdn,
       "cfprApAaaLdapProviderTimeout": cfprApAaaLdapProviderTimeout,
       "cfprApAaaLdapProviderVendor": cfprApAaaLdapProviderVendor,
       "cfprApAaaLocaleTable": cfprApAaaLocaleTable,
       "cfprApAaaLocaleEntry": cfprApAaaLocaleEntry,
       "cfprApAaaLocaleInstanceId": cfprApAaaLocaleInstanceId,
       "cfprApAaaLocaleDn": cfprApAaaLocaleDn,
       "cfprApAaaLocaleRn": cfprApAaaLocaleRn,
       "cfprApAaaLocaleConfigState": cfprApAaaLocaleConfigState,
       "cfprApAaaLocaleConfigStatusMessage": cfprApAaaLocaleConfigStatusMessage,
       "cfprApAaaLocaleDescr": cfprApAaaLocaleDescr,
       "cfprApAaaLocaleIntId": cfprApAaaLocaleIntId,
       "cfprApAaaLocaleName": cfprApAaaLocaleName,
       "cfprApAaaLocalePolicyLevel": cfprApAaaLocalePolicyLevel,
       "cfprApAaaLocalePolicyOwner": cfprApAaaLocalePolicyOwner,
       "cfprApAaaLogTable": cfprApAaaLogTable,
       "cfprApAaaLogEntry": cfprApAaaLogEntry,
       "cfprApAaaLogInstanceId": cfprApAaaLogInstanceId,
       "cfprApAaaLogDn": cfprApAaaLogDn,
       "cfprApAaaLogRn": cfprApAaaLogRn,
       "cfprApAaaLogMaxSize": cfprApAaaLogMaxSize,
       "cfprApAaaLogPurgeWindow": cfprApAaaLogPurgeWindow,
       "cfprApAaaLogSize": cfprApAaaLogSize,
       "cfprApAaaModLRTable": cfprApAaaModLRTable,
       "cfprApAaaModLREntry": cfprApAaaModLREntry,
       "cfprApAaaModLRInstanceId": cfprApAaaModLRInstanceId,
       "cfprApAaaModLRDn": cfprApAaaModLRDn,
       "cfprApAaaModLRRn": cfprApAaaModLRRn,
       "cfprApAaaModLRAffected": cfprApAaaModLRAffected,
       "cfprApAaaModLRCause": cfprApAaaModLRCause,
       "cfprApAaaModLRChangeSet": cfprApAaaModLRChangeSet,
       "cfprApAaaModLRCode": cfprApAaaModLRCode,
       "cfprApAaaModLRCreated": cfprApAaaModLRCreated,
       "cfprApAaaModLRDescr": cfprApAaaModLRDescr,
       "cfprApAaaModLRId": cfprApAaaModLRId,
       "cfprApAaaModLRInd": cfprApAaaModLRInd,
       "cfprApAaaModLRSessionId": cfprApAaaModLRSessionId,
       "cfprApAaaModLRSeverity": cfprApAaaModLRSeverity,
       "cfprApAaaModLRTrig": cfprApAaaModLRTrig,
       "cfprApAaaModLRTxId": cfprApAaaModLRTxId,
       "cfprApAaaModLRUser": cfprApAaaModLRUser,
       "cfprApAaaOrgTable": cfprApAaaOrgTable,
       "cfprApAaaOrgEntry": cfprApAaaOrgEntry,
       "cfprApAaaOrgInstanceId": cfprApAaaOrgInstanceId,
       "cfprApAaaOrgDn": cfprApAaaOrgDn,
       "cfprApAaaOrgRn": cfprApAaaOrgRn,
       "cfprApAaaOrgConfigState": cfprApAaaOrgConfigState,
       "cfprApAaaOrgConfigStatusMessage": cfprApAaaOrgConfigStatusMessage,
       "cfprApAaaOrgDescr": cfprApAaaOrgDescr,
       "cfprApAaaOrgName": cfprApAaaOrgName,
       "cfprApAaaOrgOrgDn": cfprApAaaOrgOrgDn,
       "cfprApAaaPreLoginBannerTable": cfprApAaaPreLoginBannerTable,
       "cfprApAaaPreLoginBannerEntry": cfprApAaaPreLoginBannerEntry,
       "cfprApAaaPreLoginBannerInstanceId": cfprApAaaPreLoginBannerInstanceId,
       "cfprApAaaPreLoginBannerDn": cfprApAaaPreLoginBannerDn,
       "cfprApAaaPreLoginBannerRn": cfprApAaaPreLoginBannerRn,
       "cfprApAaaPreLoginBannerDescr": cfprApAaaPreLoginBannerDescr,
       "cfprApAaaPreLoginBannerIntId": cfprApAaaPreLoginBannerIntId,
       "cfprApAaaPreLoginBannerMessage": cfprApAaaPreLoginBannerMessage,
       "cfprApAaaPreLoginBannerName": cfprApAaaPreLoginBannerName,
       "cfprApAaaPreLoginBannerPolicyLevel": cfprApAaaPreLoginBannerPolicyLevel,
       "cfprApAaaPreLoginBannerPolicyOwner": cfprApAaaPreLoginBannerPolicyOwner,
       "cfprApAaaProviderGroupTable": cfprApAaaProviderGroupTable,
       "cfprApAaaProviderGroupEntry": cfprApAaaProviderGroupEntry,
       "cfprApAaaProviderGroupInstanceId": cfprApAaaProviderGroupInstanceId,
       "cfprApAaaProviderGroupDn": cfprApAaaProviderGroupDn,
       "cfprApAaaProviderGroupRn": cfprApAaaProviderGroupRn,
       "cfprApAaaProviderGroupConfigState": cfprApAaaProviderGroupConfigState,
       "cfprApAaaProviderGroupDescr": cfprApAaaProviderGroupDescr,
       "cfprApAaaProviderGroupName": cfprApAaaProviderGroupName,
       "cfprApAaaProviderGroupSize": cfprApAaaProviderGroupSize,
       "cfprApAaaProviderRefTable": cfprApAaaProviderRefTable,
       "cfprApAaaProviderRefEntry": cfprApAaaProviderRefEntry,
       "cfprApAaaProviderRefInstanceId": cfprApAaaProviderRefInstanceId,
       "cfprApAaaProviderRefDn": cfprApAaaProviderRefDn,
       "cfprApAaaProviderRefRn": cfprApAaaProviderRefRn,
       "cfprApAaaProviderRefDescr": cfprApAaaProviderRefDescr,
       "cfprApAaaProviderRefName": cfprApAaaProviderRefName,
       "cfprApAaaProviderRefOrder": cfprApAaaProviderRefOrder,
       "cfprApAaaPwdProfileTable": cfprApAaaPwdProfileTable,
       "cfprApAaaPwdProfileEntry": cfprApAaaPwdProfileEntry,
       "cfprApAaaPwdProfileInstanceId": cfprApAaaPwdProfileInstanceId,
       "cfprApAaaPwdProfileDn": cfprApAaaPwdProfileDn,
       "cfprApAaaPwdProfileRn": cfprApAaaPwdProfileRn,
       "cfprApAaaPwdProfileChangeCount": cfprApAaaPwdProfileChangeCount,
       "cfprApAaaPwdProfileChangeDuringInterval": cfprApAaaPwdProfileChangeDuringInterval,
       "cfprApAaaPwdProfileChangeInterval": cfprApAaaPwdProfileChangeInterval,
       "cfprApAaaPwdProfileExpirationWarnTime": cfprApAaaPwdProfileExpirationWarnTime,
       "cfprApAaaPwdProfileHistoryCount": cfprApAaaPwdProfileHistoryCount,
       "cfprApAaaPwdProfileNoChangeInterval": cfprApAaaPwdProfileNoChangeInterval,
       "cfprApAaaRadiusEpTable": cfprApAaaRadiusEpTable,
       "cfprApAaaRadiusEpEntry": cfprApAaaRadiusEpEntry,
       "cfprApAaaRadiusEpInstanceId": cfprApAaaRadiusEpInstanceId,
       "cfprApAaaRadiusEpDn": cfprApAaaRadiusEpDn,
       "cfprApAaaRadiusEpRn": cfprApAaaRadiusEpRn,
       "cfprApAaaRadiusEpDescr": cfprApAaaRadiusEpDescr,
       "cfprApAaaRadiusEpFsmDescr": cfprApAaaRadiusEpFsmDescr,
       "cfprApAaaRadiusEpFsmPrev": cfprApAaaRadiusEpFsmPrev,
       "cfprApAaaRadiusEpFsmProgr": cfprApAaaRadiusEpFsmProgr,
       "cfprApAaaRadiusEpFsmRmtInvErrCode": cfprApAaaRadiusEpFsmRmtInvErrCode,
       "cfprApAaaRadiusEpFsmRmtInvErrDescr": cfprApAaaRadiusEpFsmRmtInvErrDescr,
       "cfprApAaaRadiusEpFsmRmtInvRslt": cfprApAaaRadiusEpFsmRmtInvRslt,
       "cfprApAaaRadiusEpFsmStageDescr": cfprApAaaRadiusEpFsmStageDescr,
       "cfprApAaaRadiusEpFsmStamp": cfprApAaaRadiusEpFsmStamp,
       "cfprApAaaRadiusEpFsmStatus": cfprApAaaRadiusEpFsmStatus,
       "cfprApAaaRadiusEpFsmTry": cfprApAaaRadiusEpFsmTry,
       "cfprApAaaRadiusEpIntId": cfprApAaaRadiusEpIntId,
       "cfprApAaaRadiusEpName": cfprApAaaRadiusEpName,
       "cfprApAaaRadiusEpPolicyLevel": cfprApAaaRadiusEpPolicyLevel,
       "cfprApAaaRadiusEpPolicyOwner": cfprApAaaRadiusEpPolicyOwner,
       "cfprApAaaRadiusEpRetries": cfprApAaaRadiusEpRetries,
       "cfprApAaaRadiusEpTimeout": cfprApAaaRadiusEpTimeout,
       "cfprApAaaRadiusEpFsmTable": cfprApAaaRadiusEpFsmTable,
       "cfprApAaaRadiusEpFsmEntry": cfprApAaaRadiusEpFsmEntry,
       "cfprApAaaRadiusEpFsmInstanceId": cfprApAaaRadiusEpFsmInstanceId,
       "cfprApAaaRadiusEpFsmDn": cfprApAaaRadiusEpFsmDn,
       "cfprApAaaRadiusEpFsmRn": cfprApAaaRadiusEpFsmRn,
       "cfprApAaaRadiusEpFsmCompletionTime": cfprApAaaRadiusEpFsmCompletionTime,
       "cfprApAaaRadiusEpFsmCurrentFsm": cfprApAaaRadiusEpFsmCurrentFsm,
       "cfprApAaaRadiusEpFsmDescrData": cfprApAaaRadiusEpFsmDescrData,
       "cfprApAaaRadiusEpFsmFsmStatus": cfprApAaaRadiusEpFsmFsmStatus,
       "cfprApAaaRadiusEpFsmProgress": cfprApAaaRadiusEpFsmProgress,
       "cfprApAaaRadiusEpFsmRmtErrCode": cfprApAaaRadiusEpFsmRmtErrCode,
       "cfprApAaaRadiusEpFsmRmtErrDescr": cfprApAaaRadiusEpFsmRmtErrDescr,
       "cfprApAaaRadiusEpFsmRmtRslt": cfprApAaaRadiusEpFsmRmtRslt,
       "cfprApAaaRadiusEpFsmStageTable": cfprApAaaRadiusEpFsmStageTable,
       "cfprApAaaRadiusEpFsmStageEntry": cfprApAaaRadiusEpFsmStageEntry,
       "cfprApAaaRadiusEpFsmStageInstanceId": cfprApAaaRadiusEpFsmStageInstanceId,
       "cfprApAaaRadiusEpFsmStageDn": cfprApAaaRadiusEpFsmStageDn,
       "cfprApAaaRadiusEpFsmStageRn": cfprApAaaRadiusEpFsmStageRn,
       "cfprApAaaRadiusEpFsmStageDescrData": cfprApAaaRadiusEpFsmStageDescrData,
       "cfprApAaaRadiusEpFsmStageLastUpdateTime": cfprApAaaRadiusEpFsmStageLastUpdateTime,
       "cfprApAaaRadiusEpFsmStageName": cfprApAaaRadiusEpFsmStageName,
       "cfprApAaaRadiusEpFsmStageOrder": cfprApAaaRadiusEpFsmStageOrder,
       "cfprApAaaRadiusEpFsmStageRetry": cfprApAaaRadiusEpFsmStageRetry,
       "cfprApAaaRadiusEpFsmStageStageStatus": cfprApAaaRadiusEpFsmStageStageStatus,
       "cfprApAaaRadiusProviderTable": cfprApAaaRadiusProviderTable,
       "cfprApAaaRadiusProviderEntry": cfprApAaaRadiusProviderEntry,
       "cfprApAaaRadiusProviderInstanceId": cfprApAaaRadiusProviderInstanceId,
       "cfprApAaaRadiusProviderDn": cfprApAaaRadiusProviderDn,
       "cfprApAaaRadiusProviderRn": cfprApAaaRadiusProviderRn,
       "cfprApAaaRadiusProviderAuthPort": cfprApAaaRadiusProviderAuthPort,
       "cfprApAaaRadiusProviderDescr": cfprApAaaRadiusProviderDescr,
       "cfprApAaaRadiusProviderEncKey": cfprApAaaRadiusProviderEncKey,
       "cfprApAaaRadiusProviderKey": cfprApAaaRadiusProviderKey,
       "cfprApAaaRadiusProviderKeySet": cfprApAaaRadiusProviderKeySet,
       "cfprApAaaRadiusProviderName": cfprApAaaRadiusProviderName,
       "cfprApAaaRadiusProviderOrder": cfprApAaaRadiusProviderOrder,
       "cfprApAaaRadiusProviderRetries": cfprApAaaRadiusProviderRetries,
       "cfprApAaaRadiusProviderService": cfprApAaaRadiusProviderService,
       "cfprApAaaRadiusProviderTimeout": cfprApAaaRadiusProviderTimeout,
       "cfprApAaaRealmFsmTable": cfprApAaaRealmFsmTable,
       "cfprApAaaRealmFsmEntry": cfprApAaaRealmFsmEntry,
       "cfprApAaaRealmFsmInstanceId": cfprApAaaRealmFsmInstanceId,
       "cfprApAaaRealmFsmDn": cfprApAaaRealmFsmDn,
       "cfprApAaaRealmFsmRn": cfprApAaaRealmFsmRn,
       "cfprApAaaRealmFsmCompletionTime": cfprApAaaRealmFsmCompletionTime,
       "cfprApAaaRealmFsmCurrentFsm": cfprApAaaRealmFsmCurrentFsm,
       "cfprApAaaRealmFsmDescr": cfprApAaaRealmFsmDescr,
       "cfprApAaaRealmFsmFsmStatus": cfprApAaaRealmFsmFsmStatus,
       "cfprApAaaRealmFsmProgress": cfprApAaaRealmFsmProgress,
       "cfprApAaaRealmFsmRmtErrCode": cfprApAaaRealmFsmRmtErrCode,
       "cfprApAaaRealmFsmRmtErrDescr": cfprApAaaRealmFsmRmtErrDescr,
       "cfprApAaaRealmFsmRmtRslt": cfprApAaaRealmFsmRmtRslt,
       "cfprApAaaRealmFsmStageTable": cfprApAaaRealmFsmStageTable,
       "cfprApAaaRealmFsmStageEntry": cfprApAaaRealmFsmStageEntry,
       "cfprApAaaRealmFsmStageInstanceId": cfprApAaaRealmFsmStageInstanceId,
       "cfprApAaaRealmFsmStageDn": cfprApAaaRealmFsmStageDn,
       "cfprApAaaRealmFsmStageRn": cfprApAaaRealmFsmStageRn,
       "cfprApAaaRealmFsmStageDescr": cfprApAaaRealmFsmStageDescr,
       "cfprApAaaRealmFsmStageLastUpdateTime": cfprApAaaRealmFsmStageLastUpdateTime,
       "cfprApAaaRealmFsmStageName": cfprApAaaRealmFsmStageName,
       "cfprApAaaRealmFsmStageOrder": cfprApAaaRealmFsmStageOrder,
       "cfprApAaaRealmFsmStageRetry": cfprApAaaRealmFsmStageRetry,
       "cfprApAaaRealmFsmStageStageStatus": cfprApAaaRealmFsmStageStageStatus,
       "cfprApAaaRealmFsmTaskTable": cfprApAaaRealmFsmTaskTable,
       "cfprApAaaRealmFsmTaskEntry": cfprApAaaRealmFsmTaskEntry,
       "cfprApAaaRealmFsmTaskInstanceId": cfprApAaaRealmFsmTaskInstanceId,
       "cfprApAaaRealmFsmTaskDn": cfprApAaaRealmFsmTaskDn,
       "cfprApAaaRealmFsmTaskRn": cfprApAaaRealmFsmTaskRn,
       "cfprApAaaRealmFsmTaskCompletion": cfprApAaaRealmFsmTaskCompletion,
       "cfprApAaaRealmFsmTaskFlags": cfprApAaaRealmFsmTaskFlags,
       "cfprApAaaRealmFsmTaskItem": cfprApAaaRealmFsmTaskItem,
       "cfprApAaaRealmFsmTaskSeqId": cfprApAaaRealmFsmTaskSeqId,
       "cfprApAaaRemoteUserTable": cfprApAaaRemoteUserTable,
       "cfprApAaaRemoteUserEntry": cfprApAaaRemoteUserEntry,
       "cfprApAaaRemoteUserInstanceId": cfprApAaaRemoteUserInstanceId,
       "cfprApAaaRemoteUserDn": cfprApAaaRemoteUserDn,
       "cfprApAaaRemoteUserRn": cfprApAaaRemoteUserRn,
       "cfprApAaaRemoteUserConfigState": cfprApAaaRemoteUserConfigState,
       "cfprApAaaRemoteUserConfigStatusMessage": cfprApAaaRemoteUserConfigStatusMessage,
       "cfprApAaaRemoteUserDescr": cfprApAaaRemoteUserDescr,
       "cfprApAaaRemoteUserName": cfprApAaaRemoteUserName,
       "cfprApAaaRemoteUserPwd": cfprApAaaRemoteUserPwd,
       "cfprApAaaRemoteUserPwdSet": cfprApAaaRemoteUserPwdSet,
       "cfprApAaaRoleTable": cfprApAaaRoleTable,
       "cfprApAaaRoleEntry": cfprApAaaRoleEntry,
       "cfprApAaaRoleInstanceId": cfprApAaaRoleInstanceId,
       "cfprApAaaRoleDn": cfprApAaaRoleDn,
       "cfprApAaaRoleRn": cfprApAaaRoleRn,
       "cfprApAaaRoleConfigState": cfprApAaaRoleConfigState,
       "cfprApAaaRoleConfigStatusMessage": cfprApAaaRoleConfigStatusMessage,
       "cfprApAaaRoleDescr": cfprApAaaRoleDescr,
       "cfprApAaaRoleIntId": cfprApAaaRoleIntId,
       "cfprApAaaRoleName": cfprApAaaRoleName,
       "cfprApAaaRolePolicyLevel": cfprApAaaRolePolicyLevel,
       "cfprApAaaRolePolicyOwner": cfprApAaaRolePolicyOwner,
       "cfprApAaaRolePriv": cfprApAaaRolePriv,
       "cfprApAaaSessionTable": cfprApAaaSessionTable,
       "cfprApAaaSessionEntry": cfprApAaaSessionEntry,
       "cfprApAaaSessionInstanceId": cfprApAaaSessionInstanceId,
       "cfprApAaaSessionDn": cfprApAaaSessionDn,
       "cfprApAaaSessionRn": cfprApAaaSessionRn,
       "cfprApAaaSessionHost": cfprApAaaSessionHost,
       "cfprApAaaSessionId": cfprApAaaSessionId,
       "cfprApAaaSessionIntDel": cfprApAaaSessionIntDel,
       "cfprApAaaSessionLoginTime": cfprApAaaSessionLoginTime,
       "cfprApAaaSessionPid": cfprApAaaSessionPid,
       "cfprApAaaSessionRefreshPeriod": cfprApAaaSessionRefreshPeriod,
       "cfprApAaaSessionSessionTimeout": cfprApAaaSessionSessionTimeout,
       "cfprApAaaSessionSwitchId": cfprApAaaSessionSwitchId,
       "cfprApAaaSessionTerm": cfprApAaaSessionTerm,
       "cfprApAaaSessionUi": cfprApAaaSessionUi,
       "cfprApAaaSessionUser": cfprApAaaSessionUser,
       "cfprApAaaSessionInfoTable": cfprApAaaSessionInfoTable,
       "cfprApAaaSessionInfoEntry": cfprApAaaSessionInfoEntry,
       "cfprApAaaSessionInfoInstanceId": cfprApAaaSessionInfoInstanceId,
       "cfprApAaaSessionInfoDn": cfprApAaaSessionInfoDn,
       "cfprApAaaSessionInfoRn": cfprApAaaSessionInfoRn,
       "cfprApAaaSessionInfoAddress": cfprApAaaSessionInfoAddress,
       "cfprApAaaSessionInfoDestIp": cfprApAaaSessionInfoDestIp,
       "cfprApAaaSessionInfoEtime": cfprApAaaSessionInfoEtime,
       "cfprApAaaSessionInfoId": cfprApAaaSessionInfoId,
       "cfprApAaaSessionInfoPriv": cfprApAaaSessionInfoPriv,
       "cfprApAaaSessionInfoType": cfprApAaaSessionInfoType,
       "cfprApAaaSessionInfoUser": cfprApAaaSessionInfoUser,
       "cfprApAaaSessionInfoUserType": cfprApAaaSessionInfoUserType,
       "cfprApAaaSessionInfoTableTable": cfprApAaaSessionInfoTableTable,
       "cfprApAaaSessionInfoTableEntry": cfprApAaaSessionInfoTableEntry,
       "cfprApAaaSessionInfoTableInstanceId": cfprApAaaSessionInfoTableInstanceId,
       "cfprApAaaSessionInfoTableDn": cfprApAaaSessionInfoTableDn,
       "cfprApAaaSessionInfoTableRn": cfprApAaaSessionInfoTableRn,
       "cfprApAaaSessionLRTable": cfprApAaaSessionLRTable,
       "cfprApAaaSessionLREntry": cfprApAaaSessionLREntry,
       "cfprApAaaSessionLRInstanceId": cfprApAaaSessionLRInstanceId,
       "cfprApAaaSessionLRDn": cfprApAaaSessionLRDn,
       "cfprApAaaSessionLRRn": cfprApAaaSessionLRRn,
       "cfprApAaaSessionLRAffected": cfprApAaaSessionLRAffected,
       "cfprApAaaSessionLRCause": cfprApAaaSessionLRCause,
       "cfprApAaaSessionLRChangeSet": cfprApAaaSessionLRChangeSet,
       "cfprApAaaSessionLRCode": cfprApAaaSessionLRCode,
       "cfprApAaaSessionLRCreated": cfprApAaaSessionLRCreated,
       "cfprApAaaSessionLRDescr": cfprApAaaSessionLRDescr,
       "cfprApAaaSessionLRId": cfprApAaaSessionLRId,
       "cfprApAaaSessionLRInd": cfprApAaaSessionLRInd,
       "cfprApAaaSessionLRSessionId": cfprApAaaSessionLRSessionId,
       "cfprApAaaSessionLRSeverity": cfprApAaaSessionLRSeverity,
       "cfprApAaaSessionLRTrig": cfprApAaaSessionLRTrig,
       "cfprApAaaSessionLRTxId": cfprApAaaSessionLRTxId,
       "cfprApAaaSessionLRUser": cfprApAaaSessionLRUser,
       "cfprApAaaShellLoginTable": cfprApAaaShellLoginTable,
       "cfprApAaaShellLoginEntry": cfprApAaaShellLoginEntry,
       "cfprApAaaShellLoginInstanceId": cfprApAaaShellLoginInstanceId,
       "cfprApAaaShellLoginDn": cfprApAaaShellLoginDn,
       "cfprApAaaShellLoginRn": cfprApAaaShellLoginRn,
       "cfprApAaaShellLoginDescr": cfprApAaaShellLoginDescr,
       "cfprApAaaShellLoginId": cfprApAaaShellLoginId,
       "cfprApAaaShellLoginIntId": cfprApAaaShellLoginIntId,
       "cfprApAaaShellLoginLocalHost": cfprApAaaShellLoginLocalHost,
       "cfprApAaaShellLoginName": cfprApAaaShellLoginName,
       "cfprApAaaShellLoginPolicyLevel": cfprApAaaShellLoginPolicyLevel,
       "cfprApAaaShellLoginPolicyOwner": cfprApAaaShellLoginPolicyOwner,
       "cfprApAaaShellLoginRemoteHost": cfprApAaaShellLoginRemoteHost,
       "cfprApAaaShellLoginSession": cfprApAaaShellLoginSession,
       "cfprApAaaShellLoginSwitchId": cfprApAaaShellLoginSwitchId,
       "cfprApAaaSshAuthTable": cfprApAaaSshAuthTable,
       "cfprApAaaSshAuthEntry": cfprApAaaSshAuthEntry,
       "cfprApAaaSshAuthInstanceId": cfprApAaaSshAuthInstanceId,
       "cfprApAaaSshAuthDn": cfprApAaaSshAuthDn,
       "cfprApAaaSshAuthRn": cfprApAaaSshAuthRn,
       "cfprApAaaSshAuthData": cfprApAaaSshAuthData,
       "cfprApAaaSshAuthOldStrType": cfprApAaaSshAuthOldStrType,
       "cfprApAaaSshAuthStrType": cfprApAaaSshAuthStrType,
       "cfprApAaaTacacsPlusEpTable": cfprApAaaTacacsPlusEpTable,
       "cfprApAaaTacacsPlusEpEntry": cfprApAaaTacacsPlusEpEntry,
       "cfprApAaaTacacsPlusEpInstanceId": cfprApAaaTacacsPlusEpInstanceId,
       "cfprApAaaTacacsPlusEpDn": cfprApAaaTacacsPlusEpDn,
       "cfprApAaaTacacsPlusEpRn": cfprApAaaTacacsPlusEpRn,
       "cfprApAaaTacacsPlusEpDescr": cfprApAaaTacacsPlusEpDescr,
       "cfprApAaaTacacsPlusEpFsmDescr": cfprApAaaTacacsPlusEpFsmDescr,
       "cfprApAaaTacacsPlusEpFsmPrev": cfprApAaaTacacsPlusEpFsmPrev,
       "cfprApAaaTacacsPlusEpFsmProgr": cfprApAaaTacacsPlusEpFsmProgr,
       "cfprApAaaTacacsPlusEpFsmRmtInvErrCode": cfprApAaaTacacsPlusEpFsmRmtInvErrCode,
       "cfprApAaaTacacsPlusEpFsmRmtInvErrDescr": cfprApAaaTacacsPlusEpFsmRmtInvErrDescr,
       "cfprApAaaTacacsPlusEpFsmRmtInvRslt": cfprApAaaTacacsPlusEpFsmRmtInvRslt,
       "cfprApAaaTacacsPlusEpFsmStageDescr": cfprApAaaTacacsPlusEpFsmStageDescr,
       "cfprApAaaTacacsPlusEpFsmStamp": cfprApAaaTacacsPlusEpFsmStamp,
       "cfprApAaaTacacsPlusEpFsmStatus": cfprApAaaTacacsPlusEpFsmStatus,
       "cfprApAaaTacacsPlusEpFsmTry": cfprApAaaTacacsPlusEpFsmTry,
       "cfprApAaaTacacsPlusEpIntId": cfprApAaaTacacsPlusEpIntId,
       "cfprApAaaTacacsPlusEpName": cfprApAaaTacacsPlusEpName,
       "cfprApAaaTacacsPlusEpPolicyLevel": cfprApAaaTacacsPlusEpPolicyLevel,
       "cfprApAaaTacacsPlusEpPolicyOwner": cfprApAaaTacacsPlusEpPolicyOwner,
       "cfprApAaaTacacsPlusEpRetries": cfprApAaaTacacsPlusEpRetries,
       "cfprApAaaTacacsPlusEpTimeout": cfprApAaaTacacsPlusEpTimeout,
       "cfprApAaaTacacsPlusEpFsmTable": cfprApAaaTacacsPlusEpFsmTable,
       "cfprApAaaTacacsPlusEpFsmEntry": cfprApAaaTacacsPlusEpFsmEntry,
       "cfprApAaaTacacsPlusEpFsmInstanceId": cfprApAaaTacacsPlusEpFsmInstanceId,
       "cfprApAaaTacacsPlusEpFsmDn": cfprApAaaTacacsPlusEpFsmDn,
       "cfprApAaaTacacsPlusEpFsmRn": cfprApAaaTacacsPlusEpFsmRn,
       "cfprApAaaTacacsPlusEpFsmCompletionTime": cfprApAaaTacacsPlusEpFsmCompletionTime,
       "cfprApAaaTacacsPlusEpFsmCurrentFsm": cfprApAaaTacacsPlusEpFsmCurrentFsm,
       "cfprApAaaTacacsPlusEpFsmDescrData": cfprApAaaTacacsPlusEpFsmDescrData,
       "cfprApAaaTacacsPlusEpFsmFsmStatus": cfprApAaaTacacsPlusEpFsmFsmStatus,
       "cfprApAaaTacacsPlusEpFsmProgress": cfprApAaaTacacsPlusEpFsmProgress,
       "cfprApAaaTacacsPlusEpFsmRmtErrCode": cfprApAaaTacacsPlusEpFsmRmtErrCode,
       "cfprApAaaTacacsPlusEpFsmRmtErrDescr": cfprApAaaTacacsPlusEpFsmRmtErrDescr,
       "cfprApAaaTacacsPlusEpFsmRmtRslt": cfprApAaaTacacsPlusEpFsmRmtRslt,
       "cfprApAaaTacacsPlusEpFsmStageTable": cfprApAaaTacacsPlusEpFsmStageTable,
       "cfprApAaaTacacsPlusEpFsmStageEntry": cfprApAaaTacacsPlusEpFsmStageEntry,
       "cfprApAaaTacacsPlusEpFsmStageInstanceId": cfprApAaaTacacsPlusEpFsmStageInstanceId,
       "cfprApAaaTacacsPlusEpFsmStageDn": cfprApAaaTacacsPlusEpFsmStageDn,
       "cfprApAaaTacacsPlusEpFsmStageRn": cfprApAaaTacacsPlusEpFsmStageRn,
       "cfprApAaaTacacsPlusEpFsmStageDescrData": cfprApAaaTacacsPlusEpFsmStageDescrData,
       "cfprApAaaTacacsPlusEpFsmStageLastUpdateTime": cfprApAaaTacacsPlusEpFsmStageLastUpdateTime,
       "cfprApAaaTacacsPlusEpFsmStageName": cfprApAaaTacacsPlusEpFsmStageName,
       "cfprApAaaTacacsPlusEpFsmStageOrder": cfprApAaaTacacsPlusEpFsmStageOrder,
       "cfprApAaaTacacsPlusEpFsmStageRetry": cfprApAaaTacacsPlusEpFsmStageRetry,
       "cfprApAaaTacacsPlusEpFsmStageStageStatus": cfprApAaaTacacsPlusEpFsmStageStageStatus,
       "cfprApAaaTacacsPlusProviderTable": cfprApAaaTacacsPlusProviderTable,
       "cfprApAaaTacacsPlusProviderEntry": cfprApAaaTacacsPlusProviderEntry,
       "cfprApAaaTacacsPlusProviderInstanceId": cfprApAaaTacacsPlusProviderInstanceId,
       "cfprApAaaTacacsPlusProviderDn": cfprApAaaTacacsPlusProviderDn,
       "cfprApAaaTacacsPlusProviderRn": cfprApAaaTacacsPlusProviderRn,
       "cfprApAaaTacacsPlusProviderDescr": cfprApAaaTacacsPlusProviderDescr,
       "cfprApAaaTacacsPlusProviderEncKey": cfprApAaaTacacsPlusProviderEncKey,
       "cfprApAaaTacacsPlusProviderKey": cfprApAaaTacacsPlusProviderKey,
       "cfprApAaaTacacsPlusProviderKeySet": cfprApAaaTacacsPlusProviderKeySet,
       "cfprApAaaTacacsPlusProviderName": cfprApAaaTacacsPlusProviderName,
       "cfprApAaaTacacsPlusProviderOrder": cfprApAaaTacacsPlusProviderOrder,
       "cfprApAaaTacacsPlusProviderPort": cfprApAaaTacacsPlusProviderPort,
       "cfprApAaaTacacsPlusProviderRetries": cfprApAaaTacacsPlusProviderRetries,
       "cfprApAaaTacacsPlusProviderTimeout": cfprApAaaTacacsPlusProviderTimeout,
       "cfprApAaaUserTable": cfprApAaaUserTable,
       "cfprApAaaUserEntry": cfprApAaaUserEntry,
       "cfprApAaaUserInstanceId": cfprApAaaUserInstanceId,
       "cfprApAaaUserDn": cfprApAaaUserDn,
       "cfprApAaaUserRn": cfprApAaaUserRn,
       "cfprApAaaUserAccountStatus": cfprApAaaUserAccountStatus,
       "cfprApAaaUserClearPwdHistory": cfprApAaaUserClearPwdHistory,
       "cfprApAaaUserConfigState": cfprApAaaUserConfigState,
       "cfprApAaaUserConfigStatusMessage": cfprApAaaUserConfigStatusMessage,
       "cfprApAaaUserDescr": cfprApAaaUserDescr,
       "cfprApAaaUserEmail": cfprApAaaUserEmail,
       "cfprApAaaUserEncPwd": cfprApAaaUserEncPwd,
       "cfprApAaaUserEncPwdSet": cfprApAaaUserEncPwdSet,
       "cfprApAaaUserExpiration": cfprApAaaUserExpiration,
       "cfprApAaaUserExpires": cfprApAaaUserExpires,
       "cfprApAaaUserFirstName": cfprApAaaUserFirstName,
       "cfprApAaaUserLastName": cfprApAaaUserLastName,
       "cfprApAaaUserName": cfprApAaaUserName,
       "cfprApAaaUserPhone": cfprApAaaUserPhone,
       "cfprApAaaUserPriv": cfprApAaaUserPriv,
       "cfprApAaaUserPwd": cfprApAaaUserPwd,
       "cfprApAaaUserPwdSet": cfprApAaaUserPwdSet,
       "cfprApAaaUserDataTable": cfprApAaaUserDataTable,
       "cfprApAaaUserDataEntry": cfprApAaaUserDataEntry,
       "cfprApAaaUserDataInstanceId": cfprApAaaUserDataInstanceId,
       "cfprApAaaUserDataDn": cfprApAaaUserDataDn,
       "cfprApAaaUserDataRn": cfprApAaaUserDataRn,
       "cfprApAaaUserDataDescr": cfprApAaaUserDataDescr,
       "cfprApAaaUserDataIntId": cfprApAaaUserDataIntId,
       "cfprApAaaUserDataName": cfprApAaaUserDataName,
       "cfprApAaaUserDataPolicyLevel": cfprApAaaUserDataPolicyLevel,
       "cfprApAaaUserDataPolicyOwner": cfprApAaaUserDataPolicyOwner,
       "cfprApAaaUserDataPwdChangeCount": cfprApAaaUserDataPwdChangeCount,
       "cfprApAaaUserDataPwdChangeIntervalBegin": cfprApAaaUserDataPwdChangeIntervalBegin,
       "cfprApAaaUserDataPwdChangedDate": cfprApAaaUserDataPwdChangedDate,
       "cfprApAaaUserDataPwdHistory": cfprApAaaUserDataPwdHistory,
       "cfprApAaaUserEpTable": cfprApAaaUserEpTable,
       "cfprApAaaUserEpEntry": cfprApAaaUserEpEntry,
       "cfprApAaaUserEpInstanceId": cfprApAaaUserEpInstanceId,
       "cfprApAaaUserEpDn": cfprApAaaUserEpDn,
       "cfprApAaaUserEpRn": cfprApAaaUserEpRn,
       "cfprApAaaUserEpDescr": cfprApAaaUserEpDescr,
       "cfprApAaaUserEpFsmDescr": cfprApAaaUserEpFsmDescr,
       "cfprApAaaUserEpFsmPrev": cfprApAaaUserEpFsmPrev,
       "cfprApAaaUserEpFsmProgr": cfprApAaaUserEpFsmProgr,
       "cfprApAaaUserEpFsmRmtInvErrCode": cfprApAaaUserEpFsmRmtInvErrCode,
       "cfprApAaaUserEpFsmRmtInvErrDescr": cfprApAaaUserEpFsmRmtInvErrDescr,
       "cfprApAaaUserEpFsmRmtInvRslt": cfprApAaaUserEpFsmRmtInvRslt,
       "cfprApAaaUserEpFsmStageDescr": cfprApAaaUserEpFsmStageDescr,
       "cfprApAaaUserEpFsmStamp": cfprApAaaUserEpFsmStamp,
       "cfprApAaaUserEpFsmStatus": cfprApAaaUserEpFsmStatus,
       "cfprApAaaUserEpFsmTry": cfprApAaaUserEpFsmTry,
       "cfprApAaaUserEpIntId": cfprApAaaUserEpIntId,
       "cfprApAaaUserEpMaxLoginAttempts": cfprApAaaUserEpMaxLoginAttempts,
       "cfprApAaaUserEpMinPwdLength": cfprApAaaUserEpMinPwdLength,
       "cfprApAaaUserEpName": cfprApAaaUserEpName,
       "cfprApAaaUserEpPolicyLevel": cfprApAaaUserEpPolicyLevel,
       "cfprApAaaUserEpPolicyOwner": cfprApAaaUserEpPolicyOwner,
       "cfprApAaaUserEpPwdStrengthCheck": cfprApAaaUserEpPwdStrengthCheck,
       "cfprApAaaUserEpUserAccountUnlockTime": cfprApAaaUserEpUserAccountUnlockTime,
       "cfprApAaaUserEpFsmTable": cfprApAaaUserEpFsmTable,
       "cfprApAaaUserEpFsmEntry": cfprApAaaUserEpFsmEntry,
       "cfprApAaaUserEpFsmInstanceId": cfprApAaaUserEpFsmInstanceId,
       "cfprApAaaUserEpFsmDn": cfprApAaaUserEpFsmDn,
       "cfprApAaaUserEpFsmRn": cfprApAaaUserEpFsmRn,
       "cfprApAaaUserEpFsmCompletionTime": cfprApAaaUserEpFsmCompletionTime,
       "cfprApAaaUserEpFsmCurrentFsm": cfprApAaaUserEpFsmCurrentFsm,
       "cfprApAaaUserEpFsmDescrData": cfprApAaaUserEpFsmDescrData,
       "cfprApAaaUserEpFsmFsmStatus": cfprApAaaUserEpFsmFsmStatus,
       "cfprApAaaUserEpFsmProgress": cfprApAaaUserEpFsmProgress,
       "cfprApAaaUserEpFsmRmtErrCode": cfprApAaaUserEpFsmRmtErrCode,
       "cfprApAaaUserEpFsmRmtErrDescr": cfprApAaaUserEpFsmRmtErrDescr,
       "cfprApAaaUserEpFsmRmtRslt": cfprApAaaUserEpFsmRmtRslt,
       "cfprApAaaUserEpFsmStageTable": cfprApAaaUserEpFsmStageTable,
       "cfprApAaaUserEpFsmStageEntry": cfprApAaaUserEpFsmStageEntry,
       "cfprApAaaUserEpFsmStageInstanceId": cfprApAaaUserEpFsmStageInstanceId,
       "cfprApAaaUserEpFsmStageDn": cfprApAaaUserEpFsmStageDn,
       "cfprApAaaUserEpFsmStageRn": cfprApAaaUserEpFsmStageRn,
       "cfprApAaaUserEpFsmStageDescrData": cfprApAaaUserEpFsmStageDescrData,
       "cfprApAaaUserEpFsmStageLastUpdateTime": cfprApAaaUserEpFsmStageLastUpdateTime,
       "cfprApAaaUserEpFsmStageName": cfprApAaaUserEpFsmStageName,
       "cfprApAaaUserEpFsmStageOrder": cfprApAaaUserEpFsmStageOrder,
       "cfprApAaaUserEpFsmStageRetry": cfprApAaaUserEpFsmStageRetry,
       "cfprApAaaUserEpFsmStageStageStatus": cfprApAaaUserEpFsmStageStageStatus,
       "cfprApAaaUserEpFsmTaskTable": cfprApAaaUserEpFsmTaskTable,
       "cfprApAaaUserEpFsmTaskEntry": cfprApAaaUserEpFsmTaskEntry,
       "cfprApAaaUserEpFsmTaskInstanceId": cfprApAaaUserEpFsmTaskInstanceId,
       "cfprApAaaUserEpFsmTaskDn": cfprApAaaUserEpFsmTaskDn,
       "cfprApAaaUserEpFsmTaskRn": cfprApAaaUserEpFsmTaskRn,
       "cfprApAaaUserEpFsmTaskCompletion": cfprApAaaUserEpFsmTaskCompletion,
       "cfprApAaaUserEpFsmTaskFlags": cfprApAaaUserEpFsmTaskFlags,
       "cfprApAaaUserEpFsmTaskItem": cfprApAaaUserEpFsmTaskItem,
       "cfprApAaaUserEpFsmTaskSeqId": cfprApAaaUserEpFsmTaskSeqId,
       "cfprApAaaUserLocaleTable": cfprApAaaUserLocaleTable,
       "cfprApAaaUserLocaleEntry": cfprApAaaUserLocaleEntry,
       "cfprApAaaUserLocaleInstanceId": cfprApAaaUserLocaleInstanceId,
       "cfprApAaaUserLocaleDn": cfprApAaaUserLocaleDn,
       "cfprApAaaUserLocaleRn": cfprApAaaUserLocaleRn,
       "cfprApAaaUserLocaleConfigState": cfprApAaaUserLocaleConfigState,
       "cfprApAaaUserLocaleConfigStatusMessage": cfprApAaaUserLocaleConfigStatusMessage,
       "cfprApAaaUserLocaleDescr": cfprApAaaUserLocaleDescr,
       "cfprApAaaUserLocaleName": cfprApAaaUserLocaleName,
       "cfprApAaaUserRoleTable": cfprApAaaUserRoleTable,
       "cfprApAaaUserRoleEntry": cfprApAaaUserRoleEntry,
       "cfprApAaaUserRoleInstanceId": cfprApAaaUserRoleInstanceId,
       "cfprApAaaUserRoleDn": cfprApAaaUserRoleDn,
       "cfprApAaaUserRoleRn": cfprApAaaUserRoleRn,
       "cfprApAaaUserRoleConfigState": cfprApAaaUserRoleConfigState,
       "cfprApAaaUserRoleConfigStatusMessage": cfprApAaaUserRoleConfigStatusMessage,
       "cfprApAaaUserRoleDescr": cfprApAaaUserRoleDescr,
       "cfprApAaaUserRoleName": cfprApAaaUserRoleName,
       "cfprApAaaWebLoginTable": cfprApAaaWebLoginTable,
       "cfprApAaaWebLoginEntry": cfprApAaaWebLoginEntry,
       "cfprApAaaWebLoginInstanceId": cfprApAaaWebLoginInstanceId,
       "cfprApAaaWebLoginDn": cfprApAaaWebLoginDn,
       "cfprApAaaWebLoginRn": cfprApAaaWebLoginRn,
       "cfprApAaaWebLoginDescr": cfprApAaaWebLoginDescr,
       "cfprApAaaWebLoginId": cfprApAaaWebLoginId,
       "cfprApAaaWebLoginIntId": cfprApAaaWebLoginIntId,
       "cfprApAaaWebLoginLocalHost": cfprApAaaWebLoginLocalHost,
       "cfprApAaaWebLoginName": cfprApAaaWebLoginName,
       "cfprApAaaWebLoginPolicyLevel": cfprApAaaWebLoginPolicyLevel,
       "cfprApAaaWebLoginPolicyOwner": cfprApAaaWebLoginPolicyOwner,
       "cfprApAaaWebLoginRemoteHost": cfprApAaaWebLoginRemoteHost,
       "cfprApAaaWebLoginSession": cfprApAaaWebLoginSession,
       "cfprApAaaWebLoginSwitchId": cfprApAaaWebLoginSwitchId}
)
